"""The two calls every register script shares: the January 2028 completion standard and the 2031 range rule.
(Keel, Tue 10 Nov 2026, Sydney.) MODEL, not a forecast or a promise.

Decided Tue 10 Nov 2026 07:04 (Sydney), `keel/pm/ASK_HUMANS.md`:
  1. Completion standard: "sufficient without reinvestment" (the municipal escrow verifier's test, card Q20).
     Design H_plain: the ten rungs at their plain size (design A sized at today's forward rates, each rung's own
     coupons reinvested for its own payment, as the Trading Notes say), plus a pooled backstop of extra face in the same
     Treasuries (IBTQ, IBTR and the five T-bonds) whose coupons and principal wait in a short-term Treasury ETF for the
     next payment due. The backstop is the cheapest one (exact linear programme) that pays all ten if no coupon and no
     waiting dollar ever earns a cent. It replaces Mon 9 Nov's call (design A sized for reinvestment 3 points below
     forwards, kept here as the alternative "KEEL").
  2. Range rule (card Q19): bottom = the floor fund's payout if no more interest is earned from its purchase (January
     2028), worked out at its purchase yield; top = that plus the moved half's payout on the same basis, worked out on
     the move day (before the 2031 meetings); both rounded down to $5,000; the 2033 contribution is the lower of what
     the two funds pay and the stated top, and any excess joins the half kept (CANON D12); no figure before the move.

Every script reads the design from here (CALL), so a change of standard is one line. `--design KEEL` on a script
reproduces the Mon 9 Nov standard on the same code.

Tue 10 Nov, afternoon (bond desk check, research/panel/2026-11-10_bond_desk_register_check.md):
  * the backstop is sized so all ten are paid if every waiting dollar loses a Treasury-bill ETF's fee (WAIT_FEE, 0.15%
    a year) instead of earning nothing: every coupon, fund payout and carried surplus waits in that ETF. The design
    sized at exactly 0% is kept as H_plain_0 (Tue 10 Nov morning; $335,771);
  * each stated end is worked out from the late-2032 fund's own holdings (the engine's IBTM bond, coupon fixed on the
    6 Nov curve) priced on the trade day's curve, cut by HAIRCUT (0.5%) before rounding down; the morning's one-par-bond
    deductions (ded_floor, ded_moved) stay as a comparison ("par stand-in"); owned_test() checks the stated ends
    against holdings the rule does not assume (3.50% and 4.00% coupons, the par stand-in) and against frictions.
"""
import itertools
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402

CALL = "H_plain"
ALT = "KEEL"
STEP = 5_000.0
DECIDED = "Tue 10 Nov 2026 07:04 Sydney (keel/pm/ASK_HUMANS.md)"
RUN = "Tue 10 Nov 2026 (Sydney)"

c = E.Curve(E.load_par())
I = E.instruments(c)
Y = E.YEARS
BASE = E.Reinvest(c)
ZERO = E.Reinvest(c, "zero")
FEE = E.ASSUMPTIONS["fund_fee"]
WAIT_FEE = 0.0015    # a year on every waiting dollar: a Treasury-bill ETF's fee, as a cushion (bond desk check, finding 3)
HAIRCUT = 0.005      # cut from each end's zero-interest value before rounding down (bond desk check, finding 1)


class Flat(E.Reinvest):
    """Money earns a flat r a year from the day it arrives (r < 0: it pays a fee while it waits)."""

    def __init__(self, curve, r):
        super().__init__(curve, "flat")
        self.r = r

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        return math.exp(self.r * (d2 - d1).days / 365.25)


FEEW = Flat(c, -WAIT_FEE)


def design_arg(argv=None):
    """The design a script runs: CALL unless `--design NAME` is given."""
    argv = sys.argv[1:] if argv is None else argv
    if "--design" in argv:
        return argv[argv.index("--design") + 1]
    return CALL


def tag(name):
    """Suffix for results files: none for the call, the design's name otherwise."""
    return "" if name == CALL else f"_{name}"


# ---------------------------------------------------------------- delivery for own-rung, pooled and hybrid books

def own_amounts(units, world, insts=I):
    """Money each rung's own flows reach on its own payment date (design A), uncapped."""
    return {y: units.get(y, 0.0) * sum(a * world.grow(d, date(y, 1, 1)) for d, a, _ in E.rung_flows(insts[y], world))
            for y in Y}


