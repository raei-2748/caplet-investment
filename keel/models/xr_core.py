"""AI-generated (Claude Code), Tue 27 Oct 2026. MODEL, not a forecast or a promise.
The Model Suite's engine: market paths in, Laura's plan (Caplet XR, as in IPS V25) and five rival plans out.

STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA global equities 7.5% compound | VT fee 0.06%
Every assumption is numbered in ASSUMPTIONS.md (A01...); the code cites them as [Axx].

A "path" is a dict of numpy arrays with N rows (one per world) and M = 192 monthly columns, column m = the month
that ends m+1 months after 1 Jan 2027:
  s0   (N,)   parallel yield move (percentage points) from the curve date to 1 Jan 2027, the build day
  dy   (N,M)  monthly parallel yield move after the build (pp)                         [A04]
  eq   (N,M)  monthly log total return of world stocks before VT's fee                  [A06]
  cpi  (N,M)  monthly log change of US consumer prices                                  [A10]
  fx   (N,M)  monthly log change of Taiwan dollars per US dollar (optional)             [A11]
Months are counted from 1 Jan 2027: 2 Jan 2028 = 12, Jan 2031 = 48, 1 Jan 2033 = 72, 1 Jan 2042 = 180.
"""
import csv
import datetime as dt
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
CURVE_CSV = ROOT / "keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"
CURVE_DATE = dt.date(2026, 10, 22)
T0 = dt.date(2027, 1, 1)
M = 192
PAY, DEP27, DEP28 = 50_000.0, 300_000.0, 150_000.0
YMIN = 0.25                       # yields floored at 0.25% [A05]
EQ_G, EQ_VOL, VT_FEE = 0.075, 0.1678, 0.0006   # [A06] [A07]
PAY_M = [72 + 12 * j for j in range(10)]       # 1 Jan 2033 ... 1 Jan 2042

# payment year: (holding, maturity, coupon % or None = iBond fund treated as a par bond at its yield) [A03]
RUNGS = {
    2033: ("IBTM", dt.date(2032, 12, 15), None), 2034: ("IBTO", dt.date(2033, 12, 15), None),
    2035: ("IBTP", dt.date(2034, 12, 15), None), 2036: ("IBTQ", dt.date(2035, 12, 15), None),
    2037: ("IBTR", dt.date(2036, 12, 15), None), 2038: ("T 4.75% Feb-2037", dt.date(2037, 2, 15), 4.75),
    2039: ("T 4.50% May-2038", dt.date(2038, 5, 15), 4.50), 2040: ("T 4.375% Nov-2039", dt.date(2039, 11, 15), 4.375),
    2041: ("T 4.25% Nov-2040", dt.date(2040, 11, 15), 4.25), 2042: ("T 3.125% Nov-2041", dt.date(2041, 11, 15), 3.125),
}


def yrs(a, b):
    return (b - a).days / 365.25


H0 = yrs(CURVE_DATE, T0)          # 0.19 years from the curve date to the build


# ---------------------------------------------------------------- the curve [A01] [A02]
def load_par(date="10/22/2026"):
    tenor = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
             "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
    with open(CURVE_CSV) as fh:
        for r in csv.DictReader(fh):
            if r["Date"] == date:
                return {t: float(r[k]) for k, t in tenor.items()}
    raise KeyError(date)


PAR = load_par()
_X = np.array(sorted(PAR)); _Y = np.array([PAR[t] for t in _X])


def curve(t):
    """Par yield (%) at maturity t years, today's shape [A02]."""
    return np.interp(t, _X, _Y)


def bootstrap_cost(par=PAR, val=CURVE_DATE):
    """Cost on 1 Jan 2027 of the ten payments: bootstrapped zero curve, the method of ladder_pv.py [A01]."""
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); dfs = []
    for y in p:
        c = y / 2; dfs.append((1 - c * sum(dfs)) / (1 + c))
    g, lz = np.r_[0, grid], np.log(np.r_[1, dfs])
    f = lambda t: np.exp(np.interp(t, g, lz))
    return sum(PAY * f(yrs(val, dt.date(y, 1, 1))) for y in RUNGS) / f(yrs(val, T0))


COST_HEADLINE = bootstrap_cost()
PAY_T = np.array([yrs(T0, dt.date(y, 1, 1)) for y in RUNGS])          # 6.0 ... 15.0 years


