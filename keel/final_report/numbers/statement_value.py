"""What a broker statement shows co-sponsors in 2031 and 2032 (numbers owner's analysis worker, Tue 24 Nov 2026,
Sydney). MODEL and Keel arithmetic, not a forecast or a promise. Proposed NUMBERS 8y.

Three readers playing funders (24 Nov) said co-sponsors will be shown a broker statement at the 2031 meetings and again
before the December 2032 payout; that a bond fund two years from its end shows a market value BELOW what it will pay
out, so the statement could show less than the $115,000 Laura signs for, with no one explaining why; and that a single
IBTM line mixes the 2033 payment's lot with the building's lots. This script sizes that on the register's own engine.

On the central path (6 Nov 2026 curve's forwards, VT at 7.5% a year, the escrow standard, Keel's reading of "most",
the move modelled on 1 Jan 2031, trade Thu 2 Jan 2031), for 2 Jan 2031, 1 Jul 2031, 3 Jan 2032, 1 Jul 2032 and
1 Dec 2032:
  (a) the market value (net asset value on that date's forwards) of the building's two IBTM lots together (floor lot,
      January 2028; moved lot, January 2031), and of the 2033 payment's own lot separately; and, beside them, the
      distributions each has already paid, which wait in the short-term Treasury ETF (a separate statement line, shared
      with every other waiting dollar);
  (b) what the building's two lots pay at the fund's end (15 Dec 2032) at today's forwards, and the zero-interest
      count the top was set on ($117,731; less 0.5%, $117,142; stated $115,000); and the same count re-done on each
      statement date (what the holdings still to pay and the distributions already paid hand over by 15 Dec 2032 if
      nothing earns interest from that date, after the fund's fee and the waiting ETF's fee);
  (c) the face value of the Treasuries behind the building's lots (the engine's stand-in bond: face 1.0 per unit) and
      their coupons still to come, gross and after the fund's fee; with IBTM's real 3.50% average coupon as a variant;
  (d) the first date on which the building's money on the statement reaches $115,000: the two IBTM lots alone, and the
      two lots plus their distributions already paid; and the single IBTM line (all three lots) for comparison.
Then the register's 1-in-20 high-yield and 1-in-20 low-yield worlds in January 2028 (NUMBERS 4, Exhibit 3; today's
forwards moved in parallel by the scenario's yield move from January 2027 on), (a) and (d) against each world's own
stated top and against $115,000; and a 1-point rise in yields during 2031: on each statement date (at once), and held
for good from just after the move (2 Jan 2031) or from 1 Jul 2031.

Valuation (the register's own conventions; one_fund.py's, which reproduces 8t and 8w):
  * a facility lot: units = money put in / the gross holdings' value on the trade day (completion.zero_per_dollar's
    price); on date t, held in IBTM at net asset value = units x the gross holdings' remaining flows discounted at that
    date's forwards x the fee charged since the trade day; after the holdings mature (4 Jul 2032 in the engine) the
    fund holds cash, grown at forwards; each distribution already paid waits in the short-term Treasury ETF, grown at
    forwards (the ETF's 0.15% belongs to the design test, NUMBERS 0, as 8t and 8w);
  * the ten payments' holdings and the backstop: one_fund.inst_parts (custody.py's nav=True), copied, since importing
    one_fund.py or fund_exit.py would rewrite their results files;
  * the market price on the exchange is not modelled: IBTM traded 0.06% to 0.09% above net asset value on normal days
    (NUMBERS 0), more in a stress.

Run from the repo root:  python3 -I keel/final_report/numbers/statement_value.py
Writes keel/final_report/numbers/results_statement_value_2026-11-24.json only (a few seconds, numpy only). Imports
engine, plan and completion and changes none of them; reads no results file.
"""
import json
import math
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

RUN = "Tue 24 Nov 2026 (Sydney), numbers owner's analysis worker"
OUT = HERE / "results_statement_value_2026-11-24.json"

NAME = C.CALL
DSG = C.design(NAME)
OWN, POOL = DSG["own"], DSG["pool"] or {}
c, I, BASE = C.c, C.I, C.BASE
FEE, WF, END, WAM, HOLD = E.ASSUMPTIONS["fund_fee"], C.WAIT_FEE, C.END, C.WAM, C.HOLD["engine"]
J27, J28, J31, J33 = E.J27, E.J28, E.J31, E.J33
TOP_LINE = 115_000.0
f = float


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


