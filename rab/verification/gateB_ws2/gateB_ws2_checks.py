"""Gate B, WS2 (M3 branch, M4 cap share, M8 sensitivity): primary build vs blind rebuild, key by key.

WS2 Gate B reconciler, RAB Kit, 2026-09-30 (Sydney). AI-generated verification (Claude Code) for Team Caplet; no
deliverable text. Nothing here changes the strategy or rab/numbers.yaml.

What it does
  1. Every one of the blind build's 307 headline keys (rab/verification/blind_ws2/out/blind_headlines.json) is matched to
     the primary build's value in rab/results/, with the spec tolerance -> gateB_ws2_table.csv / .md.
  2. The primary build's own 29 headline keys (its WS2 summary) against the blind value.
  3. Cross-evaluation: each build's rule code run on the OTHER build's return paths and floor draws. If the rule code
     agrees exactly, every gap between the builds is sampling noise in the paths.
  4. Distribution tests (Kolmogorov-Smirnov) of the two builds' return paths, model by model.
  5. Noise band: the primary code with 10 other seeds (2,000,000 more paths per model); pooled s*.
  6. Named discrepancies: narrower-range reading, announced-basis top (M4 A2), P(gift = face-based top), the memo's
     "gift below $150k" count, Pareto grid counts, Sobol luck-share definitions.
  7. insight_v1 (rab/inventory.md H8, H11, H12, H13, H15, E4's s = 3/4 and 1) on insight_v1's own random draws and
     on the 28 Sep basis.

Run from the worktree root (about 3 minutes, no network, seed 20260930):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws2/gateB_ws2_checks.py
Needs the blind paths in rab/verification/blind_ws2/out/paths/ (regenerate with rab/verification/blind_ws2/run_all.sh).
"""
import json
import math
import os
import re
import sys

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PRIM = os.path.join(ROOT, "rab", "results")
BLIND = os.path.join(ROOT, "rab", "verification", "blind_ws2")
BLO = os.path.join(BLIND, "out")
sys.path.insert(0, os.path.join(ROOT, "rab", "models"))
sys.path.insert(0, BLIND)

import ws2_common as C  # noqa: E402  primary
import m3_branch as M3  # noqa: E402  primary
import m4_cap as M4  # noqa: E402  primary
import blind_common as bc  # noqa: E402  blind
import blind_m4 as bm4  # noqa: E402  blind

N = C.N_PATHS
F = 150_000.0
RES = {}
LOG = []


def say(s=""):
    print(s, flush=True)
    LOG.append(s)


# ====================================================================== 1. key-by-key table (blind keys)
XMAP = {"X1": "mu_c", "X2": "sd_log", "X3": "inv_nu", "X4": "d", "X5": "e", "X6": "fee", "X7": "phi"}
INV_X = {v: k for k, v in XMAP.items()}
M3COL = {"top2031": "U", "gift2033": "G", "kept": "K", "total": "T"}
ADCOL = {"E_G": "EG", "G_p5": "G_p5", "G_p50": "G_p50", "G_p95": "G_p95", "E_K": "EK", "K_p5": "K_p5",
         "K_p50": "K_p50", "E_width": "E_width", "U_p50": "U_p50", "E_U_minus_G": "E_short_top",
         "P_K_ge_thr_G": "P_flex", "P_G_lt_L": "P_D", "P_top_fund": "P_top_fund", "P_top_gift_eq_U": "P_top",
         "P_G_below_middle": "P_below_middle"}


def load_primary():
    P = {"s3": pd.read_csv(os.path.join(PRIM, "M3", "summary.csv")).set_index("model"),
         "post": pd.read_csv(os.path.join(PRIM, "M3", "bayes_posterior.csv")).set_index("param"),
         "fd": pd.read_csv(os.path.join(PRIM, "M4", "floor_delivery.csv")),
         "dec": pd.read_csv(os.path.join(PRIM, "M4", "decision.csv")).set_index("model"),
         "sp": pd.read_csv(os.path.join(PRIM, "M4", "s_profile.csv")),
         "rs": pd.read_csv(os.path.join(PRIM, "M4", "rule_sensitivity.csv")),
         "tor": pd.read_csv(os.path.join(PRIM, "M8", "tornado.csv")).set_index("input"),
         "sB": pd.read_csv(os.path.join(PRIM, "M8", "sobol_B.csv")),
         "ms": pd.read_csv(os.path.join(PRIM, "M8", "must_state.csv")),
         "fr": pd.read_csv(os.path.join(PRIM, "M8", "floor_reading.csv")).set_index("d_bp"),
         "ir": pd.read_csv(os.path.join(PRIM, "M8", "input_ranges.csv")).set_index("input"),
         "m4log": open(os.path.join(PRIM, "M4", "run_log.txt")).read()}
    P["sA"] = {y: pd.read_csv(os.path.join(PRIM, "M8", f"sobol_A_{y}.csv")).set_index("input")
               for y in ("top2031", "gift2033")}
    P["ad"] = P["sp"][np.isclose(P["sp"].s, 0.5)].set_index("model")
    P["pareto"] = {m: pd.read_csv(os.path.join(PRIM, "M4", f"pareto_{m}.csv")) for m in ("T", "BOOT", "BAYES")}
    return P


def primary_value(key, P, inp):
    p = key.split(".")
    if p[0] == "M3":
        m = p[1]
        if p[2] == "posterior_mean":
            return float(P["post"].loc[p[3], "mean"])
        if p[2] == "analytic_median_top":
            return F + 0.5 * inp["B0"] * math.exp(3 * C.MU_L)
        if p[2] == "analytic_P_top":
            return float(stats.norm.cdf(math.sqrt(2) * C.MU_L / C.SIG_L))
        met = p[2]
        if met.startswith(("P_",)):
            return float(P["s3"].loc[m, met])
        base, q = met.rsplit("_", 1)
        return float(P["s3"].loc[m, f"{M3COL[base]}_{q}"])
    if p[0] == "M4":
        fd, dec = P["fd"], P["dec"]
        if p[1] == "h_star":
            return float(fd.h_star.iloc[0])
        if p[1] == "A_announced_floor":
            return float(fd.announced_floor.iloc[0])
        if p[1] == "s_star":
            return float(dec.loc[p[2], "s_star"])
        if p[1] == "s_star_robust":
            return float(dec.loc["ROBUST", "s_star"])
        if p[1] == "PR7_recommendation":
            return float(dec.recommendation.iloc[0])
        if p[1] == "phi":
            q = ".".join(p[2:])
            col = {"p0.5": "phi_p0_5", "p1": "phi_p1", "p5": "phi_p5", "p50": "phi_p50", "p95": "phi_p95",
                   "max": "phi_max"}[q]
            return float(fd[col].iloc[0])
        if p[1] == "adopted_half":
            return float(P["ad"].loc[p[2], ADCOL[p[3]]])
        if p[1] == "rule_sensitivity":
            mm = re.match(r"thr([\d.]+)_conf([\d.]+)", ".".join(p[2:]))
            kap, conf = float(mm.group(1)), float(mm.group(2))
            r = P["rs"][(P["rs"].model.isin(["T", "BOOT", "BAYES"])) & np.isclose(P["rs"].kappa, kap)
                        & np.isclose(P["rs"].confidence, conf)]
            return None if r.s_star.isna().any() else float(r.s_star.min())
        if p[1] == "pareto":
            m, what = p[2], p[3]
            df = P["pareto"][m]
            if what == "n_front":
                return int(len(df))
            if what == "s_at_max_E_G_feasible":
                return float(df.loc[df.E_gift.idxmax(), "s"])
            if what == "front_points_dominated_by_grid":
                return int(re.search(rf"Pareto {m}\s*:.*dominated by a grid point: (\d+)", P["m4log"]).group(1))
    if p[0] == "M8":
        tor, fr, ir = P["tor"], P["fr"], P["ir"]
        if p[1] == "base":
            return {"V_A_0": float(fr.loc[0.0, "ladder_2027"]), "B0": float(fr.loc[0.0, "IPS_fund"]),
                    "top2031_median": float(tor.loc["fee", "top_p50_at_low"]),
                    "top2031_p5": float(tor.loc["fee", "top_p5_at_low"]),
                    "gift2033_median": float(tor.loc["fee", "gift_p50_at_low"])}[p[2]]
        if p[1] == "X4_d_bp_2":
            return [round(float(ir.loc["d", "low"]), 2), round(float(ir.loc["d", "high"]), 2)]
        if p[1] == "X5_e_pts_2":
            return [round(float(ir.loc["e", "low"]), 2), round(float(ir.loc["e", "high"]), 2)]
        if p[1] == "tornado":
            if p[2] == "rank":
                a = tor[tor.kind == "assumption"].sort_values("swing_top_p50", ascending=False)
                return [INV_X[i] for i in a.index]
            if p[2] == "BASE":
                b = float(tor.loc["fee", "top_p50_at_low"])
                return {"Y1_med_low": b, "Y1_med_high": b, "swing_Y1_med": 0.0}[p[3]]
            row = {"REF_s_lever": "s", "REF_return_model": "model"}.get(p[2], XMAP.get(p[2]))
            r = tor.loc[row]
            return float({"Y1_med_low": r.top_p50_at_low, "Y1_med_high": r.top_p50_at_high,
                          "swing_Y1_med": r.swing_top_p50}[p[3]])
        if p[1] == "sobolA":
            y = p[2]
            if p[3] == "luck_share_S1":
                d = P["sA"][y]
                return float(d[d.index.str.startswith("u")].S1.sum())
            nm = XMAP.get(p[4], p[4])
            return float(P["sA"][y].loc[nm, p[3]])
        if p[1] == "sobolB":
            out = p[2]
            r = P["sB"][(P["sB"].output == out) & (P["sB"].input == XMAP[p[4]])]
            return float(r[p[3]].iloc[0])
        if p[1] == "ips_must_state":
            ms = P["ms"]
            return {"top3": [INV_X[i] for i in ms.input], "p5_agrees": bool(ms.in_p5_top3.all()),
                    "tornado_agrees": bool(ms.in_tornado_top3.all())}[p[2]]
        if p[1] == "floor_reading":
            d = float(p[2][1:])
            col = {"V_A": "ladder_2027", "IPS_floor_F": "IPS_floor", "IPS_fund_B0": "IPS_fund",
                   "E6_floor_F": "E6_floor", "E6_fund_B0": "E6_fund"}[p[3]]
            return float(fr.loc[d, col])
    raise KeyError(key)


