# Q4b research cards: do co-sponsors cut their giving when share prices fall, by how much, and how late?

Research run, Mon 9 Nov 2026 (Sydney). These are notes for the Final Report store, not report prose. The claim
tested: "The funders who would co-sponsor a residency (private and corporate foundations, corporate sponsors, public
arts funds, and in Taiwan the National Culture and Arts Foundation and corporate foundations) cut their giving when
share prices fall, and by how much, with what lag." I treated it as a philanthropy-economics and public-finance
problem. It is checked against Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt`) and the case
(`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, cited as "case l.N", the line in that text file). The plan is frozen, so a "yes"
in the Clash column is a risk to note in the Final Report, never a change to propose. I did not attempt Laura's
facility cost (case l.164-166), contingency sizing (case l.106-107), or Taiwan law and tax.

How to read the table:
- Tags are as in `../HARVEST_BRIEF.md`. RESIDENCY is added, as in Q9: how residencies and arts bodies are funded.
- Verified? has four values:
  - VERIFIED, with what I read (full text, a PDF page, an abstract page, or a search excerpt of the source itself);
  - UNVERIFIED, not read at the source;
  - CONFLICTING, two sources read that disagree;
  - prior, verified by an earlier Keel file that is named and was not re-read today.
  "Keel inference" and "Keel arithmetic" mark my own reasoning or sums, not a source's claim.
- Every URL was accessed 9 Nov 2026. Percentages are nominal (money of the day) unless marked "real". A "lag" counts
  from the year shares fell. NT$ figures are nominal.
