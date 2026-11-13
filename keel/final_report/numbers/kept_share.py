"""Keeping 30%, half or 70% of the shares: the trade-off the IPS chose (Keel numbers owner, Sat 14 Nov 2026, Sydney).
MODEL, not a forecast, not a promise and not a recommendation. NUMBERS 8o; card Q5b.

Run from the repo root:  python3 -I keel/final_report/numbers/kept_share.py
   or from this folder:  python3 -I kept_share.py
Writes keel/final_report/numbers/results_kept_share_2026-11-14.json and prints the figures (about 15 seconds, numpy
only). Reads results_2026-11-10.json, results_kept_half_2026-11-10.json, results_joint_stress_2026-11-10.json and
results_share_split_2026-11-12.json only to show the checks; writes nothing else; changes no other script.

The claim tested: "Keeping half of the shares unpromised (IPS l.15) is a sound split between what Laura can promise
co-sponsors in 2031 and what she keeps for the three named uses (cost overruns, a stronger Taiwan dollar, a co-sponsor
falling short). Moving 70% of VT (keeping 30%) or moving 30% (keeping 70%) would be worse on balance."
The frozen IPS says "half of the value of the shares will be promised to no one ... Before you meet co-sponsors in
2031, the other half will move into Treasuries" (l.15). The other two splits are benchmarks that show the trade-off the
IPS chose, never a recommendation to change it.

What changes, and only that: the fraction of VT moved into the late-2032 Treasury fund before the 2031 meetings.
  move70  70% moved, 30% kept (her flexibility is 30% of the shares)
  plan    50% moved, 50% kept (IPS l.15); must reproduce NUMBERS 4, 8f, 8i, 8j, 8k and 8n's option B to the dollar
  move30  30% moved, 70% kept
Everything else is the plan exactly as plan.run buys it: the ten, the top-up and the extra Treasuries, the floor (Keel's
reading of "most", NUMBERS 0) and VT in January 2028; the move on 1 Jan 2031. plan.run moves exactly half, so this
script takes its output and scales the moved half and the kept half in proportion (both are linear in VT's value on
the move day): moved money = VT on 1 Jan 2031 x f; what the moved part pays = plan.run's moved half x 2f; the shares
kept on 1 Jan 2033 = plan.run's half kept x 2(1 - f). At f = 0.5 both multipliers are exactly 1, so the plan's figures
are plan.run's own. Then completion.rule states the range on the same rule (each end = the money put into the late-2032
fund x what $1 of its holdings pays on 15 Dec 2032 if nothing earns interest from the trade day, less 0.5%, rounded
down to $5,000); the 2033 facility contribution is the lower of what the floor and the moved part pay and the stated
top; anything above the top joins her flexibility (CANON D12).

Names (WORDS.md): "her flexibility" = the shares not moved, promised to no one, on 1 Jan 2033; "her flexibility plus
anything above the top" = that plus what the funds pay above the stated top. Facility costs are out of scope: shares of
the stated top are percentages only, never Laura's building cost.

Three bases, built exactly as share_split.py and range_margin.py build them (route 1):
  house    plan.draws + plan.run + completion.rule (200,000 simulated futures, seed 2033);
  history  plan.shiller_windows + plan.run + completion.rule (1,770 US stock windows since 1871, rates at today's
           forwards);
  joint    joint_stress.py's own setup code, run from its source up to its first results block (nothing it writes is
           run), then its plan_path re-done with the move fraction applied (585 windows, Jan 1962 to Sep 2010 starts).
Plus 8j's real Taiwan dollar test (Fed G.5 monthly, the repo mirror, 417 windows, VT bought Oct 1983 to Jun 2018) on
the history basis, exactly as joint_stress.py block twd_test builds it.
"""
import ast
import csv
import json
import sys
import time
from datetime import date
from pathlib import Path

import numpy as np

T0 = time.perf_counter()
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
DEPOSIT = 150_000.0
END = date(2032, 12, 15)
TWD = 0.10                         # 10% more US dollars for the same NT$ budget (NUMBERS 8d, 8j)
TWD_STRICT = 1 / 0.9 - 1           # NT$ per US$ down 10%: 11.1% more US dollars (8j's stricter reading)
SHARES_OF_CONTRIB = (0.10, 0.13, 0.17, 0.20, 0.30)   # as joint_stress.twd_test (13% / 17%: Q5's overrun norms, illustration)

MOVES = {
    "move70": dict(f=0.7, label="Move 70% of the shares into Treasuries before the 2031 meetings; keep 30%"),
    "plan": dict(f=0.5, label="The plan (IPS l.15): move half, keep half promised to no one"),
    "move30": dict(f=0.3, label="Move 30%; keep 70%"),
}
FRONTIER = [round(x, 2) for x in np.arange(0.0, 1.0001, 0.05)]


# ---------------------------------------------------------------- the joint replay's setup (as range_margin.py)

