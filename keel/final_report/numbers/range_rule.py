"""The 2031 range as one rule, and its confidence (Keel, Tue 10 Nov 2026). MODEL, not a forecast or a promise.

Run from the repo root:  python3 -I keel/final_report/numbers/range_rule.py
   or from this folder:  python3 -I range_rule.py
Writes keel/final_report/numbers/results_range_rule_2026-11-10.json and prints the figures (about 20 seconds, numpy only).
Tue 10 Nov re-run: the completion is the call in completion.py (H_plain, "sufficient without reinvestment"); add
`--design KEEL` for Mon 9 Nov's margin. The first run's output, results_range_rule.json, is kept as it was.

Card: keel/final_report/research/cards/Q19_range_rule_and_confidence.md. Engine and paths are the register's own
(engine.py, plan.py; curve 6 Nov 2026; house model 200,000 paths, seed 2033; Shiller windows since 1871; Keel's margin
= design A sized for reinvestment 3 points below forwards, NUMBERS section 2).

The rule tested (notes, not report text):
  bottom  = what the floor fund pays if, from the day it was bought, no distribution and none of its final cash earns
            anything (its "zero-interest value"), rounded down to $5,000;
  top     = the floor's zero-interest value + the moved half's zero-interest value (measured from the move), rounded
            down to $5,000;
  cap     = the 2033 facility contribution is the lower of what the floor and the moved half actually pay and the stated
            top; anything above the top joins the half kept (CANON D12);
  when    = both ends are stated only after the move (IPS l.15: "Before you meet co-sponsors in 2031, the other half
            will move into Treasuries").
Deductions are worked out at each path's own purchase yields (the zero-interest loss is larger when yields are higher),
and compared with the fixed 4.1% and 2.5% of NUMBERS section 3.

Tue 10 Nov afternoon (bond desk check, research/panel/2026-11-10_bond_desk_register_check.md, findings 1, 2, 5, 9):
the call is now completion.rule: each end is the money put in x the zero-interest payout per $1 of the fund's own
holdings on the trade day (the engine's IBTM bond, coupon fixed on the 6 Nov curve, priced on that day's curve), less
0.5%, rounded down to $5,000. The morning's one-par-bond rule stays as "par", measured from purchase. The "worst case
owned" is now the zero-interest payout of the engine's holdings, and owned_test() re-tests every stated end against
3.50% and 4.00% coupons, the par stand-in and frictions of 0.1% to 1%. History windows move yields in proportion
(mF, mM), not by a parallel equivalent. Stated (rounded) percentiles use the 'lower' method. The floor gets the larger
of 73.3% of what is left and $75,001 (plan.run, most=True).
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

STEP = 5_000.0
c = E.Curve(E.load_par())
I = E.instruments(c)
base = E.Reinvest(c)
u_fwd = E.size_own_rung(I, base)
import completion as C   # noqa: E402
NAME = C.design_arg()
DSG = C.design(NAME)
MARGIN = DSG["margin"]                                   # 1 Jan 2027 value: H_plain $33,484; KEEL $21,149
MF = C.margin_fn(NAME)                                   # its January 2028 price on each path (completion.py)
WAM, END = I[2033].hold_mat, I[2033].end               # IBTM's holdings mature about 4 Jul 2032; fund ends 15 Dec 2032
FEE = E.ASSUMPTIONS["fund_fee"]
out = {"stamp": {"curve": "US Treasury par curve, 6 Nov 2026 close", "engine": "engine.py + plan.py (register)",
                 "design": NAME, "margin_jan2027_value": MARGIN, "rounding": "down to $5,000", "status": "MODEL"}}


def down(x, step=STEP):
    return np.floor(np.asarray(x, float) / step) * step


# ---------------------------------------------------------------- 1. the deductions, re-derived (NUMBERS 3)

def fund_flows(curve, buy, coupon=None):
    """$1 put into the late-2032 iBond fund (IBTM) on `buy`: its holdings as one bond maturing at the fund's average
    maturity (WAM), at the curve's par yield (as engine.py does) or at a given coupon priced on the curve; the fee
    shrinks each flow by (1 - fee)^years held. The holdings' principal then waits in cash inside the fund to 15 Dec."""
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
    """Share of the modelled payout (every flow earning forward rates to 15 Dec 2032) lost if (a) nothing earns any
    interest from the purchase on, (b) rates fall 3 points for good from the purchase, (c) for the floor only: nothing
    earns any interest from 1 Jan 2031 on (what can still be lost on the day she speaks, money received before then
    counted at its value that day)."""
    cpn, fl = fund_flows(curve, buy, coupon)
    b, z, s3 = E.Reinvest(curve), E.Reinvest(curve, "zero"), E.Reinvest(curve, "shift", 0.03)
    v = lambda w: sum(a * w.grow(d, END) for d, a in fl)
    vb = v(b)
    r = {"coupon": cpn, "flows": len(fl), "zero": 1 - v(z) / vb, "minus3": 1 - v(s3) / vb}
    if buy < E.J31:
        held = sum(a * b.grow(d, E.J31) for d, a in fl if d < E.J31) + sum(a for d, a in fl if d >= E.J31)
        r["zero_from_2031"] = 1 - held / vb
    return r


