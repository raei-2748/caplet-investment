"""Monte Carlo comparison of two strategies for Laura Gao, 2027-2033, using VERIFIED inputs where available.

VERIFIED inputs (files in competition/official_market_data/):
- Cost at 2027-01-01 of the ten $50k payments on the official 2026-09-25 Treasury curve: $292,264
  (research/verified_2026-09-27/official_curve_pv.py). Same curve: 2y par yield 4.81%.
- JPM 2026 LTCMA (USD): U.S. large cap compound 6.70%, arithmetic 7.94%, vol 16.47%;
  U.S. intermediate Treasuries compound 4.00%, arithmetic 4.06%, vol 3.48%; correlation between them -0.01.
ASSUMPTIONS (labelled; change them below and re-run):
- Annual returns are lognormal; log mean/sd are solved so compound and arithmetic returns match JPM exactly.
- 2033 Treasury yield level for Strategy G: today's implied forward cost plus a parallel shift ~ N(0, RATE_SD).
- The 2y Treasury yield in 2031 equals today's 4.81% (used only for the 2031 floor).
- Growth sleeve rebalanced annually; no fees, no taxes (taxes out of scope per case).
"""
import numpy as np

PATHS, SEED = 200_000, 20260927
LADDER_COST_2027 = 292_264          # verified, official curve
Y2 = 0.0481                          # verified 2y par yield, 2026-09-25
L2033_FWD = None                     # computed below from the same curve logic (see forward factor)

def lognorm_params(compound, arithmetic):
    mu = np.log(1 + compound)
    s2 = 2 * np.log((1 + arithmetic) / (1 + compound))
    return mu, np.sqrt(s2)

EQ = lognorm_params(0.0670, 0.0794)   # JPM U.S. large cap
BD = lognorm_params(0.0400, 0.0406)   # JPM U.S. intermediate Treasuries
RHO = -0.01                            # JPM correlation

# Forward value at 2033-01-01 of the ladder bought in 2027: cost grown at the 2027->2033 forward rate.
# From official_curve_pv.py: implied forward zero 2027->2033 = 5.08% (semiannual) -> factor over 6 years.
FWD_FACTOR_27_33 = (1 + 0.0508 / 2) ** 12
L2033_BASE = None
# Cost at 2033-01-01 of the ten payments if bought then at the forward curve: payments discounted at the forward
# zeros from 2033; approximated by a flat annual rate that reproduces the curve's 2027 value (5.26% flat -> $295k is
# the flat-rate equivalent). We price the 2033 annuity-due at flat 5.26% +/- shock (ASSUMPTION: flat curve in 2033).
def annuity_due(rate):
    t = np.arange(10)
    return (50_000 / (1 + rate[..., None]) ** t).sum(-1)

def simulate(strategy, deposit_2028=150_000, eq_mu_shift=0.0, rate_sd=0.010, eq_w=0.60, floor_share=0.80,
             glide=(0.75, 0.75, 0.75, 0.75, 0.60, 0.40)):
    rng = np.random.default_rng(SEED)
    z1 = rng.standard_normal((PATHS, 6)); z2 = rng.standard_normal((PATHS, 6))
    ze = z1; zb = RHO * z1 + np.sqrt(1 - RHO**2) * z2
    req = np.exp(EQ[0] + eq_mu_shift + EQ[1] * ze - 0) - 1
    rbd = np.exp(BD[0] + BD[1] * zb) - 1
    rate33 = 0.0526 + rate_sd * rng.standard_normal(PATHS)
    reserve_2033 = annuity_due(np.maximum(rate33, 0.0))

    if strategy == "G":   # growth first, buy the reserve in 2033
        v = np.full(PATHS, 300_000.0)
        for y in range(6):                     # years 2027..2032
            if y == 1: v += deposit_2028
            w = glide[y]
            v *= 1 + w * req[:, y] + (1 - w) * rbd[:, y]
        surplus = v - reserve_2033
        return {"shortfall_prob": float((surplus < 0).mean()), "surplus": surplus, "floor": None}

    # Strategy L: lock the ladder in 2027; growth sleeve holds everything else
    s = np.full(PATHS, 300_000.0 - LADDER_COST_2027)
    for y in range(4):                         # 2027..2030
        if y == 1: s += deposit_2028
        s *= 1 + eq_w * req[:, y] + (1 - eq_w) * rbd[:, y]
    floor = floor_share * s * (1 + Y2) ** 2    # 2031: lock floor in a 2y Treasury
    rest = (1 - floor_share) * s
    for y in (4, 5):
        rest *= 1 + eq_w * req[:, y] + (1 - eq_w) * rbd[:, y]
    surplus = floor + rest                     # ladder covers all ten payments by construction
    return {"shortfall_prob": 0.0, "surplus": surplus, "floor": floor}

def pct(x): return {p: int(round(np.percentile(x, p), -3)) for p in (5, 25, 50, 75, 95)}

if __name__ == "__main__":
    print(f"Equity log-params {EQ}, bond log-params {BD}")
    cases = [("Base (JPM official)", {}),
             ("2028 deposit only $75k", {"deposit_2028": 75_000}),
             ("2028 deposit missing", {"deposit_2028": 0}),
             ("Equities 1.7pp/yr weaker (5.0% compound)", {"eq_mu_shift": np.log(1.05) - np.log(1.067)}),
             ("2033 rate shock sd 1.5pp", {"rate_sd": 0.015})]
    for name, kw in cases:
        print(f"\n== {name}")
        for strat in ("L", "G"):
            r = simulate(strat, **kw)
            line = f"  {strat}: P(payments not fully funded)={r['shortfall_prob']*100:.1f}%  surplus 2033 p5/25/50/75/95={pct(r['surplus'])}"
            if r["floor"] is not None:
                line += f"\n     2031 floor (80% of sleeve in 2y Treasury) p5/50/95={[pct(r['floor'])[p] for p in (5,50,95)]}"
            print(line)
    print("\n== Growth-sleeve equity weight sensitivity (Strategy L, base)")
    for w in (0.5, 0.6, 0.7):
        r = simulate("L", eq_w=w)
        print(f"  equity {int(w*100)}%: surplus p5/50/95 = {[pct(r['surplus'])[p] for p in (5,50,95)]}")
