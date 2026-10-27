"""AI-generated (Claude Code), the Lab (Jun), Tue 27 Oct 2026. Research run R07 (synergies), tests for Jun. MODEL.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 world stocks 7.5% compound, 16.78% vol | 100,000 paths
       per world (house seed 20261027, storms seed 20261028, deposit-noise seed 20261107) | history = Shiller 1871-2023
Run from repo root: python3 keel/ips_rewrite/lab/K07_synergy_tests.py [T1 T5 T2 T4 T8 T7]   (numpy; ~10 minutes)
Writes keel/ips_rewrite/lab/K07_results.json. Memo: K07_memo.md. Questions: research/R07_synergies/FUSIONS.md s.4-5.

Engine: the Model Suite (keel/models/xr_core.py + gens.py), imported unchanged. `xr_plus` below is a copy of
xr_core.caplet_xr with four switches added, and with the defaults it reproduces caplet_xr exactly (checked at start):
  d28 may be an array (one deposit per path)          T1, T7
  gshare = the gift's share of VT (V25: 0.5); with lock=True that share is what moves into Treasuries in Jan 2031
  top_share = the share of VT quoted in the top (default = gshare)                            T5
  holdback = Jan 2028 hold-back: the coupon gap projected at 2 Jan 2028 yields + `holdback` dollars, bought in an
             IBTM-like Treasury maturing Dec 2032 BEFORE the floor and VT; at 2033 it pays the set-aside first,
             and any excess joins Laura's side (standby)                                        T2
  remeasure = Jan 2031 re-measure: the bottom deducts the coupon gap projected at Jan 2031 yields (less what the
              hold-back will pay, if any) instead of A14's fixed $3,700                         T3
Conventions as the Suite [A01]-[A19]: "cheque short" = more than $1,000 short after Laura's kept stocks (A17);
"late gap over $1k" = true 2033-42 gap beyond the 2033 set-aside with no backstop (R10's convention);
"gap > kept" = that late gap is larger than what Laura kept on 1 Jan 2033 (K_overnight's 7.7% convention).
"""
import datetime as dt
import json
import pathlib
import sys
import time

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "keel/models"))
import gens  # noqa: E402
import xr_core as x  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "K07_results.json"
N = 100_000
SEED_HOUSE, SEED_STORM, SEED_DEP = 20261027, 20261028, 20261107
STAMP = ("MODEL | curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% compound, 16.78% vol | "
         f"{N:,} paths per world | seeds house {SEED_HOUSE}, storms {SEED_STORM}, deposit noise {SEED_DEP} | "
         "engine keel/models/xr_core.py (Model Suite) | history Shiller 1871-2023")
T_F = x.yrs(dt.date(2028, 1, 2), dt.date(2032, 12, 15))
T_L = x.yrs(dt.date(2031, 1, 1), dt.date(2032, 12, 15))
CUSH = 7_500.0


def slim(p):
    """Drop the inflation and FX arrays (unused here) to save memory."""
    return {k: v for k, v in p.items() if k in ("s0", "dy", "eq", "start")}


def house(n=N, seed=SEED_HOUSE, rho=0.0, haircut=0.0):
    p = slim(gens.lognormal(n, seed=seed, rho=rho))
    if haircut:
        p["eq"] = p["eq"] + (np.log(1 + x.EQ_G - haircut) - np.log(1 + x.EQ_G)) / 12
    return p


def storms(n=N, haircut=0.0):
    return slim(gens.regime(n, seed=SEED_STORM, target=x.EQ_G - haircut))


