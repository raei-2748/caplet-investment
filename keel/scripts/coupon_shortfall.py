"""FICTION (Team Keel), MODEL. Coupon-reinvestment shortfall of Keel's ladder bought 1 Jan 2027.
Curve: treasury.gov par CSV row 10/23/2026 (fetched 24 Oct 19:39 UTC), method A of keel/scripts/ladder_pv.py
(par yields semiannual, bootstrapped on 0.5y grid, log-linear discount factors). Forward rates from 1 Jan 2027.
Rungs: iBond ETFs 2033-37 = zero-coupon-like, $ at 15 Dec 2032-36 (ASSUMED date, UNVERIFIED);
T-bonds 4.750% 15 Feb 2037 (->2038), 4.500% 15 May 2038 (->2039), 4.375% 15 Nov 2039/4.250% 2040/3.125% 2041 (->2040-42).
Design A (own rung): each T-bond's coupons are reinvested to its own maturity at forward rates, face sized so that
  face + reinvested coupons = $50,000; principal waits as cash to 1 Jan (holdings basis convention).
Design B (IPS v2 literal, "Treasuries maturing before the next payment"): every coupon funds the NEXT payment date;
  rungs sized backward (2042 first) so each year's cash = $50,000; iBond faces shrink by the T-bond coupons they receive.
Shocks: reinvestment forward rates lower by X pp (continuous-comp approx), floored at 0, from 2 Jan 2027.
Usage: python3 -I coupon_shortfall.py /path/to/tsy_2026.csv /path/to/fred_GS10_monthly.csv"""
import csv, sys
from datetime import date
import numpy as np

COLS = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
        "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
rows = {r["Date"]: r for r in csv.DictReader(open(sys.argv[1]))}
DAY = sys.argv[3] if len(sys.argv) > 3 else "10/23/2026"
m_, d_, y_ = map(int, DAY.split("/")); VAL = date(y_, m_, d_)
par = {COLS[k]: float(rows[DAY][k]) for k in COLS}
grid = np.arange(0.5, 30.01, 0.5)
ts = sorted(par); p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
for yv in p:
    c = yv / 2; df.append((1 - c * sum(df)) / (1 + c))
G, LZ = np.r_[0, grid], np.log(np.r_[1, df])
lnf = lambda t: np.interp(t, G, LZ)                    # ln discount factor from VAL
yf = lambda d: (d - VAL).days / 365.25
J27, J33 = yf(date(2027, 1, 1)), yf(date(2033, 1, 1))

def grow(t1, t2, shift=0.0):
    """Growth of $1 reinvested at t1 to t2 at the forward rate + shift (pp), cc, floored at 0."""
    if t2 <= t1: return 1.0
    r = (lnf(t1) - lnf(t2)) / (t2 - t1)
    return float(np.exp(max(r + shift / 100, 0.0) * (t2 - t1)))

def cdates(mat):
    out, y, m = [], mat.year, mat.month
    while True:
        d = date(y, m, 15)
        if d <= date(2027, 1, 1): break
        out.append(d); m -= 6
        if m <= 0: m += 12; y -= 1
    return sorted(out)

PAYY = list(range(2033, 2043)); PAYD = {Y: date(Y, 1, 1) for Y in PAYY}
TB = {2038: (date(2037, 2, 15), 4.75), 2039: (date(2038, 5, 15), 4.50), 2040: (date(2039, 11, 15), 4.375),
      2041: (date(2040, 11, 15), 4.25), 2042: (date(2041, 11, 15), 3.125)}
IB = {Y: date(Y - 1, 12, 15) for Y in range(2033, 2038)}
pv27 = lambda t: float(np.exp(lnf(t) - lnf(J27)))       # price at 1 Jan 2027 of $1 at t

def nextpay(d):
    for Y in PAYY:
        if d <= PAYD[Y]: return Y

# ---------- Design A ----------
def A_value(Y, F, shiftfn):
    mat, cpn = TB[Y]; tm = yf(mat)
    return F * (1 + cpn / 200 * sum(grow(yf(d), tm, shiftfn(yf(d))) for d in cdates(mat)))
