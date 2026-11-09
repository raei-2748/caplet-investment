"""Q20: a pooled book or Keel's margin for the ten payments (Keel, Tue 10 Nov 2026). MODEL, not a forecast.

Run:  cd keel/final_report/numbers && python3 -I pooled.py
Writes keel/final_report/numbers/results_pooled.json and prints the figures (about a minute).

Same curve (6 Nov 2026 close), instruments, reinvestment worlds and history windows as the register
(`engine.py`, `plan.py`, NUMBERS sections 1, 2, 3, 4). Nothing in engine.py or plan.py is changed.

Two ways to run the ten rungs:
  own   design A: each rung's coupons are reinvested in Treasuries maturing before its OWN payment (the Trading
        Notes' "reinvested coupons fund the rest"); any surplus carries to the next payment.
  pool  design B: every flow is held only until the NEXT payment due (later bonds' coupons pay earlier payments);
        any surplus carries to the next payment.
A "hybrid" runs a base book of ten rungs as `own` and a separate backstop of extra units of the same ten
Treasuries as `pool` (its flows pay whatever is next due and short).

Sizing at zero interest is a linear programme: at 0% every payment is met if and only if the cash that has arrived
by each 1 January covers the payments due by then (surplus carries free). Solved two ways: the engine's fixed-point
heuristic (`engine.size_matched`, which produced NUMBERS 2) and an exact vertex enumeration (10 variables, 20
constraints), so the register's figures can be checked against the true minimum.
"""
import itertools
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402
import plan as P     # noqa: E402

c = E.Curve(E.load_par())
I = E.instruments(c)
Y = E.YEARS
base = E.Reinvest(c)
zero = E.Reinvest(c, "zero")
shift = lambda s: E.Reinvest(c, "shift", s)
DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"
PLAIN_COST = None   # set below: $302,287, the ten at today's forward rates (NUMBERS 1)


# ---------------------------------------------------------------- delivery for every design

def own_amounts(units, world):
    """Money each rung's own flows reach on its own payment date (design A), uncapped."""
    return {y: units.get(y, 0.0) * sum(a * world.grow(d, date(y, 1, 1)) for d, a, _ in E.rung_flows(I[y], world))
            for y in Y}


def pool_buckets(units, world):
    """Money that reaches each payment date when every flow is held to the next payment due (design B)."""
    b = {y: 0.0 for y in Y}
    for y2, u in units.items():
        if u <= 0:
            continue
        for d, a, _ in E.rung_flows(I[y2], world):
            ny = E.next_payment(d)
            if ny in b:
                b[ny] += u * a * world.grow(d, date(ny, 1, 1))
    return b


def deliver(world, own=None, pool=None):
    """Pay each 1 January from: the base book run `own`, plus everything run `pool`, plus surplus carried forward at
    the rate locked that day. Returns {year: paid}."""
    oa = own_amounts(own, world) if own else {y: 0.0 for y in Y}
    pb = pool_buckets(pool, world) if pool else {y: 0.0 for y in Y}
    out, carry = {}, 0.0
    for y in Y:
        avail = oa[y] + pb[y] + carry
        out[y] = min(avail, E.PAYMENT)
        carry = max(avail - E.PAYMENT, 0.0) * (world.grow(date(y, 1, 1), date(y + 1, 1, 1)) if y < 2042 else 0.0)
    return out


def short(world, own=None, pool=None):
    return sum(E.PAYMENT - v for v in deliver(world, own, pool).values())


def cost(units):
    return sum(u * I[y].price for y, u in units.items())


def add(u1, u2):
    return {y: u1.get(y, 0.0) + u2.get(y, 0.0) for y in Y}


# ---------------------------------------------------------------- exact sizing at zero interest (vertex enumeration)

def zero_cash_matrix():
    """C[k, j]: cash from one unit of instrument j that reaches payment k when held to the next payment due, at 0%."""
    C = np.zeros((10, 10))
    for j, y2 in enumerate(Y):
        for d, a, _ in E.rung_flows(I[y2], zero):
            ny = E.next_payment(d)
            if ny in Y:
                C[Y.index(ny), j] += a
    return C


CZ = zero_cash_matrix()
CUM = np.cumsum(CZ, axis=0)                  # cash arrived by each 1 January, per unit
PRICE = np.array([I[y].price for y in Y])
_COMBOS = np.array(list(itertools.combinations(range(20), 10)), dtype=np.int16)


