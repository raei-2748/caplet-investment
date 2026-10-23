"""M2 figures (called by m2_rate_paths.py). WS4, RAB Kit. AI-generated (Claude Code) for Team Caplet.

Colour-blind-safe palette (dataviz reference slots 1-3, validated all-pairs: CVD dE >= 9.2, normal-vision dE >= 24):
blue #2a78d6, orange #eb6834, aqua #1baf7a; text and reference marks in neutral greys. Every series is also
labelled in text, so identity never rests on colour alone.
"""
import os
from datetime import date

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb"
FOOT = "MODEL. Laura's plan (Nov-15 STRIPS basis), 28 Sep 2026 Treasury par curve. AI-generated (Claude Code), RAB Kit M2."


def style():
    plt.rcParams.update({
        "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
        "axes.edgecolor": GRID, "axes.linewidth": 1.0, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1.0,
        "grid.linestyle": "-", "axes.axisbelow": True, "axes.labelcolor": INK2, "xtick.color": INK2,
        "ytick.color": INK2, "text.color": INK, "font.size": 10, "axes.titlesize": 12, "axes.titleweight": "semibold",
        "axes.titlelocation": "left", "axes.spines.top": False, "axes.spines.right": False, "lines.linewidth": 2,
        "lines.solid_capstyle": "round", "legend.frameon": False})


def head(fig, title, sub, width=120):
    import textwrap
    fig.text(0.01, 0.975, title, fontsize=12.5, fontweight="semibold", color=INK, ha="left", va="top")
    fig.text(0.01, 0.925, "\n".join(textwrap.wrap(sub, width)), fontsize=8.3, color=INK2, ha="left", va="top")


def foot(fig, text=FOOT):
    fig.text(0.01, 0.01, text, fontsize=7.5, color=MUTED, ha="left", va="bottom")


def fig_estimators(res, out):
    rec = {r["row"].split()[0]: r for r in res["reconciliation"]["rows"] if r.get("P") is not None}
    est = res["estimators"]
    hd = res["headline"]
    rows = [("insight_v1 '1 in 3' basis (25 Sep curve, D1 method)", rec["R1"]["P"], None, None, "ref"),
            ("Same D1 method on the 28 Sep curve", rec["R2"]["P"], None, None, "ref")]
    names = {"E1": "E1 History, rescaled to today's volatility", "E2": "E2 History at similar yield levels",
             "E3": "E3 Vasicek one-factor model (statsmodels)", "E4": "E4 Three-factor curve model (PCA + VAR)",
             "E5": "E5 Options market (MOVE index)"}
    for e in est:
        rows.append((names[e["id"]], e["P_gap"], e.get("P_lo90"), e.get("P_hi90"), "est"))
    fig, ax = plt.subplots(figsize=(9.2, 4.9))
    ys = np.arange(len(rows))[::-1]
    lo, hi = hd["range"]
    ax.axvspan(100 * lo, 100 * hi, color=BLUE, alpha=0.10, lw=0)
    ax.axvline(100 * hd["P_gap"], color=BLUE, lw=2)
    ax.text(100 * lo - 0.8, -0.75, f"M2 headline {100 * hd['P_gap']:.0f}% = about 1 in "
            f"{hd['about_1_in']} (median of E1-E5)", color=INK, fontsize=8.5, va="center", ha="right")
    ax.set_ylim(-1.2, len(rows) - 0.5)
    for yv, (lab, p, l90, h90, kind) in zip(ys, rows):
        if l90 is not None:
            ax.plot([100 * l90, 100 * h90], [yv, yv], color=BLUE, lw=2, alpha=0.5)
        if kind == "ref":
            ax.plot(100 * p, yv, "o", ms=9, mfc=SURF, mec=MUTED, mew=2)
        else:
            ax.plot(100 * p, yv, "o", ms=9, color=BLUE, mec=SURF, mew=2)
        ax.text(100 * p + (2.2 if h90 is None else 100 * (h90 - p) + 1.2), yv, f"{100 * p:.0f}%", va="center",
                fontsize=9, color=INK)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9)
    ax.axhline(len(rows) - 2.5, color=GRID, lw=1)
    ax.set_xlim(0, 50)
    ax.set_xlabel("Chance the ten payments cost more than $300,000 on 1 Jan 2027 (%)")
    ax.grid(axis="y", visible=False)
    head(fig, "About 1 in 3: five methods agree within a few points",
         "Hollow: insight_v1's method (forward rates come true, 2026 volatility). Filled: the five M2 estimators, no "
         "view on rate direction. Bars: 90% bootstrap range (history estimators). Band: range of the five.")
    fig.subplots_adjust(left=0.40, right=0.97, top=0.82, bottom=0.14)
    foot(fig)
    fig.savefig(os.path.join(out, "m2_fig1_estimators.png"), dpi=200)
    plt.close(fig)


