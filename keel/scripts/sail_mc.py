"""FICTION (Team Keel). How big is the sail? MODEL, not a forecast.

Value on 1 Jan 2033 of the facility+flexibility money ("the sail") for stock shares of the 2028 money of
0/25/50/75/100%. The ten $50k payments are already bought by the 2027 $300k (ladder_pv.py); this is only what is left.

Inputs (state them or don't post the number):
- Stocks: J.P. Morgan Asset Management, 2026 Long-Term Capital Market Assumptions, USD matrix, data as of
  30 Sep 2025, "AC World Equity": compound 7.00%, arithmetic 8.28%, volatility 16.78%. Lognormal yearly returns,
  median growth 7.00%/yr, before fund fees and taxes. Buy and hold 1 Jan 2028 -> 1 Jan 2033, no rebalancing.
- Bonds: one Treasury bought 1 Jan 2028, maturing near 1 Jan 2033, yield = 5y par 4.95% (Treasury par curve,
  21 Oct 2026). Semiannual coupons reinvested at the same yield (MODEL); FLOOR_NOREINV shows reinvestment at 2.95%.
- 2027 leftover: $300,000 minus ladder cost (ladder_pv.py), held one year at the 1y par 4.52%, joins on 1 Jan 2028.
- Rate shock for thread 2: parallel normal shift of the whole curve, vol 90bp/yr (MODEL/UNVERIFIED assumption,
  not fetched), scaled by sqrt(time) to 1 Jan 2027.
Run: python3 sail_mc.py
"""
from datetime import date
import numpy as np
from ladder_pv import cost, VAL

N, SEED = 200_000, 2033
EQ_G, EQ_VOL = 0.0700, 0.1678          # JPM 2026 LTCMA AC World compound / vol
Y5, Y1 = 0.0495, 0.0452                # par curve 21 Oct 2026
YEARS = 5
SHARES = [0, .25, .50, .75, 1.00]
RATE_VOL_BP = 90.0                     # MODEL/UNVERIFIED
DEP28 = 150_000

sig = np.sqrt(np.log(1 + (EQ_VOL / (1 + 0.0828)) ** 2))   # log-vol matching 16.78% arithmetic vol
mu = np.log(1 + EQ_G)                                       # median compound 7.00%
rng = np.random.default_rng(SEED)
eq = np.exp(rng.normal(mu, sig, (N, YEARS)).sum(1))         # growth of $1 in stocks, 2028-2032


def bond_growth(y, reinv=None):
    reinv = y if reinv is None else reinv
    c, n = y / 2, 2 * YEARS
    return 1 + c * sum((1 + reinv / 2) ** k for k in range(n))  # principal + coupons reinvested


C0 = cost()
LEFT = (300_000 - C0) * (1 + Y1)


def sail(share, money, eqpath=eq, y=Y5):
    return money * (1 - share) * bond_growth(y) + money * share * eqpath


def fmt(x):
    return f"${x / 1000:,.0f}k"


if __name__ == "__main__":
    money = DEP28 + LEFT
    print(f"Ladder cost 1 Jan 2027 ${C0:,.0f}, leftover then ${300_000 - C0:,.0f}; 2028 money ${money:,.0f}")
    print(f"Bond growth x{bond_growth(Y5):.4f} (x{bond_growth(Y5, Y5 - .02):.4f} if coupons reinvested 2pt lower)")
    base0 = sail(0, money)[()] if np.ndim(sail(0, money)) else sail(0, money)
    print("\nshare | p5 | p25 | p50 | p75 | p95 | floor | below 0% option | stocks -40% 2028-31 then +7% 2032")
    for s in SHARES:
        v = sail(s, money) * np.ones(N)
        q = np.percentile(v, [5, 25, 50, 75, 95])
        floor = money * (1 - s) * bond_growth(Y5)
        stress = money * (1 - s) * bond_growth(Y5) + money * s * 0.60 * 1.07
        print(f"{int(s*100):>3}% | " + " | ".join(fmt(x) for x in q) +
              f" | {fmt(floor)} | {np.mean(v < base0 - 1e-6) * 100:.0f}% | {fmt(stress)}")

    print("\n2028 deposit stress (floor = bond part; p5/p50 of the sail):")
    for dep in (75_000, 0):
        m = dep + LEFT
        for s in (0, .25, .5):
            v = sail(s, m) * np.ones(N)
            print(f"  deposit ${dep:,} share {int(s*100)}%: floor {fmt(m*(1-s)*bond_growth(Y5))} "
                  f"p5 {fmt(np.percentile(v,5))} p50 {fmt(np.percentile(v,50))}")

    # Thread 2: ladder above $300k on 1 Jan 2027
    print("\nThread 2: ladder price on 1 Jan 2027 under a parallel normal yield shock")
    t = (date(2027, 1, 1) - VAL).days / 365.25
    dv = (cost(-.01) - cost(.01)) / 2
    for label, horizon in (("to 1 Jan 2027 (%.2fy)" % t, t), ("one full year", 1.0)):
        sd = RATE_VOL_BP * np.sqrt(horizon)
        shocks = rng.normal(0, sd, 20_000)
        grid = np.linspace(-4 * sd, 4 * sd, 81)
        costs = np.interp(shocks, grid, [cost(g / 100) for g in grid])
        gap = np.maximum(costs - 300_000, 0)
        print(f"  {label}: sd {sd:.0f}bp, P(cost>$300k) {np.mean(gap > 0)*100:.0f}%, "
              f"mean gap if short ${gap[gap>0].mean():,.0f}, p95 gap ${np.percentile(gap,95):,.0f}, "
              f"p99 gap ${np.percentile(gap,99):,.0f}")
    for bp in (-25, -50, -100):
        g = cost(bp / 100) - 300_000
        print(f"  yields {bp}bp: ladder ${cost(bp/100):,.0f}, gap ${max(g,0):,.0f} "
              f"(2028 cost ${max(g,0)*(1+Y1+bp/1e4):,.0f})")

    # Joint bad case: yields -100bp by 1 Jan 2027 (gap topped up from 2028), 5y yield in 2028 3.95%,
    # stocks -40% 2028-31 then +7%.
    g = max(cost(-1.0) - 300_000, 0) * (1 + Y1 - .01)
    m = DEP28 - g
    print(f"\nJoint bad case: yields -100bp, gap ${g:,.0f} paid from 2028 deposit, 5y at 3.95%, stocks -40%:")
    for s in SHARES:
        v = m * (1 - s) * bond_growth(Y5 - .01) + m * s * 0.60 * 1.07
        print(f"  {int(s*100):>3}%: sail {fmt(v)}, floor {fmt(m*(1-s)*bond_growth(Y5-.01))}")
