"""Blind rebuild of M6 (rivals on the same metrics + branch-fund choice), written from rab/models/M6_SPEC.md only
(curve method, C_Y, rung costs, r1 and the floor convention come from M5_SPEC.md B1-B4, reused from blind_m5.py).

Run:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/blind_m6.py   (from the worktree root)
AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blind_curve import (CURVE_DATE, DEPOSIT_2027, DEPOSIT_2028, FLOOR_FACE, JAN_2027, JAN_2028, JAN_2031, JAN_2033,
                         PAY_MATURITIES, PAYMENT, Curve, yearfrac, yearfrac_array)
import blind_m5 as m5
from blind_m5 import N, HIST, buy_longest_first, curve_from_row, load_annual, load_soy

OUT = os.path.join(HERE, "out", "M6")
os.makedirs(OUT, exist_ok=True)

SEED = 20260930
SEED_INFL = 20260936
N_PATHS = 200_000
Y5_TODAY = float(N("market.par_curve")["5 Yr"]) / 100.0     # 0.0506
R1_TODAY = float(N("market.par_curve")["1 Yr"]) / 100.0     # 0.0459
C_TODAY = float(N("laura.ladder.cost_2027_strips"))         # 292,418.11
L_TODAY = float(N("laura.ladder.headroom_2027_strips"))     # 7,581.89
FUND0_TODAY = float(N("laura.stock_fund_2028_usd.strips"))  # 40,736
G_TODAY = L_TODAY * (1 + R1_TODAY) + DEPOSIT_2028

TRADES = {"REC": 13, "R1": 12, "R2": 24, "R3": 21, "R4": 24, "R4b": 24, "R5_m3": 72, "R5_m5": 72, "R6": 13}
GLIDE_R4 = [0.65, 0.60, 0.50, 0.40, 0.30, 0.20]
GLIDE_R4B = [0.75, 0.75, 0.75, 0.75, 0.60, 0.40]

# taus from the plan's dates
TAU_2027 = yearfrac_array(JAN_2027, PAY_MATURITIES)
TAU_2028 = yearfrac_array(JAN_2028, PAY_MATURITIES)
TAU_2031 = yearfrac_array(JAN_2031, PAY_MATURITIES)
TAU_2033 = yearfrac_array(JAN_2033, PAY_MATURITIES)   # first one negative -> DF 1 (cash)
JAN = {t: dt.date(2027 + t, 1, 1) for t in range(0, 7)}
TAU_PAY_AT = {t: yearfrac_array(JAN[t], PAY_MATURITIES) for t in range(0, 7)}
TAU_150K_AT = {t: yearfrac(JAN[t], JAN_2033) for t in range(0, 7)}

TODAY_CURVE = Curve.from_tenors(N("market.par_curve"))


# ---------------------------------------------------------------------------------------------------------------
# shared pieces
# ---------------------------------------------------------------------------------------------------------------
def reserve_on(c: Curve, taus: np.ndarray) -> float:
    return float(PAYMENT * c.df(taus).sum())


def cppi_floor_on(c: Curve, t: int) -> float:
    """floor_t: the ten payment zeros plus 150,000 at 1 Jan 2033, valued on curve c seen from 1 Jan (2027+t)."""
    return float(PAYMENT * c.df(TAU_PAY_AT[t]).sum() + FLOOR_FACE * c.df(TAU_150K_AT[t]))


def gift_rule(bottom, U31, T33):
    """Adopted announcement rule for any rival (spec section 2). Works on scalars or arrays."""
    bottom = np.asarray(bottom, float); U31 = np.asarray(U31, float); T33 = np.asarray(T33, float)
    U33 = T33 - bottom
    gift = bottom + np.minimum(np.maximum(U33, 0.0), U31) / 2.0
    gift = np.where(T33 < bottom, np.maximum(T33, 0.0), gift)
    top = bottom + U31 / 2.0
    return gift, top


def cppi_path(A0, deposits, floors, e, m):
    """CPPI over t = 0..5; A0 scalar or array; deposits[t] added at 1 Jan (2027+t) before the rebalancing;
    floors[t] for t = 0..6; e[t] equity return in year t. Returns (A at t=4, A at t=6, floor broken flag).
    The flag counts t >= 1 only: at t = 0 the floor (which includes the 150,000 promise for 2033 while future
    deposits are not counted) exceeds the 300,000 by construction, so 2027 is all zeros in every path."""
    A = np.asarray(A0, float).copy()
    broke = np.zeros_like(A, dtype=bool)
    A4 = None
    for t in range(6):
        A = A + deposits[t]
        if t == 4:
            A4 = A.copy()
        fl = floors[t]
        cushion = A - fl
        if t >= 1:
            broke = broke | (cushion < 0)
        E = np.minimum(A, m * np.maximum(cushion, 0.0))
        S = A - E
        A = E * (1.0 + e[t]) + S * floors[t + 1] / fl
    return A4, A, broke


def whole_portfolio_path(weights_eq, deposits, e, b):
    """Rebalanced every 1 Jan to the year's equity weight; deposits[t] at 1 Jan (2027+t). Returns (A4, A6)."""
    A = np.zeros_like(np.asarray(e[0], float)) + 0.0
    A4 = None
    for t in range(6):
        A = A + deposits[t]
        if t == 4:
            A4 = A.copy()
        A = A * (1.0 + weights_eq[t] * e[t] + (1 - weights_eq[t]) * b[t])
    return A4, A


def breakevens():
    """b(n) for n = 6..15 from today's par curve and the 25 Sep 2026 TIPS real yields (flat below 5 years)."""
    mi = pd.read_csv(os.path.join(HIST, "market_inflation_2026-09.csv")).set_index("series")
    real_t = np.array([5, 7, 10, 20, 30], float)
    real_y = np.array([mi.loc[f"DFII{int(t)}", "value"] for t in real_t], float) / 100.0
    rows = []
    for k in range(1, 11):
        n = 5 + k
        y_nom = TODAY_CURVE.par_yield(n)
        r_real = float(np.interp(n, real_t, real_y))
        b = (1 + y_nom) / (1 + r_real) - 1
        rows.append({"k": k, "n_years": n, "y_nom": y_nom, "r_real": r_real, "breakeven": b,
                     "tips_rung_cost_at_par": PAYMENT / (1 + b) ** n})
    return pd.DataFrame(rows), mi


