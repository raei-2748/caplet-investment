"""The Final Report's one numbers engine (Keel, Mon 9 Nov 2026). MODEL, not a forecast or a promise.

What it models: Caplet's FINAL design as submitted on 7 Nov 2026 (`keel/final_report/FINAL_IPS_as_submitted.txt`):
  Jan 2027  the $300,000 deposit buys ten Treasuries, one per payment (the frozen WInS book's instruments:
            iBond funds IBTM, IBTO, IBTP, IBTQ, IBTR for 2033-2037; the 4.750% Feb-2037, 4.500% May-2038,
            4.375% Nov-2039, 4.250% Nov-2040 and 3.125% Nov-2041 T-bonds for 2038-2042);
  Jan 2028  the $150,000 deposit first completes the ladder if it cost more than $300,000; "most" of the rest buys a
            Treasury fund maturing late 2032 (IBTM: the floor); the rest buys VT (the ceiling);
  2031      before the co-sponsor meetings, half of VT moves into Treasuries (here: IBTM again, maturing late 2032);
            the other half is promised to no one;
  2033      the ladder is the operating reserve; the gift is between the floor and floor + the moved half.

Curve: US Treasury daily par yield curve, Fri 6 Nov 2026 close (the day trading froze), treasury.gov CSV in
`competition/official_market_data/daily-treasury-rates_2026-11-06.csv`. Method A, the same as
`keel/scripts/ladder_pv.py` and `ladder_history.py`: par yields read as semiannual bond-equivalent yields,
interpolated on a half-year grid, bootstrapped, log-linear discount factors. Values are forward values on 1 Jan 2027.

Every other input is stated in `ASSUMPTIONS` below and in `keel/final_report/NUMBERS.md`.
"""
import csv
import math
from datetime import date
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-11-06.csv"
CURVE_DAY = "11/06/2026"
VAL = date(2026, 11, 6)
J27, J28, J31, J33 = date(2027, 1, 1), date(2028, 1, 1), date(2031, 1, 1), date(2033, 1, 1)
PAYMENT = 50_000.0
YEARS = list(range(2033, 2043))
TENORS = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
          "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}

ASSUMPTIONS = {
    "fund_end": "iBond funds terminate 'on or about' 15 Dec of their year (ishares.com IBTM page, read 9 Nov 2026)",
    "fund_fee": 0.0007,   # iBonds expense ratio 0.07% (ishares.com, read 9 Nov 2026)
    "vt_fee": 0.0006,     # VT expense ratio 0.06% (TNA note 3; Vanguard)
    # Weighted average maturity of each fund's holdings (years, as of 4 Nov 2026, ishares.com, recorded in
    # keel/scripts/holdings_ladder.py). The holdings mature about then; the money then waits in cash until 15 Dec.
    "fund_wam": {2033: 5.65, 2034: 6.62, 2035: 7.66, 2036: 8.65, 2037: 9.53},
    # Coupons of the funds' holdings: modelled as the curve's par yield to the WAM date (IBTM's own weighted average
    # coupon is 3.50%, so this overstates the interest to be reinvested: conservative for the reinvestment test).
    "eq_growth": 0.075,   # J.P. Morgan 2027 LTCMA, global equities 7.5% (USD), press release 19 Oct 2026 (TNA's figure)
    "eq_vol": 0.1788,     # J.P. Morgan 2027 LTCMA, AC World equity volatility (USD matrix, estimates as of 30 Sep
                          # 2026; row "AC World Equity 7.50 8.94 17.88 7.00", read 9 Nov 2026); same edition as eq_growth
    "yield_vol": 0.009,   # yearly s.d. of Treasury yield changes for the 2027-2031 purchases (MODEL assumption, as in
                          # keel/scripts/sail_mc.py; history replay is run beside it)
    "floor_share": 0.733, # share of the 2028 money left after completing the ladder that buys the floor: the frozen
                          # WInS book's split (3,361 IBTM shares x $21.65 = $72,766 floor stand-in against 167 VT x
                          # $158.83 = $26,525; attribution pack of 20 Oct). FINAL says only "most".
}


def yf(d, base=VAL):
    return (d - base).days / 365.25


def load_par(path=CURVE_CSV, day=CURVE_DAY):
    for r in csv.DictReader(open(path)):
        if r["Date"] == day:
            return {t: float(r[k]) for k, t in TENORS.items()}
    raise SystemExit(f"{day} not in {path}")


class Curve:
    """Method A bootstrap. df(t) from VAL; P(d) = discount factor from 1 Jan 2027 to date d."""

    def __init__(self, par, shift=0.0):
        ts = sorted(par)
        grid = np.arange(0.5, 30.01, 0.5)
        p = np.interp(grid, ts, [par[t] / 100 + shift for t in ts])
        df = []
        for y in p:
            c = y / 2
            df.append((1 - c * sum(df)) / (1 + c))
        self.g, self.lz = np.r_[0, grid], np.log(np.r_[1, df])
        self.par = par

    def df(self, t):
        return float(np.exp(np.interp(t, self.g, self.lz)))

    def P(self, d, base=J27):
        return self.df(yf(d)) / self.df(yf(base))

    def fwd(self, d1, d2):
        """Continuously compounded forward rate between two dates."""
        tau = (d2 - d1).days / 365.25
        return math.log(self.P(d1) / self.P(d2)) / tau if tau > 0 else 0.0


