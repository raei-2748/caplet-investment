"""M7: stress scenarios for Root-and-Branch and the real value of the $50,000 payments. Spec: rab/models/M7_SPEC.md.

AI-generated research code (Claude Code) for Team Caplet, WS3, 2026-09-30. MODEL outputs (historical episodes replayed
through the adopted rules on today's curve), not forecasts. Deterministic. No network.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m7_stress.py
"""
import json
import os
from datetime import date

import numpy as np
import pandas as pd

import hist_lib as H

OUT = os.path.join(H.RES, "M7")
LOG = []


def say(s=""):
    LOG.append(s)
    print(s)


N = H.numbers()
PAR = N["market.par_curve"]["value"]
Y1, Y5 = PAR["1 Yr"] / 100, PAR["5 Yr"] / 100
MI = pd.read_csv(os.path.join(H.HIST, "market_inflation_2026-09.csv")).set_index("series").value
BE = MI["T10YIE"] / 100
EXPINF = MI["EXPINF10YR"] / 100
JPM_INFL = pd.read_csv(os.path.join(H.HIST, "jpm_ltcma_2026_usd.csv")).set_index("asset").loc["U.S. Inflation",
                                                                                            "compound_2026"] / 100
T0 = H.D_REF


def curve(shift_pp):
    return H.Curve(PAR, bp=shift_pp * 100)


def fwd_df(cv, T, d):
    t0 = H.yf(T0, T)
    return float(cv.df(max(H.yf(T0, d), t0)) / cv.df(t0))


def run(sc):
    dpre, dy, e, pi = sc["dpre"], np.asarray(sc["dy"]), np.asarray(sc["e"]), np.asarray(sc["pi"])
    s = np.r_[dpre, dpre + np.cumsum(dy)]                                  # s[t] = shift on 1 Jan 2027+t, t=0..6
    cvs = [curve(x) for x in s]
    A = [date(2027 + t, 1, 1) for t in range(7)]
    rung27 = np.array([H.PAY * fwd_df(cvs[0], A[0], p) for p in H.NOV15])
    rung28 = np.array([H.PAY * fwd_df(cvs[1], A[1], p) for p in H.NOV15])
    C = float(rung27.sum())
    M, f = H.DEP1, np.zeros(10)
    for k in range(9, -1, -1):
        f[k] = min(1.0, M / rung27[k]) if M > 0 else 0.0
        M -= f[k] * rung27[k]
    L = max(M, 0.0) if f.min() >= 1 - 1e-12 else 0.0
    r1 = Y1 + dpre / 100
    T = float(((1 - f) * rung28).sum())
    G = L * (1 + r1) + H.DEP2 - T
    y5 = Y5 + s[1] / 100
    out = dict(id=sc["id"], name=sc["name"], dpre_bp=dpre * 100, C=C, L=L, T=T, G=G, funded=bool(G >= 0), y5=y5)
    if G < 0:
        out.update(F=0.0, fund0=0.0, fund31=0.0, fund33=0.0, gift=0.0, top=0.0, kept=0.0, T33=0.0, shortfall=-G)
    else:
        Cf = H.FLOOR_FACE / (1 + y5) ** 5
        F, fund0 = (H.FLOOR_FACE, G - Cf) if G >= Cf else (G * (1 + y5) ** 5, 0.0)
        g = np.cumprod(1 + e[1:6])
        f31, f33 = fund0 * g[2], fund0 * g[4]
        out.update(F=F, fund0=fund0, fund31=f31, fund33=f33, top=F + f31 / 2, gift=F + min(f33, f31) / 2,
                   kept=f33 - min(f33, f31) / 2, T33=F + f33, shortfall=0.0, top_reached=bool(f33 >= f31))
    defl = float(np.prod(1 + pi[:6]))
    out.update(deflator_2033=defl, real_gift=out["gift"] / defl, real_T33=out["T33"] / defl)
    rv = np.array([H.PAY / np.prod(1 + pi[:5 + k]) for k in range(1, 11)])
    out.update(real_pay_2033=rv[0], real_pay_2042=rv[-1], real_pay_total=rv.sum())
    # context rivals on the same path
    out["R1_T33"] = max(G, 0) * (1 + y5) ** 5
    b = np.array([Y5 + s[t] / 100 - 5 * dy[t] / 100 for t in range(6)])
    res33 = sum(H.PAY * (1.0 if p <= A[6] else fwd_df(cvs[6], A[6], p)) for p in H.NOV15)
    a = H.DEP1
    for t in range(6):
        if t == 1:
            a += H.DEP2
        a *= 1 + 0.6 * e[t] + 0.4 * b[t]
    out["R2_T33"] = a - res33
    a = H.DEP1
    for t in range(6):
        if t == 1:
            a += H.DEP2

        def fl_val(cv, T):
            return sum(H.PAY * (1.0 if p <= T else fwd_df(cv, T, p)) for p in H.NOV15) + 150_000 * fwd_df(cv, T, H.A33)
        fl = fl_val(cvs[t], A[t])
        fl1 = fl_val(cvs[t + 1], A[t + 1])
        E = min(a, 3 * max(a - fl, 0.0))
        a = E * (1 + e[t]) + (a - E) * fl1 / fl
    out["R5_T33"] = a - res33
    return out


