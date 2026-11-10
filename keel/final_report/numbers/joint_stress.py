"""Joint stress of rates and shares on Caplet's FINAL plan with Keel's call (Keel, Tue 10 Nov 2026). MODEL.

Run:  cd keel/final_report/numbers && python3 -I joint_stress.py [--design KEEL]
Writes results_joint_stress_2026-11-10.json and prints the figures (about 30 seconds). The Tue 10 Nov morning run's
results_joint_stress.json (Keel's margin, fixed 4.1% and 2.5% deductions) is kept as it was.

Tue 10 Nov re-run: the completion is the call in completion.py (H_plain, "sufficient without reinvestment": the ten
as written plus a pooled backstop); the stated ends follow the range rule of card Q19 (completion.rule: each end's
payout if no more interest is earned, at its own purchase yield, rounded down to $5,000; the 2033 contribution is the
lower of what the funds pay and the stated top, the excess joins the half kept). Overflow is now the money left after
the 2042 payment, valued on 1 Jan 2033 on the 6 Nov forwards. The method notes below describe the first run.

Tue 10 Nov afternoon (bond desk check, findings 1, 2, 5): the stated ends are completion.rule on the fund's own
holdings (zero-interest payout per $1 on the trade day, less 0.5%, rounded down), at proportional moves (m28, m31) in
the windows and at parallel moves in the scenario worlds, where the realised payout is now priced the same way; the
floor gets the larger of 73.3% of what is left and $75,001 (plan.run, most=True); money left after 2042 is put into
1 Jan 2033 money at the world's own rates (completion.in_2033_money), not at the 6 Nov forwards; stated (rounded)
percentiles use the 'lower' method.

Tue 10 Nov evening (numbers owner, NUMBERS 8j and 8k): the Taiwan dollar test is run on the 2033 contribution after the
cap (the lower of what the funds pay and the stated top, NUMBERS 4), for the half kept alone and for the half kept plus
the excess; the real-currency test and gift_terms follow the same definitions (gift_terms on NUMBERS 8d's conventions).
New block returns_to_laura: the backstop's money left after 2042, the excess and the half kept, in 1 Jan 2033 money at
each world's own rates, at forwards and over the 585 joint windows. Its independent check is returns_check.py.

Why (panel, bond desk weakness 4): the house model draws shares and Treasury yields independently. In a recession both
often fall: the kept half (half of VT, promised to no one) shrinks, and lower reinvestment rates use up Keel's margin,
so the reserve's overflow shrinks too. This replays both from the SAME historical months.

Method (nothing here changes the register's design; every input is the register's):
  * Curve, instruments, plan: engine.py and plan.py on the 6 Nov 2026 close. Keel's call: design A sized so every rung
    pays $50,000 if every reinvestment from 2027 earns 3 points below today's forwards (margin $21,149, NUMBERS 2);
    floor bought Jan 2028 (73.3% of what is left), VT the rest, half of VT moved into Treasuries 1 Jan 2031, half kept.
  * Joint replay: one window per monthly start s from Jan 1962 to Sep 2010 (the 585 windows of NUMBERS 2). Month s is
    1 Jan 2027. Rates: the 1-year Treasury yield path (FRED DGS1, monthly averages) applied in proportion to today's
    forward rates, capped at 3x (engine.history_windows, NUMBERS 2's method). Shares: US stocks with dividends
    (Shiller monthly, the series plan.py reads) from the SAME calendar months: VT bought at s+12 (Jan 2028), half moved
    at s+48 (Jan 2031), kept half valued at s+72 (Jan 2033).
  * Purchases on the path: the floor's yield in Jan 2028 = forward x m(s+12); the moved half's yield in Jan 2031 =
    forward x m(s+48); the margin bought in Jan 2028 is re-priced at the ladder's own forward yield x m(s+12)
    (plan.run takes one parallel shift; the margin is adjusted so the ladder uses its own yield, not the floor's).
  * Payments: engine.deliver on the path (as NUMBERS 2). Overflow: each rung's money above $50,000 on its payment date,
    summed (nominal) and valued on 1 Jan 2033 on the 6 Nov forwards (as NUMBERS 8h: $36,859 nominal at forwards).
  * Stated bottom = floor payout (yield locked in Jan 2028) x 0.959, rounded down to $5,000 (NUMBERS 3).
    Stated top = floor x 0.959 + moved half x 0.975, rounded down to $5,000 (NUMBERS 4, correction under review).
    Realised floor and moved half: the fund's distributions and final cash grown on the path (checks the deductions).
  * Independent benchmark: every rate window paired with every share window (585 x 585), the same marginals with the
    link between them removed; and the house model (plan.house, 200,000 paths, seed 2033), which draws them apart.
  * Inflation world: yields rise 3 points in a straight line over 2027-2030 and stay; shares return 0% (with
    dividends) 2028-2033; US prices 5% a year, Taiwan building costs 5% a year. Also history starts Jan 1973, Jan 1979.
  * Taiwan dollar test (bond desk): does the kept half cover the extra dollars a 10% stronger Taiwan dollar needs on
    the announced contribution (floor + moved half, CANON D12)? House, history (rates at forwards), joint replay, and
    the real Taiwan dollar from Fed H.10 monthly (keel/models/data/twd_per_usd_monthly.csv) paired with the same
    months' shares, from the meeting (Jan 2031) to the gift (Jan 2033).
"""
import csv
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402
import plan as P     # noqa: E402

DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"
SHILLER = E.ROOT / "keel/models/data/shiller_monthly.csv"
TWD = E.ROOT / "keel/models/data/twd_per_usd_monthly.csv"
END = date(2032, 12, 15)
FEE = E.ASSUMPTIONS["fund_fee"]
NAMED = ["2000-01", "2006-06", "2007-01", "2007-07", "1973-01", "1979-01", "2008-01", "1962-01", "1981-07"]

c = E.Curve(E.load_par())
I = E.instruments(c)
base = E.Reinvest(c)
minus3 = E.Reinvest(c, "shift", s=0.03)
zero = E.Reinvest(c, "zero")
import completion as C   # noqa: E402
NAME = C.design_arg()
DSG = C.design(NAME)
OWN, POOL = DSG["own"], DSG["pool"]
units = OWN
MARGIN = DSG["margin"]
S = P.setup(c)
fF, fM, tauF, tauM = S["fF"], S["fM"], S["tauF"], S["tauM"]


# ---------------------------------------------------------------- helpers
class Additive(E.Reinvest):
    """Reinvestment at today's forwards plus delta(d1) points (locked on arrival), floored at zero."""

    def __init__(self, curve, delta):
        super().__init__(curve, "base")
        self.delta = delta

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        tau = (d2 - d1).days / 365.25
        f = self.c.fwd(max(d1, E.J27), d2) + (self.delta(d1) if d1 > E.J27 else 0.0)
        return math.exp(max(f, 0.0) * tau)


