"""D3_control_and_equity.py - M034: judge the sleeve's equity against Laura's riskless control, not against a stock index.

Question (phase_C survivors M034): should every sleeve recommendation be judged against the money Laura could lock
for certain (the whole surplus in Treasuries maturing just before 2033), and does 60% sleeve equity earn its risk?

What it computes (all model outputs, not forecasts):
 1. The riskless control: the 2027 leftover in a zero-coupon Treasury maturing 2033-01-01 at today's forward, and
    the $150k 2028 deposit locked the same way at the January-2028 rate (today's forward +/- a yearly rate move).
 2. Sleeve equity 0/20/40/50/60/70/100% (80% of the sleeve locked in 2031, as in the plan): 2033 surplus
    p5/p25/p50/p75/p95, the "lift" over the control on the SAME simulated path, and P(plan ends below control).
 3. The same under: the D3 central case (real STRIPS ladder, Sep-Dec 2026 rate risk, AC World + short govt/credit,
    fund expenses); forward-consistent sleeve bonds; Vanguard-midpoint equities; a 0.5% advisory fee on the sleeve.
 4. Whole-portfolio equity share in 2028 implied by each sleeve weight.

Inputs and status: everything comes from strategy_mc_v2.py (see its docstring): VERIFIED-REPO-FILE curve and JPM
rows; ASSUMPTION lognormal returns, 2031 2y yield 4.81%, yearly rate-move sd 0.71pp (F-014), fee levels.
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_control_and_equity.py
"""
import sys
from dataclasses import replace

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from strategy_mc_v2 import CENTRAL, FWD_28_33, FWD_FACTOR_27_33, Cfg, pct, simulate  # noqa: E402

WEIGHTS = (0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 1.0)


def frontier(base, label):
    # Laura can lock the control herself: no advisory fee and no fund expense on it
    ctl = simulate(replace(base, adv_fee_sleeve=0.0, adv_fee_ladder=0.0, fund_expense=0.0), "C")["surplus"]
    print(f"\n== {label}")
    print(f"  riskless control p5/p50/p95: ${pct(ctl)[0]}k/${pct(ctl)[1]}k/${pct(ctl)[2]}k")
    print("  sleeve equity | surplus p5/p25/p50/p75/p95 | median lift vs control | lift p5 / p95 (same path) | "
          "P(plan < control)")
    rows = {}
    for w in WEIGHTS:
        r = simulate(replace(base, eq_w=(w,) * 6))["surplus"]
        lift = r - ctl
        rows[w] = (np.percentile(r, [5, 50, 95]), np.median(lift))
        print(f"  {w:5.0%} | {'/'.join(f'${v}k' for v in pct(r, (5, 25, 50, 75, 95)))} | "
              f"{np.median(r) / 1000 - np.median(ctl) / 1000:+.1f}k | "
              f"{np.percentile(lift, 5) / 1000:+.0f}k / {np.percentile(lift, 95) / 1000:+.0f}k | "
              f"{np.mean(r < ctl) * 100:.0f}%")
    (p5a, p50a, p95a), _ = rows[0.4]
    (p5b, p50b, p95b), _ = rows[0.6]
    print(f"  40% -> 60% equity: p5 {(p5b - p5a) / 1000:+.1f}k, p50 {(p50b - p50a) / 1000:+.1f}k, "
          f"p95 {(p95b - p95a) / 1000:+.1f}k")
    return rows


def main():
    print("Riskless control arithmetic (today's curve, no rate move): 2027 leftover $7,736 x "
          f"{FWD_FACTOR_27_33:.4f} = ${7736 * FWD_FACTOR_27_33:,.0f}; $150,000 x {FWD_28_33:.4f} (2028->2033 forward) = "
          f"${150000 * FWD_28_33:,.0f}; total ${7736 * FWD_FACTOR_27_33 + 150000 * FWD_28_33:,.0f}")
    frontier(Cfg(), "VERIFIED inputs (US large cap, JPM intermediate Treasuries 4.0%)")
    frontier(CENTRAL, "D3 CENTRAL (STRIPS ladder, Sep-Dec rate risk, AC World + short govt/credit 4.0%, fund expenses)")
    frontier(replace(CENTRAL, bd_asset="SHORT_TSY_FWD"), "CENTRAL with sleeve bonds at the forward-implied 4.9%")
    frontier(replace(CENTRAL, eq_asset="US_LC_VANGUARD"), "CENTRAL with Vanguard-midpoint equities (5.2%)")
    frontier(replace(CENTRAL, adv_fee_sleeve=0.005), "CENTRAL with a 0.5% advisory fee on the sleeve (control pays none)")

    print("\n== Whole-portfolio equity share at 2028-01-01 (median sleeve; ladder at forward value $306,077 F-106)")
    s28 = (300_000 - 292_264) * 1.055 + 150_000
    for w in WEIGHTS:
        print(f"  sleeve equity {w:4.0%}: whole-portfolio equity {w * s28 / (306_077 + s28) * 100:4.1f}%")
    print("  WInS option (ii) weights at 66% hedge: VT = sleeve share x 33%: " + ", ".join(
        f"{w:.0%} -> VT {w * 33:.1f}% / VGSH {(1 - w) * 33:.1f}%" for w in (0.4, 0.5, 0.6)))


if __name__ == "__main__":
    main()
