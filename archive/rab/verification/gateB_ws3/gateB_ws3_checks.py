"""Gate B, WS3 (M5 history, M6 rivals, M7 stress): reference build vs blind rebuild, key by key and row by row.

AI-generated verification code (Claude Code, WS3 Gate B reconciler) for Team Caplet; no deliverable text.

Reference build: rab/models/m5_backtest.py, m6_rivals.py, m7_stress.py -> rab/results/M5, M6, M7 (+ ws3_numbers.py ->
rab/results/WS3_numbers_proposed.yaml). Blind build: rab/verification/blind/*.py -> rab/verification/blind/out/.
Tolerances: the gate's (RUN_PLAN s3: dollar outcomes and range ends +-2%, probabilities +-2pp) and, stricter, each spec's
own (M5/M7 deterministic: per-window $1, summaries $100, shares 0.5pp; M6 MC: percentiles 2%, probabilities 2pp,
switch-rule decisions identical).

Run from the worktree root (about 5 s; add --rerun to first re-run both builds in a temporary copy and check that the
committed outputs reproduce byte for byte, about 30 s more):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws3/gateB_ws3_checks.py [--rerun]
Writes rab/verification/gateB_ws3/gateB_ws3_results.json, gateB_ws3_table.csv, gateB_ws3_table.md.
The large-sample check of the fund rule's threshold is a separate script (gateB_ws3_mc_precision.py); its stored output
is read here if present.
"""
import argparse
import filecmp
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd
import yaml

WT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HERE = os.path.dirname(os.path.abspath(__file__))
PR = os.path.join(WT, "rab", "results")
BL = os.path.join(WT, "rab", "verification", "blind", "out")
PY = "/Users/ray/Research/rab-ws/.venv/bin/python"
N_MC = 200_000

ROWS = []          # the key table
DETAIL = {}        # per-row comparisons


def jload(p):
    with open(p) as f:
        return json.load(f)


P5, P6, P7 = (jload(os.path.join(PR, m, f"{m}_results.json")) for m in ("M5", "M6", "M7"))
BH = jload(os.path.join(BL, "blind_headlines.json"))["headlines"]
PROP = yaml.safe_load(open(os.path.join(PR, "WS3_numbers_proposed.yaml")))["numbers"]
NUM = yaml.safe_load(open(os.path.join(WT, "rab", "numbers.yaml")))
NUMS = NUM.get("numbers", NUM)


def b(k):
    if k not in BH:
        raise KeyError(f"blind key missing: {k}")
    return BH[k]


def psum(rid):
    return next(r for r in P6["summary"] if r["rival"] == rid)


# --------------------------------------------------------------------------------------------------- verdict logic
def se_diff(p1, p2, n=N_MC):
    """Standard error of the difference of two independent MC proportions."""
    return math.sqrt(max(p1 * (1 - p1), 1e-12) / n + max(p2 * (1 - p2), 1e-12) / n)


def add(section, key, pv, bv, kind, decision=False, note="", spec_tol=None, cause=""):
    """kind: usd_det (spec $1), usd_sum (spec $100), share_det (0.5pp), prob_mc, pct_mc, bp, exact, bool, text, ratio."""
    row = dict(section=section, key=key, decision=decision, primary=pv, blind=bv, kind=kind, note=note)
    if kind in ("exact", "bool", "text"):
        same = pv == bv
        row.update(diff="same" if same else "differs", verdict="MATCH" if same else (cause and "WITHIN TOL") or "UNRECONCILED")
    else:
        pv_, bv_ = float(pv), float(bv)
        d = bv_ - pv_
        row["diff_num"] = d
        if kind in ("usd_det", "usd_sum"):
            tol = spec_tol if spec_tol is not None else (1.0 if kind == "usd_det" else 100.0)
            rel = abs(d) / max(abs(pv_), 1.0)
            row["diff"] = f"{d:+,.2f} ({rel:+.3%})" if abs(d) < 1000 else f"{d:+,.0f} ({rel:+.2%})"
            row["verdict"] = "MATCH" if abs(d) <= tol else ("WITHIN TOL" if rel <= 0.02 else "UNRECONCILED")
        elif kind == "share_det":
            row["diff"] = f"{d * 100:+.2f}pp"
            row["verdict"] = "MATCH" if abs(d) <= 0.005 else ("WITHIN TOL" if abs(d) <= 0.02 else "UNRECONCILED")
        elif kind == "prob_mc":
            s = se_diff(pv_, bv_)
            row["diff"] = f"{d * 100:+.3f}pp ({abs(d) / s:.1f} SE)"
            row["verdict"] = ("MATCH" if d == 0 else "MC NOISE" if abs(d) <= 3 * s else
                              "WITHIN TOL" if abs(d) <= 0.02 else "UNRECONCILED")
        elif kind == "pct_mc":
            rel = abs(d) / max(abs(pv_), 1.0)
            row["diff"] = f"{d:+,.0f} ({d / max(abs(pv_), 1.0):+.2%})"
            row["verdict"] = "MATCH" if abs(d) <= 1 else ("MC NOISE" if rel <= 0.02 else "UNRECONCILED")
        elif kind == "bp":
            row["diff"] = f"{d:+.4f}bp"
            row["verdict"] = "MATCH" if abs(d) <= 0.05 else ("WITHIN TOL" if abs(d) <= 1 else "UNRECONCILED")
        elif kind == "ratio_mc":
            row["diff"] = f"{d:+.4f}"
            row["verdict"] = "MC NOISE" if abs(d) <= 0.005 else "UNRECONCILED"
        elif kind == "count_mc":
            row["diff"] = f"{d:+.0f}"
            row["verdict"] = "MATCH" if d == 0 else "MC NOISE"
        else:
            raise ValueError(kind)
    if cause:
        row["note"] = (row["note"] + "; " if row["note"] else "") + cause
    ROWS.append(row)
    return row


# --------------------------------------------------------------------------------------------------- row-level
def frame_compare(name, p, bdf, keys, colmap, tol=1.0, bools=()):
    m = p.merge(bdf, on=keys, how="outer", suffixes=("_p", "_b"), indicator=True)
    only_p, only_b = int((m._merge == "left_only").sum()), int((m._merge == "right_only").sum())
    m = m[m._merge == "both"]
    cols = {}
    worst = 0.0
    for pc, bc in colmap.items():
        a = pd.to_numeric(m[pc + "_p" if pc + "_p" in m else pc], errors="coerce")
        c = pd.to_numeric(m[bc + "_b" if bc + "_b" in m else bc], errors="coerce")
        both_nan = a.isna() & c.isna()
        dd = (a - c).abs()[~both_nan]
        nan_mismatch = int((a.isna() ^ c.isna()).sum())
        mx = float(dd.max()) if len(dd) else 0.0
        cols[pc] = dict(blind_col=bc, max_abs_diff=round(mx, 4), nan_mismatch=nan_mismatch)
        worst = max(worst, mx if not math.isnan(mx) else 0.0)
    for pc, bc in bools:
        a = m[pc + "_p" if pc + "_p" in m else pc].astype(str).str.lower()
        c = m[bc + "_b" if bc + "_b" in m else bc].astype(str).str.lower()
        cols[pc] = dict(blind_col=bc, mismatches=int((a != c).sum()))
    ok = worst <= tol and only_p == 0 and only_b == 0 and all(v.get("nan_mismatch", 0) == 0 and v.get("mismatches", 0) == 0
                                                              for v in cols.values())
    DETAIL[name] = dict(rows_joined=int(len(m)), only_primary=only_p, only_blind=only_b, tolerance=tol,
                        max_abs_diff=round(worst, 4), columns=cols, verdict="MATCH" if ok else "CHECK")
    return DETAIL[name]


