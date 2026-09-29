"""M6: rivals on the same metrics, and the branch-fund choice with a pre-registered switch rule. Spec: M6_SPEC.md.

AI-generated research code (Claude Code) for Team Caplet, WS3, 2026-09-30. MODEL outputs only (history replayed
through each rival's rules; J.P. Morgan 2026 LTCMA Monte Carlo). Not a forecast. No network. Seed 20260930.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m6_rivals.py
Writes rab/results/M6/.
"""
import json
import os
from datetime import date

import numpy as np
import pandas as pd

import hist_lib as H
from m5_backtest import TAU_27, TAU_28, rec_window

OUT = os.path.join(H.RES, "M6")
LOG = []
PATHS = 200_000
RIVALS = ["REC", "R1", "R2", "R3", "R4", "R4b", "R5", "R5m5", "R6"]
NAMES = {"REC": "Root-and-Branch (adopted)", "R1": "All-Treasury", "R2": "60/40 whole portfolio",
         "R3": "Ladder + 60/40 growth money", "R4": "Glide path 65->20", "R4b": "Growth-first 75->40", "R5": "CPPI m=3", "R5m5": "CPPI m=5",
         "R6": "TIPS ladder + REC branch"}
TRADES = {"REC": 13, "R1": 12, "R2": 24, "R3": 21, "R4": 24, "R4b": 24, "R5": 72, "R5m5": 72, "R6": 13}
GLIDE = [0.65, 0.60, 0.50, 0.40, 0.30, 0.20]
GROWTH_FIRST = [0.75, 0.75, 0.75, 0.75, 0.60, 0.40]      # insight_v1 E7 firm B / strategy_mc.py default (ref H16)


def say(s=""):
    LOG.append(s)
    print(s)


def dates_tau(d0, dates):
    return np.array([H.yf(d0, d) for d in dates])


TAU31 = dates_tau(H.A31, H.NOV15)
TAU33 = dates_tau(H.A33, H.NOV15)          # first entry is negative (15 Nov 2032 < 1 Jan 2033): cash, DF = 1


def floor_flows_tau(tprime):
    """CPPI floor cash flows seen from 1 Jan (2027 + t'): the ten payment zeros and 150,000 on 1 Jan 2033."""
    d0 = date(2027 + tprime, 1, 1)
    return dates_tau(d0, H.NOV15), H.yf(d0, H.A33)


def reserve_value(dfun, tau):
    """50,000 per payment; zeros that already matured count as cash (DF of a negative time = 1)."""
    return float(H.PAY * np.where(tau <= 0, 1.0, dfun(np.maximum(tau, 0))).sum())


# ================================================================================================= history lens
def ladder_step(rungs27, r1, rungs28):
    M, f = H.DEP1, np.zeros(10)
    for k in range(9, -1, -1):
        f[k] = min(1.0, M / rungs27[k]) if M > 0 else 0.0
        M -= f[k] * rungs27[k]
    L = max(M, 0.0) if f.min() >= 1 - 1e-12 else 0.0
    T = float(((1 - f) * rungs28).sum())
    return L, T, L * (1 + r1) + H.DEP2 - T


def gift_rule(bottom, T33, U31):
    U33 = T33 - bottom
    if T33 < bottom:
        return max(T33, 0.0)
    return bottom + min(max(U33, 0.0), max(U31, 0.0)) / 2


