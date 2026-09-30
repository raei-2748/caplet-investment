"""WS8: build the RAB Lab page (rab/page/index.html) from the committed model code and results.

RAB Kit, 30 Sep 2026 (Sydney). AI-generated research (Claude Code) for Team Caplet; not a competition submission.
The page is one self-contained HTML file: no server, no network data. Everything it shows is exported here:

  1. Range explorer: the first 20,000 of M3's 200,000 paths for the three decision models (T fat tails, BOOT history,
     BAYES uncertain mean), regenerated with M3's own generators and seed 20260930, plus M4's floor-delivery draws
     (phi) for the same path indices. Each model's annual log returns x are stored standardised,
     z = (x - model mean) / model sd, so the page can rescale them to the viewer's median return and volatility:
     x' = ln(1 + median) + vol * z. At the model's own settings the page reproduces M3/M4 on the subsample.
     The gift rule is ws2_common.rule / m4_cap.measures (announced low end $145,000), and a coupon shortfall
     follows m4_gap_owner.outcome mechanism C (WS3 rule 3: Laura's half first, then the gift above the floor,
     then the floor), with the gap scenarios from m4_gap_owner.gaps() (numbers.yaml reinvest.rung.*).
  2. Cost of certainty: rab/results/M5/cost_of_certainty_series.csv (PV of the ten $50,000 payments on each curve
     date), thinned to one point per week (per month before 1962), with the extreme days and 28 Sep 2026 kept.
  3. Friday tickets: rab/trades/tickets.csv (both books).
  4. Checks: the page's own JS (lab_core.js, run under node) must equal a numpy re-implementation on the same
     subsample, and the subsample must sit within Monte Carlo noise of the published 200,000-path figures.
     Results go to rab/page/page_check.txt.

Run from the worktree root (about 1 minute; no network):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/page/build_page.py
"""
from __future__ import annotations

import base64
import csv
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "rab" / "page"
sys.path.insert(0, str(ROOT / "rab" / "models"))
import ws2_common as C  # noqa: E402
import m3_branch as M3  # noqa: E402
import m4_cap as M4  # noqa: E402
import m4_gap_owner as GO  # noqa: E402

N_SUB = 20_000
MODELS = ["T", "BOOT", "BAYES"]
LABEL = {"T": "Fat tails", "BOOT": "History", "BAYES": "Uncertain mean"}
LONG = {"T": "Student-t with 4 degrees of freedom, centred on JPM's 7.00%",
        "BOOT": "Shiller 1871-2025 monthly returns, 24-month blocks, re-centred on 7.00%",
        "BAYES": "Student-t fitted to 1871-2025 with pymc; centre drawn around 7.00% (sd 1.5 points)"}
Z_SCALE, PHI_OFF, PHI_SCALE = 2000.0, 0.96, 1e6
A_LOW = GO.A            # $145,000 announced low end (M4 PR-3)
SCEN_LABEL = {"none (STRIPS basis, M4 as specified)": "Zero-coupon (STRIPS) ladder: nothing to reinvest",
              "Book L, curve forwards": "Book L, coupons earn the curve's forward rates",
              "Book L, today's yields": "Book L, coupons earn today's yields",
              "Book L, today's yields - 2 points": "Book L, coupons earn today's yields minus 2 points",
              "Book L, 2%": "Book L, coupons earn 2%"}


def b64(a: np.ndarray) -> str:
    return base64.b64encode(np.ascontiguousarray(a).astype("<" + a.dtype.str[1:]).tobytes()).decode()


def outcome_np(x, B0, F, phi, s, g31, r):
    """numpy twin of lab_core.js compute() (same rule, same mechanism C) for the check."""
    B3 = B0 * np.exp(x[:, :3].sum(1))
    B5 = B3 * np.exp(x[:, 3:].sum(1))
    if g31 == 0:
        U = F + s * B3
        G = np.minimum(phi * F + s * np.minimum(B5, B3), U)
        K = phi * F + B5 - G
        return B3, B5, U, G, K, np.zeros_like(B3, dtype=bool)
    G, K, U, low, _ = GO.outcome("C", B3, B5, phi, F, s, g31, r)
    return B3, B5, U, G, K, low


def summary_np(B3, B5, U, G, K, low, B0):
    return {"top_p50": float(np.median(U)), "top_p5": float(np.percentile(U, 5)),
            "top_p95": float(np.percentile(U, 95)), "gift_p5": float(np.percentile(G, 5)),
            "gift_p50": float(np.median(G)), "gift_p95": float(np.percentile(G, 95)), "gift_mean": float(G.mean()),
            "p_below_low": float(np.mean(G < A_LOW)), "p_top": float(np.mean(B5 >= B3)), "p_lowered": float(np.mean(low)),
            "p_keep10": float(np.mean(K >= 0.10 * G)), "kept_p5": float(np.percentile(K, 5)),
            "p_fund_down": float(np.mean(B3 < B0))}


