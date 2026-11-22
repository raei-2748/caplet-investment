"""The whole Taiwan-dollar series, the 1986-88 rise, the "since 1991" labels, and the argument tree's figures that had
no register section (numbers owner, Sun 22 Nov 2026 evening, Sydney). Card Q217's open item in NUMBERS section 9, parts
1 to 4. Keel arithmetic on data read at source, plus 8q's three worlds re-used as they stand (MODEL); not a forecast.
NUMBERS 8x.

Run from the repo root:  python3 -I keel/final_report/numbers/twd_whole_series.py
   or from this folder:  python3 -I twd_whole_series.py
Writes keel/final_report/numbers/results_twd_whole_series_2026-11-22.json and prints the figures (about 15 seconds,
numpy only). It writes no other file and changes no script. For part C it runs taiwan_joint.py's own top-level code up
to its fixed-stress loop (every statement that assigns to that script's `out` dict skipped, so nothing is written, the
way taiwan_joint.py itself runs joint_stress.py), then calls that script's own `test` with one more rise. Every
register figure it starts from is asserted against its results file.

Parts:
  A  FRED EXTAUS read at source Sun 22 Nov 2026 (extaus_fred_read_2026-11-22.txt, 517 months, Oct 1983 to Oct 2026)
     against the repo mirror keel/models/data/twd_per_usd_monthly.csv (516 months to Sep 2026).
  B  Every two-year currency move on the whole series (8j's convention: NT$ per US$ at the start / at the end - 1, the %
     more US dollars a fixed NT$ bill needs), against 8j's own windows (moves from Oct 1986) and the windows since 1991.
  C  Card Q217 row 7: the largest two-year move (Jan 1986 to Jan 1988) on her $115,000, by 8q's method (need = the rise
     times the contribution; left = the pot less the need, at face; 8q's central pots), and in 8q's three worlds.
  D  Building costs in 1986-88: no national index (DGBAS's starts Jan 1991); Taipei City's index (from 1981, read at
     source today) gives a city-index joint figure, labelled as such.
  E  8q's joint series since 1991 (card Q131's 406 windows to Oct 2026): the largest joint rise, the highest strong-
     Taiwan-dollar window, the windows at 28% or more and their runs (card Q210's four episodes), the separate spans.
  F  The tree's figures with no register section (SECOND_WAY_2026-11-22.md): the WInS book x 1.5 against the plan in
     January 2028; the reserve's $502,605 at zero interest; the book's DV01; the 2000-2003 replay; writers' 2009 receipts.

Conventions and sources are in each part's comments and in NUMBERS 8x.
"""
import ast
import csv
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUN = "Sun 22 Nov 2026 evening (Sydney)"
OUTFILE = HERE / "results_twd_whole_series_2026-11-22.json"
FRED_TXT = HERE / "extaus_fred_read_2026-11-22.txt"
MIRROR = ROOT / "keel/models/data/twd_per_usd_monthly.csv"
TAIPEI = HERE / "taipei_cci_1981_1993_read_2026-11-22.csv"
TJ_SRC = HERE / "taiwan_joint.py"
TJ_RES = HERE / "results_taiwan_joint_2026-11-17.json"
JS_RES = HERE / "results_joint_stress_2026-11-17.json"
SW_RES = HERE / "results_strong_twd_windows_2026-11-18.json"
CARDS = HERE.parent / "research/cards/data"
H = 24
TOP, BOTTOM = 115_000.0, 95_000.0
OCT26_CCI = 120.50          # card Q103, read at source Tue 17 Nov (NUMBERS 8d), as strong_twd_windows.py


def add(m, k):
    y, mo = int(m[:4]), int(m[5:7])
    t = y * 12 + mo - 1 + k
    return f"{t // 12:04d}-{t % 12 + 1:02d}"


def runs(starts):
    """Group start months into runs of consecutive months."""
    out = []
    for s in starts:
        if out and add(out[-1][-1], 1) == s:
            out[-1].append(s)
        else:
            out.append([s])
    return out


out = {"stamp": {"run": RUN, "status": "Keel arithmetic on data read at source; part C's world shares are MODEL "
                                        "(8q's three worlds, unchanged)", "numbers_section": "8x",
                 "card": "research/cards/Q217_taiwan_dollar_1985_1992.md"}}

