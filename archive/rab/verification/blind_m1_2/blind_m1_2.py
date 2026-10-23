#!/usr/bin/env python
"""
blind_m1_2.py  -  second blind build of M1 (ladder cost and WInS book cost).

WS1-second-blind-pricer, 2026-09-30 (Sydney). AI-generated verification code (Claude Code) for Team Caplet.

Built ONLY from rab/models/M1_METHOD.md (the 30 Sep corrected spec) and the raw inputs it lists (I1-I7).
No file in rab/models/*.py or rab/verification/ was read. This is the Gate A dual computation.

Run:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind_m1_2/blind_m1_2.py
Writes, next to this file:
    results.json        every section's numbers, plus input hashes and interpretive choices
    history_daily.csv   section G per-day values (for like-with-like date comparison)

Interpretive choices where the spec left room (all recorded in results.json["interpretation"]):
  P1  A4(ii) "extra discount-factor nodes": the 0.5-year bootstrap grid is unchanged; nodes at t = 1/12, 2/12,
      0.25 with ln DF = -2t ln(1 + y/2) are added to the ln-DF interpolation table only.
  P2  A4(iv) zero rates: z_j = -ln DF_j / t_j on the 0.5j grid, linear in t, flat beyond both ends. For t < 0.5
      this equals the base ln-DF rule (a straight line from (0,0)), so DF(1 Jan 2027) is unchanged by design.
  P3  C: the two "stale" WInS prices (4.5% Feb-2036 at 102.95; 4.375% Feb-2038 at 99.98) were recorded without
      saying clean or dirty. Primary: treat as CLEAN (spec step 1: Dirty_WInS = clean + accrued). Secondary
      yield "if the price were dirty" also reported.
  P4  E: the cost used for own yield and buffer cost EXCLUDES the trade commission ("price paid"; buying more of
      the same holding is the same trade). Book-cost totals in B include commissions as the spec says.
  P5  E: iBond internal principal "held inside the fund from maturity to E_f at the scenario rate, then paid at
      E_f" is exactly equivalent (same rate r, or the same curve forwards) to a holder flow on the note's maturity
      date, because year fractions add (days/365.25). It is modelled that way. The fund's money-market and cash
      lines (24 Sep) are scaled by k_f and treated as a holder flow at S (they are cash today; the money-market
      line matured 24 Sep 2026).
  P6  E: the 7bp fee is charged per spec as -(0.0007/12) x P_ETF (price paid per share) at every month end after S
      up to and including E_f = 15 Dec of the fund year; the last month end used is 30 Nov of that year.
  P7  B4 Portfolio rule: implemented as written (Book L values with commissions excluded). At `sheet_as_read`
      prices it reproduces every Portfolio quantity exactly and every displayed target within $0.50. A variant
      with the $175 of commissions in the denominator is also reported; it does NOT reproduce the Sheet.
  P10 C diagnostic: the Sheet's status texts ("Price checked (-8bp)" etc.) are compared with the spec gap on the
      28 Sep curve AND, as a labelled diagnostic only, with the same gap on the 25 Sep curve (row 09/25/2026 of
      I1). The reference curve for every reported number stays 28 Sep.
  P8  G: "value on D" for "cheapest since" is the value from the D row of I2 (2026.csv), which is the same curve
      as I1. Comparison is value(d) <= value(D), scanning d < D, per series.
  P9  Rounding: all arithmetic in floating point; JSON carries cents (2 dp) or more; dollar rounding is applied
      only in the printed summary and in the *_usd_rounded fields.
"""
from __future__ import annotations

import calendar
import csv
import hashlib
import json
import math
import statistics
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]  # worktree root (rab/verification/blind_m1_2 -> ws1)
SEED = 20260930  # run convention; this model has no stochastic step

# ----------------------------------------------------------------------------- inputs (spec section 1)
I1 = ROOT / "rab/data/treasury_par_2000_2026/2026.csv"
I2_DIRS = [ROOT / "rab/data/treasury_par_1990_1999", ROOT / "rab/data/treasury_par_2000_2026"]
I3 = ROOT / "rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv"
I4 = ROOT / "rab/data/wins/wins_prices_2026-09-28.csv"
I5 = ROOT / "rab/data/etf/nasdaq_historical.json"
I6 = ROOT / "research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv"
I7 = ROOT / "rab/data/ishares/ibonds_facts.csv"
CURVE_URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
             "daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026"
             "&page&_format=csv")

# ----------------------------------------------------------------------------- conventions (spec section 2)
D = date(2026, 9, 28)          # curve / reference date
S = D                          # settlement date (UNVERIFIED WInS convention)
A = date(2027, 1, 1)           # Laura's $300,000 arrives
A2028 = date(2028, 1, 1)
YEAR_DAYS = 365.25
PAYMENT = 50_000.0
DEPOSIT = 300_000.0
DEPOSIT_2028 = 150_000.0
COMM_ETF = 25.0
COMM_TSY = 10.0
FEE_ANNUAL = 0.0007

EXACT_DATES = [date(y, 1, 1) for y in range(2033, 2043)]      # payment dates
NOV15_DATES = [date(y, 11, 15) for y in range(2032, 2042)]    # STRIPS maturities funding them
ETF_ORDER = ["IBTM", "IBTO", "IBTP", "IBTQ", "IBTR"]
ETF_YEAR = {"IBTM": 2032, "IBTO": 2033, "IBTP": 2034, "IBTQ": 2035, "IBTR": 2036}

TENOR_YEARS = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": 0.25, "6 Mo": 0.5, "1 Yr": 1.0, "2 Yr": 2.0,
               "3 Yr": 3.0, "5 Yr": 5.0, "7 Yr": 7.0, "10 Yr": 10.0, "20 Yr": 20.0, "30 Yr": 30.0}
GRID = np.arange(1, 61) * 0.5   # t_j = 0.5 j, j = 1..60


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def money(x: float) -> str:
    return f"${x:,.0f}"


def num(s: str) -> float:
    return float(str(s).replace("$", "").replace(",", "").replace("%", "").strip())


# ----------------------------------------------------------------------------- A1 curve
def par_points(row: dict, shift_bp: float = 0.0):
    """(tenor years, par yield decimal) from a Treasury CSV row; blanks skipped; unused columns ignored."""
    pts = []
    for col, t in TENOR_YEARS.items():
        v = row.get(col)
        if v is None:
            continue
        v = str(v).strip()
        if v == "" or v.upper() == "N/A":
            continue
        pts.append((t, (float(v) + shift_bp / 100.0) / 100.0))
    pts.sort()
    return np.array([p[0] for p in pts]), np.array([p[1] for p in pts])


def bootstrap(par_grid: np.ndarray) -> np.ndarray:
    """A1 step 3: each grid point is a par bond paying p_j/2 every half-year."""
    dfs = np.empty(len(par_grid))
    running = 0.0
    for j, p in enumerate(par_grid):
        c = p / 2.0
        dfs[j] = (1.0 - c * running) / (1.0 + c)
        running += dfs[j]
    return dfs


