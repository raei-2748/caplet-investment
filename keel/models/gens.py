"""AI-generated (Claude Code), Tue 27 Oct 2026. MODEL. Market-path generators for the Model Suite (see xr_core.py).

  lognormal(N)   the house model: J.P. Morgan 7.5% compound, 16.78% vol, normal yearly moves; yields a random walk
                 of 1 point a year; independent [A06] [A04]
  regime(N)      fat tails + regime switching: a two-state Markov model (calm / storm) fitted to 152 years of US
                 stocks and 70 years of 10-year yields, Student-t shocks, storms pull yields down [A30]-[A33]
  bootstrap(N)   stationary block bootstrap of real months 1871-2023 (stocks, yields and prices together, so every
                 crash keeps its own rates and inflation); stock level reset to 7.5% unless raw=True [A34]
  history()      every real start month: 1 Jan 2027 is mapped to that month and history runs forward [A35]
"""
import csv
import pathlib

import numpy as np

from xr_core import DATA, EQ_G, EQ_VOL, H0, M, ROOT, curve

RATE_VOL = 1.00                   # pp a year [A04]
Y10 = float(curve(10))            # today's 10-year par yield, 4.96%


# ---------------------------------------------------------------- real data
def shiller():
    """Monthly (date, log total return, 10y yield %, CPI), Jan 1871 - Jun 2023 (dividends end there) [A34]."""
    rows = [r for r in csv.DictReader(open(DATA / "shiller_monthly.csv"))]
    rows = [r for r in rows if float(r["Dividend"]) > 0 and float(r["Consumer Price Index"]) > 0]
    d = [r["Date"][:7] for r in rows]
    P = np.array([float(r["SP500"]) for r in rows]); D = np.array([float(r["Dividend"]) for r in rows])
    Y = np.array([float(r["Long Interest Rate"]) for r in rows]); C = np.array([float(r["Consumer Price Index"]) for r in rows])
    eq = np.log((P[1:] + D[1:] / 12) / P[:-1])
    return {"date": d, "eq": eq, "y": Y, "dy": np.diff(Y), "cpi": np.diff(np.log(C)), "P": P}


def gs10():
    rows = list(csv.DictReader(open(ROOT / "keel/library/ips_numbers_2026-10/fred_GS10_monthly.csv")))
    return [r["observation_date"][:7] for r in rows], np.array([float(r["GS10"]) for r in rows])


def twd():
    rows = list(csv.DictReader(open(DATA / "twd_per_usd_monthly.csv")))
    return [r["Date"][:7] for r in rows], np.array([float(r["TWD_per_USD"]) for r in rows])


def cpi_us():
    rows = list(csv.DictReader(open(DATA / "cpi_us_monthly.csv")))
    return [r["Date"][:7] for r in rows], np.array([float(r["Index"]) for r in rows])


# ---------------------------------------------------------------- inflation and FX pieces
def _cpi_ar1(rng, N, mean=0.025):
    """US inflation: AR(1) on monthly log CPI changes fitted 1953-2023, mean reset to J.P. Morgan's 2.5% [A10]."""
    h = shiller(); i0 = h["date"].index("1953-01"); x = h["cpi"][i0:]
    xm = x - x.mean(); phi = (xm[1:] @ xm[:-1]) / (xm[:-1] @ xm[:-1]); sd = np.std(xm[1:] - phi * xm[:-1])
    out = np.zeros((N, M)); prev = np.zeros(N); mu = np.log(1 + mean) / 12
    for m in range(M):
        prev = phi * prev + rng.normal(0, sd, N); out[:, m] = mu + prev
    return out


def _fx_boot(rng, N, block=12, drift=False):
    """TWD per USD: stationary bootstrap of real monthly moves Oct 1983 - Sep 2026; drift removed unless drift=True [A11]."""
    _, x = twd(); r = np.diff(np.log(x))
    if not drift:
        r = r - r.mean()
    return r[_stationary(rng, N, len(r), block)]


def _stationary(rng, N, n, block):
    """Politis-Romano stationary bootstrap indices (N, M)."""
    idx = np.empty((N, M), int); cur = rng.integers(0, n, N)
    for m in range(M):
        new = rng.random(N) < 1 / block
        cur = np.where(new, rng.integers(0, n, N), (cur + 1) % n); idx[:, m] = cur
    return idx


# ---------------------------------------------------------------- generators
def lognormal(N, seed=20261027, rho=0.0):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(N, M))
    dyz = rng.normal(size=(N, M))
    eqz = rho * dyz + np.sqrt(1 - rho ** 2) * z           # rho > 0: stocks fall when yields fall [A09]
    return {"s0": rng.normal(0, RATE_VOL * np.sqrt(H0), N),
            "dy": dyz * RATE_VOL / np.sqrt(12),
            "eq": np.log(1 + EQ_G) / 12 + EQ_VOL / np.sqrt(12) * eqz,
            "cpi": _cpi_ar1(rng, N), "fx": _fx_boot(rng, N)}


