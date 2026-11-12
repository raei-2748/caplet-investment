"""Data for the Final Report exhibits, on the register of Tue 10 Nov 2026 (rebuilt Wed 11 Nov 2026, Sydney).

Design H_plain ("sufficient without reinvestment", with the fee cushion), the Treasury curve of Fri 6 Nov 2026, the
range rule on the fund's holdings and Keel's reading of "most". Everything modelled is MODEL (NUMBERS.md stamp).

Where the figures come from:
  Table 1  (Section 2)      NUMBERS.md 8g version 2, the WInS record at cost. No results file holds it, so the rows are
                            copied here by hand and check() compares every cell with the 8g table. Since Thu 12 Nov
                            evening also the units bought against the targets set before trading (NUMBERS 8m), checked
                            against 8m, the Portfolio tab (portfolio.csv) and the 23 Oct WInS snapshot.
  Figure 1 (3a)             numbers/results_reserve_2026-11-10.json (NUMBERS 8h): blocks composition_1jan2033_base,
                            base (today's forwards), fee (nothing earns interest and waiting money pays the ETF's fee:
                            Keel's standard, SKELETON Exhibits item 2) and zero (nothing earns interest, no fee).
  Table 2  (3b, 3c)         numbers/results_joint_stress_2026-11-10.json (NUMBERS 8i, 8j): scenarios forwards, minus3
                            and inflation; joint.named 2006-06 and 2007-07; the 585-window percentiles; and
                            twd_test.joint_replay for the contribution and the flexibility across windows.
  Cross-check (8k)          numbers/results_returns_2026-11-10.json: the flexibility at forwards by a second route.
  Figure 1, Fri 13 Nov      numbers/results_topup_2026-11-13.json (NUMBERS 8h): when each payment's cash reaches Laura
                            (a fund's end date is not its cash date; a bond due on a weekend or holiday pays the next
                            business day), and the top-up's column reconciled with its cost (the note items).

Nothing is computed here except rounding, sums and the joining of two parts the register names (the flexibility is the
half kept plus the excess, NUMBERS 8i column "Half kept plus excess"). Run this file to print every exhibit figure and
the check against NUMBERS.md; it exits with 1 if any figure fails.

    python3 keel/final_report/exhibits/exhibit_data.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FR = os.path.normpath(os.path.join(HERE, ".."))
NUMBERS_DIR = os.path.join(FR, "numbers")
NUMBERS_MD = os.path.join(FR, "NUMBERS.md")
TNA_TXT = os.path.normpath(os.path.join(FR, "..", "drafts", "writing_room_2026-11-03", "tna_as_submitted.txt"))
# Every WInS trade note as copied 13 Oct (CANON's "WN"); the May-2038 note (WN l.17) is not one of the TNA's three.
WN_TXT = os.path.normpath(os.path.join(FR, "..", "..", "caplet", "google_drive", "ips_report",
                                       "05_trading_note_reflection_wins_trading_notes.md"))
# The 23 Oct WInS export with its "Pays for" column (NUMBERS 8g cites it for what the book stands for)
SNAPSHOT_MD = os.path.normpath(os.path.join(FR, "..", "..", "competition", "wins", "2026-10-23_snapshot.md"))
# The Portfolio tab's target units, set before the first fill (NUMBERS 8m cites portfolio.csv l.20-31)
PORTFOLIO_CSV = os.path.normpath(os.path.join(FR, "..", "..", "caplet", "google_drive", "sheets",
                                              "portfolio_and_trading_notes", "portfolio.csv"))
REGISTER_DATE = "2026-11-10"


def _load(name):
    with open(os.path.join(NUMBERS_DIR, name)) as fh:
        return json.load(fh)


RESERVE = _load(f"results_reserve_{REGISTER_DATE}.json")
JOINT = _load(f"results_joint_stress_{REGISTER_DATE}.json")
RETURNS = _load(f"results_returns_{REGISTER_DATE}.json")
MAIN = _load(f"results_{REGISTER_DATE}.json")          # NUMBERS sections 1-5 (Table 3: the top-up, section 5's distances)
INPUTS = _load("inflation_inputs.json")                # NUMBERS 8d's inputs (Table 3: the Taiwan dollar, building costs)
TOPUP_PAID = _load("results_topup_2026-11-13.json")    # NUMBERS 8h, Fri 13 Nov: the top-up reconciled; the cash dates
SKELETON_MD = os.path.join(FR, "SKELETON.md")         # Table 3's definitions and dates are Keel's calls, set out there
WORDS_MD = os.path.join(FR, "WORDS.md")               # the report's one name for each thing

assert RESERVE["stamp"]["design"] == "H_plain" and RESERVE["stamp"]["curve"] == "11/06/2026", RESERVE["stamp"]
assert JOINT["stamp"]["curve"] == "11/06/2026", JOINT["stamp"]


def dollars(v):
    return f"${v:,.0f}"


def cents(v):
    return f"${v:,.2f}"


def cents_plain(v):
    """Table 1's amounts: the dollar sign is in the column head ("Amount ($)"), which buys the "Pays for" column."""
    return f"{v:,.2f}"


def hundreds(v):
    return f"${round(v / 100) * 100:,.0f}"


# =================================================================================================================
# Table 1, the holdings (Section 2; Wharton requires it). NUMBERS 8g version 2. Not a model.
# =================================================================================================================
# (identifier as 8g gives it, name, asset type as 8g gives it, amount at cost, % of $300,000, role in the plan)
# The role is the 23 Oct snapshot's "Pays for" column (NUMBERS 8g cites it), except VT's, where the snapshot says only
# "growth sleeve": IPS l.15 gives VT's two jobs (its returns set the top; half of it is promised to no one). Table 1
# prints it short (PAYS_FOR_PRINT); the template's measuring variant reads it too.
HOLDINGS = [
    ("IBTM", "iShares iBonds Dec 2032 Term Treasury ETF", "ETF (Treasury)", 97489.95, 32.50, "2033 payment and floor stand-in"),
    ("IBTO", "iShares iBonds Dec 2033 Term Treasury ETF", "ETF (Treasury)", 23408.64, 7.80, "2034 payment"),
    ("IBTP", "iShares iBonds Dec 2034 Term Treasury ETF", "ETF (Treasury)", 22155.30, 7.39, "2035 payment"),
    ("IBTQ", "iShares iBonds Dec 2035 Term Treasury ETF", "ETF (Treasury)", 20973.24, 6.99, "2036 payment"),
    ("IBTR", "iShares iBonds Dec 2036 Term Treasury ETF", "ETF (Treasury)", 19823.72, 6.61, "2037 payment"),
    ("(WInS id)", "T-Bond 4.750% 15-Feb-2037", "Treasury bond", 19203.80, 6.40, "2038 payment"),
    ("532281 (probably)", "T-Bond 4.500% 15-May-2038", "Treasury bond", 18615.26, 6.20, "2039 payment"),
    ("(WInS id)", "T-Bond 4.375% 15-Nov-2039", "Treasury bond", 16200.95, 5.40, "2040 payment"),
    ("(WInS id)", "T-Bond 4.250% 15-Nov-2040", "Treasury bond", 15790.32, 5.26, "2041 payment"),
    ("(WInS id)", "T-Bond 3.125% 15-Nov-2041", "Treasury bond", 14991.00, 5.00, "2042 payment"),
    ("VT", "Vanguard Total World Stock ETF", "ETF (equity)", 26524.61, 8.84, "Growth: top of the range and the half kept"),
    ("N/A", "Cash", "Cash", 3513.79, 1.17, "Cash"),
    ("N/A", "Commissions and bond interest paid at purchase", "Cost", 1309.42, 0.44, "Cost of buying"),
]
HOLDINGS_TOTAL = (300000.00, 100.00)  # 8g: "must equal $300,000 and 100%"
N_TREASURIES = 10                      # the first ten rows, in payment order 2033-2042
HOLDINGS_NOTE_FACTS = {"commissions": 200.00, "accrued_interest": 1109.42, "wins_cash": 3513.79,
                       "trade_dates": "6-7 Oct 2026 (U.S. Eastern)"}

# How Table 1 prints 8g's cells. Placeholders are in square brackets until Caplet's final WInS export (8g
# "Identifiers"); 532281 is Wharton's own example row and still to confirm. Asset types: 8g's "ETF (Treasury)" and
# "ETF (equity)" in plain words; at 12 pt "ETF (Treasury)" would push the longest fund name off one line.
ID_PRINT = {"(WInS id)": "[ID]", "532281 (probably)": "[532281]"}
# The costs row (Thu 12 Nov evening; panel 2: "the fees and accrued-interest row must not look like a holding", faculty
# judge; "the extra row for money that left at purchase is not in Wharton's example", finalist judge). It now sits
# below an "All holdings" subtotal, its label runs across the first four columns (no ticker, no asset type, no units)
# and says what it is: costs at purchase, not a holding. Same money as 8g's row: the $200 of commissions ("fees", as
# SKELETON 2.5 and 8m's "Cost" row say it) and the $1,109.42 of bond interest accrued at purchase. 3.86 in at 12 pt;
# the four columns hold 4.27 in. Wed 11 Nov's "Commissions and accrued interest at purchase" read as a holding.
NAME_PRINT = {"Commissions and bond interest paid at purchase":
              "Costs at purchase, not a holding: fees and accrued interest"}
COSTS_ROW = len(HOLDINGS) - 1          # the last 8g row; not a holding
HOLDINGS_LABEL = "All holdings"        # the twelve holdings, cash included (Wharton's example lists cash as a row)
LABEL_SPAN = 4                         # label rows (the two subtotals, the costs row) run across columns 1-4

