"""Jun, H-033 round 3 (Wed 4 Nov 2026): the ladder's duration v the cheques', re-derived a second way.

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code, for the fictional Jun). Not text to submit.
MODEL = a computer estimate from this script, not a fact. Standard library only:  python3 -I jun_r3_duration.py

Inputs are Kai's (keel/huddles/2026-11-04_the-word-the-writer-meant/research/kai_r2_check.md):
  - settlement Fri 23 Oct 2026 (the WInS snapshot day, competition/wins/2026-10-23_snapshot.md);
  - five T-bonds at their WInS clean prices that day (per $1,000 face, divided by 10 here);
  - five iBond funds at iShares effective durations "as of Oct 16, 2026" (IBTM 5.02 ... IBTR 7.56), their cheques
    discounted at a flat 5.00%;
  - cheques of $50,000 on 1 Jan 2033-2042; each rung weighted by its own cheque's present value.

What is different from Kai's script (the "second way"):
  - bonds priced on the coupon-period grid (ICMA: time in half-years to each coupon), not 2 x days/365.25;
  - yields solved by Newton's method, not bisection;
  - modified duration by bumping the yield 1bp each way and repricing, not by the closed-form sum;
  - cheque times by actual/actual (ISDA) year fractions, cheque durations by the same bump;
  - Macaulay duration printed for every line (Kai printed modified only).
Section 3 puts back what the method leaves out, one thing at a time. Section 4 looks for the "$49k" (round 2).
"""
from datetime import date
from pathlib import Path

SETTLE = date(2026, 10, 23)
CHEQUE = 50_000.0
H = 0.0001  # 1 basis point