# ---------------------------------------------------------------- A. FRED read at source against the mirror
FRED = {}
for line in open(FRED_TXT, encoding="utf-8"):
    p = line.split()
    if len(p) == 2 and p[0][:2] in ("19", "20"):
        FRED[p[0][:7]] = float(p[1])
MIR = {r["Date"][:7]: float(r["TWD_per_USD"]) for r in csv.DictReader(open(MIRROR, encoding="utf-8"))}
assert len(FRED) == 517 and min(FRED) == "1983-10" and max(FRED) == "2026-10"
assert len(MIR) == 516 and max(MIR) == "2026-09"
mism = [m for m in MIR if abs(MIR[m] - FRED[m]) > 1e-9]
assert not mism, mism
assert FRED["2026-10"] == 32.2695                      # card Q131's FRED read of 17 Nov (preliminary then)
out["A_fred_against_mirror"] = {"fred_months": len(FRED), "mirror_months": len(MIR), "mismatches": len(mism),
                                "fred_last_updated": "2026-11-02 3:51 PM CST", "oct_2026": FRED["2026-10"]}

# ---------------------------------------------------------------- B. every two-year currency move
MONTHS = sorted(FRED)
W = [(FRED[a] / FRED[add(a, H)] - 1, a, add(a, H)) for a in MONTHS if add(a, H) in FRED]
assert len(W) == 493 and W[0][1] == "1983-10" and W[-1][1] == "2024-10"
mx = max(W)
assert (mx[1], mx[2]) == ("1986-01", "1988-01") and round(mx[0] * 100, 1) == 38.3, mx
X8689 = mx[0]
top5 = sorted(W, reverse=True)[:5]
# 8j's windows: VT bought Oct 1983 to Jun 2018, the move from month 36 to month 60, so moves start Oct 1986 to Jun 2021
W8j = [w for w in W if "1986-10" <= w[1] <= "2021-06"]
assert len(W8j) == 417
mx8j = max(W8j)
js = json.load(open(JS_RES, encoding="utf-8"))["twd_test"]["real_twd_with_same_months_shares"]
assert abs(mx8j[0] - js["twd_cost_change_max_and_start"][0]) < 1e-12 and add(mx8j[1], -36) == \
    js["twd_cost_change_max_and_start"][1] == "1983-11"          # 8j: +29.4%, VT bought Nov 1983
# since 1991: starts Jan 1991 to Oct 2024 (card Q131's 406 windows)
W91 = [w for w in W if w[1] >= "1991-01"]
assert len(W91) == 406
mx91 = max(W91)
assert (mx91[1], mx91[2]) == ("2009-02", "2011-02") and round(mx91[0] * 100, 1) == 16.9, mx91
strong91 = [w for w in W91 if w[0] >= 0.10]
assert len(strong91) == 30                            # 8q's Q131 block: 30 of the 406 since 1991
sw = json.load(open(SW_RES, encoding="utf-8"))
W80 = [w for w in W if w[1] <= "1990-12"]             # starts Oct 1983 to Dec 1990
hi_strong = 0.2903                                    # floor of the highest strong window since 1991 (29.03%), part E
peak, low = max(MONTHS[:120], key=lambda m: FRED[m]), min(MONTHS[:120], key=lambda m: FRED[m])
watch = next(m for m in MONTHS if m > "1985-08" and FRED["1985-08"] / FRED[m] - 1 >= 0.10)
out["B_currency_windows"] = {
    "windows_whole_series": len(W), "first_start": W[0][1], "last_start": W[-1][1],
    "largest": [X8689, mx[1], mx[2]], "largest_daily_q10b_not_rerun": "+39.7% Dec 1985 to Dec 1987 (card Q10b, H.10 daily)",
    "five_largest": [[w[0], w[1], w[2]] for w in top5],
    "largest_on_8j_windows": [mx8j[0], mx8j[1], mx8j[2]], "windows_8j": len(W8j),
    "largest_since_1991": [mx91[0], mx91[1], mx91[2]], "windows_since_1991": len(W91),
    "ratio_1986_88_to_largest_since_1991": X8689 / mx91[0],
    "strong_10pct_since_1991": len(strong91),
    "starts_oct1983_to_dec1990": {"windows": len(W80), "at_10pct_or_more": sum(w[0] >= 0.10 for w in W80),
                                  "at_20pct_or_more": sum(w[0] >= 0.20 for w in W80),
                                  "at_29pct_or_more": sum(w[0] >= hi_strong for w in W80),
                                  "note": "overlapping windows of one episode: never odds (card Q210)"},
    "peak_to_low_1983_1993": [peak, FRED[peak], low, FRED[low], FRED[peak] / FRED[low] - 1],
    "watch_10pct_from_aug1985_fires": [watch, FRED["1985-08"] / FRED[watch] - 1],
    "move_from_aug1985_after_2y_3y": [FRED["1985-08"] / FRED["1987-08"] - 1, FRED["1985-08"] / FRED["1988-08"] - 1],
}
assert (peak, low) == ("1985-08", "1992-06") and watch == "1986-10"

