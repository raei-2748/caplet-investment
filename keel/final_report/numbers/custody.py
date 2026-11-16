"""Custody: the largest balance at one broker, January 2028 to 1 January 2033 (numbers owner, Mon 16 Nov 2026, Sydney).
MODEL, not a forecast or a promise. NUMBERS 8t.

Run from the repo root:  python3 -I keel/final_report/numbers/custody.py
   or from this folder:  python3 -I custody.py
Writes keel/final_report/numbers/results_custody_2026-11-16.json and prints the figures (about 10 seconds, numpy only).
Imports engine.py, plan.py and completion.py and changes none of them; reads no results file.

The question. Table 3's custody line and aha row 5b set "$589,655 at the end" (NUMBERS 8k) against SIPC's $500,000
cover. 8k's $589,655 is all of Laura's money valued on 1 Jan 2033 (the reserve, the contribution carried 17 days from
December 2032, the excess and the half kept), a total for the 87.2% / 12.8% split, not a dated broker balance. This
script values, on every month-end from 31 Jan 2028 to 31 Dec 2032 and on 1 Jan 2033 before the first payment, what the
plan holds at one broker (every holding at one broker: CLAUDE.md, card Q78), at nominal market value, split by holding.

The plan as registered (sections 2 to 4, 8h): today's forward rates on the 6 Nov 2026 curve, VT at its median 7.5% a
year; the escrow standard (completion.CALL, H_plain: the ten own rungs plus the backstop); Keel's reading of "most";
the move on 1 Jan 2031. Fees as the register charges them in its forward world: the iBond funds' 0.07% (engine flows,
and plan.run's floor and moved half) and VT's 0.06%; waiting money earns forward short rates (the Treasury-bill ETF's
0.15% is charged only in the design test, section 0, not in the forward world).

How each holding is valued on a date t (the register's own conventions):
  * the ten rungs and the backstop (8h, reserve.py): each flow already received (a coupon, a fund distribution, a fund's
    payout) waits in the Treasury-bill ETF, grown at forwards from its arrival; each flow still to come is discounted on
    the 6 Nov curve's forwards to t (a forward market value). The backstop's 2027 flows are counted from their dates,
    as 8h counts them. On 1 Jan 2033 this gives 8h's $444,545 (asserted);
  * the floor (bought 1 Jan 2028 with plan.run's floor money) and the moved half (1 Jan 2031): the money put in grown at
    forwards from the purchase, less the fund fee from the purchase (plan.run's formula); on 15 Dec 2032 they pay
    plan.run's $103,178 and $20,298 (asserted), which then wait in the Treasury-bill ETF;
  * VT: plan.run's central path (7.5% a year less the 0.06% fee), filled in between its anchor dates (1 Jan 2028,
    1 Jan 2031, 1 Jan 2033) at a constant rate; half moves on 1 Jan 2031; the half kept reaches 8k's $21,347 (asserted).
The contribution leaves the broker in December 2032 (8k: "$115,000 paid in December 2032"); its exact day is not set.
Reading A: it leaves when the funds' cash arrives (Mon 20 to Wed 22 Dec 2032, 8h's cash dates), before 31 Dec 2032.
Reading B: it waits at the broker to 1 Jan 2033, as 8k's all-money total counts it; then 1 Jan 2033 equals $589,655.
Cash: in the model every waiting dollar is in the Treasury-bill ETF, an ETF share, so uninvested cash is $0 at every
month-end. For SIPC's $250,000 cash limit the script also gives the largest month-end cash if each month's receipts
waited uninvested to the month-end, and the December 2032 payouts if they waited as cash.
Sensitivity: the parallel rise in yields on 30 Nov 2032 alone (everything else central) that would take that month-end
under $500,000, and the balance with yields 1 point lower or higher that day.
"""
import calendar
import json
import math
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

RUN = "Mon 16 Nov 2026 (Sydney)"
OUTFILE = HERE / "results_custody_2026-11-16.json"
NAME = C.design_arg()
DSG = C.design(NAME)
OWN, POOL = DSG["own"], DSG["pool"] or {}
c, I, BASE = C.c, C.I, C.BASE
END = date(2032, 12, 15)
J28, J31, J33 = E.J28, E.J31, E.J33
FEE = E.ASSUMPTIONS["fund_fee"]
SIPC_TOTAL, SIPC_CASH = 500_000.0, 250_000.0
CASH_DAY = date(2032, 12, 22)        # the last day of IBTM's cash range (8h: Mon 20 to Wed 22 Dec 2032)