def pool_buckets(units, world, insts=I):
    """Money reaching each payment date when every flow is held to the next payment due (the backstop's rule)."""
    b = {y: 0.0 for y in Y}
    for y2, u in units.items():
        if u <= 0:
            continue
        for d, a, _ in E.rung_flows(insts[y2], world):
            ny = E.next_payment(d)
            if ny in b:
                b[ny] += u * a * world.grow(d, date(ny, 1, 1))
    return b


def ledger(world, own=None, pool=None, insts=I):
    """Pay each 1 January from the own-rung book, the pooled backstop and any surplus carried forward at the rate locked
    that day. Returns (paid by year, uncapped available by year, carry after each payment, money left after 2042)."""
    oa = own_amounts(own, world, insts) if own else {y: 0.0 for y in Y}
    pb = pool_buckets(pool, world, insts) if pool else {y: 0.0 for y in Y}
    paid, avail_y, carry_y, carry, left = {}, {}, {}, 0.0, 0.0
    for y in Y:
        avail = oa[y] + pb[y] + carry
        avail_y[y] = avail
        paid[y] = min(avail, E.PAYMENT)
        surplus = max(avail - E.PAYMENT, 0.0)
        carry_y[y] = surplus
        if y < 2042:
            carry = surplus * world.grow(date(y, 1, 1), date(y + 1, 1, 1))
        else:
            left = surplus
    return paid, avail_y, carry_y, left


def short(world, own=None, pool=None, insts=I):
    return sum(E.PAYMENT - v for v in ledger(world, own, pool, insts)[0].values())


def cost(units, insts=I):
    return sum(u * insts[y].price for y, u in units.items())


def add(u1, u2):
    return {y: (u1 or {}).get(y, 0.0) + (u2 or {}).get(y, 0.0) for y in Y}


# ---------------------------------------------------------------- the exact backstop at zero interest (card Q20)

_COMBOS = np.array(list(itertools.combinations(range(20), 10)), dtype=np.int16)
NEED = E.PAYMENT * np.arange(1, 11)


def _defl(d, r):
    """At a flat rate r, $1 on date d is worth this many 1 Jan 2027 dollars (so carrying money forward at r is exact)."""
    return math.exp(-r * E.yf(d, E.J27))


def _cum(insts, r=0.0):
    """Cash from one unit of each instrument that has arrived by each 1 January, held to the next payment at a flat r
    (0: earns nothing; -WAIT_FEE: pays the ETF's fee), in deflated money so the carry between payments is exact."""
    C = np.zeros((10, 10))
    w = Flat(c, r)                     # at a flat rate the curve plays no part
    for j, y2 in enumerate(Y):
        for d, a, _ in E.rung_flows(insts[y2], w):
            ny = E.next_payment(d)
            if ny in Y:
                C[Y.index(ny), j] += a * _defl(d, r)
    return np.cumsum(C, axis=0)


def lp_min_cost(insts, lb, need_cum, r=0.0):
    """min price.x  s.t.  CUM x >= need_cum, x >= lb. Exact, by vertex enumeration (10 variables, 20 constraints)."""
    CUM = _cum(insts, r)
    PRICE = np.array([insts[y].price for y in Y])
    G = np.vstack([CUM, np.eye(10)])
    h = np.r_[need_cum, lb]
    best, bx = np.inf, None
    for s in range(0, len(_COMBOS), 20000):
        cb = _COMBOS[s:s + 20000]
        A, rhs = G[cb], h[cb]
        det = np.linalg.det(A)
        ok = np.abs(det) > 1e-9
        if not ok.any():
            continue
        x = np.linalg.solve(A[ok], rhs[ok][..., None])[..., 0]
        feas = ((x @ CUM.T) >= need_cum - 1e-6).all(axis=1) & (x >= lb - 1e-6).all(axis=1)
        if not feas.any():
            continue
        xc = x[feas]
        cs = xc @ PRICE
        k = int(np.argmin(cs))
        if cs[k] < best:
            best, bx = float(cs[k]), xc[k]
    return {y: float(max(bx[i], 0.0)) for i, y in enumerate(Y)}


def backstop_for(insts, base_units, r=-WAIT_FEE):
    """The cheapest extra units, run pooled, that cover what the own-rung book lacks if every waiting dollar earns a
    flat r (the call: -WAIT_FEE, the ETF's fee; r = 0 gives the Tue 10 Nov morning backstop)."""
    w = Flat(c, r)
    oz = own_amounts(base_units, w, insts)
    need = np.cumsum([(E.PAYMENT - oz[y]) * _defl(date(y, 1, 1), r) for y in Y])
    return lp_min_cost(insts, np.zeros(10), need, r)