dd = {"floor_bought_jan2028": losses(c, E.J28), "moved_half_bought_jan2031": losses(c, E.J31),
      "floor_with_ibtm_real_coupon_3.50pct": losses(c, E.J28, coupon=0.035),
      "moved_with_ibtm_real_coupon_3.50pct": losses(c, E.J31, coupon=0.035)}
GRID = np.round(np.arange(-0.0425, 0.0601, 0.0025), 6)
gF, gF31, gM = [], [], []
for s in GRID:
    cs = E.Curve(c.par, shift=float(s))
    lf, lm = losses(cs, E.J28), losses(cs, E.J31)
    gF.append(max(lf["zero"], 0.0))
    gF31.append(max(lf["zero_from_2031"], 0.0))
    gM.append(max(lm["zero"], 0.0))
gF, gF31, gM = map(np.array, (gF, gF31, gM))
dd["by_parallel_yield_shift"] = {f"{s*100:+.2f}pt": {"floor_zero": float(a), "floor_zero_from_2031": float(b2),
                                                      "moved_zero": float(m)}
                                 for s, a, b2, m in zip(GRID, gF, gF31, gM) if abs(round(s * 400) % 2) == 0}
out["deductions"] = dd
# the same on the fund's own holdings (the call): zero-interest payout per $1 on the trade day, and the cut it implies
TAU_F, TAU_M = E.yf(END, E.J28), E.yf(END, E.J31)
growF = lambda s: np.exp(np.maximum(C._fF0 + s, 0.001) * TAU_F) * (1 - FEE) ** TAU_F   # plan.run's floor per $1
growM = lambda s: np.exp(np.maximum(C._fM0 + s, 0.001) * TAU_M) * (1 - FEE) ** TAU_M
dd["holdings_by_parallel_yield_shift"] = {
    f"{s*100:+.0f}pt": {"floor_zero_per_dollar": float(C.zero_per_dollar(E.J28, s)),
                        "floor_cut_before_haircut": float(1 - C.zero_per_dollar(E.J28, s) / growF(s)),
                        "floor_cut_with_haircut": float(1 - C.zero_per_dollar(E.J28, s) * (1 - C.HAIRCUT) / growF(s)),
                        "moved_zero_per_dollar": float(C.zero_per_dollar(E.J31, s)),
                        "moved_cut_before_haircut": float(1 - C.zero_per_dollar(E.J31, s) / growM(s))}
    for s in (-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03)}
HG = np.round(np.arange(-0.04, 0.0601, 0.0025), 6)
hF = np.array([1 - C.zero_per_dollar(E.J28, s) / growF(s) for s in HG])     # holdings' true floor loss by shift
zF = lambda s: np.interp(s, GRID, gF)
zF31 = lambda s: np.interp(s, GRID, gF31)
zM = lambda s: np.interp(s, GRID, gM)


# ---------------------------------------------------------------- 2. the rule on one path (any of the engine's worlds)

RULES = ("holdings", "par", "par_2031", "fixed")


