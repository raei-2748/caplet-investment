"""AI-generated (Claude Code), Sat 31 Oct 2026, the Writing Room (round 4 beat 7). MODEL, not a forecast.
(Keel is a simulated team, AI-written.) Q12: why not a safe ladder and the rest in stocks?
The price of the floor, on the Model Suite's engine (keel/models/xr_core.py), unchanged; one rival added.
  XR    the suite's champion, caplet_xr(lock=True, cush=7500): the 2028 deposit fills any ladder gap, buys a Treasury
        repaying the rest in Dec 2032 (the floor) and puts the floor's expected interest in VT; 2031 range = floor up to
        floor + half VT, the promised half locked in Treasuries that day.
  A09   rivals/A09.md at its strongest, same promise shape: the same ladder; the 2028 deposit (after any gap) goes
        80% VT / 20% IEF, rebalanced each January; on 1 Jan 2031 it buys a Treasury repaying XR's floor (R) in Dec 2032
        if the pot can pay for it, else everything it has (the bottom); half of what's left is promised and locked the
        same day (the top), half stays Laura's. Cheque gap, cap and Laura's half work exactly as in caplet_xr.
  Both carry the suite's $7,500 cushion rule (rule G, [A19]); *_nocush rows drop it for both.
  A09h  A09 locking only half its 2031 pot as the bottom (more stocks, lower bottom), promising half the rest.
Worst 2028-30 = the 5% of paths with the lowest VT growth from Jan 2028 to Jan 2031.
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 LTCMA global equities 7.5% | 50,000 paths per world, gens.py seeds | MODEL.
Run from repo root: python3 keel/drafts/writing_room_2026-10-31/a09_price.py"""
import datetime as dt, json, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "keel/models"))
import gens, xr_core as x  # noqa: E402
from xr_core import curve, YMIN, yrs, PAY, DEP27, DEP28, VT_FEE  # noqa: E402

N = 50_000


def a09(p, lock_share=None, cush=7_500.0):
    S = x.shift_path(p)
    cost27 = x.ladder_cost(p["s0"]); gap27 = np.maximum(cost27 - DEP27, 0); L0 = np.maximum(DEP27 - cost27, 0)
    billg = np.cumprod(1 + np.maximum(curve(.25) + S[:, :-1], YMIN) / 1200, axis=1); L33 = L0 * billg[:, 71]
    unfilled = np.maximum(gap27 - DEP28, 0); R = np.maximum(DEP28 - gap27, 0)
    eqr = np.exp(p["eq"] - VT_FEE / 12) - 1
    vt, ief = .8 * R, .2 * R
    for m in range(12, 48):
        if m in (24, 36):
            t = vt + ief; vt, ief = .8 * t, .2 * t
        vt = vt * (1 + eqr[:, m]); ief = ief * (1 + x._fund_ret(S, m, *x.FUND["IEF"]))
    P31 = vt + ief
    t2 = yrs(dt.date(2031, 1, 1), dt.date(2032, 12, 15))
    g2 = (1 + np.maximum(curve(t2) + S[:, 48], YMIN) / 200) ** (2 * t2)   # $1 in a Dec-2032 Treasury bought 1 Jan 2031
    lock_cost = np.minimum(P31, R / g2) if lock_share is None else lock_share * P31
    bottom_paid = lock_cost * g2
    rest = P31 - lock_cost
    bottom = np.maximum(np.floor((bottom_paid - 3700.0) / 5000) * 5000, 0)   # XR's own bottom rule [A14]
    top = bottom_paid + 0.5 * rest
    gift_half = 0.5 * rest * g2                                          # the promised half, locked that day
    eqc = np.cumsum(p["eq"] - VT_FEE / 12, axis=1)
    grow = lambda a, b: np.exp(eqc[:, b - 1] - eqc[:, a - 1])
    half = 0.5 * rest * grow(48, 72)                                     # Laura's half stays in VT
    deliv = x.ladder_delivery(S); proj = x.ladder_delivery(S, freeze=72)
    short_true = np.maximum(10 * PAY - deliv.sum(axis=1), 0); S33 = np.maximum(10 * PAY - proj.sum(axis=1), 0)
    side = L33 + half; base = bottom_paid + gift_half
    room = np.maximum(np.minimum(top, base - np.maximum(S33 - side, 0)) - bottom, 0)
    A = S33 + np.minimum(cush, np.maximum(side - S33, 0) + room)          # the same cushion rule as XR [A19]
    uncovered = np.maximum(A - side, 0); raw = base - uncovered
    gift = np.clip(np.minimum(top, raw), 0, None)
    kept = np.maximum(side - A, 0) + np.maximum(raw - top, 0)
    extra = np.maximum(short_true - A, 0); kept42 = kept * grow(72, 180)
    short = (unfilled > 1) | (uncovered > base + 1) | (extra > kept42 + 1)
    return {"gift": gift, "bottom": bottom, "top": top, "payments_short": short,
            "payments_short_amt": np.where(short, unfilled + np.maximum(extra - kept42, 0), 0),
            "laura_2042": np.maximum(kept42 - extra, 0), "P31": P31, "R": R}