# Units bought against the targets set before trading (Thu 12 Nov evening; SKELETON's density cut, row 2.5: "the targets
# become one column of Table 1 (units bought against target), not a second table"). NUMBERS 8m, typed in like the rows
# above and checked against 8m's text, the Portfolio tab's target units (portfolio.csv l.20-31, 8m's source), the
# 23 Oct snapshot's quantities, and units x price paid = 8g's amount. Bonds trade in units of $1,000 of face value (8m
# "lots of $1,000"). VT's target was the cash then left (8m), 164 shares at 2 Oct prices; it was bought last (order 11,
# filled 7 Oct, 8:27 PM ET), after the ten Treasuries. In the order of HOLDINGS: (units held, target units).
UNITS = [(4503, 4503), (1024, 1024), (927, 927), (894, 894), (853, 853),
         (20, 20), (20, 20), (18, 18), (18, 18), (20, 20),
         (167, 164)]
# VT's cell carries why its two numbers differ (the brief: "167 / 164, bought last from the cash left"; "from the cash
# left" needs 1.17 in, the column holds 0.97, so "from cash left"). VT's row is two lines already (its name and its
# "Pays for" wrap), so the third line costs one single-spaced line.
VT_UNITS_WORDS = ("bought last,", "from cash left")
UNITS_HEAD = "Units bought / target"
# Since the "Pays for" column (fresh reader, Wed 11 Nov) the types are one word, Wharton's own ("ETF", and "Bond" for
# its "Treasury Bond"): each name already says Treasury, T-Bond or Stock.
TYPE_PRINT = {"ETF (Treasury)": "ETF", "ETF (equity)": "ETF", "Treasury bond": "Bond", "Cash": "Cash", "Cost": "Cost"}
# "Pays for": the payment year each holding funds in the miniature (8g: the WInS book is Laura's whole plan in
# miniature). Two cells take two lines at 12 pt in the 0.79-in column ("\n" is a line break): IBTM's two jobs (TNA l.13,
# CANON A24) and VT's (IPS l.15; "flexibility" is the IPS's word for the half promised to no one, and Table 2's head).
PAYS_FOR_PRINT = {"2033 payment and floor stand-in": "2033 and\nthe floor",
                  "Growth: top of the range and the half kept": "Range top,\nflexibility",
                  "Cash": "", "Cost of buying": ""}


def pays_for(role):
    return PAYS_FOR_PRINT.get(role, role.replace(" payment", ""))

SUBTOTAL_LABEL = "Treasuries for the ten payments and the floor"   # card Q28 row 33: never "the payments" alone


def units_cell(i):
    """'4,503 / 4,503': units bought / target units (8m). VT's cell adds why they differ, on two more lines."""
    held, target = UNITS[i]
    s = f"{held:,} / {target:,}"
    if HOLDINGS[i][0] == "VT":
        s += "\n" + "\n".join(VT_UNITS_WORDS)
    return s


def table1_rows():
    """Table 1 as printed: list of (kind, cells). kind is 'row' (a holding), 'subtotal' (the ten Treasuries),
    'holdings' (all twelve holdings, cash included), 'costs' (money that left at purchase: not a holding) or 'total'.
    Cells are Wharton's five columns plus "Units bought / target" (after the asset type) and "Pays for". In the label
    rows (subtotal, holdings, costs) the first cell is the label, printed across the first LABEL_SPAN columns; the
    next LABEL_SPAN - 1 cells are empty. Amounts in cents as WInS records them; percentages to two decimals (8g's
    largest remainder)."""
    out = []
    pad = [""] * (LABEL_SPAN - 1)
    for i, (ident, name, typ, amt, pct, role) in enumerate(HOLDINGS):
        if i == COSTS_ROW:
            ha, hp = holdings_subtotal()
            out.append(("holdings", [HOLDINGS_LABEL] + pad + [cents_plain(ha), f"{hp:.2f}", ""]))
            out.append(("costs", [NAME_PRINT[name]] + pad + [cents_plain(amt), f"{pct:.2f}", ""]))
            continue
        out.append(("row", [ID_PRINT.get(ident, ident), NAME_PRINT.get(name, name), TYPE_PRINT[typ],
                            units_cell(i) if i < len(UNITS) else "", cents_plain(amt), f"{pct:.2f}", pays_for(role)]))
        if i == N_TREASURIES - 1:
            sa, sp = treasury_subtotal()
            out.append(("subtotal", [SUBTOTAL_LABEL] + pad + [cents_plain(sa), f"{sp:.2f}", ""]))
    out.append(("total", ["Total"] + pad + [cents_plain(HOLDINGS_TOTAL[0]), f"{HOLDINGS_TOTAL[1]:.2f}", ""]))
    return out


def treasury_subtotal():
    a = round(sum(h[3] for h in HOLDINGS[:N_TREASURIES]), 2)
    p = round(sum(h[4] for h in HOLDINGS[:N_TREASURIES]), 2)
    return a, p


def holdings_subtotal():
    """The twelve holdings (ten Treasuries, VT, cash): every 8g row but the costs row."""
    a = round(sum(h[3] for k, h in enumerate(HOLDINGS) if k != COSTS_ROW), 2)
    p = round(sum(h[4] for k, h in enumerate(HOLDINGS) if k != COSTS_ROW), 2)
    return a, p


TABLE1_HEADER = ["Ticker or identifier", "Name of investment", "Asset type", UNITS_HEAD, "Amount ($)",
                 "% of total",  # "portfolio" needs 0.58 in
                 "Pays for"]


# =================================================================================================================
# Figure 1, the operating reserve running down (3a). NUMBERS 8h, MODEL, read from results_reserve_2026-11-10.json.
# =================================================================================================================
# Waiting times in the Trading Notes' words (CANON A15, A16, B35): the figure labels a wait only where it is long
# enough to see. The model's months stay in FIGURE1_ROWS[...]["months_model"] (10.5 and 7.6).
WAIT_WORDS = {2038: "10.5 months", 2039: "7.5 months"}


def _short_holding(label):
    """'4.750% T-bond 15 Feb 2037' -> '4.750% Feb 2037'; 'IBTM payout, now cash ...' -> 'IBTM'."""
    m = re.match(r"([\d.]+%) T-bond \d+ (\w+ \d{4})", label)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    return label.split()[0]


def _figure1():
    own = [r for r in RESERVE["composition_1jan2033_base"] if r.get("role") == "own rung"]
    own.sort(key=lambda r: r["payment"])
    rows = []
    for c, b, f, z in zip(own, RESERVE["base"], RESERVE["fee"], RESERVE["zero"]):
        year = c["payment"]
        assert int(b["date"][:4]) == year == int(f["date"][:4]) == int(z["date"][:4])
        kind = "T-bond" if c["type"] == "Treasury bond" else "iBond ETF"   # IBTM's 2033 rung is an iBond ETF until
        cd = TOPUP_PAID["cash_dates"][str(year)]                            # it pays out in December 2032
        assert cd["ends"] == c["pays_out"]
        rows.append({
            "year": year,
            "holding": _short_holding(c["holding"]),
            "kind": kind,
            "ends": c["pays_out"],              # a fund's end date or a bond's maturity date (the model's date)
            "cash_first": cd["cash_first"],     # when the cash reaches Laura (Fri 13 Nov: the bars end at cash_last)
            "cash_last": cd["cash_last"],
            "months_cash": cd["months_to_payment_from_last"],
            "months_model": c["months_before_payment"],
            "wait_words": WAIT_WORDS.get(year),
            "at_forwards": b["own_holding_pays"],
            "own_if_nothing_earns": f["own_holding_pays"],          # Keel's standard: after the ETF's 0.15% fee
            "backstop_if_nothing_earns": f["backstop_and_carry_cover"],
            "own_if_nothing_earns_no_fee": z["own_holding_pays"],    # card Q28's column; the note's variant
            "backstop_if_nothing_earns_no_fee": z["backstop_and_carry_cover"],
        })
    return rows


FIGURE1_ROWS = _figure1()
FIGURE1_TOTALS = {
    "at_forwards": sum(r["at_forwards"] for r in FIGURE1_ROWS),
    "own_if_nothing_earns": sum(r["own_if_nothing_earns"] for r in FIGURE1_ROWS),
    "backstop_if_nothing_earns": sum(r["backstop_if_nothing_earns"] for r in FIGURE1_ROWS),
    "own_if_nothing_earns_no_fee": sum(r["own_if_nothing_earns_no_fee"] for r in FIGURE1_ROWS),
    "backstop_if_nothing_earns_no_fee": sum(r["backstop_if_nothing_earns_no_fee"] for r in FIGURE1_ROWS),
}
FIGURE1_NOTE_FACTS = {
    "left_after_2042_no_fee": RESERVE["zero_left_after_2042"],          # the $1,414 spare without the fee
    "left_after_2042_with_fee": RESERVE["fee_left_after_2042"],         # $0: the standard is met exactly
    "left_after_2042_at_forwards": RESERVE["base_left_after_2042"],     # $74,123 if rates follow the forwards
    "reserve_1jan2033": RESERVE["composition_1jan2033_total"],          # $444,545
    "own_rungs_1jan2033": RESERVE["own_rungs_value_1jan2033"],          # $399,089
    "funded_1jan2033": RESERVE["composition_1jan2033_total"] / RESERVE["own_rungs_value_1jan2033"],
    "etf_fee": 0.0015,
    "curve": "Treasury par yield curve, 6 Nov 2026",
    # Fri 13 Nov (bond reader, 12 Nov): the last column reconciled with the top-up's cost (NUMBERS 8h)
    "topup_for_no_interest_jan2028": TOPUP_PAID["for_no_interest_jan2028"],       # $35,894
    "topup_face_and_fund_dollars": TOPUP_PAID["face_and_fund_dollars"],           # $36,867
    "topup_interest_undiscounted": TOPUP_PAID["interest_undiscounted"],           # $19,143
    "topup_all_flows_undiscounted": TOPUP_PAID["all_flows_undiscounted"],         # $56,010
    "topup_fee_while_waiting": TOPUP_PAID["fee"]["fee_on_the_topups_own_waiting_money"],   # $90
    "topup_comes_back_1jan2033": TOPUP_PAID["comes_back_if_forwards_hold"]["value_1jan2033"],  # $45,456
}


