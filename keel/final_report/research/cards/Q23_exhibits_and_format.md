# Q23 research cards: Wharton's page format measured, and the exhibits designed

**Date.** Tue 10 Nov 2026 (Sydney), Mon 9 Nov in the US. Web sources were read at the source that day (Parallel
web_search and web_fetch) unless a row says otherwise. Measurements were made with `../../template/build_template.py`
(python-docx, LibreOffice 7 headless, pdfplumber); numbers in `../../template/measurements.json`.

**Notes for the Final Report store, not report prose.** Exhibit figures come only from `../../NUMBERS.md` (sections
named in each row); the specs are `../../exhibits/specs.md`.

**Why this card.** Scorecard rows "Exhibits" and "Minimum requirements" were the weakest (2). Wharton's instructions
fix the report's length in pages, not words, and say "Tables and graphics may be single-spaced when needed for
readability. Graphics should support the narrative and clarify the team's analysis rather than distract from it."
The skeleton's budgets rest on one untested claim (a double-spaced page holds about 280-300 words), and the exhibits
were described but never drawn.

**Claims tested.**
1. CASE_MAP E and SKELETON v2: "In Wharton's exact format a double-spaced page holds about 280-300 words of prose, so
   9-12 pages leave about 2,700-2,900 words once the exhibits are placed" (SKELETON v2: about 700 words in Section 2,
   about 2,000 in Section 3, 2,700 in all).
2. SKELETON: "Two exhibits beyond the holdings table answer two case questions at a glance."

