#!/usr/bin/env python
"""Blind second implementation of M1 (RAB Kit, WS1-blind-pricer, 2026-09-30 Sydney).

Written from rab/models/M1_METHOD.md and the raw inputs only. The reference implementation
(rab/models/m1_ladder.py), the insight_v1 pricing scripts and rab/numbers.yaml were NOT read.

Covers spec sections A (curve, ten payments), B (book cost, sizing rule), C (yield check),
F (plan split) and G (history). Sections D (ETF look-through), E (reinvestment) and B5 are
out of this agent's scope (PV of the ten payments and book cost holding by holding).

Run:  /Users/ray/Research/rab-ws/.venv/bin/python blind_pricer.py
Writes results.json and RESULTS.md next to this file.
"""
from __future__ import annotations

import calendar
import csv
import glob
import json
import math
import os
from datetime import date, timedelta

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
WT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))  # worktree root
DATA = os.path.join(WT, "rab", "data")

CURVE_2026 = os.path.join(DATA, "treasury_par_2000_2026", "2026.csv")
PORTFOLIO_CSV = os.path.join(DATA, "sheet", "Portfolio_values_2026-09-30T0030AEST.csv")
WINS_CSV = os.path.join(DATA, "wins", "wins_prices_2026-09-28.csv")

D = date(2026, 9, 28)          # reference / curve date
S = D                          # settlement (spec s2: S = D)
A = date(2027, 1, 1)           # Laura's $300k arrives
A2028 = date(2028, 1, 1)
START_CASH = 300_000.0
PAYMENT = 50_000.0
COMM_ETF, COMM_BOND = 25.0, 10.0

TENOR_YEARS = {
    "1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": 0.25, "6 Mo": 0.5, "1 Yr": 1.0, "2 Yr": 2.0,
    "3 Yr": 3.0, "5 Yr": 5.0, "7 Yr": 7.0, "10 Yr": 10.0, "20 Yr": 20.0, "30 Yr": 30.0,
}  # "1.5 Month" and "4 Mo" deliberately absent (spec A1.1)

EXACT_DATES = [date(y, 1, 1) for y in range(2033, 2043)]
NOV15_DATES = [date(y, 11, 15) for y in range(2032, 2042)]


# ----------------------------------------------------------------------------- dates
def add_months(d: date, n: int) -> date:
    """Same day of month, clamped to month end (spec s2)."""
    y, m = divmod(d.month - 1 + n, 12)
    y += d.year
    m += 1
    last = calendar.monthrange(y, m)[1]
    return date(y, m, min(d.day, last))


def is_eom(d: date) -> bool:
    return d.day == calendar.monthrange(d.year, d.month)[1]


def coupon_dates(maturity: date, settle: date) -> list[date]:
    """All coupon dates from the one before `settle` up to maturity (semiannual, EOM rule)."""
    eom = is_eom(maturity)
    dates = [maturity]
    k = 1
    while True:
        d = add_months(maturity, -6 * k)
        if eom:
            d = date(d.year, d.month, calendar.monthrange(d.year, d.month)[1])
        dates.append(d)
        if d <= settle:
            break
        k += 1
    return sorted(dates)


def tau(d: date, ref: date = D, basis: float = 365.25) -> float:
    return (d - ref).days / basis


# ----------------------------------------------------------------------------- curve
def read_curve_row(path: str, want: str) -> dict[str, float]:
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row["Date"] == want:
                out = {}
                for k, v in row.items():
                    if k in TENOR_YEARS and v not in ("", "N/A", None):
                        out[k] = float(v)
                return out
    raise KeyError(want)


