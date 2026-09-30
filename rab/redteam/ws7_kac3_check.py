"""WS7 key-assumptions challenge, round 3 (read-only), RAB Kit, 2026-09-30 (Sydney). AI-generated (Claude Code) for Team
Caplet. MODEL outputs, not in numbers.yaml (UNVERIFIED for team outputs until WS1 adopts them). Uses rab/models/m1_ladder.py read-only (Book L holder
cash flows, M1_METHOD.md E1). Questions:
 [1] How much of Book L's coupon-reinvestment exposure is still unseen at the 2031 range check and at the 2033 gift?
 [2] Per-rung delivery at own yield / curve (from the same flows) - is any payment short even at today's yields?
 [3] Post-2033 costs on the operating reserve (no model charges them; M8 fees stop at 2032).
Writes nothing. Run from the worktree root:
  PYTHONDONTWRITEBYTECODE=1 /Users/ray/Research/rab-ws/.venv/bin/python rab/redteam/ws7_kac3_check.py"""
import sys, os, io, contextlib
from datetime import date
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "models"))
import m1_ladder as M

ROOT = M.ROOT
rows = M.load_rows([os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
row = next(r for r in rows if r["_date"] == date(2026, 9, 28))
s = row["_date"]; cv = M.Curve(row)
wins = M.read_wins(os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv"))
with contextlib.redirect_stdout(io.StringIO()):
    look = M.section_d(row, s)
H, F = M.ibond_holdings(), M.ishares_facts()
rungs = []
for name, w in wins.items():
    if not w["bookL_size"]:
        continue
    T = date(int(w["bookL_pays_year"]), 1, 1); qty = w["bookL_size"]
    px = w["price"] if w["type"] == "ETF" else w["price"] + M.accrued(w["coupon"], w["mat"], s)
    cost = qty * px / (100 if w["type"] == "Treasury" else 1)
    fl = M.holder_flows(name, w, qty, s, look, H, F)
    rungs.append(dict(name=name, T=T, cost=cost, fl=fl, y=M.irr(fl, s, cost)))
rungs.sort(key=lambda r: r["T"])

def g(a, d, T, r):
    return a * (1 + r / 2) ** (2 * M.years(d, T))

def V_split(r, cut, r_late, policy):
    """flows before `cut` earn own yield; 'matched' = rate locked at receipt; 'bills' = rate resets at cut."""
    tot = 0.0
    for d, a in r["fl"]:
        if d >= cut:
            tot += g(a, d, r["T"], r_late)
        elif policy == "matched" or r["T"] <= cut:
            tot += g(a, d, r["T"], r["y"])
        else:
            tot += g(a, d, cut, r["y"]) * (1 + r_late / 2) ** (2 * M.years(cut, r["T"]))
    return tot

def V_flat(r, rate):
    return sum(g(a, d, r["T"], rate) for d, a in r["fl"])

print("[1] Share of the coupon gap still unseen at a check date (own yield until the date, lower rate after)")
for label, late in (("2%", lambda r: 0.02), ("own-2pp", lambda r: r["y"] - 0.02)):
    full = sum(V_flat(r, r["y"]) - V_flat(r, late(r)) for r in rungs)
    for cut in (date(2031, 1, 1), date(2033, 1, 1)):
        for pol in ("matched", "bills"):
            unseen = sum(V_flat(r, r["y"]) - V_split(r, cut, late(r), pol) for r in rungs)
            print(f"  late rate {label:7s} cut {cut}: policy {pol:7s} gap arising after cut ${unseen:,.0f} of ${full:,.0f} "
                  f"= {unseen/full:.0%}")
print("\n[2] Per-rung delivery (Book L as sized in the Sheet)")
short_own = short_curve = 0
for r in rungs:
    vo, vc = V_flat(r, r["y"]), M.grow(r["fl"], r["T"], "curve", cv)
    short_own += vo < 50000; short_curve += vc < 50000
    cp = sum(a for d, a in r["fl"] if a > 0 and d < max(dd for dd, _ in r["fl"]))
    print(f"  {r['name']:22s} pays {r['T']} own {r['y']:.2%} at own ${vo:,.0f} at curve ${vc:,.0f}")
print(f"  rungs under $50,000: at own yield {short_own}/10, at curve forwards {short_curve}/10")

print("\n[3] Post-2033 costs on the operating reserve (reserve = PV of remaining payments, flat yield; fee on the balance"
      " at each 1 Jan after the payment, 2033-2041)")
for y in (0.05, 0.03):
    bal = [sum(50000 / (1 + y) ** (k - j) for k in range(j + 1, 10)) for j in range(10)]  # after payment j (2033+j)
    for fee in (0.0025, 0.005, 0.01):
        pv = sum(fee * b / (1 + y) ** j for j, b in enumerate(bal))
        print(f"  yield {y:.0%} fee {fee:.2%}/yr: PV at 1 Jan 2033 of fees ${pv:,.0f}; reserve after 2033 payment "
              f"${bal[0]:,.0f}")