**Problem class.** Document engineering under a page cap (fitting fixed content into fixed pages, as in grant
proposals with page limits), plus information design for a print reader (table versus chart, APA layout). Prior art:
APA 7's paper-format and table/figure rules; Tufte and Few on tables versus graphs; the usability five-second test;
metric-compatible fonts for measuring layout without the licensed font.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Wharton lets tables and graphics be single-spaced "when needed for readability"; everything else is double-spaced | Wharton Global Youth Program (2026b), Final Report instructions, "Required Format and Submission" | PROCESS | TEXTBOOK | Table 1 is only whole on one page because of this allowance (row 9) | "When needed for readability" is a condition: use it for tables and figures, never to squeeze prose | VERIFIED: competition/official/2026_27/2026_WGY_Final_Report_Instructions.txt | no | Repo, official file |
| 2 | Wharton: "Graphics should support the narrative and clarify the team's analysis rather than distract from it"; Creativity and Presentation rewards "supporting data, projections, graphics ... used purposefully" | Wharton Global Youth Program (2026b), Final Report instructions, format section and evaluation criteria | PROCESS | TEXTBOOK | Each exhibit must answer one case question named in its spec, or it goes | None | VERIFIED: same file | no | Repo, official file |
| 3 | Wharton names no paper size; its own instructions PDF is US Letter (612 x 792 pt), as are its other 2026-27 PDFs checked | Wharton Global Youth Program (2026b), Final Report instructions PDF (pdfinfo) | PROCESS | NICHE | Build on Letter from the first draft; the template does | A4 is not banned; it is a risk only if the team drafts on one size and exports on the other | VERIFIED: pdfinfo on competition/official/2026_27/2026_WGY_Final_Report_Instructions.pdf | no | Repo, official file |
| 4 | Word installed in Australia opens new documents on A4 (Office takes the size from the regional setting at install); Google Docs keeps a per-user default | Office Watch (2022, 2026); Proofed (2021); Google (n.d.), Docs Editors Help "Change page settings" | PROCESS | NICHE | Caplet works in Sydney: a draft started on A4 holds 24-25 lines a page against Letter's 23, so a 12-page A4 draft becomes about 12.5 Letter pages | Office Watch and Proofed are secondary (tech publishers), not Microsoft | VERIFIED: office-watch.com/2022/two-ways-change-word-opening-paper-size and getproofed.com.au, read 10 Nov | no | Web |
| 5 | Measured: a full Letter page in Wharton's format holds 23 lines at a 27.6-pt pitch (Word's double spacing for 12-pt Times New Roman), 14.3 words a line, 313 to 352 words with 120-180-word paragraphs (303 to 320 with 80-word paragraphs) | Own measurement, template/measurements.json "plain" | PROCESS | NICHE | The page budget: about 330 words a full page, not 280-300 | Filler is the Declaration of Independence (5.07 characters a word); shorter words give more, longer fewer (row 6) | VERIFIED (own measurement; LibreOffice with Liberation Serif, metric-compatible with Times New Roman, row 24) | no | template/build_template.py measure |
| 6 | Words a page depend on word length: about 350 at Caplet's IPS's 4.66 characters a word, about 320 at Keel's cards' 5.2, about 290 at the case study's 5.81 | Own arithmetic: line capacity of about 87 characters including spaces (14.26 words x 6.07) divided by each text's characters per word plus one, times 23 lines | PROCESS | NICHE | The 280-300 claim holds only for prose as long-worded as Wharton's own case study; plain English with short words gets about 330-350 | Ignores digits and capitals being wider than average letters; a check in the real draft on 27 Nov settles it | VERIFIED (own arithmetic on own measurement); word lengths measured on FINAL_IPS_as_submitted.txt, the case study text and Q16 | no | This card |
| 7 | An APA Level 1 or Level 2 heading costs exactly one double-spaced line (about 14 words); APA forbids blank lines above or below headings | Own measurement; American Psychological Association (n.d.-a), "Headings" | PROCESS | KNOWN | Section 2's title, Level 1 and four Level 2 headings cost six lines (about 85 words); Section 3's Level 1 and six Level 2 cost seven (about 100) | Fewer headings buy prose, but Wharton's sections and the case's questions are what judges look for; keep them | VERIFIED: apastyle.apa.org/style-grammar-guidelines/paper-format/headings, read 10 Nov; own measurement | no | Web; template |
| 8 | APA repeats the paper title, bold and centred, on the first line of the first page of text, and needs no "Introduction" heading | American Psychological Association (2021), Publication Manual student paper checklist; APA (n.d.-a) | PROCESS | KNOWN | Costs one line on page 2; measured with and without (row 33) | Optional for Wharton, which asks APA only for citations; keeping it looks finished | VERIFIED: apastyle.apa.org/instructional-aids/publication-manual-formatting-checklist.pdf, read 10 Nov | no | Web |
| 9 | Table 1 (13 holdings and a total) measures 14.1 double-spaced lines with a single-spaced body; with a double-spaced body it cannot fit on one page (it spans two) | Own measurement (blocks: table1_5col_single, table1_5col_double) | RESERVE2033, PROCESS | NICHE | The required table costs about 200 words of prose; use Wharton's single-spacing allowance for its body | Number, title and note stay double-spaced (APA), which is 7 of the 14 lines | VERIFIED (own measurement) | no | template |
| 10 | Full fund names need 3.04 inches at 12 pt, so a sixth column ("Pays for", asked by panel 1) wraps every iBond row and costs 4 more lines (18.1 against 14.1) | Own measurement with the Liberation Serif metrics | PROCESS | NICHE | Keep Wharton's five columns; Figure 1's "Paid from" column does the mapping | The panel's wish is met elsewhere, not dropped | VERIFIED (own measurement) | no | template; exhibits/specs.md |
| 11 | Wharton's own example table uses the short asset types "Stock", "ETF", "Treasury Bond", "Cash", and whole dollars | Wharton Global Youth Program (2026b), Final Report instructions, "Example Portfolio Table" | PROCESS | KNOWN | Table 1 uses "ETF" and "Treasury bond", which frees the width for one-line names; it keeps cents because they match the WInS record | NUMBERS 8g says "ETF (Treasury)"; the names still say Treasury | VERIFIED: official file | no | Repo, official file |
| 12 | Figure 1 (the reserve, 6.5 x 3.85 in image, three-line note) measures 16.0 lines, about 230 words of prose | Own measurement (blocks: figure1) | RESERVE2033 | NICHE | The biggest single exhibit; trimming the image to 3.4 in would save about 1.5 lines | Smaller type inside it would fall below 10 pt | VERIFIED (own measurement) | no | template |
| 13 | Table 2 (four markets by four outcomes) measures 11.1 lines, about 160 words | Own measurement (blocks: table2_markets) | COSPONSOR, RANGE2031 | NICHE | The cheapest way to answer "favorable and unfavorable market outcomes" | Placeholder cells; Q24's real wording may run longer | VERIFIED (own measurement, placeholder data) | no | template |
| 14 | A seven-row monitoring table measures 17.1 lines (about 245 words of prose displaced) while holding about 160 words of content single-spaced | Own measurement (blocks: table3_monitoring, filler cells of realistic length) | MONITOR, PROCESS | NICHE | If 3e's monitoring table is used, it is a fourth exhibit; SKELETON v2's "about a page" for Exhibits 2 and 3 leaves it out | Tables of words read slower than prose; legitimate only if the content is truly a grid (signal, when, what it changes, what it never changes) | VERIFIED (own measurement) | no | template |
| 15 | APA table rules: number bold; title one double-spaced line below in italic title case; body single, 1.5 or double; column heads centred in sentence case; borders only top, under heads, above totals and bottom; no vertical rules; notes start "Note." | American Psychological Association (n.d.-b), "Table setup" | PROCESS | TEXTBOOK | Table 1 and Table 2 follow it exactly | None | VERIFIED: apastyle.apa.org/style-grammar-guidelines/tables-figures/tables, read 10 Nov | no | Web |
| 16 | APA: use the same font in tables as in the text; inside figure images use a sans-serif font of 8-14 pt. Wharton: "Use 12-point Times New Roman font" | American Psychological Association (n.d.-c), "Font"; Wharton Global Youth Program (2026b) | PROCESS | NICHE | Keel's call: Times New Roman inside figures too (at least 10 pt), because Wharton's rule ranks first and asks APA only for citations | A strict APA reader could prefer sans serif in the image; a strict Wharton reader would mark a second font | VERIFIED: apastyle.apa.org/style-grammar-guidelines/paper-format/font, read 10 Nov | no | Web |
| 17 | APA numbers tables and figures separately, in the order the text mentions them; each is placed after its first call-out, at the top or bottom of a page, with one blank double-spaced line before the text | American Psychological Association (n.d.-b); (n.d.-d), "Figure setup" | PROCESS | TEXTBOOK | The report says Table 1, Figure 1, Table 2 (not "Exhibit 1-3"); the template places each at the top of a page | Top-of-page placement can strand a few lines at the foot of the page before | VERIFIED: apastyle.apa.org tables and figures pages, read 10 Nov | no | Web |
| 18 | APA double-spaces table and figure numbers, titles and notes, but lets the table body and the words inside a figure image be single-spaced | American Psychological Association (n.d.-e), "Line spacing" | PROCESS | TEXTBOOK | A note longer than two lines costs a line each; keep notes to three lines | Single-spacing the notes too would save about 1.5 lines an exhibit under Wharton's allowance, at the cost of APA form (row 34) | VERIFIED: apastyle.apa.org/style-grammar-guidelines/paper-format/line-spacing, read 10 Nov | no | Web |
| 19 | APA paragraphs: first line indented 0.5 in, left-aligned and ragged right, no extra space before or after paragraphs, no manual hyphens | American Psychological Association (n.d.-f), "Paragraph alignment and indentation"; APA (2025), Student paper setup guide | PROCESS | TEXTBOOK | The template's body style; Google Docs and Word defaults may add space after paragraphs, which costs lines | None | VERIFIED: apastyle.apa.org/style-grammar-guidelines/paper-format/paragraph-format, read 10 Nov | no | Web |
| 20 | When length is counted in words, APA counts every word in the paper "but do not count words in figure images" | American Psychological Association (2021), Publication Manual student paper checklist, "Paper Length" | PROCESS | KNOWN | Wharton counts pages, so labels inside Figure 1 cost page space but no prose; information put in a figure's labels is cheap only if it reads at a glance | Not a licence to move prose into images | VERIFIED: APA checklist PDF, read 10 Nov | no | Web |
| 21 | "Tables usually outperform graphics in reporting on small data sets of 20 numbers or less. The special power of graphics comes in the display of large data sets." | Tufte (2001), ch. 2 | PROCESS | TEXTBOOK | Table 2 (16 numbers) is a table; the all-Treasury comparison (4 numbers) is a sentence; Figure 1 (dozens of dates and amounts with a shape) is a graphic | A rule of thumb, not a law; Few (row 22) refines it by task | VERIFIED: scanned chapter at lmscontent.embanet.com/USC/CMGT587/Tufte Ch2 and 5.pdf, read 10 Nov | no | Web |
| 22 | Tables work best to look up individual values or when values must be precise; graphs when the message is in the shape of the data (patterns, trends, exceptions) | Few (2005), Effectively communicating numbers | PROCESS | TEXTBOOK | Table 1 is a look-up of exact amounts (table); Figure 1's message is a shape, a staircase that steps down one holding a year and turns from funds to bonds (graph) | None | VERIFIED: perceptualedge.com/articles/Whitepapers/Communicating_Numbers.pdf, read 10 Nov | no | Web |
| 23 | "Communication is most effective when you say neither more nor less than what is relevant to your message"; bars suit discrete values compared one by one | Few (2009), Visual communication: Core design principles (IBM white paper) | PROCESS | KNOWN | Figure 1 shows one holding per payment and nothing else; the reserve's dollar value is left to the prose | None | VERIFIED: public.dhe.ibm.com Few white paper, read 10 Nov | no | Web |
| 24 | Liberation Serif is metrically identical to Times New Roman (same character widths), so page measurements made with it hold for Times New Roman | Red Hat (2007/2011), "Liberation fonts"; Fedora Project (n.d.); Liberation fonts (Wikipedia) | PROCESS | NICHE | The measurements transfer to Word with real Times New Roman; the test PDF itself embeds Liberation Serif, so the submitted PDF must come from Word or Google Docs with Times New Roman (the audit lists fonts) | Vertical metrics can differ slightly between programs; re-measure once in the program Caplet uses | VERIFIED: redhat.com/en/blog/liberation-fonts and fedoraproject.org wiki, read 10 Nov | no | Web |
| 25 | Wharton puts page numbers bottom left, overriding APA's top right; APA student papers need no running head | Wharton Global Youth Program (2026b); American Psychological Association (2025), Student paper setup guide | PROCESS | KNOWN | Template footer: page number bottom left on every page, title page included (APA numbers the title page 1) | Whether the title page shows its number is not stated by Wharton; showing it is the APA default | VERIFIED: both read | no | Repo; Web |
| 26 | Section page limits are per section (title 1, Section 2 two to three, Section 3 six to eight), so each section should start on a new page to make the count auditable | Wharton Global Youth Program (2026b), "Required Report Length"; Keel's call | PROCESS, MINREQ | NICHE | The template starts Section 3 and References on new pages, and the audit reports pages per section | Costs the unused part of page 4 if Section 2 is short; fill it or cut to two pages | VERIFIED (Wharton's table); the page-break rule is Keel's call | no | template |
| 27 | The test PDF with one 300-dpi figure is about 0.3 MB, far under the 5 MB limit; no link annotations | Own measurement (audit) | PROCESS, MINREQ | KNOWN | Size is no risk unless photos are added; keep figures at 300 dpi PNG | Word's PDF export can embed fonts differently; run the audit on the exported file | VERIFIED (own measurement) | no | template |
| 28 | Wharton: "Do not include external links that evaluators are expected to open"; APA reference entries carry URLs | Wharton Global Youth Program (2026b); APA (2025) | PROCESS, MINREQ | NICHE | Keep URLs in References as plain text (no hyperlink), never in the body as something to click | Keel's reading; Wharton has not said whether reference URLs count | UNVERIFIED (Wharton's intent) | no | Repo; Web |
| 29 | The five-second test: show a design for five seconds, hide it, ask what was remembered; it measures first impressions, not full understanding | Perfetti (2007); Gronier (2016) | PROCESS | KNOWN | Each exhibit names the one question a first reader should answer; Keel's own first look passed Table 1 and Figure 1 and failed the range chart | Keel looking at its own drafts is not a test with fresh readers; Gronier found it measures perceived, not actual, usability | VERIFIED: articles.centercentre.com/five_second_test and guillaumegronier.com 2016 JUS paper, read 10 Nov | no | Web |
| 30 | The reserve as a staircase of holdings, each ending at its 1 January payment, shows size by count, composition by shade and change by the step, without showing $427,028 against $500,000 owed | Own design on NUMBERS 8h | RESERVE2033, LIQUIDITY | NICHE | Answers the case's "how its composition should change ... as the annual payments approach and are made" in one picture, and names liquidity (when each payment's cash arrives) | The half-month waits are too short to see; only the two long waits show | VERIFIED (own drawing on register figures) | no | exhibits/build_exhibits.py |
| 31 | A chart of the 2031 range forming (bands narrowing from 2026 to 2031) fails the five-second test: readers cannot tell which band is which end without the legend, and its bands mix two risks | Own drawing on NUMBERS 4 placeholders | RANGE2031 | NICHE | Supports SKELETON v2's switch to a scenario table | Keel's own look, not a panel | VERIFIED (own drawing) | no | exhibits/exhibit3_range_candidate.png |
| 32 | APA figure and table notes should name where the data come from ("Data from ...") and define anything the image cannot | American Psychological Association (n.d.-b, n.d.-d) | PROCESS | TEXTBOOK | Figure 1's note should cite the Treasury curve in APA form (U.S. Department of the Treasury, 2026) and the curve go in References | Figure 1's draft note now carries it; the curve still has to go in References on 27 Nov | VERIFIED: APA tables and figures pages ("notes ... copyright attribution"); the exact "Data from" wording was not read on those pages (UNVERIFIED) | no | Web |
| 33 | Measured prose at twelve Letter pages, exhibits at the top of their pages: 3,030 words with Table 1 and Figure 1; 2,898 with Table 2 added; 2,662 with a fourth, monitoring table (Table 3); Section 2 is 700 in each (its three-page ceiling); without the paper title on page 2, 2,906 | Own measurement (fits) | PROCESS | NICHE | SKELETON v2's 2,700 (700 + 2,000) fits three exhibits with about 100-150 words to spare in real text; with four, Section 3's 2,000 is about 40 over; Section 2's 700 is the ceiling itself, so budget 650 there | Filler paragraphs end mid-sentence; real paragraphs of mixed length lose a little more at their last lines | VERIFIED (own measurement) | no | template measure |
| 34 | Small levers measured with three exhibits: single-spaced exhibit notes add about 40 words (2,941); dropping the paper title about 10 (2,906); A4 paper holds 3,057, 159 (5.5%) more than Letter | Own measurement (fits) | PROCESS | NICHE | None is worth taking: keep APA's double-spaced notes and the paper title, and build on Letter from the first draft so the 27 Nov text does not overrun when exported | APA asks notes double-spaced | VERIFIED (own measurement) | no | template measure |

