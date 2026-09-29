"""Blind M3: the Branch 2028-2033 under four return models (M3_SPEC.md). Writes out/M3/.

Run: /Users/ray/Research/rab-ws/.venv/bin/python blind_m3.py
"""
from __future__ import annotations

import math
import sys
import time

import numpy as np
import pandas as pd

import blind_common as bc

OUT = bc.OUT / "M3"
OUT.mkdir(parents=True, exist_ok=True)
N = bc.N_PATHS
F, S, B0 = bc.F_FLOOR, bc.S_ADOPTED, bc.B0

HEADLINE_MODELS = ["T", "BOOT", "BAYES"]
ALL_MODELS = ["L", "T", "BOOT", "BAYES", "BOOT-raw", "BOOT-b1", "BOOT-b60", "BAYES-hist"]


def summarise(tag: str, x: np.ndarray) -> dict:
    o = bc.outcomes(x)
    row = {"model": tag}
    for key in ("B3", "U", "G", "K", "T"):
        row.update(bc.pct_row(o[key], key))
    row["P_top_reached"] = float((o["B5"] >= o["B3"]).mean())
    row["P_upper_half"] = float((o["B5"] / o["B3"] >= 0.5).mean())
    row["median_position_p"] = float(np.median(o["p"]))
    row["P_B3_below_B0"] = float((o["B3"] < B0).mean())
    row["P_G_ge_F"] = float((o["G"] >= F - 1e-9).mean())
    row["realised_mean_log_return"] = float(x.mean())
    row["realised_sd_log_return"] = float(x.std(ddof=1))
    return row