def joint_setup():
    """Run joint_stress.py's own top-level code up to its first results block (def window), skipping every statement
    that assigns to its `out` dict; nothing is written. Returns its namespace (J, A, starts, keys, kpos, TWD, ...).
    Copied from range_margin.py and share_split.py unchanged."""
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


# ---------------------------------------------------------------- the one change: the fraction moved

def refrac(res, f):
    """plan.run output with a fraction f of VT moved before the 2031 meetings instead of half. Only the moved part and
    the kept part change, in proportion to VT's value on the move day; the floor, VT bought and all before are as
    plan.run bought them. At f = 0.5 the multipliers are exactly 1 and 0.5, so the plan is plan.run's own output."""
    o = dict(res)
    o["moved_money"] = np.asarray(res["vt31"], float) * f
    o["moved"] = np.asarray(res["moved"], float) * (2 * f)
    o["kept33"] = np.asarray(res["kept33"], float) * (2 * (1 - f))
    o["top"] = np.asarray(res["floor"], float) + o["moved"]
    o["total"] = o["top"] + o["kept33"]
    return o


def finish(res, r, pay, n, topup, extra=None):
    """Common outputs, broadcast to n futures. res: refrac output; r: completion.rule output; pay: what the floor and
    the moved part pay; topup: what comes back from the top-up and the extra Treasuries (1 Jan 2033 money)."""
    bc = lambda x: np.broadcast_to(np.asarray(x, float), (n,)).copy()
    B, T, pay = bc(r["bottom"]), bc(r["top"]), bc(pay)
    contrib = np.minimum(pay, T)
    excess = pay - contrib
    kept = bc(res["kept33"])
    o = dict(bottom=B, top=T, bottom_raw=bc(r["bottom_raw"]), top_raw=bc(r["top_raw"]), width=T - B, pay=pay,
             contrib=contrib, excess=excess, flex=kept, flexa=kept + excess, cf=contrib + kept + excess,
             topup=bc(topup), vt31=bc(res["vt31"]), moved=bc(res["moved"]), floor_pay=bc(res["floor"]),
             floor_money=bc(res["floor_money"]), vt28=bc(res["vt28"]))
    if extra:
        o.update({k: bc(v) for k, v in extra.items()})
    return o


def run_central(f, topup, g):
    res = refrac(P.run(c, margin=MARGIN, margin_fn=MF), f)
    r = C.rule(res)
    o = finish(res, r, res["top"], 1, topup)
    o["returns_8k"] = o["excess"] * g + o["flex"] + o["topup"]       # 8k: the excess carried 17 days at forwards
    return o


def run_house(f, draws, topup):
    d0, d1, d2, vt3, vt2 = draws
    res = refrac(P.run(c, MARGIN, None, DEPOSIT, d0, d1, d2, vt3, vt2, MF), f)
    r = C.rule(res, d0 + d1, d0 + d1 + d2)
    return finish(res, r, r["payout"], d0.size, topup, {"vt2": vt2})


def run_history(f, w, topup):
    vt3 = np.array([a for _, a, _ in w])
    vt2 = np.array([b for _, _, b in w])
    res = refrac(P.run(c, MARGIN, None, DEPOSIT, vt3=vt3, vt2=vt2, margin_fn=MF), f)
    r = C.rule(res)
    o = finish(res, r, r["payout"], len(w), topup, {"vt2": vt2})
    o["starts"] = [k for k, _, _ in w]
    return o


def run_joint(f, ns):
    """joint_stress.plan_path (H_plain branch) with the move fraction applied, then its realised payouts and the cap."""
    A = ns["A"]
    m28, m31 = np.asarray(A["m28"], float), np.asarray(A["m31"], float)
    fF, fM = ns["fF"], ns["fM"]
    d1 = fF * (m28 - 1)
    d2 = fM * m31 - fM - d1
    mf = C.margin_fn_mult(NAME, m28)
    res = refrac(P.run(c, margin=MARGIN, d0=0.0, d1=d1, d2=d2, vt3=A["vt3"], vt2=A["vt2"], margin_fn=mf), f)
    r = C.rule(res, mF=m28, mM=m31)
    floor_real = np.asarray(res["floor"], float) * A["floor_real_ratio"]
    moved_real = np.asarray(res["moved"], float) * A["moved_real_ratio"]
    o = finish(res, r, floor_real + moved_real, m28.size, A["overflow_jan2033_value"], {"vt2": A["vt2"]})
    g = np.asarray(A["g_end_j33"], float)
    o["returns_8k"] = o["excess"] * g + o["flex"] + o["topup"]       # 8k's convention, each window's own rate
    o["starts"] = list(ns["starts"])
    return o


# ---------------------------------------------------------------- summaries

def pl(a, ps=(5, 50, 95)):
    a = np.asarray(a, float)
    return [float(np.nanpercentile(a, p)) for p in ps]


