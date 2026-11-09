"""Wharton Final Report page template, measurements and pour tool (Team Keel, Tue 10 Nov 2026).

Wharton's format (competition/official/2026_27/2026_WGY_Final_Report_Instructions.txt, "Required Format and
Submission"): PDF no larger than 5 MB; 12-point Times New Roman; double-spaced; 1-inch margins; page numbers in the
bottom-left corner; APA citations; a separate References page; no links evaluators are expected to open. "Tables and
graphics may be single-spaced when needed for readability." Pages: title 1; Portfolio Implementation 2-3; Integrated
Recommendation and Reflection 6-8; 9-12 in all, References not counted. Wharton names no paper size; its own PDF is
US Letter (612 x 792 pt), so Letter is the default here.

APA 7 student-paper settings layered on top (apastyle.apa.org, read 10 Nov 2026): first-line indent 0.5 in; no extra
space before or after paragraphs or headings; left-aligned, ragged right; Level 1 heading centred bold title case,
Level 2 flush left bold, Level 3 flush left bold italic; the paper title repeated, bold and centred, at the top of the
first page of text; table and figure number in bold, title in italic title case on the next double-spaced line;
table body single-, 1.5- or double-spaced; number, title and notes double-spaced; borders only at the top, under the
column heads, above a totals row and at the bottom; "Note." in italics; References on a new page, label centred bold,
entries double-spaced with a 0.5 in hanging indent.

Usage (python3 with python-docx; LibreOffice "soffice" for PDF):
  python3 build_template.py demo                 the format test: template_test.docx/.pdf (12 pages + References)
  python3 build_template.py measure              all measurements -> measurements.json (several minutes)
  python3 build_template.py pour report.md       27 Nov: pour text into the template -> report.docx/.pdf + audit
  python3 build_template.py audit some.pdf       page audit of any PDF (sections, pages, size, fonts, links)

Filler for measuring is the Declaration of Independence (public domain; National Archives transcription), never
report text.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
EXHIBITS = os.path.join(HERE, "..", "exhibits")
sys.path.insert(0, EXHIBITS)
import exhibit_data as D  # noqa: E402

FONT = "Times New Roman"
PAPER = {"letter": (8.5, 11.0), "a4": (8.27, 11.69)}
SECTION2 = "Portfolio Implementation"
SECTION3 = "Integrated Recommendation and Reflection"
REFS = "References"


# =================================================================================================================
# Low-level formatting helpers
# =================================================================================================================
def _set_run_font(rpr_parent, name=FONT):
    """Force a style or run to one font for every script, removing theme-font overrides (python-docx's default
    template points headings at theme fonts, which would beat a plain font name)."""
    rpr = rpr_parent.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for att in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rfonts.get(qn(att)) is not None:
            del rfonts.attrib[qn(att)]
    for att in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(att), name)


def _style(doc, name, base=None, size=12, bold=False, italic=False, align=None, indent=None, spacing="double",
           keep_next=False, hanging=None):
    styles = doc.styles
    try:
        st = styles[name]
    except KeyError:
        from docx.enum.style import WD_STYLE_TYPE
        st = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    if base:
        st.base_style = styles[base]
    f = st.font
    f.name, f.size, f.bold, f.italic = FONT, Pt(size), bold, italic
    f.color.rgb = RGBColor(0, 0, 0)
    _set_run_font(st.element)
    pf = st.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE if spacing == "double" else WD_LINE_SPACING.SINGLE
    pf.widow_control = True
    pf.keep_with_next = keep_next
    pf.first_line_indent = Inches(indent) if indent is not None else Inches(0)
    if hanging is not None:
        pf.left_indent = Inches(hanging)
        pf.first_line_indent = Inches(-hanging)
    else:
        pf.left_indent = Inches(0)
    if align is not None:
        pf.alignment = align
    return st


def _page_number_footer(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT     # Wharton: page numbers bottom left
    p.style = footer.part.document.styles["Normal"] if False else p.style
    run = p.add_run()
    for kind, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)
    run.font.name, run.font.size = FONT, Pt(12)
    _set_run_font(run._r)


def _cell_borders(cell, **edges):
    tcpr = cell._tc.get_or_add_tcPr()
    borders = tcpr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        mar = tcpr.find(qn("w:tcMar"))
        if mar is not None:
            mar.addprevious(borders)
        else:
            tcpr.append(borders)
    for edge, val in edges.items():
        el = OxmlElement(f"w:{edge}")
        if val:
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), str(val))   # eighths of a point
            el.set(qn("w:color"), "000000")
        else:
            el.set(qn("w:val"), "nil")
        borders.append(el)


def _cell_margins(cell, twips):
    """Left and right padding on the cell itself (LibreOffice ignores the table-level default)."""
    tcpr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for side in ("left", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(twips))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    # CT_TcPr order: tcW, gridSpan, vMerge, tcBorders, shd, noWrap, tcMar, ...; tcMar goes after tcBorders/shd
    after = [qn("w:tcW"), qn("w:gridSpan"), qn("w:vMerge"), qn("w:tcBorders"), qn("w:shd"), qn("w:noWrap")]
    idx = 0
    for i, k in enumerate(list(tcpr)):
        if k.tag in after:
            idx = i + 1
    tcpr.insert(idx, mar)


def _table_no_borders(table):
    tblpr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tblpr.append(borders)


TBLPR_ORDER = ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize", "tblStyleColBandSize", "tblW",
               "jc", "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook",
               "tblCaption", "tblDescription"]


def _order_tblpr(table):
    """Word rejects table properties out of schema order (CT_TblPr); put every child back in order."""
    tblpr = table._tbl.tblPr
    kids = list(tblpr)
    rank = {qn(f"w:{n}"): i for i, n in enumerate(TBLPR_ORDER)}
    for k in kids:
        tblpr.remove(k)
    for k in sorted(kids, key=lambda e: rank.get(e.tag, 99)):
        tblpr.append(k)


def _fixed_widths(table, widths):
    """Fixed layout with explicit grid widths: Word honours cell widths alone, LibreOffice and Google Docs need the
    grid and the fixed layout too."""
    tblpr = table._tbl.tblPr
    lay = tblpr.find(qn("w:tblLayout"))
    if lay is None:
        lay = OxmlElement("w:tblLayout")
        tblpr.append(lay)
    lay.set(qn("w:type"), "fixed")
    tw = OxmlElement("w:tblW")
    tw.set(qn("w:w"), str(int(sum(widths) * 1440)))
    tw.set(qn("w:type"), "dxa")
    old = tblpr.find(qn("w:tblW"))
    if old is not None:
        tblpr.remove(old)
    tblpr.append(tw)
    mar = OxmlElement("w:tblCellMar")
    for side in ("left", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), "58")          # 0.04 in: full fund names fit on one line at 12 pt
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblpr.append(mar)
    grid = table._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(int(w * 1440)))
    for i, col in enumerate(table.columns):
        col.width = Inches(widths[i])


def _row_keep(row, header=False):
    trpr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    trpr.append(el)
    if header:
        h = OxmlElement("w:tblHeader")
        trpr.append(h)


# =================================================================================================================
# The document builder
# =================================================================================================================
class Report:
    """A Wharton-format report. Methods add blocks in order; save() writes .docx and (optionally) .pdf."""

    def __init__(self, paper="letter", table_spacing="single", note_spacing="double", blank_after_exhibit=True):
        self.doc = Document()
        self.table_spacing = table_spacing
        self.note_spacing = note_spacing
        self.blank_after_exhibit = blank_after_exhibit
        w, h = PAPER[paper]
        sec = self.doc.sections[0]
        sec.page_width, sec.page_height = Inches(w), Inches(h)
        for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
            setattr(sec, side, Inches(1))
        sec.header_distance = Inches(0.5)
        sec.footer_distance = Inches(0.5)
        d = self.doc
        _style(d, "Normal")
        _style(d, "APA Body", base="Normal", indent=0.5)
        _style(d, "APA Title Page", base="Normal", align=WD_ALIGN_PARAGRAPH.CENTER)
        _style(d, "APA Paper Title", base="Normal", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        # Built-in heading styles keep navigation and PDF bookmarks working in Word; restyled to APA.
        _style(d, "Heading 1", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        _style(d, "Heading 2", bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=True)
        _style(d, "Heading 3", bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=True)
        _style(d, "APA Exhibit Number", base="Normal", bold=True, keep_next=True)
        _style(d, "APA Exhibit Title", base="Normal", italic=True, keep_next=True)
        _style(d, "APA Exhibit Note", base="Normal", spacing=note_spacing)
        _style(d, "APA Table Text", base="Normal", spacing=table_spacing)
        _style(d, "APA Reference", base="Normal", hanging=0.5)
        _page_number_footer(sec)

    # ---- text blocks --------------------------------------------------------------------------------------------
    def title_page(self, title="[Report title]", lines=None):
        """Wharton: official team name, advisor's first and last name, finalized team member names, team WInS
        username, matching the roster. APA student layout: title bold, 3-4 lines down, then one blank line."""
        lines = lines or ["[Official team name]", "[Finalized team member names]", "Advisor: [Advisor first and last name]",
                          "WInS username: [Team WInS username]", "[School name]",
                          "Wharton Global High School Investment Competition, 2026-2027", "[Submission date]"]
        for _ in range(3):
            self.doc.add_paragraph("", style="APA Title Page")
        p = self.doc.add_paragraph(title, style="APA Title Page")
        p.runs[0].bold = True
        self.doc.add_paragraph("", style="APA Title Page")
        for i, line in enumerate(lines):
            self.doc.add_paragraph(line, style="APA Title Page")
        self.page_break()

    def page_break(self):
        p = self.doc.add_paragraph(style="Normal")
        p.add_run().add_break(WD_BREAK.PAGE)
        # an empty paragraph after a break would cost a line: put the break inside the last paragraph instead
        return p

    def paper_title(self, text):
        self.doc.add_paragraph(text, style="APA Paper Title")

    def heading(self, text, level=1, new_page=False):
        p = self.doc.add_paragraph(text, style=f"Heading {level}")
        p.paragraph_format.page_break_before = new_page
        return p

    def para(self, text):
        return self.doc.add_paragraph(text, style="APA Body")

    def blank(self):
        return self.doc.add_paragraph("", style="Normal")

    # ---- exhibits -----------------------------------------------------------------------------------------------
    def _number_title(self, label, title, top=False):
        p = self.doc.add_paragraph(label, style="APA Exhibit Number")
        p.paragraph_format.page_break_before = top    # APA: an exhibit sits at the top or bottom of a page
        self.doc.add_paragraph(title, style="APA Exhibit Title")

    def _note(self, text):
        if not text:
            return
        p = self.doc.add_paragraph(style="APA Exhibit Note")
        r = p.add_run("Note.")
        r.italic = True
        p.add_run(" " + text)

    def table(self, label, title, header, rows, widths, aligns, note=None, total_row=False, bold_last=False, top=False):
        """APA table: number (bold), title (italic), body single-spaced by default (Wharton and APA both allow it),
        borders at top, under the heads, above a totals row and at the bottom; no vertical rules."""
        self._number_title(label, title, top)
        t = self.doc.add_table(rows=1 + len(rows), cols=len(header))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        _table_no_borders(t)
        _fixed_widths(t, widths)
        for r_i, values in enumerate([header] + rows):
            row = t.rows[r_i]
            _row_keep(row, header=(r_i == 0))
            for c_i, val in enumerate(values):
                cell = row.cells[c_i]
                cell.width = Inches(widths[c_i])
                _cell_margins(cell, 58)
                p = cell.paragraphs[0]
                p.style = self.doc.styles["APA Table Text"]
                p.paragraph_format.keep_with_next = r_i < len(rows)   # keep the table on one page
                if r_i == 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER          # APA: centre column heads
                else:
                    p.alignment = aligns[c_i]
                run = p.add_run(str(val))
                if (bold_last and r_i == len(rows)) or False:
                    run.bold = True
                edges = {}
                if r_i == 0:
                    edges.update(top=8, bottom=8)
                if r_i == len(rows):
                    edges.update(bottom=8)
                if total_row and r_i == len(rows):
                    edges.update(top=4)
                if edges:
                    _cell_borders(cell, **edges)
        _order_tblpr(t)
        # the paragraph after a table: the note (or a blank line if none)
        self._note(note)
        if self.blank_after_exhibit:
            self.blank()
        return t

    def figure(self, label, title, image_path, width_in=6.5, note=None, top=False):
        self._number_title(label, title, top)
        p = self.doc.add_paragraph(style="APA Table Text")
        p.paragraph_format.keep_with_next = bool(note)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(image_path, width=Inches(width_in))
        self._note(note)
        if self.blank_after_exhibit:
            self.blank()

    def references(self, entries):
        self.heading(REFS, level=1, new_page=True)
        for e in entries:
            self.doc.add_paragraph(e, style="APA Reference")

    def save(self, path_docx, pdf=True):
        self.doc.save(path_docx)
        if pdf:
            return to_pdf(path_docx)
        return None


# =================================================================================================================
# The exhibits, as APA blocks (data from ../exhibits/exhibit_data.py, which cites NUMBERS.md by section)
# =================================================================================================================
L, C, R = WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.RIGHT


def add_table1_holdings(rep, pays_for=False, top=False):
    """Exhibit 1 = APA Table 1. Wharton's five required columns, each row on one line at 12 pt (full fund names need
    3.04 in). Asset types use Wharton's own example labels ("ETF", "Treasury bond", "Cash"). pays_for=True adds the
    panel's "Pays for" column: it only fits if names wrap, so it is kept for measuring, not recommended."""
    type_label = {"ETF (Treasury)": "ETF", "ETF (equity)": "ETF", "Treasury bond": "Treasury bond", "Cash": "Cash",
                  "Cost": "Cost"}
    name_label = {"Commissions and bond interest paid at purchase": "Commissions and accrued interest"}
    if pays_for:
        header = ["Ticker or identifier", "Name", "Asset type", "Amount", "%", "Pays for"]
        widths = [0.8, 2.3, 1.05, 0.93, 0.52, 0.9]
        aligns = [L, L, L, R, R, L]
        short = {"2033 payment and floor stand-in": "2033, floor", "Growth: top of the range and the half kept":
                 "Growth", "Cost of buying": "Costs"}
        rows = [[h[0], name_label.get(h[1], h[1]), type_label[h[2]], f"${h[3]:,.2f}", f"{h[4]:.2f}",
                 short.get(h[5], h[5].replace(" payment", ""))] for h in D.HOLDINGS]
        rows.append(["Total", "", "", f"${D.HOLDINGS_TOTAL[0]:,.2f}", f"{D.HOLDINGS_TOTAL[1]:.2f}", ""])
    else:
        header = ["Ticker or identifier", "Name", "Asset type", "Amount", "%"]
        widths = [0.8, 3.15, 1.05, 0.92, 0.58]
        aligns = [L, L, L, R, R]
        rows = [[h[0], name_label.get(h[1], h[1]), type_label[h[2]], f"${h[3]:,.2f}", f"{h[4]:.2f}"]
                for h in D.HOLDINGS]
        rows.append(["Total", "", "", f"${D.HOLDINGS_TOTAL[0]:,.2f}", f"{D.HOLDINGS_TOTAL[1]:.2f}"])
    note = ("Amounts are the quantities held times the prices paid on 6-7 October 2026 (U.S. Eastern), on the "
            "original $300,000. Cash is the cash shown in WInS; costs are $200 of commissions and $1,109.42 of "
            "accrued bond interest.")
    rep.table("Table 1", "Laura's Plan in Miniature: The Final WInS Portfolio at Cost", header, rows, widths, aligns,
              note=note, total_row=True, bold_last=True, top=top)


