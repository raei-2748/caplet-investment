"""The bond market's fall of 1994, replayed on a ladder shaped like Laura's (card Q232 rows 11-12; NUMBERS 9).
Keel, Tue 24 Nov 2026 (numbers owner's analysis worker). MODEL and Keel arithmetic: a history replay, never a plan
figure. NUMBERS.md is the only source of plan figures.

Run from the repo root:  python3 -I keel/final_report/numbers/replay_1994.py
Writes keel/final_report/numbers/results_replay_1994_2026-11-24.json and prints the figures.

Data: FRED daily constant-maturity Treasury par yields DGS1, DGS2, DGS3, DGS5, DGS7, DGS10, DGS20, DGS30 (the Treasury's
H.15 curve as FRED republishes it), 1 Dec 1993 to 31 Jan 1996, read at source 24 Nov 2026 and saved in
`data/fred_1994/` (URLs and the check against the 27 Sep 2026 mirror in `data/fred_1994/SOURCE.txt`). A day is used
when all eight tenors have a value (542 days in the files; 500 from 31 Dec 1993 to 29 Dec 1995).

Curve (the register's method A, `engine.Curve`, unchanged): each day's eight par yields are read as semiannual
bond-equivalent yields, interpolated linearly on a half-year grid from 0.5 to 30 years (below 1 year the 1-year yield is
held flat), bootstrapped to discount factors, and discount factors are interpolated log-linearly. Time is days / 365.25
from the valuation day. So the ladders are priced off an interpolated PAR curve, bootstrapped to a zero curve.

Two ladders, both held unchanged from the start day while their remaining terms shorten:
  A. "The payments' value" (card Q232 row 11's method): ten $50,000 payments due 1 Jan 2000..2009, six to fifteen years
     ahead on 31 Dec 1993 as Laura's are from 2027, each valued as a zero-coupon amount. Laura cannot hold zeros (STRIPS
     are not permitted), so this is the value of the promises, not of a holding.
  B. "A coupon ladder" (card Q232 row 12's method): ten Treasuries of $50,000 face each, maturing 31 Dec 1999..2008
     (six to fifteen years out), coupons paid 30 Jun and 31 Dec, each bought at par on the start day (coupon = that
     day's par rate to its maturity on the curve above, so the ten cost $500,000). Value = the bonds' full price on the
     day plus coupons already received, held as cash earning nothing. This is the shape of a holding.
Variants: the same two ladders set up on 31 Jan 1994 (the last close before the Fed's first move of 4 Feb 1994), with
payments and maturities six to fifteen years from that day; and a short-end sensitivity that adds DGS3MO and DGS6MO
from the 27 Sep 2026 mirror (`archive/rab/data/fred/`, not read at source today).

Not here: a world share index. MSCI's level service refuses dates before 1 Jan 1997 (read 24 Nov 2026), and the repo's
Shiller series is US shares only, so the replay leaves shares out.
"""
import calendar
import csv
import json
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402

DATA = HERE / "data/fred_1994"
MIRROR = E.ROOT / "archive/rab/data/fred"
TEN = {"DGS1": 1, "DGS2": 2, "DGS3": 3, "DGS5": 5, "DGS7": 7, "DGS10": 10, "DGS20": 20, "DGS30": 30}
SHORT = {"DGS3MO": .25, "DGS6MO": .5}
FACE = 50_000.0
LAST = date(1995, 12, 29)          # last trading day of 1995


def load(folder, series, lo="1993-12-01", hi="1996-01-31"):
    days = {}
    for col, t in series.items():
        for r in csv.DictReader(open(folder / f"{col}.csv")):
            d = r["observation_date"]
            if lo <= d <= hi and r[col] not in ("", "."):
                days.setdefault(d, {})[t] = float(r[col])
    return {date.fromisoformat(d): p for d, p in sorted(days.items()) if len(p) == len(series)}


def add_months_eom(d, m):
    """d moved by m months, keeping the month's end (31 Dec -> 30 Jun -> 31 Dec)."""
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    last = calendar.monthrange(y, mo)[1]
    eom = d.day == calendar.monthrange(d.year, d.month)[1]
    return date(y, mo, last if eom else min(d.day, last))


def t_years(d, day):
    return (d - day).days / 365.25


def zero_value(curve, day, pays):
    return sum(FACE * curve.df(t_years(p, day)) for p in pays if p > day)


