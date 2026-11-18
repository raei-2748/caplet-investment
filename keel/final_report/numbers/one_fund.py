"""One fund, three promises: how much of Laura's plan rests on the late-2032 iBonds Treasury fund (IBTM)
(numbers owner, Thu 19 Nov 2026, Sydney). MODEL and Keel arithmetic, not a forecast or a promise. NUMBERS 8w.

A blind judge (research/panel/2026-11-19_judge_endowment_bond_pm.md, section 5 item 3) asked the plan to "make IBTM's
concentration explicit: one fund carries the 2033 payment, the bottom and the top". This script sizes it on the
register's central path, changing nothing in the engine:
  1. on 1 Jan 2028 (after the 2028 deposit's purchases), 1 Jan 2031 (after the move) and 1 Jan 2032, and for scale on
     Tue 30 Nov 2032 (8t's peak month-end): what Laura holds in IBTM, lot by lot (the 2033 payment's own lot, bought
     January 2027 with its $2,287 tail finished January 2028; the floor lot, January 2028; the moved lot, January 2031),
     in dollars and as a share of everything she holds at one broker, with the next-largest single holding beside it;
     and which promises each lot pays, with each promise's dollar figure;
  2. her IBTM as a share of the fund at today's size (net assets and shares outstanding read at source, ishares.com,
     17 Nov 2026), for her real plan ($450,000), with the WInS book ($300,000) beside it only as a reference;
  3. what one fund event (an early end, a merger, a moved end) touches at once: section 3's own worst gaps, read from
     results_fund_exit_2026-11-18.json and asserted against the figures the register prints (not recomputed).

Valuation (the register's own conventions, as 8t, numbers/custody.py):
  * world: today's forward rates on the 6 Nov 2026 curve, VT on plan.run's central 7.5% path, the escrow standard
    (completion.CALL), Keel's reading of "most", the move on 1 Jan 2031; waiting money earns forwards (the bill ETF's
    0.15% belongs to the design test, NUMBERS 0);
  * an iBond fund at net asset value, as a broker's statement shows it: units x the gross holdings' remaining flows on
    the date's forwards, less the 0.07% fee already charged (custody.py's nav=True for the ten; fund_exit.py's nav() for
    the two facility lots, units = money put in / that day's net asset value, as completion.zero_per_dollar);
  * each distribution already paid waits in the short-term Treasury ETF, grown at forwards: it belongs to the same
    promise but is no longer inside IBTM, so a fund event cannot touch it;
  * T-bonds at forward market value; VT as custody.vt_value.
The whole-portfolio total is reconciled with custody.py's NAV-basis balance (which grows the facility lots as one sum,
plan.run's formula, so it charges the fund fee on a distribution even after it is paid out): adding that fee back ($0 on
1 Jan 2028, $14 to $39 later) the two agree to the cent, an asserted identity; and 8t's headline figures ($462,496 on 1 Jan 2028; $587,008 and, at net asset value,
$587,192 on 30 Nov 2032) are reproduced by a copy of custody.py's functions (custody.py itself is not imported: it
writes its results file on import).

Run from the repo root:  python3 -I keel/final_report/numbers/one_fund.py
Writes keel/final_report/numbers/results_one_fund_2026-11-19.json and prints the figures (about 10 seconds, numpy only).
Imports engine, plan and completion and changes none of them; reads results_fund_exit_2026-11-18.json (read only).
"""
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

RUN = "Thu 19 Nov 2026 (Sydney), numbers owner"
OUT = HERE / "results_one_fund_2026-11-19.json"
FUND_EXIT = HERE / "results_fund_exit_2026-11-18.json"

NAME = C.CALL
DSG = C.design(NAME)
OWN, POOL = DSG["own"], DSG["pool"] or {}
c, I, BASE = C.c, C.I, C.BASE
FEE, END, WAM, HOLD = E.ASSUMPTIONS["fund_fee"], C.END, C.WAM, C.HOLD["engine"]
J27, J28, J31, J33 = E.J27, E.J28, E.J31, E.J33


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


