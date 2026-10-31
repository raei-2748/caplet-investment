"""AI-generated (Claude Code), Sat 31 Oct 2026, Laura's Room (round 4 beat 6, Amara). MODEL.
(Keel is a simulated team, AI-written.) LR-08 "the bad naming day": today's Q12 (why not a safe ladder and the rest in
stocks?) read from the co-sponsor's chair. After naming day both plans lock what they name, so a co-sponsor holding
the range in 2032 cannot tell XR from A09. The only difference a co-sponsor ever sees is WHAT NUMBER Laura can name,
and how that number moves with the market she is fundraising in.
  xr    Caplet XR as V45 describes it: ladder, the 2028 floor (IBTM to Dec 2032), the floor's expected interest in VT,
        range named Jan 2031 with the lock and the $7,500 cushion (xr_core.caplet_xr(lock=True, cush=7500))
  a09   rival A09 at its strongest (rivals/A09.md): the same ladder; the 2028 money 80% VT / 20% IEF, rebalanced each
        January; in Jan 2031 a share f of the pot is locked in a Treasury to Dec 2032 (the bottom, rounded down to
        $5k), the rest goes to VT; top = locked face + half the rest; the promised half is locked on naming day as in
        XR; same cushion and coupon-gap rule. f is set so A09's MEDIAN bottom equals XR's: the same typical promise.
  Both bottoms carry L-13's 2031 mark (the projected coupon gap and cushion that Laura's own money can't cover come
  off the bottom before it is named; PR #84 review, 31 Oct). Then: the named bottom's tail (p1, p5, p10), how often it is under $125k / $100k, the bottom in the worlds where
  stocks fell most in 2028-31 (W-04: the same years co-sponsors give less), the gift and Laura's kept money (the
  price of XR's floor), and broken promises.
STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA world stocks 7.5% compound, 16.78% vol |
50,000 paths per world (house, storms, bootstrap) + every start month since 1871 (history) | engine keel/models/xr_core.py
unchanged | MODEL.
Run from repo root: python3 keel/rooms/lauras_room/LR-08_the_bad_naming_day.py   (numpy only; ~2 min)"""
import datetime as dt
import json
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "keel/models"))
import gens  # noqa: E402
import xr_core as x  # noqa: E402

N = 50_000
CUSH = 7_500.0
OUT = pathlib.Path(__file__).with_name("LR-08_results.json")


def a09(p, f, cush=CUSH, d28=x.DEP28):
    """Rival A09 on each path, written to mirror xr_core.caplet_xr(lock=True) line for line except 2028-31."""
    S = x.shift_path(p); n = S.shape[0]
    cost27 = x.ladder_cost(p["s0"]); gap27 = np.maximum(cost27 - x.DEP27, 0)
    L0 = np.maximum(x.DEP27 - cost27, 0)
    billg = np.cumprod(1 + np.maximum(x.curve(.25) + S[:, :-1], x.YMIN) / 1200, axis=1)
    L33 = L0 * billg[:, 71]
    unfilled = np.maximum(gap27 - d28, 0)
    R = np.maximum(d28 - gap27, 0)
    eqr = np.exp(p["eq"] - x.VT_FEE / 12) - 1
    vt, ief = 0.8 * R, 0.2 * R
    for m in range(12, 48):                                    # Jan 2028 -> Jan 2031, 80/20, rebalanced each January
        if m in (24, 36):
            t = vt + ief; vt, ief = 0.8 * t, 0.2 * t
        vt = vt * (1 + eqr[:, m]); ief = ief * (1 + x._fund_ret(S, m, *x.FUND["IEF"]))
    P31 = vt + ief
    t2 = x.yrs(dt.date(2031, 1, 1), dt.date(2032, 12, 15))
    g2 = (1 + np.maximum(x.curve(t2) + S[:, 48], x.YMIN) / 200) ** (2 * t2)   # 2031 -> Dec 2032 Treasury growth
    F = f * P31; face = F * g2
    bottom = np.maximum(np.floor(face / 5000) * 5000, 0)
    rest31 = (1 - f) * P31
    top = face + 0.5 * rest31
    eqc = np.cumsum(p["eq"] - x.VT_FEE / 12, axis=1)
    grow = lambda a, b: np.exp(eqc[:, b - 1] - eqc[:, a - 1])
    gift_half = 0.5 * rest31 * g2                              # promised half locked on naming day (as XR's lock)
    half = 0.5 * rest31 * grow(48, 72)                         # Laura's half stays in VT
    deliv = x.ladder_delivery(S); proj = x.ladder_delivery(S, freeze=72)
    short_true = np.maximum(10 * x.PAY - deliv.sum(axis=1), 0)
    S33 = np.maximum(10 * x.PAY - proj.sum(axis=1), 0)
    side = L33 + half; base = face + gift_half
    room = np.maximum(np.minimum(top, base - np.maximum(S33 - side, 0)) - bottom, 0)
    A = S33 + np.minimum(cush, np.maximum(side - S33, 0) + room)
    uncovered = np.maximum(A - side, 0)
    raw = base - uncovered
    gift = np.clip(np.minimum(top, raw), 0, None)
    kept = np.maximum(side - A, 0) + np.maximum(raw - top, 0)
    extra = np.maximum(short_true - A, 0)
    kept42 = kept * grow(72, 180)
    miss_after = extra > kept42 + 1.0
    short = (unfilled > 1) | (uncovered > base + 1) | miss_after
    S31 = np.maximum(10 * x.PAY - x.ladder_delivery(S, freeze=48).sum(axis=1), 0)
    u31 = ceil5(np.maximum(S31 + cush - L33 - 0.5 * rest31, 0))
    return {"bottom_premark": bottom, "bottom": np.maximum(bottom - u31, 0), "u31": u31, "top": top, "gift": gift, "kept33": kept, "laura_2042": np.maximum(kept42 - extra, 0),
            "payments_short": short, "payments_short_amt": np.where(short, unfilled + np.maximum(extra - kept42, 0), 0),
            "R": R}


