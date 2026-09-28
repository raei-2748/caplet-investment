"""AX1_quant_audit.py - AX1 (cluster auditor, rates and quant) checks on D3_quant.md and D3_model_v2_results.md.

What it does (plain English): re-uses the D3 model code unchanged (strategy_mc_v2.py, D3_funded_status_log.py) and
the saved D3 data snapshots to reproduce every number the AX1 audit adds. It does not change any D3 file.

Checks printed:
 [1] v2 reproduces the verified strategy_mc.py path by path (lock-early and growth-first).
 [2] Equity "lift" over the all-Treasury control: MEAN vs MEDIAN, in five assumption sets (D3 reports medians only).
 [3] Why the central-case control is wide: its p5/p50/p95 with and without the Sep-Dec 2026 rate move.
 [4] Barbell vs the plan's own equity frontier (same model, sleeve bonds at JPM 4.0% and at 5.0%): is the barbell
     "just a lower-equity point on the same frontier"?
 [5] 2026 history: on how many of 185 official curve dates the real Nov-15 STRIPS ladder cost <= $300,000.
 [6] FRED 10-year yield: how often a fall of 19bp / 50bp / 100bp / 150bp happened over 98 calendar days (the time
     from 25 Sep to 1 Jan), and the worst such fall since 1990; the ladder gap and the Jan-2028 cost to finish it at
     that worst fall.
 [7] The mean January-2027 gap in cost dollars vs in payment face dollars.
 [9] Unbought payment face at a -50bp / -100bp fall: longest rungs first (plan) vs nearest rungs first.
 [8] Two 2033 contribution rules with the same flexibility (D3's "give 90%, capped" vs "bought floor + half of the
     rest", uncapped): which one announces the higher bottom in 2031?

Inputs and status labels:
 - research/insight_v1/scripts/strategy_mc_v2.py (D3 model: VERIFIED-REPO-FILE curve 2026-09-25 and JPM 2026 LTCMA rows;
   ASSUMPTION lognormal returns, zero-drift rate moves, 2031 2y yield 4.81%, barbell lock 4.98%).
 - research/verified_2026-09-27/strategy_mc.py (verified base model).
 - research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv (treasury.gov 2026 daily par curves, VERIFIED-PRIMARY,
   re-checked 2026-09-28: live 09/25/2026 row equals the repo file).
 - research/insight_v1/scripts/data/D3/fred_DGS10.csv (FRED DGS10, VERIFIED-PRIMARY; spot-checked live 2026-09-28:
   2008-12-31 2.25, 2026-09-24 5.18).
Run from the repo root (about 15 seconds):  .venv/bin/python research/insight_v1/scripts/AX1_quant_audit.py
"""
import csv
import importlib.util
import sys
from dataclasses import replace
from datetime import date, timedelta

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
import D3_funded_status_log as LOG  # noqa: E402
from strategy_mc_v2 import CENTRAL, TABLES, Cfg, interp_rows, simulate  # noqa: E402

FRED10 = "research/insight_v1/scripts/data/D3/fred_DGS10.csv"


def q(x, ps=(5, 50, 95)):
    return "/".join(f"${np.percentile(x, p) / 1000:.0f}k" for p in ps)


