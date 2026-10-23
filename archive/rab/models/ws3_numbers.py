"""Collect WS3 headline numbers (M5, M6, M7) into rab/results/WS3_numbers_proposed.yaml for WS1/WS0 to merge into
rab/numbers.yaml at the next lock (WS1 is the only writer of numbers.yaml; PM-35). Same fields as numbers.yaml entries.
Values are read from the result files, never typed. AI-generated (Claude Code), WS3, 2026-09-30.

Run from the worktree root after m5_backtest.py, m6_rivals.py, m7_stress.py:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/ws3_numbers.py
"""
import json
import os

import pandas as pd
import yaml

import hist_lib as H

R = H.RES


def entry(value, unit, quote_as, scale, status, method, source, note="", valuation_date="n/a",
          maturity="15 Nov of the year before each payment (STRIPS maturity dates)", basis="see method"):
    return dict(value=value, unit=unit, quote_as=quote_as, scale=scale, status=status, curve_date="2026-09-28",
                valuation_date=valuation_date, maturity_convention=maturity, instrument_basis=basis, method=method,
                source=source, as_of="2026-09-28", note=note)


def r0(x, n=0):
    return round(float(x), n)


def main():
    m5 = json.load(open(os.path.join(R, "M5", "M5_results.json")))
    m6 = json.load(open(os.path.join(R, "M6", "M6_results.json")))
    m7 = json.load(open(os.path.join(R, "M7", "M7_results.json")))
    # Gate B fix: summaries come from the JSON (full precision). The CSVs are written with 2 decimals, which had turned
    # probabilities such as the glide path's 0.17% into 0.0 and 60/40's 1.27% into 0.01.
    S5 = pd.DataFrame(m5["part_b_summary"]).set_index(["view", "fund"])
    S6 = pd.DataFrame(m6["summary"]).set_index("rival")
    T7 = pd.read_csv(os.path.join(R, "M7", "stress_table.csv")).set_index("id")
    P7 = pd.read_csv(os.path.join(R, "M7", "real_value_paths.csv")).set_index("path")
    HD = pd.read_csv(os.path.join(R, "M7", "real_value_history_distribution.csv")).set_index("payment")
    ext = m5["part_a"]["extended"]
    out = {}
    M5m = "rab/models/M5_SPEC.md part A"
    out["ws3.certainty.share_months_as_cheap_since_1871"] = entry(
        r0(ext["since_1871"]["share_months_le_today"], 4), "share of month-start curves 1871-2026",
        "only about one month in four since 1871 was as cheap as 28 Sep 2026", "history", "MODEL", M5m,
        "rab/results/M5/M5_results.json part_a.extended.since_1871",
        note=f"Pre-1962 curves flat at the long rate; bias-corrected {ext['flat_bias_sensitivity']['median_error']['share_months_le_today_since_1871']:.3f}"
             f" / {ext['flat_bias_sensitivity']['p95_error']['share_months_le_today_since_1871']:.3f}. Since 1962: "
             f"{ext['since_1962']['share_months_le_today']:.3f}.", valuation_date="each curve date (same time to maturity)")
    out["ws3.certainty.low_1981"] = entry(
        dict(usd=r0(ext["since_1962_daily"]["min"]), date=ext["since_1962_daily"]["min_date"]), "USD",
        "about $110,000 on 30 Sep 1981, the cheapest day since at least 1962 (and the cheapest month since 1871)", "history", "MODEL", M5m,
        "rab/results/M5/M5_results.json part_a.extended.since_1962_daily", valuation_date="each curve date")
    h = S5.loc[("hist", "world_eq")]
    t = S5.loc[("today_yields", "world_eq")]
    M5b = "rab/models/M5_SPEC.md part B"
    out["ws3.backtest.hist.unfunded_windows"] = entry(
        dict(windows=int(h.windows), unfunded=int(h.n_unfunded), topups=int(h.n_topup), floor_below_150k=int(h.n_bottom_lt_150k),
             ladder_cost_max=r0(pd.read_csv(os.path.join(R, "M5", "backtest_by_start_year.csv")).query(
                 "view=='hist' and fund=='world_eq'").C.max())),
        "start years 1872-2020", "starting on 1 January of any year since 1872, the plan would have paid all ten payments",
        "history", "MODEL", M5b, "rab/results/M5/backtest_summary.csv (hist, world_eq)",
        note="History's yields and returns. The ladder cost more than $300,000 in most start years (lower yields than "
             "today), so the 2028 deposit finished it and the bottom was below $150,000 in 91 of 149.")
    out["ws3.backtest.hist.gift"] = entry(
        dict(worst=r0(h.gift_worst), worst_Y=int(h.gift_worst_Y), p10=r0(h.gift_p10), median=r0(h.gift_median)), "USD",
        "at the yields of a typical past era the same promises would have left about $130,000 for the facility",
        "history", "MODEL", M5b, "rab/results/M5/backtest_summary.csv (hist, world_eq)")
    out["ws3.backtest.today_yields.gift"] = entry(
        dict(worst=r0(t.gift_worst), worst_Y=int(t.gift_worst_Y), p10=r0(t.gift_p10), median=r0(t.gift_median),
             top_reached=r0(t.share_top_reached, 3)), "USD",
        "with today's yields, the worst five-year stretch since 1872 still gives a gift of about $159,000",
        "laura_plan", "MODEL", M5b, "rab/results/M5/backtest_summary.csv (today_yields, world_eq)",
        note="Worst window = fund bought 1929 (Great Depression). Floor $150,000 in every window.")
    h9 = m5["h9_reconciliation"]
    out["ws3.backtest.H9_reverified"] = entry(
        dict(total_worst_raw=r0(h9["raw_total_worst"]), total_worst_rescaled=r0(h9["rescaled_total_worst"]),
             p10_rescaled=r0(h9["rescaled_total_p10"]), median_rescaled=r0(h9["rescaled_total_median"])),
        "USD", "quote only in the Final Report appendix", "reference", "REPRODUCED",
        "E6 [5] convention (U.S. S&P, windows 1928-2020, rescaled to 7% over 1928-2025) on the 28 Sep basis",
        "rab/results/M5/M5_results.json h9_reconciliation", note="insight_v1 H9: $171k / $169k / $185k / $214k. Unchanged.")
    M6m = "rab/models/M6_SPEC.md"
    for rid, key in (("REC", "rec"), ("R1", "all_treasury"), ("R2", "sixty_forty"), ("R3", "ladder_6040"),
                     ("R4", "glide"), ("R4b", "growth_first"), ("R5", "cppi3"), ("R5m5", "cppi5")):
        r = S6.loc[rid]
        v = dict(mc_short=r0(r.mc_unfunded, 4), mc_T33=[r0(r.mc_T33_p5), r0(r.mc_T33_p50), r0(r.mc_T33_p95)],
                 mc_certain31=r0(r.mc_certain31_p50), hist_short=f"{int(r.h_unfunded)}/{int(r.h_windows)}",
                 hist_T33=[r0(r.h_T33_p10), r0(r.h_T33_median), r0(r.h_T33_p90)], trades=int(r.trades))
        if rid in ("R5", "R5m5"):
            v["mc_floor_broken"] = r0(r.mc_floor_broken, 4)
        out[f"ws3.rivals.{key}"] = entry(v, "USD / share", "quote only in the Final Report (rivals table)", "model",
                                         "MODEL", M6m, "rab/results/M6/rivals_summary.csv",
                                         note="MC: JPM 2026 LTCMA, 200,000 paths, seed 20260930. T33 = money for the "
                                              "facility and flexibility on 1 Jan 2033 after the payments.")
    tips = m6["tips"]
    out["ws3.rivals.tips_ladder"] = entry(
        dict(mc_p_any_short=r0(tips["p_any_short"], 3), hist_short=f"{int(S6.loc['R6'].h_unfunded)}/{int(S6.loc['R6'].h_windows)}",
             extra_cost_95pct=r0(tips["tips_extra_cost_for_95pct_full_usd"], -3)), "share / USD",
        "a TIPS ladder would leave at least one $50,000 payment short in most inflation paths", "model", "MODEL", M6m,
        "rab/results/M6/M6_results.json tips")
    h16 = m6["h16_reverified"]
    out["ws3.rivals.H16_reverified"] = entry(
        dict(deposit_150k=r0(h16["deposit_150000"], 4), deposit_75k=r0(h16["deposit_75000"], 4),
             deposit_0=r0(h16["deposit_0"], 4)), "probability",
        "a growth-first plan misses a payment in about 1 path in 45 (1 in 10 if the 2028 deposit is halved)",
        "model", "MODEL", M6m, "rab/results/M6/M6_results.json h16_reverified",
        note="Supersedes ref.H16 (3.2% / 13.7% / 40.8%, old engine with 4.00% bonds).")
    dec = pd.read_csv(os.path.join(R, "M6", "fund_choice_decision.csv"))
    rob = m6["fund_robustness"]["mc"]["A4"]
    finals = dec.set_index("fund")["final"]
    decision = "KEEP VT" if all(str(f).startswith("KEEP VT") for f in finals) else "SWITCH: " + ", ".join(
        f for f, v in finals.items() if not str(v).startswith("KEEP VT"))
    gb = os.path.join(H.WT, "rab", "verification", "gateB_ws3", "gateB_ws3_mc_precision.json")
    gbn = ""
    if os.path.exists(gb):
        g = json.load(open(gb))
        gbn = (f" Gate B (rab/gates/gate_B_ws3.md): without seed noise the ratio is {g['reference']['ratio_mean']:.4f} "
               f"(reference sampler) and {g['blind']['ratio_mean']:.4f} (blind sampler), 100 seeds x 200,000 paths each: "
               f"just under the bar, so at the spec's 200,000 paths the spread test passes on about "
               f"{g['reference']['share_seeds_ratio_le_090']:.0%} of seeds, not all of them.")
    out["ws3.fund_choice"] = entry(
        dict(decision=decision, gold_reit_mc_p5_change=r0(dec.set_index("fund").loc["A4", "mc_p5_change"]),
             gold_reit_spread_ratio=r0(dec.set_index("fund").loc["A4", "mc_spread90_ratio"], 4),
             gold_reit_spread_test_seeds=f"{rob['c1b']}/20"), "USD / ratio",
        "none of four alternatives to VT moves the bad-case gift by more than about $1,500", "laura_plan", "MODEL",
        M6m + " section 5", "rab/results/M6/fund_choice_decision.csv; M6_results.json fund_robustness",
        note="Gold/REIT passes the number tests on the base seed only at the threshold (spread ratio 0.899 vs 0.90) and "
             f"on {rob['c1b']} of 20 other seeds: not robust under M6_SPEC s7, so VT stays." + gbn)
    th = m7["thresholds"]
    M7m = "rab/models/M7_SPEC.md"
    out["ws3.stress.thresholds_bp"] = entry(
        dict(topup_starts=r0(th["topup_starts_bp"], 1), fund_used_up=r0(th["fund_used_up_bp"], 1),
             payment_unfunded=r0(th["payment_unfunded_bp"], 1)), "basis points (parallel fall before 1 Jan 2027, persisting to Jan 2028)",
        "the $150,000 bottom survives a fall in yields of about 1 percentage point before the money arrives",
        "laura_plan", "MODEL", M7m, "rab/results/M7/M7_results.json thresholds",
        note="topup_starts equals laura.ladder.breakeven_fall_bp_strips (26.2).")
    for sid in ("S1", "S2", "S3", "S4a", "S5", "S6"):
        r = T7.loc[sid]
        out[f"ws3.stress.{sid}"] = entry(
            dict(name=r["name"], gift=r0(r.gift), real_gift=r0(r.real_gift), floor=r0(r.F), payments_funded=bool(r.funded)),
            "USD", "quote only in the Final Report (stress table)", "laura_plan", "MODEL", M7m,
            "rab/results/M7/stress_table.csv")
    bk = P7.loc[[p for p in P7.index if p.startswith("Market breakeven")][0]]
    out["ws3.real_value.breakeven"] = entry(
        dict(pay_2033=r0(bk.pay_2033), pay_2042=r0(bk.pay_2042), all_ten=r0(bk.total)), "USD of 1 Jan 2027",
        "at the market's expected inflation the last $50,000 payment buys about what $35,000 buys in 2027",
        "laura_plan", "MODEL", M7m + " section 4", "rab/results/M7/real_value_paths.csv",
        note="Inflation 2.34% a year = FRED T10YIE on 28 Sep 2026.")
    s1 = P7.loc[[p for p in P7.index if p.startswith("1970s")][0]]
    out["ws3.real_value.1970s"] = entry(
        dict(pay_2042=r0(s1.pay_2042), all_ten=r0(s1.total)), "USD of 1 Jan 2027",
        "in a 1970s-style inflation the last payment would buy about what $18,000 buys in 2027", "laura_plan",
        "MODEL", M7m + " section 4", "rab/results/M7/real_value_paths.csv")
    out["ws3.real_value.history_2042"] = entry(
        dict(p5=r0(HD.loc["2042", "p5"]), p50=r0(HD.loc["2042", "p50"]), p95=r0(HD.loc["2042", "p95"])), "USD of 1 Jan 2027",
        "quote only in the Final Report appendix", "history", "MODEL", M7m + " section 4",
        "rab/results/M7/real_value_history_distribution.csv")
    out["ws3.real_value.H19_reverified"] = entry(
        m7["h19"]["h19_reproduced"], "USD of 2026 at 2.5% (7 and 16 years)", "quote only in the Final Report appendix",
        "reference", "REPRODUCED", "insight_v1 strategy_changes.md I4 convention",
        "rab/results/M7/M7_results.json h19", note="2.5% now sourced: JPM 2026 LTCMA U.S. inflation 2.50% (repo PDF p.2).")
    doc = {"ws3_numbers_proposed": {"status": "PROPOSED by WS3 for WS1/WS0 (not yet in numbers.yaml; numbers.yaml unchanged)",
                                    "numbers_yaml_sha256_read": open(os.path.join(H.WT, "rab", "numbers.lock")).read().split()[0]
                                    if os.path.exists(os.path.join(H.WT, "rab", "numbers.lock")) else "n/a"},
           "numbers": out}
    with open(os.path.join(R, "WS3_numbers_proposed.yaml"), "w") as f:
        yaml.safe_dump(doc, f, sort_keys=False, width=120, allow_unicode=False)
    print(f"wrote {len(out)} entries")


if __name__ == "__main__":
    main()
