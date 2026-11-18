"""Strong-Taiwan-dollar two-year windows: what a fixed NT$ building budget cost in US dollars (numbers owner, Wed 18 Nov
2026 evening, Sydney). Keel arithmetic on data read at source; not a model of the plan and not a forecast. NUMBERS 8q,
block "Added Wed 18 Nov evening (card Q131)".

Run from the repo root:  python3 -I keel/final_report/numbers/strong_twd_windows.py
   or from this folder:  python3 -I strong_twd_windows.py
Writes keel/final_report/numbers/results_strong_twd_windows_2026-11-18.json and prints the figures (under a second,
numpy only). Imports no register module and runs no model: it reads card Q10e's index as copied into taiwan_joint.py
(parsed with ast, never executed), the FRED EXTAUS mirror, card Q131's monthly file (as a cross-check only) and
results_taiwan_joint_2026-11-17.json (8q's central pots and its 1-in-20 rise). It writes no other file.

The claim re-derived (card Q131, research/cards/Q131_taiwan_materials_labour_and_the_nt_dollar.md, rows 14, 15 and 40,
verdict part 3 and "What the plan takes"): in the 30 two-year windows since 1991 with the Taiwan dollar 10% or more
stronger, the US-dollar cost of a fixed NT$ building budget rose a median 22.3% (range 9.3% to 29.0%), beating the
currency move in 25 of 30; on the $115,000 top that is about $25,600 (median) and $33,400 (worst).

Definitions (card Q131's conventions, which are NUMBERS 8j's and 8q's):
  * a window is 24 months from one month's average to the same month two years later; start months Jan 1991 to Oct
    2024 (406 windows on data to Oct 2026; 405 on 8q's data to Sep 2026);
  * the NT$ move over a window = NT$ per US$ at the start / NT$ per US$ at the end - 1: the % more US dollars a fixed
    NT$ bill needs at the end; positive = a stronger Taiwan dollar; "strong" = 10% or more (8j's test size);
  * the US-dollar cost rise = (index at the end / index at the start) x (NT$ per US$ at the start / at the end) - 1,
    which is 8q's joint move U[end] / U[start] - 1 with U = index / NT$ per US$ (taiwan_joint.joint_move);
  * "beat the currency move" = US-dollar cost rise > NT$ move, i.e. the index in NT$ rose over the window;
  * an episode = a run of consecutive start months (card Q131's grouping); a period = episodes whose windows overlap
    (start months less than 24 apart), so periods share no month.
Dollar sizes follow 8q: the need is the rise times the figure (the $115,000 top, or the $95,000 bottom), "left" is the
pot less the need, at face; the pots are 8q's central ones read from results_taiwan_joint_2026-11-17.json (the half
kept $21,179 and the half kept plus the excess $28,682; WORDS: "her flexibility plus anything above the top").

Data:
  * DGBAS construction cost index (total, 2021 = 100), Jan 1991 to Sep 2026: card Q10e's read of 15 Nov 2026
    (ccispl.xls / cciidx.xls), the CCI_TEXT block of taiwan_joint.py, parsed here without running that script;
    October 2026 = 120.50, read at source Tue 17 Nov (card Q103, DGBAS ccispl.xls; NUMBERS 8d).
  * NT$ per US$: keel/models/data/twd_per_usd_monthly.csv, the FRED EXTAUS mirror verified for all 516 months (8l),
    Oct 1983 to Sep 2026; October 2026 = 32.2695, card Q131's read at FRED on 17 Nov 2026 (preliminary).
  * Cross-check: card Q131's own file (research/cards/data/Q131_cci_parts_ntd_monthly.csv, DGBAS database read of 17 Nov
    US date, funid A030502015) must agree with both series in every month, Jan 1991 to Oct 2026 (asserted).
"""
import ast
import csv
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUN = "Wed 18 Nov 2026 evening (Sydney)"
OUTFILE = HERE / "results_strong_twd_windows_2026-11-18.json"
TWD = ROOT / "keel/models/data/twd_per_usd_monthly.csv"
CARD_CSV = HERE.parent / "research/cards/data/Q131_cci_parts_ntd_monthly.csv"
TJ_SRC = HERE / "taiwan_joint.py"
TJ_RES = HERE / "results_taiwan_joint_2026-11-17.json"

