"""NUMBERS.md section 8 items, on the same engine and curve (Keel, Mon 9 Nov 2026). MODEL, not a forecast.

Run from the repo root:  python3 -I keel/final_report/numbers/extras.py
Writes keel/final_report/numbers/results_extras_2026-11-06.json and prints the figures.

1. Per-rung reinvestment: where each rung's $50,000 comes from (principal, coupons, interest on coupons), and the
   flat reinvestment rate at which the ladder as written still pays all ten (the break-even).
2. A dated cost history of the ten payments from this one engine: every Treasury close of 2026 to 6 Nov.
3. The strongest rival on Caplet's own design: everything left in 2028 goes into VT, and the floor is bought only in
   Jan 2031 (same final mix as FINAL after its 2031 move). Same house paths and history windows as plan.py.
"""
import csv
import json
import math
import sys
from datetime import date, datetime
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402
import plan as P     # noqa: E402

out = {}
c = E.Curve(E.load_par())
I = E.instruments(c)
base = E.Reinvest(c)
units = E.size_own_rung(I, base)


class Flat(E.Reinvest):
    """Every cash flow earns one flat rate r from receipt until it is needed."""

    def __init__(self, curve, r):
        super().__init__(curve, "flat")
        self.r = r

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        return math.exp(self.r * (d2 - d1).days / 365.25)


# ---------------------------------------------------------------- 1. per-rung reinvestment
rows = {}
for y in E.YEARS:
    pay = date(y, 1, 1)
    fl = E.rung_flows(I[y], base)
    u = units[y]
    princ = sum(u * a for d, a, k in fl if k != "coupon")
    cpn = sum(u * a for d, a, k in fl if k == "coupon")
    grown = sum(u * a * base.grow(d, pay) for d, a, k in fl)
    zero_val = sum(u * a for d, a, k in fl)   # money earns nothing between receipt and payment
    m3 = E.Reinvest(c, "shift", 0.03)
    v3 = sum(u * a * m3.grow(d, pay) for d, a, k in fl)
    rows[y] = {"instrument": I[y].name, "cost_jan2027": u * I[y].price, "principal_or_payout": princ,
               "coupons": cpn, "interest_on_coupons_at_forwards": grown - princ - cpn,
               "share_of_50k_from_interest_on_interest": (grown - princ - cpn) / E.PAYMENT,
               "delivered_if_reinvested_3pt_below_forwards": v3, "delivered_if_money_earns_nothing": zero_val}
out["per_rung"] = rows


def worst_payment(r, carry=True):
    d = E.deliver(I, units, Flat(c, r), pooled=False)
    return min(v for _, v in d), sum(E.PAYMENT - v for _, v in d)


lo, hi = 0.0, 0.10
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (lo, mid) if worst_payment(mid)[0] >= E.PAYMENT - 0.5 else (mid, hi)
out["flat_break_even_rate"] = hi
out["flat_rate_table"] = {f"{r:.3f}": {"worst_payment": worst_payment(r)[0], "total_short": worst_payment(r)[1]}
                          for r in (0.0, 0.01, 0.02, 0.03, 0.035, 0.04, 0.045)}
out["forward_rates_for_reference"] = {"2027-2033": c.fwd(E.J27, E.J33), "2027-2037": c.fwd(E.J27, date(2037, 1, 1)),
                                      "2033-2042": c.fwd(E.J33, date(2042, 1, 1))}


# ---------------------------------------------------------------- 2. dated cost history (every 2026 close to 6 Nov)
class DatedCurve(E.Curve):
    def __init__(self, par, val):
        super().__init__(par)
        self.val = val

    def P(self, d, base=E.J27):
        t = lambda x: (x - self.val).days / 365.25
        return self.df(t(d)) / self.df(t(base))


days = {}
for fn in ("daily-treasury-rates_2026-10-23.csv", "daily-treasury-rates_2026-11-06.csv"):
    for r in csv.DictReader(open(E.ROOT / "competition/official_market_data" / fn)):
        d = datetime.strptime(r["Date"], "%m/%d/%Y").date()
        try:
            days[d] = {t: float(r[k]) for k, t in E.TENORS.items()}
        except (KeyError, ValueError):
            continue
hist = []
for d in sorted(days):
    cc = DatedCurve(days[d], d)
    ii = E.instruments(cc)
    uu = E.size_own_rung(ii, E.Reinvest(cc))
    u3 = E.size_own_rung(ii, E.Reinvest(cc, "shift", 0.03))
    hist.append({"date": d.isoformat(), "payments": E.ladder_cost(cc), "ten_held": E.cost(ii, uu),
                 "ten_held_with_margin_minus3": E.cost(ii, u3), "y10": days[d][10]})
pay = np.array([h["payments"] for h in hist])
held = np.array([h["ten_held"] for h in hist])
out["history"] = {
    "days": len(hist), "first": hist[0]["date"], "last": hist[-1]["date"],
    "payments_min": {"value": float(pay.min()), "date": hist[int(pay.argmin())]["date"]},
    "payments_max": {"value": float(pay.max()), "date": hist[int(pay.argmax())]["date"]},
    "ten_held_min": {"value": float(held.min()), "date": hist[int(held.argmin())]["date"]},
    "ten_held_max": {"value": float(held.max()), "date": hist[int(held.argmax())]["date"]},
    "days_payments_under_300k": int((pay < 300_000).sum()),
    "days_ten_held_under_300k": int((held < 300_000).sum()),
    "trade_days_7_8_oct": [h for h in hist if h["date"] in ("2026-10-07", "2026-10-08")],
    "ipsday_6_nov": hist[-1],
    "series": hist,
}

