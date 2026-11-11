"""How much room the 2031 range leaves, path by path (Keel numbers owner, Wed 11 Nov 2026 evening, Sydney). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/range_margin.py
   or from this folder:  python3 -I range_margin.py
Writes keel/final_report/numbers/results_range_margin_2026-11-11.json and prints the figures (about 15 seconds, numpy
only). Reads no results file and writes no other file. NUMBERS 8l.

The claim tested (card Q4c, Gaps; NUMBERS 4, "The 2031 move and the range"): "After the 2031 move the gift stays inside
the stated range with room to spare in every path, and the range never collapses to one figure."

Definitions (NUMBERS 0, 3 and 4; the Tue 10 Nov register, design H_plain, exactly as range_rule.py and joint_stress.py
use them):
  * each stated end = the money put into the late-2032 fund x what $1 of the fund's own holdings pays on 15 Dec 2032 if
    nothing earns interest from the trade day, less 0.5%, rounded down to $5,000 (completion.rule); the bottom is fixed
    when the floor is bought (Jan 2028), the top at the 2031 move;
  * the 2033 facility contribution = the lower of what the floor and the moved half pay and the stated top; the excess
    above the top joins the half kept;
  * "what the funds pay": house model and US stock history as range_rule.py (plan.run's floor + moved half, at the
    path's purchase yields); joint replay as joint_stress.py (realised on each window's own rates, NUMBERS 8i).

Three worlds, each built by the register's own functions (route 1):
  house    plan.draws + plan.run + completion.rule, as range_rule.py section 3 (200,000 paths, seed 2033);
  history  plan.history + completion.rule, as range_rule.py section 4 (1,770 windows, rates at today's forwards);
  joint    joint_stress.py's own setup code, run from its source up to its first results block (nothing it writes is
           run), so its plan_path and fund_ratio are used as they stand (585 windows).

Route 2, a second calculation (as returns_check.py checks NUMBERS 8k): it takes only each path's money left after the
completion (R), its draws or window inputs and the curve's discount factors, and recomputes everything after that with
its own code: the IBTM holdings (coupon re-derived from the curve), the split of the 2028 money ("most"), VT and the
moved half, each end's zero-interest payout, the rounding (in whole dollars, integer division), what the funds pay
(the joint replay's realised payout re-derived from the window's 1-year yield ratios), the contribution and the excess.
It does not call completion.rule, completion.zero_per_dollar, plan.run or joint_stress's functions. Plus three checks
that need no model: the rounding bounds on each margin, the expected number of one-figure ranges if the rounding
remainder is uniform, and the house model re-drawn with another seed. And one stricter reading: the floor's and moved
half's distributions wait in the Treasury-bill ETF at its 0.15% a year fee (NUMBERS 0) instead of at face.
"""
import ast
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

NAME = C.design_arg()
DSG = C.design(NAME)
MARGIN = DSG["margin"]
MF = C.margin_fn(NAME)
c = E.Curve(E.load_par())
STEP = 5_000.0
END = date(2032, 12, 15)
FRICTIONS = (0.005, 0.0075, 0.01)


# ---------------------------------------------------------------- route 1: the register's own functions

def joint_setup():
    """Run joint_stress.py's own top-level code up to its first results block (def window), skipping every statement
    that assigns to its `out` dict; nothing is written. Returns its namespace (J, A, starts, ...)."""
    path = HERE / "joint_stress.py"
    tree = ast.parse(path.read_text())

    def touches_out(t):
        while isinstance(t, (ast.Subscript, ast.Attribute)):
            t = t.value
        return isinstance(t, ast.Name) and t.id == "out"

    body = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "window":
            break
        if isinstance(node, ast.Assign) and any(touches_out(t) for t in node.targets):
            continue
        body.append(node)
    ns = {"__name__": "joint_stress_setup", "__file__": str(path)}
    exec(compile(ast.Module(body=body, type_ignores=[]), str(path), "exec"), ns)
    return ns


