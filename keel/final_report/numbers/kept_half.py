"""How small the half kept "promised to no one" gets in the years shares fall (Keel, Mon 9 Nov 2026, evening). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/kept_half.py [--design KEEL]
Writes keel/final_report/numbers/results_kept_half_2026-11-10.json and prints the figures (the Mon 9 Nov
results_kept_half.json, on Keel's margin, is kept). Tue 10 Nov: the completion is the call in completion.py (H_plain);
the kept half plus the range rule's excess (card Q19, CANON D12) is added. Tue 10 Nov afternoon: the range rule is
completion.rule on the fund's own holdings (0.5% cut), and VT is what plan.run buys under Keel's reading of "most"
(the floor gets at least $75,001), not a fixed 26.7% of what is left.

Why: the IPS keeps half of VT for overruns, a stronger Taiwan dollar or "a co-sponsor falling short", and says
co-sponsors cut budgets when shares fall. The kept half is itself in VT, so it is likely to be smaller in exactly those
years (research/cards/Q9_what_makes_a_residency_last.md row 30). This measures by how much, on the register's own
engine, margin and paths (house: 200,000 paths, seed 2033; history: every Shiller window since 1871, as plan.py).
"Shares fell" = VT's value on 1 Jan 2033 below its value on 1 Jan 2031 (the two years from the co-sponsor meetings to
the gift), or below its 2028 cost (the five years since it was bought).
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402
import plan as P     # noqa: E402

c = E.Curve(E.load_par())
import completion as C   # noqa: E402
NAME = C.design_arg()
m3 = C.design(NAME)["margin"]
MF = C.margin_fn(NAME)


def summary(fin, vt3, vt2, sF=0.0, sM=0.0):
    kept = fin["kept33"]
    rr = C.rule(fin, sF, sM)
    kpe = kept + rr["excess"]
    top = fin["top"]
    vt_cost = fin["vt28"] + 0 * kept                                 # VT bought in Jan 2028, at cost (most rule)
    kept_at_cost = vt_cost / 2
    fell2 = vt2 < 1.0
    fell5 = vt3 * vt2 < 1.0
    deep2 = vt2 < 0.8
    q = lambda a, p: float(np.percentile(a, p)) if np.size(a) else None
    return {
        "kept_half_at_cost_2028": float(np.median(kept_at_cost)),
        "kept_p1_p5_p50_p95": [q(kept, 1), q(kept, 5), q(kept, 50), q(kept, 95)],
        "kept_as_share_of_top_p5_p50_p95": [q(kept / top, 5), q(kept / top, 50), q(kept / top, 95)],
        "share_paths_shares_fell_2031_2033": float(fell2.mean()),
        "kept_median_if_fell_2031_2033": q(kept[fell2], 50),
        "kept_p5_if_fell_2031_2033": q(kept[fell2], 5),
        "kept_median_if_rose_2031_2033": q(kept[~fell2], 50),
        "share_paths_fell_over_20pct_2031_2033": float(deep2.mean()),
        "kept_median_if_fell_over_20pct": q(kept[deep2], 50),
        "share_paths_vt_below_cost_2033": float(fell5.mean()),
        "kept_median_if_vt_below_cost_2033": q(kept[fell5], 50),
        "share_paths_kept_under_15k": float((kept < 15_000).mean()),
        "share_paths_kept_under_10k": float((kept < 10_000).mean()),
        "kept_plus_excess_p1_p5_p50_p95": [q(kpe, 1), q(kpe, 5), q(kpe, 50), q(kpe, 95)],
        "kept_plus_excess_median_if_fell_2031_2033": q(kpe[fell2], 50),
        "kept_plus_excess_median_if_rose_2031_2033": q(kpe[~fell2], 50),
        "kept_plus_excess_median_if_fell_over_20pct": q(kpe[deep2], 50),
        "kept_plus_excess_median_if_vt_below_cost_2033": q(kpe[fell5], 50),
        "share_paths_kept_plus_excess_under_15k": float((kpe < 15_000).mean()),
        "share_paths_kept_plus_excess_under_10k": float((kpe < 10_000).mean()),
        "excess_p5_p50_p95": [q(rr["excess"], 5), q(rr["excess"], 50), q(rr["excess"], 95)],
    }


# house paths, drawn exactly as plan.house draws them
import math
rng = np.random.default_rng(P.SEED)
sv = E.ASSUMPTIONS["yield_vol"]
d0 = rng.normal(0, sv * math.sqrt(E.yf(E.J27)), P.N)
d1 = rng.normal(0, sv, P.N)
d2 = rng.normal(0, sv * math.sqrt(3), P.N)
mu, sd = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"]
vt3 = np.exp(rng.normal(mu * 3, sd * math.sqrt(3), P.N))
vt2 = np.exp(rng.normal(mu * 2, sd * math.sqrt(2), P.N))
fin = P.run(c, m3, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
out = {"house": summary(fin, vt3, vt2, d0 + d1, d0 + d1 + d2)}

w = P.shiller_windows()
h3 = np.array([a for _, a, _ in w])
h2 = np.array([b for _, _, b in w])
fin_h = P.run(c, m3, None, 150_000.0, 0.0, 0.0, 0.0, h3, h2, MF)
out["history"] = summary(fin_h, h3, h2)
lo = int(np.argmin(fin_h["kept33"]))
out["history"]["kept_lowest"] = {"value": float(fin_h["kept33"][lo]), "start": w[lo][0]}
starts = {"1929-09": None, "1973-01": None, "2000-03": None, "2007-10": None, "2020-01": None}
ex_h = C.rule(fin_h)["excess"]
starts_x = {}
for i, (k, _, _) in enumerate(w):
    if k[:7] in starts:
        starts[k[:7]] = float(fin_h["kept33"][i])
        starts_x[k[:7]] = float(fin_h["kept33"][i] + ex_h[i])
out["history"]["kept_at_named_starts"] = starts
out["history"]["kept_plus_excess_at_named_starts"] = starts_x
out["history"]["kept_plus_excess_lowest"] = float(np.min(fin_h["kept33"] + ex_h))
cen = P.run(c, m3, margin_fn=MF)
out["central"] = {"kept33": float(cen["kept33"]), "vt_bought_jan2028": float(cen["vt28"]),
                  "kept_at_cost": float(cen["vt28"] / 2),
                  "excess": float(C.rule(cen)["excess"])}
out["stamp"] = {"curve": E.CURVE_DAY, "design": NAME, "margin_jan2027_value": m3, "run": C.RUN}
json.dump(out, open(HERE / f"results_kept_half_2026-11-10{C.tag(NAME)}.json", "w"), indent=1)
print(json.dumps(out, indent=1))
