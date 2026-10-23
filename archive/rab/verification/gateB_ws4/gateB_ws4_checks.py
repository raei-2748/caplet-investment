#!/usr/bin/env python
"""Gate B (WS4, M2) reconciliation checks: primary rab/models/m2_rate_paths.py vs blind rab/verification/blind/m2_blind.py.

WS4 Gate B reconciler, 2026-09-30 (Sydney). AI-generated verification code (Claude Code) for Team Caplet; MODEL outputs.

What it does (all read-only on inputs; writes only into this folder):
  [T] key-by-key table: every primary headline key (and the sub-values quoted in its meaning) against the blind value,
      diff, tolerance (Gate B: probabilities +-2pp, dollar outcomes +-2% and the spec's $500, deterministic to $1) and verdict.
  [P] Monte Carlo precision: E5 in closed form, E3 Rao-Blackwellised over 2,000,000 parameter draws, E4 with 4,000,000
      draws per sampler (numpy SVD as the primary, eigendecomposition as the blind), E1/E2 bootstrap-interval
      spread over 50 seeds. Gives the noise-free headline.
  [C] Cause checks for every difference: R1/R2/R5 valuation convention vs insight_v1 D1 code, R4 float ties vs AX1b code.
  [H] insight_v1 reconciliation (rab/inventory.md s2 H5, H6, H7, H13, H14): 25 Sep reruns of both builds, S4 30.7%,
      strategy_mc_v2 34.4%, D1 exact-date 18.7%, 2026 days over $300k.
  [X] Added at the 30 Sep re-check (second reconciler session): the blind headline keys first reported in commit
      97c3467 (4 Jan five-estimator median, PV today, 2033 rung, window counts, R3), with the primary's own code rerun
      on a 4 Jan purchase (primary_4jan_variant.py, in memory); and the blind builder's standard-library third pricer
      (rab/verification/blind/deterministic_check.json) compared against the PRIMARY, which that script never saw.
      Writes gateB_ws4_third_pricer.md as well.
Run from the worktree root:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws4/gateB_ws4_checks.py
Seed 20260930 (sub-seeds noted inline). Runtime about 30 s.
"""
from __future__ import annotations

import csv
import datetime as dt
import importlib.util
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PY = sys.executable
SEED = 20260930
PRIMARY_JSON = ROOT / "rab/results/M2/m2_results.json"
BLIND_JSON = ROOT / "rab/verification/blind/results.json"
HIST_CSV = ROOT / "rab/results/M2/m2_history_windows.csv"

