"""AI-generated (Claude Code), Tue 3 Nov 2026, the Genius Lab (round 7 beat 5; huddle H-023). MODEL.
(Keel is a simulated team, AI-written.) L-17 "interest that earns nothing": the Window's request (H-021, W-08).
V54 P8 prices the ladder's reinvestment gap once, on naming day (1 Jan 2031), "at that day's yields, plus a cushion";
the model behind every cheque figure looks again in January 2033 (W-08: one look 96.01%, two 99.87% of futures pay
every cheque in full). Kai's lock (idea bank #147): on naming day, set aside what the ladder would be short if no
coupon earned anything from that day on, in Treasuries maturing before each January, and never look again.

Arms (W-08's fair arms reused unchanged, beside three locks; all on V54's design via L-13 -> L-14 -> L-16 -> W-08):
  A0f  naming-day set-aside at that day's yields + $7,500 cushion, plus the January 2033 second look (as modelled)
  W0f  the same set-aside, no second look (V54 as written)
  K    Kai's lock, the model's own rungs: each rung's gap if every coupon paid after naming day earns 0% (and the
       bill wait between a bond's maturity and its January earns 0%), coupons paid before naming day keep what they
       earned (the model reinvests each coupon at its day's yield to the rung's maturity); bought on naming day in
       par Treasuries maturing before each January, their own coupons also held at 0% (cost = gap / (1 + y m))
  KK   strictest: as K, but coupons paid before naming day also stop earning on naming day
  Kz   as K, priced as zero-coupon Treasuries (discounted at that day's yields): needs STRIPS, banned on the
       WInS-only basis; shown only to price what the 0% coupon rule costs
  KW   Kai's side knife (round 2): the model reinvests each coupon to maturity as if in a zero (a STRIPS); on WInS a
       coupon reinvested before naming day sits in a coupon bond, whose own coupons after naming day also earn 0%
  K0   Kai's sealed bet: the lock as W-08c sized it (each bond sized to pay $50,000 at maturity, no bill wait),
       applied to the model's real ladder, which counts on bill interest while a bond waits for its January
  For every lock: the 2027 leftover (L33) pays the earliest gaps first; the lock comes from the stocks Laura keeps,
  then from the range's money on naming day (the range lowered by what the kept stocks couldn't cover, as W0f);
  no second look in 2033; scored on the realised gap.
Also: Kai's W-08c deterministic sizing re-done on the model's own rung sizing (C1's roast check), the coupons'
share of the ten cheques (Felix's C4), and top reached per arm (Felix's C3).
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: W-08 chain unchanged (A0f must equal W-08's), one block appended | MODEL.
Run from repo root: python3 keel/rooms/lab/L-17_interest_that_earns_nothing/run.py [S0 S6 S9]  (~40 s each)"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
W08P = HERE.parents[1] / "window" / "W-08_the_second_look.py"
_s = importlib.util.spec_from_file_location("W08", W08P); W08 = importlib.util.module_from_spec(_s); _s.loader.exec_module(W08)
L16, L14 = W08.L16, W08.L14

BLOCK17 = '''
    # ---- Genius Lab L-17: interest that earns nothing (Kai's lock) ----
    pc17 = lambda a, ps: [round(float(np.percentile(a, p_))) for p_ in ps]
    t31_ = yrs(TODAY, dt.date(2031, 1, 1)); tn_ = yrs(T27, dt.date(2031, 1, 1))
    i31_ = min(np.searchsorted(step_t, t31_), len(step_t) - 1)
    def zgaps(shm, s27v, strictest=False, wins=False, no_wait=False):
        """Per rung: the gap at its January if nothing earns interest after naming day (nominal), and its face."""
        gaps, faces = {}, {}
        for (py, (name, mat, cpn)) in RUNGS.items():
            T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27v, YMIN)
            cc = (y0p if cpn is None else np.full(len(s27v), cpn)) / 100
            k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
            idx = np.clip(np.searchsorted(step_t, k + TOFF), 0, len(step_t) - 1)
            yk = np.maximum(y0p[:, None] + shm[:, idx] - s27v[:, None], YMIN) / 100
            expo = (T - k) if not strictest else np.maximum(tn_ - k, 0)
            grow = (1 + yk / 2) ** (2 * expo[None, :])
            if wins:                                                     # KW: a coupon reinvested before naming sits in a
                pre_ = (1 + yk / 2) ** (2 * np.maximum(tn_ - k, 0)[None, :])   # coupon bond: compounds to naming day, then
                grow = pre_ * (1 + yk * np.maximum(T - np.maximum(k, tn_), 0)[None, :])  # its own coupons sit at 0%
            gz = np.where((k > tn_ + 1e-9)[None, :], 1.0, grow)          # paid after naming day: earns 0%
            dbase = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - k)[None, :])).sum(axis=1)
            gapf_base = (1 + np.maximum(curve(.25) + s27v, YMIN) / 100) ** yrs(mat, dt.date(py, 1, 1))
            face = PAY / (dbase * gapf_base)                             # the model's own sizing (ips_numbers.py s3)
            if no_wait:                                                  # K0: Kai's W-08c sizing (face = PAY / db), applied
                gaps[py] = np.maximum(PAY - PAY / dbase * (1 + (cc / 2) * gz.sum(axis=1)), 0)   # to the model's real ladder
                faces[py] = face; continue
            gaps[py] = np.maximum(PAY - face * (1 + (cc / 2) * gz.sum(axis=1)), 0)
            faces[py] = face
        return gaps, faces
    def lock_cost(gaps, s31v, how):
        c = np.zeros(len(s31v))
        for py, gp in gaps.items():
            m = yrs(dt.date(2031, 1, 1), dt.date(py, 1, 1)); y = np.maximum(curve(m) + s31v, YMIN) / 100
            c += gp / (1 + y * m) if how == "par0" else gp * (1 + y / 2) ** (-2 * m)
        return c
    s31 = shifts[:, i31_]
    out17 = {}
    # deterministic replica of Kai's W-08c (no rate moves): his sizing (face = PAY / db) v the model's (with the bill wait)
    z1 = np.zeros((1, shifts.shape[1])); s0 = np.zeros(1)
    g_det, f_det = zgaps(z1, s0)
    out17["deterministic_22oct_no_moves"] = {
        "lock_gap_nominal_model_sizing": round(float(sum(v[0] for v in g_det.values()))),
        "lock_cost_par0_model_sizing": round(float(lock_cost(g_det, s0, "par0")[0])),
        "lock_cost_zero_model_sizing": round(float(lock_cost(g_det, s0, "zero")[0])),
        "per_rung_gap": {str(py): round(float(v[0])) for py, v in g_det.items()},
        "kai_W08c_par0_for_comparison": 11201,
        "faces_sum": round(float(sum(v[0] for v in f_det.values()))),
        "coupons_and_interest_share_of_500k": round(1 - float(sum(v[0] for v in f_det.values())) / (10 * PAY), 4)}
    S31z = proj_at(2031)                                                  # A0's naming-day gap at that day's yields
    out17["A0_set_aside_S31_plus_7500_minus_L33_p50_p95_p99"] = pc17(np.maximum(S31z + 7500 - L33, 0), (50, 95, 99))
    def arm17(gaps, how):
        gaps = {py: v.copy() for py, v in gaps.items()}
        remL = L33.copy()
        for py in sorted(gaps):                                          # the 2027 leftover pays the earliest gaps
            use = np.minimum(remL, gaps[py]); gaps[py] -= use; remL -= use
        deliver = sum(gaps.values())                                     # nominal, at each January
        cost = lock_cost(gaps, s31, how)
        x_ = np.minimum(cost, 0.5 * V31)                                 # from the stocks Laura keeps first (P8)
        y_ = np.minimum(np.maximum(cost - x_, 0), lockd / bill2)         # then the range's money, on naming day
        funded = np.where(cost > 1e-9, np.minimum((x_ + y_) / np.maximum(cost, 1e-9), 1.0), 1.0)
        keep_ = np.where(V31 > 0, 1 - x_ / np.maximum(0.5 * V31, 1e-9), 1.0)
        rem = half * keep_                                               # the kept half, Jan 2033 (no 2033 sale)
        u31_ = ceil5(np.maximum(cost - 0.5 * V31, 0))
        lockd_ = lockd - y_ * bill2
        topq = f5(top - u31_); botq = bottom - u31_
        cash = L33 + funded * deliver                                    # no second look in January 2033
        g = np.minimum(topq, lockd_)
        short = np.maximum(shortfall - cash, 0) + unfilled
        exc = np.maximum(lockd_ - g, 0)
        l42 = rem * g_after + np.maximum(cash - S33 - extra_, 0) + exc  # W-08's formula, like for like
        l42r = rem * g_after + np.maximum(cash - shortfall, 0) + exc     # release on the realised gap
        taken = np.clip(1 - rem / np.maximum(half, 1e-9), 0, 1)
        anys = short > 0.5
        r = {"cheques_paid_in_full": sm(1 - anys.mean()), "p_cheque_short_over_1k": sm((short > 1000).mean()),
             "short_p50_p90_when_short": [md(short, anys), round(float(np.percentile(short[anys], 90))) if anys.any() else 0],
             "p_short_from_rung_never_bought_only": sm((anys & (np.maximum(shortfall - cash, 0) < 0.5)).mean()),
             "p_short_with_lock_fully_funded": sm((anys & (funded > 1 - 1e-9) & (unfilled < 0.5)).mean()),
             "lock_cost_p50_p95_p99": pc17(cost, (50, 95, 99)), "lock_cost_mean": round(float(cost.mean())),
             "lock_delivers_nominal_p50": round(float(np.median(deliver))),
             "lock_unused_released_p50_mean": [round(float(np.median(np.maximum(cash - shortfall, 0)))),
                                               round(float(np.maximum(cash - shortfall, 0).mean()))],
             "p_lock_not_fully_funded": sm((funded < 1 - 1e-9).mean()),
             "kept_half": {"p_lock_takes_any": sm((taken > 0.01).mean()),
                           "share_taken_p50_p90_when_taken": [round(float(np.median(taken[taken > 0.01])), 3) if (taken > 0.01).any() else 0,
                                                              round(float(np.percentile(taken[taken > 0.01], 90)), 3) if (taken > 0.01).any() else 0],
                           "p_half_or_more_taken": sm((taken >= 0.5).mean()),
                           "p_nothing_left": sm((rem < np.maximum(500, 0.02 * half)).mean()),
                           "left_2033_p5_p50": pc17(rem, (5, 50))},
             "p_range_lowered_on_naming_day": sm((u31_ > 0).mean()), "range_cut_p50_when": md(u31_, u31_ > 0),
             "p_gift_pays_cheques_after_naming": 0.0,
             "p_top_reached": sm((g >= topq - 1).mean()), "p_below_quoted_bottom": sm((g < botq - 1e-6).mean()),
             "top_quoted_p50": round(float(np.median(topq))), "gift_mean": round(float(g.mean())),
             "laura_2042_mean": round(float(l42.mean())), "laura_2042_mean_realised_release": round(float(l42r.mean()))}
        return r, short, taken, rem
    g_mc, _ = zgaps(shifts, s27)
    g_kk, _ = zgaps(shifts, s27, strictest=True)
    g_kw, _ = zgaps(shifts, s27, wins=True)
    g_k0, _ = zgaps(shifts, s27, no_wait=True)
    bad = S31 >= np.percentile(S31, 90)
    for name, (gg, how) in {"K Kai's lock (model rungs, par bonds, their coupons at 0%)": (g_mc, "par0"),
                            "KK strictest (coupons paid before naming day stop earning too)": (g_kk, "par0"),
                            "Kz K priced as zero-coupon bonds (STRIPS: banned on WInS)": (g_mc, "zero"),
                            "KW WInS-true: coupons reinvested before naming sit in coupon bonds whose coupons earn 0%": (g_kw, "par0"),
                            "K0 Kai as W-08c sized it (no bill wait), on the real ladder": (g_k0, "par0")}.items():
        r, short, taken, rem = arm17(gg, how)
        r["worst_tenth_of_naming_day_gaps"] = {"p_nothing_left": sm((rem[bad] < np.maximum(500, 0.02 * half[bad])).mean()),
            "share_taken_p50": round(float(np.median(taken[bad])), 3), "p_cheque_short_any": sm((short[bad] > 0.5).mean())}
        out17[name] = r
    out16["L17"] = out17'''


def main():
    b = L16.BLOCK16
    assert b.count('    lr["L16"] = out16') == 1
    L16.BLOCK16 = b.replace('    lr["L16"] = out16', BLOCK17 + '\n    lr["L16"] = out16')
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
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V54's design via L-13 -> L-14 -> L-16 -> W-08, L-17 block appended | MODEL")
    keepW = ["A0f A0, cut paid on naming day, realised gap", "W0f W0, cut paid on naming day, realised gap"]
    w08 = json.loads((W08P.parent / "W-08_results.json").read_text())
    for k in sys.argv[1:] or ["S0", "S6"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]
        row = {n: r[n] for n in keepW}
        row.update(r["L17"])
        if names[k] in w08:                                              # A0f/W0f must equal the Window's run
            for n in keepW:
                assert w08[names[k]][n]["cheques_paid_in_full"] == r[n]["cheques_paid_in_full"], (k, n)
                assert w08[names[k]][n]["gift_mean"] == r[n]["gift_mean"], (k, n)
            row["check"] = "A0f and W0f identical to W-08_results.json"
        out[names[k]] = row
        print(names[k], json.dumps(row), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