class Curve:
    """Spec A1: linear par interpolation on a semiannual grid, bootstrap, log-linear DF."""

    def __init__(self, tenor_yields_pct: dict[str, float], shift_bp: float = 0.0,
                 basis: float = 365.25, par_interp: str = "linear",
                 df_interp: str = "logdf", short_nodes: bool = False):
        pts = sorted((TENOR_YEARS[k], v / 100 + shift_bp / 10_000) for k, v in tenor_yields_pct.items())
        self.tenors = np.array([p[0] for p in pts])
        self.pars = np.array([p[1] for p in pts])
        self.basis = basis
        self.df_interp = df_interp
        self.grid = 0.5 * np.arange(1, 61)
        if par_interp == "linear":
            self.p = np.interp(self.grid, self.tenors, self.pars)
        elif par_interp == "pchip":
            f = PchipInterpolator(self.tenors, self.pars, extrapolate=False)
            p = f(self.grid)
            p = np.where(self.grid < self.tenors[0], self.pars[0], p)
            p = np.where(self.grid > self.tenors[-1], self.pars[-1], p)
            self.p = p
        else:
            raise ValueError(par_interp)
        dfs = []
        acc = 0.0
        for pj in self.p:
            c = pj / 2
            dfj = (1 - c * acc) / (1 + c)
            dfs.append(dfj)
            acc += dfj
        self.df_grid = np.array(dfs)
        # interpolation nodes
        t_nodes = [0.0]
        ln_nodes = [0.0]
        if short_nodes:
            for k in ("1 Mo", "2 Mo", "3 Mo"):
                if k in tenor_yields_pct:
                    t = TENOR_YEARS[k]
                    y = tenor_yields_pct[k] / 100 + shift_bp / 10_000
                    t_nodes.append(t)
                    ln_nodes.append(-2 * t * math.log(1 + y / 2))
        t_nodes.extend(self.grid.tolist())
        ln_nodes.extend(np.log(self.df_grid).tolist())
        self.t_nodes = np.array(t_nodes)
        self.ln_nodes = np.array(ln_nodes)

    def par_at(self, t: float) -> float:
        return float(np.interp(t, self.tenors, self.pars))

    def df_t(self, t: float) -> float:
        if t <= 0:
            return 1.0
        if self.df_interp == "logdf":
            return math.exp(float(np.interp(t, self.t_nodes, self.ln_nodes)))  # flat beyond 30y
        # (iv) zero rates linear in t
        zt = self.t_nodes[1:]
        zr = -self.ln_nodes[1:] / zt
        return math.exp(-float(np.interp(t, zt, zr)) * t)

    def df(self, d: date, ref: date = D) -> float:
        return self.df_t((d - ref).days / self.basis)


def build_curve(shift_bp: float = 0.0, **kw) -> Curve:
    return Curve(read_curve_row(CURVE_2026, "09/28/2026"), shift_bp=shift_bp, **kw)


# ----------------------------------------------------------------------------- section A
def pv_payments(curve: Curve, dates: list[date], ref: date = D) -> float:
    return sum(PAYMENT * curve.df(d, ref) for d in dates)


def section_A() -> dict:
    out = {}
    base = build_curve()
    out["curve_inputs_pct"] = read_curve_row(CURVE_2026, "09/28/2026")
    out["par_grid_pct"] = [round(x * 100, 6) for x in base.p]
    out["df_grid"] = [round(x, 10) for x in base.df_grid]
    out["df_1jan2027"] = base.df(A)
    out["df_1jan2028"] = base.df(A2028)
    for name, dates in (("exact", EXACT_DATES), ("nov15", NOV15_DATES)):
        v0 = pv_payments(base, dates)
        va = v0 / base.df(A)
        v28 = v0 / base.df(A2028)

        def gap(b):
            c = build_curve(shift_bp=b)
            return pv_payments(c, dates) / c.df(A) - START_CASH

        be = brentq(gap, -500, 500, xtol=1e-6)
        out[name] = {
            "dates": [d.isoformat() for d in dates],
            "df_per_date": [base.df(d) for d in dates],
            "pv_per_date": [PAYMENT * base.df(d) for d in dates],
            "V0_spot": v0,
            "V_A_1jan2027": va,
            "headroom_vs_300k": START_CASH - va,
            "breakeven_parallel_fall_bp": -be,
            "V_1jan2028": v28,
        }
    # A4 model-risk band
    band = {}
    variants = {
        "i_days365": dict(basis=365.0),
        "ii_days365_short_nodes": dict(basis=365.0, short_nodes=True),
        "iii_pchip": dict(par_interp="pchip"),
        "iv_zero_linear": dict(df_interp="zero"),
    }
    for k, kw in variants.items():
        c = build_curve(**kw)
        band[k] = {}
        for name, dates in (("exact", EXACT_DATES), ("nov15", NOV15_DATES)):
            v0 = pv_payments(c, dates)
            band[k][name] = {"V0_spot": v0, "V_A_1jan2027": v0 / c.df(A)}
    out["A4_model_risk_band"] = band
    return out


