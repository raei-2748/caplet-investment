# Q38 research card: a verified public identifier for every holding in Table 1

Fri 13 Nov 2026 Sydney (evening run). Report part: Section 2 (Portfolio Implementation), Table 1 (the holdings table
Wharton requires), its identifier column and its note.
Notes for the Final Report store, not report prose.

Checked against: Wharton's Final Report instructions (repo copy `competition/official/2026_27/2026_WGY_Final_Report_Instructions.txt`
l.80-102; `WHARTON_NORTH_STAR.md` section 0), `NUMBERS.md` 8g (the holdings table at cost and its "Identifiers"
bullet) and 8h (the cash-date table), `exhibits/tables.md` (Table 1 as built), `exhibits/exhibit_data.py` (`HOLDINGS`,
`ID_PRINT`), `exhibits/build_exhibits.py` (`add_table1` widths), `CANON.md` B17 and B18, the 23 Oct WInS snapshot
(`competition/wins/2026-10-23_snapshot.md`, a repo file; WInS itself was not opened), the team's order tickets
(`caplet/google_drive/sheets/portfolio_and_trading_notes/rb_tickets.csv`, which list a CUSIP for each bond), and cards
Q16 (rows 1, 6, 12), Q26 (row 18) and H8 row 80. The plan is frozen: nothing here changes a holding or a figure.

**Claims tested**
1. Keep, kill or change: "Table 1 can carry a verified public identifier for every holding without Caplet's WInS export."
2. Keep, kill or change: "The six ETFs are identified by their tickers, each confirmed on the sponsor's own page."
3. Keep, kill or change: "Each of the five Treasury bonds has a CUSIP that can be read, with its coupon and maturity
   date, at an official Treasury source, and those match NUMBERS 8g, 8h and Table 1."
4. Keep, kill or change: "Wharton's example number 532281 is a WInS number, not a CUSIP."
5. Keep, kill or change: "A CUSIP satisfies Wharton's 'ticker or identifier'."
6. Keep, kill or change (found on the way): "A CUSIP fits Table 1's identifier column as it is now laid out."

**Problem class and the field that solved it.** Securities reference data: naming each holding with a code that any
reader can look up and that points to exactly one security. The securities industry solved it with the CUSIP system
(nine characters that "uniquely identify a company or issuer and the type of financial instrument", run by CUSIP Global
Services; Investor.gov) and with the issuer as the source of record: for a Treasury, the Treasury's own offering
announcement and auction result; for a fund, its sponsor's fact sheet. Data managers call this taking the identifier
from the issuer, not from a trading screen.

## Verdicts in one screen

1. **KEEP.** Every one of the eleven holdings has a public identifier verified at its issuer today: six tickers at
   iShares and Vanguard, five CUSIPs at the U.S. Treasury (Fiscal Data's auctions dataset and TreasuryDirect's auction
   PDFs). Caplet's WInS export is no longer needed for Table 1.
2. **KEEP.** IBTM, IBTO, IBTP, IBTQ, IBTR and VT, each with its full name as NUMBERS 8g prints it (iShares adds the ®
   marks); fund CUSIPs 46436E296, 46436E148, 46438G646, 46438G422, 46438G158, 922042742 (not needed in the table).
3. **KEEP, no mismatch.** 4.750% 15 Feb 2037 = 912810PT9; 4.500% 15 May 2038 = 912810PX0; 4.375% 15 Nov 2039 =
   912810QD3; 4.250% 15 Nov 2040 = 912810QL5; 3.125% 15 Nov 2041 = 912810QT8. Coupon and maturity day agree with 8g,
   8h, Table 1 and the Figure 1 table; Treasury calls all five a "Bond", as Table 1's type column does; none is callable.
   The team's tickets and CANON B17 carry the same five CUSIPs.
4. **CHANGE.** From Wharton's text alone, 532281 is the value printed in the "Ticker" column for "T-Bond 4.500%
   15-May-2038" in a table marked "For illustrative purposes only". It is not a CUSIP: a CUSIP has nine characters, and
   this bond's is 912810PX0. Wharton never says it is a WInS number; that is an inference (8g already says "probably").
5. **KEEP.** Wharton asks for "ticker or identifier"; a CUSIP is the standard identifier for U.S. government bonds
   (Investor.gov). The example's own bond row shows Wharton expects a non-ticker identifier for a bond.
