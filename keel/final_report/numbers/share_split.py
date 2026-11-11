"""What more shares would buy: the benchmark on the other side of the 2028 split (Keel numbers worker, Thu 12 Nov 2026
morning, Sydney). MODEL, not a forecast, not a promise and not a recommendation. NUMBERS 8n.

Run from the repo root:  python3 -I keel/final_report/numbers/share_split.py
   or from this folder:  python3 -I share_split.py
Writes keel/final_report/numbers/results_share_split_2026-11-12.json and prints the figures (about 20 seconds, numpy
only). Reads results_2026-11-10.json and results_joint_stress_2026-11-10.json only to show the checks; writes nothing
else; changes no other script.

Why (blind panel, Thu 12 Nov): a finance professor judge wrote that the only benchmark is all-Treasury (NUMBERS 4, C8)
and "the plan never shows what more shares would buy". This is the other side: plans with more shares, on the same
rules, so the report can show the trade-off the IPS chose. The frozen IPS says "Most of the 2028 deposit will fund a
Treasury fund maturing in late 2032" (IPS l.15); options C to E break that word and are benchmarks only.

The money compared is what is left in January 2028 after the top-up (plan.run's R; the top-up itself, the ten payments
and the backstop are the same in every option and every path). Five splits of it:
  A  all to the floor (= C8, the all-Treasury benchmark; reproduced as a check)
  B  the plan: the floor gets the larger of 73.3% of what is left and $75,001 (Keel's reading of "most", NUMBERS 0)
  C  half floor, half VT
  D  a quarter floor, three quarters VT
  E  all VT
Same rules for every option (NUMBERS 4): half the VT moves into the late-2032 Treasury fund before the 2031 meetings;
each stated end = the money in the late-2032 fund x what $1 of its holdings pays on 15 Dec 2032 if nothing earns
interest from the trade day, less 0.5%, rounded down to $5,000 (completion.rule); the other half is promised to no one
(her flexibility); the 2033 facility contribution is the lower of what the floor and the moved half pay and the stated
top; anything above the top joins her flexibility.

Three bases, built exactly as range_margin.py builds them (route 1):
  house    plan.draws + plan.run + completion.rule (200,000 simulated futures, seed 2033);
  history  plan.shiller_windows + plan.run + completion.rule (1,770 US stock windows since 1871, rates at today's
           forwards), as plan.history but with the split passed through;
  joint    joint_stress.py's own setup code, run from its source up to its first results block (nothing it writes is
           run), then its plan_path re-done with the split passed through (585 windows, Jan 1962 to Sep 2010 starts).

What comes back from the top-up (the backstop's money, NUMBERS 8h and 8k) is the same in every option: the backstop and
the ten are bought before the split. Joint replay: each window's own figure (8k). US stock history: $45,456 in every
window (rates at today's forwards). House model: $45,456 too, because the house model moves no rates after 2031 and
models no reinvestment (NUMBERS 7); it is labelled so.
"""
import ast
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
PLAN_BOTTOM = 95_000.0          # the plan's central stated bottom (NUMBERS 4)
END = date(2032, 12, 15)

OPTIONS = {
    "A": dict(share=1.0, most=False, label="All to the floor (C8, the all-Treasury benchmark)"),
    "B": dict(share=None, most=True, label="The plan: floor gets the larger of 73.3% of what is left and $75,001"),
    "C": dict(share=0.5, most=False, label="Half floor, half VT"),
    "D": dict(share=0.25, most=False, label="A quarter floor, three quarters VT"),
    "E": dict(share=0.0, most=False, label="All VT"),
}


# ---------------------------------------------------------------- the joint replay's setup (as range_margin.py)

def joint_setup():
    """Run joint_stress.py's own top-level code up to its first results block (def window), skipping every statement
    that assigns to its `out` dict; nothing is written. Returns its namespace (J, A, starts, ...). Copied from
    range_margin.py unchanged."""
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


# ---------------------------------------------------------------- one option on each basis

def finish(res, r, pay, topup, extra=None):
    """Common outputs. res: plan.run output; r: completion.rule output; pay: what the floor and the moved half pay;
    topup: what comes back from the top-up (1 Jan 2033 money)."""
    B, T = np.asarray(r["bottom"], float), np.asarray(r["top"], float)
    pay = np.asarray(pay, float)
    contrib = np.minimum(pay, T)
    excess = pay - contrib
    kept = np.asarray(res["kept33"], float)
    flex = kept + excess
    o = dict(bottom=B, top=T, bottom_raw=np.asarray(r["bottom_raw"], float), top_raw=np.asarray(r["top_raw"], float),
             pay=pay, contrib=contrib, excess=excess, kept=kept, flex=flex, cf=contrib + flex,
             topup=np.broadcast_to(np.asarray(topup, float), pay.shape).copy(),
             floor_money=np.asarray(res["floor_money"], float), vt28=np.asarray(res["vt28"], float),
             R=np.asarray(res["R"], float), floor_pay=np.asarray(res["floor"], float))
    o["all"] = o["cf"] + o["topup"]
    if extra:
        o.update(extra)
    return o