def build(curve, zero_too=False):
    """The designs on one curve: plain rungs, Keel's minus-3 rungs, the backstop sized with the ETF's fee (and, if
    asked, the one sized at exactly 0%)."""
    insts = E.instruments(curve)
    plain = E.size_own_rung(insts, E.Reinvest(curve))
    keel = E.size_own_rung(insts, E.Reinvest(curve, "shift", 0.03))
    back = backstop_for(insts, plain, -WAIT_FEE)
    pc = cost(plain, insts)
    out = {
        "insts": insts, "plain": plain, "plain_cost": pc,
        "H_plain": {"own": plain, "pool": back, "cost": pc + cost(back, insts), "margin": cost(back, insts),
                    "backstop": back},
        "KEEL": {"own": keel, "pool": None, "cost": cost(keel, insts), "margin": cost(keel, insts) - pc},
    }
    if zero_too:
        b0 = backstop_for(insts, plain, 0.0)
        out["H_plain_0"] = {"own": plain, "pool": b0, "cost": pc + cost(b0, insts), "margin": cost(b0, insts),
                            "backstop": b0}
    return out


B0 = build(c, zero_too=True)
PLAIN = B0["plain"]
PLAIN_COST = B0["plain_cost"]
BACKSTOP = B0["H_plain"]["backstop"]
DESIGNS = {
    "H_plain": dict(B0["H_plain"], label="Ten rungs as written plus a pooled backstop, sufficient without reinvestment "
                                         "after a 0.15% a year fee on all waiting money (Tue 10 Nov call, afternoon)"),
    "H_plain_0": dict(B0["H_plain_0"], label="The same backstop sized at exactly 0% (Tue 10 Nov morning; comparison "
                                             "only, not runnable as --design)"),
    "KEEL": dict(B0["KEEL"], label="Design A sized for reinvestment 3 points below forwards (Mon 9 Nov call, "
                                   "replaced)"),
}


def design(name=None):
    return DESIGNS[name or CALL]


def units_all(name=None):
    d = design(name)
    return add(d["own"], d["pool"])


# ---------------------------------------------------------------- the backstop's price in January 2028

def _after_j28(units):
    """Flows after 1 Jan 2028 of the given units (date, amount), and those that arrive in 2027 (held as cash)."""
    after, before = [], 0.0
    for y, u in units.items():
        if u <= 0:
            continue
        for d, a, _ in E.rung_flows(I[y], BASE):
            if d > E.J28:
                after.append((E.yf(d, E.J28), c.fwd(E.J28, d), u * a))
            else:
                before += u * a
    return after, before


_BS_AFTER, _BS_BEFORE = _after_j28(BACKSTOP)


def backstop_price28(shift=0.0, mult=1.0):
    """What the backstop costs on 1 Jan 2028 (its flows after that date discounted at today's forwards x mult + shift,
    plus its 2027 flows held as cash at face), vectorised over shift or mult."""
    shift, mult = np.asarray(shift, float), np.asarray(mult, float)
    v = np.zeros(np.broadcast(shift, mult).shape)
    for t, f, a in _BS_AFTER:
        v = v + a * np.exp(-(f * mult + shift) * t)
    return v + _BS_BEFORE


_P0 = float(backstop_price28())


# The whole design re-sized on a curve moved by d0 before 1 Jan 2027 (the ten bought that day at that day's forward
# rates; the backstop sized at zero interest on top of them). Falling yields make the plain rungs bigger, so the backstop
# needed at zero shrinks: it costs $22,380 at -2 points and $38,104 at +1 point (1 Jan 2027 money on that curve).
D0_GRID = np.round(np.arange(-0.03, 0.0201, 0.0025), 6)
_SHIFTED = {}


def shifted(d0):
    """build() on today's curve moved by d0 (cached)."""
    key = round(float(d0), 6)
    if key not in _SHIFTED:
        _SHIFTED[key] = build(E.Curve(c.par, shift=key)) if key != 0 else B0
    return _SHIFTED[key]


def _margin_grid(name):
    return np.array([shifted(s)[name]["margin"] for s in D0_GRID])


_MG = {}


def margin_at(name, d0):
    """The design's margin (1 Jan 2027 money, on the curve moved by d0), interpolated on D0_GRID."""
    if name not in _MG:
        _MG[name] = _margin_grid(name)
    return np.interp(np.asarray(d0, float), D0_GRID, _MG[name])