# ---------------------------------------------------------------- the register's figures (asserted; stop if any fails)
cen = P.run(c, margin=DSG["margin"], margin_fn=C.margin_fn(NAME))
rr = C.rule(cen)
FM, MM = f(cen["floor_money"]), f(cen["moved_money"])
FZ, MZ = f(rr["floor_zero"]), f(rr["moved_zero"])
PAYOUT = f(rr["payout"])
near(FM, 81_244.28, 0.01, "floor money (NUMBERS 4)")
near(MM, 18_349.05, 0.01, "moved money (NUMBERS 3)")
near(f(cen["floor"]), 102_365, 1, "the floor's payout, late 2032 (NUMBERS 4)")
near(f(cen["moved"]), 20_138, 1, "the moved half's payout (NUMBERS 4)")
near(PAYOUT, 122_503, 1, "what the late-2032 fund pays on its two purchases (NUMBERS 4)")
near(f(rr["bottom_raw"]), 97_605, 1, "unrounded bottom (NUMBERS 4)")
near(f(rr["top_raw"]), 117_142, 1, "unrounded top (NUMBERS 4)")
near(FZ, 98_096, 1, "floor lot's zero-interest value (NUMBERS 3)")
near(FZ + MZ, 117_731, 1, "both lots' zero-interest value (NUMBERS 3)")
assert (f(rr["bottom"]), f(rr["top"]), f(rr["gift"])) == (95_000.0, 115_000.0, 115_000.0)
assert POOL.get(2033, 0.0) == 0.0          # the extra Treasuries hold no IBTM (8h, 8w)
assert WAM == date(2032, 7, 4) and END == date(2032, 12, 15)
A_W = [a for d, a in HOLD if d == WAM][0]
CPN_HALF = HOLD[0][1]                       # the stand-in bond's gross half-year coupon per unit
near(A_W - CPN_HALF, 1.0, 1e-12, "the stand-in bond's principal is 1.0 per unit: units are face")
near(2 * CPN_HALF, C.HOLD_COUPON, 1e-12, "coupon")


# ---------------------------------------------------------------- worlds
class World:
    """Today's forwards on the 6 Nov 2026 curve, moved in parallel by `s` (an Exhibit 3 yield world; 0 centrally), and
    by a further `jump` for every stretch of time after `jump_day` (a rise held for good). Rates floored at zero, as
    the engine does."""

    def __init__(self, s=0.0, jump=0.0, jump_day=None, label="central"):
        self.s, self.jump, self.jd, self.label = s, jump, jump_day, label

    def _extra(self, t1, t2):
        if not self.jump or self.jd is None or t2 <= self.jd:
            return 0.0
        return self.jump * E.yf(t2, max(t1, self.jd))

    def disc(self, t, d):
        """Value on t of $1 paid on d (d > t)."""
        return math.exp(-max(c.fwd(t, d) + self.s, 0.0) * E.yf(d, t) - self._extra(t, d))

    def grow(self, d1, d2):
        """What $1 waiting from d1 grows to by d2."""
        if d2 <= d1:
            return 1.0
        return math.exp(max(c.fwd(d1, d2) + self.s, 0.0) * E.yf(d2, d1) + self._extra(d1, d2))


CEN = World()


def nav_gross(w, t, hold=HOLD):
    """The gross holdings' remaining flows after t, per unit, valued on t."""
    return sum(a * w.disc(t, d) for d, a in hold if d > t)