def add_figure1_reserve(rep, top=False):
    img = os.path.join(EXHIBITS, "exhibit2_reserve.png")
    note = ("Model values at forward rates on the Treasury curve of 6 November 2026 (U.S. Department of the "
            "Treasury, 2026). \u201cAbove $50,000\u201d is what each holding pays beyond its payment at those rates; "
            "if reinvestment earns 3 points less, each pays exactly $50,000.")
    rep.figure("Figure 1", "The Operating Reserve Runs Down One Holding a Year, 2033-2042", img, note=note, top=top)


def add_table2_markets(rep, top=False):
    header = D.SCENARIO_COLUMNS
    rows = [list(r) for r in D.SCENARIO_ROWS]
    widths = [2.0, 1.05, 1.3, 1.0, 1.15]
    aligns = [L, C, C, C, C]
    note = ("PLACEHOLDER: figures from cards Q19 and Q24 once they are in NUMBERS.md; *under review in NUMBERS.md "
            "section 4. Model values; the stated range is what Laura can announce before the 2031 meetings.")
    rep.table("Table 2", "The Plan Under Four Markets", header, rows, widths, aligns, note=note, top=top)


def add_table3_monitoring(rep, filler, top=False):
    """A monitoring table shaped like the skeleton's 3e (signal, what it changes, what it never changes). Row labels
    are from CASE_MAP section E item 2; the cells are FILLER of realistic length, for measuring only."""
    header = ["What Laura watches", "When", "What it can change", "What it never changes"]
    labels = ["Treasury yields", "World shares (VT)", "Taiwan dollar and building costs", "Co-sponsor budgets",
              "Each iBond fund's payout", "The 2028 deposit", "U.S. Treasury default"]
    rows = []
    for lab in labels:
        rows.append([lab, filler.words(3), filler.words(11), filler.words(9)])
    widths = [1.55, 1.05, 2.0, 1.9]
    rep.table("Table 3", "What to Monitor as 2031 and 2033 Approach", header, rows, widths, [L, L, L, L],
              note=filler.words(30), top=top)


