"""D3_range_rules.py - M039 and M060: the 2031 co-sponsor range (floor share, top rule, cap rule) and how confident
Laura can honestly be that her 2033 contribution lands inside it.

Questions (phase_C survivors):
 - M060: what share of the 2031 sleeve should be locked as the floor (80%, or towards 100%)?
 - M039: since Laura decides the contribution, should the range be partly a policy (never give more than the top;
   keep any excess as flexibility), so the confidence is about the bottom and the top is a stated percentile?

What it computes (model outputs, not forecasts):
 1. Floor share 50-100%: 2033 surplus p5/p50/p95 (2027 view), median bought floor, median range width for a top set
    at the 80th / 90th percentile of the unlocked money's 2-year growth (computed in 2031 from the planning model).
 2. What Laura would actually announce in 2031 in a bad / middle / good 2031 state (sleeve at its p10/p50/p90).
 3. Contribution rules: give everything / cap at the top / give a share of the post-reserve money (with and without
    cap). For each: P(contribution below / within / above the range), P(top reached), and the flexibility kept.
 4. How model-dependent the stated confidence is: the same range rule tested on fat tails, weaker/stronger equities,
    Vanguard-midpoint equities, and on every historical 2-year period 1928-2025 (raw, and rescaled to JPM's medians).
 5. The 2031 2-year yield at 3.0% / 4.0% / 4.81% (M060 caveat).
Inputs and status: strategy_mc_v2.py (VERIFIED-REPO-FILE JPM rows and curve; ASSUMPTION lognormal returns, 2031 2y
yield 4.81%); historical annual returns, Damodaran histretSP (VERIFIED-PRIMARY dataset page, accessed 2026-09-28,
snapshot data/D3/damodaran_histretSP_1928_2025.csv): S&P 500 incl. dividends for equity; sleeve bonds proxied by
50% 3-month T-bill + 50% 10-year Treasury bond (ASSUMPTION: about the duration of an intermediate Treasury index).
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_range_rules.py
"""
import csv
import sys
from dataclasses import replace

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from strategy_mc_v2 import Cfg, growth_2y, pct, range_eval, simulate  # noqa: E402

HIST = "research/insight_v1/scripts/data/D3/damodaran_histretSP_1928_2025.csv"


def load_hist():
    rows = [r for r in csv.DictReader(l for l in open(HIST) if not l.startswith("#"))]
    yrs = np.array([int(r["year"]) for r in rows])
    eq = np.array([float(r["sp500_tr"]) for r in rows])
    bd = 0.5 * np.array([float(r["tbill_3m_avg"]) for r in rows]) + 0.5 * np.array([float(r["tbond_10y_tr"]) for r in rows])
    return yrs, eq, bd


def rescale(x, target_compound):
    """Keep the historical sequence of good and bad years, but move the average (log) return to the target."""
    lx = np.log1p(x)
    return np.expm1(lx - lx.mean() + np.log1p(target_compound))


