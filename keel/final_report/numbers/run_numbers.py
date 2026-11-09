"""Every figure in keel/final_report/NUMBERS.md sections 1-5, from one curve and one engine (Keel). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/run_numbers.py [--design KEEL]
Writes keel/final_report/numbers/results_2026-11-10.json (results_2026-11-10_KEEL.json for the alternative) and prints
the register's figures (about a minute).

Tue 10 Nov 2026: the completion standard and the range rule come from completion.py (the call: H_plain, "sufficient
without reinvestment"; the 2031 range rule of card Q19). The Mon 9 Nov file results_2026-11-06.json is kept as it was.
Tue 10 Nov afternoon (bond desk check): the backstop carries the ETF's fee on all waiting money; the stated ends come from
the fund's holdings less a 0.5% haircut, tested against holdings the rule does not assume; the floor takes at least just
over half the 2028 deposit (Keel's reading of "most"); section 5 adds falls during 2027.
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E       # noqa: E402
import plan as P         # noqa: E402
import completion as C   # noqa: E402

NAME = C.design_arg()
out = {}
c = C.c
I = C.I
base, zero = C.BASE, C.ZERO
shift = lambda s: E.Reinvest(c, "shift", s)
DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"
f01 = c.fwd(E.J27, E.J28)

# ---------------------------------------------------------------- C3: the ladder's cost on the 6 Nov close (unchanged)
units = C.PLAIN
out["C3"] = {
    "curve_cost_payment_dates": E.ladder_cost(c),
    "ten_instruments_with_fund_fees": E.cost(I, units),
    "ladder_duration_years": P.setup(c)["dur_l"],
    "dv01_per_bp": (E.ladder_cost(E.Curve(c.par, -0.0001)) - E.ladder_cost(E.Curve(c.par, 0.0001))) / 2,
    "rungs": {y: {"instrument": I[y].name, "units": units[y], "cost": units[y] * I[y].price} for y in E.YEARS},
}
for fall in (0.0025, 0.005, 0.01, 0.02):
    out["C3"][f"cost_if_yields_fall_{int(fall*1e4)}bp_before_jan2027"] = C.shifted(-fall)["plain_cost"]

# ---------------------------------------------------------------- C1: reinvestment, every design on one table
designs = {}
for lab, w in [("forward", base), ("minus1", shift(0.01)), ("minus2", shift(0.02)), ("minus3", shift(0.03)),
               ("zero", zero)]:
    designs[f"A_{lab}"] = (E.size_own_rung(I, w), None)
designs["B_matched_forward"] = (None, E.size_matched(I, base))
designs["B_matched_zero"] = (None, E.size_matched(I, zero))
designs["H_plain"] = (C.PLAIN, C.BACKSTOP)
designs["H_plain_0"] = (C.PLAIN, C.design("H_plain_0")["pool"])
c1 = {}
hist = {k: [] for k in designs}
starts = []
for st, m in E.history_windows(DGS1, "DGS1"):
    w = E.Reinvest(c, "hist", mult=m)
    starts.append(st)
    for k, (own, pool) in designs.items():
        hist[k].append(C.short(w, own, pool))
for k, (own, pool) in designs.items():
    h = np.array(hist[k])
    allu = C.add(own, pool)
    c1[k] = {
        "cost": C.cost(allu),
        "units_bought_in_jan_2027": sum(1 for y in E.YEARS if (own or pool)[y] > 1),
        "short_if_rates_fall_for_good": {f"{s}pt": C.short(shift(s / 100), own, pool) for s in (1, 2, 3)},
        "short_if_interest_earns_nothing": C.short(zero, own, pool),
        "short_if_waiting_money_pays_0.15pct_a_year": C.short(C.FEEW, own, pool),
        "left_after_2042_if_interest_earns_nothing": C.ledger(zero, own, pool)[3],
        "history_windows": len(h),
        "history_share_with_any_shortfall": float((h > 1).mean()),
        "history_windows_short": int((h > 1).sum()),
        "history_median_shortfall": float(np.median(h)),
        "history_1_in_20_shortfall": float(np.percentile(h, 95)),
        "history_worst_shortfall": float(h.max()),
        "history_worst_start": starts[int(h.argmax())],
    }
c1["history_first_start"], c1["history_last_start"] = starts[0], starts[-1]
pre = sum(units[y] * a * base.grow(d, E.J33) for y in E.YEARS for d, a, k in E.rung_flows(I[y], base)
          if d < E.J33 and k == "coupon")
c1["interest_received_before_2033_valued_jan_2033"] = pre
c1["H_plain_backstop"] = {
    "units": {y: u for y, u in C.BACKSTOP.items() if u > 0.5},
    "cost_jan2027": {y: u * I[y].price for y, u in C.BACKSTOP.items() if u > 0.5},
    "total_jan2027": C.cost(C.BACKSTOP),
    "zero_ledger": {},
}
paid, avail, carry, left = C.ledger(zero, C.PLAIN, C.BACKSTOP)
oz = C.own_amounts(C.PLAIN, zero)
pz = C.pool_buckets(C.BACKSTOP, zero)
for y in E.YEARS:
    c1["H_plain_backstop"]["zero_ledger"][y] = {"own_rung_at_zero": oz[y], "backstop_cash_due": pz[y],
                                                "available": avail[y], "paid": paid[y], "carried": carry[y]}
c1["H_plain_backstop"]["zero_ledger_left_after_2042"] = left
c1["H_plain_backstop"]["fee_ledger"] = {}
paid, avail, carry, left = C.ledger(C.FEEW, C.PLAIN, C.BACKSTOP)
of = C.own_amounts(C.PLAIN, C.FEEW)
pf = C.pool_buckets(C.BACKSTOP, C.FEEW)
for y in E.YEARS:
    c1["H_plain_backstop"]["fee_ledger"][y] = {"own_rung": of[y], "backstop_cash_due": pf[y], "available": avail[y],
                                               "paid": paid[y], "carried": carry[y]}
c1["H_plain_backstop"]["fee_ledger_left_after_2042"] = left
c1["H_plain_backstop"]["wait_fee_a_year"] = C.WAIT_FEE
c1["H_plain_backstop"]["cost_of_the_fee_cushion"] = C.design("H_plain")["margin"] - C.design("H_plain_0")["margin"]
c1["H_plain_backstop"]["morning_backstop_units"] = {y: u for y, u in C.design("H_plain_0")["pool"].items() if u > 0.5}
# the IBTM tail bought in Jan 2028 misses its 2027 distributions; the completion money above its Jan 2028 price covers them
_tail = C.PLAIN_COST - 300_000
_tu = _tail / I[2033].price
c1["H_plain_backstop"]["ibtm_tail"] = {
    "tail_jan2027": _tail, "units": _tu,
    "distributions_2027_missed": sum(_tu * a for d, a, _ in I[2033].flows if d <= E.J28),
    "completion_money_for_tail_jan2028": _tail * math.exp(f01),
    "tail_price_jan2028": sum(_tu * a * c.P(d) / c.P(E.J28) for d, a, _ in I[2033].flows if d > E.J28)}
out["C1"] = c1

# ---------------------------------------------------------------- C2: an iBond fund pays its net asset value (unchanged)
c2 = {}
for y in range(2033, 2038):
    inst = I[y]
    u = units[y]
    fee_free = sum(u * a / (1 - E.ASSUMPTIONS["fund_fee"]) ** E.yf(d, E.J27) * base.grow(d, date(y, 1, 1))
                   for d, a, _ in inst.flows)
    with_fee = sum(u * a * base.grow(d, date(y, 1, 1)) for d, a, _ in inst.flows)
    wam, end = inst.cash_wait
    principal = [a for d, a, k in inst.flows if k != "coupon"][0] * u
    c2[inst.name] = {"fee_cost_on_50k": fee_free - with_fee, "months_in_cash_before_end": (end - wam).days / 365.25 * 12,
                     "lost_if_cash_earns_nothing_in_final_months": principal * (base.grow(wam, end) - 1),
                     "as_share_of_payment": principal * (base.grow(wam, end) - 1) / E.PAYMENT}
out["C2"] = c2

# ---------------------------------------------------------------- section 3: the rule on the fund's holdings
_tF, _fFc = E.yf(date(2032, 12, 15), E.J28), c.fwd(E.J28, date(2032, 12, 15))
_tM, _fMc = E.yf(date(2032, 12, 15), E.J31), c.fwd(E.J31, date(2032, 12, 15))
_fee = E.ASSUMPTIONS["fund_fee"]


def _equiv(buy, sh, hold="engine", haircut=C.HAIRCUT):
    """The rule's cut as a share of the payout at the path's own rates (what the old fixed 4.1% / 2.5% meant)."""
    tau, f = (_tF, _fFc) if buy == E.J28 else (_tM, _fMc)
    fwdpay = math.exp(max(f + sh, 0.001) * tau) * (1 - _fee) ** tau
    return 1 - float(C.zero_per_dollar(buy, sh, 1.0, hold)) * (1 - haircut) / fwdpay


out["deductions"] = {
    "haircut": C.HAIRCUT, "engine_ibtm_coupon": C.HOLD_COUPON,
    "zero_payout_per_dollar_today": {"floor_jan2028": float(C.zero_per_dollar(E.J28)),
                                     "moved_jan2031": float(C.zero_per_dollar(E.J31))},
    "cut_today_with_haircut": {"floor": _equiv(E.J28, 0.0), "moved": _equiv(E.J31, 0.0)},
    "cut_today_before_haircut": {"floor": _equiv(E.J28, 0.0, haircut=0.0), "moved": _equiv(E.J31, 0.0, haircut=0.0)},
    "by_shift_with_haircut": {f"{x*100:+.0f}pt": {"floor": _equiv(E.J28, x), "moved": _equiv(E.J31, x)}
                              for x in (-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03)},
    "par_stand_in_morning": {"floor_today": float(C.ded_floor(0.0)), "moved_today": float(C.ded_moved(0.0)),
                             "by_shift": {f"{x*100:+.0f}pt": {"floor": float(C.ded_floor(x)), "moved": float(C.ded_moved(x))}
                                          for x in (-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03)}},
    "holdings_vs_engine_zero_payout_pct": {f"{x*100:+.0f}pt": {h: 100 * (float(C.zero_per_dollar(E.J28, x, 1.0, h))
                                                                           / float(C.zero_per_dollar(E.J28, x)) - 1)
                                                                for h in ("coupon_3.50", "coupon_4.00")}
                                           for x in (-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03)},
    "minus3_from_purchase": {"floor": C.losses(c, E.J28)["minus3"], "moved": C.losses(c, E.J31)["minus3"]},
    "shift_where_par_floor_loss_reaches_4.1pct_pt": float(np.interp(0.041, C.GF, C.GRID) * 100),
}

# ---------------------------------------------------------------- section 4: the plan from 2028, with the rule
KEYS = ("complete", "R", "floor", "vt28", "vt31", "moved", "top", "kept33", "total", "all_t")


def ruled(res, sF, sM):
    r = C.rule(res, sF, sM)
    r["kept_plus_excess"] = res["kept33"] + r["excess"]
    return r


def pq(a, qs=(5, 50, 95)):
    return [float(np.percentile(np.asarray(a, float), q)) for q in qs]


def plan_block(name):
    """Central, house and history for one design, with the Q19 rule (deductions at each path's purchase yields)."""
    mf = C.margin_fn(name) if name != "no_margin" else None
    d = P.run(c, margin_fn=mf)
    r = ruled(d, 0.0, 0.0)
    h = P.house(c, margin_fn=mf)
    d0, d1, d2, _, _ = h["draws"]
    rh = ruled(h, d0 + d1, d0 + d1 + d2)
    hs = P.history(c, margin_fn=mf)
    rs = ruled(hs, 0.0, 0.0)
    lo = int(np.argmin(rs["top"]))
    blk = {
        "margin_jan2027_value": C.design(name)["margin"] if name != "no_margin" else 0.0,
        "central": {k: float(d[k]) for k in KEYS},
        "central_rule": {k: float(np.asarray(r[k]).item()) for k in ("dF", "dM", "bottom_raw", "bottom", "top_raw", "top",
                                                                     "payout", "gift", "excess", "kept_plus_excess")},
        "floor_money_jan2028": float(d["floor_money"]),
        "floor_share_of_2028_deposit": float(d["floor_money"] / 150_000),
        "most_rule_house": {
            "share_paths_binding": float(h["most_binds"].mean()),
            "vt_squeeze_where_binding_p50_p95_max": pq(h["vt_squeeze"][h["most_binds"]], (50, 95, 100))
            if h["most_binds"].any() else [0, 0, 0],
            "vt_bought_where_binding_p5_p50": pq(h["vt28"][h["most_binds"]], (5, 50)) if h["most_binds"].any() else [0, 0],
            "vt_share_of_left_where_binding_p5_p50": pq((h["vt28"] / np.maximum(h["R"], 1))[h["most_binds"]], (5, 50))
            if h["most_binds"].any() else [0, 0],
            "floor_money_p5_p50_p95": pq(h["floor_money"]),
            "floor_money_without_rule_p5_p50_p95": pq(E.ASSUMPTIONS["floor_share"] * h["R"]),
            "share_floor_money_under_75k_without_rule": float((E.ASSUMPTIONS["floor_share"] * h["R"] < 75_000).mean()),
            "completion_above_which_rule_binds": 150_000 - 75_001 / E.ASSUMPTIONS["floor_share"],
        },
        "owned_test_house": C.owned_summary(C.owned_test(h, rh, d0 + d1, d0 + d1 + d2)),
        "owned_test_history": C.owned_summary(C.owned_test(hs, rs)),
        "house": {k: pq(h[k]) for k in ("complete", "R", "floor", "vt28", "vt31", "moved", "top", "kept33", "total", "all_t")},
        "house_rule": dict({k: pq(rh[k]) for k in ("bottom_raw", "top_raw", "gift", "excess", "kept_plus_excess", "dF", "dM")},
                           **{k: C.qs(rh[k]) for k in ("bottom", "top")}),
        "house_rule_extra": {
            "share_gift_equals_stated_top": float((np.abs(rh["gift"] - rh["top"]) < 1e-6).mean()),
            "share_payout_below_stated_top": float((rh["payout"] < rh["top"] - 1e-6).mean()),
            "share_zero_world_below_stated_top": float((rh["zero_world"] < rh["top"] - 1e-6).mean()),
            "share_floor_zero_below_stated_bottom": float((rh["floor_zero"] < rh["bottom"] - 1e-6).mean()),
            "P_stated_bottom_at_least": {f"{t//1000}k": float((rh["bottom"] >= t).mean()) for t in
                                         (80_000, 90_000, 95_000, 100_000, 110_000, 120_000)},
            "P_stated_top_at_least": {f"{t//1000}k": float((rh["top"] >= t).mean()) for t in
                                      (90_000, 100_000, 110_000, 115_000, 120_000, 130_000, 140_000, 150_000)},
            "share_total_below_all_treasury": float((h["total"] < h["all_t"]).mean()),
            "share_payout_below_all_treasury": float((h["top"] < h["all_t"]).mean()),
            "fixed_4.1_2.5": {
                "share_zero_world_below_fixed_top": float((rh["zero_world"] <
                                                           C.down(h["floor"] * 0.959 + h["moved"] * 0.975) - 1e-6).mean()),
                "share_floor_zero_below_fixed_bottom": float((rh["floor_zero"] < C.down(h["floor"] * 0.959) - 1e-6).mean()),
            },
        },
        "history": {k: pq(hs[k]) for k in ("floor", "moved", "top", "kept33", "total")},
        "history_rule": dict({k: pq(rs[k]) for k in ("top_raw", "gift", "excess", "kept_plus_excess")},
                             **{k: C.qs(rs[k]) for k in ("bottom", "top")}),
        "history_lowest_stated_top": [float(rs["top"][lo]), float(rs["top_raw"][lo]), hs["starts"][lo]],
        "history_lowest_payout": [float(hs["top"].min()), hs["starts"][int(hs["top"].argmin())]],
        "history_windows": len(hs["starts"]),
    }
    return blk, d, h, rh


plans = {}
for lab in ("no_margin", "KEEL", "H_plain"):
    plans[lab], dd, hh, rr = plan_block(lab)
    if lab == NAME:
        D_CALL, H_CALL, RH_CALL = dd, hh, rr
mf = C.margin_fn(NAME)
sens = {}
for g in (0.04, 0.06, 0.075, 0.09, 0.10):
    d = P.run(c, vt3=(1 + g) ** 3, vt2=(1 + g) ** 2, margin_fn=mf)
    r = ruled(d, 0.0, 0.0)
    sens[f"{g:.3f}"] = {"payout": float(d["top"]), "stated_top_raw": float(r["top_raw"]), "stated_top": float(r["top"]),
                        "gift": float(r["gift"]), "excess": float(r["excess"]), "kept33": float(d["kept33"]),
                        "kept_plus_excess": float(r["kept_plus_excess"]), "total": float(d["total"])}
plans["vt_growth_sensitivity_central"] = sens
dz = P.run(c, vt3=0.0, vt2=0.0, margin_fn=mf)
rz = ruled(dz, 0.0, 0.0)
plans["deletion_test_vt_to_zero"] = {"floor_payout": float(dz["floor"]), "stated_bottom": float(rz["bottom"]),
                                     "stated_top": float(rz["top"]), "gift": float(rz["gift"]),
                                     "excess_kept_by_laura": float(rz["excess"])}
# the floor's expected interest (payout less the money put in), against the VT bought
dc = plans[NAME]
plans["floor_expected_interest"] = dc["central"]["floor"] - dc["floor_money_jan2028"]
# what comes back if rates follow today's forwards: everything above the ten payments, carried to 1 Jan 2042
own, pool = C.design(NAME)["own"], C.design(NAME)["pool"]
_, _, carry_b, left_b = C.ledger(base, own, pool)
plans["overflow_if_forwards_hold"] = {
    "left_after_2042_nominal": left_b, "value_jan2027": left_b * c.P(date(2042, 1, 1)),
    "value_jan2033": left_b * c.P(date(2042, 1, 1)) / c.P(E.J33),
    "carry_after_each_payment": carry_b,
}
plans["missed_deposit_2033_payment_short"] = (C.PLAIN_COST - 300_000) / c.P(E.J33)
# all-Treasury benchmark on the same completion (C8)
F_all = dc["central"]["all_t"]
z0 = float(C.zero_per_dollar(E.J28)) * (1 - C.HAIRCUT)
R0 = dc["central"]["R"]
med_kept = float(np.median(H_CALL["kept33"]))
grow0 = F_all / R0
_hz = C.zero_per_dollar(E.J28, H_CALL["draws"][0] + H_CALL["draws"][1]) * (1 - C.HAIRCUT)
plans["all_treasury"] = {
    "payout_central": F_all, "stated_zero_interest_central": R0 * z0,
    "stated_rounded": float(C.down(R0 * z0)), "house": pq(H_CALL["all_t"]),
    "same_flexibility_payout": F_all - med_kept,
    "same_flexibility_stated": float(C.down((F_all - med_kept) / grow0 * z0)),
    "final_median_kept_half": med_kept,
    "share_final_stated_top_below_all_t_stated": float((RH_CALL["top"] < C.down(H_CALL["R"] * _hz)).mean()),
    "share_final_payout_below_all_t": float((H_CALL["top"] < H_CALL["all_t"]).mean()),
    "share_final_total_above_all_t": float((H_CALL["total"] > H_CALL["all_t"]).mean()),
}
out["plan"] = plans
out["C5"] = {"move_date_modelled": "1 Jan 2031", "rule": "card Q19, completion.rule", "design": NAME}

# ---------------------------------------------------------------- C6 (section 5): a smaller or missed 2028 deposit
c6 = {}
share = E.ASSUMPTIONS["floor_share"]
fee = E.ASSUMPTIONS["fund_fee"]
tauF = E.yf(date(2032, 12, 15), E.J28)
for fall in (0.0, 0.0025, 0.005, 0.01, 0.02):
    need_l, b, cc = C.completion_exact(-fall, "plain")
    need_h, _, _ = C.completion_exact(-fall, NAME)
    fF = cc.fwd(E.J28, date(2032, 12, 15))
    row = {"ladder_only": need_l, "with_standard": need_h,
           "deposit_fall_that_breaks_ladder_pct": 100 * (1 - max(need_l, 0) / 150_000),
           "deposit_fall_that_breaks_standard_pct": 100 * (1 - max(need_h, 0) / 150_000)}
    for dep in (150_000, 112_500, 75_000, 37_500):
        R = max(dep - need_h, 0.0) if need_h > 0 else dep - need_h
        fm = max(share * R, min(R, dep / 2 + 1.0))          # Keel's reading of "most" (plan.run, most=True)
        fl = fm * math.exp(fF * tauF) * (1 - fee) ** tauF
        braw = fm * float(C.zero_per_dollar(E.J28, -fall)) * (1 - C.HAIRCUT)
        row[str(dep)] = {"left": R, "floor_money": fm, "most_binds": bool(fm > share * R + 1e-6), "vt_bought": R - fm,
                         "floor_payout": fl, "stated_bottom_raw": braw, "stated_bottom": float(C.down(braw)),
                         "standard_complete": bool(dep >= need_h), "ladder_complete": bool(dep >= need_l)}
    c6[f"fall_{int(fall*1e4)}bp"] = row
# a missed deposit: the plain ladder's tail unbought (2033 rung short at forwards), no backstop
tail = C.PLAIN_COST - 300_000
plain_less_tail = dict(C.PLAIN)
plain_less_tail[2033] = C.PLAIN[2033] - tail / I[2033].price
c6["missed"] = {"tail_unbought_jan2027": tail,
                "short_at_forwards": C.short(base, plain_less_tail),
                "short_at_forwards_by_payment": {y: E.PAYMENT - v for y, v in C.ledger(base, plain_less_tail)[0].items()},
                "short_at_zero": C.short(zero, plain_less_tail),
                "history_windows_short": int(sum(C.short(E.Reinvest(c, "hist", mult=m), plain_less_tail) > 1
                                                 for _, m in E.history_windows(DGS1, "DGS1")))}
# a deposit between the ladder's tail and the full standard: ladder complete, backstop part-bought, nothing for the
# building; what it still pays at zero interest if the backstop is bought pro rata
for dep in (10_000, 20_000, 30_000):
    frac = max(min((dep - max(C.completion_exact(0.0, "plain")[0], 0)) / (C.design(NAME)["margin"] * math.exp(f01)), 1.0), 0.0) \
        if NAME == "H_plain" else 0.0
    pool_part = {y: u * frac for y, u in C.BACKSTOP.items()} if NAME == "H_plain" else None
    c6[f"partial_{dep}"] = {"backstop_share_bought": frac, "short_at_zero": C.short(zero, C.PLAIN, pool_part)}
# a fall DURING 2027, after the ten are bought (bond desk check, finding 10): the tail and the backstop are repriced
_mf = C.margin_fn(NAME)
for fall in (0.005, 0.01, 0.02):
    rr = P.run(c, d1=-fall, margin_fn=_mf)
    c6[f"fall_during_2027_{int(fall*1e4)}bp"] = {"completion_jan2028": float(rr["complete"]),
                                                 "deposit_fall_that_breaks_standard_pct": 100 * (1 - float(rr["complete"]) / 150_000)}
out["C6"] = c6
out["stamp"] = {"curve": "US Treasury par yield curve, 6 Nov 2026 close", "valuation": "forward to 1 Jan 2027",
                "design": NAME, "decided": C.DECIDED, "run": C.RUN,
                "assumptions": {k: v for k, v in E.ASSUMPTIONS.items()}}

(HERE / f"results_2026-11-10{C.tag(NAME)}.json").write_text(json.dumps(out, indent=1, default=str))

# ---------------------------------------------------------------- print
k = C.fmt
print("design", NAME, "| C3", k(out["C3"]["curve_cost_payment_dates"]), k(out["C3"]["ten_instruments_with_fund_fees"]),
      {kk: round(v) for kk, v in out["C3"].items() if kk.startswith("cost_if")})
for kk, v in c1.items():
    if isinstance(v, dict) and "cost" in v:
        print(f"C1 {kk:18s} cost {k(v['cost'])} bought {v['units_bought_in_jan_2027']} | -1/-2/-3 "
              f"{[round(x) for x in v['short_if_rates_fall_for_good'].values()]} zero {k(v['short_if_interest_earns_nothing'])} | "
              f"hist {v['history_share_with_any_shortfall']:.1%} ({v['history_windows_short']}) med {k(v['history_median_shortfall'])} "
              f"1in20 {k(v['history_1_in_20_shortfall'])} worst {k(v['history_worst_shortfall'])} ({v['history_worst_start']})")
print("backstop", {y: round(u) for y, u in c1["H_plain_backstop"]["units"].items()}, k(c1["H_plain_backstop"]["total_jan2027"]))
for y, v in c1["H_plain_backstop"]["zero_ledger"].items():
    print("  zero ledger", y, {a: round(b) for a, b in v.items()})
print("deductions", json.dumps(out["deductions"], indent=None))
for lab in ("no_margin", "KEEL", "H_plain"):
    v = plans[lab]
    print(f"\nPLAN {lab}: margin {k(v['margin_jan2027_value'])} central", {a: round(b) for a, b in v["central"].items()})
    print("  rule", {a: (round(b, 4) if abs(b) < 1 else round(b)) for a, b in v["central_rule"].items()},
          "floor money", k(v["floor_money_jan2028"]), f"share {v['floor_share_of_2028_deposit']:.1%}")
    print("  house", {a: [round(x) for x in b] for a, b in v["house"].items()})
    print("  house rule", {a: [round(x, 4) if abs(x) < 1 else round(x) for x in b] for a, b in v["house_rule"].items()})
    print("  house extra", json.dumps(v["house_rule_extra"]))
    print("  history", {a: [round(x) for x in b] for a, b in v["history"].items()},
          {a: [round(x) for x in b] for a, b in v["history_rule"].items()}, "lowest stated top", v["history_lowest_stated_top"],
          "lowest payout", v["history_lowest_payout"])
print("\nsensitivity", {g: {a: round(b) for a, b in v.items()} for g, v in sens.items()})
print("deletion", {a: round(b) for a, b in plans["deletion_test_vt_to_zero"].items()},
      "floor expected interest", k(plans["floor_expected_interest"]))
print("overflow", {a: (round(b) if not isinstance(b, dict) else {y: round(x) for y, x in b.items()})
                   for a, b in plans["overflow_if_forwards_hold"].items()})
print("all-Treasury", {a: (round(b, 4) if isinstance(b, float) and b < 1 else ([round(x) for x in b] if isinstance(b, list) else round(b)))
                       for a, b in plans["all_treasury"].items()})
for kk, v in c6.items():
    print("C6", kk, json.dumps(v, default=lambda o: round(o) if isinstance(o, float) else o)[:600])
