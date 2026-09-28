"""D3_barbell.py - M238: should the sleeve be a "barbell" (lock a facility floor in January 2028 in a Treasury that
matures just before 2033, hold the rest 100% in broad equity) instead of a rebalanced 60/40 sleeve plus an 80% lock
in 2031?

What it computes (model outputs, not forecasts; common random numbers, so differences are caused by the design):
 1. 2033 surplus p1/p5/p50/p95 for the plan and barbells locking 50/65/80% of the January-2028 sleeve.
 2. The 2031 co-sponsor announcement each design supports: bought floor, p80 top (from the unlocked money's 2-year
    growth under the same model), median width, and the floor as a share of the top.
 3. Robustness: fat tails (t4, same 5% bad year), Vanguard-midpoint equities, a lower January-2028 lock rate (4.0%),
    a stock crash in 2031-32 (bottom decile of 2-year equity returns), and every historical 6-year window 1928-2025
    (S&P 500 + bond proxy; raw and rescaled to JPM's medians).
Inputs and status: strategy_mc_v2.py (VERIFIED-REPO-FILE curve and JPM rows; ASSUMPTION lognormal returns; barbell
lock at today's 5-year par yield 4.98% (F-001) as if unchanged in January 2028, as in B10a); historical returns from
Damodaran histretSP (VERIFIED-PRIMARY dataset page, accessed 2026-09-28): S&P 500 incl. dividends; sleeve bonds =
50% 3-month T-bill + 50% 10-year Treasury bond (ASSUMPTION proxy for intermediate Treasuries).
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_barbell.py
"""
import sys
from dataclasses import replace

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from D3_range_rules import load_hist, rescale  # noqa: E402
from strategy_mc_v2 import Cfg, draws, growth_2y, range_eval, returns, simulate  # noqa: E402

PLAN = Cfg()
DESIGNS = [("plan: 60/40 sleeve, 80% lock in 2031", PLAN)] + [
    (f"barbell: lock {x:.0%} in Jan 2028, rest 100% equity", Cfg(floor_design="barbell", barbell_share=x))
    for x in (0.5, 0.65, 0.8)]


def q(x, ps=(1, 5, 50, 95)):
    return "/".join(f"${np.percentile(x, p) / 1000:.0f}k" for p in ps)


def main():
    print("== 1-2. Outcomes and the 2031 announcement (JPM U.S. large cap; intermediate Treasuries)")
    print("  design | 2033 surplus p1/p5/p50/p95 | floor known in | median floor | median p80 top | median width | "
          "floor/top | P(within, no cap)")
    base_draws = draws(PLAN)
    req, _ = returns(PLAN, base_draws)
    crash = (1 + req[:, 4]) * (1 + req[:, 5]) <= np.percentile((1 + req[:, 4]) * (1 + req[:, 5]), 10)
    results = {}
    for name, cfg in DESIGNS:
        r = simulate(cfg)
        e = range_eval(r, ("pct", 80), growth_2y(cfg))
        results[name] = r
        known = "2031" if cfg.floor_design == "one_date" else "2028"
        print(f"  {name:42s} | {q(r['surplus'])} | {known} | ${np.median(r['locked33']) / 1000:.0f}k | "
              f"${np.median(e['hi']) / 1000:.0f}k | ${np.median(e['hi'] - e['lo']) / 1000:.0f}k | "
              f"{np.median(e['lo'] / e['hi']):.0%} | {e['p_within'] * 100:.0f}%")

    print("\n== 3a. Robustness (2033 surplus p1/p5/p50/p95)")
    tests = [("fat tails t4, same 5% bad year", dict(tails="t", t_nu=4.0, t_scale=1.09)),
             ("Vanguard-midpoint equities 5.2%", dict(eq_asset="US_LC_VANGUARD")),
             ("AC World equity + short govt/credit", dict(eq_asset="ACWI", bd_asset="SHORT_GC")),
             ("sleeve bonds at 5.0% (removes the JPM-4.0% vs 4.98%-lock gap)", dict(bd_asset="INT_TSY_FWD"))]
    for tname, kw in tests:
        print(f"  -- {tname}")
        for name, cfg in DESIGNS:
            print(f"     {name:42s} | {q(simulate(replace(cfg, **kw))['surplus'])}")
    print("  -- barbell lock rate 4.0% instead of 4.98% (rates fell by January 2028)")
    for x in (0.5, 0.65, 0.8):
        r = simulate(Cfg(floor_design="barbell", barbell_share=x, barbell_rate=0.04))
        print(f"     barbell {x:.0%}                                      | {q(r['surplus'])}")
    print("\n   whole-portfolio equity share on 2028-01-01 at medians (ladder $306,077 at forward value, F-106):")
    s28 = (300_000 - 292_264) * 1.055 + 150_000
    print(f"     plan {0.6 * s28 / (306_077 + s28):.1%}; barbell 50% {0.5 * s28 / (306_077 + s28):.1%}; "
          f"barbell 65% {0.35 * s28 / (306_077 + s28):.1%}; barbell 80% {0.2 * s28 / (306_077 + s28):.1%}")
    print("\n== 3b. A stock crash in 2031-32 (bottom 10% of 2-year equity returns, i.e. after the 2031 announcement)")
    for name, cfg in DESIGNS:
        r = results[name]
        e = range_eval(r, ("pct", 80), growth_2y(cfg))
        print(f"  {name:42s} | median surplus ${np.median(r['surplus'][crash]) / 1000:.0f}k "
              f"(all paths ${np.median(r['surplus']) / 1000:.0f}k); share of the announced range's width lost "
              f"{np.median(((e['hi'] - r['surplus']) / (e['hi'] - e['lo']))[crash]):.0%}")

    print("\n== 3c. Every historical 6-year window 1928-2025 placed in 2027-2032 (93 windows)")
    yrs, heq, hbd = load_hist()
    for lab, eq, bd in (("raw history", heq, hbd), ("rescaled to JPM medians", rescale(heq, 0.067), rescale(hbd, 0.040))):
        n = len(eq) - 5
        R = np.array([eq[i:i + 6] for i in range(n)])
        B = np.array([bd[i:i + 6] for i in range(n)])
        print(f"  -- {lab}")
        for name, cfg in DESIGNS:
            r = simulate(cfg, ret=(R, B))
            s = r["surplus"]
            w = s.argmin()
            print(f"     {name:42s} | min ${s.min() / 1000:.0f}k (start {yrs[w]}), p10 ${np.percentile(s, 10) / 1000:.0f}k,"
                  f" median ${np.median(s) / 1000:.0f}k, max ${s.max() / 1000:.0f}k")
        for start in (1929, 1973, 2000, 2007):
            i = int(np.where(yrs == start)[0][0])
            vals = [simulate(cfg, ret=(R[i:i + 1], B[i:i + 1]))["surplus"][0] for _, cfg in DESIGNS]
            print(f"     {start}-{start + 5} sequence: " + ", ".join(
                f"{nm.split(':')[0]} {nm.split(':')[1].split(',')[0].strip() if 'barbell' in nm else ''} ${v / 1000:.0f}k".replace("  ", " ")
                for (nm, _), v in zip(DESIGNS, vals)))


if __name__ == "__main__":
    main()