def tolerance(tol, unit, key):
    """Returns (kind, value): rel / abs / exact / list / report."""
    t = tol.strip()
    if t in ("report",) or unit == "bool":
        return ("exact", 0) if unit == "bool" else ("report", None)
    if t in ("identical", "data (exact)", "top-3 identical"):
        return ("exact", 0)
    if t == "exact":
        return ("abs", 0.005)
    if t == "MC error":                      # both builds evaluate the same closed form; blind JSON rounds to 4 dp
        return ("abs", 0.005 if unit == "USD" else 5e-5)
    if t.startswith("0.05"):
        return ("abs", 0.05)
    if t == "0.02":
        return ("abs", 0.02)
    if t == "2 points":
        return ("abs", 0.02)
    if t.startswith("10%"):
        return ("rel", 0.10)
    if t == "1% of medians":
        return ("abs", 0.01 * 174_950)
    if t.endswith("%"):
        return ("rel", float(t[:-1]) / 100)
    raise ValueError((key, tol))


def compare(key, pv, bv, tol, unit):
    kind, tv = tolerance(tol, unit, key)
    if isinstance(bv, list) or isinstance(pv, list):
        if key.endswith("rank"):
            ok = pv[:3] == bv[:3]
            return ("MATCH" if pv == bv else ("WITHIN TOL" if ok else "OUTSIDE TOL")), "", "top-3 identical"
        return ("MATCH" if pv == bv else "OUTSIDE TOL"), "", "identical"
    if isinstance(bv, bool) or isinstance(pv, bool):
        return ("MATCH" if pv == bv else "OUTSIDE TOL"), "", "identical"
    if bv is None or pv is None:
        return ("MATCH" if pv is None and bv is None else "OUTSIDE TOL"), "", "both 'none'"
    d = float(pv) - float(bv)
    if kind == "report":
        return ("REPORT" if d != 0 else "MATCH"), d, "report only"
    if kind == "exact":
        return ("MATCH" if abs(d) < 1e-12 else "OUTSIDE TOL"), d, "identical"
    if kind == "abs":
        ok = abs(d) <= tv + 1e-12
        exact = abs(d) <= (0.005 if unit == "USD" else 1e-9)
        return ("MATCH" if exact else ("WITHIN TOL" if ok else "OUTSIDE TOL")), d, f"+-{tv:g}"
    rel = d / float(bv) if bv else (0.0 if d == 0 else math.inf)
    ok = abs(rel) <= tv + 1e-12
    exact = abs(d) <= (0.005 if unit == "USD" else 1e-9)
    return ("MATCH" if exact else ("WITHIN TOL" if ok else "OUTSIDE TOL")), d, f"+-{tv:.0%}"


def fmt(v, unit):
    if v is None:
        return "none"
    if isinstance(v, (list, bool, str)):
        return str(v)
    if unit == "USD":
        return f"{v:,.2f}"
    if unit in ("points", "keys"):
        return f"{v:g}"
    return f"{v:.4f}"


def key_table(P, inp):
    bh = json.load(open(os.path.join(BLO, "blind_headlines.json")))
    rows = []
    for key, rec in bh.items():
        bv, unit, tol = rec["value"], rec.get("unit", ""), rec.get("tolerance", "")
        pv = primary_value(key, P, inp)
        verdict, d, tol_used = compare(key, pv, bv, tol, unit)
        z = ""
        if unit == "probability" and isinstance(pv, float) and isinstance(bv, float) and key.startswith(("M3", "M4")):
            se = math.sqrt(max(pv * (1 - pv), 1e-12) / N + max(bv * (1 - bv), 1e-12) / N)
            z = round(float(pv - bv) / se, 2) if se > 1e-6 else 0.0
        rel = (float(d) / float(bv) if isinstance(d, float) and isinstance(bv, (int, float)) and not isinstance(bv, bool)
               and bv not in (0, None) else "")
        rows.append({"key": key, "unit": unit, "primary": pv, "blind": bv, "diff": d, "rel_diff": rel,
                     "tolerance": tol_used, "noise_z": z, "verdict": verdict})
    return pd.DataFrame(rows)


