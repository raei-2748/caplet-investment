# The Final Report template (Tue 10 Nov 2026)

A page template in Wharton's exact format, the measurements made with it, and the tool that pours the 27 Nov text
into it. No report text lives here: the filler is the Declaration of Independence (public domain, National Archives
transcription, `filler_declaration.txt`). Exhibit designs: `../exhibits/specs.md`. Sources and verdicts: card
`../research/cards/Q23_exhibits_and_format.md`.

## What the template does

| Rule | Source | In the template |
|---|---|---|
| 12-pt Times New Roman | Wharton | Every style, tables and figure labels included (figures drawn in Times New Roman metrics) |
| Double-spaced; no extra space between paragraphs; 0.5 in first-line indent; left-aligned | Wharton; APA 7 | Body style "APA Body" (Word's double spacing: 27.6 pt, 23 lines a Letter page) |
| 1-inch margins | Wharton; APA | All four sides |
| Page numbers bottom left | Wharton (APA says top right; Wharton wins) | Footer field on every page, title page = 1 |
| Paper size | Not stated by Wharton; its own PDFs are US Letter | Letter (A4 measured for comparison) |
| Title page: team name, advisor, members, WInS username, matching the roster | Wharton | Placeholders in brackets; Caplet fills them |
| Paper title repeated, bold and centred, on page 2 | APA 7 | "APA Paper Title" (optional, one line) |
| Level 1 headings centred bold; Level 2 flush left bold; Level 3 flush left bold italic; no blank lines around headings | APA 7 | Word's built-in Heading 1-3, restyled (so Word's navigation pane and PDF bookmarks work) |
| Section 3 and References start on a new page | Keel's call (Wharton's page limits are per section) | page-break-before on those two headings |
| Tables: number bold, title italic, body single-spaced, borders top / under heads / above total / bottom, notes "*Note.*" double-spaced | APA 7; Wharton allows single-spaced tables and graphics | `Report.table()` |
| Figures: number bold, title italic, image, note | APA 7 | `Report.figure()` |
| Exhibits at the top of a page, one blank line before the text | APA 7 | `top=True` |
| References on a new page, label centred bold, entries double-spaced with a 0.5 in hanging indent | Wharton; APA 7 | `Report.references()` |
| PDF at most 5 MB; no links to open | Wharton | The audit reports size and link annotations |

## How to use it

```
python3 keel/final_report/template/build_template.py demo          # template_test.docx/.pdf + exhibit previews
python3 keel/final_report/template/build_template.py measure       # every measurement -> measurements.json (~15 min)
python3 keel/final_report/template/build_template.py fit --exhibits t1,f1,t2 --paper letter
python3 keel/final_report/template/build_template.py pour report.md   # 27 Nov
python3 keel/final_report/template/build_template.py audit some.pdf   # any PDF: pages per section, size, fonts, links
```

Needs python-docx, pdfplumber and LibreOffice (`soffice`); the figure needs matplotlib
(`python3 keel/final_report/exhibits/build_exhibits.py`). Exhibit data: `../exhibits/exhibit_data.py`, which cites
NUMBERS.md by section; change it there and rebuild.

**The 27 Nov pour.** Write the report as plain text: `%title:`, `%team:`, `%members:`, `%advisor:`, `%wins:`,
`%school:`, `%date:` lines for the title page; `# ` Level 1 (`# Portfolio Implementation`, `# Integrated
Recommendation and Reflection`), `## ` Level 2, `### ` Level 3; `[[TABLE 1]]`, `[[FIGURE 1]]`, `[[TABLE 2]]` where each
exhibit goes; `[[REFERENCES]]` and then one reference per paragraph; `*italics*` inside text. Run `pour`; it writes
`report.docx` and `report.pdf`, prints the prose word count and audits the pages (title 1, Section 2 two to three,
Section 3 six to eight, 9-12 without References, at most 5 MB). Then open `report.docx` in the program Caplet will
submit from (Word, or Google Docs by upload), check the font shows as Times New Roman, export to PDF, and run `audit`
on that PDF: its font list must say TimesNewRoman, not LiberationSerif.

## Measurements (Letter unless stated; filler words average 5.07 characters)

**A full page of prose.** 23 lines at a 27.6-pt pitch, 14.3 words a line.

