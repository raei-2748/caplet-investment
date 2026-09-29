"""Build rab/numbers.yaml (DRAFT) from M1's results plus the insight_v1 reference numbers (rab/inventory.md s2).

WS1, RAB Kit, 2026-09-30 (Sydney). AI-generated (Claude Code). WS1 is the only writer of numbers.yaml (PM-35).
Every entry carries: value, unit, quote_as, scale (laura_plan / wins_book / market / history / reference), status,
curve_date, valuation_date, maturity_convention, instrument_basis, method, source, as_of, note.

Run from the worktree root (after m1_ladder.py):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/build_numbers.py
Writes rab/numbers.yaml and rab/numbers.yaml.sha256.
"""
import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
R = json.load(open(os.path.join(ROOT, "rab/models/out/m1_results.json")))
CD = R["meta"]["curve_date"]
SRC = "rab/models/m1_ladder.py -> rab/models/out/m1_results.json"
N = {}

STRIPS = "15 Nov of the year before each payment (STRIPS maturity dates)"
EXACT = "1 Jan 2033 ... 1 Jan 2042 (the payment dates themselves)"
ZERO = "zero-coupon ladder on the par-derived zero curve (D1 method); MODEL, no dealer mark-up"
BOOK_L = ("Book L: the ten WInS-listed holdings (IBTM-IBTR iBonds ETFs + five coupon Treasuries), sized for Laura's "
          "2027 deposit dollar for dollar")


def r0(x):
    return int(round(x))


def k(x, step=1000):
    return f"${int(round(x / step) * step):,}"


def add(id_, value, unit, quote_as, scale, status, source, note="", **basis):
    e = {"value": value, "unit": unit, "quote_as": quote_as, "scale": scale, "status": status}
    e.update(basis)
    e["source"] = source
    if note:
        e["note"] = note
    N[id_] = e


def laura_basis(mat, val=CD, inst=ZERO):
    return dict(curve_date=CD, valuation_date=val, maturity_convention=mat, instrument_basis=inst,
                method="rab/models/M1_METHOD.md section A (D1 method)", as_of=CD)


A = R["A"]
# ---------------------------------------------------------------------------------------------- market
par = A["par_yields_pct"]
add("market.par_curve", {k_: float(v) for k_, v in par.items()}, "percent (semiannual bond-equivalent par yield)",
    f"10-year Treasury yield {float(par['10 Yr']):.2f}% on {CD}", "market", "VERIFIED-PRIMARY",
    "rab/data/treasury_par_2000_2026/2026.csv (home.treasury.gov Daily Treasury Par Yield Curve; byte-identical re-fetch "
    "30 Sep 2026)", curve_date=CD, as_of=CD,
    note="Latest official curve at the fetch (29 Sep 2026 ~10:40 ET; the 29 Sep curve publishes after the close). "
         "FRED DGS series (rab/data/fred/) end 25 Sep and match the Treasury 25 Sep row.")

# ---------------------------------------------------------------------------------------------- Laura: ladder
s, e = A["nov15"], A["exact"]
add("laura.ladder.cost_today_strips", round(s["spot"], 2), "USD", f"about $289,000 at {CD} yields", "laura_plan",
    "MODEL", f"{SRC} A.nov15.spot",
    "HEADLINE for 'what the ten payments cost today'. Equals insight_v1 H3 ($289,119) to the cent.",
    **laura_basis(STRIPS))
add("laura.ladder.cost_2027_strips", round(s["fwd_2027"], 2), "USD",
    "about $292,000 on 1 Jan 2027, locked in at 28 Sep 2026 yields", "laura_plan", "MODEL", f"{SRC} A.nov15.fwd_2027",
    "HEADLINE for 'cost against the $300,000 deposit'. Forward value on the day the deposit arrives. Equals H3.",
    **laura_basis(STRIPS, val="2027-01-01"))
add("laura.ladder.headroom_2027_strips", round(s["headroom_2027"], 2), "USD", "about $7,600 of room under $300,000",
    "laura_plan", "MODEL", f"{SRC} A.nov15.headroom_2027", **laura_basis(STRIPS, val="2027-01-01"))
