"""AI-generated (Claude Code), Wed 28 Oct 2026. MODEL. Genius Lab L-11 "A cure with a birthday".
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed 20261016
       | basis: ips_numbers.py unchanged except L-10's patches (imported from its run.py) | MODEL, not a promise.
Run from repo root: python3 keel/rooms/lab/L-11_birthday_cure/run.py [S0 S1 S6]   (~3 min per scenario)

Round 1 (Wed 28 Oct) asks for a cure for the coupon gap that is itself bought on its birthday. Requests answered:
Library -> Lab (28 Oct): (a) a reserve bought on the 2028 deposit day, Laura's, released in 2042 if unused; (b) a
check before every cheque, 2034-42, vs one Jan 2033 re-match; (c) how much of the shortfall arrives after Jan 2033.
Archive -> Lab (27 Oct): the Jan 2033 set-aside (visible gap + cushion C), Laura's half not a source afterwards.

Designs (all share one 2033 order: leftover cash, then [Laura's half if allowed], then the gift above the top's
surplus, the top, and last the bottom):
  D0  L-10 base: no rule. Post-2033 gaps are paid from Laura's half kept in stocks to 2042 (the F2 clash).
  D1  C6 / Archive set-aside: Jan 2033 moves the visible gap + C into cash; afterwards Laura's half is never a source.
  D2  Birthday reserve: Rz taken from the stock-fund budget on 2 Jan 2028, held in short Treasuries (bill rate to
      2033, then 0%: cautious); Laura's half is never sold for a payment. Unused reserve goes to Laura after 2042.
  D3  D2 + a yearly check: each January 2034-42 the newly visible gap is moved from the reserve, and only if the
      reserve is spent, from Laura's half (sold that year, at that year's price).
Plus the immunisation challenger (C-c): how much of a 30-year Treasury, bought Jan 2028 and sold Jan 2033, would
offset the gap's rate exposure (deterministic, same curve).
"""
import contextlib, io, json, pathlib, sys
HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE.parent / "L-10_last_in_line"))
import run as L10   # noqa: E402  (L-10's patch list and scenarios, reused unchanged)