def world_house(seed=P.SEED):
    d0, d1, d2, vt3, vt2 = P.draws(P.N, seed)
    H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
    sF, sM = d0 + d1, d0 + d1 + d2
    r = C.rule(H, sF, sM)
    return dict(B=r["bottom"], T=r["top"], b_raw=r["bottom_raw"], t_raw=r["top_raw"], Fz=r["floor_zero"],
                Mz=r["moved_zero"], pay=r["payout"], F=np.asarray(H["floor"], float), contrib=r["gift"],
                excess=r["excess"], R=np.asarray(H["R"], float), fm=np.asarray(H["floor_money"], float),
                mm=np.asarray(H["moved_money"], float), most=np.asarray(H["most_binds"]), vt3=vt3, vt2=vt2,
                sF=sF, sM=sM, label=f"house model, {P.N:,} paths, seed {seed}")


def world_history():
    HS = P.history(c, margin=MARGIN, margin_fn=MF)
    r = C.rule(HS)
    n = len(HS["starts"])
    bc = lambda x: np.broadcast_to(np.asarray(x, float), (n,)).copy()
    w = P.shiller_windows()
    return dict(B=bc(r["bottom"]), T=bc(r["top"]), b_raw=bc(r["bottom_raw"]), t_raw=bc(r["top_raw"]),
                Fz=bc(r["floor_zero"]), Mz=bc(r["moved_zero"]), pay=bc(r["payout"]), F=bc(HS["floor"]),
                contrib=bc(r["gift"]), excess=bc(r["excess"]), R=bc(HS["R"]), fm=bc(HS["floor_money"]),
                mm=bc(HS["moved_money"]), most=np.broadcast_to(np.asarray(HS["most_binds"]), (n,)).copy(),
                vt3=np.array([a for _, a, _ in w]), vt2=np.array([b for _, _, b in w]), starts=HS["starts"],
                label=f"US stock history, {n:,} windows since 1871, rates at today's forwards")


def world_joint(ns):
    J, A = ns["J"], ns["A"]
    Fz, Z = np.asarray(J["floor_zero"], float), np.asarray(J["zero_world"], float)
    return dict(B=np.asarray(J["bottom_stated"], float), T=np.asarray(J["top_stated"], float),
                b_raw=np.asarray(J["bottom_raw"], float), t_raw=np.asarray(J["top_raw"], float), Fz=Fz, Mz=Z - Fz,
                pay=np.asarray(J["gift_realised"], float), F=np.asarray(J["floor_realised"], float),
                contrib=np.asarray(J["gift_capped"], float), excess=np.asarray(J["excess"], float),
                R=np.asarray(J["R"], float), fm=np.asarray(J["floor_money"], float),
                mm=np.asarray(J["moved_money"], float), most=np.asarray(J["most_binds"]),
                vt3=A["vt3"], vt2=A["vt2"], m28=A["m28"], m31=A["m31"], starts=ns["starts"],
                label=f"joint replay, {len(ns['starts'])} windows (Jan 1962 to Sep 2010 starts), each on its own rates")


def pct(a, method="linear", ps=(5, 50, 95)):
    a = np.asarray(a, float)
    return [float(np.percentile(a, p, method=method)) for p in ps]


def stats(a, stated=False):
    """1-in-20 low, median, 1-in-20 high, minimum, maximum. Stated (rounded) figures without interpolation."""
    a = np.asarray(a, float)
    lo, med, hi = pct(a, "lower" if stated else "linear")
    return {"p5": lo, "p50": med, "p95": hi, "min": float(a.min()), "max": float(a.max()), "n": int(a.size)}


def where_min(a, w):
    i = int(np.argmin(a))
    o = {"value": float(a[i]), "index": i, "bottom": float(w["B"][i]), "top": float(w["T"][i]),
         "floor_zero": float(w["Fz"][i]), "moved_zero": float(w["Mz"][i]), "floor_money": float(w["fm"][i]),
         "moved_money": float(w["mm"][i]), "funds_pay": float(w["pay"][i])}
    if "starts" in w:
        o["start"] = w["starts"][i]
    return o