def months_from_j27(d):
    return (d.year - 2027) * 12 + (d.month - 1) + (d.day - 1) / 30.44


def ladder_yield_j28():
    """Continuously compounded yield, seen from Jan 2028, of the ten payments (the margin is a slice of the ladder)."""
    ts = [E.yf(date(y, 1, 1), E.J28) for y in E.YEARS]
    pv = sum(c.P(date(y, 1, 1)) / c.P(E.J28) for y in E.YEARS)
    lo, hi = 0.0, 0.2
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if sum(math.exp(-mid * t) for t in ts) > pv else (lo, mid)
    return lo


YL = ladder_yield_j28()


def payments(world):
    paid, avail, carry, left = C.ledger(world, OWN, POOL)
    sh = sum(E.PAYMENT - v for v in paid.values())
    return {"shortfall": sh, "overflow_nominal": left,
            "overflow_jan2033_value": C.in_2033_money(left, world),
            "overflow_jan2033_value_at_6nov_forwards": left * c.P(date(2042, 1, 1)) / c.P(E.J33),
            "rungs_short": sum(1 for v in paid.values() if v < E.PAYMENT - 1)}


IBTM = I[2033]


def fund_ratio(buy, world, m_buy, s_buy=0.0):
    """Payout on 15 Dec 2032 per $1 put into the late-2032 Treasury fund on `buy`, before the fund fee: the fund's
    flows after `buy`, priced at today's forwards x m_buy + s_buy, distributions and final cash grown in `world`."""
    fl = [(d, a / (1 - FEE) ** E.yf(d, E.J27), k) for d, a, k in IBTM.flows if d > buy]
    price = sum(a * math.exp(-max(c.fwd(buy, d) * m_buy + s_buy, 0.0) * E.yf(d, buy)) for d, a, _ in fl)
    pay = sum(a * world.grow(d, END) for d, a, _ in fl)
    return pay / price


def down5k(x):
    return np.floor(np.asarray(x) / 5000.0) * 5000.0


def plan_path(m28, m31, vt3, vt2, extra_d1_ladder=None, parallel28=None):
    """plan.run with the proportional mapping: floor yield fF*m28, moved yield fM*m31. The completion beyond the tail:
    H_plain, the backstop priced exactly at today's forwards x m28 (or + parallel28 in a parallel world); KEEL, the
    margin re-priced at YL*m28 (the first run's convention). Stated ends: completion.rule at each purchase's yield move."""
    m28, m31 = np.asarray(m28, float), np.asarray(m31, float)
    d1 = fF * (m28 - 1)
    d2 = fM * m31 - fM - d1
    if NAME == "KEEL":
        dL = YL * (m28 - 1) if extra_d1_ladder is None else extra_d1_ladder
        marg = MARGIN * np.exp(-S["dur_l"] * (dL - d1))
        r = P.run(c, margin=marg, d0=0.0, d1=d1, d2=d2, vt3=vt3, vt2=vt2)
    else:
        mf = C.margin_fn(NAME) if parallel28 is not None else C.margin_fn_mult(NAME, m28)
        if parallel28 is not None:
            par = parallel28
            mf0 = mf
            mf = lambda d0, dd1: mf0(0.0, par)
        r = P.run(c, margin=MARGIN, d0=0.0, d1=d1, d2=d2, vt3=vt3, vt2=vt2, margin_fn=mf)
    rr = C.rule(r, sF=d1, sM=d1 + d2) if parallel28 is not None else C.rule(r, mF=m28, mM=m31)
    r["floor_zero"], r["zero_world"] = rr["floor_zero"], rr["zero_world"]
    r["bottom_raw"], r["top_raw"] = rr["bottom_raw"], rr["top_raw"]
    r["bottom_stated"], r["top_stated"] = rr["bottom"], rr["top"]
    return r


def shiller_index():
    """US stocks with dividends, monthly, exactly as plan.shiller_windows builds it."""
    p, dv, keys = [], [], []
    for r in csv.DictReader(open(SHILLER)):
        if r["Date"] >= "2023-07":
            break
        p.append(float(r["SP500"]))
        dv.append(float(r["Dividend"]))
        keys.append(r["Date"][:7])
    p, dv = np.array(p), np.array(dv)
    tr = (p[1:] + dv[:-1] / 12) / p[:-1]
    return keys, np.r_[1.0, np.cumprod(tr)]


def q(a, ps=(5, 50, 95)):
    a = np.asarray(a, float)
    return [float(np.percentile(a, p)) for p in ps] if a.size else None


def qs(a, ps=(5, 50, 95)):
    """Stated (rounded) figures: no interpolation between $5,000 steps."""
    return C.qs(a, ps) if np.size(a) else None


out = {"stamp": {"curve": E.CURVE_DAY, "run": C.RUN, "design": NAME, "label": DSG["label"],
                 "margin_jan2027_value": MARGIN, "ladder_yield_from_jan2028": YL, "fF": fF, "fM": fM}}

# ---------------------------------------------------------------- 0. checks against the register
cen = plan_path(1.0, 1.0, 1.075 ** 3, 1.075 ** 2)
reg = P.run(c, margin=MARGIN)
pb = payments(base)
out["checks"] = {
    "central_floor": float(cen["floor"]), "register_floor": float(reg["floor"]),
    "central_top": float(cen["top"]), "central_kept33": float(cen["kept33"]),
    "central_bottom_stated": float(cen["bottom_stated"]), "central_top_stated": float(cen["top_stated"]),
    "forwards_overflow_nominal": pb["overflow_nominal"], "forwards_overflow_jan2033": pb["overflow_jan2033_value"],
    "forwards_shortfall": pb["shortfall"],
    "floor_ratio_zero_world_vs_forwards": fund_ratio(E.J28, zero, 1.0) / fund_ratio(E.J28, base, 1.0) - 1,
    "floor_ratio_minus3_vs_forwards": fund_ratio(E.J28, Additive(c, lambda d: -0.03), 1.0)
                                      / fund_ratio(E.J28, base, 1.0) - 1,
    "moved_ratio_zero_world_vs_forwards": fund_ratio(E.J31, zero, 1.0) / fund_ratio(E.J31, base, 1.0) - 1,
    "floor_ratio_forwards_vs_plan": fund_ratio(E.J28, base, 1.0) / math.exp(fF * tauF) - 1,
}

