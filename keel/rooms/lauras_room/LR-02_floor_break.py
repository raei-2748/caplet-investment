"""FICTION (the room) + real work. Laura's Room LR-02 (Sun 25 Oct 2026): how often, and by how much, does the 2033
gift land BELOW the quoted 2031 bottom, i.e. the coupon gap eats past the half Laura keeps AND the contribution above
the floor (IPS v4 P5 names only those two steps)? And does a buffer from the 2028 deposit close it?
Unchanged model keel/library/ips_numbers_2026-10/ips_numbers.py, patched in memory exactly as P06 (22 Oct curve,
2027 LTCMA 7.5%), plus output lines. MODEL. Run from repo root (~1-2 min). Output: LR-02_results.json here."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
m = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
tmp = HERE / "_lr02_full.json"
src = m.read_text()
for old, new in [
    ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
     f'CURVE_CSV = pathlib.Path(r"{ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"}")'),
    ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
    ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
    ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
    ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', 'EQ_MU, EQ_VOL, VT_FEE = np.log(1.075), 0.1678, 0.0006'),
    ('    out["laura_kept_2033"] = {', '''    out["LR02"] = {}
    for B in (0, 5000, 10000):   # buffer held flat to 2033, used before Laura's half (conservative, as L-02)
        unc = np.maximum(S33 - L33 - B - half, 0)
        g = np.minimum(top, floor_paid + half - unc)
        brk = g < bottom - 1e-6
        out["LR02"][B] = {"p_gift_below_quoted_bottom": round(float(brk.mean()), 4),
                          "p_gap_reaches_floor_holding": round(float((unc > half).mean()), 4),
                          "median_break_when_it_happens": round(float(np.median((bottom - g)[brk]))) if brk.any() else 0,
                          "p95_break_when_it_happens": round(float(np.percentile((bottom - g)[brk], 95))) if brk.any() else 0,
                          "p_needs_gift_above_floor": round(float((unc > 0).mean()), 4)}
    brk0 = np.minimum(top, floor_paid + half - np.maximum(S33 - L33 - half, 0)) < bottom - 1e-6
    out["LR02_when_broken"] = {"median_S33": round(float(np.median(S33[brk0]))) if brk0.any() else 0,
                               "median_V33": round(float(np.median(V33[brk0]))) if brk0.any() else 0,
                               "median_V33_all": round(float(np.median(V33)))}
    out["laura_kept_2033"] = {'''),
]:
    assert src.count(old) == 1, old
    src = src.replace(old, new)
exec(compile(src, str(m), "exec"), {"__name__": "__main__", "__file__": str(m)})
res = json.loads(tmp.read_text()); tmp.unlink()
keep = {k: res[k] for k in ("LR02", "LR02_when_broken", "range_2031", "p_gift_inside_range", "L02_buffer") if k in res}
(HERE / "LR-02_results.json").write_text(json.dumps(keep, indent=1))
print(json.dumps(keep, indent=1))