def row_level():
    # ---- M5 part A series
    p = pd.read_csv(os.path.join(PR, "M5", "cost_of_certainty_series.csv"))
    q = pd.read_csv(os.path.join(BL, "M5", "cost_of_certainty_series.csv"))
    frame_compare("M5 cost-of-certainty series (every curve date 1871-2026)", p[["date", "V0", "basis"]], q, ["date", "basis"],
                  {"V0": "V0"}, tol=0.011)
    p = pd.read_csv(os.path.join(PR, "M5", "cost_of_certainty_by_year.csv"))
    q = pd.read_csv(os.path.join(BL, "M5", "cost_of_certainty_by_year.csv"))
    frame_compare("M5 cost by calendar year (min / median / max)", p, q, ["year", "basis"],
                  {"V0_min": "min", "V0_median": "median", "V0_max": "max"}, tol=0.51)
    # ---- M5 part B per window
    p = pd.read_csv(os.path.join(PR, "M5", "backtest_by_start_year.csv")).rename(columns={"fund": "fund_series"})
    q = pd.read_csv(os.path.join(BL, "M5", "backtest_by_start_year.csv"))
    cmap = {"C": "ladder_cost_C", "L": "leftover_L", "T": "topup_T", "G": "growth_money_G", "S": "short_S",
            "F": "floor_face_F", "fund0": "fund0", "fund31": "fund31", "fund33": "fund33", "bottom": "bottom",
            "top": "top", "gift": "gift", "kept": "kept", "T33": "T33", "real_gift": "real_gift", "real_T33": "real_T33",
            "ips_F": "ips_variant_F", "ips_gift": "ips_variant_gift"}
    frame_compare("M5 backtest, every (view, fund, start year): 6 x 149 windows", p, q, ["view", "fund_series", "Y"], cmap,
                  tol=0.011, bools=[("top_reached", "top_reached"), ("basis_Y", "basis_Y"), ("basis_Y1", "basis_Y1")])
    # ---- M6 history lens per window
    p = pd.read_csv(os.path.join(PR, "M6", "rivals_history.csv"))
    p["rival"] = p.rival.replace({"R5": "R5_m3", "R5m5": "R5_m5"})
    q = pd.read_csv(os.path.join(BL, "M6", "rivals_history.csv"))
    pn = p[p.rival != "R6"].copy()
    q = q.copy()
    q["promise_missed"] = np.where(q.promised_150k_met.isna(), np.nan, (q.promised_150k_met.astype(str) == "False").astype(float))
    pn["promise_missed"] = np.where(pn.floor_broken.isna(), np.nan, (pn.floor_broken.astype(str) == "True").astype(float))
    frame_compare("M6 history lens, every (rival, start year): 8 rivals x 149", pn, q, ["Y", "rival"],
                  {"T33": "T33", "certain31": "certain31", "gift": "gift", "shortfall": "shortfall", "top": "top",
                   "real_T33": "real_T33", "promise_missed": "promise_missed"}, tol=0.011, bools=[("unfunded", "unfunded")])
    pt = p[p.rival == "R6"][["Y", "shortfall", "tips_paid_total", "tips_min_payment", "unfunded"]]
    qt = pd.read_csv(os.path.join(BL, "M6", "tips_history_delivery.csv"))
    qt["min_paid"] = qt[[f"paid_{k}" for k in range(1, 11)]].min(axis=1)
    qt["any_short"] = qt.n_short > 0
    frame_compare("M6 TIPS ladder, every inflation path 1872-2011 (140)", pt, qt, ["Y"],
                  {"shortfall": "total_gap", "tips_paid_total": "total_paid", "tips_min_payment": "min_paid"}, tol=0.011,
                  bools=[("unfunded", "any_short")])
    # ---- M6 fund alternatives, deterministic lenses
    p = pd.read_csv(os.path.join(PR, "M6", "fund_alternatives.csv"))
    q = pd.read_csv(os.path.join(BL, "M6", "fund_alternatives.csv"))
    p = p[p.lens != "MC_JPM"].copy()
    q = q[q.lens != "MC"].copy()
    frame_compare("M6 fund alternatives, history 1928-2020 (93) and ETF 2011-2020 (10) lenses", p, q, ["fund", "lens"],
                  {"gift_worst": "gift_worst", "gift_p10": "gift_p10", "gift_p50": "gift_p50", "gift_p90": "gift_p90",
                   "T33_p50": "T33_p50", "p_top": "p_top"}, tol=0.011)
    # ---- M7 stress table
    p = pd.DataFrame(P7["stress"]).rename(columns={"id": "scenario"})
    q = pd.read_csv(os.path.join(BL, "M7", "stress_table.csv"))
    q = q[q.scenario != "S2_lit"]
    frame_compare("M7 stress table, every scenario (13) and quantity", p, q, ["scenario"],
                  {"C": "ladder_cost_C", "L": "leftover_L", "T": "topup_T", "G": "growth_money_G", "y5": "y5",
                   "F": "floor_face_F", "fund0": "fund0", "fund31": "fund31", "fund33": "fund33", "top": "top",
                   "gift": "gift", "kept": "kept", "T33": "T33", "shortfall": "short_S", "deflator_2033": "deflator_2033",
                   "real_gift": "real_gift", "real_T33": "real_T33", "real_pay_2033": "real_pay_2033",
                   "real_pay_2042": "real_pay_2042", "real_pay_total": "real_pay_total", "R1_T33": "R1_T33",
                   "R2_T33": "R2_T33", "R5_T33": "R5_T33"}, tol=0.011, bools=[("funded", "payments_funded")])
    # ---- M7 real value paths
    p = pd.DataFrame(P7["real_value_paths"])
    key = lambda s: ("breakeven" if "breakeven" in s.lower() and "S3" not in s else "cleveland" if "leveland" in s else
                     "jpm" if s.lower().startswith("jpm") else "fed" if s.startswith("Fed") or s.startswith("fed") else
                     "S1" if "1970s" in s else "S7" if "Great Inflation" in s else "S2" if "Japan" in s else
                     "S3" if ("2021-25" in s or "2022" in s) else "S5" if "Depression" in s else s)
    p["pid"] = p.path.map(key)
    q = pd.read_csv(os.path.join(BL, "M7", "real_value_paths.csv"))
    q["pid"] = q.path.map(key)
    frame_compare("M7 real value, every inflation path (9) and payment (10)", p, q, ["pid"],
                  {**{f"pay_{y}": f"real_{y}" for y in range(2033, 2043)}, "total": "total_real"}, tol=0.011)
    p = pd.DataFrame(P7["real_value_history"]).astype({"payment": str})
    tot = p[p.payment == "total"].iloc[0]
    p = p[p.payment != "total"]
    q = pd.read_csv(os.path.join(BL, "M7", "real_value_history_distribution.csv")).rename(columns={"payment_year": "payment"})
    q["payment"] = q.payment.astype(str)
    frame_compare("M7 real value, U.S. history distribution (p5/p50/p95 per payment)", p, q, ["payment"],
                  {"p5": "p5", "p50": "p50", "p95": "p95"}, tol=0.011)
    for k in ("p5", "p50", "p95"):
        add("M7", f"  history, all ten payments real total {k}", float(tot[k]), b(f"M7.real_value_history.total_{k}"), "usd_det")


