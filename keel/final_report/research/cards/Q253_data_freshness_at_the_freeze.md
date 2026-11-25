# Q253. At the freeze, has any outside figure the report prints gone stale or changed since card Q146 (Wed 18 Nov)?

- **Date:** Wed 25 Nov 2026, Sydney, evening. Every source was read Wed 25 Nov 2026, Sydney, which is 24 Nov in New York. US pages carry data to the 23 or 24 Nov close.
- **Report parts:**
  - 3e area (1): J.P. Morgan's 7.5% among published forecasts, and Table 2's note.
  - 2.2, 2.3 and Table 1: facts on IBTM-IBTR and VT.
  - 3e and Table 3:
    - the US debt limit, against the Treasury-default reason (IPS l.17; Table 3 row 2);
    - the fund-notices row;
    - the building-cost date;
    - the Taiwan dollar watch.
  - 3c: the 6 Nov curve's date, as a register note only.
- Notes for the Final Report store, not report prose.
  - Plan figures come only from `NUMBERS.md`. Every other figure is a source's own, or Keel arithmetic on it, labelled as such.
  - The register stays on the 6 Nov 2026 curve by rule (NUMBERS section 0). Nothing here re-sizes it.
- **Not repeated:**
  - Card Q146 (18 Nov freshness check) and card Q117 (17 Nov). This card updates them and does not restate them.
  - Card Q6b (the panel of houses). Card Q30 rows 21-28 and store rows Q15-026 and Q58-035 (the debt limit). Card Q103 (October building-cost index).
  - Store greps (`store/insights.jsonl`, Wed 25 Nov evening):
    - "BMO": 0
    - "GMO": 20 (all the 30 Sep or earlier forecasts)
    - "debt limit": 17
    - "X date" or "X-date": 37
- **Claims tested (each to keep, kill or change):**
  1. "J.P. Morgan's 7.5% is still above the middle of published forecasts."
  2. "No iBond fund Laura holds has a notice of early end, merger or fee change, and every fee is still 0.07%."
  3. "VT's fee is still 0.06%, and its holdings count and date still match CANON B12-B14."
  4. "NUMBERS 8d's October 2026 Taiwan building-cost index is still the latest. Taiwan's CPI and the Taiwan dollar need no working file changed."
  5. "Nothing new on the US debt limit, or on a delayed Treasury payment, bears on the plan's Treasury-default reason (any Treasury payment more than five business days late)."
- **Problem class:** keeping a set of dated figures honest at a freeze while the sources keep publishing.
  - The sorting rule is auditing's (card Q117 rows 26-28, not repeated). A fact that already existed on the date, such as a missed house's forecast, corrects a count or a wording. A new reading is disclosed beside the dated figure and never booked in its place.
  - New here: the official source can itself revise a dated figure after the report is in (row 27).

## Changes (anything that changes a register, CANON, SKELETON or card wording)

No NUMBERS figure changes, and no CANON line is wrong. Four dated facts outside NUMBERS change.

1. **The debt-limit dates have moved earlier** (card Q30 rows 21-28; store Q15-026, Q58-035). The plan's rule is unchanged.
   - When the limit binds:
     - Then: "between late winter and mid-summer of 2027" (BPC, June); May 2027 in NTU's August central case.
     - Now: "February or March 2027" (BPC, 18 Nov); February 2027 (NTU, 12 Nov).
   - The X-date:
     - Then: about August 2027 to May 2028, with NTU's central case February 2028.
     - Now: about August to December 2027. That is Keel arithmetic on BPC's "roughly six to nine months". NTU gives "by the beginning of December 2027", with scenarios from November 2027 to February 2028.
   - BPC itself says the X-date range "has not yet come into focus". Any report line that dates the risk says "2027", never "early 2028".
   - What counts under Table 3 row 2 is still a Treasury payment more than five business days late, never the X-date itself (rows 30-36).
2. **The forecast panel gains a house, and its bottom house updates.**
   - BMO Wealth Management's 2027 edition is new to the panel: 6.2% a year for global shares over 10 years (data to 30 Jun 2026, PDF dated about 13 Nov 2026). This forecast existed before Q146's count, so it corrects the count and not a wording.
   - GMO's 31 Oct forecast was published 19 Nov. Its world blend is about -2.1% nominal (it was -2.5%; Keel arithmetic).
   - With eighteen houses the median is about 6.7 (Keel arithmetic). It is 6.5 with fifteen houses and 6.9 with seventeen. "Above the middle of published forecasts" holds in every count.
   - The report still prints no median figure, and never calls 7.5% "the top" or "the consensus" (rows 1-11).
3. **The release date for November's building-cost index and CPI is now verified at the official source:** 8 Dec 2026, 16:00 Taipei, which is 19:00 Sydney.
   - Q146 marked "7-8 Dec" UNVERIFIED. It is one date, and it falls after the report is due (Sat 5 Dec 09:00 Sydney).
   - So October 2026's 120.50 (+7.18%) is the last index the report can print. NUMBERS 8d's "about 8 Dec" is exact.
   - The platform also warns that the latest three months may be revised. Print the index as "October 2026, as first published" (rows 24-27).
