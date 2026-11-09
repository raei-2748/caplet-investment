# Exhibit specs for the Final Report (Tue 10 Nov 2026)

Design notes, not report text. Every figure comes from `../NUMBERS.md` with its section (MODEL where the register says
so); nothing here is new arithmetic except sums and rounding. Data module: `exhibit_data.py`. Figure renderer:
`build_exhibits.py`. Tables are real Word tables built by `../template/build_template.py` (`demo` writes the test PDF
with all three exhibits in place). Research and sources: `../research/cards/Q23_exhibits_and_format.md`.

## 0. Rules that apply to every exhibit

- **Labels in the report follow APA 7, not Keel's "Exhibit" numbers.** APA numbers tables and figures separately, in
  the order the text calls them out: Exhibit 1 = **Table 1**, Exhibit 2 = **Figure 1**, Exhibit 3 = **Table 2** (and a
  monitoring table, if 3e uses one, = **Table 3**). "Exhibit" stays as Keel's internal name only.
- **Layout (APA 7, apastyle.apa.org, read 10 Nov):** number in bold; title on the next double-spaced line in italic
  title case; table body single-spaced (APA allows single, 1.5 or double; Wharton: "Tables and graphics may be
  single-spaced when needed for readability"); number, title and note double-spaced; borders only at the top, under the
  column heads, above a totals row and at the bottom, never vertical; column heads centred, sentence case; "*Note.*"
  in italics; each exhibit placed after its first call-out, at the top or bottom of a page, with one blank
  double-spaced line between it and the text.
- **Font:** Times New Roman everywhere, including inside figure images (at least 10 pt at printed size). APA advises
  a sans-serif font inside figure images, but Wharton's rule is "Use 12-point Times New Roman font" and Wharton asks
  for APA only for citations; Keel follows Wharton (card Q23 row 16).
- **Black and white.** Two greys at most plus black; no colour carries meaning (judges may print).
- **Cost on the page (measured, Letter, 23 lines a page, about 14 words a line):** Table 1 = 14.1 lines (about 200
  words of prose); Figure 1 = 16.0 lines (about 230); Table 2 = 11.1 lines (about 160); a monitoring table of seven
  rows = 17.1 lines (about 245). Each count includes the number, title, note and the blank line after.
- **Five-second test** (Perfetti, 2007): look for five seconds, cover it, say what you remember. Each spec names the
  one question a first reader should be able to answer. The results below are Keel's own first-look check on the
  rendered drafts; the fresh-reader test with people is still due Mon 23 Nov (`../TOOLS.md`).

## Exhibit 1 = Table 1, the holdings (required)

| Item | Spec |
|---|---|
| Case question | Wharton, Section 2: "Include a table listing every holding in your final WInS portfolio ... ticker or identifier, name, asset type, amount allocated, and percentage of the portfolio ... expressed using the original $300,000 ... The total must equal $300,000 and 100%." A minimum requirement ("Actual holdings"). |
| Five-second question | "What did the $300,000 buy?" (ten Treasury holdings, one world stock fund, a little cash) |
| Data | `NUMBERS.md` 8g, version 2 (the WInS record at cost; not a model). 13 rows and a total: five iBond ETFs, five T-bonds, VT, cash $3,513.79, and commissions and accrued interest $1,309.42; $300,000.00 and 100.00%. |
| Form | APA table, Wharton's five columns only: Ticker or identifier, Name, Asset type, Amount, %. Body single-spaced, 12 pt; every row on one line. Amounts to the cent, right-aligned; percentages to two decimals (largest remainder, as 8g), right-aligned; Total row bold under a thin rule. Rows in payment order (2033 to 2042), then VT, cash, costs. |
| Number and title | **Table 1** / *Laura's Plan in Miniature: The Final WInS Portfolio at Cost* |
| Note (draft) | *Note.* Amounts are the quantities held times the prices paid on 6-7 October 2026 (U.S. Eastern), on the original $300,000. Cash is the cash shown in WInS; costs are $200 of commissions and $1,109.42 of accrued bond interest. |
| Measured | 14.1 double-spaced lines (5.4 in). A double-spaced body does not fit on one page at all (it spans two), so the single-spacing allowance is what keeps the required table whole. |
| Choices made for width | Full fund names need 3.04 in at 12 pt ("iShares iBonds Dec 2032 Term Treasury ETF"). To keep each row on one line: asset types use Wharton's own example labels ("ETF", "Treasury bond", "Cash") rather than 8g's "ETF (Treasury)"; the costs row reads "Commissions and accrued interest" (8g: "Commissions and bond interest paid at purchase"); the last column head is "%"; cell padding 0.04 in. |
| Not adopted | The panel's "Pays for" column (bond desk). At 12 pt it forces every iBond name onto two lines (18.1 lines instead of 14.1). Figure 1's "Paid from" column carries the same mapping, so nothing is lost. If Caplet wants the roles in Table 1 itself, the cheaper form is three APA table spanner rows ("Treasuries for the ten payments and the floor", "Growth", "Cash and costs", with 8g's group totals 89.55%, 8.84%, 1.61%): about 1.5 more lines. |
| Open | The five bond identifiers are "[WInS ID]" until Caplet's final WInS export (8g "Identifiers"); 532281 is Wharton's own example row for the May-2038 bond and still unconfirmed. SKELETON v2 says the $1,309.42 is "placed inside the holdings they paid for", but NUMBERS 8g v2 keeps it on its own row and says why (WInS's accrual on the May-2038 bond differs); the table follows the register, and SKELETON's wording needs a one-line fix by the lead. |
| Five-second result | Passes. The eye lands on the column of dollar amounts and the bold $300,000.00 / 100.00 total; the five near-identical "iShares iBonds" rows read as one block of Treasuries; VT stands out as the one stock fund. Risk: "[WInS ID]" placeholders read as unfinished; they must be filled before 27 Nov. |
| Files | Built in `../template/build_template.py` (`add_table1_holdings`); preview `exhibit1_holdings_preview.png` (cropped from the test PDF). |

## Exhibit 2 = Figure 1, the operating reserve running down 2033-2042

| Item | Spec |
|---|---|
| Case question | The case: "recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made"; Wharton: "Recommend an appropriate operating reserve"; the Client Knowledge criterion names "liquidity needs". SKELETON v2: "ten bars or rows, one per payment, each showing which holding pays it, when its cash arrives and how much it pays above $50,000". |
| Five-second question | "Which holding pays each year's $50,000, and when does its cash arrive?" |
| Data | `NUMBERS.md` 8h (MODEL, Keel's design A, 6 Nov curve's forwards): the ten holdings in payment order; cash arrives 15 December for the iBond ETFs (about half a month early), 15 Feb 2037 (10.5 months), 15 May 2038 (7.6 months), 15 Nov of 2039, 2040 and 2041 (1.5 months). "Above $50,000" per rung: $1,705, $2,085, $2,499, $2,979, $3,594, $4,487, $4,572, $4,648, $5,266, $5,025 ($36,859 in all), read from `numbers/results_reserve.json`, the engine file 8h names; 8h prints only the ends and the sum, and the 8h table gives the same values to within $1 (before less paid less after). **Add this column to NUMBERS 8h before 27 Nov.** |
| Form | Ten rows, one per payment, 2033 at the top. Left: year and the holding that pays it. Middle: a bar for each holding, held from January 2027 until its cash arrives (light grey = iBond Treasury ETF, dark grey = Treasury bond), and a black tick at the 1 January payment; a dotted line and the words "cash waits 10.5 months" / "7.6 months" where the wait is long enough to see. Right: what each pays above $50,000. One axis (years, starting in January 2027 and broken before 2033), hairline year grid, legend inside the figure. Reads three ways at once: one holding per payment; the light-grey funds are gone after 2037 (half funds to all bonds); one holding drops away each year (the run-down, no selling). |
| Number and title | **Figure 1** / *The Operating Reserve Runs Down One Holding a Year, 2033-2042* |
| Note (draft) | *Note.* Model values at forward rates on the Treasury curve of 6 November 2026 (U.S. Department of the Treasury, 2026). "Above $50,000" is what each holding pays beyond its payment at those rates; if reinvestment earns 3 points less, each pays exactly $50,000. (NUMBERS 8h: design A, sized so each rung pays $50,000 if every reinvestment earns 3 points below the forwards.) |
| Measured | Image 6.5 x 3.85 in at 300 dpi; 16.0 double-spaced lines with number, title and a three-line note. |
| Rejected form | A stacked bar of the reserve's value each 1 January ($427,028 falling to $55,025). It shows size, but it puts "$427,028 against $500,000 still owed" in the picture, the comparison two judges said alarms a lay reader unless a sentence explains it. Size and the 107% funded ratio go in 3a's prose, where the explanation sits beside them. |
| Five-second result | Passes on the designed question: the first thing seen is the staircase of bars each ending at a black tick one year apart, then the two long waits labelled in words; the switch from light to dark grey after 2037 is the second thing seen. Two risks found on the first draft: the bars started at the axis edge (2032), so a reader could think they were bought in 2032; fixed on 10 Nov with a broken axis (a "2027" tick at the left and a cut through every bar, the usual mark for a skipped stretch). Still open: "Above $50,000" can be misread as the payment being larger than $50,000 unless the note is read. A fresh reader should be asked both on Mon 23 Nov. |
| Files | `exhibit2_reserve.png` (300 dpi, in the template), `exhibit2_reserve.svg` (text kept as text, Times New Roman then Liberation Serif), `exhibit2_reserve_preview.png` (as laid out in the test PDF). |

## Exhibit 3 = Table 2, the plan under four markets (SKELETON v2's choice; data still to come)

| Item | Spec |
|---|---|
| Case question | The case's "favorable and unfavorable market outcomes"; Wharton: "Explain the level of confidence associated with that range and the factors that could affect it"; panel 1 asked for a scenario table (two judges) and for the 2031 announcement under three markets (one judge); one table answers both. |
| Five-second question | "In a bad market, what still holds and what shrinks?" (the payments hold; the top and the half kept shrink) |
| Data | Cards Q19 and Q24 (other workers, not landed on 10 Nov). Today only the central row has register figures, from `NUMBERS.md` 4: stated range $110,000 to $130,000 (the top's per-end correction is "under review"), gift $138,735 (floor $115,929 plus moved half $22,806; capped at the stated top if CANON D12's cap rule is adopted), half kept $23,986. The rates-lower row's payments column comes from `NUMBERS.md` 2 and 8h (design A pays every rung exactly $50,000 if reinvestment earns 3 points less). Every other cell is "[Q24]". |
| Form | APA table: rows = today's forward rates; rates 3 points lower for good; a recession replayed from history (shares and rates falling together); inflation (rates up, shares flat). Columns = ten payments, stated range (2031), gift (late 2032), half kept (2033). 16 numbers: a table, not a chart (Tufte: tables beat graphics for 20 numbers or fewer). Single-spaced body; dollars rounded to the nearest $1,000 except the stated range. |
| Number and title | **Table 2** / *The Plan Under Four Markets* (to sharpen on 27 Nov once the numbers say what the table shows) |
| Note (draft) | *Note.* Model values. The stated range is what Laura can announce before the 2031 meetings; the gift is what the floor and the moved half pay in late 2032. [One sentence per non-central row naming its source when Q24 lands.] |
| Measured | 11.1 double-spaced lines with the placeholder note. |
| Five-second result | Cannot pass yet (placeholders). The design passes if the payments column reads the same words in all four rows, so the eye finds the one column that never changes; keep that column first after the row labels. |
| Files | Built by `add_table2_markets` in the template; preview `exhibit3_markets_preview.png`. |

## The former Exhibit 3 candidates (for the record)

1. **The range forming under three markets (chart).** Drafted as `exhibit3_range_candidate.png` with NUMBERS 4's
   house-model bands as PLACEHOLDERS (bottom $93k / $116k / $140k; top $111k / $139k / $171k). It **fails** the
   five-second test: the first look shows grey and dark bands of different heights, and a reader cannot tell which end
   is which, or that the bands are 1-in-20 spreads from today rather than outcomes, without reading the legend. It
   also mixes marginal spreads (the top's band includes the floor's yield risk). Superseded by Table 2, as SKELETON
   v2 decided.
2. **The assumptions and monitoring table.** Kept, but as its own table in 3e (SKELETON v2: "the monitoring table
   carries most of 3e"), not as Exhibit 3. Spec: **Table 3** / *What to Monitor as 2031 and 2033 Approach*; columns
   What Laura watches, When, What it can change, What it never changes; rows from CASE_MAP E item 2 (Treasury yields
   in January 2028, VT before the 2031 move, the Taiwan dollar and building costs, co-sponsor budgets, each iBond
   fund's payout against par, the 2028 deposit, a U.S. Treasury default); the last two are the IPS's only two reasons
   to change. Measured with filler cells of realistic length: 17.1 lines (about 245 words of prose displaced, while
   holding about 160 words of content single-spaced). **It is a fourth exhibit**: SKELETON v2's "about a page" for
   Exhibits 2 and 3 does not include it.
3. **The gift against an all-Treasury plan.** Fold into one sentence in 3b, no exhibit: NUMBERS 4 C8 gives four
   numbers (all-Treasury certain $158,157 with the margin; the FINAL's median top $138,735 central; counting the half
   kept, median $164k against $158k, and about the same in the 1-in-20 low, $128k against $127k). Four numbers sit
   better in a sentence than in a figure, and the funder judge read this comparison as second-guessing the IPS.