def history_lens():
    soy, A = H.load_soy(), H.load_annual()
    mi = pd.read_csv(os.path.join(H.HIST, "market_inflation_2026-09.csv")).set_index("series").value
    b_k = breakevens(mi)
    rows = []
    for Y in range(1872, 2021):
        cv = {t: H.soy_curve(soy, Y + t) for t in range(7)}
        e = A.loc[Y:Y + 5, "world_eq"].values
        b = 0.5 * A.loc[Y:Y + 5, "us_bill"].values + 0.5 * A.loc[Y:Y + 5, "us_bond10"].values
        cpi = A.loc[Y:Y + 5, "cpi_infl"].values
        I6 = float(np.prod(1 + cpi))
        rungs27, rungs28 = H.PAY * cv[0].df(TAU_27), H.PAY * cv[1].df(TAU_28)
        r1 = soy.loc[Y, "1 Yr"] / 100 if soy.loc[Y, "1 Yr"] == soy.loc[Y, "1 Yr"] else A.loc[Y, "us_bill"]
        y5 = cv[1].par(5)
        res31 = reserve_value(cv[4].df, TAU31)
        res33 = reserve_value(cv[6].df, TAU33)
        base = dict(Y=Y, basis=soy.loc[Y, "basis"], deflator=I6)
        # REC
        o = rec_window(rungs27, r1, rungs28, y5, e[1:], cpi)
        rows.append(dict(base, rival="REC", T33=o["T33"], certain31=o["bottom"], gift=o["gift"],
                         unfunded=o["S"] > 0, shortfall=o["S"], top=o["top"]))
        L, T, G = ladder_step(rungs27, r1, rungs28)
        # R1 all-Treasury
        face = max(G, 0) * (1 + y5) ** 5
        rows.append(dict(base, rival="R1", T33=face, certain31=face, gift=face, unfunded=G < 0,
                         shortfall=max(0, -G), top=face))
        # R3 ladder + 60/40 growth money
        g = np.cumprod(1 + 0.6 * e[1:] + 0.4 * b[1:])
        V31, V33 = max(G, 0) * g[2], max(G, 0) * g[4]
        rows.append(dict(base, rival="R3", T33=V33, certain31=0.0, gift=gift_rule(0.0, V33, V31), unfunded=G < 0,
                         shortfall=max(0, -G), top=V31 / 2))
        # R2 60/40 whole, R4 glide whole
        for rid, w in (("R2", [0.6] * 6), ("R4", GLIDE), ("R4b", GROWTH_FIRST)):
            a = H.DEP1
            a31 = None
            for t in range(6):
                if t == 1:
                    a += H.DEP2
                if t == 4:
                    a31 = a
                a *= 1 + w[t] * e[t] + (1 - w[t]) * b[t]
            T33 = a - res33
            U31 = a31 - res31
            rows.append(dict(base, rival=rid, T33=T33, certain31=0.0, gift=gift_rule(0.0, T33, U31), unfunded=T33 < 0,
                             shortfall=max(0, -T33), top=max(U31, 0) / 2))
        # R5 CPPI m = 3, 5
        for rid, m in (("R5", 3.0), ("R5m5", 5.0)):
            a, a31 = H.DEP1, None
            for t in range(6):
                if t == 1:
                    a += H.DEP2
                if t == 4:
                    a31 = a
                tp, tf = floor_flows_tau(t)
                fl = reserve_value(cv[t].df, tp) + 150_000 * float(cv[t].df(tf))
                c = a - fl
                E = min(a, m * max(c, 0.0))
                S = a - E
                fl_next = reserve_value(cv[t + 1].df, tp - H.yf(date(2027 + t, 1, 1), date(2028 + t, 1, 1))) + \
                    150_000 * float(cv[t + 1].df(max(tf - H.yf(date(2027 + t, 1, 1), date(2028 + t, 1, 1)), 0)))
                a = E * (1 + e[t]) + S * fl_next / fl
            T33 = a - res33
            rows.append(dict(base, rival=rid, T33=T33, certain31=0.0, gift=gift_rule(0.0, T33, a31 - res31),
                             unfunded=T33 < 0, shortfall=max(0, -T33), top=max(a31 - res31, 0) / 2,
                             floor_broken=T33 < 150_000 - 0.5))
        # R6 TIPS ladder: delivery under history's inflation (today's breakevens), Y <= 2011
        if Y <= 2011:
            infl = A.loc[Y:Y + 14, "cpi_infl"].values
            paid = np.array([H.PAY * max(1.0, float(np.prod(1 + infl[:5 + k]))) / (1 + b_k[k - 1]) ** (5 + k)
                             for k in range(1, 11)])
            sh = np.maximum(0, H.PAY - paid)
            rows.append(dict(base, rival="R6", T33=o["T33"], certain31=o["bottom"], gift=o["gift"],
                             unfunded=bool((sh > 0).any()), shortfall=float(sh.sum()), top=o["top"],
                             tips_paid_total=float(paid.sum()), tips_min_payment=float(paid.min())))
    df = pd.DataFrame(rows)
    df["real_T33"] = df.T33 / df.deflator
    df.to_csv(os.path.join(OUT, "rivals_history.csv"), index=False, float_format="%.2f")
    return df


def breakevens(mi):
    """Annual breakeven b(n) at n = 6..15 years: (1 + nominal par) / (1 + TIPS real yield) - 1."""
    tc = H.today_curve()
    rn, rr = [5, 7, 10, 20, 30], [mi[f"DFII{n}"] / 100 for n in (5, 7, 10, 20, 30)]
    out = []
    for n in range(6, 16):
        out.append((1 + tc.par(n)) / (1 + float(np.interp(n, rn, rr))) - 1)
    return np.array(out)


# ================================================================================================= MC lens (JPM)
JPM_ASSETS = {"acwi": "AC World Equity", "uslc": "U.S. Large Cap", "eafe": "EAFE Equity",
              "em": "Emerging Markets Equity", "ussc": "U.S. Small Cap", "value": "U.S. Equity Value Factor",
              "reit": "U.S. REITs", "gold": "Gold", "bond": "U.S. Intermediate Treasuries"}


def jpm_draws(seed=H.SEED, paths=PATHS):
    st = pd.read_csv(os.path.join(H.HIST, "jpm_ltcma_2026_usd.csv")).set_index("asset")
    cr = pd.read_csv(os.path.join(H.HIST, "jpm_ltcma_2026_corr.csv"))
    keys = list(JPM_ASSETS)
    n = len(keys)
    C = np.eye(n)
    for i, a in enumerate(keys):
        for j, b in enumerate(keys):
            if i != j:
                r = cr[((cr.row == JPM_ASSETS[a]) & (cr.col == JPM_ASSETS[b])) |
                       ((cr.row == JPM_ASSETS[b]) & (cr.col == JPM_ASSETS[a]))]["corr"]
                C[i, j] = float(r.iloc[0])
    w, V = np.linalg.eigh(C)
    fixed = w.min() < 1e-8
    if fixed:
        w = np.clip(w, 1e-8, None)
        C = V @ np.diag(w) @ V.T
        d = np.sqrt(np.diag(C))
        C = C / np.outer(d, d)
    L = np.linalg.cholesky(C)
    mu, sd, info = [], [], {}
    for a in keys:
        comp = st.loc[JPM_ASSETS[a], "compound_2026"] / 100
        ar = st.loc[JPM_ASSETS[a], "arithmetic_2026"] / 100
        if a == "bond":            # market-consistent override: today's 5-year par yield
            ar, comp = 0.0506 + (ar - comp), 0.0506
        mu.append(np.log(1 + comp))
        sd.append(np.sqrt(2 * np.log((1 + ar) / (1 + comp))))
        info[a] = dict(compound=comp, arithmetic=ar, log_mu=mu[-1], log_sd=sd[-1])
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal((paths, 6, n)) @ L.T
    R = np.exp(np.array(mu) + Z * np.array(sd)) - 1
    return {k: R[:, :, i] for i, k in enumerate(keys)}, dict(corr_fixed=bool(fixed), min_eig=float(np.linalg.eigvalsh(C).min()),
                                                              assets=info, corr=C.round(3).tolist(), keys=keys)