# ------------------------------------------------------------------------------------------ the engine
def xr_plus(p, d28=x.DEP28, lock=False, cush=0.0, gshare=0.5, top_share=None, holdback=None,
            remeasure=False, bottom_cut=3700.0, _cache=None):
    S = x.shift_path(p); N_ = S.shape[0]
    d28 = np.broadcast_to(np.asarray(d28, float), (N_,))
    cost27 = x.ladder_cost(p["s0"])
    gap27 = np.maximum(cost27 - x.DEP27, 0)
    L0 = np.maximum(x.DEP27 - cost27, 0)
    billg = np.cumprod(1 + np.maximum(x.curve(.25) + S[:, :-1], x.YMIN) / 1200, axis=1)
    L33 = L0 * billg[:, 71]
    unfilled = np.maximum(gap27 - d28, 0)
    R = np.maximum(d28 - gap27, 0)
    y_f = np.maximum(x.curve(T_F) + S[:, 12], x.YMIN)
    d, db = x._coupon_growth(y_f, y_f, S, 12, T_F, S[:, 12])
    disc_f = (1 + y_f / 200) ** (2 * T_F)                         # $1 on 2 Jan 2028 -> Dec 2032 at the build yield
    c = _cache if _cache is not None else {}
    if "deliv" not in c:
        c["deliv"] = x.ladder_delivery(S).sum(axis=1)
        c["proj33"] = x.ladder_delivery(S, freeze=72).sum(axis=1)
    short_true = np.maximum(10 * x.PAY - c["deliv"], 0)
    S33 = np.maximum(10 * x.PAY - c["proj33"], 0)
    # T2: the January 2028 hold-back, bought before the floor and VT
    if holdback is not None:
        if "proj28" not in c:
            c["proj28"] = x.ladder_delivery(S, freeze=12).sum(axis=1)
        G28 = np.maximum(10 * x.PAY - c["proj28"], 0)
        Hc = np.minimum((G28 + holdback) / disc_f, R)               # cost on 2 Jan 2028
        hb_target = Hc * disc_f                                     # what it pays in Dec 2032 at the build yield
        hb33 = Hc * disc_f * d / db                                 # what it really pays (its own coupons reinvested)
    else:
        G28 = np.zeros(N_); Hc = np.zeros(N_); hb_target = np.zeros(N_); hb33 = np.zeros(N_)
    Rp = R - Hc
    floor_paid = Rp * d / db
    B0 = Rp - Rp / disc_f
    eqc = np.cumsum(p["eq"] - x.VT_FEE / 12, axis=1)
    grow = lambda a, b: np.exp(eqc[:, b - 1] - eqc[:, a - 1])
    V31 = B0 * grow(12, 48); V33 = B0 * grow(12, 72)
    # T3: re-measure the coupon gap in January 2031 and deduct it before the range is named
    if remeasure:
        if "proj31" not in c:
            c["proj31"] = x.ladder_delivery(S, freeze=48).sum(axis=1)
        G31 = np.maximum(10 * x.PAY - c["proj31"], 0)
        cut = np.maximum(G31 - hb_target, 0)
    else:
        G31 = None; cut = bottom_cut
    bottom = np.maximum(np.floor((Rp - cut) / 5000) * 5000, 0)
    ts = gshare if top_share is None else top_share
    top = Rp + ts * V31
    laura_half = (1 - gshare) * V33
    if lock:
        gift_part = gshare * V31 * (1 + np.maximum(x.curve(T_L) + S[:, 48], x.YMIN) / 200) ** (2 * T_L)
    else:
        gift_part = gshare * V33
    side = L33 + laura_half + hb33
    base = floor_paid + gift_part
    room = np.maximum(np.minimum(top, base - np.maximum(S33 - side, 0)) - bottom, 0)
    A = S33 + (np.minimum(cush, np.maximum(side - S33, 0) + room) if cush else 0)
    uncovered = np.maximum(A - side, 0)
    raw = base - uncovered
    gift = np.clip(np.minimum(top, raw), 0, None)
    above_top = np.maximum(raw - top, 0)
    kept_side = np.maximum(side - A, 0)
    kept = kept_side + above_top
    extra = np.maximum(short_true - A, 0)
    kept42 = kept * grow(72, 180)
    miss_after = extra > kept42 + 1.0
    deficit = np.maximum(uncovered - base, 0)
    payments_short = (unfilled > 1) | (deficit > 1) | miss_after
    short_amt = np.where(payments_short, unfilled + deficit + np.maximum(extra - kept42, 0), 0)
    return {"cost27": cost27, "gap27": gap27, "unfilled": unfilled, "R": R, "Rp": Rp, "Hc": Hc, "G28": G28, "G31": G31,
            "hb33": hb33, "floor_paid": floor_paid, "B0": B0, "V31": V31, "V33": V33, "bottom": bottom, "top": top,
            "gift": gift, "S33": S33, "A": A, "short_true": short_true, "extra": extra, "kept_side": kept_side,
            "kept33": kept, "laura_2042": np.maximum(kept42 - extra, 0), "payments_short": payments_short,
            "payments_short_amt": short_amt, "L33": L33, "laura_half": laura_half}


