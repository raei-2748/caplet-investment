"""AI-generated (Claude Code), 26 Oct 2026. Run from repo root: python3 keel/ips_rewrite/lab/D1_run_22oct.py 1.07 (or 1.075). D1 lab: run the unchanged ips_numbers.py on the 22 Oct curve (patch as C-01), plus a decomposition of below-top paths."""
import json, pathlib, sys
ROOT = pathlib.Path("/home/user/caplet-investment")
mu = sys.argv[1]
m = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
tmp = pathlib.Path(__file__).parent / f"_d1_{mu}.json"
src = m.read_text()
for old, new in [
    ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
     f'CURVE_CSV = pathlib.Path(r"{ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"}")'),
    ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
    ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
    ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
    ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', f'EQ_MU, EQ_VOL, VT_FEE = np.log({mu}), 0.1678, 0.0006'),
    ('    out["laura_kept_2033"] = {', '''    below = gift < top - 1000
    stk = V33 < V31
    fl = floor_paid < R - 1000
    unc_ = uncovered > 0
    out["D1"] = {"p_below_top": round(float(below.mean()),4),
      "below_top_and_stocks_fell_31_33": round(float((below & stk).mean()),4),
      "below_top_stocks_did_not_fall": round(float((below & ~stk).mean()),4),
      "below_top_with_floor_payout_short_1k": round(float((below & fl).mean()),4),
      "below_top_with_uncovered_coupon_gap": round(float((below & unc_).mean()),4),
      "p_stocks_fall_31_33": round(float(stk.mean()),4),
      "p_ladder_gap_cuts_R": round(float((R < 149999).mean()),4),
      "R_p5_p50": [round(float(np.percentile(R,5))), round(float(np.median(R)))],
      "ibtm_cost_p50": round(float(np.median(ibtm_cost))),
      "y5_28_p50": round(float(np.median(y5_28)),3),
      "floor_paid_over_R_p1_p5_p50": [round(float(np.percentile(floor_paid/R,q)),4) for q in (1,5,50)],
      "floor_paid_minus_R_p5": round(float(np.percentile(floor_paid-R,5))),
      "VT_share_of_R_p50": round(float(np.median(B0/R)),4),
      "gift_below_top_median_gap": round(float(np.median((top-gift)[below]))),
    }
    out["laura_kept_2033"] = {'''),
]:
    assert src.count(old) == 1, old
    src = src.replace(old, new)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, str(m), "exec"), {"__name__": "__main__", "__file__": str(m)})
res = json.loads(tmp.read_text())
keys = ["ladder_cost_bootstrap_headline","ladder_headroom","ladder_headroom_bp","p_ladder_over_300k_on_1jan2027","stock_fund_2jan2028","floor_paid","range_2031","gift_2033","p_gift_inside_range","p_gift_at_top_within_1k","p_floor_holding_pays_below_bottom","p_shortfall_needs_gift_above_floor","floor_paid_vs_remainder","allocation_jan2028_typical","D1","ladder_delivery_if_rates_fall_and_stay"]
print(json.dumps({k: res[k] for k in keys}, indent=1))
