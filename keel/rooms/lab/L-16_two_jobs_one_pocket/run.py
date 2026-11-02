"""AI-generated (Claude Code), Mon 2 Nov 2026, the Genius Lab (round 6 beat 5, Amara builds). MODEL.
(Keel is a simulated team, AI-written.) L-16 "two jobs, one pocket": V52 gives the stocks Laura keeps two jobs.
P6: "The other half stays with Laura, liquid any day, as her flexibility". P8: the reinvestment gap is "set aside
from the stocks Laura keeps; whatever they can't cover lowers the whole range". Requests answered:
  Library (H-015, S-11 break 3): in the bad cases, what share of the kept half does the gap take by Jan 2033, and
      how often is nothing left?
  Laura's Room (Kai, H-011): trace LR-09's S9 cheque gap (median $5,032): a rung never bought, or thin reinvestment
      after 2033? Do Laura's half kept to 2042, or a bigger 2031 set-aside, close it, and at what cost to the gift?
Arms (all on V52's design = L-15's "same day" arm: L-13 slide, lock before naming, bank-at-the-mark, 2033 top-up):
  A0  V52 as MODELLED: the gap at the day's yields PLUS a $7,500 margin (C, LR-05), set aside from the kept half;
      after Jan 2033 the kept stocks are never a source (Archive A19). Reproduces LR-09.
  A1  V52 as WRITTEN: "we price that gap at the day's yields and set it aside" - no margin (C = 0)
  A2  Kai's bigger set-aside: margin $15,000
  B0  P9's order read literally ("the cheques, then the floor, then everything above it"): A0, and any cheque gap
      after 2033 is paid from the kept stocks (valued 2042, one lump: L-11 D0's approximation)
  B1  A1 + the same backstop (no margin; the order line alone carries later gaps)
  G   gap first, then halve (challenger): the gap + margin comes out of ALL the stocks, then the rest is split half
      promised / half kept, so the promised half and the flexible half share it
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: L-14 run.py chain unchanged (k grid 0.80/0.76 as L-15/LR-09); one block
appended after L-14's | MODEL.
Run from repo root: python3 keel/rooms/lab/L-16_two_jobs_one_pocket/run.py [S0 S1 S2 S6 S9]  (sequential)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "L-14_price_of_the_floor" / "run.py"
_s = importlib.util.spec_from_file_location("L14", P); L14 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L14)

BLOCK16 = '''
    # ---- Genius Lab L-16: two jobs, one pocket ----
    pc16 = lambda a, ps: [round(float(np.percentile(a, p_))) for p_ in ps]
    gap31 = (S31 + C - L33) > 1                                       # a gap (incl. margin) visible on naming day
    def arm16(C_, backstop=False, share=False):
        need31_ = np.maximum(S31 + C_ - L33, 0)
        if share:
            x_ = np.minimum(need31_, V31)                                # from all the stocks
            hp_ = 0.5 * (V31 - x_)                                       # promised half, after the set-aside
            half_b_ = hp_ * (V33 / np.maximum(V31, 1e-9))                # the kept half, Jan 2033
            u31_ = ceil5(np.maximum(need31_ - V31, 0))
            lockd_ = floor_paid + hp_ * bill2; top_ = R + hp_
        else:
            x_ = np.minimum(need31_, 0.5 * V31)                          # from the kept half only (V52)
            keep_ = np.where(V31 > 0, 1 - x_ / np.maximum(0.5 * V31, 1e-9), 1.0)
            half_b_ = half * keep_
            u31_ = ceil5(np.maximum(need31_ - 0.5 * V31, 0))
            lockd_ = lockd; top_ = top
        topq = f5(top_ - u31_); botq = bottom - u31_
        c0 = L33 + x_ * bill2
        cash, sold, g = at_2033(c0, S33 + C_, half_b_, True, topq, lockd_)
        fgift = cash - c0 - sold                                         # the gift pays a cheque after naming
        rem = half_b_ - sold                                             # the kept stocks left, Jan 2033
        post = np.maximum(S33 + extra_ - cash, 0)                        # gap still open after Jan 2033
        sh33 = np.maximum(S33 - cash, 0)                                 # part of it visible in 2033, unpaid
        late = np.minimum(post, rem * g_after) if backstop else np.zeros(N)
        short = post - late + unfilled
        exc = np.maximum(lockd_ - fgift - g, 0)
        l42 = rem * g_after - late + np.maximum(cash - S33 - extra_, 0) + exc
        taken = np.clip(1 - rem / np.maximum(half, 1e-9), 0, 1)        # share of the untouched kept half gone
        anys = short > 0.5
        r = {"cheques_paid_in_full": sm(1 - anys.mean()), "p_cheque_short_any": sm(anys.mean()),
             "p_cheque_short_over_1k": sm((short > 1000).mean()),
             "short_p50_p90_when_short": [md(short, anys), round(float(np.percentile(short[anys], 90))) if anys.any() else 0],
             "short_parts_share_of_dollars": {
                 "rung_never_bought_2027_28": sm(unfilled.sum() / max(short.sum(), 1)),
                 "visible_in_2033_unpaid": sm(np.minimum(sh33, post - late).sum() / max(short.sum(), 1)),
                 "after_2033_reinvestment": sm(np.maximum(post - late - sh33, 0).sum() / max(short.sum(), 1))},
             "p_short_from_post2033_only": sm((anys & (unfilled < 0.5) & (sh33 < 0.5)).mean()),
             "kept_half": {
                 "p_gap_takes_any": sm((taken > 0.01).mean()),
                 "share_taken_p50_p90_when_taken": [round(float(np.median(taken[taken > 0.01])), 3) if (taken > 0.01).any() else 0,
                                                    round(float(np.percentile(taken[taken > 0.01], 90)), 3) if (taken > 0.01).any() else 0],
                 "p_half_or_more_taken": sm((taken >= 0.5).mean()),
                 "p_nothing_left": sm((rem < np.maximum(500, 0.02 * half)).mean()),
                 "left_2033_p5_p50": pc16(rem, (5, 50)), "untouched_2033_p50": round(float(np.median(half))),
                 "p_sold_after_2033_for_cheques": sm((late > 1).mean()), "sold_after_p50_when": md(late, late > 1)},
             "p_range_lowered_on_naming_day": sm((u31_ > 0).mean()), "range_cut_p50_when": md(u31_, u31_ > 0),
             "p_gift_pays_cheques_after_naming": sm((fgift > 1).mean()), "gift_paid_p50_when": md(fgift, fgift > 1),
             "p_top_reached": sm((g >= topq - 1).mean()), "p_below_quoted_bottom": sm((g < botq - 1e-6).mean()),
             "top_quoted_p50": round(float(np.median(topq))), "gift_mean": round(float(g.mean())),
             "laura_2042_mean": round(float(l42.mean()))}
        return r, short, taken, rem
    out16 = {"p_gap_visible_on_naming_day_incl_margin": sm(gap31.mean()),
             "S31_p50_p95_p99": pc16(S31, (50, 95, 99)), "extra_after_2033_p50_p95_p99": pc16(extra_, (50, 95, 99)),
             "unfilled_p99_max": pc16(unfilled, (99, 100)), "B0_stock_fund_p50": round(float(np.median(B0))),
             "kept_half_2031_p50": round(float(np.median(0.5 * V31)))}
    arms = {"A0 V52 as modelled (margin 7.5k)": dict(C_=7500), "A1 V52 as written (no margin)": dict(C_=0),
            "A2 bigger set-aside (margin 15k)": dict(C_=15000),
            "B0 A0 + order line as backstop after 2033": dict(C_=7500, backstop=True),
            "B1 A1 + order line as backstop after 2033": dict(C_=0, backstop=True),
            "G gap first, then halve (margin 7.5k)": dict(C_=7500, share=True)}
    keep16 = {}
    for name, kw in arms.items():
        r, short, taken, rem = arm16(**kw)
        out16[name] = r; keep16[name] = (short, taken, rem)
    # checks: A0 must be L-14's XR / LR-09's same-day arm exactly
    assert abs(out16["A0 V52 as modelled (margin 7.5k)"]["gift_mean"] - out14["XR (V39)"]["gift_mean"]) <= 1
    assert abs(out16["A0 V52 as modelled (margin 7.5k)"]["p_top_reached"] - out14["XR (V39)"]["p_top_reached"]) < 1e-9
    # the bad cases inside each world: paths where the gap seen on naming day is in its worst tenth
    bad = S31 >= np.percentile(S31, 90)
    out16["worst_tenth_of_naming_day_gaps"] = {n: {"p_nothing_left": sm((keep16[n][2][bad] < np.maximum(500, 0.02 * half[bad])).mean()),
        "share_taken_p50": round(float(np.median(keep16[n][1][bad])), 3), "p_cheque_short_any": sm((keep16[n][0][bad] > 0.5).mean())}
        for n in arms}
    lr["L16"] = out16'''


def main():
    b = L14.BLOCK14
    assert b.count("for k in (0.80, 0.65):") == 1
    b = b.replace("for k in (0.80, 0.65):", "for k in (0.80, 0.76):") + BLOCK16
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', b)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)
    L14.L10.SCENARIOS.setdefault("S9 yields 1pt lower before the build + 2028 deposit halved",
                                 dict(dy_build=-1.0, d28=75_000.0))     # LR-09's world, same definition
    names = {k.split()[0]: k for k in L14.L10.SCENARIOS}
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | "
                    "rho 0.5 unless S0 | V52's design via L-13 -> L-14 (= L-15 same day) | MODEL")
    for k in sys.argv[1:] or ["S0", "S1", "S2", "S6", "S9"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]["L16"]
        out[names[k]] = r
        print(names[k], json.dumps(r), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