# ---------------------------------------------------------------- 1. the joint replay
keys, idx = shiller_index()
kpos = {k: i for i, k in enumerate(keys)}
rows = []
for st, m in E.history_windows(DGS1, "DGS1"):
    i = kpos[st]
    w = E.Reinvest(c, "hist", mult=m)
    pay = payments(w)
    m28, m31 = m(E.J28), m(E.J31)
    rows.append({"start": st, "m28": m28, "m31": m31, "m33": m(E.J33),
                 "vt3": idx[i + 48] / idx[i + 12], "vt2": idx[i + 72] / idx[i + 48],
                 "stocks_first_year": idx[i + 12] / idx[i],
                 "floor_real_ratio": fund_ratio(E.J28, w, m28) / math.exp(fF * m28 * tauF),
                 "moved_real_ratio": fund_ratio(E.J31, w, m31) / math.exp(fM * m31 * tauM),
                 # Tue 10 Nov evening (NUMBERS 8k): 15 Dec 2032 money -> 1 Jan 2033 money at the window's own rates, and
                 # the ten payments' value on 1 Jan 2033 at the window's own rates (promised money, for the shares)
                 "g_end_j33": w.grow(END, E.J33),
                 "pay33": sum(E.PAYMENT / w.grow(E.J33, date(y, 1, 1)) for y in E.YEARS), **pay})
n = len(rows)
A = {k: np.array([r[k] for r in rows]) for k in rows[0] if k != "start"}
starts = [r["start"] for r in rows]
J = plan_path(A["m28"], A["m31"], A["vt3"], A["vt2"])
J["floor_realised"] = J["floor"] * A["floor_real_ratio"]
J["moved_realised"] = J["moved"] * A["moved_real_ratio"]
J["gift_realised"] = J["floor_realised"] + J["moved_realised"]
J["gift_capped"] = np.minimum(J["gift_realised"], J["top_stated"])        # the rule's cap (CANON D12)
J["excess"] = J["gift_realised"] - J["gift_capped"]


def window(i):
    return {"start": starts[i], "vt_bought": keys[kpos[starts[i]] + 12],
            "rate_ratio_jan2028": float(A["m28"][i]), "rate_ratio_jan2031": float(A["m31"][i]),
            "rate_ratio_jan2033": float(A["m33"][i]),
            "shares_2028_2031": float(A["vt3"][i]), "shares_2031_2033": float(A["vt2"][i]),
            "payments_shortfall": float(A["shortfall"][i]), "rungs_short": int(A["rungs_short"][i]),
            "overflow_nominal": float(A["overflow_nominal"][i]),
            "overflow_jan2033_value": float(A["overflow_jan2033_value"][i]),
            "completion_jan2028": float(J["complete"][i]),
            "floor_money": float(J["floor_money"][i]), "most_binds": bool(J["most_binds"][i]),
            "floor_payout": float(J["floor"][i]), "bottom_stated": float(J["bottom_stated"][i]),
            "floor_realised": float(J["floor_realised"][i]),
            "moved_half": float(J["moved"][i]), "top_stated": float(J["top_stated"][i]),
            "floor_plus_moved_model": float(J["top"][i]), "gift_realised": float(J["gift_realised"][i]),
            "bottom_raw": float(J["bottom_raw"][i]), "top_raw": float(J["top_raw"][i]),
            "gift_capped": float(J["gift_capped"][i]), "excess_to_kept_half": float(J["excess"][i]),
            "kept_plus_excess_jan2033": float(J["kept33"][i] + J["excess"][i]),
            "kept_half_jan2033": float(J["kept33"][i]),
            "kept_plus_overflow_jan2033": float(J["kept33"][i] + A["overflow_jan2033_value"][i])}


worst_kept = int(np.argmin(J["kept33"]))
worst_pay = int(np.argmax(A["shortfall"]))
worst_both = int(np.argmin(J["kept33"] + A["overflow_jan2033_value"]))
lowest_top = int(np.argmin(J["top_stated"]))
lowest_bottom = int(np.argmin(J["bottom_stated"]))
joint = {
    "windows": n, "first": starts[0], "last": starts[-1],
    "share_with_payment_shortfall": float((A["shortfall"] > 1).mean()),
    "shortfall_p50_p95_max": [float(np.median(A["shortfall"])), float(np.percentile(A["shortfall"], 95)),
                              float(A["shortfall"].max())],
    "overflow_nominal_p5_p50_p95": q(A["overflow_nominal"]),
    "overflow_jan2033_p5_p50_p95": q(A["overflow_jan2033_value"]),
    "share_overflow_under_10k_jan2033": float((A["overflow_jan2033_value"] < 10_000).mean()),
    "bottom_stated_p5_p50_p95": qs(J["bottom_stated"]), "top_stated_p5_p50_p95": qs(J["top_stated"]),
    "kept33_p1_p5_p50_p95": q(J["kept33"], (1, 5, 50, 95)),
    "kept_plus_overflow_p5_p50_p95": q(J["kept33"] + A["overflow_jan2033_value"]),
    "completion_jan2028_p5_p50_p95": q(J["complete"]),
    "most_rule": {"windows_binding": int(J["most_binds"].sum()),
                  "binding_starts": [s for s, b in zip(starts, J["most_binds"]) if b],
                  "vt_squeeze_where_binding_p50_max": ([float(np.median(J["vt_squeeze"][J["most_binds"]])),
                                                        float(J["vt_squeeze"][J["most_binds"]].max())]
                                                       if J["most_binds"].any() else [0.0, 0.0]),
                  "floor_money_p5_p50_p95": q(J["floor_money"])},
    "floor_realised_minus_bottom_stated_min": float((J["floor_realised"] - J["bottom_stated"]).min()),
    "gift_realised_minus_top_stated_min_before_cap": float((J["gift_realised"] - J["top_stated"]).min()),
    "zero_interest_floor_minus_bottom_stated_min": float((J["floor_zero"] - J["bottom_stated"]).min()),
    "zero_interest_total_minus_top_stated_min": float((J["zero_world"] - J["top_stated"]).min()),
    "gift_realised_below_bottom_stated": int((J["gift_realised"] < J["bottom_stated"] - 1).sum()),
    "floor_realised_below_bottom_stated": int((J["floor_realised"] < J["bottom_stated"] - 1).sum()),
    "gift_realised_above_top_stated_share": float((J["gift_realised"] > J["top_stated"] + 1).mean()),
    "gift_realised_minus_top_stated_p5_p50_p95": q(J["gift_realised"] - J["top_stated"]),
    "floor_realised_ratio_min": float(A["floor_real_ratio"].min()),
    "moved_realised_ratio_min": float(A["moved_real_ratio"].min()),
    "named": {s: window(starts.index(s)) for s in NAMED if s in starts},
    "worst_kept": window(worst_kept), "worst_payments": window(worst_pay),
    "worst_kept_plus_overflow": window(worst_both),
    "lowest_top_stated": window(lowest_top), "lowest_bottom_stated": window(lowest_bottom),
}
# cushions together: kept half and overflow in their own bottom fifth at once
kq = J["kept33"] <= np.percentile(J["kept33"], 20)
oq = A["overflow_jan2033_value"] <= np.percentile(A["overflow_jan2033_value"], 20)
joint["both_in_bottom_fifth"] = float((kq & oq).mean())
fell = A["vt3"] * A["vt2"] < 1.0
joint["share_vt_below_cost_2033"] = float(fell.mean())
joint["if_vt_below_cost"] = {"overflow_jan2033_median": float(np.median(A["overflow_jan2033_value"][fell])),
                             "kept_median": float(np.median(J["kept33"][fell])),
                             "share_with_payment_shortfall": float((A["shortfall"][fell] > 1).mean()),
                             "shortfall_max": float(A["shortfall"][fell].max())}