def rule(res, sF=0.0, sM=0.0, mF=1.0, mM=1.0, floor_rule="holdings"):
    """Stated ends, payout and excess. res: plan.run output; sF, sM: parallel yield moves at the floor's purchase and at
    the move; mF, mM: proportional moves (history windows). floor_rule 'holdings' (the call): completion.rule, on the
    fund's own holdings with the 0.5% cut; 'par': the morning's one-par-bond deductions measured from purchase; 'par_2031':
    the floor's measured from the move date; 'fixed': NUMBERS 3's old fixed 4.1% and 2.5%. Every rule is tested against
    the same worst case: the zero-interest payout of the engine's holdings, no cut."""
    hr = C.rule(res, sF, sM, mF, mM)
    F, M, K = np.broadcast_arrays(*(np.asarray(res[x], float) for x in ("floor", "moved", "kept33")))
    eF = np.asarray(sF, float) + C._fF0 * (np.asarray(mF, float) - 1)
    eM = np.asarray(sM, float) + C._fM0 * (np.asarray(mM, float) - 1)
    if floor_rule == "holdings":
        dF, dM, bottom, top = hr["dF"], hr["dM"], hr["bottom"], hr["top"]
    else:
        if floor_rule == "fixed":
            dF, dM = 0.041 + 0 * F, 0.025 + 0 * M
        else:
            dF = zF(eF) if floor_rule == "par" else zF31(eF)
            dM = zM(eM)
        bottom, top = down(F * (1 - dF)), down(F * (1 - dF) + M * (1 - dM))
    z = 0 * F
    dF, dM, bottom, top = dF + z, dM + z, bottom + z, top + z
    worst, worst_floor = hr["zero_world"] + z, hr["floor_zero"] + z
    payout = F + M                                          # at the path's own rates (plan.py's "top")
    gift = np.minimum(payout, top)
    return dict(F=F, M=M, dF=dF, dM=dM, bottom=bottom, top=top, worst=worst, worst_floor=worst_floor,
                payout=payout, gift=gift, excess=payout - gift, kept=K, kept_plus=K + payout - gift,
                worst_below_top=worst < top - 0.5, worst_below_bottom=worst_floor < bottom - 0.5,
                floor_money=np.asarray(res["floor_money"], float) + 0 * F, most_binds=np.asarray(res["most_binds"]) | (0 * F > 0))


def k(x):
    return float(np.round(x, 0))


q = lambda a, p: float(np.percentile(a, p)) if np.size(a) else 0.0
qs = lambda a: C.qs(a) if np.size(a) else [0.0, 0.0, 0.0]          # stated figures: no interpolation between steps
cen = P.run(c, margin=MARGIN, margin_fn=MF)
central = {}
for lab in RULES:
    r = rule(cen, floor_rule=lab)
    central[lab] = {key: k(np.asarray(r[key]).item()) for key in ("F", "M", "bottom", "top", "worst", "worst_floor",
                                                                  "payout", "gift", "excess", "kept", "kept_plus",
                                                                  "floor_money")}
    central[lab]["dF"], central[lab]["dM"] = float(np.asarray(r["dF"]).item()), float(np.asarray(r["dM"]).item())
rc = rule(cen)
hc = C.rule(cen)
F0, M0 = float(cen["floor"]), float(cen["moved"])
central["holdings_raw"] = {"bottom_unrounded": k(hc["bottom_raw"].item()), "top_unrounded": k(hc["top_raw"].item()),
                           "floor_zero_payout": k(hc["floor_zero"].item()), "moved_zero_payout": k(hc["moved_zero"].item()),
                           "zero_world": k(hc["zero_world"].item()), "zF_per_dollar": float(hc["zF"]),
                           "zM_per_dollar": float(hc["zM"])}
central["rounded_to_1000_instead"] = {"bottom": k(down(hc["bottom_raw"], 1000).item()),
                                      "top": k(down(hc["top_raw"], 1000).item())}