def main():
    plan = growth_2y(Cfg())
    print("Planning model 2-year growth of the unlocked 60/40 money (2031-2032): p10/p20/p50/p80/p90 = " +
          ", ".join(f"{np.percentile(plan, q):.3f}" for q in (10, 20, 50, 80, 90)))

    print("\n== 1. Floor share (one-date lock, 1 January 2031, 2-year Treasury at 4.81%)")
    print("  share | 2033 surplus p5/p50/p95 | floor p5/p50/p95 | median width p80 top | p90 top | P(surplus >= 1.25 x floor)")
    for a in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        cfg = Cfg(floor_share=a)
        r = simulate(cfg)
        pg = growth_2y(cfg)
        e80, e90 = range_eval(r, ("pct", 80), pg), range_eval(r, ("pct", 90), pg)
        print(f"  {a:4.0%} | {'/'.join(f'${v}k' for v in pct(r['surplus']))} | {'/'.join(f'${v}k' for v in pct(r['floor33']))} | "
              f"${np.median(e80['hi'] - e80['lo']) / 1000:.0f}k | ${np.median(e90['hi'] - e90['lo']) / 1000:.0f}k | "
              f"{np.mean(r['surplus'] >= 1.25 * r['floor33']) * 100:.0f}%")

    print("\n== 2. What Laura would announce in 2031 (80% floor; p80 top), by how 2027-2030 went")
    r = simulate(Cfg())
    s31 = r["S31"]
    for q, lab in ((10, "bad (p10)"), (50, "middle (p50)"), (90, "good (p90)")):
        v = np.percentile(s31, q)
        F = 0.8 * v * 1.0481 ** 2
        R = 0.2 * v
        print(f"  {lab:12s}: sleeve on 1 Jan 2031 ${v / 1000:.0f}k -> floor ${F / 1000:.0f}k (bought), most likely "
              f"${(F + R * np.percentile(plan, 50)) / 1000:.0f}k, top p80 ${(F + R * np.percentile(plan, 80)) / 1000:.0f}k,"
              f" top p90 ${(F + R * np.percentile(plan, 90)) / 1000:.0f}k; floor = {F / (F + R * np.percentile(plan, 80)):.0%}"
              f" of the p80 top")

    print("\n== 3. Contribution rules (80% floor; top = p80 or p90 of the unlocked money's 2-year growth)")
    print("  rule | top | P(below) | P(within) | P(above) | P(top reached) | contribution p5/p50/p95 | flexibility p5/p50/p95")
    for top in (80, 90):
        for name, kw in (("give all of the surplus", dict(contribution="all")),
                         ("give all, capped at the top", dict(contribution="cap")),
                         ("give 90%, no cap", dict(contribution="share", share=0.9)),
                         ("give 90%, capped", dict(contribution="share_cap", share=0.9)),
                         ("give 80%, capped", dict(contribution="share_cap", share=0.8))):
            e = range_eval(r, ("pct", top), plan, **kw)
            print(f"  {name:28s} | p{top} | {e['p_below'] * 100:.1f}% | {e['p_within'] * 100:.1f}% | "
                  f"{e['p_above'] * 100:.1f}% | {e['p_top'] * 100:.0f}% | {'/'.join(f'${v}k' for v in pct(e['C']))} | "
                  f"{'/'.join(f'${v}k' for v in pct(e['flex']))}")

    print("\n== 4. Is the stated confidence model-proof? Range set with the planning model (80% floor), no cap:")
    print("  outcome model | P(within) with p80 top | with p90 top | P(below)")
    tests = [("planning model itself", Cfg()), ("fat tails t4", Cfg(tails="t", t_nu=4.0)),
             ("fat tails t4, same 5% bad year", Cfg(tails="t", t_nu=4.0, t_scale=1.09)),
             ("Vanguard-midpoint equities", Cfg(eq_asset="US_LC_VANGUARD")),
             ("equities 1.7pp/yr weaker", Cfg(eq_mu_shift=np.log(1.05) - np.log(1.067))),
             ("equities 3pp/yr stronger", Cfg(eq_mu_shift=np.log(1.097) - np.log(1.067))),
             ("0.5% advisory fee on ladder too", Cfg(adv_fee_ladder=0.005))]
    for name, cfg in tests:
        rr = simulate(cfg)
        e80, e90 = range_eval(rr, ("pct", 80), plan), range_eval(rr, ("pct", 90), plan)
        print(f"  {name:32s} | {e80['p_within'] * 100:5.1f}% | {e90['p_within'] * 100:5.1f}% | "
              f"{e80['p_below'] * 100:.2f}% (fees dent floor in {np.mean(rr['breach'] > 0) * 100:.2f}% of paths)")
    yrs, heq, hbd = load_hist()
    g80, g90 = np.percentile(plan, 80), np.percentile(plan, 90)
    for lab, eq, bd in (("historical 1928-2025, raw", heq, hbd),
                        ("historical, rescaled to JPM medians", rescale(heq, 0.067), rescale(hbd, 0.040))):
        mixr = 0.6 * eq + 0.4 * bd
        g2 = (1 + mixr[:-1]) * (1 + mixr[1:])
        print(f"  {lab:32s} | {np.mean(g2 <= g80) * 100:5.1f}% | {np.mean(g2 <= g90) * 100:5.1f}% | 0% (floor bought)"
              f"   [{len(g2)} overlapping 2-year periods; worst {yrs[:-1][g2.argmin()]}-{yrs[1:][g2.argmin()]}: "
              f"{(g2.min() - 1) * 100:+.1f}%]")
    print("  (P(within) for the whole-surplus rule equals the share of outcomes at or below the top; the bought floor"
          " makes P(below) zero in every row except where fees are charged to it)")

    print("\n== 5. 2031 2-year Treasury yield (floor 80%): median bought floor")
    for y in (0.03, 0.035, 0.04, 0.0481):
        rr = simulate(Cfg(y2_2031=y))
        print(f"  {y * 100:.2f}%: floor median ${np.median(rr['floor33']) / 1000:.1f}k; 2033 surplus median "
              f"${np.median(rr['surplus']) / 1000:.1f}k")


if __name__ == "__main__":
    main()
