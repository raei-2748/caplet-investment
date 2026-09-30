"""Blind M8: which assumptions move the 2031 range (tornado + Sobol), M8_SPEC.md. Writes out/M8/.

Needs out/M3/summary.csv for one tornado reference bar (return-model choice).
Run: /Users/ray/Research/rab-ws/.venv/bin/python blind_m8.py
"""
from __future__ import annotations

import datetime as dt
import math
import time

import numpy as np
import pandas as pd
from scipy.special import ndtri, stdtrit

import blind_common as bc

OUT = bc.OUT / "M8"
OUT.mkdir(parents=True, exist_ok=True)
F_FACE, S = bc.F_FLOOR, bc.S_ADOPTED
D2027 = dt.date(2027, 1, 1)
JAN1 = [dt.date(y, 1, 1) for y in range(2028, 2033)]  # 2028..2032

BASE = {"mu_c": 0.07, "sd_log": bc.SIG_L, "inv_nu": 0.0, "d": 0.0, "e": 0.0, "fee": 0.0, "phi": 1.0}
UNIFORM = {"mu_c": (0.0408, 0.0800), "sd_log": (0.12, 0.20), "inv_nu": (0.0, 1.0 / 3.0), "fee": (0.0, 0.010), "phi": (0.9755, 1.0)}

_tenors, _ys = bc.load_par_curve()
CURVE = bc.D1Curve(_tenors, _ys)
LADDER = bc.Ladder(CURVE, bc.NOV15_DATES)


# ---- data: empirical yield changes -------------------------------------------------------------------------------
def fred_changes(series: str, days: int) -> np.ndarray:
    df = pd.read_csv(bc.DATA / "fred" / f"{series}.csv")
    df.columns = ["date", "v"]
    df["v"] = pd.to_numeric(df["v"], errors="coerce")
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"] >= "1990-01-02"].reset_index(drop=True)
    dates = df["date"].to_numpy(dtype="datetime64[D]")
    vals = df["v"].to_numpy(dtype=float)
    ends = dates + np.timedelta64(days, "D")
    ok = ends <= dates[-1]
    idx = np.searchsorted(dates, ends[ok], side="right") - 1
    return vals[idx] - vals[ok]


D_CHANGES_BP = fred_changes("DGS10", 95) * 100.0   # X4: 95-day change of the 10-year, in bp
E_CHANGES_PTS = fred_changes("DGS5", 365)          # X5: 365-day change of the 5-year, in points


def emp_quantile(samples: np.ndarray, u) -> np.ndarray:
    return np.percentile(samples, 100.0 * np.asarray(u, dtype=float))


# ---- the one-path model (M8_SPEC section 1) ----------------------------------------------------------------------
def curve_block(d_bp: np.ndarray):
    """V0(d), V_A(d) and the ladder value on 1 Jan 2028..2032, arrays over the shift vector d (bp)."""
    d_bp = np.atleast_1d(np.asarray(d_bp, dtype=float))
    v0 = LADDER.v0(d_bp)
    dfs = CURVE.df([D2027] + JAN1, d_bp)  # (m, 6)
    va = v0 / dfs[:, 0]
    lv = v0[:, None] / dfs[:, 1:]          # (m, 5): 2028..2032
    return v0, va, lv


def second_deposit(va, v28, y1, y5, reading: str = "IPS"):
    """F and B0 on 2 Jan 2028. reading 'IPS': the floor repays the whole remainder; 'E6': $150k face kept."""
    gap = va > bc.DEPOSIT_2027
    leftover = np.maximum(bc.DEPOSIT_2027 - va, 0.0)
    disc5 = (1.0 + y5) ** 5
    top_up = np.where(gap, (va - bc.DEPOSIT_2027) * v28 / va, 0.0)
    if reading == "IPS":
        r = np.maximum(0.0, bc.DEPOSIT_2028 - top_up)
        f = np.where(gap, r, bc.DEPOSIT_2028)
        b0 = np.where(gap, r - r / disc5, leftover * (1.0 + y1) + bc.DEPOSIT_2028 - bc.DEPOSIT_2028 / disc5)
    else:  # E6 reading
        f = np.full_like(va, bc.DEPOSIT_2028)
        b0 = leftover * (1.0 + y1) + bc.DEPOSIT_2028 - bc.DEPOSIT_2028 / disc5 - top_up
    return f, b0


