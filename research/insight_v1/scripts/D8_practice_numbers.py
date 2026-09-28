"""D8 Professional-Practice Benchmarker: numbers for M109 (required return per goal), M026 (fees) and
M006/M235 (does a rebalancing rule move anything measurable?).

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D8_practice_numbers.py

Inputs and status labels
- Case cash flows: +$300,000 on 2027-01-01, +$150,000 on 2028-01-01, ten x $50,000 on 1 Jan 2033..2042
  (competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt p.2-3; VERIFIED-REPO-FILE, F-601).
- Official Treasury par curve 2026-09-25 (competition/official_market_data/daily-treasury-rates_2026-09.csv;
  VERIFIED-REPO-FILE). Bootstrap method copied from research/verified_2026-09-27/official_curve_pv.py
  (method = ASSUMPTION already used by the verified script; reproduces $292,264).
- JPM 2026 LTCMA: AC World equity 7.00% compound, 16.78% vol; cash 3.10% (VERIFIED-REPO-FILE via brief s6 / F-3xx).
- Short-Treasury sleeve bond return 3.9%/yr, vol 2.0%/yr: ASSUMPTION (brief/wins_now s8 suggests 3.5-3.9%;
  VGSH SEC yield 4.55% on 9/24 is the upper bound, JPM cash 3.10% the lower).
- Sleeve mix 60% equity / 40% short Treasuries, rebalanced yearly: ASSUMPTION (provisional team call, brief s7).
- Fee levels 0.25% / 0.50% / 1.00% a year: ASSUMPTION scenarios bracketing Kitces/Veres medians (1.00% AUM fee up to
  $1M; ~0.50% for HNW; kitces.com, read 2026-09-27, VERIFIED-PRIMARY for what Kitces reports).
- Fund expense of an IEF-type fund 0.15% (iShares page, VERIFIED-PRIMARY via wins_now ticket s1).
Outputs are deterministic (M109, M026) or seeded Monte Carlo (band check); every output is ASSUMPTION-based
arithmetic on the inputs above.
"""
import csv
from datetime import date

import numpy as np
from scipy.optimize import brentq

# ---------- curve (same method as official_curve_pv.py) ----------
CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
row = next(r for r in csv.DictReader(open(CSV)) if r["Date"] == "09/25/2026")
tenor = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
par = {t: float(row[k]) for k, t in tenor.items()}
val = date(2026, 9, 25)
yf = lambda d: (d - val).days / 365.25


def build(par):
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
    for y in p:
        c = y / 2; df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]; lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


DF = build(par)
d = lambda y: DF(yf(date(y, 1, 1)))          # discount factor to 1 Jan of year y
fwd_growth = lambda y0, y1: d(y0) / d(y1)     # growth locked in by today's curve from y0 to y1
ladder_2027 = sum(50000 * d(y) / d(2027) for y in range(2033, 2043))
reserve_2033 = sum(50000 * d(y) / d(2033) for y in range(2033, 2043))
print(f"Check: ladder cost at 2027-01-01 ${ladder_2027:,.0f} (verified $292,264); "
      f"reserve value at 2033-01-01 ${reserve_2033:,.0f} (F-106 $394,930)")

# ---------- M109: required return per goal ----------
print("\n[M109] Required return (IRR, annual) of the case cash flows")


def irr(flows):  # flows: {year: amount}, + = into portfolio
    f = lambda r: sum(a / (1 + r) ** (y - 2027) for y, a in flows.items())
    return brentq(lambda r: -f(r), -0.5, 1.0)


base = {2027: 300000, 2028: 150000, **{y: -50000 for y in range(2033, 2043)}}
print(f"  Payments only, both deposits: {irr(base)*100:.2f}%")
print(f"  Payments only, first deposit only: {irr({k: v for k, v in base.items() if k != 2028})*100:.2f}%")
for fac in (50000, 100000, 150000, 165000, 200000, 207000, 250000):
    fl = dict(base); fl[2033] = fl[2033] - fac
    print(f"  Payments + ${fac/1e3:.0f}k facility in 2033: {irr(fl)*100:.2f}%")

# Facility reachable with NO equity: everything above the ladder held in Treasuries at today's forwards.
sleeve27 = 300000 - ladder_2027
tsy_only = sleeve27 * fwd_growth(2027, 2033) + 150000 * fwd_growth(2028, 2033)
print(f"  Facility money in 2033 if the surplus earns only today's Treasury forwards: ${tsy_only:,.0f}")
print(f"    (2027 leftover ${sleeve27:,.0f} x {fwd_growth(2027,2033):.4f}; 2028 deposit x {fwd_growth(2028,2033):.4f})")
f5 = fwd_growth(2028, 2033) ** (1 / 5) - 1
print(f"  Implied 2028->2033 forward Treasury return: {f5*100:.2f}%/yr (NOT lockable today for the 2028 deposit: "
      f"no derivatives in the plan; it is the market's break-even, not a promise)")