def mc_lens(R):
    n = H.numbers()
    tc = H.today_curve()
    c27 = n["laura.ladder.cost_2027_strips"]["value"]
    y1, y5_0 = 0.0459, 0.0506
    e, b = R["acwi"], R["bond"]
    P = e.shape[0]
    dy = np.cumsum(-(b - 0.0506) / 5.0, axis=1)                  # dy[:, t] = cumulative change after year t
    dyat = np.c_[np.zeros(P), dy]                                  # dyat[:, t] = change by 1 Jan (2027+t)
    dfd = lambda d0: (lambda tau: tc.df(H.yf(H.D_REF, d0) + tau) / tc.df(H.yf(H.D_REF, d0)))

    def shifted_value(d0, tau, amt, dyv):
        base = dfd(d0)
        v = np.zeros(P)
        for t_, a_ in zip(np.atleast_1d(tau), np.atleast_1d(amt)):
            if t_ <= 0:
                v += a_
            else:
                v += a_ * float(base(t_)) * np.exp(-dyv * t_)
        return v

    res33 = shifted_value(H.A33, TAU33, [H.PAY] * 10, dyat[:, 6])
    res31 = shifted_value(H.A31, TAU31, [H.PAY] * 10, dyat[:, 4])
    out = {}
    L = H.DEP1 - c27
    G = L * (1 + y1) + H.DEP2
    y5 = np.maximum(y5_0 + dyat[:, 1], 0.001)
    Cf = H.FLOOR_FACE / (1 + y5) ** 5
    ok = G >= Cf
    F = np.where(ok, H.FLOOR_FACE, G * (1 + y5) ** 5)
    fund0 = np.where(ok, G - Cf, 0.0)
    ge = np.cumprod(1 + e, axis=1)
    f31, f33 = fund0 * ge[:, 3] / ge[:, 0], fund0 * ge[:, 5] / ge[:, 0]
    out["REC"] = dict(T33=F + f33, certain31=F, gift=F + np.minimum(f33, f31) / 2, unfunded=np.zeros(P, bool))
    face = G * (1 + y5) ** 5
    out["R1"] = dict(T33=face, certain31=face, gift=face, unfunded=np.zeros(P, bool))
    g64 = np.cumprod(1 + 0.6 * e + 0.4 * b, axis=1)
    V31, V33 = G * g64[:, 3] / g64[:, 0], G * g64[:, 5] / g64[:, 0]
    out["R3"] = dict(T33=V33, certain31=np.zeros(P), gift=np.minimum(V33, V31) / 2, unfunded=np.zeros(P, bool))
    for rid, w in (("R2", [0.6] * 6), ("R4", GLIDE), ("R4b", GROWTH_FIRST)):
        a = np.full(P, H.DEP1)
        a31 = None
        for t in range(6):
            if t == 1:
                a = a + H.DEP2
            if t == 4:
                a31 = a.copy()
            a = a * (1 + w[t] * e[:, t] + (1 - w[t]) * b[:, t])
        T33 = a - res33
        U31 = np.maximum(a31 - res31, 0)
        gift = np.where(T33 < 0, 0.0, np.minimum(np.maximum(T33, 0), U31) / 2)
        out[rid] = dict(T33=T33, certain31=np.zeros(P), gift=gift, unfunded=T33 < 0)
    for rid, m in (("R5", 3.0), ("R5m5", 5.0)):
        a = np.full(P, H.DEP1)
        a31 = None
        for t in range(6):
            if t == 1:
                a = a + H.DEP2
            if t == 4:
                a31 = a.copy()
            d0, d1 = date(2027 + t, 1, 1), date(2028 + t, 1, 1)
            tp, tf = floor_flows_tau(t)
            step = H.yf(d0, d1)
            fl = shifted_value(d0, list(tp) + [tf], [H.PAY] * 10 + [150_000], dyat[:, t])
            fl1 = shifted_value(d1, list(tp - step) + [tf - step], [H.PAY] * 10 + [150_000], dyat[:, t + 1])
            c = a - fl
            E = np.minimum(a, m * np.maximum(c, 0))
            a = E * (1 + e[:, t]) + (a - E) * fl1 / fl
        T33 = a - res33
        U31 = np.maximum(a31 - res31, 0)
        gift = np.where(T33 < 0, 0.0, np.minimum(np.maximum(T33, 0), U31) / 2)
        out[rid] = dict(T33=T33, certain31=np.zeros(P), gift=gift, unfunded=T33 < 0, floor_broken=T33 < 150_000 - 0.5)
    h16 = {}
    for dep in (150_000, 75_000, 0):
        a = np.full(P, H.DEP1)
        for t in range(6):
            if t == 1:
                a = a + dep
            a = a * (1 + GROWTH_FIRST[t] * e[:, t] + (1 - GROWTH_FIRST[t]) * b[:, t])
        h16[f"deposit_{dep}"] = float(np.mean(a < res33))
    # REC with the same deposit variants: payments are bought in 2027 and 2028 first
    for dep in (75_000, 0):
        Gd = L * (1 + y1) + dep
        h16[f"REC_deposit_{dep}_unfunded"] = float(np.mean(Gd < 0))
    out["_h16"] = h16
    # R6 TIPS: AR(1) inflation, independent stream
    A = H.load_annual()
    p = A.cpi_infl.loc[1952:2025].values
    X = np.c_[np.ones(len(p) - 1), p[:-1]]
    beta, *_ = np.linalg.lstsq(X, p[1:], rcond=None)
    phi = float(beta[1])
    resid = p[1:] - X @ beta
    s = float(np.sqrt((resid ** 2).sum() / (len(resid) - 2)))
    mi = pd.read_csv(os.path.join(H.HIST, "market_inflation_2026-09.csv")).set_index("series").value
    mu = mi["T10YIE"] / 100
    cpi = pd.read_csv(os.path.join(H.HIST, "raw", "fred_CPIAUCNS.csv"))
    cpi.columns = ["date", "v"]
    cpi = cpi.set_index("date").v.astype(float)
    pi0 = cpi["2026-08-01"] / cpi["2025-08-01"] - 1
    rng = np.random.default_rng(H.SEED + 6)
    pis = np.empty((P, 15))
    prev = np.full(P, pi0)
    for t in range(15):
        prev = mu + phi * (prev - mu) + s * rng.standard_normal(P)
        pis[:, t] = prev
    b_k = breakevens(mi)
    cum = np.cumprod(1 + pis, axis=1)
    paid = np.stack([H.PAY * np.maximum(1.0, cum[:, 4 + k]) / (1 + b_k[k - 1]) ** (5 + k) for k in range(1, 11)], axis=1)
    short = np.maximum(0, H.PAY - paid)
    out["R6"] = dict(T33=out["REC"]["T33"], certain31=out["REC"]["certain31"], gift=out["REC"]["gift"],
                     unfunded=(short > 0).any(axis=1), shortfall=short.sum(axis=1), paid_total=paid.sum(axis=1))
    infl_info = dict(phi=phi, s=s, mu=mu, pi0=float(pi0), breakevens_6_15y=b_k.round(5).tolist(),
                     p_any_short=float((short > 0).any(axis=1).mean()), shortfall_p50=float(np.median(short.sum(axis=1))),
                     shortfall_p95=float(np.percentile(short.sum(axis=1), 95)),
                     paid_total_p5=float(np.percentile(paid.sum(axis=1), 5)),
                     paid_total_p50=float(np.median(paid.sum(axis=1))),
                     paid_total_p95=float(np.percentile(paid.sum(axis=1), 95)))
    # buffer: extra TIPS needed so that 95% of paths deliver every payment in full
    need = (H.PAY / paid).max(axis=1)
    infl_info["tips_scale_for_95pct_full"] = float(np.percentile(need, 95))
    infl_info["tips_extra_cost_for_95pct_full_usd"] = float((np.percentile(need, 95) - 1) * c27)
    return out, infl_info, dict(G=G, fund0_median=float(np.median(fund0)), y5_p5=float(np.percentile(y5, 5)),
                                y5_p95=float(np.percentile(y5, 95)), res33_median=float(np.median(res33)))


