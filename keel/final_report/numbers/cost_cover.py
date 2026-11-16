"""Fund costs beyond the 0.07% fee, against the range and against the payments; and a trade-day limit for Table 3 row 5
(numbers owner, Tue 17 Nov 2026, Sydney). MODEL, not a forecast or a promise. NUMBERS 3 ("Bond desk 4's check
figures"), 2 ("The payments' own exposure to fund costs") and 4 ("A trade-day limit").

Run from the repo root:  python3 -I keel/final_report/numbers/cost_cover.py
   or from this folder:  python3 -I cost_cover.py
Writes keel/final_report/numbers/results_cost_cover_2026-11-17.json and prints every figure (about 20 seconds, numpy
only). Imports engine.py, plan.py and completion.py and changes none of them; reads no results file. Every path and
rule is the register's (design H_plain with the fee cushion, the range rule on the fund's holdings with the fee charged
from each trade day, Keel's reading of "most", house model 200,000 paths, seed 2033), called exactly as range_rule.py
and range_margin.py call them.

Part A, bond desk 4's check figures (research/panel/2026-11-16_bond_desk_4_3c_and_monitoring.md, check1 and check2;
NUMBERS 9, "Mon 16 Nov night"). A "cost beyond the fees" is x% of what the funds pay, taken off on top of the 0.07% fund
fee and the bill fund's 0.15% that the rule already charges. The top is missed at cost x if
  * at zero interest:  (floor + moved half's zero-interest value) x (1 - x) < stated top, so the cover is 1 - top / that;
  * at the interest the market expects: what the two funds pay (plan.run, the path's own rates) x (1 - x) < stated top,
    so the cover is 1 - top / what the funds pay.
Plus the contribution's place against $95,000-$115,000 from today (51.2%: a check figure, never printed), and the floor's
holdings' coupons paid out before its end (check3).

Part B, the payments' own exposure (coherence reader 6, M9). The same kind of cost, x% off every flow of the five iBond
funds (IBTM, IBTO, IBTP, IBTQ, IBTR: the own rungs and the backstop's extra IBTQ and IBTR), run through the register's
ledger (completion.ledger) in three worlds: today's forwards, zero interest, and zero interest with the bill fund's 0.15%
on every waiting dollar (the standard of section 2). The T-bonds carry no fund cost. x is 0.1%, 0.5% (the share the
range carries for the same costs) and a cost that grows with time, 0.03 points a year from 1 Jan 2027 to each fund's end
(IBTF's 2022 tracking beyond its fee, NUMBERS 0, the haircut row). "Cost share times payout": x times what each fund rung
pays at zero interest, summed; the ledger then says which payment is short and by how much.

Part C, a trade-day limit (Table 3 row 5, bond desk 4, M6). Since card Q45 "money put in" is units x that day's net asset
value (NUMBERS 0), so a fill above or below net asset value can lower a stated end but never make one unowned. With every
fund leg filled p% off net asset value against Laura (a premium paid, a discount taken):
  * January 2027: the five funds cost p more per dollar of net asset value, so the top-up is larger, carried to
    January 2028 at the curve's 2027 rate (IPS l.13); January 2028: the top-up's IBTM and the extra IBTQ and IBTR the
    same; the floor buys 1 / (1 + p) of the net asset value;
  * the 2031 move: VT sold at 1 - p and the late-2032 fund bought at 1 + p.
Central path through plan.run (the extra cost enters as part of the January 2028 completion); house model for the two
range legs alone (the floor and the move, the 2027 legs left out there), counting paths whose stated bottom or top steps
down a $5,000 step.
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
NAME = C.CALL
MARGIN = C.design(NAME)["margin"]
MF = C.margin_fn(NAME)
OUT = HERE / "results_cost_cover_2026-11-17.json"
COSTS = (0.005, 0.0075, 0.01, 0.02, 0.03)
FUND_YEARS = (2033, 2034, 2035, 2036, 2037)
f = lambda x: float(np.asarray(x).item())
out = {"run": "Tue 17 Nov 2026 (Sydney), numbers owner", "rule": C.RULE_VERSION, "design": NAME}

# ================================================================ Part A: bond desk 4's check figures
cen = P.run(c, margin=MARGIN, margin_fn=MF)
rc = C.rule(cen)
Fz, Mz, Tz = f(rc["floor_zero"]), f(rc["moved_zero"]), f(rc["zero_world"])
bot, top, pay = f(rc["bottom"]), f(rc["top"]), f(rc["payout"])
b_raw, t_raw = f(rc["bottom_raw"]), f(rc["top_raw"])
A = {
    "central": {
        "floor_zero": Fz, "moved_zero": Mz, "both_zero": Tz, "bottom_raw": b_raw, "top_raw": t_raw,
        "stated_bottom": bot, "stated_top": top, "funds_pay_modelled": pay,
        "top_haircut": Tz - t_raw, "top_rounding": t_raw - top, "bottom_haircut": Fz - b_raw, "bottom_rounding": b_raw - bot,
        "cover_top_zero_interest": 1 - top / Tz, "cover_top_modelled_payout": 1 - top / pay,
        "cover_bottom_floor_alone_zero": 1 - bot / Fz, "cover_bottom_both_funds_zero": 1 - bot / Tz,
        "cover_bottom_modelled_payout": 1 - bot / pay,
        "per_0.1pct_of_both_funds_zero": 0.001 * Tz,
    }
}
print("A. central: both funds' zero-interest value %.2f, stated top %.0f, haircut %.2f + rounding %.2f = %.2f"
      % (Tz, top, Tz - t_raw, t_raw - top, Tz - top))
print("   cover at zero interest 1 - %.0f/%.2f = %.4f%%; at the modelled payout 1 - %.0f/%.2f = %.4f%%"
      % (top, Tz, 100 * (1 - top / Tz), top, pay, 100 * (1 - top / pay)))
print("   bottom: below it only at costs of %.2f%% (floor alone, zero interest) / %.2f%% (both funds, zero) / %.2f%% (modelled)"
      % (100 * (1 - bot / Fz), 100 * (1 - bot / Tz), 100 * (1 - bot / pay)))

d0, d1, d2, vt3, vt2 = P.draws(P.N, P.SEED)
H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
sF, sM = d0 + d1, d0 + d1 + d2
rh = C.rule(H, sF, sM)
B, T, PAY, TZ, GIFT = rh["bottom"], rh["top"], rh["payout"], rh["zero_world"], rh["gift"]
n = len(B)
house = {"paths": n, "by_cost": {}}
for x in COSTS:
    zt, zb = TZ * (1 - x) < T - 0.5, TZ * (1 - x) < B - 0.5
    pt, pb = PAY * (1 - x) < T - 0.5, PAY * (1 - x) < B - 0.5
    house["by_cost"][f"{x:.4f}"] = {
        "zero_interest_top_missed": int(zt.sum()), "zero_interest_top_missed_share": float(zt.mean()),
        "zero_interest_largest_gap_top": float(np.max(T - TZ * (1 - x))) if zt.any() else 0.0,
        "zero_interest_below_bottom": int(zb.sum()),
        "modelled_top_missed": int(pt.sum()), "modelled_top_missed_share": float(pt.mean()),
        "modelled_largest_gap_top": float(np.max(T - PAY * (1 - x))) if pt.any() else 0.0,
        "modelled_below_bottom": int(pb.sum()),
    }
    print("   house, cost %.2f%%: zero interest top missed %d (%.3f%%), below bottom %d; modelled payout top missed %d, below bottom %d"
          % (100 * x, zt.sum(), 100 * zt.mean(), zb.sum(), pt.sum(), pb.sum()))
cz, cm = 1 - T / TZ, 1 - T / PAY
house["cover_zero"] = {"min": float(cz.min()), "p5": float(np.percentile(cz, 5)), "median": float(np.median(cz))}
house["cover_modelled"] = {"min": float(cm.min()), "p5": float(np.percentile(cm, 5)), "median": float(np.median(cm)),
                           "argmin_floor_money": float(np.asarray(H["floor_money"])[np.argmin(cm)]),
                           "argmin_most_binds": bool(np.asarray(H["most_binds"])[np.argmin(cm)])}
print("   cover at zero interest: min %.3f%% p5 %.3f%% median %.3f%%; at the modelled payout: min %.3f%% p5 %.3f%% median %.3f%%"
      % (100 * cz.min(), 100 * np.percentile(cz, 5), 100 * np.median(cz), 100 * cm.min(), 100 * np.percentile(cm, 5),
         100 * np.median(cm)))
inr = (GIFT >= 95_000) & (GIFT <= 115_000)
house["never_printed"] = {
    "contribution_in_95k_115k": float(inr.mean()),
    "stated_range_exactly_95k_115k": float(((B == 95_000) & (T == 115_000)).mean()),
    "contribution_at_least_95k": float((GIFT >= 95_000).mean()),
    "note": "check figures from today, never printed (bond desk 4, M1): the certainty belongs to the range stated in 2031",
}
house["printable_instead"] = {"stated_bottom_at_least_95k": float((B >= 95_000).mean()),
                              "stated_top_at_least_115k": float((T >= 115_000).mean())}
print("   never printed: contribution in $95,000-$115,000 %.2f%%; range exactly that %.2f%%; contribution >= $95,000 %.2f%%"
      % (100 * inr.mean(), 100 * house["never_printed"]["stated_range_exactly_95k_115k"],
         100 * house["never_printed"]["contribution_at_least_95k"]))
A["house"] = house

# check3: the floor's holdings' coupons paid out before its end (they wait in the bill fund, NUMBERS 0)
WAM, END, FEE = C.WAM, C.END, C.FEE


def parts(buy, money):
    fl = [(d, a) for d, a in C.HOLD["engine"] if d > buy]
    nav = sum(a * c.P(d, base=buy) for d, a in fl)
    dist_net = sum(a * (1 - FEE) ** E.yf(d, buy) * math.exp(-C.WAIT_FEE * E.yf(END, d)) for d, a in fl if d != WAM)
    dist_face = sum(a * (1 - FEE) ** E.yf(d, buy) for d, a in fl if d != WAM)
    last = [a for d, a in fl if d == WAM][0] * (1 - FEE) ** E.yf(END, buy)
    dates = [d.isoformat() for d, a in fl if d != WAM]
    return {"paid_before_end_net_of_bill_fee": money * dist_net / nav, "paid_before_end_at_face": money * dist_face / nav,
            "final_flow": money * last / nav, "count": len(dates), "first": dates[0], "last": dates[-1]}


fm_c, mm_c = f(cen["floor_money"]), f(cen["moved_money"])
A["payouts_before_end"] = {"floor": parts(E.J28, fm_c), "moved_half": parts(E.J31, mm_c),
                           "note": "the engine's holdings pay semiannual coupons (the real fund pays monthly); the "
                                   "coupon at the holdings' maturity (4 Jul 2032) is in the final flow, as check3"}
pf, pm = A["payouts_before_end"]["floor"], A["payouts_before_end"]["moved_half"]
print("   floor's coupons paid before its end: %.2f (at face %.2f), %d coupons %s to %s; final flow %.2f; sum %.2f vs %.2f"
      % (pf["paid_before_end_net_of_bill_fee"], pf["paid_before_end_at_face"], pf["count"], pf["first"], pf["last"],
         pf["final_flow"], pf["paid_before_end_net_of_bill_fee"] + pf["final_flow"], Fz))
print("   moved half's: %.2f" % pm["paid_before_end_net_of_bill_fee"])
assert abs(pf["paid_before_end_net_of_bill_fee"] + pf["final_flow"] - Fz) < 0.01
out["A_bond_desk_4"] = A

# ================================================================ Part B: the payments' own exposure


def insts_less(x_by_year):
    """The ten instruments with each iBond fund's flows cut by x (a cost beyond the fee, off every flow)."""
    ins = {}
    for y in E.YEARS:
        i = copy.copy(C.I[y])
        x = x_by_year.get(y, 0.0)
        if x:
            i.flows = [(d, a * (1 - x), k) for d, a, k in C.I[y].flows]
        ins[y] = i
    return ins


