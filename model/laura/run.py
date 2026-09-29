"""Run every analysis used in decisions/ memos.

    python -m model.laura.run            # from the repo root

Writes:
    outputs/laura/results.json   machine-readable numbers (memos cite these keys)
    outputs/laura/tables.md      human-readable tables
    outputs/charts/laura/*.png   up to 5 charts
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

import numpy as np

from .engine import (T_STEPS, all_historical_windows, default_strategies, facility, historical_market,
                     liability_pv, load_config, run, simulate_market, sleeve_growth_quantiles, summarize)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "laura"
CHARTS = ROOT / "outputs" / "charts" / "laura"
K = 1000.0


def k(x):
    return f"${x / K:,.0f}k"


def liability_table(cfg):
    ys = [0.0, 0.02, 0.03, 0.035, 0.04, 0.045, 0.05, 0.0515, 0.055, 0.06]
    return [{"yield": y, "pv_2033": float(liability_pv(y, 2033, cfg)), "pv_2027": float(liability_pv(y, 2027, cfg))}
            for y in ys]


def strategy_grid(cfg, strategies):
    rows = []
    for scen in ["bear", "base", "bull"]:
        for regime, rho in cfg["equity"]["rho_regimes"].items():
            m = simulate_market(cfg, scen, rho)
            for key, s in strategies.items():
                o = summarize(run(m, s, cfg), cfg)
                o.update(scenario=scen, regime=regime, key=key)
                rows.append(o)
    return rows


NAMED = {1929: "Great Crash 1929-34", 1969: "Stagflation 1969-74", 2000: "Dot-com 2000-05",
         2003: "GFC hits in final year (2003-08)", 2017: "2022 hits in final year (2017-22)",
         1977: "Rates to 15% (1977-82)", 2007: "GFC first (2007-12)"}


def historical(cfg, strategies):
    wins = all_historical_windows(cfg)
    out = {}
    for key, s in strategies.items():
        surpl = np.array([run(m, s, cfg).surplus[0] for m in wins])
        starts = [int(m.label.split()[1].split("-")[0]) for m in wins]
        out[key] = {
            "n_windows": len(wins),
            "n_funded": int(np.sum(surpl >= -1e-6)),
            "worst_surplus": float(surpl.min()),
            "worst_window": starts[int(np.argmin(surpl))],
            "median_facility": float(np.median(facility(surpl, cfg))),
            "p10_facility": float(np.quantile(facility(surpl, cfg), 0.10)),
            "named": {NAMED[y]: float(surpl[starts.index(y)]) for y in NAMED if y in starts},
            "shortfall_windows": [starts[i] for i in np.where(surpl < -1e-6)[0]],
        }
    return out


def sensitivity(cfg, strategies):
    out = {}
    base_m = simulate_market(cfg, "base", 0.0)
    # 1. starting yield (Jan-2027 rates unknown today)
    out["y0"] = {}
    for y0 in [0.040, 0.045, 0.0515, 0.055]:
        m = simulate_market(cfg, "base", 0.0, y0=y0)
        out["y0"][f"{y0:.4f}"] = {key: summarize(run(m, s, cfg), cfg) for key, s in strategies.items()}
        out["y0"][f"{y0:.4f}"]["cost_to_lock_2027"] = float(liability_pv(y0, 2027, cfg))
    # 2. B: sleeve equity share and trigger
    for key in ("A", "B"):
        out[f"{key}_sleeve"] = {}
        for w in [0.6, 0.8, 1.0]:
            s = copy.deepcopy(strategies[key]); s.sleeve_equity = w
            out[f"{key}_sleeve"][str(w)] = summarize(run(base_m, s, cfg), cfg)
    bear_m = simulate_market(cfg, "bear", cfg["equity"]["rho_regimes"]["inflation_regime"])
    out["A_sleeve_bear"] = {}
    for w in [0.6, 0.8, 1.0]:
        s = copy.deepcopy(strategies["A"]); s.sleeve_equity = w
        out["A_sleeve_bear"][str(w)] = summarize(run(bear_m, s, cfg), cfg)
    out["B_trigger"] = {}
    for trig in [None, 1.15, 1.25, 1.35]:
        s = copy.deepcopy(strategies["B"]); s.lock_trigger = trig
        out["B_trigger"][str(trig)] = summarize(run(base_m, s, cfg), cfg)
    out["B_schedule"] = {}
    for name, sched in {"30->100": [0.3, 0.45, 0.6, 0.8, 1, 1], "50->100": [0.5, 0.6, 0.7, 0.8, 1, 1],
                        "70->100": [0.7, 0.8, 0.9, 1, 1, 1]}.items():
        s = copy.deepcopy(strategies["B"]); s.hedge_schedule = sched
        out["B_schedule"][name] = summarize(run(base_m, s, cfg), cfg)
    # 3. flexibility buffer (D5): facility amount vs buffer, strategy A (chosen in D1), base
    rA = run(base_m, strategies["A"], cfg)
    out["buffer"] = {str(b): {f"p{q}": float(np.quantile(facility(rA.surplus, cfg, b), q / 100)) for q in (10, 50, 90)}
                     for b in [0.0, 0.1, 0.2, 0.3, 0.4]}
    # 4. the $150k 2028 contribution (D8)
    out["contribution_2028"] = {}
    for label, contrib in {"as planned": {2027: 300000, 2028: 150000},
                           "half ($75k)": {2027: 300000, 2028: 75000},
                           "delayed to 2030": {2027: 300000, 2030: 150000},
                           "never arrives": {2027: 300000}}.items():
        c2 = copy.deepcopy(cfg); c2["client"]["contributions"] = contrib
        out["contribution_2028"][label] = {key: summarize(run(base_m, s, c2), c2)
                                           for key, s in strategies.items() if key in ("A", "B", "C60")}
    return out


def announce_tests(cfg, strategies, key="B"):
    """2031 'announce then protect' rule (D6)."""
    qs = cfg["policy"]["announce_quantiles"]
    B = strategies[key]
    out = {}
    hist_wins = all_historical_windows(cfg)
    for p in [0.0, 0.5, 0.7, 0.8, 0.9, 1.0]:
        gq = sleeve_growth_quantiles(cfg, B.sleeve_equity, qs)
        row = {"g_quantiles": gq.tolist()}
        for scen in ["bear", "base", "bull"]:
            for regime in ["inflation_regime", "growth_regime"]:
                m = simulate_market(cfg, scen, cfg["equity"]["rho_regimes"][regime])
                a = run(m, B, cfg, announce=True, lock_fraction=p, g_quantiles=gq).announce
                ok = a["surplus_2031"] > 0
                width = (a["high"] - a["low"])[ok]
                row[f"{scen}|{regime}"] = {
                    "p_in_range": float(a["in_range"][ok].mean()),
                    "p_at_or_above_low": float(a["at_or_above_low"][ok].mean()),
                    "median_low": float(np.median(a["low"][ok])),
                    "median_high": float(np.median(a["high"][ok])),
                    "median_width": float(np.median(width)),
                    "median_width_pct_of_mid": float(np.median(width / ((a["high"] + a["low"])[ok] / 2))),
                    "median_committed_min": float(np.median(a["committed_min"][ok])),
                    "p_at_or_above_committed": float(a["at_or_above_committed"][ok].mean()),
                    "p10_low": float(np.quantile(a["low"][ok], 0.10)),
                    "mean_facility": float(a["facility"][ok].mean()),
                    "p_two_tier_ok": float((a["at_or_above_committed"] & a["at_or_below_high"])[ok].mean()),
                }
        hits, above, two = [], [], []
        for m in hist_wins:
            a = run(m, B, cfg, announce=True, lock_fraction=p, g_quantiles=gq).announce
            if a["surplus_2031"][0] > 0:
                hits.append(bool(a["in_range"][0])); above.append(bool(a["at_or_above_low"][0]))
                two.append(bool(a["at_or_above_committed"][0] and a["at_or_below_high"][0]))
        row["history"] = {"n": len(hits), "p_in_range": float(np.mean(hits)), "p_at_or_above_low": float(np.mean(above)),
                          "p_two_tier_ok": float(np.mean(two))}
        out[str(p)] = row
    return out


def reserve_runoff(cfg, y=0.045):
    """2033-2042: ladder composition as payments are made (D3)."""
    rows = []
    for year in cfg["client"]["payment_years"]:
        remaining = [T for T in cfg["client"]["payment_years"] if T >= year]
        rows.append({"year": year, "payments_left": len(remaining), "ladder_value_start": float(liability_pv(y, year, cfg)),
                     "next_maturity": year, "longest_maturity": remaining[-1]})
    return rows


def fx_real(cfg, summary):
    infl = cfg["inflation"]
    f50 = summary["facility_2033_nominal"]["p50"]
    sh = cfg["policy"]["twd_shock"]
    return {"median_nominal_usd": f50,
            "median_2027_usd": f50 / (1 + infl["us_breakeven"]) ** 6,
            "median_in_2027_taiwan_facility_cost_terms": f50 / (1 + infl["taiwan_facility_cost_inflation"]) ** 6,
            "twd_purchasing_power_if_usd_weakens": f50 * (1 - sh),
            "twd_purchasing_power_if_usd_strengthens": f50 * (1 + sh)}


def charts(cfg, strategies, res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    CHARTS.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    col = {"A": "#1f4e79", "B": "#2e8b57", "C60": "#c0504d", "C80": "#e38b2c"}
    m = simulate_market(cfg, "base", 0.0)
    years = np.arange(2027, 2034)

    # 1. Funded-ratio fan: A vs C80
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    for key in ["A", "C80"]:
        r = run(m, strategies[key], cfg)
        fr = r.V / r.L
        lo, mid, hi = (np.quantile(fr, q, axis=0) for q in (0.05, 0.5, 0.95))
        ax.fill_between(years, lo, hi, color=col[key], alpha=0.15)
        ax.plot(years, mid, color=col[key], lw=2, label=f"{strategies[key].name}: median and 5-95% band")
        ax.plot(years, lo, color=col[key], lw=0.8, ls="--")
    ax.axhline(1.0, color="black", lw=1)
    ax.text(2029.2, 0.9, "Below this line the ten $50k payments are not fully covered", fontsize=8)
    ax.set_ylabel("Assets ÷ cost of the ten payments")
    ax.set_title("Locking the payments first keeps even bad outcomes above the line")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    fig.tight_layout(); fig.savefig(CHARTS / "01_funded_ratio_fan.png", dpi=160); plt.close(fig)

    # 2. Strategy comparison: certainty vs facility (base scenario, base regime)
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    for row in res["grid"]:
        if row["scenario"] == "base" and row["regime"] == "base":
            key = row["key"]; f = row["facility_2033_nominal"]
            ax.errorbar(row["p_funded"] * 100, f["p50"] / K,
                        yerr=[[(f["p50"] - f["p10"]) / K], [(f["p90"] - f["p50"]) / K]],
                        fmt="o", color=col[key], capsize=4, ms=8, label=strategies[key].name)
            ax.annotate(key, (row["p_funded"] * 100, f["p50"] / K), xytext=(-18 if key == "A" else 8, 4),
                        textcoords="offset points", fontsize=9, color=col[key], weight="bold")
    ax.set_xlabel("Probability the ten payments are fully funded (%)")
    ax.set_ylabel("2033 facility contribution ($k)\nmedian; bars = 10th-90th percentile")
    ax.set_title("More equity adds little to the median but a lot to the downside")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout(); fig.savefig(CHARTS / "02_strategy_comparison.png", dpi=160); plt.close(fig)

    # 3. Robustness to the 2028 contribution
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    cases = list(res["sensitivity"]["contribution_2028"].keys())
    x = np.arange(len(cases))
    for i, key in enumerate(["A", "B", "C60"]):
        vals = [res["sensitivity"]["contribution_2028"][c][key]["p_funded"] * 100 for c in cases]
        ax.bar(x + (i - 1) * 0.27, vals, 0.27, color=col[key], label=strategies[key].name)
    ax.set_xticks(x, cases); ax.set_ylim(40, 101)
    ax.set_ylabel("P(ten payments funded) %")
    ax.set_title("If the 2028 $150k is late or smaller, only 'lock early' still funds every payment")
    ax.legend(frameon=False, fontsize=8, loc="lower left")
    fig.tight_layout(); fig.savefig(CHARTS / "03_contribution_2028_robustness.png", dpi=160); plt.close(fig)

    # 4. Announce then protect (Strategy A): what Laura could tell co-sponsors in 2031 (median path)
    ann = res["announce"]["A"]
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ps = [p for p in sorted(ann.keys(), key=float) if float(p) in (0.0, 0.5, 0.7, 0.9)]
    for i, p in enumerate(ps):
        d = ann[p]["base|inflation_regime"]
        ax.plot([d["median_committed_min"] / K, d["median_low"] / K], [i, i], color=col["A"], lw=8, alpha=0.9,
                solid_capstyle="butt", label="Committed minimum -> low end" if i == 0 else None)
        ax.plot([d["median_low"] / K, d["median_high"] / K], [i, i], color="#9dc3e6", lw=8, solid_capstyle="butt",
                label="Announced 10-90% range" if i == 0 else None)
        ax.plot(d["mean_facility"] / K, i, "k|", ms=16, mew=2, label="Expected contribution" if i == 0 else None)
        ax.text(d["median_high"] / K + 3, i, f"\\${d['median_committed_min']/K:,.0f}k guaranteed, \\${d['median_low']/K:,.0f}-{d['median_high']/K:,.0f}k likely",
                va="center", fontsize=8)
    ax.set_yticks(range(len(ps)), [f"lock {float(p):.0%}" for p in ps])
    ax.set_xlim(0, 290); ax.set_xlabel("2033 facility contribution ($k), median 2031 outcome, strategy A")
    ax.set_title("Moving 2031 surplus into 2033 Treasuries turns a guess into a promise")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    fig.tight_layout(); fig.savefig(CHARTS / "04_announce_protect.png", dpi=160); plt.close(fig)

    # 5. Historical replay across all 93 windows
    wins = all_historical_windows(cfg)
    starts = [int(w.label.split()[1].split("-")[0]) for w in wins]
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    for key in ["A", "C80"]:
        s = [run(w, strategies[key], cfg).surplus[0] / K for w in wins]
        ax.plot(starts, s, color=col[key], lw=1.5, label=strategies[key].name)
    ax.axhline(0, color="black", lw=1)
    ax.set_xlabel("First year of the historical 6-year sequence replayed as 2027-2032")
    ax.set_ylabel("2033 surplus after buying\nthe reserve ($k)")
    ax.set_title("Replaying every 6-year stretch since 1928 on today's yields")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout(); fig.savefig(CHARTS / "05_historical_replay.png", dpi=160); plt.close(fig)


def write_tables(res, path):
    L = []
    L.append("# Laura Gao model: key tables\n")
    L.append("_Generated by `python -m model.laura.run`. Numbers in USD nominal unless stated._\n")
    L.append("## Liability: cost of the ten $50k payments\n\n| Flat yield | Needed at start 2033 | Needed at start 2027 |\n|---|---|---|")
    for r in res["liability"]:
        L.append(f"| {r['yield']:.2%} | {k(r['pv_2033'])} | {k(r['pv_2027'])} |")
    L.append("\n## Strategy comparison (20,000 simulated paths per cell)\n")
    L.append("| Scenario | Stock-bond regime | Strategy | P(funded) | Facility p10 | p50 | p90 |\n|---|---|---|---|---|---|---|")
    for r in res["grid"]:
        f = r["facility_2033_nominal"]
        L.append(f"| {r['scenario']} | {r['regime']} | {r['strategy']} | {r['p_funded']:.2%} | {k(f['p10'])} | {k(f['p50'])} | {k(f['p90'])} |")
    L.append("\n## Historical replay: every 6-year window 1928-2025 applied to today's yields\n")
    L.append("| Strategy | Windows funded | Worst surplus (window) | Median facility | Shortfall windows |\n|---|---|---|---|---|")
    for key, h in res["history"].items():
        L.append(f"| {key} | {h['n_funded']}/{h['n_windows']} | {k(h['worst_surplus'])} ({h['worst_window']}) | {k(h['median_facility'])} | {h['shortfall_windows']} |")
    L.append("\n### Named stresses: 2033 surplus over reserve cost\n\n| Window | " + " | ".join(res["history"]) + " |\n|---|" + "---|" * len(res["history"]))
    for name in next(iter(res["history"].values()))["named"]:
        L.append(f"| {name} | " + " | ".join(k(h["named"][name]) for h in res["history"].values()) + " |")
    L.append("\n## Sensitivity: starting yield in Jan 2027\n\n| y0 | Cost to lock in 2027 | A P(funded) / p50 | B P(funded) / p50 | C60 P(funded) / p50 |\n|---|---|---|---|---|")
    for y0, d in res["sensitivity"]["y0"].items():
        cells = [f"{d[s]['p_funded']:.1%} / {k(d[s]['facility_2033_nominal']['p50'])}" for s in ("A", "B", "C60")]
        L.append(f"| {float(y0):.2%} | {k(d['cost_to_lock_2027'])} | " + " | ".join(cells) + " |")
    for sec, title in [("A_sleeve", "A: equity share of growth sleeve (base)"), ("A_sleeve_bear", "A: equity share of growth sleeve (bear + inflation regime)"),
                       ("B_sleeve", "B: equity share of growth sleeve"), ("B_trigger", "B: early lock-in trigger"),
                       ("B_schedule", "B: hedge schedule")]:
        L.append(f"\n## {title}\n\n| Setting | P(funded) | Facility p10 | p50 | p90 |\n|---|---|---|---|---|")
        for key2, o in res["sensitivity"][sec].items():
            f = o["facility_2033_nominal"]
            L.append(f"| {key2} | {o['p_funded']:.2%} | {k(f['p10'])} | {k(f['p50'])} | {k(f['p90'])} |")
    L.append("\n## Flexibility buffer (A, base): facility contribution\n\n| Buffer kept | p10 | p50 | p90 |\n|---|---|---|---|")
    for b, d in res["sensitivity"]["buffer"].items():
        L.append(f"| {float(b):.0%} | {k(d['p10'])} | {k(d['p50'])} | {k(d['p90'])} |")
    L.append("\n## The 2028 $150k contribution\n\n| Case | A P(funded) / p50 | B P(funded) / p50 | C60 P(funded) / p50 |\n|---|---|---|---|")
    for lab, d in res["sensitivity"]["contribution_2028"].items():
        L.append(f"| {lab} | " + " | ".join(f"{d[s]['p_funded']:.1%} / {k(d[s]['facility_2033_nominal']['p50'])}" for s in ("A", "B", "C60")) + " |")
    for key, ann in res["announce"].items():
        L.append(f"\n## 2031 announce-then-protect (Strategy {key}; range = 10th-90th pct of team's base case)\n")
        L.append("| Share of surplus locked | Base median 10-90 range | Width (% of mid) | Median committed minimum (certain) | Base in-range | Bear+inflation ≥ low | History in-range | History ≥ low | Two-tier [committed, high]: base / bear / history | Mean facility (base) |\n|---|---|---|---|---|---|---|---|---|---|")
        for p, d in sorted(ann.items(), key=lambda x: float(x[0])):
            b = d["base|inflation_regime"]; br = d["bear|inflation_regime"]; h = d["history"]
            L.append(f"| {float(p):.0%} | {k(b['median_low'])}-{k(b['median_high'])} | {b['median_width_pct_of_mid']:.0%} | {k(b['median_committed_min'])} | {b['p_in_range']:.0%} | {br['p_at_or_above_low']:.0%} | {h['p_in_range']:.0%} (n={h['n']}) | {h['p_at_or_above_low']:.0%} | {b['p_two_tier_ok']:.0%} / {br['p_two_tier_ok']:.0%} / {h['p_two_tier_ok']:.0%} | {k(b['mean_facility'])} |")
    L.append("\n## Reserve run-off 2033-2042 (ladder at 4.5%)\n\n| Year | Payments left | Ladder value at start of year |\n|---|---|---|")
    for r in res["runoff"]:
        L.append(f"| {r['year']} | {r['payments_left']} | {k(r['ladder_value_start'])} |")
    fx = res["fx_real"]
    L.append(f"\n## Inflation and currency (A, base median facility)\n\n- Nominal 2033: {k(fx['median_nominal_usd'])}\n"
             f"- In 2027 US dollars (2.5% breakeven): {k(fx['median_2027_usd'])}\n"
             f"- In 2027 Taiwan facility-cost terms (2.5%): {k(fx['median_in_2027_taiwan_facility_cost_terms'])}\n"
             f"- If USD/TWD falls 15%: buys what {k(fx['twd_purchasing_power_if_usd_weakens'])} buys today; if it rises 15%: {k(fx['twd_purchasing_power_if_usd_strengthens'])}\n")
    path.write_text("\n".join(L))


def main():
    cfg = load_config()
    strategies = default_strategies(cfg)
    OUT.mkdir(parents=True, exist_ok=True)
    res = {"config": cfg, "strategies": {k_: vars(s) for k_, s in strategies.items()}}
    res["liability"] = liability_table(cfg)
    res["grid"] = strategy_grid(cfg, strategies)
    res["history"] = historical(cfg, strategies)
    res["sensitivity"] = sensitivity(cfg, strategies)
    res["announce"] = {key: announce_tests(cfg, strategies, key) for key in ("A", "B")}
    res["runoff"] = reserve_runoff(cfg)
    base_A = next(r for r in res["grid"] if r["key"] == "A" and r["scenario"] == "base" and r["regime"] == "base")
    res["fx_real"] = fx_real(cfg, base_A)
    (OUT / "results.json").write_text(json.dumps(res, indent=1, default=lambda o: list(o) if isinstance(o, tuple) else str(o)))
    write_tables(res, OUT / "tables.md")
    try:
        charts(cfg, strategies, res)
    except ImportError:
        print("matplotlib not installed; skipped charts")
    print(f"wrote {OUT/'results.json'}, {OUT/'tables.md'}, charts in {CHARTS}")


if __name__ == "__main__":
    main()