# ================================================================================================= summaries
def summarise(hist, mc):
    rows = []
    for rid in RIVALS:
        h = hist[hist.rival == rid]
        m = mc[rid]
        rec = dict(rival=rid, name=NAMES[rid], trades=TRADES[rid])
        if rid != "R6":
            rec.update(h_windows=len(h), h_unfunded=int(h.unfunded.sum()), h_max_shortfall=h.shortfall.max(),
                       h_T33_worst=h.T33.min(), h_T33_worst_Y=int(h.loc[h.T33.idxmin(), "Y"]), h_T33_p10=h.T33.quantile(.1),
                       h_T33_median=h.T33.median(), h_T33_p90=h.T33.quantile(.9), h_realT33_median=h.real_T33.median(),
                       h_realT33_worst=h.real_T33.min(), h_certain31_median=h.certain31.median(),
                       h_gift_worst=h.gift.min(), h_gift_p10=h.gift.quantile(.1), h_gift_median=h.gift.median())
            if rid in ("R5", "R5m5"):
                rec["h_floor_broken"] = int(h.floor_broken.sum())
        else:
            rec.update(h_windows=len(h), h_unfunded=int(h.unfunded.sum()), h_max_shortfall=h.shortfall.max(),
                       h_shortfall_median=h.shortfall.median(), h_min_payment=h.tips_min_payment.min())
        rec.update(mc_unfunded=float(np.mean(m["unfunded"])), mc_T33_p5=float(np.percentile(m["T33"], 5)),
                   mc_T33_p50=float(np.median(m["T33"])), mc_T33_p95=float(np.percentile(m["T33"], 95)),
                   mc_certain31_p50=float(np.median(m["certain31"])), mc_gift_p5=float(np.percentile(m["gift"], 5)),
                   mc_gift_p50=float(np.median(m["gift"])), mc_gift_p95=float(np.percentile(m["gift"], 95)))
        if "floor_broken" in m:
            rec["mc_floor_broken"] = float(np.mean(m["floor_broken"]))
        if "shortfall" in m:
            rec["mc_shortfall_p95"] = float(np.percentile(m["shortfall"], 95))
        rows.append(rec)
    return pd.DataFrame(rows)