joint["if_vt_above_cost"] = {"overflow_jan2033_median": float(np.median(A["overflow_jan2033_value"][~fell])),
                             "kept_median": float(np.median(J["kept33"][~fell])),
                             "share_with_payment_shortfall": float((A["shortfall"][~fell] > 1).mean())}
low_rates = A["m31"] < 0.6
joint["if_rates_fell_40pct_by_2031"] = {"share": float(low_rates.mean()),
                                        "kept_median": float(np.median(J["kept33"][low_rates])),
                                        "overflow_jan2033_median": float(np.median(A["overflow_jan2033_value"][low_rates])),
                                        "top_stated_median": float(np.median(J["top_stated"][low_rates])),
                                        "bottom_stated_median": float(np.median(J["bottom_stated"][low_rates]))}
both = kq & oq
joint["both_in_bottom_fifth_starts"] = [s for s, b in zip(starts, both) if b]
joint["bottom_fifth_cutoffs_kept_overflow"] = [float(np.percentile(J["kept33"], 20)),
                                               float(np.percentile(A["overflow_jan2033_value"], 20))]
cush = J["kept33"] + A["overflow_jan2033_value"]
joint["kept_plus_overflow_median_all"] = float(np.median(cush))
joint["kept_plus_overflow_median_if_vt_below_cost"] = float(np.median(cush[fell]))
joint["deductions"] = {
    "floor_realised_more_than_4_1pct_below_locked": int((A["floor_real_ratio"] < 0.959).sum()),
    "moved_realised_more_than_2_5pct_below_locked": int((A["moved_real_ratio"] < 0.975).sum()),
    "worst_floor": [float(A["floor_real_ratio"].min()), starts[int(np.argmin(A["floor_real_ratio"]))]],
    "worst_moved": [float(A["moved_real_ratio"].min()), starts[int(np.argmin(A["moved_real_ratio"]))],
                    float(A["m31"][int(np.argmin(A["moved_real_ratio"]))])],
    "gift_realised_below_unrounded_deducted_top": int((J["gift_realised"] < J["top_raw"] - 1e-6).sum()),
    "gift_realised_minus_top_stated_min": float((J["gift_realised"] - J["top_stated"]).min()),
}
eras = {}
for lo, hi in (("1962", "1980"), ("1980", "2000"), ("2000", "2011")):
    msk = np.array([lo <= s[:4] < hi for s in starts])
    eras[f"{lo}-{int(hi) - 1}"] = {
        "windows": int(msk.sum()), "share_with_payment_shortfall": float((A["shortfall"][msk] > 1).mean()),
        "shortfall_p50_p95_max": [float(np.median(A["shortfall"][msk])), float(np.percentile(A["shortfall"][msk], 95)),
                                  float(A["shortfall"][msk].max())],
        "overflow_jan2033_p5_p50": q(A["overflow_jan2033_value"][msk], (5, 50)),
        "kept_p5_p50": q(J["kept33"][msk], (5, 50)),
        "kept_plus_overflow_p5_p50": q(cush[msk], (5, 50)),
        "bottom_stated_p5_p50": qs(J["bottom_stated"][msk], (5, 50)),
        "top_stated_p5_p50": qs(J["top_stated"][msk], (5, 50)),
        "share_vt_below_cost": float(fell[msk].mean()),
    }
joint["by_era_of_start"] = eras
lv3, lv2 = np.log(A["vt3"]), np.log(A["vt2"])
joint["corr_windows"] = {
    "kept33_vs_overflow": float(np.corrcoef(J["kept33"], A["overflow_jan2033_value"])[0, 1]),
    "kept33_vs_shortfall": float(np.corrcoef(J["kept33"], A["shortfall"])[0, 1]),
    "log_shares_2028_2031_vs_log_rate_ratio_2031_over_2028": float(np.corrcoef(lv3, np.log(A["m31"] / A["m28"]))[0, 1]),
    "log_shares_2028_2033_vs_log_rate_ratio_2033": float(np.corrcoef(lv3 + lv2, np.log(A["m33"]))[0, 1]),
    "log_shares_2028_2033_vs_overflow": float(np.corrcoef(lv3 + lv2, A["overflow_jan2033_value"])[0, 1]),
    "note": "585 overlapping monthly windows: about four independent rate eras, so these are descriptions, not estimates",
}
out["joint"] = joint

# ---------------------------------------------------------------- 2. the independent benchmark (585 x 585 pairs)
ii, jj = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
ii, jj = ii.ravel(), jj.ravel()
Pr = plan_path(A["m28"][ii], A["m31"][ii], A["vt3"][jj], A["vt2"][jj])
ov = A["overflow_jan2033_value"][ii]
kp = Pr["kept33"]
kq2 = kp <= np.percentile(kp, 20)
oq2 = ov <= np.percentile(ov, 20)
fell2 = (A["vt3"][jj] * A["vt2"][jj]) < 1.0
out["independent_pairs"] = {
    "pairs": int(ii.size),
    "bottom_stated_p5_p50_p95": qs(Pr["bottom_stated"]), "top_stated_p5_p50_p95": qs(Pr["top_stated"]),
    "kept33_p1_p5_p50_p95": q(kp, (1, 5, 50, 95)),
    "kept_plus_overflow_p5_p50_p95": q(kp + ov),
    "both_in_bottom_fifth": float((kq2 & oq2).mean()),
    "if_vt_below_cost": {"overflow_jan2033_median": float(np.median(ov[fell2])),
                         "share_with_payment_shortfall": float((A["shortfall"][ii][fell2] > 1).mean())},
    "if_vt_above_cost": {"overflow_jan2033_median": float(np.median(ov[~fell2])),
                         "share_with_payment_shortfall": float((A["shortfall"][ii][~fell2] > 1).mean())},
    "share_kept_plus_overflow_under_25k": float(((kp + ov) < 25_000).mean()),
    "kept_plus_overflow_median_if_vt_below_cost": float(np.median((kp + ov)[fell2])),
}
out["joint"]["share_kept_plus_overflow_under_25k"] = float(((J["kept33"] + A["overflow_jan2033_value"]) < 25_000).mean())

