"""The team's 16 Oct "about $1,900" of room, on its own basis (numbers owner, Thu 19 Nov 2026 morning, Sydney). MODEL,
Keel arithmetic. NUMBERS 8b, "The team's 16 Oct figure"; coherence reader 10, M10
(`research/meta/COHERENCE_10_2026-11-18_evening.md`).

Caplet's experience tab (kept by Caplet: `keel/library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/
01_experience_with_caplet_edits.txt` l.15) says "16 Oct: rates fell and the ladder's room under $300,000 shrank to about
$1,900". The figure is the 16 Oct check's ($298,087, room $1,913: `keel/library/assistant_review_2026-10/checks/
RESULTS_16Oct2026.md` section 5; CLAUDE.md's 17 Oct line), on its "zero basis": $50,000 due on each holding's end date
(the five iBonds funds on 15 Dec of the year before their payment, the five bonds at maturity), discounted to 1 Jan 2027,
no coupons. NUMBERS 8b prices the same close on two other bases (the payment dates, $294,770; the ten held, $295,493).

This script prices the zero basis on the register's own curve method (engine.Curve on each close, dated as
extras.py's DatedCurve), so the team's figure is booked with its basis, and asserts:
  * 8b's 16 Oct row ($294,770 and $295,493) and 8b's 37 of 214 closes under $300,000 (payment dates);
  * the zero basis on the 15, 16 and 22 Oct closes within $100 of the check's own figures ($297,778, $298,087, $302,139;
    the check bootstrapped its curve with its own pricer, `indep_pricer.py`, so a gap of tens of dollars is method).

Run from the repo root:  python3 -I keel/final_report/numbers/room_16oct.py
Writes keel/final_report/numbers/results_room_16oct_2026-11-19.json (a few seconds, numpy only). Imports engine.py and
changes nothing; reads the two official curve CSVs extras.py reads; writes no other file.
"""
import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402

OUT = HERE / "results_room_16oct_2026-11-19.json"
DEP = 300_000.0


def near(x, y, tol, what):
    assert abs(x - y) <= tol, (what, x, y)


class DatedCurve(E.Curve):
    """extras.py's DatedCurve, copied (importing extras re-runs it): the curve of one close, discounting to 1 Jan 2027."""

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

ENDS = {y: (date(y - 1, 12, 15) if y in E.FUNDS else E.BONDS[y][2]) for y in E.YEARS}


def zero_basis(cc):
    """$50,000 due on each holding's end date, discounted to 1 Jan 2027 (the 16 Oct check's 'zero basis')."""
    return sum(E.PAYMENT * cc.P(ENDS[y]) for y in E.YEARS)


series = []
for d in sorted(days):
    cc = DatedCurve(days[d], d)
    series.append({"date": d.isoformat(), "payment_dates": E.ladder_cost(cc), "zero_basis_holding_end_dates": zero_basis(cc)})
pay_under = sum(s["payment_dates"] < DEP for s in series)
zero_under = [s["date"] for s in series if s["zero_basis_holding_end_dates"] < DEP]
assert len(series) == 214 and pay_under == 37, (len(series), pay_under)          # 8b: 37 of 214

d16 = date(2026, 10, 16)
c16 = DatedCurve(days[d16], d16)
ii = E.instruments(c16)
held16 = E.cost(ii, E.size_own_rung(ii, E.Reinvest(c16)))
pay16, zero16 = E.ladder_cost(c16), zero_basis(c16)
near(pay16, 294_770, 1, "8b 16 Oct payment dates")
near(held16, 295_493, 1, "8b 16 Oct ten held")
check = {"2026-10-15": 297_778, "2026-10-16": 298_087, "2026-10-22": 302_139}     # RESULTS_16Oct2026.md, sections 1 and 5
gaps = {}
for k, v in check.items():
    z = next(s["zero_basis_holding_end_dates"] for s in series if s["date"] == k)
    gaps[k] = z - v
    near(z, v, 100, f"check's zero basis {k}")
near(DEP - zero16, 1_843, 1, "16 Oct room on the zero basis, register curve method")

out = {"run": "Thu 19 Nov 2026 morning (Sydney), numbers owner", "section": "NUMBERS 8b, the team's 16 Oct figure",
       "basis": "zero basis: $50,000 due on each holding's end date (iBonds funds 15 Dec of the year before the payment; "
                "bonds at maturity), discounted to 1 Jan 2027 on each close's par curve, engine.Curve method; no coupons",
       "team_record": {"words": "the ladder's room under $300,000 shrank to about $1,900 (16 Oct)",
                       "check_figure": {"cost": 298_087, "room": 1_913}},
       "16_oct": {"zero_basis_cost": zero16, "zero_basis_room": DEP - zero16, "payment_dates_cost": pay16,
                  "payment_dates_room": DEP - pay16, "ten_held_cost": held16, "ten_held_room": DEP - held16},
       "register_minus_check_zero_basis": gaps,
       "closes": len(series), "closes_under_300k_payment_dates": pay_under,
       "closes_under_300k_zero_basis": len(zero_under),
       "zero_basis_under_300k_first_last": [zero_under[0], zero_under[-1]] if zero_under else None,
       "all_asserts_pass": True}
OUT.write_text(json.dumps(out, indent=1, default=float))

k_ = lambda x: f"${x:,.0f}"
print(f"16 Oct: zero basis {k_(zero16)}, room {k_(DEP - zero16)} (check: $298,087, $1,913); payment dates {k_(pay16)} "
      f"(room {k_(DEP - pay16)}); ten held {k_(held16)} (room {k_(DEP - held16)})")
print("register minus check, zero basis:", {k: round(v) for k, v in gaps.items()})
print(f"closes under $300,000: payment dates {pay_under} of {len(series)}; zero basis {len(zero_under)} "
      f"({out['zero_basis_under_300k_first_last']})")
print("all asserts pass; wrote", OUT.name)
