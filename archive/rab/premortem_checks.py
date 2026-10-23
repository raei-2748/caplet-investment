"""WS0 pre-mortem rough checks (not headline numbers; WS1/M1 owns the real ones).

Inputs are copied from the team Sheet 1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM, read 30 Sep 2026 (Sydney):
tab "Portfolio" (target units, prices = 28 Sep 2026 WInS closes; bond price there = clean + accrued per $100)
and tab "Book L" (literal ladder: clean price, accrued, face). Volumes: yfinance 20-day daily volume, pulled 30 Sep 2026.
ASSUMPTIONS (ASM): iBonds ETFs treated as a bullet Treasury maturing 15 Dec of their year with a 4% coupon;
settlement 2 Oct 2026; flat reinvestment rate; semiannual compounding. No network. Seed not needed (deterministic).

[1] Cash buffer: how far can yields fall (parallel) before the Portfolio-tab units, bought at 28 Sep prices, overspend $300k?
[2] Reinvestment: literal ladder (Book L) value on each payment date if coupons are reinvested at 0% / 2% / own yield.
"""
from datetime import date

SETTLE = date(2026, 10, 2)


def yf(d):
    return (d - SETTLE).days / 365.25


def bond_flows(coupon, maturity, face):
    """Semiannual coupon dates after SETTLE up to maturity; returns [(t_years, cash)]."""
    flows, y, m = [], maturity.year, maturity.month
    d = maturity
    while d > SETTLE:
        flows.append((yf(d), face * coupon / 2))
        m -= 6
        if m <= 0:
            m += 12
            y -= 1
        d = date(y, m, maturity.day)
    flows = sorted(flows)
    flows[-1] = (flows[-1][0], flows[-1][1] + face)
    return flows


def price(flows, ytm):
    return sum(c / (1 + ytm / 2) ** (2 * t) for t, c in flows)