# ---------------------------------------------------------------- 3. the house model on the same definitions
H = P.house(c, margin=MARGIN, margin_fn=C.margin_fn(NAME))
_hd0, _hd1, _hd2, _, _ = H["draws"]
_hr = C.rule(H, _hd0 + _hd1, _hd0 + _hd1 + _hd2)
Hb, Ht = _hr["bottom"], _hr["top"]
out["house"] = {"bottom_stated_p5_p50_p95": qs(Hb), "top_stated_p5_p50_p95": qs(Ht),
                "share_most_rule_binds": float(H["most_binds"].mean()),
                "kept33_p1_p5_p50_p95": q(H["kept33"], (1, 5, 50, 95)),
                "floor_p5_p50_p95": q(H["floor"]), "top_model_p5_p50_p95": q(H["top"]),
                "note": "no reinvestment and no overflow in the house model (NUMBERS 7); yields and shares independent"}

# ---------------------------------------------------------------- 4. correlation of stocks and rates in the data used
ym_keys, ym = E.monthly_series(DGS1, "DGS1")
ymap = dict(zip(ym_keys, ym))
ann = []
for y in range(1962, 2023):
    a, b = f"{y}-01", f"{y + 1}-01"
    if a in kpos and b in kpos and a in ymap and b in ymap:
        ann.append((y, math.log(idx[kpos[b]] / idx[kpos[a]]), ymap[b] - ymap[a], math.log(ymap[b] / ymap[a])))
ann = np.array(ann)


def cor(mask):
    return {"years": int(mask.sum()), "stocks_vs_yield_change_points": float(np.corrcoef(ann[mask, 1], ann[mask, 2])[0, 1]),
            "stocks_vs_yield_change_proportional": float(np.corrcoef(ann[mask, 1], ann[mask, 3])[0, 1]),
            "yield_change_sd_points": float(np.std(ann[mask, 2], ddof=1))}


mon = []
for k0, k1 in zip(ym_keys[:-1], ym_keys[1:]):
    if k0 in kpos and k1 in kpos:
        mon.append((int(k0[:4]), math.log(idx[kpos[k1]] / idx[kpos[k0]]), ymap[k1] - ymap[k0]))
mon = np.array(mon)
out["correlation_data"] = {
    "annual_jan_to_jan_1962_2022": cor(np.ones(len(ann), bool)),
    "annual_1962_1999": cor(ann[:, 0] < 2000),
    "annual_2000_2022": cor(ann[:, 0] >= 2000),
    "monthly_1962_2023_stocks_vs_1y_yield_change": float(np.corrcoef(mon[:, 1], mon[:, 2])[0, 1]),
    "monthly_2000_2023": float(np.corrcoef(mon[mon[:, 0] >= 2000, 1], mon[mon[:, 0] >= 2000, 2])[0, 1]),
    "monthly_1962_1999": float(np.corrcoef(mon[mon[:, 0] < 2000, 1], mon[mon[:, 0] < 2000, 2])[0, 1]),
    "dgs1_annual_log_ratio_sd": float(np.std(ann[:, 3], ddof=1)),
    "dgs1_annual_log_ratio_sd_as_points_at_4_6pct": float(np.std(ann[:, 3], ddof=1) * 4.6),
    "house_model": 0.0,
    "house_yield_sd_points": E.ASSUMPTIONS["yield_vol"] * 100,
    "sign": "positive = shares and yields fall together (the recession case the bond desk names)",
}

# ---------------------------------------------------------------- 5. scenario worlds
def world_row(label, world, m28, m31, vt3, vt2, dL=None, us_cpi=0.024, tw_cci=0.030, parallel28=None):
    pay = payments(world)
    r = plan_path(m28, m31, vt3, vt2, dL, parallel28)
    if parallel28 is None:
        fr = fund_ratio(E.J28, world, m28) / math.exp(fF * m28 * tauF)
        mr = fund_ratio(E.J31, world, m31) / math.exp(fM * m31 * tauM)
    else:                                  # parallel worlds: priced the way the rule prices them (forwards + move)
        fr = fund_ratio(E.J28, world, 1.0, fF * (m28 - 1)) / math.exp(fF * m28 * tauF)
        mr = fund_ratio(E.J31, world, 1.0, fM * (m31 - 1)) / math.exp(fM * m31 * tauM)
    paid_out = float(r["floor"] * fr + r["moved"] * mr)
    gift = min(paid_out, float(r["top_stated"]))
    return {"label": label, **{k: float(v) for k, v in pay.items()},
            "completion_jan2028": float(r["complete"]), "left_for_floor_and_vt": float(r["R"]),
            "floor_money": float(r["floor_money"]), "most_binds": bool(r["most_binds"]),
            "vt_bought": float(r["vt28"]), "vt_squeeze": float(r["vt_squeeze"]),
            "floor_payout": float(r["floor"]), "floor_realised": float(r["floor"] * fr),
            "floor_zero_interest": float(r["floor_zero"]), "zero_interest_total": float(r["zero_world"]),
            "bottom_raw": float(r["bottom_raw"]),
            "bottom_stated": float(r["bottom_stated"]), "moved_half": float(r["moved"]), "top_raw": float(r["top_raw"]),
            "top_stated": float(r["top_stated"]), "funds_pay": paid_out, "gift_realised": gift,
            "excess_to_kept_half": paid_out - gift, "kept_half_jan2033": float(r["kept33"]),
            "kept_plus_excess_jan2033": float(r["kept33"]) + paid_out - gift,
            "gift_in_2027_us_dollars": gift / (1 + us_cpi) ** 6,
            "gift_ntd_m_2033_at_32_768": gift * 32.768 / 1e6,
            "gift_ntd_m_in_jan2027_building_costs": gift * 32.768 / (1 + tw_cci) ** 6 / 1e6,
            "us_cpi": us_cpi, "tw_building_costs": tw_cci}


sc = {}
sc["forwards"] = world_row("Today's forwards; shares 7.5% a year", base, 1.0, 1.0, 1.075 ** 3, 1.075 ** 2,
                          parallel28=0.0)
fwdJ28 = c.fwd(E.J28, END)
fwdJ31 = c.fwd(E.J31, END)
sc["minus3"] = world_row("Rates 3 points lower for good from Jan 2027; shares 7.5%", minus3,
                         (fF - 0.03) / fF, (fM - 0.03) / fM, 1.075 ** 3, 1.075 ** 2, dL=-0.03, parallel28=-0.03)