def ladder_cost(curve):
    """Forward value on 1 Jan 2027 of ten $50,000 payments on 1 Jan 2033..2042 (the payment-date basis)."""
    return sum(PAYMENT * curve.P(date(y, 1, 1)) for y in YEARS)


# ---------------------------------------------------------------- the ten instruments, as cash flows from 1 Jan 2027

BONDS = {2038: ("4.750% T-bond 15 Feb 2037", 4.750, date(2037, 2, 15)),
         2039: ("4.500% T-bond 15 May 2038", 4.500, date(2038, 5, 15)),
         2040: ("4.375% T-bond 15 Nov 2039", 4.375, date(2039, 11, 15)),
         2041: ("4.250% T-bond 15 Nov 2040", 4.250, date(2040, 11, 15)),
         2042: ("3.125% T-bond 15 Nov 2041", 3.125, date(2041, 11, 15))}
FUNDS = {2033: "IBTM", 2034: "IBTO", 2035: "IBTP", 2036: "IBTQ", 2037: "IBTR"}


def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    return date(d.year + y, mo + 1, min(d.day, 28))


def coupon_dates(mat, start=J27):
    out, k = [], 0
    while True:
        d = add_months(mat, -6 * k)
        if d <= start:
            break
        out.append(d)
        k += 1
    return sorted(out)


class Instrument:
    """Cash flows per unit bought on 1 Jan 2027, and its forward price. Flows are (date, amount, kind)."""

    def __init__(self, year, curve):
        self.year = year
        self.pay_date = date(year, 1, 1)
        if year in BONDS:
            self.name, cpn, mat = BONDS[year]
            self.flows = [(d, cpn / 200, "coupon") for d in coupon_dates(mat)]
            self.flows[-1] = (mat, cpn / 200 + 1.0, "principal")
            self.end = mat
            self.price = sum(a * curve.P(d) for d, a, _ in self.flows)   # forward dirty price per 1 face
            self.cash_wait = None
        else:
            self.name = FUNDS[year]
            fee = ASSUMPTIONS["fund_fee"]
            self.end = date(year - 1, 12, 15)
            wam = add_months(date(2026, 11, 4), round(ASSUMPTIONS["fund_wam"][year] * 12))
            self.hold_mat = wam
            cds = coupon_dates(wam)
            # par coupon to the WAM date on this curve (a par bond bought 1 Jan 2027 costs 1.0)
            ann = sum(curve.P(d) for d in cds) / 2
            cpn = (1 - curve.P(wam)) / ann
            flows = [(d, cpn / 2, "coupon") for d in cds]
            flows[-1] = (wam, cpn / 2 + 1.0, "holdings mature")
            # the fee is charged on net assets: each flow is smaller by (1-fee)^years since purchase
            self.flows = [(d, a * (1 - fee) ** yf(d, J27), k) for d, a, k in flows]
            self.price = 1.0
            self.cash_wait = (wam, self.end)   # the fund holds cash from its holdings' maturity to its end
        self.unit_value_base = None


def instruments(curve):
    return {y: Instrument(y, curve) for y in YEARS}


# ---------------------------------------------------------------- reinvestment worlds

class Reinvest:
    """How much $1 received on date d1 grows to by date d2, locked at d1 (buy a Treasury maturing at d2).
    kind: 'base' = today's forward rates; 'shift' = forward rates lower by s (floored at zero);
    'zero' = money earns nothing; 'hist' = forward rates times the ratio of a historical 1-year Treasury yield to its
    value at the window's start (proportional, as in keel/models/ASSUMPTIONS.md A35)."""

    def __init__(self, curve, kind="base", s=0.0, mult=None):
        self.c, self.kind, self.s, self.mult = curve, kind, s, mult

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        tau = (d2 - d1).days / 365.25
        if self.kind == "zero":
            return 1.0
        f = self.c.fwd(max(d1, J27), d2)
        if self.kind == "shift":
            f = max(f - self.s, 0.0) if d1 > J27 else f
        elif self.kind == "hist":
            f = f * self.mult(d1)
        return math.exp(f * tau)


def next_payment(d):
    """The payment a cash flow received on date d is held for: the first 1 Jan on or after d, never before 2033."""
    y = d.year if (d.month, d.day) == (1, 1) else d.year + 1
    return max(y, 2033)


def fund_terminal(inst, world):
    """Value on the fund's end date (15 Dec) of one unit's flows that arrive before its end, held inside the fund
    (the holdings' maturities wait in cash until the end): used for the NAV-not-par test."""
    return sum(a * world.grow(d, inst.end) for d, a, _ in inst.flows)