def twd(pot, contrib):
    """8j's test on one pot: does it cover the extra US dollars a stronger Taiwan dollar needs on the contribution?"""
    pot, contrib = np.asarray(pot, float), np.asarray(contrib, float)
    d = {}
    for tag, x in (("10pct", TWD), ("strict_11.1pct", TWD_STRICT)):
        ok = pot >= contrib * x
        gap = (contrib * x - pot)[~ok]
        d[f"covers_{tag}"] = float(ok.mean())
        d[f"fails_count_{tag}"] = int((~ok).sum())
        d[f"gap_when_fails_p50_p95_max_{tag}"] = ([float(np.median(gap)), float(np.percentile(gap, 95)),
                                                   float(gap.max())] if gap.size else [0.0, 0.0, 0.0])
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(contrib > 0, pot / np.where(contrib > 0, contrib, 1.0), np.nan)
    d["largest_stronger_twd_covered_19_in_20"] = float(np.nanpercentile(ratio, 5))
    d["covers_share_of_contribution"] = {f"{x:.2f}": float((pot >= contrib * x).mean()) for x in SHARES_OF_CONTRIB}
    return d


def summary(o):
    n = o["pay"].size
    inside = (o["contrib"] >= o["bottom"] - 0.5) & (o["contrib"] <= o["top"] + 0.5)
    with np.errstate(divide="ignore", invalid="ignore"):
        rf = np.where(o["top"] > 0, o["flex"] / np.where(o["top"] > 0, o["top"], 1.0), np.nan)
        rfa = np.where(o["top"] > 0, o["flexa"] / np.where(o["top"] > 0, o["top"], 1.0), np.nan)
    fell = o["vt2"] < 1.0
    s = {
        "futures": int(n),
        "stated_bottom_p5_p50_p95": C.qs(o["bottom"]),
        "stated_top_p5_p50_p95": C.qs(o["top"]),
        "width_p5_p50_p95": C.qs(o["width"]),
        "share_width_zero_one_figure": float((o["width"] < 0.5).mean()),
        "count_width_zero_one_figure": int((o["width"] < 0.5).sum()),
        "share_width_5k_or_less": float((o["width"] < 5_000.5).mean()),
        "contribution_p5_p50_p95": C.qs(o["contrib"]),
        "contribution_min": float(o["contrib"].min()),
        "share_contribution_inside_stated_range": float(inside.mean()),
        "share_contribution_equals_stated_top": float((np.abs(o["contrib"] - o["top"]) < 0.5).mean()),
        "funds_pay_p5_p50_p95": pl(o["pay"]),
        "excess_p5_p50_p95": pl(o["excess"]),
        "flexibility_p1_p5_p50_p95": pl(o["flex"], (1, 5, 50, 95)),
        "flexibility_min": float(o["flex"].min()),
        "flexibility_plus_above_top_p1_p5_p50_p95": pl(o["flexa"], (1, 5, 50, 95)),
        "flexibility_plus_above_top_min": float(o["flexa"].min()),
        "flexibility_median_if_shares_fell_2031_2033": float(np.median(o["flex"][fell])) if fell.any() else None,
        "flexibility_plus_above_top_median_if_shares_fell_2031_2033": (float(np.median(o["flexa"][fell]))
                                                                       if fell.any() else None),
        "share_shares_fell_2031_2033": float(fell.mean()),
        "flexibility_over_stated_top_p5_p50_p95": pl(rf),
        "flexibility_over_funds_pay_p5_p50_p95": pl(o["flex"] / o["pay"]),
        "flexibility_plus_above_top_over_stated_top_p5_p50_p95": pl(rfa),
        "contribution_plus_flexibility_plus_above_top_p5_p50_p95": pl(o["cf"]),
        "vt_on_move_day_p5_p50_p95": pl(o["vt31"]),
        "twd_flexibility": twd(o["flex"], o["contrib"]),
        "twd_flexibility_plus_above_top": twd(o["flexa"], o["contrib"]),
    }
    if "returns_8k" in o:
        s["returns_to_laura_8k_p5_p50_p95"] = pl(o["returns_8k"])
    if "starts" in o:
        st = o["starts"]
        for key, arr in (("flexibility", o["flex"]), ("flexibility_plus_above_top", o["flexa"]),
                         ("contribution", o["contrib"])):
            i = int(np.argmin(arr))
            ties = np.flatnonzero(arr <= arr[i] + 0.5)
            s[f"worst_{key}"] = {"value": float(arr[i]), "start": st[i], "stated_bottom": float(o["bottom"][i]),
                                 "stated_top": float(o["top"][i]), "windows_at_minimum": int(ties.size),
                                 "starts_at_minimum_first_12": [st[t] for t in ties[:12]]}
    return s


def versus(o, b):
    """This split against the plan, future by future."""
    dc, df, dfa, dcf = o["contrib"] - b["contrib"], o["flex"] - b["flex"], o["flexa"] - b["flexa"], o["cf"] - b["cf"]
    return {"contribution_difference_p5_p50_p95": pl(dc),
            "share_contribution_above_plan": float((dc > 0.5).mean()),
            "share_contribution_below_plan": float((dc < -0.5).mean()),
            "share_contribution_same_as_plan": float((np.abs(dc) <= 0.5).mean()),
            "flexibility_difference_p5_p50_p95": pl(df),
            "flexibility_plus_above_top_difference_p5_p50_p95": pl(dfa),
            "total_difference_p5_p50_p95": pl(dcf),
            "share_total_above_plan": float((dcf > 0.5).mean())}


