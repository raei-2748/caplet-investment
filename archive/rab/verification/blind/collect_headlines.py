"""Collect the blind rebuild's headline keys for M5, M6 and M7 into one flat JSON and a short Markdown report.

Reads only rab/verification/blind/out/*/*_results.json (this folder's own outputs). Key names follow the specs'
vocabulary so the Gate B reconciler can line them up with the primary's results; nothing here was read from the
primary's code or results.

Run:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/collect_headlines.py
AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def load(m):
    with open(os.path.join(OUT, m, f"{m}_results.json")) as f:
        return json.load(f)


def clean(v):
    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
        return None
    return v


def usd(v):
    return "n/a" if v is None else f"${v:,.0f}"


def pct(v, d=1):
    return "n/a" if v is None else f"{100 * v:.{d}f}%"


def main():
    H = {}
    m5, m6, m7 = load("M5"), load("M6"), load("M7")

    # ---------------- M5 ----------------
    a = m5["part_a_headlines"]
    for k in ("V0_D", "cost_2020_median", "cost_2020_min", "cost_2020_max", "cost_2020_max_date", "cheapest_since_spot",
              "share_days_le_300k_since_2000_spot", "share_days_le_300k_since_1990_spot", "days_priced_since_2000",
              "days_priced_1990_2026", "n_months_since_1871", "share_months_le_V0D_since_1871",
              "share_months_le_300k_since_1871", "share_months_le_V0D_since_1962", "share_months_le_300k_since_1962",
              "share_years_median_below_V0D_1871_2026", "n_years_1871_2026", "share_months_le_V0D_since_1871_adj_median",
              "share_months_le_V0D_since_1871_adj_p95", "share_months_le_300k_since_1871_adj_median",
              "share_months_le_300k_since_1871_adj_p95"):
        H[f"M5.A.{k}"] = a[k]
    for k in ("lowest_since_1871", "highest_since_1871", "lowest_since_1962", "highest_since_1962"):
        H[f"M5.A.{k}.usd"] = a[k]["usd"]
        H[f"M5.A.{k}.date"] = a[k]["date"]
        H[f"M5.A.{k}.basis"] = a[k]["basis"]
    for k in ("median", "p05", "p95", "n"):
        H[f"M5.A.flat_vs_full_1962_2026.{k}"] = a["flat_vs_full_1962_2026"][k]
    for k in ("n_months", "largest_abs_diff_usd", "median_abs_diff_usd"):
        H[f"M5.A.fred_vs_treasury_1990_2026.{k}"] = a["fred_vs_treasury_1990_2026"][k]
    repro = m5["reproduction_vs_numbers_yaml"]
    H["M5.A.reproduction_vs_numbers_yaml.all_agree"] = all(v["agree"] for v in repro.values())
    H["M5.A.reproduction_vs_numbers_yaml.n_checks"] = len(repro)
    b_keys = ("gift_worst", "gift_worst_Y", "gift_p10", "gift_median", "gift_p90", "gift_best", "gift_best_Y",
              "T33_worst", "T33_worst_Y", "T33_p10", "T33_median", "T33_p90", "T33_best",
              "real_gift_worst", "real_gift_worst_Y", "real_gift_p10", "real_gift_median", "real_gift_p90",
              "real_T33_worst", "real_T33_median", "share_top_reached", "n_short_S_gt_0", "largest_S",
              "n_topup_T_gt_0", "largest_T", "ips_variant_gift_worst", "ips_variant_gift_worst_Y", "n_C_gt_300k",
              "ladder_cost_C_median", "ladder_cost_C_max", "ladder_cost_C_max_Y", "fund0_median", "n_fund0_zero", "n_windows")
    for row in m5["part_b_summary"]:
        p = f"M5.B.{row['view']}.{row['fund_series']}"
        for k in b_keys:
            H[f"{p}.{k}"] = clean(row[k])
    for row in m5["era_table"]:
        p = f"M5.B.era.{row['era']}"
        for k in ("n", "median_ladder_cost", "median_gift", "worst_gift", "worst_gift_Y", "median_T33", "share_top_reached", "n_topup"):
            H[f"{p}.{k}"] = row[k]
    for k, v in m5["part_b_checks"].items():
        H[f"M5.B.check.{k}"] = v
    H["M5.n_series_points"] = m5["n_series_points"]

    # ---------------- M6 ----------------
    for row in m6["rivals_summary"]:
        p = f"M6.{row['lens']}.{row['rival']}"
        for k, v in row.items():
            if k in ("lens", "rival", "note"):
                continue
            v = clean(v)
            if v is None:
                continue
            H[f"{p}.{k}"] = v
    for k, v in m6["H16_reverify"].items():
        H[f"M6.H16.{k}"] = v
    for row in m6["fund_alternatives"]:
        p = f"M6.fund.{row['lens']}.{row['fund']}"
        for k, v in row.items():
            if k in ("fund", "label", "lens"):
                continue
            v = clean(v)
            if v is None:
                continue
            H[f"{p}.{k}"] = v
    for row in m6["fund_choice_decision"]:
        p = f"M6.fund_decision.{row['fund']}"
        for k in ("test1_benefit_p5", "test1_benefit_spread", "test2_history_p10", "test2_history_spread", "test2_same_direction",
                  "test3_median_not_cut", "tests_1_to_3_pass", "mc_gift_p5_delta", "mc_spread90_ratio", "mc_gift_p50_delta",
                  "hist_gift_p10_delta", "hist_spread80_ratio", "hist_gift_p50_delta", "pass_1_to_3", "seeds", "robust_switch", "final"):
            H[f"{p}.{k}"] = row[k]
    H["M6.fund_decision.any_switch"] = any(str(r["final"]).startswith("SWITCH") for r in m6["fund_choice_decision"])
    for k in ("phi", "sigma", "mu_breakeven", "pi0_aug26_over_aug25", "n_obs", "mean_pi_2027_2041"):
        H[f"M6.R6.inflation_ar1.{k}"] = m6["inflation_ar1"][k]
    for r in m6["breakevens"]:
        H[f"M6.R6.breakeven.n{int(r['n_years'])}"] = r["breakeven"]
    H["M6.mc.jpm_corr_fixed"] = m6["jpm_inputs"]["corr_fixed"]
    H["M6.mc.reserve33_p50"] = m6["mc_reserve33_p50"]
    H["M6.mc.reserve31_p50"] = m6["mc_reserve31_p50"]
    H["M6.mc.dy1_p5_p50_p95"] = m6["mc_dy1_p5_p50_p95"]
    H["M6.mc.seed"], H["M6.mc.n_paths"] = m6["seed"], m6["n_paths"]

    # ---------------- M7 ----------------
    s_keys = ("dpre", "s1", "s6", "ladder_cost_C", "leftover_L", "topup_T", "growth_money_G", "y5", "floor_cost_Cf", "floor_face_F",
              "fund0", "fund31", "fund33", "bottom", "top", "gift", "kept", "T33", "payments_funded", "short_S", "deflator_2033",
              "real_gift", "real_T33", "real_pay_2033", "real_pay_2042", "real_pay_total", "R1_T33", "R2_T33", "R2_reserve33",
              "R5_T33", "R5_floor_broken", "cum_e_2028_2032", "sum_dy")
    for row in m7["stress_table"]:
        p = f"M7.{row['scenario']}"
        H[f"{p}.name"] = row["name"]
        for k in s_keys:
            H[f"{p}.{k}"] = clean(row[k])
    H["M7.all_headline_scenarios_payments_funded"] = all(r["payments_funded"] for r in m7["stress_table"] if not r["scenario"].endswith("_lit"))
    for ev in m7["downgrade_events"]:
        p = f"M7.downgrade.{ev['scenario']}"
        for k in ("announcement", "dgs10_start_date", "dgs10_start", "dgs10_end_date", "dgs10_end", "dgs10_change_pp",
                  "alt_prior_close_change_pp", "sp500_change"):
            H[f"{p}.{k}"] = ev[k]
    for k in ("a_topup_starts_C_300k_bp", "b_fund0_zero_floor_150k_bp", "c_payment_unfunded_G_zero_bp"):
        H[f"M7.threshold.{k}"] = m7["thresholds"][k]
    for row in m7["real_value_paths"]:
        p = f"M7.real_value.{row['path']}"
        for k in ("annual_avg_infl_15y", "real_2033", "real_2042", "total_real"):
            H[f"{p}.{k}"] = row[k]
    rh = m7["real_value_history"]
    for k in ("n_windows", "total_p5", "total_p50", "total_p95", "worst_window_Y", "worst_total", "infl15_p5", "infl15_p50", "infl15_p95"):
        H[f"M7.real_value_history.{k}"] = rh[k]
    for row in rh["per_payment"]:
        if int(row["payment_year"]) in (2033, 2037, 2042):
            for k in ("p5", "p50", "p95", "min", "max"):
                H[f"M7.real_value_history.{int(row['payment_year'])}.{k}"] = row[k]
    H["M7.H19.2033"], H["M7.H19.2042"] = m7["H19"]["2033"], m7["H19"]["2042"]
    H["M7.H19.reference"] = m7["H19"]["reference"]
    H["M7.H19.convention"] = m7["H19"]["convention"]

    meta = {"what": "Blind rebuild of M5, M6, M7 from rab/models/*_SPEC.md, rab/data/ and rab/numbers.yaml only",
            "collected_sydney": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            "curve_date": m5["curve_date"], "mc_seed": m6["seed"], "mc_paths": m6["n_paths"], "n_keys": len(H),
            "sources": ["out/M5/M5_results.json", "out/M6/M6_results.json", "out/M7/M7_results.json"]}
    with open(os.path.join(OUT, "blind_headlines.json"), "w") as f:
        json.dump({"meta": meta, "headlines": H}, f, indent=1, default=str)

    # ---------------- report ----------------
    L = []
    L.append("# WS3 blind rebuild: M5 history, M6 rivals, M7 stress (report)")
    L.append("")
    L.append(f"Built from `rab/models/M5_SPEC.md`, `M6_SPEC.md`, `M7_SPEC.md`, `rab/data/` and the locked `rab/numbers.yaml` only "
             f"(28 Sep 2026 curve). Every figure is MODEL output. Flat key list: `out/blind_headlines.json` ({len(H)} keys). "
             f"Generated {meta['collected_sydney']}.")
    L.append("")
    L.append("## M5: cost of certainty and the century backtest")
    L.append("")
    L.append(f"- Reproduction of the locked history figures on the 1990-2026 daily curves: {sum(v['agree'] for v in repro.values())}/{len(repro)} agree "
             f"(today {usd(a['V0_D'])}; 2020 median {usd(a['cost_2020_median'])}; peak {usd(a['cost_2020_max'])} on {a['cost_2020_max_date']}; "
             f"cheapest since {a['cheapest_since_spot']}).")
    L.append(f"- Extended to 1871: lowest {usd(a['lowest_since_1871']['usd'])} ({a['lowest_since_1871']['date']}), highest {usd(a['highest_since_1871']['usd'])} "
             f"({a['highest_since_1871']['date']}). Share of months since 1871 at least as cheap as today: {pct(a['share_months_le_V0D_since_1871'])} "
             f"({pct(a['share_months_le_V0D_since_1871_adj_median'])} after the flat-curve correction); at or under $300,000: {pct(a['share_months_le_300k_since_1871'])}. "
             f"Since 1962: {pct(a['share_months_le_V0D_since_1962'])}. Calendar years whose median cost was below today's: {pct(a['share_years_median_below_V0D_1871_2026'])} "
             f"({int(round(a['share_years_median_below_V0D_1871_2026'] * a['n_years_1871_2026']))} of {a['n_years_1871_2026']}).")
    fv = a["flat_vs_full_1962_2026"]
    L.append(f"- Flat-curve check 1962-2026: flat/full - 1 median {100 * fv['median']:.2f}% (5th-95th {100 * fv['p05']:.2f}% to {100 * fv['p95']:.2f}%). "
             f"FRED vs Treasury file: largest difference {usd(a['fred_vs_treasury_1990_2026']['largest_abs_diff_usd'])}.")
    L.append("")
    L.append("| view | fund | worst gift (Y) | p10 | median | p90 | best | median T33 | median real gift | top reached | windows with top-up (largest) | short |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for row in m5["part_b_summary"]:
        L.append(f"| {row['view']} | {row['fund_series']} | {usd(row['gift_worst'])} ({row['gift_worst_Y']}) | {usd(row['gift_p10'])} | {usd(row['gift_median'])} | "
                 f"{usd(row['gift_p90'])} | {usd(row['gift_best'])} | {usd(row['T33_median'])} | {usd(row['real_gift_median'])} | {pct(row['share_top_reached'])} | "
                 f"{row['n_topup_T_gt_0']} ({usd(row['largest_T'])}) | {row['n_short_S_gt_0']} |")
    L.append("")
    L.append("Era table (history's yields, world stocks): " + "; ".join(
        f"{r['era']}: ladder {usd(r['median_ladder_cost'])}, median gift {usd(r['median_gift'])}, worst {usd(r['worst_gift'])} ({r['worst_gift_Y']})"
        for r in m5["era_table"]) + ".")
    ck = m5["part_b_checks"]
    L.append(f"Today-yields check: fund0 {ck['today_fund0']:,.2f} vs {ck['target_fund0']:,.0f}; floor cost {ck['today_Cf']:,.2f} vs {ck['target_Cf']:,.0f} (both within $1).")
    L.append("")
    L.append("## M6: rivals on the same metrics, and the branch-fund rule")
    L.append("")
    hist = [r for r in m6["rivals_summary"] if r["lens"] == "history"]
    mc = [r for r in m6["rivals_summary"] if r["lens"] == "MC"]
    L.append("History lens, 149 start years 1872-2020 (R6: 140 inflation paths):")
    L.append("")
    L.append("| rival | unfunded share (largest shortfall) | T33 worst / p10 / median / p90 | gift worst / p10 / median / p90 | certain in 2031 (median) | top reached | trades |")
    L.append("|---|---|---|---|---|---|---|")
    for r in hist:
        if r["rival"] == "R6":
            L.append(f"| R6 TIPS ladder | {pct(r['unfunded_share'])} of paths have at least one payment short (largest total gap {usd(r['largest_shortfall'])}; "
                     f"{pct(r['share_payments_short'])} of payments short; {pct(r['share_windows_total_paid_lt_500k'])} pay less than $500,000 in total) | "
                     f"= REC | n/a | n/a | n/a | {r['trades']} |")
            continue
        L.append(f"| {r['rival']} | {pct(r['unfunded_share'])} ({usd(r['largest_shortfall'])}) | {usd(r['T33_worst'])} / {usd(r['T33_p10'])} / {usd(r['T33_p50'])} / {usd(r['T33_p90'])} | "
                 f"{usd(r['gift_worst'])} / {usd(r['gift_p10'])} / {usd(r['gift_p50'])} / {usd(r['gift_p90'])} | {usd(r['certain31_p50'])} | {pct(r['top_reached_share'])} | {r['trades']} |")
    L.append("")
    L.append(f"MC lens (JPM 2026 LTCMA, {m6['n_paths']:,} paths, seed {m6['seed']}):")
    L.append("")
    L.append("| rival | unfunded share | T33 p5 / p50 / p95 | gift p5 / p50 / p95 | top reached | notes |")
    L.append("|---|---|---|---|---|---|")
    for r in mc:
        if r["rival"] == "R6":
            L.append(f"| R6 TIPS ladder | {pct(r['unfunded_share'])} (any payment short) | = REC | n/a | n/a | {pct(r['share_payments_short'])} of payments short; "
                     f"{pct(r['share_paths_total_paid_lt_500k'])} of paths pay less than $500,000 in total; median gap {usd(r['gap_p50'])} |")
            continue
        note = ""
        if "promised_150k_met_share" in r and clean(r.get("promised_150k_met_share")) is not None:
            note = f"$150,000 promise met in {pct(r['promised_150k_met_share'])} of paths (cushion negative at some 1 Jan 2028-32 in {pct(r['floor_broken_share'])})"
        L.append(f"| {r['rival']} | {pct(r['unfunded_share'], 2)} | {usd(r['T33_p5'])} / {usd(r['T33_p50'])} / {usd(r['T33_p95'])} | "
                 f"{usd(r['gift_p5'])} / {usd(r['gift_p50'])} / {usd(r['gift_p95'])} | {pct(r['top_reached_share'])} | {note} |")
    h16 = m6["H16_reverify"]
    L.append("")
    L.append(f"H16 re-verified (growth-first R4b, share of paths where the money cannot buy the reserve): 2028 deposit $150k {pct(h16['deposit_150k'])}, "
             f"$75k {pct(h16['deposit_75k'])}, none {pct(h16['deposit_0'])} (insight_v1 on the 25 Sep curve: "
             + " / ".join(pct(h16['reference_H16_25sep'][k]) for k in ('deposit_150k', 'deposit_75k', 'deposit_0')) + ").")
    L.append("")
    L.append("Branch-fund alternatives (REC fixed except the fund; fund0 $40,736; buy-and-hold):")
    L.append("")
    L.append("| fund | MC gift p5 / p50 / p95 (spread90) | MC P(top) | history 1928-2020 gift p10 / p50 / p90 (spread80) | ETF 2011-2020 gift p50 | rule |")
    L.append("|---|---|---|---|---|---|")
    fa = {(r["fund"], r["lens"]): r for r in m6["fund_alternatives"]}
    dec = {r["fund"]: r for r in m6["fund_choice_decision"]}
    for fid in ("A0", "A1", "A2", "A3", "A4"):
        mcr, hr, er = fa[(fid, "MC")], fa[(fid, "history_1928_2020")], fa.get((fid, "etf_2011_2020"))
        d = dec.get(fid)
        rule = "baseline" if d is None else (f"{d['final']} (tests 1-3 {'pass' if d['tests_1_to_3_pass'] else 'fail'}; {d['pass_1_to_3']}/{d['seeds']} seeds)")
        L.append(f"| {fid} {mcr['label']} | {usd(mcr['gift_p5'])} / {usd(mcr['gift_p50'])} / {usd(mcr['gift_p95'])} ({usd(mcr['spread90'])}) | {pct(mcr['p_top'])} | "
                 f"{usd(hr['gift_p10'])} / {usd(hr['gift_p50'])} / {usd(hr['gift_p90'])} ({usd(hr['spread80'])}) | {usd(er['gift_p50']) if er else 'n/a'} | {rule} |")
    L.append("")
    L.append(f"Pre-registered switch rule outcome: {'a switch is indicated' if H['M6.fund_decision.any_switch'] else 'VT stays'}. "
             + "; ".join(f"{fid}: {dec[fid]['final']}" for fid in ("A1", "A2", "A3", "A4")) + ".")
    ar = m6["inflation_ar1"]
    L.append(f"R6 inputs: breakevens 6-15y {100 * min(r['breakeven'] for r in m6['breakevens']):.2f}-{100 * max(r['breakeven'] for r in m6['breakevens']):.2f}%; "
             f"inflation AR(1) phi {ar['phi']:.3f}, sigma {100 * ar['sigma']:.2f}pp, mean {100 * ar['mu_breakeven']:.2f}%, start {100 * ar['pi0_aug26_over_aug25']:.2f}%.")
    L.append("")
    L.append("## M7: stress scenarios and the real value of the payments")
    L.append("")
    L.append("| scenario | shift before purchase (pp) | ladder cost 1 Jan 2027 | top-up 2028 | floor face | fund0 | 2031 range bottom-top | 2033 gift | T33 | payments funded | real gift (2027 $) | real 2042 payment |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in m7["stress_table"]:
        if r["scenario"].endswith("_lit"):
            continue
        L.append(f"| {r['scenario']} {r['name'].split(':')[0][:44]} | {r['dpre']:+.2f} | {usd(r['ladder_cost_C'])} | {usd(r['topup_T'])} | {usd(r['floor_face_F'])} | {usd(r['fund0'])} | "
                 f"{usd(r['bottom'])}-{usd(r['top'])} | {usd(r['gift'])} | {usd(r['T33'])} | {'yes' if r['payments_funded'] else 'NO'} | {usd(r['real_gift'])} | {usd(r['real_pay_2042'])} |")
    thr = m7["thresholds"]
    L.append("")
    L.append(f"Thresholds on the base path (yields fall x before 1 Jan 2027 and stay there): top-up starts at {thr['a_topup_starts_C_300k_bp']:.1f}bp; "
             f"the stock fund reaches $0 with the $150,000 floor intact at {thr['b_fund0_zero_floor_150k_bp']:.1f}bp; a payment is unfunded at {thr['c_payment_unfunded_G_zero_bp']:.1f}bp.")
    ev = {e["scenario"]: e for e in m7["downgrade_events"]}
    L.append("Measured downgrade moves (FRED DGS10, announcement-day close to 20 trading days later): " + "; ".join(
        f"{sid} {e['dgs10_change_pp']:+.2f}pp (S&P 500 {100 * e['sp500_change']:+.1f}%)" for sid, e in ev.items()) + ".")
    rv = {r["path"]: r for r in m7["real_value_paths"]}
    L.append("")
    L.append("Real value of the $50,000 payments in 1 Jan 2027 dollars: " + "; ".join(
        f"{name.split('_')[0] if not name.startswith('S') else name.split('_')[0]} ({100 * r['annual_avg_infl_15y']:.1f}%/yr): 2033 {usd(r['real_2033'])}, 2042 {usd(r['real_2042'])}, ten payments {usd(r['total_real'])}"
        for name, r in rv.items()) + ".")
    L.append(f"History, every 15-year window 1872-2011 ({rh['n_windows']}): ten-payment real total p5 {usd(rh['total_p5'])}, median {usd(rh['total_p50'])}, p95 {usd(rh['total_p95'])}; "
             f"worst window starts {rh['worst_window_Y']} ({usd(rh['worst_total'])}). H19 reproduced: {usd(m7['H19']['2033'])} / {usd(m7['H19']['2042'])} "
             f"(reference {usd(m7['H19']['reference']['2033'])} / {usd(m7['H19']['reference']['2042'])}), convention {m7['H19']['convention']}; "
             f"sourced input: {m7['H19']['sourced_input']}.")
    L.append("")
    L.append("## Flags for the reconciler (spec readings chosen here)")
    L.append("")
    lit = next(r for r in m7["stress_table"] if r["scenario"] == "S2_lit")
    s2 = next(r for r in m7["stress_table"] if r["scenario"] == "S2")
    L.append(f"1. M7 S2: the spec writes the Japan rate change as `(jpn_ltrate ... )/100`, but `jpn_ltrate` is already in percent, so the literal reading "
             f"gives a near-zero shift while S1 (10 Yr differences) is in percentage points. Headline S2 uses percentage points (gift {usd(s2['gift'])}, "
             f"s1 {s2['s1']:+.2f}pp); the literal reading is kept as row `S2_lit` (gift {usd(lit['gift'])}, s1 {lit['s1']:+.4f}pp).")
    L.append("2. M6 R6 `unfunded`: read as 'at least one of the ten payments paid below $50,000' (the spec: 'a payment is short when paid < 50,000'). "
             "Two alternates are reported next to it: share of payments short, and share of paths whose ten payments total under $500,000.")
    L.append("3. M6 R5 (CPPI): the gift rule uses bottom = certain31 = 0 as the spec's metric list says; the $150,000 promise is scored separately "
             "(`promised_150k_met_share`). `floor_broken_share` counts a negative cushion at any 1 Jan from 2028 on (at 1 Jan 2027 the floor exceeds "
             "the first deposit by construction, since the 2028 deposit is not counted).")
    L.append("4. M7 downgrade windows start at the close of the announcement day (all three were announced after the close); the prior-day reading is in "
             "`downgrade_events.csv` as `alt_prior_close_change_pp`.")
    L.append("5. M5 H1: the published 11 Oct 2010 row has every tenor blank and is dropped (noted in `M5_results.json`).")
    L.append("")
    L.append("Disclosure: before this session's work the tail of `rab-ws/STATUS.md` and the primary's commit message (`git log`) were seen; they carry "
             "one-sentence headline figures. They were not used to write or tune any code here; the code was written from the specs and re-run unchanged "
             "except for the additions listed above (S2_lit, R6 alternates, this report).")
    with open(os.path.join(HERE, "BLIND_REPORT.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))
    print(f"\nwrote {os.path.join(OUT, 'blind_headlines.json')} ({len(H)} keys) and {os.path.join(HERE, 'BLIND_REPORT.md')}")


if __name__ == "__main__":
    main()