class CouponLadder:
    """Ten $50,000-face Treasuries bought at par on `start`, one maturing on each date in `mats`."""

    def __init__(self, curve, start, mats):
        self.start, self.bonds = start, []
        for m in mats:
            cds, k = [], 0
            while True:
                d = add_months_eom(m, -6 * k)
                if d <= start:
                    break
                cds.append(d)
                k += 1
            cds.sort()
            ann = sum(curve.df(t_years(d, start)) for d in cds) / 2
            cpn = (1 - curve.df(t_years(m, start))) / ann          # par coupon, a yearly rate
            flows = [(d, FACE * cpn / 2) for d in cds]
            flows[-1] = (m, FACE * cpn / 2 + FACE)
            self.bonds.append({"maturity": m.isoformat(), "coupon_pct": cpn * 100, "flows": flows,
                               "cost": sum(a * curve.df(t_years(d, start)) for d, a in flows)})

    def value(self, curve, day):
        held = sum(a * curve.df(t_years(d, day)) for b in self.bonds for d, a in b["flows"] if d > day)
        cash = sum(a for b in self.bonds for d, a in b["flows"] if d <= day)
        return held + cash, held, cash

    def paid(self):
        cpns = sum(a for b in self.bonds for _, a in b["flows"]) - FACE * len(self.bonds)
        return {"principal": FACE * len(self.bonds), "coupons": cpns, "total": FACE * len(self.bonds) + cpns}


def duration(fn):
    """Effective duration of a value function of a par curve, from a 1bp parallel move of every par yield."""
    def at(shift):
        return fn(shift)
    v0, up, dn = at(0.0), at(1e-4), at(-1e-4)
    return (dn - up) / (2e-4 * v0)


def path_stats(days, vals, start_value, label):
    vals = np.asarray(vals)
    i_tr = int(np.argmin(vals))
    i_hi = int(np.argmax(vals[:i_tr + 1]))
    hi = vals[i_hi]
    after = np.where(vals[i_tr:] >= start_value)[0]
    i_back = i_tr + int(after[0]) if len(after) else None
    after_hi = np.where(vals[i_tr:] >= hi)[0]
    i_back_hi = i_tr + int(after_hi[0]) if len(after_hi) else None
    below = vals < start_value
    first_below = int(np.argmax(below)) if below.any() else None
    end94 = max(i for i, d in enumerate(days) if d.year == 1994)
    return {
        "label": label,
        "start": {"day": days[0].isoformat(), "value": float(vals[0])},
        "high_before_trough": {"day": days[i_hi].isoformat(), "value": float(hi)},
        "trough": {"day": days[i_tr].isoformat(), "value": float(vals[i_tr]),
                   "fall_from_start_pct": float(vals[i_tr] / start_value - 1) * 100,
                   "fall_from_high_pct": float(vals[i_tr] / hi - 1) * 100},
        "back_to_start": {"day": days[i_back].isoformat() if i_back is not None else None,
                          "first_day_below_start": days[first_below].isoformat() if first_below is not None else None,
                          "trading_days_below_start": int(below.sum()),
                          "trading_days_trough_to_back": (i_back - i_tr) if i_back is not None else None},
        "back_to_high": {"day": days[i_back_hi].isoformat() if i_back_hi is not None else None},
        "end_1994": {"day": days[end94].isoformat(), "value": float(vals[end94]),
                     "vs_start_pct": float(vals[end94] / start_value - 1) * 100},
        "end_1995": {"day": days[-1].isoformat(), "value": float(vals[-1]),
                     "vs_start_pct": float(vals[-1] / start_value - 1) * 100},
    }