def add_months(d, n):
    m = d.month - 1 + n
    return date(d.year + m // 12, m % 12 + 1, d.day)


def yearfrac_isda(d0, d1):
    """Actual/actual ISDA: days in each calendar year over that year's length."""
    t, d = 0.0, d0
    while d.year < d1.year:
        nxt = date(d.year + 1, 1, 1)
        t += (nxt - d).days / (366 if d.year % 4 == 0 else 365)
        d = nxt
    return t + (d1 - d).days / (366 if d.year % 4 == 0 else 365)


class Bond:
    """Semiannual fixed coupon, priced on the ICMA period grid."""

    def __init__(self, cpn, mat):
        self.cpn, self.mat = cpn, mat
        dates, d = [], mat
        while d > SETTLE:
            dates.append(d)
            d = add_months(d, -6)
        self.prev, self.dates = d, sorted(dates)
        nxt = self.dates[0]
        self.w = (nxt - SETTLE).days / (nxt - self.prev).days          # fraction of a period to next coupon
        self.accrued = cpn / 2 * (SETTLE - self.prev).days / (nxt - self.prev).days
        self.flows = [(self.w + k, cpn / 2 + (100.0 if dd == mat else 0.0)) for k, dd in enumerate(self.dates)]

    def dirty(self, y):
        return sum(cf / (1 + y / 2) ** p for p, cf in self.flows)

    def solve(self, clean):
        target, y = clean + self.accrued, 0.05
        for _ in range(50):
            f = self.dirty(y) - target
            dfdy = (self.dirty(y + H) - self.dirty(y - H)) / (2 * H)
            y -= f / dfdy
        return y

    def mod_bump(self, y):
        return (self.dirty(y - H) - self.dirty(y + H)) / (2 * H * self.dirty(y))

    def macaulay(self, y):
        return sum(p / 2 * cf / (1 + y / 2) ** p for p, cf in self.flows) / self.dirty(y)


def cheque_pv(t, y):
    return CHEQUE / (1 + y / 2) ** (2 * t)


def cheque_mod_bump(t, y):
    return (cheque_pv(t, y - H) - cheque_pv(t, y + H)) / (2 * H * cheque_pv(t, y))


# ---- inputs (Kai's) -------------------------------------------------------------------------------------------
FUNDS = [("IBTM", 2033, 5.02, 3.50), ("IBTO", 2034, 5.68, 4.04), ("IBTP", 2035, 6.39, 4.12),
         ("IBTQ", 2036, 7.03, 4.28), ("IBTR", 2037, 7.56, 4.35)]           # name, cheque year, eff. dur, avg coupon
FUND_Y = 0.05
TBONDS = [("4.75% Feb-2037", 2038, 4.75, date(2037, 2, 15), 976.134), ("4.50% May-2038", 2039, 4.50, date(2038, 5, 15), 948.129),
          ("4.375% Nov-2039", 2040, 4.375, date(2039, 11, 15), 919.574), ("4.25% Nov-2040", 2041, 4.25, date(2040, 11, 15), 897.877),
          ("3.125% Nov-2041", 2042, 3.125, date(2041, 11, 15), 769.963)]   # name, cheque year, coupon, maturity, WInS last
WINS_MV = {"IBTM": 99_313.67, "IBTO": 23_936.00, "IBTP": 22_725.59, "IBTQ": 21_594.48, "IBTR": 20_450.68,
           "4.75% Feb-2037": 19_522.68, "4.50% May-2038": 18_962.57, "4.375% Nov-2039": 16_552.34,
           "4.25% Nov-2040": 16_161.79, "3.125% Nov-2041": 15_399.25}       # snapshot "Market value", 23 Oct

rows = []  # name, cheque year, y, holding mod, holding mac, cheque t, cheque mod, cheque pv, bond or None
for name, cy, ed, _ in FUNDS:
    t = yearfrac_isda(SETTLE, date(cy, 1, 1))
    rows.append(dict(name=name, cy=cy, y=FUND_Y, mod=ed, mac=ed * (1 + FUND_Y / 2), t=t,
                     cmod=cheque_mod_bump(t, FUND_Y), pv=cheque_pv(t, FUND_Y), bond=None))
for name, cy, c, mat, last in TBONDS:
    b = Bond(c, mat)
    y = b.solve(last / 10)
    t = yearfrac_isda(SETTLE, date(cy, 1, 1))
    rows.append(dict(name=name, cy=cy, y=y, mod=b.mod_bump(y), mac=b.macaulay(y), t=t,
                     cmod=cheque_mod_bump(t, y), pv=cheque_pv(t, y), bond=b))


def ladder(weights, label):
    """Value-weighted durations of the holdings v PV-weighted durations of the cheques (the liability never changes)."""
    W = sum(weights.values()); P = sum(r["pv"] for r in rows)
    a_mod = sum(weights[r["name"]] * r["mod"] for r in rows) / W
    a_mac = sum(weights[r["name"]] * r["mac"] for r in rows) / W
    l_mod = sum(r["pv"] * r["cmod"] for r in rows) / P
    l_mac = sum(r["pv"] * r["t"] for r in rows) / P
    print(f"  {label:<58} modified {a_mod:5.2f} v {l_mod:5.2f} ({a_mod / l_mod:4.0%})   "
          f"Macaulay {a_mac:5.2f} v {l_mac:5.2f} (short by {l_mac - a_mac:4.2f})")
    return a_mod, l_mod, a_mac, l_mac


print("Jun r3 duration check, MODEL, settlement 23 Oct 2026 (python3 -I jun_r3_duration.py)\n")
print("1. Per rung (holding v its own cheque, years)")
print(f"  {'rung':<16}{'pays':>5}{'yield':>8}{'hold mod':>10}{'hold Mac':>10}{'chq mod':>9}{'chq Mac':>9}{'short (Mac)':>13}{'cheque PV':>11}")
for r in rows:
    print(f"  {r['name']:<16}{r['cy']:>5}{r['y']:>8.3%}{r['mod']:>10.2f}{r['mac']:>10.2f}{r['cmod']:>9.2f}"
          f"{r['t']:>9.2f}{r['t'] - r['mac']:>13.2f}{r['pv']:>11,.0f}")
print(f"  every rung shorter than its own cheque: {all(r['mac'] < r['t'] for r in rows)}"
      f"  (smallest gap {min(r['t'] - r['mac'] for r in rows):.2f}y, largest {max(r['t'] - r['mac'] for r in rows):.2f}y)")
print(f"  sum of cheque PVs (own-rung sizing): ${sum(r['pv'] for r in rows):,.0f}")
print("  fund rungs: 'hold mod' is iShares effective duration (16 Oct); 'hold Mac' = effective x (1 + 0.05/2), an approximation\n")

print("2. Whole ladder v the cheques (Kai's weighting: each rung costs its own cheque's PV)")
base = ladder({r["name"]: r["pv"] for r in rows}, "A. own-rung sizing (Kai's inputs, second way)")
print("  Kai's published figures: 7.61 v 9.99 modified, ratio 76%.\n")

print("3. Put back what the method leaves out, one at a time (the cheques' side never changes)")
# 3a. funds' Macaulay from a bond model of each fund instead of effective x (1+y/2)
fund_bonds = {}
for name, cy, ed, avg_c in FUNDS:
    fb = Bond(avg_c, date(cy - 1, 12, 15))      # one bond with the fund's average coupon, ending 15 Dec before its cheque
    fund_bonds[name] = fb
saved = {r["name"]: (r["mod"], r["mac"]) for r in rows}
for r in rows:
    if r["name"] in fund_bonds:
        fb = fund_bonds[r["name"]]
        r["mod"], r["mac"] = fb.mod_bump(FUND_Y), fb.macaulay(FUND_Y)
print("  funds as one bond each (average coupon, ends 15 Dec, 5.00%): modelled modified v iShares effective")
for name, _, ed, _ in FUNDS:
    print(f"    {name}: {fund_bonds[name].mod_bump(FUND_Y):.2f} v {ed:.2f}   (Macaulay {fund_bonds[name].macaulay(FUND_Y):.2f})")
ladder({r["name"]: r["pv"] for r in rows}, "B. funds' durations from that bond model")
for r in rows:
    r["mod"], r["mac"] = saved[r["name"]]
ladder(WINS_MV, "C. WInS weights, 23 Oct (all of IBTM's $99,314)")
others = [r for r in rows if r["name"] != "IBTM"]
scale = sum(WINS_MV[r["name"]] for r in others) / sum(r["pv"] for r in others)
w_d = dict(WINS_MV); w_d["IBTM"] = scale * rows[0]["pv"]
ladder(w_d, f"D. WInS weights, IBTM cut to its 2033 rung (x{scale:.2f} of PV)")
w_e = {r["name"]: (r["pv"] if r["bond"] is None else 500 * r["bond"].dirty(r["y"])) for r in rows}
ladder(w_e, "E. T-bonds bought at $50,000 face (funds at PV)")
for r in rows:
    if r["name"] in fund_bonds:
        fb = fund_bonds[r["name"]]
        r["mod"], r["mac"] = fb.mod_bump(FUND_Y), fb.macaulay(FUND_Y)
w_f = {r["name"]: (r["pv"] if r["bond"] is None else 500 * r["bond"].dirty(r["y"])) for r in rows}
ladder(w_f, "F. B and E together (the longest this script makes it)")
for r in rows:
    r["mod"], r["mac"] = saved[r["name"]]
# how much of the ladder would have to sit in the 2042 bond alone, the other nine in PV proportions, to reach the cheques
rest = rows[:-1]
m_rest = sum(r["pv"] * r["mac"] for r in rest) / sum(r["pv"] for r in rest)
need = (base[3] - m_rest) / (rows[-1]["mac"] - m_rest)
print(f"  To reach the cheques' {base[3]:.2f}y Macaulay, {need:.0%} of the ladder's money would have to sit in the 2042 bond"
      f" alone (it holds {rows[-1]['pv'] / sum(r['pv'] for r in rows):.0%} under own-rung sizing): a bet on the long end,"
      " not one bond per payment.")
print("  Not put back (none is worth two years): durations are today's and shrink as the funds turn to cash before each"
      "\n  December; one parallel yield move per rung; fund durations dated 16 Oct, a week before settlement (about 0.02y);"
      "\n  cheques discounted at each rung's own yield, not one curve.\n")

print("4. The money duration leaves out: where each $50,000 comes from (own-rung sizing, reinvested at the rung's yield)")
tot_p = tot_c = tot_r = 0.0
for r in rows:
    b = r["bond"] if r["bond"] is not None else fund_bonds[r["name"]]
    T = 2 * r["t"]                                            # cheque date in half-years from settlement (act/act)
    # flows' times in half-years on the act/act clock, so cost and growth use one clock
    grow = sum(cf * (1 + r["y"] / 2) ** (T - 2 * yearfrac_isda(SETTLE, d))
               for (p, cf), d in zip(b.flows, b.dates))
    units = CHEQUE / grow                                     # face (per 100) bought so the rung pays exactly $50,000
    principal = units * 100
    coupons = units * sum(cf for _, cf in b.flows) - principal
    tot_p += principal; tot_c += coupons; tot_r += CHEQUE - principal - coupons
print(f"  principal ${tot_p:,.0f} ({tot_p / 5e5:.0%}), coupons ${tot_c:,.0f} ({tot_c / 5e5:.0%}), "
      f"interest on reinvested coupons and waiting money ${tot_r:,.0f} ({tot_r / 5e5:.0%})")
print("  (funds modelled as one bond each, as in 3B; settlement 23 Oct, not the January 2027 purchase)")
src = Path(__file__).resolve().parents[3] / "library/assistant_review_2026-10/oct20/ldi/ldi_second_opinion.md"
try:
    hit = [(i, ln) for i, ln in enumerate(src.read_text().splitlines(), 1) if "$49k (10%)" in ln and "principal" in ln]
    for i, ln in hit:
        print(f"  The round-2 figure at its file, keel/library/assistant_review_2026-10/oct20/ldi/ldi_second_opinion.md:{i}:"
              f"\n    {ln.strip()[:230]}")
    print("  (its own source, oct20/ldi/data/ldi_19oct_stdout.txt, is not in the repo: the $49k is quoted, not re-runnable;"
          " this section is the re-run)")
except OSError:
    print("  ldi_second_opinion.md not found")