ramp = lambda d: 0.03 * min(max(months_from_j27(d), 0) / 48.0, 1.0)
infl = Additive(c, ramp)
sc["inflation"] = world_row("Inflation world: yields +3 points by 2031, shares flat 2028-2033, prices 5% a year",
                            infl, (fF + ramp(E.J28)) / fF, (fM + ramp(E.J31)) / fM, 1.0, 1.0,
                            dL=ramp(E.J28), us_cpi=0.05, tw_cci=0.05, parallel28=ramp(E.J28))
sc["inflation_shares_minus_20"] = world_row("Inflation world with shares -20% 2028-2031 (1973-74 style)", infl,
                                            (fF + ramp(E.J28)) / fF, (fM + ramp(E.J31)) / fM, 0.8, 1.0,
                                            dL=ramp(E.J28), us_cpi=0.05, tw_cci=0.05, parallel28=ramp(E.J28))
out["scenarios"] = sc

# ---------------------------------------------------------------- 6. the Taiwan dollar test (re-run Tue 10 Nov evening)
# Which "gift": the 2033 contribution after the cap, i.e. the lower of what the floor and the moved half pay and the
# stated top (NUMBERS 4, "One definition, used everywhere"; CANON D12). It is the US-dollar sum fixed at the 2031
# meetings that has to buy a Taiwan-dollar budget in December 2032. Until Tue 10 Nov afternoon the kept-half-alone test
# used what the funds pay (before the cap) and only the cap-rule test used the stated top; both now use the
# contribution, which equals the stated top wherever the funds pay at least the top (every path and window here; the
# share is reported). "x% stronger Taiwan dollar" = x% more US dollars for the same NT$ budget (NUMBERS 8d: NT$ at
# 32.768 / 1.10); the stricter reading (NT$ per US$ falls 10%, so 11.1% more US dollars) is reported beside it.
# Two pots: the half kept alone (VT, promised to no one), and the half kept plus the excess the cap sends to it.
SHARES_OF_CONTRIB = (0.10, 0.13, 0.17, 0.20, 0.30)


def twd_test(kept, contribution, excess, label, top_stated):
    kept, contribution, excess = (np.asarray(a, float) for a in (kept, contribution, excess))
    o = {"label": label,
         "gift_used": "the 2033 contribution after the cap: min(what the floor and the moved half pay, stated top)",
         "share_contribution_equals_stated_top": float((np.abs(contribution - np.asarray(top_stated, float)) < 0.5).mean()),
         "contribution_p5_p50_p95": qs(contribution), "excess_p5_p50_p95": q(excess)}
    for name, pot in (("kept_half", kept), ("kept_half_plus_excess", kept + excess)):
        d = {"pot_p5_p50_p95": q(pot)}
        for x in (0.10, 1 / 0.9 - 1):
            need = contribution * x
            ok = pot >= need
            gap = (need - pot)[~ok]
            d[f"covers_{x:.3f}"] = float(ok.mean())
            d[f"fails_count_{x:.3f}"] = int((~ok).sum())
            d[f"gap_when_fails_p50_p95_max_{x:.3f}"] = ([float(np.median(gap)), float(np.percentile(gap, 95)),
                                                        float(gap.max())] if gap.size else [0.0, 0.0, 0.0])
        ratio = pot / contribution
        d["pot_over_contribution_p5_p50_p95"] = q(ratio)
        d["largest_stronger_twd_covered_19_in_20"] = float(np.percentile(ratio, 5))   # in "x% more US dollars"
        d["largest_covered_19_in_20_as_ntd_per_usd_fall"] = float(1 - 1 / (1 + np.percentile(ratio, 5)))
        # the same pot against an overrun allowance of x% of the contribution (Q5's early-stage norms, illustration only)
        d["covers_share_of_contribution"] = {f"{x:.2f}": float((pot >= contribution * x).mean()) for x in SHARES_OF_CONTRIB}
        o[name] = d
    return o


Hh = P.history(c, margin=MARGIN, margin_fn=C.margin_fn(NAME))
Hh_top_stated = C.rule(Hh)["top"]
H_contrib = np.minimum(H["top"], Ht)                     # the house model's funds pay = H["top"] (model, at the path's rates)
Hh_contrib = np.minimum(Hh["top"], Hh_top_stated)
tw = {"house": twd_test(H["kept33"], H_contrib, H["top"] - H_contrib, "house model, 200,000 paths", Ht),
      "history_rates_at_forwards": twd_test(Hh["kept33"], Hh_contrib, Hh["top"] - Hh_contrib,
                                            "US stocks every window since 1871 (1,770), rates at forwards", Hh_top_stated),
      "joint_replay": twd_test(J["kept33"], J["gift_capped"], J["excess"],
                               "joint replay 1962-2010 starts (585; funds pay as realised on each window's rates)",
                               J["top_stated"])}
out["kept_half_on_meeting_day_2031"] = {"central": float(cen["vt31"] / 2), "house_p5_p50_p95": q(H["vt31"] / 2),
                                        "history_p5_p50_p95": q(Hh["vt31"] / 2), "joint_p5_p50_p95": q(J["vt31"] / 2),
                                        "note": "equal to the moved half on that day, before it is moved"}
# the real Taiwan dollar (Fed H.10 monthly, mirror), paired with the same months' US shares (rates at forwards): the move
# from the meetings (VT purchase + 36 months, Jan 2031) to the gift (+60 months, Jan 2033), on the same contribution
fx = {r["Date"][:7]: float(r["TWD_per_USD"]) for r in csv.DictReader(open(TWD))}
w_hist = P.shiller_windows()
sel, cost, st_fx = [], [], []
for i, (st, _, _) in enumerate(w_hist):
    j0 = kpos[st]
    if j0 + 60 < len(keys) and keys[j0 + 36] in fx and keys[j0 + 60] in fx and st >= "1983-10":
        sel.append(i)
        cost.append(fx[keys[j0 + 36]] / fx[keys[j0 + 60]] - 1)   # extra US$ per fixed NT$ budget (+ = Taiwan dollar stronger)
        st_fx.append(st)
sel, cost = np.array(sel), np.array(cost)
kk, cc, ee = Hh["kept33"][sel], Hh_contrib[sel], (Hh["top"] - Hh_contrib)[sel]
rt = {"windows": int(sel.size), "first_vt_purchase": st_fx[0], "last_vt_purchase": st_fx[-1],
      "meeting_to_gift": "VT purchase + 36 months to + 60 months (Jan 2031 to Jan 2033 in the plan)",
      "gift_used": "the 2033 contribution after the cap (history model, rates at forwards)",
      "contribution_p5_p50_p95": qs(cc),
      "twd_cost_change_p5_p50_p95": q(cost), "twd_cost_change_max_and_start": [float(cost.max()), st_fx[int(np.argmax(cost))]],
      "share_twd_stronger_by_10pct_or_more": float((cost >= 0.10).mean()),
      "share_twd_stronger_at_all": float((cost > 0).mean()),
      "corr_twd_cost_vs_shares_2031_2033": float(np.corrcoef(cost, np.log(np.array([w_hist[i][2] for i in sel])))[0, 1])}