WORLDS = {"forwards": C.BASE, "zero": C.ZERO, "zero_and_bill_fee": C.FEEW}
OWN, POOL = C.PLAIN, C.BACKSTOP


def exposure(x_by_year, label):
    ins = insts_less(x_by_year)
    res = {"x_by_year": {str(y): x for y, x in x_by_year.items()}}
    # cost share times each fund rung's payout at zero interest (own units plus the backstop's units)
    share = {}
    for y in FUND_YEARS:
        units = OWN.get(y, 0.0) + (POOL.get(y, 0.0) if POOL else 0.0)
        paid0 = units * sum(a for d, a, _ in E.rung_flows(C.I[y], C.ZERO))
        paidf = units * sum(a * C.FEEW.grow(d, date(y, 1, 1)) for d, a, _ in E.rung_flows(C.I[y], C.FEEW))
        share[str(y)] = {"units": units, "pays_zero": paid0, "pays_zero_and_bill_fee_to_payment": paidf,
                         "cost": x_by_year.get(y, 0.0) * paid0}
    res["cost_share_x_payout"] = share
    res["cost_total"] = sum(v["cost"] for v in share.values())
    for w, world in WORLDS.items():
        base_paid, _, _, base_left = C.ledger(world, OWN, POOL)
        paid, _, carry, left = C.ledger(world, OWN, POOL, ins)
        res[w] = {"short_by_year": {str(y): E.PAYMENT - paid[y] for y in E.YEARS if E.PAYMENT - paid[y] > 0.005},
                  "short_total": sum(E.PAYMENT - v for v in paid.values()), "left_after_2042": left,
                  "left_after_2042_without_the_cost": base_left}
    print("B. %s: cost share x payout $%.2f; zero interest: short $%.2f, left $%.2f (was $%.2f); zero + bill fee: short $%.2f %s; forwards: left $%.2f (was $%.2f)"
          % (label, res["cost_total"], res["zero"]["short_total"], res["zero"]["left_after_2042"],
             res["zero"]["left_after_2042_without_the_cost"], res["zero_and_bill_fee"]["short_total"],
             {k: round(v, 2) for k, v in res["zero_and_bill_fee"]["short_by_year"].items()},
             res["forwards"]["left_after_2042"], res["forwards"]["left_after_2042_without_the_cost"]))
    return res


