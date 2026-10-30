"""AI-generated (Claude Code), Fri 30 Oct 2026, the Genius Lab (round 3 beat 5, Nora builds). MODEL.
(Keel is a simulated team, AI-written.) L-13 "slide the range": why does V29's top miss, and what does each end cost?
  base   V29's design (L-12 = LR8 "MB+T +lock"): bottom = floor rule cut by the 2031 mark's uncovered gap (q_mc);
         top = R + half the stocks on naming day (NOT cut); top quoted rounded down to $5k
  why    every missed top split by cause: (i) the Treasuries bought on naming day pay less than the quoted top
         (the anchor), (ii) they pay enough but the cheques' 2033 top-up takes the gift below it (cheques first)
  A      slide the whole range: the top is cut by the same uncovered gap as the bottom (one mark, both ends)
  B      Library #84 (b): top named in 2031 on that day's prices = what the bought Treasuries project to pay in 2033
         (floor at 2031 yields frozen + promised half at the 2031 bill rate), less the uncovered gap, less a cushion
         k fixed in advance ($0 / $2.5k / $5k), rounded down to $5k: does one k hold the top's chance steady?
  reqs   Window W-03 (width > 20% of the top, as quoted), Writing Room (door 4 takes from the gift after naming),
         Courtroom (door table: where each change lands), Library #84 (a) (implied over/under cost ratio)
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | rho 0.5 unless S0 | basis: LR8 run.py chain unchanged (as L-12); one block appended | MODEL.
Run from repo root: python3 keel/rooms/lab/L-13_slide_the_range/run.py [S0 S1 S2 S6]  (~3 min each, sequential)"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / "long_room" / "LR8_banked_at_the_mark" / "run.py"
_spec = importlib.util.spec_from_file_location("LR8", P)
LR8 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LR8)
LR05, L11 = LR8.LR05, LR8.L11
L10 = L11.L10

BLOCK13 = '''
    # ---- Genius Lab L-13: slide the range ----
    f5 = lambda a: np.floor(a / 5000) * 5000
    need33 = S33 + C; cash0 = L33 + x * bill2
    nb = np.maximum(need33 - cash0, 0); fh = np.minimum(nb, half_b); fg = np.minimum(nb - fh, lockd)
    u31 = ceil5(np.maximum(S31 + C - L33 - 0.5 * V31, 0))        # the 2031 mark's uncovered gap (cuts q_mc)
    tot_short = lambda cash: np.maximum(S33 + extra_ - cash, 0) + unfilled
    # floor projected on naming day: IBTM's coupons reinvested at yields frozen on 1 Jan 2031
    k_ = np.arange(1, int(np.floor(t_ibtm * 2)) + 1) / 2
    idx_ = np.clip(np.searchsorted(step_t, k_ + yrs(TODAY, T28)), 0, len(step_t) - 1)
    i31 = np.searchsorted(step_t, yrs(TODAY, dt.date(2031, 1, 1)))
    yk31 = np.maximum(y5_28[:, None] + shifts[:, np.minimum(idx_, i31)] - s28[:, None], YMIN) / 100
    d31 = 1 + (y5_28 / 200) * ((1 + yk31 / 2) ** (2 * (t_ibtm - k_)[None, :])).sum(axis=1)
    db_ = 1 + (y5_28 / 200) * ((1 + y5_28[:, None] / 200) ** (2 * (t_ibtm - k_)[None, :])).sum(axis=1)
    floor31 = R * d31 / db_
    bill2_31 = (1 + np.maximum(curve(.25) + sh(t28 + 3), YMIN) / 100) ** 2
    D31 = floor31 + 0.5 * V31 * bill2_31                          # what naming day's Treasuries project to pay
    def arm(top_q, bot_q):
        cash, sold, g = at_2033(cash0, need33, half_b, True, top_q, lockd)
        reach = g >= top_q - 1
        w = top_q - bot_q
        m = 1 - reach.mean()
        return {"top_quoted_p5_p50_p95": [round(float(np.percentile(top_q, p_))) for p_ in (5, 50, 95)],
                "bottom_quoted_p50": round(float(np.median(bot_q))),
                "p_top_reached": sm(reach.mean()),
                "implied_over_vs_under_cost_ratio": round(float(reach.mean() / max(m, 1e-9)), 2),
                "p_below_quoted_bottom": sm((g < bot_q - 1e-6).mean()),
                "gift_p5_p50_mean": [round(float(np.percentile(g, 5))), round(float(np.median(g))), round(float(g.mean()))],
                "median_short_of_top_when_missed": md(top_q - g, ~reach),
                "width_p50": round(float(np.median(w))), "width_pct_of_top_p50": round(float(np.median(w / np.maximum(top_q, 1))) * 100, 1),
                "p_width_over_20pct_of_top": sm((w > 0.2 * top_q).mean()),
                "p_payment_short_over_1k": sm((tot_short(cash) > 1000).mean())}
    T5 = f5(top)
    out13 = {"base V29": arm(T5, q_mc)}
    miss = lockd - fg < T5 - 1
    out13["why_top_missed"] = {"p_missed": sm(miss.mean()),
        "anchor_bought_treasuries_below_quoted_top": sm((miss & (lockd < T5 - 1)).mean()),
        "cheques_first_2033_topup_took_it_below": sm((miss & (lockd >= T5 - 1)).mean()),
        "p_2031_mark_cut_the_bottom_not_the_top": sm((u31 > 0).mean()),
        "median_cut_when_cut": md(u31, u31 > 0)}
    out13["A slide (top cut like the bottom)"] = arm(f5(top - u31), q_mc)
    for kc in (0, 2500, 5000):
        out13[f"B projected top, cushion {kc}"] = arm(f5(np.maximum(D31 - u31 - kc, q_mc)), q_mc)
    # Writing Room: door 4 takes from the gift after naming because her half is gone
    out13["door4_gift_pays_cheques"] = {"p_gift_pays_over_1": sm((fg > 1).mean()), "p_over_1k": sm((fg > 1000).mean()),
        "median_taken_when_taken": md(fg, fg > 1), "p_that_pushes_gift_below_quoted_top": sm(((fg > 1) & (lockd - fg < T5 - 1)).mean())}
    # Courtroom: where each change lands (share of paths)
    out13["door_table"] = {"a_hope_before_2031_stocks_below_2028_cost": sm((V31 < B0).mean()),
        "b_her_half_sold_2031_or_2033": sm(((x > 1) | (fh > 1)).mean()),
        "c_bottom_cut_before_quoted": sm((q_mc < bottom - 1).mean()),
        "d_gift_after_naming_pays_cheques": sm((fg > 1).mean()),
        "e_cheque_short_over_1k": sm((tot_short(cash0 + fh + fg) > 1000).mean())}
    lr["L13"] = out13
    res["LR05"] = lr'''


def main():
    add = LR8.ADD
    assert add.count('    res["LR05"] = lr') == 1
    add = add.replace('    res["LR05"] = lr', BLOCK13)
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
        out[name] = {"check_vs_L12": r["MB+T +lock"], "L13": r["L13"]}
        print(name, json.dumps(out[name]["L13"], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