add("laura.ladder.breakeven_fall_bp_strips", round(s["breakeven_fall_bp"], 1), "basis points",
    "yields would have to fall about a quarter of a percentage point (about 26bp) before 1 Jan 2027",
    "laura_plan", "MODEL", f"{SRC} A.nov15.breakeven_fall_bp", "Parallel shift of the par curve.",
    **laura_basis(STRIPS, val="2027-01-01"))
add("laura.ladder.value_today_exact", round(e["spot"], 2), "USD", "about $287,000", "laura_plan", "MODEL",
    f"{SRC} A.exact.spot", "Value of the payments on their own dates (liability value); not a buyable ladder.",
    **laura_basis(EXACT))
add("laura.ladder.value_2027_exact", round(e["fwd_2027"], 2), "USD", "about $290,000 on 1 Jan 2027", "laura_plan",
    "MODEL", f"{SRC} A.exact.fwd_2027", "Equals the $290,291 in rab/premortem.md PM-24.",
    **laura_basis(EXACT, val="2027-01-01"))
add("laura.ladder.breakeven_fall_bp_exact", round(e["breakeven_fall_bp"], 1), "basis points", "about 33bp",
    "laura_plan", "MODEL", f"{SRC} A.exact.breakeven_fall_bp", **laura_basis(EXACT, val="2027-01-01"))
add("laura.ladder.cost_2027_strips_model_band", [r0(x) for x in s["fwd_2027_band"]], "USD (min, max)",
    "$292,000 give or take $300 across reasonable curve methods", "laura_plan", "MODEL", f"{SRC} A.band",
    "Band over days/365, +1-3M nodes, PCHIP par, linear zero rates. Never quote a single variant.",
    **laura_basis(STRIPS, val="2027-01-01"))
g = A["band"]["days/365 + 1-3M nodes (GPT)"]["nov15"]
add("laura.ladder.gpt_check", {"today": round(g["spot"], 2), "fwd_2027": round(g["fwd_2027"], 2)}, "USD",
    "an independent check agreed within about $200", "laura_plan", "REPRODUCED",
    f"{SRC} A.band['days/365 + 1-3M nodes (GPT)']; research/insight_v1/verification/ladder_2026-09-28/gpt/",
    "ChatGPT's blind figures ($289,003 / $292,214) reproduced to the cent by the D1 method with its two conventions.",
    **laura_basis(STRIPS))
add("laura.ladder.value_2028", {"exact": r0(e["fwd_2028"]), "strips": r0(s["fwd_2028"])}, "USD",
    "about $305,000 on 2 Jan 2028", "laura_plan", "MODEL", f"{SRC} A.*.fwd_2028", "Input to the plan split.",
    **laura_basis("both", val="2028-01-01"))
add("laura.ladder.strips_reinvestment", 0, "USD", "no coupons to reinvest", "laura_plan", "MODEL",
    "M1_METHOD.md A5", "A STRIPS ladder has no coupons; each $50,000 waits 47 days (15 Nov to 1 Jan) in cash. Applies "
    "only if Laura's real plan may use STRIPS (FAQ 'for BOTH contributions': under the strict reading it may not).",
    **laura_basis(STRIPS))