years_to_end = {y: E.yf(C.I[y].end, E.J27) for y in FUND_YEARS}
Bx = {
    "0.1pct": exposure({y: 0.001 for y in FUND_YEARS}, "0.1% off every fund flow"),
    "0.5pct": exposure({y: 0.005 for y in FUND_YEARS}, "0.5% (the range's share)"),
    "0.03pt_a_year": exposure({y: 0.0003 * years_to_end[y] for y in FUND_YEARS}, "0.03 points a year to each fund's end"),
}
Bx["years_to_end_from_1jan2027"] = {str(y): v for y, v in years_to_end.items()}
# the largest flat cost the $1,414 spare at zero interest (no bill fee) covers: solve by bisection
lo, hi = 0.0, 0.02
for _ in range(60):
    mid = (lo + hi) / 2
    paid = C.ledger(C.ZERO, OWN, POOL, insts_less({y: mid for y in FUND_YEARS}))[0]
    if sum(E.PAYMENT - v for v in paid.values()) > 0.005:
        hi = mid
    else:
        lo = mid
Bx["largest_flat_cost_covered_zero_interest_no_bill_fee"] = lo
Bx["five_funds_pay_zero"] = sum(v["pays_zero"] for v in Bx["0.5pct"]["cost_share_x_payout"].values())
print("   largest cost off every fund flow that zero interest (no bill fee) still covers: %.4f%%; five funds pay $%.2f at zero"
      % (100 * lo, Bx["five_funds_pay_zero"]))
