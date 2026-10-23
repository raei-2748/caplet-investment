#!/usr/bin/env python3
"""Third, standard-library-only check of M2's deterministic keys.

WS4 blind builder, 30 Sep 2026 (Sydney). AI-generated verification code (Claude Code) for Team Caplet; MODEL figures,
no deliverable text. Written from `rab/models/M2_SPEC.md` (s2 dates, s3 curve and cost conventions, s7 H14, s8 2028
base and H13) and the 28 Sep 2026 row of the Treasury par-curve file. It shares no code with the reference build
(`rab/models/m2_rate_paths.py`, not read) or with `m2_blind.py` in this folder (not read either): no numpy, pandas,
scipy or statsmodels, only `math`, `csv`, `json`, `datetime`.

Why a third pricer: Gate A used a stdlib pricer as its tie-breaker for M1. The M2 keys that need no Monte Carlo and
no history panel (costs, break-evens, the ladder yield, H13, H14, the 2028 base) can be checked the same way. The
one Monte Carlo key touched here is E5, whose closed form 1 - Phi(b*_RW / sigma_h) needs only the RW break-even
computed here and sigma_h read from `results.json` (an input, so labelled as a consistency check, not a rebuild).

Run: python rab/verification/blind/deterministic_check.py [--curve-date 2026-09-28] [--out <json>]
Exit code 1 if any comparison exceeds its tolerance.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # worktree root
HERE = Path(__file__).resolve().parent

# The 12 tenors of the reference curve R (spec s3.1). "1.5 Month" and "4 Mo" are not used.
TENORS = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": 0.25, "6 Mo": 0.5, "1 Yr": 1.0, "2 Yr": 2.0, "3 Yr": 3.0,
          "5 Yr": 5.0, "7 Yr": 7.0, "10 Yr": 10.0, "20 Yr": 20.0, "30 Yr": 30.0}
PAYMENTS = [dt.date(Y - 1, 11, 15) for Y in range(2033, 2043)]  # Nov-15 STRIPS basis, ten x $50,000 (spec s2)
PAY = 50_000.0
DEPOSIT_A = 300_000.0
DEPOSIT_B = 150_000.0


# ----------------------------------------------------------------------------------------------------------------
# Inputs
# ----------------------------------------------------------------------------------------------------------------
def load_par_row(date: dt.date) -> dict[float, float]:
    """Par curve (tenor years -> percent) for one date from the Treasury CSV (spec I1)."""
    folder = "treasury_par_2000_2026" if date.year >= 2000 else "treasury_par_1990_1999"
    path = ROOT / "rab" / "data" / folder / f"{date.year}.csv"
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            if dt.datetime.strptime(row["Date"].strip(), "%m/%d/%Y").date() == date:
                return {TENORS[k]: float(row[k]) for k in TENORS if row.get(k, "").strip() not in ("", ".")}
    raise SystemExit(f"no par-curve row for {date} in {path}")


def yaml_value(key: str) -> float | None:
    """Read `<key>: ... value: X` from rab/numbers.yaml with a line scan (stdlib only)."""
    path = ROOT / "rab" / "numbers.yaml"
    if not path.exists():
        return None
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        if line.strip() == f"{key}:":
            for nxt in lines[i + 1:i + 12]:
                s = nxt.strip()
                if s.startswith("value:"):
                    try:
                        return float(s.split(":", 1)[1].strip())
                    except ValueError:
                        return None
            return None
    return None


# ----------------------------------------------------------------------------------------------------------------
# Curve (spec s3.1, the M1 "D1 method")
# ----------------------------------------------------------------------------------------------------------------
def interp(xs: list[float], ys: list[float], x: float) -> float:
    """Linear interpolation on sorted xs, flat outside."""
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    lo, hi = 0, len(xs) - 1
    while hi - lo > 1:  # binary search for the bracket
        mid = (lo + hi) // 2
        if xs[mid] <= x:
            lo = mid
        else:
            hi = mid
    w = (x - xs[lo]) / (xs[hi] - xs[lo])
    return ys[lo] + w * (ys[hi] - ys[lo])


class Curve:
    """Bootstrapped discount curve from a par vector, valued at date v."""

    def __init__(self, par: dict[float, float], v: dt.date):
        self.v = v
        xs = sorted(par)
        ys = [par[x] / 100.0 for x in xs]
        grid = [0.5 * j for j in range(1, 61)]
        p = [interp(xs, ys, t) for t in grid]
        dfs: list[float] = []
        running = 0.0
        for pj in p:
            c = pj / 2.0
            df = (1.0 - c * running) / (1.0 + c)  # j = 1 gives 1 / (1 + p_1/2)
            dfs.append(df)
            running += df
        self.ts = [0.0] + grid
        self.ls = [0.0] + [math.log(d) for d in dfs]

    def df(self, d: dt.date) -> float:
        tau = (d - self.v).days / 365.25
        return math.exp(interp(self.ts, self.ls, tau))


def shifted(par: dict[float, float], b_bp: float) -> dict[float, float]:
    return {t: y + b_bp / 100.0 for t, y in par.items()}


# ----------------------------------------------------------------------------------------------------------------
# Ladder costs (spec s3.2) and ladder yield (s3.3)
# ----------------------------------------------------------------------------------------------------------------
def pv_at(par: dict[float, float], v: dt.date) -> float:
    cur = Curve(par, v)
    return sum(PAY * cur.df(P) for P in PAYMENTS)


def cost_rw(par: dict[float, float], A: dt.date) -> float:
    """'Yields unchanged': the curve on the purchase day is `par`, valued at A."""
    return pv_at(par, A)


def cost_fwd(par: dict[float, float], D: dt.date, A: dt.date) -> float:
    """'Forward rates come true': today's curve carried to A at its own short rate."""
    cur = Curve(par, D)
    return sum(PAY * cur.df(P) for P in PAYMENTS) / cur.df(A)