cen = P.run(c, margin=DSG["margin"], margin_fn=C.margin_fn(NAME))
fm, vt28, vt31 = float(cen["floor_money"]), float(cen["vt28"]), float(cen["vt31"])
floor_pay, moved_pay, kept33 = float(cen["floor"]), float(cen["moved"]), float(cen["kept33"])
rr = C.rule(cen)
contribution = float(rr["gift"])     # the stated top, $115,000
excess = float(rr["excess"])


def kind(y):
    return "ibond_etfs" if y in E.FUNDS else "treasury_bonds"


def reserve_parts(t, shift=0.0, nav=False):
    """The ten rungs and the backstop on date t: flows received wait in the Treasury-bill ETF (grown at forwards from
    arrival); flows to come at forwards to t, discounted at an extra parallel `shift` (continuous) if given.
    nav=False: 8h's convention, an iBond fund at the value of its flows after the fee still to be charged (so 1 Jan 2033
    gives $444,545). nav=True: at its net asset value, the gross holdings' value less only the fee already charged,
    which is what a broker's statement shows (each fund flow grossed up for the fee from t to the holdings' maturity)."""
    out = {"treasury_bonds": 0.0, "ibond_etfs": 0.0, "tbill_etf_waiting": 0.0}
    for y in E.YEARS:
        u = OWN.get(y, 0.0) + POOL.get(y, 0.0)
        if u <= 0:
            continue
        for d, a, _ in E.rung_flows(I[y], BASE):
            if d <= t:
                out["tbill_etf_waiting"] += u * a * BASE.grow(d, t)
            else:
                g = 1.0
                if nav and y in E.FUNDS:
                    g = (1 - FEE) ** -max(E.yf(min(d, I[y].hold_mat), t), 0.0)
                out[kind(y)] += u * a * g * c.P(d) / c.P(t) * math.exp(-shift * E.yf(d, t))
    return out


def fund_value(money, buy, t):
    """Money put into the late-2032 fund on `buy`, on date t <= 15 Dec 2032 (plan.run's formula: forwards, fee)."""
    return money * c.P(buy) / c.P(t) * (1 - FEE) ** E.yf(t, buy)


def vt_value(t):
    """VT on the central path (plan.run's anchors), constant growth between them; returns (VT held, of which kept)."""
    if t < J31:
        return vt28 * (vt31 / vt28) ** ((t - J28).days / (J31 - J28).days), 0.0
    k = vt31 / 2 * (kept33 / (vt31 / 2)) ** ((t - J31).days / (J33 - J31).days)
    return k, k


def balance(t, reading="A", shift=0.0, nav=False):
    r = reserve_parts(t, shift, nav)
    vt, _ = vt_value(t)
    floor_fund = moved_fund = 0.0
    facility_waiting = 0.0
    if t < END:
        floor_fund = fund_value(fm, J28, t)
        if t >= J31:
            moved_fund = fund_value(vt31 / 2, J31, t)
    else:
        g = BASE.grow(END, t)
        if reading == "B" or t < CASH_DAY:
            facility_waiting = (floor_pay + moved_pay) * g
        else:
            facility_waiting = excess * g        # the contribution has left; the excess stays (8k)
    parts = dict(r, floor_fund=floor_fund, moved_half_fund=moved_fund, facility_payout_waiting=facility_waiting, vt=vt)
    total = sum(parts.values())
    return total, parts


def month_ends():
    out = []
    for y in range(2028, 2033):
        for m in range(1, 13):
            out.append(date(y, m, calendar.monthrange(y, m)[1]))
    return out


def received_in_month(t):
    """Flows received in t's calendar month (coupons, distributions, payouts), grown to t: the most that would sit as
    uninvested cash at the month-end if each month's receipts were swept only after it."""
    s = 0.0
    for y in E.YEARS:
        u = OWN.get(y, 0.0) + POOL.get(y, 0.0)
        for d, a, _ in E.rung_flows(I[y], BASE):
            if d <= t and (d.year, d.month) == (t.year, t.month):
                s += u * a * BASE.grow(d, t)
    return s


# ---------------------------------------------------------------- checks against the register
r33 = reserve_parts(J33)
assert abs(sum(r33.values()) - 444_545) < 1.0, sum(r33.values())                    # 8h
assert abs(fund_value(fm, J28, END) - floor_pay) < 1e-6 and abs(floor_pay - 103_178) < 1.0     # section 4
assert abs(fund_value(vt31 / 2, J31, END) - moved_pay) < 1e-6 and abs(moved_pay - 20_298) < 1.0
assert abs(vt_value(J31)[0] - vt31 / 2) < 1e-6 and abs(vt_value(J33)[1] - kept33) < 1e-6 and abs(kept33 - 21_347) < 1.0
assert abs(vt31 - 36_989) < 1.0 and abs(vt28 - 29_829) < 1.0 and abs(fm - 81_889) < 1.0      # section 4
b33B = balance(J33, "B")[0]
assert abs(b33B - 589_655) < 2.0, b33B                                                 # 8k's all-money total
b28 = balance(date(2028, 1, 1))[0]                                                    # after the January 2028 purchases