# the lowest flat yearly rate on every waiting dollar (and the funds' own cash), after the bill fund's 0.15%, at which
# all ten are still paid with each cost: how much interest the cost needs
for key, xb in (("0.1pct", {y: 0.001 for y in FUND_YEARS}), ("0.5pct", {y: 0.005 for y in FUND_YEARS}),
                ("0.03pt_a_year", {y: 0.0003 * years_to_end[y] for y in FUND_YEARS})):
    ins = insts_less(xb)
    lo, hi = -C.WAIT_FEE, 0.02
    for _ in range(60):
        mid = (lo + hi) / 2
        paid = C.ledger(C.Flat(c, mid), OWN, POOL, ins)[0]
        if sum(E.PAYMENT - v for v in paid.values()) > 0.005:
            lo = mid
        else:
            hi = mid
    Bx[key]["flat_net_rate_needed"] = hi
    Bx[key]["flat_gross_rate_needed_before_bill_fee"] = hi + C.WAIT_FEE
    print("   %s: all ten paid if waiting money earns at least %.4f%% a year net (%.4f%% before the bill fund's 0.15%%)"
          % (key, 100 * hi, 100 * (hi + C.WAIT_FEE)))
out["B_payments_exposure"] = Bx

# ================================================================ Part C: a trade-day limit


def legs(p, res, sF_=0.0, sM_=0.0):
    """The two range legs filled p off net asset value against Laura: the floor buys 1/(1+p) of NAV; the move sells VT at
    1-p and buys the fund at 1+p. Returns the stated ends with and without."""
    base = C.rule(res, sF_, sM_)
    r2 = dict(res)
    r2["floor_money"] = np.asarray(res["floor_money"], float) / (1 + p)
    r2["moved_money"] = np.asarray(res["moved_money"], float) * (1 - p) / (1 + p)
    alt = C.rule(r2, sF_, sM_)
    return base, alt


