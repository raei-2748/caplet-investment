(Keel is a simulated team, AI-written.)

# Tess, research note: P4 of FINAL (V57), two sentences
Read 4 Nov 2026 (Sydney). Huddle H-029, round 1. Fiction; the sources are real and were fetched today.

## Summary
| Line | Verdict | Fix |
|---|---|---|
| (a) "Shares are called safe over ten years, but time makes a loss rarer, not smaller, and a fixed cheque can't wait for a recovery." | TRUE IF | "not smaller" to "not cheaper to insure" |
| (b1) "Her 2028 deposit comes from book advances, speaking fees and licensing, which tend to dry up in the same downturns that hit share prices." | TRUE IF | "tend to dry up" to "can dry up"; the evidence covers speaking income in one shock (2020), not advances or licensing |
| (b2) "Her income already rides on shares, so her portfolio shouldn't bet on them twice." | FALSE as written | No word fix keeps the claim as a fact. The case says nothing about what her income rides on. |

The "fixed cheque can't wait for a recovery" clause is the case's own logic (ten fixed payments, 2033-2042) and is not tested here.

## Sources read
### Case text (the client profile)
File: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (repo text copy of the case; the PDF in the brief was not re-opened).

Quote, lines 43-45, near-verbatim from the repo text:
> "At the beginning of 2027, Laura plans to invest $300,000 with an asset management firm. She will contribute an additional $150,000 at the beginning of 2028, using earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial ventures."

Also, lines 61-65:
> "Laura's living expenses and short-term financial needs will be covered by income and financial resources outside the portfolio. Apart from the two contributions described above, she will neither add to nor withdraw from the portfolio before 2033."

What the case says about the 2028 money:
- It is a plan ("plans to invest"; "will contribute"). The case does not say the money is certain, and it does not say the money is at risk.
- It names the source as "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures." The IPS line drops "other entrepreneurial ventures" and changes "engagements" to "fees." That is a fact-of-wording point for the team, not one of my verdicts.
- The case says nothing about downturns, share prices, or whether her income moves with markets.

### (a) Zvi Bodie, "On the Risk of Stocks in the Long Run," Financial Analysts Journal, 1995
- Source: CFA Institute Research Foundation page, https://rpc.cfainstitute.org/research/financial-analysts-journal/1995/on-the-risk-of-stocks-in-the-long-run (read 4 Nov 2026, via fetch tool). Only the abstract opened; the full article is for CFA members.
- Quotes (near-verbatim, via fetch tool):
  > "A familiar proposition is that investing in common stocks is less risky the longer an investor plans to hold them."
  > "[I]f this proposition were true, then the cost of insuring against earning less than the risk-free rate of interest should decline as the investment horizon lengthens."
  > "This paper shows that the opposite is true, even if stock returns are mean reverting in the long run."
  > "For guarantors of money-fixed annuities, the proposition that stocks in their portfolios are a better hedge the longer the maturity is unambiguously wrong."
- Mechanism, two plain sentences: the familiar claim is that stocks get safer with time. Bodie measures risk as the cost of insuring against a shortfall below the risk-free rate, and finds that cost does not fall with time; it rises.
- Sentence tested: "time makes a loss rarer, not smaller."
- Where it breaks: the abstract never addresses how likely a loss is (the probability). It does not say "rarer." "Rarer" is the familiar claim Bodie is arguing against, so it cannot be cited from this paper. What the paper supports is "not cheaper to insure," which is stronger than "not smaller."
- Verdict: TRUE IF. Condition: "rarer" holds only if it means the chance of a loss is lower, which Bodie does not test; what he finds is that the cost of protection does not fall. Smallest fix: "time makes a loss rarer, not smaller" to "time makes a loss rarer, not cheaper to insure."

### (a) Liang Zou, "Investments with Downside Insurance and the Issue of Time Diversification," Financial Analysts Journal, Vol. 53 No. 4, 1 July 1997, pp. 73-79, doi:10.2469/faj.v53.n4.2102
- Source: CFA Institute Research Foundation page, https://rpc.cfainstitute.org/research/financial-analysts-journal/1997/investments-with-downside-insurance-and-the-issue-of-time-diversification (read 4 Nov 2026, via fetch tool).
- Quotes (near-verbatim, via fetch tool):
  > "the degree of risk is not a monotonic function of the policy's time horizon"
  > "the cost of such insurance peaks at a finite time horizon."
  > "The peak is typically between 5 and 15 years."
  > "although a 5-year insurance policy can be much riskier than a 1-year policy, it can also be riskier than a 30-year policy."