def stats(o):
    g = o["gift"]; hit = g >= o["top"] - 1000; P = float(hit.mean())
    sa = o["payments_short_amt"]
    return {"p_cheque_short_over_1k": round(float((sa > 1000).mean()), 4),
            "p_ladder_unfilled_after_deposit": round(float((o["unfilled"] > 1000).mean()), 4),
            "p_late_gap_over_1k_no_backstop": round(float((o["extra"] > 1000).mean()), 4),
            "p_late_gap_exceeds_kept_2033": round(float((o["extra"] > o["kept_side"] + 1).mean()), 4),
            "p_total_coupon_gap_exceeds_kept_half_plus_cash": round(float((o["short_true"] > o["L33"] + o["laura_half"] + o["hb33"] + 1).mean()), 4),
            "p_gift_below_bottom": round(float((g < o["bottom"] - 1).mean()), 4),
            "p_top_reached": round(P, 4), "implied_k": round(P / max(1e-9, 1 - P), 2),
            "gift_p1_p5_p50_p95": [round(float(np.percentile(g, q))) for q in (1, 5, 50, 95)],
            "bottom_p50": round(float(np.median(o["bottom"]))), "top_p50": round(float(np.median(o["top"]))),
            "width_p50": round(float(np.median(o["top"] - o["bottom"]))),
            "laura_kept_2033_p50": round(float(np.median(o["kept33"]))),
            "laura_2042_p50": round(float(np.median(o["laura_2042"]))),
            "short_amt_p50_when_short": round(float(np.median(sa[sa > 1000]))) if (sa > 1000).any() else 0}


def save(key, val):
    R = json.loads(OUT.read_text()) if OUT.exists() else {}
    R["stamp"] = STAMP; R[key] = val
    OUT.write_text(json.dumps(R, indent=1))
    print(f"{key} saved ({time.strftime('%H:%M:%S')})", flush=True)


def selfcheck():
    p = house(20_000)
    a = x.caplet_xr(p); b = xr_plus(p)
    a2 = x.caplet_xr(p, lock=True, cush=CUSH); b2 = xr_plus(p, lock=True, cush=CUSH)
    ok = all(np.allclose(a[k], b[k]) for k in ("gift", "bottom", "top", "payments_short")) and \
        all(np.allclose(a2[k], b2[k]) for k in ("gift", "bottom", "top"))
    assert ok, "xr_plus does not reproduce xr_core.caplet_xr"
    return {"xr_plus_reproduces_caplet_xr_20k_paths": ok}


# ------------------------------------------------------------------------------------------ T1 joint storm
def deposit_factor(p, rho, sig, n):
    """f = min(1, exp(sig * (rho*m + sqrt(1-rho^2)*e))): the deposit can only shrink. m = the 2027 market factor:
    standardised sum of the 2027 stock return and the yield move from the curve date to 2 Jan 2028 (both low = bad)."""
    S = x.shift_path(p)
    ze = p["eq"][:, :12].sum(1); zy = S[:, 12]
    ze = (ze - ze.mean()) / ze.std(); zy = (zy - zy.mean()) / zy.std()
    m = ze + zy; m = (m - m.mean()) / m.std()
    e = np.random.default_rng(SEED_DEP).normal(size=n)
    return np.minimum(1.0, np.exp(sig * (rho * m + np.sqrt(1 - rho ** 2) * e)))


