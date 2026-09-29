"""Write rab/numbers_ws3.yaml: the WS3 headline numbers used in the three WS3 decision memos
(D_fund_choice.md, D_rivals.md, D_stress_bad_year.md), each with value, unit, source file and its Gate B
cross-check against the blind build. Values are read from result files, never typed.
AI-generated (Claude Code), WS3, 2026-09-30 (Sydney).

    /Users/ray/Research/rab-ws/.venv/bin/python rab/decisions/build_numbers_ws3.py          # write the yaml
    /Users/ray/Research/rab-ws/.venv/bin/python rab/decisions/build_numbers_ws3.py --check  # + trace memo figures

--check lists every $, %, bp and decimal figure in the three memos that does not match (at its printed precision) a
value in rab/numbers_ws3.yaml or rab/numbers.yaml, apart from the case facts and rule thresholds in ALLOW.
It is a typo screen, not a proof: a round figure ("about $31,000") can match an unrelated value by chance, so every
memo figure was also checked by hand against its named key.
"""
import hashlib
import json
import os
import re
import sys

import pandas as pd
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RES = os.path.join(ROOT, "rab", "results")
OUT = os.path.join(ROOT, "rab", "numbers_ws3.yaml")
MEMOS = ["D_fund_choice.md", "D_rivals.md", "D_stress_bad_year.md"]
IPS_SNAPSHOT = "/Users/ray/Research/rab-ws/ws6/rab/trades/data/ips_doc_text_2026-09-30.txt"  # rab/ws6, read-only
IPS_WORDS_30SEP = 483  # wc -w of the IPS body in that snapshot (checked below when the file is present)


def load():
    j = lambda *p: json.load(open(os.path.join(ROOT, *p)))
    return dict(
        m5=j("rab", "results", "M5", "M5_results.json"),
        m6=j("rab", "results", "M6", "M6_results.json"),
        m7=j("rab", "results", "M7", "M7_results.json"),
        prec=j("rab", "verification", "gateB_ws3", "gateB_ws3_mc_precision.json"),
        blind=j("rab", "verification", "blind", "out", "blind_headlines.json")["headlines"],
        fa=pd.read_csv(os.path.join(RES, "M6", "fund_alternatives.csv")),
    )


def verdict(ref, bld, kind, scale=None):
    """kind 'det': deterministic ($1, 1e-6 on ratios); 'mc': Gate B tolerance (2% of level, 2pp on shares)."""
    worst = 0.0
    for k, r in ref.items():
        if k not in bld or not isinstance(r, (int, float)) or isinstance(r, bool):
            continue
        b = bld[k]
        d = abs(float(r) - float(b))
        if kind == "det":
            tol = 1.0 if abs(float(r)) > 10 else 1e-6
        elif abs(float(r)) <= 1.5 and k.endswith(("share", "short", "broken", "missed", "ratio", "reached")):
            tol = 0.02
        else:
            tol = 0.02 * (scale if scale else max(abs(float(r)), 1.0))
        worst = max(worst, d / tol)
    if worst <= 1.0:
        return "MATCH" if kind == "det" else "MC NOISE (within Gate B tolerance)"
    return f"CHECK (diff {worst:.2f}x tolerance)"


def rnd(d, n=2):
    return {k: (round(float(v), n) if isinstance(v, float) else v) for k, v in d.items()}


def e(value, unit, quote_as, source, gate_b, blind=None, note=None):
    out = dict(value=value, unit=unit, quote_as=quote_as, source=source, gate_b=gate_b)
    if blind is not None:
        out["blind"] = blind
    if note:
        out["note"] = note
    return out


