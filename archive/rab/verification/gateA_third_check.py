"""Gate A third pricer: a minimal, standard-library-only recomputation of M1 sections A3, B1 and C.

WS1-reconciler, 2026-09-30 (Sydney). AI-generated verification (Claude Code) for Team Caplet; no deliverable text.
Written from rab/models/M1_METHOD.md (sections 2, A1-A3, A6, B1-B3, B6, C1-C5) and the raw inputs I1, I3, I4 only.
It does not import numpy, scipy, m1_ladder.py or blind_pricer.py, and solves by bisection (the others use brentq).
It compares its numbers with the two existing implementations (rab/models/out/m1_results.json and
rab/verification/blind_m1/results.json) and with rab/numbers.yaml, compares primary vs blind on the other sections
both built (A4, B, C, F, G), and exits non-zero if anything differs by more than the spec tolerance
($1; 0.01bp for break-evens; 0.5bp for C yields; $100 for G). See gateA_reconciliation.md.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateA_third_check.py
"""
import csv
import json
import math
import os
import sys
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
I1 = os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")
I3 = os.path.join(ROOT, "rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv")
I4 = os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv")
PRIMARY = os.path.join(ROOT, "rab/models/out/m1_results.json")
BLIND = os.path.join(ROOT, "rab/verification/blind_m1/results.json")
OUT = os.path.join(ROOT, "rab/verification/gateA_third_check.json")

D = date(2026, 9, 28)                      # curve date = valuation = settlement (spec s2)
A27, A28 = date(2027, 1, 1), date(2028, 1, 1)
DEPOSIT, PAY = 300_000.0, 50_000.0
TENORS = [("1 Mo", 1 / 12), ("2 Mo", 2 / 12), ("3 Mo", 0.25), ("6 Mo", 0.5), ("1 Yr", 1.0), ("2 Yr", 2.0),
          ("3 Yr", 3.0), ("5 Yr", 5.0), ("7 Yr", 7.0), ("10 Yr", 10.0), ("20 Yr", 20.0), ("30 Yr", 30.0)]
DATES = {"exact": [date(y, 1, 1) for y in range(2033, 2043)],          # A2: the payment dates
         "nov15": [date(y - 1, 11, 15) for y in range(2033, 2043)]}    # A2: STRIPS maturities (A6 headline)


def interp(x, xs, ys):
    """Piecewise-linear interpolation, flat outside [xs[0], xs[-1]]."""
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    k = 1
    while xs[k] < x:
        k += 1
    w = (x - xs[k - 1]) / (xs[k] - xs[k - 1])
    return ys[k - 1] + w * (ys[k] - ys[k - 1])


def curve_row(day):
    with open(I1, newline="") as f:
        for r in csv.DictReader(f):
            if r["Date"] == day.strftime("%m/%d/%Y"):
                return r
    raise SystemExit(f"curve {day} not in {I1}")


def make_df(row, shift_bp=0.0):
    """A1: linear par grid every 0.5y to 30y, bootstrap, log-linear DF in t = days/365.25."""
    pts = [(t, float(row[k]) / 100 + shift_bp / 10_000) for k, t in TENORS if row.get(k, "").strip()]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    grid = [0.5 * j for j in range(1, 61)]
    annuity, lndf = 0.0, []                  # annuity = DF_1 + ... + DF_{j-1}
    for t in grid:
        c = interp(t, xs, ys) / 2
        df = (1 - c * annuity) / (1 + c)
        # self-check: the grid par bond reprices to 1 on its own discount factors
        assert abs(c * (annuity + df) + df - 1) < 1e-12
        annuity += df
        lndf.append(math.log(df))
    gx, gy = [0.0] + grid, [0.0] + lndf
    return lambda d: math.exp(interp((d - D).days / 365.25, gx, gy))


def liability(row, basis, shift_bp=0.0):
    df = make_df(row, shift_bp)
    v0 = sum(PAY * df(d) for d in DATES[basis])
    return {"spot": v0, "fwd_2027": v0 / df(A27), "fwd_2028": v0 / df(A28)}