# ================================================================================================= fund choice
FUNDS = ["A0", "A1", "A2", "A3", "A4"]
FUND_NAMES = {"A0": "VT (baseline)", "A1": "VTI + VXUS 62/38", "A2": "U.S. only", "A3": "VT + small/value tilt",
              "A4": "VT + gold/REIT"}
MC_W = {"A0": {"acwi": 1.0}, "A1": {"uslc": 0.62, "eafe": 0.285, "em": 0.095}, "A2": {"uslc": 1.0},
        "A3": {"acwi": 0.70, "ussc": 0.15, "value": 0.15}, "A4": {"acwi": 0.80, "gold": 0.10, "reit": 0.10}}


def rec_gift_from_fund(f31, f33, F=150_000.0):
    return F + np.minimum(f33, f31) / 2, F + f33


def fund_choice(R):
    fund0 = H.numbers()["laura.stock_fund_2028_usd.strips"]["value"]
    rows = []
    # MC: bought 1 Jan 2028 (year index 1), buy-and-hold
    for a in FUNDS:
        f31 = sum(w * fund0 * np.prod(1 + R[k][:, 1:4], axis=1) for k, w in MC_W[a].items())
        f33 = sum(w * fund0 * np.prod(1 + R[k][:, 1:6], axis=1) for k, w in MC_W[a].items())
        g, t = rec_gift_from_fund(f31, f33)
        rows.append(dict(fund=a, lens="MC_JPM", gift_p5=np.percentile(g, 5), gift_p10=np.percentile(g, 10),
                         gift_p50=np.median(g), gift_p90=np.percentile(g, 90), gift_p95=np.percentile(g, 95),
                         p_top=float(np.mean(f33 >= f31)), width_p50=float(np.median(f31 / 2)),
                         T33_p5=np.percentile(t, 5), T33_p50=np.median(t), kept_p50=float(np.median(t - g)),
                         fund33_p5=np.percentile(f33, 5)))
    A = H.load_annual()
    hs = {"A0": {"world_eq": 1.0},
          "A1": {"us_mkt_kf": 0.62, "_exus": 0.38},
          "A2": {"us_mkt_kf": 1.0},
          "A3": {"world_eq": 0.70, "us_smallval": 0.30},
          "A4": {"world_eq": 0.80, "gold": 0.10, "housing": 0.10}}
    A["_exus"] = (A.world_eq - 0.62 * A.us_eq) / 0.38
    for lens, (ys, cols) in {"history_1928_2020": (range(1928, 2021), hs),
                             "etf_2011_2020": (range(2011, 2021), {"A0": {"vt_etf": 1.0},
                                                                  "A1": {"vti_etf": 0.62, "vxus_etf": 0.38},
                                                                  "A2": {"vti_etf": 1.0},
                                                                  "A4": {"vt_etf": 0.8, "gld_etf": 0.1, "vnq_etf": 0.1}})}.items():
        for a, wts in cols.items():
            g_, t_, top_ = [], [], []
            for Y in ys:
                f31 = sum(w * fund0 * np.prod(1 + A.loc[Y + 1:Y + 3, c].values) for c, w in wts.items())
                f33 = sum(w * fund0 * np.prod(1 + A.loc[Y + 1:Y + 5, c].values) for c, w in wts.items())
                g, t = rec_gift_from_fund(f31, f33)
                g_.append(g)
                t_.append(t)
                top_.append(f33 >= f31)
            g_ = np.array(g_)
            rows.append(dict(fund=a, lens=lens, windows=len(g_), gift_worst=g_.min(), gift_p5=np.percentile(g_, 5),
                             gift_p10=np.percentile(g_, 10), gift_p50=np.median(g_), gift_p90=np.percentile(g_, 90),
                             gift_p95=np.percentile(g_, 95), p_top=float(np.mean(top_)), T33_p50=np.median(t_)))
    df = pd.DataFrame(rows)
    df["name"] = df.fund.map(FUND_NAMES)
    df.to_csv(os.path.join(OUT, "fund_alternatives.csv"), index=False, float_format="%.2f")
    # pre-registered rule (M6_SPEC s5)
    mc = df[df.lens == "MC_JPM"].set_index("fund")
    hh = df[df.lens == "history_1928_2020"].set_index("fund")
    sp90 = lambda r: r.gift_p95 - r.gift_p5
    sp80 = lambda r: r.gift_p90 - r.gift_p10
    sentence = {"A1": "Same stocks as VT in two funds: one more trade and one more thing to explain, no new risk "
                      "spread (fails the one-sentence test for a benefit).",
                "A2": "Puts every stock dollar in one country; a judge would ask why Laura bets on the U.S. alone.",
                "A3": "Tilts to small and cheap companies, which have sometimes paid more but can lag for a decade.",
                "A4": "Adds gold and property, which do not always fall with stocks.",
                "A0": "One fund that owns the world's stock market, left alone."}
    dec = []
    b0m, b0h = mc.loc["A0"], hh.loc["A0"]
    for a in FUNDS[1:]:
        m, h = mc.loc[a], hh.loc[a]
        c1a = m.gift_p5 >= b0m.gift_p5 + 2000
        c1b = sp90(m) <= 0.90 * sp90(b0m)
        c2 = (c1a and h.gift_p10 >= b0h.gift_p10 + 1000) or (c1b and sp80(h) <= 0.95 * sp80(b0h))
        c3 = (m.gift_p50 >= b0m.gift_p50 - 500) and (h.gift_p50 >= b0h.gift_p50 - 1000)
        switch = bool((c1a or c1b) and c2 and c3)
        dec.append(dict(fund=a, name=FUND_NAMES[a], mc_p5_change=m.gift_p5 - b0m.gift_p5,
                        mc_spread90_ratio=sp90(m) / sp90(b0m), mc_median_change=m.gift_p50 - b0m.gift_p50,
                        hist_p10_change=h.gift_p10 - b0h.gift_p10, hist_spread80_ratio=sp80(h) / sp80(b0h),
                        hist_median_change=h.gift_p50 - b0h.gift_p50, test1_p5=bool(c1a), test1_spread=bool(c1b),
                        test2_history=bool(c2), test3_median=bool(c3), passes_numbers=switch,
                        one_sentence=sentence[a], decision="SWITCH (if the sentence and WInS check pass)" if switch
                        else "KEEP VT"))
    D = pd.DataFrame(dec)
    D.to_csv(os.path.join(OUT, "fund_choice_decision.csv"), index=False, float_format="%.4f")
    return df, D


