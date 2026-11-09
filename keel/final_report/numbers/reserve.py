"""The operating reserve from 1 Jan 2033 (Keel, Mon 9 Nov 2026, night). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/reserve.py
Writes keel/final_report/numbers/results_reserve.json and prints the figures.

Why: Wharton's Section 3 asks the team to "recommend an appropriate operating reserve"; the case asks for "its size
and initial asset composition" and how "its composition should change, if at all, as the annual payments approach and
are made". The IPS: "From 2033 the Treasuries are the operating reserve." This values those Treasuries on each 1 January
from 2033 to 2042, on the register's one curve (6 Nov close), engine and instruments, in two worlds: rates follow
today's forward rates ('base'), and every reinvestment from 2027 earns 3 points less ('minus 3', the world Keel's
margin is sized for, NUMBERS section 2). Units are Keel's call (design A sized for minus 3, NUMBERS section 2).
Value of a rung on a date = its money already received, grown to that date at the rate locked when it arrived, plus its
flows still to come, discounted on the 6 Nov curve's forwards (a forward market value, not a forecast).
"""
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E   # noqa: E402

c = E.Curve(E.load_par())
I = E.instruments(c)
base = E.Reinvest(c, "base")
minus3 = E.Reinvest(c, "shift", s=0.03)
units = E.size_own_rung(I, minus3)            # Keel's call: every rung pays $50,000 even 3 points below forwards
units_plain = E.size_own_rung(I, base)        # the ladder with no margin


def rung_value(y, u, on, world):
    """Forward value on date `on` of rung y's units: flows received by `on` grown at the world's locked rates,
    flows after `on` discounted on the curve's forwards."""
    v = 0.0
    for d, a, _ in E.rung_flows(I[y], world):
        if d <= on:
            v += u * a * world.grow(d, on)
        else:
            v += u * a * c.P(d) / c.P(on)
    return v


def kind(y):
    return "iBond ETF" if y in E.FUNDS else "Treasury bond"


out = {"stamp": {"curve": E.CURVE_DAY, "run": "Mon 9 Nov 2026 night", "units": "design A sized for minus 3 (Keel's call)"}}
for wname, w in (("base", base), ("minus3", minus3)):
    rows = []
    for yr in E.YEARS:
        on = date(yr, 1, 1)
        live = [y for y in E.YEARS if y >= yr]
        vals = {y: rung_value(y, units[y], on, w) for y in live}
        before = sum(vals.values())
        pay = min(vals[yr], E.PAYMENT)
        surplus_this_rung = vals[yr] - E.PAYMENT
        after = before - vals[yr]
        owed_after = E.PAYMENT * (len(live) - 1)
        pv_owed_after = sum(E.PAYMENT * c.P(date(y, 1, 1)) / c.P(on) for y in live if y > yr)
        bonds_after = sum(v for y, v in vals.items() if y > yr and kind(y) == "Treasury bond")
        funds_after = sum(v for y, v in vals.items() if y > yr and kind(y) == "iBond ETF")
        rows.append({"date": on.isoformat(), "value_before_payment": before, "payment": pay,
                     "this_rung_over_50k": surplus_this_rung, "value_after_payment": after,
                     "payments_still_owed": owed_after, "forward_value_of_payments_still_owed": pv_owed_after,
                     "after_in_bonds": bonds_after, "after_in_ibond_etfs": funds_after,
                     "share_bonds_after": bonds_after / after if after else None})
    out[wname] = rows

# composition on 1 Jan 2033, rung by rung (base world), before the first payment
on = E.J33
comp = []
for y in E.YEARS:
    v = rung_value(y, units[y], on, base)
    inst = I[y]
    comp.append({"payment": y, "holding": inst.name, "type": kind(y), "pays_out": inst.end.isoformat(),
                 "months_before_payment": round(((date(y, 1, 1) - inst.end).days) / 30.44, 1),
                 "value_1jan2033": v, "units_jan2027": units[y], "cost_jan2027": units[y] * inst.price})
out["composition_1jan2033_base"] = comp
out["ladder_cost_jan2027_with_margin"] = E.cost(I, units)
out["ladder_cost_jan2027_no_margin"] = E.cost(I, units_plain)
out["margin_jan2027"] = E.cost(I, units) - E.cost(I, units_plain)
out["margin_value_1jan2033_if_rates_follow_forwards"] = sum(rung_value(y, units[y] - units_plain[y], E.J33, base)
                                                             for y in E.YEARS)
json.dump(out, open(HERE / "results_reserve.json", "w"), indent=1)

k = lambda x: f"${x:,.0f}"
print("ladder cost Jan 2027: with margin", k(out["ladder_cost_jan2027_with_margin"]), "no margin",
      k(out["ladder_cost_jan2027_no_margin"]), "margin", k(out["margin_jan2027"]),
      "| margin's value 1 Jan 2033 if forwards hold", k(out["margin_value_1jan2033_if_rates_follow_forwards"]))
for wname in ("base", "minus3"):
    print(f"\n{wname}: date | before | paid | rung over 50k | after | owed | fwd value owed | bonds share after")
    for r in out[wname]:
        sb = f"{r['share_bonds_after']:.0%}" if r["share_bonds_after"] is not None else "-"
        print(r["date"], k(r["value_before_payment"]), k(r["payment"]), k(r["this_rung_over_50k"]),
              k(r["value_after_payment"]), k(r["payments_still_owed"]), k(r["forward_value_of_payments_still_owed"]), sb)
print("\ncomposition 1 Jan 2033 (base):")
for r in comp:
    print(r["payment"], r["holding"], r["type"], r["pays_out"], r["months_before_payment"], k(r["value_1jan2033"]),
          k(r["cost_jan2027"]))
