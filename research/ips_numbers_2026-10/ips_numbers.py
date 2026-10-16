"""IPS number sheet for Laura's real plan (Root-and-Branch on WInS-listed holdings).

AI-generated (Claude Code) for Team Caplet, 2026-10-16. MODEL numbers, not promises.
Inputs: Treasury par curve 15 Oct 2026 (competition/official_market_data/daily-treasury-rates_2026-10.csv),
FRED GS10 monthly (fred_GS10_monthly.csv), JPM 2026 LTCMA AC World 7.00% compound / 16.78% vol, VT fee 0.06%.

Plan modelled (IPS Version 5):
  1 Jan 2027: $300k buys ten rungs, each sized to deliver $50,000 if its income is reinvested at its own yield.
              Leftover (if any) is kept in a Treasury fund as the first buffer for a shortfall.
  2 Jan 2028: $150k first fills any rung gap; the remainder R buys IBTM (Dec 2032) sized to pay back R (the floor);
              the rest goes into VT.
  2031:       range = [R - $3,700 rounded down to $5k, R + half of VT's value].
  2033:       gift = floor holding + half of VT, capped at the top. A ladder shortfall is paid by the leftover, then
              Laura's half, then the gift above the floor.
Run: python3 research/ips_numbers_2026-10/ips_numbers.py   (numpy + pandas; ~1 minute)
"""
import datetime as dt
import json
import pathlib

import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"
CURVE_DATE = "10/15/2026"
TODAY = dt.date(2026, 10, 15)
T27, T28 = dt.date(2027, 1, 1), dt.date(2028, 1, 2)
N = 200_000
SEED = 20261016
RATE_VOL = 1.00     # pp per year, parallel shift (GS10 12-month change sd 1953-2026 = 1.08)
YMIN = 0.25         # yields floored at 0.25%
EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006
DEPOSIT27, DEPOSIT28, PAY = 300_000.0, 150_000.0, 50_000.0

# payment year: (holding, maturity, coupon % or None = iBond fund modelled as a par bond, coupon = its yield)
RUNGS = {
    2033: ("IBTM", dt.date(2032, 12, 15), None), 2034: ("IBTO", dt.date(2033, 12, 15), None),
    2035: ("IBTP", dt.date(2034, 12, 15), None), 2036: ("IBTQ", dt.date(2035, 12, 15), None),
    2037: ("IBTR", dt.date(2036, 12, 15), None), 2038: ("T 4.75% Feb-2037", dt.date(2037, 2, 15), 4.75),
    2039: ("T 4.50% May-2038", dt.date(2038, 5, 15), 4.50), 2040: ("T 4.375% Nov-2039", dt.date(2039, 11, 15), 4.375),
    2041: ("T 4.25% Nov-2040", dt.date(2040, 11, 15), 4.25), 2042: ("T 3.125% Nov-2041", dt.date(2041, 11, 15), 3.125),
}


def yrs(a, b):
    return (b - a).days / 365.25


def load_curve():
    df = pd.read_csv(CURVE_CSV)
    row = df[df.Date == CURVE_DATE].iloc[0]
    pts = {1/12: "1 Mo", .25: "3 Mo", .5: "6 Mo", 1: "1 Yr", 2: "2 Yr", 3: "3 Yr", 5: "5 Yr", 7: "7 Yr",
           10: "10 Yr", 20: "20 Yr", 30: "30 Yr"}
    xs = np.array(list(pts)); ys = np.array([float(row[k]) for k in pts.values()])
    return lambda t: np.interp(t, xs, ys)  # % par yield, used as a zero rate (C1: ~$200 difference)


def fwd_rate(curve, t0, t1):
    """Forward yield (%, semiannual) from t0 to t1 implied by today's curve."""
    z0, z1 = curve(t0) / 100, curve(t1) / 100
    a0, a1 = (1 + z0 / 2) ** (2 * t0), (1 + z1 / 2) ** (2 * t1)
    return 200 * ((a1 / a0) ** (1 / (2 * (t1 - t0))) - 1)


TOFF = yrs(TODAY, T27)  # step times are measured from today


