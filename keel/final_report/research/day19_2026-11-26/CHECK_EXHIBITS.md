# Exhibits check before the writing day (Thu 26 Nov 2026, Sydney)

Read-only check of the four printed exhibits (Table 1, Figure 1, Figure 2, the watch list) and of Caplet's own Table 1.
Checked against `NUMBERS.md` (the only source of figures), `CANON.md`, `NAME_ORDER.md` (the lead's decisions of Wed
25 Nov evening win), `SECTION_NOTES.md` (Exhibits block) and `WORDS.md`. Files read: `charts/FINAL_2026-11-23.md`,
`exhibits/tables.md`, `exhibits/specs.md`, `exhibits/exhibits_letter.pdf` (text), the SVG text of
`charts/final/figure1_reserve.svg` and `figure2_markets.svg`, `voice/round21/CAPLET_V2_SECTION2_2026-11-25.md`,
`CAPLET_DOC_2026-11-25.md`, `numbers/reserve.py`, `numbers/results_reserve_2026-11-17.json`. Nothing was rebuilt or
edited.

**Short answer.** Every figure printed in the four exhibits matches NUMBERS (Table 1 to the cent; Figure 1's fee basis
to the dollar; Figure 2's ten ends and six flexibility dots; the watch list's $3,016, $57,455, $85,000, 3.57 points,
$11,500, $28,700, 1.5% to 5.0%, 0.5%). The mismatches are labels and names that the decisions of Tue 24 and Wed 25 Nov
changed after the exhibits were built on Mon 23 Nov, plus Figure 1's basis. Caplet's Table 1 matches NUMBERS 8g and the
exhibits' Table 1 in every dollar amount, weight, CUSIP and total.

## 1. Mismatches

Severity: H = would print wrong or against a lead's decision; M = against a name rule or a note the notes ask for;
L = wording to tidy when the note is written on Fri 27 Nov.