# ---------------------------------------------------------------------------------------------- Laura: split
F = R["F"]
for b, lab in (("nov15", "strips"), ("exact", "exact")):
    f = F[b]
    add(f"laura.plan_split_2028.{lab}", {"ladder": round(f["ladder"], 4), "floor": round(f["floor"], 4),
                                         "stock_fund": round(f["fund"], 4)}, "share of Laura's money on 2 Jan 2028",
        f"ladder {f['ladder']:.0%}, floor {f['floor']:.0%}, stock fund {f['fund']:.0%}", "laura_plan", "MODEL",
        f"{SRC} F.{b}",
        "E6 [7] method on the 28 Sep curve. The Portfolio tab types 65.9 / 24.3 (+1 point cash) / 8.7 (25 Sep, exact "
        "basis). On the STRIPS basis 28 Sep gives 66.0 / 25.2 / 8.8: within 0.1 point of the tab.",
        curve_date=CD, valuation_date="2028-01-02", maturity_convention=STRIPS if b == "nov15" else EXACT,
        instrument_basis="ladder forward value + floor (5-year par, annual) + stock fund", as_of=CD,
        method="M1_METHOD.md section F")
    add(f"laura.stock_fund_2028_usd.{lab}", r0(f["fund_usd"]), "USD", f"about {k(f['fund_usd'])}", "laura_plan",
        "MODEL", f"{SRC} F.{b}.fund_usd", curve_date=CD, valuation_date="2028-01-02",
        maturity_convention=STRIPS if b == "nov15" else EXACT, instrument_basis="growth money minus floor cost", as_of=CD)
add("laura.floor_cost_2028", r0(F["nov15"]["floor_cost"]), "USD",
    "about $117,000 buys the $150,000 floor (at 28 Sep 5-year yield)", "laura_plan", "MODEL", f"{SRC} F.nov15.floor_cost",
    "150,000 / (1 + 5-year par)^5, annual compounding (E6 convention). The rate in Jan 2028 is unknown.",
    curve_date=CD, valuation_date="2028-01-02", maturity_convention="5 years", instrument_basis="floor", as_of=CD)

# ---------------------------------------------------------------------------------------------- history
G = R.get("G", {})
if G:
    hs, he = G["nov15"], G["exact"]
    hb = dict(curve_date="every daily par curve 1990-01-02 .. " + CD, valuation_date="each curve date (same time to "
              "maturity as on " + CD + ")", maturity_convention=STRIPS, instrument_basis=ZERO,
              method="M1_METHOD.md section G (= rab/rescued/ladder_history_2000_2026.py, extended to 1990)", as_of=CD)
    add("history.cost_2020_median", r0(hs["spot"]["y2020_median"]), "USD",
        "about $460,000 at 2020 yields", "history", "REPRODUCED", f"{SRC} G.nov15.spot.y2020_median",
        "Backs the IPS line 'about $460,000 at 2020 yields' (was UNVERIFIED). 2020 range and exact basis below.", **hb)
    add("history.cost_2020_range", [r0(hs["spot"]["y2020_min"]), r0(hs["spot"]["y2020_max"])], "USD (min, max)",
        "$408,000 to $470,000 during 2020", "history", "REPRODUCED", f"{SRC} G.nov15.spot", **hb)
    add("history.cost_max", {"usd": r0(hs["spot"]["max"]), "date": hs["spot"]["max_date"]}, "USD",
        "about $470,000 on 4 Aug 2020, the most expensive day since 1990", "history", "REPRODUCED",
        f"{SRC} G.nov15.spot.max", **hb)
    add("history.cheapest_since", {"spot": hs["spot"]["last_date_at_or_below_today"],
                                   "fwd_2027": hs["fwd_2027"]["last_date_at_or_below_today"],
                                   "exact_spot": he["spot"]["last_date_at_or_below_today"]}, "date",
        "the cheapest since mid-2002", "history", "REPRODUCED", f"{SRC} G.*.last_date_at_or_below_today",
        "Backs 'cheapest since 2002' (was UNVERIFIED): the last day the same payments cost as little as on 28 Sep "
        "2026 was 28 May 2002 (10 Jun 2002 on the 1 Jan 2027 forward basis). Adding 1990-1999 does not change it.", **hb)
    add("history.share_days_le_300k", {"since_2000_spot": round(hs["spot"]["share_days_le_300k_since_2000"], 4),
                                       "since_2000_fwd": round(hs["fwd_2027"]["share_days_le_300k_since_2000"], 4),
                                       "since_1990_spot": round(hs["spot"]["share_days_le_300k_since_1990"], 4)},
        "share of trading days", "on about 1 day in 9 since 2000 would $300,000 have bought all ten payments",
        "history", "REPRODUCED", f"{SRC} G.nov15", **hb)
    add("history.days_priced_since_2000", hs["days_since_2000"], "trading days",
        "every daily Treasury curve since 2000 (about 6,700 days)", "history", "REPRODUCED", f"{SRC} G.nov15",
        "Backs 'tested on every Treasury curve since 2000' in the narrow sense: the ladder cost and the deposit check "
        "run on all of them.", **hb)
    add("history.unfunded_days", {"days": hs["unfunded_days_since_2000"], "of": hs["days_since_2000"],
                                  "years": hs["unfunded_years"], "worst_date": hs["unfunded_worst"]["date"],
                                  "worst_usd_2027": r0(hs["unfunded_worst"]["usd_2027"])}, "trading days / USD",
        "only at 2020-21 yields would part of one payment have been left unfunded (worst about $21,000)", "history",
        "REPRODUCED", f"{SRC} G.nov15.unfunded_*",
        "Day d counts if the 1 Jan 2027 gap exceeds the whole 2028 deposit on that day's curve (deposit on time).",
        **hb)

