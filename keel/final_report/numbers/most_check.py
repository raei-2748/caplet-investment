"""When can the floor no longer get "most" of the 2028 deposit? (Numbers owner, Fri 13 Nov 2026, Sydney.) MODEL.

IPS l.15: "Most of the 2028 deposit will fund a Treasury fund maturing in late 2032" (the floor). The IPS's order is the
ladder first (l.13), then the floor and VT. Under Keel's call (completion.py: the top-up, $38,282 in January 2028 at
today's forwards) and Keel's reading of "most" (plan.run, most=True: the floor gets the larger of 73.3% of what is left
and $75,001, or all of what is left if that is less), "most" holds exactly when what is left after the ladder and the
top-up is more than half the deposit, so when the top-up costs less than half the deposit.

Run from the repo root:  python3 -I keel/final_report/numbers/most_check.py
Writes keel/final_report/numbers/results_most_2026-11-13.json (about half a minute). Read by NUMBERS.md section 5.

What it finds, on the engine and the register's conventions:
  (a) the fall in yields before 1 Jan 2027 (parallel, the ten and the top-up re-sized exactly on the shifted curve, as
      section 5's table) at which the top-up reaches half the deposit; the same for the ten alone (the IPS's own sizing);
  (b) the same for a fall during 2027 (the ten already bought; the unbought tail and the top-up re-priced in January
      2028, rates floored at zero), alone and after a fall before 1 Jan 2027;
  (c) the smallest 2028 deposit for which "most" holds at today's yields (and after falls before 1 Jan 2027);
  (d) how often it fails: the house model (plan.house, 200,000 paths, seed 2033), the 585 joint windows (1962-2010
      starts, rates in proportion from 1 Jan 2027, as joint_stress.py) and, for the fall before 1 Jan 2027 that no
      replay covers, every 56-day stretch of the 1-year Treasury yield since 1962 (FRED DGS1, daily; 6 Nov to 1 Jan is
      56 days);
  (e) what the plan does then, under the IPS's order: the floor takes all of what is left, VT none.
"""
import json
import math
import sys
from bisect import bisect_right
from datetime import date, timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

DEP = 150_000.0
HALF = DEP / 2
c = C.c
FEE = E.ASSUMPTIONS["fund_fee"]
SHARE = E.ASSUMPTIONS["floor_share"]
DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"
END = date(2032, 12, 15)


def comp0(d0, name=None):
    """January 2028 top-up after a parallel fall d0 before 1 Jan 2027 (section 5's exact re-sizing)."""
    return C.completion_exact(d0, name)[0]


def solve(f, lo, hi, target, tol=1e-7):
    """Bisection for f(x) = target on [lo, hi] with f decreasing in x."""
    flo, fhi = f(lo) - target, f(hi) - target
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(60):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2


# ---------------------------------------------------------------- the January 2028 price of the tail and the top-up
# Both priced as the register does (completion.backstop_price28): flows after 1 Jan 2028 discounted at today's forwards
# moved by `shift`, flows in 2027 counted at face; here rates are floored at zero so that any fall can be priced.
def _flows_after(units):
    after, before = [], 0.0
    for y, u in units.items():
        if u <= 0:
            continue
        for d, a, _ in E.rung_flows(C.I[y], C.BASE):
            if d > E.J28:
                after.append((E.yf(d, E.J28), c.fwd(E.J28, d), u * a))
            else:
                before += u * a
    return after, before


BS_AFTER, BS_BEFORE = _flows_after(C.BACKSTOP)
TAIL_AFTER, TAIL_BEFORE = _flows_after({2033: 1.0})       # per fund dollar of IBTM


def price28(after, before, shift):
    return before + sum(a * math.exp(-max(f + shift, 0.0) * t) for t, f, a in after)