def cost_series():
    s = pd.read_csv(ROOT / "rab/results/M5/cost_of_certainty_series.csv", parse_dates=["date"])
    s = s.sort_values("date").reset_index(drop=True)
    monthly = s[s["basis"] == "flat_shiller_gs10"]
    daily = s[s["basis"] != "flat_shiller_gs10"].copy()
    daily["wk"] = daily["date"].dt.strftime("%G-%V")
    weekly = daily.groupby("wk", sort=False).tail(1)
    keep = {int(s["V0"].idxmin()), int(s["V0"].idxmax()), len(s) - 1}
    out = pd.concat([monthly, weekly.drop(columns="wk"), s.loc[sorted(keep)]]).drop_duplicates("date")
    out = out.sort_values("date")
    m5 = json.load(open(ROOT / "rab/results/M5/M5_results.json"))["part_a"]
    ext = m5["extended"]
    return {"d": [d.strftime("%Y-%m-%d") for d in out["date"]], "v": [round(v / 100) for v in out["V0"]],
            "unit": "hundreds of USD", "today": {"date": "2026-09-28", "v": m5["today_V0"]},
            "min": {"date": ext["since_1962_daily"]["min_date"], "v": ext["since_1962_daily"]["min"]},
            "max": {"date": ext["since_1962_daily"]["max_date"], "v": ext["since_1962_daily"]["max"]},
            "y2020_median": m5["m1g_repro"]["y2020_median"],
            "last_as_cheap": m5["m1g_repro"]["last_date_at_or_below_today"],
            "share_months_le_today_1871": ext["since_1871"]["share_months_le_today"],
            "share_months_le_today_1962": ext["since_1962"]["share_months_le_today"],
            "flat_before": "1962-01-01", "n_points_source": int(len(s))}


def tickets():
    rows = list(csv.DictReader(open(ROOT / "rab/trades/tickets.csv")))
    keep = ["book", "seq", "id", "ticker", "type", "wins_name_expected", "wins_name_status", "serves", "qty",
            "qty_unit", "ref_price", "ref_asof", "max_price", "commission", "preview_expected", "cash_after_locked",
            "cash_after_worst", "x_of_2adv30", "yield_gap_bp", "yield_check", "trap", "alternate"]
    return [{k: r.get(k, "") for k in keep} for r in rows]


