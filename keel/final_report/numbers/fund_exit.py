"""An early end of the late-2032 fund (IBTM) after the 2031 move: what the stated range and the 2033 payment lose
(numbers owner, Wed 18 Nov 2026 evening, Sydney). MODEL and Keel arithmetic, not a forecast or a promise. NUMBERS 3,
"An early end of the late-2032 fund after the move (Wed 18 Nov evening)".

Bond desk 5 (research/panel/2026-11-18_bond_desk_5_3c_table3_3e.md, M2) found in scratch that if IBTM were ended early
(or merged, or its end moved) after the 1 January 2031 move, and the cash then waited earning nothing, both lots would
pay less than the stated $115,000 top ($4,589 short for an exit on 2 Jan 2031, $2,256 on 1 Jul 2031, covered from about
January 2032), while Table 3 row 4 says such a gap is "met from the 0.5% margin" and NUMBERS 0 lists "a fund swap"
among what the 0.5% covers. The margin pays for costs; it does not pay for the lost lock on the rate: an exit turns the
holdings' remaining coupons and principal (what the range rule counts, undiscounted) into their market value on the
exit day, which is less by the interest they had left to pay.

Method (the register's central path; nothing re-sized):
  * the two lots: the floor (money put in $81,244.28, bought 1 Jan 2028) and the moved shares ($18,349.05, 1 Jan 2031),
    each on the range rule's holdings (completion.HOLD["engine"]: the engine's IBTM bond, coupon fixed on the 6 Nov
    curve), units = money / the holdings' value on the trade day (today's forwards), as completion.zero_per_dollar;
  * exit on date D (2 Jan 2031, the day after the modelled move, then the 1st of each month to 1 Dec 2032): each
    distribution before D, less the 0.07% fee from the trade day, waits in the short-term Treasury ETF; on D the fund
    pays its net asset value: the holdings' remaining flows valued on today's forwards for D (rates floored at zero)
    less the fee from the trade day to D; after the holdings mature (4 Jul 2032 in the engine) the fund holds cash and
    pays that; the payout then waits in the ETF to 15 Dec 2032;
  * waiting cash two ways: (a) earning nothing after the ETF's 0.15% a year (the standard "certain" is stated on,
    NUMBERS 0), also at face (no fee) for reference; (b) in the ETF at today's forward rates less its 0.15% fee (cash
    inside the fund earns the forward rate less the fund's fee); and (c) the flat yearly rate, before the ETF's fee, the
    waiting cash must earn for both lots to pay the stated top;
  * with no exit, (a) equals the rule's zero-interest value ($117,731 for both lots; asserted), so the shortfall against
    the stated $115,000 is the exit's loss less the room under the top ($2,731: the 0.5% held back, $589, and the
    rounding down, $2,142);
  * the 2033 payment: the same exit applied to the IBTM rung the first deposit buys (completion.PLAIN[2033]), the ten
    re-run through completion.ledger under the standard (zero interest, the ETF's 0.15%; the backstop as sized, which
    holds no IBTM), with and without the 0.5% fund cost the payments' margin is sized for; exits monthly from 1 Feb
    2027; and, for scale, the same test on the other four funds' rungs (their largest shortfall over monthly exits).

Run from the repo root:  python3 -I keel/final_report/numbers/fund_exit.py
Writes keel/final_report/numbers/results_fund_exit_2026-11-18.json (about 30 seconds, numpy only). Imports engine,
plan and completion and changes none of them; reads no results file; writes no other file.
"""
import copy
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

c = C.c
OUT = HERE / "results_fund_exit_2026-11-18.json"
FEE, WF, END, WAM = C.FEE, C.WAIT_FEE, C.END, C.WAM
HOLD = C.HOLD["engine"]
f = lambda x: float(np.asarray(x).item())


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


