"""M3: the Branch 2028-2033 under three return models (spec: rab/models/M3_SPEC.md).

WS2, RAB Kit, 2026-09-30 (Sydney). AI-generated research (Claude Code) for Team Caplet; no deliverable text.
Every output is a MODEL property under the stated assumptions, not a forecast.

Run from the worktree root (about 1 minute; no network):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m3_branch.py
Writes rab/results/M3/ (CSV, PNG, run_log.txt, numbers_proposed.yaml, bayes_posterior_draws.npz).
M4 and M8 import the path generators from this file, so every WS2 model sees the same paths.
"""
import csv
import os
import sys

os.environ.setdefault("PYTENSOR_FLAGS", "mode=NUMBA,cxx=")   # this Mac's clang rejects pytensor's C flags
import numpy as np
import pandas as pd
from scipy import integrate, optimize, stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ws2_common as C  # noqa: E402

OUT = os.path.join(C.RESULTS, "M3")
LOG = []
NU_T = 4
TRUNC = 5.0


def say(s=""):
    print(s)
    LOG.append(s)


# ------------------------------------------------------------------ return models (annual log returns, paths x 5)
def gen_L(n=C.N_PATHS):
    return C.MU_L + C.SIG_L * C.rng("L").standard_normal((n, 5))


def t_scale():
    """Scale c so that c * t_4, truncated at |x| <= 5 sig_L, has sd sig_L (M3_SPEC section 3, T)."""
    K = TRUNC * C.SIG_L

    def var(c):
        a = K / c
        Z = stats.t.cdf(a, NU_T) - stats.t.cdf(-a, NU_T)
        return c * c * integrate.quad(lambda z: z * z * stats.t.pdf(z, NU_T), -a, a)[0] / Z, 1 - Z

    c0 = C.SIG_L * np.sqrt((NU_T - 2) / NU_T)
    c = optimize.brentq(lambda c: var(c)[0] - C.SIG_L ** 2, 0.8 * c0, 1.5 * c0, xtol=1e-12)
    return c, var(c)[1]


def truncated_t(g, mu, scale, nu, bound, shape):
    """Draws mu + scale * t_nu; any draw with |x - mu| > bound is redrawn. Parameters are scalars or arrays that
    broadcast to shape (e.g. one value per path, shape (n, 1))."""
    mu, scale, nu, bound = (np.broadcast_to(np.asarray(a, float), shape) for a in (mu, scale, nu, bound))
    x = mu + scale * g.standard_t(nu)
    bad = np.abs(x - mu) > bound
    while bad.any():
        x[bad] = mu[bad] + scale[bad] * g.standard_t(nu[bad])
        bad = np.abs(x - mu) > bound
    return x


def gen_T(n=C.N_PATHS):
    c, _ = t_scale()
    return truncated_t(C.rng("T"), C.MU_L, c, NU_T, TRUNC * C.SIG_L, (n, 5))


def shiller_monthly():
    d = pd.read_csv(os.path.join(C.ROOT, "rab/data/ws2_returns/shiller_monthly.csv"))
    i0, i1 = d.index[d["month"] == "1871-01"][0], d.index[d["month"] == "2025-12"][0]
    y = np.log1p(d.loc[i0:i1, "r_nominal"].to_numpy(float))
    assert len(y) == 1860 and np.isfinite(y).all()
    return y


def gen_BOOT(n=C.N_PATHS, block=24, recentre=True, stream="BOOT"):
    y = shiller_monthly()
    if recentre:
        y = y - y.mean() + C.MU_L / 12
    g = C.rng(stream)
    m = len(y)
    idx = g.integers(0, m, n)
    months = np.empty((n, 60))
    months[:, 0] = y[idx]
    p = 1.0 / block
    for k in range(1, 60):
        jump = g.random(n) < p
        idx = np.where(jump, g.integers(0, m, n), (idx + 1) % m)
        months[:, k] = y[idx]
    return months.reshape(n, 5, 12).sum(axis=2)


