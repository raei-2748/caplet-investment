"""Laura's 2031 facility-contribution range: what she would quote, and with what confidence.

AI-generated research (Claude Code) for Team Caplet. NOT submission text; log it in the AI-use record.
Basis: the "Roots First" plan in COMPETITION.md s7, WInS-listed securities only (6 Oct Wharton email):
  Jan 2027  $300k buys the ladder (IBTM-IBTR + five T-bonds) for the ten $50k payments.
  Jan 2028  $150k: fill any ladder gap, buy IBTM sized to return the remainder (the floor), rest + 2027 leftover in VT.
  Jan 2031  quote: bottom = floor (rounded down to $5k after any expected ladder shortfall);
            top = floor + half of VT's value that day (rounded down to $1k).
  Jan 2033  gift = min(floor + half of VT, top). Laura keeps the other half.

Run:  python range_2031.py ../assistant_review_2026-10/checks/par_to_16Oct.csv 10/16/2026
Everything is a MODEL. Return assumptions: JPM 2026 LTCMA AC World 7.00% compound, 16.78% vol (VERIFIED, see
CLAUDE.md); historical world equity returns from archive/rab/data/history/annual_history.csv (world_eq, 1872-2025).
"""
import csv
import os
import sys
from datetime import date

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "assistant_review_2026-10", "checks"))
import indep_pricer as P  # noqa: E402

N = 200_000
SEED = 20261016
J27, J28, D32 = date(2027, 1, 1), date(2028, 1, 2), date(2032, 12, 15)
EQ_MU, EQ_VOL = 0.0700, 0.1678          # JPM 2026 LTCMA AC World, compound / vol
VT_FEE, IBTM_FEE = 0.0006, 0.0007        # Vanguard, iShares (insight_v1/securities_and_allocation.md)
RATE_VOL = 0.0090                        # 90bp a year, parallel; sensitivity below
# IBTM is a fund, not a bond: its Dec 2032 payout drifts from the amount it was sized for. rab WS2 (W
# ws2.range.floor_delivery): ~$149.4k median on $150k, below face ~69% of the time, worst ~$146.3k.
# Shortfall share d ~ N(0.4%, 0.8%), so P(d > 0) ~ 69%; the 2031 bottom uses the worst case, 2.5%.
IBTM_DRIFT_MU, IBTM_DRIFT_SD, IBTM_DRIFT_WORST = 0.004, 0.008, 0.025
DV01_27 = 289.0                          # ladder $/bp on 1 Jan 2027 (CLAUDE.md, verified 2026-09-27)
HALF = 0.5


def ladder_cost(c, d0):
    return P.ladder(c, d0, P.BUYABLE) / c.df(P.yf(d0, J27))


def equity_paths(rng, model, years):
    """Gross growth factors per year, shape (N, years), net of VT's fee."""
    if model == "lognormal":
        s = np.sqrt(np.log(1 + EQ_VOL ** 2 / (1 + EQ_MU) ** 2))   # rough match of arithmetic vol
        m = np.log(1 + EQ_MU)
        g = np.exp(rng.normal(m, s, (N, years)))
    elif model == "fat_tails":
        df = 4
        s = np.sqrt(np.log(1 + EQ_VOL ** 2 / (1 + EQ_MU) ** 2))
        t = rng.standard_t(df, (N, years)) / np.sqrt(df / (df - 2))
        g = np.exp(np.log(1 + EQ_MU) + s * t)
    elif model == "history":
        path = os.path.join(HERE, "..", "..", "rab", "data", "history", "annual_history.csv")
        r = np.array([float(x["world_eq"]) for x in csv.DictReader(open(path)) if x["world_eq"]])
        # whole consecutive windows, so crashes and recoveries keep their order
        start = rng.integers(0, len(r) - years + 1, N)
        g = 1 + r[start[:, None] + np.arange(years)]
    else:
        raise ValueError(model)
    return g * (1 - VT_FEE)