# --------------------------------------------------------------------------------------------------- headline keys
def headline_keys():
    A = P5["part_a"]
    ext = A["extended"]
    S = {(r["view"], r["fund"]): r for r in P5["part_b_summary"]}
    h, t = S[("hist", "world_eq")], S[("today_yields", "world_eq")]
    sec = "M5"
    # 1 m5.cost_of_certainty.today_usd
    add(sec, "m5.cost_of_certainty.today_usd: ten payments on 28 Sep 2026", A["today_V0"], b("M5.A.V0_D"), "usd_det", True,
        note="numbers.yaml laura.ladder.cost_today_strips 289,119.20")
    add(sec, "  2020 median cost", A["m1g_repro"]["y2020_median"], b("M5.A.cost_2020_median"), "usd_det", True)
    add(sec, "  peak cost ($470,249)", A["m1g_repro"]["y2020_max"], b("M5.A.cost_2020_max"), "usd_det", True)
    add(sec, "  peak date", A["m1g_repro"]["y2020_max_date"], b("M5.A.cost_2020_max_date"), "exact", True)
    add(sec, "  cheapest since (last day as cheap)", A["m1g_repro"]["last_date_at_or_below_today"], b("M5.A.cheapest_since_spot"),
        "exact", True)
    # 2 share of months
    add(sec, "m5.cost_of_certainty.share_months_since_1871_as_cheap", ext["since_1871"]["share_months_le_today"],
        b("M5.A.share_months_le_V0D_since_1871"), "share_det", True)
    add(sec, "  same, flat-curve bias removed (median error)", ext["flat_bias_sensitivity"]["median_error"]["share_months_le_today_since_1871"],
        b("M5.A.share_months_le_V0D_since_1871_adj_median"), "share_det", True)
    add(sec, "  same, flat-curve bias removed (95th pct error)", ext["flat_bias_sensitivity"]["p95_error"]["share_months_le_today_since_1871"],
        b("M5.A.share_months_le_V0D_since_1871_adj_p95"), "share_det", True)
    add(sec, "  share of months since 1962", ext["since_1962"]["share_months_le_today"], b("M5.A.share_months_le_V0D_since_1962"),
        "share_det", True)
    add(sec, "  share of months since 1871 at or under $300,000", ext["since_1871"]["share_months_le_300k"],
        b("M5.A.share_months_le_300k_since_1871"), "share_det")
    add(sec, "  share of calendar years whose median is below today", ext["share_years_median_below_today"],
        b("M5.A.share_years_median_below_V0D_1871_2026"), "share_det")
    add(sec, "  cheapest day ($110,214)", ext["since_1962_daily"]["min"], b("M5.A.lowest_since_1962.usd"), "usd_det", True)
    add(sec, "  cheapest day, date", ext["since_1962_daily"]["min_date"], b("M5.A.lowest_since_1962.date"), "exact", True)
    mon = pd.read_csv(os.path.join(BL, "M5", "cost_of_certainty_monthly.csv"))
    i = mon.V0.idxmin()
    add(sec, "  cheapest month start since 1871 ($111,249)", ext["since_1871"]["min"], float(mon.V0[i]), "usd_det",
        note=f"blind monthly file, {mon.date[i]}; the blind report's 'lowest since 1871' ($110,214) is over every curve "
             "date, not month starts: spec wording (A3 ii), both builds give both figures")
    add(sec, "  highest day ($470,249, 4 Aug 2020)", ext["since_1962_daily"]["max"], b("M5.A.highest_since_1871.usd"), "usd_det")
    add(sec, "  flat-vs-full curve bias, median", P5["part_a"]["check_flat_vs_full"]["median"], b("M5.A.flat_vs_full_1962_2026.median"),
        "share_det")
    add(sec, "  FRED vs Treasury file, largest difference", P5["part_a"]["check_fred_vs_par"]["max_abs_usd"],
        b("M5.A.fred_vs_treasury_1990_2026.largest_abs_diff_usd"), "usd_det")
    # share of days <= 300k since 2000 (H17), from the primary series
    ser = pd.read_csv(os.path.join(PR, "M5", "cost_of_certainty_series.csv"))
    s00 = ser[(ser.date >= "2000-01-01") & (ser.basis == "treasury_par")]
    add(sec, "  share of days since 2000 at or under $300,000 (insight_v1 H17: 11.1%)", float((s00.V0 <= 300_000).mean()),
        b("M5.A.share_days_le_300k_since_2000_spot"), "share_det", note=f"{len(s00)} days in the primary series")
    # 3 start years all paid
    add(sec, "m5.hist.start_years_all_payments_paid (windows with no payment short)", h["windows"] - h["n_unfunded"],
        b("M5.B.hist.world_eq.n_windows") - b("M5.B.hist.world_eq.n_short_S_gt_0"), "exact", True)
    add(sec, "  dearest ladder ($411k)", max(r["ladder_cost_max"] for r in P5["eras"]), b("M5.B.hist.world_eq.ladder_cost_C_max"),
        "usd_det", True, note="primary: era table maximum")
    add(sec, "  start years where the 2028 deposit finished the ladder", h["n_topup"], b("M5.B.hist.world_eq.n_topup_T_gt_0"), "exact", True)
    add(sec, "  start years with the floor below $150k", h["n_bottom_lt_150k"], b("M5.B.hist.world_eq.n_fund0_zero"), "exact", True,
        note="blind counts fund0 = 0, which is the same event (G < floor cost)")
    # 4 hist gift
    add(sec, "m5.hist.gift_median_usd", h["gift_median"], b("M5.B.hist.world_eq.gift_median"), "usd_sum", True)
    add(sec, "  gift p10", h["gift_p10"], b("M5.B.hist.world_eq.gift_p10"), "usd_sum", True)
    add(sec, "  gift worst", h["gift_worst"], b("M5.B.hist.world_eq.gift_worst"), "usd_sum", True)
    add(sec, "  gift worst start year", h["gift_worst_Y"], b("M5.B.hist.world_eq.gift_worst_Y"), "exact", True)
    add(sec, "  share of windows with the top reached", h["share_top_reached"], b("M5.B.hist.world_eq.share_top_reached"), "share_det")
    # 5 today's yields
    add(sec, "m5.today_yields.gift_worst_usd", t["gift_worst"], b("M5.B.today_yields.world_eq.gift_worst"), "usd_sum", True)
    add(sec, "  worst start year (fund bought the next year)", t["gift_worst_Y"], b("M5.B.today_yields.world_eq.gift_worst_Y"), "exact", True)
    add(sec, "  gift p10", t["gift_p10"], b("M5.B.today_yields.world_eq.gift_p10"), "usd_sum", True)
    add(sec, "  gift median", t["gift_median"], b("M5.B.today_yields.world_eq.gift_median"), "usd_sum", True)
    add(sec, "  top reached", t["share_top_reached"], b("M5.B.today_yields.world_eq.share_top_reached"), "share_det", True)
    add(sec, "  windows with the floor below $150k", t["n_bottom_lt_150k"], b("M5.B.today_yields.world_eq.n_fund0_zero"), "exact", True)
    add(sec, "  check: fund0 at today's yields (numbers.yaml 40,736)", t["fund0_median"], b("M5.B.check.today_fund0"), "usd_det", True)
    for k, lab in (("1872-1913", "era 1872-1913"), ("1914-1945", "era 1914-1945"), ("1946-1981", "era 1946-1981"),
                   ("1982-2020", "era 1982-2020")):
        e = next(r for r in P5["eras"] if r["era"] == k)
        add(sec, f"  {lab}: median ladder cost / median gift / worst gift",
            f"{e['ladder_cost_median']:,.0f} / {e['gift_median']:,.0f} / {e['gift_worst']:,.0f}",
            f"{b(f'M5.B.era.{k}.median_ladder_cost'):,.0f} / {b(f'M5.B.era.{k}.median_gift'):,.0f} / "
            f"{b(f'M5.B.era.{k}.worst_gift'):,.0f}", "text")
    # 6 H9: third computation (the blind spec has no H9 row)
    h9 = P5["h9_reconciliation"]
    third = h9_third()
    add(sec, "m5.H9_reverified.rescaled_total_worst_usd (third computation, this script)", h9["rescaled_total_worst"],
        third["rescaled_worst"], "usd_det", True, note="blind M5 has no H9 row (not in M5_SPEC); recomputed here from "
        "annual_history.csv and the blind build's fund0")
    add(sec, "  H9 raw total worst (blind per-window T33, U.S., 1928-2020)", h9["raw_total_worst"], third["raw_worst"], "usd_det", True)
    add(sec, "  H9 rescaled p10", h9["rescaled_total_p10"], third["rescaled_p10"], "usd_det", True)
    add(sec, "  H9 rescaled median", h9["rescaled_total_median"], third["rescaled_median"], "usd_det", True)

    sec = "M6"
    rec = psum("REC")
    add(sec, "m6.rec.mc_T33_median_usd", rec["mc_T33_p50"], b("M6.MC.REC.T33_p50"), "pct_mc", True)
    add(sec, "  REC MC T33 p5", rec["mc_T33_p5"], b("M6.MC.REC.T33_p5"), "pct_mc", True)
    add(sec, "  REC MC T33 p95", rec["mc_T33_p95"], b("M6.MC.REC.T33_p95"), "pct_mc", True)
    add(sec, "  REC MC gift p5", rec["mc_gift_p5"], b("M6.MC.REC.gift_p5"), "pct_mc", True)
    add(sec, "  REC MC gift p50", rec["mc_gift_p50"], b("M6.MC.REC.gift_p50"), "pct_mc", True)
    add(sec, "  REC MC payments short (share)", rec["mc_unfunded"], b("M6.MC.REC.unfunded_share"), "prob_mc", True)
    add(sec, "  REC certain by 2031", rec["mc_certain31_p50"], b("M6.MC.REC.certain31_p50"), "usd_det", True)
    r2 = psum("R2")
    add(sec, "m6.sixty_forty_whole.mc_payment_short", r2["mc_unfunded"], b("M6.MC.R2.unfunded_share"), "prob_mc", True)
    add(sec, "  60/40 history windows short (of 149)", r2["h_unfunded"], round(b("M6.history.R2.unfunded_share") * 149), "exact", True)
    add(sec, "  60/40 MC T33 p5", r2["mc_T33_p5"], b("M6.MC.R2.T33_p5"), "pct_mc", True)
    add(sec, "  glide path 65->20 MC short", psum("R4")["mc_unfunded"], b("M6.MC.R4.unfunded_share"), "prob_mc", True)
    add(sec, "  growth-first 75->40 MC short", psum("R4b")["mc_unfunded"], b("M6.MC.R4b.unfunded_share"), "prob_mc", True)
    for rid, bid in (("R1", "R1"), ("R3", "R3"), ("R4", "R4"), ("R4b", "R4b"), ("R5", "R5_m3"), ("R5m5", "R5_m5")):
        r = psum(rid)
        for q, bq in (("p5", "p5"), ("p50", "p50"), ("p95", "p95")):
            add(sec, f"  {rid} MC T33 {q}", r[f"mc_T33_{q}"], b(f"M6.MC.{bid}.T33_{bq}"), "pct_mc")
        add(sec, f"  {rid} history windows short / T33 median", f"{r['h_unfunded']} / {r['h_T33_median']:,.0f}",
            f"{round(b(f'M6.history.{bid}.unfunded_share') * 149)} / {b(f'M6.history.{bid}.T33_p50'):,.0f}", "text")
    h16 = P6["h16_reverified"]
    add(sec, "m6.H16_reverified.growth_first_short_deposit_75k", h16["deposit_75000"], b("M6.H16.deposit_75k"), "prob_mc", True)
    add(sec, "  H16 deposit $150k", h16["deposit_150000"], b("M6.H16.deposit_150k"), "prob_mc", True)
    add(sec, "  H16 deposit $0", h16["deposit_0"], b("M6.H16.deposit_0"), "prob_mc", True)
    c3, c5 = psum("R5"), psum("R5m5")
    add(sec, "m6.cppi3.mc_floor_broken (T33 < $150k)", c3["mc_floor_broken"], 1 - b("M6.MC.R5_m3.promised_150k_met_share"),
        "prob_mc", True, note="blind: 1 - promised_150k_met_share (same event); the blind's 'floor_broken_share' 1.60% "
        "is a different event (cushion negative at some 1 Jan 2028-32)")
    add(sec, "  CPPI m=3 MC T33 median", c3["mc_T33_p50"], b("M6.MC.R5_m3.T33_p50"), "pct_mc", True)
    add(sec, "  CPPI m=5 MC $150k missed", c5["mc_floor_broken"], 1 - b("M6.MC.R5_m5.promised_150k_met_share"), "prob_mc", True)
    hist_all = pd.read_csv(os.path.join(PR, "M6", "rivals_history.csv"))
    hist_c3 = hist_all[hist_all.rival == "R5"]
    for rid, bid, lab in (("R5", "R5_m3", "m=3"), ("R5m5", "R5_m5", "m=5")):
        hc = hist_c3[hist_c3.rival == rid] if rid == "R5" else hist_all[hist_all.rival == rid]
        add(sec, f"  CPPI {lab} history: windows with T33 < $150k", int(psum(rid)["h_floor_broken"]),
            round((1 - b(f"M6.history.{bid}.promised_150k_met_share")) * 149), "exact", False,
            note=f"per-window primary CSV: {int((hc.floor_broken.astype(str) == 'True').sum())}. The committed summary said 1 "
                 "(numpy-bool sum in an object column); fixed in m6_rivals.py at this gate")
    tips = P6["tips"]
    add(sec, "m6.tips_ladder.mc_any_payment_short", tips["p_any_short"], b("M6.MC.R6.unfunded_share"), "prob_mc", True)
    add(sec, "  TIPS history paths short (of 140)", psum("R6")["h_unfunded"], round(b("M6.history.R6.unfunded_share") * 140), "exact", True)
    add(sec, "  TIPS MC total shortfall p95", tips["shortfall_p95"], b("M6.MC.R6.gap_p95"), "pct_mc")
    add(sec, "  TIPS AR(1) phi", round(tips["phi"], 6), round(b("M6.R6.inflation_ar1.phi"), 6), "exact")
    sc = tips_scale_third()
    add(sec, "  TIPS ladder size needed for full delivery in 95% of paths (x; third computation)",
        tips["tips_scale_for_95pct_full"], sc, "pct_mc", True,
        note="blind build's own inflation paths (same seed and draw order by spec), scale = p95 of max_k 50,000 / paid_k")
    add(sec, "  ... extra cost ($125k)", tips["tips_extra_cost_for_95pct_full_usd"],
        (sc - 1) * NUMS["laura.ladder.cost_2027_strips"]["value"], "pct_mc", True)
    dec = {r["fund"]: r for r in P6["fund_decision"]}
    rob = P6["fund_robustness"]["mc"]
    add(sec, "m6.fund_choice.gold_reit_spread_ratio (seed 20260930)", dec["A4"]["mc_spread90_ratio"],
        b("M6.fund_decision.A4.mc_spread90_ratio"), "ratio_mc", True)
    add(sec, "  A4 MC gift p5 change", dec["A4"]["mc_p5_change"], b("M6.fund_decision.A4.mc_gift_p5_delta"), "pct_mc", True,
        note="relative to VT's p5 ($165k): -0.01%")
    add(sec, "  A4 history p10 change", dec["A4"]["hist_p10_change"], b("M6.fund_decision.A4.hist_gift_p10_delta"), "usd_det", True)
    add(sec, "  A4 history spread80 ratio", round(dec["A4"]["hist_spread80_ratio"], 6), round(b("M6.fund_decision.A4.hist_spread80_ratio"), 6),
        "exact", True)
    add(sec, "  A4 tests 1-3 on seed 20260930", bool(dec["A4"]["passes_numbers"]), bool(b("M6.fund_decision.A4.tests_1_to_3_pass")),
        "bool", True)
    add(sec, "  A4 spread test passed on 20 other seeds", rob["A4"]["c1b"], b("M6.fund_decision.A4.pass_1_to_3"), "count_mc", True,
        note="different seed sets (reference 20261930-49, blind 20260930-49); see the large-sample row")
    mp = os.path.join(HERE, "gateB_ws3_mc_precision.json")
    if os.path.exists(mp):
        m = jload(mp)
        add(sec, "  A4 spread ratio without noise (100 seeds x 200k paths each build)", m["reference"]["ratio_mean"],
            m["blind"]["ratio_mean"], "ratio_mc", True,
            note=f"se {m['reference']['ratio_se']:.4f}; pooled 10M paths {m['reference']['pooled']['spread_ratio']:.4f} / "
                 f"{m['blind']['pooled']['spread_ratio']:.4f}; passes the 0.90 bar on {m['reference']['share_seeds_ratio_le_090']:.0%}"
                 f" / {m['blind']['share_seeds_ratio_le_090']:.0%} of 200k-path seeds")
    for a in ("A1", "A2", "A3"):
        add(sec, f"  {a} tests 1-3 pass", bool(dec[a]["passes_numbers"]), bool(b(f"M6.fund_decision.{a}.tests_1_to_3_pass")), "bool", True)
    add(sec, "  final decision (all four alternatives)", "KEEP VT", "KEEP VT" if b("M6.fund_decision.any_switch") == 0 else "SWITCH",
        "exact", True)

    sec = "M7"
    th = P7["thresholds"]
    add(sec, "m7.threshold.floor_150k_holds_to_bp", th["fund_used_up_bp"], b("M7.threshold.b_fund0_zero_floor_150k_bp"), "bp", True)
    add(sec, "  top-up starts (numbers.yaml 26.2bp)", th["topup_starts_bp"], b("M7.threshold.a_topup_starts_C_300k_bp"), "bp", True)
    add(sec, "  a payment unfunded", th["payment_unfunded_bp"], b("M7.threshold.c_payment_unfunded_G_zero_bp"), "bp", True)
    st = {r["id"]: r for r in P7["stress"]}
    add(sec, "m7.stress.worst_gift_usd (S2b)", min(r["gift"] for r in P7["stress"]),
        min(b(f"M7.{s}.gift") for s in st), "usd_det", True)
    for s in ("S0", "S1", "S2", "S2b", "S3", "S3b", "S4a", "S4b", "S4c", "S4d", "S5", "S6", "S7"):
        add(sec, f"  {s} gift / real gift", f"{st[s]['gift']:,.2f} / {st[s]['real_gift']:,.2f}",
            f"{b(f'M7.{s}.gift'):,.2f} / {b(f'M7.{s}.real_gift'):,.2f}", "text", True)
    add(sec, "  every scenario funds every payment", all(r["funded"] for r in P7["stress"]), bool(b("M7.all_headline_scenarios_payments_funded")),
        "bool", True)
    dg = {r["announced"]: r for r in P7["downgrades"]}
    add(sec, "m7.downgrade_2011.dy_bp (FRED DGS10, 20 trading days)", dg["2011-08-05"]["dy_bp"], b("M7.downgrade.S4a.dgs10_change_pp") * 100,
        "bp", True)
    add(sec, "  Fitch 2023", dg["2023-08-01"]["dy_bp"], b("M7.downgrade.S4b.dgs10_change_pp") * 100, "bp", True)
    add(sec, "  Moody's 2025", dg["2025-05-16"]["dy_bp"], b("M7.downgrade.S4c.dgs10_change_pp") * 100, "bp", True)
    add(sec, "  S4a ladder cost / fund0", f"{st['S4a']['C']:,.2f} / {st['S4a']['fund0']:,.2f}",
        f"{b('M7.S4a.ladder_cost_C'):,.2f} / {b('M7.S4a.fund0'):,.2f}", "text", True)
    rv = P7["real_value_paths"][0]
    add(sec, "m7.real_value.pay_2042_breakeven_usd", rv["pay_2042"], b("M7.real_value.breakeven_T10YIE_2.34.real_2042"), "usd_det", True)
    add(sec, "  all ten at breakeven", rv["total"], b("M7.real_value.breakeven_T10YIE_2.34.total_real"), "usd_det", True)
    s1 = next(r for r in P7["real_value_paths"] if r["path"].startswith("1970s"))
    add(sec, "  1970s path: 2042 payment", s1["pay_2042"], b("M7.S1.real_pay_2042"), "usd_det", True)
    add(sec, "  1970s path: all ten", s1["total"], b("M7.S1.real_pay_total"), "usd_det", True)
    hd = {str(r["payment"]): r for r in P7["real_value_history"]}
    add(sec, "  history 2042 payment p5 / p50 / p95", f"{hd['2042']['p5']:,.2f} / {hd['2042']['p50']:,.2f} / {hd['2042']['p95']:,.2f}",
        f"{b('M7.real_value_history.2042.p5'):,.2f} / {b('M7.real_value_history.2042.p50'):,.2f} / {b('M7.real_value_history.2042.p95'):,.2f}",
        "text", True)
    add(sec, "  H19 reproduced (2033 / 2042)", f"{P7['h19']['h19_reproduced']['2033']:,.2f} / {P7['h19']['h19_reproduced']['2042']:,.2f}",
        f"{b('M7.H19.2033'):,.2f} / {b('M7.H19.2042'):,.2f}", "text", True)