def tips_delivery(bk: pd.DataFrame, infl_growth: np.ndarray):
    """infl_growth: (..., 10) CPI growth factors I_k from 1 Jan Y to 1 Jan (Y+5+k). Returns paid (..., 10)."""
    b = bk["breakeven"].to_numpy()
    n = bk["n_years"].to_numpy()
    return PAYMENT * np.maximum(1.0, infl_growth) / (1 + b) ** n


# ---------------------------------------------------------------------------------------------------------------
# History lens
# ---------------------------------------------------------------------------------------------------------------
def history_lens(soy, ann, bk):
    curves = {y: curve_from_row(soy.loc[y]) for y in soy.index}
    rows = []
    for Y in range(1872, 2021):
        cs = [curves[Y + j] for j in range(7)]
        e = [float(ann.loc[Y + t, "world_eq"]) for t in range(6)]
        b = [0.5 * float(ann.loc[Y + t, "us_bill"]) + 0.5 * float(ann.loc[Y + t, "us_bond10"]) for t in range(6)]
        I = float(np.prod([1 + ann.loc[t, "cpi_infl"] for t in range(Y, Y + 6)]))
        reserve33 = reserve_on(cs[6], TAU_2033)
        reserve31 = reserve_on(cs[4], TAU_2031)
        base = {"Y": Y, "deflator_I": I, "reserve33": reserve33, "reserve31": reserve31}

        # REC: M5 B1-B6, hist view, world_eq
        rec = m5.window(Y, "hist", "world_eq", soy, ann, ann["world_eq"], {})
        G, y5, T, S = rec["growth_money_G"], rec["y5"], rec["topup_T"], rec["short_S"]
        rows.append({**base, "rival": "REC", "assets31": rec["floor_face_F"] * cs[4].df(2.0) + rec["fund31"],
                     "certain31": rec["floor_face_F"], "U31": rec["fund31"], "top": rec["top"],
                     "T33": rec["T33"] if S == 0 else G, "gift": rec["gift"], "unfunded": S > 0, "shortfall": S,
                     "floor_broken": False, "G": G, "y5": y5, "topup_T": T})
        # R1: all-Treasury
        face = G * (1 + y5) ** 5 if G >= 0 else 0.0
        rows.append({**base, "rival": "R1", "assets31": face * cs[4].df(2.0), "certain31": face, "U31": 0.0, "top": face,
                     "T33": face if G >= 0 else G, "gift": face, "unfunded": G < 0, "shortfall": max(-G, 0.0),
                     "floor_broken": False, "G": G, "y5": y5, "topup_T": T})
        # R3: ladder + 60/40 growth money (no floor)
        r6040 = [0.6 * e[t] + 0.4 * b[t] for t in range(6)]
        g31 = float(np.prod([1 + r6040[t] for t in range(1, 4)]))
        g33 = g31 * float(np.prod([1 + r6040[t] for t in range(4, 6)]))
        if G >= 0:
            A4, A6 = G * g31, G * g33
            gift, top = gift_rule(0.0, A4, A6)
            rows.append({**base, "rival": "R3", "assets31": A4, "certain31": 0.0, "U31": A4, "top": float(top),
                         "T33": A6, "gift": float(gift), "unfunded": False, "shortfall": 0.0, "floor_broken": False,
                         "G": G, "y5": y5, "topup_T": T})
        else:
            rows.append({**base, "rival": "R3", "assets31": 0.0, "certain31": 0.0, "U31": 0.0, "top": 0.0, "T33": G,
                         "gift": 0.0, "unfunded": True, "shortfall": -G, "floor_broken": False, "G": G, "y5": y5, "topup_T": T})
        # R2, R4, R4b: whole-portfolio rules, reserve bought on 1 Jan Y+6
        deposits = [DEPOSIT_2027, DEPOSIT_2028, 0, 0, 0, 0]
        for rid, w in (("R2", [0.6] * 6), ("R4", GLIDE_R4), ("R4b", GLIDE_R4B)):
            A4, A6 = whole_portfolio_path(w, deposits, np.array(e), np.array(b))
            A4, A6 = float(A4), float(A6)
            T33 = A6 - reserve33
            U31 = max(0.0, A4 - reserve31)
            gift, top = gift_rule(0.0, U31, T33)
            rows.append({**base, "rival": rid, "assets31": A4, "certain31": 0.0, "U31": U31, "top": float(top), "T33": T33,
                         "gift": float(gift), "unfunded": T33 < 0, "shortfall": max(-T33, 0.0), "floor_broken": False,
                         "G": np.nan, "y5": y5, "topup_T": np.nan})
        # R5: CPPI, m = 3 and 5
        floors = [cppi_floor_on(cs[t], t) for t in range(7)]
        for m in (3, 5):
            A4, A6, broke = cppi_path(0.0, deposits, floors, np.array(e), m)
            A4, A6 = float(A4), float(A6)
            T33 = A6 - reserve33
            U31 = max(0.0, A4 - reserve31)
            gift, top = gift_rule(0.0, U31, T33)
            rows.append({**base, "rival": f"R5_m{m}", "assets31": A4, "certain31": 0.0, "U31": U31, "top": float(top),
                         "T33": T33, "gift": float(gift), "unfunded": T33 < 0, "shortfall": max(-T33, 0.0),
                         "floor_broken": bool(broke), "promised_150k_met": T33 >= FLOOR_FACE, "G": np.nan, "y5": y5,
                         "topup_T": np.nan, "floor0": floors[0], "floor6": floors[6]})
    hist = pd.DataFrame(rows)
    hist["real_T33"] = hist["T33"] / hist["deflator_I"]
    hist["real_gift"] = hist["gift"] / hist["deflator_I"]
    hist["top_reached"] = (hist["T33"] - hist["certain31"]) >= hist["U31"] - 1e-9

    # R6: TIPS ladder delivery under each historical inflation path, Y = 1872..2011
    trows = []
    cpi = ann["cpi_infl"]
    for Y in range(1872, 2012):
        I = np.array([np.prod([1 + cpi.loc[t] for t in range(Y, Y + 5 + k)]) for k in range(1, 11)])
        paid = tips_delivery(bk, I)
        gap = np.maximum(0.0, PAYMENT - paid)
        trows.append({"Y": Y, **{f"paid_{k}": paid[k - 1] for k in range(1, 11)}, "n_short": int((paid < PAYMENT - 1e-9).sum()),
                      "total_gap": gap.sum(), "total_paid": paid.sum(), "total_excess": np.maximum(0.0, paid - PAYMENT).sum(),
                      "infl_15y_annual": I[-1] ** (1 / 15) - 1})
    tips = pd.DataFrame(trows)
    return hist, tips