def breakeven_fall_bp(row, basis):
    """A3: the fall b (bp, positive) at which the 1 Jan 2027 value reaches $300,000; bisection to 1e-6 bp."""
    lo, hi = 0.0, 200.0                      # value rises as yields fall
    assert liability(row, basis, -lo)["fwd_2027"] < DEPOSIT < liability(row, basis, -hi)["fwd_2027"]
    while hi - lo > 1e-6:
        mid = (lo + hi) / 2
        if liability(row, basis, -mid)["fwd_2027"] < DEPOSIT:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def add_months(d, n):
    y, m = divmod(d.month - 1 + n, 12)
    y, m = d.year + y, m + 1
    last = [31, 29 if y % 4 == 0 and (y % 100 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    return date(y, m, min(d.day, last))


def coupon_dates(mat):
    """Spec s2: M, M-6m, M-12m, ... (same day, clamped). All bonds here mature on the 15th, so no end-of-month case."""
    assert mat.day == 15
    out, k = [], 0
    while True:
        d = add_months(mat, -6 * k)
        out.append(d)
        if d <= D:
            return sorted(out)
        k += 1


def yield_check(row):
    """Section C, steps 1-4, with bisection (the other two builders use scipy brentq)."""
    df = make_df(row)
    px = list(csv.DictReader(open(I4, newline="")))
    out = {}
    for p in px:
        if p["type"] != "Treasury":
            continue
        c, mat, clean = float(p["coupon_pct"]), date.fromisoformat(p["maturity"]), float(p["price"])
        sched = coupon_dates(mat)
        prev = max(d for d in sched if d <= D)
        nxt = [d for d in sched if d > D]
        acc = c / 2 * (D - prev).days / (nxt[0] - prev).days
        cfs = [c / 2 + (100 if d == mat else 0) for d in nxt]
        w = (nxt[0] - D).days / (nxt[0] - prev).days
        dirty_model = sum(cf * df(d) for cf, d in zip(cfs, nxt))          # DF(S) = 1 because S = D

        def ytm(price):
            lo, hi = -0.05, 0.5
            for _ in range(200):
                mid = (lo + hi) / 2
                pv = sum(cf / (1 + mid / 2) ** (k + w) for k, cf in enumerate(cfs))
                lo, hi = (mid, hi) if pv > price else (lo, mid)
            return (lo + hi) / 2
        gap = (ytm(clean + acc) - ytm(dirty_model)) * 10_000
        out[p["instrument"]] = {"accrued_model": acc, "gap_bp": gap, "flag": abs(gap) > 25}
    return out


def num(s):
    s = s.replace("$", "").replace(",", "").strip()
    return float(s) if s else None


def portfolio_book():
    """B1-B3: Portfolio tab quantities (I3 units column) at close_0928 prices (I4), recorded accrued."""
    px = {}
    with open(I4, newline="") as f:
        for r in csv.DictReader(f):
            px[r["instrument"]] = r
    rows, started = [], False
    with open(I3, newline="") as f:
        for r in csv.reader(f):
            if len(r) > 7 and r[1] == "Holding":
                started = True
                continue
            if started and r[1] in px:
                rows.append((r[1], num(r[7])))
    out = []
    for name, qty in rows:
        p = px[name]
        if p["type"] == "ETF":
            price, value, comm = float(p["price"]), qty * float(p["price"]), 25.0
        else:
            price = float(p["price"]) + float(p["accrued_per100_recorded"])     # dirty per 100 face
            value, comm = qty * price / 100, 10.0
        out.append({"ticker": name, "quantity": qty, "price": price, "value": value, "commission": comm,
                    "cost_usd": value + comm})
    return out


def other_sections(P, B):
    """Primary vs blind on everything else both built (A4, B other price sets and Book L, C, F, G).
    Comparison only; the third pricer does not recompute these. Tolerances from the spec: $1, 0.5bp, G $100."""
    rows = []
    for pv, bv in (("days/365", "i_days365"), ("days/365 + 1-3M nodes (GPT)", "ii_days365_short_nodes"),
                   ("PCHIP par interpolation", "iii_pchip"), ("linear zero rates", "iv_zero_linear")):
        for basis in ("nov15", "exact"):
            rows.append((f"A4 {bv} {basis} spot", P["A"]["band"][pv][basis]["spot"],
                         B["A"]["A4_model_risk_band"][bv][basis]["V0_spot"], 1.0))
            rows.append((f"A4 {bv} {basis} fwd_2027", P["A"]["band"][pv][basis]["fwd_2027"],
                         B["A"]["A4_model_risk_band"][bv][basis]["V_A_1jan2027"], 1.0))
    for book in ("portfolio", "bookL"):
        for ps in ("sheet_as_read", "close_0928", "close_0928_model_accrued"):
            if ps in P["B"][book] and ps in B["B"][book]:
                rows.append((f"B {book} {ps} cost", P["B"][book][ps]["cost"], B["B"][book][ps]["cost"], 1.0))
    for c in P["C"]:
        bc = B["C"][c["bond"]]
        rows.append((f"C {c['bond']} gap_bp", c["gap_bp"], bc["gap_bp"], 0.5))
        rows.append((f"C {c['bond']} gap_vs_par_bp", c["gap_vs_par_bp"], bc["yield_minus_par_at_maturity_bp"], 0.5))
    for basis in ("nov15", "exact"):
        for pk, bk in (("ladder", "share_ladder"), ("floor", "share_floor"), ("fund", "share_fund")):
            rows.append((f"F {basis} {pk} share x 100", 100 * P["F"][basis][pk], 100 * B["F"][basis][bk], 0.05))
    gmap = {("nov15", "spot"): "V0_nov15", ("nov15", "fwd_2027"): "V_A_nov15",
            ("exact", "spot"): "V0_exact", ("exact", "fwd_2027"): "V_A_exact"}
    date_rows = []
    for (basis, kind), bk in gmap.items():
        pg, bg = P["G"][basis][kind], B["G"][bk]
        for pk, bkk in (("y2020_median", "2020_median"), ("y2020_min", "2020_min"), ("y2020_max", "2020_max"),
                        ("max", "all_time_max")):
            rows.append((f"G {basis} {kind} {pk}", pg[pk], bg[bkk], 100.0))
        date_rows.append((f"G {basis} {kind} cheapest since", pg["last_date_at_or_below_today"],
                          bg["cheapest_since_last_date_at_or_below_D"]))
        date_rows.append((f"G {basis} {kind} max date", pg["max_date"], bg["all_time_max_date"]))
        if kind == "fwd_2027":
            for pk in ("share_days_le_300k_since_2000", "share_days_le_300k_since_1990"):
                rows.append((f"G {basis} V_A {pk} x 100", 100 * pg[pk], 100 * bg[pk], 0.05))
            rows.append((f"G {basis} deposit check days", P["G"][basis]["unfunded_days_since_2000"],
                         bg["deposit_check_days_unfunded"], 0.5))
            rows.append((f"G {basis} deposit check worst", P["G"][basis]["unfunded_worst"]["usd_2027"],
                         bg["deposit_check_max_unfunded"], 100.0))
    fails = [n for n, p, b, tol in rows if abs(p - b) >= tol] + [n for n, p, b in date_rows if p != b]
    worst = max(abs(p - b) for n, p, b, tol in rows)
    print(f"\nprimary vs blind, other sections: {len(rows)} numbers + {len(date_rows)} dates compared; "
          f"largest difference {worst:.2e}; failures: {fails or 'none'}")
    return {"n_numbers": len(rows), "n_dates": len(date_rows), "max_abs_diff": worst, "fails": fails}


def main():
    row = curve_row(D)
    res = {"curve_date": D.isoformat(), "A": {}, "B": {}}
    for basis in ("nov15", "exact"):
        L = liability(row, basis)
        L["headroom_2027"] = DEPOSIT - L["fwd_2027"]
        L["breakeven_fall_bp"] = breakeven_fall_bp(row, basis)
        res["A"][basis] = L
    book = portfolio_book()
    assert len(book) == 11, [b["ticker"] for b in book]
    res["B"]["portfolio_close_0928"] = {"holdings": book, "cost": sum(b["cost_usd"] for b in book),
                                        "commissions": sum(b["commission"] for b in book)}
    res["B"]["portfolio_close_0928"]["cash_left"] = DEPOSIT - res["B"]["portfolio_close_0928"]["cost"]
    res["headline"] = {"pv_ten_payments_usd": res["A"]["nov15"]["spot"], "basis": "nov15 (A6)",
                       "book_total_cost_usd": res["B"]["portfolio_close_0928"]["cost"]}

    # ---- compare with the primary (m1_ladder.py) and the blind rebuild
    P, B = json.load(open(PRIMARY)), json.load(open(BLIND))
    checks = []
    for basis in ("nov15", "exact"):
        for key, pk, bk in (("spot", "spot", "V0_spot"), ("fwd_2027", "fwd_2027", "V_A_1jan2027"),
                            ("fwd_2028", "fwd_2028", "V_1jan2028"),
                            ("headroom_2027", "headroom_2027", "headroom_vs_300k")):
            checks.append((f"A {basis} {key}", res["A"][basis][key], P["A"][basis][pk], B["A"][basis][bk], "USD"))
        checks.append((f"A {basis} breakeven_fall_bp", res["A"][basis]["breakeven_fall_bp"],
                       P["A"][basis]["breakeven_fall_bp"], B["A"][basis]["breakeven_parallel_fall_bp"], "bp"))
    pb, bb = P["B"]["portfolio"]["close_0928"], B["B"]["portfolio"]["close_0928"]
    mine = res["B"]["portfolio_close_0928"]
    checks.append(("B Portfolio close_0928 cost", mine["cost"], pb["cost"], bb["cost"], "USD"))
    checks.append(("B Portfolio close_0928 cash_left", mine["cash_left"], pb["cash_left"], bb["cash_left"], "USD"))
    for h, p_row, b_row in zip(book, pb["rows"], bb["rows"]):
        assert h["ticker"] == p_row["name"] == b_row["ticker"]
        checks.append((f"B {h['ticker']} cost_usd", h["cost_usd"], p_row["value"] + p_row["commission"],
                       b_row["cost"], "USD"))
    ph = P.get("headline")
    if ph:
        checks.append(("headline pv_ten_payments_usd", res["headline"]["pv_ten_payments_usd"],
                       ph["pv_ten_payments_usd"], B["A"]["nov15"]["V0_spot"], "USD"))
        checks.append(("headline book_total_cost_usd", res["headline"]["book_total_cost_usd"],
                       ph["book_total_cost_usd"], bb["cost"], "USD"))

    # ---- numbers.yaml (DRAFT) must carry the same headline values, rounded as it stores them
    try:
        import yaml
        NY = yaml.safe_load(open(os.path.join(ROOT, "rab/numbers.yaml")))["numbers"]
        ny = {"laura.ladder.cost_today_strips": res["A"]["nov15"]["spot"],
              "laura.ladder.cost_2027_strips": res["A"]["nov15"]["fwd_2027"],
              "laura.ladder.headroom_2027_strips": res["A"]["nov15"]["headroom_2027"],
              "laura.ladder.value_today_exact": res["A"]["exact"]["spot"],
              "laura.ladder.value_2027_exact": res["A"]["exact"]["fwd_2027"]}
        for k, v in ny.items():
            checks.append((f"numbers.yaml {k}", v, NY[k]["value"], NY[k]["value"], "USD"))
        checks.append(("numbers.yaml wins.portfolio.cost_close_0928", mine["cost"],
                       NY["wins.portfolio.cost_close_0928"]["value"]["cost"],
                       NY["wins.portfolio.cost_close_0928"]["value"]["cost"], "USD"))
    except ImportError:
        print("pyyaml not available: numbers.yaml cross-check skipped")

    # ---- section C yield gaps (tolerance 0.5bp) and the 25bp stale-price flags
    res["C"] = yield_check(row)
    for c in P["C"]:
        mine_c, bc = res["C"][c["bond"]], B["C"][c["bond"]]
        checks.append((f"C {c['bond'][:22]} gap", mine_c["gap_bp"], c["gap_bp"], bc["gap_bp"], "bp_c"))
        if not mine_c["flag"] == c["flag"] == bc["flag_stale"]:
            checks.append((f"C {c['bond'][:22]} FLAG MISMATCH", 1, 0, 0, "bp_c"))

    worst, fails = 0.0, []
    print(f"{'quantity':42s} {'third':>14s} {'primary':>14s} {'blind':>14s} {'max |diff|':>11s}")
    for name, t, p, b, unit in checks:
        d = max(abs(t - p), abs(t - b), abs(p - b))
        tol = {"USD": 1.0, "bp": 0.01, "bp_c": 0.5}[unit]
        if d >= tol:
            fails.append(name)
        if unit == "USD":
            worst = max(worst, d)
        print(f"{name:42s} {t:14.2f} {p:14.2f} {b:14.2f} {d:11.2e} {unit}")
    res["comparison"] = {"n_checks": len(checks), "max_abs_diff_usd": worst, "fails": fails,
                         "tolerance": "$1 (USD), 0.01bp (break-even), 0.5bp (C yields)"}
    res["primary_vs_blind_other_sections"] = other_sections(P, B)
    fails += res["primary_vs_blind_other_sections"]["fails"]
    json.dump(res, open(OUT, "w"), indent=1, default=str)
    print(f"\n{len(checks)} checks; largest dollar difference ${worst:.2e}; failures: {fails or 'none'}")
    print(f"headline (A6): ten payments ${res['headline']['pv_ten_payments_usd']:,.2f} on the Nov-15 basis; "
          f"exact basis ${res['A']['exact']['spot']:,.2f} (secondary); Portfolio close_0928 cost "
          f"${res['headline']['book_total_cost_usd']:,.2f}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
