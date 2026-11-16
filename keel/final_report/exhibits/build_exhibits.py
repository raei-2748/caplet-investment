"""Build the Final Report's four exhibits on the register of Tue 10 Nov 2026 (rebuilt Fri 13 Nov 2026 morning, Sydney;
re-built Mon 16 Nov 2026 on the Sun 15 Nov evening results files, NUMBERS 9; Mon 16 Nov evening: card Q73's three
Figure 1 fixes and Table 2's held-the-same line and history check, REBUILD_2026-11-16_evening.md; Mon 16 Nov night:
that night's hand edits to tables.md (coherence reader 6; bond desk 4) carried in, here and in exhibit_data.py, and an
exhibit too tall for one Letter page measured on a tall page and previewed whole, with a warning).

    python3 -I keel/final_report/exhibits/build_exhibits.py            everything below (about a minute)
    python3 -I keel/final_report/exhibits/build_exhibits.py figure     Figure 1 only

Every figure comes from exhibit_data.py, which reads the results files in ../numbers/ and checks each figure against
NUMBERS.md; this script stops if that check fails, or if any exhibit text (title, head, cell or note item) carries a
word never printed there (words_check: the conceit's words, "endowment", "optimal", "natural hedge", "fail-safe",
"fixed", "89%"). Writes, next to this file:

  figure1_reserve.svg          Figure 1 (text kept as text; Times New Roman, then Liberation Serif)
  figure1_reserve_2x.png       Figure 1 preview at 2x (192 dpi at its printed width of 6.5 in)
  exhibit2_reserve.png         Figure 1 at 300 dpi, the file ../template/build_template.py places (its old name)
  table1_holdings_2x.png       Table 1 preview at 2x, cropped from the Wharton-format PDF
  table2_markets_2x.png        Table 2 preview at 2x, cropped from the same PDF
  table3_monitoring_2x.png     Table 3 preview at 2x, cropped from the same PDF
  exhibits_letter.docx / .pdf  the four exhibits as APA blocks on Letter in Wharton's format; each note shows the
                               items it must carry (notes are written on 27 Nov, not here)
  tables.md                    every exhibit as Markdown text, with its source and note items
  measurements.json            each exhibit's height in double-spaced lines on a Letter page (card Q23's method), and
                               (Thu 12 Nov evening) "s2_fit": the most prose Section 2 holds in Wharton's three pages
                               beside Table 1, against SKELETON's 580-word budget

Format (Wharton; card Q23): 12-point Times New Roman, double-spaced text, 1-inch margins, Letter; tables single-spaced
(Wharton: "Tables and graphics may be single-spaced when needed for readability"); APA 7 number, title, note. Black and
white, two greys at most. Liberation Serif has Times New Roman's character widths, so sizes and line breaks hold.
"""
import json
import os
import shutil
import sys
import tempfile
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.normpath(os.path.join(HERE, "..", "template"))
sys.dont_write_bytecode = True     # leave no __pycache__ here or in ../template (another owner's folder)
sys.path.insert(0, HERE)
import exhibit_data as D  # noqa: E402

# ---- print style: black, two greys, hairline rules (dataviz skill: two categories, two well-separated greys) ----
INK = "#000000"
FUND = "#c8c8c8"      # iBond Treasury ETF: light grey, black text on it
BOND = "#505050"      # Treasury bond: dark grey, white text on it
RULE = "#9a9a9a"      # hairline year grid
PREVIEW_DPI = 192     # "2x": twice a 96-dpi screen at the printed size
PRINT_DPI = 300


def pick_font():
    names = {f.name for f in font_manager.fontManager.ttflist}
    for n in ("Times New Roman", "Liberation Serif", "Tinos"):
        if n in names:
            return n
    return "serif"


FONT = pick_font()
plt.rcParams.update({"font.family": FONT, "svg.fonttype": "none", "pdf.fonttype": 42})


