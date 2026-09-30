"""M4 sensitivity (not pre-registered; no decision rule changes): WHO fills a coupon-reinvestment gap on Laura's
dated holdings, and does D6 "keep half" survive under that owner?

Why: after the v3 memos, WS7's red team (STATUS.md, rounds r3 / kac-2 / fact-audit, 30 Sep) found that the kit named
three different owners for the same gap: Laura's kept half (WS2 range memo v3 condition 5, WS6 note IBTM_R), the ten
holdings themselves (WS2 D6 memo v3), and the whole stock fund in 2031 before the range is set (WS3
D_stress_bad_year.md rule 3 before ad74847), and none after 2033. WS3 then rewrote its rule 3 (ad74847) as "Laura's
half first, then the gift above the floor, then the floor; in 2031 lower the top by any gap her half cannot cover".
This script tests D6 under all three readings on BOTH WS2 builds (g31 = the gap valued 1 Jan 2031, g33 = 1 Jan 2033,
r = the scenario rate; money set aside earns r):

  A. "kept money pays in 2033" (v3; = rab/models/m4_ladder_gap.py): K' = K - g33. Reproduced here as a self-check.
  B. "stock fund fills the gap in 2031, before the range is set" (WS3 rule 3 before ad74847): g31 is set aside from the
     fund; the fund left is B3' = B3 - g31 and keeps its stock path (B5' = B5 B3'/B3); the top is F + s B3'.
  C. "Laura's half first, then the gift above the floor, then the floor" (WS3 rule 3 from ad74847): in 2031 the part
     of the gap Laura's part (1 - s) B3 cannot cover, ex = max(0, g31 - (1 - s) B3), is set aside from the fund and
     the top is lowered by it (U = F + s B3 - ex); the rest of the gap, (g31 - ex)(1 + r)^2, is paid in 2033 from
     Laura's kept money; if that runs out, the gift is cut (payments first).
  In B and C, if g31 > B3 the fund is gone and the rest comes out of the floor: the announced bottom moves.
  In these flat-rate scenarios the whole gap is visible in 2031 (yields have already moved); a fall in yields AFTER
  2031 is not modelled here (WS3/M7 territory).

Gap scenarios: numbers.yaml reinvest.rung.* as in m4_ladder_gap.py, plus "curve forwards" (at_curve: coupons earn the
28 Sep curve's own forward rates). Rung gaps are max(0, 50,000 - delivered): later rungs' surpluses are not netted.

Tolerance: the largest gap, valued 1 Jan 2031, for which share s still passes PR-4 and PR-5 in all three models
(bisection to $10), for s = 0, 1/3, 0.40, 1/2, under B and C (A's is in ladder_gap_tolerance.csv, valued 2033).

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
MECHS = ("A", "B", "C")
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


def outcome(mech, B3, B5, phi, F, s, g31, r):
    """Gift G (after any payments-first cut), kept money K (>= 0 unless mech A), top U, and two flags:
    lowered = the 2031 top was lowered for the gap; short = the gap exceeded the whole fund in 2031."""
    g33 = g31 * (1 + r) ** 2
    if mech == "A":
        G, K = LG.GK(B3, B5, phi, F, s)
        z = np.zeros_like(B3, dtype=bool)
        return G, K - g33, F + s * B3, z, z
    ex = np.full_like(B3, g31) if mech == "B" else np.maximum(0.0, g31 - (1 - s) * B3)
    B3n = B3 - ex
    short = B3n < 0
    f = np.where(short, 0.0, B3n / np.where(B3 > 0, B3, 1.0))
    B3p, B5p = np.maximum(B3n, 0.0), B5 * f
    U = F + s * B3p if mech == "B" else F + s * B3 - ex
    G = np.minimum(phi * F + s * np.minimum(B5p, B3p), U)
    K = phi * F + B5p - G - (g31 - ex) * (1 + r) ** 2          # mech B: g31 - ex = 0
    cut = np.maximum(0.0, -K)                                   # payments first: the gift pays what K cannot
    G, K = G - cut, K + cut
    take = np.where(short, -B3n * (1 + r) ** 2, 0.0)            # fund gone: the rest comes out of the floor
    G = np.where(short, phi * F - take, G)
    U = np.where(short, F - take, U)
    K = np.where(short, 0.0, K)
    return G, K, U, ex > 0, short


def passes(G, K):
    return (np.mean(G < A) <= PD_MAX) and (np.mean(K >= KAPPA * G) >= CONF)


def tol(mech, B3, B5, phi, F, s, r=0.03):
    if not passes(*outcome(mech, B3, B5, phi, F, s, 0.0, r)[:2]):
        return None
    lo, hi = 0.0, 150_000.0
    while hi - lo > 10:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if passes(*outcome(mech, B3, B5, phi, F, s, mid, r)[:2]) else (lo, mid)
    return lo


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    gp = gaps()
    rows, tl, log = [], [], []
    say = lambda t: (print(t, flush=True), log.append(t))
    say("M4 gap-owner sensitivity (not pre-registered; MODEL; 28 Sep 2026 curve; 200,000 paths per model per build)")
    say("  A = kept money pays in 2033 (v3; m4_ladder_gap.py); B = whole fund fills the gap in 2031 before the range; "
        "C = Laura's part first, top lowered in 2031 only by what it cannot cover (WS3 rule 3, ad74847)")
    for k, v in gp.items():
        say(f"  gap scenario {k:38s}: rung gaps ${v['gap_sum']:,.0f} over {v['rungs_short']} rungs "
            f"(surpluses on other rungs ${v['surplus_sum']:,.0f}, not netted); valued 1 Jan 2033 ${v['g33']:,.0f}, "
            f"1 Jan 2031 ${v['g31']:,.0f} at {v['rate']:.0%}")
    for build, fn in (("primary", LG.primary_GK), ("blind", LG.blind_GK)):
        data = fn()
        for m in MODELS:
            B3, B5, phi, F = data[m]
            for mech in ("B", "C"):
                for s in TOL_SHARES:
                    tl.append(dict(build=build, model=m, s=s, mech=mech,
                                   max_gap_1jan2031=tol(mech, B3, B5, phi, F, s)))
            for name, v in gp.items():
                best, at = {k: None for k in MECHS}, {}
                for s in S_GRID:
                    for mech in MECHS:
                        G, K, U, low, short = outcome(mech, B3, B5, phi, F, s, v["g31"], v["rate"])
                        if mech == "A":  # exactly as m4_ladder_gap.py: PR-4 on the uncut gift
                            G0 = LG.GK(B3, B5, phi, F, s)[0]
                            ok = (np.mean(G0 < A) <= PD_MAX) and (np.mean(K >= KAPPA * G0) >= CONF)
                            pk = float(np.mean(K >= KAPPA * G0))
                            G = G0 - np.maximum(0.0, -K)
                        else:
                            ok, pk = passes(G, K), float(np.mean(K >= KAPPA * G))
                        if ok:
                            best[mech] = float(s)
                        if s in (0.0, 0.5):
                            at[(mech, s)] = dict(pk=pk, EG=float(np.mean(G)), top=float(np.median(U)),
                                                 low=float(np.mean(low)), short=float(np.mean(short)),
                                                 below=float(np.mean(G < A)), kp5=float(np.percentile(K, 5)))
                r = dict(build=build, model=m, scenario=name, gap_sum=v["gap_sum"], surplus_sum=v["surplus_sum"],
                         g33=v["g33"], g31=v["g31"])
                for mech in MECHS:
                    h = at[(mech, 0.5)]
                    r.update({f"s_star_{mech}": best[mech], f"P_keep10_half_{mech}": h["pk"],
                              f"P_keep10_zero_{mech}": at[(mech, 0.0)]["pk"], f"E_gift_half_{mech}": h["EG"],
                              f"top_median_half_{mech}": h["top"], f"kept_p5_half_{mech}": h["kp5"],
                              f"P_top_lowered_half_{mech}": h["low"], f"P_fund_short_{mech}": h["short"],
                              f"P_gift_below_145k_half_{mech}": h["below"]})
                rows.append(r)
                fs = lambda x: "none" if x is None else f"{x:.2f}"
                say(f"  {build:7s} {m:5s} {name:38s} s* A {fs(best['A'])} B {fs(best['B'])} C {fs(best['C'])} | "
                    + " | ".join(f"{k}: P(kept>=10%) {at[(k, 0.5)]['pk']:.1%}, top med ${at[(k, 0.5)]['top']:,.0f}, "
                                 f"P(top lowered) {at[(k, 0.5)]['low']:.2%}, P(gift<$145k) {at[(k, 0.5)]['below']:.2%}"
                                 for k in MECHS))
    df, dt = pd.DataFrame(rows), pd.DataFrame(tl)
    rob = []
    for (b, sc), g in df.groupby(["build", "scenario"], sort=False):
        rr = dict(build=b, scenario=sc)
        for mech in MECHS:
            col = g[f"s_star_{mech}"]
            rr[f"s_star_robust_{mech}"] = None if col.isna().any() else float(col.min())
        rob.append(rr)
    say("  robust s* (min over T, BOOT, BAYES; PR-7 keeps half only if 0.40-0.60):")
    fa = lambda x: "none" if x is None else f"{x:.2f}"
    for rr in rob:
        say(f"    {rr['build']:7s} {rr['scenario']:38s} " + "  ".join(f"{k} {fa(rr[f's_star_robust_{k}'])}"
                                                                  for k in MECHS))
    say("  largest gap (valued 1 Jan 2031) that still passes PR-4 and PR-5 in all three models:")
    for (mech, b, s), g in dt.groupby(["mech", "build", "s"]):
        v = g["max_gap_1jan2031"]
        say(f"    {mech} {b:7s} share {s:.2f}: " + ("fails with no gap (" + ", ".join(g.loc[v.isna(), "model"]) + ")"
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
