"""AI-generated (Claude Code), Sun 1 Nov 2026, the Genius Lab (round 5 beat 5, Nora builds; huddle H-010). MODEL.
(Keel is a simulated team, AI-written.) L-15 "hold it, then say it": three challengers on V47's own design.
  A   ORDER and LOCK TIMING (the Library's request, H-009): V47 says "On the day she names it, the half she promised
      moves into Treasuries". The model names and moves on the same day (1 Jan 2031). Arms:
        same day (V47; check = L-14 "XR (V39)")
        name first, move later: a week / a month / a quarter late; a month late with a fat-tailed month (t, 3 df)
        "wait while it rises": move at the end of the first week stocks fall, at most a quarter late
        skipped where stocks rose most in the year before naming (2030 in its top fifth / top tenth): the half stays
        in stocks to 2033; a quarter late only after a top-fifth 2030; skipped everywhere (reference)
        move first, name later (a month / a quarter / six months): the top is read off Treasuries already held
      Inside 2031 stocks move as a Brownian bridge on the model's own 2031 draw (yearly paths untouched; extra draws
      from a separate generator, seed 20261101). Bills earn the model's 2031 and 2032 short rates.
  B   THE PRICE'S ADDRESS: Archive A26's matched rival (A09 at k = 0.76, same $145k median bottom): where its mean lead
      in gift + Laura's 2042 money sits, by fifths of 2028-32 stocks, of 2028-30 stocks, and of XR's own wealth.
  C   THE MISS, SIZED: when V47's gift misses its top, by how much (median, p90, max, share under $5k).
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: L-14 run.py chain (L-13 slide, lock) unchanged, k grid (0.80, 0.76) as Archive
A26; one block appended | MODEL.
Run from repo root: python3 keel/rooms/lab/L-15_hold_it_then_say_it/run.py [S0 S1 S6]  (sequential: L-10's runner
shares one temp file)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "L-14_price_of_the_floor" / "run.py"
_s = importlib.util.spec_from_file_location("L14", P); L14 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L14)

BLOCK15 = '''
    # ---- Genius Lab L-15: hold it, then say it ----
    rg = np.random.default_rng(20261101)
    L1 = logr[:, 3]                                              # the model's own 2031 stock draw (log)
    r31 = np.maximum(curve(.25) + sh(t28 + 3), YMIN) / 100
    r32 = np.maximum(curve(.25) + sh(t28 + 4), YMIN) / 100
    assert np.allclose(bill2, (1 + r31) * (1 + r32))
    hp = 0.5 * V31                                               # the promised half on naming day
    def lock_at(Xt, t):                                          # promised half moved t years after 1 Jan 2031
        return floor_paid + hp * np.exp(Xt) * (1 + r31) ** (1 - t) * (1 + r32)
    def bridge(t, fat=False):
        e = rg.standard_t(3, N) / np.sqrt(3.0) if fat else rg.normal(size=N)
        return t * L1 + EQ_VOL * np.sqrt(t * (1 - t)) * e
    base = None
    def arm15(ld):
        cash, sold, g = at_2033(cash0, need33, half_b, True, topX, ld)
        exc = np.maximum(ld - (cash - cash0 - sold) - g, 0)
        l42 = (half_b - sold) * g_after + np.maximum(cash - S33 - extra_, 0) + exc
        miss = g < topX - 1; short = topX - g
        r = {"p_top_reached": sm(1 - miss.mean()),
             "p_below_quoted_bottom": sm((g < q_mc - 1e-6).mean()),
             "p_cheque_short_over_1k": sm((tot_short(cash) > 1000).mean()),
             "miss_p50_p90_when_missed": [md(short, miss), round(float(np.percentile(short[miss], 90))) if miss.any() else 0],
             "p_miss_over_5k": sm((short > 5000).mean()),
             "gift_mean": round(float(g.mean())), "laura_2042_mean": round(float(l42.mean()))}
        if base is not None:
            r["gift_mean_change_vs_same_day"] = round(float(g.mean() - base[0].mean()))
            r["laura_2042_mean_change_vs_same_day"] = round(float(l42.mean() - base[1].mean()))
            r["p_laura_gains_over_1k"] = sm(((l42 - base[1]) > 1000).mean())
        return r, g, l42
    out15 = {"A_order_and_lock_timing": {}}
    A = out15["A_order_and_lock_timing"]
    r0, g0, l0 = arm15(lockd)
    A["same day (V47)"] = r0
    base = (g0, l0)
    assert abs(r0["p_top_reached"] - sm((gX >= topX - 1).mean())) < 1e-9
    for tag, t in (("a week", 1 / 52), ("a month", 1 / 12), ("a quarter", 0.25), ("six months", 0.5), ("a year", 1.0)):
        A[f"name first, move {tag} late"] = arm15(lock_at(bridge(t), t))[0]
    # Jun's second control: a year late is L-12's "delayed 1y" arm exactly (the bridge ends on the year's own draw)
    V32c = B0 * np.exp(logr[:, :4].sum(axis=1)) * (V33 / np.maximum(B0 * np.exp(logr.sum(axis=1)), 1e-9))
    assert np.allclose(lock_at(L1, 1.0), floor_paid + 0.5 * V32c * (1 + r32))
    A["name first, move a month late, fat-tailed month (t 3df)"] = arm15(lock_at(bridge(1 / 12, fat=True), 1 / 12))[0]
    # wait while it rises: weekly bridge, move at the end of the first week stocks fall, at most 13 weeks
    X = np.zeros(N); Xl = np.zeros(N); tl = np.zeros(N); done = np.zeros(N, bool); s = 0.0
    for k in range(1, 14):
        t = k / 52
        Xn = X + (t - s) / (1 - s) * (L1 - X) + EQ_VOL * np.sqrt((t - s) * (1 - t) / (1 - s)) * rg.normal(size=N)
        stop = (~done) & ((Xn < X) | (k == 13))
        Xl[stop] = Xn[stop]; tl[stop] = t; done |= stop; X = Xn; s = t
    rw, gw, lw = arm15(floor_paid + hp * np.exp(Xl) * (1 + r31) ** (1 - tl) * (1 + r32))
    rw["weeks_waited_p50_mean"] = [round(float(np.median(tl * 52)), 1), round(float((tl * 52).mean()), 2)]
    rw["p_moved_higher_than_naming_day"] = sm((Xl > 0).mean())
    A["wait while it rises (move after the first down week, at most a quarter)"] = rw
    y30 = logr[:, 2]
    for tag, q in (("top fifth", 80), ("top tenth", 90)):
        m = y30 >= np.percentile(y30, q)
        rs, gs_, ls_ = arm15(np.where(m, floor_paid + 0.5 * V33, lockd))
        rs["p_top_reached_in_skipped_paths"] = sm((gs_[m] >= topX[m] - 1).mean())
        rs["p_top_reached_in_skipped_paths_if_moved"] = sm((g0[m] >= topX[m] - 1).mean())
        rs["mean_2030_stock_return_pct_in_skipped"] = round(float((np.exp(y30[m]).mean() - 1) * 100), 1)
        A[f"skipped after a {tag} 2030"] = rs
    m5 = y30 >= np.percentile(y30, 80)
    A["a quarter late only after a top-fifth 2030"] = arm15(np.where(m5, lock_at(bridge(0.25), 0.25), lockd))[0]
    A["skipped everywhere (no lock)"] = arm15(floor_paid + 0.5 * V33)[0]
    # move first, name later: the named top is read off what is already in Treasuries, so it cannot move
    for tag in ("a month", "a quarter", "six months"):
        topN = f5(top - u31)                                      # same mark, same half: nothing between the move and the words
        cash, sold, g = at_2033(cash0, need33, half_b, True, topN, lockd)
        A[f"move first, name {tag} later"] = {"p_top_reached": sm((g >= topN - 1).mean()),
            "identical_to_same_day": bool(np.array_equal(g, g0) and np.array_equal(topN, topX))}
    # B: the price's address (A09 at k = 0.76, Archive A26's match)
    bA, gA_, lA_ = gA[0.76]
    D = (gA_ + lA_) - (gX + l42X)
    tot5 = logr.sum(axis=1)
    # Jun (H-010 r1), set before the run: the primary sort is 2028-30 stocks (the window where the plans differ and
    # the one P8 uses); 2028-32 shown beside it; sorting on Laura's own wealth is shown but "sorts on the answer"
    Dg = gA_ - gX
    def by_fifths(key, D=D):
        e = np.percentile(key, [20, 40, 60, 80]); qi = np.searchsorted(e, key, side="right")
        rows = {}
        for i in range(5):
            m = qi == i
            rows[f"fifth {i + 1} (1 = worst)"] = {"mean_lead_A09": round(float(D[m].mean())),
                "median_lead_A09": round(float(np.median(D[m]))), "p_A09_ahead": sm((D[m] > 1).mean()),
                "share_of_total_lead_pct": round(float(D[m].sum() / D.sum() * 100), 1)}
        return rows
    out15["B_price_address"] = {"check_A26_mean_lead": round(float(D.mean())),
        "A09_bottom_p50": round(float(np.median(bA))), "XR_bottom_p50": round(float(np.median(q_mc))),
        "p_A09_ahead": sm((D > 1).mean()), "lead_p5_p25_p50_p75_p95": pc(D, (5, 25, 50, 75, 95)),
        "PRIMARY_by_2028_30_stocks": by_fifths(w), "by_2028_30_stocks_gift_only": by_fifths(w, Dg),
        "check_A26_mean_lead_gift_only": round(float(Dg.mean())),
        "by_2028_32_stocks": by_fifths(tot5),
        "by_XR_own_gift_plus_laura2042": by_fifths(gX + l42X),
        "top_fifth_2028_32_mean_lead_v_other_80pct": [round(float(D[tot5 >= np.percentile(tot5, 80)].mean())),
                                                      round(float(D[tot5 < np.percentile(tot5, 80)].mean()))],
        "p_stocks_2028_32_beat_treasuries_by_any": sm((np.exp(tot5) > (1 + y5_28 / 100) ** 5).mean())}
    beat = np.exp(tot5) > (1 + y5_28 / 100) ** 5; ahead = D > 1
    out15["B_price_address"]["rival_ahead_v_stocks_beat_treasuries"] = {
        "p_same_sign": sm((beat == ahead).mean()), "p_rival_ahead_given_stocks_beat": sm(ahead[beat].mean()),
        "p_rival_ahead_given_stocks_lag": sm(ahead[~beat].mean()),
        "mean_lead_when_stocks_beat_v_lag": [round(float(D[beat].mean())), round(float(D[~beat].mean()))]}
    # C: the miss, sized (V47 same day)
    miss = gX < topX - 1; sh_ = topX - gX
    out15["C_miss_sized"] = {"p_missed": sm(miss.mean()),
        "miss_p50_p90_p99_max": [md(sh_, miss)] + ([round(float(np.percentile(sh_[miss], p_))) for p_ in (90, 99)] + [round(float(sh_[miss].max()))] if miss.any() else [0, 0, 0]),
        "share_of_misses_under_2500": sm((sh_[miss] < 2500).mean()) if miss.any() else 1.0,
        "share_of_misses_under_5000": sm((sh_[miss] < 5000).mean()) if miss.any() else 1.0,
        "p_inside_range": sm(((gX >= q_mc - 1e-6) & (gX <= topX + 1)).mean()),
        "paths_below_quoted_bottom_of_N": [int((gX < q_mc - 1e-6).sum()), int(N)],
        "p_miss_over_1k": sm((sh_ > 1000).mean()),
        "p_below_unrounded_top": sm((gX < (top - u31) - 1).mean()),
        "median_below_unrounded_top_when_below": md((top - u31) - gX, gX < (top - u31) - 1),
        "top_quoted_p50": round(float(np.median(topX))), "gift_p50": round(float(np.median(gX)))}
    lr["L15"] = out15'''


def main():
    b = L14.BLOCK14
    assert b.count("for k in (0.80, 0.65):") == 1
    b = b.replace("for k in (0.80, 0.65):", "for k in (0.80, 0.76):")
    assert b.endswith('    lr["L14"] = out14')
    b = b + BLOCK15
    blk = L14.L13.BLOCK13.replace('    lr["L13"] = out13', b)
    add = L14.LR8.ADD.replace('    res["LR05"] = lr', blk)
    block = L14.LR05.BLOCK.replace('    res["LR05"] = lr', add)
    L14.L11.EXTRA = L14.L11.EXTRA.replace('    out["L11"] = res', block)
    names = {k.split()[0]: k for k in L14.L10.SCENARIOS}
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = ("curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 (bridge "
                    "draws 20261101) | rho 0.5 unless S0 | V47's design via L-13 -> L-14 -> A26 | MODEL")
    for k in sys.argv[1:] or ["S0", "S1", "S6"]:
        r = L14.L11.run(**L14.L10.SCENARIOS[names[k]])["LR05"]
        out[names[k]] = {"check_L14_XR": {kk: r["L14"]["XR (V39)"][kk] for kk in ("p_top_reached", "gift_mean")},
                         "L15": r["L15"]}
        print(names[k], json.dumps(out[names[k]], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