References for the rows (APA 7; access date 10 Nov 2026 for web sources):
- American Psychological Association. (n.d.-a). *Headings*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/paper-format/headings
- American Psychological Association. (n.d.-b). *Table setup*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables
- American Psychological Association. (n.d.-c). *Font*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/paper-format/font
- American Psychological Association. (n.d.-d). *Figure setup*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/figures
- American Psychological Association. (n.d.-e). *Line spacing*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/paper-format/line-spacing
- American Psychological Association. (n.d.-f). *Paragraph alignment and indentation*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/paper-format/paragraph-format
- American Psychological Association. (2021). *Publication manual, 7th edition: Student paper checklist*. https://apastyle.apa.org/instructional-aids/publication-manual-formatting-checklist.pdf
- American Psychological Association. (2025). *Student paper setup guide* (7th ed.). https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf
- Few, S. (2005). *Effectively communicating numbers: Selecting the best means and manner of display*. Perceptual Edge. https://www.perceptualedge.com/articles/Whitepapers/Communicating_Numbers.pdf
- Few, S. (2009). *Visual communication: Core design principles for displaying quantitative information* [White paper]. IBM. https://public.dhe.ibm.com/software/data/sw-library/cognos/pdfs/whitepapers/wp_visual_communications_core_design_principles.pdf
- Gronier, G. (2016). Measuring the first impression: Testing the validity of the 5 second test. *Journal of Usability Studies, 12*(1), 8-25. https://uxpajournal.org/measuring-testing-validity-5-second-test/ (volume, issue and pages checked on the ACM Digital Library record, https://dl.acm.org/doi/abs/10.5555/3040226.3040228, 10 Nov; the paper was read at https://www.guillaumegronier.com/resources/2016_JUS_Gronier.pdf)
- Office Watch. (2022, October 2). *Two ways to change Word's opening paper size*. https://office-watch.com/2022/two-ways-change-word-opening-paper-size
- Perfetti, C. (2007, September 11). *5-second tests: Measuring your site's content pages*. Center Centre. https://articles.centercentre.com/five_second_test/
- Proofed. (2021, February 27). *How to change the paper size in Microsoft Word*. https://getproofed.com.au/writing-tips/how-to-change-the-paper-size-in-microsoft-word
- Red Hat. (2011, June 3). *Liberation fonts* [Blog post]. https://www.redhat.com/en/blog/liberation-fonts
- Tufte, E. R. (2001). *The visual display of quantitative information* (2nd ed.). Graphics Press.
- Wharton Global Youth Program. (2026b). [Final Report instructions, 2026–2027 Wharton Global High School Investment Competition]. Unpublished document distributed to registered teams (REFERENCES_APA row 121). Filed as competition/official/2026_27/2026_WGY_Final_Report_Instructions.pdf.