def fit_regimes(x, iters=300):
    """Hamilton two-state Gaussian Markov-switching model by EM. Returns means, sds, transition matrix, smoothed P."""
    n = len(x); mu = np.array([x.mean() + .005, x.mean() - .02]); sd = np.array([x.std() * .7, x.std() * 2])
    P = np.array([[.98, .02], [.08, .92]])
    for _ in range(iters):
        lik = np.exp(-.5 * ((x[:, None] - mu) / sd) ** 2) / sd
        a = np.zeros((n, 2)); a[0] = [.8, .2]; c = np.zeros(n)
        for t in range(n):
            pr = a[t - 1] @ P if t else a[0]
            v = pr * lik[t]; c[t] = v.sum(); a[t] = v / c[t]
        b = np.ones((n, 2)); sm = np.zeros((n, 2)); xi = np.zeros((2, 2))
        for t in range(n - 2, -1, -1):
            b[t] = P @ (lik[t + 1] * b[t + 1]); b[t] /= b[t].sum()
        sm = a * b; sm /= sm.sum(1, keepdims=True)
        for t in range(n - 1):
            m_ = a[t][:, None] * P * (lik[t + 1] * b[t + 1])[None, :]; xi += m_ / m_.sum()
        P = xi / xi.sum(1, keepdims=True)
        mu = (sm * x[:, None]).sum(0) / sm.sum(0)
        sd = np.sqrt((sm * (x[:, None] - mu) ** 2).sum(0) / sm.sum(0))
    return mu, sd, P, sm, np.log(c).sum()


_REG = None


def regime_params():
    """Fit once: stock regimes on 1871-2023; yields' monthly drift and sd in each regime on 1953-2023 [A30]-[A32]."""
    global _REG
    if _REG is None:
        h = shiller(); mu, sd, P, sm, ll = fit_regimes(h["eq"])
        i0 = h["date"].index("1953-04") - 1
        w = sm[i0:, :]; dy = h["dy"][i0:]
        dmu = (w * dy[:, None]).sum(0) / w.sum(0)
        dsd = np.sqrt((w * (dy[:, None] - dmu) ** 2).sum(0) / w.sum(0))
        # kurtosis left inside each regime -> Student-t degrees of freedom by moments [A31]
        z = (h["eq"][:, None] - mu) / sd; k = ((sm * z ** 4).sum(0) / sm.sum(0))
        nu = np.clip(4 + 6 / np.maximum(k - 3, 1e-3), 4.5, 30)
        _REG = {"mu": mu, "sd": sd, "P": P, "dy_mu": dmu, "dy_sd": dsd, "nu": nu, "loglik": ll,
                "storm_share": float(sm[:, 1].mean())}
    return _REG


def regime(N, seed=20261028, target=EQ_G, level_shift=None):
    rp = regime_params(); rng = np.random.default_rng(seed)
    st = (rng.random(N) < rp["storm_share"]).astype(int)
    eq = np.zeros((N, M)); dy = np.zeros((N, M))
    for m in range(M):
        nu = rp["nu"][st]
        t = rng.standard_t(nu) * np.sqrt((nu - 2) / nu)
        eq[:, m] = rp["mu"][st] + rp["sd"][st] * t
        wmu = rp["dy_mu"] @ [1 - rp["storm_share"], rp["storm_share"]]
        dy[:, m] = rp["dy_mu"][st] - wmu + rp["dy_sd"][st] * rng.normal(size=N)
        st = np.where(rng.random(N) < rp["P"][st, 1], 1, 0)
    # reset the level: median 16-year compound return = target, shape (tails, regimes, storms' yield moves) kept [A33]
    if level_shift is None:
        g = np.median(eq.sum(1)) / M
        level_shift = np.log(1 + target) / 12 - g
    eq += level_shift
    return {"s0": rng.normal(0, RATE_VOL * np.sqrt(H0), N), "dy": dy, "eq": eq,
            "cpi": _cpi_ar1(rng, N), "fx": _fx_boot(rng, N)}


def _rel(y_ratio):
    """History's yield moves in proportion: a path of y_t / y_start becomes today's 10-year x that ratio [A35]."""
    return Y10 * (y_ratio - 1)


def bootstrap(N, seed=20261029, block=24, raw=False):
    h = shiller(); n = len(h["eq"]); rng = np.random.default_rng(seed)
    idx = _stationary(rng, N, n, block)
    eq = h["eq"][idx]
    if not raw:
        eq = eq - h["eq"].mean() + np.log(1 + EQ_G) / 12
    dl = np.diff(np.log(h["y"]))                               # monthly log change of the 10-year yield
    s0i = rng.integers(1, n, N)
    s0 = _rel(np.exp(dl[s0i] + dl[s0i - 1]))
    S = s0[:, None] + _rel(np.exp(np.cumsum(dl[idx], axis=1))) * (1 + s0[:, None] / Y10)
    dy = np.diff(np.concatenate([s0[:, None], S], axis=1), axis=1)
    return {"s0": s0, "dy": dy, "eq": eq, "cpi": h["cpi"][idx], "fx": _fx_boot(rng, N)}


def history(horizon=M, start_from="1871-03", raw=True):
    """Each real start month s: build day = s, the two months before give s0. Paths stop at June 2023."""
    h = shiller(); n = len(h["eq"]); d = h["date"]; y = h["y"]
    s_first = d.index(start_from)
    starts = [s for s in range(max(2, s_first), n) if s + horizon <= n]
    eq = np.array([h["eq"][s:s + horizon] for s in starts])
    if not raw:
        eq = eq - h["eq"].mean() + np.log(1 + EQ_G) / 12
    pad = lambda a: np.pad(a, ((0, 0), (0, M - horizon))) if horizon < M else a   # zeros: unused months
    s0 = np.array([_rel(y[s] / y[s - 2]) for s in starts])
    S = np.array([_rel(y[s:s + horizon + 1] / y[s - 2]) for s in starts])     # level path since the curve date
    return {"s0": s0, "dy": pad(np.diff(S, axis=1)), "eq": pad(eq),
            "cpi": pad(np.array([h["cpi"][s:s + horizon] for s in starts])), "start": [d[s] for s in starts]}