for name, pot in (("kept_half", kk), ("kept_half_plus_excess", kk + ee)):
    need = cc * np.maximum(cost, 0.0)
    gap = need - pot
    bad = gap > 0
    rt[name] = {"covers_actual_move": float((~bad).mean()), "fails_count": int(bad.sum()),
                "fails_starts": [s for s, b in zip(st_fx, bad) if b],
                "gap_when_fails_p50_max": ([float(np.median(gap[bad])), float(gap[bad].max())] if bad.any() else [0.0, 0.0]),
                "worst_uncovered": [float(gap.max()), st_fx[int(np.argmax(gap))]]}
tw["real_twd_with_same_months_shares"] = rt
# the contribution and the stated range in other money, on NUMBERS 8d's conventions (numbers/inflation_inputs.json;
# US dollars of 1 Jan 2027 over 6 years; NT$ of today's building from the Sep 2026 index, 6.17 years, as real_values.py)
_inf = json.load(open(HERE / "inflation_inputs.json"))
_us = [_inf["us"][k] for k in ("low", "central", "high")]
_tc = [_inf["taiwan_construction"][k] for k in ("low", "central", "high")]
_fx0, _fxs = _inf["usdtwd"]["latest"], min(_inf["usdtwd"]["range_10y"])
_yrs_tw = 2033 - 2026 - (10 / 12)
gifts = {"contribution_central": float(np.minimum(cen["top"], cen["top_stated"])),
         "stated_bottom_central": float(cen["bottom_stated"]), "stated_top_central": float(cen["top_stated"]),
         "funds_pay_central_before_cap": float(cen["top"])}
tw["gift_terms"] = {"conventions": {"usdtwd_6nov": _fx0, "strongest_10y": _fxs, "us_inflation_low_central_high": _us,
                                    "tw_building_costs_low_central_high": _tc, "tw_years_from_sep_2026_index": _yrs_tw,
                                    "note": "8d's conventions; the contribution is the stated top centrally"}}
for lab, g in gifts.items():
    tw["gift_terms"][lab] = {
        "usd_paid_dec_2032": g,
        "ntd_m_at_32_768": g * _fx0 / 1e6, "ntd_m_at_strongest_10y": g * _fxs / 1e6,
        "ntd_m_if_twd_10pct_stronger": g * _fx0 / 1.10 / 1e6,
        "in_jan2027_us_dollars_low_central_high": [g / (1 + r) ** 6 for r in _us],
        "ntd_m_of_todays_building_low_central_high_cost_growth": [g * _fx0 / (1 + r) ** _yrs_tw / 1e6 for r in _tc],
        "extra_usd_for_10pct_stronger_twd": g * 0.10,
        "extra_usd_at_strongest_10y": g * (_fx0 / _fxs - 1),
    }
out["twd_test"] = tw

# ---------------------------------------------------------------- 6b. what returns to Laura (Tue 10 Nov evening, NUMBERS 8k)
# Three parts, each in 1 Jan 2033 money at the world's own rates: the backstop's money left after the 2042 payment
# (completion.in_2033_money), the excess the cap sends back (paid about 15 Dec 2032, carried 17 days at the world's own
# rate), and the half kept (VT on 1 Jan 2033). Promised money: the ten payments' value on 1 Jan 2033 at the world's own
# rates, plus the contribution (15 Dec 2032, carried the same 17 days).
def _ret(back, exc, kept, pay33, contr33):
    tot = back + exc + kept
    return {"backstop_left_p5_p50_p95": q(back), "excess_p5_p50_p95": q(exc), "half_kept_p5_p50_p95": q(kept),
            "total_p5_p50_p95": q(tot), "total_p1_min": [float(np.percentile(tot, 1)), float(tot.min())],
            "share_returned_of_all_money_p5_p50_p95": q(tot / (tot + pay33 + contr33)),
            "promised_p5_p50_p95": q(pay33 + contr33)}


fw = sc["forwards"]
g_fw = base.grow(END, E.J33)
pay33_fw = sum(E.PAYMENT * c.P(date(y, 1, 1)) / c.P(E.J33) for y in E.YEARS)
ret_fw = {"backstop_left_jan2033": fw["overflow_jan2033_value"], "backstop_left_nominal_1jan2042": fw["overflow_nominal"],
          "excess_paid_dec2032": fw["excess_to_kept_half"], "excess_jan2033": fw["excess_to_kept_half"] * g_fw,
          "half_kept_jan2033": fw["kept_half_jan2033"],
          "total_excess_at_face": fw["overflow_jan2033_value"] + fw["excess_to_kept_half"] + fw["kept_half_jan2033"],
          "total_jan2033": fw["overflow_jan2033_value"] + fw["excess_to_kept_half"] * g_fw + fw["kept_half_jan2033"],
          "contribution_paid_dec2032": fw["gift_realised"], "contribution_jan2033": fw["gift_realised"] * g_fw,
          "payments_value_jan2033": pay33_fw, "carry_15dec2032_to_1jan2033": g_fw}
ret_fw["promised_jan2033"] = ret_fw["payments_value_jan2033"] + ret_fw["contribution_jan2033"]
ret_fw["share_returned"] = ret_fw["total_jan2033"] / (ret_fw["total_jan2033"] + ret_fw["promised_jan2033"])
ret_fw["total_in_jan2027_money"] = ret_fw["total_jan2033"] * c.P(E.J33)
out["returns_to_laura"] = {
    "forwards": ret_fw,
    "joint_replay": dict(_ret(A["overflow_jan2033_value"], J["excess"] * A["g_end_j33"], J["kept33"], A["pay33"],
                              J["gift_capped"] * A["g_end_j33"]), windows=n,
                         note="each part's percentiles are its own; the total's are of the per-window sums"),
}
_tot = A["overflow_jan2033_value"] + J["excess"] * A["g_end_j33"] + J["kept33"]
out["returns_to_laura"]["joint_replay"]["lowest_total_window"] = window(int(np.argmin(_tot)))
out["returns_to_laura"]["joint_replay"]["lowest_total"] = float(_tot.min())
out["returns_to_laura"]["joint_replay"]["share_total_under_25k_50k"] = [float((_tot < 25_000).mean()),
                                                                       float((_tot < 50_000).mean())]