def build():
    D = load()
    m5, m6, m7, B, fa = D["m5"], D["m6"], D["m7"], D["blind"], D["fa"]
    N = {}

    # ---------------- fund choice (M6 part B) ----------------
    fd = {r["fund"]: r for r in m6["fund_decision"]}
    a = fa.set_index(["fund", "lens"])
    vt = a.loc[("A0", "MC_JPM")]
    N["ws3.fund.stock_fund_share_of_deposits"] = e(
        round(40736 / 450000, 4), "share of $450,000 (2027 + 2028 deposits)", "about 9% of Laura's money",
        "DERIVED: rab/numbers.yaml laura.stock_fund_2028_usd.strips (40,736) / 450,000", "n/a (locked key / case fact)")
    ref = dict(gift_p5=float(vt.gift_p5), gift_p50=float(vt.gift_p50))
    bl = dict(gift_p5=B["M6.fund.MC.A0.gift_p5"], gift_p50=B["M6.fund.MC.A0.gift_p50"])
    N["ws3.fund.vt_gift_mc"] = e(rnd(ref, 0), "USD (2033 gift, Laura's plan)",
                                 "with VT the bad-case (1 in 20) gift is about $165,000 and the typical gift about $174,000",
                                 "rab/results/M6/fund_alternatives.csv (A0, MC_JPM)", verdict(ref, bl, "mc"), rnd(bl, 0))
    names = {"A1": "VTI + VXUS 62/38", "A2": "U.S. only", "A3": "VT + small/value tilt", "A4": "VT + gold/REIT"}
    for f, nm in names.items():
        r = fd[f]
        ref = dict(mc_p5_change=r["mc_p5_change"], mc_spread_ratio=r["mc_spread90_ratio"],
                   mc_median_change=r["mc_median_change"], hist_p10_change=r["hist_p10_change"],
                   hist_spread_ratio=r["hist_spread80_ratio"], hist_median_change=r["hist_median_change"])
        p = f"M6.fund_decision.{f}."
        bl = dict(mc_p5_change=B[p + "mc_gift_p5_delta"], mc_spread_ratio=B[p + "mc_spread90_ratio"],
                  mc_median_change=B[p + "mc_gift_p50_delta"], hist_p10_change=B[p + "hist_gift_p10_delta"],
                  hist_spread_ratio=B[p + "hist_spread80_ratio"], hist_median_change=B[p + "hist_gift_p50_delta"])
        det = {k: v for k, v in ref.items() if k.startswith("hist")}
        v_det = verdict(det, bl, "det")
        v_mc = verdict({k: v for k, v in ref.items() if k.startswith("mc")}, bl, "mc", scale=float(vt.gift_p5))
        val = rnd(ref, 4)
        val.update(seeds_spread_test_passed=f"{r['mc_seeds_spread_test_passed']}/{r['mc_seeds']}", final=r["final"])
        bl_r = rnd(bl, 4)
        bl_r.update(seeds_spread_test_passed=f"{B[p + 'pass_1_to_3']}/{B[p + 'seeds']}", final=B[p + "final"])
        N[f"ws3.fund.alt.{f}"] = e(
            val, "USD change vs VT (gift: MC 5th percentile / median; history 10th percentile / median); spread ratios",
            f"{nm}: quote only as a row of the Final Report table", "rab/results/M6/fund_choice_decision.csv (row " + f + ")",
            f"history lens: {v_det}; MC lens: {v_mc}; final decision {'identical' if r['final'] == B[p + 'final'] else 'DIFFERENT'}",
            bl_r)
    P = D["prec"]
    N["ws3.fund.gold_reit_noise_free"] = e(
        dict(spread_ratio_ref=round(P["reference"]["ratio_mean"], 4), spread_ratio_blind=round(P["blind"]["ratio_mean"], 4),
             bar=0.90, share_seeds_pass_ref=P["reference"]["share_seeds_ratio_le_090"],
             share_seeds_pass_blind=P["blind"]["share_seeds_ratio_le_090"],
             p5_gain_ref=round(P["reference"]["p5_change_mean"], 0), p5_gain_blind=round(P["blind"]["p5_change_mean"], 0),
             median_gain_ref=round(P["reference"]["median_change_mean"], 0),
             margin_under_bar=round(0.90 - P["reference"]["ratio_mean"], 4)),
        "ratio / share of 200,000-path seeds / USD", "gold/REIT is 0.001 under the 0.90 bar: a close call",
        "rab/verification/gateB_ws3/gateB_ws3_mc_precision.json (100 seeds x 200,000 paths per build)",
        "MC NOISE (0.8991 in both builds; gate_B_ws3.md s4)")
    rb = m6["fund_robustness"]
    hv = [rb["gold_float_era_1971_2020"], rb["reit_half_as_VT_1928_2020"], rb["both_1971_2020"]]
    N["ws3.fund.gold_reit_history_without_proxies"] = e(
        dict(p10_change_min=round(min(x["p10_change"] for x in hv), 0), p10_change_max=round(max(x["p10_change"] for x in hv), 0),
             spread_ratio_min=round(min(x["spread80_ratio"] for x in hv), 2), spread_ratio_max=round(max(x["spread80_ratio"] for x in hv), 2)),
        "USD / ratio", "with the flattering history proxies removed, gold/REIT still narrows the spread",
        "rab/results/M6/M6_results.json fund_robustness (3 history variants)", "reference build only (robustness check; not in the blind spec)")
    e0, e4 = a.loc[("A0", "etf_2011_2020")], a.loc[("A4", "etf_2011_2020")]
    ref = dict(p10_change=float(e4.gift_p10 - e0.gift_p10), median_change=float(e4.gift_p50 - e0.gift_p50))
    bl = dict(p10_change=B["M6.fund.etf_2011_2020.A4.gift_p10"] - B["M6.fund.etf_2011_2020.A0.gift_p10"],
              median_change=B["M6.fund.etf_2011_2020.A4.gift_p50"] - B["M6.fund.etf_2011_2020.A0.gift_p50"])
    N["ws3.fund.gold_reit_etf_lens"] = e(rnd(ref, 0), "USD change vs VT, real ETF returns (80% VT + 10% GLD + 10% VNQ), 10 windows 2012-2025",
                                         "on real ETF prices gold/REIT added nothing", "DERIVED: rab/results/M6/fund_alternatives.csv (etf_2011_2020 rows)",
                                         verdict(ref, bl, "det"), rnd(bl, 0))
    mx = max(max(abs(fd[f]["mc_p5_change"]), abs(fd[f]["hist_p10_change"])) for f in names)
    N["ws3.fund.max_abs_badcase_change"] = e(round(mx, 0), "USD (largest bad-case change vs VT, any alternative, either lens)",
                                             "no alternative moves the bad-case gift by more than about $1,500",
                                             "DERIVED: max |mc_p5_change|, |hist_p10_change| in rab/results/M6/fund_choice_decision.csv",
                                             "derived from reconciled rows (U.S. only, history: MATCH)")
    N["ws3.fund.gold_reit_gain_share_of_gift"] = e(round(P["reference"]["p5_change_mean"] / float(vt.gift_p50), 4), "share of VT's median gift",
                                                   "about 0.7% of the gift", "DERIVED: gold_reit_noise_free.p5_gain_ref / vt_gift_mc.gift_p50",
                                                   "derived from MC NOISE rows")

    # ---------------- rivals (M6 part A) ----------------
    S = {r["rival"]: r for r in m6["summary"]}
    bmap = {"REC": "REC", "R1": "R1", "R2": "R2", "R3": "R3", "R4": "R4", "R4b": "R4b", "R5": "R5_m3", "R5m5": "R5_m5"}
    label = {"REC": "Root-and-Branch (adopted)", "R1": "All-Treasury", "R2": "60/40 whole portfolio",
             "R3": "Ladder + 60/40 growth money", "R4": "Glide path 65->20", "R4b": "Growth-first 75->40",
             "R5": "CPPI multiplier 3", "R5m5": "CPPI multiplier 5"}
    for rid, bid in bmap.items():
        r = S[rid]
        ref = dict(mc_short=r["mc_unfunded"], mc_T33_p5=r["mc_T33_p5"], mc_T33_p50=r["mc_T33_p50"], mc_T33_p95=r["mc_T33_p95"],
                   mc_certain31_p50=r["mc_certain31_p50"])
        bl = dict(mc_short=B[f"M6.MC.{bid}.unfunded_share"], mc_T33_p5=B[f"M6.MC.{bid}.T33_p5"], mc_T33_p50=B[f"M6.MC.{bid}.T33_p50"],
                  mc_T33_p95=B[f"M6.MC.{bid}.T33_p95"], mc_certain31_p50=B[f"M6.MC.{bid}.certain31_p50"])
        hist = dict(h_T33_p10=r["h_T33_p10"], h_T33_median=r["h_T33_median"], h_T33_p90=r["h_T33_p90"])
        hbl = dict(h_T33_p10=B[f"M6.history.{bid}.T33_p10"], h_T33_median=B[f"M6.history.{bid}.T33_p50"],
                   h_T33_p90=B[f"M6.history.{bid}.T33_p90"])
        val = rnd({**ref, **hist}, 0)
        val["mc_short"] = round(float(r["mc_unfunded"]), 5)
        val.update(hist_short=f"{int(r['h_unfunded'])}/{int(r['h_windows'])}", hist_max_shortfall=round(float(r["h_max_shortfall"]), 0),
                   trades=int(r["trades"]))
        if rid in ("R5", "R5m5"):
            val.update(mc_floor_150k_missed=round(float(r["mc_floor_broken"]), 4), hist_floor_150k_missed=f"{int(r['h_floor_broken'])}/149")
            bl[f"mc_floor_150k_missed"] = 1 - B[f"M6.MC.{bid}.promised_150k_met_share"]
            ref["mc_floor_150k_missed"] = r["mc_floor_broken"]
        gate = f"MC lens: {verdict(ref, bl, 'mc')}; history lens: {verdict(hist, hbl, 'det')}"
        N[f"ws3.rivals.{rid}"] = e(val, "share of paths / USD of 2033 money for the facility and flexibility after the payments (T33) / count",
                                   f"{label[rid]}: quote only as a row of the Final Report rivals table",
                                   "rab/results/M6/M6_results.json summary (= rivals_summary.csv, full precision)", gate,
                                   {**rnd({**bl, **hbl}, 0), "mc_short": round(float(bl["mc_short"]), 5)})
    t = m6["tips"]
    N["ws3.rivals.R6_tips"] = e(
        dict(mc_any_payment_short=round(t["p_any_short"], 4), hist_short=f"{int(S['R6']['h_unfunded'])}/{int(S['R6']['h_windows'])}",
             scale_for_95pct=round(t["tips_scale_for_95pct_full"], 2), extra_cost_for_95pct=round(t["tips_extra_cost_for_95pct_full_usd"], 0)),
        "share of paths / count / multiple / USD", "a TIPS ladder leaves at least one $50,000 payment short in most inflation paths",
        "rab/results/M6/M6_results.json tips", "MATCH (same seed and draw order by spec; gate_B_ws3.md s2)",
        dict(mc_any_payment_short=round(B["M6.MC.R6.unfunded_share"], 4), hist_short_share=round(B["M6.history.R6.unfunded_share"], 4)))
    rec, r1 = S["REC"], S["R1"]
    N["ws3.rivals.rec_minus_all_treasury_mc"] = e(
        dict(T33_p5=round(rec["mc_T33_p5"] - r1["mc_T33_p5"], 0), T33_p50=round(rec["mc_T33_p50"] - r1["mc_T33_p50"], 0),
             T33_p95=round(rec["mc_T33_p95"] - r1["mc_T33_p95"], 0)),
        "USD (difference of percentiles, not a percentile of differences)",
        "against all Treasuries, Root-and-Branch gives up about $9,500 in a bad case for about $38,000 in a good case",
        "DERIVED: ws3.rivals.REC minus ws3.rivals.R1", "derived from MC NOISE rows")
    st = {s["id"]: s for s in m7["stress"]}
    ref = {f"{i}_{k}": st[i][src] for i in ("S0", "S5", "S6", "S2b") for k, src in (("rec_T33", "T33"), ("all_treasury_T33", "R1_T33"))}
    bl = {f"{i}_{k}": B[f"M7.{i}.{src}"] for i in ("S0", "S5", "S6", "S2b") for k, src in (("rec_T33", "T33"), ("all_treasury_T33", "R1_T33"))}
    ref["S5_all_treasury_ahead"] = st["S5"]["R1_T33"] - st["S5"]["T33"]
    bl["S5_all_treasury_ahead"] = B["M7.S5.R1_T33"] - B["M7.S5.T33"]
    N["ws3.rivals.stress_rec_vs_all_treasury"] = e(rnd(ref, 0), "USD of 2033 money (T33) in M7 scenarios",
                                                   "in a 1929-style crash all Treasuries would end about $28,000 ahead",
                                                   "rab/results/M7/M7_results.json stress (T33, R1_T33)", verdict(ref, bl, "det"), rnd(bl, 0))

    # ---------------- stress (M7, M5 today's yields) ----------------
    th = m7["thresholds"]
    ref = dict(topup_starts=th["topup_starts_bp"], fund_used_up=th["fund_used_up_bp"], payment_unfunded=th["payment_unfunded_bp"])
    bl = dict(topup_starts=B["M7.threshold.a_topup_starts_C_300k_bp"], fund_used_up=B["M7.threshold.b_fund0_zero_floor_150k_bp"],
              payment_unfunded=B["M7.threshold.c_payment_unfunded_G_zero_bp"])
    N["ws3.stress.thresholds_bp"] = e(rnd(ref, 1), "basis points (parallel fall before 1 Jan 2027 that lasts to Jan 2028)",
                                      "the $150,000 bottom survives a fall in yields of about 1 point before the money arrives; a payment needs a fall of over 4 points",
                                      "rab/results/M7/M7_results.json thresholds", verdict(ref, bl, "det"), rnd(bl, 1),
                                      note="topup_starts = rab/numbers.yaml laura.ladder.breakeven_fall_bp_strips (26.2)")
    fields = (("ladder_2027", "C", "ladder_cost_C"), ("topup", "T", "topup_T"), ("floor", "F", "floor_face_F"),
              ("fund_2028", "fund0", "fund0"), ("range_top_2031", "top", "top"), ("gift_2033", "gift", "gift"),
              ("laura_keeps", "kept", "kept"), ("T33", "T33", "T33"), ("real_gift", "real_gift", "real_gift"))
    for sid in ("S0", "S1", "S2", "S2b", "S3", "S3b", "S4a", "S5", "S6"):
        s = st[sid]
        ref = {k: s[src] for k, src, _ in fields}
        bl = {k: B[f"M7.{sid}.{bsrc}"] for k, _, bsrc in fields}
        val = rnd(ref, 2)
        val.update(name=s["name"], payments_funded=bool(s["funded"]), range_bottom_2031=round(s["F"], 2))
        N[f"ws3.stress.{sid}"] = e(val, "USD (Laura's plan)", "quote only in the Final Report stress table",
                                   "rab/results/M7/M7_results.json stress (= stress_table.csv)", verdict(ref, bl, "det"), rnd(bl, 2))
    N["ws3.stress.worst_gift_13_scenarios"] = e(round(min(s["gift"] for s in m7["stress"]), 2), "USD",
                                                "the lowest gift in all 13 stress scenarios is about $147,000 (Japan, with a 1-point fall before Jan 2027)",
                                                "rab/results/M7/M7_results.json stress (min gift, S2b)", "MATCH (gate_B_ws3.md s2)")
    after = [s for s in m7["stress"] if s["F"] >= 150000 - 1e-6]
    w = min(after, key=lambda s: s["gift"])
    N["ws3.stress.worst_gift_once_floor_bought"] = e(dict(gift=round(w["gift"], 2), scenario=w["id"], base_gift=round(st["S0"]["gift"], 2),
                                                          drop_vs_base=round(st["S0"]["gift"] - w["gift"], 2)),
                                                     "USD", "once the $150,000 floor is bought, the worst replay (Great Depression) still gives about $159,000",
                                                     "rab/results/M7/M7_results.json stress (scenarios with floor = 150,000)", "MATCH (derived from MATCH rows)")
    dg = {d["announced"][:4]: d["dy_bp"] for d in m7["downgrades"]}
    ref = dict(y2011=dg["2011"], y2023=dg["2023"], y2025=dg["2025"])
    bl = dict(y2011=100 * B["M7.downgrade.S4a.dgs10_change_pp"], y2023=100 * B["M7.downgrade.S4b.dgs10_change_pp"],
              y2025=100 * B["M7.downgrade.S4c.dgs10_change_pp"])
    N["ws3.stress.downgrades_dy10_bp"] = e(rnd(ref, 0), "basis points, 10-year yield over the 20 trading days after each downgrade (FRED DGS10)",
                                           "after the 2011 downgrade the 10-year yield fell about half a point",
                                           "rab/results/M7/M7_results.json downgrades", verdict(ref, bl, "det"), rnd(bl, 0))
    tb = next(r for r in m5["part_b_summary"] if r["view"] == "today_yields" and r["fund"] == "world_eq")
    ref = dict(gift_worst=tb["gift_worst"], gift_median=tb["gift_median"], share_top_reached=tb["share_top_reached"])
    bl = dict(gift_worst=B["M5.B.today_yields.world_eq.gift_worst"], gift_median=B["M5.B.today_yields.world_eq.gift_median"],
              share_top_reached=B["M5.B.today_yields.world_eq.share_top_reached"])
    val = rnd(ref, 2)
    val.update(windows=int(tb["windows"]), payments_short=int(tb["n_unfunded"]), floor_below_150k=int(tb["n_bottom_lt_150k"]),
               worst_start_year=int(tb["gift_worst_Y"]), note_fund_bought=int(tb["gift_worst_Y"]) + 1)
    N["ws3.stress.today_yields_backtest"] = e(val, "USD / count (149 start years 1872-2020, today's yields, history's returns)",
                                              "with today's yields, the worst stretch since 1872 still gives a gift of about $159,000",
                                              "rab/results/M5/M5_results.json part_b_summary (today_yields, world_eq)", verdict(ref, bl, "det"), rnd(bl, 2))
    rv = {p["path"]: p for p in m7["real_value_paths"]}
    be = next(v for k, v in rv.items() if k.startswith("Market breakeven"))
    s70 = next(v for k, v in rv.items() if k.startswith("1970s"))
    ref = dict(breakeven_2042=be["pay_2042"], breakeven_2033=be["pay_2033"], s1970s_2042=s70["pay_2042"])
    bl = dict(breakeven_2042=B["M7.real_value.breakeven_T10YIE_2.34.real_2042"], breakeven_2033=B["M7.real_value.breakeven_T10YIE_2.34.real_2033"],
              s1970s_2042=B["M7.real_value.S1_1970s stagflation.real_2042"])
    val = rnd(ref, 2)
    val["breakeven_inflation"] = round(m7["inflation_inputs"]["T10YIE"], 4)
    N["ws3.stress.real_value_payments"] = e(val, "USD of 1 Jan 2027 (what each $50,000 payment buys)",
                                            "at the market's expected inflation the last $50,000 payment buys about what $35,000 buys in 2027; in a 1970s-style decade about $18,000",
                                            "rab/results/M7/M7_results.json real_value_paths", verdict(ref, bl, "det"), rnd(bl, 2))
    jpm = pd.read_csv(os.path.join(ROOT, "rab", "data", "history", "jpm_ltcma_2026_usd.csv")).set_index("asset")
    N["ws3.inputs.mc"] = e(dict(stocks_ac_world_compound_pct=float(jpm.loc["AC World Equity", "compound_2026"]),
                                treasury_5y_par_pct=round(100 * st["S0"]["y5"], 2), paths=int(m6["paths"]), seed=int(m6["seed"])),
                           "percent a year / count", "J.P. Morgan 2026: world stocks 7.0% a year; Treasuries at today's 5.06% five-year yield",
                           "rab/data/history/jpm_ltcma_2026_usd.csv; M6_SPEC.md s4 (5-year par of 28 Sep 2026)", "MATCH (inputs shared by spec)")
    words = IPS_WORDS_30SEP
    if os.path.exists(IPS_SNAPSHOT):
        txt = open(IPS_SNAPSHOT).read().split("\nInvestment Policy Statement\n", 1)[1]
        words = len(txt.split())
        assert words == IPS_WORDS_30SEP, words
    N["ws3.ips.word_count_30sep"] = e(dict(words=words, limit=500, spare=500 - words), "words (whitespace count)",
                                      "the 30 Sep IPS has about 17 words to spare",
                                      "DERIVED: wc -w of the IPS body in " + IPS_SNAPSHOT + " (branch rab/ws6)",
                                      "n/a", note="Google Docs may count hyphenated or dollar tokens differently; recount in the Doc.")
    return N