EXTRA = '''
    import numpy as _np
    # ---- L-11 ----
    unfilled = UNFILLED27 * (1 + np.maximum(curve(3 + TOFF) + s27, YMIN) / 100) ** 6
    extra_ = np.maximum(shortfall - S33, 0)
    rng2 = np.random.default_rng(SEED + 11)
    vt_yr = np.exp(((EQ_MU - VT_FEE) + EQ_VOL * rng2.normal(size=(N, 9))))      # Laura's half, 2033 -> 2042, yearly
    t28 = yrs(TODAY, T28)
    bill5 = np.ones(N)
    for j in range(5):
        bill5 *= 1 + np.maximum(curve(.25) + sh(t28 + j), YMIN) / 100              # short Treasuries, 2028 -> 2033
    # projected total delivery with rates frozen after 1 Jan of year Y (what a check that January would see)
    def proj_at(Y):
        iY = np.searchsorted(step_t, yrs(TODAY, dt.date(Y, 1, 1)))
        p = np.zeros(N)
        for (py, (name, mat, cpn)) in RUNGS.items():
            T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27, YMIN)
            cc = (y0p if cpn is None else np.full(N, cpn)) / 100
            kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
            ii = np.clip(np.searchsorted(step_t, kk + TOFF), 0, len(step_t) - 1)
            relf = shifts[:, np.minimum(ii, iY)] - s27[:, None]
            ykk = np.maximum(y0p[:, None] + relf, YMIN) / 100
            dd = 1 + (cc / 2) * ((1 + ykk / 2) ** (2 * (T - kk))).sum(axis=1)
            db = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - kk))).sum(axis=1)
            p += PAY * dd / db
        return np.maximum(10 * PAY - p, 0)
    G = {Y: proj_at(Y) for Y in range(2034, 2042)}
    G[2033] = S33; G[2042] = shortfall

    sm = lambda x: round(float(x), 4)
    md = lambda x, m: round(float(np.median(x[m]))) if m.any() else 0

    def at_2033(cash0, need, half_L, allow_half, top_, gift_avail):
        nb = np.maximum(need - cash0, 0)
        from_half = np.minimum(nb, half_L) if allow_half else np.zeros(N)
        nb2 = nb - from_half
        from_gift = np.minimum(nb2, gift_avail)
        gift_ = np.minimum(top_, gift_avail - from_gift)
        return cash0 + from_half + from_gift, from_half, gift_

    def report(short, gift_, top_, bottom_, sold, release=None, laura42=None):
        tot = short + unfilled
        r = {"p_payment_short_over_1": sm(((tot > 1)).mean()), "p_payment_short_over_1k": sm((tot > 1000).mean()),
             "median_short_when_short": md(tot, tot > 1),
             "p_laura_half_sold_for_payments": sm((sold > 1).mean()), "median_sold_when_sold": md(sold, sold > 1),
             "gift_2033_p5_p50": [round(float(np.percentile(gift_, 5))), round(float(np.median(gift_)))],
             "p_top_reached_within_1k": sm((gift_ >= top_ - 1000).mean()),
             "p_below_bottom_2033": sm((gift_ < bottom_ - 1e-6).mean()),
             "top_p50": round(float(np.median(top_))), "bottom_p50": round(float(np.median(bottom_)))}
        if release is not None:
            r["release_to_laura_after_2042_p50"] = round(float(np.median(release)))
        if laura42 is not None:
            r["laura_2042_stocks_plus_release_p5_p50"] = [round(float(np.percentile(laura42, 5))), round(float(np.median(laura42)))]
        return r

    res = {}
    # (c) the block's blind spot: how much of the shortfall arrives after Jan 2033
    m1 = shortfall > 1000
    res["blind_spot"] = {
        "p_shortfall_over_1k": sm(m1.mean()),
        "share_of_shortfall_dollars_after_2033": sm(extra_.sum() / max(shortfall.sum(), 1)),
        "median_share_after_2033_when_over_1k": sm(np.median(extra_[m1] / shortfall[m1])) if m1.any() else 0,
        "p_visible_in_2033_over_1k": sm((S33 > 1000).mean()),
        "p_appears_only_after_2033_over_1k": sm(((extra_ > 1000) & (S33 <= 1000)).mean()),
        "median_S33_and_extra_when_over_1k": [md(S33, m1), md(extra_, m1)],
        "shortfall_p50_p95_p99": [round(float(np.percentile(shortfall, q))) for q in (50, 95, 99)],
        "extra_p95_p99_p999": [round(float(np.percentile(extra_, q))) for q in (95, 99, 99.9)],
        "stock_fund_B0_p50": round(float(np.median(B0))), "bill_growth_2028_33_p50": round(float(np.median(bill5)), 4)}

    half_L = half; gift_avail = floor_paid + half
    # D0: L-10 base reproduced (post-2033 from Laura's half in stocks, to 2042 in one lump)
    cash, sold, g0 = at_2033(L33, S33, half_L, True, top, gift_avail)
    short0 = np.maximum(S33 + extra_ - cash, 0) - np.minimum(np.maximum(S33 + extra_ - cash, 0), (half_L - sold) * g_after)
    sold0 = sold + np.minimum(np.maximum(S33 + extra_ - cash, 0), (half_L - sold) * g_after)
    res["D0 no rule (L-10 base)"] = report(short0, g0, top, bottom, sold0)
    # D1: one Jan 2033 re-match (visible gap + cushion C), Laura's half never a source afterwards (Archive A19)
    for C in (0, 5_000, 7_500, 10_000, 20_000):
        cash, sold, g1 = at_2033(L33, S33 + C, half_L, True, top, gift_avail)
        rel = np.maximum(cash - S33 - extra_, 0)
        res[f"D1 2033 set-aside, cushion {C/1000:g}k"] = report(np.maximum(S33 + extra_ - cash, 0), g1, top, bottom, sold,
                                                              release=rel, laura42=(half_L - sold) * g_after + rel)
    # D2: birthday reserve Rz bought 2 Jan 2028 in short Treasuries, kept for the coupons still to come; the gap
    # visible in Jan 2033 is set aside as in D1 (leftover, Laura's half, gift). Source (a) the stock-fund budget,
    # (b) the floor budget (the locked 2028 order: payments, then floor, then stocks).
    for src in ("fund", "floor"):
        for Rz in (2_500, 5_000, 7_500, 10_000):
            if src == "fund":
                r0 = np.minimum(Rz, np.maximum(B0, 0)); f = np.where(B0 > 0, (B0 - r0) / np.maximum(B0, 1e-9), 1.0)
                topz = R + 0.5 * V31 * f; halfz = 0.5 * V33 * f; fpz = floor_paid; botz = bottom
            else:
                r0 = np.minimum(Rz, R); f = np.maximum(R - r0, 0) / np.maximum(R, 1e-9)
                fpz = floor_paid * f; halfz = 0.5 * V33 * f
                botz = np.maximum(np.floor((R - r0 - 3700) / 5000) * 5000, 0); topz = R - r0 + 0.5 * V31 * f
            res33 = r0 * bill5
            cash, sold, g2 = at_2033(L33 + res33, S33 + res33, halfz, True, topz, fpz + halfz)
            rel = np.maximum(cash - S33 - extra_, 0)
            res[f"D2 birthday reserve {Rz/1000:g}k from {src}"] = report(np.maximum(S33 + extra_ - cash, 0), g2, topz, botz,
                                                                sold, release=rel, laura42=(halfz - sold) * g_after + rel)
    # D3: a check before every cheque, 2034-42, with no reserve: newly visible gap from cash, then Laura's half
    cash, sold, g1 = at_2033(L33, S33, half_L, True, top, gift_avail)
    covered = S33.copy(); cash_left = cash - np.minimum(cash, S33); units = half_L - sold; price = np.ones(N)
    sold_v = sold.copy(); short3 = np.maximum(S33 - cash, 0)
    for j, Y in enumerate(range(2034, 2043)):
        price = price * vt_yr[:, j]
        need = np.maximum(G[Y] - covered, 0); covered = covered + need
        pay_c = np.minimum(need, cash_left); cash_left -= pay_c; need -= pay_c
        pay_s = np.minimum(need, units * price); units -= pay_s / price; sold_v += pay_s
        short3 += need - pay_s
    res["D3 yearly check, no reserve"] = report(short3, g1, top, bottom, sold_v, release=cash_left,
                                                laura42=units * price + cash_left)
    p_sold_after = ((sold_v - sold) > 1)
    res["D3 yearly check, no reserve"]["p_stocks_sold_at_a_payment_deadline_2034_42"] = sm(p_sold_after.mean())
    out["L11"] = res
    out["laura_kept_2033"] = {'''