def t1():
    out = {"design": "Jan 2028 deposit = $150k x f, f = min(1, exp(sig*(rho*m + sqrt(1-rho^2)*e))), m = 2027 stocks + "
                     "yield move to Jan 2028 (standardised); rho also sets the stock-yield correlation in every month "
                     "(gens.lognormal rho). sig 0.35 base (1-in-20 bad year: deposit ~$84k), 0.50 sensitivity. "
                     "'fixed' = deposit $150k on the same paths.", "worlds": {}}
    for rho in (0.0, 0.5, 0.8):
        p = house(rho=rho); cache = {}; row = {}
        for plan, kw in (("V25", {}), ("champion_lock_G", {"lock": True, "cush": CUSH})):
            row[plan] = {"fixed_150k": stats(xr_plus(p, _cache=cache, **kw))}
            for sig in (0.35, 0.50):
                f = deposit_factor(p, rho, sig, N)
                o = xr_plus(p, d28=150_000 * f, _cache=cache, **kw)
                s = stats(o); s["deposit_p5_p50"] = [round(float(np.percentile(150_000 * f, q))) for q in (5, 50)]
                row[plan][f"linked_sig{sig}"] = s
        out["worlds"][f"rho={rho}"] = row
        del p, cache
    # the 2008 replay: yields -1.9pt by 1 Jan 2027, deposit -50%, stocks -40% in one year
    rep = {}
    for case, (crash_months, extra_dy) in {"A_crash_2027_before_deposit": (slice(0, 12), 0.0),
                                           "B_crash_2028_after_VT": (slice(12, 24), 0.0),
                                           "C_crash_2028_and_yields_fall_another_1.9pt_in_2028": (slice(12, 24), -1.9)}.items():
        p = house()
        p["s0"] = np.full(N, -1.9)
        p["eq"][:, crash_months] = np.log(0.6) / 12
        if extra_dy:
            p["dy"][:, 12:24] = extra_dy / 12
        rep[case] = {}
        for plan, kw in (("V25", {}), ("champion_lock_G", {"lock": True, "cush": CUSH})):
            o = xr_plus(p, d28=75_000.0, **kw); s = stats(o)
            s["ladder_cost_1jan2027"] = round(float(o["cost27"][0])); s["gap27"] = round(float(o["gap27"][0]))
            s["R_after_gap"] = round(float(o["R"][0]))
            s["coupon_gap_projected_2033_p50_p95"] = [round(float(np.percentile(o["S33"], q))) for q in (50, 95)]
            s["true_gap_p50_p95"] = [round(float(np.percentile(o["short_true"], q))) for q in (50, 95)]
            rep[case][plan] = s
        del p
    out["replay_2008"] = rep
    save("T1_joint_storm", out)


