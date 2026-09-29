"""M1 ladder pricer: ten $50k payments on the official par curve, WInS book cost, bond yield check, iBond
look-through, coupon reinvestment stress, plan split, and the history comparison.

WS1, RAB Kit, 2026-09-30 (Sydney). AI-generated research code (Claude Code) for Team Caplet; MODEL outputs.
Spec: rab/models/M1_METHOD.md (sections A-G are mirrored here as [A]-[G]). Seed not needed (deterministic).

Reuse (per rab/inventory.md): the curve is the D1 method of research/insight_v1/scripts/D1_purchase_rule.py. This file
re-implements it with options (for the model-risk band) and asserts, at run time, that with default options it equals
D1's own `curve()` to 1e-12 on every discount factor used. The history section reproduces
rab/rescued/ladder_history_2000_2026.py (same method, same-ttm) and extends it to 1990 and the exact-date basis.

Run from the worktree root:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m1_ladder.py
Options: --curve-date YYYY-MM-DD (default: latest row in the 2026 file); --wins-prices PATH; --portfolio PATH.
Writes rab/models/out/m1_results.json, m1_report.txt, m1_bond_check_<date>.csv, m1_reinvestment_<date>.csv.
"""
import argparse
import calendar
import csv
import glob
import importlib.util
import json
import math
import os
import statistics as st
from datetime import date, timedelta

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "rab", "models", "out")
TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
A27, A28 = date(2027, 1, 1), date(2028, 1, 1)
YEARS = list(range(2033, 2043))
PAY, DEP1, DEP2 = 50_000, 300_000, 150_000
COMM = {"ETF": 25, "Treasury": 10}
TSY_URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/"
           "{y}/all?type=daily_treasury_yield_curve&field_tdr_date_value={y}&page&_format=csv")
REPORT = []


def say(s=""):
    REPORT.append(s)
    print(s)


# ----------------------------------------------------------------------------------------------------------- curve
def load_rows(paths):
    rows = []
    for p in paths:
        for r in csv.DictReader(open(p)):
            m, d, y = r["Date"].split("/")
            r["_date"] = date(int(y), int(m), int(d))
            rows.append(r)
    return sorted({r["_date"]: r for r in rows}.values(), key=lambda r: r["_date"])


class Curve:
    """[A1] D1 method by default: linear par on a 0.5y grid, semiannual bootstrap, log-linear DF, days/365.25."""

    def __init__(self, row, bp=0.0, basis=365.25, short_nodes=False, par_interp="linear", df_interp="logdf"):
        self.d0, self.basis = row["_date"], basis
        par = {t: float(row[k]) + bp / 100 for k, t in TENOR.items() if row.get(k) not in (None, "", "N/A")}
        self.ts = sorted(par)
        self.ps = [par[t] / 100 for t in self.ts]
        grid = np.arange(0.5, 30.01, 0.5)
        if par_interp == "linear":
            p = np.interp(grid, self.ts, self.ps)
        else:  # monotone cubic through the published tenors, flat outside
            f = PchipInterpolator(self.ts, self.ps, extrapolate=False)
            p = np.where(grid < self.ts[0], self.ps[0], np.where(grid > self.ts[-1], self.ps[-1], f(grid)))
        df = []
        for y in p:
            c = y / 2
            df.append((1 - c * sum(df)) / (1 + c))
        g, lz = [0.0], [0.0]
        if short_nodes:
            for t in (1 / 12, 2 / 12, .25):
                if t in par:
                    g.append(t)
                    lz.append(math.log((1 + par[t] / 200) ** (-2 * t)))
        self.g = np.array(g + list(grid))
        self.lz = np.array(lz + list(np.log(df)))
        self.df_interp = df_interp

    def tau(self, d):
        return (d - self.d0).days / self.basis

    def df(self, d):
        t = self.tau(d)
        if self.df_interp == "logdf":
            return float(math.exp(np.interp(t, self.g, self.lz)))
        z = -self.lz[1:] / self.g[1:]  # zero rates at nodes t > 0; flat below the first node
        return float(math.exp(-np.interp(t, self.g[1:], z) * t))

    def par_at(self, t):
        return float(np.interp(t, self.ts, self.ps))


def pay_dates(basis):
    return [date(y, 1, 1) if basis == "exact" else date(y - 1, 11, 15) for y in YEARS]


def liability(cv, basis):
    v0 = sum(PAY * cv.df(d) for d in pay_dates(basis))
    return {"spot": v0, "fwd_2027": v0 / cv.df(A27), "fwd_2028": v0 / cv.df(A28)}


def breakeven_bp(row, basis, **kw):
    f = lambda bp: liability(Curve(row, bp, **kw), basis)["fwd_2027"] - DEP1
    return -brentq(f, -600, 200, xtol=1e-4)


# ----------------------------------------------------------------------------------------------------------- bonds
def add_months(d, n, eom):
    y, m = divmod(d.month - 1 + n, 12)
    y, m = d.year + y, m + 1
    last = calendar.monthrange(y, m)[1]
    return date(y, m, last if eom else min(d.day, last))


