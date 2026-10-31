"""AI-generated (Claude Code), Sat 31 Oct 2026, the Genius Lab (round 4 beat 5, Felix builds). MODEL.
(Keel is a simulated team, AI-written.) L-14 "the price of the floor": Q12, why not a safe ladder and the rest in stocks?
  XR    V39's design: L-12/L-13 chain ("MB+T +lock") with L-13's slide (the top cut by the 2031 mark like the bottom)
  A09   the rival (keel/ips_rewrite/rivals/A09.md) at its strongest, on the SAME paths and seed: the same cheque
        ladder; the 2028 remainder R in 80% world stocks (the same VT draws as XR's fund) / 20% intermediate
        Treasuries (5-year yield, duration 4.5), rebalanced yearly; on naming day (1 Jan 2031) a share k of the pot
        buys a 2-year Treasury held to Jan 2033 (the bottom); the rest stays 80/20; gift = bottom + half the rest,
        capped at the top; the other half is Laura's. Given every XR rule too: the same 2031 mark, cushion, bank-at-
        the-mark sale and slide. k = 0.80 keeps about the same fifth in stocks after naming as XR; k = 0.65 sensitivity.
  W-04  both plans in the worst (and best) 5% of 2028-30 stock paths (Giving USA: giving falls in recession years)
  R06   the Window's "about a fifteenth": the stock fund's share of the portfolio on 2 Jan 2028, on this design
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: L-13 run.py chain unchanged; one block appended | MODEL.
Run from repo root: python3 keel/rooms/lab/L-14_price_of_the_floor/run.py [S0 S1 S2 S6]  (~3 min each, sequential)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parent / "L-13_slide_the_range" / "run.py"
_spec = importlib.util.spec_from_file_location("L13", P)
L13 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(L13)
LR8 = L13.LR8; LR05, L11 = LR8.LR05, LR8.L11; L10 = L11.L10

BLOCK14 = '''
    lr["L13"] = out13
    # ---- Genius Lab L-14: the price of the floor (A09 v XR, same paths) ----
    pc = lambda a, ps=(5, 50): [round(float(np.percentile(a, p_))) for p_ in ps]
    w = logr[:, :3].sum(axis=1)                               # 2028-30 stock draws, shared by both plans
    worst = w <= np.percentile(w, 5); best = w >= np.percentile(w, 95)
    def report14(name, bot_q, top_q, g, l42, cash):
        r = {"p_cheque_short_over_1k": sm((tot_short(cash) > 1000).mean()),
             "bottom_quoted_p5_p50": pc(bot_q), "top_quoted_p5_p50": pc(top_q),
             "gift_p5_p50_p95": pc(g, (5, 50, 95)), "gift_mean": round(float(g.mean())),
             "p_top_reached": sm((g >= top_q - 1).mean()), "p_below_quoted_bottom": sm((g < bot_q - 1e-6).mean()),
             "laura_2042_p50_mean": [round(float(np.median(l42))), round(float(l42.mean()))],
             "gift_plus_laura2042_mean": round(float((g + l42).mean())),
             "p_bottom_below_125k": sm((bot_q < 125000).mean()), "p_bottom_below_100k": sm((bot_q < 100000).mean())}
        for tag, m in (("worst5_2028_30", worst), ("best5_2028_30", best)):
            r[tag] = {"bottom_p50": round(float(np.median(bot_q[m]))), "top_p50": round(float(np.median(top_q[m]))),
                      "gift_p5_p50": pc(g[m]), "laura_2042_p50": round(float(np.median(l42[m])))}
        return r
    out14 = {}
    # XR, V39 (slide on)
    topX = f5(top - u31)
    cash, sold, gX = at_2033(cash0, need33, half_b, True, topX, lockd)
    excX = np.maximum(lockd - (cash - cash0 - sold) - gX, 0)
    l42X = (half_b - sold) * g_after + np.maximum(cash - S33 - extra_, 0) + excX
    out14["XR (V39)"] = report14("XR", q_mc, topX, gX, l42X, cash)
    # A09: 80/20 to naming day, then the bottom bought
    yb = [np.maximum(curve(5) + sh(t28 + j), YMIN) for j in range(6)]
    rbond = [yb[j] / 100 - 4.5 * (yb[j + 1] - yb[j]) / 100 for j in range(5)]
    gst = np.exp(logr)
    mix = [0.8 * gst[:, j] + 0.2 * (1 + rbond[j]) for j in range(5)]
    W31 = R * mix[0] * mix[1] * mix[2]
    lock_g = (1 + np.maximum(curve(2) + sh(t28 + 3), YMIN) / 200) ** 4
    out14["A09_pot_2031_p5_p50_p95"] = pc(W31, (5, 50, 95))
    out14["XR_gift_money_2031_p5_p50_p95 (floor at 2031 yields + stocks)"] = pc(floor31 / lock_g + V31, (5, 50, 95))
    out14["XR_stock_share_after_naming_p50"] = round(float(np.median(V31 / (floor31 / lock_g + V31))), 3)
    gA = {}
    for k in (0.80, 0.65):
        L31 = k * W31 * lock_g
        rest31 = (1 - k) * W31
        rest33 = rest31 * mix[3] * mix[4]
        xA = np.minimum(need31, 0.5 * rest31)
        keepA = np.where(rest31 > 0, 1 - xA / np.maximum(0.5 * rest31, 1e-9), 1.0)
        halfA = 0.5 * rest33
        uA = ceil5(np.maximum(S31 + C - L33 - 0.5 * rest31, 0))
        botA = np.maximum(f5(L31) - uA, 0)
        topA = np.maximum(f5(L31 + 0.5 * rest31 - uA), botA)
        c0 = L33 + xA * bill2
        cash, sold, g = at_2033(c0, need33, halfA * keepA, True, topA, L31 + halfA)
        exc = np.maximum(L31 + halfA - (cash - c0 - sold) - g, 0)
        l42 = (halfA * keepA - sold) * g_after + np.maximum(cash - S33 - extra_, 0) + exc
        out14[f"A09 k={k}"] = report14("A09", botA, topA, g, l42, cash)
        gA[k] = (botA, g, l42)
    # Kai's bet (H-005 r1): do A09's sub-$100k bottoms cluster in bad 2028-30 stock markets?
    bA8 = gA[0.80][0]; lo = bA8 < 100000
    out14["kai_bet_A09_bottom_under_100k"] = {"p": sm(lo.mean()),
        "share_with_2028_30_stocks_down": sm((w[lo] < 0).mean()) if lo.any() else 0,
        "share_in_worst_10pct_of_2028_30": sm((w[lo] <= np.percentile(w, 10)).mean()) if lo.any() else 0,
        "median_2028_30_stock_return_pct": round(float((np.exp(np.median(w[lo])) - 1) * 100), 1) if lo.any() else 0,
        "p_stocks_down_2028_30_all_paths": sm((w < 0).mean())}
    # the price of the floor, path by path (XR minus A09 k=0.8)
    bA, gA8, lA8 = gA[0.80]
    out14["price"] = {"median_gift_XR_minus_A09": round(float(np.median(gX) - np.median(gA8))),
                      "mean_gift_XR_minus_A09": round(float(gX.mean() - gA8.mean())),
                      "mean_gift_plus_laura2042_XR_minus_A09": round(float((gX + l42X).mean() - (gA8 + lA8).mean())),
                      "p_XR_gift_higher": sm((gX > gA8 + 1).mean()),
                      "p_XR_bottom_higher": sm((q_mc > bA + 1).mean()),
                      "worst5_bottom_XR_minus_A09_p50": round(float(np.median((q_mc - bA)[worst]))),
                      "worst5_gift_XR_minus_A09_p50": round(float(np.median((gX - gA8)[worst]))),
                      "best5_gift_XR_minus_A09_p50": round(float(np.median((gX - gA8)[best])))}
    # the premium test: the gift money alone (no halves, no cap), stocks at 7.5% v stocks earning only the 2028
    # five-year Treasury yield (same shocks). If the mean gap vanishes, A09's extra is the stock premium: pay for risk.
    zz = (logr - (EQ_MU - VT_FEE)) / EQ_VOL
    gq = np.exp(np.log(1 + y5_28 / 100)[:, None] - VT_FEE - 0.5 * EQ_VOL ** 2 + EQ_VOL * zz)
    def pots(gs):
        mx = [0.8 * gs[:, j] + 0.2 * (1 + rbond[j]) for j in range(5)]
        w31 = R * mx[0] * mx[1] * mx[2]
        pA = 0.8 * w31 * lock_g + 0.2 * w31 * mx[3] * mx[4]
        pX = floor_paid + B0 * gs.prod(axis=1)
        return pX, pA
    prem = {}
    for tag, gs in (("stocks 7.5%", gst), ("stocks earn the Treasury yield", gq)):
        pX, pA = pots(gs)
        prem[tag] = {"XR_p5_p50_mean": pc(pX) + [round(float(pX.mean()))], "A09_p5_p50_mean": pc(pA) + [round(float(pA.mean()))],
                     "mean_gap_A09_minus_XR": round(float(pA.mean() - pX.mean())),
                     "p5_gap_XR_minus_A09": round(float(np.percentile(pX, 5) - np.percentile(pA, 5)))}
    out14["premium_test_gift_money_2033"] = prem
    # Kai's check (H-005 r2): the world-stock return (compound, before fee) at which the average gifts are equal
    def gifts(gs):
        v31 = B0 * gs[:, :3].prod(axis=1); v33 = B0 * gs.prod(axis=1)
        xx = np.minimum(need31, 0.5 * v31)
        hb = 0.5 * v33 * np.where(v31 > 0, 1 - xx / np.maximum(0.5 * v31, 1e-9), 1.0)
        tq = f5(R + 0.5 * v31 - ceil5(np.maximum(S31 + C - L33 - 0.5 * v31, 0)))
        gx = at_2033(L33 + xx * bill2, need33, hb, True, tq, floor_paid + 0.5 * v31 * bill2)[2]
        mx = [0.8 * gs[:, j] + 0.2 * (1 + rbond[j]) for j in range(5)]
        w31 = R * mx[0] * mx[1] * mx[2]; L31_ = 0.8 * w31 * lock_g; r31 = 0.2 * w31; r33 = r31 * mx[3] * mx[4]
        xa = np.minimum(need31, 0.5 * r31); ha = 0.5 * r33 * np.where(r31 > 0, 1 - xa / np.maximum(0.5 * r31, 1e-9), 1.0)
        ua = ceil5(np.maximum(S31 + C - L33 - 0.5 * r31, 0)); ba = np.maximum(f5(L31_) - ua, 0)
        ta = np.maximum(f5(L31_ + 0.5 * r31 - ua), ba)
        ga = at_2033(L33 + xa * bill2, need33, ha, True, ta, L31_ + 0.5 * r33)[2]
        return gx, ga, ba
    be = {}
    for m in (0.03, 0.04, 0.05, 0.06, 0.075):
        gx, ga, ba = gifts(np.exp(np.log(1 + m) - VT_FEE + EQ_VOL * zz))
        be[f"{m:.3f}"] = {"mean_gift_XR": round(float(gx.mean())), "mean_gift_A09": round(float(ga.mean())),
                          "median_gift_XR": round(float(np.median(gx))), "median_gift_A09": round(float(np.median(ga))),
                          "p_A09_bottom_under_100k": sm((ba < 100000).mean())}
    out14["kai_breakeven_stock_return"] = be
    # R06 "a fifteenth" on this design: the stock fund's share on 2 Jan 2028
    port28 = cost27_p * (1 + curve(6 + TOFF) / 100) + leftover27 * 1.045 + DEPOSIT28
    out14["R06_stock_fund_2028"] = {"B0_p50": round(float(np.median(B0))),
        "share_of_portfolio_p50": round(float(np.median(B0 / port28)), 4),
        "one_in_x_of_portfolio": round(float(1 / np.median(B0 / port28)), 1),
        "share_of_both_deposits_p50": round(float(np.median(B0 / (DEPOSIT27 + DEPOSIT28))), 4),
        "share_of_2028_deposit_p50": round(float(np.median(B0 / DEPOSIT28)), 4)}
    lr["L14"] = out14'''


def main():
    blk = L13.BLOCK13
    assert blk.count('    lr["L13"] = out13') == 1
    blk = blk.replace('    lr["L13"] = out13', BLOCK14)
    add = LR8.ADD
    assert add.count('    res["LR05"] = lr') == 1
    add = add.replace('    res["LR05"] = lr', blk)
    assert LR05.BLOCK.count('    res["LR05"] = lr') == 1
    block = LR05.BLOCK.replace('    res["LR05"] = lr', add)
    assert L11.EXTRA.count('    out["L11"] = res') == 1
    L11.EXTRA = L11.EXTRA.replace('    out["L11"] = res', block)
    names = {k.split()[0]: k for k in L10.SCENARIOS}
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 unless S0 | MODEL"
    for k in sys.argv[1:] or ["S0", "S1", "S2", "S6"]:
        name = names[k]
        r = L11.run(**L10.SCENARIOS[name])["LR05"]
        out[name] = {"check_vs_L13_slide": r["L13"]["A slide (top cut like the bottom)"], "L14": r["L14"]}
        print(name, json.dumps(out[name]["L14"], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