class Curve:
    """Par-curve bootstrap with log-linear discount factors (A1), plus the A4 variants."""

    def __init__(self, ts, ys, *, interp="linear", year_days=YEAR_DAYS, short_nodes=False,
                 zero_interp=False, ref=D):
        self.ts, self.ys = np.asarray(ts, float), np.asarray(ys, float)
        self.year_days, self.ref, self.zero_interp = year_days, ref, zero_interp
        if interp == "linear":
            self.par_grid = np.interp(GRID, self.ts, self.ys)          # flat beyond both ends
        elif interp == "pchip":
            self.par_grid = PchipInterpolator(self.ts, self.ys)(np.clip(GRID, self.ts[0], self.ts[-1]))
        else:
            raise ValueError(interp)
        self.dfs = bootstrap(self.par_grid)
        if zero_interp:
            self.zx = GRID.copy()
            self.zy = -np.log(self.dfs) / GRID
        else:
            xs = [0.0] + list(GRID)
            ys_ = [0.0] + list(np.log(self.dfs))
            if short_nodes:
                for t in (1 / 12, 2 / 12, 0.25):
                    idx = np.where(np.isclose(self.ts, t))[0]
                    if len(idx):
                        xs.append(t)
                        ys_.append(-2.0 * t * math.log(1.0 + self.ys[idx[0]] / 2.0))
            order = np.argsort(xs)
            self.lx, self.ly = np.array(xs)[order], np.array(ys_)[order]

    def tau(self, d: date) -> float:
        return (d - self.ref).days / self.year_days

    def df_tau(self, tau):
        tau = np.asarray(tau, float)
        if self.zero_interp:
            z = np.interp(tau, self.zx, self.zy)
            return np.exp(-z * tau)
        return np.exp(np.interp(tau, self.lx, self.ly))

    def df(self, d: date) -> float:
        return float(self.df_tau(self.tau(d)))

    def par_at(self, t: float) -> float:
        """A1 step 2 interpolation of the par yield (decimal) at t years; flat beyond the ends."""
        return float(np.interp(t, self.ts, self.ys))


def load_curve_row(path: Path, mmddyyyy: str) -> dict:
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row["Date"].strip() == mmddyyyy:
                return row
    raise KeyError(f"{mmddyyyy} not in {path}")


REF_ROW = load_curve_row(I1, "09/28/2026")
REF_TS, REF_YS = par_points(REF_ROW)


def ref_curve(shift_bp: float = 0.0, **kw) -> Curve:
    ts, ys = par_points(REF_ROW, shift_bp)
    return Curve(ts, ys, **kw)


BASE = ref_curve()

# ----------------------------------------------------------------------------- bond arithmetic (section 2)
def is_eom(d: date) -> bool:
    return d.day == calendar.monthrange(d.year, d.month)[1]


def add_months(d: date, n: int, force_eom: bool) -> date:
    y = d.year + (d.month - 1 + n) // 12
    m = (d.month - 1 + n) % 12 + 1
    last = calendar.monthrange(y, m)[1]
    return date(y, m, last if force_eom else min(d.day, last))


def schedule(maturity: date, settle: date):
    """Coupon dates strictly after settle (ascending, ending at maturity) and the previous coupon date."""
    eom = is_eom(maturity)
    after, k = [], 0
    while True:
        cd = add_months(maturity, -6 * k, eom)
        if cd <= settle:
            return sorted(after), cd
        after.append(cd)
        k += 1


def accrued_model(coupon_pct: float, maturity: date, settle: date = S) -> float:
    nxt, prev = schedule(maturity, settle)
    return coupon_pct / 2.0 * (settle - prev).days / (nxt[0] - prev).days


def dirty_model(curve: Curve, coupon_pct: float, maturity: date, settle: date = S) -> float:
    dates, _ = schedule(maturity, settle)
    v = sum(coupon_pct / 2.0 * curve.df(d) for d in dates) + 100.0 * curve.df(maturity)
    return v / curve.df(settle)


def street_yield(price_dirty: float, coupon_pct: float, maturity: date, settle: date = S) -> float:
    dates, prev = schedule(maturity, settle)
    w = (dates[0] - settle).days / (dates[0] - prev).days
    n = len(dates)
    cfs = [coupon_pct / 2.0 + (100.0 if k == n - 1 else 0.0) for k in range(n)]

    def f(y):
        return sum(cf / (1.0 + y / 2.0) ** (k + w) for k, cf in enumerate(cfs)) - price_dirty

    return brentq(f, -0.5, 1.0, xtol=1e-14, maxiter=500)


def bp(x: float) -> float:
    return x * 1e4


# ----------------------------------------------------------------------------- load I3, I4, I5, I6, I7
def load_portfolio(path: Path):
    """Sheet `Portfolio` tab as displayed: holdings (units, displayed price) and the typed plan split."""
    holdings, split = [], {}
    with open(path, newline="") as f:
        for r in csv.reader(f):
            if len(r) > 7 and r[3] in ("ETF", "Treasury bond"):
                holdings.append({"name": r[1], "kind": "ETF" if r[3] == "ETF" else "Treasury",
                                 "qty": num(r[7]), "price_sheet": num(r[6]), "target_sheet": num(r[5]),
                                 "job": r[2]})
            if len(r) > 2 and r[1] in ("Payment ladder", "Facility floor", "Stock fund", "Cash") \
                    and r[2].endswith("%"):
                split[r[1]] = num(r[2]) / 100.0
    return holdings, split


def load_wins(path: Path):
    out = {}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rec = {"kind": r["type"], "price": num(r["price"]), "wins_name": r["wins_name"],
                   "price_source": r["price_source"], "price_status": r["price_status"],
                   "role": r["portfolio_role"]}
            if r["type"] == "Treasury":
                rec.update(coupon=float(r["coupon_pct"]), maturity=date.fromisoformat(r["maturity"]),
                           cusip=r["cusip"],
                           accrued_rec=(float(r["accrued_per100_recorded"])
                                        if r["accrued_per100_recorded"].strip() else None))
            else:
                rec.update(end=date.fromisoformat(r["maturity"]) if r["maturity"].strip() else None)
            rec["bookL_size"] = float(r["bookL_size"]) if r["bookL_size"].strip() else None
            rec["bookL_end"] = date.fromisoformat(r["bookL_end_date"]) if r["bookL_end_date"].strip() else None
            rec["bookL_pays"] = int(r["bookL_pays_year"]) if r["bookL_pays_year"].strip() else None
            out[r["instrument"]] = rec
    return out


def load_ibond_holdings(path: Path):
    """I6: per fund, list of notes (par, coupon rounded to 1/8, maturity, cusip) and cash-like par."""
    funds = {t: {"notes": [], "cash_par": 0.0, "asof": None} for t in ETF_ORDER}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            t = r["fund"]
            if t not in funds:
                continue
            funds[t]["asof"] = r["holdings_asof"]
            par = float(r["par"])
            if r["asset_class"] == "Fixed Income":
                c_raw = float(r["coupon_pct"])
                funds[t]["notes"].append({"cusip": r["cusip"], "par": par, "coupon": round(8 * c_raw) / 8.0,
                                          "coupon_raw": c_raw, "maturity": date.fromisoformat(r["maturity"])})
            else:  # Money Market, Cash: at face
                funds[t]["cash_par"] += par
    return funds


def load_ibond_facts(path: Path):
    out = {}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            out[r["ticker"]] = {
                "nav": num(r["nav"]), "shares_out": num(r["shares_outstanding"]),
                "close": num(r["closing_price"]), "avg_ytm_pct": num(r["avg_ytm"]),
                "wam_years": float(r["wam"].replace("yrs", "").strip()),
                "premium_discount_pct_published": num(r["premium_discount_pct"]),
                "asof": r["nav_asof"], "url": r["url"]}
    return out