def cash_words(r):
    """When a row's cash reaches Laura, as NUMBERS 8h's cash table and card Q2b (card 5) print it: 'Tue 17 Feb 2037' or
    'Mon 20 to Wed 22 Dec 2032'."""
    from datetime import date as _dt
    a, b = (_dt.fromisoformat(r[k]) for k in ("cash_first", "cash_last"))
    one = lambda d, month=True: f"{d.strftime('%a')} {d.day}" + (f" {d.strftime('%b')} {d.year}" if month else "")
    return one(a) if a == b else f"{one(a, False)} to {one(b)}"
# The note's ratio in WORDS.md's form (Thu 12 Nov): "about $1.11 for each $1 the payments need at today's rates, because
# the top-up is sized for no interest" ($444,545 against $399,089 on 1 Jan 2033, NUMBERS 8h).
FIGURE1_PER_DOLLAR = f"${FIGURE1_NOTE_FACTS['funded_1jan2033']:.2f}"
# Figure 1's heads (Thu 12 Nov, lay reader): the right-hand columns' head asks the question they answer, in WORDS.md's
# names; the first number column says "today's market rates", never "forward rates".
FIGURE1_HEADS = {
    "payment": "Payment",
    "timeline": "Held from January 2027 until its cash arrives",
    "c1": ("At today's", "market rates"),
    "question": ("If interest earns nothing,", "what pays each $50,000?"),
    "c2": ("Its own", "Treasury"),
    "c3": ("What the", "top-up pays"),  # Thu 12 Nov, lead: the column holds what its Treasuries pay ($55,920), not its cost ($38,282)
}
FIGURE1_LEGEND = ("iBond Treasury fund", "Treasury bond", "$50,000 paid on 1 January", "cash waiting")


# =================================================================================================================
# Table 2, the plan under several markets (3b, 3c). NUMBERS 8i (and 8j for the spread of the flexibility), MODEL.
# =================================================================================================================
# Row order (card Q28): the base first; the stresses by how far the stated range falls; the rates-up world last.
WORLDS = [
    # (key, plain name printed in the table, where the data sit in the JSON)
    ("forwards", "Today's forward rates", ("scenarios", "forwards")),
    ("2006-06", "Replay from 2006: shares fall", ("named", "2006-06")),
    ("minus3", "Rates 3 points lower for good", ("scenarios", "minus3")),
    ("2007-07", "Replay from 2007: rates fall early", ("named", "2007-07")),
    ("inflation", "Inflation: rates 3 points higher", ("scenarios", "inflation")),
]


def _world(src):
    block, key = src
    w = JOINT["scenarios"][key] if block == "scenarios" else JOINT["joint"]["named"][key]
    paid_in_full = (w["shortfall"] if block == "scenarios" else w["payments_shortfall"]) == 0
    contribution = w["gift_realised"] if block == "scenarios" else w["gift_capped"]
    funds_pay = w["funds_pay"] if block == "scenarios" else w["gift_realised"]
    return {"payments": "All paid" if paid_in_full else "SHORT", "bottom": w["bottom_stated"],
            "top": w["top_stated"], "contribution": contribution, "funds_pay": funds_pay,
            "excess": w["excess_to_kept_half"], "half_kept": w["kept_half_jan2033"],
            "flexibility": w["kept_plus_excess_jan2033"], "bottom_raw": w["bottom_raw"], "top_raw": w["top_raw"]}


TABLE2_WORLDS = [(key, name, _world(src)) for key, name, src in WORLDS]

_J = JOINT["joint"]
_JR = JOINT["twd_test"]["joint_replay"]
assert _J["share_with_payment_shortfall"] == 0.0 and _J["windows"] == 585
assert _JR["share_contribution_equals_stated_top"] == 1.0   # so the contribution's spread is the stated top's
TABLE2_SPREAD_LABEL = f"All {_J['windows']} history replays (1962-2010 starts)"
TABLE2_SPREAD = [
    (label, {"payments": "All paid", "bottom": _J["bottom_stated_p5_p50_p95"][i], "top": _J["top_stated_p5_p50_p95"][i],
             "contribution": _JR["contribution_p5_p50_p95"][i],
             "flexibility": _JR["kept_half_plus_excess"]["pot_p5_p50_p95"][i]})
    for i, label in enumerate(["1-in-20 low", "Median", "1-in-20 high"])
]
# The contribution is not a column: it equals the stated top in every world and every window (8i, 8j; checked below).
# It is the confidence answer, so it is a row of the table, the last one (fresh reader and coordinator, Wed 11 Nov),
# not a clause of the note.
TABLE2_HEADER = ["World", "Ten payments", "Stated bottom (2031)", "Stated top (2031)", "Flexibility (Jan 2033)"]
# As printed: an APA column spanner groups the two stated ends (the range Laura announces), which also keeps the
# heads to two lines.
TABLE2_SPANNER = "Stated in 2031"
TABLE2_HEAD_ROW = ["World", "Ten payments", "Bottom", "Top", "Flexibility\n(Jan 2033)"]  # break after the word
TABLE2_RESULT_ROW = "In every world and every replay, the facility contribution in January 2033 equals the stated top."


def table2_cells(v):
    """One printed row: stated ends to the dollar (they are $5,000 steps by the rule); the
    flexibility to the nearest $100, as SKELETON's prose rounds it (about $29,800), so no model value prints as a round
    $5,000 step or as $50,000, the payment's size."""
    return [v["payments"], dollars(v["bottom"]), dollars(v["top"]), hundreds(v["flexibility"])]


# Compatibility for ../template/build_template.py (not Keel's exhibits file; it reads these two names and draws a
# five-column Table 2). Same data, the stated range in one column.
SCENARIO_COLUMNS = ["World", "Ten payments", "Stated bottom (2031)", "Stated top (2031)", "Flexibility (Jan 2033)"]
SCENARIO_ROWS = [tuple([name] + table2_cells(v)) for _, name, v in TABLE2_WORLDS]


# =================================================================================================================
# Table 3, monitoring (3e). SKELETON Exhibits item 4 (spec of Thu 12 Nov), card Q30 "Table 3 cut", the bond reader of
# Wed 11 Nov (research/panel/2026-11-11_bond_desk_table3.md). Seven rows in three levels, five columns, one trigger
# per "look closer or act when" cell; the two reasons defined in their rows; custody is not a row (one line of 3e prose).
# =================================================================================================================
from datetime import date as _date  # noqa: E402

_C6 = MAIN["C6"]
DEPOSIT_2028 = 150000.0
TOPUP = _C6["fall_0bp"]["with_standard"]                 # $38,282: the top-up, January 2028 prices (NUMBERS 2, 5)
TOPUP_TEN_LACK = _C6["fall_0bp"]["ladder_only"]          # $2,388: what the ten Treasuries still lack
TOPUP_NO_INTEREST = TOPUP - TOPUP_TEN_LACK               # $35,894: met even if money received earns nothing (NUMBERS 2)
BOTTOM_AFTER_2PT_FALL = _C6["fall_200bp"]["150000"]["stated_bottom"]   # $60,000 (NUMBERS 5)
FALL_TAKES_WHOLE_DEPOSIT = 3.60   # points; NUMBERS 5 text only (no results file holds it), checked against the text
TWD_PER_USD = INPUTS["usdtwd"]["latest"]                                # 32.768 on 6 Nov (NUMBERS 8d)
CCI_BAND = (INPUTS["taiwan_construction"]["low"], INPUTS["taiwan_construction"]["high"])   # 1.5% to 5.0% (8d)
TWD_TEST = 0.10                                          # a 10% stronger Taiwan dollar (NUMBERS 8j)
_TWDF = JOINT["scenarios"]["forwards"]
CONTRIBUTION_FWD = _TWDF["gift_realised"]                # $115,000 at today's forwards (8i, 8j)
TWD_NEED = TWD_TEST * CONTRIBUTION_FWD                   # $11,500 more in December 2032 (8j central case)
FLEX_FWD = _TWDF["kept_plus_excess_jan2033"]             # $29,823; printed to the nearest $100, as Table 2 prints it
TRADE_DAYS = (_date(2027, 1, 4), _date(2028, 1, 3))      # 1 Jan 2027 is a market holiday, 1 Jan 2028 a Saturday
FEB37_PAYS = _date(2037, 2, 17)                          # 15 Feb 2037 is a Sunday, 16 Feb Presidents' Day (8h)
MISSED_BY = _date(2028, 3, 31)                           # a missed deposit: nothing received by this date
CONFIRM_BY = _date(2027, 12, 1)                          # the early warning: Laura confirms the deposit in writing
MISSED_SHORT_2033 = MAIN["C6"]["missed"]["short_at_forwards"]   # $3,016: the 2033 payment short at today's rates (NUMBERS 5)
IBOND_SLACK = "4 to 9"                                   # business days, cash in hand to the year's last business day (card Q2b)
IBOND_SLACK_2036 = "4 to 6"                              # the tightest year, 15 Dec 2035 a Saturday (card Q2b)
DEFAULT_DAYS = 5                                         # a Treasury default: not paid within five business days