def ladder_cost(s0):
    """Cost of the ten rungs on 1 Jan 2027 after a parallel move s0 (pp), zero view anchored to the headline."""
    s0 = np.atleast_1d(s0)
    z = np.maximum(curve(PAY_T)[None, :] + s0[:, None], YMIN) / 100
    c = PAY * ((1 + z / 2) ** (-2 * PAY_T)).sum(axis=1)
    z0 = curve(PAY_T) / 100
    return c * COST_HEADLINE / (PAY * ((1 + z0 / 2) ** (-2 * PAY_T)).sum())


def flat_ladder_cost(y):
    """Cost of ten $50k payments 6..15 years ahead at a flat yield y (%), semiannual compounding (history view)."""
    y = np.asarray(y, float)[..., None] / 100
    return PAY * ((1 + y / 2) ** (-2 * PAY_T)).sum(axis=-1)


# ---------------------------------------------------------------- yields along a path
def shift_path(p):
    """S[:, m] = total parallel move since the curve date, at month m (m = 0 is the build day)."""
    return np.concatenate([p["s0"][:, None], p["s0"][:, None] + np.cumsum(p["dy"], axis=1)], axis=1)


def bill(S, m):
    return np.maximum(curve(.25) + S[:, m], YMIN) / 100


def _coupon_growth(y0, cc, S, m0, T, s_ref, freeze=None):
    """1 + coupons reinvested to maturity, each in a zero at its date's yield (own yield + move since m0) [A08]."""
    k = np.arange(1, int(np.floor(T * 2 + 1e-9)) + 1) / 2
    idx = np.minimum(m0 + np.round(k * 12).astype(int), S.shape[1] - 1)
    if freeze is not None:
        idx = np.minimum(idx, freeze)
    yk = np.maximum(y0[:, None] + S[:, idx] - s_ref[:, None], YMIN) / 100
    return 1 + (cc / 200) * ((1 + yk / 2) ** (2 * (T - k)[None, :])).sum(axis=1), \
        1 + (cc / 200) * ((1 + y0[:, None] / 200) ** (2 * (T - k)[None, :])).sum(axis=1)


def ladder_delivery(S, freeze=None):
    """What each rung pays on its 1 January (N, 10). Each rung is sized on 1 Jan 2027 so that, if every coupon is
    reinvested at the build-day yield, it delivers exactly $50,000 [A03] [A08]. freeze = month after which yields
    are held (a 2033 projection)."""
    N = S.shape[0]; out = np.zeros((N, 10))
    for j, (py, (_, mat, cpn)) in enumerate(RUNGS.items()):
        T = yrs(T0, mat)
        y0 = np.maximum(curve(T) + S[:, 0], YMIN)
        cc = y0 if cpn is None else np.full(N, cpn)
        d, dbase = _coupon_growth(y0, cc, S, 0, T, S[:, 0], freeze)
        mm = min(int(round(T * 12)), S.shape[1] - 1)
        if freeze is not None:
            mm = min(mm, freeze)
        gap = yrs(mat, dt.date(py, 1, 1))
        g = (1 + bill(S, mm)) ** gap; gb = (1 + bill(S, 0)) ** gap
        out[:, j] = PAY * d * g / (dbase * gb)
    return out