# =================================================================================================================
# Filler (public domain) and PDF tools
# =================================================================================================================
class Filler:
    def __init__(self, path=os.path.join(HERE, "filler_declaration.txt")):
        with open(path) as fh:
            self.tokens = fh.read().split()
        self.i = 0

    def words(self, n):
        out = []
        for _ in range(n):
            out.append(self.tokens[self.i % len(self.tokens)])
            self.i += 1
        s = " ".join(out)
        return s[0].upper() + s[1:] if s else s

    def paragraphs(self, total, per=120):
        out, left = [], total
        while left > 0:
            k = min(per, left)
            out.append(self.words(k).rstrip(",;:") + ("" if out else ""))
            left -= k
        return out


def to_pdf(path_docx):
    outdir = os.path.dirname(os.path.abspath(path_docx))
    profile = os.path.join(tempfile.gettempdir(), "keel_lo_profile")
    cmd = ["soffice", f"-env:UserInstallation=file://{profile}", "--headless", "--convert-to", "pdf",
           "--outdir", outdir, path_docx]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    return os.path.splitext(os.path.abspath(path_docx))[0] + ".pdf"


def pdf_pages_text(path_pdf):
    import pdfplumber
    pages = []
    with pdfplumber.open(path_pdf) as pdf:
        for pg in pdf.pages:
            words = pg.extract_words(keep_blank_chars=False, use_text_flow=True, extra_attrs=["fontname", "size"])
            pages.append({"words": words, "height": pg.height, "width": pg.width,
                          "images": len(pg.images), "annots": len(pg.annots or [])})
    return pages