def real_twd(o, ns, w):
    """8j's real Taiwan dollar test on the history basis, exactly as joint_stress.py builds it: the move in NT$ per US$
    from the meetings (VT purchase + 36 months) to the gift (+ 60 months), on each window's contribution."""
    keys, kpos = ns["keys"], ns["kpos"]
    fx = {r["Date"][:7]: float(r["TWD_per_USD"]) for r in csv.DictReader(open(ns["TWD"]))}
    sel, cost, st_fx = [], [], []
    for i, (st, _, _) in enumerate(w):
        j0 = kpos[st]
        if j0 + 60 < len(keys) and keys[j0 + 36] in fx and keys[j0 + 60] in fx and st >= "1983-10":
            sel.append(i)
            cost.append(fx[keys[j0 + 36]] / fx[keys[j0 + 60]] - 1)
            st_fx.append(st)
    sel, cost = np.array(sel), np.array(cost)
    cc = o["contrib"][sel]
    out = {"windows": int(sel.size), "first_vt_purchase": st_fx[0], "last_vt_purchase": st_fx[-1],
           "contribution_p5_p50_p95": C.qs(cc)}
    for name, pot in (("flexibility", o["flex"][sel]), ("flexibility_plus_above_top", o["flexa"][sel])):
        gap = cc * np.maximum(cost, 0.0) - pot
        bad = gap > 0
        out[name] = {"covers_actual_move": float((~bad).mean()), "fails_count": int(bad.sum()),
                     "fails_starts": [s for s, b in zip(st_fx, bad) if b],
                     "gap_when_fails_p50_max": ([float(np.median(gap[bad])), float(gap[bad].max())]
                                                if bad.any() else [0.0, 0.0])}
    return out


# ---------------------------------------------------------------- run
out = {"stamp": {"run": "Sat 14 Nov 2026 (Sydney)", "curve": E.CURVE_DAY, "design": NAME,
                 "register": "Tue 10 Nov 2026 (NUMBERS 0, 3, 4, 8f, 8i, 8j, 8k, 8l, 8n)", "haircut": C.HAIRCUT,
                 "step": C.STEP, "seed": P.SEED, "futures": P.N,
                 "status": "MODEL; benchmarks of the split the frozen IPS chose (l.15), not a recommendation",
                 "splits": {k: v["label"] for k, v in MOVES.items()},
                 "names": "flexibility = the shares not moved, on 1 Jan 2033 (WORDS: her flexibility); "
                          "flexibility_plus_above_top = that plus what the funds pay above the stated top",
                 "conventions": "contribution, excess and flexibility at face (15 Dec 2032 / 1 Jan 2033), as NUMBERS 4; "
                                "stated figures and the contribution read without interpolation (method 'lower'), "
                                "others linear; Taiwan dollar test as NUMBERS 8j (10% = 10% more US dollars on the "
                                "contribution; strict = NT$ per US$ down 10%); returns_to_laura as NUMBERS 8k"}}

_, _, _, left_fw = C.ledger(C.BASE, DSG["own"], DSG["pool"])
TOPUP_FW = float(C.in_2033_money(left_fw, C.BASE))
G_FW = float(C.BASE.grow(END, E.J33))
out["topup_return_forwards_jan2033"] = TOPUP_FW

draws = P.draws(P.N, P.SEED)
W_HIST = P.shiller_windows()
ns = joint_setup()
W = {}
for k, m in MOVES.items():
    W[k] = {"central": run_central(m["f"], TOPUP_FW, G_FW), "house": run_house(m["f"], draws, TOPUP_FW),
            "history": run_history(m["f"], W_HIST, TOPUP_FW), "joint": run_joint(m["f"], ns)}

res = {}
for k, m in MOVES.items():
    cen = W[k]["central"]
    g = lambda a: float(np.asarray(a).ravel()[0])
    res[k] = {"label": m["label"], "fraction_moved": m["f"], "fraction_kept": round(1 - m["f"], 10),
              "central_today": {
                  "stated_bottom": g(cen["bottom"]), "stated_top": g(cen["top"]),
                  "bottom_raw": g(cen["bottom_raw"]), "top_raw": g(cen["top_raw"]), "width": g(cen["width"]),
                  "funds_pay": g(cen["pay"]), "contribution": g(cen["contrib"]), "excess": g(cen["excess"]),
                  "flexibility": g(cen["flex"]), "flexibility_plus_above_top": g(cen["flexa"]),
                  "contribution_plus_flexibility_plus_above_top": g(cen["cf"]),
                  "flexibility_over_stated_top": g(cen["flex"]) / g(cen["top"]),
                  "flexibility_plus_above_top_over_stated_top": g(cen["flexa"]) / g(cen["top"]),
                  "twd_10pct_need": g(cen["contrib"]) * TWD,
                  "twd_10pct_flexibility_cover_multiple": g(cen["flex"]) / (g(cen["contrib"]) * TWD),
                  "twd_10pct_flexibility_plus_above_top_cover_multiple": g(cen["flexa"]) / (g(cen["contrib"]) * TWD),
                  "moved_money_2031": g(cen["vt31"]) * m["f"], "moved_pays": g(cen["moved"]),
                  "returns_to_laura_8k": g(cen["returns_8k"])}}
    for b in ("house", "history", "joint"):
        res[k][b] = summary(W[k][b])
        if k != "plan":
            res[k][b]["against_plan"] = versus(W[k][b], W["plan"][b])
    res[k]["history"]["real_twd_since_1983"] = real_twd(W[k]["history"], ns, W_HIST)
