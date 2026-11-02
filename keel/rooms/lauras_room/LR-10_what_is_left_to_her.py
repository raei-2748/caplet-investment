"""LR-10, Laura's Room, Mon 2 Nov 2026 (round 6 beat 6). (Keel is a simulated team, AI-written.) MODEL.

What is left to her? The Genius Lab's L-16 seed for this room: V53 (D33) P8 sets the reinvestment gap, plus a cushion,
aside "from the stocks Laura keeps, so her flexibility shrinks before her promise does", and only "Whatever the stocks
can't cover lowers the whole range." In L-16 that empties the kept half by January 2033 in about 1 future in 5 (base)
and 2 in 3 (yields 2 points lower for good). The case: Laura "recognizes that committing all remaining assets could
limit her financial flexibility as the project develops" (:102-103), and the strategy must preserve "appropriate
financial flexibility when determining the facility contribution" (:145, strategy bullet 5).

The question the room asks: BEFORE she names the range nothing has been promised to anyone, so P7's reason ("a number
said aloud ... cannot be quietly halved") does not yet apply. What does it cost to stop the gap at part of her kept
half on naming day, and lower the whole range for the rest, while keeping V53's order after naming (her flexibility
first, then the gift)?

Arms (L-16's six reproduced unchanged, plus two):
  H25  the kept half pays the gap + cushion only down to a quarter of itself; the rest leaves the promised half on
       naming day (set aside in bills with the rest) and lowers both ends of the quote by that much (ceil $5k)
  H50  the same, down to half of itself
After naming nothing changes: in January 2033 the kept stocks pay any top-up first, then the gift (V53 P8/P9's order).

Re-uses the Lab's L-16 chain (curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% | 200,000 paths, seed 20261016 |
rho 0.5 unless S0 | V52's design = V53's) by patching one branch of its block; A0 must still equal L-14's XR (the Lab's
assert). Writes LR-10_results.json beside this file; never touches the Lab's results.

    python3 keel/rooms/lauras_room/LR-10_what_is_left_to_her.py            # S0 S2 S6 S9
    python3 keel/rooms/lauras_room/LR-10_what_is_left_to_her.py S0         # a subset
"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
L16P = HERE.parent / "lab" / "L-16_two_jobs_one_pocket" / "run.py"
_s = importlib.util.spec_from_file_location("L16", L16P); L16 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L16)

PATCHES = [
    ("    def arm16(C_, backstop=False, share=False):",
     "    def arm16(C_, backstop=False, share=False, phi_=0.0):"),
    ("            x_ = np.minimum(need31_, 0.5 * V31)                          # from the kept half only (V52)\n"
     "            keep_ = np.where(V31 > 0, 1 - x_ / np.maximum(0.5 * V31, 1e-9), 1.0)\n"
     "            half_b_ = half * keep_\n"
     "            u31_ = ceil5(np.maximum(need31_ - 0.5 * V31, 0))\n"
     "            lockd_ = lockd; top_ = top",
     "            x_ = np.minimum(need31_, (1 - phi_) * 0.5 * V31)             # kept half pays, down to phi_ of itself\n"
     "            keep_ = np.where(V31 > 0, 1 - x_ / np.maximum(0.5 * V31, 1e-9), 1.0)\n"
     "            half_b_ = half * keep_\n"
     "            u31_ = ceil5(np.maximum(need31_ - (1 - phi_) * 0.5 * V31, 0))  # both ends of the quote come down\n"
     "            lockd_ = lockd; top_ = top\n"
     "            if phi_ > 0:                                                 # LR-10: the rest leaves the promised half\n"
     "                y_ = np.minimum(np.maximum(need31_ - x_, 0), 0.5 * V31)  # on naming day, into the same bills\n"
     "                assert (y_ * bill2 <= lockd + 1e-6).all()\n"
     "                x_ = x_ + y_\n"
     "                lockd_ = lockd - y_ * bill2"),
    ('            "G gap first, then halve (margin 7.5k)": dict(C_=7500, share=True)}',
     '            "G gap first, then halve (margin 7.5k)": dict(C_=7500, share=True),\n'
     '            "H25 kept half pays down to a quarter, then the range (margin 7.5k)": dict(C_=7500, phi_=0.25),\n'
     '            "H50 kept half pays down to half, then the range (margin 7.5k)": dict(C_=7500, phi_=0.5)}'),
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
    f = HERE / "LR-10_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V52's design (= V53's) via L-13 -> L-14 -> L-16, H25/H50 added | MODEL")
    for k in sys.argv[1:] or ["S0", "S2", "S6", "S9"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]
        out[names[k]] = r
        print(names[k], flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
