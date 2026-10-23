"""Blind rebuild of M7 (stress scenarios + real value of the $50,000 payments), written from rab/models/M7_SPEC.md only.

Run:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/blind_m7.py   (from the worktree root)
AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blind_curve import (CURVE_DATE, DEPOSIT_2027, DEPOSIT_2028, FLOOR_FACE, JAN_2033, PAY_MATURITIES, PAYMENT, Curve,
                         yearfrac, yearfrac_array)
from blind_m5 import DATA, HIST, N, buy_longest_first, load_annual, load_soy

OUT = os.path.join(HERE, "out", "M7")
os.makedirs(OUT, exist_ok=True)

PAR = N("market.par_curve")
Y5_TODAY = float(PAR["5 Yr"]) / 100.0
R1_TODAY = float(PAR["1 Yr"]) / 100.0
JAN = {t: dt.date(2027 + t, 1, 1) for t in range(0, 7)}
BASE_E = 0.07            # JPM AC World compound
BASE_PI = 0.0234         # T10YIE 28 Sep 2026 (checked against market_inflation_2026-09.csv below)


# ---------------------------------------------------------------------------------------------------------------
# engine
# ---------------------------------------------------------------------------------------------------------------
class ShiftedCurves:
    """Curve at 1 Jan T = today's par curve shifted by s_{T-2027} (pp), bootstrapped after the shift, used forward."""

    def __init__(self, s_pp):
        self.s = list(s_pp)                   # s_0..s_6
        self.c = [Curve.from_tenors(PAR, shift_pp=s) for s in self.s]

    def fwd(self, t, dates):
        """DF_T(d) = DF(d)/DF(T) on the s_t curve; a date at or before T is cash (1)."""
        c = self.c[t]
        tau_T = yearfrac(CURVE_DATE, JAN[t])
        out = []
        for d in np.atleast_1d(dates):
            if (d - JAN[t]).days <= 0:
                out.append(1.0)
            else:
                out.append(float(c.df(yearfrac(CURVE_DATE, d)) / c.df(tau_T)))
        return np.array(out)


def run_scenario(dpre, dy, e, pi, m_cppi=3):
    """dpre in pp; dy[t] pp change during year 2027+t (t=0..5); e[t] fund return; pi[t] inflation t=0..14."""
    dy = np.asarray(dy, float); e = np.asarray(e, float); pi = np.asarray(pi, float)
    s = [dpre + dy[:t].sum() for t in range(7)]
    sc = ShiftedCurves(s)
    C = float(PAYMENT * sc.fwd(0, PAY_MATURITIES).sum())
    R = PAYMENT * sc.fwd(0, PAY_MATURITIES)
    f, L = buy_longest_first(R, DEPOSIT_2027)
    u = 1.0 - f
    r1 = R1_TODAY + dpre / 100.0
    T = float((u * PAYMENT * sc.fwd(1, PAY_MATURITIES)).sum())
    G = L * (1 + r1) + DEPOSIT_2028 - T
    y5 = Y5_TODAY + s[1] / 100.0
    Cf = FLOOR_FACE / (1 + y5) ** 5
    if G < 0:
        F, fund0, S = 0.0, 0.0, -G
    else:
        S = 0.0
        if G >= Cf:
            F, fund0 = FLOOR_FACE, G - Cf
        else:
            F, fund0 = G * (1 + y5) ** 5, 0.0
    fund31 = fund0 * (1 + e[1]) * (1 + e[2]) * (1 + e[3])
    fund33 = fund31 * (1 + e[4]) * (1 + e[5])
    mn = min(fund33, fund31)
    bottom, top, gift, kept, T33 = F, F + fund31 / 2, F + mn / 2, fund33 - mn / 2, F + fund33
    deflator = float(np.prod(1 + pi[:6]))
    real_pay = [PAYMENT / float(np.prod(1 + pi[:5 + k])) for k in range(1, 11)]
    # context rivals on the same path
    b = [(Y5_TODAY + s[t] / 100.0) - 5 * dy[t] / 100.0 for t in range(6)]
    r1_T33 = G * (1 + y5) ** 5 if G >= 0 else G
    A = 0.0
    for t in range(6):
        A += DEPOSIT_2027 if t == 0 else (DEPOSIT_2028 if t == 1 else 0.0)
        A *= 1 + 0.6 * e[t] + 0.4 * b[t]
    reserve33 = float(PAYMENT * sc.fwd(6, PAY_MATURITIES).sum())
    r2_T33 = A - reserve33
    floors = [float(PAYMENT * sc.fwd(t, PAY_MATURITIES).sum() + FLOOR_FACE * sc.fwd(t, [JAN_2033])[0]) for t in range(7)]
    A = 0.0
    broke = False
    for t in range(6):
        A += DEPOSIT_2027 if t == 0 else (DEPOSIT_2028 if t == 1 else 0.0)
        cushion = A - floors[t]
        broke = broke or cushion < 0
        E = min(A, m_cppi * max(cushion, 0.0))
        Sz = A - E
        A = E * (1 + e[t]) + Sz * floors[t + 1] / floors[t]
    r5_T33 = A - reserve33
    return {"dpre": dpre, "s1": s[1], "s6": s[6], "ladder_cost_C": C, "leftover_L": L, "leftover_rate_r1": r1, "topup_T": T,
            "n_rungs_partial": int((u > 1e-12).sum()), "growth_money_G": G, "y5": y5, "floor_cost_Cf": Cf, "floor_face_F": F,
            "fund0": fund0, "fund31": fund31, "fund33": fund33, "bottom": bottom, "top": top, "gift": gift, "kept": kept,
            "T33": T33, "payments_funded": G >= 0, "short_S": S, "deflator_2033": deflator, "real_gift": gift / deflator,
            "real_T33": T33 / deflator, **{f"real_pay_{2032 + k}": real_pay[k - 1] for k in range(1, 11)},
            "real_pay_total": sum(real_pay), "R1_T33": r1_T33, "R2_T33": r2_T33, "R2_reserve33": reserve33,
            "R5_T33": r5_T33, "R5_floor_broken": broke, "R5_floor0": floors[0],
            "cum_e_2028_2032": float(np.prod(1 + e[1:6])) - 1, "sum_dy": float(dy.sum())}