out["splits"] = res

# the central frontier (today's forwards, VT at its median): every 5% of the shares moved, for the trade-off's shape
fr = []
base_c = P.run(c, margin=MARGIN, margin_fn=MF)
for f in FRONTIER:
    rf = refrac(base_c, f)
    rr = C.rule(rf)
    top, pay = float(rr["top"]), float(rf["top"])
    con = min(pay, top)
    fr.append({"fraction_moved": f, "stated_bottom": float(rr["bottom"]), "stated_top": top,
               "top_raw": float(rr["top_raw"]), "funds_pay": pay, "contribution": con, "excess": pay - con,
               "flexibility": float(rf["kept33"]), "flexibility_plus_above_top": float(rf["kept33"]) + pay - con,
               "total": con + float(rf["kept33"]) + pay - con})
# where each $5,000 step of the stated top starts (fraction moved at which top_raw reaches the step), centrally
r_half = C.rule(base_c)
b_raw, m_raw_half = float(r_half["bottom_raw"]), float(r_half["top_raw"] - r_half["bottom_raw"])
steps = []
for top in np.arange(95_000, 145_001, 5_000):
    f_need = (top - b_raw) / m_raw_half * 0.5          # top_raw(f) = bottom_raw + (f / 0.5) x moved half's raw value
    if 0.0 <= f_need <= 1.0:
        rf = refrac(base_c, f_need)
        pay = float(rf["top"])
        kept = float(rf["kept33"])
        steps.append({"stated_top": float(top), "fraction_moved_from": f_need, "flexibility": kept,
                      "excess": pay - float(top), "flexibility_plus_above_top": kept + pay - float(top)})
out["central_frontier"] = {"by_fraction": fr, "step_starts": steps,
                           "note": "central only (today's forwards, VT 7.5% a year); a benchmark of the trade, not a "
                                   "choice open to Caplet (IPS l.15 is frozen at half)"}

# ---------------------------------------------------------------- checks: the plan must reproduce the register
reg = json.load(open(HERE / "results_2026-11-10.json"))["plan"]["H_plain"]
KH = json.load(open(HERE / "results_kept_half_2026-11-10.json"))
JSN = json.load(open(HERE / "results_joint_stress_2026-11-10.json"))
SS = json.load(open(HERE / "results_share_split_2026-11-12.json"))["options"]["B"]
pc_, ph, ps, pj = res["plan"]["central_today"], res["plan"]["house"], res["plan"]["history"], res["plan"]["joint"]
tw = JSN["twd_test"]
WP = W["plan"]


def mad(a, b):
    return float(np.max(np.abs(np.asarray(a, float) - np.asarray(b, float))))


