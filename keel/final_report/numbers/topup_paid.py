"""What the top-up pays, reconciled with what it costs (numbers owner, Fri 13 Nov 2026, Sydney). MODEL.

Figure 1's right-hand column ("What the top-up pays", NUMBERS 8h) totals $55,920 if nothing earns interest and waiting
money pays the Treasury-bill ETF's 0.15% fee; the top-up's part bought for that (NUMBERS 2) costs $35,894 in January
2028. A bond reader (research/panel/2026-11-12_bond_desk_table3_built.md, section 2) guessed the bridge: $36,867 of face
and fund dollars plus about $19,000 of their coupons, summed undiscounted over the ten payment years. This script checks
it on the engine, and writes the cash dates Figure 1 uses (when the money reaches Laura, not when a fund ends).

Run from the repo root:  python3 -I keel/final_report/numbers/topup_paid.py
Writes keel/final_report/numbers/results_topup_2026-11-13.json (a few seconds). Read by NUMBERS 8h and
keel/final_report/exhibits/exhibit_data.py.

"If interest earns nothing" (the register's 'zero' world; 'fee' adds the ETF's fee): money already received earns
nothing while it waits for its payment; every coupon, every fund distribution and every fund's final payout still
arrives and counts. The funds' own 0.07% fee is in every flow.
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import completion as C    # noqa: E402

c, I, Y = C.c, C.I, C.Y
BACK = {y: u for y, u in C.BACKSTOP.items() if u > 0.5}
f01 = c.fwd(E.J27, E.J28)

rows, face, interest = [], 0.0, 0.0
for y, u in BACK.items():
    fl = E.rung_flows(I[y], C.ZERO)                   # at zero the fund's final payout is its cash, nothing added
    tot = u * sum(a for _, a, _ in fl)
    price28 = u * I[y].price * math.exp(f01)         # its 1 Jan 2027 cost carried a year, as completion_exact does
    rows.append({"pays_for": y, "holding": I[y].name, "face_or_fund_dollars": u, "cost_jan2027": u * I[y].price,
                 "price_jan2028": price28, "price_per_100_face_jan2028": 100 * price28 / u,
                 "all_flows_undiscounted": tot, "interest_undiscounted": tot - u,
                 "last_flow": max(d for d, _, _ in fl).isoformat()})
    face += u
    interest += tot - u

zero_paid, zero_avail, zero_carry, zero_left = C.ledger(C.ZERO, C.PLAIN, C.BACKSTOP)
fee_paid, fee_avail, fee_carry, fee_left = C.ledger(C.FEEW, C.PLAIN, C.BACKSTOP)
own_zero = C.own_amounts(C.PLAIN, C.ZERO)
own_fee = C.own_amounts(C.PLAIN, C.FEEW)
pool_zero = C.pool_buckets(C.BACKSTOP, C.ZERO)
pool_fee = C.pool_buckets(C.BACKSTOP, C.FEEW)
covers_zero = sum(E.PAYMENT - min(own_zero[y], E.PAYMENT) for y in Y)
covers_fee = sum(E.PAYMENT - min(own_fee[y], E.PAYMENT) for y in Y)
topup28 = C.completion_exact(0.0)[0]
tail28 = C.completion_exact(0.0, "plain")[0]

out = {"stamp": {"run": "Fri 13 Nov 2026 (Sydney)", "design": C.CALL, "curve": E.CURVE_DAY},
       "topup_jan2028": topup28, "ten_still_lack_jan2028": tail28, "for_no_interest_jan2028": topup28 - tail28,
       "for_no_interest_jan2027": C.cost(C.BACKSTOP),
       "holdings": rows,
       "face_and_fund_dollars": face,
       "interest_undiscounted": interest,
       "all_flows_undiscounted": face + interest,
       "zero": {"covers": covers_zero, "left_after_2042": zero_left,
                "check_covers_plus_left_equals_all_flows": covers_zero + zero_left},
       "fee": {"covers": covers_fee, "left_after_2042": fee_left,
               "fee_on_the_topups_own_waiting_money": face + interest - covers_fee - fee_left,
               "fee_on_the_tens_own_waiting_money": sum(own_zero[y] - own_fee[y] for y in Y)},
       "by_payment_fee_world": {y: {"own_pays": min(own_fee[y], E.PAYMENT), "topup_pays": E.PAYMENT - min(own_fee[y], E.PAYMENT),
                                    "topup_cash_arriving_for_it": pool_fee[y]} for y in Y}}
# what comes back from the top-up if rates follow today's forwards (8h, 8k), for the same sentence
res = json.loads((HERE / "results_reserve_2026-11-10.json").read_text())
out["comes_back_if_forwards_hold"] = {"nominal_by_1jan2042": res["base_left_after_2042"],
                                      "value_1jan2033": res["margin_value_1jan2033_at_forwards"]}

# ---------------------------------------------------------------- cash dates (Figure 1, since Fri 13 Nov)
# The iBond funds end "on or about" 15 Dec; the three that have ended paid holders 3 to 7 days later (IBTD 15 -> 22 Dec
# 2023, IBTE 16 -> 19 Dec 2024, IBTF 15 -> 18 Dec 2025; card Q16 row 6). Card Q2b card 5 turns that into a cash-in-hand
# range per fund (15 Dec 2035 is a Saturday: end taken as Mon 17 Dec, as IBTE in 2024). A Treasury bond pays on its
# maturity date, or the next business day if that is a weekend or a federal holiday (31 CFR 356.30; card Q16 row 12):
# 15 Feb 2037 is a Sunday and 16 Feb Presidents' Day, so Tue 17 Feb; 15 May 2038 is a Saturday, so Mon 17 May.
CASH = {2033: ("2032-12-20", "2032-12-22"), 2034: ("2033-12-19", "2033-12-22"), 2035: ("2034-12-18", "2034-12-22"),
        2036: ("2035-12-20", "2035-12-24"), 2037: ("2036-12-18", "2036-12-22"),
        2038: ("2037-02-17", "2037-02-17"), 2039: ("2038-05-17", "2038-05-17"), 2040: ("2039-11-15", "2039-11-15"),
        2041: ("2040-11-15", "2040-11-15"), 2042: ("2041-11-15", "2041-11-15")}
cash = {}
for y, (a, b) in CASH.items():
    d1, d2 = date.fromisoformat(a), date.fromisoformat(b)
    assert I[y].end <= d1 <= d2 < date(y, 1, 1) and d1.weekday() < 5 and d2.weekday() < 5
    cash[y] = {"ends": I[y].end.isoformat(), "cash_first": a, "cash_last": b,
               "days_to_payment_from_last": (date(y, 1, 1) - d2).days,
               "months_to_payment_from_last": round((date(y, 1, 1) - d2).days / 30.44, 2),
               "months_to_payment_model": round((date(y, 1, 1) - I[y].end).days / 30.44, 2)}
out["cash_dates"] = cash
(HERE / "results_topup_2026-11-13.json").write_text(json.dumps(out, indent=1))

k = C.fmt
print(f"top-up {k(topup28)} = ten still lack {k(tail28)} + for no interest {k(topup28 - tail28)} "
      f"({k(C.cost(C.BACKSTOP))} in 1 Jan 2027 money)")
for r in rows:
    print(f"  {r['holding']:<28} face {k(r['face_or_fund_dollars'])} cost27 {k(r['cost_jan2027'])} "
          f"price28 {k(r['price_jan2028'])} ({r['price_per_100_face_jan2028']:.2f}) flows {k(r['all_flows_undiscounted'])}"
          f" interest {k(r['interest_undiscounted'])}")
print(f"face and fund dollars {k(face)} + interest {k(interest)} = {k(face + interest)} undiscounted")
print(f"zero: covers {k(covers_zero)} + left {k(zero_left)} = {k(covers_zero + zero_left)}")
print(f"fee: covers {k(covers_fee)} left {k(fee_left)}; fee on the top-up's waiting money "
      f"{k(out['fee']['fee_on_the_topups_own_waiting_money'])}; on the ten's own {k(out['fee']['fee_on_the_tens_own_waiting_money'])}")
print("comes back at forwards", {a: k(b) for a, b in out["comes_back_if_forwards_hold"].items()})
for y, v in cash.items():
    print(y, v)
