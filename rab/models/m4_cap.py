"""M4: the cap share s (decision D6) under the pre-registered rule of rab/models/M4_SPEC.md section 5.

WS2, RAB Kit, 2026-09-30 (Sydney). AI-generated research (Claude Code) for Team Caplet; no deliverable text.
The rule was committed (3d98ce0) before this file was written. Every output is a MODEL property, not a forecast,
and the result is a decision for the team to ratify; nothing is applied to the IPS or the Sheet.

Run from the worktree root after m3_branch.py (about 5 minutes; no network):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m4_cap.py
Writes rab/results/M4/.
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m3_branch as M3  # noqa: E402
import ws2_common as C  # noqa: E402

OUT = os.path.join(C.RESULTS, "M4")
LOG = []
FEE_F = 0.0007
KAPPA, CONF = 0.10, 0.95          # PR-5
PD_MAX = 0.005                    # PR-3, PR-4
H_GRID = np.round(np.arange(0, 0.0501, 0.005), 3)
S_GRID = np.round(np.arange(0, 1.0001, 0.01), 2)
MODELS = ["L", "T", "BOOT", "BAYES"]


def say(s=""):
    print(s)
    LOG.append(s)


# ------------------------------------------------------------------ floor delivery (M4_SPEC section 2)
def dgs1_changes():
    d = pd.read_csv(os.path.join(C.ROOT, "rab/data/fred/DGS1.csv"))
    d.columns = ["date", "v"]
    d["date"] = pd.to_datetime(d["date"])
    d["v"] = pd.to_numeric(d["v"], errors="coerce")
    x = d.dropna().set_index("date")["v"]
    x = x[x.index >= "1990-01-02"]
    tgt = x.index + pd.Timedelta(days=913)
    end = x.reindex(x.index.union(tgt)).sort_index().ffill().reindex(tgt).to_numpy()
    ok = tgt <= x.index[-1]
    return (end - x.to_numpy())[ok]


def phi_draws(y5, n=C.N_PATHS):
    ch = dgs1_changes()
    g = C.rng("floor")
    r = np.maximum(0.0, y5 + ch[g.integers(0, len(ch), n)] / 100)
    coup = sum((1 + r) ** (5 - kk) for kk in range(1, 6))
    phi = (1 - FEE_F) ** 5 * (1 + y5 * coup) / (1 + y5) ** 5
    return phi, r, len(ch)


# ------------------------------------------------------------------ measures
def measures(o, phi, F, s, l=0.0, low=None):
    """o = dict with B3, B5 arrays; returns the M4_SPEC section 4 measures for share s and low end."""
    B3, B5 = o["B3"], o["B5"]
    U = F + s * B3
    L = (np.full_like(B3, low) if low is not None else F) + l * s * B3
    G = np.minimum(phi * F + s * np.minimum(B5, B3), U)
    K = phi * F + B5 - G
    out = {"EG": G.mean(), "G_p5": np.percentile(G, 5), "G_p50": np.median(G), "G_p95": np.percentile(G, 95),
           "EK": K.mean(), "K_p5": np.percentile(K, 5), "K_p50": np.median(K),
           "P_flex": np.mean(K >= KAPPA * G), "P_D": np.mean(G < L), "E_width": np.mean(U - L),
           "U_p50": np.median(U), "L_p50": np.median(L), "P_top": np.mean(G >= U - 1e-6),
           "P_below_middle": np.mean(G < (L + U) / 2), "E_short_top": np.mean(U - G), "_G": G, "_K": K}
    # Added after the first run (not pre-registered; no decision uses it): the fund-based "top reached" (B5 >= B3),
    # and the variant in which the top is also announced from the rounded-down floor, U_A = low + s B3.
    out["P_top_fund"] = np.mean(B5 >= B3)
    if low is not None and l == 0:
        UA = low + s * B3
        GA = np.minimum(phi * F + s * np.minimum(B5, B3), UA)
        KA = phi * F + B5 - GA
        out.update({"A_EG": GA.mean(), "A_P_top": np.mean(GA >= UA - 1e-6), "A_P_flex": np.mean(KA >= KAPPA * GA),
                    "A_K_p5": np.percentile(KA, 5), "A_P_D": np.mean(GA < low), "A_U_p50": np.median(UA)})
    return out


def largest_s(rows, pd_max=PD_MAX, kappa=None, conf=CONF, G=None, K=None):
    ok = [r for r in rows if r["P_D"] <= pd_max and r[f"P_flex_{kappa}" if kappa else "P_flex"] >= conf]
    return max(r["s"] for r in ok) if ok else None


def main():
    os.makedirs(OUT, exist_ok=True)
    inp = C.inputs()
    F, y5 = inp["F"], inp["y5"]
    say(f"M4 cap optimiser | run {C.stamp()} | numbers.yaml {inp['numbers_sha'][:12]} | rule: M4_SPEC.md s5 "
        f"(pre-registered, commit 3d98ce0)")

    # PR-3: announced floor
    phi, r, nch = phi_draws(y5)
    fd = {"n_changes": nch, "phi_min": phi.min(), "phi_p0_5": np.percentile(phi, 0.5), "phi_p1": np.percentile(phi, 1),
          "phi_p5": np.percentile(phi, 5), "phi_p50": np.median(phi), "phi_p95": np.percentile(phi, 95),
          "phi_max": phi.max(), "P_r_zero": np.mean(r == 0)}
    h_star = next(h for h in H_GRID if np.mean(phi < 1 - h) <= PD_MAX)
    A = np.floor(F * (1 - h_star) / 5000) * 5000
    rows_h = [{"h": h, "P_phi_below_1_minus_h": np.mean(phi < 1 - h)} for h in H_GRID]
    pd.DataFrame(rows_h).assign(**{k: v for k, v in fd.items()}, h_star=h_star, announced_floor=A).to_csv(
        os.path.join(OUT, "floor_delivery.csv"), index=False)
    say(f"  floor delivery phi ({nch} historical 30-month changes of the 1-year yield since 1990): p0.5 "
        f"{fd['phi_p0_5']:.4f}, p5 {fd['phi_p5']:.4f}, median {fd['phi_p50']:.4f}, max {fd['phi_max']:.4f}; "
        f"floor pays ${phi.min() * F:,.0f} at worst, ${np.median(phi) * F:,.0f} at the median")
    say(f"  PR-3: h* = {h_star:.3f} -> announced floor A = ${A:,.0f} (P(floor holding pays less) = "
        f"{np.mean(phi * F < A):.3%})")

    # s-profile for every model (PR-4..PR-6)
    prof, outs = [], {}
    for m in MODELS:
        x = M3.paths(m)
        o = C.rule(x, inp["B0"], F)
        outs[m] = o
        for s in S_GRID:
            q = measures(o, phi, F, s, low=A)
            row = {"model": m, "s": s, **{k: v for k, v in q.items() if not k.startswith("_")}}
            for kap in (0.05, 0.10, 0.15, 0.20):
                row[f"P_flex_{kap}"] = np.mean(q["_K"] >= kap * q["_G"])
            prof.append(row)
    dfp = pd.DataFrame(prof)
    dfp.to_csv(os.path.join(OUT, "s_profile.csv"), index=False)

    # decision
    sstar = {}
    for m in MODELS:
        rows = dfp[dfp.model == m].to_dict("records")
        sstar[m] = largest_s(rows)
    s_rob = min(sstar[m] for m in M3.DECISION)
    if 0.40 <= s_rob <= 0.60:
        rec, why = 0.5, "keep 1/2: robust optimum within [0.40, 0.60] (PR-7)"
    elif s_rob < 0.40:
        cands = [c for c in (1 / 4, 1 / 3) if c <= s_rob + 1e-9]
        rec = max(cands) if cands else np.floor(s_rob / 0.05) * 0.05
        why = "change below 1/2 (PR-7): decision to ratify"
    else:
        rec = max(c for c in (2 / 3, 3 / 4, 1.0) if c <= s_rob + 1e-9)
        why = "change above 1/2 (PR-7): decision to ratify"
    adopted = dfp[dfp.s == 0.5].set_index("model")
    dec = [{"model": m, "s_star": sstar[m], "votes": m in M3.DECISION, **{f"adopted_{k}": adopted.loc[m, k] for k in
            ("EG", "G_p5", "G_p50", "EK", "K_p5", "K_p50", "P_flex", "P_D", "E_width", "P_top", "P_below_middle",
             "E_short_top")}} for m in MODELS]
    dec.append({"model": "ROBUST", "s_star": s_rob, "votes": True, "adopted_EG": np.nan})
    pd.DataFrame(dec).assign(recommendation=rec, reason=why, announced_floor=A, h_star=h_star).to_csv(
        os.path.join(OUT, "decision.csv"), index=False)
    for m in MODELS:
        a = adopted.loc[m]
        say(f"  {m:6s} s* = {sstar[m]:.2f} | at s = 1/2: E[gift] ${a['EG']:,.0f}, gift p5 ${a['G_p5']:,.0f}, kept p5 "
            f"${a['K_p5']:,.0f}, P(kept >= 10% of gift) {a['P_flex']:.2%}, P(gift < ${A / 1000:.0f}k) {a['P_D']:.3%}, "
            f"P(gift = face-based top) {a['P_top']:.1%}, P(fund no lower in 2033) {a['P_top_fund']:.1%}, "
            f"E[shortfall below top] ${a['E_short_top']:,.0f}")
        say(f"         announced-basis top (A + s B3, added after the first run): P(top reached) {a['A_P_top']:.1%}, "
            f"P(kept >= 10% of gift) {a['A_P_flex']:.2%}, E[gift] ${a['A_EG']:,.0f}, median top ${a['A_U_p50']:,.0f}")
    say(f"  ROBUST s* = {s_rob:.2f} -> recommendation s = {rec:.3f} ({why})")

    # PR-8 rule sensitivity
    rs = []
    for m in MODELS:
        rows = dfp[dfp.model == m].to_dict("records")
        for kap in (0.05, 0.10, 0.15, 0.20):
            for conf in (0.90, 0.95, 0.99):
                ok = [r_["s"] for r_ in rows if r_["P_D"] <= PD_MAX and r_[f"P_flex_{kap}"] >= conf]
                rs.append({"model": m, "kappa": kap, "confidence": conf, "s_star": max(ok) if ok else None})
    dfr = pd.DataFrame(rs)
    dfr.to_csv(os.path.join(OUT, "rule_sensitivity.csv"), index=False)
    # Gate B fix (30 Sep): a model with no passing share makes the robust s* "none"; pandas' min() skipped it.
    piv = dfr[dfr.model.isin(M3.DECISION)].groupby(["kappa", "confidence"])["s_star"].agg(
        lambda v: v.min() if v.notna().all() else np.nan).unstack()
    say("  rule sensitivity (robust s* = min over T, BOOT, BAYES), rows = kept-money threshold, columns = confidence:")
    for kap, rr in piv.iterrows():
        say(f"    keep >= {kap:.0%} of gift: " + ", ".join(f"{c:.0%}: " + ("none" if pd.isna(v) else f"{v:.2f}")
                                                          for c, v in rr.items()))

    # narrower range (l > 0), s = 1/2
    nr = []
    for m in MODELS:
        for l in np.round(np.arange(0, 0.91, 0.1), 1):
            q = measures(outs[m], phi, F, 0.5, l=l, low=A)
            nr.append({"model": m, "l": l, "low_end_p50": q["L_p50"], "width_p50": np.median(0.5 * outs[m]["B3"] *
                       (1 - l)) + (F - A), "P_D": q["P_D"], "E_width": q["E_width"]})
    dfn = pd.DataFrame(nr)
    dfn.to_csv(os.path.join(OUT, "narrower_range.csv"), index=False)
    for m in M3.DECISION:
        z = dfn[dfn.model == m].set_index("l")
        say(f"  narrower range, {m:5s}: low end raised to ${z.loc[0.4, 'low_end_p50']:,.0f} (l=0.4) -> P(gift below it) "
            f"{z.loc[0.4, 'P_D']:.2%}; to ${z.loc[0.6, 'low_end_p50']:,.0f} (l=0.6) -> {z.loc[0.6, 'P_D']:.2%}; "
            f"to ${z.loc[0.8, 'low_end_p50']:,.0f} (l=0.8) -> {z.loc[0.8, 'P_D']:.2%}")

    # Pareto search
    fronts = {m: pareto(m, outs[m], phi, F) for m in M3.DECISION}
    figures(dfp, dfn, fronts, phi, F, A, sstar, rec, inp)
    open(os.path.join(OUT, "run_log.txt"), "w").write("\n".join(LOG) + "\n")


def pareto(m, o, phi, F, n_opt=50_000):
    from pymoo.algorithms.moo.nsga2 import NSGA2
    from pymoo.core.problem import Problem
    from pymoo.optimize import minimize
    from pymoo.util.nds.non_dominated_sorting import NonDominatedSorting

    def evaluate(X, B3, B5, ph):
        Fo, Gc = [], []
        for s, l, h in X:
            U = F + s * B3
            L = F * (1 - h) + l * s * B3
            G = np.minimum(ph * F + s * np.minimum(B5, B3), U)
            K = ph * F + B5 - G
            Fo.append([-G.mean() / 1000, np.mean(G < L), np.mean(U - L) / 1000])
            Gc.append([CONF - np.mean(K >= KAPPA * G)])
        return np.array(Fo), np.array(Gc)

    B3s, B5s, ps = o["B3"][:n_opt], o["B5"][:n_opt], phi[:n_opt]

    class P(Problem):
        def __init__(self):
            super().__init__(n_var=3, n_obj=3, n_ieq_constr=1, xl=np.array([0, 0, 0]), xu=np.array([1, 1, 0.05]))

        def _evaluate(self, X, out, *a, **kw):
            out["F"], out["G"] = evaluate(X, B3s, B5s, ps)

    res = minimize(P(), NSGA2(pop_size=120), ("n_gen", 200), seed=C.SEED, verbose=False)
    # cross-check (added; not in the spec): brute-force grid on all paths, exact non-dominated set
    grid = np.array([(s_, l_, h_) for s_ in np.arange(0, 1.001, 0.05) for l_ in np.arange(0, 1.001, 0.05)
                     for h_ in (0.0, 0.025, 0.05)])
    Fg, Gg = evaluate(grid, o["B3"], o["B5"], phi)
    okg = Gg[:, 0] <= 0
    ndg = NonDominatedSorting().do(Fg[okg], only_non_dominated_front=True)
    gf = pd.DataFrame({"s": grid[okg][ndg, 0], "l": grid[okg][ndg, 1], "h": grid[okg][ndg, 2],
                       "E_gift": -Fg[okg][ndg, 0] * 1000, "P_D": Fg[okg][ndg, 1], "E_width": Fg[okg][ndg, 2] * 1000})
    gf.sort_values(["P_D", "E_width"]).to_csv(os.path.join(OUT, f"pareto_grid_{m}.csv"), index=False)
    X = np.atleast_2d(res.X)
    Fo, Gc = evaluate(X, o["B3"], o["B5"], phi)
    feas = Gc[:, 0] <= 0
    X, Fo = X[feas], Fo[feas]
    nd = NonDominatedSorting().do(Fo, only_non_dominated_front=True)
    X, Fo = X[nd], Fo[nd]
    df = pd.DataFrame({"s": X[:, 0], "l": X[:, 1], "h": X[:, 2], "E_gift": -Fo[:, 0] * 1000, "P_D": Fo[:, 1],
                       "E_width": Fo[:, 2] * 1000}).sort_values(["P_D", "E_width"])
    df.to_csv(os.path.join(OUT, f"pareto_{m}.csv"), index=False)
    # does any grid point dominate an NSGA-II point (both on all paths)?
    Fa, Fb = df[["E_gift", "P_D", "E_width"]].to_numpy() * [-1, 1, 1], gf[["E_gift", "P_D", "E_width"]].to_numpy() * [-1, 1, 1]
    dom = [bool(np.any(np.all(Fb <= a + 1e-12, axis=1) & np.any(Fb < a - 1e-9, axis=1))) for a in Fa]
    say(f"  Pareto {m:5s}: NSGA-II {len(df)} non-dominated points (s {df.s.min():.2f}-{df.s.max():.2f}, l "
        f"{df.l.min():.2f}-{df.l.max():.2f}); grid front {len(gf)} points (s up to {gf.s.max():.2f}); NSGA-II points "
        f"dominated by a grid point: {sum(dom)}")
    return df


def figures(dfp, dfn, fronts, phi, F, A, sstar, rec, inp):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    C.style(plt)

    # s-profile
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
    for m in ["L", "T", "BOOT", "BAYES"]:
        z = dfp[dfp.model == m]
        a1.plot(z.s, z.EG / 1e3, color=C.COL[m], ls=C.LS[m], label=C.LABEL[m], lw=1.8)
        a2.plot(z.s, z.P_flex * 100, color=C.COL[m], ls=C.LS[m], label=C.LABEL[m], lw=1.8)
        if m in M3.DECISION:
            a2.plot(sstar[m], z.set_index("s").loc[sstar[m], "P_flex"] * 100, "o", ms=8, color=C.COL[m],
                    mec=C.SURFACE, mew=2)
    z = dfp[dfp.model == "BAYES"]
    a1.plot(z.s, z.EK / 1e3, color=C.COL["BAYES"], lw=1.2, alpha=0.6)
    a1.text(0.02, z.EK.iloc[2] / 1e3 + 2, "Laura keeps (expected)", fontsize=8, color=C.INK2)
    a1.text(0.02, z.EG.iloc[2] / 1e3 + 2, "gift (expected)", fontsize=8, color=C.INK2)
    for a in (a1, a2):
        a.axvline(0.5, color=C.INK, lw=1, ls=":")
    a1.text(0.51, 60, "adopted: half", fontsize=8)
    a1.set_xlabel("share of the stock fund promised (s)")
    a1.set_ylabel("U.S. dollars (thousands), Laura's plan")
    a1.set_title("Every extra share moves dollars from Laura to the gift")
    a2.axhline(CONF * 100, color=C.INK2, lw=1, ls="--")
    a2.text(0.02, CONF * 100 + 0.6, "rule: at least 95% of paths", fontsize=8, color=C.INK2)
    a2.set_ylim(80, 101)
    a2.set_xlabel("share of the stock fund promised (s)")
    a2.set_ylabel("paths where Laura keeps >= 10% of her gift (%)")
    a2.set_title("Flexibility falls as the share rises")
    a2.legend(loc="lower left", fontsize=7.5)
    a2.annotate(f"largest share passing: {min(sstar[m] for m in M3.DECISION):.2f}-{max(sstar[m] for m in M3.DECISION):.2f}",
                (min(sstar[m] for m in M3.DECISION), 95), xytext=(-150, -45), textcoords="offset points", fontsize=8,
                arrowprops=dict(arrowstyle="-", color=C.INK2, lw=0.8))
    C.footer(fig, f"MODEL. Dots = the largest share passing both hard rules in each decision model (M4_SPEC PR-6). "
                  f"Announced floor ${A / 1000:.0f}k; seed 20260930. WS2 M4.")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_M4_s_profile.png"), dpi=160)
    plt.close(fig)

    # Pareto fronts: small multiples, colour = expected gift (one sequential hue)
    from matplotlib.colors import LinearSegmentedColormap
    seq = LinearSegmentedColormap.from_list("blue", ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.0), sharey=True)
    vmin = min(df.E_gift.min() for df in fronts.values()) / 1e3
    vmax = max(df.E_gift.max() for df in fronts.values()) / 1e3
    ad = dfp[dfp.s == 0.5].set_index("model")
    for ax, (m, df) in zip(axes, fronts.items()):
        sc = ax.scatter(df.E_width / 1e3, df.P_D * 100, s=16, c=df.E_gift / 1e3, cmap=seq, vmin=vmin, vmax=vmax,
                        edgecolors=C.INK2, linewidths=0.3)
        ax.scatter(ad.loc[m, "E_width"] / 1e3, ad.loc[m, "P_D"] * 100, marker="*", s=200, color=C.COL["BOOT"],
                   edgecolors=C.INK, linewidths=0.6, zorder=5)
        ax.annotate("adopted: half,\nlow end = floor", (ad.loc[m, "E_width"] / 1e3, ad.loc[m, "P_D"] * 100),
                    xytext=(-95, 45), textcoords="offset points", fontsize=7.5,
                    arrowprops=dict(arrowstyle="-", color=C.INK2, lw=0.8))
        ax.set_title(C.LABEL[m], fontsize=9.5)
        ax.set_xlabel("expected range width ($k)")
    axes[0].set_ylabel("chance the gift is below the announced low end (%)")
    cax = fig.add_axes([0.905, 0.2, 0.012, 0.64])
    cb = fig.colorbar(sc, cax=cax)
    cb.set_label("expected 2033 gift ($k)")
    fig.suptitle("Best trade-offs found (NSGA-II): narrower ranges need a higher low end, which can be broken",
                 fontsize=11, fontweight="bold")
    C.footer(fig, "MODEL. Search over share, low-end share and floor haircut, with the flexibility rule. Each dot "
                  "is a non-dominated choice. WS2 M4.")
    fig.subplots_adjust(left=0.07, right=0.88, bottom=0.2, top=0.84, wspace=0.08)
    fig.savefig(os.path.join(OUT, "fig_M4_pareto.png"), dpi=160)
    plt.close(fig)

    # narrower range, the plain version
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    for m in M3.DECISION:
        z = dfn[dfn.model == m]
        ax.plot(z.low_end_p50 / 1e3, z.P_D * 100, color=C.COL[m], ls=C.LS[m], marker="o", ms=5, label=C.LABEL[m])
    ax.set_xlabel("announced low end in a typical case, U.S. dollars (thousands)")
    ax.set_ylabel("chance the 2033 gift is below it (%)")
    ax.set_title("Raising the low end above the floor brings a chance of a broken promise")
    ax.legend(fontsize=8)
    C.footer(fig, f"MODEL. Share 1/2. Low end = ${A / 1000:.0f}k + l x half the fund's 2031 value, l = 0 to 0.9. "
                  "Adopted: l = 0. WS2 M4.")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_M4_narrower.png"), dpi=160)
    plt.close(fig)

    # floor delivery
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    ax.hist(phi * F / 1e3, bins=80, color=C.COL["T"], edgecolor=C.SURFACE, linewidth=0.5)
    ax.axvline(F / 1e3, color=C.INK, lw=1.2)
    ax.axvline(A / 1e3, color=C.COL["BOOT"], lw=2, ls="--")
    ax.text(F / 1e3 + 0.1, ax.get_ylim()[1] * 0.9, "face $150k", fontsize=8.5)
    ax.text(A / 1e3 + 0.1, ax.get_ylim()[1] * 0.9, f"announce ${A / 1000:.0f}k", fontsize=8.5)
    ax.set_xlabel("what the floor holding pays by late 2032, U.S. dollars (thousands), Laura's plan")
    ax.set_ylabel("paths")
    ax.set_title("An iBond-fund floor pays a little less than its face value")
    C.footer(fig, "MODEL. Income reinvested at the 5-year yield plus a historical 30-month change in the 1-year\n"
                  "yield (1990-2026, floored at 0%); 0.07% fund fee. WS2 M4.")
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_M4_floor.png"), dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
