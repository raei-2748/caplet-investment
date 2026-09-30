"""M4 sensitivity (not pre-registered; no decision rests on it): the D6 rule when the dated holdings' coupon
reinvestment falls short and Laura's kept money has to fill the gap.

Why: WS7's red team (rab/redteam/ws7_devils_advocate_checks.py [1], commit 913c4f1 on rab/ws7) reran the primary M4
code with Laura's kept money K reduced by the Book L coupon-reinvestment shortfall and asked WS2 to re-derive it
before any use. M4_SPEC s3 defines K = phi F + B5 - G with no ladder term: on the headline STRIPS basis there are no
coupons to reinvest (numbers.yaml laura.ladder.strips_reinvestment). The gap only exists if Laura's real ladder is
Book L, the ten WInS-listed holdings (numbers.yaml reinvest.*).

What it does, on BOTH WS2 builds (primary code + primary paths; blind code + blind paths):
  1. gap scenarios from numbers.yaml reinvest.rung.*: sum over the ten rungs of max(0, 50,000 - delivered), valued
     on 1 Jan 2033 at the scenario rate (own yields ~5%, own - 2 points at 3%, 2%, 0%; WS7's conventions plus "own");
  2. for each model and scenario: the largest share passing PR-4 and PR-5 with K - gap in place of K, and
     P(K - gap >= 0.10 G) at shares 0 and 1/2; at share 1/2 also P(K - gap < 0) and, if the ten payments come first
     (the gift is cut by any gap the kept money cannot cover), P(gift < $145,000);
  3. tolerance: the largest gap (valued 1 Jan 2033) the rule can absorb and still pass PR-5 at share s, i.e. the
     value g with exactly 95% of paths having K - 0.10 G >= g, for s = 0, 1/3, 0.40, 1/2. At s = 0.40 this is the
     largest gap for which PR-7 still keeps half (robust s* >= 0.40).

Writes rab/results/M4/ladder_gap.csv, ladder_gap_robust.csv, ladder_gap_tolerance.csv and ladder_gap_log.txt.
Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m4_ladder_gap.py
"""
from __future__ import annotations

import math
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rab" / "models"))
sys.path.insert(0, str(ROOT / "rab" / "verification" / "blind_ws2"))
import ws2_common as C  # noqa: E402
import m3_branch as M3  # noqa: E402
import m4_cap as M4  # noqa: E402

OUT = ROOT / "rab" / "results" / "M4"
MODELS = ["T", "BOOT", "BAYES"]
S_GRID = np.round(np.arange(0.0, 1.0 + 1e-9, 0.01), 2)
KAPPA, CONF, PD_MAX = 0.10, 0.95, 0.005
A = 145_000.0  # announced floor, PR-3 (rab/results/M4/floor_delivery.csv h* = 0.025)
TOL_SHARES = [0.0, 0.33, 0.40, 0.50]
# (numbers.yaml field, valuation rate to 1 Jan 2033). "own" = today's yields 4.98-5.44% -> 5%.
SCEN = {"none (STRIPS basis, M4 as specified)": (None, 0.0), "Book L, today's yields": ("at_own", 0.05),
        "Book L, today's yields - 2 points": ("at_own_minus_2pp", 0.03), "Book L, 2%": ("at_2pct", 0.02),
        "Book L, 0%": ("at_0pct", 0.0)}


def gaps():
    N = yaml.safe_load(open(ROOT / "rab" / "numbers.yaml"))["numbers"]
    rungs = sorted((v["value"] for k, v in N.items() if k.startswith("reinvest.rung.")), key=lambda x: x["pays"])
    assert len(rungs) == 10 and rungs[0]["pays"] == "2033-01-01" and rungs[-1]["pays"] == "2042-01-01"
    out = {}
    for name, (field, rate) in SCEN.items():
        if field is None:
            out[name] = dict(field="", rate=rate, gap_sum=0.0, gap_pv_2033=0.0, rungs_short=0)
            continue
        g = [max(0.0, 50_000.0 - r[field]) for r in rungs]
        out[name] = dict(field=field, rate=rate, gap_sum=sum(g),
                         gap_pv_2033=sum(x / (1 + rate) ** i for i, x in enumerate(g)),
                         rungs_short=sum(x > 0 for x in g))
    return out


def primary_GK():
    """Primary build: M3 paths + M4 phi, exactly as rab/models/m4_cap.py (PR-2, PR-3)."""
    inp = C.inputs()
    phi, _, _ = M4.phi_draws(inp["y5"])
    res = {}
    for m in MODELS:
        o = C.rule(M3.paths(m), inp["B0"], inp["F"])
        res[m] = (o["B3"], o["B5"], phi, inp["F"])
    return res