## (b) Cards: the strongest ideas

**1. The page holds about 330 words, not 280-300 (rows 5, 6).**
- What is it? A direct measurement: Wharton's format (12-pt Times New Roman metrics, double-spaced, 1-inch margins,
  Letter, APA paragraphs) lays out 23 lines a page at 14.3 words a line, 313-352 words on a full page of
  120-180-word paragraphs.
- Did it work? Yes: three independent pages agree within 13%, and the line pitch (27.6 pt) is exactly Word's double
  spacing for Times New Roman, so the layout engine matches Word.
- How is the report like it? The report is plain English with short words (Caplet's IPS averages 4.66 characters a
  word), which packs more words a line than the filler (5.07).
- How is it not? Real paragraphs vary, end on short lines, and carry wide figures like "$115,929"; Wharton's case
  style (5.81 characters) would give about 290.
- What Caplet takes: budget about 330 words for a full page of prose, and check on 27 Nov with the audit, not a
  rule of thumb.

**2. The required table only fits because of the single-spacing allowance (rows 1, 9, 10, 11).**
- What is it? Table 1 at 12 pt with a single-spaced body is 14.1 lines; double-spaced it spans two pages; with a
  sixth column it wraps every fund name.
- Did it work? Yes: with Wharton's five columns, Wharton's own short asset types and tight cell padding, every row is
  one line and the table is a clean half page plus its note.