def schedule(mat):
    """All coupon dates of a semiannual Treasury maturing `mat`, newest last (back to 1990)."""
    eom = mat.day == calendar.monthrange(mat.year, mat.month)[1]
    out, k = [], 0
    while True:
        d = add_months(mat, -6 * k, eom)
        if d.year < 1990:
            break
        out.append(d)
        k += 1
    return out[::-1]


def prev_next(mat, s):
    sch = schedule(mat)
    nxt = next(d for d in sch if d > s)
    return sch[sch.index(nxt) - 1], nxt


def accrued(c, mat, s):
    p, n = prev_next(mat, s)
    return c / 2 * (s - p).days / (n - p).days


def flows(c, mat, s, face=100.0):
    fl = [(d, face * c / 200) for d in schedule(mat) if d > s]
    fl[-1] = (fl[-1][0], fl[-1][1] + face)
    return fl


def model_dirty(cv, c, mat, s):
    return sum(a * cv.df(d) for d, a in flows(c, mat, s)) / cv.df(s)


def street_yield(c, mat, s, dirty):
    """[C3] P = sum CF_k / (1 + y/2)^(k-1+w), w = days(S -> next) / days in the period."""
    p, n = prev_next(mat, s)
    w = (n - s).days / (n - p).days
    fl = flows(c, mat, s)
    f = lambda y: sum(a / (1 + y / 2) ** (k + w) for k, (_, a) in enumerate(fl)) - dirty
    return brentq(f, -0.05, 0.5, xtol=1e-12)


def clean_at_yield(c, mat, s, y):
    p, n = prev_next(mat, s)
    w = (n - s).days / (n - p).days
    return sum(a / (1 + y / 2) ** (k + w) for k, (_, a) in enumerate(flows(c, mat, s))) - accrued(c, mat, s)


def years(d0, d1, basis=365.25):
    return (d1 - d0).days / basis


# ---------------------------------------------------------------------------------------------------------- inputs
def read_wins(path):
    rows = list(csv.DictReader(open(path)))
    for r in rows:
        r["price"] = float(r["price"])
        r["coupon"] = float(r["coupon_pct"]) if r["coupon_pct"] else None
        r["mat"] = date.fromisoformat(r["maturity"]) if r["maturity"] else None
        r["acc_rec"] = float(r["accrued_per100_recorded"]) if r["accrued_per100_recorded"] else None
        r["bookL_size"] = int(r["bookL_size"]) if r["bookL_size"] else None
        r["bookL_end"] = date.fromisoformat(r["bookL_end_date"]) if r["bookL_end_date"] else None
    return {r["instrument"]: r for r in rows}


def num(s):
    s = s.replace("$", "").replace(",", "").replace("%", "").strip()
    return float(s) if s not in ("", "-") else None


def read_portfolio(path):
    """Sheet tab Portfolio as exported (gviz CSV): rows with holding, job, type, weight, target $, price, units."""
    out = []
    for r in csv.reader(open(path)):
        if len(r) > 7 and r[3] in ("ETF", "Treasury bond") and r[1]:
            out.append({"holding": r[1], "job": r[2], "type": "ETF" if r[3] == "ETF" else "Treasury",
                        "weight_pct": num(r[4]), "target": num(r[5]), "price": num(r[6]), "units": int(num(r[7])),
                        "status": r[12]})
        if len(r) > 5 and r[1] == "Cash" and r[3] == "Cash":
            out_cash = num(r[5])
    return out, out_cash