def _d(d, weekday=True):
    """'Mon 4 Jan 2027' (weekday=True) or '31 March 2028'."""
    return f"{d.strftime('%a')} {d.day} {d.strftime('%b')} {d.year}" if weekday else f"{d.day} {d.strftime('%B')} {d.year}"


_NUM = {5: "five"}
# Cells. Words are WORDS.md's: "the top-up", "her flexibility", "facility contribution", "simulated futures", "the
# floor", "the world share fund (VT)", "her team" (Wharton: "Laura or her asset management team"). The last column is
# a list of runs: (text, italic); "\n" breaks the line inside the cell.
TABLE3_HEADER = ["Signal", "Reader", "Carry on while", "Look closer or act when",
                 "What it changes; what it never changes"]
TABLE3_LEVELS = {
    "reason": "The two reasons to change the plan",
    "closer": "Look closer: a date or an instrument may change, never the plan",
    "watch": "Watch: the plan carries on",
}


def _changes(changes, never):
    """The last column: two labelled parts in one run of text (a line break between them costs a line a row)."""
    return [("Changes: ", True), (changes + ". ", False), ("Never: ", True), (never + ".", False)]


TABLE3_ROWS = [
    ("reason", [
        f"The 2028 deposit ({dollars(DEPOSIT_2028)})",
        "Laura",
        f"Confirmed by {CONFIRM_BY.day} {CONFIRM_BY.strftime('%b')} {CONFIRM_BY.year}; the {dollars(TOPUP)} top-up first",
        f"Nothing received by {_d(MISSED_BY, weekday=False)} (a missed deposit)",
        _changes(f"no range; the 2033 payment {dollars(MISSED_SHORT_2033)} short", "a sale")]),
    ("reason", [
        "Treasury payments",
        "Team",
        "Paid on the due date, moved past holidays",
        f"A Treasury default: a payment over {_NUM[DEFAULT_DAYS]} business days late",
        _changes("what the Treasuries pay, restated", "a forced sale")]),
    ("closer", [
        "The debt limit's X-date",
        "Team",
        "No X-date within a month of a cash date",
        "An X-date within a month of a payout, maturity or trade day",
        _changes("nothing before it (a late payment is row 2)", "a sale ahead of it")]),
    ("closer", [
        "iBond fund notices, the floor's too",
        "Team",
        f"Cash in {IBOND_SLACK} business days before the year's last ({IBOND_SLACK_2036} for 2036)",
        "A notice that moves a fund's end date past a payment",
        _changes("the fund, for a Treasury due in time, paid from the reserve", "the amount; the shares")]),
    ("closer", [
        f"Trade days: {_d(TRADE_DAYS[0])}, {_d(TRADE_DAYS[1])}",
        "Team",
        "Limit orders near each fund's net asset value",
        "A date cannot be kept (a halt; a first draw after January 2033)",
        _changes("a date, by days", "the step or its order")]),
    ("watch", [
        "Treasury yields and share prices",
        "Team",
        "Any level: a fall in the market is not a reason",
        f"None. 2 points lower before 2027: a {dollars(BOTTOM_AFTER_2PT_FALL)} bottom; "
        f"{FALL_TAKES_WHOLE_DEPOSIT:.2f} lower: the top-up takes the whole deposit",
        _changes("prices until each end is bought, then her flexibility",
                 f"the payments, to a {FALL_TAKES_WHOLE_DEPOSIT:.2f} fall")]),
    ("watch", [
        "Her flexibility's three uses",
        "Laura",
        f"US$1 = NT${TWD_PER_USD:.3f}; construction cost index up {100 * CCI_BAND[0]:.1f}% to "
        f"{100 * CCI_BAND[1]:.1f}% a year",
        f"A Taiwan dollar {100 * TWD_TEST:.0f}% stronger ({dollars(TWD_NEED)} more on {dollars(CONTRIBUTION_FWD)})",
        _changes(f"a call on her flexibility ({hundreds(FLEX_FWD)} today)", "the range")]),
]


def cell_text(v):
    """A cell as plain text (runs joined; a line break becomes a space)."""
    if isinstance(v, (list, tuple)):
        return "".join(t for t, _ in v).replace("\n", " ")
    return str(v).replace("\n", " ")


def table3_rows():
    """Table 3 as printed: list of (kind, cells); a level is a 'spanner' row (one italic cell across the table)."""
    out, level = [], None
    for lev, cells in TABLE3_ROWS:
        if lev != level:
            out.append(("spanner", [TABLE3_LEVELS[lev]]))
            level = lev
        out.append(("row", cells))
    return out


# =================================================================================================================
# The check against NUMBERS.md
# =================================================================================================================
def _section(md, start, stop_prefix):
    i = md.index(start)
    j = md.find(stop_prefix, i + len(start))
    return md[i:j if j > 0 else len(md)]


def _table_rows(text, header_start):
    """Rows (lists of cells) of the first Markdown table whose header line starts with header_start."""
    lines = text.splitlines()
    for k, ln in enumerate(lines):
        if ln.strip().startswith(header_start):
            rows = []
            for ln2 in lines[k + 2:]:
                s = ln2.strip()
                if not s.startswith("|"):
                    break
                rows.append([c.strip() for c in s.strip("|").split("|")])
            return rows
    raise KeyError(header_start)


def _money(s):
    return [float(x.replace(",", "")) for x in re.findall(r"\$([\d,]+(?:\.\d+)?)", s)]