def row(o, bad):
    s = x.summary(o)
    s.update({"gift_mean": round(float(o["gift"].mean())), "laura_2042_mean": round(float(o["laura_2042"].mean())),
              "bottom_p5": round(float(np.percentile(o["bottom"], 5))),
              "worst5_2028_30": {"bottom_p50": round(float(np.median(o["bottom"][bad]))),
                                 "gift_p50": round(float(np.median(o["gift"][bad]))),
                                 "gift_p5": round(float(np.percentile(o["gift"][bad], 5)))}})
    return s


def main():
    W = {"lognormal": gens.lognormal(N), "regime": gens.regime(N), "bootstrap": gens.bootstrap(N)}
    out = {"stamp": __doc__.split("STAMP: ")[1].split(" | MODEL")[0]}
    for name, p in W.items():
        eqc = np.cumsum(p["eq"], axis=1); g2830 = eqc[:, 47] - eqc[:, 11]
        bad = g2830 <= np.percentile(g2830, 5)
        xr = x.caplet_xr(p, lock=True, cush=7_500); a = a09(p); ah = a09(p, lock_share=.5)
        r = {"XR": row(xr, bad), "A09": row(a, bad), "A09h": row(ah, bad),
             "XR_nocush": row(x.caplet_xr(p, lock=True), bad), "A09_nocush": row(a09(p, cush=0.0), bad)}
        r["A09_bottom_below_XR_floor"] = round(float((a["bottom"] < xr["bottom"] - 1).mean()), 4)
        r["A09_bottom_below_XR_floor_by_10k"] = round(float((a["bottom"] < xr["bottom"] - 10_000).mean()), 4)
        r["price_of_floor_gift_p50"] = r["A09"]["gift_p50"] - r["XR"]["gift_p50"]
        r["price_of_floor_gift_mean"] = r["A09"]["gift_mean"] - r["XR"]["gift_mean"]
        r["price_of_floor_laura2042_mean"] = r["A09"]["laura_2042_mean"] - r["XR"]["laura_2042_mean"]
        r["vt_2028_30_worst5_total_return"] = round(float(np.exp(np.percentile(g2830, 5)) - 1), 3)
        out[name] = r
        print(name, json.dumps({k: r[k] for k in r if k.startswith(("price", "A09_b", "vt"))}))
        for k in ("XR", "A09", "A09h", "XR_nocush", "A09_nocush"):
            s = r[k]; print(f"  {k:10} short {s['p_payment_short']:.4f} gift p5/p50/mean {s['gift_p5']}/{s['gift_p50']}/{s['gift_mean']}"
                          f" bottom p5/p50 {s['bottom_p5']}/{s['bottom_p50']} top p50 {s['top_p50']} top-reached {s['p_top_reached']}"
                          f" below-bottom {s['p_below_bottom']} L42 mean {s['laura_2042_mean']} worst5 {s['worst5_2028_30']}")
    pathlib.Path(__file__).with_name("a09_price_results.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
