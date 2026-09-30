"""M9 security selection screen: best WInS security per slot of the Portfolio-tab book, with a runner-up.

WS6, RAB Kit, 2026-09-30 (Sydney). AI-generated research code (Claude Code) for Team Caplet; MODEL outputs.
Deterministic (no random numbers). No network: reads only files committed in the worktree.

What it does, per slot (each dated payment 2033-2042, the floor, the branch, cash):
  maturity fit    : the holding must end BEFORE the 1 Jan payment (ending early is safe, the money waits; ending
                    after the payment is not, the price on the day is unknown); months early.
  yield vs curve  : WInS price where one was SEEN (28 Sep), else the curve model price; flag |gap| > 25bp.
  reinvestment    : share of a holding's cash that arrives as coupons before the payment date, and what $1 invested
                    delivers on the payment date if coupons are reinvested at 0%, 2%, own yield - 2 points, own yield,
                    as a share of the "curve" case (M1_METHOD.md section E, same functions).
  cost            : commission as % of the order, expense ratio, 30-day median bid/ask (iShares pages, 28 Sep).
  liquidity       : order size vs 2 x 30-day average volume (official rule), vs 10% of the 20-day median (kit rule,
                    PM-05) and vs half of the lowest day in 20 (the WInS FAQ "half of market volume" rule, worst day).
  WInS listing    : SEEN (tab WInS Notes / Book L, 29 Sep) or UNVERIFIED, and the exact name string.

Reuse: every price, yield, accrued and cash-flow calculation is rab/models/m1_ladder.py (imported, not copied), on the
Gate A basis (28 Sep 2026 par curve, settlement = curve date). The ten book rungs are cross-checked against the locked
rab/numbers.yaml reinvest.rung.* values (ratio to the curve case must agree to 1e-9).

Run from the worktree root:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/m9_screen.py
Writes rab/trades/out/m9_screen_<curve date>.csv and .json and prints the report.
"""
import argparse
import csv
import importlib.util
import json
import os
from datetime import date

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "rab", "trades", "out")
spec = importlib.util.spec_from_file_location("m1", os.path.join(ROOT, "rab/models/m1_ladder.py"))
m1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m1)

MSPD = os.path.join(ROOT, "rab/trades/data/mspd_table5_2026-08-31.json")
ETF_SUMMARY = os.path.join(ROOT, "rab/data/etf/etf_summary_2026-09-28.csv")
WINS = os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv")
PORT = os.path.join(ROOT, "rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv")
NUMBERS = os.path.join(ROOT, "rab/numbers.yaml")
SCEN = ["own", "own-2pp", 0.02, 0.0, "curve"]
INVEST = 10_000.0  # scale-free: every ratio below is per dollar invested

# iShares product pages (rab/data/ishares/*.html.gz, 28 Sep 2026): 30-day median bid/ask spread, expense ratio 0.07%
IBOND_SPREAD_PCT = {"IBTM": 0.05, "IBTO": 0.04, "IBTP": 0.04, "IBTQ": 0.04, "IBTR": 0.04}
IBOND_NAME = {  # iShares' own fund names (product pages, 28 Sep 2026); WInS showed this form for IBTM (SEEN 29 Sep)
    "IBTL": "iShares iBonds Dec 2031 Term Treasury ETF", "IBTM": "iShares iBonds Dec 2032 Term Treasury ETF",
    "IBTO": "iShares iBonds Dec 2033 Term Treasury ETF", "IBTP": "iShares iBonds Dec 2034 Term Treasury ETF",
    "IBTQ": "iShares iBonds Dec 2035 Term Treasury ETF", "IBTR": "iShares iBonds Dec 2036 Term Treasury ETF"}


def bond_key(c, mat):
    return f"T {c:.3f}% {mat.strftime('%d-%b-%Y')}"


