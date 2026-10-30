"""AI-generated (Claude Code), Fri 30 Oct 2026, the Archive (round 3 beat 9). MODEL.
(Keel is a simulated team, AI-written.) Checks V33 paras 6-7 ("a cheque can fail only if ... yields drop two points
before we buy and her 2028 deposit comes in under about $85,000"; "her 2028 deposit never carries a cheque") on
V29/V33's design (LR8 "MB+T +lock"; the L-13 slide moves only the range, so cheques are unchanged). The $85k in V33
comes from K07 T7, which ran V25's design. Extends the Lab's L-12 corner grid to -2pt and larger deposits.
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 | MODEL.
Run from repo root: python3 keel/rooms/archive_checks/A25_deposit_corner.py"""
import json, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "lab" / "L-12_four_doors" / "run_requests.py"
_spec = importlib.util.spec_from_file_location("L12R", P)
R = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(R)
L11 = R.L11

L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', R.build(False))
out = {"stamp": "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 | V29/V33 design (LR8 MB+T +lock) | MODEL"}
for dy, deps in ((0.0, (40_000.0,)), (-1.0, (65_000.0, 100_000.0)),
                 (-2.0, (50_000.0, 75_000.0, 85_000.0, 100_000.0, 125_000.0, 150_000.0))):
    for d28 in deps:
        key = f"dy_build {dy:+g}pt, 2028 deposit ${d28:,.0f}"
        r = L11.run(d28=d28, dy_build=dy)["LR05"]["L12_requests"]
        out[key] = {"p_payment_short_over_1k": r["p_payment_short_over_1k"]}
        print(key, json.dumps(out[key]), flush=True)
(HERE / "A25_results.json").write_text(json.dumps(out, indent=1))