def comp(d0, d1):
    """Top-up in January 2028 after a fall d0 before 1 Jan 2027 and d1 during 2027: the ten and the backstop sized
    exactly on the d0 curve and carried a year at its 2027 rate (section 5), then re-priced for d1 (rates floored at
    zero), as completion.margin_fn re-prices the backstop."""
    b = C.shifted(d0)
    cc = E.Curve(c.par, shift=float(d0)) if d0 else c
    carry = math.exp(cc.fwd(E.J27, E.J28))
    tail = max(b["plain_cost"] - 300_000.0, 0.0)
    back = b[C.CALL]["margin"]
    r_tail = price28(TAIL_AFTER, TAIL_BEFORE, d0 + d1) / price28(TAIL_AFTER, TAIL_BEFORE, d0)
    r_back = price28(BS_AFTER, BS_BEFORE, d0 + d1) / price28(BS_AFTER, BS_BEFORE, d0)
    return (tail * r_tail + back * r_back) * carry


out = {"stamp": {"run": "Fri 13 Nov 2026 (Sydney)", "design": C.CALL, "curve": E.CURVE_DAY, "deposit_2028": DEP,
                 "most_means": "the floor gets more than half the 2028 deposit (more than $75,000)",
                 "keel_reading": "floor = max(73.3% of what is left, min(what is left, $75,001)); VT the rest"}}

# ---------------------------------------------------------------- (a) a fall before 1 Jan 2027
fa = lambda x: comp0(-x)                                 # increasing in the fall x
a_call = solve(lambda x: -fa(x), 0.005, 0.03, -HALF)
a_plain = solve(lambda x: -comp0(-x, "plain"), 0.005, 0.035, -HALF)
guard = solve(lambda x: -fa(x), 0.0, 0.02, -(DEP - 75_001 / SHARE))   # where Keel's $75,001 starts to bind
out["a_fall_before_jan2027"] = {
    "points_where_topup_reaches_half_the_deposit": 100 * a_call,
    "topup_at_that_fall": fa(a_call),
    "points_where_the_ten_alone_reach_half_the_deposit_ips_own_sizing": 100 * a_plain,
    "points_where_keel_75001_starts_to_bind": 100 * guard,
    "topup_where_75001_starts_to_bind": DEP - 75_001 / SHARE,
    "grid": {f"{x:.2f}": {"topup": comp0(-x / 100), "left": DEP - comp0(-x / 100),
                          "floor_share_of_deposit": min(max(SHARE * (DEP - comp0(-x / 100)),
                                                            min(DEP - comp0(-x / 100), HALF + 1)), DEP) / DEP}
             for x in (0.0, 0.5, 1.0, 1.25, 1.5, 1.75, 2.0)},
}

# ---------------------------------------------------------------- (b) a fall during 2027
z = -0.10                                                   # every rate floored at zero
out["b_fall_during_2027"] = {
    "check_register_section5": {f"{x}pt": comp(0.0, -x / 100) for x in (0.5, 1, 2)},
    "topup_if_every_rate_is_zero_in_jan2028": comp(0.0, z),
    "left_then": DEP - comp(0.0, z),
    "most_holds_after_any_fall_during_2027_alone": bool(comp(0.0, z) < HALF),
    "points_during_2027_alone_where_keel_75001_starts_to_bind":
        100 * solve(lambda x: -comp(0.0, -x), 0.0, 0.06, -(DEP - 75_001 / SHARE)),
    "after_a_fall_before_jan2027": {},
}
for x0 in (0.5, 1.0):
    if comp(-x0 / 100, z) <= HALF:
        out["b_fall_during_2027"]["after_a_fall_before_jan2027"][f"{x0}pt"] = {"points_during_2027": None,
                                                                              "topup_at_zero": comp(-x0 / 100, z)}
        continue
    x1 = solve(lambda x: -comp(-x0 / 100, -x), 0.0, 0.06, -HALF)
    out["b_fall_during_2027"]["after_a_fall_before_jan2027"][f"{x0}pt"] = {
        "points_during_2027": 100 * x1, "total_points": x0 + 100 * x1}