# ---------------------------------------------------------------------------------------------------------------
# scenarios
# ---------------------------------------------------------------------------------------------------------------
def downgrade_events():
    d = pd.read_csv(os.path.join(DATA, "fred", "DGS10.csv"))
    d["date"] = pd.to_datetime(d["observation_date"]).dt.date
    d["y"] = pd.to_numeric(d["DGS10"], errors="coerce")
    d = d.dropna(subset=["y"]).reset_index(drop=True)            # trading days = days with a published yield
    sp = pd.read_csv(os.path.join(HIST, "raw", "yf_GSPC_daily.csv"), skiprows=[1, 2])
    sp = sp.rename(columns={sp.columns[0]: "date"})
    sp["date"] = pd.to_datetime(sp["date"]).dt.date
    sp["close"] = pd.to_numeric(sp["Close"], errors="coerce")
    sp = sp.dropna(subset=["close"]).reset_index(drop=True)
    events = [("S4a", "S&P (5 Aug 2011, after the close)", dt.date(2011, 8, 5)),
              ("S4b", "Fitch (1 Aug 2023, after the close)", dt.date(2023, 8, 1)),
              ("S4c", "Moody's (16 May 2025, after the close)", dt.date(2025, 5, 16))]
    rows = []
    for sid, name, ann in events:
        i0 = d.index[d["date"] <= ann].max()                        # last close before the announcement (announcement date itself)
        i1 = i0 + 20
        j0 = sp.index[sp["date"] <= ann].max(); j1 = j0 + 20
        alt0 = i0 - 1                                               # alternative reading: prior trading day's close
        rows.append({"scenario": sid, "event": name, "announcement": str(ann), "dgs10_start_date": str(d.loc[i0, "date"]),
                     "dgs10_start": d.loc[i0, "y"], "dgs10_end_date": str(d.loc[i1, "date"]), "dgs10_end": d.loc[i1, "y"],
                     "dgs10_change_pp": round(float(d.loc[i1, "y"] - d.loc[i0, "y"]), 2),
                     "alt_prior_close_change_pp": round(float(d.loc[alt0 + 20, "y"] - d.loc[alt0, "y"]), 2),
                     "sp500_start_date": str(sp.loc[j0, "date"]), "sp500_start": sp.loc[j0, "close"],
                     "sp500_end_date": str(sp.loc[j1, "date"]), "sp500_end": sp.loc[j1, "close"],
                     "sp500_change": float(sp.loc[j1, "close"] / sp.loc[j0, "close"] - 1)})
    ev = pd.DataFrame(rows)
    ev.to_csv(os.path.join(OUT, "downgrade_events.csv"), index=False, float_format="%.4f")
    return ev