# ----------------------------------------------------------------------------- bonds
def accrued_model(coupon_pct: float, maturity: date, settle: date = S) -> dict:
    cds = coupon_dates(maturity, settle)
    prev = max(d for d in cds if d <= settle)
    nxt = min(d for d in cds if d > settle)
    acc = (coupon_pct / 2) * (settle - prev).days / (nxt - prev).days
    return {"prev": prev, "next": nxt, "days_accrued": (settle - prev).days,
            "days_period": (nxt - prev).days, "accrued": acc}


def bond_flows(coupon_pct: float, maturity: date, settle: date = S) -> list[tuple[date, float]]:
    cds = [d for d in coupon_dates(maturity, settle) if d > settle]
    flows = [(d, coupon_pct / 2) for d in cds]
    flows[-1] = (maturity, coupon_pct / 2 + 100.0)
    return flows


def dirty_model(curve: Curve, coupon_pct: float, maturity: date, settle: date = S) -> float:
    dfS = curve.df(settle)
    return sum(cf * curve.df(d) / dfS for d, cf in bond_flows(coupon_pct, maturity, settle))


def street_yield(dirty: float, coupon_pct: float, maturity: date, settle: date = S) -> float:
    flows = bond_flows(coupon_pct, maturity, settle)
    info = accrued_model(coupon_pct, maturity, settle)
    w = (info["next"] - settle).days / info["days_period"]

    def f(y):
        return sum(cf / (1 + y / 2) ** (k + w) for k, (_, cf) in enumerate(flows)) - dirty

    return brentq(f, -0.05, 0.5, xtol=1e-12)


# ----------------------------------------------------------------------------- inputs
HOLDING_ORDER = ["IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "T 4.750% 15-Feb-2037", "T 4.500% 15-May-2038",
                 "T 4.375% 15-Nov-2039", "T 4.250% 15-Nov-2040", "T 3.125% 15-Nov-2041", "VT"]


def read_portfolio() -> dict[str, dict]:
    """Sheet Portfolio tab: quantity (units column) and displayed price per holding."""
    out = {}
    with open(PORTFOLIO_CSV, newline="") as f:
        for row in csv.reader(f):
            if len(row) > 7 and row[1] in HOLDING_ORDER:
                out[row[1]] = {
                    "type": row[3],
                    "sheet_price": float(row[6].replace("$", "").replace(",", "")),
                    "quantity": float(row[7].replace(",", "")),
                    "sheet_value": float(row[5].replace("$", "").replace(",", "")),
                    "status": row[12],
                }
    assert len(out) == 11, out.keys()
    return out


def read_wins() -> dict[str, dict]:
    out = {}
    with open(WINS_CSV, newline="") as f:
        for row in csv.DictReader(f):
            r = dict(row)
            r["price"] = float(r["price"])
            r["accrued_recorded"] = float(r["accrued_per100_recorded"]) if r["accrued_per100_recorded"] else None
            r["coupon"] = float(r["coupon_pct"]) if r["coupon_pct"] else None
            r["maturity_d"] = date.fromisoformat(r["maturity"]) if r["maturity"] else None
            r["bookL_size"] = float(r["bookL_size"]) if r["bookL_size"] else None
            out[r["instrument"]] = r
    return out


# ----------------------------------------------------------------------------- section B
def book_cost(holdings: dict[str, float], prices: dict[str, float], types: dict[str, str]) -> dict:
    rows = []
    total_val = total_comm = 0.0
    for h, q in holdings.items():
        p = prices[h]
        if types[h] == "Treasury":
            val = q * p / 100
            comm = COMM_BOND
        else:
            val = q * p
            comm = COMM_ETF
        rows.append({"ticker": h, "quantity": q, "price": p, "value": val, "commission": comm,
                     "cost": val + comm, "weight": val / START_CASH})
        total_val += val
        total_comm += comm
    return {"rows": rows, "value": total_val, "commissions": total_comm, "cost": total_val + total_comm,
            "cash_left": START_CASH - total_val - total_comm}