def bisect(f, lo: float, hi: float, target: float, steps: int = 200) -> float:
    """Root of f(x) = target on [lo, hi]; f monotone. 200 halvings of an 800bp bracket is far below 1e-12bp."""
    flo = f(lo) - target
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        fmid = f(mid) - target
        if (fmid > 0) == (flo > 0):
            lo, flo = mid, fmid
        else:
            hi = mid
        if hi - lo < 1e-13:
            break
    return 0.5 * (lo + hi)


def breakeven_fall_bp(par, D, A, convention: str) -> float:
    if convention == "FWD":
        f = lambda b: cost_fwd(shifted(par, b), D, A)  # noqa: E731
    else:
        f = lambda b: cost_rw(shifted(par, b), A)  # noqa: E731
    b_star = bisect(f, -400.0, 400.0, DEPOSIT_A)
    return -b_star


def ladder_yield_pct(par: dict[float, float], D: dt.date) -> float:
    """y (percent, semiannual) with sum 50,000 (1 + y/200)^(-2 tau_Y) = V(D)."""
    V = pv_at(par, D)
    taus = [(P - D).days / 365.25 for P in PAYMENTS]
    f = lambda y: sum(PAY * (1.0 + y / 200.0) ** (-2.0 * t) for t in taus)  # noqa: E731
    # f is decreasing in y; bisect on [-5, 50] percent
    lo, hi = -5.0, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > V:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-13:
            break
    return 0.5 * (lo + hi)