def downgrade_events():
    g = pd.read_csv(os.path.join(H.HIST, "raw", "yf_GSPC_daily.csv"), header=[0, 1], index_col=0)
    spx = g["Close"].iloc[:, 0]
    spx.index = pd.to_datetime(spx.index)
    d = pd.read_csv(os.path.join(H.DATA, "fred", "DGS10.csv"))
    d.columns = ["date", "v"]
    d["date"] = pd.to_datetime(d.date)
    d["v"] = pd.to_numeric(d.v, errors="coerce")
    d = d.dropna().set_index("date").v
    rows = []
    for ev, day in (("S&P downgrade (AAA to AA+)", "2011-08-05"), ("Fitch downgrade (AAA to AA+)", "2023-08-01"),
                    ("Moody's downgrade (Aaa to Aa1)", "2025-05-16")):
        t = pd.Timestamp(day)
        i, j = d.index.searchsorted(t), spx.index.searchsorted(t)
        rows.append(dict(event=ev, announced=day, base_date=d.index[i].date().isoformat(), y10_base=d.iloc[i],
                         end_date=d.index[i + 20].date().isoformat(), y10_end=d.iloc[i + 20],
                         dy_bp=round((d.iloc[i + 20] - d.iloc[i]) * 100, 1),
                         spx_change=spx.iloc[j + 20] / spx.iloc[j] - 1,
                         spx_min_change=spx.iloc[j:j + 21].min() / spx.iloc[j] - 1))
    return pd.DataFrame(rows)


def scenarios(dg):
    A = H.load_annual()
    soy = H.load_soy()
    y10 = soy["10 Yr"]
    base_e, base_pi = [0.07] * 6, [BE] * 15
    S = [dict(id="S0", name="Base (JPM 7% stocks, breakeven inflation)", dpre=0.0, dy=[0] * 6, e=base_e, pi=base_pi)]
    for sid, nm, a0, pi0 in (("S1", "1970s stagflation (1973-78)", 1973, 1973), ("S5", "Great Depression (1928-33)", 1928, 1928),
                             ("S7", "Great Inflation (1966-71)", 1966, 1966)):
        dy = [(y10[a0 + t + 1] - y10[a0 + t]) for t in range(6)]
        S.append(dict(id=sid, name=nm, dpre=0.0, dy=dy, e=list(A.loc[a0:a0 + 5, "world_eq"]),
                      pi=list(A.loc[pi0:pi0 + 14, "cpi_infl"])))
    jdy = [(A.loc[1990 + t + 1, "jpn_ltrate"] - A.loc[1990 + t, "jpn_ltrate"]) for t in range(6)]
    jpi = list(A.loc[1990:2004, "jpn_cpi_infl"])
    S.append(dict(id="S2", name="Japan's lost decade (1990-95)", dpre=0.0, dy=jdy, e=list(A.loc[1990:1995, "jpn_eq"]), pi=jpi))
    S.append(dict(id="S2b", name="Japan, and rates fall 1pp before Jan 2027", dpre=-1.0, dy=jdy,
                  e=list(A.loc[1990:1995, "jpn_eq"]), pi=jpi))
    pi22 = list(A.loc[2021:2025, "cpi_infl"]) + [BE] * 10
    for sid, nm, t in (("S3", "2022 happens in 2028", 1), ("S3b", "2022 happens in 2027", 0)):
        dy, e = [0.0] * 6, list(base_e)
        dy[t], e[t] = y10[2023] - y10[2022], A.loc[2022, "world_eq"]
        S.append(dict(id=sid, name=nm, dpre=0.0, dy=dy, e=e, pi=pi22))
    for sid, row in zip(("S4a", "S4b", "S4c"), dg.itertuples()):
        S.append(dict(id=sid, name=f"{row.event.split(' (')[0]} {row.announced[:4]}-style, before the ladder is bought",
                      dpre=row.dy_bp / 100, dy=[0] * 6, e=base_e, pi=base_pi))
    e = list(base_e)
    e[1] = -0.20
    S.append(dict(id="S4d", name="Downgrade + buyers' strike (hypothetical)",
                  dpre=1.0, dy=[0] * 6, e=e, pi=base_pi))
    dy, e = [0.0] * 6, list(base_e)
    dy[1], e[1] = y10[2009] - y10[2008], A.loc[2008, "world_eq"]
    S.append(dict(id="S6", name="2008 happens in 2028", dpre=0.0, dy=dy, e=e, pi=base_pi))
    order = ["S0", "S1", "S7", "S2", "S2b", "S3", "S3b", "S5", "S6", "S4a", "S4b", "S4c", "S4d"]
    return sorted(S, key=lambda x: order.index(x["id"]))


