"""Build the Final Report's four exhibits on the register of Tue 10 Nov 2026 (rebuilt Fri 13 Nov 2026 morning, Sydney;
re-built Mon 16 Nov 2026 on the Sun 15 Nov evening results files, NUMBERS 9; Mon 16 Nov evening: card Q73's three
Figure 1 fixes and Table 2's held-the-same line and history check, REBUILD_2026-11-16_evening.md; Mon 16 Nov night:
that night's hand edits to tables.md (coherence reader 6; bond desk 4) carried in, here and in exhibit_data.py, and an
exhibit too tall for one Letter page measured on a tall page and previewed whole, with a warning; Tue 17 Nov: Table 3
cut back to one page, 27.9 to 21.4 lines with its note, the cut details listed under it for 3e's notes, and row 5's
trade-day limit from NUMBERS 4, REBUILD_2026-11-17.md; Wed 18 Nov evening: the morning's hand edits to Table 2's note
carried in, the 7.5%'s source and standing, the room under the top and the starting months' method, with carry_check,
then a second pass: no median figure (the lead's call on card Q146) and the note trimmed to sit between two prose
lines; then a third pass: Table 3 row 4 in the numbers owner's words on what the 0.5% margin pays, and bond desk 5's
H1-H3, M5 and M6 in Tables 2 and 3, REBUILD_2026-11-18_evening.md).

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
from matplotlib.transforms import blended_transform_factory  # noqa: E402
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
            num_l = C2_R - width(D.dollars(r["own_printed"]))
            assert right + 0.04 <= num_l, f"'waits {r['wait_words']}' runs into the number column"
        text(X_YEAR, y, str(r["year"]))
        # one world (card Q73-035): what pays each $50,000 if cash waiting earns nothing, after the 0.15% fee, with
        # each fund's flows 0.5% smaller (Thu 26 Nov: the fee-and-margin basis, NUMBERS 8h, 8zb)
        text(C2_R, y, D.dollars(r["own_printed"]), ha="right")
        text(C3_R, y, D.dollars(r["backstop_printed"]), ha="right")

    # ---- totals: 8zb's totals of unrounded figures, which add up exactly, "$442,930 + $57,070 = $500,000" ----
    ax.plot([0, W], [last + 0.03, last + 0.03], color=INK, linewidth=0.6)
    yt = last + 0.03 + ROW_H / 2 + 0.01
    # Tue 17 Nov (coherence reader 7, M2): labelled as a ten-year sum of payouts, never "Total" (read as a size)
    lab = text(X_YEAR, yt, D.FIGURE1_TOTAL_LABEL)
    fig.canvas.draw()
    assert lab.get_window_extent().transformed(ax.transData.inverted()).x1 + 0.04 <= C2_L, \
        "the total row's label runs into the number column"
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
# Figure 2 (Mon 23 Nov, the lead's decision 2): Table 2 drawn as ranges and dots (card c4), in place of Table 2 in the
# report. Both fresh readers got its point faster (charts/fresh_read_2026-11-23/). What the table carried and the picture
# cannot: "All paid" is the APA title; the bottom and top are printed at each end of each range; the contribution =
# top line and the held-the-same line go to the note. History is the median starting month alone (decision 3).
# Position on a common scale (Cleveland and McGill's first task) for the ends and the dots; two panels side by side,
# each with its own dollar axis, never a dual axis; today's row in black, the others dark grey, identity in the labels.
# =================================================================================================================
F2_W, F2_H = 6.5, 2.30


def _k(v):
    return f"${v / 1000:,.0f}k" if v % 1000 == 0 else f"${v / 1000:,.1f}k"


def figure2(outputs):
    rows = [(name, v) for _, name, v in D.TABLE2_WORLDS]
    hist = D.TABLE2_HISTORY
    assert len(rows) == 5 and len(hist) == 1, (len(rows), len(hist))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(F2_W, F2_H), sharey=True, gridspec_kw={"width_ratios": [1.55, 1]})
    # Thu 26 Nov: the notes' longer row names (CHECK_EXHIBITS item 12) were clipped at 0.335; measured, 0.41 holds them
    fig.subplots_adjust(left=0.41, right=0.985, top=0.75, bottom=0.12, wspace=0.08)
    ys = [7.0, 6.0, 5.0, 4.0, 3.0]
    y_hist = 0.9
    lab = []
    for y, (name, v) in zip(ys + [y_hist], rows + [(n, v) for n, v in hist]):
        col = INK if name == rows[0][0] else BOND
        lo, hi, fx = v["bottom"] / 1000, v["top"] / 1000, v["flexibility"]
        a1.plot([lo, hi], [y, y], color=col, lw=2.0, solid_capstyle="butt")
        a1.plot([lo, hi], [y, y], "|", color=col, ms=7, mew=1.0)
        a1.text(lo - 1.6, y, _k(v["bottom"]), fontsize=10, va="center", ha="right")
        a1.text(hi + 1.6, y, _k(v["top"]), fontsize=10, va="center", ha="left")
        fx_r = round(fx, -2)
        a2.plot([fx_r / 1000], [y], "o", ms=4.5, color=col)
        a2.text(fx_r / 1000 + 1.4, y, f"${fx_r:,.0f}", fontsize=10, va="center", ha="left")
        lab.append(name)
    for a in (a1, a2):
        a.axhline(2.05, color=RULE, lw=0.5)
        for side in ("top", "right", "left"):
            a.spines[side].set_visible(False)
        a.spines["bottom"].set_linewidth(0.6)
        a.tick_params(axis="y", length=0)
        a.tick_params(axis="x", length=3, width=0.6, labelsize=10)
        a.set_ylim(0.3, 7.6)
    # Mon 23 Nov (render check): from a1's left edge the label ran past a1 into a2 and was clipped; anchored at the
    # figure's left edge (x in figure fraction, y in data), it spans the label column and the empty band of a1
    a1.text(0.005, 1.55, "Every starting month since 1962 (585, overlapping):", fontsize=10, style="italic",
            va="center", ha="left", transform=blended_transform_factory(fig.transFigure, a1.transData), clip_on=False)
    a1.set_yticks(ys + [y_hist])
    a1.set_yticklabels(lab[:5] + ["Median starting month"], fontsize=10)
    a1.set_xlim(57, 133)
    a1.set_xticks([75, 100, 125])
    a1.set_xticklabels(["$75k", "$100k", "$125k"])
    a2.set_xlim(0, 45)
    a2.set_xticks([0, 20, 40])
    a2.set_xticklabels(["$0", "$20k", "$40k"])
    a1.set_title("Bottom and top she could state in 2031", fontsize=10, loc="left", pad=6)
    a2.set_title("Her flexibility and\nanything above the\ntop, Jan 2033", fontsize=10, loc="left", pad=6)   # Thu 26 Nov: three lines since the label column widened
    for path, dpi in outputs:
        if path.endswith(".svg"):
            fig.savefig(path, facecolor="white")
            _svg_font_fallback(path)
        else:
            fig.savefig(path, dpi=dpi, facecolor="white")
    plt.close(fig)
    return [p for p, _ in outputs]


# =================================================================================================================
# Labels and note items (working labels; the notes are written on 27 Nov from these items, not here)
# =================================================================================================================
EXHIBITS = {
    # Every title says the exhibit's scale (fresh reader and coordinator, Wed 11 Nov): Table 1 is the WInS book on the
    # original $300,000 (8g: "Laura's whole plan in miniature"); Figure 1 and Table 2 are her plan for both deposits.
    "t1": {"label": "Table 1",
           "title": "The Final WInS Portfolio at Cost on the Original $300,000",
           # Sat 14 Nov (coherence reader 4): "in Miniature" claimed a faithful reduction (no top-up, no extra
           # Treasuries; VT 8.84% against the plan's 6.58%, 6.63% before Tue 17 Nov evening); the scale stays in the WInS notes' "scaled to the model
           # portfolio", said in 2.0 and 2.1
           # Thu 12 Nov evening: 75 words (was 50). The units column needs its basis (targets set before the first
           # trade; a bond unit is $1,000 of face value) and SKELETON's density cut sends 2.5's two other targets
           # here (bonds within 25 basis points; cash never below $1,000). The costs label now says what the row is,
           # so its item shrinks to the coupon clause; "the full-size plan is Figure 1 and Table 2" goes (the title
           # carries the scale; 2.0 and 2.1 name the plan).
           # Mon 23 Nov (ATTACKS D3, D17; ARGUMENT_TREE branch 1): the reconciliation with the plan is printed once,
           # here, with its one reason (about 50 words in a terse note); the 25-basis-point and cash targets go to
           # 2.5's prose, where the tree puts the price rule ("met at the 5 October check and at every fill"), and the
           # identifiers item drops "VT bought last" (the units cell says it); a source line closes the note (APA). So
           # 110 words (was 75): +50 reconciliation, +12 source, -17 targets, -10 identifiers (counted terse)
           "section": "Section 2 (2-3 pages)", "note_budget_words": 110,
           "note_items": [
               "amounts at cost: units held x price paid on 6-7 Oct 2026 (U.S. Eastern), on the original $300,000 (8g)",
               "units bought / target: targets set before the first trade (Portfolio tab, 2 Oct prices); a bond "
               "unit is $1,000 of face value (8m)",
               # D3's one reason, D17's split rule once; never "after the freeze", "a new standard", "we changed"
               f"reconciled with the plan, both at cost: scaled by 1.5 to $450,000 the portfolio holds "
               f"{D.dollars(D.RECON['book_x15'][0])} of payment Treasuries, {D.dollars(D.RECON['book_x15'][1])} of "
               f"floor and {D.dollars(D.RECON['book_x15'][2])} of VT; the plan in January 2028 holds "
               f"{D.dollars(D.RECON['plan_jan2028'][0])}, {D.dollars(D.RECON['plan_jan2028'][1])} and "
               f"{D.dollars(D.RECON['plan_jan2028'][2])}, because the portfolio was built before the operating "
               # Thu 26 Nov (CHECK_EXHIBITS item 9; NAME_ORDER decision 2): Section 2 glosses the name at first use
               f"reserve was sized (the extra Treasuries, {D.dollars(D.TOPUP_NO_INTEREST)}: more Treasuries bought in "
               "January 2028 so the ten are paid even if cash waiting earns nothing); in both, what is left "
               f"goes about {round(100 * D.RECON['plan_floor_share'])}% to the floor and "
               f"{100 - round(100 * D.RECON['plan_floor_share'])}% to VT, the floor always over half the deposit "
               "(NUMBERS 8 (e), 4; ATTACKS D3, D17)",
               # Mon 16 Nov night (coherence reader 6, L3): the floor is the fund, the bottom is the figure (WORDS)
               # Thu 26 Nov (CHECK_EXHIBITS item 8; NAME_ORDER decision 3, row 30): the floor is the January 2028
               # purchase of more of the fund, not the fund; never "IBTM's floor lot" or "IBTM floor shares"
               "Pays for: each holding's payment (1 January; 23 Oct snapshot); the floor: more of the late-2032 "
               "Treasury fund (IBTM), bought in January 2028, whose payout sets the bottom of her range; in the WInS "
               "portfolio a second IBTM lot stands in for it (TNA l.13; CANON A24; 8g)",
               "costs row: $200 of fees and $1,109.42 of accrued bond interest, repaid with each bond's next coupon "
               "(8g v2)",
               "identifiers: tickers for funds, CUSIPs for bonds (8g, card Q38)",
               # APA 7: the source closes the general note
               "source line: \"Data from the team's WInS trade record, 6-7 Oct 2026; team calculations.\"",
               # registered Sun 22 Nov (NUMBERS 8 (e)); the tree allows it only here and only with its reason
               "if room (not in the budget): rate sensitivity, about $160 per 0.01 point against about $200 for the "
               "payments at the same scale, about four-fifths: matched by date, not duration; the holdings' interest "
               "arrives before the payments, a wait covered because the ten are paid even if cash waiting earns nothing "
               "(NUMBERS 8 (e); NAME_ORDER decision 14; ARGUMENT_TREE "
               "branch 1)"]},
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
           # Tue 17 Nov (coherence reader 7, M1): the reserve's size joins item 4, about 7 words in a terse note, so 84
           # Mon 23 Nov (ARGUMENT_TREE section 6, nugget 16, "Figure 1's note: placed"; APA source line): +16 words
           # for interest on interest, +9 for the source, so 109 (was 84). The $502,605 and the release rule are 3a's
           # prose (D18: "Section 3a states ... and one release rule"); the note keeps the market value (item 4)
           "section": "Section 3, part 3a", "note_budget_words": 109,
           "note_items": [
               # Thu 26 Nov (CHECK_EXHIBITS items 3, 14-17, 20 and section 3): the figure is drawn on the fee-and-margin
               # basis, ink's own count (FACTS l.183; NUMBERS 8h l.1199, l.1275; 8zb), and item 1 names that basis.
               # Mon 16 Nov night (coherence reader 6, M9; WORDS "The standard the payments meet"): the funds' basis
               "1. the condition, defined once: money a bond or fund has already paid out earns nothing while it waits "
               "for its 1 January payment, and pays the short-term Treasury ETF's 0.15% a year; every coupon and fund "
               "payout still counts; and each iBonds Treasury fund's payouts are counted 0.5% smaller, the margin for "
               f"the funds' costs beyond their {100 * D.FUND_FEE:.2f}% fee (such as the cost of trading); fund rows: "
               "what each fund's bonds pay, its net asset value, not a fixed sum (WORDS; 8h; 8zb; NAME_ORDER rows 14, "
               "18, 19, 47)",
               # the $130 between $57,200 and $57,070 is arithmetic, not a registered line: never printed until the
               # numbers owner registers its split (fee against margin)
               f"2. the extra Treasuries reconciled: their "
               f"{D.dollars(D.FIGURE1_NOTE_FACTS['topup_for_no_interest_jan2028'])} (January 2028) buys "
               f"{D.dollars(D.FIGURE1_NOTE_FACTS['topup_face_and_fund_dollars'])} of face value and fund dollars; "
               f"with {D.dollars(D.FIGURE1_NOTE_FACTS['topup_interest_undiscounted'])} of their own interest, added up "
               f"undiscounted, that is {D.dollars(D.FIGURE1_NOTE_FACTS['topup_all_flows_undiscounted'])}; after the "
               f"short-term Treasury ETF's 0.15% a year and the 0.5% margin, "
               f"{D.dollars(D.FIGURE1_TOTALS['backstop_printed'])} reaches the payments and nothing is left: the "
               "standard is met exactly (8h, 8zb)",
               f"3. rounding: rows are rounded to the dollar and add to "
               f"{D.dollars(D.FIGURE1_FOOT[0])} and {D.dollars(D.FIGURE1_FOOT[1])}; the total row is the totals "
               f"of the unrounded figures, {D.dollars(D.FIGURE1_TOTAL_ROW[0])} + {D.dollars(D.FIGURE1_TOTAL_ROW[1])} = "
               f"{D.dollars(D.FIGURE1_TOTAL_ROW[2])} (8zb)",
               f"4. the other basis, today's market rates (one world in the figure, card Q73-035): each own Treasury "
               f"pays its whole {D.dollars(D.FIGURE1_PAYMENT)} and about "
               f"{D.hundreds(D.FIGURE1_NOTE_FACTS['topup_comes_back_1jan2033'])} of the extra Treasuries comes back "
               f"to Laura by 2042 (valued at 1 January 2033): about {D.FIGURE1_PER_DOLLAR} for each $1 the payments "
               "need on 1 January 2033, because the extra Treasuries are sized for cash waiting earning nothing (8h; "
               "card Q31); the operating reserve's size, printed once, here: about "
               f"{D.hundreds(D.FIGURE1_NOTE_FACTS['reserve_1jan2033'])} at today's rates (8h, 8k; NAME_ORDER "
               "decisions 6 and 7: never beside the total row, a ten-year sum of payouts)",
               "5. Treasury par curve of 6 Nov 2026; each payment in its own year's dollars (8h)",
               # Mon 23 Nov: GOLDMINE 16, placed here by the tree (NUMBERS 8a's sentence)
               "6. why the extra Treasuries rise with the years: interest earned on interest is 3% of the 2033 "
               "payment and about 15% of the 2041 and 2042 payments (8a)",
               "7. source line: \"Data from U.S. Department of the Treasury (n.d.); team calculations.\"",
               # Thu 26 Nov (CHECK_EXHIBITS item 17): SECTION_NOTES asks for the release rule; one clause, if room
               # (NUMBERS 8h release table); otherwise 3a's prose carries it
               "8. if room (not in the budget): if the funds cost nothing beyond their fee, the own Treasuries pay "
               f"{D.dollars(D.FIGURE1_TOTALS['own_if_nothing_earns'])}, the extra Treasuries "
               f"{D.dollars(D.FIGURE1_TOTALS['backstop_if_nothing_earns'])}, and "
               f"{D.dollars(D.FIGURE1_NOTE_FACTS['left_after_2042_with_fee'])} is left (8h four-world table); if cash "
               "waiting earns nothing and pays no fee, and the funds cost nothing beyond their fee, the Treasuries pay "
               "about $502,600 against the $500,000 owed (NUMBERS 8 (e)); rows end when the cash reaches Laura (8h "
               "cash table); the top-up, $2,388, completes the ten, in \"Its own Treasury\" (8h); each 1 January, "
               "short-term Treasury ETF money above what every later payment needs can come back (8h release table)"]},
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
           # Tue 17 Nov (coherence reader 7, M13; lay reader 3): 3b's simulated futures' volatility and yield moves join
           # the shares item (about 17 words in a terse note) and 3c's rate past the margin leaves 3c's prose for an
           # if-then item (about 25 words), so 137 (was 95); 3c and 3e give back about 36 words of prose
           # Wed 18 Nov evening (the morning's hand edits, carried): 32 more words in a terse note, so 169 (was 137):
           # 22.2 lines, one Letter page but not between two prose lines (measured: 138 words or fewer, 20.2 lines;
           # 139-156, 21.2; 157 or more, 22.2).
           # Wed 18 Nov evening, second pass (the lead's call, ASK_HUMANS top row, card Q146: no median figure; the
           # coordinator: 156 words or fewer): counted clause by clause against Tue 17 Nov's terse note
           # (REBUILD_2026-11-18_evening.md, "Second pass"), +16 words, not +32: the 7.5%'s source and standing, +7
           # ("(J.P. Morgan's 2027 assumption, above the middle of published forecasts)", J.P. Morgan named once for
           # the 7.5% and the 17.88%, no median, no count); the room under the top, +5 ("used up the room under the top
           # (about 2% centrally)" for "passed the range's 0.5%", "centrally" moved; its two parts are the range-rule
           # item's 0.5% and rounding down); the method, +4 ("(overlapping starting months, past frequencies, never
           # probabilities)" for "(method in 3e)"). So 153: 21.2 lines, between two prose lines again
           # Wed 18 Nov evening, third pass (bond desk 5, H1 and H3; REBUILD_2026-11-18_evening.md, "Third pass"):
           # counted on a full terse rendering of the note, before and after (254 and 255 words), +1, so 154: the
           # curve's date gains "the day trading froze" (+4, H3); the range rule names the fund, "the late-2032 Treasury
           # fund" (+2, H1), and the room item says "the fund's costs ... (about 2% of what it pays" (+4, H1: one fund,
           # bought twice; the 2% is a share of what it pays, in all); paid for by "(our own assumption)" for "(our own
           # assumption, not a market figure)" (-4), "above the top" for "above the stated top" (-1), and the dates item
           # said once ("to the floor's trade day, Mon 3 Jan 2028" for "to January 2028 (traded Mon 3 Jan 2028)", -4);
           # no fact cut. Still 139-156 words, so 21.2 lines (measured)
           # Mon 23 Nov (ATTACKS D7, D20, D22 row 7; card Q210 row 30; ARGUMENT_TREE branch 4 and section 6, nugget 9):
           # the forecast's small effect as a robustness check (+24 words), the assumptions table completed (growth
           # "compounded", the 200,000 simulated futures: +4), the history rows' overlap said where they are named
           # (+14, the old spread item's 6 folded in), and an APA source line (+20); "checked against history" (22
           # words) leaves for 3c's prose (EXHIBITS["t2"]["for_prose"]). Counted terse: 154 + 34 = 188, which takes
           # the table off its page (measured); with the overlap said in 8 words and a 16-word source line, 172
           "section": "Section 3, parts 3b and 3c", "note_budget_words": 172,
           "note_items": [
               # Wed 18 Nov evening, third pass (bond desk 5, H3): the range Table 2 states is dated to the curve of the
               # day trading froze, and never re-sized (on 13 Nov 2026's curve the same rule states $105,000 to $125,000:
               # NUMBERS 4, "On a later curve", disclosed, never re-booked)
               "MODEL, not forecasts; Treasury curve of 6 Nov 2026, the day trading froze (bond desk 5, H3: never "
               "re-sized to a later curve, NUMBERS 4)",
               # Third pass (bond desk 5, H1): the floor and the shares moved into Treasuries buy the same fund, IBTM,
               # the late-2032 Treasury fund (plan.py; CANON C19, D2; Table 1's "2033 and the floor"), so the rule names it
               "each end (the range rule): units of the late-2032 Treasury fund held x its remaining coupons and "
               "principal per unit, "
               "from its published holdings on the trade day, undiscounted, less the fees to 15 Dec 2032 and 0.5%; "
               # Mon 16 Nov night (coherence reader 6, L2): WORDS bans "moved half" and names the history "every
               # starting month since 1962"
               "the bottom rounded down to $5,000; the top = the unrounded bottom plus that of the shares moved into "
               "Treasuries, rounded down once (NUMBERS 0, 3; coherence reader 6, Mon 16 Nov, L2: never \"the moved "
               "half's\")",
               # Tue 17 Nov (coherence reader 7, M13; lay reader 3): the simulated futures' assumptions beside the 7.5%,
               # out of 3e's prose (17.88%) and beside 3b's "about 93 of 100" (0.9 points a year), NUMBERS 0.
               # Wed 18 Nov morning (hand edit; the lead's call on coherence reader 9, H6): the 7.5% named as J.P.
               # Morgan's and placed above the middle of published forecasts; 3e names the assumption in words and points
               # here. Second pass, Wed 18 Nov evening (the lead's call on card Q146, ASK_HUMANS): no median figure and
               # no count of houses, since the median moves with the panel (fifteen, sixteen, seventeen) while "above the
               # middle" holds on every count (check() asserts it, unprinted); J.P. Morgan named once, for the 7.5% and
               # the 17.88% ("its"). Never "the top", "the consensus", "upper third" or a median (words_check). The
               # reviewer's mark follows the source, so the Letter PDF's placeholder note leaves it out (_unmarked)
               f"shares grow {100 * D.SHARE_RETURN:.1f}% a year, compounded, in rows 1 and 3 (J.P. Morgan Asset Management's (2026) 2027 assumption, "
               f"{D.SHARE_RETURN_STANDING}, CANON B15; coherence reader 9, H6, and the lead's calls of Wed 18 Nov "
               "morning and evening (no median figure, card Q146, ASK_HUMANS): 3e names the assumption in words and "
               f"points here) and, in 3b's 200,000 simulated futures, its {100 * D.SHARE_VOL:.2f}% volatility; yields there "
               f"move about {D.YIELD_SD_POINTS:.1f} points a year, independent of shares (our own assumption; "
               "NUMBERS 0)",
               # Tue 17 Nov (lay reader 3: "$120 for each further 0.1%" was one figure too many in 3c's prose): the
               # bond desk's signed form kept for judges as an if-then line (NUMBERS 3; bond desk 4, H1).
               # Tue 17 Nov evening (coherence reader 8, L6): $118 is the central slope, $144 at the house 1-in-20
               # high (NUMBERS 3), so "centrally", never "at most".
               # Wed 18 Nov morning (hand edit; coherence reader 9, H2: "past the range's 0.5%" read as the central
               # threshold): the threshold is the room under the top (WORDS: the 0.5% margin plus the rounding down;
               # 2.32% centrally, NUMBERS 8u, printed "about 2%"), and "centrally" moves to it, where it governs the
               # whole if-then line. Second pass: its two parts are named once, in the range-rule item above ("less the
               # fees ... and 0.5%", "rounded down"; carry_check), so this item prints "about 2% centrally" alone
               # Third pass (bond desk 5, H1): "the fund's costs", one fund (named in the range-rule item), and the 2%
               # is "of what it pays" on both purchases, in all (2.32% = 1 - $115,000 / $117,731, NUMBERS 8u)
               f"if the fund's costs beyond the fees used up the room under the top (about "
               f"{round(100 * D.ROOM_UNDER_TOP)}% of what it pays, centrally, NUMBERS 8u: its two parts, the 0.5% and "
               "the rounding down, are the range-rule item's) and cash waiting earned nothing, the contribution would "
               "fall short of "
               f"the top by about ${round(D.SHORT_PER_TENTH, -1):,.0f} for each further 0.1% (NUMBERS 3, 8u; bond desk "
               "4, H1; coherence reader 9, H2, Wed 18 Nov: \"past the range's 0.5%\" read as the central threshold)",
               # Wed 18 Nov morning (hand edit; SKELETON Exhibits item 3 and row 3e's hand-off): 3e's recast no longer
               # carries the method, so "(method in 3e)" goes and the note says it. Second pass: "past frequencies" for
               # SKELETON's "shares of the past", which the note's "shares" (stocks) could make a reader misread
               # (D.TABLE2_STARTS_METHOD, checked against SKELETON's two ends of the phrase)
               f"starting months: U.S. yields and stocks from the start month ({D.TABLE2_STARTS_METHOD}); 585 "
               "overlapping months, about four independent rate eras, so only the median is shown (NUMBERS 7; card "
               "Q210 rule (c); the lead's decision 3, Mon 23 Nov)",
               # Mon 23 Nov (D22 row 7; nugget 9, "Placed as a robustness check"; D20's last clause; NUMBERS 4's
               # return table and 8v)
               "robustness: the top states $115,000 for any share growth from 4% to 10% a year, and near 5%, the "
               "team's own build from yield, growth and valuation; at 3.1% it is $110,000 (NUMBERS 4, 8v)",
               "inflation row: prices up 5% a year",
               "flexibility: the half of VT promised to no one plus whatever the fund pays above the top, to the "
               "nearest $100 (8i; bond desk 5, H1: one fund)",
               # Third pass: the same three dates said once each (the trade days are the dates the markets run to)
               "each column's own date: the bottom turns on markets to the floor's trade day, Mon 3 Jan 2028; the top "
               "to the January 2031 move's trade day, Thu 2 Jan 2031, before the 2031 meetings; her flexibility to January 2033 (NUMBERS 4; "
               "IPS l.15)",
               "source line: \"Data from U.S. Department of the Treasury (n.d.), Board of Governors of the Federal "
               "Reserve System (n.d.-a) and Shiller (n.d.); team calculations.\""],
           # Mon 23 Nov: out of the note for its budget, for 3c's prose (printed in tables.md under the table)
           "for_prose": [
               f"checked against history: each named world's flexibility ({D.hundreds(D.TABLE2_FLEX_WORLDS[0])} to "
               f"{D.hundreds(D.TABLE2_FLEX_WORLDS[1])}) is below the median starting month's "
               f"({D.hundreds(D.TABLE2_FLEX_MEDIAN)}) (8i, 8j)"]},
    # Mon 23 Nov (the lead's decision 2): Figure 2 replaces Table 2 in the report; Table 2 stays in tables.md as its
    # data and the store's record. The note carries Table 2's items, its two in-table lines (what is held the same;
    # the contribution equals the top) and the history's overlap clause; the panel titles carry two of the three dates.
    # Budget: Table 2's 172 + 26 for the two lines + 4 for the longer source line - 8 for the dates = 194
    "f2": {"label": "Figure 2",
           "title": "In Every Market Tested, All Ten Payments Are Paid in Full",
           "section": "Section 3, parts 3b and 3c", "note_budget_words": 194,
           "note_items": [
               "MODEL, not forecasts: Laura's plan for both deposits ($450,000); Treasury curve of 6 Nov 2026, the day "
               "trading froze (bond desk 5, H3: never re-sized to a later curve, NUMBERS 4)",
               D.TABLE2_HELD_SAME,
               D.TABLE2_RESULT_ROW,
               "each end (the range rule): units of the late-2032 Treasury fund held x its remaining coupons and "
               "principal per unit, from its published holdings on the trade day, undiscounted, less the fees to 15 "
               "Dec 2032 and 0.5%; the bottom rounded down to $5,000; the top = the unrounded bottom plus that of the "
               "shares moved into Treasuries, rounded down once (NUMBERS 0, 3)",
               f"shares grow {100 * D.SHARE_RETURN:.1f}% a year, compounded, in the first and third worlds "
               f"(J.P. Morgan Asset Management's (2026) 2027 assumption, {D.SHARE_RETURN_STANDING}, CANON B15) and, in "
               f"3b's 200,000 simulated futures, its {100 * D.SHARE_VOL:.2f}% volatility; yields there move about "
               f"{D.YIELD_SD_POINTS:.1f} points a year, independent of shares (our own assumption; NUMBERS 0)",
               f"if the fund's costs beyond the fees used up the room under the top (about "
               f"{round(100 * D.ROOM_UNDER_TOP)}% of what it pays, centrally, NUMBERS 8u: its two parts, the 0.5% and "
               "the rounding down, are the range-rule item's) and cash waiting earned nothing, the contribution would "
               f"fall short of the top by about ${round(D.SHORT_PER_TENTH, -1):,.0f} for each further 0.1% (NUMBERS "
               "3, 8u)",
               f"starting months: U.S. yields and stocks from the start month ({D.TABLE2_STARTS_METHOD}); 585 "
               "overlapping months, about four independent rate eras, so only the median is shown (NUMBERS 7; card "
               "Q210 rule (c))",
               "robustness: the top states $115,000 for any share growth from 4% to 10% a year, and near 5%, the "
               "team's own build from yield, growth and valuation; at 3.1% it is $110,000 (NUMBERS 4, 8v)",
               "inflation world: prices up 5% a year",
               "flexibility: the half of VT promised to no one plus whatever the fund pays above the top, to the "
               "nearest $100 (8i; bond desk 5, H1: one fund)",
               # Thu 26 Nov (CHECK_EXHIBITS item 13; NAME_ORDER decision 4): a note may be read before 3b sets up "the
               # move", so it says what moves and when
               "dates: the bottom turns on markets to the floor's trade day, Mon 3 Jan 2028; the top to the January "
               "2031 move's trade day, Thu 2 Jan 2031, before the first 2031 meeting (NUMBERS 4, 8r; IPS l.15)",
               "source line: \"Data from U.S. Department of the Treasury (n.d.), Board of Governors of the Federal "
               "Reserve System (n.d.-a) and Shiller (n.d.); team calculations.\""]},
    # Thu 26 Nov (NAME_ORDER decision 8; CHECK_EXHIBITS item 1): the watch list PRINTS AS TABLE 2 under APA 7
    # numbering (Table 1, Figure 1, Figure 2, then this table); Keel's files keep its working name, "Table 3" (the key
    # "t3", TABLE3_* in exhibit_data.py, the preview's file name and this script's comments)
    "t3": {"label": "Table 2",
           # Thu 12 Nov (SKELETON Exhibits item 4): seven rows in three levels, five columns, one trigger per cell.
           # Fri 13 Nov evening: rows rewritten for three readers and card Q36, refitted to one page (18.4 lines without
           # the note, 21.4 with 40 words; was 18.9 and 21.9 with 35). Mon 16 Nov night: 27.9 lines after that night's
           # hand edits, off the page. Tue 17 Nov: cut back to 21.4 and 18.4, the cut details in D.TABLE3_FOR_3E
           # Mon 23 Nov (ATTACKS D19): seven signals in three lists (the plan; a figure, a fund or a date; her
           # flexibility); the count and the two reasons are unchanged, so the title stands
           "title": "Seven Signals to Watch as 2031 and 2033 Approach; Two Can Change Laura's $450,000 Plan",
           # Tue 17 Nov (coherence reader 7, M13): the building-cost band's source and date join the note; the X-date
           # item is reworded in plain words (lay reader 3). Measured that evening: the table holds one page with a
           # 44-word note and not with 46, so 44 (was 40); a terse note of all five items runs about 44-45 words
           # ("Building costs: DGBAS index, October 2026" is six of them)
           "section": "Section 3, part 3e", "note_budget_words": 44,
           "note_items": [
               # Tue 17 Nov evening (card Q117; the lead's call): "today's rates" dated once, here, as Table 2's note
               # dates its own (six words more for the 27 Nov note to find within its 44)
               f"{D.dollars(D.TOPUP)}: January 2028 money {D.TABLE3_NOTE_TODAY}, the top-up "
               f"({D.dollars(D.TOPUP_TEN_LACK)}) "
               f"and the extra Treasuries ({D.dollars(D.TOPUP_NO_INTEREST)})",
               # Tue 17 Nov (lay reader 3): the cells say "debt-limit deadline"; the note defines it and keeps the
               # term of art once
               # Mon 23 Nov: "(its estimate, else the Congressional Budget Office's)" to the 3e list (7 words for the
               # source line)
               "debt-limit deadline: the day the debt limit would stop the Treasury paying every bill, the \"X-date\"",
               "cash dates: fund payouts, maturities, trade days",
               # Thu 26 Nov (CHECK_EXHIBITS items 2, 5, 6; NUMBERS 8y; WHARTON_NORTH_STAR l.122): the Who gloss and
               # what the broker's statement shows (a fund sends none; never the single IBTM line)
               D.TEAM_WHO_GLOSS,
               "statement: the broker's own, at least quarterly, of a second account holding the building's two IBTM "
               "lots and their paid distributions (8y); rows 6 and 7 are read with it",
               # Mon 16 Nov night (bond desk 4, L10): the 3.57 points (3.60 before Tue 17 Nov evening's re-size) are the standard's, with cash waiting earning
               # nothing (NUMBERS 5; the ladder alone holds to 3.89 points)
               f"payments hold, even if cash waiting earns nothing, to a {D.FALL_TAKES_WHOLE_DEPOSIT:.2f}-point fall "
               "before 2027",
               # Tue 17 Nov (coherence reader 7, M13; case l.146-147): the building-cost band's source and date
               # Wed 18 Nov evening, third pass (bond desk 5, M6 (a)): the cell says "five-year building costs", so the
               # item's name follows it (the same two words)
               # Mon 23 Nov: the building-cost band's source moves into the APA source line (+6 words, paid by the
               # X-date's estimator moving to the 3e list, -7), so 44 as before
               f"source line: \"Data from Directorate-General of Budget, Accounting and Statistics (n.d.), "
               f"construction cost index to October 2026; team calculations.\" ({D.CCI_SOURCE}, 8d)"]},
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


def add_figure2(BT, rep, note_text, top=False):
    rep.figure(EXHIBITS["f2"]["label"], EXHIBITS["f2"]["title"], os.path.join(HERE, "exhibit3_markets.png"),
               width_in=F2_W, note=note_text, top=top)


def add_table2(BT, rep, note_text, top=False):
    widths = [2.50, 0.95, 0.95, 0.95, 1.15]
    aligns = [BT.L, BT.L, BT.R, BT.R, BT.R]
    # Mon 16 Nov evening (card Q14b row 20): first, one line of what is held the same in every row
    rows = [("held", [D.TABLE2_HELD_SAME])]
    rows += [("row", [name] + D.table2_cells(v)) for _, name, v in D.TABLE2_WORLDS]
    rows.append(("spanner", [D.TABLE2_SPREAD_LABEL]))
    rows += [("indent", [label] + D.table2_cells(v)) for label, v in D.TABLE2_HISTORY]
    rows.append(("result", [D.TABLE2_RESULT_ROW]))        # the confidence answer, inside the table
    return apa_table(BT, rep, "t2", D.TABLE2_HEAD_ROW, rows, widths, aligns, note_text, top,
                     spanners=[(2, 3, D.TABLE2_SPANNER)])


def add_table3(BT, rep, note_text, top=False):
    # Widths (6.5 in): the reader column holds "Laura" and "Team" on one line; the last column is the widest, as it
    # carries two parts ("Changes:" and "Never:", in italics).
    # Fri 13 Nov evening: "Who" needs less than "Reader". Tue 17 Nov: 0.05 in from each middle column to the last, which
    # carries the longest cells (rows 1, 2 and 4 each a line shorter); [0.85, 0.48, 1.55, 1.62, 2.00] before
    widths = [0.85, 0.48, 1.50, 1.57, 2.10]
    aligns = [BT.L] * 5
    return apa_table(BT, rep, "t3", D.TABLE3_HEADER, D.table3_rows(), widths, aligns, note_text, top, row_gap=1)


# Words never printed in any exhibit, title or note (Mon 16 Nov evening, lead's brief; CONCEIT V2.2: the conceit stays
# in prose, never in a table or note; WORDS and Book 19's banned words; an iBond fund's payout is never fixed,
# NUMBERS 3). Patterns are matched on whole words, case ignored.
# Mon 16 Nov night: "fixed" is allowed only negated, "not a fixed" (WORDS: an iBond fund pays "not a fixed amount";
# Figure 1's note item 1, coherence reader 6, M9: "its net asset value, not a fixed sum").
# Wed 18 Nov evening: J.P. Morgan's 7.5% is never "the top" of the forecasts, "the consensus" or "upper third" (CANON
# B15; card Q117; the lead's brief), so three more patterns; second pass, a fourth: no median figure (card Q146)
NEVER_WORDS = (r"\bpencil", r"\bink(ed|s)?\b", r"\bendowment", r"\boptimal", r"\bnatural hedge", r"\bfail-safe",
               r"(?<!\bnot a )\bfixed\b", r"\b89%", r"\bupper third", r"\bconsensus",
               r"\btop of (?:the )?(?:published )?(?:forecasts|estimates)",
               # second pass (the lead's call, card Q146): no median figure for the published forecasts anywhere
               r"\bmedian (?:about |of )?[\d.]+%",
               # Mon 23 Nov (ATTACKS D3, D20; ARGUMENT_TREE branches 1-6 "Left out"): the reconciliation's banned
               # framings, the book's scale words, a bare "1 in 20" from history, and the plan's other banned names
               r"\bafter the freeze", r"\bnew standard", r"\bwe changed", r"\bin miniature", r"\btwo-thirds scale",
               r"\bscale model", r"\bglide path", r"\bsecured\b", r"\bportfolio insurance", r"\baverages 7\.5%",
               r"\bduration match", r"\b1[- ]in[- ]20\b(?! (?:simulated )?futures?)", r"\bcushion")

# Wed 18 Nov evening: what Table 2's note must carry since the morning's hand edits (the build stops if one is
# missing), and the stale pointers it must not (3e's recast no longer carries the starting months' method; the
# threshold is the room under the top, not "the range's 0.5%")
# Second pass (the lead's call on card Q146; the coordinator's trim): the phrase without a median; the room under the
# top as "about 2% centrally", its two parts still named in the range-rule item (the last three musts); never a median,
# a count of houses, "shares of the past" (the note's shares are stocks), and J.P. Morgan named once
# Third pass (bond desk 5, H1 and H3): one fund behind the top, named, "the fund's costs" and "what it pays"; the
# curve dated to the day trading froze; never "the funds' costs", "the funds pay" or "two Treasury funds"
T2_NOTE_MUST = (f"J.P. Morgan Asset Management's (2026) 2027 assumption, {D.SHARE_RETURN_STANDING}",
                f"the room under the top (about {round(100 * D.ROOM_UNDER_TOP)}% of what it pays, centrally",
                D.TABLE2_STARTS_METHOD,
                "less the fees to 15 Dec 2032 and 0.5%", "the bottom rounded down to $5,000", "rounded down once",
                "units of the late-2032 Treasury fund held", "the fund's costs beyond the fees",
                "whatever the fund pays above the top", "Treasury curve of 6 Nov 2026, the day trading froze")
T2_NOTE_NEVER = ("method in 3e", "passed the range's 0.5%", "median about", "fifteen", "shares of the past",
                 "upper third", "the funds' costs", "the funds pay", "two Treasury funds")


def carry_check(verbose=True):
    """Fails if Table 2's note items lack one of the Wed 18 Nov morning edits, or keep a pointer they replaced, in the
    items themselves or in the Letter PDF's placeholder note (which leaves the reviewers' marks out)."""
    # Mon 23 Nov: Figure 2 carries Table 2's note in the report; both are checked
    items = "; ".join(EXHIBITS["t2"]["note_items"] + EXHIBITS["f2"]["note_items"])
    placeholder = items_note("t2") + " " + items_note("f2")
    fails = [("must", s, where) for s in T2_NOTE_MUST for where, t in (("items", items), ("placeholder", placeholder))
             if s not in t]
    fails += [("never", s, "items") for s in T2_NOTE_NEVER if s in items]
    fails += [("never", s, "placeholder") for s in T2_NOTE_NEVER if s in placeholder]
    # second pass: J.P. Morgan named once in the note (it covers the 7.5% and the 17.88%)
    fails += [("once", "J.P. Morgan", f"{ex} {where}") for ex in ("t2", "f2")
              for where, t in (("items", "; ".join(EXHIBITS[ex]["note_items"])), ("placeholder", items_note(ex)))
              if t.count("J.P. Morgan") != 1]
    n = 2 * len(T2_NOTE_MUST) + 2 * len(T2_NOTE_NEVER) + 2
    if verbose:
        for kind, s, where in fails:
            print(f"  FAIL     carry     Table 2 note ({where}): {kind} {s!r}")
        print(f"Carry check: Table 2's note, {n} checks, {len(fails)} FAIL")
    return n, fails


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
    out += [("f1 total label", D.FIGURE1_TOTAL_LABEL)]     # Tue 17 Nov (coherence reader 7, M2)
    out += [("t2 head", h) for h in D.TABLE2_HEAD_ROW + [D.TABLE2_SPANNER, D.TABLE2_SPREAD_LABEL]]
    out += [("t2 line", D.TABLE2_HELD_SAME), ("t2 line", D.TABLE2_RESULT_ROW)]
    out += [("t2 world", name) for _, name, _ in D.TABLE2_WORLDS]
    out += [("f2 label", t) for t in ("Every starting month since 1962 (585, overlapping):", "Median starting month",
                                      "Bottom and top she could state in 2031",
                                      "Her flexibility and anything above the top, Jan 2033")]
    out += [(f"{ex} note item", t) for ex in ("t2",) for t in EXHIBITS[ex]["note_items"]]
    out += [("t2 title", EXHIBITS["t2"]["title"])]
    out += [("t3 head", h) for h in D.TABLE3_HEADER + list(D.TABLE3_LEVELS.values())]
    out += [("t3 cell", D.cell_text(c)) for _, cells in D.TABLE3_ROWS for c in cells]
    out += [("t3 for 3e", t) for t in D.TABLE3_FOR_3E]     # Tue 17 Nov: the cut details, read like the cells
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


ADDERS = {"t1": add_table1, "f1": add_figure1, "t2": add_table2, "f2": add_figure2, "t3": add_table3}
# Mon 23 Nov (the lead's decision 2): Figure 2 in the report, Table 2 in tables.md only
ORDER = ("t1", "f1", "f2", "t3")


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
        for ex, name in (("t1", "table1_holdings_2x.png"), ("t3", "table3_monitoring_2x.png")):
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
FILLER_START = {"t1": 0, "f1": 50, "t2": 110, "f2": 110, "t3": 155}


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
                    tall = _measure_tall(BT, ex, note, workdir, variant)
                    if tall["fits_one_page"]:
                        # Wed 18 Nov evening (Table 2 with its 169-word note): taller than the room between two prose
                        # lines but inside Letter's 9-in block, so it fits one page with at most one prose line
                        # beside it. Its height by the same gap method is the page cost; before tonight this case
                        # was printed as "does not fit one page" with a negative overrun
                        n_lines = tall["lines_on_a_tall_page"]
                        res[key] = {"lines": n_lines, "inches": tall["inches"],
                                    "prose_words_displaced": int(round(n_lines * 14.26, -1)), "note_words": words,
                                    "pages_spanned": 1, "fits_one_page": True, "between_two_prose_lines": False,
                                    "under_letter_text_block_inches": round(-tall["over_one_letter_page_inches"], 2),
                                    "method": "fits one Letter page, not between two prose lines: the same gap "
                                              "measured on a page of Letter width, 22 in tall (Letter's text block "
                                              "is 9 in, 23.5 double-spaced lines)"}
                    else:
                        res[key] = {"lines": None, "pages_spanned": b[0] - a[0] + 1, "note_words": words, **tall}
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
            "over_one_letter_page_lines": round((inches - LETTER_BODY_IN) * 72 / 27.6, 1),
            "fits_one_page": inches <= LETTER_BODY_IN,      # Wed 18 Nov evening: was always False
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
    L.append("# The Final Report's exhibits as text (built Mon 23 Nov 2026, Sydney)\n")
    L.append(f"Generated by `build_exhibits.py` from `exhibit_data.py`, which reads `../numbers/results_*_{D.REGISTER_DATE}.json` "
             "(and, for Table 2's note, `results_break_2026-11-18.json`, NUMBERS 8u) "
             "and checks every figure against `../NUMBERS.md` (sections named under each exhibit). Notes for the "
             "store, not report prose: titles are working labels and each note lists the items it must carry; both "
             "are written on 27 Nov. Square brackets mark placeholders. MODEL = Keel's calculation, not a forecast.\n")
    # Mon 23 Nov: the attack decisions and the argument tree, carried into the scripts (charts/FINAL_2026-11-23.md)
    t1m, t3m3 = (measures.get(f"{k}_note_budget", {}) for k in ("t1", "t3"))
    L.append("**Mon 23 Nov (ATTACKS D3, D7, D17, D19, D20, D22; `../ARGUMENT_TREE.md`; card Q210; "
             "`../charts/FINAL_2026-11-23.md`):** Table 1's note reconciles the book (x 1.5) with the plan in January "
             "2028 and states the floor's split once (NUMBERS 8 (e)), and its 25-basis-point and cash targets go to "
             "2.5's prose; Figure 1's note gains interest on interest (8a); Table 2's history rows are the 5th and "
             "95th percentiles of overlapping starting months, never \"1 in 20\", and its note gains the robustness "
             "check, the overlap clause and the 200,000 simulated futures, while the check against history goes to "
             "3c's prose; Table 3 is three lists (the plan, a figure, a fund or a date, her flexibility), the "
             "debt-limit deadline joins row 2 with \"hold and wait\", the yields row moves to row 3, and a new row 6 "
             "carries co-sponsors' pledges with the statement of the late-2032 fund they see in 2031 and before its "
             "December 2032 payout (rows 1, 2, 4, 5 and 7 keep their numbers); every note ends with an APA source "
             "line; more banned words are checked. Measured: Table 1 22.9 lines with a 110-word note; Table 2 23.2 with "
             "172; Table 3 22.4 with 44.**\n")
    # Mon 23 Nov, later: the lead's decisions after the fresh read (charts/fresh_read_2026-11-23/), live measures
    f1m, f2m = measures.get("f1_note_budget", {}), measures.get("f2_note_budget", {})
    L.append("**Mon 23 Nov, later: the lead's decisions after two fresh readers (`../charts/fresh_read_2026-11-23/`; "
             "`../charts/FINAL_2026-11-23.md`, \"Decisions applied\"):** Figure 1 stays the reserve schedule and the "
             "money picture stays a candidate; Figure 2, Table 2 drawn as ranges and dots, replaces Table 2 in the "
             "report, its APA title saying that all ten payments are paid in every market tested, the bottom and top "
             "printed at each end of each range; Table 2 stays below as Figure 2's data and the store's record; history "
             "is the median starting month alone (card Q210 rule (c); NUMBERS registers no highest starting month); "
             "Table 3 row 5's limit is the first 2031 meeting and every \"Changes\" cell names an act (card Q222 row "
             "38); every source line takes the works-cited draft's author and date form. Measured: Table 1 "
             + str(t1m.get("lines")) + " lines; Figure 1 " + str(f1m.get("lines")) + "; Figure 2 "
             + str(f2m.get("lines")) + " with a " + str(EXHIBITS["f2"]["note_budget_words"]) + "-word note; Table 3 "
             + str(t3m3.get("lines")) + ".**\n")
    # Mon 16 Nov night: the hand edits of that night (coherence reader 6; bond desk 4), carried into the scripts
    L.append("**Hand edits, Mon 16 Nov night (coherence reader 6; bond desk 4), each marked in place below: carried into "
             "`exhibit_data.py` and `build_exhibits.py` the same night, so a rebuild keeps them; Table 3's page fit is "
             "re-measured (its page cost below), since rows 4, 5 and 7 are longer, and Table 2's, since its printed "
             "head now reads \"" + D.TABLE2_FLEX_HEAD + "\" as well (SKELETON Exhibits item 3).**\n")
    # Tue 17 Nov evening, later: the two dated lines below keep the count measured on their day (21.4); the line for
    # coherence reader 8 carries tonight's measure
    L.append("**Tue 17 Nov: Table 3 cut back to one page (27.9 to " + "21.4"
             + " double-spaced lines with its note), every row's signal, trigger, change and \"never\" kept and no "
             "figure changed; each detail cut is listed under the table for 3e's notes; row 5's \"[x]%\" is now NUMBERS "
             "4's trade-day limit, 0.5% (`REBUILD_2026-11-17.md`).**\n")
    # Tue 17 Nov evening: coherence reader 7 (M1, M2, M3, M13) and lay reader 3, applied in the scripts
    L.append("**Tue 17 Nov evening (coherence reader 7; lay reader 3; `../research/panel/2026-11-17_fixes_applied.md`):** "
             "Figure 1's total row is labelled \"" + D.FIGURE1_TOTAL_LABEL + "\", a ten-year sum of payouts, never the "
             "reserve's size, which note item 4 now carries once at today's rates (M1, M2); Table 2's note gains the "
             "simulated futures' volatility and yield moves (M13) and 3c's rate past the margin as an if-then item (lay "
             "reader 3); Table 3 says \"debt-limit deadline\" for the X-date, names the 0.5% margin in row 4 (M3), says "
             "\"Never: a sale of shares\" for \"Never: VT\" and the Taiwan dollar's move once, as 10% stronger, and its "
             "note names the building-cost band's source and date (M13); row 6 reads \"the top to Jan 2031\" so the "
             "table stays on one page (" + "21.4" + " lines with a "
             + str(EXHIBITS["t3"]["note_budget_words"]) + "-word note).\n")
    # Tue 17 Nov evening, later: coherence reader 8 and the evening lay reader, applied in the scripts
    L.append("**Tue 17 Nov evening, later (coherence reader 8; the evening lay reader; "
             "`../research/panel/2026-11-17_fixes_applied_evening.md`):** Table 3 row 1 says who fills the gap and what "
             "is never sold; row 4 names the 0.5% margin the payments and the range each carry, with what it covers in "
             "the 3e list (M1); row 6 says the bottom is set in January 2028; the note dates today's rates once; Table "
             "2's note says \"centrally\" for the rate past the margin (L6). Table 3 measures "
             + str(measures.get("t3_note_budget", {}).get("lines")) + " lines with a "
             + str(EXHIBITS["t3"]["note_budget_words"]) + "-word note.\n")
    # Wed 18 Nov evening: the morning's hand edits to Table 2's note, carried into the scripts (carry_check). The first
    # pass's line is kept as it was measured (static); the second pass's line carries tonight's measures
    t2m, t3m = measures.get("t2_note_budget", {}), measures.get("t3_note_budget", {})
    L.append("**Wed 18 Nov morning hand edits to Table 2's note, carried Wed 18 Nov evening (`REBUILD_2026-11-18_evening.md`; "
             "the lead's calls on coherence reader 9, H2 and H6; SKELETON Exhibits item 3 and row 3e's hand-off):** the "
             "7.5% named as J.P. Morgan's 2027 assumption for world shares and placed above the middle of published "
             "forecasts, never \"the top\", \"the consensus\" or \"upper third\"; the rate past the margin from the room "
             "under the top (the 0.5% margin plus the rounding down, about 2% centrally, NUMBERS 8u); the starting "
             "months' method in the note, since 3e's recast no longer carries it. Table 2 then measured 22.2 lines with "
             "a 169-word note (was 20.2 with 137), one Letter page but not between two prose lines.\n")
    t2_where = (", one Letter page but not between two prose lines" if t2m.get("between_two_prose_lines") is False
                else ", between two prose lines on one Letter page")
    # Wed 18 Nov evening, third pass: the second pass's line is kept as it was measured (static, like the first's)
    L.append("**Wed 18 Nov evening, second pass (the lead's call, `../../pm/ASK_HUMANS.md` top row, card Q146; the "
             "coordinator's trim):** no median figure and no count of houses: \"J.P. Morgan's 2027 assumption, "
             + D.SHARE_RETURN_STANDING + "\", since the median moves with the panel while \"above the middle\" holds on "
             "every count (checked, not printed); J.P. Morgan named once, for the 7.5% and the 17.88%; the room under "
             "the top printed \"about 2% centrally\", its two parts named in the range-rule item; the method "
             "\"overlapping starting months, past frequencies, never probabilities\" (\"shares of the past\" could be "
             "read as stocks). Table 2 measured 21.2 lines with a 153-word note, between two prose lines on one Letter "
             "page; Table 3 21.9 lines with its 44-word note, one Letter page; no figure changed.\n")
    # Wed 18 Nov evening, third pass (the lead's call on Table 3 row 4; bond desk 5): this line carries tonight's
    # measures
    L.append("**Wed 18 Nov evening, third pass (the lead's call on Table 3 row 4, NUMBERS 3 \"An early end of the "
             "late-2032 fund after the move\" and 9; bond desk 5, `../research/panel/2026-11-18_bond_desk_5_3c_table3_3e.md`, "
             "H1, H2, H3, M5, M6):** Table 3 row 4 says what the 0.5% margin pays and what it cannot, in the numbers "
             "owner's words fitted to four lines (\"trading costs from the 0.5% margin, lost interest from what its "
             "cash earns\"), the 3e list split the same way with the early end's size; Table 2's note names the one "
             "fund behind the top, the late-2032 Treasury fund, bought twice (\"the fund's costs\", \"about 2% of "
             "what it pays\"), and dates its curve to the day trading froze; row 7 says \"her $115,000 part\", "
             "\"shares at 7.5%\" for the $28,700, \"alone\" for the currency's $11,500 and \"five-year\" for the "
             "building-cost band, the joint move (22.3% in the middle span) and the two index readings in the 3e list; row 5 "
             "says \"funds\". Table 2 measured 21.2 lines with a 154-word note, between two prose lines on one Letter page; "
             "Table 3 21.9 lines with its 44-word note, one Letter page.\n")

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
        # Wed 18 Nov evening: an exhibit inside Letter's 9-in block but too tall to sit between two prose lines
        where = (f", one Letter page but not between two prose lines ({m.get('under_letter_text_block_inches')} in "
                 f"under Letter's 9-in text block)" if m.get("between_two_prose_lines") is False else "")
        return (f"Page cost in Wharton's format (Letter, 12 pt, double-spaced text, single-spaced body): "
                f"**{m.get('lines')} double-spaced lines** with a {m.get('note_words')}-word note "
                f"(about {m.get('prose_words_displaced')} words of prose{where}); "
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
             "`composition_1jan2033_base` and `fee_and_margin` (NUMBERS 8zb, the printed basis since Thu 26 Nov; `fee`, 8h's "
             "old basis, for note item 8; `base`, today's market rates, for note item 4 only); cash dates "
             "and the note's reconciliation from "
             f"`results_topup_{D.REGISTER_DATE}.json` (Fri 13 Nov; re-run Sun 15 Nov evening). The figure is `figure1_reserve.svg`; its numbers as text:\n")
    rows = []
    for r in D.FIGURE1_ROWS:
        arrives = D.cash_words(r)             # Fri 13 Nov: the cash date (8h's cash table), not the fund's end date
        if r["wait_words"]:
            arrives += f" (waits {r['wait_words']})"
        rows.append([r["year"], r["holding"], "Treasury bond" if r["kind"] == "T-bond" else D.FUND_TYPE,
                     arrives, D.dollars(r["own_printed"]), D.dollars(r["backstop_printed"]), ""])
    # Mon 16 Nov evening (card Q73): one world; the heads print the sum and the total row adds up exactly
    own_tot, extra_tot, sum_tot = (D.dollars(v) for v in D.FIGURE1_TOTAL_ROW)
    # Tue 17 Nov (coherence reader 7, M2): the row's label says it is a sum of payouts 2033-2042, not a size
    rows.append([f"**{D.FIGURE1_TOTAL_LABEL}**", "", "", "", f"**{own_tot}**", f"**+ {extra_tot}**",
                 f"**= {sum_tot}**"])
    hd = D.FIGURE1_HEADS
    L.append(_md_table([hd["payment"] + " (1 Jan)", "Paid from", "Type", "Cash arrives", " ".join(hd["c2"]),
                        f"{hd['plus']} {' '.join(hd['c3'])}", f"{hd['equals']} {hd['sum']}"], rows,
                       right={4, 5, 6}) + "\n")
    L.append(f"As drawn (Mon 16 Nov evening, card Q73's three fixes; basis changed Thu 26 Nov, CHECK_EXHIBITS item 3): "
             f"one world, cash waiting earning nothing after the 0.15% fee on waiting money, with every iBonds Treasury "
             f"fund flow 0.5% smaller (the `fee_and_margin` block, NUMBERS 8h and 8zb; it was the \"fee\" block, "
             f"$444,080 + $55,920 with $1,177 left); the heads read \"{' '.join(hd['c2'])} {hd['plus']} "
             f"{' '.join(hd['c3'])} {hd['equals']} {hd['sum']}\" and the total row \"{D.FIGURE1_TOTAL_LABEL}: "
             f"{own_tot} {hd['plus']} {extra_tot} "
             f"{hd['equals']} {sum_tot}\" (Tue 17 Nov, coherence reader 7, M2: what the ten payments are paid over "
             f"2033-2042, summed undiscounted, never the reserve's size, which is note item 4's; 8zb's totals of "
             f"unrounded figures; the rows, rounded, add to "
             f"{D.dollars(D.FIGURE1_FOOT[0])} and {D.dollars(D.FIGURE1_FOOT[1])}, note item 3); the \"At today's "
             f"market rates\" column ($50,000 ten times) is now note item 4; no axis break (the timeline runs unbroken "
             f"from January 2027 to 2042); a dotted line and \"waits 10.5 months\" / \"waits 7.5 months\" mark the two "
             f"long waits; legend: {D.FIGURE1_LEGEND[0]} (coherence reader 6, Mon 16 Nov, L2: the figure's own Type "
             f"column); {'; '.join(D.FIGURE1_LEGEND[1:])}.\n")
    L.append("Note items: " + "; ".join(EXHIBITS["f1"]["note_items"]) + ".\n")
    L.append(cost("f1") + "\n")

    # Figure 2 (Mon 23 Nov, the lead's decision 2)
    L.append(f"## {EXHIBITS['f2']['label']}. {EXHIBITS['f2']['title']} (the lead's title, Mon 23 Nov)\n")
    L.append(f"{EXHIBITS['f2']['section']}. In the report in place of Table 2: `figure2_markets.svg`, "
             "`figure2_markets_2x.png`, `exhibit3_markets.png` (300 dpi, the Letter build's). Data: Table 2 below "
             "(NUMBERS 8i, 8j). Left panel: the bottom and top she could state in each world, each printed at its end; "
             "right panel: her flexibility and anything above the top, January 2033, to the nearest $100; the history "
             "row is the median starting month alone (card Q210 rule (c)).\n")
    L.append("Note items: " + "; ".join(EXHIBITS["f2"]["note_items"]) + ".\n")
    L.append(cost("f2") + "\n")

    # Table 2
    L.append(f"## Old {EXHIBITS['t2']['label']} (Figure 2's data and the store's record; not in the report since Mon 23 "
             f"Nov; the label \"Table 2\" now prints on the watch list). {EXHIBITS['t2']['title']}\n")
    L.append(f"{EXHIBITS['t2']['section']}. Source: NUMBERS 8i (MODEL; the spread of the flexibility from 8j's joint "
             f"replay column), `results_joint_stress_{D.REGISTER_DATE}.json`.\n")
    rows = [[name] + D.table2_cells(v) for _, name, v in D.TABLE2_WORLDS]
    rows.append([f"*{D.TABLE2_SPREAD_LABEL}*", "", "", "", ""])
    rows += [[f"&nbsp;&nbsp;{label}"] + D.table2_cells(v) for label, v in D.TABLE2_HISTORY]
    L.append(f"First line of the table, full width under the heads, a thin rule below (Mon 16 Nov evening, card Q14b "
             f"row 20): \"{D.TABLE2_HELD_SAME}\" (checked: one design, one range-rule stamp and the $150,000 2028 "
             "deposit in every world of the results file; 8i, NUMBERS 0).\n")
    L.append(_md_table(D.TABLE2_HEADER, rows, right={2, 3, 4}) + "\n")
    L.append(f"Last row of the table, full width under a rule: \"{D.TABLE2_RESULT_ROW}\" (coherence reader 6, Mon 16 "
             "Nov, L2 and M6, also the header, the first row and the history label above: WORDS's names) (checked: all "
             "five worlds and 100% of the 585 replays, 8i and 8j).\n")
    L.append("Note items: " + "; ".join(EXHIBITS["t2"]["note_items"]) + ".\n")
    L.append("For 3c's prose, not the note (Mon 23 Nov, the note's budget): " + "; ".join(EXHIBITS["t2"]["for_prose"])
             + ".\n")
    L.append("Page cost: not in the report since Mon 23 Nov (Figure 2 is); last measured 23.2 lines with a 172-word "
             "note.\n")

    # Table 3
    L.append(f"## {EXHIBITS['t3']['label']} in print (Keel files: Table 3, the watch list). {EXHIBITS['t3']['title']} "
             "(working title)\n")
    L.append(f"{EXHIBITS['t3']['section']}. Source: SKELETON Exhibits item 4 (Thu 12 Nov spec: card Q30's cut, the bond "
             "reader of Wed 11 Nov, Keel's definitions of the two reasons); every figure from NUMBERS 2, 5, 8d, 8h and "
             "8j (and row 5's limit from NUMBERS 4) through `exhibit_data.py`, checked. Single-spaced; each level is an "
             "italic row across the table; the last column prints \"Changes:\" and \"Never:\" in italics, in one run of "
             "text (a line break between them would cost a line a row). Column widths 0.85, 0.48, 1.50, 1.57 and 2.10 "
             "in (Tue 17 Nov; was 0.85, 0.48, 1.55, 1.62 and 2.00).\n")
    rows = []
    for kind, cells in D.table3_rows():
        if kind == "spanner":
            rows.append([f"*{cells[0]}*", "", "", "", ""])
        else:
            rows.append([D.cell_text(c) if not isinstance(c, list) else
                         "".join(f"*{t}*" if it else ("<br>" if t == "\n" else t) for t, it in c) for c in cells])
    L.append(_md_table(D.TABLE3_HEADER, rows, right=set()) + "\n")
    L.append("Note items: " + "; ".join(EXHIBITS["t3"]["note_items"]) + ".\n")
    L.append("Mon 16 Nov hand edits to Table 3 (carried into `exhibit_data.py` the same night; on Tue 17 Nov rows 1, 2, "
             "4, 5 and 7 were cut back to fit the page, their details listed below): "
             "row 1, the missed deposit's cost on both bases (coherence reader 6 and bond desk 4, M7, L5; L5's action "
             "wording declined: card Q34 keeps the later money's order in 3e's prose); row 2, \"payments ... "
             "restated\" corrected (bond desk 4, L6); row 4, the frozen name of the waiting fund (coherence reader 6, "
             "L1: TNA l.5, WN l.17), filings read in any year and a dated missing-notice trigger (bond desk 4, M5), one "
             "action per event and no \"Treasury due by 15 December\", which WInS does not list for 2033 or 2035 (bond "
             "desk 4, M4; coherence reader 6, L17); row 5, a stressed-trade-day trigger, its distance then a placeholder, "
             "not yet in NUMBERS (bond desk 4, M6; 0.5% since Tue 17 Nov, NUMBERS 4); row 6, \"the 2031 move\" alone banned (coherence reader 6, L2); row 7, one "
             "reading of \"10% stronger\" (8j: 10% more US dollars) and a \"carry on while\" that is a condition "
             "(bond desk 4, M7; its building-cost trigger declined: SKELETON's Sat 14 Nov decision, CANON A34); the "
             "note names its basis (bond desk 4, L10; the ladder alone holds to 3.89 points, NUMBERS 5).\n")
    # Tue 17 Nov: the details cut to fit the page, for 3e's notes (D.TABLE3_FOR_3E, checked in D.check())
    L.append("**For 3e's notes (Tue 17 Nov; rows 4, 5 and 7 added to on Wed 18 Nov evening, third pass): what left "
             "Table 3's cells to fit one page, not printed in the table or its note, never lost.**\n")
    L.append("\n".join(f"- {t}." for t in D.TABLE3_FOR_3E) + "\n")
    L.append("Not a row: custody (one line of 3e prose, SKELETON item 4 (c)). IBTA's early end in 2021 is in the list "
             "above (row 4's window and cash), an example of row 4's \"early end\" for 3e's prose, never in the table "
             "or its note.\n")
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
    _, carry_fails = carry_check()          # Wed 18 Nov evening: the morning's hand edits to Table 2's note
    if carry_fails:
        sys.exit("Stopped: Table 2's note lacks a Wed 18 Nov edit or keeps a pointer it replaced (listed above).")
    print("font:", FONT)
    print(figure1([(os.path.join(HERE, "figure1_reserve.svg"), None),
                   (os.path.join(HERE, "figure1_reserve_2x.png"), PREVIEW_DPI),
                   (os.path.join(HERE, "exhibit2_reserve.png"), PRINT_DPI)]))
    print(figure2([(os.path.join(HERE, "figure2_markets.svg"), None),
                   (os.path.join(HERE, "figure2_markets_2x.png"), PREVIEW_DPI),
                   (os.path.join(HERE, "exhibit3_markets.png"), PRINT_DPI)]))
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
    m["_built"] = (f"Mon 23 Nov 2026 (Sydney): ATTACKS D3, D7, D17, D19, D20, D22 and the argument tree carried; "
                   f"register of {D.REGISTER_DATE} (results_*_{D.REGISTER_DATE}.json; NUMBERS 8 (e) for Table 1's note; "
                   "Table 3 row 5's limit from NUMBERS 4, Tue 17 Nov; Table 2's note from NUMBERS 8u and 8v, second pass, "
                   "results_break_2026-11-18.json, Wed 18 Nov; third pass: Table 3 row 4 and the 3e list from NUMBERS 3's "
                   "early end, results_fund_exit_2026-11-18.json, and 8q's strong-Taiwan-dollar spans, "
                   "results_strong_twd_windows_2026-11-18.json)")
    with open(os.path.join(HERE, "measurements.json"), "w") as fh:
        json.dump(m, fh, indent=1)
    print(json.dumps(m, indent=1))
    tables_md(m)
    print("tables.md written")


if __name__ == "__main__":
    main(sys.argv)