def replay(curves, start, pays, mats, label):
    days = [d for d in curves if start <= d <= LAST]
    assert days[0] == start, (days[0], start)
    c0 = E.Curve(curves[start])
    # A. the payments' value
    zv = [zero_value(E.Curve(curves[d]), d, pays) for d in days]
    za = path_stats(days, zv, zv[0], "A: ten $50,000 payments valued as zeros (the payments' value)")
    tr = date.fromisoformat(za["trough"]["day"])
    za["unchanged_curve_on_trough_day"] = zero_value(c0, tr, pays)
    za["duration_on_start_day_years"] = duration(
        lambda s: zero_value(E.Curve(curves[start], shift=s), start, pays))
    za["pays"] = {"dates": [p.isoformat() for p in pays], "total": FACE * len(pays),
                  "note": "the dollars due do not move: $50,000 on each date, whatever the price did in between"}
    # B. the coupon ladder bought at par on the start day
    lad = CouponLadder(c0, start, mats)
    bv = [lad.value(E.Curve(curves[d]), d) for d in days]
    cb = path_stats(days, [v[0] for v in bv], bv[0][0],
                    "B: ten $50,000-face Treasuries bought at par, value with coupons received held as cash")
    trb = days.index(date.fromisoformat(cb["trough"]["day"]))
    cb["trough"]["bonds_only"] = bv[trb][1]
    cb["trough"]["coupons_received"] = bv[trb][2]
    cb["unchanged_curve_on_trough_day"] = lad.value(c0, days[trb])[0]
    ia = days.index(tr)
    cb["on_A_trough_day"] = {"day": tr.isoformat(), "value": bv[ia][0],
                             "vs_start_pct": (bv[ia][0] / bv[0][0] - 1) * 100}
    cb["duration_on_start_day_years"] = duration(
        lambda s: CouponLadder(c0, start, mats).value(E.Curve(curves[start], shift=s), start)[0])
    cb["bonds"] = [{k: v for k, v in b.items() if k != "flows"} for b in lad.bonds]
    cb["pays"] = {**lad.paid(), "note": "fixed at purchase: each bond pays its stated coupons and $50,000 at maturity"}
    # weekly check: Fridays only (or the week's last trading day), same paths
    wk = {}
    for i, d in enumerate(days):
        wk[d.isocalendar()[:2]] = i
    wi = sorted(wk.values())
    za["weekly_trough"] = {"day": days[wi[int(np.argmin([zv[i] for i in wi]))]].isoformat(),
                           "fall_from_start_pct": (min(zv[i] for i in wi) / zv[0] - 1) * 100}
    cb["weekly_trough"] = {"day": days[wi[int(np.argmin([bv[i][0] for i in wi]))]].isoformat(),
                           "fall_from_start_pct": (min(bv[i][0] for i in wi) / bv[0][0] - 1) * 100}
    return {"label": label, "days": len(days), "A_payments_value": za, "B_coupon_ladder": cb}


# ---------------------------------------------------------------- runs
curves = load(DATA, TEN)
S0 = date(1993, 12, 31)
base = replay(curves, S0, [date(y, 1, 1) for y in range(2000, 2010)], [date(y, 12, 31) for y in range(1999, 2009)],
              "base: start 31 Dec 1993 (card Q232's start), eight tenors 1-30 years read at source")
S1 = date(1994, 1, 31)
late_jan = replay(curves, S1, [date(y, 1, 31) for y in range(2000, 2010)], [date(y, 1, 31) for y in range(2000, 2010)],
                  "variant: start 31 Jan 1994 (late January, before the Fed's 4 Feb move), ladder set 6-15 years out")
curves_short = load(MIRROR, {**SHORT, **TEN})
short_end = replay(curves_short, S0, [date(y, 1, 1) for y in range(2000, 2010)],
                   [date(y, 12, 31) for y in range(1999, 2009)],
                   "sensitivity: base with DGS3MO and DGS6MO added from the 27 Sep 2026 mirror")

CARD = {"row_11": {"start_31Dec1993": 272_118, "high_12Jan1994": 279_053, "trough_4Nov1994": 237_959,
                   "fall_from_start_pct": -12.6, "fall_from_high_pct": -14.7, "unchanged_curve_4Nov1994": 288_189,
                   "back_to_start": "1995-05-04", "trading_days_below_start": 309, "end_1995_29Dec": 316_665},
        "row_12": {"trough_pct": -9.15, "trough_day": "1994-05-09", "end_1994_pct": -7.06,
                   "back_to_cost": "1995-04-20", "end_1995_pct": 13.8, "paid_total": 809_058,
                   "coupons_pct": [5.37, 6.16]}}

a, b = base["A_payments_value"], base["B_coupon_ladder"]


def grid_coupon_total(par):
    """Row 12's $809,058 again, with coupon times on an exact half-year grid (t = k/2) instead of calendar days."""
    c, tot = E.Curve(par), 0.0
    for n in range(6, 16):
        cpn = (1 - c.df(n)) / (sum(c.df(j / 2) for j in range(1, 2 * n + 1)) / 2)
        tot += FACE * cpn * n
    return FACE * 10 + tot