def main():
    inp = C.inputs()
    B0, F = inp["B0"], inp["F"]
    phi_full, _, _ = M4.phi_draws(inp["y5"])
    phi = phi_full[:N_SUB]
    summ = pd.read_csv(ROOT / "rab/results/M3/summary.csv").set_index("model")
    go = pd.read_csv(ROOT / "rab/results/M4/gap_owner.csv")
    go = go[go["build"] == "primary"]
    gaps = GO.gaps()
    data = {"meta": {"seed": C.SEED, "n_sub": N_SUB, "n_full": C.N_PATHS, "B0": B0, "F": F, "A": A_LOW,
                     "mu_default": C.MU_L, "median_default": C.JPM_COMPOUND, "numbers_sha": inp["numbers_sha"][:12],
                     "curve_date": inp["curve_date"], "z_scale": Z_SCALE, "phi_off": PHI_OFF,
                     "phi_scale": PHI_SCALE, "kappa": 0.10, "conf": 0.95, "s_adopted": C.S_ADOPTED},
            "models": {}, "scenarios": [], "published": {}, "check": {}}
    xs = {}
    for m in MODELS:
        x = M3.paths(m)                                  # full 200,000 so the stream matches M3 exactly
        mean, sd = float(x.mean()), float(x.std())
        assert abs(mean - summ.loc[m, "x_mean"]) < 1e-12 and abs(sd - summ.loc[m, "x_sd"]) < 1e-12
        xs[m] = x[:N_SUB]
        z = np.round((xs[m] - mean) / sd * Z_SCALE)
        assert np.abs(z).max() < 32767
        data["models"][m] = {"label": LABEL[m], "long": LONG[m], "mean": mean, "sd": sd,
                             "z": b64(z.astype(np.int16))}
    pq = np.round((phi - PHI_OFF) * PHI_SCALE)
    assert pq.min() >= 0 and pq.max() < 65535
    data["phi"] = b64(pq.astype(np.uint16))
    for name, v in gaps.items():
        if name not in SCEN_LABEL:
            continue
        data["scenarios"].append({"key": name, "label": SCEN_LABEL[name], "g31": v["g31"], "rate": v["rate"],
                                  "gap_sum": v["gap_sum"], "g33": v["g33"]})
    # Published 200,000-path figures at half (M3 summary for STRIPS; M4 gap_owner mechanism C for Book L)
    for m in MODELS:
        pub = {"top_p50": summ.loc[m, "U_p50"], "top_p5": summ.loc[m, "U_p5"], "top_p95": summ.loc[m, "U_p95"],
               "p_fund_down": summ.loc[m, "P_B3_below_B0"]}
        for _, r in go[go["model"] == m].iterrows():
            pub[r["scenario"]] = {"p_keep10": r["P_keep10_half_C"], "gift_mean": r["E_gift_half_C"],
                                  "kept_p5": r["kept_p5_half_C"], "p_below_low": r["P_gift_below_145k_half_C"],
                                  "top_p50": r["top_median_half_C"]}
        data["published"][m] = pub
    data["cost"] = cost_series()
    data["tickets"] = tickets()

    # ---------------- checks
    lines = ["RAB Lab page checks (rab/page/build_page.py)",
             f"  numbers.yaml sha256 {inp['numbers_sha'][:12]}; seed {C.SEED}; subsample first {N_SUB:,} of "
             f"{C.N_PATHS:,} paths per model; B0 ${B0:,.2f}; F ${F:,.0f}; announced low end ${A_LOW:,.0f}"]
    # (a) quantisation: rebuild x from z and phi from the stored ints, as the page does
    cases = []
    for m in MODELS:
        dm = data["models"][m]
        zq = np.frombuffer(base64.b64decode(dm["z"]), dtype="<i2").reshape(N_SUB, 5) / Z_SCALE
        xq = dm["mean"] + dm["sd"] * zq
        phq = np.frombuffer(base64.b64decode(data["phi"]), dtype="<u2") / PHI_SCALE + PHI_OFF
        for sc in data["scenarios"]:
            for s in (0.5, 1 / 3):
                exact = summary_np(*outcome_np(xs[m], B0, F, phi, s, sc["g31"], sc["rate"]), B0)
                quant = summary_np(*outcome_np(xq, B0, F, phq, s, sc["g31"], sc["rate"]), B0)
                cases.append({"model": m, "scenario": sc["key"], "s": s, "exact": exact, "quant": quant})
    worst_q = max(abs(c["exact"][k] - c["quant"][k]) for c in cases for k in c["exact"] if k.startswith(("top", "gift", "kept")))
    worst_qp = max(abs(c["exact"][k] - c["quant"][k]) for c in cases for k in c["exact"] if k.startswith("p_"))
    lines.append(f"  (a) storage rounding (int16 z/{Z_SCALE:.0f}, phi to 1e-6): largest dollar change ${worst_q:,.2f}, "
                 f"largest probability change {worst_qp * 100:.3f} points (over {len(cases)} model x scenario x share cases)")
    data["check"]["cases"] = [{"model": c["model"], "scenario": c["scenario"], "s": c["s"], "expect": c["quant"]}
                              for c in cases]
    # (b) subsample vs published 200,000 paths at half
    lines.append("  (b) subsample (20,000) vs published (200,000), share 1/2:")
    for m in MODELS:
        pub = data["published"][m]
        st = next(c["exact"] for c in cases if c["model"] == m and c["s"] == 0.5
                  and c["scenario"].startswith("none"))
        lines.append(f"      {m:5s} STRIPS: median top ${st['top_p50']:,.0f} vs ${pub['top_p50']:,.0f}; top p5 "
                     f"${st['top_p5']:,.0f} vs ${pub['top_p5']:,.0f}; p95 ${st['top_p95']:,.0f} vs ${pub['top_p95']:,.0f}; "
                     f"P(fund below cost 2031) {st['p_fund_down']:.1%} vs {pub['p_fund_down']:.1%}")
        for sc in data["scenarios"]:
            c = next(c["exact"] for c in cases if c["model"] == m and c["s"] == 0.5 and c["scenario"] == sc["key"])
            p = pub[sc["key"]]
            lines.append(f"      {m:5s} {sc['key'][:36]:36s}: P(keeps>=10%) {c['p_keep10']:.1%} vs {p['p_keep10']:.1%}; "
                         f"E gift ${c['gift_mean']:,.0f} vs ${p['gift_mean']:,.0f}; kept 1-in-20 ${c['kept_p5']:,.0f} vs "
                         f"${p['kept_p5']:,.0f}; P(gift<$145k) {c['p_below_low']:.2%} vs {p['p_below_low']:.2%}")
    # write data, inline into the template
    js_core = (PAGE / "lab_core.js").read_text()
    tpl = (PAGE / "template.html").read_text()
    blob = json.dumps(data, separators=(",", ":"), default=float)
    html = tpl.replace("/*__LAB_CORE__*/", js_core).replace("\"__LAB_DATA__\"", blob)
    assert "__LAB" not in html
    (PAGE / "lab_data.json").write_text(blob)
    (PAGE / "index.html").write_text(html)
    # (c) the page's own JS under node must equal the numpy twin on the stored data
    try:
        res = subprocess.run(["node", str(PAGE / "check_core.js")], capture_output=True, text=True, timeout=300)
        lines.append("  (c) " + (res.stdout.strip() or res.stderr.strip()))
        ok = res.returncode == 0
    except FileNotFoundError:
        lines.append("  (c) node not found: JS check NOT run")
        ok = False
    lines.append(f"  page {PAGE / 'index.html'} {len(html) / 1024:,.0f} KB")
    (PAGE / "page_check.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if not ok:
        raise SystemExit("JS check failed")


if __name__ == "__main__":
    main()