central["owned_test"] = C.owned_summary(C.owned_test(cen, hc))
central["owned_after_move_zero_world_minus_bottom"] = k(central["holdings"]["worst_floor"] - central["holdings"]["bottom"])
central["owned_after_move_zero_world_minus_top"] = k(central["holdings"]["worst"] - central["holdings"]["top"])
central["owned_after_move_forward_minus_top"] = k(central["holdings"]["payout"] - central["holdings"]["top"])
out["central"] = central


# ---------------------------------------------------------------- 3. house model (paths drawn exactly as plan.house)

d0, d1, d2, vt3, vt2 = P.draws()
H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
chk = P.house(c, margin=MARGIN, margin_fn=MF)
assert np.allclose(H["top"], chk["top"]), "house paths differ from plan.house"
mu, sd = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"]


def summarise(r, res):
    pct = lambda a: [q(a, 5), q(a, 50), q(a, 95)]
    width = r["top"] - r["bottom"]
    return {
        "stated_bottom_p5_p50_p95": qs(r["bottom"]), "stated_top_p5_p50_p95": qs(r["top"]),
        "floor_payout_p5_p50_p95": pct(r["F"]), "payout_floor_plus_moved_p5_p50_p95": pct(r["payout"]),
        "range_width_p5_p50_p95": qs(width), "share_width_zero": float((width < 1).mean()),
        "share_payout_above_stated_top": float((r["payout"] > r["top"] + 1e-6).mean()),
        "excess_p5_p50_p95": pct(r["excess"]), "excess_mean": float(r["excess"].mean()),
        "share_gift_below_bottom": float((r["gift"] < r["bottom"] - 1e-6).mean()),
        "share_gift_equals_top": float((np.abs(r["gift"] - r["top"]) < 1e-6).mean()),
        "share_zero_world_below_stated_top": float(r["worst_below_top"].mean()),
        "share_zero_world_floor_below_stated_bottom": float(r["worst_below_bottom"].mean()),
        "kept_half_p5_p50_p95": pct(r["kept"]), "kept_plus_excess_p5_p50_p95": pct(r["kept_plus"]),
        "floor_deduction_p5_p50_p95": pct(r["dF"]), "moved_deduction_p5_p50_p95": pct(r["dM"]),
        "share_payments_full": float(np.mean(res["payments_full"])),
        "share_most_rule_binds": float(np.mean(res["most_binds"])),
    }


sF_h, sM_h = d0 + d1, d0 + d1 + d2
house = {lab: summarise(rule(H, sF_h, sM_h, floor_rule=lab), H) for lab in RULES}
rh = rule(H, sF_h, sM_h)
hh = C.rule(H, sF_h, sM_h)
house["holdings"]["P_stated_top_at_least"] = {f"{t//1000}k": float((rh["top"] >= t).mean())
                                              for t in (90_000, 100_000, 110_000, 115_000, 120_000, 130_000, 140_000, 150_000)}
house["holdings"]["P_stated_bottom_at_least"] = {f"{t//1000}k": float((rh["bottom"] >= t).mean())
                                                 for t in (80_000, 90_000, 95_000, 100_000, 110_000, 120_000)}
house["holdings"]["owned_test"] = C.owned_summary(C.owned_test(H, hh, sF_h, sM_h))
for lab in ("par", "fixed"):
    rx = rule(H, sF_h, sM_h, floor_rule=lab)
    g = (rx["top"] - rx["worst"])[rx["worst_below_top"]]
    house[lab]["zero_world_shortfall_below_top_p50_p95_max_where_short"] = (
        [q(g, 50), q(g, 95), float(g.max())] if g.size else [0, 0, 0])
house["fixed"]["purchase_shift_above_which_fixed_4.1pct_is_below_true_zero_loss_pt"] = float(np.interp(0.041, hF, HG) * 100)
house["fixed"]["share_paths_floor_shift_above_that"] = float((sF_h > np.interp(0.041, hF, HG)).mean())
out["house"] = house