for weq in (0.5, 0.6, 0.7):
    rs = weq * 0.07 + (1 - weq) * f5
    v = sleeve27 * (1 + rs) ** 6 + 150000 * (1 + rs) ** 5
    print(f"  Deterministic sleeve {weq*100:.0f}% equity at JPM 7.00% + bonds at forward {f5*100:.2f}%: ${v:,.0f} "
          f"({v - tsy_only:+,.0f} vs Treasury-only)")
for tgt in (150000, 175000, 200000, 207000, 225000, 250000):
    r = brentq(lambda r: sleeve27 * (1 + r) ** 6 + 150000 * (1 + r) ** 5 - tgt, -0.5, 1)
    print(f"  Sleeve return needed for ${tgt/1e3:.0f}k facility money in 2033: {r*100:.2f}%/yr")

# ---------- M026: fees ----------
print("\n[M026] Fee arithmetic (deterministic, ASSUMPTION returns)")
r_eq, r_b, w = 0.07, 0.039, 0.60
r_sl = w * r_eq + (1 - w) * r_b
print(f"  Sleeve return used: {r_sl*100:.2f}%/yr (60% x 7.00% + 40% x 3.9%)")
# ladder market value path at forwards
lad = {y: sum(50000 * d(p) / d(y) for p in range(max(y, 2033), 2043)) for y in range(2027, 2043)}


def surplus_2033(fee, base_):  # base_: 'sleeve' or 'all' assets; fee always paid out of the sleeve
    s = sleeve27
    for y in range(2027, 2033):  # fee charged at the start of each year on that year's assets
        if y == 2028: s += 150000
        fee_amt = fee * (s + (lad[y] if base_ == "all" else 0))
        s = (s - fee_amt) * (1 + r_sl)
    return s


nofee = surplus_2033(0, "sleeve")
print(f"  2033 facility money, no fee: ${nofee:,.0f}")
for fee in (0.0025, 0.005, 0.01):
    a, b = surplus_2033(fee, "sleeve"), surplus_2033(fee, "all")
    print(f"  fee {fee*100:.2f}%: on sleeve only ${a:,.0f} ({a-nofee:+,.0f}); "
          f"on ALL assets, paid from sleeve ${b:,.0f} ({b-nofee:+,.0f})")
# fee charged ON the ladder and paid FROM the ladder, 2027-2042 (PV at 2027 of the amounts taken)
for fee in (0.0015, 0.005, 0.01):
    pv = sum(fee * lad[y] * d(y) / d(2027) for y in range(2027, 2043))
    print(f"  fee {fee*100:.2f}% taken from the ladder 2027-42: PV ${pv:,.0f} = {pv/(300000-ladder_2027):.1f}x the "
          f"${300000-ladder_2027:,.0f} headroom")
print(f"  2027 fee on all assets at 1.00%: ${0.01*300000:,.0f} vs 2027 sleeve ${sleeve27:,.0f} (fits once)")
prod = w * 0.0006 + (1 - w) * 0.0003
print(f"  Sleeve product cost with VT 0.06% / VGSH 0.03%: {prod*100:.3f}%/yr; STRIPS ladder: no ongoing fund fee")

# ---------- M006/M235: does a rebalancing rule move anything? ----------
print("\n[M006/M235] Sleeve equity drift 2028->2031 without rebalancing (MC, 100k paths, seed 20260927)")
rng = np.random.default_rng(20260927)
n = 100000
mu_e = np.log(1 + r_eq); sd_e = 0.1678
mu_b = np.log(1 + r_b); sd_b = 0.02
E = np.full(n, 0.6); B = np.full(n, 0.4)
for _ in range(3):  # 2028, 2029, 2030 -> weight at 1 Jan 2031
    E *= np.exp(rng.normal(mu_e, sd_e, n))  # compound (median) growth 7.00%, log-vol ~16.78% (ASSUMPTION)
    B *= np.exp(rng.normal(mu_b, sd_b, n))
wt = E / (E + B)
print(f"  Equity share of sleeve on 2031-01-01, never rebalanced: p5 {np.percentile(wt,5)*100:.0f}% / "
      f"p50 {np.percentile(wt,50)*100:.0f}% / p95 {np.percentile(wt,95)*100:.0f}%")
print(f"  Share of paths outside a 55-65% band by 2031: {np.mean((wt<0.55)|(wt>0.65))*100:.0f}%")
