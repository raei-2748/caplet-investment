"""AI-generated (Claude Code), Thu 29 Oct 2026, the Genius Lab (round 2 beat 5). MODEL. (Keel is a simulated team, AI-written.)
L-12 "four doors": V29's framework under every "as needs change" stress, and the one exception anyone would ask for.
(1) V29's design (Long Room LR8 "MB+T +lock": coupon gap banked at the 2031 mark from spare cash and Laura's half,
    promised half locked into short Treasuries on naming day, one 2033 top-up) has only been run on S0, S1 and S6.
    This runs it on all nine of L-10's stresses (deposit halved or missing, yields lower before the build, stocks
    halved before or after naming).
(2) The tempting exception (Library N2/J1, bank #70): after a fall, delay the naming-day lock one year "for a
    recovery". Arm "+lock delayed 1y": the promised half stays in stocks 2031-32, then short Treasuries 2032-33.
    Stress multipliers (h_pre, h_post) are applied to the 2032 value too, so in S8 the fall lands inside the delay.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | basis: LR8 run.py (-> LR-05 -> L-11 -> L-10 -> ips_numbers.py) unchanged; one block appended | MODEL.
Run from repo root: python3 keel/rooms/lab/L-12_four_doors/run.py [S0 S1 ... S8]  (~3 min each)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / "long_room" / "LR8_banked_at_the_mark" / "run.py"
_spec = importlib.util.spec_from_file_location("LR8", P)
LR8 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LR8)
LR05, L11 = LR8.LR05, LR8.L11
L10 = L11.L10

LAB12 = '''
    # ---- Genius Lab L-12: the delayed lock (one year), beside V29's lock on naming day ----
    scale33 = V33 / np.maximum(B0 * np.exp(logr.sum(axis=1)), 1e-9)                # = h_pre * h_post
    V32 = B0 * np.exp(logr[:, :4].sum(axis=1)) * scale33
    bill1 = 1 + np.maximum(curve(.25) + sh(t28 + 4), YMIN) / 100                    # short Treasuries, 2032 -> 2033
    lockd_late = floor_paid + 0.5 * V32 * bill1
    cash, sold, g_late = at_2033(L33 + x * bill2, S33 + C, half_b, True, top, lockd_late)
    lab("MB+T +lock delayed 1y", np.maximum(S33 + extra_ - cash, 0), g_late, sold, lost,
        np.maximum(cash - S33 - extra_, 0), half_b)
    cash, sold, g_now = at_2033(L33 + x * bill2, S33 + C, half_b, True, top, lockd)
    d = g_late - g_now
    down = V31 < B0                                                                 # stocks below their 2028 cost on naming day
    lr["L12_delay"] = {
        "p_stocks_below_2028_cost_on_naming_day": sm(down.mean()),
        "all_paths": {"p_delay_raises_gift_over_1k": sm((d > 1000).mean()), "p_delay_cuts_gift_over_1k": sm((d < -1000).mean()),
                      "gift_change_p5_p50_p95": [round(float(np.percentile(d, q))) for q in (5, 50, 95)],
                      "mean_gift_change": round(float(d.mean())),
                      "mean_extra_kept_by_laura_above_top": round(float(np.maximum(lockd_late - top, 0).mean() - np.maximum(lockd - top, 0).mean()))},
        "paths_down_on_naming_day": {"p_delay_raises_gift_over_1k": sm(((d > 1000) & down).sum() / max(int(down.sum()), 1)),
                                     "p_delay_cuts_gift_over_1k": sm(((d < -1000) & down).sum() / max(int(down.sum()), 1)),
                                     "mean_gift_change": round(float(d[down].mean())) if down.any() else 0}}
    res["LR05"] = lr'''

KEEP = ("MB+T +lock", "MB+T +lock delayed 1y", "L12_delay")


def main():
    add = LR8.ADD
    assert add.count('    res["LR05"] = lr') == 1
    add = add.replace('    res["LR05"] = lr', LAB12)
    assert LR05.BLOCK.count('    res["LR05"] = lr') == 1
    block = LR05.BLOCK.replace('    res["LR05"] = lr', add)
    assert L11.EXTRA.count('    out["L11"] = res') == 1
    L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', block)
    names = {k.split()[0]: k for k in L10.SCENARIOS}
    keys = sys.argv[1:] or list(names)
    for k in keys:
        name = names[k]
        r = L11.run(**L10.SCENARIOS[name])["LR05"]
        res = {"stamp": "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | MODEL",
               "scenario": name, **{k2: r[k2] for k2 in KEEP}}
        (HERE / f"results_{k}.json").write_text(json.dumps(res, indent=1))
        print(name, json.dumps(res, indent=1), flush=True)


if __name__ == "__main__":
    main()