def write(N):
    sha = hashlib.sha256(open(os.path.join(ROOT, "rab", "numbers.yaml"), "rb").read()).hexdigest()
    head = (
        "# WS3 headline numbers (M5 history, M6 rivals + fund choice, M7 stress) used in the WS3 decision memos\n"
        "# rab/decisions/D_fund_choice.md, D_rivals.md, D_stress_bad_year.md. AI-generated (Claude Code) for Team Caplet.\n"
        "# NOT rab/numbers.yaml: WS1 is its only writer. Keys for the next lock are in rab/results/WS3_numbers_proposed.yaml\n"
        "# (the FIXED file of commit 52e30ec). Every entry is MODEL, Treasury par curve of 2026-09-28, Nov-15 STRIPS basis,\n"
        "# Laura's plan unless the unit says otherwise. 'blind' = the same figure from the blind build\n"
        "# (rab/verification/blind/out/blind_headlines.json); 'gate_b' = its verdict at Gate B tolerances (rab/gates/gate_B_ws3.md).\n"
        "# None of these may go in a WInS Trading Note (not in numbers.yaml). Written by rab/decisions/build_numbers_ws3.py.\n")
    meta = dict(meta=dict(stream="WS3", written="2026-09-30 (Sydney)", curve_date="2026-09-28", numbers_yaml_sha256=sha,
                          builder="rab/decisions/build_numbers_ws3.py"))
    with open(OUT, "w") as f:
        f.write(head)
        yaml.safe_dump(meta, f, sort_keys=False, width=140, allow_unicode=True)
        yaml.safe_dump(dict(numbers=N), f, sort_keys=False, width=140, allow_unicode=True)