class Lot:
    """A facility lot of IBTM: `money` put in on `buy` (units x that day's net asset value)."""

    def __init__(self, buy, money, w, hold=HOLD):
        self.buy, self.money, self.hold = buy, money, hold
        self.units = money / nav_gross(w, buy, hold)

    def parts(self, w, t):
        """(held in IBTM at net asset value, distributions already paid waiting in the short-term Treasury ETF)."""
        if t < self.buy:
            return 0.0, 0.0
        wam = max(d for d, _ in self.hold)
        waiting = sum(self.units * a * (1 - FEE) ** E.yf(d, self.buy) * w.grow(d, t)
                      for d, a in self.hold if self.buy < d <= t and d != wam)
        if t < wam:
            held = self.units * nav_gross(w, t, self.hold) * (1 - FEE) ** E.yf(t, self.buy)
        else:                                            # the holdings have matured: cash inside the fund
            a_w = [a for d, a in self.hold if d == wam][0]
            held = self.units * a_w * (1 - FEE) ** E.yf(t, self.buy) * w.grow(wam, t)
        return held, waiting

    def zero_count(self, w, t):
        """What the lot hands over by 15 Dec 2032 if nothing earns interest from t: the distributions already paid at
        their balance on t, less the waiting ETF's 0.15% a year to 15 Dec 2032; each flow still to come less the fund's
        fee from the trade day and, for a distribution, the ETF's fee from its arrival; the principal less the fee to
        15 Dec 2032 (completion.zero_per_dollar's count, re-done on date t). On the trade day it is the rule's value."""
        held, waiting = self.parts(w, t)
        wam = max(d for d, _ in self.hold)
        z = waiting * math.exp(-WF * E.yf(END, t))
        if t < wam:
            for d, a in self.hold:
                if d <= t:
                    continue
                net = self.units * a * (1 - FEE) ** E.yf(d, self.buy)
                z += net * ((1 - FEE) ** E.yf(END, wam) if d == wam else math.exp(-WF * E.yf(END, d)))
        else:
            z += held * (1 - FEE) ** E.yf(END, t)
        return z

    def face(self):
        return self.units * 1.0

    def coupons_after(self, t, net=False):
        """The holdings' coupons still to come after t (the final coupon included), gross or after the fund's fee."""
        wam = max(d for d, _ in self.hold)
        a_w = [a for d, a in self.hold if d == wam][0]
        out = 0.0
        for d, a in self.hold:
            if d <= t:
                continue
            cp = a - 1.0 if d == wam else a
            out += self.units * cp * ((1 - FEE) ** E.yf(d, self.buy) if net else 1.0)
        assert a_w > 1.0
        return out


def lots(w, fm, mm, hold=HOLD):
    return Lot(J28, fm, w, hold), Lot(J31, mm, w, hold)


FL, MV = lots(CEN, FM, MM)
# on its trade day each lot's count is the rule's zero-interest value (completion.zero_per_dollar), and its
# net asset value is the money put in
near(FL.zero_count(CEN, J28), FZ, 0.01, "floor lot's count on its trade day = the rule's $98,096")
near(MV.zero_count(CEN, J31), MZ, 0.01, "moved lot's count on the move day = the rule's value")
near(sum(FL.parts(CEN, J28)), FM, 0.01, "floor lot at net asset value on its trade day")
near(sum(MV.parts(CEN, J31)), MM, 0.01, "moved lot at net asset value on the move day")


# ---------------------------------------------------------------- the ten payments' holdings (one_fund.inst_parts)
def inst_parts(y, t, w=CEN):
    """One of the ten holdings (own rung + any extra Treasuries in it) on t: (held, waiting in the bill ETF).
    An iBond fund at net asset value (custody.py nav=True), as one_fund.py; central world only."""
    u = OWN.get(y, 0.0) + POOL.get(y, 0.0)
    held = waiting = 0.0
    for d, a, _ in E.rung_flows(I[y], BASE):
        if d <= t:
            waiting += u * a * BASE.grow(d, t)
        else:
            g = (1 - FEE) ** -max(E.yf(min(d, I[y].hold_mat), t), 0.0) if y in E.FUNDS else 1.0
            held += u * a * g * c.P(d) / c.P(t)
    return held, waiting


