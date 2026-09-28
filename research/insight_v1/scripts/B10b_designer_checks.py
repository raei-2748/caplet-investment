"""B10b contrarian checks: attack "lock early" from the case designers' side with numbers.

What it computes (all ASSUMPTION-based model outputs, not forecasts):
 1. "Price of certainty" frontier: lock a fraction f of the ten-payment ladder in January 2027, invest the rest of
    the money 60/40 (JPM large cap / intermediate Treasuries) until 2033, then buy the unlocked share of the
    reserve in 2033. Reports P(payments not fully funded) and 2033 surplus p5/p50/p95, with the 2028 deposit at
    $150k and at $75k. (Brief section 8 item 1 covered partial locks only with NO 2028 deposit.)
 2. Equity-funded "bucket" reserve: how much equity in 2033 is needed to pay one of the last $50k payments
    (2040, 2041, 2042) with 95% or 99% probability, versus the Treasury price of that payment.
 3. Duration roll-down of a held ladder from 2033 to 2042 (how the reserve's "composition changes" by itself).
 4. Whole-portfolio equity share path under lock-early (2027, 2028, 2031 after the floor lock).

Inputs and status:
 - $292,264 ladder cost at 2027-01-01 (VERIFIED-REPO-FILE: research/verified_2026-09-27/official_curve_pv.py).
 - JPM 2026 LTCMA: large cap 6.70% compound / 7.94% arithmetic; intermediate Treasuries 4.00% / 4.06%;
   correlation -0.01 (VERIFIED-REPO-FILE: competition/official_market_data/, F-301, F-307, F-314).
 - Forward zeros from 2027 to 2033/2037/2042: 5.08/5.24/5.48% semiannual (F-012); spot duration numbers F-105.
 - 2033 reserve price for unlocked share: flat 5.26% +/- N(0, 1pp), same convention as strategy_mc.py
   (ASSUMPTION; slightly overstates the cost vs forwards, F-408).
 - Forward rates used for the roll-down: flat 5.35% annual from 2033 (ASSUMPTION, near F-012).
 - i.i.d. lognormal annual returns, no fees, no taxes (ASSUMPTION, as in strategy_mc.py).
Run from repo root:  .venv/bin/python research/insight_v1/scripts/B10b_designer_checks.py
"""
import numpy as np

PATHS, SEED = 200_000, 20260927
LADDER = 292_264


def lp(c, a):
    return np.log(1 + c), np.sqrt(2 * np.log((1 + a) / (1 + c)))


EQ, BD, RHO = lp(0.067, 0.0794), lp(0.040, 0.0406), -0.01


def draws(n_years, seed=SEED):
    rng = np.random.default_rng(seed)
    z1 = rng.standard_normal((PATHS, n_years))
    z2 = rng.standard_normal((PATHS, n_years))
    req = np.exp(EQ[0] + EQ[1] * z1) - 1
    rbd = np.exp(BD[0] + BD[1] * (RHO * z1 + np.sqrt(1 - RHO ** 2) * z2)) - 1
    rate33 = 0.0526 + 0.010 * rng.standard_normal(PATHS)
    return req, rbd, rate33


def annuity_due(r):
    t = np.arange(10)
    return (50_000 / (1 + np.maximum(r, 0)[:, None]) ** t).sum(1)


def frontier(dep2028, eq_w=0.60):
    req, rbd, r33 = draws(6)
    res33 = annuity_due(r33)
    out = []
    for f in (1.0, 0.95, 0.90, 0.80, 0.70, 0.50, 0.0):
        s = np.full(PATHS, 300_000 - f * LADDER)
        for y in range(6):
            if y == 1:
                s += dep2028
            s *= 1 + eq_w * req[:, y] + (1 - eq_w) * rbd[:, y]
        surplus = s - (1 - f) * res33
        miss = (surplus < 0).mean()
        p = np.percentile(surplus, [5, 50, 95])
        out.append((f, miss, *p))
    return out


def equity_bucket():
    rows = []
    for year, t in ((2040, 7), (2041, 8), (2042, 9)):
        mu, sd = EQ[0] * t, EQ[1] * np.sqrt(t)
        tsy = 50_000 / (1.0535 ** t)
        for conf, z in ((0.95, 1.645), (0.99, 2.326)):
            need = 50_000 / np.exp(mu - z * sd)
            rows.append((year, conf, need, tsy, need / tsy))
    return rows


def rolldown(r=0.0535):
    rows = []
    for start in range(10):          # 2033 .. 2042, value just BEFORE that year's payment
        t = np.arange(10 - start)
        pv = 50_000 / (1 + r) ** t
        rows.append((2033 + start, pv.sum(), (pv * t).sum() / pv.sum()))
    return rows


if __name__ == "__main__":
    for dep in (150_000, 75_000):
        print(f"\n== Price-of-certainty frontier, 2028 deposit ${dep:,} (60/40 unlocked money, no 2031 floor)")
        print("  lock share | P(payments short) | 2033 surplus p5 / p50 / p95")
        for f, miss, p5, p50, p95 in frontier(dep):
            print(f"  {f:>9.0%} | {miss:>16.2%} | ${p5:>9,.0f} / ${p50:>9,.0f} / ${p95:>9,.0f}")
    print("\n== Equity needed in 2033 to fund one late payment vs Treasury price (JPM large cap, lognormal)")
    for year, conf, need, tsy, ratio in equity_bucket():
        print(f"  {year} payment at {conf:.0%}: equity ${need:,.0f} vs Treasury ${tsy:,.0f} -> {ratio:.2f}x")
    print("\n== Held-ladder roll-down (value and Macaulay duration just before each payment, flat 5.35%)")
    for yr, v, d in rolldown():
        print(f"  {yr}: value ${v:,.0f}, duration {d:.2f} y")
    # 4. whole-portfolio equity share path (lock-early, 60% sleeve equity, 80% floor lock in 2031)
    s27 = 300_000 - LADDER
    print("\n== Whole-portfolio equity share under lock-early (ASSUMPTION: sleeve medians)")
    print(f"  2027-01-01: {0.6 * s27 / 300_000:.1%} (sleeve ${s27:,.0f})")
    print("  2028-01-01: 20.4% (F-409)")
    s31 = 190_000  # ASSUMPTION: rough median sleeve on 2031-01-01 before the floor lock
    ladder31 = 356_384  # F-106
    print(f"  2031-01-01 after 80% floor lock: {0.6 * 0.2 * s31 / (ladder31 + s31):.1%}")
