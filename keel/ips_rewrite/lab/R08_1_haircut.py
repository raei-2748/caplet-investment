"""AI-generated (Claude Code), Genius Lab WO-R8 idea 1, 27 Oct 2026. MODEL.
STAMP: curve 22 Oct 2026 | JPM 2027 global equities 7.5% (sceptic 6.5%) | 200,000 paths, seed 20261016 | rho 0 and 0.5 | MODEL
Run: python3 keel/ips_rewrite/lab/R08_1_haircut.py   (uses R08_core's cached paths)

Question (seed b, beaten): the top of the 2031 range = bottom + a share of the stocks. Does the SHARE (1/3, 1/2, 2/3) set
how often the top is reached? Hypothesis: no. If the gift gets share s of the stock fund in 2033 and the top quotes
share s of its 2031 value, the top is reached whenever stocks are no lower in 2033 than in 2031, whatever s is. The
only dial that moves the fractile is a HAIRCUT h: quote the stocks at (1 - h) of their 2031 value, the way a lender
values collateral. Then the top is reached whenever stocks fall less than h.
"""
import json, pathlib
import numpy as np
from scipy.stats import norm
import R08_core as core

HERE = pathlib.Path(__file__).parent


def rule(p, s, h):
    halfL = (1 - s) * p["V33"]                       # Laura's share of the stock fund
    unc = np.maximum(p["S33"] - p["L33"] - halfL, 0)  # coupon gap after leftover cash and Laura's share
    top = p["R"] + s * (1 - h) * p["V31"]
    raw = p["floor_paid"] + s * p["V33"] - unc
    gift = np.minimum(top, raw)
    kept = p["L33"] + halfL - np.minimum(p["S33"], p["L33"] + halfL) + np.maximum(raw - top, 0)
    hit = gift >= top - 1000
    return {
        "p_top_reached_within_1k": round(float(hit.mean()), 4),
        "implied_over_under_cost_ratio": round(float(hit.mean() / (1 - hit.mean())), 2),
        "p_top_reached_exact": round(float((gift >= top - 1).mean()), 4),
        "p_stocks_no_lower_in_2033_than_2031_by_haircut": round(float((p["V33"] >= (1 - h) * p["V31"]).mean()), 4),
        "p_gift_below_bottom": round(float((gift < p["bottom"] - 1e-6).mean()), 4),
        "top_p50": round(float(np.median(top))), "width_p50": round(float(np.median(top - p["bottom"]))),
        "gift_p5_p50_mean": [round(float(np.percentile(gift, 5))), round(float(np.median(gift))), round(float(gift.mean()))],
        "laura_kept_p50_mean": [round(float(np.median(kept))), round(float(kept.mean()))],
    }


if __name__ == "__main__":
    out = {"stamp": core.STAMP.format(mu="7.5% / 6.5%", rho="0 / 0.5")}
    for rho, mu in ((0.0, "1.075"), (0.5, "1.075"), (0.5, "1.065")):
        p = core.paths(rho, mu)
        tab = {}
        for s in (1 / 3, 1 / 2, 2 / 3):
            for h in (0.0, 0.1, 0.2, 0.3):
                tab[f"share={s:.2f} haircut={h:.0%}"] = rule(p, s, h)
        out[f"rho={rho} mu={mu}"] = tab
    # closed-form check (no coupon gap, no tolerance): P(V33/V31 >= 1-h), 2 years, lognormal
    m, v = 2 * (np.log(1.075) - 0.0006), 0.1678 * np.sqrt(2)
    out["closed_form_p_top_7.5pct"] = {f"haircut={h:.0%}": round(float(norm.sf((np.log(1 - h + 1e-12) - m) / v)), 4)
                                      for h in (0.0, 0.1, 0.2, 0.3)}
    (HERE / "R08_1_haircut_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