# ---------------------------------------------------------------- C. card Q217 row 7 by 8q's method
tj = json.load(open(TJ_RES, encoding="utf-8"))
COVER = tj["rise_covered_central"]["kept_half_plus_excess"]
COVER_KEPT = tj["rise_covered_central"]["kept_half"]
POT, KEPT = COVER * TOP, COVER_KEPT * TOP             # unrounded, as 8q's central column
assert (round(POT), round(KEPT), round(POT - KEPT)) == (28_682, 21_179, 7_503)
need = X8689 * TOP


def run_taiwan_joint_prefix():
    """taiwan_joint.py's top-level code up to its fixed-stress loop (`fixed = {}`), skipping every statement that assigns
    to its `out` dict; nothing is written. Returns that script's namespace (WORLDS, test, cen, cr, C, E, P, c, ...)."""
    tree = ast.parse(TJ_SRC.read_text(encoding="utf-8"))

    def touches_out(t):
        while isinstance(t, (ast.Subscript, ast.Attribute)):
            t = t.value
        return isinstance(t, ast.Name) and t.id == "out"

    body = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "fixed" for t in node.targets):
            break
        if isinstance(node, ast.Assign) and any(touches_out(t) for t in node.targets):
            continue
        body.append(node)
    ns = {"__name__": "taiwan_joint_prefix", "__file__": str(TJ_SRC)}
    argv, sys.argv = sys.argv, [str(TJ_SRC)]           # design CALL, as the register's run
    try:
        exec(compile(ast.Module(body=body, type_ignores=[]), str(TJ_SRC), "exec"), ns)
    finally:
        sys.argv = argv
    return ns


NS = run_taiwan_joint_prefix()
test = NS["test"]
worlds = {}
for w in ("house", "history", "joint"):
    # check: the +38.9% row reproduces 8q's results file exactly, then the new rise
    chk = test(w, NS["STRESS"]["joint_24m_worst_jul2006_jul2008"], "contribution")
    reg = tj["fixed_stresses"][w]["joint_24m_worst_jul2006_jul2008"]["contribution"]
    for pot in ("kept_half", "kept_half_plus_excess"):
        assert chk[pot]["covers"] == reg[pot]["covers"], (w, pot)
    r = test(w, X8689, "contribution")
    worlds[w] = {"covers_kept_half_plus_excess": r["kept_half_plus_excess"]["covers"],
                 "covers_kept_half": r["kept_half"]["covers"],
                 "gap_when_fails_p50_max": [r["kept_half_plus_excess"]["gap_when_fails_p50_p95_max"][0],
                                            r["kept_half_plus_excess"]["gap_when_fails_p50_p95_max"][2]],
                 "for_comparison_38_9pct_covers": reg["kept_half_plus_excess"]["covers"]}
cen = test("central", X8689, "contribution")
assert abs(cen["kept_half_plus_excess"]["left_min"] - (POT - need)) < 1.0
out["C_row7_1986_88_on_her_top"] = {
    "rise_currency_alone": X8689, "need_on_115000": need,
    "pot_half_kept_plus_excess": POT, "left_half_kept_plus_excess": POT - need,
    "pot_half_kept": KEPT, "left_half_kept": KEPT - need,
    "need_over_pot": need / POT,
    "on_95000_bottom_lower_reading": {"need": X8689 * BOTTOM, "left_pot_alone": POT - X8689 * BOTTOM,
                                      "left_with_20000_gap_between_ends": POT + 20_000 - X8689 * BOTTOM},
    "three_worlds_contribution": worlds,
    "method": "8q's central column and fixed-stress test (taiwan_joint.test), the rise = the currency alone",
}

