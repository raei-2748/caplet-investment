"""Caplet's FINAL plan from 2027 to 2033 on the engine's curve (Keel, Mon 9 Nov 2026). MODEL, not a forecast.

The order is the IPS's own: the $300,000 buys the ten Treasuries in Jan 2027; in Jan 2028 the $150,000 first completes
the ladder, then "most" of what is left buys the floor (a Treasury fund maturing late 2032, IBTM) and "the rest" buys
VT; before the 2031 co-sponsor meetings half of VT moves into Treasuries (IBTM again, maturing late 2032); the other
half is promised to no one. The 2031 range runs from the floor's payout to the floor plus the moved half.

Worlds:
  house    VT log returns normal, median growth 7.5% a year (J.P. Morgan 2027, global equities), s.d. 16.78%
           (J.P. Morgan 2026, AC World); Treasury yields move in parallel, s.d. 0.9 points a year (MODEL assumption);
           stocks and yields independent. 200,000 paths, seed 2033.
  history  VT replaced by US stocks with dividends (Shiller monthly, every 3-year and 5-year window since 1871);
           yields stay on today's forward curve.
"""
import csv
import math
from datetime import date

import numpy as np

import engine as E

SEED, N = 2033, 200_000


def setup(curve):
    insts = E.instruments(curve)
    base = E.Reinvest(curve)
    units = E.size_own_rung(insts, base)
    c27 = E.cost(insts, units)
    bump = 0.0001
    up = E.Curve(curve.par, shift=bump)
    dn = E.Curve(curve.par, shift=-bump)
    dur_l = (E.ladder_cost(dn) - E.ladder_cost(up)) / (2 * bump * E.ladder_cost(curve))
    # build order: longest rungs first (they move most with yields), so any part still unbought in Jan 2027 is the
    # 2033 rung, completed in Jan 2028 at that day's prices; its sensitivity is about its years to run
    tail_dur = (E.yf(date(2033, 1, 1), E.J28))
    f01 = curve.fwd(E.J27, E.J28)
    fF = curve.fwd(E.J28, date(2032, 12, 15))
    fM = curve.fwd(E.J31, date(2032, 12, 15))
    return dict(c27=c27, dur_l=dur_l, tail_dur=tail_dur, f01=f01, fF=fF, fM=fM,
                tauF=E.yf(date(2032, 12, 15), E.J28), tauM=E.yf(date(2032, 12, 15), E.J31))


def run(curve, margin=0.0, share=None, deposit=150_000.0, d0=None, d1=None, d2=None, vt3=None, vt2=None):
    """Vectorised plan. margin: extra ladder cost (1 Jan 2027 value) bought with the 2028 deposit's first dollars.
    d0, d1, d2: parallel yield changes now->Jan 2027, Jan 2027->Jan 2028, Jan 2028->Jan 2031 (arrays or floats).
    vt3, vt2: VT growth factors Jan 2028->Jan 2031 and Jan 2031->Jan 2033 (before the fund fee)."""
    s = setup(curve)
    share = E.ASSUMPTIONS["floor_share"] if share is None else share
    fee, vfee = E.ASSUMPTIONS["fund_fee"], E.ASSUMPTIONS["vt_fee"]
    d0 = np.asarray(0.0 if d0 is None else d0, float)
    d1 = np.asarray(0.0 if d1 is None else d1, float)
    d2 = np.asarray(0.0 if d2 is None else d2, float)
    c27 = s["c27"] * np.exp(-s["dur_l"] * d0)                   # the ten at Jan 2027 prices
    short27 = np.maximum(c27 - 300_000, 0.0)
    left27 = np.maximum(300_000 - c27, 0.0)
    r01 = np.maximum(s["f01"] + d0, 0.001)
    # completion in Jan 2028: the unbought tail (plus the margin), re-priced for a year of carry and the 2027 move
    complete = (short27 * np.exp(-s["tail_dur"] * d1) + margin * np.exp(-s["dur_l"] * d1)) * np.exp(r01)
    R = deposit + left27 * np.exp(r01) - complete
    payments_full = R >= 0
    R = np.maximum(R, 0.0)
    yF = np.maximum(s["fF"] + d0 + d1, 0.001)
    floor = share * R * np.exp(yF * s["tauF"]) * (1 - fee) ** s["tauF"]
    vt28 = (1 - share) * R
    vt3 = np.asarray(np.exp(math.log(1.075) * 3) if vt3 is None else vt3, float)
    vt2 = np.asarray(np.exp(math.log(1.075) * 2) if vt2 is None else vt2, float)
    vt31 = vt28 * vt3 * (1 - vfee) ** 3
    yM = np.maximum(s["fM"] + d0 + d1 + d2, 0.001)
    moved = vt31 / 2 * np.exp(yM * s["tauM"]) * (1 - fee) ** s["tauM"]
    kept33 = vt31 / 2 * vt2 * (1 - vfee) ** 2
    all_t = R * np.exp(yF * s["tauF"]) * (1 - fee) ** s["tauF"]
    return dict(complete=complete, R=R, payments_full=payments_full, floor=floor, vt28=vt28, vt31=vt31,
                moved=moved, top=floor + moved, kept33=kept33, total=floor + moved + kept33, all_t=all_t, setup=s)


def house(curve, margin=0.0, share=None, deposit=150_000.0, n=N, seed=SEED):
    rng = np.random.default_rng(seed)
    sv = E.ASSUMPTIONS["yield_vol"]
    t0 = E.yf(E.J27)
    d0 = rng.normal(0, sv * math.sqrt(t0), n)
    d1 = rng.normal(0, sv, n)
    d2 = rng.normal(0, sv * math.sqrt(3), n)
    mu, sd = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"]
    vt3 = np.exp(rng.normal(mu * 3, sd * math.sqrt(3), n))
    vt2 = np.exp(rng.normal(mu * 2, sd * math.sqrt(2), n))
    return run(curve, margin, share, deposit, d0, d1, d2, vt3, vt2)


def shiller_windows(path=None):
    """Growth factors of US stocks with dividends over every 3-year window and the 2 years after it."""
    path = path or (E.ROOT / "keel/models/data/shiller_monthly.csv")
    p, dv, keys = [], [], []
    for r in csv.DictReader(open(path)):
        if r["Date"] >= "2023-07":
            break
        p.append(float(r["SP500"]))
        dv.append(float(r["Dividend"]))
        keys.append(r["Date"][:7])
    p, dv = np.array(p), np.array(dv)
    tr = (p[1:] + dv[:-1] / 12) / p[:-1]
    idx = np.r_[1.0, np.cumprod(tr)]
    out = []
    for i in range(len(idx) - 60):
        out.append((keys[i], idx[i + 36] / idx[i], idx[i + 60] / idx[i + 36]))
    return out


def history(curve, margin=0.0, share=None, deposit=150_000.0):
    w = shiller_windows()
    vt3 = np.array([a for _, a, _ in w])
    vt2 = np.array([b for _, _, b in w])
    res = run(curve, margin, share, deposit, vt3=vt3, vt2=vt2)
    res["starts"] = [k for k, _, _ in w]
    return res


def pct(a, qs=(5, 50, 95)):
    return [float(np.percentile(a, q)) for q in qs]