# ------------------------------------------------------------------------------------------ T5 implied ratio
def t5():
    out = {"note": "The 2031 lock is a Courtroom recommendation (28 Oct), NOT adopted in V25. Reported with and without.",
           "worlds": {}}
    W = {"house": house(), "storms": storms(), "history_2027_33_window": gens.history(horizon=72)}
    for name, p in W.items():
        cache = {}; row = {}
        row["V25_no_lock"] = stats(xr_plus(p, _cache=cache))
        row["lock_only"] = stats(xr_plus(p, lock=True, _cache=cache))
        row["champion_lock_G"] = stats(xr_plus(p, lock=True, cush=CUSH, _cache=cache))
        row["V25_plus_G_no_lock"] = stats(xr_plus(p, cush=CUSH, _cache=cache))
        # route 1: the gift owns (and locks) a bigger share s of VT, top = R + s*V31
        r1 = {}
        for s in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
            st = stats(xr_plus(p, lock=True, cush=CUSH, gshare=s, _cache=cache))
            r1[f"{s:.2f}"] = {k: st[k] for k in ("p_top_reached", "implied_k", "p_gift_below_bottom", "p_cheque_short_over_1k",
                                                 "top_p50", "gift_p1_p5_p50_p95", "laura_kept_2033_p50")}
        row["route1_lock_bigger_gift_share"] = r1
        # route 2: the gift owns and locks half, but the top quotes c x V31 (c > 0.5 counts on the lock's interest)
        r2 = {}
        for c_ in (0.50, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.58, 0.60):
            st = stats(xr_plus(p, lock=True, cush=CUSH, top_share=c_, _cache=cache))
            r2[f"{c_:.2f}"] = {k: st[k] for k in ("p_top_reached", "implied_k", "top_p50", "gift_p1_p5_p50_p95")}
        row["route2_lock_half_quote_more"] = r2
        # same top-share sweep without the lock (as M6) for comparison
        row["no_lock_top_share_0.50_0.55"] = {f"{c_:.2f}": stats(xr_plus(p, top_share=c_, _cache=cache))["p_top_reached"]
                                              for c_ in (0.50, 0.55)}
        out["worlds"][name] = row
    save("T5_implied_ratio", out)


# ------------------------------------------------------------------------------------------ T2 + T3 side by side
def t2_t3():
    out = {"design": "Same paths for every column. hold-back = coupon gap projected at 2 Jan 2028 yields + $7,500, bought "
                     "in an IBTM-like Treasury maturing Dec 2032 before the floor and VT (bottom keeps A14's $3,700 cut). "
                     "re-measure = bottom deducts the gap projected at Jan 2031 yields (less what the hold-back will pay) "
                     "instead of $3,700. Base plans: V25 (no lock, no cushion) and the champion (lock + rule G). "
                     "Worlds: house rho 0; joint storm rho 0.8 with the linked deposit (sig 0.35); storms.",
           "worlds": {}}
    worlds = {"house_rho0": (lambda: house(), None), "joint_storm_rho0.8_linked_deposit": (lambda: house(rho=0.8), 0.8),
              "storms": (lambda: storms(), None)}
    for name, (mk, rho) in worlds.items():
        p = mk(); cache = {}
        d28 = 150_000 * deposit_factor(p, rho, 0.35, N) if rho is not None else x.DEP28
        row = {}
        for base, kw in (("V25", {}), ("champion_lock_G", {"lock": True, "cush": CUSH})):
            r = {}
            for var, extra in (("base", {}), ("T2_holdback_2028", {"holdback": CUSH}),
                               ("T3_remeasure_2031", {"remeasure": True}),
                               ("T2+T3_combined", {"holdback": CUSH, "remeasure": True})):
                o = xr_plus(p, d28=d28, _cache=cache, **kw, **extra); s = stats(o)
                if "holdback" in extra:
                    s["holdback_cost_2028_p50_p95"] = [round(float(np.percentile(o["Hc"], q))) for q in (50, 95)]
                    s["p_holdback_covers_2033_setaside"] = round(float((o["hb33"] >= o["A"] - 1).mean()), 4)
                if extra.get("remeasure"):
                    s["gap_projected_2031_p50_p95"] = [round(float(np.percentile(o["G31"], q))) for q in (50, 95)]
                r[var] = s
            row[base] = r
        out["worlds"][name] = row
        del p, cache
    save("T2_T3_holdback_and_remeasure", out)