def solve_ytm(flows, target):
    lo, hi = -0.02, 0.2
    for _ in range(200):
        mid = (lo + hi) / 2
        if price(flows, mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def mod_dur(flows, ytm):
    p0, h = price(flows, ytm), 1e-4
    return -(price(flows, ytm + h) - price(flows, ytm - h)) / (2 * h) / p0


def fv(flows, r, t_pay):
    return sum(c * (1 + r / 2) ** (2 * (t_pay - t)) for t, c in flows)


# Book L literal ladder (Sheet, read 30 Sep 2026): (name, coupon, maturity, face or $value, clean, accrued, pays on)
BONDS = [
    ("T 4.750% Feb-2037", 0.04750, date(2037, 2, 15), 30000, 97.152, 0.560, date(2038, 1, 1)),
    ("T 4.500% May-2038", 0.04500, date(2038, 5, 15), 29000, 94.281, 0.530, date(2039, 1, 1)),
    ("T 4.375% Nov-2039", 0.04375, date(2039, 11, 15), 27000, 91.363, 1.606, date(2040, 1, 1)),
    ("T 4.250% Nov-2040", 0.04250, date(2040, 11, 15), 26000, 89.186, 1.572, date(2041, 1, 1)),
    ("T 3.125% Nov-2041", 0.03125, date(2041, 11, 15), 29000, 76.367, 1.156, date(2042, 1, 1)),
]
# ETF rungs: (ticker, cost $, discount factor to pay date from Book L, end date, pays on)
ETFS = [
    ("IBTM", 36497, 0.729825, date(2032, 12, 15), date(2033, 1, 1)),
    ("IBTO", 34577, 0.691509, date(2033, 12, 15), date(2034, 1, 1)),
    ("IBTP", 32783, 0.655288, date(2034, 12, 15), date(2035, 1, 1)),
    ("IBTQ", 31031, 0.620501, date(2035, 12, 15), date(2036, 1, 1)),
    ("IBTR", 29348, 0.586914, date(2036, 12, 15), date(2037, 1, 1)),
]
ETF_COUPON = 0.04  # ASM

print("[2] Literal ladder: value on each payment date by coupon reinvestment rate (target $50,000)")
print(f"  {'holding':20s} {'own yld':>7s} {'@own':>9s} {'@own-2pp':>9s} {'@2%':>9s} {'@0%':>9s}")
tot = {"own": 0, "m2": 0, "2": 0, "0": 0}
durs = {}
for name, c, mat, face, clean, acc, pay in BONDS:
    fl = bond_flows(c, mat, face)
    dirty = face * (clean + acc) / 100
    y = solve_ytm(fl, dirty)
    durs[name] = mod_dur(fl, y)
    a, m, b, z = fv(fl, y, yf(pay)), fv(fl, y - 0.02, yf(pay)), fv(fl, 0.02, yf(pay)), fv(fl, 0.0, yf(pay))
    tot["own"] += a; tot["m2"] += m; tot["2"] += b; tot["0"] += z
    print(f"  {name:20s} {y*100:6.2f}% {a:9,.0f} {m:9,.0f} {b:9,.0f} {z:9,.0f}")
for tk, cost, df, end, pay in ETFS:
    y_pay = (1 / df) ** (1 / (2 * yf(pay))) - 1  # semiannual rate per half-year to pay date
    y = 2 * y_pay
    unit = bond_flows(ETF_COUPON, end, 100.0)
    face = cost / price(unit, y) * 100
    fl = bond_flows(ETF_COUPON, end, face)
    durs[tk] = mod_dur(fl, y)
    a, m, b, z = fv(fl, y, yf(pay)), fv(fl, y - 0.02, yf(pay)), fv(fl, 0.02, yf(pay)), fv(fl, 0.0, yf(pay))
    tot["own"] += a; tot["m2"] += m; tot["2"] += b; tot["0"] += z
    print(f"  {tk:20s} {y*100:6.2f}% {a:9,.0f} {m:9,.0f} {b:9,.0f} {z:9,.0f}   (ASM bullet, 4% coupon)")
print(f"  total of ten rungs: own-yield ${tot['own']:,.0f}; own-2pp ${tot['m2']:,.0f}; 2% ${tot['2']:,.0f}; 0% ${tot['0']:,.0f}"
      f" (target $500,000)")
print("  (each rung reinvests its own coupons to its own payment date; pooling cash across rungs moves money between"
      " dates but, at a flat rate, does not remove the exposure; a proper cash-flow schedule is WS1/M1's job)")

# [1] Portfolio tab (plan on 2 Jan 2028 scaled to $300k): (holding, units, price per share or per $100 dirty, duration key)
PORT = [
    ("IBTM", 4486, 21.75, "IBTM"), ("IBTO", 1017, 22.99, "IBTO"), ("IBTP", 921, 24.07, "IBTP"),
    ("IBTQ", 886, 23.67, "IBTQ"), ("IBTR", 846, 23.46, "IBTR"),
    ("T 4.750% Feb-2037", 20000, 97.712, "T 4.750% Feb-2037"), ("T 4.500% May-2038", 19000, 94.811, "T 4.500% May-2038"),
    ("T 4.375% Nov-2039", 18000, 92.969, "T 4.375% Nov-2039"), ("T 4.250% Nov-2040", 17000, 90.758, "T 4.250% Nov-2040"),
    ("T 3.125% Nov-2041", 19000, 77.523, "T 3.125% Nov-2041"), ("VT", 164, 158.42, None),
]
COMM = 6 * 25 + 5 * 10
spend = []
for name, u, p, k in PORT:
    v = u * p / 100 if name.startswith("T ") else u * p
    spend.append((name, v, durs.get(k, 0.0)))
base = sum(v for _, v, _ in spend) + COMM
bond_val = sum(v for _, v, d in spend if d)
bond_dur = sum(v * d for _, v, d in spend) / bond_val
print("\n[1] Portfolio tab bought at 28 Sep prices")
print(f"  spend incl. ${COMM} commissions: ${base:,.0f}; cash left ${300000 - base:,.0f}")
print(f"  Treasury part ${bond_val:,.0f}, value-weighted modified duration {bond_dur:.1f}y")
for bp in (5, 10, 15, 20, 25, 30):
    for vt in (0.0, 0.02):
        new = sum(v * (1 + d * bp / 1e4) if d else v * (1 + vt) for _, v, d in spend) + COMM
        print(f"  yields -{bp:2d}bp, VT +{vt*100:.0f}%: spend ${new:,.0f}  cash ${300000 - new:,.0f}")

# [3] Volume: order size vs 20-day median and 20-day minimum daily volume (yfinance, pulled 30 Sep 2026)
VOL = {"IBTM": (148900, 23637), "IBTO": (158050, 36389), "IBTP": (84800, 10523), "IBTQ": (91550, 7044),
       "IBTR": (33500, 7600), "VT": (2014100, 1290522)}
print("\n[3] Order size as % of daily volume (Portfolio tab units; min includes a partial 29 Sep session)")
for name, u, p, k in PORT:
    if name in VOL:
        med, mn = VOL[name]
        print(f"  {name:5s} {u:6,d} sh = {100*u/med:4.1f}% of 20d median, {100*u/mn:5.1f}% of 20d min")
