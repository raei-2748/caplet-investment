"""Blind M4: the cap share (decision D6) under the pre-registered rule PR-1..PR-8 (M4_SPEC.md). Writes out/M4/.

Needs the M3 paths in out/paths/ (run blind_m3.py first).
Run: /Users/ray/Research/rab-ws/.venv/bin/python blind_m4.py
"""
from __future__ import annotations

import math
import time

import numpy as np
import pandas as pd

import blind_common as bc

OUT = bc.OUT / "M4"
OUT.mkdir(parents=True, exist_ok=True)
F, B0 = bc.F_FLOOR, bc.B0
Y5, FEE_F = bc.Y5_PAR, bc.FEE_FLOOR
DECISION_MODELS = ["T", "BOOT", "BAYES"]
ALL_MODELS = ["T", "BOOT", "BAYES", "L"]
S_GRID = np.round(np.arange(0.0, 1.0 + 1e-9, 0.01), 2)
H_GRID = np.round(np.arange(0.0, 0.05 + 1e-9, 0.005), 3)
N_PARETO_PATHS = 50_000


# ---- section 1-2: floor delivery ---------------------------------------------------------------------------------
def dgs1_changes(days: int = 913) -> np.ndarray:
    """Changes of the 1-year CMT over `days` calendar days, every business day from 2 Jan 1990 with an end value."""
    df = pd.read_csv(bc.DATA / "fred" / "DGS1.csv")
    df.columns = ["date", "v"]
    df["v"] = pd.to_numeric(df["v"], errors="coerce")
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"] >= "1990-01-02"].reset_index(drop=True)
    dates = df["date"].to_numpy(dtype="datetime64[D]")
    vals = df["v"].to_numpy(dtype=float)
    ends = dates + np.timedelta64(days, "D")
    ok = ends <= dates[-1]
    idx = np.searchsorted(dates, ends[ok], side="right") - 1  # last value on or before date + days
    return vals[idx] - vals[ok]


def floor_delivery(rng: np.random.Generator, n: int, dr_list: np.ndarray, y5: float = Y5, fee: float = FEE_F):
    """M4_SPEC s2: coupons of a 5-year par bullet reinvested at r = max(0, y5 + Delta_r/100) to year 5."""
    dr = rng.choice(dr_list, size=n, replace=True)
    r = np.maximum(0.0, y5 + dr / 100.0)
    reinvest = sum((1.0 + r) ** j for j in range(5))  # (1+r)^(5-k) for k = 1..5
    phi = (1.0 - fee) ** 5 * (1.0 + y5 * reinvest) / (1.0 + y5) ** 5
    return phi, dr, r


def phi_of_r(r: float, y5: float = Y5, fee: float = FEE_F) -> float:
    return (1 - fee) ** 5 * (1 + y5 * sum((1 + r) ** j for j in range(5))) / (1 + y5) ** 5


# ---- section 3-4: decision space and measures --------------------------------------------------------------------
def measures(B3, B5, phi, s, l=0.0, h=0.0, A=None, thr=0.10) -> dict:
    """Outcomes of x = (s, l, h) on one set of paths; if A is given, the low end is the announced A (PR-3)."""
    U = F + s * B3
    L = np.full_like(U, A) if A is not None else F * (1.0 - h) + l * s * B3
    G = np.minimum(phi * F + s * np.minimum(B5, B3), U)
    K = phi * F + B5 - G
    return {
        "E_G": G.mean(), "G_p5": np.percentile(G, 5), "G_p50": np.median(G), "G_p95": np.percentile(G, 95),
        "E_K": K.mean(), "K_p5": np.percentile(K, 5), "K_p50": np.median(K),
        "P_K_ge_thr_G": (K >= thr * G).mean(), "P_G_lt_L": (G < L).mean(),
        "E_width": (U - L).mean(), "U_p50": np.median(U), "L_p50": np.median(L),
        "P_top_fund": (B5 >= B3).mean(), "P_top_gift_eq_U": (G >= U - 1e-9).mean(),
        "P_G_below_middle": (G < 0.5 * (L + U)).mean(), "E_U_minus_G": (U - G).mean(),
    }