def tips_scale_third():
    sys.path.insert(0, os.path.join(WT, "rab", "verification", "blind"))
    import blind_m5 as BM5
    import blind_m6 as BM6
    bk, mi = BM6.breakevens()
    r = BM6.mc_inflation(BM5.load_annual(), bk, mi)
    need = np.max(BM6.PAYMENT / r["paid"], axis=1)
    return float(np.percentile(need, 95))


def h9_third():
    """insight_v1 H9 convention (E6 [5]): U.S. stocks, windows Y = 1928..2020, today's yields; rescaled so the mean log
    return over 1928-2025 is ln 1.07. Written here from annual_history.csv, using the blind build's fund0."""
    A = pd.read_csv(os.path.join(WT, "rab", "data", "history", "annual_history.csv")).set_index("year")
    f0 = b("M5.B.check.today_fund0")
    eq = A.us_eq.loc[1928:2025]
    lg = np.log1p(eq)
    rs = np.expm1(lg - lg.mean() + math.log(1.07))
    tot = np.array([150_000 + f0 * np.prod(1 + rs.loc[Y + 1:Y + 5].values) for Y in range(1928, 2021)])
    q = pd.read_csv(os.path.join(BL, "M5", "backtest_by_start_year.csv"))
    q = q[(q.view == "today_yields") & (q.fund_series == "us_eq") & (q.Y >= 1928)]
    return dict(raw_worst=float(q.T33.min()), raw_worst_Y=int(q.loc[q.T33.idxmin(), "Y"]), rescaled_worst=float(tot.min()),
                rescaled_worst_Y=1928 + int(tot.argmin()), rescaled_p10=float(np.percentile(tot, 10)),
                rescaled_median=float(np.median(tot)))