def bayes_fit(force=False):
    """History fit of the BAYES model (M3_SPEC section 3, part 1); cached in rab/results/M3/."""
    path = os.path.join(OUT, "bayes_posterior_draws.npz")
    if os.path.exists(path) and not force:
        z = np.load(path)
        return {k: z[k] for k in z.files}
    import arviz as az
    import pymc as pm
    z = pd.read_csv(os.path.join(C.ROOT, "rab/data/ws2_returns/shiller_annual.csv"))
    z = z[(z.year >= 1871) & (z.year <= 2025)]["log_r_nominal"].to_numpy(float)
    assert len(z) == 155
    seed = int(C.rng("BAYES-mcmc").integers(0, 2 ** 31 - 1))
    with pm.Model():
        m_h = pm.Normal("m_h", 0.08, 0.05)
        sigma = pm.HalfNormal("sigma", 0.30)
        nu_p = pm.Gamma("nu_p", alpha=2.0, beta=0.1)
        nu = pm.Deterministic("nu", 2.0 + nu_p)
        pm.StudentT("z", nu=nu, mu=m_h, sigma=sigma, observed=z)
        idata = pm.sample(draws=1000, tune=1000, chains=4, cores=1, target_accept=0.9, random_seed=seed,
                          progressbar=False)
    summ = az.summary(idata, var_names=["m_h", "sigma", "nu"])
    post = idata["posterior"]
    out = {k: np.asarray(post[k].values).reshape(-1) for k in ("m_h", "sigma", "nu")}
    rhat = {k: float(summ.loc[k, "r_hat"]) for k in ("m_h", "sigma", "nu")}
    ess = {k: float(summ.loc[k, "ess_bulk"]) for k in ("m_h", "sigma", "nu")}
    for k in rhat:
        if not (rhat[k] <= 1.01 and ess[k] >= 400):
            raise SystemExit(f"BAYES did not converge: {k} r_hat {rhat[k]} ess {ess[k]}")
    out["r_hat"] = np.array([rhat[k] for k in ("m_h", "sigma", "nu")])
    out["ess_bulk"] = np.array([ess[k] for k in ("m_h", "sigma", "nu")])
    out["seed"] = np.array([seed])
    os.makedirs(OUT, exist_ok=True)
    np.savez(path, **out)
    return out


def gen_BAYES(n=C.N_PATHS, hist=False):
    post = bayes_fit()
    g = C.rng("BAYES-hist" if hist else "BAYES")
    j = g.integers(0, len(post["sigma"]), n)
    sig, nu = post["sigma"][j][:, None], post["nu"][j][:, None]
    mu = post["m_h"][j][:, None] if hist else g.normal(C.MU_L, 0.015, n)[:, None]
    sd = sig * np.sqrt(nu / (nu - 2))
    return truncated_t(g, mu, sig, nu, TRUNC * sd, (n, 5))


GENERATORS = {
    "L": gen_L, "T": gen_T, "BOOT": gen_BOOT, "BAYES": gen_BAYES,
    "BOOT-raw": lambda n=C.N_PATHS: gen_BOOT(n, recentre=False, stream="BOOT-raw"),
    "BOOT-b1": lambda n=C.N_PATHS: gen_BOOT(n, block=1, stream="BOOT-b1"),
    "BOOT-b60": lambda n=C.N_PATHS: gen_BOOT(n, block=60, stream="BOOT-b60"),
    "BAYES-hist": lambda n=C.N_PATHS: gen_BAYES(n, hist=True),
}
DECISION = ["T", "BOOT", "BAYES"]
HEADLINE = ["L", "T", "BOOT", "BAYES"]


def paths(model, n=C.N_PATHS):
    return GENERATORS[model](n)


# ------------------------------------------------------------------ summaries
PCT = (5, 10, 25, 50, 75, 90, 95)


def summarise(model, x, inp):
    o = C.rule(x, inp["B0"], inp["F"])
    row = {"model": model}
    for k in ("B3", "U", "G", "K", "T"):
        q = np.percentile(o[k], PCT)
        for p, v in zip(PCT, q):
            row[f"{k}_p{p}"] = round(float(v), 2)
        row[f"{k}_mean"] = round(float(o[k].mean()), 2)
    row["P_top_reached"] = float(np.mean(o["B5"] >= o["B3"]))
    row["P_upper_half"] = float(np.mean(o["B5"] / o["B3"] >= 0.5))
    row["median_position"] = float(np.median(o["pos"]))
    row["P_B3_below_B0"] = float(np.mean(o["B3"] < inp["B0"]))
    row["P_G_within_range"] = float(np.mean((o["G"] >= inp["F"] - 1e-9) & (o["G"] <= o["U"] + 1e-9)))
    row["P_K_ge_10pct_G"] = float(np.mean(o["K"] >= 0.10 * o["G"]))
    row["x_mean"] = float(x.mean())
    row["x_sd"] = float(x.std())
    row["x_min"] = float(x.min())
    row["x_p1"] = float(np.percentile(x, 1))
    row["worst_3yr_B3_over_B0"] = float((o["B3"] / inp["B0"]).min())
    return row, o


