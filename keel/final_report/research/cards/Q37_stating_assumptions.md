# Q37 research card: stating the plan's assumptions and limits so a judge trusts them

Fri 13 Nov 2026 Sydney (evening run). Report parts: Section 3, part 3e (assumptions, uncertainties, limits and what to
monitor) and Table 2's note.
Notes for the Final Report store, not report prose.

Checked against: Wharton's Final Report instructions (`WHARTON_NORTH_STAR.md` section 0: "Clearly identify important
assumptions, uncertainties, and limitations. Explain what Laura or her asset management team should monitor as 2031 and
2033 approach"), the case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` l.97-99, l.131-132 and
l.146-149), FINAL IPS l.11, l.13, l.15 and l.17, `CANON.md` A4, A14, B15, C9, C15, `NUMBERS.md` sections 0, 4, 5, 7, 8d,
8i, 8j and 8l, the code (`numbers/completion.py` l.54 and l.453, `numbers/range_margin.py` l.59 and l.210), `SKELETON.md`
rows 3c, 3d, 3e (l.45-47, l.77) and Exhibits items 3-4 (l.100-104), `WORDS.md`, the professor, practitioner and
finalist panel files, store rows H2-067, H7-110, H9-041, H9-042, H10-055, Q4c-010, and cards Q4c, Q6, Q10, Q18, Q24, Q26
and Q28. It does not redo them. The plan is frozen: a "risk" in the Clash column is a risk to record, never a change to
the strategy. Every plan figure is quoted from NUMBERS with its section and is MODEL unless NUMBERS says otherwise;
"Keel arithmetic" marks my own sums.

**Claims tested (each to keep, kill or change)**
1. "3e meets Wharton's 'assumptions and limitations' best by naming each assumption with its number, its source, and one
   sentence on what changes (for the payments, and for the 2031 range) if it is wrong."
2. "Four assumptions are enough: Treasury yields at today's forward rates; shares at 7.5% a year (J.P. Morgan's 2027
   estimate); the 2028 deposit arrives in full by 31 March 2028; the funds' running costs stay under half a percent. The
   US paying its debts is a limit, not an assumption."
3. "Readers trust a plan more when it says which outcomes do not depend on an assumption than when it gives a range for
   every assumption."

**Problem class and the field that solved it.** Forecasting communication and actuarial disclosure: telling a
non-specialist reader what a long-horizon projection rests on, whose judgement each input is, and how far each output
moves. Solved in practice by the actuarial standards (ASOP No. 41 on communications, ASOP No. 27 on selecting and
disclosing assumptions), public pension accounting (GASB Statement No. 67's note disclosures and its one-point discount
rate sensitivity), the Social Security Trustees (economic assumptions section and the one-at-a-time sensitivity
appendix), and the Congressional Budget Office (the conditioning assumption first, then named uncertainties). The trust
question is answered by risk-communication experiments and reviews (van der Bles et al. 2019 and 2020; Gustafson and
Rice 2020; Schneider et al. 2021; Dries et al. 2026).

## Verdicts in one screen