# ====================================================================== 2. the primary build's own headline keys
def primary_headlines(P):
    """The 29 headline keys of the primary's WS2 summary, each against the blind value (published files only)."""
    bh = {k: v["value"] for k, v in json.load(open(os.path.join(BLO, "blind_headlines.json"))).items()}
    s3, ad, dec = P["s3"], P["ad"], P["dec"]
    bsum = pd.read_csv(os.path.join(BLO, "M3", "summary.csv")).set_index("model")
    bfd = pd.read_csv(os.path.join(BLO, "M4", "floor_delivery.csv")).set_index("quantity")["value"]
    bnr = pd.read_csv(os.path.join(BLO, "M4", "narrower_range.csv"))
    pnr = pd.read_csv(os.path.join(PRIM, "M4", "narrower_range.csv"))
    rec6 = pd.read_csv(os.path.join(PRIM, "M3", "reconcile_E6.csv")).set_index("measure")
    brec6 = pd.read_csv(os.path.join(BLO, "M3", "reconcile_E6.csv")).set_index("quantity")
    D = ["T", "BOOT", "BAYES"]
    rs = lambda kap, conf: primary_value(f"M4.rule_sensitivity.thr{kap}_conf{conf}", P, None)
    boot06 = pnr[(pnr.model == "BOOT") & np.isclose(pnr.l, 0.6)].iloc[0]
    e6p = max(abs(rec6.loc[m, "L_E6_basis_k"] - rec6.loc[m, "E6_25sep_k"]) * 1000 for m in rec6.index
              if m != "P_top_reached")
    e6b = max(abs(brec6.loc[m, "L_25sep_basis_B0_40400_seed20260927"] - brec6.loc[m, "insight_v1_E6_ref_H8"])
              for m in ("total_p5", "total_p50", "total_p95"))
    rows = [
        ("top2031_median_T", s3.loc["T", "U_p50"], bh["M3.T.top2031_p50"], "rel", 0.02),
        ("top2031_median_BOOT", s3.loc["BOOT", "U_p50"], bh["M3.BOOT.top2031_p50"], "rel", 0.02),
        ("top2031_median_BAYES", s3.loc["BAYES", "U_p50"], bh["M3.BAYES.top2031_p50"], "rel", 0.02),
        ("top2031_p5_min_across_models", min(s3.loc[m, "U_p5"] for m in D), min(bh[f"M3.{m}.top2031_p5"] for m in D),
         "rel", 0.02),
        ("top2031_p95_max_across_models", max(s3.loc[m, "U_p95"] for m in D),
         max(bh[f"M3.{m}.top2031_p95"] for m in D), "rel", 0.02),
        ("p_gift_reaches_top_T", s3.loc["T", "P_top_reached"], bh["M3.T.P_top_reached"], "abs", 0.02),
        ("p_gift_reaches_top_BOOT", s3.loc["BOOT", "P_top_reached"], bh["M3.BOOT.P_top_reached"], "abs", 0.02),
        ("p_gift_reaches_top_BAYES", s3.loc["BAYES", "P_top_reached"], bh["M3.BAYES.P_top_reached"], "abs", 0.02),
        ("p_gift_upper_half_min", min(s3.loc[m, "P_upper_half"] for m in D), min(bh[f"M3.{m}.P_upper_half"] for m in D),
         "abs", 0.02),
        ("p_gift_within_range (8 models, 1.6M paths)", float(s3.P_G_within_range.min()), float(bsum.P_G_ge_F.min()),
         "exact", 0),
        ("gift2033_median_BAYES", s3.loc["BAYES", "G_p50"], bh["M3.BAYES.gift2033_p50"], "rel", 0.02),
        ("gift2033_BAYES_p5", s3.loc["BAYES", "G_p5"], bh["M3.BAYES.gift2033_p5"], "rel", 0.02),
        ("gift2033_BAYES_p95", s3.loc["BAYES", "G_p95"], bh["M3.BAYES.gift2033_p95"], "rel", 0.02),
        ("p_fund_below_cost_2031 (max of 3)", max(s3.loc[m, "P_B3_below_B0"] for m in D),
         max(bh[f"M3.{m}.P_B3_below_B0"] for m in D), "abs", 0.02),
        ("p_fund_below_cost_2031 (min of 3)", min(s3.loc[m, "P_B3_below_B0"] for m in D),
         min(bh[f"M3.{m}.P_B3_below_B0"] for m in D), "abs", 0.02),
        ("E6_reconcile_max_abs_diff (USD)", e6p, e6b, "report", None),
        ("D6_robust_s_star", float(dec.loc["ROBUST", "s_star"]), bh["M4.s_star_robust"], "abs", 0.02),
        ("D6_recommendation_s", float(dec.recommendation.iloc[0]), bh["M4.PR7_recommendation"], "exact", 0),
        ("p_keep_10pct_of_gift_at_half_BAYES", ad.loc["BAYES", "P_flex"], bh["M4.adopted_half.BAYES.P_K_ge_thr_G"],
         "abs", 0.02),
        ("p_keep_10pct_at_half (max of 3)", max(ad.loc[m, "P_flex"] for m in D),
         max(bh[f"M4.adopted_half.{m}.P_K_ge_thr_G"] for m in D), "abs", 0.02),
        ("s_star_if_keep_5pct", rs(0.05, 0.95), bh["M4.rule_sensitivity.thr0.05_conf0.95"], "abs", 0.02),
        ("s_star_if_keep_15pct", rs(0.15, 0.95), bh["M4.rule_sensitivity.thr0.15_conf0.95"], "abs", 0.02),
        ("announced_floor", float(P["fd"].announced_floor.iloc[0]), bh["M4.A_announced_floor"], "exact", 0),
        ("floor_delivery_median (phi p50 x $150k)", float(P["fd"].phi_p50.iloc[0]) * F, float(bfd["phi_p50"]) * F,
         "rel", 0.02),
        ("floor_delivery_worst (phi min x $150k)", float(P["fd"].phi_min.iloc[0]) * F, float(bfd["phi_min"]) * F,
         "rel", 0.02),
        ("P(floor pays < $150k)", float(P["fd"].P_phi_below_1_minus_h.iloc[0]), float(bfd["P_phi_lt_1.000"]), "abs", 0.02),
        ("p_breach_low_end_160k_BOOT (blind at the same low end)", float(boot06.P_D),
         float(np.interp(boot06.low_end_p50, bnr.BOOT_low_end_p50, bnr.BOOT_P_G_lt_L)), "abs", 0.02),
        ("sobol_ST_jan2027_yields", primary_value("M8.sobolB.median_top2031.ST.X4", P, None),
         bh["M8.sobolB.median_top2031.ST.X4"], "abs", 0.05),
        ("sobol_ST_jan2028_5y_yield", primary_value("M8.sobolB.median_top2031.ST.X5", P, None),
         bh["M8.sobolB.median_top2031.ST.X5"], "abs", 0.05),
        ("sobol_ST_costs", primary_value("M8.sobolB.median_top2031.ST.X6", P, None),
         bh["M8.sobolB.median_top2031.ST.X6"], "abs", 0.05),
        ("sobol_ST_expected_return", primary_value("M8.sobolB.median_top2031.ST.X1", P, None),
         bh["M8.sobolB.median_top2031.ST.X1"], "abs", 0.05),
        ("tornado_swing_jan2027_yields", float(P["tor"].loc["d", "swing_top_p50"]), bh["M8.tornado.X4.swing_Y1_med"],
         "abs", 1749.5),
        ("tornado_swing_costs", float(P["tor"].loc["fee", "swing_top_p50"]), bh["M8.tornado.X6.swing_Y1_med"],
         "abs", 1749.5),
        ("tornado_swing_expected_return", float(P["tor"].loc["mu_c", "swing_top_p50"]), bh["M8.tornado.X1.swing_Y1_med"],
         "abs", 1749.5),
        ("floor_IPS_reading_minus50bp", float(P["fr"].loc[-50.0, "IPS_floor"]), bh["M8.floor_reading.d-50.IPS_floor_F"],
         "abs", 0.005),
        ("fund_IPS_reading_minus50bp", float(P["fr"].loc[-50.0, "IPS_fund"]), bh["M8.floor_reading.d-50.IPS_fund_B0"],
         "abs", 0.005),
    ]
    out = []
    for key, pv, bv, kind, tv in rows:
        pv, bv = float(pv), float(bv)
        d = pv - bv
        if kind == "report":
            v = "REPORT"
        elif kind == "exact":
            v = "MATCH" if abs(d) < 1e-12 else "OUTSIDE TOL"
        elif kind == "abs":
            v = "MATCH" if abs(d) <= (0.005 if abs(pv) > 10 else 5e-5) else ("WITHIN TOL" if abs(d) <= tv else
                                                                                "OUTSIDE TOL")
        else:
            v = "MATCH" if abs(d) <= 0.005 else ("WITHIN TOL" if abs(d / bv) <= tv else "OUTSIDE TOL")
        out.append({"key": key, "primary": pv, "blind": bv, "diff": d,
                    "tolerance": ("report" if kind == "report" else "identical" if kind == "exact" else
                                  f"+-{tv:.0%}" if kind == "rel" else f"+-{tv:g}"), "verdict": v})
    df = pd.DataFrame(out)
    df.to_csv(os.path.join(HERE, "gateB_ws2_primary_headlines.csv"), index=False)
    say(f"[2] primary's {len(df)} headline rows: {df.verdict.value_counts().to_dict()}")
    RES["primary_headlines"] = out
    return df


# ====================================================================== 3. cross-evaluation of the rule code
def summ_cols(o, B0):
    r = {}
    for k in ("U", "G", "K", "T"):
        for q in (5, 50, 95):
            r[f"{k}_p{q}"] = float(np.percentile(o[k], q))
    r["P_top_reached"] = float(np.mean(o["B5"] >= o["B3"]))
    r["P_upper_half"] = float(np.mean(o["B5"] / o["B3"] >= 0.5))
    r["P_B3_below_B0"] = float(np.mean(o["B3"] < B0))
    return r


def primary_sstar(o, phi, A):
    best = None
    for s in M4.S_GRID:
        q = M4.measures(o, phi, F, s, low=A)
        if q["P_D"] <= M4.PD_MAX and q["P_flex"] >= M4.CONF:
            best = float(s)
    return best