# --------------------------------------------------------------------------------------------------------- [A] ladder
def section_a(rows, row):
    say(f"[A] Ten $50,000 payments (1 Jan 2033-2042) on the par curve of {row['_date']} (D1 method)")
    # reuse check against D1's own curve function
    spec = importlib.util.spec_from_file_location(
        "d1", os.path.join(ROOT, "research/insight_v1/scripts/D1_purchase_rule.py"))
    d1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(d1)
    cv, f1 = Curve(row), d1.curve(row)
    test = pay_dates("exact") + pay_dates("nov15") + [A27, A28, row["_date"] + timedelta(days=3)]
    worst = max(abs(cv.df(d) - f1(d)) for d in test)
    assert worst < 1e-12, worst
    say(f"    reuse check: this Curve equals D1_purchase_rule.curve() on all {len(test)} dates (max diff {worst:.1e})")
    res = {"curve_date": row["_date"].isoformat(), "par_yields_pct": {k: row[k] for k in TENOR if row.get(k)}}
    for basis in ("exact", "nov15"):
        L = liability(cv, basis)
        be = breakeven_bp(row, basis)
        res[basis] = {**L, "headroom_2027": DEP1 - L["fwd_2027"], "breakeven_fall_bp": be,
                      "rungs_spot": {str(y): PAY * cv.df(d) for y, d in zip(YEARS, pay_dates(basis))}}
        lab = "exact 1 Jan dates " if basis == "exact" else "Nov-15 STRIPS dates"
        say(f"    {lab}: value at {row['_date']} ${L['spot']:,.2f}; forward to 1 Jan 2027 ${L['fwd_2027']:,.2f} "
            f"(headroom ${DEP1 - L['fwd_2027']:,.0f}; passes $300k after a {be:.1f}bp parallel fall); "
            f"forward to 1 Jan 2028 ${L['fwd_2028']:,.0f}")
    # [A4] model-risk band
    variants = {"days/365": dict(basis=365), "days/365 + 1-3M nodes (GPT)": dict(basis=365, short_nodes=True),
                "PCHIP par interpolation": dict(par_interp="pchip"), "linear zero rates": dict(df_interp="zero")}
    res["band"] = {}
    for name, kw in variants.items():
        c2 = Curve(row, **kw)
        res["band"][name] = {b: liability(c2, b) for b in ("exact", "nov15")}
        say(f"    band {name:28s}: exact spot ${res['band'][name]['exact']['spot']:,.0f} fwd "
            f"${res['band'][name]['exact']['fwd_2027']:,.0f} | Nov-15 spot ${res['band'][name]['nov15']['spot']:,.0f} "
            f"fwd ${res['band'][name]['nov15']['fwd_2027']:,.0f}")
    for b in ("exact", "nov15"):
        vals = [res[b]["fwd_2027"]] + [v[b]["fwd_2027"] for v in res["band"].values()]
        res[b]["fwd_2027_band"] = [min(vals), max(vals)]
    say("    STRIPS (Laura's real ladder, Nov-15 basis): each $50,000 waits 47 days in cash; no coupons to reinvest")
    return res


# --------------------------------------------------------------------------------------------------- [C] yield check
def section_c(cv, wins, s):
    say(f"\n[C] Yield check of WInS bond prices against the {cv.d0} curve (settlement = {s}; flag if |gap| > 25bp)")
    out = []
    for k, r in wins.items():
        if r["type"] != "Treasury":
            continue
        c, mat = r["coupon"], r["mat"]
        ai = accrued(c, mat, s)
        dm = model_dirty(cv, c, mat, s)
        y_model = street_yield(c, mat, s, dm)
        y_w = street_yield(c, mat, s, r["price"] + ai)
        gap = (y_w - y_model) * 1e4
        par_gap = (y_w - cv.par_at(years(s, mat))) * 1e4
        rec = r["acc_rec"]
        row = {"bond": k, "cusip": r["cusip"], "wins_clean": r["price"], "accrued_model": ai, "accrued_recorded": rec,
               "model_clean": dm - ai, "yield_wins": y_w, "yield_model": y_model, "gap_bp": gap,
               "gap_vs_par_bp": par_gap, "flag": abs(gap) > 25,
               "clean_band_25bp": [clean_at_yield(c, mat, s, y_model + 0.0025), clean_at_yield(c, mat, s, y_model - 0.0025)],
               "accrued_flag": rec is not None and abs(rec - ai) > 0.05}
        out.append(row)
        say(f"    {k:22s} WInS clean {r['price']:8.3f} -> yield {y_w * 100:5.2f}%; model clean {dm - ai:8.3f} "
            f"(yield {y_model * 100:5.2f}%): gap {gap:+6.1f}bp (vs par {par_gap:+6.1f}bp) "
            f"{'FLAG: stale or wrong' if row['flag'] else 'ok'}; accrued model {ai:.3f}"
            + (f" vs recorded {rec:.3f}{' <- MISMATCH' if row['accrued_flag'] else ''}" if rec is not None else ""))
    return out


def model_price_table(cv, s):
    """Model clean prices and the +-25bp clean-price band for every fixed-coupon Treasury maturing 2036-2042 in the
    MSPD Table V snapshot (candidate alternates; WInS listing UNVERIFIED)."""
    path = os.path.join(ROOT, "research/insight_v1/wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv")
    out = []
    for r in csv.DictReader(open(path)):
        if r["maturity_date"] in ("", "null") or r["coupon_pct"] in ("", "null"):
            continue
        mat = date.fromisoformat(r["maturity_date"])
        if not date(2036, 1, 1) <= mat <= date(2042, 1, 1):
            continue
        c = float(r["coupon_pct"])
        ai = accrued(c, mat, s)
        dm = model_dirty(cv, c, mat, s)
        y = street_yield(c, mat, s, dm)
        out.append({"cusip": r["underlying_cusip"], "security_class": r["security_class"], "coupon_pct": c,
                    "maturity": mat.isoformat(), "model_clean": round(dm - ai, 3), "accrued": round(ai, 4),
                    "model_yield_pct": round(y * 100, 3),
                    "clean_low_(+25bp)": round(clean_at_yield(c, mat, s, y + 0.0025), 3),
                    "clean_high_(-25bp)": round(clean_at_yield(c, mat, s, y - 0.0025), 3)})
    return out