4. **Dated readings to disclose beside the register, never in place of it:**

   | Reading | Was | Now |
   |---|---|---|
   | IBTM net assets | $641.4m (17 Nov) | $623.3m (24 Nov) |
   | IBTR premium | 0.16% (16 Nov) | 0.01% (23 Nov) |
   | VT 30-day spread | 0.01% | 0.02% (23 Nov) |
   | 10-year Treasury yield | 5.10 (17 Nov) | 4.91 (24 Nov close); 4.86 on 6 Nov |
   | NT$ per US dollar | | 32.939 (24 Nov); 32.768 on 6 Nov |

   Debt-limit headroom: $575.6bn on 23 Nov (Keel arithmetic).

**Unchanged** (each read at source today):
- the 0.07% fee of all five iBond funds;
- VT's 0.06% fee and its 10,158 stocks at 31 Oct;
- J.P. Morgan's 7.5%;
- Taiwan's October CPI (+2.33%) and October building-cost index (120.50);
- CANON B38 (no Treasury iBond fund ends in 2037-43).

## Verdicts in one screen

1. **"J.P. Morgan's 7.5% is above the middle": KEEP.**
   - J.P. Morgan's release still reads "Global equities are projected to return 7.5% (USD), increasing from 7.0%" (19 Oct 2026, no revision).
   - Two new readings:
     - GMO's 31 Oct forecast, published 19 Nov: US large shares -6.8% a year after inflation, international large -1.2%, emerging 1.9%. Its blend is about -2.1% nominal (Keel arithmetic). It is still the bottom house.
     - BMO's 2027 edition, a missed house: "6.9% in the U.S. and 6.2% globally".
   - Eighteen houses give a median of about 6.7 (Keel arithmetic). Six are above J.P. Morgan, one level with it, and ten below.
   - Nothing else published since 16 Nov is a long-term forecast. UBS, Morgan Stanley and Goldman put out one-year targets. Northern Trust's 2027 edition is likely in December; whatever it prints, the median stays between about 6.45 and 7.0 (Keel arithmetic, row 11).
   - Judge's note: a judge who knows another house's lower forecast cannot catch the report out. The wording survives every count, and a printed median would not.
2. **"No fund notice; every fee is 0.07%": KEEP.**
   - All five fund pages (IBTM, IBTO, IBTP, IBTQ, IBTR) show 0.07% "as of current prospectus" and no notice.
   - The closures page has no Treasury iBond closure since Q146.
   - None of iShares Trust's EDGAR filings from 17 to 24 Nov concerns these funds.
   - No new Treasury iBond fund ending 2037-43 has been filed, so CANON B38 stands.
   - IBTR's premium is back to 0.01%.