def rung_flows(inst, world):
    """Each instrument's flows, with the iBond fund's final payout arriving on 15 Dec as one amount (its NAV),
    the money inside the fund having waited in cash at the world's short rate."""
    if inst.cash_wait is None:
        return inst.flows
    out = [(d, a, k) for d, a, k in inst.flows if k == "coupon"]
    wam, end = inst.cash_wait
    last = [a for d, a, k in inst.flows if k != "coupon"][0]
    out.append((end, last * world.grow(wam, end), "fund payout (NAV)"))
    return out


def size_own_rung(insts, world):
    """Design A: each rung's flows are reinvested to its own payment date. Units so it delivers $50,000 in `world`."""
    units = {}
    for y, inst in insts.items():
        fv = sum(a * world.grow(d, date(y, 1, 1)) for d, a, _ in rung_flows(inst, world))
        units[y] = PAYMENT / fv
    return units


def _buckets(insts, units, world):
    """Money that reaches each payment date from the flows earmarked for it (each flow is held, at the rate locked
    the day it arrives, until the first payment on or after its arrival, never before 2033)."""
    b = {y: 0.0 for y in YEARS}
    own = {y: 0.0 for y in YEARS}
    for y2, u in units.items():
        for d, a, _ in rung_flows(insts[y2], world):
            ny = next_payment(d)
            if ny in b:
                v = a * world.grow(d, date(ny, 1, 1))
                b[ny] += u * v
                if ny == y2:
                    own[y2] += v
    return b, own


def size_matched(insts, world, iters=400, fixed=None, floor=None):
    """Design B (cash-flow matched, a dedicated portfolio in Leibowitz's sense): every flow is held only until the next
    payment date; later bonds' coupons help pay earlier payments; flows before 2033 are held for 2033; any surplus
    is carried to the next payment at the rate locked that day. Units are found by fixed-point iteration so that every
    payment is exactly met in `world` with as little surplus as possible."""
    fixed = fixed or {}
    units = size_own_rung(insts, world)
    units.update(fixed)
    for y, lb in (floor or {}).items():
        units[y] = max(units[y], lb)
    for _ in range(iters):
        b, own = _buckets(insts, units, world)
        carry = 0.0
        new = {}
        for y in YEARS:
            others = b[y] - units[y] * own[y]
            need = PAYMENT - others - carry
            new[y] = fixed[y] if y in fixed else max(need / own[y], (floor or {}).get(y, 0.0), 0.0)
            avail = others + carry + new[y] * own[y]
            carry = max(avail - PAYMENT, 0.0) * (world.grow(date(y, 1, 1), date(y + 1, 1, 1)) if y < 2042 else 0)
        if max(abs(new[y] - units[y]) for y in YEARS) < 1e-6:
            units = new
            break
        units = {y: 0.5 * units[y] + 0.5 * new[y] for y in YEARS}
    return units


def cost(insts, units):
    return sum(units[y] * insts[y].price for y in YEARS)


def deliver(insts, units, world, pooled):
    """What each payment date actually receives. pooled=False: own rung (design A); True: matched (design B), with any
    surplus carried to the next payment at the rate locked that day. Returns list of (year, delivered)."""
    out = []
    if not pooled:
        carry = 0.0
        for y in YEARS:
            avail = carry + sum(units[y] * a * world.grow(d, date(y, 1, 1)) for d, a, _ in rung_flows(insts[y], world))
            out.append((y, min(avail, PAYMENT)))
            carry = max(avail - PAYMENT, 0.0) * (world.grow(date(y, 1, 1), date(y + 1, 1, 1)) if y < 2042 else 0)
        return out
    bucket = {y: 0.0 for y in YEARS}
    for y2, u in units.items():
        for d, a, _ in rung_flows(insts[y2], world):
            ny = next_payment(d)
            if ny in bucket:
                bucket[ny] += u * a * world.grow(d, date(ny, 1, 1))
    carry = 0.0
    for y in YEARS:
        avail = bucket[y] + carry
        out.append((y, min(avail, PAYMENT) if avail < PAYMENT else PAYMENT))
        surplus = max(avail - PAYMENT, 0.0)
        carry = surplus * world.grow(date(y, 1, 1), date(y + 1, 1, 1)) if y < 2042 else 0.0
    return out


# ---------------------------------------------------------------- history: the 1-year Treasury yield since 1962

def monthly_series(path, col):
    acc = {}
    for r in csv.DictReader(open(path)):
        v = r[col]
        if v in ("", "."):
            continue
        k = r["observation_date"][:7]
        acc.setdefault(k, []).append(float(v))
    keys = sorted(acc)
    return keys, np.array([np.mean(acc[k]) for k in keys])


def history_windows(path, col, years=16, cap=3.0):
    """Yield (start_month, mult) where mult(d) = y(start + months since 1 Jan 2027) / y(start), capped at `cap`."""
    keys, ys = monthly_series(path, col)
    n = years * 12
    for i in range(len(ys) - n):
        y0 = ys[i]
        seg = np.minimum(ys[i:i + n + 1] / y0, cap)

        def mult(d, seg=seg):
            k = (d.year - 2027) * 12 + (d.month - 1)
            return float(seg[min(max(k, 0), n)])
        yield keys[i], mult