def lp_min_cost(lb, need_cum):
    """min PRICE.x  s.t.  CUM x >= need_cum (cumulative cash by each date), x >= lb. Exact, by vertex enumeration."""
    G = np.vstack([CUM, np.eye(10)])
    h = np.r_[need_cum, lb]
    best, bx = np.inf, None
    for s in range(0, len(_COMBOS), 20000):
        cb = _COMBOS[s:s + 20000]
        A = G[cb]                                   # (n, 10, 10)
        rhs = h[cb]                                 # (n, 10)
        det = np.linalg.det(A)
        ok = np.abs(det) > 1e-9
        if not ok.any():
            continue
        x = np.linalg.solve(A[ok], rhs[ok][..., None])[..., 0]
        feas = ((x @ CUM.T) >= need_cum - 1e-6).all(axis=1) & (x >= lb - 1e-6).all(axis=1)
        if not feas.any():
            continue
        xc = x[feas]
        cs = xc @ PRICE
        k = int(np.argmin(cs))
        if cs[k] < best:
            best, bx = float(cs[k]), xc[k]
    return {y: float(max(bx[i], 0.0)) for i, y in enumerate(Y)}


NEED = E.PAYMENT * np.arange(1, 11)


def lp_pooled(floor_units):
    lb = np.array([floor_units.get(y, 0.0) for y in Y])
    return lp_min_cost(lb, NEED)


def lp_sleeve(base_units):
    """Backstop: extra units, run pooled, that cover what the base book (run own) lacks at 0%."""
    oz = own_amounts(base_units, zero)
    need = NEED - np.cumsum([oz[y] for y in Y])
    return lp_min_cost(np.zeros(10), need)


# ---------------------------------------------------------------- NY Regulation 126 scenarios (11 NYCRR 95.10(d))

class NY7(E.Reinvest):
    """Reinvestment at TODAY's spot rate for the tenor (the 'level' curve, not forwards) plus the scenario's change
    at the date the money arrives; changes on the way down floored so the 5-year rate stays at 50% of its start
    (95.10(d)(2)), unless floor=False."""

    def __init__(self, curve, delta, floor=True):
        super().__init__(curve, "ny7")
        self.delta, self.floor = delta, floor
        self.z5 = -math.log(curve.df(5.0)) / 5.0

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        tau = (d2 - d1).days / 365.25
        z = -math.log(self.c.df(tau)) / tau
        dl = self.delta(max(E.yf(d1, E.J27), 0.0))
        if self.floor:
            dl = max(dl, -0.5 * self.z5)
        return math.exp(max(z + dl, 0.0) * tau)


NY = {"i_level": lambda t: 0.0,
      "ii_up_half_pt_a_year_10y": lambda t: 0.005 * min(t, 10),
      "iii_up_1pt_5y_then_back": lambda t: 0.01 * t if t <= 5 else (0.01 * (10 - t) if t <= 10 else 0.0),
      "iv_pop_up_3pt": lambda t: 0.03,
      "v_down_half_pt_a_year_10y": lambda t: -0.005 * min(t, 10),
      "vi_down_1pt_5y_then_back": lambda t: -0.01 * t if t <= 5 else (-0.01 * (10 - t) if t <= 10 else 0.0),
      "vii_pop_down_3pt": lambda t: -0.03}


# ---------------------------------------------------------------- the designs

plain = E.size_own_rung(I, base)
PLAIN_COST = cost(plain)
keel = E.size_own_rung(I, shift(0.03))
a_zero = E.size_own_rung(I, zero)

# The frozen WInS book's rung shape (NUMBERS 8g, at cost; IBTM's rung lot is 1,142 of its 4,503 shares at $21.65,
# the rest is the floor stand-in, Q17 row 26)
WINS_RUNG_COST = {2033: 1142 * 21.65, 2034: 23408.64, 2035: 22155.30, 2036: 20973.24, 2037: 19823.72,
                  2038: 19203.80, 2039: 18615.26, 2040: 16200.95, 2041: 15790.32, 2042: 14991.00}
_ws = sum(WINS_RUNG_COST.values())
WINS_SHARE = {y: v / _ws for y, v in WINS_RUNG_COST.items()}


def shape_units(total):
    return {y: WINS_SHARE[y] * total / I[y].price for y in Y}


def shape_pure():
    """Smallest uniform scale of the WInS shape that pays all ten at 0%, run pooled (bisection)."""
    lo, hi = PLAIN_COST, 2 * PLAIN_COST
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if short(zero, pool=shape_units(mid)) > 0.01 else (lo, mid)
    return shape_units(hi)


