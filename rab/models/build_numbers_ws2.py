"""Build rab/numbers_ws2.yaml: WS2 headline numbers for the three decision memos in rab/decisions/.

Reads only files already produced and reconciled at Gate B (rab/gates/gate_B_ws2.md): the primary results in
rab/results/M3, M4, M8, the blind rebuild in rab/verification/blind_ws2/out, and the Gate B check outputs. No model is
re-run here. For every entry the primary value is `value` and, where the blind build has the same quantity, the
blind value is `blind` with a verdict against the Gate B tolerances (dollars +-2%, probabilities +-2 points,
shares 0.02). Entries marked DERIVED are simple arithmetic on reconciled keys.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/models/build_numbers_ws2.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / "rab" / "results"
BLIND = ROOT / "rab" / "verification" / "blind_ws2" / "out"
GB = ROOT / "rab" / "verification" / "gateB_ws2"
OUT = ROOT / "rab" / "numbers_ws2.yaml"
MODELS = ["T", "BOOT", "BAYES"]  # the three decision models (M4_SPEC PR-2); L is reference only
F = 150_000.0

BASIS = ("Laura's plan, MODEL, Treasury par curve of 2026-09-28, Nov-15 STRIPS basis; stock fund B0 = $40,736 on "
         "2 Jan 2028; floor $150,000 face; share 1/2 unless stated; no fees unless stated; 200,000 paths per model, "
         "seed 20260930")


def r0(x):
    return int(round(float(x)))


def p4(x):
    return round(float(x), 4)


def verdict(primary, blind, kind):
    """Gate B tolerances (rab/gates/gate_B_ws2.md s2)."""
    if blind is None:
        return "primary only"
    a, b = float(primary), float(blind)
    if a == b:
        return "MATCH"
    if kind == "usd":
        ok = abs(a - b) <= 0.02 * max(abs(a), abs(b))
    elif kind == "prob":
        ok = abs(a - b) <= 0.02
    elif kind == "share":
        ok = abs(a - b) <= 0.02
    else:
        raise ValueError(kind)
    return "WITHIN TOL" if ok else "OUTSIDE TOL"


def worst(verdicts):
    order = ["OUTSIDE TOL", "primary only", "WITHIN TOL", "MATCH"]
    for v in order:
        if v in verdicts:
            return v
    return "MATCH"


def main():
    m3 = pd.read_csv(RES / "M3" / "summary.csv").set_index("model")
    dec = pd.read_csv(RES / "M4" / "decision.csv").set_index("model")
    prof = pd.read_csv(RES / "M4" / "s_profile.csv")
    prof["s"] = prof["s"].round(2)
    bprof = pd.read_csv(BLIND / "M4" / "s_profile.csv")
    bprof["s"] = bprof["s"].round(2)
    rule = pd.read_csv(RES / "M4" / "rule_sensitivity.csv")
    floor = pd.read_csv(RES / "M4" / "floor_delivery.csv")
    sob_b = pd.read_csv(RES / "M8" / "sobol_B.csv")
    sob_a = pd.read_csv(RES / "M8" / "sobol_A_top2031.csv")
    torn = pd.read_csv(RES / "M8" / "tornado.csv").set_index("input")
    btorn = pd.read_csv(BLIND / "M8" / "tornado.csv")
    fread = pd.read_csv(RES / "M8" / "floor_reading.csv").set_index("d_bp")
    bfread = pd.read_csv(BLIND / "M8" / "floor_reading.csv")
    must = pd.read_csv(RES / "M8" / "must_state.csv")
    gbt = pd.read_csv(GB / "gateB_ws2_table.csv").set_index("key")
    gbj = json.loads((GB / "gateB_ws2_results.json").read_text())
    nyaml = (ROOT / "rab" / "numbers.yaml").read_bytes()

    def row(df, model, s):
        r = df[(df["model"] == model) & (df["s"] == s)]
        assert len(r) == 1, (model, s, len(r))
        return r.iloc[0]

    def gb(key):
        return gbt.loc[key, "verdict"] if key in gbt.index else "not in Gate B table"

    n = {}
    checks = []

    # ------------------------------------------------------------------ D6: the cap share
    n["ws2.d6.decision_share"] = dict(
        value=float(dec.loc["ROBUST", "recommendation"]), unit="share of the stock fund's 2031 value",
        quote_as="keep half (D6, to ratify at the 26 Oct meeting)",
        what="pre-registered rule PR-7 (M4_SPEC s5, commit 3d98ce0): keep 1/2 if the robust s* is in 0.40-0.60",
        source="rab/results/M4/decision.csv (ROBUST.recommendation)", gate_b=gb("M4.PR7_recommendation"))

    sstar = {m: float(dec.loc[m, "s_star"]) for m in MODELS}
    sstar["robust"] = float(dec.loc["ROBUST", "s_star"])
    ns = gbj["noise_band"]
    n["ws2.d6.s_star"] = dict(
        value=sstar, unit="share (largest s on a 0.01 grid passing PR-4 and PR-5)",
        quote_as="the largest share that passes both tests is 0.47-0.50 (MODEL)",
        what="M4 s* per decision model; robust = the smallest of the three",
        source="rab/results/M4/decision.csv (s_star)",
        extra_seeds_values_seen={m: ns[m]["s_star_values"] for m in MODELS if m in ns},
        extra_seeds_source="rab/verification/gateB_ws2/gateB_ws2_results.json noise_band (10 more seeds, 2M paths)",
        gate_b=worst([gb(f"M4.s_star.{m}") for m in MODELS] + [gb("M4.s_star_robust")]))

    # options table: s = 0.33 (about 1/3), 0.47, 0.50, 0.67 (about 2/3), 0.75, 1.00
    opts, bopts, vs = {}, {}, []
    for s in [0.33, 0.47, 0.50, 0.67, 0.75, 1.00]:
        o, bo = {}, {}
        for m in MODELS:
            p, b = row(prof, m, s), row(bprof, m, s)
            o[m] = dict(E_gift=r0(p["EG"]), P_keep_10pct=p4(p["P_flex"]), kept_p5=r0(p["K_p5"]),
                        kept_p50=r0(p["K_p50"]), P_gift_below_145k=p4(p["P_D"]))
            bo[m] = dict(E_gift=r0(b["E_G"]), P_keep_10pct=p4(b["P_K_ge_thr_G"]), kept_p5=r0(b["K_p5"]),
                         kept_p50=r0(b["K_p50"]), P_gift_below_145k=p4(b["P_G_lt_L"]))
            vs += [verdict(p["EG"], b["E_G"], "usd"), verdict(p["P_flex"], b["P_K_ge_thr_G"], "prob"),
                   verdict(p["P_D"], b["P_G_lt_L"], "prob")]
            if p["K_p5"] > 0 or b["K_p5"] > 0:
                vs.append(verdict(p["K_p5"], b["K_p5"], "usd"))
        opts[f"s={s:.2f}"] = o
        bopts[f"s={s:.2f}"] = bo
    checks.append(("options table primary vs blind", worst(vs)))
    n["ws2.d6.options"] = dict(
        value=opts, blind=bopts, unit="USD / probability",
        quote_as="see the D6 memo table (round to $1k; probabilities to whole percent)",
        what="expected 2033 gift, chance Laura keeps >= 10% of her gift, kept money p5 / p50, chance the gift is "
             "below the announced $145,000, by share s",
        source="rab/results/M4/s_profile.csv; blind rab/verification/blind_ws2/out/M4/s_profile.csv",
        gate_b=f"{worst(vs)} (compared here against the blind s_profile.csv with the Gate B tolerances)")

    pd_max = float(prof[prof["model"].isin(MODELS)]["P_D"].max())
    bpd_max = float(bprof[bprof["model"].isin(MODELS)]["P_G_lt_L"].max())
    n["ws2.d6.p_gift_below_145k_any_share"] = dict(
        value=pd_max, blind=bpd_max, unit="probability (largest over s = 0.00-1.00 and the three models)",
        quote_as="no model path puts the gift below $145,000 at any share (0 in 200,000 per model; not proof)",
        source="rab/results/M4/s_profile.csv (P_D); blind s_profile.csv (P_G_lt_L)",
        gate_b=verdict(pd_max, bpd_max, "prob"))

    cost47 = {m: r0(row(prof, m, 0.50)["EG"] - row(prof, m, 0.47)["EG"]) for m in MODELS}
    n["ws2.d6.half_vs_047_expected_gift"] = dict(
        value=cost47, unit="USD (E[gift] at 1/2 minus at 0.47)", status="DERIVED",
        quote_as="about $1,500 more expected gift at half than at 0.47 (MODEL)",
        source="rab/results/M4/s_profile.csv (EG at s = 0.50 and 0.47)", gate_b="DERIVED from WITHIN TOL rows")

    def robust(k, c):
        vals = rule[(rule["kappa"] == k) & (rule["confidence"] == c) & rule["model"].isin(MODELS)]["s_star"]
        return None if vals.isna().any() else float(vals.min())
    def pr7(x):
        """M4_SPEC PR-7: the share the rule would recommend for a robust s* of x."""
        if x is None:
            return None
        if 0.40 <= x <= 0.60:
            return 0.5
        if x > 0.60:
            return max(c for c in (2 / 3, 0.75, 1.0) if c <= x + 1e-12)
        if x >= 0.25:
            return max(c for c in (0.25, 1 / 3) if c <= x + 1e-12)
        return round(int(round(x * 100)) // 5 * 0.05, 2)

    rs = {"keep5pct_at95": robust(0.05, 0.95), "keep10pct_at95": robust(0.10, 0.95),
          "keep15pct_at95": robust(0.15, 0.95), "keep10pct_at99": robust(0.10, 0.99),
          "keep20pct_at95": robust(0.20, 0.95)}
    n["ws2.d6.rule_sensitivity"] = dict(
        value=rs, pr7_recommends={k: (None if v is None else round(pr7(v), 4)) for k, v in rs.items()},
        unit="robust s* over the three decision models; pr7_recommends = the share PR-7 would then give",
        quote_as="a 5% cushion would allow about 2/3; a 15% cushion about 1/5 (MODEL)",
        source="rab/results/M4/rule_sensitivity.csv",
        gate_b=worst([gb(f"M4.rule_sensitivity.thr{k}_conf{c}") for k in (0.05, 0.1, 0.15, 0.2)
                      for c in (0.9, 0.95, 0.99)]))

    # ------------------------------------------------------------------ 2031 range: stated confidence
    within = {m: float(m3.loc[m, "P_G_within_range"]) for m in m3.index}
    n["ws2.range.gift_inside_range"] = dict(
        value=within, unit="probability (8 model variants x 200,000 paths = 1.6 million paths)",
        quote_as="certain by construction if the floor holding pays, the 2028 deposit arrives, the gift is capped "
                 "and no fee is taken from the floor; no model path fell outside",
        source="rab/results/M3/summary.csv (P_G_within_range)", gate_b="MATCH (gate_B_ws2.md s2)")

    f0 = floor.iloc[0]
    n["ws2.range.floor_delivery"] = dict(
        value=dict(worst=r0(F * f0["phi_min"]), median=r0(F * f0["phi_p50"]), p95=r0(F * f0["phi_p95"]),
                   best=r0(F * f0["phi_max"]), P_below_150k=p4(f0["P_phi_below_1_minus_h"])),
        unit="USD paid by a $150,000-face iBond-fund floor in late 2032 / probability",
        quote_as="the floor pays about $149,000 in a typical case and at least about $146,000; it falls short of "
                 "$150,000 about 2 times in 3 (MODEL)",
        source="rab/results/M4/floor_delivery.csv (phi x $150,000; 8,565 historical 30-month rate changes)",
        gate_b=worst([gb("M4.phi.p50"), gb("M4.phi.p95"), gb("M4.phi.max")]))

    n["ws2.range.announced_floor"] = dict(
        value=float(f0["announced_floor"]), h_star=float(f0["h_star"]), unit="USD",
        quote_as="$145,000: the floor holding's worst case, rounded down to $5,000",
        source="rab/results/M4/floor_delivery.csv (PR-3)",
        gate_b=worst([gb("M4.h_star"), gb("M4.A_announced_floor")]))

    n["ws2.range.floor_shortfall_vs_face"] = dict(
        value=dict(typical=r0(F * (1 - f0["phi_p50"])), worst=r0(F * (1 - f0["phi_min"]))),
        unit="USD below $150,000", status="DERIVED",
        quote_as="typically about $600, at most about $3,700 (MODEL)",
        source="$150,000 x (1 - phi) from rab/results/M4/floor_delivery.csv", gate_b="DERIVED from WITHIN TOL rows")

    top = {m: dict(p5=r0(m3.loc[m, "U_p5"]), p50=r0(m3.loc[m, "U_p50"]), p95=r0(m3.loc[m, "U_p95"]))
           for m in ["L"] + MODELS}
    n["ws2.range.top2031"] = dict(
        value=top, unit="USD (2031 top = $150,000 + half the fund; p5, p50, p95)",
        quote_as="a top of about $175,000 in a typical case; 90% of paths about $165,000-$190,000 (MODEL, at "
                 "28 Sep 2026 yields)",
        source="rab/results/M3/summary.csv (U_p5, U_p50, U_p95)",
        gate_b=worst([gb(f"M3.{m}.top2031_p{q}") for m in MODELS for q in (5, 50, 95)]))

    def half(col, bcol, kind, fmt):
        v = {m: fmt(row(prof, m, 0.50)[col]) for m in MODELS}
        b = {m: fmt(row(bprof, m, 0.50)[bcol]) for m in MODELS}
        vv = worst([verdict(v[m], b[m], kind) for m in MODELS])
        return v, b, vv

    v, b, vv = half("P_top_fund", "P_top_fund", "prob", p4)
    n["ws2.range.p_fund_holds_2031_to_2033"] = dict(
        value=v, blind=b, unit="probability",
        quote_as="about 3 times in 4 the stock fund is worth at least its 2031 value in 2033, and the gift then "
                 "lands at the top or within about $3,700 of it (MODEL)",
        source="rab/results/M4/s_profile.csv (P_top_fund, s = 0.50); same as M3 P_top_reached", gate_b=vv)

    v, b, vv = half("P_top", "P_top_gift_eq_U", "prob", p4)
    n["ws2.range.p_gift_equals_face_top"] = dict(
        value=v, blind=b, unit="probability",
        quote_as="with an iBond-fund floor the gift equals the $150,000-based top exactly only about 1 time in 4 "
                 "(MODEL; the floor usually pays a few hundred dollars under face)",
        source="rab/results/M4/s_profile.csv (P_top, s = 0.50)", gate_b=vv + " (T differs by 3.3 s.e.; gate_B s3 #3)")

    v, b, vv = half("E_short_top", "E_U_minus_G", "usd", r0)
    n["ws2.range.expected_short_of_top"] = dict(
        value=v, blind=b, unit="USD (average of top minus gift)",
        quote_as="on average the gift ends about $2,000 below the top (MODEL)",
        source="rab/results/M4/s_profile.csv (E_short_top, s = 0.50)", gate_b=vv)

    v, b, vv = half("P_below_middle", "P_G_below_middle", "prob", lambda x: round(float(x), 5))
    n["ws2.range.p_below_middle"] = dict(
        value=v, blind=b, unit="probability (middle of $145,000 and the top)",
        quote_as="below the middle of the range at most about 1 time in 200 (MODEL, history model)",
        source="rab/results/M4/s_profile.csv (P_below_middle, s = 0.50)", gate_b=vv)

    g = {m: dict(p5=r0(m3.loc[m, "G_p5"]), p50=r0(m3.loc[m, "G_p50"]), p95=r0(m3.loc[m, "G_p95"])) for m in MODELS}
    n["ws2.range.gift2033"] = dict(
        value=g, unit="USD (p5, p50, p95; floor paying face)",
        quote_as="a 2033 gift of about $174,000 in a typical case (MODEL)",
        source="rab/results/M3/summary.csv (G_p5, G_p50, G_p95)",
        gate_b=worst([gb(f"M3.{m}.gift2033_p{q}") for m in MODELS for q in (5, 50, 95)]))

    n["ws2.range.p_fund_below_cost_2031"] = dict(
        value={m: p4(m3.loc[m, "P_B3_below_B0"]) for m in MODELS}, unit="probability",
        quote_as="in about 1 case in 5 the fund is worth less in 2031 than it cost in 2028; the range is then "
                 "narrower but its bottom does not move (MODEL)",
        source="rab/results/M3/summary.csv (P_B3_below_B0)",
        gate_b=worst([gb(f"M3.{m}.P_B3_below_B0") for m in MODELS]))

    a2 = {m: dict(P_top=p4(row(prof, m, 0.50)["A_P_top"]),
                  E_gift_lower_by=r0(row(prof, m, 0.50)["EG"] - row(prof, m, 0.50)["A_EG"]),
                  P_keep_10pct=p4(row(prof, m, 0.50)["A_P_flex"])) for m in MODELS}
    n["ws2.range.option_top_from_145k"] = dict(
        value=a2, unit="probability / USD", status="MODEL (exploratory, not pre-registered: M4_SPEC s9 A2)",
        quote_as="if the top is also counted from $145,000, the gift reaches it about 9 times in 10, with a gift "
                 "about $3,500 lower on average (MODEL)",
        source="rab/results/M4/s_profile.csv (A_P_top, A_EG, A_P_flex at s = 0.50)",
        gate_b="P_top and E_gift WITHIN TOL (gate_B_ws2.md s2, computed on blind paths); P_keep_10pct primary only")

    nr = gbj["discrepancies"]["narrower_range"]
    worst160 = max(v2["P_D_at_160k"] for k2, v2 in nr.items() if "A_based" in k2 or "spec" in k2)
    worst165 = max(v2["P_D_at_165k"] for k2, v2 in nr.items() if "A_based" in k2 or "spec" in k2)
    n["ws2.range.narrower_low_end_breach"] = dict(
        value={"160k": p4(worst160), "165k": p4(worst165)},
        unit="probability the gift is below a raised low end (worst of 3 models, both builds, both readings)",
        status="MODEL (explored only; PR-1 never recommends it)",
        quote_as="a low end of $160,000 would be broken about 4 times in 1,000; $165,000 about 2 times in 100 "
                 "(MODEL, history model)",
        source="rab/verification/gateB_ws2/gateB_ws2_results.json discrepancies.narrower_range",
        gate_b="WITHIN TOL (gate_B_ws2.md s3 #4)")

    fr, vs = {}, []
    bf = bfread.set_index("d_bp")
    for d in (-50.0, -100.0):
        p, bb = fread.loc[d], bf.loc[d]
        fr[f"{int(d)}bp"] = dict(IPS_floor=r0(p["IPS_floor"]), IPS_fund=r0(p["IPS_fund"]),
                                 keep150k_floor=r0(p["E6_floor"]), keep150k_fund=r0(p["E6_fund"]))
        vs += [verdict(round(p[a], 2), round(bb[b2], 2), "usd") for a, b2 in
               [("IPS_floor", "IPS_floor_F"), ("IPS_fund", "IPS_fund_B0"), ("E6_floor", "E6_floor_F"),
                ("E6_fund", "E6_fund_B0")]]
    checks.append(("floor reading primary vs blind (to the cent)", worst(vs)))
    n["ws2.range.floor_reading"] = dict(
        value=fr, unit="USD (2028 floor face and stock fund, if yields fall before Jan 2027)", status="MODEL (deterministic)",
        quote_as="after a 0.5-point fall: floor $143k + fund $29k under 'the whole remainder', or floor $150k + "
                 "fund $23k under 'keep $150,000' (MODEL)",
        source="rab/results/M8/floor_reading.csv (flag F4); blind rab/verification/blind_ws2/out/M8/floor_reading.csv",
        gate_b=f"{worst(vs)} to the cent (gate_B_ws2.md s2)")

    # ------------------------------------------------------------------ the three assumptions
    sb = sob_b[sob_b["output"] == "median_top2031"].set_index("input")
    n["ws2.assume.sobol_total_index_median_top"] = dict(
        value={k: round(float(sb.loc[k, "ST"]), 3) for k in ["d", "e", "fee", "mu_c", "sd_log", "inv_nu"]},
        unit="Sobol total index ST (assumptions only; market luck fixed)",
        quote_as="yields on 1 Jan 2027 explain about 90% of the variation in the typical 2031 top; the 5-year "
                 "yield in Jan 2028 about 7%; costs about 3%; the stock-return assumption under 1% (MODEL)",
        what="d = yield move before the Jan 2027 purchase; e = 5-year yield move during 2027; fee = yearly cost "
             "on all assets paid from the fund; mu_c = stock expected return; sd_log = volatility; inv_nu = tails",
        source="rab/results/M8/sobol_B.csv (output median_top2031)",
        gate_b=worst([gb(f"M8.sobolB.median_top2031.ST.X{i}") for i in range(1, 7)]))

    tv, bv, vs = {}, {}, []
    bt = btorn.set_index(btorn["input"].str.split(" ").str[0])
    for k, bk in [("d", "X4"), ("e", "X5"), ("fee", "X6"), ("mu_c", "X1")]:
        tv[k] = dict(low_input=float(torn.loc[k, "low"]), high_input=float(torn.loc[k, "high"]),
                     median_top_at_low=r0(torn.loc[k, "top_p50_at_low"]),
                     median_top_at_high=r0(torn.loc[k, "top_p50_at_high"]))
        bv[k] = dict(median_top_at_low=r0(bt.loc[bk, "Y1_med_low"]), median_top_at_high=r0(bt.loc[bk, "Y1_med_high"]))
        vs += [verdict(tv[k]["median_top_at_low"], bv[k]["median_top_at_low"], "usd"),
               verdict(tv[k]["median_top_at_high"], bv[k]["median_top_at_high"], "usd")]
    n["ws2.assume.tornado_median_top"] = dict(
        value=tv, blind=bv, unit="USD (median 2031 top with one input at its low / high; d in bp, e in points, "
                                 "fee and mu_c as yearly rates)",
        quote_as="Jan-2027 yields (historical 95-day moves, 2.5-97.5%) move the typical top from about $143k to "
                 "$194k; the Jan-2028 5-year yield $168k-$182k; a 1% yearly cost $175k -> $167k; the stock return "
                 "(4.1%-8%) $173k-$176k (MODEL)",
        source="rab/results/M8/tornado.csv; blind rab/verification/blind_ws2/out/M8/tornado.csv", gate_b=worst(vs))

    n["ws2.assume.must_state"] = dict(
        value=must["input"].tolist(), unit="inputs, ranked by ST",
        quote_as="(1) yields when the 2027 deposit buys the ten holdings; (2) the 5-year yield when the floor is "
                 "bought in Jan 2028; (3) costs, and that the stock fund pays them",
        what="pre-registered rule M8_SPEC s3.4; the tornado and the 1-in-20 ranking agree",
        source="rab/results/M8/must_state.csv", gate_b="MATCH (gate_B_ws2.md s2)")

    luck_s1 = float(sob_a[sob_a["input"].str.startswith("u")]["S1"].sum())
    luck_st = float(sob_a[sob_a["input"].str.startswith("u")]["ST"].sum())
    n["ws2.assume.luck_share_top2031"] = dict(
        value=dict(sum_S1=round(luck_s1, 3), sum_ST=round(luck_st, 3)),
        unit="share of the variance of the 2031 top due to stock-market luck 2028-2030",
        quote_as="stock-market luck explains only about a fifth of the uncertainty in the 2031 top (MODEL)",
        source="rab/results/M8/sobol_A_top2031.csv (u1..u3)", gate_b="MATCH (gate_B_ws2.md s2 and s3 #8)")

    doc = dict(
        meta=dict(
            stream="WS2 (range + cap)", written="2026-09-30 (Sydney)", curve_date="2026-09-28", basis=BASIS,
            numbers_yaml_sha256=hashlib.sha256(nyaml).hexdigest(),
            builder="rab/models/build_numbers_ws2.py (reads reconciled results only; re-run after any model re-run)",
            gate_b="rab/gates/gate_B_ws2.md (PASS)",
            not_numbers_yaml=("NOT rab/numbers.yaml (WS1 is its only writer, PM-35). The Gate-B-reconciled "
                              "proposals are rab/results/M3/numbers_proposed.yaml and "
                              "rab/verification/gateB_ws2/numbers_proposed_M4_M8.yaml."),
            rules=["Quote the quote_as string. Round to $1k (ranges to $5k) outside appendices.",
                   "Never put a range, odds, share or $145,000 figure in a WInS Trade note.",
                   "Re-run make -f rab/models/ws2.mk all, the blind run_all.sh, gateB_ws2_checks.py and this "
                   "builder after Friday's curve refresh: the fund B0 moves with the curve."],
            checks=dict(checks)),
        numbers=n,
        static=dict(
            ips_word_count=dict(
                value=dict(body=483, limit=500), unit="words (wc -w)",
                what="IPS body text (excluding title and elevator pitch) of the IPS Report Google Doc",
                source="IPS Report Google Doc 1qtEuzXq_QYdQ9VJlusPY9km2l80E1hkk8FPR0iw71-w, read-only via the "
                       "Drive connector on 2026-09-30 (doc headed 'EXEMPLAR ONLY'); Wharton may count differently",
                status="READ 2026-09-30")),
    )
    OUT.write_text("# WS2 headline numbers for rab/decisions/D6_cap_share.md, D_range_confidence_2031.md and\n"
                   "# D_ips_three_assumptions.md. AI-generated (Claude Code) for Team Caplet. Generated by\n"
                   "# rab/models/build_numbers_ws2.py; do not edit by hand.\n"
                   + yaml.safe_dump(doc, sort_keys=False, width=118, allow_unicode=False))
    for k, v in checks:
        print(f"check: {k}: {v}")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(n)} entries + 1 static)")


if __name__ == "__main__":
    main()
