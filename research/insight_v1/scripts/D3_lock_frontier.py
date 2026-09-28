"""D3_lock_frontier.py - M243: what is the honest reason to lock 100% of the payments in January 2027?

Question (phase_C survivors M243): with the 2028 deposit present, a 70-95% lock also shows no payment shortfall in
the model; what is our real reason to lock 100%, and where are we overstating it?

What it computes (model outputs, not forecasts):
 1. The "price of certainty" frontier (reproduces B10b_designer_checks.py): lock a share f of the ten-payment ladder
    in January 2027 (f of every rung), invest the rest 60/40 until 2033, buy the unlocked share of the payments in
    2033. No 2031 facility floor, so the comparison isolates the payments decision.
 2. The same frontier under stresses the case does not rule out: a smaller or missing 2028 deposit, a deposit cut
    that is more likely after a bad 2027 for stocks, Vanguard-midpoint equities, fat tails, and lower 2033 rates
    (the payments cost more to buy later).
 3. For each: P(payments not fully funded), mean shortfall when short, and the median 2033 surplus (what the lock
    costs the facility).
Inputs and status: strategy_mc_v2.py (VERIFIED-REPO-FILE JPM rows and curve; ASSUMPTION lognormal returns; the 2033
purchase uses the verified convention, a flat 5.26% +/- 1pp annuity, which is ~$6k dearer than forwards (F-408);
deposit-cut probability 25% and correlation 0.6 are ASSUMPTION scenarios; Vanguard 5.2% midpoint VERIFIED-PRIMARY by
B10a).
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_lock_frontier.py
"""
import sys
from dataclasses import replace

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from strategy_mc_v2 import Cfg, simulate  # noqa: E402

LOCKS = (1.0, 0.95, 0.9, 0.8, 0.7, 0.5, 0.0)
BASE = Cfg(floor_design="none")
SCENARIOS = [
    ("verified inputs, deposit $150k (B10b check)", {}),
    ("deposit $75k", {"deposit": 75_000}),
    ("deposit missing", {"deposit": 0.0}),
    ("deposit cut to $0 in 25% of paths, rho 0.6 with 2027 stocks", {"cut_prob": 0.25, "cut_frac": 1.0,
                                                                     "rho_deposit": 0.6}),
    ("Vanguard-midpoint equities 5.2%", {"eq_asset": "US_LC_VANGUARD"}),
    ("fat tails t4, same 5% bad year", {"tails": "t", "t_nu": 4.0, "t_scale": 1.09}),
    ("2033 rates centred 4.0% (payments dearer later)", {"rate33_mean": 0.040}),
    ("combined: Vanguard + $75k + 2033 rates 4.5%", {"eq_asset": "US_LC_VANGUARD", "deposit": 75_000,
                                                     "rate33_mean": 0.045}),
]


def main():
    base_med = {}
    for name, kw in SCENARIOS:
        cfg = replace(BASE, **kw)
        print(f"\n== {name}")
        print("  lock | P(payments short) | mean short if short | surplus p5/p50/p95 | median given up by locking 100%")
        meds = {}
        for f in LOCKS:
            r = simulate(cfg, "P", lock_frac=f)
            s = r["surplus"]
            short = np.maximum(-s, 0)
            meds[f] = np.median(s)
            ms = short[short > 0].mean() if (short > 0).any() else 0.0
            p5, p50, p95 = (np.percentile(s, q) / 1000 for q in (5, 50, 95))
            print(f"  {f:4.0%} | {np.mean(s < 0) * 100:6.2f}% | ${ms:,.0f} | ${p5:.0f}k/${p50:.0f}k/${p95:.0f}k | "
                  f"{(meds[f] - meds[1.0]) / 1000 if f != 1.0 else 0:+.1f}k")
        base_med[name] = meds
    print("\nReading: last column = median 2033 surplus of this lock share minus that of the 100% lock, i.e. what"
          " full certainty costs the facility at the median (negative = the full lock also has the higher median).")


if __name__ == "__main__":
    main()