# ---------------------------------------------------------------- (c) the smallest deposit
t0 = comp0(0.0)
out["c_smallest_deposit"] = {
    "topup_today": t0,
    "smallest_deposit_today": 2 * t0,          # left = deposit - top-up > deposit / 2  <=>  deposit > 2 x top-up
    "as_share_of_150000": 2 * t0 / DEP,
    "after_falls_before_jan2027": {f"{x}pt": 2 * comp0(-x / 100) for x in (0.5, 1.0)},
    "deposit_below_which_keel_75001_binds_today": (SHARE * t0 + 1) / (SHARE - 0.5),
}

# ---------------------------------------------------------------- (d) how often
mf = C.margin_fn()
S0 = P.setup(c)
h = P.house(c, margin_fn=mf)
d0, d1 = h["draws"][0], h["draws"][1]
fails = h["R"] <= HALF
out["d_how_often"] = {"house": {
    "paths": int(fails.size), "paths_failing": int(fails.sum()), "share_failing": float(fails.mean()),
    "share_keel_75001_binds": float(h["most_binds"].mean()),
    "largest_topup": float(h["complete"].max()),
    "share_fall_before_jan2027_beyond_a": float((d0 <= -a_call).mean()),
    "failing_paths_d0_d1_points": [[round(100 * float(x), 3), round(100 * float(y), 3)]
                                   for x, y in zip(d0[fails], d1[fails])],
}}
# plan.run prices the ten's cost after a fall before 1 Jan 2027 by duration; re-sized exactly (section 5's way, on
# completion.D0_GRID), the unbought tail is a little dearer after a large fall and two more paths fail
_g = C.D0_GRID
_tail_exact = np.interp(d0, _g, [max(C.shifted(x)["plain_cost"] - 300_000.0, 0.0) for x in _g])
_tail_dur = np.maximum(S0["c27"] * np.exp(-S0["dur_l"] * d0) - 300_000.0, 0.0)
_corr = (_tail_exact - _tail_dur) * np.exp(-S0["tail_dur"] * d1) * np.exp(np.maximum(S0["f01"] + d0, 0.001))
out["d_how_often"]["house"]["paths_failing_with_the_tail_resized_exactly"] = int((h["R"] - _corr <= HALF).sum())
# the 585 joint windows (joint_stress.py's method: rates from 1 Jan 2027 at today's forwards x the window's ratio)
S = P.setup(c)
rows = []
for st, m in E.history_windows(DGS1, "DGS1"):
    m28 = m(E.J28)
    r = P.run(c, d0=0.0, d1=S["fF"] * (m28 - 1), margin_fn=C.margin_fn_mult(C.CALL, m28))
    rows.append((st, float(r["complete"]), float(r["R"]), bool(r["most_binds"])))
comp_w = np.array([x[1] for x in rows])
out["d_how_often"]["joint_windows"] = {
    "windows": len(rows), "first": rows[0][0], "last": rows[-1][0],
    "windows_failing": int(sum(x[2] <= HALF for x in rows)),
    "windows_keel_75001_binds": int(sum(x[3] for x in rows)),
    "largest_topup": float(comp_w.max()), "largest_topup_start": rows[int(comp_w.argmax())][0],
    "smallest_left": float(DEP - comp_w.max())}
# every 56-day stretch since 1962 (6 Nov 2026 to 1 Jan 2027 is 56 days): did the 1-year yield fall by a's points, or by
# the same share of its level (a / 4.33, the 1-year par yield of 6 Nov), the history replays' proportional method?
ds, ys = [], []
for line in open(DGS1).read().splitlines()[1:]:
    k, v = line.split(",")
    if v not in ("", "."):
        ds.append(date.fromisoformat(k))
        ys.append(float(v))
ys = np.array(ys)
one_year = c.par[1]
falls_pt, falls_prop, starts, levels = [], [], [], []
for i, d in enumerate(ds):
    j = bisect_right(ds, d + timedelta(days=56)) - 1
    if ds[-1] < d + timedelta(days=56):
        break
    falls_pt.append(ys[i] - ys[j])
    falls_prop.append((ys[i] - ys[j]) / ys[i])
    starts.append(d)
    levels.append(ys[i])