def main() -> None:
    t0 = time.time()
    log = []
    say = lambda s: (print(s, flush=True), log.append(s))

    # --- paths -------------------------------------------------------------------------------------------------
    c_T, disc = bc.t_scale_c()
    say(f"T scale c = {c_T:.7f}; raw draws discarded {100*disc:.3f}%")
    r_m = bc.load_shiller_monthly()
    y_m = np.log1p(r_m)
    say(f"Shiller monthly: n={r_m.shape[0]}, mean log {y_m.mean():.6f} (x12 {12*y_m.mean():.4f}), sd {y_m.std(ddof=1):.5f}")
    z_a = bc.load_shiller_annual()

    paths = {}
    paths["L"] = bc.paths_L(bc.rng_for("L"), N)
    paths["T"] = bc.paths_T(bc.rng_for("T"), N, c_T)
    paths["BOOT"] = bc.paths_BOOT(bc.rng_for("BOOT"), N, r_m, mean_block=24, recentre=True)
    paths["BOOT-raw"] = bc.paths_BOOT(bc.rng_for("BOOT-raw"), N, r_m, mean_block=24, recentre=False)
    paths["BOOT-b1"] = bc.paths_BOOT(bc.rng_for("BOOT-b1"), N, r_m, mean_block=1, recentre=True)
    paths["BOOT-b60"] = bc.paths_BOOT(bc.rng_for("BOOT-b60"), N, r_m, mean_block=60, recentre=True)

    say("BAYES: fitting StudentT to 155 annual log returns (pymc NUTS, 4 x (1000 + 1000), target_accept 0.9) ...")
    t1 = time.time()
    post, summ, ok = bc.fit_bayes_history(z_a)
    say(f"BAYES fit done in {time.time()-t1:.0f}s; converged={ok}")
    print(summ)
    if not ok:
        say("STOP: r_hat > 1.01 or ESS < 400 (M3_SPEC s3 requires convergence)")
        sys.exit(2)
    bp = []
    for k in ("m_h", "sigma", "nu"):
        v = post[k]
        bp.append({"param": k, "mean": v.mean(), "sd": v.std(ddof=1), "p5": np.percentile(v, 5),
                   "p95": np.percentile(v, 95), "r_hat": float(summ.loc[k, "r_hat"]),
                   "ess_bulk": float(summ.loc[k, "ess_bulk"])})
    pd.DataFrame(bp).to_csv(OUT / "bayes_posterior.csv", index=False)
    np.savetxt(OUT / "bayes_posterior_draws.csv", np.column_stack([post["m_h"], post["sigma"], post["nu"]]),
               delimiter=",", header="m_h,sigma,nu", comments="")
    paths["BAYES"] = bc.paths_BAYES(bc.rng_for("BAYES"), N, post)
    paths["BAYES-hist"] = bc.paths_BAYES(bc.rng_for("BAYES-hist"), N, post, hist_mean=True)
    for tag, x in paths.items():
        bc.save_paths(tag, x)

    # --- 1. summary.csv ------------------------------------------------------------------------------------------
    rows = [summarise(tag, paths[tag]) for tag in ALL_MODELS]
    summary = pd.DataFrame(rows)
    summary.to_csv(OUT / "summary.csv", index=False)

    # analytic checks for L (M3_SPEC s6)
    med_top_L = F + S * B0 * math.exp(3 * bc.MU_L)
    p_top_L = 0.5 * (1 + math.erf(math.sqrt(2) * bc.MU_L / bc.SIG_L / math.sqrt(2)))  # Phi(sqrt2 mu/sig)
    rL = summary.set_index("model").loc["L"]
    say(f"L check: median top {rL['U_p50']:,.0f} vs analytic {med_top_L:,.0f}; P(top) {rL['P_top_reached']:.4f} vs {p_top_L:.4f}")

    # --- 2. range_confidence.csv ---------------------------------------------------------------------------------
    rc = []
    for tag in ALL_MODELS:
        o = bc.outcomes(paths[tag])
        rc.append({"model": tag, "bottom": F, "bottom_status": "certain by construction (M3_SPEC s5 conditions a-d)",
                   "top_p50": np.median(o["U"]), "top_p5": np.percentile(o["U"], 5), "top_p95": np.percentile(o["U"], 95),
                   "gift_p50": np.median(o["G"]), "gift_p5": np.percentile(o["G"], 5), "gift_p95": np.percentile(o["G"], 95),
                   "P_top_reached": (o["B5"] >= o["B3"]).mean(), "P_upper_half": (o["B5"] / o["B3"] >= 0.5).mean()})
    pd.DataFrame(rc).to_csv(OUT / "range_confidence.csv", index=False)

    # --- 3. conditional_top.csv (BOOT) ---------------------------------------------------------------------------
    ct = []
    for tag in ("BOOT", "BOOT-raw", "BOOT-b1", "BOOT-b60", "L"):
        o = bc.outcomes(paths[tag])
        med = np.median(o["B3"])
        top = o["B5"] >= o["B3"]
        lo, hi = o["B3"] < med, o["B3"] >= med
        ct.append({"model": tag, "P_top_given_B3_below_median": top[lo].mean(), "P_top_given_B3_above_median": top[hi].mean(),
                   "difference_pp": 100 * (top[hi].mean() - top[lo].mean()),
                   "corr_x123_x45": np.corrcoef(paths[tag][:, :3].sum(1), paths[tag][:, 3:].sum(1))[0, 1]})
    pd.DataFrame(ct).to_csv(OUT / "conditional_top.csv", index=False)

    # --- 5. reconcile_E6.csv -------------------------------------------------------------------------------------
    x_e6 = bc.paths_L(np.random.default_rng(20260927), N)
    o6 = bc.outcomes(x_e6, b0=40_400.0)
    oL = bc.outcomes(paths["L"])
    e6 = [
        {"quantity": "total_p5", "L_28sep_B0_40736": np.percentile(oL["T"], 5), "L_25sep_basis_B0_40400_seed20260927": np.percentile(o6["T"], 5), "insight_v1_E6_ref_H8": 182_000},
        {"quantity": "total_p50", "L_28sep_B0_40736": np.median(oL["T"]), "L_25sep_basis_B0_40400_seed20260927": np.median(o6["T"]), "insight_v1_E6_ref_H8": 207_000},
        {"quantity": "total_p95", "L_28sep_B0_40736": np.percentile(oL["T"], 95), "L_25sep_basis_B0_40400_seed20260927": np.percentile(o6["T"], 95), "insight_v1_E6_ref_H8": 250_000},
        {"quantity": "gift_p5", "L_28sep_B0_40736": np.percentile(oL["G"], 5), "L_25sep_basis_B0_40400_seed20260927": np.percentile(o6["G"], 5), "insight_v1_E6_ref_H8": None},
        {"quantity": "gift_p50", "L_28sep_B0_40736": np.median(oL["G"]), "L_25sep_basis_B0_40400_seed20260927": np.median(o6["G"]), "insight_v1_E6_ref_H8": None},
        {"quantity": "gift_p95", "L_28sep_B0_40736": np.percentile(oL["G"], 95), "L_25sep_basis_B0_40400_seed20260927": np.percentile(o6["G"], 95), "insight_v1_E6_ref_H8": None},
        {"quantity": "kept_p50", "L_28sep_B0_40736": np.median(oL["K"]), "L_25sep_basis_B0_40400_seed20260927": np.median(o6["K"]), "insight_v1_E6_ref_H8": None},
        {"quantity": "median_top_2031", "L_28sep_B0_40736": np.median(oL["U"]), "L_25sep_basis_B0_40400_seed20260927": np.median(o6["U"]), "insight_v1_E6_ref_H8": None},
        {"quantity": "P_top_reached", "L_28sep_B0_40736": (oL["B5"] >= oL["B3"]).mean(), "L_25sep_basis_B0_40400_seed20260927": (o6["B5"] >= o6["B3"]).mean(), "insight_v1_E6_ref_H8": None},
    ]
    pd.DataFrame(e6).to_csv(OUT / "reconcile_E6.csv", index=False)
    say("E6 reconcile (L, B0=40,400, seed 20260927): total p5/p50/p95 = "
        f"{np.percentile(o6['T'],5):,.0f} / {np.median(o6['T']):,.0f} / {np.percentile(o6['T'],95):,.0f} "
        "(insight_v1 H8: 182,000 / 207,000 / 250,000; H8 is a rounded 25 Sep figure)")

    # --- 6. figures ------------------------------------------------------------------------------------------------
    try:
        make_figures(paths)
    except Exception as exc:  # figures never block the numbers
        say(f"figure step failed: {exc!r}")

    # --- 7. headline + numbers_proposed ----------------------------------------------------------------------------
    sm = summary.set_index("model")
    head = {"model_set": HEADLINE_MODELS, "B0": B0, "F": F, "s": S, "N": N, "seed": bc.SEED}
    for tag in ALL_MODELS:
        r = sm.loc[tag]
        head[tag] = {"top2031_p50": r["U_p50"], "top2031_p5": r["U_p5"], "top2031_p95": r["U_p95"],
                     "gift2033_p50": r["G_p50"], "gift2033_p5": r["G_p5"], "gift2033_p95": r["G_p95"],
                     "kept_p50": r["K_p50"], "total_p50": r["T_p50"], "total_p5": r["T_p5"], "total_p95": r["T_p95"],
                     "P_top_reached": r["P_top_reached"], "P_upper_half": r["P_upper_half"],
                     "P_B3_below_B0": r["P_B3_below_B0"], "median_position": r["median_position_p"],
                     "realised_mean": r["realised_mean_log_return"], "realised_sd": r["realised_sd_log_return"]}
    hm = [head[t] for t in HEADLINE_MODELS]
    head["across_3_models"] = {
        "top2031_p50_range": [min(h["top2031_p50"] for h in hm), max(h["top2031_p50"] for h in hm)],
        "top2031_90pct_low_range": [min(h["top2031_p5"] for h in hm), max(h["top2031_p5"] for h in hm)],
        "top2031_90pct_high_range": [min(h["top2031_p95"] for h in hm), max(h["top2031_p95"] for h in hm)],
        "P_top_reached_range": [min(h["P_top_reached"] for h in hm), max(h["P_top_reached"] for h in hm)],
        "P_upper_half_range": [min(h["P_upper_half"] for h in hm), max(h["P_upper_half"] for h in hm)],
        "gift2033_p50_range": [min(h["gift2033_p50"] for h in hm), max(h["gift2033_p50"] for h in hm)],
    }
    head["bayes_posterior"] = {r["param"]: {"mean": r["mean"], "sd": r["sd"]} for r in bp}
    head["L_analytic_check"] = {"median_top_analytic": med_top_L, "P_top_analytic": p_top_L}
    head["elapsed_s"] = time.time() - t0
    head["log"] = log
    bc.write_json(head, OUT / "headline_M3.json")
    write_numbers_proposed(head)
    say(f"M3 done in {time.time()-t0:.0f}s -> {OUT}")


