"""AI-generated (Claude Code), Genius Lab WO-R8 idea 2, 27 Oct 2026. MODEL.
STAMP: curve 22 Oct 2026 | JPM 2027 global equities 7.5% (sceptic 6.5%) | 200,000 paths, seed 20261016 | rho 0 and 0.5 | MODEL
Run: python3 keel/ips_rewrite/lab/R08_2_lock.py

Question (seed d): "lock what you announce". Under today's rule the gift's half of the stock fund is capped at its 2031
value, so between 2031 and 2033 the facility keeps every fall and hands every rise back to Laura: the gift is short a
put, Laura holds the matching call, and nobody paid a premium. If, on the day Laura names the range (1 Jan 2031), the
promised half of the stocks is sold into IBTM (the floor fund, which matures Dec 2032), the top becomes owned too.
Variants: A today; B lock the whole promised half; C = B and quote the bottom as floor + locked half (rounded down);
D lock half of the promised half (a quarter of the fund) and raise the bottom by that quarter.
Laura's own half stays in stocks in every variant; the coupon gap draws on leftover cash, then Laura's half, as today.
"""
import json, pathlib
import numpy as np
import R08_core as core

HERE = pathlib.Path(__file__).parent
rd = lambda x: np.floor((x - 3700) / 5000) * 5000      # the office's "rounded down" rule for a quoted bottom


def variant(p, lock_share, raise_bottom):
    halfL = 0.5 * p["V33"]
    unc = np.maximum(p["S33"] - p["L33"] - halfL, 0)
    top = p["R"] + 0.5 * p["V31"]
    locked = lock_share * p["V31"]
    stock_part = (0.5 - lock_share) * p["V33"]
    raw = p["floor_paid"] + locked * p["g2"] + stock_part - unc
    gift = np.minimum(top, raw)
    bottom = rd(p["R"] + locked) if raise_bottom else p["bottom"]
    kept = p["L33"] + halfL - np.minimum(p["S33"], p["L33"] + halfL) + np.maximum(raw - top, 0)
    total = gift + kept
    hit = gift >= top - 1000
    r = {"p_top_reached_within_1k": round(float(hit.mean()), 4),
         "p_gift_below_quoted_bottom": round(float((gift < bottom - 1e-6).mean()), 4),
         "bottom_p50": round(float(np.median(bottom))), "top_p50": round(float(np.median(top))),
         "gift_p5_p50_mean": [round(float(np.percentile(gift, q))) for q in (5, 50)] + [round(float(gift.mean()))],
         "gift_shortfall_below_top_mean": round(float((top - gift).mean())),
         "laura_kept_p5_p50_mean": [round(float(np.percentile(kept, q))) for q in (5, 50)] + [round(float(kept.mean()))],
         "total_gift_plus_kept_p5_p50_mean": [round(float(np.percentile(total, q))) for q in (5, 50)] + [round(float(total.mean()))]}
    return r, total, gift


if __name__ == "__main__":
    out = {"stamp": core.STAMP.format(mu="7.5% / 6.5%", rho="0 / 0.5")}
    for rho, mu in ((0.0, "1.075"), (0.5, "1.075"), (0.5, "1.065")):
        p = core.paths(rho, mu)
        res = {}
        A, tA, gA = variant(p, 0.0, False)
        res["A today (cap, no lock)"] = A
        for name, ls, rb in (("B lock promised half", 0.5, False), ("C lock promised half + raise bottom", 0.5, True),
                             ("D lock a quarter + raise bottom", 0.25, True)):
            r, t, g = variant(p, ls, rb)
            r["expected_total_cost_vs_A"] = round(float(tA.mean() - t.mean()))
            r["median_total_cost_vs_A"] = round(float(np.median(tA - t)))
            r["gift_gain_vs_A_mean"] = round(float(g.mean() - gA.mean()))
            res[name] = r
        # the free option under today's rule, in dollars
        halfL = 0.5 * p["V33"]; unc = np.maximum(p["S33"] - p["L33"] - halfL, 0)
        top = p["R"] + 0.5 * p["V31"]; raw = p["floor_paid"] + 0.5 * p["V33"] - unc
        res["today: value handed to Laura above the cap (mean)"] = round(float(np.maximum(raw - top, 0).mean()))
        res["today: facility's expected miss below the top (mean)"] = round(float(np.maximum(top - raw, 0).mean()))
        res["IBTM growth 2031->Dec 2032 p5/p50/p95"] = [round(float(np.percentile(p["g2"], q)), 4) for q in (5, 50, 95)]
        out[f"rho={rho} mu={mu}"] = res
    (HERE / "R08_2_lock_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
