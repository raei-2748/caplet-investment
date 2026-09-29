"""Shared helpers for WS3 models M5 (backtest), M6 (rivals) and M7 (stress). AI-generated research code (Claude Code).

Curve = M1_METHOD.md A1 ("D1 method"): linear par on a 0.5-year grid, semiannual bootstrap, log-linear discount
factors, days/365.25. Re-implemented here (not imported from m1_ladder.py) and checked against the Gate A
numbers.yaml headline in `self_test()`.
"""
import csv
import math
import os
from datetime import date

import numpy as np
import pandas as pd
import yaml

WT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(WT, "rab", "data")
HIST = os.path.join(DATA, "history")
RES = os.path.join(WT, "rab", "results")
SEED = 20260930

TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
GRID = np.arange(0.5, 30.01, 0.5)
D_REF = date(2026, 9, 28)
A27, A28, A31, A33 = date(2027, 1, 1), date(2028, 1, 1), date(2031, 1, 1), date(2033, 1, 1)
NOV15 = [date(y - 1, 11, 15) for y in range(2033, 2043)]          # STRIPS maturities for the 2033..2042 payments
PAY, DEP1, DEP2, FLOOR_FACE = 50_000.0, 300_000.0, 150_000.0, 150_000.0

# Okabe-Ito colour-blind-safe palette
OI = {"black": "#000000", "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73", "yellow": "#F0E442",
      "blue": "#0072B2", "vermillion": "#D55E00", "purple": "#CC79A7", "grey": "#999999"}


def yf(d0, d1):
    return (d1 - d0).days / 365.25


# ------------------------------------------------------------------------------------------------------------ curve
class Curve:
    """Par yields in percent keyed by the par-file column names; blank / NaN tenors are skipped."""

    def __init__(self, par, bp=0.0):
        pts = sorted((TENOR[k], float(v) / 100 + bp / 1e4) for k, v in par.items()
                     if k in TENOR and v is not None and v == v and str(v).strip() not in ("", "N/A"))
        if not pts:
            raise ValueError("no tenors")
        ts, ps = zip(*pts)
        self.ts, self.ps = np.array(ts), np.array(ps)
        p = np.interp(GRID, self.ts, self.ps)
        df = np.empty_like(p)
        s = 0.0
        for j, y in enumerate(p):
            c = y / 2
            df[j] = (1 - c * s) / (1 + c)
            s += df[j]
        self.g = np.r_[0.0, GRID]
        self.lz = np.r_[0.0, np.log(df)]

    def df(self, t):
        return np.exp(np.interp(t, self.g, self.lz))

    def par(self, t):
        return float(np.interp(t, self.ts, self.ps))


def ladder_value(cv, times):
    return float(PAY * cv.df(np.asarray(times)).sum())


# ------------------------------------------------------------------------------------------------------------ data
def load_par_files():
    """H1: every Treasury par-curve row 1990-2026 as (date, dict)."""
    import glob
    files = sorted(glob.glob(os.path.join(DATA, "treasury_par_1990_1999", "*.csv"))) + \
        sorted(f for f in glob.glob(os.path.join(DATA, "treasury_par_2000_2026", "*.csv")) if "refetch" not in f)
    rows = {}
    for p in files:
        for r in csv.DictReader(open(p)):
            m, d, y = r["Date"].split("/")
            rows[date(int(y), int(m), int(d))] = {k: r.get(k) for k in TENOR}
    return sorted(rows.items())


def load_fred_daily():
    df = pd.read_csv(os.path.join(HIST, "daily_curves_1962_1989.csv"), parse_dates=["date"])
    out = []
    for r in df.itertuples(index=False):
        rec = dict(zip(df.columns[1:], r[1:]))
        out.append((r[0].date(), rec))
    return out


def load_shiller():
    return pd.read_csv(os.path.join(HIST, "shiller_monthly.csv"))


def load_soy():
    return pd.read_csv(os.path.join(HIST, "soy_curves.csv")).set_index("year")


def soy_curve(soy, y, bp=0.0):
    row = soy.loc[y]
    return Curve({k: row[k] for k in TENOR}, bp=bp)


def load_annual():
    return pd.read_csv(os.path.join(HIST, "annual_history.csv")).set_index("year")


def numbers():
    with open(os.path.join(WT, "rab", "numbers.yaml")) as f:
        return yaml.safe_load(f)["numbers"]


def today_curve(bp=0.0):
    return Curve(numbers()["market.par_curve"]["value"], bp=bp)


# ------------------------------------------------------------------------------------------------------------ plots
def plot_style():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"figure.dpi": 150, "savefig.dpi": 150, "font.size": 9.5, "axes.titlesize": 11,
                         "axes.labelsize": 9.5, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.alpha": 0.25, "legend.frameon": False,
                         "font.family": "DejaVu Sans", "text.parse_math": False})
    return plt


def kusd(x):
    return f"${x / 1000:,.0f}k"


def self_test():
    """The re-implemented curve must reproduce the Gate A headline to the cent."""
    n = numbers()
    cv = today_curve()
    v0 = ladder_value(cv, [yf(D_REF, p) for p in NOV15])
    va = v0 / float(cv.df(yf(D_REF, A27)))
    assert abs(v0 - n["laura.ladder.cost_today_strips"]["value"]) < 0.01, v0
    assert abs(va - n["laura.ladder.cost_2027_strips"]["value"]) < 0.01, va
    return v0, va


if __name__ == "__main__":
    print(self_test())