H = 24                     # months in a window
STRONG = 0.10              # 10% or more stronger NT$ (8j's test)
OCT26_CCI = 120.50         # card Q103, read at source Tue 17 Nov (NUMBERS 8d)
OCT26_FX = 32.2695         # card Q131, FRED EXTAUS read 17 Nov 2026 (preliminary)
TOP, BOTTOM = 115_000.0, 95_000.0


# ---------------------------------------------------------------- 0. data
def cci_from_taiwan_joint():
    """Card Q10e's index as copied into taiwan_joint.py (CCI_TEXT), parsed with ast; the script is not run."""
    tree = ast.parse(TJ_SRC.read_text(encoding="utf-8"))
    txt = [n.value.value for n in tree.body
           if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "CCI_TEXT"]
    assert len(txt) == 1
    out = {}
    for line in txt[0].strip().splitlines():
        p = [x.strip() for x in line.split("|")]
        for m, v in enumerate(p[1:], 1):
            if v:
                out[f"{int(p[0]):04d}-{m:02d}"] = float(v)
    return out


CCI = cci_from_taiwan_joint()
FX = {r["Date"][:7]: float(r["TWD_per_USD"]) for r in csv.DictReader(open(TWD, encoding="utf-8"))}
assert min(CCI) == "1991-01" and max(CCI) == "2026-09" and len(CCI) == 429
assert max(FX) == "2026-09" and len(FX) == 516
CCI["2026-10"] = OCT26_CCI
FX["2026-10"] = OCT26_FX
MONTHS = sorted(k for k in CCI if k in FX)
assert MONTHS[0] == "1991-01" and MONTHS[-1] == "2026-10" and len(MONTHS) == 430

# cross-check every month against card Q131's own file
card = list(csv.DictReader(open(CARD_CSV, encoding="utf-8")))
assert [r["month"] for r in card] == MONTHS
cci_diff = max(abs(float(r["cci_total"]) - CCI[r["month"]]) for r in card)
fx_diff = max(abs(float(r["twd_per_usd"]) - FX[r["month"]]) for r in card)
assert cci_diff < 1e-9 and fx_diff < 1e-9, (cci_diff, fx_diff)

C = np.array([CCI[m] for m in MONTHS])
F = np.array([FX[m] for m in MONTHS])
N = len(MONTHS) - H                                  # 406 windows, starts Jan 1991 to Oct 2024
NTD = F[:N] / F[H:] - 1                              # >0 = NT$ stronger (8j)
USD = (C[H:] / C[:N]) * (F[:N] / F[H:]) - 1          # 8q's joint move
IDX = C[H:] / C[:N] - 1                              # the index in NT$
assert N == 406 and MONTHS[N - 1] == "2024-10"