def analyse(w):
    B, T, pay, contrib, exc = w["B"], w["T"], w["pay"], w["contrib"], w["excess"]
    Fz, Mz = w["Fz"], w["Mz"]
    Z = Fz + Mz
    n = B.size
    width = T - B
    o = {"label": w["label"], "paths": int(n)}
    # (i) the contribution less the stated bottom (realised payouts)
    i_ = contrib - B
    o["i_contribution_less_bottom"] = dict(stats(i_, True), count_zero=int((i_ < 0.5).sum()),
                                           share_zero=float((i_ < 0.5).mean()), count_below=int((i_ < -0.5).sum()))
    # the room before the contribution could fall below the bottom: what the funds pay, and their zero-interest
    # payout less 0.5% (card Q4c row 27's measure), each less the stated bottom
    o["room_funds_pay_less_bottom"] = stats(pay - B)
    o["room_zero_interest_less_half_pct_less_bottom"] = stats(Z * (1 - C.HAIRCUT) - B)
    # (ii) the width of the range
    steps = np.round(width / STEP).astype(int)
    o["ii_width"] = dict(stats(width, True), count_zero=int((steps == 0).sum()), share_zero=float((steps == 0).mean()),
                         count_5k=int((steps == 1).sum()), share_5k=float((steps == 1).mean()),
                         distribution={f"{int(k * STEP)}": int(v) for k, v in zip(*np.unique(steps, return_counts=True))})
    zero = steps == 0
    if zero.any():
        o["ii_width"]["where_zero"] = {
            "stated_bottom_p50_min_max": [float(np.median(B[zero])), float(B[zero].min()), float(B[zero].max())],
            "moved_half_zero_interest_p50_max": [float(np.median(Mz[zero])), float(Mz[zero].max())],
            "vt_growth_2028_2031_p50_max": [float(np.median(w["vt3"][zero])), float(w["vt3"][zero].max())],
            "vt_bought_p50": float(np.median((w["R"] - w["fm"])[zero])),
            "share_most_binds": float(w["most"][zero].mean()),
            "excess_p50_min": [float(np.median(exc[zero])), float(exc[zero].min())],
            "count_vt_bought_zero": int(((w["R"] - w["fm"]) < 0.5)[zero].sum()),
            "yield_move_before_jan2028_p50_max": ([float(np.median(w["sF"][zero])), float(w["sF"][zero].max())]
                                                  if "sF" in w else None)}
        if "starts" in w:
            o["ii_width"]["where_zero"]["starts"] = [w["starts"][k] for k in np.flatnonzero(zero)]
    one = steps == 1
    if one.any():
        o["ii_width"]["where_5k"] = {"vt_growth_2028_2031_p50": float(np.median(w["vt3"][one])),
                                     "share_most_binds": float(w["most"][one].mean())}
        if "starts" in w:
            o["ii_width"]["where_5k"]["starts"] = [w["starts"][k] for k in np.flatnonzero(one)]
    # (iii) the contribution less the stated top: realised, and if the funds paid only their holdings' zero-interest
    # payout less a fund cost x (0.5% is the rule's own haircut; 0.75% and 1% go beyond it)
    o["iii_contribution_less_top_realised"] = dict(stats(contrib - T), count_below=int((contrib < T - 0.5).sum()))
    for x in FRICTIONS:
        cx = np.minimum(Z * (1 - x), T)
        short = cx < T - 0.5
        below = cx < B - 0.5
        o[f"iii_zero_interest_less_{x:.4f}"] = {
            "contribution_less_top": stats(cx - T), "count_top_short": int(short.sum()), "share_top_short": float(short.mean()),
            "largest_top_gap": float((T - cx)[short].max()) if short.any() else 0.0,
            "top_gap_p50_where_short": float(np.median((T - cx)[short])) if short.any() else 0.0,
            "contribution_less_bottom": stats(cx - B), "count_below_bottom": int(below.sum()),
            "share_below_bottom": float(below.mean()),
            "largest_gap_below_bottom": float((B - cx)[below].max()) if below.any() else 0.0,
            "floor_alone_short_of_bottom": int((Fz * (1 - x) < B - 0.5).sum())}
    # (iv) the excess
    o["iv_excess"] = dict(stats(exc), count_under_1000=int((exc < 1000).sum()), share_under_1000=float((exc < 1000).mean()))
    # (v) what each end's holdings pay at zero interest, less the stated end; and the realised payouts
    o["v_floor_zero_less_bottom"] = dict(stats(Fz - B), at_min=where_min(Fz - B, w))
    o["v_both_zero_less_top"] = dict(stats(Z - T), at_min=where_min(Z - T, w))
    o["v_floor_pays_less_bottom"] = stats(w["F"] - B)
    o["v_funds_pay_less_top"] = stats(pay - T)
    # the largest fund friction (share of value) that leaves each stated end owned at zero interest in every path
    o["largest_friction_covered_every_path"] = {"bottom": float(np.min(1 - B / Fz)), "top": float(np.min(1 - T / Z))}
    vt = w["R"] - w["fm"]
    o["vt_bought"] = dict(stats(vt), count_zero=int((vt < 0.5).sum()), share_zero=float((vt < 0.5).mean()),
                          count_under_5000=int((vt < STEP).sum()))
    return o