def snapshot(t, w=CEN, fl=FL, mv=MV, own=True):
    fh, fw = fl.parts(w, t)
    mh, mw = mv.parts(w, t)
    row = {"date": t.isoformat(), "weekday": t.strftime("%a"),
           "building_ibtm_lots_market_value": fh + mh, "floor_lot": fh, "moved_lot": mh,
           "building_distributions_paid_waiting_in_bill_etf": fw + mw, "floor_lot_paid": fw, "moved_lot_paid": mw,
           "building_money_on_statement": fh + mh + fw + mw,
           "building_zero_count_from_this_date": fl.zero_count(w, t) + mv.zero_count(w, t)}
    if own:
        oh, ow = inst_parts(2033, t)
        bill = ow + fw + mw + sum(inst_parts(y, t)[1] for y in E.YEARS if y != 2033)
        row.update({"payment_2033_lot_market_value": oh, "payment_2033_lot_paid_waiting": ow,
                    "single_ibtm_line_three_lots": oh + fh + mh,
                    "bill_etf_line_all_waiting_money": bill,
                    "building_share_of_bill_etf_line": (fw + mw) / bill if bill else 0.0})
    row["building_ibtm_lots_vs_115000"] = row["building_ibtm_lots_market_value"] - TOP_LINE
    row["building_money_vs_115000"] = row["building_money_on_statement"] - TOP_LINE
    return row


# 8w reproduced to the dollar (1 Jan 2031, 1 Jan 2032, 30 Nov 2032)
for t, own_v, fl_v, mv_v in ((J31, 38_273, 82_051, 18_349), (date(2032, 1, 1), 38_434, 82_395, 18_426),
                             (date(2032, 11, 30), 39_352, 84_340, 18_861)):
    s = snapshot(t)
    near(s["payment_2033_lot_market_value"], own_v, 1, f"8w own lot {t}")
    near(s["floor_lot"], fl_v, 1, f"8w floor lot {t}")
    near(s["moved_lot"], mv_v, 1, f"8w moved lot {t}")
near(snapshot(J31)["bill_etf_line_all_waiting_money"], 78_247, 1, "8w bill ETF 1 Jan 2031")
near(snapshot(date(2032, 1, 1))["bill_etf_line_all_waiting_money"], 101_995, 1, "8w bill ETF 1 Jan 2032")
near(snapshot(date(2032, 11, 30))["bill_etf_line_all_waiting_money"], 122_781, 1, "8w bill ETF 30 Nov 2032")
near(snapshot(J31)["floor_lot_paid"], 11_236, 1, "8w floor lot's paid distributions 1 Jan 2031")

DATES = [date(2031, 1, 2), date(2031, 7, 1), date(2032, 1, 3), date(2032, 7, 1), date(2032, 12, 1)]
table = [snapshot(t) for t in DATES]
end_row = snapshot(END)
END_PAY = end_row["building_money_on_statement"]
# at the fund's end the two lots hand over what plan.run pays, plus the fund fee plan.run's lumping charges on
# distributions after they leave the fund (8w's fee wedge): within $60, never below
assert 0.0 <= END_PAY - PAYOUT < 60.0, (END_PAY, PAYOUT)

# (c) face and coupons still to come, the stand-in bond and IBTM's real 3.50% average coupon
face = {"engine_bond": {"coupon": C.HOLD_COUPON, "matures": WAM.isoformat(),
                        "floor_lot_face": FL.face(), "moved_lot_face": MV.face(),
                        "building_face": FL.face() + MV.face(),
                        "coupons_still_to_come_gross": {t.isoformat(): FL.coupons_after(t) + MV.coupons_after(t)
                                                        for t in DATES},
                        "coupons_still_to_come_after_fee": {t.isoformat(): FL.coupons_after(t, True)
                                                            + MV.coupons_after(t, True) for t in DATES},
                        "floor_lot_coupons_from_trade_day_gross": FL.coupons_after(J28),
                        "moved_lot_coupons_from_trade_day_gross": MV.coupons_after(J31)}}
FL35, MV35 = lots(CEN, FM, MM, C.HOLD["coupon_3.50"])
face["coupon_3.50"] = {"coupon": 0.035, "floor_lot_face": FL35.face(), "moved_lot_face": MV35.face(),
                       "building_face": FL35.face() + MV35.face(),
                       "zero_count_both_lots": FL35.zero_count(CEN, J28) + MV35.zero_count(CEN, J31),
                       "coupons_still_to_come_gross": {t.isoformat(): FL35.coupons_after(t) + MV35.coupons_after(t)
                                                       for t in DATES},
                       "market_value": {t.isoformat(): sum(FL35.parts(CEN, t)[:1]) + sum(MV35.parts(CEN, t)[:1])
                                        for t in DATES}}
