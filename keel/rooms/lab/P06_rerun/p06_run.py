"""FICTION (the room) + real work. Board card P06: re-run the four MODEL tail figures in the vote copy at the
J.P. Morgan 2027 LTCMA global-equity 7.5% (old: 2026 edition, AC World 7.00% compound), on the 22 Oct 2026 curve.
No model file is edited: each script's text is patched in memory (equity return only, plus the curve the 22 Oct runs
used), and both editions run with the same seeds, so the only difference is the return. MODEL.
Run from the repo root: python3 keel/rooms/lab/P06_rerun/p06_run.py  (a few minutes). Output: p06_results.json here."""
import contextlib, io, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
CURVE = ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"

def patched(path, patches):
    src = path.read_text()
    for old, new in patches:
        assert src.count(old) == 1, (path.name, old)
        src = src.replace(old, new)
    return src

def run(src, path, argv=None):
    g = {"__name__": "__main__", "__file__": str(path)}
    old_argv, buf = sys.argv, io.StringIO()
    sys.argv = [str(path)] + (argv or [])
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, str(path), "exec"), g)
    finally:
        sys.argv = old_argv
    return g, buf.getvalue()

out = {}
for ed, r in (("2026_7.0", "1.07"), ("2027_7.5", "1.075")):
    # 1) coupon miss and buffer (ips_numbers.py via the L-02 patches)
    m = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
    tmp = HERE / f"_ips_{ed}.json"
    src = patched(m, [
        ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"', f'CURVE_CSV = pathlib.Path(r"{CURVE}")'),
        ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
        ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
        ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
        ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', f'EQ_MU, EQ_VOL, VT_FEE = np.log({r}), 0.1678, 0.0006'),
        ('    out["laura_kept_2033"] = {',
         '''    out["L02_buffer"] = {}
    for B in (0, 10000, 15000):
        out["L02_buffer"][B] = round(float((shortfall > L33 + half + B).mean()), 4)
    out["laura_kept_2033"] = {'''),
    ])
    run(src, m)
    res = json.loads(tmp.read_text()); tmp.unlink()
    out.setdefault(ed, {})["ips_numbers"] = {k: res[k] for k in ("L02_buffer", "stock_fund_2jan2028", "range_2031", "gift_2033", "p_gift_inside_range") if k in res}
    # 2) quoted 2031 bottom (range_2031.py)
    m2 = ROOT / "keel/library/range_2031/range_2031.py"
    src2 = patched(m2, [('EQ_MU, EQ_VOL = 0.0700, 0.1678', f'EQ_MU, EQ_VOL = {float(r)-1:.4f}, 0.1678')])
    src2 = src2.replace('range_2031_results.csv', f'_p06_{ed}.csv')
    _, txt = run(src2, m2, [str(CURVE), "10/22/2026"])
    out[ed]["range_2031_stdout"] = txt
    (m2.parent / f"_p06_{ed}.csv").unlink(missing_ok=True)
    # 3) 29% below the 2031 top (L-07 rung 2)
    m3 = ROOT / "keel/rooms/lab/L-07_lunch_line/r2.py"
    src3 = patched(m3, [('mu = np.log(1.07) - 0.0006', f'mu = np.log({r}) - 0.0006')])
    _, txt3 = run(src3, m3)
    out[ed]["r2_A5A6"] = [l for l in txt3.splitlines() if "P(V33>=V31)" in l or "V31 median" in l]
(HERE / "p06_results.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "range_2031_stdout"} for k, v in out.items()}, indent=1))
