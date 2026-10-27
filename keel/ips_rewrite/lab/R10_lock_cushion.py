"""AI-generated (Claude Code), WO-R10 (Courtroom condition on the lock), 28 Oct 2026. MODEL.
STAMP: curve 22 Oct 2026 | JPM 2027 global equities 7.5% (sceptic 6.5%) | 200,000 paths, seed 20261016 | rho 0 and 0.5 | MODEL
Run: python3 keel/ips_rewrite/lab/R10_lock_cushion.py

Question: the Courtroom adopted "lock what you announce" (R08_2 variant B) on condition that it still works with the
Jan 2033 re-match (R08_5), and asked that the cushion come from leftover cash and Laura's half BEFORE the contribution.
R08_2's E took the whole set-aside (projected gap + $7,500) in that order, but let the $7,500 dent the gift when
Laura's side ran dry: 2.2% of paths fell below the quoted bottom. Rules compared, all with the 2031 lock (B):
  B      - lock, no set-aside (the gap is drawn when it shows up)
  E      - lock + set-aside of projected gap + $7,500, drawn cash -> Laura's half -> gift (R08_2)
  F      - lock + set-aside of projected gap, drawn as E; the $7,500 cushion only out of what Laura's side has left
           (cushion = min(7,500, leftover + Laura's half - projected gap)); the contribution never pays for the cushion
  G      - as F, but the cushion may also come out of the contribution ABOVE the quoted bottom (never below it):
           cash -> Laura's half -> contribution down to the bottom. The Courtroom's order, with the bottom untouchable.
"Payments short" = true 2033-42 shortfall above the set-aside, by more than $1k (B: above nothing).
"""
import json, pathlib
import numpy as np
import R08_core as core

HERE = pathlib.Path(__file__).parent
CUSH = 7500


def run(p, rule):
    halfL = 0.5 * p["V33"]; side = p["L33"] + halfL
    top = p["R"] + 0.5 * p["V31"]; locked = 0.5 * p["V31"]
    if rule == "B":
        A = p["S33"]; late = p["shortfall"] - 0          # no set-aside: gap drawn as it shows up, same claim on the gift
    elif rule == "E":
        A = p["S33"] + CUSH
    elif rule == "F":
        A = p["S33"] + np.minimum(CUSH, np.maximum(side - p["S33"], 0))
    else:
        base = p["floor_paid"] + locked * p["g2"]
        room = np.maximum(np.minimum(top, base - np.maximum(p["S33"] - side, 0)) - p["bottom"], 0)
        A = p["S33"] + np.minimum(CUSH, np.maximum(side - p["S33"], 0) + room)
    unc = np.maximum(A - side, 0)
    raw = p["floor_paid"] + locked * p["g2"] - unc
    gift = np.minimum(top, raw)
    kept = side - np.minimum(A, side) + np.maximum(raw - top, 0)
    late = p["shortfall"] - (A if rule != "B" else p["S33"])
    return {"p_gift_below_quoted_bottom": round(float((gift < p["bottom"] - 1e-6).mean()), 4),
            "p_inside_range": round(float((gift >= p["bottom"] - 1e-6).mean()), 4),
            "p_top_reached_within_1k": round(float((gift >= top - 1000).mean()), 4),
            "p_payments_short_over_1k_after_2033": round(float((late > 1000).mean()), 4),
            "short_by_p95_max_when_short": [round(float(np.percentile(late[late > 1000], q))) for q in (95, 100)] if (late > 1000).any() else 0,
            "set_aside_p50_p95": [round(float(np.percentile(A, q))) for q in (50, 95)],
            "laura_kept_p5_p50_mean": [round(float(np.percentile(kept, q))) for q in (5, 50)] + [round(float(kept.mean()))]}


if __name__ == "__main__":
    out = {"stamp": core.STAMP.format(mu="7.5% / 6.5%", rho="0 / 0.5")}
    for rho, mu in ((0.0, "1.075"), (0.5, "1.075"), (0.5, "1.065")):
        p = core.paths(rho, mu)
        out[f"rho={rho} mu={mu}"] = {r: run(p, r) for r in ("B", "E", "F", "G")}
    (HERE / "R10_lock_cushion_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
