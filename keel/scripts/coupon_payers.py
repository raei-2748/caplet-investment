"""MODEL. Who pays a coupon shortfall? Floor / sail / Laura's kept half, 25% sail rule (keel/scripts/sail_mc.py method).
2028 money = $150,000 - holdings gap $992 x (1 + 1y 4.44%) = $148,964 (23 Oct close, Jun's 25 Oct sheet).
Floor = 75% in a Treasury maturing near 1 Jan 2033 at the 5y par (4.82%, or 2.82% if yields fell 2pp), coupons
reinvested at the same yield; sail = 25% in AC World stocks, lognormal 7.00% compound / 16.78% vol (JPM 2026 LTCMA),
N=200,000, seed 2033, buy and hold 2028-32. Laura's kept half = half the sail on 1 Jan 2033 (cap ignored: conservative).
Usage: python3 -I q3_payers.py TSY_CSV GS10_CSV"""
import sys, io, contextlib, runpy
from datetime import date
import numpy as np
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(sys.argv[0].replace("coupon_payers.py", "coupon_shortfall.py"), run_name="lib")
pv27, lnf, yf, grow, J27, J33, IB, PAYD = (g[k] for k in ("pv27", "lnf", "yf", "grow", "J27", "J33", "IB", "PAYD"))
deliverA, pv33, PAYY = g["deliverA"], g["pv33"], g["PAYY"]

# iBond rungs as par bonds (coupon = forward par yield from 1 Jan 2027), coupons reinvested to maturity: add-on
def cd(mat):
    out, y, m = [], mat.year, mat.month
    while True:
        d = date(y, m, 15)
        if d <= date(2027, 1, 1): break
        out.append(d); m -= 6
        if m <= 0: m += 12; y -= 1
    return sorted(out)
def ib_short(X):
    sf = {}
    for Y, mat in IB.items():
        ds = cd(mat); tm = yf(mat)
        c = (1 - pv27(tm)) / sum(pv27(yf(d)) for d in ds)          # forward par coupon per half-year
        v0 = 1 + c * sum(grow(yf(d), tm) for d in ds); v1 = 1 + c * sum(grow(yf(d), tm, X) for d in ds)
        sf[Y] = 50000 * (1 - v1 / v0)
    return sf
print("iBond-as-par-bond add-on (design A):")
SA = {}
for X in (-1, -2, -3):
    sfT = {Y: 50000 - v for Y, v in deliverA(lambda t, X=X: X).items()}
    sfI = ib_short(X)
    tot = {Y: sfT[Y] + sfI.get(Y, 0) for Y in PAYY}
    SA[X] = (pv33(sfT, X), pv33(tot, X))
    print(f"  {X:+d}pp: iBonds " + " ".join(f"{Y%100}:{sfI[Y]:,.0f}" for Y in IB) +
          f" | iBond nominal ${sum(sfI.values()):,.0f} | A+iBond nominal ${sum(tot.values()):,.0f}, 2033$ ${SA[X][1]:,.0f}")

def bond_growth(y, n=10):
    return 1 + y / 2 * sum((1 + y / 2) ** k for k in range(n))
N, SEED = 200_000, 2033
sig = np.sqrt(np.log(1 + (0.1678 / 1.0828) ** 2)); mu = np.log(1.07)
eq = np.exp(np.random.default_rng(SEED).normal(mu, sig, (N, 5)).sum(1))
Y1, Y5 = .0444, .0482; GAP = 992
print("\nPayers (2pp lower for good; shortfall in 2033 $: T-bonds only / T-bonds + iBond income):",
      f"${SA[-2][0]:,.0f} / ${SA[-2][1]:,.0f}")
for dep in (150_000, 75_000, 0):
    m = dep - GAP * (1 + Y1)
    for y5, lab in ((Y5, "5y 4.82%"), (Y5 - .02, "5y 2.82% (rates already down)")):
        floor = max(m, 0) * .75 * bond_growth(y5); half = max(m, 0) * .125 * eq; sail = 2 * half
        row = f"  deposit ${dep:,} {lab}: floor ${floor:,.0f}; sail p5/p50/p95 ${np.percentile(sail,5):,.0f}/${np.percentile(sail,50):,.0f}/${np.percentile(sail,95):,.0f}"
        for k, S in (("T", SA[-2][0]), ("T+iB", SA[-2][1])):
            row += f" | {k}: P(half>=S) {np.mean(half >= S):.1%}, P(sail>=S) {np.mean(sail >= S):.1%}"
        print(row)
# joint bad case: yields -2pp for good + stocks -40% 2028-31 then +7% in 2032
m = 150000 - GAP * (1 + Y1); half_bad = m * .125 * .60 * 1.07
print(f"\nJoint bad case (yields -2pp, stocks -40% then +7%): half ${half_bad:,.0f}, sail ${2*half_bad:,.0f}, "
      f"floor ${m*.75*bond_growth(Y5-.02):,.0f}; shortfall ${SA[-2][0]:,.0f}/${SA[-2][1]:,.0f}; uncovered by half "
      f"${max(SA[-2][0]-half_bad,0):,.0f}/${max(SA[-2][1]-half_bad,0):,.0f}")
for X in (-1, -2, -3):
    for k, S in (("T", SA[X][0]), ("T+iB", SA[X][1])):
        print(f"  floor cut in advance for {X:+d}pp ({k}): ${S:,.0f} in 2033 $ = ${S/bond_growth(Y5):,.0f} of 2028 money at 4.82% "
              f"(${S/bond_growth(Y5+X/100):,.0f} if bought after the fall); floor ${m*.75*bond_growth(Y5):,.0f} -> ${m*.75*bond_growth(Y5)-S:,.0f}")
