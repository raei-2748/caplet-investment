"""Independent audit of the Final Report's numbers (28 Nov 2026). MODEL, not a forecast.

Written from scratch for the audit. It does not import or read any file in keel/final_report/numbers/. Inputs:
  * the 6 Nov 2026 Treasury par curve (treasury.gov, re-read 28 Nov 2026; identical to
    competition/official_market_data/daily-treasury-rates_2026-11-06.csv),
  * the five bonds' terms (coupon, maturity),
  * each iBonds fund's ACTUAL holdings (data/ibonds_holdings.csv, ishares.com),
  * the draft's stated rules (no interest on early receipts, 0.15% a year on waiting cash, fund payouts cut 0.5%,
    0.07% fund fee, 0.06% VT fee, 7.5% world-share growth, 17.88% volatility).

Where the existing engine made a simplifying choice, this file makes a different, more literal one, so agreement is
evidence and not an echo:
  * curve: par yields interpolated with a monotone cubic (PCHIP), bills read as money-market yields, bootstrapped
    semiannually, zero rates interpolated with PCHIP (the engine: linear par, log-linear discount factors);
    a Nelson-Siegel-Svensson fit is the second method;
  * funds: each fund's real Treasury notes, coupons and maturities, with principal held inside the fund to its
    15 December end (the engine: one par bond at the fund's average maturity, coupon = par yield);
  * fees: 0.07% a year charged on the fund's net assets month by month (the engine: (1 - fee)^t on each flow).
"""
import csv
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
VAL = date(2026, 11, 6)
J27, J28, J31, J33 = date(2027, 1, 1), date(2028, 1, 1), date(2031, 1, 1), date(2033, 1, 1)
PAY = 50_000.0
YEARS = list(range(2033, 2043))
FUND_FEE, VT_FEE, WAIT_FEE, CUT = 0.0007, 0.0006, 0.0015, 0.005

# treasury.gov par yield curve, 6 Nov 2026 (bond-equivalent, %)
PAR_6NOV = {1 / 12: 4.02, 1.5 / 12: 4.07, 2 / 12: 4.15, 3 / 12: 4.19, 4 / 12: 4.19, 6 / 12: 4.23, 1: 4.33, 2: 4.51,
            3: 4.59, 5: 4.64, 7: 4.74, 10: 4.86, 20: 5.29, 30: 5.26}


def yf(d1, d2):
    return (d2 - d1).days / 365.25


def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    # end-of-month rule: keep month-end notes at month end
    last = (date(y + (mo == 12), mo % 12 + 1, 1) - timedelta(days=1)).day
    if d.day >= 28 and (d + timedelta(days=1)).month != d.month:
        return date(y, mo, last)
    return date(y, mo, min(d.day, last))


# ------------------------------------------------------------------------------------------------ curves
class Curve:
    """Zero curve from VAL. zc(t) continuously compounded zero rate; df(t) = exp(-zc t)."""

    def __init__(self, ts, zs):
        self.f = PchipInterpolator(ts, zs, extrapolate=True)

    def df_t(self, t):
        t = max(t, 0.0)
        return math.exp(-float(self.f(t)) * t) if t > 0 else 1.0

    def df(self, d):
        return self.df_t(yf(VAL, d))

    def P(self, d1, d2):
        """Forward discount factor from d1 to d2 (d1 <= d2)."""
        return self.df(d2) / self.df(d1)

    def fwd_cc(self, d1, d2):
        tau = yf(d1, d2)
        return -math.log(self.P(d1, d2)) / tau if tau > 0 else 0.0