def run_central(opt, topup):
    res = P.run(c, margin=MARGIN, share=opt["share"], margin_fn=MF, most=opt["most"])
    r = C.rule(res)
    return finish(res, r, np.asarray(res["top"], float), topup)


def run_house(opt, draws, topup):
    d0, d1, d2, vt3, vt2 = draws
    res = P.run(c, MARGIN, opt["share"], DEPOSIT, d0, d1, d2, vt3, vt2, MF, most=opt["most"])
    r = C.rule(res, d0 + d1, d0 + d1 + d2)
    return finish(res, r, r["payout"], topup, {"all_t": np.asarray(res["all_t"], float)})


def run_history(opt, topup):
    w = P.shiller_windows()
    vt3 = np.array([a for _, a, _ in w])
    vt2 = np.array([b for _, _, b in w])
    res = P.run(c, MARGIN, opt["share"], DEPOSIT, vt3=vt3, vt2=vt2, margin_fn=MF, most=opt["most"])
    r = C.rule(res)
    n = len(w)
    bc = lambda x: np.broadcast_to(np.asarray(x, float), (n,)).copy()
    o = finish({k: bc(res[k]) for k in ("kept33", "floor_money", "vt28", "R", "floor")},
               {k: bc(r[k]) for k in ("bottom", "top", "bottom_raw", "top_raw")}, bc(r["payout"]), topup)
    o["starts"] = [k for k, _, _ in w]
    return o


def run_joint(opt, ns):
    """joint_stress.plan_path (H_plain branch) with the split passed through, then its realised payouts and cap."""
    A = ns["A"]
    m28, m31 = np.asarray(A["m28"], float), np.asarray(A["m31"], float)
    fF, fM = ns["fF"], ns["fM"]
    d1 = fF * (m28 - 1)
    d2 = fM * m31 - fM - d1
    mf = C.margin_fn_mult(NAME, m28)
    res = P.run(c, margin=MARGIN, share=opt["share"], d0=0.0, d1=d1, d2=d2, vt3=A["vt3"], vt2=A["vt2"],
                margin_fn=mf, most=opt["most"])
    r = C.rule(res, mF=m28, mM=m31)
    floor_real = np.asarray(res["floor"], float) * A["floor_real_ratio"]
    moved_real = np.asarray(res["moved"], float) * A["moved_real_ratio"]
    o = finish(res, r, floor_real + moved_real, A["overflow_jan2033_value"])
    g = np.asarray(A["g_end_j33"], float)
    # 8k's convention: contribution and excess carried 17 days to 1 Jan 2033 at the window's own rate
    o["all_8k"] = o["contrib"] * g + o["excess"] * g + o["kept"] + o["topup"]
    o["returns_8k"] = o["excess"] * g + o["kept"] + o["topup"]
    o["starts"] = list(ns["starts"])
    o["vt_bought"] = [ns["keys"][ns["kpos"][s] + 12] for s in ns["starts"]]
    return o


# ---------------------------------------------------------------- summaries

def pl(a, ps=(5, 50, 95)):
    return [float(np.percentile(np.asarray(a, float), p)) for p in ps]


