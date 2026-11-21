"""What a building budget set on the stated bottom has behind it (numbers owner, Fri 20 Nov 2026 morning, Sydney).
MODEL and Keel arithmetic, not a forecast or a promise. NUMBERS 8u row 4 and 8q ("The same rises on the stated bottom");
bond desk 5, L5 (`research/panel/2026-11-18_bond_desk_5_3c_table3_3e.md`).

8u row 4 printed "30.2% on the bottom" beside its 24.9% on the top, and 8q shows its rises "on the stated bottom" as
"the lower reading". Both set the pot (her flexibility plus anything above the top, $28,682 centrally: the half kept
plus the excess) against the bottom, $95,000, as if the contribution were the bottom. It is not: the contribution
equals the stated top in every path and window (8q's check, asserted here), so a building budget set on the bottom has
the pot AND the gap between the two ends behind it. This script:
  (1) re-derives the lower reading, the pot over the bottom (30.2%, break_test.py's `rise_it_covers_on_the_bottom`), and
      8q's central bottom-table figures, and asserts them;
  (2) re-derives 8q's house-model shares "on the stated bottom" (the pot alone against the rise x each path's bottom)
      and asserts them equal to `results_taiwan_joint_2026-11-17.json`, so the relabel says what taiwan_joint.py
      computes;
  (3) gives the full reading: the pot plus (the contribution - the bottom) against the rise x the bottom, centrally
      ($48,682, 51.2% of $95,000: bond desk 5's figure, asserted) and in the house paths.
Nothing is re-sized and no register figure moves: the register's design (H_plain with the fee cushion and the payments'
0.5% margin), the range rule on the fund's holdings, Keel's reading of "most", the house model (200,000 paths, seed
2033), the 6 Nov 2026 curve, VT at 7.5% a year centrally.

Run from the repo root:  python3 -I keel/final_report/numbers/bottom_reading.py
Writes keel/final_report/numbers/results_bottom_reading_2026-11-20.json (about 10 seconds, numpy only). Imports
engine.py, plan.py and completion.py and changes none of them. Reads one results file, read only:
`results_taiwan_joint_2026-11-17.json`, for 8q's three rises (exact) and its house shares (to assert against). It does
not import taiwan_joint.py or break_test.py, because importing either re-runs it and rewrites its results file.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

c = C.c
NAME = C.CALL
MARGIN = C.design(NAME)["margin"]
MF = C.margin_fn(NAME)
OUT = HERE / "results_bottom_reading_2026-11-20.json"
TJ = json.loads((HERE / "results_taiwan_joint_2026-11-17.json").read_text())
STRESS = TJ["stresses"]                     # 8q: 10% (8j), +24.6%, +28.0%, +38.9%
f = lambda x: float(np.asarray(x).item())


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


# ---------------------------------------------------------------- central (today's forwards, VT 7.5% a year)
cen = P.run(c, margin=MARGIN, margin_fn=MF)
rc = C.rule(cen)
bot, top, gift = f(rc["bottom"]), f(rc["top"]), f(rc["gift"])
kept, excess = f(cen["kept33"]), f(rc["excess"])
pot = kept + excess
assert (bot, top, gift) == (95_000.0, 115_000.0, 115_000.0)          # the contribution is the top, not the bottom
near(kept, 21_179, 1, "8u/8q half kept")
near(excess, 7_503, 1, "8u/8q above the top")
near(pot, 28_682, 1, "8u/8q her flexibility plus anything above the top")
near(round(100 * pot / gift, 1), 24.9, 1e-9, "8u/8q 24.9% on the top")
near(round(100 * pot / bot, 1), 30.2, 1e-9, "8u's 30.2%: the pot over the bottom (break_test.py)")
full_pot = pot + gift - bot                                             # the pot plus the $20,000 between the two ends
near(gift - bot, 20_000, 1e-9, "the gap between the ends")
near(full_pot, 48_682, 1, "bond desk 5, L5: $48,682 behind a budget set on the bottom")
near(round(100 * full_pot / bot, 1), 51.2, 1e-9, "bond desk 5, L5: 51.2%")

central = {"stated_bottom": bot, "stated_top": top, "contribution": gift, "half_kept": kept, "above_the_top": excess,
           "pot_her_flexibility_plus_anything_above_the_top": pot,
           "pot_over_the_top_rise_covered": pot / gift,
           "lower_reading_pot_over_the_bottom": pot / bot,
           "gap_between_the_ends": gift - bot,
           "full_reading_behind_a_budget_set_on_the_bottom": full_pot,
           "full_reading_rise_covered_on_the_bottom": full_pot / bot,
           "half_kept_alone_full_reading_on_the_bottom": (kept + gift - bot) / bot,
           "rises": {}}
# 8q's central bottom table (Keel arithmetic on the register's central figures), reproduced; and the full reading
reg8q = {"joint_18m_1in20": (23_358, 5_324, -2_179), "joint_24m_1in20": (26_593, 2_090, -5_414),
         "joint_24m_worst_jul2006_jul2008": (36_972, -8_290, -15_793)}
for s, x in STRESS.items():
    need = x * bot
    row = {"rise": x, "need_on_the_bottom": need,
           "lower_reading_left_pot": pot - need, "lower_reading_left_half_kept_alone": kept - need,
           "full_reading_left_pot": full_pot - need, "full_reading_left_half_kept_alone": kept + gift - bot - need}
    if s in reg8q:
        n8, l8, k8 = reg8q[s]
        near(need, n8, 1, f"8q need on the bottom {s}")
        near(pot - need, l8, 1, f"8q left on the bottom {s}")
        near(kept - need, k8, 1, f"8q half kept alone on the bottom {s}")
    central["rises"][s] = row

# ---------------------------------------------------------------- house model (200,000 paths, seed 2033), as 8q
d0, d1, d2, vt3, vt2 = P.draws()
H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
Hr = C.rule(H, d0 + d1, d0 + d1 + d2)
hk = np.asarray(H["kept33"], float)
hg, he = np.asarray(Hr["gift"], float), np.asarray(Hr["excess"], float)
ht, hb = np.asarray(Hr["top"], float), np.asarray(Hr["bottom"], float)
assert float((np.abs(hg - ht) < 0.5).mean()) == 1.0                    # the contribution is the top in every path
hpot, hgap = hk + he, hg - hb
house = {"paths": int(hk.size),
         "gap_between_the_ends_p5_p50_p95": [float(np.percentile(hgap, p)) for p in (5, 50, 95)],
         "gap_between_the_ends_min_max": [float(hgap.min()), float(hgap.max())],
         "rises": {}}
assert hgap.min() >= 0
for s, x in STRESS.items():
    need = x * hb
    lo_pot, lo_kept = float((hpot - need >= 0).mean()), float((hk - need >= 0).mean())
    tj = TJ["fixed_stresses"]["house"][s]["stated_bottom"]
    near(lo_pot, tj["kept_half_plus_excess"]["covers"], 1e-12, f"8q house on the bottom, pot {s}")
    near(lo_kept, tj["kept_half"]["covers"], 1e-12, f"8q house on the bottom, half kept alone {s}")
    house["rises"][s] = {"rise": x,
                         "lower_reading_covers_pot": lo_pot, "lower_reading_covers_half_kept_alone": lo_kept,
                         "full_reading_covers_pot": float((hpot + hgap - need >= 0).mean()),
                         "full_reading_covers_half_kept_alone": float((hk + hgap - need >= 0).mean()),
                         "on_the_contribution_covers_pot":
                             TJ["fixed_stresses"]["house"][s]["contribution"]["kept_half_plus_excess"]["covers"]}
# 8q's rounded house shares on the bottom (lower reading), as printed
for s, (p8, k8) in {"joint_18m_1in20": (73.3, 36.6), "joint_24m_1in20": (57.7, 25.6),
                    "joint_24m_worst_jul2006_jul2008": (19.8, 7.1)}.items():
    near(round(100 * house["rises"][s]["lower_reading_covers_pot"], 1), p8, 1e-9, f"8q house pot {s}")
    near(round(100 * house["rises"][s]["lower_reading_covers_half_kept_alone"], 1), k8, 1e-9, f"8q house kept {s}")
ok = hb > 0
house["rise_covered_19_in_20_on_the_bottom"] = {
    "lower_reading_pot": float(np.percentile(hpot[ok] / hb[ok], 5)),
    "full_reading_pot": float(np.percentile((hpot[ok] + hgap[ok]) / hb[ok], 5)),
    "paths_with_a_bottom": int(ok.sum())}

out = {"run": "Fri 20 Nov 2026 morning (Sydney), numbers owner", "section": "NUMBERS 8u row 4 and 8q (the bottom's "
       "lower reading); bond desk 5, L5", "rule": C.RULE_VERSION, "design": NAME, "curve": E.CURVE_DAY,
       "note": "MODEL and Keel arithmetic. The lower reading sets the pot against the bottom as if the contribution "
               "were the bottom; the contribution equals the top in every path, so the full reading adds the gap "
               "between the ends. Neither is for prose: co-sponsors count the top.",
       "central": central, "house": house}
OUT.write_text(json.dumps(out, indent=1, default=float))

k = C.fmt
print(f"central: pot {k(pot)} (half kept {k(kept)} + above the top {k(excess)}); contribution {k(gift)} = the top")
print(f"  on the top {100 * pot / gift:.2f}%; lower reading, pot over the bottom {100 * pot / bot:.2f}%; full reading "
      f"{k(full_pot)} behind a budget set on {k(bot)}, {100 * full_pot / bot:.2f}%")
for s, r in central["rises"].items():
    print(f"  {s:32s} +{100 * r['rise']:.1f}% need {k(r['need_on_the_bottom'])}: lower left {k(r['lower_reading_left_pot'])}"
          f" (kept {k(r['lower_reading_left_half_kept_alone'])}); full left {k(r['full_reading_left_pot'])}"
          f" (kept {k(r['full_reading_left_half_kept_alone'])})")
g = house["gap_between_the_ends_p5_p50_p95"]
print(f"house: gap between the ends p5/p50/p95 {[k(v) for v in g]}, min/max {[k(v) for v in house['gap_between_the_ends_min_max']]}")
for s, r in house["rises"].items():
    print(f"  {s:32s} lower {100 * r['lower_reading_covers_pot']:.1f}% ({100 * r['lower_reading_covers_half_kept_alone']:.1f}%)"
          f"  full {100 * r['full_reading_covers_pot']:.1f}% ({100 * r['full_reading_covers_half_kept_alone']:.1f}%)"
          f"  on the contribution {100 * r['on_the_contribution_covers_pot']:.1f}%")
h19 = house["rise_covered_19_in_20_on_the_bottom"]
print(f"  covered 19 in 20 on the bottom: lower {100 * h19['lower_reading_pot']:.1f}%, full {100 * h19['full_reading_pot']:.1f}%")
print("wrote", OUT.name)
