"""FICTION (the room) + real work. Courtroom C-01 (Sun 25 Oct 2026): is D1's $10k buffer anything more than quoting
the 2031 bottom $10k lower? Same unchanged model and in-memory patch as LR-02 (22 Oct curve, 2027 LTCMA 7.5%), but
the buffer is paid for properly: it comes out of the 2028 remainder, so the floor holding, the quoted bottom and the
top all fall with it (LR-02 subtracted it from the gap only). MODEL. Run from repo root (~1-2 min)."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
m = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
tmp = HERE / "_c01_full.json"
src = m.read_text()
for old, new in [
    ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
     f'CURVE_CSV = pathlib.Path(r"{ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"}")'),
    ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
    ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
    ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
    ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', 'EQ_MU, EQ_VOL, VT_FEE = np.log(1.075), 0.1678, 0.0006'),
    ('    out["laura_kept_2033"] = {', '''    def stats(gift, bot, tp, kept):
        brk = gift < bot - 1e-6
        return {"p_gift_below_quoted_bottom": round(float(brk.mean()), 4),
                "median_break": round(float(np.median((bot - gift)[brk]))) if brk.any() else 0,
                "bottom_p50": round(float(np.median(bot))), "top_p50": round(float(np.median(tp))),
                "gift_p50": round(float(np.median(gift))), "gift_mean": round(float(gift.mean())),
                "laura_kept_p5": round(float(np.percentile(kept, 5))), "laura_kept_p50": round(float(np.median(kept))),
                "gift_plus_kept_mean": round(float((gift + kept).mean()))}
    C = {}
    gap = np.maximum(S33 - L33, 0)
    # d alone: payments come before the floor; only the quoted bottom moves
    for Q in (0, 5000, 10000):
        unc = np.maximum(gap - half, 0)
        raw = floor_paid + half - unc
        g = np.minimum(top, raw)
        kept = half + L33 - np.minimum(S33, L33 + half) + raw - g   # anything above the cap stays with Laura
        C[f"d_alone_quote_lower_{Q}"] = stats(g, bottom - Q, top, kept)
    # c + d: buffer B taken from the 2028 remainder, held flat, used first; floor, bottom and top fall with it
    for B in (5000, 10000):
        R2 = R - B
        fp2 = floor_paid * R2 / R
        bot2 = np.floor((R2 - 3700) / 5000) * 5000
        top2 = R2 + 0.5 * V31
        used_b = np.minimum(gap, B); unused = B - used_b
        unc = np.maximum(gap - B - half, 0)
        kept_base = half - np.minimum(np.maximum(gap - B, 0), half) + np.maximum(L33 - S33, 0)
        raw = fp2 + half - unc + unused                    # anything above the cap stays with Laura
        g_to_gift = np.minimum(top2, raw)
        C[f"c{B}_unused_to_gift"] = stats(g_to_gift, bot2, top2, kept_base + raw - g_to_gift)
        raw2 = fp2 + half - unc
        g_keep = np.minimum(top2, raw2)
        C[f"c{B}_unused_to_laura"] = stats(g_keep, bot2, top2, kept_base + unused + raw2 - g_keep)
    C["p_buffer_touched"] = round(float((gap > 0).mean()), 4)
    out["C01"] = C
    out["laura_kept_2033"] = {'''),
]:
    assert src.count(old) == 1, old
    src = src.replace(old, new)
exec(compile(src, str(m), "exec"), {"__name__": "__main__", "__file__": str(m)})
res = json.loads(tmp.read_text()); tmp.unlink()
(HERE / "C-01_results.json").write_text(json.dumps({"C01": res["C01"], "LR02": res.get("LR02")}, indent=1))
print(json.dumps(res["C01"], indent=1))