falls_pt, falls_prop, levels = np.array(falls_pt), np.array(falls_prop), np.array(levels)
near = (levels >= 3.0) & (levels <= 6.0)                    # a 1-year yield near today's 4.33%
thr_pt, thr_prop = 100 * a_call, 100 * a_call / one_year


def episodes(mask):
    """Years in which any 56-day stretch starting that year passed the threshold."""
    return sorted({starts[i].year for i in np.flatnonzero(mask)})


def runs(mask):
    """Episodes: stretches passing the threshold whose starts lie within 60 days of each other, with the largest fall
    and the 1-year yield at the first start."""
    eps, last = [], None
    for i in np.flatnonzero(mask):
        d = starts[i]
        if last is not None and (d - last).days <= 60:
            eps[-1]["last_start"] = d.isoformat()
            eps[-1]["largest_fall_points"] = max(eps[-1]["largest_fall_points"], float(falls_pt[i]))
        else:
            eps.append({"first_start": d.isoformat(), "last_start": d.isoformat(),
                        "largest_fall_points": float(falls_pt[i]), "yield_at_first_start": float(levels[i])})
        last = d
    return eps


out["d_how_often"]["history_56_days_dgs1"] = {
    "stretches": int(falls_pt.size), "first_start": starts[0].isoformat(), "last_start": starts[-1].isoformat(),
    "threshold_points": thr_pt, "share_falling_by_threshold_points": float((falls_pt >= thr_pt).mean()),
    "years_points": episodes(falls_pt >= thr_pt),
    "threshold_share_of_level": thr_prop, "one_year_par_6nov": one_year,
    "share_falling_by_threshold_share": float((falls_prop >= thr_prop).mean()),
    "years_share": episodes(falls_prop >= thr_prop),
    "share_falling_half_a_point_or_more": float((falls_pt >= 0.5).mean()),
    "episodes_points": runs(falls_pt >= thr_pt),
    "stretches_starting_at_3_to_6pct": int(near.sum()),
    "share_falling_by_threshold_points_from_3_to_6pct": float((near & (falls_pt >= thr_pt)).sum() / near.sum()),
    "stretches_starting_1_to_15_nov": int(sum(1 for d in starts if d.month == 11 and d.day <= 15)),
    "of_which_falling_by_threshold_points": int(sum(1 for d, x in zip(starts, falls_pt)
                                                     if d.month == 11 and d.day <= 15 and x >= thr_pt)),
}

# ---------------------------------------------------------------- (e) what the plan does then
tauF = E.yf(END, E.J28)


def at_fall(x):
    """The plan after a parallel fall of x (points/100) before 1 Jan 2027, with the full deposit, under the IPS's order."""
    cc = E.Curve(c.par, shift=-x)
    t = comp0(-x)
    left = DEP - t
    fm = max(SHARE * left, min(left, HALF + 1.0))
    vt = left - fm
    payout = fm * math.exp(cc.fwd(E.J28, END) * tauF) * (1 - FEE) ** tauF
    braw = fm * float(C.zero_per_dollar(E.J28, -x)) * (1 - C.HAIRCUT)
    bottom = float(C.down(braw))
    top = bottom if vt == 0 else None      # with no VT the top is the bottom: the range is one figure
    return {"fall_points": 100 * x, "topup": t, "topup_share_of_deposit": t / DEP, "left": left, "floor_money": fm,
            "floor_share_of_deposit": fm / DEP, "floor_share_of_what_is_left": fm / left, "vt_bought": vt,
            "floor_payout": payout, "stated_bottom": bottom, "stated_top_if_no_vt": top,
            "contribution_if_no_vt": min(payout, bottom) if vt == 0 else None,
            "excess_if_no_vt": payout - bottom if vt == 0 else None,
            "frozen_split_instead_vt": (1 - SHARE) * left}