# framing options after the move (claim 4): what each states, what a co-sponsor can count (CASE: documented commitment
# at face value; an "up to" counts as nothing, Q18 rows 1, 5-7), and where the gift lands
def options(r):
    narrow_bottom, narrow_top = down(r["worst"] * (1 - C.HAIRCUT)), down(r["payout"])
    return {
        "A_ips_band": {"bottom": r["bottom"], "top": r["top"], "counted_if_bottom_pledged": r["bottom"],
                       "gift": r["gift"], "excess": r["excess"]},
        "C_narrow_after_move": {"bottom": narrow_bottom, "top": narrow_top, "counted_if_bottom_pledged": narrow_bottom,
                                "gift": np.minimum(r["payout"], narrow_top), "excess": r["payout"] - np.minimum(r["payout"], narrow_top)},
        "D_one_figure_at_least": {"bottom": r["top"], "top": r["top"], "counted_if_bottom_pledged": r["top"],
                                  "gift": r["gift"], "excess": r["excess"]},
    }


out["framing_options_central"] = {kk: {a: k(np.asarray(b).item()) for a, b in vv.items()} for kk, vv in options(rc).items()}
out["framing_options_house_p5_p50_p95"] = {kk: {a: (qs(np.asarray(b)) if a in ("bottom", "top", "counted_if_bottom_pledged")
                                                    else [q(np.asarray(b), p) for p in (5, 50, 95)]) for a, b in vv.items()}
                                          for kk, vv in options(rh).items()}
out["framing_options_house_counted_gain_C_over_A"] = qs(down(rh["worst"] * (1 - C.HAIRCUT)) - rh["bottom"])


# ---------------------------------------------------------------- 4. US stock history (plan.history; yields at forwards)

HS = P.history(c, margin=MARGIN, margin_fn=MF)
rs = rule(HS)
hist = summarise(rs, HS)
hist["owned_test"] = C.owned_summary(C.owned_test(HS, C.rule(HS)))
starts = HS["starts"]
lo_i = int(np.argmin(rs["top"]))
hist["lowest_stated_top"] = [k(rs["top"][lo_i]), starts[lo_i]]
hist["windows"] = len(starts)
named = {}
for key in ("1929-07", "1929-09", "1973-01", "2000-01", "2007-07", "2008-01", "2009-03", "2020-01"):
    if key in starts:
        i = starts.index(key)
        named[key] = {"vt_3yr_growth": float(HS["vt31"][i] / HS["vt28"]), "stated_bottom": k(rs["bottom"][i]),
                      "stated_top": k(rs["top"][i]), "payout": k(rs["payout"][i]), "gift": k(rs["gift"][i]),
                      "excess": k(rs["excess"][i]), "kept_half_2033": k(rs["kept"][i]),
                      "kept_plus_excess_2033": k(rs["kept_plus"][i])}
hist["named_windows"] = named
out["history_stocks"] = hist


# ---------------------------------------------------------------- 5. joint history: rates and US stocks, same months

def shiller_index():
    p, dv, keys = [], [], []
    for r in csv.DictReader(open(E.ROOT / "keel/models/data/shiller_monthly.csv")):
        if r["Date"] >= "2023-07":
            break
        p.append(float(r["SP500"]))
        dv.append(float(r["Dividend"]))
        keys.append(r["Date"][:7])
    p, dv = np.array(p), np.array(dv)
    idx = np.r_[1.0, np.cumprod((p[1:] + dv[:-1] / 12) / p[:-1])]
    return {kk: i for i, kk in enumerate(keys)}, idx


pos, idx = shiller_index()
st = P.setup(c)
DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"
JK = ("bottom", "top", "payout", "excess", "kept", "kept_plus", "worst_below_top", "worst_below_bottom",
      "floor_money", "most_binds")