FA = {Y: 50000 / A_value(Y, 1.0, lambda t: 0) for Y in TB}
FA.update({Y: 50000.0 for Y in IB})
def costA():
    c = sum(FA[Y] * pv27(yf(IB[Y])) for Y in IB)
    for Y, (mat, cpn) in TB.items():
        c += FA[Y] * (pv27(yf(mat)) + cpn / 200 * sum(pv27(yf(d)) for d in cdates(mat)))
    return c
def deliverA(shiftfn):
    return {Y: (50000.0 if Y in IB else A_value(Y, FA[Y], shiftfn)) for Y in PAYY}

# ---------- Design B ----------
def B_cash(F, shiftfn):
    """cash at each payment date from T-bond faces F (dict), coupons rolled to the next payment date."""
    cash = {Y: 0.0 for Y in PAYY}
    for Yb, (mat, cpn) in TB.items():
        if Yb not in F: continue
        for d in cdates(mat):
            Y = nextpay(d); cash[Y] += F[Yb] * cpn / 200 * grow(yf(d), yf(PAYD[Y]), shiftfn(yf(d)))
        cash[Yb] += F[Yb]   # principal (idle to 1 Jan)
    return cash
FB = {}
for Yb in sorted(TB, reverse=True):          # solve backward: later bonds' coupons land in earlier windows
    FB[Yb] = 0.0
    lo, hi = 0.0, 60000.0
    for _ in range(60):
        FB[Yb] = (lo + hi) / 2
        (lo, hi) = (FB[Yb], hi) if B_cash(FB, lambda t: 0)[Yb] < 50000 else (lo, FB[Yb])
base_cashB = B_cash(FB, lambda t: 0)
def B_roll(cash, ib, shiftfn):
    """add iBond $ and roll any surplus over $50k forward to the next payment date (reinvested)."""
    out, carry = {}, 0.0
    for i, Y in enumerate(PAYY):
        avail = cash[Y] + ib.get(Y, 0) + carry
        out[Y] = min(avail, 50000.0)
        if i + 1 < len(PAYY):
            t = yf(PAYD[Y]); carry = max(avail - 50000, 0) * grow(t, yf(PAYD[PAYY[i + 1]]), shiftfn(t))
    return out
IBB, carry = {}, 0.0                      # size iBonds on base forwards: buy only what the coupons + carry miss
for i, Y in enumerate(PAYY[:5]):
    avail = base_cashB[Y] + carry
    IBB[Y] = max(50000 - avail, 0.0)
    t = yf(PAYD[Y]); carry = max(avail + IBB[Y] - 50000, 0) * grow(t, yf(PAYD[PAYY[i + 1]]))
def costB():
    c = sum(IBB[Y] * pv27(yf(IB[Y])) for Y in IB)
    for Y, (mat, cpn) in TB.items():
        c += FB[Y] * (pv27(yf(mat)) + cpn / 200 * sum(pv27(yf(d)) for d in cdates(mat)))
    return c
def deliverB(shiftfn):
    d = B_roll(B_cash(FB, shiftfn), IBB, shiftfn)
    return {Y: d[Y] for Y in PAYY}
# note: deliverB caps each year at $50k, so a surplus never hides a later shortfall; shortfall reported >= 0 per year
def pv33(sf, X):   # shortfall in 2033 dollars, discounted at the shifted forward curve (cost to cover in 2033)
    return sum(v / grow(J33, yf(PAYD[Y]), X) for Y, v in sf.items())

