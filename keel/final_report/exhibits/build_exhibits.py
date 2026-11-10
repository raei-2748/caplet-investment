"""Build the Final Report's three exhibits on the register of Tue 10 Nov 2026 (rebuilt Wed 11 Nov 2026, Sydney).

    python3 -I keel/final_report/exhibits/build_exhibits.py            everything below (about a minute)
    python3 -I keel/final_report/exhibits/build_exhibits.py figure     Figure 1 only

Every figure comes from exhibit_data.py, which reads the results files in ../numbers/ and checks each figure against
NUMBERS.md; this script stops if that check fails. Writes, next to this file:

  figure1_reserve.svg          Figure 1 (text kept as text; Times New Roman, then Liberation Serif)
  figure1_reserve_2x.png       Figure 1 preview at 2x (192 dpi at its printed width of 6.5 in)
  exhibit2_reserve.png         Figure 1 at 300 dpi, the file ../template/build_template.py places (its old name)
  table1_holdings_2x.png       Table 1 preview at 2x, cropped from the Wharton-format PDF
  table2_markets_2x.png        Table 2 preview at 2x, cropped from the same PDF
  exhibits_letter.docx / .pdf  the three exhibits as APA blocks on Letter in Wharton's format; each note shows the
                               items it must carry (notes are written on 27 Nov, not here)
  tables.md                    every exhibit as Markdown text, with its source and note items
  measurements.json            each exhibit's height in double-spaced lines on a Letter page (card Q23's method)

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
from matplotlib.patches import Rectangle, Polygon  # noqa: E402

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
# Geometry in inches (the figure is drawn on one axes in inch units, y downwards).
W, H = 6.5, 3.40
X_YEAR = 0.0                       # payment year, left-aligned
AX_L, AX_R = 0.72, 3.76            # the staircase
C1_R, C2_R, C3_R = 4.70, 5.64, 6.50  # right edges of the three number columns
SPAN_L = 4.80                      # left end of the spanner over columns 2 and 3
T0, T_CUT, T1 = 2030.85, 2031.25, 2043.0   # T0 stands for January 2027 (the axis is broken at T_CUT)
HEAD_TOP, HEAD_RULE = 0.03, 0.62
ROW0, ROW_H, BAR_H = 0.66, 0.222, 0.15
FS_NUM, FS_LAB, FS_HEAD = 10.5, 10, 10.5


def X(t):
    return AX_L + (t - T0) / (T1 - T0) * (AX_R - AX_L)


def row_y(i):
    return ROW0 + (i + 0.5) * ROW_H


def figure1(outputs):
    """outputs: list of (path, dpi); an .svg path ignores dpi."""
    rows = D.FIGURE1_ROWS
    n = len(rows)
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")

    def text(x, y, s, ha="left", va="center", size=FS_NUM, weight="normal", color=INK, **kw):
        ax.text(x, y, s, ha=ha, va=va, fontsize=size, fontweight=weight, color=color, **kw)

    # ---- column heads ----
    hb = HEAD_RULE - 0.06                      # baseline of the lowest head line
    text(X_YEAR, hb, "Payment", va="bottom", weight="bold", size=FS_HEAD)
    text((AX_L + AX_R) / 2, 0.30, "Held from January 2027 until its cash arrives", ha="center", va="bottom",
         weight="bold", size=FS_HEAD)
    text(C1_R, hb, "rates", ha="right", va="bottom", weight="bold", size=FS_HEAD)
    text(C1_R, hb - 0.17, "At forward", ha="right", va="bottom", weight="bold", size=FS_HEAD)
    # the spanner says what the two columns test; the 0.15% fee on waiting money is in the note
    span_c = (SPAN_L + C3_R) / 2
    text(span_c, 0.20, "If nothing earns interest", ha="center", va="bottom", weight="bold", size=FS_HEAD)
    ax.plot([SPAN_L, C3_R], [0.235, 0.235], color=INK, linewidth=0.6)
    text(C2_R, hb, "Own holding", ha="right", va="bottom", weight="bold", size=FS_HEAD)
    # where the extra money comes from and when it is bought (NUMBERS section 2: "In January 2028 the deposit's
    # first dollars also buy extra face in the same Treasuries"); it is not in the WInS book
    text(C3_R, hb - 0.17, "Bought with", ha="right", va="bottom", weight="bold", size=FS_HEAD)
    text(C3_R, hb, "2028 deposit", ha="right", va="bottom", weight="bold", size=FS_HEAD)
    # the timeline's own head: January 2027 at the left (bars start at purchase), then the payment years
    text(X(T0), hb, "2027", ha="left", va="bottom", size=FS_LAB)
    for yr in range(2033, 2043, 2):
        text(X(yr), hb, str(yr), ha="center", va="bottom", size=FS_LAB)
    ax.plot([0, W], [HEAD_RULE, HEAD_RULE], color=INK, linewidth=0.6)
    _cut(ax, X(T_CUT), HEAD_RULE, 0.07)            # the break shows on the head rule too

    # ---- year grid behind the bars ----
    last = ROW0 + n * ROW_H
    for yr in range(2033, 2043):
        ax.plot([X(yr), X(yr)], [HEAD_RULE, last], color=RULE, linewidth=0.35, zorder=0)

    # ---- one row per payment ----
    for i, r in enumerate(rows):
        y = row_y(i)
        end = yearfrac(r["pays_out"])
        bond = r["kind"] == "T-bond"
        ax.add_patch(Rectangle((X(T0), y - BAR_H / 2), X(end) - X(T0), BAR_H, facecolor=BOND if bond else FUND,
                               edgecolor=INK, linewidth=0.5, zorder=2))
        _cut(ax, X(T_CUT), y, BAR_H / 2 + 0.035)
        text(X(T_CUT) + 0.075, y, r["holding"], size=FS_LAB, color="white" if bond else INK, zorder=5)
        # the payment: a black tick on 1 January
        ax.plot([X(r["year"]), X(r["year"])], [y - 0.095, y + 0.095], color=INK, linewidth=2.0,
                solid_capstyle="butt", zorder=4)
        if r["wait_words"]:   # long waits in the Trading Notes' words
            ax.plot([X(end), X(r["year"])], [y, y], color=INK, linewidth=0.7, linestyle=(0, (1.2, 1.4)), zorder=3)
            text(X(r["year"]) + 0.06, y, f"cash waits {r['wait_words']}", size=FS_LAB)
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
    for kind, label in (("fund", "iBond Treasury ETF"), ("bond", "Treasury bond"),
                        ("tick", "$50,000 payment on 1 January")):
        if kind == "tick":
            ax.plot([x + 0.07, x + 0.07], [yl - 0.08, yl + 0.08], color=INK, linewidth=2.0, solid_capstyle="butt")
        else:
            ax.add_patch(Rectangle((x, yl - BAR_H / 2), 0.28, BAR_H, facecolor=FUND if kind == "fund" else BOND,
                                   edgecolor=INK, linewidth=0.5))
        t = ax.text(x + (0.2 if kind == "tick" else 0.36), yl, label, ha="left", va="center", fontsize=FS_LAB)
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        x = bb.x1 + 0.3

    for path, dpi in outputs:
        if path.endswith(".svg"):
            fig.savefig(path, facecolor="white")
            _svg_font_fallback(path)
        else:
            fig.savefig(path, dpi=dpi, facecolor="white")
    plt.close(fig)
    return [p for p, _ in outputs]


def _cut(ax, x, y, half):
    """A broken-axis mark: a white slanted gap edged by two short ink lines (the usual mark for a skipped stretch)."""
    dx, gap = 0.035, 0.045
    pts = [(x - dx, y + half), (x + dx, y - half), (x + dx + gap, y - half), (x - dx + gap, y + half)]
    ax.add_patch(Polygon(pts, closed=True, facecolor="white", edgecolor="none", zorder=6))
    for off in (0.0, gap):
        ax.plot([x - dx + off, x + dx + off], [y + half, y - half], color=INK, linewidth=0.6, zorder=7)


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
           "title": "The Final WInS Portfolio at Cost on the Original $300,000: Laura's Whole Plan in Miniature",
           "section": "Section 2 (2-3 pages)", "note_budget_words": 50,
           "note_items": [
               "amounts at cost: quantity held x price paid on 6-7 Oct 2026 (U.S. Eastern), on the original $300,000 (8g)",
               "Pays for: the payment (1 January of that year) each holding stands for; the full-size plan for both "
               "deposits is Figure 1 and Table 2 (8g, 23 Oct snapshot)",
               "the floor: the least Laura can promise co-sponsors in 2031; IBTM stands in for the plan's late-2032 "
               "floor fund (TNA l.13, CANON A24, 8g)",
               "costs row = $200 of commissions + $1,109.42 of bond interest accrued at purchase, which comes back "
               "with each bond's next coupon (8g v2)"]},
    "f1": {"label": "Figure 1",
           "title": "Each Payment Has Its Own Treasury; Extra Treasuries Bought With the 2028 Deposit Pay Any Gap if "
                    "Nothing Earns Interest (Laura's Plan for Both Deposits, $450,000, Modelled)",
           "section": "Section 3, part 3a", "note_budget_words": 55,
           "note_items": [
               "MODEL, at forward rates on the Treasury par yield curve of 6 Nov 2026",
               "the right-hand columns are what each payment gets if nothing earns interest from 2027 and waiting "
               "money pays the Treasury-bill ETF's 0.15% fee: the $500,000 of payments split between the payment's "
               "own holding ($444,080) and the Treasuries bought with the 2028 deposit ($55,920); not the reserve's "
               "value on 1 Jan 2033 ($444,545 at forward rates) (8h)",
               "if room: those extra Treasuries cost $34,369 in 1 Jan 2027 money (section 2); not in the WInS book",
               "rows may not add to the totals because of rounding"]},
    "t2": {"label": "Table 2",
           "title": "Laura's Plan for Both Deposits ($450,000) in Five Markets and 585 History Replays, Modelled",
           "section": "Section 3, parts 3b and 3c", "note_budget_words": 45,
           "note_items": [
               "MODEL, not forecasts; Treasury curve of 6 Nov 2026",
               "shares 7.5% a year in rows 1 and 3",
               "replays: U.S. yields and stocks from the start month (method in 3e)",
               "inflation row: prices up 5% a year",
               "flexibility: the half of VT promised to no one plus whatever the funds pay above the stated top, to "
               "the nearest $100 (8i)",
               "spread rows: each column's own percentile"]},
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


def apa_table(BT, rep, ex, header, rows, widths, aligns, note_text, top=False, spanners=None):
    """rows: list of (kind, cells); kind is row, subtotal, total, spanner (one italic cell across the table, a rule
    above), indent (a stub indented under a spanner) or result (one plain cell across the table, a rule above: a
    finding that holds for every row). Borders: top and bottom of the heads, above a subtotal, spanner, result or
    total, and at the bottom; never vertical (APA 7). spanners: [(first column, last column, text)] puts a column
    spanner over those heads (a second head row, with a rule under the spanner); the other heads span both head rows,
    set at the bottom."""
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
    for r_i, (kind, values) in enumerate(all_rows):
        if spanners and r_i == 0:
            continue
        row = t.rows[r_i + nh - 1]
        BT._row_keep(row, header=(r_i == 0))
        if kind in ("spanner", "result"):
            merged = row.cells[0].merge(row.cells[-1])
            cells = [merged]
            values = [values[0]]
        else:
            cells = row.cells
        last = r_i == len(all_rows) - 1
        for c_i, (cell, val) in enumerate(zip(cells, values)):
            full = kind in ("spanner", "result")
            cell.width = Inches(sum(widths) if full else widths[c_i])
            BT._cell_margins(cell, PAD)
            _pad(cell, 0 if full else c_i, len(header) - 1 if full else c_i, len(header))
            p = cell.paragraphs[0]
            p.style = rep.doc.styles["APA Table Text"]
            p.paragraph_format.keep_with_next = not last
            if kind == "head":
                p.alignment = BT.C
            else:
                p.alignment = BT.L if full else aligns[c_i]
            if kind == "indent" and c_i == 0:
                p.paragraph_format.left_indent = Inches(0.2)
            if kind == "subtotal":
                p.paragraph_format.space_after = Pt(6)      # one deliberate gap after the subtotal (card Q28)
            run = p.add_run(str(val))
            run.bold = kind == "total"
            run.italic = kind == "spanner"
            edges = {}
            if kind == "head":
                edges.update(top=8, bottom=8)
            if kind in ("subtotal", "spanner", "result"):
                edges.update(top=4)
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
    # "[532281]" 0.611 in; the costs label 3.078; "Asset" 0.370; bold "300,000.00" 0.750; bold "100.00" 0.458;
    # "Range top," 0.722. Two "Pays for" cells take two lines by design (IBTM's and VT's two jobs).
    widths = [0.67, 3.17, 0.47, 0.85, 0.55, 0.79]
    aligns = [BT.L, BT.L, BT.L, BT.R, BT.R, BT.C]
    return apa_table(BT, rep, "t1", D.TABLE1_HEADER, D.table1_rows(), widths, aligns, note_text, top)


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


ADDERS = {"t1": add_table1, "f1": add_figure1, "t2": add_table2}


def items_note(ex):
    return "[Note to carry: " + "; ".join(EXHIBITS[ex]["note_items"]) + ".]"


def build_letter_pdf(BT, path_docx):
    """The three exhibits on Letter in Wharton's format, each with its note items as a placeholder note."""
    rep = BT.Report(paper="letter")
    for k, ex in enumerate(("t1", "f1", "t2")):
        rep.para("Above the exhibit.")
        ADDERS[ex](BT, rep, items_note(ex), top=(k > 0))
        rep.para("Below the exhibit.")
    return rep.save(path_docx)