checks = {
    "central_vs_NUMBERS_4": {
        "stated": [[pc_["stated_bottom"], pc_["stated_top"]], [reg["central_rule"]["bottom"], reg["central_rule"]["top"]]],
        "unrounded": [[pc_["bottom_raw"], pc_["top_raw"]], [reg["central_rule"]["bottom_raw"], reg["central_rule"]["top_raw"]]],
        "funds_pay": [pc_["funds_pay"], reg["central"]["top"]],
        "contribution": [pc_["contribution"], reg["central_rule"]["gift"]],
        "excess": [pc_["excess"], reg["central_rule"]["excess"]],
        "half_kept": [pc_["flexibility"], reg["central"]["kept33"]],
        "half_kept_plus_excess": [pc_["flexibility_plus_above_top"], reg["central_rule"]["kept_plus_excess"]],
        "total": [pc_["contribution_plus_flexibility_plus_above_top"], reg["central"]["total"]]},
    "house_vs_NUMBERS_4_and_8f": {
        "stated_bottom": [ph["stated_bottom_p5_p50_p95"], JSN["house"]["bottom_stated_p5_p50_p95"]],
        "stated_top": [ph["stated_top_p5_p50_p95"], JSN["house"]["top_stated_p5_p50_p95"]],
        "contribution": [ph["contribution_p5_p50_p95"], reg["house_rule"]["gift"]],
        "excess": [ph["excess_p5_p50_p95"], reg["house_rule"]["excess"]],
        "half_kept_p1_p5_p50_p95": [ph["flexibility_p1_p5_p50_p95"], KH["house"]["kept_p1_p5_p50_p95"]],
        "half_kept_plus_excess_p1_p5_p50_p95": [ph["flexibility_plus_above_top_p1_p5_p50_p95"],
                                                KH["house"]["kept_plus_excess_p1_p5_p50_p95"]],
        "half_kept_over_funds_pay_8f": [ph["flexibility_over_funds_pay_p5_p50_p95"],
                                        KH["house"]["kept_as_share_of_top_p5_p50_p95"]],
        "half_kept_median_if_fell": [ph["flexibility_median_if_shares_fell_2031_2033"],
                                     KH["house"]["kept_median_if_fell_2031_2033"]],
        "half_kept_plus_excess_median_if_fell": [ph["flexibility_plus_above_top_median_if_shares_fell_2031_2033"],
                                                 KH["house"]["kept_plus_excess_median_if_fell_2031_2033"]],
        "total": [ph["contribution_plus_flexibility_plus_above_top_p5_p50_p95"], reg["house"]["total"]]},
    "history_vs_NUMBERS_4_and_8f": {
        "stated_top": [ps["stated_top_p5_p50_p95"], reg["history_rule"]["top"]],
        "half_kept_p1_p5_p50_p95": [ps["flexibility_p1_p5_p50_p95"], KH["history"]["kept_p1_p5_p50_p95"]],
        "half_kept_plus_excess_p1_p5_p50_p95": [ps["flexibility_plus_above_top_p1_p5_p50_p95"],
                                                KH["history"]["kept_plus_excess_p1_p5_p50_p95"]],
        "half_kept_plus_excess_lowest": [ps["flexibility_plus_above_top_min"], KH["history"]["kept_plus_excess_lowest"]],
        "half_kept_over_funds_pay_8f": [ps["flexibility_over_funds_pay_p5_p50_p95"],
                                        KH["history"]["kept_as_share_of_top_p5_p50_p95"]],
        "half_kept_lowest": [ps["worst_flexibility"]["value"], KH["history"]["kept_lowest"]["value"]],
        "half_kept_lowest_start": [ps["worst_flexibility"]["start"], KH["history"]["kept_lowest"]["start"]]},
    "joint_vs_NUMBERS_8i": {
        "stated_bottom": [pj["stated_bottom_p5_p50_p95"], JSN["joint"]["bottom_stated_p5_p50_p95"]],
        "stated_top": [pj["stated_top_p5_p50_p95"], JSN["joint"]["top_stated_p5_p50_p95"]],
        "half_kept_p1_p5_p50_p95": [pj["flexibility_p1_p5_p50_p95"], JSN["joint"]["kept33_p1_p5_p50_p95"]],
        "max_abs_diff_vs_joint_stress_J": {k2: mad(WP["joint"][k1], ns["J"][k2]) for k1, k2 in
                                           (("bottom", "bottom_stated"), ("top", "top_stated"),
                                            ("contrib", "gift_capped"), ("excess", "excess"), ("flex", "kept33"))}},
    "twd_vs_NUMBERS_8j": {
        b: {"flexibility_covers_10pct": [res["plan"][bb]["twd_flexibility"]["covers_10pct"],
                                         tw[b]["kept_half"]["covers_0.100"]],
            "flexibility_fails": [res["plan"][bb]["twd_flexibility"]["fails_count_10pct"],
                                  tw[b]["kept_half"]["fails_count_0.100"]],
            "flexibility_covers_strict": [res["plan"][bb]["twd_flexibility"]["covers_strict_11.1pct"],
                                          tw[b]["kept_half"]["covers_0.111"]],
            "flexibility_19_in_20": [res["plan"][bb]["twd_flexibility"]["largest_stronger_twd_covered_19_in_20"],
                                     tw[b]["kept_half"]["largest_stronger_twd_covered_19_in_20"]],
            "plus_above_top_covers_10pct": [res["plan"][bb]["twd_flexibility_plus_above_top"]["covers_10pct"],
                                            tw[b]["kept_half_plus_excess"]["covers_0.100"]],
            "plus_above_top_fails": [res["plan"][bb]["twd_flexibility_plus_above_top"]["fails_count_10pct"],
                                     tw[b]["kept_half_plus_excess"]["fails_count_0.100"]],
            "shares_of_contribution_flexibility": [res["plan"][bb]["twd_flexibility"]["covers_share_of_contribution"],
                                                   tw[b]["kept_half"]["covers_share_of_contribution"]],
            "shares_of_contribution_plus_above_top": [
                res["plan"][bb]["twd_flexibility_plus_above_top"]["covers_share_of_contribution"],
                tw[b]["kept_half_plus_excess"]["covers_share_of_contribution"]]}
        for b, bb in (("house", "house"), ("history_rates_at_forwards", "history"), ("joint_replay", "joint"))},
    "real_twd_vs_NUMBERS_8j": {
        "flexibility": [res["plan"]["history"]["real_twd_since_1983"]["flexibility"]["covers_actual_move"],
                        tw["real_twd_with_same_months_shares"]["kept_half"]["covers_actual_move"]],
        "flexibility_fails_starts": [",".join(res["plan"]["history"]["real_twd_since_1983"]["flexibility"]["fails_starts"]),
                                     ",".join(tw["real_twd_with_same_months_shares"]["kept_half"]["fails_starts"])],
        "flexibility_gap_p50_max": [res["plan"]["history"]["real_twd_since_1983"]["flexibility"]["gap_when_fails_p50_max"],
                                    tw["real_twd_with_same_months_shares"]["kept_half"]["gap_when_fails_p50_max"]],
        "plus_above_top": [res["plan"]["history"]["real_twd_since_1983"]["flexibility_plus_above_top"]["covers_actual_move"],
                           tw["real_twd_with_same_months_shares"]["kept_half_plus_excess"]["covers_actual_move"]],
        "windows": [res["plan"]["history"]["real_twd_since_1983"]["windows"],
                    tw["real_twd_with_same_months_shares"]["windows"]]},
    "returns_vs_NUMBERS_8k": {
        "central_total_jan2033": [pc_["returns_to_laura_8k"], JSN["returns_to_laura"]["forwards"]["total_jan2033"]],
        "carry_15dec_to_1jan": [G_FW, JSN["returns_to_laura"]["forwards"]["carry_15dec2032_to_1jan2033"]],
        "topup_return": [TOPUP_FW, JSN["returns_to_laura"]["forwards"]["backstop_left_jan2033"]],
        "joint_total_p5_p50_p95": [pj["returns_to_laura_8k_p5_p50_p95"],
                                   JSN["returns_to_laura"]["joint_replay"]["total_p5_p50_p95"]]},
    "vs_NUMBERS_8n_option_B": {
        b: {"stated_bottom": [res["plan"][b]["stated_bottom_p5_p50_p95"], SS[b]["stated_bottom_p5_p50_p95"]],
            "stated_top": [res["plan"][b]["stated_top_p5_p50_p95"], SS[b]["stated_top_p5_p50_p95"]],
            "contribution": [res["plan"][b]["contribution_p5_p50_p95"], SS[b]["contribution_p5_p50_p95"]],
            "flexibility_plus_above_top": [res["plan"][b]["flexibility_plus_above_top_p1_p5_p50_p95"][1:],
                                           SS[b]["flexibility_p5_p50_p95"]],
            "half_kept": [res["plan"][b]["flexibility_p1_p5_p50_p95"][1:], SS[b]["half_kept_p5_p50_p95"]],
            "total": [res["plan"][b]["contribution_plus_flexibility_plus_above_top_p5_p50_p95"],
                      SS[b]["contribution_plus_flexibility_p5_p50_p95"]]}
        for b in ("house", "history", "joint")},
    "same_floor_every_split_max_abs_diff": float(max(mad(W[k][b]["floor_pay"], WP[b]["floor_pay"])
                                                     for k in MOVES for b in ("house", "history", "joint"))),
    "same_bottom_every_split_max_abs_diff": float(max(mad(W[k][b]["bottom"], WP[b]["bottom"])
                                                      for k in MOVES for b in ("house", "history", "joint"))),
    "moved_plus_kept_value_on_move_day_equals_vt31": float(max(mad(W[k]["house"]["vt31"], WP["house"]["vt31"])
                                                               for k in MOVES)),
}


