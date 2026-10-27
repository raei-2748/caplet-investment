"""AI-generated (Claude Code), Genius Lab WO-R8 idea 3, 27 Oct 2026. MODEL (+ history from FRED GS10).
STAMP: curve 22 Oct 2026 | no equity input | 200,000 paths, seed 20261016 | rates 1pp/yr parallel random walk | MODEL
Run: python3 keel/ips_rewrite/lab/R08_3_corner.py

Question (seed c): the payments' failure corner = (yield change before the 1 Jan 2027 build) x (2028 deposit size).
V25 says "we can name exactly where it breaks: yields falling more than two percentage points before the purchase
while her 2028 deposit more than halves". Map it, then ask how wide the corner really is: the build is 71 days away.
Also carries the unfunded slice through 2027 (it is bought in Jan 2028 at 2028 prices; ~5-year duration slice).
"""
import csv, datetime as dt, json, pathlib
import numpy as np
from scipy.stats import norm

HERE = pathlib.Path(__file__).parent
ROOT = pathlib.Path("/home/user/caplet-investment")
rows = list(csv.DictReader(open(ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv")))
r = rows[0]; assert r["Date"] == "10/22/2026"
ten = {"1 Mo": 1/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3, "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
ts = np.array(list(ten.values())); ps = np.array([float(r[k]) for k in ten]) / 100
V = dt.date(2026, 10, 22); yrs = lambda a, b: (b - a).days / 365.25
T27 = dt.date(2027, 1, 1)


def zdf(shift=0.0):  # same bootstrap as D1_split.py
    grid = np.arange(.5, 30.01, .5); p = np.interp(grid, ts, ps) + shift / 100; d = []
    for y in p:
        c = y / 2; d.append((1 - c * sum(d)) / (1 + c))
    g = np.r_[0, grid]; lz = np.log(np.r_[1, d]); return lambda t: np.exp(np.interp(t, g, lz))


def ladder(shift):
    f = zdf(shift); a = yrs(V, T27); return sum(50000 * f(yrs(V, dt.date(k, 1, 1))) / f(a) for k in range(2033, 2043))


if __name__ == "__main__":
    out = {"stamp": "curve 22 Oct 2026 | 200,000 paths, seed 20261016 | 1pp/yr parallel walk | MODEL; history FRED GS10 monthly 1953-2026"}
    base = ladder(0)
    out["ladder_cost_1jan2027_no_move"] = round(base)
    shifts = [1.0, 0.5, 0.0, -0.25, -0.5, -1.0, -1.5, -2.0, -2.5, -3.0]
    deps = [150, 125, 100, 75, 50, 25, 0]
    grid = {}
    for s in shifts:
        gap = max(ladder(s) - 300000, 0)
        grid[f"{s:+.2f}pp"] = {"gap_at_build": round(gap), "deposit_needed_k": round(gap / 1000, 1),
                               "unfunded_by_deposit_k": {str(d): round(max(gap - d * 1000, 0) / 1000, 1) for d in deps}}
    out["map_unfunded_payments"] = grid
    # boundary: the fall that would exhaust a deposit of D
    ss = np.linspace(0, -4, 801); costs = np.array([ladder(x) for x in ss])
    out["fall_needed_to_exhaust_deposit"] = {f"${d}k": (f"{-ss[np.argmax(costs - 300000 > d * 1000)]:.2f}pp"
                                                        if (costs - 300000 > d * 1000).any() else "> 4pp") for d in deps}
    # how wide is the corner? 71 days to the build
    tau = yrs(V, T27); sd = 1.0 * np.sqrt(tau)
    out["model_p_fall_before_build"] = {f"{x}pp": float(f"{norm.cdf(-x / sd):.2g}") for x in (0.25, 0.5, 1.0, 1.5, 2.0)}
    out["model_sd_pp_to_build"] = round(sd, 3)
    # history: GS10 monthly averages, every 2- and 3-month change since 1953
    gs = np.array([float(x["GS10"]) for x in csv.DictReader(open(ROOT / "keel/library/ips_numbers_2026-10/fred_GS10_monthly.csv"))])
    dates = [x["observation_date"] for x in csv.DictReader(open(ROOT / "keel/library/ips_numbers_2026-10/fred_GS10_monthly.csv"))]
    hist = {}
    for h in (2, 3):
        d = gs[h:] - gs[:-h]; i = int(d.argmin())
        hist[f"{h}_month"] = {"windows": len(d), "worst_fall_pp": round(float(d.min()), 2), "worst_ending": dates[i + h],
                              **{f"p_fall_over_{x}pp": round(float((d <= -x).mean()), 4) for x in (0.5, 1.0, 1.5, 2.0)}}
    out["history_gs10"] = hist
    # MC: build-day move, then the unfunded slice (2033 rung, ~5y duration) rides 2027's move until the 2028 deposit
    rng = np.random.default_rng(20261016); N = 200_000
    d1 = rng.normal(0, sd, N); d2 = rng.normal(0, 1.0, N)
    sg = np.linspace(-3, 3, 241); cg = np.array([ladder(x) for x in sg])
    gap27 = np.maximum(np.interp(d1, sg, cg) - 300000, 0)
    gap28 = gap27 * np.exp(-5.0 * d2 / 100)
    out["mc_p_ladder_over_300k_at_build"] = round(float((gap27 > 0).mean()), 4)
    out["mc_gap28_p50_p95_p99_max"] = [round(float(np.percentile(gap28, q))) for q in (50, 95, 99)] + [round(float(gap28.max()))]
    out["mc_p_payments_unfunded_by_deposit"] = {f"${d}k": float(f"{(gap28 > d * 1000).mean():.3g}") for d in deps}
    (HERE / "R08_3_corner_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