def margin_fn(name=None, curve=c):
    """For plan.run: the January 2028 cost of the completion beyond the unbought tail, given d0 (move to 1 Jan 2027)
    and d1 (move over 2027).
    KEEL: the register's 9 Nov convention (margin fixed in 1 Jan 2027 money, moved with the ladder's duration on d1).
    H_plain: the backstop sized at zero interest on top of the ten bought on 1 Jan 2027 (so it depends on d0), carried a
    year at that curve's 2027 rate, then repriced exactly for the move over 2027 (d1), convexity included."""
    name = name or CALL
    d = design(name)
    f01 = curve.fwd(E.J27, E.J28)
    if name == "KEEL":
        import plan as P
        dur = P.setup(curve)["dur_l"]
        m = d["margin"]
        return lambda d0, d1: m * np.exp(-dur * np.asarray(d1, float)) * np.exp(np.maximum(f01 + np.asarray(d0, float), 0.001))

    def f(d0, d1):
        d0, d1 = np.asarray(d0, float), np.asarray(d1, float)
        return (margin_at(name, d0) * np.exp(np.maximum(f01 + d0, 0.001))
                * backstop_price28(d0 + d1) / backstop_price28(d0))
    return f


def margin_fn_mult(name, m28):
    """As margin_fn, for history windows that move every forward rate in proportion (x m28 in January 2028; the window
    starts at today's forwards, so d0 = 0)."""
    name = name or CALL
    d = design(name)
    f01 = c.fwd(E.J27, E.J28)
    if name == "KEEL":
        return None
    return lambda d0, d1: d["margin"] * math.exp(f01) * backstop_price28(0.0, np.asarray(m28, float)) / _P0


def completion_exact(d0=0.0, name=None):
    """Section 5: the January 2028 completion if yields move by d0 before 1 Jan 2027 and then follow that curve's
    forwards: (whole design's cost - $300,000) carried a year, or the ladder alone (name='plain'). Negative = money
    left from the first deposit."""
    b = shifted(d0)
    cc = E.Curve(c.par, shift=float(d0)) if d0 else c
    f01 = cc.fwd(E.J27, E.J28)
    cst = b["plain_cost"] if name == "plain" else b[name or CALL]["cost"]
    return (cst - 300_000.0) * math.exp(f01), b, cc


# ---------------------------------------------------------------- the range rule (card Q19)

WAM, END = I[2033].hold_mat, I[2033].end


def fund_flows(curve, buy, coupon=None):
    """$1 put into the late-2032 iBond fund (IBTM) on `buy` (as range_rule.py): holdings as one bond maturing at the
    fund's average maturity at the curve's par yield, fee charged on net assets, principal then waits to 15 Dec 2032."""
    cds = E.coupon_dates(WAM, start=buy)
    pb = lambda d: curve.P(d) / curve.P(buy)
    if coupon is None:
        cpn, price = (1 - pb(WAM)) / (sum(pb(d) for d in cds) / 2), 1.0
    else:
        cpn = coupon
        price = sum(cpn / 2 * pb(d) for d in cds) + pb(WAM)
    fl = [(d, cpn / 2 / price) for d in cds]
    fl[-1] = (WAM, (cpn / 2 + 1) / price)
    return cpn, [(d, a * (1 - FEE) ** ((d - buy).days / 365.25)) for d, a in fl]


def losses(curve, buy, coupon=None):
    """Share of the modelled payout (flows earning forwards to 15 Dec 2032) lost if nothing earns interest from the
    purchase on ('zero'), or if rates fall 3 points for good from the purchase ('minus3')."""
    cpn, fl = fund_flows(curve, buy, coupon)
    b, z, s3 = E.Reinvest(curve), E.Reinvest(curve, "zero"), E.Reinvest(curve, "shift", 0.03)
    v = lambda w: sum(a * w.grow(d, END) for d, a in fl)
    vb = v(b)
    return {"coupon": cpn, "zero": 1 - v(z) / vb, "minus3": 1 - v(s3) / vb}


GRID = np.round(np.arange(-0.0425, 0.0601, 0.0025), 6)
_gF, _gM = [], []
for _s in GRID:
    _cs = E.Curve(c.par, shift=float(_s))
    _gF.append(max(losses(_cs, E.J28)["zero"], 0.0))
    _gM.append(max(losses(_cs, E.J31)["zero"], 0.0))
GF, GM = np.array(_gF), np.array(_gM)


def ded_floor(sF):
    """The floor's deduction: share of its payout lost if nothing earns interest after its purchase in January 2028,
    at a purchase yield moved by sF (parallel) from today's forwards."""
    return np.interp(sF, GRID, GF)