def fund_robustness(n_seeds=20):
    """Not part of the pre-registered rule: how fragile is its output? (a) MC tests on other seeds; (b) history tests
    with the proxies that flatter a gold/REIT mix removed: gold's floating era only (1971-2020 starts) and the REIT half
    replaced by VT (the history 'REIT' is a home-price index)."""
    fund0 = H.numbers()["laura.stock_fund_2028_usd.strips"]["value"]
    tally = {a: dict(c1a=0, c1b=0, c3=0) for a in FUNDS[1:]}
    ratios = {a: [] for a in FUNDS[1:]}
    for i in range(n_seeds):
        R, _ = jpm_draws(seed=H.SEED + 1000 + i)
        st = {}
        for a in FUNDS:
            f31 = sum(w * fund0 * np.prod(1 + R[k][:, 1:4], axis=1) for k, w in MC_W[a].items())
            f33 = sum(w * fund0 * np.prod(1 + R[k][:, 1:6], axis=1) for k, w in MC_W[a].items())
            g, _ = rec_gift_from_fund(f31, f33)
            st[a] = (np.percentile(g, 5), np.median(g), np.percentile(g, 95))
        for a in FUNDS[1:]:
            p5, p50, p95 = st[a]
            b5, b50, b95 = st["A0"]
            tally[a]["c1a"] += p5 >= b5 + 2000
            tally[a]["c1b"] += (p95 - p5) <= 0.90 * (b95 - b5)
            tally[a]["c3"] += p50 >= b50 - 500
            ratios[a].append((p95 - p5) / (b95 - b5))
    A = H.load_annual()
    out = {"seeds": n_seeds, "mc": {a: dict(tally[a], spread_ratio_min=float(min(ratios[a])),
                                              spread_ratio_max=float(max(ratios[a])))
                                     for a in FUNDS[1:]}}
    variants = {"gold_float_era_1971_2020": (range(1971, 2021), {"world_eq": 0.80, "gold": 0.10, "housing": 0.10}),
                "reit_half_as_VT_1928_2020": (range(1928, 2021), {"world_eq": 0.90, "gold": 0.10}),
                "both_1971_2020": (range(1971, 2021), {"world_eq": 0.90, "gold": 0.10})}
    for lab, (ys, wts) in variants.items():
        gs, g0 = [], []
        for Y in ys:
            f31 = sum(w * fund0 * np.prod(1 + A.loc[Y + 1:Y + 3, c].values) for c, w in wts.items())
            f33 = sum(w * fund0 * np.prod(1 + A.loc[Y + 1:Y + 5, c].values) for c, w in wts.items())
            gs.append(rec_gift_from_fund(f31, f33)[0])
            b31 = fund0 * np.prod(1 + A.loc[Y + 1:Y + 3, "world_eq"].values)
            b33 = fund0 * np.prod(1 + A.loc[Y + 1:Y + 5, "world_eq"].values)
            g0.append(rec_gift_from_fund(b31, b33)[0])
        gs, g0 = np.array(gs), np.array(g0)
        out[lab] = dict(windows=len(gs), p10_change=float(np.percentile(gs, 10) - np.percentile(g0, 10)),
                        spread80_ratio=float((np.percentile(gs, 90) - np.percentile(gs, 10)) /
                                             (np.percentile(g0, 90) - np.percentile(g0, 10))),
                        median_change=float(np.median(gs) - np.median(g0)))
    return out


