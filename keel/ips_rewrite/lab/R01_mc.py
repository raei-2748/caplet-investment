"""WO-R1: the dedicated ladder (R01, B3 with every holding >= $10k face) vs the current ladder (A), stress-tested in the
200,000 rate paths of keel/library/ips_numbers_2026-10/ips_numbers.py (same seed, same 1.00pp/yr parallel random walk,
yields floored at 0.25%).

AI-generated (Claude Code) for the IPS rewrite, Genius Lab, 26 Oct 2026 (Sydney). MODEL numbers, 15 Oct 2026 par curve.
Both ladders are bought on 1 Jan 2027 at the 15 Oct curve (prices and faces from R01_dedication.py); only what happens
to coupons afterwards differs, so the test isolates reinvestment risk. Path shift after 1 Jan 2027 = shift(t) - shift(1 Jan 2027).
  A  = current policy: each rung's coupons reinvested in itself at its own yield + shift, then the short rate (3-mo +
       shift) from maturity to the payment date (same formula as ips_numbers.py section 3).
       short_total = 500,000 - total delivered (the number sheet's measure); short_pay = sum of per-payment gaps with any
       surplus carried forward at the short rate.
  B3 = dedicated: every cash flow goes to one short Treasury pot (3-mo + shift, monthly); $50,000 leaves it each 1 Jan
       2033-42; short_pay = sum of per-payment gaps.
  A-pooled = A's faces run under B3's pot policy (shows whether the gain comes from the faces or the spending rule).
Run: python3 keel/ips_rewrite/lab/R01_mc.py   (numpy, pandas, scipy; ~1-2 minutes)
"""
import datetime as dt
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import R01_dedication as R  # noqa: E402  (curve, RUNGS, price, coupon_dates, ladder_B3)

YMIN, RATE_VOL, SEED, N = 0.25, 1.00, 20261016, 200_000
TODAY, T27 = dt.date(2026, 10, 15), dt.date(2027, 1, 1)
TOFF = R.yrs(TODAY, T27)
PAY = R.PAY
M = 12 * 16 + 1  # months from 1 Jan 2027 to 1 Jan 2043


def rel_paths(n=N):
    """Same draws as ips_numbers.py; returns shift relative to 1 Jan 2027 on a monthly grid from 1 Jan 2027."""
    rng = np.random.default_rng(SEED)
    step_t = np.arange(0, R.yrs(TODAY, dt.date(2043, 1, 1)) + 1 / 12, 1 / 12)
    inc = rng.normal(0, RATE_VOL * np.sqrt(1 / 12), (n, len(step_t) - 1))
    shifts = np.concatenate([np.zeros((n, 1)), inc.cumsum(axis=1)], axis=1).astype(np.float32)
    del inc
    i27 = np.searchsorted(step_t, TOFF)
    idx = np.clip(np.searchsorted(step_t, np.arange(M) / 12 + TOFF), 0, len(step_t) - 1)
    return shifts[:, idx] - shifts[:, [i27]]


def faces_A():
    """A: each rung sized alone so that reinvesting at its own yield delivers $50,000 (R01 ladder_A)."""
    out = {}
    for py, (mat, cpn) in R.RUNGS.items():
        p, c = R.price(mat, cpn); y0 = R.curve(R.yrs(T27, mat))
        v = 1.0
        for cd in R.coupon_dates(mat):
            v += c / 2 * (1 + y0 / 200) ** (2 * R.yrs(cd, mat))
        out[py] = PAY / (v * (1 + R.curve(.25) / 100) ** R.yrs(mat, dt.date(py, 1, 1)))
    return out


def month(d):
    return int(round(R.yrs(T27, d) * 12))


def run_A(faces, rel):
    n = rel.shape[0]; per = {}
    for py, (mat, cpn) in R.RUNGS.items():
        _, c = R.price(mat, cpn); y0 = R.curve(R.yrs(T27, mat)); T = R.yrs(T27, mat)
        v = np.ones(n, dtype=np.float64)
        for cd in R.coupon_dates(mat):
            yk = np.maximum(y0 + rel[:, month(cd)], YMIN) / 100
            v += c / 2 * (1 + yk / 2) ** (2 * R.yrs(cd, mat))
        bill = np.maximum(R.curve(.25) + rel[:, month(mat)], YMIN) / 100
        per[py] = faces[py] * v * (1 + bill) ** R.yrs(mat, dt.date(py, 1, 1))
    total = sum(per.values())
    short_total = np.maximum(10 * PAY - total, 0)
    carry = np.zeros(n); short_pay = np.zeros(n); prev = None
    for py in sorted(R.RUNGS):
        if prev:
            carry *= (1 + np.maximum(R.curve(.25) + rel[:, month(dt.date(prev, 1, 1))], YMIN) / 100)
        cash = carry + per[py]
        short_pay += np.maximum(PAY - cash, 0); carry = np.maximum(cash - PAY, 0); prev = py
    return short_total, short_pay


def run_pot(faces, rel):
    """One short Treasury pot: all coupons and maturities in, $50,000 out each 1 Jan 2033-42."""
    n = rel.shape[0]
    flow = np.zeros(M)
    for q, f in faces.items():
        mat, cpn = R.RUNGS[q]; _, c = R.price(mat, cpn)
        for cd in R.coupon_dates(mat):
            flow[month(cd)] += f * c / 2
        flow[month(mat)] += f
    pay_m = {month(dt.date(py, 1, 1)) for py in R.RUNGS}
    pot = np.zeros(n); short = np.zeros(n); worst_single = np.zeros(n)
    for m in range(M):
        if m in pay_m:
            gap = np.maximum(PAY - pot, 0); short += gap; worst_single = np.maximum(worst_single, gap)
            pot = np.maximum(pot - PAY, 0)
        pot += flow[m]
        pot *= (1 + np.maximum(R.curve(.25) + rel[:, m], YMIN) / 100) ** (1 / 12)
    return short, worst_single, pot