def summarize_history(hist: pd.DataFrame, tips: pd.DataFrame):
    out = []
    for rid, g in hist.groupby("rival", sort=False):
        d = {"lens": "history", "rival": rid, "n": len(g), "unfunded_share": g["unfunded"].mean(),
             "largest_shortfall": g["shortfall"].max(),
             "largest_shortfall_Y": int(g.loc[g["shortfall"].idxmax(), "Y"]) if g["shortfall"].max() > 0 else None,
             "T33_worst": g["T33"].min(), "T33_worst_Y": int(g.loc[g["T33"].idxmin(), "Y"]),
             "T33_p10": g["T33"].quantile(0.10), "T33_p50": g["T33"].quantile(0.50), "T33_p90": g["T33"].quantile(0.90),
             "certain31_p50": g["certain31"].quantile(0.5), "certain31_min": g["certain31"].min(),
             "gift_worst": g["gift"].min(), "gift_p10": g["gift"].quantile(0.10), "gift_p50": g["gift"].quantile(0.5),
             "gift_p90": g["gift"].quantile(0.9), "top_reached_share": g["top_reached"].mean(),
             "real_T33_worst": g["real_T33"].min(), "real_T33_p10": g["real_T33"].quantile(0.1),
             "real_T33_p50": g["real_T33"].quantile(0.5), "trades": TRADES[rid]}
        if rid.startswith("R5"):
            d["floor_broken_share"] = g["floor_broken"].mean()
            d["promised_150k_met_share"] = g["promised_150k_met"].mean()
        out.append(d)
    d = {"lens": "history", "rival": "R6", "n": len(tips), "unfunded_share": (tips["n_short"] > 0).mean(),
         "largest_shortfall": tips["total_gap"].max(), "largest_shortfall_Y": int(tips.loc[tips["total_gap"].idxmax(), "Y"]),
         "gap_p50": tips["total_gap"].quantile(0.5), "gap_p90": tips["total_gap"].quantile(0.9),
         "share_payments_short": (tips[[f"paid_{k}" for k in range(1, 11)]] < PAYMENT - 1e-9).to_numpy().mean(),
         "total_paid_p10": tips["total_paid"].quantile(0.1), "total_paid_p50": tips["total_paid"].quantile(0.5),
         "total_paid_p90": tips["total_paid"].quantile(0.9), "trades": TRADES["R6"],
         # alternate readings of "unfunded" for R6, reported for reconciliation (the spec's wording is per payment)
         "share_windows_total_paid_lt_500k": (tips["total_paid"] < 10 * PAYMENT - 1e-6).mean(),
         "n_short_p50": float(tips["n_short"].median()),
         "note": "delivery only; T33 = REC's by construction"}
    out.append(d)
    return pd.DataFrame(out)


# ---------------------------------------------------------------------------------------------------------------
# MC lens (JPM 2026 LTCMA)
# ---------------------------------------------------------------------------------------------------------------
MC_ASSETS = ["AC World Equity", "U.S. Large Cap", "EAFE Equity", "Emerging Markets Equity", "U.S. Small Cap",
             "U.S. Equity Value Factor", "U.S. REITs", "Gold", "U.S. Intermediate Treasuries", "U.S. Inflation"]
IDX = {a: i for i, a in enumerate(MC_ASSETS)}


def load_jpm():
    u = pd.read_csv(os.path.join(HIST, "jpm_ltcma_2026_usd.csv")).set_index("asset")
    c = pd.read_csv(os.path.join(HIST, "jpm_ltcma_2026_corr.csv"))
    comp = np.array([u.loc[a, "compound_2026"] for a in MC_ASSETS], float) / 100.0
    arith = np.array([u.loc[a, "arithmetic_2026"] for a in MC_ASSETS], float) / 100.0
    # override (ASSUMPTION, market-consistent): Intermediate Treasuries compound = today's 5-year par; arithmetic keeps the gap
    i = IDX["U.S. Intermediate Treasuries"]
    gap = arith[i] - comp[i]
    comp[i] = Y5_TODAY
    arith[i] = Y5_TODAY + gap
    R = np.eye(len(MC_ASSETS))
    for _, r in c.iterrows():
        if r["row"] in IDX and r["col"] in IDX:
            R[IDX[r["row"]], IDX[r["col"]]] = r["corr"]
            R[IDX[r["col"]], IDX[r["row"]]] = r["corr"]
    assert not np.isnan(R).any()
    w, V = np.linalg.eigh(R)
    fixed = False
    if w.min() < 1e-8:
        w = np.maximum(w, 1e-8)
        R = V @ np.diag(w) @ V.T
        dsq = np.sqrt(np.diag(R))
        R = R / np.outer(dsq, dsq)
        fixed = True
    mu = np.log1p(comp)
    s = np.sqrt(2 * np.log((1 + arith) / (1 + comp)))
    return {"compound": comp, "arith": arith, "mu": mu, "sigma": s, "corr": R, "corr_fixed": fixed,
            "min_eig_raw": float(np.linalg.eigvalsh(R).min())}


