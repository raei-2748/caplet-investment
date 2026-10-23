# Judge Lens: writing for a Wharton-trained finance reader

Team Caplet, Knox Grammar. 2026-27 Wharton Global HS Investment Competition (Laura Gao case, "Roots First" strategy).
Purpose: use the concepts a Wharton finance student or alumnus studied, name them correctly once, and explain them in plain English.

## A. Who judges each round

| Round | What is known | Source |
|---|---|---|
| Final reports to Top 50 (2024 cycle) | "internal reviewers and a group of professional asset managers from abrdn in Philadelphia"; 1,600+ reports, 63 countries | [S1] |
| Final reports to Top 50 (2025 cycle) | "internal reviewers and a group of professional asset managers" (abrdn not named); 1,800+ reports, 66 countries | [S2] |
| Final reports to Top 50 (2026 cycle, most recent) | "Wharton School student evaluators, as well as a professional review panel of asset managers from Aberdeen Investments in Philadelphia"; about 2,300 reports, 79 countries | [S3] |
| Semifinals (2025) | 15 judges in five panels of three, mostly industry (advisers, executives, a family-office founder); one Wharton MBA. Her advice: avoid hiding behind jargon; "the best solutions are made up of simple, elegant ideas" | [S4] |
| Semifinals (2026) | 15 named judges; "panels of Wharton alumni and industry experts" | [S5] |
| Global Finale (2026) | 5 "industry leaders": an Aberdeen credit manager, a CIO, a hedge fund COO (WG'04), a PE founder (WG'03), a WRDS product manager (Penn alum) | [S6] |
| Official criteria | Not based on portfolio returns. Judges look at strategy quality, fit with the client's objectives, research and analysis, and how well teams "communicate and defend" their recommendations | [S7] |

**What this means for us.** In the most recent cycle, the first reader of our report was probably a Wharton undergraduate or an asset manager. The 2026 post confirms the student reviewers. We do not know whether they return for 2026-27 (UNVERIFIED). Nothing public describes a rubric, how scores are weighted, or whether students and professionals read the same reports (UNVERIFIED). Semifinal and finale judges are mostly practitioners, and many are Wharton alumni. So the report has to hold up for two readers: a student who has just done FNCE 2050/2250, and a practitioner who builds liability-matched bond portfolios for a living.

## B. Wharton undergraduate finance curriculum

The concentration requires FNCE 1000 and FNCE 1010 plus four more FNCE credit units. The "Investments" track requires FNCE 2050 and FNCE 2070 [S8].

| Course | Key topics (official description) | What a reader brings to our report |
|---|---|---|
| FNCE 1000 Corporate Finance (core) | Time value of money and capital budgeting, the risk-return trade-off, market efficiency, capital structure, dividends [S9] | Present value, discounting, NPV. They will check our PV of the ten $50k payments |
| FNCE 1010 Monetary Economics and the Global Economy (core, required of all Wharton students) | What drives inflation, interest rates, asset prices and exchange rates; monetary policy [S9][S10] | Real vs nominal rates, Fed path, yield curve. They will ask about inflation risk |
| FNCE 2050 Investment Management | "management of investment portfolios": portfolio selection, asset allocation, risk-return, performance evaluation, active vs passive. Not stock picking. Past syllabus used Bodie-Kane-Marcus *Investments* [S9][S11] | Diversification, asset allocation, passive core, benchmarks |
| FNCE 2250 Fixed Income Securities | Fixed income markets, valuation and risk management. Past versions covered yield-curve construction, duration and convexity, and term-structure models [S9][S12] | Duration, immunization, cash-flow matching, reinvestment risk. **This is the course most relevant to our strategy** |
| FNCE 2070 Valuation | Company valuation via DCF and multiples [S9] | Not central to us; VT is passive |
| FNCE 2020 Consumer Financial Decision Making | How households manage and mismanage money; life-cycle decisions, retirement (Mitchell, Roussanov) [S9][S13] | Goals-based planning for a real person |
| FNCE 2390 Behavioral Finance | Psychology behind investor mistakes; challenges the rational-investor assumption [S9] | Framing, loss aversion, mental accounting |