def s_star(B3, B5, phi, A, thr=0.10, conf=0.95, max_pd=0.005):
    """PR-6: largest s on the grid meeting PR-4 (P(G<A) <= max_pd) and PR-5 (P(K >= thr G) >= conf)."""
    best = None
    for s in S_GRID:
        U = F + s * B3
        G = np.minimum(phi * F + s * np.minimum(B5, B3), U)
        K = phi * F + B5 - G
        if (G < A).mean() <= max_pd and (K >= thr * G).mean() >= conf:
            best = float(s)
    return best


def pr7(s_rob: float) -> tuple[float, str]:
    if 0.40 <= s_rob <= 0.60:
        return 0.5, "keep s = 1/2 (0.40 <= s* <= 0.60: evidence does not justify changing a simple rule)"
    if s_rob < 0.40:
        cands = [c for c in (0.25, 1 / 3) if c <= s_rob + 1e-12]
        if cands:
            return max(cands), "s* < 0.40: largest of {1/4, 1/3} not above s* (decision to ratify)"
        return math.floor(s_rob / 0.05) * 0.05, "s* < 1/4: s* rounded down to 0.05 (decision to ratify)"
    cands = [c for c in (2 / 3, 0.75, 1.0) if c <= s_rob + 1e-12]
    return max(cands), "s* > 0.60: largest of {2/3, 3/4, 1} not above s* (decision to ratify)"


# ---- section 6.5: Pareto search --------------------------------------------------------------------------------
def pareto_search(B3, B5, phi, seed: int):
    from pymoo.algorithms.moo.nsga2 import NSGA2
    from pymoo.core.problem import Problem
    from pymoo.optimize import minimize

    class CapProblem(Problem):
        def __init__(self):
            super().__init__(n_var=3, n_obj=3, n_ieq_constr=1, xl=np.array([0.0, 0.0, 0.0]), xu=np.array([1.0, 1.0, 0.05]))

        def _evaluate(self, X, out, *args, **kwargs):
            s, l, h = X[:, 0:1], X[:, 1:2], X[:, 2:3]
            b3, b5, ph = B3[None, :], B5[None, :], phi[None, :]
            U = F + s * b3
            L = F * (1.0 - h) + l * s * b3
            G = np.minimum(ph * F + s * np.minimum(b5, b3), U)
            K = ph * F + b5 - G
            out["F"] = np.column_stack([-G.mean(1), (G < L).mean(1), (U - L).mean(1)])
            out["G"] = (0.95 - (K >= 0.10 * G).mean(1))[:, None]

    res = minimize(CapProblem(), NSGA2(pop_size=120), ("n_gen", 200), seed=seed, verbose=False)
    return res.X if res.X is not None else np.empty((0, 3))


def dominated_by_grid(front: pd.DataFrame, grid: pd.DataFrame) -> int:
    """Count front points that some feasible grid point dominates on (-E_G, P_D, E_width)."""
    fa = front[["E_G", "P_G_lt_L", "E_width"]].to_numpy()
    ga = grid[grid["P_K_ge_thr_G"] >= 0.95][["E_G", "P_G_lt_L", "E_width"]].to_numpy()
    if ga.size == 0:
        return 0
    n = 0
    for f in fa:
        better_eq = (ga[:, 0] >= f[0] - 1e-9) & (ga[:, 1] <= f[1] + 1e-12) & (ga[:, 2] <= f[2] + 1e-9)
        strictly = (ga[:, 0] > f[0] + 1e-6) | (ga[:, 1] < f[1] - 1e-9) | (ga[:, 2] < f[2] - 1e-6)
        n += int((better_eq & strictly).any())
    return n


