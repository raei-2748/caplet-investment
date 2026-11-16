"""Data for the Final Report exhibits, on the register of Tue 10 Nov 2026 (rebuilt Wed 11 Nov 2026, Sydney; on the
Sun 15 Nov evening re-run files since then, every input path and figure re-checked Mon 16 Nov morning).

Design H_plain ("sufficient without reinvestment", with the fee cushion), the Treasury curve of Fri 6 Nov 2026, the
range rule on the fund's holdings and Keel's reading of "most". Everything modelled is MODEL (NUMBERS.md stamp).

Where the figures come from:
  Table 1  (Section 2)      NUMBERS.md 8g version 2, the WInS record at cost. No results file holds it, so the rows are
                            copied here by hand and check() compares every cell with the 8g table. Since Thu 12 Nov
                            evening also the units bought against the targets set before trading (NUMBERS 8m), checked
                            against 8m, the Portfolio tab (portfolio.csv) and the 23 Oct WInS snapshot.
  Figure 1 (3a)             numbers/results_reserve_2026-11-15.json (NUMBERS 8h): blocks composition_1jan2033_base,
                            base (today's forwards), fee (nothing earns interest and waiting money pays the ETF's fee:
                            Keel's standard, SKELETON Exhibits item 2) and zero (nothing earns interest, no fee).
  Table 2  (3b, 3c)         numbers/results_joint_stress_2026-11-15.json (NUMBERS 8i, 8j): scenarios forwards, minus3
                            and inflation; joint.named 2006-06 and 2007-07; the 585-window percentiles; and
                            twd_test.joint_replay for the contribution and the flexibility across windows.
  Cross-check (8k)          numbers/results_returns_2026-11-15.json: the flexibility at forwards by a second route.
  Figure 1, Fri 13 Nov      numbers/results_topup_2026-11-15.json (NUMBERS 8h): when each payment's cash reaches Laura
                            (a fund's end date is not its cash date; a bond due on a weekend or holiday pays the next
                            business day), and the top-up's column reconciled with its cost (the note items).
  Table 3  (3e)             numbers/results_2026-11-15.json (NUMBERS 2, 5) and inflation_inputs.json (8d).
  Mon 16 Nov evening        Figure 1 at one basis (8h "fee"), its heads printing the sum and its total row 8h's totals
                            ($444,080 + $55,920 = $500,000; the rows foot to $444,081 and $55,919, a required note
                            item); the title opens with its condition (card Q73). Table 2's held-the-same line and the
                            note's check of the five worlds against the median replay (8i, 8j; card Q14b rows 20-21).
  Mon 16 Nov night          the hand edits made that night in tables.md (coherence reader 6; bond desk 4), carried
                            here: WORDS's names in Figure 1's legend and Table 2 (head, first row, history label, last
                            row); Table 3 rows 1, 2, 4, 5, 6 and 7 (row 1's second figure, the ten $57,455 short if cash
                            waiting earns nothing: results_2026-11-15.json C6.missed.short_at_zero, NUMBERS 5; row 7's
                            29.79 = 32.768 / 1.10 and its 9.1%, NUMBERS 8j), each checked in check().
  The backstop on 1 Jan 2033 (Figure 1's note, item 4 since Mon 16 Nov evening): its VALUE there at today's forwards, $45,456
                            (results_reserve margin_value_1jan2033_at_forwards; NUMBERS 8h, 8i, section 4), never its
                            cost carried, $45,487 (margin_cost_carried_to_1jan2033_at_forwards: no funds' fee). NUMBERS 9.

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
REGISTER_DATE = "2026-11-15"   # Sun 15 Nov evening: the re-run with the fee charged in the range rule (was 2026-11-10)


def _load(name):
    with open(os.path.join(NUMBERS_DIR, name)) as fh:
        return json.load(fh)


RESERVE = _load(f"results_reserve_{REGISTER_DATE}.json")
JOINT = _load(f"results_joint_stress_{REGISTER_DATE}.json")
RETURNS = _load(f"results_returns_{REGISTER_DATE}.json")
MAIN = _load(f"results_{REGISTER_DATE}.json")          # NUMBERS sections 1-5 (Table 3: the top-up, section 5's distances)
INPUTS = _load("inflation_inputs.json")                # NUMBERS 8d's inputs (Table 3: the Taiwan dollar, building costs)
TOPUP_PAID = _load(f"results_topup_{REGISTER_DATE}.json")    # NUMBERS 8h, Fri 13 Nov: the top-up reconciled; the cash dates
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
    ("912810PT9", "T-Bond 4.750% 15-Feb-2037", "Treasury bond", 19203.80, 6.40, "2038 payment"),
    ("912810PX0", "T-Bond 4.500% 15-May-2038", "Treasury bond", 18615.26, 6.20, "2039 payment"),
    ("912810QD3", "T-Bond 4.375% 15-Nov-2039", "Treasury bond", 16200.95, 5.40, "2040 payment"),
    ("912810QL5", "T-Bond 4.250% 15-Nov-2040", "Treasury bond", 15790.32, 5.26, "2041 payment"),
    ("912810QT8", "T-Bond 3.125% 15-Nov-2041", "Treasury bond", 14991.00, 5.00, "2042 payment"),
    ("VT", "Vanguard Total World Stock ETF", "ETF (equity)", 26524.61, 8.84, "Growth: top of the range and the half kept"),
    ("N/A", "Cash", "Cash", 3513.79, 1.17, "Cash"),
    ("N/A", "Commissions and bond interest paid at purchase", "Cost", 1309.42, 0.44, "Cost of buying"),
]
HOLDINGS_TOTAL = (300000.00, 100.00)  # 8g: "must equal $300,000 and 100%"
N_TREASURIES = 10                      # the first ten rows, in payment order 2033-2042
HOLDINGS_NOTE_FACTS = {"commissions": 200.00, "accrued_interest": 1109.42, "wins_cash": 3513.79,
                       "trade_dates": "6-7 Oct 2026 (U.S. Eastern)"}

# How Table 1 prints 8g's cells. Identifiers (Fri 13 Nov evening, card Q38): tickers for the six ETFs and, for the
# five Treasury bonds, their CUSIPs, each read at Treasury's Fiscal Data auctions dataset and in the bond's own
# TreasuryDirect auction result; no placeholder is left, and Caplet's WInS export is no longer needed for Table 1.
# Wharton's example "532281" is not a CUSIP and is never printed (never a mix of WInS numbers and CUSIPs). Asset types: 8g's "ETF (Treasury)" and
# "ETF (equity)" in plain words; at 12 pt "ETF (Treasury)" would push the longest fund name off one line.
ID_PRINT = {}   # no placeholders since Fri 13 Nov evening (card Q38)
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
VT_UNITS_WORDS = ("bought last,", "with the rest")   # Fri 13 Nov evening: "from cash left" (0.926 in) no longer fits the 0.97-in column the CUSIPs pay for; "with the rest" is 0.824 in; the note keeps "the cash then left"
UNITS_HEAD = "Units bought / target"
# Since the "Pays for" column (fresh reader, Wed 11 Nov) the types are one word, Wharton's own ("ETF", and "Bond" for
# its "Treasury Bond"): each name already says Treasury, T-Bond or Stock.
TYPE_PRINT = {"ETF (Treasury)": "ETF", "ETF (equity)": "ETF", "Treasury bond": "Bond", "Cash": "Cash", "Cost": "Cost"}
# "Pays for": the payment year each holding funds in the miniature (8g: the WInS book is Laura's whole plan in
# miniature). Two cells take two lines at 12 pt in the 0.79-in column ("\n" is a line break): IBTM's two jobs (TNA l.13,
# CANON A24) and VT's (IPS l.15; "flexibility" is the IPS's word for the half promised to no one, and Table 2's head).
PAYS_FOR_PRINT = {"2033 payment and floor stand-in": "2033 and\nthe floor",
                  "Growth: top of the range and the half kept": "Range\ntop,\nflexibility",   # 3 lines in the 0.71-in column (Fri 13 Nov evening)
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
# Figure 1, the operating reserve running down (3a). NUMBERS 8h, MODEL, read from results_reserve_2026-11-15.json.
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
    # Mon 16 Nov (NUMBERS 9): the backstop is read at its VALUE on 1 Jan 2033 at today's forwards ($45,456: the reserve
    # before the first payment less the own rungs, 8h), never its cost carried there ($45,487, which leaves out the
    # funds' fee). Read from 8h's own reserve run; the top-up file and Table 2's forwards world must agree (below).
    "topup_comes_back_1jan2033": RESERVE["margin_value_1jan2033_at_forwards"],             # $45,456
    "backstop_cost_carried_1jan2033": RESERVE["margin_cost_carried_to_1jan2033_at_forwards"],   # $45,487: never printed
}
_bk = FIGURE1_NOTE_FACTS["topup_comes_back_1jan2033"]
assert abs(_bk - (RESERVE["composition_1jan2033_total"] - RESERVE["own_rungs_value_1jan2033"])) < 0.01, _bk
assert abs(_bk - TOPUP_PAID["comes_back_if_forwards_hold"]["value_1jan2033"]) < 0.01, _bk
assert abs(_bk - JOINT["scenarios"]["forwards"]["overflow_jan2033_value"]) < 0.01, _bk
assert round(_bk) != round(FIGURE1_NOTE_FACTS["backstop_cost_carried_1jan2033"]), "the backstop must be its value"


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
# Mon 16 Nov evening (card Q73's three fixes, charts/DESIGNS.md section 2):
#   1. the sum in the column heads, "Its own Treasury + Extra Treasuries = $50,000" (Q73-010, -036: LACERA's formula
#      head, GASB 67's Funded/Unfunded split), and a total row that adds up exactly, "$444,080 + $55,920 = $500,000"
#      (8h's totals of unrounded figures; Missouri's two equal totals, Q73-002); the printed rows foot to $444,081 and
#      $55,919, so the rounding note is a required note item, no longer "if room";
#   2. one world per exhibit (Q73-035): the "At today's market rates" column ($50,000 ten times) leaves the figure for
#      the note; the figure is drawn at one basis only, cash waiting earning nothing after the 0.15% fee (8h "fee");
#   3. the condition first in the title, then the verdict (Q73-016, -037); never "about 89%", which is not in NUMBERS.
# The question head ("If cash waiting earns nothing, what pays each $50,000?", Thu 12 Nov) goes: the title now opens
# with the condition and the heads print the sum, so the figure is two head lines shorter.
FIGURE1_PAYMENT = 50000.0                       # each payment (8h: each own holding pays exactly $50,000 at forwards)
FIGURE1_HEADS = {
    "payment": "Payment",
    "timeline": "Held from January 2027 until its cash arrives",
    "c2": ("Its own", "Treasury"),
    "c3": ("Extra", "Treasuries"),  # Fri 13 Nov evening: the $35,894's name (WORDS); was "What the top-up pays"
    "plus": "+",
    "equals": "=",
    "sum": dollars(FIGURE1_PAYMENT),            # the heads read "Its own Treasury + Extra Treasuries = $50,000"
}
# Mon 16 Nov night (coherence reader 6, L2): the legend's fund key is the figure's own Type column, "iBond Treasury
# fund" (was "iBonds Treasury ETF")
FIGURE1_LEGEND = ("iBond Treasury fund", "Treasury bond", "$50,000 due on 1 January", "cash waiting")
FIGURE1_TITLE = ("If Cash Waiting Earns Nothing, Each $50,000 Payment Is Still Met by Its Own Treasury and Extra "
                 "Treasuries From the 2028 Deposit (Laura's Plan for Both Deposits, $450,000, Modelled)")
# The total row: 8h's totals of unrounded figures, which add exactly to the ten payments ($500,000)
FIGURE1_TOTAL_ROW = (FIGURE1_TOTALS["own_if_nothing_earns"], FIGURE1_TOTALS["backstop_if_nothing_earns"],
                     FIGURE1_TOTALS["own_if_nothing_earns"] + FIGURE1_TOTALS["backstop_if_nothing_earns"])
assert round(FIGURE1_TOTAL_ROW[0]) + round(FIGURE1_TOTAL_ROW[1]) == round(FIGURE1_TOTAL_ROW[2]) == \
    10 * FIGURE1_PAYMENT == round(FIGURE1_TOTALS["at_forwards"]), FIGURE1_TOTAL_ROW
# What the printed rows add to (each row rounded to the dollar): the rounding note's pairing
FIGURE1_FOOT = (sum(round(r["own_if_nothing_earns"]) for r in FIGURE1_ROWS),
                sum(round(r["backstop_if_nothing_earns"]) for r in FIGURE1_ROWS))
assert sum(FIGURE1_FOOT) == 10 * FIGURE1_PAYMENT, FIGURE1_FOOT


# =================================================================================================================
# Table 2, the plan under several markets (3b, 3c). NUMBERS 8i (and 8j for the spread of the flexibility), MODEL.
# =================================================================================================================
# Row order (card Q28): the base first; the stresses by how far the stated range falls; the rates-up world last.
WORLDS = [
    # (key, plain name printed in the table, where the data sit in the JSON)
    # Mon 16 Nov night (coherence reader 6, L2): WORDS's name, "today's market rates", never "forward rates"
    ("forwards", "Today's market rates", ("scenarios", "forwards")),
    ("2006-06", "Replay from 2006: shares fall", ("named", "2006-06")),
    ("minus3", "Rates 3 points lower from Jan 2027", ("scenarios", "minus3")),   # Sat 14 Nov: timing labelled
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
# Mon 16 Nov night (coherence reader 6, L2): WORDS's name, "every starting month since 1962" (was "All 585 history
# replays")
TABLE2_SPREAD_LABEL = f"Every starting month since 1962 ({_J['windows']}, 1962-2010 starts)"
TABLE2_SPREAD = [
    (label, {"payments": "All paid", "bottom": _J["bottom_stated_p5_p50_p95"][i], "top": _J["top_stated_p5_p50_p95"][i],
             "contribution": _JR["contribution_p5_p50_p95"][i],
             "flexibility": _JR["kept_half_plus_excess"]["pot_p5_p50_p95"][i]})
    for i, label in enumerate(["1-in-20 low", "Median", "1-in-20 high"])
]
# The contribution is not a column: it equals the stated top in every world and every window (8i, 8j; checked below).
# It is the confidence answer, so it is a row of the table, the last one (fresh reader and coordinator, Wed 11 Nov),
# not a clause of the note.
# Mon 16 Nov night (coherence reader 6, M6; WORDS l.28; SKELETON Exhibits item 3): $29,800 is her flexibility plus
# anything above the top, said so, never under "Flexibility" alone, so the last head names both, in print as well.
TABLE2_FLEX_HEAD = "Her flexibility and anything above the top (Jan 2033)"
TABLE2_HEADER = ["World", "Ten payments", "Stated bottom (2031)", "Stated top (2031)", TABLE2_FLEX_HEAD]
# As printed: an APA column spanner groups the two stated ends (the range Laura announces). Since Mon 16 Nov night the
# last head sets on four lines in its 1.15-in column (was two, "Flexibility / (Jan 2033)"): measured, Table 2 costs
# 1.0 double-spaced line more for it (17.2 to 18.2 with its 95-word note), and 0.5 more for the last row, which "every
# starting month" sets on two lines (16.7 to 17.2).
TABLE2_SPANNER = "Stated in 2031"
TABLE2_HEAD_ROW = ["World", "Ten payments", "Bottom", "Top", TABLE2_FLEX_HEAD]
# Mon 16 Nov night (coherence reader 6, L2 and M6): "every starting month" (WORDS), never "every replay"
TABLE2_RESULT_ROW = ("In every world and every starting month, the facility contribution in January 2033 equals the "
                     "stated top.")
# Mon 16 Nov evening (card Q14b row 20; charts/DESIGNS.md sections 3 and 8): one line, under the heads, naming what is
# held the same in every row, as the Bank of England's Table 3.A row "Assumptions that are consistent across
# projections". Every row is the same plan (NUMBERS 8i: one design, one range rule, one run): both deposits ($300,000
# in January 2027, $150,000 in January 2028), the plan's steps on their dates (the ten in January 2027; the top-up,
# the extra Treasuries, the floor and VT in January 2028; half of VT moved before the 2031 meetings), the funds' fees
# (0.07%, the waiting ETF's 0.15%, VT's 0.06%; NUMBERS 0) and the range rule (NUMBERS 0, 3); only Treasury yields and
# share prices differ (the inflation row's 5% prices change no printed cell, only the 2027-dollar value, 8i). Checked
# in check(): the 2028 deposit is $150,000 in every scenario world, one rule stamp for the whole run.
TABLE2_HELD_SAME = ("Every row keeps the plan's deposits, steps, dates, fees and range rule; only the markets "
                    "differ.")
# The note's check against history (Mon 16 Nov, ARGUMENT_LOG Day 9; card Q14b row 21, the Bank of England's staff
# checking named scenarios against a reference distribution): all five named worlds leave her less flexibility than
# the median replay. Computed here, checked in check(), and printed in the note.
TABLE2_FLEX_MEDIAN = TABLE2_SPREAD[1][1]["flexibility"]                       # $32,326 (8j joint replay column)
TABLE2_FLEX_WORLDS = (min(v["flexibility"] for _, _, v in TABLE2_WORLDS),     # $19,476 (replay from 2006)
                      max(v["flexibility"] for _, _, v in TABLE2_WORLDS))     # $29,823 (today's forwards)
assert TABLE2_FLEX_WORLDS[1] < TABLE2_FLEX_MEDIAN, (TABLE2_FLEX_WORLDS, TABLE2_FLEX_MEDIAN)


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
BOTTOM_AFTER_1PT_FALL = _C6["fall_100bp"]["150000"]["stated_bottom"]   # $85,000: "most" still holds (NUMBERS 5)
FALL_TAKES_WHOLE_DEPOSIT = 3.60   # points; NUMBERS 5 text only (no results file holds it), checked against the text
TWD_PER_USD = INPUTS["usdtwd"]["latest"]                                # 32.768 on 6 Nov (NUMBERS 8d)
CCI_BAND = (INPUTS["taiwan_construction"]["low"], INPUTS["taiwan_construction"]["high"])   # 1.5% to 5.0% (8d)
CCI_5Y = 0.0327                                          # building costs a year, five years to Sep 2026 (8d; card Q10 row 20)
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
# Mon 16 Nov night (coherence reader 6, M7; bond desk 4, L5): the missed deposit's cost on both bases, never the
# $3,016 alone (NUMBERS 5 and l.1900): the ten $57,455 short if cash waiting earns nothing
MISSED_SHORT_ZERO = MAIN["C6"]["missed"]["short_at_zero"]       # $57,455 (NUMBERS 5: "the ten are $57,455 short at 0%")
# Mon 16 Nov night (bond desk 4, M7): one reading of "10% stronger", 8j's (10% more US dollars for the same NT$
# budget): NT$ per US$ from 32.768 to 32.768 / 1.10 = 29.79, which is 9.1% below its level (1 - 1 / 1.10)
TWD_STRONG = TWD_PER_USD / (1 + TWD_TEST)                # 29.79 (NUMBERS 8j)
TWD_BAND = 1 - 1 / (1 + TWD_TEST)                         # 9.1%: how far NT$ per US$ falls for 10% more US dollars
IBOND_SLACK = "4 to 9"                                   # business days, cash in hand to the year's last business day (card Q2b)
IBOND_SLACK_2036 = "4 to 6"                              # the tightest year, 15 Dec 2035 a Saturday (card Q2b)
IBTA_SLACK = "19"                                        # Sun 15 Nov evening (card Q3c row 8): IBTA ended early, its cash
# about 19 business days before year end, notice filed 28 Sep 2021, so notices come in September to October (NUMBERS 8h)
DEFAULT_DAYS = 5                                         # a Treasury default: not paid within five business days
# Mon 16 Nov night (bond desk 4, M5): row 4 watches both fees, the iBond funds' and the waiting ETF's (NUMBERS 0), and
# a missing ending notice by the end of October of a fund's final year (notices come September to October, card Q3c)
FUND_FEE = 0.0007                                        # the iBond funds' fee (NUMBERS 0: "0.07% fee"), checked below
WAIT_FEE = FIGURE1_NOTE_FACTS["etf_fee"]                 # the short-term Treasury ETF's 0.15% a year (NUMBERS 0)
NOTICE_BY = "31 October"                                 # of the final year: the last day of the notice window


def _d(d, weekday=True):
    """'Mon 4 Jan 2027' (weekday=True) or '31 March 2028'."""
    return f"{d.strftime('%a')} {d.day} {d.strftime('%b')} {d.year}" if weekday else f"{d.day} {d.strftime('%B')} {d.year}"


_NUM = {5: "five"}
# Cells. Words are WORDS.md's: "the top-up", "her flexibility", "facility contribution", "simulated futures", "the
# floor", "the world share fund (VT)", "her team" (Wharton: "Laura or her asset management team"). The last column is
# a list of runs: (text, italic); "\n" breaks the line inside the cell.
TABLE3_HEADER = ["Signal", "Who", "Carry on while", "Look closer or act when",
                 "What it changes; what it never changes"]
TABLE3_LEVELS = {
    "reason": "The two reasons to change the plan",
    "closer": "Look closer: a date or an instrument may change, never the plan",
    "watch": "Watch: the plan carries on",
}


def _changes(changes, never):
    """The last column: two labelled parts in one run of text (a line break between them costs a line a row)."""
    return [("Changes: ", True), (changes + ". ", False), ("Never: ", True), (never + ".", False)]


# Fri 13 Nov evening (bond desk re-read, third coherence reader, lay reader; research/panel/2026-11-13_*): "Watched
# by" for "Reader"; row 1 names the first $38,282's two parts and what a missed deposit changes until the money comes;
# row 2 says how a due date moves; row 3 one set of cash dates, the X-date defined in the note; row 4 watches all three
# fund events (an early end, a merger, an end moved past a payment) and a missing October notice (card Q36), the swap
# for a Treasury "maturing just before it's needed" (IPS l.13) paid from the fund's own cash and any gap from the
# extra Treasuries, never "the reserve" before 2033; row 5 adds the 2031 move, the first draw goes to 3e's prose;
# row 6 shows the 1-point case ("most" still holds, NUMBERS 5) and what a fall changes and when it stops changing it;
# the 3.6-point bound moves to the note; row 7's levels are dated and the five-year building-cost rate is shown.
TABLE3_ROWS = [
    ("reason", [
        f"The 2028 deposit ({dollars(DEPOSIT_2028)})",
        "Laura",
        f"Confirmed by {CONFIRM_BY.day} {CONFIRM_BY.strftime('%b')} {CONFIRM_BY.year}; its first {dollars(TOPUP)} "
        "(today's rates) to the payments",   # Sat 14 Nov (bond reader 2): a today's-rates figure, so labelled
        f"Nothing received by {_d(MISSED_BY, weekday=False)} (a missed deposit)",
        # Mon 16 Nov night (coherence reader 6, M7; bond desk 4, L5): both bases, never the $3,016 alone (NUMBERS 5);
        # L5's action wording declined: card Q34 keeps the later money's order in 3e's prose
        _changes(f"no range until money comes; the ten short: {dollars(MISSED_SHORT_2033)} at today's rates, "
                 f"{dollars(MISSED_SHORT_ZERO)} if cash waiting earns nothing",
                 "a sale")]),
    ("reason", [
        "Treasury payments",
        "Team",
        "Paid when due, or the next business day",   # 31 CFR 356.30(a): weekends and holidays alike (bond reader 2)
        f"A Treasury default: a payment over {_NUM[DEFAULT_DAYS]} business days late",
        # Mon 16 Nov night (bond desk 4, L6): Laura's payments are fixed at $50,000 and never restated
        _changes("each payment's cover and both ends re-checked on what was paid; the range restated",
                 "a forced sale")]),
    ("closer", [
        "Debt-limit X-date",
        "Team",
        "No X-date within a month of a cash date",
        "An X-date within a month of a cash date",
        _changes("nothing before it", "a sale ahead of it")]),
    ("closer", [
        # Mon 16 Nov night (coherence reader 6, L1: the frozen name of the waiting fund, TNA l.5, WN l.17; bond desk 4,
        # M5: filings read in any year, the ending notice in its final year, a dated missing-notice trigger and the
        # iBond fee beside the waiting ETF's; M4 and coherence reader 6, L17: one action per event, and no "Treasury due
        # by 15 December", which WInS does not list for 2033 or 2035 (WN l.20, l.22))
        "iBond and short-term Treasury ETF notices",
        "Team",
        f"Every filing read, any year; ending notice in September to October of the final year; cash {IBOND_SLACK} "
        f"business days before year end ({IBOND_SLACK_2036} for 2036); fees {100 * FUND_FEE:.2f}% and "
        f"{100 * WAIT_FEE:.2f}%",
        # Sun 15 Nov evening (card Q3c row 8): notices since September (IBTA's, 28 Sep 2021). IBTA's early end (cash
        # about 19 business days before year end) is the trigger's "ends early", for 3e's prose: any mention of it in
        # this row or the note puts Table 3 on two pages (measured); "for 2036" (was ", 2036 payment") keeps 18.9 lines
        f"A fund ends early, merges or moves past a payment; a fee rises; no ending notice by {NOTICE_BY} of the "
        "final year",
        _changes("early cash waits in the short-term Treasury ETF; a merged or moved fund is sold for an earlier iBond "
                 "fund or that ETF, any gap from the extra Treasuries, re-tested; a dearer waiting ETF swapped for a "
                 "cheaper one; the range's from its 0.5%",
                 "VT")]),
    # Sat 14 Nov (bond reader 2, coherence reader 4): an extension or merger needs a sale, so "paid out, or its shares
    # sold"; a 31 December note can pay after 1 January, so "by 15 December"; the late-2032 fund holds both ends of the
    # range, so "the range's" margin; a gap paid from the extra Treasuries leaves the no-interest test short by it, so
    # "re-tested"; the October notice is practice, not a duty ("without further notice"), so silence is a reading, not
    # a swap; the waiting money's bill fund (0.15%, NUMBERS 0, its fund UNVERIFIED) is now watched.   # Fri 13 Nov evening (card Q36 row 23): "the shares" could mean the iBond fund's own
    ("closer", [
        "Trades in 2027, 2028, 2031",
        "Team",
        # Mon 16 Nov night (bond desk 4, M6): a stressed trade day is a watch item (NUMBERS 0, l.82), so the row has a
        # trigger for it; its distance, [x]%, is a placeholder until NUMBERS carries it
        "First trading day; limit orders within [x]% of net asset value",
        "A date cannot be kept (a trading halt); prices further off: wait day by day",
        _changes("the date, never past the 2031 meetings", "the step or its order")]),
    # Sat 14 Nov (bond reader 2): an open date for the 2031 move is a timing option, and waiting after a fall is the
    # market call IPS l.17 rules out, so the day is fixed now (the first trading day, as modelled; Keel's call,
    # ASK_HUMANS); coherence reader 4: the 2031 date stays before the meetings (IPS l.15).
    ("watch", [
        "Treasury yields and share prices",
        "Team",
        "Any level",   # Sat 14 Nov (coherence reader 4): the l.17 echo dropped, as SKELETON said
        f"None (for scale: 1 point lower before 4 Jan 2027 gives an {dollars(BOTTOM_AFTER_1PT_FALL)} bottom)",
        # Mon 16 Nov night (coherence reader 6, L2): never "the 2031 move" alone
        _changes("the bottom to Jan 2028, the top to the move before the 2031 meetings, then her flexibility",
                 "the payments")]),
    ("watch", [
        "Her flexibility's three uses",
        "Laura",
        # Mon 16 Nov night (bond desk 4, M7): "carry on while" is a condition, measured from the rate when the range is
        # stated (8j; card Q10b), with 6 Nov 2026's rate for scale only
        f"NT$ per US$ within {100 * TWD_BAND:.1f}% of its level when the range is stated ({TWD_PER_USD:.3f} on 6 Nov "
        f"2026, for scale); building-cost trend {100 * CCI_BAND[0]:.1f}% to "
        f"{100 * CCI_BAND[1]:.1f}% a year",   # "trend": a rate over years, not a one-year ceiling
        # (card Q10c: costs rise in bursts); the five-year rate, 3.27% (8d), goes to 3e's prose: no room
        # Mon 16 Nov night (bond desk 4, M7): one reading of "10% stronger", 8j's: 10% more US dollars for the same NT$
        # budget, NT$ per US$ from 32.768 to 29.79 (never 29.49, which gives $12,778); its building-cost trigger declined
        # (SKELETON's Sat 14 Nov decision, CANON A34)
        f"NT$ per US$ {100 * TWD_BAND:.1f}% below its level when the range is stated ({TWD_STRONG:.2f} from "
        f"{TWD_PER_USD:.3f}): {100 * TWD_TEST:.0f}% more US dollars, {dollars(TWD_NEED)} on "
        f"{dollars(CONTRIBUTION_FWD)}",
        _changes(f"a call on her flexibility ({hundreds(FLEX_FWD)} in 2033 with anything above the top)",
                 "the range")]),
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
          and VT_UNITS_WORDS[1] == "with the rest")
    note("Table 1", "VT's cell: bought last, with the rest (of the cash)", " ".join(VT_UNITS_WORDS),
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
         "ROUNDING: rows equal 8h and foot $1 off its totals of unrounded figures (the note's required rounding "
         "item names the pairing, Mon 16 Nov evening)")
    # ---- Figure 1, Mon 16 Nov evening: card Q73's three fixes (charts/DESIGNS.md section 2) ----
    # 1. The sum in the heads and a total row that adds up exactly
    note("Figure 1", "Heads print the sum: Its own Treasury + Extra Treasuries = $50,000",
         " ".join([" ".join(FIGURE1_HEADS["c2"]), FIGURE1_HEADS["plus"], " ".join(FIGURE1_HEADS["c3"]),
                   FIGURE1_HEADS["equals"], FIGURE1_HEADS["sum"]]),
         "each row's own + extra = $50,000 (checked per row above)", "8h, card Q73-036",
         "PASS" if FIGURE1_HEADS["sum"] == dollars(50000) and all(
             round(f["own_if_nothing_earns"]) + round(f["backstop_if_nothing_earns"]) == 50000 for f in FIGURE1_ROWS)
         else "FAIL")
    a, b, s = (round(x) for x in FIGURE1_TOTAL_ROW)
    cmp("Figure 1", "Total row: own + extra = the sum printed (adds up exactly)", a + b, s, "8h", tol=0)
    cmp("Figure 1", "Total row: the sum = the ten payments at $50,000", s, 10 * 50000, "8h", tol=0)
    cmp("Figure 1", "Total row: the sum = 8h's All-ten total ($500,000)", s, _money(tot[1])[0], "8h", tol=0)
    cmp("Figure 1", "Total row: own = 8h's All-ten total, after fee", a, _money(tot[4])[0], "8h", tol=0)
    cmp("Figure 1", "Total row: extra = 8h's All-ten total, after fee", b, _money(tot[4])[1], "8h", tol=0)
    cmp("Figure 1", "Rounding note: the printed rows' foot adds to $500,000", sum(FIGURE1_FOOT), 10 * 50000,
        "8h", tol=0)
    cmp("Figure 1", "Rounding note: own foot is $1 from 8h's total", abs(FIGURE1_FOOT[0] - a), 1, "8h", tol=0)
    cmp("Figure 1", "Rounding note: extra foot is $1 from 8h's total", abs(FIGURE1_FOOT[1] - b), 1, "8h", tol=0)
    # 2. One world: the figure prints only the zero-interest-after-fee basis; today's rates go to the note
    printed_heads = " ".join([FIGURE1_HEADS["payment"], FIGURE1_HEADS["timeline"]] + list(FIGURE1_HEADS["c2"]) +
                             list(FIGURE1_HEADS["c3"]) + [FIGURE1_HEADS["sum"]] + list(FIGURE1_LEGEND)).lower()
    one_world = "c1" not in FIGURE1_HEADS and "today" not in printed_heads and "today" not in FIGURE1_TITLE.lower()
    note("Figure 1", "One world: no today's-rates column, head or title (it is in the note)", "one basis",
         "card Q73-035", "card Q73", "PASS" if one_world else "FAIL")
    cmp("Figure 1", "Note, today's rates: every own Treasury pays its whole $50,000 (rows at forwards)",
        sum(1 for f in FIGURE1_ROWS if round(f["at_forwards"]) == 50000), 10, "8h", tol=0)
    # 3. The condition first in the title, then the verdict
    note("Figure 1", "Title opens with the condition", FIGURE1_TITLE.split(",")[0], "If Cash Waiting Earns Nothing",
         "card Q73-016, -037", "PASS" if FIGURE1_TITLE.startswith("If Cash Waiting Earns Nothing,") else "FAIL")
    note("Figure 1", "Title keeps its scale and basis", "$450,000; Modelled", "specs.md section 0", "specs.md",
         "PASS" if "$450,000" in FIGURE1_TITLE and "Modelled" in FIGURE1_TITLE else "FAIL")
    note("Figure 1", "Title never gives a share NUMBERS does not hold (\"about 89%\")", FIGURE1_TITLE,
         "no per cent", "DESIGNS section 2, rater P", "PASS" if "%" not in FIGURE1_TITLE else "FAIL")
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
    note("Figure 1", "'The extra Treasuries' (head): bought with the 2028 deposit",
         "In January 2028 the deposit's first dollars also buy extra face",
         "found" if "In January 2028 the deposit's first dollars also buy extra face" in s2 else "not found", "section 2",
         "PASS" if "In January 2028 the deposit's first dollars also buy extra face" in s2 else "FAIL")
    with open(WORDS_MD) as fh:
        words = fh.read()
    # Mon 16 Nov night: WORDS's row reads "the 2028 deposit's first dollars" since coherence reader 6's H1
    ok = "| the extra Treasuries |" in words and \
        "more Treasuries bought with the 2028 deposit's first dollars, right after the top-up" in words
    note("Figure 1", "'The extra Treasuries' is WORDS.md's name for that money", "the extra Treasuries", "found" if ok else "not found",
         "WORDS.md", "PASS" if ok else "FAIL")
    cmp("Figure 1", "Note: the ratio, dollars held for each $1 the payments need", float(FIGURE1_PER_DOLLAR[1:]),
        round(float(re.search(r"Funded ratio: \$[\d,]+ against \$[\d,]+, ([\d.]+)% funded", s8h).group(1)) / 100, 2),
        "8h", tol=0.0001)
    note("Figure 1", "Note: the ratio as WORDS.md words it", f"about {FIGURE1_PER_DOLLAR} for each $1",
         "found" if f"about {FIGURE1_PER_DOLLAR} for each $1" in words else "not found", "WORDS.md",
         "PASS" if f"about {FIGURE1_PER_DOLLAR} for each $1" in words else "FAIL")
    banned = ("backstop", "gift", "overflow", "paths", "forward rates", "interest earns nothing", "top-up pays")
    printed_f1 = " ".join([FIGURE1_HEADS["payment"], FIGURE1_HEADS["timeline"]] + list(FIGURE1_HEADS["c2"]) +
                          list(FIGURE1_HEADS["c3"]) + [FIGURE1_HEADS["sum"]] + list(FIGURE1_LEGEND) +
                          [FIGURE1_TITLE]).lower()
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
    # Mon 16 Nov (NUMBERS 9): the backstop at its value on 1 Jan 2033, not its cost carried; against 8h's own sentence,
    # 8h's composition total, the 8i forwards row and section 4
    m = re.search(r"cost carried to 1 Jan 2033 at forwards is \$([\d,]+); its value there is \$([\d,]+)", s8h1)
    cmp("Figure 1", "Note: the backstop is its value on 1 Jan 2033 (8h), not its cost carried",
        round(F["topup_comes_back_1jan2033"]), float(m.group(2).replace(",", "")) if m else None, "8h")
    cmp("Figure 1", "Note: the cost carried, kept apart and never printed", round(F["backstop_cost_carried_1jan2033"]),
        float(m.group(1).replace(",", "")) if m else None, "8h")
    m = re.search(r"\| \*\*Total \$[\d,]+\*\* \| \| \*\*\$[\d,]+\*\* \| \*\*\$([\d,]+)\*\* \|", s8h)
    cmp("Figure 1", "Note: the backstop = 8h composition's backstop column total", round(F["topup_comes_back_1jan2033"]),
        float(m.group(1).replace(",", "")) if m else None, "8h composition")
    r = [x for x in _table_rows(_section(md, "### 8i.", "\n### 8j."), "| World | Ten payments")
         if x[0].startswith("Today's forwards")][0]
    cmp("Figure 1", "Note: the backstop = 8i forwards row, left after 2042 in 1 Jan 2033 money",
        round(F["topup_comes_back_1jan2033"]), _money(r[9])[0], "8i")
    m = re.search(r"if it all waits in the ETF, worth \$([\d,]+) in 1 Jan 2033 money",
                  re.sub(r"\s+", " ", _section(md, "## 4. The plan from 2028", "\n## 5.")))
    cmp("Figure 1", "Note: the backstop = section 4's 1 Jan 2033 value", round(F["topup_comes_back_1jan2033"]),
        float(m.group(1).replace(",", "")) if m else None, "4")
    phrase = "money already received earns nothing while it waits"
    with open(WORDS_MD) as fh:            # read again: the wait-label loop above reuses the name `words`
        words_md = fh.read()
    ok = phrase in words_md and phrase in s8h1 and "every coupon and fund payout still counts" in words_md
    note("Figure 1", "Note: 'if cash waiting earns nothing' defined once", phrase, "WORDS.md and 8h", "WORDS, 8h",
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
    # ---- Table 2, Mon 16 Nov evening: the line of what is held the same, and the note's check against history ----
    # What is held the same: one run, one rule, one design for every row (the results file's stamp); the 2028 deposit
    # is $150,000 in each scenario world (completion + what is left for the floor and VT); the named replays use the
    # same plan (8i: "This is the plan under the escrow standard ... in five worlds").
    stamp = JOINT["stamp"]
    dep_ok = all(abs(JOINT["scenarios"][k]["completion_jan2028"] + JOINT["scenarios"][k]["left_for_floor_and_vt"]
                     - DEPOSIT_2028) < 0.01 for k in ("forwards", "minus3", "inflation"))
    rule_ok = stamp["design"] == "H_plain" and "haircut 0.5%" in stamp["rule"] and \
        "rounded down to $5,000" in stamp["rule"] and "fund fee charged from each trade day" in stamp["rule"] and \
        "0.15% fee" in stamp["rule"]
    same_ok = "This is the plan under the escrow standard" in s8i and "in five worlds" in s8i
    note("Table 2", "Held-the-same line: one plan, deposits, fees and range rule in every row",
         TABLE2_HELD_SAME, f"deposit $150,000 in each world: {dep_ok}; one rule stamp: {rule_ok}; 8i one plan: "
         f"{same_ok}", "8i; results stamp; NUMBERS 0", "PASS" if dep_ok and rule_ok and same_ok else "FAIL")
    note("Table 2", "Held-the-same line names deposits, steps, dates, fees and the range rule", TABLE2_HELD_SAME,
         "card Q14b row 20", "card Q14b", "PASS" if all(w in TABLE2_HELD_SAME for w in
                                                         ("deposits", "steps", "dates", "fees", "range rule"))
         else "FAIL")
    # The check against the 585 replays (ARGUMENT_LOG Mon 16 Nov Day 9; AHA_REGISTER reserve; card Q14b row 21)
    for key, name, v in TABLE2_WORLDS:
        note("Table 2", f"History check: {name} leaves less flexibility than the median replay",
             hundreds(v["flexibility"]), f"< {hundreds(TABLE2_FLEX_MEDIAN)}", "8i, 8j",
             "PASS" if v["flexibility"] < TABLE2_FLEX_MEDIAN else "FAIL")
    cmp("Table 2", "History check: the median replay's flexibility (8j joint replay)", round(TABLE2_FLEX_MEDIAN),
        fx[1], "8j")
    lo_b = min(v["bottom"] for _, _, v in TABLE2_WORLDS)
    hi_t = max(v["top"] for _, _, v in TABLE2_WORLDS)
    note("Table 2", "History check (for 3c, not printed): the lowest stated bottom is below the 1-in-20 low",
         dollars(lo_b), f"< {dollars(sb[0])}", "8i", "PASS" if lo_b < sb[0] else "FAIL")
    note("Table 2", "History check (for 3c, not printed): no named world's top reaches the 1-in-20 high",
         dollars(hi_t), f"< {dollars(st[2])}", "8i", "PASS" if hi_t < st[2] else "FAIL")
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
    cmp("Table 3", "Row 6 (store): bottom after a 2-point fall before Jan 2027", BOTTOM_AFTER_2PT_FALL,
        float(m.group(1).replace(",", "")) if m else None, "5")
    m = re.search(r"After a 1-point fall: \$([\d,]+), VT \$([\d,]+), floor payout \$[\d,]+, stated \$([\d,]+)", s5)
    cmp("Table 3", "Row 6: bottom after a 1-point fall before Jan 2027", BOTTOM_AFTER_1PT_FALL,
        float(m.group(3).replace(",", "")) if m else None, "5")
    note("Table 3", "Row 6: \"most\" still holds after a 1-point fall (floor money over half the deposit, VT bought)",
         f"floor {m.group(1) if m else None}, VT {m.group(2) if m else None}", "floor > $75,000, VT > $0", "5",
         "PASS" if m and float(m.group(1).replace(",", "")) > DEPOSIT_2028 / 2 and float(m.group(2).replace(",", "")) > 0
         else "FAIL")
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
    m = re.search(r"([\d.]+)% a year over the five years to September 2026", s8d)
    cmp("Table 3", "Row 7: building costs a year, five years to Sep 2026 (%)", 100 * CCI_5Y,
        float(m.group(1)) if m else None, "8d", tol=0.0001)
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
    # Sun 15 Nov evening (card Q3c row 8; NUMBERS 8h): IBTA's cash about 19 business days before year end; notices
    # in September to October
    with open(os.path.join(FR, "research", "cards", "Q3c_ended_ibond_funds_payouts.md")) as fh:
        q3c = re.sub(r"\s+", " ", fh.read())
    m = re.search(r"its cash came about (\d+) business days before year end", q3c)
    sep_ok = "September to October" in re.sub(r"\s+", " ", s8h)
    note("Table 3", "Row 4: IBTA's business days before year end; notices September to October",
         f"{IBTA_SLACK}; September to October", f"{m.group(1) if m else None}; "
         f"{'September to October' if sep_ok else None}", "card Q3c row 8, NUMBERS 8h",
         "PASS" if m and m.group(1) == IBTA_SLACK and sep_ok and "September to October" in
         " ".join(cell_text(c) for _, cells in TABLE3_ROWS for c in cells) else "FAIL")
    m = re.search(r"the 2033 payment is \$([\d,]+) short at forward rates", re.sub(r"\s+", " ", s5))
    cmp("Table 3", "Row 1: a missed deposit, the 2033 payment short", round(MISSED_SHORT_2033),
        float(m.group(1).replace(",", "")) if m else None, "5")
    # Mon 16 Nov night (coherence reader 6, M7; bond desk 4, L5): the ten short if cash waiting earns nothing
    m = re.search(r"the ten are \$([\d,]+) short at 0%", re.sub(r"\s+", " ", s5))
    cmp("Table 3", "Row 1: a missed deposit, the ten short if cash waiting earns nothing", round(MISSED_SHORT_ZERO),
        float(m.group(1).replace(",", "")) if m else None, "5")
    note("Table 3", "Row 1: the missed deposit's cost on both bases, never the $3,016 alone (NUMBERS 5)",
         f"{dollars(MISSED_SHORT_2033)}; {dollars(MISSED_SHORT_ZERO)}", "both printed", "5",
         "PASS" if f"{dollars(MISSED_SHORT_2033)} at today's rates, {dollars(MISSED_SHORT_ZERO)} if cash waiting earns "
         "nothing" in cell_text(TABLE3_ROWS[0][1][4]) else "FAIL")
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
            ("Row 5: the 2031 move", "the 2031 move", "row 5 adds the 2031 move"),
            ("Row 6: the scale", f"1 point; {dollars(BOTTOM_AFTER_1PT_FALL)}",
             "a 1-point fall in yields before January 2027 gives a stated bottom of $85,000"),
            ("Note: the bound", f"{FALL_TAKES_WHOLE_DEPOSIT:.2f}-point", "a 3.60-point fall takes the whole deposit"),
            ("Row 7: the test", f"{100 * TWD_TEST:.0f}% stronger", "row 7 tests a 10% stronger Taiwan dollar")):
        note("Table 3", what, mine, want, "SKELETON Exhibits item 4", "PASS" if want in sk4 else "FAIL")
    shut = (TRADE_DAYS[0] - _date(2027, 1, 1)).days == 3 and _date(2028, 1, 1).weekday() == 5 and \
        all(d.weekday() == 0 for d in TRADE_DAYS)
    note("Table 3", "Row 5: both trade days are the first market day of the year", "Mondays after a closed 1 January",
         "1 Jan 2027 holiday (Fri), 1 Jan 2028 Saturday", "calendar", "PASS" if shut else "FAIL")
    # Every figure printed in Table 3 is one checked above (a printed number with no check fails here)
    printed = " ".join(cell_text(c) for _, cells in TABLE3_ROWS for c in cells)
    allowed = {dollars(DEPOSIT_2028), dollars(TOPUP), dollars(TOPUP_TEN_LACK), dollars(TOPUP_NO_INTEREST),
               dollars(MISSED_SHORT_2033), dollars(MISSED_SHORT_ZERO),
               dollars(BOTTOM_AFTER_1PT_FALL), dollars(TWD_NEED), dollars(CONTRIBUTION_FWD), hundreds(FLEX_FWD)}
    found = set(re.findall(r"(?<![A-Z])\$[\d,]+", printed))   # NT$ and US$ mark an exchange rate, not a dollar figure
    # Mon 16 Nov night (bond desk 4, M7): the rate is printed as "NT$ per US$", 6 Nov 2026's level for scale only, and
    # the trigger at 8j's one reading of "10% stronger" (10% more US dollars: 32.768 / 1.10 = 29.79, 9.1% below)
    if "NT$" in printed:
        note("Table 3", "Row 7: the exchange rate as printed (for scale)", f"{TWD_PER_USD:.3f} on 6 Nov 2026",
             "32.768 (8d)", "8d", "PASS" if f"({TWD_PER_USD:.3f} on 6 Nov 2026, for scale)" in printed and
             "NT$ per US$ within" in printed else "FAIL")
    m = re.search(r"\(NT\$ per US\$ from ([\d.]+) to\s+([\d.]+) / 1\.10 = ([\d.]+)\)", s8j)
    cmp("Table 3", "Row 7: the trigger's level, NT$ per US$ for 10% more US dollars (8j)", round(TWD_STRONG, 2),
        float(m.group(3)) if m else None, "8j", tol=0.0001)
    cmp("Table 3", "Row 7: how far below its level (%), 1 - 29.79 / 32.768", round(100 * TWD_BAND, 1),
        round(100 * (1 - float(m.group(3)) / float(m.group(2))), 1) if m else None, "8j", tol=0.0001)
    note("Table 3", "Row 7: one reading of \"10% stronger\", 8j's (never NT$ per US$ down 10%, 29.49)",
         f"{TWD_STRONG:.2f}", "29.79 (8j)", "8j", "PASS" if f"({TWD_STRONG:.2f} from {TWD_PER_USD:.3f})" in printed and
         f"{100 * TWD_BAND:.1f}% below its level when the range is stated" in printed and
         f"{TWD_PER_USD * (1 - TWD_TEST):.2f}" not in printed else "FAIL")
    note("Table 3", "Every dollar figure printed is checked", ", ".join(sorted(found)), ", ".join(sorted(allowed)),
         "this check", "PASS" if found <= allowed else "FAIL")
    nums = set(re.findall(r"(?<![\w$,.])\d+(?:\.\d+)?%?", printed.replace("NT$", "NT ").replace("US$", "US ")))
    known = {"2028", "31", "2027", "4", "3", "17", "2037", "10", "14", "2031", "2033", "2", "1", "1.5%", "5.0%",
             "9", "6", "2036", IBTA_SLACK,
             f"{FALL_TAKES_WHOLE_DEPOSIT:.2f}", f"{TWD_PER_USD:.3f}", "10%", "2026", f"{100 * CCI_5Y:.2f}%", "0.5%",
             f"{100 * TWD_BAND:.1f}%", f"{TWD_STRONG:.2f}", f"{100 * FUND_FEE:.2f}%"}   # Mon 16 Nov night: row 7, row 4
    ok = "less 0.5%" in md and "from its 0.5%" in printed      # row 4: the floor's swap from the range rule's 0.5% cut
    note("Table 3", "Row 4: the floor's 0.5% margin is the range rule's cut (NUMBERS 4: each end less 0.5%)",
         "0.5% margin", "less 0.5%" if "less 0.5%" in md else None, "4", "PASS" if ok else "FAIL")
    # Sat 14 Nov (bond reader 2): row 4 watches the bill fund's fee (NUMBERS 0: 0.15% a year, its fund UNVERIFIED) and
    # swaps into a Treasury maturing by 15 December (the iBonds' end, 15 December, card Q36)
    fee_ok = "0.15% a year" in md and abs(WAIT_FEE - 0.0015) < 1e-12
    note("Table 3", "Row 4: the short-term Treasury ETF's fee is the register's", f"{100 * WAIT_FEE:.2f}%",
         "0.15% a year" if fee_ok else None, "0", "PASS" if fee_ok and f"{100 * WAIT_FEE:.2f}%" in printed else "FAIL")
    # Mon 16 Nov night (bond desk 4, M5): the iBond funds' fee beside it (NUMBERS 0: "0.07% fee")
    s0 = _section(md, "## 0.", "\n## 1.")
    ok7 = f"{100 * FUND_FEE:.2f}% fee" in s0
    note("Table 3", "Row 4: the iBond funds' fee is the register's", f"{100 * FUND_FEE:.2f}%",
         f"{100 * FUND_FEE:.2f}% fee" if ok7 else None, "0", "PASS" if ok7 and f"{100 * FUND_FEE:.2f}%" in printed
         else "FAIL")
    # Mon 16 Nov night (bond desk 4, M4; coherence reader 6, L17): no "Treasury due by 15 December" for a fund's swap,
    # since WInS lists no individual Treasury maturing in 2033 or 2035 (WN l.20, l.22); the swap names the class, an
    # earlier iBond fund or the short-term Treasury ETF; early cash waits in that ETF
    with open(WN_TXT) as fh:
        wn = fh.read()
    wn_ok = "no individual Treasury maturing in 2033" in wn and "no individual Treasury maturing in 2035" in wn
    swap_ok = "Treasury due by" not in printed and "sold for an earlier iBond fund or that ETF" in printed and \
        "early cash waits in the short-term Treasury ETF" in printed
    note("Table 3", "Row 4: a fund's swap names the class, never an individual Treasury (WInS lists none for 2033, 2035)",
         "an earlier iBond fund or that ETF", "WN l.20, l.22" if wn_ok else None, "WN; card Q36",
         "PASS" if wn_ok and swap_ok else "FAIL")
    # Mon 16 Nov night (coherence reader 6, L1): the waiting fund's frozen name (TNA l.5, WN l.17)
    with open(TNA_TXT) as fh:
        tna = fh.read()
    name_ok = "short-term Treasury ETF" in tna and "short-term Treasury ETF" in wn and \
        "iBond and short-term Treasury ETF notices" in printed and "bill fund" not in printed and \
        "Treasury-bill" not in printed
    note("Table 3", "Row 4: the waiting fund's name is the frozen notes' (TNA l.5, WN l.17)", "short-term Treasury ETF",
         "found in TNA and WN" if name_ok else None, "TNA; WN", "PASS" if name_ok else "FAIL")
    note("Table 3", "Row 4: a dated missing-notice trigger at the end of the notice window (September to October)",
         NOTICE_BY, "September to October (8h)", "8h; bond desk 4, M5",
         "PASS" if sep_ok and NOTICE_BY == "31 October" and f"no ending notice by {NOTICE_BY} of the final year"
         in printed else "FAIL")
    known |= {"0.15%", "15"}
    note("Table 3", "Every other number printed is a checked date or figure", ", ".join(sorted(nums - known)) or "none",
         "dates and figures above", "this check", "PASS" if nums <= known else "FAIL")

    banned3 = ("backstop", "gift", "overflow", "paths", "forward rates", "half kept", "kept half", "moved half", "rung",
               "completion", "model", "cap ", "capped", "excess", "stated ends", "escrow", "reserve",
               "interest earns nothing")
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