def section_B(curve: Curve) -> dict:
    pf = read_portfolio()
    wins = read_wins()
    types = {h: ("Treasury" if h.startswith("T ") else "ETF") for h in HOLDING_ORDER}
    pf_qty = {h: pf[h]["quantity"] for h in HOLDING_ORDER}
    bookL_names = [h for h in HOLDING_ORDER if h != "VT"]
    bookL_qty = {h: wins[h]["bookL_size"] for h in bookL_names}

    # price sets (dirty per 100 for bonds)
    sheet_as_read = {h: pf[h]["sheet_price"] for h in HOLDING_ORDER}
    close_0928, close_0928_model = {}, {}
    accrued = {}
    for h in HOLDING_ORDER:
        w = wins[h]
        if types[h] == "Treasury":
            am = accrued_model(w["coupon"], w["maturity_d"])
            accrued[h] = {"recorded": w["accrued_recorded"], "model": am["accrued"],
                          "prev_coupon": am["prev"].isoformat(), "next_coupon": am["next"].isoformat(),
                          "days_accrued": am["days_accrued"], "days_period": am["days_period"],
                          "clean": w["price"]}
            close_0928[h] = w["price"] + w["accrued_recorded"]
            close_0928_model[h] = w["price"] + am["accrued"]
        else:
            close_0928[h] = w["price"]
            close_0928_model[h] = w["price"]

    out = {"accrued": accrued, "portfolio": {}, "bookL": {}}
    for nm, ps in (("sheet_as_read", sheet_as_read), ("close_0928", close_0928),
                   ("close_0928_model_accrued", close_0928_model)):
        out["portfolio"][nm] = book_cost(pf_qty, ps, types)
        out["bookL"][nm] = book_cost(bookL_qty, {h: ps[h] for h in bookL_names}, types)

    # B4 sizing-rule check, at sheet_as_read prices (what the Sheet formulas saw) and at close_0928
    def end_date(h):
        if h.startswith("T "):
            return wins[h]["maturity_d"]
        return date(int(wins[h]["maturity"][:4]), 12, 15)

    sizing = {}
    for nm, ps in (("sheet_as_read", sheet_as_read), ("close_0928", close_0928)):
        bl = {}
        for h in bookL_names:
            target = PAYMENT * curve.df(end_date(h))
            if types[h] == "Treasury":
                q = math.ceil(target / (ps[h] / 100) / 1000) * 1000
            else:
                q = math.ceil(target / ps[h])
            bl[h] = {"df_end": curve.df(end_date(h)), "target": target, "size": q,
                     "sheet_size": bookL_qty[h], "match": q == bookL_qty[h],
                     "value": q * ps[h] / (100 if types[h] == "Treasury" else 1)}
        tot = sum(v["value"] for v in bl.values())
        pfz = {}
        for h in HOLDING_ORDER:
            if h == "VT":
                target = 0.087 * START_CASH
            else:
                target = 0.659 * START_CASH * bl[h]["value"] / tot
                if h == "IBTM":
                    target += 0.243 * START_CASH
            if types[h] == "Treasury":
                q = math.floor(target / (ps[h] / 100) / 1000) * 1000
            else:
                q = math.floor(target / ps[h])
            pfz[h] = {"target": target, "size": q, "sheet_size": pf_qty[h], "match": q == pf_qty[h]}
        sizing[nm] = {"bookL": bl, "bookL_value_sum": tot, "portfolio": pfz}
    out["B4_sizing_check"] = sizing
    out["portfolio_sheet_values"] = {h: pf[h]["sheet_value"] for h in HOLDING_ORDER}
    out["portfolio_status"] = {h: pf[h]["status"] for h in HOLDING_ORDER}
    return out


