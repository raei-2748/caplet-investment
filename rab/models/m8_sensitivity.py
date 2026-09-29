"""M8: which assumptions move the 2031 range most (tornado + Sobol). Spec: rab/models/M8_SPEC.md.

WS2, RAB Kit, 2026-09-30 (Sydney). AI-generated research (Claude Code) for Team Caplet; no deliverable text.
Every output is a MODEL property, not a forecast. Market luck is kept apart from assumptions.

Run from the worktree root after m3_branch.py (about 3 minutes; no network):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m8_sensitivity.py
Writes rab/results/M8/.
"""
import os
import sys
from datetime import date

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m1_ladder as M1  # noqa: E402  (WS1's Gate A pricer: the D1 curve method)
import ws2_common as C  # noqa: E402

OUT = os.path.join(C.RESULTS, "M8")
LOG = []
S = 0.5
PHI_LOW = 0.9755                  # M4_SPEC section 2: phi when income earns 0%
N_TORNADO = C.N_PATHS
N_LUCK_B = 4_000
D_GRID = np.arange(-250.0, 250.01, 1.0)


def say(s=""):
    print(s)
    LOG.append(s)


# ------------------------------------------------------------------ inputs
def fred_changes(series, days):
    d = pd.read_csv(os.path.join(C.ROOT, "rab/data/fred", f"{series}.csv"))
    d.columns = ["date", "v"]
    d["date"] = pd.to_datetime(d["date"])
    d["v"] = pd.to_numeric(d["v"], errors="coerce")
    x = d.dropna().set_index("date")["v"]
    x = x[x.index >= "1990-01-02"]
    tgt = x.index + pd.Timedelta(days=days)
    end = x.reindex(x.index.union(tgt)).sort_index().ffill().reindex(tgt).to_numpy()
    return np.sort((end - x.to_numpy())[tgt <= x.index[-1]])


