"""What Laura's ten payments would have cost on every Treasury curve since 1962, and on every month since 1871.
Keel, Mon 9 Nov 2026. MODEL, on the register's own engine (method A bootstrap, payment-date basis).

Run from the repo root:  python3 -I keel/final_report/numbers/price_history.py
Writes keel/final_report/numbers/results_price_history.json and prints the figures.

Basis: each past curve is treated as if it were the 6 Nov 2026 curve, so the ten payments are always the same
distance ahead (the forward value on 1 Jan 2027 of $50,000 on 1 Jan 2033..2042). This answers "would $300,000 have
bought the ten on that day's rates?". It differs slightly from NUMBERS.md 8b, which values each 2026 close on its own
date; both are printed for 2026 so the two can be compared.

Data:
  1962 - 2025: FRED constant-maturity Treasury yields DGS1MO..DGS30 (Treasury's own par curve, as FRED republishes
               it; downloaded 27 Sep 2026, archive/rab/data/fred/). Tenors missing on a day (no 20-year 1987-93, no
               30-year 2002-06, no 2-year before 1976, no bills before 1981) are left out and the curve is interpolated
               across the gap.
  2026:        treasury.gov daily par curves in competition/official_market_data/ (the register's source).
  1871 - 2026: Shiller's monthly long-term government bond yield (keel/models/data/shiller_monthly.csv, to 2023),
               then the monthly average of the 10-year CMT. Only one rate, so the curve is flat at that rate; the
               flat-curve bias is measured on 1962-2026, where both exist.
"""
import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402

DEP = 300_000.0
FRED = E.ROOT / "archive/rab/data/fred"
FRED_TENORS = {"DGS1MO": 1 / 12, "DGS3MO": .25, "DGS6MO": .5, "DGS1": 1, "DGS2": 2, "DGS3": 3, "DGS5": 5,
               "DGS7": 7, "DGS10": 10, "DGS20": 20, "DGS30": 30}


def cost(par):
    return E.ladder_cost(E.Curve(par))


# ---------------------------------------------------------------- 1. daily, full curve, 1962-2026
days = {}
for col, t in FRED_TENORS.items():
    for r in csv.DictReader(open(FRED / f"{col}.csv")):
        if r[col] in ("", ".") or r["observation_date"] >= "2026-01-01":
            continue
        days.setdefault(r["observation_date"], {})[t] = float(r[col])
for fn in ("daily-treasury-rates_2026-10-23.csv", "daily-treasury-rates_2026-11-06.csv"):
    for r in csv.DictReader(open(E.ROOT / "competition/official_market_data" / fn)):
        d = datetime.strptime(r["Date"], "%m/%d/%Y").date().isoformat()
        par = {}
        for k, t in E.TENORS.items():
            try:
                par[t] = float(r[k])
            except (KeyError, ValueError):
                pass
        days[d] = par

keys, costs, y10 = [], [], []
for d in sorted(days):
    par = days[d]
    if 1 not in par or 10 not in par or not ({20, 30} & set(par)):
        continue          # a usable curve needs the 1-year, the 10-year and a 20- or 30-year point
    keys.append(d)
    costs.append(cost(par))
    y10.append(par[10])
keys = np.array(keys)
c = np.array(costs)
yrs = np.array([int(k[:4]) for k in keys])


def share(mask):
    return float((c[mask] <= DEP).mean())


def cheapest_since(day):
    """The latest earlier day whose cost was at or below this day's cost."""
    i = int(np.where(keys == day)[0][0])
    prior = np.where(c[:i] <= c[i])[0]
    return {"day": day, "cost": float(c[i]), "cheapest_since": keys[prior[-1]] if len(prior) else "before 1962",
            "cost_then": float(c[prior[-1]]) if len(prior) else None}