def yearfrac(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    start = date(y, 1, 1)
    return y + (date(y, m, d) - start).days / (date(y + 1, 1, 1) - start).days


# =================================================================================================================
# Figure 1: the escrow verifier's sufficiency schedule beside a staircase (card Q28, section (c))
# =================================================================================================================
# Geometry in inches (the figure is drawn on one axes in inch units, y downwards). Thu 12 Nov: no axis break (lay
# reader, Wed 11 Nov: "the axis break marks are odd"); the time scale runs unbroken from January 2027, so every bar's
# length is its real holding time.
# Mon 16 Nov evening (card Q73's three fixes): one world, so the "At today's market rates" column ($50,000 ten times)
# goes to the note; the heads print the sum, "Its own Treasury + Extra Treasuries = $50,000", and the total row adds
# up, "$444,080 + $55,920 = $500,000"; the question head goes (the title now opens with the condition), so the head is
# two lines, not four, and the figure 0.37 in shorter (3.56 -> 3.19 in).
W, H = 6.5, 3.19
X_YEAR = 0.0                       # payment year, left-aligned
AX_L, AX_R = 0.62, 3.70            # the timeline
SUM_R = 6.50                       # right edge of the sum ("= $50,000" head; "$500,000" in the total row)
OP_GAP = 0.09                      # space either side of the "+" and "=" signs
T0, T1 = 2027.0, 2042.10           # 1 January 2027 at the left edge; the last payment, 1 January 2042, near the right
YEAR_LABELS = (2027, 2030, 2033, 2036, 2039, 2042)
HEAD_RULE = 0.42
ROW0, ROW_H, BAR_H = 0.46, 0.222, 0.15
FS_NUM, FS_LAB, FS_HEAD = 10.5, 10, 10.5
LINE = 0.17                        # one head line at 10.5 pt


def X(t):
    return AX_L + (t - T0) / (T1 - T0) * (AX_R - AX_L)


def row_y(i):
    return ROW0 + (i + 0.5) * ROW_H


def figure1(outputs):
    """outputs: list of (path, dpi); an .svg path ignores dpi."""
    rows = D.FIGURE1_ROWS
    hd = D.FIGURE1_HEADS
    n = len(rows)
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")

    def text(x, y, s, ha="left", va="center", size=FS_NUM, weight="normal", color=INK, **kw):
        return ax.text(x, y, s, ha=ha, va=va, fontsize=size, fontweight=weight, color=color, **kw)

    def width(s, size=FS_NUM, weight="normal"):
        t = ax.text(0, 0, s, fontsize=size, fontweight=weight)
        fig.canvas.draw()
        w = t.get_window_extent().transformed(ax.transData.inverted()).width
        t.remove()
        return w

    # ---- the sum's columns, laid out from the right edge by the widest text in each (Mon 16 Nov evening) ----
    own_tot, extra_tot, sum_tot = (D.dollars(v) for v in D.FIGURE1_TOTAL_ROW)
    w_sum = max(width(hd["sum"], FS_HEAD, "bold"), width(sum_tot))
    w_op = max(width(hd["plus"], FS_HEAD, "bold"), width(hd["equals"], FS_HEAD, "bold"))
    w_b = max(width(hd["c3"][0], FS_HEAD, "bold"), width(hd["c3"][1], FS_HEAD, "bold"), width(extra_tot))
    w_a = max(width(hd["c2"][0], FS_HEAD, "bold"), width(hd["c2"][1], FS_HEAD, "bold"), width(own_tot))
    X_EQ = SUM_R - w_sum - OP_GAP - w_op / 2            # centre of "="
    C3_R = X_EQ - w_op / 2 - OP_GAP                     # right edge of "Extra Treasuries"
    X_PLUS = C3_R - w_b - OP_GAP - w_op / 2             # centre of "+"
    C2_R = X_PLUS - w_op / 2 - OP_GAP                   # right edge of "Its own Treasury"
    C2_L = C2_R - w_a                                   # left edge of that column (the wait labels must clear it)

    # ---- column heads: two lines; the lower (L4) sits on the head rule ----
    L4 = HEAD_RULE - 0.06
    L3 = L4 - LINE
    text(X_YEAR, L4, hd["payment"], va="bottom", weight="bold", size=FS_HEAD)
    text((AX_L + AX_R) / 2, L3, hd["timeline"], ha="center", va="bottom", weight="bold", size=FS_HEAD)
    for yr in YEAR_LABELS:
        text(X(yr), L4, str(yr), ha="left" if yr == T0 else "center", va="bottom", size=FS_LAB)
    # the sum in the heads: "Its own Treasury + Extra Treasuries = $50,000" (card Q73-010, -036)
    for x_r, (a, b) in ((C2_R, hd["c2"]), (C3_R, hd["c3"])):
        text(x_r, L3, a, ha="right", va="bottom", weight="bold", size=FS_HEAD)
        text(x_r, L4, b, ha="right", va="bottom", weight="bold", size=FS_HEAD)
    text(X_PLUS, L4, hd["plus"], ha="center", va="bottom", weight="bold", size=FS_HEAD)
    text(X_EQ, L4, hd["equals"], ha="center", va="bottom", weight="bold", size=FS_HEAD)
    text(SUM_R, L4, hd["sum"], ha="right", va="bottom", weight="bold", size=FS_HEAD)
    ax.plot([0, W], [HEAD_RULE, HEAD_RULE], color=INK, linewidth=0.6)

    # ---- year grid behind the bars (the bars hide it before each one's cash arrives) ----
    last = ROW0 + n * ROW_H
    for yr in range(int(T0) + 1, 2043):
        ax.plot([X(yr), X(yr)], [HEAD_RULE, last], color=RULE, linewidth=0.35, zorder=0)

    # ---- one row per payment ----
    for i, r in enumerate(rows):
        y = row_y(i)
        end = yearfrac(r["cash_last"])     # Fri 13 Nov: when the cash reaches Laura, not the fund's end date (8h)
        bond = r["kind"] == "T-bond"
        ax.add_patch(Rectangle((X(T0), y - BAR_H / 2), X(end) - X(T0), BAR_H, facecolor=BOND if bond else FUND,
                               edgecolor=INK, linewidth=0.5, zorder=2))
        text(X(T0) + 0.07, y, r["holding"], size=FS_LAB, color="white" if bond else INK, zorder=5)
        # the payment: a black tick on 1 January
        ax.plot([X(r["year"]), X(r["year"])], [y - 0.095, y + 0.095], color=INK, linewidth=2.0,
                solid_capstyle="butt", zorder=4)
        if r["wait_words"]:   # the long waits, in the Trading Notes' months; the legend says what the dots are
            ax.plot([X(end), X(r["year"])], [y, y], color=INK, linewidth=0.7, linestyle=(0, (1.2, 1.4)), zorder=3)
            lab = text(X(r["year"]) + 0.05, y, f"waits {r['wait_words']}", size=FS_LAB, zorder=5,
                       bbox=dict(facecolor="white", edgecolor="none", pad=0.4))
            fig.canvas.draw()
            right = lab.get_window_extent().transformed(ax.transData.inverted()).x1
            num_l = C2_R - width(D.dollars(r["own_if_nothing_earns"]))
            assert right + 0.04 <= num_l, f"'waits {r['wait_words']}' runs into the number column"
        text(X_YEAR, y, str(r["year"]))
        # one world (card Q73-035): only what pays each $50,000 if cash waiting earns nothing, after the 0.15% fee
        text(C2_R, y, D.dollars(r["own_if_nothing_earns"]), ha="right")
        text(C3_R, y, D.dollars(r["backstop_if_nothing_earns"]), ha="right")

    # ---- totals: 8h's totals of unrounded figures, which add up exactly, "$444,080 + $55,920 = $500,000" ----
    ax.plot([0, W], [last + 0.03, last + 0.03], color=INK, linewidth=0.6)
    yt = last + 0.03 + ROW_H / 2 + 0.01
    text(X_YEAR, yt, "Total")
    text(C2_R, yt, own_tot, ha="right")
    text(X_PLUS, yt, hd["plus"], ha="center")
    text(C3_R, yt, extra_tot, ha="right")
    text(X_EQ, yt, hd["equals"], ha="center")
    text(SUM_R, yt, sum_tot, ha="right")

    # ---- legend inside the figure (APA), one row ----
    yl = H - 0.12
    x = 0.0
    for kind, label in zip(("fund", "bond", "tick", "wait"), D.FIGURE1_LEGEND):
        if kind == "tick":
            ax.plot([x + 0.07, x + 0.07], [yl - 0.08, yl + 0.08], color=INK, linewidth=2.0, solid_capstyle="butt")
            lx = x + 0.2
        elif kind == "wait":
            ax.plot([x, x + 0.3], [yl, yl], color=INK, linewidth=0.7, linestyle=(0, (1.2, 1.4)))
            lx = x + 0.38
        else:
            ax.add_patch(Rectangle((x, yl - BAR_H / 2), 0.28, BAR_H, facecolor=FUND if kind == "fund" else BOND,
                                   edgecolor=INK, linewidth=0.5))
            lx = x + 0.36
        t = ax.text(lx, yl, label, ha="left", va="center", fontsize=FS_LAB)
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        x = bb.x1 + 0.28
    assert x - 0.28 <= W + 0.001, "legend wider than the figure"

    for path, dpi in outputs:
        if path.endswith(".svg"):
            fig.savefig(path, facecolor="white")
            _svg_font_fallback(path)
        else:
            fig.savefig(path, dpi=dpi, facecolor="white")
    plt.close(fig)
    return [p for p, _ in outputs]


def _svg_font_fallback(path):
    with open(path) as fh:
        s = fh.read()
    s = s.replace(f"font-family: '{FONT}'", "font-family: 'Times New Roman', 'Liberation Serif', serif")
    s = s.replace(f"font-family:'{FONT}'", "font-family:'Times New Roman','Liberation Serif',serif")
    with open(path, "w") as fh:
        fh.write(s)


# =================================================================================================================
# Labels and note items (working labels; the notes are written on 27 Nov from these items, not here)
# =================================================================================================================
EXHIBITS = {
    # Every title says the exhibit's scale (fresh reader and coordinator, Wed 11 Nov): Table 1 is the WInS book on the
    # original $300,000 (8g: "Laura's whole plan in miniature"); Figure 1 and Table 2 are her plan for both deposits.
    "t1": {"label": "Table 1",
           "title": "The Final WInS Portfolio at Cost on the Original $300,000",
           # Sat 14 Nov (coherence reader 4): "in Miniature" claimed a faithful reduction (no top-up, no extra
           # Treasuries; VT 8.84% against the plan's 6.63%); the scale stays in the WInS notes' "scaled to the model
           # portfolio", said in 2.0 and 2.1
           # Thu 12 Nov evening: 75 words (was 50). The units column needs its basis (targets set before the first
           # trade; a bond unit is $1,000 of face value) and SKELETON's density cut sends 2.5's two other targets
           # here (bonds within 25 basis points; cash never below $1,000). The costs label now says what the row is,
           # so its item shrinks to the coupon clause; "the full-size plan is Figure 1 and Table 2" goes (the title
           # carries the scale; 2.0 and 2.1 name the plan).
           "section": "Section 2 (2-3 pages)", "note_budget_words": 75,
           "note_items": [
               "amounts at cost: units held x price paid on 6-7 Oct 2026 (U.S. Eastern), on the original $300,000 (8g)",
               "units bought / target: targets set before the first trade (Portfolio tab, 2 Oct prices); a bond "
               "unit is $1,000 of face value (8m)",
               "the other two targets, met: every bond bought within 25 basis points of the Treasury curve; cash "
               "never below $1,000 (8m; 2.5)",
               # Mon 16 Nov night (coherence reader 6, L3): the floor is the fund, the bottom is the figure (WORDS)
               "Pays for: each holding's payment (1 January; 23 Oct snapshot); the floor: the late-2032 Treasury fund "
               "whose payout sets the least Laura can promise in 2031 (TNA l.13), here IBTM's floor lot (CANON A24, "
               "8g) (coherence reader 6, Mon 16 Nov, L3: the floor is the fund, the bottom is the figure, WORDS)",
               "costs row: $200 of fees and $1,109.42 of accrued bond interest, repaid with each bond's next coupon "
               "(8g v2)",
               "identifiers: tickers for funds, CUSIPs for bonds (8g, card Q38); VT bought last, with the cash left "
               "(8m)"]},
    "f1": {"label": "Figure 1",
           # Fri 13 Nov evening: WORDS.md's names ("the extra Treasuries", "cash waiting earns nothing"; the top-up is
           # the $2,388 that completes the ten, IPS l.13). Mon 16 Nov evening (card Q73-016, -037): the condition first,
           # then the verdict, then the scale; the title lives in exhibit_data so its check can read it
           "title": D.FIGURE1_TITLE,
           # Fri 13 Nov (bond reader, 12 Nov): the definition and the reconciliation join, in priority order.
           # Mon 16 Nov evening (card Q73's three fixes): one world in the figure, so today's market rates move here
           # (item 4: each own Treasury pays its whole $50,000, what comes back, and the ratio, merged); the rounding
           # clause is required (item 3), since the total row prints 8h's totals and the rows foot a dollar off. In a
           # terse note items 1-5 run 17 words longer than Fri 13 Nov's items 1-4 (114 against 97, counted), so the
           # budget is 77 (was 60); item 6 only if room, else 3a's prose (the bars show the cash dates)
           "section": "Section 3, part 3a", "note_budget_words": 77,
           "note_items": [
               # Mon 16 Nov night (coherence reader 6, M9; WORDS "The standard the payments meet"): the funds' basis
               "1. \"if cash waiting earns nothing\" (the title's condition), defined once: money already received "
               "earns nothing while it waits; every coupon and fund payout still counts (WORDS; 8h); fund rows: what "
               f"each fund's bonds pay less its {100 * D.FUND_FEE:.2f}% fee, its net asset value, not a fixed sum "
               "(coherence reader 6, Mon 16 Nov, M9)",
               # Mon 16 Nov (NUMBERS 9): every figure read from exhibit_data, the backstop at its VALUE on 1 Jan 2033
               # ($45,456, to the nearest $100), never its cost carried ($45,487)
               f"2. the extra Treasuries' column reconciled: their "
               f"{D.dollars(D.FIGURE1_NOTE_FACTS['topup_for_no_interest_jan2028'])} (January 2028) buys "
               f"{D.dollars(D.FIGURE1_NOTE_FACTS['topup_face_and_fund_dollars'])} at face; "
               f"with {D.dollars(D.FIGURE1_NOTE_FACTS['topup_interest_undiscounted'])} of their own interest, summed "
               f"undiscounted, they pay {D.dollars(D.FIGURE1_TOTALS['backstop_if_nothing_earns'])} after "
               f"{D.dollars(D.FIGURE1_NOTE_FACTS['topup_fee_while_waiting'])} of the waiting fund's 0.15% fee (8h)",
               f"3. rounding (required since Mon 16 Nov evening): rows are rounded to the dollar and add to "
               f"{D.dollars(D.FIGURE1_FOOT[0])} and {D.dollars(D.FIGURE1_FOOT[1])}; the total row is 8h's totals "
               f"of unrounded figures, {D.dollars(D.FIGURE1_TOTAL_ROW[0])} + {D.dollars(D.FIGURE1_TOTAL_ROW[1])} = "
               f"{D.dollars(D.FIGURE1_TOTAL_ROW[2])} (8h)",
               f"4. the other basis, today's market rates (one world in the figure, card Q73-035): each own Treasury "
               f"pays its whole {D.dollars(D.FIGURE1_PAYMENT)} and about "
               f"{D.hundreds(D.FIGURE1_NOTE_FACTS['topup_comes_back_1jan2033'])} of the extra Treasuries comes back "
               f"(1 Jan 2033 money): about {D.FIGURE1_PER_DOLLAR} for each $1 the payments need on 1 Jan 2033, because "
               "the extra Treasuries are sized for cash waiting earning nothing (8h; card Q31)",
               "5. Treasury par curve of 6 Nov 2026; each payment in its own year's dollars (8h)",
               "6. if room: bars end when the cash reaches Laura (a fund a few days after its 15 December end, a bond "
               "on its maturity date or the next business day; 8h cash table); paid in every historical rate stretch "
               "tested (585 starts, 1962-2010; NUMBERS 2); the top-up, $2,388, completes the ten, in \"Its own "
               "Treasury\"; the floor's IBTM shares are a separate lot from the 2033 payment's"]},
    "t2": {"label": "Table 2",
           "title": "Laura's Plan for Both Deposits ($450,000) in Five Markets and in History Since 1962, Modelled",
           # Sun 15 Nov evening (bond desk 3c check, research/panel/2026-11-15_bond_desk_3c_precision.md): M2, the
           # basis of each end, as Laura measures it on the day (NUMBERS 0); M5, each column's own date (the old last
           # item dated every column to January 2028; only the bottom is); M6, "before the 2031 meetings" (IPS l.15)
           # with the modelled trade days. The required items need about 95 words in a terse note (counted Sun 15 Nov
           # evening), so the budget is 95 (was 45).
           # Mon 16 Nov evening (card Q14b rows 20-21; ARGUMENT_LOG Day 9): the line of what is held the same is a row
           # of the table (D.TABLE2_HELD_SAME), not the note; the note gains one sentence checking the five worlds
           # against the 585 replays (9 words in a terse note: "Each named world's flexibility is below the median
           # replay's"), paid for by the range-rule item's "modelled on the 6 Nov 2026 curve until then" (9 words),
           # which the first item already says, so the budget stays 95. "the fee" is now "the fees" (NUMBERS 0 has
           # two: the fund's and the waiting ETF's 0.15%; morning observation 2). M7's dates item, "if room", is
           # cut, as SKELETON's page arithmetic names it first: Figure 1 carries the cash dates, and the sequence stays
           # in the store and 3a's prose.
           "section": "Section 3, parts 3b and 3c", "note_budget_words": 95,
           "note_items": [
               "MODEL, not forecasts; Treasury curve of 6 Nov 2026",
               "each end (the range rule): units of the fund held x its remaining coupons and principal per unit, "
               "from its published holdings on the trade day, undiscounted, less the fees to 15 Dec 2032 and 0.5%; "
               # Mon 16 Nov night (coherence reader 6, L2): WORDS bans "moved half" and names the history "every
               # starting month since 1962"
               "the bottom rounded down to $5,000; the top = the unrounded bottom plus that of the shares moved into "
               "Treasuries, rounded down once (NUMBERS 0, 3; coherence reader 6, Mon 16 Nov, L2: never \"the moved "
               "half's\")",
               "shares 7.5% a year in rows 1 and 3",
               "starting months: U.S. yields and stocks from the start month (method in 3e)",
               "inflation row: prices up 5% a year",
               "flexibility: the half of VT promised to no one plus whatever the funds pay above the stated top, to "
               "the nearest $100 (8i)",
               "spread rows: each column's own percentile",
               "each column's own date: the bottom turns on markets to January 2028 (traded Mon 3 Jan 2028), the top "
               "on markets to the move before the 2031 meetings (traded Thu 2 Jan 2031), her flexibility on markets "
               "to January 2033 (NUMBERS 4; IPS l.15)",
               f"checked against history: each named world's flexibility ({D.hundreds(D.TABLE2_FLEX_WORLDS[0])} to "
               f"{D.hundreds(D.TABLE2_FLEX_WORLDS[1])}) is below the median starting month's "
               f"({D.hundreds(D.TABLE2_FLEX_MEDIAN)}) (8i, 8j)"]},
    "t3": {"label": "Table 3",
           # Thu 12 Nov (SKELETON Exhibits item 4): seven rows in three levels, five columns, one trigger per cell.
           # Fri 13 Nov evening: rows rewritten for three readers and card Q36, refitted to one page (18.4 lines without
           # the note, 21.4 with 40 words; was 18.9 and 21.9 with 35)
           "title": "Seven Signals to Watch as 2031 and 2033 Approach; Two Can Change Laura's $450,000 Plan",
           "section": "Section 3, part 3e", "note_budget_words": 40,
           "note_items": [
               f"{D.dollars(D.TOPUP)}: January 2028 money at today's rates, the top-up ({D.dollars(D.TOPUP_TEN_LACK)}) "
               f"and the extra Treasuries ({D.dollars(D.TOPUP_NO_INTEREST)})",
               "X-date: when the debt limit stops the Treasury paying every bill (its estimate, else the "
               "Congressional Budget Office's)",
               "cash dates: fund payouts, maturities, trade days",
               # Mon 16 Nov night (bond desk 4, L10): the 3.60 points are the standard's, with cash waiting earning
               # nothing (NUMBERS 5; the ladder alone holds to 3.89 points)
               f"payments hold, even if cash waiting earns nothing, to a {D.FALL_TAKES_WHOLE_DEPOSIT:.2f}-point fall "
               "before 2027"]},
}


# =================================================================================================================
# The tables as Word tables (APA 7), built with the template's own helpers (../template/build_template.py)
# =================================================================================================================
def _template():
    sys.path.insert(0, TEMPLATE)
    import build_template as BT
    return BT


def _lr_margins(cell, left, right):
    """Set a cell's left and right padding (twips) after BT._cell_margins has written both."""
    from docx.oxml.ns import qn
    mar = cell._tc.get_or_add_tcPr().find(qn("w:tcMar"))
    for side, tw in (("left", left), ("right", right)):
        mar.find(qn(f"w:{side}")).set(qn("w:w"), str(tw))


PAD = 58          # twips each side between columns
OUTER = 0         # no padding at the table's outer edges: text sits flush with the ends of the rules (buys 0.08 in)


def _pad(cell, c_first, c_last, n_cols):
    from_left = PAD if c_first > 0 else OUTER
    from_right = PAD if c_last < n_cols - 1 else OUTER
    _lr_margins(cell, from_left, from_right)


LABEL_KINDS = ("subtotal", "holdings", "costs")


def apa_table(BT, rep, ex, header, rows, widths, aligns, note_text, top=False, spanners=None, row_gap=0,
              label_span=0, label_indent=None):
    """rows: list of (kind, cells); kind is row, subtotal, holdings (a second subtotal), costs (money that is not a
    holding), total, spanner (one italic cell across the table, a rule above), indent (a stub indented under a
    spanner), result (one plain cell across the table, a rule above: a finding that holds for every row) or held (one
    plain cell across the table right under the heads, a thin rule below: what is held the same in every row, Table
    2 since Mon 16 Nov evening). Borders:
    top and bottom of the heads, above a subtotal, holdings, spanner, result or total, and at the bottom; never
    vertical (APA 7). spanners: [(first column, last column, text)] puts a column spanner over those heads (a second
    head row, with a rule under the spanner); the other heads span both head rows, set at the bottom. label_span=k
    prints the label of each subtotal, holdings and costs row across the first k columns (Table 1); label_indent
    {kind: inches} indents that label (the Treasury subtotal lines up with the names)."""
    from docx.shared import Inches, Pt
    rep._number_title(EXHIBITS[ex]["label"], EXHIBITS[ex]["title"], top)
    nh = 2 if spanners else 1
    t = rep.doc.add_table(rows=nh + len(rows), cols=len(header))
    t.alignment = BT.WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    BT._table_no_borders(t)
    BT._fixed_widths(t, widths)
    if spanners:
        _two_row_head(BT, rep, t, header, widths, spanners)
    all_rows = [("head", header)] + rows
    n = len(header)
    for r_i, (kind, values) in enumerate(all_rows):
        if spanners and r_i == 0:
            continue
        row = t.rows[r_i + nh - 1]
        BT._row_keep(row, header=(r_i == 0))
        if kind in ("spanner", "result", "held"):
            merged = row.cells[0].merge(row.cells[-1])
            cells, spans = [merged], [(0, n - 1)]
            values = [values[0]]
        elif label_span and kind in LABEL_KINDS:
            # Table 1's label rows: the label runs across the first label_span columns (no ticker, type or units)
            grid = list(row.cells)
            merged = grid[0].merge(grid[label_span - 1])
            cells = [merged] + grid[label_span:]
            spans = [(0, label_span - 1)] + [(c, c) for c in range(label_span, n)]
            values = [values[0]] + list(values[label_span:])
        else:
            cells = row.cells
            spans = [(c, c) for c in range(n)]
        last = r_i == len(all_rows) - 1
        for (c0, c1), cell, val in zip(spans, cells, values):
            full = c1 > c0
            cell.width = Inches(sum(widths[c0:c1 + 1]))
            BT._cell_margins(cell, PAD)
            _pad(cell, c0, c1, n)
            p = cell.paragraphs[0]
            p.style = rep.doc.styles["APA Table Text"]
            p.paragraph_format.keep_with_next = not last
            if kind == "head":
                p.alignment = BT.C
            else:
                p.alignment = BT.L if full else aligns[c0]
            if kind == "indent" and c0 == 0:
                p.paragraph_format.left_indent = Inches(0.2)
            if full and label_indent and kind in label_indent:
                p.paragraph_format.left_indent = Inches(label_indent[kind])
            if kind == "subtotal":
                p.paragraph_format.space_after = Pt(6)      # one deliberate gap after the subtotal (card Q28)
            if kind == "row" and row_gap:
                p.paragraph_format.space_after = Pt(row_gap)  # Table 3: multi-line rows need air between them
            # a cell is a string, or a list of runs (text, italic) as Table 3's last column is
            for text_, it in (val if isinstance(val, (list, tuple)) else [(str(val), kind == "spanner")]):
                run = p.add_run(text_)
                run.bold = kind == "total"
                run.italic = it
            edges = {}
            if kind == "head":
                edges.update(top=8, bottom=8)
            if kind in ("subtotal", "holdings", "spanner", "result") and not (kind == "spanner" and r_i == 1):
                edges.update(top=4)                         # a level right under the heads needs no second rule
            if kind == "total":
                edges.update(top=4)
            if kind == "held":
                edges.update(bottom=4)                      # sets the line apart from the rows it describes
            if last:
                edges.update(bottom=8)
            if edges:
                BT._cell_borders(cell, **edges)
    BT._order_tblpr(t)
    rep._note(note_text)
    if rep.blank_after_exhibit:
        rep.blank()
    return t


def _two_row_head(BT, rep, t, header, widths, spanners):
    from docx.enum.table import WD_ALIGN_VERTICAL
    from docx.shared import Inches
    covered = {c for a, b, _ in spanners for c in range(a, b + 1)}
    for r in (0, 1):
        BT._row_keep(t.rows[r], header=True)

    def fill(cell, text, w, edges, c_first, c_last):
        cell.width = Inches(w)
        BT._cell_margins(cell, PAD)
        _pad(cell, c_first, c_last, len(header))
        p = cell.paragraphs[0]
        p.style = rep.doc.styles["APA Table Text"]
        p.paragraph_format.keep_with_next = True
        p.alignment = BT.C
        p.add_run(text)
        BT._cell_borders(cell, **edges)
    for c, text in enumerate(header):
        if c in covered:
            fill(t.cell(1, c), text, widths[c], {"bottom": 8}, c, c)
        else:
            m = t.cell(0, c).merge(t.cell(1, c))
            m.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
            fill(m, text, widths[c], {"top": 8, "bottom": 8}, c, c)
            # the continuation cell of a vertical merge carries the rule under the heads in LibreOffice and Word
            from docx.table import _Cell
            BT._cell_borders(_Cell(t.rows[1]._tr.tc_lst[c], t), bottom=8)
    for a, b, text in spanners:
        m = t.cell(0, a).merge(t.cell(0, b))
        fill(m, text, sum(widths[a:b + 1]), {"top": 8, "bottom": 4}, a, b)


def add_table1(BT, rep, note_text, top=False):
    # Each cell needs its text + its padding (0.08 in between columns, none at the outer edges) + slack, or it wraps:
    # (before Fri 13 Nov evening) "[532281]" 0.611 in; "Asset" 0.370; "from cash left" 0.926 and "4,503 / 4,503" 0.880; bold "300,000.00" 0.750;
    # bold "100.00" 0.458; "Range top," 0.722; the longest bond name 2.014. Thu 12 Nov evening: the "Units bought /
    # target" column (1.05 in) is paid for by the name column (3.17 -> 2.13 in), so the five iBond fund names and VT's
    # take two lines (IBTM's and VT's rows had two already). The label rows run across the first four columns (4.31
    # in): the Treasury subtotal indented to the names, "All holdings" and the costs row flush left like "Total".
    # Units are centred: bought and target have the same digits in every row, so the slashes line up.
    # Fri 13 Nov evening (card Q38): the bonds' CUSIPs (widest "912810QD3", 0.824 in by font metrics) widen column 1
    # to 0.87 in, paid by every other column's slack, each set by rendering in LibreOffice (which needs about 0.02-0.04
    # in more than the font metrics: the bond names wrapped at 2.09 and "4,503 / 4,503" at 0.96): names 2.12, units
    # 0.97 (VT's "with the rest" 0.824), amount 0.83 (bold "300,000.00" 0.750), % 0.54 (bold "100.00" 0.458), and
    # Pays-for 0.71, VT's cell on three lines ("Range / top, / flexibility"), which its three-line units cell already
    # makes the row's height. Table 1 keeps 20.9 lines with its note budget.
    widths = [0.87, 2.12, 0.46, 0.97, 0.83, 0.54, 0.71]
    aligns = [BT.L, BT.L, BT.L, BT.C, BT.R, BT.R, BT.C]
    return apa_table(BT, rep, "t1", D.TABLE1_HEADER, D.table1_rows(), widths, aligns, note_text, top,
                     label_span=D.LABEL_SPAN, label_indent={"subtotal": widths[0] + PAD / 1440})


def add_figure1(BT, rep, note_text, top=False):
    rep.figure(EXHIBITS["f1"]["label"], EXHIBITS["f1"]["title"], os.path.join(HERE, "exhibit2_reserve.png"),
               width_in=W, note=note_text, top=top)


def add_table2(BT, rep, note_text, top=False):
    widths = [2.50, 0.95, 0.95, 0.95, 1.15]
    aligns = [BT.L, BT.L, BT.R, BT.R, BT.R]
    # Mon 16 Nov evening (card Q14b row 20): first, one line of what is held the same in every row
    rows = [("held", [D.TABLE2_HELD_SAME])]
    rows += [("row", [name] + D.table2_cells(v)) for _, name, v in D.TABLE2_WORLDS]
    rows.append(("spanner", [D.TABLE2_SPREAD_LABEL]))
    rows += [("indent", [label] + D.table2_cells(v)) for label, v in D.TABLE2_SPREAD]
    rows.append(("result", [D.TABLE2_RESULT_ROW]))        # the confidence answer, inside the table
    return apa_table(BT, rep, "t2", D.TABLE2_HEAD_ROW, rows, widths, aligns, note_text, top,
                     spanners=[(2, 3, D.TABLE2_SPANNER)])


def add_table3(BT, rep, note_text, top=False):
    # Widths (6.5 in): the reader column holds "Laura" and "Team" on one line; the last column is the widest, as it
    # carries two parts ("Changes:" and "Never:", in italics).
    widths = [0.85, 0.48, 1.55, 1.62, 2.00]   # Fri 13 Nov evening: "Who" needs less than "Reader"
    aligns = [BT.L] * 5
    return apa_table(BT, rep, "t3", D.TABLE3_HEADER, D.table3_rows(), widths, aligns, note_text, top, row_gap=1)


# Words never printed in any exhibit, title or note (Mon 16 Nov evening, lead's brief; CONCEIT V2.2: the conceit stays
# in prose, never in a table or note; WORDS and Book 19's banned words; an iBond fund's payout is never fixed,
# NUMBERS 3). Patterns are matched on whole words, case ignored.
# Mon 16 Nov night: "fixed" is allowed only negated, "not a fixed" (WORDS: an iBond fund pays "not a fixed amount";
# Figure 1's note item 1, coherence reader 6, M9: "its net asset value, not a fixed sum").
NEVER_WORDS = (r"\bpencil", r"\bink(ed|s)?\b", r"\bendowment", r"\boptimal", r"\bnatural hedge", r"\bfail-safe",
               r"(?<!\bnot a )\bfixed\b", r"\b89%")


def exhibit_texts():
    """Every string the four exhibits print or carry as note items: (where, text)."""
    out = []
    for ex in ORDER:
        out.append((f"{ex} title", EXHIBITS[ex]["title"]))
        out += [(f"{ex} note item", t) for t in EXHIBITS[ex]["note_items"]]
    out += [("t1 head", h) for h in D.TABLE1_HEADER]
    out += [("t1 cell", c) for _, cells in D.table1_rows() for c in cells]
    hd = D.FIGURE1_HEADS
    out += [("f1 head", v if isinstance(v, str) else " ".join(v)) for v in hd.values()]
    out += [("f1 legend", t) for t in D.FIGURE1_LEGEND] + [("f1 bar", r["holding"]) for r in D.FIGURE1_ROWS]
    out += [("t2 head", h) for h in D.TABLE2_HEAD_ROW + [D.TABLE2_SPANNER, D.TABLE2_SPREAD_LABEL]]
    out += [("t2 line", D.TABLE2_HELD_SAME), ("t2 line", D.TABLE2_RESULT_ROW)]
    out += [("t2 world", name) for _, name, _ in D.TABLE2_WORLDS]
    out += [("t3 head", h) for h in D.TABLE3_HEADER + list(D.TABLE3_LEVELS.values())]
    out += [("t3 cell", D.cell_text(c)) for _, cells in D.TABLE3_ROWS for c in cells]
    return out


def words_check(verbose=True):
    """Fails if any exhibit text carries a word that is never printed there. Returns (n checks, failures)."""
    import re
    texts = exhibit_texts()
    fails = [(w, pat, t) for w, t in texts for pat in NEVER_WORDS if re.search(pat, t, re.I)]
    if verbose:
        for w, pat, t in fails:
            print(f"  FAIL     words     {w}: '{pat}' in {t!r}")
        print(f"Words check: {len(texts)} exhibit texts x {len(NEVER_WORDS)} patterns, {len(fails)} FAIL")
    return len(texts) * len(NEVER_WORDS), fails


ADDERS = {"t1": add_table1, "f1": add_figure1, "t2": add_table2, "t3": add_table3}
ORDER = ("t1", "f1", "t2", "t3")


# Mon 16 Nov night: a note item may carry its reviewer's mark, as tables.md records it ("(coherence reader 6, Mon 16
# Nov, L3: ...)", or "; coherence reader 6, ..." inside a source's brackets). The mark is bookkeeping, not an item the
# note carries, so the Letter PDF's placeholder note leaves it out (it would also push Table 1's note off its page).
_MARK = r"(?:coherence reader|bond desk|funder test)"


def _unmarked(item):
    import re
    item = re.sub(r" \(" + _MARK + r"[^()]*(?:\([^()]*\)[^()]*)*\)", "", item)
    return re.sub(r"; " + _MARK + r"[^()]*(?:\([^()]*\)[^()]*)*(?=\))", "", item)


def items_note(ex):
    return "[Note to carry: " + "; ".join(_unmarked(t) for t in EXHIBITS[ex]["note_items"]) + ".]"


def build_letter_pdf(BT, path_docx):
    """The four exhibits on Letter in Wharton's format, each with its note items as a placeholder note."""
    rep = BT.Report(paper="letter")
    for k, ex in enumerate(ORDER):
        rep.para("Above the exhibit.")
        ADDERS[ex](BT, rep, items_note(ex), top=(k > 0))
        rep.para("Below the exhibit.")
    return rep.save(path_docx)


def crop_previews(BT, pdf):
    import pdfplumber
    pages = BT.pdf_pages_text(pdf)
    out = {}
    with pdfplumber.open(pdf) as doc:
        for ex, name in (("t1", "table1_holdings_2x.png"), ("t2", "table2_markets_2x.png"),
                         ("t3", "table3_monitoring_2x.png")):
            pi, ln = BT.find_line(pages, EXHIBITS[ex]["label"])
            pj, below = BT.find_line(pages, "Below the exhibit.", start_page=pi)
            top = ln["top"] - 6
            page = doc.pages[pi]
            if pi == pj:
                bottom = below["top"] - 27.6 + 4      # stop above the blank line after the exhibit
                img = page.crop((66, top, page.width - 66, bottom)).to_image(resolution=PREVIEW_DPI)
                img.save(os.path.join(HERE, name))
                out[ex] = name
                continue
            # Table 1 since Thu 12 Nov evening: its note-items placeholder (about 110 words, longer than the 75-word
            # budget) pushes the line after it to the next page; stop under the last text line above the page number.
            body = [x for x in BT.lines_of(pages[pi]["words"]) if x["top"] < pages[pi]["height"] - 72]
            assert body, f"{ex} spans pages"
            img = page.crop((66, top, page.width - 66, body[-1]["bottom"] + 6)).to_image(resolution=PREVIEW_DPI)
            if pj == pi + 1 and body[-1]["text"].endswith(".]"):
                img.save(os.path.join(HERE, name))
                out[ex] = name
                continue
            # Mon 16 Nov night: the exhibit runs over a page break: Table 1's placeholder note by two lines (its items
            # grew with coherence reader 6's L3), and Table 3 itself (its rows grew with that night's hand edits; see
            # measurements.json). The preview joins each page's part, label to "Below the exhibit.", so it shows the
            # whole exhibit; the build says so, and measure() sizes the overrun.
            parts = [img.original]
            for k in range(pi + 1, pj + 1):
                lim = below["top"] - 1 if k == pj else pages[k]["height"] - 72
                more = [x for x in BT.lines_of(pages[k]["words"]) if x["top"] < lim]
                if not more:
                    continue
                pk = doc.pages[k]
                parts.append(pk.crop((66, more[0]["top"] - 6, pk.width - 66, more[-1]["bottom"] + 6)).to_image(
                    resolution=PREVIEW_DPI).original)
            from PIL import Image
            joined = Image.new("RGB", (max(p.width for p in parts), sum(p.height for p in parts)), "white")
            y = 0
            for p in parts:
                joined.paste(p, (0, y))
                y += p.height
            joined.save(os.path.join(HERE, name))
            out[ex] = f"{name} (joined from pages {pi + 1}-{pj + 1} of the Letter PDF: it runs over a page break)"
            print(f"  WARNING  {EXHIBITS[ex]['label']} with its note-items placeholder runs over a page break in "
                  f"exhibits_letter.pdf (pages {pi + 1}-{pj + 1}); its preview joins the parts")
    return out


# Where each exhibit's filler note starts in the filler text: where it started on Wed 11 Nov (one shared filler, notes
# of 50, 60, 45 and 35 words in turn). Fixed since Thu 12 Nov evening, so that a longer Table 1 note does not change the
# words, and so the line breaks, of the notes measured after it (Figure 1 measured a line taller when it moved).
FILLER_START = {"t1": 0, "f1": 50, "t2": 110, "t3": 155}


def measure(BT, workdir):
    """Card Q23's method: an exhibit between two prose lines on a Letter page; its height = the gap / 27.6 pt - 1
    double-spaced lines, counting the number, title, note and the blank line after. Notes are filler of each
    exhibit's word budget (the notes are written on 27 Nov), and without a note, so the cost per note line shows."""
    f = BT.Filler()
    res = {}
    for ex in ORDER:
        f.i = FILLER_START[ex]
        for variant, words in (("note_budget", EXHIBITS[ex]["note_budget_words"]), ("no_note", 0)):
            note = f.words(words) + "." if words else None
            rep = BT.Report(paper="letter")
            rep.para("Above the exhibit.")
            ADDERS[ex](BT, rep, note)
            rep.para("Below the exhibit.")
            pdf = rep.save(os.path.join(workdir, f"m_{ex}_{variant}.docx"))
            pages = BT.pdf_pages_text(pdf)
            a = BT.find_line(pages, "Above the exhibit.")
            b = BT.find_line(pages, "Below the exhibit.")
            key = f"{ex}_{variant}"
            if a[0] == b[0]:
                gap = b[1]["top"] - a[1]["top"]
                lines = gap / 27.6 - 1
                res[key] = {"lines": round(lines, 1), "inches": round((gap - 27.6) / 72, 2),
                            "prose_words_displaced": int(round(lines * 14.26, -1)), "note_words": words,
                            "pages_spanned": 1}
            else:
                # Too tall to sit between two prose lines (Table 3 with its note): it moved whole to the next page,
                # so measure from the top of that page (where the "Above" line sat on its own page) to "Below".
                n = BT.find_line(pages, EXHIBITS[ex]["label"], start_page=b[0])
                whole = n[0] == b[0] and abs(n[1]["top"] - a[1]["top"]) < 2.0 and a[0] == b[0] - 1
                if whole:
                    gap = b[1]["top"] - a[1]["top"]
                    lines = gap / 27.6
                    res[key] = {"lines": round(lines, 1), "inches": round(gap / 72, 2),
                                "prose_words_displaced": int(round(lines * 14.26, -1)), "note_words": words,
                                "pages_spanned": 1, "method": "from the top of its own page (too tall to sit "
                                                              "between two prose lines)"}
                else:
                    # Mon 16 Nov night: too tall for one Letter page (Table 3 after that night's hand edits). Measured
                    # again by the same method on a page of Letter width and 22 in tall, so the size of the overrun
                    # is known: Letter's text block is 9 in (648 pt, 23.5 double-spaced lines).
                    res[key] = {"lines": None, "pages_spanned": b[0] - a[0] + 1, "note_words": words,
                                **_measure_tall(BT, ex, note, workdir, variant)}
    return res


LETTER_BODY_IN = 9.0        # 11 in less two 1-in margins


def _measure_tall(BT, ex, note, workdir, variant):
    """Card Q23's method on a page of Letter width and 22 in tall, for an exhibit too tall for one Letter page."""
    BT.PAPER.setdefault("tall", (8.5, 22.0))
    rep = BT.Report(paper="tall")
    rep.para("Above the exhibit.")
    ADDERS[ex](BT, rep, note)
    rep.para("Below the exhibit.")
    pages = BT.pdf_pages_text(rep.save(os.path.join(workdir, f"tall_{ex}_{variant}.docx")))
    a, b = BT.find_line(pages, "Above the exhibit."), BT.find_line(pages, "Below the exhibit.")
    assert a[0] == b[0], f"{ex} spans pages even 22 in tall"
    gap = b[1]["top"] - a[1]["top"]
    inches = (gap - 27.6) / 72
    return {"lines_on_a_tall_page": round(gap / 27.6 - 1, 1), "inches": round(inches, 2),
            "over_one_letter_page_inches": round(inches - LETTER_BODY_IN, 2),
            "over_one_letter_page_lines": round((inches - LETTER_BODY_IN) * 72 / 27.6, 1), "fits_one_page": False,
            "method": "too tall for one Letter page: measured on a page of Letter width, 22 in tall (Letter's text "
                      "block is 9 in, 23.5 double-spaced lines)"}


SECTION2_BUDGET = 580        # SKELETON, Panel 2's density cut (Thu 12 Nov): 100 + 120 + 80 + 130 + 150 words
CEILING_BEFORE = 661         # the same fit, Thu 12 Nov evening, on Wed 11 Nov's Table 1 (6 columns, 50-word note)


def fit_section2(BT, workdir):
    """Section 2 against Wharton's three-page maximum (card Q23 row 33's method, `fit_mock` in the template): title page,
    paper title, the Level 1 heading, the lead and part 2.1 with its Level 2 heading on page 2, Table 1 (with the
    note budget in filler) at the top of page 3, then parts 2.2, 2.3 and 2.5 with their headings; Section 3 starts
    on a new page. Each prose block is filled with filler (120-word paragraphs) until one more word would push
    Table 1 off page 3 or Section 3 off page 5. The sum is the most prose Section 2 holds in three pages."""
    note = BT.Filler().words(EXHIBITS["t1"]["note_budget_words"]) + "."
    n = [0]

    def pages(pre, post):
        n[0] += 1
        f = BT.Filler()
        rep = BT.Report(paper="letter")
        rep.title_page()
        rep.paper_title("[Report Title]")
        rep.heading(BT.SECTION2, 1)
        BT._prose_with_headings(rep, f, pre, ["Part 2.1 Heading"], 120)
        add_table1(BT, rep, note, top=True)
        BT._prose_with_headings(rep, f, post, [f"Part {p} Heading" for p in BT.S2_PARTS[1:]], 120, lead=False)
        rep.heading(BT.SECTION3, 1, new_page=True)
        rep.para("Section three starts here.")
        return BT.pdf_pages_text(rep.save(os.path.join(workdir, "s2_fit.docx")))

    def most(lo, hi, ok):
        best = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                best, lo = mid, mid + 1
            else:
                hi = mid - 1
        return best

    pre = most(150, 400, lambda v: BT.find_line(pages(v, 0), "Table 1")[0] == 2)
    post = most(100, 700, lambda v: BT.find_line(pages(pre, v), BT.SECTION3)[0] == 4)
    final = pages(pre, post)
    t1_page = BT.find_line(final, "Table 1")[0] + 1
    ceiling = pre + post
    return {"ceiling_words": ceiling, "before_table1_words": pre, "after_table1_words": post,
            "budget_words": SECTION2_BUDGET, "headroom_words": ceiling - SECTION2_BUDGET,
            "headroom_real_text_words": int(round(ceiling * 0.97 - SECTION2_BUDGET)),
            "headroom_lines": round((ceiling - SECTION2_BUDGET) / 14.26, 1),
            "ceiling_before_words": CEILING_BEFORE, "table1_page": t1_page,
            "pages": "title 1; Section 2 pages 2-4 (Wharton's maximum, 3); Section 3 from page 5",
            "conversions": n[0],
            "method": "card Q23 row 33 (fit_mock): Letter, Wharton's format, 120-word filler paragraphs, the paper title "
                      "on page 2, Level 1 heading, lead + 2.1 under one Level 2 heading before Table 1 (top of page 3), "
                      "2.2, 2.3 and 2.5 under three after it; Table 1 with its note budget in filler. Real text runs "
                      "2-3% under a filler ceiling (Q23), so the real-text headroom takes 3% off the ceiling."}


# =================================================================================================================
# tables.md: every exhibit as text
# =================================================================================================================
def _md_table(header, rows, right):
    def esc(s):
        return str(s).replace("|", "\\|")
    out = ["| " + " | ".join(header) + " |",
           "|" + "|".join("---:" if i in right else "---" for i in range(len(header))) + "|"]
    for r in rows:
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    return "\n".join(out)


def tables_md(measures):
    L = []
    L.append("# The Final Report's exhibits as text (built Mon 16 Nov 2026 evening, Sydney)\n")
    L.append(f"Generated by `build_exhibits.py` from `exhibit_data.py`, which reads `../numbers/results_*_{D.REGISTER_DATE}.json` "
             "and checks every figure against `../NUMBERS.md` (sections named under each exhibit). Notes for the "
             "store, not report prose: titles are working labels and each note lists the items it must carry; both "
             "are written on 27 Nov. Square brackets mark placeholders. MODEL = Keel's calculation, not a forecast.\n")
    # Mon 16 Nov night: the hand edits of that night (coherence reader 6; bond desk 4), carried into the scripts
    L.append("**Hand edits, Mon 16 Nov night (coherence reader 6; bond desk 4), each marked in place below: carried into "
             "`exhibit_data.py` and `build_exhibits.py` the same night, so a rebuild keeps them; Table 3's page fit is "
             "re-measured (its page cost below), since rows 4, 5 and 7 are longer, and Table 2's, since its printed "
             "head now reads \"" + D.TABLE2_FLEX_HEAD + "\" as well (SKELETON Exhibits item 3).**\n")

    def cost(ex):
        m = measures.get(f"{ex}_note_budget", {})
        n = measures.get(f"{ex}_no_note", {})
        if m.get("lines") is None and m.get("lines_on_a_tall_page") is not None:
            # Mon 16 Nov night: too tall for one Letter page; its size from a tall page (measure, _measure_tall)
            return (f"Page cost in Wharton's format (Letter, 12 pt, double-spaced text, single-spaced body): **does not "
                    f"fit one page: {m['lines_on_a_tall_page']} double-spaced lines ({m['inches']} in) with a "
                    f"{m.get('note_words')}-word note, {m['over_one_letter_page_lines']} lines "
                    f"({m['over_one_letter_page_inches']} in) more than Letter's 9-in text block**; "
                    f"{n.get('lines_on_a_tall_page', n.get('lines'))} lines ({n.get('inches')} in) without a note "
                    f"({n.get('over_one_letter_page_lines', 0)} over). Measured on a page of Letter width, 22 in tall.")
        return (f"Page cost in Wharton's format (Letter, 12 pt, double-spaced text, single-spaced body): "
                f"**{m.get('lines')} double-spaced lines** with a {m.get('note_words')}-word note "
                f"(about {m.get('prose_words_displaced')} words of prose); "
                f"{n.get('lines')} lines without a note.")

    # Table 1
    L.append(f"## {EXHIBITS['t1']['label']}. {EXHIBITS['t1']['title']} (working title)\n")
    L.append(f"{EXHIBITS['t1']['section']}. Source: NUMBERS 8g version 2, the WInS record at cost (not a model).\n")
    rows = []
    k = D.LABEL_SPAN
    for kind, cells in D.table1_rows():
        cells = [c.replace("\n", " ") for c in cells]
        if kind == "subtotal":                       # printed across the first four columns, indented to the names
            cells = ["", f"*{cells[0]}*"] + [""] * (k - 2) + [f"*{c}*" if c else "" for c in cells[k:]]
        if kind == "holdings":                       # printed flush left across the first four columns
            cells = [f"*{cells[0]}*"] + [""] * (k - 1) + [f"*{c}*" if c else "" for c in cells[k:]]
        if kind == "total":
            cells = [f"**{c}**" if c else "" for c in cells]
        rows.append(cells)
    L.append(_md_table(D.TABLE1_HEADER, rows, right={4, 5}) + "\n")
    L.append("Printed: the five iBond fund names and VT's take two lines in the 2.12-in name column, as does the "
             "Pays-for cell of IBTM (\"2033 and / the floor\"); VT's Pays-for cell takes three (\"Range / top, / "
             "flexibility\") and so does its units cell (\"167 / 164 / bought last, / with the rest\"). The bonds' "
             "identifiers are their CUSIPs (card Q38). Units are centred, so the slashes line up. "
             "The two subtotals and the costs row print their labels across the first four columns: the Treasury "
             "subtotal indented to the names; \"All holdings\" and the costs row flush left, with no ticker, type or "
             "units. Rules above each subtotal and the total. Asset types are one word (Wharton's \"ETF\" and \"Bond\" "
             "for its \"Treasury Bond\"); the dollar sign is in the head.\n")
    L.append("Note items: " + "; ".join(EXHIBITS["t1"]["note_items"]) + ".\n")
    L.append(cost("t1") + "\n")
    s2 = measures.get("s2_fit")
    if s2:
        L.append(f"Section 2 in Wharton's three pages (measured): {s2['ceiling_words']} words of prose at most beside "
                 f"Table 1 (Q23's method); SKELETON budgets {s2['budget_words']}, so **{s2['headroom_words']} words of "
                 f"headroom** (about {s2['headroom_real_text_words']} in real text, which runs 2-3% under a filler "
                 f"ceiling). The same fit on Wed 11 Nov's Table 1 (six columns, 50-word note): {s2['ceiling_before_words']}.\n")

    # Figure 1
    L.append(f"## {EXHIBITS['f1']['label']}. {EXHIBITS['f1']['title']} (working title)\n")
    L.append(f"{EXHIBITS['f1']['section']}. Source: NUMBERS 8h (MODEL), `results_reserve_{D.REGISTER_DATE}.json` blocks "
             "`composition_1jan2033_base` and `fee` (`base`, today's market rates, for note item 4 only); cash dates "
             "and the note's reconciliation from "
             f"`results_topup_{D.REGISTER_DATE}.json` (Fri 13 Nov; re-run Sun 15 Nov evening). The figure is `figure1_reserve.svg`; its numbers as text:\n")
    rows = []
    for r in D.FIGURE1_ROWS:
        arrives = D.cash_words(r)             # Fri 13 Nov: the cash date (8h's cash table), not the fund's end date
        if r["wait_words"]:
            arrives += f" (waits {r['wait_words']})"
        rows.append([r["year"], r["holding"], "Treasury bond" if r["kind"] == "T-bond" else "iBond Treasury fund",
                     arrives, D.dollars(r["own_if_nothing_earns"]), D.dollars(r["backstop_if_nothing_earns"]), ""])
    # Mon 16 Nov evening (card Q73): one world; the heads print the sum and the total row adds up exactly
    own_tot, extra_tot, sum_tot = (D.dollars(v) for v in D.FIGURE1_TOTAL_ROW)
    rows.append(["**Total**", "", "", "", f"**{own_tot}**", f"**+ {extra_tot}**", f"**= {sum_tot}**"])
    hd = D.FIGURE1_HEADS
    L.append(_md_table([hd["payment"] + " (1 Jan)", "Paid from", "Type", "Cash arrives", " ".join(hd["c2"]),
                        f"{hd['plus']} {' '.join(hd['c3'])}", f"{hd['equals']} {hd['sum']}"], rows,
                       right={4, 5, 6}) + "\n")
    L.append(f"As drawn (Mon 16 Nov evening, card Q73's three fixes): one world, cash waiting earning nothing after the "
             f"0.15% fee on waiting money (8h's \"fee\" block); the heads read \"{' '.join(hd['c2'])} {hd['plus']} "
             f"{' '.join(hd['c3'])} {hd['equals']} {hd['sum']}\" and the total row \"{own_tot} {hd['plus']} {extra_tot} "
             f"{hd['equals']} {sum_tot}\" (8h's totals of unrounded figures; the rows, rounded, add to "
             f"{D.dollars(D.FIGURE1_FOOT[0])} and {D.dollars(D.FIGURE1_FOOT[1])}, note item 3); the \"At today's "
             f"market rates\" column ($50,000 ten times) is now note item 4; no axis break (the timeline runs unbroken "
             f"from January 2027 to 2042); a dotted line and \"waits 10.5 months\" / \"waits 7.5 months\" mark the two "
             f"long waits; legend: {D.FIGURE1_LEGEND[0]} (coherence reader 6, Mon 16 Nov, L2: the figure's own Type "
             f"column); {'; '.join(D.FIGURE1_LEGEND[1:])}.\n")
    L.append("Note items: " + "; ".join(EXHIBITS["f1"]["note_items"]) + ".\n")
    L.append(cost("f1") + "\n")

    # Table 2
    L.append(f"## {EXHIBITS['t2']['label']}. {EXHIBITS['t2']['title']} (working title)\n")
    L.append(f"{EXHIBITS['t2']['section']}. Source: NUMBERS 8i (MODEL; the spread of the flexibility from 8j's joint "
             f"replay column), `results_joint_stress_{D.REGISTER_DATE}.json`.\n")
    rows = [[name] + D.table2_cells(v) for _, name, v in D.TABLE2_WORLDS]
    rows.append([f"*{D.TABLE2_SPREAD_LABEL}*", "", "", "", ""])
    rows += [[f"&nbsp;&nbsp;{label}"] + D.table2_cells(v) for label, v in D.TABLE2_SPREAD]
    L.append(f"First line of the table, full width under the heads, a thin rule below (Mon 16 Nov evening, card Q14b "
             f"row 20): \"{D.TABLE2_HELD_SAME}\" (checked: one design, one range-rule stamp and the $150,000 2028 "
             "deposit in every world of the results file; 8i, NUMBERS 0).\n")
    L.append(_md_table(D.TABLE2_HEADER, rows, right={2, 3, 4}) + "\n")
    L.append(f"Last row of the table, full width under a rule: \"{D.TABLE2_RESULT_ROW}\" (coherence reader 6, Mon 16 "
             "Nov, L2 and M6, also the header, the first row and the history label above: WORDS's names) (checked: all "
             "five worlds and 100% of the 585 replays, 8i and 8j).\n")
    L.append("Note items: " + "; ".join(EXHIBITS["t2"]["note_items"]) + ".\n")
    L.append(cost("t2") + "\n")

    # Table 3
    L.append(f"## {EXHIBITS['t3']['label']}. {EXHIBITS['t3']['title']} (working title)\n")
    L.append(f"{EXHIBITS['t3']['section']}. Source: SKELETON Exhibits item 4 (Thu 12 Nov spec: card Q30's cut, the bond "
             "reader of Wed 11 Nov, Keel's definitions of the two reasons); every figure from NUMBERS 2, 5, 8d, 8h and "
             "8j through `exhibit_data.py`, checked. Single-spaced; each level is an italic row across the table; the "
             "last column prints \"Changes:\" and \"Never:\" in italics, each on its own line.\n")
    rows = []
    for kind, cells in D.table3_rows():
        if kind == "spanner":
            rows.append([f"*{cells[0]}*", "", "", "", ""])
        else:
            rows.append([D.cell_text(c) if not isinstance(c, list) else
                         "".join(f"*{t}*" if it else ("<br>" if t == "\n" else t) for t, it in c) for c in cells])
    L.append(_md_table(D.TABLE3_HEADER, rows, right=set()) + "\n")
    L.append("Note items: " + "; ".join(EXHIBITS["t3"]["note_items"]) + ".\n")
    L.append("Mon 16 Nov hand edits to Table 3 (carried into `exhibit_data.py` the same night; page re-measured below): "
             "row 1, the missed deposit's cost on both bases (coherence reader 6 and bond desk 4, M7, L5; L5's action "
             "wording declined: card Q34 keeps the later money's order in 3e's prose); row 2, \"payments ... "
             "restated\" corrected (bond desk 4, L6); row 4, the frozen name of the waiting fund (coherence reader 6, "
             "L1: TNA l.5, WN l.17), filings read in any year and a dated missing-notice trigger (bond desk 4, M5), one "
             "action per event and no \"Treasury due by 15 December\", which WInS does not list for 2033 or 2035 (bond "
             "desk 4, M4; coherence reader 6, L17); row 5, a stressed-trade-day trigger, its distance [x]% not yet in "
             "NUMBERS (bond desk 4, M6); row 6, \"the 2031 move\" alone banned (coherence reader 6, L2); row 7, one "
             "reading of \"10% stronger\" (8j: 10% more US dollars) and a \"carry on while\" that is a condition "
             "(bond desk 4, M7; its building-cost trigger declined: SKELETON's Sat 14 Nov decision, CANON A34); the "
             "note names its basis (bond desk 4, L10; the ladder alone holds to 3.89 points, NUMBERS 5).\n")
    L.append("Not a row: custody (one line of 3e prose, SKELETON item 4 (c)). Not in the table or its note: IBTA's "
             f"early end in 2021 (cash about {D.IBTA_SLACK} business days before year end; notice filed 28 Sep 2021; "
             "card Q3c row 8, NUMBERS 8h), an example of row 4's \"ends early\" for 3e's prose. Any mention of it in "
             "row 4 or a longer note puts Table 3 on two pages (measured Sun 15 Nov evening).\n")
    L.append(cost("t3") + "\n")
    with open(os.path.join(HERE, "tables.md"), "w") as fh:
        fh.write("\n".join(L))


# =================================================================================================================
def main(argv):
    fails, _ = D.check(verbose=True)
    if fails:
        sys.exit("Stopped: an exhibit figure does not match NUMBERS.md (listed above).")
    _, word_fails = words_check()
    if word_fails:
        sys.exit("Stopped: an exhibit text carries a word never printed there (listed above).")
    print("font:", FONT)
    print(figure1([(os.path.join(HERE, "figure1_reserve.svg"), None),
                   (os.path.join(HERE, "figure1_reserve_2x.png"), PREVIEW_DPI),
                   (os.path.join(HERE, "exhibit2_reserve.png"), PRINT_DPI)]))
    if argv[1:2] == ["figure"]:
        return
    BT = _template()
    pdf = build_letter_pdf(BT, os.path.join(HERE, "exhibits_letter.docx"))
    print(pdf, BT.audit(pdf, quiet=True).get("fonts"))
    print(crop_previews(BT, pdf))
    work = tempfile.mkdtemp(prefix="keel_exhibits_")
    m = measure(BT, work)
    m["s2_fit"] = fit_section2(BT, work)
    shutil.rmtree(work, ignore_errors=True)
    m["_method"] = ("Card Q23: Letter, 1-inch margins, 12-pt Times New Roman metrics (Liberation Serif), double-spaced "
                    "text at a 27.6-pt pitch, table bodies single-spaced, APA number, title and note double-spaced, a "
                    "blank double-spaced line after each exhibit; LibreOffice headless; words a line 14.26 (Q23 row 5)")
    m["_built"] = f"Mon 16 Nov 2026 evening (Sydney), register of {D.REGISTER_DATE} (results_*_{D.REGISTER_DATE}.json)"
    with open(os.path.join(HERE, "measurements.json"), "w") as fh:
        json.dump(m, fh, indent=1)
    print(json.dumps(m, indent=1))
    tables_md(m)
    print("tables.md written")


if __name__ == "__main__":
    main(sys.argv)
