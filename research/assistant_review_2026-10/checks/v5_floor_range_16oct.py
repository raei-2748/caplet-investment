"""Floor, range and '99 in 100' check for IPS Version 5 (16 Oct 2026). AI check, MODEL numbers.
Floor: IBTM bought 1 Jan 2028 as a par coupon bond to 15 Dec 2032 (forward curve), sized to deliver $150,000 on
1 Jan 2033 with distributions reinvested at its own yield. We then shock the reinvestment rate.
Range: bottom = $145,000 quote; top = $150,000 + half the stock fund in 2031; gift = floor delivered + half the fund
in 2033, capped at the top. Stock fund: lognormal, 7.0% compound, 16.8% vol (JPM 2026 LTCMA AC World, repo CLAUDE.md).
Usage: python3 v5_floor_range_16oct.py tsy_202610_new.csv 10/15/2026
"""
import os
import sys
from datetime import date
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_pricer as ip  # noqa: E402

D28, MAT, PAY = date(2028, 1, 1), date(2032, 12, 15), date(2033, 1, 1)


def main(path, day):
    m, d, y = map(int, day.split("/"))
    d0 = date(y, m, d)
    c = ip.Curve(ip.load_curve(path, day))
    fwd = lambda t: c.df(ip.yf(d0, t)) / c.df(ip.yf(d0, D28))
    ts = [t for t, _ in ip.bond_flows(5.0, MAT, D28)[0]]
    cpn = 100 * (1 - fwd(MAT)) / (sum(fwd(t) for t in ts) / 2)
    fl = ip.bond_flows(cpn, MAT, D28)[0]
    price = sum(cf * fwd(t) for t, cf in fl)
    ytm = ip.ytm_from_dirty(price, cpn, MAT, D28)
    dlv = lambda r: sum(cf * (1 + r / 2) ** (2 * ip.yf(t, PAY)) for t, cf in fl)
    face = 150_000 / dlv(ytm) * 100
    cost = face * price / 100
    print(f"{day}: floor forward yield {ytm*100:.2f}%; cost in Jan 2028 ${cost:,.0f}; left for stocks ${150000-cost:,.0f}")
    for s in (-0.01, -0.02, -0.03, -0.04):
        print(f"   reinvest {s*100:+.0f}pp for good: floor delivers ${face*dlv(ytm+s)/100:,.0f}")
    # range simulation; 2027 leftover added to the fund (where it sits is undecided; see Tab 15 #1)
    ladder_cost = float(sys.argv[3]) if len(sys.argv) > 3 else 297_800
    fund0 = (150_000 - cost) + max(0.0, 300_000 - ladder_cost)
    rng = np.random.default_rng(0)
    n = 200_000
    mu, vol = np.log(1.07), 0.168
    g31 = np.exp(rng.normal(mu - 0 * vol**2, vol, (n, 3)).sum(1))       # Jan 2028 -> Jan 2031
    g33 = np.exp(rng.normal(mu, vol, (n, 2)).sum(1))                     # Jan 2031 -> Jan 2033
    f31, f33 = fund0 * g31, fund0 * g31 * g33
    top = 150_000 + f31 / 2
    floor_dlv = face * dlv(ytm - 0.02) / 100                             # stressed floor: yields -2pp for good
    gift = np.minimum(floor_dlv + f33 / 2, top)
    print(f"   stock fund Jan 2028 ${fund0:,.0f} (incl. 2027 leftover ${max(0,300000-ladder_cost):,.0f}); "
          f"range 'today' $145,000 - ${150000+fund0/2:,.0f}")
    print(f"   2031 top p5/p50/p95 ${np.percentile(top,5):,.0f} / ${np.percentile(top,50):,.0f} / ${np.percentile(top,95):,.0f}")
    print(f"   gift (floor stressed -2pp) p5/p50/p95 ${np.percentile(gift,5):,.0f} / ${np.percentile(gift,50):,.0f} / "
          f"${np.percentile(gift,95):,.0f}; below $145,000 in {np.mean(gift<145_000)*100:.3f}% of paths; "
          f"at the cap in {np.mean(gift>=top-1)*100:.0f}%")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