# 8q's register figures, read from its results file (never re-computed by a model here)
tj = json.load(open(TJ_RES, encoding="utf-8"))
reg = tj["checks"]["register"]
assert (reg["central_kept"], reg["central_excess"]) == ([21_179, 21_179], [7_503, 7_503])   # engine = register
assert reg["central_contribution"] == [TOP, TOP]
COVER = tj["rise_covered_central"]["kept_half_plus_excess"]   # 24.9% (the engine's unrounded pots over the top)
COVER_KEPT = tj["rise_covered_central"]["kept_half"]          # 18.4%
P95 = tj["joint_series"]["24m"]["p95_1in20"]                  # 28.0% (405 windows to Sep 2026)
assert round(COVER * 100, 1) == 24.9 and round(COVER_KEPT * 100, 1) == 18.4 and round(P95 * 100, 1) == 28.0
POT, KEPT = COVER * TOP, COVER_KEPT * TOP            # unrounded, as 8q's central column uses them
EXCESS = POT - KEPT
assert (round(POT), round(KEPT), round(EXCESS)) == (28_682, 21_179, 7_503)   # 8q: $28,682 = $21,179 + $7,503
# 8q's three worlds, read (not run): the rise each covers 19 times in 20, and its +24.6% row (18-month 1-in-20)
COV19 = {w: tj["rise_covered_19_in_20"][w]["kept_half_plus_excess"] for w in ("house", "history", "joint")}
assert [round(COV19[w] * 100, 1) for w in ("house", "history", "joint")] == [15.8, 18.0, 17.6]
ROW246 = {w: tj["fixed_stresses"][w]["joint_18m_1in20"]["contribution"]["kept_half_plus_excess"]["covers"]
          for w in ("house", "history", "joint")}
assert [round(ROW246[w] * 100, 1) for w in ("house", "history", "joint")] == [51.0, 64.9, 65.3]
assert round(tj["joint_series"]["18m"]["p95_1in20"] * 100, 1) == 24.6
NEED_P95 = TOP * P95
assert round(NEED_P95) == 32_191 and round(NEED_P95 - POT) == 3_509          # 8q's $32,191 need, $3,509 short

# this series reproduces 8q's own 1-in-20 on 8q's data (405 windows, to Sep 2026)
p95_405 = float(np.percentile(USD[:N - 1], 95))
assert abs(p95_405 - P95) < 1e-12, (p95_405, P95)
p95_406 = float(np.percentile(USD, 95))

# ---------------------------------------------------------------- 1. the strong-NT$ windows
S = NTD >= STRONG
idx = np.flatnonzero(S)
u = USD[S]
med, lo, hi = float(np.median(u)), float(u.min()), float(u.max())
i_lo, i_hi = int(idx[np.argmin(u)]), int(idx[np.argmax(u)])
beat = int((USD[S] > NTD[S]).sum())
idx_rose = int((IDX[S] > 0).sum())
# the same set on 8q's data to Sep 2026 (the Oct 2024 window is the only one that needs October 2026)
S405 = NTD[:N - 1] >= STRONG
assert (S405 == S[:N - 1]).all() and not S[N - 1]

assert int(S.sum()) == 30 and round(float(S.mean()) * 100, 1) == 7.4
assert round(p95_406 * 100, 1) == 28.0                                   # October 2026 leaves 8q's 28.0% as it is
assert round(med * 100, 1) == 22.3 and round(lo * 100, 1) == 9.3 and round(hi * 100, 1) == 29.0
second = int(idx[np.argsort(u)[-2]])                                      # the near-tie for the worst window
assert (MONTHS[second], MONTHS[second + H]) == ("2019-08", "2021-08") and round(float(USD[second]) * 100, 2) == 29.03
assert beat == 25 and idx_rose == 25
assert (MONTHS[i_lo], MONTHS[i_lo + H]) == ("1998-09", "2000-09")
assert (MONTHS[i_hi], MONTHS[i_hi + H]) == ("2003-03", "2005-03")
# the next-strongest NT$ moves below the line, and the closest window above it
below = np.sort(NTD[~S])[::-1]
closest_above = float(NTD[S].min())
assert MONTHS[int(idx[np.argmin(NTD[S])])] == "2019-01" and round(closest_above * 100, 2) == 10.00
assert round(float(below[0]) * 100, 2) == 9.95
other_med = float(np.median(USD[~S]))
assert round(other_med * 100, 1) == 2.0
ntd_med, idx_med = float(np.median(NTD[S])), float(np.median(IDX[S]))     # the currency itself; the index in NT$
assert round(ntd_med * 100, 1) == 11.7 and round(idx_med * 100, 1) == 7.2  # card Q131 row 14: total +7.2%
assert round(med / ntd_med, 1) == 1.9
fell = sorted(float(IDX[t]) for t in idx if IDX[t] <= 0)
assert len(fell) == 5 and round(fell[0] * 100, 1) == -1.6 and round(fell[-1] * 100, 1) == -0.7