def phi(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


# ----------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--curve-date", default="2026-09-28")
    ap.add_argument("--out", default=str(HERE / "deterministic_check.json"))
    args = ap.parse_args()

    D = dt.date.fromisoformat(args.curve_date)
    A = dt.date(2027, 1, 1)
    B = dt.date(2028, 1, 1)
    gate_a_date = dt.date(2026, 9, 28)
    R = load_par_row(D)
    if len(R) != 12:
        print(f"warning: {len(R)} of 12 tenors present on {D}")

    out: dict = {"meta": {"curve_date": D.isoformat(), "purchase_date": A.isoformat(), "second_deposit": B.isoformat(),
                          "horizon_days": (A - D).days, "basis": "Nov-15 STRIPS, ten x $50,000, MODEL",
                          "python": sys.version.split()[0], "libraries": "standard library only"},
                 "reference_curve_R_pct": {f"{t:.6f}": y for t, y in sorted(R.items())}}

    # --- deterministic keys ------------------------------------------------------------------------------------
    c_fwd = cost_fwd(R, D, A)
    c_rw = cost_rw(R, A)
    pv_today = pv_at(R, D)
    be_fwd = breakeven_fall_bp(R, D, A, "FWD")
    be_rw = breakeven_fall_bp(R, D, A, "RW")
    y_D = ladder_yield_pct(R, D)
    # y is in percent; the shift is +-1bp, so x100 turns (percent / bp) into bp per bp (spec s3.3: expected ~1)
    dy_db = 100.0 * (ladder_yield_pct(shifted(R, 1.0), D) - ladder_yield_pct(shifted(R, -1.0), D)) / 2.0
    rung_2033_at_R = PAY * Curve(R, A).df(PAYMENTS[0])
    out["deterministic"] = {
        "cost_fwd_R_usd": c_fwd, "cost_rw_R_usd": c_rw, "pv_today_R_usd": pv_today,
        "headroom_fwd_usd": DEPOSIT_A - c_fwd, "headroom_rw_usd": DEPOSIT_A - c_rw,
        "breakeven_fall_bp_fwd": be_fwd, "breakeven_fall_bp_rw": be_rw,
        "ladder_yield_y_D_pct": y_D, "dy_db_at_R": dy_db, "rung_2033_cost_at_A_rw_usd": rung_2033_at_R,
    }

    # --- H14 (spec s8, D1 [8]): no 2028 deposit ---------------------------------------------------------------
    h14 = {}
    for b in (-50.0, -100.0):
        c = shifted(R, b)
        cur = Curve(c, D)
        gap = cost_fwd(c, D, A) - DEPOSIT_A
        rung_2033_fwd = PAY * cur.df(PAYMENTS[0]) / cur.df(A)
        h14[f"{b:+.0f}bp"] = {"gap_usd": gap, "rung_2033_fwd_usd": rung_2033_fwd,
                              "unfunded_2033_usd": gap / rung_2033_fwd * PAY}
    out["H14"] = h14

    # --- 2028 base (spec s8 check) -----------------------------------------------------------------------------
    y1 = R[1.0]
    y5 = R[5.0]
    F_base = DEPOSIT_B / (1.0 + y5 / 100.0) ** 5
    base = {}
    for conv, cost in (("fwd", c_fwd), ("rw", c_rw)):
        leftover = DEPOSIT_A - cost
        G = DEPOSIT_B + leftover * (1.0 + y1 / 100.0)
        base[conv] = {"leftover_usd": leftover, "grown_at_1y_pct": y1, "G_usd": G, "F_usd": F_base,
                      "S_usd": max(0.0, G - F_base)}
    out["base_2028"] = base

    # --- H13 (spec s8, E6 [8]) ---------------------------------------------------------------------------------
    h13 = {}
    for b in (-50.0, -100.0, -150.0):
        c = shifted(R, b)
        cur = Curve(c, D)
        gap = cost_fwd(c, D, A) - DEPOSIT_A
        carry = cur.df(A) / cur.df(B)  # growth from A to B at the shifted curve's own forward rate
        topup = max(gap, 0.0) * carry
        leftover = max(-gap, 0.0) * carry  # zero whenever gap > 0 (always the case at -50bp and beyond)
        G = DEPOSIT_B + leftover - topup
        row = {"gap_usd": gap, "topup_on_B_usd": topup, "G_usd": G}
        for label, y5b in (("y5_unchanged", y5), ("y5_shifted", y5 + b / 100.0)):
            F = DEPOSIT_B / (1.0 + y5b / 100.0) ** 5
            S = max(0.0, G - F)
            face = DEPOSIT_B if G >= F else G * (1.0 + y5b / 100.0) ** 5
            row[label] = {"y5_pct": y5b, "floor_cost_usd": F, "stock_fund_usd": S, "floor_face_usd": face}
        h13[f"{b:+.0f}bp"] = row
    out["H13"] = h13

    # --- E5 closed form (consistency only; sigma_h is an input from results.json) -----------------------------
    sigma_h = None
    res_path = HERE / "results.json"
    if res_path.exists():
        try:
            sigma_h = json.load(open(res_path))["headline_keys"]["E5_sigma_h_bp"]
        except (KeyError, json.JSONDecodeError):
            sigma_h = None
    if sigma_h:
        out["E5_closed_form"] = {"sigma_h_bp_input": sigma_h, "breakeven_rw_bp": be_rw,
                                 "P_gap_gt_0": 1.0 - phi(be_rw / sigma_h),
                                 "note": "1 - Phi(b*_RW / sigma_h): a parallel Normal shift; consistency with E5"}

    # --- comparisons ------------------------------------------------------------------------------------------
    checks = []

    def add(name, mine, ref, tol, source):
        if ref is None:
            checks.append({"key": name, "mine": mine, "ref": None, "diff": None, "tol": tol, "source": source,
                           "verdict": "NO REFERENCE"})
            return
        diff = mine - ref
        checks.append({"key": name, "mine": mine, "ref": ref, "diff": diff, "tol": tol, "source": source,
                       "verdict": "MATCH" if abs(diff) <= tol else "FAIL"})

    if D == gate_a_date:
        add("cost_fwd_R_usd", c_fwd, yaml_value("laura.ladder.cost_2027_strips"), 1.0, "numbers.yaml (Gate A)")
        add("breakeven_fall_bp_fwd", be_fwd, yaml_value("laura.ladder.breakeven_fall_bp_strips"), 0.05,
            "numbers.yaml (Gate A, 1 dp)")
        add("S2028_base_fwd_usd", base["fwd"]["S_usd"], yaml_value("laura.stock_fund_2028_usd.strips"), 1.0,
            "numbers.yaml (Gate A, whole dollars)")
        add("F2028_base_usd", F_base, yaml_value("laura.floor_cost_2028"), 1.0, "numbers.yaml (Gate A, whole dollars)")
        add("H14_-50bp_unfunded_2033_usd", h14["-50bp"]["unfunded_2033_usd"], 9281.0, 1.0, "M2_SPEC s8 must-reproduce")
        add("H14_-100bp_unfunded_2033_usd", h14["-100bp"]["unfunded_2033_usd"], 28753.0, 1.0,
            "M2_SPEC s8 must-reproduce")
        add("pv_today_R_usd", pv_today, 289119.20, 0.01, "Gate A headline (task brief)")

    blind_keys = None
    if res_path.exists():
        try:
            blind_keys = json.load(open(res_path))["headline_keys"]
        except (KeyError, json.JSONDecodeError):
            blind_keys = None
    if blind_keys and D == gate_a_date:
        pairs = [
            ("cost_fwd_R_usd", c_fwd, 0.01), ("cost_rw_R_usd", c_rw, 0.01),
            ("breakeven_fall_bp_fwd", be_fwd, 1e-4), ("breakeven_fall_bp_rw", be_rw, 1e-4),
            ("S2028_base_fwd_usd", base["fwd"]["S_usd"], 0.01), ("F2028_base_usd", F_base, 0.01),
            ("S2028_base_rw_usd", base["rw"]["S_usd"], 0.01),
            ("H13_-50bp_fund_y5_unchanged", h13["-50bp"]["y5_unchanged"]["stock_fund_usd"], 0.01),
            ("H13_-50bp_fund_y5_shifted", h13["-50bp"]["y5_shifted"]["stock_fund_usd"], 0.01),
            ("H13_-100bp_fund_y5_unchanged", h13["-100bp"]["y5_unchanged"]["stock_fund_usd"], 0.01),
            ("H13_-100bp_fund_y5_shifted", h13["-100bp"]["y5_shifted"]["stock_fund_usd"], 0.01),
            ("H13_-150bp_floor_face_y5_unchanged", h13["-150bp"]["y5_unchanged"]["floor_face_usd"], 0.01),
            ("H13_-150bp_floor_face_y5_shifted", h13["-150bp"]["y5_shifted"]["floor_face_usd"], 0.01),
            ("H14_-50bp_unfunded_2033_usd", h14["-50bp"]["unfunded_2033_usd"], 0.01),
            ("H14_-100bp_unfunded_2033_usd", h14["-100bp"]["unfunded_2033_usd"], 0.01),
        ]
        for key, mine, tol in pairs:
            add(f"{key} vs m2_blind", mine, blind_keys.get(key), tol, "m2_blind results.json headline_keys")
        if "E5_closed_form" in out:
            try:
                e5_p = json.load(open(res_path))["estimators"]["E5_move_options"]["P_gap_gt_0"]
            except (KeyError, json.JSONDecodeError):
                e5_p = None
            add("E5 P(gap>0): closed form vs m2_blind Monte Carlo", out["E5_closed_form"]["P_gap_gt_0"], e5_p, 0.005,
                "m2_blind results.json (100,000 draws; MC noise ~0.15pp)")

    out["checks"] = checks
    n_fail = sum(1 for c in checks if c["verdict"] == "FAIL")
    out["summary"] = {"checks": len(checks), "fail": n_fail,
                      "no_reference": sum(1 for c in checks if c["verdict"] == "NO REFERENCE")}

    # --- print ------------------------------------------------------------------------------------------------
    print(f"curve {D}  purchase {A}  ({(A - D).days} days)  stdlib only")
    print(f"Cost_FWD(R) = {c_fwd:,.2f}   Cost_RW(R) = {c_rw:,.2f}   PV today = {pv_today:,.2f}")
    print(f"break-even fall: FWD {be_fwd:.4f}bp   RW {be_rw:.4f}bp   headroom RW {DEPOSIT_A - c_rw:,.2f}")
    print(f"ladder yield y(D) = {y_D:.4f}%   dy/db = {dy_db:.4f}   2033 rung at A (RW) = {rung_2033_at_R:,.2f}")
    print(f"H14 unfunded 2033: -50bp {h14['-50bp']['unfunded_2033_usd']:,.2f}   -100bp {h14['-100bp']['unfunded_2033_usd']:,.2f}")
    print(f"2028 base: FWD S {base['fwd']['S_usd']:,.2f} / F {F_base:,.2f}   RW S {base['rw']['S_usd']:,.2f}")
    for b, row in h13.items():
        print(f"H13 {b}: gap {row['gap_usd']:,.0f} top-up {row['topup_on_B_usd']:,.0f} | fund y5 unchanged "
              f"{row['y5_unchanged']['stock_fund_usd']:,.0f} (face {row['y5_unchanged']['floor_face_usd']:,.0f}) | "
              f"fund y5 shifted {row['y5_shifted']['stock_fund_usd']:,.0f} (face {row['y5_shifted']['floor_face_usd']:,.0f})")
    if "E5_closed_form" in out:
        print(f"E5 closed form: 1 - Phi({be_rw:.2f} / {sigma_h:.2f}) = {out['E5_closed_form']['P_gap_gt_0']:.4f}")
    print(f"checks: {len(checks)}  fail: {n_fail}")
    for c in checks:
        ref = "n/a" if c["ref"] is None else f"{c['ref']:,.4f}"
        diff = "" if c["diff"] is None else f"  diff {c['diff']:+.6f}"
        print(f"  {c['verdict']:<12} {c['key']:<58} mine {c['mine']:,.4f}  ref {ref}{diff}")

    Path(args.out).write_text(json.dumps(out, indent=1))
    print(f"wrote {args.out}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