J = {"start": [], "short": [], **{kk: [] for kk in JK}}
OT = []
for s0, mult in E.history_windows(DGS1, "DGS1"):
    i0 = pos.get(s0)
    if i0 is None or i0 + 72 >= len(idx):
        continue
    w = E.Reinvest(c, "hist", mult=mult)
    short = C.short(w, DSG["own"], DSG["pool"])
    a3 = idx[i0 + 48] / idx[i0 + 12]            # VT bought Jan 2028 = 12 months after the window starts; moved 3 years on
    a2 = idx[i0 + 72] / idx[i0 + 48]
    m28, m31 = mult(E.J28), mult(E.J31)
    jd1 = st["fF"] * (m28 - 1)
    jd2 = st["fM"] * m31 - st["fM"] - jd1
    mfj = C.margin_fn_mult(NAME, m28) if NAME != "KEEL" else None
    res = P.run(c, MARGIN, None, 150_000.0, 0.0, jd1, jd2, a3, a2, mfj)
    r = rule(res, mF=m28, mM=m31)
    OT.append(C.owned_test(res, C.rule(res, mF=m28, mM=m31), mF=m28, mM=m31))
    J["start"].append(s0)
    J["short"].append(short)
    for key in JK:
        J[key].append(float(np.asarray(r[key]).item()))
for key in J:
    if key != "start":
        J[key] = np.array(J[key])
ot_joint = {v: {f: np.array([float(np.asarray(o[v][f]).item()) for o in OT]) for f in OT[0][v]} for v in OT[0]}
has_short = J["short"] > 1
joint = {"windows": len(J["start"]), "first": J["start"][0], "last": J["start"][-1],
         "share_payments_short": float(has_short.mean()),
         "stated_top_p5_p50_p95": qs(J["top"]),
         "stated_bottom_p5_p50_p95": qs(J["bottom"]),
         "share_payout_above_top": float((J["payout"] > J["top"] + 1e-6).mean()),
         "share_zero_world_below_top": float(J["worst_below_top"].mean()),
         "share_zero_world_floor_below_bottom": float(J["worst_below_bottom"].mean()),
         "owned_test": C.owned_summary(ot_joint),
         "most_rule": {"windows_binding": int(J["most_binds"].sum()),
                       "binding_starts": [J["start"][i] for i in np.flatnonzero(J["most_binds"] > 0.5)][:40],
                       "floor_money_p5_p50_p95": [q(J["floor_money"], p) for p in (5, 50, 95)]},
         "excess_p5_p50_p95": [q(J["excess"], p) for p in (5, 50, 95)],
         "where_payments_short": {
             "short_p50_max": [q(J["short"][has_short], 50), float(J["short"][has_short].max())] if has_short.any() else [0, 0],
             "excess_p50_min": [q(J["excess"][has_short], 50), float(J["excess"][has_short].min())] if has_short.any() else [0, 0],
             "share_excess_alone_covers": float((J["excess"][has_short] >= J["short"][has_short]).mean()) if has_short.any() else None,
             "share_excess_plus_kept_covers": float((J["kept_plus"][has_short] >= J["short"][has_short]).mean()) if has_short.any() else None,
             "share_gift_after_short_still_at_or_above_bottom": float((J["payout"][has_short] - J["short"][has_short] >= J["bottom"][has_short]).mean()) if has_short.any() else None,
             "share_gift_after_short_still_at_top": float((J["payout"][has_short] - J["short"][has_short] >= J["top"][has_short]).mean()) if has_short.any() else None,
             "gift_after_short_minus_bottom_min": float((J["payout"][has_short] - J["short"][has_short] - J["bottom"][has_short]).min()) if has_short.any() else None,
             "starts": [J["start"][i] for i in np.flatnonzero(has_short)],
         }}
named_j = {}
for key in ("1973-01", "1979-10", "1981-01", "1981-12", "2000-01", "2002-09", "2007-07", "2008-01"):
    if key in J["start"]:
        i = J["start"].index(key)
        named_j[key] = {kk: k(J[kk][i]) for kk in ("short", "bottom", "top", "payout", "excess", "kept", "kept_plus",
                                                   "floor_money")}
joint["named_windows"] = named_j
out["history_joint_rates_and_stocks"] = joint


# ---------------------------------------------------------------- 6. how the range narrows: today, Jan 2028, Jan 2031, 2033