# episodes (runs of consecutive starts) and periods (no shared month)
eps, cur = [], [int(idx[0])]
for t in idx[1:]:
    t = int(t)
    if t - cur[-1] > 1:
        eps.append(cur)
        cur = []
    cur.append(t)
eps.append(cur)
periods, curp = [], [eps[0]]
for e in eps[1:]:
    if e[0] - curp[-1][-1] < H:
        curp.append(e)
    else:
        periods.append(curp)
        curp = [e]
periods.append(curp)
assert len(eps) == 7 and len(periods) == 5


def block(ts):
    v = USD[ts]
    return {"starts": [MONTHS[ts[0]], MONTHS[ts[-1]]], "windows": len(ts), "usd_cost_median": float(np.median(v)),
            "usd_cost_min": float(v.min()), "usd_cost_max": float(v.max()),
            "ntd_move_max": float(NTD[ts].max()), "index_in_ntd_median": float(np.median(IDX[ts]))}


EPIS = [block(e) for e in eps]
PERS = [block([t for e in p for t in e]) for p in periods]
per_meds = sorted(p["usd_cost_median"] for p in PERS)
med_of_periods = float(np.median(per_meds))
assert [p["windows"] for p in PERS] == [5, 5, 9, 4, 7]
assert round(med_of_periods * 100, 1) == 22.3
assert max(int(e[-1]) for e in eps) == MONTHS.index("2019-09")        # last strong window ends Sep 2021

# against 8q's central cover and its 1-in-20
n_above_cover = int((u > COVER).sum())
n_above_p95 = int((u > P95).sum())
n_above_kept = int((u > COVER_KEPT).sum())
assert (n_above_cover, n_above_p95, n_above_kept) == (10, 7, 21)
per_above_cover = sum(1 for p in PERS if p["usd_cost_max"] > COVER)
assert per_above_cover == 2                                             # 2003-05 and 2019-21
# the 1-in-20 tail of all 405 windows (8q's data): how many are strong-NT$ windows
tail = USD[:N - 1] > P95
n_tail, n_tail_strong = int(tail.sum()), int((tail & S[:N - 1]).sum())
assert (n_tail, n_tail_strong) == (21, 7)
tail_other = [t for t in range(N - 1) if tail[t] and not S[t]]
tail_other_ntd = [float(NTD[t]) for t in tail_other]
assert round(min(tail_other_ntd) * 100, 1) == 2.2 and round(max(tail_other_ntd) * 100, 1) == 8.6
assert sorted({MONTHS[t][:4] for t in tail_other}) == ["1991", "2002", "2003", "2006"]
# per period: how many windows pass the central cover; period medians
above_by_period = [int((USD[[t for e in p for t in e]] > COVER).sum()) for p in periods]
assert above_by_period == [0, 5, 0, 0, 5]
assert [round(p["usd_cost_median"] * 100, 1) for p in PERS] == [9.9, 28.5, 22.3, 18.6, 27.0]
assert round(PERS[2]["usd_cost_max"] * 100, 1) == 24.6

# January starts only (Laura's calendar)
jan = [int(t) for t in idx if MONTHS[int(t)].endswith("-01")]
ujan = USD[jan]
assert [MONTHS[t] for t in jan] == ["1998-01", "2009-01", "2016-01", "2019-01"]
assert (ujan < COVER).all()

# threshold sensitivity: 9% to 11%
sens = {}
for th in (0.09, 0.095, 0.105, 0.11):
    ss = NTD >= th
    sens[f"{th:.3f}"] = {"windows": int(ss.sum()), "median": float(np.median(USD[ss])),
                         "min": float(USD[ss].min()), "max": float(USD[ss].max())}
