"""Reconcile the D1 ladder price with the independent GPT check (research/insight_v1/verification/ladder_2026-09-28/gpt/).

Claude Code, 2026-09-29. MODEL prices on the 2026-09-28 Treasury par curve (treasury_par_2026_to_09-28.csv, downloaded from
home.treasury.gov on 2026-09-29). Uses D1_purchase_rule.py's curve method and changes one convention at a time:
year basis (days/365.25 as in D1, days/365 as in GPT) and whether the 1-3 month yields are used as discount-factor nodes.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/verification/ladder_2026-09-28/reconcile.py
"""
import csv
from datetime import date

import numpy as np

HERE = "research/insight_v1/verification/ladder_2026-09-28/"
TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
VAL, ANCHOR = date(2026, 9, 28), date(2027, 1, 1)

row = next(r for r in csv.DictReader(open(HERE + "treasury_par_2026_to_09-28.csv")) if r["Date"] == "09/28/2026")
par = {t: float(row[k]) for k, t in TENOR.items()}


def curve(basis, short_nodes):
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g, lz = [0.0], [0.0]
    if short_nodes:
        for t in (1 / 12, 2 / 12, .25):
            g.append(t)
            lz.append(np.log((1 + par[t] / 200) ** (-2 * t)))
    g += list(grid)
    lz += list(np.log(df))
    return lambda d: float(np.exp(np.interp((d - VAL).days / basis, g, lz)))


for basis, short in [(365.25, False), (365, False), (365.25, True), (365, True)]:
    f = curve(basis, short)
    spot = sum(50_000 * f(date(y, 11, 15)) for y in range(2032, 2042))
    print(f"days/{basis}, 1-3M nodes {short}: today ${spot:,.2f}  forward to 1 Jan 2027 ${spot / f(ANCHOR):,.2f}")