rng = np.random.default_rng(2031)
n = 200_000
v3 = np.exp(rng.normal(mu * 3, sd * math.sqrt(3), n))
v2 = np.exp(rng.normal(mu * 2, sd * math.sqrt(2), n))
dm = rng.normal(0, E.ASSUMPTIONS["yield_vol"] * math.sqrt(3), n)
R28 = P.run(c, MARGIN, None, 150_000.0, 0.0, 0.0, dm, v3, v2, MF)      # floor bought at today's forwards; VT still to run
r28 = rule(R28, 0.0, dm)
narrow = {
    "today_nov2026": {"stated_bottom_p5_p50_p95": house["holdings"]["stated_bottom_p5_p50_p95"],
                      "stated_top_p5_p50_p95": house["holdings"]["stated_top_p5_p50_p95"]},
    "jan2028_floor_bought_at_forwards": {"stated_bottom": k(r28["bottom"][0]),
                                         "stated_top_p5_p50_p95": qs(r28["top"]),
                                         "kept_plus_excess_p5_p50_p95": [q(r28["kept_plus"], p) for p in (5, 50, 95)]},
    "jan2031_after_move_central": {"stated_bottom": central["holdings"]["bottom"], "stated_top": central["holdings"]["top"],
                                   "worst_case_owned": central["holdings"]["worst"],
                                   "payout_at_forwards": central["holdings"]["payout"]},
    "dec2032_paid_central": {"gift": central["holdings"]["gift"], "excess_to_kept_half": central["holdings"]["excess"],
                             "kept_half_plus_excess_1jan2033": central["holdings"]["kept_plus"]},
}
out["narrowing"] = narrow


# ---------------------------------------------------------------- 7. stating the range before the move is made

def before_move(gap_years, n=200_000, seed=7):
    """She states the top on a day `gap_years` before the move, from VT's value that day; VT then moves randomly
    until the move. Share of draws where the zero-interest payout of the engine's holdings after the move is below the
    stated top, and the median and 1-in-20 size of that gap. Central path otherwise."""
    g = np.random.default_rng(seed)
    ratio = np.exp(g.normal(mu * gap_years, sd * math.sqrt(gap_years), n)) * (1 - E.ASSUMPTIONS["vt_fee"]) ** gap_years
    Fz = float(hc["floor_zero"])
    Mz_then = float(hc["moved_zero"]) / ((1 + E.ASSUMPTIONS["eq_growth"]) ** gap_years)   # VT that day, central
    top_then = down((Fz + Mz_then) * (1 - C.HAIRCUT))
    gap = top_then - (Fz + Mz_then * ratio)
    bad = gap > 0
    return {"share_top_not_owned": float(bad.mean()), "gap_p50_p95_where_short": [q(gap[bad], 50), q(gap[bad], 95)],
            "stated_top": float(top_then)}


def before_move_house(gap_years, seed=8):
    """As before_move, over the house paths: each path's moved half is its value on the day she speaks; VT then moves
    by an independent draw until the move (the rounding headroom differs path by path)."""
    g = np.random.default_rng(seed)
    ratio = np.exp(g.normal(mu * gap_years, sd * math.sqrt(gap_years), P.N)) * (1 - E.ASSUMPTIONS["vt_fee"]) ** gap_years
    Fz, Mz = hh["floor_zero"], hh["moved_zero"]
    top_then = down((Fz + Mz) * (1 - C.HAIRCUT))
    gap = top_then - (Fz + Mz * ratio)
    bad = gap > 0
    return {"share_top_not_owned": float(bad.mean()), "gap_p50_p95_where_short": [q(gap[bad], 50), q(gap[bad], 95)]}


out["stated_before_move"] = {f"{m}_months": {"central": before_move(m / 12), "house": before_move_house(m / 12)}
                             for m in (1, 3, 6, 12)}


# ---------------------------------------------------------------- 8. Exhibit 3 candidate rows