# ---------------------------------------------------------------- IBTM read at source (not the engine)
FUND = {"net_assets": 641_351_942.0, "shares_outstanding": 29_250_000.0, "nav_per_share": 21.9352,
        "as_of": "17 Nov 2026", "holdings": 15,
        "source": "https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf "
                  "(read Thu 19 Nov 2026, Sydney; the same $641,351,942 was read at blackrock.com on 18 Nov, card Q146 "
                  "row 26)"}
WINS = {"ibtm_shares": 4_503, "ibtm_cost": 97_489.95, "ibtm_share_of_book": 0.3250,
        "source": "NUMBERS 8g (at cost on the original $300,000); CANON D2 (4,503 shares: 1,142 rung, 3,361 floor)"}

# ---------------------------------------------------------------- the register's central figures (asserted)
cen = P.run(c, margin=DSG["margin"], margin_fn=C.margin_fn(NAME))
rr = C.rule(cen)
f = float
FM, MM = f(cen["floor_money"]), f(cen["moved_money"])
vt28, vt31, kept33 = f(cen["vt28"]), f(cen["vt31"]), f(cen["kept33"])
floor_pay, moved_pay = f(cen["floor"]), f(cen["moved"])
BOT, TOP = f(rr["bottom"]), f(rr["top"])
FZ, MZ = f(rr["floor_zero"]), f(rr["moved_zero"])
near(FM, 81_244.28, 0.01, "floor money (section 4)")
near(MM, 18_349.05, 0.01, "moved money (section 3)")
near(vt28, 29_594, 1, "VT bought Jan 2028")
near(vt31, 36_698, 1, "VT on 1 Jan 2031")
near(kept33, 21_179, 1, "half kept on 1 Jan 2033")
near(floor_pay, 102_365, 1, "floor payout late 2032")
near(moved_pay, 20_138, 1, "moved half's payout late 2032")
near(floor_pay + moved_pay, 122_503, 1, "what the late-2032 fund pays on its two purchases")
assert (BOT, TOP) == (95_000.0, 115_000.0) and f(rr["gift"]) == 115_000.0
near(FZ, 98_096, 1, "floor lot's zero-interest value")
near(FZ + MZ, 117_731, 1, "both lots' zero-interest value")
assert POOL.get(2033, 0.0) == 0.0          # the extra Treasuries hold no IBTM (8h; section 3's block)

# the 2033 payment's own lot: what it pays (8h)
own_fwd = C.own_amounts(OWN, BASE)[2033]
own_std = C.own_amounts(OWN, C.FEEW)[2033]
near(own_fwd, 50_000, 0.01, "IBTM's own lot pays $50,000 at forwards (8h)")
near(own_std, 47_338, 1, "IBTM's own lot under the standard (8h)")
near(I[2033].price * OWN[2033], 37_908, 1, "the 2033 rung's cost, 1 Jan 2027 money (8a)")


# ---------------------------------------------------------------- valuation
def inst_parts(y, t, nav=True):
    """One of the ten holdings (own rung + any extra Treasuries in it) on date t: (held, waiting in the bill ETF).
    nav=True: an iBond fund at net asset value (custody.py's nav=True); False: 8h's convention (after the fee still to
    come)."""
    u = OWN.get(y, 0.0) + POOL.get(y, 0.0)
    held = waiting = 0.0
    for d, a, _ in E.rung_flows(I[y], BASE):
        if d <= t:
            waiting += u * a * BASE.grow(d, t)
        else:
            g = (1 - FEE) ** -max(E.yf(min(d, I[y].hold_mat), t), 0.0) if (nav and y in E.FUNDS) else 1.0
            held += u * a * g * c.P(d) / c.P(t)
    return held, waiting


def nav_gross(buy, t):
    """The holdings' remaining gross flows after t, valued on t on today's forwards (fund_exit.nav)."""
    return sum(a * math.exp(-max(c.fwd(t, d), 0.0) * E.yf(d, t)) for d, a in HOLD if d > t)