def bisect(fn, lo, hi, iters=60):
    flo = fn(lo)
    assert flo * fn(hi) < 0, (lo, hi, flo, fn(hi))
    for _ in range(iters):
        mid = (lo + hi) / 2
        if (fn(mid) > 0) == (flo > 0):
            lo, flo = mid, fn(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def months(start, end):
    out, y, m = [], start.year, start.month
    while date(y, m, 1) <= end:
        out.append(date(y, m, 1))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


# ---------------------------------------------------------------- the register's central figures
MARGIN, MF = C.design(C.CALL)["margin"], C.margin_fn(C.CALL)
cen = P.run(c, margin=MARGIN, margin_fn=MF)
rr = C.rule(cen)
FM, MM = f(cen["floor_money"]), f(cen["moved_money"])
BOT, TOP = f(rr["bottom"]), f(rr["top"])
FZ, MZ = f(rr["floor_zero"]), f(rr["moved_zero"])
assert (BOT, TOP) == (95_000.0, 115_000.0)
near(FM, 81_244.28, 0.01, "floor money")
near(MM, 18_349.05, 0.01, "moved money")
near(FZ + MZ, 117_731, 1, "both funds' zero-interest value")


# ---------------------------------------------------------------- one lot, exit on D
def nav(buy, D):
    """The holdings' remaining gross flows after D valued on D on today's forwards (rates floored at zero)."""
    return sum(a * math.exp(-max(c.fwd(D, d), 0.0) * E.yf(d, D)) for d, a in HOLD if d > D)


def grow(world, d1, d2, where="etf"):
    """Growth of waiting cash from d1 to d2. world: 'zero' (nothing, less the ETF's fee), 'face' (nothing, no fee),
    'fwd' (today's forwards less the fee), or a float r (a flat yearly rate before the fee). where: 'etf' (0.15%) or
    'fund' (inside IBTM, its 0.07% charged separately, so no further fee here)."""
    if d2 <= d1:
        return 1.0
    t = E.yf(d2, d1)
    fee = WF if where == "etf" else 0.0
    if world == "face":
        return 1.0
    if world == "zero":
        return math.exp(-fee * t)
    if world == "fwd":
        return math.exp((c.fwd(d1, d2) - fee) * t)
    return math.exp((world - fee) * t)


def lot(buy, money, D, world):
    """What `money` put into IBTM on `buy` pays by 15 Dec 2032 if the fund ends (or is sold) on D (D=None: no exit)."""
    units = money / nav(buy, buy)
    tot = 0.0
    for d, a in HOLD:
        if d <= buy:
            continue
        net = units * a * (1 - FEE) ** E.yf(d, buy)
        if d == WAM:
            continue                                           # the principal: below
        if D is None or d <= D:
            tot += net * grow(world, d, END)                   # a distribution: waits in the ETF to 15 Dec 2032
    a_w = [a for d, a in HOLD if d == WAM][0]
    if D is None or D >= END:                                  # no exit: the principal waits inside the fund to the end
        tot += units * a_w * (1 - FEE) ** E.yf(END, buy) * grow(world, WAM, END, "fund")
    elif D >= WAM:                                             # exit after the holdings matured: the fund pays its cash
        tot += units * a_w * (1 - FEE) ** E.yf(D, buy) * grow(world, WAM, D, "fund") * grow(world, D, END)
    else:                                                      # exit before: the fund pays its net asset value
        tot += units * nav(buy, D) * (1 - FEE) ** E.yf(D, buy) * grow(world, D, END)
    return tot


# checks: with no exit the zero world is the rule's value; the forwards world is near plan.run's modelled payout
near(lot(E.J28, FM, None, "zero"), FZ, 0.01, "floor lot, no exit = rule's zero-interest value")
near(lot(E.J31, MM, None, "zero"), MZ, 0.01, "moved lot, no exit = rule's zero-interest value")
NOEXIT_FWD = lot(E.J28, FM, None, "fwd") + lot(E.J31, MM, None, "fwd")
PAY = f(rr["payout"])
assert abs(NOEXIT_FWD - PAY) < 150, (NOEXIT_FWD, PAY)            # plan.run charges no ETF fee on distributions

# bond desk 5's scratch figures (exits before the holdings mature, where its method and this one coincide)
for D, both, what in ((date(2031, 1, 2), 110_411, "2 Jan 2031"), (date(2031, 7, 1), 112_744, "1 Jul 2031"),
                      (date(2032, 1, 1), 115_172, "1 Jan 2032")):
    near(lot(E.J28, FM, D, "zero") + lot(E.J31, MM, D, "zero"), both, 1, f"bond desk 5, {what}")
near(lot(E.J28, FM, date(2029, 1, 1), "zero"), 84_443, 1, "bond desk 5, floor lot 1 Jan 2029")

# ---------------------------------------------------------------- the range: exits after the move, monthly
DATES = [date(2031, 1, 2)] + months(date(2031, 2, 1), date(2032, 12, 1))
rows = []
for D in DATES:
    r = {"exit": D.isoformat()}
    for w in ("zero", "face", "fwd"):
        fl, mv = lot(E.J28, FM, D, w), lot(E.J31, MM, D, w)
        r[w] = {"floor_lot": fl, "moved_lot": mv, "both": fl + mv, "against_top": fl + mv - TOP,
                "floor_against_bottom": fl - BOT}
    r["loss_against_no_exit_zero"] = FZ + MZ - r["zero"]["both"]
    need = lambda x: lot(E.J28, FM, D, x) + lot(E.J31, MM, D, x) - TOP
    r["rate_needed_before_etf_fee"] = 0.0 if need(0.0) >= 0 else bisect(need, 0.0, 0.10)
    rows.append(r)
short = [r for r in rows if r["zero"]["against_top"] < 0]
first_cov = next(r["exit"] for r in rows if r["zero"]["against_top"] >= 0 and
                 all(q["zero"]["against_top"] >= 0 for q in rows[rows.index(r):]))
assert all(r["fwd"]["against_top"] > 0 for r in rows)
assert all(r["fwd"]["floor_against_bottom"] > 0 for r in rows)
short_b = [r for r in rows if r["zero"]["floor_against_bottom"] < 0]

# before the move, for reference: the floor lot alone (nothing is stated yet; it lowers what she could state)
pre = {D.isoformat(): {"floor_lot_zero": lot(E.J28, FM, D, "zero"), "floor_lot_fwd": lot(E.J28, FM, D, "fwd"),
                       "floor_zero_no_exit": FZ}
       for D in (date(2029, 1, 1), date(2030, 1, 1), date(2031, 1, 1))}

# a higher yield on the exit day (the loss grows with it): today's forwards + 1 point on D, the worst exit date
def nav_up(buy, D, up):
    return sum(a * math.exp(-max(c.fwd(D, d) + up, 0.0) * E.yf(d, D)) for d, a in HOLD if d > D)


def both_zero_up(D, up):
    tot = 0.0
    for buy, money in ((E.J28, FM), (E.J31, MM)):
        units = money / nav(buy, buy)
        tot += sum(units * a * (1 - FEE) ** E.yf(d, buy) * grow("zero", d, END) for d, a in HOLD if buy < d <= D and d != WAM)
        tot += units * nav_up(buy, D, up) * (1 - FEE) ** E.yf(D, buy) * grow("zero", D, END)
    return tot


near(both_zero_up(date(2031, 1, 2), 0.0), rows[0]["zero"]["both"], 0.01, "up=0 check")
up1 = {"exit": "2031-01-02", "both_zero_yield_1pt_higher_on_exit_day": both_zero_up(date(2031, 1, 2), 0.01)}
up1["against_top"] = up1["both_zero_yield_1pt_higher_on_exit_day"] - TOP

# ---------------------------------------------------------------- the payments: the same exit on each fund's own rung
OWN, POOL, I = C.PLAIN, C.BACKSTOP, C.I


def exit_inst(y, D):
    """Fund y's instrument if the fund ends on D: its coupons to D, then one payout on D (net asset value on today's
    forwards less the fee from 1 Jan 2027; after its holdings mature, its cash)."""
    inst = I[y]
    i = copy.copy(inst)
    wam, end = inst.cash_wait
    if D >= end:
        return i
    if D >= wam:
        i.cash_wait, i.end = (wam, D), D                      # the cash inside the fund is paid on D
        return i
    gross = [(d, a / (1 - FEE) ** E.yf(d, E.J27)) for d, a, _ in inst.flows]
    navD = sum(a * math.exp(-max(c.fwd(D, d), 0.0) * E.yf(d, D)) for d, a in gross if d > D)
    i.flows = [(d, a, k) for d, a, k in inst.flows if d <= D] + [(D, navD * (1 - FEE) ** E.yf(D, E.J27), "exit")]
    i.cash_wait = None
    return i


def payments(y, D, cut=0.0):
    ins = dict(I)
    ins[y] = exit_inst(y, D)
    if cut:
        ins = C.cost_cut(ins, cut)
    out = {}
    for w, world in (("standard", C.FEEW), ("forwards", C.BASE)):
        paid, _, _, left = C.ledger(world, OWN, POOL, ins)
        out[w] = {"short": sum(E.PAYMENT - v for v in paid.values()), "left_after_2042": left,
                  "short_by_year": {str(k): E.PAYMENT - v for k, v in paid.items() if E.PAYMENT - v > 0.005}}
    return out


# no exit: the register's figures (the standard: nothing short, $1,177 left; with the 0.5% cut, nothing left)
base = payments(2033, date(2033, 1, 1))
near(base["standard"]["short"], 0.0, 0.005, "no exit, standard")
near(base["standard"]["left_after_2042"], 1_177, 1, "no exit, $1,177 left")
base_cut = payments(2033, date(2033, 1, 1), C.PAY_MARGIN)
near(base_cut["standard"]["short"], 0.0, 0.01, "no exit, 0.5% cut")

PDATES = months(date(2027, 2, 1), date(2032, 12, 1))
pay33 = []
for D in PDATES:
    a, b = payments(2033, D), payments(2033, D, C.PAY_MARGIN)
    pay33.append({"exit": D.isoformat(), "standard_short": a["standard"]["short"],
                  "standard_short_by_year": a["standard"]["short_by_year"],
                  "standard_left_after_2042": a["standard"]["left_after_2042"],
                  "standard_with_0.5pct_cost_short": b["standard"]["short"],
                  "forwards_short": a["forwards"]["short"]})
assert all(p["forwards_short"] < 0.005 for p in pay33)
worst33 = max(pay33, key=lambda p: p["standard_short"])
last_short33 = [p["exit"] for p in pay33 if p["standard_short"] > 0.005]
last_short33_cut = [p["exit"] for p in pay33 if p["standard_with_0.5pct_cost_short"] > 0.005]

others = {}
for y in (2034, 2035, 2036, 2037):
    wam, end = I[y].cash_wait
    ds = months(date(2027, 2, 1), date(end.year, end.month, 1))
    res = [(D, payments(y, D)) for D in ds]
    w = max(res, key=lambda t: t[1]["standard"]["short"])
    sh = [D for D, p in res if p["standard"]["short"] > 0.005]
    others[E.FUNDS[y]] = {"worst_exit": w[0].isoformat(), "worst_short_standard": w[1]["standard"]["short"],
                          "short_by_year_at_worst": w[1]["standard"]["short_by_year"],
                          "exits_short": len(sh), "exits_tested": len(ds),
                          "last_exit_short": sh[-1].isoformat() if sh else None,
                          "short_at_forwards_any": any(p["forwards"]["short"] > 0.005 for _, p in res),
                          "holdings_mature": wam.isoformat(), "fund_ends": end.isoformat()}

out = {"run": "Wed 18 Nov 2026 evening (Sydney), numbers owner", "rule": C.RULE_VERSION, "design": C.CALL,
       "curve": E.CURVE_DAY, "register_results": C.RESULTS,
       "note": "MODEL, Keel arithmetic. Central path (today's forwards; VT at 7.5%). An exit is an early end, a merger "
               "or a moved end of IBTM; its proceeds wait in the short-term Treasury ETF (Table 3 row 4's action).",
       "stated": {"bottom": BOT, "top": TOP, "floor_zero": FZ, "moved_zero": MZ, "both_zero": FZ + MZ,
                  "room_under_top": FZ + MZ - TOP, "haircut_part": (FZ + MZ) * C.HAIRCUT,
                  "rounding_part": (FZ + MZ) * (1 - C.HAIRCUT) - TOP, "room_under_bottom_floor_alone": FZ - BOT},
       "no_exit_forwards_this_method": NOEXIT_FWD, "no_exit_modelled_payout_plan_run": PAY,
       "range_exits_after_the_move": rows,
       "range_summary": {"exits_short_of_top_zero": len(short), "first_exit_short": short[0]["exit"] if short else None,
                         "last_exit_short": short[-1]["exit"] if short else None,
                         "covered_from": first_cov,
                         "largest_short_zero": -min(r["zero"]["against_top"] for r in rows),
                         "largest_short_face": -min(r["face"]["against_top"] for r in rows),
                         "smallest_room_forwards": min(r["fwd"]["against_top"] for r in rows),
                         "exits_floor_lot_short_of_bottom_zero": len(short_b),
                         "last_exit_floor_short_of_bottom": short_b[-1]["exit"] if short_b else None,
                         "largest_floor_short_of_bottom_zero": -min(r["zero"]["floor_against_bottom"] for r in rows)},
       "before_the_move_floor_lot": pre, "yield_1pt_higher_on_exit_day": up1,
       "payments_ibtm_exit": {"no_exit": base, "no_exit_with_0.5pct_cost": base_cut, "monthly": pay33,
                              "worst": worst33, "exits_short_standard": len(last_short33),
                              "last_exit_short_standard": last_short33[-1] if last_short33 else None,
                              "exits_short_with_0.5pct_cost": len(last_short33_cut),
                              "last_exit_short_with_0.5pct_cost": last_short33_cut[-1] if last_short33_cut else None},
       "payments_other_funds_exit": others}
OUT.write_text(json.dumps(out, indent=1, default=float))

k = lambda x: f"${x:,.0f}"
print("room under the top", k(FZ + MZ - TOP), "no-exit forwards", k(NOEXIT_FWD), "plan.run", k(PAY))
for r in rows:
    print(r["exit"], "zero both", k(r["zero"]["both"]), "vs top", k(r["zero"]["against_top"]), "| face",
          k(r["face"]["against_top"]), "| fwd", k(r["fwd"]["against_top"]), "| floor vs bottom zero",
          k(r["zero"]["floor_against_bottom"]), "| rate needed %.2f%%" % (100 * r["rate_needed_before_etf_fee"]),
          "| loss", k(r["loss_against_no_exit_zero"]))
print("covered from", first_cov, "; short exits", len(short))
print("pre-move floor lot:", {a: k(b["floor_lot_zero"]) for a, b in pre.items()})
print("1 pt higher on 2 Jan 2031:", k(up1["both_zero_yield_1pt_higher_on_exit_day"]), k(up1["against_top"]))
print("payments, IBTM exit: worst", worst33["exit"], k(worst33["standard_short"]), worst33["standard_short_by_year"],
      "; exits short", len(last_short33), "last", last_short33[-1] if last_short33 else None,
      "; with 0.5% cost: exits short", len(last_short33_cut), "last", last_short33_cut[-1] if last_short33_cut else None)
for p in pay33:
    if p["exit"][5:7] in ("01", "07"):
        print("   ", p["exit"], "standard short", k(p["standard_short"]), "with 0.5% cost", k(p["standard_with_0.5pct_cost_short"]),
              "left", k(p["standard_left_after_2042"]))
for n, v in others.items():
    print("payments,", n, "worst", v["worst_exit"], k(v["worst_short_standard"]), "exits short", v["exits_short"], "of",
          v["exits_tested"], "last", v["last_exit_short"], "at forwards short any:", v["short_at_forwards_any"])
print("wrote", OUT)
