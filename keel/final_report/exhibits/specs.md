# Exhibit specs for the Final Report (rebuilt Thu 12 Nov 2026, Sydney, on the register of Tue 10 Nov; Table 1 again Thu 12 Nov evening)

Design notes, not report text. Titles below are working labels and each note is a list of the items it must carry;
both are written on 27 Nov. Design: H_plain ("sufficient without reinvestment", with the fee cushion), the Treasury
curve of 6 Nov 2026, the range rule on the fund's holdings, Keel's reading of "most". MODEL = Keel's calculation.

**What changed Thu 12 Nov evening, and why** (lead's brief; SKELETON's density cut, row 2.5, and Exhibits item 1; panel 2's
faculty and finalist judges, `../research/panel/2026-11-12_judge_faculty.md` and `..._judge_finalist.md`).
- **Table 1 has a seventh column, "Units bought / target"** (after the asset type): "4,503 / 4,503" and so on for the
  ten Treasuries, all at exactly their targets; VT "167 / 164" with "bought last, / from cash left" under it. Why:
  SKELETON's density cut makes 2.5's targets set before trading one column of Table 1, not a second table, so Section
  2's three pages hold (the faculty judge: 2.5's table was not counted). Every figure is NUMBERS 8m's, checked in
  `exhibit_data.py` against 8m's text, the Portfolio tab's target units (`portfolio.csv`, 8m's source), the 23 Oct
  snapshot's quantities and, for each holding, units x price paid = 8g's amount to the cent. Wharton's five columns
  and "Pays for" stay. The column is paid for by the name column (3.17 -> 2.13 in), so the five iBond fund names and
  VT's take two lines.
- **The costs row is set apart.** It now sits below a new "All holdings" subtotal ($298,690.58, 99.56%: the twelve
  holdings, cash included) and above the total, with no ticker, type or units, its label across the first four
  columns: "Costs at purchase, not a holding: fees and accrued interest". Why: the faculty judge ("the fees and
  accrued-interest row must not look like a holding") and the finalist ("the extra row for money that left at purchase
  is not in Wharton's example; I would look twice"). The total stays $300,000.00 and 100.00%.
- **Table 1 costs 20.9 lines with a 75-word note** (15.9 without; Wed: 16.9 and 12.9). **Section 2 measured against
  Wharton's three pages for the first time with the table as built:** at most 626 words of prose beside it, so 46 words
  of headroom over the density cut's 580 (about 27 in real text). See Page cost.

**What changed Thu 12 Nov, and why** (lead's brief; SKELETON Exhibits items 2 and 4; Panel 2's density cut).
- **Table 3 built** (Exhibit 4 below): seven rows in three levels, five columns, one trigger per cell, the two reasons
  to change the plan defined in their own rows. Why: SKELETON item 4 and the bond reader's condition for signing off
  ("I wouldn't approve a policy whose only two exits are undefined").
- **Figure 1 fixed.** The right-hand head now asks the question its two columns answer ("If interest earns nothing,
  what pays each $50,000?"); the axis break is gone (one scale, 2027 to 2042); `../WORDS.md` names throughout ("At
  today's market rates", "Its own Treasury", "What the top-up pays": renamed by the lead the same morning, since the column totals what the top-up's Treasuries pay, $55,920, while `WORDS.md` and the prose give its cost, $38,282); the note carries the ratio with its reason and the
  historical rate stretches. Why: the lay reader (`../research/panel/2026-11-11_lay_reader_3a_3b_figure1.md`), card
  Q31 and the density cut, which moved the ratio out of 2.0 and 3a into this note.
- **The letter build holds four exhibits** and the check now reads Figure 1's and Table 3's words as well as figures.

**Files.**
- `exhibit_data.py` reads every modelled figure from `../numbers/results_reserve_2026-11-10.json`,
  `results_joint_stress_2026-11-10.json`, `results_returns_2026-11-10.json`, and (Thu 12 Nov, for Table 3)
  `results_2026-11-10.json` (the top-up and the yield-fall distances, block C6) and `inflation_inputs.json` (the
  exchange rate and the construction cost band). Table 1's rows are the WInS record
  (8g), which no results file holds, so they are typed in and checked cell by cell against the 8g table; its units
  (Thu 12 Nov evening) are typed in from 8m and checked against 8m, `caplet/google_drive/sheets/
  portfolio_and_trading_notes/portfolio.csv` (the Portfolio tab 8m cites) and the 23 Oct snapshot.
  Run it to print every exhibit figure and the check against `../NUMBERS.md`.
  - Thu 12 Nov evening, with Table 1's units column and costs row: **333 figures; 327 PASS, 0 FAIL, 6 flagged** (the
    same six: five identifier placeholders; Figure 1's rows foot $1 off 8h's totals, which its note's rounding clause
    covers). Thu 12 Nov morning: 269; 263 PASS. Wed 11 Nov: 235; 229 PASS.
  - New checks (Thu 12 Nov evening, 64): each Treasury's target units against 8m's criterion row and bought = target
    against 8m's "All ten held at exactly the target units"; VT's 167 and 164 against 8m; VT's cell words against 8m
    ("from the cash then left", "filled last"); every target against the Portfolio tab's "Type into WInS" column and VT's
    order (11 of 11); units held against the 23 Oct snapshot; units x price paid = 8g's amount, holding by holding; the
    "All holdings" subtotal three ways (the eleven at cost, $295,176.79, plus WInS cash; $300,000 less the costs row;
    8g's groups); the costs row below that subtotal and above the total, with no ticker, type or units, and its label
    saying "costs" and "not a holding".
  - New checks (Thu 12 Nov): Figure 1's top-up head against NUMBERS section 2 and `WORDS.md`; its $1.11 against 8h's
    111.4%; Table 3's every dollar figure, date and number against NUMBERS 2, 5, 8d, 8h and 8j, its two definitions
    and trade days against SKELETON item 4, the trade days and the Feb-2037 bond's date against the calendar; no
    banned word ("backstop", "gift", "overflow", "paths") in any printed cell, head or legend.
  - The check also reads the waiting times from the Trading Notes (TNA and the WInS trade-note file), Table 1's
    "Pays for" from the 23 Oct WInS snapshot, and the cost of the Treasuries bought with the 2028 deposit from
    NUMBERS section 2.
- `build_exhibits.py` stops if any figure fails, then writes:
  - `figure1_reserve.svg` (text kept as text) and `figure1_reserve_2x.png`;
  - `exhibit2_reserve.png`: Figure 1 at 300 dpi, under the old name `../template/build_template.py` places.
    Checked Thu 12 Nov and kept, not deleted: `build_exhibits.py` writes it and `../template/build_template.py`
    (line 414) reads it;
  - `table1_holdings_2x.png`, `table2_markets_2x.png` and `table3_monitoring_2x.png`, cropped from
    `exhibits_letter.pdf` and `.docx` (the four exhibits on Letter in Wharton's format, each note showing its items;
    the bracketed items are what each note must carry, longer than the budget the measure uses);
  - `tables.md`: every exhibit as text;
  - `measurements.json`: the page cost of each exhibit and (Thu 12 Nov evening) `s2_fit`, Section 2 against
    Wharton's three pages (see Page cost).
  - The Table 1 preview stops under its note: since Thu 12 Nov evening the note-items placeholder (about 110 words,
    longer than the 75-word budget) pushes the line after the table onto the next page of the letter build.
- Rerun from the repo root: `python3 -I keel/final_report/exhibits/build_exhibits.py` (about 30 seconds since Thu 12
  Nov evening: Section 2's fit takes about 18 LibreOffice conversions; needs matplotlib, python-docx, pdfplumber and
  LibreOffice).
- Research behind the design:
  - `../research/cards/Q28_exhibits_prior_art.md` section (c), the design brief;
  - `../research/cards/Q23_exhibits_and_format.md`, Wharton's format and the measuring method.

## 0. Rules for every exhibit

- **APA 7 labels.** Keel's Exhibit 1, 2, 3, 4 are **Table 1**, **Figure 1**, **Table 2**, **Table 3**, numbered in the
  order the text calls them out.
- **Layout (APA 7; Wharton allows single spacing in tables and graphics).**
  - Number in bold; title in italic title case on the next double-spaced line.
  - Body single-spaced, 12 pt. Number, title and note double-spaced. "*Note.*" in italics.
  - Rules only at the top, under the heads, above a subtotal, spanner or total, and at the bottom; never vertical.
  - Each exhibit at the top or bottom of a page after its first call-out, with one blank double-spaced line after it.
- **Font.** Times New Roman, including inside the figure: at least 10 pt at printed size; figure numbers 10.5 pt.
  Built with Liberation Serif, which has the same character widths (card Q23 row 24).
- **Black and white.** Black plus two greys; no colour carries meaning.
- **Five-second test** (Perfetti, 2007). Each spec names the one question a first reader should answer. A fresh
  first-round reader read all three on Wed 11 Nov (`../research/panel/2026-11-11_fresh_reader_exhibits.md`); the
  fixes are in each spec. The next fresh-reader test is Mon 23 Nov.
- **Scale in every title** (fresh reader, Wed 11 Nov). Table 1 is the WInS book on the original $300,000 (8g: Laura's
  whole plan in miniature). Figure 1 and Table 2 are her plan for both deposits ($450,000), modelled.
- **Page cost, measured Thu 12 Nov.**
  - Method (card Q23): an exhibit between two prose lines on a Letter page in Wharton's format. Height = the gap /
    27.6 pt, less one line. It includes the number, title, note and the blank line after. An exhibit too tall for
    that (Table 3) is measured from the top of its own page.
  - A note is double-spaced like prose, so its words cost about what the same words cost in prose (about 14 a line).
  - The fixed cost below is each exhibit without its note:

| Exhibit | Section | Without a note | With the note budget | Prose it displaces (budget note) | Wed 11 Nov |
|---|---|---|---|---|---|
| Table 1 | Section 2 | 15.9 lines (units column, "All holdings" row) | 20.9 lines (75-word note) | about 300 words | 12.9 / 16.9 (50 words) |
| Figure 1 | 3a | 13.3 lines (image 6.5 x 3.56 in; two-line title) | 17.3 lines (60-word note) | about 250 words | 12.9 / 16.9 (55 words) |
| Table 2 | 3b, 3c | 9.2 lines | 12.2 lines (45-word note) | about 170 words | the same |
| Table 3 | 3e | 18.9 lines (30 single-spaced body lines) | 21.9 lines (35-word note) | about 310 words | Q23's filler measure 17.1 |
| Section 3's three exhibits | | 41.4 lines | 51.4 lines (2.2 pages) | about 730 words | Q23's 44.2 (16.0 + 11.1 + 17.1) |

  - Where the lines went since Wed 11 Nov. Figure 1: +0.4 fixed (the question head takes two lines more) and five
    more note words for the ratio. Table 3: real cells, not Q23's filler: +4.8 lines on Q23's 17.1 (two-line heads,
    three level rows, four- and five-line cells in the trigger and changes columns, a 1-pt gap after each row, which
    costs about 0.3 line in all).
  - **RISK: Section 3 no longer fits its budget.** Q23 row 33's ceiling of about 1,960 words beside the three
    exhibits assumed 44.2 lines; they now cost 51.4, about 100 words more, so the ceiling falls to about 1,860, about
    40 words under SKELETON's 1,900 budget. Ways back, each about one line (14 words): Table 3's note to about 20
    words (today's market rates; the reader); Figure 1's note to 45 words (move the historical rate stretches to 3a's
    prose); Table 3 without the row gaps (0.3). Or 3e gives 40 words. The lead's call; nothing is cut here.
  - **Section 2, measured Thu 12 Nov evening (`measurements.json` `s2_fit`).** Card Q23 row 33's fit (`fit_mock`):
    title page; on page 2 the paper title, the Level 1 heading, the lead and 2.1 under one Level 2 heading; Table 1
    with a 75-word filler note at the top of page 3; 2.2, 2.3 and 2.5 under three Level 2 headings; Section 3 on a new
    page. Each prose block is filled until one more word pushes Table 1 off page 3 or Section 3 off page 5.
    - **Ceiling 626 words** (299 before Table 1, 327 after) against the density cut's **580: 46 words of headroom**
      (3.2 lines), **about 27 in real text** (Q23: real paragraphs run 2-3% under a filler ceiling). Section 2 ends on
      page 4: three pages, Wharton's maximum.
    - The same fit on Wed 11 Nov's Table 1 (six columns, 50-word note, 16.9 lines): 661. On tonight's table with a
      50-word note: 654 (run once, not in the build). So the units column, the "All holdings" row and VT's third line
      cost about 7 words of prose at the page breaks, and the 25 extra note words about 28: the ceiling moves in whole
      lines at page breaks, not smoothly.
    - What moves it: each 14 words of note or one more Level 2 heading costs about one line (14 words). The note's
      75 words is a budget for its five items; at 50 the headroom is about 74 (54 in real text).
    - Superseded: "about 670 words of ceiling beside Table 1" (Wed 11 Nov, an estimate from Q23's 700 less the table's
      growth, not a fit).
  - Items cut from the notes go to prose: the inflation row's $89,546 in 2027 dollars (3b or 3c), the range rule (3c),
    the replay method and VT's purchase month (3e).

## Exhibit 1 = Table 1, the holdings (Section 2; Wharton requires it)

| Item | Spec |
|---|---|
| Case question | Wharton, Section 2: a table of every holding in the final WInS portfolio with "ticker or identifier, name, asset type, amount allocated, and percentage of the portfolio", "expressed using the original $300,000 investment"; "The total must equal $300,000 and 100%." |
| Five-second question | "What did the $300,000 buy, which payment does each holding stand for, and was it bought as planned?" (ten Treasury holdings, 89.55%, one per payment year, IBTM also the floor, each at exactly its target units; one world stock fund for the range's top and the flexibility, bought last from the cash left; a little cash; and, set apart, the costs at purchase, which are not a holding) |
| Data | NUMBERS 8g version 2, the WInS record at cost, and 8m, the targets set before trading; not a model. 13 rows of 8g: twelve holdings (cash included, as in Wharton's example) and the costs row. Amounts in cents as WInS records them; percentages to two decimals by largest remainder, as 8g. Subtotal under the ten Treasuries: $268,652.18, 89.55% (8g "In groups"). VT $26,524.61 (8.84%); cash $3,513.79 (1.17%) = the cash WInS shows. **All holdings (Thu 12 Nov evening): $298,690.58, 99.56%** = the eleven at cost ($295,176.79, 8g) plus WInS cash = $300,000 less the costs row = 8g's groups (89.55 + 8.84 + 1.17). Costs row $1,309.42 (0.44%) = $200 of commissions + $1,109.42 of bond interest accrued at purchase. Total $300,000.00, 100.00%. **Units (8m; Thu 12 Nov evening):** IBTM 4,503 / 4,503; IBTO 1,024 / 1,024; IBTP 927 / 927; IBTQ 894 / 894; IBTR 853 / 853; the five bonds 20 / 20, 20 / 20, 18 / 18, 18 / 18 and 20 / 20 units of $1,000 face; VT 167 / 164 (164 at 2 Oct prices; its target was the cash then left; order 11 of 11, filled 7 Oct, 8:27 PM ET). Each holding's units x price paid (23 Oct snapshot) equals its 8g amount to the cent. |
| Form (Thu 12 Nov evening) | Seven columns: Wharton's five, with "Units bought / target" after the asset type, and "Pays for" last. Rows in payment order (IBTM for 2033 down to the 3.125% Nov 2041 bond for 2042); then the Treasury subtotal (thin rule above, 6-pt gap after); VT; cash; **"All holdings"** (thin rule above); **the costs row**; the bold Total under a rule. The two subtotals and the costs row print their labels across the first four columns (4.31 in), with no ticker, type or units: the Treasury subtotal indented to the names (it is a group inside the holdings), "All holdings" and the costs row flush left like "Total" (they reconcile the holdings to the $300,000). Widths 0.67 / 2.13 / 0.46 / 1.05 / 0.85 / 0.55 / 0.79 in, no padding at the table's outer edges. Units centred: bought and target have the same digits in every row and Times digits are all one width, so the slashes line up. Two lines: the five iBond fund names ("iShares iBonds Dec 2032 / Term Treasury ETF"), VT's name and the two designed Pays-for cells; three: VT's units cell. Card Q28 still holds: no grouping by role (IBTM does two jobs); "All holdings" is not a role group but the line the costs row hangs from. |
| Units bought / target (Thu 12 Nov evening; SKELETON density cut, 2.5) | The head reads "Units bought / target" (two lines). The targets are the Portfolio tab's units, set before the first fill (portfolio.csv l.20-31, priced on 2 Oct closes and 5 Oct bond checks; 8m). All ten Treasuries print equal pairs, so the eye reads "met" down the column; VT's unequal pair carries its reason in the cell, "bought last, / from cash left" (the brief's "bought last from the cash left"; "from the cash left" needs 1.17 in and the column holds 0.97). A bond's units are $1,000 of face value (the note). Not printed: the other two targets (bonds within 25 basis points; cash never below $1,000), which go to the note, as the density cut says. |
| Pays for (fresh reader and coordinator, Wed 11 Nov) | The payment year each holding stands for, from the 23 Oct WInS snapshot's "Pays for" column (8g cites it): 2034 to 2042 for IBTO to the Nov-2041 bond. IBTM: "2033 and / the floor" (snapshot: "2033 payment + floor stand-in"). VT: "Range top, / flexibility" (the snapshot says "growth sleeve"; IPS l.15 gives the two jobs; "flexibility" is the IPS's word for the half promised to no one and Table 2's head, chosen over "half kept", which a stranger cannot read). Cash, costs, subtotal and total: blank. Centred. Those two cells cannot fit one line at 12 pt: the column has 0.75 in of text room and "2033 and the floor" needs 1.2 in. |
| Wording choices (each forced by width at 12 pt) | Asset types are one word, Wharton's own: "ETF" (8g's "ETF (Treasury)" and "ETF (equity)"; each name already says Treasury or Stock) and "Bond" (Wharton's example says "Treasury Bond"; each name says T-Bond). The dollar sign moved into the head, "Amount ($)". The % head is "% of total": "portfolio" needs 0.58 in. The Treasury subtotal is named "Treasuries for the ten payments and the floor"; never "the payments" alone, which would contradict the Trading Note on IBTM (card Q28 row 33). "All holdings", not "Holdings": the twelve rows above it, cash included. |
| Costs row (Thu 12 Nov evening; panel 2) | Printed "Costs at purchase, not a holding: fees and accrued interest" (3.86 in, across the first four columns, which hold 4.27 in), below "All holdings" and above the total, with no ticker, type or units. Why: the faculty judge ("must not look like a holding") and the finalist ("not in Wharton's example; I would look twice"). It says what it is and that it is not a holding, and it reconciles the holdings ($298,690.58) to Wharton's $300,000. "Fees", as SKELETON 2.5 and 8m say it, for WInS's $200 of commissions. Same money as 8g's "Commissions and bond interest paid at purchase"; amount and percentage exactly 8g's ($1,309.42, 0.44%); the check keeps 8g's name and confirms both. Wed 11 Nov's label ("Commissions and accrued interest at purchase", in the name column with "N/A" and "Cost") read as a holding. Still open (fresh reader): accrued interest is not spent; the note says it comes back with each bond's next coupon. |
| Identifiers | ETFs by ticker. The bonds are placeholders in square brackets: "[532281]" for the May-2038 bond (Wharton's own example row, still to confirm) and "[ID]" for the other four. They are filled from Caplet's final WInS export before 27 Nov (8g "Identifiers"). |
| Number and working title | **Table 1** / *The Final WInS Portfolio at Cost on the Original $300,000: Laura's Whole Plan in Miniature* (one line; 8g's own words for what the book is, which answers the reader's "how do rungs this size become $50,000 each?") |
| Note must carry (about 75 words; was 50) | Amounts at cost: units held x price paid on 6-7 Oct 2026 (U.S. Eastern), on the original $300,000 (8g). Units bought / target: the targets were set before the first trade (Portfolio tab, 2 Oct prices); a bond unit is $1,000 of face value (8m). The other two targets, met: every bond bought within 25 basis points of the Treasury curve; cash never below $1,000 (8m; SKELETON's density cut sends both here from 2.5). Pays for: the payment (1 January of that year) each holding stands for; the floor: the least Laura can promise co-sponsors in 2031, which IBTM stands in for (TNA l.13, CANON A24, 8g). The costs row: the $200 of fees and $1,109.42 of bond interest accrued at purchase, which comes back with each bond's next coupon (8g v2). Cut Thu 12 Nov evening: "the full-size plan for both deposits is Figure 1 and Table 2" (the title carries the scale; 2.0 and 2.1 name the plan; kept in the store). |
| Measured | **20.9 lines with a 75-word note; 15.9 without** (Thu 12 Nov evening). The column, the "All holdings" row and VT's third line add 3.0 lines; the 25 more note words 2.0. Wed 11 Nov: 16.9 and 12.9. Before the "Pays for" column: 14.9 and 11.9. Mon 9 Nov's version: 14.1 lines with a shorter note and no subtotal. Section 2 beside it: at most 626 words in three pages, 46 over the 580 budget (see Page cost). |
| Five-second result | Keel's look, Thu 12 Nov evening: the eye lands on IBTM's 32.50% and "2033 and the floor", then runs down two columns that say the same thing differently, the years and the equal pairs; VT's unequal pair explains itself in the cell; the costs row, flush left under "All holdings" with no ticker, reads as the reconciling line, not a holding. Not yet read by a fresh reader (due Mon 23 Nov). Fresh reader, Wed 11 Nov, before the Pays-for fix: 4 for clarity, 3 for wanting to read on. Risks left: the bracketed identifiers read as unfinished until Caplet's export fills them; the wrapped fund names make the top half look denser than the bond rows. |
| Files | `table1_holdings_2x.png`; Markdown in `tables.md`; built by `add_table1` in `build_exhibits.py`; units in `exhibit_data.UNITS`, rows in `exhibit_data.table1_rows`. |

## Exhibit 2 = Figure 1, the operating reserve running down (3a)

| Item | Spec |
|---|---|
| Case question | The case: "recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made". Wharton: "Recommend an appropriate operating reserve". |
| Five-second question | "Which Treasury pays each year's $50,000, when does its cash arrive, and what pays the gap if interest earns nothing?" (answer in the title: the top-up from the 2028 deposit) |
| Form (card Q28: the escrow sufficiency schedule beside a staircase; Thu 12 Nov fixes) | Ten rows, 2033 at the top. Left: the payment year. Middle: one bar per own Treasury, from January 2027 until its cash arrives, labelled on the bar with its ticker or coupon and date; light grey for the iBond Treasury funds, dark grey with white text for the Treasury bonds; a black tick at each 1 January payment. **One scale, 2027 to 2042, no break** (Thu 12 Nov, lead's brief): years 2027, 2030, 2033, 2036, 2039 and 2042 along the head, so the six years held before the first payment show at their true length. The two long waits keep the Trading Notes' months on a dotted line: "waits 10.5 months" (Feb-2037 bond) and "waits 7.5 months" (May-2038 bond; CANON A16, B35; the model's 7.6 is not printed); "cash" left the label so it clears the number columns, and the legend names the dotted line "cash waiting". Right: "At today's market rates" ($50,000 in every row), then, under a two-line head that **asks the question the columns answer**, "If interest earns nothing, what pays each $50,000?", two columns: "Its own Treasury" and "The top-up". A total row under a rule. Legend inside the figure, one line: iBond Treasury fund; Treasury bond; $50,000 paid on 1 January; cash waiting (the build stops if it does not fit). |
| Words (`../WORDS.md`, Thu 12 Nov) | "today's market rates", not "forward rates"; "Its own Treasury", not "Own holding"; "The top-up", not "Backstop" or "Bought with / 2028 deposit" (WORDS.md's name since Wed 11 Nov evening, which also says where it comes from in the title); "interest earns nothing". The check fails on any banned word in the figure's title, heads, legend or labels. |
| Data | NUMBERS 8h, MODEL; `results_reserve_2026-11-10.json`. Holdings and cash dates come from `composition_1jan2033_base`; "At today's market rates" from `base` ($50,000 in every row; the top-up is untouched). The two question columns come from `fee`, Keel's standard as SKELETON's Exhibits item 2 sets it: nothing earns interest from 2027 and every waiting dollar pays the Treasury-bill fund's 0.15% fee. Own Treasury $47,338 (2033) down to $42,180 (2041) and $42,469 (2042); the top-up $2,662 to $7,820; each row exactly $50,000; totals $500,000, $444,080 and $55,920. Nothing is left after 2042; without the fee, $1,414 is left (the `zero` block). |
| Number and working title | **Figure 1** / *Each Payment Has Its Own Treasury, and the Top-Up From the 2028 Deposit Pays Any Gap if Interest Earns Nothing (Laura's Plan for Both Deposits, $450,000, Modelled)* (two lines; the point first, then the scale) |
| Note must carry (about 60 words; was 55) | Modelled at today's market rates (Treasury par curve of 6 Nov 2026); Laura's plan for both deposits ($450,000); each payment in the dollars of its own 1 January. The two right-hand columns: if nothing earns interest from 2027 and waiting money pays the Treasury-bill fund's 0.15% fee, own Treasuries pay $444,080 and the top-up $55,920 of the $500,000. **The ratio with its reason** (density cut; card Q31; WORDS.md): about $1.11 for each $1 on 1 Jan 2033 at today's rates ($444,545 against $399,089, 8h's 111.4%), because the top-up is sized for no interest. The top-up: the first $38,282 of the 2028 deposit; $2,388 completes the ten and $35,894 pays the last column (NUMBERS 2); not in the WInS portfolio. Paid in every historical rate stretch tested (585 starting months, 1962-2010; NUMBERS 2; no longer "if room", the density cut puts it here). The rounding clause. Cut: Wed 11 Nov's $34,369 in 1 Jan 2027 money, replaced by the top-up's $38,282 in January 2028 money, as 2.0 and WORDS.md state it. Scale is stated twice, in the title and the note's first item. |
| Rounding (coordinator, Wed 11 Nov) | Every row equals 8h and sums to exactly $50,000. The totals are 8h's totals of unrounded figures ($500,000, $444,080, $55,920); the printed rows foot to $444,081 and $55,919, which the note's rounding clause covers. |
| Words never used | Waiting money is never called cash held at 0% or cash not invested (CANON A15). No fund bar carries a bare "$50,000": the funds pay net asset value (card Q28 row 13). |
| Measured | Image 6.5 x 3.56 in (was 3.40: the question head). 17.3 lines with a 60-word note; 13.3 without. Wed 11 Nov: 16.9 and 12.9. Tue 10 Nov: 16.0 lines, 3.85-in image. |
| Five-second result | Not re-tested since Thu 12 Nov's fixes; the fresh-reader test is Mon 23 Nov. Fresh reader, Wed 11 Nov: bars 5, right-hand columns 2 ("Backstop" undefined; "zero interest on what?"). Keel's look Thu 12 Nov: the head now says what the two columns answer, and the bars' 2027-2033 stretch shows money held six years before it pays. Still open: the reader would drop the constant "At today's market rates" column; kept, since it shows each own Treasury pays exactly $50,000 at today's rates (8h), and 3a's prose must say they were sized to do so. |
| Not drawn | Q28's optional lighter last stretch on each fund bar (cash inside the fund in its final months): a third grey breaks the two-greys rule, and the register gives no per-fund maturity months. |
| Files | `figure1_reserve.svg`, `figure1_reserve_2x.png`, `exhibit2_reserve.png` (300 dpi); its numbers as text in `tables.md`. |

## Exhibit 3 = Table 2, the plan under several markets (3b and 3c)

| Item | Spec |
|---|---|
| Case question | The case's "favorable and unfavorable market outcomes". Wharton: "Explain the level of confidence associated with that range and the factors that could affect it". Panel 1 asked for a scenario table and for the 2031 announcement under three markets; one table answers both. |
| Five-second question | "In a bad market, what still holds and what shrinks?" (The payments hold in every row. The stated range and the flexibility move.) |
| Why a table (card Q28) | Five named, conditional worlds against four outputs, which no fan chart can hold. Text also avoids the misreading that sank the range chart. Do not claim that fan charts fail: the Bank of England's 2026 test found the public reads them well. |
| Rows (order: base first; stresses by how far the range falls; the rates-up world last) | 1. Today's forward rates. 2. Replay from 2006: shares fall (VT bought June 2007). 3. Rates 3 points lower for good. 4. Replay from 2007: rates fall early (VT bought July 2008; "most" binds). 5. Inflation: rates 3 points higher. Then, under a rule, an italic spanner "All 585 history replays (1962-2010 starts)" with three indented rows: 1-in-20 low, median, 1-in-20 high. They are set apart so the promise range and the uncertainty never look alike (card Q28 rows 23, 25). |
| Columns (time order; the column that never changes first) | World; Ten payments; under a spanner "Stated in 2031": Bottom, Top; Flexibility (Jan 2033) = half of VT kept plus the excess over the stated top (card Q25, NUMBERS 8i "Half kept plus excess"). Widths 2.50 / 0.95 / 0.95 / 0.95 / 1.15 in. Cut, as Q28 says: funds pay, excess, left after 2042, completion. Cut on Wed 11 Nov (coordinator): the contribution column, which equals the stated top in every world and every window (8i, 8j; the check confirms all eight rows). |
| Result row (fresh reader and coordinator, Wed 11 Nov) | The confidence answer moved out of the note into the table: a last full-width row under a rule, "In every world and every replay, the facility contribution in January 2033 equals the stated top." Checked: all five worlds and 100% of the 585 replays (`twd_test.joint_replay`). |
| Data | NUMBERS 8i (MODEL); `results_joint_stress_2026-11-10.json`. The flexibility's spread comes from 8j's joint-replay column. All paid in every row. Stated ranges: $95,000-$115,000; $95,000-$105,000; $80,000-$95,000; $80,000-$95,000; $100,000-$120,000. The contribution (not printed) equals the stated top in every row and every window (8j). Flexibility $29,823; $19,476; $21,086; $21,910; $23,641. Spread: bottom $80,000 / $95,000 / $115,000; top $95,000 / $115,000 / $140,000; flexibility $19,690 / $31,809 / $49,629. |
| Rounding | Stated ends to the dollar (they are $5,000 steps by the rule). Flexibility to the nearest $100 ($29,800 and so on), as SKELETON's prose rounds it. Q28 said $1,000, but that would print $49,629 as $50,000 (the payment's size) and $29,823 as $30,000 (a round step that reads as a stated figure). |
| Number and working title | **Table 2** / *Laura's Plan for Both Deposits ($450,000) in Five Markets and 585 History Replays, Modelled* (one line; it also counts the eight rows the reader found under "Five Markets") |
| Note must carry (about 45 words; only what changes a cell) | MODEL, not forecasts; curve of 6 Nov 2026. Shares 7.5% a year in rows 1 and 3. Replays: U.S. yields and stocks from the start month (method in 3e). Inflation row: prices up 5% a year. Flexibility: the half of VT promised to no one plus whatever the funds pay above the stated top, to the nearest $100 (the reader asked "excess of what?"). Spread rows: each column's own percentile. To prose: the replay method and VT's purchase month (3e), the inflation row's $89,546 in 1 Jan 2027 dollars (3b or 3c), the range rule (3c), and why rates move the range more than shares do (the reader's own finding). |
| Measured | 12.2 lines with a 45-word note; 9.2 without. Before the fixes: 12.7 and 8.7. Two head lines thanks to the spanner (three with "Stated bottom (2031)" as a head). |
| Five-second result | Fresh reader, before the fix: 4 and 4; "All paid" read at once; the confidence answer was in the note. It now closes the table. Open for 3c's prose: what confidence Laura states in one number, and what she says before 2031 while the range still moves with rates. |
| Files | `table2_markets_2x.png`; Markdown in `tables.md`; built by `add_table2` in `build_exhibits.py`. |

## Exhibit 4 = Table 3, what to monitor as 2031 and 2033 approach (3e)

| Item | Spec |
|---|---|
| Case question | Wharton, Section 3: "Explain what Laura or her asset management team should monitor as 2031 and 2033 approach and how changing conditions could affect your recommendations." |
| Five-second question | "What would make Laura change the plan?" (two things, both defined in their rows: a missed 2028 deposit and a Treasury default; everything else changes a date, an instrument or her flexibility, never the plan) |
| Form (SKELETON item 4; cards Q15, Q26, Q30; bond reader, Wed 11 Nov) | Seven rows in three levels, each level an italic full-width row under a rule: "The two reasons to change the plan" (rows 1-2); "Look closer: a date or an instrument may change, never the plan" (rows 3-5); "Watch: the plan carries on" (rows 6-7). Five columns: Signal; Reader; Carry on while; Look closer or act when; What it changes; what it never changes. One trigger per cell; no source column. The last column opens each part with an italic "Changes:" and "Never:". Widths 0.85 / 0.60 / 1.50 / 1.65 / 1.90 in, all left-aligned, single-spaced, a 1-pt gap after each row (rows ran together without it). |
| Rows (as printed) | 1. The 2028 deposit ($150,000) / Laura / Confirmed in late 2027; the $38,282 top-up comes first / Nothing received by 31 March 2028 (a missed deposit) / Changes: the plan, before any range is stated. Never: the Treasuries held. 2. Treasury payments to her or her funds / Team / Paid by the next business day (Tue 17 Feb 2037 for the February 2037 bond) / A Treasury default: any marketable Treasury payment over five business days late / Changes: the payments and range, restated on what was received. Never: a forced sale. 3. The X-date of the debt limit / Team / No X-date within a month of a cash date / An X-date within a month of a payout, maturity or trade day / Changes: that money moves to bills due before it. Never: the payments. 4. iBond fund notices, the floor's too / Team / Cash arrives 10 to 14 days before 1 January / A notice that moves a fund's end date / Changes: the instrument, to a Treasury maturing in time. Never: the payment. 5. Trade days: Mon 4 Jan 2027, Mon 3 Jan 2028 / Team / Limit orders near each fund's net asset value / A date cannot be kept (a halt; a first draw after January 2033) / Changes: a date, by days. Never: the step or its order. 6. Treasury yields and share prices / Team / Any level: a fall in the market is not a reason / None. Yields 2 points lower before 2027: a $60,000 bottom; 3.60 lower: the top-up takes the whole deposit / Changes: prices, until each end is bought; then only her flexibility. Never: the payments. 7. Her flexibility's three uses / Laura / US$1 = NT$32.768; construction cost index up 1.5% to 5.0% a year / A Taiwan dollar 10% stronger ($11,500 more on $115,000) / Changes: a call on her flexibility ($29,800 today). Never: the range. |
| Sources (all checked) | Row 1: NUMBERS 2 (the top-up $38,282) and SKELETON item 4 (31 March 2028; confirmed in writing in late 2027). Row 2: SKELETON item 4's definition (five business days; S&P's test) and 8h (Tue 17 Feb 2037). Row 3: SKELETON item 4 (a month; payout, maturity, trade day; bills). Row 4: 8h (cash 10 to 14 days before 1 January; notice in mid-October). Row 5: SKELETON item 4 and the calendar (both 1 Januaries closed). Row 6: NUMBERS 5 and C6 (`fall_200bp`, stated bottom $60,000; 3.60 points takes the whole deposit). Row 7: 8d (US$1 = NT$32.768 on 6 Nov; construction cost band) and 8j (a 10% stronger Taiwan dollar: $11,500 more on the $115,000 top; her flexibility $29,823, printed $29,800 as in Table 2). |
| Number and working title | **Table 3** / *Seven Signals to Watch as 2031 and 2033 Approach; Two Can Change Laura's $450,000 Plan* (one line) |
| Note must carry (about 35 words; Thu 12 Nov evening: more spills the table onto a second page) | Today's market rates (curve of 6 Nov 2026); the top-up's two parts, in January 2028 dollars: $2,388 the ten Treasuries still lack plus $35,894 so each payment is met even if money already received earns nothing (never "so no payment needs interest", which is false: each payment needs its own bonds' coupons; bond reader) (NUMBERS 2, 5); (a deposit received after 31 March 2028 runs the same order, card Q34: said in 3e's prose, not here, for the page); the X-date is the Treasury's estimate, else the CBO's; "Team" is Wharton's "her asset management team". |
| Choices against SKELETON item 4 (each forced by width or source) | (a) Row 4's trigger is a notice that moves a fund's end date; SKELETON's "bridge if cash is not in by 28 Dec" has no source in NUMBERS (no 28 Dec date, no bridge instrument), so it is left to 3e's prose or a NUMBERS entry first. (b) Row 1 names the $38,282 and the note carries its two parts, since both parts in the cell made it seven lines. (c) "Reader" for "who reads it" (the head fits one line). (d) Row 5 drops the 2031 meetings and keeps the first draw slipping past January 2033 inside its trigger. (e) Row 7's test is the $11,500 against the $29,800 of flexibility, not 8j's tail probability (the density cut keeps tail probabilities out). (f) Row 6 shows NUMBERS 5's distances, not spreads, as SKELETON asks; its trigger cell opens "None." because no market level is a reason. (g) Custody is not a row (SKELETON item 4 (c): one line of prose). |
| Measured | 21.9 lines with a 35-word note (8.39 in of the 9-in text block); 18.9 without. It fits one page only at the top of its own page. Q23's filler estimate was 17.1. |
| Five-second result | Not yet tested. Keel's look: the three italic level rows and the "Changes:/Never:" pairs carry the point before any cell is read; the two reasons sit first. Due Mon 23 Nov with the others. |
| Files | `table3_monitoring_2x.png`; Markdown in `tables.md`; built by `add_table3` in `build_exhibits.py`; rows in `exhibit_data.TABLE3_ROWS`. |

## Decisions taken (coordinator, Wed 11 Nov; lead, Thu 12 Nov) and what is still open

1. Taken: Table 1's costs row is printed "Commissions and accrued interest at purchase" (one line).
2. Taken: Figure 1's rows equal 8h; its note carries the standard rounding clause.
3. Taken: Table 2 has no contribution column. Superseded the same day by decision 6: the claim is a table row.
   The two Section 3 notes were held to about 100 words together (55 + 45); Thu 12 Nov: 60 + 45, and Table 3's 35.
4. Taken (fresh reader, coordinator): every title says its scale; Table 1 is the WInS book on the original
   $300,000 (Laura's whole plan in miniature), Figure 1 and Table 2 her plan for both deposits ($450,000), modelled.
   Figure 1's note says its right-hand columns are the $500,000 of payments split, not the reserve's value.
5. Taken: Figure 1 has a title sentence with its point; "Backstop" is "Bought with / 2028 deposit" (since Thu 12 Nov
   "The top-up", decision 8). Table 1 has a
   "Pays for" column (two cells on two lines; +2.0 lines with the note; Section 2 still within budget).
6. Taken: Table 2's last row says the contribution equals the stated top in every world and replay.
7. Open: `../template/build_template.py` belongs to another owner. Its own `add_figure1_reserve` and
   `add_table2_markets` still carry Tue 10 Nov's note text, and its Table 1 has no subtotal. It still runs on the new
   `exhibit_data.py` (compatibility names kept and checked again after these fixes, including its own measuring
   variant with "Pays for"; `SCENARIO_COLUMNS` has five columns without the contribution). Its titles and notes
   predate the scale fix. On 27 Nov, pour with `build_exhibits.py`'s `add_table1`, `add_figure1` and `add_table2`, or update
   the template.
8. Taken Thu 12 Nov (lead's brief): Table 3 is built and checked; Figure 1 has no axis break, a question head, WORDS.md
   names and the ratio in its note. `exhibit2_reserve.png` stays (two builds use it).
9. Open Thu 12 Nov: Section 3's three exhibits cost about 100 words more than Q23 assumed (see Page cost); row 4's
   bridge needs a NUMBERS entry before it can be printed.
10. Taken Thu 12 Nov evening (lead's brief): Table 1 gains "Units bought / target" (NUMBERS 8m, checked) and the costs
   row is set apart below an "All holdings" subtotal, labelled "Costs at purchase, not a holding: fees and accrued
   interest"; the total stays $300,000.00 and 100.00%. Note budget 75 words (two of 2.5's targets moved in, the
   full-size-plan pointer out). Section 2 measured: 626-word ceiling, 46 words of headroom over 580 (about 27 in real
   text).
11. Open Thu 12 Nov evening, for the lead (files the exhibits owner does not edit): SKELETON's Exhibits item 1 still
   says "one subtotal row" (there are now two subtotals and the set-apart costs row) and its Section 2 head still says
   "about 650 words and Table 1" (the density cut's 580 fits; the ceiling is 626); 8g's table keeps the costs row's
   name and its "Cost" type (the exhibit prints its own label, checked against 8g's amounts). The template's own
   Table 1 (`../template/build_template.py`, `add_table1_holdings`) has neither the units column nor the "All holdings"
   row: on 27 Nov pour with `build_exhibits.add_table1` (decision 7).

## Former candidates, for the record

1. **The range forming under three markets (chart).** Failed the five-second test on Tue 10 Nov: bands were read as
   outcomes. Superseded by Table 2. The chart file is deleted. On today's register the house-model figures are: floor
   payout $88,047 / $103,097 / $124,380; stated bottom $85,000 / $95,000 / $115,000; stated top $95,000 / $115,000 /
   $140,000 (NUMBERS section 4).
2. **The monitoring table (Table 3, 3e).** Built Thu 12 Nov as the fourth exhibit (Exhibit 4 above); Q23's filler
   measure of 17.1 lines is superseded by 21.9.
3. **The contribution against an all-Treasury plan.** One sentence in 3b, no exhibit. An all-Treasury plan gives
   $140,761 at forward rates (stated $130,000). The FINAL's funds pay $123,476, and the stated top is $115,000.
   Counting the half kept and the excess, the FINAL's house-model median is $145,687 against $140,649, and its
   1-in-20 low $113,449 against $113,169 (NUMBERS section 4, C8).