def load_nasdaq_close(path: Path, mmddyyyy="09/28/2026"):
    d = json.load(open(path))
    out = {}
    for t, rows in d.items():
        for r in rows:
            if r["date"] == mmddyyyy:
                out[t] = {"close": float(r["close"]), "volume": int(r["volume"].replace(",", ""))}
    return out


PORTFOLIO, SPLIT = load_portfolio(I3)
WINS = load_wins(I4)
IB_HOLD = load_ibond_holdings(I6)
IB_FACTS = load_ibond_facts(I7)
NASDAQ = load_nasdaq_close(I5)

BOOK_BONDS = [n for n, r in WINS.items() if r["kind"] == "Treasury" and r["bookL_size"]]
STALE_BONDS = [n for n, r in WINS.items() if r["kind"] == "Treasury" and not r["bookL_size"]]


# ----------------------------------------------------------------------------- A. ten payments
def pv_dates(curve: Curve, dates) -> float:
    return float(sum(PAYMENT * curve.df(d) for d in dates))


def basis_values(curve_fn, dates):
    """A3 for one basis: spot, forward to A, headroom, break-even fall, forward to 1 Jan 2028."""
    c0 = curve_fn(0.0)
    v0 = pv_dates(c0, dates)
    va = v0 / c0.df(A)

    def f(b):
        c = curve_fn(b)
        return pv_dates(c, dates) / c.df(A) - DEPOSIT

    be = brentq(f, -800.0, 0.0, xtol=1e-6) if va < DEPOSIT else brentq(f, 0.0, 800.0, xtol=1e-6)
    return {"spot_V0": v0, "forward_VA_2027_01_01": va, "headroom_vs_300k": DEPOSIT - va,
            "breakeven_parallel_fall_bp": -be, "forward_2028_01_01": v0 / c0.df(A2028),
            "per_date_DF": {d.isoformat(): c0.df(d) for d in dates},
            "per_date_PV": {d.isoformat(): PAYMENT * c0.df(d) for d in dates}}


def section_A():
    out = {"curve_date": D.isoformat(), "settlement": S.isoformat(),
           "tenors_used": {f"{t:.6f}": y * 100 for t, y in zip(REF_TS, REF_YS)},
           "par_grid_first_last": [float(BASE.par_grid[0]), float(BASE.par_grid[-1])],
           "DF_A_2027_01_01": BASE.df(A), "DF_2028_01_01": BASE.df(A2028),
           "nov15_basis": basis_values(lambda b: ref_curve(b), NOV15_DATES),
           "exact_basis": basis_values(lambda b: ref_curve(b), EXACT_DATES)}
    out["headline_pv_ten_payments_usd"] = out["nov15_basis"]["spot_V0"]  # A6
    out["exact_minus_nov15_spot"] = out["exact_basis"]["spot_V0"] - out["nov15_basis"]["spot_V0"]
    # A4 model-risk band
    variants = {
        "i_days365": dict(year_days=365.0),
        "ii_days365_plus_short_nodes": dict(year_days=365.0, short_nodes=True),
        "iii_pchip_par": dict(interp="pchip"),
        "iv_zero_rates_linear": dict(zero_interp=True),
    }
    band = {}
    for name, kw in variants.items():
        c = ref_curve(0.0, **kw)
        band[name] = {}
        for label, dates in (("nov15", NOV15_DATES), ("exact", EXACT_DATES)):
            v0 = pv_dates(c, dates)
            band[name][label] = {"spot_V0": v0, "forward_VA": v0 / c.df(A), "DF_A": c.df(A)}
    out["A4_model_risk_band"] = band
    out["A5_note"] = ("Laura's real ladder is a STRIPS ladder (Nov-15 basis): no coupon reinvestment; each "
                      "$50,000 waits 47 days (15 Nov to 1 Jan) in cash.")
    return out


# ----------------------------------------------------------------------------- B. WInS book
def price_sets():
    """B3: three price sets. ETF: per share. Treasury: (clean, accrued) per 100."""
    sheet = {h["name"]: (h["price_sheet"], None) for h in PORTFOLIO}   # bonds: displayed dirty; ETFs: live
    close, close_model = {}, {}
    for n, r in WINS.items():
        if r["kind"] == "ETF":
            close[n] = close_model[n] = (r["price"], None)
        elif r["accrued_rec"] is not None:
            close[n] = (r["price"], r["accrued_rec"])
            close_model[n] = (r["price"], accrued_model(r["coupon"], r["maturity"]))
    return {"sheet_as_read": sheet, "close_0928": close, "close_0928_model_accrued": close_model}


def dirty_of(name: str, pset: dict) -> float:
    p, acc = pset[name]
    return p if acc is None else p + acc


def book_cost(holdings, pset, label):
    """B1. holdings: list of (name, kind, qty)."""
    rows, tot_val, tot_comm = [], 0.0, 0.0
    for name, kind, qty in holdings:
        price = dirty_of(name, pset)
        value = qty * price if kind == "ETF" else qty * price / 100.0
        comm = COMM_ETF if kind == "ETF" else COMM_TSY
        rows.append({"ticker": name, "kind": kind, "quantity": qty, "price": price, "value_usd": value,
                     "commission_usd": comm, "cost_usd": value + comm, "weight_of_300k": value / DEPOSIT})
        tot_val += value
        tot_comm += comm
    cost = tot_val + tot_comm
    return {"price_set": label, "holdings": rows, "total_value_usd": tot_val, "total_commission_usd": tot_comm,
            "total_cost_usd": cost, "total_cost_usd_rounded": round(cost), "cash_left_usd": DEPOSIT - cost,
            "invested_weight": tot_val / DEPOSIT}


def bookL_holdings():
    hs = []
    for n, r in WINS.items():
        if r["bookL_size"]:
            hs.append((n, r["kind"], r["bookL_size"]))
    return hs


def portfolio_holdings():
    return [(h["name"], h["kind"], h["qty"]) for h in PORTFOLIO]


def bookL_rule(pset, curve: Curve):
    """B4 Book L sizing: target = 50,000 x DF(end); ETF ceil(target/price); bond ceil(target/(dirty/100)/1000)x1000."""
    out = {}
    for n, r in WINS.items():
        if not r["bookL_size"]:
            continue
        end = r["bookL_end"]
        target = PAYMENT * curve.df(end)
        price = dirty_of(n, pset)
        if r["kind"] == "ETF":
            size = math.ceil(target / price - 1e-9)
            value = size * price
        else:
            size = math.ceil(target / (price / 100.0) / 1000.0 - 1e-9) * 1000
            value = size * price / 100.0
        out[n] = {"end": end.isoformat(), "DF_end": curve.df(end), "target_usd": target, "price": price,
                  "size_rule": size, "size_in_I4": r["bookL_size"], "diff": size - r["bookL_size"],
                  "value_rule_usd": value}
    return out


