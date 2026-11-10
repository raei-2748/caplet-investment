# Exhibit specs for the Final Report (rebuilt Wed 11 Nov 2026, Sydney, on the register of Tue 10 Nov)

Design notes, not report text. Titles below are working labels and each note is a list of the items it must carry;
both are written on 27 Nov. Design: H_plain ("sufficient without reinvestment", with the fee cushion), the Treasury
curve of 6 Nov 2026, the range rule on the fund's holdings, Keel's reading of "most". MODEL = Keel's calculation.

**Files.**
- `exhibit_data.py` reads every modelled figure from `../numbers/results_reserve_2026-11-10.json`,
  `results_joint_stress_2026-11-10.json` and `results_returns_2026-11-10.json`. Table 1's rows are the WInS record
  (8g), which no results file holds, so they are typed in and checked cell by cell against the 8g table.
  Run it to print every exhibit figure and the check against `../NUMBERS.md`.
  - Wed 11 Nov, after the fresh reader's fixes: 235 figures; 229 PASS, 0 FAIL, 6 flagged (five identifier
    placeholders; Figure 1's rows foot $1 off 8h's totals, which its note's rounding clause covers).
  - The check also reads the waiting times from the Trading Notes (TNA and the WInS trade-note file), Table 1's
    "Pays for" from the 23 Oct WInS snapshot, and the cost of the Treasuries bought with the 2028 deposit from
    NUMBERS section 2.
- `build_exhibits.py` stops if any figure fails, then writes:
  - `figure1_reserve.svg` (text kept as text) and `figure1_reserve_2x.png`;
  - `exhibit2_reserve.png`: Figure 1 at 300 dpi, under the old name `../template/build_template.py` places;
  - `table1_holdings_2x.png` and `table2_markets_2x.png`, cropped from `exhibits_letter.pdf` (the three exhibits on
    Letter in Wharton's format, each note showing its items);
  - `tables.md`: every exhibit as text;
  - `measurements.json`: the page cost of each exhibit.
- Rerun from the repo root: `python3 -I keel/final_report/exhibits/build_exhibits.py` (about 15 seconds; needs
  matplotlib, python-docx, pdfplumber and LibreOffice).
- Research behind the design:
  - `../research/cards/Q28_exhibits_prior_art.md` section (c), the design brief;
  - `../research/cards/Q23_exhibits_and_format.md`, Wharton's format and the measuring method.

## 0. Rules for every exhibit

- **APA 7 labels.** Keel's Exhibit 1, 2, 3 are **Table 1**, **Figure 1**, **Table 2**, numbered in the order the text
  calls them out. A monitoring table in 3e would be Table 3.
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
- **Page cost, measured Wed 11 Nov.**
  - Method (card Q23): an exhibit between two prose lines on a Letter page in Wharton's format. Height = the gap /
    27.6 pt, less one line. It includes the number, title, note and the blank line after.
  - A note is double-spaced like prose, so its words cost about what the same words cost in prose (about 14 a line).
  - The fixed cost below is each exhibit without its note:

| Exhibit | Section | Without a note | With the note budget | Prose it displaces (budget note) | Before the fresh reader's fixes |
|---|---|---|---|---|---|
| Table 1 | Section 2 | 12.9 lines | 16.9 lines (50-word note) | about 240 words | 11.9 / 14.9 (45 words) |
| Figure 1 | 3a | 12.9 lines (image 6.5 x 3.40 in; two-line title) | 16.9 lines (55-word note) | about 240 words | 11.9 / 14.9 (45 words) |
| Table 2 | 3b, 3c | 9.2 lines | 12.2 lines (45-word note) | about 170 words | 8.7 / 12.7 (55 words) |
| Section 3's two exhibits | | 22.1 lines | 29.1 lines (1.2 pages) | about 410 words | 20.6 / 27.6 |

  - Where the lines went. Table 1: +1.0 fixed (two "Pays for" cells on two lines) and +1.0 from five more note words.
    Figure 1: +1.0 fixed (the title is now a sentence with the scale, two lines) and +1.0 from ten more note words.
    Table 2: +0.5 fixed (the result row) and -1.0 from ten fewer note words.
  - Does each still fit? Section 2: two lines are about 30 words, so SKELETON's ceiling of about 700 words beside
    Table 1 falls to about 670, still above its 650-word budget. Section 3: against SKELETON v2's 27.1 lines (Q23's
    Tue 10 Nov measures, 16.0 + 11.1), the two exhibits now cost 29.1 lines with their notes held to 100 words
    together (55 + 45): two lines (about 30 words) over, so the ceiling of about 1,960 words falls to about 1,930, still
    above the 1,900 budget. Cutting Figure 1's optional note item (the $34,369 cost) wins back one line.
  - Items cut from the notes go to prose: the inflation row's $89,546 in 2027 dollars (3b or 3c), the range rule (3c),
    the replay method and VT's purchase month (3e).