**Textbook and CFA spine.** Bodie, Kane and Marcus *Investments* (the FNCE 2050 text [S11]) covers bond portfolio management: immunization and cash-flow matching/dedication. The CFA Level I reading "Basics of Portfolio Planning and Construction" sets out the IPS: return and risk objectives, **ability vs willingness** to take risk, and the constraints of **time horizon, liquidity, legal/regulatory, taxes, unique circumstances** [S14]. CFA Level III LDI readings cover cash-flow matching, duration matching and multiple-liability immunization [S15].

## C. Concept map for "Roots First"

| Textbook concept | Plain-English gloss (high-school voice) | Where it goes in our report | Misuse to avoid |
|---|---|---|---|
| **Investment Policy Statement (IPS)** [S14] | A written agreement on what the money must do, how much risk is allowed, and what rules apply. | Opening client analysis | Listing headings with no numbers. Each constraint needs a value (e.g. horizon 2027-2042) |
| **Ability vs willingness to bear risk** [S14] | Ability is how much loss the plan can survive. Willingness is how much loss the client can stomach. | Risk objective | Treating them as the same. Here ability is low for the payment money (fixed obligation) and higher for the facility money |
| **Present value of an annuity** [S9] | What ten future $50k payments are worth today, given current interest rates. | Sizing the ladder | Discounting at a guessed "expected return". Use the Treasury yield for each maturity |
| **Liability-driven investing (LDI)** [S15] | Start from what you owe, then invest to meet it, rather than chasing the highest return. | Strategy headline | Calling any bond holding "LDI". The point is that assets are built around the liabilities |
| **Cash-flow matching / dedication** [S15] | Buy bonds that pay out just before each $50k bill is due. | Core of the ladder table | Claiming it removes all risk. Small timing gaps and leftover cash remain |
| **Immunization / duration matching** [S12][S15] | Match the average timing (duration) of assets and liabilities so rate moves affect both about equally. | One sentence on why we chose matching instead | Saying we "immunized". Duration matching needs rebalancing; we chose matching because the payments are fixed and missing one is costly |
| **Reinvestment risk** [S15] | The risk that coupons and early maturities must be reinvested at lower rates. | Risk section | Saying it is zero. Coupons arrive before payment dates, and IBTM pays out in Dec-2032 a few weeks before the 2033 payment. Small but real |
| **Term structure / yield curve** [S12] | Each maturity has its own interest rate; the curve plots them. | Pricing each rung | Using one "bond yield" for 2032 and 2041 alike |
| **Default vs interest-rate vs inflation risk** [S10] | Treasuries have essentially no default risk, prices still move with rates before maturity, and inflation erodes what $50k buys. | Risk section | "Risk-free" with no qualifier. Say "no meaningful default risk if held to maturity, in nominal dollars" |
| **Nominal vs real** [S10] | $50k in 2042 buys less than $50k today. | Risk section and facility forecast | Mixing real and nominal numbers. The payments are fixed nominal amounts, so a nominal ladder fits; inflation hits the facility goal more |
| **Defined-maturity (term) bond ETF** [S16] | A fund holding bonds that all mature in one year, which closes and pays out its net assets that December. | Instrument choice for 2033-37 rungs | Calling the payout "guaranteed par". It is NAV at termination, after fees (0.07%) [S16]. Mapping (checked in WInS 29 Sep): IBTM Dec-2032, IBTO 2033, IBTP 2034, IBTQ 2035, IBTR 2036 = five funds (IBTN on WInS is an unrelated stock) |
| **Safety-first (Roy 1952)** [S17] | Choose the plan that minimizes the chance of falling below a disaster level. | Why the payments come first | Citing it and then picking by expected return |
| **Shortfall risk / probability of meeting goals** | The chance that we end up short of a target. | Payment certainty and the 2031 facility range | Giving one point estimate. Give a range plus a confidence level |
| **Surplus** (assets minus PV of liabilities) | What is left once the payments are fully covered. | Funds the facility | Counting surplus before the liabilities are fully funded |
| **Floor + cushion (portfolio insurance idea)** [S18] | Lock in a safe base (floor), then take risk only with the extra (cushion). | 2028 $150k: IBTM floor + VT sleeve | Calling it **CPPI**. CPPI rebalances dynamically using a multiplier. Ours is a static, buy-and-hold floor plus a risky sleeve; Perold-Sharpe call that "buy-and-hold" [S18] |
| **Core-satellite** [S11] | A safe core with a smaller growth add-on. | Describing the overall shape | Using it as a buzzword without stating the weights |
| **Diversification / passive global equity** [S9][S11] | VT holds thousands of companies worldwide, so no single company sinks us. | VT sleeve | "VT cannot fall much". World equity can drop 30-50% |
| **Monte Carlo simulation** | Run thousands of random futures to see the spread of outcomes. | 2031 facility range | Hiding the inputs. State the return/volatility assumptions and their source; don't imply precision |
| **Sequence (sequence-of-returns) risk** | Bad returns just before money is needed hurt the most. | Why equity never funds a payment | Applying it to the matched ladder, which isn't exposed to it |
| **Liquidity constraint** [S14] | Money must be in cash on the exact date it is needed. | IPS constraints | Ignoring bid-ask spreads and settlement for bonds and ETFs |
| **Behavioral framing / mental accounting** [S9] | People feel safer when each pot of money has a job. | Communicating to the client and co-sponsors | Presenting it as manipulation. Say the "buckets" match how the client thinks |