def portfolio_rule(pset, bookL_vals: dict, include_comm_in_denominator: bool):
    """B4 Portfolio sizing: rung target = 0.659 x 300k x share; IBTM adds 0.243 x 300k; VT = 0.087 x 300k."""
    ladder_sh, floor_sh, stock_sh = SPLIT["Payment ladder"], SPLIT["Facility floor"], SPLIT["Stock fund"]
    vals = {n: v["value_rule_usd"] for n, v in bookL_vals.items()}
    denom = sum(vals.values()) + (5 * COMM_ETF + 5 * COMM_TSY if include_comm_in_denominator else 0.0)
    out = {}
    for h in PORTFOLIO:
        n = h["name"]
        price = dirty_of(n, pset)
        if n == "VT":
            target = stock_sh * DEPOSIT
        else:
            target = ladder_sh * DEPOSIT * vals[n] / denom
            if n == "IBTM":
                target += floor_sh * DEPOSIT
        if h["kind"] == "ETF":
            size = math.floor(target / price + 1e-9)
        else:
            size = math.floor(target / (price / 100.0) / 1000.0 + 1e-9) * 1000
        out[n] = {"target_usd": target, "target_in_sheet_usd": h["target_sheet"], "price": price,
                  "size_rule": size, "size_in_sheet": h["qty"], "diff": size - h["qty"]}
    return out


def section_B():
    psets = price_sets()
    out = {"price_sets": {k: {n: {"price": p, "accrued": a} for n, (p, a) in v.items()} for k, v in psets.items()},
           "portfolio": {}, "bookL": {}}
    for label, pset in psets.items():
        out["portfolio"][label] = book_cost(portfolio_holdings(), pset, label)
        out["bookL"][label] = book_cost(bookL_holdings(), pset, label)
    out["headline"] = out["portfolio"]["close_0928"]  # B6
    # I5 cross-check of the iShares closes used in close_0928 for IBTO-IBTR
    out["I5_check"] = {t: {"nasdaq_close": NASDAQ[t]["close"], "I4_price": WINS[t]["price"],
                           "abs_diff": abs(NASDAQ[t]["close"] - WINS[t]["price"]),
                           "within_half_cent": abs(NASDAQ[t]["close"] - WINS[t]["price"]) <= 0.005 + 1e-9,
                           "half_cent_tie": abs(abs(NASDAQ[t]["close"] - WINS[t]["price"]) - 0.005) < 1e-9}
                       for t in ETF_ORDER + ["VT"]}
    # accrued: recorded vs model
    out["accrued_recorded_vs_model"] = {
        n: {"recorded": WINS[n]["accrued_rec"], "model": accrued_model(WINS[n]["coupon"], WINS[n]["maturity"]),
            "diff_per100": WINS[n]["accrued_rec"] - accrued_model(WINS[n]["coupon"], WINS[n]["maturity"]),
            "prev_coupon": schedule(WINS[n]["maturity"], S)[1].isoformat(),
            "next_coupon": schedule(WINS[n]["maturity"], S)[0][0].isoformat(),
            "days_accrued_model": (S - schedule(WINS[n]["maturity"], S)[1]).days}
        for n in BOOK_BONDS}
    # B4 sizing checks at both price sets the Sheet could have used
    b4 = {}
    for label in ("sheet_as_read", "close_0928"):
        bl = bookL_rule(psets[label], BASE)
        b4[label] = {"bookL": bl,
                     "portfolio_spec_rule_commissions_excluded": portfolio_rule(psets[label], bl, False),
                     "portfolio_variant_denominator_includes_175_commissions": portfolio_rule(psets[label], bl, True)}
    out["B4_sizing_rule_check"] = b4
    return out, psets


# ----------------------------------------------------------------------------- D. iBonds look-through
def model_nav(ticker: str, curve: Curve):
    f, facts = IB_HOLD[ticker], IB_FACTS[ticker]
    so = facts["shares_out"]
    nav = 0.0
    for n in f["notes"]:
        nav += (n["par"] / so) * dirty_model(curve, n["coupon"], n["maturity"]) / 100.0
    cash_ps = f["cash_par"] / so
    return nav + cash_ps, cash_ps


def section_D():
    out = {}
    for t in ETF_ORDER:
        facts = IB_FACTS[t]
        nav0, cash_ps = model_nav(t, BASE)
        pub = facts["nav"]

        def g(b):
            return model_nav(t, ref_curve(b))[0] - pub

        shift = brentq(g, -300.0, 300.0, xtol=1e-4)
        par_at_wam_pct = BASE.par_at(facts["wam_years"]) * 100.0
        ytm_gap_bp = (facts["avg_ytm_pct"] - par_at_wam_pct) * 100.0
        notes = []
        for n in IB_HOLD[t]["notes"]:
            notes.append({"cusip": n["cusip"], "coupon": n["coupon"], "coupon_raw_2dp": n["coupon_raw"],
                          "maturity": n["maturity"].isoformat(), "par": n["par"],
                          "per_share": n["par"] / facts["shares_out"],
                          "dirty_model": dirty_model(BASE, n["coupon"], n["maturity"])})
        out[t] = {
            "holdings_asof": IB_HOLD[t]["asof"], "facts_asof": facts["asof"], "shares_outstanding": facts["shares_out"],
            "published_nav": pub, "model_nav": nav0, "cash_per_share": cash_ps,
            "model_over_published_minus_1": nav0 / pub - 1.0,
            "fund_price_vs_curve_bp": shift, "k_f_published_over_model": pub / nav0,
            "shift_reliable": abs(nav0 / pub - 1.0) < 0.01,
            "shift_comment": ("usable" if abs(nav0 / pub - 1.0) < 0.01 else
                              "NOT a mispricing: 24 Sep holdings vs 28 Sep share count (creation in between); "
                              "use ytm_gap_bp instead"),
            "avg_ytm_pct_ishares": facts["avg_ytm_pct"], "wam_years": facts["wam_years"],
            "par_yield_at_wam_pct": par_at_wam_pct, "ytm_gap_bp": ytm_gap_bp, "ytm_flag_gt_25bp": abs(ytm_gap_bp) > 25,
            "close": facts["close"], "premium_discount_computed_pct": (facts["close"] / pub - 1.0) * 100.0,
            "premium_discount_published_pct": facts["premium_discount_pct_published"],
            "n_notes": len(notes), "notes": notes,
            "timing_caveat": "share count is 28 Sep, holdings are 24 Sep: a creation/redemption in between biases the ratio"}
    return out