# the 3.50% count matches NUMBERS 4's Keel arithmetic ($117,449 for the top after 0.5%)
near((FL35.zero_count(CEN, J28) + MV35.zero_count(CEN, J31)) * (1 - C.HAIRCUT), 117_449, 2, "3.50% top (NUMBERS 4)")


# (d) the first date on or after the move on which each measure reaches $115,000 (and stays there), daily
def days(a, b):
    out, d = [], a
    while d <= b:
        out.append(d)
        d += timedelta(days=1)
    return out


SCAN = days(date(2031, 1, 2), END)


def first_reach(series, level):
    """First date the series is >= level and stays >= level to the end; None if never."""
    first = None
    for d, v in series:
        if v >= level - 1e-9:
            first = first or d
        else:
            first = None
    return first.isoformat() if first else None


def peak(series):
    d, v = max(series, key=lambda x: x[1])
    return {"date": d.isoformat(), "value": v}


def scan(w, fl, mv, levels, own=False):
    lots_only, money, zc = [], [], []
    for t in SCAN:
        fh, fw = fl.parts(w, t)
        mh, mw = mv.parts(w, t)
        lots_only.append((t, fh + mh))
        money.append((t, fh + mh + fw + mw))
        zc.append((t, fl.zero_count(w, t) + mv.zero_count(w, t)))
    out = {}
    for lab, lv in levels.items():
        out[lab] = {"building_ibtm_lots": first_reach(lots_only, lv), "building_money_on_statement":
                    first_reach(money, lv), "zero_count": first_reach(zc, lv)}
    out["peak_building_ibtm_lots"] = peak(lots_only)
    out["min_zero_count_after_move"] = min(v for _, v in zc)
    out["building_money_on_15dec2032"] = money[-1][1]
    if own:                                  # before 15 Dec 2032, when all three lots pay out
        line = [(t, fl.parts(w, t)[0] + mv.parts(w, t)[0] + inst_parts(2033, t)[0]) for t in SCAN if t < END]
        out["single_ibtm_line_min_before_end"] = min(v for _, v in line)
        out["single_ibtm_line_first_at_or_above_115000"] = first_reach(line, TOP_LINE)
    return out


first_central = scan(CEN, FL, MV, {"115000": TOP_LINE}, own=True)
assert first_central["min_zero_count_after_move"] >= FZ + MZ - 0.01        # the count never falls below $117,731


# ---------------------------------------------------------------- the 1-in-20 yield worlds in January 2028 (Exhibit 3)
def yield_world(z_y):
    """range_rule.scen's yield move: S = z x 0.9 points x sqrt(years to 1 Jan 2027 + 1), split before and during
    2027; shares central; the move after January 2028 is nil (d2 = 0)."""
    t0 = E.yf(E.J27)
    S = z_y * E.ASSUMPTIONS["yield_vol"] * math.sqrt(t0 + 1)
    a0, a1 = S * t0 / (t0 + 1), S / (t0 + 1)
    res = P.run(c, DSG["margin"], None, 150_000.0, a0, a1, 0.0, None, None, C.margin_fn(NAME))
    r = C.rule(res, a0 + a1, a0 + a1)
    return S, res, r


