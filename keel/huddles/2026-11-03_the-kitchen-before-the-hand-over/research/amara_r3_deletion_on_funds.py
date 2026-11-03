"""AI-generated (Claude Code), Tue 3 Nov 2026, the Kitchen (H-027, round 3, Amara's check). MODEL, a TEST for the
Window to gate on Wed 4 Nov, never a promoted result. (Keel is a simulated team, AI-written.)

Question: the Archive's A33 deletion test ("wipe every share on naming day, no cheque worse off") pays the five fund
rungs as par bonds (A33 header: "Funds paid as par bonds, as in L-17"). The Courtroom's exhibit N showed that, with the
funds as funds (net asset value), the lock as sized (KW) misses, and the lock sized as the words read (KWN) does not.
Nobody has run the deletion test on exhibit N's funds. This script does exactly that and nothing else.

How: L-17's chain, unchanged. Into L-17's BLOCK17 go, in order, A33's ADD block (verbatim, imported from the A33
script), then exhibit N's BLOCKN (verbatim, imported from the exhibit N script), then the block below. Neither
script nor any file outside this folder is edited or written.

The block below re-writes one arm function (armND) that takes the stocks' naming-day value and the floor's money as
inputs, so a deletion test can be scored on exhibit N's funds:
  short = max(shortfall + fund leg - (L33 + funded x lock delivery), 0) + unfilled      (exhibit N's scoring)
  lock from the kept half first (0.5 x V31), then the floor's money (A33's rule when the shares are wiped)
Baseline asserts, inside the run (before anything is reported):
  (1) armND, no leg, shares kept      == L-17's KW arm, path by path              (A33's own assert)
  (2) armND, no leg, shares wiped     == A33's "wiped on naming day", path by path
  (3) armND, KW lock, funds at NAV    == exhibit N's KW-N cheques paid in full
  (4) armND, KWN lock, funds at NAV   == exhibit N's KWN cheques paid in full
and outside the run: the same four against L-17 results.json, A33_results.json and exhibit_N_results.json.
Arms reported (each against the SAME lock with the shares kept, as A33 does):
  KW-N  wiped: the lock as the model sized it, funds at NAV, every share gone on 1 Jan 2031
  KWN   wiped: the lock sized as the words read (exhibit N), funds at NAV, every share gone
  KWN   halved: every share halves on naming day
  Two floor conventions when the shares are wiped (the floor IBTM is itself a fund):
    "floor at NAV" (main): the lock may draw on floor_paid minus the floor's own leg (fl_R, exhibit N's)
    "floor at par" (exhibit N's convention): the lock may draw on floor_paid; the floor's leg falls on the gift only
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17, A33 + exhibit N + this block
appended | MODEL.
Run from repo root: python3 -B keel/huddles/2026-11-03_the-kitchen-before-the-hand-over/research/amara_r3_deletion_on_funds.py [S0 S6 S9]"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
A33P = ROOT / "keel" / "rooms" / "archive_checks" / "A33_lock_deletion_test.py"
EXNP = ROOT / "keel" / "rooms" / "courtroom" / "C-06_w5_on_trial" / "exhibit_N_funds_at_nav.py"
L17R = ROOT / "keel" / "rooms" / "lab" / "L-17_interest_that_earns_nothing" / "results.json"


def load(name, p):
    s = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


A33 = load("A33", A33P)      # only its ADD text is used
EXN = load("EXN", EXNP)      # its L-17 chain is the one run; its BLOCKN text is used
L17, L16, L14 = EXN.L17, EXN.L16, EXN.L14

BLOCKA = '''
    # ---- Kitchen H-027 (Amara, r3): A33's deletion test on exhibit N's funds ----
    def armND(gaps, how, leg_real, add, V31v, lockdv):
        gaps = {py: v.copy() for py, v in gaps.items()}
        if add is not None:
            for py, a in add.items():
                gaps[py] = gaps[py] + a
        remL = L33.copy()
        for py in sorted(gaps):
            use = np.minimum(remL, gaps[py]); gaps[py] -= use; remL -= use
        deliver = sum(gaps.values()); cost = lock_cost(gaps, s31, how)
        x_ = np.minimum(cost, 0.5 * V31v)
        y_ = np.minimum(np.maximum(cost - x_, 0), lockdv / bill2)
        funded = np.where(cost > 1e-9, np.minimum((x_ + y_) / np.maximum(cost, 1e-9), 1.0), 1.0)
        cash = L33 + funded * deliver
        short = np.maximum(shortfall + leg_real - cash, 0) + unfilled
        return short, x_, y_, cost
    zeroA = np.zeros(len(s27))
    # baselines first
    shKW0, _, _, _ = armND(g_kw, "par0", zeroA, None, V31, lockd)
    assert np.allclose(shKW0, shK), "baseline 1: KW replica differs from L-17's arm"
    shKWw, _, _, _ = armND(g_kw, "par0", zeroA, None, V31 * 0.0, floor_paid)
    assert np.allclose(shKWw, shortA(V31 * 0.0, floor_paid)[0]), "baseline 2: wiped KW differs from A33"
    shKWN_, _, _, _ = armND(g_kw, "par0", legR, None, V31, lockd)
    assert sm(1 - (shKWN_ > 0.5).mean()) == outN["KW-N funds at NAV, bills as the path has them"]["cheques_paid_in_full"], "baseline 3: KW-N"
    shKWN, _, _, _ = armND(g_kw, "par0", legR, per0, V31, lockd)
    kwn_key = "KWN lock sized as the words read (funds' bonds idle + fee), scored with the real leg"
    assert sm(1 - (shKWN > 0.5).mean()) == outN[kwn_key]["cheques_paid_in_full"], "baseline 4: KWN"
    resH = {"baseline": {"KW_par_bonds_kept": sm(1 - (shKW0 > 0.5).mean()),
                         "KW_par_bonds_wiped_n_worse_vs_kept": int((shKWw > shKW0 + 0.5).sum()),
                         "KW_N_funds_kept": sm(1 - (shKWN_ > 0.5).mean()),
                         "KWN_funds_kept": sm(1 - (shKWN > 0.5).mean()),
                         "asserted": "1-4 in-run (L-17 KW path by path, A33 wiped path by path, exhibit N KW-N and KWN)"}}
    def score(sh1, sh0, x1, y1, cost1):
        worse = sh1 > sh0 + 0.5; better = sh1 < sh0 - 0.5; anys = sh1 > 0.5
        return {"cheques_paid_in_full": sm(1 - anys.mean()),
                "p_any_cheque_worse_off_than_shares_kept": sm(worse.mean()), "n_paths_worse": int(worse.sum()),
                "p_any_cheque_better_off": sm(better.mean()),
                "worse_by_p50_max": [round(float(np.median((sh1 - sh0)[worse]))) if worse.any() else 0,
                                     round(float((sh1 - sh0).max()))],
                "p_short_over_1k": sm((sh1 > 1000).mean()),
                "short_p50_p90_when_short": [md(sh1, anys), round(float(np.percentile(sh1[anys], 90))) if anys.any() else 0],
                "lock_from_floor_p50_p95_when_any": [md(y1, y1 > 1), round(float(np.percentile(y1[y1 > 1], 95))) if (y1 > 1).any() else 0],
                "p_floor_cannot_buy_lock": sm(((x1 + y1) < cost1 - 1e-6).mean())}
    for flab, fmoney in (("floor at NAV (main)", floor_paid - fl_R), ("floor at par (exhibit N's convention)", floor_paid)):
        r_ = {}
        for alab, add_, sh0 in (("KW-N (lock as the model sized it)", None, shKWN_),
                                ("KWN (lock sized as the words read)", per0, shKWN)):
            sh1, x1, y1, c1 = armND(g_kw, "par0", legR, add_, V31 * 0.0, fmoney)
            r_[alab + ", wiped on naming day"] = score(sh1, sh0, x1, y1, c1)
        sh1, x1, y1, c1 = armND(g_kw, "par0", legR, per0, V31 * 0.5, fmoney + 0.5 * 0.5 * V31 * bill2)
        r_["KWN (lock sized as the words read), halved on naming day"] = score(sh1, shKWN, x1, y1, c1)
        resH[flab] = r_
    resH["floor_leg_fl_R_p5_p50_p95"] = pc17(fl_R, (5, 50, 95))
    out17["KITCHEN_H027_AMARA"] = resH'''


def main():
    b17 = L17.BLOCK17
    anchor = '    out16["L17"] = out17'
    assert b17.count(anchor) == 1
    blk17 = b17.replace(anchor, A33.ADD + '\n' + anchor + EXN.BLOCKN + BLOCKA)
    b = L16.BLOCK16
    assert b.count('    lr["L16"] = out16') == 1
    L16.BLOCK16 = b.replace('    lr["L16"] = out16', blk17 + '\n    lr["L16"] = out16')
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
    l17 = json.loads(L17R.read_text())
    a33 = json.loads((A33P.parent / "A33_results.json").read_text())
    exn = json.loads((EXNP.parent / "exhibit_N_results.json").read_text())
    kwname = "KW WInS-true: coupons reinvested before naming sit in coupon bonds whose coupons earn 0%"
    kwn_key = "KWN lock sized as the words read (funds' bonds idle + fee), scored with the real leg"
    kwN_key = "KW-N funds at NAV, bills as the path has them"
    f = HERE / "amara_r3_deletion_on_funds_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V54's design + C06's lock via L-13 -> L-14 -> L-16 -> W-08 -> L-17, "
                    "A33 + exhibit N + Kitchen block appended | MODEL, a test for the Window, not promoted")
    for k in sys.argv[1:] or ["S0"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]["L17"]
        row = r["KITCHEN_H027_AMARA"]; n = names[k]
        chk = []
        if n in l17:                                                       # baseline against the saved files
            assert l17[n][kwname]["cheques_paid_in_full"] == row["baseline"]["KW_par_bonds_kept"], k; chk.append("L-17")
        if n in a33:
            assert a33[n]["wiped on naming day"]["n_paths_worse"] == row["baseline"]["KW_par_bonds_wiped_n_worse_vs_kept"], k
            assert a33[n] == r["ARCHIVE_A33"] | {kk: a33[n][kk] for kk in ("kw_as_modelled", "check") if kk in a33[n]}, k
            chk.append("A33")
        if n in exn:
            assert exn[n][kwN_key]["cheques_paid_in_full"] == row["baseline"]["KW_N_funds_kept"], k
            assert exn[n][kwn_key]["cheques_paid_in_full"] == row["baseline"]["KWN_funds_kept"], k
            assert exn[n][kwn_key] == r["C06N"][kwn_key], k
            chk.append("exhibit N")
        row["baseline"]["matches_saved_files"] = chk
        out[n] = row
        print(n, json.dumps(row), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
