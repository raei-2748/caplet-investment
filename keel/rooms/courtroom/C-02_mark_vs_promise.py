"""FICTION (the room) + real work. Courtroom C-02 (Tue 27 Oct 2026): LR-04 on trial. Laura's Room says: don't pad
the 2031 bottom today, cut it in 2031 only by the coupon gap already visible ("variation margin"). Charge: a bottom
that can be cut is not the "promised minimum" of the locked TNA. This run asks the one question that settles it:
how often does the number the IPS can name today (the floor quoted at $145k) end up lower when Laura speaks in 2031?
Reuses LR-04's patch of the unchanged model (22 Oct curve, J.P. Morgan 2027 7.5% world stocks, 200,000 paths) and
adds three ways to apply the 2031 mark:
  A  LR-04 as written: bottom - (visible gap rounded UP to $5k)
  B  net the gap against the rounding first: floor-to-$5k of (floor remainder - $3,700 - visible gap)
  C  as B, but let the gap use the $3,700 too: floor-to-$5k of (floor remainder - visible gap)
MODEL. Run from repo root (~3-4 min). Output: C-02_results.json here."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
lr04 = ROOT / "keel/rooms/lauras_room/LR-04_price_of_a_margin.py"
src = lr04.read_text().split("\nkeep = ")[0]
ns = {"__file__": str(lr04), "__name__": "lr04"}
exec(compile(src, str(lr04), "exec"), ns)
ns["ADD"] += '''
    def rule(q):
        brk = gift < q - 1e-6
        return {"p_break": round(float(brk.mean()), 5), "n_break": int(brk.sum()),
                "p_quote_below_standard_bottom": round(float((q < bottom - 1e-6).mean()), 4),
                "p_quote_below_145k": round(float((q < 145000 - 1e-6).mean()), 4),
                "p_quote_below_140k": round(float((q < 140000 - 1e-6).mean()), 4),
                "mean_cut_vs_standard": round(float((bottom - q).mean())),
                "p99_cut_vs_standard": round(float(np.percentile(bottom - q, 99)))}
    slack = (R - 3700) - bottom
    out["LR04"]["C02"] = {
        "none": rule(bottom),
        "A_LR04": rule(bottom - vm),
        "B_net_rounding_first": rule(np.floor((R - 3700 - unc31) / 5000) * 5000),
        "C_net_rounding_and_3700": rule(np.floor((R - unc31) / 5000) * 5000),
        "p_standard_bottom_below_145k": round(float((bottom < 145000 - 1e-6).mean()), 4),
        "p_unc31_positive": round(float((unc31 > 0).mean()), 4),
        "p_unc31_exceeds_rounding_slack": round(float((unc31 > slack).mean()), 4),
        "unc31_when_positive_p50_p95": [round(float(np.percentile(unc31[unc31 > 0], q))) for q in (50, 95)] if (unc31 > 0).any() else [0, 0],
        "p_S31_positive": round(float((S31 > 0).mean()), 4),
        "p_floor_holding_below_quote_A": round(float((floor_paid < bottom - vm).mean()), 4),
    }'''
out = {f"mu={mu} rho={rho}": ns["run"](rho, mu)["LR04"]["C02"] for mu, rho in (("1.075", 0.0), ("1.065", 0.5))}
(HERE / "C-02_results.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
