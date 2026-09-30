"""M4 sensitivity (not pre-registered; no decision rule changes): WHO fills a coupon-reinvestment gap on Laura's
dated holdings, and does D6 "keep half" survive under that owner?

Why: after the v3 memos, WS7's red team (STATUS.md, rounds r3 / kac-2 / fact-audit, 30 Sep) found that the kit names
three different owners for the same gap: Laura's kept half (WS2 range memo condition 5, WS6 note IBTM_R), the ten
holdings themselves (WS2 D6 memo "the fix belongs in the holdings"), and the whole stock fund in 2031 before the range
is set (WS3 D_stress_bad_year.md rule 3), and none after 2033. The case says the range "must protect the operating
commitment", which is rule 3. This script tests D6 under both mechanisms on BOTH WS2 builds:

  A. "kept money pays in 2033" (v3; = rab/models/m4_ladder_gap.py): K' = K - g33. Reproduced here as a self-check.
  B. "stock fund fills the gap in 2031, before the range is set" (WS3 rule 3): g31 = g33 / (1 + r)^2 is set aside in
     Treasuries at the scenario rate r; the fund left is B3' = B3 - g31 and keeps its stock path (B5' = B5 B3'/B3);
     the top is F + s B3'; gift and kept money follow the M4 rule on B3', B5'. If g31 > B3 the fund is gone and the
     rest comes out of the floor: the announced bottom moves (counted as a PR-4 failure).
     In these flat-rate scenarios the whole gap is visible in 2031 (yields have already moved), so nothing is left
     for 2031-2033; a fall in yields AFTER 2031 is not modelled here (WS3/M7 territory).

Gap scenarios: numbers.yaml reinvest.rung.* as in m4_ladder_gap.py, plus "curve forwards" (at_curve: coupons earn the
28 Sep curve's own forward rates). Rung gaps are max(0, 50,000 - delivered): later rungs' surpluses are not netted.

Tolerance (mechanism B): the largest gap, valued 1 Jan 2031, for which share s still passes PR-4 and PR-5 in all three
models (bisection to $10), for s = 0, 1/3, 0.40, 1/2.

Writes rab/results/M4/gap_owner.csv, gap_owner_robust.csv, gap_owner_tolerance.csv, gap_owner_log.txt.
Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m4_gap_owner.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rab" / "models"))
import m4_ladder_gap as LG  # noqa: E402  (primary_GK, blind_GK, GK, constants: shared with the v3 check)

OUT = ROOT / "rab" / "results" / "M4"
MODELS, S_GRID, KAPPA, CONF, PD_MAX, A = LG.MODELS, LG.S_GRID, LG.KAPPA, LG.CONF, LG.PD_MAX, LG.A
TOL_SHARES = [0.0, 0.33, 0.40, 0.50]
SCEN = {"none (STRIPS basis, M4 as specified)": (None, 0.0), "Book L, curve forwards": ("at_curve", 0.05),
        "Book L, today's yields": ("at_own", 0.05), "Book L, today's yields - 2 points": ("at_own_minus_2pp", 0.03),
        "Book L, 2%": ("at_2pct", 0.02), "Book L, 0%": ("at_0pct", 0.0)}


def gaps():
    N = yaml.safe_load(open(ROOT / "rab" / "numbers.yaml"))["numbers"]
    rungs = sorted((v["value"] for k, v in N.items() if k.startswith("reinvest.rung.")), key=lambda x: x["pays"])
    assert len(rungs) == 10 and rungs[0]["pays"] == "2033-01-01" and rungs[-1]["pays"] == "2042-01-01"
    out = {}
    for name, (field, r) in SCEN.items():
        if field is None:
            out[name] = dict(rate=r, gap_sum=0.0, g33=0.0, g31=0.0, rungs_short=0, surplus_sum=0.0)
            continue
        g = [max(0.0, 50_000.0 - x[field]) for x in rungs]
        su = [max(0.0, x[field] - 50_000.0) for x in rungs]
        g33 = sum(v / (1 + r) ** i for i, v in enumerate(g))
        out[name] = dict(rate=r, gap_sum=sum(g), g33=g33, g31=g33 / (1 + r) ** 2, rungs_short=sum(v > 0 for v in g),
                         surplus_sum=sum(su))
    return out


def rule3(B3, B5, phi, F, s, g31, r):
    """Mechanism B. Returns gift G, kept K, top U and a flag for 'the fund could not cover the gap'."""
    B3n = B3 - g31
    short = B3n < 0
    f = np.where(short, 0.0, B3n / B3)
    B3p, B5p = np.maximum(B3n, 0.0), B5 * f
    U = F + s * B3p
    G = np.minimum(phi * F + s * np.minimum(B5p, B3p), U)
    # fund exhausted: the rest of the gap comes out of the floor money in 2031 and grows at r to 2033
    take = np.where(short, -B3n * (1 + r) ** 2, 0.0)
    G = np.where(short, phi * F - take, G)
    U = np.where(short, F - take, U)
    K = np.where(short, 0.0, phi * F + B5p - G)
    return G, K, U, short


def passes(G, K):
    return (np.mean(G < A) <= PD_MAX) and (np.mean(K >= KAPPA * G) >= CONF)


def tol_rule3(B3, B5, phi, F, s, r=0.03):
    lo, hi = 0.0, 150_000.0
    if not passes(*rule3(B3, B5, phi, F, s, 0.0, r)[:2]):
        return None
    while hi - lo > 10:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if passes(*rule3(B3, B5, phi, F, s, mid, r)[:2]) else (lo, mid)
    return lo


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    gp = gaps()
    rows, tol, log = [], [], []
    say = lambda t: (print(t, flush=True), log.append(t))
    say("M4 gap-owner sensitivity (not pre-registered; MODEL; 28 Sep 2026 curve; 200,000 paths per model per build)")
    say("  A = kept money pays in 2033 (v3 memos; m4_ladder_gap.py); B = stock fund fills the gap in 2031 before the "
        "range is set (WS3 stress rule 3)")
    for k, v in gp.items():
        say(f"  gap scenario {k:38s}: rung gaps ${v['gap_sum']:,.0f} over {v['rungs_short']} rungs "
            f"(surpluses on other rungs ${v['surplus_sum']:,.0f}, not netted); valued 1 Jan 2033 ${v['g33']:,.0f}, "
            f"1 Jan 2031 ${v['g31']:,.0f} at {v['rate']:.0%}")
    for build, fn in (("primary", LG.primary_GK), ("blind", LG.blind_GK)):
        data = fn()
        for m in MODELS:
            B3, B5, phi, F = data[m]
            for s in TOL_SHARES:
                tol.append(dict(build=build, model=m, s=s, mech="B", max_gap_1jan2031=tol_rule3(B3, B5, phi, F, s)))
            for name, v in gp.items():
                best = {"A": None, "B": None}
                at = {}
                for s in S_GRID:
                    G, K = LG.GK(B3, B5, phi, F, s)
                    KA = K - v["g33"]
                    okA = (np.mean(G < A) <= PD_MAX) and (np.mean(KA >= KAPPA * G) >= CONF)
                    GB, KB, UB, short = rule3(B3, B5, phi, F, s, v["g31"], v["rate"])
                    okB = passes(GB, KB)
                    if okA:
                        best["A"] = float(s)
                    if okB:
                        best["B"] = float(s)
                    if s in (0.0, 0.5):
                        at[s] = dict(pA=float(np.mean(KA >= KAPPA * G)), pB=float(np.mean(KB >= KAPPA * GB)),
                                     EG_A=float(np.mean(G - np.maximum(0.0, -KA))), EG_B=float(np.mean(GB)),
                                     top_med_B=float(np.median(UB)), p_short_B=float(np.mean(short)),
                                     p_below_A_B=float(np.mean(GB < A)), keptp5_B=float(np.percentile(KB, 5)))
                h = at[0.5]
                rows.append(dict(build=build, model=m, scenario=name, gap_sum=v["gap_sum"], surplus_sum=v["surplus_sum"],
                                 g33=v["g33"], g31=v["g31"],
                                 s_star_A=best["A"], s_star_B=best["B"], P_keep10_half_A=h["pA"],
                                 P_keep10_half_B=h["pB"], P_keep10_zero_B=at[0.0]["pB"], E_gift_half_A=h["EG_A"],
                                 E_gift_half_B=h["EG_B"], top_median_half_B=h["top_med_B"],
                                 kept_p5_half_B=h["keptp5_B"], P_fund_short_B=h["p_short_B"],
                                 P_gift_below_145k_half_B=h["p_below_A_B"]))
                say(f"  {build:7s} {m:5s} {name:38s} s* A {best['A'] if best['A'] is not None else 'none':>4} "
                    f"B {best['B'] if best['B'] is not None else 'none':>4} | half: P(kept >= 10%) A {h['pA']:.1%} "
                    f"B {h['pB']:.1%} | E gift A ${h['EG_A']:,.0f} B ${h['EG_B']:,.0f} | B: top median "
                    f"${h['top_med_B']:,.0f}, kept p5 ${h['keptp5_B']:,.0f}, P(fund < gap) {h['p_short_B']:.2%}, "
                    f"P(gift < $145k) {h['p_below_A_B']:.2%}")
    df, dt = pd.DataFrame(rows), pd.DataFrame(tol)
    rob = []
    for (b, sc), g in df.groupby(["build", "scenario"], sort=False):
        r = dict(build=b, scenario=sc)
        for mech in ("A", "B"):
            col = g[f"s_star_{mech}"]
            r[f"s_star_robust_{mech}"] = None if col.isna().any() else float(col.min())
        rob.append(r)
    say("  robust s* (min over T, BOOT, BAYES; PR-7 keeps half only if 0.40-0.60):")
    for r in rob:
        fa = lambda x: "none" if x is None else f"{x:.2f}"
        say(f"    {r['build']:7s} {r['scenario']:38s} A {fa(r['s_star_robust_A'])}  B {fa(r['s_star_robust_B'])}")
    say("  mechanism B: largest gap (valued 1 Jan 2031, set aside at 3%) that still passes PR-4 and PR-5 in all "
        "three models:")
    for (b, s), g in dt.groupby(["build", "s"]):
        v = g["max_gap_1jan2031"]
        say(f"    {b:7s} share {s:.2f}: " + ("fails with no gap (" + ", ".join(g.loc[v.isna(), "model"]) + ")"
                                             if v.isna().any() else f"${v.min():,.0f}"))
    # self-check: mechanism A must equal the v3 check (m4_ladder_gap.py) on the scenarios both scripts share
    v3 = pd.read_csv(OUT / "ladder_gap.csv")
    mrg = df.merge(v3, on=["build", "model", "scenario"], how="inner")
    assert len(mrg) == 2 * 3 * 5, len(mrg)
    same = ((mrg["s_star_A"].fillna(-1) == mrg["s_star"].fillna(-1))
            & np.isclose(mrg["P_keep10_half_A"], mrg["P_keep10_half"], atol=1e-12)).all()
    say(f"  self-check: mechanism A reproduces rab/results/M4/ladder_gap.csv on all 30 shared rows: {bool(same)}")
    assert same
    df.to_csv(OUT / "gap_owner.csv", index=False)
    pd.DataFrame(rob).to_csv(OUT / "gap_owner_robust.csv", index=False)
    dt.to_csv(OUT / "gap_owner_tolerance.csv", index=False)
    (OUT / "gap_owner_log.txt").write_text("\n".join(log) + "\n")


if __name__ == "__main__":
    main()