def write_numbers_proposed(head: dict) -> None:
    a = head["across_3_models"]
    lines = [
        "# numbers_proposed_blind.yaml: BLIND M3 rebuild figures in the rab/numbers.yaml schema (for WS0/WS1 review; WS2 does",
        "# not write numbers.yaml). All MODEL, seed 20260930, 200,000 paths per model, B0 = laura.stock_fund_2028_usd.strips.",
        "numbers:",
    ]
    def entry(key, value, unit, quote, note):
        lines.extend([f"  {key}:", f"    value: {value}", f"    unit: {unit}", f"    quote_as: {quote}", "    scale: laura_plan",
                      "    status: MODEL (blind rebuild)", "    curve_date: '2026-09-28'", "    valuation_date: '2031-01-01'",
                      "    method: rab/verification/blind/blind_m3.py (M3_SPEC.md)", f"    note: {note}"])
    entry("branch.range2031.bottom", 150000, "USD", "$150,000 (the owned floor)", "certain by construction if the four M3_SPEC s5 conditions hold")
    lo_k, hi_k = round(a['top2031_p50_range'][0] / 1000), round(a['top2031_p50_range'][1] / 1000)
    q_top = f"about ${lo_k},000 in every model" if lo_k == hi_k else f"about ${lo_k}k-{hi_k}k"
    entry("branch.range2031.top_median_3models", f"[{a['top2031_p50_range'][0]:.0f}, {a['top2031_p50_range'][1]:.0f}]", "USD (min, max over T, BOOT, BAYES)",
          q_top, "median of F + half the 2031 fund")
    entry("branch.range2031.top_90pct_3models", f"[{a['top2031_90pct_low_range'][0]:.0f}, {a['top2031_90pct_high_range'][1]:.0f}]", "USD (widest 5th-95th over the 3 models)",
          f"about ${round(a['top2031_90pct_low_range'][0]/5000)*5}k to ${round(a['top2031_90pct_high_range'][1]/5000)*5}k", "as seen today")
    entry("branch.gift2033.P_top_reached_3models", f"[{a['P_top_reached_range'][0]:.4f}, {a['P_top_reached_range'][1]:.4f}]", "probability",
          f"about {round(100*a['P_top_reached_range'][0])}-{round(100*a['P_top_reached_range'][1])}% the gift is at the top", "P(B5 >= B3)")
    entry("branch.gift2033.P_upper_half_3models", f"[{a['P_upper_half_range'][0]:.4f}, {a['P_upper_half_range'][1]:.4f}]", "probability",
          f"about {round(100*a['P_upper_half_range'][0])}-{round(100*a['P_upper_half_range'][1])}% in the upper half", "P(B5/B3 >= 0.5)")
    (OUT / "numbers_proposed_blind.yaml").write_text("\n".join(lines) + "\n")