def shape_pure_own():
    lo, hi = PLAIN_COST, 2 * PLAIN_COST
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if short(zero, own=shape_units(mid)) > 0.01 else (lo, mid)
    return shape_units(hi)


sleeve_plain = lp_sleeve(plain)
sleeve_keel = lp_sleeve(keel)
DESIGNS = {
    # name: (description, own-run units, pool-run units, sizing note)
    "A_plain": ("Ten as written, sized at today's forward rates (NUMBERS 1)", plain, None, "own-rung, forwards"),
    "KEEL": ("Keel's call: design A sized for rates 3 points lower (NUMBERS 2)", keel, None, "own-rung, -3 pt"),
    "KEEL_run_pooled": ("Keel's call's units, every coupon paying the next payment due", None, keel,
                        "same units, pooled policy"),
    "A_zero": ("Design A sized so interest is never needed (NUMBERS 2)", a_zero, None, "own-rung, 0%"),
    "B_zero_engine": ("Pooled, no floor, sized at 0% (NUMBERS 2 design B)", None, E.size_matched(I, zero),
                      "engine heuristic"),
    "B_zero_lp": ("Pooled, no floor, sized at 0%, exact minimum", None, lp_pooled({}), "exact LP"),
}
for f in (0.25, 0.50, 0.75, 1.00):
    fl = {y: f * plain[y] for y in Y}
    DESIGNS[f"P{int(f*100)}_engine"] = (f"Pooled, each rung at least {f:.0%} of its plain size, sized at 0%",
                                        None, E.size_matched(I, zero, floor=fl), "engine heuristic")
    DESIGNS[f"P{int(f*100)}_lp"] = (f"Pooled, each rung at least {f:.0%} of its plain size, sized at 0%, exact",
                                    None, lp_pooled(fl), "exact LP")
DESIGNS["Pkeel_engine"] = ("Pooled, each rung at least Keel's call's size, sized at 0%", None,
                           E.size_matched(I, zero, floor=keel), "engine heuristic")
DESIGNS["Pkeel_lp"] = ("Pooled, each rung at least Keel's call's size, sized at 0%, exact", None, lp_pooled(keel),
                       "exact LP")
shp = shape_units(PLAIN_COST)
DESIGNS["Pshape_floor_lp"] = ("Pooled, each rung at least the WInS book's shape scaled to $302,287, sized at 0%, "
                              "exact", None, lp_pooled(shp), "exact LP")
DESIGNS["Pshape_pure"] = ("The WInS book's shape scaled up until it pays all ten at 0%, run pooled", None,
                          shape_pure(), "uniform scale")
DESIGNS["Ashape_pure"] = ("The WInS book's shape scaled up until it pays all ten at 0%, run own-rung", shape_pure_own(),
                          None, "uniform scale")
DESIGNS["H_plain"] = ("Hybrid: ten rungs at plain size run own-rung, plus a pooled backstop of extra units sized "
                      "at 0%", plain, sleeve_plain, "exact LP for the backstop")
DESIGNS["H_keel"] = ("Hybrid: ten rungs at Keel's call's size run own-rung, plus a pooled backstop sized at 0%",
                     keel, sleeve_keel, "exact LP for the backstop")


# ---------------------------------------------------------------- tests

def gift(m):
    d = P.run(c, margin=m)
    fl, mv, kp = float(d["floor"]), float(d["moved"]), float(d["kept33"])
    return {"margin_jan2027": m, "completion_jan2028": float(d["complete"]), "floor_payout": fl,
            "moved_half": mv, "stated_bottom": math.floor(fl * 0.959 / 5000) * 5000,
            "stated_top": math.floor((fl * 0.959 + mv * 0.975) / 5000) * 5000,
            "kept_half_1jan2033": kp, "vt_bought_jan2028": float(d["vt28"])}


windows = list(E.history_windows(DGS1, "DGS1"))
res = {"stamp": {"curve": E.CURVE_DAY, "run": "Tue 10 Nov 2026 (Sydney)", "engine": "engine.py, plan.py unchanged",
                 "history_windows": len(windows), "first_start": windows[0][0], "last_start": windows[-1][0]}}