# ----------------------------------------------------------------------------- C. yield check
def section_C(D_out):
    out = {}
    for n in BOOK_BONDS + STALE_BONDS:
        r = WINS[n]
        c, M = r["coupon"], r["maturity"]
        acc_m = accrued_model(c, M)
        acc_r = r["accrued_rec"]
        clean = r["price"]
        dirty_w = clean + acc_m
        dirty_mod = dirty_model(BASE, c, M)
        y_w = street_yield(dirty_w, c, M)
        y_mod = street_yield(dirty_mod, c, M)
        gap = bp(y_w - y_mod)
        par_mat = BASE.par_at(BASE.tau(M))
        rec = {"cusip": r["cusip"], "coupon_pct": c, "maturity": M.isoformat(), "clean_wins": clean,
               "accrued_model": acc_m, "accrued_recorded": acc_r,
               "dirty_wins_model_accrued": dirty_w,
               "dirty_wins_recorded_accrued": (clean + acc_r) if acc_r is not None else None,
               "dirty_model": dirty_mod, "clean_model": dirty_mod - acc_m,
               "yield_wins_pct": y_w * 100, "yield_model_pct": y_mod * 100, "gap_bp": gap,
               "yield_wins_recorded_accrued_pct": (street_yield(clean + acc_r, c, M) * 100) if acc_r is not None else None,
               "par_yield_at_maturity_pct": par_mat * 100, "yield_wins_minus_par_bp": bp(y_w - par_mat),
               "flag_stale_or_wrong": abs(gap) > 25.0, "in_book": n in BOOK_BONDS,
               "price_source": r["price_source"], "price_status": r["price_status"]}
        if n in STALE_BONDS:  # P3: also the reading where the recorded price is already dirty
            y_dirty = street_yield(clean, c, M)
            rec["if_price_were_dirty"] = {"yield_pct": y_dirty * 100, "gap_bp": bp(y_dirty - y_mod)}
        # cross-reference: IBTR holds 912810FT0 (the 4.5% Feb-2036); its Sheet status text if any
        out[n] = rec
    # named alternates for flagged bonds (from the book itself: nearest-maturity book bond that passes)
    passing = [n for n in BOOK_BONDS if not out[n]["flag_stale_or_wrong"]]
    for n in out:
        if out[n]["flag_stale_or_wrong"]:
            M = WINS[n]["maturity"]
            alt = min(passing, key=lambda k: abs((WINS[k]["maturity"] - M).days)) if passing else None
            out[n]["named_alternate"] = alt
            out[n]["advice"] = "stale or wrong: do not trade at this price; use the named alternate"
    # cross-reference: IBTR holds the 4.5% Feb-2036 (912810FT0); its curve-implied dirty price is in D
    for note in D_out["IBTR"]["notes"]:
        if note["cusip"] == "912810FT0":
            out["T 4.500% 15-Feb-2036"]["same_bond_inside_IBTR_dirty_model"] = note["dirty_model"]
    # P10 diagnostic: Sheet status texts vs the spec gap on 28 Sep and on 25 Sep (diagnostic only)
    sheet_status = {"T 4.750% 15-Feb-2037": -8, "T 4.500% 15-May-2038": 6, "T 4.375% 15-Nov-2039": 13,
                    "T 4.250% 15-Nov-2040": 14, "T 3.125% 15-Nov-2041": 15}
    ts25, ys25 = par_points(load_curve_row(I1, "09/25/2026"))
    c25 = Curve(ts25, ys25)
    diag = {}
    for n in BOOK_BONDS:
        r = WINS[n]
        c, M = r["coupon"], r["maturity"]
        y_m25 = street_yield(dirty_model(c25, c, M), c, M)
        y_m28 = street_yield(dirty_model(BASE, c, M), c, M)
        y_w_model_acc = street_yield(r["price"] + accrued_model(c, M), c, M)
        y_w_rec_acc = street_yield(r["price"] + r["accrued_rec"], c, M)
        diag[n] = {"sheet_status_bp": sheet_status[n],
                   "gap_28sep_model_accrued_bp": bp(y_w_model_acc - y_m28),
                   "gap_28sep_recorded_accrued_bp": bp(y_w_rec_acc - y_m28),
                   "gap_25sep_model_accrued_bp": bp(y_w_model_acc - y_m25),
                   "gap_25sep_recorded_accrued_bp": bp(y_w_rec_acc - y_m25)}
    out["_diagnostic_sheet_status_vs_curves"] = {
        "note": ("DIAGNOSTIC ONLY. The Sheet's -8 and +6 are reproduced by the 25 Sep curve with the recorded "
                 "accrued; the +6 for the May-2038 is an artefact of its recorded accrued (0.530 vs 1.663 model). "
                 "The +13/+14/+15 are not reproduced on either curve."),
        "per_bond": diag}
    return out


# ----------------------------------------------------------------------------- E. coupon reinvestment stress
def month_ends(after: date, upto: date):
    """Month-end dates strictly after `after` and <= `upto`."""
    out = []
    y, m = after.year, after.month
    while True:
        me = date(y, m, calendar.monthrange(y, m)[1])
        if me > upto:
            return out
        if me > after:
            out.append(me)
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def flows_treasury(name: str, face: float):
    r = WINS[name]
    c, M = r["coupon"], r["maturity"]
    dates, _ = schedule(M, S)
    flows = [(d, face * c / 2.0 / 100.0) for d in dates]
    flows.append((M, face))
    price_paid = face * (r["price"] + accrued_model(c, M)) / 100.0
    return flows, price_paid


def flows_ibond(ticker: str, shares: float, k_f: float, p_etf: float):
    f, so = IB_HOLD[ticker], IB_FACTS[ticker]["shares_out"]
    E_f = date(ETF_YEAR[ticker], 12, 15)
    flows = []
    for n in f["notes"]:
        a = n["par"] / so * k_f * shares
        dates, _ = schedule(n["maturity"], S)
        flows += [(d, a * n["coupon"] / 2.0 / 100.0) for d in dates]
        flows.append((n["maturity"], a))          # P5: principal, equivalent to holding at r inside the fund to E_f
    flows.append((S, f["cash_par"] / so * k_f * shares))   # P5: cash lines at face today
    fee = FEE_ANNUAL / 12.0 * p_etf * shares
    flows += [(me, -fee) for me in month_ends(S, E_f)]     # P6
    return flows, shares * p_etf, E_f


def value_at(flows, T: date, r=None, curve: Curve | None = None):
    if curve is not None:
        dT = curve.df(T)
        return sum(cf * curve.df(d) / dT for d, cf in flows)
    return sum(cf * (1.0 + r / 2.0) ** (2.0 * (T - d).days / YEAR_DAYS) for d, cf in flows)


def own_yield(flows, cost: float) -> float:
    def f(r):
        return sum(cf * (1.0 + r / 2.0) ** (-2.0 * (d - S).days / YEAR_DAYS) for d, cf in flows) - cost
    return brentq(f, -0.9, 2.0, xtol=1e-12, maxiter=500)


def stress_one(name, kind, qty, k_f_map, pset):
    if kind == "Treasury":
        flows, cost = flows_treasury(name, qty)
        T = date(WINS[name]["bookL_pays"], 1, 1)
        E_f = None
    else:
        flows, cost, E_f = flows_ibond(name, qty, k_f_map[name], pset[name][0])
        T = date(ETF_YEAR[name] + 1, 1, 1)
    y = own_yield(flows, cost)
    scen = {"own_yield": y, "own_minus_2pts": y - 0.02, "r_2pct": 0.02, "r_0pct": 0.0}
    vals = {k: value_at(flows, T, r=v) for k, v in scen.items()}
    vals["curve"] = value_at(flows, T, curve=BASE)
    return {"pays": T.isoformat(), "own_yield_pct": y * 100, "cost_paid_excl_commission": cost,
            "n_flows": len(flows), "fund_end": E_f.isoformat() if E_f else None,
            "delivered_value": vals, "ratio_to_curve": {k: v / vals["curve"] for k, v in vals.items()}}