def real_value_section(S):
    A = H.load_annual()
    paths = {"Market breakeven 2.34% (T10YIE, 28 Sep 2026)": [BE] * 15,
             f"Cleveland Fed expected {EXPINF * 100:.2f}% (EXPINF10YR, Sep 2026)": [EXPINF] * 15,
             f"JPM 2026 LTCMA {JPM_INFL * 100:.2f}%": [JPM_INFL] * 15,
             "Fed target 2.00%": [0.02] * 15}
    for sc in S:
        if sc["id"] in ("S1", "S2", "S3", "S5", "S7"):
            nm = "2021-25 inflation, then breakeven (S3)" if sc["id"] == "S3" else sc["name"]
            paths[nm] = sc["pi"]
    rows = []
    for nm, pi in paths.items():
        pi = np.asarray(pi)
        rv = [H.PAY / np.prod(1 + pi[:5 + k]) for k in range(1, 11)]
        rows.append(dict(path=nm, avg_inflation=float(np.prod(1 + pi) ** (1 / 15) - 1),
                         **{f"pay_{2032 + k}": rv[k - 1] for k in range(1, 11)}, total=float(np.sum(rv))))
    P = pd.DataFrame(rows)
    P.to_csv(os.path.join(OUT, "real_value_paths.csv"), index=False, float_format="%.2f")
    hist = []
    for Y in range(1872, 2012):
        pi = A.loc[Y:Y + 14, "cpi_infl"].values
        hist.append([H.PAY / np.prod(1 + pi[:5 + k]) for k in range(1, 11)])
    hist = np.array(hist)
    HD = pd.DataFrame({"payment": [2032 + k for k in range(1, 11)],
                       "p5": np.percentile(hist, 5, axis=0), "p50": np.median(hist, axis=0),
                       "p95": np.percentile(hist, 95, axis=0)})
    tot = hist.sum(axis=1)
    HD.loc[len(HD)] = ["total", np.percentile(tot, 5), np.median(tot), np.percentile(tot, 95)]
    HD.to_csv(os.path.join(OUT, "real_value_history_distribution.csv"), index=False, float_format="%.2f")
    h19 = N["ref.H19.real_value_50k"]["value"]
    rep = {"2033": 50_000 / 1.025 ** 7, "2042": 50_000 / 1.025 ** 16}
    return P, HD, dict(h19_reference=h19, h19_reproduced=rep, h19_match=all(abs(rep[k] - h19[k]) < 1 for k in rep),
                       windows=len(hist))