# ---------------------------------------------------------------------------------------------------- [D] iBonds
def ibond_holdings():
    path = os.path.join(ROOT, "research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv")
    out = {}
    for r in csv.DictReader(open(path)):
        if not r["fund"].startswith("IBT"):
            continue
        h = out.setdefault(r["fund"], {"notes": [], "cash": 0.0, "asof": r["holdings_asof"]})
        if r["asset_class"] == "Fixed Income":
            h["notes"].append((round(float(r["coupon_pct"]) * 8) / 8, date.fromisoformat(r["maturity"]),
                               float(r["par"])))
        else:
            h["cash"] += float(r["par"])
    return out


def ishares_facts():
    path = os.path.join(ROOT, "rab/data/ishares/ibonds_facts.csv")
    return {r["ticker"]: {"nav": num(r["nav"]), "close": num(r["closing_price"]),
                          "shares": num(r["shares_outstanding"]), "asof": r["nav_asof"],
                          "avg_ytm": r["avg_ytm"], "avg_volume_30d": num(r["avg_volume_30d"]),
                          "wam": num(r["wam"].replace(" yrs", "")), "prem_disc": num(r["premium_discount_pct"])}
            for r in csv.DictReader(open(path))}


def nav_model(row, h, shares, s, bp=0.0):
    cv = Curve(row, bp)
    return (sum(par * model_dirty(cv, c, mat, s) / 100 for c, mat, par in h["notes"]) + h["cash"]) / shares


def section_d(row, s):
    say(f"\n[D] iBonds look-through: holdings {ibond_holdings()['IBTM']['asof']} (iShares), shares/NAV 28 Sep")
    H, F = ibond_holdings(), ishares_facts()
    out = {}
    for t in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR"):
        h, f = H[t], F[t]
        m = nav_model(row, h, f["shares"], s)
        shift = brentq(lambda bp: nav_model(row, h, f["shares"], s, bp) - f["nav"], -300, 300, xtol=1e-3)
        cv = Curve(row)
        par_wam = cv.par_at(f["wam"])
        ytm_gap = (num(f["avg_ytm"]) / 100 - par_wam) * 1e4
        out[t] = {"nav": f["nav"], "close": f["close"], "model_nav": m, "ratio": f["nav"] / m, "shift_bp": shift,
                  "notes": len(h["notes"]), "last_note": max(n[1] for n in h["notes"]).isoformat(),
                  "ishares_avg_ytm": f["avg_ytm"], "wam": f["wam"], "par_at_wam": par_wam, "ytm_gap_bp": ytm_gap,
                  "premium_discount_pct": f["prem_disc"], "implied_shares_at_holdings_date": f["shares"] * m / f["nav"],
                  "lookthrough_reliable": abs(f["nav"] / m - 1) < 0.005}
        say(f"    {t}: NAV {f['nav']:.2f}, close {f['close']:.2f} (premium {f['prem_disc']:+.2f}%); iShares avg YTM "
            f"{f['avg_ytm']} vs par curve at its {f['wam']:.2f}y average maturity {par_wam * 100:.2f}% -> {ytm_gap:+.1f}bp"
            f" {'FLAG' if abs(ytm_gap) > 25 else 'ok'}; look-through model NAV {m:.4f} (NAV/model {f['nav'] / m - 1:+.2%}"
            + (f", shift {shift:+.1f}bp)" if out[t]["lookthrough_reliable"] else
               f": holdings 24 Sep vs shares 28 Sep do not line up; implied 24 Sep shares "
               f"{out[t]['implied_shares_at_holdings_date']:,.0f} vs {f['shares']:,.0f} on 28 Sep)"))
    say("    (look-through: holdings 24 Sep, shares 28 Sep; where they do not line up, the cash-flow schedule in [E] is "
        "scaled to the published NAV)")
    return out


# ---------------------------------------------------------------------------------------------------- [B] book cost
def book_cost(holdings):
    """holdings: list of dicts with type, qty, px (per share, or dirty per 100). Returns cost details."""
    rows, tot, comm = [], 0.0, 0
    for h in holdings:
        v = h["qty"] * h["px"] / (100 if h["type"] == "Treasury" else 1)
        rows.append({**h, "value": v, "commission": COMM[h["type"]]})
        tot += v
        comm += COMM[h["type"]]
    return {"rows": rows, "securities": tot, "commissions": comm, "cost": tot + comm, "cash_left": DEP1 - tot - comm}