def build_scenarios(soy, ann, ev):
    soy10 = soy["10 Yr"]
    cpi, weq = ann["cpi_infl"], ann["world_eq"]
    base_dy, base_e, base_pi = [0.0] * 6, [BASE_E] * 6, [BASE_PI] * 15

    def analog(A0, rate_series, ret_series, infl_series, scale=1.0):
        dy = [float(rate_series.loc[A0 + t + 1] - rate_series.loc[A0 + t]) * scale for t in range(6)]
        e = [float(ret_series.loc[A0 + t]) for t in range(6)]
        pi = [float(infl_series.loc[A0 + t]) for t in range(15)]
        return dy, e, pi

    S = {}
    S["S0"] = ("Base", 0.0, base_dy, base_e, base_pi)
    dy, e, pi = analog(1973, soy10, weq, cpi); S["S1"] = ("1970s stagflation (1973 plays 2027)", 0.0, dy, e, pi)
    dy, e, pi = analog(1990, ann["jpn_ltrate"], ann["jpn_eq"], ann["jpn_cpi_infl"]); S["S2"] = ("Japan's lost decade (1990 plays 2027)", 0.0, dy, e, pi)
    S["S2b"] = ("Japan, rates fall first (-1.00 pp before the ladder)", -1.00, dy, e, pi)
    dy = list(base_dy); e = list(base_e); dy[1] = float(soy10.loc[2023] - soy10.loc[2022]); e[1] = float(weq.loc[2022])
    pi3 = [float(cpi.loc[y]) for y in range(2021, 2026)] + [BASE_PI] * 10
    S["S3"] = ("2022 in 2028", 0.0, dy, e, pi3)
    dy = list(base_dy); e = list(base_e); dy[0] = float(soy10.loc[2023] - soy10.loc[2022]); e[0] = float(weq.loc[2022])
    S["S3b"] = ("2022 in 2027", 0.0, dy, e, pi3)
    for sid in ("S4a", "S4b", "S4c"):
        r = ev.set_index("scenario").loc[sid]
        S[sid] = (f"Downgrade, {r['event']}: DGS10 {r['dgs10_change_pp']:+.2f} pp over 20 trading days", float(r["dgs10_change_pp"]), base_dy, base_e, base_pi)
    e = list(base_e); e[1] = -0.20
    S["S4d"] = ("Downgrade plus buyers' strike (hypothetical): +1.00 pp, fund -20% in 2028", 1.00, base_dy, e, base_pi)
    dy, e, pi = analog(1928, soy10, weq, cpi); S["S5"] = ("Great Depression (1928 plays 2027)", 0.0, dy, e, pi)
    dy = list(base_dy); e = list(base_e); dy[1] = float(soy10.loc[2009] - soy10.loc[2008]); e[1] = float(weq.loc[2008])
    S["S6"] = ("2008 in 2028", 0.0, dy, e, base_pi)
    dy, e, pi = analog(1966, soy10, weq, cpi); S["S7"] = ("Great Inflation (1966 plays 2027)", 0.0, dy, e, pi)
    # Unit check, not a headline. The spec's S2 line reads "dy = (jpn_ltrate A0+t+1 - A0+t)/100"; jpn_ltrate is in
    # percent (7.36 in 1990), so the literal "/100" gives a decimal while S1's dy (10 Yr differences) is in percentage
    # points. S2 above uses percentage points (consistent with S1 and with dpre); S2_lit applies the "/100" literally.
    dy2, e2, pi2 = analog(1990, ann["jpn_ltrate"], ann["jpn_eq"], ann["jpn_cpi_infl"], scale=0.01)
    S["S2_lit"] = ("Japan, dy read literally as (ltrate diff)/100 (spec unit check, not a headline)", 0.0, dy2, e2, pi2)
    return S


