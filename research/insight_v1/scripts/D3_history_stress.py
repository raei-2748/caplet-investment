"""D3_history_stress.py - M059: check the plan (and the barbell / ratchet / partial-lock alternatives) against real
historical return sequences, not only the i.i.d. lognormal model.

What it computes:
 1. Crash-year frequency: model vs history (how often a stock year is -30% or worse).
 2. Named episodes placed at the worst time for Laura, with every other year at JPM's median return:
    (a) during 2028-2030 (before the 2031 floor is bought), (b) during 2031-2032 (after it is bought).
    Output: the bought 2031 floor and the 2033 facility money, against the model's p5 and median.
 3. Every historical 6-year window 1928-2025 run through 2027-2032 (93 windows), raw and rescaled so each asset's
    average (log) return equals JPM's median: plan, ratchet, barbell 50%, and 90%/70% partial payment locks.
Inputs and status: Damodaran histretSP (VERIFIED-PRIMARY dataset page, accessed 2026-09-28; snapshot
data/D3/damodaran_histretSP_1928_2025.csv): S&P 500 incl. dividends (equity); sleeve bonds = 50% 3-month T-bill +
50% 10-year Treasury bond (ASSUMPTION proxy for intermediate Treasuries). Model: strategy_mc_v2.py (VERIFIED-REPO-FILE
JPM rows; ASSUMPTION lognormal). Named episodes use calendar-year returns (a crash that spans two calendar years is
split across them).
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_history_stress.py
"""
import sys

import numpy as np

sys.path.insert(0, "research/insight_v1/scripts")
from D3_range_rules import load_hist, rescale  # noqa: E402
from strategy_mc_v2 import Cfg, draws, returns, simulate  # noqa: E402

EQ_MED, BD_MED = 0.067, 0.040          # JPM compound (median) returns used for the "other" years
EPISODES = {"1929-31 Depression": (1929, 3), "1973-74 oil shock": (1973, 2), "2000-02 dot-com": (2000, 3),
            "2008 crisis": (2008, 1), "2022 stocks+bonds": (2022, 1)}


def run_path(cfg, eq, bd, strategy="L", f=1.0):
    r = simulate(cfg, strategy, lock_frac=f, ret=(np.atleast_2d(eq), np.atleast_2d(bd)))
    return r


def main():
    yrs, heq, hbd = load_hist()
    req, _ = returns(Cfg(), draws(Cfg()))
    reqt, _ = returns(Cfg(tails="t", t_nu=4.0, t_scale=1.09), draws(Cfg(tails="t", t_nu=4.0, t_scale=1.09)))
    print("== 1. How often is a stock year -30% or worse?")
    print(f"  model (JPM, lognormal) {np.mean(req <= -0.30) * 100:.2f}% of years; fat-tailed t4 {np.mean(reqt <= -0.30) * 100:.2f}%;"
          f" S&P 500 1928-2025 {np.mean(heq <= -0.30) * 100:.1f}% ({', '.join(str(y) for y in yrs[heq <= -0.30])}); "
          f"-20% or worse: model {np.mean(req <= -0.20) * 100:.1f}%, history {np.mean(heq <= -0.20) * 100:.1f}%")

    base = simulate(Cfg())
    m5, m50 = np.percentile(base["surplus"], 5), np.median(base["surplus"])
    f5, f50 = np.percentile(base["floor33"], 5), np.median(base["floor33"])
    print(f"\n== 2. Named episodes (plan: 60/40 sleeve, 80% floor bought 1 Jan 2031). Model: floor p5 ${f5 / 1000:.0f}k, "
          f"median ${f50 / 1000:.0f}k; 2033 facility money p5 ${m5 / 1000:.0f}k, median ${m50 / 1000:.0f}k")
    print("  episode | placed | years used | 2031 floor | 2033 facility money | vs model median | payments")
    for name, (start, n) in EPISODES.items():
        i = int(np.where(yrs == start)[0][0])
        for lab, first in (("2028-30 (before lock)", 1), ("2031-32 (after lock)", 4)):
            k = min(n, 6 - first) if first == 4 else min(n, 3)
            eq = np.full(6, EQ_MED)
            bd = np.full(6, BD_MED)
            eq[first:first + k] = heq[i:i + k]
            bd[first:first + k] = hbd[i:i + k]
            r = run_path(Cfg(), eq, bd)
            used = f"{start}-{start + k - 1}" if k > 1 else f"{start}"
            print(f"  {name:20s} | {lab:21s} | {used:9s} | ${r['floor33'][0] / 1000:.0f}k | ${r['surplus'][0] / 1000:.0f}k | "
                  f"{(r['surplus'][0] / m50 - 1) * 100:+.0f}% | all ten bought in 2027")

    print("\n== 3. Every historical 6-year window 1928-2025 placed in 2027-2032")
    designs = [("plan (80% lock 2031)", Cfg(), "L", 1.0),
               ("ratchet (thirds 2029-31)", Cfg(floor_design="ratchet"), "L", 1.0),
               ("barbell 50% (Jan 2028)", Cfg(floor_design="barbell", barbell_share=0.5), "L", 1.0),
               ("90% payment lock, no floor", Cfg(floor_design="none"), "P", 0.9),
               ("70% payment lock, no floor", Cfg(floor_design="none"), "P", 0.7)]
    for lab, eq, bd in (("raw history", heq, hbd), ("rescaled to JPM medians", rescale(heq, EQ_MED), rescale(hbd, BD_MED))):
        n = len(eq) - 5
        R = np.array([eq[i:i + 6] for i in range(n)])
        B = np.array([bd[i:i + 6] for i in range(n)])
        print(f"  -- {lab} ({n} windows)")
        for name, cfg, strat, f in designs:
            r = simulate(cfg, strat, lock_frac=f, ret=(R, B))
            s = r["surplus"]
            w = s.argmin()
            extra = f"; payments short in {np.sum(s < 0)} windows" if strat == "P" else ""
            print(f"     {name:28s} | worst ${s.min() / 1000:.0f}k (start {yrs[w]}), p10 ${np.percentile(s, 10) / 1000:.0f}k, "
                  f"median ${np.median(s) / 1000:.0f}k{extra}")
    mod = simulate(Cfg())["surplus"]
    print(f"  model for comparison (plan): p1 ${np.percentile(mod, 1) / 1000:.0f}k, p10 ${np.percentile(mod, 10) / 1000:.0f}k, "
          f"median ${np.median(mod) / 1000:.0f}k")


if __name__ == "__main__":
    main()
