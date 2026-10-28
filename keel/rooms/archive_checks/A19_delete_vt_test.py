"""AI-generated (Claude Code), Wed 28 Oct 2026, the Archive (round 1 beat 9). MODEL.
A19's test, made a number: does Laura's stock fund (VT) ever decide WHETHER a cheque is paid, or only WHO pays?
Locked TNA reflection 3: "VT is where we allow ourselves to be wrong - because it's the only investment not standing
between Laura and a payment deadline." The Long Room (28 Oct) adopted "bank it at the mark, top-up" 4-1-1, with the
rider "the stocks decide who pays for the coupon gap, never whether a cheque is paid" (Felix dissenting: a reading,
not the words). The Archive's test is a deletion test: run the adopted plan, then run it again with Laura's stocks
worth nothing (2031 and 2033) or 60% lower, and compare every path's payment shortfall, cheque by cheque, path by path.
If no path's shortfall changes, the stocks stand behind no payment deadline, and the rider is a fact, not a reading.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | basis: Long Room LR8 run.py (LR-05, L-11, L-10, ips_numbers.py) unchanged; one block appended | MODEL.
Run from repo root: python3 keel/rooms/archive_checks/A19_delete_vt_test.py [S0 S1 S6]  (~3 min each)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "long_room" / "LR8_banked_at_the_mark" / "run.py"
_spec = importlib.util.spec_from_file_location("LR8", P)
LR8 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LR8)
LR05, L11 = LR8.LR05, LR8.L11

ARCH = '''
    # ---- Archive A19: the deletion test (stocks wiped, or 60% lower, in 2031 and 2033) ----
    def plan(scale, allow):
        # banked at the mark, with the 2031 lock (as V28 says); every stock value scaled by `scale`
        V31s = V31 * scale; V33s = V33 * scale
        x_ = np.minimum(need31, 0.5 * V31s)
        keep_ = np.where(V31s > 0, 1 - x_ / np.maximum(0.5 * V31s, 1e-9), 1.0)
        half_ = 0.5 * V33s * keep_
        lockd_ = floor_paid + 0.5 * V31s * bill2
        top_ = top - 0.5 * V31 + 0.5 * V31s
        cash_, sold_, g_ = at_2033(L33 + x_ * bill2, S33 + C, half_, allow, top_, lockd_)
        short_ = np.maximum(S33 + extra_ - cash_, 0) + unfilled
        return short_, sold_, g_, x_
    arch = {}
    for form, allow in (("top-up", True), ("strict", False)):
        s1, sold1, g1_, x1 = plan(1.0, allow)
        r = {"p_short_over_1k": sm((s1 > 1000).mean())}
        for lab_, sc in (("stocks_zero", 0.0), ("stocks_minus_60pct", 0.4)):
            s0, sold0, g0_, x0 = plan(sc, allow)
            d = s0 - s1
            r[lab_] = {"paths_where_a_cheque_changes_over_1": int((np.abs(d) > 1).sum()),
                       "paths_where_a_cheque_changes_over_1k": int((np.abs(d) > 1000).sum()),
                       "max_change_in_shortfall": round(float(np.abs(d).max())),
                       "paths_where_stocks_make_a_cheque_worse": int((d < -1).sum()),
                       "p_short_over_1k": sm((s0 > 1000).mean()),
                       "gift_p50_change": round(float(np.median(g0_ - g1_))),
                       "gift_p5_change": round(float(np.percentile(g0_ - g1_, 5)))}
        # who pays when the stocks are sold in Jan 2033: would the gift have paid instead, to the dollar?
        sold_m = sold1 > 1
        sN, soldN, gN, _ = plan(1.0, False)
        r["jan2033_sales"] = {"p_sold": sm(sold_m.mean()), "median_sold": md(sold1, sold_m),
                              "of_those_paths_gift_would_have_paid_all": sm(((np.abs(sN - s1) < 1) & sold_m).sum() / max(int(sold_m.sum()), 1)),
                              "median_gift_saved_by_the_sale": md(g1_ - gN, sold_m)}
        arch[form] = r
    sT = plan(1.0, True)[0]; sS = plan(1.0, False)[0]
    arch["top-up_vs_strict_paths_where_a_cheque_differs_over_1"] = int((np.abs(sT - sS) > 1).sum())
    lr["ARCH_A19"] = arch
    res["LR05"] = lr'''


def main():
    add = LR8.ADD
    assert add.count('    res["LR05"] = lr') == 1
    add = add.replace('    res["LR05"] = lr', ARCH)
    assert LR05.BLOCK.count('    res["LR05"] = lr') == 1
    block = LR05.BLOCK.replace('    res["LR05"] = lr', add)
    assert L11.EXTRA.count('    out["L11"] = res') == 1
    L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', block)
    keys = sys.argv[1:] or ["S0", "S1", "S6"]
    for k in keys:
        name = L11.SCEN[k]
        r = L11.run(**L11.L10.SCENARIOS[name])["LR05"]
        res = {"stamp": "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | MODEL",
               "check_MB+T_lock_p_short_over_1k": r["MB+T +lock"]["p_payment_short_over_1k"], "A19": r["ARCH_A19"]}
        f = HERE / f"A19_results_{k}.json"
        f.write_text(json.dumps(res, indent=1))
        print(name, json.dumps(res, indent=1), flush=True)


if __name__ == "__main__":
    main()