# ---------------------------------------------------------------- Caplet XR (IPS V25) [A12]-[A17]
def caplet_xr(p, d28=DEP28, trap=0.0, top_share=0.5, bottom_cut=3700.0, lock=False, cush=0.0):
    """Laura's plan on each path. trap = L-10's coverage test: at least `trap` dollars stay behind for the payments
    before anything goes to the facility (0 = V25 as written). lock = the 28 Oct champion's "lock what you announce":
    in Jan 2031 the gift's half of VT moves into a Treasury maturing Dec 2032 [A18]. cush = WO-R10 rule G: a cushion
    on top of the projected gap, drawn from cash, then Laura's half, then the gift down to the bottom, never below [A19]."""
    S = shift_path(p); N = S.shape[0]
    cost27 = ladder_cost(p["s0"])
    gap27 = np.maximum(cost27 - DEP27, 0)
    L0 = np.maximum(DEP27 - cost27, 0)
    billg = np.cumprod(1 + np.maximum(curve(.25) + S[:, :-1], YMIN) / 1200, axis=1)   # bills, month by month
    L33 = L0 * billg[:, 71]
    # 2 Jan 2028: the deposit fills any rung gap first, then the floor (IBTM) and VT [A13]
    unfilled = np.maximum(gap27 - d28, 0)
    R = np.maximum(d28 - gap27, 0)
    t_f = yrs(dt.date(2028, 1, 2), dt.date(2032, 12, 15))
    y_f = np.maximum(curve(t_f) + S[:, 12], YMIN)
    ibtm = R / (1 + y_f / 200) ** (2 * t_f)
    d, db = _coupon_growth(y_f, y_f, S, 12, t_f, S[:, 12])
    floor_paid = R * d / db
    B0 = R - ibtm
    eqc = np.cumsum(p["eq"] - VT_FEE / 12, axis=1)            # log growth of $1 in VT from 1 Jan 2027
    grow = lambda a, b: np.exp(eqc[:, b - 1] - eqc[:, a - 1])  # growth from month a to month b
    V31 = B0 * grow(12, 48); V33 = B0 * grow(12, 72)
    # 2031: the range [A14]
    bottom = np.maximum(np.floor((R - bottom_cut) / 5000) * 5000, 0)
    top = R + top_share * V31
    # 1 Jan 2033: the reserve is re-matched once [A15]
    deliv = ladder_delivery(S); proj = ladder_delivery(S, freeze=72)
    short_true = np.maximum(10 * PAY - deliv.sum(axis=1), 0)
    S33 = np.maximum(10 * PAY - proj.sum(axis=1), 0)
    half = 0.5 * V33                                          # Laura's half (and, unlocked, the gift's half)
    if lock:
        t2 = yrs(dt.date(2031, 1, 1), dt.date(2032, 12, 15))
        gift_half = 0.5 * V31 * (1 + np.maximum(curve(t2) + S[:, 48], YMIN) / 200) ** (2 * t2)
    else:
        gift_half = half
    side = L33 + half; base = floor_paid + gift_half
    room = np.maximum(np.minimum(top, base - np.maximum(S33 - side, 0)) - bottom, 0)
    A = S33 + (np.minimum(cush, np.maximum(side - S33, 0) + room) if cush else 0)   # what is set aside in bills
    uncovered = np.maximum(A - side, 0)                       # the leftover, then Laura's half, then the gift
    raw = base - uncovered
    gift = np.clip(np.minimum(top, raw), 0, None)
    above_top = np.maximum(raw - top, 0)                      # the cap: anything above the top stays Laura's [A16]
    kept = np.maximum(side - A, 0) + above_top                # stays in VT, sellable any day [A16]
    S33 = A
    need = np.maximum(trap - kept, 0); held = np.minimum(need, gift); gift = gift - held
    # after 2033: the true gap beyond the 2033 projection comes from what Laura kept [A17]
    extra = np.maximum(short_true - S33, 0)
    kept42 = kept * grow(72, 180)
    miss_after = extra > kept42 + held + 1.0
    released = np.maximum(held - np.maximum(extra - kept42, 0), 0)
    payments_short = (unfilled > 1) | (uncovered > base + 1) | miss_after
    return {"cost27": cost27, "gap27": gap27, "unfilled": unfilled, "R": R, "floor_paid": floor_paid, "B0": B0,
            "V31": V31, "V33": V33, "bottom": bottom, "top": top, "gift": gift, "gift_later": gift + released,
            "S33": S33, "short_true": short_true, "kept33": kept, "held": held,
            "laura_2042": np.maximum(kept42 - extra, 0),
            "payments_short": payments_short, "payments_short_amt": np.where(payments_short,
                                                                            unfilled + np.maximum(extra - kept42 - held, 0), 0)}


# ---------------------------------------------------------------- rivals [A20]-[A26]
FUND = {"IEF": (7.0, 8.0), "TLT": (16.0, 20.0)}               # (duration, maturity point of its yield) [A21]
IMM_MARGIN = 1.05                                             # the immunising team keeps 5% above the payments' value [A24]


def _fund_ret(S, m, dur, tau):
    y = np.maximum(curve(tau) + S[:, m], YMIN) / 100
    dyy = (S[:, m + 1] - S[:, m]) / 100
    roll = dur * (curve(tau) - curve(tau - 1 / 12)) / 100      # roll-down along today's curve shape [A21]
    return y / 12 + roll - dur * dyy + 0.5 * dur ** 2 * dyy ** 2


