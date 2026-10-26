"""AI-generated (Claude Code), 27 Oct 2026. MODEL. WO-R5: wrong-way risk + newsvendor check.
Run from repo root: python3 keel/ips_rewrite/lab/R05_joint.py
Runs the unchanged ips_numbers.py on the 22 Oct curve (patched as D1_run_22oct.py), but makes each year's stock
shock (2028-2032) correlated with that year's parallel yield change: rho > 0 means yields fall when stocks fall
(a recession), which is the case R05 S2 worries about. rho = 0 reproduces the independent model.
"""
import json, pathlib, io, contextlib
import numpy as np
ROOT = pathlib.Path("/home/user/caplet-investment")
m = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
here = pathlib.Path(__file__).parent

EXTRA = '''
    below_bottom = gift < bottom - 1e-6
    big = S33 > np.percentile(S33, 95)
    out["R05"] = {
      "p_top_reached_within_1k": round(float((gift >= top - 1000).mean()), 4),
      "implied_over_under_cost_ratio": round(float((gift >= top - 1000).mean() / max(1e-9, 1 - (gift >= top - 1000).mean())), 2),
      "p_gift_below_bottom": round(float(below_bottom.mean()), 4),
      "p_coupon_gap_exceeds_lauras_half": round(float((uncovered > 0).mean()), 4),
      "S33_p50_p95_p99": [round(float(np.percentile(S33, q))) for q in (50, 95, 99)],
      "half_p5_p50_all": [round(float(np.percentile(half, q))) for q in (5, 50)],
      "half_p5_p50_when_S33_in_worst_5pct": [round(float(np.percentile(half[big], q))) for q in (5, 50)],
      "uncovered_p99": round(float(np.percentile(uncovered, 99))),
      "uncovered_mean_when_positive": round(float(uncovered[uncovered > 0].mean())) if (uncovered > 0).any() else 0,
      "p_floor_dented_by_gap_over_5k": round(float((uncovered > 5000).mean()), 4),
      "top_p50": round(float(np.median(top))), "bottom_p50": round(float(np.median(bottom))),
    }
    out["laura_kept_2033"] = {'''

def run(rho, mu="1.075"):
    tmp = here / f"_r05_{rho}_{mu}.json"
    src = m.read_text()
    reps = [
        ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
         f'CURVE_CSV = pathlib.Path(r"{ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"}")'),
        ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
        ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
        ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
        ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', f'EQ_MU, EQ_VOL, VT_FEE = np.log({mu}), 0.1678, 0.0006'),
        ('    z = rng.normal(size=(N, 5))', f'''    _t0 = yrs(TODAY, T28)
    _dy = np.stack([sh(_t0 + j + 1) - sh(_t0 + j) for j in range(5)], axis=1) / RATE_VOL
    z = {rho} * _dy + np.sqrt(1 - {rho}**2) * rng.normal(size=(N, 5))'''),
        ('    out["laura_kept_2033"] = {', EXTRA),
    ]
    for old, new in reps:
        assert src.count(old) == 1, old
        src = src.replace(old, new)
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, str(m), "exec"), {"__name__": "__main__", "__file__": str(m)})
    res = json.loads(tmp.read_text()); tmp.unlink()
    return res

if __name__ == "__main__":
    table = {}
    for mu in ("1.075", "1.065"):
        for rho in (0.0, 0.3, 0.5):
            r = run(rho, mu)
            table[f"mu={mu} rho={rho}"] = {**r["R05"], "ladder_headroom": r["ladder_headroom"],
                                           "stock_fund_2jan2028_p50": r["stock_fund_2jan2028"]["p50"]}
    (here / "R05_joint_results.json").write_text(json.dumps(table, indent=1))
    print(json.dumps(table, indent=1))