def pct(x):
    return {"p_over_1k": round(float((x > 1000).mean()), 3), "p50": round(float(np.median(x))),
            "p95": round(float(np.percentile(x, 95))), "p99": round(float(np.percentile(x, 99)))}


if __name__ == "__main__":
    fA = faces_A()
    fB, costB = R.ladder_B3(10_000)
    costA = sum(f * R.price(*R.RUNGS[q])[0] for q, f in fA.items())
    out = {"meta": {"curve": "15 Oct 2026 par curve (MODEL; par yields as zero rates)", "paths": N, "seed": SEED,
                    "rate_vol_pp_yr": RATE_VOL, "basis": "MODEL; bought 1 Jan 2027 at the 15 Oct curve; reinvestment risk only"},
           "cost": {"A": round(costA), "B3": round(costB), "extra": round(costB - costA)},
           "faces": {str(q): {"A": round(fA[q]), "B3": round(fB[q]), "B3_over_A": round(fB[q] / fA[q], 2)} for q in sorted(fA)},
           "cost_by_rung": {str(q): {"A": round(fA[q] * R.price(*R.RUNGS[q])[0]), "B3": round(fB[q] * R.price(*R.RUNGS[q])[0])}
                            for q in sorted(fA)}}
    # deterministic check against R01 (constant shift from 1 Jan 2027)
    det = {}
    for dy in (-1.0, -2.0, -3.0, 1.0):
        rel = np.full((1, M), dy, dtype=np.float32)
        a_tot, a_pay = run_A(fA, rel); b, _, _ = run_pot(fB, rel); ap, _, _ = run_pot(fA, rel)
        det[f"{dy:+g}pp"] = {"A_total": round(float(a_tot[0])), "A_pay": round(float(a_pay[0])), "B3": round(float(b[0])),
                             "A_pooled": round(float(ap[0]))}
    out["deterministic_check"] = det
    print(json.dumps(det, indent=1))
    # 200,000 paths, in chunks
    rel = rel_paths()
    res = {"A_total": [], "A_pay": [], "B3": [], "B3_worst_single": [], "A_pooled": [], "B3_left_2043": []}
    for s in range(0, N, 50_000):
        r = rel[s:s + 50_000]
        a_tot, a_pay = run_A(fA, r); b, bw, bl = run_pot(fB, r); ap, _, _ = run_pot(fA, r)
        for k, v in zip(res, (a_tot, a_pay, b, bw, ap, bl)):
            res[k].append(v)
    res = {k: np.concatenate(v) for k, v in res.items()}
    out["shortfall_200k_paths"] = {k: pct(res[k]) for k in ("A_total", "A_pay", "B3", "A_pooled")}
    out["B3_worst_single_payment_gap"] = pct(res["B3_worst_single"])
    out["B3_left_in_pot_after_2042_p50"] = round(float(np.median(res["B3_left_2043"])))
    out["p_B3_short_more_than_A"] = round(float((res["B3"] > res["A_total"] + 1).mean()), 4)
    out["rel_shift_2033_p5_p50_p95"] = [round(float(np.percentile(rel[:, 72], q)), 2) for q in (5, 50, 95)]
    (HERE / "R01_mc_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({k: v for k, v in out.items() if k != "deterministic_check"}, indent=1))


# ---- where the money for each payment comes from (B3, flat curve) and how far the WInS book would move ----
WINS = {2033: ("IBTM (ladder part)", None), 2034: ("IBTO", 1024 * 22.86), 2035: ("IBTP", 927 * 23.90),
        2036: ("IBTQ", 894 * 23.46), 2037: ("IBTR", 853 * 23.24), 2038: ("T Feb-2037", 20_000 * .96019),
        2039: ("T May-2038", 20_000 * .93076), 2040: ("T Nov-2039", 18_000 * .90005),
        2041: ("T Nov-2040", 18_000 * .87724), 2042: ("T Nov-2041", 20_000 * .74955)}  # COMPETITION.md s8, fill prices

if __name__ == "__main__":
    pre = {"principal": 0.0, "coupons_before_2033": 0.0, "coupons_2033_on": 0.0}
    for q, f in fB.items():
        mat, cpn = R.RUNGS[q]; _, c = R.price(mat, cpn); pre["principal"] += f
        for cd in R.coupon_dates(mat):
            pre["coupons_before_2033" if cd < dt.date(2033, 1, 1) else "coupons_2033_on"] += f * c / 2
    out["B3_cash_sources_flat"] = {k: round(v) for k, v in pre.items()}
    scale = np.median([WINS[q][1] / out["cost_by_rung"][str(q)]["A"] for q in WINS if WINS[q][1]])
    mv = {}
    for q, (name, now) in WINS.items():
        now = now if now else scale * out["cost_by_rung"][str(q)]["A"]
        tgt = scale * out["cost_by_rung"][str(q)]["B3"]
        mv[name] = {"now": round(now), "target": round(tgt), "change": round(tgt - now)}
    out["wins_move_at_fill_prices"] = {"scale_vs_A": round(float(scale), 3), "rungs": mv,
                                       "sold": round(sum(-v["change"] for v in mv.values() if v["change"] < 0)),
                                       "bought": round(sum(v["change"] for v in mv.values() if v["change"] > 0))}
    (HERE / "R01_mc_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({k: out[k] for k in ("B3_cash_sources_flat", "wins_move_at_fill_prices")}, indent=1))