def summary(o, stated_method=True):
    s = {
        "paths": int(o["pay"].size),
        "stated_bottom_p5_p50_p95": C.qs(o["bottom"]),
        "stated_top_p5_p50_p95": C.qs(o["top"]),
        "contribution_p5_p50_p95": C.qs(o["contrib"]) if stated_method else pl(o["contrib"]),
        "contribution_p5_p50_p95_linear": pl(o["contrib"]),
        "contribution_min": float(o["contrib"].min()),
        "share_contribution_below_95k": float((o["contrib"] < PLAN_BOTTOM - 0.5).mean()),
        "share_contribution_equals_stated_top": float((np.abs(o["contrib"] - o["top"]) < 0.5).mean()),
        "share_stated_bottom_zero": float((o["bottom"] < 0.5).mean()),
        "flexibility_p5_p50_p95": pl(o["flex"]),
        "flexibility_min": float(o["flex"].min()),
        "half_kept_p5_p50_p95": pl(o["kept"]),
        "excess_p5_p50_p95": pl(o["excess"]),
        "funds_pay_p5_p50_p95": pl(o["pay"]),
        "contribution_plus_flexibility_p5_p50_p95": pl(o["cf"]),
        "topup_return_p5_p50_p95": pl(o["topup"]),
        "all_money_p5_p50_p95": pl(o["all"]),
        "all_money_min": float(o["all"].min()),
        "floor_money_p5_p50_p95": pl(o["floor_money"]),
        "floor_share_of_deposit_p50": float(np.median(o["floor_money"]) / DEPOSIT),
        "share_floor_money_over_half_deposit": float((o["floor_money"] > DEPOSIT / 2).mean()),
        "vt_bought_p5_p50_p95": pl(o["vt28"]),
    }
    if "starts" in o:
        st = o["starts"]
        for key, arr in (("contribution", o["contrib"]), ("flexibility", o["flex"]), ("all_money", o["all"]),
                         ("stated_top", o["top"])):
            i = int(np.argmin(arr))
            w = {"value": float(arr[i]), "start": st[i], "stated_bottom": float(o["bottom"][i]),
                 "stated_top": float(o["top"][i]), "contribution": float(o["contrib"][i]),
                 "flexibility": float(o["flex"][i]), "all_money": float(o["all"][i])}
            if "vt_bought" in o:
                w["vt_bought"] = o["vt_bought"][i]
            ties = np.flatnonzero(arr <= arr[i] + 0.5)
            w["windows_at_minimum"] = int(ties.size)
            w["starts_at_minimum_first_12"] = [st[t] for t in ties[:12]]
            if "vt_bought" in o:
                w["vt_bought_at_minimum_first_12"] = [o["vt_bought"][t] for t in ties[:12]]
            s[f"worst_{key}"] = w
    return s


def versus(o, b):
    """This option against the plan (B), path by path."""
    d_c, d_a = o["contrib"] - b["contrib"], o["all"] - b["all"]
    return {"share_contribution_above_plan": float((d_c > 0.5).mean()),
            "share_contribution_below_plan": float((d_c < -0.5).mean()),
            "contribution_difference_p5_p50_p95": pl(d_c),
            "share_all_money_above_plan": float((d_a > 0.5).mean()),
            "all_money_difference_p5_p50_p95": pl(d_a),
            "flexibility_difference_p5_p50_p95": pl(o["flex"] - b["flex"])}


# ---------------------------------------------------------------- run
out = {"stamp": {"run": "Thu 12 Nov 2026 morning (Sydney)", "curve": E.CURVE_DAY, "design": NAME,
                 "register": "Tue 10 Nov 2026 (NUMBERS 0, 3, 4, 8h, 8i, 8k, 8l)", "haircut": C.HAIRCUT,
                 "step": C.STEP, "status": "MODEL; a benchmark, not a recommendation",
                 "options": {k: v["label"] for k, v in OPTIONS.items()},
                 "money_compared": "what is left in January 2028 after the top-up (plan.run R)",
                 "conventions": "contribution, excess and half kept at face (15 Dec 2032 / 1 Jan 2033), as NUMBERS 4; "
                                "what comes back from the top-up in 1 Jan 2033 money, as NUMBERS 8h and 8k; stated "
                                "figures and the contribution read without interpolation (method 'lower'), others linear"}}

# what comes back from the top-up at today's forwards (8h, 8k): the backstop's money left after 2042, in 2033 money
_, _, _, left_fw = C.ledger(C.BASE, DSG["own"], DSG["pool"])
TOPUP_FW = float(C.in_2033_money(left_fw, C.BASE))
out["topup_return_forwards_jan2033"] = TOPUP_FW

draws = P.draws(P.N, P.SEED)
ns = joint_setup()
W = {}
for k, opt in OPTIONS.items():
    W[k] = {"central": run_central(opt, TOPUP_FW), "house": run_house(opt, draws, TOPUP_FW),
            "history": run_history(opt, TOPUP_FW), "joint": run_joint(opt, ns)}