def bootstrap_pchip(par=PAR_6NOV, shift=0.0):
    """Method B (the audit's own). Bills (<= 6 months) as money-market yields; 1y as a bill's coupon-equivalent
    (two half-year periods); 2y-30y par bonds with semiannual coupons on par yields interpolated by PCHIP."""
    ts = sorted(par)
    ys = np.array([par[t] / 100 + shift for t in ts])
    pf = PchipInterpolator(ts, ys)
    knots_t, knots_z = [], []
    for t in [x for x in ts if x <= 0.5]:
        y = float(pf(t))
        d = 1 / (1 + y * t)
        knots_t.append(t); knots_z.append(-math.log(d) / t)
    dfs = {0.5: math.exp(-knots_z[-1] * 0.5)}
    # semiannual grid from 1.0 to 30.0
    for k in range(2, 61):
        t = k / 2
        c = float(pf(t)) / 2
        s = sum(dfs[j / 2] for j in range(1, k))
        dfs[t] = (1 - c * s) / (1 + c)
        knots_t.append(t); knots_z.append(-math.log(dfs[t]) / t)
    return Curve(np.array(knots_t), np.array(knots_z))


def nss_fit(par=PAR_6NOV, shift=0.0):
    """Method C: Nelson-Siegel-Svensson zero curve fitted to the par yields (least squares on par yields)."""
    ts = np.array(sorted(par)); ys = np.array([par[t] / 100 + shift for t in ts])

    def z(t, b):
        b0, b1, b2, b3, l1, l2 = b
        t = np.maximum(t, 1e-6)
        x1, x2 = t / l1, t / l2
        f1 = (1 - np.exp(-x1)) / x1
        return b0 + b1 * f1 + b2 * (f1 - np.exp(-x1)) + b3 * ((1 - np.exp(-x2)) / x2 - np.exp(-x2))

    def par_model(b):
        out = []
        for t in ts:
            if t <= 0.5:
                d = math.exp(-z(t, b) * t)
                out.append((1 / d - 1) / t)
            else:
                n = int(round(t * 2))
                grid = np.arange(1, n + 1) / 2
                d = np.exp(-z(grid, b) * grid)
                out.append(2 * (1 - d[-1]) / d.sum())
        return np.array(out)

    res = least_squares(lambda b: par_model(b) - ys, x0=[0.05, -0.01, -0.01, 0.01, 2.0, 10.0],
                        bounds=([-0.2, -0.2, -0.5, -0.5, 0.05, 0.5], [0.2, 0.2, 0.5, 0.5, 30, 60]))
    b = res.x
    grid = np.r_[np.linspace(0.02, 1, 50), np.arange(1.5, 40.5, 0.5)]
    c = Curve(grid, z(grid, b))
    c.fit_err_bp = float(np.max(np.abs(res.fun)) * 1e4)
    return c


# ------------------------------------------------------------------------------------------------ instruments
class Bond:
    def __init__(self, name, cpn, mat):
        self.name, self.cpn, self.mat = name, cpn, mat
        ds, k = [], 0
        while True:
            d = add_months(mat, -6 * k)
            if d <= date(2020, 1, 1):
                break
            ds.append(d); k += 1
        self.cdates = sorted(ds)

    def flows(self, after, face=1.0):
        out = [(d, face * self.cpn / 200) for d in self.cdates if d > after]
        if out:
            out[-1] = (out[-1][0], out[-1][1] + face)
        return out

    def accrued(self, settle, face=1.0):
        prev = max(d for d in self.cdates if d <= settle)
        nxt = min(d for d in self.cdates if d > settle)
        return face * self.cpn / 200 * (settle - prev).days / (nxt - prev).days

    def dirty(self, curve, at):
        return sum(a * curve.P(at, d) for d, a in self.flows(at))


BONDS = {2038: Bond("4.750% 15 Feb 2037", 4.750, date(2037, 2, 15)),
         2039: Bond("4.500% 15 May 2038", 4.500, date(2038, 5, 15)),
         2040: Bond("4.375% 15 Nov 2039", 4.375, date(2039, 11, 15)),
         2041: Bond("4.250% 15 Nov 2040", 4.250, date(2040, 11, 15)),
         2042: Bond("3.125% 15 Nov 2041", 3.125, date(2041, 11, 15))}
FUND_FOR = {2033: "IBTM", 2034: "IBTO", 2035: "IBTP", 2036: "IBTQ", 2037: "IBTR"}