def ceil5(a):
    return np.ceil(a / 5000) * 5000


def xr_marked(p, cush=CUSH):
    """XR with L-13's 2031 mark (keel/rooms/lab/L-13_slide_the_range/run.py: u31 = ceil5(max(S31 + C - L33 - 0.5 V31, 0)))
    applied to the named bottom: the projected 2033 coupon gap (yields frozen on naming day) plus the cushion, less
    what Laura's leftover cash and her half can cover, comes off the bottom before she names it. PR #84 review fix."""
    o = x.caplet_xr(p, lock=True, cush=cush)
    S = x.shift_path(p)
    cost27 = x.ladder_cost(p["s0"]); L0 = np.maximum(x.DEP27 - cost27, 0)
    billg = np.cumprod(1 + np.maximum(x.curve(.25) + S[:, :-1], x.YMIN) / 1200, axis=1)
    L33 = L0 * billg[:, 71]
    S31 = np.maximum(10 * x.PAY - x.ladder_delivery(S, freeze=48).sum(axis=1), 0)
    u31 = ceil5(np.maximum(S31 + cush - L33 - 0.5 * o["V31"], 0))
    o["bottom_premark"] = o["bottom"]; o["u31"] = u31; o["bottom"] = np.maximum(o["bottom"] - u31, 0)
    return o


def calibrate(p, target):
    lo, hi = 0.3, 1.0
    for _ in range(30):
        f = (lo + hi) / 2
        if np.median(a09(p, f)["bottom"]) < target:
            lo = f
        else:
            hi = f
    return round(hi, 4)


def stock_3y(p):
    """World stocks' total return Jan 2028 -> Jan 2031 (the three years before naming day)."""
    return np.exp(p["eq"][:, 12:48].sum(axis=1) - 36 * x.VT_FEE / 12) - 1


def report(o, r3, crash, crash5):
    b, g = o["bottom"], o["gift"]
    q = lambda a, v: round(float(np.percentile(a, v)))
    return {"bottom_p1_p5_p10_p50": [q(b, 1), q(b, 5), q(b, 10), q(b, 50)],
            "p_bottom_under_125k": round(float((b < 125_000).mean()), 4),
            "p_bottom_under_100k": round(float((b < 100_000).mean()), 4),
            "bottom_in_worst_tenth_of_2028_31_stocks_p50_min": [q(b[crash], 50), round(float(b[crash].min()))],
            "worst_5pct_2028_30_stocks_bottom_p50_gift_p50": [q(b[crash5], 50), q(g[crash5], 50)],
            "corr_bottom_with_2028_31_stocks": round(float(np.corrcoef(b, r3)[0, 1]), 3) if b.std() > 0 else 0.0,
            "top_p50": q(o["top"], 50),
            "gift_p5_p50_p95": [q(g, 5), q(g, 50), q(g, 95)],
            "laura_kept_2033_p50": q(o["kept33"], 50),
            "laura_gift_plus_kept_2033_p50": q(g + o["kept33"], 50),
            "laura_2042_mean": round(float(o["laura_2042"].mean())),
            "p_cheque_short_over_1k": round(float((o["payments_short_amt"] > 1000).mean()), 5),
            "n_gift_below_named_bottom": int((g < b - 1).sum()),
            "p_top_reached": round(float((g >= o["top"] - 1000).mean()), 4),
            "p_mark_cuts_bottom": round(float((o["u31"] > 0).mean()), 4),
            "bottom_premark_p1_p5_p50": [q(o["bottom_premark"], v) for v in (1, 5, 50)],
            "n_gift_below_premark_bottom": int((g < o["bottom_premark"] - 1).sum())}


def run():
    W = {"house": gens.lognormal(N), "storms": gens.regime(N), "bootstrap": gens.bootstrap(N), "history": gens.history()}
    res = {"stamp": __doc__.split("STAMP: ")[1].split("\nRun")[0].replace("\n", " "), "worlds": {}}
    f_house = None
    for name, p in W.items():
        xr = xr_marked(p)
        r3 = stock_3y(p)
        crash = r3 <= np.percentile(r3, 10); crash5 = r3 <= np.percentile(r3, 5)
        if f_house is None:                                     # calibrate once, in the house world, then hold f fixed
            f_house = calibrate(p, float(np.median(xr["bottom"])))
        ra = a09(p, f_house)
        res["worlds"][name] = {"n_paths": int(len(r3)),
                               "stocks_2028_31_worst_tenth_cutoff": round(float(np.percentile(r3, 10)), 3),
                               "xr": report(xr, r3, crash, crash5), "a09": report(ra, r3, crash, crash5)}
        print(name, json.dumps(res["worlds"][name], indent=1))
    res["a09_locked_share_f"] = f_house
    OUT.write_text(json.dumps(res, indent=1))
    print("f =", f_house, "->", OUT)


if __name__ == "__main__":
    run()