# ---------------------------------------------------------------------------------------------- reinvestment
E = R["E"]
eb = dict(curve_date=CD, valuation_date="each payment date (1 Jan 2033 ... 1 Jan 2042)",
          maturity_convention="iBonds end 15 Dec of their year; bonds at maturity (up to 10.5 months early)",
          instrument_basis=BOOK_L, method="M1_METHOD.md section E", as_of=CD)
t = E["bookL_totals"]
add("reinvest.bookL_delivered", {"own_yield": r0(t["own"]), "own_minus_2pp": r0(t["own-2pp"]), "at_2pct": r0(t["0.02"]),
                                 "at_0pct": r0(t["0.0"]), "at_curve_forwards": r0(t["curve"])},
    "USD delivered on the ten payment dates (target 500,000 = ten payments of 50,000)",
    "coupons reinvested at today's yields: about $503,000; at 2%: about $466,000; at 0%: about $447,000",
    "laura_plan", "MODEL", f"{SRC} E.bookL_totals",
    "Applies if Laura's real ladder must use WInS-listed instruments (strict FAQ reading). iBonds by look-through "
    "(holdings 24 Sep, scaled to NAV), 0.07% fee, distributions paid when coupons are received.", **eb)
b = E["bookL_buffer"]
add("reinvest.bookL_buffer_cost", {"own_yield": r0(b["own"]), "own_minus_2pp": r0(b["own-2pp"]), "at_2pct": r0(b["0.02"]),
                                   "at_0pct": r0(b["0.0"])}, "USD extra today",
    "about $20,000 more today keeps every payment whole if coupons earn only 2%", "laura_plan", "MODEL",
    f"{SRC} E.bookL_buffer", "More of the same holdings, rung by rung. Compare with the $7,600 headroom.", **eb)
for rr in E["bookL"]:
    add(f"reinvest.rung.{rr['holding'].replace(' ', '_')}", {"pays": rr["pays"], "cost": r0(rr["cost"]),
                                                             "own_yield_pct": round(rr["own_yield"] * 100, 2),
                                                             "at_own": r0(rr["v_own"]), "at_own_minus_2pp": r0(rr["v_own-2pp"]),
                                                             "at_2pct": r0(rr["v_0.02"]), "at_0pct": r0(rr["v_0.0"]),
                                                             "at_curve": r0(rr["v_curve"])}, "USD",
        "per-rung detail; quote only in the Final Report appendix", "laura_plan", "MODEL", f"{SRC} E.bookL", **eb)