def main() -> None:
    t0 = time.time()
    log = []
    say = lambda s: (print(s, flush=True), log.append(s))

    paths = {m: bc.load_paths(m) for m in ALL_MODELS}
    n = paths["T"].shape[0]
    outs = {m: bc.outcomes(paths[m]) for m in ALL_MODELS}

    # --- floor delivery (PR-3) -------------------------------------------------------------------------------------
    dr_list = dgs1_changes(913)
    phi, dr, r = floor_delivery(bc.rng_for("PHI"), n, dr_list)
    say(f"Delta_r: {dr_list.shape[0]} start dates; p2.5 {np.percentile(dr_list,2.5):+.2f}, median {np.median(dr_list):+.2f}, "
        f"p97.5 {np.percentile(dr_list,97.5):+.2f} points; share below -{100*Y5:.2f} (r floored at 0): {100*(dr_list < -100*Y5).mean():.1f}%")
    say(f"phi checks: r=y5 -> {phi_of_r(Y5):.4f} (spec 0.9965); r=0 -> {phi_of_r(0.0):.4f} (spec 0.9755)")
    fd_rows = [{"quantity": "phi_p0.5", "value": np.percentile(phi, 0.5)}, {"quantity": "phi_p1", "value": np.percentile(phi, 1)},
               {"quantity": "phi_p5", "value": np.percentile(phi, 5)}, {"quantity": "phi_p50", "value": np.median(phi)},
               {"quantity": "phi_p95", "value": np.percentile(phi, 95)}, {"quantity": "phi_max", "value": phi.max()},
               {"quantity": "phi_min", "value": phi.min()}, {"quantity": "phi_mean", "value": phi.mean()},
               {"quantity": "P_r_floored_at_0", "value": (r <= 0).mean()}, {"quantity": "n_delta_r", "value": dr_list.shape[0]}]
    h_star = None
    for h in H_GRID:
        p = (phi < 1.0 - h).mean()
        fd_rows.append({"quantity": f"P_phi_lt_{1-h:.3f}", "value": p})
        if h_star is None and p <= 0.005:
            h_star = float(h)
    A = math.floor(F * (1.0 - h_star) / 5000.0) * 5000.0
    fd_rows += [{"quantity": "h_star", "value": h_star}, {"quantity": "A_announced_floor", "value": A},
                {"quantity": "P_phi_F_lt_A", "value": (phi * F < A).mean()}]
    pd.DataFrame(fd_rows).to_csv(OUT / "floor_delivery.csv", index=False)
    say(f"PR-3: h* = {h_star:.3f}, announced floor A = ${A:,.0f}; P(phi F < A) = {100*(phi*F < A).mean():.3f}%")

    # --- s_profile.csv ------------------------------------------------------------------------------------------------
    prof = []
    for m in ALL_MODELS:
        o = outs[m]
        for s in S_GRID:
            row = {"model": m, "s": float(s)}
            row.update(measures(o["B3"], o["B5"], phi, s, A=A))
            prof.append(row)
    prof = pd.DataFrame(prof)
    prof.to_csv(OUT / "s_profile.csv", index=False)

    # --- decision.csv (PR-4 to PR-7) ---------------------------------------------------------------------------------
    stars = {m: s_star(outs[m]["B3"], outs[m]["B5"], phi, A) for m in ALL_MODELS}
    s_rob = min(stars[m] for m in DECISION_MODELS)
    rec, why = pr7(s_rob)
    dec = []
    for m in ALL_MODELS:
        o = outs[m]
        adopted = measures(o["B3"], o["B5"], phi, 0.5, A=A)
        row = {"model": m, "votes": m in DECISION_MODELS, "s_star_model": stars[m], "s_star_robust": s_rob,
               "PR7_recommendation": rec, "PR7_reason": why}
        row.update({f"adopted_half_{k}": v for k, v in adopted.items()})
        # what binds at s*: which constraint fails at s* + 0.01
        nxt = min(stars[m] + 0.01, 1.0)
        mm = measures(o["B3"], o["B5"], phi, nxt, A=A)
        row["binding_at_s_star_plus_0.01"] = ("PR-5 flexibility" if mm["P_K_ge_thr_G"] < 0.95 else "") + \
                                             (" PR-4 credibility" if mm["P_G_lt_L"] > 0.005 else "") or "grid end"
        dec.append(row)
    pd.DataFrame(dec).to_csv(OUT / "decision.csv", index=False)
    say("PR-6 s*: " + ", ".join(f"{m} {stars[m]:.2f}" for m in ALL_MODELS) + f"; robust s* = {s_rob:.2f} -> PR-7: s = {rec:.4g} ({why})")

    # --- rule_sensitivity.csv ------------------------------------------------------------------------------------
    rs = []
    for thr in (0.05, 0.10, 0.15, 0.20):
        for conf in (0.90, 0.95, 0.99):
            row = {"flex_threshold": thr, "confidence": conf}
            for m in ALL_MODELS:
                v = s_star(outs[m]["B3"], outs[m]["B5"], phi, A, thr=thr, conf=conf)
                row[f"s_star_{m}"] = np.nan if v is None else v  # NaN: no share on the grid meets the rule
            vals = [row[f"s_star_{m}"] for m in DECISION_MODELS]
            row["s_star_robust"] = np.nan if any(np.isnan(v) for v in vals) else min(vals)
            row["PR7_would_recommend"] = np.nan if np.isnan(row["s_star_robust"]) else pr7(row["s_star_robust"])[0]
            rs.append(row)
    pd.DataFrame(rs).to_csv(OUT / "rule_sensitivity.csv", index=False)

    # --- Pareto search (NSGA-II) + grid check ----------------------------------------------------------------------
    pareto_summary = {}
    for m in DECISION_MODELS:
        o = outs[m]
        t1 = time.time()
        X = pareto_search(o["B3"][:N_PARETO_PATHS], o["B5"][:N_PARETO_PATHS], phi[:N_PARETO_PATHS], bc.SEED)
        rows = []
        for s, l, h in X:
            row = {"s": s, "l": l, "h": h}
            row.update(measures(o["B3"], o["B5"], phi, s, l=l, h=h))
            rows.append(row)
        front = pd.DataFrame(rows).sort_values("s").reset_index(drop=True)
        front.to_csv(OUT / f"pareto_{m}.csv", index=False)
        # brute-force grid (A3): s, l in 0.05 steps; h in {0, 0.025, 0.05}, all paths
        grid_rows = []
        for s in np.round(np.arange(0, 1.0001, 0.05), 2):
            for l in np.round(np.arange(0, 1.0001, 0.05), 2):
                for h in (0.0, 0.025, 0.05):
                    row = {"s": s, "l": l, "h": h}
                    row.update(measures(o["B3"], o["B5"], phi, s, l=l, h=h))
                    grid_rows.append(row)
        grid = pd.DataFrame(grid_rows)
        grid.to_csv(OUT / f"pareto_grid_{m}.csv", index=False)
        ndom = dominated_by_grid(front, grid)
        feas = front[front["P_K_ge_thr_G"] >= 0.95]
        pareto_summary[m] = {"n_front": int(len(front)), "n_feasible_on_200k": int(len(feas)),
                             "s_range": [float(front["s"].min()), float(front["s"].max())] if len(front) else None,
                             "max_E_G_feasible": float(feas["E_G"].max()) if len(feas) else None,
                             "s_at_max_E_G": float(feas.loc[feas["E_G"].idxmax(), "s"]) if len(feas) else None,
                             "front_points_dominated_by_grid": ndom, "elapsed_s": time.time() - t1}
        say(f"Pareto {m}: {len(front)} points, s in [{front['s'].min():.2f}, {front['s'].max():.2f}], "
            f"{len(feas)} feasible on 200k, {ndom} dominated by a grid point ({time.time()-t1:.0f}s)")

    # --- narrower_range.csv -----------------------------------------------------------------------------------------
    nr = []
    for l in np.round(np.arange(0.0, 0.9 + 1e-9, 0.1), 1):
        row = {"l": float(l), "s": 0.5, "h": h_star}
        for m in ALL_MODELS:
            o = outs[m]
            mm = measures(o["B3"], o["B5"], phi, 0.5, l=l, h=h_star)
            row[f"{m}_low_end_p50"] = mm["L_p50"]
            row[f"{m}_width_p50"] = np.median(F + 0.5 * o["B3"] - (F * (1 - h_star) + l * 0.5 * o["B3"]))
            row[f"{m}_P_G_lt_L"] = mm["P_G_lt_L"]
        nr.append(row)
    pd.DataFrame(nr).to_csv(OUT / "narrower_range.csv", index=False)

    # --- figures -------------------------------------------------------------------------------------------------
    try:
        make_figures(prof, phi, A, h_star, stars, s_rob)
    except Exception as exc:
        say(f"figure step failed: {exc!r}")

    # --- headline ------------------------------------------------------------------------------------------------
    head = {"h_star": h_star, "A_announced_floor": A, "s_star_by_model": stars, "s_star_robust": s_rob,
            "PR7_recommendation": rec, "PR7_reason": why, "N": n, "seed": bc.SEED,
            "phi": {"p0.5": float(np.percentile(phi, 0.5)), "p1": float(np.percentile(phi, 1)), "p5": float(np.percentile(phi, 5)),
                    "p50": float(np.median(phi)), "p95": float(np.percentile(phi, 95)), "max": float(phi.max()), "min": float(phi.min())},
            "delta_r_n": int(dr_list.shape[0]), "adopted_half": {}, "pareto": pareto_summary,
            "rule_sensitivity_s_star_robust": {f"thr{r['flex_threshold']}_conf{r['confidence']}": (None if np.isnan(r["s_star_robust"]) else r["s_star_robust"]) for r in rs}}
    for m in ALL_MODELS:
        o = outs[m]
        mm = measures(o["B3"], o["B5"], phi, 0.5, A=A)
        head["adopted_half"][m] = {k: float(v) for k, v in mm.items()}
    head["elapsed_s"] = time.time() - t0
    head["log"] = log
    bc.write_json(head, OUT / "headline_M4.json")
    say(f"M4 done in {time.time()-t0:.0f}s -> {OUT}")