# ----------------------------------------------------------------------------- section C
def section_C(curve: Curve) -> dict:
    wins = read_wins()
    out = {}
    for h, w in wins.items():
        if w["type"] != "Treasury":
            continue
        am = accrued_model(w["coupon"], w["maturity_d"])
        clean = w["price"]
        dirty_wins = clean + am["accrued"]
        dm = dirty_model(curve, w["coupon"], w["maturity_d"])
        y_w = street_yield(dirty_wins, w["coupon"], w["maturity_d"])
        y_m = street_yield(dm, w["coupon"], w["maturity_d"])
        par_at_mat = curve.par_at(tau(w["maturity_d"]))
        rec = w["accrued_recorded"]
        entry = {
            "coupon": w["coupon"], "maturity": w["maturity"], "cusip": w["cusip"],
            "clean_wins": clean, "accrued_model": am["accrued"], "accrued_recorded": rec,
            "dirty_wins_model_accrued": dirty_wins, "dirty_model_curve": dm,
            "clean_model_curve": dm - am["accrued"],
            "yield_wins_pct": y_w * 100, "yield_model_pct": y_m * 100,
            "gap_bp": (y_w - y_m) * 1e4,
            "yield_minus_par_at_maturity_bp": (y_w - par_at_mat) * 1e4,
            "par_at_maturity_pct": par_at_mat * 100,
            "flag_stale": abs(y_w - y_m) * 1e4 > 25,
            "in_book": w["portfolio_role"].startswith("Jan"),
        }
        if rec is not None:
            y_rec = street_yield(clean + rec, w["coupon"], w["maturity_d"])
            entry["yield_wins_recorded_accrued_pct"] = y_rec * 100
            entry["gap_recorded_accrued_bp"] = (y_rec - y_m) * 1e4
        # the two stale prices: also test the "price is dirty" reading
        if rec is None:
            y_d = street_yield(clean, w["coupon"], w["maturity_d"])
            entry["yield_if_price_is_dirty_pct"] = y_d * 100
            entry["gap_if_price_is_dirty_bp"] = (y_d - y_m) * 1e4
        out[h] = entry
    return out


# ----------------------------------------------------------------------------- section F
def section_F(curve: Curve, secA: dict) -> dict:
    y1 = curve.par_at(1.0)
    y5 = curve.par_at(5.0)
    out = {"y1_pct": y1 * 100, "y5_pct": y5 * 100}
    for basis in ("exact", "nov15"):
        va = secA[basis]["V_A_1jan2027"]
        leftover = START_CASH - va
        ladder = secA[basis]["V_1jan2028"]
        G = leftover * (1 + y1) + 150_000
        floor = 150_000 / (1 + y5) ** 5
        fund = G - floor
        total = ladder + G
        out[basis] = {"leftover_1jan2027": leftover, "ladder_2jan2028": ladder, "growth_money_G": G,
                      "floor": floor, "stock_fund": fund, "total": total,
                      "share_ladder": ladder / total, "share_floor": floor / total, "share_fund": fund / total}
    return out