# --------------------------------------------------------------------------------------------------- proposed numbers
def proposed():
    """Every value in WS3_numbers_proposed.yaml against the blind build (these are the numbers WS1 would lock)."""
    out = []

    def chk(entry, field, pv, bv, kind):
        r = add("proposed", f"{entry}.{field}", pv, bv, kind, True)
        out.append(r)

    P = {k: v["value"] for k, v in PROP.items()}
    chk("ws3.certainty.share_months_as_cheap_since_1871", "value", P["ws3.certainty.share_months_as_cheap_since_1871"],
        b("M5.A.share_months_le_V0D_since_1871"), "share_det")
    chk("ws3.certainty.low_1981", "usd", P["ws3.certainty.low_1981"]["usd"], b("M5.A.lowest_since_1962.usd"), "usd_det")
    v = P["ws3.backtest.hist.unfunded_windows"]
    chk("ws3.backtest.hist.unfunded_windows", "unfunded", v["unfunded"], b("M5.B.hist.world_eq.n_short_S_gt_0"), "exact")
    chk("ws3.backtest.hist.unfunded_windows", "topups", v["topups"], b("M5.B.hist.world_eq.n_topup_T_gt_0"), "exact")
    chk("ws3.backtest.hist.unfunded_windows", "floor_below_150k", v["floor_below_150k"], b("M5.B.hist.world_eq.n_fund0_zero"), "exact")
    chk("ws3.backtest.hist.unfunded_windows", "ladder_cost_max", v["ladder_cost_max"], b("M5.B.hist.world_eq.ladder_cost_C_max"), "usd_det")
    for f, k in (("worst", "gift_worst"), ("p10", "gift_p10"), ("median", "gift_median")):
        chk("ws3.backtest.hist.gift", f, P["ws3.backtest.hist.gift"][f], b(f"M5.B.hist.world_eq.{k}"), "usd_det")
    for f, k in (("worst", "gift_worst"), ("p10", "gift_p10"), ("median", "gift_median"), ("top_reached", "share_top_reached")):
        chk("ws3.backtest.today_yields.gift", f, P["ws3.backtest.today_yields.gift"][f], b(f"M5.B.today_yields.world_eq.{k}"),
            "share_det" if f == "top_reached" else "usd_det")
    t9 = h9_third()
    for f, k in (("total_worst_raw", "raw_worst"), ("total_worst_rescaled", "rescaled_worst"), ("p10_rescaled", "rescaled_p10"),
                 ("median_rescaled", "rescaled_median")):
        chk("ws3.backtest.H9_reverified", f, P["ws3.backtest.H9_reverified"][f], t9[k], "usd_det")
    for key, bid in (("rec", "REC"), ("all_treasury", "R1"), ("sixty_forty", "R2"), ("ladder_6040", "R3"), ("glide", "R4"),
                     ("growth_first", "R4b"), ("cppi3", "R5_m3"), ("cppi5", "R5_m5")):
        v = P[f"ws3.rivals.{key}"]
        chk(f"ws3.rivals.{key}", "mc_short", v["mc_short"], b(f"M6.MC.{bid}.unfunded_share"), "prob_mc")
        for i, q in enumerate(("p5", "p50", "p95")):
            chk(f"ws3.rivals.{key}", f"mc_T33_{q}", v["mc_T33"][i], b(f"M6.MC.{bid}.T33_{q}"), "pct_mc")
        chk(f"ws3.rivals.{key}", "mc_certain31", v["mc_certain31"], b(f"M6.MC.{bid}.certain31_p50"), "pct_mc")
        chk(f"ws3.rivals.{key}", "hist_short", v["hist_short"], f"{round(b(f'M6.history.{bid}.unfunded_share') * 149)}/149", "exact")
        for i, q in enumerate(("p10", "p50", "p90")):
            chk(f"ws3.rivals.{key}", f"hist_T33_{q}", v["hist_T33"][i], b(f"M6.history.{bid}.T33_{q}"), "usd_det")
        chk(f"ws3.rivals.{key}", "trades", v["trades"], b(f"M6.history.{bid}.trades"), "exact")
        if "mc_floor_broken" in v:
            chk(f"ws3.rivals.{key}", "mc_floor_broken", v["mc_floor_broken"], 1 - b(f"M6.MC.{bid}.promised_150k_met_share"), "prob_mc")
    v = P["ws3.rivals.tips_ladder"]
    chk("ws3.rivals.tips_ladder", "mc_p_any_short", v["mc_p_any_short"], b("M6.MC.R6.unfunded_share"), "prob_mc")
    chk("ws3.rivals.tips_ladder", "hist_short", v["hist_short"], f"{round(b('M6.history.R6.unfunded_share') * 140)}/140", "exact")
    v = P["ws3.rivals.H16_reverified"]
    for f, k in (("deposit_150k", "deposit_150k"), ("deposit_75k", "deposit_75k"), ("deposit_0", "deposit_0")):
        chk("ws3.rivals.H16_reverified", f, v[f], b(f"M6.H16.{k}"), "prob_mc")
    v = P["ws3.fund_choice"]
    chk("ws3.fund_choice", "decision", v["decision"], "KEEP VT" if b("M6.fund_decision.any_switch") == 0 else "SWITCH", "exact")
    chk("ws3.fund_choice", "gold_reit_mc_p5_change", v["gold_reit_mc_p5_change"], b("M6.fund_decision.A4.mc_gift_p5_delta"), "pct_mc")
    chk("ws3.fund_choice", "gold_reit_spread_ratio", v["gold_reit_spread_ratio"], b("M6.fund_decision.A4.mc_spread90_ratio"), "ratio_mc")
    v = P["ws3.stress.thresholds_bp"]
    for f, k in (("topup_starts", "a_topup_starts_C_300k_bp"), ("fund_used_up", "b_fund0_zero_floor_150k_bp"),
                 ("payment_unfunded", "c_payment_unfunded_G_zero_bp")):
        chk("ws3.stress.thresholds_bp", f, v[f], round(b(f"M7.threshold.{k}"), 1), "bp")
    for s in ("S1", "S2", "S3", "S4a", "S5", "S6"):
        v = P[f"ws3.stress.{s}"]
        chk(f"ws3.stress.{s}", "gift", v["gift"], b(f"M7.{s}.gift"), "usd_det")
        chk(f"ws3.stress.{s}", "real_gift", v["real_gift"], b(f"M7.{s}.real_gift"), "usd_det")
        chk(f"ws3.stress.{s}", "floor", v["floor"], b(f"M7.{s}.floor_face_F"), "usd_det")
        chk(f"ws3.stress.{s}", "payments_funded", v["payments_funded"], bool(b(f"M7.{s}.payments_funded")), "bool")
    v = P["ws3.real_value.breakeven"]
    for f, k in (("pay_2033", "real_2033"), ("pay_2042", "real_2042"), ("all_ten", "total_real")):
        chk("ws3.real_value.breakeven", f, v[f], b(f"M7.real_value.breakeven_T10YIE_2.34.{k}"), "usd_det")
    v = P["ws3.real_value.1970s"]
    chk("ws3.real_value.1970s", "pay_2042", v["pay_2042"], b("M7.S1.real_pay_2042"), "usd_det")
    chk("ws3.real_value.1970s", "all_ten", v["all_ten"], b("M7.S1.real_pay_total"), "usd_det")
    v = P["ws3.real_value.history_2042"]
    for f in ("p5", "p50", "p95"):
        chk("ws3.real_value.history_2042", f, v[f], b(f"M7.real_value_history.2042.{f}"), "usd_det")
    v = P["ws3.real_value.H19_reverified"]
    chk("ws3.real_value.H19_reverified", "2033", v["2033"], b("M7.H19.2033"), "usd_det")
    chk("ws3.real_value.H19_reverified", "2042", v["2042"], b("M7.H19.2042"), "usd_det")
    # precision check: proposed probabilities must carry the model's value, not a 2-decimal CSV rounding
    prec = []
    for key, rid in (("sixty_forty", "R2"), ("glide", "R4"), ("growth_first", "R4b"), ("cppi3", "R5"), ("cppi5", "R5m5")):
        pv = P[f"ws3.rivals.{key}"]["mc_short"]
        mv = psum(rid)["mc_unfunded"]
        prec.append(dict(entry=f"ws3.rivals.{key}.mc_short", proposed=pv, model=mv, ok=abs(pv - mv) < 5e-5))
        if "mc_floor_broken" in P[f"ws3.rivals.{key}"]:
            pv, mv = P[f"ws3.rivals.{key}"]["mc_floor_broken"], psum(rid)["mc_floor_broken"]
            prec.append(dict(entry=f"ws3.rivals.{key}.mc_floor_broken", proposed=pv, model=mv, ok=abs(pv - mv) < 5e-5))
    DETAIL["proposed_precision"] = prec
    return out


