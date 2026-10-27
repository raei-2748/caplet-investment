"""AI-generated (Claude Code), Tue 27 Oct 2026. MODEL. Genius Lab L-10 "Last in line".
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed 20261016
       | basis: ips_numbers.py unchanged except the patches below; MODEL, not a promise.
Run from repo root: python3 keel/rooms/lab/L-10_last_in_line/run.py   (~2 min per scenario)

Reads Laura's plan as a capital structure: losses run down a fixed order (D1a): leftover cash, then Laura's kept
half of the stock fund, then the gift above the 2031 bottom, then the bottom (the floor), then the ten payments.
For each "as needs change" stress it reports how often each layer is touched: the per-layer "probability of
exhaustion" in the sense of the IRS's Rev. Rul. 77-374 test (the chance the money runs out), asked for by the
Library (REQUESTS 27 Oct). Patching approach copied from keel/ips_rewrite/lab/R05_joint.py.
"""
import contextlib, io, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
M = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
HERE = pathlib.Path(__file__).parent
CSV22 = ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"

EXTRA = '''
    unfilled = UNFILLED27 * (1 + np.maximum(curve(3 + TOFF) + s27, YMIN) / 100) ** 6   # missing rung money, 2033 $
    short_2033 = np.maximum(uncovered - floor_paid - half, 0)                           # gap beyond floor + both halves
    pay_unmet = (unfilled > 1) | (short_2033 > 1) | miss
    gift_c = np.maximum(gift, 0)
    touched_keep = (shortfall + unfilled) > L33 + 1000
    out["L10"] = {
      "p_keep_touched": round(float(touched_keep.mean()), 4),
      "p_top_missed": round(float((gift_c < top - 1000).mean()), 4),
      "p_bottom_missed": round(float((gift_c < bottom - 1e-6).mean()), 4),
      "p_payment_unmet": round(float(pay_unmet.mean()), 4),
      "p_payment_unmet_parts": {"jan2027_gap_not_filled": round(float((unfilled > 1).mean()), 4),
                                "gap_beyond_floor_in_2033": round(float((short_2033 > 1).mean()), 4),
                                "post2033_gap_beyond_kept_half": round(float(miss.mean()), 4)},
      "payment_unmet_median_when_it_happens": round(float(np.median((unfilled + short_2033 + np.where(miss, extra - kept_after * g_after, 0))[pay_unmet]))) if pay_unmet.any() else 0,
      "p_exhaustion_payment_or_bottom": round(float((pay_unmet | (gift_c < bottom - 1e-6)).mean()), 4),
      "bottom_p50": round(float(np.median(bottom))), "top_p50": round(float(np.median(top))),
      "gift_p5_p50": [round(float(np.percentile(gift_c, 5))), round(float(np.median(gift_c)))],
      "kept_half_2033_p50": round(float(np.median(half))),
      "cushion_under_payments_2033_p50": round(float(np.median(L33 + 2 * half + floor_paid))),
      "p_ladder_over_300k": round(float((gap27 > 0).mean()), 4),
      "jan2027_gap_p50_when_positive": round(float(np.median(gap27[gap27 > 0]))) if (gap27 > 0).any() else 0,
    }
    # the cure tested after S1 showed the hole: a 2033 "cash trap" (a CLO-style coverage test). Before the gift goes
    # out, what stays behind with Laura (kept_after) must be at least H; any shortfall T is held back from the gift in
    # cash (no interest assumed: conservative) and goes to the facility later if the payments never need it.
    cure = {}
    for H in (10_000, 20_000, 30_000):
        need = np.maximum(H - kept_after, 0)
        for tag, room in (("top_only", np.maximum(gift_c - bottom, 0)), ("top_then_bottom", gift_c)):
            T = np.minimum(need, room)
            g2 = gift_c - T
            miss2 = extra > kept_after * g_after + T
            unmet2 = (unfilled > 1) | (short_2033 > 1) | miss2
            later = np.maximum(T - np.maximum(extra - kept_after * g_after, 0), 0)
            cure[f"H={H} {tag}"] = {
              "p_payment_unmet": round(float(unmet2.mean()), 4),
              "p_bottom_missed_2033": round(float((g2 < bottom - 1e-6).mean()), 4),
              "p_top_missed_2033": round(float((g2 < top - 1000).mean()), 4),
              "p_trap_used": round(float((T > 0).mean()), 4),
              "trap_p50_when_used": round(float(np.median(T[T > 0]))) if (T > 0).any() else 0,
              "gift_2033_p50": round(float(np.median(g2))),
              "gift_incl_later_release_p50": round(float(np.median(g2 + later))),
              "p_gift_incl_later_below_bottom": round(float((g2 + later < bottom - 1e-6).mean()), 4),
              "p_top_missed_incl_later": round(float((g2 + later < top - 1000).mean()), 4)}
    out["L10"]["cure"] = cure
    out["laura_kept_2033"] = {'''


