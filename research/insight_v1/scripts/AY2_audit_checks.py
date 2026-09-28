"""AY2_audit_checks.py - audit checks behind the AY2 corrections to D7 (band odds) and D8 (devil's advocate numbers).

Agent AY2 (cluster auditor: Wharton intent, practice benchmark, communication), insight_v1 run, 2026-09-28.

What it does (plain English):
[1] D8 M109 used a Treasury-forward middle case ($204k) next to a p5 ($159k) from a different model with lower bond
    inputs, and called the gap "an order of magnitude". This re-runs the growth money with ONE set of inputs, so the
    median gain and the bad-case (p5) cost of 50/60/70% stocks are measured against the same Treasury-only figure.
[2] D7 M002 reported the chance that a WInS rebalancing band fires by Oct 20 as 0.00% / 0.12% / 0.29% from a normal
    (thin-tailed) model. This re-runs the same window with fat tails (Student-t, 3 degrees of freedom) and with a
    crisis-level volatility, to see whether the conclusion ("no sensible band will fire; do not plan a discipline
    trade") survives, and whether two-decimal odds are meaningful.

Inputs (with status labels):
- Growth money: $7,736 left over in 2027 (F-104, VERIFIED-REPO-FILE via the verified curve script), held at the bond
  rate in 2027 (ticket: T-bills in 2027); +$150,000 on 2028-01-01 (case, VERIFIED-REPO-FILE); yearly rebalance
  2028-2032; value on 2033-01-01.
- Equity: JPM 2026 LTCMA AC World 7.00% compound, 16.78% vol (VERIFIED-REPO-FILE via brief s6); lognormal i.i.d.
  (ASSUMPTION, same family as the verified model).
- Growth-money bonds: 5.23%/yr (the 2028->2033 forward from the 2026-09-25 curve, D8 script; a break-even, NOT
  lockable) or 3.9%/yr (D8's short-Treasury ASSUMPTION); deterministic (ASSUMPTION: ignores rate risk in the bonds and
  in the Treasury-only benchmark).
- Band window: 13 U.S. trading days of moves after an Oct 1 fill to Oct 20, weekly checks Oct 2, 9, 16, 20 (as in
  D7_rule_trigger_odds.py). Relative volatility = equity volatility only (VGSH ~1.8% ignored; ASSUMPTION, tiny effect).
  Volatility 16.78% (JPM) or 35% (crisis-level; ASSUMPTION for a stress regime). Student-t(3) scaled to the same
  standard deviation (ASSUMPTION for fat tails).
Seeds fixed (20260927). Outputs are model outputs, not forecasts.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/AY2_audit_checks.py
Results are recorded in research/insight_v1/phase_D/audit_judges_practice_comms.md and in the "Audit corrections
(AY2)" sections of D7_wharton_intent.md and D8_practice.md.
"""
import numpy as np

SEED = 20260927


def growth_money_percentiles():
    rng = np.random.default_rng(SEED)
    n = 200_000
    g, vol = 1.07, 0.1678
    sig = np.sqrt(np.log(1 + vol**2 / (g + vol**2 / 2) ** 2))  # log-sd consistent with 16.78% vol (~0.154)
    mu = np.log(g)
    print("[1] Growth money on 2033-01-01, ONE input set (AC World equity; deterministic bonds)")
    for rb in (0.0523, 0.039):
        base = None
        for w in (0.0, 0.5, 0.6, 0.7):
            s = np.full(n, 7736 * (1 + rb)) + 150_000
            for _ in range(5):  # 2028..2032
                re = np.exp(rng.normal(mu, sig, n)) - 1
                s = s * (1 + w * re + (1 - w) * rb)
            p5, p50, p95 = np.percentile(s, [5, 50, 95])
            if w == 0.0:
                base = p50
                print(f"    bonds {rb*100:.2f}%: Treasury-only ${base:,.0f}")
                continue
            print(f"    bonds {rb*100:.2f}%, stocks {w*100:.0f}%: p5 ${p5:,.0f} ({p5-base:+,.0f}) / "
                  f"p50 ${p50:,.0f} ({p50-base:+,.0f}) / p95 ${p95:,.0f} ({p95-base:+,.0f})")


def band_odds():
    rng = np.random.default_rng(SEED)
    n, days = 400_000, 13
    check = [0, 5, 10, 12]  # Oct 2, 9, 16, 20

    def p_hit(w0, lo, hi, steps):
        r = np.exp(np.cumsum(steps, axis=1)[:, check])
        w = w0 * r / (w0 * r + (1 - w0))
        return ((w < lo) | (w > hi)).any(axis=1).mean()

    print("\n[2] P(a WInS band fires by Oct 20), weekly checks; growth band = VT share of growth money; whole-book")
    print("    band = VT share of the $300k (20.5% +/- 2 points)")
    for label, vol, df in [("normal, 16.8% vol (D7 model)", 0.1678, None), ("t(3) fat tails, 16.8% vol", 0.1678, 3),
                           ("normal, 35% crisis vol", 0.35, None), ("t(3), 35% crisis vol", 0.35, 3)]:
        sd = vol / np.sqrt(252)
        if df is None:
            steps = rng.normal(0, sd, (n, days))
        else:
            steps = rng.standard_t(df, (n, days)) * sd / np.sqrt(df / (df - 2))
        a = p_hit(0.60, 0.55, 0.65, steps)
        b = p_hit(0.60, 0.57, 0.63, steps)
        c = p_hit(0.205, 0.185, 0.225, steps)
        print(f"    {label:30s} growth 55-65: {a:6.2%} | growth 57-63: {b:6.2%} | whole-book +/-2: {c:6.2%}")


if __name__ == "__main__":
    growth_money_percentiles()
    band_odds()