assert sens["0.090"]["windows"] == 39 and round(sens["0.090"]["median"] * 100, 1) == 21.2
assert sens["0.110"]["windows"] == 20 and round(sens["0.110"]["median"] * 100, 1) == 22.4
assert [(sens[k]["windows"], round(sens[k]["median"] * 100, 1)) for k in ("0.095", "0.105")] == [(32, 22.4), (24, 22.4)]
assert all(9.0 <= round(v["min"] * 100, 1) <= 9.3 and round(v["max"] * 100, 1) == 29.0 for v in sens.values())
assert [round(float(x) * 100, 1) for x in ujan] == [9.7, 19.3, 19.5, 18.8]
assert sorted(MONTHS[t] for t in idx if IDX[t] <= 0) == ["1998-01", "1998-06", "1998-07", "1998-08", "1998-09"]
above_p95_years = sorted(MONTHS[int(t)][:4] for t in idx if USD[t] > P95)
assert above_p95_years == ["2003"] * 4 + ["2019"] * 3

# the one strong-NT$ 12-month window since 2022 (card Q131 row 22): Jul 2024 to Jul 2025
a, b = MONTHS.index("2024-07"), MONTHS.index("2025-07")
ntd12, usd12 = F[a] / F[b] - 1, (C[b] / C[a]) * (F[a] / F[b]) - 1
assert round(ntd12 * 100, 1) == 11.3 and round(usd12 * 100, 1) == 11.1
since22 = [MONTHS[t] for t in range(MONTHS.index("2022-01"), len(MONTHS) - 12) if F[t] / F[t + 12] - 1 >= STRONG]
assert since22 == ["2024-07"]


assert all(COV19[w] < med < tj["joint_series"]["18m"]["p95_1in20"] for w in COV19)   # the median sits between them

# ---------------------------------------------------------------- 2. dollars (Keel arithmetic on 8q's central pots)
def dollars(x):
    return {"rise": float(x), "need_top": TOP * x, "left_top_flex_plus_excess": POT - TOP * x,
            "left_top_half_kept": KEPT - TOP * x, "need_bottom": BOTTOM * x,
            "left_bottom_flex_plus_excess": POT - BOTTOM * x, "left_bottom_half_kept": KEPT - BOTTOM * x}


D = {"median": dollars(med), "lowest": dollars(lo), "highest": dollars(hi), "8q_1in20": dollars(P95)}
assert round(D["median"]["need_top"]) == 25_607 and round(D["median"]["left_top_flex_plus_excess"]) == 3_075
assert round(D["median"]["left_top_half_kept"]) == -4_428
assert round(D["highest"]["need_top"]) == 33_386 and round(D["highest"]["left_top_flex_plus_excess"]) == -4_704
assert round(D["highest"]["left_top_half_kept"]) == -12_207
assert round(D["lowest"]["need_top"]) == 10_701 and round(D["lowest"]["left_top_flex_plus_excess"]) == 17_981
assert round(D["median"]["need_bottom"]) == 21_154 and round(D["median"]["left_bottom_flex_plus_excess"]) == 7_528
assert round(D["highest"]["need_bottom"]) == 27_580 and round(D["highest"]["left_bottom_flex_plus_excess"]) == 1_102
# card Q131 row 40's "about $25,600" and "about $33,400", to the nearest $100
assert round(D["median"]["need_top"], -2) == 25_600 and round(D["highest"]["need_top"], -2) == 33_400
# the worst strong window against 8q's 1-in-20 row: $1,195 more need
assert round(D["highest"]["need_top"] - NEED_P95) == 1_195
assert round(D["median"]["left_bottom_half_kept"]) == 25                  # on the bottom the half kept alone just covers it
assert round(D["8q_1in20"]["left_bottom_flex_plus_excess"]) == 2_090      # 8q's bottom row, reproduced
assert round(D["8q_1in20"]["left_top_half_kept"]) == -11_012 and round(D["8q_1in20"]["need_bottom"]) == 26_593
assert round(D["lowest"]["left_top_half_kept"]) == 10_478
assert round(D["lowest"]["need_bottom"]) == 8_840 and round(D["lowest"]["left_bottom_flex_plus_excess"]) == 19_842