out["e_what_the_plan_does"] = {"at_threshold": at_fall(a_call), "at_1.5pt": at_fall(0.015), "at_2pt": at_fall(0.02)}

(HERE / "results_most_2026-11-13.json").write_text(json.dumps(out, indent=1, default=str))

k = C.fmt
A, B, Cc, D = (out[x] for x in ("a_fall_before_jan2027", "b_fall_during_2027", "c_smallest_deposit", "d_how_often"))
print(f"(a) before Jan 2027: 'most' fails at a {A['points_where_topup_reaches_half_the_deposit']:.3f}-point fall "
      f"(top-up {k(A['topup_at_that_fall'])}); ten alone at {A['points_where_the_ten_alone_reach_half_the_deposit_ips_own_sizing']:.3f}; "
      f"$75,001 binds from {A['points_where_keel_75001_starts_to_bind']:.3f}")
for x, v in A["grid"].items():
    print(f"    {x} pt: top-up {k(v['topup'])} left {k(v['left'])} floor share {v['floor_share_of_deposit']:.1%}")
print(f"(b) during 2027: section 5 check {[round(v) for v in B['check_register_section5'].values()]}; "
      f"at zero rates top-up {k(B['topup_if_every_rate_is_zero_in_jan2028'])}, left {k(B['left_then'])}; "
      f"$75,001 binds from {B['points_during_2027_alone_where_keel_75001_starts_to_bind']:.2f} pt during 2027; "
      f"after falls before: {B['after_a_fall_before_jan2027']}")
print(f"(c) smallest deposit today {k(Cc['smallest_deposit_today'])} ({Cc['as_share_of_150000']:.1%}); "
      f"after 0.5/1 pt {[k(v) for v in Cc['after_falls_before_jan2027'].values()]}; "
      f"$75,001 binds below {k(Cc['deposit_below_which_keel_75001_binds_today'])}")
hd = D["house"]
print(f"(d) house {hd['paths_failing']} of {hd['paths']} ({hd['share_failing']:.5%}); binds {hd['share_keel_75001_binds']:.1%}; "
      f"largest top-up {k(hd['largest_topup'])}; d0 beyond a: {hd['share_fall_before_jan2027_beyond_a']:.5%}; "
      f"failing (d0, d1): {hd['failing_paths_d0_d1_points'][:20]}")
jw = D["joint_windows"]
print(f"    house with the tail re-sized exactly: {hd['paths_failing_with_the_tail_resized_exactly']} fail")
print(f"    joint {jw['windows_failing']} of {jw['windows']} fail, {jw['windows_keel_75001_binds']} bind; largest top-up "
      f"{k(jw['largest_topup'])} ({jw['largest_topup_start']})")
hh = D["history_56_days_dgs1"]
print(f"    56-day stretches {hh['stretches']} ({hh['first_start']} to {hh['last_start']}): fall >= {hh['threshold_points']:.2f} pt "
      f"{hh['share_falling_by_threshold_points']:.2%} {hh['years_points']}; >= {hh['threshold_share_of_level']:.1%} of level "
      f"{hh['share_falling_by_threshold_share']:.2%} {hh['years_share']}; >= 0.5 pt {hh['share_falling_half_a_point_or_more']:.1%}")
print(f"    episodes {len(hh['episodes_points'])}; from 3-6%: {hh['share_falling_by_threshold_points_from_3_to_6pct']:.3%} of "
      f"{hh['stretches_starting_at_3_to_6pct']}; 1-15 Nov starts {hh['of_which_falling_by_threshold_points']} of "
      f"{hh['stretches_starting_1_to_15_nov']}")
for e in hh["episodes_points"]:
    print("     ", e)
for lab, v in out["e_what_the_plan_does"].items():
    print("(e)", lab, {a: (round(b, 4) if isinstance(b, float) and abs(b) < 10 else (round(b) if isinstance(b, float) else b))
                       for a, b in v.items()})