def simulate_returns(jpm, seed, n_paths=N_PATHS, n_years=6):
    rng = np.random.default_rng(seed)
    Lc = np.linalg.cholesky(jpm["corr"])
    Z = rng.standard_normal((n_years, n_paths, len(MC_ASSETS)))
    Zc = Z @ Lc.T
    return np.exp(jpm["mu"] + jpm["sigma"] * Zc) - 1.0    # (years, paths, assets) simple returns


def fwd_df(t, dy_cum_t, target: dt.date):
    """Today's curve rolled forward to 1 Jan (2027+t), every zero rate shifted by dy_cum_t (array over paths)."""
    tau = yearfrac(JAN[t], target)
    if tau <= 0:
        return np.ones_like(dy_cum_t)
    base = TODAY_CURVE.df(yearfrac(CURVE_DATE, target)) / TODAY_CURVE.df(yearfrac(CURVE_DATE, JAN[t]))
    return base * np.exp(-dy_cum_t * tau)


def mc_lens(jpm, seed=SEED):
    r = simulate_returns(jpm, seed)
    e = r[:, :, IDX["AC World Equity"]]
    b = r[:, :, IDX["U.S. Intermediate Treasuries"]]
    n = e.shape[1]
    dyr = -(b - Y5_TODAY) / 5.0                      # yield change in year t
    dy = np.zeros((7, n))
    for t in range(1, 7):
        dy[t] = dy[t - 1] + dyr[t - 1]

    def reserve(t):
        return PAYMENT * sum(fwd_df(t, dy[t], P) for P in PAY_MATURITIES)

    def floor(t):
        return PAYMENT * sum(fwd_df(t, dy[t], P) for P in PAY_MATURITIES) + FLOOR_FACE * fwd_df(t, dy[t], JAN_2033)

    reserve33, reserve31 = reserve(6), reserve(4)
    res = {}
    # REC
    y5 = np.maximum(0.001, Y5_TODAY + dy[1])
    Cf = FLOOR_FACE / (1 + y5) ** 5
    G = G_TODAY
    F = np.where(G >= Cf, FLOOR_FACE, G * (1 + y5) ** 5)
    fund0 = np.maximum(G - Cf, 0.0)
    g31 = np.prod(1 + e[1:4], axis=0)
    g33 = g31 * np.prod(1 + e[4:6], axis=0)
    fund31, fund33 = fund0 * g31, fund0 * g33
    T33 = F + fund33
    gift, top = gift_rule(F, fund31, T33)
    res["REC"] = {"T33": T33, "gift": gift, "certain31": F, "U31": fund31, "unfunded": np.zeros(n, bool), "shortfall": np.zeros(n),
                  "top_reached": fund33 >= fund31, "fund0": fund0, "y5": y5}
    # R1
    face = G * (1 + y5) ** 5
    res["R1"] = {"T33": face, "gift": face, "certain31": face, "U31": np.zeros(n), "unfunded": np.zeros(n, bool),
                 "shortfall": np.zeros(n), "top_reached": np.ones(n, bool)}
    # R3
    r6040 = 0.6 * e + 0.4 * b
    A4 = G * np.prod(1 + r6040[1:4], axis=0)
    A6 = A4 * np.prod(1 + r6040[4:6], axis=0)
    gift, top = gift_rule(0.0, A4, A6)
    res["R3"] = {"T33": A6, "gift": gift, "certain31": np.zeros(n), "U31": A4, "unfunded": np.zeros(n, bool),
                 "shortfall": np.zeros(n), "top_reached": A6 >= A4}
    # R2, R4, R4b (+ R4b deposit variants)
    for rid, w, dep28 in (("R2", [0.6] * 6, DEPOSIT_2028), ("R4", GLIDE_R4, DEPOSIT_2028), ("R4b", GLIDE_R4B, DEPOSIT_2028),
                          ("R4b_dep75k", GLIDE_R4B, 75_000.0), ("R4b_dep0", GLIDE_R4B, 0.0)):
        deposits = [DEPOSIT_2027, dep28, 0, 0, 0, 0]
        A4, A6 = whole_portfolio_path(w, deposits, e, b)
        T33 = A6 - reserve33
        U31 = np.maximum(0.0, A4 - reserve31)
        gift, top = gift_rule(0.0, U31, T33)
        res[rid] = {"T33": T33, "gift": gift, "certain31": np.zeros(n), "U31": U31, "unfunded": T33 < 0,
                    "shortfall": np.maximum(-T33, 0.0), "top_reached": np.maximum(T33, 0) >= U31}
    # R5 CPPI
    floors = [floor(t) for t in range(7)]
    deposits = [DEPOSIT_2027, DEPOSIT_2028, 0, 0, 0, 0]
    for m in (3, 5):
        A4, A6, broke = cppi_path(np.zeros(n), deposits, floors, e, m)
        T33 = A6 - reserve33
        U31 = np.maximum(0.0, A4 - reserve31)
        gift, top = gift_rule(0.0, U31, T33)
        res[f"R5_m{m}"] = {"T33": T33, "gift": gift, "certain31": np.zeros(n), "U31": U31, "unfunded": T33 < 0,
                           "shortfall": np.maximum(-T33, 0.0), "top_reached": np.maximum(T33, 0) >= U31,
                           "floor_broken": broke, "promised_150k_met": T33 >= FLOOR_FACE}
    return res, {"e": e, "b": b, "dy": dy, "reserve33": reserve33, "reserve31": reserve31, "returns": r}