def blind_GK():
    """Blind build: blind paths (out/paths) + blind phi, exactly as blind_m4.py main()."""
    import blind_common as bc
    import blind_m4 as bm
    n = bc.load_paths("T").shape[0]
    phi, _, _ = bm.floor_delivery(bc.rng_for("PHI"), n, bm.dgs1_changes(913))
    res = {}
    for m in MODELS:
        o = bc.outcomes(bc.load_paths(m))
        res[m] = (o["B3"], o["B5"], phi, bc.F_FLOOR)
    return res


def GK(B3, B5, phi, F, s):
    U = F + s * B3
    G = np.minimum(phi * F + s * np.minimum(B5, B3), U)
    return G, phi * F + B5 - G


def tolerance(B3, B5, phi, F, s):
    """Largest g with P(K - g >= KAPPA G) >= CONF: the order statistic leaving ceil(CONF n) paths at or above it."""
    G, K = GK(B3, B5, phi, F, s)
    d = np.sort(K - KAPPA * G)
    n = d.size
    return float(d[n - math.ceil(CONF * n)])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    gp = gaps()
    rows, tol, log = [], [], []
    say = lambda s: (print(s, flush=True), log.append(s))
    say("M4 ladder-gap sensitivity (not pre-registered; MODEL; 28 Sep 2026 curve; 200,000 paths per model)")
    for k, v in gp.items():
        say(f"  gap scenario {k:38s}: rung gaps ${v['gap_sum']:,.0f} over {v['rungs_short']} rungs, "
            f"valued 1 Jan 2033 at {v['rate']:.0%}: ${v['gap_pv_2033']:,.0f}")
    for build, fn in (("primary", primary_GK), ("blind", blind_GK)):
        data = fn()
        for m in MODELS:
            B3, B5, phi, F = data[m]
            for s in TOL_SHARES:
                tol.append(dict(build=build, model=m, s=s, max_gap_pv_2033=tolerance(B3, B5, phi, F, s)))
            for name, v in gp.items():
                best, keep = None, {}
                for s in S_GRID:
                    G, K = GK(B3, B5, phi, F, s)
                    Kn = K - v["gap_pv_2033"]
                    pf = float(np.mean(Kn >= KAPPA * G))
                    if s in (0.0, 0.5):
                        # payments first: if the gap exceeds the kept money, the gift is cut by the difference
                        Gc = G - np.maximum(0.0, -Kn)
                        keep[s] = (pf, float(np.percentile(Kn, 5)), float(np.mean(Kn < 0)), float(np.mean(Gc < A)))
                    if np.mean(G < A) <= PD_MAX and pf >= CONF:
                        best = float(s)
                rows.append(dict(build=build, model=m, scenario=name, gap_pv_2033=v["gap_pv_2033"], s_star=best,
                                 P_keep10_half=keep[0.5][0], P_keep10_zero=keep[0.0][0], kept_p5_half=keep[0.5][1],
                                 P_kept_negative_half=keep[0.5][2], P_gift_below_A_payments_first_half=keep[0.5][3]))
                say(f"  {build:7s} {m:5s} {name:38s} s* {best if best is not None else 'none':>4} | "
                    f"P(kept >= 10% of gift): half {keep[0.5][0]:.1%}, zero {keep[0.0][0]:.1%} | "
                    f"kept p5 at half ${keep[0.5][1]:,.0f} | half: P(kept < 0) {keep[0.5][2]:.2%}, "
                    f"P(gift < $145k if payments come first) {keep[0.5][3]:.2%}")
    df, dt = pd.DataFrame(rows), pd.DataFrame(tol)
    rob = []
    for (b, sc), g in df.groupby(["build", "scenario"], sort=False):
        v = None if g["s_star"].isna().any() else float(g["s_star"].min())
        rob.append(dict(build=b, scenario=sc, s_star_robust=v))
    say("  robust s* (min over T, BOOT, BAYES; PR-7 keeps half only if 0.40-0.60):")
    for r in rob:
        say(f"    {r['build']:7s} {r['scenario']:38s} {r['s_star_robust'] if r['s_star_robust'] is not None else 'none'}")
    pd.DataFrame(rob).to_csv(OUT / "ladder_gap_robust.csv", index=False)
    tmin = dt.groupby(["build", "s"])["max_gap_pv_2033"].min().reset_index()
    say("  largest gap (valued 1 Jan 2033) that still passes PR-5 in all three models:")
    for _, r in tmin.iterrows():
        say(f"    {r['build']:7s} share {r['s']:.2f}: ${r['max_gap_pv_2033']:,.0f}")
    df.to_csv(OUT / "ladder_gap.csv", index=False)
    dt.to_csv(OUT / "ladder_gap_tolerance.csv", index=False)
    (OUT / "ladder_gap_log.txt").write_text("\n".join(log) + "\n")


if __name__ == "__main__":
    main()