def crop_previews(BT, pdf):
    import pdfplumber
    pages = BT.pdf_pages_text(pdf)
    out = {}
    with pdfplumber.open(pdf) as doc:
        for ex, name in (("t1", "table1_holdings_2x.png"), ("t2", "table2_markets_2x.png")):
            pi, ln = BT.find_line(pages, EXHIBITS[ex]["label"])
            pj, below = BT.find_line(pages, "Below the exhibit.", start_page=pi)
            assert pi == pj, f"{ex} spans pages"
            top = ln["top"] - 6
            bottom = below["top"] - 27.6 + 4          # stop above the blank line after the exhibit
            page = doc.pages[pi]
            img = page.crop((66, top, page.width - 66, bottom)).to_image(resolution=PREVIEW_DPI)
            img.save(os.path.join(HERE, name))
            out[ex] = name
    return out


def measure(BT, workdir):
    """Card Q23's method: an exhibit between two prose lines on a Letter page; its height = the gap / 27.6 pt - 1
    double-spaced lines, counting the number, title, note and the blank line after. Notes are filler of each
    exhibit's word budget (the notes are written on 27 Nov), and without a note, so the cost per note line shows."""
    f = BT.Filler()
    res = {}
    for ex in ("t1", "f1", "t2"):
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
                res[key] = {"lines": None, "pages_spanned": b[0] - a[0] + 1, "note_words": words}
    return res


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
    L.append("# The Final Report's exhibits as text (built Wed 11 Nov 2026, Sydney)\n")
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
    for kind, cells in D.table1_rows():
        cells = [c.replace("\n", " ") for c in cells]
        if kind == "subtotal":
            cells = ["", f"*{cells[1]}*", "", f"*{cells[3]}*", f"*{cells[4]}*", ""]
        if kind == "total":
            cells = [f"**{c}**" if c else "" for c in cells]
        rows.append(cells)
    L.append(_md_table(D.TABLE1_HEADER, rows, right={3, 4}) + "\n")
    L.append("Two Pays-for cells print on two lines at 12 pt: IBTM's (\"2033 and / the floor\") and VT's (\"Range top, / "
             "flexibility\"). Asset types are one word (Wharton's \"ETF\" and \"Bond\" for its \"Treasury Bond\"); the "
             "dollar sign is in the head.\n")
    L.append("Note items: " + "; ".join(EXHIBITS["t1"]["note_items"]) + ".\n")
    L.append(cost("t1") + "\n")

    # Figure 1
    L.append(f"## {EXHIBITS['f1']['label']}. {EXHIBITS['f1']['title']} (working title)\n")
    L.append(f"{EXHIBITS['f1']['section']}. Source: NUMBERS 8h (MODEL), `results_reserve_2026-11-10.json` blocks "
             "`composition_1jan2033_base`, `base` and `fee`. The figure is `figure1_reserve.svg`; its numbers as text:\n")
    rows = []
    for r in D.FIGURE1_ROWS:
        y, m, d = r["pays_out"].split("-")
        arrives = f"{int(d)} {date(int(y), int(m), 1).strftime('%b')} {y}"
        if r["wait_words"]:
            arrives += f" (cash waits {r['wait_words']})"
        rows.append([r["year"], r["holding"], "Treasury bond" if r["kind"] == "T-bond" else "iBond Treasury ETF",
                     arrives, D.dollars(r["at_forwards"]), D.dollars(r["own_if_nothing_earns"]),
                     D.dollars(r["backstop_if_nothing_earns"])])
    T = D.FIGURE1_TOTALS
    rows.append(["**Total**", "", "", "", f"**{D.dollars(T['at_forwards'])}**",
                 f"**{D.dollars(T['own_if_nothing_earns'])}**", f"**{D.dollars(T['backstop_if_nothing_earns'])}**"])
    L.append(_md_table(["Payment (1 Jan)", "Paid from", "Type", "Cash arrives", "At forward rates",
                        "If nothing earns interest (after the ETF fee): own holding",
                        "If nothing earns interest: bought with the 2028 deposit"], rows, right={4, 5, 6}) + "\n")
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
    shutil.rmtree(work, ignore_errors=True)
    m["_method"] = ("Card Q23: Letter, 1-inch margins, 12-pt Times New Roman metrics (Liberation Serif), double-spaced "
                    "text at a 27.6-pt pitch, table bodies single-spaced, APA number, title and note double-spaced, a "
                    "blank double-spaced line after each exhibit; LibreOffice headless; words a line 14.26 (Q23 row 5)")
    m["_built"] = "Wed 11 Nov 2026 (Sydney), register of Tue 10 Nov 2026"
    with open(os.path.join(HERE, "measurements.json"), "w") as fh:
        json.dump(m, fh, indent=1)
    print(json.dumps(m, indent=1))
    tables_md(m)
    print("tables.md written")


if __name__ == "__main__":
    main(sys.argv)