compare = {
    "row_11": {"start": a["start"]["value"] - CARD["row_11"]["start_31Dec1993"],
               "high": a["high_before_trough"]["value"] - CARD["row_11"]["high_12Jan1994"],
               "trough": a["trough"]["value"] - CARD["row_11"]["trough_4Nov1994"],
               "unchanged_curve": a["unchanged_curve_on_trough_day"] - CARD["row_11"]["unchanged_curve_4Nov1994"],
               "end_1995": a["end_1995"]["value"] - CARD["row_11"]["end_1995_29Dec"],
               "trough_day_same": a["trough"]["day"] == "1994-11-04",
               "back_to_start_same": a["back_to_start"]["day"] == CARD["row_11"]["back_to_start"],
               "days_below_same": a["back_to_start"]["trading_days_below_start"] == CARD["row_11"]["trading_days_below_start"]},
    "row_12": {"trough_pct_diff": b["trough"]["fall_from_start_pct"] - CARD["row_12"]["trough_pct"],
               "trough_day_same": b["trough"]["day"] == CARD["row_12"]["trough_day"],
               "back_to_cost_same": b["back_to_start"]["day"] == CARD["row_12"]["back_to_cost"],
               "paid_total_diff": b["pays"]["total"] - CARD["row_12"]["paid_total"],
               "paid_total_on_half_year_grid": grid_coupon_total(curves[S0]),
               "why_paid_total_differs": "the card set coupons on an exact half-year grid; this script uses calendar "
                                         "days / 365.25 (longest coupon 6.155% against 6.154%); the falls and dates "
                                         "do not change"},
}

out = {"label": "MODEL; Keel arithmetic on FRED H.15 par yields; a history replay, never a plan figure",
       "run": "Tue 24 Nov 2026", "script": "keel/final_report/numbers/replay_1994.py",
       "data": "keel/final_report/numbers/data/fred_1994/ (read at source 24 Nov 2026; SOURCE.txt)",
       "method": "engine.Curve method A on each day's eight par yields; time = days/365.25; daily marks on every day "
                 "with all eight tenors; weekly (last trading day of each week) as a check",
       "base": base, "late_january": late_jan, "short_end_sensitivity": short_end,
       "card_Q232": CARD, "base_minus_card": compare}
json.dump(out, open(HERE / "results_replay_1994_2026-11-24.json", "w"), indent=1, default=str)


def line(r, k):
    x = r[k]
    return (f"  {k[:1]}: start {x['start']['day']} ${x['start']['value']:,.0f}; high {x['high_before_trough']['day']} "
            f"${x['high_before_trough']['value']:,.0f}; trough {x['trough']['day']} ${x['trough']['value']:,.0f} "
            f"({x['trough']['fall_from_start_pct']:+.2f}% from start, {x['trough']['fall_from_high_pct']:+.2f}% from high); "
            f"back to start {x['back_to_start']['day']} ({x['back_to_start']['trading_days_below_start']} days below); "
            f"back to high {x['back_to_high']['day']}; end 1994 {x['end_1994']['vs_start_pct']:+.2f}%; "
            f"end 1995 ${x['end_1995']['value']:,.0f} ({x['end_1995']['vs_start_pct']:+.2f}%); "
            f"duration {x['duration_on_start_day_years']:.2f}y; weekly trough {x['weekly_trough']['day']} "
            f"{x['weekly_trough']['fall_from_start_pct']:+.2f}%")


for r in (base, late_jan, short_end):
    print(r["label"], f"({r['days']} days)")
    print(line(r, "A_payments_value"))
    print("     unchanged curve on trough day:", f"${r['A_payments_value']['unchanged_curve_on_trough_day']:,.0f}")
    print(line(r, "B_coupon_ladder"))
    bb = r["B_coupon_ladder"]
    print("     coupons", ", ".join(f"{x['coupon_pct']:.2f}%" for x in bb["bonds"]), "; cost",
          f"${sum(x['cost'] for x in bb['bonds']):,.2f}", "; pays", {k: round(v) for k, v in bb["pays"].items() if k != "note"})
print("base minus card:", json.dumps(compare, default=str))

# Keel's own figures, so a later edit that moves them fails loudly (set from the first run, 24 Nov 2026)
assert len(curves) == 542 and base["days"] == 500
assert round(a["start"]["value"]) == 272_118 and round(a["trough"]["value"]) == 237_959
assert round(a["high_before_trough"]["value"]) == 279_053 and round(a["unchanged_curve_on_trough_day"]) == 288_189
assert a["trough"]["day"] == "1994-11-04" and a["high_before_trough"]["day"] == "1994-01-12"
assert round(a["trough"]["fall_from_start_pct"], 1) == -12.6 and round(a["trough"]["fall_from_high_pct"], 1) == -14.7
assert a["back_to_start"]["day"] == "1995-05-04" and a["back_to_start"]["trading_days_below_start"] == 309
assert round(b["trough"]["fall_from_start_pct"], 2) == -9.15 and b["trough"]["day"] == "1994-05-09"
assert b["back_to_start"]["day"] == "1995-04-20" and round(b["duration_on_start_day_years"], 2) == 7.76
assert round(compare["row_12"]["paid_total_on_half_year_grid"]) == 809_058