designs_out = {}
hist_short = {}
for name, (desc, own, pool, note) in DESIGNS.items():
    allu = add(own or {}, pool or {})
    hs = []
    for st, m in windows:
        hs.append(short(E.Reinvest(c, "hist", mult=m), own, pool))
    hs = np.array(hs)
    hist_short[name] = hs
    total = cost(allu)
    row = {
        "description": desc, "sizing": note, "cost_jan2027": total, "over_keel": None,
        "rungs_bought": sum(1 for y in Y if allu[y] > 1),
        "units": {y: allu[y] for y in Y}, "rung_cost": {y: allu[y] * I[y].price for y in Y},
        "rung_vs_plain": {y: allu[y] / plain[y] for y in Y},
        "short_fall_for_good_1_2_3pt": [short(shift(s / 100), own, pool) for s in (1, 2, 3)],
        "short_zero": short(zero, own, pool),
        "short_zero_by_payment": {y: E.PAYMENT - v for y, v in deliver(zero, own, pool).items()},
        "ny126": {k: {"floored": short(NY7(c, f, True), own, pool), "unfloored": short(NY7(c, f, False), own, pool)}
                  for k, f in NY.items()},
        "history_share_any": float((hs > 1).mean()), "history_median": float(np.median(hs)),
        "history_1_in_20": float(np.percentile(hs, 95)), "history_worst": float(hs.max()),
        "history_worst_start": windows[int(hs.argmax())][0] if hs.max() > 1 else None,
        "surplus_jan2033_value_at_forwards": sum(v for v in deliver(base, own, pool).values()) - 0,  # filled below
        "gift": gift(total - PLAIN_COST),
    }
    # what Laura gets back at forwards: total delivered is capped at $500,000; the overflow is the last carry
    oa = own_amounts(own, base) if own else {y: 0.0 for y in Y}
    pb = pool_buckets(pool, base) if pool else {y: 0.0 for y in Y}
    carry, over = 0.0, 0.0
    for y in Y:
        avail = oa[y] + pb[y] + carry
        if y < 2042:
            carry = max(avail - E.PAYMENT, 0.0) * base.grow(date(y, 1, 1), date(y + 1, 1, 1))
        else:
            over = max(avail - E.PAYMENT, 0.0)
    row["overflow_1jan2042_at_forwards"] = over
    row["overflow_value_jan2027"] = over * c.P(date(2042, 1, 1))
    del row["surplus_jan2033_value_at_forwards"]
    designs_out[name] = row
for name in designs_out:
    designs_out[name]["over_keel"] = designs_out[name]["cost_jan2027"] - designs_out["KEEL"]["cost_jan2027"]
res["designs"] = designs_out
res["check_reproduces_NUMBERS_2"] = {
    "A_plain_cost": designs_out["A_plain"]["cost_jan2027"], "KEEL_cost": designs_out["KEEL"]["cost_jan2027"],
    "KEEL_short_zero": designs_out["KEEL"]["short_zero"], "KEEL_hist_share": designs_out["KEEL"]["history_share_any"],
    "P100_engine_cost": designs_out["P100_engine"]["cost_jan2027"],
    "engine_deliver_matches": abs(sum(E.PAYMENT - v for _, v in E.deliver(I, keel, zero, False))
                                  - designs_out["KEEL"]["short_zero"]) < 1e-6,
}


# ---------------------------------------------------------------- CANON tests: what each payment rests on

def sources(own, pool, world):
    """Per payment: share paid by its own instrument's flows (in an own-run book: all of them, grown; in a pooled
    book: only those arriving in the year before the payment), and by everything else."""
    oa = own_amounts(own, world) if own else {y: 0.0 for y in Y}
    out = {}
    for y in Y:
        mine = oa[y]
        if pool and pool.get(y, 0) > 0:
            mine += sum(pool[y] * a * world.grow(d, date(y, 1, 1)) for d, a, _ in E.rung_flows(I[y], world)
                        if E.next_payment(d) == y)
        out[y] = min(mine, E.PAYMENT) / E.PAYMENT
    return out


def fixed_cash_share(units):
    """A17/A18 test for a book run own-rung: the rung's own coupons and principal, counted at face (no interest on
    them), as a share of the $50,000 it pays."""
    return {y: units[y] * sum(a for _, a, _ in E.rung_flows(I[y], zero)) / E.PAYMENT for y in Y}


