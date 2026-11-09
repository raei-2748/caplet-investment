"""The operating reserve from 1 Jan 2033 (Keel; Mon 9 Nov 2026 night, re-run Tue 10 Nov on the escrow standard). MODEL.

Run from the repo root:  python3 -I keel/final_report/numbers/reserve.py [--design KEEL]
Writes keel/final_report/numbers/results_reserve_2026-11-10.json (the Mon 9 Nov results_reserve.json is kept).

Why: Wharton's Section 3 asks the team to "recommend an appropriate operating reserve"; the case asks for "its size
and initial asset composition" and how "its composition should change, if at all, as the annual payments approach and
are made". The IPS: "From 2033 the Treasuries are the operating reserve."

Design (completion.py): the call H_plain = the ten rungs at plain size, each rung's own coupons reinvested for its own
payment (the Trading Notes), plus the pooled backstop bought with the 2028 deposit (extra face in IBTQ, IBTR and the five
T-bonds), whose coupons and principal wait in a short-term Treasury ETF for the next payment due; any money above a
payment carries forward in that ETF. Worlds: 'base' = today's forward rates; 'zero' = nothing earns interest from 2027.
Value on a date = money already received, grown at the rate locked when it arrived, plus flows still to come, discounted
on the 6 Nov curve's forwards (a forward market value, not a forecast).

Tue 10 Nov afternoon (bond desk check, findings 4, 5, 8, 12): the release test counts money already received at its
value on the release day and then lets nothing earn interest (0%), or lose the ETF's fee (the design's own standard,
completion.WAIT_FEE); money left after 2042 is put into 2033 money at each world's own rates (completion.in_2033_money);
the composition shows IBTM's payout (15 Dec 2032) as cash in the short Treasury ETF; the backstop's 1 Jan 2033 value is
read from the composition (reserve before the payment less the own rungs), not carried from its 2027 cost.
"""
import math
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E       # noqa: E402
import completion as C   # noqa: E402

NAME = C.design_arg()
c, I, Y = C.c, C.I, C.Y
D = C.design(NAME)
OWN, POOL = D["own"], D["pool"] or {}


def kind(y):
    return "iBond ETF" if y in E.FUNDS else "Treasury bond"


def own_value(y, u, on, world):
    """Rung y's own-run units on date `on`: flows received grown at locked rates, later flows at forwards."""
    v = 0.0
    for d, a, _ in E.rung_flows(I[y], world):
        v += u * a * (world.grow(d, on) if d <= on else c.P(d) / c.P(on))
    return v


def pool_future(on, world):
    """The backstop's holdings on `on`: its flows still to come, at forwards (by instrument)."""
    out = {}
    for y, u in POOL.items():
        if u > 0.5:
            out[y] = sum(u * a * c.P(d) / c.P(on) for d, a, _ in E.rung_flows(I[y], world) if d > on)
    return out


def run(world):
    paid, avail, carry, left = C.ledger(world, OWN, POOL)
    oa = C.own_amounts(OWN, world)
    pb = C.pool_buckets(POOL, world)
    rows, cin = [], 0.0
    for yr in Y:
        on = date(yr, 1, 1)
        etf_before = pb[yr] + cin                       # backstop money and carried surplus, waiting in the ETF
        live = [y for y in Y if y >= yr]
        rungs = {y: own_value(y, OWN[y], on, world) for y in live}
        back = pool_future(on, world)
        before = sum(rungs.values()) + sum(back.values()) + etf_before
        own_pay = min(oa[yr], E.PAYMENT)
        from_etf = paid[yr] - own_pay
        etf_after = carry[yr]
        after_bonds = sum(v for y, v in rungs.items() if y > yr and kind(y) == "Treasury bond") + \
            sum(v for y, v in back.items() if kind(y) == "Treasury bond")
        after_funds = sum(v for y, v in rungs.items() if y > yr and kind(y) == "iBond ETF") + \
            sum(v for y, v in back.items() if kind(y) == "iBond ETF")
        after = after_bonds + after_funds + etf_after
        pv_owed = sum(E.PAYMENT * c.P(date(y, 1, 1)) / c.P(on) for y in Y if y > yr)
        rows.append({"date": on.isoformat(), "value_before_payment": before, "payment_made": paid[yr],
                     "own_holding_pays": oa[yr], "own_holding_above_50k": oa[yr] - E.PAYMENT,
                     "backstop_and_carry_cover": max(from_etf, 0.0), "etf_before": etf_before,
                     "value_after_payment": after, "payments_still_owed": E.PAYMENT * len([y for y in Y if y > yr]),
                     "forward_value_of_payments_still_owed": pv_owed,
                     "funded_ratio_after": after / pv_owed if pv_owed else None,
                     "after_in_bonds": after_bonds, "after_in_ibond_etfs": after_funds, "after_in_short_etf": etf_after,
                     "share_bonds_after": after_bonds / after if after else None,
                     "share_ibond_after": after_funds / after if after else None,
                     "share_short_etf_after": etf_after / after if after else None})
        cin = carry[yr] * (world.grow(on, date(yr + 1, 1, 1)) if yr < 2042 else 0.0)
    return rows, left