# ---------------------------------------------------------------- D. building costs in 1986-88
TP = {}
rows = [r for r in csv.reader(l for l in open(TAIPEI, encoding="utf-8") if not l.startswith("#"))]
assert rows[0][0] == "year"
for r in rows[1:]:
    v = [float(x) for x in r[1:13]]
    assert abs(sum(v) / 12 - float(r[13])) <= 0.0125, r[0]       # the table's own yearly index
    for i, x in enumerate(v, 1):
        TP[f"{int(r[0]):04d}-{i:02d}"] = x
assert min(TP) == "1981-01" and max(TP) == "1993-12" and len(TP) == 156
UT = {m: TP[m] / FRED[m] for m in TP if m in FRED}
WT = [(UT[add(a, H)] / UT[a] - 1, a, add(a, H), TP[add(a, H)] / TP[a] - 1, FRED[a] / FRED[add(a, H)] - 1)
      for a in sorted(UT) if a <= "1990-12" and add(a, H) in UT]
assert len(WT) == 87
t8688 = next(w for w in WT if w[1] == "1986-01")
tmx = max(WT)
strongT = [w[0] for w in WT if w[4] >= 0.10]
out["D_building_costs_1986_88"] = {
    "national_index": "none before Jan 1991: DGBAS's 'Construction Cost Indices in Taiwan Area' compiled on trial from "
                      "Jan 1991, formally published Jul 1991 (DGBAS method note, read 22 Nov 2026); 8q's joint figure "
                      "cannot be computed for 1986-88",
    "other_series": "Taipei City's and Taiwan Province's construction cost indices (from 1981, local DBAS offices); the "
                    "wholesale price index's construction input prices (from 1975, materials only). Only Taipei's was read",
    "taipei_jan1986_jan1988": {"cost_ntd": t8688[3], "currency": t8688[4], "joint_usd": t8688[0],
                               "need_on_115000": t8688[0] * TOP, "left_half_kept_plus_excess": POT - t8688[0] * TOP},
    "taipei_largest_joint_starts_oct1983_dec1990": [tmx[0], tmx[1], tmx[2], tmx[3], tmx[4]],
    "taipei_strong_currency_windows": {"count": len(strongT), "median_joint": float(np.median(strongT))},
}
assert round(t8688[0] * 100, 1) == 48.1 and (tmx[1], tmx[2]) == ("1987-05", "1989-05") and round(tmx[0] * 100, 1) == 50.4

# ---------------------------------------------------------------- E. 8q's joint series since 1991
tree = ast.parse(TJ_SRC.read_text(encoding="utf-8"))
txt = [n.value.value for n in tree.body if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "CCI_TEXT"]
CCI = {}
for line in txt[0].strip().splitlines():
    p = [x.strip() for x in line.split("|")]
    for mo, v in enumerate(p[1:], 1):
        if v:
            CCI[f"{int(p[0]):04d}-{mo:02d}"] = float(v)
CCI["2026-10"] = OCT26_CCI
M91 = sorted(m for m in CCI if m in FRED)
assert M91[0] == "1991-01" and M91[-1] == "2026-10" and len(M91) == 430
J = [((CCI[add(a, H)] / CCI[a]) * (FRED[a] / FRED[add(a, H)]) - 1, a, add(a, H), FRED[a] / FRED[add(a, H)] - 1)
     for a in M91 if add(a, H) in CCI]