def fig_waterfall(res, out):
    wf = res["reconciliation"]["waterfall"]
    labels = ["insight_v1\n25 Sep curve", "Curve rose\nby 28 Sep", "No view on\nrate direction",
              "Today's rate\nvolatility (M2)"]
    ps = [100 * s["P"] for s in wf]
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    x = np.arange(4)
    ax.bar(x[0], ps[0], width=0.55, color=MUTED)
    ax.bar(x[3], ps[3], width=0.55, color=BLUE)
    for i in (1, 2):
        lo_, hi_ = sorted((ps[i - 1], ps[i]))
        ax.bar(x[i], hi_ - lo_, bottom=lo_, width=0.55, color=ORANGE if ps[i] > ps[i - 1] else AQUA)
    step3 = ps[3] - ps[2]
    for i in range(3):
        ax.plot([x[i] + 0.275, x[i + 1] - 0.275], [ps[i], ps[i]], color=MUTED, lw=1)
    txt = [f"{ps[0]:.0f}%", f"{ps[1] - ps[0]:+.0f} pts\n= {ps[1]:.0f}%", f"{ps[2] - ps[1]:+.0f} pts\n= {ps[2]:.0f}%",
           f"{step3:+.0f} pts\n= {ps[3]:.0f}%"]
    for i in range(4):
        top = max(ps[i], ps[i - 1] if i else 0)
        ax.text(x[i], top + 1.0, txt[i], ha="center", va="bottom", fontsize=9, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, 45)
    ax.set_ylabel("Chance of a shortfall on 1 Jan 2027 (%)")
    ax.grid(axis="x", visible=False)
    head(fig, "Why the answer is still about 1 in 3",
         f"Higher yields by 28 Sep gave more room ({ps[1] - ps[0]:+.0f} pts). Pricing with yields unchanged instead of "
         f"forward rates ({ps[2] - ps[1]:+.0f}) and using today's rate volatility instead of 2026's calm average "
         f"({step3:+.0f}) take it back.", width=110)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.8, bottom=0.2)
    foot(fig)
    fig.savefig(os.path.join(out, "m2_fig2_waterfall.png"), dpi=200)
    plt.close(fig)


def fig_cost(res, dists, out):
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    bins = np.arange(250, 346, 2.5)
    ax.axvspan(300, 345, color=MUTED, alpha=0.12, lw=0)
    peak = 0
    for key, col, lab in (("E1", BLUE, "E1 history, rescaled"),
                          ("E4", ORANGE, "E4 three-factor model")):
        c = dists[key] / 1000
        h, e = np.histogram(c, bins=bins, density=True)
        ax.plot(0.5 * (e[1:] + e[:-1]), h, color=col, lw=2, label=lab)
        peak = max(peak, h.max())
    ax.set_ylim(0, peak * 1.45)
    b = res["base"]
    for xv, col in ((300, INK), (b["cost_rw"] / 1000, INK2), (b["cost_fwd"] / 1000, MUTED)):
        ax.axvline(xv, color=col, lw=1)
    top = peak * 1.40
    ax.text(301, top, "$300,000 deposit:\npart of the 2033 payment\nwaits beyond this line", fontsize=8.3, color=INK,
            va="top")
    ax.text(b["cost_rw"] / 1000 + 0.5, top, f"yields\nunchanged\n${b['cost_rw'] / 1000:.1f}k", fontsize=8,
            color=INK2, va="top")
    ax.text(b["cost_fwd"] / 1000 - 0.5, top, f"forward\nrates\n${b['cost_fwd'] / 1000:.1f}k", fontsize=8,
            color=MUTED, ha="right", va="top")
    ax.set_xlim(255, 345)
    ax.set_yticks([])
    ax.set_xlabel("Cost of the ten payments on 1 Jan 2027 ($ thousand)")
    ax.legend(loc="upper left", fontsize=8.3)
    ax.grid(axis="y", visible=False)
    head(fig, "Where the January 2027 price could land",
         "Grey zone: $300,000 is not enough, so part of the earliest payment waits for the 2028 deposit.")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.84, bottom=0.15)
    foot(fig)
    fig.savefig(os.path.join(out, "m2_fig3_cost_distribution.png"), dpi=200)
    plt.close(fig)