# --------------------------------------------------------------------------------------------------- insight_v1
def insight_v1():
    """rab/inventory.md s2 rows that WS3 must reconcile (H8, H9, H12, H13, H16, H17, H18, H19)."""
    rec = psum("REC")
    t9 = h9_third()
    h9 = P5["h9_reconciliation"]
    A = P5["part_a"]
    rows = [
        dict(ref="H8", insight_v1="REC total p5/p50/p95 $182k / $207k / $250k; gift $165k / $174k / $188k; P(top) 73% "
                                  "(25 Sep, E6 engine, seed 20260927)",
             primary=f"${rec['mc_T33_p5'] / 1e3:,.1f}k / ${rec['mc_T33_p50'] / 1e3:,.1f}k / ${rec['mc_T33_p95'] / 1e3:,.1f}k; gift "
                     f"${rec['mc_gift_p5'] / 1e3:,.1f}k / ${rec['mc_gift_p50'] / 1e3:,.1f}k / ${rec['mc_gift_p95'] / 1e3:,.1f}k",
             blind=f"${b('M6.MC.REC.T33_p5') / 1e3:,.1f}k / ${b('M6.MC.REC.T33_p50') / 1e3:,.1f}k / ${b('M6.MC.REC.T33_p95') / 1e3:,.1f}k; "
                   f"gift ${b('M6.MC.REC.gift_p5') / 1e3:,.1f}k / ${b('M6.MC.REC.gift_p50') / 1e3:,.1f}k / "
                   f"${b('M6.MC.REC.gift_p95') / 1e3:,.1f}k; P(top) {b('M6.MC.REC.top_reached_share'):.1%}",
             why="Within $2k at every point (E6 [2] re-run today prints the H8 figures unchanged). Causes: the 28 Sep basis "
                 "(leftover $7,582 vs $7,736, 5-year yield 5.06% vs 4.98%, bond fund 5.06% vs 5.00%), M6's correlated "
                 "9-asset JPM draws vs E6's one-asset lognormal, and seed 20260930 vs 20260927. WS2's M3 owns H8"),
        dict(ref="H9", insight_v1="rescaled worst $169k (1928), raw worst $171k, p10 $185k, median $214k",
             primary=f"${h9['rescaled_total_worst']:,.0f} / ${h9['raw_total_worst']:,.0f} / ${h9['rescaled_total_p10']:,.0f} / "
                     f"${h9['rescaled_total_median']:,.0f}",
             blind=f"(third computation) ${t9['rescaled_worst']:,.0f} / ${t9['raw_worst']:,.0f} / ${t9['rescaled_p10']:,.0f} / "
                   f"${t9['rescaled_median']:,.0f}",
             why="Reproduced on the 28 Sep basis (E6 [5] re-run today, 25 Sep basis: $169k / $171k / $185k / $214k, top "
                 "reached 77%). The raw worst is $171.5k because the 28 Sep stock fund is $40,736, about $290 more than "
                 "E6's 25 Sep $40,443. M5's own worst ($159k gift, $173k total) is lower because M5 adds 1872-1927 and uses a world fund"),
        dict(ref="H12", insight_v1="bad 2031-32 returns: gift median $169k, never below the announced bottom",
             primary="not an M5-M7 output; closest: S6 2008-in-2028 gift $164,302, S5 Depression $159,298",
             blind="S6 $164,302; S5 $159,298", why="Different question (a named episode, not the bottom decile). Both "
                                                    "agree the gift never falls below the bottom once the floor is bought. WS2 owns H12"),
        dict(ref="H13", insight_v1="rates fall first: fund $20-23k (-50bp), $1-7k (-100bp), none, floor $127-137k (-150bp) on 25 Sep",
             primary=h13_row("primary"), blind=h13_row("blind"),
             why="Both M7 engines give exactly the low end of WS4's 28 Sep ranges (WS4 Gate B: $22,590-25,419 / "
                 "$3,626-9,366 / none; floor $130,724-140,469): a fall that persists to Jan 2028 is the E6 [8] convention with "
                 "the smallest fund. The fund is used up at 109.3bp; the 25 Sep figures were lower because there was less room"),
        dict(ref="H16", insight_v1="growth-first misses a payment 3.2% / 13.7% / 40.8% ($150k / $75k / $0 2028 deposit), 25 Sep, "
                                   "old engine with 4.00% bonds",
             primary=f"{P6['h16_reverified']['deposit_150000']:.2%} / {P6['h16_reverified']['deposit_75000']:.2%} / "
                     f"{P6['h16_reverified']['deposit_0']:.2%}",
             blind=f"{b('M6.H16.deposit_150k'):.2%} / {b('M6.H16.deposit_75k'):.2%} / {b('M6.H16.deposit_0'):.2%}",
             why="Superseded, not reproduced: the M6 bond fund earns today's 5.06% (JPM 4.00% before), so the whole-portfolio "
                 "plan grows faster and misses less. Both builds agree within 0.2pp"),
        dict(ref="H17", insight_v1="2020 median about $459k; max $470,249 on 4 Aug 2020; cheapest since 28 May 2002; <= $300k on "
                                   "11.1% of days since 2000",
             primary=f"${A['m1g_repro']['y2020_median']:,.0f}; ${A['m1g_repro']['y2020_max']:,.0f} on {A['m1g_repro']['y2020_max_date']}; "
                     f"{A['m1g_repro']['last_date_at_or_below_today']}; {share_days_primary():.1%}",
             blind=f"${b('M5.A.cost_2020_median'):,.0f}; ${b('M5.A.cost_2020_max'):,.0f} on {b('M5.A.cost_2020_max_date')}; "
                   f"{b('M5.A.cheapest_since_spot')}; {b('M5.A.share_days_le_300k_since_2000_spot'):.1%}",
             why="Identical (three pricers at Gate A, both WS3 builds here)"),
        dict(ref="H18", insight_v1="a payment partly unfunded on 197 of 6,688 days, all 2020-21; worst $20,588 on 4 Aug 2020",
             primary="not an M5 output (M5 is start-of-year); M5 start years 1872-2020: 0 unfunded", blind=h18_third(),
             why="Third computation here with the blind curve code (forward to the day's 1 Jan 2027 equivalent, deposit valued "
                 "one year later). A 1 January start never hits it, which is why M5 finds 0 of 149"),
        dict(ref="H19", insight_v1="$42,063 (2033), $33,681 (2042) at 2.5% (ASSUMPTION)",
             primary=f"${P7['h19']['h19_reproduced']['2033']:,.2f} / ${P7['h19']['h19_reproduced']['2042']:,.2f}",
             blind=f"${b('M7.H19.2033'):,.2f} / ${b('M7.H19.2042'):,.2f}",
             why="Exact with its own convention (7 and 16 years from 2026). The M7 headline ($35,342) uses 1 Jan 2027 dollars and "
                 "the 2.34% breakeven, so it is not the same number; the 2.5% is now sourced to JPM"),
    ]
    DETAIL["insight_v1"] = rows
    return rows