## Exhibit 1 = Table 1, the holdings (Section 2; Wharton requires it)

| Item | Spec |
|---|---|
| Case question | Wharton, Section 2: a table of every holding in the final WInS portfolio with "ticker or identifier, name, asset type, amount allocated, and percentage of the portfolio", "expressed using the original $300,000 investment"; "The total must equal $300,000 and 100%." |
| Five-second question | "What did the $300,000 buy, and which payment does each holding stand for?" (ten Treasury holdings, 89.55%, one per payment year, IBTM also the floor; one world stock fund for the range's top and the flexibility; a little cash and costs) |
| Data | NUMBERS 8g version 2, the WInS record at cost; not a model. 13 holdings plus one subtotal and the total. Amounts in cents as WInS records them; percentages to two decimals by largest remainder, as 8g. Subtotal under the ten Treasuries: $268,652.18, 89.55% (8g "In groups"). Cash $3,513.79 (1.17%) = the cash WInS shows. Costs row $1,309.42 (0.44%) = $200 of commissions + $1,109.42 of bond interest accrued at purchase. Total $300,000.00, 100.00%. |
| Form | Wharton's five columns plus "Pays for" (fresh reader, Wed 11 Nov). Rows in payment order (IBTM for 2033 down to the 3.125% Nov 2041 bond for 2042). Then one subtotal row with a thin rule above and a 6-pt gap after; then VT, cash, the costs row, and a bold Total row under a rule. No spanner rows and no other subtotals (card Q28: IBTM does two jobs, so a grouping by role cannot work; a subtotal of one row adds nothing). Widths 0.67 / 3.17 / 0.47 / 0.85 / 0.55 / 0.79 in, with no padding at the table's outer edges (text flush with the rule ends): every row on one line except the two designed two-line cells. |
| Pays for (fresh reader and coordinator, Wed 11 Nov) | The payment year each holding stands for, from the 23 Oct WInS snapshot's "Pays for" column (8g cites it): 2034 to 2042 for IBTO to the Nov-2041 bond. IBTM: "2033 and / the floor" (snapshot: "2033 payment + floor stand-in"). VT: "Range top, / flexibility" (the snapshot says "growth sleeve"; IPS l.15 gives the two jobs; "flexibility" is the IPS's word for the half promised to no one and Table 2's head, chosen over "half kept", which a stranger cannot read). Cash, costs, subtotal and total: blank. Centred. Those two cells cannot fit one line at 12 pt: the column has 0.75 in of text room and "2033 and the floor" needs 1.2 in. |
| Wording choices (each forced by width at 12 pt) | To make room for "Pays for", asset types are one word, Wharton's own: "ETF" (8g's "ETF (Treasury)" and "ETF (equity)"; each name already says Treasury or Stock) and "Bond" (Wharton's example says "Treasury Bond"; each name says T-Bond). The dollar sign moved into the head, "Amount ($)". The % head is "% of total": "portfolio" needs 0.58 in. The subtotal is named "Treasuries for the ten payments and the floor"; never "the payments" alone, which would contradict the Trading Note on IBTM (card Q28 row 33). |
| Costs row (coordinator, Wed 11 Nov) | Printed "Commissions and accrued interest at purchase" (3.08 in; the column holds 3.09 in), so it fits one line. 8g's name, "Commissions and bond interest paid at purchase" (3.22 in), wrapped to two. Same meaning: $200 of commissions and $1,109.42 of bond interest accrued at purchase. Amount and percentage exactly 8g's ($1,309.42, 0.44%); the check keeps 8g's name and confirms both. Still open (fresh reader): accrued interest is typed "Cost" though it comes back; the note says so. |
| Identifiers | ETFs by ticker. The bonds are placeholders in square brackets: "[532281]" for the May-2038 bond (Wharton's own example row, still to confirm) and "[ID]" for the other four. They are filled from Caplet's final WInS export before 27 Nov (8g "Identifiers"). |
| Number and working title | **Table 1** / *The Final WInS Portfolio at Cost on the Original $300,000: Laura's Whole Plan in Miniature* (one line; 8g's own words for what the book is, which answers the reader's "how do rungs this size become $50,000 each?") |
| Note must carry (about 50 words) | Amounts at cost: quantity held x price paid on 6-7 Oct 2026 (U.S. Eastern), on the original $300,000. Pays for: the payment (1 January of that year) each holding stands for; the full-size plan for both deposits is Figure 1 and Table 2. The floor: the least Laura can promise co-sponsors in 2031; IBTM stands in for the plan's late-2032 floor fund (TNA l.13, CANON A24, 8g). What the costs row holds; the accrued interest comes back with each bond's next coupon. |
| Measured | 16.9 lines with a 50-word note; 12.9 without. Before the "Pays for" column: 14.9 and 11.9. Mon 9 Nov's version: 14.1 lines with a shorter note and no subtotal. |
| Five-second result | Keel's look: the eye lands on IBTM's 32.50% and, beside it, "2033 and the floor", so the big row explains itself; the years then run down the last column. Fresh reader, before the fix: 4 for clarity, 3 for wanting to read on (IBTM's weight unexplained; scale unclear; "[ID]"). Risk left: the bracketed identifiers read as unfinished until Caplet's export fills them. |
| Files | `table1_holdings_2x.png`; Markdown in `tables.md`; built by `add_table1` in `build_exhibits.py`. |

## Exhibit 2 = Figure 1, the operating reserve running down (3a)

| Item | Spec |
|---|---|
| Case question | The case: "recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made". Wharton: "Recommend an appropriate operating reserve". |
| Five-second question | "Which holding pays each year's $50,000, when does its cash arrive, and what covers the gap if nothing earns interest?" (answer in the title: extra Treasuries bought with the 2028 deposit) |
| Form (card Q28: the escrow verifier's sufficiency schedule beside a staircase) | Ten rows, 2033 at the top. Left: the payment year. Middle: one bar per own holding, from purchase (January 2027, at the broken left edge) until its cash arrives, labelled on the bar with its ticker or coupon and date. The bars are light grey for the iBond Treasury ETFs and dark grey with white text for the Treasury bonds. A black tick marks each 1 January payment. A dotted line and the Trading Notes' words mark the two long waits: "cash waits 10.5 months" (Feb-2037 bond) and "cash waits 7.5 months" (May-2038 bond; CANON A16, B35; the model's 7.6 is not printed). Right: three printed number columns: "At forward rates", then, under a spanner "If nothing earns interest", "Own holding" and "Bought with / 2028 deposit" (fresh reader and coordinator, Wed 11 Nov: "Backstop" said neither where the money comes from nor when it is bought; NUMBERS section 2: "In January 2028 the deposit's first dollars also buy extra face in the same Treasuries"; it is not in the WInS book). The 0.15% fee moved from the spanner to the note. A total row sits under a rule, and a legend inside the figure. The axis years run along the head: 2027, then 2033 to 2041. The axis is broken before 2033 (a cut through every bar and through the head rule). |
| Data | NUMBERS 8h, MODEL; `results_reserve_2026-11-10.json`. Holdings and cash dates come from `composition_1jan2033_base`; "At forward rates" from `base` ($50,000 in every row; the backstop is untouched). The zero-interest columns come from `fee`, Keel's standard as SKELETON's Exhibits item 2 sets it: nothing earns interest from 2027 and every waiting dollar pays the Treasury-bill ETF's 0.15% fee. Own holding $47,338 (2033) down to $42,180 (2041) and $42,469 (2042); backstop $2,662 to $7,820; each row exactly $50,000; totals $500,000, $444,080 and $55,920. Nothing is left after 2042; without the fee, $1,414 is left (the `zero` block). |
| Number and working title | **Figure 1** / *Each Payment Has Its Own Treasury; Extra Treasuries Bought With the 2028 Deposit Pay Any Gap if Nothing Earns Interest (Laura's Plan for Both Deposits, $450,000, Modelled)* (two lines; the point first, from NUMBERS section 2's own sentence, then the scale) |
| Note must carry (about 55 words) | MODEL, at forward rates on the Treasury par yield curve of 6 Nov 2026. The right-hand columns are what each payment gets if nothing earns interest from 2027 and waiting money pays the Treasury-bill ETF's 0.15% fee: the $500,000 of payments split between the payment's own holding ($444,080) and the Treasuries bought with the 2028 deposit ($55,920), not the reserve's value on 1 Jan 2033 ($444,545 at forward rates; the reader confused the two). If room: those Treasuries cost $34,369 in 1 Jan 2027 money (section 2) and are not in the WInS book. The standard clause that rows may not add to the totals because of rounding. To 3a's prose: the escrow test's name, the short-term Treasury ETF where waiting money sits (CANON A15), the reserve's funded ratio (111.4%), and nothing left after 2042 ($1,414 without the fee). |
| Rounding (coordinator, Wed 11 Nov) | Every row equals 8h and sums to exactly $50,000. The totals are 8h's totals of unrounded figures ($500,000, $444,080, $55,920); the printed rows foot to $444,081 and $55,919, which the note's rounding clause covers. |
| Words never used | Waiting money is never called cash held at 0% or cash not invested (CANON A15). No fund bar carries a bare "$50,000": the funds pay net asset value (card Q28 row 13). |
| Measured | Image 6.5 x 3.40 in. 16.9 lines with a 55-word note; 12.9 without. Before the fixes: 14.9 and 11.9. Tue 10 Nov's version: 16.0 lines, 3.85-in image, three-line note. |
| Five-second result | Fresh reader, before the fix: bars 5, right-hand columns 2 ("Backstop" undefined; "zero interest on what?"; no title sentence; scale unclear). All four are now addressed in the heads, the title and the note. Open: the reader would drop the constant "At forward rates" column ("tells me nothing"). Kept for now: it shows each own holding pays exactly $50,000 at forward rates (8h), the other half of the escrow test; 3a's prose must say they were sized to do so, or the column goes (dropping it saves no height). |
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

## Decisions taken (coordinator, Wed 11 Nov) and what is still open

1. Taken: Table 1's costs row is printed "Commissions and accrued interest at purchase" (one line).
2. Taken: Figure 1's rows equal 8h; its note carries the standard rounding clause.
3. Taken: Table 2 has no contribution column. Superseded the same day by decision 6: the claim is a table row.
   The two Section 3 notes are held to about 100 words together (now 55 + 45).
4. Taken (fresh reader, coordinator): every title says its scale; Table 1 is the WInS book on the original
   $300,000 (Laura's whole plan in miniature), Figure 1 and Table 2 her plan for both deposits ($450,000), modelled.
   Figure 1's note says its right-hand columns are the $500,000 of payments split, not the reserve's value.
5. Taken: Figure 1 has a title sentence with its point; "Backstop" is "Bought with / 2028 deposit". Table 1 has a
   "Pays for" column (two cells on two lines; +2.0 lines with the note; Section 2 still within budget).
6. Taken: Table 2's last row says the contribution equals the stated top in every world and replay.
7. Open: `../template/build_template.py` belongs to another owner. Its own `add_figure1_reserve` and
   `add_table2_markets` still carry Tue 10 Nov's note text, and its Table 1 has no subtotal. It still runs on the new
   `exhibit_data.py` (compatibility names kept and checked again after these fixes, including its own measuring
   variant with "Pays for"; `SCENARIO_COLUMNS` has five columns without the contribution). Its titles and notes
   predate the scale fix. On 27 Nov, pour with `build_exhibits.py`'s `add_table1`, `add_figure1` and `add_table2`, or update
   the template.

## Former candidates, for the record

1. **The range forming under three markets (chart).** Failed the five-second test on Tue 10 Nov: bands were read as
   outcomes. Superseded by Table 2. The chart file is deleted. On today's register the house-model figures are: floor
   payout $88,047 / $103,097 / $124,380; stated bottom $85,000 / $95,000 / $115,000; stated top $95,000 / $115,000 /
   $140,000 (NUMBERS section 4).
2. **The monitoring table (Table 3, 3e).** Kept as a fourth exhibit (SKELETON item 4; card Q26). Its spec and
   measure are still Q23's: 17.1 lines with filler cells.
3. **The contribution against an all-Treasury plan.** One sentence in 3b, no exhibit. An all-Treasury plan gives
   $140,761 at forward rates (stated $130,000). The FINAL's funds pay $123,476, and the stated top is $115,000.
   Counting the half kept and the excess, the FINAL's house-model median is $145,687 against $140,649, and its
   1-in-20 low $113,449 against $113,169 (NUMBERS section 4, C8).