1. **Claim 1: CHANGE (keep the core, add four things).** Number, source and "what changes" is right and is what every
   professional form asks (ASOP 41 3.2; ASOP 27 4.1.1-4.1.2; GASB 67 para 31(b); Trustees V.B). Four additions: (a) use
   the case's own five assumption areas as the list (case l.146-149: investment performance, the timing of cash flows,
   outside funding, the effect of inflation, the financial flexibility Laura should preserve); (b) say whose each
   assumption is and what kind it is (ASOP 41 3.4.4; ASOP 27 4.1.1 and 4.2: a market observation, an outside forecast, a
   case input, or a margin Caplet chose on purpose); (c) give the date of the information (ASOP 41 3.4.5: the 6 Nov 2026
   curve; J.P. Morgan's estimates as of 30 Sep 2026, NUMBERS 0); (d) say the direction and the time an assumption bites
   (CBO; Trustees VI.D), then say once which outcome none of them moves, as the Trustees' table shows the depletion year
   unchanged across nearly every assumption. "What changes for the payments" is "nothing" for four of the five areas, so
   saying it once beats saying it five times.
2. **Claim 2: CHANGE.** Four is not enough and two of the four are misnamed. The four cover two of the case's five areas
   (investment performance, timing); they miss outside funding, inflation and her flexibility, all named in case
   l.146-149. Misnamed: (i) "running costs under half a percent" is not a yearly cost: the 0.5% is a one-time cut from
   each end's zero-interest value that covers fund frictions (NUMBERS 0, 4, 8l; `completion.py` l.453), worth roughly
   0.10% a year over the floor's five years (Keel arithmetic); SKELETON 3c and 3d already say "half a percent a year",
   which overstates the margin about five-fold; (ii) "arrives in full by 31 March 2028" mixes the assumption (in full at
   the start of 2028, a case input) with the definition of reason 1 (nothing received by 31 March 2028); a smaller
   deposit is absorbed (the payments' standard survives a fall of 74.5% at today's yields, NUMBERS 5). Also: zero
   interest after January 2028 and the 0.5% cut are margins, not assumptions (ASOP 27 3.4.2, 4.1.1). The US paying its
   debts is neither a limit nor an ordinary assumption: it is the plan's one stated condition (IPS l.11 "barring a US
   default"; CANON A4), to be stated first, CBO-style, and sized once (card Q4c). The limits are separate: funds pay net
   asset value, the model's limits, money secured but not the site or people (CANON C9).
3. **Claim 3: CHANGE (as phrased, unsupported).** No experiment compares "does not depend" statements with ranges. What
   the evidence shows: numeric ranges cost little or no trust (van der Bles 2020 internal meta-analysis: numeric range
   d = -0.15 on trust in the number, d = -0.03, not significant, on the source); verbal hedges cost more (d = -0.55 and
   -0.21); across 28 studies, communicating uncertainty has no overall effect on trust in the source (Dries 2026, Hedges'
   g = 0.00, 95% CI -0.05 to 0.06); ranges and probabilities have only positive or null effects, while expert
   disagreement is the one form with consistently negative effects (Gustafson and Rice 2020, k = 48); stated uncertainty
   protects trust when the figure later changes (Dries 2024, d = 0.99-1.54, as reported in Dries 2026). So: give numbers
   for what moves; say "does not depend" only where a test shows it (NUMBERS 4: the stated top is $115,000 at every share
   return from 4% to 10%; the deletion test), framed as a test result, not as reassurance; never use verbal hedges; never
   frame the 7.5% as forecasters disagreeing.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Name each assumption in prose with its number, its source and what it moves; a reader qualified in the field should be able to judge each one | Actuarial Standards Board (2010), ASOP 41 3.2; professor panel ("7.5% compound, 17.88% volatility sit in a table note though Wharton asks that they be clearly identified") | PRESENTATION, CEILING | TEXTBOOK | 3e names its assumptions in prose; Table 2's note keeps only the model mechanics | ASOP 41 is written for actuaries; the judge is not one, so clarity is "appropriate to the intended users" (3.1.2) | VERIFIED (ASOP 41 read in full at the ASB) | no | ASOP 41 3.1.2, 3.2 |
| 2 | Use the case's own five assumption areas as 3e's list, in the case's order | Laura_Gao_2026_Client_Profile l.146-149; l.97-99 ("identify the assumptions supporting their recommendation") | PRESENTATION, LAURA | KNOWN | Investment performance; timing of cash flows; outside funding; inflation on projections and facility costs; the flexibility she keeps. A judge scoring against the case can tick each | Five areas in about 200 words is tight; one sentence each | VERIFIED (case text read) | no | case l.146-149 |
| 3 | Say whose each assumption is: the party responsible for each material assumption is named | ASOP 41 3.4.4; ASOP 27 4.2 (source of any assumption not selected by the actuary) | PRESENTATION, PROCESS | NICHE | Four owners: the bond market (the curve), J.P. Morgan (7.5% and its 2.4% inflation), the case (deposits, fixed payments, dates), Caplet (zero-interest standard, 0.5% cut, the house model, "most") | One or two words per assumption, not a column | VERIFIED (ASOP 41, ASOP 27 read in full) | no | ASOP 41 3.4.4; ASOP 27 4.2 |
| 4 | Say what kind each assumption is: an estimate of future experience, an observation of market data, or a combination | ASOP 27 (Doc. 211) 4.1.1 | PRESENTATION, CERTAINTY | NICHE | The curve's forward rates are a market observation; 7.5% is an outside estimate; the deposits are case inputs; zero interest and the 0.5% cut are margins Caplet chose | Kinds overlap; keep it to the owner word (row 3), which implies the kind | VERIFIED (ASOP 27 read in full) | no | ASOP 27 4.1.1 |
| 5 | Disclose deliberate margins as margins, not as forecasts | ASOP 27 3.4.2, 3.5(d), 4.1.1 (disclose any provision for adverse deviation) | CERTAINTY, RESERVE2033, FLOOR | NICHE | "If interest earns nothing" (the payments' standard from 2028) and the 0.5% cut on each end of the range are chosen cautions; saying so stops a judge reading zero interest as a forecast | WORDS explains "If interest earns nothing" once in Figure 1's note; 3e only names it as a margin | VERIFIED (ASOP 27 read in full) | no | ASOP 27 3.4.2, 3.5, 4.1.1 |
| 6 | Give the date of the information | ASOP 41 3.4.5, 4.1.3(h); SSA Trustees (2026) V.B ("Actual economic data were generally available through the third quarter of 2025") | PRESENTATION | KNOWN | The 6 Nov 2026 Treasury curve; J.P. Morgan's estimates as of 30 Sep 2026 (NUMBERS 0) | One clause; the curve date may already sit in Table 2's note | VERIFIED (both read at source) | no | ASOP 41; Trustees V.B |
| 7 | State the conditioning assumption first, then the uncertainties, each with its direction | Congressional Budget Office (2025), "Uncertainty of CBO's long-term projections": projections "show what would happen ... if current laws ... generally remained the same" | TWOREASONS, CERTAINTY | KNOWN | 3e opens with the IPS's one condition, "barring a US default" (IPS l.11; CANON A4), sized once (card Q4c: about 1% a year or less outside a debt-limit standoff) | CBO's condition is a policy choice; Laura's is a credit event. Same shape, not the same thing | VERIFIED (CBO uncertainty section read in full) | no | CBO LTBO 2025 |
| 8 | Name when each assumption bites, not only how much | SSA Trustees (2026) VI.D (25-year results barely move with fertility, "In contrast, the 75-year cost rate varies over a wide range"); CBO (2025) on timing | MOVE2031, FLOOR, CEILING | NICHE | Yields before January 2028 move the bottom; shares until the 2031 move move the top; after the move nothing moves either end (NUMBERS 4, "When each end is fixed") | Partly in 3c already; 3e repeats only the dates | VERIFIED (Trustees VI.D read in full) | no | Trustees VI.D; NUMBERS 4 |
| 9 | Show what does not move in the same table as what does | SSA Trustees (2026) VI.D: the reserve depletion year stays 2034 across nearly every assumption varied (2035 only at high real wage growth) | PRESENTATION, CERTAINTY, LADDER | NICHE | Table 2's payments column reads "paid" in every row; the unchanged column is the finding | The Trustees' constant is a projection; Laura's is owned money; do not imply the payments are a forecast | VERIFIED (Trustees VI.D read in full) | no | Trustees VI.D |
| 10 | Vary one assumption at a time from the central case, others held | SSA Trustees (2026) VI.D and main report ("one parameter at a time"); store row H9-041 (ASOP 51, secondary) | PRESENTATION, PROCESS | KNOWN | Caplet already does this (NUMBERS 4, Exhibit 3 rows; Table 2 via 8i). The Trustees give a primary-source name for it, which H9-041 lacked | Joint moves exist too (8i joint replay); the Trustees add a stochastic appendix for that | VERIFIED (Trustees read at source; ASOP 51 itself still not read) | no | Trustees VI.D |
| 11 | A rule of thumb per assumption: how much one unit of the input moves the output | SSA Trustees (2026) VI.D (each 0.1 point of real interest rate moves the actuarial balance about 0.05% of payroll) | CEILING, HALFKEPT | NICHE | From NUMBERS 4's 4%-10% row: each point of share return moves the top before rounding about $545 and her flexibility (half kept plus excess) about $1,538 (Keel arithmetic); the stated top does not move | Store only: a per-point figure invites false precision and the stated top is flat | VERIFIED (source); Keel arithmetic on NUMBERS 4 | no | Trustees VI.D |
| 12 | Say whether a return is compound (geometric) or average (arithmetic) | Governmental Accounting Standards Board (2012), GASB 67 para 31(b)(1)(f); professor panel | CEILING | TEXTBOOK | 7.5% is compound; J.P. Morgan's arithmetic figure is 8.94% (NUMBERS 0; CANON B15). One word, "compound", settles it | none | VERIFIED (GASB 67 note paragraphs read at source) | no | GASB 67 para 31 |
| 13 | One sensitivity on the input that moves the headline, at one point either side | GASB 67 para 31(b)(1)(g) (net pension liability at a discount rate 1 point higher and 1 point lower) | FLOOR, COMPLETE2028, PRESENTATION | KNOWN | The bottom moves with yields before January 2028: after a 1-point fall before 2027 the stated bottom is $85,000 (NUMBERS 5); Table 2 already gives 1-in-20 low and high yields in January 2028 ($80,000-$100,000 and $110,000-$135,000, NUMBERS 4) | NUMBERS has no 1-point-higher figure; Table 2's 1-in-20 rows do the same job | VERIFIED (GASB 67 read at source) | no | GASB 67 |
| 14 | State a return in one standard form: rate, compound, currency, before or after fees, with the inflation it includes | ASOP 27 4.1.1 example ("investment return: x% per year, net of investment expenses and including inflation at y%"); ASOP 27 3.5.3, 3.6 (consistency) | CEILING, INFLATION_TWD | NICHE | 7.5% a year compound, in US dollars, before VT's 0.06% fee, from the same J.P. Morgan edition as the 2.4% inflation used in NUMBERS 8d, so the two are consistent | One clause, or Table 2's note for the fee | VERIFIED (ASOP 27 read in full; NUMBERS 0, 8d) | no | ASOP 27 4.1.1 |
| 15 | Reinvestment is its own named investment assumption | ASOP 27 3.7.3(b) ("Effect of Reinvestment") | REINVEST, RESERVE2033 | NICHE | The payments' standard assumes nothing earns interest from 2027 (NUMBERS 0), so reinvestment drops out for the payments; it still shapes what comes back to Laura | Already a margin (row 5); say it once | VERIFIED (ASOP 27 read in full) | no | ASOP 27 3.7.3 |
| 16 | The deposit assumption is "in full at the start of 2028"; 31 March 2028 is reason 1's trigger, not the assumption | Case (deposit at the start of 2028); SKELETON Exhibits item 4 (reason defined); NUMBERS 5 | COMPLETE2028, TWOREASONS | KNOWN | A smaller deposit is absorbed in the IPS's order; the payments' standard survives a fall of 74.5% at today's yields and the ladder 98.4% (NUMBERS 5) | A recession can cut the deposit while yields fall (card Q1; NUMBERS 5), so say both numbers' basis: today's yields | VERIFIED (NUMBERS 5 read) | no (claim 2's wording was the problem) | NUMBERS 5 |
| 17 | The yields assumption moves the top-up's size, the bottom and what comes back; never whether the ten are paid after January 2028 | NUMBERS 0, 4, 5; WORDS ("the interest rates the bond market expects today") | LADDER, FLOOR, COMPLETE2028 | KNOWN | One sentence with the curve date. "Most" holds only at today's rates (NUMBERS 5: a fall of about 1.3 points before January 2027 breaks it) | In an extreme fall before 2027 the top-up could take the whole deposit (3.60 points, NUMBERS 5); keep that out of prose (density rule) | VERIFIED (NUMBERS read) | no | NUMBERS 0, 4, 5 |
| 18 | The 7.5% moves only the top and her flexibility; at 4% to 10% the stated top is $115,000 in every column | NUMBERS 4 (sensitivity table; deletion test) | CEILING, HALFKEPT | KNOWN | 3e's headline number: the share return was tested from 4% to 10% and the stated top did not move; half kept plus excess $24,648 to $33,873; VT at zero leaves one figure, $95,000, and the payments unchanged | Card Q6: 7.5% is the top of eight houses' published range; luck, not the forecast, moves the moved half | VERIFIED (NUMBERS 4 read) | no | NUMBERS 4 |
| 19 | The 0.5% is a one-time cut of each end's value for fund frictions, not "half a percent a year" | NUMBERS 0 (haircut row), 4, 7, 8l; `numbers/completion.py` l.54, l.453; `numbers/range_margin.py` l.59, l.210 ("share of value") | FLOOR, CEILING, CERTAINTY | NICHE | Fees assumed: 0.07% a year (iBond funds), 0.06% (VT), 0.15% a year on waiting money (NUMBERS 0). The 0.5% covers an ETF bought above net asset value, spreads, a fee change made with notice. Over the floor's five years it equals about 0.10% a year (Keel arithmetic: 0.5% / 4.96 years); over the moved half's two years about 0.26% | At a 0.75% cut the top is short in about 1 path in 17, by at most $429 (NUMBERS 4, 8l) | VERIFIED (code and NUMBERS read) | risk: SKELETON 3c and 3d say "half a percent a year", about five times the margin the rule holds for the floor | NUMBERS 0, 8l; code |
| 20 | The waiting-money fee is an assumption the payments' standard depends on | NUMBERS 0, 7 | RESERVE2033, COMPLETE2028 | NICHE | 0.15% a year on every waiting dollar in a Treasury-bill ETF; at 0.20% the cushion needs about a third more (NUMBERS 7, an estimate, not a run) | Which ETF is UNVERIFIED (WInS listing, a student checks) | VERIFIED (NUMBERS read); ETF UNVERIFIED | no | NUMBERS 0, 7 |
| 21 | Inflation cannot make the payments fail because they are fixed in dollars; it decides what they and the contribution buy | Case l.90; CANON A14, C15; NUMBERS 8d | INFLATION_TWD | KNOWN | US inflation 2.4% a year (J.P. Morgan 2027, band 1.9%-3.5%); the $95,000-$115,000 range is worth $82,399-$99,747 in 1 Jan 2027 dollars at 2.4% (NUMBERS 8d) | Never repeat the TNA's "nonexistent inflation risk" outside the payments (CANON C15) | VERIFIED (NUMBERS 8d, CANON read) | no | NUMBERS 8d |
| 22 | Taiwan building costs and the Taiwan dollar are not model inputs; they are tested against her flexibility | NUMBERS 8d, 8j; IPS l.15 | INFLATION_TWD, HALFKEPT | KNOWN | Taiwan construction 3.0% a year (band 1.5%-5.0%); USD/TWD 32.768 on 6 Nov; a 10% stronger Taiwan dollar is covered by the half kept in 93.2% of paths (8j) | The case puts facility cost estimates out of scope; say "tested", not "assumed" | VERIFIED (NUMBERS read) | no | NUMBERS 8d, 8j |
| 23 | Outside funding: none for the payments or the bottom; co-sponsor money comes year by year in NT$ | IPS l.11 ("or on anybody else's money"); SKELETON 3e (card Q11d) | COSPONSOR, CERTAINTY | KNOWN | One clause answers the case's "outside funding" area: only Laura's figure is fixed before 2033 | A co-sponsor shortfall is one of the IPS's three uses of her flexibility, not a reason to change | VERIFIED (IPS, SKELETON read) | no | IPS l.11 |
| 24 | Her flexibility is an assumption the case names: the IPS sizes it as half the shares, not to a cost | Case l.146-149; IPS l.15; NUMBERS 4 | HALFKEPT | KNOWN | About $21,300, about $29,800 with anything above the top (NUMBERS 4), for the IPS's three uses in its own order | Not sized to an overrun estimate; the case puts facility costs out of scope | VERIFIED (case, IPS, NUMBERS read) | no | case l.146-149 |
| 25 | Model mechanics go in Table 2's note: yields 0.9 point a year, independent of shares; the joint replay beside it | NUMBERS 0, 7, 8i; SKELETON l.77; card Q24 (-0.31 in 1962-99, +0.22 since 2000) | PRESENTATION, CEILING | KNOWN | The note names the house model (200,000 paths), 7.5% and 17.88%, the 0.9-point yield spread and independence, and the 585-window replay, because each changes a cell | Finalist: correlations "are for someone else", so never in prose | VERIFIED (NUMBERS read) | no | NUMBERS 0, 8i |
| 26 | Numeric ranges cost little or no trust; verbal hedges cost more | van der Bles et al. (2020): internal meta-analysis, numeric range d = -0.15 on trust in the number and d = -0.03 (not significant) on the source; verbal d = -0.55 and -0.21; n = 5,780 over five experiments | PRESENTATION | KNOWN | Give the numbers; no "could be somewhat higher or lower" anywhere in 3e | UK samples; facts about the present, not forecasts (the authors' limitation) | VERIFIED (read in full; no retraction or correction notice, Crossref with Retraction Watch data, 13 Nov) | no | PNAS 117(14) |
| 27 | "Estimated" and "around" do not tell readers there is uncertainty | van der Bles et al. (2020), experiment 4 (the word "estimated" did not reduce trust but "failed to communicate uncertainty") | PRESENTATION | NICHE | WORDS' "about" is a rounding word; it can never be 3e's only signal of uncertainty. The 1-in-20 points or the 4%-10% test carry it | none | VERIFIED (read in full) | no | PNAS 117(14) |
| 28 | Ranges and probabilities have only positive or null effects; expert disagreement is the one form with consistently negative effects | Gustafson and Rice (2020), systematic review, k = 48 papers, 68 experiments, 38,947 participants | PRESENTATION, CEILING | NICHE | Present the 7.5% as a tested input (4%-10%, NUMBERS 4), not as "forecasters disagree" (card Q6: eight houses from 5.8% to 7.5%). The 4% end already covers every house | Dries 2026 found too few consensus studies to test this (k = 1); science topics only | VERIFIED (read in full; no notice, Crossref, 13 Nov) | no | PUS 29(6) |
| 29 | Across 28 experiments, communicating uncertainty neither raises nor lowers trust in the source | Dries et al. (2026), random-effects meta-analysis, Hedges' g = 0.00, 95% CI -0.05 to 0.06; 7 clean studies g = 0.11, not significant; no moderation by uncertainty type | PRESENTATION | NICHE | Stating assumptions is safe; it is done because Wharton asks and because it is true, not as a trust device | Mostly fictitious communicators, online, Western samples; trust in the source, not in the plan | VERIFIED (read in full; no notice, Crossref, 13 Nov) | no | RSOS 13(4) |
| 30 | Uncertainty stated in advance protects trust when the figure later changes | Dries et al. (2024), d = 0.99-1.54, as reported in Dries et al. (2026), which counts it among its clean studies; carded in Q18 r23 | MOVE2031, COSPONSOR | KNOWN | The 2031 range will not be today's $95,000-$115,000; saying now which end moves, when, and with what, protects the 2031 conversation | The 2024 paper was read for Q18, not again here | VERIFIED (as reported in Dries 2026, read in full); no notice, Crossref, 13 Nov | no | RSOS 13(4) |
| 31 | Without a quality cue, readers treat evidence as high quality; a "low quality" label cuts trust, a "high quality" label adds nothing | Schneider et al. (2021), two preregistered randomised trials, US, n = 2,140; "low" against no cue d = 0.25 | PRESENTATION | NICHE | Do not label the 7.5% in words as weak or strong; give its test result. Where an input is genuinely weak (the waiting ETF's fee), say so with the reason, as the authors advise | Health topic; a label without reasons; one intervention | VERIFIED (main text read in full; no notice, Crossref, 13 Nov) | no | PLOS ONE 16(11) |
| 32 | Caveats about evidence "may or may not be read"; keep the size of uncertainty separate from the quality of the evidence | van der Bles et al. (2019), framework, Box 5a and the economic-statistics case | PRESENTATION | KNOWN | Supports the professor: the five assumptions in prose, not only in a note. The 1-in-20 points (size) and "a forecast for 10-15 years" (quality, CANON B15) are kept in separate clauses | A framework, not an experiment | VERIFIED (main sections read; no notice, Crossref, 13 Nov) | no | RSOS 6(5) |
| 33 | Say whether anything changed since the last communication | ASOP 41 3.5; ASOP 27 4.1.3; Trustees V.B ("unchanged from the 2025 report") | PROCESS, CEILING | NICHE | The 7.5% is the same figure the Trading Notes cited (TNA l.23; CANON B15): one half-clause shows coherence across all three deliverables | The 17.88% replaced 16.78% on 9 Nov (house figures moved by at most $2,100, NUMBERS 0): store only | VERIFIED (sources read) | no | ASOP 41 3.5 |
| 34 | Limits are separate from assumptions and each residual is named and sized | CANON C9 ("the other residuals (NAV, reinvested coupons, waiting money, the Jan 2027 price, the 2028 top-up) are named and sized"); ASOP 41 3.4.1, 4.1.3(e) | CERTAINTY, FLOOR | KNOWN | One sentence after the assumptions: funds pay net asset value; the house model's limits (NUMBERS 7: about four rate eras in 585 windows); the plan secures money, not the site or the people | Density: 3e cannot size every residual; the sizes live in NUMBERS | VERIFIED (CANON, NUMBERS 7 read) | no | CANON C9 |
| 35 | A wide management range weakened investors' positive reaction to an audit emphasis paragraph | Kelton and Montague (2018), experiment with nonprofessional investors | COSPONSOR | NICHE | Store only; bears on the range's width (card Q35), not on 3e | Abstract only | UNVERIFIED (abstract only; no notice, Crossref, 13 Nov) | no | AOS 65 |

## (b) Cards

**B1. The case's five areas as 3e's spine, each with owner, number and what moves (rows 2, 3, 4, 6, 14, 16-24)**
- What it is: professional disclosure names each significant assumption, its source and owner, its kind, its date, and
  its effect (ASOP 41 3.2, 3.4.4, 3.4.5; ASOP 27 4.1.1, 4.1.2, 4.2; GASB 67 para 31(b); Trustees V.B).
- Did it work: it is required practice for US pension and Social Security reports; the Trustees' section defines each
  assumption, gives its direction, its history by economic cycle and its values, and says whether it changed.
- How Laura's case is like it: the case lists the areas itself (l.146-149), so the list is not Caplet's choice; the
  owners are few (the bond market, J.P. Morgan, the case, Caplet).
- How it is not: a pension report has pages; 3e has about 200 words. So one sentence per area and the owner as one or
  two words, never a column of its own.
- What Caplet takes. **3e, structure:** one sentence per area in the case's order: (1) investment performance (the
  interest rates the bond market expects today, dated 6 Nov 2026; J.P. Morgan's 7.5% a year compound with its yearly
  spread, dated 30 Sep 2026; the funds' fees); (2) timing of cash flows (both deposits on time, the 2028 deposit in full
  at the start of 2028; payments at the start of each year); (3) outside funding (none for the payments or the bottom,
  IPS l.11); (4) inflation (payments fixed in dollars; J.P. Morgan's 2.4%; the Taiwan dollar and building costs tested,
  NUMBERS 8d, 8j); (5) her flexibility (IPS l.15's half). Each sentence carries what it moves; one closing clause names
  the outcome none of them moves (the ten payments after January 2028). Each area's monitoring signal is already a
  Table 3 row (deposit, market prices, fund notices, flexibility uses), so no new row is needed.

**B2. The one condition first, then the limits (rows 7, 34)**
- What it is: CBO states its conditioning assumption (current law) before any uncertainty, then names each uncertainty
  with its direction and timing; ASOP 41 asks for cautions and limits on use as their own disclosure.
- Did it work: it lets a reader separate "if the premise holds, here is the range" from "the premise itself".
- Like Laura's case: the IPS already wrote the condition, "barring a US default" (l.11), as Caplet's definition of a
  high degree of certainty (CANON A4).
- Not like it: CBO's condition is a policy choice that will almost surely change; Laura's is a rare credit event, sized
  in card Q4c at about 1% a year or less outside a debt-limit standoff.
- What Caplet takes. **3e, opening clause:** the condition in the IPS's words, called the plan's one condition (not "a
  limit"), sized once. **3e, after the five areas:** one sentence of limits (funds pay net asset value; the model's
  limits; money, not the site or people). The two reasons and Table 3 follow, as SKELETON row 3e has them.

**B3. What does not move, shown beside what does; 3e's headline number (rows 9, 10, 13, 18)**
- What it is: the Trustees vary one assumption at a time and print every output in every table, including the depletion
  year that stays at 2034; GASB 67 prints one discount-rate line at one point either side.
- Did it work: a reader sees which assumption matters by which column moves.
- Like Laura's case: Caplet already runs one-at-a-time tests (NUMBERS 4, Exhibit 3 rows) and the deletion test, and the
  payments column is constant.
- Not like it: the Trustees' constant is still a projection; Laura's payments are owned Treasuries held to their end, so
  "paid" in every row is a property of the design, not a forecast.
- What Caplet takes. **3e headline number:** the share return was tested from 4% to 10% and the stated top stayed
  $115,000 (NUMBERS 4), with the deletion test (VT at zero: payments unchanged, one figure, $95,000) as the second half
  of the same clause if words allow. **Table 2:** keep the payments column; its note says the rows move one input at a
  time from the central case, except the joint replay. A GASB-style line on the bottom needs a 1-point-higher run that
  NUMBERS does not have; the 1-in-20 yield rows already do the job, so no new run is asked unless the lead wants one.

**B4. Margins named as margins, and the 0.5% named correctly (rows 5, 15, 19, 20)**
- What it is: ASOP 27 lets an actuary build in a provision for adverse deviation but requires it to be disclosed, so a
  reader does not take a margin for a forecast.
- Did it work: it is the standard's answer to hidden conservatism.
- Like Laura's case: two of Caplet's figures are deliberate margins: the payments are sized so all ten are paid if
  nothing earns interest from 2027 (NUMBERS 0), and each end of the range is cut by 0.5% of its zero-interest value
  (NUMBERS 0, 4).
- Not like it: an actuary's margin usually lowers a discount rate; Caplet's margins are set in dollars of owned money.
- What Caplet takes. **3e, investment-performance sentence:** the funds' fees as assumptions (0.07%, 0.06%, 0.15% on
  waiting money) and the 0.5% as a one-time cut of value for fund frictions. **For the lead (SKELETON 3c and 3d):** both
  rows say "half a percent a year". The code applies 0.5% once to each end's value (`completion.py` l.453;
  `range_margin.py` l.210 "share of value"), which over the floor's five years is about 0.10% a year beyond the 0.07%
  fee (Keel arithmetic). "A year" overstates the margin about five-fold. The plain wording is "0.5% of its value", as
  NUMBERS 4 and 8l say. The 0.75% case (top short in about 1 path in 17, by at most $429) is also a share of value.

**B5. How to say it so trust holds (rows 26-32)**
- What it is: experiments and two reviews on how uncertainty statements affect trust.
- Did it work: numbers cost little or nothing (van der Bles 2020; Gustafson and Rice 2020; Dries 2026 g = 0.00); words
  cost more; disagreement costs most; uncertainty stated early protects trust when a figure later changes (Dries 2024).
  Uncertainty never raised trust in van der Bles 2020.
- Like Laura's case: the judges, and later Laura's co-sponsors, read a forecast-based figure (the top) beside owned
  figures (the bottom, the payments).
- Not like it: the samples are lay, online, mostly UK, US and other Western readers; the objects are facts and health
  estimates, not a ten-year plan; Wharton's judges are expert readers. Transfer is a judgement.
- What Caplet takes. **3e and Table 2's note, style rules, not sentences:** every uncertainty as a number (the 4%-10%
  test, the 1-in-20 points), never a verbal hedge; "about" only for rounding (WORDS); the 7.5% as a tested input, not as
  houses disagreeing (card Q6's eight-house range stays in the store); no quality labels in words; say once, in 3c or
  3e, that the 2031 range will be worked out on that day and which end can move until then (NUMBERS 4), since that is
  the change the co-sponsors will see.

## (c) Verdicts

**Claim 1: CHANGE.**
- Kept: number, source, and what changes. Every form read asks for these. ASOP 41 3.2 sets the test (a qualified
  reader can appraise each assumption); ASOP 27 4.1.1-4.1.2 asks for each significant assumption, its kind and its
  rationale; GASB 67 para 31(b) lists the significant assumptions, how the expected return was set, and whether rates
  are arithmetic or geometric; Trustees V.B gives, for each assumption, what it is, why it matters and in which
  direction, its history and its values.
- Added: the case's own list (l.146-149) as the structure; the owner and kind of each assumption (ASOP 41 3.4.4; ASOP
  27 4.1.1, 4.2); the information date (ASOP 41 3.4.5); direction and timing (CBO; Trustees VI.D's 25-year against
  75-year contrast); and the unchanged outcome stated once (Trustees VI.D).
- Changed: "one sentence on what changes" for the payments AND the range, per assumption, would repeat "nothing for the
  payments" four times. Say what each moves; say once what none moves. Exception: the 2028 deposit, which is the one
  assumption that can reach the payments (beyond a fall of 74.5% at today's yields, NUMBERS 5), and a missed deposit is
  reason 1.
- Where: 3e prose for the five areas; Table 2's note for model mechanics (row 25), in line with SKELETON's own rule
  that the note carries only assumptions that change a cell (l.103). This settles the tension between SKELETON l.47
  (prose) and l.77 (note): both, split by what changes a cell.

**Claim 2: CHANGE.** Item by item, with the outcome each bears on and the NUMBERS section:

| Item in the claim | Verdict | What it is | What depends on it | NUMBERS |
|---|---|---|---|---|
| Treasury yields at today's forward rates | KEEP, renamed | A market observation, 6 Nov 2026 curve; WORDS: "the interest rates the bond market expects today" | The top-up's size, the bottom (fixed January 2028), what comes back, "most"; not the payments after January 2028 | 0, 4, 5 |
| Shares at 7.5% a year (J.P. Morgan) | KEEP, completed | J.P. Morgan's 2027 estimate for world shares, compound, US dollars, estimates as of 30 Sep 2026, before VT's 0.06% fee, 17.88% yearly spread | The top and her flexibility only; the stated top is $115,000 from 4% to 10% | 0, 4 |
| 2028 deposit in full by 31 March 2028 | CHANGE | The assumption is the case's: in full at the start of 2028. 31 March is reason 1's trigger | The top-up first; then the floor and VT; the payments' standard survives a fall of 74.5% at today's yields | 5 |
| Funds' running costs under half a percent | CHANGE (misnamed) | Fees are 0.07%, 0.06% and 0.15% a year; the 0.5% is a one-time cut of each end's value for frictions | Each end of the range; the 0.15% on waiting money bears on the payments' cushion (at 0.20%, about a third more) | 0, 7, 8l |
| US paying its debts is a limit | CHANGE | The plan's one condition (IPS l.11; CANON A4) | Everything; sized once (card Q4c) | (card Q4c) |
| Missing: inflation | ADD | Case input (payments fixed in dollars) plus J.P. Morgan's 2.4% | What payments and the contribution buy, not whether paid | 8d |
| Missing: outside funding | ADD | None for the payments or the bottom (IPS l.11) | Co-sponsor money, year by year in NT$ | (IPS, card Q11d) |
| Missing: her flexibility | ADD | IPS l.15's half of the shares | About $21,300; about $29,800 with the excess | 4 |
| Missing: the house model's independence of shares and yields | ADD to Table 2's note | Caplet's model choice, 0.9 point a year | The 1-in-20 points; the joint replay is beside it | 0, 7, 8i |
| Zero interest after January 2028 | NAME AS A MARGIN | A provision Caplet chose (ASOP 27 3.4.2, 4.1.1) | The size of the top-up's no-interest part ($35,894) | 0, 5 |
| Taiwan dollar and building costs | NAME AS TESTED | Not a model input | Her flexibility (8j: 93.2% of paths at a 10% stronger Taiwan dollar) | 8d, 8j |

**Claim 3: CHANGE.**
- Not supported as phrased: no study read compares "does not depend" statements with ranges, and the reviews give no
  reason to expect either to raise trust. Dries 2026 finds no overall effect of uncertainty communication on trust in
  the source (g = 0.00, k = 28; the seven clean studies g = 0.11, not significant); van der Bles 2020 found it "never
  significantly increased perceived trust or reliability".
- What is supported: numeric ranges cost little (numbers d = -0.15) or nothing (source d = -0.03) while verbal hedges
  cost more (d = -0.55, -0.21) (van der Bles 2020); quantified ranges and probabilities show only positive or null
  effects, disagreement only negative or null (Gustafson and Rice 2020); without a quality cue readers assume high
  quality, and a low-quality label costs trust (Schneider 2021, d = 0.25); uncertainty stated early protects trust when
  evidence changes (Dries 2024 as reported in Dries 2026).
- The reason to say "does not depend" is Wharton and the case, not trust research: the case asks how favourable and
  unfavourable outcomes would affect the recommendations (l.148-149), and the strongest true answer is a test showing an
  output unchanged. Keep both: ranges for what moves, a tested "no change" for what does not.

## (d) Gaps

- **No 1-point-higher figure for the bottom in NUMBERS.** Section 5 has falls only. Table 2's 1-in-20 yield rows already
  show both sides, so no run is asked; the numbers owner would run one only if the lead wants a GASB-style line.
- **The 0.5% per-year equivalents (0.10% and 0.26%) are Keel arithmetic,** not a NUMBERS figure. The report should not
  print them; it should say "0.5% of its value". The numbers owner may want to confirm before SKELETON is reworded.
- **Which Treasury-bill ETF and its fee: UNVERIFIED** (NUMBERS 0, 7); a student checks the WInS listing.
- **No study tests claim 3 directly.** The evidence is about ranges and verbal hedges, mostly lay online readers in the
  UK, US and other Western countries, facts and health estimates rather than a ten-year plan, and fictitious
  communicators (Dries 2026's own limitation).
- **ASOP No. 51 still not read at the ASB** (store row H9-041 stays UNVERIFIED); the Trustees' "one parameter at a
  time" is the primary source this card uses instead. ASOP No. 41: a revision's exposure draft is dated Dec 2025; I saw
  no adopted revision, so cite Doc. No. 120.
- **Not read in full:** Kelton and Montague (2018) (paywalled, abstract only); Schneider et al. (2022, Judgment and
  Decision Making) and Dries et al. (2025, PNAS Nexus), found but not read; CBO's May 2025 alternative-scenarios report
  (numeric scenarios) not read.
- **Trustees Report date:** the SSA page metadata says May 2026; the transmittal date was not checked. Cited as (2026).
- **CANON's unverified list (l.324)** still asks "J.P. Morgan's 7.5%: compound or arithmetic", though B15 records it
  verified compound on 9 Nov (NUMBERS 0). A stale line for the CANON owner; nothing in this card depends on it.
- **The CDS sizing** of the condition is taken from card Q4c, not re-checked here.
- **REFERENCES_APA:** van der Bles 2019 and 2020, Dries 2024 and GASB's Statement No. 67 summary page are present and
  used. New entries below: SSA Trustees 2026, ASOP 41, ASOP 27, CBO 2025, GASB Statement No. 67 itself, Gustafson and
  Rice 2020, Dries et al. 2026, Schneider et al. 2021, Kelton and Montague 2018 (UNVERIFIED). No existing entry found
  wrong.
- **Retraction check method:** Crossref's "updates" filter, which carries the Retraction Watch data; checked against a
  known retraction (Wakefield et al., 1998, Lancet), which it lists. Zero notices for every psychology or behavioural
  paper here, 13 Nov 2026.

## Sources (APA 7; all accessed 13 Nov 2026)

Read at the source (1-10); used as reported in a source read in full (11):
1. Actuarial Standards Board. (2010). *Actuarial communications* (Actuarial Standard of Practice No. 41, Doc. No. 120).
   https://www.actuarialstandardsboard.org/asops/actuarial-communications/ (read in full)
2. Actuarial Standards Board. (2023). *Selection of assumptions for measuring pension obligations* (Actuarial Standard
   of Practice No. 27, Doc. No. 211). https://www.actuarialstandardsboard.org/wp-content/uploads/2024/05/asop027_211.pdf
   (read in full; effective for reports issued on or after 1 Jan 2025)
3. Board of Trustees, Federal Old-Age and Survivors Insurance and Federal Disability Insurance Trust Funds. (2026).
   *The 2026 annual report of the Board of Trustees of the Federal Old-Age and Survivors Insurance and Federal Disability
   Insurance Trust Funds*. Social Security Administration. Section V.B, Economic assumptions and methods,
   https://www.ssa.gov/oact/TR/2026/V_B_econ.html; Appendix VI.D, Long-range sensitivity analysis,
   https://www.ssa.gov/OACT/TR/2026/VI_D_LRsens.html (both sections read in full)
4. Congressional Budget Office. (2025). *The long-term budget outlook: 2025 to 2055*.
   https://www.cbo.gov/publication/61270 (the section "Uncertainty of CBO's long-term projections" read in full)
5. Governmental Accounting Standards Board. (2012). *Statement No. 67: Financial reporting for pension plans: An
   amendment of GASB Statement No. 25* (No. 327-B). https://storage.gasb.org/GASBS67.pdf (note disclosure paragraphs,
   including para 31, read at the source)
6. van der Bles, A. M., van der Linden, S., Freeman, A. L. J., & Spiegelhalter, D. J. (2020). The effects of
   communicating uncertainty on public trust in facts and numbers. *Proceedings of the National Academy of Sciences,
   117*(14), 7672–7683. https://doi.org/10.1073/pnas.1913678117 (REFERENCES_APA row 114; read in full; no notice)
7. van der Bles, A. M., van der Linden, S., Freeman, A. L. J., Mitchell, J., Galvao, A. B., Zaval, L., & Spiegelhalter,
   D. J. (2019). Communicating uncertainty about facts, numbers and science. *Royal Society Open Science, 6*(5), Article
   181870. https://doi.org/10.1098/rsos.181870 (REFERENCES_APA row 243; main sections read; no notice)
8. Gustafson, A., & Rice, R. E. (2020). A review of the effects of uncertainty in public science communication.
   *Public Understanding of Science, 29*(6), 614–633. https://doi.org/10.1177/0963662520942122 (read in full, author
   copy at https://escholarship.org/uc/item/8h30f60h; no notice)
9. Dries, C., Schneider, C. R., Oeberst, A., McDowell, M., Egharevba, G., & Rebitschek, F. G. (2026). The impact of
   uncertainty communication on trust in its sources: A systematic review and meta-analysis. *Royal Society Open
   Science, 13*(4), Article 251896. https://doi.org/10.1098/rsos.251896 (read in full; no notice)
10. Schneider, C. R., Freeman, A. L. J., Spiegelhalter, D., & van der Linden, S. (2021). The effects of quality of
    evidence communication on perception of public health information about COVID-19: Two randomised controlled trials.
    *PLOS ONE, 16*(11), Article e0259048. https://doi.org/10.1371/journal.pone.0259048 (main text read in full at
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8598038; no notice)
11. Dries, C., McDowell, M., Rebitschek, F. G., & Leuker, C. (2024). When evidence changes: Communicating uncertainty
    protects against a loss of trust. *Public Understanding of Science, 33*(6), 777–794.
    https://doi.org/10.1177/09636625241228449 (REFERENCES_APA row 46; its result used as reported in source 9; no notice)

UNVERIFIED (not read in full):
12. Kelton, A. S., & Montague, N. R. (2018). The unintended consequences of uncertainty disclosures made by auditors
    and managers on nonprofessional investor judgments. *Accounting, Organizations and Society, 65*, 44–55.
    https://doi.org/10.1016/j.aos.2017.10.001 (abstract only; no notice)

Case and plan files used (repo): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`;
`keel/final_report/FINAL_IPS_as_submitted.txt`; `CANON.md`; `NUMBERS.md`; `SKELETON.md`; `WORDS.md`;
`numbers/completion.py`; `numbers/range_margin.py`.