# ------------------------------------------------------------------------------------------ T4 survivorship haircut
def t4():
    out = {"design": "Equity median 7.5% less 0.6pt (6.9%) and less 2.0pt (5.5%), vol unchanged; house and storm worlds; "
                     "history = raw Shiller US paths with the same haircut subtracted from every month.", "worlds": {}}
    for h in (0.0, 0.006, 0.020):
        for name, mk in (("house", lambda: house(haircut=h)), ("storms", lambda: storms(haircut=h))):
            p = mk(); cache = {}; row = {}
            for plan, kw in (("V25", {}), ("champion_lock_G", {"lock": True, "cush": CUSH})):
                row[plan] = stats(xr_plus(p, _cache=cache, **kw))
            for k in ("balanced", "glide", "bucket", "immunise", "lock_late"):
                s = x.summary(x.rival(p, k))
                row[k] = {kk: s[kk] for kk in ("p_payment_short", "p_below_bottom", "p_any_promise_broken", "gift_p50")}
            out["worlds"][f"{name}_less_{h * 100:.1f}pt"] = row
            del p, cache
        # history (US-only): M1b / M6 window and M7 history rows with the haircut
        hh = gens.history(); h6 = gens.history(horizon=72)
        for q in (hh, h6):
            q["eq"] = q["eq"] - h / 12
        row = {}
        o6 = xr_plus(h6); s6 = stats(o6)
        row["V25_2027_33_window"] = {k: s6[k] for k in ("p_top_reached", "implied_k", "p_gift_below_bottom")}
        o6c = xr_plus(h6, lock=True, cush=CUSH); s6c = stats(o6c)
        row["champion_2027_33_window"] = {k: s6c[k] for k in ("p_top_reached", "implied_k", "p_gift_below_bottom")}
        for plan, kw in (("V25", {}), ("champion_lock_G", {"lock": True, "cush": CUSH})):
            s = stats(xr_plus(hh, **kw)); row[plan + "_full"] = {k: s[k] for k in ("p_cheque_short_over_1k", "p_gift_below_bottom", "p_top_reached")}
        for k in ("balanced", "glide", "bucket", "immunise", "lock_late"):
            s = x.summary(x.rival(hh, k))
            row[k] = {kk: s[kk] for kk in ("p_payment_short", "p_below_bottom", "p_any_promise_broken")}
        out["worlds"][f"history_raw_less_{h * 100:.1f}pt"] = row
    out["history_world_figures_resting_on_US_only_data_A07"] = [
        "M1b: 0 broken promises in 1,756 historical starts; closest call 1928-29 start ($8,400 V25 / $3,100 champion above the bottom)",
        "M1b/M6: top reached 84% (V25) and 97% (champion) in history; 'odds 5:1 (history)' at the V25 top",
        "M7 history rows: rivals break a promise 22-36% (history column), lock-late median gift $305k, 60/40 Laura 2042 $285k",
        "M7 sequence-risk share (stocks beat bonds in failing 60/40 paths), history and bootstrap_raw",
        "M8: the January 1923 start (stocks ~7% a year for 15 years, 60/40 bounces 1937 and 1938)",
        "Every 'bootstrap_raw' figure (raw 9.2% US median)",
        "Not equity-dependent, so survivorship does not apply: M1 price of certainty (US 10-year yields), M3 build stress (GS10 moves)"]
    save("T4_survivorship_haircut", out)