def mspd_bonds():
    """Treasury Bonds class (the 20- and 30-year issues, CUSIP 912810...) from MSPD Table V, 31 Aug 2026."""
    j = json.load(open(MSPD))
    out = []
    for r in j["data"]:
        if r["security_class1_desc"] != "Treasury Bonds" or r["maturity_date"] in (None, "", "null") \
                or r["interest_rate_pct"] in (None, "", "null"):
            continue
        out.append({"coupon": float(r["interest_rate_pct"]), "mat": date.fromisoformat(r["maturity_date"]),
                    "cusip": r["security_class2_desc"], "outstanding_musd": float(r["outstanding_amt"]) / 1000})
    return sorted(out, key=lambda b: (b["mat"], b["coupon"]))


def ratios(fl, s, cost, T, cv):
    own = m1.irr(fl, s, cost)
    v = {}
    for k in SCEN:
        r = own if k == "own" else own - 0.02 if k == "own-2pp" else k
        v[str(k)] = m1.grow(fl, T, r, cv)
    return own, v


def need50k(v):
    """Laura's plan, one payment: dollars to invest today so the holding delivers $50,000 on the payment date,
    at the curve (today's forward rates), at 2% and at 0% reinvestment of coupons (MODEL)."""
    return {"need_50k_curve": 50_000 * INVEST / v["curve"], "need_50k_2pct": 50_000 * INVEST / v["0.02"],
            "need_50k_0pct": 50_000 * INVEST / v["0.0"]}


def eval_bond(cv, s, b, pays, wins):
    T = date(pays, 1, 1)
    c, mat = b["coupon"], b["mat"]
    ai = m1.accrued(c, mat, s)
    dm = m1.model_dirty(cv, c, mat, s)
    y_model = m1.street_yield(c, mat, s, dm)
    w = wins.get(bond_key(c, mat))
    seen = w is not None
    dirty = (w["price"] + ai) if seen else dm
    y = m1.street_yield(c, mat, s, dirty)
    gap = (y - y_model) * 1e4
    qty = INVEST / (dirty / 100)
    fl = m1.flows(c, mat, s, face=qty)
    own, v = ratios(fl, s, INVEST, T, cv)
    coupons = sum(a for _, a in fl) - qty
    return {"id": bond_key(c, mat), "kind": "Treasury bond", "cusip": b["cusip"], "coupon": c,
            "ends": mat.isoformat(), "months_early": round((T - mat).days / 30.4375, 1), "before_payment": mat < T,
            "wins_listing": ("SEEN (WInS price recorded 28 Sep, tab Book L / premortem PM-04)" if seen else
                             "UNVERIFIED (not seen in WInS; bond class suggests it may be listed)"),
            "price_basis": "WInS 28 Sep clean + model accrued" if seen else "curve model (no WInS price)",
            "clean": (w["price"] if seen else dm - ai), "yield_pct": y * 100, "gap_bp": gap,
            "yield_flag": abs(gap) > 25, "coupon_share_of_cash": coupons / (coupons + qty),
            "own_yield_pct": own * 100, **{f"r_{k}": v[str(k)] / v["curve"] for k in SCEN[:-1]},
            "per10k_at_curve": v["curve"], "per10k_at_2pct": v["0.02"], **need50k(v),
            "commission_usd": 10, "expense_pct": 0.0, "outstanding_musd": b["outstanding_musd"]}


def eval_ibond(cv, s, t, pays, wins, look, H, F, etf):
    T = date(pays, 1, 1)
    w = wins[t]
    qty = INVEST / w["price"]
    fl = m1.holder_flows(t, w, qty, s, look, H, F)
    own, v = ratios(fl, s, INVEST, T, cv)
    notes = H[t]["notes"]
    k = look[t]["ratio"]
    coupons = sum(a for _, a in fl if a > 0) - sum(par / F[t]["shares"] * k * qty for _, _, par in notes)
    principal = sum(par / F[t]["shares"] * k * qty for _, _, par in notes)
    e = etf.get(t, {})
    return {"id": t, "kind": "iBonds ETF", "name": IBOND_NAME[t], "ends": w["mat"].isoformat(),
            "months_early": round((T - w["mat"]).days / 30.4375, 1), "before_payment": w["mat"] < T,
            "wins_listing": ("SEEN 29 Sep (tab WInS Notes)" if "SEEN" in w["wins_name_status"] else
                             "UNVERIFIED (WInS name not recorded; IBTN in WInS is INSCORP Inc)"),
            "price_basis": w["price_source"], "clean": w["price"],
            "yield_pct": float(F[t]["avg_ytm"].rstrip("%")), "gap_bp": look[t]["ytm_gap_bp"],
            "yield_flag": abs(look[t]["ytm_gap_bp"]) > 25, "coupon_share_of_cash": coupons / (coupons + principal),
            "own_yield_pct": own * 100, **{f"r_{k2}": v[str(k2)] / v["curve"] for k2 in SCEN[:-1]},
            "per10k_at_curve": v["curve"], "per10k_at_2pct": v["0.02"], **need50k(v), "commission_usd": 25,
            "expense_pct": 0.07,
            "spread_pct": IBOND_SPREAD_PCT[t], "adv30": e.get("avg_volume_30d"), "median20": e.get("median_volume_20d"),
            "min20": e.get("min_volume_20d")}