res["canon_tests"] = {
    "own_instrument_share_of_each_payment_at_forwards": {n: sources(DESIGNS[n][1], DESIGNS[n][2], base)
                                                         for n in ("KEEL", "P100_lp", "Pkeel_lp", "H_plain", "H_keel",
                                                                   "B_zero_lp", "P25_lp")},
    "fixed_cash_share_own_rung": {n: fixed_cash_share(DESIGNS[n][1]) for n in ("A_plain", "KEEL", "H_plain", "H_keel")},
    "pooled_2033_payment_from_later_bonds_at_forwards": {},
}
for n in ("P100_lp", "Pkeel_lp", "KEEL_run_pooled"):
    pool = DESIGNS[n][2]
    later = sum(pool[y2] * a * base.grow(d, E.J33) for y2 in Y if y2 >= 2038
                for d, a, _ in E.rung_flows(I[y2], base) if E.next_payment(d) == 2033)
    res["canon_tests"]["pooled_2033_payment_from_later_bonds_at_forwards"][n] = later


# ---------------------------------------------------------------- claim 3: Keel's call's shortfall windows in detail

def shiller_index():
    """Monthly US stock total-return index (Shiller; dividends to Jun 2023, then the Jun 2023 dividend held flat:
    MODEL extension, flagged)."""
    import csv
    keys, p, dv = [], [], []
    for r in csv.DictReader(open(E.ROOT / "keel/models/data/shiller_monthly.csv")):
        keys.append(r["Date"][:7])
        p.append(float(r["SP500"]))
        dv.append(float(r["Dividend"]))
    last_div = [d for d in dv if d > 0][-1]
    dv = [d if d > 0 else last_div for d in dv]
    p, dv = np.array(p), np.array(dv)
    tr = (p[1:] + dv[:-1] / 12) / p[:-1]
    return {k: v for k, v in zip(keys, np.r_[1.0, np.cumprod(tr)])}, "2023-06"


SH, SH_DIV_END = shiller_index()
SH_KEYS = sorted(SH)


def month_plus(key, m):
    yy, mm = int(key[:4]), int(key[5:7])
    yy, mm = divmod(yy * 12 + mm - 1 + m, 12)
    return f"{yy:04d}-{mm + 1:02d}"


gk = gift(designs_out["KEEL"]["cost_jan2027"] - PLAIN_COST)
vt28 = gk["vt_bought_jan2028"]
vfee = E.ASSUMPTIONS["vt_fee"]
detail = []
keel_pay_short = 0
for (st, m), hs in zip(windows, hist_short["KEEL"]):
    if hs <= 1:
        continue
    w = E.Reinvest(c, "hist", mult=m)
    paid = deliver(w, own=keel)
    shorts = {y: E.PAYMENT - v for y, v in paid.items() if E.PAYMENT - v > 1}
    keel_pay_short += len(shorts)
    # 2031 check: the same window's rates up to Jan 2031, then held at their Jan 2031 level
    m31 = m(E.J31)
    w31 = E.Reinvest(c, "hist", mult=lambda d, m=m, m31=m31: m(d) if d < E.J31 else m31)
    proj31 = short(w31, own=keel)
    kept = {}
    for y in shorts:
        k28, k31, ky = month_plus(st, 12), month_plus(st, 48), month_plus(st, 12 * (y - 2027))
        if ky in SH and k28 in SH:
            v = vt28 * SH[k31] / SH[k28] * (1 - vfee) ** 3 / 2 * SH[ky] / SH[k31] * (1 - vfee) ** (y - 2031)
            kept[y] = {"kept_half_value": v, "stock_month": ky, "after_div_data_end": ky > SH_DIV_END}
    detail.append({"start": st, "total_short": hs, "short_by_payment": shorts,
                   "projected_short_at_2031_check_if_rates_then_stay": proj31,
                   "kept_half_at_short_dates": kept,
                   "kept_half_covers_all": all(kept.get(y, {"kept_half_value": 0})["kept_half_value"] >= s
                                               for y, s in shorts.items()) if kept else None})
res["claim3_keel_shortfall_windows"] = {
    "n_windows": len(windows), "n_short": len(detail), "share": len(detail) / len(windows),
    "payments_short": keel_pay_short, "payments_tested": 10 * len(windows),
    "vt_bought_jan2028_central": vt28, "kept_half_1jan2033_central": gk["kept_half_1jan2033"],
    "windows": detail,
}

# ---------------------------------------------------------------- the lead's reading of P100: base run own-rung, extra pooled
p100 = DESIGNS["P100_lp"][2]
p100_extra = {y: max(p100[y] - plain[y], 0.0) for y in Y}
res["P100_holdings_run_as_hybrid"] = {
    "extra_units_over_plain": p100_extra,
    "short_zero": short(zero, own=plain, pool=p100_extra),
    "short_zero_by_payment": {y: E.PAYMENT - v for y, v in deliver(zero, own=plain, pool=p100_extra).items()},
    "note": "P100's holdings, but each rung's own coupons reinvested in its own rung and only the extra pooled",
}

