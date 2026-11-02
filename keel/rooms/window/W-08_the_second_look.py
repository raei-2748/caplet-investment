"""W-08, the Window, Tue 3 Nov 2026 (round 7 beat 2). (Keel is a simulated team, AI-written.) AI-generated (Claude
Code). MODEL.

"The second look": V54 P8 names one step ("Before she names the range, we price that gap at that day's yields, plus a
cushion, and move that much from the stocks Laura keeps into Treasuries"), and P9 says "From 2033, the ladder and the
money set aside for its gap become the operating reserve". The model the cheques' numbers come from (L-11's at_2033,
used by L-13 -> L-14 -> L-16, A0) takes a SECOND step V54 never names: in January 2033 it prices the gap again at that
day's yields, adds the cushion again, and tops the reserve up from her kept stocks first, then from the gift. The
Genius Lab showed (L-16, A1) that dropping one unnamed step, the cushion, cut the cheques paid in full from 99.8% to
76%. Does dropping the second look matter as much?

Arms (L-16's chain, unchanged; one branch patched, the way LR-10 patches it):
  A0   L-16's A0 = V54 as modelled: naming-day set-aside with a $7,500 cushion + the January 2033 second look
  W0   V54 as written: the naming-day set-aside with its cushion, and NO second look in 2033 (whatever has grown
       since naming day is not topped up; any later gap is a cheque short)
  W1   W0 with no cushion (V52 as written, no second look)
  W0f, W1f, A0f   Kai's repair of the test (round 2): what the stocks can't cover on naming day leaves the range's
       money that day into the same bills (LR-10's y_ at phi 0, up to all that is locked), and every arm is scored
       on the realised gap (`shortfall`) instead of max(shortfall, S33). W0 and W1 left that money with Laura and
       counted futures where yields rose after 2033 as short.

Re-uses the Genius Lab's L-16 chain (curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0). A0 must still equal L-14's XR (the Lab's assert). Writes W-08_results.json beside
this file; never touches the Lab's results.

    python3 keel/rooms/window/W-08_the_second_look.py S0 S6      # ~70 s each
"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
L16P = HERE.parent / "lab" / "L-16_two_jobs_one_pocket" / "run.py"
_s = importlib.util.spec_from_file_location("L16", L16P); L16 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L16)

PATCHES = [
    ("    def arm16(C_, backstop=False, share=False):",
     "    def arm16(C_, backstop=False, share=False, no33=False, fair_=False):"),
    ("            lockd_ = lockd; top_ = top\n        topq",
     "            lockd_ = lockd; top_ = top\n"
     "            if fair_:                                                    # W0f (Kai): the range's cut pays the gap\n"
     "                y_ = np.minimum(np.maximum(need31_ - x_, 0), lockd / bill2)  # on naming day, into the same bills\n"
     "                x_ = x_ + y_\n"
     "                lockd_ = lockd - y_ * bill2\n"
     "        topq"),
    ("        cash, sold, g = at_2033(c0, S33 + C_, half_b_, True, topq, lockd_)\n",
     "        cash, sold, g = at_2033(c0, S33 + C_, half_b_, True, topq, lockd_)\n"
     "        if no33:                                                         # W-08: no second look in 2033\n"
     "            cash = c0; sold = np.zeros(N); g = np.minimum(topq, lockd_)\n"),
    ("        post = np.maximum(S33 + extra_ - cash, 0)",
     "        post = np.maximum((shortfall if fair_ else S33 + extra_) - cash, 0)   # fair_: the realised gap (Kai)"),
    ('            "G gap first, then halve (margin 7.5k)": dict(C_=7500, share=True)}',
     '            "G gap first, then halve (margin 7.5k)": dict(C_=7500, share=True),\n'
     '            "W0 V54 as written: cushion, no second look": dict(C_=7500, no33=True),\n'
     '            "W1 no cushion, no second look": dict(C_=0, no33=True),\n'
     '            "A0f A0, cut paid on naming day, realised gap": dict(C_=7500, fair_=True),\n'
     '            "W0f W0, cut paid on naming day, realised gap": dict(C_=7500, no33=True, fair_=True),\n'
     '            "W1f W1, cut paid on naming day, realised gap": dict(C_=0, no33=True, fair_=True)}'),
]
b = L16.BLOCK16
for old, new in PATCHES:
    assert b.count(old) == 1, old[:60]
    b = b.replace(old, new)
L16.BLOCK16 = b
L14 = L16.L14


def main():
    blk14 = L14.BLOCK14
    assert blk14.count("for k in (0.80, 0.65):") == 1
    blk14 = blk14.replace("for k in (0.80, 0.65):", "for k in (0.80, 0.76):") + L16.BLOCK16
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', blk14)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)
    L14.L10.SCENARIOS.setdefault("S9 yields 1pt lower before the build + 2028 deposit halved",
                                 dict(dy_build=-1.0, d28=75_000.0))
    names = {k.split()[0]: k for k in L14.L10.SCENARIOS}
    f = HERE / "W-08_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V54's design (= V52/V53 as modelled) via L-13 -> L-14 -> L-16, W0/W1 added | MODEL")
    keep = ["A0 V52 as modelled (margin 7.5k)", "A1 V52 as written (no margin)",
            "W0 V54 as written: cushion, no second look", "W1 no cushion, no second look",
            "A0f A0, cut paid on naming day, realised gap", "W0f W0, cut paid on naming day, realised gap",
            "W1f W1, cut paid on naming day, realised gap"]
    for k in sys.argv[1:] or ["S0", "S6"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]
        out[names[k]] = {n: r[n] for n in keep}
        out[names[k]]["worst_tenth_of_naming_day_gaps"] = {n: r["worst_tenth_of_naming_day_gaps"][n] for n in keep}
        print(names[k], flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
