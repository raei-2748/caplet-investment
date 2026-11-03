"""AI-generated (Claude Code), Tue 3 Nov 2026, the Archive (round 7 beat 9). MODEL. (Keel is a simulated team, AI-written.)
A33: does submitted reflection 3 still hold under the round's lock? Reflection 3: "VT is where we allow ourselves to be
wrong – because it's the only investment not standing between Laura and a payment deadline." V54/C06 P5: "the cheques
never depend on it". The Courtroom's C06 (V54 + six lines) prices the reinvestment gap on naming day "as if later bond
payments sat idle" and moves it "from the stocks Laura keeps into Treasuries ... Whatever the stocks can't cover lowers
the whole range". That is the Genius Lab's KW arm (L-17). Deletion test (as A19 did on 28 Oct for LR8): run KW as
modelled, then wipe every share on naming day (1 Jan 2031: the promised half and the kept half both 0), so the lock
comes from the floor's money alone, and compare each future's cheque shortfall. Also a 50% fall on naming day.
Basis: L-17 run.py unchanged (its BLOCK17 + one block appended after the arms), so KW "as modelled" must equal
L-17's results.json (asserted). Funds paid as par bonds, as in L-17 (the Courtroom's exhibit N is the funds-at-NAV view).
Run from repo root: python3 keel/rooms/archive_checks/A33_lock_deletion_test.py [S0 S6 S9]  (~40 s each)"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
L17P = HERE.parent / "lab" / "L-17_interest_that_earns_nothing" / "run.py"
_s = importlib.util.spec_from_file_location("L17", L17P); L17 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L17)

ADD = '''
    # ---- Archive A33: deletion test on KW ----
    gk = {py: v.copy() for py, v in g_kw.items()}
    remA = L33.copy()
    for py in sorted(gk):
        use = np.minimum(remA, gk[py]); gk[py] -= use; remA -= use
    delivA = sum(gk.values()); costA = lock_cost(gk, s31, "par0")
    def shortA(V31v, lockdv):
        xa = np.minimum(costA, 0.5 * V31v)
        ya = np.minimum(np.maximum(costA - xa, 0), lockdv / bill2)
        fa = np.where(costA > 1e-9, np.minimum((xa + ya) / np.maximum(costA, 1e-9), 1.0), 1.0)
        return np.maximum(shortfall - (L33 + fa * delivA), 0) + unfilled, xa, ya
    _, shK, _, _ = arm17(g_kw, "par0")
    sh0, x0, y0 = shortA(V31, lockd)
    assert np.allclose(sh0, shK), "KW replica differs from L-17's arm"
    resA = {"kw_cheques_paid_in_full_check": sm(1 - (sh0 > 0.5).mean())}
    for lab_, f_ in (("wiped on naming day", 0.0), ("halved on naming day", 0.5)):
        sh1, x1, y1 = shortA(V31 * f_, floor_paid + f_ * 0.5 * V31 * bill2)
        worse = sh1 > sh0 + 0.5; better = sh1 < sh0 - 0.5
        resA[lab_] = {"cheques_paid_in_full": sm(1 - (sh1 > 0.5).mean()),
                      "p_any_cheque_worse_off": sm(worse.mean()), "p_any_cheque_better_off": sm(better.mean()),
                      "n_paths_worse": int(worse.sum()),
                      "worse_by_p50_max": [round(float(np.median((sh1 - sh0)[worse]))) if worse.any() else 0,
                                           round(float((sh1 - sh0).max()))],
                      "p_short_over_1k": sm((sh1 > 1000).mean()),
                      "lock_paid_from_floor_p50_p95_when_any": [md(y1, y1 > 1), round(float(np.percentile(y1[y1 > 1], 95))) if (y1 > 1).any() else 0],
                      "p_floor_cannot_buy_lock": sm(((x1 + y1) < costA - 1e-6).mean())}
    resA["as_modelled_lock_from_floor_p"] = sm((y0 > 1).mean())
    resA["as_modelled_n_paths_short"] = int((sh0 > 0.5).sum())
    out17["ARCHIVE_A33"] = resA'''


def main():
    b = L17.BLOCK17
    anchor = '    out16["L17"] = out17'
    assert b.count(anchor) == 1
    L17.BLOCK17 = b.replace(anchor, ADD + '\n' + anchor)
    # run L-17's main logic but keep only our block's output (L-17's own results.json is not rewritten)
    L16, L14 = L17.L16, L17.L14
    bb = L16.BLOCK16
    L16.BLOCK16 = bb.replace('    lr["L16"] = out16', L17.BLOCK17 + '\n    lr["L16"] = out16')
    blk14 = L14.BLOCK14.replace("for k in (0.80, 0.65):", "for k in (0.80, 0.76):") + L16.BLOCK16
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', blk14)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)
    L14.L10.SCENARIOS.setdefault("S9 yields 1pt lower before the build + 2028 deposit halved",
                                 dict(dy_build=-1.0, d28=75_000.0))
    names = {k.split()[0]: k for k in L14.L10.SCENARIOS}
    l17 = json.loads((L17P.parent / "results.json").read_text())
    kwname = "KW WInS-true: coupons reinvested before naming sit in coupon bonds whose coupons earn 0%"
    f = HERE / "A33_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "V54's design + C06's lock (L-17 KW) via L-13 -> L-14 -> L-16 -> W-08 -> L-17, A33 block appended | MODEL")
    for k in sys.argv[1:] or ["S0", "S6", "S9"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]["L17"]
        row = r["ARCHIVE_A33"]
        row["kw_as_modelled"] = r[kwname]["cheques_paid_in_full"]
        if names[k] in l17:
            assert l17[names[k]][kwname]["cheques_paid_in_full"] == r[kwname]["cheques_paid_in_full"], k
            assert l17[names[k]][kwname]["gift_mean"] == r[kwname]["gift_mean"], k
            row["check"] = "KW identical to L-17 results.json"
        out[names[k]] = row
        print(names[k], json.dumps(row), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