def k(v):
    return f"${v / 1000:,.0f}k"


def main():
    os.makedirs(OUT, exist_ok=True)
    inp = C.inputs()
    say(f"M3 branch Monte Carlo | run {C.stamp()} | numbers.yaml sha256 {inp['numbers_sha'][:12]} (Gate A lock)")
    say(f"  inputs: B0 = ${inp['B0']:,.2f} (stock fund, 2 Jan 2028, Nov-15 basis), F = ${inp['F']:,.0f}, s = 1/2, "
        f"curve {inp['curve_date']}; JPM AC World median {C.JPM_COMPOUND:.2%}, sd log {C.SIG_L:.6f}")
    c, rej = t_scale()
    say(f"  T: nu = {NU_T}, truncation |x - mu| <= {TRUNC} sd, calibrated scale c = {c:.7f} ({c / C.SIG_L:.4f} sd), "
        f"{rej:.4%} of raw draws discarded")
    post = bayes_fit(force="--refit" in sys.argv)
    rows, outs = [], {}
    for m in ["L", "T", "BOOT", "BAYES", "BOOT-raw", "BOOT-b1", "BOOT-b60", "BAYES-hist"]:
        x = paths(m)
        r, o = summarise(m, x, inp)
        rows.append(r)
        outs[m] = (x, o)
        say(f"  {m:10s} top 2031 p5/p50/p95 {k(r['U_p5'])} / {k(r['U_p50'])} / {k(r['U_p95'])} | gift 2033 "
            f"{k(r['G_p5'])} / {k(r['G_p50'])} / {k(r['G_p95'])} | kept {k(r['K_p5'])} / {k(r['K_p50'])} / "
            f"{k(r['K_p95'])} | P(top) {r['P_top_reached']:.1%} | P(upper half) {r['P_upper_half']:.2%} | "
            f"annual log mean {r['x_mean']:.4f} sd {r['x_sd']:.4f}")
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT, "summary.csv"), index=False)

    # analytic checks for L (M3_SPEC section 6)
    L = df.set_index("model").loc["L"]
    med_top = inp["F"] + 0.5 * inp["B0"] * np.exp(3 * C.MU_L)
    p_top = stats.norm.cdf(np.sqrt(2) * C.MU_L / C.SIG_L)
    say(f"  check L: median top {L['U_p50']:,.0f} vs analytic {med_top:,.0f}; P(top) {L['P_top_reached']:.4f} vs "
        f"analytic {p_top:.4f}")
    assert abs(L["U_p50"] / med_top - 1) < 0.002 and abs(L["P_top_reached"] - p_top) < 0.005
    assert (df["P_G_within_range"] == 1.0).all()

    # range confidence table
    rc = []
    for m in HEADLINE:
        r = df.set_index("model").loc[m]
        rc.append({"model": m, "label": C.LABEL[m], "bottom_usd": inp["F"],
                   "bottom_confidence": "certain by construction if: floor pays face; 2028 deposit arrived; gift capped; "
                                        "no fee from the floor",
                   "top_median_usd": r["U_p50"], "top_p5_usd": r["U_p5"], "top_p95_usd": r["U_p95"],
                   "P_gift_reaches_top": r["P_top_reached"], "P_gift_upper_half": r["P_upper_half"],
                   "gift_p5_usd": r["G_p5"], "gift_p50_usd": r["G_p50"], "gift_p95_usd": r["G_p95"],
                   "P_fund_below_cost_2031": r["P_B3_below_B0"]})
    pd.DataFrame(rc).to_csv(os.path.join(OUT, "range_confidence.csv"), index=False)

    # conditional P(top) for BOOT (serial dependence check)
    cond = []
    for m in ("BOOT", "BOOT-b60", "L"):
        o = outs[m][1]
        lo = o["B3"] < np.median(o["B3"])
        top = o["B5"] >= o["B3"]
        cond.append({"model": m, "P_top_all": top.mean(), "P_top_given_B3_below_median": top[lo].mean(),
                     "P_top_given_B3_above_median": top[~lo].mean()})
        say(f"  {m:8s} P(top) {top.mean():.1%}; if the fund is below its median in 2031 {top[lo].mean():.1%}, "
            f"above {top[~lo].mean():.1%}")
    pd.DataFrame(cond).to_csv(os.path.join(OUT, "conditional_top.csv"), index=False)

    # posterior table
    pr = []
    for i, v in enumerate(("m_h", "sigma", "nu")):
        a = post[v]
        pr.append({"param": v, "mean": a.mean(), "sd": a.std(), "p5": np.percentile(a, 5), "p50": np.median(a),
                   "p95": np.percentile(a, 95), "r_hat": post["r_hat"][i], "ess_bulk": post["ess_bulk"][i]})
    sd_post = post["sigma"] * np.sqrt(post["nu"] / (post["nu"] - 2))
    pr.append({"param": "sd_implied", "mean": sd_post.mean(), "sd": sd_post.std(), "p5": np.percentile(sd_post, 5),
               "p50": np.median(sd_post), "p95": np.percentile(sd_post, 95), "r_hat": np.nan, "ess_bulk": np.nan})
    pd.DataFrame(pr).to_csv(os.path.join(OUT, "bayes_posterior.csv"), index=False)
    say("  BAYES posterior (Shiller annual 1871-2025): " + "; ".join(
        f"{p['param']} {p['mean']:.4f} (90% {p['p5']:.4f}-{p['p95']:.4f})" for p in pr))

    # reconcile with insight_v1 E6 (25 Sep basis)
    b0_e6 = 7_736 * 1.045 + 150_000 - 150_000 / 1.0498 ** 5
    xL = outs["L"][0]
    o6 = C.rule(xL, b0_e6, inp["F"])
    e6 = {"gift": (165, 174, 188), "kept": (16, 32, 66), "total": (182, 207, 250), "top_median": 175, "P_top": 0.73}
    rec = []
    for lab, arr, ref in (("gift", "G", e6["gift"]), ("kept", "K", e6["kept"]), ("total", "T", e6["total"])):
        for p, rv in zip((5, 50, 95), ref):
            rec.append({"measure": f"{lab}_p{p}", "E6_25sep_k": rv,
                        "L_E6_basis_k": round(np.percentile(o6[arr], p) / 1000, 1),
                        "L_28sep_basis_k": round(np.percentile(outs['L'][1][arr], p) / 1000, 1)})
    rec.append({"measure": "top_median", "E6_25sep_k": 175, "L_E6_basis_k": round(np.median(o6["U"]) / 1000, 1),
                "L_28sep_basis_k": round(L["U_p50"] / 1000, 1)})
    rec.append({"measure": "P_top_reached", "E6_25sep_k": 0.73, "L_E6_basis_k": round(float(np.mean(o6["B5"] >= o6["B3"])), 3),
                "L_28sep_basis_k": round(L["P_top_reached"], 3)})
    pd.DataFrame(rec).to_csv(os.path.join(OUT, "reconcile_E6.csv"), index=False)
    say(f"  reconcile E6: B0 on the E6 basis ${b0_e6:,.0f} vs ${inp['B0']:,.0f} now; table in reconcile_E6.csv")

    figures(df, outs, inp)
    proposed(df, inp)
    open(os.path.join(OUT, "run_log.txt"), "w").write("\n".join(LOG) + "\n")


