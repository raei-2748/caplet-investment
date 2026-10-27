"""AI-generated (Claude Code), Genius Lab WO-R8 idea 4, 27 Oct 2026. MODEL.
STAMP: curve 22 Oct 2026 | JPM 2027 global equities 7.5% | 200,000 paths, seed 20261016 | rho 0 and 0.5 | MODEL
Run: python3 keel/ips_rewrite/lab/R08_4_coupons.py

Question (seed e): where do the coupons go? The office model (and the WInS notes' "reinvested coupons fund the rest")
silently assumes each coupon buys more of its OWN rung on the day it arrives, locking that day's yield to the rung's
maturity. The easy alternative in practice is to sweep coupons into a short Treasury fund and roll it. The rungs were
sized assuming term reinvestment, so a sweep lives on the 3-month yield (4.22% on 22 Oct against 4.7-5.3% for the
rungs). How much does the policy choice cost the ten payments? (Cash: no reinvestment, as a bound.)
Plus a deterministic check: yields fall X points the day after the build and stay there.
"""
import datetime as dt, json, pathlib
import numpy as np
import R08_core as core

HERE = pathlib.Path(__file__).parent


def deterministic(dy, mode):
    """Model's 'rates fall and stay' stress (ips_numbers.py s3), with coupons into own rung or a rolling bill fund."""
    import csv
    rows = list(csv.DictReader(open(core.CURVE))); row = rows[0]
    pts = {1/12: "1 Mo", .25: "3 Mo", .5: "6 Mo", 1: "1 Yr", 2: "2 Yr", 3: "3 Yr", 5: "5 Yr", 7: "7 Yr", 10: "10 Yr", 20: "20 Yr", 30: "30 Yr"}
    xs = np.array(list(pts)); ys = np.array([float(row[k]) for k in pts.values()])
    curve = lambda t: np.interp(t, xs, ys)
    yrs = lambda a, b: (b - a).days / 365.25
    TODAY, T27 = dt.date(2026, 10, 22), dt.date(2027, 1, 1); TOFF = yrs(TODAY, T27)
    RUNGS = {2033: (dt.date(2032, 12, 15), None), 2034: (dt.date(2033, 12, 15), None), 2035: (dt.date(2034, 12, 15), None),
             2036: (dt.date(2035, 12, 15), None), 2037: (dt.date(2036, 12, 15), None), 2038: (dt.date(2037, 2, 15), 4.75),
             2039: (dt.date(2038, 5, 15), 4.50), 2040: (dt.date(2039, 11, 15), 4.375), 2041: (dt.date(2040, 11, 15), 4.25),
             2042: (dt.date(2041, 11, 15), 3.125)}
    tot = 0.0
    for py, (mat, cpn) in RUNGS.items():
        T = yrs(T27, mat); y0 = curve(T + TOFF); cc = (y0 if cpn is None else cpn) / 100
        k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        if mode == "own":
            yk = max(y0 + dy, 0.25) / 100; grow = ((1 + yk / 2) ** (2 * (T - k))).sum()
        else:
            rb = max(curve(.25) + dy, 0.25) / 100; grow = ((1 + rb / 12) ** (12 * (T - k))).sum()
        d = 1 + cc / 2 * grow
        db = 1 + cc / 2 * ((1 + y0 / 200) ** (2 * (T - k))).sum()
        gy = yrs(mat, dt.date(py, 1, 1))
        g = (1 + max(curve(.25) + dy, 0.25) / 100) ** gy; gb = (1 + curve(.25) / 100) ** gy
        tot += 50000 / (db * gb) * d * g
    return round(tot)


if __name__ == "__main__":
    out = {"stamp": core.STAMP.format(mu="7.5%", rho="0 / 0.5")}
    for rho in (0.0, 0.5):
        p = core.paths(rho, "1.075")
        buf = p["L33"] + 0.5 * p["V33"]          # leftover cash + Laura's half: what stands before the gift
        res = {}
        for name, key in (("coupons buy their own rung (model default)", "delivered"),
                          ("coupons swept into a rolling 3-month bill fund", "delivered_rolled"),
                          ("coupons held as cash (bound)", "delivered_cash")):
            s = np.maximum(500000 - p[key], 0)
            res[name] = {"shortfall_p50_p95_p99": [round(float(np.percentile(s, q))) for q in (50, 95, 99)],
                         "mean": round(float(s.mean())), "p_short_over_1k": round(float((s > 1000).mean()), 4),
                         "p_short_exceeds_leftover_plus_lauras_half": round(float((s > buf).mean()), 4)}
        out[f"rho={rho}"] = res
    out["deterministic_ten_payment_total"] = {f"{dy:+g}pp": {"own rung": deterministic(dy, "own"),
                                                             "bill sweep": deterministic(dy, "bills")} for dy in (0, -1, -2)}
    (HERE / "R08_4_coupons_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