| Paragraph length | Words on a full page (three pages measured) |
|---|---|
| 80 words | 303-320 |
| 120 words | 313-339 |
| 180 words | 331-352 |
| A4, 120 words | 332-356 (24-25 lines) |

Word length moves this more than anything else: at Caplet's IPS's 4.66 characters a word a page holds about 350
words; at the case study's 5.81, about 290 (arithmetic on the measured line capacity of about 87 characters).

**What each block costs** (double-spaced lines of 23 a page; one line is about 14 words):

| Block | Lines | About |
|---|---|---|
| Level 1 or Level 2 heading | 1.0 | 14 words |
| Paper title on page 2 | 1.0 | 14 words |
| Table 1, holdings, 5 columns, single-spaced body, 3-line note | 14.1 | 200 words (5.4 in) |
| Table 1 with a sixth "Pays for" column (names wrap) | 18.1 | 260 words |
| Table 1 with a double-spaced body | does not fit one page | |
| Figure 1, the reserve (6.5 x 3.85 in image, 3-line note) | 16.0 | 230 words (6.2 in) |
| Table 2, four markets (placeholder cells) | 11.1 | 160 words |
| Table 3, a seven-row monitoring table (filler cells) | 17.1 | 245 words |

**Words of prose that fit at the maximum, twelve pages** (exhibits at the top of their pages; Section 2 = pages 2-4,
Section 3 = pages 5-12; headings as SKELETON v2: paper title, two Level 1, four Level 2 in Section 2, six in Section 3):

| Exhibits placed | Variant | Section 2 prose | Section 3 prose | Total prose | Pages (title / S2 / S3 / with References) | PDF |
|---|---|---|---|---|---|---|
| Table 1, Figure 1 | Letter, standard | 700 | 2,330 | **3,030** | 1 / 3 / 8 / 13 | 0.31 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | Letter, standard | 700 | 2,198 | **2,898** | 1 / 3 / 8 / 13 | 0.33 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2, Table 3 | Letter, standard | 700 | 1,962 | **2,662** | 1 / 3 / 8 / 13 | 0.34 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | Letter, notes single-spaced | 740 | 2,201 | **2,941** | 1 / 3 / 8 / 13 | 0.33 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | Letter, no paper title on page 2 | 708 | 2,198 | **2,906** | 1 / 3 / 8 / 13 | 0.32 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | A4, standard | 744 | 2,313 | **3,057** | 1 / 3 / 8 / 13 | 0.33 MB, 0 links, ok=True |

Read-out: SKELETON v2's three exhibits leave **2,898 words** (about 2,800-2,850 in real text); two exhibits leave
3,030; a fourth (the monitoring table) takes 236 more and leaves 2,662. **Section 2 is 700 in every Letter fit: that
is its three-page ceiling with Table 1, not a target** (budget about 650). Single-spaced notes add about 40 words and
dropping the paper title about 10 (both within noise of a line or two); A4 holds about 160 more (5.5%), so a draft
written on A4 runs about half a page over when exported to Letter. At Wharton's nine-page minimum the same plan holds
about 1,900 words (estimate: three pages fewer at about 330; not measured). Every fit PDF can be rebuilt with `build_template.py` (the PDFs are not kept in the repo).

## Caveats

- **Layout engine.** LibreOffice with Liberation Serif, which has Times New Roman's character widths; the line pitch
  matches Word's double spacing exactly. Google Docs has not been measured. Re-run `audit` on the real export.
- **Filler is not prose.** Filler paragraphs are cut at a word count, not at a sentence; real paragraphs of mixed
  length lose a little more at their last lines. Treat the fits as the ceiling, about 2-3% above what real text gets.
- **Noise between fits.** Each block of filler starts where the last one stopped, so its word lengths differ from fit
  to fit; differences under about 30 words between two fits are noise, not an effect.
- **Widow and orphan control is on** (Word's default), which occasionally moves a line to the next page (one page in
  the measurements had 22 lines).
- **The test PDF embeds Liberation Serif.** It shows the layout; it is not a file to submit.

## Files

- `build_template.py`: the template, the measurements, `pour` and `audit`.
- `filler_declaration.txt`: public-domain filler for measuring.
- `template_test.docx`, `template_test.pdf`: the format test, twelve pages and References, with Tables 1 and 2 and
  Figure 1 in place.
- `measurements.json`: every number above. `measure_runs/` (rebuilt on demand, not kept): the PDF of each fit.
