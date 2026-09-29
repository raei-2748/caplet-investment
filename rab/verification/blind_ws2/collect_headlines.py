"""Collect the blind rebuild's headline keys (M3, M4, M8) into out/blind_headlines.json and out/BLIND_HEADLINES.md.

The blind builder does not open rab/results/; WS0 (or the Gate B reconciler) compares this file with the primary
results using the tolerances quoted from the specs (M3 s6, M4 s7, M8 s4).
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"


def load(name: str) -> dict:
    with open(OUT / name) as fh:
        return json.load(fh)


def main() -> None:
    m3 = load("M3/headline_M3.json")
    m4 = load("M4/headline_M4.json")
    m8 = load("M8/headline_M8.json")

    keys = {}
    # ---- M3 (tolerance: range ends and gift percentiles within 2%; probabilities within 2 points) -----------------
    for tag in ("L", "T", "BOOT", "BAYES", "BOOT-raw", "BOOT-b1", "BOOT-b60", "BAYES-hist"):
        r = m3[tag]
        for k in ("top2031_p5", "top2031_p50", "top2031_p95", "gift2033_p5", "gift2033_p50", "gift2033_p95", "kept_p50",
                  "total_p5", "total_p50", "total_p95"):
            keys[f"M3.{tag}.{k}"] = {"value": round(r[k], 2), "unit": "USD", "tolerance": "2%"}
        for k in ("P_top_reached", "P_upper_half", "P_B3_below_B0"):
            keys[f"M3.{tag}.{k}"] = {"value": round(r[k], 4), "unit": "probability", "tolerance": "2 points"}
    for k, v in m3["bayes_posterior"].items():
        keys[f"M3.BAYES.posterior_mean.{k}"] = {"value": round(v["mean"], 4), "unit": "", "tolerance": "10% (MCMC noise)"}
    keys["M3.L.analytic_median_top"] = {"value": round(m3["L_analytic_check"]["median_top_analytic"], 2), "unit": "USD", "tolerance": "MC error"}
    keys["M3.L.analytic_P_top"] = {"value": round(m3["L_analytic_check"]["P_top_analytic"], 4), "unit": "probability", "tolerance": "MC error"}

    # ---- M4 (s* within 0.02; probabilities within 2 points; E[G], percentiles within 2%; h*, A identical) ---------
    keys["M4.h_star"] = {"value": m4["h_star"], "unit": "", "tolerance": "identical"}
    keys["M4.A_announced_floor"] = {"value": m4["A_announced_floor"], "unit": "USD", "tolerance": "identical"}
    for m, v in m4["s_star_by_model"].items():
        keys[f"M4.s_star.{m}"] = {"value": v, "unit": "share", "tolerance": "0.02"}
    keys["M4.s_star_robust"] = {"value": m4["s_star_robust"], "unit": "share", "tolerance": "0.02"}
    keys["M4.PR7_recommendation"] = {"value": m4["PR7_recommendation"], "unit": "share", "tolerance": "identical"}
    for k in ("p0.5", "p1", "p5", "p50", "p95", "max"):
        keys[f"M4.phi.{k}"] = {"value": round(m4["phi"][k], 5), "unit": "ratio", "tolerance": "2%"}
    for m, r in m4["adopted_half"].items():
        for k in ("E_G", "G_p5", "G_p50", "G_p95", "E_K", "K_p5", "K_p50", "E_width", "U_p50", "E_U_minus_G"):
            keys[f"M4.adopted_half.{m}.{k}"] = {"value": round(r[k], 2), "unit": "USD", "tolerance": "2%"}
        for k in ("P_K_ge_thr_G", "P_G_lt_L", "P_top_fund", "P_top_gift_eq_U", "P_G_below_middle"):
            keys[f"M4.adopted_half.{m}.{k}"] = {"value": round(r[k], 4), "unit": "probability", "tolerance": "2 points"}
    for k, v in m4["rule_sensitivity_s_star_robust"].items():
        keys[f"M4.rule_sensitivity.{k}"] = {"value": v, "unit": "share", "tolerance": "0.02"}
    for m, r in m4["pareto"].items():
        keys[f"M4.pareto.{m}.n_front"] = {"value": r["n_front"], "unit": "points", "tolerance": "report"}
        keys[f"M4.pareto.{m}.s_at_max_E_G_feasible"] = {"value": r["s_at_max_E_G"], "unit": "share", "tolerance": "report"}
        keys[f"M4.pareto.{m}.front_points_dominated_by_grid"] = {"value": r["front_points_dominated_by_grid"], "unit": "points", "tolerance": "report"}

    # ---- M8 (base exact; tornado medians within 1%; Sobol ST within 0.05 or the 95% interval; top-3 identical) -----
    keys["M8.base.V_A_0"] = {"value": round(m8["base"]["V_A_0"], 2), "unit": "USD", "tolerance": "exact"}
    keys["M8.base.B0"] = {"value": round(m8["base"]["B0"], 2), "unit": "USD", "tolerance": "exact"}
    keys["M8.base.top2031_median"] = {"value": round(m8["base"]["top2031_median"], 2), "unit": "USD", "tolerance": "1%"}
    keys["M8.base.top2031_p5"] = {"value": round(m8["base"]["top2031_p5"], 2), "unit": "USD", "tolerance": "1%"}
    keys["M8.base.gift2033_median"] = {"value": round(m8["base"]["gift2033_median"], 2), "unit": "USD", "tolerance": "1%"}
    ir = m8["input_ranges"]
    keys["M8.X4_d_bp_2.5_97.5"] = {"value": [round(x, 2) for x in ir["X4_d_bp_2.5_97.5"]], "unit": "bp", "tolerance": "data (exact)"}
    keys["M8.X5_e_pts_2.5_97.5"] = {"value": [round(x, 4) for x in ir["X5_e_pts_2.5_97.5"]], "unit": "points", "tolerance": "data (exact)"}
    for r in m8["tornado"]:
        nm = r["input"].split(" ")[0] if r["input"] not in ("BASE",) else "BASE"
        if nm.startswith("REF"):
            nm = "REF_" + ("s_lever" if "lever" in r["input"] else "return_model")
        keys[f"M8.tornado.{nm}.Y1_med_low"] = {"value": round(r["Y1_med_low"], 2), "unit": "USD", "tolerance": "1%"}
        keys[f"M8.tornado.{nm}.Y1_med_high"] = {"value": round(r["Y1_med_high"], 2), "unit": "USD", "tolerance": "1%"}
        keys[f"M8.tornado.{nm}.swing_Y1_med"] = {"value": round(r["swing_Y1_med"], 2), "unit": "USD", "tolerance": "1% of medians"}
    keys["M8.tornado.rank"] = {"value": m8["tornado_rank"], "unit": "order", "tolerance": "top-3 identical"}
    for r in m8["sobol_A_top2031"]:
        keys[f"M8.sobolA.top2031.ST.{r['input'].split(' ')[0]}"] = {"value": round(r["ST"], 4), "unit": "index", "tolerance": f"0.05 or 95% CI +-{r['ST_conf95']:.3f}"}
    for r in m8["sobol_A_gift2033"]:
        keys[f"M8.sobolA.gift2033.ST.{r['input'].split(' ')[0]}"] = {"value": round(r["ST"], 4), "unit": "index", "tolerance": f"0.05 or 95% CI +-{r['ST_conf95']:.3f}"}
    keys["M8.sobolA.top2031.luck_share_S1"] = {"value": round(m8["sobol_A_top2031_luck_share_S1"], 4), "unit": "share", "tolerance": "0.05"}
    keys["M8.sobolA.gift2033.luck_share_S1"] = {"value": round(m8["sobol_A_gift2033_luck_share_S1"], 4), "unit": "share", "tolerance": "0.05"}
    for r in m8["sobol_B"]:
        keys[f"M8.sobolB.{r['output']}.ST.{r['input'].split(' ')[0]}"] = {"value": round(r["ST"], 4), "unit": "index", "tolerance": f"0.05 or 95% CI +-{r['ST_conf95']:.3f}"}
        keys[f"M8.sobolB.{r['output']}.S1.{r['input'].split(' ')[0]}"] = {"value": round(r["S1"], 4), "unit": "index", "tolerance": f"0.05 or 95% CI +-{r['S1_conf95']:.3f}"}
    v = m8["ips_must_state"]
    keys["M8.ips_must_state.top3"] = {"value": v["top3_by_sobolB_median_ST"], "unit": "inputs", "tolerance": "identical"}
    keys["M8.ips_must_state.p5_agrees"] = {"value": v["p5_agrees"], "unit": "bool", "tolerance": "report"}
    keys["M8.ips_must_state.tornado_agrees"] = {"value": v["tornado_agrees"], "unit": "bool", "tolerance": "report"}
    for r in m8["floor_reading"]:
        d = int(r["d_bp"])
        for k in ("V_A", "IPS_floor_F", "IPS_fund_B0", "E6_floor_F", "E6_fund_B0"):
            keys[f"M8.floor_reading.d{d}.{k}"] = {"value": round(r[k], 2), "unit": "USD", "tolerance": "exact"}

    with open(OUT / "blind_headlines.json", "w") as fh:
        json.dump(keys, fh, indent=1)
    lines = ["# Blind rebuild headline keys (WS2: M3, M4, M8)", "",
             "Built from the SPEC files only; compare against rab/results/ with the tolerance in the last column (Gate B).", "",
             "| key | value | unit | tolerance |", "|---|---|---|---|"]
    for k, r in keys.items():
        val = r["value"]
        if isinstance(val, float):
            val = f"{val:,.4f}" if abs(val) < 10 else f"{val:,.2f}"
        lines.append(f"| {k} | {val} | {r['unit']} | {r['tolerance']} |")
    (OUT / "BLIND_HEADLINES.md").write_text("\n".join(lines) + "\n")
    print(f"{len(keys)} headline keys -> {OUT/'blind_headlines.json'}, {OUT/'BLIND_HEADLINES.md'}")


if __name__ == "__main__":
    main()
