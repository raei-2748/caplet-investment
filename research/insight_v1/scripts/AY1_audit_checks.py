"""AY1 (cluster auditor: client psychology and co-sponsors) - checks behind the corrections to D5, D6 and D12.

How to run (repo root):  .venv/bin/python research/insight_v1/scripts/AY1_audit_checks.py   (about 10 seconds)

It re-uses the specialists' own engines (same random stream, same inputs), so every difference from their files is a
difference in what is computed, not in the simulation:
- D5 engine: research/insight_v1/scripts/D5_range_and_flexibility.py (draws, sleeve_2031, G_FLOOR).
- D6 engine: research/insight_v1/scripts/D6_behavioural_numbers.py (draws, lock_early, BD, BD_CONSISTENT, EQ).

INPUTS and status labels (all inherited; nothing new is assumed except where marked)
- Ladder $292,264 at 2027-01-01 (VERIFIED-REPO-FILE, official_curve_pv.py); 2y par 4.81% on 2026-09-25 used as the
  2031 two-year rate (VERIFIED-REPO-FILE input, ASSUMPTION that it holds in 2031).
- JPM 2026 LTCMA U.S. large cap 6.70%/7.94%, intermediate Treasuries 4.00%/4.06%, correlation -0.01
  (VERIFIED-REPO-FILE); sleeve bonds 5.00% in D6 case B (ASSUMPTION, D6/B10a); Student-t df=4 fat tails (ASSUMPTION,
  D6's own check).
- Rule parameters a (2031 lock share), s (give-back share), q (top percentile): TEAM CHOICES (ASSUMPTION).
- 2031 two-year rates 3.0% and 6.0% in check [4]: illustrative ASSUMPTIONS, not forecasts.
- WInS weights (option ii hedge 66% of $300,000): research/insight_v1/wins_now/securities_and_allocation_v0.md
  (provisional ticket).

WHAT IT PRINTS
 [1] D5: the 2033 gift given the median 2031 growth money (a=0.7, s=0.5): p1/p5/p50/p95/p99 and the share of paths
     in D5's quoted "$168k-$184k" band (D5 wrote "98% of paths (p1-p95)").
 [2] D5 vs D6: range width top/bottom as a function of BOTH the lock share a and the give-back share s. D6's ratios
     assume s = 1 (everything unlocked is promised); D5 recommends s = 0.5.
 [3] D6: the "plain rule" (most stock with P(2033 growth money < money put in) <= 5%) on a 5-point grid, for lock
     shares 0.8 and 0.7, cases A (bonds 4%) and B (bonds 5%), normal and fat-tailed equity returns.
 [3b] D6: the same rule with a 0.5% or 1.0% yearly fee on the growth money (ASSUMPTION).
 [4] D5/D6: how much the bought 2031 floor moves if the 2031 two-year rate is not 4.81%.
 [5] D6/D12: WInS hedge dollars vs the $292k promise (the note cannot say the WInS trade is "sized to $292k").
"""
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # both scripts guard their printing with __main__, so importing is silent
    return mod


D5 = load("D5_range_and_flexibility")
D6 = load("D6_behavioural_numbers")


def k(x):
    return f"${x / 1000:,.1f}k"


def check1():
    print("[1] D5 conditional gift at the median 2031 growth money (a=0.7, s=0.5)")
    r = D5.draws()
    S = D5.sleeve_2031(r)
    G2 = r[:, 4] * r[:, 5]
    S_med = float(np.median(S))
    F = 0.7 * S_med * D5.G_FLOOR
    T = F + 0.15 * S_med * float(np.percentile(G2, 85))
    gift = F + 0.15 * S_med * G2
    ps = (1, 5, 50, 95, 99)
    print("    floor", k(F), "top(q=85)", k(T), "midpoint", k((F + T) / 2))
    print("    gift p1/p5/p50/p95/p99:", " / ".join(k(np.percentile(gift, p)) for p in ps))
    inside = ((gift >= 168_000) & (gift <= 184_000)).mean()
    print(f"    share of paths with gift in $168k-$184k: {inside:.3f}  (p1-p95 spans 94% of paths by definition)")
    print(f"    share of paths with gift below the midpoint: {(gift < (F + T) / 2).mean():.4f};"
          f" 2-year growth of the unlocked part needed to fall below it: G2 < {((F + T) / 2 - F) / (0.15 * S_med):.3f}")
    print(f"    => the lower half of the stated range is reached only if the unlocked money loses about"
          f" {(1 - ((F + T) / 2 - F) / (0.15 * S_med)) * 100:.0f}% in two years")


def check2():
    print("\n[2] Range width (top / bottom) depends on the lock share a AND the give-back share s")
    r = D5.draws()
    G2 = r[:, 4] * r[:, 5]
    for q in (0.85, 0.90):
        gq = float(np.percentile(G2, q * 100))
        row = []
        for a in (0.6, 0.7, 0.8, 0.9):
            for s in (0.5, 1.0):
                ratio = 1 + s * (1 - a) / a * gq / D5.G_FLOOR       # independent of the 2031 sleeve size
                row.append(f"a={a:.1f},s={s:.1f}: {ratio:.2f}x")
        print(f"    top at q={q:.2f}: " + "; ".join(row))
    print("    at-risk promised share s*(1-a): D5 (0.7,0.5) = 0.15; D6 base (0.8,1.0) = 0.20; D6 edge (0.7,1.0) = 0.30")