def mc_inflation(ann, bk, mi, n_paths=N_PATHS):
    """R6 in the MC lens: AR(1) annual CPI inflation, its own random stream."""
    cpi = ann["cpi_infl"]
    x = cpi.loc[1952:2024].to_numpy()  # pi_{t-1}
    y = cpi.loc[1953:2025].to_numpy()  # pi_t
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    s = float(np.sqrt((resid ** 2).sum() / (len(y) - 2)))
    phi = float(beta[1])
    mu = float(mi.loc["T10YIE", "value"]) / 100.0
    raw = pd.read_csv(os.path.join(HIST, "raw", "fred_CPIAUCNS.csv"))
    raw["observation_date"] = raw["observation_date"].astype(str)
    cpi_aug26 = float(raw.loc[raw["observation_date"] == "2026-08-01", "CPIAUCNS"].iloc[0])
    cpi_aug25 = float(raw.loc[raw["observation_date"] == "2025-08-01", "CPIAUCNS"].iloc[0])
    pi0 = cpi_aug26 / cpi_aug25 - 1
    rng = np.random.default_rng(SEED_INFL)
    pi = np.empty((15, n_paths))
    prev = np.full(n_paths, pi0)
    for t in range(15):
        eps = rng.standard_normal(n_paths)
        prev = mu + phi * (prev - mu) + s * eps
        pi[t] = prev
    growth = np.cumprod(1 + pi, axis=0)          # index t: growth 2027..(2027+t)
    I = np.stack([growth[4 + k] for k in range(1, 11)], axis=1)   # (paths, 10): to 1 Jan (2032+k) = years 2027..2031+k
    paid = tips_delivery(bk, I)
    gap = np.maximum(0.0, PAYMENT - paid)
    params = {"phi": phi, "sigma": s, "mu_breakeven": mu, "pi0_aug26_over_aug25": pi0, "intercept": float(beta[0]),
              "n_obs": int(len(y)), "cpi_aug_2026": cpi_aug26, "cpi_aug_2025": cpi_aug25,
              "mean_pi_2027_2041": float(pi.mean())}
    return {"paid": paid, "gap": gap, "any_short": (paid < PAYMENT - 1e-9).any(axis=1), "params": params, "pi": pi}


def summarize_mc(res, tips_mc):
    rows = []
    pct = lambda a, p: float(np.percentile(a, p))
    for rid, d in res.items():
        r = {"lens": "MC", "rival": rid, "n": len(d["T33"]), "unfunded_share": float(d["unfunded"].mean()),
             "largest_shortfall": float(d["shortfall"].max()),
             "shortfall_p99": pct(d["shortfall"], 99),
             "T33_p5": pct(d["T33"], 5), "T33_p50": pct(d["T33"], 50), "T33_p95": pct(d["T33"], 95),
             "certain31_p50": pct(d["certain31"], 50), "certain31_min": float(d["certain31"].min()),
             "gift_p5": pct(d["gift"], 5), "gift_p50": pct(d["gift"], 50), "gift_p95": pct(d["gift"], 95),
             "top_reached_share": float(d["top_reached"].mean()), "trades": TRADES.get(rid.split("_dep")[0], np.nan)}
        if "floor_broken" in d:
            r["floor_broken_share"] = float(d["floor_broken"].mean())
            r["promised_150k_met_share"] = float(d["promised_150k_met"].mean())
        rows.append(r)
    t = tips_mc
    rows.append({"lens": "MC", "rival": "R6", "n": len(t["gap"]), "unfunded_share": float(t["any_short"].mean()),
                 "largest_shortfall": float(t["gap"].sum(axis=1).max()), "gap_p50": pct(t["gap"].sum(axis=1), 50),
                 "gap_p90": pct(t["gap"].sum(axis=1), 90), "gap_p95": pct(t["gap"].sum(axis=1), 95),
                 "share_payments_short": float((t["paid"] < PAYMENT - 1e-9).mean()),
                 "total_paid_p5": pct(t["paid"].sum(axis=1), 5), "total_paid_p50": pct(t["paid"].sum(axis=1), 50),
                 "total_paid_p95": pct(t["paid"].sum(axis=1), 95), "trades": TRADES["R6"],
                 "share_paths_total_paid_lt_500k": float((t["paid"].sum(axis=1) < 10 * PAYMENT - 1e-6).mean()),
                 "n_short_p50": float(np.median((t["paid"] < PAYMENT - 1e-9).sum(axis=1))),
                 "note": "delivery only; T33 = REC's by construction"})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------------------------
# Part B: branch-fund alternatives
# ---------------------------------------------------------------------------------------------------------------
MC_FUNDS = {
    "A0": {"AC World Equity": 1.0},
    "A1": {"U.S. Large Cap": 0.62, "EAFE Equity": 0.285, "Emerging Markets Equity": 0.095},
    "A2": {"U.S. Large Cap": 1.0},
    "A3": {"AC World Equity": 0.70, "U.S. Small Cap": 0.15, "U.S. Equity Value Factor": 0.15},
    "A4": {"AC World Equity": 0.80, "Gold": 0.10, "U.S. REITs": 0.10},
}
FUND_LABEL = {"A0": "VT (baseline)", "A1": "VTI + VXUS 62/38", "A2": "U.S. only (VTI)", "A3": "VT + small/value tilt",
              "A4": "VT + gold/REIT"}


def fund_metrics_from_paths(fund31, fund33):
    """REC with everything fixed except the fund (fund0 = numbers.yaml, floor 150,000 at today's y5)."""
    gift = FLOOR_FACE + np.minimum(fund33, fund31) / 2
    T33 = FLOOR_FACE + fund33
    return gift, T33, fund33 >= fund31, fund31 / 2


def basket_growth(returns_by_component: dict, weights: dict, years: list):
    """Buy-and-hold: value per $1 after the listed years, components compounding separately."""
    g31 = 0.0
    g33 = 0.0
    for comp, w in weights.items():
        r = returns_by_component[comp]
        p31 = np.prod([1 + r[y] for y in years[:3]], axis=0)
        p33 = p31 * np.prod([1 + r[y] for y in years[3:5]], axis=0)
        g31 = g31 + w * p31
        g33 = g33 + w * p33
    return g31, g33


def fund_mc(returns, fund_id):
    """returns: (years, paths, assets) from simulate_returns; fund bought 1 Jan 2028 = start of year index 1."""
    w = MC_FUNDS[fund_id]
    g31 = sum(wi * np.prod(1 + returns[1:4, :, IDX[a]], axis=0) for a, wi in w.items())
    g33 = sum(wi * np.prod(1 + returns[1:6, :, IDX[a]], axis=0) for a, wi in w.items())
    return FUND0_TODAY * g31, FUND0_TODAY * g33