def rival(p, kind, d28=DEP28, band=0.20):
    """Pool strategies that other teams are likely to file (all within Wharton's list: VT, Treasury ETFs, bills).
      balanced   60% VT / 40% IEF, rebalanced every January, for the whole 16 years
      glide      target-date path: 80% VT in 2027 sliding to 30% by Jan 2033, then 30/70
      bucket     70/30 to 2033; then three years of cheques in bills, the rest 50/50, bills refilled each January
      immunise   payments' value in a duration-matched IEF/TLT mix (no maturities), everything else in VT
      lock_late  100% VT until Jan 2032, then buy a Treasury ladder for the ten payments
    Gift (Jan 2033) = everything above the reserve the team keeps [A22]; the 2031 range = the team's own
    projection of that gift, plus or minus `band` [A23]."""
    S = shift_path(p); N = S.shape[0]
    eqr = np.exp(p["eq"] - VT_FEE / 12) - 1
    W = {"VT": np.full(N, 0.0), "IEF": np.zeros(N), "TLT": np.zeros(N), "BIL": np.zeros(N), "LAD": np.zeros(N)}
    lad_pay = np.zeros(N)                                    # per-payment amount the late ladder still owes
    gift = np.zeros(N); low = np.zeros(N); high = np.zeros(N); short_amt = np.zeros(N)

    def total():
        return W["VT"] + W["IEF"] + W["TLT"] + W["BIL"] + W["LAD"]

    def set_w(w):                                            # rebalance the liquid pot to weights w
        tot = W["VT"] + W["IEF"] + W["TLT"] + W["BIL"]
        for k in ("VT", "IEF", "TLT", "BIL"):
            W[k] = tot * w.get(k, 0.0)

    def target(m):
        yr = m // 12
        if kind == "balanced":
            return {"VT": .6, "IEF": .4}
        if kind == "glide":
            e = .8 - (.5 * min(yr, 6) / 6)
            return {"VT": e, "IEF": 1 - e}
        if kind == "bucket":
            return {"VT": .7, "IEF": .3} if m < 72 else None
        if kind == "lock_late":
            return {"VT": 1.0} if m < 60 else {"BIL": 1.0}
        return None

    def immunise_weights(m, n_left):
        t = np.arange(n_left) + (72 - m) / 12 if m < 72 else np.arange(n_left)
        t = np.maximum(t, 0.01)
        dfs = (1 + curve(t) / 200) ** (-2 * t)
        dur = (t * dfs).sum() / dfs.sum()
        a = np.clip((FUND["TLT"][0] - dur) / (FUND["TLT"][0] - FUND["IEF"][0]), 0, 1)   # IEF share
        return a

    def pv_future(m):                                         # value at month m of payments still due (zero view)
        tleft = np.array([(pm - m) / 12 for pm in PAY_M if pm >= m])
        if len(tleft) == 0:
            return np.zeros(N)
        z = np.maximum(curve(np.maximum(tleft, .01))[None, :] + S[:, [m]], YMIN) / 100
        return PAY * ((1 + z / 2) ** (-2 * tleft[None, :])).sum(axis=1)

    for m in range(M):
        if m == 0:
            W["VT"] += 0  # deposits below
            if kind == "immunise":
                a = immunise_weights(0, 10)
                W["IEF"] += DEP27 * a; W["TLT"] += DEP27 * (1 - a)
            else:
                W["BIL"] += DEP27; set_w(target(0))
        if m == 12:
            if kind == "immunise":
                W["VT"] += d28
            else:
                W["BIL"] += d28
        if m % 12 == 0 and m > 0 and m != 72 and kind != "immunise" and target(m) is not None:
            set_w(target(m))
        if kind == "immunise" and m % 12 == 0 and m > 0:      # keep the bond sleeve duration-matched
            n_left = sum(1 for pm in PAY_M if pm >= m)
            if n_left:
                a = immunise_weights(m, n_left); b = W["IEF"] + W["TLT"]
                W["IEF"], W["TLT"] = b * a, b * (1 - a)
        if m == 48:                                           # 2031: the team names a range [A23]
            if kind == "immunise":
                proj = W["VT"] * 1.075 ** 2 + (W["IEF"] + W["TLT"]) * (1 + curve(8) / 100) ** 2 \
                    - IMM_MARGIN * pv_future(48) * (1 + curve(2) / 100) ** 2
            elif kind == "lock_late":
                proj = total() * 1.075 - pv_future(48) * (1 + bill(S, 48)) ** 2
            else:
                er = {"balanced": .6 * .075 + .4 * curve(8) / 100, "glide": .4 * .075 + .6 * curve(8) / 100,
                      "bucket": .7 * .075 + .3 * curve(8) / 100}[kind]
                proj = total() * (1 + er) ** 2 - 10 * PAY
            proj = np.maximum(proj, 0)
            low, high = proj * (1 - band), proj * (1 + band)
        if m == 60 and kind == "lock_late":                    # Jan 2032: buy the payments' ladder
            c = pv_future(60); pot = total()
            frac = np.minimum(pot / c, 1.0)
            W["LAD"] = c * frac; lad_pay = PAY * frac
            for k in ("VT", "IEF", "TLT"):
                W[k] = 0.0
            W["BIL"] = pot - W["LAD"]
        if m == 72:                                           # 1 Jan 2033: the gift [A22]
            if kind == "immunise":                             # keep 1.05x the payments' value in bonds, give the rest
                tot = total(); gift = np.maximum(tot - IMM_MARGIN * pv_future(72), 0); rem = tot - gift
                a_ = immunise_weights(72, 10)
                W["VT"], W["IEF"], W["TLT"], W["BIL"] = 0 * rem, rem * a_, rem * (1 - a_), 0 * rem
            elif kind == "lock_late":
                gift = W["BIL"].copy(); W["BIL"] = 0.0
            else:
                tot = W["VT"] + W["IEF"] + W["TLT"] + W["BIL"]
                gift = np.maximum(tot - 10 * PAY, 0); rem = tot - gift
                if kind == "bucket":
                    W["BIL"] = np.minimum(rem, 3 * PAY); r = rem - W["BIL"]; W["VT"], W["IEF"], W["TLT"] = r * .5, r * .5, 0 * r
                else:
                    e = .6 if kind == "balanced" else .3
                    W["VT"], W["IEF"], W["TLT"], W["BIL"] = rem * e, rem * (1 - e), 0 * rem, 0 * rem
        if m in PAY_M:                                        # a cheque goes out
            if kind == "lock_late":
                W["LAD"] = np.maximum(W["LAD"] - lad_pay, 0)
                short_amt += PAY - lad_pay
            else:
                pot = W["VT"] + W["IEF"] + W["TLT"] + W["BIL"]
                short_amt += np.maximum(PAY - pot, 0)
                if kind == "bucket":
                    fromb = np.minimum(W["BIL"], PAY); W["BIL"] -= fromb; rest = PAY - fromb
                    liq = W["VT"] + W["IEF"]
                    W["VT"] -= rest * W["VT"] / np.maximum(liq, 1); W["IEF"] -= rest * W["IEF"] / np.maximum(liq, 1)
                    tot = W["VT"] + W["IEF"] + W["BIL"]           # refill the bucket to 3 cheques
                    nb = np.minimum(tot, 3 * PAY); r = tot - nb
                    W["BIL"], W["VT"], W["IEF"] = nb, r * .5, r * .5
                else:
                    sc = np.where(pot > 0, np.maximum(pot - PAY, 0) / np.maximum(pot, 1), 0)
                    for k in ("VT", "IEF", "TLT", "BIL"):
                        W[k] = W[k] * sc
                    if kind == "immunise":
                        pass
            for k in W:
                W[k] = np.maximum(W[k], 0)
        if m == M - 1:
            break
        # one month of returns
        W["VT"] = W["VT"] * (1 + eqr[:, m])
        W["IEF"] = W["IEF"] * (1 + _fund_ret(S, m, *FUND["IEF"]))
        W["TLT"] = W["TLT"] * (1 + _fund_ret(S, m, *FUND["TLT"]))
        W["BIL"] = W["BIL"] * (1 + bill(S, m) / 12)
    return {"gift": gift, "bottom": low, "top": high, "payments_short": short_amt > 1, "payments_short_amt": short_amt,
            "laura_2042": total()}


# ---------------------------------------------------------------- summaries
def pct(x, q):
    return float(np.percentile(x, q))


def summary(o, label=""):
    g = o["gift"]
    return {"label": label,
            "p_payment_short": round(float((o["payments_short_amt"] > 1000).mean()), 4),
            "p_payment_short_any": round(float(o["payments_short"].mean()), 4),
            "short_amt_p50_when_short": round(pct(o["payments_short_amt"][o["payments_short_amt"] > 1000], 50))
            if (o["payments_short_amt"] > 1000).any() else 0,
            "gift_p5": round(pct(g, 5)), "gift_p50": round(pct(g, 50)), "gift_p95": round(pct(g, 95)),
            "p_below_bottom": round(float((g < o["bottom"] - 1).mean()), 4),
            "p_top_reached": round(float((g >= o["top"] - 1000).mean()), 4),
            "bottom_p50": round(pct(o["bottom"], 50)), "top_p50": round(pct(o["top"], 50)),
            "laura_2042_p50": round(pct(o["laura_2042"], 50)),
            "p_any_promise_broken": round(float(((o["payments_short_amt"] > 1000) | (g < o["bottom"] - 1)).mean()), 4)}
