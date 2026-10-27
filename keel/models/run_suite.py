"""AI-generated (Claude Code), Tue 27 Oct 2026. MODEL. Runs the whole Model Suite and writes results + charts.
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 LTCMA global equities 7.5% compound, 16.78% vol | 50,000 paths per world
       | history: Shiller monthly 1871-2023 (US stocks stand in for world stocks) | seeds in gens.py
Run from repo root: .venv/bin/python keel/models/run_suite.py      (numpy + matplotlib; about 3 minutes)
Writes keel/models/results/suite_results.json and keel/models/charts/*.png. Read README.md for what it all means.
"""
import json
import sys

import numpy as np

sys.path.insert(0, __import__("os").path.dirname(__file__))
import gens  # noqa: E402
import xr_core as x  # noqa: E402

N = 50_000
OUT = x.HERE / "results"; CH = x.HERE / "charts"
PLANS = ["balanced", "glide", "bucket", "immunise", "lock_late"]
NAMES = {"xr": "Caplet XR (V25)", "xr_trap": "Caplet XR + $10k coverage test",
         "xr_lock": "Caplet XR, lock + cushion", "balanced": "60/40 balanced",
         "glide": "Target-date glide", "bucket": "Three-year bucket", "immunise": "Bond-fund immunisation",
         "lock_late": "All stocks, lock in 2032"}
R = {"stamp": __doc__.split("STAMP: ")[1].split("\nRun")[0].replace("\n       ", " ")}


def worlds():
    return {"lognormal": gens.lognormal(N), "regime": gens.regime(N), "bootstrap": gens.bootstrap(N),
            "bootstrap_raw": gens.bootstrap(N, raw=True), "history": gens.history()}


def all_plans(p, band=0.20):
    out = {"xr": x.summary(x.caplet_xr(p), NAMES["xr"]), "xr_trap": x.summary(x.caplet_xr(p, trap=10_000), NAMES["xr_trap"]),
           "xr_lock": x.summary(x.caplet_xr(p, lock=True, cush=7_500), NAMES["xr_lock"])}
    for k in PLANS:
        out[k] = x.summary(x.rival(p, k, band=band), NAMES[k])
    return out