# ---------------------------------------------------------------- gift ranges in the house model (200,000 paths)
house = {}
for n in ("KEEL", "P100_lp", "H_plain", "A_zero", "P50_lp"):
    m = designs_out[n]["cost_jan2027"] - PLAIN_COST
    h = P.house(c, margin=m)
    stated_top = h["floor"] * 0.959 + h["moved"] * 0.975
    house[n] = {"floor": P.pct(h["floor"]), "stated_top_unrounded": P.pct(stated_top), "kept33": P.pct(h["kept33"]),
                "payments_full_share": float(h["payments_full"].mean())}
res["house_gift_p5_p50_p95"] = house

(HERE / "results_pooled.json").write_text(json.dumps(res, indent=1, default=str))

# ---------------------------------------------------------------- print
k = lambda x: f"${x:,.0f}"
print("check:", {a: (round(b, 4) if isinstance(b, float) and b < 1 else round(b) if isinstance(b, float) else b)
                 for a, b in res["check_reproduces_NUMBERS_2"].items()})
hdr = "design | cost | vs Keel | bought | -1/-2/-3 | zero | hist any / 1in20 / worst (start) | NY7 vii fl/unfl, i | bottom / top / kept"
print(hdr)
for n, r in designs_out.items():
    g = r["gift"]
    print(f"{n:16s} {k(r['cost_jan2027'])} {r['over_keel']:+9,.0f} {r['rungs_bought']:2d} "
          f"{[round(x) for x in r['short_fall_for_good_1_2_3pt']]} {k(r['short_zero'])} | "
          f"{r['history_share_any']:.1%} {k(r['history_1_in_20'])} {k(r['history_worst'])} ({r['history_worst_start']}) | "
          f"{k(r['ny126']['vii_pop_down_3pt']['floored'])}/{k(r['ny126']['vii_pop_down_3pt']['unfloored'])} "
          f"{k(r['ny126']['i_level']['floored'])} | floor {k(g['floor_payout'])} {k(g['stated_bottom'])} / "
          f"{k(g['stated_top'])} / {k(g['kept_half_1jan2033'])} | overflow(2027$) {k(r['overflow_value_jan2027'])}")
for n in ("KEEL", "P100_lp", "Pkeel_lp", "Pshape_floor_lp", "Pshape_pure", "H_plain", "H_keel", "P25_lp", "P50_lp",
          "P75_lp", "B_zero_lp"):
    r = designs_out[n]
    print(n, "units", {y: round(r["units"][y]) for y in Y}, "x plain", {y: round(r["rung_vs_plain"][y], 2) for y in Y})
for n, v in res["canon_tests"]["own_instrument_share_of_each_payment_at_forwards"].items():
    print("own-instrument share", n, {y: round(x, 2) for y, x in v.items()})
for n, v in res["canon_tests"]["fixed_cash_share_own_rung"].items():
    print("fixed cash share (own rung)", n, {y: round(x, 2) for y, x in v.items()})
print("2033 payment from 2038-42 bonds' coupons (pooled, forwards):",
      {n: k(v) for n, v in res["canon_tests"]["pooled_2033_payment_from_later_bonds_at_forwards"].items()})
print("P100 holdings run as hybrid (own base, pooled extra): short at 0%",
      k(res["P100_holdings_run_as_hybrid"]["short_zero"]),
      {y: round(v) for y, v in res["P100_holdings_run_as_hybrid"]["short_zero_by_payment"].items()})
for n, v in house.items():
    print("house", n, {a: [round(x) for x in b] if isinstance(b, list) else round(b, 4) for a, b in v.items()})
c3 = res["claim3_keel_shortfall_windows"]
print(f"claim 3: {c3['n_short']} of {c3['n_windows']} windows short; payments short {c3['payments_short']} of "
      f"{c3['payments_tested']}")
for d in c3["windows"]:
    print(d["start"], k(d["total_short"]), {y: round(s) for y, s in d["short_by_payment"].items()},
          "2031 check", k(d["projected_short_at_2031_check_if_rates_then_stay"]),
          "kept", {y: round(v["kept_half_value"]) for y, v in d["kept_half_at_short_dates"].items()},
          "covers" if d["kept_half_covers_all"] else "NOT")
