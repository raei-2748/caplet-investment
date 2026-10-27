"""AI-generated (Claude Code), Genius Lab WO-R8 idea 5, 27 Oct 2026. MODEL.
STAMP: curve 22 Oct 2026 | JPM 2027 global equities 7.5% (sceptic 6.5%) | 200,000 paths, seed 20261016 | rho 0 and 0.5 | MODEL
Run: python3 keel/ips_rewrite/lab/R08_5_rematch.py

Question (seed a, beaten): the Jan 2033 one-time re-match. On 1 Jan 2033 the coupon gap still to come can be projected
from that day's yields. Set aside an amount A in T-bills next to the ladder before the gift is paid; after that, no
share is ever sold to meet a payment (the TNA's "VT ... not standing between Laura and a payment deadline").
How big should A be? Rules tested:
  today  - no set-aside: the gap is drawn when it shows up (from Laura's half, which stays in stocks to 2042)
  R0     - A = the projected gap (the Archive's proposal)
  R+10k  - A = projected gap + a flat $10,000 (close to L-10's coverage test)
  S1     - A = what the gap would be if yields fell a FURTHER 1 point for good after 2033 (a stress test, the way a
           bank or insurer sizes capital: the cushion shrinks by itself as the rungs mature)
  S2     - the same with a 2-point fall
  R+5k / R+7.5k - flat cushions sized to the 2033 projection's own error (p95 / p99 of true minus projected gap)
A is drawn from leftover Treasury cash, then Laura's half of the stocks, then the gift (above the cap first). Bills are
assumed to earn nothing (conservative). "Payments short" = total nominal shortfall 2033-42 above A (> $1k).
"""
import json, pathlib
import numpy as np
import R08_core as core

HERE = pathlib.Path(__file__).parent


def rematch(p, A):
    halfL = 0.5 * p["V33"]
    top = p["R"] + 0.5 * p["V31"]
    need = np.maximum(A - p["L33"] - halfL, 0)
    raw = p["floor_paid"] + 0.5 * p["V33"] - need
    gift = np.minimum(top, raw)
    stock_sold = np.minimum(np.maximum(A - p["L33"], 0), halfL + np.maximum(p["floor_paid"] + 0.5 * p["V33"] - top, 0))
    kept = p["L33"] + halfL - np.minimum(A, p["L33"] + halfL) + np.maximum(raw - top, 0)
    late = p["shortfall"] - A
    return gift, stock_sold, kept, late


def stats(p, A, base_gift):
    gift, sold, kept, late = rematch(p, A)
    hit = gift >= (p["R"] + 0.5 * p["V31"]) - 1000
    pos = A > 1
    return {"p_set_aside": round(float(pos.mean()), 4),
            "set_aside_p50_p95_when_any": [round(float(np.percentile(A[pos], q))) for q in (50, 95)] if pos.any() else [0, 0],
            "p_stock_sold_in_2033": round(float((sold > 1).mean()), 4),
            "stock_sold_p50_when_sold": round(float(np.median(sold[sold > 1]))) if (sold > 1).any() else 0,
            "p_top_reached_within_1k": round(float(hit.mean()), 4),
            "p_gift_below_bottom": round(float((gift < p["bottom"] - 1e-6).mean()), 4),
            "gift_p50_mean": [round(float(np.median(gift))), round(float(gift.mean()))],
            "gift_cost_vs_today_mean": round(float(base_gift.mean() - gift.mean())),
            "p_payments_short_without_selling_stock_after_2033": round(float((late > 1000).mean()), 4),
            "median_short_when_short": round(float(np.median(late[late > 1000]))) if (late > 1000).any() else 0,
            "p_short_even_selling_lauras_rest_by_2042": round(float((late > 1000 + kept * p["g_after"]).mean()), 4),
            "unused_set_aside_returned_mean": round(float(np.maximum(A - p["shortfall"], 0).mean()))}


if __name__ == "__main__":
    out = {"stamp": core.STAMP.format(mu="7.5% / 6.5%", rho="0 / 0.5")}
    for rho, mu in ((0.0, "1.075"), (0.5, "1.075"), (0.5, "1.065")):
        p = core.paths(rho, mu)
        base_gift = p["gift"]
        # today's rule: gap drawn at need; after 2033 the extra comes from Laura's half (stock sold after 2033)
        extra = np.maximum(p["shortfall"] - p["S33"], 0)
        res = {"today": {"p_stock_sold_after_2033_for_payments": round(float((extra > 1000).mean()), 4),
                         "p_any_stock_sold_for_payments_2033_42": round(float(((p["S33"] > p["L33"] + 1) | (extra > 1000)).mean()), 4),
                         "p_top_reached_within_1k": round(float((p["gift"] >= p["top"] - 1000).mean()), 4),
                         "gift_p50_mean": [round(float(np.median(p["gift"]))), round(float(p["gift"].mean()))]}}
        for name, A in (("R0 projected gap", p["S33"]), ("R+5k flat", p["S33"] + 5000), ("R+7.5k flat", p["S33"] + 7500),
                        ("R+10k flat", p["S33"] + 10000),
                        ("S1 one-point stress", p["S33m1"]), ("S2 two-point stress", p["S33m2"]),
                        ("S1 + $5k", p["S33m1"] + 5000)):
            res[name] = stats(p, A, base_gift)
        res["projection_error_2033 (true minus projected gap) p95/p99"] = [round(float(np.percentile(p["shortfall"] - p["S33"], q))) for q in (95, 99)]
        out[f"rho={rho} mu={mu}"] = res
    (HERE / "R08_5_rematch_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
