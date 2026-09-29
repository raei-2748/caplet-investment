"""Blind rebuild (WS3): the D1 par-curve method, written from M5_SPEC.md section 2 only.

Tenor map: 1 Mo = 1/12 ... 30 Yr = 30; blank tenors skipped; other columns ignored.
Par grid t_j = 0.5 j, j = 1..60; linear interpolation of (tenor, yield/100), flat outside.
Bootstrap DF_j = (1 - (p_j/2) sum_{i<j} DF_i) / (1 + p_j/2).
DF(t) = exp of the linear interpolation of (0, 0), (t_j, ln DF_j); flat ln DF beyond 30 years.
Year fraction = calendar days / 365.25.
A curve with only the 10 Yr column is a flat par curve at that yield.

AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.
"""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass

import numpy as np

TENOR_YEARS = {
    "1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": 0.25, "6 Mo": 0.5,
    "1 Yr": 1.0, "2 Yr": 2.0, "3 Yr": 3.0, "5 Yr": 5.0, "7 Yr": 7.0,
    "10 Yr": 10.0, "20 Yr": 20.0, "30 Yr": 30.0,
}
TENOR_ORDER = list(TENOR_YEARS)
GRID = 0.5 * np.arange(1, 61)  # 0.5 .. 30.0
DAYS_PER_YEAR = 365.25


def yearfrac(d0: dt.date, d1: dt.date) -> float:
    """Calendar days / 365.25 (negative if d1 < d0)."""
    return (d1 - d0).days / DAYS_PER_YEAR


def yearfrac_array(d0: dt.date, dates) -> np.ndarray:
    return np.array([(d - d0).days for d in dates], dtype=float) / DAYS_PER_YEAR


def _clean_tenors(tenor_yields_pct: dict) -> tuple[np.ndarray, np.ndarray]:
    """Return (tenor years, yields as decimals) for the non-blank tenors, sorted by tenor."""
    ts, ys = [], []
    for name, t in TENOR_YEARS.items():
        v = tenor_yields_pct.get(name)
        if v is None:
            continue
        try:
            fv = float(v)
        except (TypeError, ValueError):
            continue
        if np.isnan(fv):
            continue
        ts.append(t)
        ys.append(fv / 100.0)
    if not ts:
        raise ValueError("curve has no tenors")
    order = np.argsort(ts)
    return np.asarray(ts)[order], np.asarray(ys)[order]


def par_on_grid(tenors: np.ndarray, yields: np.ndarray) -> np.ndarray:
    """Linear interpolation of the par yields onto the semiannual grid; flat outside the quoted range."""
    return np.interp(GRID, tenors, yields)


def bootstrap(p: np.ndarray) -> np.ndarray:
    """Discount factors on the grid from par yields p (decimal, semiannual coupons)."""
    p = np.asarray(p, dtype=float)
    if p.ndim == 1:
        p = p[None, :]
        squeeze = True
    else:
        squeeze = False
    n, m = p.shape
    df = np.empty((n, m))
    running = np.zeros(n)
    for j in range(m):
        c = p[:, j] / 2.0
        df[:, j] = (1.0 - c * running) / (1.0 + c)
        running += df[:, j]
    return df[0] if squeeze else df


@dataclass
class Curve:
    """One par curve, bootstrapped; df(t) for t in years from the curve date."""
    tenors: np.ndarray       # years, quoted tenors present
    yields: np.ndarray       # decimals, same order
    ln_df_knots: np.ndarray  # length 61: 0 at t=0, then ln DF_j
    t_knots: np.ndarray      # length 61: 0, 0.5, ..., 30

    @classmethod
    def from_tenors(cls, tenor_yields_pct: dict, shift_pp: float = 0.0) -> "Curve":
        """Build from a {tenor name: yield in percent} mapping; shift_pp is a parallel shift of every par yield
        (percentage points) applied before the bootstrap (M7 convention)."""
        tenors, yields = _clean_tenors(tenor_yields_pct)
        yields = yields + shift_pp / 100.0
        p = par_on_grid(tenors, yields)
        df = bootstrap(p)
        return cls(tenors=tenors, yields=yields,
                   ln_df_knots=np.concatenate([[0.0], np.log(df)]),
                   t_knots=np.concatenate([[0.0], GRID]))

    @classmethod
    def flat(cls, yield_pct: float) -> "Curve":
        return cls.from_tenors({"10 Yr": yield_pct})

    def df(self, t):
        """Discount factor at t years (scalar or array). t <= 0 gives 1 (a matured flow is cash); beyond 30 years
        ln DF is held flat."""
        t = np.asarray(t, dtype=float)
        ln = np.interp(t, self.t_knots, self.ln_df_knots)
        return np.exp(ln)

    def df_dates(self, d0: dt.date, dates) -> np.ndarray:
        return self.df(yearfrac_array(d0, dates))

    def par_yield(self, n_years: float) -> float:
        """Par yield (decimal) at n years: linear interpolation over the tenors present, flat outside.
        A flat (single-tenor) curve returns that yield."""
        return float(np.interp(n_years, self.tenors, self.yields))

    def zero_rate(self, t):
        t = np.asarray(t, dtype=float)
        return -np.log(self.df(t)) / np.where(t > 0, t, np.nan)


def many_curves_df(par_rows: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Vectorised: par_rows is (N, 12) percent with NaN for blanks in TENOR_ORDER; returns (N, len(t)) DFs.
    Same method as Curve, computed for many curves at once (used for the daily history)."""
    tenor_years = np.array([TENOR_YEARS[k] for k in TENOR_ORDER])
    n = par_rows.shape[0]
    P = np.empty((n, GRID.size))
    for i in range(n):
        row = par_rows[i]
        mask = ~np.isnan(row)
        P[i] = np.interp(GRID, tenor_years[mask], row[mask] / 100.0)
    DF = bootstrap(P)  # (n, 60)
    ln_knots = np.concatenate([np.zeros((n, 1)), np.log(DF)], axis=1)
    t_knots = np.concatenate([[0.0], GRID])
    out = np.empty((n, t.size))
    for i in range(n):
        out[i] = np.exp(np.interp(t, t_knots, ln_knots[i]))
    return out


# ---- fixed dates of the plan -----------------------------------------------------------------------------------
CURVE_DATE = dt.date(2026, 9, 28)                      # D
PAY_MATURITIES = [dt.date(2031 + k, 11, 15) for k in range(1, 11)]   # P_k = 15 Nov 2032 .. 15 Nov 2041
PAY_DATES = [dt.date(2032 + k, 1, 1) for k in range(1, 11)]          # payments 1 Jan 2033 .. 1 Jan 2042
JAN_2027 = dt.date(2027, 1, 1)
JAN_2028 = dt.date(2028, 1, 1)
JAN_2031 = dt.date(2031, 1, 1)
JAN_2033 = dt.date(2033, 1, 1)
PAYMENT = 50_000.0
DEPOSIT_2027 = 300_000.0
DEPOSIT_2028 = 150_000.0
FLOOR_FACE = 150_000.0