## D. Ten style rules (what makes a finance student nod, not cringe)

1. **Name it once, explain it once.** Give the textbook term in bold the first time, with a one-line gloss. After that, use the plain word.
2. **No unqualified "risk-free" or "guaranteed".** Write "no meaningful default risk, in nominal dollars, if held to maturity".
3. **Show the PV calculation.** One small table: payment year, $50k, yield, discount factor, PV. Finance readers check this first.
4. **Every probability comes with its assumptions.** "We estimate X% confidence, assuming A, B, C (source)."
5. **Give ranges, not points,** for anything uncertain (the 2031 facility figure).
6. **Don't borrow fancy names for simple things.** Ours is not CPPI, not immunization and not "alpha". Accurate simple labels beat impressive wrong ones.
7. **Say why we rejected the alternatives** (duration matching, all-equity, a 60/40 mix). Judges reward "defend your recommendation" [S7].
8. **Keep the client's goal in the topic sentence of every section.** Fit to the client is an official criterion [S7].
9. **One idea per sentence, short words, no jargon piles.** The 2025 semifinal judge's advice was "simple, elegant ideas" [S4].
10. **Admit the residual risks.** Inflation, the ETF payout depending on its NAV, timing gaps, equity drawdowns. Name each risk, size it, and say how we mitigate it. Honesty reads as expertise.

## E. Sources

- [S1] https://globalyouth.wharton.upenn.edu/news/here-are-the-top-50-teams-advancing-to-wharton-global-youths-2024-investment-competition-semifinals/
- [S2] https://globalyouth.wharton.upenn.edu/news/announcing-the-semifinalists-in-the-2025-wharton-global-high-school-investment-competition/
- [S3] https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- [S4] https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
- [S5] https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/
- [S6] https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/
- [S7] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/
- [S8] https://fnce.wharton.upenn.edu/programs/undergraduate/
- [S9] https://fnce.wharton.upenn.edu/?p=225 (Undergraduate Course Descriptions)
- [S10] https://faculty.wharton.upenn.edu/profile/ssalgado (FNCE 1010 description)
- [S11] https://finance.wharton.upenn.edu/coursepages/2007Fall/keim-205-720-07c.pdf (FNCE 205 syllabus, 2007; older, used as indicative)
- [S12] https://finance.wharton.upenn.edu/coursepages/2010_Spring/Dieckmann_FNCE235-725-2010A.pdf (Fixed Income syllabus, 2010; indicative)
- [S13] https://www.thedp.com/article/2020/02/penn-wharton-financial-literacy-course
- [S14] https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/basics-of-portfolio-planning-and-construction
- [S15] https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/overview-fixed-income-portfolio-management ; https://analystprep.com/study-notes/cfa-level-iii/cash-flow-matching-strategies/
- [S16] https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf ; https://stockanalysis.com/etf/ibtm
- [S17] https://www.econometricsociety.org/publications/econometrica/1952/07/01/safety-first-and-holding-assets
- [S18] https://rpc.cfainstitute.org/research/financial-analysts-journal/1988/dynamic-strategies-for-asset-allocation

Not cited to a specific source (standard textbook material; confirm in BKM or the CFA curriculum before quoting): the glosses for shortfall risk, surplus, Monte Carlo, sequence risk and core-satellite.

AI use: researched and compiled by Claude (Anthropic), 13 October 2026