# ----------------------------------------------------------------------------- section G
def section_G(secA: dict) -> dict:
    files = sorted(glob.glob(os.path.join(DATA, "treasury_par_1990_1999", "*.csv"))
                   + glob.glob(os.path.join(DATA, "treasury_par_2000_2026", "*.csv")))
    t_exact = np.array([tau(d) for d in EXACT_DATES])
    t_nov = np.array([tau(d) for d in NOV15_DATES])
    tA = tau(A)
    tA1 = tau(A + timedelta(days=365))
    rows = []
    for fp in files:
        with open(fp, newline="") as f:
            for row in csv.DictReader(f):
                ty = {k: float(v) for k, v in row.items() if k in TENOR_YEARS and v not in ("", "N/A", None)}
                if "6 Mo" not in ty or "10 Yr" not in ty:
                    continue
                m, dd, yy = row["Date"].split("/")
                d = date(int(yy), int(m), int(dd))
                c = Curve(ty)
                dfA = c.df_t(tA)
                v0e = sum(PAYMENT * c.df_t(t) for t in t_exact)
                v0n = sum(PAYMENT * c.df_t(t) for t in t_nov)
                dfA1 = c.df_t(tA1)
                rows.append((d, v0e, v0e / dfA, v0n, v0n / dfA, dfA1 / dfA))
    rows.sort()
    dates = np.array([r[0] for r in rows])
    arr = np.array([r[1:] for r in rows])
    cols = {"V0_exact": 0, "V_A_exact": 1, "V0_nov15": 2, "V_A_nov15": 3}
    out = {"n_days": len(rows), "first": dates[0].isoformat(), "last": dates[-1].isoformat()}
    ref = {"V0_exact": secA["exact"]["V0_spot"], "V_A_exact": secA["exact"]["V_A_1jan2027"],
           "V0_nov15": secA["nov15"]["V0_spot"], "V_A_nov15": secA["nov15"]["V_A_1jan2027"]}
    y = np.array([d.year for d in dates])
    for k, j in cols.items():
        v = arr[:, j]
        m2020 = y == 2020
        imax = int(np.argmax(v))
        below = np.where((dates < D) & (v <= ref[k]))[0]
        out[k] = {
            "value_on_D_from_history_row": float(v[dates == D][0]) if (dates == D).any() else None,
            "value_on_D_sectionA": ref[k],
            "2020_median": float(np.median(v[m2020])), "2020_min": float(v[m2020].min()),
            "2020_max": float(v[m2020].max()), "2020_max_date": dates[m2020][int(np.argmax(v[m2020]))].isoformat(),
            "all_time_max": float(v[imax]), "all_time_max_date": dates[imax].isoformat(),
            "cheapest_since_last_date_at_or_below_D": dates[below[-1]].isoformat() if len(below) else None,
        }
    for k in ("V_A_exact", "V_A_nov15"):
        v = arr[:, cols[k]]
        out[k]["share_days_le_300k_since_1990"] = float((v <= START_CASH).mean())
        out[k]["share_days_le_300k_since_2000"] = float((v[y >= 2000] <= START_CASH).mean())
        unfunded = np.maximum(0.0, v - START_CASH - 150_000 * arr[:, 4])
        out[k]["deposit_check_days_unfunded"] = int((unfunded > 0).sum())
        out[k]["deposit_check_share_unfunded"] = float((unfunded > 0).mean())
        out[k]["deposit_check_max_unfunded"] = float(unfunded.max())
        out[k]["deposit_check_max_unfunded_date"] = dates[int(np.argmax(unfunded))].isoformat()
    return out


# ----------------------------------------------------------------------------- main
def main() -> None:
    curve = build_curve()
    res = {"meta": {"agent": "WS1-blind-pricer", "curve_date": D.isoformat(), "settle": S.isoformat(),
                    "curve_file": os.path.relpath(CURVE_2026, WT),
                    "curve_source": "U.S. Treasury Daily Par Yield Curve (home.treasury.gov), row 09/28/2026",
                    "spec": "rab/models/M1_METHOD.md", "code_read": "none of m1_ladder.py / insight_v1 / numbers.yaml"}}
    res["A"] = section_A()
    res["B"] = section_B(curve)
    res["C"] = section_C(curve)
    res["F"] = section_F(curve, res["A"])
    res["G"] = section_G(res["A"])
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(res, f, indent=1, default=str)
    write_md(res)


def money(x: float) -> str:
    return f"${x:,.2f}"