6. **CHANGE.** It does not fit as laid out: the CUSIPs measure 0.78 to 0.82 in at 12-pt Times metrics against the
   column's 0.67 in ("[532281]" is 0.61 in). The column needs about 0.88 in, about 0.21 in more, and the other columns
   hold about 0.15 in of slack. The layout options are in (c).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | IBTM: ticker IBTM, "iShares® iBonds® Dec 2032 Term Treasury ETF", CUSIP 46436E296, Nasdaq, launched 6 Jul 2022; the iBond funds "will terminate on or about October or December 15 of the year in each Fund's name" | S10 (fact sheet, data as of 30 Sep 2026); S15 (fund page, re-read) | PRESENTATION, LADDER | KNOWN | Table 1 prints IBTM; the fund is held to its end (on or about 15 Dec 2032, Q16 row 1) | The fund-specific date is in the summary prospectus (Q16 row 1, Q15 row 28), not the fact sheet | VERIFIED (fact sheet read in full; fund page by quote extraction) | no | iShares fact sheet PDF; iShares US fund page |
| 2 | IBTO: "iShares® iBonds® Dec 2033 Term Treasury ETF", CUSIP 46436E148, Nasdaq, launched 27 Jun 2023 | S11 | PRESENTATION, LADDER | KNOWN | Table 1 prints IBTO | The ticker was not in the extracted quote; it is in the file name and on the fund page (REFERENCES row 10) | VERIFIED (fact sheet, quote extraction from the full PDF) | no | iShares fact sheet PDF |
| 3 | IBTP: "iShares® iBonds® Dec 2034 Term Treasury ETF", CUSIP 46438G646, Nasdaq, launched 11 Jun 2024 | S12 | PRESENTATION, LADDER | KNOWN | Table 1 prints IBTP | The ticker was not in the extracted quote; it is in the file name and on the fund page (REFERENCES row 11) | VERIFIED (fact sheet, quote extraction) | no | iShares fact sheet PDF |
| 4 | IBTQ: ticker IBTQ, "iShares® iBonds® Dec 2035 Term Treasury ETF", CUSIP 46438G422, Nasdaq, launched 25 Mar 2025 | S13 | PRESENTATION, LADDER | KNOWN | Table 1 prints IBTQ | 15 Dec 2035 is a Saturday; 8h takes the end as Mon 17 Dec 2035 | VERIFIED (fact sheet, quote extraction) | no | iShares fact sheet PDF |
| 5 | IBTR: ticker IBTR, "iShares® iBonds® Dec 2036 Term Treasury ETF", CUSIP 46438G158, Nasdaq, launched 25 Mar 2026 | S14 | PRESENTATION, LADDER | KNOWN | Table 1 prints IBTR | none | VERIFIED (fact sheet, quote extraction) | no | iShares fact sheet PDF |
| 6 | VT: ticker VT, "Vanguard Total World Stock ETF", CUSIP 922042742, NYSE Arca, inception 24 Jun 2008, expense ratio 0.06% (as of 30 Sep 2026) | S16 (REFERENCES row 116, re-read) | PRESENTATION | KNOWN | Table 1 prints VT | none | VERIFIED (fact sheet, quote extraction) | no | Vanguard fact sheet F3141 |
| 7 | Bond for 2038: CUSIP 912810PT9, 4-3/4%, 30-year bond, issued 15 Feb 2007 (reopened 15 May 2007), matures 15 Feb 2037, not callable | S1 (query 1); S2; S8 | PRESENTATION, LADDER | KNOWN | Table 1 prints 912810PT9 | Matches CANON B17 and the tickets | VERIFIED (Fiscal Data record, auction result PDF and TreasuryDirect record read in full) | no (TNA l.5 "the 4.750% Treasury maturing 15 Feb 2037") | Fiscal Data API; TreasuryDirect |
| 8 | Bond for 2039: CUSIP 912810PX0, 4-1/2%, "29-Year 9-Month Bond" (Bonds of May 2038), issued 15 Aug 2008, dated 15 May 2008, matures 15 May 2038, reopened 17 Nov 2008 | S1; S3; S4 | PRESENTATION, LADDER | KNOWN | Table 1 prints 912810PX0 | This is Wharton's own example bond | VERIFIED (announcement and result PDFs read in full) | no | TreasuryDirect PDFs; Fiscal Data API |
| 9 | Bond for 2040: CUSIP 912810QD3, 4-3/8%, 30-year bond, issued Mon 16 Nov 2009 (dated 15 Nov 2009), matures 15 Nov 2039, reopened Dec 2009 and Jan 2010 | S1; S5 | PRESENTATION, LADDER | KNOWN | Table 1 prints 912810QD3 | none | VERIFIED (result PDF read in full) | no | TreasuryDirect PDF; Fiscal Data API |
| 10 | Bond for 2041: CUSIP 912810QL5, 4-1/4%, 30-year bond, issued 15 Nov 2010, matures 15 Nov 2040, reopened Dec 2010 and Jan 2011 | S1; S6 | PRESENTATION, LADDER | KNOWN | Table 1 prints 912810QL5 | none | VERIFIED (result PDF read in full) | no | TreasuryDirect PDF; Fiscal Data API |
| 11 | Bond for 2042: CUSIP 912810QT8, 3-1/8%, 30-year bond, issued 15 Nov 2011, matures 15 Nov 2041, reopened Dec 2011 and Jan 2012 | S1; S7 | PRESENTATION, LADDER | KNOWN | Table 1 prints 912810QT8 | none | VERIFIED (result PDF read in full) | no | TreasuryDirect PDF; Fiscal Data API |
| 12 | Coupon plus maturity day picks out one bond: on the five dates Treasury has auctioned seven bonds, and the two dates with twins differ by coupon (15 Nov 2040: 1.375%, 912810ST6, and 4.250%; 15 Nov 2041: 2.000%, 912810TC2, and 3.125%) | S1 (query 2: every original issue maturing on the five dates) | PRESENTATION, LADDER | NICHE | Backs 8g's "names the bonds by coupon and date, which identifies them uniquely": the coupon must stay in the name | H8 row 80 had 912810ST6 from a secondary source; it is now verified | VERIFIED (Fiscal Data query) | no | Fiscal Data API |
| 13 | 532281 is not a CUSIP (CUSIPs have nine characters; this bond's is 912810PX0). Wharton's text puts it in a "Ticker" column of a table "For illustrative purposes only" and says nothing about where it comes from | S17 l.80-102; S9; S1 | PRESENTATION | NICHE | Do not print 532281 unless Caplet sees it on its own WInS export | 8g and exhibit_data say "probably" the WInS id; SKELETON 1 says "Wharton's own example" | VERIFIED (Wharton text and Investor.gov read) | risk: printing 532281 unseen prints a number no one in the repo has read on Caplet's own portfolio | Repo copy of the instructions; Investor.gov |
| 14 | A CUSIP is an "identifier" in Wharton's sense: it "identifies most financial instruments, including ... U.S. government and municipal bonds" | S9; S17 | PRESENTATION | TEXTBOOK | One identifier type per asset type: tickers for funds, CUSIPs for bonds | Wharton's example uses tickers for ETFs, so the ETFs keep theirs | VERIFIED (Investor.gov page read) | no | Investor.gov |
| 15 | The May-2038 bond's official interest dates are 15 May and 15 Nov; it was first sold on 15 Aug 2008 with interest dated from 15 May 2008. That fits 8g v2's finding that WInS used a 15 Aug coupon date: WInS likely took the first sale date as a coupon date (inference) | S3 ("Interest Payment Dates: November 15 and May 15"); S4 | LADDER | NICHE | Explains the about $225 accrual gap behind 8g's costs row; store only, since no WInS accrued figure is quoted in the report | 8g v2 and Q17 row 32 (MODEL $1,338 standard accrual at 6 Oct) | VERIFIED (announcement read); the WInS cause is UNVERIFIED | no | TreasuryDirect PDF |
| 16 | All eleven identifiers pass the CUSIP check digit (computed by this worker, modulus-10 "double every second character" rule), so none was mistyped in the repo | Computed from rows 1-11 | PRESENTATION | KNOWN | A last typo check before 27 Nov | The check-digit rule itself was not read at a primary source | UNVERIFIED (rule from memory; the digits come from verified pages) | no | Worker calculation |
| 17 | The five maturities fall on Sun 15 Feb 2037, Sat 15 May 2038, Tue 15 Nov 2039, Thu 15 Nov 2040 and Fri 15 Nov 2041, as 8h's cash table has them | Calendar (computed); 8h; Q16 row 12 (next-business-day rule) | LADDER | KNOWN | Confirms 8h's dates and the "10.5" and "7.5 months" waits | none | VERIFIED (weekdays computed; holiday rule from Q16) | no (TNA's "10.5 months" and "7.5 months" agree, 8h) | Worker calculation |
| 18 | Treasury classes all five as "Bond" (four 30-year issues and one 29-year 9-month issue), never a note | S1 (security_type) | PRESENTATION | KNOWN | Table 1's one-word type "Bond" is Treasury's own word; Wharton's example says "Treasury Bond" | none | VERIFIED (Fiscal Data) | no | Fiscal Data API |
| 19 | None of the five can be called ("callable": "No" in both Treasury records) | S1; S8 | LADDER, CERTAINTY | KNOWN | Re-confirms Q26 row 18 | none | VERIFIED | no | Fiscal Data API; TreasuryDirect web service |
| 20 | A CUSIP needs about 0.21 in more than the identifier column's 0.67 in; the other six columns hold about 0.15 in of slack ("[532281]" 0.611 in; "912810QD3" 0.824 in; measured at 12 pt in Liberation Serif, which has Times New Roman's widths) | `build_exhibits.add_table1` widths and its comment; worker measurement | PRESENTATION | NICHE | The exhibit builder must widen column 1 before 27 Nov | Section 2 has 46 words of headroom (tables.md); a wrap in five rows costs about 2.5 double-spaced lines | VERIFIED (measured) | no | Worker measurement |

## (b) Cards

**Card 1. The five bond CUSIPs, read at the Treasury.**
- What is it? The nine-character code Treasury gives each marketable security, printed on its offering announcement and
  auction result and listed in Fiscal Data's auctions dataset: 912810PT9, 912810PX0, 912810QD3, 912810QL5, 912810QT8.
- Did it work? Yes. One Fiscal Data query returned all five with coupon, issue and maturity dates; the five original
  auction results agree line for line; all five match 8g, 8h, Table 1, CANON B17 and the team's tickets.
- How is Laura's case like it? Table 1 must name each holding so a judge can check it; a CUSIP is checkable by anyone
  at a government site.
- How is it not? The judges see WInS, which may label bonds with its own numbers, so a CUSIP will not match the screen
  character for character. The name column (coupon and date) bridges the two.
- What Caplet takes: Table 1's identifier column for rows 6 to 10 of the table (the five bonds); one note item and one
  References entry (S1). No prose.

**Card 2. What 532281 is, and is not.**
- What is it? The entry in Wharton's example "Ticker" column for "T-Bond 4.500% 15-May-2038", in a table "For
  illustrative purposes only. The holdings and allocations below are not intended to represent a recommended investment
  strategy."
- Did it work? As an example, yes: it shows a bond needs a non-ticker identifier. As a fact about Caplet's bond, it is
  unproven. Wharton never says what system issued it.
- How is Laura's case like it? It names the very bond Caplet holds for the 2039 payment, which is why 8g guessed it is
  the WInS number.
- How is it not? It is six digits; a CUSIP has nine characters (Investor.gov) and this bond's is 912810PX0. Printing
  532281 would make one bond the only row identified by a number from an example table.
- What Caplet takes: drop "[532281]" from Table 1 unless Caplet's export shows it; CANON-style note in the store only.

**Card 3. Coupon and date pick out one bond; the coupon must stay.**
- What is it? Every bond Treasury has auctioned maturing on Caplet's five dates: seven in all. Two dates carry twins
  that differ only by coupon (1.375% and 4.250% on 15 Nov 2040; 2.000% and 3.125% on 15 Nov 2041).
- Did it work? Yes: coupon plus maturity day is unique on all five dates, so 8g's "identifies them uniquely" holds.
- How is Laura's case like it? The team's order tickets already told the 3.125% from the 2.000% Nov-2041 ("Same date
  as the 2.000% Nov-2041: check the coupon").
- How is it not? Uniqueness here rests on auctioned issues only; Fiscal Data says "Treasury uses an auction process to
  sell marketable securities" (S1), so that covers the bonds a portfolio can hold.
- What Caplet takes: Table 1's names keep the coupon to three decimals, as Wharton's example does; store only.

**Card 4. The column must widen.**
- What is it? A measured fit test: the five CUSIPs print 0.78 to 0.82 in wide at 12 pt; the column is 0.67 in.
- Did it work? Not as laid out. The slack across the other columns is about 0.15 in; the CUSIP needs about 0.21 in.
- How is Laura's case like it? Section 2 has 46 words of headroom; a wrapped identifier or name in five bond rows adds
  about five single-spaced lines (about 2.5 double-spaced lines, roughly 30 words of prose).
- How is it not? Exhibit layout is the builder's call; nothing in the plan changes.
- What Caplet takes: options A to C in (c), for the exhibit builder before 27 Nov.

**Card 5. Why WInS charged less accrued interest on the May-2038 bond.**
- What is it? Treasury's offering announcement: interest dates 15 November and 15 May, dated date 15 May 2008, first
  sold 15 August 2008. WInS used 15 August as a coupon date (8g v2).
- Did it work? It explains the about $225 gap between WInS's charge and standard accrual (Q17 row 32, MODEL): WInS
  likely anchored on the first sale date. The cause inside WInS is an inference.
- How is Laura's case like it? It is a fact about the simulator, not about Laura's bond: the real bond pays on 15 May
  and 15 Nov, which is what Figure 1 and 8h assume.
- How is it not? It changes no figure the report quotes (8g: no WInS accrued figure is quoted).
- What Caplet takes: store only; a bond-desk answer if a judge asks about the costs row.

## (c) Verdicts

**Claim 1, KEEP.** All eleven identifiers are verified at their issuers (rows 1 to 11). The ask of Ray on Mon 9 Nov
(ASK_HUMANS l.42) is no longer on Table 1's critical path; the export would only add WInS's own bond numbers.

**Claim 2, KEEP.** The fund names in 8g match the sponsors' names apart from the ® marks, which a table may drop. The
iShares fact sheets say the iBond funds "will terminate on or about October or December 15 of the year in each Fund's
name" (IBTM, IBTP, IBTR as quoted; the extracted lines for IBTO and IBTQ read "December 15" and "Oct or Dec 15"); each
of Caplet's five has "Dec" in its name, and IBTM's prospectus gives "on or about December 15, 2032" (Q16 row 1). Say
each fund is held to its end, never "held to maturity" (WORDS).

**Claim 3, KEEP, no mismatch.** Each line checked:

| Holding (8g, Table 1) | Treasury: CUSIP | Coupon | First issued | Matures | 8g and Table 1 | 8h cash table |
|---|---|---|---|---|---|---|
| T-Bond 4.750% 15-Feb-2037 | 912810PT9 | 4-3/4% | 15 Feb 2007 | 15 Feb 2037 | match | Sun 15 Feb 2037, paid Tue 17 Feb: match |
| T-Bond 4.500% 15-May-2038 | 912810PX0 | 4-1/2% | 15 Aug 2008 (dated 15 May 2008) | 15 May 2038 | match | Sat 15 May 2038, paid Mon 17 May: match |
| T-Bond 4.375% 15-Nov-2039 | 912810QD3 | 4-3/8% | 16 Nov 2009 (dated 15 Nov 2009) | 15 Nov 2039 | match | Tue 15 Nov 2039: match |
| T-Bond 4.250% 15-Nov-2040 | 912810QL5 | 4-1/4% | 15 Nov 2010 | 15 Nov 2040 | match | Thu 15 Nov 2040: match |
| T-Bond 3.125% 15-Nov-2041 | 912810QT8 | 3-1/8% | 15 Nov 2011 | 15 Nov 2041 | match | Fri 15 Nov 2041: match |

**Claim 4, CHANGE.** Keep "not a CUSIP" (verified). Kill "is a WInS number" as a statement of fact: Wharton's text
does not say it, and no repo file shows a WInS bond number. It may be one; only Caplet's export can show it.

**Claim 5, KEEP.** "Ticker or identifier" is Wharton's wording; a CUSIP is the identifier the Treasury itself prints.

**Claim 6, CHANGE.** Measured fit (12 pt, Times New Roman widths):

| Text | Width |
|---|---|
| "[532281]" (now) | 0.611 in |
| 912810PT9 / PX0 / QD3 / QL5 / QT8 | 0.778 / 0.796 / 0.824 / 0.806 / 0.806 in |
| Column 1 now / needed | 0.67 in / about 0.88 in |

Options for the exhibit builder (Keel's, logged by the lead):
- A (recommended): widen column 1 to about 0.88 in, paid from the other columns' slack (units about 0.04, Pays for about
  0.03, name about 0.04, amount 0.02, others 0.02) plus rewording VT's units cell so no line is wider than "4,503 /
  4,503" (0.880 in, freeing about 0.05). Tight: re-measure in the built PDF.
- B: let the five bond names wrap to two lines (column 2 gives 0.21 in): about five more single-spaced lines, about 2.5
  double-spaced lines, roughly 30 of Section 2's 46 words of headroom.
- C: drop "T-Bond " from the five bond names (0.545 in), since the type column already says "Bond". Frees the most room
  but departs from Wharton's own example name ("T-Bond 4.500% 15-May-2038") and from 8g; not recommended.

**Decision note for the lead (Table 1, identifiers).**
- Default, whatever happens with the export: tickers for the six ETFs; CUSIPs for the five Treasury bonds, all five
  the same way; drop the square-bracket placeholders and "[532281]".
- If Caplet's export arrives and shows a WInS number for every bond, Caplet may switch all five at once; never a mix of
  WInS numbers and CUSIPs, and never 532281 alone. Keel's view: keep the CUSIPs even then, because any judge can check
  them at the Treasury and the names already match the WInS screen.
- Table 1's note gains one item (no new sentence of prose): identifiers are tickers for the funds and CUSIPs for the
  Treasury bonds, with the Treasury's dataset cited (S1). About 12 words; the note is budgeted at 75.
- `exhibit_data.py`: `ID_PRINT` maps the five bond rows to their CUSIPs; `HOLDINGS` rows 6 to 10 change their first
  field; 8g's "Identifiers" bullet and table change the same day (numbers owner); SKELETON item 1 and CASE_MAP E's
  "identifiers of four bonds come from Caplet's final export" become history.
- References page: one entry for the bonds (S1, the dataset) is enough; the five auction PDFs (S2 to S7) are backup if
  a reader wants each bond's own page. The fund tickers need no reference (Wharton's example cites none).

**APA 7 elements for each Treasury page (all retrieved 13 Nov 2026):**

| Page | Author | Date | Title (italic) | Description | Publisher | URL |
|---|---|---|---|---|---|---|
| Fiscal Data auctions dataset (S1) | Bureau of the Fiscal Service | 2026, November 9 (page: "Last Updated 11/09/2026") | Treasury securities auctions data | [Data set] | U.S. Department of the Treasury | https://fiscaldata.treasury.gov/datasets/treasury-securities-auctions-data/treasury-securities-auctions-data (with "Retrieved November 13, 2026, from", as the data are updated) |
| Feb-2037 auction result (S2) | Bureau of the Public Debt | 2007, February 8 | Results of Treasury's auction of 30-year bonds | [Press release] | U.S. Department of the Treasury | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2007/ofn0208071.pdf |
| May-2038 offering announcement (S3) | Bureau of the Public Debt | 2008b, July 30 | Treasury offering announcement | [Press release] | U.S. Department of the Treasury | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2008/A_20080730_2.pdf |
| May-2038 auction result (S4) | Bureau of the Public Debt | 2008a, August 7 | Treasury auction results | [Press release] | U.S. Department of the Treasury | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2008/R_20080807_1.pdf |
| Nov-2039 auction result (S5) | Bureau of the Public Debt | 2009, November 12 | Treasury auction results | [Press release] | U.S. Department of the Treasury | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2009/R_20091112_1.pdf |
| Nov-2040 auction result (S6) | Bureau of the Public Debt | 2010, November 10 | Treasury auction results | [Press release] | U.S. Department of the Treasury | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2010/R_20101110_2.pdf |
| Nov-2041 auction result (S7) | Bureau of the Public Debt | 2011, November 10 | Treasury auction results | [Press release] | U.S. Department of the Treasury | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2011/R_20111110_1.pdf |

2008a and 2008b follow APA's rule for one author's works in one year (ordered by title: "Treasury auction results"
before "Treasury offering announcement"). Wharton forbids links "to open", so the References page prints the URLs as
text, as the REFERENCES list already does.

## (d) Gaps

- WInS's own bond numbers: not seen (WInS not used). Whether 532281 is one stays open until Caplet's export.
- The fact sheets for IBTO, IBTP, IBTQ, IBTR and VT, and the IBTM fund page, were read by quote extraction from the full
  documents, not line by line; the IBTO and IBTP extracts did not include the ticker line, and the IBTO and IBTQ termination lines
  came back worded differently from IBTM's ("December 15", "Oct or Dec 15"). Not material: each fund's name carries its
  December end, and IBTM's prospectus was read in full by Q16.
- Author of the 2008 to 2011 Treasury PDFs: their text layer prints "PUBLIC DEBT NEWS" and "Office of Financing" but not
  the bureau's name, which the 2007 PDF prints ("Bureau of the Public Debt"). Check a page image before the References
  page is set; "Bureau of the Public Debt" is the likely author (it became part of the Fiscal Service in 2012; not
  verified here).
- The CUSIP check-digit rule (row 16) was applied from memory, not read at CUSIP Global Services; the CUSIPs themselves
  are verified at their issuers, so the check is only a typo guard.
- REFERENCES_APA: no error found in rows 9, 10 to 13 or 116 (re-read). Two notes for its keeper: the BlackRock (2026)
  fact sheets here (S10 to S14) need year suffixes that fit the list's existing BlackRock (2026) entry (row 140); and
  Q26's TreasuryDirect "Securities search" source (its S16) is not yet in the list (S8 here is the same service).
- H8 row 80 (store) still calls 912810ST6 a secondary-source CUSIP; Fiscal Data now verifies it (row 12). The store
  keeper may update it.
- Table width options (c) were measured with Liberation Serif metrics in Python, not in the built PDF.

## Sources (APA 7; all accessed 13 Nov 2026)

S1. Bureau of the Fiscal Service. (2026, November 9). *Treasury securities auctions data* [Data set]. U.S. Department
    of the Treasury. Retrieved November 13, 2026, from
    https://fiscaldata.treasury.gov/datasets/treasury-securities-auctions-data/treasury-securities-auctions-data
    (read through its API: query 1, the five CUSIPs, 13 records, https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query?fields=cusip,security_type,security_term,auction_date,announcemt_date,issue_date,maturity_date,int_rate,original_issue_date,reopening,callable,pdf_filenm_announcemt,pdf_filenm_comp_results&filter=cusip:in:(912810PT9,912810PX0,912810QD3,912810QL5,912810QT8);
    query 2, every original issue maturing on the five dates, 7 records, same endpoint with
    filter=maturity_date:in:(2037-02-15,2038-05-15,2039-11-15,2040-11-15,2041-11-15),reopening:eq:No). Read in full.
S2. Bureau of the Public Debt. (2007, February 8). *Results of Treasury's auction of 30-year bonds* [Press release].
    U.S. Department of the Treasury. https://www.treasurydirect.gov/instit/annceresult/press/preanre/2007/ofn0208071.pdf
    Read in full.
S3. Bureau of the Public Debt. (2008b, July 30). *Treasury offering announcement* [Press release]. U.S. Department of
    the Treasury. https://www.treasurydirect.gov/instit/annceresult/press/preanre/2008/A_20080730_2.pdf Read in full.
S4. Bureau of the Public Debt. (2008a, August 7). *Treasury auction results* [Press release]. U.S. Department of the
    Treasury. https://www.treasurydirect.gov/instit/annceresult/press/preanre/2008/R_20080807_1.pdf Read in full.
S5. Bureau of the Public Debt. (2009, November 12). *Treasury auction results* [Press release]. U.S. Department of the
    Treasury. https://www.treasurydirect.gov/instit/annceresult/press/preanre/2009/R_20091112_1.pdf Read in full.
S6. Bureau of the Public Debt. (2010, November 10). *Treasury auction results* [Press release]. U.S. Department of the
    Treasury. https://www.treasurydirect.gov/instit/annceresult/press/preanre/2010/R_20101110_2.pdf Read in full.
S7. Bureau of the Public Debt. (2011, November 10). *Treasury auction results* [Press release]. U.S. Department of the
    Treasury. https://www.treasurydirect.gov/instit/annceresult/press/preanre/2011/R_20111110_1.pdf Read in full.
S8. TreasuryDirect. (n.d.). *Securities search* [Web service; CUSIP 912810PT9]. U.S. Department of the Treasury.
    Retrieved November 13, 2026, from https://www.treasurydirect.gov/TA_WS/securities/search?cusip=912810PT9&format=json
    Read in full (two records: the February 2007 issue and the May 2007 reopening). Same service as Q26's S16.
S9. U.S. Securities and Exchange Commission. (n.d.). *CUSIP number*. Investor.gov. Retrieved November 13, 2026, from
    https://www.investor.gov/introduction-investing/investing-basics/glossary/cusip-number Read (short glossary entry).
S10. BlackRock. (2026a). *iShares iBonds Dec 2032 Term Treasury ETF* [Fact sheet, data as of September 30, 2026].
     iShares. https://www.ishares.com/us/literature/fact-sheet/ibtm-ishares-ibonds-dec-2032-term-treasury-etf-fund-fact-sheet-en-us.pdf
     Read in full.
S11. BlackRock. (2026b). *iShares iBonds Dec 2033 Term Treasury ETF* [Fact sheet, data as of September 30, 2026].
     iShares. https://www.ishares.com/us/literature/fact-sheet/ibto-ishares-ibonds-dec-2033-term-treasury-etf-fund-fact-sheet-en-us.pdf
     Quote extraction from the full PDF.
S12. BlackRock. (2026c). *iShares iBonds Dec 2034 Term Treasury ETF* [Fact sheet, data as of September 30, 2026].
     iShares. https://www.ishares.com/us/literature/fact-sheet/ibtp-ishares-ibonds-dec-2034-term-treasury-etf-fund-fact-sheet-en-us.pdf
     Quote extraction from the full PDF.
S13. BlackRock. (2026d). *iShares iBonds Dec 2035 Term Treasury ETF* [Fact sheet, data as of September 30, 2026].
     iShares. https://www.ishares.com/us/literature/fact-sheet/ibtq-ishares-ibonds-dec-2035-term-treasury-etf-fund-fact-sheet-en-us.pdf
     Quote extraction from the full PDF.
S14. BlackRock. (2026e). *iShares iBonds Dec 2036 Term Treasury ETF* [Fact sheet, data as of September 30, 2026].
     iShares. https://www.ishares.com/us/literature/fact-sheet/ibtr-ishares-ibonds-dec-2036-term-treasury-etf-fund-fact-sheet-en-us.pdf
     Quote extraction from the full PDF.
S15. BlackRock. (n.d.-b). *iShares iBonds Dec 2032 Term Treasury ETF (IBTM)* [Fund page]. iShares. Retrieved November
     13, 2026, from https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (REFERENCES
     row 9; re-read by quote extraction: name, CUSIP 46436E296, Nasdaq, inception 6 Jul 2022).
S16. Vanguard. (2026b). *Vanguard Total World Stock ETF* [Fact sheet] (F3141). https://fund-docs.vanguard.com/F3141.pdf?product-type=ETF
     (REFERENCES row 116; re-read by quote extraction: ticker VT, CUSIP 922042742, NYSE Arca, as of 30 Sep 2026).
S17. Wharton Global Youth Program. (2026b). [Final Report instructions, 2026–2027 Wharton Global High School Investment
     Competition]. Unpublished document distributed to registered teams. (REFERENCES row 121; repo copy
     `competition/official/2026_27/2026_WGY_Final_Report_Instructions.txt` l.76-102, read in full.)

## Correction and Keel's call (Fri 13 Nov 2026, evening, lead)

- **The WInS record does carry its own bond identifiers.** The frozen Trading Notes file
  (`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`, l.16-18, l.23-24, l.38-40) names
  each bond by its WInS symbol: B-T-4.750-15022037, B-T-4.500-15052038, B-T-4.375-15112039, B-T-4.250-15112040 and
  B-T-3.125-15112041 (type, coupon, maturity as DDMMYYYY). Rows 13 and 14 above said Wharton's 532281 has no stated
  source; that stands, but the claim that only a WInS export could supply a WInS identifier is wrong: the symbols are
  already in a submitted document.
- **Keel's call:** Table 1's identifier column keeps the CUSIPs (public, checkable at Treasury, nine characters, all
  passing the check digit, row 16). The WInS symbols are the Trading Notes' own names, so Table 1's note may say once
  that WInS lists the bonds as B-T-coupon-maturity, as the Trading Notes quote them, if the 75-word note has room on
  27 Nov. Ray's Portfolio Summary export (asked 9 Nov) is no longer needed for Table 1.
- Logged in `keel/pm/ASK_HUMANS.md` (Fri 13 Nov evening).