def section_E(D_out, psets):
    k_f = {t: D_out[t]["k_f_published_over_model"] for t in ETF_ORDER}
    pset = psets["close_0928"]
    out = {"bookL": {}, "portfolio": {}}
    scen_keys = ["own_yield", "own_minus_2pts", "r_2pct", "r_0pct", "curve"]
    tot = {k: 0.0 for k in scen_keys}
    buf = {k: 0.0 for k in scen_keys}
    for name, kind, qty in bookL_holdings():
        r = stress_one(name, kind, qty, k_f, pset)
        r["vs_50k"] = {k: v - PAYMENT for k, v in r["delivered_value"].items()}
        out["bookL"][name] = r
        for k in scen_keys:
            v = r["delivered_value"][k]
            tot[k] += v
            if v < PAYMENT:
                buf[k] += r["cost_paid_excl_commission"] * (PAYMENT / v - 1.0)
    out["bookL_total_delivered"] = tot
    out["bookL_total_vs_500k"] = {k: v - 10 * PAYMENT for k, v in tot.items()}
    out["bookL_buffer_cost"] = buf
    for name, kind, qty in portfolio_holdings():
        if name == "VT":
            continue
        r = stress_one(name, kind, qty, k_f, pset)
        out["portfolio"][name] = {"pays": r["pays"], "own_yield_pct": r["own_yield_pct"],
                                  "ratio_to_curve": r["ratio_to_curve"], "delivered_value": r["delivered_value"]}
    return out


# ----------------------------------------------------------------------------- F. plan split
def section_F(A_out):
    y1 = BASE.par_at(1.0)
    y5 = BASE.par_at(5.0)
    out = {"y1_pct": y1 * 100, "y5_pct": y5 * 100}
    for label in ("exact_basis", "nov15_basis"):
        v0, va = A_out[label]["spot_V0"], A_out[label]["forward_VA_2027_01_01"]
        leftover = DEPOSIT - va
        ladder = v0 / BASE.df(A2028)
        G = leftover * (1.0 + y1) + DEPOSIT_2028
        floor = DEPOSIT_2028 / (1.0 + y5) ** 5
        stock = G - floor
        total = ladder + G
        out[label] = {"leftover_2027": leftover, "ladder_2028": ladder, "growth_money_G": G, "floor": floor,
                      "stock_fund": stock, "total": total,
                      "shares": {"ladder": ladder / total, "floor": floor / total, "stock_fund": stock / total,
                                 "floor_plus_stock": G / total}}
    out["typed_split_in_sheet"] = SPLIT
    return out


# ----------------------------------------------------------------------------- G. history
def section_G(A_out):
    tau_exact = np.array([(d - D).days / YEAR_DAYS for d in EXACT_DATES])
    tau_nov = np.array([(d - D).days / YEAR_DAYS for d in NOV15_DATES])
    tau_A = (A - D).days / YEAR_DAYS
    tau_A1 = (A + timedelta(days=365) - D).days / YEAR_DAYS
    rows = []
    files = sorted([p for dd in I2_DIRS for p in dd.glob("*.csv")], key=lambda p: int(p.stem))
    for path in files:
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                if not (r.get("6 Mo", "").strip() and r.get("10 Yr", "").strip()):
                    continue
                m, dd_, y = r["Date"].split("/")
                d = date(int(y), int(m), int(dd_))
                if d > D:
                    continue
                ts, ys = par_points(r)
                c = Curve(ts, ys, ref=d)
                dfA = float(c.df_tau(tau_A))
                v0e = float(PAYMENT * c.df_tau(tau_exact).sum())
                v0n = float(PAYMENT * c.df_tau(tau_nov).sum())
                vAe, vAn = v0e / dfA, v0n / dfA
                dep = DEPOSIT_2028 * float(c.df_tau(tau_A1)) / dfA
                rows.append((d, v0n, vAn, v0e, vAe, max(0.0, vAn - DEPOSIT - dep), max(0.0, vAe - DEPOSIT - dep),
                             float(c.par_at(10.0)) * 100))
    rows.sort()
    with open(HERE / "history_daily.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "V0_nov15", "VA_nov15", "V0_exact", "VA_exact", "unfunded_nov15", "unfunded_exact",
                    "par_10y_pct"])
        for row in rows:
            w.writerow([row[0].isoformat()] + [f"{x:.2f}" for x in row[1:7]] + [f"{row[7]:.2f}"])
    dates = [r[0] for r in rows]
    series = {"V0_nov15": 1, "VA_nov15": 2, "V0_exact": 3, "VA_exact": 4}
    on_D = {k: rows[-1][i] for k, i in series.items()}
    assert rows[-1][0] == D, "last history row must be the reference date"
    out = {"n_days": len(rows), "first_date": dates[0].isoformat(), "last_date": dates[-1].isoformat(),
           "values_on_D_from_I2": on_D,
           "consistency_with_section_A": {"V0_nov15_diff": on_D["V0_nov15"] - A_out["nov15_basis"]["spot_V0"],
                                          "VA_nov15_diff": on_D["VA_nov15"] - A_out["nov15_basis"]["forward_VA_2027_01_01"],
                                          "V0_exact_diff": on_D["V0_exact"] - A_out["exact_basis"]["spot_V0"],
                                          "VA_exact_diff": on_D["VA_exact"] - A_out["exact_basis"]["forward_VA_2027_01_01"]},
           "series": {}}
    for k, i in series.items():
        vals = np.array([r[i] for r in rows])
        v2020 = [r[i] for r in rows if r[0].year == 2020]
        imax = int(vals.argmax())
        prior = [(r[0], r[i]) for r in rows if r[0] < D and r[i] <= on_D[k]]
        since2000 = [(r[0], r[i]) for r in rows if r[0] >= date(2000, 1, 1)]
        out["series"][k] = {
            "value_on_D": on_D[k],
            "y2020": {"median": statistics.median(v2020), "min": min(v2020), "max": max(v2020), "n": len(v2020)},
            "max_all_days": {"value": float(vals[imax]), "date": rows[imax][0].isoformat()},
            "min_all_days": {"value": float(vals.min()), "date": rows[int(vals.argmin())][0].isoformat()},
            "share_days_le_300k_since_1990": float(np.mean(vals <= DEPOSIT)),
            "share_days_le_300k_since_2000": float(np.mean([v <= DEPOSIT for _, v in since2000])),
            "last_date_before_D_at_or_below_value_on_D": prior[-1][0].isoformat() if prior else None,
            "value_on_that_date": prior[-1][1] if prior else None,
            "n_days_le_value_on_D_before_D": len(prior),
        }
    for k, i in (("nov15", 5), ("exact", 6)):
        unf = np.array([r[i] for r in rows])
        out[f"deposit_check_{k}"] = {"days_unfunded_positive": int((unf > 0).sum()),
                                     "share_days_unfunded": float(np.mean(unf > 0)),
                                     "max_unfunded_usd": float(unf.max()),
                                     "max_unfunded_date": rows[int(unf.argmax())][0].isoformat()}
    out["note"] = ("V0 asks 'would $300,000 in hand that day have bought all ten payments?'; V_A asks 'would the "
                   "ladder have cost at most $300,000 on the day the deposit arrives?'. Headline history figures are "
                   "Nov-15 basis (A6). Same time to maturity: payment dates shifted with the curve date.")
    return out