assert len(J) == 406
jmx = max(J)
assert (jmx[1], jmx[2]) == ("2006-07", "2008-07") and round(jmx[0] * 100, 1) == 38.9
jstrong = [w for w in J if w[3] >= 0.10]
assert len(jstrong) == 30
smx = max(jstrong)
assert abs(smx[0] - sw["strong_windows"]["usd_cost_max"]) < 1e-12 and round(smx[0] * 100, 1) == 29.0
above_smx = sum(w[0] > smx[0] for w in J)
J405 = [w for w in J if w[1] <= "2024-09"]            # 8q's own data, to Sep 2026
p95 = float(np.percentile([w[0] for w in J405], 95))
assert round(p95 * 100, 1) == 28.0
at28 = sorted(w[1] for w in J if w[0] >= 0.28)
runs28 = runs(at28)
above_p95_405 = sum(w[0] > p95 for w in J405)
spans = sorted({(len(M91) - 1 - k) // H for k in range(H)})
out["E_joint_since_1991"] = {
    "windows": len(J), "first_start": J[0][1], "last_start": J[-1][1],
    "largest_joint": [jmx[0], jmx[1], jmx[2]],
    "highest_strong_twd_window": [smx[0], smx[1], smx[2]], "windows_with_a_larger_joint_rise": above_smx,
    "rank_of_29pct_among_406": above_smx + 1,
    "p95_on_8q_405": p95, "windows_above_p95_on_405": above_p95_405,
    "windows_at_28pct_or_more": len(at28), "runs_of_start_months": [[r[0], r[-1], len(r)] for r in runs28],
    "separate_two_year_spans": spans,
    "currency_1986_88_against_largest_joint": {"currency_1986_88": X8689, "largest_joint_since_1991": jmx[0],
                                               "points_below": (jmx[0] - X8689) * 100,
                                               "need_1986_88": need, "need_2006_08": jmx[0] * TOP},
}

# ---------------------------------------------------------------- F. the tree's figures with no register section
C, E, P, c = NS["C"], NS["E"], NS["P"], NS["c"]
cenp, Y = NS["cen"], E.YEARS
# F1. the WInS book at cost (8g) x 1.5 against the plan in January 2028 at cost (section 4); NUMBERS_ANSWERS attack 3
book = {"IBTM": 97_489.95, "IBTO": 23_408.64, "IBTP": 22_155.30, "IBTQ": 20_973.24, "IBTR": 19_823.72,
        "Feb37": 19_203.80, "May38": 18_615.26, "Nov39": 16_200.95, "Nov40": 15_790.32, "Nov41": 14_991.00,
        "VT": 26_524.61, "cash": 3_513.79, "costs": 1_309.42}
assert abs(sum(book.values()) - 300_000) < 0.005
fl = 3361 * 21.65                                     # 3,361 IBTM shares as the floor stand-in (section 0, 8m)
lad = sum(v for k, v in book.items() if k not in ("VT", "cash", "costs")) - fl
assert abs(lad - 195_886.53) < 0.005
complete, fm, vt, R = (float(cenp[k]) for k in ("complete", "floor_money", "vt28", "R"))
assert (round(complete), round(fm), round(vt), round(R)) == (39_162, 81_244, 29_594, 110_838)
plan_pay = 300_000 + complete
out["F1_book_x15"] = {
    "book_at_cost": {"payment_treasuries": lad, "floor_standin": fl, "vt": book["VT"],
                     "cash_and_costs": book["cash"] + book["costs"]},
    "book_x15": {"payment_treasuries": 1.5 * lad, "floor": 1.5 * fl, "vt": 1.5 * book["VT"],
                 "cash_and_costs": 1.5 * (book["cash"] + book["costs"])},
    "plan_jan2028_at_cost": {"payment_treasuries": plan_pay, "floor": fm, "vt": vt},
    "plan_pct_of_450000": [plan_pay / 4500, fm / 4500, vt / 4500],
    "book_pct_of_300000": [lad / 3000, fl / 3000, book["VT"] / 3000],
    "floor_share_of_what_is_left": {"book": fl / (fl + book["VT"]), "plan": fm / R},
    "basis": "money put in: the book's at 6-7 Oct ET fills; the plan's $300,000 in Jan 2027 plus Jan 2028's $39,162",
}
# F2. the reserve at zero interest (8a, 8h, section 2); NUMBERS_ANSWERS attack 28
zo = C.own_amounts(C.PLAIN, C.ZERO)
zp = C.pool_buckets(C.BACKSTOP, C.ZERO)
left0 = C.ledger(C.ZERO, C.PLAIN, C.BACKSTOP)[3]
leftfee = C.ledger(C.Flat(c, -C.WAIT_FEE), C.PLAIN, C.BACKSTOP)[3]
assert (round(sum(zo.values())), round(sum(zp.values())), round(left0)) == (445_405, 57_200, 2_604)
assert round(leftfee) == 1_177
out["F2_reserve_at_zero"] = {"own_rungs_pay": sum(zo.values()), "extra_treasuries_pay": sum(zp.values()),
                             "total_no_fee": sum(zo.values()) + sum(zp.values()), "owed": 500_000.0,
                             "left_no_fee": left0, "left_with_bill_fee": leftfee}
# F3. DV01 on the 6 Nov curve, 1 Jan 2027 value per 1 bp parallel move of the par curve, fixed flows; attack 12
reg17 = json.load(open(HERE / "results_2026-11-17.json", encoding="utf-8"))
I = C.I
fills = {2038: 20, 2039: 20, 2040: 18, 2041: 18, 2042: 20}       # WInS face in $1,000s (8g, 8m)


def value(units, curve):
    return sum(u * a * curve.P(d) for y, u in units.items() for d, a, _ in E.rung_flows(I[y], C.BASE))


up, dn = E.Curve(c.par, shift=0.0001), E.Curve(c.par, shift=-0.0001)
dv = lambda u: (value(u, dn) - value(u, up)) / 2
liab = (E.ladder_cost(dn) - E.ladder_cost(up)) / 2
assert abs(liab - reg17["C3"]["dv01_per_bp"]) < 0.01
plain_dv = dv(C.PLAIN)
assert abs(plain_dv - 234) < 0.5
book_units = {y: (fills[y] * 1000 / C.PLAIN[y] if y in fills else 0.6765) * C.PLAIN[y] for y in Y}
fl_units = 3361 / 1142 * book_units[2033]
out["F3_dv01"] = {"payments_full": liab, "payments_scaled_two_thirds": liab * 2 / 3, "plan_ten_plain": plain_dv,
                  "plan_ten_plus_extra": dv(C.add(C.PLAIN, C.BACKSTOP)), "wins_book_ten_rungs": dv(book_units),
                  "wins_book_floor_standin": dv({2033: fl_units}),
                  "book_over_scaled_payments": dv(book_units) / (liab * 2 / 3),
                  "approximation": "funds at card Q17's 67.6-67.7% of a full rung (23 Oct curve), each fund's payout "
                                   "as one amount on 15 Dec; the second-way bootstrap gets about $155"}
# F4. the 2000-2003 replay (card Q85 checkpoints; card Q131's monthly file for the building)
pr = {r["period"]: float(r["msci_acwi_price_usd_level"])
      for r in csv.DictReader(open(CARDS / "Q85_msci_acwi_price_usd_checkpoints.csv", encoding="utf-8"))}
gr = {r["period"]: float(r["msci_acwi_gross_usd_level"])
      for r in csv.DictReader(open(CARDS / "Q85_msci_acwi_gross_usd_checkpoints.csv", encoding="utf-8"))}
sh_start = pr["2000-12"] / pr["1999-12"] * gr["2002-12"] / gr["2000-12"] - 1   # Dec 1999 close to Dec 2002 close
sh_end = pr["2000-12"] / pr["2000-01"] * gr["2003-01"] / gr["2000-12"] - 1     # Jan 2000 close to Jan 2003 close
q131 = {r["month"]: r for r in csv.DictReader(open(CARDS / "Q131_cci_parts_ntd_monthly.csv", encoding="utf-8"))}
cost_ntd = float(q131["2004-12"]["cci_total"]) / float(q131["2003-01"]["cci_total"]) - 1
cost_usd = (1 + cost_ntd) * float(q131["2003-01"]["twd_per_usd"]) / float(q131["2004-12"]["twd_per_usd"]) - 1
assert round(sh_start * 100, 1) == -42.1 and round(sh_end * 100, 1) == -40.6
assert round(cost_ntd * 100, 1) == 18.4 and round(cost_usd * 100, 1) == 27.2
assert abs(CCI["2003-01"] - float(q131["2003-01"]["cci_total"])) < 1e-9          # 8q's series = card Q131's file
out["F4_replay_2000_2003"] = {"world_shares_jan2000_to_jan2003_start_of_month": sh_start,
                              "world_shares_end_of_month": sh_end,
                              "building_ntd_jan2003_to_dec2004": cost_ntd, "building_usd_jan2003_to_dec2004": cost_usd}
# F6. writers' 2009 receipts (card Q148 row 5: Census Nonemployer Statistics, NAICS 7115, legal form S)
q148 = [r for r in csv.reader(l for l in open(CARDS / "Q148_official_series.csv", encoding="utf-8")
                              if not l.startswith("#"))]
sp = {int(r[1]): float(r[2]) for r in q148 if r and r[0] == "census_nonemployer_7115_sole_prop_receipts"}
w09 = sp[2009] / sp[2008] - 1
assert round(w09 * 100, 1) == -7.8
out["F6_writers_2009"] = {"receipts_2008_usd_thousand": sp[2008], "receipts_2009_usd_thousand": sp[2009],
                          "change": w09}

json.dump(out, open(OUTFILE, "w", encoding="utf-8"), indent=1, default=float)
pct = lambda x: f"{x * 100:+.2f}%"
k = lambda x: f"${x:,.0f}"
b, cc, d, e = out["B_currency_windows"], out["C_row7_1986_88_on_her_top"], out["D_building_costs_1986_88"], \
    out["E_joint_since_1991"]
print("A  FRED read 22 Nov: 517 months, mirror 516 months, mismatches", len(mism))
print("B  largest two-year move", pct(X8689), mx[1], "to", mx[2], "| on 8j's windows", pct(mx8j[0]), mx8j[1], "to",
      mx8j[2], "| since 1991", pct(mx91[0]), mx91[1], "to", mx91[2], "| ratio", f"{X8689 / mx91[0]:.2f}")
print("   five largest:", [(round(w[0] * 100, 2), w[1]) for w in top5])
print("   starts Oct 1983-Dec 1990:", b["starts_oct1983_to_dec1990"])
print("   peak to low", b["peak_to_low_1983_1993"], "| 10% watch from Aug 1985 fires", b["watch_10pct_from_aug1985_fires"],
      "| after 2y, 3y", [round(x * 100, 2) for x in b["move_from_aug1985_after_2y_3y"]])
print("C  need on $115,000", k(need), "| left with the excess", k(POT - need), "| half kept alone", k(KEPT - need),
      "| need / pot", f"{need / POT:.3f}")
print("   three worlds (covers with the excess / half kept alone):",
      {w: (round(v["covers_kept_half_plus_excess"] * 100, 2), round(v["covers_kept_half"] * 100, 2)) for w, v in
       worlds.items()})
print("   lower reading on $95,000:", {kk: round(vv) for kk, vv in cc["on_95000_bottom_lower_reading"].items()})
print("D  Taipei Jan 1986-Jan 1988: cost", pct(t8688[3]), "currency", pct(t8688[4]), "joint", pct(t8688[0]), "need",
      k(t8688[0] * TOP), "left", k(POT - t8688[0] * TOP), "| largest", pct(tmx[0]), tmx[1], tmx[2], "| strong:",
      d["taipei_strong_currency_windows"])
print("E  largest joint since 1991", pct(jmx[0]), jmx[1], jmx[2], "| highest strong window", pct(smx[0]), smx[1],
      "| windows with a larger joint rise", above_smx, "| p95 (405)", pct(p95), "above it", above_p95_405,
      "| at 28%+", len(at28), "runs", e["runs_of_start_months"], "| spans", spans)
print("F1", {kk: (round(vv) if isinstance(vv, float) else vv) for kk, vv in out["F1_book_x15"]["book_x15"].items()},
      "plan", {kk: round(vv) for kk, vv in out["F1_book_x15"]["plan_jan2028_at_cost"].items()},
      "shares", out["F1_book_x15"]["floor_share_of_what_is_left"])
print("F2", {kk: round(vv) for kk, vv in out["F2_reserve_at_zero"].items()})
print("F3", {kk: (round(vv, 1) if isinstance(vv, float) else vv[:30]) for kk, vv in out["F3_dv01"].items()})
print("F4", {kk: round(vv * 100, 2) for kk, vv in out["F4_replay_2000_2003"].items()})
print("F6", out["F6_writers_2009"])
print("All asserts passed.")
