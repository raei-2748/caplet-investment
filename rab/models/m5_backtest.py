"""M5: century backtest of Root-and-Branch and the cost-of-certainty history. Spec: rab/models/M5_SPEC.md.

AI-generated research code (Claude Code) for Team Caplet, WS3, 2026-09-30. Every output is MODEL (history replayed
through the adopted rules), not a forecast. No network. Deterministic (no random numbers).

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m5_backtest.py
Writes rab/results/M5/*.csv, *.png and M5_results.json.
"""
import json
import os
import statistics as st
from datetime import date, timedelta

import numpy as np
import pandas as pd

import hist_lib as H

OUT = os.path.join(H.RES, "M5")
LOG = []


def say(s=""):
    LOG.append(s)
    print(s)


TAU_REF = np.array([H.yf(H.D_REF, p) for p in H.NOV15])                     # A2: same time to maturity as on D
TAU_27 = np.array([H.yf(H.A27, p) for p in H.NOV15])                        # B1
TAU_28 = np.array([H.yf(H.A28, p) for p in H.NOV15])                        # B3
TAU_33 = np.array([H.yf(H.A33, p) for p in H.NOV15])                        # rivals (M6): reserve bought in 2033


# ================================================================================================ Part A
def part_a():
    say("[A] Cost of certainty: the ten payments on every curve 1871-2026 (Nov-15 basis, same time to maturity as on "
        "28 Sep 2026)")
    rows = []
    for d, par in H.load_par_files():
        if d > H.D_REF:
            continue
        try:
            cv = H.Curve(par)
        except ValueError:
            continue
        rows.append((d, H.ladder_value(cv, TAU_REF), "treasury_par", cv.par(10)))
    n_par = len(rows)
    for d, par in H.load_fred_daily():
        cv = H.Curve(par)
        rows.append((d, H.ladder_value(cv, TAU_REF), "fred_cmt", cv.par(10)))
    sh = H.load_shiller()
    for r in sh[(sh.year >= 1871) & (sh.year <= 1961)].itertuples():
        cv = H.Curve({"10 Yr": r.GS10})
        rows.append((date(int(r.year), int(r.month), 1), H.ladder_value(cv, TAU_REF), "flat_shiller_gs10", r.GS10 / 100))
    s = pd.DataFrame(rows, columns=["date", "V0", "basis", "y10"]).sort_values("date").reset_index(drop=True)
    s["date"] = pd.to_datetime(s.date)
    s.to_csv(os.path.join(OUT, "cost_of_certainty_series.csv"), index=False, float_format="%.2f")

    today = float(s[s.date == pd.Timestamp(H.D_REF)].V0.iloc[0])
    par = s[s.basis == "treasury_par"]
    y20 = par[par.date.dt.year == 2020]
    cheaper = par[(par.V0 <= today) & (par.date < pd.Timestamp(H.D_REF))]
    res = {"today_V0": today, "par_days": int(n_par),
           "m1g_repro": {"y2020_median": float(st.median(y20.V0)), "y2020_max": float(y20.V0.max()),
                         "y2020_max_date": y20.loc[y20.V0.idxmax(), "date"].date().isoformat(),
                         "last_date_at_or_below_today": cheaper.date.max().date().isoformat()}}
    n = H.numbers()
    chk = [("today", today, n["laura.ladder.cost_today_strips"]["value"]),
           ("2020 median", res["m1g_repro"]["y2020_median"], n["history.cost_2020_median"]["value"]),
           ("2020 max", res["m1g_repro"]["y2020_max"], n["history.cost_max"]["value"]["usd"])]
    for lab, a, b in chk:
        say(f"    reproduce M1 G {lab:12s}: ${a:,.2f} vs numbers.yaml ${b:,.2f} -> {'OK' if abs(a - b) < 1 else 'MISMATCH'}")
    say(f"    reproduce M1 G max date {res['m1g_repro']['y2020_max_date']} (numbers.yaml "
        f"{n['history.cost_max']['value']['date']}); cheapest since {res['m1g_repro']['last_date_at_or_below_today']}"
        f" (numbers.yaml {n['history.cheapest_since']['value']['spot']})")

    # monthly observations: first curve date of each month
    s["ym"] = s.date.dt.to_period("M")
    m = s.groupby("ym").first().reset_index()
    by_year = s.groupby(s.date.dt.year).agg(V0_min=("V0", "min"), V0_median=("V0", "median"), V0_max=("V0", "max"),
                                            basis=("basis", "first"), y10_median=("y10", "median"))
    by_year.index.name = "year"
    by_year.to_csv(os.path.join(OUT, "cost_of_certainty_by_year.csv"), float_format="%.0f")
    ext = {}
    for lab, sub in (("since_1871", m), ("since_1962", m[m.date.dt.year >= 1962])):
        lo, hi = sub.loc[sub.V0.idxmin()], sub.loc[sub.V0.idxmax()]
        ext[lab] = {"months": int(len(sub)), "min": float(lo.V0), "min_date": lo.date.date().isoformat(),
                    "max": float(hi.V0), "max_date": hi.date.date().isoformat(),
                    "share_months_le_today": float((sub.V0 <= today).mean()),
                    "share_months_le_300k": float((sub.V0 <= 300_000).mean())}
    # daily extremes since 1962 (all days, not only month starts)
    d62 = s[s.date.dt.year >= 1962]
    ext["since_1962_daily"] = {"min": float(d62.V0.min()), "min_date": d62.loc[d62.V0.idxmin(), "date"].date().isoformat(),
                               "max": float(d62.V0.max()), "max_date": d62.loc[d62.V0.idxmax(), "date"].date().isoformat(),
                               "days": int(len(d62))}
    ext["share_years_median_below_today"] = float((by_year.V0_median < today).mean())
    ext["years"] = int(len(by_year))
    res["extended"] = ext
    for lab in ("since_1871", "since_1962"):
        e = ext[lab]
        say(f"    {lab}: {e['months']} month-start curves; lowest ${e['min']:,.0f} ({e['min_date']}), highest "
            f"${e['max']:,.0f} ({e['max_date']}); months at or below today's ${today:,.0f}: "
            f"{e['share_months_le_today']:.1%}; at or below $300,000: {e['share_months_le_300k']:.1%}")
    e = ext["since_1962_daily"]
    say(f"    daily since 1962: lowest ${e['min']:,.0f} on {e['min_date']}; highest ${e['max']:,.0f} on {e['max_date']}")
    say(f"    years (1871-2026) whose median cost is below today's: {ext['share_years_median_below_today']:.1%}")

    # A4 (a) flat vs full, first curve date of each month 1962-2026
    full = {}
    for d, par in H.load_par_files():
        if d <= H.D_REF:
            full.setdefault((d.year, d.month), (d, par))
    for d, par in H.load_fred_daily():
        full.setdefault((d.year, d.month), (d, par))
    rat = []
    for (yy, mm), (d, par) in sorted(full.items()):
        try:
            cv = H.Curve(par)
        except ValueError:
            continue
        if par.get("10 Yr") in (None, "", "N/A") or par.get("10 Yr") != par.get("10 Yr"):
            continue
        flat = H.Curve({"10 Yr": par["10 Yr"]})
        rat.append((yy, H.ladder_value(flat, TAU_REF) / H.ladder_value(cv, TAU_REF) - 1))
    r = pd.DataFrame(rat, columns=["year", "err"])
    r["decade"] = (r.year // 10) * 10
    tab = r.groupby("decade").err.describe(percentiles=[.05, .5, .95])[["count", "5%", "50%", "95%"]]
    tab.to_csv(os.path.join(OUT, "check_flat_vs_full_curve.csv"), float_format="%.4f")
    res["check_flat_vs_full"] = {"median": float(r.err.median()), "p5": float(r.err.quantile(.05)),
                                 "p95": float(r.err.quantile(.95)), "by_decade": tab.round(4).reset_index().to_dict("records")}
    say(f"    check A4(a) flat-at-10y vs full curve, 1962-2026 month starts: median {r.err.median():+.1%}, "
        f"5th-95th pct {r.err.quantile(.05):+.1%} .. {r.err.quantile(.95):+.1%}")
    for row in tab.itertuples():
        say(f"        {row.Index}s: median {row._3:+.1%} (5th {row._2:+.1%}, 95th {row._4:+.1%}), n={int(row.count)}")

    # A4 (b) FRED vs Treasury file, 1990-2026 month starts
    fr = {}
    for sname, col in {"DGS1MO": "1 Mo", "DGS3MO": "3 Mo", "DGS6MO": "6 Mo", "DGS1": "1 Yr", "DGS2": "2 Yr",
                       "DGS3": "3 Yr", "DGS5": "5 Yr", "DGS7": "7 Yr", "DGS10": "10 Yr", "DGS20": "20 Yr",
                       "DGS30": "30 Yr"}.items():
        f = pd.read_csv(os.path.join(H.DATA, "fred", f"{sname}.csv"))
        f.columns = ["date", "v"]
        f["v"] = pd.to_numeric(f.v, errors="coerce")
        fr[col] = dict(zip(f.date, f.v))
    diffs = []
    for (yy, mm), (d, par) in sorted(full.items()):
        if yy < 1990:
            continue
        fp = {c: fr[c].get(d.isoformat()) for c in fr}
        if fp["10 Yr"] is None or fp["10 Yr"] != fp["10 Yr"]:
            continue
        diffs.append(H.ladder_value(H.Curve(fp), TAU_REF) - H.ladder_value(H.Curve(par), TAU_REF))
    res["check_fred_vs_par"] = {"n": len(diffs), "max_abs_usd": float(np.max(np.abs(diffs))),
                                "median_usd": float(np.median(diffs))}
    say(f"    check A4(b) FRED vs Treasury par file, {len(diffs)} month starts 1990-2026: largest difference "
        f"${np.max(np.abs(diffs)):,.0f} (median ${np.median(diffs):,.0f}; FRED lacks the 2-month tenor)")
    # sensitivity: remove the flat-curve bias from pre-1962 months (median and 95th-percentile error of A4(a))
    sens = {}
    for lab, err in (("median_error", float(r.err.median())), ("p95_error", float(r.err.quantile(.95)))):
        adj = np.where(m.date.dt.year < 1962, m.V0 / (1 + err), m.V0)
        sens[lab] = {"error": err, "share_months_le_today_since_1871": float((adj <= today).mean())}
    res["extended"]["flat_bias_sensitivity"] = sens
    say(f"    sensitivity: correcting pre-1962 months for the flat-curve bias ({sens['median_error']['error']:+.1%} / "
        f"{sens['p95_error']['error']:+.1%}) gives {sens['median_error']['share_months_le_today_since_1871']:.1%} / "
        f"{sens['p95_error']['share_months_le_today_since_1871']:.1%} of months since 1871 at or below today")
    fig_cost(m, today, d62)
    return res, s


def fig_cost(m, today, daily):
    plt = H.plot_style()
    fig, ax = plt.subplots(figsize=(9, 4.4))
    pre = m[m.date.dt.year < 1962]
    post = m[m.date.dt.year >= 1962]
    ax.plot(pre.date, pre.V0 / 1000, color=H.OI["blue"], lw=1.1, ls=(0, (3, 1.5)),
            label="1871-1961: flat curve at the 10-year rate (approximation)")
    ax.plot(post.date, post.V0 / 1000, color=H.OI["blue"], lw=1.3, label="1962-2026: full Treasury curve")
    ax.axhline(300, color=H.OI["vermillion"], lw=1.2, ls="--")
    ax.text(pd.Timestamp("1960-06-01"), 440, "Laura's first deposit: $300,000 (dashed line)", color=H.OI["vermillion"],
            fontsize=8.5)
    ax.axhline(today / 1000, color=H.OI["green"], lw=1.0, ls=":")
    ax.annotate(f"28 Sep 2026: ${today / 1000:,.0f}k\n(cheapest since mid-2002)", xy=(pd.Timestamp("2026-09-28"), today / 1000),
                xytext=(pd.Timestamp("1990-01-01"), 150), fontsize=8.5, color=H.OI["green"],
                arrowprops=dict(arrowstyle="->", color=H.OI["green"], lw=0.8))
    pk = daily.loc[daily.V0.idxmax()]
    ax.annotate(f"{pk.date:%-d %b %Y}: ${pk.V0 / 1000:,.0f}k (highest)", xy=(pk.date, pk.V0 / 1000),
                xytext=(pd.Timestamp("1994-01-01"), 520), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", lw=0.8, color="#444444"))
    lo = daily.loc[daily.V0.idxmin()]
    ax.annotate(f"{lo.date:%-d %b %Y}: ${lo.V0 / 1000:,.0f}k (lowest)", xy=(lo.date, lo.V0 / 1000),
                xytext=(pd.Timestamp("1955-01-01"), 90), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", lw=0.8, color="#444444"))
    ax.set_ylabel("Cost today of the ten $50,000 payments ($ thousands)")
    ax.set_title("The price of certainty: what Laura's ten payments would have cost on each date (MODEL)")
    ax.set_ylim(0, max(560, m.V0.max() / 1000 * 1.05))
    ax.legend(loc="upper left", fontsize=8)
    fig.text(0.01, 0.005, "Month-start values; same payment timing as on 28 Sep 2026 (STRIPS 15 Nov 2032-41), D1 curve "
             "method. Sources: Treasury par curves 1990-, FRED DGS 1962-89, Shiller GS10 1871-1961.",
             fontsize=6.5, color="#555555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_cost_of_certainty.png"))
    plt.close(fig)


# ================================================================================================ Part B
def rec_window(C_rungs, L_rate, rungs28, y5, rets, cpi=None, ips_variant=False):
    """One start year. C_rungs: the ten rung costs on the 2027-analog curve; rungs28: rung costs on the 2028-analog
    curve (for the top-up); rets: five calendar-year fund returns (2028..2032 analogs); cpi: six inflation rates."""
    M = H.DEP1
    f = np.zeros(10)
    for k in range(9, -1, -1):                   # longest first
        f[k] = min(1.0, M / C_rungs[k]) if M > 0 else 0.0
        M -= f[k] * C_rungs[k]
    L = max(M, 0.0) if f.min() >= 1 - 1e-12 else 0.0
    T = float(((1 - f) * rungs28).sum())
    G = L * (1 + L_rate) + H.DEP2 - T
    out = dict(C=float(C_rungs.sum()), L=L, T=T, G=G, S=max(0.0, -G))
    if G < 0:
        out.update(F=0.0, fund0=0.0, fund31=0.0, fund33=0.0, bottom=0.0, top=0.0, gift=0.0, kept=0.0, T33=0.0,
                   top_reached=False)
    else:
        face = H.FLOOR_FACE - T if ips_variant and T > 0 else H.FLOOR_FACE
        Cf = face / (1 + y5) ** 5
        if G >= Cf:
            F, fund0 = face, G - Cf
        else:
            F, fund0 = G * (1 + y5) ** 5, 0.0
        g = np.cumprod(1 + np.asarray(rets))
        fund31, fund33 = fund0 * g[2], fund0 * g[4]
        m = min(fund33, fund31)
        out.update(F=F, fund0=fund0, fund31=fund31, fund33=fund33, bottom=F, top=F + fund31 / 2, gift=F + m / 2,
                   kept=fund33 - m / 2, T33=F + fund33, top_reached=bool(fund33 >= fund31))
    if cpi is not None:
        I = float(np.prod(1 + np.asarray(cpi)))
        out.update(deflator=I, real_gift=out["gift"] / I, real_T33=out["T33"] / I)
    return out


def rescale(x, target):
    lx = np.log1p(x)
    return np.expm1(lx - lx.mean() + np.log1p(target))


def part_b():
    say("\n[B] Start-year backtest of the adopted plan (Y plays 2027 .. Y+6 plays 2033)")
    soy, A = H.load_soy(), H.load_annual()
    n = H.numbers()
    Y0, Y1 = 1872, 2020
    today_par = n["market.par_curve"]["value"]
    c27 = n["laura.ladder.cost_2027_strips"]["value"]
    tc = H.today_curve()
    # today's rung costs on 1 Jan 2027 (forward), they sum to the Gate A headline
    t_rungs = H.PAY * tc.df(np.array([H.yf(H.D_REF, p) for p in H.NOV15])) / float(tc.df(H.yf(H.D_REF, H.A27)))
    assert abs(t_rungs.sum() - c27) < 0.01
    y1_today, y5_today = today_par["1 Yr"] / 100, today_par["5 Yr"] / 100
    series = {"world_eq": A.world_eq, "us_eq": A.us_eq}
    resc = {k: pd.Series(rescale(v.loc[1872:2025].values, 0.07), index=range(1872, 2026)) for k, v in series.items()}
    rows = []
    for Y in range(Y0, Y1 + 1):
        cY, cY1 = H.soy_curve(soy, Y), H.soy_curve(soy, Y + 1)
        rungs27 = H.PAY * cY.df(TAU_27)
        rungs28 = H.PAY * cY1.df(TAU_28)
        r1 = soy.loc[Y, "1 Yr"] / 100 if soy.loc[Y, "1 Yr"] == soy.loc[Y, "1 Yr"] else A.loc[Y, "us_bill"]
        y5 = cY1.par(5)
        cpi = A.loc[Y:Y + 5, "cpi_infl"].values
        for fs, ser in series.items():
            rets = ser.loc[Y + 1:Y + 5].values
            for view in ("hist", "today_yields", "today_yields_rescaled"):
                if view == "hist":
                    o = rec_window(rungs27, r1, rungs28, y5, rets, cpi)
                    oi = rec_window(rungs27, r1, rungs28, y5, rets, cpi, ips_variant=True)
                else:
                    rr = rets if view == "today_yields" else resc[fs].loc[Y + 1:Y + 5].values
                    o = rec_window(t_rungs, y1_today, t_rungs, y5_today, rr, cpi)
                    oi = o
                o.update(view=view, fund=fs, Y=Y, basis_Y=soy.loc[Y, "basis"], basis_Y1=soy.loc[Y + 1, "basis"],
                         ips_gift=oi["gift"], ips_F=oi["F"])
                rows.append(o)
    df = pd.DataFrame(rows)
    cols = ["view", "fund", "Y", "basis_Y", "basis_Y1", "C", "L", "T", "G", "S", "F", "fund0", "fund31", "fund33",
            "bottom", "top", "gift", "kept", "T33", "top_reached", "deflator", "real_gift", "real_T33", "ips_F",
            "ips_gift"]
    df[cols].to_csv(os.path.join(OUT, "backtest_by_start_year.csv"), index=False, float_format="%.2f")

    # checks on the today_yields view (numbers.yaml)
    t = df[(df.view == "today_yields")].iloc[0]
    say(f"    check today_yields: fund0 ${t.fund0:,.0f} vs numbers.yaml laura.stock_fund_2028_usd.strips "
        f"${n['laura.stock_fund_2028_usd.strips']['value']:,}; floor cost ${t.G - t.fund0:,.0f} vs laura.floor_cost_2028 "
        f"${n['laura.floor_cost_2028']['value']:,}")
    summ = []
    for (view, fs), g in df.groupby(["view", "fund"], sort=False):
        rec = {"view": view, "fund": fs, "windows": len(g)}
        for q in ("gift", "T33", "real_gift", "real_T33"):
            v = g[q]
            rec.update({f"{q}_worst": v.min(), f"{q}_worst_Y": int(g.loc[v.idxmin(), "Y"]), f"{q}_p10": v.quantile(.1),
                        f"{q}_median": v.median(), f"{q}_p90": v.quantile(.9), f"{q}_best": v.max()})
        rec.update(share_top_reached=g.top_reached.mean(), n_unfunded=int((g.S > 0).sum()), max_S=g.S.max(),
                   n_topup=int((g["T"] > 0).sum()), max_T=g["T"].max(), ips_gift_worst=g.ips_gift.min(),
                   bottom_median=g.bottom.median(), fund0_median=g.fund0.median(), C_median=g.C.median(),
                   n_bottom_lt_150k=int((g.bottom < 150_000 - 0.5).sum()))
        summ.append(rec)
    S = pd.DataFrame(summ)
    S.to_csv(os.path.join(OUT, "backtest_summary.csv"), index=False, float_format="%.2f")
    for r in S.itertuples():
        say(f"    {r.view:22s} {r.fund:8s} ({r.windows} windows): gift worst {H.kusd(r.gift_worst)} ({r.gift_worst_Y}), "
            f"p10 {H.kusd(r.gift_p10)}, median {H.kusd(r.gift_median)}, best {H.kusd(r.gift_best)} | total worst "
            f"{H.kusd(r.T33_worst)} ({r.T33_worst_Y}), median {H.kusd(r.T33_median)} | real gift worst "
            f"{H.kusd(r.real_gift_worst)} ({r.real_gift_worst_Y}), median {H.kusd(r.real_gift_median)} | top reached "
            f"{r.share_top_reached:.0%} | top-up in {r.n_topup} (max {H.kusd(r.max_T)}), unfunded in {r.n_unfunded} "
            f"(max {H.kusd(r.max_S)}); floor below $150k in {r.n_bottom_lt_150k}; IPS-wording worst gift {H.kusd(r.ips_gift_worst)}")
    # era table
    h = df[(df.view == "hist") & (df.fund == "world_eq")]
    eras = [(1872, 1913), (1914, 1945), (1946, 1981), (1982, 2020)]
    et = []
    for a, b in eras:
        g = h[(h.Y >= a) & (h.Y <= b)]
        et.append(dict(era=f"{a}-{b}", windows=len(g), ladder_cost_median=g.C.median(), ladder_cost_max=g.C.max(),
                       topup_windows=int((g["T"] > 0).sum()), fund0_median=g.fund0.median(), gift_median=g.gift.median(),
                       gift_worst=g.gift.min(), real_gift_median=g.real_gift.median(),
                       top_reached=g.top_reached.mean()))
    ET = pd.DataFrame(et)
    ET = ET.round({c: 0 for c in ET.columns if c not in ("era", "windows", "topup_windows", "top_reached")}).round(
        {"top_reached": 3})
    ET.to_csv(os.path.join(OUT, "backtest_eras.csv"), index=False)
    say("    eras (hist view, VT-like world fund):")
    for r in ET.itertuples():
        say(f"      {r.era}: ladder cost median {H.kusd(r.ladder_cost_median)} (max {H.kusd(r.ladder_cost_max)}), "
            f"top-ups {r.topup_windows}/{r.windows}; stock fund median {H.kusd(r.fund0_median)}; gift median "
            f"{H.kusd(r.gift_median)}, worst {H.kusd(r.gift_worst)}; real gift median {H.kusd(r.real_gift_median)}; "
            f"top reached {r.top_reached:.0%}")
    worst = h.nsmallest(5, "gift")[["Y", "C", "T", "F", "fund0", "gift", "real_gift"]]
    say("    five lowest gifts (hist, world): " + "; ".join(
        f"{int(r.Y)} gift {H.kusd(r.gift)} (ladder {H.kusd(r.C)}, top-up {H.kusd(r.T)}, floor {H.kusd(r.F)}, fund "
        f"{H.kusd(r.fund0)})" for r in worst.itertuples()))
    # reconciliation with insight_v1 H9 (E6 [5] convention: U.S. S&P, starts 1928-2020, rescaled over 1928-2025)
    t = df[(df.view == "today_yields") & (df.fund == "us_eq") & (df.Y >= 1928)]
    eq = A.us_eq.loc[1928:2025]
    rs = pd.Series(rescale(eq.values, 0.07), index=eq.index)
    f0 = float(t.fund0.iloc[0])
    tot = np.array([150_000 + f0 * np.prod(1 + rs.loc[Y + 1:Y + 5].values) for Y in range(1928, 2021)])
    h9 = {"raw_total_worst": float(t.T33.min()), "raw_total_worst_Y": int(t.loc[t.T33.idxmin(), "Y"]),
          "rescaled_total_worst": float(tot.min()), "rescaled_total_worst_Y": 1928 + int(tot.argmin()),
          "rescaled_total_p10": float(np.percentile(tot, 10)), "rescaled_total_median": float(np.median(tot)),
          "insight_v1_H9": {"raw_worst": 171000, "rescaled_worst": 169000, "p10": 185000, "median": 214000}}
    say(f"    reconcile insight_v1 H9 on the 28 Sep basis (U.S., 1928-2020 starts): raw total worst "
        f"{H.kusd(h9['raw_total_worst'])} ({h9['raw_total_worst_Y']}); rescaled worst {H.kusd(h9['rescaled_total_worst'])} "
        f"({h9['rescaled_total_worst_Y']}), p10 {H.kusd(h9['rescaled_total_p10'])}, median {H.kusd(h9['rescaled_total_median'])} "
        f"(H9: $171k / $169k / $185k / $214k)")
    fig_b(h)
    return df, S, ET, h9


def fig_b(h):
    plt = H.plot_style()
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(h.Y, h.C / 1000, color=H.OI["blue"], lw=1.3, label="ladder cost on the 2027-analog deposit day")
    ax.axhline(300, color=H.OI["vermillion"], ls="--", lw=1.1, label="first deposit $300,000")
    ax.axhline(450, color=H.OI["orange"], ls=":", lw=1.2, label="both deposits $450,000")
    pre = h[h.basis_Y == "flat_shiller_gs10"]
    ax.axvspan(pre.Y.min() - 0.5, pre.Y.max() + 0.5, color="#bbbbbb", alpha=0.18, lw=0)
    ax.text(pre.Y.min() + 1, 60, "flat-curve era (10-year rate only)", fontsize=8, color="#555555")
    ax.set_xlabel("start year Y (plays 2027)")
    ax.set_ylabel("$ thousands")
    ax.set_ylim(0, 500)
    ax.set_title("What the ten payments cost if the plan had started in year Y (MODEL, history's yields)")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m5_ladder_cost_by_start_year.png"))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 4.4))
    ax.bar(h.Y, h.F / 1000, color=H.OI["sky"], width=0.85, label="floor (known in 2028)")
    ax.bar(h.Y, (h.gift - h.F) / 1000, bottom=h.F / 1000, color=H.OI["orange"], width=0.85,
           label="+ half the stock fund (capped at the 2031 top)")
    ax.plot(h.Y, h.T33 / 1000, color=H.OI["black"], lw=1.0, label="all money for the facility and flexibility (2033)")
    tu = h[h["T"] > 0]
    if len(tu):
        ax.scatter(tu.Y, np.full(len(tu), 8), marker="^", color=H.OI["vermillion"], s=14, zorder=3,
                   label="rates so low the 2028 deposit had to finish the ladder")
    ax.axhline(150, color="#555555", lw=0.8, ls="--")
    ax.set_xlabel("start year Y (plays 2027)")
    ax.set_ylabel("$ thousands (nominal)")
    ax.set_title("The 2033 facility gift from every start year, history's yields and returns (MODEL)")
    ax.legend(loc="upper left", fontsize=7.8, ncol=2)
    ax.set_ylim(0, max(h.T33.max() / 1000 * 1.1, 300))
    fig.text(0.01, 0.005, "Stock fund = 62% U.S. + 38% outside (today's VT mix). Floor = Treasury bought in the 2028-analog "
             "year. All ten payments are fully funded in every one of the 149 windows.", fontsize=6.5, color="#555555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_m5_gift_by_start_year.png"))
    plt.close(fig)


def main():
    os.makedirs(OUT, exist_ok=True)
    H.self_test()
    ra, _ = part_a()
    df, S, ET, h9 = part_b()
    res = {"part_a": ra, "part_b_summary": S.to_dict("records"), "eras": ET.to_dict("records"), "h9_reconciliation": h9,
           "seed": "none (deterministic)", "spec": "rab/models/M5_SPEC.md"}
    with open(os.path.join(OUT, "M5_results.json"), "w") as f:
        json.dump(res, f, indent=1, default=float)
    with open(os.path.join(OUT, "M5_report.txt"), "w") as f:
        f.write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