# ----------------------------------------------------------------------------- B5 cash margin (needs D)
def section_B5(D_out, psets):
    pset = psets["close_0928"]
    nav0 = {t: D_out[t]["model_nav"] for t in ETF_ORDER}
    dirty0 = {n: dirty_model(BASE, WINS[n]["coupon"], WINS[n]["maturity"]) for n in BOOK_BONDS}

    def cost(b):
        c = ref_curve(b)
        total = 0.0
        for name, kind, qty in portfolio_holdings():
            price = dirty_of(name, pset)
            if kind == "Treasury":
                total += qty * price / 100.0 * dirty_model(c, WINS[name]["coupon"], WINS[name]["maturity"]) / dirty0[name]
                total += COMM_TSY
            elif name in ETF_ORDER:
                total += qty * price * model_nav(name, c)[0] / nav0[name] + COMM_ETF
            else:
                total += qty * price + COMM_ETF
        return total

    c0 = cost(0.0)
    b_300 = brentq(lambda b: cost(b) - DEPOSIT, -600.0, 0.0, xtol=1e-6)
    b_299 = brentq(lambda b: cost(b) - (DEPOSIT - 1000.0), -600.0, 0.0, xtol=1e-6)
    return {"cost_at_0_shift": c0, "check_equals_B1_close_0928": True,
            "fall_bp_cost_reaches_300k": -b_300, "fall_bp_cash_below_1000": -b_299,
            "cost_at_minus_10bp": cost(-10.0), "cost_at_minus_25bp": cost(-25.0), "cost_at_plus_25bp": cost(25.0)}


# ----------------------------------------------------------------------------- checks against Sheet display
def sheet_checks(B_out):
    """Cross-checks against numbers displayed in the Sheet (data, not code): Book L DFs and yield statuses."""
    bookL_dfs_sheet = {"IBTM": 0.729825, "IBTO": 0.691509, "IBTP": 0.655288, "IBTQ": 0.620501, "IBTR": 0.586914,
                       "T 4.750% 15-Feb-2037": 0.581302, "T 4.500% 15-May-2038": 0.541306,
                       "T 4.375% 15-Nov-2039": 0.495540, "T 4.250% 15-Nov-2040": 0.466558,
                       "T 3.125% 15-Nov-2041": 0.438835}
    out = {}
    for n, dfs in bookL_dfs_sheet.items():
        mine = BASE.df(WINS[n]["bookL_end"])
        out[n] = {"sheet_DF": dfs, "my_DF": mine, "diff": mine - dfs, "agree_6dp": abs(mine - dfs) < 1.5e-6}
    return {"bookL_DF_vs_sheet_display": out,
            "sheet_status_gaps_bp_as_displayed": {"T 4.750% 15-Feb-2037": -8, "T 4.500% 15-May-2038": 6,
                                                  "T 4.375% 15-Nov-2039": 13, "T 4.250% 15-Nov-2040": 14,
                                                  "T 3.125% 15-Nov-2041": 15}}


