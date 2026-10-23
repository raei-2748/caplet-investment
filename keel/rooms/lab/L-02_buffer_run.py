"""FICTION (the room) + real work. Lab L-02 and the SD-T03 reprice: re-run the unchanged IPS-number model
(keel/library/ips_numbers_2026-10/ips_numbers.py) on the 22 Oct 2026 curve, plus the buffer test lines.
The model file is not edited: this script patches its text in memory (curve file, curve date, output path) and
adds five output lines. MODEL. Run from the repo root: python3 keel/rooms/lab/L-02_buffer_run.py (~1-2 min).
Output: keel/rooms/lab/L-02_results_22oct.json (keys L02_buffer, L02_shortfall_pcts; the rest = the full model)."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
MODEL = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
OUT = pathlib.Path(__file__).resolve().parent / "L-02_results_22oct.json"

src = MODEL.read_text()
patches = [
    ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
     'CURVE_CSV = ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"'),
    ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
    ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
    ('(HERE / "results.json")', f'(pathlib.Path(r"{OUT}"))'),
    ('    out["laura_kept_2033"] = {',
     '''    out["L02_buffer"] = {}
    for B in (0, 5000, 10000, 15000, 20000, 25000):   # buffer held flat to 2033 (conservative)
        out["L02_buffer"][B] = {"p_total_need_exceeds_leftover_half_buffer": round(float((shortfall > L33 + half + B).mean()), 4),
                                "p_buffer_alone_short": round(float((shortfall > B).mean()), 4),
                                "p_needs_gift_above_floor": round(float((np.maximum(S33 - L33 - half - B, 0) > 0).mean()), 4)}
    out["L02_shortfall_pcts"] = {q: round(float(np.percentile(shortfall, q))) for q in (50, 80, 90, 95, 99)}
    out["laura_kept_2033"] = {'''),
]
for old, new in patches:
    assert src.count(old) == 1, old
    src = src.replace(old, new)
code = compile(src, str(MODEL), "exec")
exec(code, {"__name__": "__main__", "__file__": str(MODEL)})