# ---------------------------------------------------------------- 3. the strongest rival on FINAL's own design
res = json.load(open(HERE / "results_2026-11-06.json"))
m3 = res["plan"]["margin_minus3"]["margin_jan2027_value"] if "plan" in res and "margin_minus3" in res["plan"] else None
if m3 is None:
    for v in res.values():
        if isinstance(v, dict) and "margin_minus3" in v:
            m3 = v["margin_minus3"]["margin_jan2027_value"]
share = E.ASSUMPTIONS["floor_share"]
keep_frac = (1 - share) / 2          # FINAL keeps half of VT to 2033: 13.35% of the 2028 money at cost
fee, vfee = E.ASSUMPTIONS["fund_fee"], E.ASSUMPTIONS["vt_fee"]


def draws(n=P.N, seed=P.SEED):
    rng = np.random.default_rng(seed)
    sv = E.ASSUMPTIONS["yield_vol"]
    d0 = rng.normal(0, sv * math.sqrt(E.yf(E.J27)), n)
    d1 = rng.normal(0, sv, n)
    d2 = rng.normal(0, sv * math.sqrt(3), n)
    mu, sd = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"]
    vt3 = np.exp(rng.normal(mu * 3, sd * math.sqrt(3), n))
    vt2 = np.exp(rng.normal(mu * 2, sd * math.sqrt(2), n))
    return d0, d1, d2, vt3, vt2


def rival(fin):
    """From plan.run's output: same R; all of it in VT 2028-2031; in Jan 2031 the same mix as FINAL after its move
    (86.65% Treasuries to late 2032, 13.35% VT kept to 2033)."""
    s = fin["setup"]
    vt31 = fin["R"] * VT3 * (1 - vfee) ** 3
    yM = np.maximum(s["fM"] + D0 + D1 + D2, 0.001)
    floor31 = (1 - keep_frac) * vt31 * np.exp(yM * s["tauM"]) * (1 - fee) ** s["tauM"]
    kept = keep_frac * vt31 * VT2 * (1 - vfee) ** 2
    return {"top": floor31, "kept33": kept, "total": floor31 + kept}


D0, D1, D2, VT3, VT2 = draws()
fin = P.run(c, m3, None, 150_000.0, D0, D1, D2, VT3, VT2)
riv = rival(fin)
out["rival_late_lock"] = {
    "what": "2028 money after completion all in VT; in Jan 2031 86.65% moved to Treasuries maturing late 2032, 13.35% kept",
    "house": {"final_top": P.pct(fin["top"]), "rival_top": P.pct(riv["top"]),
              "final_total": P.pct(fin["total"]), "rival_total": P.pct(riv["total"]),
              "share_rival_top_below_110k": float((riv["top"] < 110_000).mean()), "share_final_top_below_110k": float((fin["top"] < 110_000).mean()),
              "share_rival_top_below_final_top": float((riv["top"] < fin["top"]).mean()),
              "share_rival_total_below_final_total": float((riv["total"] < fin["total"]).mean()),
              "rival_top_p1": float(np.percentile(riv["top"], 1)), "final_top_p1": float(np.percentile(fin["top"], 1))},
}
w = P.shiller_windows()
VT3 = np.array([a for _, a, _ in w]); VT2 = np.array([b for _, _, b in w])
D0 = D1 = D2 = np.zeros(len(w))
fin_h = P.run(c, m3, None, 150_000.0, 0.0, 0.0, 0.0, VT3, VT2)
riv_h = rival(fin_h)
lo_i = int(np.argmin(riv_h["top"]))
out["rival_late_lock"]["history"] = {
    "windows": len(w), "final_top": P.pct(fin_h["top"]), "rival_top": P.pct(riv_h["top"]),
    "rival_top_lowest": {"value": float(riv_h["top"][lo_i]), "start": w[lo_i][0]},
    "final_top_lowest": float(np.min(fin_h["top"])),
    "share_rival_top_below_110k": float((riv_h["top"] < 110_000).mean()),
    "share_rival_top_below_final_top": float((riv_h["top"] < fin_h["top"]).mean()),
}
out["stamp"] = {"curve": E.CURVE_DAY, "margin_jan2027_value": m3, "run": "Mon 9 Nov 2026"}
json.dump(out, open(HERE / "results_extras_2026-11-06.json", "w"), indent=1, default=str)

k = lambda v: f"${v:,.0f}"
for y, r in rows.items():
    print(y, r["instrument"][:26].ljust(26), "cost", k(r["cost_jan2027"]), "coupons", k(r["coupons"]),
          "int-on-int", k(r["interest_on_coupons_at_forwards"]), f"({r['share_of_50k_from_interest_on_interest']:.1%})",
          "-3pt", k(r["delivered_if_reinvested_3pt_below_forwards"]), "zero", k(r["delivered_if_money_earns_nothing"]))
print("flat break-even", f"{out['flat_break_even_rate']:.3%}", out["flat_rate_table"], out["forward_rates_for_reference"])
h = out["history"]
print("history", h["days"], h["first"], h["last"], "payments", h["payments_min"], h["payments_max"],
      "held", h["ten_held_min"], h["ten_held_max"], "days<300k payments", h["days_payments_under_300k"],
      "held", h["days_ten_held_under_300k"])
print("7-8 Oct", [(x["date"], k(x["payments"]), k(x["ten_held"])) for x in h["trade_days_7_8_oct"]])
print("rival", json.dumps(out["rival_late_lock"], indent=1, default=lambda v: round(v)))