# ---------------------------------------------------------------- 3. out
out = {
    "stamp": {"run": RUN, "status": "Keel arithmetic on data read at source (not MODEL, not a forecast)",
              "card": "research/cards/Q131_taiwan_materials_labour_and_the_nt_dollar.md (rows 14, 15, 40)",
              "numbers_section": "8q, block 'Added Wed 18 Nov evening (card Q131)'",
              "cci": "card Q10e's read (taiwan_joint.py CCI_TEXT, parsed) Jan 1991-Sep 2026 + Oct 2026 120.50 (card Q103)",
              "twd": "keel/models/data/twd_per_usd_monthly.csv (FRED EXTAUS mirror, VERIFIED 8l) + Oct 2026 32.2695 "
                     "(card Q131, FRED read 17 Nov 2026, preliminary)",
              "pots": "results_taiwan_joint_2026-11-17.json checks.register (central_kept, central_excess)"},
    "checks": {"months": len(MONTHS), "card_q131_csv_max_abs_diff": {"cci_total": cci_diff, "twd_per_usd": fx_diff},
               "p95_1in20_405_windows_reproduces_8q": p95_405, "p95_1in20_406_windows_with_oct2026": p95_406,
               "same_30_windows_on_8q_data_to_sep2026": True},
    "definition": {"window_months": H, "starts": [MONTHS[0], MONTHS[N - 1]], "windows": N, "strong_ntd_at_least": STRONG,
                   "ntd_move": "fx_start / fx_end - 1", "usd_cost_rise": "(cci_end / cci_start) * (fx_start / fx_end) - 1"},
    "strong_windows": {
        "count": int(S.sum()), "share_of_windows": float(S.mean()),
        "usd_cost_median": med, "usd_cost_min": lo, "usd_cost_min_window": [MONTHS[i_lo], MONTHS[i_lo + H]],
        "usd_cost_max": hi, "usd_cost_max_window": [MONTHS[i_hi], MONTHS[i_hi + H]],
        "beat_the_currency_move": beat, "index_in_ntd_rose": idx_rose,
        "closest_window_above_the_line": {"start": "2019-01", "ntd_move": closest_above},
        "next_ntd_moves_below_the_line": [float(x) for x in below[:3]],
        "other_windows_usd_cost_median": other_med,
        "ntd_move_median": ntd_med, "index_in_ntd_median": idx_med, "median_usd_over_median_ntd": med / ntd_med,
        "index_fell_in_ntd": fell,
        "above_8q_central_cover_24_9": n_above_cover, "above_8q_1in20_28_0": n_above_p95,
        "above_half_kept_alone_cover_18_4": n_above_kept,
        "periods_with_a_window_above_central_cover": per_above_cover,
        "of_405_windows_above_8q_1in20": {"windows": n_tail, "of_which_strong_ntd": n_tail_strong,
                                           "others_ntd_move_range": [min(tail_other_ntd), max(tail_other_ntd)],
                                           "others_starts": [MONTHS[t] for t in tail_other]},
        "above_central_cover_by_period": above_by_period,
        "windows": [{"start": MONTHS[int(t)], "end": MONTHS[int(t) + H], "ntd_move": float(NTD[t]),
                     "usd_cost_rise": float(USD[t]), "index_in_ntd": float(IDX[t])} for t in idx],
        "episodes": EPIS, "periods": PERS, "median_of_period_medians": med_of_periods,
        "january_starts": {"starts": [MONTHS[t] for t in jan], "usd_cost": [float(x) for x in ujan]},
        "threshold_sensitivity": sens,
        "strong_12m_windows_since_2022": {"starts": since22, "ntd_move": float(ntd12), "usd_cost_rise": float(usd12)}},
    "keel_arithmetic_on_8q_central_pots": {"pots": {"half_kept": KEPT, "excess": EXCESS, "half_kept_plus_excess": POT},
                                           "cover_central": COVER, "cover_half_kept_alone": COVER_KEPT,
                                           "8q_1in20_rise": P95, "8q_rise_covered_19_in_20": COV19,
                                           "8q_24_6pct_row_covers": ROW246, **D},
}
json.dump(out, open(OUTFILE, "w"), indent=1, default=float)