def ded_moved(sM):
    """The moved half's deduction, bought on the move day at a yield moved by sM from today's forwards."""
    return np.interp(sM, GRID, GM)


def down(x, step=STEP):
    return np.floor(np.asarray(x, float) / step) * step


def rule_par(F, M, sF=0.0, sM=0.0, payout=None):
    """The Tue 10 Nov morning rule (one par bond at the purchase yield; no haircut): kept as a comparison only."""
    F, M, sF, sM = np.broadcast_arrays(*(np.asarray(x, float) for x in (F, M, sF, sM)))
    Fz, Mz = F * (1 - ded_floor(sF)), M * (1 - ded_moved(sM))
    pay = F + M if payout is None else np.asarray(payout, float)
    top = down(Fz + Mz)
    gift = np.minimum(pay, top)
    return dict(bottom_raw=Fz, bottom=down(Fz), top_raw=Fz + Mz, top=top, payout=pay, gift=gift, excess=pay - gift,
                zero_world=Fz + Mz)


# ---------------------------------------------------------------- the range rule on the fund's own holdings (afternoon)

_PW = (1 - FEE) ** ((END - WAM).days / 365.25)     # the fee on the holdings' principal while it waits to 15 Dec 2032


def _bond(coupon):
    """Holdings as one bond with this coupon maturing at IBTM's average maturity, fee from 1 Jan 2027 (test variants)."""
    fl = [(d, coupon / 2) for d in E.coupon_dates(WAM)]
    fl[-1] = (WAM, coupon / 2 + 1.0)
    return [(d, a * (1 - FEE) ** E.yf(d, E.J27)) for d, a in fl]


HOLD = {"engine": [(d, a) for d, a, _ in I[2033].flows],     # the engine's IBTM: coupon fixed on the 6 Nov curve
        "coupon_3.50": _bond(0.035), "coupon_4.00": _bond(0.040)}
HOLD_COUPON = 2 * I[2033].flows[0][1] / (1 - FEE) ** E.yf(I[2033].flows[0][0], E.J27)


def zero_per_dollar(buy, s=0.0, mult=1.0, hold="engine"):
    """What $1 put into the late-2032 fund on `buy` pays on 15 Dec 2032 if nothing earns interest from then on: the
    holdings' remaining coupons and principal (fee to each flow, and on the principal to 15 Dec), over their price on
    the trade day's curve (today's forwards from `buy`, x mult + s; rates floored at zero). Vectorised over s, mult."""
    fl = [(d, a) for d, a in HOLD[hold] if d > buy]
    s, mult = np.asarray(s, float), np.asarray(mult, float)
    nav = 0.0
    for d, a in fl:
        nav = nav + a * np.exp(-np.maximum(c.fwd(buy, d) * mult + s, 0.0) * E.yf(d, buy))
    z = sum(a * (_PW if d == WAM else 1.0) for d, a in fl)
    return z / nav


_fF0, _fM0 = c.fwd(E.J28, END), c.fwd(E.J31, END)


def rule(res, sF=0.0, sM=0.0, mF=1.0, mM=1.0, payout=None, hold="engine", haircut=HAIRCUT):
    """Stated ends and the 2033 contribution under the rule (card Q19, on holdings). res: plan.run output (needs
    floor_money, moved_money, floor, moved); sF, sM: parallel yield moves at the floor's purchase (Jan 2028) and at the
    move; mF, mM: proportional moves (history windows). Each end = the money put in x the fund's zero-interest payout
    per $1 on that trade day, less the haircut, rounded down to $5,000; top = bottom (unrounded) + the moved half.
    payout: what the two funds pay (default: plan.run's floor + moved, at the path's own rates)."""
    Fm, Mm = np.asarray(res["floor_money"], float), np.asarray(res["moved_money"], float)
    zf, zm = zero_per_dollar(E.J28, sF, mF, hold), zero_per_dollar(E.J31, sM, mM, hold)
    Fz, Mz = Fm * zf, Mm * zm
    b_raw, t_raw = Fz * (1 - haircut), (Fz + Mz) * (1 - haircut)
    F, M = np.asarray(res["floor"], float), np.asarray(res["moved"], float)
    pay = F + M if payout is None else np.asarray(payout, float)
    bottom, top = down(b_raw), down(t_raw)
    gift = np.minimum(pay, top)
    with np.errstate(divide="ignore", invalid="ignore"):
        dF = np.where(F > 0, 1 - b_raw / np.where(F > 0, F, 1), 0.0)
        dM = np.where(M > 0, 1 - Mz * (1 - haircut) / np.where(M > 0, M, 1), 0.0)
    return dict(zF=zf, zM=zm, floor_zero=Fz, moved_zero=Mz, zero_world=Fz + Mz, dF=dF, dM=dM,
                bottom_raw=b_raw, bottom=bottom, top_raw=t_raw, top=top, payout=pay, gift=gift, excess=pay - gift)