def bootstrap_cost():
    """Headline cost: the verified 27-Sep method (bootstrapped zero curve, forward value at 1 Jan 2027)."""
    df = pd.read_csv(CURVE_CSV)
    out = {}
    for date in df.Date[:5]:
        row = df[df.Date == date].iloc[0]
        tenor = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
                 "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
        par = {t: float(row[k]) for k, t in tenor.items()}
        ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
        p = np.interp(grid, ts, [par[t] / 100 for t in ts]); dfs = []
        for y in p:
            c = y / 2; dfs.append((1 - c * sum(dfs)) / (1 + c))
        g = np.r_[0, grid]; lz = np.log(np.r_[1, dfs])
        f = lambda t: np.exp(np.interp(t, g, lz))
        val = dt.datetime.strptime(date, "%m/%d/%Y").date()
        ta = yrs(val, T27)
        cost = sum(PAY * f(yrs(val, dt.date(y, 1, 1))) / f(ta) for y in RUNGS)
        out[str(val)] = {"cost": round(float(cost)), "headroom": round(float(DEPOSIT27 - cost))}
    return out


def main():
    rng = np.random.default_rng(SEED)
    curve = load_curve()
    out = {"meta": {"curve_date": "2026-10-15", "paths": N, "seed": SEED, "rate_vol_pp_per_yr": RATE_VOL,
                    "equity": "VT ~ lognormal, 7.00% compound, 16.78% vol (JPM 2026 LTCMA AC World), minus 0.06% fee",
                    "basis": "MODEL; par yields used as zero rates; rates and stocks independent"}}

    # --- 1. Ladder cost at today's curve, carried to 1 Jan 2027 (zero-coupon view, as in the IPS's $292k) ---
    pay_t = np.array([yrs(TODAY, dt.date(y, 1, 1)) for y in RUNGS])
    dfs = (1 + curve(pay_t) / 200) ** (-2 * pay_t)
    carry = (1 + curve(TOFF) / 200) ** (2 * TOFF)
    cost27 = PAY * dfs.sum() * carry
    dv01 = PAY * (dfs * pay_t).sum() * carry / 1e4
    out["ladder_cost_1jan2027_today_curve"] = round(cost27)
    boot = bootstrap_cost()
    out["ladder_cost_bootstrap_headline"] = boot   # same method as research/verified_2026-09-27/official_curve_pv.py
    out["ladder_headroom"] = round(DEPOSIT27 - cost27)
    out["ladder_headroom_bp"] = round((DEPOSIT27 - cost27) / dv01, 1)

    # --- 2. Rate paths: parallel shift, random walk, monthly steps from today to 2043 ---
    step_t = np.arange(0, yrs(TODAY, dt.date(2043, 1, 1)) + 1 / 12, 1 / 12)
    inc = rng.normal(0, RATE_VOL * np.sqrt(1 / 12), (N, len(step_t) - 1))
    shifts = np.concatenate([np.zeros((N, 1)), inc.cumsum(axis=1)], axis=1)
    sh = lambda t: shifts[:, min(np.searchsorted(step_t, t), len(step_t) - 1)]

    # cost of the rungs on 1 Jan 2027 under each path (parallel shift since today)
    s27 = sh(TOFF)
    pay_t27 = np.array([yrs(T27, dt.date(y, 1, 1)) for y in RUNGS])
    z27 = np.maximum(curve(pay_t27)[None, :] + s27[:, None], YMIN) / 100     # roll-down ignored
    cost27_p = PAY * ((1 + z27 / 2) ** (-2 * pay_t27)).sum(axis=1)
    cost27_p *= boot[str(TODAY)]["cost"] / np.median(cost27_p)   # anchor to the bootstrapped headline
    gap27 = np.maximum(cost27_p - DEPOSIT27, 0)
    leftover27 = np.maximum(DEPOSIT27 - cost27_p, 0)
    out["p_ladder_over_300k_on_1jan2027"] = round(float((gap27 > 0).mean()), 3)

    # --- 3. Ladder delivery with coupon reinvestment (2027 purchase at 1 Jan 2027 yields) ---
    delivered = np.zeros(N); delivered_base = 0.0
    short_by_2033 = np.zeros(N)
    per_rung = {}
    for (py, (name, mat, cpn)), pt in zip(RUNGS.items(), pay_t27):
        T = yrs(T27, mat)
        y0 = curve(T + TOFF)  # today's yield for that maturity; the path shift applies from 1 Jan 2027
        y0p = np.maximum(y0 + s27, YMIN)
        gap_yrs = yrs(mat, dt.date(py, 1, 1))
        # each rung is sized on its own 1-Jan-2027 yield so that reinvesting at that yield delivers $50,000
        c = None if cpn is None else cpn
        # per-path: own yield y0p; reinvestment at y0p + (shift(t) - shift(TOFF))
        rel = shifts - s27[:, None]
        cc = (y0p if c is None else np.full(N, c)) / 100
        k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        idx = np.clip(np.searchsorted(step_t, k + TOFF), 0, len(step_t) - 1)
        yk = np.maximum(y0p[:, None] + rel[:, idx], YMIN) / 100
        grow = (1 + yk / 2) ** (2 * (T - k)[None, :])
        d = 1 + (cc / 2) * grow.sum(axis=1)
        dbase = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - k)[None, :])).sum(axis=1)
        bill_now = np.maximum(curve(.25) + s27 + rel[:, idx[-1]] if len(idx) else curve(.25) + s27, YMIN) / 100
        gapf = (1 + bill_now) ** gap_yrs
        gapf_base = (1 + np.maximum(curve(.25) + s27, YMIN) / 100) ** gap_yrs
        face = PAY / (dbase * gapf_base)
        val = face * d * gapf
        delivered += val
        per_rung[py] = (name, float(np.percentile(val, 5)), float(np.median(val)))
    shortfall = np.maximum(10 * PAY - delivered, 0)
    out["ladder_delivery_p5_p50"] = [round(np.percentile(delivered, 5)), round(np.median(delivered))]
    out["ladder_shortfall"] = {"p_any_over_1k": round(float((shortfall > 1000).mean()), 3),
                               "p50": round(float(np.median(shortfall))), "p95": round(float(np.percentile(shortfall, 95))),
                               "p99": round(float(np.percentile(shortfall, 99)))}
    out["per_rung_p5_p50"] = {str(k): [v[0], round(v[1]), round(v[2])] for k, v in per_rung.items()}

    # deterministic stress: rates fall X pp on 2 Jan 2027 and stay there (only reinvestment changes)
    stress = {}
    for dy in (0, -1, -2, -3, -4.5):
        tot = 0.0
        for (py, (name, mat, cpn)) in RUNGS.items():
            T = yrs(T27, mat); y0 = curve(T + TOFF)
            cc = (y0 if cpn is None else cpn) / 100
            k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
            yk = max(y0 + dy, YMIN) / 100
            d = 1 + cc / 2 * ((1 + yk / 2) ** (2 * (T - k))).sum()
            db = 1 + cc / 2 * ((1 + y0 / 200) ** (2 * (T - k))).sum()
            gy = yrs(mat, dt.date(py, 1, 1))
            g = (1 + max(curve(.25) + dy, YMIN) / 100) ** gy; gb = (1 + curve(.25) / 100) ** gy
            tot += PAY / (db * gb) * d * g
        stress[f"{dy:+g}pp"] = round(tot)
    out["ladder_delivery_if_rates_fall_and_stay"] = stress

    # --- 4. Floor and stock fund (2 Jan 2028) ---
    s28 = sh(yrs(TODAY, T28))
    t_ibtm = yrs(T28, dt.date(2032, 12, 15))
    y5_28 = np.maximum(fwd_rate(curve, yrs(TODAY, T28), yrs(TODAY, T28) + t_ibtm) + s28, YMIN)
    R = DEPOSIT28 - gap27                                    # remainder after filling any rung gap
    ibtm_cost = R / (1 + y5_28 / 200) ** (2 * t_ibtm)        # sized to pay back R at its yield
    # floor delivery: coupon fund, reinvestment risk to Dec 2032
    k = np.arange(1, int(np.floor(t_ibtm * 2)) + 1) / 2
    idx = np.clip(np.searchsorted(step_t, k + yrs(TODAY, T28)), 0, len(step_t) - 1)
    rel = shifts[:, idx] - s28[:, None]
    yk = np.maximum(y5_28[:, None] + rel, YMIN) / 100
    d = 1 + (y5_28 / 200) * ((1 + yk / 2) ** (2 * (t_ibtm - k)[None, :])).sum(axis=1)
    dbase = 1 + (y5_28 / 200) * ((1 + y5_28[:, None] / 200) ** (2 * (t_ibtm - k)[None, :])).sum(axis=1)
    floor_paid = R * d / dbase
    B0 = DEPOSIT28 - gap27 - ibtm_cost
    out["stock_fund_2jan2028"] = {"p5": round(np.percentile(B0, 5)), "p50": round(np.median(B0)), "p95": round(np.percentile(B0, 95))}
    out["floor_paid"] = {"p1": round(np.percentile(floor_paid, 1)), "p5": round(np.percentile(floor_paid, 5)),
                         "p50": round(np.median(floor_paid))}
    out["p_floor_remainder_below_150k"] = round(float((R < DEPOSIT28 - 1).mean()), 3)

    # --- 5. VT to 2031 and 2033 ---
    z = rng.normal(size=(N, 5))
    logr = (EQ_MU - VT_FEE) + EQ_VOL * z
    V31 = B0 * np.exp(logr[:, :3].sum(axis=1))
    V33 = B0 * np.exp(logr.sum(axis=1))
    # leftover from 2027 kept in Treasuries to 2033 at its 6-year yield
    L33 = leftover27 * (1 + np.maximum(curve(6 + TOFF) + s27, YMIN) / 100) ** 6

    # --- 6. 2031 range and 2033 gift ---
    bottom = np.floor((R - 3700) / 5000) * 5000
    top = R + 0.5 * V31
    # shortfall known in 2033: ladder delivery projected at 2033 yields (shift frozen after 1 Jan 2033)
    t33 = yrs(TODAY, dt.date(2033, 1, 1)); i33 = np.searchsorted(step_t, t33)
    shifts_frozen = shifts.copy(); shifts_frozen[:, i33:] = shifts[:, [i33]]
    # recompute ladder delivery with frozen shifts (projection a 2033 analyst could make)
    proj = np.zeros(N)
    for (py, (name, mat, cpn)) in RUNGS.items():
        T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27, YMIN)
        cc = (y0p if cpn is None else np.full(N, cpn)) / 100
        kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        ii = np.clip(np.searchsorted(step_t, kk + TOFF), 0, len(step_t) - 1)
        relf = shifts_frozen[:, ii] - s27[:, None]
        ykk = np.maximum(y0p[:, None] + relf, YMIN) / 100
        dd = 1 + (cc / 2) * ((1 + ykk / 2) ** (2 * (T - kk)[None, :])).sum(axis=1)
        db = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - kk)[None, :])).sum(axis=1)
        proj += PAY * dd / db
    S33 = np.maximum(10 * PAY - proj, 0)
    half = 0.5 * V33
    uncovered = np.maximum(S33 - L33 - half, 0)               # leftover first, then Laura's half
    gift = np.minimum(top, floor_paid + half - uncovered)
    inside = (gift >= bottom - 1e-6)
    out["range_2031"] = {"bottom_p50": round(np.median(bottom)), "bottom_mode_share_145k": round(float((bottom == 145000).mean()), 3),
                         "top_p5": round(np.percentile(top, 5)), "top_p50": round(np.median(top)), "top_p95": round(np.percentile(top, 95)),
                         "width_p50": round(np.median(top - bottom))}
    out["gift_2033"] = {"p5": round(np.percentile(gift, 5)), "p50": round(np.median(gift)), "p95": round(np.percentile(gift, 95)),
                        "mean": round(gift.mean())}
    out["p_gift_inside_range"] = round(float(inside.mean()), 4)
    out["p_gift_at_top_within_1k"] = round(float((gift >= top - 1000).mean()), 3)
    out["p_gift_below_middle"] = round(float((gift < (top + bottom) / 2).mean()), 4)
    out["p_floor_holding_pays_below_bottom"] = round(float((floor_paid < bottom).mean()), 4)
    out["p_shortfall_needs_gift_above_floor"] = round(float((uncovered > 0).mean()), 4)
    # after 2033: the true shortfall (rates keep moving) vs what Laura still holds (her half, leftover)
    extra = np.maximum(shortfall - S33, 0)
    kept_after = np.maximum(L33 + half - S33, 0)
    out["post2033_shortfall"] = {"p95": round(np.percentile(extra, 95)), "p99": round(np.percentile(extra, 99)),
                                 "p_exceeds_what_laura_kept": round(float((extra > kept_after).mean()), 4)}
    # Laura's kept half stays in VT after 2033; does it cover the later shortfall?
    g_after = np.exp(((EQ_MU - VT_FEE) + EQ_VOL * rng.normal(size=(N, 9))).sum(axis=1))
    miss = extra > kept_after * g_after
    out["post2033_shortfall"]["p_exceeds_kept_if_kept_in_VT_to_2042"] = round(float(miss.mean()), 4)
    out["post2033_shortfall"]["median_uncovered_when_it_happens"] = round(float(np.median((extra - kept_after * g_after)[miss]))) if miss.any() else 0
    out["floor_paid_vs_remainder"] = {"p1": round(float(np.percentile(floor_paid / R, 1)), 4),
                                      "p50": round(float(np.median(floor_paid / R)), 4)}
    S_any = shortfall > 1000
    out["p_payment_needs_more_than_kept_half_and_leftover_total"] = round(float((shortfall > L33 + half).mean()), 4)
    out["laura_kept_2033"] = {"p5": round(np.percentile(half + L33 - np.minimum(S33, L33 + half), 5)),
                              "p50": round(np.median(half + L33 - np.minimum(S33, L33 + half)))}

    # --- 7. Allocation in Jan 2028 (typical path) ---
    lad28 = cost27 * (1 + curve(6 + TOFF) / 100)  # rough 1-year carry of the ladder
    lo = DEPOSIT27 - cost27
    tot = lad28 + lo * 1.045 + DEPOSIT28
    fl = float(np.median(ibtm_cost)); vt = float(np.median(B0))
    out["allocation_jan2028_typical"] = {"payment_treasuries": round(lad28 / tot, 3), "floor_treasury_IBTM": round(fl / tot, 3),
                                         "leftover_treasury": round(lo * 1.045 / tot, 3), "VT": round(vt / tot, 3),
                                         "total": round(tot)}

    # --- 8. Historical replay of rate moves (GS10, monthly, 1953-2026): shortfall only ---
    gs = pd.read_csv(HERE / "fred_GS10_monthly.csv").GS10.values
    H = int(np.ceil(yrs(T27, dt.date(2042, 1, 1)) * 12))
    hist = []
    for s in range(0, len(gs) - H):
        path = gs[s:s + H + 1] - gs[s]
        tot_d = 0.0
        for (py, (name, mat, cpn)) in RUNGS.items():
            T = yrs(T27, mat); y0 = curve(T + TOFF)
            cc = (y0 if cpn is None else cpn) / 100
            kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
            yk = np.maximum(y0 + path[np.minimum((kk * 12).astype(int), H)], YMIN) / 100
            dd = 1 + cc / 2 * ((1 + yk / 2) ** (2 * (T - kk))).sum()
            db = 1 + cc / 2 * ((1 + y0 / 200) ** (2 * (T - kk))).sum()
            tot_d += PAY * dd / db
        hist.append(tot_d)
    hist = np.array(hist)
    hs = np.maximum(10 * PAY - hist, 0)
    out["history_replay"] = {"start_months": len(hist), "p_shortfall_over_1k": round(float((hs > 1000).mean()), 3),
                             "worst_shortfall": round(hs.max()), "p95_shortfall": round(np.percentile(hs, 95)),
                             "worst_start": str(pd.read_csv(HERE / "fred_GS10_monthly.csv").observation_date[int(hs.argmax())])}

    (HERE / "results.json").write_text(json.dumps(out, indent=2, default=float))
    print(json.dumps(out, indent=2, default=float))


if __name__ == "__main__":
    main()
