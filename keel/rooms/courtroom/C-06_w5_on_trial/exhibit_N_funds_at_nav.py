"""AI-generated (Claude Code), Tue 3 Nov 2026, the Courtroom (round 7 beat 8; huddle H-026, C-06). MODEL.
(Keel is a simulated team, AI-written.) Exhibit N: the five fund rungs as funds, not par bonds.

The Lab's L-17 found that Kai's lock (KW: on naming day, 1 Jan 2031, set aside what the ladder would be short if every
bond payment from then on sat idle) pays every cheque in 200,000 of 200,000 model futures once bought. Jun (L-17 s5,
"what would worry an actuary"): that is true by construction, and one leg is known to be unzeroed: the model pays the
five fund rungs (IBTM-IBTR, the 2033-37 cheques) as par bonds maturing on 15 December. The iBond funds instead hold
Treasuries that mature through their final year; the cash waits for the December close ("During the final year of
the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the
liquidation of the fund"; "the Funds do not seek to return any predetermined amount": iShares, R04 row 8), and they
charge 0.07% a year (archived product pages, `archive/rab/data/ishares/`). This exhibit adds that leg and re-scores KW.

The leg, per fund rung and path (simple interest within the final year; fee on the rung's face for its life):
  leg = face * sum_j (1/12) * (c - b_j) * w_j  +  face * 0.0007 * T
  face, c   the model's own rung (face from L-17 zgaps, coupon c = its yield when bought in January 2027)
  j         twelve maturity dates spread evenly through the rung's final year (month-ends Jan-Nov, then 15 Dec);
            ASSUMPTION: the index rule allows any date from 1 Jan to 15 Dec; real weights were not read
  w_j       years from that maturity to the fund's 15 December close
  b_j       the path's 3-month bill rate on that date (REAL arm), or 0 (BOUND arm: what the lock's own rule assumes)
The floor (IBTM again, bought 2 Jan 2028 to repay R) gets the same leg with its 2028 yield, against the gift side.

Arms (all on L-17's KW lock and scoring, V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17):
  KW        as the Lab ran it (asserted equal to L-17's results.json)
  KW-N      funds at net asset value, bills as each path has them (the model's rates, floored at 0.25%)
  KW-N0     funds at net asset value with bills at 0% after maturity: a bound beyond the model's own rate floor
  KWN-w     as KWN without the fee: only what the words' "sat idle" covers, scored with the real leg (fee included)
  KWN       the lock sized as W5's words read: the bonds inside the funds count as "later bond payments" that sit
            idle (leg at 0% bills, plus the fee, added to each fund rung's gap), then scored with KW-N's real leg
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | L-17 chain unchanged, one block appended | MODEL.
Run from repo root: python3 keel/rooms/courtroom/C-06_w5_on_trial/exhibit_N_funds_at_nav.py [S0 S6 S9]"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
L17P = HERE.parents[1] / "lab" / "L-17_interest_that_earns_nothing" / "run.py"
_s = importlib.util.spec_from_file_location("L17", L17P); L17 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L17)
W08, L16, L14 = L17.W08, L17.L16, L17.L14

BLOCKN = '''
    # ---- Courtroom C-06, exhibit N: the five fund rungs as funds (net asset value), not par bonds ----
    FEE_N = 0.0007
    def billr_n(d_):
        i_ = min(int(np.searchsorted(step_t, yrs(TODAY, d_))), len(step_t) - 1)
        return np.maximum(curve(.25) + shifts[:, i_], YMIN) / 100
    def mds_n(mat):
        Y = mat.year
        return [dt.date(Y, m + 1, 1) - dt.timedelta(days=1) for m in range(1, 12)] + [mat]
    _, faces_n = zgaps(shifts, s27, wins=True)
    def fund_leg(zero_bills, fee=True):
        leg = np.zeros(len(s27)); per = {}
        for py, (name, mat, cpn) in RUNGS.items():
            if cpn is not None:
                continue
            T = yrs(T27, mat); cc = np.maximum(curve(T + TOFF) + s27, YMIN) / 100
            acc = np.zeros(len(s27))
            for d_ in mds_n(mat):
                w = yrs(d_, mat); b = 0.0 if zero_bills else billr_n(d_)
                acc += (cc - b) * w / 12
            lg = faces_n[py] * acc + (faces_n[py] * FEE_N * T if fee else 0.0)
            per[py] = lg; leg = leg + lg
        return leg, per
    legR, perR = fund_leg(False)
    leg0, per0 = fund_leg(True)
    try:                                                                 # the floor: IBTM bought 2 Jan 2028 to repay R
        mat_f = dt.date(2032, 12, 15); cf = y5_28 / 100; accR = np.zeros(len(s27)); acc0 = np.zeros(len(s27))
        for d_ in mds_n(mat_f):
            w = yrs(d_, mat_f); accR += (cf - billr_n(d_)) * w / 12; acc0 += cf * w / 12
        fl_R = R * accR + R * FEE_N * t_ibtm; fl_0 = R * acc0 + R * FEE_N * t_ibtm; floor_ok = True
    except NameError:
        fl_R = np.zeros(len(s27)); fl_0 = np.zeros(len(s27)); floor_ok = False
    def armN(gaps, how, leg_real, add=None, floor_leg=None):
        gaps = {py: v.copy() for py, v in gaps.items()}
        if add is not None:
            for py, a in add.items():
                gaps[py] = gaps[py] + a
        remL = L33.copy()
        for py in sorted(gaps):
            use = np.minimum(remL, gaps[py]); gaps[py] -= use; remL -= use
        deliver = sum(gaps.values())
        cost = lock_cost(gaps, s31, how)
        x_ = np.minimum(cost, 0.5 * V31)
        y_ = np.minimum(np.maximum(cost - x_, 0), lockd / bill2)
        funded = np.where(cost > 1e-9, np.minimum((x_ + y_) / np.maximum(cost, 1e-9), 1.0), 1.0)
        keep_ = np.where(V31 > 0, 1 - x_ / np.maximum(0.5 * V31, 1e-9), 1.0)
        rem = half * keep_
        u31_ = ceil5(np.maximum(cost - 0.5 * V31, 0))
        lockd_ = lockd - y_ * bill2 - (0.0 if floor_leg is None else floor_leg)
        topq = f5(top - u31_); botq = bottom - u31_
        cash = L33 + funded * deliver
        g = np.minimum(topq, lockd_)
        short = np.maximum(shortfall + leg_real - cash, 0) + unfilled
        exc = np.maximum(lockd_ - g, 0)
        l42r = rem * g_after + np.maximum(cash - shortfall - leg_real, 0) + exc
        anys = short > 0.5; full = (funded > 1 - 1e-9) & (unfilled < 0.5)
        return {"cheques_paid_in_full": sm(1 - anys.mean()), "p_cheque_short_over_1k": sm((short > 1000).mean()),
                "short_p50_p90_when_short": [md(short, anys), round(float(np.percentile(short[anys], 90))) if anys.any() else 0],
                "p_short_with_lock_fully_funded": sm((anys & full).mean()),
                "lock_cost_p50_p95": pc17(cost, (50, 95)), "lock_cost_mean": round(float(cost.mean())),
                "p_kept_stocks_all_gone": sm((rem < np.maximum(500, 0.02 * half)).mean()),
                "p_range_lowered_on_naming_day": sm((u31_ > 0).mean()),
                "p_below_quoted_bottom": sm((g < botq - 1e-6).mean()), "p_top_reached": sm((g >= topq - 1).mean()),
                "gift_mean": round(float(g.mean())), "laura_2042_mean_realised_release": round(float(l42r.mean())),
                "unused_lock_back_to_laura_p50": round(float(np.median(np.maximum(cash - shortfall - leg_real, 0))))}, cost
    outN = {"floor_leg_in_scope": floor_ok,
            "fund_leg_real_p5_p50_p95": pc17(legR, (5, 50, 95)), "fund_leg_zero_bills_p50_p95_max": pc17(leg0, (50, 95, 100)),
            "fund_leg_real_per_rung_p50": {str(k): round(float(np.median(v))) for k, v in perR.items()},
            "fund_leg_zero_bills_per_rung_p50": {str(k): round(float(np.median(v))) for k, v in per0.items()},
            "fee_part_p50": round(float(np.median(sum(faces_n[py] * FEE_N * yrs(T27, RUNGS[py][1]) for py in perR)))),
            "floor_leg_real_p5_p50_p95": pc17(fl_R, (5, 50, 95)), "floor_leg_zero_bills_p50": round(float(np.median(fl_0))),
            "floor_margin_R_minus_bottom_p50_min": [round(float(np.median(R - bottom))), round(float(np.min(R - bottom)))] if floor_ok else None}
    zero = np.zeros(len(s27))
    rKW, cKW = armN(g_kw, "par0", zero)
    outN["KW as the Lab ran it (check)"] = rKW
    outN["KW-N funds at NAV, bills as the path has them"] = armN(g_kw, "par0", legR, floor_leg=fl_R)[0]
    outN["KW-N0 funds at NAV, bills at 0% (bound)"] = armN(g_kw, "par0", leg0, floor_leg=fl_0)[0]
    rKWN, cKWN = armN(g_kw, "par0", legR, add=per0, floor_leg=fl_R)
    outN["KWN lock sized as the words read (funds' bonds idle + fee), scored with the real leg"] = rKWN
    outN["KWN under the 0% bound"] = armN(g_kw, "par0", leg0, add=per0, floor_leg=fl_0)[0]
    per0w = fund_leg(True, fee=False)[1]
    outN["KWN-w words only (funds' bonds idle, fee not priced), scored with the real leg"] = armN(g_kw, "par0", legR, add=per0w, floor_leg=fl_R)[0]
    outN["KWN_extra_lock_cost_p50_p95"] = pc17(cKWN - cKW, (50, 95))
    out17["C06N"] = outN'''


def main():
    b17 = L17.BLOCK17
    assert b17.count('    out16["L17"] = out17') == 1
    blk17 = b17.replace('    out16["L17"] = out17', '    out16["L17"] = out17' + BLOCKN)
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
    f = HERE / "exhibit_N_results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17, exhibit N appended | MODEL")
    lab = json.loads((L17P.parent / "results.json").read_text())
    kwname = "KW WInS-true: coupons reinvested before naming sit in coupon bonds whose coupons earn 0%"
    for k in sys.argv[1:] or ["S0", "S6", "S9"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]["L17"]
        row = r["C06N"]
        chk = row["KW as the Lab ran it (check)"]
        if names[k] in lab:                                              # KW must equal the Lab's run
            assert lab[names[k]][kwname]["cheques_paid_in_full"] == chk["cheques_paid_in_full"], k
            assert lab[names[k]][kwname]["gift_mean"] == chk["gift_mean"], k
            row["check"] = "KW (no leg) identical to L-17 results.json on cheques paid in full and gift mean"
        out[names[k]] = row
        print(names[k], json.dumps(row), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
