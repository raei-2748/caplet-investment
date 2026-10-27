"""AI-generated (Claude Code), Tue 27 Oct 2026 (Sydney), overnight push for north stars 3 + 4. MODEL numbers.
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% compound, 16.78% vol | 200,000 paths, seed 20261016
Run from repo root: python3 keel/ips_rewrite/lab/K_overnight.py   (numpy, pandas; ~2 minutes)

Tests one question per idea from the overnight knowledge dig (research/R06_overnight_dig.md):
  K1  Rising equity share ("bond tent"): how the stock share of everything Laura owns moves 2028-2042 under V25,
      with no trade after Jan 2028 except the 2033 contribution.
  K2  Flight path: how often each January checkpoint (2027, 2028, 2033) finds the ten payments under-funded,
      i.e. how often the single funding test actually has to act.
  K3  Ratchet: lock half of any gain on the contribution's stocks into a Treasury maturing Dec 2032 each January
      2029-2031. Does a bottom that can only rise beat V25's fixed bottom?
  K4  Rival archetypes in a simple common model (annual steps): static 60/40, glide 70->30, three-bucket, 90/10
      barbell, all-Treasury fund, vs V25. P(miss a payment), the 2033 contribution, the price of certainty.
V25's own numbers come from the unchanged keel/library/ips_numbers_2026-10/ips_numbers.py, patched to the 22 Oct
curve and 7.5% exactly as R05_joint.py does; K4 is a separate, cruder model and says so.
"""
import contextlib
import io
import json
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"