res = {}
for k in OPTIONS:
    cen = W[k]["central"]
    g = lambda a: float(np.asarray(a).ravel()[0])
    res[k] = {
        "label": OPTIONS[k]["label"],
        "central_today": {"floor_money_jan2028": g(cen["floor_money"]), "vt_bought_jan2028": g(cen["vt28"]),
                          "floor_share_of_deposit": g(cen["floor_money"]) / DEPOSIT,
                          "keeps_most_of_2028_deposit": g(cen["floor_money"]) > DEPOSIT / 2,
                          "stated_bottom": g(cen["bottom"]), "stated_top": g(cen["top"]),
                          "bottom_raw": g(cen["bottom_raw"]), "top_raw": g(cen["top_raw"]),
                          "funds_pay": g(cen["pay"]), "contribution": g(cen["contrib"]), "excess": g(cen["excess"]),
                          "half_kept": g(cen["kept"]), "flexibility": g(cen["flex"]),
                          "contribution_plus_flexibility": g(cen["cf"]), "topup_return": g(cen["topup"]),
                          "all_money": g(cen["all"])},
    }
    for b in ("house", "history", "joint"):
        res[k][b] = summary(W[k][b])
        if k != "B":
            res[k][b]["against_plan"] = versus(W[k][b], W["B"][b])
    j = W[k]["joint"]
    res[k]["joint"]["all_money_8k_convention_p5_p50_p95"] = pl(j["all_8k"])
    res[k]["joint"]["returns_8k_convention_p5_p50_p95"] = pl(j["returns_8k"])
out["options"] = res

# ---------------------------------------------------------------- checks
reg = json.load(open(HERE / "results_2026-11-10.json"))["plan"]
c8 = reg["all_treasury"]
hp = reg["H_plain"]
JSN = json.load(open(HERE / "results_joint_stress_2026-11-10.json"))
cA, cB = res["A"]["central_today"], res["B"]["central_today"]
hA, hB = W["A"]["house"], W["B"]["house"]
checks = {
    "C8_payout_central": [cA["funds_pay"], c8["payout_central"]],
    "C8_stated_unrounded_central": [cA["bottom_raw"], c8["stated_zero_interest_central"]],
    "C8_stated_central": [cA["stated_top"], c8["stated_rounded"]],
    "C8_house_payout_p5_p50_p95": [pl(hA["pay"]), c8["house"]],
    "C8_house_all_t_equals_option_A_payout_max_abs_diff": float(np.max(np.abs(hA["pay"] - hA["all_t"]))),
    "C8_share_plan_payout_below_all_t": [float((hB["pay"] < hA["pay"]).mean()), c8["share_final_payout_below_all_t"]],
    "C8_share_plan_stated_top_below_all_t_stated": [float((hB["top"] < hA["top"]).mean()),
                                                     c8["share_final_stated_top_below_all_t_stated"]],
    "C8_share_plan_total_above_all_t": [float((hB["cf"] > hA["pay"]).mean()), c8["share_final_total_above_all_t"]],
    "A_contribution_plus_flexibility_equals_C8_payout_max_abs_diff": float(np.max(np.abs(hA["cf"] - hA["pay"]))),
    "B_central_vs_register": {"floor_payout": [g(W["B"]["central"]["floor_pay"]), hp["central"]["floor"]],
                              "funds_pay": [cB["funds_pay"], hp["central"]["top"]],
                              "half_kept": [cB["half_kept"], hp["central"]["kept33"]],
                              "contribution_plus_flexibility": [cB["contribution_plus_flexibility"],
                                                                hp["central"]["total"]],
                              "stated": [[cB["stated_bottom"], cB["stated_top"]],
                                         [hp["central_rule"]["bottom"], hp["central_rule"]["top"]]],
                              "excess": [cB["excess"], hp["central_rule"]["excess"]]},
    "B_house_vs_register": {"stated_bottom": [res["B"]["house"]["stated_bottom_p5_p50_p95"], hp["house_rule"]["bottom"]],
                            "stated_top": [res["B"]["house"]["stated_top_p5_p50_p95"], hp["house_rule"]["top"]],
                            "flexibility": [res["B"]["house"]["flexibility_p5_p50_p95"],
                                            hp["house_rule"]["kept_plus_excess"]],
                            "contribution_plus_flexibility": [res["B"]["house"]["contribution_plus_flexibility_p5_p50_p95"],
                                                              hp["house"]["total"]]},
    "B_history_vs_register": {"stated_top": [res["B"]["history"]["stated_top_p5_p50_p95"], hp["history_rule"]["top"]],
                              "flexibility": [res["B"]["history"]["flexibility_p5_p50_p95"],
                                              hp["history_rule"]["kept_plus_excess"]]},
    "B_joint_vs_joint_stress_J_max_abs_diff": {
        k2: float(np.max(np.abs(np.asarray(W["B"]["joint"][k1], float) - np.asarray(ns["J"][k2], float))))
        for k1, k2 in (("bottom", "bottom_stated"), ("top", "top_stated"), ("contrib", "gift_capped"),
                       ("excess", "excess"), ("kept", "kept33"), ("floor_money", "floor_money"))},
    "B_joint_returns_vs_8k": [res["B"]["joint"]["returns_8k_convention_p5_p50_p95"],
                              JSN["returns_to_laura"]["joint_replay"]["total_p5_p50_p95"]],
    "topup_return_vs_8k": [TOPUP_FW, JSN["returns_to_laura"]["forwards"]["backstop_left_jan2033"]],
    "same_R_every_option_house_max_abs_diff": float(max(np.max(np.abs(W[k]["house"]["R"] - W["B"]["house"]["R"]))
                                                        for k in OPTIONS)),
    "same_topup_every_option_joint_max_abs_diff": float(max(np.max(np.abs(W[k]["joint"]["topup"] - W["B"]["joint"]["topup"]))
                                                            for k in OPTIONS)),
}
out["checks"] = checks
out["run_seconds"] = time.perf_counter() - T0