def lines_of(words, tol=2.0):
    """Group words into text lines by their top coordinate."""
    lines = []
    for w in sorted(words, key=lambda w: (round(w["top"]), w["x0"])):
        if lines and abs(lines[-1]["top"] - w["top"]) <= tol:
            lines[-1]["words"].append(w)
        else:
            lines.append({"top": w["top"], "bottom": w["bottom"], "words": [w]})
    for ln in lines:
        ln["text"] = " ".join(x["text"] for x in ln["words"])
    return lines


def find_line(pages, text, start_page=0):
    for i, pg in enumerate(pages):
        if i < start_page:
            continue
        for ln in lines_of(pg["words"]):
            if ln["text"].strip() == text:
                return i, ln
    return None, None


def audit(path_pdf, quiet=False):
    """Page audit against Wharton's limits: where each section starts, pages per section, total pages without
    References, file size, fonts used, link annotations."""
    pages = pdf_pages_text(path_pdf)
    p2, _ = find_line(pages, SECTION2)
    p3, _ = find_line(pages, SECTION3)
    pr, _ = find_line(pages, REFS)
    n = len(pages)
    fonts = sorted({w["fontname"].split("+")[-1] for pg in pages for w in pg["words"]})
    res = {"pages": n, "section2_start": None if p2 is None else p2 + 1,
           "section3_start": None if p3 is None else p3 + 1, "references_start": None if pr is None else pr + 1,
           "size_bytes": os.path.getsize(path_pdf), "fonts": fonts,
           "link_annotations": sum(pg["annots"] for pg in pages)}
    if None not in (p2, p3, pr):
        res["title_pages"] = p2
        res["section2_pages"] = p3 - p2
        res["section3_pages"] = pr - p3
        res["pages_without_references"] = pr
        res["ok"] = (p2 == 1 and 2 <= res["section2_pages"] <= 3 and 6 <= res["section3_pages"] <= 8
                     and 9 <= pr <= 12 and res["size_bytes"] <= 5 * 1024 * 1024)
    if not quiet:
        print(json.dumps(res, indent=1))
    return res