- How is the report like it? The table is a minimum requirement ("Actual holdings"); a broken or split table is the
  most visible format fault a judge could find.
- How is it not? The panel wanted a "Pays for" column; it does not fit, so that job moves to Figure 1.
- What Caplet takes: five columns, single-spaced body, numbers to the cent, the table at the top of page 3, and the
  bond identifiers filled from the final export.

**3. Choose the form by the job: table for look-up, chart for shape, sentence for four numbers (rows 21, 22, 23).**
- What is it? Tufte's 20-number rule and Few's look-up versus shape test.
- Did it work? It settled three choices: Table 1 (exact amounts, look-up) is a table; Figure 1 (a staircase of ten
  holdings, its message a shape) is a graphic; Table 2 (16 numbers) is a table; the all-Treasury comparison (4
  numbers) is a sentence.
- How is the report like it? Judges read many reports in a stack; the exhibit that answers at a glance wins the
  Creativity and Presentation criterion's "used purposefully".
- How is it not? Tufte wrote for statistical graphics in print; a judge may read on screen and zoom.
- What Caplet takes: no exhibit without a case question it answers; no chart for fewer than about 20 numbers.

**4. The reserve as a staircase (rows 12, 30).**
- What is it? Figure 1: one row per payment, each holding's bar ending at its 1 January payment; light grey funds
  give way to dark grey bonds after 2037; the two long waits labelled in words; what each pays above $50,000 at
  forward rates in a right-hand column.