def write_md(res: dict) -> None:
    L = []
    A_ = res["A"]
    L.append("# Blind M1 pricing (WS1-blind-pricer)\n")
    L.append("Independent implementation of `rab/models/M1_METHOD.md`, sections A, B, C, F, G. Reference code, "
             "insight_v1 scripts and `numbers.yaml` were not read. Curve: U.S. Treasury par yield curve, "
             f"row 09/28/2026 (`{res['meta']['curve_file']}`). Settlement = 28 Sep 2026. AI-generated check "
             "(Claude Code) for Team Caplet; no deliverable text.\n")
    L.append("## A. The ten $50,000 payments on the 28 Sep 2026 par curve\n")
    L.append("| Basis | Spot value V0 (28 Sep 2026) | Value on 1 Jan 2027 | Headroom vs $300k | Break-even parallel fall | Value on 1 Jan 2028 |")
    L.append("|---|---|---|---|---|---|")
    for b, lab in (("exact", "Exact (1 Jan 2033-2042)"), ("nov15", "Nov-15 (15 Nov 2032-2041)")):
        a = A_[b]
        L.append(f"| {lab} | {money(a['V0_spot'])} | {money(a['V_A_1jan2027'])} | {money(a['headroom_vs_300k'])} | "
                 f"{a['breakeven_parallel_fall_bp']:.2f} bp | {money(a['V_1jan2028'])} |")
    L.append(f"\nDF(1 Jan 2027) = {A_['df_1jan2027']:.8f}; DF(1 Jan 2028) = {A_['df_1jan2028']:.8f}.\n")
    L.append("Per payment (exact basis):\n")
    L.append("| Payment date | DF | PV |")
    L.append("|---|---|---|")
    for d, df, pv in zip(A_["exact"]["dates"], A_["exact"]["df_per_date"], A_["exact"]["pv_per_date"]):
        L.append(f"| {d} | {df:.6f} | {money(pv)} |")
    L.append("\nPer payment (Nov-15 basis):\n")
    L.append("| Payment date | DF | PV |")
    L.append("|---|---|---|")
    for d, df, pv in zip(A_["nov15"]["dates"], A_["nov15"]["df_per_date"], A_["nov15"]["pv_per_date"]):
        L.append(f"| {d} | {df:.6f} | {money(pv)} |")
    L.append("\nA4 model-risk band (report, never headline):\n")
    L.append("| Variant | V0 exact | V_A exact | V0 Nov-15 | V_A Nov-15 |")
    L.append("|---|---|---|---|---|")
    for k, v in A_["A4_model_risk_band"].items():
        L.append(f"| {k} | {money(v['exact']['V0_spot'])} | {money(v['exact']['V_A_1jan2027'])} | "
                 f"{money(v['nov15']['V0_spot'])} | {money(v['nov15']['V_A_1jan2027'])} |")

    B_ = res["B"]
    L.append("\n## B. Cost of the WInS book\n")
    for book in ("portfolio", "bookL"):
        L.append(f"### {'Portfolio tab' if book == 'portfolio' else 'Book L'}\n")
        for ps, r in B_[book].items():
            L.append(f"**Price set `{ps}`**: value {money(r['value'])} + commissions {money(r['commissions'])} = "
                     f"cost **{money(r['cost'])}**; cash left {money(r['cash_left'])}.\n")
            L.append("| Holding | Quantity | Price | Value | Commission | Cost | Weight |")
            L.append("|---|---|---|---|---|---|---|")
            for row in r["rows"]:
                L.append(f"| {row['ticker']} | {row['quantity']:,.0f} | {row['price']:.4f} | {money(row['value'])} | "
                         f"{money(row['commission'])} | {money(row['cost'])} | {row['weight']*100:.2f}% |")
            L.append("")
    L.append("### Accrued interest (per $100 face, settlement 28 Sep 2026, actual/actual)\n")
    L.append("| Bond | Prev coupon | Next coupon | Days | Model accrued | Recorded | Difference |")
    L.append("|---|---|---|---|---|---|---|")
    for h, a in B_["accrued"].items():
        L.append(f"| {h} | {a['prev_coupon']} | {a['next_coupon']} | {a['days_accrued']}/{a['days_period']} | "
                 f"{a['model']:.4f} | {a['recorded']:.3f} | {a['recorded'] - a['model']:+.4f} |")
    L.append("\n### B4 sizing-rule check\n")
    for ps, sz in B_["B4_sizing_check"].items():
        L.append(f"Prices `{ps}`: Book L sizes match the Sheet for "
                 f"{sum(v['match'] for v in sz['bookL'].values())}/10 rungs; Portfolio sizes match for "
                 f"{sum(v['match'] for v in sz['portfolio'].values())}/11 holdings.\n")
        L.append("| Holding | Book L target | Book L size (mine / Sheet) | Portfolio target | Portfolio size (mine / Sheet) |")
        L.append("|---|---|---|---|---|")
        for h in HOLDING_ORDER:
            bl = sz["bookL"].get(h)
            pf = sz["portfolio"][h]
            bls = f"{money(bl['target'])} | {bl['size']:,.0f} / {bl['sheet_size']:,.0f}" if bl else "- | -"
            L.append(f"| {h} | {bls} | {money(pf['target'])} | {pf['size']:,.0f} / {pf['sheet_size']:,.0f} |")
        L.append("")

    C_ = res["C"]
    L.append("## C. Yield check of WInS bond prices (curve 28 Sep 2026)\n")
    L.append("| Bond | Clean (WInS) | Accrued model / recorded | Dirty WInS | Dirty model | Yield WInS | Yield model | Gap (bp) | vs par at maturity (bp) | Flag |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for h, c in C_.items():
        rec = f"{c['accrued_recorded']:.3f}" if c["accrued_recorded"] is not None else "n/a"
        flag = "STALE" if c["flag_stale"] else "ok"
        L.append(f"| {h} | {c['clean_wins']:.3f} | {c['accrued_model']:.4f} / {rec} | {c['dirty_wins_model_accrued']:.4f} | "
                 f"{c['dirty_model_curve']:.4f} | {c['yield_wins_pct']:.4f}% | {c['yield_model_pct']:.4f}% | "
                 f"{c['gap_bp']:+.1f} | {c['yield_minus_par_at_maturity_bp']:+.1f} | {flag} |")
    L.append("\nFor the two prices reported stale, the yield if the WInS figure is read as a dirty price: "
             + "; ".join(f"{h}: {c['yield_if_price_is_dirty_pct']:.3f}% (gap {c['gap_if_price_is_dirty_bp']:+.1f} bp)"
                         for h, c in C_.items() if "yield_if_price_is_dirty_pct" in c) + ".\n")

    F_ = res["F"]
    L.append("## F. Plan split on the current curve\n")
    L.append(f"y1 = {F_['y1_pct']:.2f}%, y5 = {F_['y5_pct']:.2f}% (par yields, annual compounding as E6).\n")
    L.append("| Basis | Leftover 1 Jan 2027 | Ladder 2 Jan 2028 | Growth money G | Floor | Stock fund | Total | Ladder / Floor / Fund |")
    L.append("|---|---|---|---|---|---|---|---|")
    for b in ("exact", "nov15"):
        f = F_[b]
        L.append(f"| {b} | {money(f['leftover_1jan2027'])} | {money(f['ladder_2jan2028'])} | {money(f['growth_money_G'])} | "
                 f"{money(f['floor'])} | {money(f['stock_fund'])} | {money(f['total'])} | "
                 f"{f['share_ladder']*100:.1f}% / {f['share_floor']*100:.1f}% / {f['share_fund']*100:.1f}% |")

    G_ = res["G"]
    L.append(f"\n## G. History, same time to maturity ({G_['n_days']:,} curve days, {G_['first']} to {G_['last']})\n")
    L.append("| Measure | Value on D | 2020 median | 2020 min | 2020 max (date) | All-time max (date) | Cheapest since (last date at or below D) |")
    L.append("|---|---|---|---|---|---|---|")
    for k in ("V0_exact", "V_A_exact", "V0_nov15", "V_A_nov15"):
        g = G_[k]
        L.append(f"| {k} | {money(g['value_on_D_sectionA'])} | {money(g['2020_median'])} | {money(g['2020_min'])} | "
                 f"{money(g['2020_max'])} ({g['2020_max_date']}) | {money(g['all_time_max'])} ({g['all_time_max_date']}) | "
                 f"{g['cheapest_since_last_date_at_or_below_D']} |")
    for k in ("V_A_exact", "V_A_nov15"):
        g = G_[k]
        L.append(f"\n{k}: share of days with value <= $300,000: since 1990 {g['share_days_le_300k_since_1990']*100:.1f}%, "
                 f"since 2000 {g['share_days_le_300k_since_2000']*100:.1f}%. Deposit check: {g['deposit_check_days_unfunded']:,} days "
                 f"({g['deposit_check_share_unfunded']*100:.1f}%) with an unfunded part; max {money(g['deposit_check_max_unfunded'])} on "
                 f"{g['deposit_check_max_unfunded_date']}.")
    with open(os.path.join(HERE, "RESULTS.md"), "w") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
