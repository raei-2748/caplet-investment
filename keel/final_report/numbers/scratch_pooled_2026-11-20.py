"""Scratch: answers to the fixed-income judge's arithmetic attacks of Fri 20 Nov 2026 (analysis worker for the numbers
owner). Keel arithmetic and MODEL on the register's engine; NOT a register script. It changes no register file, writes
no results file and moves no register figure; it prints. Answers: `research/attacks_2026-11-20/NUMBERS_ANSWERS.md`.

Run from the repo root:  python3 -I keel/final_report/numbers/scratch_pooled_2026-11-20.py   (about 30 seconds)
Imports engine.py, plan.py and completion.py and changes none of them; reads results_2026-11-17.json (read only) to
assert the register's figures it starts from.

Parts (the judge's attack numbers, `research/attacks_2026-11-20/judge_fixed_income_pm.md`):
  A  attack 9:  the zero-interest test, own-rung or pooled; the extra Treasuries re-sized with ALL cash pooled across the
                ten (every other rule kept: the bill fund's 0.15% on every waiting dollar, every iBond fund flow 0.5%
                smaller, the same instruments, more of the same bonds and funds, the ten at their plain sizes); a middle
                variant pooled only from 2033; the timing ledger; what the re-size would do to the floor, VT and range.
  B  attack 3:  the WInS book at cost scaled to $450,000 beside the plan in January 2028 at cost.
  D  attack 12: the per-payment table for the WInS book on the 6 Nov curve (bond yields at fill, payouts against the
                scaled $33,333, DV01 of the book against the liability).
  E  attack 25: deposits of $0 to $39,162: what fails, on each basis.
  F  attack 27: the all-Treasury plan with the same flexibility (section 4, C8), unpacked.
  G  attack 28: the reserve as a schedule (reproduces 8a and 8h).
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

c, I, Y = C.c, C.I, E.YEARS
PAY = E.PAYMENT
f01 = c.fwd(E.J27, E.J28)
CARRY = math.exp(f01 * E.T01)          # 1 Jan 2027 money -> January 2028 money at d0 = d1 = 0 (completion.margin_fn)
REG = json.loads((HERE / "results_2026-11-17.json").read_text())
k = lambda x: f"${x:,.0f}"


def close(a, b, tol=1.0, what=""):
    assert abs(a - b) <= tol, f"{what}: {a} against {b}"


# ====================================================================== A. attack 9: own-rung or pooled
CUT = C.cost_cut(I)                    # every iBond fund flow 0.5% smaller (PAY_MARGIN); prices unchanged
R_STD = -C.WAIT_FEE                    # the bill fund's 0.15% on every waiting dollar


def bucket_own(y2, d):
    return y2                          # own rung: every flow waits for its own payment


def bucket_pool(y2, d):
    return E.next_payment(d)           # pooled: every flow waits for the next payment due


def bucket_from_2033(y2, d):
    return y2 if d < E.J33 else E.next_payment(d)   # own rule to 2032, pooled from 2033


def cash_matrix(insts, r, rule):
    """M[k, j]: deflated cash from one unit of instrument j counted for payment k (flat rate r: exact carry)."""
    M = np.zeros((10, 10))
    w = C.Flat(c, r)
    for j, y2 in enumerate(Y):
        for d, a, _ in E.rung_flows(insts[y2], w):
            b = rule(y2, d)
            if b in Y:
                M[Y.index(b), j] += a * C._defl(d, r)
    return M


def extra_needed(insts, r, own_rule, base=None):
    """Cheapest extra units (pooled, x >= 0) so that the plain rungs run under own_rule plus the extra pay all ten at a
    flat r. Cumulative test: cash counted by each 1 January covers the payments due by then; surplus carries."""
    base = C.PLAIN if base is None else base
    u = np.array([base[y] for y in Y])
    own_cash = cash_matrix(insts, r, own_rule) @ u
    need = np.cumsum([PAY * C._defl(date(y, 1, 1), r) for y in Y]) - np.cumsum(own_cash)
    return C.lp_min_cost(insts, np.zeros(10), need, r)


def ledger_rule(world, insts, own_units, own_rule, pool_units):
    """C.ledger with a choice of rule for the plain rungs (pool_units always pooled)."""
    cash = {y: 0.0 for y in Y}
    for units, rule in ((own_units, own_rule), (pool_units, bucket_pool)):
        for y2, uu in (units or {}).items():
            if uu <= 0:
                continue
            for d, a, _ in E.rung_flows(insts[y2], world):
                b = rule(y2, d)
                if b in cash:
                    cash[b] += uu * a * world.grow(d, date(b, 1, 1))
    paid, avail_y, carry_y, carry, left = {}, {}, {}, 0.0, 0.0
    for y in Y:
        avail = cash[y] + carry
        avail_y[y] = avail
        paid[y] = min(avail, PAY)
        carry_y[y] = max(avail - PAY, 0.0)
        if y < 2042:
            carry = carry_y[y] * world.grow(date(y, 1, 1), date(y + 1, 1, 1))
        else:
            left = carry_y[y]
    return dict(cash=cash, paid=paid, avail=avail_y, carry=carry_y, left=left,
                short=sum(PAY - v for v in paid.values()))


cost27 = lambda u: sum(u[y] * I[y].price for y in Y)
reg_c1 = REG["C1"]

# A0. reproduce the register's own-rung test (section 2): the call, its 0% twin, P100 and design B
x_call = extra_needed(CUT, R_STD, bucket_own)
close(cost27(x_call), cost27(C.BACKSTOP), 0.5, "call backstop")
close(cost27(C.BACKSTOP), 35_213, 1, "backstop 2027")
close(cost27(C.BACKSTOP) * CARRY, 36_774, 1, "extra Treasuries Jan 2028")
x_call0 = extra_needed(I, 0.0, bucket_own)
close(C.PLAIN_COST + cost27(x_call0), 335_771, 1, "H_plain_0")
x_pool0 = extra_needed(I, 0.0, bucket_pool)
close(C.PLAIN_COST + cost27(x_pool0), 332_922, 1, "P100 at 0%")
xb = C.lp_min_cost(I, np.zeros(10), np.cumsum([PAY for _ in Y]).astype(float), 0.0)
close(cost27(xb), 319_687, 1, "design B at 0%")
print("A0 register reproduced: backstop", k(cost27(C.BACKSTOP)), "(2027),", k(cost27(C.BACKSTOP) * CARRY),
      "(Jan 2028); H_plain_0", k(C.PLAIN_COST + cost27(x_call0)), "; P100", k(C.PLAIN_COST + cost27(x_pool0)),
      "; design B", k(cost27(xb)), "buys", sum(1 for y in Y if xb[y] > 1), "rungs:",
      {y: round(xb[y]) for y in Y})
print("   design B at 0% against H_plain_0: ", k(C.PLAIN_COST + cost27(x_call0) - cost27(xb)), "less (the judge's",
      "'about $16,000')")

# A1. the same standard as the call, with every flow of the ten pooled too
x_pool = extra_needed(CUT, R_STD, bucket_pool)
x_mid = extra_needed(CUT, R_STD, bucket_from_2033)
rows = {"call (own-rung ten, pooled extra)": x_call, "pooled from 2033 only": x_mid, "all cash pooled": x_pool}
print("\nA1 extra Treasuries under the call's standard (zero interest, bill fee 0.15%, fund flows 0.5% smaller)")
print("   variant | 1 Jan 2027 money | January 2028 money | less than the call (Jan 2028) | extra by holding")
A1 = {}
for name, x in rows.items():
    v27, v28 = cost27(x), cost27(x) * CARRY
    A1[name] = (v27, v28)
    print(f"   {name:36s} {k(v27):>9s} {k(v28):>9s} {k(cost27(x_call) * CARRY - v28):>8s}  ",
          {I[y].name: round(x[y]) for y in Y if x[y] > 0.5})
save28 = (cost27(x_call) - cost27(x_pool)) * CARRY
save28_mid = (cost27(x_call) - cost27(x_mid)) * CARRY
print("   at exactly 0% (no fee, no margin): call", k(cost27(x_call0)), "pooled", k(cost27(x_pool0)), "saving",
      k(cost27(x_call0) - cost27(x_pool0)), "(register: $2,849)")

# A2. checks: each variant pays all ten under the standard; what is spare in the other worlds
print("\nA2 ledgers (short / left after 2042)")
for name, x, rule in (("call", C.BACKSTOP, bucket_own), ("pooled from 2033", x_mid, bucket_from_2033),
                      ("all pooled", x_pool, bucket_pool)):
    std = ledger_rule(C.FEEW, CUT, C.PLAIN, rule, x)
    fee = ledger_rule(C.FEEW, I, C.PLAIN, rule, x)
    zer = ledger_rule(C.ZERO, I, C.PLAIN, rule, x)
    fwd = ledger_rule(C.BASE, I, C.PLAIN, rule, x)
    assert std["short"] < 0.01, (name, std["short"])
    print(f"   {name:18s} standard: short {k(std['short'])}, left {k(std['left'])} | fee only: left {k(fee['left'])}"
          f" | 0%: left {k(zer['left'])} | forwards: left {k(fwd['left'])} on 1 Jan 2042 = "
          f"{k(C.in_2033_money(fwd['left'], C.BASE))} in 1 Jan 2033 money")
    if name == "call":
        close(zer["left"], 2_604, 1, "call 0% left")
        close(fee["left"], 1_177, 1, "call fee left")
        close(fwd["left"], 75_934, 1, "call forwards left")

# A3. the timing: all cash pooled, under the standard (zero interest, bill fee, fund flows 0.5% smaller)
print("\nA3 timing, all cash pooled, under the standard: cash counted for each 1 January / payment / balance carried")
std_p = ledger_rule(C.FEEW, CUT, C.PLAIN, bucket_pool, x_pool)
std_c = ledger_rule(C.FEEW, CUT, C.PLAIN, bucket_own, C.BACKSTOP)
cum_in, cum_out = 0.0, 0.0
for y in Y:
    print(f"   {y}: pooled cash in {k(std_p['cash'][y]):>9s}, carried after {k(std_p['carry'][y]):>9s} | call: own rung"
          f" + extra in {k(std_c['cash'][y]):>9s}, carried after {k(std_c['carry'][y]):>8s}")
# the 2042 rung (3.125% Nov 2041) as the judge's example: where its coupons go under each rule
w = C.Flat(c, R_STD)
b42 = {"own": {}, "pool": {}}
for d, a, _ in E.rung_flows(CUT[2042], w):
    for lab, rule in (("own", bucket_own), ("pool", bucket_pool)):
        b = rule(2042, d)
        b42[lab][b] = b42[lab].get(b, 0.0) + C.PLAIN[2042] * a
print("   the 2042 rung's own cash (3.125% Nov 2041, plain face $29,021), by the payment it is counted for:")
print("     own rule:", {y: round(v) for y, v in sorted(b42["own"].items())})
print("     pooled:  ", {y: round(v) for y, v in sorted(b42["pool"].items())})
binding = [y for y in Y if std_p["carry"][y] < 1.0]
print("   pooled: balance carried is nil after", binding, "(the dates the extra is sized for)")

# A4. what the pooled re-size would do to the 2028 split and the range (central, today's forwards, same rule)
def central(extra28):
    d = P.run(c, margin_fn=lambda d0, d1: extra28 + 0 * np.asarray(d0, float))
    r = C.rule(d)
    return dict(complete=float(d["complete"]), R=float(d["R"]), floor_money=float(d["floor_money"]),
                vt=float(d["vt28"]), floor=float(d["floor"]), moved=float(d["moved"]),
                bottom_raw=float(r["bottom_raw"]), bottom=float(r["bottom"]), top_raw=float(r["top_raw"]),
                top=float(r["top"]), excess=float(r["excess"]), kept=float(d["kept33"]),
                flex=float(d["kept33"] + r["excess"]))


base = central(cost27(C.BACKSTOP) * CARRY)
close(base["complete"], 39_162, 1, "completion")
close(base["floor_money"], 81_244, 1, "floor money")
close(base["vt"], 29_594, 1, "VT")
close(base["bottom_raw"], 97_605, 1, "bottom raw")
close(base["top_raw"], 117_142, 1, "top raw")
print("\nA4 central plan, call against pooled (MODEL, today's forwards, VT 7.5%, the same range rule)")
for name, ex in (("call", cost27(C.BACKSTOP) * CARRY), ("pooled from 2033", cost27(x_mid) * CARRY),
                 ("all pooled", cost27(x_pool) * CARRY)):
    z = central(ex)
    print(f"   {name:16s} first slice {k(z['complete'])}, left {k(z['R'])}, floor money {k(z['floor_money'])}, VT "
          f"{k(z['vt'])}, floor pays {k(z['floor'])}, bottom {k(z['bottom_raw'])} -> {k(z['bottom'])}, top "
          f"{k(z['top_raw'])} -> {k(z['top'])}, excess {k(z['excess'])}, half kept {k(z['kept'])}, "
          f"flexibility plus excess {k(z['flex'])}")

# A5. what pooling the ten changes in the forward-rate world (the WInS notes' "reinvested coupons fund the rest"):
# share of each payment paid by its own Treasury's cash that arrives in the year before it, at forwards
def own_share_pooled(units):
    out = {}
    for y in Y:
        mine = sum(units[y] * a * C.BASE.grow(d, date(y, 1, 1)) for d, a, _ in E.rung_flows(I[y], C.BASE)
                   if E.next_payment(d) == y)
        out[y] = min(mine, PAY) / PAY
    return out


osp = own_share_pooled(C.add(C.PLAIN, x_pool))
print("\nA5 all pooled, at forwards: share of each payment from its own Treasury's cash of that year",
      {y: f"{v:.0%}" for y, v in osp.items()})
early = sum(C.PLAIN[y2] * a * C.BASE.grow(d, E.J33) for y2 in Y if y2 >= 2038
            for d, a, _ in E.rung_flows(I[y2], C.BASE) if E.next_payment(d) == 2033)
print("   the 2038-2042 bonds' coupons counted for the 2033 payment when pooled, at forwards:", k(early))

# A6. the reinvestment exposure of the ten as written (plain sizes, no extra) at zero interest, own-rung against pooled
for lab, rule in (("own-rung", bucket_own), ("pooled", bucket_pool)):
    L = ledger_rule(C.ZERO, I, C.PLAIN, rule, None)
    print(f"A6 the ten as written at 0%, {lab}: short {k(L['short'])}",
          {y: round(PAY - v) for y, v in L["paid"].items() if PAY - v > 0.5})

# ====================================================================== B. attack 3: the WInS book against the plan
book = {"IBTM": 97_489.95, "IBTO": 23_408.64, "IBTP": 22_155.30, "IBTQ": 20_973.24, "IBTR": 19_823.72,
        "Feb37": 19_203.80, "May38": 18_615.26, "Nov39": 16_200.95, "Nov40": 15_790.32, "Nov41": 14_991.00,
        "VT": 26_524.61, "cash": 3_513.79, "costs": 1_309.42}
close(sum(book.values()), 300_000, 0.01, "8g total")
floor_standin = 3361 * 21.65
ladder = sum(book[x] for x in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "Feb37", "May38", "Nov39", "Nov40",
                               "Nov41")) - floor_standin
close(ladder, 195_886.53, 0.01, "Q17 ladder")
cashc = book["cash"] + book["costs"]
B_book = {"payment Treasuries": ladder, "floor (book: IBTM floor stand-in)": floor_standin, "VT": book["VT"],
          "cash and purchase costs (WInS only)": cashc}
plan_pay = 300_000 + base["complete"]
B_plan = {"payment Treasuries": plan_pay, "floor (book: IBTM floor stand-in)": base["floor_money"], "VT": base["vt"],
          "cash and purchase costs (WInS only)": 0.0}
print("\nB  WInS book at cost x 1.5 against the plan in January 2028 at cost (money put in)")
for key in B_book:
    b, p_ = 1.5 * B_book[key], B_plan[key]
    print(f"   {key:38s} book {k(B_book[key]):>9s} ({B_book[key]/3000:5.2f}%) x1.5 {k(b):>9s} | plan {k(p_):>9s} "
          f"({p_/4500:5.2f}%) | plan less book {k(p_ - b):>8s} ({(p_ - b)/4500:+.2f} points)")
left_book, left_plan = 1.5 * (floor_standin + book["VT"]), base["R"]
print(f"   left for floor and VT: book x1.5 {k(left_book)}, plan {k(left_plan)}; floor's share of it: book "
      f"{floor_standin/(floor_standin+book['VT']):.2%}, plan {base['floor_money']/left_plan:.2%}")
ten_held_7oct, ten_held_6nov = 289_216, 302_287       # NUMBERS 8b, the engine's ten held (design A), 1 Jan 2027 money
print(f"   payment Treasuries, plan less book x1.5 {k(plan_pay - 1.5*ladder)} = extra Treasuries "
      f"{k(cost27(C.BACKSTOP)*CARRY)} + the ten's price {k(plan_pay - cost27(C.BACKSTOP)*CARRY - 1.5*ladder)}; the ten's"
      f" price = 8b's rise from 7 Oct to 6 Nov {k(ten_held_6nov - ten_held_7oct)} + the tail's year of carry "
      f"{k(base['complete'] - cost27(C.BACKSTOP)*CARRY - (C.PLAIN_COST - 300_000))} - the book above 8b's 7 Oct engine "
      f"value {k(1.5*ladder - ten_held_7oct)}")

# ====================================================================== D. attack 12: per payment, WInS book, 6 Nov
def ytm(clean100, cpn, mat, settle):
    """Street yield (semiannual) from a clean price per 100; standard actual/actual accrual."""
    cds = sorted(E.add_months(mat, -6 * n) for n in range(0, 60))
    nxt = min(d for d in cds if d > settle)
    prv = E.add_months(nxt, -6)
    acc = cpn / 2 * (settle - prv).days / (nxt - prv).days
    rem = [d for d in cds if d >= nxt and d <= mat]
    wfr = (nxt - settle).days / (nxt - prv).days
    dirty = clean100 + acc

    def pv(y):
        return sum((cpn / 2 + (100 if i == len(rem) - 1 else 0)) / (1 + y / 2) ** (wfr + i) for i in range(len(rem)))
    lo, hi = 0.0, 0.2
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if pv(mid) > dirty else (lo, mid)
    return (lo + hi) / 2


SET = date(2026, 10, 7)
fills = {2038: (960.190, 20), 2039: (930.763, 20), 2040: (900.053, 18), 2041: (877.240, 18), 2042: (749.550, 20)}
fund_shares = {2033: 1142, 2034: 1024, 2035: 927, 2036: 894, 2037: 853}
fund_paid = {2033: 21.65, 2034: 22.86, 2035: 23.90, 2036: 23.46, 2037: 23.24}
oct_par = E.load_par(E.ROOT / "competition/official_market_data/daily-treasury-rates_2026-10.csv", "10/07/2026")
ten = sorted(oct_par)
zero_own = C.own_amounts(C.PLAIN, C.ZERO)
print("\nD  per payment, WInS book (6 Nov curve unless marked; scaled payment $33,333)")
gap_cash_days = {2033: "10-12 d", 2034: "10-13 d", 2035: "10-14 d", 2036: "8-12 d", 2037: "10-14 d",
                 2038: "318 d (10.4 mo)", 2039: "229 d (7.5 mo)", 2040: "47 d (1.5 mo)", 2041: "47 d (1.5 mo)",
                 2042: "47 d (1.5 mo)"}
cov = {}
for y in Y:
    inst = I[y]
    if y in E.BONDS:
        px, lots = fills[y]
        _, cp, mat = E.BONDS[y]
        yy = ytm(px / 10, cp, mat, SET)
        cov[y] = lots * 1000 / C.PLAIN[y]
        print(f"   {y} {inst.name:26s} face ${lots*1000:,} | fill {px/10:.4f} clean, yield {yy:.2%} | "
              f"{cov[y]:.2%} of a full rung | pays {k(cov[y]*PAY)} at forwards, {k(cov[y]*zero_own[y])} if cash waiting "
              f"earns nothing | against $33,333: {k(cov[y]*PAY - PAY*2/3)} / {k(cov[y]*zero_own[y] - PAY*2/3)} | "
              f"cash {gap_cash_days[y]} before 1 Jan")
    else:
        wam = E.add_months(date(2026, 11, 4), round(E.ASSUMPTIONS["fund_wam"][y] * 12))
        t = (wam - SET).days / 365.25
        pary = float(np.interp(t, ten, [oct_par[x] for x in ten])) / 100
        print(f"   {y} {inst.name:26s} {fund_shares[y]:,} shares at ${fund_paid[y]} = {k(fund_shares[y]*fund_paid[y])}"
              f" | par curve to the fund's average maturity on 7 Oct {pary:.2%} (stand-in) | about 67.6-67.7% of a "
              f"full rung (card Q17, 23 Oct curve) | about {k(0.676*PAY)}-{k(0.677*PAY)} at forwards, about "
              f"{k(0.676*zero_own[y])}-{k(0.677*zero_own[y])} if cash waiting earns nothing | cash "
              f"{gap_cash_days[y]} before 1 Jan")


def value(units, curve, insts=I):
    """1 Jan 2027 value of fixed flows (each fund's payout on 15 Dec as one amount, as NUMBERS 1's $234 counts it)."""
    return sum(u * a * curve.P(d) for y, u in units.items() for d, a, _ in E.rung_flows(insts[y], C.BASE))


up, dn = E.Curve(c.par, shift=0.0001), E.Curve(c.par, shift=-0.0001)
dv = lambda u: (value(u, dn) - value(u, up)) / 2
liab_dv = (E.ladder_cost(dn) - E.ladder_cost(up)) / 2
close(liab_dv, REG["C3"]["dv01_per_bp"], 0.01, "liability dv01")
plain_dv = dv(C.PLAIN)
close(plain_dv, 234, 0.5, "held dv01 (NUMBERS 1)")
book_units = {y: (cov[y] if y in cov else 0.6765) * C.PLAIN[y] for y in Y}   # funds at card Q17's 67.6-67.7%
print(f"   DV01 (1 Jan 2027 value per 1bp, 6 Nov curve): payments {k(liab_dv)} (scaled x2/3: {k(liab_dv*2/3)}); "
      f"the ten at plain size {k(plain_dv)} ({plain_dv/value(C.PLAIN, c)/1e-4:.2f} years); WInS ladder about "
      f"{k(dv(book_units))} against {k(liab_dv*2/3)} ({dv(book_units)/(liab_dv*2/3):.0%}); the plan's ten plus extra "
      f"Treasuries {k(dv(C.add(C.PLAIN, C.BACKSTOP)))} against {k(liab_dv)} "
      f"({dv(C.add(C.PLAIN, C.BACKSTOP))/liab_dv:.0%})")
fl_units = 3361 * 21.65 / (fund_shares[2033] * 21.65) * book_units[2033]
print(f"   the book's floor stand-in (3,361 IBTM shares) about {k(dv({2033: fl_units}))} a bp more, on no liability")

# ====================================================================== E. attack 25: deposits of $0 to $39,162
print("\nE  a deposit between nothing and the first slice (today's yields; the ladder's tail first, then the extra "
      "Treasuries pro rata)")
tail27 = C.PLAIN_COST - 300_000
tail28 = base["complete"] - cost27(C.BACKSTOP) * CARRY
for dep in (0, 10_000, 20_000, 30_000, base["complete"]):
    tail_share = min(dep / tail28, 1.0)
    frac = max(min((dep - tail28) / (cost27(C.BACKSTOP) * CARRY), 1.0), 0.0)
    own = dict(C.PLAIN)
    own[2033] = C.PLAIN[2033] - (1 - tail_share) * tail27 / I[2033].price
    part = {y: u * frac for y, u in C.BACKSTOP.items()}
    res = {}
    for lab, wld, ins in (("forwards", C.BASE, I), ("zero", C.ZERO, I), ("zero+fee", C.FEEW, I),
                          ("standard", C.FEEW, CUT)):
        L = ledger_rule(wld, ins, own, bucket_own, part)
        res[lab] = (L["short"], {y: round(PAY - v) for y, v in L["paid"].items() if PAY - v > 0.5})
    print(f"   deposit {k(dep):>8s}: extra Treasuries bought {frac:.0%} | short at forwards {k(res['forwards'][0])} "
          f"{res['forwards'][1]} | cash waiting at zero {k(res['zero'][0])} | with the bill fee {k(res['zero+fee'][0])}"
          f" | the standard (fee, funds 0.5% smaller) {k(res['standard'][0])} {res['standard'][1]}")
    if dep in (10_000, 20_000, 30_000):
        close(res["zero"][0], REG["C6"][f"partial_{dep}"]["short_at_zero"], 1, f"C6 {dep}")
    if dep == 0:
        close(res["zero"][0], 57_455, 1, "missed at zero")
        close(res["forwards"][0], 3_016, 1, "missed at forwards")

# ====================================================================== F. attack 27: the all-Treasury plan, same flexibility
at = REG["plan"]["all_treasury"]
d0 = P.run(c, margin_fn=C.margin_fn())
F_all, R0 = float(d0["all_t"]), float(d0["R"])
close(F_all, at["payout_central"], 0.5, "all-T payout")
z0 = float(C.zero_per_dollar(E.J28)) * (1 - C.HAIRCUT)
grow0 = F_all / R0
med = at["final_median_kept_half"]
fm_all = (F_all - med) / grow0
print(f"\nF  all-Treasury, same flexibility: floor money in January 2028 {k(fm_all)}, held back {k(R0 - fm_all)} "
      f"(grows to the FINAL's median half kept {k(med)} at the floor's forwards); pays {k(F_all - med)}; zero-interest "
      f"value less 0.5% {k(fm_all*z0)} -> stated {k(float(C.down(fm_all*z0)))}, known in January 2028; above the "
      f"stated figure {k(F_all - med - float(C.down(fm_all*z0)))}; flexibility in all "
      f"{k(med + F_all - med - float(C.down(fm_all*z0)))} against the FINAL's central $28,682")

# ====================================================================== G. attack 28: the reserve as a schedule
print("\nG  the reserve, payment by payment, if cash waiting earns nothing (own rung / extra Treasuries' cash counted for"
      " that payment / extra covers / carried after)")
zo = C.own_amounts(C.PLAIN, C.ZERO)
zp = C.pool_buckets(C.BACKSTOP, C.ZERO)
paid, avail, carry, left = C.ledger(C.ZERO, C.PLAIN, C.BACKSTOP)
own_face_pay = {y: C.PLAIN[y] * sum(a for _, a, _ in E.rung_flows(I[y], C.ZERO)) for y in Y}
ext_face_pay = {y: C.BACKSTOP[y] * sum(a for _, a, _ in E.rung_flows(I[y], C.ZERO)) for y in Y}
for y in Y:
    print(f"   {y} {I[y].name:26s} own {k(C.PLAIN[y]):>8s} -> pays {k(zo[y]):>8s} | extra {k(C.BACKSTOP[y]):>7s} "
          f"(pays {k(ext_face_pay[y]):>7s} over its life) | extra cash for {y} {k(zp[y]):>7s} | covers "
          f"{k(PAY - zo[y]):>7s} | carried {k(carry[y]):>7s}")
print(f"   totals: own {k(sum(zo.values()))}, extra cash {k(sum(zp.values()))}, left {k(left)}")
close(sum(zo.values()), 445_405, 1, "own at zero")
close(sum(zp.values()), 57_200, 1, "extra at zero")
close(left, 2_604, 1, "left at zero")
print("\nAll asserts passed.")
