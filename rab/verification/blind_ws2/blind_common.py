"""Blind rebuild of WS2 models M3, M4, M8 from their SPEC files only (Gate B).

Shared pieces: the D1 par-curve method (M1_METHOD.md A1, incorporated by reference in M8_SPEC section 1), the
four return models of M3_SPEC section 3, and the Root-and-Branch outcome rule of M3_SPEC section 2.

Blind protocol: the builder read M3_SPEC.md, M4_SPEC.md, M8_SPEC.md, M1_METHOD.md sections 1-2 and A (the curve
recipe that M8 cites), rab/numbers.yaml and rab/data/. No file under rab/models/*.py, rab/results/ or
research/insight_v1/scripts was opened. AI-generated research (Claude Code) for Team Caplet; no deliverable text.

Environment note: pytensor's C compiler fails on this Mac (Apple clang 21: "ld: library 'd64' not found"), so the
BAYES model runs pymc with PYTENSOR_FLAGS=cxx= (pure-Python ops). Same maths, slower, still under a minute here.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy import integrate, optimize, stats

os.environ.setdefault("PYTENSOR_FLAGS", "cxx=")

HERE = Path(__file__).resolve().parent
WS = HERE.parents[2]  # worktree root: blind -> verification -> rab -> <worktree>
DATA = WS / "rab" / "data"
OUT = HERE / "out"
PATHS_DIR = OUT / "paths"

SEED = 20260930
N_PATHS = 200_000

# ---- locked inputs (rab/numbers.yaml, Gate A) and spec constants -----------------------------------------------
CURVE_DATE = dt.date(2026, 9, 28)
B0 = 40_736.193940603116          # laura.stock_fund_2028_usd.strips (full precision, M3_SPEC s1)
F_FLOOR = 150_000.0               # floor face
S_ADOPTED = 0.5                   # share promised at the top (D6 default)
MU_L = math.log(1.07)             # JPM LTCMA 2026 AC World compound 7.00%
SIG_L = math.sqrt(2.0 * math.log(1.0828 / 1.07))  # lognormal fit to arithmetic 8.28%
Y1_PAR = 0.0459                   # 1-year par, 28 Sep 2026
Y5_PAR = 0.0506                   # 5-year par, 28 Sep 2026
FEE_FLOOR = 0.0007                # iBond ETF expense ratio
DEPOSIT_2027 = 300_000.0
DEPOSIT_2028 = 150_000.0

# Gate A check values (rab/numbers.yaml, LOCKED)
LOCKED = {
    "V0_nov15": 289_119.20, "VA_nov15": 292_418.11, "headroom_nov15": 7_581.89, "breakeven_bp_nov15": 26.2,
    "V0_exact": 287_016.47, "VA_exact": 290_291.38, "breakeven_bp_exact": 33.2,
    "V2028_nov15": 306_525, "V2028_exact": 304_295, "floor_cost_2028": 117_194, "B0": 40_736,
}

PCTS = [5, 10, 25, 50, 75, 90, 95]


# ---- D1 curve ----------------------------------------------------------------------------------------------------
TENOR_YEARS = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": 0.25, "6 Mo": 0.5, "1 Yr": 1.0, "2 Yr": 2.0, "3 Yr": 3.0,
               "5 Yr": 5.0, "7 Yr": 7.0, "10 Yr": 10.0, "20 Yr": 20.0, "30 Yr": 30.0}


def load_par_curve(curve_date: dt.date = CURVE_DATE):
    """Return (tenors_years, par_yields_percent) for one row of the Treasury daily par-curve CSV (blank tenors skipped)."""
    path = DATA / "treasury_par_2000_2026" / f"{curve_date.year}.csv"
    want = curve_date.strftime("%m/%d/%Y")
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            if row["Date"] == want:
                tenors, ys = [], []
                for col, t in TENOR_YEARS.items():
                    v = row.get(col, "").strip()
                    if v:
                        tenors.append(t)
                        ys.append(float(v))
                return np.array(tenors), np.array(ys)
    raise KeyError(f"{want} not in {path}")


class D1Curve:
    """M1_METHOD.md A1: linear par interpolation on a half-year grid, semiannual bootstrap, log-linear DF.

    All methods accept a vector of parallel shifts in basis points and return arrays shaped (n_shift, ...).
    """

    def __init__(self, tenors: np.ndarray, par_pct: np.ndarray, ref_date: dt.date = CURVE_DATE):
        self.ref = ref_date
        self.t_grid = 0.5 * np.arange(1, 61)  # 0.5 .. 30
        # np.interp is flat beyond the first and last tenor, as A1 step 2 requires
        self.base_par = np.interp(self.t_grid, tenors, par_pct / 100.0)

    def tau(self, d: dt.date) -> float:
        return (d - self.ref).days / 365.25

    def ln_df_grid(self, shift_bp) -> np.ndarray:
        shift = np.atleast_1d(np.asarray(shift_bp, dtype=float))
        p = self.base_par[None, :] + shift[:, None] / 10_000.0  # a parallel shift adds the same amount everywhere
        m = shift.shape[0]
        df = np.empty((m, 60))
        cum = np.zeros(m)
        for j in range(60):
            c = p[:, j] / 2.0
            df[:, j] = (1.0 - c * cum) / (1.0 + c)
            cum = cum + df[:, j]
        return np.concatenate([np.zeros((m, 1)), np.log(df)], axis=1)  # knots t = 0, 0.5, ..., 30

    def df(self, dates, shift_bp=0.0) -> np.ndarray:
        """Discount factors, shape (n_shift, n_dates)."""
        dates = list(dates) if isinstance(dates, (list, tuple)) else [dates]
        taus = np.array([self.tau(d) for d in dates])
        ln_df = self.ln_df_grid(shift_bp)
        x = taus / 0.5
        idx = np.clip(np.floor(x), 0, 59).astype(int)
        w = x - idx
        val = ln_df[:, idx] * (1.0 - w) + ln_df[:, idx + 1] * w
        val = np.where(taus[None, :] >= 30.0, ln_df[:, 60][:, None], val)  # flat ln DF beyond 30 years
        return np.exp(val)


NOV15_DATES = [dt.date(y, 11, 15) for y in range(2032, 2042)]   # STRIPS maturities (headline basis)
EXACT_DATES = [dt.date(y, 1, 1) for y in range(2033, 2043)]     # the payment dates (not buyable)
DATE_2027 = dt.date(2027, 1, 1)
DATE_2028 = dt.date(2028, 1, 1)


class Ladder:
    """The ten $50,000 payments on the D1 curve, as a function of a parallel shift (bp)."""

    def __init__(self, curve: D1Curve, dates=NOV15_DATES, payment: float = 50_000.0):
        self.curve, self.dates, self.payment = curve, dates, payment

    def v0(self, shift_bp=0.0) -> np.ndarray:
        return self.payment * self.curve.df(self.dates, shift_bp).sum(axis=1)

    def value_at(self, when: dt.date, shift_bp=0.0) -> np.ndarray:
        return self.v0(shift_bp) / self.curve.df([when], shift_bp)[:, 0]

    def breakeven_fall_bp(self, deposit: float = DEPOSIT_2027) -> float:
        f = lambda b: float(self.value_at(DATE_2027, b)[0]) - deposit
        b = optimize.brentq(f, -400.0, 0.0, xtol=1e-4)
        return -b


def curve_checks() -> dict:
    """Reproduce the Gate A numbers from the raw curve (exact to the cent is expected)."""
    tenors, ys = load_par_curve()
    curve = D1Curve(tenors, ys)
    nov, ex = Ladder(curve, NOV15_DATES), Ladder(curve, EXACT_DATES)
    va = float(nov.value_at(DATE_2027)[0])
    out = {
        "V0_nov15": float(nov.v0()[0]), "VA_nov15": va, "headroom_nov15": DEPOSIT_2027 - va,
        "breakeven_bp_nov15": nov.breakeven_fall_bp(),
        "V0_exact": float(ex.v0()[0]), "VA_exact": float(ex.value_at(DATE_2027)[0]),
        "breakeven_bp_exact": ex.breakeven_fall_bp(),
        "V2028_nov15": float(nov.value_at(DATE_2028)[0]), "V2028_exact": float(ex.value_at(DATE_2028)[0]),
        "floor_cost_2028": DEPOSIT_2028 / (1 + Y5_PAR) ** 5,
    }
    leftover = DEPOSIT_2027 - va
    out["B0"] = leftover * (1 + Y1_PAR) + DEPOSIT_2028 - DEPOSIT_2028 / (1 + Y5_PAR) ** 5
    return out


# ---- return models (M3_SPEC section 3) ---------------------------------------------------------------------------
def rng_for(tag: str) -> np.random.Generator:
    """Independent, reproducible stream per model: SeedSequence(SEED, hash(tag))."""
    h = int.from_bytes(tag.encode(), "little") % (2**31 - 1)
    return np.random.default_rng(np.random.SeedSequence([SEED, h]))


def t_scale_c(nu: float = 4.0, k_sig: float = 5.0, sig: float = SIG_L) -> tuple[float, float]:
    """Scale c so that c * t_nu truncated at |c t| > k_sig * sig has standard deviation exactly sig.

    Returns (c, share of raw draws discarded)."""
    def trunc_var(a):
        num, _ = integrate.quad(lambda t: t * t * stats.t.pdf(t, nu), -a, a, limit=200)
        return num / (1 - 2 * stats.t.sf(a, nu))

    def g(c):
        a = k_sig * sig / c
        return c * c * trunc_var(a) - sig * sig

    c = optimize.brentq(g, 0.03, 0.3, xtol=1e-10)
    return c, 2 * stats.t.sf(k_sig * sig / c, nu)


def paths_L(rng: np.random.Generator, n: int, mu: float = MU_L, sig: float = SIG_L) -> np.ndarray:
    return rng.normal(mu, sig, size=(n, 5))


def paths_T(rng: np.random.Generator, n: int, c: float, nu: float = 4.0, mu: float = MU_L,
            sig: float = SIG_L, k_sig: float = 5.0) -> np.ndarray:
    x = mu + c * rng.standard_t(nu, size=(n, 5))
    bad = np.abs(x - mu) > k_sig * sig
    while bad.any():
        x[bad] = mu + c * rng.standard_t(nu, size=int(bad.sum()))
        bad = np.abs(x - mu) > k_sig * sig
    return x


def load_shiller_monthly() -> np.ndarray:
    """Monthly nominal total returns r_nominal, rows 1871-01 .. 2025-12 (1,860 values)."""
    import pandas as pd
    df = pd.read_csv(DATA / "ws2_returns" / "shiller_monthly.csv")
    df = df[(df["month"] >= "1871-01") & (df["month"] <= "2025-12")]
    r = df["r_nominal"].to_numpy(dtype=float)
    assert r.shape[0] == 1860 and np.isfinite(r).all(), r.shape
    return r


def load_shiller_annual() -> np.ndarray:
    import pandas as pd
    df = pd.read_csv(DATA / "ws2_returns" / "shiller_annual.csv")
    z = df["log_r_nominal"].to_numpy(dtype=float)
    assert z.shape[0] == 155 and np.isfinite(z).all(), z.shape
    return z


def paths_BOOT(rng: np.random.Generator, n: int, r_monthly: np.ndarray, mean_block: float = 24.0,
               recentre: bool = True, mu: float = MU_L, months: int = 60) -> np.ndarray:
    """Politis-Romano stationary bootstrap of monthly log returns, summed to 5 annual log returns."""
    y = np.log1p(r_monthly)
    if recentre:
        y = y - y.mean() + mu / 12.0
    nm = y.shape[0]
    p_jump = 1.0 / mean_block
    idx = np.empty((n, months), dtype=np.int64)
    idx[:, 0] = rng.integers(0, nm, size=n)
    for m in range(1, months):
        jump = rng.random(n) < p_jump
        fresh = rng.integers(0, nm, size=n)
        idx[:, m] = np.where(jump, fresh, (idx[:, m - 1] + 1) % nm)  # index n is followed by index 1
    return y[idx].reshape(n, months // 12, 12).sum(axis=2)


def fit_bayes_history(z_annual: np.ndarray, seed: int = SEED):
    """M3_SPEC s3 BAYES part 1: StudentT fit to 155 Jan-Jan log returns. Returns (posterior dict, diagnostics)."""
    import arviz as az
    import pymc as pm

    with pm.Model():
        m_h = pm.Normal("m_h", mu=0.08, sigma=0.05)
        sigma = pm.HalfNormal("sigma", sigma=0.30)
        nu_p = pm.Gamma("nu_prime", alpha=2.0, beta=0.1)  # rate 0.1
        nu = pm.Deterministic("nu", 2.0 + nu_p)
        pm.StudentT("z", nu=nu, mu=m_h, sigma=sigma, observed=z_annual)
        idata = pm.sample(draws=1000, tune=1000, chains=4, cores=4, target_accept=0.9, random_seed=seed,
                          progressbar=False, compute_convergence_checks=False)
    summ = az.summary(idata, var_names=["m_h", "sigma", "nu"])  # arviz 1.x: no hdi_prob keyword
    post = {k: idata.posterior[k].values.reshape(-1) for k in ("m_h", "sigma", "nu")}
    assert post["m_h"].shape[0] == 4000
    ok = bool((summ["r_hat"] <= 1.01).all() and (summ["ess_bulk"] >= 400).all())
    return post, summ, ok


def paths_BAYES(rng: np.random.Generator, n: int, post: dict, mu_f_mean: float = math.log(1.07),
                mu_f_sd: float = 0.015, hist_mean: bool = False, k_sig: float = 5.0) -> np.ndarray:
    """M3_SPEC s3 BAYES part 3: one posterior draw and one forward mean per path; t shocks with 5-sd redraw."""
    j = rng.integers(0, post["m_h"].shape[0], size=n)
    sig_j, nu_j, mh_j = post["sigma"][j], post["nu"][j], post["m_h"][j]
    mu_f = mh_j if hist_mean else rng.normal(mu_f_mean, mu_f_sd, size=n)
    bound = k_sig * sig_j * np.sqrt(nu_j / (nu_j - 2.0))
    t = rng.standard_t(nu_j[:, None], size=(n, 5))
    x = mu_f[:, None] + sig_j[:, None] * t
    bad = np.abs(x - mu_f[:, None]) > bound[:, None]
    while bad.any():
        rows = np.nonzero(bad)[0]
        t_new = rng.standard_t(nu_j[rows])
        x[bad] = mu_f[rows] + sig_j[rows] * t_new
        bad = np.abs(x - mu_f[:, None]) > bound[:, None]
    return x


# ---- the rule (M3_SPEC section 2) -------------------------------------------------------------------------------
def outcomes(x: np.ndarray, b0: float = B0, f: float = F_FLOOR, s: float = S_ADOPTED) -> dict:
    b3 = b0 * np.exp(x[:, :3].sum(axis=1))
    b5 = b3 * np.exp(x[:, 3:].sum(axis=1))
    m = np.minimum(b5, b3)
    return {"B3": b3, "B5": b5, "U": f + s * b3, "G": f + s * m, "K": b5 - s * m, "T": f + b5,
            "p": np.minimum(b5 / b3, 1.0)}


def pct_row(a: np.ndarray, prefix: str) -> dict:
    q = np.percentile(a, PCTS)
    row = {f"{prefix}_p{p}": float(v) for p, v in zip(PCTS, q)}
    row[f"{prefix}_mean"] = float(a.mean())
    return row


def save_paths(tag: str, x: np.ndarray) -> None:
    PATHS_DIR.mkdir(parents=True, exist_ok=True)
    np.save(PATHS_DIR / f"{tag}.npy", x.astype(np.float64))


def load_paths(tag: str) -> np.ndarray:
    p = PATHS_DIR / f"{tag}.npy"
    if not p.exists():
        raise FileNotFoundError(f"{p} missing: run blind_m3.py first")
    return np.load(p)


def write_json(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))


if __name__ == "__main__":
    chk = curve_checks()
    print("Gate A reproduction (blind curve):")
    worst = 0.0
    for k, v in chk.items():
        ref = LOCKED[k]
        d = v - ref
        worst = max(worst, abs(d) if k.startswith(("V", "B", "floor", "headroom")) and k not in ("V2028_nov15", "V2028_exact", "floor_cost_2028", "B0") else 0)
        print(f"  {k:22s} blind {v:14.2f}  locked {ref:12.2f}  diff {d:+.2f}")
    c, disc = t_scale_c()
    print(f"T scale c = {c:.7f} (spec 0.1162464), discarded share {100*disc:.3f}% (spec 0.268%)")