- Did it work? On Keel's first look, yes: the one holding per payment, the switch to bonds and the two long waits are
  seen before any label is read.
- How is the report like it? It answers the case's reserve question ("how its composition should change ... as the
  annual payments approach and are made") and names liquidity, which panel 1 found missing.
- How is it not? It leaves the reserve's dollar size to the prose (on purpose: the $427,028 against $500,000
  comparison needs its sentence).
- What Caplet takes: Figure 1 in 3a, called out before it appears, with the Treasury curve cited in its note.

**5. Four exhibits do not fit the budget the skeleton assumed (rows 13, 14, 33).**
- What is it? The measured fits at twelve pages with two, three and four exhibits.
- Did it work? See section (c).
- How is the report like it? SKELETON v2 counts Exhibits 2 and 3 at "about a page" and plans a monitoring table in 3e
  as well; that is a fourth exhibit.
- How is it not? A monitoring table may replace about as many words of 3e prose as it displaces.
- What Caplet takes: decide by 16 Nov whether the monitoring table is Table 3 (and 3e's prose shrinks by its size) or
  a paragraph.

## (c) Verdicts with the measurements

All prose counts below are ceilings measured on Letter at twelve pages (the maximum), with 120-word filler
paragraphs, every exhibit at the top of its page, and SKELETON v2's headings. Real text lands about 2-3% lower
(paragraphs end on short lines), and word length moves it most (row 6).

**Claim 1. "A double-spaced page holds about 280-300 words of prose, so 9-12 pages leave about 2,700-2,900 words once
the exhibits are placed." Verdict: CHANGE the first half; KEEP the second half only for three exhibits at twelve pages.**
- **Words a page: CHANGE to about 330.** A full Letter page measured 303-352 words (23 lines, 14.3 words a line).
  280-300 holds only for prose with words as long as the case study's (5.81 characters).
- **Words left for prose at twelve pages:**

| Exhibits placed | Variant | Section 2 prose | Section 3 prose | Total prose | Pages (title / S2 / S3 / with References) | PDF |
|---|---|---|---|---|---|---|
| Table 1, Figure 1 | Letter, standard | 700 | 2,330 | **3,030** | 1 / 3 / 8 / 13 | 0.31 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | Letter, standard | 700 | 2,198 | **2,898** | 1 / 3 / 8 / 13 | 0.33 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2, Table 3 | Letter, standard | 700 | 1,962 | **2,662** | 1 / 3 / 8 / 13 | 0.34 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | Letter, notes single-spaced | 740 | 2,201 | **2,941** | 1 / 3 / 8 / 13 | 0.33 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | Letter, no paper title on page 2 | 708 | 2,198 | **2,906** | 1 / 3 / 8 / 13 | 0.32 MB, 0 links, ok=True |
| Table 1, Figure 1, Table 2 | A4, standard | 744 | 2,313 | **3,057** | 1 / 3 / 8 / 13 | 0.33 MB, 0 links, ok=True |

- **Two exhibits beyond the holdings table (Table 1, Figure 1, Table 2): 2,898 words, about 2,800-2,850 in real
  text.** The claim's 2,700-2,900 holds. Section 2 takes 700, Section 3 2,198.
- **With the monitoring table as a fourth exhibit: 2,662**, under the claim's range. Section 3 drops to 1,962, below
  SKELETON v2's "about 2,000"; the table costs 236 words of prose.
- **Section 2 has no slack.** 700 words is the most that three pages hold with Table 1, the paper title and five
  headings; one more line spills onto a fourth page and breaks Wharton's limit. In real text that is about 680.
  Budget 650.
- **"9-12 pages" is a range of totals, not of the 2,700-2,900.** At Wharton's minimum (nine pages: Section 2 two
  pages, Section 3 six) the same plan holds about 1,900 words (estimate: three pages fewer at about 330 words; not
  measured). The figures in the claim describe the twelve-page maximum.