def share_days_primary():
    ser = pd.read_csv(os.path.join(PR, "M5", "cost_of_certainty_series.csv"))
    s = ser[(ser.date >= "2000-01-01") & (ser.basis == "treasury_par")]
    return float((s.V0 <= 300_000).mean())


def h13_row(which):
    sys.path.insert(0, os.path.join(WT, "rab", "models"))
    sys.path.insert(0, os.path.join(WT, "rab", "verification", "blind"))
    out = []
    for bp in (50, 100, 150):
        if which == "primary":
            import m7_stress as M
            r = M.run(dict(id="x", name="x", dpre=-bp / 100, dy=[0.0] * 6, e=[0.07] * 6, pi=[0.0234] * 15))
            out.append(f"-{bp}bp fund ${r['fund0']:,.0f}, floor ${r['F']:,.0f}")
        else:
            import blind_m7 as BM
            r = BM.run_scenario(-bp / 100, [0.0] * 6, [0.07] * 6, [0.0234] * 15)
            out.append(f"-{bp}bp fund ${r['fund0']:,.0f}, floor ${r['floor_face_F']:,.0f}")
    return "; ".join(out)


def h18_third():
    sys.path.insert(0, os.path.join(WT, "rab", "verification", "blind"))
    import datetime as dt
    import glob
    from blind_curve import Curve
    T0, ANCHOR = dt.date(2026, 9, 28), dt.date(2027, 1, 1)
    mats = [dt.date(y - 1, 11, 15) for y in range(2033, 2043)]
    n, unf, worst = 0, [], (None, 0.0)
    for f in sorted(glob.glob(os.path.join(WT, "rab", "data", "treasury_par_2000_2026", "*.csv"))):
        df = pd.read_csv(f)
        for _, r in df.iterrows():
            d = pd.to_datetime(r["Date"]).date()
            if d > T0:
                continue
            par = {k: r[k] for k in df.columns if k != "Date"}
            try:
                c = Curve.from_tenors(par)
            except Exception:
                continue
            a = d + (ANCHOR - T0)
            yf = lambda x: (x - d).days / 365.25
            dfa = float(c.df(yf(a)))
            fwd = sum(50_000 * float(c.df(yf(a + (m - ANCHOR)))) for m in mats) / dfa
            dep = 150_000 * float(c.df(yf(a + dt.timedelta(days=365)))) / dfa
            n += 1
            g = fwd - 300_000 - dep
            if g > 0:
                unf.append(d)
                if g > worst[1]:
                    worst = (d, g)
    yrs = sorted({d.year for d in unf})
    DETAIL["h18_third"] = dict(days=n, unfunded_days=len(unf), years=yrs, worst_date=str(worst[0]), worst_usd=worst[1])
    return f"{len(unf)} of {n} days ({', '.join(map(str, yrs))}); worst ${worst[1]:,.0f} on {worst[0]}"