def section_b(cv, wins, port, s):
    say("\n[B] Cost of the WInS book (Sheet tabs Portfolio and Book L; quantities as read 30 Sep 00:30 AEST)")
    res = {}
    # three price sets for the Portfolio tab
    sets = {}
    sets["sheet_as_read"] = [{"name": h["holding"], "type": h["type"], "qty": h["units"], "px": h["price"]}
                             for h in port]
    sets["close_0928"] = []
    sets["close_0928_model_accrued"] = []
    for h in port:
        w = wins[h["holding"]]
        if h["type"] == "ETF":
            px1 = px2 = w["price"]
        else:
            px1 = w["price"] + w["acc_rec"]
            px2 = w["price"] + accrued(w["coupon"], w["mat"], s)
        sets["close_0928"].append({"name": h["holding"], "type": h["type"], "qty": h["units"], "px": px1})
        sets["close_0928_model_accrued"].append({"name": h["holding"], "type": h["type"], "qty": h["units"], "px": px2})
    res["portfolio"] = {k: book_cost(v) for k, v in sets.items()}
    for k, v in res["portfolio"].items():
        say(f"    Portfolio tab, {k:26s}: securities ${v['securities']:,.2f} + commissions ${v['commissions']} = "
            f"${v['cost']:,.2f}; cash left ${v['cash_left']:,.2f}")
    base = res["portfolio"]["close_0928"]
    say("      holding                    qty      price     value  weight")
    for r in base["rows"]:
        say(f"      {r['name']:22s} {r['qty']:>9,} {r['px']:>9.3f} {r['value']:>10,.2f} {r['value'] / DEP1:6.2%}")
    lad = sum(r["value"] for r in base["rows"] if r["name"] != "VT")
    vt = next(r["value"] for r in base["rows"] if r["name"] == "VT")
    res["portfolio_split_close_0928"] = {"dated_holdings_incl_floor": lad / DEP1, "vt": vt / DEP1,
                                         "cash": base["cash_left"] / DEP1}
    say(f"      dated holdings (ladder + floor in IBTM) {lad / DEP1:.1%}, VT {vt / DEP1:.1%}, cash {base['cash_left'] / DEP1:.1%}")

    # Book L
    sets_l = {}
    for lab, acc in (("close_0928", "rec"), ("close_0928_model_accrued", "model")):
        hs = []
        for k, w in wins.items():
            if not w["bookL_size"]:
                continue
            px = w["price"] if w["type"] == "ETF" else w["price"] + (w["acc_rec"] if acc == "rec" else
                                                                     accrued(w["coupon"], w["mat"], s))
            hs.append({"name": k, "type": w["type"], "qty": w["bookL_size"], "px": px, "pays": int(w["bookL_pays_year"]),
                       "end": w["bookL_end"]})
        sets_l[lab] = hs
    res["bookL"] = {k: book_cost(v) for k, v in sets_l.items()}
    for k, v in res["bookL"].items():
        say(f"    Book L (sizes as read), {k:24s}: securities ${v['securities']:,.2f} + commissions "
            f"${v['commissions']} = ${v['cost']:,.2f}; cash left ${v['cash_left']:,.2f}")

    # [B4] sizing-rule check at 28 Sep closes
    say("    [B4] sizing rule re-run at 28 Sep closes (differences from the displayed sizes are due to live prices)")
    bl_rows = []
    for k, w in wins.items():
        if not w["bookL_size"]:
            continue
        tgt = PAY * cv.df(w["bookL_end"])
        px = w["price"] if w["type"] == "ETF" else w["price"] + w["acc_rec"]
        q = math.ceil(tgt / px) if w["type"] == "ETF" else math.ceil(tgt / (px / 100) / 1000) * 1000
        bl_rows.append({"name": k, "type": w["type"], "qty": q, "px": px, "df": cv.df(w["bookL_end"]), "target": tgt,
                        "shown_qty": w["bookL_size"]})
    bl = book_cost(bl_rows)
    res["bookL_rule"] = bl
    say(f"      Book L rule: targets ${sum(r['target'] for r in bl_rows):,.2f}; cost ${bl['cost']:,.2f}; cash left "
        f"${bl['cash_left']:,.2f}; size changes: "
        + (", ".join(f"{r['name']} {r['shown_qty']:,}->{r['qty']:,}" for r in bl_rows if r["qty"] != r["shown_qty"])
           or "none"))
    shares = {r["name"]: r["value"] / bl["securities"] for r in bl["rows"]}
    p_rows = []
    for h in port:
        w = wins[h["holding"]]
        if h["holding"] == "VT":
            tgt = 0.087 * DEP1
        else:
            tgt = 0.659 * DEP1 * shares[h["holding"]] + (0.243 * DEP1 if h["holding"] == "IBTM" else 0)
        px = w["price"] if h["type"] == "ETF" else w["price"] + w["acc_rec"]
        q = math.floor(tgt / px) if h["type"] == "ETF" else math.floor(tgt / (px / 100) / 1000) * 1000
        p_rows.append({"name": h["holding"], "type": h["type"], "qty": q, "px": px, "target": tgt, "shown_qty": h["units"]})
    pr = book_cost(p_rows)
    res["portfolio_rule"] = pr
    say(f"      Portfolio rule: cost ${pr['cost']:,.2f}; cash left ${pr['cash_left']:,.2f}; size changes: "
        + (", ".join(f"{r['name']} {r['shown_qty']:,}->{r['qty']:,}" for r in p_rows if r["qty"] != r["shown_qty"])
           or "none"))
    # cash margin: parallel fall in yields that uses up the cash (bonds + iBonds repriced on the curve, VT flat)
    return res