def lot_parts(buy, money, t):
    """A facility lot of IBTM bought on `buy` with `money` (units x that day's net asset value), on date t <= 15 Dec
    2032: (held in IBTM at net asset value, distributions already paid waiting in the bill ETF at forwards)."""
    if t < buy:
        return 0.0, 0.0
    units = money / nav_gross(buy, buy)
    waiting = sum(units * a * (1 - FEE) ** E.yf(d, buy) * BASE.grow(d, t)
                  for d, a in HOLD if buy < d <= t and not (d == WAM and t >= WAM))
    if t < WAM:
        held = units * nav_gross(buy, t) * (1 - FEE) ** E.yf(t, buy)
    else:                                               # the holdings have matured: cash inside the fund, at forwards
        a_w = [a for d, a in HOLD if d == WAM][0]
        held = units * a_w * (1 - FEE) ** E.yf(t, buy) * BASE.grow(WAM, t)
    return held, waiting


def lot_waiting_fee_to_t(buy, money, t):
    """The same lot's distributions already paid, with the fund fee charged to t (plan.run's lumping), for the
    reconciliation only."""
    if t < buy:
        return 0.0
    units = money / nav_gross(buy, buy)
    return sum(units * a * (1 - FEE) ** E.yf(t, buy) * BASE.grow(d, t)
               for d, a in HOLD if buy < d <= t and not (d == WAM and t >= WAM))


def vt_value(t):
    """VT on plan.run's central path, constant growth between its anchors (custody.vt_value)."""
    if t < J31:
        return vt28 * (vt31 / vt28) ** ((t - J28).days / (J31 - J28).days)
    return vt31 / 2 * (kept33 / (vt31 / 2)) ** ((t - J31).days / (J33 - J31).days)


def custody_balance(t, nav=False):
    """custody.balance(t, 'A', nav=nav) for t < 15 Dec 2032, copied (the facility lots grown as one sum)."""
    tot = sum(sum(inst_parts(y, t, nav)) for y in E.YEARS)
    tot += FM * c.P(J28) / c.P(t) * (1 - FEE) ** E.yf(t, J28)
    if t >= J31:
        tot += MM * c.P(J31) / c.P(t) * (1 - FEE) ** E.yf(t, J31)
    return tot + vt_value(t)


# 8t reproduced (custody.py's headline and net-asset-value figures)
near(custody_balance(J28), 462_496, 1, "8t: 1 Jan 2028 after the purchases")
near(custody_balance(date(2032, 11, 30)), 587_008, 1, "8t: peak month-end, 30 Nov 2032")
near(custody_balance(date(2032, 11, 30), nav=True), 587_192, 1, "8t: the same at net asset value")
near(custody_balance(date(2029, 8, 31)), 501_210, 1, "8t: first month-end above $500,000")


def name(y):
    return E.FUNDS[y] if y in E.FUNDS else I[y].name