def plain_rule(req, rbd, floor_share, ws):
    money_in = 300_000 - D6.LADDER + D6.DEP
    out = {}
    for w in ws:
        sur, _, _ = D6.lock_early(req, rbd, eq_w=w, floor_share=floor_share)
        out[w] = float((sur < money_in).mean())
    ok = [w for w in ws if out[w] <= 0.05]
    return (max(ok) if ok else None), out


def check3():
    print("\n[3] D6 plain rule on a 5-point grid: most stock with P(2033 growth money < $157.7k) <= 5%")
    ws = [x / 100 for x in range(40, 81, 5)]
    for bd_label, bd in (("A bonds 4.00%", D6.BD), ("B bonds 5.00%", D6.BD_CONSISTENT)):
        req, rbd = D6.draws(D6.EQ, bd=bd)
        for fs in (0.8, 0.7):
            pick, out = plain_rule(req, rbd, fs, ws)
            print(f"    normal, {bd_label}, lock {fs:.1f}: pick {int(pick * 100)}%  [" +
                  ", ".join(f"{int(w * 100)}:{out[w] * 100:.1f}" for w in ws) + "]")
    eq_c = D6.lp(0.052, 0.052 + (0.0794 - 0.0670))      # D6 case C: Vanguard midpoint, JPM volatility kept
    req, rbd = D6.draws(eq_c, bd=D6.BD_CONSISTENT)
    pick, out = plain_rule(req, rbd, 0.8, ws)
    print(f"    normal, C Vanguard 5.2% + bonds 5.00%, lock 0.8: pick {int(pick * 100)}%  [" +
          ", ".join(f"{int(w * 100)}:{out[w] * 100:.1f}" for w in ws) + "]")
    # fat tails, same construction as D6.section_fat_tails
    rng = np.random.default_rng(D6.SEED)
    z1 = rng.standard_normal((D6.PATHS, 6))
    z2 = rng.standard_normal((D6.PATHS, 6))
    t = np.random.default_rng(D6.SEED + 7).standard_t(4, (D6.PATHS, 6)) / np.sqrt(4 / 2)
    for bd_label, bd in (("A bonds 4.00%", D6.BD), ("B bonds 5.00%", D6.BD_CONSISTENT)):
        req = np.exp(D6.EQ[0] + D6.EQ[1] * t) - 1
        rbd = np.exp(bd[0] + bd[1] * (D6.RHO * z1 + np.sqrt(1 - D6.RHO ** 2) * z2)) - 1
        pick, out = plain_rule(req, rbd, 0.8, ws)
        print(f"    fat-tail t4, {bd_label}, lock 0.8: pick {int(pick * 100)}%  [" +
              ", ".join(f"{int(w * 100)}:{out[w] * 100:.1f}" for w in ws) + "]")


def check3b():
    """Fee sensitivity of the plain rule (brief s14 blind spot: no management-fee assumption anywhere). The fee is taken
    off each year's sleeve return while the sleeve is invested (ASSUMPTION: 0.5% or 1.0% a year; ETF costs alone are
    0.03-0.15%, ticket s1)."""
    print("\n[3b] D6 plain rule with a yearly fee on the growth money (5-point grid, lock 0.8)")
    ws = [x / 100 for x in range(40, 81, 5)]
    money_in = 300_000 - D6.LADDER + D6.DEP
    for bd_label, bd in (("A bonds 4.00%", D6.BD), ("B bonds 5.00%", D6.BD_CONSISTENT)):
        req, rbd = D6.draws(D6.EQ, bd=bd)
        for fee in (0.0, 0.005, 0.010):
            out = {}
            for w in ws:
                sur, _, _ = D6.lock_early(req - fee, rbd - fee, eq_w=w)
                out[w] = float((sur < money_in).mean())
            ok = [w for w in ws if out[w] <= 0.05]
            print(f"    {bd_label}, fee {fee * 100:.1f}%: pick {int(max(ok) * 100)}%  [P at 50/60/70%:"
                  f" {out[0.5] * 100:.1f}/{out[0.6] * 100:.1f}/{out[0.7] * 100:.1f}]")


def check4():
    print("\n[4] Bought 2031 floor vs the 2031 two-year rate (floor = a x sleeve x (1+y)^2; D5/D6 use y = 4.81%)")
    base = (1.0481) ** 2
    for y in (0.03, 0.0481, 0.06):
        print(f"    y={y * 100:.2f}%: floor {((1 + y) ** 2 / base - 1) * 100:+.1f}% vs the model")


def check5():
    print("\n[5] WInS hedge vs the real promise")
    hedge = 0.66 * 300_000
    print(f"    option (ii) hedge ${hedge:,.0f} = {hedge / 292_264:.0%} of the $292,264 ladder;"
          f" = the ladder's share of both deposits ({292_264 / 450_000:.1%}) scaled to $300,000")
    print("    option (iii) hedge $294,000 (98%): here 'about $292k' is the WInS order size as well")


if __name__ == "__main__":
    check1()
    check2()
    check3()
    check3b()
    check4()
    check5()