def cross_eval(inp):
    say("\n[3] Cross-evaluation: each build's rule code on the other build's paths and floor draws")
    models = ["L", "T", "BOOT", "BAYES", "BOOT-raw", "BOOT-b1", "BOOT-b60", "BAYES-hist"]
    xb = {m: np.load(os.path.join(BLO, "paths", f"{m}.npy")) for m in models}
    xp = {m: M3.paths(m) for m in models}
    bsum = pd.read_csv(os.path.join(BLO, "M3", "summary.csv")).set_index("model")
    psum = pd.read_csv(os.path.join(PRIM, "M3", "summary.csv")).set_index("model")
    out = {"M3": {}, "M4": {}}
    worst_a, worst_b = 0.0, 0.0
    for m in models:
        rp, _ = M3.summarise(m, xb[m], inp)                       # primary code, blind paths
        ob = bc.outcomes(xp[m])                                    # blind code, primary paths
        rb = summ_cols(ob, bc.B0)
        da = max(abs(rp[c] - bsum.loc[m, c]) for c in rb)          # vs the blind's own published summary
        db = max(abs(rb[c] - psum.loc[m, c]) for c in rb)          # vs the primary's own published summary
        worst_a, worst_b = max(worst_a, da), max(worst_b, db)
        out["M3"][m] = {"primary_code_on_blind_paths_max_abs_diff": da, "blind_code_on_primary_paths_max_abs_diff": db}
    say(f"  M3 (8 models x 15 figures): primary code on blind paths reproduces the blind summary to "
        f"{worst_a:.2e}; blind code on primary paths reproduces the primary summary to {worst_b:.2e}")
    out["M3"]["worst"] = [worst_a, worst_b]

    # floor draws: same empirical list?
    lp_, lb_ = M4.dgs1_changes(), bm4.dgs1_changes(913)
    same_list = bool(len(lp_) == len(lb_) and np.allclose(np.sort(lp_), np.sort(lb_), atol=0, rtol=0))
    phi_p, _, _ = M4.phi_draws(inp["y5"])
    phi_b, _, _ = bm4.floor_delivery(bc.rng_for("PHI"), N, lb_)
    A = 145_000.0
    say(f"  floor: empirical 30-month changes identical in both builds: {same_list} (n = {len(lp_)}); "
        f"P(phi < 1) primary {np.mean(phi_p < 1):.4f}, blind {np.mean(phi_b < 1):.4f}")
    out["floor"] = {"same_delta_list": same_list, "n": int(len(lp_)), "P_phi_lt_1_primary": float(np.mean(phi_p < 1)),
                    "P_phi_lt_1_blind": float(np.mean(phi_b < 1))}
    bsp = pd.read_csv(os.path.join(BLO, "M4", "s_profile.csv"))
    psp = pd.read_csv(os.path.join(PRIM, "M4", "s_profile.csv"))
    bdec = pd.read_csv(os.path.join(BLO, "M4", "decision.csv")).set_index("model")
    pdec = pd.read_csv(os.path.join(PRIM, "M4", "decision.csv")).set_index("model")
    w1, w2, sst = 0.0, 0.0, {}
    for m in ["T", "BOOT", "BAYES", "L"]:
        ob = bc.outcomes(xb[m])
        op = C.rule(xp[m], inp["B0"], F)
        # primary measures on blind paths + blind phi, vs the blind's s_profile at s = 1/2
        qa = M4.measures(ob, phi_b, F, 0.5, low=A)
        rb = bsp[(bsp.model == m) & np.isclose(bsp.s, 0.5)].iloc[0]
        da = max(abs(qa[ADCOL[k]] - rb[k]) / (1 if k.startswith("P") else max(1.0, abs(rb[k]))) for k in ADCOL)
        # blind measures on primary paths + primary phi, vs the primary's s_profile at s = 1/2
        qb = bm4.measures(op["B3"], op["B5"], phi_p, 0.5, A=A)
        rp = psp[(psp.model == m) & np.isclose(psp.s, 0.5)].iloc[0]
        db = max(abs(qb[k] - rp[ADCOL[k]]) / (1 if k.startswith("P") else max(1.0, abs(rp[ADCOL[k]]))) for k in ADCOL
                 if k != "P_top_gift_eq_U")      # tolerance 1e-9 vs 1e-6 in the two codes; checked separately below
        s_a = primary_sstar(ob, phi_b, A)
        s_b = bm4.s_star(op["B3"], op["B5"], phi_p, A)
        sst[m] = {"primary_code_blind_paths": s_a, "blind_published": float(bdec.loc[m, "s_star_model"]),
                  "blind_code_primary_paths": s_b, "primary_published": float(pdec.loc[m, "s_star"])}
        w1, w2 = max(w1, da), max(w2, db)
        eqU_tol = abs(np.mean(np.minimum(phi_p * F + 0.5 * np.minimum(op["B5"], op["B3"]), op["U"]) >= op["U"] - 1e-6)
                      - np.mean(np.minimum(phi_p * F + 0.5 * np.minimum(op["B5"], op["B3"]), op["U"]) >= op["U"] - 1e-9))
        sst[m]["P_top_eq_U_tolerance_effect"] = float(eqU_tol)
    say(f"  M4 at s = 1/2 (15 measures x 4 models): primary code on blind paths reproduces the blind s_profile to "
        f"{w1:.2e} (relative); blind code on primary paths reproduces the primary s_profile to {w2:.2e}")
    for m, v in sst.items():
        say(f"  s*_{m}: primary code on blind paths {v['primary_code_blind_paths']:.2f} (blind published "
            f"{v['blind_published']:.2f}); blind code on primary paths {v['blind_code_primary_paths']:.2f} (primary "
            f"published {v['primary_published']:.2f})")
    out["M4"] = {"max_rel_diff_primary_code_on_blind": w1, "max_rel_diff_blind_code_on_primary": w2, "s_star": sst}
    RES["cross_eval"] = out
    return xp, xb, phi_p, phi_b


# ====================================================================== 4. distribution tests of the paths
def dist_tests(xp, xb):
    say("\n[4] Same model, different random numbers? KS tests on each path's 3-year and 2-year log growth")
    out = {}
    for m in xp:
        a3, b3 = xp[m][:, :3].sum(1), xb[m][:, :3].sum(1)
        a2, b2 = xp[m][:, 3:].sum(1), xb[m][:, 3:].sum(1)
        k3, k2 = stats.ks_2samp(a3, b3), stats.ks_2samp(a2, b2)
        out[m] = {"KS_3yr_D": float(k3.statistic), "KS_3yr_p": float(k3.pvalue), "KS_2yr_D": float(k2.statistic),
                  "KS_2yr_p": float(k2.pvalue), "mean_x_primary": float(xp[m].mean()), "mean_x_blind": float(xb[m].mean()),
                  "sd_x_primary": float(xp[m].std()), "sd_x_blind": float(xb[m].std())}
        say(f"  {m:10s} KS 3-year D {k3.statistic:.4f} (p {k3.pvalue:.2f}), 2-year D {k2.statistic:.4f} "
            f"(p {k2.pvalue:.2f}); annual log mean {xp[m].mean():.4f} / {xb[m].mean():.4f}, sd {xp[m].std():.4f} / "
            f"{xb[m].std():.4f}")
    # any KS p < 0.05: is it chance? primary code with 3 more seeds, against the blind and against itself
    seed0 = C.SEED
    for m in [m for m, v in out.items() if min(v["KS_3yr_p"], v["KS_2yr_p"]) < 0.05]:
        reps = []
        for j in (1, 2, 3):
            C.SEED = seed0 + j
            x2 = M3.paths(m)
            reps.append({"seed": C.SEED,
                         "p_vs_blind_3yr": float(stats.ks_2samp(x2[:, :3].sum(1), xb[m][:, :3].sum(1)).pvalue),
                         "p_vs_blind_2yr": float(stats.ks_2samp(x2[:, 3:].sum(1), xb[m][:, 3:].sum(1)).pvalue),
                         "p_vs_primary_seed0_2yr": float(stats.ks_2samp(x2[:, 3:].sum(1), xp[m][:, 3:].sum(1)).pvalue)})
        C.SEED = seed0
        out[m]["reseeded"] = reps
        say(f"  {m}: re-seeded primary vs blind / vs its own seed: " + "; ".join(
            f"p {r['p_vs_blind_3yr']:.2f}/{r['p_vs_blind_2yr']:.2f} vs {r['p_vs_primary_seed0_2yr']:.2f}" for r in reps))
    pp = np.load(os.path.join(PRIM, "M3", "bayes_posterior_draws.npz"))
    bp = pd.read_csv(os.path.join(BLO, "M3", "bayes_posterior_draws.csv"))
    out["posterior_m_h"] = {"primary_mean": float(pp["m_h"].mean()), "blind_mean": float(bp["m_h"].mean()),
                            "mcse_each": float(pp["m_h"].std() / math.sqrt(2600))}
    say(f"  BAYES posterior centre m_h: primary {pp['m_h'].mean():.4f}, blind {bp['m_h'].mean():.4f} (MCMC s.e. about "
        f"{pp['m_h'].std() / math.sqrt(2600):.4f} each); BAYES-hist uses it as the forward centre, BAYES does not")
    RES["dist_tests"] = out