def fig_history(res, dates, y, sig, vas_rows, out):
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.6, 6.4), sharex=True, gridspec_kw={"height_ratios": [1.2, 1]})
    t = np.array([d.year + (d.timetuple().tm_yday - 1) / 365.25 for d in dates])
    a1.plot(t, y, color=BLUE, lw=1.4)
    for v, first in zip(vas_rows, (1962, 1990, 2000)):
        a1.plot([first, 2026.75], [v["theta_pct"]] * 2, color=INK2, lw=1)
        a1.text(2027.9, v["theta_pct"] + {1962: 0.0, 1990: 0.35, 2000: -0.35}[first],
                f"fit from {first}: {v['theta_pct']:.1f}%", fontsize=8, color=INK2, va="center", clip_on=False)
    a1.plot(t[-1], y[-1], "o", ms=8, color=BLUE, mec=SURF, mew=2)
    a1.text(t[-1] - 0.4, y[-1] + 0.2, f"today {y[-1]:.2f}%", fontsize=8, ha="right", va="bottom", color=INK)
    a1.text(1996, 14.6, "Grey lines: the long-run 'normal' level a Vasicek model fits,\nwhich depends on the start "
            "year chosen (labels at right)", fontsize=8, color=INK2)
    a1.set_ylabel("Ladder yield (%)")
    head(fig, "History cannot say where 'normal' is, so M2 takes no view on direction",
         "Top: the ladder's own yield since 1962, with the long-run level a Vasicek model fits from three start years. "
         "Bottom: how jumpy that yield has been (EWMA), today and in the options market.")
    vol = sig * np.sqrt(252)
    a2.plot(t, vol, color=BLUE, lw=1.2)
    mv = res["move"]
    a2.axhline(res["panel"]["vol_all_bp_yr"], color=INK2, lw=1)
    a2.text(2027.9, res["panel"]["vol_all_bp_yr"], f"1962-2026\naverage {res['panel']['vol_all_bp_yr']:.0f}bp",
            fontsize=8, color=INK2, va="center", clip_on=False)
    a2.plot(t[-1], vol[-1], "o", ms=8, color=BLUE, mec=SURF, mew=2)
    a2.plot(t[-1], mv["sigma_bp_yr"], "o", ms=8, color=ORANGE, mec=SURF, mew=2)
    a2.text(t[-1] - 0.8, 250, f"options market (MOVE, orange dot) {mv['sigma_bp_yr']:.0f}bp\n"
            f"today from recent days (blue dot) {vol[-1]:.0f}bp", fontsize=8, ha="right", color=INK,
            bbox=dict(facecolor=SURF, edgecolor="none", alpha=0.9, pad=1))
    a2.set_ylim(0, 420)
    a2.set_ylabel("Volatility (bp a year)")
    a2.set_xlim(1962, 2027.5)
    fig.subplots_adjust(left=0.08, right=0.85, top=0.87, bottom=0.08, hspace=0.12)
    foot(fig, "Ladder yield = the single yield that prices the ten payments (same time to maturity as today). "
              "Volatility: EWMA of daily changes (0.97). MODEL. RAB Kit M2.")
    fig.savefig(os.path.join(out, "m2_fig4_history_level_and_volatility.png"), dpi=200)
    plt.close(fig)


def fig_fund(res, dist28, out):
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    for key, col, lab in (("H-FHS", BLUE, "history rescaled to today's volatility"),
                          ("H-LVL", ORANGE, "history at similar yield levels")):
        s = np.sort(dist28[key]) / 1000
        ax.plot(s, np.arange(1, len(s) + 1) / len(s) * 100, color=col, lw=2, label=lab)
    base = res["fifteen_months"]["base_fwd_fund"] / 1000
    ax.axvline(base, color=INK2, lw=1)
    ax.text(base + 0.8, 8, f"plan today ${base:.0f}k", fontsize=8.5, color=INK2)
    ax.axvline(20, color=MUTED, lw=1)
    ax.text(20.8, 60, "$20k", fontsize=8.5, color=MUTED)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Stock fund bought on 1 Jan 2028 ($ thousand)")
    ax.set_ylabel("Chance it is this size or smaller (%)")
    ax.legend(loc="lower right", fontsize=8.5)
    head(fig, "Rates to January 2028 move the stock fund, not the payments",
         "If rates fall first, part of the 2028 deposit completes the ladder and the floor costs more; if they rise, "
         "the fund grows. 15-month curve moves from history, 1963-2025 starts.")
    fig.subplots_adjust(left=0.1, right=0.98, top=0.84, bottom=0.15)
    foot(fig)
    fig.savefig(os.path.join(out, "m2_fig5_stock_fund_2028.png"), dpi=200)
    plt.close(fig)


def make_all(res, dists, dist28, dates, y, sig, vas_rows, out):
    style()
    fig_estimators(res, out)
    fig_waterfall(res, out)
    fig_cost(res, dists, out)
    fig_history(res, dates, y, sig, vas_rows, out)
    fig_fund(res, dist28, out)
