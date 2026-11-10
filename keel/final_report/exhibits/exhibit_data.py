"""Data for the Final Report exhibits, on the register of Tue 10 Nov 2026 (rebuilt Wed 11 Nov 2026, Sydney).

Design H_plain ("sufficient without reinvestment", with the fee cushion), the Treasury curve of Fri 6 Nov 2026, the
range rule on the fund's holdings and Keel's reading of "most". Everything modelled is MODEL (NUMBERS.md stamp).

Where the figures come from:
  Table 1  (Section 2)      NUMBERS.md 8g version 2, the WInS record at cost. No results file holds it, so the rows are
                            copied here by hand and check() compares every cell with the 8g table.
  Figure 1 (3a)             numbers/results_reserve_2026-11-10.json (NUMBERS 8h): blocks composition_1jan2033_base,
                            base (today's forwards), fee (nothing earns interest and waiting money pays the ETF's fee:
                            Keel's standard, SKELETON Exhibits item 2) and zero (nothing earns interest, no fee).
  Table 2  (3b, 3c)         numbers/results_joint_stress_2026-11-10.json (NUMBERS 8i, 8j): scenarios forwards, minus3
                            and inflation; joint.named 2006-06 and 2007-07; the 585-window percentiles; and
                            twd_test.joint_replay for the contribution and the flexibility across windows.
  Cross-check (8k)          numbers/results_returns_2026-11-10.json: the flexibility at forwards by a second route.

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
REGISTER_DATE = "2026-11-10"


def _load(name):
    with open(os.path.join(NUMBERS_DIR, name)) as fh:
        return json.load(fh)


RESERVE = _load(f"results_reserve_{REGISTER_DATE}.json")
JOINT = _load(f"results_joint_stress_{REGISTER_DATE}.json")
RETURNS = _load(f"results_returns_{REGISTER_DATE}.json")

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
# 8g's costs-row name needs 3.22 in at 12 pt; the column has 3.13 in. Printed short, same meaning (coordinator,
# Wed 11 Nov): the $200 of commissions and the $1,109.42 of bond interest accrued at purchase.
NAME_PRINT = {"Commissions and bond interest paid at purchase": "Commissions and accrued interest at purchase"}
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


def table1_rows():
    """Table 1 as printed: list of (kind, cells). kind is 'row', 'subtotal' or 'total'; cells are Wharton's five
    columns plus "Pays for". Amounts in cents as WInS records them; percentages to two decimals (8g's largest
    remainder)."""
    out = []
    for i, (ident, name, typ, amt, pct, role) in enumerate(HOLDINGS):
        out.append(("row", [ID_PRINT.get(ident, ident), NAME_PRINT.get(name, name), TYPE_PRINT[typ], cents_plain(amt),
                            f"{pct:.2f}", pays_for(role)]))
        if i == N_TREASURIES - 1:
            sa, sp = treasury_subtotal()
            out.append(("subtotal", ["", SUBTOTAL_LABEL, "", cents_plain(sa), f"{sp:.2f}", ""]))
    out.append(("total", ["Total", "", "", cents_plain(HOLDINGS_TOTAL[0]), f"{HOLDINGS_TOTAL[1]:.2f}", ""]))
    return out


def treasury_subtotal():
    a = round(sum(h[3] for h in HOLDINGS[:N_TREASURIES]), 2)
    p = round(sum(h[4] for h in HOLDINGS[:N_TREASURIES]), 2)
    return a, p


TABLE1_HEADER = ["Ticker or identifier", "Name of investment", "Asset type", "Amount ($)", "% of total",  # "portfolio"
                 "Pays for"]                                                                          # needs 0.58 in


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
        rows.append({                                                       # it pays out on 15 Dec 2032
            "year": year,
            "holding": _short_holding(c["holding"]),
            "kind": kind,
            "pays_out": c["pays_out"],
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
}


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
            note("Table 1", f"{name}: printed as", NAME_PRINT[name], name, "8g (coordinator's short label, Wed 11 Nov)",
                 "PASS" if amt == 1309.42 and pct == 0.44 else "FAIL")
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
    note("Figure 1", "Printed rows foot to (own / backstop)", f"{dollars(foot_own)} / {dollars(foot_bk)}",
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
    note("Figure 1", "'Bought with the 2028 deposit' (head)", "In January 2028 the deposit's first dollars also buy extra face",
         "found" if "In January 2028 the deposit's first dollars also buy extra face" in s2 else "not found", "section 2",
         "PASS" if "In January 2028 the deposit's first dollars also buy extra face" in s2 else "FAIL")
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
    print("\nFigure 1 (NUMBERS 8h, MODEL): year | paid from | cash arrives | at forwards | nothing earns after fee: own + backstop")
    for f in FIGURE1_ROWS:
        print(f"  {f['year']} | {f['holding']:<16} | {f['pays_out']} ({f['wait_words'] or str(f['months_model']) + ' mo'}) |"
              f" {dollars(f['at_forwards'])} | {dollars(f['own_if_nothing_earns'])} + {dollars(f['backstop_if_nothing_earns'])}")
    T = FIGURE1_TOTALS
    print(f"  Total {dollars(T['at_forwards'])} | {dollars(T['own_if_nothing_earns'])} + {dollars(T['backstop_if_nothing_earns'])}")
    print("\nTable 2 (NUMBERS 8i, 8j, MODEL)")
    for _, name, v in TABLE2_WORLDS:
        print(f"  {name:<36}", " | ".join(table2_cells(v)))
    print(f"  {TABLE2_SPREAD_LABEL}")
    for label, v in TABLE2_SPREAD:
        print(f"  {label:<36}", " | ".join(table2_cells(v)))
    print()
    fails, _ = check()
    sys.exit(1 if fails else 0)