def leaves(x, path=""):
    """Every [ours, register] pair in the check blocks (a list of two numbers, two equal-length number lists, or two
    dicts of numbers), with its path. Lists of other lengths and notes are information only."""
    if isinstance(x, dict):
        for kk, v in x.items():
            yield from leaves(v, f"{path}/{kk}")
    elif isinstance(x, list) and len(x) == 2:
        a, b = x
        if isinstance(a, dict) and isinstance(b, dict):
            for kk in a:
                yield f"{path}/{kk}", a[kk], b[kk]
        elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
            for i, (u, v) in enumerate(zip(a, b)):
                if isinstance(u, list):
                    yield from ((f"{path}[{i}]{q}", uu, vv) for q, uu, vv in
                                ((f"[{j}]", uu, vv) for j, (uu, vv) in enumerate(zip(u, v))))
                else:
                    yield f"{path}[{i}]", u, v
        else:
            yield path, a, b


pairs = list(leaves({k: v for k, v in checks.items() if k not in ("same_floor_every_split_max_abs_diff",
                                                                   "same_bottom_every_split_max_abs_diff",
                                                                   "moved_plus_kept_value_on_move_day_equals_vt31")}))
bad, dmax, smax = [], 0.0, 0.0
for pth, a, b in pairs:
    if isinstance(a, str) or isinstance(b, str):
        if a != b:
            bad.append([pth, a, b])
        continue
    d = abs(float(a) - float(b))
    if max(abs(float(a)), abs(float(b))) > 1.5:          # dollars: must agree to the dollar (within $0.50)
        dmax = max(dmax, d)
        if d > 0.5:
            bad.append([pth, a, b])
    else:                                               # shares and ratios: must be identical (1e-9)
        smax = max(smax, d)
        if d > 1e-9:
            bad.append([pth, a, b])