def simulate(pts, d0, model, rate_vol=RATE_VOL, half=HALF, seed=SEED):
    rng = np.random.default_rng(seed)
    c = P.Curve(pts)
    base27 = ladder_cost(c, d0)
    fwd_1y = c.df(P.yf(d0, J27)) / c.df(P.yf(d0, J28)) - 1                    # 2027 -> 2028 cash rate
    fwd_df_floor = c.df(P.yf(d0, D32)) / c.df(P.yf(d0, J28))                   # 2028 price of $1 in Dec 2032
    fwd_y5 = fwd_df_floor ** (-1 / (2 * P.yf(J28, D32))) * 2 - 2              # as a semiannual yield

    # rates: one parallel shock to 1 Jan 2027, a second to Jan 2028
    s27 = rng.normal(0, rate_vol * np.sqrt(P.yf(d0, J27)), N)
    s28 = s27 + rng.normal(0, rate_vol * 1.0, N)
    cost27 = base27 - DV01_27 * s27 * 1e4                                      # duration approximation
    left27 = 300_000 - cost27
    topup = np.maximum(0, -left27) * (1 + fwd_1y)
    left28 = np.maximum(0, left27) * (1 + fwd_1y)
    y5 = fwd_y5 + s28
    floor = 150_000 - topup                                                    # IBTM sized to return the remainder
    floor_cost = floor / (1 + y5 / 2) ** (2 * P.yf(J28, D32)) * (1 + IBTM_FEE) ** P.yf(J28, D32)
    vt0 = 150_000 - topup - floor_cost + left28 - 25                           # one $25 VT trade
    payout = floor * (1 - rng.normal(IBTM_DRIFT_MU, IBTM_DRIFT_SD, N))         # what IBTM actually pays

    g = equity_paths(rng, model, 5)                                            # 2028..2032
    vt31 = vt0 * g[:, :3].prod(1)
    vt33 = vt31 * g[:, 3:].prod(1)
    bottom = np.floor(floor * (1 - IBTM_DRIFT_WORST) / 5_000) * 5_000          # cautious payout, rounded down
    top = np.floor((floor * (1 - IBTM_DRIFT_MU) + half * vt31) / 1_000) * 1_000 # expected payout + half of VT
    gift = np.minimum(payout + half * vt33, top)
    return dict(base27=base27, left27=left27, topup=topup, floor=floor, floor_cost=floor_cost, vt0=vt0,
                vt31=vt31, vt33=vt33, payout=payout, bottom=bottom, top=top, gift=gift,
                kept=payout + vt33 - gift,
                fwd_y5=fwd_y5)


def pct(x, q=(5, 50, 95)):
    return " / ".join(f"${v:,.0f}" for v in np.percentile(x, q))


