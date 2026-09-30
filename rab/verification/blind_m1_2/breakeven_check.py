"""Second computation of the coupon-reinvestment break-even rates (WS7 key-assumptions check, single build until now).

Completeness critic, RAB Kit, 30 Sep 2026 (Sydney). AI-generated verification code (Claude Code) for Team Caplet.
WS7 found the weakest load-bearing assumption: Book L (the ten WInS-listed holdings, sized as in the Sheet) delivers
$500,000 in total only if coupons are reinvested at 4.97% a year or more, and every rung reaches $50,000 only at 5.60%
(rab/redteam/ws7_assumptions_reinvest_check.py, built on rab/models/m1_ladder.py cash flows). numbers_ws3.yaml carries
it as "NOT Gate-B checked ... UNVERIFIED". This script recomputes both rates from the BLIND M1 build
(blind_m1_2.py, written from M1_METHOD.md only, shares no code with m1_ladder.py or the WS7 script): same Book L
holdings, the blind cash flows (look-through iBonds, 0.07% fee, cash lines), the same semiannual convention
(1 + r/2)^(2t) to each payment date (1 Jan 2033 ... 1 Jan 2042), 28 Sep 2026 closes.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind_m1_2/breakeven_check.py
Writes rab/verification/blind_m1_2/breakeven_check.txt.
"""
import contextlib
import io
import os
import sys
from datetime import date

from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import blind_m1_2 as B  # noqa: E402

with contextlib.redirect_stdout(io.StringIO()):
    _, psets = B.section_B()
    D_out = B.section_D()
k_f = {t: D_out[t]["k_f_published_over_model"] for t in B.ETF_ORDER}
pset = psets["close_0928"]

rungs = []
for name, kind, qty in B.bookL_holdings():
    if kind == "Treasury":
        flows, cost = B.flows_treasury(name, qty)
        T = date(B.WINS[name]["bookL_pays"], 1, 1)
    else:
        flows, cost, _ = B.flows_ibond(name, qty, k_f[name], pset[name][0])
        T = date(B.ETF_YEAR[name] + 1, 1, 1)
    rungs.append((name, flows, T, cost))


def V(rung, r):
    _, flows, T, _ = rung
    return B.value_at(flows, T, r=r)


def total(r):
    return sum(V(g, r) for g in rungs)


r_tot = brentq(lambda x: total(x) - 500000.0, -0.02, 0.10, xtol=1e-12)
r_all = brentq(lambda x: min(V(g, x) for g in rungs) - 50000.0, -0.02, 0.10, xtol=1e-12)
lines = [
    "Coupon-reinvestment break-even, BLIND M1 build (blind_m1_2.py), Book L as sized in the Sheet, 28 Sep 2026 closes",
    f"  total delivered = $500,000 at a flat reinvestment rate of {r_tot * 100:.4f}%  (WS7 primary: 4.97%)",
    f"  every rung >= $50,000 at a flat rate of {r_all * 100:.4f}%  (WS7 primary: 5.60%)",
    f"  total at 2%: ${total(0.02):,.0f}  at 0%: ${total(0.0):,.0f}  (numbers.yaml reinvest.bookL_delivered: $466,185 / $446,840)",
    "  per rung, rate at which it reaches $50,000:",
]
for g in rungs:
    try:
        rr = brentq(lambda x: V(g, x) - 50000.0, -0.05, 0.20, xtol=1e-12)
        lines.append(f"    {g[0]:<28} pays {g[2].isoformat()}  {rr * 100:6.3f}%")
    except ValueError:
        lines.append(f"    {g[0]:<28} pays {g[2].isoformat()}  no root in [-5%, 20%]")
ok_tot = abs(round(r_tot * 100, 2) - 4.97) <= 0.005 + 1e-9
ok_all = abs(round(r_all * 100, 2) - 5.60) <= 0.005 + 1e-9
lines.append(f"verdict: total break-even {'MATCH' if ok_tot else 'DIFFERS'} at 2dp; every-rung break-even "
             f"{'MATCH' if ok_all else 'DIFFERS'} at 2dp")
out = "\n".join(lines) + "\n"
open(os.path.join(HERE, "breakeven_check.txt"), "w").write(out)
print(out)