FRICTIONS = (0.001, 0.0025, 0.005, 0.0075, 0.01)


def owned_test(res, rr, sF=0.0, sM=0.0, mF=1.0, mM=1.0):
    """Are the stated ends owned at zero interest on holdings the rule does not assume? For each variant: the floor's
    and the floor-plus-moved-half's zero-interest payout, and whether it is below the stated bottom / top. Variants:
    the engine's holdings (what the rule uses, before its haircut), 3.50% coupon (IBTM's real average coupon), 4.00%,
    the morning's par stand-in, and frictions of 0.1% to 1% of value on the engine's holdings."""
    out = {}
    Fm, Mm = np.asarray(res["floor_money"], float), np.asarray(res["moved_money"], float)
    for h in ("engine", "coupon_3.50", "coupon_4.00"):
        Fz = Fm * zero_per_dollar(E.J28, sF, mF, h)
        Tz = Fz + Mm * zero_per_dollar(E.J31, sM, mM, h)
        out[h] = (Fz, Tz)
    eF = np.asarray(sF, float) + _fF0 * (np.asarray(mF, float) - 1)
    eM = np.asarray(sM, float) + _fM0 * (np.asarray(mM, float) - 1)
    Fp = np.asarray(res["floor"], float) * (1 - ded_floor(eF))
    out["par_stand_in"] = (Fp, Fp + np.asarray(res["moved"], float) * (1 - ded_moved(eM)))
    Fz, Tz = out["engine"]
    for x in FRICTIONS:
        out[f"engine_less_{x:.4f}"] = (Fz * (1 - x), Tz * (1 - x))
    res_ = {}
    for k, (fz, tz) in out.items():
        gb, gt = rr["bottom"] - fz, rr["top"] - tz
        res_[k] = {"bottom_not_owned": gb > 0.5, "top_not_owned": gt > 0.5, "gap_bottom": gb, "gap_top": gt}
    return res_


def owned_summary(t):
    """Shares and largest gaps from owned_test (any shape)."""
    o = {}
    for k, v in t.items():
        b, tp = np.atleast_1d(v["bottom_not_owned"]), np.atleast_1d(v["top_not_owned"])
        gb, gt = np.atleast_1d(v["gap_bottom"]), np.atleast_1d(v["gap_top"])
        o[k] = {"share_bottom_not_owned": float(b.mean()), "share_top_not_owned": float(tp.mean()),
                "count_bottom_not_owned": int(b.sum()), "count_top_not_owned": int(tp.sum()),
                "largest_gap_bottom": float(gb.max()) if b.any() else 0.0,
                "largest_gap_top": float(gt.max()) if tp.any() else 0.0}
    return o


def qs(a, ps=(5, 50, 95)):
    """Percentiles of stated (rounded) figures without interpolation between $5,000 steps (method 'lower')."""
    a = np.asarray(a, float)
    return [float(np.percentile(a, p, method="lower")) for p in ps] if a.size else None


def in_2033_money(left_2042, world):
    """Money left on 1 Jan 2042, in 1 Jan 2033 money at that world's own rates (bond desk check, finding 5)."""
    return left_2042 / world.grow(E.J33, date(2042, 1, 1))


def fmt(x):
    return f"${x:,.0f}"


if __name__ == "__main__":
    for n, d in DESIGNS.items():
        print(n, fmt(d["cost"]), "margin", fmt(d["margin"]), "short at 0%",
              fmt(short(ZERO, d["own"], d["pool"])), "|", d["label"])
    print("backstop units", {y: round(u) for y, u in BACKSTOP.items() if u > 0.5})
    print("backstop Jan 2028 price, today's forwards", fmt(_P0), "| +/-1 pt", fmt(float(backstop_price28(0.01))),
          fmt(float(backstop_price28(-0.01))), "| -3 pt", fmt(float(backstop_price28(-0.03))))
    print("deductions at today's forwards: floor", f"{float(ded_floor(0.0)):.4%}", "moved", f"{float(ded_moved(0.0)):.4%}")
