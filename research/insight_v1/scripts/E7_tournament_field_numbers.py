"""Model numbers for the six tournament firm summaries (research/insight_v1/phase_E/tournament/firm_*.md).

Inputs (labels as in brief s3):
- Engine, returns, reserve pricing, seed and path count: research/verified_2026-09-27/strategy_mc.py (VRF inputs:
  JPM 2026 LTCMA U.S. large cap 6.70% compound / 16.47% vol, intermediate Treasuries 4.00%; ladder $292,264).
- Glide paths (equity share of the whole portfolio, years 2027-2032) and gift/kept splits: ASSUMPTION, chosen to
  describe each firm's approach. Firm B uses strategy_mc.py's own default glide (reproduces 3.2% miss).
- Firm D numbers are not computed here; they are quoted from phase_E/E6_final_spec.md (E6_final_checks.py).
Run from the repo root: .venv/bin/python research/insight_v1/scripts/E7_tournament_field_numbers.py
"""
import sys
import numpy as np
sys.path.insert(0, "research/verified_2026-09-27")
from strategy_mc import simulate  # noqa: E402

GLIDES = {
    "A glide 65->20": (0.65, 0.60, 0.50, 0.40, 0.30, 0.20),
    "B growth-first": (0.75, 0.75, 0.75, 0.75, 0.60, 0.40),
    "C themed 65->25": (0.65, 0.65, 0.65, 0.55, 0.40, 0.25),
    "E 60/40->40/60": (0.60, 0.60, 0.55, 0.50, 0.40, 0.40),
    "F optimiser 55->20": (0.55, 0.50, 0.45, 0.35, 0.25, 0.20),
}
P = (5, 10, 25, 50, 75, 90, 95)

def k(x): return f"${x/1000:.0f}k"

for name, g in GLIDES.items():
    print(f"\n== {name} {g}")
    for dep in (150_000, 75_000, 0):
        r = simulate("G", glide=g, deposit_2028=dep)
        s = r["surplus"]
        line = f"  deposit {dep:>7}: miss {r['shortfall_prob']*100:.1f}%"
        if dep == 150_000:
            q = np.percentile(s, P)
            line += "  surplus " + " ".join(f"p{p}={k(v)}" for p, v in zip(P, q))
            tail = np.sort(s)[: int(0.05 * s.size)].mean()
            line += f"  CVaR5={k(tail)}"
        print(line)
    avg_eq = np.mean(g)
    print(f"  average equity share 2027-32: {avg_eq*100:.1f}%")

# Facility gift = share of the 2033 money left after the reserve (ASSUMPTION per firm); kept = the rest.
SPLITS = {"A glide 65->20": 0.85, "B growth-first": 0.90, "C themed 65->25": 0.85,
          "E 60/40->40/60": 0.80, "F optimiser 55->20": 0.85}
print("\n== Facility gift percentiles (gift = share x max(surplus, 0))")
for name, share in SPLITS.items():
    s = np.maximum(simulate("G", glide=GLIDES[name])["surplus"], 0)
    q = np.percentile(share * s, P)
    print(f"  {name} share {share:.0%}: " + " ".join(f"p{p}={k(v)}" for p, v in zip(P, q)))