def shocks(u: np.ndarray, inv_nu: np.ndarray) -> np.ndarray:
    """z = Phi^-1(u) if inv_nu = 0 else t^-1_nu(u) sqrt((nu-2)/nu), clipped to [-5, 5]. Broadcasts inv_nu against u."""
    inv_nu = np.asarray(inv_nu, dtype=float)
    z_n = ndtri(u)
    if np.all(inv_nu == 0):
        return np.clip(np.broadcast_to(z_n, np.broadcast_shapes(z_n.shape, inv_nu.shape)), -5, 5)
    nu = 1.0 / np.where(inv_nu > 0, inv_nu, 1.0)  # placeholder where inv_nu == 0
    z_t = stdtrit(nu, u) * np.sqrt((nu - 2.0) / nu)
    z = np.where(inv_nu > 0, z_t, z_n)
    return np.clip(z, -5.0, 5.0)


def simulate(mu_c, sd_log, inv_nu, d, e, fee, u, phi=1.0, years: int = 5, s: float = S, reading: str = "IPS"):
    """Y1 = top of the 2031 range (U) and Y2 = the 2033 gift (G, needs years = 5).

    Parameter arrays have shape (m,) (or scalars); u has shape (m, n, k) or (m, k) or (k,), k >= years.
    Returns (U, G, F, B0) broadcast to (m, n) (n = 1 when u has one luck path per parameter set).
    """
    mu_c, sd_log, inv_nu, d, e, fee, phi = [np.atleast_1d(np.asarray(a, dtype=float)) for a in (mu_c, sd_log, inv_nu, d, e, fee, phi)]
    m = max(a.shape[0] for a in (mu_c, sd_log, inv_nu, d, e, fee, phi))
    u = np.asarray(u, dtype=float)
    if u.ndim == 1:
        u = u[None, None, :]
    elif u.ndim == 2:
        u = u[:, None, :] if u.shape[0] == m else u[None, :, :]
    n = u.shape[1]
    col = lambda a: (np.broadcast_to(a, (m,)))[:, None]  # (m, 1)

    v0, va, lv = curve_block(np.broadcast_to(d, (m,)))
    y1 = bc.Y1_PAR + np.broadcast_to(d, (m,)) / 10_000.0
    y5 = np.maximum(0.001, bc.Y5_PAR + np.broadcast_to(d, (m,)) / 10_000.0 + np.broadcast_to(e, (m,)) / 100.0)
    f, b0 = second_deposit(va, lv[:, 0], y1, y5, reading)
    f, b0, y5 = f[:, None], b0[:, None], y5[:, None]
    floor_cost = f / (1.0 + y5) ** 5

    z = shocks(u[:, :, :years], col(inv_nu)[:, :, None])  # (m, n, years)
    mu_log = np.log1p(col(mu_c))
    sd = col(sd_log)
    fee_c = col(fee)
    b = np.broadcast_to(b0, (m, n)).copy()
    b3 = None
    for k in range(years):
        fv = floor_cost * (1.0 + y5) ** k
        fee_k = fee_c * (lv[:, k][:, None] + fv + b)
        b = np.maximum(b - fee_k, 0.0) * np.exp(mu_log + sd * z[:, :, k])
        if k == 2:
            b3 = b.copy()
    top = f + s * b3
    if years >= 5:
        gift = np.minimum(col(phi) * f + s * np.minimum(b, b3), top)
    else:
        gift = np.full_like(top, np.nan)
    return top, gift, np.broadcast_to(f, (m, n)), np.broadcast_to(b0, (m, n))