# ================================================================================================= figures
def fig_rivals(S):
    plt = H.plot_style()
    order = ["REC", "R1", "R3", "R2", "R4", "R4b", "R5", "R5m5"]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=True)
    Si = S.set_index("rival")
    for ax, lens in zip(axes, ("mc", "h")):
        for i, rid in enumerate(order):
            r = Si.loc[rid]
            if lens == "mc":
                lo, mid, hi, cert = r.mc_T33_p5, r.mc_T33_p50, r.mc_T33_p95, r.mc_certain31_p50
                unf = r.mc_unfunded
                lab = "never short" if unf == 0 else (f"{unf:.2%} short" if unf < 0.001 else f"{unf:.1%} short")
            else:
                lo, mid, hi, cert = r.h_T33_p10, r.h_T33_median, r.h_T33_p90, r.h_certain31_median
                lab = f"{int(r.h_unfunded)}/{int(r.h_windows)} short" if r.h_unfunded else "never short"
            col = H.OI["blue"] if rid == "REC" else H.OI["grey"]
            ax.plot([lo / 1000, hi / 1000], [i, i], color=col, lw=2.4, solid_capstyle="round")
            ax.plot(mid / 1000, i, "o", color=H.OI["orange"] if rid == "REC" else "#333333", ms=6,
                    label=("middle outcome" if i == 1 else None))
            if cert > 0:
                ax.plot(cert / 1000, i - 0.28, marker="D", color=H.OI["green"], ms=5, ls="none",
                        label=("certain by 2031 (can be promised)" if rid == "REC" else None))
            ax.text(max(hi / 1000, 0) + 8, i, lab, va="center", fontsize=7.5,
                    color=H.OI["vermillion"] if "never" not in lab else "#444444")
        ax.axvline(0, color="#777777", lw=0.8)
        ax.set_title("Monte Carlo, JPM 2026 assumptions (bar: 5th-95th percentile)" if lens == "mc" else
                     "History 1872-2020, each era's yields and returns (bar: 10th-90th)", fontsize=9.3)
    axes[0].set_yticks(range(len(order)))
    axes[0].set_yticklabels([NAMES[r] for r in order])
    axes[0].invert_yaxis()
    hs, ls = axes[0].get_legend_handles_labels()
    fig.legend(hs, ls, loc="lower center", ncol=2, fontsize=7.8, bbox_to_anchor=(0.5, 0.0))
    for ax in axes:
        ax.set_xlabel("2033 money for facility + flexibility, after the payments ($k)", fontsize=8.5)
    fig.suptitle("Rivals on the same metrics (MODEL). Every plan gets $300,000 in 2027 and $150,000 in 2028", fontsize=11)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_m6_rivals.png"))
    plt.close(fig)