- **Small levers, measured:** single-spaced exhibit notes add about 40 (measured 2,941 against 2,898) words (Wharton allows single-spaced tables
  and graphics, but APA double-spaces notes; not worth breaking APA for); dropping the paper title on page 2 adds
  about 10 (2,906); A4 paper holds 3,057 with three exhibits (159, or 5.5%, more than Letter), so a draft written on
  A4 runs over when exported to Letter.
- **Word length is the biggest lever.** At Caplet's IPS's 4.66 characters a word the same pages hold about 7% more
  (about 3,100 with three exhibits); at the case study's 5.81, about 11% fewer (about 2,580). On 27 Nov `pour`
  measures the real text; the budget is a plan, the audit is the test.
- **PDF size:** 0.33 MB with Figure 1 at 300 dpi, no link annotations: far under 5 MB.

**Claim 2. "Two exhibits beyond the holdings table answer two case questions at a glance." Verdict: KEEP, with the
third exhibit changed and APA labels.**
- **Figure 1 (the reserve running down, NUMBERS 8h)** answers the case's question on how the reserve's composition
  "should change ... as the annual payments approach and are made". Keel's first look passes it: one holding per
  payment, funds giving way to bonds in 2037, the two long waits labelled. It costs 16.0 lines (about 230 words).