def thresholds():
    """Parallel fall before 1 Jan 2027 (persisting to Jan 2028) at which (a) the ladder first needs a top-up,
    (b) the stock fund is used up (the 2028 deposit can still buy the $150,000 floor, nothing left for stocks), and
    (c) a payment would be unfunded (G < 0). Solved by bisection to 0.01bp on the S0 path."""
    from scipy.optimize import brentq
    base = dict(id="T", name="t", dy=[0] * 6, e=[0.07] * 6, pi=[BE] * 15)
    f = lambda x, key: run(dict(base, dpre=-x))[key]
    a = brentq(lambda x: f(x, "C") - H.DEP1, 0, 3)
    lo, hi = 0.0, 5.0
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if run(dict(base, dpre=-m))["fund0"] > 1e-6 else (lo, m)
    fund_gone = hi
    lo, hi = 0.0, 8.0
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if run(dict(base, dpre=-m))["G"] >= 0 else (lo, m)
    unfunded = hi
    return dict(topup_starts_bp=a * 100, fund_used_up_bp=fund_gone * 100, payment_unfunded_bp=unfunded * 100,
                note="parallel fall before 1 Jan 2027 that persists to 1 Jan 2028; E6/M1 F floor convention")


def figs(T, P, HD):
    plt = H.plot_style()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    T = T.reset_index(drop=True)
    y = np.arange(len(T))
    ax.barh(y, T.F / 1000, color=H.OI["sky"], height=0.62, label="floor (the promised bottom)")
    ax.barh(y, (T.gift - T.F) / 1000, left=T.F / 1000, color=H.OI["orange"], height=0.62,
            label="+ half the stock fund (capped)")
    ax.plot(T.real_gift / 1000, y, "D", color=H.OI["black"], ms=4.5, label="gift in 2027 dollars (after inflation)")
    for i, r in T.iterrows():
        ax.text(r.gift / 1000 + 3, i, f"${r.gift / 1000:,.0f}k" + ("" if r.funded else "  PAYMENTS SHORT"), va="center",
                fontsize=7.5)
    ax.set_yticks(y)
    ax.set_yticklabels(T.name, fontsize=8)
    ax.invert_yaxis()
    ax.axvline(150, color="#555555", ls="--", lw=0.8)
    ax.set_xlabel("2033 facility gift ($ thousands, nominal unless marked)")
    fig.suptitle("Stress tests: all ten $50,000 payments are paid in every scenario (MODEL)", fontsize=10.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, -0.11), ncol=3, fontsize=7.8)
    ax.set_xlim(0, max(T.gift.max() / 1000 * 1.25, 230))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m7_stress.png"))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 4.4))
    yrs = np.arange(2033, 2043)
    h = HD[HD.payment != "total"]
    ax.fill_between(yrs, h.p5.astype(float) / 1000, h.p95.astype(float) / 1000, color=H.OI["grey"], alpha=0.25,
                    label="U.S. history 1872-2025: 5th-95th percentile of 15-year inflation paths")
    styles = {"Market": (H.OI["blue"], "-"), "Cleveland": (H.OI["sky"], ":"), "JPM": (H.OI["green"], "--"),
              "Fed": (H.OI["black"], "-"), "1970s": (H.OI["vermillion"], "-"), "Great Inflation": (H.OI["purple"], "--"),
              "Japan": (H.OI["orange"], "-"), "2021-25": ("#8c6d00", "-."), "Great Depression": ("#666666", ":")}
    for r in P.itertuples():
        c, ls = next(v for k, v in styles.items() if r.path.startswith(k))
        vals = [getattr(r, f"pay_{y}") / 1000 for y in yrs]
        ax.plot(yrs, vals, color=c, ls=ls, lw=1.5, label=f"{r.path} (avg {r.avg_inflation:.1%})")
    ax.axhline(50, color="#444444", lw=0.8)
    ax.set_ylabel("value of each $50,000 payment in 1 Jan 2027 dollars ($k)")
    ax.set_xlabel("payment year")
    ax.set_title("A fixed $50,000 buys less each year: real value of the ten payments (MODEL)")
    ax.legend(fontsize=6.6, loc="lower left", ncol=2)
    ax.set_ylim(0, 75)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m7_real_value.png"))
    plt.close(fig)