class Switch(E.Reinvest):
    """Forward rates until `on`, then a flat r (0: nothing earns interest; -WAIT_FEE: waiting money loses the ETF's
    fee): money waiting in the floating short ETF, or inside an iBond fund after its holdings mature, switches too."""

    def __init__(self, curve, on, r):
        super().__init__(curve, "base")
        self.on, self.r = on, r

    def grow(self, d1, d2):
        if d2 <= d1:
            return 1.0
        g = super().grow(d1, min(d2, self.on)) if d1 < self.on else 1.0
        t0 = max(d1, self.on)
        return g * math.exp(self.r * (d2 - t0).days / 365.25) if d2 > t0 else g


def release_schedule(world, r_test=0.0):
    """Escrow-style release (Keel's reading, not in the IPS): after each payment, the ETF money that can be handed back
    while everything left still pays every later payment if, from that day, nothing earns interest (r_test = 0) or
    every waiting dollar loses the ETF's fee (r_test = -WAIT_FEE), cash inside the iBond funds included. Money already received (own rungs' coupons waiting in
    the ETF) is counted at its value that day; flows still to come at face; all in that day's money (exact carry)."""
    rel, cin, total, out = {}, 0.0, 0.0, []
    pb = C.pool_buckets(POOL, world)
    oa = C.own_amounts(OWN, world)
    for yr in Y:
        on = date(yr, 1, 1)
        dfl = lambda d: math.exp(-r_test * (d - on).days / 365.25)   # $1 at d in money of `on`, carried at r_test
        sw = Switch(c, on, r_test)
        avail = oa[yr] + pb[yr] + cin
        surplus = max(avail - E.PAYMENT, 0.0)
        slack = surplus
        cum_av, cum_need = surplus, 0.0
        for k in [y for y in Y if y > yr]:
            own_k = sum(OWN[k] * a * (world.grow(d, on) if d <= on else dfl(d))
                        for d, a, _ in E.rung_flows(I[k], sw))
            pool_k = sum(u * a * dfl(d) for y2, u in POOL.items() for d, a, _ in E.rung_flows(I[y2], sw)
                         if d > on and E.next_payment(d) == k)
            cum_av += own_k + pool_k
            cum_need += E.PAYMENT * dfl(date(k, 1, 1))
            slack = min(slack, cum_av - cum_need)
        x = max(min(slack, surplus), 0.0)
        rel[yr] = x
        total += x
        out.append({"date": on.isoformat(), "released": x, "etf_after_release": surplus - x})
        cin = (surplus - x) * (world.grow(on, date(yr + 1, 1, 1)) if yr < 2042 else 0.0)
    return out, total


out = {"stamp": {"curve": E.CURVE_DAY, "run": C.RUN, "design": NAME, "label": D["label"]}}
WORLDS = (("base", C.BASE), ("zero", C.ZERO), ("fee", C.FEEW), ("minus3", E.Reinvest(c, "shift", 0.03)))
for wname, w in WORLDS:
    rows, left = run(w)
    out[wname] = rows
    out[f"{wname}_left_after_2042"] = left
    out[f"{wname}_left_after_2042_value_jan2033"] = C.in_2033_money(left, w)          # at that world's own rates
    out[f"{wname}_left_after_2042_value_jan2033_at_6nov_forwards"] = left * c.P(date(2042, 1, 1)) / c.P(E.J33)

# composition on 1 Jan 2033, before the first payment (base world)
on = E.J33
comp = []
for y in Y:
    paid_out = I[y].end <= on
    comp.append({"payment": y, "holding": I[y].name + (" payout, now cash in the short Treasury ETF" if paid_out else ""),
                 "type": "cash (short Treasury ETF)" if paid_out else kind(y), "role": "own rung",
                 "pays_out": I[y].end.isoformat(), "months_before_payment": round(((date(y, 1, 1) - I[y].end).days) / 30.44, 1),
                 "value_1jan2033": own_value(y, OWN[y], on, C.BASE), "units_jan2027": OWN[y],
                 "cost_jan2027": OWN[y] * I[y].price})