spec = importlib.util.spec_from_file_location("m2_blind", ROOT / "rab/verification/blind/m2_blind.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)

P = json.load(open(PRIMARY_JSON))
Bl = json.load(open(BLIND_JSON))
OUT: dict = {"meta": {"run_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "seed": SEED,
                      "primary": str(PRIMARY_JSON.relative_to(ROOT)), "blind": str(BLIND_JSON.relative_to(ROOT))}}


def say(s=""):
    print(s, flush=True)


def pest(i):
    return P["estimators"][i]


def psens(id_):
    return next(s for s in P["sensitivities"] if s["id"] == id_)


def prow(prefix):
    return next(r for r in P["reconciliation"]["rows"] if r["row"].startswith(prefix))


BE = Bl["estimators"]
BF = Bl["fifteen_month"]
PF = {v["variant"].split()[0]: v for v in P["fifteen_months"]["variants"]}
PH = {(r["shift_bp"], r["five_year"]): r for r in P["h13_h14"]}
BH = Bl["H13_recheck"]["results"]
bmean_gaps = [BE[k]["mean_gap_given_pos_usd"] for k in BE]
bp95 = [BE[k]["gap_p95_usd"] for k in BE]
bwaits = [BE[k]["P_gap_gt_rung2033"] for k in BE]

# ---------------------------------------------------------------------------------------------------------------- [H] 25 Sep reruns
say("[H] re-running both builds on the 25 Sep curve (insight_v1's date) ...")
with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    subprocess.run([PY, str(ROOT / "rab/models/m2_rate_paths.py"), "--curve-date", "2026-09-25", "--no-figs", "--out",
                    str(td / "p")], check=True, capture_output=True, cwd=ROOT)
    subprocess.run([PY, str(ROOT / "rab/verification/blind/m2_blind.py"), "--curve-date", "2026-09-25", "--out",
                    str(td / "b")], check=True, capture_output=True, cwd=ROOT)
    P25 = json.load(open(td / "p" / "m2_results.json"))
    B25 = json.load(open(td / "b" / "results.json"))
P25H = {(r["shift_bp"], r["five_year"]): r for r in P25["h13_h14"]}
B25H = B25["H13_recheck"]["results"]

# ---------------------------------------------------------------------------------------------------------------- [X] added 30 Sep re-check
# (a) 4 Jan purchase: the blind reports a five-estimator 4 Jan median; the primary only ran E1 on 4 Jan. Rerun the
#     primary's own code with A = 2027-01-04 (in memory; primary_4jan_variant.py), at the spec's n_h = 65 and strict 64.
say("[X] re-running the primary build with the purchase on Mon 4 Jan 2027 (n_h 64 and 65) ...")
with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    P4 = {}
    for n in (64, 65):
        cmd = [PY, str(HERE / "primary_4jan_variant.py"), str(td / f"p{n}")] + (["--n-h", "65"] if n == 65 else [])
        subprocess.run(cmd, check=True, capture_output=True, cwd=ROOT)
        P4[n] = json.load(open(td / f"p{n}" / "m2_results.json"))
assert P4[64]["meta"]["n_h"] == 64 and P4[65]["meta"]["n_h"] == 65
# (b) primary functions for keys the primary does not publish (PV today, 2033 rung cost): load the primary module
_spec_p = importlib.util.spec_from_file_location("m2_primary", ROOT / "rab/models/m2_rate_paths.py")
PM = importlib.util.module_from_spec(_spec_p)
_spec_p.loader.exec_module(PM)
_D, _A = dt.date(2026, 9, 28), dt.date(2027, 1, 1)
_R = PM.to_par12(PM.read_treasury()[_D])[None, :]
P_PV_TODAY = float(PM.rungs_rw(_R, _D).sum())
P_RUNG2033 = float(PM.rungs_rw(_R, _A)[0, 0])
# (c) the blind builder's standard-library third pricer (rab/verification/blind/deterministic_check.py, commit 97c3467)
DC = json.load(open(ROOT / "rab/verification/blind/deterministic_check.json"))

# ---------------------------------------------------------------------------------------------------------------- [T] table
# kind -> tolerance rule.  decision = the number feeds a decision or a quoted figure (vs supporting / reconciliation).
ROWS = []


def add(key, what, pv, bv, kind, decision, note=""):
    ROWS.append({"key": key, "what": what, "primary": pv, "blind": bv, "kind": kind, "decision": decision, "note": note})


add("laura.rates.gap_odds_2027", "HEADLINE P(cost > $300k on 1 Jan 2027), median E1-E5", P["headline"]["P_gap"],
    Bl["headline"]["P_ladder_cost_gt_300k_on_1jan2027"], "prob", True)
add("gap_odds_range_min", "E2 similar-level history (range low end)", P["headline"]["range"][0], Bl["headline"]["range_min"], "prob", True)
add("  E2 90% bootstrap low", "moving-block bootstrap, 1,000 reps", pest(1)["P_lo90"], BE["E2_history_similar_level"]["P_gap_gt_0_ci90_blockboot"][0], "prob", False,
    "rng seeding differs (see P3)")
add("  E2 90% bootstrap high", "", pest(1)["P_hi90"], BE["E2_history_similar_level"]["P_gap_gt_0_ci90_blockboot"][1], "prob", False, "rng seeding differs (see P3)")
add("gap_odds_range_max", "E1 history rescaled (range high end)", P["headline"]["range"][1], Bl["headline"]["range_max"], "prob", True)
add("  E1 90% bootstrap low", "", pest(0)["P_lo90"], BE["E1_history_rescaled"]["P_gap_gt_0_ci90_blockboot"][0], "prob", False)
add("  E1 90% bootstrap high", "", pest(0)["P_hi90"], BE["E1_history_rescaled"]["P_gap_gt_0_ci90_blockboot"][1], "prob", False)
add("E3_vasicek_1962", "E3 Vasicek AR(1), parameter uncertainty", pest(2)["P_gap"], BE["E3_vasicek_ar1"]["P_gap_gt_0"], "prob", True,
    "same seed and draw order -> identical draws")
add("  E3 plug-in (OLS)", "", P["vasicek"][0]["P_plugin_ols"], BE["E3_vasicek_ar1"]["fits"][0]["plugin_P_hat"], "prob", False)
add("  E3 plug-in (bias-corrected)", "", P["vasicek"][0]["P_plugin_bc"], BE["E3_vasicek_ar1"]["fits"][0]["plugin_P_bc"], "prob", False)
add("  E3 share of draws at phi = 1", "", pest(2)["share_draws_random_walk"], BE["E3_vasicek_ar1"]["share_draws_random_walk"], "prob", False)
add("E4_pca_var_1990", "E4 PCA + VAR(1)", pest(3)["P_gap"], BE["E4_pca_var"]["P_gap_gt_0"], "prob", True,
    "different normal samplers -> Monte Carlo noise (see P2)")
for j in range(3):
    add(f"  E4 PCA share {j + 1}", "", P["pca_var"]["variance_shares"][j], BE["E4_pca_var"]["pca_variance_shares"][j], "pca", False)
add("  E4 without mean reversion", "E4-RW sensitivity", psens("E4-RW")["P_gap"], BE["E4_pca_var"]["random_walk_variant"]["P_gap_gt_0"], "prob", False,
    "Monte Carlo noise")
add("E5_move_calibrated", "E5 MOVE-calibrated", pest(4)["P_gap"], BE["E5_move_options"]["P_gap_gt_0"], "prob", True,
    "same seed -> identical draws; closed form 32.69%")
add("  MOVE on 28 Sep", "", P["move"]["move_D"], BE["E5_move_options"]["MOVE_D"], "exact", False)
add("  rho = median RV / MOVE", "", P["move"]["rho_median"], BE["E5_move_options"]["rho_median"], "rel2", False)
add("  E5 with MOVE 63-day average", "sensitivity", psens("E5-avg63")["P_gap"], BE["E5_move_options"]["variants"]["move_63d_mean_x_rho"]["P_gap_gt_0"], "prob", False)
add("cost_2027_yields_unchanged", "Cost_RW(R), 1 Jan 2027", P["base"]["cost_rw"], Bl["deterministic"]["cost_rw_R_usd"], "usd_det", True)
add("  Cost_FWD(R) (numbers.yaml $292,418.11)", "", P["base"]["cost_fwd"], Bl["deterministic"]["cost_fwd_R_usd"], "usd_det", True)
add("breakeven_fall_bp_yields_unchanged", "RW break-even parallel fall", P["base"]["breakeven_fall_bp_rw"], Bl["deterministic"]["breakeven_fall_bp_rw"], "bp_det", True)
add("  FWD break-even (numbers.yaml 26.2bp)", "", P["base"]["breakeven_fall_bp_fwd"], Bl["deterministic"]["breakeven_fall_bp_fwd"], "bp_det", True)
R1b = Bl["reconciliation"]["R1_D1_lognormal_25sep"]
R2b = Bl["reconciliation"]["R2_D1_lognormal_28sep"]
R5b = Bl["reconciliation"]["R5_lognormal_28sep_RW_centre"]
add("recon_R1_insight_v1_25sep", "D1 [6] lognormal, 25 Sep (blind spec reading)", prow("R1")["P"], R1b["P"], "prob", False,
    "valuation-date convention (C1)")
add("  R1, blind same convention as primary", "each row's curve valued on its own date", prow("R1")["P"], R1b["variant_moving_valuation"]["P"], "prob", False)
add("recon_R2_D1_28sep", "D1 [6] lognormal, 28 Sep (blind spec reading)", prow("R2 ")["P"], R2b["P"], "prob", False, "valuation-date convention (C1)")
add("  R2, blind same convention as primary", "", prow("R2 ")["P"], R2b["variant_moving_valuation"]["P"], "prob", False)
add("recon_R5_no_view_centre_2026_vol", "R2 with yields-unchanged centre (blind spec reading)", prow("R5")["P"], R5b["P"], "prob", False,
    "valuation-date convention (C1)")
add("  R5, blind same convention as primary", "", prow("R5")["P"], R5b["variant_moving_valuation"]["P"], "prob", False)
ax = prow("R4")["detail"]
R4b = Bl["reconciliation"]["R4_AX1b_dgs10_68day_windows"]
for yr in (1962, 1990, 2000):
    add(f"recon_AX1b_26bp_since{yr}" if yr == 1962 else f"  AX1b 26bp since {yr}", "DGS10 fell >= 26bp in 68 trading days (blind <=)",
        ax[f"insight_v1 file since {yr} >= 26bp"], R4b[f"fell_ge_26bp_since_{yr}"]["share_le"], "prob", False, "float ties at exactly -26bp (C2)")
for yr in (1962, 1990, 2000):
    add(f"  AX1b 19bp since {yr}", "(25 Sep headroom; H5 history 32-36%)", ax[f"insight_v1 file since {yr} >= 19bp"],
        R4b[f"fell_ge_19bp_since_{yr}"]["share_le"], "prob", False, "float ties (C2)")
add("m2_on_25sep_curve", "M2 headline rerun on the 25 Sep curve", P25["headline"]["P_gap"], B25["headline"]["P_ladder_cost_gt_300k_on_1jan2027"], "prob", False,
    "both builds rerun here")
for i, k in enumerate(["E1_history_rescaled", "E2_history_similar_level", "E3_vasicek_ar1", "E4_pca_var", "E5_move_options"]):
    add(f"  25 Sep E{i + 1}", "", P25["estimators"][i]["P_gap"], B25["estimators"][k]["P_gap_gt_0"], "prob", False)
add("gap_if_any_typical", "median over E1-E5 of mean gap given a gap", P["headline"]["median_mean_gap_given_gap"], float(np.median(bmean_gaps)), "usd", True)
add("  median gap p95", "", P["headline"]["median_gap_p95"], float(np.median(bp95)), "usd", True)
add("  E4 mean gap given a gap", "only MC-noisy per-estimator dollar row", pest(3)["mean_gap_given_gap"], BE["E4_pca_var"]["mean_gap_given_pos_usd"], "usd", False)
add("  E4 gap p95", "", pest(3)["gap_p95"], BE["E4_pca_var"]["gap_p95_usd"], "usd", False)
add("  E4 cost p50", "", pest(3)["cost_p50"], BE["E4_pca_var"]["cost_p50_usd"], "usd", False)
add("P_whole_payment_waits_max", "max over E1-E5 of P(gap > own 2033 rung)", P["headline"]["max_P_whole_payment_waits"], float(max(bwaits)), "prob", True)
for v in ("H-FHS", "H-LVL", "H-RAW"):
    tag = "stock_fund_2028_median" if v == "H-LVL" else f"  2028 fund median {v}"
    add(tag, f"stock fund p50 on 1 Jan 2028, {v}", PF[v]["fund_p50"], BF[v]["S_p50"], "usd", True)
for v in ("H-FHS", "H-LVL", "H-RAW"):
    add(f"  2028 fund p5 {v}", "", PF[v]["fund_p5"], BF[v]["S_p5"], "usd", False)
add("  2028 fund base, FWD (numbers.yaml $40,736)", "", P["fifteen_months"]["base_fwd_fund"], BF["check_base_fwd"]["S_usd"], "usd_det", True)
add("  2028 floor base (numbers.yaml $117,194)", "", P["fifteen_months"]["base_fwd_floor"], BF["check_base_fwd"]["F_usd"], "usd_det", True)
add("  2028 fund base, RW", "", P["fifteen_months"]["base_rw"]["fund_p50"], BF["base_rw"]["S_usd"], "usd_det", False)
pl20 = [PF[v]["P_fund_lt_20k"] for v in ("H-FHS", "H-LVL", "H-RAW")]
bl20 = [BF[v]["P_S_lt_20k"] for v in ("H-FHS", "H-LVL", "H-RAW")]
add("P_stock_fund_below_20k_2028", "median over the three variants of P(fund < $20k)", float(np.median(pl20)), float(np.median(bl20)), "prob", True)
for v in ("H-FHS", "H-LVL", "H-RAW"):
    add(f"  P(fund < $20k) {v}", "", PF[v]["P_fund_lt_20k"], BF[v]["P_S_lt_20k"], "prob", False)
    add(f"  P(no fund) {v}", "", PF[v]["P_fund_zero"], BF[v]["P_S_eq_0"], "prob", False)
    add(f"  P(top-up) {v}", "", PF[v]["P_topup"], BF[v]["P_T_gt_0"], "prob", False)
for b in (-50, -100, -150):
    bb = BH[f"{b}bp"]
    for lab5, tag in (("5y unchanged", "y5_unchanged"), ("5y also lower", "y5_shifted")):
        key = "H13_fund_minus100bp_low" if (b == -100 and tag == "y5_shifted") else f"  H13 fund {b}bp, {lab5}"
        add(key, "", PH[(b, lab5)]["stock_fund"], bb[tag]["stock_fund_usd"], "usd_det", True)
        if b == -150:
            add(f"  H13 floor face {b}bp, {lab5}", "", PH[(b, lab5)]["floor_face"], bb[tag]["floor_face_usd"], "usd_det", True)
    add(f"  H13 top-up Jan 2028 {b}bp", "", PH[(b, "5y unchanged")]["topup_2028"], bb["topup_on_B_usd"], "usd_det", False)
add("H14_unfunded_2033_minus50bp", "no 2028 deposit, -50bp", PH[(-50, "5y unchanged")]["unfunded_2033_if_no_deposit"],
    Bl["H14_recheck"]["-50bp"]["unfunded_2033_usd"], "usd_det", True)
add("  H14 -100bp", "", PH[(-100, "5y unchanged")]["unfunded_2033_if_no_deposit"], Bl["H14_recheck"]["-100bp"]["unfunded_2033_usd"], "usd_det", True)
bf = Bl["estimators"]["E3_vasicek_ar1"]["fits"]
for i, lab in enumerate(("1962+", "1990+", "2000+")):
    add("vasicek_theta_1962_vs_2000" if i == 0 else f"  Vasicek theta {lab}", "long-run level, %", P["vasicek"][i]["theta_pct"], bf[i]["theta_pct"], "theta", False)
    add(f"  Vasicek kappa_bc {lab}", "per year", P["vasicek"][i]["kappa_bc_per_yr"], bf[i]["vasicek_bc"]["kappa_per_yr"], "kappa", False)
    add(f"  ADF p-value {lab}", "", P["vasicek"][i]["adf_pvalue"], bf[i]["adf_pvalue"], "prob", False)
add("ewma_vol_today", "EWMA ladder-yield vol at D, bp/yr", P["panel"]["ewma_vol_today_bp_yr"], Bl["ladder_yield"]["sigma_D_bp_per_year"], "rel2", False)
add("  1962-2026 vol (E3 residual sd), bp/yr", "", P["vasicek"][0]["sigma_bp_yr"], bf[0]["sigma_bp_per_yr"], "rel2", False)
add("  E5 horizon sd sigma_h, bp", "", P["move"]["sigma_h_bp"], BE["E5_move_options"]["sigma_h_bp"], "rel2", False)
add("  E1, purchase Mon 4 Jan 2027", "sensitivity", psens("S-E1-4Jan")["P_gap"], Bl["sensitivities"]["purchase_4jan2027"]["per_estimator"]["E1"], "prob", False)
# ---- [X] rows added at the 30 Sep re-check: blind headline keys first reported in 97c3467, and quoted sub-values
s4b = Bl["sensitivities"]["purchase_4jan2027"]
add("sensitivity_purchase_4jan2027_median", "median E1-E5, purchase 4 Jan; primary code rerun at the spec's n_h = 65",
    P4[65]["headline"]["P_gap"], s4b["P_median"], "prob", False, "primary rerun via primary_4jan_variant.py")
add("  4 Jan median, primary at strict n_h = 64", "1 Jan 2027 is a holiday: spec erratum", P4[64]["headline"]["P_gap"], s4b["P_median"],
    "prob", False, "n_h 64 vs 65 (spec erratum)")
for e in ("E2", "E3", "E4", "E5"):
    add(f"  4 Jan {e} (n_h = 65)", "", P4[65]["headline"]["estimators"][e], s4b["per_estimator"][e], "prob", False,
        {"E4": "Monte Carlo noise (samplers)", "E5": "rho over 98-day vs 95-day windows"}.get(e, ""))
add("  4 Jan Cost_RW(R)", "", P4[65]["base"]["cost_rw"], s4b["cost_rw_R_usd"], "usd_det", False)
add("  4 Jan RW break-even", "", P4[65]["base"]["breakeven_fall_bp_rw"], s4b["breakeven_fall_bp_rw"], "bp_det", False)
add("pv_today_R_usd", "PV of the ten payments on 28 Sep (numbers.yaml Gate A $289,119.20)", P_PV_TODAY, Bl["deterministic"]["pv_today_R_usd"],
    "usd_det", True, "primary value from its own rungs_rw(R, D)")
add("  2033 rung cost at R, 1 Jan 2027, yields unchanged", "threshold for 'a whole payment waits'", P_RUNG2033,
    Bl["deterministic"]["rung_costs_rw_R_usd"]["2033"], "usd_det", False)
add("  ladder yield today", "percent", P["panel"]["ladder_yield_today_pct"], Bl["ladder_yield"]["y_D_pct"], "pct_det", False)
add("  d ladder yield / d parallel shift", "", P["panel"]["dy_per_parallel_shift"], Bl["ladder_yield"]["dy_db_at_R"], "rel2", False)
add("  median P(gap > $10k)", "median over E1-E5", P["headline"]["median_P_gap_gt_10k"],
    float(np.median([BE[k]["P_gap_gt_10k"] for k in BE])), "prob", False)
add("  R3 strategy_mc_v2 (a), 25 Sep, analytic", "insight_v1 printed 30.2% (Monte Carlo)", prow("R3 ")["P"],
    Bl["reconciliation"]["R3_strategy_mc_v2_parallel_37bp"]["P_25sep_analytic"], "prob", False)
add("  R3' same on 28 Sep", "", prow("R3'")["P"], Bl["reconciliation"]["R3_strategy_mc_v2_parallel_37bp"]["P_28sep_analytic"], "prob", False)
add("  E1 windows (95-day)", "count", pest(0)["n_scenarios"], Bl["windows"]["count"], "exact", False)
add("  E1 non-overlapping windows", "count", pest(0)["n_indep"], Bl["windows"]["n_nonoverlapping"], "exact", False)
add("  E2 windows (10y 4.0-6.5%)", "count", pest(1)["n_scenarios"], BE["E2_history_similar_level"]["n_scenarios"], "exact", False)
add("  15-month windows", "count", PF["H-RAW"]["n_windows"], BF["H-RAW"]["n"], "exact", False)
for v in ("H-FHS", "H-LVL", "H-RAW"):
    add(f"  2028 mean top-up if any {v}", "", PF[v]["mean_topup_given_topup"], BF[v]["mean_T_given_pos"], "usd", False)

TOL = {"prob": 0.02, "pca": 0.005, "theta": 0.05, "kappa": 0.02, "usd_det": 1.0, "bp_det": 0.01, "exact": 1e-9, "pct_det": 1e-4}


def verdict(r):
    p, b, k = r["primary"], r["blind"], r["kind"]
    d = b - p
    r["diff"] = d
    if k == "usd":
        tol = min(0.02 * abs(p), 500.0)
        r["tol"] = f"min(2%, $500) = ${tol:,.0f}"
    elif k == "rel2":
        tol = 0.02 * abs(p)
        r["tol"] = "2%"
    else:
        tol = TOL[k]
        r["tol"] = {"prob": "2pp", "pca": "0.5pt", "theta": "5bp", "kappa": "0.02/yr", "usd_det": "$1", "bp_det": "0.01bp",
                    "exact": "exact", "pct_det": "0.01bp"}[k]
    ok = abs(d) <= tol
    same = abs(d) <= {"usd_det": 0.005, "bp_det": 1e-4, "pct_det": 1e-8}.get(k, 1e-9) or (k in ("prob",) and abs(d) < 5e-7)
    r["verdict"] = ("MATCH" if same else "WITHIN TOL") if ok else "UNRECONCILED"
    return r


for r in ROWS:
    verdict(r)


def fmt(v, k):
    if k in ("prob", "pca"):
        return f"{100 * v:.2f}%"
    if k in ("usd", "usd_det"):
        return f"${v:,.2f}" if k == "usd_det" else f"${v:,.0f}"
    if k == "bp_det":
        return f"{v:.3f}bp"
    if k == "theta":
        return f"{v:.3f}%"
    if k == "kappa":
        return f"{v:.4f}"
    if k == "pct_det":
        return f"{v:.4f}%"
    if k == "exact" and float(v).is_integer():
        return f"{int(v):,}"
    return f"{v:.4g}"


def fdiff(d, k):
    if k in ("prob", "pca"):
        return f"{100 * d:+.2f}pp"
    if k == "usd_det":
        return f"{d:+.2f}"
    if k == "usd":
        return f"{d:+,.0f}"
    if k == "bp_det":
        return f"{d:+.4f}bp"
    if k in ("theta", "pct_det"):
        return f"{100 * d:+.2f}bp" if k == "theta" else f"{100 * d:+.4f}bp"
    return f"{d:+.3g}"


with open(HERE / "gateB_ws4_table.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["key", "what", "primary", "blind", "diff", "tolerance", "verdict", "decision_relevant", "note"])
    for r in ROWS:
        w.writerow([r["key"].strip(), r["what"], repr(r["primary"]), repr(r["blind"]), repr(r["diff"]), r["tol"], r["verdict"],
                    r["decision"], r["note"]])
md = ["| Key | Primary | Blind | Diff | Tol | Verdict |", "|---|---|---|---|---|---|"]
for r in ROWS:
    key = r["key"].strip()
    key = f"`{key}`" if not r["key"].startswith("  ") else f"&nbsp;&nbsp;{key}"
    md.append(f"| {key}{' (D)' if r['decision'] else ''} | {fmt(r['primary'], r['kind'])} | {fmt(r['blind'], r['kind'])} | "
              f"{fdiff(r['diff'], r['kind'])} | {r['tol']} | {r['verdict']} |")
(HERE / "gateB_ws4_table.md").write_text("\n".join(md) + "\n")
n_unrec = sum(r["verdict"] == "UNRECONCILED" for r in ROWS)
OUT["table"] = {"n_rows": len(ROWS), "n_decision": sum(r["decision"] for r in ROWS),
                "n_match": sum(r["verdict"] == "MATCH" for r in ROWS), "n_within_tol": sum(r["verdict"] == "WITHIN TOL" for r in ROWS),
                "n_unreconciled": n_unrec,
                "max_abs_prob_diff_pp": max(100 * abs(r["diff"]) for r in ROWS if r["kind"] == "prob"),
                "max_abs_prob_diff_decision_pp": max(100 * abs(r["diff"]) for r in ROWS if r["kind"] == "prob" and r["decision"]),
                "max_abs_usd_det_diff": max(abs(r["diff"]) for r in ROWS if r["kind"] == "usd_det")}
say(f"[T] {len(ROWS)} rows: {OUT['table']['n_match']} MATCH, {OUT['table']['n_within_tol']} WITHIN TOL, {n_unrec} UNRECONCILED; "
    f"max prob diff {OUT['table']['max_abs_prob_diff_pp']:.2f}pp (decision keys {OUT['table']['max_abs_prob_diff_decision_pp']:.3f}pp); "
    f"max deterministic $ diff {OUT['table']['max_abs_usd_det_diff']:.4f}")

# ---------------------------------------------------------------------------------------------------------------- [P] precision
D = dt.date(2026, 9, 28)
A = dt.date(2027, 1, 1)
n_h = Bl["meta"]["n_h_business_days"]
be_rw = Bl["deterministic"]["breakeven_fall_bp_rw"]
bstar = -be_rw / 100.0
prec = {}
# P1 E5 closed form: parallel shift b ~ N(0, sigma_h^2); cost falls as b rises, so P = Phi(-be_rw / sigma_h)
sh = BE["E5_move_options"]["sigma_h_bp"]
prec["E5_closed_form"] = float(norm.cdf(-be_rw / sh))
prec["E5_mc_100k"] = BE["E5_move_options"]["P_gap_gt_0"]
# P1 E3 Rao-Blackwellised: P = E over parameter draws of Phi((b* - m) / sqrt(v))
f0 = bf[0]
yD = Bl["ladder_yield"]["y_D_pct"]
s_e2 = f0["s_e_pct_per_step"] ** 2
cov = np.array(f0["cov_params"])
rb = []
for i in range(4):
    rng = np.random.default_rng([SEED, 300 + i])
    th = rng.multivariate_normal([f0["c_bc"], f0["phi_bc"]], cov, size=500_000)
    c, ph = th[:, 0].copy(), th[:, 1].copy()
    rw = ph >= 1
    ph[rw], c[rw] = 1.0, 0.0
    with np.errstate(divide="ignore", invalid="ignore"):
        m = np.where(rw, 0.0, (c - (1 - ph) * yD) * (1 - ph ** n_h) / (1 - ph))
        v = np.where(rw, n_h * s_e2, s_e2 * (1 - ph ** (2 * n_h)) / (1 - ph ** 2))
    rb.append(float(norm.cdf((bstar - m) / np.sqrt(v)).mean()))
prec["E3_rao_blackwell_2M"] = float(np.mean(rb))
prec["E3_rao_blackwell_chunks"] = rb
prec["E3_mc_100k"] = BE["E3_vasicek_ar1"]["P_gap_gt_0"]
# P2 E4 with both samplers, 20 x 200,000 draws each (4,000,000 per sampler)
dates, P12, _, _ = B.build_panel(D)
iD = int(np.searchsorted(dates, np.datetime64(D)))
R = P12[iD].copy()
m90 = dates >= np.datetime64("1990-01-02")
Y = P12[m90] @ B.W_K.T
dY = np.diff(Y, axis=0)
w_, V_ = np.linalg.eigh(np.cov(dY, rowvar=False, ddof=1))
o_ = np.argsort(w_)[::-1]
L = V_[:, o_][:, :3]
Yb = Y.mean(axis=0)
F = (Y - Yb) @ L
U = (Y - Yb) - F @ L.T
from statsmodels.tsa.api import VAR  # noqa: E402

var = VAR(F).fit(1, trend="c")
mu = var.forecast(F[-1:], n_h)[-1]
S = var.forecast_cov(n_h)[-1]
CU = n_h * np.cov(np.diff(U, axis=0), rowvar=False, ddof=1)
e4 = {"svd_numpy": [], "eigh_blind": []}
for i in range(20):
    for tag in e4:
        rng = np.random.default_rng([SEED, 400 + i])
        if tag == "svd_numpy":
            Fh = rng.multivariate_normal(mu, S, size=200_000)
            dU = rng.multivariate_normal(np.zeros(10), CU, size=200_000, method="eigh")
        else:
            Fh = B.mvn_draw(rng, mu, S, 200_000)
            dU = B.mvn_draw(rng, np.zeros(10), CU, 200_000)
        DK = (Fh - F[-1]) @ L.T + dU
        cst = B.cost_rw(R[None, :] + DK[:, B.E4_TO_12], A)
        e4[tag].append(float((cst > 300_000).mean()))
prec["E4_4M_by_sampler"] = {k: {"mean": float(np.mean(v)), "se": float(np.std(v, ddof=1) / math.sqrt(len(v))),
                                "chunk_sd": float(np.std(v, ddof=1)), "binomial_chunk_sd": float(math.sqrt(np.mean(v) * (1 - np.mean(v)) / 200_000)), "chunks": v}
                            for k, v in e4.items()}
prec["E4_8M_pooled"] = float(np.mean(e4["svd_numpy"] + e4["eigh_blind"]))
prec["E4_mc_100k"] = {"primary": pest(3)["P_gap"], "blind": BE["E4_pca_var"]["P_gap_gt_0"],
                      "se_one_run": float(math.sqrt(0.322 * 0.678 / 100_000))}
e1, e2 = Bl["headline"]["range_max"], Bl["headline"]["range_min"]
nf = [e1, e2, prec["E3_rao_blackwell_2M"], prec["E4_8M_pooled"], prec["E5_closed_form"]]
prec["noise_free_estimators"] = dict(zip(["E1", "E2", "E3", "E4", "E5"], nf))
prec["noise_free_headline"] = float(np.median(nf))
prec["reported_headline"] = P["headline"]["P_gap"]
rep = [P["headline"]["estimators"][k] for k in ("E1", "E2", "E3", "E4", "E5")]
prec["leave_one_out_median"] = {f"without_E{i + 1}": float(np.median([x for j, x in enumerate(rep) if j != i])) for i in range(5)}
# 4 Jan sensitivity: spec s2 says n_h = 65, but Fri 1 Jan 2027 is a bond-market holiday, so a strict count is 64
s4j = Bl["sensitivities"]["purchase_4jan2027"]
sig_yr = BE["E5_move_options"]["rho_median"] * BE["E5_move_options"]["MOVE_D"]
prec["E5_4jan_closed_form"] = {f"n_h_{n}": float(norm.cdf(-s4j["breakeven_fall_bp_rw"] / (sig_yr * math.sqrt(n / 252)))) for n in (64, 65)}
say(f"[P] E5 closed form {prec['E5_closed_form']:.4%} (MC {prec['E5_mc_100k']:.4%}); E3 RB {prec['E3_rao_blackwell_2M']:.4%} "
    f"(MC {prec['E3_mc_100k']:.4%}); E4 4M svd {prec['E4_4M_by_sampler']['svd_numpy']['mean']:.4%} / eigh "
    f"{prec['E4_4M_by_sampler']['eigh_blind']['mean']:.4%}; noise-free headline {prec['noise_free_headline']:.4%}")
# P3 bootstrap interval spread (primary's re-seeded bootstrap, 50 seeds) using the committed window indicators
c1, c2 = [], []
for r in csv.DictReader(open(HIST_CSV)):
    c1.append(float(r["cost_E1"]))
    if r["cost_E2"]:
        c2.append(float(r["cost_E2"]))
ind = {"E1": (np.array(c1) > 300_000).astype(float), "E2": (np.array(c2) > 300_000).astype(float)}
assert abs(ind["E1"].mean() - e1) < 1e-12 and abs(ind["E2"].mean() - e2) < 1e-12
bs = {}
for tag, x in ind.items():
    n = len(x)
    nb = math.ceil(n / n_h)
    los, his = [], []
    for sd in range(50):
        rng = np.random.default_rng([SEED, 900 + sd])
        st = rng.integers(0, n - n_h + 1, size=(1000, nb))
        idx = (st[:, :, None] + np.arange(n_h)[None, None, :]).reshape(1000, -1)[:, :n]
        ps = x[idx].mean(axis=1)
        los.append(np.percentile(ps, 5))
        his.append(np.percentile(ps, 95))
    bs[tag] = {"lo_mean": float(np.mean(los)), "lo_sd": float(np.std(los, ddof=1)), "lo_min": float(np.min(los)), "lo_max": float(np.max(los)),
               "hi_mean": float(np.mean(his)), "hi_sd": float(np.std(his, ddof=1)), "hi_min": float(np.min(his)), "hi_max": float(np.max(his))}
prec["bootstrap_interval_spread_50_seeds"] = bs
say(f"[P] E2 bootstrap endpoints over 50 seeds: low {bs['E2']['lo_min']:.1%}-{bs['E2']['lo_max']:.1%}, high "
    f"{bs['E2']['hi_min']:.1%}-{bs['E2']['hi_max']:.1%}")
OUT["precision"] = prec

# ---------------------------------------------------------------------------------------------------------------- [C] causes
causes = {}
# C1 valuation convention in D1 [6]: insight_v1 values each 2026 row's curve from that row's own date
d1_src = (ROOT / "research/insight_v1/scripts/D1_purchase_rule.py").read_text().splitlines()
causes["C1_D1_curve_valuation_line"] = next(f"D1_purchase_rule.py:{i + 1}: {ln.strip()}" for i, ln in enumerate(d1_src)
                                            if 'v = row["_date"]' in ln)
causes["C1_values"] = {"R1": {"primary": prow("R1")["P"], "blind_fixed": R1b["P"], "blind_own_date": R1b["variant_moving_valuation"]["P"],
                              "insight_v1_printed": 0.305},
                       "R2": {"primary": prow("R2 ")["P"], "blind_fixed": R2b["P"], "blind_own_date": R2b["variant_moving_valuation"]["P"],
                              "insight_v1_printed": 0.242},
                       "R5": {"primary": prow("R5")["P"], "blind_fixed": R5b["P"], "blind_own_date": R5b["variant_moving_valuation"]["P"]}}
# C2 AX1b float ties
ax_src = (ROOT / "research/insight_v1/scripts/AX1b_rates_audit.py").read_text().splitlines()
causes["C2_AX1b_comparison_line"] = next(f"AX1b_rates_audit.py:{i + 1}: {ln.strip()}" for i, ln in enumerate(ax_src)
                                         if "cc <= -x / 100" in ln)
ds, ys = [], []
for r in csv.DictReader(open(ROOT / "research/insight_v1/scripts/data/D3/fred_DGS10.csv")):
    if r["DGS10"] not in ("", "."):
        ds.append(dt.date.fromisoformat(r["observation_date"]))
        ys.append(float(r["DGS10"]))
ys, ds = np.array(ys), np.array(ds)
chg, start = ys[68:] - ys[:-68], ds[:-68]
ties = {}
for yr in (1962, 1990, 2000):
    mk = start >= dt.date(yr, 1, 1)
    cc = chg[mk]
    for x in (19, 26):
        tie = np.abs(cc + x / 100) < 1e-9
        ties[f"{x}bp_since_{yr}"] = {"windows": int(mk.sum()), "exact_ties": int(tie.sum()),
                                     "ties_counted_by_raw_float_le": int((tie & (cc <= -x / 100)).sum()),
                                     "share_raw_float_le": float((cc <= -x / 100).mean()),
                                     "share_inclusive_bp_rounded": float((np.round(cc * 100) <= -x).mean()),
                                     "share_strict": float((np.round(cc * 100) < -x).mean())}
causes["C2_ties"] = ties
say(f"[C] AX1b 26bp since 1962: {ties['26bp_since_1962']['exact_ties']} exact ties, raw float counts "
    f"{ties['26bp_since_1962']['ties_counted_by_raw_float_le']}; shares raw {ties['26bp_since_1962']['share_raw_float_le']:.4%} / "
    f"inclusive {ties['26bp_since_1962']['share_inclusive_bp_rounded']:.4%} / strict {ties['26bp_since_1962']['share_strict']:.4%}")
OUT["causes"] = causes

# ---------------------------------------------------------------------------------------------------------------- [H] insight_v1
hv = {}
A25 = dt.date(2026, 9, 25)
t25 = (A - A25).days / 365.25
c25 = R1b["cost_fwd_25sep_usd"]
be25 = Bl["reconciliation"]["R3_strategy_mc_v2_parallel_37bp"]["breakeven_fall_bp_25sep_fwd"]
hv["H5_components_25sep"] = {
    "D1_6_lognormal_vol_7.16": {"printed": 0.305, "primary": prow("R1")["P"], "blind_own_date": R1b["variant_moving_valuation"]["P"]},
    "S4_red_team_vol_7.24": {"printed": 0.307, "rebuilt": float(1 - norm.cdf(math.log(300_000 / c25) / (0.0724 * math.sqrt(t25))))},
    "strategy_mc_v2_sd_37bp": {"printed": 0.302, "analytic": float(norm.cdf(-be25 / 37.0))},
    "strategy_mc_v2_sd_48bp": {"printed": 0.344, "analytic": float(norm.cdf(-be25 / 48.0))},
    "AX1b_19bp_1962_1990_2000": {"printed": "31.8 / 36.1 / 34.0%", "primary": [ax[f"insight_v1 file since {y} >= 19bp"] for y in (1962, 1990, 2000)],
                                 "blind_inclusive": [R4b[f"fell_ge_19bp_since_{y}"]["share_le"] for y in (1962, 1990, 2000)]},
    "M2_method_25sep": {"primary": P25["headline"]["P_gap"], "blind": B25["headline"]["P_ladder_cost_gt_300k_on_1jan2027"],
                        "range_primary": P25["headline"]["range"],
                        "cost_rw_25sep": P25["base"]["cost_rw"], "breakeven_rw_25sep_bp": P25["base"]["breakeven_fall_bp_rw"]},
}
# H6 exact-date 18.7% rebuilt with the blind's curve engine (each 2026 row valued on its own date, as D1)
exact_mats = [dt.date(y, 1, 1) for y in B.PAY_YEARS]
m26 = dates >= np.datetime64("2026-01-01")
rows26 = P12[m26]
d26 = list(dates[m26].astype(object))
ce = np.array([B.rung_costs_fwd(rows26[i][None, :], d26[i], A, mats=exact_mats).sum() for i in range(len(d26))])
cn = np.array([B.rung_costs_fwd(rows26[i][None, :], d26[i], A).sum() for i in range(len(d26))])
vol_e = float(np.std(np.diff(np.log(ce)), ddof=1) * math.sqrt(252))
tD = (A - D).days / 365.25
hv["H6_28sep"] = {"model_nov15": {"printed": 0.242, "primary": prow("R2 ")["P"], "blind_own_date": R2b["variant_moving_valuation"]["P"]},
                  "model_exact": {"printed": 0.187, "primary": prow("R2e")["P"],
                                  "rebuilt_blind_engine": float(1 - norm.cdf(math.log(300_000 / ce[-1]) / (vol_e * math.sqrt(tD)))),
                                  "cost_exact_fwd": float(ce[-1]), "vol": vol_e},
                  "history_26bp": {"printed": [0.276, 0.311], "primary": [ax["insight_v1 file since 1962 >= 26bp"], ax["insight_v1 file since 1990 >= 26bp"]]}}
# H7 days of 2026 with the ladder over $300k (Nov-15 and exact), to 25 Sep (insight_v1) and to 28 Sep
upto25 = np.array([d <= A25 for d in d26])
hv["H7_days_over_300k_2026"] = {"printed": {"exact": "173/185", "nov15": "176/185", "worst": "27 Feb 2026 $327,631"},
                                "rebuilt_to_25sep": {"exact": f"{int((ce[upto25] > 3e5).sum())}/{int(upto25.sum())}",
                                                     "nov15": f"{int((cn[upto25] > 3e5).sum())}/{int(upto25.sum())}",
                                                     "worst_nov15": [str(d26[int(np.argmax(cn))]), float(cn.max())]},
                                "rebuilt_to_28sep": {"exact": f"{int((ce > 3e5).sum())}/{len(ce)}", "nov15": f"{int((cn > 3e5).sum())}/{len(cn)}"},
                                "last_day_over_300k_nov15": str(d26[int(np.where(cn > 3e5)[0][-1])])}
hv["H13_25sep_vs_E6_8"] = {"E6_printed": {"-50bp": "fund $20-23k", "-100bp": "fund $1-7k", "-150bp": "no fund; floor $127-137k",
                                          "topups_hardcoded_in_E6": [9_555, 25_711, 42_633]},
                           "primary_25sep": {f"{r['shift_bp']} {r['five_year']}": {"topup": r["topup_2028"], "fund": r["stock_fund"], "face": r["floor_face"]}
                                             for r in P25["h13_h14"]},
                           "blind_25sep": {k: {"topup": v["topup_on_B_usd"], "fund_y5_unch": v["y5_unchanged"]["stock_fund_usd"],
                                               "fund_y5_shift": v["y5_shifted"]["stock_fund_usd"], "face_y5_unch": v["y5_unchanged"]["floor_face_usd"],
                                               "face_y5_shift": v["y5_shifted"]["floor_face_usd"]} for k, v in B25H.items()}}
hv["H14"] = {"printed_25sep": [11_957, 31_413], "printed_28sep": [9_281, 28_753],
             "primary_25sep": [P25H[(-50, "5y unchanged")]["unfunded_2033_if_no_deposit"], P25H[(-100, "5y unchanged")]["unfunded_2033_if_no_deposit"]],
             "blind_25sep": [B25["H14_recheck"]["-50bp"]["unfunded_2033_usd"], B25["H14_recheck"]["-100bp"]["unfunded_2033_usd"]],
             "primary_28sep": [PH[(-50, "5y unchanged")]["unfunded_2033_if_no_deposit"], PH[(-100, "5y unchanged")]["unfunded_2033_if_no_deposit"]],
             "blind_28sep": [Bl["H14_recheck"]["-50bp"]["unfunded_2033_usd"], Bl["H14_recheck"]["-100bp"]["unfunded_2033_usd"]]}
OUT["insight_v1"] = hv
say(f"[H] 25 Sep M2 headline: primary {P25['headline']['P_gap']:.4%}, blind {B25['headline']['P_ladder_cost_gt_300k_on_1jan2027']:.4%}; "
    f"S4 30.7% -> {hv['H5_components_25sep']['S4_red_team_vol_7.24']['rebuilt']:.4%}; sd48 -> "
    f"{hv['H5_components_25sep']['strategy_mc_v2_sd_48bp']['analytic']:.4%}; H6 exact -> {hv['H6_28sep']['model_exact']['rebuilt_blind_engine']:.4%}; "
    f"H7 to 25 Sep {hv['H7_days_over_300k_2026']['rebuilt_to_25sep']}; H14 25 Sep {hv['H14']['primary_25sep']}")
# inventory M2 row AX1b [B]: an "unchanged curve" drift adds about $1.0k to the January cost and lifts the odds ~3 points
hv["AX1b_B_unchanged_curve"] = {"printed": "about +$1.0k (inventory: +$1,044), +3.4 points (25 Sep)",
                                "primary_25sep_rw_minus_fwd_usd": P25["base"]["cost_rw"] - P25["base"]["cost_fwd"],
                                "primary_28sep_rw_minus_fwd_usd": P["base"]["cost_rw"] - P["base"]["cost_fwd"],
                                "primary_28sep_R5_minus_R2_pp": 100 * (prow("R5")["P"] - prow("R2 ")["P"])}
say(f"[H] AX1b [B] unchanged-curve drift: 25 Sep +${hv['AX1b_B_unchanged_curve']['primary_25sep_rw_minus_fwd_usd']:,.0f}, "
    f"28 Sep +${hv['AX1b_B_unchanged_curve']['primary_28sep_rw_minus_fwd_usd']:,.0f}; R5 - R2 = "
    f"{hv['AX1b_B_unchanged_curve']['primary_28sep_R5_minus_R2_pp']:+.2f}pp")
# Third session: the two inventory M2 figures s5 had not rebuilt. (a) D1 [6] 25 Sep exact-date basis, printed 24.3%.
# (b) AX1b [B] "+3.4 points" on 25 Sep: D1 [6]'s lognormal with the yields-unchanged centre instead of forwards.
t25_ = (A - A25).days / 365.25
vol_e25 = float(np.std(np.diff(np.log(ce[upto25])), ddof=1) * math.sqrt(252))
vol_n25 = float(np.std(np.diff(np.log(cn[upto25])), ddof=1) * math.sqrt(252))
c_ex25 = float(ce[upto25][-1])
p_ex25 = float(1 - norm.cdf(math.log(300_000 / c_ex25) / (vol_e25 * math.sqrt(t25_))))
p_n25 = float(1 - norm.cdf(math.log(300_000 / float(cn[upto25][-1])) / (vol_n25 * math.sqrt(t25_))))
p_rw25 = float(1 - norm.cdf(math.log(300_000 / P25["base"]["cost_rw"]) / (vol_n25 * math.sqrt(t25_))))
hv["third_session_25sep"] = {
    "D1_6_exact_25sep": {"printed": 0.243, "rebuilt_blind_engine": p_ex25, "cost_exact_fwd": c_ex25, "vol": vol_e25, "t": t25_},
    "D1_6_nov15_25sep_same_code": {"printed": 0.305, "rebuilt_blind_engine": p_n25, "cost_nov15_fwd": float(cn[upto25][-1]), "vol": vol_n25},
    "AX1b_B_lift_25sep": {"printed_pp": 3.4, "R1_with_rw_centre": p_rw25, "lift_pp": 100 * (p_rw25 - p_n25)}}
say(f"[H] 25 Sep exact-date D1 [6]: {p_ex25:.4%} (printed 24.3%; cost ${c_ex25:,.2f}, vol {vol_e25:.4f}); Nov-15 same code "
    f"{p_n25:.4%}; AX1b [B] 25 Sep lift {100 * (p_rw25 - p_n25):+.2f}pp (printed +3.4)")

# ---------------------------------------------------------------------------------------------------------------- [X] third pricer vs primary
# deterministic_check.py (standard library only) was compared by its author with numbers.yaml and m2_blind only.
# Here it is compared with the PRIMARY build, which it never saw.
dd, d28, d13 = DC["deterministic"], DC["base_2028"], DC["H13"]
tp = [("Cost_FWD(R)", dd["cost_fwd_R_usd"], P["base"]["cost_fwd"], "usd"),
      ("Cost_RW(R)", dd["cost_rw_R_usd"], P["base"]["cost_rw"], "usd"),
      ("PV today", dd["pv_today_R_usd"], P_PV_TODAY, "usd"),
      ("FWD break-even", dd["breakeven_fall_bp_fwd"], P["base"]["breakeven_fall_bp_fwd"], "bp"),
      ("RW break-even", dd["breakeven_fall_bp_rw"], P["base"]["breakeven_fall_bp_rw"], "bp"),
      ("ladder yield today (%)", dd["ladder_yield_y_D_pct"], P["panel"]["ladder_yield_today_pct"], "pct"),
      ("d ladder yield / d shift", dd["dy_db_at_R"], P["panel"]["dy_per_parallel_shift"], "ratio"),
      ("2033 rung cost at R (RW)", dd["rung_2033_cost_at_A_rw_usd"], P_RUNG2033, "usd"),
      ("2028 fund base, FWD", d28["fwd"]["S_usd"], P["fifteen_months"]["base_fwd_fund"], "usd"),
      ("2028 floor base", d28["fwd"]["F_usd"], P["fifteen_months"]["base_fwd_floor"], "usd"),
      ("2028 fund base, RW", d28["rw"]["S_usd"], P["fifteen_months"]["base_rw"]["fund_p50"], "usd")]
for b in (-50, -100, -150):
    for lab5, tag in (("5y unchanged", "y5_unchanged"), ("5y also lower", "y5_shifted")):
        tp.append((f"H13 {b}bp fund, {lab5}", d13[f"{b}bp"][tag]["stock_fund_usd"], PH[(b, lab5)]["stock_fund"], "usd"))
        tp.append((f"H13 {b}bp floor face, {lab5}", d13[f"{b}bp"][tag]["floor_face_usd"], PH[(b, lab5)]["floor_face"], "usd"))
    tp.append((f"H13 {b}bp top-up Jan 2028", d13[f"{b}bp"]["topup_on_B_usd"], PH[(b, "5y unchanged")]["topup_2028"], "usd"))
for b in (-50, -100):
    tp.append((f"H14 {b}bp unfunded 2033", DC["H14"][f"{b}bp"]["unfunded_2033_usd"], PH[(b, "5y unchanged")]["unfunded_2033_if_no_deposit"], "usd"))
tp.append(("E5 closed form vs primary E5 Monte Carlo", DC["E5_closed_form"]["P_gap_gt_0"], pest(4)["P_gap"], "prob"))
TP_TOL = {"usd": 0.01, "bp": 1e-4, "pct": 1e-6, "ratio": 1e-6, "prob": 0.02}
tp_rows = [{"what": w, "third_pricer": a, "primary": b, "diff": a - b, "tol": TP_TOL[k], "kind": k, "ok": abs(a - b) <= TP_TOL[k]}
           for w, a, b, k in tp]
OUT["third_pricer_vs_primary"] = {"source": "rab/verification/blind/deterministic_check.json (standard library only, commit 97c3467)",
                                  "author_checks": DC["summary"], "n": len(tp_rows), "n_fail": sum(not r["ok"] for r in tp_rows),
                                  "max_abs_usd_diff": max(abs(r["diff"]) for r in tp_rows if r["kind"] == "usd"),
                                  "max_abs_bp_diff": max(abs(r["diff"]) for r in tp_rows if r["kind"] == "bp"), "rows": tp_rows}
tmd = ["| Quantity | Third pricer (stdlib) | Primary | Diff | Tol | OK |", "|---|---|---|---|---|---|"]
for r in tp_rows:
    f_ = {"usd": lambda v: f"${v:,.2f}", "bp": lambda v: f"{v:.4f}bp", "pct": lambda v: f"{v:.6f}%", "ratio": lambda v: f"{v:.8f}",
          "prob": lambda v: f"{100 * v:.2f}%"}[r["kind"]]
    tmd.append(f"| {r['what']} | {f_(r['third_pricer'])} | {f_(r['primary'])} | {r['diff']:+.2e} | {r['tol']:g} | {'yes' if r['ok'] else 'NO'} |")
(HERE / "gateB_ws4_third_pricer.md").write_text("\n".join(tmd) + "\n")
say(f"[X] third pricer vs primary: {len(tp_rows)} comparisons, {OUT['third_pricer_vs_primary']['n_fail']} failures; max $ diff "
    f"{OUT['third_pricer_vs_primary']['max_abs_usd_diff']:.2e}; max bp diff {OUT['third_pricer_vs_primary']['max_abs_bp_diff']:.2e}")
OUT["four_jan"] = {"primary_n_h_64": {"median": P4[64]["headline"]["P_gap"], "estimators": P4[64]["headline"]["estimators"],
                                      "rho": P4[64]["move"]["rho_median"], "cost_rw": P4[64]["base"]["cost_rw"],
                                      "breakeven_rw": P4[64]["base"]["breakeven_fall_bp_rw"]},
                   "primary_n_h_65": {"median": P4[65]["headline"]["P_gap"], "estimators": P4[65]["headline"]["estimators"],
                                      "rho": P4[65]["move"]["rho_median"]},
                   "blind_n_h_65": {"median": s4b["P_median"], "estimators": s4b["per_estimator"], "rho_used": BE["E5_move_options"]["rho_median"]}}
say(f"[X] 4 Jan median: primary n_h 64 {P4[64]['headline']['P_gap']:.4%}, n_h 65 {P4[65]['headline']['P_gap']:.4%}; blind (65) {s4b['P_median']:.4%}")

OUT["pass"] = bool(n_unrec == 0 and OUT["third_pricer_vs_primary"]["n_fail"] == 0)
json.dump(OUT, open(HERE / "gateB_ws4_results.json", "w"), indent=1, default=float)
say(f"wrote {HERE / 'gateB_ws4_results.json'}, gateB_ws4_table.csv, gateB_ws4_table.md, gateB_ws4_third_pricer.md; pass = {OUT['pass']}")