jmax = max(checks["joint_vs_NUMBERS_8i"]["max_abs_diff_vs_joint_stress_J"].values())
checks["summary"] = {"pairs_compared": len(pairs), "largest_dollar_difference": dmax,
                     "largest_share_difference": smax, "joint_J_largest_difference": jmax,
                     "mismatches": bad,
                     "plan_reproduces_register": bool(not bad and jmax <= 1e-6
                                                      and checks["same_floor_every_split_max_abs_diff"] <= 1e-6
                                                      and checks["same_bottom_every_split_max_abs_diff"] <= 1e-6)}
out["checks"] = checks
out["run_seconds"] = time.perf_counter() - T0

(HERE / f"results_kept_share_2026-11-14{C.tag(NAME)}.json").write_text(json.dumps(out, indent=1, default=float))


# ---------------------------------------------------------------- print
def k_(x):
    return f"${x / 1000:,.1f}k"


def pc(x):
    return f"{100 * x:.1f}%"


print(f"top-up and extra Treasuries returned (forwards, 1 Jan 2033 money): {TOPUP_FW:,.0f}; carry {G_FW:.10f}")
for k in MOVES:
    cc = res[k]["central_today"]
    print("=" * 30, k, res[k]["label"])
    print(f"  central: stated {cc['stated_bottom']:,.0f} to {cc['stated_top']:,.0f} (raw {cc['bottom_raw']:,.0f} to "
          f"{cc['top_raw']:,.0f}); funds pay {cc['funds_pay']:,.0f}; contribution {cc['contribution']:,.0f}; excess "
          f"{cc['excess']:,.0f}; flexibility {cc['flexibility']:,.0f}; +above {cc['flexibility_plus_above_top']:,.0f}; "
          f"total {cc['contribution_plus_flexibility_plus_above_top']:,.0f}; flex/top "
          f"{pc(cc['flexibility_over_stated_top'])}; TWD x{cc['twd_10pct_flexibility_cover_multiple']:.2f} / "
          f"x{cc['twd_10pct_flexibility_plus_above_top_cover_multiple']:.2f}; returns 8k {cc['returns_to_laura_8k']:,.0f}")
    for b in ("house", "history", "joint"):
        s = res[k][b]
        t1, t2 = s["twd_flexibility"], s["twd_flexibility_plus_above_top"]
        print(f"  {b:7s} bottom {s['stated_bottom_p5_p50_p95']} top {s['stated_top_p5_p50_p95']} width "
              f"{s['width_p5_p50_p95']} one-figure {s['count_width_zero_one_figure']} | contribution "
              f"{s['contribution_p5_p50_p95']} inside {pc(s['share_contribution_inside_stated_range'])}")
        print(f"          flex p1/p5/p50/p95 {[round(x) for x in s['flexibility_p1_p5_p50_p95']]} | +above "
              f"{[round(x) for x in s['flexibility_plus_above_top_p1_p5_p50_p95']]} | flex/top p50 "
              f"{pc(s['flexibility_over_stated_top_p5_p50_p95'][1])} (+above {pc(s['flexibility_plus_above_top_over_stated_top_p5_p50_p95'][1])})"
              f" | TWD flex {pc(t1['covers_10pct'])} ({t1['fails_count_10pct']} fail) +above {pc(t2['covers_10pct'])} "
              f"({t2['fails_count_10pct']} fail); 13%/17% flex {pc(t1['covers_share_of_contribution']['0.13'])}/"
              f"{pc(t1['covers_share_of_contribution']['0.17'])}")
        if "against_plan" in s:
            v = s["against_plan"]
            print(f"          vs plan: contribution diff {[round(x) for x in v['contribution_difference_p5_p50_p95']]}, "
                  f"flex diff {[round(x) for x in v['flexibility_difference_p5_p50_p95']]}, +above diff "
                  f"{[round(x) for x in v['flexibility_plus_above_top_difference_p5_p50_p95']]}, total diff "
                  f"{[round(x) for x in v['total_difference_p5_p50_p95']]}, total above plan {pc(v['share_total_above_plan'])}")
    rt = res[k]["history"]["real_twd_since_1983"]
    print(f"  real TWD since 1983 ({rt['windows']} windows): flex {pc(rt['flexibility']['covers_actual_move'])} "
          f"(fails {rt['flexibility']['fails_count']}), +above {pc(rt['flexibility_plus_above_top']['covers_actual_move'])} "
          f"(fails {rt['flexibility_plus_above_top']['fails_count']})")
print("=" * 30, "central frontier step starts")
for s_ in steps:
    print(f"  top {s_['stated_top']:,.0f} from {pc(s_['fraction_moved_from'])} moved: flexibility {s_['flexibility']:,.0f}"
          f", excess {s_['excess']:,.0f}, +above {s_['flexibility_plus_above_top']:,.0f}")
print("=" * 30, "checks")
for kk, vv in checks.items():
    print(" ", kk, json.dumps(vv, default=float)[:400])
print(f"run time {out['run_seconds']:.1f} s")