def ladder_grid():
    rows = M1.load_rows([os.path.join(C.ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
    row = next(r for r in rows if r["_date"] == date(2026, 9, 28))
    V_A, V_28, LV = [], [], []
    for d in D_GRID:
        cv = M1.Curve(row, d)
        v0 = sum(M1.PAY * cv.df(t) for t in M1.pay_dates("nov15"))
        V_A.append(v0 / cv.df(M1.A27))
        V_28.append(v0 / cv.df(M1.A28))
        LV.append([v0 / cv.df(date(y, 1, 1)) for y in range(2028, 2033)])
    return np.array(V_A), np.array(V_28), np.array(LV)


class Engine:
    def __init__(self, inp):
        self.inp = inp
        self.VA, self.V28, self.LV = ladder_grid()
        self.d_emp = fred_changes("DGS10", 95) * 100      # basis points
        self.e_emp = fred_changes("DGS5", 365)            # points
        i0 = int(np.where(D_GRID == 0)[0][0])
        assert abs(self.VA[i0] - inp["V_A"]) < 0.01, (self.VA[i0], inp["V_A"])

    def q(self, emp, u):
        return np.percentile(emp, np.clip(u, 0, 1) * 100)

    def start(self, d, e):
        """Floor face F and stock fund B0 on 2 Jan 2028 (M8_SPEC section 1, IPS 'whole remainder' reading)."""
        VA = np.interp(d, D_GRID, self.VA)
        V28 = np.interp(d, D_GRID, self.V28)
        y1 = 0.0459 + d / 1e4
        y5 = np.maximum(0.001, 0.0506 + d / 1e4 + e / 100)
        gap = VA > 300_000
        left = np.maximum(0.0, 300_000 - VA)
        T = np.maximum(0.0, VA - 300_000) * V28 / VA
        R = np.maximum(0.0, 150_000 - T)
        F = np.where(gap, R, 150_000.0)
        B0 = np.where(gap, R - R / (1 + y5) ** 5, left * (1 + y1) + 150_000 - 150_000 / (1 + y5) ** 5)
        return F, B0, y5

    def run(self, mu_c, sd_log, inv_nu, d, e, fee, phi, z, s=S):
        """z: standardised shocks, shape (..., 5) broadcastable against the assumption arrays (shape (...))."""
        F, B0, y5 = self.start(d, e)
        fc = F / (1 + y5) ** 5
        lv = np.stack([np.interp(d, D_GRID, self.LV[:, k]) for k in range(5)], axis=-1)
        mu = np.log1p(mu_c)
        B = B0 * np.ones(np.broadcast(np.asarray(mu), z[..., 0]).shape)
        out = {}
        for k in range(5):
            fv = fc * (1 + y5) ** k
            B = np.maximum(B - fee * (lv[..., k] + fv + B), 0.0) * np.exp(mu + sd_log * z[..., k])
            if k == 2:
                out["B3"] = B.copy()
        out["B5"] = B
        out["F"] = F * np.ones_like(B)
        out["U"] = F + s * out["B3"]
        out["G"] = np.minimum(phi * F + s * np.minimum(out["B5"], out["B3"]), out["U"])
        return out


def zq(u, inv_nu):
    """Standardised quantile: normal if inv_nu == 0, else Student-t with nu = 1/inv_nu scaled to unit sd; clip +-5."""
    u = np.clip(u, 1e-12, 1 - 1e-12)
    inv_nu = np.asarray(inv_nu, float)
    zn = stats.norm.ppf(u)
    nu = np.where(inv_nu > 0, 1 / np.maximum(inv_nu, 1e-12), 1e6)
    zt = stats.t.ppf(u, nu) * np.sqrt((nu - 2) / nu)
    return np.clip(np.where(inv_nu > 0, zt, zn), -5, 5)


BASE = {"mu_c": 0.07, "sd_log": C.SIG_L, "inv_nu": 0.0, "d": 0.0, "e": 0.0, "fee": 0.0, "phi": 1.0}
NAMES = {"mu_c": "Stock fund's expected return", "sd_log": "Stock fund's volatility", "inv_nu": "Fat tails",
         "d": "Yield move before the Jan 2027 purchase", "e": "5-year yield move during 2027 (floor price)",
         "fee": "Yearly costs paid from the stock fund", "phi": "What the floor fund pays (reinvestment)"}


def main():
    os.makedirs(OUT, exist_ok=True)
    inp = C.inputs()
    say(f"M8 sensitivity | run {C.stamp()} | numbers.yaml {inp['numbers_sha'][:12]}")
    E = Engine(inp)
    F0, B00, _ = E.start(np.array(0.0), np.array(0.0))
    say(f"  checks: V_A(0) = ${np.interp(0, D_GRID, E.VA):,.2f} (numbers.yaml ${inp['V_A']:,.2f}); B0(0,0) = "
        f"${float(B00):,.2f} (numbers.yaml B0 ${inp['B0']:,.2f})")
    assert abs(float(B00) - inp["B0"]) < 0.01
    lo_d, hi_d = np.percentile(E.d_emp, [2.5, 97.5])
    lo_e, hi_e = np.percentile(E.e_emp, [2.5, 97.5])
    rng_ = {"mu_c": (0.0408, 0.0800), "sd_log": (0.12, 0.20), "inv_nu": (0.0, 1 / 3), "d": (lo_d, hi_d),
            "e": (lo_e, hi_e), "fee": (0.0, 0.010), "phi": (PHI_LOW, 1.0)}
    pd.DataFrame([{"input": k, "label": NAMES[k], "base": BASE[k], "low": v[0], "high": v[1],
                   "n_hist": len(E.d_emp) if k == "d" else (len(E.e_emp) if k == "e" else None)}
                  for k, v in rng_.items()]).to_csv(os.path.join(OUT, "input_ranges.csv"), index=False)
    say(f"  historical ranges (2.5-97.5%, since 1990): 95-day 10-year change {lo_d:.0f} to {hi_d:.0f} bp "
        f"(n={len(E.d_emp)}); 1-year 5-year change {lo_e:.2f} to {hi_e:.2f} points (n={len(E.e_emp)})")

    # ---------------------------------------------------------------- tornado
    u = C.rng("M8-luck").random((N_TORNADO, 5))
    z_norm = zq(u, 0.0)

    def stats_for(p, s=S):
        z = z_norm if p["inv_nu"] == 0 else zq(u, p["inv_nu"])
        o = E.run(p["mu_c"], p["sd_log"], p["inv_nu"], np.array(p["d"]), np.array(p["e"]), p["fee"], p["phi"], z, s)
        return {"top_p50": np.median(o["U"]), "top_p5": np.percentile(o["U"], 5), "gift_p50": np.median(o["G"]),
                "bottom": float(np.median(o["F"]))}

    base = stats_for(BASE)
    tor = []
    for kname, (lo, hi) in rng_.items():
        r_lo = stats_for({**BASE, kname: lo})
        r_hi = stats_for({**BASE, kname: hi})
        tor.append({"input": kname, "label": NAMES[kname], "kind": "assumption", "low": lo, "high": hi,
                    **{f"{m}_at_low": r_lo[m] for m in r_lo}, **{f"{m}_at_high": r_hi[m] for m in r_hi},
                    "swing_top_p50": abs(r_hi["top_p50"] - r_lo["top_p50"]),
                    "swing_top_p5": abs(r_hi["top_p5"] - r_lo["top_p5"]),
                    "swing_gift_p50": abs(r_hi["gift_p50"] - r_lo["gift_p50"])})
    r13, r23 = stats_for(BASE, 1 / 3), stats_for(BASE, 2 / 3)
    tor.append({"input": "s", "label": "Decision: share promised 1/3 vs 2/3 (not an assumption)", "kind": "decision",
                "low": 1 / 3, "high": 2 / 3, **{f"{m}_at_low": r13[m] for m in r13}, **{f"{m}_at_high": r23[m] for m in r23},
                "swing_top_p50": abs(r23["top_p50"] - r13["top_p50"]), "swing_top_p5": abs(r23["top_p5"] - r13["top_p5"]),
                "swing_gift_p50": abs(r23["gift_p50"] - r13["gift_p50"])})
    m3 = pd.read_csv(os.path.join(C.RESULTS, "M3", "summary.csv")).set_index("model").loc[["L", "T", "BOOT", "BAYES"]]
    tor.append({"input": "model", "label": "Return model: L / T / BOOT / BAYES (M3; not an assumption)",
                "kind": "model", "low": np.nan, "high": np.nan, "top_p50_at_low": m3.U_p50.min(),
                "top_p50_at_high": m3.U_p50.max(), "top_p5_at_low": m3.U_p5.min(), "top_p5_at_high": m3.U_p5.max(),
                "gift_p50_at_low": m3.G_p50.min(), "gift_p50_at_high": m3.G_p50.max(),
                "swing_top_p50": m3.U_p50.max() - m3.U_p50.min(), "swing_top_p5": m3.U_p5.max() - m3.U_p5.min(),
                "swing_gift_p50": m3.G_p50.max() - m3.G_p50.min()})
    dt = pd.DataFrame(tor).sort_values("swing_top_p50", ascending=False)
    dt.to_csv(os.path.join(OUT, "tornado.csv"), index=False)
    say(f"  base: bottom ${base['bottom']:,.0f}, median top ${base['top_p50']:,.0f}, p5 top ${base['top_p5']:,.0f}, "
        f"median gift ${base['gift_p50']:,.0f}")
    for _, r in dt.iterrows():
        say(f"  tornado {r['label'][:58]:58s} median top ${r['top_p50_at_low']:,.0f} .. ${r['top_p50_at_high']:,.0f} "
            f"(swing ${r['swing_top_p50']:,.0f}); p5 top swing ${r['swing_top_p5']:,.0f}; gift swing "
            f"${r['swing_gift_p50']:,.0f}")

    # ---------------------------------------------------------------- Sobol A (luck included)
    from SALib.analyze import sobol as sa
    from SALib.sample import sobol as ss

    def to_inputs(X, names):
        p = dict(BASE)
        for i, nm in enumerate(names):
            if nm in ("d", "e"):
                p[nm] = E.q(E.d_emp if nm == "d" else E.e_emp, X[:, i])
            elif nm.startswith("u"):
                continue
            else:
                p[nm] = X[:, i]
        return p

    sob = {}
    for yname, names in (("top2031", ["mu_c", "sd_log", "inv_nu", "d", "e", "fee", "u1", "u2", "u3"]),
                         ("gift2033", ["mu_c", "sd_log", "inv_nu", "d", "e", "fee", "phi", "u1", "u2", "u3", "u4",
                                       "u5"])):
        bounds = [[rng_[n][0], rng_[n][1]] if n in ("mu_c", "sd_log", "inv_nu", "fee", "phi") else [0, 1]
                  for n in names]
        prob = {"num_vars": len(names), "names": names, "bounds": bounds}
        X = ss.sample(prob, 2 ** 14, calc_second_order=False, seed=C.SEED)
        p = to_inputs(X, names)
        uu = np.full((len(X), 5), 0.5)
        for i, nm in enumerate(names):
            if nm.startswith("u"):
                uu[:, int(nm[1]) - 1] = X[:, i]
        z = zq(uu, p["inv_nu"][:, None] if np.ndim(p["inv_nu"]) else p["inv_nu"])
        o = E.run(p["mu_c"], p["sd_log"], p["inv_nu"], np.asarray(p["d"], float), np.asarray(p["e"], float),
                  p["fee"], p["phi"], z)
        Y = o["U"] if yname == "top2031" else o["G"]
        Si = sa.analyze(prob, Y, calc_second_order=False, conf_level=0.95, seed=C.SEED)
        df = pd.DataFrame({"input": names, "label": [NAMES.get(n, f"market luck {2027 + int(n[1])}" if n.startswith("u")
                                                              else n) for n in names],
                           "S1": Si["S1"], "S1_conf": Si["S1_conf"], "ST": Si["ST"], "ST_conf": Si["ST_conf"]})
        df = df.sort_values("ST", ascending=False)
        df.to_csv(os.path.join(OUT, f"sobol_A_{yname}.csv"), index=False)
        luck = df[df.input.str.startswith("u")].ST.sum()
        say(f"  Sobol A {yname}: total-order luck (sum of ST over years) {luck:.2f}; assumptions: " +
            "; ".join(f"{r.input} ST {r.ST:.3f}" for r in df.itertuples() if not r.input.startswith("u")))
        sob[yname] = df

    # ---------------------------------------------------------------- Sobol B (assumptions only)
    names = ["mu_c", "sd_log", "inv_nu", "d", "e", "fee"]
    prob = {"num_vars": 6, "names": names, "bounds": [[0, 1] if n in ("d", "e") else list(rng_[n]) for n in names]}
    X = ss.sample(prob, 2 ** 12, calc_second_order=False, seed=C.SEED)
    uB = C.rng("M8-sobol").random((N_LUCK_B, 5))
    nu_grid = np.linspace(0, 1 / 3, 121)
    zg = np.stack([zq(uB, v) for v in nu_grid])
    ymed, yp5 = np.empty(len(X)), np.empty(len(X))
    p = to_inputs(X, names)
    for a in range(0, len(X), 512):
        b = min(a + 512, len(X))
        iv = p["inv_nu"][a:b]
        pos = np.clip(iv / (1 / 3) * (len(nu_grid) - 1), 0, len(nu_grid) - 1 - 1e-9)
        i0 = np.floor(pos).astype(int)
        w = (pos - i0)[:, None, None]
        z = zg[i0] * (1 - w) + zg[i0 + 1] * w
        o = E.run(p["mu_c"][a:b, None], p["sd_log"][a:b, None], iv[:, None], np.asarray(p["d"][a:b])[:, None],
                  np.asarray(p["e"][a:b])[:, None], p["fee"][a:b, None], 1.0, z)
        ymed[a:b] = np.median(o["U"], axis=1)
        yp5[a:b] = np.percentile(o["U"], 5, axis=1)
    rowsB = []
    for yname, Y in (("median_top2031", ymed), ("p5_top2031", yp5)):
        Si = sa.analyze(prob, Y, calc_second_order=False, conf_level=0.95, seed=C.SEED)
        for i, n in enumerate(names):
            rowsB.append({"output": yname, "input": n, "label": NAMES[n], "S1": Si["S1"][i], "S1_conf": Si["S1_conf"][i],
                          "ST": Si["ST"][i], "ST_conf": Si["ST_conf"][i]})
    dB = pd.DataFrame(rowsB)
    dB.to_csv(os.path.join(OUT, "sobol_B.csv"), index=False)
    for yname in ("median_top2031", "p5_top2031"):
        z = dB[dB.output == yname].sort_values("ST", ascending=False)
        say(f"  Sobol B {yname}: " + "; ".join(f"{r.input} ST {r.ST:.3f} (+-{r.ST_conf:.3f})" for r in z.itertuples()))
    top3 = dB[dB.output == "median_top2031"].sort_values("ST", ascending=False).head(3)
    top3p5 = dB[dB.output == "p5_top2031"].sort_values("ST", ascending=False).head(3)
    tor_rank = [r for r in dt[dt.kind == "assumption"].input][:3]
    say(f"  MUST STATE (Sobol B, median top): {', '.join(top3.input)} | p5 ranking: {', '.join(top3p5.input)} | "
        f"tornado: {', '.join(tor_rank)}")
    pd.DataFrame({"rank": [1, 2, 3], "input": list(top3.input), "label": list(top3.label),
                  "ST_median_top": list(top3.ST), "in_p5_top3": [x in set(top3p5.input) for x in top3.input],
                  "in_tornado_top3": [x in set(tor_rank) for x in top3.input]}).to_csv(
        os.path.join(OUT, "must_state.csv"), index=False)

    # ---------------------------------------------------------------- floor reading (F4)
    fr = []
    for dbp in (0.0, -50.0, -100.0):
        F, B0, y5 = E.start(np.array(dbp), np.array(0.0))
        VA = float(np.interp(dbp, D_GRID, E.VA))
        V28 = float(np.interp(dbp, D_GRID, E.V28))
        T = max(0.0, VA - 300_000) * V28 / VA
        left = max(0.0, 300_000 - VA)
        y1 = 0.0459 + dbp / 1e4
        B0_e6 = left * (1 + y1) + 150_000 - T - 150_000 / (1 + float(y5)) ** 5
        F_e6 = 150_000.0 if B0_e6 >= 0 else (150_000 - T) * 1.0
        fr.append({"d_bp": dbp, "ladder_2027": VA, "top_up_2028": T, "IPS_floor": float(F), "IPS_fund": float(B0),
                   "E6_floor": F_e6, "E6_fund": max(B0_e6, 0.0)})
    pd.DataFrame(fr).to_csv(os.path.join(OUT, "floor_reading.csv"), index=False)
    for r in fr:
        say(f"  floor reading d={r['d_bp']:+.0f}bp: ladder ${r['ladder_2027']:,.0f}, top-up ${r['top_up_2028']:,.0f}; "
            f"IPS 'whole remainder' floor ${r['IPS_floor']:,.0f} + fund ${r['IPS_fund']:,.0f}; E6 floor "
            f"${r['E6_floor']:,.0f} + fund ${r['E6_fund']:,.0f}")

    figures(dt, sob, dB, base)
    open(os.path.join(OUT, "run_log.txt"), "w").write("\n".join(LOG) + "\n")


def figures(dt, sob, dB, base):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    C.style(plt)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
    d = dt.iloc[::-1]
    for ax, col, ttl in ((axes[0], "top_p50", "Median top of the 2031 range"),
                         (axes[1], "top_p5", "Bad-case (5th percentile) top")):
        b = base[col] / 1e3
        for i, (_, r) in enumerate(d.iterrows()):
            lo, hi = r[f"{col}_at_low"] / 1e3, r[f"{col}_at_high"] / 1e3
            colr = C.COL["T"] if r["kind"] == "assumption" else C.INK2
            left, right = min(lo, hi), max(lo, hi)
            ax.barh(i, right - left, left=left, color=colr, alpha=1.0 if r["kind"] == "assumption" else 0.5,
                    edgecolor=C.SURFACE, linewidth=2, height=0.7)
            if r["kind"] == "assumption":
                ax.text(lo, i, "L", ha="right" if lo <= hi else "left", va="center", fontsize=7, color=C.INK2)
                ax.text(hi, i, "H", ha="left" if hi >= lo else "right", va="center", fontsize=7, color=C.INK2)
        ax.axvline(b, color=C.INK, lw=1)
        allv = np.r_[d[f"{col}_at_low"].to_numpy(float), d[f"{col}_at_high"].to_numpy(float)] / 1e3
        ax.set_xlim(np.nanmin(allv) - 3, np.nanmax(allv) + 3)
        ax.text(b, -0.75, f" base ${b:,.0f}k", fontsize=7.5, color=C.INK, va="center")
        ax.set_title(ttl)
        ax.set_xlabel("U.S. dollars (thousands), Laura's plan")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(len(d)), [r["label"] for _, r in d.iterrows()], fontsize=8)
    fig.suptitle("What moves the top of the 2031 range (bottom = floor; share = half)", fontweight="bold")
    C.footer(fig, "MODEL. One input at a time, low (L) to high (H), others at base; 200,000 common market paths. Grey "
                  "bars are not assumptions (the share decision, the return model). Ranges: rab/results/M8/input_ranges.csv. WS2 M8.")
    fig.tight_layout(rect=(0, 0.05, 1, 0.97))
    fig.savefig(os.path.join(OUT, "fig_M8_tornado.png"), dpi=160)
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.0), sharey=True)
    for ax, yname, ttl in ((axes[0], "median_top2031", "Typical (median) 2031 top"),
                           (axes[1], "p5_top2031", "Bad-case (5th percentile) 2031 top")):
        order = list(dB[dB.output == "median_top2031"].sort_values("ST", ascending=False).input)
        z = dB[dB.output == yname].set_index("input").loc[order].iloc[::-1]
        yy = np.arange(len(z))
        ax.barh(yy + 0.18, z.ST, height=0.34, color=C.COL["T"], xerr=z.ST_conf, ecolor=C.INK2, capsize=2,
                label="total effect (ST)")
        ax.barh(yy - 0.18, z.S1.clip(lower=0), height=0.34, color=C.COL["BAYES"], xerr=z.S1_conf, ecolor=C.INK2,
                capsize=2, label="alone (S1)")
        ax.set_title(ttl)
        ax.set_xlabel("share of the variance explained")
        ax.grid(axis="y", visible=False)
        ax.set_xlim(0, 1)
    axes[0].set_yticks(yy, [NAMES[n] for n in z.index], fontsize=8)
    axes[1].legend(loc="lower right", fontsize=8)
    fig.suptitle("Sobol indices, assumptions only (market luck averaged out)", fontweight="bold")
    C.footer(fig, "MODEL. SALib Sobol/Saltelli, N = 4,096, 95% bootstrap intervals; each point = median or 5th "
                  "percentile over 4,000 common market paths. WS2 M8.")
    fig.tight_layout(rect=(0, 0.05, 1, 0.97))
    fig.savefig(os.path.join(OUT, "fig_M8_sobol.png"), dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