def scen(label, z_sh=0.0, z_y=0.0, vt3x=None, vt2x=None, d1x=None, d2x=None):
    t0 = E.yf(E.J27)
    sv = E.ASSUMPTIONS["yield_vol"]
    S = z_y * sv * math.sqrt(t0 + 1)                         # yields at Jan 2028, conditional split before/after Jan 2027
    a0, a1 = S * t0 / (t0 + 1), S / (t0 + 1)
    a1 = a1 if d1x is None else d1x
    a2 = 0.0 if d2x is None else d2x
    g3 = math.exp(mu * 3 + z_sh * sd * math.sqrt(3)) if vt3x is None else vt3x
    g2 = math.exp(mu * 2) if vt2x is None else vt2x
    res = P.run(c, MARGIN, None, 150_000.0, a0, a1, a2, g3, g2, MF)
    r = rule(res, a0 + a1, a0 + a1 + a2)
    row = {key: k(np.asarray(r[key]).item()) for key in ("bottom", "top", "payout", "gift", "excess", "kept", "kept_plus",
                                                         "floor_money")}
    row["most_binds"] = bool(np.asarray(r["most_binds"]).item())
    row["vt_3yr_growth"] = g3
    row["range"] = label
    return row


rows = {
    "shares_1in20_low_2028_31": scen("shares low", z_sh=-1.645),
    "shares_median": scen("median", z_sh=0.0),
    "shares_1in20_high_2028_31": scen("shares high", z_sh=1.645),
    "yields_1in20_low_jan2028": scen("yields low", z_y=-1.645),
    "yields_1in20_high_jan2028": scen("yields high", z_y=1.645),
    "vt_to_zero": scen("VT worthless", vt3x=0.0, vt2x=0.0),
}
for key in ("2008-01", "1929-07", "2000-01"):
    if key in named:
        rows[f"history_vt_bought_{key}"] = dict(named[key], range=f"US stocks from {key}")
for key in ("2007-07",):
    if key in named_j:
        rows[f"joint_rates_and_stocks_from_{key}"] = dict(named_j[key], range=f"rates and US stocks from {key}")
out["exhibit3_rows"] = rows

(HERE / f"results_range_rule_2026-11-10{C.tag(NAME)}.json").write_text(json.dumps(out, indent=1, default=str))


# ---------------------------------------------------------------- print
def m(x):
    return f"${x:,.0f}"


print("margin", m(MARGIN))
for key, v in dd.items():
    if key not in ("by_parallel_yield_shift", "holdings_by_parallel_yield_shift"):
        print("deduction", key, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
print("holdings by shift", json.dumps({kk: {a: round(b, 5) for a, b in vv.items()}
                                       for kk, vv in dd["holdings_by_parallel_yield_shift"].items()}))
for lab in RULES:
    print("central", lab, {kk: (m(vv) if abs(vv) > 1 else round(vv, 4)) for kk, vv in central[lab].items()})
for kk in ("holdings_raw", "rounded_to_1000_instead", "owned_test"):
    print("central", kk, json.dumps(central[kk]))
print("central owned after move: floor zero - bottom", m(central["owned_after_move_zero_world_minus_bottom"]),
      "| zero world - top", m(central["owned_after_move_zero_world_minus_top"]),
      "| forwards - top", m(central["owned_after_move_forward_minus_top"]))
for lab, v in house.items():
    print("house", lab, json.dumps({kk: ([round(x) if abs(x) > 1 else round(x, 4) for x in vv] if isinstance(vv, list)
                                         else (round(vv, 4) if isinstance(vv, float) else vv)) for kk, vv in v.items()}))
print("history", json.dumps({kk: vv for kk, vv in hist.items() if kk != "named_windows"}, default=str)[:3000])
for kk, vv in named.items():
    print("  window", kk, vv)
print("joint", json.dumps({kk: vv for kk, vv in joint.items() if kk != "named_windows"})[:4000])
for kk, vv in named_j.items():
    print("  joint window", kk, vv)
print("narrowing", json.dumps(narrow))
print("framing central", json.dumps(out["framing_options_central"]))
print("framing house", json.dumps({kk: {a: [round(x) for x in b] for a, b in vv.items()} for kk, vv in out["framing_options_house_p5_p50_p95"].items()}))
print("counted gain C over A (house p5/50/95)", [round(x) for x in out["framing_options_house_counted_gain_C_over_A"]])
print("stated before move", json.dumps(out["stated_before_move"]))
for kk, vv in rows.items():
    print("exhibit3", kk, {a: (round(b, 3) if isinstance(b, float) and abs(b) < 10 else b) for a, b in vv.items()})