def mc_fund_table(returns):
    pct = lambda a, p: float(np.percentile(a, p))
    rows = {}
    for fid in MC_FUNDS:
        f31, f33 = fund_mc(returns, fid)
        gift, T33, top, width = fund_metrics_from_paths(f31, f33)
        rows[fid] = {"gift_p5": pct(gift, 5), "gift_p50": pct(gift, 50), "gift_p95": pct(gift, 95),
                     "spread90": pct(gift, 95) - pct(gift, 5), "p_top": float(top.mean()),
                     "range_width_p50": pct(width, 50), "T33_p5": pct(T33, 5), "T33_p50": pct(T33, 50)}
    return rows


def history_fund_table(ann):
    a = ann.copy()
    a["exus_impl"] = (a["world_eq"] - 0.62 * a["us_eq"]) / 0.38
    hist_w = {"A0": {"world_eq": 1.0}, "A1": {"us_mkt_kf": 0.62, "exus_impl": 0.38}, "A2": {"us_mkt_kf": 1.0},
              "A3": {"world_eq": 0.70, "us_smallval": 0.30}, "A4": {"world_eq": 0.80, "gold": 0.10, "housing": 0.10}}
    etf_w = {"A0": {"vt_etf": 1.0}, "A1": {"vti_etf": 0.62, "vxus_etf": 0.38}, "A2": {"vti_etf": 1.0},
             "A4": {"vt_etf": 0.80, "gld_etf": 0.10, "vnq_etf": 0.10}}
    pct = lambda s, p: float(np.percentile(s, p))
    out = {"history": {}, "etf": {}}
    per_window = []
    for lens, wmap, years in (("history", hist_w, range(1928, 2021)), ("etf", etf_w, range(2011, 2021))):
        for fid, w in wmap.items():
            gifts, t33s, tops = [], [], []
            for Y in years:
                yrs = list(range(Y + 1, Y + 6))
                comps = {c: a[c] for c in w}
                g31, g33 = basket_growth(comps, w, yrs)
                f31, f33 = FUND0_TODAY * g31, FUND0_TODAY * g33
                gift, T33, top, width = fund_metrics_from_paths(f31, f33)
                gifts.append(float(gift)); t33s.append(float(T33)); tops.append(bool(top))
                per_window.append({"lens": lens, "fund": fid, "Y": Y, "fund31": float(f31), "fund33": float(f33),
                                   "gift": float(gift), "T33": float(T33), "top_reached": bool(top)})
            gifts = np.array(gifts)
            assert not np.isnan(gifts).any(), (lens, fid)
            out[lens][fid] = {"n": len(gifts), "gift_worst": float(gifts.min()), "gift_p10": pct(gifts, 10),
                              "gift_p50": pct(gifts, 50), "gift_p90": pct(gifts, 90), "spread80": pct(gifts, 90) - pct(gifts, 10),
                              "p_top": float(np.mean(tops)), "T33_p50": pct(np.array(t33s), 50)}
    return out, pd.DataFrame(per_window)


def switch_rule(mc: dict, hist: dict):
    """Pre-registered switch rule, tests 1-3 mechanical; test 4 is a judgement recorded as pending."""
    rows = []
    b, hb = mc["A0"], hist["A0"]
    for fid in ("A1", "A2", "A3", "A4"):
        a, ha = mc[fid], hist[fid]
        t1_p5 = a["gift_p5"] >= b["gift_p5"] + 2000
        t1_spread = a["spread90"] <= 0.90 * b["spread90"]
        t2_p5 = ha["gift_p10"] >= hb["gift_p10"] + 1000
        t2_spread = ha["spread80"] <= 0.95 * hb["spread80"]
        t2 = (t1_p5 and t2_p5) or (t1_spread and t2_spread)
        t3 = (a["gift_p50"] >= b["gift_p50"] - 500) and (ha["gift_p50"] >= hb["gift_p50"] - 1000)
        mech = (t1_p5 or t1_spread) and t2 and t3
        rows.append({"fund": fid, "label": FUND_LABEL[fid], "test1_benefit_p5": t1_p5, "test1_benefit_spread": t1_spread,
                     "test2_history_p10": t2_p5, "test2_history_spread": t2_spread, "test2_same_direction": t2,
                     "test3_median_not_cut": t3, "tests_1_to_3_pass": mech,
                     "test4_one_sentence": "judgement + WS6 listing check (not assessed mechanically)",
                     "mc_gift_p5_delta": a["gift_p5"] - b["gift_p5"], "mc_spread90_ratio": a["spread90"] / b["spread90"],
                     "mc_gift_p50_delta": a["gift_p50"] - b["gift_p50"], "hist_gift_p10_delta": ha["gift_p10"] - hb["gift_p10"],
                     "hist_spread80_ratio": ha["spread80"] / hb["spread80"], "hist_gift_p50_delta": ha["gift_p50"] - hb["gift_p50"],
                     "decision_this_seed": "SWITCH candidate (pending test 4 and seed robustness)" if mech else "KEEP VT"})
    return pd.DataFrame(rows)


def fund_robustness(jpm, hist, n_seeds=20):
    """Re-run the MC tests on other seeds; a SWITCH counts only if every seed agrees."""
    seeds = [SEED + i for i in range(n_seeds)]
    tally = {fid: {"pass_1_to_3": 0, "t1_p5": 0, "t1_spread": 0, "t3": 0} for fid in ("A1", "A2", "A3", "A4")}
    p5_by_seed = {fid: [] for fid in MC_FUNDS}
    for sd in seeds:
        r = simulate_returns(jpm, sd)
        mc = mc_fund_table(r)
        dec = switch_rule(mc, hist)
        for _, row in dec.iterrows():
            t = tally[row["fund"]]
            t["pass_1_to_3"] += int(row["tests_1_to_3_pass"]); t["t1_p5"] += int(row["test1_benefit_p5"])
            t["t1_spread"] += int(row["test1_benefit_spread"]); t["t3"] += int(row["test3_median_not_cut"])
        for fid in MC_FUNDS:
            p5_by_seed[fid].append(mc[fid]["gift_p5"])
    rows = []
    for fid, t in tally.items():
        rows.append({"fund": fid, "seeds": n_seeds, **t, "robust_switch": t["pass_1_to_3"] == n_seeds,
                     "gift_p5_seed_min": min(p5_by_seed[fid]), "gift_p5_seed_max": max(p5_by_seed[fid]),
                     "A0_gift_p5_seed_min": min(p5_by_seed["A0"]), "A0_gift_p5_seed_max": max(p5_by_seed["A0"])})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------------------------