# =================================================================================================================
# The mock report used for measuring: real exhibits, Wharton's sections, filler prose
# =================================================================================================================
S2_PARTS = ["2.1", "2.2", "2.3", "2.5"]          # SKELETON v2: 2.0 lead (no heading) then 2.1-2.3, 2.5
S3_PARTS = ["3a", "3b", "3c", "3d", "3e", "3f"]  # SKELETON v2: 3.0 lead (no heading) then 3a-3f


# Where each exhibit starts (1-indexed page, top of page), following SKELETON v2's order: Table 1 in Section 2 after
# the lead and 2.1; Figure 1 in 3a; Table 2 in 3c; Table 3 (the monitoring table) in 3e.
EXHIBIT_PAGES = {"t1": 3, "f1": 6, "t2": 8, "t3": 10}
EXHIBIT_LABEL = {"t1": "Table 1", "f1": "Figure 1", "t2": "Table 2", "t3": "Table 3"}


def build_mock(path, plan, paper="letter", per=120, exhibits=("t1", "f1", "t2"), pays_for=False, paper_title=True,
               table_spacing="single", note_spacing="double", pdf=True, top=True):
    """plan: word counts per prose block. s2_pre = lead and 2.1 before Table 1; s2_post = 2.2 to 2.5 after it;
    s3 = one block before each Section 3 exhibit and one after the last. Exhibits start at the top of a page."""
    f = Filler()
    rep = Report(paper=paper, table_spacing=table_spacing, note_spacing=note_spacing)
    rep.title_page()
    if paper_title:
        rep.paper_title("[Report Title]")
    rep.heading(SECTION2, 1)
    _prose_with_headings(rep, f, plan["s2_pre"], ["Part 2.1 Heading"], per)
    if "t1" in exhibits:
        add_table1_holdings(rep, pays_for=pays_for, top=top)
    _prose_with_headings(rep, f, plan["s2_post"], [f"Part {p} Heading" for p in S2_PARTS[1:]], per, lead=False)
    rep.heading(SECTION3, 1, new_page=True)
    blocks = plan["s3"]
    s3_ex = [e for e in exhibits if e != "t1"]
    heads = _s3_heads(s3_ex)
    for i, words in enumerate(blocks):
        _prose_with_headings(rep, f, words, heads[i], per, lead=(i == 0))
        if i < len(s3_ex):
            e = s3_ex[i]
            if e == "f1":
                add_figure1_reserve(rep, top=top)
            elif e == "t2":
                add_table2_markets(rep, top=top)
            elif e == "t3":
                add_table3_monitoring(rep, f, top=top)
    rep.references(SAMPLE_REFERENCES)
    return rep.save(path, pdf=pdf)


def _s3_heads(s3_ex):
    """Level 2 headings of Section 3 between its exhibits: 3a holds Figure 1, 3c Table 2, 3e Table 3."""
    home = {"f1": "3a", "t2": "3c", "t3": "3e"}
    blocks, cur = [], []
    for part in S3_PARTS:
        cur.append(f"Part {part} Heading")
        if any(home[e] == part for e in s3_ex):
            blocks.append(cur)
            cur = []
    blocks.append(cur)
    return blocks


