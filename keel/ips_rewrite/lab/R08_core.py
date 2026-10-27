"""AI-generated (Claude Code), Genius Lab WO-R8, 27 Oct 2026 (Sydney). MODEL.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA global equities 7.5% (sceptic 6.5%) | 200,000 paths,
seed 20261016 | rates 1pp/yr parallel random walk, stocks 16.78% vol | MODEL (keel/library/ips_numbers_2026-10/ips_numbers.py)

Shared engine for the R08_* idea scripts. It runs the unchanged office model on the 22 Oct curve (same patches as
R05_joint.py: rho = correlation of each year's 2028-32 stock shock with that year's yield change), and adds:
  - g2:        growth of $1 put into IBTM on 1 Jan 2031 until Dec 2032 (for "lock what you announce")
  - S33m1/m2:  the coupon gap a 2033 analyst would project if yields fell a further 1 / 2 points for good after 2033
  - delivered_rolled / delivered_cash: the ladder's ten-payment total if coupons were parked in a rolling T-bill fund
               (or held as cash) instead of buying more of their own rung (the model's default)
It then dumps the per-path arrays (float32) to a cache, so each idea script can try its rule on the same 200,000 futures.
Run directly to fill the cache: python3 keel/ips_rewrite/lab/R08_core.py
"""
import contextlib, io, os, pathlib, tempfile
import numpy as np

ROOT = pathlib.Path("/home/user/caplet-investment")
MODEL = ROOT / "keel/library/ips_numbers_2026-10/ips_numbers.py"
CURVE = ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"
CACHE = pathlib.Path(os.environ.get("R08_CACHE", pathlib.Path(tempfile.gettempdir()) / "r08_cache"))
STAMP = ("STAMP: curve 22 Oct 2026 | JPM 2027 global equities {mu} | 200,000 paths, seed 20261016 | rho {rho} | MODEL")

EXTRA = '''
    # ---------- R08 additions ----------
    _t31 = yrs(TODAY, dt.date(2031, 1, 1)); _tl = yrs(dt.date(2031, 1, 1), dt.date(2032, 12, 15))
    _y31 = np.maximum(fwd_rate(curve, _t31, _t31 + _tl) + sh(_t31), YMIN)
    g2 = (1 + _y31 / 200) ** (2 * _tl)
    def _proj(delta):
        sf = shifts_frozen.copy(); sf[:, i33 + 1:] += delta
        tot = np.zeros(N)
        for (py, (name, mat, cpn)) in RUNGS.items():
            T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27, YMIN)
            cc = (y0p if cpn is None else np.full(N, cpn)) / 100
            kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
            ii = np.clip(np.searchsorted(step_t, kk + TOFF), 0, len(step_t) - 1)
            ykk = np.maximum(y0p[:, None] + sf[:, ii] - s27[:, None], YMIN) / 100
            dd = 1 + (cc / 2) * ((1 + ykk / 2) ** (2 * (T - kk)[None, :])).sum(axis=1)
            db = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - kk)[None, :])).sum(axis=1)
            tot += PAY * dd / db
        return np.maximum(10 * PAY - tot, 0)
    S33m1 = _proj(-1.0); S33m2 = _proj(-2.0)
    # coupons parked in a rolling 3-month bill fund (monthly roll) or held as cash, instead of buying their own rung
    _rm = np.maximum(curve(.25) + shifts, YMIN) / 100
    _G = np.concatenate([np.zeros((N, 1)), np.log1p(_rm[:, :-1] / 12).cumsum(axis=1)], axis=1)
    del _rm
    dr = np.zeros(N); dc = np.zeros(N)
    for (py, (name, mat, cpn)) in RUNGS.items():
        T = yrs(T27, mat); y0p = np.maximum(curve(T + TOFF) + s27, YMIN)
        cc = (y0p if cpn is None else np.full(N, cpn)) / 100
        kk = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
        ii = np.clip(np.searchsorted(step_t, kk + TOFF), 0, len(step_t) - 1)
        iT = min(np.searchsorted(step_t, T + TOFF), len(step_t) - 1)
        grow_r = np.exp(_G[:, [iT]] - _G[:, ii]).sum(axis=1)
        dbase = 1 + (cc / 2) * ((1 + y0p[:, None] / 200) ** (2 * (T - kk)[None, :])).sum(axis=1)
        gy = yrs(mat, dt.date(py, 1, 1))
        relT = shifts[:, iT] - s27
        gapf = (1 + np.maximum(curve(.25) + s27 + relT, YMIN) / 100) ** gy
        gapf_base = (1 + np.maximum(curve(.25) + s27, YMIN) / 100) ** gy
        face = PAY / (dbase * gapf_base)
        dr += face * (1 + (cc / 2) * grow_r) * gapf
        dc += face * (1 + (cc / 2) * len(kk)) * gapf
    del _G
    np.savez_compressed(R08_OUT, R=R, floor_paid=floor_paid, V31=V31, V33=V33, L33=L33, bottom=bottom, top=top,
        S33=S33, S33m1=S33m1, S33m2=S33m2, shortfall=shortfall, delivered=delivered, delivered_rolled=dr,
        delivered_cash=dc, g2=g2, gift=gift, uncovered=uncovered, g_after=g_after, s27=s27, gap27=gap27,
        B0=B0)
    out["laura_kept_2033"] = {'''


def _run(rho, mu, outpath):
    src = MODEL.read_text()
    reps = [
        ('CURVE_CSV = ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv"',
         f'CURVE_CSV = pathlib.Path(r"{CURVE}")'),
        ('CURVE_DATE = "10/15/2026"', 'CURVE_DATE = "10/22/2026"'),
        ('TODAY = dt.date(2026, 10, 15)', 'TODAY = dt.date(2026, 10, 22)'),
        ('(HERE / "results.json")', f'(pathlib.Path(r"{outpath}.json"))'),
        ('EQ_MU, EQ_VOL, VT_FEE = np.log(1.07), 0.1678, 0.0006', f'EQ_MU, EQ_VOL, VT_FEE = np.log({mu}), 0.1678, 0.0006'),
        ('    z = rng.normal(size=(N, 5))', f'''    _t0 = yrs(TODAY, T28)
    _dy = np.stack([sh(_t0 + j + 1) - sh(_t0 + j) for j in range(5)], axis=1) / RATE_VOL
    z = {rho} * _dy + np.sqrt(1 - {rho}**2) * rng.normal(size=(N, 5))'''),
        ('    out["laura_kept_2033"] = {', EXTRA.replace("R08_OUT", f'r"{outpath}.npz"')),
    ]
    for old, new in reps:
        assert src.count(old) == 1, old
        src = src.replace(old, new)
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, str(MODEL), "exec"), {"__name__": "__main__", "__file__": str(MODEL)})


def paths(rho=0.0, mu="1.075"):
    """Per-path arrays for one scenario (cached). Every array has 200,000 entries, one per future."""
    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f"r08_rho{rho}_mu{mu}".replace(".", "p")
    if not pathlib.Path(f"{out}.npz").exists():
        _run(rho, mu, out)
    d = np.load(f"{out}.npz")
    return {k: d[k].astype(np.float64) for k in d.files}


if __name__ == "__main__":
    for rho, mu in ((0.0, "1.075"), (0.5, "1.075"), (0.5, "1.065")):
        p = paths(rho, mu)
        print(STAMP.format(mu=mu, rho=rho), "| top p50", round(np.median(p["top"])), "| gift p50", round(np.median(p["gift"])))