for y, v in pool_future(on, C.BASE).items():
    comp.append({"payment": y, "holding": I[y].name, "type": kind(y), "role": "backstop (pooled)",
                 "pays_out": I[y].end.isoformat(), "value_1jan2033": v, "units_jan2027": POOL[y],
                 "cost_jan2027": POOL[y] * I[y].price})
etf33 = out["base"][0]["etf_before"]
comp.append({"holding": "Short-term Treasury ETF (type; which one WInS lists is UNVERIFIED)", "type": "Treasury ETF",
             "role": "backstop money received 2027-2032, waiting for the next payment due", "value_1jan2033": etf33})
out["composition_1jan2033_base"] = comp
out["ladder_cost_jan2027"] = D["cost"]
out["plain_cost_jan2027"] = C.PLAIN_COST
out["margin_jan2027"] = D["margin"]
own33 = sum(r["value_1jan2033"] for r in comp if r.get("role") == "own rung")
back33 = sum(r["value_1jan2033"] for r in comp if r.get("role") != "own rung")
out["margin_cost_carried_to_1jan2033_at_forwards"] = D["margin"] / c.P(E.J33)
out["margin_value_1jan2033_at_forwards"] = back33                    # reserve before the payment less the own rungs
out["own_rungs_value_1jan2033"] = own33
tot33 = own33 + back33
by_type = {}
for r in comp:
    by_type[r["type"]] = by_type.get(r["type"], 0.0) + r["value_1jan2033"]
out["composition_1jan2033_by_type"] = {t: {"value": v, "share": v / tot33} for t, v in by_type.items()}
out["composition_1jan2033_total"] = tot33
for key, rt in (("release_if_forwards_hold", -C.WAIT_FEE), ("release_if_forwards_hold_tested_at_0pct", 0.0)):
    rs, tot = release_schedule(C.BASE, rt)
    out[key] = {"test": f"later payments paid if waiting money earns {rt:+.2%} a year from the release day",
                "schedule": rs, "total_nominal": tot,
                "value_jan2027": sum(r["released"] * c.P(date(int(r["date"][:4]), 1, 1)) for r in rs),
                "value_jan2033": sum(r["released"] * c.P(date(int(r["date"][:4]), 1, 1)) for r in rs) / c.P(E.J33)}
rs, tot = release_schedule(C.BASE, -C.WAIT_FEE)
(HERE / f"results_reserve_2026-11-10{C.tag(NAME)}.json").write_text(json.dumps(out, indent=1))

k = C.fmt
print("design", NAME, "cost", k(D["cost"]), "margin", k(D["margin"]), "margin at 1 Jan 2033", k(out["margin_value_1jan2033_at_forwards"]))
for wname, _ in WORLDS:
    print(f"\n{wname}: date | before | paid | own pays | backstop+carry cover | after | fwd value owed | funded | bonds/iBond/short ETF"
          f" | left after 2042 {k(out[wname + '_left_after_2042'])} ({k(out[wname + '_left_after_2042_value_jan2033'])} in 2033 money)")
    for r in out[wname]:
        fr = f"{r['funded_ratio_after']:.1%}" if r["funded_ratio_after"] else "-"
        sh = (f"{r['share_bonds_after']:.0%}/{r['share_ibond_after']:.0%}/{r['share_short_etf_after']:.0%}"
              if r["share_bonds_after"] is not None else "-")
        print(r["date"], k(r["value_before_payment"]), k(r["payment_made"]), k(r["own_holding_pays"]),
              k(r["backstop_and_carry_cover"]), k(r["value_after_payment"]), k(r["forward_value_of_payments_still_owed"]),
              fr, sh)
print("\ncomposition 1 Jan 2033 (base):")
for r in comp:
    print(r.get("payment", ""), r["holding"][:40], r["role"], k(r["value_1jan2033"]), r.get("months_before_payment", ""))
for key in ("release_if_forwards_hold", "release_if_forwards_hold_tested_at_0pct"):
    o = out[key]
    print(key, [(r["date"][:4], round(r["released"])) for r in o["schedule"]], "total", k(o["total_nominal"]),
          "value 2027", k(o["value_jan2027"]), "2033", k(o["value_jan2033"]))
print("by type 1 Jan 2033", {t: (k(v["value"]), f"{v['share']:.1%}") for t, v in out["composition_1jan2033_by_type"].items()},
      "total", k(tot33), "| backstop", k(back33), "| cost carried", k(out["margin_cost_carried_to_1jan2033_at_forwards"]))