def main() -> None:
    t0 = time.time()
    log = []
    say = lambda s_: (print(s_, flush=True), log.append(s_))

    # --- base checks (M8_SPEC s1, exact) -------------------------------------------------------------------------
    v0, va, lv = curve_block(np.array([0.0]))
    f0, b00 = second_deposit(va, lv[:, 0], bc.Y1_PAR, bc.Y5_PAR)
    say(f"base: V_A(0) = {va[0]:,.2f} (locked 292,418.11); B0 = {b00[0]:,.2f} (locked 40,736.19); V_28 = {lv[0,0]:,.2f}")
    assert abs(va[0] - 292_418.11) < 0.01 and abs(b00[0] - 40_736.19) < 0.01

    # --- input_ranges.csv ----------------------------------------------------------------------------------------
    x4_lo, x4_hi = np.percentile(D_CHANGES_BP, [2.5, 97.5])
    x5_lo, x5_hi = np.percentile(E_CHANGES_PTS, [2.5, 97.5])
    pd.DataFrame([
        {"input": "X4 d: 95-day change of DGS10 (bp)", "n": D_CHANGES_BP.shape[0], "p2.5": x4_lo, "p50": np.median(D_CHANGES_BP), "p97.5": x4_hi,
         "min": D_CHANGES_BP.min(), "max": D_CHANGES_BP.max(), "share_below_-26.2bp_(headroom_gone)": (D_CHANGES_BP < -26.2).mean()},
        {"input": "X5 e: 365-day change of DGS5 (points)", "n": E_CHANGES_PTS.shape[0], "p2.5": x5_lo, "p50": np.median(E_CHANGES_PTS), "p97.5": x5_hi,
         "min": E_CHANGES_PTS.min(), "max": E_CHANGES_PTS.max(), "share_below_-26.2bp_(headroom_gone)": np.nan},
    ]).to_csv(OUT / "input_ranges.csv", index=False)
    say(f"X4 d: 2.5%/97.5% = {x4_lo:+.1f} / {x4_hi:+.1f} bp (n={D_CHANGES_BP.shape[0]}); X5 e: {x5_lo:+.2f} / {x5_hi:+.2f} points (n={E_CHANGES_PTS.shape[0]})")
    lohi = {"mu_c": UNIFORM["mu_c"], "sd_log": UNIFORM["sd_log"], "inv_nu": UNIFORM["inv_nu"], "d": (x4_lo, x4_hi),
            "e": (x5_lo, x5_hi), "fee": UNIFORM["fee"], "phi": UNIFORM["phi"]}
    labels = {"mu_c": "X1 stock fund compound return", "sd_log": "X2 sd of annual log return", "inv_nu": "X3 tail heaviness 1/nu",
              "d": "X4 curve shift to 1 Jan 2027 (bp)", "e": "X5 5-year yield change in 2027 (pts)", "fee": "X6 yearly fee on all assets",
              "phi": "X7 floor delivery ratio (gift only)"}

    # --- 1. tornado --------------------------------------------------------------------------------------------------
    rng = np.random.default_rng(np.random.SeedSequence([bc.SEED, 8]))
    u_common = rng.random((bc.N_PATHS, 5))

    def run(params: dict, s_: float = S):
        top, gift, _, _ = simulate(params["mu_c"], params["sd_log"], params["inv_nu"], params["d"], params["e"], params["fee"],
                                   u_common, phi=params["phi"], years=5, s=s_)
        return float(np.median(top)), float(np.percentile(top, 5)), float(np.median(gift))

    base_med, base_p5, base_g = run(BASE)
    rows = [{"input": "BASE", "low_value": np.nan, "high_value": np.nan, "Y1_med_low": base_med, "Y1_med_high": base_med,
             "Y1_p5_low": base_p5, "Y1_p5_high": base_p5, "Y2_med_low": base_g, "Y2_med_high": base_g, "swing_Y1_med": 0.0,
             "kind": "base"}]
    for key in ("mu_c", "sd_log", "inv_nu", "d", "e", "fee", "phi"):
        lo, hi = lohi[key]
        pl, ph = dict(BASE), dict(BASE)
        pl[key], ph[key] = lo, hi
        ml, p5l, gl = run(pl)
        mh, p5h, gh = run(ph)
        rows.append({"input": labels[key], "low_value": lo, "high_value": hi, "Y1_med_low": ml, "Y1_med_high": mh, "Y1_p5_low": p5l,
                     "Y1_p5_high": p5h, "Y2_med_low": gl, "Y2_med_high": gh, "swing_Y1_med": abs(mh - ml), "kind": "assumption"})
    # reference bars (not assumptions)
    m13, p13, g13 = run(BASE, s_=1 / 3)
    m23, p23, g23 = run(BASE, s_=2 / 3)
    rows.append({"input": "REF decision lever s = 1/3 vs 2/3", "low_value": 1 / 3, "high_value": 2 / 3, "Y1_med_low": m13, "Y1_med_high": m23,
                 "Y1_p5_low": p13, "Y1_p5_high": p23, "Y2_med_low": g13, "Y2_med_high": g23, "swing_Y1_med": abs(m23 - m13), "kind": "reference"})
    m3 = pd.read_csv(bc.OUT / "M3" / "summary.csv").set_index("model")
    tops = m3.loc[["L", "T", "BOOT", "BAYES"], "U_p50"]
    rows.append({"input": "REF return-model choice (M3 L/T/BOOT/BAYES median top)", "low_value": tops.idxmin(), "high_value": tops.idxmax(),
                 "Y1_med_low": tops.min(), "Y1_med_high": tops.max(), "Y1_p5_low": np.nan, "Y1_p5_high": np.nan, "Y2_med_low": np.nan,
                 "Y2_med_high": np.nan, "swing_Y1_med": tops.max() - tops.min(), "kind": "reference"})
    tornado = pd.DataFrame(rows)
    tornado_sorted = pd.concat([tornado[tornado.kind == "base"],
                                tornado[tornado.kind == "assumption"].sort_values("swing_Y1_med", ascending=False),
                                tornado[tornado.kind == "reference"]])
    tornado_sorted.to_csv(OUT / "tornado.csv", index=False)
    say(f"tornado base: median top {base_med:,.0f}, p5 {base_p5:,.0f}, median gift {base_g:,.0f}")
    for _, r in tornado_sorted[tornado_sorted.kind == "assumption"].iterrows():
        say(f"  {r['input']:42s} low {r['Y1_med_low']:>9,.0f}  high {r['Y1_med_high']:>9,.0f}  swing {r['swing_Y1_med']:>8,.0f}")
    tornado_rank = list(tornado_sorted[tornado_sorted.kind == "assumption"]["input"].str[:2])

    # --- 2. Sobol A (luck included) ---------------------------------------------------------------------------------
    from SALib.analyze import sobol as sobol_an
    from SALib.sample import sobol as sobol_sp

    def sobol_A(names, bounds, n_luck, years, fn, tag):
        prob = {"num_vars": len(names), "names": names, "bounds": bounds}
        X = sobol_sp.sample(prob, 2**14, calc_second_order=False, seed=bc.SEED)
        Y = fn(X)
        Si = sobol_an.analyze(prob, Y, calc_second_order=False, conf_level=0.95, seed=bc.SEED, print_to_console=False)
        df = pd.DataFrame({"input": names, "S1": Si["S1"], "S1_conf95": Si["S1_conf"], "ST": Si["ST"], "ST_conf95": Si["ST_conf"]})
        df["kind"] = ["luck" if nm.startswith("u") else "assumption" for nm in names]
        df["n_samples"] = X.shape[0]
        df["Y_median"] = np.median(Y)
        df["Y_p5"] = np.percentile(Y, 5)
        df.to_csv(OUT / f"sobol_A_{tag}.csv", index=False)
        luck = df[df.kind == "luck"]
        assum = df[df.kind == "assumption"]
        say(f"Sobol A {tag}: n={X.shape[0]}; S1 luck {luck.S1.sum():.3f} vs assumptions {assum.S1.sum():.3f}; "
            f"ST top: " + ", ".join(f"{r.input} {r.ST:.3f}" for r in df.sort_values('ST', ascending=False).head(4).itertuples()))
        return df

    def fn_top(X):
        mu_c, sd, inv, du, eu, fee = (X[:, i] for i in range(6))
        top, _, _, _ = simulate(mu_c, sd, inv, emp_quantile(D_CHANGES_BP, du), emp_quantile(E_CHANGES_PTS, eu), fee, X[:, 6:9], years=3)
        return top[:, 0]

    def fn_gift(X):
        mu_c, sd, inv, du, eu, fee, phi = (X[:, i] for i in range(7))
        _, gift, _, _ = simulate(mu_c, sd, inv, emp_quantile(D_CHANGES_BP, du), emp_quantile(E_CHANGES_PTS, eu), fee, X[:, 7:12], phi=phi, years=5)
        return gift[:, 0]

    namesA1 = ["X1 mu_c", "X2 sd_log", "X3 inv_nu", "X4 d", "X5 e", "X6 fee", "u1", "u2", "u3"]
    boundsA1 = [list(UNIFORM["mu_c"]), list(UNIFORM["sd_log"]), list(UNIFORM["inv_nu"]), [0, 1], [0, 1], list(UNIFORM["fee"]), [0, 1], [0, 1], [0, 1]]
    sA1 = sobol_A(namesA1, boundsA1, 3, 3, fn_top, "top2031")
    namesA2 = namesA1[:6] + ["X7 phi", "u1", "u2", "u3", "u4", "u5"]
    boundsA2 = boundsA1[:6] + [list(UNIFORM["phi"])] + [[0, 1]] * 5
    sA2 = sobol_A(namesA2, boundsA2, 5, 5, fn_gift, "gift2033")

    # --- 3. Sobol B (assumptions only; median and p5 of Y1 over 4,000 fixed luck paths) -------------------------------
    rngB = np.random.default_rng(np.random.SeedSequence([bc.SEED, 88]))
    u_fixed = rngB.random((4000, 3))
    probB = {"num_vars": 6, "names": namesA1[:6], "bounds": boundsA1[:6]}
    XB = sobol_sp.sample(probB, 2**12, calc_second_order=False, seed=bc.SEED)
    t1 = time.time()
    med = np.empty(XB.shape[0])
    p5 = np.empty(XB.shape[0])
    chunk = 256
    for i in range(0, XB.shape[0], chunk):
        Xc = XB[i:i + chunk]
        top, _, _, _ = simulate(Xc[:, 0], Xc[:, 1], Xc[:, 2], emp_quantile(D_CHANGES_BP, Xc[:, 3]), emp_quantile(E_CHANGES_PTS, Xc[:, 4]),
                                Xc[:, 5], u_fixed, years=3)
        med[i:i + chunk] = np.median(top, axis=1)
        p5[i:i + chunk] = np.percentile(top, 5, axis=1)
    say(f"Sobol B: {XB.shape[0]} parameter sets x 4000 luck paths in {time.time()-t1:.0f}s")
    outB = []
    for tag, Y in (("median_top2031", med), ("p5_top2031", p5)):
        Si = sobol_an.analyze(probB, Y, calc_second_order=False, conf_level=0.95, seed=bc.SEED, print_to_console=False)
        for j, nm in enumerate(probB["names"]):
            outB.append({"output": tag, "input": nm, "S1": Si["S1"][j], "S1_conf95": Si["S1_conf"][j], "ST": Si["ST"][j], "ST_conf95": Si["ST_conf"][j]})
    sB = pd.DataFrame(outB)
    sB.to_csv(OUT / "sobol_B.csv", index=False)
    rank_med = list(sB[sB.output == "median_top2031"].sort_values("ST", ascending=False)["input"].str[:2])
    rank_p5 = list(sB[sB.output == "p5_top2031"].sort_values("ST", ascending=False)["input"].str[:2])
    say("Sobol B ST (median top): " + ", ".join(f"{r.input} {r.ST:.3f}" for r in sB[sB.output == 'median_top2031'].sort_values('ST', ascending=False).itertuples()))
    say("Sobol B ST (p5 top):     " + ", ".join(f"{r.input} {r.ST:.3f}" for r in sB[sB.output == 'p5_top2031'].sort_values('ST', ascending=False).itertuples()))

    # --- 4. the three assumptions the IPS must state (pre-registered rule) ---------------------------------------------
    top3 = rank_med[:3]
    agree_p5 = set(top3) == set(rank_p5[:3])
    agree_tornado = set(top3) == set(tornado_rank[:3])
    verdict = {"top3_by_sobolB_median_ST": top3, "top3_by_sobolB_p5_ST": rank_p5[:3], "top3_by_tornado_swing": tornado_rank[:3],
               "p5_agrees": agree_p5, "tornado_agrees": agree_tornado,
               "rule": "the three inputs with the largest ST in Sobol B for the median Y1; disagreements reported, not resolved by hand"}
    say(f"IPS must state (Sobol B median ST): {top3}; p5 ranking {rank_p5[:3]} agrees={agree_p5}; tornado {tornado_rank[:3]} agrees={agree_tornado}")

    # --- 5. floor_reading.csv ----------------------------------------------------------------------------------------
    fr = []
    for dd in (0.0, -50.0, -100.0):
        v0d, vad, lvd = curve_block(np.array([dd]))
        y1 = bc.Y1_PAR + dd / 10_000
        y5 = max(0.001, bc.Y5_PAR + dd / 10_000)
        f_ips, b_ips = second_deposit(vad, lvd[:, 0], y1, y5, "IPS")
        f_e6, b_e6 = second_deposit(vad, lvd[:, 0], y1, y5, "E6")
        fr.append({"d_bp": dd, "V_A": vad[0], "gap_2027": max(0.0, vad[0] - bc.DEPOSIT_2027), "V_28": lvd[0, 0],
                   "top_up_T": max(0.0, (vad[0] - bc.DEPOSIT_2027) * lvd[0, 0] / vad[0]), "y5_2028": y5,
                   "IPS_floor_F": f_ips[0], "IPS_fund_B0": b_ips[0], "E6_floor_F": f_e6[0], "E6_fund_B0": b_e6[0],
                   "IPS_top2031_median_paths": np.nan})
    pd.DataFrame(fr).to_csv(OUT / "floor_reading.csv", index=False)
    for r in fr:
        say(f"floor reading d={r['d_bp']:+.0f}bp: V_A {r['V_A']:,.0f}; IPS F {r['IPS_floor_F']:,.0f} B0 {r['IPS_fund_B0']:,.0f}; "
            f"E6 F {r['E6_floor_F']:,.0f} B0 {r['E6_fund_B0']:,.0f}")

    # --- figures ---------------------------------------------------------------------------------------------------
    try:
        make_figures(tornado_sorted, sA1, sA2, sB, base_med)
    except Exception as exc:
        say(f"figure step failed: {exc!r}")

    head = {"base": {"top2031_median": base_med, "top2031_p5": base_p5, "gift2033_median": base_g, "V_A_0": float(va[0]), "B0": float(b00[0])},
            "input_ranges": {"X4_d_bp_2.5_97.5": [float(x4_lo), float(x4_hi)], "X5_e_pts_2.5_97.5": [float(x5_lo), float(x5_hi)],
                             "n_d": int(D_CHANGES_BP.shape[0]), "n_e": int(E_CHANGES_PTS.shape[0])},
            "tornado": tornado_sorted.drop(columns=["kind"]).to_dict(orient="records"),
            "tornado_rank": tornado_rank,
            "sobol_A_top2031": sA1[["input", "S1", "ST", "ST_conf95"]].to_dict(orient="records"),
            "sobol_A_top2031_luck_share_S1": float(sA1[sA1.kind == "luck"].S1.sum()),
            "sobol_A_top2031_assumption_share_S1": float(sA1[sA1.kind == "assumption"].S1.sum()),
            "sobol_A_gift2033": sA2[["input", "S1", "ST", "ST_conf95"]].to_dict(orient="records"),
            "sobol_A_gift2033_luck_share_S1": float(sA2[sA2.kind == "luck"].S1.sum()),
            "sobol_A_gift2033_assumption_share_S1": float(sA2[sA2.kind == "assumption"].S1.sum()),
            "sobol_B": sB.to_dict(orient="records"), "ips_must_state": verdict, "floor_reading": fr,
            "elapsed_s": time.time() - t0, "log": log}
    bc.write_json(head, OUT / "headline_M8.json")
    say(f"M8 done in {time.time()-t0:.0f}s -> {OUT}")


