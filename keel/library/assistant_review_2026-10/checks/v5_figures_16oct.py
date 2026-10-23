"""Check the figures added to IPS Version 5 on 16 Oct 2026 (AI check, not submission text).
1) ladder cost on the latest curves; 2) coupon/distribution reinvestment shortfall if yields fall 2pp for good.
Basis: each rung = an instrument maturing before its payment (iBond ETFs as par coupon bonds ending 15 Dec,
T-bonds with their actual coupons), bought 1 Jan 2027 at curve yields, sized so it delivers $50,000 on its
payment date when income is reinvested at the instrument's own yield. Reinvestment = semiannual compounding.
Usage: python3 v5_figures_16oct.py tsy_202610_new.csv 10/15/2026
"""
import sys
from datetime import date
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_pricer as ip  # noqa: E402

RUNGS = [  # (name, coupon or None for par, maturity, payment)
    ("IBTM", None, date(2032, 12, 15), date(2033, 1, 1)), ("IBTO", None, date(2033, 12, 15), date(2034, 1, 1)),
    ("IBTP", None, date(2034, 12, 15), date(2035, 1, 1)), ("IBTQ", None, date(2035, 12, 15), date(2036, 1, 1)),
    ("IBTR", None, date(2036, 12, 15), date(2037, 1, 1)), ("T4.750 Feb37", 4.750, date(2037, 2, 15), date(2038, 1, 1)),
    ("T4.500 May38", 4.500, date(2038, 5, 15), date(2039, 1, 1)), ("T4.375 Nov39", 4.375, date(2039, 11, 15), date(2040, 1, 1)),
    ("T4.250 Nov40", 4.250, date(2040, 11, 15), date(2041, 1, 1)), ("T3.125 Nov41", 3.125, date(2041, 11, 15), date(2042, 1, 1)),
]
D27 = date(2027, 1, 1)


def flows(cpn, mat):
    f, _ = ip.bond_flows(cpn, mat, D27)
    return f  # per 100 face


def deliver(cpn, mat, pay, r):
    """Value on the payment date per 100 face, all cash reinvested at r (semiannual)."""
    return sum(cf * (1 + r / 2) ** (2 * ip.yf(d, pay)) for d, cf in flows(cpn, mat))


def main(path, day):
    m, d, y = map(int, day.split("/"))
    d0 = date(y, m, d)
    c = ip.Curve(ip.load_curve(path, day))
    fwd = lambda t: c.df(ip.yf(d0, t)) / c.df(ip.yf(d0, D27))  # forward discount to 1 Jan 2027
    tot_cost = 0
    base_tot = {}
    for shock in (0.0, -0.02, None):
        short = 0
        for name, cpn, mat, pay in RUNGS:
            # par coupon for iBond stand-ins from the forward curve
            if cpn is None:
                fl = [t for t, _ in ip.bond_flows(5.0, mat, D27)[0]]
                ann = sum(fwd(t) for t in fl) / 2
                cpn = 100 * (1 - fwd(mat)) / ann
            price = sum(cf * fwd(t) for t, cf in flows(cpn, mat))  # dirty per 100 at 1 Jan 2027
            ytm = ip.ytm_from_dirty(price, cpn, mat, D27)
            face = 50_000 / deliver(cpn, mat, pay, ytm) * 100
            if shock == 0.0:
                tot_cost += face * price / 100
            r = 0.0 if shock is None else ytm + shock
            short += 50_000 - face * deliver(cpn, mat, pay, r) / 100
        label = "0% reinvestment" if shock is None else f"reinvest at own yield {shock*100:+.0f}pp"
        print(f"  {label}: total short ${short:,.0f}")
    print(f"{day}: ladder cost at 1 Jan 2027 (coupon basis) ${tot_cost:,.0f}; headroom ${300000-tot_cost:,.0f}")


if __name__ == "__main__":
    for day in sys.argv[2:]:
        main(sys.argv[1], day)