def snapshot(t):
    rows = {}
    waiting = 0.0
    for y in E.YEARS:
        h, w = inst_parts(y, t)
        rows[name(y)] = h
        waiting += w
    ibtm_rung = rows.pop("IBTM")
    fl_h, fl_w = lot_parts(J28, FM, t)
    mv_h, mv_w = lot_parts(J31, MM, t)
    rung_w = inst_parts(2033, t)[1]
    waiting += fl_w + mv_w
    vt = vt_value(t)
    ibtm = ibtm_rung + fl_h + mv_h
    total = ibtm + sum(rows.values()) + waiting + vt
    # custody.py grows each facility lot as one sum with the fee charged to t on every dollar; held + waiting here
    # charges the fund's fee on a distribution only until it is paid out. With the fee charged to t on the waiting
    # distributions too, the two are the same sum to the cent (the identity), so the whole-portfolio total differs
    # from custody.py's net-asset-value balance by that fee alone.
    fee_wedge = sum(lot_waiting_fee_to_t(b, mo, t) for b, mo in ((J28, FM), (J31, MM))) - (fl_w + mv_w)
    near(total + fee_wedge, custody_balance(t, nav=True), 0.01, f"identity with custody.py's NAV basis, {t}")
    assert -50 < fee_wedge <= 0, fee_wedge
    others = dict(rows, **{"short-term Treasury ETF (all waiting money)": waiting, "VT": vt})
    nxt = max(others, key=others.get)
    nxt_single = max((k for k in others if k != "short-term Treasury ETF (all waiting money)"), key=others.get)
    promises = [{"promise": "the 2033 payment (IBTM is its own Treasury holding)", "figure": 50_000.0,
                 "lot": "own lot (January 2027; $2,287 tail January 2028)",
                 "pays": "$50,000 at today's forwards; $47,338 if cash waiting earns nothing, the extra Treasuries "
                         "the other $2,662 (8h)"}]
    if t >= J28:
        promises.append({"promise": "the bottom" + (" (owned, not yet stated: stated in 2031)" if t < J31 else
                                                   " (stated in 2031)"),
                         "figure": BOT, "lot": "floor lot (January 2028)",
                         "pays": "zero-interest value $98,096; $102,365 at today's forwards (section 4)"})
    if t >= J31:
        promises.append({"promise": "the top = the 2033 contribution (stated in 2031)", "figure": TOP,
                         "lot": "floor lot + moved lot (the late-2032 fund bought twice)",
                         "pays": "zero-interest value $117,731; $122,503 at today's forwards (section 4)"})
    return {"date": t.isoformat(), "ibtm": {"own_lot_2033_payment": ibtm_rung, "floor_lot": fl_h, "moved_lot": mv_h,
                                            "total": ibtm},
            "ibtm_distributions_already_paid_waiting_in_bill_etf": {"own_lot": rung_w, "floor_lot": fl_w,
                                                                   "moved_lot": mv_w},
            "whole_portfolio": total, "ibtm_share": ibtm / total,
            "bill_etf_all_waiting": waiting, "bill_etf_share": waiting / total,
            "whole_portfolio_custody_lumping": custody_balance(t, nav=True), "fee_wedge": fee_wedge,
            "whole_portfolio_8t_headline_basis": custody_balance(t, nav=False),
            "ibtm_with_its_distributions_waiting": ibtm + rung_w + fl_w + mv_w,
            "ibtm_with_its_distributions_waiting_share": (ibtm + rung_w + fl_w + mv_w) / total,
            "next_largest_holding": {"name": nxt, "value": others[nxt], "share": others[nxt] / total},
            "next_largest_single_security": {"name": nxt_single, "value": others[nxt_single],
                                             "share": others[nxt_single] / total},
            "facility_lots_reconcile_with_plan_run": {
                "floor_lot_held_plus_waiting": fl_h + fl_w,
                "plan_run_formula": FM * c.P(J28) / c.P(t) * (1 - FEE) ** E.yf(t, J28) if t >= J28 else 0.0},
            "ibtm_share_of_fund_17nov2026": ibtm / FUND["net_assets"],
            "ibtm_equivalent_shares_at_17nov2026_nav": ibtm / FUND["nav_per_share"],
            "ibtm_equivalent_shares_share_of_shares_outstanding": ibtm / FUND["nav_per_share"] / FUND["shares_outstanding"],
            "promises_ibtm_pays": promises,
            "promised_dollars_on_ibtm": sum(p["figure"] for p in promises if not p["promise"].startswith("the bottom")
                                            or t < J31)}