# ---------------------------------------------------------------- month-ends
rows = []
for t in month_ends() + [J33]:
    for reading in ("A", "B"):
        if reading == "B" and t < date(2032, 12, 1):
            continue
        tot, parts = balance(t, reading)
        rows.append({"date": t.isoformat(), "reading": reading if t >= date(2032, 12, 1) else "A and B",
                     "total": tot, "parts": parts, "above_sipc_500k": tot > SIPC_TOTAL, "excess_over_500k": tot - SIPC_TOTAL,
                     "cash_if_month_receipts_unswept": received_in_month(t) if t != J33 else None})

me = [r for r in rows if r["date"] != J33.isoformat()]
peakA = max((r for r in me if r["reading"] != "B"), key=lambda r: r["total"])
peakB = max((r for r in me if r["reading"] != "A"), key=lambda r: r["total"])
first_above = next(r for r in me if r["total"] > SIPC_TOTAL)
last_below = [r for r in me if r["total"] <= SIPC_TOTAL and r["date"] < first_above["date"]][-1]
above_A = [r["date"] for r in me if r["reading"] != "B" and r["above_sipc_500k"]]
d15 = balance(END, "A")[0]
d21A = balance(date(2032, 12, 21), "A")[0]
j33A = balance(J33, "A")

# cash: the largest month's receipts at a month-end, and the December 2032 payouts if they waited as cash
cash_month = max((r for r in me if r["reading"] != "B"), key=lambda r: r["cash_if_month_receipts_unswept"])
ibtm_payout = sum(OWN.get(2033, 0.0) * a for d, a, k in E.rung_flows(I[2033], BASE) if d == END)
dec31 = date(2032, 12, 31)
dec_receipts = received_in_month(dec31)                   # IBTM's payout and December's other distributions
cash_dec_A = dec_receipts + excess * BASE.grow(END, dec31)
cash_dec_B = dec_receipts + (floor_pay + moved_pay) * BASE.grow(END, dec31)
cash_other = max((r for r in me if r["reading"] != "B" and r["date"] < "2032-12"),
                 key=lambda r: r["cash_if_month_receipts_unswept"])
# the same peak at net asset value (a broker's statement), and the first month-end above $500,000 on that basis
navA = max(((t, balance(t, "A", nav=True)[0]) for t in month_ends()), key=lambda x: x[1])
nav_first = next((t, v) for t, v in ((t, balance(t, "A", nav=True)[0]) for t in month_ends()) if v > SIPC_TOTAL)

# sensitivity on 30 Nov 2032: a parallel move in yields that day alone
t_s = date(2032, 11, 30)
base_s = balance(t_s)[0]
lo, hi = 0.0, 0.2
for _ in range(80):
    mid = (lo + hi) / 2
    if balance(t_s, "A", mid)[0] > SIPC_TOTAL:
        lo = mid
    else:
        hi = mid
breakeven = (lo + hi) / 2
sens = {f"{s:+.0%}": balance(t_s, "A", s)[0] for s in (-0.01, 0.01, 0.02)}
r_s = reserve_parts(t_s)
mv = r_s["treasury_bonds"] + r_s["ibond_etfs"]
r_up = reserve_parts(t_s, 0.0001)
dur = (mv - (r_up["treasury_bonds"] + r_up["ibond_etfs"])) / (0.0001 * mv)

