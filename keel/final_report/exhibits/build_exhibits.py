"""Build the Final Report's four exhibits on the register of Tue 10 Nov 2026 (rebuilt Fri 13 Nov 2026 morning, Sydney).

    python3 -I keel/final_report/exhibits/build_exhibits.py            everything below (about a minute)
    python3 -I keel/final_report/exhibits/build_exhibits.py figure     Figure 1 only

Every figure comes from exhibit_data.py, which reads the results files in ../numbers/ and checks each figure against
NUMBERS.md; this script stops if that check fails. Writes, next to this file:

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
# length is its real holding time. The right-hand head is the question its two columns answer.
W, H = 6.5, 3.56
X_YEAR = 0.0                       # payment year, left-aligned
AX_L, AX_R = 0.62, 3.70            # the timeline
C1_R, C2_R, C3_R = 4.88, 5.66, 6.50  # right edges of the three number columns
SPAN_L = 4.96                      # left end of the rule under the question (over columns 2 and 3)
T0, T1 = 2027.0, 2042.10           # 1 January 2027 at the left edge; the last payment, 1 January 2042, near the right
YEAR_LABELS = (2027, 2030, 2033, 2036, 2039, 2042)
HEAD_RULE = 0.79
ROW0, ROW_H, BAR_H = 0.83, 0.222, 0.15
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

    # ---- column heads: four lines; the lowest (L4) sits on the head rule ----
    L4 = HEAD_RULE - 0.06
    L3, L2, L1 = L4 - LINE, L4 - 2 * LINE - 0.06, L4 - 3 * LINE - 0.06
    text(X_YEAR, L4, hd["payment"], va="bottom", weight="bold", size=FS_HEAD)
    text((AX_L + AX_R) / 2, L3, hd["timeline"], ha="center", va="bottom", weight="bold", size=FS_HEAD)
    for yr in YEAR_LABELS:
        text(X(yr), L4, str(yr), ha="left" if yr == T0 else "center", va="bottom", size=FS_LAB)
    text(C1_R, L3, hd["c1"][0], ha="right", va="bottom", weight="bold", size=FS_HEAD)
    text(C1_R, L4, hd["c1"][1], ha="right", va="bottom", weight="bold", size=FS_HEAD)
    # the question the two right-hand columns answer, over a rule that groups them
    # Fri 13 Nov evening: right-aligned on the last column, since "If cash waiting earns nothing," is wider than the
    # rule's span; it sits two lines above the other heads, so it may run left over "At today's market rates"
    text(C3_R, L1, hd["question"][0], ha="right", va="bottom", weight="bold", size=FS_HEAD)
    text(C3_R, L2, hd["question"][1], ha="right", va="bottom", weight="bold", size=FS_HEAD)
    ax.plot([SPAN_L, C3_R], [L2 + 0.035, L2 + 0.035], color=INK, linewidth=0.6)
    for x_r, (a, b) in ((C2_R, hd["c2"]), (C3_R, hd["c3"])):
        if a:
            text(x_r, L3, a, ha="right", va="bottom", weight="bold", size=FS_HEAD)
        text(x_r, L4, b, ha="right", va="bottom", weight="bold", size=FS_HEAD)
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
            text(X(r["year"]) + 0.05, y, f"waits {r['wait_words']}", size=FS_LAB, zorder=5,
                 bbox=dict(facecolor="white", edgecolor="none", pad=0.4))
        text(X_YEAR, y, str(r["year"]))
        text(C1_R, y, D.dollars(r["at_forwards"]), ha="right")
        text(C2_R, y, D.dollars(r["own_if_nothing_earns"]), ha="right")
        text(C3_R, y, D.dollars(r["backstop_if_nothing_earns"]), ha="right")

    # ---- totals (the register's totals of unrounded figures, NUMBERS 8h) ----
    T = D.FIGURE1_TOTALS
    ax.plot([0, W], [last + 0.03, last + 0.03], color=INK, linewidth=0.6)
    yt = last + 0.03 + ROW_H / 2 + 0.01
    text(X_YEAR, yt, "Total")
    text(C1_R, yt, D.dollars(T["at_forwards"]), ha="right")
    text(C2_R, yt, D.dollars(T["own_if_nothing_earns"]), ha="right")
    text(C3_R, yt, D.dollars(T["backstop_if_nothing_earns"]), ha="right")

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
               "Pays for: each holding's payment (1 January; 23 Oct snapshot); the floor: the least Laura can promise "
               "co-sponsors in 2031, IBTM standing in (TNA l.13, CANON A24, 8g)",
               "costs row: $200 of fees and $1,109.42 of accrued bond interest, repaid with each bond's next coupon "
               "(8g v2)",
               "identifiers: tickers for funds, CUSIPs for bonds (8g, card Q38); VT bought last, with the cash left "
               "(8m)"]},
    "f1": {"label": "Figure 1",
           # Fri 13 Nov evening: WORDS.md's names ("the extra Treasuries", "cash waiting earns nothing"; the top-up is
           # the $2,388 that completes the ten, IPS l.13); the point first, then the scale
           "title": "Each Payment Has Its Own Treasury, and Extra Treasuries From the 2028 Deposit Pay Any Gap if Cash "
                    "Waiting Earns Nothing (Laura's Plan for Both Deposits, $450,000, Modelled)",
           # Fri 13 Nov (bond reader, 12 Nov): the definition and the reconciliation join, in priority order. The
           # budget stays 60 words: items 1 to 4 fit it in a terse note (counted Fri 13 Nov, the title already
           # carrying "$450,000" and "Modelled"); 5 and 6 only if room, else 3a's prose (the bars show the cash dates)
           "section": "Section 3, part 3a", "note_budget_words": 60,
           "note_items": [
               "1. \"if cash waiting earns nothing\", defined once: money already received earns nothing while it "
               "waits; every coupon and fund payout still counts (WORDS; 8h)",
               "2. the last column reconciled: the extra Treasuries' $35,894 (January 2028) buys $36,867 at face; "
               "with $19,143 of their own interest, summed undiscounted, they pay $55,920 after $90 of the waiting "
               "fund's 0.15% fee; at today's rates about $45,500 comes back (1 Jan 2033 money) (8h)",
               f"3. the ratio with its reason: about {D.FIGURE1_PER_DOLLAR} for each $1 on 1 Jan 2033 at today's "
               "rates, because the extra Treasuries are sized for cash waiting earning nothing (8h; card Q31)",
               "4. Treasury par curve of 6 Nov 2026; each payment in its own year's dollars (8h)",
               "5. bars end when the cash reaches Laura: a fund a few days after its 15 December end, a bond on its "
               "maturity date or the next business day (8h cash table)",
               "6. if room: paid in every historical rate stretch tested (585 starts, 1962-2010; NUMBERS 2); the "
               "top-up, $2,388, completes the ten, in \"Its own Treasury\"; the floor's IBTM shares are a separate lot "
               "from the 2033 payment's; rows may not add because of rounding"]},
    "t2": {"label": "Table 2",
           "title": "Laura's Plan for Both Deposits ($450,000) in Five Markets and in History Since 1962, Modelled",
           "section": "Section 3, parts 3b and 3c", "note_budget_words": 45,
           "note_items": [
               "MODEL, not forecasts; Treasury curve of 6 Nov 2026",
               "shares 7.5% a year in rows 1 and 3",
               "replays: U.S. yields and stocks from the start month (method in 3e)",
               "inflation row: prices up 5% a year",
               "flexibility: the half of VT promised to no one plus whatever the funds pay above the stated top, to "
               "the nearest $100 (8i)",
               "spread rows: each column's own percentile",
               "each row is a different market before January 2028; within each, the bottom is fixed from then"]},
    "t3": {"label": "Table 3",
           # Thu 12 Nov (SKELETON Exhibits item 4): seven rows in three levels, five columns, one trigger per cell.
           # Fri 13 Nov evening: rows rewritten for three readers and card Q36, refitted to one page (18.4 lines without
           # the note, 21.4 with 40 words; was 18.9 and 21.9 with 35)
           "title": "Seven Signals to Watch as 2031 and 2033 Approach; Two Can Change Laura's $450,000 Plan",
           "section": "Section 3, part 3e", "note_budget_words": 40,
           "note_items": [
               "$38,282: January 2028 money at today's rates, the top-up ($2,388) and the extra Treasuries ($35,894)",
               "X-date: when the debt limit stops the Treasury paying every bill (its estimate, else the "
               "Congressional Budget Office's)",
               "cash dates: fund payouts, maturities, trade days",
               "payments hold to a 3.60-point fall before 2027"]},
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
    spanner) or result (one plain cell across the table, a rule above: a finding that holds for every row). Borders:
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
        if kind in ("spanner", "result"):
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
    rows = [("row", [name] + D.table2_cells(v)) for _, name, v in D.TABLE2_WORLDS]
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


ADDERS = {"t1": add_table1, "f1": add_figure1, "t2": add_table2, "t3": add_table3}
ORDER = ("t1", "f1", "t2", "t3")


def items_note(ex):
    return "[Note to carry: " + "; ".join(EXHIBITS[ex]["note_items"]) + ".]"


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
            else:
                # Table 1 since Thu 12 Nov evening: its note-items placeholder (about 110 words, longer than the
                # 75-word budget) pushes the line after it to the next page; the whole table and note sit on page pi,
                # so stop under the last text line above the page number.
                body = [x for x in BT.lines_of(pages[pi]["words"]) if x["top"] < pages[pi]["height"] - 72]
                assert pj == pi + 1 and body and body[-1]["text"].endswith(".]"), f"{ex} spans pages"
                bottom = body[-1]["bottom"] + 6
            img = page.crop((66, top, page.width - 66, bottom)).to_image(resolution=PREVIEW_DPI)
            img.save(os.path.join(HERE, name))
            out[ex] = name
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
            rep = BT.Report(paper="letter")
            rep.para("Above the exhibit.")
            ADDERS[ex](BT, rep, f.words(words) + "." if words else None)
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
                    res[key] = {"lines": None, "pages_spanned": b[0] - a[0] + 1, "note_words": words}
    return res


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
    L.append("# The Final Report's exhibits as text (built Fri 13 Nov 2026 morning, Sydney)\n")
    L.append("Generated by `build_exhibits.py` from `exhibit_data.py`, which reads `../numbers/results_*_2026-11-10.json` "
             "and checks every figure against `../NUMBERS.md` (sections named under each exhibit). Notes for the "
             "store, not report prose: titles are working labels and each note lists the items it must carry; both "
             "are written on 27 Nov. Square brackets mark placeholders. MODEL = Keel's calculation, not a forecast.\n")

    def cost(ex):
        m = measures.get(f"{ex}_note_budget", {})
        return (f"Page cost in Wharton's format (Letter, 12 pt, double-spaced text, single-spaced body): "
                f"**{m.get('lines')} double-spaced lines** with a {m.get('note_words')}-word note "
                f"(about {m.get('prose_words_displaced')} words of prose); "
                f"{measures.get(f'{ex}_no_note', {}).get('lines')} lines without a note.")

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
    L.append(f"{EXHIBITS['f1']['section']}. Source: NUMBERS 8h (MODEL), `results_reserve_2026-11-10.json` blocks "
             "`composition_1jan2033_base`, `base` and `fee`; cash dates and the note's reconciliation from "
             "`results_topup_2026-11-13.json` (Fri 13 Nov). The figure is `figure1_reserve.svg`; its numbers as text:\n")
    rows = []
    for r in D.FIGURE1_ROWS:
        arrives = D.cash_words(r)             # Fri 13 Nov: the cash date (8h's cash table), not the fund's end date
        if r["wait_words"]:
            arrives += f" (waits {r['wait_words']})"
        rows.append([r["year"], r["holding"], "Treasury bond" if r["kind"] == "T-bond" else "iBond Treasury fund",
                     arrives, D.dollars(r["at_forwards"]), D.dollars(r["own_if_nothing_earns"]),
                     D.dollars(r["backstop_if_nothing_earns"])])
    T = D.FIGURE1_TOTALS
    rows.append(["**Total**", "", "", "", f"**{D.dollars(T['at_forwards'])}**",
                 f"**{D.dollars(T['own_if_nothing_earns'])}**", f"**{D.dollars(T['backstop_if_nothing_earns'])}**"])
    hd = D.FIGURE1_HEADS
    q = " ".join(hd["question"])
    L.append(_md_table([hd["payment"] + " (1 Jan)", "Paid from", "Type", "Cash arrives", " ".join(hd["c1"]),
                        f"{q} {' '.join(hd['c2'])}", f"{q} {hd['c3'][1]}"], rows, right={4, 5, 6}) + "\n")
    L.append(f"As drawn: no axis break (the timeline runs unbroken from January 2027 to 2042); the two right-hand columns "
             f"sit under the question \"{q}\" (the 0.15% fee on waiting money is in the note); a dotted line and "
             f"\"waits 10.5 months\" / \"waits 7.5 months\" mark the two long waits; legend: "
             f"{'; '.join(D.FIGURE1_LEGEND)}.\n")
    L.append("Note items: " + "; ".join(EXHIBITS["f1"]["note_items"]) + ".\n")
    L.append(cost("f1") + "\n")

    # Table 2
    L.append(f"## {EXHIBITS['t2']['label']}. {EXHIBITS['t2']['title']} (working title)\n")
    L.append(f"{EXHIBITS['t2']['section']}. Source: NUMBERS 8i (MODEL; the spread of the flexibility from 8j's joint "
             "replay column), `results_joint_stress_2026-11-10.json`.\n")
    rows = [[name] + D.table2_cells(v) for _, name, v in D.TABLE2_WORLDS]
    rows.append([f"*{D.TABLE2_SPREAD_LABEL}*", "", "", "", ""])
    rows += [[f"&nbsp;&nbsp;{label}"] + D.table2_cells(v) for label, v in D.TABLE2_SPREAD]
    L.append(_md_table(D.TABLE2_HEADER, rows, right={2, 3, 4}) + "\n")
    L.append(f"Last row of the table, full width under a rule: \"{D.TABLE2_RESULT_ROW}\" (checked: all five worlds "
             "and 100% of the 585 replays, 8i and 8j).\n")
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
    L.append("Not a row: custody (one line of 3e prose, SKELETON item 4 (c)).\n")
    L.append(cost("t3") + "\n")
    with open(os.path.join(HERE, "tables.md"), "w") as fh:
        fh.write("\n".join(L))


# =================================================================================================================
def main(argv):
    fails, _ = D.check(verbose=True)
    if fails:
        sys.exit("Stopped: an exhibit figure does not match NUMBERS.md (listed above).")
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
    m["_built"] = "Sat 14 Nov 2026 morning (Sydney), register of Tue 10 Nov 2026"
    with open(os.path.join(HERE, "measurements.json"), "w") as fh:
        json.dump(m, fh, indent=1)
    print(json.dumps(m, indent=1))
    tables_md(m)
    print("tables.md written")


if __name__ == "__main__":
    main(sys.argv)