def make_figures(tornado: pd.DataFrame, sA1, sA2, sB, base_med: float) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    d = tornado[tornado.kind != "base"].iloc[::-1]
    fig, ax = plt.subplots(figsize=(9, 4.8))
    y = np.arange(len(d))
    for i, r in enumerate(d.itertuples()):
        col = "#0072B2" if r.kind == "assumption" else "#999999"
        lo, hi = sorted([r.Y1_med_low, r.Y1_med_high])
        ax.barh(i, (hi - lo) / 1000, left=(lo - base_med) / 1000, color=col, height=0.6)
        ax.text((hi - base_med) / 1000 + 0.3, i, f"\\${lo/1000:.0f}k to \\${hi/1000:.0f}k", va="center", fontsize=8)
    ax.axvline(0, color="k", lw=1)
    ax.set_yticks(y)
    ax.set_yticklabels(d["input"], fontsize=8)
    ax.set_xlim(-35, 30)
    ax.set_xlabel(f"change in the median 2031 top from the base \\${base_med/1000:.0f}k (\\$ thousand)\ngrey bars are reference levers, not assumptions", fontsize=9)
    ax.set_title("Tornado: each input at its low and high value, others at base (blind rebuild)", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M8_tornado.png", dpi=150)
    plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, (tag, df) in zip(axes[:2], (("median top 2031", sB[sB.output == "median_top2031"]), ("5th percentile top 2031", sB[sB.output == "p5_top2031"]))):
        df = df.sort_values("ST", ascending=True)
        yy = np.arange(len(df))
        ax.barh(yy + 0.2, df["ST"], height=0.4, color="#0072B2", label="total ST", xerr=df["ST_conf95"], error_kw={"lw": 0.8})
        ax.barh(yy - 0.2, df["S1"], height=0.4, color="#56B4E9", label="first-order S1", xerr=df["S1_conf95"], error_kw={"lw": 0.8})
        ax.set_yticks(yy)
        ax.set_yticklabels(df["input"], fontsize=8)
        ax.set_title(f"Sobol B (assumptions only): {tag}", fontsize=9)
        ax.set_xlim(0, 1)
        ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax = axes[2]
    for k, (tag, df, col) in enumerate((("top 2031", sA1, "#0072B2"), ("gift 2033", sA2, "#009E73"))):
        luck = df[df.kind == "luck"].S1.sum()
        assum = df[df.kind == "assumption"].S1.sum()
        ax.bar(k - 0.2, luck, width=0.4, color="#D55E00", label="market luck" if k == 0 else None)
        ax.bar(k + 0.2, assum, width=0.4, color=col, label="assumptions" if k == 0 else None)
        ax.text(k - 0.2, luck + 0.01, f"{100*luck:.0f}%", ha="center", fontsize=8)
        ax.text(k + 0.2, assum + 0.01, f"{100*assum:.0f}%", ha="center", fontsize=8)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["top 2031", "gift 2033"])
    ax.set_ylim(0, 1)
    ax.set_title("Sobol A: share of variance (sum of S1)", fontsize=9)
    ax.legend(frameon=False, fontsize=8)
    fig.suptitle("M8 Sobol indices (blind rebuild)", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M8_sobol.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