- Mechanism: the cost of insuring a stock portfolio against a shortfall rises to a peak and then falls, so the cost is not a simple function of horizon. The peak sits in the 5 to 15 year range.
- Sentence tested: "not smaller," at ten years.
- Where it breaks: at ten years the cost is in the peak range, so "not smaller" holds at ten years in Zou's model. But past about 15 years the cost falls. So "not smaller" is a claim about the ten-year window, not about time in general. That supports keeping ten years in the sentence.
- Verdict: supports the ten-year wording, consistent with TRUE IF above.

### (a) Samuelson on time diversification (search and fetch)
- Samuelson's own paper was not opened. The SOA article below quotes its conditions.
- Source: Rowland Davis, "The Myth of 'The Myth of Time Diversification'," Risks & Rewards (Society of Actuaries), Issue 64, August 2014, pp. 23-25, https://www.soa.org/4935b6/globalassets/assets/library/newsletters/risks-and-rewards/2014/august/rar-2014-iss64-davis.pdf (read 4 Nov 2026, via fetch tool).
- Quotes (near-verbatim, via fetch tool): Samuelson's proof "only holds with those conditions in place." Davis writes that "Samuelson never said anything different" when risk is measured by more complicated metrics than terminal wealth.
- Verdict note: the time-diversification claim is conditional. That supports the TRUE IF on line (a), not a flat TRUE.
- Also: The SLCG practice note, https://www.slcg.com/files/practice-notes/time-diversification.pdf (read 4 Nov 2026, via fetch tool), says "Time diversification is the belief that risk declines over longer investment horizons," and "if returns are not negatively serially correlated, investment risk does not decline over longer horizons." It gives no loss-probability or guarantee-cost figures.

### (b1) Book advances, speaking fees and licensing in downturns
Searched for evidence that these income streams fall in recessions or bear markets. Results:

1. Authors Guild, "Authors Guild Survey Shows Drastic 42 Percent Decline in Authors Earnings in Last Decade," https://authorsguild.org/news/authors-guild-survey-shows-drastic-42-percent-decline-in-authors-earnings-in-last-decade/ (read 4 Nov 2026, via fetch tool; undated on the page).
   - Quotes (near-verbatim, via fetch tool): "a median of $6,080 in 2017, down 42 percent from 2009." Book-related income: "declining 21 percent to $3,100 in 2017 from $3,900 in 2013."
   - Causes named: "the growing dominance of Amazon over the marketplace," "lower royalties and advances for mid-list books," "the blockbuster mentality of publishers who grant celebrity writers massive advances."
   - The page does not mention recessions or the 2008-09 downturn. It uses 2009 only as a comparison year. The fall is a structural trend, not a cycle.
   - Verdict relevance: no support for "dry up in the same downturns."

2. Authors Guild, "COVID-19 Survey 3: Summary of Responses," https://authorsguild.org/news/authors-guild-covid-19-survey-3-summary-of-responses/ (read 4 Nov 2026, via fetch tool). Dated 18 Feb 2021 on the page.
   - Quotes (near-verbatim, via fetch tool): "71.4% reported that their income (from any source) had declined since the crisis began." "46.3% reported losing income from speaking engagement cancellations." "12.9% reported losing income due to book contract cancellations or payment delays." "21.6% reported losing income due to loss of book sales or revenue through self-publishing."
   - The page does not mention advances or licensing by name. "Book contract cancellations or payment delays" is the nearest to advances, and it is a guess at the match.
   - This is the best evidence in the search: speaking income was hit hardest in the 2020 shock. But it is one pandemic shock, it is a survey of authors who chose to respond, and it is not a bear market.

3. Meeting cancellations 2008-09 (MPI and American Express survey), https://www.businesstravelnews.com/Corporate-Meetings-News/MPI-Amex-Survey-Meeting-Cancellations-Limited-Budgets-Underscore-Downturn (read 4 Nov 2026, via fetch tool; undated).
   - Quotes (near-verbatim, via fetch tool): "organizations on average cancelled more than four meetings in the second half of 2008 and an additional 3.4 this year."
   - The page does not mention speakers or speaker fees. It is indirect evidence that corporate events fell in 2008-09. It does not show speaking fees falling.