# ---------------------------------------------------------------------------------------------- WInS book
B = R["B"]
wb = dict(curve_date=CD, valuation_date=CD, maturity_convention="as held", method="M1_METHOD.md section B", as_of=CD)
for key, lab, q, headline in (("close_0928", "cost_close_0928", "about $294,800 including $200 commission", True),
                              ("close_0928_model_accrued", "cost_model_accrued", "about $295,000", False),
                              ("sheet_as_read", "cost_sheet_as_read", "about $294,600", False)):
    p = B["portfolio"][key]
    add(f"wins.portfolio.{lab}", {"cost": round(p["cost"], 2), "cash_left": round(p["cash_left"], 2),
                                  "commissions": p["commissions"]}, "USD", q, "wins_book", "MODEL",
        f"{SRC} B.portfolio.{key}",
        ("HEADLINE WInS book cost. " if headline else "") +
        {"close_0928": "Portfolio-tab quantities; 28 Sep closes; bond accrued as recorded in the Sheet.",
         "close_0928_model_accrued": "As close_0928 with accrued recomputed (act/act) at 28 Sep; the recorded 0.530 "
                                     "on the May-2038 bond looks wrong (see wins.bond_accrued_mismatch).",
         "sheet_as_read": "Sheet values as displayed 30 Sep 00:30 AEST (ETF prices live 29 Sep intraday)."}[key],
        instrument_basis="Sheet tab Portfolio (Laura's Jan-2028 plan scaled to $300,000)", **wb)
pc = B["portfolio"]["close_0928"]
add("wins.portfolio.holdings_close_0928", [{"holding": r["name"], "qty": r["qty"], "price": round(r["px"], 3),
                                            "value": round(r["value"], 2), "weight": round(r["value"] / 300000, 4)}
                                           for r in pc["rows"]], "USD / share of $300,000",
    "use percentages in notes (e.g. IBTM about a third of the book)", "wins_book", "MODEL",
    f"{SRC} B.portfolio.close_0928.rows", "Bond price = clean + accrued per $100 face; bond qty = face $ (UNVERIFIED "
    "WInS unit, PM-02).", instrument_basis="Sheet tab Portfolio", **wb)
sp = B["portfolio_split_close_0928"]
add("wins.portfolio.split_close_0928", {k_: round(v, 4) for k_, v in sp.items()}, "share of $300,000",
    f"dated Treasury holdings {sp['dated_holdings_incl_floor']:.0%}, world stock fund {sp['vt']:.0%}, cash "
    f"{sp['cash']:.0%}", "wins_book", "MODEL", f"{SRC} B.portfolio_split_close_0928",
    "Dated holdings include IBTM's floor share.", instrument_basis="Sheet tab Portfolio", **wb)
add("wins.portfolio.targets_typed", {"ladder_65.9pct": 197700, "floor_24.3pct": 72900, "stock_fund_8.7pct": 26100,
                                     "cash_1.1pct": 3300, "ibtm_target": 97590}, "USD",
    "the ladder is about two-thirds of the WInS book", "wins_book", "SEEN (Sheet, 30 Sep)",
    "rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv", "Typed-in split x $300,000 (IBTM = its rung + floor).",
    instrument_basis="Sheet tab Portfolio", **wb)
cm = B["cash_margin"]
add("wins.portfolio.cash_margin", {"fall_bp_cash_zero": round(cm["fall_bp_cash_zero"], 1),
                                   "fall_bp_cash_below_1000": round(cm["fall_bp_cash_below_1000"], 1)}, "basis points",
    "if yields fall about a fifth of a point before Friday, re-size the units or cash drops below $1,000",
    "wins_book", "MODEL", f"{SRC} B.cash_margin",
    "Units fixed at the Portfolio tab; bonds and iBonds repriced on a parallel shift; VT unchanged. WS0 rough check "
    "said about 28bp.", instrument_basis="Sheet tab Portfolio", **wb)
for key, lab in (("close_0928", "cost_close_0928"), ("close_0928_model_accrued", "cost_model_accrued")):
    p = B["bookL"][key]
    add(f"wins.bookL.{lab}", {"cost": round(p["cost"], 2), "cash_left": round(p["cash_left"], 2),
                              "commissions": p["commissions"]}, "USD", "about $292,600 including $175 commission",
        "wins_book", "MODEL", f"{SRC} B.bookL.{key}",
        "Book L sizes as displayed at the read (live ETF prices move them). Earlier reads: $292,226 (29 Sep), "
        "$292,244 (30 Sep 00:33 AEST, as displayed). The sizing rule at 28 Sep closes gives $292,417 / cash $7,583.",
        instrument_basis="Sheet tab Book L (literal ladder, one holding per payment)", **wb)