DATES = [J28, J31, date(2032, 1, 1), date(2032, 11, 30)]
snaps = [snapshot(t) for t in DATES]
# 1 Jan 2028: the floor lot is exactly the money put in; 1 Jan 2031: the moved lot is exactly the money moved
near(snaps[0]["ibtm"]["floor_lot"], FM, 0.01, "floor lot on its trade day")
near(snaps[1]["ibtm"]["moved_lot"], MM, 0.01, "moved lot on its trade day")
# 8t's 30 Nov 2032 parts: the facility lots as one sum ($102,158 + $20,097, plan.run's formula) against held + waiting
near(FM * c.P(J28) / c.P(date(2032, 11, 30)) * (1 - FEE) ** E.yf(date(2032, 11, 30), J28), 102_158, 1, "8t floor")

# how much VT alone moves IBTM's share on 1 Jan 2031: VT on that day at section 4's house 1-in-20 low and high (each
# its own percentile), everything else central. After the move half of VT is in the moved lot and half is VT, so the
# moved lot and VT are each v / 2 (Keel arithmetic on the central path; not a house-model distribution)
VT31_HOUSE = {"1-in-20 low": 18_962.0, "1-in-20 high": 61_435.0}      # section 4, "VT on 1 Jan 2031"
s31 = snaps[1]
vt_sens = {}
for lab, v in VT31_HOUSE.items():
    ib = s31["ibtm"]["total"] - MM + v / 2
    tot = s31["whole_portfolio"] - vt31 + v
    vt_sens[lab] = {"vt_1jan2031": v, "ibtm": ib, "whole_portfolio": tot, "ibtm_share": ib / tot}
near(s31["whole_portfolio"] - vt31 + vt31, s31["whole_portfolio"], 1e-6, "identity")

# promised dollars: the ten payments and the stated top (the bottom sits inside the top)
ALL_PROMISED = 10 * E.PAYMENT + TOP
on_ibtm = E.PAYMENT + TOP
near(on_ibtm / ALL_PROMISED, 0.2683, 0.0001, "share of promised dollars")

# ---------------------------------------------------------------- section 3's worst gaps (quoted, read and asserted)
fx = json.loads(FUND_EXIT.read_text())
rs, pay = fx["range_summary"], fx["payments_ibtm_exit"]
m = {q["exit"]: q for q in pay["monthly"]}
event = {
    "top_largest_short_zero": rs["largest_short_zero"], "top_first_exit_short": rs["first_exit_short"],
    "top_covered_from": rs["covered_from"], "top_exits_short": rs["exits_short_of_top_zero"],
    "bottom_largest_short_zero": rs["largest_floor_short_of_bottom_zero"],
    "bottom_last_exit_short": rs["last_exit_floor_short_of_bottom"],
    "bottom_exits_short": rs["exits_floor_lot_short_of_bottom_zero"],
    "top_smallest_room_at_market_rates": rs["smallest_room_forwards"],
    "above_top_no_exit_at_market_rates_this_method": fx["no_exit_forwards_this_method"] - TOP,
    "ten_short_exit_1jan2031": m["2031-01-01"]["standard_short"],
    "ten_short_exit_1jan2031_by_year": m["2031-01-01"]["standard_short_by_year"],
    "ten_short_exit_1jul2031": m["2031-07-01"]["standard_short"],
    "ten_short_worst_exit": pay["worst"]["exit"], "ten_short_worst": pay["worst"]["standard_short"],
    "ten_last_exit_short": pay["last_exit_short_standard"],
    "ten_short_exit_1jan2031_with_0.5pct_cost": m["2031-01-01"]["standard_with_0.5pct_cost_short"],
    "ten_last_exit_short_with_0.5pct_cost": pay["last_exit_short_with_0.5pct_cost"],
    "ten_short_at_market_rates_any": any(q["forwards_short"] > 0.005 for q in pay["monthly"]),
}
near(event["top_largest_short_zero"], 4_589, 1, "section 3: $4,589")
near(event["bottom_largest_short_zero"], 2_887, 1, "section 3: $2,887")
near(event["top_smallest_room_at_market_rates"], 7_295, 1, "section 3: $7,295 over")
near(event["above_top_no_exit_at_market_rates_this_method"], 7_459, 1, "section 3: $7,459 over")
near(event["ten_short_exit_1jan2031"], 1_827, 1, "section 3: $1,827")
near(event["ten_short_exit_1jul2031"], 936, 1, "section 3: $936")
near(event["ten_short_worst"], 8_671, 1, "section 3: $8,671")
near(event["ten_short_exit_1jan2031_with_0.5pct_cost"], 2_756, 1, "section 3: $2,756")
assert event["top_covered_from"] == "2032-01-01" and event["bottom_last_exit_short"] == "2031-10-01"
assert event["ten_last_exit_short"] == "2032-01-01" and event["ten_last_exit_short_with_0.5pct_cost"] == "2032-07-01"
assert list(event["ten_short_exit_1jan2031_by_year"]) == ["2036"] and not event["ten_short_at_market_rates_any"]