out["returns_to_laura"]["joint_replay"]["corr_backstop_left_vs_half_kept"] = float(
    np.corrcoef(A["overflow_jan2033_value"], J["kept33"])[0, 1])

# ---------------------------------------------------------------- 7. liquidity: when each payment's cash arrives
liq = []
for y in E.YEARS:
    inst = I[y]
    liq.append({"payment": f"1 Jan {y}", "holding": inst.name, "cash_on": inst.end.isoformat(),
                "months_early": round((date(y, 1, 1) - inst.end).days / 30.44, 1)})
out["liquidity_cash_dates"] = liq
out["liquidity_floor_and_moved"] = {"holding": "IBTM (late-2032 Treasury fund)", "cash_on_or_about": END.isoformat(),
                                    "kept_half": "VT, promised to no one; sellable any trading day"}

json.dump(out, open(HERE / f"results_joint_stress_2026-11-10{C.tag(NAME)}.json", "w"), indent=1, default=float)

# ---------------------------------------------------------------- print
k = lambda x: f"${x:,.0f}"
print("checks:", {a: (round(b, 4) if abs(b) < 5 else round(b)) for a, b in out["checks"].items()})
print(f"joint windows {n} ({starts[0]} to {starts[-1]}); shortfall share {joint['share_with_payment_shortfall']:.1%}; "
      f"p50/p95/max {[round(x) for x in joint['shortfall_p50_p95_max']]}")
for key in ("overflow_jan2033_p5_p50_p95", "bottom_stated_p5_p50_p95", "top_stated_p5_p50_p95", "kept33_p1_p5_p50_p95",
            "kept_plus_overflow_p5_p50_p95", "completion_jan2028_p5_p50_p95", "gift_realised_minus_top_stated_p5_p50_p95"):
    print(" joint", key, [round(x) for x in joint[key]])
for key in ("gift_realised_below_bottom_stated", "floor_realised_below_bottom_stated", "gift_realised_above_top_stated_share",
            "floor_realised_ratio_min", "moved_realised_ratio_min", "both_in_bottom_fifth", "share_vt_below_cost_2033",
            "share_overflow_under_10k_jan2033", "share_kept_plus_overflow_under_25k"):
    print(" joint", key, joint[key])
print(" joint most rule", joint["most_rule"])
for key in ("floor_realised_minus_bottom_stated_min", "gift_realised_minus_top_stated_min_before_cap",
            "zero_interest_floor_minus_bottom_stated_min", "zero_interest_total_minus_top_stated_min"):
    print(" joint", key, round(joint[key]))
print(" joint if VT below cost", joint["if_vt_below_cost"], "| above", joint["if_vt_above_cost"])
print(" joint kept+overflow median all / if VT below cost", round(joint["kept_plus_overflow_median_all"]),
      round(joint["kept_plus_overflow_median_if_vt_below_cost"]), "| independent if below cost",
      round(out["independent_pairs"]["kept_plus_overflow_median_if_vt_below_cost"]) if "independent_pairs" in out else "")
print(" joint deductions", joint["deductions"])
print(" joint both-bottom-fifth starts", len(joint["both_in_bottom_fifth_starts"]), joint["both_in_bottom_fifth_starts"])
for era, v in joint["by_era_of_start"].items():
    print(" era", era, json.dumps(v, default=float))
print(" joint if rates fell 40% by 2031", joint["if_rates_fell_40pct_by_2031"])
print(" joint corr", joint["corr_windows"])
for key in ("bottom_stated_p5_p50_p95", "top_stated_p5_p50_p95", "kept33_p1_p5_p50_p95", "kept_plus_overflow_p5_p50_p95"):
    print(" indep", key, [round(x) for x in out["independent_pairs"][key]])
print(" indep", {a: b for a, b in out["independent_pairs"].items() if not isinstance(b, list)})
print(" house", {a: ([round(x) for x in b] if isinstance(b, list) else b) for a, b in out["house"].items()})
print("corr data", json.dumps(out["correlation_data"], indent=0))
for lab, wdw in list(joint["named"].items()) + [("worst kept", joint["worst_kept"]), ("worst pay", joint["worst_payments"]),
                                                 ("worst kept+over", joint["worst_kept_plus_overflow"]),
                                                 ("lowest top", joint["lowest_top_stated"]),
                                                 ("lowest bottom", joint["lowest_bottom_stated"])]:
    print(f" {lab:15s} {wdw['start']} VT {wdw['vt_bought']} m28 {wdw['rate_ratio_jan2028']:.2f} m31 {wdw['rate_ratio_jan2031']:.2f} "
          f"sh {wdw['shares_2028_2031']:.2f}/{wdw['shares_2031_2033']:.2f} | short {k(wdw['payments_shortfall'])} "
          f"over33 {k(wdw['overflow_jan2033_value'])} | bottom {k(wdw['bottom_stated'])} top {k(wdw['top_stated'])} "
          f"gift {k(wdw['gift_realised'])} kept {k(wdw['kept_half_jan2033'])} compl {k(wdw['completion_jan2028'])}")
for lab, r in sc.items():
    print(f" SC {lab:28s} fm {k(r['floor_money'])} binds {r['most_binds']} squeeze {k(r['vt_squeeze'])} floor {k(r['floor_payout'])} "
          f"realised {k(r['floor_realised'])} zero {k(r['floor_zero_interest'])}/{k(r['zero_interest_total'])} "
          f"raw {k(r['bottom_raw'])}/{k(r['top_raw'])} over nominal {k(r['overflow_nominal'])} funds pay {k(r['funds_pay'])}")
    print(f" SC {lab:28s} short {k(r['shortfall'])} over33 {k(r['overflow_jan2033_value'])} bottom {k(r['bottom_stated'])} "
          f"top {k(r['top_stated'])} gift {k(r['gift_realised'])} kept {k(r['kept_half_jan2033'])} "
          f"compl {k(r['completion_jan2028'])} gift2027$ {k(r['gift_in_2027_us_dollars'])} NT$m(2027 build) {r['gift_ntd_m_in_jan2027_building_costs']:.2f}")
for lab, r in tw.items():
    print(" TWD", lab, json.dumps(r, default=float))
print(" RETURNS forwards", json.dumps(out["returns_to_laura"]["forwards"], default=float))
print(" RETURNS joint", json.dumps({a: b for a, b in out["returns_to_laura"]["joint_replay"].items()
                                    if a != "lowest_total_window"}, default=float))
print(" RETURNS lowest window", json.dumps(out["returns_to_laura"]["joint_replay"]["lowest_total_window"], default=float))
print(" kept half on 2031 meeting day", json.dumps(out["kept_half_on_meeting_day_2031"], default=float))