def cash_margin(row, wins, port, s, res_b, look):
    """Parallel fall (bp) at which the Portfolio units, repriced on the shifted curve, cost more than $300,000."""
    base_cv = Curve(row)
    H, F = ibond_holdings(), ishares_facts()

    def cost(bp):
        cv = Curve(row, bp)
        tot = 0.0
        for h in port:
            w = wins[h["holding"]]
            if h["holding"] == "VT":
                tot += h["units"] * w["price"]
            elif h["type"] == "ETF":
                ratio = nav_model(row, H[h["holding"]], F[h["holding"]]["shares"], s, bp) / \
                        nav_model(row, H[h["holding"]], F[h["holding"]]["shares"], s)
                tot += h["units"] * w["price"] * ratio
            else:
                dm0 = model_dirty(base_cv, w["coupon"], w["mat"], s)
                dm1 = model_dirty(cv, w["coupon"], w["mat"], s)
                tot += h["units"] * (w["price"] + w["acc_rec"]) / 100 * dm1 / dm0
            tot += COMM[h["type"]]
        return tot

    c0 = cost(0)
    be = brentq(lambda bp: cost(bp) - DEP1, -200, 0, xtol=1e-3)
    be1k = brentq(lambda bp: cost(bp) - (DEP1 - 1000), -200, 0, xtol=1e-3)
    say(f"    cash margin (Portfolio units, 28 Sep closes, bonds and iBonds repriced on a parallel shift, VT flat): "
        f"cost ${c0:,.0f}; all cash used after a {-be:.1f}bp fall; cash below $1,000 after a {-be1k:.1f}bp fall")
    return {"cost_at_0": c0, "fall_bp_cash_zero": -be, "fall_bp_cash_below_1000": -be1k}


# ------------------------------------------------------------------------------------------- [E] reinvestment
def month_ends(a, b):
    out, d = [], date(a.year, a.month, calendar.monthrange(a.year, a.month)[1])
    while d < b:
        if d > a:
            out.append(d)
        y, m = (d.year, d.month + 1) if d.month < 12 else (d.year + 1, 1)
        d = date(y, m, calendar.monthrange(y, m)[1])
    return out


def holder_flows(name, w, qty, s, look, H, F):
    """[E1] Cash to the holder from S to the payment date, per holding (qty shares or face $)."""
    if w["type"] == "Treasury":
        return flows(w["coupon"], w["mat"], s, face=qty)
    h, f = H[name], F[name]
    k = look[name]["ratio"]  # scale the notes so they are worth the published NAV
    end = w["mat"]  # termination date E_f (15 Dec of the fund year), as recorded in the price file
    fl = []
    for c, mat, par in h["notes"]:
        a = par / f["shares"] * k * qty
        fl += flows(c, mat, s, face=a)  # coupons pass through; principal held in the fund (same rate, see spec)
    fl += [(d, -0.0007 / 12 * w["price"] * qty) for d in month_ends(s, end)]
    return fl


def grow(fl, T, r, cv=None):
    if r == "curve":
        return sum(a * cv.df(d) / cv.df(T) for d, a in fl)
    return sum(a * (1 + r / 2) ** (2 * years(d, T)) for d, a in fl)


def irr(fl, s, cost):
    return brentq(lambda r: sum(a * (1 + r / 2) ** (-2 * years(s, d)) for d, a in fl) - cost, -0.05, 0.3, xtol=1e-12)