def check(verbose=True):
    """Compare every exhibit figure with NUMBERS.md. Returns (fails, results); results rows are
    (exhibit, figure, exhibit value, register value, section, status)."""
    with open(NUMBERS_MD) as fh:
        md = fh.read()
    res = []

    def cmp(ex, what, mine, reg, sec, tol=0.5):
        ok = reg is not None and abs(mine - reg) <= tol
        res.append((ex, what, mine, reg, sec, "PASS" if ok else "FAIL"))

    def note(ex, what, mine, reg, sec, status):
        res.append((ex, what, mine, reg, sec, status))

    # ---- Table 1 against 8g ----
    s8g = _section(md, "### 8g.", "\n### 8h.")
    rows = _table_rows(s8g, "| Ticker or identifier")
    body = [r for r in rows if not r[0].startswith("**Total")]
    total = [r for r in rows if r[0].startswith("**Total")][0]
    for h, r in zip(HOLDINGS, body):
        ident, name, typ, amt, pct, _ = h
        ok_text = (r[0] == ident and r[1] == name and r[2] == typ)
        note("Table 1", f"{name}: identifier, name, type", f"{ident} | {name} | {typ}", " | ".join(r[:3]), "8g",
             "PASS" if ok_text else "FAIL")
        cmp("Table 1", f"{name}: amount", amt, _money(r[3])[0], "8g", tol=0.005)
        cmp("Table 1", f"{name}: %", pct, float(r[4].rstrip("%")), "8g", tol=0.0001)
        if name in NAME_PRINT:
            lab = NAME_PRINT[name].lower()
            note("Table 1", f"{name}: printed as", NAME_PRINT[name], name,
                 "8g (Thu 12 Nov label: costs, not a holding; panel 2)",
                 "PASS" if amt == 1309.42 and pct == 0.44 and lab.startswith("costs") and "not a holding" in lab
                 and "fees" in lab and "accrued interest" in lab else "FAIL")
        if ident in ID_PRINT:
            note("Table 1", f"{name}: identifier", ID_PRINT[ident], ident, "8g", "PLACEHOLDER (Caplet's final WInS export)")
    note("Table 1", "row count", len(HOLDINGS), len(body), "8g", "PASS" if len(HOLDINGS) == len(body) else "FAIL")
    cmp("Table 1", "Total amount", HOLDINGS_TOTAL[0], _money(total[3])[0], "8g", tol=0.005)
    cmp("Table 1", "Total %", HOLDINGS_TOTAL[1], float(total[4].strip("*%")), "8g", tol=0.0001)
    cmp("Table 1", "Sum of the rows = $300,000.00", round(sum(h[3] for h in HOLDINGS), 2), 300000.00, "8g", tol=0.005)
    cmp("Table 1", "Sum of the % = 100.00", round(sum(h[4] for h in HOLDINGS), 2), 100.00, "8g", tol=0.0001)
    m = re.search(r"Treasuries ([\d.]+)% \(\$([\d,.]+)", s8g)
    sa, sp = treasury_subtotal()
    cmp("Table 1", "Subtotal, ten Treasuries: amount", sa, float(m.group(2).replace(",", "")), "8g In groups", tol=0.005)
    cmp("Table 1", "Subtotal, ten Treasuries: %", sp, float(m.group(1)), "8g In groups", tol=0.0001)
    m = re.search(r"\$([\d,]+) of commissions.*?\$([\d,.]+) that WInS charged", s8g, re.S)
    cmp("Table 1", "Costs row: commissions", HOLDINGS_NOTE_FACTS["commissions"], float(m.group(1).replace(",", "")), "8g v2")
    cmp("Table 1", "Costs row: bond interest at purchase", HOLDINGS_NOTE_FACTS["accrued_interest"],
        float(m.group(2).replace(",", "")), "8g v2", tol=0.005)
    cmp("Table 1", "Costs row = commissions + interest", HOLDINGS_NOTE_FACTS["commissions"] +
        HOLDINGS_NOTE_FACTS["accrued_interest"], HOLDINGS[12][3], "8g v2", tol=0.005)
    m = re.search(r"cash row now equals the cash WInS shows \(\$([\d,.]+)\)", s8g)
    cmp("Table 1", "Cash row = WInS cash", HOLDINGS[11][3], float(m.group(1).replace(",", "")), "8g v2", tol=0.005)
    note("Table 1", "8g cites the snapshot's Pays for column and 'plan in miniature'", "yes",
         "yes" if ('"Pays for" column' in s8g and "whole plan in miniature" in s8g) else "no", "8g",
         "PASS" if ('"Pays for" column' in s8g and "whole plan in miniature" in s8g) else "FAIL")
    with open(SNAPSHOT_MD) as fh:
        snap = _table_rows(fh.read(), "| Symbol | Qty")
    snap = [r for r in snap if not r[0].startswith("**Total")]
    for h, r in zip(HOLDINGS[:N_TREASURIES + 1], snap):
        printed = pays_for(h[5]).replace("\n", " ")
        want = r[6]
        if want.startswith("20"):                      # a payment year (IBTM: "2033 payment + floor stand-in")
            ok = printed.split()[0] == want.split()[0] and (("floor" in want) == ("floor" in printed))
            note("Table 1", f"{h[0] if h[0] != '(WInS id)' else h[1]}: Pays for", printed, want, "23 Oct snapshot",
                 "PASS" if ok else "FAIL")
        else:                                          # VT: "growth sleeve"; its two jobs are IPS l.15's
            note("Table 1", f"{h[0]}: Pays for", printed, f"{want} (IPS l.15: the top; half promised to no one)",
                 "23 Oct snapshot, IPS l.15", "PASS" if h[0] == "VT" and want == "growth sleeve" else "FAIL")
    note("Table 1", "Pays for: snapshot rows in holding order", len(snap), N_TREASURIES + 1, "23 Oct snapshot",
         "PASS" if len(snap) == N_TREASURIES + 1 and snap[0][0].startswith("IBTM") and snap[-1][0].startswith("VT")
         else "FAIL")

    # ---- Table 1, Thu 12 Nov evening: the costs row set apart, and units bought against target (8m) ----
    # The holdings subtotal: the twelve holdings = $300,000 less the costs row = 8g's "cost of the eleven holdings"
    # plus the cash WInS shows; its % = 100 less the costs row's 0.44.
    ha, hp = holdings_subtotal()
    m = re.search(r"\$300,000\s+less\s+the\s+cost\s+of\s+the\s+eleven\s+holdings\s+\(\$([\d,.]+)\)", s8g)
    eleven = float(m.group(1).replace(",", "")) if m else None
    cmp("Table 1", "All holdings = the eleven at cost + WInS cash", ha,
        None if eleven is None else round(eleven + HOLDINGS_NOTE_FACTS["wins_cash"], 2), "8g v2 (Keel's call)", tol=0.005)
    cmp("Table 1", "All holdings = $300,000 less the costs row", ha,
        round(HOLDINGS_TOTAL[0] - HOLDINGS[COSTS_ROW][3], 2), "8g", tol=0.005)
    cmp("Table 1", "All holdings % = 100 less the costs row's %", hp,
        round(HOLDINGS_TOTAL[1] - HOLDINGS[COSTS_ROW][4], 2), "8g", tol=0.0001)
    m = re.search(r"Treasuries ([\d.]+)% .*?VT ([\d.]+)%, cash ([\d.]+)%, costs at purchase ([\d.]+)%", s8g)
    cmp("Table 1", "All holdings % = 8g's groups (Treasuries + VT + cash)", hp,
        round(float(m.group(1)) + float(m.group(2)) + float(m.group(3)), 2) if m else None, "8g In groups", tol=0.0001)
    kinds = [k for k, _ in table1_rows()]
    order_ok = kinds[-3:] == ["holdings", "costs", "total"] and kinds.count("costs") == 1 and \
        kinds.index("subtotal") == N_TREASURIES and kinds.count("row") == len(HOLDINGS) - 1
    note("Table 1", "Costs row below the holdings subtotal, above the total; no ticker, type or units",
         " > ".join(kinds[-3:]), "holdings > costs > total", "panel 2 (faculty, finalist judges)",
         "PASS" if order_ok and all(c == "" for c in table1_rows()[-2][1][1:LABEL_SPAN]) else "FAIL")
    # Units against 8m's targets (the criterion row names each target; the result says all ten were met exactly)
    s8m = _section(md, "### 8m.", "\n### 8n.")
    m = re.search(r"IBTM ([\d,]+); IBTO ([\d,]+); IBTP ([\d,]+); IBTQ ([\d,]+); IBTR ([\d,]+); bonds ([\d, ]+) lots of "
                  r"\$1,000", s8m)
    targets_8m = [int(x.replace(",", "")) for x in m.groups()[:5]] + [int(x) for x in m.group(6).split(",")] if m else []
    ten_exact = "All ten held at exactly the target units" in s8m
    m = re.search(r"(\d+) shares against (\d+) at 2 Oct prices", s8m)
    vt_8m = (int(m.group(1)), int(m.group(2))) if m else None
    note("Table 1", "Units: 8m says all ten Treasuries were bought at exactly their targets", "yes",
         "yes" if ten_exact else "no", "8m", "PASS" if ten_exact else "FAIL")
    for i in range(N_TREASURIES):
        h, (held, target) = HOLDINGS[i], UNITS[i]
        who = h[0] if h[0] not in ID_PRINT else h[1]
        cmp("Table 1", f"{who}: target units", target, targets_8m[i] if i < len(targets_8m) else None, "8m")
        cmp("Table 1", f"{who}: units bought = target", held, target if ten_exact else None, "8m")
    cmp("Table 1", "VT: units bought", UNITS[N_TREASURIES][0], vt_8m[0] if vt_8m else None, "8m")
    cmp("Table 1", "VT: target units (2 Oct prices)", UNITS[N_TREASURIES][1], vt_8m[1] if vt_8m else None, "8m")
    ok = ("filled last" in s8m and 'from the cash then left' in s8m and VT_UNITS_WORDS[0].startswith("bought last")
          and "cash left" in VT_UNITS_WORDS[1])
    note("Table 1", "VT's cell: bought last, from cash left", " ".join(VT_UNITS_WORDS),
         "8m: sized \"from the cash then left\", bought last (filled last)", "8m", "PASS" if ok else "FAIL")
    # The same units in the 23 Oct WInS snapshot (quantities held) and units x price paid = 8g's amount at cost
    for h, (held, _), r in zip(HOLDINGS[:N_TREASURIES + 1], UNITS, snap):
        who = h[0] if h[0] not in ID_PRINT else h[1]
        cmp("Table 1", f"{who}: units held (WInS snapshot)", held, float(r[1].replace(",", "")), "23 Oct snapshot")
        cmp("Table 1", f"{who}: units x price paid = 8g amount", round(held * float(r[3].replace(",", "")), 2), h[3],
            "23 Oct snapshot, 8g", tol=0.005)
    # The targets as the Portfolio tab set them before the first fill (8m's source; WInS units, bonds in $1,000 lots)
    import csv
    with open(PORTFOLIO_CSV, newline="") as fh:
        grid = list(csv.reader(fh))
    head = next(r for r in grid if "Holding" in r and "Target units" in r)
    c_hold, c_win, c_ord = head.index("Holding"), [c for c, v in enumerate(head) if v.startswith("Type into WInS")][0], \
        head.index("Order tonight")
    tab = [r for r in grid[grid.index(head) + 1:] if len(r) > c_ord and r[c_win].strip()]
    note("Table 1", "Portfolio tab: eleven target rows in holding order", len(tab), N_TREASURIES + 1,
         "portfolio.csv l.20-31 (8m)", "PASS" if len(tab) == N_TREASURIES + 1 and tab[0][c_hold] == "IBTM"
         and tab[-1][c_hold] == "VT" else "FAIL")
    for h, (_, target), r in zip(HOLDINGS[:N_TREASURIES + 1], UNITS, tab):
        who = h[0] if h[0] not in ID_PRINT else h[1]
        cmp("Table 1", f"{who}: target units (Portfolio tab, set 2 Oct)", target, float(r[c_win].replace(",", "")),
            "portfolio.csv (8m)")
    orders = [int(r[c_ord]) for r in tab]
    note("Table 1", "VT bought last (order 11 of 11 on the Portfolio tab)", orders[-1], max(orders),
         "portfolio.csv (8m)", "PASS" if orders[-1] == max(orders) == N_TREASURIES + 1 else "FAIL")

    # ---- Figure 1 against 8h ----
    s8h = _section(md, "### 8h.", "\n### 8i.")
    four = _table_rows(s8h, "| Payment | Forwards: own holding pays")
    by_year = {int(r[0]): r for r in four if r[0].isdigit()}
    for f in FIGURE1_ROWS:
        r = by_year[f["year"]]
        fw, mi, ze, fe = _money(r[1]), _money(r[2]), _money(r[3]), _money(r[4])
        cmp("Figure 1", f"{f['year']} at forward rates, own holding pays", round(f["at_forwards"]), fw[0], "8h")
        cmp("Figure 1", f"{f['year']} at forward rates, backstop covers", 0, fw[2], "8h")
        cmp("Figure 1", f"{f['year']} nothing earns, after fee: own holding", round(f["own_if_nothing_earns"]), fe[0], "8h")
        cmp("Figure 1", f"{f['year']} nothing earns, after fee: backstop", round(f["backstop_if_nothing_earns"]), fe[1], "8h")
        cmp("Figure 1", f"{f['year']} own + backstop = $50,000", round(f["own_if_nothing_earns"]) +
            round(f["backstop_if_nothing_earns"]), 50000, "8h")
        cmp("Figure 1", f"{f['year']} nothing earns, no fee: own holding", round(f["own_if_nothing_earns_no_fee"]), ze[0], "8h")
        cmp("Figure 1", f"{f['year']} nothing earns, no fee: backstop", round(f["backstop_if_nothing_earns_no_fee"]), ze[1], "8h")
    tot = [r for r in four if r[0].startswith("All ten")][0]
    T = FIGURE1_TOTALS
    cmp("Figure 1", "Total at forward rates", round(T["at_forwards"]), _money(tot[1])[0], "8h")
    cmp("Figure 1", "Total own holdings, after fee", round(T["own_if_nothing_earns"]), _money(tot[4])[0], "8h")
    cmp("Figure 1", "Total backstop, after fee", round(T["backstop_if_nothing_earns"]), _money(tot[4])[1], "8h")
    cmp("Figure 1", "Total own holdings, no fee", round(T["own_if_nothing_earns_no_fee"]), _money(tot[3])[0], "8h")
    cmp("Figure 1", "Total backstop, no fee", round(T["backstop_if_nothing_earns_no_fee"]), _money(tot[3])[1], "8h")
    foot_own = sum(round(f["own_if_nothing_earns"]) for f in FIGURE1_ROWS)
    foot_bk = sum(round(f["backstop_if_nothing_earns"]) for f in FIGURE1_ROWS)
    note("Figure 1", "Printed rows foot to (own / top-up)", f"{dollars(foot_own)} / {dollars(foot_bk)}",
         f"{dollars(round(T['own_if_nothing_earns']))} / {dollars(round(T['backstop_if_nothing_earns']))}",
         "8h (totals of unrounded figures)", "PASS" if foot_own == round(T["own_if_nothing_earns"]) else
         "ROUNDING: rows equal 8h and foot $1 off its totals of unrounded figures (the note carries the rounding clause)")
    left = [r for r in four if r[0].startswith("Left after the last payment")][0]
    cmp("Figure 1", "Left after 2042, nothing earns, no fee", round(FIGURE1_NOTE_FACTS["left_after_2042_no_fee"]),
        _money(left[3])[0], "8h")
    cmp("Figure 1", "Left after 2042, nothing earns, after fee", round(FIGURE1_NOTE_FACTS["left_after_2042_with_fee"]),
        _money(left[4])[0], "8h")
    cmp("Figure 1", "Left after 2042 at forwards", round(FIGURE1_NOTE_FACTS["left_after_2042_at_forwards"]),
        _money(left[1])[0], "8h")
    s2 = _section(md, "## 2. Reinvestment", "\n## 3.")
    m = re.search(r"\| Cost \(1 Jan 2027 value\) \|.*?\*\*\$([\d,]+)\*\*", s2)
    cmp("Figure 1", "Treasuries bought with the 2028 deposit: cost in 1 Jan 2027 money (note item)",
        round(RESERVE["margin_jan2027"]), float(m.group(1).replace(",", "")), "section 2 table")
    note("Figure 1", "'The top-up' (head): extra Treasuries bought with the 2028 deposit",
         "In January 2028 the deposit's first dollars also buy extra face",
         "found" if "In January 2028 the deposit's first dollars also buy extra face" in s2 else "not found", "section 2",
         "PASS" if "In January 2028 the deposit's first dollars also buy extra face" in s2 else "FAIL")
    with open(WORDS_MD) as fh:
        words = fh.read()
    ok = "| the top-up |" in words and "more Treasuries bought with the first part of the 2028 deposit" in words
    note("Figure 1", "'The top-up' is WORDS.md's name for that money", "the top-up", "found" if ok else "not found",
         "WORDS.md", "PASS" if ok else "FAIL")
    cmp("Figure 1", "Note: the ratio, dollars held for each $1 the payments need", float(FIGURE1_PER_DOLLAR[1:]),
        round(float(re.search(r"Funded ratio: \$[\d,]+ against \$[\d,]+, ([\d.]+)% funded", s8h).group(1)) / 100, 2),
        "8h", tol=0.0001)
    note("Figure 1", "Note: the ratio as WORDS.md words it", f"about {FIGURE1_PER_DOLLAR} for each $1",
         "found" if f"about {FIGURE1_PER_DOLLAR} for each $1" in words else "not found", "WORDS.md",
         "PASS" if f"about {FIGURE1_PER_DOLLAR} for each $1" in words else "FAIL")
    banned = ("backstop", "gift", "overflow", "paths", "forward rates")
    printed_f1 = " ".join([FIGURE1_HEADS["payment"], FIGURE1_HEADS["timeline"]] + list(FIGURE1_HEADS["c1"]) +
                          list(FIGURE1_HEADS["question"]) + list(FIGURE1_HEADS["c2"]) + list(FIGURE1_HEADS["c3"]) +
                          list(FIGURE1_LEGEND)).lower()
    note("Figure 1", "No word WORDS.md bans in the figure's text", ", ".join(b for b in banned if b in printed_f1) or "none",
         "none", "WORDS.md", "PASS" if not any(b in printed_f1 for b in banned) else "FAIL")
    m = re.search(r"Funded ratio: \$([\d,]+) against \$([\d,]+), ([\d.]+)% funded", s8h)
    cmp("Figure 1", "Reserve on 1 Jan 2033", round(FIGURE1_NOTE_FACTS["reserve_1jan2033"]), float(m.group(1).replace(",", "")), "8h")
    cmp("Figure 1", "Own rungs on 1 Jan 2033", round(FIGURE1_NOTE_FACTS["own_rungs_1jan2033"]), float(m.group(2).replace(",", "")), "8h")
    cmp("Figure 1", "Funded on 1 Jan 2033 (%)", round(100 * FIGURE1_NOTE_FACTS["funded_1jan2033"], 1), float(m.group(3)), "8h", tol=0.05)
    m = re.search(r"the Feb-2037 bond ([\d.]+) months; the May-2038 bond ([\d.]+) months; the three November bonds ([\d.]+) months", s8h)
    model_months = {f["year"]: f["months_model"] for f in FIGURE1_ROWS}
    cmp("Figure 1", "Feb-2037 bond wait, model months", model_months[2038], float(m.group(1)), "8h", tol=0.01)
    cmp("Figure 1", "May-2038 bond wait, model months", model_months[2039], float(m.group(2)), "8h", tol=0.01)
    cmp("Figure 1", "November bonds' wait, model months", model_months[2040], float(m.group(3)), "8h", tol=0.01)
    holdings_8h = {int(r[0]): r[1] for r in _table_rows(s8h, "| Payment | Holding | Own rung") if r[0].isdigit()}
    for f in FIGURE1_ROWS:
        ok = f["holding"].split()[0] in holdings_8h[f["year"]] or f["holding"].replace(" ", "") in holdings_8h[f["year"]].replace(" ", "")
        note("Figure 1", f"{f['year']} paid from", f["holding"], holdings_8h[f["year"]], "8h composition",
             "PASS" if ok else "FAIL")
    with open(TNA_TXT) as fh, open(WN_TXT) as fh2:
        tna = fh.read() + fh2.read()
    for year, words in WAIT_WORDS.items():
        n = words.split()[0]
        ok = (f"{n}-month" in tna) or (f"{n} months" in tna)
        note("Figure 1", f"{year} wait label '{words}'", words, f"TNA and WInS trade notes ({'found' if ok else 'not found'})",
             "CANON A15, A16, B35", "PASS" if ok else "FAIL")

    # ---- Figure 1, Fri 13 Nov: cash dates (8h's cash table, card Q2b card 5) and the top-up's column reconciled ----
    from datetime import date as _dt
    cash_8h = {int(r[0]): r for r in _table_rows(s8h, "| Payment | Paid from | Ends or matures | Cash reaches Laura")
               if r[0].isdigit()}
    with open(os.path.join(FR, "research", "cards", "Q2b_escrows_lotteries_settlements_stress.md")) as fh:
        q2b_text = re.sub(r"\s+", " ", fh.read())
    for f in FIGURE1_ROWS:
        w = cash_words(f)
        r = cash_8h.get(f["year"])
        note("Figure 1", f"{f['year']} cash reaches Laura", w, r[3] if r else None, "8h cash table",
             "PASS" if r and r[3] == w else "FAIL")
        note("Figure 1", f"{f['year']} cash date as card Q2b gives it", w, "found" if f"| {w} |" in q2b_text else
             "not found", "card Q2b, card 5", "PASS" if f"| {w} |" in q2b_text else "FAIL")
        e, a, b = (_dt.fromisoformat(f[k]) for k in ("ends", "cash_first", "cash_last"))
        y1 = _dt(f["year"], 1, 1)
        ok = e <= a <= b < y1 and a.weekday() < 5 and b.weekday() < 5
        days = f"{(y1 - b).days}" if a == b else f"{(y1 - b).days} to {(y1 - a).days}"
        note("Figure 1", f"{f['year']} cash on a business day, after the end date, before 1 January",
             f"{f['ends']} -> {f['cash_first']}..{f['cash_last']}", "calendar", "calendar", "PASS" if ok else "FAIL")
        note("Figure 1", f"{f['year']} days from cash to 1 January", days, r[4].split(" (")[0] if r else None,
             "8h cash table", "PASS" if r and r[4].split(" (")[0] == days else "FAIL")
    for f in FIGURE1_ROWS:
        if f["wait_words"]:
            n = float(f["wait_words"].split()[0])
            note("Figure 1", f"{f['year']} wait label within 0.1 month of the cash wait", f["wait_words"],
                 f"{f['months_cash']:.2f} months from the cash", "8h cash table",
                 "PASS" if abs(n - f["months_cash"]) <= 0.1 else "FAIL")
    s8h1 = re.sub(r"\s+", " ", s8h)
    F = FIGURE1_NOTE_FACTS
    for what, mine, pat in (
            ("top-up's part for no interest, January 2028", F["topup_for_no_interest_jan2028"],
             r"part for no interest costs \$([\d,]+) in January 2028"),
            ("what it buys, face and fund dollars", F["topup_face_and_fund_dollars"],
             r"What it buys:\*\* \$([\d,]+) of face and fund dollars"),
            ("its own interest, undiscounted", F["topup_interest_undiscounted"],
             r"back plus \$([\d,]+) of its own interest"),
            ("face plus interest, undiscounted", F["topup_all_flows_undiscounted"],
             r"without discounting: \$([\d,]+)"),
            ("the ETF's fee while it waits", F["topup_fee_while_waiting"], r"fee takes \$([\d,]+) of that"),
            ("reaches the payments (the column's total)", T["backstop_if_nothing_earns"],
             r"\*\*\$([\d,]+)\*\* reaches the payments"),
            ("what comes back, 1 Jan 2033 money", F["topup_comes_back_1jan2033"],
             r"\*\*\$([\d,]+)\*\* in 1 Jan 2033 money \(this part of the top-up plus")):
        m = re.search(pat, s8h1)
        cmp("Figure 1", f"Note: {what}", round(mine), float(m.group(1).replace(",", "")) if m else None, "8h reconciled")
    cmp("Figure 1", "Note: $35,894 is Table 3's part for no interest", round(F["topup_for_no_interest_jan2028"]),
        round(TOPUP_NO_INTEREST), "2, 5")
    cmp("Figure 1", "Note: face + interest - fee = the column's total", round(F["topup_all_flows_undiscounted"] -
        F["topup_fee_while_waiting"]), round(T["backstop_if_nothing_earns"]), "8h reconciled")
    cmp("Figure 1", "Note: what comes back = 8h's backstop on 1 Jan 2033", round(F["topup_comes_back_1jan2033"]),
        round(RESERVE["margin_value_1jan2033_at_forwards"]), "8h")
    phrase = "money already received earns nothing while it waits"
    with open(WORDS_MD) as fh:            # read again: the wait-label loop above reuses the name `words`
        words_md = fh.read()
    ok = phrase in words_md and phrase in s8h1 and "every coupon and fund payout still counts" in words_md
    note("Figure 1", "Note: 'if interest earns nothing' defined once", phrase, "WORDS.md and 8h", "WORDS, 8h",
         "PASS" if ok else "FAIL")

    # ---- Table 2 against 8i (and 8j for the spread of the flexibility) ----
    s8i = _section(md, "### 8i.", "\n### 8j.")
    rows = _table_rows(s8i, "| World | Ten payments")
    prefix = {"forwards": "Today's forwards", "minus3": "Rates 3 points lower", "2007-07": "Joint replay from Jul 2007",
              "2006-06": "Joint replay from Jun 2006", "inflation": "Inflation world"}
    for key, name, v in TABLE2_WORLDS:
        r = [x for x in rows if x[0].startswith(prefix[key])][0]
        note("Table 2", f"{name}: ten payments", v["payments"], r[1], "8i", "PASS" if v["payments"] == r[1] else "FAIL")
        cmp("Table 2", f"{name}: stated bottom", v["bottom"], _money(r[2])[0], "8i")
        cmp("Table 2", f"{name}: stated bottom unrounded", round(v["bottom_raw"]), _money(r[2])[1], "8i")
        cmp("Table 2", f"{name}: stated top", v["top"], _money(r[3])[0], "8i")
        cmp("Table 2", f"{name}: stated top unrounded", round(v["top_raw"]), _money(r[3])[1], "8i")
        cmp("Table 2", f"{name}: contribution", round(v["contribution"]), _money(r[5])[0], "8i")
        cmp("Table 2", f"{name}: flexibility (half kept plus excess)", round(v["flexibility"]), _money(r[8])[0], "8i")
        cmp("Table 2", f"{name}: half kept + excess = flexibility", round(v["half_kept"]) + round(v["excess"]),
            round(v["flexibility"]), "8i", tol=1.0)
        cmp("Table 2", f"{name}: contribution = min(funds pay, top)", v["contribution"], min(v["funds_pay"], v["top"]), "8i rule")
        cmp("Table 2", f"{name}: note claim, contribution = stated top", v["contribution"], v["top"], "8i")
    spread = _table_rows(s8i, "| | 1-in-20 low")
    sb = _money([r for r in spread if r[0] == "Stated bottom"][0][1] + " " + " ".join([r for r in spread if r[0] == "Stated bottom"][0][2:]))
    st = _money(" ".join([r for r in spread if r[0] == "Stated top"][0][1:]))
    for i, (label, v) in enumerate(TABLE2_SPREAD):
        cmp("Table 2", f"585 windows {label}: stated bottom", v["bottom"], sb[i], "8i")
        cmp("Table 2", f"585 windows {label}: stated top", v["top"], st[i], "8i")
        cmp("Table 2", f"585 windows {label}: note claim, contribution = stated top (8j)", v["contribution"], st[i], "8i, 8j")
    s8j = _section(md, "### 8j.", "\n### 8k.")
    r = [x for x in _table_rows(s8j, "| Test (gift") if x[0].startswith("The half kept plus the excess: the same")][0]
    fx = _money(r[3])
    for i, (label, v) in enumerate(TABLE2_SPREAD):
        cmp("Table 2", f"585 windows {label}: flexibility", round(v["flexibility"]), fx[i], "8j (joint replay column)")
    allw = all(v["contribution"] == v["top"] for _, _, v in TABLE2_WORLDS)
    note("Table 2", "Result row: contribution = stated top in every world and replay", TABLE2_RESULT_ROW,
         f"five worlds {'all' if allw else 'NOT all'}; replays share {_JR['share_contribution_equals_stated_top']:.0%}",
         "8i, 8j (twd_test.joint_replay)", "PASS" if allw and _JR["share_contribution_equals_stated_top"] == 1.0 else "FAIL")
    m = re.search(r"windows \(Jan 1962 to Sep 2010 starts\)", s8i)
    note("Table 2", "Spread rows' data span", TABLE2_SPREAD_LABEL, m.group(0) if m else None, "8i",
         "PASS" if m and "1962-2010" in TABLE2_SPREAD_LABEL else "FAIL")
    m = re.search(r"\$120,000, worth \$([\d,]+) in 1 Jan 2027 dollars", s8i)
    infl = JOINT["scenarios"]["inflation"]["gift_in_2027_us_dollars"]
    cmp("Table 2", "Inflation row's contribution in 1 Jan 2027 dollars (now for 3b or 3c prose)", round(infl), float(m.group(1).replace(",", "")), "8i")

    # ---- 8k: the flexibility at forwards, by the second route ----
    s8k = _section(md, "### 8k.", "\n## 9.")
    m = re.search(r"The flexibility \(half kept plus excess\) is \$([\d,]+)", s8k)
    fwd = TABLE2_WORLDS[0][2]
    cmp("Table 2", "Flexibility at forwards (8k)", round(fwd["flexibility"]), float(m.group(1).replace(",", "")), "8k")
    r1 = RETURNS["route1_other_files"]
    cmp("Table 2", "Flexibility at forwards, route 1 of returns_check (range_rule's half kept + excess)",
        r1["half_kept_from_range_rule_jan2033"] + r1["excess_from_range_rule_dec2032"], round(fwd["flexibility"]),
        "8k check", tol=1.0)

    # ---- Table 3 against NUMBERS 2, 5, 8d, 8h, 8j and SKELETON's definitions (Exhibits item 4) ----
    s5 = _section(md, "## 5. A smaller or missed 2028 deposit", "\n## 6.")
    r = [x for x in _table_rows(s5, "| Yields fall before Jan 2027") if x[0].startswith("None")][0]
    cmp("Table 3", "Row 1: the top-up ($38,282)", round(TOPUP), _money(r[2])[0], "5")
    cmp("Table 3", "Row 1: what the ten Treasuries still lack ($2,388)", round(TOPUP_TEN_LACK), _money(r[1])[0], "5")
    m = re.search(r"the \$([\d,]+) tail plus the backstop \(\$([\d,]+)\)", s2)
    cmp("Table 3", "Row 1: the top-up's part for no interest on money received ($35,894)", round(TOPUP_NO_INTEREST),
        float(m.group(2).replace(",", "")), "2")
    cmp("Table 3", "Row 1: the top-up's two parts add up", round(TOPUP_TEN_LACK) + round(TOPUP_NO_INTEREST),
        round(TOPUP), "2, 5")
    dep = [x for x in _table_rows(s5, "| 2028 deposit | Floor money") if x[0].startswith("$150,000")]
    cmp("Table 3", "Row 1: the 2028 deposit", DEPOSIT_2028, _money(dep[0][0])[0] if dep else None, "5")
    m = re.search(r"After 2 points: the floor takes all \$[\d,]+ left, VT \$0, stated \$([\d,]+)", s5)
    cmp("Table 3", "Row 6: bottom after a 2-point fall before Jan 2027", BOTTOM_AFTER_2PT_FALL,
        float(m.group(1).replace(",", "")) if m else None, "5")
    m = re.search(r"The standard takes the whole \$150,000 at a ([\d.]+)-point fall", s5)
    cmp("Table 3", "Row 6: the fall at which the top-up takes the whole deposit (points)", FALL_TAKES_WHOLE_DEPOSIT,
        float(m.group(1)) if m else None, "5", tol=0.0001)
    s8d = _section(md, "### 8d.", "\n### 8e.")
    m = re.search(r"USD/TWD:\*\* ([\d.]+) on 6 Nov", s8d)
    cmp("Table 3", "Row 7: Taiwan dollars to the US dollar", TWD_PER_USD, float(m.group(1)) if m else None, "8d",
        tol=0.0001)
    m = re.search(r"band ([\d.]+)%-([\d.]+)% \(DGBAS construction cost index", s8d)
    cmp("Table 3", "Row 7: building costs, low end of the band (%)", 100 * CCI_BAND[0], float(m.group(1)), "8d",
        tol=0.0001)
    cmp("Table 3", "Row 7: building costs, high end of the band (%)", 100 * CCI_BAND[1], float(m.group(2)), "8d",
        tol=0.0001)
    m = re.search(r"A ([\d.]+)% stronger Taiwan dollar on \$([\d,]+) needs \$([\d,]+) more", re.sub(r"\s+", " ", s8j))
    cmp("Table 3", "Row 7: the test, a stronger Taiwan dollar (%)", 100 * TWD_TEST, float(m.group(1)), "8j", tol=0.0001)
    cmp("Table 3", "Row 7: the contribution it is tested on", round(CONTRIBUTION_FWD), _money(m.group(0))[0], "8j")
    cmp("Table 3", "Row 7: more US dollars needed", round(TWD_NEED), _money(m.group(0))[1], "8j")
    m = re.search(r"with the excess \(\$([\d,]+)\), ([\d.]+) times", re.sub(r"\s+", " ", s8j))
    cmp("Table 3", "Row 7: her flexibility at today's forwards", round(FLEX_FWD), float(m.group(1).replace(",", "")),
        "8j", tol=0.5)
    cmp("Table 3", "Row 7: her flexibility as printed (Table 2's rounding)", float(hundreds(FLEX_FWD)[1:].replace(",", "")),
        float(table2_cells(TABLE2_WORLDS[0][2])[3][1:].replace(",", "")), "Table 2, row 1")
    m = re.search(r"pays on (\w{3} \d+ \w{3} \d{4})\)", s8h)
    note("Table 3", "Row 2: the Feb-2037 bond's business-day date", _d(FEB37_PAYS), m.group(1) if m else None, "8h",
         "PASS" if m and m.group(1) == _d(FEB37_PAYS) and FEB37_PAYS.weekday() == 1 else "FAIL")
    with open(os.path.join(FR, "research", "cards", "Q2b_escrows_lotteries_settlements_stress.md")) as fh:
        q2b = re.sub(r"\s+", " ", fh.read())
    m = re.search(r"the five iBond rungs (\d+ to \d+) business days .*?2036 the tightest at (\d+ to \d+)", q2b)
    ok = bool(m) and m.group(1) == IBOND_SLACK and m.group(2) == IBOND_SLACK_2036
    note("Table 3", "Row 4: business days of slack, all years and 2036", f"{IBOND_SLACK}; {IBOND_SLACK_2036}",
         f"{m.group(1)}; {m.group(2)}" if m else None, "card Q2b, card 5", "PASS" if ok else "FAIL")
    m = re.search(r"the 2033 payment is \$([\d,]+) short at forward rates", re.sub(r"\s+", " ", s5))
    cmp("Table 3", "Row 1: a missed deposit, the 2033 payment short", round(MISSED_SHORT_2033),
        float(m.group(1).replace(",", "")) if m else None, "5")
    with open(SKELETON_MD) as fh:
        sk = fh.read()
    sk4 = sk[sk.index("4. **Table 3, monitoring**"):]
    sk4 = sk4[:sk4.index("\n## ")]
    for what, mine, want in (
            ("Row 1: a missed deposit", f"nothing received by {_d(MISSED_BY, weekday=False)}",
             "a missed deposit** is nothing received by 31 March 2028"),
            ("Row 2: a Treasury default", f"within {_NUM[DEFAULT_DAYS]} business days", "within five business days"),
            ("Row 1: the early warning", f"confirmed in writing by {_d(CONFIRM_BY, weekday=False)}",
             "confirms the deposit in writing by 1 December 2027"),
            ("Row 3: the X-date's window", "within a month of a date the plan needs cash",
             "within a month of a date the plan needs cash"),
            ("Row 5: the trade days", f"{_d(TRADE_DAYS[0])} and {_d(TRADE_DAYS[1])}", "Mon 4 Jan 2027 and Mon 3 Jan 2028"),
            ("Row 5: the first draw", "first draw after January 2033", "first draw slipping past January 2033"),
            ("Row 6: the distances", f"{dollars(BOTTOM_AFTER_2PT_FALL)}; {FALL_TAKES_WHOLE_DEPOSIT:.2f}-point",
             "cuts the stated bottom to $60,000; a 3.60-point fall takes the whole deposit"),
            ("Row 7: the test", f"{100 * TWD_TEST:.0f}% stronger", "row 7 tests a 10% stronger Taiwan dollar")):
        note("Table 3", what, mine, want, "SKELETON Exhibits item 4", "PASS" if want in sk4 else "FAIL")
    shut = (TRADE_DAYS[0] - _date(2027, 1, 1)).days == 3 and _date(2028, 1, 1).weekday() == 5 and \
        all(d.weekday() == 0 for d in TRADE_DAYS)
    note("Table 3", "Row 5: both trade days are the first market day of the year", "Mondays after a closed 1 January",
         "1 Jan 2027 holiday (Fri), 1 Jan 2028 Saturday", "calendar", "PASS" if shut else "FAIL")
    # Every figure printed in Table 3 is one checked above (a printed number with no check fails here)
    printed = " ".join(cell_text(c) for _, cells in TABLE3_ROWS for c in cells)
    allowed = {dollars(DEPOSIT_2028), dollars(TOPUP), dollars(TOPUP_TEN_LACK), dollars(TOPUP_NO_INTEREST),
               dollars(MISSED_SHORT_2033),
               dollars(BOTTOM_AFTER_2PT_FALL), dollars(TWD_NEED), dollars(CONTRIBUTION_FWD), hundreds(FLEX_FWD)}
    found = set(re.findall(r"(?<![A-Z])\$[\d,]+", printed))   # NT$ and US$ mark an exchange rate, not a dollar figure
    if "US$1 = NT$" in printed:
        note("Table 3", "Row 7: the exchange rate as printed", f"US$1 = NT${TWD_PER_USD:.3f}", "32.768 (8d)", "8d",
             "PASS" if f"US$1 = NT${TWD_PER_USD:.3f}" in printed else "FAIL")
    note("Table 3", "Every dollar figure printed is checked", ", ".join(sorted(found)), ", ".join(sorted(allowed)),
         "this check", "PASS" if found <= allowed else "FAIL")
    nums = set(re.findall(r"(?<![\w$,.])\d+(?:\.\d+)?%?", printed.replace("NT$", "NT ").replace("US$", "US ")))
    known = {"2028", "31", "2027", "4", "3", "17", "2037", "10", "14", "2031", "2033", "2", "1", "1.5%", "5.0%",
             "9", "6", "2036",
             f"{FALL_TAKES_WHOLE_DEPOSIT:.2f}", f"{TWD_PER_USD:.3f}", "10%"}
    note("Table 3", "Every other number printed is a checked date or figure", ", ".join(sorted(nums - known)) or "none",
         "dates and figures above", "this check", "PASS" if nums <= known else "FAIL")

    banned3 = ("backstop", "gift", "overflow", "paths", "forward rates", "half kept", "kept half", "moved half", "rung",
               "completion", "model", "cap ", "capped", "excess", "stated ends", "escrow")
    printed3 = " ".join([printed] + TABLE3_HEADER + list(TABLE3_LEVELS.values())).lower()
    note("Table 3", "No word WORDS.md bans", ", ".join(b for b in banned3 if b in printed3) or "none", "none",
         "WORDS.md", "PASS" if not any(b in printed3 for b in banned3) else "FAIL")

    fails = [x for x in res if x[5] == "FAIL"]
    if verbose:
        for ex, what, mine, reg, sec, status in res:
            if status != "PASS":
                print(f"  {status:<8} {ex:<9} {what}: exhibit {mine} | register {reg} ({sec})")
        n_pass = sum(1 for x in res if x[5] == "PASS")
        print(f"Check against NUMBERS.md: {len(res)} figures, {n_pass} PASS, {len(fails)} FAIL, "
              f"{len(res) - n_pass - len(fails)} flagged (placeholders or rounding, listed above)")
    return fails, res