if __name__ == "__main__":
    hold = sum(50000 * pv27(yf(IB[Y])) for Y in IB) + sum(50000 * pv27(yf(TB[Y][0])) for Y in TB)
    print(f"Curve {DAY}: 1y {par[1]} 5y {par[5]} 10y {par[10]} 20y {par[20]} 30y {par[30]}")
    print(f"Cost A ${costA():,.0f} | cost B ${costB():,.0f} | check: holdings-basis zero ladder ${hold:,.0f}")
    print("Faces A (T-bonds):", {Y: round(FA[Y]) for Y in TB})
    print("Faces B (T-bonds):", {Y: round(FB[Y]) for Y in TB}, " iBond $ B:", {Y: round(IBB[Y]) for Y in IB})
    totcpn = sum(FA[Y] * TB[Y][1] / 200 * len(cdates(TB[Y][0])) for Y in TB)
    pre33 = sum(FA[Y] * TB[Y][1] / 200 * sum(1 for d in cdates(TB[Y][0]) if d < date(2033, 1, 1)) for Y in TB)
    print(f"A: total T-bond coupons ${totcpn:,.0f} (before 2033 ${pre33:,.0f})")
    for name, dfn in (("A own-rung", deliverA), ("B next-payment", deliverB)):
        print(f"\n{name}: shortfall by payment year (nominal $), reinvestment X pp lower for good")
        for X in (-1, -2, -3):
            d = dfn(lambda t, X=X: X); sf = {Y: 50000 - d[Y] for Y in PAYY}
            print(f"  {X:+d}pp: " + " ".join(f"{Y % 100}:{sf[Y]:,.0f}" for Y in PAYY if abs(sf[Y]) > .5) +
                  f" | total nominal ${sum(sf.values()):,.0f} | 2033$ ${pv33(sf, X):,.0f}")
    # path 1: yields drift down 2pp evenly over 2027-2030 then stay
    ramp = lambda t: -2 * min(max((t - J27) / 4, 0), 1)
    for name, dfn in (("A", deliverA), ("B", deliverB)):
        d = dfn(ramp); sf = {Y: 50000 - d[Y] for Y in PAYY}
        print(f"Path ramp -2pp over 4y, {name}: total ${sum(sf.values()):,.0f}, 2033$ ${pv33(sf, -2):,.0f}")
    # Monte Carlo: random-walk parallel shift, 90bp/yr (Jun's assumption, UNVERIFIED), monthly from 1 Jan 2027
    rng = np.random.default_rng(2033); N = 4000
    steps = np.arange(0, 16.01, 1 / 12)
    for name, dfn in (("A", deliverA), ("B", deliverB)):
        tot = []
        for i in range(N):
            w = np.r_[0, rng.normal(0, .9 * np.sqrt(1 / 12), len(steps) - 1).cumsum()]
            fn = lambda t, w=w: float(np.interp(t - J27, steps, w))
            d = dfn(fn); tot.append(sum(50000 - d[Y] for Y in PAYY))
        tot = np.array(tot)
        print(f"MC {name} (90bp/yr, N={N}): total shortfall p5 ${np.percentile(tot,5):,.0f} p50 ${np.percentile(tot,50):,.0f} "
              f"p95 ${np.percentile(tot,95):,.0f} p99 ${np.percentile(tot,99):,.0f}; P(>$1k) {np.mean(tot>1000):.0%}")
    # historical replay: GS10 monthly changes 1953-2026 as a parallel shift (16-year windows)
    h = [(r["observation_date"], float(r["GS10"])) for r in csv.DictReader(open(sys.argv[2]))]
    for name, dfn in (("A", deliverA), ("B", deliverB)):
        res = []
        for s in range(0, len(h) - 15 * 12):
            seg = np.array([v for _, v in h[s:s + 16 * 12 + 1]]) - h[s][1]
            st = np.arange(len(seg)) / 12
            d = dfn(lambda t, seg=seg, st=st: float(np.interp(t - J27, st, seg)))
            res.append((sum(50000 - d[Y] for Y in PAYY), h[s][0]))
        v = np.array([r[0] for r in res]); w = max(res)
        print(f"History {name}: {len(res)} starts, p95 ${np.percentile(v,95):,.0f}, worst ${w[0]:,.0f} (start {w[1]}), "
              f"P(>$1k) {np.mean(v>1000):.0%}")