# ---------------------------------------------------------------- route 2: a second calculation

FEE, VFEE = E.ASSUMPTIONS["fund_fee"], E.ASSUMPTIONS["vt_fee"]
SHARE = E.ASSUMPTIONS["floor_share"]
yrs = lambda d2, d1: (d2 - d1).days / 365.25
Pd = c.P                                                   # discount factor from 1 Jan 2027 (the curve, an input)


def months_add(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    return date(d.year + y, mo + 1, d.day)


WAM2 = months_add(date(2026, 11, 4), round(5.65 * 12))     # IBTM's holdings: average maturity 5.65 years on 4 Nov 2026
CDS2 = sorted(d for d in (months_add(WAM2, -6 * k) for k in range(40)) if d > E.J27)
CPN2 = (1 - Pd(WAM2)) / (sum(Pd(d) for d in CDS2) / 2)    # par coupon to the WAM date on the 6 Nov curve
FLOWS2 = [(d, (CPN2 / 2 + (1.0 if d == WAM2 else 0.0)) * (1 - FEE) ** yrs(d, E.J27)) for d in CDS2]
WAITFEE2 = (1 - FEE) ** yrs(END, WAM2)


def zero_payout2(buy, rate_of, etf_fee=0.0):
    """What $1 put into the fund on `buy` pays on 15 Dec 2032 if nothing earns interest: remaining holdings' flows at
    face (principal less the fee while it waits in the fund; distributions less etf_fee a year while they wait outside)
    over their price on the trade day, discounted at rate_of(d) (a per-flow continuously compounded rate, floored at 0)."""
    num = den = 0.0
    for d, a in FLOWS2:
        if d <= buy:
            continue
        t = yrs(d, buy)
        den += a * math.exp(-max(rate_of(d), 0.0) * t)
        num += a * (WAITFEE2 if d == WAM2 else math.exp(-etf_fee * yrs(END, d)))
    return num / den


def zero_payout2_vec(buy, s, etf_fee=0.0):
    """As zero_payout2, vectorised over a parallel move s of today's forwards (house paths)."""
    s = np.asarray(s, float)
    num, den = 0.0, 0.0
    for d, a in FLOWS2:
        if d <= buy:
            continue
        t = yrs(d, buy)
        f = math.log(Pd(buy) / Pd(d)) / t
        den = den + a * np.exp(-np.maximum(f + s, 0.0) * t)
        num = num + a * (WAITFEE2 if d == WAM2 else math.exp(-etf_fee * yrs(END, d)))
    return num / den


def down2(x):
    """Round down to $5,000 in whole dollars by integer division."""
    return np.array([(int(math.floor(v)) // 5000) * 5000 for v in np.ravel(x)], float).reshape(np.shape(x))


def split2(R, vt3):
    fm = np.maximum(SHARE * R, np.minimum(R, 150_000.0 / 2 + 1.0))
    vt31 = (R - fm) * vt3 * (1 - VFEE) ** 3
    return fm, vt31 / 2


tauF2, tauM2 = yrs(END, E.J28), yrs(END, E.J31)
fF2 = math.log(Pd(E.J28) / Pd(END)) / tauF2
fM2 = math.log(Pd(E.J31) / Pd(END)) / tauM2


def route2_house(w):
    fm, mm = split2(w["R"], w["vt3"])
    zF = zero_payout2_vec(E.J28, w["sF"])
    zM = zero_payout2_vec(E.J31, w["sM"])
    Fz, Mz = fm * zF, mm * zM
    F = fm * np.exp(np.maximum(fF2 + w["sF"], 0.001) * tauF2) * (1 - FEE) ** tauF2
    M = mm * np.exp(np.maximum(fM2 + w["sM"], 0.001) * tauM2) * (1 - FEE) ** tauM2
    zFw = zero_payout2_vec(E.J28, w["sF"], C.WAIT_FEE)
    zMw = zero_payout2_vec(E.J31, w["sM"], C.WAIT_FEE)
    return finish2(fm, mm, Fz, Mz, F, F + M, fm * zFw, mm * zMw)


def route2_history(w):
    fm, mm = split2(w["R"], w["vt3"])
    zF = zero_payout2(E.J28, lambda d: math.log(Pd(E.J28) / Pd(d)) / yrs(d, E.J28))
    zM = zero_payout2(E.J31, lambda d: math.log(Pd(E.J31) / Pd(d)) / yrs(d, E.J31))
    zFw = zero_payout2(E.J28, lambda d: math.log(Pd(E.J28) / Pd(d)) / yrs(d, E.J28), C.WAIT_FEE)
    zMw = zero_payout2(E.J31, lambda d: math.log(Pd(E.J31) / Pd(d)) / yrs(d, E.J31), C.WAIT_FEE)
    F = fm * math.exp(fF2 * tauF2) * (1 - FEE) ** tauF2
    M = mm * math.exp(fM2 * tauM2) * (1 - FEE) ** tauM2
    return finish2(fm, mm, fm * zF, mm * zM, F, F + M, fm * zFw, mm * zMw)


def route2_joint(w, ns):
    """Each window's trade-day curve is today's forwards x the window's 1-year yield ratio that month; what the funds
    pay is the holdings' flows (before the fee) grown at the window's rates to 15 Dec 2032 over their trade-day price,
    less the fee over the whole holding (the convention joint_stress.py uses for the realised payout)."""
    mults = {st: m for st, m in E.history_windows(ns["DGS1"], "DGS1")}
    n = len(w["starts"])
    fm, mm = split2(w["R"], w["vt3"])
    out = {k: np.zeros(n) for k in ("zF", "zM", "zFw", "zMw", "pF", "pM")}
    raw = [(d, a / (1 - FEE) ** yrs(d, E.J27)) for d, a in FLOWS2]           # the holdings before the fee
    for k, st in enumerate(w["starts"]):
        m = mults[st]
        for buy, zk, wk, pk in ((E.J28, "zF", "zFw", "pF"), (E.J31, "zM", "zMw", "pM")):
            mb = m(buy)
            rate = lambda d, buy=buy, mb=mb: math.log(Pd(buy) / Pd(d)) / yrs(d, buy) * mb
            out[zk][k] = zero_payout2(buy, rate)
            out[wk][k] = zero_payout2(buy, rate, C.WAIT_FEE)
            grow = lambda d1: (Pd(max(d1, E.J27)) / Pd(END)) ** m(d1) if d1 < END else 1.0
            price = sum(a * math.exp(-max(rate(d), 0.0) * yrs(d, buy)) for d, a in raw if d > buy)
            paid = sum(a * grow(d) for d, a in raw if d > buy)
            out[pk][k] = paid / price * (1 - FEE) ** yrs(END, buy)
    F, M = fm * out["pF"], mm * out["pM"]
    return finish2(fm, mm, fm * out["zF"], mm * out["zM"], F, F + M, fm * out["zFw"], mm * out["zMw"])


def finish2(fm, mm, Fz, Mz, F, pay, Fzw, Mzw):
    Z = Fz + Mz
    B, T = down2(Fz * (1 - C.HAIRCUT)), down2(Z * (1 - C.HAIRCUT))
    contrib = np.minimum(pay, T)
    return dict(fm=fm, mm=mm, Fz=Fz, Mz=Mz, B=B, T=T, F=F, pay=pay, contrib=contrib, excess=pay - contrib,
                Fzw=Fzw, Zw=Fzw + Mzw)


def compare(w, r2):
    """Largest differences between route 1 and route 2, and the headline figures recomputed from route 2."""
    d = {k: float(np.max(np.abs(np.asarray(w[k], float) - np.asarray(r2[k], float))))
         for k in ("fm", "mm", "Fz", "Mz", "B", "T", "F", "pay", "contrib", "excess")}
    width = r2["T"] - r2["B"]
    steps = np.round(width / STEP).astype(int)
    Z = r2["Fz"] + r2["Mz"]
    h = {"stated_ends_differing": int(((np.abs(w["B"] - r2["B"]) > 0.5) | (np.abs(w["T"] - r2["T"]) > 0.5)).sum()),
         "width": stats(width, True), "width_zero": int((steps == 0).sum()), "width_5k": int((steps == 1).sum()),
         "contribution_less_bottom_min": float((r2["contrib"] - r2["B"]).min()),
         "contribution_below_top_realised": int((r2["contrib"] < r2["T"] - 0.5).sum()),
         "excess": stats(r2["excess"]),
         "floor_zero_less_bottom_min": float((r2["Fz"] - r2["B"]).min()),
         "both_zero_less_top_min": float((Z - r2["T"]).min()),
         "funds_pay_less_top_min": float((r2["pay"] - r2["T"]).min()),
         "floor_pays_less_bottom_min": float((r2["F"] - r2["B"]).min())}
    for x in FRICTIONS:
        cx = np.minimum(Z * (1 - x), r2["T"])
        h[f"at_{x:.4f}"] = {"top_short": int((cx < r2["T"] - 0.5).sum()), "below_bottom": int((cx < r2["B"] - 0.5).sum()),
                            "largest_top_gap": float((r2["T"] - cx).max())}
    # the stricter reading: distributions wait in the Treasury-bill ETF at its fee, not at face
    h["etf_wait_fee"] = {"floor_zero_less_bottom": stats(r2["Fzw"] - r2["B"]),
                         "both_zero_less_top": stats(r2["Zw"] - r2["T"]),
                         "bottom_not_owned": int((r2["Fzw"] < r2["B"] - 0.5).sum()),
                         "top_not_owned": int((r2["Zw"] < r2["T"] - 0.5).sum()),
                         "largest_friction_covered_every_path": {"bottom": float(np.min(1 - r2["B"] / r2["Fzw"])),
                                                                 "top": float(np.min(1 - r2["T"] / r2["Zw"]))}}
    return {"largest_abs_difference_route1_vs_route2": d, "route2_headlines": h}


def no_model_checks(w):
    """Checks that need no model: (a) rounding bounds, (b) expected one-figure ranges if the rounding remainder is
    uniform."""
    Fz, Mz, B, T = w["Fz"], w["Mz"], w["B"], w["T"]
    b, z = Fz * (1 - C.HAIRCUT), (Fz + Mz) * (1 - C.HAIRCUT)
    m = Mz * (1 - C.HAIRCUT)
    return {
        "bottom_bounds_broken": int(((Fz - B) < C.HAIRCUT * Fz - 1e-6).sum() + ((Fz - B) >= C.HAIRCUT * Fz + STEP).sum()),
        "top_bounds_broken": int((((Fz + Mz) - T) < C.HAIRCUT * (Fz + Mz) - 1e-6).sum()
                                 + (((Fz + Mz) - T) >= C.HAIRCUT * (Fz + Mz) + STEP).sum()),
        "lowest_possible_floor_margin_0.5pct_of_smallest_floor_zero": float(C.HAIRCUT * Fz.min()),
        "lowest_possible_top_margin_0.5pct_of_smallest_zero_total": float(C.HAIRCUT * (Fz + Mz).min()),
        "width_zero_needs_moved_half_under_5000_after_cut": int((m < STEP).sum()),
        "width_zero_expected_if_remainder_uniform": float(np.maximum(1 - m / STEP, 0.0).sum()),
        "width_zero_actual": int((np.round((T - B) / STEP) == 0).sum()),
        "width_zero_identity_holds": bool(np.all((np.round((T - B) / STEP) == 0) == (np.floor(z / STEP) == np.floor(b / STEP)))),
    }


# ---------------------------------------------------------------- run
out = {"stamp": {"run": "Wed 11 Nov 2026 evening (Sydney)", "curve": E.CURVE_DAY, "design": NAME,
                 "register": "Tue 10 Nov 2026 (NUMBERS 0, 3, 4, 8i)", "haircut": C.HAIRCUT, "step": STEP,
                 "status": "MODEL"}}

cen = P.run(c, margin=MARGIN, margin_fn=MF)
rc = C.rule(cen)
g = lambda a: float(np.asarray(a).item())
Zc = g(rc["zero_world"])
out["central"] = {"bottom": g(rc["bottom"]), "top": g(rc["top"]), "funds_pay": g(rc["payout"]),
                  "contribution": g(rc["gift"]), "excess": g(rc["excess"]),
                  "i_contribution_less_bottom": g(rc["gift"]) - g(rc["bottom"]),
                  "ii_width": g(rc["top"]) - g(rc["bottom"]),
                  "iii_contribution_less_top": g(rc["gift"]) - g(rc["top"]),
                  "iii_at_0.75pct": min(Zc * 0.9925, g(rc["top"])) - g(rc["top"]),
                  "v_floor_zero_less_bottom": g(rc["floor_zero"]) - g(rc["bottom"]),
                  "v_both_zero_less_top": Zc - g(rc["top"]),
                  "room_zero_interest_less_half_pct_less_bottom": g(rc["top_raw"]) - g(rc["bottom"]),
                  "room_funds_pay_less_bottom": g(rc["payout"]) - g(rc["bottom"])}

W = {"house": world_house(), "history": world_history()}
ns = joint_setup()
W["joint"] = world_joint(ns)

for k, w in W.items():
    out[k] = analyse(w)
    out[k]["no_model_checks"] = no_model_checks(w)

# the joint replay reproduces joint_stress's register figures (8i)
JS = json.load(open(HERE / "results_joint_stress_2026-11-10.json"))["joint"]
oj = out["joint"]
out["joint"]["reproduces_8i"] = {
    "floor_zero_less_bottom_min": [oj["v_floor_zero_less_bottom"]["min"], JS["zero_interest_floor_minus_bottom_stated_min"]],
    "both_zero_less_top_min": [oj["v_both_zero_less_top"]["min"], JS["zero_interest_total_minus_top_stated_min"]],
    "floor_pays_less_bottom_min": [oj["v_floor_pays_less_bottom"]["min"], JS["floor_realised_minus_bottom_stated_min"]],
    "funds_pay_less_top_min": [oj["v_funds_pay_less_top"]["min"], JS["gift_realised_minus_top_stated_min_before_cap"]],
    "stated_bottom_p5_p50_p95": [C.qs(W["joint"]["B"]), JS["bottom_stated_p5_p50_p95"]],
    "stated_top_p5_p50_p95": [C.qs(W["joint"]["T"]), JS["top_stated_p5_p50_p95"]],
}

# route 2
R2 = {"house": route2_house(W["house"]), "history": route2_history(W["history"]), "joint": route2_joint(W["joint"], ns)}
out["second_way"] = {k: compare(W[k], R2[k]) for k in R2}
# the stricter reading's cost at the central path, in dollars at each end
zFw_c = zero_payout2(E.J28, lambda d: math.log(Pd(E.J28) / Pd(d)) / yrs(d, E.J28), C.WAIT_FEE)
zF_c = zero_payout2(E.J28, lambda d: math.log(Pd(E.J28) / Pd(d)) / yrs(d, E.J28))
zMw_c = zero_payout2(E.J31, lambda d: math.log(Pd(E.J31) / Pd(d)) / yrs(d, E.J31), C.WAIT_FEE)
zM_c = zero_payout2(E.J31, lambda d: math.log(Pd(E.J31) / Pd(d)) / yrs(d, E.J31))
fmc, mmc = g(cen["floor_money"]), g(cen["moved_money"])
out["second_way"]["etf_wait_fee_central"] = {
    "floor_cost": fmc * (zF_c - zFw_c), "moved_cost": mmc * (zM_c - zMw_c),
    "share_of_floor_zero": 1 - zFw_c / zF_c, "share_of_moved_zero": 1 - zMw_c / zM_c,
    "floor_zero_less_bottom": fmc * zFw_c - g(rc["bottom"]),
    "both_zero_less_top": fmc * zFw_c + mmc * zMw_c - g(rc["top"])}
out["second_way"]["holdings"] = {"coupon_route2": CPN2, "coupon_engine": C.HOLD_COUPON, "wam": WAM2.isoformat(),
                                 "flows": len(FLOWS2)}
# sampling: the house model drawn again with another seed
w34 = world_house(seed=2034)
a34 = analyse(w34)
out["second_way"]["house_seed_2034"] = {
    "width_zero": a34["ii_width"]["count_zero"], "width_5k": a34["ii_width"]["count_5k"],
    "width_p5_p50_p95": [a34["ii_width"]["p5"], a34["ii_width"]["p50"], a34["ii_width"]["p95"]],
    "at_0.75pct_top_short": a34["iii_zero_interest_less_0.0075"]["count_top_short"],
    "at_0.75pct_below_bottom": a34["iii_zero_interest_less_0.0075"]["count_below_bottom"],
    "floor_zero_less_bottom_min": a34["v_floor_zero_less_bottom"]["min"],
    "both_zero_less_top_min": a34["v_both_zero_less_top"]["min"],
    "excess_p5_p50_p95_min": [a34["iv_excess"]["p5"], a34["iv_excess"]["p50"], a34["iv_excess"]["p95"], a34["iv_excess"]["min"]]}

(HERE / f"results_range_margin_2026-11-11{C.tag(NAME)}.json").write_text(json.dumps(out, indent=1, default=float))


# ---------------------------------------------------------------- print
def rnd(x):
    if isinstance(x, dict):
        return {k: rnd(v) for k, v in x.items()}
    if isinstance(x, list):
        return [rnd(v) for v in x]
    if isinstance(x, float):
        return round(x) if abs(x) >= 10 else round(x, 5)
    return x


print("central", json.dumps(rnd(out["central"])))
for k in ("house", "history", "joint"):
    print("=" * 20, k)
    for kk, vv in out[k].items():
        if kk in ("label", "paths"):
            continue
        s = json.dumps(rnd(vv))
        print(" ", kk, s if len(s) < 1500 else s[:1500] + " ...")
print("=" * 20, "second way")
for k, v in out["second_way"].items():
    print(" ", k, json.dumps(rnd(v)))
for k in ("house", "history", "joint"):
    print("  largest differences, unrounded", k,
          {a: f"{b:.2e}" for a, b in out["second_way"][k]["largest_abs_difference_route1_vs_route2"].items()})