if __name__ == "__main__":
    print("Table 1 (NUMBERS 8g v2, WInS record at cost)")
    for kind, cells in table1_rows():
        print(f"  {kind:<9}", " | ".join(c.replace("\n", " / ") for c in cells))
    print("\nFigure 1 (NUMBERS 8h, MODEL): year | paid from | cash arrives | at forwards | nothing earns after fee: own + top-up")
    for f in FIGURE1_ROWS:
        print(f"  {f['year']} | {f['holding']:<16} | {cash_words(f)} ({f['wait_words'] or str(f['months_cash']) + ' mo'}) |"
              f" {dollars(f['at_forwards'])} | {dollars(f['own_if_nothing_earns'])} + {dollars(f['backstop_if_nothing_earns'])}")
    T = FIGURE1_TOTALS
    print(f"  Total {dollars(T['at_forwards'])} | {dollars(T['own_if_nothing_earns'])} + {dollars(T['backstop_if_nothing_earns'])}")
    print("\nTable 2 (NUMBERS 8i, 8j, MODEL)")
    for _, name, v in TABLE2_WORLDS:
        print(f"  {name:<36}", " | ".join(table2_cells(v)))
    print(f"  {TABLE2_SPREAD_LABEL}")
    for label, v in TABLE2_SPREAD:
        print(f"  {label:<36}", " | ".join(table2_cells(v)))
    print("\nTable 3 (SKELETON Exhibits item 4; figures from NUMBERS 2, 5, 8d, 8h, 8j)")
    for kind, cells in table3_rows():
        print(f"  {kind:<8}", " | ".join(cell_text(c) for c in cells))
    print()
    fails, _ = check()
    sys.exit(1 if fails else 0)