worlds = {}
for lab, z, exp in (("yields_1in20_low_jan2028", -1.645, (80_000, 100_000, 103_940, 75_001)),
                    ("yields_1in20_high_jan2028", 1.645, (110_000, 130_000, 142_858, 88_241))):
    S, res, r = yield_world(z)
    fm, mm = f(res["floor_money"]), f(res["moved_money"])
    assert (f(r["bottom"]), f(r["top"])) == exp[:2], (lab, f(r["bottom"]), f(r["top"]))
    near(f(r["payout"]), exp[2], 1, f"{lab}: what the funds pay (NUMBERS 4, Exhibit 3)")
    near(fm, exp[3], 1, f"{lab}: floor money")
    w = World(s=S, label=lab)
    fl, mv = lots(w, fm, mm)
    near(fl.zero_count(w, J28) + mv.zero_count(w, J31), f(r["zero_world"]), 0.01, f"{lab}: count = rule")
    end_money = sum(fl.parts(w, END)) + sum(mv.parts(w, END))
    assert 0.0 <= end_money - f(r["payout"]) < 80.0, (lab, end_money, f(r["payout"]))
    rows = [snapshot(t, w, fl, mv, own=False) for t in DATES]
    worlds[lab] = {"yield_move_points": S * 100, "floor_money": fm, "moved_money": mm,
                   "stated_bottom": f(r["bottom"]), "stated_top": f(r["top"]), "unrounded_top": f(r["top_raw"]),
                   "zero_count_both_lots": f(r["zero_world"]), "funds_pay_plan_run": f(r["payout"]),
                   "building_money_15dec2032_this_method": end_money, "dates": rows,
                   "first_reach": scan(w, fl, mv, {"own_stated_top": f(r["top"]), "115000": TOP_LINE})}


# ---------------------------------------------------------------- a 1-point rise in yields during 2031
def at_once(t, jump):
    """Held lots on t if yields were `jump` higher from t on (the short-term Treasury ETF taken as not moving)."""
    w = World(jump=jump, jump_day=t)
    b0 = FL.parts(CEN, t)[0] + MV.parts(CEN, t)[0]
    b1 = FL.parts(w, t)[0] + MV.parts(w, t)[0]
    # the 2033 payment's own lot at the same jump (its after-fee flows grossed up, as inst_parts)
    u = OWN[2033]
    o0 = inst_parts(2033, t)[0]
    o1 = 0.0
    for d, a, _ in E.rung_flows(I[2033], BASE):
        if d > t:
            g = (1 - FEE) ** -max(E.yf(min(d, I[2033].hold_mat), t), 0.0)
            o1 += u * a * g * c.P(d) / c.P(t) * math.exp(-jump * E.yf(d, t))
    return {"date": t.isoformat(), "building_lots_change": b1 - b0, "building_lots_change_pct": (b1 - b0) / b0,
            "payment_2033_lot_change": o1 - o0}


shock_now = {f"{j:+.0%}": [at_once(t, j) for t in DATES] for j in (0.01, -0.01)}


def held_for_good(jday):
    w = World(jump=0.01, jump_day=jday, label=f"+1 point from {jday}")
    rows = [snapshot(t, w, FL, MV, own=False) for t in DATES if t >= jday]
    return {"from": jday.isoformat(), "dates": rows,
            "first_reach": scan(w, FL, MV, {"115000": TOP_LINE}),
            "building_money_15dec2032": sum(FL.parts(w, END)) + sum(MV.parts(w, END))}


shock_kept = {"from_2jan2031": held_for_good(date(2031, 1, 2)), "from_1jul2031": held_for_good(date(2031, 7, 1))}

# ---------------------------------------------------------------- Keel arithmetic for the note
k = C.fmt
t0 = table[0]
for r in table:
    r["single_ibtm_line_less_building_money"] = r["single_ibtm_line_three_lots"] - r["building_money_on_statement"]
    r["building_zero_count_less_market_value"] = (r["building_zero_count_from_this_date"]
                                                  - r["building_money_on_statement"])
monthly = []
for t in [date(y, m, 1) for y in (2031, 2032) for m in range(1, 13)]:
    t = max(t, date(2031, 1, 2))
    fh, fw = FL.parts(CEN, t)
    mh, mw = MV.parts(CEN, t)
    monthly.append({"date": t.isoformat(), "building_ibtm_lots": fh + mh, "building_money": fh + mh + fw + mw,
                    "zero_count": FL.zero_count(CEN, t) + MV.zero_count(CEN, t)})
notes = {
    "gap_lots_to_115000_on_2jan2031": TOP_LINE - t0["building_ibtm_lots_market_value"],
    "gap_money_to_115000_on_2jan2031": TOP_LINE - t0["building_money_on_statement"],
    "gap_lots_to_115000_on_1dec2032": TOP_LINE - table[-1]["building_ibtm_lots_market_value"],
    "paid_out_by_1dec2032_share_of_building_money": table[-1]["building_distributions_paid_waiting_in_bill_etf"]
    / table[-1]["building_money_on_statement"],
    "end_pay_less_plan_run": END_PAY - PAYOUT,
}