def section_e(cv, wins, port, s, look):
    say(f"\n[E] Coupon reinvestment stress (holder cash flows to each 1 Jan payment date; S = {s}; bonds at WInS clean + "
        "model accrued; iBonds by look-through scaled to NAV, 0.07% fee)")
    H, F = ibond_holdings(), ishares_facts()
    scen = ["own", "own-2pp", 0.02, 0.0, "curve"]
    out = {"bookL": [], "portfolio": []}
    tot = {str(k): 0.0 for k in scen}
    buf = {str(k): 0.0 for k in scen}
    cost_tot = 0.0
    say("    Book L rung      pays   cost     own yld   @own     @own-2pp  @2%      @0%      @curve   (target $50,000)")
    for name, w in wins.items():
        if not w["bookL_size"]:
            continue
        T = date(int(w["bookL_pays_year"]), 1, 1)
        qty = w["bookL_size"]
        px = w["price"] if w["type"] == "ETF" else w["price"] + accrued(w["coupon"], w["mat"], s)  # model accrued
        cost = qty * px / (100 if w["type"] == "Treasury" else 1)
        fl = holder_flows(name, w, qty, s, look, H, F)
        y = irr(fl, s, cost)
        vals = {}
        for k in scen:
            r = y if k == "own" else y - 0.02 if k == "own-2pp" else k
            vals[str(k)] = grow(fl, T, r, cv)
        rec = {"holding": name, "pays": T.isoformat(), "cost": cost, "own_yield": y,
               **{f"v_{k}": v for k, v in vals.items()}}
        out["bookL"].append(rec)
        cost_tot += cost
        for k, v in vals.items():
            tot[k] += v
            if v < PAY:
                buf[k] += cost * (PAY / v - 1)
        say(f"    {name:20s} {T.year} {cost:>9,.0f} {y * 100:6.2f}% " + " ".join(f"{vals[str(k)]:>8,.0f}" for k in scen))
    say(f"    {'total (ten rungs)':20s}      {cost_tot:>9,.0f}         " + " ".join(f"{tot[str(k)]:>8,.0f}" for k in scen)
        + "   vs $500,000")
    say("    extra cost to make every rung reach $50,000 (buffer, more of the same holdings): "
        + "; ".join(f"{k}: ${buf[str(k)]:,.0f}" for k in scen))
    out["bookL_totals"] = tot
    out["bookL_buffer"] = buf
    out["bookL_cost"] = cost_tot
    # Portfolio rungs: ratio to the curve scenario
    for h in port:
        if h["holding"] == "VT":
            continue
        w = wins[h["holding"]]
        T = date(int(w["bookL_pays_year"]), 1, 1)
        fl = holder_flows(h["holding"], w, h["units"], s, look, H, F)
        px = w["price"] if w["type"] == "ETF" else w["price"] + accrued(w["coupon"], w["mat"], s)
        cost = h["units"] * px / (100 if w["type"] == "Treasury" else 1)
        y = irr(fl, s, cost)
        vc = grow(fl, T, "curve", cv)
        out["portfolio"].append({"holding": h["holding"], "own_yield": y, "v_curve": vc,
                                 **{f"ratio_{k}": grow(fl, T, (y if k == "own" else y - 0.02 if k == "own-2pp" else k), cv) / vc
                                    for k in scen[:-1]}})
    say("    Portfolio tab rungs, delivered value vs the curve scenario: "
        + "; ".join(f"{p['holding'].split(' 15-')[0]} 0%: {p['ratio_0.0']:.1%}" for p in out["portfolio"]))
    return out


# ------------------------------------------------------------------------------------------------ [F] plan split
def section_f(row, res_a):
    say("\n[F] Plan split on 2 Jan 2028 (E6 [7] method) on this curve")
    y1, y5 = float(row["1 Yr"]) / 100, float(row["5 Yr"]) / 100
    out = {}
    for b in ("exact", "nov15"):
        L = res_a[b]
        left = DEP1 - L["fwd_2027"]
        G = left * (1 + y1) + DEP2
        floor = DEP2 / (1 + y5) ** 5
        tot = L["fwd_2028"] + G
        out[b] = {"ladder": L["fwd_2028"] / tot, "floor": floor / tot, "fund": (G - floor) / tot, "total": tot,
                  "fund_usd": G - floor, "floor_cost": floor, "leftover_2027": left}
        say(f"    {b:6s}: ladder {L['fwd_2028'] / tot:.1%} / floor {floor / tot:.1%} / stock fund {(G - floor) / tot:.1%} "
            f"of ${tot:,.0f} (fund ${G - floor:,.0f}; floor costs ${floor:,.0f}; 2027 leftover ${left:,.0f})")
    say("    (the Portfolio tab types in 65.9 / 24.3 (+1 cash) / 8.7, from E6 [7] on the 25 Sep curve)")
    return out