def thresholds():
    """On the S0 path with dpre = -x (dy = 0): x where C = 300,000; fund0 = 0; G = 0."""
    base = lambda x: run_scenario(-x, [0.0] * 6, [BASE_E] * 6, [BASE_PI] * 15)
    xa = brentq(lambda x: base(x)["ladder_cost_C"] - DEPOSIT_2027, 0.0, 5.0, xtol=1e-6)
    # (b) fund0 falls to 0 exactly where G = Cf (the floor is still 150,000 there); G - Cf is continuous in x
    xb = brentq(lambda x: base(x)["growth_money_G"] - base(x)["floor_cost_Cf"], 0.0, 5.0, xtol=1e-6)
    xc = brentq(lambda x: base(x)["growth_money_G"], 0.0, 8.0, xtol=1e-6)
    out = {"a_topup_starts_C_300k_bp": 100 * xa, "b_fund0_zero_floor_150k_bp": 100 * xb, "c_payment_unfunded_G_zero_bp": 100 * xc}
    for k, x in (("a", xa), ("b", xb), ("c", xc)):
        r = base(x)
        out[f"{k}_check"] = {"x_pp": x, "C": r["ladder_cost_C"], "G": r["growth_money_G"], "Cf": r["floor_cost_Cf"], "F": r["floor_face_F"],
                             "fund0": r["fund0"], "y5": r["y5"], "T": r["topup_T"]}
    return out


# ---------------------------------------------------------------------------------------------------------------
# real value of the payments
# ---------------------------------------------------------------------------------------------------------------
def real_values(S, ann, mi):
    paths = {"breakeven_T10YIE_2.34": [BASE_PI] * 15,
             "cleveland_EXPINF10YR_latest": [float(mi.loc["EXPINF10YR", "value"]) / 100.0] * 15,
             "jpm_ltcma_2026_2.50": [0.025] * 15, "fed_target_2.00": [0.02] * 15}
    for sid in ("S1", "S2", "S3", "S5", "S7"):
        paths[f"{sid}_{S[sid][0].split(' (')[0]}"] = S[sid][4]
    rows = []
    for name, pi in paths.items():
        pi = np.asarray(pi)
        rv = [PAYMENT / float(np.prod(1 + pi[:5 + k])) for k in range(1, 11)]
        rows.append({"path": name, "annual_avg_infl_15y": float(np.prod(1 + pi) ** (1 / 15) - 1),
                     **{f"real_{2032 + k}": rv[k - 1] for k in range(1, 11)}, "total_real": sum(rv), "real_2033": rv[0], "real_2042": rv[9],
                     "total_nominal": 10 * PAYMENT})
    rvp = pd.DataFrame(rows)
    rvp.to_csv(os.path.join(OUT, "real_value_paths.csv"), index=False, float_format="%.2f")
    cpi = ann["cpi_infl"]
    W = []
    for Y in range(1872, 2012):
        pi = np.array([cpi.loc[Y + t] for t in range(15)])
        W.append([PAYMENT / float(np.prod(1 + pi[:5 + k])) for k in range(1, 11)] + [float(np.prod(1 + pi) ** (1 / 15) - 1)])
    W = np.array(W)
    dist = pd.DataFrame({"payment_year": [2032 + k for k in range(1, 11)],
                         "p5": np.percentile(W[:, :10], 5, axis=0), "p50": np.percentile(W[:, :10], 50, axis=0),
                         "p95": np.percentile(W[:, :10], 95, axis=0), "min": W[:, :10].min(axis=0), "max": W[:, :10].max(axis=0)})
    totals = W[:, :10].sum(axis=1)
    dist_tot = {"n_windows": int(W.shape[0]), "first_Y": 1872, "last_Y": 2011, "total_p5": float(np.percentile(totals, 5)),
                "total_p50": float(np.percentile(totals, 50)), "total_p95": float(np.percentile(totals, 95)),
                "worst_window_Y": int(1872 + totals.argmin()), "worst_total": float(totals.min()),
                "infl15_p5": float(np.percentile(W[:, 10], 5)), "infl15_p50": float(np.percentile(W[:, 10], 50)), "infl15_p95": float(np.percentile(W[:, 10], 95))}
    dist.to_csv(os.path.join(OUT, "real_value_history_distribution.csv"), index=False, float_format="%.2f")
    h19 = {"convention": "2.5% a year, 7 and 16 years from 2026 (insight_v1 I4)", "2033": PAYMENT / 1.025 ** 7, "2042": PAYMENT / 1.025 ** 16,
           "reference": N("ref.H19.real_value_50k"), "sourced_input": "JPM 2026 LTCMA U.S. Inflation 2.50% (jpm_ltcma_2026_usd.csv)",
           "M7_convention_2.50_from_1Jan2027": {"2033": PAYMENT / 1.025 ** 6, "2042": PAYMENT / 1.025 ** 15}}
    return rvp, dist, dist_tot, h19