out = {"run": RUN, "status": "MODEL; Keel arithmetic where marked", "proposed_numbers_section": "8y",
       "curve": E.CURVE_DAY, "design": NAME, "rule": C.RULE_VERSION,
       "world": "today's forwards on the 6 Nov 2026 curve; VT on plan.run's central 7.5% path; iBond funds at net "
                "asset value; waiting money in the short-term Treasury ETF at forwards (its 0.15% belongs to the "
                "design test, as 8t and 8w); the engine's IBTM stand-in bond (coupon 4.2513%, matures 4 Jul 2032, "
                "semiannual coupons; the real fund pays monthly)",
       "register_asserted": {"floor_money": FM, "moved_money": MM, "floor_payout": f(cen["floor"]),
                             "moved_payout": f(cen["moved"]), "funds_pay": PAYOUT, "floor_zero": FZ,
                             "both_zero": FZ + MZ, "unrounded_bottom": f(rr["bottom_raw"]),
                             "unrounded_top": f(rr["top_raw"]), "stated_bottom": 95_000.0, "stated_top": 115_000.0},
       "statement_dates": table, "at_fund_end_15dec2032": end_row, "monthly_central": monthly,
       "first_reach_central": first_central, "face_and_coupons": face, "yield_worlds_jan2028": worlds,
       "yield_rise_1pt_at_once": shock_now, "yield_rise_1pt_held_for_good": shock_kept, "keel_arithmetic": notes}
OUT.write_text(json.dumps(out, indent=1, default=float))

print("register asserted: floor money", k(FM), "moved", k(MM), "pays", k(PAYOUT), "zero", k(FZ + MZ),
      "unrounded top", k(f(rr["top_raw"])), "floor payout", k(f(cen["floor"])))
for r in table + [end_row]:
    print(f"{r['date']} {r['weekday']}: building lots {k(r['building_ibtm_lots_market_value'])} (floor "
          f"{k(r['floor_lot'])}, moved {k(r['moved_lot'])}) + paid out {k(r['building_distributions_paid_waiting_in_bill_etf'])}"
          f" = {k(r['building_money_on_statement'])} | count {k(r['building_zero_count_from_this_date'])} | own lot "
          f"{k(r['payment_2033_lot_market_value'])} (+{k(r['payment_2033_lot_paid_waiting'])} paid) | IBTM line "
          f"{k(r['single_ibtm_line_three_lots'])} | bill ETF {k(r['bill_etf_line_all_waiting_money'])} "
          f"({r['building_share_of_bill_etf_line']:.1%} the building's)")
print("face:", {a: (k(b["building_face"]), k(b["floor_lot_face"]), k(b["moved_lot_face"])) for a, b in face.items()})
print("coupons still to come, gross:", {a: k(b) for a, b in face["engine_bond"]["coupons_still_to_come_gross"].items()})
print("first reach, central:", first_central)
for lab, wv in worlds.items():
    print(lab, f"S {wv['yield_move_points']:+.3f} pt", "range", k(wv["stated_bottom"]), "-", k(wv["stated_top"]),
          "pays", k(wv["funds_pay_plan_run"]), "| first", wv["first_reach"])
    for r in wv["dates"]:
        print("   ", r["date"], "lots", k(r["building_ibtm_lots_market_value"]), "money",
              k(r["building_money_on_statement"]), "count", k(r["building_zero_count_from_this_date"]))
for j, rows in shock_now.items():
    print("at once", j, [(r["date"], k(r["building_lots_change"]), f"{r['building_lots_change_pct']:.2%}",
                          k(r["payment_2033_lot_change"])) for r in rows])
for lab, v in shock_kept.items():
    print("held for good", lab, "end", k(v["building_money_15dec2032"]), v["first_reach"],
          [(r["date"], k(r["building_ibtm_lots_market_value"]), k(r["building_money_on_statement"]),
            k(r["building_zero_count_from_this_date"])) for r in v["dates"]])
print("notes:", {a: (round(b, 4) if abs(b) < 2 else k(b)) for a, b in notes.items()})
print("wrote", OUT)