def main():
    path, day = sys.argv[1], sys.argv[2]
    m, d, y = map(int, day.split("/"))
    d0 = date(y, m, d)
    pts = P.load_curve(path, day)

    print(f"Curve {day}: 2y {dict(pts)[2]*100:.2f}%  5y {dict(pts)[5]*100:.2f}%  10y {dict(pts)[10]*100:.2f}%")
    r = simulate(pts, d0, "lognormal")
    print(f"Ladder cost on 1 Jan 2027 (curve unchanged, forward): ${r['base27']:,.0f}; "
          f"headroom ${300_000 - r['base27']:,.0f} = {(300_000 - r['base27'])/DV01_27:.0f}bp")
    print(f"Forward 5y-ish yield for Jan 2028 -> Dec 2032: {r['fwd_y5']*100:.2f}%")
    print(f"P(2028 deposit must top up the ladder): {(r['topup'] > 0).mean()*100:.0f}%; "
          f"top-up p95 ${np.percentile(r['topup'], 95):,.0f}")
    print(f"Floor (IBTM sized for, Dec 2032) p5/p50/p95: {pct(r['floor'])}; cost in Jan 2028 {pct(r['floor_cost'])}")
    print(f"IBTM actual payout p5/p50/p95: {pct(r['payout'])}; below the sized amount "
          f"{(r['payout'] < r['floor']).mean()*100:.0f}%; quoted bottom p5/p50 {pct(r['bottom'], (5, 50))}")
    print(f"VT bought Jan 2028: {pct(r['vt0'])}")
    print()

    hdr = (f"{'model':10s} {'quote bottom':>13s} {'quote top p5 / p50 / p95':>32s} {'P(top)':>7s} "
           f"{'P(>=mid)':>8s} {'gift p5 / p50 / p95':>32s} {'Laura keeps p5 / p50':>22s} {'P(VT<cost 2031)':>15s}")
    print("2031 quote and 2033 outcome, three equity models (rates 90bp/yr)")
    print(hdr)
    rows = []
    for model in ("lognormal", "fat_tails", "history"):
        r = simulate(pts, d0, model)
        p_top = (r["gift"] >= r["top"]).mean()
        mid = (r["bottom"] + r["top"]) / 2
        p_mid = (r["gift"] >= mid).mean()
        p_bot = (r["gift"] >= r["bottom"]).mean()
        print(f"{model:10s} {np.median(r['bottom']):13,.0f} {pct(r['top']):>32s} {p_top*100:6.0f}% "
              f"{p_mid*100:7.1f}% {pct(r['gift']):>32s} {pct(r['kept'], (5, 50)):>22s} "
              f"{(r['vt31'] < r['vt0']).mean()*100:14.0f}%  P(>=bottom) {p_bot*100:.3f}%")
        rows.append(dict(model=model, bottom_median=np.median(r["bottom"]),
                         top_p5=np.percentile(r["top"], 5), top_p50=np.percentile(r["top"], 50),
                         top_p95=np.percentile(r["top"], 95), p_gift_ge_bottom=p_bot, p_gift_reaches_top=p_top,
                         p_gift_ge_midpoint=p_mid, gift_p5=np.percentile(r["gift"], 5),
                         gift_p50=np.percentile(r["gift"], 50), gift_p95=np.percentile(r["gift"], 95)))
    print("P(gift >= bottom) per model is in the CSV (p_gift_ge_bottom).")
    print()

    print("Overpromising trade-off: share of VT promised above the floor (lognormal)")
    print(f"{'share':>6s} {'top p50':>9s} {'P(reach top)':>13s} {'P(>=mid)':>9s} {'gift p50':>9s} {'Laura keeps p5':>15s}")
    for share in (1 / 3, 0.5, 2 / 3, 1.0):
        r = simulate(pts, d0, "lognormal", half=share)
        mid = (r["bottom"] + r["top"]) / 2
        print(f"{share:6.2f} {np.median(r['top']):9,.0f} {(r['gift'] >= r['top']).mean()*100:12.0f}% "
              f"{(r['gift'] >= mid).mean()*100:8.1f}% {np.median(r['gift']):9,.0f} {np.percentile(r['kept'], 5):15,.0f}")
    print()

    print("Sensitivity (lognormal): rate volatility")
    for rv in (0.006, 0.009, 0.012):
        r = simulate(pts, d0, "lognormal", rate_vol=rv)
        print(f"  {rv*1e4:.0f}bp/yr: P(top-up) {(r['topup'] > 0).mean()*100:.0f}%  floor p5 ${np.percentile(r['floor'], 5):,.0f}  "
              f"top p50 ${np.median(r['top']):,.0f}  VT0 p5/p50/p95 {pct(r['vt0'])}")
    print("Sensitivity: parallel yield shift today (deterministic, no rate shocks)")
    for sh in (-0.01, -0.005, 0.0, 0.005):
        c = P.Curve(pts, sh)
        cost = ladder_cost(c, d0)
        print(f"  {sh*1e4:+.0f}bp: ladder ${cost:,.0f}  2028 top-up ${max(0, cost - 300_000):,.0f}  "
              f"floor ${150_000 - max(0, cost - 300_000) * 1.045:,.0f}")

    out = os.path.join(HERE, "range_2031_results.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for row in rows:
            w.writerow({k: (f"{v:.4f}" if isinstance(v, float) and v < 1.0001 else (round(v) if isinstance(v, float) else v))
                        for k, v in row.items()})
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