def figures(table, rvp, dist):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    t = table[~table["scenario"].str.endswith("_lit")].set_index("scenario")   # unit-check rows are not drawn
    fig, ax = plt.subplots(figsize=(12, 5))
    x = np.arange(len(t))
    ax.bar(x - 0.2, t["bottom"] / 1000, width=0.4, color="tab:green", label="2031 bottom (floor F)")
    ax.bar(x - 0.2, (t["gift"] - t["bottom"]) / 1000, bottom=t["bottom"] / 1000, width=0.4, color="tab:olive", label="gift above the floor")
    ax.bar(x + 0.2, t["T33"] / 1000, width=0.4, color="tab:blue", alpha=0.6, label="all money 1 Jan 2033 (T33)")
    ax.plot(x, t["real_gift"] / 1000, "k_", markersize=14, label="real gift (2027 dollars)")
    ax.set_xticks(x); ax.set_xticklabels(t.index, fontsize=8)
    ax.set_ylabel("$ thousands"); ax.set_title("M7 (blind): Root-and-Branch under each stress path; payments funded in every scenario shown")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y"); fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m7_stress.png"), dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    yrs = dist["payment_year"]
    ax.fill_between(yrs, dist["p5"] / 1000, dist["p95"] / 1000, color="tab:gray", alpha=0.25, label="history 1872-2011: 5th-95th pct of 15-year windows")
    ax.plot(yrs, dist["p50"] / 1000, color="tab:gray", label="history median")
    for _, r in rvp.iterrows():
        vals = [r[f"real_{y}"] / 1000 for y in yrs]
        ax.plot(yrs, vals, lw=1.2 if r["path"].startswith(("breakeven", "jpm", "fed", "cleveland")) else 0.9,
                ls="-" if r["path"].startswith(("breakeven", "jpm", "fed", "cleveland")) else "--", label=r["path"][:36])
    ax.axhline(50, color="black", lw=0.8, ls=":")
    ax.set_ylabel("Real value of a $50,000 payment ($ thousands, 1 Jan 2027 dollars)"); ax.set_xlabel("Payment year")
    ax.set_title("M7 (blind): what each fixed $50,000 payment buys, under sourced inflation paths")
    ax.legend(fontsize=7, ncol=2); ax.grid(alpha=0.3); fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m7_real_value.png"), dpi=150); plt.close(fig)


