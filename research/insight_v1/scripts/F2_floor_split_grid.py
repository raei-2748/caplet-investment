"""F2 - floor size x split grid for the Root-and-Branch design (requested 2026-09-30: "what ratio should we take").

How to run (repo root, no network):  .venv/bin/python research/insight_v1/scripts/F2_floor_split_grid.py

Same engine, seed, paths and inputs as E4/F1 (E4.rival_design). Two choices vary:
  F = floor bought 1 Jan 2028 that repays F just before 2033 (150k = REC default = the 2028 deposit), and
  s = share of the stock fund that goes to the facility (REC default 1/2); Laura keeps 1 - s. Cap rule unchanged.
The ten payments are bought in 2027 in every cell, so no cell changes whether the payments are funded.

Proposed decision rules (written before the split results were seen; F1 floor results were already known):
  R1 lower the floor only if median gift rises >= $5k AND gift p5 falls by <= $5k vs REC (JPM central case)
  R2 guaranteed floor >= $125k (the committed money co-sponsors count; seed-money / lead-gift evidence)
  R3 Laura's kept money: p5 >= $12.5k (3 months of a $50k budget, NORI minimum) and median <= $100k (2-year max)
  R4 2031 range width (median top / floor) <= 1.30x, so the range stays informative (Du et al. 2011)
Every number is a MODEL PROPERTY under E4's stated assumptions, never a forecast.
"""
import importlib.util, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("E4", os.path.join(HERE, "E4_rival_numbers.py"))
E4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(E4)
D6, k = E4.D6, E4.k
G = E4.LEFT * (1 + E4.Y1) + D6.DEP
FLOORS = [150_000, 125_000, 100_000]
SPLITS = [0.4, 0.5, 0.6, 0.75]


def a_for(F):
    return F / (1 + E4.Y5) ** 5 / G


def grid(label, req):
    base = E4.rival_design(req, a=a_for(150_000), s=0.5)
    b50, b5 = np.median(base["gift"]), np.percentile(base["gift"], 5)
    print(f"\n== {label}")
    print("floor | s    | gift p5 / p50 / p95      | kept p5 / p50  | width | vs REC gift p50 / p5 | R1 R2 R3 R4")
    for F in FLOORS:
        for s in SPLITS:
            d = E4.rival_design(req, a=a_for(F), s=s)
            g, kp = d["gift"], d["kept"]
            w = np.median(d["top"]) / d["bottom"][0]
            dm, d5 = np.median(g) - b50, np.percentile(g, 5) - b5
            r1 = "ok" if F == 150_000 or (dm >= 5_000 and d5 >= -5_000) else "--"
            r2 = "ok" if F >= 125_000 else "--"
            r3 = "ok" if np.percentile(kp, 5) >= 12_500 and np.median(kp) <= 100_000 else "--"
            r4 = "ok" if w <= 1.30 else "--"
            print(f"{F // 1000:4d}k | {s:.2f} | {k(np.percentile(g,5))} / {k(np.median(g))} / {k(np.percentile(g,95))} "
                  f"| {k(np.percentile(kp,5))} / {k(np.median(kp))} | {w:.2f}x | {k(dm):>6s} / {k(d5):>6s}      "
                  f"| {r1} {r2} {r3} {r4}")


req, _ = D6.draws(E4.JPM_ACWI, bd=D6.BD_CONSISTENT)
grid("JPM 2026 LTCMA (ACWI 7.00%, bonds 5.00%), 200,000 paths", req)
vg = D6.lp(0.0508, 0.0508 + (0.0828 - 0.0700))
grid("Vanguard-like house (5.08% compound, JPM vol; ASSUMPTION hybrid)", D6.draws(vg, bd=D6.BD_CONSISTENT)[0])

yrs, heq, _ = E4.load_hist()
R = np.array([eq for eq in [E4.rescale(heq, 0.07)[i:i + 6] for i in range(len(heq) - 5)]])
print(f"\n== History, every 6-year window 1928-2025 rescaled to 7.00% ({len(R)} windows): gift worst / median, kept worst / median")
for F in FLOORS:
    for s in SPLITS:
        d = E4.rival_design(R, a=a_for(F), s=s)
        print(f"{F // 1000:4d}k | {s:.2f} | gift {k(d['gift'].min())} / {k(np.median(d['gift']))} "
              f"| kept {k(d['kept'].min())} / {k(np.median(d['kept']))}")