out = {
    "stamp": {"run": RUN, "status": "MODEL", "curve": E.CURVE_DAY, "design": NAME, "label": DSG["label"],
              "numbers_section": "8t", "world": "today's forward rates; VT at its median 7.5% a year (plan.run central)",
              "fees": "iBond funds 0.07% (engine flows; plan.run floor and moved half); VT 0.06%; waiting money earns "
                      "forwards (the Treasury-bill ETF's 0.15% is the design test's, not the forward world's)",
              "one_broker": "every holding at one broker (CLAUDE.md; card Q78)",
              "reading_A": "the contribution leaves when the funds' cash arrives (by Wed 22 Dec 2032, 8h's cash dates)",
              "reading_B": "the contribution waits at the broker to 1 Jan 2033 (8k's all-money total counts it so)"},
    "checks": {"reserve_1jan2033": sum(r33.values()), "floor_payout": floor_pay, "moved_half_payout": moved_pay,
               "half_kept_1jan2033": kept33, "all_money_1jan2033_reading_B": b33B, "contribution": contribution,
               "excess": excess, "balance_1jan2028_after_purchases": b28},
    "peak_month_end_reading_A": {"date": peakA["date"], "total": peakA["total"], "parts": peakA["parts"],
                                 "excess_over_500k": peakA["total"] - SIPC_TOTAL},
    "peak_month_end_reading_B": {"date": peakB["date"], "total": peakB["total"], "parts": peakB["parts"],
                                 "excess_over_500k": peakB["total"] - SIPC_TOTAL},
    "first_month_end_above_500k": {"date": first_above["date"], "total": first_above["total"],
                                   "previous_month_end": last_below["date"], "previous_total": last_below["total"]},
    "month_ends_above_500k_reading_A": {"count": len(above_A), "first": above_A[0], "last": above_A[-1]},
    "15dec2032_before_the_funds_pay_out": d15,
    "21dec2032_reading_A_before_the_contribution_leaves": d21A,
    "1jan2033_before_first_payment": {"reading_A": j33A[0], "reading_A_parts": j33A[1], "reading_B": b33B},
    "cash": {"model_uninvested_cash_every_month_end": 0.0,
             "largest_month_receipts_unswept": {"date": cash_month["date"],
                                                "amount": cash_month["cash_if_month_receipts_unswept"]},
             "largest_month_receipts_unswept_before_dec2032": {"date": cash_other["date"],
                                                               "amount": cash_other["cash_if_month_receipts_unswept"]},
             "ibtm_own_rung_payout_15dec2032": ibtm_payout,
             "december_2032_reserve_receipts": dec_receipts,
             "31dec2032_if_december_receipts_wait_as_cash_reading_A": cash_dec_A,
             "31dec2032_if_december_receipts_wait_as_cash_reading_B": cash_dec_B,
             "sipc_cash_limit": SIPC_CASH},
    "nav_basis": {"peak_month_end_reading_A": {"date": navA[0].isoformat(), "total": navA[1]},
                  "first_month_end_above_500k": {"date": nav_first[0].isoformat(), "total": nav_first[1]},
                  "note": "iBond funds at net asset value (gross holdings less the fee already charged), as a broker's "
                          "statement shows them; the headline uses 8h's convention (after the fee still to come)"},
    "sensitivity_30nov2032": {"central": base_s, "parallel_yield_move_that_day": sens,
                              "rise_that_takes_it_under_500k": breakeven,
                              "reserve_bonds_and_ibond_etfs_value": mv, "their_duration_years": dur},
    "month_ends": rows,
}
OUTFILE.write_text(json.dumps(out, indent=1, default=float))

k = C.fmt
print("checks: reserve 1 Jan 2033", k(sum(r33.values())), "| floor", k(floor_pay), "| moved", k(moved_pay),
      "| half kept", k(kept33), "| all money 1 Jan 2033 (reading B)", k(b33B), "| 1 Jan 2028 after buying", k(b28))
for lab, p in (("A", peakA), ("B", peakB)):
    print(f"peak month-end, reading {lab}: {p['date']} {k(p['total'])} ({k(p['total'] - SIPC_TOTAL)} over $500,000)")
    print("   ", {a: k(b) for a, b in p["parts"].items()})
print("first month-end above $500,000:", first_above["date"], k(first_above["total"]), "| previous", last_below["date"],
      k(last_below["total"]))
print("month-ends above $500,000 (A):", len(above_A), above_A[0], "to", above_A[-1])
print("15 Dec 2032", k(d15), "| 21 Dec 2032 (A)", k(d21A), "| 1 Jan 2033 before the payment: A", k(j33A[0]), "B", k(b33B))
print("cash: largest month's receipts", cash_month["date"], k(cash_month["cash_if_month_receipts_unswept"]),
      "| before Dec 2032", cash_other["date"], k(cash_other["cash_if_month_receipts_unswept"]),
      "| IBTM payout", k(ibtm_payout), "| 31 Dec 2032 if December receipts wait as cash: A", k(cash_dec_A), "B", k(cash_dec_B))
print("NAV basis: peak (A)", navA[0], k(navA[1]), "| first above $500,000", nav_first[0], k(nav_first[1]))
print("30 Nov 2032:", k(base_s), {a: k(b) for a, b in sens.items()}, "| rise to go under $500,000",
      f"{breakeven:.2%}", "| reserve securities", k(mv), f"duration {dur:.2f}")
for r in rows:
    if r["date"][5:7] in ("06", "12") or r["date"] in (first_above["date"], last_below["date"]) or r["date"] == J33.isoformat():
        print(r["date"], r["reading"], k(r["total"]))