def main():
    soy, ann = load_soy(), load_annual()
    mi = pd.read_csv(os.path.join(HIST, "market_inflation_2026-09.csv")).set_index("series")
    assert abs(float(mi.loc["T10YIE", "value"]) / 100.0 - BASE_PI) < 1e-9
    ev = downgrade_events()
    S = build_scenarios(soy, ann, ev)
    rows = []
    for sid, (name, dpre, dy, e, pi) in S.items():
        r = run_scenario(dpre, dy, e, pi)
        rows.append({"scenario": sid, "name": name, **r, "dy_path_pp": [round(v, 3) for v in dy], "e_path": [round(v, 4) for v in e],
                     "pi_first6": [round(v, 4) for v in pi[:6]]})
    table = pd.DataFrame(rows)
    table.to_csv(os.path.join(OUT, "stress_table.csv"), index=False, float_format="%.2f")
    base = table.set_index("scenario").loc["S0"]
    checks = {"S0_C_vs_numbers": (float(base["ladder_cost_C"]), float(N("laura.ladder.cost_2027_strips"))),
              "S0_fund0_vs_numbers": (float(base["fund0"]), float(N("laura.stock_fund_2028_usd.strips"))),
              "S0_Cf_vs_numbers": (float(base["floor_cost_Cf"]), float(N("laura.floor_cost_2028")))}
    thr = thresholds()
    rvp, dist, dist_tot, h19 = real_values(S, ann, mi)
    figures(table, rvp, dist)

    res = {"model": "M7 blind rebuild", "spec": "rab/models/M7_SPEC.md", "curve_date": str(CURVE_DATE), "checks_vs_numbers_yaml": checks,
           "downgrade_events": ev.to_dict(orient="records"), "thresholds": thr, "stress_table": table.to_dict(orient="records"),
           "real_value_paths": rvp.to_dict(orient="records"), "real_value_history": {"per_payment": dist.to_dict(orient="records"), **dist_tot},
           "H19": h19}
    with open(os.path.join(OUT, "M7_results.json"), "w") as f:
        json.dump(res, f, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))

    L = ["M7 blind rebuild: stress scenarios and the real value of the payments (MODEL, 28 Sep 2026 curve)", "=" * 110]
    L.append("Checks vs numbers.yaml (S0): " + "; ".join(f"{k}: {a:,.2f} vs {b:,.2f}" for k, (a, b) in checks.items()))
    L.append("")
    L.append("Downgrade windows (FRED DGS10, last close before the after-hours announcement -> 20 trading days later; S&P 500 secondary):")
    with pd.option_context("display.width", 300, "display.max_columns", 40):
        L.append(ev[["scenario", "event", "dgs10_start_date", "dgs10_start", "dgs10_end_date", "dgs10_end", "dgs10_change_pp", "alt_prior_close_change_pp", "sp500_change"]].to_string(index=False))
    L.append("")
    L.append("Stress table:")
    cols = ["scenario", "name", "dpre", "s1", "ladder_cost_C", "topup_T", "growth_money_G", "y5", "floor_face_F", "fund0", "fund31", "fund33", "bottom", "top", "gift",
            "T33", "payments_funded", "real_gift", "real_T33", "real_pay_2033", "real_pay_2042", "real_pay_total", "R1_T33", "R2_T33", "R5_T33", "R5_floor_broken"]
    with pd.option_context("display.width", 400, "display.max_columns", 60, "display.float_format", "{:,.2f}".format, "display.max_colwidth", 40):
        L.append(table[cols].to_string(index=False))
    L.append("")
    L.append("Thresholds (S0 path, dpre = -x persisting to Jan 2028, dy = 0):")
    for k in ("a_topup_starts_C_300k_bp", "b_fund0_zero_floor_150k_bp", "c_payment_unfunded_G_zero_bp"):
        L.append(f"  {k:36s} {thr[k]:8.1f} bp   check: {thr[k[0] + '_check']}")
    L.append("")
    L.append("Real value of the ten $50,000 payments (1 Jan 2027 dollars):")
    with pd.option_context("display.width", 300, "display.max_columns", 40, "display.float_format", "{:,.0f}".format):
        L.append(rvp[["path", "annual_avg_infl_15y", "real_2033", "real_2042", "total_real"]].assign(annual_avg_infl_15y=lambda d: (100 * d.annual_avg_infl_15y).round(2)).to_string(index=False))
        L.append("History, every 15-year window 1872..2011 (" + str(dist_tot["n_windows"]) + " windows):")
        L.append(dist.to_string(index=False))
    L.append(f"  totals: p5 {dist_tot['total_p5']:,.0f}  p50 {dist_tot['total_p50']:,.0f}  p95 {dist_tot['total_p95']:,.0f}; worst window {dist_tot['worst_window_Y']} ({dist_tot['worst_total']:,.0f})")
    L.append(f"  H19 reproduction: 2033 {h19['2033']:,.0f} (ref {h19['reference']['2033']}), 2042 {h19['2042']:,.0f} (ref {h19['reference']['2042']}); {h19['convention']}; sourced input: {h19['sourced_input']}")
    L.append("")
    L.append("Assumptions: parallel shifts of today's par curve (bootstrap after the shift); analog returns annual in each market's own currency; no fees;"
             " the ladder is held to maturity, so price moves after 1 Jan 2027 never change the payments.")
    open(os.path.join(OUT, "M7_report.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
