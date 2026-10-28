"""FICTION (the room) + real work. Long Room, Wed 28 Oct 2026 (round 1 beat 8): the repair test.
Amara's flaw in C6+MC (Laura's Room LR-05): the 2031 mark counts on Laura's half to cover the coupon gap, but the half
is only sold in January 2033. From 2031 to 2033 a share price still stands behind the cheques' coupon money, and the
sale itself is a fixed-dollar sale on a fixed date: the forced sale V28's paragraph 4 warns about.
Repair (Jun): bank it at the mark. On the day Laura names her range (Jan 2031), the part of the gap + cushion that her
half covers is sold from her half into short Treasuries, the same day the promised half moves. After that no share
price stands behind any cheque. Two forms:
  MB    strict: from 2031 Laura's half is never a source; any growth in the gap 2031-33 falls on leftover cash, then the
        gift (top first, bottom last)
  MB+T  as MB, but in Jan 2033 any growth in the gap beyond what was banked may still come from Laura's half
  +lock each arm again with the promised half moved into short Treasuries on naming day, as V26-V28 say (the shared
        model never did this: Kai's catch)
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | basis: LR-05's script and L-11's run.py unchanged; this block is appended after LR-05's | MODEL.
Run from repo root: python3 keel/rooms/long_room/LR8_banked_at_the_mark/run.py [S0 S1 S6]  (~3 min each)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
LR = HERE.parents[1] / "lauras_room" / "LR-05_who_pays_the_blind_fifth.py"
_spec = importlib.util.spec_from_file_location("LR05", LR)
LR05 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LR05)
L11 = LR05.L11

ADD = '''
    # ---- Long Room beat 8: bank it at the mark ----
    bill2 = np.ones(N)
    for j in (3, 4):
        bill2 *= 1 + np.maximum(curve(.25) + sh(t28 + j), YMIN) / 100              # short Treasuries, 2031 -> 2033
    need31 = np.maximum(S31 + C - L33, 0)
    x = np.minimum(need31, 0.5 * V31)                                               # sold from Laura's half, Jan 2031
    keep = np.where(V31 > 0, 1 - x / np.maximum(0.5 * V31, 1e-9), 1.0)             # share of her half still in stocks
    q_mc = bottom - ceil5(np.maximum(S31 + C - L33 - 0.5 * V31, 0))                 # same quoted bottom as C6+MC
    def lab(name, short, g, sold33, sold_value_lost, rel, half33):
        r = lr05(short, g, top, q_mc, sold33)
        l42 = (half33 - sold33) * g_after + rel
        r["laura_2042_half_plus_release_p5_p50"] = [round(float(np.percentile(l42, 5))), round(float(np.median(l42)))]
        r["p_stocks_sold_2031"] = sm((x > 1).mean()); r["median_sold_2031_when_sold"] = md(x, x > 1)
        r["p_stocks_sold_2033"] = sm((sold33 > 1).mean())
        r["median_2033_value_given_up_by_selling_in_2031"] = md(sold_value_lost, x > 1)
        lr[name] = r
    # C6+MC reproduced with Laura's 2042 money, for a like-for-like row
    cash, sold, g1 = at_2033(L33, S33 + C, half, True, top, floor_paid + half)
    lab("C6+MC (check)", np.maximum(S33 + extra_ - cash, 0), g1, sold, np.zeros(N),
        np.maximum(cash - S33 - extra_, 0), half)
    half_b = half * keep                                                            # her half in 2033 after the 2031 sale
    lost = x * (V33 / np.maximum(V31, 1e-9)) - x * bill2                            # stocks' 2031-33 move given up (+ = cost)
    for name, allow in (("MB strict", False), ("MB+T top-up", True)):
        cash, sold, g = at_2033(L33 + x * bill2, S33 + C, half_b, allow, top, floor_paid + half)
        lab(name, np.maximum(S33 + extra_ - cash, 0), g, sold, lost, np.maximum(cash - S33 - extra_, 0), half_b)
    # Kai's catch: the shared model never moves the promised half into Treasuries in 2031 (gift = floor + 0.5 * V33,
    # capped), though V26-V28 say "the day she names it, we lock it". "+lock" arms do what the draft says: the
    # promised half (0.5 * V31) moves into short Treasuries on naming day and earns bill rates to 2033.
    lockd = floor_paid + 0.5 * V31 * bill2
    cash, sold, g = at_2033(L33, S33 + C, half, True, top, lockd)
    lab("C6+MC +lock", np.maximum(S33 + extra_ - cash, 0), g, sold, np.zeros(N), np.maximum(cash - S33 - extra_, 0), half)
    for name, allow in (("MB strict +lock", False), ("MB+T +lock", True)):
        cash, sold, g = at_2033(L33 + x * bill2, S33 + C, half_b, allow, top, lockd)
        lab(name, np.maximum(S33 + extra_ - cash, 0), g, sold, lost, np.maximum(cash - S33 - extra_, 0), half_b)
    cash, sold, g = at_2033(L33 + res33, S33 + res33, halfz, True, topz, fpz + 0.5 * V31 * f * bill2)
    ra = lr05(np.maximum(S33 + extra_ - cash, 0), g, topz, botz - ceil5(np.maximum(S31 - L33 - 0.5 * V31 * f, 0)), sold)
    lr["A+M +lock"] = ra
    res["LR05"] = lr'''


def main():
    assert LR05.BLOCK.count('    res["LR05"] = lr') == 1
    block = LR05.BLOCK.replace('    res["LR05"] = lr', ADD)
    assert L11.EXTRA.count('    out["L11"] = res') == 1
    L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', block)
    keys = sys.argv[1:] or ["S0", "S1", "S6"]
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | MODEL"
    for k in keys:
        name = L11.SCEN[k]
        r = L11.run(**L11.L10.SCENARIOS[name])["LR05"]
        out[name] = {k2: r[k2] for k2 in ("C6+MC", "C6+MC (check)", "MB strict", "MB+T top-up", "A+M", "C6+MC +lock", "MB strict +lock", "MB+T +lock", "A+M +lock")}
        print(name, json.dumps(out[name], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