# ====================================================================== 5. noise band (primary code, 10 more seeds)
def noise_band(inp, n_seeds=10):
    say(f"\n[5] Noise band: primary code with {n_seeds} other seeds x 200,000 paths per model (BAYES posterior fixed)")
    seed0 = C.SEED
    A = 145_000.0
    S = M4.S_GRID
    models = ["L", "T", "BOOT", "BAYES"]
    acc = {m: {"flex": np.zeros(len(S)), "pd": np.zeros(len(S)), "n": 0} for m in models}
    rows = []
    for j in range(1, n_seeds + 1):
        C.SEED = seed0 + j
        phi, _, _ = M4.phi_draws(inp["y5"])
        for m in models:
            o = C.rule(M3.paths(m), inp["B0"], F)
            flex = np.empty(len(S))
            pdd = np.empty(len(S))
            m5 = np.minimum(o["B5"], o["B3"])
            for i, s in enumerate(S):
                G = np.minimum(phi * F + s * m5, F + s * o["B3"])
                K = phi * F + o["B5"] - G
                flex[i] = np.mean(K >= 0.10 * G)
                pdd[i] = np.mean(G < A)
            ok = (flex >= 0.95) & (pdd <= 0.005)
            sstar = float(S[ok].max()) if ok.any() else None
            acc[m]["flex"] += flex * N
            acc[m]["pd"] += pdd * N
            acc[m]["n"] += N
            i5 = int(np.where(np.isclose(S, 0.5))[0][0])
            G5 = np.minimum(phi * F + 0.5 * m5, o["U"])
            rows.append({"seed": C.SEED, "model": m, "U_p5": np.percentile(o["U"], 5), "U_p50": np.median(o["U"]),
                         "U_p95": np.percentile(o["U"], 95), "G_p50": np.median(o["G"]),
                         "P_top_fund": np.mean(o["B5"] >= o["B3"]), "P_upper_half": np.mean(o["B5"] / o["B3"] >= 0.5),
                         "P_flex_half": flex[i5], "P_top_eq_U_half": np.mean(G5 >= o["U"] - 1e-6), "s_star": sstar,
                         "P_phi_lt_1": np.mean(phi < 1)})
    C.SEED = seed0
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(HERE, "noise_band.csv"), index=False)
    band = {}
    for m in models:
        z = df[df.model == m]
        fl, pdd = acc[m]["flex"] / acc[m]["n"], acc[m]["pd"] / acc[m]["n"]
        ok = (fl >= 0.95) & (pdd <= 0.005)
        pooled = float(S[ok].max()) if ok.any() else None
        band[m] = {c: [float(z[c].min()), float(z[c].max())] for c in z.columns if c not in ("seed", "model")}
        band[m]["s_star_values"] = sorted(set(float(v) for v in z.s_star))
        band[m]["s_star_pooled_2M"] = pooled
        band[m]["P_flex_half_pooled_2M"] = float(fl[int(np.where(np.isclose(S, 0.5))[0][0])])
        say(f"  {m:5s} s* over seeds {band[m]['s_star_values']} (pooled 2,000,000 paths: {pooled}); median top "
            f"${band[m]['U_p50'][0]:,.0f}-${band[m]['U_p50'][1]:,.0f}; p5 top ${band[m]['U_p5'][0]:,.0f}-"
            f"${band[m]['U_p5'][1]:,.0f}; P(top) {band[m]['P_top_fund'][0]:.4f}-{band[m]['P_top_fund'][1]:.4f}; "
            f"P(keep >= 10%) at 1/2 {band[m]['P_flex_half'][0]:.4f}-{band[m]['P_flex_half'][1]:.4f} "
            f"(pooled {band[m]['P_flex_half_pooled_2M']:.4f}); P(gift = face top) {band[m]['P_top_eq_U_half'][0]:.4f}-"
            f"{band[m]['P_top_eq_U_half'][1]:.4f}")
    rob = [min(v) for v in zip(*[[r for r in df[df.model == m].s_star] for m in ("T", "BOOT", "BAYES")])]
    band["robust_s_star_per_seed"] = rob
    say(f"  robust s* per seed (min over T, BOOT, BAYES): {rob} -> PR-7 keeps 1/2 in every seed: "
        f"{all(0.40 <= r <= 0.60 for r in rob)}")
    RES["noise_band"] = band


# ====================================================================== 6. named discrepancies
def exact_phi(inp):
    """phi on the full empirical list (each of the 8,565 changes weighted equally): no sampling noise."""
    ch = M4.dgs1_changes()
    y5 = inp["y5"]
    r = np.maximum(0.0, y5 + ch / 100)
    coup = sum((1 + r) ** (5 - k) for k in range(1, 6))
    return np.sort((1 - M4.FEE_F) ** 5 * (1 + y5 * coup) / (1 + y5) ** 5)


def discrepancies(inp, xp, xb, phi_p, phi_b):
    say("\n[6] Named discrepancies")
    A, h = 145_000.0, 0.025
    out = {}
    builds = {"primary": (xp, phi_p), "blind": (xb, phi_b)}
    ph_exact = exact_phi(inp)
    out["phi_exact"] = {"P_phi_lt_1": float(np.mean(ph_exact < 1)), "p50": float(np.median(ph_exact)),
                        "min": float(ph_exact.min()), "max": float(ph_exact.max()),
                        "p95": float(np.percentile(ph_exact, 95)), "P_phi_lt_0.98": float(np.mean(ph_exact < 0.98))}
    say(f"  phi on the full empirical list (no sampling): P(phi < 1) {out['phi_exact']['P_phi_lt_1']:.4f}; median "
        f"{out['phi_exact']['p50']:.4f} (${out['phi_exact']['p50'] * F:,.0f}); min ${out['phi_exact']['min'] * F:,.0f}; "
        f"p95 ${out['phi_exact']['p95'] * F:,.0f}; max ${out['phi_exact']['max'] * F:,.0f}")

    # 6a narrower range: two readings of the low end, on both builds' paths
    lg = np.round(np.arange(0, 0.901, 0.05), 2)
    nr = {}
    for bname, (xx, ph) in builds.items():
        for m in ("T", "BOOT", "BAYES"):
            o = C.rule(xx[m], inp["B0"], F)
            G = np.minimum(ph * F + 0.5 * np.minimum(o["B5"], o["B3"]), o["U"])
            for reading, base in (("A_based", A), ("spec_F(1-h*)", F * (1 - h))):
                lows, pds = [], []
                for l in lg:
                    L = base + l * 0.5 * o["B3"]
                    lows.append(np.median(L))
                    pds.append(np.mean(G < L))
                lows, pds = np.array(lows), np.array(pds)
                nr[f"{bname}|{m}|{reading}"] = {f"P_D_at_{int(t / 1000)}k": float(np.interp(t, lows, pds))
                                                for t in (155_000, 160_000, 165_000)}
    out["narrower_range"] = nr
    for m in ("T", "BOOT", "BAYES"):
        say(f"  narrower range {m:5s} P(gift < low end) at a typical low end of $155k / $160k / $165k: " + "; ".join(
            f"{b} {r.split('_')[0]} " + " / ".join(f"{v:.2%}" for v in nr[f'{b}|{m}|{r}'].values())
            for b in builds for r in ("A_based", "spec_F(1-h*)")))

    # 6b announced-basis top (M4 A2), on both builds
    a2 = {}
    for bname, (xx, ph) in builds.items():
        for m in ("L", "T", "BOOT", "BAYES"):
            o = C.rule(xx[m], inp["B0"], F)
            m5 = np.minimum(o["B5"], o["B3"])
            G = np.minimum(ph * F + 0.5 * m5, o["U"])
            UA = A + 0.5 * o["B3"]
            GA = np.minimum(ph * F + 0.5 * m5, UA)
            KA = ph * F + o["B5"] - GA
            a2[f"{bname}|{m}"] = {"P_top_reached_A": float(np.mean(GA >= UA - 1e-6)), "E_G_A": float(GA.mean()),
                                  "E_G": float(G.mean()), "E_G_fall": float(G.mean() - GA.mean()),
                                  "U_A_p50": float(np.median(UA)), "P_flex_A": float(np.mean(KA >= 0.1 * GA))}
    out["A2_announced_basis_top"] = a2
    for b in builds:
        v = [a2[f"{b}|{m}"] for m in ("T", "BOOT", "BAYES")]
        say(f"  A2 ({b}): top from $145k reached in {min(x['P_top_reached_A'] for x in v):.1%}-"
            f"{max(x['P_top_reached_A'] for x in v):.1%}; expected gift lower by ${min(x['E_G_fall'] for x in v):,.0f}-"
            f"${max(x['E_G_fall'] for x in v):,.0f}; median top ${min(x['U_A_p50'] for x in v):,.0f}-"
            f"${max(x['U_A_p50'] for x in v):,.0f}")

    # 6c memo D6 item 1: gift below $150,000 (floor paid phi F), s = 1/2
    below = {}
    for bname, (xx, ph) in builds.items():
        for m in ("T", "BOOT", "BAYES"):
            o = C.rule(xx[m], inp["B0"], F)
            G = np.minimum(ph * F + 0.5 * np.minimum(o["B5"], o["B3"]), o["U"])
            below[f"{bname}|{m}"] = int(np.sum(G < F))
    out["gift_below_150k_paths"] = below
    say("  memo item 1, paths (of 200,000) with the gift below $150,000: " +
        "; ".join(f"{k} {v}" for k, v in below.items()))

    # 6d P(gift = face-based top): exact over phi
    eq = {}
    for bname, (xx, ph) in builds.items():
        for m in ("T", "BOOT", "BAYES", "L"):
            o = C.rule(xx[m], inp["B0"], F)
            thr = 1 + 0.5 * np.maximum(o["B3"] - o["B5"], 0) / F        # G = U iff phi >= thr
            p_exact = 1 - np.searchsorted(ph_exact, thr - 1e-6 / F, side="left") / len(ph_exact)
            eq[f"{bname}|{m}"] = {"sampled_phi": float(np.mean(np.minimum(ph * F + 0.5 * np.minimum(o['B5'], o['B3']),
                                                                         o['U']) >= o['U'] - 1e-6)),
                                  "phi_integrated_exactly": float(np.mean(p_exact))}
    out["P_gift_eq_face_top"] = eq
    say("  P(gift = face-based top) at 1/2, sampled phi -> phi integrated exactly: " + "; ".join(
        f"{k} {v['sampled_phi']:.4f} -> {v['phi_integrated_exactly']:.4f}" for k, v in eq.items()))

    # 6e Pareto grid counts: each build's counting rule on the other build's fronts
    par = {}
    for m in ("T", "BOOT", "BAYES"):
        pf = pd.read_csv(os.path.join(PRIM, "M4", f"pareto_{m}.csv"))
        pg = pd.read_csv(os.path.join(PRIM, "M4", f"pareto_grid_{m}.csv"))
        bf = pd.read_csv(os.path.join(BLO, "M4", f"pareto_{m}.csv"))
        bg = pd.read_csv(os.path.join(BLO, "M4", f"pareto_grid_{m}.csv"))
        # primary rule: front filtered to feasible + non-dominated on 200k; grid = feasible non-dominated grid
        from pymoo.util.nds.non_dominated_sorting import NonDominatedSorting
        bff = bf[bf.P_K_ge_thr_G >= 0.95]
        Fo = np.column_stack([-bff.E_G, bff.P_G_lt_L, bff.E_width])
        nd = NonDominatedSorting().do(Fo, only_non_dominated_front=True)
        bgf = bg[bg.P_K_ge_thr_G >= 0.95]
        Fg = np.column_stack([-bgf.E_G, bgf.P_G_lt_L, bgf.E_width])
        ndg = NonDominatedSorting().do(Fg, only_non_dominated_front=True)
        Fa, Fb = Fo[nd], Fg[ndg]
        dom_p_rule_on_blind = int(sum(bool(np.any(np.all(Fb <= a + 1e-12, axis=1) & np.any(Fb < a - 1e-9, axis=1)))
                                      for a in Fa))
        # blind rule on primary data
        front = pf.rename(columns={"E_gift": "E_G", "P_D": "P_G_lt_L"})
        grid = pg.rename(columns={"E_gift": "E_G", "P_D": "P_G_lt_L"}).assign(P_K_ge_thr_G=1.0)
        dom_b_rule_on_primary = bm4.dominated_by_grid(front, grid)
        par[m] = {"primary_published": int(re.search(rf"Pareto {m}\s*:.*dominated by a grid point: (\d+)",
                                                     open(os.path.join(PRIM, 'M4', 'run_log.txt')).read()).group(1)),
                  "blind_published": int(json.load(open(os.path.join(BLO, "blind_headlines.json")))[
                      f"M4.pareto.{m}.front_points_dominated_by_grid"]["value"]),
                  "primary_rule_on_blind_front": dom_p_rule_on_blind, "blind_front_feasible_nd": int(len(nd)),
                  "blind_rule_on_primary_front": int(dom_b_rule_on_primary)}
    out["pareto_counts"] = par
    say("  Pareto points dominated by a grid point (published / other build's rule on this build's front): " + "; ".join(
        f"{m}: primary {v['primary_published']} / blind rule {v['blind_rule_on_primary_front']}, blind "
        f"{v['blind_published']} / primary rule {v['primary_rule_on_blind_front']} (of {v['blind_front_feasible_nd']})"
        for m, v in par.items()))

    # 6f Sobol luck share: two summaries of the same indices
    luck = {}
    for y, us in (("top2031", ["u1", "u2", "u3"]), ("gift2033", ["u1", "u2", "u3", "u4", "u5"])):
        pa = pd.read_csv(os.path.join(PRIM, "M8", f"sobol_A_{y}.csv")).set_index("input")
        ba = pd.read_csv(os.path.join(BLO, "M8", f"sobol_A_{y}.csv"))
        bl = ba[ba.kind == "luck"]
        luck[y] = {"primary_sum_S1": float(pa.loc[us, "S1"].sum()), "primary_sum_ST": float(pa.loc[us, "ST"].sum()),
                   "blind_sum_S1": float(bl["S1"].sum()), "blind_sum_ST": float(bl["ST"].sum())}
    out["sobol_luck_share"] = luck
    say("  Sobol A luck share, sum of S1 / sum of ST: " + "; ".join(
        f"{y}: primary {v['primary_sum_S1']:.3f} / {v['primary_sum_ST']:.3f}, blind {v['blind_sum_S1']:.3f} / "
        f"{v['blind_sum_ST']:.3f}" for y, v in luck.items()))
    RES["discrepancies"] = out


