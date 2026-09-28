"""D3_ratchet.py - M055: should the facility floor be locked progressively (a third each January 2029-2031) or by
stepping sleeve equity down in 2029-30, rather than on one date in 2031?

What it computes (model outputs, not forecasts; common random numbers):
 1. The premise: how much a -30% stock year in 2030 cuts the 2031 floor at 60% sleeve equity.
 2. Designs: one-date 80% lock (plan); lock in thirds 2029/2030/2031 (B10a); a dated equity step-down
    (60% -> 50% in 2029 -> 40% from 2030) with the one-date lock; constant lower equity (50%, 45%, 40%).
    For each: 2031 floor p5/p50/p95 (2033 value), 2033 surplus p5/p50/p95, and the floor after a bottom-decile 2030.
 3. A dominance test: does any progressive design beat a simple constant-weight design with the same bad case (p5)?
    If not, the extra rule does not earn its place (brief design principle).
Inputs and status: strategy_mc_v2.py (VERIFIED-REPO-FILE JPM rows and curve; ASSUMPTION lognormal returns, lock rates
4y 4.96% / 3y 4.94% / 2y 4.81% = today's par yields assumed unchanged at each lock date, as in B10a).
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_ratchet.py
"""
import sys

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from strategy_mc_v2 import Cfg, draws, returns, simulate  # noqa: E402

DESIGNS = [("one date, 80% in 2031, 60% equity (plan)", Cfg()),
           ("thirds 2029/2030/2031, 60% equity", Cfg(floor_design="ratchet")),
           ("step-down 60/60/50/40, one date 2031", Cfg(eq_w=(0.6, 0.6, 0.5, 0.4, 0.4, 0.4))),
           ("constant 50% equity, one date 2031", Cfg(eq_w=(0.5,) * 6)),
           ("constant 45% equity, one date 2031", Cfg(eq_w=(0.45,) * 6)),
           ("constant 40% equity, one date 2031", Cfg(eq_w=(0.4,) * 6))]


def q(x, ps=(5, 50, 95)):
    return "/".join(f"${np.percentile(x, p) / 1000:.0f}k" for p in ps)


def main():
    req, _ = returns(Cfg(), draws(Cfg()))
    plan = simulate(Cfg())
    near30 = (req[:, 3] > -0.32) & (req[:, 3] < -0.28)
    print("== 1. Premise: a stock year near -30% in 2030 (paths with 2030 equity return between -32% and -28%)")
    print(f"  median 2031 floor ${np.median(plan['floor33'][near30]) / 1000:.0f}k vs ${np.median(plan['floor33']) / 1000:.0f}k"
          f" in all paths ({np.median(plan['floor33'][near30]) / np.median(plan['floor33']) - 1:+.0%}); "
          f"{near30.mean() * 100:.1f}% of paths; model P(a 2030 stock year of -30% or worse) {np.mean(req[:, 3] <= -0.30) * 100:.1f}%")
    bad30 = req[:, 3] <= np.percentile(req[:, 3], 10)
    print("\n== 2. Designs")
    print("  design | locked money for 2033 p5/p50/p95 | 2033 surplus p5/p50/p95 | locked money after a bottom-10% 2030")
    res = {}
    for name, cfg in DESIGNS:
        r = simulate(cfg)
        res[name] = r
        print(f"  {name:40s} | {q(r['locked33'])} | {q(r['surplus'])} | ${np.median(r['locked33'][bad30]) / 1000:.0f}k")
    print("\n== 3. Dominance test on the 2033 surplus (same p5 -> compare median and p95)")
    rat = res["thirds 2029/2030/2031, 60% equity"]["surplus"]
    target = np.percentile(rat, 5)
    best = None
    for w in np.arange(0.30, 0.61, 0.01):
        r = simulate(Cfg(eq_w=(round(w, 2),) * 6))["surplus"]
        gap = abs(np.percentile(r, 5) - target)
        if best is None or gap < best[0]:
            best = (gap, w, r)
    _, w, r = best
    print(f"  ratchet (thirds): p5/p50/p95 {q(rat)}")
    print(f"  constant {w:.0%} equity with the same p5: {q(r)}")
    sd = res["step-down 60/60/50/40, one date 2031"]["surplus"]
    target = np.percentile(sd, 5)
    best = None
    for w2 in np.arange(0.30, 0.61, 0.01):
        rr = simulate(Cfg(eq_w=(round(w2, 2),) * 6))["surplus"]
        gap = abs(np.percentile(rr, 5) - target)
        if best is None or gap < best[0]:
            best = (gap, w2, rr)
    print(f"  step-down: p5/p50/p95 {q(sd)}; constant {best[1]:.0%} equity with the same p5: {q(best[2])}")


if __name__ == "__main__":
    main()