# ---------------------------------------------------------------------------------------------------- [G] history
def section_g(row):
    say("\n[G] History: the same ten payments on every Treasury par curve 1990-2026 (same time to maturity as on "
        f"{row['_date']})")
    files = sorted(glob.glob(os.path.join(ROOT, "rab/data/treasury_par_1990_1999/*.csv"))) + \
        sorted(f for f in glob.glob(os.path.join(ROOT, "rab/data/treasury_par_2000_2026/*.csv")) if "refetch" not in f)
    rows = load_rows(files)
    D = row["_date"]
    rows = [r for r in rows if r["_date"] <= D]
    res = {}
    for basis in ("nov15", "exact"):
        offs = [p - D for p in pay_dates(basis)]
        offa = A27 - D
        series = []
        for r in rows:
            try:
                cv = Curve(r)
            except Exception:  # a day whose tenors are all blank
                continue
            d = r["_date"]
            a = d + offa
            spot = sum(PAY * cv.df(d + o) for o in offs)
            fwd = spot / cv.df(a)
            dep = DEP2 * cv.df(a + timedelta(days=365)) / cv.df(a)
            series.append((d, spot, fwd, max(0.0, fwd - DEP1 - dep)))
        last = series[-1]
        assert last[0] == D
        out = {"days": len(series), "first": series[0][0].isoformat(), "last": D.isoformat()}
        for lab, i in (("spot", 1), ("fwd_2027", 2)):
            y20 = [x[i] for x in series if x[0].year == 2020]
            mx = max(series, key=lambda x: x[i])
            cheaper = [x[0] for x in series if x[i] <= last[i] and x[0] < D]
            since00 = [x for x in series if x[0].year >= 2000]
            out[lab] = {"today": last[i], "y2020_median": st.median(y20), "y2020_min": min(y20), "y2020_max": max(y20),
                        "y2020_max_date": max((x for x in series if x[0].year == 2020), key=lambda x: x[i])[0].isoformat(),
                        "max": mx[i], "max_date": mx[0].isoformat(),
                        "last_date_at_or_below_today": cheaper[-1].isoformat() if cheaper else None,
                        "share_days_le_300k_since_2000": sum(x[i] <= DEP1 for x in since00) / len(since00),
                        "share_days_le_300k_since_1990": sum(x[i] <= DEP1 for x in series) / len(series),
                        "share_days_cheaper_than_today_since_2000": sum(x[i] <= last[i] for x in since00[:-1]) / (len(since00) - 1)}
            o = out[lab]
            say(f"    {basis:5s} {lab:8s}: today ${o['today']:,.0f}; 2020 median ${o['y2020_median']:,.0f} (min "
                f"${o['y2020_min']:,.0f}, max ${o['y2020_max']:,.0f} on {o['y2020_max_date']}); highest ${o['max']:,.0f} on "
                f"{o['max_date']}; last day as cheap as today: {o['last_date_at_or_below_today']}; <= $300k on "
                f"{o['share_days_le_300k_since_2000']:.1%} of days since 2000 ({o['share_days_le_300k_since_1990']:.1%} since 1990)")
        s00 = [x for x in series if x[0].year >= 2000]
        unf = [x for x in s00 if x[3] > 0]
        out["unfunded_days_since_2000"] = len(unf)
        out["days_since_2000"] = len(s00)
        out["unfunded_years"] = sorted({x[0].year for x in unf})
        if unf:
            wmax = max(unf, key=lambda x: x[3])
            out["unfunded_worst"] = {"date": wmax[0].isoformat(), "usd_2027": wmax[3]}
        say(f"    {basis:5s} deposit check (gap bigger than the whole 2028 deposit): {len(unf)} of {len(s00)} days since "
            f"2000, years {out['unfunded_years']}"
            + (f"; worst {out['unfunded_worst']['date']} ${out['unfunded_worst']['usd_2027']:,.0f} (2027 dollars)" if unf else ""))
        res[basis] = out
    return res


# -------------------------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--curve-date")
    ap.add_argument("--wins-prices", default="rab/data/wins/wins_prices_2026-09-28.csv")
    ap.add_argument("--portfolio", default="rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv")
    ap.add_argument("--skip-history", action="store_true")
    a = ap.parse_args()
    rows = load_rows([os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
    row = rows[-1] if not a.curve_date else next(r for r in rows if r["_date"] == date.fromisoformat(a.curve_date))
    s = row["_date"]
    say(f"M1 ladder pricer | curve: U.S. Treasury Daily Par Yield Curve {s} ({TSY_URL.format(y=s.year)}) | "
        f"valuation and settlement date {s} | MODEL prices")
    wins = read_wins(os.path.join(ROOT, a.wins_prices))
    port, port_cash = read_portfolio(os.path.join(ROOT, a.portfolio))
    cv = Curve(row)
    res = {"meta": {"curve_date": s.isoformat(), "curve_url": TSY_URL.format(y=s.year),
                    "curve_file": "rab/data/treasury_par_2000_2026/2026.csv", "valuation_date": s.isoformat(),
                    "wins_prices": a.wins_prices, "portfolio_snapshot": a.portfolio,
                    "method": "rab/models/M1_METHOD.md"}}
    res["A"] = section_a(rows, row)
    res["B"] = section_b(cv, wins, port, s)
    res["D"] = section_d(row, s)
    res["B"]["cash_margin"] = cash_margin(row, wins, port, s, res["B"], res["D"])
    res["C"] = section_c(cv, wins, s)
    res["C_table"] = model_price_table(cv, s)
    res["E"] = section_e(cv, wins, port, s, res["D"])
    res["F"] = section_f(row, res["A"])
    if not a.skip_history:
        res["G"] = section_g(row)
    os.makedirs(OUT, exist_ok=True)
    tag = s.isoformat()
    with open(os.path.join(OUT, f"m1_bond_check_{tag}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res["C_table"][0]))
        w.writeheader()
        w.writerows(res["C_table"])
    with open(os.path.join(OUT, f"m1_reinvestment_{tag}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res["E"]["bookL"][0]))
        w.writeheader()
        w.writerows(res["E"]["bookL"])
    json.dump(res, open(os.path.join(OUT, "m1_results.json"), "w"), indent=1, default=str)
    open(os.path.join(OUT, "m1_report.txt"), "w").write("\n".join(REPORT) + "\n")
    say(f"\nwrote rab/models/out/m1_results.json, m1_report.txt, m1_bond_check_{tag}.csv, m1_reinvestment_{tag}.csv")


if __name__ == "__main__":
    main()