3. **"VT 0.06%, 10,158 at 31 Oct": KEEP.**
   - The fee is 0.06% (as of 27 Feb 2026). The holdings count is 10,158 at 31 Oct 2026, against an index of 10,207. The fact sheet is still the 30 Sep edition (10,185).
   - World shares fell about 5.1% in November to the 24th (Keel arithmetic on VT's year-to-date return). That is context only.
4. **"October's index is the latest; CPI and NT$ need no change": KEEP, with the release date upgraded to VERIFIED.**
   - November's index and CPI are due 8 Dec, 16:00 Taipei. That is after the report is due.
   - NT$32.939 per US dollar on 24 Nov is 0.52% weaker than 6 Nov's 32.768 (Keel arithmetic). That is context only.
   - Judge's note: the building-cost index the report prints can be revised by its own publisher after the report is in. "As first published" is the honest date, the same way the range is dated to a curve.
5. **"Nothing new on the debt limit bears on the reason": CHANGE the dates; KEEP the rule.**
   - Both counters now put the limit in February or March 2027. BPC's six to nine months puts the X-date about August to December 2027.
   - Headroom is $575.6bn on 23 Nov, down from $739.8bn on 9 Nov (Keel arithmetic).
   - No source reports a late Treasury payment.
   - Judge's note: the deadline people watch is the X-date. The event the plan watches is a payment more than five business days late. The window now falls in the plan's first year, while the ten are held and before the 2028 deposit is invested. The rule needs no change, because it counts payments, not deadlines.
6. **Register note: the curve.** The 24 Nov close is 1y 4.59, 2y 4.63, 3y 4.67, 5y 4.69, 7y 4.79, 10y 4.91, 20y 5.33, 30y 5.30.
   - That is 0.04 to 0.26 points above 6 Nov and 0.01 to 0.21 below 17 Nov (Keel arithmetic).
   - The report stays on 6 Nov and is never re-sized.

## Rows for the store

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | J.P. Morgan's 2027 release (19 Oct 2026) still reads "Global equities are projected to return 7.5% (USD), increasing from 7.0%", with no revision note | J.P. Morgan Asset Management (2026) | CEILING, OTHER | KNOWN | Table 2's note keeps "J.P. Morgan's 7.5%" with its date | The fetch served a copy taken 7 Nov, so it proves "unchanged since 7 Nov"; a 20 Nov J.P. Morgan Personal Investing article restates the themes with no new figure | VERIFIED (read at source, 25 Nov 2026; cached 7 Nov copy) | None (TNA note 3 uses J.P. Morgan's 7.5%) | This run: am.jpmorgan.com press release |
| 2 | GMO's 7-year forecast as of 31 Oct 2026 (published 19 Nov) puts US large shares at -6.8% a year after inflation in its "normal" rate case (was -7.3 at 30 Sep) | GMO (2026) | CEILING, OTHER | KNOWN | The panel's bottom house still expects US shares to lose money after inflation for seven years; Laura's shares carry no promise, so such a forecast only lowers a top not yet stated | GMO prints real 7-year figures; J.P. Morgan prints nominal 10-15 year figures; Q6b converts before comparing | VERIFIED (read at source, 25 Nov 2026) | None | This run: gmo.com PDF |
| 3 | GMO's world blend on Q6b's 62/28/10 weights (US large -6.8, international large -1.2, emerging 1.9) is about -4.4% real, about -2.1% nominal at 2.4% inflation (Keel arithmetic); it was about -2.5 | GMO (2026); card Q6b row 20 | CEILING | NICHE | GMO stays the panel's lowest house; the median does not move | GMO publishes no world figure; the blend and its weights are Keel's (Q6b) | VERIFIED (inputs read at source, 25 Nov 2026; blend Keel arithmetic) | None | This run: gmo.com PDF |
| 4 | GMO prints two cases, "normal" (1.3% equilibrium real cash rate) and "low" (0.0%), and US large shares are -3.8 in the low case; a panel must say which case it uses | GMO (2026) | CEILING, PRESENTATION | NICHE | A forecast is a figure plus its assumption, as Laura's range is a figure plus its date | Q6b used the normal case; keep it so the panel is consistent | VERIFIED (read at source, 25 Nov 2026) | None | This run: gmo.com PDF |
| 5 | BMO Wealth Management's Capital Market Assumptions 2027 edition (data 30 Jun 2026, PDF dated about 13 Nov 2026): "we forecast equity total returns (annualized) to be 6.9% in the U.S. and 6.2% globally" over 10 years | Phillips, Schleif & Karthik (2026) | CEILING, OTHER | KNOWN | A house missing from every earlier count, below J.P. Morgan | The text read names no global index (its Exhibit 8 uses MSCI World) and no currency (a US wealth brand, so likely US dollars: UNVERIFIED); inflation (2.5%) is shown separately, so the figure is nominal | VERIFIED (read at source, 25 Nov 2026; currency UNVERIFIED) | None | This run: bmo.com PDF |
| 6 | BMO's parts: international developed 4.9%, emerging 5.9%, global 6.2% against 12.8% over the last ten years, because "a modest mean reversion of elevated valuations suggests annualized total returns in the mid-single digits" | Phillips et al. (2026) | CEILING | KNOWN | Another house reads the same high valuations and lands below J.P. Morgan | None new | VERIFIED (read at source, 25 Nov 2026) | None | This run: bmo.com PDF |
| 7 | Eighteen houses with BMO and GMO's October figure: median about 6.7 (Keel arithmetic); six above J.P. Morgan (Fidelity International 7.6, Goldman Sachs 7.7, BNY 7.7, HSBC 7.8, Robeco 7.85, BlackRock 9.0), Aon level, ten below | Card Q146 panel; GMO (2026); Phillips et al. (2026) | CEILING, PRESENTATION | NICHE | "Above the middle of published forecasts" holds at 15 (6.5), 17 (6.9) and 18 (6.7) houses: the wording survives every count, a printed median would not | The median moves with the panel (Q146 Changes 1); no median figure goes in the report | VERIFIED (inputs read at source, 25 Nov 2026; median Keel arithmetic) | None | This run: Keel arithmetic |
| 8 | BMO existed before the 18 Nov count, so it corrects the count; GMO's October figure is a new reading, shown beside the 30 Sep one, never booked in its place | Card Q117 rows 26-28 (the sorting rule) | PROCESS, PRESENTATION | NICHE | The same rule keeps the range on the 6 Nov curve | None | VERIFIED (dates read at source, 25 Nov 2026) | None | This run: Keel analysis |
| 9 | Year-ahead outlooks of 18-19 Nov are one-year targets, never members of a 7-plus-year panel: UBS has MSCI AC World 1,335 now, 1,460 by Dec 2027; Goldman Sachs "an S&P 500 total return of 18% through the end of 2027"; Morgan Stanley's 2027 outlook | UBS (2026); Goldman Sachs (2026); Morgan Stanley (2026) | CEILING, PRESENTATION | KNOWN | Keeps the panel to long-horizon figures like the 7.5% | One-year targets swing with the mood of the month; mixing them in would move the median by fashion | VERIFIED for UBS and Goldman (read at source, 25 Nov 2026); UNVERIFIED for Morgan Stanley (search excerpt only) | None | This run: ubs.com PDF, goldmansachs.com, morganstanley.com |
| 10 | No other house's long-term figure is new since 16 Nov: Northern Trust 2026 edition (released Dec 2025); Schwab "Last updated September 30, 2026"; Invesco APAC Q2 2026; Amundi 21 Apr 2026; Vanguard's model page (30 Sep run); BlackRock dated 16 Nov but data to 30 Sep, figures in charts and a spreadsheet only; PGIM and Fidelity International as Q146; EFG 2027 (9 Nov) global figure in a chart only; American Century 3-5 years | House pages (see Sources) | CEILING | KNOWN | The panel is as fresh as it can be at the freeze | AQR, Research Affiliates after 31 Oct and Morgan Stanley's long-term assumptions not found (Gaps) | VERIFIED (read at source, 25 Nov 2026) | None | This run: house pages |
| 11 | Northern Trust's 2027 edition will replace its 6.9 and may land before 4 Dec (New York); whatever it prints, the median of eighteen stays between about 6.45 and 7.0, below 7.5 (Keel arithmetic) | Northern Trust (2025); row 7 | CEILING, PROCESS | NICHE | Table 2's note needs no rewrite whatever one new edition says | Only one house was tested; two or more high editions together were not | UNVERIFIED (the 2027 edition's date is not announced) | None | This run: northerntrust.com; Keel arithmetic |
| 12 | All five of Laura's Treasury iBond funds (IBTM, IBTO, IBTP, IBTQ, IBTR) still show a 0.07% expense ratio and management fee "as of current prospectus" | BlackRock (2026a-e) | LADDER, FLOOR | KNOWN | NUMBERS 0's 0.07% fee stands for Table 1 and the range rule | None | VERIFIED (read at source, 25 Nov 2026) | None | This run: blackrock.com fund pages |
| 13 | No fund page carries a notice of early end, merger, fee change or index change; each shows only its standard end-of-life disclosure | BlackRock (2026a-e) | LADDER, TWOREASONS | KNOWN | Table 3's fund-notices row reads "none" at the freeze | The watch is September-October of each end year (IBTA ended 15 days early), never "ended on schedule" | VERIFIED (read at source, 25 Nov 2026) | None | This run: blackrock.com |
| 14 | IBTM had net assets of $623.3m on 24 Nov (was $641.4m on 17 Nov, -2.8%, Keel arithmetic); 15 holdings; NAV $22.14; spread 0.05%; premium -0.02% (23 Nov); yield to maturity 4.77%; duration 4.93 years | BlackRock (2026a) | FLOOR, COMPLETE2028 | KNOWN | Context for 2.2: the floor's fund is about $620m and trades at its value | Fund size moves with flows; nothing in the plan rests on it | VERIFIED (read at source, 25 Nov 2026) | None | This run: blackrock.com IBTM page |
| 15 | The other four funds on 24 Nov: IBTO $519.7m (13 holdings), IBTP $383.1m (4), IBTQ $308.1m (4), IBTR $118.0m (4); spreads 0.04%; premiums -0.01% to 0.02% (23 Nov) | BlackRock (2026b-e) | LADDER | KNOWN | Table 1 context, dated | IBTR is still the smallest | VERIFIED (read at source, 25 Nov 2026) | None | This run: blackrock.com |
| 16 | IBTR's premium was back to 0.01% on 23 Nov from 0.16% on 16 Nov: Q146 row 29's gap passed, and a limit order within 0.5% of net asset value (Table 3 row 5) handles both days | BlackRock (2026e); card Q146 row 29 | LADDER, PROCESS | NICHE | Shows why the plan trades at the fund's value, not the day's quote | Two readings a week apart are not a statistic | VERIFIED (read at source, 25 Nov 2026) | None | This run: blackrock.com IBTR page |
| 17 | iShares' closed-funds page shows no Treasury iBond closure since Q146; its newest entries are IBIC (15 Oct 2026) and the August 2026 closures, and IBTA's early end is still listed | iShares (2026) | LADDER, TWOREASONS | KNOWN | "Never 'ended on schedule'" stays sourced to the issuer's own page | The page lists announced closures; it is not the prospectus | VERIFIED (read at source, 25 Nov 2026) | None | This run: ishares.com closed funds |
| 18 | IBTG (December 2026) has not yet ended and is not on the closures page; its scheduled mid-December end falls after the report is due, so whether it ends on time is unknown when the report is written | iShares (2026) | LADDER, PRESENTATION | NICHE | The report cannot cite IBTG as an example; IBTA stays the one | IBTG is not one of Laura's funds | VERIFIED (read at source, 25 Nov 2026) | None | This run: ishares.com |
| 19 | iShares Trust's EDGAR filings 17-24 Nov (none concerns IBTM-IBTR): 497s: index changes for PABD/PABU and the S&P growth and value funds; 485BPOS: MLRX, and a 23 Nov batch of international and factor funds; 485APOS: three new buffer ETFs; 8-A12B: MLRX; NPORT-P: 30 Sep holdings | SEC EDGAR (2026) | LADDER, FLOOR | KNOWN | A prospectus supplement for any of Laura's funds would appear here first; none did | Read to 24 Nov New York time; a later filing is after this card | VERIFIED (read at source, 25 Nov 2026) | None | This run: sec.gov EDGAR |
| 20 | No new Treasury iBond fund ending 2037-43 has been filed (no 485APOS for one), so CANON B38 stands: the 2038-42 payments stay on T-bonds | SEC EDGAR (2026); CANON B38 | LADDER | NICHE | Table 1's five T-bonds stay the only route for the later five payments | A fund could be filed later; it would change nothing already bought | VERIFIED (read at source, 25 Nov 2026) | None | This run: sec.gov EDGAR |
| 21 | VT's expense ratio is still 0.06% (as of 27 Feb 2026); 10,158 holdings at 31 Oct 2026 (index 10,207); developed 90.51%, emerging 9.49% | Vanguard (2026a) | CEILING, HALFKEPT | KNOWN | CANON B12-B14 and TNA note 3's "about 10,000 stocks at a 0.06% fee" stand | A 30 Nov count may post before 4 Dec; both are true with their dates | VERIFIED (read at source, 25 Nov 2026) | None | This run: advisors.vanguard.com |
| 22 | VT's fact sheet is still the 30 Sep 2026 edition: 10,185 stocks (index 10,221), 0.06%, ETF assets $81,752m, US 62.4%, Taiwan 3.5%, TSMC 1.6% | Vanguard (2026b) | CEILING, INFLATION_TWD | KNOWN | A fact-sheet citation is dated 30 Sep; the advisor page gives 31 Oct | VT holds Taiwan at about 3.5%: never a Taiwan-dollar hedge | VERIFIED (read at source, 25 Nov 2026) | None | This run: fund-docs.vanguard.com F3141 |
| 23 | VT's 30-day bid/ask spread was 0.02% on 23 Nov (was 0.01%); its year-to-date return at net asset value was 5.36% to 24 Nov against 10.99% to 31 Oct, so world shares fell about 5.1% in November to the 24th (Keel arithmetic) | Vanguard (2026a) | CEILING, MOVE2031 | KNOWN | Context only: the register stays dated 6 Nov, and NUMBERS 8p already tests a 40% fall before the 2031 move, with the bottom and every payment unchanged | A month's move says nothing about 2031 | VERIFIED (read at source, 25 Nov 2026; change Keel arithmetic) | None | This run: advisors.vanguard.com |
| 24 | DGBAS's price-release list (updated 24 Nov) still ends at October 2026: CPI +2.33% a year, core +2.23%, January-October +1.98% | DGBAS (2026a, 2026b) | INFLATION_TWD, RESIDENCY | KNOWN | NUMBERS 8d's inflation input stands | None | VERIFIED (read at source, 25 Nov 2026) | None | This run: eng.stat.gov.tw |
| 25 | The October release names the next one: "Next release － December 8, 2026, for the price indices for November 2026" (16:00 Taipei; the Chinese text says the same) | DGBAS (2026b) | INFLATION_TWD, PROCESS | KNOWN | November CPI comes out 8 Dec, 19:00 Sydney, after the 5 Dec 09:00 Sydney deadline | None | VERIFIED (read at source, 25 Nov 2026) | None | This run: DGBAS October release PDF |
| 26 | The building-cost index platform says November data is "預計於115年12月8日 16:00發布" (expected 8 Dec 2026, 16:00): Q146's UNVERIFIED "7-8 Dec" is one date, after the report is due, so October's 120.50 (+7.18%) is the last index the report can print | DGBAS (2026c) | RESIDENCY, INFLATION_TWD | KNOWN | NUMBERS 8d's "about 8 Dec" is exact; Table 3's building-cost row is dated October 2026 | The page did not render in a plain fetch; the line was read in a search tool's excerpt of the live page | VERIFIED (read at source via a live-page excerpt, 25 Nov 2026) | None | This run: stat.gov.tw/CCI |
| 27 | The same platform warns "最近3個月資料均可能修正" (the latest three months' data may all be revised): October's 120.50 could change with November's release, after the report is in | DGBAS (2026c) | RESIDENCY, PRESENTATION | NICHE | Print it as "October 2026, as first published": a dated reading, like the curve | The size of past revisions was not checked (Gaps) | VERIFIED (read at source, 25 Nov 2026) | None | This run: stat.gov.tw/CCI |
| 28 | Taiwan's central bank: NT$32.939 per US dollar on 24 Nov (32.895 on 23 Nov, 32.850 on 17 Nov, 32.768 on 6 Nov), so the Taiwan dollar is 0.52% weaker than on 6 Nov (Keel arithmetic) | CBC (2026) | INFLATION_TWD | KNOWN | Context only: NUMBERS 8d keeps 32.768; a weaker NT$ makes US-dollar money go further in Taiwan, the opposite of the watched risk | Table 3 row 7 watches an NT$ 10% stronger than in 2031, far from a 0.5% move | VERIFIED (read at source, 25 Nov 2026) | None | This run: cbc.gov.tw |
| 29 | Treasury par curve at the 24 Nov 2026 close: 1y 4.59, 2y 4.63, 3y 4.67, 5y 4.69, 7y 4.79, 10y 4.91, 20y 5.33, 30y 5.30; 0.04 to 0.26 points above 6 Nov (most at 1 year), 0.01 to 0.21 below 17 Nov (Keel arithmetic) | US Department of the Treasury (2026) | CERTAINTY, PRESENTATION | KNOWN | Register note only: the report stays on the 6 Nov curve and is never re-sized; most of the rise Q146 saw at 5-30 years has gone | The 20 Nov fall (2y 4.76 to 4.63) is one day's news | VERIFIED (read at source, 25 Nov 2026) | None | This run: home.treasury.gov CSV |
| 30 | BPC (18 Nov 2026): the US "will most likely reach the debt limit once again in February or March 2027", with resources "expected to last roughly six to nine months", so the X-date is about August-December 2027 (Keel arithmetic); BPC says the range "has not yet come into focus for a specific projection" | Quakenbush, Till & Akabas (2026) | TWOREASONS, CERTAINTY | KNOWN | Q30's window (about August 2027-May 2028) moves earlier: the risk now sits in 2027, the plan's first year | BPC gives no X-date projection yet | VERIFIED (read at source, 25 Nov 2026) | Watch: never date the debt-limit risk "early 2028" | This run: bipartisanpolicy.org |
| 31 | Why the dates moved: BPC counts "$764 billion in remaining borrowing authority", with debt $398bn above CBO's projection at the end of fiscal 2026; store row Q15-026 had BPC's June "between late winter and mid-summer of 2027" | Quakenbush et al. (2026); store Q15-026 | TWOREASONS | KNOWN | A debt-limit date is a forecast with its own date, like the range | None | VERIFIED (read at source, 25 Nov 2026) | None | This run: bipartisanpolicy.org |
| 32 | NTU (12 Nov 2026): the limit is likely hit in February 2027, with the X-date "by the beginning of December 2027" (scenarios November 2027-February 2028; $777bn of room on 30 Oct); its August central case was May 2027 and February 2028 | Dickerson (2026) | TWOREASONS | KNOWN | Two independent counters now agree on early 2027 for the limit | NTU gives scenarios, not one forecast | VERIFIED (read at source, 25 Nov 2026) | None | This run: ntu.org |
| 33 | Daily Treasury Statement (Keel arithmetic, debt subject to limit against the $41,103,996m limit): headroom $640.7bn on 16 Nov, $589.6bn on 17 Nov, $575.6bn on 23 Nov; it was $739.8bn on 9 Nov (card Q30), about $82bn a week | US Treasury Fiscal Service (2026) | TWOREASONS | NICHE | Shows the room being used up, which is why both counters moved their dates forward | One day fell $51bn (16-17 Nov); two weeks are not a trend | VERIFIED (read at source, 25 Nov 2026; headroom Keel arithmetic) | None | This run: api.fiscaldata.treasury.gov |
| 34 | A Fiscal Times story on Yahoo Finance (18 Nov) says BPC estimates an October 2027 X-date; BPC's own brief gives no X-date projection | Yahoo Finance / The Fiscal Times (2026); Quakenbush et al. (2026) | TWOREASONS, PRESENTATION | NICHE | Cite BPC, never the retelling | None | CONFLICTING (the retelling says October 2027; BPC says the range is not yet in focus) | None | This run: finance.yahoo.com |
| 35 | Senator Thune, interviewed by Semafor and reported by Bloomberg (20 Nov), said a debt-limit rise "probably ends up getting punted" into 2027 | Bloomberg (2026) | TWOREASONS | KNOWN | No fix is likely before the report goes in | Second-hand, behind a paywall | UNVERIFIED (search excerpt of Bloomberg's report of a Semafor interview; not read in either article) | None | This run: bloomberg.com excerpt |
| 36 | For the plan: the X-date window now falls in late 2027, while the ten are held and before the 2028 deposit is invested; Table 3 row 2 counts a Treasury payment more than five business days late, never the X-date, so the rule needs no change, and no source reports a late payment | NUMBERS failure table row (a); Quakenbush et al. (2026); Dickerson (2026); card Q30 | TWOREASONS, CERTAINTY | NICHE | 3e can say the debt limit returns in 2027 and name the date that matters: the payment, not the deadline | Q30's riskiest date for Laura (near mid-December 2032) is untouched by a 2027 X-date | VERIFIED (sources read at source, 25 Nov 2026; the implication is Keel analysis) | None | This run: Keel analysis |
| 37 | BPC also notes a continuing resolution to 11 Dec 2026 and that "market participants anticipate an additional rate hike in December": two dated events after the freeze that a judge reading in December may know and the report cannot | Quakenbush et al. (2026) | PRESENTATION, CERTAINTY | NICHE | Dated wording ("on the Treasury curve of 6 November 2026") answers a judge who knows December's news | None | VERIFIED (read at source, 25 Nov 2026) | None | This run: bipartisanpolicy.org |

## Best five for the report

1. **Row 36 (3e, Table 3 row 2).** The debt limit returns in 2027, but the plan counts payments, not deadlines. A judge who knows the X-date news sees that the rule was built for it.
2. **Row 7 (3e area (1), Table 2's note).** "Above the middle of published forecasts" survives fifteen, seventeen and eighteen houses. That is why the report prints no median.
3. **Row 26 (Table 3, 3e).** November's building-cost index comes out three days after the report is due. October 2026's 120.50 is final for the report, now verified at the official platform.
4. **Row 27 (Table 3, 3e).** The publisher may revise the index after the report is in. "As first published" is the honest date, like the curve's.
5. **Rows 13 and 19 (Table 3's fund-notices row, 2.2).** No notice appears on the fund pages or in the trust's own SEC filings. "None at the freeze" has two sources.

## Gaps

- Firecrawl reported its credits used up during this run (allowance reset 25 Nov 09:13 UTC). The run switched to Parallel and WebFetch, as the brief says. Earlier WebFetch reads of the iBond pages served October caches; the live figures above come from fresh fetches.
- BMO's 6.2%: the currency and global index were not printed in the text read (row 5).
- No 2026-27 long-term update was found for:
  - AQR;
  - Research Affiliates (after 31 Oct);
  - Morgan Stanley's long-term assumptions;
  - Vanguard's 2027 outlook;
  - a BlackRock figure in text.

  Northern Trust's 2027 edition is expected in December. Morgan Stanley's one-year outlook was seen only in a search excerpt.
- J.P. Morgan's release was read from a copy taken 7 Nov (row 1).
- The building-cost index:
  - The English advance-calendar page's rule, as read ("fifth working day"), does not match the dates. October's release (5 Nov) was the fourth working day and 8 Dec is the sixth. The dated announcement governs.
  - The size of past revisions was not checked.
- VT's 30 Nov holdings count is not yet posted. EDGAR was read to 24 Nov, New York time.
- The Thune quote was not read in the article itself (row 35).
- Secondary pages seen and not used as sources:
  - PortfolioLab, which lists GMO's 31 Oct forecast (updated 24 Nov);
  - Advisor Perspectives' GMO reprint (20 Nov);
  - stockanalysis.com (19 Nov), Politico and the New York Times (18 Nov) on the debt limit.

## Sources

American Century Investments. (2026, November 3). *Latest capital market assumptions*. https://www.americancentury.com/institutional-investors/en-at/insights/latest-capital-markets-assumptions. Retrieved November 25, 2026.

Amundi Investment Institute. (2026, April 21). *Capital market assumptions 2026*. https://research-center.amundi.com/article/capital-market-assumptions-2026. Retrieved November 25, 2026.

BlackRock. (2026). *Capital market assumptions*. https://www.blackrock.com/institutions/en-us/insights/thought-leadership/capital-market-assumptions. Retrieved November 25, 2026.

BlackRock. (n.d.-a). *iShares iBonds Dec 2032 Term Treasury ETF (IBTM)*. https://www.blackrock.com/us/individual/products/328944/ishares-ibonds-dec-2032-term-treasury-etf. Retrieved November 25, 2026.

BlackRock. (n.d.-b). *iShares iBonds Dec 2033 Term Treasury ETF (IBTO)*. https://www.blackrock.com/us/individual/products/332291/ishares-ibonds-dec-2033-term-treasury-etf. Retrieved November 25, 2026.

BlackRock. (n.d.-c). *iShares iBonds Dec 2034 Term Treasury ETF (IBTP)*. https://www.blackrock.com/us/individual/products/337745/ishares-ibonds-dec-2034-term-treasury-etf. Retrieved November 25, 2026.

BlackRock. (n.d.-d). *iShares iBonds Dec 2035 Term Treasury ETF (IBTQ)*. https://www.blackrock.com/us/individual/products/342105/ishares-ibonds-dec-2035-term-treasury-etf. Retrieved November 25, 2026.

BlackRock. (n.d.-e). *iShares iBonds Dec 2036 Term Treasury ETF (IBTR)*. https://www.blackrock.com/us/individual/products/350028/ishares-ibonds-dec-2036-term-treasury-etf. Retrieved November 25, 2026.

Bloomberg. (2026, November 20). *Thune sees debt limit hike as next year's fight, Semafor reports* [Search excerpt only]. https://www.bloomberg.com/news/articles/2026-11-20/thune-sees-debt-limit-hike-as-next-year-s-fight-semafor-reports. Retrieved November 25, 2026.

Central Bank of the Republic of China (Taiwan). (2026). *Exchange rates: NTD/USD closing rates* [Data set]. https://www.cbc.gov.tw/en/lp-700-2.html. Retrieved November 25, 2026.

Dickerson, M. (2026, November 12). *Debt limit likely to be hit in February with the X-date reached by December 2027*. National Taxpayers Union. https://www.ntu.org/publications/detail/debt-limit-likely-to-be-hit-in-february-with-the-x-date-reached-by-december-2027. Retrieved November 25, 2026.

Directorate-General of Budget, Accounting and Statistics. (2026a). *Price statistics: News releases* [Web page, updated November 24, 2026]. https://eng.stat.gov.tw/News.aspx?n=2319&sms=10854. Retrieved November 25, 2026.

Directorate-General of Budget, Accounting and Statistics. (2026b, November 5). *The price indices for October 2026* [Press release]. https://ws.dgbas.gov.tw/001/Upload/464/relfile/10854/236838/the%20price%20indices%20for%20october%202026.pdf. Retrieved November 25, 2026.

Directorate-General of Budget, Accounting and Statistics. (2026c). *營造工程物價指數 [Construction cost index] platform*. https://www.stat.gov.tw/CCI/CCI_Site/index.aspx. Retrieved November 25, 2026. Advance release calendar: https://eng.stat.gov.tw/News_NoticeCalendar_Content_EN_temp.aspx?MetaI_D=169&n=4011&year=2026. Retrieved November 25, 2026.

EFG International. (2026, November 9). *Capital market assumptions 2027*. https://www.efginternational.com/doc/jcr:876fd20b-1786-44a6-b890-b9301535d128/lang:en/EFG_CMA_2027_EN.pdf. Retrieved November 25, 2026.

Fidelity International. (2026). *Capital market assumptions update: H2 2026*. https://www.fidelity.com.au/sites/fidelity/assets/Capital-Market-Assumptions-update---H2-2026.pdf. Retrieved November 25, 2026.

GMO. (2026, November 19). *GMO 7-year asset class forecast: As of October 31, 2026*. https://www.gmo.com/globalassets/articles/gmo-7-year-asset-class-forecast/2026/gmo-7-year-asset-class-forecastoct26.pdf. Retrieved November 25, 2026.

Goldman Sachs. (2026, November 19). *US stocks predicted to extend historic rally as gains moderate*. https://www.goldmansachs.com/insights/articles/us-stocks-predicted-to-extend-historic-rally-as-gains-moderate. Retrieved November 25, 2026.

Invesco. (2026). *Long-term capital market assumptions* [Q2 2026]. https://www.invesco.com/apac/en/institutional/insights/multi-asset/long-term-capital-market-assumptions.html. Retrieved November 25, 2026.

iShares. (2026). *Closed fund updates*. https://www.ishares.com/us/products/closed-funds/updates. Retrieved November 25, 2026.

J.P. Morgan Asset Management. (2026, October 19). *J.P. Morgan releases 2027 Long-Term Capital Market Assumptions* [Press release]. https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2027-long-term-capital-market-assumptions/. Retrieved November 25, 2026.

Morgan Stanley. (2026, November 18). *2027 stock market investment outlook* [Search excerpt only]. https://www.morganstanley.com/insights/articles/stock-market-investment-outlook-2027. Retrieved November 25, 2026.

Northern Trust Asset Management. (2025). *2026 capital market assumptions report*. https://ntam.northerntrust.com/content/dam/northerntrust/investment-management/global/en/documents/thought-leadership/2026/cma/2026-capital-market-assumptions-report.pdf. Retrieved November 25, 2026.

PGIM. (2026). *Capital market assumptions*. http://www.pgim.com/global/en/financing/insights/market-portfolio/outlooks/capital-market-assumptions. Retrieved November 25, 2026.

Phillips, D., Schleif, C., & Karthik, P. (2026). *Artificial intelligence, debt & Darwin: BMO Wealth Management capital market assumptions, 2027 edition*. BMO Wealth Management. https://www.bmo.com/dam_asset/asset/7971043a-3b13-4375-a28e-863a0fe58136/2027-Long-Term-Outlook.pdf. Retrieved November 25, 2026.

Quakenbush, C., Till, A., & Akabas, S. (2026, November 18). *The debt limit returns in 2027: What to expect*. Bipartisan Policy Center. https://bipartisanpolicy.org/issue-brief/the-debt-limit-returns-in-2027-what-to-expect/. Retrieved November 25, 2026.

Schwab Asset Management. (2026). *Capital market expectations*. https://www.schwabassetmanagement.com/resource/capital-market-expectations. Retrieved November 25, 2026.

U.S. Securities and Exchange Commission. (2026). *EDGAR company filings: iShares Trust (CIK 0001100663)*. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001100663. Retrieved November 25, 2026.

U.S. Department of the Treasury. (2026). *Daily Treasury par yield curve rates, November 2026* [Data set]. https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202611?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611&page&_format=csv. Retrieved November 25, 2026.

U.S. Department of the Treasury, Bureau of the Fiscal Service. (2026). *Daily Treasury Statement: Debt subject to limit* [Data set]. https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/debt_subject_to_limit. Retrieved November 25, 2026.

UBS Global Wealth Management. (2026, November 18). *Year ahead 2027*. https://www.ubs.com/global/en/wealthmanagement/insights/marketnews/article/_jcr_content.503631324.file/PS9jb250ZW50L2RhbS9pbXBvcnRlZC9jaW9yZXNlYXJjaC9wZGYvNDAvMjUvMjcvNS80MDI1Mjc1L2VuLzQwMjUyNzUucGRm/4025275.pdf. Retrieved November 25, 2026.

Vanguard. (2026a). *Vanguard Total World Stock ETF (VT)* [Advisor product page]. https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etf. Retrieved November 25, 2026.

Vanguard. (2026b). *Vanguard Total World Stock ETF fact sheet* [As of September 30, 2026]. https://fund-docs.vanguard.com/F3141.pdf. Retrieved November 25, 2026.

Vanguard. (2026c). *Vanguard economic and market outlook: Return forecasts*. https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html. Retrieved November 25, 2026.

Yahoo Finance / The Fiscal Times. (2026, November 18). *US to hit debt limit again* [Secondary report]. https://finance.yahoo.com/economy/policy/articles/us-hit-debt-limit-again-235558036.html. Retrieved November 25, 2026.