# ------------------------------------------------------------------ figures
def figures(df, outs, inp):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    C.style(plt)
    d = df.set_index("model")
    order = ["BAYES", "BOOT", "T", "L"]

    # 1. the 2031 range as seen today
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    for i, m in enumerate(order):
        r = d.loc[m]
        y = i
        ax.plot([inp["F"] / 1e3, r["U_p50"] / 1e3], [y, y], color=C.GRID, lw=1.5, zorder=1)
        ax.plot([inp["F"] / 1e3] * 2, [y - 0.28, y + 0.28], color=C.INK, lw=3, solid_capstyle="round")
        ax.plot([r["U_p5"] / 1e3, r["U_p95"] / 1e3], [y, y], color=C.COL[m], lw=3, alpha=0.45, solid_capstyle="round")
        ax.plot([r["U_p25"] / 1e3, r["U_p75"] / 1e3], [y, y], color=C.COL[m], lw=8, solid_capstyle="round")
        ax.plot(r["U_p50"] / 1e3, y, "o", ms=9, color=C.SURFACE, mec=C.COL[m], mew=2.5)
        ax.text(r["U_p95"] / 1e3 + 0.8, y, f"top: median {k(r['U_p50'])}\n90% of paths {k(r['U_p5'])}-{k(r['U_p95'])}",
                va="center", fontsize=8, color=C.INK)
    ax.set_yticks(range(len(order)), [C.LABEL[m] for m in order])
    ax.set_xlabel("U.S. dollars (thousands), Laura's plan")
    ax.set_xlim(147, 207)
    ax.set_ylim(-0.6, len(order) - 0.4)
    ax.text(inp["F"] / 1e3 + 0.6, -0.5, "bottom = $150k floor (face value)", fontsize=8, color=C.INK, va="center")
    ax.set_title("The 2031 range as seen today: the bottom is fixed, only the top moves")
    ax.grid(axis="y", visible=False)
    C.footer(fig, "MODEL. Top = floor + half the stock fund on 1 Jan 2031. Thick bar = middle 50% of paths, thin bar = "
                  "90%, ring = median.\n200,000 paths per model; seed 20260930; 28 Sep 2026 Treasury curve. WS2 M3.")
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_M3_top2031.png"), dpi=160)
    plt.close(fig)

    # 2. the 2033 gift: cumulative distribution (the cap makes a jump at the top)
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    for m in ["L", "T", "BOOT", "BAYES"]:
        g = np.sort(outs[m][1]["G"]) / 1e3
        yy = np.arange(1, len(g) + 1) / len(g)
        step = max(1, len(g) // 4000)
        ax.plot(g[::step], yy[::step], color=C.COL[m], ls=C.LS[m], label=C.LABEL[m])
    ax.axvline(inp["F"] / 1e3, color=C.INK, lw=1.2)
    ax.text(inp["F"] / 1e3 + 0.4, 0.92, "floor $150k", fontsize=8.5)
    ax.set_xlim(148, 205)
    ax.set_xlabel("2033 gift, U.S. dollars (thousands), Laura's plan")
    ax.set_ylabel("share of paths with a gift at or below this")
    ax.set_title("The 2033 gift never falls below the floor")
    ax.legend(loc="lower right", fontsize=8.5)
    C.footer(fig, "MODEL. Gift = floor + half of the lower of the fund's 2031 and 2033 values (capped at the announced "
                  "top). Seed 20260930. WS2 M3.")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_M3_gift2033.png"), dpi=160)
    plt.close(fig)

    # 3. where in the range the gift lands
    fig, ax = plt.subplots(figsize=(8.2, 3.4))
    for i, m in enumerate(order):
        r = d.loc[m]
        a, b = r["P_top_reached"], r["P_upper_half"] - r["P_top_reached"]
        c_ = 1 - r["P_upper_half"]
        ax.barh(i, a * 100, color=C.COL[m], edgecolor=C.SURFACE, linewidth=2)
        ax.barh(i, b * 100, left=a * 100, color=C.COL[m], alpha=0.45, edgecolor=C.SURFACE, linewidth=2)
        ax.barh(i, c_ * 100, left=(a + b) * 100, color=C.INK2, edgecolor=C.SURFACE, linewidth=2)
        ax.text(a * 50, i, f"at the top {a:.0%}", ha="center", va="center", fontsize=8.5, color="white",
                fontweight="bold")
        ax.text(a * 100 + b * 50, i, f"upper half {b:.0%}", ha="center", va="center", fontsize=8.5, color=C.INK)
        ax.text(101, i, f"lower half {c_:.1%}", va="center", fontsize=8.5, color=C.INK)
    ax.set_yticks(range(len(order)), [C.LABEL[m] for m in order])
    ax.set_xlim(0, 118)
    ax.set_xlabel("share of paths (%)")
    ax.set_title("Where in the 2031 range the 2033 gift lands")
    ax.grid(visible=False)
    C.footer(fig, "MODEL. 'At the top' = the stock fund is no lower on 1 Jan 2033 than on 1 Jan 2031. Seed 20260930. "
                  "WS2 M3.")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(os.path.join(OUT, "fig_M3_where_in_range.png"), dpi=160)
    plt.close(fig)


# ------------------------------------------------------------------ proposed numbers.yaml entries (WS0/WS1 to review)
def proposed(df, inp):
    import yaml
    d = df.set_index("model")
    base = {"scale": "laura_plan", "status": "MODEL", "curve_date": inp["curve_date"],
            "maturity_convention": "ladder and leftover on the Nov-15 STRIPS basis (Gate A headline)",
            "instrument_basis": "stock fund B0 = $40,736 (2 Jan 2028); floor $150,000 face; s = 1/2; no fees",
            "method": "rab/models/M3_SPEC.md", "source": "rab/models/m3_branch.py -> rab/results/M3/summary.csv",
            "as_of": inp["curve_date"]}
    r5 = lambda v: int(round(v / 5000) * 5)
    r1 = lambda v: int(round(v / 1000))
    ent = {}
    lo = min(d.loc[m, "U_p50"] for m in DECISION)
    hi = max(d.loc[m, "U_p50"] for m in DECISION)
    ent["m3.top2031_median"] = {**base, "valuation_date": "2031-01-01",
                                "value": {m: round(float(d.loc[m, "U_p50"])) for m in HEADLINE},
                                "unit": "USD", "quote_as": (f"a top of about ${r1(lo)},000" if r1(lo) == r1(hi) else
                                                            f"a top of about ${r1(lo)},000-${r1(hi)},000")
                                + " in a typical case (MODEL, median in each of three return models)"}
    ent["m3.top2031_90pct"] = {**base, "valuation_date": "2031-01-01",
                               "value": {m: [round(float(d.loc[m, 'U_p5'])), round(float(d.loc[m, 'U_p95']))] for m in HEADLINE},
                               "unit": "USD (p5, p95)", "quote_as": "the top will probably be between about $"
                               f"{r5(min(d.loc[m, 'U_p5'] for m in DECISION))}k and ${r5(max(d.loc[m, 'U_p95'] for m in DECISION))}k (MODEL)"}
    ent["m3.p_top_reached"] = {**base, "valuation_date": "2033-01-01",
                               "value": {m: round(float(d.loc[m, "P_top_reached"]), 3) for m in HEADLINE},
                               "unit": "probability", "quote_as": "about 3 in 4 (MODEL)"}
    assert all(0.70 <= d.loc[m, "P_top_reached"] <= 0.78 for m in HEADLINE), "re-word the 3-in-4 quote"
    ent["m3.p_upper_half"] = {**base, "valuation_date": "2033-01-01",
                              "value": {m: round(float(d.loc[m, "P_upper_half"]), 4) for m in HEADLINE},
                              "unit": "probability", "quote_as": "at least halfway up the range in almost every case (MODEL)"}
    ent["m3.gift2033"] = {**base, "valuation_date": "2033-01-01",
                          "value": {m: [round(float(d.loc[m, f"G_p{p}"])) for p in (5, 50, 95)] for m in HEADLINE},
                          "unit": "USD (p5, p50, p95)", "quote_as": "a 2033 gift of about $"
                          f"{r1(min(d.loc[m, 'G_p50'] for m in DECISION))},000 in a typical case, never below $150,000 (MODEL)"}
    ent["m3.kept2033"] = {**base, "valuation_date": "2033-01-01",
                          "value": {m: [round(float(d.loc[m, f"K_p{p}"])) for p in (5, 50, 95)] for m in HEADLINE},
                          "unit": "USD (p5, p50, p95)", "quote_as": "Laura keeps about $"
                          f"{int(np.floor(min(d.loc[m, 'K_p50'] for m in DECISION) / 5000) * 5)}k-"
                          f"${int(np.ceil(max(d.loc[m, 'K_p50'] for m in DECISION) / 5000) * 5)}k in a typical case (MODEL)"}
    ent["m3.range_confidence"] = {**base, "valuation_date": "2033-01-01", "value": 1.0, "unit": "probability",
                                  "status": "BY CONSTRUCTION",
                                  "quote_as": "certain by construction if the floor holdings pay, the 2028 deposit arrives, "
                                              "the gift is capped and no fee is taken from the floor",
                                  "note": "Not a model output; M4 quantifies the floor-delivery condition."}
    hdr = ("# WS2 proposed entries for rab/numbers.yaml (NOT the Gate A file). WS1/WS0 review and merge; WS2 does not\n"
           "# write rab/numbers.yaml (PM-35). Values are MODEL outputs of rab/models/m3_branch.py.\n")
    with open(os.path.join(OUT, "numbers_proposed.yaml"), "w") as f:
        f.write(hdr)
        yaml.safe_dump({"proposed": ent}, f, sort_keys=False, width=120, allow_unicode=False)


if __name__ == "__main__":
    main()