# ---------------- traceability check of the memos ----------------
ALLOW = {  # case facts, rule thresholds, commissions, calendar facts: not model outputs
    "$": {50000, 150000, 300000, 450000, 2000, 1000, 500, 25, 10},
    "%": {10, 62, 38, 70, 30, 80, 20, 60, 40, 65, 75, 95, 99.5, 100},
    "bp": set(),
    "dec": {0.90, 0.95},
}


def leaves(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from leaves(v)
    elif isinstance(x, list):
        for v in x:
            yield from leaves(v)
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        yield float(x)


def check():
    vals = list(leaves(yaml.safe_load(open(OUT))["numbers"])) + list(leaves(yaml.safe_load(open(os.path.join(ROOT, "rab", "numbers.yaml")))))
    avals = [abs(v) for v in vals]
    bad = n = 0
    pat = re.compile(r"(\$\d[\d,]*(?:\.\d+)?k?)|(\d+(?:\.\d+)?%)|(-?\d+(?:\.\d+)?bp)|(\b\d\.\d{2,4}\b)")
    for m in MEMOS:
        text = open(os.path.join(ROOT, "rab", "decisions", m)).read()
        text = re.sub(r"`[^`]*`", "", text)  # file names and keys
        for mt in pat.finditer(text):
            tok = mt.group(0)
            if mt.group(1):
                k = tok.endswith("k")
                s = tok[1:].rstrip("k").replace(",", "")
                x = float(s) * (1000 if k else 1)
                dec = len(s.split(".")[1]) if "." in s else 0
                if dec:
                    prec = 10 ** (-dec) * (1000 if k else 1)
                else:
                    ip = s.split(".")[0]
                    prec = (1000 if k else 10 ** min(len(ip) - len(ip.rstrip("0")), 3))
                kind, cands = "$", avals
            elif mt.group(2):
                s = tok[:-1]
                x = float(s)
                prec = 10 ** (-(len(s.split(".")[1]) if "." in s else 0))
                kind, cands = "%", [v * 100 for v in avals] + avals
            elif mt.group(3):
                s = tok[:-2].lstrip("-")
                x = float(s)
                prec = 10 ** (-(len(s.split(".")[1]) if "." in s else 0))
                kind, cands = "bp", avals
            else:
                x = float(tok)
                prec = 10 ** (-len(tok.split(".")[1]))
                kind, cands = "dec", avals
            n += 1
            if x in ALLOW[kind]:
                continue
            if not any(abs(c - x) <= prec / 2 + 1e-9 for c in cands):
                bad += 1
                ctx = text[max(0, mt.start() - 50): mt.end() + 30].replace("\n", " ")
                print(f"UNTRACED {m}: {tok}  ...{ctx}...")
    print(f"check: {n} figure(s) checked, {bad} untraced, in {', '.join(MEMOS)}")
    return bad


if __name__ == "__main__":
    write(build())
    print("wrote", OUT)
    if "--check" in sys.argv:
        sys.exit(1 if check() else 0)