THIN = [('2041: ("T 4.25% Nov-2040", dt.date(2040, 11, 15), 4.25), 2042: ("T 3.125% Nov-2041", dt.date(2041, 11, 15), 3.125),',
         '2041: ("T 1.375% Nov-2040", dt.date(2040, 11, 15), 1.375), 2042: ("T 2% Nov-2041", dt.date(2041, 11, 15), 2.0),')]


def run(thin=False, **kw):
    """L-10's run() (its own code, read from its file) with L-11's block in place of L-10's; thin=True swaps the
    2041-42 rungs for the thin-coupon twins of the Window's W-01 (WInS listing UNVERIFIED)."""
    code = pathlib.Path(L10.__file__).read_text()
    body = code[code.index("def run("):code.index("\nSCENARIOS")]
    body = body.replace('return {**res["L10"], "ladder_headroom": res["ladder_headroom"]}',
                        'return {**res["L11"], "ladder_headroom": res["ladder_headroom"], '
                        '"stress_delivery": res["ladder_delivery_if_rates_fall_and_stay"]}')
    body = body.replace("    for old, new in reps:", "    reps += EXTRA_REPS\n    for old, new in reps:")
    ns = {"contextlib": contextlib, "io": io, "json": json, "pathlib": pathlib, "M": L10.M, "HERE": L10.HERE,
          "CSV22": L10.CSV22, "EXTRA": EXTRA, "EXTRA_REPS": THIN if thin else []}
    exec(body, ns)
    return ns["run"](**kw)


def immunisation_check(stress_delivery):
    """C-c: a 30-year par Treasury bought 2 Jan 2028 at the 22 Oct curve's 30y yield, sold Jan 2033 after a lasting
    move of dy (coupons reinvested at y+dy). Gain per $1 vs the ladder's extra gap, from the base model's own stress."""
    import numpy as np, pandas as pd
    row = pd.read_csv(L10.CSV22).iloc[0]
    y = float(row["30 Yr"]) / 100
    out = {"yield_30y_22oct": round(y * 100, 2)}
    for dy in (-1, -2):
        yy = y + dy / 100
        coupons = sum(y / 2 * (1 + yy / 2) ** (2 * 5 - k) for k in range(1, 11))
        price = sum(y / 2 * (1 + yy / 2) ** -k for k in range(1, 51)) + (1 + yy / 2) ** -50
        gain = coupons + price - (1 + y / 2) ** 10          # vs holding it with no rate move
        gap = stress_delivery["+0pp"] - stress_delivery[f"{dy:+g}pp"]
        out[f"{dy:+g}pp"] = {"ladder_gap_added": round(gap), "bond_gain_per_dollar_by_2033": round(gain, 3),
                             "bond_needed_to_offset": round(gap / gain)}
    return out


SCEN = {"S0": "S0 base, rates and stocks independent", "S1": "S1 base, recession-linked (rho 0.5)",
        "S6": "S6 yields fall 2pt just after the build, for good",
        "S0thin": "S0 + thin-coupon 2041-42 rungs (W-01)"}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(SCEN)
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | MODEL"
    for k in keys:
        name = SCEN[k]
        out[name] = run(thin=True, **L10.SCENARIOS[SCEN["S0"]]) if k == "S0thin" else run(**L10.SCENARIOS[name])
        if k == "S0":
            out["immunisation_check"] = immunisation_check(out[name]["stress_delivery"])
        print(name, json.dumps(out[name], indent=1), flush=True)
        f.write_text(json.dumps(out, indent=1))