def run(d28=150_000.0, rho=0.5, dy_build=0.0, dy_after=0.0, h_pre=1.0, h_post=1.0):
    tmp = HERE / "_tmp.json"
    src = M.read_text()
    reps = [
        ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
         f'CURVE_CSV = pathlib.Path(r"{CSV22}")'),
        ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
        ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
        ('(HERE / "results.json")', f'(pathlib.Path(r"{tmp}"))'),
        ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', 'EQ_MU, EQ_VOL, VT_FEE = np.log(1.075), 0.1678, 0.0006'),
        ('DEPOSIT27, DEPOSIT28, PAY = 300_000.0, 150_000.0, 50_000.0', f'DEPOSIT27, DEPOSIT28, PAY = 300_000.0, {d28}, 50_000.0'),
        # stresses on the rate paths: dy_build = a lasting move before the Jan 2027 build; dy_after = right after it
        ('    sh = lambda t: shifts[:, min(np.searchsorted(step_t, t), len(step_t) - 1)]',
         f'''    shifts[:, 1:] += {dy_build}
    shifts[:, np.searchsorted(step_t, TOFF) + 1:] += {dy_after}   # after the build step sh(TOFF) reads (audit fix)
    sh = lambda t: shifts[:, min(np.searchsorted(step_t, t), len(step_t) - 1)]'''),
        # anchor the 1 Jan 2027 cost to the bootstrapped headline WITHOUT the build stress, so the stress survives
        ('    cost27_p *= boot[str(TODAY)]["cost"] / np.median(cost27_p)   # anchor to the bootstrapped headline',
         f'''    _z0 = np.maximum(curve(pay_t27)[None, :] + (s27 - {dy_build})[:, None], YMIN) / 100
    cost27_p *= boot[str(TODAY)]["cost"] / np.median(PAY * ((1 + _z0 / 2) ** (-2 * pay_t27)).sum(axis=1))'''),
        ('    R = DEPOSIT28 - gap27                                    # remainder after filling any rung gap',
         '    R = np.maximum(DEPOSIT28 - gap27, 0); UNFILLED27 = np.maximum(gap27 - DEPOSIT28, 0)'),
        ('    B0 = DEPOSIT28 - gap27 - ibtm_cost', '    B0 = R - ibtm_cost'),
        ('    z = rng.normal(size=(N, 5))', f'''    _t0 = yrs(TODAY, T28)
    _dy = np.stack([sh(_t0 + j + 1) - sh(_t0 + j) for j in range(5)], axis=1) / RATE_VOL
    z = {rho} * _dy + np.sqrt(1 - {rho}**2) * rng.normal(size=(N, 5))'''),
        ('    V33 = B0 * np.exp(logr.sum(axis=1))', f'''    V33 = B0 * np.exp(logr.sum(axis=1))
    V31 = V31 * {h_pre}; V33 = V33 * {h_pre} * {h_post}'''),
        ('    bottom = np.floor((R - 3700) / 5000) * 5000', '    bottom = np.maximum(np.floor((R - 3700) / 5000) * 5000, 0)'),
        ('    out["laura_kept_2033"] = {', EXTRA),
    ]
    for old, new in reps:
        assert src.count(old) == 1, old
        src = src.replace(old, new)
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, str(M), "exec"), {"__name__": "__main__", "__file__": str(M)})
    res = json.loads(tmp.read_text()); tmp.unlink()
    return {**res["L10"], "ladder_headroom": res["ladder_headroom"]}


SCENARIOS = {
    "S0 base, rates and stocks independent": dict(rho=0.0),
    "S1 base, recession-linked (rho 0.5)": dict(),
    "S2 2028 deposit halved ($75k)": dict(d28=75_000.0),
    "S3 2028 deposit missing": dict(d28=0.0),
    "S4 yields 1pt lower before the Jan 2027 build": dict(dy_build=-1.0),
    "S5 S4 + 2028 deposit missing": dict(dy_build=-1.0, d28=0.0),
    "S6 yields fall 2pt just after the build, for good": dict(dy_after=-2.0),
    "S7 stocks halve before the 2031 range is set": dict(h_pre=0.5),
    "S8 stocks halve after the 2031 range is set": dict(h_post=0.5),
}

if __name__ == "__main__":
    import sys
    keys = [k for k in SCENARIOS if not sys.argv[1:] or k.split()[0] in sys.argv[1:]]
    f = HERE / "results.json"
    out = json.loads(f.read_text()) if f.exists() else {}
    out["stamp"] = "curve 22 Oct 2026 | J.P. Morgan 2027 global equities 7.5% | 200,000 paths, seed 20261016 | MODEL"
    for k in keys:
        out[k] = run(**SCENARIOS[k]); print(k, json.dumps(out[k]), flush=True)
        f.write_text(json.dumps(out, indent=1))