def pct(x, d=1):
    return f"{x * 100:+.{d}f}%"


def m(x):
    return f"${x:,.0f}" if x >= 0 else f"-${-x:,.0f}"


print(f"data: {len(MONTHS)} months {MONTHS[0]}..{MONTHS[-1]}; card Q131 file agrees in every month "
      f"(max diff index {cci_diff}, NT$ {fx_diff})")
print(f"8q's 1-in-20 on 405 windows {pct(p95_405, 4)} (8q {pct(P95, 4)}); with Oct 2026, 406 windows {pct(p95_406, 4)}")
print(f"strong NT$ (>= 10%): {int(S.sum())} of {N} windows ({S.mean() * 100:.1f}%), {len(eps)} episodes, {len(periods)} periods")
print(f"  US$ cost rise: median {pct(med, 3)}, min {pct(lo, 3)} ({MONTHS[i_lo]}->{MONTHS[i_lo + H]}), "
      f"max {pct(hi, 3)} ({MONTHS[i_hi]}->{MONTHS[i_hi + H]}); beat the currency in {beat} of 30; other windows median {pct(other_med)}")
print(f"  median NT$ move {pct(ntd_med, 2)}, median index in NT$ {pct(idx_med)}, ratio {med / ntd_med:.2f}; "
      f"index fell in {len(fell)} ({pct(fell[0])} to {pct(fell[-1])})")
print(f"  closest above the line {MONTHS[int(idx[np.argmin(NTD[S])])]} {pct(closest_above, 3)}; next below "
      + ", ".join(pct(x, 2) for x in below[:3]))
for p in PERS:
    print(f"  period {p['starts'][0]}..{p['starts'][1]}: {p['windows']} windows, US$ cost median {pct(p['usd_cost_median'])} "
          f"[{pct(p['usd_cost_min'])}, {pct(p['usd_cost_max'])}], NT$ up to {pct(p['ntd_move_max'])}")
print(f"  median of the five period medians {pct(med_of_periods)}")
print(f"  above 8q's central cover {pct(COVER)}: {n_above_cover} of 30 (periods {per_above_cover} of 5); above 8q's 1-in-20 "
      f"{pct(P95)}: {n_above_p95}; above the half kept alone's {pct(COVER_KEPT)}: {n_above_kept}")
print(f"  of the {n_tail} windows above 8q's 1-in-20 (405), {n_tail_strong} are strong-NT$ windows")
print(f"  January starts: " + ", ".join(f"{MONTHS[t]} {pct(USD[t])}" for t in jan))
for k, v in sens.items():
    print(f"  threshold {float(k) * 100:.1f}%: {v['windows']} windows, median {pct(v['median'])}, [{pct(v['min'])}, {pct(v['max'])}]")
print(f"  strong 12-month windows since 2022: {since22}, NT$ {pct(ntd12)}, US$ cost {pct(usd12)}")
for k in ("median", "lowest", "highest", "8q_1in20"):
    d = D[k]
    print(f"{k:9s} {pct(d['rise'], 2)}: top need {m(d['need_top'])}, left {m(d['left_top_flex_plus_excess'])} "
          f"(half kept alone {m(d['left_top_half_kept'])}); bottom need {m(d['need_bottom'])}, left "
          f"{m(d['left_bottom_flex_plus_excess'])} (half kept alone {m(d['left_bottom_half_kept'])})")
print(f"all asserts pass; wrote {OUTFILE.name}")