under = c <= DEP
last_before_2026 = keys[(yrs < 2026) & under][-1]
first_2026 = keys[(yrs == 2026) & under][0]
i_dear00 = int(np.argmax(np.where(yrs >= 2000, c, -1)))
out = {"basis": "forward value on 1 Jan 2027 of $50,000 on 1 Jan 2033..2042, each past curve as if it were the "
                "6 Nov 2026 curve (same distance ahead); method A bootstrap (engine.py)",
       "daily": {"days": len(c), "first": keys[0], "last": keys[-1],
                 "share_days_300k_buys_ten": {"since_1962": share(yrs >= 1962), "since_1990": share(yrs >= 1990),
                                              "since_2000": share(yrs >= 2000), "2000_to_2025": share((yrs >= 2000) & (yrs <= 2025))},
                 "days_since_2000": int((yrs >= 2000).sum()), "days_since_2000_under_300k": int(((yrs >= 2000) & under).sum()),
                 "last_day_under_300k_before_2026": last_before_2026,
                 "first_day_under_300k_in_2026": first_2026,
                 "days_2026_under_300k": int(((yrs == 2026) & under).sum()), "days_2026": int((yrs == 2026).sum()),
                 "dearest_since_2000": {"day": keys[i_dear00], "cost": float(c[i_dear00]), "y10": y10[i_dear00]},
                 "cheapest_since_2000_overall": {"day": keys[yrs >= 2000][int(np.argmin(c[yrs >= 2000]))],
                                                 "cost": float(c[yrs >= 2000].min())},
                 "share_by_decade": {f"{dec}s": share((yrs // 10 * 10) == dec) for dec in range(1960, 2030, 10)},
                 "key_days": {k: cheapest_since(k) for k in ("2026-09-28", "2026-10-05", "2026-10-07", "2026-10-08",
                                                              "2026-11-06")
                              if k in set(keys)}}}

# 2026 on both bases, so this file and NUMBERS.md 8b can be compared
ex = json.load(open(HERE / "results_extras_2026-11-06.json"))["history"]["series"]
dated = {h["date"]: h["payments"] for h in ex}
both = [(k, float(v), dated[k]) for k, v in zip(keys, c) if k in dated]
diff = np.array([a - b for _, a, b in both])
out["daily"]["check_2026_same_distance_minus_dated"] = {"mean": float(diff.mean()), "min": float(diff.min()),
                                                         "max": float(diff.max()), "days": len(both)}

# ---------------------------------------------------------------- 2. monthly, flat curve at the long rate, 1871-2026
TEN = [1 / 12, 1 / 6, .25, .5, 1, 2, 3, 5, 7, 10, 20, 30]


def flat_cost(y):
    return cost({t: y for t in TEN})


months, ylong = [], []
for r in csv.DictReader(open(E.ROOT / "keel/models/data/shiller_monthly.csv")):
    v = r["Long Interest Rate"]
    if v not in ("", "0.0", "NaN"):
        months.append(r["Date"][:7]); ylong.append(float(v))
m10 = {}
for k, y in zip(keys, y10):
    m10.setdefault(k[:7], []).append(y)
for m in sorted(m10):
    if m > months[-1]:
        months.append(m); ylong.append(float(np.mean(m10[m])))
months = np.array(months)
fc = np.array([flat_cost(y) for y in ylong])
my = np.array([int(m[:4]) for m in months])
munder = fc <= DEP
lo, hi = 0.0, 0.15
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (lo, mid) if flat_cost(mid * 100) <= DEP else (mid, hi)

# flat-curve bias where both exist: monthly averages of the full-curve daily cost against the flat cost
mfull = {}
for k, v in zip(keys, c):
    mfull.setdefault(k[:7], []).append(v)
ov = [(m, float(np.mean(mfull[m])), f) for m, f in zip(months, fc) if m in mfull]
out["monthly_flat_since_1871"] = {
    "months": len(fc), "first": months[0], "last": months[-1],
    "share_months_300k_buys_ten": {"since_1871": float(munder.mean()), "since_1962": float(munder[my >= 1962].mean()),
                                   "since_2000": float(munder[my >= 2000].mean())},
    "last_month_under_300k_before_2026": months[(my < 2026) & munder][-1],
    "flat_yield_needed_for_300k_pct": hi * 100,
    "dearest": {"month": months[int(np.argmax(fc))], "cost": float(fc.max())},
    "share_by_period": {"1871-1913": float(munder[(my >= 1871) & (my <= 1913)].mean()),
                        "1914-1945": float(munder[(my >= 1914) & (my <= 1945)].mean()),
                        "1946-1965": float(munder[(my >= 1946) & (my <= 1965)].mean()),
                        "1966-1999": float(munder[(my >= 1966) & (my <= 1999)].mean()),
                        "2000-2026": float(munder[my >= 2000].mean())},
    "flat_bias_1962_2026": {"months": len(ov),
                            "share_under_300k_full_curve": float(np.mean([a <= DEP for _, a, _ in ov])),
                            "share_under_300k_flat_curve": float(np.mean([f <= DEP for _, _, f in ov])),
                            "mean_flat_minus_full": float(np.mean([f - a for _, a, f in ov]))},
}
out["stamp"] = {"engine": "engine.py method A", "run": "Mon 9 Nov 2026"}
json.dump(out, open(HERE / "results_price_history.json", "w"), indent=1)
print(json.dumps(out, indent=1, default=str))