- Share-market yardsticks used below:
  - S&P 500 total return: 2000 -9.03%, 2001 -11.85%, 2002 -21.97%, 2008 -36.55%, 2009 +25.94%, 2010 +14.82%
    (Damodaran file in the repo, `keel/library/insight_v1/scripts/data/D3/damodaran_histretSP_1928_2025.csv`,
    as quoted in Q1; prior).
  - S&P 500 price change 2022: -19.4% (-25.4% real) (Giving USA 2023, row 7).
  - TAIEX 2015: -10.41% (Central Bank of the Republic of China (Taiwan), Annual Report 2015,
    https://www.cbc.gov.tw/en/public/Attachment/661517483371.PDF).
  - TAIEX 2022: -22.40% (TWSE annual report 2022, https://www.twse.com.tw/downloads/zh/about/company/annual_111.pdf).
  - TAIEX 2008 -46.03%, 2009 +78.34% and 2011 -21.18% come from a secondary table of TWSE data. They are UNVERIFIED at
    TWSE.
- Store checked first (`../store/insights.jsonl`). Already held there, so not repeated here:
  - Giving USA 2010 totals and the "three to five years" recovery (H2-057, H8-112, W-04);
  - arts giving -11.9% real in 2007-09, with Merton 1991 and Dimmock 2012 (H7-080);
  - university building pauses (H3-082, H8-113);
  - Barron's (H6-065);
  - the Ministry of Culture village subsidy (H9-116);
  - failed pledges (H7-070);
  - NCAF's endowment gap and its 2015 revenue fall (Q9-033, Q9-034);
  - NCAF donations counted as gifts to government (Q11b-018).
  Seed money, assurance contracts, ranges and case statements are covered in Q11a and Q11b and not repeated.
- Two corrections:
  - Row 2 corrects H9-013: "foundation giving fell 8.6% in 2009 (8.9% current)" was an early estimate. The counted
    fall was 2.1%.
  - Rows 26-27 settle Q9 row 34's open critique. The 2014 figure was ordinary investment income, not a one-off, and
    the 41% fall did not reach NCAF's grants.

## Verdicts on the claim

1. **"They cut their giving when share prices fall." CHANGE, do not kill.** The claim holds for corporate sponsors and
   public arts budgets. It is weak for foundations taken together, and false for some large foundations in a given
   crash.
   - US foundation giving rose 5.4% in 2008, while foundation assets fell 17.2% (row 1). It fell only 2.1% in 2009
     (row 2).
   - Corporate cash giving follows the previous year's profits. In the UK, business money for the arts fell four years
     running (rows 15-18).
   - US state arts budgets fell 27% from FY2008 to FY2012 and kept falling after the recession ended (rows 21-22).
   - Better claim: co-sponsors do cut, but later, by less than shares, and by very different amounts depending on the
     type of funder.
2. **How much.** Share falls in these episodes were 19-46%. Against that, the funders cut as follows:
   - **Foundations:** a few per cent on average. The 2008-10 peak to trough was about -2.3%. In 2023, the year after
     the 2022 fall, it was -2.3% real.
   - **Corporate cash and arts sponsorship:** about 7-15% over two to three years. CECP cash giving fell 7.3% over
     2007-09; US business arts support fell 14% over 2006-09; UK business arts money fell 14.5% nominal over 2008/09 to
     2010/11.
   - **US state arts agencies:** about 25-40% (-26.5% over FY2008-12, -37.7% over FY2001-04).
   - **NEA:** -17% (2010-13), after a rise through stimulus money.
   - **NCAF in Taiwan:** income swings hard (-41% in 2015, -80% in 2011), but grants moved only -1% to +5% in those
     years.
3. **How late.**
   - Foundations: one to two years. The 5% rule averages asset values across the year and allows the payout to come by
     the end of the next year; many funders also average over several years (rows 4-5).
   - Corporate money: one to three years, because it follows the previous year's profits.
   - Public money: two to four years. It is often preceded by a stimulus rise, and it takes five to seven years to
     recover.
   - In every type, the cuts come while shares are already recovering.
4. **Q9 row 30 (the kept half is in shares, so it may be smallest when co-sponsors fall short): it HOLDS in
   direction, but CHANGE the timing.** Shares fall first and recover first, while co-sponsor shortfalls arrive one to
   three years later. So when a shortfall bites, the kept half has usually won back part of its fall. The overlap is
   worst in two cases:
   - a crash about one to two years before the facility money is needed (2031-32, before 2033);
   - a long bear market such as 2000-02.
   It remains a risk to note, never a change (row 33).
5. **For the kept half and the 2031 meetings.**
   - A crash in 2029-30 would reach co-sponsors' budgets in 2031-33, which is exactly when Laura meets them and the
     building needs money.
   - Laura's bottom figure is bought in 2028 and does not move. Her own number is steady in the years when others'
     numbers are being cut.
   - The kept half is the part that is hit first and recovers first.
   - The meetings should weigh funder type: smoothed funders, signed multi-year letters, and corporate in-kind offers
     treated as non-cash (row 34).
6. **Who does not cut, or cuts least.**
   - Large endowed foundations: Gates in 2009; five foundations borrowing to give more in 2020 (rows 31-32).
   - Foundations whose grants follow multi-year averages (rows 4, 8).
   - UK trusts and foundations, which rose 26% while UK business arts money fell (row 19).
   - Corporate foundations, whose giving held in 2009, unlike corporate cash budgets (row 3).
   - Funders with a grant reserve, such as NCAF (rows 27-29).
   - Funders giving alongside match money (row 20).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | US foundation giving ROSE in the crash year: foundation assets fell 17.2% in 2008 ($682.2bn to $565.0bn) while foundation giving rose 5.4% ($44.4bn to $46.8bn). The yearbook says funders cut operating costs or drew on endowments to "shore up" giving, and used "asset-averaging" | Foundation Center, Foundations Today Series 2010, "Foundation Growth and Giving Estimates" highlights, https://www.giarts.org/sites/default/files/Foundation_Growth_2010.pdf ; second copy https://carolinapublicpress.org/wp-content/uploads/2012/01/Foundation-Center-2010-yearbook.pdf (accessed 9 Nov 2026) | COSPONSOR, HALFKEPT | NICHE | A foundation's grant budget for a year is mostly set before the crash. Shares fall first and grants follow later | US foundations only. Part of the 2008 rise is Gates (row 31) and gifts still arriving. 2008 grants were largely committed in 2007 | VERIFIED (highlights PDF, both copies) | yes, partly: the IPS says co-sponsors cut "during that same period" as shares fall; for foundations the cut comes a year or more later (risk to note) | This run: highlights PDFs |
| 2 | The counted 2009 fall was small. Foundation giving fell 2.1% to $45.8bn in 2009 (a "record" decline) and 0.2% to $45.7bn in 2010. The first estimate had been -8.4% (Foundation Center 2010), Giving USA 2010 printed -8.9% current, and the 2009 forecast was -8% to -13% | Foundation Center, Foundations Today Series 2011 highlights, https://carolinapublicpress.org/wp-content/uploads/2012/01/Foundation-Center-yearbook-2011.pdf ; Foundations Today 2009 edition highlights, https://search.issuelab.org/resource/foundations-today-foundation-yearbook-2009-edition-highlights ; row 1 URL (accessed 9 Nov 2026) | COSPONSOR | NICHE | Peak to trough, US foundation giving fell about 2.3% ($46.8bn to $45.7bn, Keel arithmetic) while the S&P 500 fell 36.55% | Nominal: the real fall is a little larger. Only one crash. Estimates made during a crash overstate the fall | VERIFIED (both highlights PDFs). CORRECTS store H9-013, whose "foundation giving fell 8.6% in 2009 (8.9% current)" is the early estimate | no | This run: highlights PDFs |
| 3 | By type in 2009: independent foundations -3.2%, community foundations -7.1%, corporate foundations +2.6% (after +3.9% in 2008), and the 25 largest funders +14.2%. The reasons given are "the commitment of many foundations to maintaining their grants budgets or reducing the extent of reductions relative to their assets losses", a market rebound, and new foundations | Foundation Center 2011 highlights (row 2 URL); 2008 corporate figure from the 2010 highlights (row 1 URL) (accessed 9 Nov 2026) | COSPONSOR | NICHE | For a co-sponsor list: big endowed funders and corporate foundations held up best in 2009, and community foundations cut most | A corporate foundation (with its own endowment) is not the same as a company's giving budget (rows 15-16). US only | VERIFIED | no | This run: highlights PDFs |
| 4 | Foundations spent a larger share of their assets in the crash. The median payout rate of 979 endowed foundations was 5.4% (2007), 5.8% (2008) and 6.4% (2009) while their assets fell about 24% in 2008. The 2009 yearbook names "short-term increases in payout rates" and a "rolling average of their asset values" | Foundation Center, "Foundation Payout" (2012), https://foundationcenter.issuelab.org/resources/14076/14076.pdf ; 2009 highlights (row 2 URL) (accessed 9 Nov 2026) | COSPONSOR, MOVE2031 | KNOWN | Smoothing is why the lag exists: grants follow an average of past asset values, not this year's price | A higher rate on a smaller base still means smaller grants a year or two later | VERIFIED (PDF) | no | This run: payout study PDF |
| 5 | US law builds in the lag. The 5% minimum is figured on asset values set "on a monthly basis" over the year. A foundation has until the end of the following year to pay it before a 30% tax, and excess payouts carry forward | 26 U.S. Code s 4942, https://www.law.cornell.edu/uscode/text/26/4942 (accessed 9 Nov 2026) | COSPONSOR, MOVE2031 | KNOWN | A crash in one year lowers the required grants mostly in the next two years, so a US foundation met in 2031 pays a 2033 pledge partly from earlier, higher asset values | US private foundations only. The rule is a floor and many pay more. Taiwan's rules for foundations were not checked (gap) | VERIFIED (statute text); the lag in years is Keel inference | no | This run: Cornell LII statute page |
| 6 | Community foundations kept granting while gifts into them fell: grants were up 15% on 2006 while gifts received were down 22% (2009 survey) | Council on Foundations, 2009 Columbus Survey results, https://cof.org/sites/default/files/2023-08/04-08-10_2009%20Columbus%20Survey%20Results_29221_0.pdf (accessed 9 Nov 2026) | COSPONSOR | NICHE | Pass-through funders run down their balances to keep grants up for a year or two | Partly at odds with row 3 (-7.1% in 2009 against 2008); different base year and sample | CONFLICTING (both read; different bases) | no | This run: survey PDF |
| 7 | 2022, the last big share fall: the S&P 500 fell 19.4% (-25.4% real). Foundation giving rose 2.5% to $105.21bn (-5.0% real), corporate giving rose 3.4% to $29.48bn (-4.2% real), individuals fell 6.4% (-13.4% real), and arts giving rose 2.9% current | Giving USA 2023 press release, Indiana University Lilly Family School of Philanthropy, https://news.iu.edu/philanthropy/live/news/51591-giving-usa-total-us-charitable-giving-declined-in (accessed 9 Nov 2026) | COSPONSOR, CAREER | KNOWN | When shares fell alongside high inflation, institutional givers held their budgets in money terms, and their real cuts were small | One year. Inflation, not the market, did most of the real cut | VERIFIED (press release) | no | This run: IU press release |
| 8 | The lag year after 2022: foundation giving fell 2.3% real in 2023, to $103.53bn from $105.99bn (2023 dollars). 22% of foundations cut their payout rate in 2022, and for 2023 more expected to cut (27%) than raise (23%), the first time in the survey's history. 79% of 546 said inflation did not change their 2022 grants, several because grants "are based on the average market return of assets over multiple years" | Giving USA 2024 via BWF, https://www.bwf.com/giving-usa-2024-report-insights/ ; Candid, https://candid.org/blogs/foundation-giving-and-payout-in-2022-what-changed-whats-next ; https://candid.org/blogs/how-inflation-affects-grantmaking-decisions-foundations ; https://candid.org/blogs/foundation-giving-data-in-2023-expected-grantmaking-in-2024 ; Chronicle of Philanthropy, 29 Jun 2023, https://www.philanthropy.com/news/many-foundations-are-taking-a-step-back-after-2-years-of-steep-increases-in-grants-budgets (accessed 9 Nov 2026) | COSPONSOR, MOVE2031 | NICHE | The foundation cut came one year after the share fall, while shares were recovering. This is the same shape as 2008-09 | Candid's own sample shows 2023 grants up 1.7% ($25.8bn to $26.2bn; median +0.3%; median payout of independent foundations 5%, mean 7.5%). Giving USA's real figure and Candid's nominal figure differ | CONFLICTING on size (Giving USA -2.3% real; Candid sample +1.7% nominal); timing agrees | yes, partly: timing, as row 1 | This run: BWF page, Candid blogs, Chronicle article |
| 9 | Arts giving held through the 2022 share fall. In 2023 dollars, arts, culture and humanities giving was $23.55bn (2019), $22.70bn (2020), $23.49bn (2021), $23.70bn (2022) and $25.26bn (2023, +6.6% real) | Giving USA 2024 table as given by BWF, https://www.bwf.com/giving-usa-2024-report-insights/ (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | KNOWN | The worst recent year for US arts giving was the 2020 shutdown (-3.6% real, Keel arithmetic), not the 2022 share fall | US totals, mostly from individuals. This is not building co-sponsorship. Read through BWF, not the Giving USA report | VERIFIED (BWF's table); Giving USA report itself not read | no | This run: BWF page |
| 10 | Foundations do not act counter-cyclically. Their payouts after financial shocks show "retrenchment" or "independence", not more giving when need rises | Calabrese, T.D. & Ely, T.L. (2022) "How US Private Foundations Change Payouts Based on Financial Shocks: Revealed Publicness or Revealed Privateness?", Journal of Public Administration Research and Theory 32(1): 166-182, https://academic.oup.com/jpart/article/32/1/166/6277840 (accessed 9 Nov 2026) | COSPONSOR | NICHE | Do not assume a foundation co-sponsor will step in when others cut | US data. Abstract only | VERIFIED (abstract page) | no | This run: OUP abstract page |
| 11 | Foundations respond asymmetrically. "A 10 percent asset shock raises payout rates by 10 to 16 basis points for positive returns but decreases them by 31 to 39 basis points after negative returns". They "do not increase aggregate spending in periods of elevated need". Founder-family foundations cut 102% more after losses. Peers crowd each other out (elasticity -0.22). Median grant payout is 4.84%, and the correlation between foundations' returns is 0.44 | Lu, Y. & Malliaris, S. (2026) "Charitable capital allocation: Evidence from private foundations", Journal of Financial Economics 185, 104377 (open access), https://www.sciencedirect.com/science/article/pii/S0304405X26001480 (accessed 9 Nov 2026) | COSPONSOR, HALFKEPT | NICHE | Foundations still run by the founder's family are the likeliest to cut. Because their returns move together, shortfalls tend to come in clusters | Rates, not dollars. In 2008-09 the aggregate rate rose (row 4) because grants lagged falling assets. US only | VERIFIED (article text) | yes, partly: supports the cluster risk in Q9 row 30 (risk to note) | This run: ScienceDirect open-access article |
| 12 | University endowments cut payouts below their own policy after losses but do not raise them after gains ("endowment hoarding"). A later study found symmetric responses | Brown, J.R., Dimmock, S.G., Kang, J.-K. & Weisbenner, S.J. (2014) "How University Endowments Respond to Financial Market Shocks", American Economic Review 104(3), https://consensus.app/papers/details/7831f601f303581cb3e87906847e0fab/ ; Rosen et al. (2019), Journal of Higher Education (via Consensus search) (accessed 9 Nov 2026) | COSPONSOR | KNOWN | A partner university or other endowed body protects its endowment first | Universities, not arts funders | CONFLICTING (abstracts of both read) | no | This run: Consensus abstracts |
| 13 | Million-dollar gifts from foundations "tend to be countercyclical". Corporate million-dollar giving is less tied to the economy. Million-dollar gifts to the arts go with good economic conditions | Osili, U. O., Ackerman, J. & Li, Y. (2019) "Economic effects on million dollar giving", Nonprofit and Voluntary Sector Quarterly 48(2): 417-439, https://doi.org/10.1177/0899764018800791 (issue year 2019, online first 2018; REFERENCES_APA row 98); abstract read at https://consensus.app/papers/details/d558d16e83195cf6b31f8d6f98a7f6b8/ (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | NICHE | Big single grants from foundations may be the steadiest co-sponsor money. Big arts gifts from individuals are the least steady | US. Abstract only | VERIFIED (abstract via Consensus) | no | This run: Consensus abstract |
| 14 | Donations respond more to booms than to busts (US aggregate data, 1968-2007) | List, J.A. & Peysakhovich, Y. (2011) "Charitable donations are more responsive to stock market booms than busts", Economics Letters, https://consensus.app/papers/details/a1e6b1a3c8aa562990811edb9db34cf9/ (accessed 9 Nov 2026) | COSPONSOR | NICHE | For all giving, the fall in a crash is milder than the rise in a boom. This matches rows 1-2 | Mostly individuals. For foundations the opposite asymmetry is found (row 11) | VERIFIED (abstract via Consensus) | no | This run: Consensus abstract |
| 15 | In the Great Recession, giving fell more than shocks to income or wealth explain; attitudes changed | Meer, J., Miller, D. & Wulfsberg, E. (2017) "The Great Recession and charitable giving", Applied Economics Letters 24(21): 1542-1549, https://doi.org/10.1080/13504851.2017.1319556 (REFERENCES_APA row 94); abstract read at https://consensus.app/papers/details/1142ead87f7951f5ac624ebb5bf70307/ (accessed 9 Nov 2026) | COSPONSOR | NICHE | A crash can cut giving through mood as well as money, so a co-sponsor's balance sheet is not the whole story | Household (PSID) data, not institutions | VERIFIED (abstract via Consensus) | no | This run: Consensus abstract |
| 16 | Corporate giving follows profits, not share prices, and the previous year's profits at that. "Corporate giving is tied more closely to corporate profits than stock market performance". Giving as a share of the previous year's pre-tax profit was 1.02% (2007/2006), 0.99% (2008/2007) and 1.21% (2009/2008), and "previous-year profit is related to current-year giving" | Federal Reserve Bank of Richmond, Econ Focus Q2 2010, https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/econ_focus/2010/q2/pdf/feature3.pdf ; CECP, Giving in Numbers 2010, https://intranet.americansforthearts.org/sites/default/files/GivinginNumbers2010.pdf (accessed 9 Nov 2026) | COSPONSOR, CAREER | KNOWN | A corporate co-sponsor's 2033 budget is set from its 2032 profits, which builds in a one-year lag | Large US companies (CECP members) | VERIFIED (both PDFs) | yes, partly: timing (risk to note) | This run: PDFs |
| 17 | Corporate giving held in 2008, fell in 2009, and switched from cash to goods. Giving rose or held for 63% of companies in 2007-08 while profits fell; it fell for 57-59% in 2009. Cash giving was $4.63bn (2007), $4.53bn (2008) and $4.29bn (2009) for 96 firms (-7.3% over two years, Keel arithmetic). "Many companies compensated for fewer cash grants with product donations". Giving USA: corporate giving rose 5.5% in 2009, driven by in-kind gifts | CECP Giving in Numbers 2012, https://cecp.org/wp-content/uploads/2016/11/GIN2012_finalweb.pdf ; 2013, https://www.americansforthearts.org/sites/default/files/GIN2013_Web_Final.pdf ; 2010 (row 16 URL); Giving USA 2010 Executive Summary, https://www.americansforthearts.org/sites/default/files/GivingUSA_2010_ExecSummary.pdf (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | KNOWN | In a downturn a corporate co-sponsor may offer materials, equipment or services instead of cash. That helps a residency but does not fill a cash pledge | Large US companies. The arts share in GIN 2013 fell through smaller gifts; the exact share was not captured | VERIFIED (PDFs) | yes, partly: timing (risk to note) | This run: CECP PDFs, Giving USA summary |
| 18 | Business support for the arts fell 14% from 2006 to 2009. The share of businesses giving to any cause fell from 70% to 52%, and to the arts from 43% to 28%. Arts sponsorship dollars rose slightly in 2009 but fell after inflation, and the arts' share of sponsorship fell from 6% to 5% | Business Committee for the Arts 2010 survey, as reported by Americans for the Arts, https://intranet.americansforthearts.org/sites/default/files/pdf/get_involved/advocacy/research/2011/business_support11.pdf (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | NICHE | After a crash, fewer companies give to the arts at all. The pool narrows; the cheques do not just shrink | Survey design and firm sizes not checked | VERIFIED (AFTA PDF) | yes, partly: timing (risk to note) | This run: AFTA PDF |
| 19 | UK business money for culture fell four years running while trusts and foundations rose. Business: £157m (2008/09, -6%), £144.1m (2009/10, -12%; Third Sector says -11%), £134.2m (2010/11, -7%, "fourth consecutive annual fall", below 2004/05). Trusts and foundations: £135m (2008/09, -7%), £154.6m (2009/10, +11%), £170.3m (2010/11, +10%). Individuals: £382.2m (2010/11, +6%). "Corporate money is a discretionary spend". In 2009 Arts & Business warned "the worst may be yet to come, with 2010-11 being the low-point" | Arts & Business figures via WalesOnline, https://www.walesonline.co.uk/business/business-news/arts-picture-private-investors-wales-1939961 ; Museums Association, 2011, https://www.museumsassociation.org/museums-journal/news/2011/02/01032011-coprorate-giving-to-museums-falls/ and 2012, https://www.museumsassociation.org/museums-journal/news/2012/02/28022012-corporate-giving-falls/ ; Third Sector, https://www.thirdsector.co.uk/corporate-giving-arts-down-11-per-cent/fundraising/article/1051947 ; A&B Private Investment in Culture 2010/11, https://www.leanarts.org.uk/app/uploads/artsandbusiness-private-investment-in-culture10-11.pdf (accessed 9 Nov 2026) | COSPONSOR, HALFKEPT | NICHE | Over 2008/09 to 2010/11, business money fell 14.5% and trusts and foundations rose 26% (nominal, Keel arithmetic). Corporate arts money hit bottom two to three years after the share trough, the longest lag here, while a mix of funder types offset part of it | UK only, one cycle. A&B's percentages may be real while the £ figures are nominal. Read through press reports, except the 2010/11 growth table (business: rise, fall, fall, fall, fall; trusts and foundations: rise, rise, fall, rise, rise; 2006/07 to 2010/11) | VERIFIED (press reports and the A&B 2010/11 table) | yes, partly: the IPS's "during that same period" does not fit a cut that lasted until 2011 (risk to note) | This run: news pages and A&B PDF |
| 20 | Match money softened the fall. Scotland's £1-for-£1 incentive limited the sponsorship fall to 7% over 2009-10, against 17% for the UK | Culture & Business Scotland, https://cultureandbusiness.scot/new-figures-for-private-investment-in-culture-reveal-contrasting-fortunes-for-the-arts-world (accessed 9 Nov 2026) | COSPONSOR | NICHE | Laura's committed lead gift works a little like match money: co-sponsors giving alongside a fixed lead may cut less | One programme. The match effect on Laura is Keel inference | VERIFIED (page) | no | This run: Culture & Business Scotland page |
| 21 | US federal arts money first rose and was cut later. NEA appropriations: $144.7m (2008), $155.0m (2009, plus $50m Recovery Act money), $167.5m (2010), $154.69m (2011), $146.0m (2012), $138.4m (2013, sequestration), which is -17.4% from 2010 to 2013 (Keel arithmetic). In the pandemic, the NEA received $75m (CARES, 2020) and $135m (ARP, 2021) | National Endowment for the Arts, Appropriations History, https://www.arts.gov/about/appropriations-history (accessed 9 Nov 2026) | COSPONSOR | KNOWN | Public money can rise in a crash through stimulus, then be cut two to four years later in austerity, after shares have recovered | US federal. This is politics, not markets. Recovery Act money is not in the yearly figures | VERIFIED (NEA page) | yes, partly: timing (risk to note) | This run: NEA page |
| 22 | US state arts agencies cut deepest and latest. Legislative appropriations: $354.1m (FY2008), $328.8m (FY2009), $291.8m (FY2010), $272.6m (FY2011), $260.2m (FY2012, "a low point"), $277.8m (FY2013), $306.5m (FY2014), $350.6m (FY2015). That is -26.5% over FY2008-12 (Keel arithmetic; NASAA says 27%). FY2012 is the year to June 2012, about three years after the March 2009 share low. The earlier cycle ran from $449.5m (FY2001) to $279.9m (FY2004), -37.7% | NASAA, FY2016 revenues news release, https://www.nasaa-arts.org/wp-content/uploads/2017/01/NASAAFY2016SAARevenuesPressRelease.pdf ; FY2016 report, https://www.nasaa-arts.org/wp-content/uploads/2017/04/NASAAFY2016SAARevenuesReport.pdf ; FY2026 report, https://www.nasaa-arts.org/wp-content/uploads/2026/02/FY2026-State-Arts-Agency-Revenues-Report_final-updated.pdf (accessed 9 Nov 2026) | COSPONSOR | KNOWN | A public arts budget is the latest and deepest cutter: it falls for about three years after shares bottom and takes about six years to come back | US states, driven by tax revenue, not share prices | VERIFIED (release and reports) | yes, partly: timing (risk to note) | This run: NASAA PDFs |
| 23 | NASAA says why: "a built-in recovery time lag: due to the structure of public finances, state budgets take longer to rebound". After the early-1990s and early-2000s recessions, "the decrease in SAA appropriations continued several years after the recession had ended". FY2017 was still 6.7% below FY2008 in real terms. The early 2010 snapshot: state arts appropriations -10%, local government support -8%, private giving to the arts -6.5% (Americans for the Arts testimony). GIA: 2010 state -6.9%, local -8.1%, NEA up | NASAA FY2017 report, https://www.nasaa-arts.org/wp-content/uploads/2017/04/NASAA-FY2017-SAA-Revenues-Report.pdf ; Americans for the Arts testimony, 13 Apr 2010, https://www.americansforthearts.org/sites/default/files/pdf/news/press/RobertLynch_AADTestimony.pdf ; Grantmakers in the Arts, "Public Funding for the Arts: 2010 Update", https://www.giarts.org/article/public-funding-arts-2010-update (accessed 9 Nov 2026) | COSPONSOR, MOVE2031 | KNOWN | Three cycles have had the same shape: public arts money keeps falling after the recession ends | The testimony's line that arts groups run about "a year behind business trends" was seen only in part (UNVERIFIED wording) | VERIFIED (NASAA report, testimony figures, GIA page) | yes, partly: timing (risk to note) | This run: PDFs and GIA page |
| 24 | Taiwan's corporate arts sponsorship hit a record in the edition covering the crash. The 10th Wenxin Award (文馨獎, 2010) recognised about NT$2.2bn of company giving, the highest of any edition in the award's 12 years (the Executive Yuan, in Chinese) and nearly double the 1st edition's NT$1.15bn. Its 176 winners included 21 that funded rebuilding after Typhoon Morakot. The 16th (2023, covering the pandemic years) recognised NT$1,870,506,685 | Executive Yuan news, 7 Aug 2010, https://www.ey.gov.tw/Page/9277F759E41CCD91/600a82fb-fe45-495c-9012-3e600e2cc717 ; NCAF news, 2 Oct 2023, https://www.ncafroc.org.tw/news_detail.html?sid=670 ; rules of the 14th award (two-year counting window, award since 1998, every two years from the 7th), https://www.ncafroc.org.tw/files/official/%E7%AC%AC14%E5%B1%86%E6%96%87%E9%A6%A8%E7%8D%8E%E5%BE%B5%E4%BB%B6%E8%AA%AA%E6%98%8E%E6%9C%83%E7%B0%A1%E5%A0%B1%E8%AA%AA%E6%98%8E.pdf (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | NICHE | Company money for the arts in Taiwan did not visibly shrink in 2008-09, even with the TAIEX down 46% in 2008 | Award totals count only givers who apply and give at least NT$500,000, so this is not a census. That the 10th edition covered 2008-09 is Keel inference from the two-year rule of the 14th. The 9th (2008) total was not found | VERIFIED (EY and NCAF page text, the 14th's rules PDF); window is Keel inference | no | This run: search excerpts of the EY and NCAF pages; rules PDF |
| 25 | Early Wenxin editions recorded corporate arts sponsorship of over NT$1bn every year ("每年皆超過十億元"), so Taiwan's corporate arts money is a steady, sizable pool | 陳以亨, 林瑩滋 & 李星美 (2004) 企業贊助藝文活動的動機因素之研究, 輔仁管理評論 11(1): 33-52, https://www.management.fju.edu.tw/zh-tw/down.php?hFFile=tw_books_caty01331169529.pdf (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | NICHE | It gives a base for row 24's record. 60% of large firms surveyed had sponsored the arts | Before 2004. Survey of large firms | VERIFIED (PDF text) | no | This run: search excerpt of the PDF |
| 26 | The cause and year of NCAF's 41% income fall, now settled: 2015, a weak market led by Taiwan shares, after a strong 2014. Financial income was NT$283,520,045 in 2014 (88.9% of revenue) and NT$150,522,150 in 2015. The return was 2.42% against 3.59% expected, with investment losses of NT$75.6m and unrealised losses of NT$173.7m. The TAIEX fell 10.41% in 2015. Total income went from NT$318,803,033 to NT$188,860,003 | NCAF Annual Report 2015 (English), https://www.ncafroc.org.tw/files/publishBookEn/20200623/4fa69c5d236e4b53843284ca1e8553fc/4fa69c5d236e4b53843284ca1e8553fc.pdf ; CBC Annual Report 2015, https://www.cbc.gov.tw/en/public/Attachment/661517483371.PDF (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | NICHE | Taiwan's main public arts grant-maker lives on market returns. Its fund is about NT$2bn each in deposits, shares and fixed income | One foundation. This answers Q9 row 34's critique: 2014 was ordinary investment income, not a one-off | VERIFIED (annual report; CBC report) | no | This run: NCAF and CBC PDFs |
| 27 | ...but NCAF's grants ROSE that year. Grant expenses went from NT$153,598,721 (2014) to NT$160,462,639 (2015), +4.5%, and regular grants from NT$109,988,100 to NT$112,538,905, +2.3%. It ran a NT$54.7m deficit, drawn from an accumulated surplus of NT$66.1m at the end of 2014 | NCAF Annual Report 2015 (row 26 URL) (accessed 9 Nov 2026) | COSPONSOR, HALFKEPT, RESIDENCY | NICHE | Taiwan's own arts funder shields its grants from market swings with money it set aside. This is the same idea as Laura's kept half, on the funder's side | The reserve was thin (NT$66.1m), and the deeper 2011 fall used it up (row 28) | VERIFIED (annual report) | no | This run: NCAF PDF |
| 28 | NCAF in 2011: investment income was NT$14m, "more than 200 million less than projected", and total income NT$37.8m against NT$191.4m in 2010 (-80%). Yet grant-related expenses held at NT$147.7m (NT$149.1m in 2010, -0.9%), and regular grants were NT$117.5m (NT$122.5m, -4.1%). The deficit was NT$183.4m, the Council for Cultural Affairs added NT$38m, and the accumulated surplus went from NT$56.8m to -NT$126.7m. The TAIEX fell 21.18% (UNVERIFIED at TWSE) | NCAF Annual Report 2011 (English), https://www.ncafroc.org.tw/files/publishBookEn/20200623/a0a3dc5a85b64f73abac07541b4df3ac/a0a3dc5a85b64f73abac07541b4df3ac.pdf (accessed 9 Nov 2026) | COSPONSOR, RESIDENCY | NICHE | Even an 80% fall in income cut NCAF's grants by only 1-4%, because government stepped in | A private co-sponsor has no government to top it up | VERIFIED (annual report); TAIEX figure UNVERIFIED at source | no | This run: NCAF PDF |
| 29 | NCAF through 2008-09: regular grants were NT$112.9m (2007), NT$108.8m (2008, -3.6%), NT$105.7m (2009, -2.8%) and NT$122.5m (2010, +15.9%), while the TAIEX fell 46.03% in 2008 and rose 78.34% in 2009 (UNVERIFIED at TWSE) | NCAF Annual Report 2011, five-year table (row 28 URL) (accessed 9 Nov 2026) | COSPONSOR | NICHE | Taiwan's deepest modern crash cut NCAF's regular grants by about 6% over two years (Keel arithmetic), and they came back above the pre-crash level in 2010, one year after shares rebounded | Regular grants only; the 2008 and 2009 income statements were not read | VERIFIED (grants table); TAIEX UNVERIFIED at source | no | This run: NCAF PDF |
| 30 | Corporate foundations and corporate giving differ in a downturn. US corporate foundations gave +3.9% (2008) and +2.6% (2009), while CECP companies cut cash giving in 2009 | Rows 3 and 17 (Foundation Center 2011 highlights, https://carolinapublicpress.org/wp-content/uploads/2012/01/Foundation-Center-yearbook-2011.pdf ; CECP 2012, https://cecp.org/wp-content/uploads/2016/11/GIN2012_finalweb.pdf) (accessed 9 Nov 2026) | COSPONSOR, MOVE2031 | NICHE | In Taiwan many large firms give through their own foundations (Fubon and Taishin, for example, appear among Wenxin winners through their groups and foundations: Fubon news, 5 Dec 2017, https://www.fubon.com/financialholdings/en/news/news_1171207_616451.htm ; row 24 NCAF URL). A pledge from the foundation may be steadier than one from the company's marketing budget | Keel inference for Taiwan. Whether Taiwan corporate foundations hold endowments or are funded yearly by the parent was not checked (gap) | VERIFIED (US figures); Taiwan point is Keel inference | no | This run: rows 3, 17, 24 |
| 31 | The largest funders can give more in a crash. The Gates Foundation's assets fell about 20%, to $38.7bn, yet it raised its giving to $3.8bn for 2009 from $3.3bn in 2008 | New York Times, 27 Jan 2009, https://www.nytimes.com/2009/01/27/us/27gates.html (accessed 9 Nov 2026) | COSPONSOR | KNOWN | A very large endowed funder may raise its giving when others cut | An outlier with a living donor topping it up | VERIFIED (article) | no | This run: NYT article |
| 32 | In 2020 large foundations borrowed to give more. Ford, MacArthur, Mellon, Kellogg and Doris Duke committed "more than $1.7 billion within the next three years", as "new funding above the previously approved budgets", with arts and culture among the named areas, raised by "using funds from their endowment or issuing long-term debt". Ford sold $1bn of social bonds (including a 50-year bond) to pay out over 10% of its endowment in 2020-21. The Council on Foundations pledge of 19 Mar 2020 drew more than 700 signatories to loosen grant terms and pay faster | MacArthur Foundation press release, 11 Jun 2020, https://www.macfound.org/press/press-releases/five-foundations-commit-18-billion-nonprofit-organizations-wake-pandemic ; Ford Foundation, https://www.fordfoundation.org/news-and-stories/news-and-press/news/ford-foundation-announces-sale-and-pricing-of-landmark-1-billion-social-bonds/ ; Council on Foundations, http://cof.org/news/call-action-philanthropys-commitment-during-covid-19 (accessed 9 Nov 2026) | COSPONSOR | KNOWN | Large endowed foundations are the funders most able to act counter-cyclically, and the arts were included | A short crash with very cheap borrowing; not like 2008 | VERIFIED (all three pages) | no | This run: MacArthur, Ford and CoF pages |
| 33 | Q9 row 30, checked against the lags: the kept half is hit first and recovers first, and co-sponsor shortfalls come one to three years later. After the 2008 fall of 36.55%, the S&P 500 rose 25.94% and 14.82% while US foundation giving dipped (2009-10), UK business arts money fell to 2010/11, and US state arts money hit bottom in FY2012. The overlap is worst for a crash one to two years before the facility needs money (2031-32), or for a long bear market (S&P 2000-02: -9.03%, -11.85%, -21.97%) | FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt`, building paragraph); rows 1-2, 19, 22 (https://carolinapublicpress.org/wp-content/uploads/2012/01/Foundation-Center-yearbook-2011.pdf ; https://www.museumsassociation.org/museums-journal/news/2012/02/28022012-corporate-giving-falls/ ; https://www.nasaa-arts.org/wp-content/uploads/2017/01/NASAAFY2016SAARevenuesPressRelease.pdf ; accessed 9 Nov 2026); Damodaran file (prior) | HALFKEPT, CEILING, COSPONSOR, MOVE2031 | NICHE | The payments and the floor do not depend on this; only the extra flexibility does | Keel inference, not modelled. Uses the S&P, not VT, and US and UK funders, not Taiwan's. A US stock index took until about 2012 to regain its 2007 level, so "partly recovered" is the honest phrase | Keel inference | yes (risk to note, never a change): the kept half is in VT and can still be low when a co-sponsor falls short, though usually less low than at the trough | This run |
| 34 | What the lags mean for the 2031 meetings. A crash in 2029-30 would reach co-sponsors' budgets in 2031-33, when Laura meets them and the building needs money. Funders with smoothed grants (multi-year averages, a reserve such as NCAF's, large endowments, trusts and foundations, corporate foundations) are steadier than corporate sponsorship and public budget lines. Written multi-year letters before 2032 cover the lag. In-kind offers do not fill a cash gap | Rows 1-5, 8, 16-19, 22, 27, 30-32 (e.g. https://www.law.cornell.edu/uscode/text/26/4942 ; https://www.sciencedirect.com/science/article/pii/S0304405X26001480 ; accessed 9 Nov 2026); case l.109-120 (2031 range and confidence; "If Laura promises more than she can ultimately contribute, she could damage her credibility") | COSPONSOR, MOVE2031, FLOOR | KNOWN | Laura's number is steady in exactly the years others' numbers are being cut; the floor was bought in 2028. This supports W-04's timing point (store H2-057) with the lag measured by funder type | Keel inference. The case allows co-sponsors for the facility but not for the ten payments (case l.84-93); nothing here touches the payments | Keel inference | no | This run |
| 35 | The IPS's own word "later" fits co-sponsors better than "during that same period". The income paragraph says advances and fees come "later and smaller" in a recession, and that "during that same period, shares fall and co-sponsors cut their budgets". The evidence: co-sponsors do cut, but mostly a year or more after shares fall, and while shares recover | FINAL IPS, income paragraph; rows 1, 8, 16, 19, 21-23 (URLs in those rows, accessed 9 Nov 2026) | COSPONSOR, CAREER | NICHE | The Final Report can give the lag by funder type without contradicting the frozen IPS: "that same period" can be read as a recession and the years after it | Keel inference | Keel inference | yes, partly (risk to note): the IPS sentence overstates how closely the two move in time | This run |

## (b) Cards: the seven strongest ideas

### Card 1. The 5% rule and averaging: why foundation grants move late and by little
- **What is it?** US private foundations must pay out 5% of asset values averaged month by month over the year, and may
  pay it by the end of the next year (row 5). Many also set grants from multi-year averages (rows 4, 8). A crash
  therefore reaches grants a year or two later, and diluted.
- **Did it work?** Yes, in 2008-10. Assets fell 17.2% in 2008 while grants rose 5.4%; grants then fell only 2.1% in 2009
  and 0.2% in 2010 (rows 1-2), and median payout rates rose from 5.4% to 6.4% (row 4). It happened again in 2022-23:
  grants held in money terms in 2022 and fell 2.3% real in 2023 (rows 7-8).
- **How is Laura like it?** Her floor was also fixed in advance (bought in 2028), and her top is set before 2031, so she
  does not react to the market in the meeting year either.
- **How is she not?** Smoothing delays a cut but does not cancel it. A foundation that smooths still gives less two years
  later. Laura's floor never shrinks, because it is owned, not averaged.
- **What Caplet takes:** in 2031, a foundation's pledge for 2033 rests on its asset values from 2030-32, so ask
  foundation co-sponsors when their averaging window closes.

### Card 2. Foundations cut a little on average, more after losses than they add after gains
- **What is it?** Across US foundations, the response to returns is asymmetric. Payout rates fall 31-39 basis points
  after a 10% loss but rise only 10-16 after a 10% gain, and foundations do not spend more when need rises. Founder-family
  foundations cut most (row 11). Calabrese and Ely find "retrenchment" or "independence", not counter-cyclical giving
  (row 10). University endowments "hoard" after losses (row 12, though a later study disagrees).
- **Did it work?** The research is recent and peer-reviewed (Journal of Financial Economics 2026; JPART 2022).
  Estimates made in a crash overstate the cut: 2009 was forecast at -8% to -13% and first estimated at -8.4%, but
  counted at -2.1% (row 2). The store's -8.6% (H9-013) is the early figure.
- **How is Laura like it?** Laura's gift is a "lead" gift fixed at its floor; it is the opposite of a smoothed,
  asymmetric payout.
- **How is she not?** Laura is one donor with a fixed purpose. Foundations balance many grantees, and their returns move
  together (correlation 0.44), so their cuts tend to come in clusters (row 11).
- **What Caplet takes:** "co-sponsors cut their budgets" is true on average but small for foundations (a few per cent).
  The risk is concentrated in founder-led foundations, corporate sponsorship and public lines.

### Card 3. Corporate sponsors follow last year's profits, swap cash for goods, and cut for longest
- **What is it?** Corporate giving tracks profits, not share prices, with a one-year lag (row 16).
- **Did it work?** In the 2008 crash:
  - US companies held their giving in 2008, then 57-59% cut in 2009; cash fell 7.3% over 2007-09 while product
    donations rose (row 17).
  - Business support for the US arts fell 14% over 2006-09, and the share of firms giving to the arts fell from 43% to
    28% (row 18).
  - In the UK, business money for culture fell four years in a row, to 2010/11, while shares were recovering (row 19).
  - Taiwan is the exception: government-recognised corporate sponsorship hit a record of about NT$2.2bn in the edition
    covering 2008-09 (row 24). The award counts applicants only, but there is no sign of a collapse.
- **How is Laura like it?** Her own career income also comes "later and smaller" (IPS). Corporate co-sponsors follow the
  same lagged path.
- **How is she not?** A company can give equipment, services or space when cash is tight; Laura's gift is cash.
- **What Caplet takes:**
  - Corporate pledges are the ones most likely to fall short, and they fall short one to three years after a crash.
  - In-kind offers help a residency but are not cash.
  - A company's own foundation may be steadier than its marketing budget (row 30).

### Card 4. Public arts money: stimulus first, cuts later, recovery last
- **What is it?** Government arts budgets follow tax revenue and politics, not share prices.
- **Did it work?** It has been the same shape in three US cycles:
  - US state arts agencies fell 26.5% over FY2008-12, hitting bottom about three years after the share low, and
    regained their FY2008 level only around FY2015 (row 22).
  - In FY2001-04 they fell 37.7% (row 22).
  - NASAA calls this "a built-in recovery time lag" (row 23).
  - Federal NEA money rose with stimulus in 2009-10 and was cut 17.4% over 2010-13 (row 21).
  - In 2020-21 emergency federal money arrived within months (row 21).
- **How is Laura like it?** Her plan is also built to ignore market moves: "A fall in the market is not one of them."
- **How is she not?** Public budgets are cut by votes, not by market prices. In Taiwan, government stepped in to support
  NCAF in 2011 (row 28), which is the opposite of the US state pattern.
- **What Caplet takes:** a public co-sponsor's line is the slowest to fall and the slowest to come back. In 2031, ask
  whether the money is a one-off grant or a recurring budget line, and when it would next be voted.

### Card 5. NCAF: income that swings with Taiwan shares, grants held steady from reserves
- **What is it?** The National Culture and Arts Foundation lives on returns from a fund about one-third in shares.
- **Did it work?**
  - In 2015 its income fell 41% (from NT$318.8m to NT$188.9m) on a weak Taiwan market, yet grant expenses rose 4.5% and
    regular grants 2.3%. It ran a NT$54.7m deficit from its accumulated surplus (rows 26-27).
  - In 2011 income fell 80% and grants fell only 1-4%, with NT$38m from the Council for Cultural Affairs (row 28).
  - In 2008-09, with the TAIEX down 46%, regular grants fell about 6% over two years and rose above the 2007 level in
    2010 (row 29).
  - It now keeps a special reserve "to keep regular grants steady" (Q9 row 34, store Q9-034).
- **How is Laura like it?** Her kept half plays the same role for the facility that NCAF's reserve plays for its grants:
  money held apart so that a bad year does not reach a promise.
- **How is she not?**
  - NCAF's reserve was thin and ran out in 2011, and government covered the gap; Laura has no one to cover her.
  - Laura's promises (the payments and the floor) are bought in Treasuries, not drawn from a reserve.
- **What Caplet takes:**
  - The 41% figure in Q9 row 34 is settled: it was a market-driven income fall in 2015 that did not reach grants.
  - Taiwan's main public arts funder already practises the idea behind the kept half.
  - If NCAF is a co-sponsor, its grant level is among the steadiest on offer, though its pledges are yearly.

### Card 6. Who gives more when shares fall
- **What is it?** These funders are counter-cyclical, or at least steadier than shares:
  - very large endowed foundations;
  - funders with smoothing rules;
  - trusts and foundations;
  - foundations giving very large single grants.
- **Did it work?**
  - Gates raised its giving to $3.8bn for 2009 after a 20% asset fall (row 31).
  - In 2020 five foundations committed more than $1.7bn above approved budgets, partly borrowed (Ford sold $1bn of
    bonds), with the arts among the named areas (row 32).
  - UK trusts and foundations rose 26% over 2008/09 to 2010/11 while business fell (row 19).
  - US corporate foundations gave more in 2009 (row 3).
  - Million-dollar foundation gifts "tend to be countercyclical" (row 13).
  - Match money halved the sponsorship fall in Scotland (row 20).
- **How is Laura like it?** Her floor is counter-cyclical in effect: it is worth most in the years others give less
  (store H2-057).
- **How is she not?** These funders choose to step up and can choose otherwise next time; Laura's floor is owned.
- **What Caplet takes:** a co-sponsor list weighted towards large endowed and smoothed funders is more robust to a
  2029-32 crash than one weighted towards corporate sponsorship or public budget lines.

### Card 7. What the lag means for the kept half and the 2031 meetings
- **What is it?** Shares fall first and recover first; co-sponsor cuts come one to three years later (rows 33, 35).
- **Did it work?** In 2008-12, the S&P 500 fell 36.55% and then rose 25.94% and 14.82%, while:
  - US foundation giving dipped in 2009-10;
  - UK business arts money fell until 2010/11;
  - US state arts money hit bottom in FY2012.
  The kept half would have been lowest in early 2009 and partly recovered by the time the deepest cuts arrived.
- **How is Laura like it?** The IPS names "a co-sponsor falling short" as a use of the kept half, and the lag means the
  kept half is usually not at its lowest when that happens.
- **How is she not?** The overlap is real in two cases: a crash in 2031-32, just before the 2033 building money is
  needed, or a long bear market like 2000-02. Then both are low at once (Q9 row 30).
- **What Caplet takes:**
  - The risk to note is "partial and lagged overlap", not "smallest exactly when".
  - A 2029-30 crash would land on co-sponsors in the 2031 meeting years, while Laura's floor is already owned and her top
    half already moved. Her number is the steady one in the room.
  - In 2031, prefer signed multi-year commitments and smoothed funders.

## (c) What would surprise a judge
1. **US foundation giving rose in the crash year.** Assets fell 17.2% in 2008, but giving rose 5.4%. The 2009 fall,
   forecast at 8-13% and first estimated at 8.4%, was counted at 2.1% (rows 1-2). Most teams will write "foundations
   cut when markets fall"; the record says "later, and by a little".
2. **Taiwan's main arts funder already keeps a kept half.** NCAF's income fell 41% in 2015 and 80% in 2011, yet its
   grants rose 4.5% in 2015 and fell under 1% in 2011, paid from reserves and a government top-up. It now keeps a
   special reserve "to keep regular grants steady" (rows 26-28; Q9-034).
3. **The cuts land while shares recover.** In the UK, business money for culture fell for the fourth year running in
   2010/11, and US state arts money hit bottom in FY2012, after the S&P had already risen 25.94% and 14.82%
   (rows 19, 22). Public arts money took about six years to come back (row 22).
4. **Taiwan's corporate arts sponsorship hit a record in the edition covering 2008-09**, about NT$2.2bn, nearly double
   the first edition's (row 24). Taiwan is not the US.
5. **The mix matters more than the average.** Over 2008/09 to 2010/11, UK trusts and foundations gave 26% more while
   business gave 14.5% less (row 19). A co-sponsor plan's risk depends on who the co-sponsors are.

## (d) Gaps (what I could not verify)
- Wenxin Award totals for the 9th (2008) and 11th (2013) editions were not found. That the 10th edition counted 2008-09
  is inferred from the 14th edition's two-year rule. Award totals count only applicants of NT$500,000 or more.
- No series was found for Taiwan corporate-foundation giving, or for whether Taiwan corporate foundations hold their
  own endowments or are funded yearly by the parent company.
- No Taiwan central or local culture budget series for 2008-10 or 2011 was read (only the 2024 Ministry of Culture
  budget, +32% to NT$26.866bn, which is not a downturn year).
- Taiwan's rules on how much a foundation must pay out each year were not checked.
- NCAF's 2008 and 2009 income statements were not read; only the 2011 report's five-year grants table and balance
  sheet.
- The TAIEX figures for 2008, 2009 and 2011 come from a secondary table, not from TWSE.
- The Americans for the Arts testimony line on arts groups being about "a year behind business trends" was seen only
  in part.
- The arts share in CECP's Giving in Numbers 2013 was not captured.
- Arts & Business UK figures were read through press reports, except the 2010/11 growth table. Whether A&B's
  percentages are real or nominal was not checked.
- Rosen et al. (2019) was read only through a Consensus abstract, and its full citation was not checked.
- No evidence was found on co-sponsorship pledges for buildings specifically: how often signed capital pledges to arts
  facilities were reduced or delayed after 2008. (The store's H7-070 on failed pledges is related, but not by funder
  type.)
- No modelling: the overlap between the kept half and co-sponsor shortfalls (row 33) is reasoned from historical
  timing, not simulated on VT paths.