- **The third exhibit is Table 2, the plan under four markets (NUMBERS 4, placeholders)**, as SKELETON v2 now says.
  The range chart failed the five-second test (row 31). Table 2 cannot be tested until card Q24 fills its cells; only
  the central row has register numbers, and its top is under review.
- **Not exhibits:** the all-Treasury comparison (NUMBERS 4 C8, four numbers) is a sentence; the monitoring table is
  a fourth exhibit only if Caplet takes the 236-word cost.
- **APA numbers tables and figures separately,** so the report says Table 1, Figure 1 and Table 2; the word
  "Exhibit" stays in Keel's notes.
- **Table 1 passes on the first look** (13 rows on one line each, total $300,000.00 and 100.00%), but only because
  of Wharton's single-spacing allowance: double-spaced it spans two pages.

## (d) Gaps

- **Google Docs and Word may lay out differently from LibreOffice.** The measurements use LibreOffice with Liberation
  Serif (same widths as Times New Roman) and reproduce Word's 27.6-pt double-spacing pitch exactly; Google Docs'
  "Double" has not been measured. On 27 Nov, open `template_test.docx` in the program Caplet will export from and run
  `build_template.py audit` on its PDF before pouring text.
- **The bond identifiers** ("[WInS ID]") wait for Caplet's final WInS export (ASK_HUMANS, 9 Nov); the identifier in Wharton's own example table, 532281, is only probably the May-2038 bond's.
- **Exhibit 3's data** wait for cards Q19 and Q24; every cell but the central row is a placeholder, and the central
  row's top is under review in NUMBERS 4.
- **NUMBERS 8h should print the per-rung "above $50,000" column** used in Figure 1 (now read from the engine file
  8h names; it matches the 8h table to within $1).
- **No fresh-reader five-second test yet**; Keel's look is not a test. Due Mon 23 Nov (`TOOLS.md`).
- **Wharton's view of URLs in References** (row 28) is unverified.