def figures(hsum, msum, mc_funds, hist_funds):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    order = ["REC", "R1", "R2", "R3", "R4", "R4b", "R5_m3", "R5_m5"]
    fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=False)
    for ax, (lens, df, lo, hi) in zip(axes, (("history (1872-2020)", hsum, "T33_p10", "T33_p90"), ("MC (JPM 2026)", msum, "T33_p5", "T33_p95"))):
        d = df.set_index("rival").loc[order]
        x = np.arange(len(order))
        ax.bar(x, d["T33_p50"] / 1000, color="tab:blue", alpha=0.7, label="typical (median)")
        ax.errorbar(x, d["T33_p50"] / 1000, yerr=[(d["T33_p50"] - d[lo]) / 1000, (d[hi] - d["T33_p50"]) / 1000], fmt="none",
                    ecolor="black", capsize=4, label=f"bad / good ({lo[4:]} / {hi[4:]})")
        for i, rid in enumerate(order):
            ax.text(i, -0.06 * ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 0, f"short {100 * d.loc[rid, 'unfunded_share']:.1f}%",
                    ha="center", va="top", fontsize=7, color="tab:red")
        ax.set_xticks(x); ax.set_xticklabels(order, rotation=30, fontsize=8)
        ax.set_title(f"Money left on 1 Jan 2033 after the reserve (T33), {lens}")
        ax.set_ylabel("$ thousands"); ax.grid(alpha=0.3, axis="y"); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_m6_rivals.png"), dpi=150); plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    fids = list(MC_FUNDS)
    x = np.arange(len(fids))
    m = np.array([[mc_funds[f]["gift_p5"], mc_funds[f]["gift_p50"], mc_funds[f]["gift_p95"]] for f in fids]) / 1000
    axes[0].bar(x, m[:, 1], color="tab:green", alpha=0.7)
    axes[0].errorbar(x, m[:, 1], yerr=[m[:, 1] - m[:, 0], m[:, 2] - m[:, 1]], fmt="none", ecolor="black", capsize=4)
    axes[0].set_xticks(x); axes[0].set_xticklabels([FUND_LABEL[f] for f in fids], rotation=20, fontsize=8)
    axes[0].set_title("2033 gift, MC lens (p5 / median / p95)"); axes[0].set_ylabel("$ thousands"); axes[0].grid(alpha=0.3, axis="y")
    h = np.array([[hist_funds["history"][f]["gift_p10"], hist_funds["history"][f]["gift_p50"], hist_funds["history"][f]["gift_p90"]] for f in fids]) / 1000
    axes[1].bar(x, h[:, 1], color="tab:olive", alpha=0.7)
    axes[1].errorbar(x, h[:, 1], yerr=[h[:, 1] - h[:, 0], h[:, 2] - h[:, 1]], fmt="none", ecolor="black", capsize=4)
    axes[1].set_xticks(x); axes[1].set_xticklabels([FUND_LABEL[f] for f in fids], rotation=20, fontsize=8)
    axes[1].set_title("2033 gift, history 1928-2020 (p10 / median / p90)"); axes[1].grid(alpha=0.3, axis="y")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_m6_fund_choice.png"), dpi=150); plt.close(fig)


