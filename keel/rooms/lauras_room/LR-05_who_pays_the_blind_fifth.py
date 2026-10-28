"""FICTION (the room) + real work. Laura's Room LR-05 (Wed 28 Oct 2026, round 1 beat 6): who pays for the coupon gap's
blind fifth, the co-sponsors' bottom (L-11 challenger A) or the gift in a bad year (champion C6)?
L-11 compared A and C6 without the 2031 mark Keel adopted on 27 Oct (LR-04, survived the Courtroom's C-02): the bottom
is cut in 2031 by the coupon gap already visible that the 2027 leftover and Laura's half can't cover. This run puts the
mark into both arms, so tonight's Long Room judges like against like.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | basis: L-11's run.py (L-10's patches, ips_numbers.py) unchanged; this block is appended | MODEL.
Run from repo root: python3 keel/rooms/lauras_room/LR-05_who_pays_the_blind_fifth.py [S0 S1 S6]  (~3 min each)
Designs (all cushions/holdings $7,500; S31 = the ten payments' gap as seen with rates frozen on 1 Jan 2031):
  A        L-11 D2: $7.5k bought 2 Jan 2028 before the floor; bottom = floor rule on the smaller floor (no mark)
  A+M      A, and in 2031 the bottom is cut by max(S31 - L33 - Laura's half(2031), 0), rounded up to $5k
  C6       L-11 D1 cushion 7.5k (Jan 2033 set-aside of the visible gap + $7.5k), no mark
  C6+M     C6 with LR-04's mark as adopted (visible gap only)
  C6+MC    C6 with the mark carrying the cushion too: cut by max(S31 + 7.5k - L33 - Laura's half(2031), 0)
  C6F+MC   C6 with Laura's half never a source (stocks never pay a cheque); mark = S31 + 7.5k - L33
  D0+M     no coupon rule, LR-04's mark (reference)
Co-sponsor money lost = 1 - (quoted bottom / unpadded floor-rule bottom)^E, E = 0.94 (List & Lucking-Reiley, as LR-04)
and 0.5; a heroic extrapolation: read the ranking, not the decimals."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
LAB = HERE.parent / "lab" / "L-11_birthday_cure"
import importlib.util   # noqa: E402
_spec = importlib.util.spec_from_file_location("L11_birthday_cure", LAB / "run.py")   # L-11 imports L-10 as "run"
L11 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(L11)

BLOCK = '''
    # ---- LR-05 (Laura's Room): the 2031 mark in both arms ----
    S31 = proj_at(2031)
    E1 = np.log(6) / np.log(6.7)
    ceil5 = lambda x: np.ceil(x / 5000) * 5000
    def lr05(short, gift_, top_, q, sold):
        base = np.maximum(bottom, 1.0)
        brk = gift_ < q - 1e-6
        tot = short + unfilled
        return {"p_payment_short_over_1k": sm((tot > 1000).mean()),
                "quoted_bottom_p5_p50": [round(float(np.percentile(q, 5))), round(float(np.median(q)))],
                "mean_cut_vs_floor_rule": round(float((bottom - q).mean())),
                "p_cut_vs_floor_rule": sm(((bottom - q) > 1).mean()),
                "p_below_quoted_bottom": sm(brk.mean()), "n_below": int(brk.sum()),
                "median_miss": md(q - gift_, brk),
                "p_top_within_1k": sm((gift_ >= top_ - 1000).mean()),
                "gift_p5_p50": [round(float(np.percentile(gift_, 5))), round(float(np.median(gift_)))],
                "p_laura_half_sold": sm((sold > 1).mean()),
                "cosponsor_cost_pct_E094": round(float((1 - (np.maximum(q, 0) / base) ** E1).mean()) * 100, 2),
                "cosponsor_cost_pct_E05": round(float((1 - (np.maximum(q, 0) / base) ** 0.5).mean()) * 100, 2)}
    C = 7500
    lr = {"corr_S31_S33": round(float(np.corrcoef(S31, S33)[0, 1]), 3),
          "corr_S31_extra": round(float(np.corrcoef(S31, extra_)[0, 1]), 3),
          "p_S31_over_1k": sm((S31 > 1000).mean())}
    # D0 + mark
    cash, sold, g = at_2033(L33, S33, half, True, top, floor_paid + half)
    sh0 = np.maximum(S33 + extra_ - cash, 0); late = np.minimum(sh0, (half - sold) * g_after)
    lr["D0+M"] = lr05(sh0 - late, g, top, bottom - ceil5(np.maximum(S31 - L33 - 0.5 * V31, 0)), sold + late)
    # C6 arms
    cash, sold, g1 = at_2033(L33, S33 + C, half, True, top, floor_paid + half)
    sh1 = np.maximum(S33 + extra_ - cash, 0)
    lr["C6"] = lr05(sh1, g1, top, bottom, sold)
    lr["C6+M"] = lr05(sh1, g1, top, bottom - ceil5(np.maximum(S31 - L33 - 0.5 * V31, 0)), sold)
    lr["C6+MC"] = lr05(sh1, g1, top, bottom - ceil5(np.maximum(S31 + C - L33 - 0.5 * V31, 0)), sold)
    # C6, stocks kept out of the payments entirely (locked TNA reflection 3 read strictly): set-aside from leftover,
    # then the gift; Laura's half never sold for the coupon gap; the mark carries visible gap + cushion - leftover
    cash, sold, g1f = at_2033(L33, S33 + C, half, False, top, floor_paid + half)
    lr["C6F+MC"] = lr05(np.maximum(S33 + extra_ - cash, 0), g1f, top, bottom - ceil5(np.maximum(S31 + C - L33, 0)), sold)
    # A arms ($7.5k before the floor)
    r0 = np.minimum(C, R); f = np.maximum(R - r0, 0) / np.maximum(R, 1e-9)
    fpz = floor_paid * f; halfz = 0.5 * V33 * f
    botz = np.maximum(np.floor((R - r0 - 3700) / 5000) * 5000, 0); topz = R - r0 + 0.5 * V31 * f
    res33 = r0 * bill5
    cash, sold, g2 = at_2033(L33 + res33, S33 + res33, halfz, True, topz, fpz + halfz)
    sh2 = np.maximum(S33 + extra_ - cash, 0)
    lr["A"] = lr05(sh2, g2, topz, botz, sold)
    lr["A+M"] = lr05(sh2, g2, topz, botz - ceil5(np.maximum(S31 - L33 - 0.5 * V31 * f, 0)), sold)
    res["LR05"] = lr
    out["L11"] = res'''


def main():
    assert L11.EXTRA.count('    out["L11"] = res') == 1
    L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', BLOCK)
    keys = sys.argv[1:] or ["S0", "S1", "S6"]
    f = HERE / "LR-05_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | MODEL"
    for k in keys:
        name = L11.SCEN[k]
        r = L11.run(**L11.L10.SCENARIOS[name])
        out[name] = {"LR05": r["LR05"], "check_L11_D2_floor_7.5k": r["D2 birthday reserve 7.5k from floor"]["p_below_bottom_2033"],
                     "check_L11_D1_7.5k": r["D1 2033 set-aside, cushion 7.5k"]["p_below_bottom_2033"]}
        print(name, json.dumps(out[name], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