add("wins.bookL.cost_rule_close_0928", {"cost": round(B["bookL_rule"]["cost"], 2),
                                        "cash_left": round(B["bookL_rule"]["cash_left"], 2),
                                        "target_sum": round(sum(r["target"] for r in B["bookL_rule"]["rows"]), 2)},
    "USD", "about $292,400", "wins_book", "MODEL", f"{SRC} B.bookL_rule",
    "Re-runs the Sheet's own sizing rule (target 50,000 x DF(end date), round up) at 28 Sep closes. Target sum "
    "reproduces the Sheet's $290,379.", instrument_basis="Sheet tab Book L", **wb)

# bond checks
for c in R["C"]:
    add(f"wins.bond_check.{c['bond'].replace(' ', '_')}", {"wins_clean": c["wins_clean"],
                                                          "model_clean": round(c["model_clean"], 3),
                                                          "yield_wins_pct": round(c["yield_wins"] * 100, 3),
                                                          "yield_model_pct": round(c["yield_model"] * 100, 3),
                                                          "gap_bp": round(c["gap_bp"], 1), "flag": c["flag"],
                                                          "clean_band_25bp": [round(x, 3) for x in c["clean_band_25bp"]]},
        "price per $100 face / percent / bp",
        "FLAG: price about 1 point of yield off the curve; do not trade at it" if c["flag"] else "within 25bp of the curve",
        "wins_book", "MODEL (price SEEN via Sheet)" if not c["flag"] else "MODEL (price UNVERIFIED, reported stale)",
        f"{SRC} C", "gap = yield of WInS price - yield of curve model price (negative = WInS price rich). The Sheet's "
        "own checks (-8/+6/+13/+14/+15bp) are reproduced (-7.5/+6.2/+12.7/+13.5/+14.6bp) by treating the clean price "
        "as the full price, i.e. they left accrued interest out; with it, all five are -15 to -2bp.",
        curve_date=CD, valuation_date=CD, maturity_convention=c["bond"], instrument_basis=f"CUSIP {c['cusip']}",
        method="M1_METHOD.md section C", as_of=CD)
may = next(c for c in R["C"] if c["bond"] == "T 4.500% 15-May-2038")
add("wins.bond_accrued_mismatch", {"bond": may["bond"], "recorded": may["accrued_recorded"],
                                   "model": round(may["accrued_model"], 4),
                                   "cost_gap_portfolio_19000_face": round((may["accrued_model"] - may["accrued_recorded"]) * 190, 2),
                                   "cost_gap_bookL_29000_face": round((may["accrued_model"] - may["accrued_recorded"]) * 290, 2)},
    "per $100 face / USD", "the Sheet under-counts this bond's accrued interest by about $200-330", "wins_book",
    "MODEL (check in WInS Preview)", f"{SRC} C",
    "The May-2038 bond pays coupons 15 May / 15 Nov (MSPD Table V), so on 28 Sep it has about 136 days of accrued "
    "(1.663 per $100). 0.530 fits a 15 Feb / 15 Aug schedule. Friday: read the accrued WInS shows at Preview.",
    curve_date=CD, valuation_date=CD, maturity_convention="15 May 2038", instrument_basis="CUSIP 912810PX0",
    method="M1_METHOD.md section 2", as_of=CD)
D = R["D"]
add("wins.ibond_checks", {t_: {"avg_ytm_minus_par_at_wam_bp": round(d["ytm_gap_bp"], 1),
                               "premium_to_nav_pct": d["premium_discount_pct"], "nav": d["nav"], "close": d["close"],
                               "lookthrough_nav_ratio": round(d["ratio"], 4), "lookthrough_reliable": d["lookthrough_reliable"]}
                          for t_, d in D.items()}, "bp / percent / USD per share",
    "each iBonds fund's yield is within 2bp of the Treasury curve", "wins_book", "MODEL (inputs VERIFIED-PRIMARY iShares)",
    f"{SRC} D", "Look-through NAV matches for IBTO/IBTP/IBTQ within 0.07%; IBTM/IBTR holdings (24 Sep) and share "
    "counts (28 Sep) do not line up (creations on 25 Sep likely, UNVERIFIED).", curve_date=CD, valuation_date=CD,
    maturity_convention="15 Dec of each fund's year", instrument_basis="iShares iBonds Dec 2032-2036 Term Treasury ETFs",
    method="M1_METHOD.md section D", as_of=CD)