out = {"run": RUN, "status": "MODEL, Keel arithmetic", "numbers_section": "8w", "curve": E.CURVE_DAY, "design": NAME,
       "world": "today's forward rates; VT on plan.run's central 7.5% path; iBond funds at net asset value",
       "fund_read_at_source": FUND, "wins_reference": WINS,
       "wins_ibtm_share_of_fund_by_shares": WINS["ibtm_shares"] / FUND["shares_outstanding"],
       "promises": {"ten_payments": 10 * E.PAYMENT, "stated_top": TOP, "stated_bottom": BOT,
                    "all_promised": ALL_PROMISED, "on_ibtm": on_ibtm, "on_ibtm_share": on_ibtm / ALL_PROMISED,
                    "own_lot_pays_forwards": own_fwd, "own_lot_pays_standard": own_std},
       "snapshots": snaps, "vt_sensitivity_1jan2031": vt_sens, "one_fund_event_section_3": event}
OUT.write_text(json.dumps(out, indent=1, default=float))

k = C.fmt
print("IBTM read at source:", k(FUND["net_assets"]), "net assets,", f"{FUND['shares_outstanding']:,.0f} shares,",
      "NAV", FUND["nav_per_share"], FUND["as_of"])
for s in snaps:
    b = s["ibtm"]
    print(f"{s['date']}: IBTM {k(b['total'])} = own lot {k(b['own_lot_2033_payment'])} + floor lot {k(b['floor_lot'])}"
          f" + moved lot {k(b['moved_lot'])} | of {k(s['whole_portfolio'])} = {s['ibtm_share']:.1%} | next "
          f"{s['next_largest_holding']['name']} {k(s['next_largest_holding']['value'])} "
          f"({s['next_largest_holding']['share']:.1%}); next single security "
          f"{s['next_largest_single_security']['name']} {k(s['next_largest_single_security']['value'])} "
          f"({s['next_largest_single_security']['share']:.1%}) | of the fund {s['ibtm_share_of_fund_17nov2026']:.4%}"
          f" ({s['ibtm_equivalent_shares_at_17nov2026_nav']:,.0f} shares) | waiting from IBTM "
          f"{ {a: k(v) for a, v in s['ibtm_distributions_already_paid_waiting_in_bill_etf'].items()} }")
    print("    floor lot held+waiting", k(s["facility_lots_reconcile_with_plan_run"]["floor_lot_held_plus_waiting"]),
          "plan.run formula", k(s["facility_lots_reconcile_with_plan_run"]["plan_run_formula"]),
          "| promises:", [(p["promise"], k(p["figure"])) for p in s["promises_ibtm_pays"]])
print("promised dollars on IBTM", k(on_ibtm), "of", k(ALL_PROMISED), f"{on_ibtm / ALL_PROMISED:.1%}",
      "| WInS:", f"{WINS['ibtm_shares'] / FUND['shares_outstanding']:.4%} of shares outstanding")
print("VT alone, 1 Jan 2031:", {a: (k(b["vt_1jan2031"]), f"{b['ibtm_share']:.1%}") for a, b in vt_sens.items()})
print("section 3 (quoted):", {a: (k(v) if isinstance(v, float) else v) for a, v in event.items()})
print("wrote", OUT)