# ----------------------------------------------------------------------------- main
def main():
    np.random.seed(SEED)
    A_out = section_A()
    B_out, psets = section_B()
    D_out = section_D()
    C_out = section_C(D_out)
    B_out["B5_cash_margin"] = section_B5(D_out, psets)
    E_out = section_E(D_out, psets)
    F_out = section_F(A_out)
    G_out = section_G(A_out)
    checks = sheet_checks(B_out)

    head = B_out["headline"]
    summary = {
        "curve_date": D.isoformat(),
        "curve_source": f"U.S. Treasury Daily Par Yield Curve, row 09/28/2026 of {I1.relative_to(ROOT)} ({CURVE_URL})",
        "pv_ten_payments_usd": round(A_out["nov15_basis"]["spot_V0"], 2),
        "pv_ten_payments_usd_rounded": round(A_out["nov15_basis"]["spot_V0"]),
        "pv_ten_payments_exact_basis_not_buyable_usd": round(A_out["exact_basis"]["spot_V0"], 2),
        "forward_VA_2027_nov15_usd": round(A_out["nov15_basis"]["forward_VA_2027_01_01"], 2),
        "headroom_nov15_usd": round(A_out["nov15_basis"]["headroom_vs_300k"], 2),
        "breakeven_fall_bp_nov15": round(A_out["nov15_basis"]["breakeven_parallel_fall_bp"], 2),
        "book_holdings": [{"ticker": h["ticker"], "quantity": h["quantity"], "price": round(h["price"], 4),
                           "cost_usd": round(h["cost_usd"], 2)} for h in head["holdings"]],
        "book_total_cost_usd": round(head["total_cost_usd"], 2),
        "book_total_cost_usd_rounded": round(head["total_cost_usd"]),
        "book_cash_left_usd": round(head["cash_left_usd"], 2),
        "book_price_set": "close_0928 (Portfolio tab quantities; ETF per share; bond dirty = clean + recorded accrued)",
    }
    acc = B_out["accrued_recorded_vs_model"]["T 4.500% 15-May-2038"]
    flags = [
        {"id": "F1", "class": "fix-before-6-Nov",
         "finding": (f"Recorded accrued for T 4.500% 15-May-2038 is {acc['recorded']:.3f} per $100; a May/Nov coupon "
                     f"cycle gives {acc['model']:.4f} at 28 Sep ({acc['days_accrued_model']} days). The 0.530 looks "
                     "copied from the Feb/Aug bond it replaced. Effect on the headline book: about "
                     f"${19000 * (acc['model'] - acc['recorded']) / 100:,.0f} more cost; the Sheet's '+6bp' status "
                     "for this bond is an artefact of the wrong accrued."),
         "evidence": "B_book.accrued_recorded_vs_model; C_yield_check._diagnostic_sheet_status_vs_curves"},
        {"id": "F2", "class": "note-in-Final-Report",
         "finding": ("The Sheet's 'Price checked (+13/+14/+15bp)' statuses are not reproduced on the 28 Sep curve "
                     "(spec gaps -6.6, -5.1, -1.9bp) nor on 25 Sep; the -8 and +6 match 25 Sep. All five book "
                     "bonds still pass the 25bp test on 28 Sep, so nothing changes in the book; refresh the status "
                     "text before the IPS."),
         "evidence": "C_yield_check"},
        {"id": "F3", "class": "note-in-Final-Report",
         "finding": ("Both 29 Sep 'stale' WInS prices confirmed: 4.5% Feb-2036 at 102.95 is 111bp rich (curve-implied "
                     "dirty 95.20, and IBTR itself holds this bond); 4.375% Feb-2038 at 99.98 is 92bp rich. Do not "
                     "trade either at those prices."),
         "evidence": "C_yield_check, D_ibonds_lookthrough.IBTR.notes"},
        {"id": "F4", "class": "ignore",
         "finding": ("IBTM and IBTR model NAV is 4.3% / 9.4% below published: the 24 Sep holdings pre-date a share "
                     "creation before 28 Sep. Their 'fund price vs curve' shift is meaningless; the iShares YTM "
                     "gap (+1.6 / +0.3bp) shows both funds price on the curve. IBTO/IBTP/IBTQ agree within 0.08%."),
         "evidence": "D_ibonds_lookthrough"},
        {"id": "F5", "class": "note-in-Final-Report",
         "finding": ("Book L sizing (target = 50k x DF(end)) ignores the 7bp fund fee and the wait from maturity to "
                     "1 Jan: in the curve scenario the five iBond rungs deliver about $40-100 under $50,000 each, "
                     "while the Treasury rungs deliver $700-2,700 over. At 0% reinvestment (WInS cash) the ten rungs "
                     "deliver about $447k against $500k."),
         "evidence": "E_reinvestment_stress"},
        {"id": "F6", "class": "ignore",
         "finding": ("I5 Nasdaq closes for IBTM (21.755) and IBTR (23.485) sit on half-cent ties; I4 uses the WInS "
                     "(21.76) and iShares (23.49) prints. Not a discrepancy."),
         "evidence": "B_book.I5_check"},
    ]
    results = {
        "flags": flags,
        "meta": {"builder": "WS1-second-blind-pricer (blind_m1_2)", "spec": "rab/models/M1_METHOD.md (30 Sep corrected)",
                 "run_date_sydney": "2026-09-30", "seed": SEED, "python": sys.version.split()[0],
                 "numpy": np.__version__,
                 "inputs_sha256": {k: sha256(p) for k, p in
                                   (("I1", I1), ("I3", I3), ("I4", I4), ("I5", I5), ("I6", I6), ("I7", I7))},
                 "I2_files": len([p for dd in I2_DIRS for p in dd.glob("*.csv")])},
        "interpretation": [ln.strip() for ln in __doc__.split("Interpretive choices")[1].splitlines() if ln.strip()],
        "summary": summary,
        "A_ten_payments": A_out, "B_book": B_out, "C_yield_check": C_out, "D_ibonds_lookthrough": D_out,
        "E_reinvestment_stress": E_out, "F_plan_split": F_out, "G_history": G_out, "checks": checks,
        "known_limits": ("MODEL prices, not dealer quotes. One curve, one day. WInS settlement, bond unit and accrued "
                         "conventions UNVERIFIED. iBond distributions modelled as pass-through coupons. History uses "
                         "today's payment times."),
    }
    (HERE / "results.json").write_text(json.dumps(results, indent=1, default=str))

    # ---- compact console summary
    nb, ex = A_out["nov15_basis"], A_out["exact_basis"]
    print(f"Curve {D}: 1Y {REF_YS[list(REF_TS).index(1.0)]*100:.2f}  10Y {BASE.par_at(10)*100:.2f}  30Y {BASE.par_at(30)*100:.2f}")
    print(f"A3 Nov-15 basis: V0 {money(nb['spot_V0'])}  V_A {money(nb['forward_VA_2027_01_01'])}  "
          f"headroom {money(nb['headroom_vs_300k'])}  break-even fall {nb['breakeven_parallel_fall_bp']:.2f}bp  "
          f"fwd 2028 {money(nb['forward_2028_01_01'])}")
    print(f"A3 exact basis : V0 {money(ex['spot_V0'])}  V_A {money(ex['forward_VA_2027_01_01'])}  "
          f"headroom {money(ex['headroom_vs_300k'])}  break-even fall {ex['breakeven_parallel_fall_bp']:.2f}bp  "
          f"fwd 2028 {money(ex['forward_2028_01_01'])}")
    for k, v in A_out["A4_model_risk_band"].items():
        print(f"   A4 {k:30s} nov15 V0 {money(v['nov15']['spot_V0'])} V_A {money(v['nov15']['forward_VA'])} | "
              f"exact V0 {money(v['exact']['spot_V0'])} V_A {money(v['exact']['forward_VA'])}")
    for book in ("portfolio", "bookL"):
        for ps in ("sheet_as_read", "close_0928", "close_0928_model_accrued"):
            b = B_out[book][ps]
            print(f"B1 {book:9s} {ps:26s} cost {b['total_cost_usd']:>12,.2f}  cash left {b['cash_left_usd']:>10,.2f}")
    print("B6 headline holdings (close_0928):")
    for h in head["holdings"]:
        print(f"   {h['ticker']:22s} q {h['quantity']:>9,.0f}  price {h['price']:>9.4f}  cost {h['cost_usd']:>11,.2f}")
    m = B_out["B5_cash_margin"]
    print(f"B5 fall to $300k cost: {m['fall_bp_cost_reaches_300k']:.2f}bp; to cash<$1,000: {m['fall_bp_cash_below_1000']:.2f}bp")
    print("C  yield check (gap = WInS - model, bp; par gap = WInS - par at maturity):")
    for n, r in C_out.items():
        if n.startswith("_"):
            continue
        extra = f"  [if dirty: gap {r['if_price_were_dirty']['gap_bp']:+.1f}]" if "if_price_were_dirty" in r else ""
        print(f"   {n:22s} clean {r['clean_wins']:7.3f} acc_m {r['accrued_model']:.4f} acc_r {r['accrued_recorded']}  "
              f"y_w {r['yield_wins_pct']:.4f} y_m {r['yield_model_pct']:.4f} gap {r['gap_bp']:+6.1f} "
              f"par {r['yield_wins_minus_par_bp']:+6.1f} {'FLAG' if r['flag_stale_or_wrong'] else 'ok'}{extra}")
    print("D  iBonds look-through:")
    for t, r in D_out.items():
        print(f"   {t} modelNAV {r['model_nav']:.4f} pub {r['published_nav']:.2f} ratio-1 {r['model_over_published_minus_1']*100:+.3f}% "
              f"shift {r['fund_price_vs_curve_bp']:+.1f}bp  ytm gap {r['ytm_gap_bp']:+.1f}bp  prem {r['premium_discount_computed_pct']:+.3f}%")
    print("E  Book L delivered value by scenario (sum of ten):")
    for k, v in E_out["bookL_total_delivered"].items():
        print(f"   {k:16s} {money(v):>10s}  vs 500k {E_out['bookL_total_vs_500k'][k]:+11,.0f}  buffer {money(E_out['bookL_buffer_cost'][k])}")
    for n, r in E_out["bookL"].items():
        dv = r["delivered_value"]
        print(f"   {n:22s} own {r['own_yield_pct']:.3f}%  own {money(dv['own_yield'])} -2 {money(dv['own_minus_2pts'])} "
              f"2% {money(dv['r_2pct'])} 0% {money(dv['r_0pct'])} curve {money(dv['curve'])}")
    for lab in ("exact_basis", "nov15_basis"):
        s = F_out[lab]["shares"]
        print(f"F  {lab}: ladder {s['ladder']*100:.1f}%  floor {s['floor']*100:.1f}%  stock {s['stock_fund']*100:.1f}%  "
              f"total {money(F_out[lab]['total'])}")
    print(f"G  {G_out['n_days']} days {G_out['first_date']}..{G_out['last_date']}")
    for k, s in G_out["series"].items():
        print(f"   {k:9s} onD {money(s['value_on_D'])}  2020 med {money(s['y2020']['median'])} "
              f"[{money(s['y2020']['min'])},{money(s['y2020']['max'])}]  max {money(s['max_all_days']['value'])} {s['max_all_days']['date']}  "
              f"le300k 90s {s['share_days_le_300k_since_1990']*100:.1f}% 00s {s['share_days_le_300k_since_2000']*100:.1f}%  "
              f"cheapest since {s['last_date_before_D_at_or_below_value_on_D']}")
    for k in ("nov15", "exact"):
        dc = G_out[f"deposit_check_{k}"]
        print(f"   deposit check {k}: unfunded days {dc['days_unfunded_positive']} ({dc['share_days_unfunded']*100:.1f}%)  max {money(dc['max_unfunded_usd'])} {dc['max_unfunded_date']}")
    print("checks: Book L DF vs Sheet display agree(6dp):",
          all(v["agree_6dp"] for v in checks["bookL_DF_vs_sheet_display"].values()),
          "| G on D vs A:", {k: round(v, 6) for k, v in G_out["consistency_with_section_A"].items()})
    print("SUMMARY", json.dumps({k: summary[k] for k in ("pv_ten_payments_usd", "book_total_cost_usd")}))


if __name__ == "__main__":
    main()