def load_holdings():
    out = {}
    exact = {4.13: 4.125, 2.88: 2.875, 1.88: 1.875, 3.88: 3.875, 4.38: 4.375, 4.63: 4.625}
    for r in csv.DictReader(open(HERE / "data/ibonds_holdings.csv")):
        f = out.setdefault(r["fund"], {"notes": [], "cash": 0.0})
        if r["cusip"] == "CASH":
            f["cash"] += float(r["par"])
        else:
            c = float(r["coupon"]); c = exact.get(round(c, 2), c)
            m = date.fromisoformat(r["maturity"])
            f["notes"].append((float(r["par"]), Bond(r["cusip"], c, m)))
    return out


HOLD = load_holdings()


class Fund:
    """An iBonds term Treasury fund modelled from its real holdings.
    Each note pays its coupons to the fund; the fund distributes coupon income (less its fee) when received; principal
    of maturing notes waits inside the fund (money-market) to the fund's end, 15 Dec of its year, then is paid out.
    The fee (0.07% a year) is charged monthly on net assets, valued on the forward curve."""

    def __init__(self, ticker, year):
        self.t, self.year = ticker, year
        self.end = date(year - 1, 12, 15)
        h = HOLD[ticker]
        self.notes, self.cash0 = h["notes"], h["cash"]

    def nav_gross(self, curve, at, cash=None):
        v = sum(p * b.dirty(curve, at) for p, b in self.notes if b.mat > at)
        return v + (self.cash0 if cash is None else cash)

    def per_dollar_flows(self, curve, buy, world, cut=0.0):
        """Flows to the holder of $1 of net assets bought on date `buy`. world: 'fwd' (fund's own cash earns the
        forward short rate) or 'zero' (it earns nothing). Returns list of (date, amount), the final one on self.end."""
        # notes outstanding at purchase; matured principal before `buy` is already in cash at NAV
        nav0 = self.nav_gross(curve, buy)
        scale = 1.0 / nav0
        # build a monthly calendar from buy to end
        events = {}
        for p, b in self.notes:
            for d, a in b.flows(buy, p):
                if d <= self.end:
                    events.setdefault(d, [0.0, 0.0])
                    if d == b.mat:
                        events[d][0] += p * b.cpn / 200
                        events[d][1] += p
                    else:
                        events[d][0] += a
        cash = self.cash0 + sum(p for p, b in self.notes if b.mat <= buy)
        flows = []
        d = buy
        while d < self.end:
            nd = min(add_months(d, 1), self.end)
            # value of the fund at d (forward) for the fee
            live = [(p, b) for p, b in self.notes if b.mat > d]
            nav = sum(p * b.dirty(curve, d) for p, b in live) + cash
            fee = nav * FUND_FEE * yf(d, nd)
            inc = sum(v[0] for dd, v in events.items() if d < dd <= nd)
            prin = sum(v[1] for dd, v in events.items() if d < dd <= nd)
            grow = (1 / curve.P(d, nd) - 1) if world == "fwd" else 0.0
            cash_int = cash * grow
            cash += prin + cash_int - max(fee - inc, 0.0)
            dist = max(inc - fee, 0.0)
            if dist > 0:
                flows.append((nd, dist * scale * (1 - cut)))
            d = nd
        flows.append((self.end, cash * scale * (1 - cut)))
        return flows


def instrument_flows(year, curve, buy, world, cut=0.0):
    """Flows per $1 of market value bought on `buy` (bonds: per $1 of dirty price; funds: per $1 of NAV)."""
    if year in BONDS:
        b = BONDS[year]
        px = b.dirty(curve, buy)
        return [(d, a / px) for d, a in b.flows(buy)]
    return Fund(FUND_FOR[year], year).per_dollar_flows(curve, buy, world, cut)


def fv_at(flows, target, curve, world, wait_fee=0.0):
    """Value on `target` of flows arriving before it: reinvested at forwards ('fwd') or held as cash ('zero'),
    less a waiting fee a year in either world if given."""
    tot = 0.0
    for d, a in flows:
        if d > target:
            continue
        g = 1 / curve.P(d, target) if world == "fwd" else 1.0
        tot += a * g * (1 - wait_fee) ** yf(d, target)
    return tot
