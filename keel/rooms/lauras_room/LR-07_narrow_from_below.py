"""AI-generated (Claude Code), Fri 30 Oct 2026, Laura's Room (round 3 beat 6, Amara). MODEL.
(Keel is a simulated team, AI-written.) LR-07 "narrow from below": once the range slides (L-13 A), how far can the
cheques still reach into the gift after naming day, and so how high can the quoted bottom sit and never be broken?
  slide   L-13's A unchanged: top = f5(top - u31), the gift from L-13's own at_2033 call (the bottom never enters it)
  tail    the gift's shortfall against the slid top: p99 / p99.9 / p99.99 / max, and the share over $1k / $5k / $10k
  narrow  bottom' = max(V29's bottom, slid top - w) for w = $5k / $10k / $15k: how often the gift lands below bottom',
          by how much, and how much bottom' raises the quoted bottom (the co-sponsors' bookable number, LR-04)
  The 28 Oct kill ("raising the quoted bottom with the lock: below it in 3-5% of paths", THINKING_LOG) predates the 2031
  mark and the slide; this re-asks it on the design the Long Room votes on tonight.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: L-13 run.py chain unchanged, one block appended | MODEL.
Run from repo root: python3 keel/rooms/lauras_room/LR-07_narrow_from_below.py [S0 S1 S2 S6]  (~3 min each)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "lab" / "L-13_slide_the_range" / "run.py"
_spec = importlib.util.spec_from_file_location("L13", P)
L13 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(L13)
LR8, LR05, L11, L10 = L13.LR8, L13.LR05, L13.L11, L13.L10

BLOCK07 = '''
    # ---- Laura's Room LR-07: narrow from below ----
    Ts = f5(top - u31)
    _c, _s, g_s = at_2033(cash0, need33, half_b, True, Ts, lockd)
    sh_ = np.maximum(Ts - g_s, 0)
    o7 = {"slide_top_p50": round(float(np.median(Ts))), "v29_bottom_p50": round(float(np.median(q_mc))),
          "slide_shortfall_vs_top_p99_p999_p9999_max": [round(float(np.percentile(sh_, p_))) for p_ in (99, 99.9, 99.99)] + [round(float(sh_.max()))],
          "p_shortfall_over_1k_5k_10k": [sm((sh_ > v).mean()) for v in (1000, 5000, 10000)],
          "p_v29_bottom_broken": sm((g_s < q_mc - 1e-6).mean()),
          "n_v29_bottom_broken_slide_vs_base": [int((g_s < q_mc - 1e-6).sum()),
                                                int((np.minimum(T5, lockd - fg) < q_mc - 1e-6).sum())],
          "n_slid_top_quoted_below_bottom": int((Ts < q_mc - 1e-6).sum())}
    # guard: a top is never quoted below its own bottom
    Tg = np.maximum(Ts, q_mc)
    _c, _s, g_g = at_2033(cash0, need33, half_b, True, Tg, lockd)
    o7["guard top>=bottom"] = {"n_v29_bottom_broken": int((g_g < q_mc - 1e-6).sum()),
        "n_below_top_less_10k": int((g_g < np.maximum(q_mc, Tg - 10000) - 1e-6).sum()),
        "p_top_reached": sm((g_g >= Tg - 1).mean())}
    for w in (5000, 10000, 15000):
        bq = np.maximum(q_mc, Ts - w)
        brk = g_s < bq - 1e-6
        o7[f"narrow w={w}"] = {"bottom_p5_p50_p95": [round(float(np.percentile(bq, p_))) for p_ in (5, 50, 95)],
            "bottom_raise_p50": round(float(np.median(bq - q_mc))), "p_bottom_raised": sm((bq > q_mc + 1).mean()),
            "p_below_bottom": sm(brk.mean()), "n_below_bottom": int(brk.sum()),
            "median_below_when_below": md(bq - g_s, brk), "max_below": round(float((bq - g_s)[brk].max())) if brk.any() else 0}
    out13["LR07"] = o7
    lr["L13"] = out13'''


def main():
    blk = L13.BLOCK13
    assert blk.count('    lr["L13"] = out13') == 1
    blk = blk.replace('    lr["L13"] = out13', BLOCK07)
    add = LR8.ADD
    assert add.count('    res["LR05"] = lr') == 1
    add = add.replace('    res["LR05"] = lr', blk)
    assert LR05.BLOCK.count('    res["LR05"] = lr') == 1
    block = LR05.BLOCK.replace('    res["LR05"] = lr', add)
    assert L11.EXTRA.count('    out["L11"] = res') == 1
    L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', block)
    names = {k.split()[0]: k for k in L10.SCENARIOS}
    f = HERE / "LR-07_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 unless S0 | MODEL"
    for k in sys.argv[1:] or ["S0", "S1", "S2", "S6"]:
        name = names[k]
        r = L11.run(**L10.SCENARIOS[name])["LR05"]["L13"]
        out[name] = {"check_vs_L13_slide": r["A slide (top cut like the bottom)"], "LR07": r["LR07"]}
        print(name, json.dumps(out[name], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