def make_figures(prof: pd.DataFrame, phi, A, h_star, stars, s_rob) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    okabe = {"L": "#999999", "T": "#E69F00", "BOOT": "#0072B2", "BAYES": "#009E73"}
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
    for m in ALL_MODELS:
        d = prof[prof["model"] == m]
        ax1.plot(d["s"], d["E_G"] / 1000, color=okabe[m], lw=1.8, label=m)
        ax2.plot(d["s"], d["P_K_ge_thr_G"], color=okabe[m], lw=1.8, label=m)
    ax1.axvline(0.5, color="k", ls="--", lw=1)
    ax1.set_xlabel("share s of the 2031 fund promised at the top")
    ax1.set_ylabel("expected 2033 gift (\\$ thousand)")
    ax1.set_title("E[gift] rises with s (adopted s = 1/2 dashed)")
    ax2.axhline(0.95, color="#D55E00", lw=1.2)
    ax2.text(0.02, 0.952, "PR-5: at least 95%", color="#D55E00", fontsize=8)
    ax2.axvline(0.5, color="k", ls="--", lw=1)
    ax2.axvline(s_rob, color="#CC79A7", lw=1.2)
    ax2.text(s_rob - 0.02, 0.56, f"robust s* = {s_rob:.2f}", color="#CC79A7", fontsize=8, ha="right")
    ax2.set_xlabel("share s")
    ax2.set_ylabel("P(Laura keeps at least 10% of her gift)")
    ax2.set_title("Flexibility constraint")
    ax2.set_ylim(0.5, 1.01)
    ax2.legend(frameon=False, fontsize=8)
    fig.suptitle("M4 s-profile (blind rebuild)", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M4_s_profile.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.2))
    for m in DECISION_MODELS:
        p = OUT / f"pareto_{m}.csv"
        if p.exists():
            d = pd.read_csv(p)
            ax.scatter(d["E_width"] / 1000, 100 * d["P_G_lt_L"], s=12, color=okabe[m], label=f"{m} NSGA-II front", alpha=0.8)
    d05 = prof[(prof["s"] == 0.5)]
    for m in DECISION_MODELS:
        r = d05[d05["model"] == m].iloc[0]
        ax.scatter(r["E_width"] / 1000, 100 * r["P_G_lt_L"], marker="*", s=140, color=okabe[m], edgecolor="k", zorder=5)
    ax.set_xlabel("expected width of the announced range (\\$ thousand)")
    ax.set_ylabel("P(gift below the announced low end), %")
    ax.set_title("Width vs disappointment; stars = adopted (s = 1/2, l = 0, low end A) (blind)", fontsize=10)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M4_pareto.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.hist(phi, bins=200, color="#0072B2", density=True)
    ax.axvline(A / F, color="#D55E00", lw=1.5)
    ax.text(A / F + 0.0005, ax.get_ylim()[1] * 0.85, f"announced floor A = \\${A:,.0f} ({100*A/F:.1f}% of face)", color="#D55E00", fontsize=8)
    ax.axvline(1 - h_star, color="#CC79A7", lw=1, ls="--")
    ax.set_xlabel("floor delivery ratio phi (what \\$150,000 of face finally pays, as a share)")
    ax.set_ylabel("density")
    ax.set_title("Floor delivery: coupons reinvested at historical 30-month yield changes (blind)", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT / "fig_M4_floor.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