| # | Exhibit | Cell or line | Says | Should say | Source | Sev |
|---|---|---|---|---|---|---|
| 1 | Watch list | Printed label (`exhibits_letter.pdf` p.6; `tables.md` heading) | "Table 3" | "Table 2" in print (Keel files keep "Table 3") | NAME_ORDER decision 8 | H |
| 2 | Watch list | Row 6 "Carry on while" | "Signed; each sees the late-2032 fund's statement in 2031 and before it pays" | The broker's own statement of a second account holding the building's two IBTM lots and their paid distributions, seen at the 2031 meetings and before the December 2032 payout (a fund sends no statement; never the single IBTM line, which overstates the building's money by $20,000 to $27,000) | NUMBERS 8y ("never the IBTM line"; second account); NAME_ORDER row 55; SECTION_NOTES Table 3 (8y) | H |
| 3 | Figure 1 | Basis of every row, the total row and note item 2 | Fee-only basis: $444,080 + $55,920, "$1,177 to spare" | Fee-and-margin basis ($442,930 + $57,070, nothing left), or the fee-only basis labelled as such in the title or note. The fee-only basis also disagrees with ink's definition, which counts each fund "after the 0.5% margin" | CAPLET_DOC item 4; NAME_ORDER row 14 (FACTS l.183); NUMBERS 8h l.1199, l.1275; spec in section 3 below | H |
| 4 | Watch list | Row 1 "Carry on while" | "first $39,162 (today's rates) to the payments" | "about $39,000" (prose and the watch list carry one rounded figure; $39,162 can stay in the note) | NAME_ORDER row 42 ("3e (Table 3: 'about $39,000')"); WORDS l.78 | M |
| 5 | Watch list | "Who" column | "Laura" / "Team" | Wharton's own pair, "Laura" or "her asset management team" | SECTION_NOTES Table 3, cards Q249-Q250 (WHARTON_NORTH_STAR l.122) | M |
| 6 | Watch list | Rows with dates (1, 4, 6, 7) | No cue document named; row 1 "Confirmed by 1 Dec 2027" | Each dated row names the document that brings it (broker's statement, at least quarterly; the funds' October end notices; January trade confirmations; the 2031 meetings); row 7 rides the statement; row 1's look is a small act: "confirm the deposit's date with Laura by 1 Dec 2027" | SECTION_NOTES Table 3, cards Q249-Q250 | M |
| 7 | Figure 1 | Type label and legend (SVG "iBond Treasury fund"; `tables.md` Type column) | "iBond Treasury fund" | "iBonds Treasury fund" | NAME_ORDER decision 14 (wins over WORDS l.22) | M |
| 8 | Table 1 | Note, the floor item | "the floor: the late-2032 Treasury fund whose payout sets the least Laura can promise in 2031 (TNA l.13), here IBTM's floor lot" | The floor is the January 2028 purchase of more of the late-2032 Treasury fund, not the fund: e.g. "the floor: more of the late-2032 Treasury fund (IBTM), bought in January 2028, whose payout sets the bottom of her range; in the WInS portfolio a second IBTM lot stands in for it". Drop "IBTM's floor lot" | NAME_ORDER decision 3, row 30 (never "IBTM floor shares") | M |
| 9 | Table 1 | Note, reconciliation item | "(the extra Treasuries, $36,774)" with no gloss | Add decision 2's gloss: "more Treasuries bought in January 2028 so the ten are paid even if cash waiting earns nothing" (Table 1 sits in Section 2, before 3a sets the name up) | NAME_ORDER decision 2, row 34 | M |
| 10 | Table 1 | Note, "if room" item | "a wait the zero-interest test covers" | "a wait covered because the ten are paid even if cash waiting earns nothing" | NAME_ORDER decision 14 (never "zero-interest test" in print) | M |
| 11 | Figure 1 | Note item 8 | "the floor's IBTM shares are a separate lot from the 2033 payment's" | Either cut (3a comes before 3b sets up the floor; Figure 1 is not in row 30's "Used in") or "the IBTM bought in January 2028 for the building is a separate lot from the 2033 payment's" | NAME_ORDER row 30, decision 3 | M |
| 12 | Figure 2 | Row names (SVG and Table 2) | "Replay from 2006: shares fall"; "Rates 3 points lower from Jan 2027"; "Replay from 2007: rates fall early"; "Inflation: rates 3 points higher" | The notes' row names: "a recession from history" (two of them, so each needs its year), "rates lower for good", "an inflation world"; at least "Rates 3 points lower for good from Jan 2027", as NUMBERS 8i has it ("for good" dropped in print) | SECTION_NOTES Figure 2; NAME_ORDER row 52; NUMBERS 8i row 2 | M |
| 13 | Figure 2 | Note, dates item | "the top to the move's, Thu 2 Jan 2031" | "the top to the January 2031 move's trade day, Thu 2 Jan 2031" (a note may be read before 3b sets up "the move") | NAME_ORDER decision 4 | L |
| 14 | Figure 1 | Note item 2 | "buys $37,711 at face" | "buys $37,711 of face value and fund dollars" ("face" alone is banned; part of the $37,711 is IBTQ and IBTR dollars, not face) | NAME_ORDER row 48; NUMBERS 8h ("$37,711 ... of face and fund dollars") | L |
| 15 | Figure 1 | Note item 2 | "the waiting fund's 0.15% fee" | "the short-term Treasury ETF's 0.15% a year" ("the fee" is the funds' 0.07%) | NAME_ORDER rows 32 and 47 | L |
| 16 | Figure 1 | Note item 8 | "at zero interest and before the waiting fund's fee the Treasuries pay about $502,600" | "if cash waiting earns nothing and pays no fee, the Treasuries pay about $502,600 against the $500,000 owed" | NAME_ORDER Conflict 14, decision 14; NUMBERS 8x (e) l.2899 | L |
| 17 | Figure 1 | Exhibit content against SECTION_NOTES | No release rule in figure or note | SECTION_NOTES asks for "the release rule"; the spec drops it. Either add one note clause (each 1 January, Treasury-ETF money above what every later payment needs can come back; NUMBERS 8h release table) or strike it from SECTION_NOTES | SECTION_NOTES Figure 1; NUMBERS 8h | L |
| 18 | Figure 1 | "waits 10.5 months" on the Feb-2037 bar | 10.5 months, drawn from the cash date Tue 17 Feb 2037 | No change needed: 10.5 is CANON B19's count from 15 Feb (10.4 from the cash, NUMBERS 8h). The 7.5 months on the May-2038 bar is exact from the cash. Recorded so no checker "fixes" it | CANON B19, B35; NUMBERS 8h cash table; SECTION_NOTES trap ("7.6 months") | none |
| 19 | All | Source lines | Table 1's "Data from the team's WInS trade record, 6-7 Oct 2026; team calculations." | Still has no works-cited entry; DGBAS (n.d.) may become (n.d.-a) if both DGBAS sets are cited | charts/FINAL_2026-11-23.md open items 6 | L |
| 20 | Figure 1 (if rebuilt) | Rows 2034-2037, 2039, 2040, 2042 on the fee-and-margin basis | Not registered: NUMBERS 8h names only $442,930, $57,070, $2,899 (2033) and $7,820 (2041) | Register the ten rows of `fee_and_margin.by_payment` in NUMBERS 8h before they print (every printed figure from NUMBERS) | CLAUDE.md; NUMBERS 8h l.1199, l.1275 | H if rebuilt |

Checked and right (no change): Table 1's every amount, %, CUSIP and both subtotals (NUMBERS 8g; sum $300,000.00,
weights 100.00% by largest remainder); Table 1's note figures ($293,830 / $109,148 / $39,787 against $339,162 /
$81,244 / $29,594; $36,774; $200 + $1,109.42; "about $160 against about $200"); Figure 1's ten rows and totals on the
fee basis (8h), cash dates (8h cash table), note items 4-6 ($46,600, $445,700, $1.12, 3% and 15%); Figure 2's ends
($95,000/$115,000, $95,000/$105,000, $75,000/$95,000, $80,000/$95,000, $100,000/$115,000, median $95,000/$115,000) and
dots ($28,700, $18,500, $19,600, $20,500, $27,600, $31,800; 8i, 8j l.1366), its note's 7.5%, 17.88%, 0.9 points,
about 2%, about $120 per 0.1% (8u: $118), 4% to 10%, 3.1% and $110,000, 585 months; the watch list's $3,016 and $57,455
(section 5), $85,000 (section 5), 3.57 points (section 5), $11,500 (8j), $28,700 (8i: $28,682), 1.5% to 5.0% (8d),
0.5% trade-day limit (section 4), "wait, never past the first 2031 meeting" (8r); no "book", no conceit word, no 5th or
95th percentile, no "forward rates" row name, no "secured", no "automatic" in any printed exhibit.

## 2. Caplet's own Table 1 (v2 tab, read Wed 25 Nov 22:55), cell by cell

Against NUMBERS 8g and the exhibits' Table 1 (`exhibits/tables.md`). All 15 dollar amounts and all 15 weights match to
the cent and the hundredth. The ten Treasury amounts add to $268,652.18 (89.55%); with VT $26,524.61 (8.84%), cash
$3,513.79 (1.17%) and costs $1,309.42 (0.44%) the total is $300,000.00 and the weights add to 100.00%. The five CUSIPs
(912810PT9, PX0, QD3, QL5, QT8) match 8g and card Q38, each with the right coupon and maturity. The note's $200 of
commissions and $1,109.42 of accrued bond interest match 8g version 2.

| # | Cell or line | Caplet says | Suggestion | Source | Sev |
|---|---|---|---|---|---|
| C1 | Note, last sentence | "Individual weights are rounded." | "Weights are rounded so that they add to 100.00%." Plain rounding would show the May-2038 bond at 6.21% (18,615.26 / 3,000 = 6.2051); the table shows 6.20%, by largest remainder. A judge who checks one cell finds 6.21 | NUMBERS 8g ("largest remainder: the May-2038 bond shows 6.20% rather than 6.21%") | M |
| C2 | Below the note | No source line | Add "Data from the team's WInS trade record, 6-7 Oct 2026; team calculations." (APA table note) | exhibits Table 1 spec; FINAL_2026-11-23 decision 6 | L |
| C3 | Bond names | "4.750% Treasury, Feb 2037" and so on | Fine as is. If the team wants Wharton's own example form, "T-Bond 4.750% 15-Feb-2037"; both name the same CUSIP. The day matters in 3a (the Feb-2037 bond pays 15 Feb, 10.5 months early) | NUMBERS 8g; CANON B19 | L |
| C4 | Fees row, Type cell | a dash | "Cost" (8g's word), or leave blank | NUMBERS 8g | L |
| C5 | Title | "Final WInS Portfolio and Intended Investment Roles" | Wharton asks for amounts "expressed using the original $300,000"; the note says "at purchase cost". Adding "at Cost on the Original $300,000" to the title or note answers Wharton's line where the judge looks | WHARTON_NORTH_STAR section 0; NUMBERS 8g | L |
| C6 | Heading and header cells | "Portfolio Implementation****"; "Allocation " (trailing space) | Formatting residue in the doc export; tidy | n/a | L |
| C7 | Roles | IBTM "2033 payment and facility floor"; VT "Facility growth and flexibility"; cash "Liquidity" | Consistent with CANON A24-A26 and the exhibits' "Pays for" column. No change. No conceit word in the table (NAME_ORDER decision 9) | CANON A24, A25, A26 | none |

Caplet's table has no units column and no "All holdings" subtotal: neither is a Wharton requirement, so nothing is
missing. Its prose ("nearly 90% of our WInS portfolio to US Treasuries") matches 89.55%.

## 3. Figure 1 on the fee-and-margin basis

**Engine output.** `numbers/results_reserve_2026-11-17.json`, block `fee_and_margin`, written by `numbers/reserve.py`
(lines 196-210: `C.cost_cut(I)` takes 0.5% off every iBond fund flow, then `C.ledger(C.FEEW, ...)`). Its world: "nothing
earns interest, every waiting dollar pays the ETF's 0.15% a year, every iBond fund flow 0.5% smaller". Registered in
NUMBERS 8h (l.1199 and l.1275): own holdings $442,930, backstop and carry $57,070, from $2,899 (2033) to $7,820 (2041),
nothing left. The other eight row values below are in the JSON only and must be registered in 8h before printing
(item 20 above).

**What changes.** Only the five fund rows (2033-2037) and the totals: each fund's own payout is 0.5% smaller ($223 to
$237 a row) and the extra Treasuries cover the same amount more. The five bond rows are identical on both bases (bonds
carry no fund cost). The bars do not move: they are a time axis, and every cash date is unchanged (8h cash table). The
today's-rates items (note items 4-6) do not move, since the margin changes only the stress world.

### Rows

| Payment (1 Jan) | Paid from | Type | Cash arrives | Its own Treasury | + Extra Treasuries | = $50,000 | Change from fee-only basis |
|---|---|---|---|---:|---:|---:|---|
| 2033 | IBTM | iBonds Treasury fund | Mon 20 to Wed 22 Dec 2032 | $47,101 | $2,899 | | own -$237, extra +$237 |
| 2034 | IBTO | iBonds Treasury fund | Mon 19 to Thu 22 Dec 2033 | $46,497 | $3,503 | | -$234 / +$234 |
| 2035 | IBTP | iBonds Treasury fund | Mon 18 to Fri 22 Dec 2034 | $45,911 | $4,089 | | -$231 / +$231 |
| 2036 | IBTQ | iBonds Treasury fund | Thu 20 to Mon 24 Dec 2035 | $45,204 | $4,796 | | -$227 / +$227 |
| 2037 | IBTR | iBonds Treasury fund | Thu 18 to Mon 22 Dec 2036 | $44,268 | $5,732 | | -$223 / +$223 |
| 2038 | 4.750% Feb 2037 | Treasury bond | Tue 17 Feb 2037 (waits 10.5 months) | $43,195 | $6,805 | | none |
| 2039 | 4.500% May 2038 | Treasury bond | Mon 17 May 2038 (waits 7.5 months) | $43,061 | $6,939 | | none |
| 2040 | 4.375% Nov 2039 | Treasury bond | Tue 15 Nov 2039 | $43,043 | $6,957 | | none |
| 2041 | 4.250% Nov 2040 | Treasury bond | Thu 15 Nov 2040 | $42,180 | $7,820 | | none |
| 2042 | 3.125% Nov 2041 | Treasury bond | Fri 15 Nov 2041 | $42,469 | $7,531 | | none |
| **Paid 2033-2042, added up** | | | | **$442,930** | **+ $57,070** | **= $500,000** | was $444,080 + $55,920 |

Sources: rows from `fee_and_margin.by_payment` (unrounded: 47,100.96 / 2,899.04; 46,497.10 / 3,502.90; 45,911.11 /
4,088.89; 45,204.04 / 4,795.96; 44,268.28 / 5,731.72; 43,195.04 / 6,804.96; 43,061.09 / 6,938.91; 43,043.06 / 6,956.94;
42,179.79 / 7,820.21; 42,469.11 / 7,530.89); totals `own_total` 442,929.57 and `backstop_total` 57,070.43, registered in
NUMBERS 8h; `short_total` and `left_after_2042` both 0.00. Cash dates: NUMBERS 8h cash table. Each row adds to exactly
$50,000 rounded. Rounded rows add to $442,929 and $57,071; the total row prints the unrounded totals, $442,930 +
$57,070, as Figure 1 does today (a $1 rounding note stays).

### Title

Recommended (labels the basis where Caplet asked, the title is the figure's claim):
*If Cash Waiting Earns Nothing and Each Fund Pays 0.5% Less, Each $50,000 Payment Is Still Met by Its Own Treasury and
Extra Treasuries From the 2028 Deposit*

Shorter alternative, keeping today's title and putting the 0.5% in note item 1. Either way the 0.5% is called "the
margin" only after it is glossed (NAME_ORDER row 19).

### Note items on this basis (writers write the note on Fri 27 Nov; each item with its source)

1. **The condition, defined once.** Money a bond or fund has already paid out earns nothing while it waits for its
   1 January payment, and pays the short-term Treasury ETF's 0.15% a year; every coupon and fund payout still counts;
   and each iBonds Treasury fund's payouts are counted 0.5% smaller, the margin for the funds' costs beyond their
   0.07% fee (such as the cost of trading). This is ink's own count (FACTS l.183). Sources: reserve.py `fee_and_margin`
   world; NUMBERS 8h l.1199, l.1275; section 2 ("Closed Tue 17 Nov evening"); NAME_ORDER rows 14, 18, 19, 47.
2. **The extra Treasuries reconciled.** Their $36,774 (January 2028) buys $37,711 of face value and fund dollars; with
   $19,489 of their own interest, added up undiscounted, that is $57,200; after the short-term Treasury ETF's fee and
   the 0.5% margin, $57,070 reaches the payments and nothing is left: the standard is met exactly. Sources: NUMBERS 8h
   ("What the top-up pays", l.1188-1199). The $130 between $57,200 and $57,070 is arithmetic and not a registered line;
   print it only after the numbers owner registers its split (fee against margin).
3. **Rounding.** Rows are rounded to the dollar and add to $442,929 and $57,071; the total row is the totals of the
   unrounded figures, $442,930 + $57,070 = $500,000. Source: `fee_and_margin` own_total, backstop_total.
4. **The other basis, today's market rates** (unchanged): each own Treasury pays its whole $50,000 and about $46,600 of
   the extra Treasuries comes back to Laura by 2042 (valued at 1 January 2033); about $1.12 for each $1 the payments
   need on 1 January 2033; the operating reserve's size, printed once, here: about $445,700 at today's rates. Sources:
   NUMBERS 8h, 8k ($46,566; $445,655); NAME_ORDER decisions 6 and 7.
5. **Curve** (unchanged): Treasury par curve of 6 Nov 2026; each payment in its own year's dollars. Source: 8h.
6. **Why the extra Treasuries rise with the years** (unchanged): interest earned on interest is 3% of the 2033 payment
   and about 15% of the 2041 and 2042 payments. Source: 8a.
7. **Source line** (unchanged): "Data from U.S. Department of the Treasury (n.d.); team calculations."
8. **If room** (replaces today's item 8):
   - If the funds cost nothing beyond their fee, the own Treasuries pay $444,080, the extra Treasuries $55,920, and
     $1,177 is left (NUMBERS 8h four-world table). This keeps the old basis as a labelled line.
   - If cash waiting earns nothing and pays no fee, and the funds cost nothing beyond their fee, the Treasuries pay
     about $502,600 against the $500,000 owed (NUMBERS 8x (e) l.2899: $502,604).
   - Rows end when the cash reaches Laura (8h cash table).
   - The $2,388 that completes the ten sits in "Its own Treasury" (8h).

**Knock-on.** Figure 1's page cost is unchanged if item 8's first bullet replaces the old item 8's $502,600 sentence
(about the same length). 3a's prose: if it quotes the extra Treasuries' column, it quotes $57,070 and "nothing left",
never "$1,177 to spare". `exhibits/exhibit_data.py` reads the `fee` block today; a rebuild would point Figure 1 at
`fee_and_margin` and its check list at the newly registered 8h rows.