# ------------------------------------------------------------------------------------------ T8 the short rung
def t8():
    p = house(); S = x.shift_path(p); s0 = p["s0"]
    T27 = x.PAY_T                                                          # 6..15 years from 1 Jan 2027
    anchor = x.COST_HEADLINE / (x.PAY * ((1 + x.curve(T27) / 200) ** (-2 * T27)).sum())
    z27 = np.maximum(x.curve(T27)[None, :] + s0[:, None], x.YMIN)
    c27 = x.PAY * (1 + z27 / 200) ** (-2 * T27) * anchor                   # cost of each rung on 1 Jan 2027 (N, 10)
    cost = c27.sum(1); gap = np.maximum(cost - x.DEP27, 0); sh = gap > 0
    T28 = T27 - 1.0
    z28 = np.maximum(x.curve(T28)[None, :] + S[:, [12]], x.YMIN)
    c28 = x.PAY * (1 + z28 / 200) ** (-2 * T28) * anchor                   # same rung on 2 Jan 2028
    bill27 = np.maximum(x.curve(1.0) + s0, x.YMIN) / 100

    def order(idx):                                                       # buy rungs in this order with $300k
        money = np.full(len(s0), x.DEP27); frac_missing = np.zeros_like(c27)
        for j in idx:
            buy = np.minimum(money, c27[:, j]); money -= buy
            frac_missing[:, j] = 1 - buy / c27[:, j]
        cost28 = (frac_missing * c28).sum(1)
        n_short = (frac_missing > 1e-9).sum(1)
        return frac_missing, cost28, n_short

    res = {"p_ladder_over_300k": round(float(sh.mean()), 4),
           "gap_p50_p95_when_short": [round(float(np.percentile(gap[sh], q))) for q in (50, 95)],
           "rung_cost_1jan2027_at_curve": {str(2033 + j): round(float(x.PAY * (1 + x.curve(T27[j]) / 200) ** (-2 * T27[j]) * anchor)) for j in range(10)}}
    for nm, idx in (("longest_first", list(range(9, -1, -1))), ("shortest_first", list(range(10)))):
        fm, c28t, ns = order(idx)
        short_rungs = {str(2033 + j): round(float((fm[sh, j] > 1e-9).mean()), 4) for j in range(10) if (fm[sh, j] > 1e-9).any()}
        extra = c28t[sh] - gap[sh]
        extra_vs_bill = c28t[sh] - gap[sh] * (1 + bill27[sh])
        res[nm] = {"share_of_short_paths_where_rung_is_short": short_rungs,
                   "p_two_or_more_rungs_short_when_short": round(float((ns[sh] >= 2).mean()), 4),
                   "missing_payment_dollars_p50": round(float(np.median((fm[sh] * x.PAY).sum(1)))),
                   "cost_jan2028_p50_p95": [round(float(np.percentile(c28t[sh], q))) for q in (50, 95)],
                   "extra_vs_2027_gap_p5_p50_p95": [round(float(np.percentile(extra, q))) for q in (5, 50, 95)],
                   "extra_vs_gap_plus_a_year_of_1y_interest_p5_p50_p95": [round(float(np.percentile(extra_vs_bill, q))) for q in (5, 50, 95)]}
    res["note"] = ("xr_core fills the gap in 2028 at its 2027 price (R = deposit - gap). 'extra' = what the missing part "
                   "really costs on 2 Jan 2028 minus that. The second line removes a year's interest, leaving only the "
                   "re-pricing from 2027 yield moves.")
    save("T8_short_rung", res)


# ------------------------------------------------------------------------------------------ T7 deposit x yields grid
def t7():
    p0 = house(); out = {"design": "Yield move to 1 Jan 2027 fixed (0/-1/-2pt), later moves random (house rho 0); "
                                   "V25 with and without L-10's $10k coverage test (trap)."}
    grid = {}
    for mv in (0.0, -1.0, -2.0):
        p = dict(p0); p["s0"] = np.full(N, mv)
        row = {"ladder_cost": round(float(x.ladder_cost(np.array([mv]))[0]))}
        for dep in (0, 10_000, 25_000, 40_000, 50_000, 65_000, 75_000, 150_000):
            a = x.caplet_xr(p, d28=float(dep)); b = x.caplet_xr(p, d28=float(dep), trap=10_000)
            row[str(dep)] = {"p_short_no_rule": round(float((a["payments_short_amt"] > 1000).mean()), 4),
                             "p_short_with_coverage_rule": round(float((b["payments_short_amt"] > 1000).mean()), 4),
                             "gift_p50": round(float(np.median(a["gift"])))}
        grid[f"{mv:+.0f}pt"] = row
    out["grid"] = grid
    save("T7_deposit_x_yields", out)


