"""AI-generated (Claude Code), Sat 31 Oct 2026, the Window (round 4 beat 2). MODEL. (Keel is a simulated team, AI-written.)
Design-stamp check of V39's "about one future in thirty missed a cheque" (the team's first plan: about three-quarters
in stocks, reserve bought in 2033). That number is the 27 Sep model (keel/library/verified_2026-09-27/strategy_mc.py,
growth-first "G") on J.P. Morgan's 2026 US large cap (6.7%) and the 25 Sep curve. V39 states "world stocks at 7.5% a
year" (J.P. Morgan 2027, global equities). This re-runs the same model, unchanged, on that basis.
Run from repo root: python3 keel/rooms/window/W-04_growth_first_restamp.py  (about 10 s)"""
import pathlib, types, numpy as np

SRC = pathlib.Path(__file__).resolve().parents[2] / "library" / "verified_2026-09-27" / "strategy_mc.py"
code = SRC.read_text()
assert code.count("rate33 = 0.0526 + rate_sd") == 1
code = code.replace("rate33 = 0.0526 + rate_sd", "rate33 = RATE33_BASE + rate_sd").replace(
    'if __name__ == "__main__":', 'if False:')
smc = types.ModuleType("smc"); smc.RATE33_BASE = 0.0526
exec(compile(code, str(SRC), "exec"), smc.__dict__)


def lp_vol(compound, vol):
    """lognormal log-mean/log-sd with the given compound (median) return and arithmetic vol (bisection)."""
    mu, lo, hi = np.log(1 + compound), 1e-4, 1.0
    f = lambda s: np.sqrt((np.exp(s * s) - 1) * np.exp(2 * mu + s * s)) - vol
    for _ in range(100):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) < 0 else (lo, m)
    return mu, (lo + hi) / 2


EQ26, BD26 = smc.EQ, smc.BD
runs = [
    ("27 Sep basis (JPM 2026 US large cap 6.7%, bonds 4.0%, 25 Sep curve)", EQ26, BD26, 0.0526),
    ("JPM 2027: world 7.5% compound, vol 16.78%; US int. Treasuries 4.6%, vol 3.48%; 25 Sep curve",
     lp_vol(0.075, 0.1678), lp_vol(0.046, 0.0348), 0.0526),
    ("JPM 2027 as above + 22 Oct curve level (ladder $298,861 vs $292,264 at DV01 $289/bp = about 23bp lower)",
     lp_vol(0.075, 0.1678), lp_vol(0.046, 0.0348), 0.0526 - (298_861 - 292_264) / 289 / 10_000),
]
for name, eq, bd, r33 in runs:
    smc.EQ, smc.BD, smc.RATE33_BASE = eq, bd, r33
    for dep in (150_000, 75_000, 0):
        p = smc.simulate("G", deposit_2028=dep)["shortfall_prob"]
        print(f"{name} | 2028 deposit ${dep:,}: P(reserve not fully funded in 2033) = {p*100:.2f}% (1 in {1/p:.0f})")