(HERE / f"results_share_split_2026-11-12{C.tag(NAME)}.json").write_text(json.dumps(out, indent=1, default=float))


# ---------------------------------------------------------------- print (rounded to $1,000 and whole percentages)
def k_(x):
    return f"${x / 1000:,.0f}k"


def pc(x):
    return f"{100 * x:.0f}%"


print(f"top-up returns (forwards, 1 Jan 2033 money): {TOPUP_FW:,.0f}")
for k in OPTIONS:
    cc = res[k]["central_today"]
    print("=" * 30, k, res[k]["label"])
    print(f"  central: floor money {cc['floor_money_jan2028']:,.0f} ({pc(cc['floor_share_of_deposit'])} of deposit; "
          f"most kept: {cc['keeps_most_of_2028_deposit']}), VT {cc['vt_bought_jan2028']:,.0f}; stated "
          f"{cc['stated_bottom']:,.0f} to {cc['stated_top']:,.0f} (raw {cc['bottom_raw']:,.0f} to {cc['top_raw']:,.0f}); "
          f"funds pay {cc['funds_pay']:,.0f}; contribution {cc['contribution']:,.0f}; flexibility {cc['flexibility']:,.0f} "
          f"(kept {cc['half_kept']:,.0f} + excess {cc['excess']:,.0f}); all money {cc['all_money']:,.0f}")
    for b in ("house", "history", "joint"):
        s = res[k][b]
        line = (f"  {b:7s} bottom {s['stated_bottom_p5_p50_p95']} top {s['stated_top_p5_p50_p95']} | contribution "
                f"p5/p50 {k_(s['contribution_p5_p50_p95'][0])}/{k_(s['contribution_p5_p50_p95'][1])} "
                f"below 95k {pc(s['share_contribution_below_95k'])} ({s['share_contribution_below_95k']:.4f}) | flex "
                f"p5/p50 {k_(s['flexibility_p5_p50_p95'][0])}/{k_(s['flexibility_p5_p50_p95'][1])} | all "
                f"p5/p50 {k_(s['all_money_p5_p50_p95'][0])}/{k_(s['all_money_p5_p50_p95'][1])} | floor>half "
                f"{s['share_floor_money_over_half_deposit']:.5f}")
        print(line)
        if "worst_contribution" in s:
            wc, wa = s["worst_contribution"], s["worst_all_money"]
            print(f"          worst contribution {wc['value']:,.0f} (start {wc['start']}"
                  f"{', VT bought ' + wc['vt_bought'] if 'vt_bought' in wc else ''}; range {wc['stated_bottom']:,.0f}-"
                  f"{wc['stated_top']:,.0f}; {wc['windows_at_minimum']} windows at it: "
                  f"{wc['starts_at_minimum_first_12']}); worst all money {wa['value']:,.0f} (start {wa['start']}"
                  f"{', VT bought ' + wa['vt_bought'] if 'vt_bought' in wa else ''}; contribution "
                  f"{wa['contribution']:,.0f}, flexibility {wa['flexibility']:,.0f})")
            wf = s["worst_flexibility"]
            print(f"          worst flexibility {wf['value']:,.0f} (start {wf['start']})")
        if "against_plan" in s:
            v = s["against_plan"]
            print(f"          vs plan: contribution above {pc(v['share_contribution_above_plan'])}, below "
                  f"{pc(v['share_contribution_below_plan'])}; all money above {pc(v['share_all_money_above_plan'])}; "
                  f"all-money diff p5/p50 {v['all_money_difference_p5_p50_p95'][0]:,.0f}/"
                  f"{v['all_money_difference_p5_p50_p95'][1]:,.0f}")
print("=" * 30, "checks")
for kk, vv in checks.items():
    print(" ", kk, json.dumps(vv, default=float))
print(f"run time {out['run_seconds']:.1f} s")