# ------------------------------------------------------------------------------------------ add-ons (run after the first pass)
def extras():
    """(a) T2/T3 in the 2008 replay; (b) V25 + rule G WITHOUT the lock (the lock is not adopted) with T2/T3;
    (c) mean gift and hold-back cost (medians do not subtract); (d) T7 finer grid at -2pt."""
    out = {}
    combos = (("base", {}), ("T2_holdback_2028", {"holdback": CUSH}), ("T3_remeasure_2031", {"remeasure": True}),
              ("T2+T3_combined", {"holdback": CUSH, "remeasure": True}))
    plans = (("V25", {}), ("V25_plus_G_no_lock", {"cush": CUSH}), ("champion_lock_G", {"lock": True, "cush": CUSH}))
    keep = ("p_cheque_short_over_1k", "p_late_gap_exceeds_kept_2033", "p_gift_below_bottom", "p_top_reached",
            "gift_p1_p5_p50_p95", "bottom_p50", "top_p50", "laura_kept_2033_p50", "short_amt_p50_when_short")
    rep = {}
    for case, (cm, extra_dy) in {"A_crash_2027_before_deposit": (slice(0, 12), 0.0),
                                 "C_crash_2028_and_yields_fall_another_1.9pt_in_2028": (slice(12, 24), -1.9)}.items():
        p = house(); p["s0"] = np.full(N, -1.9); p["eq"][:, cm] = np.log(0.6) / 12
        if extra_dy:
            p["dy"][:, 12:24] = extra_dy / 12
        cache = {}; rep[case] = {}
        for pl, kw in plans:
            rep[case][pl] = {}
            for v, ex in combos:
                o = xr_plus(p, d28=75_000.0, _cache=cache, **kw, **ex); s = stats(o)
                rep[case][pl][v] = {k: s[k] for k in keep}
        del p, cache
    out["replay_2008_with_T2_T3"] = rep
    wl = {}
    for name, (mk, rho) in {"house_rho0": (lambda: house(), None),
                            "joint_storm_rho0.8_linked_deposit": (lambda: house(rho=0.8), 0.8)}.items():
        p = mk(); cache = {}
        d28 = 150_000 * deposit_factor(p, rho, 0.35, N) if rho is not None else x.DEP28
        wl[name] = {}
        for pl, kw in plans:
            wl[name][pl] = {}
            for v, ex in combos:
                o = xr_plus(p, d28=d28, _cache=cache, **kw, **ex); s = stats(o)
                s = {k: s[k] for k in keep}
                s["gift_mean"] = round(float(o["gift"].mean())); s["holdback_cost_mean"] = round(float(o["Hc"].mean()))
                s["bottom_mean"] = round(float(o["bottom"].mean())); s["laura_kept_2033_mean"] = round(float(o["kept33"].mean()))
                wl[name][pl][v] = s
        del p, cache
    out["T2_T3_all_three_plans_with_means"] = wl
    p0 = house(); g = {}
    for dep in (65_000, 75_000, 85_000, 100_000, 115_000, 130_000, 150_000):
        p = dict(p0); p["s0"] = np.full(N, -2.0)
        a = x.caplet_xr(p, d28=float(dep)); b = x.caplet_xr(p, d28=float(dep), trap=10_000)
        g[str(dep)] = {"p_short_no_rule": round(float((a["payments_short_amt"] > 1000).mean()), 4),
                       "p_short_with_coverage_rule": round(float((b["payments_short_amt"] > 1000).mean()), 4)}
    out["T7_fine_grid_minus2pt"] = g
    save("extras", out)


if __name__ == "__main__":
    want = sys.argv[1:] or ["T1", "T5", "T2", "T4", "T8", "T7"]
    save("selfcheck", selfcheck())
    for t in want:
        {"T1": t1, "T5": t5, "T2": t2_t3, "T3": t2_t3, "T4": t4, "T8": t8, "T7": t7, "extras": extras}[t]()