# ====================================================================== 7. insight_v1 reconciliation
def e6_draws():
    """insight_v1 D6.draws(JPM ACWI): default_rng(20260927), z1 = standard_normal((200000, 6)); columns 1..5 are
    2028..2032 (D6_behavioural_numbers.py lines 65-71; E4_rival_numbers.rival_design uses req[:, 1:6])."""
    rng = np.random.default_rng(20260927)
    z1 = rng.standard_normal((200_000, 6))
    return z1[:, 1:6]


def insight_v1(inp, xp, xb):
    say("\n[7] insight_v1 reconciliation (rab/inventory.md s2)")
    z = e6_draws()
    mu, sig = C.MU_L, C.SIG_L
    x6 = mu + sig * z
    B0_e6 = 7_736 * 1.045 + 150_000 - 150_000 / 1.0498 ** 5
    B0 = inp["B0"]
    k = lambda v: round(v / 1000, 1)
    out = {"B0_E6": B0_e6, "B0_28sep": B0}

    def h8(x, b0):
        o = C.rule(x, b0, F)
        r = {f"{n}_p{q}": float(np.percentile(o[a], q)) for n, a in (("gift", "G"), ("kept", "K"), ("total", "T"))
             for q in (5, 50, 95)}
        r["top_median"] = float(np.median(o["U"]))
        r["P_top"] = float(np.mean(o["B5"] >= o["B3"]))
        ob = bc.outcomes(x, b0=b0)
        r["blind_code_same_draws_max_abs_diff"] = float(max(abs(np.percentile(ob["G"], 50) - r["gift_p50"]),
                                                            abs(np.percentile(ob["T"], 5) - r["total_p5"])))
        return r

    out["H8"] = {"E6_printed_k": {"gift": [165, 174, 188], "kept": [16, 32, 66], "total": [182, 207, 250],
                                  "top_median": 175, "P_top": 0.73},
                 "E6_draws_E6_basis": h8(x6, B0_e6), "E6_draws_28sep_basis": h8(x6, B0),
                 "primary_L_28sep": h8(xp["L"], B0), "blind_L_28sep": h8(xb["L"], B0)}
    for lab in ("E6_draws_E6_basis", "E6_draws_28sep_basis", "primary_L_28sep", "blind_L_28sep"):
        r = out["H8"][lab]
        say(f"  H8 {lab:22s} gift {k(r['gift_p5'])}/{k(r['gift_p50'])}/{k(r['gift_p95'])}k, kept "
            f"{k(r['kept_p5'])}/{k(r['kept_p50'])}/{k(r['kept_p95'])}k, total {k(r['total_p5'])}/{k(r['total_p50'])}/"
            f"{k(r['total_p95'])}k, top {k(r['top_median'])}k, P(top) {r['P_top']:.4f}")

    # H11 Vanguard-like 5.08% compound, JPM spread kept (E6 [4]: D6.lp(0.0508, 0.0508 + 0.0128))
    mu_v = math.log(1.0508)
    sig_v = math.sqrt(2 * math.log((1.0508 + 0.0128) / 1.0508))
    h11 = {}
    for lab, zz, b0 in (("E6_draws_E6_basis", z, B0_e6), ("E6_draws_28sep", z, B0),
                        ("primary_L_28sep", (xp["L"] - mu) / sig, B0), ("blind_L_28sep", (xb["L"] - mu) / sig, B0)):
        o = C.rule(mu_v + sig_v * zz, b0, F)
        h11[lab] = {"total_p5": float(np.percentile(o["T"], 5)), "total_p50": float(np.median(o["T"])),
                    "total_p95": float(np.percentile(o["T"], 95)), "P_top": float(np.mean(o["B5"] >= o["B3"])),
                    "top_median": float(np.median(o["U"]))}
    out["H11"] = h11
    say("  H11 Vanguard-like 5.08%: " + "; ".join(
        f"{lab} total {k(v['total_p5'])}/{k(v['total_p50'])}/{k(v['total_p95'])}k P(top) {v['P_top']:.3f} top "
        f"{k(v['top_median'])}k" for lab, v in h11.items()))

    # H12 bad years (bottom 10% of 3-year growth 2028-30 / 2-year growth 2031-32): gift median
    h12 = {}
    sets = [("E6_draws_E6_basis", x6, B0_e6), ("E6_draws_28sep", x6, B0)]
    sets += [(f"{b}_{m}", xx[m], B0) for b, xx in (("primary", xp), ("blind", xb)) for m in ("L", "T", "BOOT", "BAYES")]
    for lab, x, b0 in sets:
        o = C.rule(x, b0, F)
        g3, g2 = x[:, :3].sum(1), x[:, 3:].sum(1)
        early, late = g3 <= np.percentile(g3, 10), g2 <= np.percentile(g2, 10)
        h12[lab] = {"bad_2028_30_gift_median": float(np.median(o["G"][early])),
                    "bad_2031_32_gift_median": float(np.median(o["G"][late])),
                    "bad_2031_32_gift_ge_bottom": float(np.mean(o["G"][late] >= F - 1e-9))}
    out["H12"] = h12
    say("  H12 gift median in bad 2028-30 / bad 2031-32: " + "; ".join(
        f"{lab} {k(v['bad_2028_30_gift_median'])}/{k(v['bad_2031_32_gift_median'])}k" for lab, v in h12.items()))

    # H15 floor variants: $25k less floor, the freed cost goes to the stock fund
    h15 = {}
    for lab, x, b0, y5 in [("E6_draws_E6_basis", x6, B0_e6, 0.0498), ("E6_draws_28sep", x6, B0, inp["y5"])] + \
            [(f"{b}_{m}", xx[m], B0, inp["y5"]) for b, xx in (("primary", xp), ("blind", xb))
             for m in ("L", "T", "BOOT", "BAYES")]:
        base = C.rule(x, b0, F)
        v = C.rule(x, b0 + 25_000 / (1 + y5) ** 5, 125_000.0)
        h15[lab] = {"lift_total_p50": float(np.median(v["T"]) - np.median(base["T"])),
                    "lift_total_p5": float(np.percentile(v["T"], 5) - np.percentile(base["T"], 5))}
    out["H15"] = h15
    say("  H15 floor $125k vs $150k, total p50 / p5 change: " + "; ".join(
        f"{lab} {v['lift_total_p50']:+,.0f}/{v['lift_total_p5']:+,.0f}" for lab, v in h15.items()))

    # E4 / E6: s = 3/4 keeps about $8k at p5; s = 1 keeps nothing when stocks fall (phi = 1, M3 basis)
    e4 = {}
    for lab, x, b0 in [("E6_draws_E6_basis", x6, B0_e6)] + [(f"{b}_{m}", xx[m], B0) for b, xx in
                                                            (("primary", xp), ("blind", xb)) for m in ("L", "T", "BOOT", "BAYES")]:
        o34 = C.rule(x, b0, F, s=0.75)
        o1 = C.rule(x, b0, F, s=1.0)
        e4[lab] = {"kept_p5_s075": float(np.percentile(o34["K"], 5)), "P_kept_zero_s1": float(np.mean(o1["K"] <= 1e-9))}
    out["E4_s"] = e4
    say("  E4 s = 3/4 kept p5 / s = 1 P(keeps nothing): " + "; ".join(
        f"{lab} ${v['kept_p5_s075']:,.0f} / {v['P_kept_zero_s1']:.3f}" for lab, v in e4.items()))

    # H13 from M8's floor reading (E6 reading, e = 0) vs E6 [8] "5-year stays" rows
    fr = pd.read_csv(os.path.join(PRIM, "M8", "floor_reading.csv")).set_index("d_bp")
    bfr = pd.read_csv(os.path.join(BLO, "M8", "floor_reading.csv"))
    out["H13"] = {"E6_25sep_fund_k": {"-50": 23, "-100": 7}, "primary_28sep_E6_reading": {
        "-50": float(fr.loc[-50.0, "E6_fund"]), "-100": float(fr.loc[-100.0, "E6_fund"])},
        "blind_28sep_E6_reading": {"-50": float(bfr.set_index("d_bp").loc[-50.0, "E6_fund_B0"]),
                                   "-100": float(bfr.set_index("d_bp").loc[-100.0, "E6_fund_B0"])}}
    RES["insight_v1"] = out


