"""Blind rebuild of M5 (century backtest + cost-of-certainty history), written from rab/models/M5_SPEC.md only.

Inputs (spec section 1): H1 daily par files 1990-2026, H2 FRED daily 1962-1989, H3 Shiller monthly, H4 start-of-year
curves, H5 annual returns, N = rab/numbers.yaml. Outputs go to rab/verification/blind/out/M5/.

Run:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/blind_m5.py   (from the worktree root)
AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import os
import sys

import numpy as np
import pandas as pd
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
from blind_curve import (CURVE_DATE, DEPOSIT_2027, DEPOSIT_2028, FLOOR_FACE, JAN_2027, JAN_2028, PAY_MATURITIES,
                         PAYMENT, TENOR_ORDER, Curve, many_curves_df, yearfrac, yearfrac_array)

DATA = os.path.join(ROOT, "rab", "data")
HIST = os.path.join(DATA, "history")
OUT = os.path.join(HERE, "out", "M5")
os.makedirs(OUT, exist_ok=True)

NUMBERS = yaml.safe_load(open(os.path.join(ROOT, "rab", "numbers.yaml")))["numbers"]


def N(key):
    return NUMBERS[key]["value"]


# ---------------------------------------------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------------------------------------------
def load_h1() -> pd.DataFrame:
    """Daily Treasury par curve 1990-2026 in TENOR_ORDER layout (percent, NaN for blanks), one row per date."""
    frames = []
    for f in sorted(glob.glob(os.path.join(DATA, "treasury_par_1990_1999", "*.csv"))
                    + glob.glob(os.path.join(DATA, "treasury_par_2000_2026", "*.csv"))):
        d = pd.read_csv(f)
        d["date"] = pd.to_datetime(d["Date"], format="%m/%d/%Y").dt.date
        frames.append(d)
    h1 = pd.concat(frames, ignore_index=True)
    for k in TENOR_ORDER:
        if k not in h1.columns:
            h1[k] = np.nan
    h1 = h1[["date"] + TENOR_ORDER].sort_values("date").reset_index(drop=True)
    assert h1["date"].is_unique
    # a published row with every tenor blank (10/11/2010, Columbus Day) is not a curve: dropped, counted in the notes
    empty = h1[TENOR_ORDER].isna().all(axis=1)
    load_h1.dropped = [str(d) for d in h1.loc[empty, "date"]]
    return h1[~empty].reset_index(drop=True)


def load_h2() -> pd.DataFrame:
    h2 = pd.read_csv(os.path.join(HIST, "daily_curves_1962_1989.csv"))
    h2["date"] = pd.to_datetime(h2["date"]).dt.date
    for k in TENOR_ORDER:
        if k not in h2.columns:
            h2[k] = np.nan
    return h2[["date"] + TENOR_ORDER].sort_values("date").reset_index(drop=True)


def load_h3_monthly_flat() -> pd.DataFrame:
    """Shiller monthly GS10 1871-01 .. 1961-12 as flat curves dated the 1st of the month."""
    s = pd.read_csv(os.path.join(HIST, "shiller_monthly.csv"))
    s = s[(s["year"] >= 1871) & (s["year"] <= 1961)].copy()
    s["date"] = [dt.date(int(y), int(m), 1) for y, m in zip(s["year"], s["month"])]
    out = pd.DataFrame({"date": s["date"].values})
    for k in TENOR_ORDER:
        out[k] = np.nan
    out["10 Yr"] = s["GS10"].values
    return out.sort_values("date").reset_index(drop=True)


def load_soy() -> pd.DataFrame:
    soy = pd.read_csv(os.path.join(HIST, "soy_curves.csv"))
    return soy.set_index("year")


def load_annual() -> pd.DataFrame:
    return pd.read_csv(os.path.join(HIST, "annual_history.csv")).set_index("year")


def curve_from_row(row) -> Curve:
    return Curve.from_tenors({k: row[k] for k in TENOR_ORDER if k in row.index and pd.notna(row[k])})


def load_fred_first_of_month(dates) -> pd.DataFrame:
    """FRED DGS values for the given dates, in TENOR_ORDER layout (percent, NaN where blank/absent)."""
    series = {"1 Mo": "DGS1MO", "3 Mo": "DGS3MO", "6 Mo": "DGS6MO", "1 Yr": "DGS1", "2 Yr": "DGS2", "3 Yr": "DGS3",
              "5 Yr": "DGS5", "7 Yr": "DGS7", "10 Yr": "DGS10", "20 Yr": "DGS20", "30 Yr": "DGS30"}
    out = pd.DataFrame({"date": list(dates)})
    for k in TENOR_ORDER:
        out[k] = np.nan
    for tenor, sid in series.items():
        f = pd.read_csv(os.path.join(DATA, "fred", f"{sid}.csv"))
        f["date"] = pd.to_datetime(f["observation_date"]).dt.date
        f[sid] = pd.to_numeric(f[sid], errors="coerce")
        m = dict(zip(f["date"], f[sid]))
        out[tenor] = [m.get(d, np.nan) for d in out["date"]]
    return out


# ---------------------------------------------------------------------------------------------------------------
# Part A: cost-of-certainty series
# ---------------------------------------------------------------------------------------------------------------
TAU_D = yearfrac_array(CURVE_DATE, PAY_MATURITIES)   # same time to maturity as on D, for every curve date


def v0_series(frame: pd.DataFrame) -> np.ndarray:
    rows = frame[TENOR_ORDER].to_numpy(dtype=float)
    return PAYMENT * many_curves_df(rows, TAU_D).sum(axis=1)


def part_a(h1, h2, h3):
    a1 = pd.DataFrame({"date": h1["date"], "V0": v0_series(h1), "basis": "treasury_par"})
    a2 = pd.DataFrame({"date": h2["date"], "V0": v0_series(h2), "basis": "fred_cmt"})
    a3 = pd.DataFrame({"date": h3["date"], "V0": v0_series(h3), "basis": "flat_shiller_gs10"})
    ser = pd.concat([a3, a2, a1], ignore_index=True).sort_values("date").reset_index(drop=True)
    ser["year"] = [d.year for d in ser["date"]]
    ser.to_csv(os.path.join(OUT, "cost_of_certainty_series.csv"), index=False,
               columns=["date", "V0", "basis"], float_format="%.2f")
    by_year = ser.groupby("year").agg(min=("V0", "min"), median=("V0", "median"), max=("V0", "max"),
                                      n=("V0", "size"), basis=("basis", "first")).reset_index()
    by_year.to_csv(os.path.join(OUT, "cost_of_certainty_by_year.csv"), index=False, float_format="%.2f")

    v0_D = float(a1.loc[a1["date"] == CURVE_DATE, "V0"].iloc[0])
    h = {}
    # (i) reproduction of M1 G on the H1 days
    y2020 = a1[[d.year == 2020 for d in a1["date"]]]
    imax = y2020["V0"].idxmax()
    h["V0_D"] = round(v0_D, 2)
    h["cost_2020_median"] = round(float(y2020["V0"].median()), 2)
    h["cost_2020_min"] = round(float(y2020["V0"].min()), 2)
    h["cost_2020_max"] = round(float(y2020.loc[imax, "V0"]), 2)
    h["cost_2020_max_date"] = str(y2020.loc[imax, "date"])
    before = a1[(a1["date"] < CURVE_DATE) & (a1["V0"] <= v0_D)]
    h["cheapest_since_spot"] = str(before["date"].max())
    since2000 = a1[[d.year >= 2000 for d in a1["date"]]]
    h["share_days_le_300k_since_2000_spot"] = round(float((since2000["V0"] <= 300_000).mean()), 4)
    h["share_days_le_300k_since_1990_spot"] = round(float((a1["V0"] <= 300_000).mean()), 4)
    h["days_priced_since_2000"] = int(len(since2000))
    h["days_priced_1990_2026"] = int(len(a1))
    # (ii) extended series
    for tag, sub in (("since_1871", ser), ("since_1962", ser[ser["year"] >= 1962])):
        i_lo, i_hi = sub["V0"].idxmin(), sub["V0"].idxmax()
        h[f"lowest_{tag}"] = {"usd": round(float(sub.loc[i_lo, "V0"]), 2), "date": str(sub.loc[i_lo, "date"]),
                              "basis": sub.loc[i_lo, "basis"]}
        h[f"highest_{tag}"] = {"usd": round(float(sub.loc[i_hi, "V0"]), 2), "date": str(sub.loc[i_hi, "date"]),
                               "basis": sub.loc[i_hi, "basis"]}
    ser["ym"] = [(d.year, d.month) for d in ser["date"]]
    monthly = ser.groupby("ym", sort=True).first().reset_index()   # first curve date of each month
    monthly["year"] = [d.year for d in monthly["date"]]
    monthly.to_csv(os.path.join(OUT, "cost_of_certainty_monthly.csv"), index=False,
                   columns=["date", "V0", "basis"], float_format="%.2f")
    h["n_months_since_1871"] = int(len(monthly))
    h["share_months_le_V0D_since_1871"] = round(float((monthly["V0"] <= v0_D).mean()), 4)
    h["share_months_le_300k_since_1871"] = round(float((monthly["V0"] <= 300_000).mean()), 4)
    h["share_months_le_V0D_since_1962"] = round(float((monthly.loc[monthly["year"] >= 1962, "V0"] <= v0_D).mean()), 4)
    h["share_months_le_300k_since_1962"] = round(float((monthly.loc[monthly["year"] >= 1962, "V0"] <= 300_000).mean()), 4)
    h["share_years_median_below_V0D_1871_2026"] = round(float((by_year["median"] < v0_D).mean()), 4)
    h["n_years_1871_2026"] = int(len(by_year))
    yrs_below = by_year.loc[by_year["median"] < v0_D, "year"].tolist()
    h["years_median_below_V0D"] = yrs_below
    return ser, monthly, by_year, v0_D, h


def part_a4(h1, h2, monthly, v0_D, h):
    """Approximation checks: (a) flat vs full curve 1962-2026 (first date of each month); (b) FRED vs Treasury 1990-2026."""
    daily = pd.concat([h2, h1], ignore_index=True)
    daily["ym"] = [(d.year, d.month) for d in daily["date"]]
    first = daily.groupby("ym", sort=True).first().reset_index()
    full = v0_series(first)
    flat_rows = first.copy()
    for k in TENOR_ORDER:
        if k != "10 Yr":
            flat_rows[k] = np.nan
    flat = v0_series(flat_rows)
    chk = pd.DataFrame({"date": first["date"], "V0_full": full, "V0_flat10y": flat, "flat_over_full_minus_1": flat / full - 1})
    chk["decade"] = [10 * (d.year // 10) for d in chk["date"]]
    by_dec = chk.groupby("decade")["flat_over_full_minus_1"].agg(
        median="median", p05=lambda s: s.quantile(0.05), p95=lambda s: s.quantile(0.95), n="size").reset_index()
    overall = chk["flat_over_full_minus_1"]
    by_dec = pd.concat([by_dec, pd.DataFrame([{"decade": "1962-2026", "median": overall.median(),
                                                "p05": overall.quantile(0.05), "p95": overall.quantile(0.95),
                                                "n": len(overall)}])], ignore_index=True)
    chk.to_csv(os.path.join(OUT, "check_flat_vs_full_curve.csv"), index=False, float_format="%.6f")
    by_dec.to_csv(os.path.join(OUT, "check_flat_vs_full_by_decade.csv"), index=False, float_format="%.5f")
    e_med, e_p95, e_p05 = float(overall.median()), float(overall.quantile(0.95)), float(overall.quantile(0.05))
    h["flat_vs_full_1962_2026"] = {"median": round(e_med, 5), "p05": round(e_p05, 5), "p95": round(e_p95, 5), "n": int(len(overall))}
    # sensitivity: divide every pre-1962 monthly V0 by (1 + e)
    for tag, e in (("median", e_med), ("p95", e_p95)):
        adj = monthly["V0"].where(monthly["year"] >= 1962, monthly["V0"] / (1 + e))
        h[f"share_months_le_V0D_since_1871_adj_{tag}"] = round(float((adj <= v0_D).mean()), 4)
        h[f"share_months_le_300k_since_1871_adj_{tag}"] = round(float((adj <= 300_000).mean()), 4)
    # (b) FRED vs Treasury file on the first date of each month 1990-2026
    h1m = h1.copy()
    h1m["ym"] = [(d.year, d.month) for d in h1m["date"]]
    firsts = h1m.groupby("ym", sort=True).first().reset_index()
    fred = load_fred_first_of_month(firsts["date"])
    ok = fred[TENOR_ORDER].notna().any(axis=1).to_numpy()
    v_h1 = v0_series(firsts[ok])
    v_fred = v0_series(fred[ok])
    cmp_ = pd.DataFrame({"date": firsts.loc[ok, "date"].values, "V0_treasury": v_h1, "V0_fred": v_fred, "diff": v_fred - v_h1})
    cmp_.to_csv(os.path.join(OUT, "check_fred_vs_treasury.csv"), index=False, float_format="%.2f")
    i = cmp_["diff"].abs().idxmax()
    h["fred_vs_treasury_1990_2026"] = {"n_months": int(len(cmp_)), "largest_abs_diff_usd": round(float(cmp_.loc[i, "diff"].__abs__()), 2),
                                        "date": str(cmp_.loc[i, "date"]), "median_abs_diff_usd": round(float(cmp_["diff"].abs().median()), 2)}
    return h


def fig_cost(monthly, v0_D, h):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(11, 5.5))
    m = monthly.copy()
    m["dt"] = pd.to_datetime(m["date"])
    pre = m[m["year"] < 1962]
    post = m[m["year"] >= 1962]
    ax.plot(pre["dt"], pre["V0"] / 1000, ls="--", lw=1.1, color="tab:gray", label="1871-1961: flat curve at the 10-year rate")
    ax.plot(post["dt"], post["V0"] / 1000, lw=1.2, color="tab:blue", label="1962-2026: full Treasury curve")
    ax.axhline(300, color="tab:red", lw=1, ls=":", label="$300,000 deposit")
    ax.axhline(v0_D / 1000, color="tab:green", lw=1, ls="-.", label=f"28 Sep 2026: ${v0_D:,.0f}")
    ax.annotate("28 Sep 2026", (pd.Timestamp(CURVE_DATE), v0_D / 1000), xytext=(-90, -40), textcoords="offset points",
                arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.annotate(f"4 Aug 2020 peak ${h['cost_2020_max']:,.0f}", (pd.Timestamp(h["cost_2020_max_date"]), h["cost_2020_max"] / 1000),
                xytext=(-160, 10), textcoords="offset points", arrowprops=dict(arrowstyle="->"), fontsize=9)
    ax.set_ylabel("Cost of the ten $50,000 payments ($ thousands, MODEL)")
    ax.set_title("Cost of certainty: what Laura's ten payments would have cost on every Treasury curve, 1871-2026")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_cost_of_certainty.png"), dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------------------------------------------
# Part B: start-year backtest
# ---------------------------------------------------------------------------------------------------------------
TAU_2027 = yearfrac_array(JAN_2027, PAY_MATURITIES)   # tau_k
TAU_2028 = yearfrac_array(JAN_2028, PAY_MATURITIES)   # tau'_k


def buy_longest_first(rung_costs: np.ndarray, money: float):
    """Return (fractions bought f_k, leftover)."""
    f = np.zeros_like(rung_costs)
    m = money
    for k in range(len(rung_costs) - 1, -1, -1):
        fk = min(1.0, m / rung_costs[k]) if rung_costs[k] > 0 else 1.0
        f[k] = fk
        m -= fk * rung_costs[k]
    return f, max(m, 0.0)


def window(Y: int, view: str, series: str, soy: pd.DataFrame, ann: pd.DataFrame, e_col: pd.Series, today: dict):
    """One backtest window; returns a dict of every B1-B7 quantity."""
    row = {"view": view, "fund_series": series, "Y": Y, "basis_Y": soy.loc[Y, "basis"], "basis_Y1": soy.loc[Y + 1, "basis"]}
    if view == "hist":
        cY = curve_from_row(soy.loc[Y])
        cY1 = curve_from_row(soy.loc[Y + 1])
        R = PAYMENT * cY.df(TAU_2027)
        C = float(R.sum())
        f, L = buy_longest_first(R, DEPOSIT_2027)
        u = 1.0 - f
        one_yr = soy.loc[Y, "1 Yr"]
        r1 = float(one_yr) / 100.0 if pd.notna(one_yr) else float(ann.loc[Y, "us_bill"])
        T = float((u * PAYMENT * cY1.df(TAU_2028)).sum())
        y5 = cY1.par_yield(5.0)
    else:  # today_yields / today_yields_rescaled
        C = today["C"]
        L = today["L"]
        r1 = today["r1"]
        T = 0.0
        y5 = today["y5"]
        u = np.zeros(10)
    G = L * (1 + r1) + DEPOSIT_2028 - T
    row.update(ladder_cost_C=C, leftover_L=L, leftover_rate_r1=r1, topup_T=T, growth_money_G=G, y5=y5,
               n_rungs_partial=int((u > 1e-12).sum()))
    Cf = FLOOR_FACE / (1 + y5) ** 5
    row["floor_cost_Cf"] = Cf
    if G < 0:
        S = -G
        F, fund0 = 0.0, 0.0
        Fv, fund0v = 0.0, 0.0
    else:
        S = 0.0
        if G >= Cf:
            F, fund0 = FLOOR_FACE, G - Cf
        else:
            F, fund0 = G * (1 + y5) ** 5, 0.0
        # IPS-wording variant: floor repays the whole remainder of the deposit after the top-up
        Fv = FLOOR_FACE - T
        fund0v = G - Fv / (1 + y5) ** 5
        if fund0v < 0:
            Fv, fund0v = G * (1 + y5) ** 5, 0.0
    e = e_col
    g31 = float(np.prod([1 + e.loc[t] for t in range(Y + 1, Y + 4)]))
    g33 = g31 * float(np.prod([1 + e.loc[t] for t in range(Y + 4, Y + 6)]))
    fund31, fund33 = fund0 * g31, fund0 * g33
    m = min(fund33, fund31)
    bottom, top = F, F + fund31 / 2
    gift = F + m / 2
    kept = fund33 - m / 2
    T33 = F + fund33
    I = float(np.prod([1 + ann.loc[t, "cpi_infl"] for t in range(Y, Y + 6)]))
    fund31v, fund33v = fund0v * g31, fund0v * g33
    gift_v = Fv + min(fund33v, fund31v) / 2
    row.update(short_S=S, floor_face_F=F, fund0=fund0, fund31=fund31, fund33=fund33, bottom=bottom, top=top, gift=gift,
               kept=kept, T33=T33, top_reached=bool(fund33 >= fund31), deflator_I=I, real_gift=gift / I, real_T33=T33 / I,
               ips_variant_F=Fv, ips_variant_fund0=fund0v, ips_variant_gift=gift_v, growth_31=g31, growth_33=g33)
    return row


def part_b(soy, ann):
    today = {"C": float(N("laura.ladder.cost_2027_strips")), "L": float(N("laura.ladder.headroom_2027_strips")),
             "r1": float(N("market.par_curve")["1 Yr"]) / 100.0, "y5": float(N("market.par_curve")["5 Yr"]) / 100.0}
    checks = {"today_G": today["L"] * (1 + today["r1"]) + DEPOSIT_2028}
    checks["today_Cf"] = FLOOR_FACE / (1 + today["y5"]) ** 5
    checks["today_fund0"] = checks["today_G"] - checks["today_Cf"]
    checks["target_fund0"] = float(N("laura.stock_fund_2028_usd.strips"))
    checks["target_Cf"] = float(N("laura.floor_cost_2028"))
    assert abs(checks["today_fund0"] - checks["target_fund0"]) <= 1.0, checks
    assert abs(checks["today_Cf"] - checks["target_Cf"]) <= 1.0, checks

    years = list(range(1872, 2021))
    series_cols = {"world_eq": ann["world_eq"], "us_eq": ann["us_eq"]}
    rescaled = {}
    for s, col in series_cols.items():
        lr = np.log1p(col.loc[1872:2025])
        rescaled[s] = np.exp(np.log1p(col) - lr.mean() + np.log(1.07)) - 1
        checks[f"rescaled_{s}_meanlog_1872_2025"] = float(np.log1p(rescaled[s].loc[1872:2025]).mean())
        checks[f"raw_{s}_meanlog_1872_2025"] = float(lr.mean())
    rows = []
    for view in ("hist", "today_yields", "today_yields_rescaled"):
        for s in ("world_eq", "us_eq"):
            e_col = rescaled[s] if view == "today_yields_rescaled" else series_cols[s]
            for Y in years:
                rows.append(window(Y, view, s, soy, ann, e_col, today))
    bt = pd.DataFrame(rows)
    bt.to_csv(os.path.join(OUT, "backtest_by_start_year.csv"), index=False, float_format="%.4f")

    def q(s, p):
        return float(np.percentile(s, p))

    summ = []
    for (view, s), g in bt.groupby(["view", "fund_series"], sort=False):
        d = {"view": view, "fund_series": s, "n_windows": len(g)}
        for col in ("gift", "T33", "real_gift", "real_T33"):
            iw = g[col].idxmin()
            d[f"{col}_worst"] = g[col].min(); d[f"{col}_worst_Y"] = int(g.loc[iw, "Y"])
            d[f"{col}_p10"] = q(g[col], 10); d[f"{col}_median"] = q(g[col], 50); d[f"{col}_p90"] = q(g[col], 90)
            d[f"{col}_best"] = g[col].max(); d[f"{col}_best_Y"] = int(g.loc[g[col].idxmax(), "Y"])
        d["share_top_reached"] = float(g["top_reached"].mean())
        d["n_short_S_gt_0"] = int((g["short_S"] > 0).sum()); d["largest_S"] = float(g["short_S"].max())
        d["n_topup_T_gt_0"] = int((g["topup_T"] > 1e-9).sum()); d["largest_T"] = float(g["topup_T"].max())
        d["ips_variant_gift_worst"] = float(g["ips_variant_gift"].min())
        d["ips_variant_gift_worst_Y"] = int(g.loc[g["ips_variant_gift"].idxmin(), "Y"])
        d["ladder_cost_C_median"] = q(g["ladder_cost_C"], 50); d["ladder_cost_C_max"] = float(g["ladder_cost_C"].max())
        d["ladder_cost_C_max_Y"] = int(g.loc[g["ladder_cost_C"].idxmax(), "Y"])
        d["n_C_gt_300k"] = int((g["ladder_cost_C"] > DEPOSIT_2027).sum())
        d["fund0_median"] = q(g["fund0"], 50); d["n_fund0_zero"] = int((g["fund0"] <= 0).sum())
        summ.append(d)
    summary = pd.DataFrame(summ)
    summary.to_csv(os.path.join(OUT, "backtest_summary.csv"), index=False, float_format="%.2f")

    hw = bt[(bt["view"] == "hist") & (bt["fund_series"] == "world_eq")]
    eras = [(1872, 1913), (1914, 1945), (1946, 1981), (1982, 2020)]
    era_rows = []
    for a, b in eras:
        g = hw[(hw["Y"] >= a) & (hw["Y"] <= b)]
        era_rows.append({"era": f"{a}-{b}", "n": len(g), "median_ladder_cost": q(g["ladder_cost_C"], 50),
                         "median_gift": q(g["gift"], 50), "worst_gift": float(g["gift"].min()),
                         "worst_gift_Y": int(g.loc[g["gift"].idxmin(), "Y"]), "median_T33": q(g["T33"], 50),
                         "share_top_reached": float(g["top_reached"].mean()), "n_topup": int((g["topup_T"] > 1e-9).sum())})
    era = pd.DataFrame(era_rows)
    era.to_csv(os.path.join(OUT, "era_table.csv"), index=False, float_format="%.2f")
    return bt, summary, era, checks


def fig_backtest(bt):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    hw = bt[(bt["view"] == "hist") & (bt["fund_series"] == "world_eq")].sort_values("Y")
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.plot(hw["Y"], hw["ladder_cost_C"] / 1000, lw=1.3, color="tab:blue")
    ax.axhline(300, color="tab:red", ls=":", lw=1, label="$300,000 (the 2027 deposit)")
    ax.axhline(450, color="tab:gray", ls="--", lw=1, label="$450,000")
    ax.set_xlabel("Start year Y (plays 2027)"); ax.set_ylabel("Ladder cost on the deposit day ($ thousands)")
    ax.set_title("M5 (blind): cost of the ten payments on 1 Jan of each start year, 1872-2020")
    ax.legend(); ax.grid(alpha=0.3); fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m5_ladder_cost_by_start_year.png"), dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(hw["Y"], hw["floor_face_F"] / 1000, color="tab:green", width=0.8, label="floor F (bottom of the 2031 range)")
    ax.bar(hw["Y"], (hw["gift"] - hw["floor_face_F"]) / 1000, bottom=hw["floor_face_F"] / 1000, color="tab:olive", width=0.8,
           label="gift above the floor")
    ax.plot(hw["Y"], hw["T33"] / 1000, color="tab:blue", lw=1.2, label="all money on 1 Jan 2033 (T33)")
    tu = hw[hw["topup_T"] > 1e-9]
    ax.scatter(tu["Y"], np.full(len(tu), 5.0), marker="^", color="tab:red", s=28, label="2028 top-up needed", zorder=5)
    ax.set_xlabel("Start year Y (plays 2027)"); ax.set_ylabel("$ thousands")
    ax.set_title("M5 (blind): 2033 gift and total by start year, history's yields and world-stock returns")
    ax.legend(fontsize=9, loc="upper left"); ax.grid(alpha=0.3); fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m5_gift_by_start_year.png"), dpi=150); plt.close(fig)


# ---------------------------------------------------------------------------------------------------------------
def main():
    h1, h2, h3 = load_h1(), load_h2(), load_h3_monthly_flat()
    soy, ann = load_soy(), load_annual()
    ser, monthly, by_year, v0_D, h = part_a(h1, h2, h3)
    h = part_a4(h1, h2, monthly, v0_D, h)
    fig_cost(monthly, v0_D, h)
    bt, summary, era, checks = part_b(soy, ann)
    fig_backtest(bt)

    targets = {
        "V0_D": float(N("laura.ladder.cost_today_strips")),
        "cost_2020_median": float(N("history.cost_2020_median")),
        "cost_2020_max": float(N("history.cost_max")["usd"]),
        "cost_2020_max_date": str(N("history.cost_max")["date"]),
        "cheapest_since_spot": str(N("history.cheapest_since")["spot"]),
        "cost_2020_min": float(N("history.cost_2020_range")[0]),
        "share_days_le_300k_since_2000_spot": float(N("history.share_days_le_300k")["since_2000_spot"]),
        "share_days_le_300k_since_1990_spot": float(N("history.share_days_le_300k")["since_1990_spot"]),
        "days_priced_since_2000": int(N("history.days_priced_since_2000")),
    }
    repro = {}
    for k, tv in targets.items():
        mv = h[k]
        ok = (mv == tv) if isinstance(tv, str) else (abs(float(mv) - float(tv)) <= (1.0 if abs(tv) > 10 else 0.0006))
        repro[k] = {"blind": mv, "numbers_yaml": tv, "agree": bool(ok)}

    res = {"model": "M5 blind rebuild", "spec": "rab/models/M5_SPEC.md", "curve_date": str(CURVE_DATE),
           "part_a_headlines": h, "reproduction_vs_numbers_yaml": repro, "part_b_checks": checks,
           "part_b_summary": summary.to_dict(orient="records"), "era_table": era.to_dict(orient="records"),
           "n_series_points": {"daily_1990_2026": int(len(h1)), "daily_1962_1989": int(len(h2)), "monthly_1871_1961": int(len(h3)),
                               "total": int(len(ser)), "dropped_blank_h1_rows": getattr(load_h1, "dropped", [])}}
    with open(os.path.join(OUT, "M5_results.json"), "w") as f:
        json.dump(res, f, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))

    # plain-text report
    L = []
    L.append("M5 blind rebuild: cost of certainty and century backtest (MODEL; 28 Sep 2026 curve for 'today')")
    L.append("=" * 100)
    L.append("Part A. Reproduction of M1 G on the daily 1990-2026 curves (must agree with numbers.yaml):")
    for k, v in repro.items():
        L.append(f"  {k:40s} blind={v['blind']!s:>14}  numbers.yaml={v['numbers_yaml']!s:>14}  {'OK' if v['agree'] else 'DIFF'}")
    L.append("")
    L.append("Part A. Extended series 1871-2026:")
    for k in ("lowest_since_1871", "highest_since_1871", "lowest_since_1962", "highest_since_1962"):
        L.append(f"  {k:28s} ${h[k]['usd']:>12,.2f}  {h[k]['date']}  ({h[k]['basis']})")
    for k in ("n_months_since_1871", "share_months_le_V0D_since_1871", "share_months_le_300k_since_1871",
              "share_months_le_V0D_since_1962", "share_months_le_300k_since_1962",
              "share_years_median_below_V0D_1871_2026", "n_years_1871_2026",
              "share_months_le_V0D_since_1871_adj_median", "share_months_le_V0D_since_1871_adj_p95",
              "share_months_le_300k_since_1871_adj_median", "share_months_le_300k_since_1871_adj_p95"):
        L.append(f"  {k:48s} {h[k]}")
    L.append(f"  years whose median cost was below today's: {h['years_median_below_V0D']}")
    L.append(f"  A4(a) flat/full - 1, 1962-2026 monthly: {h['flat_vs_full_1962_2026']}")
    L.append(f"  A4(b) FRED vs Treasury file, first day of month 1990-2026: {h['fred_vs_treasury_1990_2026']}")
    L.append("")
    L.append("Part B. Backtest checks (today_yields view): " + ", ".join(f"{k}={v:,.2f}" for k, v in checks.items() if isinstance(v, float)))
    L.append("")
    L.append("Part B. Summary per view and fund series (149 windows, Y = 1872..2020):")
    cols = ["view", "fund_series", "gift_worst", "gift_worst_Y", "gift_p10", "gift_median", "gift_p90", "gift_best",
            "T33_worst", "T33_p10", "T33_median", "T33_p90", "real_gift_worst", "real_gift_median", "real_T33_worst",
            "real_T33_median", "share_top_reached", "n_short_S_gt_0", "largest_S", "n_topup_T_gt_0", "largest_T",
            "ips_variant_gift_worst", "n_C_gt_300k", "ladder_cost_C_median", "ladder_cost_C_max", "ladder_cost_C_max_Y"]
    disp = summary[cols].copy()
    disp["share_top_reached"] = disp["share_top_reached"].map(lambda v: f"{100 * v:.1f}%")
    with pd.option_context("display.width", 250, "display.max_columns", 50, "display.float_format", "{:,.0f}".format):
        L.append(disp.to_string(index=False))
    L.append("")
    L.append("Era table (hist view, world_eq):")
    era_d = era.copy()
    era_d["share_top_reached"] = era_d["share_top_reached"].map(lambda v: f"{100 * v:.1f}%")
    with pd.option_context("display.width", 250, "display.float_format", "{:,.0f}".format):
        L.append(era_d.to_string(index=False))
    L.append("")
    L.append("Conventions: scale-free dollars; no fees; STRIPS-like zero rungs; pre-1962 curves flat at the long rate; annual steps.")
    open(os.path.join(OUT, "M5_report.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