def fig_funds(F):
    plt = H.plot_style()
    fig, ax = plt.subplots(figsize=(8.5, 3.6))
    cols = {"MC_JPM": H.OI["blue"], "history_1928_2020": H.OI["orange"], "etf_2011_2020": H.OI["green"]}
    labs = {"MC_JPM": "Monte Carlo, JPM (p5-p50-p95)", "history_1928_2020": "History 1928-2020 (p10-median-p90)",
            "etf_2011_2020": "Actual ETFs, 5-year windows 2012-2025 (p10-median-p90)"}
    off = {"MC_JPM": -0.22, "history_1928_2020": 0.0, "etf_2011_2020": 0.22}
    for lens, g in F.groupby("lens"):
        for r in g.itertuples():
            i = FUNDS.index(r.fund)
            lo, hi = (r.gift_p5, r.gift_p95) if lens == "MC_JPM" else (r.gift_p10, r.gift_p90)
            ax.plot([lo / 1000, hi / 1000], [i + off[lens]] * 2, color=cols[lens], lw=2)
            ax.plot(r.gift_p50 / 1000, i + off[lens], "o", color=cols[lens], ms=4.5,
                    label=labs[lens] if r.fund == "A0" else None)
    ax.set_yticks(range(len(FUNDS)))
    ax.set_yticklabels([FUND_NAMES[f] for f in FUNDS])
    ax.invert_yaxis()
    ax.set_xlabel("2033 facility gift ($k): floor + half the stock fund, capped")
    ax.set_title("Branch fund choice: the gift barely moves because the fund is only ~9% of Laura's money (MODEL)",
                 fontsize=9.5)
    ax.legend(fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_m6_fund_choice.png"))
    plt.close(fig)


def main():
    os.makedirs(OUT, exist_ok=True)
    H.self_test()
    say("[M6] Rivals on the same metrics (MODEL). History lens: 149 start years 1872-2020. MC lens: JPM 2026 LTCMA, "
        f"{PATHS:,} paths, seed {H.SEED}.")
    hist = history_lens()
    R, mcinfo = jpm_draws()
    say(f"    JPM correlation matrix (9 assets) needed a positive-definite fix: {mcinfo['corr_fixed']} "
        f"(min eigenvalue after {mcinfo['min_eig']:.2e})")
    mc, infl, recinfo = mc_lens(R)
    h16 = mc.pop("_h16")
    say(f"    re-verify insight_v1 H16 (growth-first 75->40 misses a payment; was 3.2% / 13.7% / 40.8%): on this basis "
        f"{h16['deposit_150000']:.1%} / {h16['deposit_75000']:.1%} / {h16['deposit_0']:.1%} with a 2028 deposit of "
        f"$150k / $75k / $0 (REC: {h16['REC_deposit_75000_unfunded']:.0%} / {h16['REC_deposit_0_unfunded']:.0%}, its ladder is bought"
        f" from the first deposit)")
    S = summarise(hist, mc)
    S.to_csv(os.path.join(OUT, "rivals_summary.csv"), index=False, float_format="%.2f")
    for r in S.itertuples():
        if r.rival != "R6":
            say(f"  {r.name:30s}| MC: short {r.mc_unfunded:6.2%}; 2033 money p5/p50/p95 {H.kusd(r.mc_T33_p5)} / "
                f"{H.kusd(r.mc_T33_p50)} / {H.kusd(r.mc_T33_p95)}; certain in 2031 {H.kusd(r.mc_certain31_p50)}; gift "
                f"p5/p50 ${r.mc_gift_p5 / 1000:,.1f}k / ${r.mc_gift_p50 / 1000:,.1f}k"
                + (f"; $150k floor broken {r.mc_floor_broken:.2%}" if r.rival in ("R5", "R5m5") else ""))
            say(f"  {'':30s}| history: short in {int(r.h_unfunded)}/{int(r.h_windows)} (max {H.kusd(r.h_max_shortfall)}); 2033 "
                f"money worst {H.kusd(r.h_T33_worst)} ({int(r.h_T33_worst_Y)}) p10 {H.kusd(r.h_T33_p10)} median "
                f"{H.kusd(r.h_T33_median)}; real median {H.kusd(r.h_realT33_median)}; gift median {H.kusd(r.h_gift_median)}"
                + (f"; $150k floor broken in {int(r.h_floor_broken)}" if r.rival in ("R5", "R5m5") else "") + f"; trades {r.trades}")
        else:
            say(f"  {r.name:30s}| MC: at least one payment short in {r.mc_unfunded:.1%} of paths (p95 total shortfall "
                f"{H.kusd(r.mc_shortfall_p95)}); history (today's breakevens, {int(r.h_windows)} inflation paths 1872-2011): "
                f"short in {int(r.h_unfunded)}, largest total shortfall {H.kusd(r.h_max_shortfall)}, smallest payment "
                f"{H.kusd(r.h_min_payment)}")
    say(f"    TIPS: AR(1) phi {infl['phi']:.3f}, shock sd {infl['s']:.4f}, mean {infl['mu']:.4f}, start {infl['pi0']:.4f}; "
        f"to deliver every payment in 95% of paths the TIPS ladder must be {infl['tips_scale_for_95pct_full']:.2f}x as "
        f"big (about {H.kusd(infl['tips_extra_cost_for_95pct_full_usd'])} more)")
    F, D = fund_choice(R)
    say("\n[M6-B] Branch fund alternatives (REC, fund0 $40,736, bought 1 Jan 2028, buy and hold)")
    for r in F.itertuples():
        say(f"  {r.lens:18s} {r.name:24s}: gift p5 {H.kusd(r.gift_p5)} p10 {H.kusd(r.gift_p10)} median {H.kusd(r.gift_p50)} "
            f"p90 {H.kusd(r.gift_p90)} p95 {H.kusd(r.gift_p95)}; top reached {r.p_top:.0%}")
    for r in D.itertuples():
        say(f"  RULE {r.name:24s}: MC p5 {r.mc_p5_change:+,.0f}, spread x{r.mc_spread90_ratio:.2f}, median "
            f"{r.mc_median_change:+,.0f}; history p10 {r.hist_p10_change:+,.0f}, spread x{r.hist_spread80_ratio:.2f}, "
            f"median {r.hist_median_change:+,.0f} -> {r.decision}")
    rob = fund_robustness()
    for a, v in rob["mc"].items():
        say(f"  ROBUSTNESS {FUND_NAMES[a]:24s}: MC tests on {rob['seeds']} other seeds: p5 test passed {v['c1a']}, spread "
            f"test passed {v['c1b']} (spread ratio {v['spread_ratio_min']:.3f}-{v['spread_ratio_max']:.3f}), median test "
            f"passed {v['c3']}")
    for lab in ("gold_float_era_1971_2020", "reit_half_as_VT_1928_2020", "both_1971_2020"):
        v = rob[lab]
        say(f"  ROBUSTNESS gold/REIT history, {lab} ({v['windows']} windows): p10 {v['p10_change']:+,.0f}, spread "
            f"x{v['spread80_ratio']:.2f}, median {v['median_change']:+,.0f}")
    fig_rivals(S)
    fig_funds(F)
    res = dict(summary=S.to_dict("records"), h16_reverified=h16, tips=infl, rec_mc=recinfo, jpm=mcinfo, fund_alternatives=F.to_dict("records"),
               fund_decision=D.to_dict("records"), fund_robustness=rob, seed=H.SEED, paths=PATHS, spec="rab/models/M6_SPEC.md")
    with open(os.path.join(OUT, "M6_results.json"), "w") as f:
        json.dump(res, f, indent=1, default=lambda x: x.item() if hasattr(x, "item") else str(x))
    with open(os.path.join(OUT, "M6_report.txt"), "w") as f:
        f.write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