Cx = {"note": "every fund leg filled p off net asset value against Laura; stated ends worked out after the trade on units "
              "x net asset value (NUMBERS 0), so ownership holds by construction and only the stated figures can fall"}
fund27 = sum(C.PLAIN[y] * C.I[y].price for y in FUND_YEARS)                  # five funds bought 1 Jan 2027 (1 Jan 2027 money)
f01 = c.fwd(E.J27, E.J28)
tail28 = 2286.0                                                              # the top-up's IBTM at net asset value (8a)
# the backstop's IBTQ and IBTR bought in January 2028: their net asset value then, i.e. their flows after 1 Jan 2028
# discounted at today's forwards (their 2027 flows are cash the deposit adds, not fund shares, so no premium on them)
extra_funds28 = 0.0
for y in (2036, 2037):
    u = C.BACKSTOP.get(y, 0.0)
    for d, a, _ in E.rung_flows(C.I[y], C.BASE):
        if d > E.J28:
            extra_funds28 += u * a * math.exp(-c.fwd(E.J28, d) * E.yf(d, E.J28))
for p in (0.0025, 0.005, 0.0074, 0.01):
    extra28 = (fund27 * p * math.exp(f01)) + (tail28 + extra_funds28) * p    # more top-up in January 2028 money
    mfp = (lambda e: (lambda a, b: MF(a, b) + e))(extra28)
    cp = P.run(c, margin=MARGIN, margin_fn=mfp)                              # the 2027 and 2028 Treasury legs
    cp2 = dict(cp)
    cp2["floor_money"] = np.asarray(cp["floor_money"], float) / (1 + p)
    cp2["moved_money"] = np.asarray(cp["moved_money"], float) * (1 - p) / (1 + p)
    ra = C.rule(cp2)
    floor_only = legs(p, cen)[1]
    hb, ha = legs(p, H, sF, sM)
    row = {
        "extra_top_up_jan2028": extra28,
        "central_all_legs": {"bottom_raw": f(ra["bottom_raw"]), "top_raw": f(ra["top_raw"]), "bottom": f(ra["bottom"]),
                             "top": f(ra["top"]), "bottom_raw_change": f(ra["bottom_raw"]) - b_raw,
                             "top_raw_change": f(ra["top_raw"]) - t_raw, "floor_money": f(cp["floor_money"])},
        "central_range_legs_only": {"bottom_raw_change": f(floor_only["bottom_raw"]) - b_raw,
                                    "top_raw_change": f(floor_only["top_raw"]) - t_raw},
        "house_range_legs_only": {
            "bottom_steps_down": float((ha["bottom"] < hb["bottom"]).mean()),
            "top_steps_down": float((ha["top"] < hb["top"]).mean()),
            "either_steps_down": float(((ha["bottom"] < hb["bottom"]) | (ha["top"] < hb["top"])).mean()),
            "bottom_1in20_median_1in20": [C.qs(hb["bottom"]), C.qs(ha["bottom"])],
            "top_1in20_median_1in20": [C.qs(hb["top"]), C.qs(ha["top"])],
        },
    }
    Cx[f"{p:.4f}"] = row
    print("C. p %.2f%%: extra top-up $%.0f; central all legs: bottom raw %+.0f -> %.0f stated %.0f; top raw %+.0f -> %.0f stated %.0f;"
          " range legs only: bottom %+.0f top %+.0f; house (range legs): bottom steps down %.1f%%, top %.1f%%, either %.1f%%"
          % (100 * p, extra28, row["central_all_legs"]["bottom_raw_change"], row["central_all_legs"]["bottom_raw"],
             row["central_all_legs"]["bottom"], row["central_all_legs"]["top_raw_change"], row["central_all_legs"]["top_raw"],
             row["central_all_legs"]["top"], row["central_range_legs_only"]["bottom_raw_change"],
             row["central_range_legs_only"]["top_raw_change"], 100 * row["house_range_legs_only"]["bottom_steps_down"],
             100 * row["house_range_legs_only"]["top_steps_down"], 100 * row["house_range_legs_only"]["either_steps_down"]))
Cx["inputs"] = {"five_funds_cost_1jan2027": fund27, "fwd_2027": f01, "top_up_ibtm_nav_jan2028": tail28,
                "backstop_ibtq_ibtr_jan2028": extra_funds28}
out["C_trade_day_limit"] = Cx

OUT.write_text(json.dumps(out, indent=1, default=float))
print("wrote", OUT.name)