def check1():
    print("[1] Path-by-path reproduction of the verified model")
    spec = importlib.util.spec_from_file_location("smc", "research/verified_2026-09-27/strategy_mc.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    a, b = m.simulate("L")["surplus"], simulate(Cfg())["surplus"]
    ga, gb = m.simulate("G")["surplus"], simulate(Cfg(), "G")["surplus"]
    print(f"  lock-early: largest path difference ${np.abs(a - b).max():.2f}; growth-first: ${np.abs(ga - gb).max():.2f}; "
          f"G miss {np.mean(gb < 0):.1%}")


def check2():
    print("\n[2] 60% sleeve equity vs the all-Treasury control: median lift (what D3 reports) vs mean lift")
    sets = [("verified inputs", Cfg()), ("central", CENTRAL),
            ("central, sleeve bonds 4.9%", replace(CENTRAL, bd_asset="SHORT_TSY_FWD")),
            ("central, Vanguard 5.2%", replace(CENTRAL, eq_asset="US_LC_VANGUARD")),
            ("central, 0.5% sleeve fee", replace(CENTRAL, adv_fee_sleeve=0.005))]
    for label, base in sets:
        ctl = simulate(replace(base, adv_fee_sleeve=0.0, adv_fee_ladder=0.0, fund_expense=0.0), "C")["surplus"]
        p0 = simulate(replace(base, eq_w=(0.0,) * 6))["surplus"]
        p60 = simulate(replace(base, eq_w=(0.6,) * 6))["surplus"]
        print(f"  {label:27s} median lift {np.median(p60) / 1e3 - np.median(ctl) / 1e3:+5.1f}k | mean lift "
              f"{(p60 - ctl).mean() / 1e3:+5.1f}k | 60% vs 0% equity inside the plan: median "
              f"{np.median(p60) / 1e3 - np.median(p0) / 1e3:+5.1f}k, mean {(p60 - p0).mean() / 1e3:+5.1f}k")


def check3():
    print("\n[3] The 'riskless' control seen from today (p5/p50/p95 of its 2033 value)")
    for label, cfg in [("verified inputs (no Sep-Dec rate move)", Cfg()), ("central (Sep-Dec move sd 0.37pp)", CENTRAL),
                       ("central without the Sep-Dec move", replace(CENTRAL, pre_rate_sd=0.0))]:
        print(f"  {label:40s} {q(simulate(cfg, 'C')['surplus'])}")


def check4():
    print("\n[4] Barbell vs the plan's equity frontier (2033 surplus p5/p50/p95; verified inputs otherwise)")
    for bd, name in (("INT_TSY", "sleeve bonds JPM 4.0%"), ("INT_TSY_FWD", "sleeve bonds 5.0%")):
        print(f"  -- {name}")
        for w in (0.0, 0.2, 0.3, 0.4, 0.6):
            print(f"     plan, {w:.0%} sleeve equity      {q(simulate(Cfg(bd_asset=bd, eq_w=(w,) * 6))['surplus'])}")
        for x in (0.5, 0.65, 0.8):
            r = simulate(Cfg(bd_asset=bd, floor_design="barbell", barbell_share=x))
            print(f"     barbell {x:.0%} (rest 100% stock) {q(r['surplus'])}")
    print("  (whole-portfolio equity on 2028-01-01: plan 20% sleeve equity = 6.8% = barbell 80%; plan 60% = 20.4%)")


def check5():
    print("\n[5] 2026: days the ten-payment ladder cost <= $300,000 for 1 Jan 2027 (185 official curve dates)")
    n_ex = n_st = 0
    first = None
    curves = LOG.load_curves()
    for t, par in curves:
        f = LOG.build(par)
        n_ex += LOG.liab_2027(t, f) <= 300_000
        if LOG.liab_2027(t, f, LOG.STRIPS) <= 300_000:
            n_st += 1
            first = first or t
    print(f"  exact Jan-1 dates: {n_ex} of {len(curves)}; real Nov-15 STRIPS ladder: {n_st} of {len(curves)} (first: {first})")


def ladder_at(shift):
    r27 = interp_rows(TABLES["strip"][1], np.array([shift]))[0]
    r28 = interp_rows(TABLES["strip"][2], np.array([shift]))[0]
    frac, left = np.zeros(10), 300_000.0
    for i in range(9, -1, -1):                       # longest rungs first
        take = min(1.0, max(left, 0) / r27[i])
        frac[i], left = take, left - take * r27[i]
    return r27.sum(), ((1 - frac) * r28).sum()


def check6():
    print("\n[6] FRED DGS10: falls over 98 calendar days (25 Sep -> 1 Jan)")
    d = {}
    for r in csv.reader(line for line in open(FRED10) if not line.startswith("#")):
        try:
            d[date.fromisoformat(r[0])] = float(r[1])
        except ValueError:
            pass
    ds = sorted(d)
    res = []
    for t in ds:
        k = t + timedelta(days=98)
        if k > ds[-1]:
            break
        while k not in d and k > t:
            k -= timedelta(days=1)
        if k > t:
            res.append((d[k] - d[t], t, k))
    for since in (1962, 1990):
        x = np.array([a for a, b, _ in res if b.year >= since])
        print(f"  since {since} (n={len(x)}): fall >=19bp {np.mean(x <= -0.19):.1%}; >=50bp {np.mean(x <= -0.5):.1%}; "
              f">=100bp {np.mean(x <= -1.0):.2%}; >=150bp {np.mean(x <= -1.5):.2%}")
    worst = min((r for r in res if r[1].year >= 1990), key=lambda r: r[0])
    cost, finish = ladder_at(round(worst[0], 2))
    print(f"  worst since 1990: {worst[0] * 100:+.0f}bp ({worst[1]} -> {worst[2]}); at that parallel fall the STRIPS ladder "
          f"costs ${cost:,.0f} (gap ${cost - 300_000:,.0f}); finishing it in Jan 2028 with no further move ${finish:,.0f}")
    cost, finish = ladder_at(-1.5)
    print(f"  at -150bp: cost ${cost:,.0f}; finish in Jan 2028 ${finish:,.0f}")


def check7():
    print("\n[7] Mean January-2027 gap: cost dollars vs payment-face dollars (central case, deposit missing)")
    r = simulate(replace(CENTRAL, deposit=0.0))
    g = r["gap27"]
    sf = r["short_face"]
    print(f"  P(gap) {np.mean(g > 0):.1%}; mean gap if >0 ${g[g > 0].mean():,.0f} (Jan-2027 cost); mean unbought face "
          f"if short ${sf[sf > 0].mean():,.0f}")


def check8():
    from strategy_mc_v2 import growth_2y, range_eval
    print("\n[8] Contribution rules with the same flexibility: what bottom does each announce? (80% floor, p80 top)")
    rules = [("give 90%, capped (D3 M039 pick)", dict(contribution="share_cap", share=0.9)),
             ("bought floor + half of the rest, uncapped (D5-type)", dict(contribution="excess", k_excess=0.5)),
             ("give everything, capped", dict(contribution="cap"))]
    for label, cfg in (("verified", Cfg()), ("central", CENTRAL)):
        res, g = simulate(cfg), growth_2y(cfg)
        for name, kw in rules:
            e = range_eval(res, ("pct", 80), g, **kw)
            print(f"  {label:8s} {name:52s} announced bottom/top median ${np.median(e['lo']) / 1e3:.0f}k/"
                  f"${np.median(e['hi']) / 1e3:.0f}k | contribution {q(e['C'])} | flexibility {q(e['flex'])} | "
                  f"P(within) {e['p_within']:.0%}, P(top reached) {e['p_top']:.0%}")


def check9():
    print("\n[9] Unbought payment face before the 2028 top-up: longest-first (plan) vs nearest-first")
    for shift in (-0.5, -1.0):
        r27 = interp_rows(TABLES["strip"][1], np.array([shift]))[0]
        out = []
        for order in (range(9, -1, -1), range(10)):
            frac, left = np.zeros(10), 300_000.0
            for i in order:
                take = min(1.0, max(left, 0) / r27[i])
                frac[i], left = take, left - take * r27[i]
            yrs = [2033 + i for i in range(10) if frac[i] < 1]
            out.append(f"${((1 - frac) * 50_000).sum():,.0f} of {yrs}")
        print(f"  {shift * 100:+.0f}bp: longest-first {out[0]}; nearest-first {out[1]}")


if __name__ == "__main__":
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
    check7()
    check8()
    check9()