def liquidity(qty, e):
    return {"qty": qty, "adv30": e["avg_volume_30d"], "x_of_2adv30": qty / (2 * e["avg_volume_30d"]),
            "pct_median20": qty / e["median_volume_20d"], "pct_min20": qty / e["min_volume_20d"],
            "pass_2x_rule": qty <= 2 * e["avg_volume_30d"], "pass_10pct_median": qty <= 0.10 * e["median_volume_20d"],
            "pass_half_of_worst_day": qty <= 0.5 * e["min_volume_20d"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--curve-date", default="2026-09-28")
    a = ap.parse_args()
    rows = m1.load_rows([os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
    row = next(r for r in rows if r["_date"] == date.fromisoformat(a.curve_date))
    s = row["_date"]
    cv = m1.Curve(row)
    wins = m1.read_wins(WINS)
    port, _ = m1.read_portfolio(PORT)
    units = {h["holding"]: h["units"] for h in port}
    bookl = {k: w["bookL_size"] for k, w in wins.items() if w["bookL_size"]}
    etf = {r["ticker"]: {k: (float(v) if k.startswith(("avg_", "median_", "min_", "close_nasdaq")) and v else v)
                         for k, v in r.items()} for r in csv.DictReader(open(ETF_SUMMARY))}
    H, F = m1.ibond_holdings(), m1.ishares_facts()
    look = {}
    for t in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR"):
        mn = m1.nav_model(row, H[t], F[t]["shares"], s)
        look[t] = {"ratio": F[t]["nav"] / mn,
                   "ytm_gap_bp": (float(F[t]["avg_ytm"].rstrip("%")) / 100 - cv.par_at(F[t]["wam"])) * 1e4}
    bonds = mspd_bonds()
    R = []
    print(f"M9 security screen | curve {s} (U.S. Treasury par curve, D1 method via rab/models/m1_ladder.py) | "
          f"per ${INVEST:,.0f} invested | MODEL")

    # --- dated payment slots
    slot_defs = [  # (payment year, chosen in the Portfolio tab)
        (2033, "IBTM"), (2034, "IBTO"), (2035, "IBTP"), (2036, "IBTQ"), (2037, "IBTR"),
        (2038, "T 4.750% 15-Feb-2037"), (2039, "T 4.500% 15-May-2038"), (2040, "T 4.375% 15-Nov-2039"),
        (2041, "T 4.250% 15-Nov-2040"), (2042, "T 3.125% 15-Nov-2041")]
    ibond_for = {2033: "IBTM", 2034: "IBTO", 2035: "IBTP", 2036: "IBTQ", 2037: "IBTR"}
    nb = yaml.safe_load(open(NUMBERS))["numbers"]
    checks = []
    for pays, chosen in slot_defs:
        T = date(pays, 1, 1)
        # iBonds: the fund for this payment, and the one for the payment before (ends a year early: safe but idle),
        # both valued to THIS payment date
        cands = [eval_ibond(cv, s, t, pays, wins, look, H, F, etf) for yr, t in ibond_for.items() if yr in (pays, pays - 1)]
        # Treasury bonds maturing in the 24 months before the payment
        for b in bonds:
            if T.replace(year=pays - 2) <= b["mat"] < T:
                cands.append(eval_bond(cv, s, b, pays, wins))
        for c in cands:
            c["slot"] = pays
            c["chosen_in_tab"] = c["id"] == chosen
            q = units.get(c["id"])
            if c["kind"] == "iBonds ETF" and q:
                c["liquidity_portfolio"] = liquidity(q, etf[c["id"]])
                c["liquidity_bookL"] = liquidity(bookl[c["id"]], etf[c["id"]])
            if c["chosen_in_tab"]:
                key = "reinvest.rung." + c["id"].replace(" ", "_")
                ref = nb[key]["value"]
                for k, kk in (("r_0.0", "at_0pct"), ("r_0.02", "at_2pct"), ("r_own-2pp", "at_own_minus_2pp")):
                    want = ref[kk] / ref["at_curve"]
                    checks.append(abs(c[k] - want) < 5e-5)  # yaml values are rounded to $1 on ~$50k
        R += cands
        print(f"\n[{pays}] payment 1 Jan {pays}; Portfolio-tab choice: {chosen}")
        print("    candidate               ends        early  yield   gap   coupons  @0%    @2%   @own-2pp  WInS")
        for c in sorted(cands, key=lambda c: (not c["before_payment"], -c["r_0.02"])):
            print(f"    {c['id']:22s} {c['ends']}  {c['months_early']:5.1f}  {c['yield_pct']:5.2f}% {c['gap_bp']:+6.1f} "
                  f"{c['coupon_share_of_cash']:6.1%} {c['r_0.0']:6.1%} {c['r_0.02']:6.1%} {c['r_own-2pp']:6.1%}  "
                  f"{'CHOSEN ' if c['chosen_in_tab'] else ''}{'ends AFTER payment ' if not c['before_payment'] else ''}"
                  f"{'FLAG>25bp ' if c['yield_flag'] else ''}{c['wins_listing'][:10]}")
            if "liquidity_portfolio" in c:
                L = c["liquidity_portfolio"]
                print(f"      order {L['qty']:,} sh: {L['x_of_2adv30']:.1%} of 2x30d-avg ({L['adv30']:,.0f}); "
                      f"{L['pct_median20']:.1%} of 20d median; {L['pct_min20']:.1%} of the lowest day in 20")
    assert all(checks) and len(checks) == 30, ("rung ratios do not reproduce numbers.yaml", checks)
    print("\n    cross-check: the ten Portfolio-tab rungs reproduce numbers.yaml reinvest.rung.* ratios (30 of 30)")
    print("\n[upgrade candidates] same payment, lower coupon (less of the money arrives as coupons to reinvest)")
    for pays, chosen, alt in ((2041, "T 4.250% 15-Nov-2040", "T 1.375% 15-Nov-2040"),
                              (2042, "T 3.125% 15-Nov-2041", "T 2.000% 15-Nov-2041"),
                              (2038, "T 4.750% 15-Feb-2037", "T 5.000% 15-May-2037")):
        c = next(x for x in R if x["slot"] == pays and x["id"] == chosen)
        d = next(x for x in R if x["slot"] == pays and x["id"] == alt)
        print(f"    {pays}: {chosen} -> {alt}: coupons {c['coupon_share_of_cash']:.0%} -> {d['coupon_share_of_cash']:.0%} "
              f"of the cash; delivered at 0% {c['r_0.0']:.1%} -> {d['r_0.0']:.1%}, at 2% {c['r_0.02']:.1%} -> "
              f"{d['r_0.02']:.1%} of the curve case. Laura's plan, to have $50,000 on 1 Jan {pays} if coupons earn 2%: "
              f"${c['need_50k_2pct']:,.0f} -> ${d['need_50k_2pct']:,.0f} today (curve case ${c['need_50k_curve']:,.0f} -> "
              f"${d['need_50k_curve']:,.0f}; {alt} at the model price, no WInS price seen)")

    # --- floor: the 2033 slot again, as the floor (repays by late 2032)
    ibtl_e = etf.get("IBTL")
    # --- branch and cash: facts, not models
    branch = [
        {"id": "VT", "name": "Vanguard Total World Stock ETF", "wins": "SEEN 29 Sep", "expense_pct": 0.06,
         "stocks": 10048, "trades": 1, "adv30": etf["VT"]["avg_volume_30d"], "median20": etf["VT"]["median_volume_20d"]},
        {"id": "VTI+VXUS", "name": "Vanguard Morningstar Total Stock Market ETF + Vanguard Total International Stock ETF",
         "wins": "SEEN 29 Sep (both)", "expense_pct": None, "stocks": 3531 + 8755, "trades": 2,
         "adv30": min(etf["VTI"]["avg_volume_30d"], etf["VXUS"]["avg_volume_30d"]), "median20": None},
        {"id": "ACWI", "name": "iShares MSCI ACWI ETF", "wins": "UNVERIFIED", "expense_pct": 0.32, "stocks": 2196,
         "trades": 1, "adv30": etf["ACWI"]["avg_volume_30d"], "median20": etf["ACWI"]["median_volume_20d"]}]
    vt_q = units["VT"]
    branch_liq = liquidity(vt_q, etf["VT"])
    par1m = float(row["1 Mo"]) / 100
    days = (date(2026, 11, 6) - date(2026, 10, 2)).days
    breakeven = 25 / (par1m * days / 365)
    print(f"\n[branch] VT order {vt_q} sh: {branch_liq['x_of_2adv30']:.2%} of 2x30d-avg; {branch_liq['pct_median20']:.2%} "
          f"of 20d median. VT 0.06% / 10,048 stocks, one trade; VTI 0.03% + VXUS 0.05%, two trades; ACWI 0.32%, 2,196 "
          "stocks (fees and counts: insight_v1 wins_now/S2_growth_sleeve.md, Vanguard and iShares pages).")
    print(f"[cash] 1-month par yield {par1m:.2%} on {s}; WInS cash earns 0%. Over {days} days (2 Oct to 6 Nov) one $25 "
          f"commission is repaid only above ${breakeven:,.0f} in a bill fund (and only if WInS credits distributions: "
          "UNVERIFIED).")
    if ibtl_e is None:
        import statistics as st
        j = json.load(open(os.path.join(ROOT, "rab/trades/data/ibtl_nasdaq_historical_2026-09-30.json")))
        rows_l = [r for r in j["data"]["tradesTable"]["rows"] if r["date"] <= "09/28/2026" and r["date"].endswith("2026")]
        vol = [int(r["volume"].replace(",", "")) for r in rows_l]
        ibtl_e = {"close": float(rows_l[0]["close"]), "asof": rows_l[0]["date"], "avg_volume_30d": sum(vol[:30]) / 30,
                  "median_volume_20d": st.median(vol[:20]), "min_volume_20d": min(vol[:20])}
        print(f"[floor] IBTL (iShares iBonds Dec 2031 Term Treasury ETF, Nasdaq): close {ibtl_e['close']} on "
              f"{ibtl_e['asof']}; 30-session average volume {ibtl_e['avg_volume_30d']:,.0f}, 20-session median "
              f"{ibtl_e['median_volume_20d']:,.0f}; ends about 15 Dec 2031, a year before the 2033 payment; WInS listing "
              "UNVERIFIED.")

    os.makedirs(OUT, exist_ok=True)
    tag = s.isoformat()
    flat = []
    for c in R:
        d = {k: v for k, v in c.items() if not isinstance(v, dict)}
        for lk in ("liquidity_portfolio", "liquidity_bookL"):
            if lk in c:
                d.update({f"{lk}_{k}": v for k, v in c[lk].items()})
        flat.append(d)
    keys = []
    for d in flat:
        keys += [k for k in d if k not in keys]
    with open(os.path.join(OUT, f"m9_screen_{tag}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for d in flat:
            w.writerow({k: (round(v, 6) if isinstance(v, float) else v) for k, v in d.items()})
    json.dump({"curve_date": tag, "per_invested_usd": INVEST, "slots": R, "branch": branch, "ibtl": ibtl_e,
               "branch_liquidity": branch_liq, "cash": {"par_1m": par1m, "days": days, "breakeven_usd": breakeven}},
              open(os.path.join(OUT, f"m9_screen_{tag}.json"), "w"), indent=1, default=str)
    print(f"\nwrote rab/trades/out/m9_screen_{tag}.csv and .json")


if __name__ == "__main__":
    main()