# ====================================================================== 8. proposed numbers.yaml entries (M4, M8)
def proposed(P, inp):
    """Gate-B-reconciled M4/M8 figures that the D6 memo and cards quote, in the rab/numbers.yaml schema, for WS1/WS0.
    Values are the primary build's (rab/results/); the blind value is recorded beside each. WS2 does not write
    rab/numbers.yaml (PM-35)."""
    import yaml
    bh = {k: v["value"] for k, v in json.load(open(os.path.join(BLO, "blind_headlines.json"))).items()}
    dec, ad, fd, tor, fr = P["dec"], P["ad"], P["fd"], P["tor"], P["fr"]
    D = ["T", "BOOT", "BAYES"]
    nr = RES["discrepancies"]["narrower_range"]
    a2 = RES["discrepancies"]["A2_announced_basis_top"]
    base = {"scale": "laura_plan", "status": "MODEL", "curve_date": inp["curve_date"], "as_of": inp["curve_date"],
            "instrument_basis": "stock fund B0 = $40,736 (2 Jan 2028); floor $150,000 face, iBond/coupon delivery phi; "
                                "s = 1/2 unless stated; no fees", "gate_b": "reconciled, rab/gates/gate_B_ws2.md"}
    r2 = lambda v: round(float(v), 4)
    E = {}
    E["m4.cap_share_robust"] = {**base, "method": "rab/models/M4_SPEC.md s5 PR-6 (pre-registered, 3d98ce0)",
                                "source": "rab/models/m4_cap.py -> rab/results/M4/decision.csv",
                                "value": {m: float(dec.loc[m, "s_star"]) for m in D} | {"robust": float(dec.loc["ROBUST", "s_star"])},
                                "blind": {m: bh[f"M4.s_star.{m}"] for m in D} | {"robust": bh["M4.s_star_robust"]},
                                "unit": "share", "quote_as": "half is about the largest share that still lets Laura keep a "
                                "tenth of her gift in 19 of 20 outcomes (MODEL)"}
    E["m4.cap_share_recommendation"] = {**base, "method": "M4_SPEC PR-7", "source": "rab/results/M4/decision.csv",
                                        "value": float(dec.recommendation.iloc[0]), "blind": bh["M4.PR7_recommendation"],
                                        "unit": "share", "quote_as": "keep half (decision D6, to ratify 26 Oct)"}
    E["m4.announced_floor"] = {**base, "method": "M4_SPEC PR-3", "source": "rab/results/M4/floor_delivery.csv",
                               "value": float(fd.announced_floor.iloc[0]), "blind": bh["M4.A_announced_floor"],
                               "unit": "USD", "quote_as": "$145,000 (the owned floor, rounded down to $5,000)"}
    E["m4.floor_delivery"] = {**base, "method": "M4_SPEC s2", "source": "rab/results/M4/floor_delivery.csv",
                              "value": {"worst": round(float(fd.phi_min.iloc[0]) * F), "median": round(float(fd.phi_p50.iloc[0]) * F),
                                        "p95": round(float(fd.phi_p95.iloc[0]) * F), "P_below_150k": r2(fd.P_phi_below_1_minus_h.iloc[0])},
                              "blind": {"median": round(bh["M4.phi.p50"] * F), "p95": round(bh["M4.phi.p95"] * F)},
                              "unit": "USD / probability", "quote_as": "an iBond-fund floor pays about $149,000 in a "
                              "typical case and at least about $146,000; it falls short of $150,000 about 2 times in 3 (MODEL)"}
    E["m4.keep_10pct_at_half"] = {**base, "method": "M4_SPEC PR-5", "source": "rab/results/M4/s_profile.csv (s = 0.5)",
                                  "value": {m: r2(ad.loc[m, "P_flex"]) for m in D},
                                  "blind": {m: bh[f"M4.adopted_half.{m}.P_K_ge_thr_G"] for m in D}, "unit": "probability",
                                  "quote_as": "about 19 times in 20 (MODEL)"}
    E["m4.kept_at_half"] = {**base, "method": "M4_SPEC s4", "source": "rab/results/M4/s_profile.csv (s = 0.5)",
                            "value": {m: [round(float(ad.loc[m, "K_p5"])), round(float(ad.loc[m, "K_p50"]))] for m in D},
                            "blind": {m: [round(bh[f"M4.adopted_half.{m}.K_p5"]), round(bh[f"M4.adopted_half.{m}.K_p50"])]
                                      for m in D}, "unit": "USD (p5, p50)",
                            "quote_as": "Laura keeps about $33,000 in a typical case and at least about $15,000 in a "
                                        "1-in-20 bad case (MODEL)"}
    E["m4.below_middle_at_half"] = {**base, "method": "M4_SPEC s4 D3", "source": "rab/results/M4/s_profile.csv",
                                    "value": {m: r2(ad.loc[m, "P_below_middle"]) for m in D},
                                    "blind": {m: bh[f"M4.adopted_half.{m}.P_G_below_middle"] for m in D},
                                    "unit": "probability", "quote_as": "below the middle of the range at most about "
                                    "1 time in 200 (MODEL, history model)"}
    E["m4.rule_sensitivity"] = {**base, "method": "M4_SPEC PR-8", "source": "rab/results/M4/rule_sensitivity.csv",
                                "value": {"keep5pct_95": primary_value("M4.rule_sensitivity.thr0.05_conf0.95", P, None),
                                          "keep15pct_95": primary_value("M4.rule_sensitivity.thr0.15_conf0.95", P, None),
                                          "keep10pct_99": primary_value("M4.rule_sensitivity.thr0.1_conf0.99", P, None)},
                                "blind": {"keep5pct_95": bh["M4.rule_sensitivity.thr0.05_conf0.95"],
                                          "keep15pct_95": bh["M4.rule_sensitivity.thr0.15_conf0.95"],
                                          "keep10pct_99": bh["M4.rule_sensitivity.thr0.1_conf0.99"]},
                                "unit": "share (robust s*)", "quote_as": "a 5% reserve would allow about 2/3; a 15% "
                                "reserve about 1/5 (PR-7: 2/3 and 0.20) (MODEL)"}
    E["m4.announced_basis_top"] = {**base, "status": "MODEL (exploratory, not pre-registered)",
                                   "method": "M4_SPEC s9 A2", "source": "rab/results/M4/run_log.txt",
                                   "value": {m: r2(a2[f"primary|{m}"]["P_top_reached_A"]) for m in D},
                                   "blind": {m: r2(a2[f"blind|{m}"]["P_top_reached_A"]) for m in D},
                                   "unit": "probability", "quote_as": "about 9 times in 10, with a gift about $3,500 "
                                   "lower on average (MODEL)"}
    E["m4.narrower_range_breach"] = {**base, "status": "MODEL (explored, never recommended: PR-1)",
                                     "method": "M4_SPEC s6.6, compared at the same typical low end",
                                     "source": "rab/verification/gateB_ws2/gateB_ws2_results.json",
                                     "value": {f"{lvl}k": r2(max(nr[f"primary|{m}|A_based"][f"P_D_at_{lvl}k"] for m in D))
                                               for lvl in (160, 165)},
                                     "blind": {f"{lvl}k": r2(max(nr[f"blind|{m}|spec_F(1-h*)"][f"P_D_at_{lvl}k"] for m in D))
                                               for lvl in (160, 165)},
                                     "unit": "probability (worst of three models)",
                                     "quote_as": "a low end of $160k would be broken about 4 times in 1,000; $165k about "
                                                 "2 times in 100 (MODEL, history model)"}
    for x, row, lab in (("X4", "d", "jan2027_yields"), ("X5", "e", "jan2028_5y_yield"), ("X6", "fee", "costs"),
                        ("X1", "mu_c", "expected_return")):
        E[f"m8.{lab}"] = {**base, "method": "rab/models/M8_SPEC.md s3", "source": "rab/results/M8/sobol_B.csv, tornado.csv",
                          "value": {"sobol_ST_median_top": r2(primary_value(f"M8.sobolB.median_top2031.ST.{x}", P, None)),
                                    "tornado_median_top": [round(float(tor.loc[row, "top_p50_at_low"])),
                                                           round(float(tor.loc[row, "top_p50_at_high"]))]},
                          "blind": {"sobol_ST_median_top": bh[f"M8.sobolB.median_top2031.ST.{x}"],
                                    "tornado_median_top": [round(bh[f"M8.tornado.{x}.Y1_med_low"]),
                                                           round(bh[f"M8.tornado.{x}.Y1_med_high"])]},
                          "unit": "Sobol total index; USD (median 2031 top at low, high)",
                          "quote_as": {"jan2027_yields": "Treasury yields on 1 Jan 2027 explain about 90% of the "
                                       "variation in the typical 2031 top (MODEL)",
                                       "jan2028_5y_yield": "the 5-year yield in Jan 2028 (the floor's price) moves the "
                                       "typical top between about $168k and $182k (MODEL)",
                                       "costs": "a 1% yearly cost on all assets cuts the typical top by about $8k (MODEL)",
                                       "expected_return": "the stock-return assumption (4.1% to 8%) moves the typical "
                                       "top by under $3k (MODEL)"}[lab]}
    E["m8.floor_reading_minus50bp"] = {**base, "status": "MODEL (deterministic)", "method": "M8_SPEC s3.5 (flag F4)",
                                       "source": "rab/results/M8/floor_reading.csv",
                                       "value": {"IPS_floor": round(float(fr.loc[-50.0, "IPS_floor"])),
                                                 "IPS_fund": round(float(fr.loc[-50.0, "IPS_fund"])),
                                                 "E6_floor": round(float(fr.loc[-50.0, "E6_floor"])),
                                                 "E6_fund": round(float(fr.loc[-50.0, "E6_fund"]))},
                                       "blind": {"IPS_floor": round(bh["M8.floor_reading.d-50.IPS_floor_F"]),
                                                 "IPS_fund": round(bh["M8.floor_reading.d-50.IPS_fund_B0"]),
                                                 "E6_floor": round(bh["M8.floor_reading.d-50.E6_floor_F"]),
                                                 "E6_fund": round(bh["M8.floor_reading.d-50.E6_fund_B0"])},
                                       "unit": "USD", "quote_as": "after a 0.5-point fall before Jan 2027: floor $143k "
                                       "+ fund $29k (IPS 'whole remainder') or floor $150k + fund $23k (keep $150k)"}

    def clean(o):
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [clean(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        return o
    hdr = ("# Gate-B-reconciled WS2 entries (M4, M8) proposed for rab/numbers.yaml (NOT the Gate A file). Written by\n"
           "# rab/verification/gateB_ws2/gateB_ws2_checks.py. value = primary build (rab/results/), blind = blind\n"
           "# rebuild. The M3 entries are in rab/results/M3/numbers_proposed.yaml (also reconciled). WS1/WS0 review and\n"
           "# merge; WS2 does not write rab/numbers.yaml (PM-35).\n")
    with open(os.path.join(HERE, "numbers_proposed_M4_M8.yaml"), "w") as f:
        f.write(hdr)
        yaml.safe_dump({"proposed": clean(E)}, f, sort_keys=False, width=120, allow_unicode=False)
    say(f"[8] wrote numbers_proposed_M4_M8.yaml ({len(E)} entries)")


# ====================================================================== main
def main():
    inp = C.inputs()
    say(f"Gate B WS2 checks | {C.stamp()} | numbers.yaml sha256 {inp['numbers_sha'][:12]} (Gate A lock)")
    P = load_primary()
    tab = key_table(P, inp)
    tab.to_csv(os.path.join(HERE, "gateB_ws2_table.csv"), index=False)
    cnt = tab.verdict.value_counts().to_dict()
    say(f"[1] {len(tab)} blind headline keys compared: {cnt}")
    worst = tab[tab.verdict == "WITHIN TOL"].copy()
    RES["key_table_counts"] = cnt
    RES["outside_tol"] = tab[tab.verdict == "OUTSIDE TOL"].key.tolist()
    RES["report_only"] = tab[tab.verdict == "REPORT"][["key", "primary", "blind"]].to_dict("records")
    zs = tab[tab.noise_z != ""].copy()
    zs["az"] = zs.noise_z.astype(float).abs()
    RES["prob_noise_z_max"] = zs.loc[zs.az.idxmax(), ["key", "primary", "blind", "noise_z"]].to_dict() \
        if len(zs) else None
    RES["prob_noise_z_over_3"] = zs[zs.az > 3][["key", "primary", "blind", "noise_z"]].to_dict("records")
    say(f"    largest noise z among probabilities: {RES['prob_noise_z_max']}")
    rel = worst[(worst.rel_diff != "") & worst.tolerance.astype(str).str.contains("%")].copy()
    if len(rel):
        rel["ar"] = rel.rel_diff.astype(float).abs()
        rr = rel.loc[rel.ar.idxmax()]
        RES["largest_rel_within_tol"] = {"key": rr.key, "primary": rr.primary, "blind": rr.blind, "rel": rr.rel_diff}
        say(f"    largest relative gap within tolerance: {RES['largest_rel_within_tol']}")
    # markdown table
    with open(os.path.join(HERE, "gateB_ws2_table.md"), "w") as f:
        f.write("# Gate B WS2: all 307 blind headline keys against the primary build\n\n"
                "Generated by `gateB_ws2_checks.py`. Verdicts: MATCH (equal to the published precision: cents, or 4 decimals for the blind JSON), WITHIN TOL (spec tolerance), OUTSIDE TOL, REPORT "
                "(no tolerance; informational). `noise_z` = gap in binomial standard errors (N = 200,000 each).\n\n"
                "| key | primary | blind | diff | tolerance | noise_z | verdict |\n|---|---|---|---|---|---|---|\n")
        for r in tab.itertuples():
            d = "" if r.diff == "" else (fmt(r.diff, r.unit) if not isinstance(r.diff, str) else r.diff)
            f.write(f"| `{r.key}` | {fmt(r.primary, r.unit)} | {fmt(r.blind, r.unit)} | {d} | {r.tolerance} | "
                    f"{r.noise_z} | {r.verdict} |\n")
    primary_headlines(P)
    xp, xb, phi_p, phi_b = cross_eval(inp)
    dist_tests(xp, xb)
    noise_band(inp)
    discrepancies(inp, xp, xb, phi_p, phi_b)
    insight_v1(inp, xp, xb)
    proposed(P, inp)

    def conv(o):
        if isinstance(o, dict):
            return {str(a): conv(b) for a, b in o.items()}
        if isinstance(o, (list, tuple)):
            return [conv(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.bool_):
            return bool(o)
        return o
    json.dump(conv(RES), open(os.path.join(HERE, "gateB_ws2_results.json"), "w"), indent=1)
    open(os.path.join(HERE, "gateB_ws2_log.txt"), "w").write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