# ------------------------------------------------------------------ M1: the price of certainty, 1871-2026
def m1_price_of_certainty():
    h = gens.shiller(); d, y = list(h["date"]), list(h["y"])
    gd, gy = gens.gs10()
    for dd, yy in zip(gd, gy):
        if dd > d[-1]:
            d.append(dd); y.append(yy)
    y = np.array(y); c = x.flat_ladder_cost(y)
    today = float(x.COST_HEADLINE)
    dear = int(np.argmax(c)); cheap = int(np.argmin(c))
    by_decade = {}
    for dec in range(1870, 2030, 10):
        sel = [i for i, dd in enumerate(d) if int(dd[:4]) // 10 * 10 == dec]
        if sel:
            by_decade[str(dec)] = round(float((c[sel] <= x.DEP27).mean()), 2)
    return {"months": len(c), "from": d[0], "to": d[-1],
            "share_months_300k_buys_all_ten": round(float((c <= x.DEP27).mean()), 3),
            "share_months_450k_buys_all_ten": round(float((c <= x.DEP27 + x.DEP28).mean()), 3),
            "share_months_cheaper_than_today": round(float((c <= today).mean()), 3),
            "yield_needed_for_300k_pct": round(float(np.interp(-x.DEP27, -x.flat_ladder_cost(np.arange(0, 20, .01)),
                                                               np.arange(0, 20, .01))), 2),
            "dearest": {"month": d[dear], "yield": float(y[dear]), "cost": round(float(c[dear]))},
            "cheapest": {"month": d[cheap], "yield": float(y[cheap]), "cost": round(float(c[cheap]))},
            "cost_at_2020_low": round(float(x.flat_ladder_cost(min(y[[i for i, dd in enumerate(d) if dd.startswith("2020")]])))),
            "today_cost_bootstrap_22oct": round(today),
            "share_by_decade": by_decade, "_series": (d, y.tolist(), c.tolist())}


# ------------------------------------------------------------------ M1b + M7: every plan through history and four worlds
def m7_rivals(W):
    out = {}
    for name, p in W.items():
        out[name] = all_plans(p)
    out["regime_band40"] = {k: x.summary(x.rival(W["regime"], k, band=0.40), NAMES[k]) for k in PLANS}
    # sequence risk: of the histories where the 60/40 plan ran short, how many still had stocks beat bonds?
    seq = {}
    for name in ("history", "bootstrap_raw"):
        p = W[name]; o = x.rival(p, "balanced"); S = x.shift_path(p)
        bond = np.sum([np.log1p(x._fund_ret(S, m, *x.FUND["IEF"])) for m in range(180)], axis=0)
        stock = (p["eq"][:, :180] - x.VT_FEE / 12).sum(1)
        short = o["payments_short_amt"] > 1000
        if name == "history":
            seq["history_failing_start_years"] = sorted({p["start"][i][:4] for i in np.where(short)[0]})
        seq[name] = {"p_short": round(float(short.mean()), 4),
                     "share_of_shortfalls_where_stocks_beat_bonds": round(float((stock[short] > bond[short]).mean()), 3)
                     if short.any() else None,
                     "share_of_all_paths_stocks_beat_bonds": round(float((stock > bond).mean()), 3)}
    out["sequence_risk_6040"] = seq
    return out


def m1_named_histories():
    """Laura's plan and the 60/40 rival started in famous months (history's moves on today's curve) [A35]."""
    h = gens.history(); xr = x.caplet_xr(h); bal = x.rival(h, "balanced"); ll = x.rival(h, "lock_late")
    rows = {}
    for s in ("1873-01", "1907-01", "1929-01", "1937-01", "1966-01", "1973-01", "1987-01", "2000-01", "2007-06"):
        if s in h["start"]:
            i = h["start"].index(s)
            rows[s] = {"xr_gift": round(float(xr["gift"][i])), "xr_bottom": round(float(xr["bottom"][i])),
                       "xr_top": round(float(xr["top"][i])), "xr_payments_short": round(float(xr["payments_short_amt"][i])),
                       "6040_gift": round(float(bal["gift"][i])), "6040_bottom": round(float(bal["bottom"][i])),
                       "6040_payments_short": round(float(bal["payments_short_amt"][i])),
                       "lock_late_gift": round(float(ll["gift"][i])), "lock_late_payments_short": round(float(ll["payments_short_amt"][i]))}
    # the range window alone needs only six years, so starts run to mid-2017
    h6 = gens.history(horizon=72); o6 = x.caplet_xr(h6)
    rng = {"starts": len(h6["start"]), "from": h6["start"][0], "to": h6["start"][-1],
           "p_top_reached": round(float((o6["gift"] >= o6["top"] - 1000).mean()), 3),
           "p_below_bottom": round(float((o6["gift"] < o6["bottom"] - 1).mean()), 4),
           "worst_gift": round(float(o6["gift"].min())), "worst_start": h6["start"][int(np.argmin(o6["gift"]))],
           "gift_p50": round(float(np.median(o6["gift"])))}
    return {"named": rows, "range_window_history": rng,
            "_series": (h6["start"], o6["gift"].tolist(), o6["bottom"].tolist(), o6["top"].tolist())}


# ------------------------------------------------------------------ M2: fat tails and storms
def m2_tails(W):
    rp = gens.regime_params()
    out = {"fit": {"calm_monthly_mean": round(float(rp["mu"][0]), 4), "calm_monthly_sd": round(float(rp["sd"][0]), 4),
                   "storm_monthly_mean": round(float(rp["mu"][1]), 4), "storm_monthly_sd": round(float(rp["sd"][1]), 4),
                   "p_calm_to_storm": round(float(rp["P"][0, 1]), 4), "p_storm_to_calm": round(float(rp["P"][1, 0]), 4),
                   "storm_share_of_months": round(rp["storm_share"], 3),
                   "storm_avg_length_months": round(1 / float(rp["P"][1, 0]), 1),
                   "yield_drift_bp_per_month_calm_storm": [round(float(v) * 100, 1) for v in rp["dy_mu"]],
                   "student_t_df_calm_storm": [round(float(v), 1) for v in rp["nu"]]}}
    for name in ("lognormal", "regime", "bootstrap"):
        p = W[name]; o = x.caplet_xr(p); b = x.rival(p, "balanced")
        five = np.exp((p["eq"][:, 12:72]).sum(1) / 5) - 1
        out[name] = {"stocks_5y_worst_1in100_pa": round(float(np.percentile(five, 1)), 3),
                     "xr_gift_p1": round(x.pct(o["gift"], 1)), "xr_gift_p5": round(x.pct(o["gift"], 5)),
                     "xr_gift_p50": round(x.pct(o["gift"], 50)),
                     "xr_gift_p1_over_bottom": round(float(np.percentile(o["gift"] - o["bottom"], 1))),
                     "6040_gift_p1": round(x.pct(b["gift"], 1)), "6040_gift_p5": round(x.pct(b["gift"], 5)),
                     "6040_gift_p50": round(x.pct(b["gift"], 50)),
                     "xr_p_short": round(float((o["payments_short_amt"] > 1000).mean()), 4),
                     "6040_p_short": round(float((b["payments_short_amt"] > 1000).mean()), 4)}
    return out


# ------------------------------------------------------------------ M3: the January 2027 build under stress
def m3_build_stress():
    base = x.bootstrap_cost()
    shifted = lambda f: x.bootstrap_cost({t: v + f(t) for t, v in x.PAR.items()})
    par = {f"{bp:+d}bp": round(shifted(lambda t, b=bp: b / 100) - x.DEP27) for bp in (-200, -100, -50, -25, -10, 10, 25, 50, 100)}
    dv01 = (shifted(lambda t: -.01) - shifted(lambda t: .01)) / 2
    twists = {
        "bull steepener (2y -50, 10y -25, 30y 0)": lambda t: np.interp(t, [0, 2, 10, 30], [-.5, -.5, -.25, 0]),
        "bull flattener (2y 0, 10y -25, 30y -50)": lambda t: np.interp(t, [0, 2, 10, 30], [0, 0, -.25, -.5]),
        "bear steepener (2y 0, 10y +25, 30y +50)": lambda t: np.interp(t, [0, 2, 10, 30], [0, 0, .25, .5]),
        "belly rally (5-10y -40, ends 0)": lambda t: np.interp(t, [0, 2, 5, 10, 20, 30], [0, 0, -.4, -.4, 0, 0])}
    tw = {k: round(shifted(f) - base) for k, f in twists.items()}
    keyrate = {}
    for ten in (5, 7, 10, 20, 30):
        keyrate[f"{ten}y"] = round((x.bootstrap_cost({t: v - (.01 if t == ten else 0) for t, v in x.PAR.items()}) - base), 1)
    # history: how far did the 10-year yield move in the ~10 weeks before 1 Jan, 1953-2026?
    gd, gy = gens.gs10(); mv = gens.Y10 * (gy[2:] / gy[:-2] - 1)      # in proportion to today's 4.96% [A35]
    mv_abs = gy[2:] - gy[:-2]
    head_bp = (x.DEP27 - base) / dv01
    gap = lambda m: max(0.0, shifted(lambda t, mm=m: mm) - x.DEP27)
    p95 = float(np.percentile(mv, 5)); worst = float(mv.min())
    return {"cost_22oct": round(base), "headroom": round(x.DEP27 - base), "dv01_per_bp": round(dv01), "headroom_bp": round(head_bp, 1),
            "gap_or_room_after_parallel_move": par, "twists_cost_change": tw, "key_rate_dollars_per_bp_fall": keyrate,
            "history_2month_moves_1953_2026": {"n": int(len(mv)), "p_gap_opens": round(float((mv * 100 < -head_bp).mean()), 3),
                                               "one_in_20_fall_pp": round(p95, 2), "gap_at_one_in_20": round(gap(p95)),
                                               "worst_fall_pp": round(worst, 2), "worst_month": gd[int(np.argmin(mv)) + 2],
                                               "gap_at_worst": round(gap(worst)),
                                               "basis": "two-month GS10 moves scaled to today's 10-year level",
                                               "absolute_moves_one_in_20_pp": round(float(np.percentile(mv_abs, 5)), 2),
                                               "absolute_moves_gap_at_one_in_20": round(gap(float(np.percentile(mv_abs, 5))))},
            "v25_break_claim": {f"yields {f:+.1f}pp before the build": {"gap_the_2028_deposit_must_fill": round(gap(f)),
                                                                          "deposit_cut_that_breaks_a_cheque": f"{gap(f) / x.DEP28:.0%} of $150k left"}
                                for f in (-0.5, -1.0, -1.5, -2.0, -2.5, -3.0)},
            "_curve": (list(range(-300, 201, 10)), [shifted(lambda t, b=b: b / 100) for b in range(-300, 201, 10)])}


# ------------------------------------------------------------------ M4: inflation and the Taiwan dollar
def m4_inflation_fx(W):
    t = np.array(x.PAY_M) / 12
    def real(cpi):
        cum = np.cumsum(cpi, axis=1)
        return np.exp(-cum[:, np.array(x.PAY_M) - 1])                 # buying power of each cheque in 1 Jan 2027 dollars
    out = {}
    for name in ("lognormal", "bootstrap"):
        r = real(W[name]["cpi"])
        out[f"us_real_{name}"] = {"cheque1_p50": round(float(np.median(r[:, 0])), 3), "cheque10_p50": round(float(np.median(r[:, 9])), 3),
                                  "cheque10_p5": round(float(np.percentile(r[:, 9], 5)), 3),
                                  "cheque10_p95": round(float(np.percentile(r[:, 9], 95)), 3),
                                  "ten_cheques_real_total_p50": round(float(np.median(r.sum(1) * x.PAY)))}
    h = gens.shiller()
    for s in ("1941-01", "1966-01", "1973-01", "2007-06"):
        i = h["date"].index(s); c = h["cpi"][i:i + 180][None, :]
        c = np.pad(c, ((0, 0), (0, x.M - c.shape[1])))
        rr = real(c)[0]
        out[f"replay_{s}"] = {"cheque1": round(float(rr[0]), 3), "cheque10": round(float(rr[9]), 3),
                              "ten_cheques_real_total": round(float(rr.sum() * x.PAY))}
    # Taiwan: what each cheque buys on a Taiwan building site, relative to 1 Jan 2027 [A11] [A40]
    p = W["lognormal"]; o = x.caplet_xr(p)
    for drift in (False, True):
        fx = gens._fx_boot(np.random.default_rng(7), N, drift=drift)
        cumfx = np.exp(np.cumsum(fx, axis=1)[:, np.array(x.PAY_M) - 1])
        for pi in (0.02, 0.035):
            ratio = cumfx / (1 + pi) ** t
            topup = (x.PAY * np.maximum(1 / ratio - 1, 0) / 1.04 ** (t - 6)).sum(1)   # value on 1 Jan 2033 [A41]
            key = f"twd_{'drift' if drift else 'nodrift'}_tw{int(pi * 1000)}"
            out[key] = {"cheque10_p5": round(float(np.percentile(ratio[:, 9], 5)), 3),
                        "cheque10_p50": round(float(np.median(ratio[:, 9])), 3),
                        "cheque10_p95": round(float(np.percentile(ratio[:, 9], 95)), 3),
                        "topup_needed_2033_p50": round(float(np.median(topup))),
                        "topup_needed_2033_p95": round(float(np.percentile(topup, 95))),
                        "p_laura_kept_covers_topup": round(float((o["kept33"] >= topup).mean()), 3),
                        "p_kept_plus_above_bottom_covers_topup": round(float((o["kept33"] + np.maximum(o["gift"] - o["bottom"], 0) >= topup).mean()), 3)}
            if not drift and pi == 0.035:
                fan = np.percentile(ratio, [5, 25, 50, 75, 95], axis=0)
    _, fxs = gens.twd()
    out["twd_history"] = {"oct1983": float(fxs[0]), "sep2026": float(fxs[-1]),
                          "annual_vol": round(float(np.std(np.diff(np.log(fxs))) * np.sqrt(12)), 3),
                          "worst_10y_twd_rise_pct": round(float(np.min(fxs[120:] / fxs[:-120]) - 1) * 100, 1),
                          "worst_10y_twd_fall_pct": round(float(np.max(fxs[120:] / fxs[:-120]) - 1) * 100, 1)}
    out["_fan"] = fan.tolist()
    return out


# ------------------------------------------------------------------ M5: the 2028 deposit, $0 to $200k
def m5_deposit(W):
    out = {}
    for name in ("lognormal", "regime"):
        p = W[name]; rows = {}
        for d in range(0, 200_001, 12_500):
            o = x.caplet_xr(p, d28=float(d)); s = x.summary(o)
            ot = x.caplet_xr(p, d28=float(d), trap=10_000)
            rows[d] = {k: s[k] for k in ("p_payment_short", "gift_p5", "gift_p50", "gift_p95", "bottom_p50", "top_p50",
                                         "p_top_reached", "p_below_bottom")}
            rows[d]["p_ladder_unfilled"] = round(float((o["unfilled"] > 1).mean()), 4)
            rows[d]["p_payment_short_with_trap"] = round(float((ot["payments_short_amt"] > 1000).mean()), 4)
        out[name] = rows
    return out


# ------------------------------------------------------------------ M6: how high to set the 2031 top
def m6_range(W):
    out = {}
    h6 = gens.history(horizon=72)
    for name, p in (("lognormal", W["lognormal"]), ("regime", W["regime"]), ("history", h6)):
        rows = {}
        for k in (0.0, 0.25, 1 / 3, 0.5, 2 / 3, 0.75, 1.0):
            o = x.caplet_xr(p, top_share=k); g = o["gift"]; hit = g >= o["top"] - 1000
            short = np.maximum(o["top"] - g, 0)
            rows[f"{k:.2f}"] = {"p_top_reached": round(float(hit.mean()), 3), "top_p50": round(x.pct(o["top"], 50)),
                                "gift_p50": round(x.pct(g, 50)), "avg_miss_when_missed": round(float(short[~hit].mean())) if (~hit).any() else 0,
                                "odds_over_under": round(float(hit.mean() / max(1e-9, 1 - hit.mean())), 2)}
        out[name] = rows
    return out


# ------------------------------------------------------------------ charts
def charts(R, s1, s6, s3):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import datetime as dt
    INK, INK2, MUTE, GRID, SURF = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb"
    BLUE, ORANGE, AQUA, YELLOW, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#6250d6"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                         "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.color": GRID, "grid.linewidth": .6, "figure.facecolor": SURF,
                         "axes.facecolor": SURF, "savefig.facecolor": SURF})
    k = lambda v: f"${v / 1000:,.0f}k"
    fmtk = matplotlib.ticker.FuncFormatter(lambda v, _: k(v))

    def finish(fig, ax, title, sub, name):
        ax.set_title(title.replace("$", r"\$"), loc="left", fontsize=12.5, color=INK, fontweight="bold", pad=24)
        ax.text(0, 1.02, sub.replace("$", r"\$"), transform=ax.transAxes, fontsize=9, color=INK2, va="bottom")
        fig.text(.01, .01, "MODEL · Keel Model Suite · AI-generated (Claude Code), 27 Oct 2026 · " + R["stamp"].split("|")[0].strip(),
                 fontsize=7, color=MUTE)
        fig.tight_layout(rect=(0, .03, 1, 1)); fig.savefig(CH / name, dpi=150); plt.close(fig)

    # C1 the price of certainty
    d, y, c = s1
    dates = [dt.date(int(a[:4]), int(a[5:7]), 1) for a in d]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.plot(dates, c, color=BLUE, lw=1.6)
    ax.axhline(x.DEP27, color=ORANGE, lw=1.4, ls="--"); ax.text(dates[30], x.DEP27 * 1.03, "Laura's first $300,000", color=INK2, fontsize=9)
    ax.axhline(x.DEP27 + x.DEP28, color=MUTE, lw=1, ls=":"); ax.text(dates[30], (x.DEP27 + x.DEP28) * 1.03, "both deposits, $450,000", color=INK2, fontsize=9)
    ax.scatter([dates[-1]], [x.COST_HEADLINE], s=36, color=BLUE, zorder=5, edgecolor=SURF, lw=2)
    ax.annotate(f"Oct 2026: {k(x.COST_HEADLINE)}", (dates[-1], x.COST_HEADLINE), xytext=(-40, -70), textcoords="offset points", ha="right",
                fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=MUTE, lw=.8))
    ax.yaxis.set_major_formatter(fmtk); ax.set_ylim(100_000, 520_000)
    m1 = R["M1_price_of_certainty"]
    finish(fig, ax, "What Laura's ten cheques would have cost to buy outright, 1871-2026",
           f"Cost of ten $50,000 payments 6-15 years ahead at each month's 10-year Treasury yield. "
           f"$300,000 was enough in {m1['share_months_300k_buys_all_ten']:.0%} of months.", "c1_price_of_certainty.png")

    # C2 rivals: chance a promise breaks vs median gift, regime world
    reg = R["M7_rivals"]["regime"]
    order = ["xr_lock", "xr", "glide", "immunise", "lock_late", "bucket", "balanced"]
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    ys = np.arange(len(order))[::-1]
    br = [reg[o]["p_any_promise_broken"] for o in order]; gm = [reg[o]["gift_p50"] for o in order]
    col = [BLUE if o.startswith("xr") else ORANGE for o in order]
    axs[0].barh(ys, br, color=col, height=.55); axs[1].barh(ys, gm, color=col, height=.55)
    axs[0].set_yticks(ys, [NAMES[o] for o in order]); axs[0].xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1, 0))
    axs[1].xaxis.set_major_formatter(fmtk)
    for yy, v in zip(ys, br):
        axs[0].text(v + .005, yy, f"{v:.0%}" if v >= .01 else f"{v:.1%}", va="center", fontsize=9, color=INK)
    for yy, v in zip(ys, gm):
        axs[1].text(v + 3000, yy, k(v), va="center", fontsize=9, color=INK)
    axs[0].set_title("Chance a promise breaks", loc="left", fontsize=10, color=INK2)
    axs[1].set_title("Typical (median) facility gift, 2033", loc="left", fontsize=10, color=INK2)
    for a in axs:
        a.grid(axis="y", visible=False); a.tick_params(axis="y", length=0)
    axs[0].set_xlim(0, max(br) * 1.25); axs[1].set_xlim(0, max(gm) * 1.25)
    fig.suptitle("Two versions of our plan and five a rival team could file, in a world with market storms", x=.01, ha="left", fontsize=12.5,
                 fontweight="bold", color=INK)
    fig.text(.01, .9, "A promise breaks if a cheque comes up more than $1,000 short or the gift lands below the bottom of the 2031 range. 50,000 paths.",
             fontsize=9, color=INK2)
    fig.text(.01, .01, "MODEL · Keel Model Suite · AI-generated (Claude Code), 27 Oct 2026 · regime-switching model fitted to 1871-2023, level reset to 7.5%",
             fontsize=7, color=MUTE)
    fig.tight_layout(rect=(0, .03, 1, .88)); fig.savefig(CH / "c2_rivals.png", dpi=150); plt.close(fig)

    # C3 history: how far above its promised bottom the gift landed, every start month 1871-2017
    st, g, b, t = s6
    dates = [dt.date(int(a[:4]), int(a[5:7]), 1) for a in st]
    cush = np.array(g) - np.array(b)
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.fill_between(dates, 0, cush, color=BLUE, alpha=.16, lw=0); ax.plot(dates, cush, color=BLUE, lw=1.1)
    ax.axhline(0, color=ORANGE, lw=1.4, ls="--")
    ax.text(dates[10], 1500, "the promised bottom", fontsize=9, color=INK2, va="bottom")
    for s_, lab in (("1929-01", "1929"), ("1973-01", "1973"), ("2007-06", "2007")):
        if s_ in st:
            i = st.index(s_); ax.annotate(lab, (dates[i], cush[i]), xytext=(0, 38), textcoords="offset points", ha="center",
                                          fontsize=8.5, color=INK, arrowprops=dict(arrowstyle="-", color=MUTE, lw=.7))
    ax.yaxis.set_major_formatter(fmtk); ax.set_ylim(-8000, max(cush) * 1.15)
    rw = R["M1_named_histories"]["range_window_history"]
    finish(fig, ax, "If 2027 had started in any month since 1871: the gift never broke its promise",
           f"Gift minus the bottom named in 2031, for each of {rw['starts']:,} start months (history's moves on today's curve).",
           "c3_history_gift.png")

    # C4 deposit sweep
    dep = R["M5_deposit"]["lognormal"]; ds = sorted(int(v) for v in dep)
    fig, ax = plt.subplots(figsize=(9, 4.2))
    p5 = [dep[v]["gift_p5"] for v in ds]; p50 = [dep[v]["gift_p50"] for v in ds]; p95 = [dep[v]["gift_p95"] for v in ds]
    ax.fill_between(ds, p5, p95, color=BLUE, alpha=.16, lw=0); ax.plot(ds, p50, color=BLUE, lw=2)
    ax.plot(ds, [dep[v]["bottom_p50"] for v in ds], color=INK2, lw=1, ls="--")
    ax.text(ds[-1], p50[-1] + 6000, "median gift", ha="right", fontsize=9, color=INK)
    ax.text(ds[-1], dep[ds[-1]]["bottom_p50"] - 14000, "range bottom", ha="right", fontsize=9, color=INK2)
    ax.text(ds[0], 200_000, "shaded: 90% of outcomes", fontsize=9, color=INK2)
    ax.xaxis.set_major_formatter(fmtk); ax.yaxis.set_major_formatter(fmtk); ax.set_xlabel("Laura's 2028 deposit")
    finish(fig, ax, "If the 2028 deposit shrinks, the gift shrinks with it",
           "Facility gift in 2033 by the size of the 2028 deposit (house model, 50,000 paths per point). The cheques are paid first.",
           "c4_deposit_sweep.png")

    # C5 range frontier
    fig, ax = plt.subplots(figsize=(9, 4.2))
    for name, colr, lab in (("lognormal", BLUE, "house model"), ("regime", ORANGE, "fat tails + storms"), ("history", AQUA, "history since 1871")):
        rows = R["M6_range"][name]; ks = list(rows)
        xs = [rows[q]["top_p50"] for q in ks]; yv = [rows[q]["p_top_reached"] for q in ks]
        ax.plot(xs, yv, color=colr, lw=2, marker="o", ms=5, mec=SURF, mew=1.5, label=lab)
    ax.legend(frameon=False, loc="lower left", fontsize=9)
    rows = R["M6_range"]["lognormal"]
    for q, lab in (("0.00", "top = floor"), ("0.50", "V25: floor + half the stocks"), ("1.00", "floor + all the stocks")):
        ax.annotate(lab, (rows[q]["top_p50"], rows[q]["p_top_reached"]), xytext=(8, 10), textcoords="offset points", fontsize=8.5, color=INK2)
    ax.xaxis.set_major_formatter(fmtk); ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1, 0))
    ax.set_xlabel("Typical top of the 2031 range"); ax.set_ylabel("Chance the gift reaches the top")
    finish(fig, ax, "How high to set the top: every extra dollar promised costs odds",
           "Top of the range = floor + a share of the stock fund (0, 1/4, 1/3, 1/2, 2/3, 3/4, all). Same plan otherwise.", "c5_range_frontier.png")

    # C6 Taiwan fan
    fan = R["M4_inflation_fx"]["_fan"]; yrs_ = list(range(2033, 2043))
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.fill_between(yrs_, fan[0], fan[4], color=VIOLET, alpha=.12, lw=0)
    ax.fill_between(yrs_, fan[1], fan[3], color=VIOLET, alpha=.22, lw=0)
    ax.plot(yrs_, fan[2], color=VIOLET, lw=2)
    ax.axhline(1, color=MUTE, lw=1, ls=":")
    ax.text(2033, 1.02, "what $50,000 buys in Taiwan in Jan 2027", fontsize=9, color=INK2)
    ax.text(2042, fan[2][-1] - .04, "median", ha="right", fontsize=9, color=INK)
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1, 0)); ax.set_xticks(yrs_)
    finish(fig, ax, "Each $50,000 cheque, measured in Taiwan building costs",
           "Building costs +3.5% a year; Taiwan dollar moves resampled from 1983-2026. Bands: middle half and 90% of outcomes.",
           "c6_taiwan_cheque.png")

    # C7 January 2027 stress
    bps, costs = s3
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.plot(bps, costs, color=BLUE, lw=2); ax.axhline(x.DEP27, color=ORANGE, lw=1.4, ls="--")
    ax.text(bps[-1], x.DEP27 + 4000, "$300,000", ha="right", fontsize=9, color=INK2)
    m3 = R["M3_build_stress"]["history_2month_moves_1953_2026"]
    for v, lab in ((m3["one_in_20_fall_pp"] * 100, "1-in-20 fall"), (m3["worst_fall_pp"] * 100, f"worst ({m3['worst_month']})")):
        cy = float(np.interp(v, bps, costs)); ax.scatter([v], [cy], s=36, color=ORANGE, zorder=5, edgecolor=SURF, lw=2)
        ax.annotate(f"{lab}: {k(cy)}", (v, cy), xytext=(10, 6), textcoords="offset points", fontsize=8.5, color=INK)
    ax.yaxis.set_major_formatter(fmtk); ax.set_xlabel("Move in Treasury yields before 1 Jan 2027 (basis points)")
    finish(fig, ax, "The January 2027 build: what the ten cheques cost after a yield move",
           "Cost on the 22 Oct 2026 curve, moved in parallel. Above the dashed line, the 2028 deposit pays the difference.",
           "c7_jan2027_stress.png")


def strip(d):
    return {k: (strip(v) if isinstance(v, dict) else v) for k, v in d.items() if not str(k).startswith("_")}


if __name__ == "__main__":
    W = worlds(); print("worlds ready", flush=True)
    R["M1_price_of_certainty"] = m1_price_of_certainty(); print("M1", flush=True)
    R["M1_named_histories"] = m1_named_histories(); print("M1b", flush=True)
    R["M2_tails"] = m2_tails(W); print("M2", flush=True)
    R["M3_build_stress"] = m3_build_stress(); print("M3", flush=True)
    R["M4_inflation_fx"] = m4_inflation_fx(W); print("M4", flush=True)
    R["M5_deposit"] = m5_deposit(W); print("M5", flush=True)
    R["M6_range"] = m6_range(W); print("M6", flush=True)
    R["M7_rivals"] = m7_rivals(W); print("M7", flush=True)
    charts(R, R["M1_price_of_certainty"]["_series"], R["M1_named_histories"]["_series"], R["M3_build_stress"]["_curve"])
    (OUT / "suite_results.json").write_text(json.dumps(strip(R), indent=1, default=float))
    print(json.dumps(strip(R), indent=1, default=float))
