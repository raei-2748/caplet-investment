"""Cost of Laura's ten $50k payments (Jan 1 2033..2042), valued at 2027-01-01, from the OFFICIAL
Treasury par yield curve of 2026-09-25 (home.treasury.gov CSV uploaded by the team).
Method: par yields as semiannual bond-equivalent yields, linear interpolation onto a 0.5y grid,
bootstrap discount factors (DF(0)=1), log-linear DF interpolation. Value at 2027-01-01 is the
forward value today's curve locks in. Also: IEF/TLT duration-matching weights from iShares fact
sheets (as of 2026-06-30)."""
import csv, numpy as np
from datetime import date

CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
rows = list(csv.DictReader(open(CSV)))
row = next(r for r in rows if r["Date"] == "09/25/2026")
tenor = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
par = {t: float(row[k]) for k, t in tenor.items()}

val, anchor = date(2026, 9, 25), date(2027, 1, 1)
yf = lambda d: (d - val).days / 365.25

def build(par):
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
    for y in p:
        c = y / 2; df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]; lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))

def pv(shift=0.0):
    f = build({k: v + shift for k, v in par.items()}); ta = yf(anchor)
    return sum(50000 * f(yf(date(y, 1, 1))) / f(ta) for y in range(2033, 2043))

base = pv()
print(f"Official curve 2026-09-25: {par}")
print(f"PV at 2027-01-01 of ten $50k payments: ${base:,.0f}")
for s in (-1, -.5, -.25, .5, 1):
    print(f"  parallel {int(s*100):+d}bp: ${pv(s):,.0f} ({pv(s)-base:+,.0f})")
dv01 = (pv(-.01) - pv(.01)) / 2
dur = dv01 / base * 1e4
print(f"DV01 ${dv01:,.0f}/bp; effective duration {dur:.2f}y; headroom under $300k: ${300000-base:,.0f} = {(300000-base)/dv01:.0f}bp")
f = build(par); ta = yf(anchor)
z = lambda y: 2 * ((f(ta) / f(yf(date(y, 1, 1)))) ** (1 / (2 * (yf(date(y, 1, 1)) - ta))) - 1)
print("Implied forward zero (semiannual) from 2027-01-01 to 2033/2037/2042:",
      [f"{z(y)*100:.2f}%" for y in (2033, 2037, 2042)])
IEF, TLT = 6.95, 15.31  # iShares fact sheets, effective duration, as of 2026-06-30
w = (TLT - dur) / (TLT - IEF)
print(f"Duration match with IEF {IEF}y / TLT {TLT}y: {w*100:.1f}% IEF / {(1-w)*100:.1f}% TLT")