def _prose_with_headings(rep, f, total, heads, per, lead=True):
    """Spread `total` filler words across a lead (if lead) and one stretch per heading."""
    n_chunks = len(heads) + (1 if lead else 0)
    if n_chunks == 0:
        return
    sizes = [total // n_chunks + (1 if i < total % n_chunks else 0) for i in range(n_chunks)]
    k = 0
    if lead:
        for ptxt in f.paragraphs(sizes[0], per):
            rep.para(ptxt)
        k = 1
    for h, sz in zip(heads, sizes[k:]):
        rep.heading(h, 2)
        for ptxt in f.paragraphs(sz, per):
            rep.para(ptxt)


SAMPLE_REFERENCES = [
    "American Psychological Association. (2025). Student paper setup guide (7th ed.). "
    "https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf",
    "Few, S. (2005). Effectively communicating numbers: Selecting the best means and manner of display. Perceptual "
    "Edge. https://www.perceptualedge.com/articles/Whitepapers/Communicating_Numbers.pdf",
    "Tufte, E. R. (2001). The visual display of quantitative information (2nd ed.). Graphics Press.",
]


# =================================================================================================================
# Measurements
# =================================================================================================================
def measure_plain(paper="letter", per=120, workdir=None):
    """Words and lines on full pages of plain double-spaced prose (no headings)."""
    workdir = workdir or tempfile.mkdtemp()
    f = Filler()
    rep = Report(paper=paper)
    for ptxt in f.paragraphs(1600, per):
        rep.para(ptxt)
    pdf = rep.save(os.path.join(workdir, f"plain_{paper}_{per}.docx"))
    pages = pdf_pages_text(pdf)
    full = pages[1:-1] if len(pages) > 2 else pages[:1]
    counts, nlines = [], []
    for pg in full:
        lns = [ln for ln in lines_of(pg["words"]) if ln["top"] < pg["height"] - 72]   # drop the footer
        counts.append(sum(len(ln["text"].split()) for ln in lns))
        nlines.append(len(lns))
    pitch = None
    lns = [ln for ln in lines_of(full[0]["words"]) if ln["top"] < full[0]["height"] - 72]
    if len(lns) > 2:
        pitch = (lns[-1]["top"] - lns[0]["top"]) / (len(lns) - 1)
    return {"paper": paper, "paragraph_words": per, "words_per_full_page": counts, "lines_per_page": nlines,
            "line_pitch_pt": round(pitch, 2) if pitch else None,
            "words_per_line": round(sum(counts) / max(1, sum(nlines)), 2)}


def measure_blocks(paper="letter", workdir=None):
    """Height of each exhibit and heading in double-spaced text lines, from where it sits on the PDF page."""
    workdir = workdir or tempfile.mkdtemp()
    out = {}
    f = Filler()
    variants = {
        "table1_6col_single_wrapped": lambda r: add_table1_holdings(r, pays_for=True),
        "table1_5col_single": lambda r: add_table1_holdings(r, pays_for=False),
        "figure1": add_figure1_reserve,
        "table2_markets": add_table2_markets,
        "table3_monitoring": lambda r: add_table3_monitoring(r, f),
    }
    for name, fn in list(variants.items()) + [("table1_5col_double", None)]:
        spacing = "double" if name.endswith("double") else "single"
        rep = Report(paper=paper, table_spacing=spacing)
        rep.para("Above the exhibit.")
        if fn is None:
            add_table1_holdings(rep, pays_for=False)
        else:
            fn(rep)
        rep.para("Below the exhibit.")
        pdf = rep.save(os.path.join(workdir, f"block_{name}_{paper}.docx"))
        pages = pdf_pages_text(pdf)
        # first and last line positions across pages
        top_line = find_line(pages, "Above the exhibit.")
        bot_line = find_line(pages, "Below the exhibit.")
        pitch = 2 * 13.8  # Times New Roman 12 pt, Word's double spacing (checked against measure_plain)
        if top_line[0] == bot_line[0]:
            gap = bot_line[1]["top"] - top_line[1]["top"]
            out[name] = {"lines": round(gap / pitch - 1, 2), "inches": round((gap - pitch) / 72, 2),
                         "pages_spanned": 1}
        else:
            out[name] = {"lines": None, "pages_spanned": bot_line[0] - top_line[0] + 1}
    # headings: a Level 1 and a Level 2 between two prose lines
    for lvl in (1, 2):
        rep = Report(paper=paper)
        rep.para("Above the heading.")
        rep.heading("Heading Text", lvl)
        rep.para("Below the heading.")
        pdf = rep.save(os.path.join(workdir, f"heading{lvl}_{paper}.docx"))
        pages = pdf_pages_text(pdf)
        a, b = find_line(pages, "Above the heading."), find_line(pages, "Below the heading.")
        out[f"heading_level{lvl}"] = {"lines": round((b[1]["top"] - a[1]["top"]) / 27.6 - 1, 2)}
    return out


def fit_mock(paper="letter", exhibits=("t1", "f1", "t2"), per=120, pays_for=False, paper_title=True,
             note_spacing="double", workdir=None, verbose=True):
    """Most filler words that fit Wharton's maximum pages with the exhibits at the top of their pages: each prose
    block is filled (binary search, earlier blocks fixed) until the next exhibit is about to move to the next page;
    Section 2 ends on page 4 and Section 3 on page 12."""
    import copy
    workdir = workdir or tempfile.mkdtemp()
    s3_ex = [e for e in exhibits if e != "t1"]
    plan = {"s2_pre": 0, "s2_post": 0, "s3": [0] * (len(s3_ex) + 1)}
    counter = [0]

    def pages_for(p):
        counter[0] += 1
        pdf = build_mock(os.path.join(workdir, "fit.docx"), p, paper=paper, per=per, exhibits=exhibits,
                         pays_for=pays_for, paper_title=paper_title, note_spacing=note_spacing)
        return pdf_pages_text(pdf)

    def search(setter, hi, check):
        lo, best = 0, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(pages_for(setter(mid))):
                best, lo = mid, mid + 1
            else:
                hi = mid - 1
        return best

    def on_page(label, page):
        # monotone test for the binary search: the label starts on or before its page
        def check(pages):
            i = find_line(pages, label)[0]
            return i is not None and i <= page - 1
        return check

    def setter(key, idx=None):
        def f(v):
            p = copy.deepcopy(plan)
            if idx is None:
                p[key] = v
            else:
                p[key][idx] = v
            return p
        return f

    if "t1" in exhibits:
        plan["s2_pre"] = search(setter("s2_pre"), 600, on_page("Table 1", EXHIBIT_PAGES["t1"]))
    plan["s2_post"] = search(setter("s2_post"), 1200, on_page(SECTION3, 5))
    for i, e in enumerate(s3_ex):
        plan["s3"][i] = search(setter("s3", i), 900, on_page(EXHIBIT_LABEL[e], EXHIBIT_PAGES[e]))
    plan["s3"][-1] = search(setter("s3", len(s3_ex)), 2600, on_page(REFS, 13))
    final_pdf = build_mock(os.path.join(workdir, "fit.docx"), plan, paper=paper, per=per, exhibits=exhibits,
                           pays_for=pays_for, paper_title=paper_title, note_spacing=note_spacing)
    pages = pdf_pages_text(final_pdf)
    placed = {EXHIBIT_LABEL[e]: find_line(pages, EXHIBIT_LABEL[e])[0] + 1 for e in exhibits}
    s2 = plan["s2_pre"] + plan["s2_post"]
    s3 = sum(plan["s3"])
    res = {"paper": paper, "exhibits": list(exhibits), "paragraph_words": per, "paper_title_line": paper_title,
           "note_spacing": note_spacing, "plan": plan, "exhibit_pages": placed, "section2_words": s2,
           "section3_words": s3, "total_words": s2 + s3, "conversions": counter[0],
           "audit": audit(final_pdf, quiet=True)}
    if verbose:
        print(json.dumps(res, indent=1))
    return res, final_pdf


def measure_all():
    work = tempfile.mkdtemp(prefix="keel_measure_")
    results = {"plain": [], "blocks": {}, "fits": []}
    for paper in ("letter", "a4"):
        for per in (80, 120, 180):
            r = measure_plain(paper, per, work)
            print(r)
            results["plain"].append(r)
    results["blocks"]["letter"] = measure_blocks("letter", work)
    print(json.dumps(results["blocks"], indent=1))
    fits = [
        dict(paper="letter", exhibits=("t1", "f1")),
        dict(paper="letter", exhibits=("t1", "f1", "t2")),
        dict(paper="letter", exhibits=("t1", "f1", "t2", "t3")),
        dict(paper="letter", exhibits=("t1", "f1", "t2"), note_spacing="single"),
        dict(paper="letter", exhibits=("t1", "f1", "t2"), paper_title=False),
        dict(paper="a4", exhibits=("t1", "f1", "t2")),
    ]
    for kw in fits:
        r, pdf = fit_mock(workdir=work, **kw)
        results["fits"].append(r)
        tag = "_".join(kw["exhibits"]) + "_" + kw["paper"] + ("_notes1" if kw.get("note_spacing") == "single" else "") \
            + ("_notitle" if kw.get("paper_title") is False else "")
        shutil.copy(pdf, os.path.join(HERE, "measure_runs", f"fit_{tag}.pdf"))
        with open(os.path.join(HERE, "measurements.json"), "w") as fh:
            json.dump(results, fh, indent=1)
    with open(os.path.join(HERE, "measurements.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    return results


# =================================================================================================================
# Pour (27 Nov): a plain text file with light markup -> the report
# =================================================================================================================
POUR_HELP = """Pour format (UTF-8 text):
  %title: Report title            title-page fields: %title, %team, %members, %advisor, %wins, %school, %date
  #  Level 1 heading               ("#  Integrated Recommendation and Reflection" starts a new page)
  ## Level 2 heading
  ### Level 3 heading
  [[TABLE 1]] [[FIGURE 1]] [[TABLE 2]]   the exhibits, built from ../exhibits/exhibit_data.py
  [[PAGEBREAK]]
  [[REFERENCES]]                  every paragraph after this is one reference entry (hanging indent)
  Blank lines separate paragraphs. *italic* is honoured inside paragraphs and references."""


def _add_rich(p, text):
    parts = re.split(r"(\*[^*]+\*)", text)
    for part in parts:
        if part.startswith("*") and part.endswith("*") and len(part) > 2:
            p.add_run(part[1:-1]).italic = True
        elif part:
            p.add_run(part)


def pour(src, out_docx, paper="letter"):
    with open(src) as fh:
        raw = fh.read()
    meta = dict(re.findall(r"^%(\w+):\s*(.*)$", raw, flags=re.M))
    body = re.sub(r"^%\w+:.*$\n?", "", raw, flags=re.M)
    rep = Report(paper=paper)
    rep.title_page(meta.get("title", "[Report title]"),
                   [meta.get("team", "[Official team name]"), meta.get("members", "[Finalized team member names]"),
                    "Advisor: " + meta.get("advisor", "[Advisor first and last name]"),
                    "WInS username: " + meta.get("wins", "[Team WInS username]"), meta.get("school", "[School name]"),
                    "Wharton Global High School Investment Competition, 2026-2027", meta.get("date", "[Date]")])
    if meta.get("title"):
        rep.paper_title(meta["title"])
    in_refs = False
    for block in re.split(r"\n\s*\n", body.strip()):
        b = " ".join(x.strip() for x in block.strip().splitlines())
        if not b:
            continue
        if b == "[[REFERENCES]]":
            rep.heading(REFS, 1, new_page=True)
            in_refs = True
            continue
        if in_refs:
            _add_rich(rep.doc.add_paragraph(style="APA Reference"), b)
        elif b.startswith("### "):
            rep.heading(b[4:].strip(), 3)
        elif b.startswith("## "):
            rep.heading(b[3:].strip(), 2)
        elif b.startswith("# "):
            t = b[2:].strip()
            rep.heading(t, 1, new_page=(t == SECTION3))
        elif b == "[[TABLE 1]]":
            add_table1_holdings(rep)
        elif b == "[[FIGURE 1]]":
            add_figure1_reserve(rep)
        elif b == "[[TABLE 2]]":
            add_table2_markets(rep)
        elif b == "[[PAGEBREAK]]":
            rep.page_break()
        else:
            _add_rich(rep.doc.add_paragraph(style="APA Body"), b)
    pdf = rep.save(out_docx)
    words = len(re.sub(r"\[\[.*?\]\]|^#+ .*$", "", body.split("[[REFERENCES]]")[0], flags=re.M).split())
    res = audit(pdf)
    print(f"Prose words (headings and exhibits excluded): {words}")
    return res


# =================================================================================================================
def demo():
    """The format test: a 12-page mock (title page, Section 2 with Table 1, Section 3 with Figure 1 and Table 2,
    References), filler sized from the measured fit so that each section fills its maximum pages."""
    plan = DEMO_PLAN
    path = os.path.join(HERE, "template_test.docx")
    pdf = build_mock(path, plan, exhibits=("t1", "f1", "t2"))
    res = audit(pdf)
    crop_previews(pdf)
    return res


# From measurements.json (Letter; Table 1, Figure 1 and Table 2 at the tops of pages 3, 6 and 8): the most filler
# words that fit twelve pages. Rerun `measure` and update this if the exhibits change size.
DEMO_PLAN = {"s2_pre": 299, "s2_post": 401, "s3": [300, 418, 1480]}


def crop_previews(pdf):
    """PNG previews of Table 1 and Table 2 as laid out in the PDF (number, title, body and note), for the exhibits
    folder. Uses pdftoppm at 150 dpi and crops by the text positions."""
    pages = pdf_pages_text(pdf)
    for label, out in (("Table 1", "exhibit1_holdings_preview.png"), ("Figure 1", "exhibit2_reserve_preview.png"),
                       ("Table 2", "exhibit3_markets_preview.png")):
        pi, ln = find_line(pages, label)
        if pi is None:
            continue
        # end: the first body line ("Below"/prose) after the note; take the note line that starts with "Note."
        lns = lines_of(pages[pi]["words"])
        start = ln["top"] - 6
        end = None
        seen_note = False
        for x in lns:
            if x["top"] <= ln["top"]:
                continue
            if x["text"].startswith("Note."):
                seen_note = True
            elif seen_note and x["top"] - prev_bottom > 20:     # the blank line after the note
                end = prev_bottom + 6
                break
            prev_bottom = x["bottom"]
        if end is None:
            end = prev_bottom + 6
        dpi = 150
        tmp = tempfile.mkdtemp()
        subprocess.run(["pdftoppm", "-f", str(pi + 1), "-l", str(pi + 1), "-r", str(dpi), "-png", pdf,
                        os.path.join(tmp, "p")], check=True)
        png = [os.path.join(tmp, x) for x in os.listdir(tmp)][0]
        s = dpi / 72
        y0, y1 = int(start * s), int(end * s)
        subprocess.run(["convert", png, "-crop", f"{int(612 * s - 2 * 54 * s)}x{y1 - y0}+{int(54 * s)}+{y0}",
                        "+repage", os.path.join(EXHIBITS, out)], check=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["demo", "measure", "pour", "audit", "fit"])
    ap.add_argument("path", nargs="?")
    ap.add_argument("--paper", default="letter", choices=list(PAPER))
    ap.add_argument("--exhibits", default="t1,f1,t2")
    a = ap.parse_args()
    os.makedirs(os.path.join(HERE, "measure_runs"), exist_ok=True)
    if a.mode == "demo":
        demo()
    elif a.mode == "measure":
        measure_all()
    elif a.mode == "fit":
        fit_mock(paper=a.paper, exhibits=tuple(a.exhibits.split(",")))
    elif a.mode == "pour":
        if not a.path:
            sys.exit(POUR_HELP)
        pour(a.path, os.path.splitext(a.path)[0] + ".docx", paper=a.paper)
    elif a.mode == "audit":
        audit(a.path)