def main():
    soy, ann = load_soy(), load_annual()
    bk, mi = breakevens()
    bk.to_csv(os.path.join(OUT, "tips_breakevens.csv"), index=False, float_format="%.6f")

    hist, tips = history_lens(soy, ann, bk)
    hist.to_csv(os.path.join(OUT, "rivals_history.csv"), index=False, float_format="%.4f")
    tips.to_csv(os.path.join(OUT, "tips_history_delivery.csv"), index=False, float_format="%.2f")
    hsum = summarize_history(hist, tips)

    jpm = load_jpm()
    res, aux = mc_lens(jpm, SEED)
    tips_mc = mc_inflation(ann, bk, mi)
    msum = summarize_mc(res, tips_mc)
    summary = pd.concat([hsum, msum], ignore_index=True)
    summary.to_csv(os.path.join(OUT, "rivals_summary.csv"), index=False, float_format="%.4f")

    # Part B
    mc_funds = mc_fund_table(aux["returns"])
    hist_funds, fund_windows = history_fund_table(ann)
    fund_windows.to_csv(os.path.join(OUT, "fund_alternatives_windows.csv"), index=False, float_format="%.2f")
    frows = []
    for fid in MC_FUNDS:
        frows.append({"fund": fid, "label": FUND_LABEL[fid], "lens": "MC", **mc_funds[fid]})
        frows.append({"fund": fid, "label": FUND_LABEL[fid], "lens": "history_1928_2020", **hist_funds["history"][fid]})
        if fid in hist_funds["etf"]:
            frows.append({"fund": fid, "label": FUND_LABEL[fid], "lens": "etf_2011_2020", **hist_funds["etf"][fid]})
    falt = pd.DataFrame(frows)
    falt.to_csv(os.path.join(OUT, "fund_alternatives.csv"), index=False, float_format="%.4f")
    decision = switch_rule(mc_funds, hist_funds["history"])
    robust = fund_robustness(jpm, hist_funds["history"], n_seeds=20)
    decision = decision.merge(robust[["fund", "pass_1_to_3", "seeds", "robust_switch"]], on="fund")
    decision["final"] = np.where(decision["tests_1_to_3_pass"] & decision["robust_switch"],
                                 "SWITCH (subject to test 4)", np.where(decision["tests_1_to_3_pass"], "KEEP VT (not seed-robust)", "KEEP VT"))
    decision.to_csv(os.path.join(OUT, "fund_choice_decision.csv"), index=False, float_format="%.4f")
    robust.to_csv(os.path.join(OUT, "fund_robustness.csv"), index=False, float_format="%.2f")

    figures(hsum, msum, mc_funds, hist_funds)

    h16 = {"deposit_150k": float(res["R4b"]["unfunded"].mean()), "deposit_75k": float(res["R4b_dep75k"]["unfunded"].mean()),
           "deposit_0": float(res["R4b_dep0"]["unfunded"].mean()), "reference_H16_25sep": N("ref.H16.growth_first_miss")}
    results = {"model": "M6 blind rebuild", "spec": "rab/models/M6_SPEC.md", "seed": SEED, "n_paths": N_PATHS,
               "jpm_inputs": {"assets": MC_ASSETS, "compound": jpm["compound"].round(5).tolist(), "arith": jpm["arith"].round(5).tolist(),
                              "sigma": jpm["sigma"].round(5).tolist(), "corr_fixed": jpm["corr_fixed"], "min_eig_raw": jpm["min_eig_raw"]},
               "today": {"G": G_TODAY, "fund0": FUND0_TODAY, "y5": Y5_TODAY, "r1": R1_TODAY, "C_2027": C_TODAY},
               "breakevens": bk.round(6).to_dict(orient="records"),
               "inflation_ar1": tips_mc["params"],
               "mc_reserve33_p50": float(np.percentile(aux["reserve33"], 50)), "mc_reserve31_p50": float(np.percentile(aux["reserve31"], 50)),
               "mc_dy1_p5_p50_p95": [float(np.percentile(aux["dy"][1], p)) for p in (5, 50, 95)],
               "H16_reverify": h16,
               "rivals_summary": summary.to_dict(orient="records"),
               "fund_alternatives": falt.to_dict(orient="records"),
               "fund_choice_decision": decision.to_dict(orient="records"),
               "fund_robustness": robust.to_dict(orient="records")}
    with open(os.path.join(OUT, "M6_results.json"), "w") as f:
        json.dump(results, f, indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))

    L = ["M6 blind rebuild: rivals on the same metrics, and the branch-fund switch rule (MODEL)", "=" * 110]
    L.append(f"Today (numbers.yaml): C_2027={C_TODAY:,.2f}  L={L_TODAY:,.2f}  r1={R1_TODAY:.4f}  y5={Y5_TODAY:.4f}  G={G_TODAY:,.2f}  fund0={FUND0_TODAY:,.0f}")
    L.append(f"JPM corr matrix PD fix needed: {jpm['corr_fixed']} (min eigenvalue {jpm['min_eig_raw']:.4f}); Int. Treasuries override compound {jpm['compound'][8]:.4f}, arith {jpm['arith'][8]:.4f}")
    L.append(f"Inflation AR(1) 1953-2025: phi={tips_mc['params']['phi']:.3f} sigma={tips_mc['params']['sigma']:.4f} mu={tips_mc['params']['mu_breakeven']:.4f} pi0={tips_mc['params']['pi0_aug26_over_aug25']:.4f}")
    L.append("Breakevens b(n) for n=6..15: " + ", ".join(f"{r.n_years}y {100 * r.breakeven:.2f}%" for r in bk.itertuples()))
    L.append("")
    L.append("HISTORY LENS (Y = 1872..2020; R6 Y = 1872..2011):")
    hc = ["rival", "n", "unfunded_share", "largest_shortfall", "largest_shortfall_Y", "T33_worst", "T33_worst_Y", "T33_p10", "T33_p50", "T33_p90",
          "certain31_p50", "gift_worst", "gift_p10", "gift_p50", "gift_p90", "top_reached_share", "real_T33_worst", "real_T33_p50", "trades",
          "floor_broken_share", "promised_150k_met_share", "share_payments_short", "gap_p50", "total_paid_p50"]
    with pd.option_context("display.width", 300, "display.max_columns", 60, "display.float_format", "{:,.3f}".format):
        L.append(hsum[[c for c in hc if c in hsum.columns]].to_string(index=False))
    L.append("")
    L.append(f"MC LENS (JPM 2026 LTCMA, {N_PATHS:,} paths, seed {SEED}):")
    mc_cols = ["rival", "unfunded_share", "largest_shortfall", "shortfall_p99", "T33_p5", "T33_p50", "T33_p95", "certain31_p50", "gift_p5", "gift_p50",
               "gift_p95", "top_reached_share", "trades", "floor_broken_share", "promised_150k_met_share", "share_payments_short", "gap_p50", "gap_p95", "total_paid_p50"]
    with pd.option_context("display.width", 300, "display.max_columns", 60, "display.float_format", "{:,.3f}".format):
        L.append(msum[[c for c in mc_cols if c in msum.columns]].to_string(index=False))
    L.append("")
    L.append(f"H16 re-verified (R4b growth-first, share of MC paths where the money cannot buy the reserve): {h16}")
    L.append("")
    L.append("PART B. Fund alternatives (REC fixed except the fund; buy-and-hold):")
    with pd.option_context("display.width", 300, "display.max_columns", 60, "display.float_format", "{:,.3f}".format):
        L.append(falt.to_string(index=False))
    L.append("")
    L.append("Switch rule (pre-registered), applied mechanically (tests 1-3) + 20-seed robustness:")
    with pd.option_context("display.width", 300, "display.max_columns", 60, "display.float_format", "{:,.3f}".format):
        L.append(decision.to_string(index=False))
    L.append("")
    L.append("Assumptions: no fees/taxes (trade counts only); i.i.d. annual lognormal returns in the MC lens; JPM data as of 30 Sep 2025; bond proxy is an"
             " intermediate fund; TIPS ladder assumed to cost the same as the nominal ladder; REIT history before VNQ replaced by home prices (labelled).")
    open(os.path.join(OUT, "M6_report.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
