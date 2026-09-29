"""Gate B WS3: large-sample check of the one Monte Carlo number that sits on a decision threshold.

The pre-registered fund rule (M6_SPEC s5) switches from VT to an alternative only if, among other tests, the gift's
spread (p95 - p5) is at most 0.90 x VT's. VT + 10% gold + 10% REIT (A4) lands at 0.8992 (reference build) and 0.8999
(blind build) on seed 20260930, and passes the spread test on 17/20 (reference) and 14/20 (blind) other seeds. This
script estimates the ratio without the seed noise, with BOTH builds' samplers, on 100 fresh seeds each (20,000,000
paths per build; seeds 20262000-20262099, used by neither build), so the gate record can say whether A4 is really
below, at or above the line.

AI-generated verification code (Claude Code, WS3 Gate B reconciler) for Team Caplet; no deliverable text.
Run from the worktree root (about 2-3 minutes):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws3/gateB_ws3_mc_precision.py
Writes rab/verification/gateB_ws3/gateB_ws3_mc_precision.json.
"""
import json
import os
import sys

import numpy as np

WT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(WT, "rab", "models"))
sys.path.insert(0, os.path.join(WT, "rab", "verification", "blind"))
import m6_rivals as P          # noqa: E402  reference build
import blind_m6 as B           # noqa: E402  blind build

SEEDS = list(range(20262000, 20262100))
POOL = 50                      # seeds pooled for the pooled-quantile estimate (10,000,000 paths)
OUT = os.path.join(os.path.dirname(__file__), "gateB_ws3_mc_precision.json")


def stats(g0, g4):
    q0 = np.percentile(g0, [5, 50, 95])
    q4 = np.percentile(g4, [5, 50, 95])
    return dict(A0=q0.tolist(), A4=q4.tolist(), spread_ratio=float((q4[2] - q4[0]) / (q0[2] - q0[0])),
                p5_change=float(q4[0] - q0[0]), median_change=float(q4[1] - q0[1]))


def ref_gifts(seed):
    fund0 = P.H.numbers()["laura.stock_fund_2028_usd.strips"]["value"]
    R, _ = P.jpm_draws(seed=seed)
    out = {}
    for a in ("A0", "A4"):
        f31 = sum(w * fund0 * np.prod(1 + R[k][:, 1:4], axis=1) for k, w in P.MC_W[a].items())
        f33 = sum(w * fund0 * np.prod(1 + R[k][:, 1:6], axis=1) for k, w in P.MC_W[a].items())
        out[a] = P.rec_gift_from_fund(f31, f33)[0]
    return out


def blind_gifts(seed, jpm):
    r = B.simulate_returns(jpm, seed)
    out = {}
    for a in ("A0", "A4"):
        f31, f33 = B.fund_mc(r, a)
        out[a] = B.fund_metrics_from_paths(f31, f33)[0]
    return out


def run(label, fn):
    per, pool0, pool4 = [], [], []
    for i, s in enumerate(SEEDS):
        g = fn(s)
        per.append(stats(g["A0"], g["A4"]))
        if i < POOL:
            pool0.append(g["A0"].astype(np.float32))
            pool4.append(g["A4"].astype(np.float32))
    r = np.array([p["spread_ratio"] for p in per])
    pooled = stats(np.concatenate(pool0).astype(np.float64), np.concatenate(pool4).astype(np.float64))
    res = dict(seeds=len(SEEDS), paths_per_seed=200_000, seed_first=SEEDS[0], seed_last=SEEDS[-1],
               ratio_mean=float(r.mean()), ratio_sd=float(r.std(ddof=1)), ratio_se=float(r.std(ddof=1) / np.sqrt(len(r))),
               ratio_min=float(r.min()), ratio_max=float(r.max()), share_seeds_ratio_le_090=float(np.mean(r <= 0.90)),
               p5_change_mean=float(np.mean([p["p5_change"] for p in per])),
               median_change_mean=float(np.mean([p["median_change"] for p in per])),
               pooled_paths=POOL * 200_000, pooled=pooled)
    print(f"[{label}] A4/A0 spread90 ratio: mean {res['ratio_mean']:.4f} (se {res['ratio_se']:.4f}, seed sd "
          f"{res['ratio_sd']:.4f}, range {res['ratio_min']:.4f}-{res['ratio_max']:.4f}); <= 0.90 on "
          f"{res['share_seeds_ratio_le_090']:.0%} of seeds; pooled {POOL * 200_000:,} paths {pooled['spread_ratio']:.4f}; "
          f"p5 change {res['p5_change_mean']:+,.0f}; median change {res['median_change_mean']:+,.0f}")
    return res


def main():
    jpm = B.load_jpm()
    out = dict(purpose="A4 (VT + gold/REIT) vs A0 (VT) spread90 ratio without seed noise; threshold 0.90 (M6_SPEC s5)",
               reference=run("reference", ref_gifts), blind=run("blind", lambda s: blind_gifts(s, jpm)))
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
