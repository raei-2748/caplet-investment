# Q19 research cards: the 2031 range as one rule, and its confidence

Tue 10 Nov 2026 Sydney. Notes for the Final Report store, not report prose. Feeds SKELETON 3c (300 words), 3d
(250 words), Exhibit 3 and 3e.

Checked against Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.3 and l.15), the locked TNA
(l.21 through CANON A29), `keel/final_report/CANON.md` (A22, A29-A32, C5, C6, D1, D12), `keel/final_report/NUMBERS.md`
sections 3 and 4, the case (l.108-124: "communicate a credible range", "state how confident they are that her 2033
contribution will fall within that range", "explain how favorable and unfavorable market outcomes could affect the
amount", "must also protect the portfolio's ability to fund the ten-year operating commitment"), and the 9 Nov bond
desk and co-sponsor judges (`research/panel/2026-11-09_judge_bond_desk.md`, `..._judge_cosponsor.md`). The plan is
frozen: a "yes" or "risk" in the Clash column is a risk to record, never a change to the strategy.

Every number below is MODEL unless a source says otherwise. Engine: `keel/final_report/numbers/range_rule.py`
(imports `engine.py` and `plan.py`, 6 Nov 2026 Treasury curve, Keel's margin $21,149, 200,000 house paths with seed
2033, 1,770 US stock windows since 1871, 585 joint rate-and-stock windows 1962-2010), output
`keel/final_report/numbers/results_range_rule.json` (keys named in each row). Run: `python3 -I
keel/final_report/numbers/range_rule.py` (about 3 seconds). Rounding is down to $5,000 unless stated.

**Claims tested**
1. Per-end deductions give a central stated range of $110,000 to $130,000 (bond desk: $115,929 x 0.959 + $22,806 x
   0.975 = $133,412, rounded down).
2. With the cap (the 2033 contribution is the lower of what the floor and moved half pay and the stated top; any
   excess joins the kept half, CANON D12) the gift lands inside the range in every house path and history window, so
   the confidence is "certain barring a US default or a fund failing to work as its prospectus says".
3. A range rather than one figure, with the top perhaps offered on terms (a match or a challenge).
4. Bond desk: keeping the bottom at the floor after the move, about $23,000 below money owned, under-signals.
5. The range Laura can announce in 2031 is uncertain from today at both ends (bottom about $93k-$140k, top about
   $111k-$171k), and one confidence number can be stated with its assumptions and three things that would lower it.
6. Exhibit 3 data: the announcement under several markets and named history windows, and the narrowing 2028 to 2031
   to 2033.
7. Forecast-communication prior art the store lacks.

**Problem class:** a staged commitment under uncertainty with one promisor and several later funders, where the
promisor removes market risk before speaking. Prior art from four fields: fixed income (what a fund pays if
reinvestment earns nothing), fundraising field experiments (matching against announced lead money), foundation
practice (challenge grants for buildings), and forecast communication (how ranges, bounds and fan charts are read).

**Already held, not repeated:** Q6 (how far to trust 7.5%); Q11a rows 6-11 (lead gift against match, Huck & Rasul
2011 and Huck, Rasul & Shephard 2015, crowd-out), rows 31-35 (van der Bles et al. 2020 at abstract level, Joslyn &
LeClerc 2012, Du et al. 2011, Ciconte et al. 2014, Call et al.); Q11b row 27 (Kresge's 20-50% readiness test);
Q18 rows 1 and 5-7 (a market-set top is not a condition; CASE counts documented pledges at face value and a
match-conditional pledge only once met) and row 32 (the "make available up to" wording). Store items upgraded here:
H3-110 and H9-133 (Karlan & List 2007, now read at source), H9-144 (Bernanke review, now read at the Bank of England's
own PDF), H5-017 (the match idea, now tested and refused).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Each end has its own deduction: the floor fund bought in Jan 2028 pays 4.14% less if no distribution is paid and its final cash earns nothing; the half moved in Jan 2031 pays 2.45% less. With IBTM's actual 3.50% coupon: 3.85% and 2.44%. If reinvestment runs 3 points below forwards instead of zero: 2.61% and 1.49% | Keel engine, `numbers/range_rule.py`, `results_range_rule.json` key `deductions`; floor $115,929 and moved half $22,806 from NUMBERS section 4 | FLOOR, CEILING, MOVE2031, PROCESS | NICHE | Bottom = $115,929 x (1 - 4.14%) = $111,134, down to $110,000. Top = that plus $22,806 x (1 - 2.45%) = $133,383, down to $130,000. Both ends are money that exists even if interest stops for five years | Zero interest for five years is a test of ownership, not a forecast; it makes each end "owned", which is what the IPS promises | VERIFIED: re-derived on the engine (MODEL) | no (IPS l.15: the bottom is "built on the ever-reliable Treasuries"; "whatever figure you choose is money you already own") | this card's engine run, 10 Nov |
| 2 | The bond desk's arithmetic reproduces exactly: $115,929 x 0.959 + $22,806 x 0.975 = $133,412, which rounds down to $130,000. NUMBERS section 4's older top of $135,000 (the sum less 2.5%) is $1,588 more than is owned in the zero-interest test | Keel engine, `results_range_rule.json` keys `central.bond_desk_arithmetic`, `central.numbers_s4_old_top_less_2.5pct`; bond desk judge 9 Nov, weakness 2 | CEILING, FLOOR | NICHE | The stated top in the register should be $130,000, not $135,000 | Only the register is affected, not the plan | VERIFIED: re-derived on the engine (MODEL) | risk: NUMBERS section 4 carries $135,000; the lead must change it | bond desk panel; this run |
| 3 | The deduction depends on the yield at which each fund is bought, so it must be computed then, not fixed today. Floor deduction at a yield shift of -2 / 0 / +1 / +2 points: 2.03% / 4.14% / 5.36% / 6.68%; moved half 1.42% / 2.45% / 2.98% / 3.53%. A fixed 4.1% is too small whenever the floor is bought above today's forwards (51% of house paths); with fixed 4.1% and 2.5%, the zero-interest value falls below the stated top in 13.75% of house paths (median $890, 1-in-20 $3,326, worst $11,225) and below the stated bottom in 12.7% | Keel engine, `results_range_rule.json` keys `deductions.by_parallel_yield_shift`, `house.fixed` | FLOOR, CEILING, PROCESS | NICHE | The rule names a method, not a percentage: "the payout if no further interest is earned, at the yield the fund was bought at". By Jan 2028 the floor's figure is a known fact; by Jan 2031 the moved half's is | Higher yields lift the payout more than they lift the deduction, so the stated ends still rise with yields | VERIFIED: re-derived on the engine (MODEL) | no (method only; IPS unchanged) | this run |
| 4 | Counting only losses from 2031 on (distributions already received in 2028-2030 kept as cash) gives a floor deduction of 3.27% instead of 4.14%; at $5,000 rounding the central range is the same $110,000-$130,000; at $1,000 rounding it is $112,000-$134,000 instead of $111,000-$133,000 | Keel engine, `results_range_rule.json` keys `deductions.floor_bought_jan2028.zero_from_2031`, `central.rounded_to_1000_instead` | FLOOR, PROCESS | NICHE | Not worth the extra sentence: about $1,000 more, and it depends on Laura keeping three years of distributions as cash | Keel's call: the 2028 rule | VERIFIED: re-derived on the engine (MODEL) | no | this run |
| 5 | With the cap, the gift lands inside the range in every modelled path: the payout is above the stated top in 100% of 200,000 house paths, 1,770 stock windows and 585 joint windows, so the gift equals the top every time; none is below the bottom, and none breaches the zero-interest test | Keel engine, `results_range_rule.json` keys `house.2028`, `history_stocks`, `history_joint_rates_and_stocks` | CEILING, CERTAINTY, HALFKEPT | NICHE | The confidence is certain by construction: every dollar of the range is owned in Treasury funds before it is stated. The real uncertainty is which range she can state (row 7), not whether the gift lands in it | The 100% is a property of the rule, not a market forecast; it excludes a US default and a fund not paying its net asset value, which no model here prices | VERIFIED: re-derived on the engine (MODEL) | no (IPS l.15 "money you already own"; CANON D12) | this run |
| 6 | What the cap sends to the kept half: excess p5 / p50 / p95 $4,211 / $7,965 / $12,387 in the house model (mean $8,085); $5,655 / $7,775 / $10,193 in stock history; $3,790 / $7,882 / $14,627 in joint history. Kept half plus excess on 1 Jan 2033: $18,883 / $31,995 / $55,933 (house); central case $23,986 + $8,735 = $32,721 | Keel engine, `results_range_rule.json` keys `house.2028.excess_p5_p50_p95`, `kept_plus_excess_p5_p50_p95`, `central.2028` | HALFKEPT, CEILING | NICHE | The excess is the interest the zero test set aside, returned to Laura's flexibility; it is never part of the promise | Small next to the kept half; worth one clause in 3b | VERIFIED: re-derived on the engine (MODEL) | no (CANON D12: excess joins the kept half) | this run |
| 7 | Seen from today, the range Laura will be able to state is uncertain at both ends (house model, 1-in-20 each side): stated bottom $90,000 / $110,000 / $130,000; stated top $105,000 / $130,000 / $160,000; width $15,000 / $20,000 / $40,000. Chance the stated top is at least $100k 98.5%, $110k 93.6%, $120k 81.0%, $130k 59.6%, $140k 35.5%, $150k 16.8%. Chance the stated bottom is at least $90k 95.4%, $100k 81.4%, $110k 53.5%, $120k 23.6%, $130k 6.5% | Keel engine, `results_range_rule.json` keys `house.2028.stated_*`, `P_stated_top_at_least`, `P_stated_bottom_at_least` | FLOOR, CEILING, CERTAINTY | NICHE | This is where "favorable and unfavorable market outcomes" (case l.120-121) live: before 2031, rates set the bottom and shares set the top; after the move, nothing moves the range | The bottom's spread comes from the Jan 2028 Treasury yield alone (the floor amount is fixed); NUMBERS' "bottom $93k-$140k, top $111k-$171k" were payouts, these are stated figures after deductions and rounding | VERIFIED: re-derived on the engine (MODEL) | no (IPS l.15: markets move "the top of your planned band ... but the bottom will remain constant" after it is bought) | this run |
| 8 | On US stock history with yields at today's forwards, the bottom is $110,000 in every window and the top is $125,000 / $130,000 / $145,000 (p5 / p50 / p95); the lowest top is $110,000 (shares bought Jul 1929), where the range collapses to one figure. In the joint replay (rates and shares from the same months) the bottom is $95,000 / $110,000 / $125,000 and the top about $111,000 / $130,000 / $155,000 (p5 falls between two $5,000 steps) | Keel engine, `results_range_rule.json` keys `history_stocks`, `history_joint_rates_and_stocks` | FLOOR, CEILING | NICHE | Even 1929 leaves a $110,000 commitment the IPS's floor already owns | Joint replay covers 1962-2010 only; it uses one-year Treasury yields scaled to today's curve | VERIFIED: re-derived on the engine (MODEL) | no | this run |
| 9 | The range narrows on a timetable: today (house, 1-in-20) bottom $90k-$130k, top $105k-$160k; Jan 2028 (floor bought, central yields) bottom fixed at $110,000, top $120,000 / $130,000 / $145,000; Jan 2031 (half moved) $110,000-$130,000, nothing left to move it; Dec 2032 gift $130,000, excess $8,735, kept half plus excess $32,721 | Keel engine, `results_range_rule.json` key `narrowing` | FLOOR, CEILING, MOVE2031, COMPLETE2028 | NICHE | A dated table of what is known when: the same shape as a fan that closes to a line at the move | Central path; the 2028 row fixes yields at forwards | VERIFIED: re-derived on the engine (MODEL) | no (IPS l.15 sequence: floor, then the move "before you meet co-sponsors in 2031") | this run |
| 10 | Stating the figures before the move breaks the guarantee in some paths: if the top is announced 1 / 3 / 6 / 12 months before the move, the top is not fully owned in the zero-interest test in 8.0% / 12.0% / 14.4% / 15.9% of house paths; shortfall median $575 / $919 / $1,247 / $1,647, 1-in-20 $2,182 / $3,554 / $4,754 / $6,233 | Keel engine, `results_range_rule.json` key `stated_before_move` | MOVE2031, CEILING, PROCESS | NICHE | The rule needs an order: move first, then state. The IPS already says the move comes "Before you meet co-sponsors in 2031" | Central-path figures are smaller at short gaps (0.06% at one month) because the central path starts with headroom from rounding | VERIFIED: re-derived on the engine (MODEL) | no (it is the IPS's own order) | this run |
| 11 | When rates and shares fall together (joint replay), the ten payments fall short in 5.98% of windows (35 of 585; window starts Feb 2006 to Nov 2008 plus Nov 2000, so in effect one episode); shortfall median $7,263, worst $12,117. The cap's excess alone covers 40% of these; excess plus kept half covers 100%. If the shortfall were paid from the facility money instead, the gift would still be at or above the stated bottom in 100% (at least $6,801 above it) and at the stated top in 40% | Keel engine, `results_range_rule.json` key `history_joint_rates_and_stocks.where_payments_short` | REINVEST, RESERVE2033, CERTAINTY, HALFKEPT | NICHE | The range survives the worst replay; what is at stake is whether the gift is the top or a little below it | The kept half's three named uses (IPS l.15) do not include the payments; joint stress itself is card Q24's subject | VERIFIED: re-derived on the engine (MODEL) | risk: drawing on the kept half or the gift for the payments is not in the IPS; record as a limit in 3e | this run |
| 12 | Three ways to state the range after the move: A, the IPS band ($110,000-$130,000; gift $130,000; excess $8,735); C, narrowed to what is owned ($130,000-$135,000; gift $135,000; excess $3,735); D, one figure "at least $130,000". In the house model C raises the committed bottom by $15,000 / $20,000 / $40,000 (p5 / p50 / p95) and cuts the excess to $248 / $2,490 / $4,751 | Keel engine, `results_range_rule.json` keys `framing_options_central`, `framing_options_house_p5_p50_p95`, `framing_options_house_counted_gain_C_over_A` | COSPONSOR, FLOOR, CEILING, MOVE2031 | NICHE | Co-sponsors count only what is committed in writing at face value (Q18 rows 5-7), so the committed figure is the lever | C changes the IPS's bottom; D drops the range the case asks for | VERIFIED: re-derived on the engine (MODEL) | C: yes, IPS l.15 "the bottom will remain constant"; D: risk, the case asks for a range (l.108-118) | this run |
| 13 | Rounding to $1,000 instead of $5,000 gives $111,000-$133,000; the excess falls from $8,735 to $5,735 in the central case | Keel engine, `results_range_rule.json` key `central.rounded_to_1000_instead` | PROCESS, CEILING | KNOWN | $5,000 steps read as a plan, not false precision | Rounding gives up $3,000 of stated top, which goes to the kept half | VERIFIED: re-derived on the engine (MODEL) | no | this run |
| 14 | A match offer in a mail appeal to over 50,000 prior donors raised revenue per letter by 19% and the chance of giving by 22%; 2:1 and 3:1 matches did no better than 1:1; the effect was concentrated in states that voted for Bush in 2004 | Karlan, D., & List, J. A. (2007). Does price matter in charitable giving? Evidence from a large-scale natural field experiment. *American Economic Review, 97*(5), 1774-1793. https://doi.org/10.1257/aer.97.5.1774 (abstract at https://www.aeaweb.org/articles?id=10.1257/aer.97.5.1774; text at https://isps.yale.edu/sites/default/files/publication/2012/12/AER,%202007,%20Karlan,%20DoesPriceMatter.pdf; Bush-state result in NBER w12338, https://www.nber.org/system/files/working_papers/w12338/w12338.pdf; accessed 10 Nov 2026) | FUNDRAISING, COSPONSOR, CEILING | KNOWN | The best-known evidence for matches comes from small donors answering a letter, not from institutions co-funding a building | One charity, one mailing; heterogeneous; no effect from a bigger ratio | VERIFIED at source (AER abstract page and paper text); Crossref record shows no correction or retraction (checked 10 Nov) | risk: a match would make part of Laura's owned money depend on co-sponsors' acts | upgrades store H3-110, H9-133 |
| 15 | A follow-up natural field experiment found "only weak evidence that either of the matches work" ($1:$1 and $1:$3); prior supporters respond, lapsed givers do not or respond badly | Karlan, D., List, J. A., & Shafir, E. (2011). Small matches and charitable giving: Evidence from a natural field experiment. *Journal of Public Economics, 95*(5-6), 344-350. https://doi.org/10.1016/j.jpubeco.2010.11.024 (read at https://www.sciencedirect.com/science/article/abs/pii/S0047272710001842 and https://ideas.repec.org/a/eee/pubeco/v95y2011i5-6p344-350.html, accessed 10 Nov 2026) | FUNDRAISING, COSPONSOR | KNOWN | The match effect does not replicate reliably even among small donors | Small-donor mail again; the authors report imbalance across some cells | VERIFIED at source (abstract and highlights); Crossref: no correction or retraction | no | new |
| 16 | In the lab, people gave significantly more when a subsidy was framed as a match than as an equal-value rebate | Eckel, C. C., & Grossman, P. J. (2003). Rebate versus matching: Does how we subsidize charitable contributions matter? *Journal of Public Economics, 87*(3-4), 681-701. https://doi.org/10.1016/S0047-2727(01)00094-9 (read at https://www.sciencedirect.com/science/article/abs/pii/S0047272701000949, accessed 10 Nov 2026) | FUNDRAISING | KNOWN | Framing moves small donors; it says nothing about how a co-funding institution reads a founder's conditional money | Lab subjects giving lab money | VERIFIED at source (abstract); Crossref: no correction or retraction | no | new |
| 17 | The same comparison in Minnesota Public Radio's mailed fund drives (Dec 2001 to Nov 2002): a match raised more money for the charity than an equal rebate; a later review summarises both papers as "offering donors a match has a bigger effect on the total amount of money going to the charity than offering a rebate of equivalent value" | Eckel, C. C., & Grossman, P. J. (2008). Subsidizing charitable contributions: A natural field experiment comparing matching and rebate subsidies. *Experimental Economics, 11*(3), 234-252. https://doi.org/10.1007/s10683-008-9198-0 (author copy https://s3.amazonaws.com/bknet/matching/eckel2008.pdf); summary in Scharf, K., & Smith, S. (2010). *The price elasticity of charitable giving: Does the form of tax relief matter?* (IFS Working Paper W10/07). Institute for Fiscal Studies. https://ifs.org.uk/sites/default/files/output_url_files/wp1007.pdf (both accessed 10 Nov 2026) | FUNDRAISING | KNOWN | As row 16: evidence about how to word a subsidy to small donors | Effect sizes not read at source; only the direction is used here | VERIFIED at source for design and direction; sizes UNVERIFIED; Crossref: no correction or retraction | no | new |
| 18 | A review of the experimental literature on matching finds the effects depend on context, the matching rate matters less than expected, and long-term effects are little studied | Epperson, R., & Reif, C. (2019). Matching subsidies and voluntary contributions: A review. *Journal of Economic Surveys, 33*(5), 1578-1601. https://doi.org/10.1111/joes.12337 (read at https://ideas.repec.org/a/bla/jecsur/v33y2019i5p1578-1601.html, accessed 10 Nov 2026) | FUNDRAISING | KNOWN | The field's own review flags heterogeneity and short horizons: Laura's co-sponsors decide once, for a building | Abstract-level reading | VERIFIED at source (abstract); Crossref: no correction or retraction | no | new |
| 19 | A meta-review of charitable-giving interventions found that telling donors their gift would be matched gave "a small but non-significant increase in donations (r = 0.08, 95% CI [-0.02, 0.17], k = 18)" in contrived experiments | Saeri, A. K., Slattery, P., Lee, J., Houlden, T., Farr, N., Gelber, R. L., Stone, J., Huuskes, L., Timmons, S., Windle, K., Spajic, L., Freeman, L., Moss, D., Behar, J., Schubert, S., Grundy, E. A. C., & Zorker, M. (2023). What works to increase charitable donations? A meta-review with meta-meta-analysis. *Voluntas: International Journal of Voluntary and Nonprofit Organizations, 34*(3), 626-642. https://doi.org/10.1007/s11266-022-00499-y (read at https://www.cambridge.org/core/journals/voluntas/article/what-works-to-increase-charitable-donations-a-metareview-with-metametaanalysis/D0356CBAC1AE69E230F12D048A161AA1, accessed 10 Nov 2026) | FUNDRAISING | NICHE | Pooled, the match effect is small and not significant | The pooled studies are lab (dictator-game) studies, not field campaigns | VERIFIED at source (results section); Crossref: no correction or retraction (only a preprint link) | no | new |
| 20 | Kresge's building challenge grants in one year: $79,225,000 to 121 organisations, "all ... awarded on a challenge basis to provide endorsement and leverage"; recipients "planned to raise an additional $386,191,000" | The Kresge Foundation. (n.d.). *The Kresge Foundation 2004 annual report*. https://kresge.org/sites/default/files/Uploaded%20Docs/2004.pdf (accessed 10 Nov 2026) | FUNDRAISING, COSPONSOR | NICHE | A challenge is a funder's tool for leverage over a recipient; Laura is the founder, not an outside funder | Planned, not raised: no outcome figure | VERIFIED at source (annual report text) | no | new |
| 21 | Kresge moved away from challenge grants as its main tool because "the nonprofits that most needed our assistance were not positioned to raise the private gifts necessary to meet the financial rigors of our challenge grant program" | The Kresge Foundation. (n.d.). *The Kresge Foundation 2007 annual report*. https://kresge.org/sites/default/files/2007.pdf (accessed 10 Nov 2026) | FUNDRAISING, COSPONSOR | NICHE | A challenge suits funders confident the money will come; a small residency's co-sponsors may not be | One foundation's own account | VERIFIED at source | no | new |
| 22 | Kresge accepted challenge applicants who had already "raised about a half to two-thirds" of the goal and could show they would meet it by the deadline | The Kresge Foundation. (2024, March 6). *Looking back: Putting capital at the heart of impact*. https://kresge.org/news-views/looking-back-putting-capital-at-the-heart-of-impact (accessed 10 Nov 2026) | FUNDRAISING, COSPONSOR, FLOOR | NICHE | A challenge lands at the end of a campaign; Laura's money is the start of hers. Her owned bottom is the "raised" share a challenger would ask to see | Quote cut off at "of your" in the page excerpt | VERIFIED at source (partial quote) | no | adds to Q11b row 27 |
| 23 | The Bank of England's fan chart was designed so the full band holds the outcome "90 out of 100 times"; Bernanke's review said the fan charts "have weak conceptual foundations, convey little useful information over and above what could be communicated in other, more direct ways, and receive little attention from the public. They should be eliminated" (Recommendation 11), and recommended "selected alternative scenarios ... along with the central forecast" (Recommendation 8) | Bernanke, B. S. (2024). *Forecasting for monetary policy making and communication at the Bank of England: A review*. Bank of England. https://www.bankofengland.co.uk/-/media/boe/files/independent-evaluation-office/2024/forecasting-for-monetary-policy-making-and-communication-at-the-bank-of-england-a-review.pdf (accessed 10 Nov 2026) | COSPONSOR, CERTAINTY, PROCESS | NICHE | Show Laura's range as named scenarios (Exhibit 3), not as a fan; a fan of the 2033 gift would be a line | Central banks forecast things they do not own; Laura's ends are owned | VERIFIED at source (the review's PDF) | no | upgrades store H9-144 (which quoted it second-hand) |
| 24 | People trade accuracy for informativeness: they often prefer a narrow estimate that misses to a wide one that holds; as reported by Teigen et al. (2018), told the true Chicago to New York distance was 713 miles, 90% preferred "730-780 miles" to "700-1500 miles" | Yaniv, I., & Foster, D. P. (1995). Graininess of judgment under uncertainty: An accuracy-informativeness trade-off. *Journal of Experimental Psychology: General, 124*(4), 424-432. https://doi.org/10.1037/0096-3445.124.4.424 (record at https://psycnet.apa.org/record/1996-10319-001; example as reported in row 25, accessed 10 Nov 2026) | COSPONSOR, CERTAINTY | KNOWN | A wide range costs credibility; Laura's after-the-move range is $20,000 wide, not $40,000 | Example read second-hand | VERIFIED at source for the trade-off (abstract); the 730-780 example UNVERIFIED in the original; Crossref: no correction or retraction | no | new |
| 25 | The boundary effect: outcomes inside a range, even at its edge, are judged correct; outcomes just outside are judged wrong, more so the further out | Teigen, K. H., Løhre, E., & Hohle, S. M. (2018). The boundary effect: Perceived post hoc accuracy of prediction intervals. *Judgment and Decision Making, 13*(4), 309-321. https://doi.org/10.1017/S1930297500009190 (read at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AED4A7230EA737078997644325739C38/S1930297500009190a.pdf/the-boundary-effect-perceived-post-hoc-accuracy-of-prediction-intervals.pdf, accessed 10 Nov 2026) | COSPONSOR, CEILING, CERTAINTY | NICHE | A gift that always lands on the stated top reads as a promise kept; a gift $1 below the bottom would read as a promise broken. The rule makes the second impossible | Lab vignettes; the paper also finds "can" is read as the top value, so "can reach $130,000" will be heard as a maximum | VERIFIED at source (paper text); Crossref: no correction or retraction | no | new |
| 26 | Wide prediction intervals are more likely to hold but are read as less certain | Løhre, E., Juanchich, M., Sirota, M., Teigen, K. H., & Shepherd, T. G. (2019). Climate scientists' wide prediction intervals may be more likely but are perceived to be less certain. *Weather, Climate, and Society, 11*(3), 565-575. https://doi.org/10.1175/WCAS-D-18-0136.1 (author manuscript at https://repository.essex.ac.uk/24444/1/likely%20certain%20w%20figures%20-%20WCAS%20R1%20CLEAN.pdf, accessed 10 Nov 2026) | COSPONSOR, CERTAINTY | KNOWN | The $105k-$160k spread from today should be shown as dated scenarios, not as the range Laura states; what she states after the move is narrow and certain | Climate forecasts, lay readers | VERIFIED at source (author manuscript; the title states the finding); Crossref: no correction or retraction | no | new |
| 27 | One-sided statements imply a direction: "'More than 100 people' suggests a crowd, while 'less than 200' implies a shortfall"; the width of an interval "can function as a cue to credibility and expertise" | Teigen, K. H. (2023). Dimensions of uncertainty communication: What is conveyed by verbal terms and numeric ranges. *Current Psychology, 42*, 29122-29137. https://doi.org/10.1007/s12144-022-03985-0 (read at https://pmc.ncbi.nlm.nih.gov/articles/PMC9660216, accessed 10 Nov 2026; online 12 Nov 2022) | COSPONSOR, FLOOR, CEILING | NICHE | "At least $110,000" signals more to come; "up to $130,000" signals a ceiling. Both ends should be stated, each with its word | Review article | VERIFIED at source; Crossref: no correction or retraction | no | new |
| 28 | The range after the move is a range of choice, not of uncertainty: markets set which band is possible before 2031; inside the band the figure is Laura's to commit, and all of it is owned | Keel inference from rows 5, 7, 12; co-sponsor judge 9 Nov ("range of choice presented as a range of uncertainty"); IPS l.15 "whatever figure you choose is money you already own" | COSPONSOR, MOVE2031, CERTAINTY | NICHE | Say it plainly: the bottom is what she commits; the top is what she has set aside and can add as the project needs it; both are in Treasury funds | The case asks for confidence that the contribution falls in the range; for a range of choice the answer is structural, and the market uncertainty belongs to the years before | Keel inference | no (the IPS sentence says this) | co-sponsor panel; this run |

## (b) Cards

**Card 1. Each end its own deduction, computed at the purchase yield (rows 1-4, 13)**
- What is it? Each end of the range is what its Treasury fund would pay if no more interest were earned: the floor
  loses 4.14% at today's forwards (bought Jan 2028, about five years to the end), the moved half 2.45% (bought Jan
  2031, under two years). Central: $110,000 to $130,000.
- Did it work? Computed at each path's own purchase yield, the stated top is owned in the zero-interest test in 100%
  of 200,000 house paths. With a fixed 4.1% and 2.5% it fails in 13.75% of paths (median $890, worst $11,225),
  because the loss grows with the yield: 2.03% at 2 points lower, 6.68% at 2 points higher.
- How is Laura's case like it? Fixed income already does this: a bond fund's payout at a target date, less what
  reinvestment would have added. Laura's ends are owned before they are stated.
- How is it not? Zero interest for five years is a test of ownership, not a forecast (expected excess about $8,000).
- What Caplet takes: write the method, not the percentage; the figures are facts by Jan 2028 and Jan 2031. NUMBERS
  section 4's $135,000 top becomes $130,000.

**Card 2. The cap makes the confidence structural (rows 5, 6, 10, 11)**
- What is it? Gift = the lower of the payout and the stated top; any excess goes to the kept half.
- Did it work? The payout is above the stated top in 100% of house paths, stock windows and joint windows, so the
  gift is always the top; excess about $8,000 (1-in-20 $12,400) goes to the kept half.
- How is Laura's case like it? Companies' actual results cluster near the top of their range guidance (Q11a row 34).
  Laura's land on it by design, and the boundary effect (row 25) says an outcome at the edge reads as a hit.
- How is it not? Three things break it: stating before the move (8.0% of paths at one month, 15.9% at twelve); a
  payments shortfall drawn from the facility money (gift still above the bottom in 100% of such windows, but below
  the top in 60% of them, 3.6% of all joint windows); a US default or a fund not paying its net asset value.
- What Caplet takes: the confidence is "certain barring a US default or a fund failing to work as its prospectus
  says", on two conditions: the move comes before any figure is stated, and the payments never draw on the gift.

**Card 3. The real uncertainty is which range, shown as dated scenarios (rows 7-9, 23, 26)**
- What is it? From today the stated bottom runs $90,000 to $130,000 and the stated top $105,000 to $160,000 (1-in-20
  each side). The bottom is fixed when the floor is bought (Jan 2028), the top at the move (Jan 2031).
- Did it work? Bernanke told the Bank of England to drop fan charts for named scenarios; wide intervals read as
  less certain (Løhre et al. 2019).
- How is Laura's case like it? Exhibit 3 can show the announcement under several markets and narrow with the dates.
- How is it not? Central banks forecast what they do not control. After the move nothing in Laura's range is
  forecast.
- What Caplet takes: 3c gives the from-today spread as scenarios with dates and one sentence of odds (for example a
  stated top of at least $120,000 in 81% of house paths); the stated range itself is narrow and owned.

**Card 4. No match on the top (rows 14-22; Q11a rows 6-11; Q18 rows 1, 7)**
- What is it? Offer the top ($20,000 above the bottom) only if co-sponsors match it, or as a challenge.
- Did it work? Small-donor mail only: +19% revenue in one large field test (Karlan & List 2007); weak or none in a
  follow-up (2011); pooled lab r = 0.08, not significant (Saeri et al. 2023). An announced lead gift does as well or
  better (Q11a row 8), and a match lowers donors' own gifts (Q11a row 7). Kresge's challenges came after half to
  two-thirds was raised, and it moved away because many recipients could not meet them.
- How is Laura's case like it? None of these studies is a founder telling institutional co-sponsors what she owns.
- How is it not? A match is a condition with a barrier; CASE does not count it until met (Q18 row 7). It would make
  owned money depend on others, against "whatever figure you choose is money you already own" (IPS l.15).
- What Caplet takes: KILL the match. Small evidence, from the wrong kind of giver, and the wrong signal.

**Card 5. What co-sponsors count, and the bond desk's narrowing (rows 12, 27, 28; Q18 rows 5-7, 32)**
- What is it? After the move Laura owns about $133,000 in the zero test ($138,700 at forwards). The IPS band says
  $110,000 to $130,000.
- Did it work? Narrowing the stated bottom to what is owned raises the committed figure by $20,000 at the median
  ($15,000 to $40,000).
- How is Laura's case like it? A finance office counts a documented pledge at face value and an "up to" as nothing
  (Q18 rows 5-7), so the committed figure is what lifts co-sponsors.
- How is it not? Narrowing breaks "the bottom will remain constant" (IPS l.15) and takes away her choice as the
  project develops (case p.3). One figure drops the range the case asks for.
- What Caplet takes: keep the IPS band, but say what each end is. The bottom is committed in writing. The top is
  owned, set aside, and available as the project needs it (Q18 row 32's "make available up to"). Ownership is
  shown, and the modelled payout is stated. If Laura chooses to pledge a figure inside the band, it is owned, so it
  counts. That is the IPS's own sentence.

## (c) Verdicts

1. **Claim 1, central range $110,000-$130,000: KEPT, with a CHANGE in method.** Re-derived: $111,134 and $133,383
   before rounding ($133,412 on the bond desk's 4.1% and 2.5%). Change: compute each deduction at the fund's own
   purchase yield. A fixed 4.1% and 2.5% fails the zero-interest test in 13.75% of house paths (up to $11,225). NUMBERS
   section 4's $135,000 top is $1,588 too high and becomes $130,000. Feeds 3c, NUMBERS 4.
2. **Claim 2, the cap gives certainty: KEPT, with a CHANGE in framing.** The gift is inside the range, and equal to
   the top, in 100% of 200,000 house paths, 1,770 stock windows and 585 joint windows. Excess p5/p50/p95
   $4,211/$7,965/$12,387. None below the bottom. The certainty comes from the rule, not the market. Add two
   conditions: no figure is stated before the move, and the payments never draw on the gift. Feeds 3c, 3b.
3. **Claim 3, a range, with the top offered as a match or challenge: CHANGED; match KILLED.** A range: yes (case
   l.108-118; IPS "planned band"). A match or challenge on the top: no.
   - The evidence is small-donor mail: +19% revenue and +22% response in one test, no ratio effect; weak in a
     replication; pooled lab r = 0.08, not significant.
   - An announced lead gift beats a match.
   - Kresge's challenges were a funder's tool, landing at the end of a campaign.
   - A match is a condition co-sponsors cannot count until it is met, and it breaks "money you already own".
   Feeds 3d.
4. **Claim 4, the bottom under-signals: CHANGED.** The gap is real: owned after the move is $23,383 above the bottom
   in the zero test, $28,735 at forwards. Narrowing would add $20,000 (median) to what co-sponsors count, but it
   clashes with "the bottom will remain constant" (IPS l.15), so it is a risk, not an option. Keep the band. Name the
   bottom "committed" and the top "owned and available as the project needs it". Show the custodian proof (3d).
   Feeds 3d, 3c.
5. **Claim 5, uncertainty from today and one confidence number: CHANGED in its figures.** Stated (after deductions
   and rounding), not payouts:
   - house: bottom $90k/$110k/$130k, top $105k/$130k/$160k;
   - stock history: bottom $110k always, top $125k/$130k/$145k;
   - joint history: bottom $95k/$110k/$125k, top about $111k/$130k/$155k.

   One confidence number: 100% of modelled paths (MODEL), "certain barring a US default or a fund failing to work as
   its prospectus says". It assumes:
   - the 2028 deposit arrives;
   - the move precedes any stated figure;
   - the cap rule;
   - funds pay net asset value.

   Three things lower it:
   - (a) stating before the move: 8.0% of paths at one month, 15.9% at twelve months, shortfall 1-in-20 $2,182 to
     $6,233;
   - (b) a payments shortfall paid from the facility money: in 5.98% of joint windows the payments fall short, and
     the gift falls below the top in 60% of those, though never below the bottom;
   - (c) a US default, or a fund closing early or failing to pay its net asset value, which is not quantified.

   Feeds 3c, 3e.
6. **Claim 6, Exhibit 3 data: DONE** (table below). Feeds Exhibit 3, 3b, 3c.
7. **Claim 7, prior art: ADDED** (rows 23-27).
   - Bernanke at source (scenarios, not fans).
   - The accuracy-informativeness trade-off.
   - The boundary effect.
   - Wide intervals read as less certain.
   - One-sided bounds imply direction.
   van der Bles and Joslyn & LeClerc are already in Q11a and are not redone. Feeds 3c, 3d, Exhibit 3 design.

**The range rule, as notes (not prose)**
- Bottom: in Jan 2028, the floor fund's payout if it earns nothing more, at the yield it was bought at, rounded down
  to $5,000. Central $110,000. Fixed from then on.
- Top: in Jan 2031, after the move, the floor's zero-interest payout plus the moved half's (each at its own purchase
  yield), added before rounding, then rounded down to $5,000. Central $111,134 + $22,248 = $133,383, so $130,000.
- Cap: the 2033 contribution is the lower of what the two funds pay and the stated top. Central payout $138,735;
  gift $130,000.
- Excess: anything above the top joins the kept half (central $8,735; kept half plus excess $32,721 on 1 Jan 2033).
  It is never promised.
- What is stated when:
  - 2028: the bottom, as a commitment;
  - 2031, after the move and never before: the top, as owned and available;
  - Dec 2032: the funds pay out and the gift is made.
- Confidence: certain barring a US default or a fund failing to work as its prospectus says. The odds belong to the
  years before 2031 (which range), shown as dated scenarios.

**Exhibit 3 data (MODEL; payments full unless stated; 2033 dollars on 1 Jan 2033)**

| Market (what moves) | Shares 3-yr growth from Jan 2028 | Stated bottom | Stated top | Funds pay | Excess to kept half | Kept half | Kept half + excess |
|---|---|---|---|---|---|---|---|
| Today's forward rates, shares at median | x1.242 | $110,000 | $130,000 | $138,735 | $8,735 | $23,986 | $32,721 |
| Shares 1-in-20 low, Jan 2028 to Jan 2031 | x0.746 | $110,000 | $120,000 | $129,632 | $9,632 | $14,411 | $24,043 |
| Shares 1-in-20 high, Jan 2028 to Jan 2031 | x2.068 | $110,000 | $145,000 | $153,887 | $8,887 | $39,921 | $48,807 |
| Yields 1-in-20 low when the floor is bought (about 1.6 points below forwards) | x1.242 | $95,000 | $115,000 | $118,422 | $3,422 | $21,975 | $25,397 |
| Yields 1-in-20 high when the floor is bought (about 1.6 points above forwards) | x1.242 | $125,000 | $150,000 | $160,064 | $10,064 | $25,774 | $35,838 |
| Shares worthless | x0 | $110,000 | $110,000 | $115,929 | $5,929 | $0 | $5,929 |
| US shares bought Jan 2008 (history, yields at forwards) | x0.997 | $110,000 | $125,000 | $134,266 | $9,266 | $20,046 | $29,311 |
| US shares bought Jan 2000 (history) | x0.654 | $110,000 | $120,000 | $127,956 | $7,956 | $14,923 | $22,879 |
| US shares bought Jul 1929 (history, lowest top) | x0.214 | $110,000 | $110,000 | $119,868 | $9,868 | $7,586 | $17,454 |
| Recession replayed: rates from Jul 2007, shares bought Jul 2008 (joint); payments short $12,117 | n/a | $95,000 | $110,000 | $114,589 | $4,589 | $23,441 | $28,030 |
| Rates from Jan 2008, shares bought Jan 2009 (joint); payments short $7,922 | n/a | $85,000 | $110,000 | $111,320 | $1,320 | $35,629 | $36,950 |
| Rates from Jan 2000, shares bought Jan 2001 (joint) | n/a | $100,000 | $115,000 | $122,943 | $7,943 | $16,997 | $24,940 |

Narrowing row for the exhibit (central path):

| Date | Bottom | Top |
|---|---|---|
| Today | $90k-$130k | $105k-$160k |
| Jan 2028 | $110,000 | $120k / $130k / $145k |
| Jan 2031 | $110,000 | $130,000 |
| Dec 2032 | gift $130,000 | excess $8,735 |

Joint rows name the month mapped to 1 Jan 2027; shares are bought twelve months later. Stock-history rows name the
month the shares are bought. The SKELETON's "rates lower for good" and "inflation world" rows come from card Q24,
not from here.

## (d) Gaps

- The joint replay uses one-year Treasury yields scaled to today's curve, 1962-2010 only. Its payment shortfalls
  come in effect from one episode (2006-2008 starts) plus Nov 2000, so 5.98% is not an independent frequency.
- No source on how co-funding institutions (not small donors) respond to a founder's conditional money. The match
  evidence is all small-donor mail or lab work. A real campaign officer's read stays open (SKELETON 3d test).
- Eckel & Grossman effect sizes were not read at source. Only the direction is used.
- Yaniv & Foster's 730-780 example was read second-hand (Teigen et al. 2018). The original paper is not read beyond its
  record.
- Kresge gives no outcome figure (share of challenges met). "Planned to raise" is not "raised".
- van der Bles et al. 2020 is still held at abstract level in Q11a row 31. It was not re-read here.
- The odds of a fund closing early or failing to pay its net asset value are not quantified. IBTM's prospectus terms
  (wind-up in Dec 2032) are in NUMBERS, not re-read here.
- The REFERENCES_APA list should take rows 14-27. The Kresge annual reports carry no confirmed publication date
  (n.d.).
