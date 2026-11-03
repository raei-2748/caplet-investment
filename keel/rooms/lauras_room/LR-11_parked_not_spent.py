"""AI-generated (Claude Code), Tue 3 Nov 2026, Laura's Room (round 7 beat 6; huddle H-024). MODEL.
(Keel is a simulated team, AI-written.) LR-11 "parked, not spent?": the Genius Lab's Kai's lock (L-17, arm KW, WInS-true)
is paid for by the stocks Laura keeps; this room's Monday call (LR-10, H25: the kept half pays only down to a quarter of
itself, the rest lowers the range before anyone hears it) was not taken into V54. Does H25 still earn its place once
the lock replaces the cushion?

Arms (L-17's chain unchanged; its BLOCK17 is reused, with one parameter added to its arm function):
  KW       L-17's KW, re-run here; must equal L-17's results.json (asserted)
  KW+H25   KW, but the stocks Laura keeps pay the lock only down to a quarter of themselves; the rest comes from the
           range's money on naming day (the range is lowered by it before anyone hears it)
  KW+H50   the same, down to half of themselves (LR-10's other arm)
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17 | MODEL.
Run from repo root: python3 keel/rooms/lauras_room/LR-11_parked_not_spent.py [S0 S6 S9]  (~40 s each)
Writes LR-11_results.json next to this file; never touches the Lab's results.json."""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
L17P = HERE.parent / "lab" / "L-17_interest_that_earns_nothing" / "run.py"
_s = importlib.util.spec_from_file_location("L17", L17P); L17 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L17)
L16, L14 = L17.L16, L17.L14
KW_NAME = "KW WInS-true: coupons reinvested before naming sit in coupon bonds whose coupons earn 0%"


def patched_block17():
    b = L17.BLOCK17
    reps = [
        ("    def arm17(gaps, how):", "    def arm17(gaps, how, phi=0.0):"),
        ("        x_ = np.minimum(cost, 0.5 * V31)                                 # from the stocks Laura keeps first (P8)",
         "        x_ = np.minimum(cost, (1 - phi) * 0.5 * V31)                     # kept stocks first, down to phi of themselves"),
        ("        u31_ = ceil5(np.maximum(cost - 0.5 * V31, 0))",
         "        u31_ = ceil5(np.maximum(cost - (1 - phi) * 0.5 * V31, 0))"),
        ("    out16[\"L17\"] = out17",
         "    for phi_, nm_ in ((0.25, \"KW+H25\"), (0.5, \"KW+H50\")):\n"
         "        r, short, taken, rem = arm17(g_kw, \"par0\", phi_)\n"
         "        r[\"worst_tenth_of_naming_day_gaps\"] = {\"p_nothing_left\": sm((rem[bad] < np.maximum(500, 0.02 * half[bad])).mean()),\n"
         "            \"share_taken_p50\": round(float(np.median(taken[bad])), 3), \"p_cheque_short_any\": sm((short[bad] > 0.5).mean())}\n"
         "        r[\"kept_half\"][\"left_2033_mean\"] = round(float(rem.mean()))\n"
         "        out17[nm_] = r\n"
         "    rkw, _, _, remkw = arm17(g_kw, \"par0\", 0.0)\n"
         "    out17[\"KW_left_2033_mean\"] = round(float(remkw.mean()))\n"
         "    out16[\"L17\"] = out17"),
    ]
    for old, new in reps:
        assert b.count(old) == 1, old
        b = b.replace(old, new)
    return b


def main():
    b = L16.BLOCK16
    assert b.count('    lr["L16"] = out16') == 1
    L16.BLOCK16 = b.replace('    lr["L16"] = out16', patched_block17() + '\n    lr["L16"] = out16')
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
    lab = json.loads((L17P.parent / "results.json").read_text())
    f = HERE / "LR-11_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17, KW+H25/H50 added | MODEL")
    for k in sys.argv[1:] or ["S0", "S6", "S9"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]["L17"]
        kw = r[KW_NAME]
        if names[k] in lab:                                                # KW must equal the Lab's own run
            for m in ("cheques_paid_in_full", "gift_mean", "laura_2042_mean", "p_range_lowered_on_naming_day"):
                assert lab[names[k]][KW_NAME][m] == kw[m], (k, m)
        row = {"KW": kw, "KW_left_2033_mean": r["KW_left_2033_mean"], "KW+H25": r["KW+H25"], "KW+H50": r["KW+H50"],
               "check": "KW identical to the Lab's L-17 results.json"}
        out[names[k]] = row
        print(names[k], json.dumps({a: {m: row[a][m] for m in ("cheques_paid_in_full", "p_range_lowered_on_naming_day",
              "range_cut_p50_when", "p_top_reached", "gift_mean", "laura_2042_mean")} | {"kept": row[a]["kept_half"]}
              for a in ("KW", "KW+H25", "KW+H50")}), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