EXTRA = '''
    # ---------------- K overnight additions (all paths) ----------------
    K = {}
    mu_l = EQ_MU - VT_FEE
    # K1: stock share of everything Laura owns, each 1 Jan. Ladder valued at par of what is left to pay
    # (a held-to-maturity view); VT grows on the same draws (logr) to 2033, then Laura's half grows on fresh draws.
    share, share_mv = {}, {}
    lad_left = lambda y: PAY * sum(1 for p in RUNGS if p >= y)
    for j, y in enumerate((2028, 2029, 2030, 2031, 2032)):
        Vy = B0 * np.exp(logr[:, :j].sum(axis=1)) if j else B0
        tot = lad_left(2033) + R + Vy  # ladder and floor at what they will pay (par)
        share[y] = float(np.median(Vy / tot))
        # market value (flat 4.6%, the 22 Oct 4-5y area): Jun's audit, 28 Oct
        mv_lad = sum(PAY / 1.046 ** (p - y) for p in RUNGS if p >= y)
        share_mv[y] = float(np.median(Vy / (mv_lad + R / 1.046 ** (2033 - y) + Vy)))
    rng2 = np.random.default_rng(7)
    kept = np.maximum(half + L33 - np.minimum(S33, L33 + half), 0)
    g = np.exp(np.cumsum(mu_l + EQ_VOL * rng2.normal(size=(N, 10)), axis=1))
    for j, y in enumerate(range(2033, 2043)):
        Ky = kept * (g[:, j - 1] if j else 1.0)
        lad = lad_left(y) - PAY  # just after that January's payment
        share[y] = float(np.median(Ky / np.maximum(Ky + lad, 1)))
        mv_lad = sum(PAY / 1.046 ** (p - y) for p in RUNGS if p > y)
        share_mv[y] = float(np.median(Ky / np.maximum(Ky + mv_lad, 1)))
    K["K1_stock_share_median"] = {str(k): round(v, 3) for k, v in share.items() if k < 2042}
    K["K1_stock_share_median_market_value"] = {str(k): round(v, 3) for k, v in share_mv.items() if k < 2042}
    K["K1_kept_stock_dollars_p50_2033_2041"] = [round(float(np.median(kept))), round(float(np.median(kept * g[:, 7])))]
    K["K1_p_laura_keeps_nothing_2033"] = round(float((kept < 1).mean()), 3)
    # K2: flight-path checkpoints
    K["K2_checkpoints"] = {
        "jan2027_ladder_costs_more_than_300k": round(float((gap27 > 0).mean()), 3),
        "jan2027_gap_p50_when_short": round(float(np.median(gap27[gap27 > 0]))) if (gap27 > 0).any() else 0,
        "jan2028_gap_left_after_150k_deposit": round(float((gap27 > DEPOSIT28).mean()), 5),
        "jan2033_coupon_gap_over_1k": round(float((S33 > 1000).mean()), 3),
        "jan2033_gap_p95": round(float(np.percentile(S33, 95))),
        "jan2033_gap_covered_by_leftover_plus_lauras_half": round(float((S33 <= L33 + half).mean()), 4),
    }
    # K3: ratchet. Contribution half of VT = H0 = B0/2 bought Jan 2028. Each Jan 2029-2031, if the half is above its
    # high-water mark, move half of the gain into a Treasury maturing Dec 2032 (yield ~ 4.6%, 22 Oct 4-5y area).
    yT = 0.046
    H = B0 / 2; locked = np.zeros(N); hwm = H.copy()
    for j in range(3):  # returns for 2028, 2029, 2030 -> decisions on 1 Jan 2029, 2030, 2031
        H = H * np.exp(logr[:, j])
        gain = np.maximum(H - hwm, 0)
        mv = 0.5 * gain
        H = H - mv
        locked += mv * (1 + yT) ** (4 - j)   # grows to Dec 2032
        hwm = np.maximum(hwm, H)
    H31 = H
    H33 = H31 * np.exp(logr[:, 3] + logr[:, 4])
    bottom_r = np.floor((R + locked - 3700) / 5000) * 5000
    top_r = R + locked + H31
    gift_r = np.minimum(top_r, floor_paid + locked + H33 - uncovered)
    gift_v = gift
    def d(x): return {"p5": round(float(np.percentile(x, 5))), "p50": round(float(np.median(x))), "mean": round(float(x.mean()))}
    K["K3_ratchet"] = {
        "V25": {"bottom": d(bottom), "top": d(top), "gift": d(gift_v), "p_top_within_1k": round(float((gift_v >= top - 1000).mean()), 3),
                "p_below_bottom": round(float((gift_v < bottom - 1e-6).mean()), 4), "width_p50": round(float(np.median(top - bottom)))},
        "ratchet": {"bottom": d(bottom_r), "top": d(top_r), "gift": d(gift_r), "p_top_within_1k": round(float((gift_r >= top_r - 1000).mean()), 3),
                    "p_below_bottom": round(float((gift_r < bottom_r - 1e-6).mean()), 4), "width_p50": round(float(np.median(top_r - bottom_r))),
                    "p_bottom_raised_5k_plus": round(float((bottom_r >= bottom + 5000).mean()), 3)},
    }
    out["K"] = K
    out["laura_kept_2033"] = {'''


def run_v25():
    src = SRC.read_text()
    tmp = HERE / "_k_tmp.json"
    reps = [
        ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
         f'CURVE_CSV = pathlib.Path(r"{ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"}")'),
        ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
        ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
        ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
        ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', 'EQ_MU, EQ_VOL, VT_FEE = np.log(1.075), 0.1678, 0.0006'),
        ('    out["laura_kept_2033"] = {', EXTRA),
    ]
    for old, new in reps:
        assert src.count(old) == 1, old
        src = src.replace(old, new)
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, str(SRC), "exec"), {"__name__": "__main__", "__file__": str(SRC)})
    res = json.loads(tmp.read_text()); tmp.unlink()
    return res


