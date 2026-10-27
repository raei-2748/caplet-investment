"""FICTION (the room) + real work. Laura's Room LR-04 (Tue 27 Oct 2026): what does a safety margin under the quoted
2031 bottom (vote D1b) buy, and what does it cost? Two kinds of margin, named after a clearing house's two margins:
  - INITIAL margin: a fixed amount m knocked off the bottom in every path (D1b as decided 26 Oct).
  - VARIATION margin: in 2031, cut the bottom only by the coupon gap ALREADY VISIBLE then (ladder re-priced at 2031
    yields, shifts frozen from 1 Jan 2031), net of the 2027 leftover and half of the stock fund's 2031 value.
Same unchanged model as LR-02 (keel/library/ips_numbers_2026-10/ips_numbers.py, 22 Oct curve, 7.5% world stocks,
J.P. Morgan 2027), patched in memory; stocks and rates independent in this model (the Genius Lab's WO-R5 joint run
may move the tail). MODEL. Run from repo root (~1-2 min). Output: LR-04_results.json here.
Also run with the Genius Lab's joint shock (R05_joint.py: each year's stock shock correlated rho with that year's yield
change; rho > 0 = yields fall when stocks fall), rho 0 / 0.3 / 0.5, and at 6.5% stocks with rho 0.5."""
import json, pathlib, io, contextlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
m = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
ADD = '''    inside = (gift >= bottom - 1e-6)
    t31 = yrs(TODAY, dt.date(2031, 1, 1)); i31 = np.searchsorted(step_t, t31)
    sh31 = shifts.copy(); sh31[:, i31:] = shifts[:, [i31]]
    proj31 = np.zeros(N)
    for (py, (name, mat, cpn)) in RUNGS.items():
        T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27, YMIN)
        cc = (y0p if cpn is None else np.full(N, cpn)) / 100
        kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        ii = np.clip(np.searchsorted(step_t, kk + TOFF), 0, len(step_t) - 1)
        relf = sh31[:, ii] - s27[:, None]
        ykk = np.maximum(y0p[:, None] + relf, YMIN) / 100
        dd = 1 + (cc / 2) * ((1 + ykk / 2) ** (2 * (T - kk)[None, :])).sum(axis=1)
        db = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - kk)[None, :])).sum(axis=1)
        proj31 += PAY * dd / db
    S31 = np.maximum(10 * PAY - proj31, 0)
    unc31 = np.maximum(S31 - L33 - 0.5 * V31, 0)
    vm = np.ceil(unc31 / 5000) * 5000
    E = np.log(6) / np.log(6.7)          # elasticity read off List & Lucking-Reiley: seed x6.7 -> giving x~6
    def row(q):
        brk = gift < q - 1e-6
        cut = bottom - q
        return {"p_break": round(float(brk.mean()), 5), "n_break_of_N": f"{int(brk.sum())}/{N}",
                "median_break": round(float(np.median((q - gift)[brk]))) if brk.any() else 0,
                "mean_cut": round(float(cut.mean())), "p_cut_nonzero": round(float((cut > 0).mean()), 4),
                "p95_cut": round(float(np.percentile(cut, 95))),
                "cosponsor_cost_pct_E094": round(float((1 - (q / bottom) ** E).mean()) * 100, 2),
                "cosponsor_cost_pct_E05": round(float((1 - (q / bottom) ** 0.5).mean()) * 100, 2)}
    out["LR04"] = {"initial": {int(mm): row(bottom - mm) for mm in (0, 2500, 5000, 7500, 10000, 15000, 20000)},
                   "variation": {int(mm): row(bottom - vm - mm) for mm in (0, 2500, 5000)},
                   "variation_exact_no_roundup": row(bottom - unc31),
                   "variation_half_of_gap_only": row(bottom - np.ceil(0.5 * unc31 / 5000) * 5000),
                   "p_visible_gap_2031_over_1k": round(float((S31 > 1000).mean()), 4),
                   "p_gap_2033_over_1k": round(float((S33 > 1000).mean()), 4),
                   "corr_S31_S33": round(float(np.corrcoef(S31, S33)[0, 1]), 3),
                   "p_reach_top": round(float((gift >= top - 1).mean()), 4),
                   "p_reach_top_within_1k": round(float((gift >= top - 1000).mean()), 4),
                   "elasticity_E": round(float(E), 3)}'''
def run(rho, mu):
    tmp = HERE / f"_lr04_{rho}_{mu}.json"
    src = m.read_text()
    for old, new in [
        ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
         f'CURVE_CSV = pathlib.Path(r"{ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"}")'),
        ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
        ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
        ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
        ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', f'EQ_MU, EQ_VOL, VT_FEE = np.log({mu}), 0.1678, 0.0006'),
        ('    z = rng.normal(size=(N, 5))', f'''    _t0 = yrs(TODAY, T28)
    _dy = np.stack([sh(_t0 + j + 1) - sh(_t0 + j) for j in range(5)], axis=1) / RATE_VOL
    z = {rho} * _dy + np.sqrt(1 - {rho}**2) * rng.normal(size=(N, 5))'''),
        ('    inside = (gift >= bottom - 1e-6)', ADD),
    ]:
        assert src.count(old) == 1, old
        src = src.replace(old, new)
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, str(m), "exec"), {"__name__": "__main__", "__file__": str(m)})
    res = json.loads(tmp.read_text()); tmp.unlink()
    return {k: res[k] for k in ("LR04", "range_2031", "p_gift_inside_range") if k in res}

keep = {k: json.loads(json.dumps(v)) for k, v in {f"mu={mu} rho={rho}": run(rho, mu) for mu, rho in (("1.075", 0.0), ("1.075", 0.3), ("1.075", 0.5), ("1.065", 0.5))}.items()}
(HERE / "LR-04_results.json").write_text(json.dumps(keep, indent=1))
for k, v in keep.items():
    L = v["LR04"]
    print(k, "| none", L["initial"]["0"]["p_break"], "| $5k", L["initial"]["5000"]["p_break"], "| $10k", L["initial"]["10000"]["p_break"],
          "| MtM", L["variation"]["0"]["n_break_of_N"], L["variation"]["0"]["mean_cut"], L["variation"]["0"]["p_cut_nonzero"],
          L["variation"]["0"]["cosponsor_cost_pct_E094"], "| exact", L["variation_exact_no_roundup"]["n_break_of_N"],
          "| top", L["p_reach_top"], L["p_reach_top_within_1k"])