4. Speakers Corner, https://www.speakerscorner.co.uk/news/forecasting-trends-with-speakernomics (read 4 Nov 2026, via fetch tool): no speaker-fee data, no downturn figures. Not used.

- Verdict for "tend to dry up in the same downturns that hit share prices": TRUE IF. Condition: only speaking income is supported, and only in one shock (2020), where the 2020 survey shows 46.3% of respondents lost speaking income. There is no source for advances or licensing falling in a bear market, and the 2008-09 evidence is about corporate meetings, not speaker fees. Smallest fix: "which tend to dry up" to "which can dry up."

### (b2) The human-capital idea
- Source: CFA Institute Research Foundation, Ibbotson, Milevsky, Chen and Zhu, "Lifetime Financial Advice: Human Capital, Asset Allocation, and Insurance" (2007), https://rpc.cfainstitute.org/research/foundation/2007/lifetime-financial-advice-human-capital-asset-allocation-and-insurance (read 4 Nov 2026, via fetch tool). Abstract only. The PDF link (https://rpc.cfainstitute.org/-/media/documents/book/rf-publication/2007/rf-v2007-n1-4580-pdf.pdf) was not opened.
- Quotes (near-verbatim, via fetch tool): "individuals must consider more than the risk-return trade-off of financial assets"; they "must take into account human capital and mortality risk in the earlier life-cycle stages."
- The abstract does not say whether human capital is correlated with equity markets, and it does not say human capital is valued like a bond. I could not open the full text, so the claim that earnings are bond-like, or any statement about correlation with shares, is UNVERIFIED.
- Verdict for "Her income already rides on shares": FALSE as written. The case says nothing about what her income is linked to. The book supports the general idea that human capital matters for allocation, not that a particular person's income rides on shares. Smallest true fix, if the team keeps the point: "Her income already rides on shares" to "Her income may move with markets." That is a hedge, and it still needs the speaking evidence above to stand.

## URLs tried
Fetched successfully (4 Nov 2026):
1. https://rpc.cfainstitute.org/research/financial-analysts-journal/1995/on-the-risk-of-stocks-in-the-long-run (abstract only)
2. https://rpc.cfainstitute.org/research/financial-analysts-journal/1997/investments-with-downside-insurance-and-the-issue-of-time-diversification
3. https://rpc.cfainstitute.org/research/foundation/2007/lifetime-financial-advice-human-capital-asset-allocation-and-insurance (abstract only)
4. https://www.slcg.com/files/practice-notes/time-diversification.pdf
5. https://www.soa.org/4935b6/globalassets/assets/library/newsletters/risks-and-rewards/2014/august/rar-2014-iss64-davis.pdf
6. https://authorsguild.org/news/authors-guild-survey-shows-drastic-42-percent-decline-in-authors-earnings-in-last-decade/
7. https://authorsguild.org/news/authors-guild-covid-19-survey-3-summary-of-responses/
8. https://www.businesstravelnews.com/Corporate-Meetings-News/MPI-Amex-Survey-Meeting-Cancellations-Limited-Budgets-Underscore-Downturn
9. https://www.speakerscorner.co.uk/news/forecasting-trends-with-speakernomics (no relevant content)

Search results seen but not fetched (so not evidence):
- https://en.wikipedia.org/wiki/Zvi_Bodie
- https://rpc.cfainstitute.org/research/financial-analysts-journal/1996/on-the-risk-of-stocks-in-the-long-run-a-comment and the 1996 resolution and note pages (Bodie debate; not opened)
- https://thinkadvisor.com/2012/04/25/milevsky-how-much-in-risky-stocks-vs-safe-cash (not opened)
- https://www.publishersweekly.com/pw/print/20190211/79224-how-do-we-get-through-such-difficult-times-for-authors.html (not opened)
- https://www.thespeakerlab.com/blog/recession-benefit-speaking-business/ (search hit only; not opened)

Not opened (UNVERIFIED): Samuelson's 1963/1969 papers; the full Bodie 1995 article (members only); the full Ibbotson et al. 2007 text; any source on advance or licensing income in 2008-09 or in bear markets.

## Notes for the team
- The 2020 survey is a pandemic shock. Share prices fell too in March 2020, but the survey does not measure that. "Same downturns" needs the team to decide whether a pandemic counts.
- "Rarer" in (a) comes from the familiar claim that Bodie argues against. The cleanest line the paper supports is "not cheaper to insure."