def main():
    os.makedirs(OUT, exist_ok=True)
    H.self_test()
    dg = downgrade_events()
    dg.to_csv(os.path.join(OUT, "downgrade_events.csv"), index=False, float_format="%.4f")
    say("[M7] Downgrade windows (FRED DGS10; S&P 500 from Yahoo, secondary):")
    for r in dg.itertuples():
        say(f"    {r.event}, {r.announced}: 10-year {r.y10_base:.2f}% -> {r.y10_end:.2f}% after 20 trading days "
            f"({r.dy_bp:+.0f}bp); S&P 500 {r.spx_change:+.1%} (lowest {r.spx_min_change:+.1%})")
    S = scenarios(dg)
    T = pd.DataFrame([run(sc) for sc in S])
    b = T[T.id == "S0"].iloc[0]
    assert abs(b.C - N["laura.ladder.cost_2027_strips"]["value"]) < 0.01
    assert abs(b.fund0 - N["laura.stock_fund_2028_usd.strips"]["value"]) < 1
    T.to_csv(os.path.join(OUT, "stress_table.csv"), index=False, float_format="%.2f")
    with open(os.path.join(OUT, "scenario_paths.json"), "w") as f:
        json.dump(S, f, indent=1, default=float)
    say("\n[M7] Stress table (REC; 2027 = 1 Jan 2027; all MODEL):")
    for r in T.itertuples():
        say(f"  {r.id:4s} {r.name[:58]:58s}| ladder {H.kusd(r.C)}, top-up {H.kusd(r.T)}, floor {H.kusd(r.F)} at "
            f"{r.y5:.2%}, fund {H.kusd(r.fund0)} -> 2031 {H.kusd(r.fund31)} -> 2033 {H.kusd(r.fund33)}; range "
            f"{H.kusd(r.F)}-{H.kusd(r.top)}; gift {H.kusd(r.gift)} (real {H.kusd(r.real_gift)}); payments "
            f"{'funded' if r.funded else 'SHORT ' + H.kusd(r.shortfall)}; real value 2042 payment {H.kusd(r.real_pay_2042)}"
            f" | All-Treasury {H.kusd(r.R1_T33)}, 60/40 {H.kusd(r.R2_T33)}, CPPI {H.kusd(r.R5_T33)}")
    th = thresholds()
    say(f"\n[M7] Thresholds (parallel fall before 1 Jan 2027, still there in Jan 2028): top-up needed beyond "
        f"{th['topup_starts_bp']:.1f}bp; stock fund used up (floor still $150,000) beyond {th['fund_used_up_bp']:.1f}bp; "
        f"a payment unfunded beyond {th['payment_unfunded_bp']:.1f}bp")
    P, HD, h19 = real_value_section(S)
    say("\n[M7] Real value of the ten $50,000 payments (1 Jan 2027 dollars):")
    for r in P.itertuples():
        say(f"    {r.path[:60]:60s} avg {r.avg_inflation:5.2%}: 2033 {H.kusd(r.pay_2033)}, 2042 {H.kusd(r.pay_2042)}, "
            f"all ten {H.kusd(r.total)}")
    hh = HD.set_index("payment")
    say(f"    U.S. history ({h19['windows']} 15-year windows 1872-2025): 2042 payment p5/p50/p95 "
        f"{H.kusd(hh.loc[2042, 'p5'])} / {H.kusd(hh.loc[2042, 'p50'])} / {H.kusd(hh.loc[2042, 'p95'])}; all ten "
        f"{H.kusd(hh.loc['total', 'p5'])} / {H.kusd(hh.loc['total', 'p50'])} / {H.kusd(hh.loc['total', 'p95'])}")
    say(f"    insight_v1 H19 reproduced with its own convention (2.5%, 7 and 16 years from 2026): "
        f"${h19['h19_reproduced']['2033']:,.0f} / ${h19['h19_reproduced']['2042']:,.0f} -> match {h19['h19_match']}; "
        f"2.5% is now sourced to JPM 2026 LTCMA U.S. inflation ({JPM_INFL:.2%})")
    figs(T, P, HD)
    res = dict(thresholds=th, stress=T.to_dict("records"), real_value_paths=P.to_dict("records"),
               real_value_history=HD.to_dict("records"), h19=h19, downgrades=dg.to_dict("records"),
               inflation_inputs=dict(T10YIE=BE, EXPINF10YR=EXPINF, JPM=JPM_INFL), spec="rab/models/M7_SPEC.md")
    with open(os.path.join(OUT, "M7_results.json"), "w") as f:
        json.dump(res, f, indent=1, default=lambda x: x.item() if hasattr(x, "item") else str(x))
    with open(os.path.join(OUT, "M7_report.txt"), "w") as f:
        f.write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