# ---------------- K4: rival archetypes, one simple common model ----------------
def rivals(n=100_000, seed=11, dep28=150_000.0):
    """Annual steps, 1 Jan 2027 -> 1 Jan 2043. Stocks: lognormal 7.5% compound, 16.78% vol, 0.06% fee.
    Yields: one rate (10y-ish) starting 4.96% (22 Oct 10y), random walk 1.00pp/yr, floor 0.25%. Bond fund (duration 6):
    return = y_prev - 6 * dy. Bills: y - 0.7 (22 Oct 1y 4.41 vs 10y 4.96, rounded). Each rival keeps its mix, rebalanced
    yearly; on 1 Jan 2033 it pays the contribution = assets minus a reserve sized at the market value of the ten
    payments (PV at that day's yield) plus a 10% cushion; the reserve then follows the rival's own post-2033 mix.
    A miss = any January 2033-2042 when the reserve cannot pay $50,000 in full."""
    rng = np.random.default_rng(seed)
    T = 16
    z = rng.normal(size=(n, T)); e = rng.normal(size=(n, T))
    st = np.exp(np.log(1.075) - 0.0006 + 0.1678 * z) - 1
    y = np.empty((n, T + 1)); y[:, 0] = 4.96
    for t in range(T):
        y[:, t + 1] = np.maximum(y[:, t] + 1.0 * e[:, t], 0.25)
    dy = np.diff(y, axis=1)
    bond = y[:, :-1] / 100 - 6 * dy / 100
    bill = np.maximum(y[:, :-1] - 0.7, 0.25) / 100

    def pv_pay(yy, k):  # k payments, first one today
        disc = (1 + yy[:, None] / 100) ** -np.arange(k)[None, :]
        return 50_000 * disc.sum(axis=1)

    plans = {  # (stock weight by year index 0..5 for 2027-2032, post-2033 stock weight, post-2033 bill share of reserve)
        "60/40 total return": ([.6] * 6, .6, 0.0),
        "glide 70 -> 30": ([.7, .64, .58, .52, .46, .40], .3, 0.0),
        "three buckets (3 yrs in bills)": ([.5] * 6, .4, 0.3),
        "barbell 90/10": ([.1] * 6, .1, 0.9),
        "all bond fund (immunise-ish)": ([0.0] * 6, 0.0, 0.0),
    }
    out = {}
    for name, (w_pre, w_post, bshare) in plans.items():
        A = np.full(n, 300_000.0)
        for t in range(6):  # 2027..2032 (index 0 = calendar 2027)
            if t == 1:
                A += dep28
            w = w_pre[t]
            A *= 1 + w * st[:, t] + (1 - w) * bond[:, t]
        reserve_need = pv_pay(y[:, 6], 10) * 1.10
        contrib = np.maximum(A - reserve_need, 0)
        Rz = A - contrib
        miss = np.zeros(n, dtype=bool); left = Rz
        for k, t in enumerate(range(6, 16)):  # Jan 2033 .. Jan 2042 payments, then a year of returns
            miss |= left < 50_000 - 1
            left = np.maximum(left - 50_000, 0)
            ws, wb = w_post, (1 - w_post) * (1 - bshare)
            left *= 1 + ws * st[:, t] + wb * bond[:, t] + (1 - w_post) * bshare * bill[:, t]
        out[name] = {"p_miss_any_payment": round(float(miss.mean()), 4),
                     "contribution_2033": {"p5": round(float(np.percentile(contrib, 5))), "p50": round(float(np.median(contrib))),
                                           "p95": round(float(np.percentile(contrib, 95)))},
                     "p_contribution_zero": round(float((contrib < 1).mean()), 3),
                     "left_after_2042_p50": round(float(np.median(left)))}
    return out


if __name__ == "__main__":
    v = run_v25()
    res = {"stamp": "22 Oct 2026 curve; 7.5% world stocks (J.P. Morgan 2027); 200,000 paths; MODEL",
           "V25_headline": {k: v[k] for k in ("ladder_headroom", "p_ladder_over_300k_on_1jan2027", "gift_2033", "range_2031",
                                              "p_gift_inside_range", "p_gift_at_top_within_1k", "post2033_shortfall", "laura_kept_2033")},
           **v["K"]}
    res["K4_rivals_dep28_150k"] = rivals()
    res["K4_rivals_dep28_75k"] = rivals(dep28=75_000.0)
    (HERE / "K_overnight_results.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))
