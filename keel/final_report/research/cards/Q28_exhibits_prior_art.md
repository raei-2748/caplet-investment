# Q28 research cards: prior art for the three exhibits (how professionals show a matched bond book, a plan under several markets, and a holdings list)

**Date.** Tue 10 Nov 2026 (Sydney evening; Tue 10 Nov early morning in the US). Web sources were read at the source that
day with Parallel web_fetch (full text) unless a row says otherwise. Chart images in three PDFs could not be rendered
(proxy 403 on direct download), so their form is taken from captions, axis labels and series names in the extracted text.

**Report parts.** Section 2, Table 1 (the holdings); Section 3a, Figure 1 (the reserve running down); Sections 3b and
3c, Table 2 (the plan under several markets).

**Notes for the Final Report store, not report prose.** Every figure about Caplet's plan is from `../../NUMBERS.md`
(section named; 8h and 8i are MODEL, 8g is the WInS record at cost). Design input for tomorrow morning's exhibit
rebuild (`../../exhibits/specs.md`, `exhibit_data.py`). Does not redo card Q23 (page budget, APA layout, Tufte's
20-number rule, Few's look-up versus shape, the five-second test, the failed range chart).

**Claims tested.**
1. Keep, kill or change: "Professionals show a cash-flow-matched bond book against its liabilities as paired bars by
   year (asset cash flow against the payment), and Figure 1 (one bar per payment: which holding pays it, when its cash
   arrives, how much above $50,000) is that form."
2. Keep, kill or change: "For lay readers a scenario table beats a fan chart for showing a plan under several markets."
3. Keep, kill or change: "Grouping holdings by role with subtotals reads faster than a flat list" (Table 1), within
   Wharton's rule: every holding with ticker or identifier, name, type, amount and %, totalling $300,000 and 100%.

**Problem class and the field that solved it.** Showing that dated assets cover dated fixed payments, to a reader who
must trust it at a glance: solved in municipal bond defeasance (the escrow verification report's sufficiency
schedule), pension cash-flow-driven investment, insurance cash-flow testing (New York Regulation 126) and lottery
annuity funding. Showing one plan under several futures to non-specialists: central-bank forecast communication and
the psychology of risk communication (Bank of England, Bernanke Review, Winton Centre, Joslyn). Table and graph
form: statistical graphics (Cleveland and McGill; Wainer; Ehrenberg; Few), APA 7, and how funds file their own
holdings with the SEC.

## Verdicts in one screen

| Claim | Verdict | In one line, with sizes |
|---|---|---|
| 1. Paired bars are the professional form, and Figure 1 is that form | **CHANGE** (the "paired bars" half is KILLED) | No source read uses paired bars. Escrow verifiers (two real EMMA reports) use a sufficiency TABLE by payment date (requirement, receipts, excess, balance) plus a securities-by-date receipts matrix that forms a staircase; pension CDI managers (BlackRock, SEI, Barnett Waddingham) chart stacked asset cash flows against a liability line; iShares draws ticker-labelled stepped rungs. Figure 1's staircase is a fair picture of the verifier's matrix and the iShares ladder: keep it. Its third element is void: under NUMBERS 8h every own holding pays exactly $50,000 at forward rates, so "above $50,000" is $0 in all ten rows (the specs' $1,705 to $5,266, $36,859 in all, belong to the retired design). Replace it with the escrow test: own holding plus backstop equals $50,000 if interest earns nothing ($47,413 + $2,587 for 2033 up to $42,347 + $7,653 for 2041; $445,405 + $54,595 in all, 8h). |
| 2. A scenario table beats a fan chart for lay readers | **CHANGE** (keep the table; change the reason and the note) | The newest central-bank test (Bank of England Staff Working Paper 1,196, July 2026) found fan charts well understood by the public: rated second easiest (4.1 of 7, point forecasts 4.9) and about 50 points better than point forecasts on range-probability questions. It did not test scenario tables. So "beats a fan chart" is unproven. Table 2 is still right because its content is five named, conditional worlds by four outputs (a fan chart cannot hold that), and text avoids the deterministic construal error that sank the range chart (36% misread an interval despite a key; 94% correct in text, Joslyn and Savelli). The risk moves: single numbers per world read as certain (BoE: the public "mistake precision for certainty"). Add a set-apart spread row (585 windows, 1-in-20 low / median / 1-in-20 high, 8i) and a MODEL label. Rows: base world first, then the stresses; columns in time order with the payments column first. |
| 3. Grouping by role with subtotals reads faster | **CHANGE** | Grouping by type with subtotals is the professional and APA norm (a fund's own SEC schedule of investments; the California Lottery's annuity portfolio report; APA's sample tables; Wainer's "ALL is different and important"). But no source read measures "faster", and a pure role grouping cannot work: IBTM does two jobs (the 2033 payment and the floor; TNA, CANON A24) in one Wharton row of $97,489.95, 32.50% (8g). Use one subtotal row under the ten Treasuries ("for the ten payments and the floor", $268,652.18, 89.55%, 8g), set apart by a rule and a gap; no other groups. Cost about one single-spaced line, against about 1.5 for the specs' three spanners. |

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | An escrow verifier proves a bond book pays fixed debt service with a TABLE by payment date, not a chart: Date, purchase price, receipts from the securities, disbursements, cash released to the borrower, cash balance; a "Beginning Balance" row, a totals row, and a balance that ends at cents | Causey Demgen & Moore (2021a, 2021b), Exhibit A "Escrow Account Cash Flow" | PRESENTATION, CERTAINTY, LADDER, RESERVE2033 | NICHE | The professional form of "the reserve running down" is the balance column: it starts at the beginning balance and falls one payment at a time. Figure 1's question ("which holding pays each $50,000, and is it enough?") is the verifier's question | Written for an escrow agent and bond counsel, in eight-digit cents; a judge needs ten rows, not the full schedule | VERIFIED (both reports read in full on EMMA, P21483974, incl. Exhibits A, A-1, A-2, B, B-1) | risk: the escrow cash is "held uninvested"; CANON A15 says Laura's waiting money sits in a short-term Treasury ETF, never "cash at 0%". Borrow the test, not that wording | EMMA |
| 2 | The verifier's Exhibit A-1 is a matrix: each escrowed security a column, each payment date a row; each column stops at its maturity, so the cells form a staircase, with a "Total Cash Receipts" column | Causey Demgen & Moore (2021b), Exhibit A-1 | PRESENTATION, LADDER | NICHE | Figure 1's staircase (one bar per holding, each ending when its cash arrives) is this matrix drawn as a picture. That is the real professional pedigree of the current draft, not paired bars | The matrix holds many securities per date; Caplet's is strictly one holding per payment (CANON A12), so the picture is simpler | VERIFIED (as row 1) | no | EMMA |
| 3 | The verifier's standard and scope: the securities and cash are "sufficient, without reinvestment, to pay when due"; cash balances are assumed "not reinvested"; the verifier checks "mathematical accuracy" and gives "no opinion as to the attainability of the assumptions" | Causey Demgen & Moore (2021a, 2021b); escrow agreement s. 2(e) in the same file | CERTAINTY, REINVEST, PRESENTATION | NICHE | NUMBERS 8h already adopts the standard. Figure 1's note can split the same two things: the arithmetic (each payment covered if interest earns nothing) from the assumption (today's forward rates, MODEL) | A verifier signs; Keel's engine is unaudited. Say "modelled", never "verified" | VERIFIED (as row 1) | no | EMMA |
| 4 | A second real verification schedule names the gap directly: Date, Escrow Requirement, Net Escrow Receipts, Excess Receipts, Cash Balance; the excess stays within about a dollar either way and the balance about $1 | City of Renton (2010), Exhibit E "Escrow Fund Cash Flow", verified by Grant Thornton LLP | PRESENTATION, CERTAINTY, LADDER | NICHE | "Excess receipts" is the professional name for what Figure 1's "Above $50,000" column tried to show. Professionals print it as a signed number per date, not as a bar | A refunding escrow is sized to the cent; Caplet's own rungs are sized at forward rates, so the excess is $0 at forwards by design (row 5) | VERIFIED (EMMA EP728563 read in full: agreement, Exhibits D and E) | no | EMMA |
| 5 | Figure 1's third element is void: at forward rates every own holding pays exactly $50,000, $0 above, and the backstop covers nothing; if interest earns nothing the own holding pays $47,413 (2033) to $42,347 (2041) and the backstop covers $2,587 to $7,653, $54,595 in all; with the ETF's 0.15% fee too, $55,920 and nothing left | NUMBERS 8h ("Each payment in four rate worlds"); `exhibits/specs.md` Figure 1 Data row; SKELETON Exhibits item 2 | PRESENTATION, CERTAINTY, REINVEST, RESERVE2033 | NICHE | The informative number per payment is now the escrow split (own holding + backstop = $50,000 in the zero-interest world), not an excess at forwards | The fee world ends at exactly $0, the same shape as the verifier's zero end balance (row 1); the 0% world leaves $1,414 | VERIFIED (repo files read 10 Nov) | risk: specs.md still holds $1,705 to $5,266 ($36,859) and SKELETON item 2 still says "how much it pays above $50,000"; both pre-date 8h (NUMBERS 9 lists the rebuild) | Repo |
| 6 | The verifier's schedule releases what the payments do not need on day one ($135,951.59 released to the borrower) and keeps only what the schedule needs | Causey Demgen & Moore (2021b), Exhibit A "Cash Release to Borrower" column | RESERVE2033, LAURA | NICHE | The escrow release test in 8h (first release $8,813; $58,603 in all, the same $45,456 in 2033 money) has a real twin. A sentence for 3a, not a column in Figure 1 | The IPS is silent on releases; 8h calls this Keel's reading | VERIFIED (as row 1) | risk: the release is Keel's reading (8h), not an IPS commitment; keep it out of the exhibit | EMMA |
| 7 | A large manager draws a cash-flow-matched book as assets against the liability by year: "Assets (in red) versus total liability (in black)", the "Un-matched liability in yellow"; the portfolio "will roll down over time" | Costello & Shulman (2026), Illustrations 1 to 3 and text | PRESENTATION, LADDER, CERTAINTY | KNOWN | The useful borrowing is the unmatched part in its own tone, which is what the backstop fills | Images not rendered (proxy 403); form taken from captions. A 10.1-year, $8.0 billion pension liability has hundreds of flows; Laura has ten | VERIFIED (page text and captions read; images not seen) | no | Web, blackrock.com |
| 8 | Another manager's CDI chart: y-axis "Payments", x-axis "Year" 1 to 91, asset classes stacked and shaded under a black line of "Expected cash flow needs"; a later chart shows the % of liabilities paid by period | SEI (2022), Charts 1 and 4 | PRESENTATION, LADDER | KNOWN | The CDI form is stacked areas or bars under a liability line. It earns a chart at 91 years of flows; ten payments sit under Tufte's 20-number line (Q23 row 21), where a table or a labelled figure does better | Stacked layers are hard to read except the bottom one (row 10) | VERIFIED (text, axis labels and series names read) | no | Web, seic.com |
| 9 | A consultant's CDI note: a stylised chart of asset cash flows, contributions and liability cash flows over 0 to 50 years; "impossible to exactly predict cashflows"; long flows are hard to match "without relying on cashflows being reinvested"; prefer "pragmatic structures" | Barnett Waddingham (2021) | REINVEST, PRESENTATION | KNOWN | The reinvestment caveat is the reason Caplet's backstop exists (8a, 8h). "Pragmatic" supports one simple figure over an engineered one | Pension liabilities are uncertain; Laura's are ten fixed $50,000 payments | VERIFIED (PDF text read in full) | no | Web, barnett-waddingham |
| 10 | In divided bars and curve-difference charts the parts and gaps are judged as lengths, which people do badly; "If differences are to be conveyed, they should also be plotted on their own" | Cleveland & McGill (1984), s. 5.1 to 5.2 | PRESENTATION | TEXTBOOK | A stacked own-holding-plus-backstop bar would show the backstop as a sliver of 5% to 15% of a $50,000 bar, judged by length. Print the backstop as a number, or plot it on its own baseline | Their experiments are ratio judgements; a judge may simply read printed numbers | VERIFIED (paper read: theory, experiments, s. 5, conclusion) | no | Web, course copy of JASA PDF |
| 11 | Accuracy ranking of graphic encodings: position on a common scale, then nonaligned positions, length and angle, area, volume, and last shading and colour saturation | Cleveland & McGill (1984), s. 3 | PRESENTATION | TEXTBOOK | Figure 1's bar ends sit on one date axis (position, the best). Fan-chart bands encode probability by shading (the worst), one reason a fan chart was never right for exact dollar comparisons | Ranking is for decoding values, not for understanding a message; BoE (row 17) shows fans can still communicate the idea of uncertainty | VERIFIED (as row 10) | no | Web |
| 12 | iShares draws a ladder as stepped bars "Year 1" to "Year 5", rungs labelled by ticker; each fund holds bonds maturing "between January 1 and October or December 15" of its year; a "maturity transition period" (bonds mature into cash inside the fund), then "Cash", then an "End-date distribution" | iShares by BlackRock (2026), investor guide | LADDER, PRESENTATION | KNOWN | Label Figure 1's bars by ticker. For the five fund bars, a lighter last stretch can show cash inside the fund before the mid-December payout (8h; NUMBERS 3) | Images not rendered; the guide's ladder is a yield picture, not a liability match | VERIFIED (text and diagram labels read) | no | Web, ishares.com |
| 13 | The same guide: "The Funds do not seek to return any predetermined amount"; one use case is "Cash-flow matching for a house, tuition, or tax bill" | iShares by BlackRock (2026) | LADDER, CERTAINTY | KNOWN | No fund bar may carry a bare "$50,000": the amount depends on the world (8h), and the funds pay net asset value (NUMBERS 3) | None | VERIFIED (as row 12) | risk: a bare "$50,000" on a fund bar overstates (CANON B20, "the final payout is not fixed") | Web |
| 14 | A state lottery that funds fixed annuity prizes reports "Sufficiency of Cash Flow" in words only, a par roll-forward table, and a reserve fund of $2,492,362 "to mitigate credit and reinvestment risk"; no year-by-year sufficiency chart | California State Lottery (2023), Annual Investment Portfolio Report | RESERVE2033, CERTAINTY, REINVEST | NICHE | The closest real twin of Laura's fixed payments shows sufficiency in a sentence and a table, and keeps a separate reserve for reinvestment risk: the role of Caplet's backstop | A large pooled book; no per-prize matching shown | VERIFIED (report read in full) | no | Web, calottery.com |
| 15 | A regulator's cash-flow test fixes the order of its scenarios: level first; then +0.5 a year for 10 years; +1 a year for 5 years then back; +3 at once; then the same three falling (-0.5, -1, -3) | N.Y. Comp. Codes R. & Regs. tit. 11, s. 95.10(d) | PRESENTATION, REINVEST | KNOWN | Table 2's rows: the base world first, then stresses in a fixed, stated order. The rates-3-lower row (8i) is Regulation 126's scenario 7 in shape | An insurer's test runs many cash flows; Table 2 is five worlds for one reader | VERIFIED (section text read at Cornell LII) | no | Web |
| 16 | The Federal Reserve's stress-test tables show actual, projected and minimum by ratio, baseline before severely adverse, with scenarios called "not Federal Reserve forecasts" | Board of Governors of the Federal Reserve System (2026), stress test results | PRESENTATION | KNOWN | Supports "base first" and a plain MODEL, not-a-forecast label | Seen only in search excerpts | UNVERIFIED (search excerpts only) | no | Web search |
| 17 | The Bank of England's own test (300 public, 75 experts): the public rated point forecasts easiest (4.9 of 7) and fan charts second (4.1); fan charts raised correct answers on range probabilities by about 50 points over point forecasts and best conveyed expectation and uncertainty together | McMahon et al. (2026), Part I | PRESENTATION | KNOWN | Kills the stated reason in claim 2: lay readers do understand fan charts of one variable. Table 2 must win on other grounds (rows 19, 21) | One variable (inflation) over time; not a plan's several outputs | VERIFIED (working paper read: abstract, Part I, conclusion) | no | Web, bankofengland.co.uk |
| 18 | Same paper: shown point forecasts, about half the public perceived little uncertainty ("mistake precision for certainty"); dot plots also confused | McMahon et al. (2026) | PRESENTATION, COSPONSOR | KNOWN | Table 2's one number per world invites the same misreading. Remedy: a spread row and a MODEL label (rows 23, 25) | Inflation forecasts, not dollar outcomes | VERIFIED (as row 17) | no | Web |
| 19 | Same paper, footnote 1: "'Conditional' uncertainty communication, such as scenario analysis, is not explored"; the conclusion asks for scenario research and says the bar for abandoning a well-understood medium "should be high" | McMahon et al. (2026) | PRESENTATION | NICHE | No central-bank test compares scenario tables with fan charts. Table 2 is chosen for its structure (named conditional worlds by several outputs), not because fans fail | None | VERIFIED (as row 17) | no | Web |
| 20 | The Bernanke Review told the Bank to drop fan charts ("weak conceptual foundations ... little useful information ... They should be eliminated", rec. 11) and to publish alternative scenarios with the central forecast (rec. 8); the Bank agreed fan charts "have not proved to be an effective way of communicating" | Bernanke (2024), Bank of England Independent Evaluation Office page | PRESENTATION, COSPONSOR | KNOWN | Practitioners serving decision-makers moved from fans to named scenarios: the same move Caplet made. The evidence is split with row 17, so the report should not claim fans fail | A review of practice, not an experiment | VERIFIED (IEO page with recommendations and response read) | no | Web, bankofengland.co.uk |
| 21 | The deterministic construal error: 36% read an 80% forecast bracket's ends as the day's high and the night's low despite a prominent key; a text format cut the error to near zero (94% correct), "with no costs"; "it may help to separate uncertainty and other quantities" | Joslyn & Savelli (2021) | PRESENTATION | KNOWN | The failed range chart (Q23 row 31: bands read as outcomes) was this error. Table 2 in text avoids it, provided its two kinds of range look different (row 23) | Weather forecasts for lay users; judges are more numerate. Corrigendum (2022) fixed Figure 1B/F wording; not retracted | VERIFIED (full text read; corrigendum seen) | no | Web, frontiersin.org |
| 22 | Test a graphic by asking readers what it means before telling them it shows uncertainty | Joslyn & Savelli (2021), closing section | PROCESS, PRESENTATION | KNOWN | The Mon 23 Nov fresh-reader test: ask "what does this range mean?" of Table 2 and "what does this number mean?" of Figure 1's backstop column, before explaining | None | VERIFIED (as row 21) | no | Web |
| 23 | Table 2 holds two different ranges: the stated range (a rule-based promise, 8i: $95,000 to $115,000 at forwards) and the spread across 585 history windows (uncertainty: stated bottom $80,000 / $95,000 / $115,000 at 1-in-20 low / median / 1-in-20 high; top $95,000 / $115,000 / $140,000; half kept $13,874 / $23,601 / $42,015) | Joslyn & Savelli (2021); van der Bles et al. (2019), Box 5(a) "keep your expressions of the magnitude of uncertainty clearly separate"; NUMBERS 8i | COSPONSOR, FLOOR, CEILING, HALFKEPT, PRESENTATION | NICHE | Make them look different: the stated range sits in each world's row; the spread sits in its own row, set apart under a rule, with its three labels spelled out | Mixing them in one column would repeat the range chart's failure | VERIFIED (sources read; figures from 8i) | no | Web; repo |
| 24 | Ranges and intervals are misread as within-period variation; values inside an interval look equally likely; shading suits rough, not fine, comparison. Box 1: use multiple formats, words and numbers, "helpful narrative labels", assume low numeracy, acknowledge limits, test and iterate | Spiegelhalter et al. (2011) | PRESENTATION | TEXTBOOK | Name each Table 2 world in words; keep numbers in cells; put limits in the note; label Figure 1's long waits in words | Review of examples, not one experiment. No retraction or correction found (PubMed, journal page) | VERIFIED (full text read, Berkeley course copy) | no | Web |
| 25 | People read a bare numeric range in different ways (uniform, normal, U-shaped); a best estimate inside the range moves most towards the right reading | van der Bles et al. (2019), s. 6.1.2 | PRESENTATION, COSPONSOR | KNOWN | The spread row shows the median between the two 1-in-20 ends, not just two ends | The review covers uncertainty about facts and numbers now, not the future (its own stated limit). No retraction or correction found | VERIFIED (PMC full text read) | no | Web, PMC |
| 26 | A numeric range with a point estimate did not significantly lower trust in the number or the source; verbal uncertainty did; the word "estimated" alone did not even signal uncertainty | van der Bles et al. (2020) | PRESENTATION, COSPONSOR, FUNDRAISING | KNOWN | Table 2's note and cells use numbers, not "about" or "estimated"; the same holds for the co-sponsor wording in 3d | UK news readers and facts about the present (the paper's limits); n = 5,780. No retraction or correction found | VERIFIED (PMC full text read) | no | Web, PMC |
| 27 | Wainer's table rules: round a lot; order rows and columns in a way that makes sense (by size, or naturally, past to future); "ALL is different and important", summaries visually different and set apart; add space so clusters look clustered; a table is for communication, not storage | Wainer (1995), Rules I to IV; Wainer (2016) | PRESENTATION | TEXTBOOK | Table 2's columns in time order (2031 range, late-2032 contribution, 2033 kept); its base row as the standard for comparison; Table 1's one subtotal set apart, with a gap | Rules from practice; their 1979 empirical work is cited, not read | VERIFIED (ETS report: purposes, Rules I to IV, locator-table section; Significance article in full) | no | Web, ERIC; significancemagazine.com |
| 28 | Ehrenberg's rules: figures to compare go in columns; round to two effective digits; "columns of figures in single spacing with occasional deliberate gaps are easier to read than the popular double-spaced tables"; a brief verbal summary gives the reader a structure | Ehrenberg (1981) | PRESENTATION | TEXTBOOK | Supports Wharton's single-spacing allowance for all three exhibits, one deliberate gap per table, and a one-line lead before each exhibit in the prose (SKELETON 2.0) | None | VERIFIED (article read in full) | no | Web, course copy |
| 29 | A Treasury term fund's own SEC schedule groups holdings by type, each group's % on its heading line ("U.S. Government Obligations 99.5%", "Money Market Funds 0.1%"), a subtotal with cost under each group, then Total Investments 99.6%, Other Assets Less Liabilities 0.4%, Net Assets 100.0%; inside a group, rows run by coupon | iShares Trust (2022), schedule of investments, iBonds Dec 2026 Term Treasury ETF | PRESENTATION, LADDER | KNOWN | The professional holdings table groups by type with subtotals and ends on a 100% line. Wharton asks more (a % on every row); payment order beats coupon order for Laura | The SEC form shows % only per group | VERIFIED (sec.gov exhibit read in full) | no | Web, sec.gov |
| 30 | The lottery's Portfolio Summary groups holdings into Short-Term and Long-Term, each with Agency, Municipal and Treasury rows and a subtotal, then a Grand Total; columns Par, Cost, Fair Value, % | California State Lottery (2023) | PRESENTATION | KNOWN | A payment-funding portfolio reported to a lay commission uses groups and subtotals | Groups by term, not by role | VERIFIED (as row 14) | no | Web |
| 31 | APA tables: place entries to be compared next to each other; a border may separate "a row containing totals or other summary information"; spacing, never vertical rules; the sample tables group rows under category rows in the stub ("Gender", "Marital status"; "Factor 1: ..."); "use a canonical, or standard, format" | American Psychological Association (2021, 2024) | PRESENTATION | TEXTBOOK | One subtotal row with a rule above it is APA-native; nothing needs inventing | APA is a style, not evidence of reading speed | VERIFIED (both pages read in full) | no | Web, apastyle.apa.org |
| 32 | Tables suit look-up and precise values; a strength of tables is to "combine summary and detail information in a single display"; hierarchical relationships are "used routinely in tables to organize quantitative information" | Few (2012a, 2012b) | PRESENTATION | TEXTBOOK | Supports one subtotal in Table 1 as structure. No source read measures that a grouped list "reads faster" | Few's table-design chapter (ch. 8) was not read; only ch. 1 to 3 and the summary sheet | VERIFIED (summary sheet and Part 1, ch. 1 to 3, read); ch. 8 UNVERIFIED | no | Web, perceptualedge.com |
| 33 | IBTM does two jobs: the 2033 payment and the floor; in the WInS book it is one row, $97,489.95, 32.50% (8g). A role grouping cannot split one holding into two rows within Wharton's one row per holding | TNA l.13 ("IBTM does two jobs"); CANON A24, D2; NUMBERS 8g | FLOOR, LADDER, PRESENTATION | NICHE | The only role group that fits is the Treasuries "for the ten payments and the floor" ($268,652.18, 89.55%, 8g); the table note names IBTM's two jobs as the TNA does | None | VERIFIED (repo files read) | risk: a group named for the payments alone would contradict the submitted Trading Note on IBTM | Repo |
| 34 | Rounding Table 1 costs nothing: the 8g amounts rounded to whole dollars still sum to exactly $300,000, and the percentages to one decimal still sum to exactly 100.0 (own arithmetic on 8g, not a new figure); Wharton's own example row is in whole dollars and whole % | NUMBERS 8g; WHARTON_NORTH_STAR s. 0 example row | PRESENTATION | NICHE | Wainer and Ehrenberg's rounding (rows 27, 28) fits Wharton's totals exactly; it also narrows the amount column | specs.md keeps cents and two decimals; the register stays in cents either way | VERIFIED (own arithmetic, 10 Nov) | no | Repo |
| 35 | The May-2038 bond's waiting time is "7.6 months" in NUMBERS 8h and specs, "7.5 months" in the submitted trade note; CANON B35 rates 7.5 TRUE as rounding (231 days) | CANON A16, B35; NUMBERS 8h; specs.md Figure 1 Form row | LADDER, PRESENTATION | NICHE | Figure 1's label should read 7.5 months, so a judge who read the trade note sees the same number | 7.6 is the more exact figure; both are honest | VERIFIED (repo) | risk: "7.6 months" on Figure 1 beside "7.5 months" in the Trading Notes reads as a mismatch across deliverables judged together | Repo |

## (b) Cards

**Card 1. The escrow sufficiency schedule (rows 1 to 6).**
- What is it? When a municipality sets aside Treasuries to pay old bonds, an accountant verifies that the securities'
  receipts, date by date, cover each payment "without reinvestment". The proof is a table: requirement, receipts,
  excess, balance. A second exhibit lists each security's receipts down the dates and stops at its maturity, a staircase.
- Did it work? It is standard practice: the Aspire escrow agreement lets the escrow agent "conclusively rely" on the
  report for sufficiency. Two real reports read: Aspire 2021 (Causey Demgen & Moore) and Renton 2010 (Grant Thornton).
- How is Laura's case like it? Ten fixed $50,000 payments, one dated Treasury holding each, a standard that NUMBERS 8h
  already adopts.
- How is it not? The verifier signs and Keel's engine is a model; the escrow sits in cash or SLGS while Laura's waiting
  money sits in a short-term Treasury ETF (CANON A15); the funds pay net asset value, not a fixed sum.
- What Caplet takes: Figure 1 keeps its staircase and swaps "Above $50,000" for the escrow split in the zero-interest
  world: own holding pays, backstop covers, each row summing to $50,000; totals $445,405 and $54,595 (8h). The reserve's
  starting size ($444,545 against $399,089, 111.4% funded, 8h) is the verifier's "beginning balance": in the note or prose.

**Card 2. Two kinds of range must look different (rows 21 to 26).**
- What is it? People read uncertainty marks as if they were outcomes (the deterministic construal error), and a bare
  range is read many ways. Text avoids the first; a central value inside the range helps the second; numeric ranges do
  not cost trust, while words like "estimated" either cost trust or signal nothing.
- Did it work? In Joslyn's tests the text format brought correct reading to 94% with no loss of trust or decision
  quality. Van der Bles et al. (2020) ran five experiments (n = 5,780): numeric ranges did not significantly lower
  trust, and in experiment 3 neither did a range with a point estimate.
- How is Laura's case like it? Table 2 carries a promise range (what Laura announces, by rule) and an uncertainty range
  (the 1-in-20 spread across 585 windows). The failed range chart mixed the two.
- How is it not? Judges are more numerate than weather-app users; the studies used facts about the present or one-day
  forecasts, not a ten-year plan.
- What Caplet takes: Table 2 in text; the stated range in each world's row; one set-apart spread row with "1-in-20 low,
  median, 1-in-20 high" spelled out (8i); numbers, never "about" or "estimated"; the Mon 23 Nov test asks what each
  range means before explaining.

**Card 3. The central banks disagree about fan charts (rows 17 to 20).**
- What is it? The Bank of England's 2026 experiment found fan charts well understood by the public; the 2024 Bernanke
  Review told the Bank to drop them and publish named scenarios instead, and the Bank agreed.
- Did it work? Both are real: the experiment measured comprehension of one variable; the review judged usefulness to
  decision-makers. Neither tested a scenario table against a fan chart.
- How is Laura's case like it? Laura and her co-sponsors make decisions under named worlds (what if rates fall, what if
  a recession repeats); the review's audience is the closer match.
- How is it not? The BoE public sample is the closer match to a lay reader, and it liked fans.
- What Caplet takes: never claim that fan charts fail. Table 2 is right because five named worlds by four outputs is a
  table's job, and text avoids the error that sank the range chart. Keep the "MODEL, not a forecast" label.

**Card 4. How funds and style guides group a holdings list (rows 27 to 34).**
- What is it? A fund's SEC schedule groups holdings by type with a % on each group heading, subtotals, and a 100% line;
  the lottery report groups by term with subtotals; APA's samples group rows under category rows; Wainer says summaries
  are "different and important" and set apart; Ehrenberg says single spacing with deliberate gaps reads better.
- Did it work? It is universal practice; no source read measures reading speed.
- How is Laura's case like it? Thirteen holdings and a total; 89.55% in Treasuries is the number that tells a judge
  the promised money is in Treasuries (8g).
- How is it not? IBTM does two jobs (2033 payment and floor), so a pure role grouping would need two rows for one holding.
- What Caplet takes: one subtotal row under the ten Treasuries, named for the payments and the floor; no other groups;
  IBTM's two jobs in the note, as in the Trading Note.

**Card 5. Show differences as numbers, not slivers (rows 7 to 11).**
- What is it? CDI charts stack asset flows under a liability line; Cleveland and McGill showed that gaps between
  stacked layers or curves are judged as lengths, badly, and should be shown directly.
- Did it work? Their experiments: position judgements beat length judgements by factors of 1.4 to 2.5.
- How is Laura's case like it? The backstop's share of each payment is $2,587 to $7,653 of $50,000 (8h), a thin
  sliver on any stacked bar.
- How is it not? A judge reads printed numbers, so the perceptual cost matters less if the numbers are printed.
- What Caplet takes: the backstop amounts are printed as numbers in a right-hand column, not drawn as stacked segments.

## (c) Verdicts

**Claim 1: CHANGE.**
- "Paired bars by year" is not what professionals use (rows 1, 2, 4, 7, 8, 9, 12, 14). Four families were read:
  - escrow verifiers (two EMMA reports): tables, plus a staircase matrix;
  - CDI managers (three sources): stacked asset flows under a liability line;
  - iShares: stepped, ticker-labelled rungs;
  - an annuity payer and a regulator: words and tables, with scenarios in a fixed order.
- Figure 1 is not paired bars either. It is a holding-period staircase: the verifier's Exhibit A-1 drawn as a picture,
  close to the iShares ladder graphic. That pedigree holds, so keep the staircase.
- The third element fails on the numbers (row 5). Under NUMBERS 8h every own holding pays $50,000 at forwards, so an
  "above $50,000" column would print $0 ten times. The professional fix is the verifier's own test: what the
  security pays and what is still needed, under no reinvestment. In Caplet's terms that is own holding plus backstop
  equals $50,000 in the zero-interest world (8h).
- Print it as numbers, not a stacked bar (row 10).
- This also removes the open risk in specs (that "Above $50,000" reads as a bigger payment).

**Claim 2: CHANGE.**
- The stated reason is unproven (rows 17 to 20). The newest controlled test favours fan charts for one variable, and the
  only work on scenarios is a review's recommendation, not an experiment.
- The table stays, for three reasons:
  - **The content.** Five conditional worlds by four outputs: a fan chart shows one variable's spread over time, so
    named "what if" worlds cannot be drawn as one.
  - **Size.** It is a look-up of fewer than about 30 numbers (Q23 rows 21 and 22).
  - **The error it avoids.** Text avoids the deterministic construal error that failed the range chart (row 21).
- The risk the table carries is false precision (row 18), so the note and a spread row must carry the uncertainty
  (rows 23, 25, 26).
- **Row order.** Use base first, the professional convention (rows 15, 16). Then order the stresses by how far the
  stated range falls (Wainer's size order, row 27). The rates-up inflation world goes last, as its own kind (Regulation 126
  separates rising from falling).
- **Column order.** Payments first: the column that never changes, as specs already say. Then the rest in time order:
  2031, late 2032, 2033.

**Claim 3: CHANGE.**
- Grouping with a subtotal is the norm everywhere (rows 29 to 32). "Reads faster" is not measured in any source read,
  so the report and specs should not say it.
- Role grouping is limited by IBTM's two jobs (row 33). The workable form is one subtotal under the ten Treasuries.
  It costs about one single-spaced line, against about 1.5 for the specs' three spanners.
- No subtotal for groups of one or two rows. Wainer's summary rule is about adding information; a subtotal equal to
  its only row adds none.
- Rounding to whole dollars and one decimal keeps the totals exact (row 34). Whether to round is Caplet's call.

**Design notes, one per exhibit (each traced to rows).**

*Table 1, the holdings (Section 2).*
- **Form.** APA table with Wharton's five columns only. Single-spaced, one line per row (rows 28, 31).
- **Order.**
  - The ten Treasuries in payment order, 2033 to 2042, IBTM first: natural time order, not the SEC's coupon order
    (rows 27, 29).
  - Then VT, cash, the costs row, and Total.
- **Grouping.**
  - One subtotal row directly under the ten Treasuries: $268,652.18 and 89.55% (8g), named for the ten payments and
    the floor. A thin rule above it; one deliberate gap after it (rows 27, 28, 31, 33).
  - No spanner rows; no subtotal for VT or for cash and costs (row 27).
- **Labels.**
  - Tickers for the ETFs; WInS identifiers for the bonds from Caplet's export.
  - IBTM's row carries a note mark for its two jobs (row 33).
- **Numbers.** Whole dollars and one-decimal %, with exact totals $300,000 and 100.0% (row 34). Or keep cents and two
  decimals if Caplet prefers; the lead decides.
- **Note says:**
  - amounts at cost on the original $300,000;
  - what the costs row holds;
  - IBTM's two jobs.
- **Cut:**
  - the three-spanner option;
  - any "Pays for" column (already out);
  - any claim that grouping "reads faster" (row 32);
  - "[WInS ID]" placeholders before 27 Nov.

*Figure 1, the reserve running down (3a).*
- **Form.** Keep the staircase: ten rows, 2033 at the top, a bar per holding from January 2027 to its cash arrival,
  and a black tick at each 1 January (rows 2, 12).
  - Optional: a lighter last stretch on the five fund bars for cash inside the fund, kept only if it reads at print
    size (row 12).
- **Right-hand side.** Replace "Above $50,000" with two printed number columns in the escrow form, "own holding pays"
  and "backstop covers", for the world where interest earns nothing (rows 1, 4, 5, 10).
  - Each row sums to $50,000, from $47,413 + $2,587 (2033) to $42,624 + $7,376 (2042).
  - A totals line: $445,405 and $54,595 (8h).
- **Labels.**
  - Tickers and bond coupon-dates on the bars.
  - Waiting times in words: "10.5 months" and "7.5 months", the latter matching the trade note (row 35).
  - No bare "$50,000" on any fund bar (row 13).
- **Note says:**
  - MODEL on the 6 Nov curve's forwards;
  - at forwards each own holding pays $50,000 and the backstop is not touched;
  - the right columns are the escrow test "without reinvestment" (row 3);
  - with the ETF's 0.15% fee as well, nothing is left (8h);
  - waiting money sits in a short-term Treasury ETF (CANON A15);
  - the reserve's size on 1 Jan 2033 ($444,545 against $399,089, 111.4%, 8h), if prose does not carry it.
- **Title.** It should name the two facts the figure shows: one holding per payment, and the backstop's share if
  interest earns nothing.
- **Cut:**
  - "Above $50,000" and its $36,859 (row 5);
  - stacked own-plus-backstop bars (row 10);
  - the words "uninvested" or "cash at 0%" (row 1).

*Table 2, the plan under several markets (3b, 3c).*
- **Form.** APA table in text, single-spaced. No shading or bands (rows 11, 21).
- **Rows, in order (8i):**
  1. Today's forward rates: the base, set first as the standard for comparison (rows 15, 27).
  2. Joint replay from June 2006: $95,000 to $105,000.
  3. Rates 3 points lower for good: $80,000 to $95,000.
  4. Joint replay from July 2007: $80,000 to $95,000.
  5. The inflation world, last: it is the rates-up case, and its $120,000 is worth $89,546 in 2027 dollars (row 15).
  6. Under a rule, a summary row for all 585 windows: 1-in-20 low / median / 1-in-20 high for the stated bottom, the
     stated top and the half kept (rows 23, 25).
- **Columns, in time order (row 27):**
  1. Ten payments: "All paid" in every row (8i).
  2. Stated range (2031).
  3. Contribution (late 2032).
  4. Kept by Laura (2033).
  - Whether "Kept by Laura" means the half kept alone or the half kept plus the excess is for the lead to decide (both in 8i).
- **Numbers.** Rounded to $1,000, except the stated ends, which are already in $5,000 steps (rows 27, 28).
- **Note says:**
  - MODEL, not forecasts (rows 16, 18);
  - one clause per world on what moves, and its data (the 6 Nov curve; 1962-2010 Treasury yields and US stocks, 8i);
  - the stated range is Laura's rule-based announcement, while the summary row is the uncertainty (row 23);
  - the inflation row's 2027-dollar value;
  - shares at 7.5% a year in the first two rows.
  - Only assumptions that change a cell go in the note (row 24, "less is more"); the rest go to 3e prose.
- **Cut:**
  - "Funds pay", "Excess", "Left after 2042" and "Completion" columns (3a and 3b prose or Figure 1 carry them);
  - the words "about" and "estimated" (row 26);
  - any colour band (row 11).

## (d) Gaps

- **Fed stress test (row 16).** Seen in search excerpts only; it stays UNVERIFIED. Regulation 126 (row 15) carries
  the scenario-order point on its own.
- **Chart images.** BlackRock, SEI, Barnett Waddingham and iShares PDFs could not be rendered (proxy 403 on direct
  download). Each chart's geometry (stacked bars or areas, line style) is inferred from captions and labels.
- **Few's Show Me the Numbers, ch. 8 (Table Design).** Not read; only ch. 1 to 3 and the summary sheet. Few's
  specific rules on white space and grouping are UNVERIFIED here.
- **Wainer and Ehrenberg.** Wainer (1992, Educational Researcher) and Ehrenberg (1977, JRSS A) were not read. Their
  later papers stating the same rules were read instead (Wainer 1995 and 2016; Ehrenberg 1981).
- **Reading speed.** No experiment found compares grouped and flat holdings tables for speed or accuracy.
- **Retraction checks.** PubMed and the journal pages were checked for van der Bles et al. (2019, 2020) and
  Spiegelhalter et al. (2011): no notice found. Joslyn and Savelli (2021) has a corrigendum (2022) and no retraction.
  The Retraction Watch database itself was not queried.
- **REFERENCES_APA.** Row 114 (van der Bles et al., 2020) matches the PNAS page: entry correct. No other source here
  had an entry; the entries below are new and unconfirmed by the references pass.
- **Naming.** NUMBERS 8i calls the scenario table "Exhibit 3"; SKELETON and specs call it Table 2. Harmless, but the
  lead may align the register's wording.
- **SKELETON 3e.** It says all assumptions go in Table 2's note. This card recommends only those that change a cell;
  the lead decides.
- **Layout estimate.** Table 2's extra world row and summary row should add about two single-spaced lines to Q23's
  11.1-line measure. This is not measured; the template should re-measure.

## Sources (APA 7; all accessed 10 Nov 2026)

- American Psychological Association. (2021). *Table setup*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables
- American Psychological Association. (2024). *Sample tables*. APA Style. https://apastyle.apa.org/style-grammar-guidelines/tables-figures/sample-tables
- Barnett Waddingham. (2021, January). *Cashflow driven investment: If CDI is the solution, what is the question?* [Investment Insights]. https://bwd10barnettwaddingham-live-4d8d2562916-81f9e7d.divio-media.net/filer_public/44/ac/44ac5115-7854-4c07-acd1-03ebe4fea395/11012021_investment_insights_cdi_v1.pdf
- Bernanke, B. S. (2024). *Forecasting for monetary policy making and communication at the Bank of England: A review*. Bank of England, Independent Evaluation Office. https://www.bankofengland.co.uk/independent-evaluation-office/forecasting-for-monetary-policy-making-and-communication-at-the-bank-of-england-a-review/forecasting-for-monetary-policy-making-and-communication-at-the-bank-of-england-a-review
- California State Lottery. (2023). *Annual investment portfolio report* [Issue memo 8a, Attachment I, Commission meeting, September 2023]. https://static.www.calottery.com/-/media/project/calottery/pws/pdfs/commission-documents/september-2023/attachment-i-2023-investment-report.pdf
- Causey Demgen & Moore P.C. (2021a, April 28). *Verification report for the partial defeasance of the Charter School Revenue Refunding Bonds (Aspire Public Schools - Obligated Group), Series 2016* [Schedule to escrow agreement]. EMMA, Municipal Securities Rulemaking Board. https://emma.msrb.org/P21483974-P21150173-.pdf
- Causey Demgen & Moore P.C. (2021b, August 3). *Supplemental verification report* [Schedule to escrow agreement, same series]. EMMA, Municipal Securities Rulemaking Board. https://emma.msrb.org/P21483974-P21150173-.pdf
- City of Renton, Washington. (2010, May 11). *Escrow deposit agreement: Limited tax general obligation refunding bonds, 2010* [Exhibit E, escrow fund cash flow; verification by Grant Thornton LLP]. EMMA, Municipal Securities Rulemaking Board. https://emma.msrb.org/EP728563.pdf
- Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. *Journal of the American Statistical Association, 79*(387), 531-554. https://doi.org/10.1080/01621459.1984.10478080 (read at https://www.statsclass.org/dsci310/Notes/Cleveland_McGill_EPT.pdf)
- Costello, L., & Shulman, R. (2026, March). *Cashflow matching strategies*. BlackRock. https://www.blackrock.com/institutions/en-us/insights/thought-leadership/ldi-cashflow-matching-commentary
- Ehrenberg, A. S. C. (1981). The problem of numeracy. *The American Statistician, 35*(2), 67-71. (Read at https://sites.stat.washington.edu/pds/stat423/Documents/Ehrenberg.numeracy.pdf; DOI not checked.)
- Few, S. (2012a). *Designing effective tables and graphs* [Summary sheet]. Perceptual Edge. https://www.perceptualedge.com/images/Effective_Chart_Design.pdf
- Few, S. (2012b). *Show me the numbers: Designing tables and graphs to enlighten* (2nd ed., Part 1, ch. 1-3). Analytics Press. http://ad0bea668740b4435d61-b2537e77a07d94b1292a103d1f2d5dd9.r37.cf2.rackcdn.com/SMTN%20Part%201.pdf
- iShares by BlackRock. (2026). *iShares iBonds ETFs: Building better bond ladders* [Investor guide, iCRDSPMH1026U/S-6002735]. https://www.ishares.com/us/literature/brochure/ishares-ibonds-etfs-building-better-bond-ladders-investor-guide-en-us.pdf
- iShares Trust. (2022). *Schedule of investments (unaudited): iShares iBonds Dec 2026 Term Treasury ETF, July 31, 2022* [Form N-PORT exhibit]. U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/1100663/000175272422218363/NPORT_0BZH_55942602_0722.htm
- Joslyn, S., & Savelli, S. (2021). Visualizing uncertainty for non-expert end users: The challenge of the deterministic construal error. *Frontiers in Computer Science, 2*, Article 590232. https://doi.org/10.3389/fcomp.2020.590232 (corrigendum: https://doi.org/10.3389/fcomp.2022.1093379)
- McMahon, M., Naylor, M., Rholes, R., & Rickards, P. (2026). *Anchors aweigh? The effect of communicating forecast uncertainty* (Staff Working Paper No. 1,196). Bank of England. https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2026/anchors-aweigh-the-effect-of-communicating-forecast-uncertainty.pdf
- N.Y. Comp. Codes R. & Regs. tit. 11, § 95.10. https://www.law.cornell.edu/regulations/new-york/11-NYCRR-95.10
- SEI. (2022, March 31). *With cash flow driven investment, the details are important* (220366.05). https://www.seic.com/sites/default/files/2022-09/Cash%20flow%20driven%20investing_31.03.2022_0.pdf
- Spiegelhalter, D., Pearson, M., & Short, I. (2011). Visualizing uncertainty about the future. *Science, 333*(6048), 1393-1400. https://doi.org/10.1126/science.1191181 (read at https://www.stat.berkeley.edu/~aldous/157/Papers/spiegelhalter_visualizing.pdf)
- van der Bles, A. M., van der Linden, S., Freeman, A. L. J., Mitchell, J., Galvao, A. B., Zaval, L., & Spiegelhalter, D. J. (2019). Communicating uncertainty about facts, numbers and science. *Royal Society Open Science, 6*(5), Article 181870. https://doi.org/10.1098/rsos.181870 (read at https://pmc.ncbi.nlm.nih.gov/articles/PMC6549952/)
- van der Bles, A. M., van der Linden, S., Freeman, A. L. J., & Spiegelhalter, D. J. (2020). The effects of communicating uncertainty on public trust in facts and numbers. *Proceedings of the National Academy of Sciences, 117*(14), 7672–7683. https://doi.org/10.1073/pnas.1913678117 (REFERENCES_APA row 114; read at https://pmc.ncbi.nlm.nih.gov/articles/PMC7149229/)
- Wainer, H. (1995). *A study of display methods for NAEP results: I. Tables* (Program Statistics Research Technical Report No. 95-1; ETS RR-95-10). Educational Testing Service. https://files.eric.ed.gov/fulltext/ED387520.pdf
- Wainer, H. (2016, March 31). Extracting sunbeams from cucumbers: How to design a better table. *Significance*. https://significancemagazine.com/extracting-sunbeams-from-cucumbers