# ---------------------------------------------------------------------------------------------- ETF market data
summ = list(csv.DictReader(open(os.path.join(ROOT, "rab/data/etf/etf_summary_2026-09-28.csv"))))
keep = ["IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "VT", "VTI", "VXUS", "ACWI", "VGIT", "SPTI", "SGOV"]
add("market.etf_2026-09-28", {r["ticker"]: {"close": float(r["close_wins"] or r["close_ishares"] or r["close_nasdaq"]),
                                            "volume": int(r["volume_nasdaq"]), "avg_volume_20d": int(r["avg_volume_20d"]),
                                            "median_volume_20d": int(r["median_volume_20d"]),
                                            "min_volume_20d": int(r["min_volume_20d"]),
                                            "wins_name": r["wins_name_seen_2026-09-29"] or "UNVERIFIED"}
                              for r in summ if r["ticker"] in keep}, "USD per share / shares per day",
    "quote prices only with their date", "market", "VERIFIED-PRIMARY (Nasdaq consolidated; WInS close where seen)",
    "rab/data/etf/etf_summary_2026-09-28.csv", "Ticket prices must come from WInS on the day (PM-29). Avg 20d volume "
    "equals iShares' '30 Day Avg. Volume'.", curve_date="n/a", valuation_date="2026-09-28", as_of="2026-09-28",
    maturity_convention="n/a", instrument_basis="exchange-traded funds", method="rab/data/fetch_snapshot.py S")

# ---------------------------------------------------------------------------------------------- insight_v1 refs
REF = [
    ("ref.H1.ladder_2027_strips_25sep", 294387, "USD", "SUPERSEDED by laura.ladder.cost_2027_strips (28 Sep)",
     "D1_purchase_rule.py [1],[4]; 25 Sep curve; headroom $5,613 = 19bp", "2026-09-25"),
    ("ref.H2.ladder_2027_exact_25sep", 292264, "USD", "SUPERSEDED by laura.ladder.value_2027_exact (28 Sep)",
     "verified_2026-09-27/official_curve_pv.py; 25 Sep curve", "2026-09-25"),
    ("ref.H5.one_in_three", "about 1 in 3", "probability", "RETIRED: 25 Sep (19bp) basis; WS4 gives the reconciled figure",
     "D3_model_v2_results.md, S4_red_team.md, D1 [6], AX1b [C]", "2026-09-25"),
    ("ref.H6.gap_odds_28sep", {"model_nov15": 0.242, "model_exact": 0.187, "history_windows": [0.276, 0.311]},
     "probability", "REFERENCE, WS4 owns (chance the ladder costs more than $300,000 on 1 Jan 2027)",
     "D1 rerun [6] (zero-drift lognormal); AX1b [C] (68-day windows)", "2026-09-28"),
    ("ref.H7.days_over_300k_2026", {"exact": "173/185", "nov15": "176/185", "worst": "27 Feb 2026 $327,631"},
     "trading days", "REFERENCE (2026 curves)", "D1_purchase_rule.py [5]", "2026-09-25"),
    ("ref.H8.rec_2033_total", {"p5": 182000, "p50": 207000, "p95": 250000}, "USD",
     "REFERENCE, WS2 re-verifies on the 28 Sep basis (JPM ACWI 7.00%, 25 Sep, 200k paths)", "E6_final_checks.py [1]-[2]",
     "2026-09-25"),
    ("ref.H9.history_worst", {"rescaled_1928": 169000, "raw": 171000}, "USD", "REFERENCE, WS3 re-verifies",
     "E6_final_checks.py [5] (93 windows 1928-2025)", "2026-09-25"),
    ("ref.H10.stock_fund_2028", {"usd": 40000, "share": 0.087, "of_total": 464000}, "USD",
     "SUPERSEDED by laura.plan_split_2028.* and laura.stock_fund_2028_usd.* (28 Sep)", "E6_final_checks.py [2],[7]",
     "2026-09-25"),
    ("ref.H11.vanguard_like", {"p5": 179000, "p50": 202000, "p95": 242000, "p_top": 0.67}, "USD",
     "REFERENCE, WS2", "E6_final_checks.py [4]", "2026-09-25"),
    ("ref.H13.rates_fall_first", {"-50bp": "fund $20-23k", "-100bp": "fund $1-7k", "-150bp": "no fund; floor $127-137k"},
     "USD", "REFERENCE, WS4", "E6_final_checks.py [8]", "2026-09-25"),
    ("ref.H14.joint_tail_no_deposit", {"-50bp_28sep": 9281, "-100bp_28sep": 28753}, "USD unfunded of the 2033 payment",
     "REFERENCE, WS4", "D1_purchase_rule.py [8] rerun on 28 Sep", "2026-09-28"),
    ("ref.H15.floor_variants", "each $25k less floor: median +$2-3k, p5 -$9-10k", "USD", "REFERENCE, WS2 (D6 memo)",
     "F1_floor_variants.py", "2026-09-25"),
    ("ref.H16.growth_first_miss", {"deposit_150k": 0.032, "deposit_75k": 0.137, "deposit_0": 0.408}, "probability",
     "REFERENCE (not re-run), WS3 M6", "strategy_mc.py via why_us.md", "2026-09-25"),
    ("ref.H19.real_value_50k", {"2033": 42063, "2042": 33681}, "USD of today at 2.5% inflation (ASSUMPTION)",
     "REFERENCE, WS3 M7 recomputes with a sourced inflation input", "strategy_changes.md I4", "n/a"),
]
for id_, v, unit, status, src, asof in REF:
    add(id_, v, unit, "see status", "reference", status, f"research/insight_v1/{src}" if not src.startswith("research")
        else src, "From rab/inventory.md s2 (re-run 30 Sep where marked there).", as_of=asof)

# ---------------------------------------------------------------------------------------------- write
now = datetime.now(timezone.utc)
header = {
    "numbers_yaml": {
        "status": "DRAFT (not locked). Locks at Gate A when a blind second pricer agrees with M1 to $1 (RUN_PLAN s3).",
        "writer": "WS1 only (PM-35). Other streams read; changes after lock go through WS0 with a changelog line.",
        "generated_et": now.astimezone(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M %Z"),
        "generated_sydney": now.astimezone(ZoneInfo("Australia/Sydney")).strftime("%Y-%m-%d %H:%M %Z"),
        "curve_date": CD,
        "rules": ["Quote the quote_as string, not the raw value, in anything the team reads.",
                  "Tag every dollar figure laura_plan or wins_book; WInS notes use percentages or say 'in Laura's plan'.",
                  "MODEL = model output, not a market quote. Round to $1k (ranges to $5k) outside appendices.",
                  "Dated-holdings claims carry the coupon-reinvestment caveat (reinvest.*)."],
    }
}
out = os.path.join(ROOT, "rab/numbers.yaml")
with open(out, "w") as f:
    f.write("# rab/numbers.yaml - single source of RAB Kit numbers. Generated by rab/models/build_numbers.py; do not "
            "hand-edit.\n")
    yaml.safe_dump(header, f, sort_keys=False, width=118, allow_unicode=False)
    yaml.safe_dump({"numbers": N}, f, sort_keys=False, width=118, allow_unicode=False)
h = hashlib.sha256(open(out, "rb").read()).hexdigest()
open(out + ".sha256", "w").write(f"{h}  rab/numbers.yaml\n")
print(f"wrote rab/numbers.yaml ({len(N)} entries), sha256 {h}")