def make_figures(paths: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    okabe = {"L": "#999999", "T": "#E69F00", "BOOT": "#0072B2", "BAYES": "#009E73"}
    models = ["L", "T", "BOOT", "BAYES"]
    outs = {m: bc.outcomes(paths[m]) for m in models}

    fig, ax = plt.subplots(figsize=(8, 4.5))
    for m in models:
        u = outs[m]["U"] / 1000
        ax.hist(u, bins=np.linspace(140, 260, 121), density=True, histtype="step", lw=1.8, color=okabe[m])
    ymax = ax.get_ylim()[1]
    for i, m in enumerate(models):
        u = outs[m]["U"] / 1000
        ax.text(212, ymax * (0.92 - 0.09 * i), f"{m}: median \\${np.median(u):.0f}k, 90% \\${np.percentile(u,5):.0f}k-{np.percentile(u,95):.0f}k",
                color=okabe[m], fontsize=9, ha="left")
    ax.axvline(150, color="k", lw=1, ls="--")
    ax.text(150.5, ax.get_ylim()[1] * 0.5, "bottom = floor \\$150k", rotation=90, va="center", fontsize=8)
    ax.set_xlabel("Top of the range Laura announces in Jan 2031 (\\$ thousand)")
    ax.set_ylabel("density")
    ax.set_title("2031 range top = floor + half the stock fund, four return models (blind rebuild)")
    ax.set_xlim(140, 260)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M3_top2031.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    for m in models:
        g = outs[m]["G"] / 1000
        ax.hist(g, bins=np.linspace(140, 260, 121), density=True, histtype="step", lw=1.8, color=okabe[m],
                label=f"{m}: median \\${np.median(g):.0f}k, at top {100*(outs[m]['B5']>=outs[m]['B3']).mean():.0f}%")
    ax.set_xlabel("Gift in Jan 2033 (\\$ thousand); in about 3 paths in 4 the gift equals the announced top")
    ax.set_ylabel("density")
    ax.set_title("2033 gift = floor + half min(fund 2033, fund 2031): the cap in action (blind rebuild)")
    ax.legend(frameon=False, fontsize=9)
    ax.set_xlim(140, 260)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M3_gift2033.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 3.6))
    cats = []
    for m in models:
        o = outs[m]
        at_top = (o["B5"] >= o["B3"]).mean()
        upper = ((o["B5"] / o["B3"] >= 0.5) & (o["B5"] < o["B3"])).mean()
        lower = (o["B5"] / o["B3"] < 0.5).mean()
        cats.append((m, at_top, upper, lower))
    y = np.arange(len(models))
    left = np.zeros(len(models))
    for k, (lab, col) in enumerate([("at the top", "#0072B2"), ("upper half", "#56B4E9"), ("lower half", "#D55E00")]):
        vals = np.array([c[k + 1] for c in cats])
        ax.barh(y, vals, left=left, color=col, label=lab)
        for i, v in enumerate(vals):
            if v > 0.04:
                ax.text(left[i] + v / 2, i, f"{100*v:.0f}%", ha="center", va="center", color="white", fontsize=9)
        left += vals
    ax.set_yticks(y)
    ax.set_yticklabels(models)
    ax.set_xlim(0, 1)
    ax.set_xlabel("share of paths")
    ax.set_title("Where in the 2031 range the 2033 gift lands (blind rebuild)")
    ax.legend(frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, -0.45), fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M3_where_in_range.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