# --------------------------------------------------------------------------------------------------- rerun
def rerun_check():
    """Copy the worktree's rab/ (as it is now) to a temporary folder, re-run both builds there and compare every
    tracked output byte for byte with the files in the worktree."""
    tmp = tempfile.mkdtemp(prefix="gateB_ws3_")
    shutil.copytree(os.path.join(WT, "rab"), os.path.join(tmp, "rab"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    for s in ("m5_backtest.py", "m6_rivals.py", "m7_stress.py", "ws3_numbers.py"):
        subprocess.run([PY, os.path.join("rab", "models", s)], cwd=tmp, check=True, capture_output=True)
    subprocess.run(["zsh", os.path.join("rab", "verification", "blind", "run_all.sh")], cwd=tmp, check=True, capture_output=True)
    files = subprocess.run(["git", "ls-files", "rab/results", "rab/verification/blind/out"], cwd=WT, capture_output=True,
                           text=True, check=True).stdout.split()
    diff = [f for f in files if not filecmp.cmp(os.path.join(WT, f), os.path.join(tmp, f), shallow=False)]
    stamp_only = []
    for f in [d for d in diff if d.endswith("blind_headlines.json")]:
        a, c = jload(os.path.join(WT, f)), jload(os.path.join(tmp, f))
        if a["headlines"] == c["headlines"]:
            stamp_only.append(f)
    shutil.rmtree(tmp)
    diff = [d for d in diff if d not in stamp_only]
    return dict(files=len(files), differ=diff, identical_but_time_stamp=stamp_only)


# --------------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rerun", action="store_true")
    a = ap.parse_args()
    res = {}
    if a.rerun:
        res["rerun"] = rerun_check()
        print("rerun:", res["rerun"])
    row_level()
    headline_keys()
    proposed()
    iv = insight_v1()
    order = {"M5": 0, "M6": 1, "M7": 2, "proposed": 3}
    ROWS.sort(key=lambda r: order.get(r["section"], 9))
    T = pd.DataFrame(ROWS)
    tally = T.verdict.value_counts().to_dict()
    dec = T[T.decision]
    res.update(tally=tally, decision_tally=dec.verdict.value_counts().to_dict(), unreconciled=T[T.verdict == "UNRECONCILED"].key.tolist(),
               row_level=DETAIL, rows=ROWS, numbers_yaml_sha256=open(os.path.join(WT, "rab", "numbers.lock")).read().split()[0])
    with open(os.path.join(HERE, "gateB_ws3_results.json"), "w") as f:
        json.dump(res, f, indent=1, default=lambda x: x.item() if hasattr(x, "item") else str(x))
    T.drop(columns=["diff_num"], errors="ignore").to_csv(os.path.join(HERE, "gateB_ws3_table.csv"), index=False)
    fmt = lambda v: f"{v:,.2f}" if isinstance(v, float) and abs(v) >= 1 else (f"{v:.4f}" if isinstance(v, float) else str(v))
    with open(os.path.join(HERE, "gateB_ws3_table.md"), "w") as f:
        f.write("# Gate B WS3: full comparison table (generated by gateB_ws3_checks.py)\n\n")
        f.write("(D) = decision-relevant. MATCH = within the spec's deterministic tolerance; MC NOISE = Monte Carlo key "
                "within the gate tolerance and within 3 standard errors where computable.\n\n")
        f.write("| Section | Key | Primary | Blind | Diff | Verdict | Note |\n|---|---|---|---|---|---|---|\n")
        for r in ROWS:
            f.write(f"| {r['section']} | {r['key']}{' (D)' if r['decision'] else ''} | {fmt(r['primary'])} | {fmt(r['blind'])} | "
                    f"{r.get('diff', '')} | {r['verdict']} | {r['note']} |\n")
        f.write("\n## Row-level comparisons\n\n| Comparison | Rows joined | Only primary / only blind | Max abs diff | Verdict |\n"
                "|---|---|---|---|---|\n")
        for k, v in DETAIL.items():
            if isinstance(v, dict) and "rows_joined" in v:
                f.write(f"| {k} | {v['rows_joined']} | {v['only_primary']} / {v['only_blind']} | {v['max_abs_diff']} | {v['verdict']} |\n")
        f.write("\n## insight_v1 (rab/inventory.md s2)\n\n| Ref | insight_v1 | Primary | Blind / third | Why |\n|---|---|---|---|---|\n")
        for r in iv:
            f.write(f"| {r['ref']} | {r['insight_v1']} | {r['primary']} | {r['blind']} | {r['why']} |\n")
    print(f"rows {len(ROWS)}: {tally}; decision rows: {res['decision_tally']}; unreconciled: {res['unreconciled']}")
    for k, v in DETAIL.items():
        if isinstance(v, dict) and "rows_joined" in v:
            print(f"  {v['verdict']:5s} {k}: {v['rows_joined']} rows, max |diff| {v['max_abs_diff']}"
                  + ("" if v["verdict"] == "MATCH" else f"  {json.dumps(v['columns'])[:600]}"))
    print("  proposed precision:", [(p["entry"], p["proposed"], round(p["model"], 5), p["ok"]) for p in DETAIL["proposed_precision"]])
    print("  H18 third:", DETAIL.get("h18_third"))


if __name__ == "__main__":
    main()
