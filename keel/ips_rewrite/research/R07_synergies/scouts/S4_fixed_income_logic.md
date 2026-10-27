# S4 scout: fixed-income practitioner niches and logic devices (R07 rung 2, domains [6] and [12])

AI-generated research (Claude Code, scout S4, 27 Oct 2026). Not for submission. Keel recommends, Caplet decides.
No IPS prose. Every quote below was read on the page named. Where a number is mine (a quick simulation, not a
source) it is marked ILLUSTRATIVE and Jun would need to model it properly. Fetch budget ran out twice during the run,
so a few checks (Savage's own Allais answers, the 1981 Leibowitz-Weinberger article) are marked UNVERIFIED.

**Seven ideas, ranked by what they change.** The first four change how the plan is argued; 5-7 change a number or a check.

| # | Idea | Verdict for Laura | Lands in |
|---|---|---|---|
| 1 | Wald's returning bombers + Jorion-Goetzmann survivorship | Fits, and it exposes ONE number (the "3 in 4") | IPS clause + Final Report |
| 2 | Ergodicity + gambler's ruin | Fits as the logic of why the ladder exists | Final Report (IPS clause optional) |
| 3 | Allais / certainty effect | Fits, with an inversion nobody expects | Final Report |
| 4 | Contingent immunisation, "run backwards" | Partly fits; the exact difference is the insight | Final Report |
| 5 | Minimax regret for the 2031 range | Partly fits; works as a cross-check on the newsvendor | Final Report |
| 6 | Bullet vs barbell, with rolldown | Barbell and rolldown seem relevant and are not; says why | Final Report (one line), bin the rest |
| 7 | Dutch book | Seems relevant, mostly isn't; one real use as an audit | Final Report (audit line) or bin |

---

## 1. Wald's returning bombers, applied to "stocks beat bonds over most decades"

**1. Verified.**
- AMS Feature Column, "The Legend of Abraham Wald" (https://www.ams.org/samplings/feature-column/fc-2016-06). Wald's real
  question was "Given these data, what can we say about the probability of surviving a given number of hits?" and the
  method was a way to "estimate damage on the planes that never returned". The same page says the popular armour story
  is largely "plausible reconstruction" with "very little evidence for the best bits". (Only Wallis's memoir and Wald's own memoranda are firm.)
- Wikipedia, Survivorship bias (https://en.wikipedia.org/wiki/Survivorship_bias): Wald "described methods of estimating the
  vulnerability of various parts of an aircraft based on damage to surviving planes"; "there was only data from
  surviving aircraft". Finance section: "Elton, Gruber, and Blake estimated the bias across the U.S. mutual fund industry at 0.9% per year".
- Goetzmann and Jorion, "A Century of Global Stock Markets", NBER w5901 (https://www.nber.org/papers/w5901): "the United States
  has by far the highest uninterrupted real rate of appreciation of all countries" (about 5%); "For other countries, the
  median real appreciation rate is about 1.5 percent"; "The high return premium obtained for U.S. equities therefore appears
  to be the exception rather than the rule." NBER Digest (https://www.nber.org/digest/jul97/century-global-stock-markets): US real
  return 4.73% a year; world index 1921-95 "Survived" 5.35%, "Continuous" 4.86%, "Reconstructed" 4.74%; markets that became
  extinct "fell 27% the year before their break".
- Brown, Goetzmann and Ross, "Survival" (J. Finance, 1995; https://archive.nyu.edu/handle/2451/27218): "Empirical analysis of rates
  of return in Finance implicitly condition on the security surviving into the sample."
- Rung 1 had Wald right in spirit. Correction: the popular "armour where the holes are not" is legend, and what Wald actually
  did is the better story for us: he modelled the missing planes.

**2. What it is.** The data you can see come only from what survived. A history that says "stocks beat bonds most decades"
is mostly the history of the one market that kept winning (the US). Wald's real move was to stop reading the survivors and
estimate the ones that never came back.

**3. Critique.** The "survivor haircut" is small for a world index (the NBER digest's gap between the "Survived" and
"Reconstructed" indices is 0.6 points a year), large for a single country (US 4.73% vs a median of about 1.5% elsewhere, but
that is price appreciation, not like for like). Philosophically, "the US was lucky" cannot be proved ex ante; Wald-style
modelling needs an assumed hit-rate, which is itself a model. A professional would also say VT is a world index today, so
Laura's stocks are not a US bet, and the equity premium estimates Caplet uses (JPM LTCMA, forward-looking) are not backtests.

**4. Fit to Laura.** Fits, and in exactly one place. The floor, the ten payments and the 2033 reserve rest on Treasury
promises and use no historical sample at all, so survivorship cannot touch them. The ONLY survivorship-sensitive number in
the plan is the top of the 2031 range ("about 3 times in 4"), because it comes from a return distribution. ILLUSTRATIVE
(my simulation, JPM's 6.7% compound and 16.47% volatility from `CLAUDE.md`, VT stake of about $31k in Jan 2028, half of it
in the top): a 0.6-point haircut (the Survived-vs-Reconstructed gap) moves "3 in 4" to about 73%; a 2-point stress moves it
to about 68% (2 in 3). Same toy model: P(stocks beat a 5% bond over 10 years) is about 62%, falling to about 47% under the 2-point stress. So "stocks beat
bonds over most decades" is a 6-in-10 claim even in a generous model. Jun would need to model this properly.

**5. Fusion hook.** Survivorship x the Model Suite (fat-tailed regimes 1871-2023 are US-only) x the ladder: "our armour goes where
history is silent". Synergy: the plan's guarantee needs no history, and its one history-dependent number is the one the
IPS can label as such.

**6. Logic device.** The returning-planes picture, then the inversion: "The planes we can study are the ones where stocks
worked. Laura gets one plane." A judge will remember the aircraft; the chain is data -> survivors -> one number that depends on them -> that number is the top, not the floor.

**7. Lands in.** IPS: one clause (an idea, not wording): the floor owes nothing to any historical sample; only the top does.
Final Report: the full argument with the NBER numbers and a haircut table for the "3 in 4". Strong, because it also pre-empts the sceptic's best line.

---

## 2. Gambler's ruin and ergodicity, applied to fixed-dollar withdrawals

**1. Verified.**
- Peters, "The ergodicity problem in economics", Nature Physics 15 (2019) (https://www.nature.com/articles/s41567-019-0732-0). Abstract:
  "It underlies the assumption that the time average and the expectation value of an observable are the same." "Because
  wealth is not ergodic, nonsensical predictions arise." The coin toss: heads gains 50% of current wealth, tails loses 40%;
  the expectation value is +5% per toss (0.5x0.5 - 0.5x0.4) while the time-average growth is negative (about -5.3% per toss by my arithmetic, ½ln1.5 + ½ln0.6; the article gives the log change as roughly -0.05). In the paper's own words
  the expected change "does not reflect what happens over time (unless the wealth dynamic is additive)" (read via the commented copy at
  https://cyclostationarity.com/wp-content/uploads/2022/08/Peters2019-TheErgodicityProblemInEconomics_COMMENTED.pdf).
- The pushback: Doctor, Wakker and Wang, Nature Physics 2020 (summary at https://tinbergen.nl/news/567/views-of-fellows-peter-wakker-and-tong-wang-on-the-ergodicity-problem-in-nature-physics):
  Peters' work is "entirely based on elementary misunderstandings". Rung 1 marked this "med" confidence; the controversy is real.
- Gambler's ruin (https://en.wikipedia.org/wiki/Gambler%27s_ruin): "a gambler playing a game with non-positive expected value will
  eventually go bankrupt", and ruin can occur "even if each bet has a positive expected value" when stakes rise after wins.
  Date correction: the same page says the earliest mention is Pascal's letter to Fermat "in 1656", two years after the
  problem-of-points correspondence. Rung 1's "1654" is the wrong correspondence.
- Retirement-ruin practice: Milevsky and Robinson, "A Sustainable Spending Rate without Simulation", FAJ 2005
  (https://rpc.cfainstitute.org/research/financial-analysts-journal/2005/a-sustainable-spending-rate-without-simulation): "we find
  payout ratios should be lower than those many advisors recommend". (Abstract only; I did not open the ruin formulas.)

**2. What it is.** Averaging across many imaginary investors is not the same as being one investor. A portfolio that
grows by multiplication but is drained by fixed-dollar withdrawals has an absorbing barrier: once the balance cannot cover
a $50k payment, no later good year brings the missed payment back.

**3. Critique.** Peters' position is contested and much of it restates log utility / Kelly / Bernoulli (R02 #34 is already
covered), so Keel should not hang the IPS on "ergodicity economics" as a school. The useful part is the plain observation: expected value (the
ensemble average) hides ruin, and Laura has one path. Also ruin is finite-horizon here (ten payments), not the infinite game
in the textbook. And "ruin" in a retirement model usually means running dry, while the case's concept is a missed promise, which is a binary, not a dollar loss.

**4. Fit to Laura.** Fits strongly. Her liabilities are additive (ten fixed nominal $50k) and the risky asset is multiplicative; Peters'
own caveat says the ensemble average only works "if the wealth dynamic is additive". The ladder is the device that turns the
payment side into an additive, deterministic stream (Treasuries pay fixed dollars on fixed dates). ILLUSTRATIVE
(my simulation, annual lognormal at JPM 6.7%/16.47%, $300k in 2027, +$150k in 2028, $50k each January 2033-2042, all in
stocks): about 13% of paths run out of money before the last payment, yet the average terminal wealth is about $0.76m and
the median about $0.50m. The average says "fine"; one path in eight says "broken promise". Under the 2-point survivorship stress it is about 24%.
Jun would need to model this properly. (R06 D4 already ran rival archetypes; this is the all-stock bookend, and the
framing is new.)

**5. Fusion hook.** Ergodicity x cash-flow matching x Wald above. Synergy: history shows survivors (idea 1), averages
hide ruin (this idea), therefore safety has to be structural, not statistical, which is exactly what a matched ladder is.

**6. Logic device.** Peters' coin toss as a two-line story (+50% / -40%: the average investor gains, the typical investor
loses), then the causal chain to its end: "Laura's wealth is multiplicative on the way up and additive on the way out; the
only way to make the way out safe is to fix it in dollars with instruments that pay in dollars."

**7. Lands in.** Final Report (the case for the ladder against growth-first plans, with the 13% vs ~0% line and the coin toss). IPS: optional
clause that the payments do not depend on market averages. Do not cite Peters in the IPS; cite him in the Final Report with the Doctor-Wakker-Wang caveat, which shows judgement.

---

## 3. Allais paradox and the certainty effect, applied to the sceptic's argument

**1. Verified.**
- Tversky and Kahneman, "Prospect Theory", Econometrica 1979 (https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk):
  "people underweight outcomes that are merely probable in comparison with outcomes that are obtained with certainty. This
  tendency, called the certainty effect, contributes to risk aversion in choices involving sure gains."
- Allais paradox, Wikipedia (https://en.wikipedia.org/wiki/Allais_paradox): Gamble 1A is $1 million for sure; 1B is 89% $1m,
  10% $5m, 1% nothing (expected value 1.39m); most people choose 1A over 1B and 2B over 2A, which "cannot be reconciled
  with expected utility theory". Allais put his choice sets to an audience of economists at a Paris conference in 1952 and published in
  Econometrica in 1953; K&T call it "best known counterexample to expected utility theory".
- UNVERIFIED (fetch budget ran out): Savage's own first answers to the Allais problem; the claim that Savage revised them.

**2. What it is.** Offered a sure thing against a gamble with a higher average, most people take the sure thing, and then
make the opposite-looking choice when both options are risky. Economists called it a paradox because one set of
preferences cannot do both under expected-value logic.

**3. Critique.** The paradox is *descriptive*: it shows what people do, and a sceptic replies "that is a bias, not an argument". Its
dollar amounts are huge and its probabilities exact; real portfolio choices are not so clean. And judges who know prospect theory know
the certainty effect is usually presented as a flaw.

**4. Fit to Laura.** Fits, with an inversion. (a) Her ten payments are Gamble 1A: the case asks for "a high degree of
certainty", a stated requirement, not a taste. In Allais's 1B the "1% nothing" is priced at its dollar value; for Laura a
missed payment is a broken promise to a project and to co-sponsors, a cliff that dollars do not capture, which is the
legitimate reason a sure-thing preference is not a bias here. (b) The plan *is* the Allais pattern made coherent: certain
in the payments pot, a gamble in the surplus pot (1A in one account, 2B in the other). Two pots resolve the paradox without changing the preference.
(c) The inversion: Allais subjects pay a large expected-value price for certainty (1.39m vs 1m). The repo's R06 D4 finding
is that Laura pays about nothing ("certainty costs Laura about nothing"), because the ladder is priced fairly by the Treasury
curve and the surplus keeps the stocks. The sceptic's argument has an Allais-sized price attached; hers doesn't.

**5. Fusion hook.** Allais x R06 D4 (price of certainty) x mental accounts (covered, Shefrin-Statman). Synergy: the
paradox explains why judges feel the ladder is right, and the repo's numbers show it is cheap.

**6. Logic device.** Two-pot reading of the Allais table, then the pricing inversion above. Memorable one-liner for a judge: the usual price of certainty is large; hers is small.

**7. Lands in.** Final Report, in the "answer to the sceptic" section (Allais with the K&T quote, then the R06 D4 numbers once Jun re-runs them like for like). IPS: optional clause that the payments are not a bet and the surplus is. Not the headline.

---

## 4. Contingent immunisation (Leibowitz-Weinberger), is Laura's plan this run backwards?

**1. Verified.**
- Leibowitz and Weinberger, "Contingent Immunization, Part I: Risk Control Procedures", FAJ 1982
  (https://rpc.cfainstitute.org/research/financial-analysts-journal/1982/contingent-immunizationpart-i-risk-control-procedures): "Contingent
  Immunization is a procedure for the pursuit of active bond management within a framework that provides a minimum return even
  under adverse experience", via "a procedural 'safety net' based upon the modern techniques of bond immunization". "The portfolio
  remains in an active management mode as long as" the asset value stays above the safety net; it "enters the immunization mode only when absolutely necessary to assure a promised minimum return."
- Part II, "Problem Areas", FAJ 1983 (https://rpc.cfainstitute.org/research/financial-analysts-journal/1983/contingent-immunizationpart-ii-problem-areas) (title and URL only read).
- Nasdaq glossary: the manager follows an active strategy "until an adverse investment experience drives the then-available
  potential return down to the safety net level", then is "obligated to pursue an immunization strategy".
- SuperMoney: "Contingent immunization is more complex than traditional immunization strategies"; a delayed switch "can cause losses".
- UNVERIFIED: the 1981 Journal of Portfolio Management first article (rung 1 says 1981; I found only the 1982-83 FAJ pair).

**2. What it is.** Run the bond portfolio actively while its value sits above the amount needed to buy a guaranteed
minimum. If it falls to that level, switch the whole portfolio into immunisation and lock the minimum. The cushion between the portfolio and
the safety net is what pays for active risk.

**3. Critique.** The trigger needs constant monitoring, the switch has gap risk (the net moves with yields, and prices can fall faster
than you trade), and the active leg in the original is *bond* management, not stocks. The family descended into portfolio insurance
(CPPI, R02 #36), which failed in 1987 for the gap-risk reason. The common textbook point: a manager who cannot beat the
safety-net yield by enough is just paying for a complicated bond fund.

**4. Fit to Laura.** Partly. The honest comparison is exact and useful:
- Contingent immunisation is *active first, immunise on failure*. Laura is *immunise first, then take risk only with the surplus*.
  So yes, run backwards, but not as a trigger: her safety net is fully pre-funded on day one, so the trigger can never fire (it is
  CI with the trigger set at 100% of the net, the degenerate static case).
- The real CI-like feature is the 2028 deposit: in Jan 2027 the cushion over the safety net is thin (repo: headroom about
  $2k-$5k) so CI would say "you are already at the trigger, immunise everything", which the plan does. In Jan 2028 the deposit
  is a *scheduled cushion injection*, something CI's closed-fund literature never has. That event is what funds the stocks.
- The Courtroom's Jan 2031 "lock what you announce" is a *date-triggered* switch into immunisation, where CI uses a *level*
  trigger. A date trigger avoids CI's gap risk (no monitoring, no race with prices) at the cost of not reacting inside the
  four years. Plain statement: the plan is contingent immunisation whose cushion was bought in advance and whose switch is on the calendar, not the market.
- Not a fit: CI's active bond leg. Laura's active leg is stocks, and the plan deliberately keeps it small.

**5. Fusion hook.** CI x lock-what-you-announce x human capital (the 2028 deposit as a future asset). Synergy: a
strategy name practitioners recognise for what the plan is, so a judge who knows LDI places it instantly, with the differences stated.

**6. Logic device.** The three-line comparison: (i) CI waits for trouble then locks; (ii) Laura locks first then spends only
the surplus; (iii) the one scheduled lock left is a calendar date, because the promise is dated. Case study a judge would
remember: why CPPI's trigger failed in 1987 and why a pre-funded floor cannot.

**7. Lands in.** Final Report (a "lineage" box: Leibowitz-Weinberger 1982-83, what Laura keeps and what she drops). IPS: no, would need a lot of words for little gain.
(It also stays accurate to Keel's rule that a static floor plus a cushion is not CPPI.)

---

## 5. Minimax regret for the 2031 range

**1. Verified.**
- Wikipedia, Minimax regret (https://en.wikipedia.org/wiki/Minimax_regret): regret is "the difference in value between the actual
  decision made and what would have been the optimal decision in hindsight"; "The minimax regret approach is to minimize the
  worst-case regret"; credited to Savage, 1951, "The Theory of Statistical Decision". Its worked investor example (stocks,
  bonds, money market under rising, static and falling rates) picks bonds, with a mixed 61.1%/38.9% stocks/money-market
  portfolio lowering worst-case regret to about 4.28.
- MetricGate (https://metricgate.com/docs/minimax-regret-rule/): "This violation of independence of irrelevant alternatives is the
  principal theoretical objection to the rule"; "All states are treated symmetrically regardless of qualitative plausibility";
  "A single miscalibrated loss cell can change the recommended action."

**2. What it is.** Choose the action whose worst "I should have done X" is smallest. It needs no probabilities,
only a list of outcomes and what each action would have cost in each.

**3. Critique.** Sensitive to which states you list and how big the extreme ones are; depends on irrelevant alternatives (add a
state and the answer can flip); ignores likelihood, so a freak state can dominate. A professional would use it only as a robustness
check, not as the decision rule.

**4. Fit to Laura.** Partly, and as a cross-check on something already in the plan. The plan's top comes from a newsvendor
(R05 #13): announce where under- and over-promising cost balance, using the case's own warning that overpromising "could
damage her credibility", roughly 3x worse. R05 #13's own best objection is that the 3x ratio is a judgement. Minimax regret
removes the probabilities but still needs that ratio, so it does NOT escape the objection. What it adds is that the answer is stable
when the probabilities are removed. ILLUSTRATIVE (my toy: add-on over the floor = half of a $31k VT stake after three years at
JPM's numbers; announce a, regret of announcing too high = a - realised, too low = realised - a, over-promising weighted 3x):
the minimax-regret announcement is the weighted point between the lowest and highest state,
a = (hi + 3 lo)/4. With bounds at the 1st-99th percentile that is about $16.4k above the floor (the 32nd percentile of the
stock add-on); with the 0.1st-99.9th it is about $17.2k (37th). The newsvendor quantile at 1/(1+3) is about $15.5k (25th). A
method that ignores probabilities and one that uses them land within about $1k-$2k of each other. Caution: both ratios share the same 3x input and the agreement is
partly the nature of the toy (the answer sits a quarter of the way up the span), so call it "does not contradict", not "proves". Jun would need to model this properly.

**5. Fusion hook.** Minimax regret x newsvendor x Goodhart cap (covered). Synergy: two decision rules with different assumptions
give nearly the same top; the Final Report can say the range is not an artefact of one method.

**6. Logic device.** A 3x3 regret table (under-promise / middle / over-promise against weak / central / strong markets) that co-sponsors can read in
ten seconds, with Savage's one-line rule under it.

**7. Lands in.** Final Report (range-setting section, robustness paragraph). IPS: bin. It is a method for the
range, and the IPS is told not to hold the range.

---

## 6. Bullet vs barbell for the floor, and rolldown

**1. Verified.**
- Fong and Vasicek, "The Tradeoff between Return and Risk in Immunized Portfolios", FAJ 1983
  (https://rpc.cfainstitute.org/research/financial-analysts-journal/1983/the-tradeoff-between-return-and-risk-in-immunized-portfolios):
  "Immunization risk equals the weighted variance of times to payment around the horizon date"; risk "will be low if portfolio
  payments cluster around the end of the horizon" and "high if payments are widely dispersed in time". (The page does not use
  the words bullet or barbell; the mapping is mine.) Already covered in R05 #7.
- Rolldown, AnalystPrep CFA III notes (https://analystprep.com/study-notes/cfa-level-iii/models-for-fixed-income-returns-2/): rolldown
  is "the return from renewing bonds in the portfolio as they mature", "assuming the yield curve will remain unchanged".

**2. What they are.** A bullet holds bonds all maturing at (or just before) the liability date; a barbell splits the same
duration across a short and a long bond. Rolldown is the price gain a bond earns as it ages down an upward-sloping curve, if the curve holds still.

**3. Critique.** Barbells have more convexity, so they win slightly in parallel yield moves and lose when the curve twists or
the short leg must be reinvested; rolldown needs a static curve, and it is a mark-to-market idea, not a hold-to-maturity one.

**4. Fit to Laura.**
- *Bullet vs barbell: seems relevant to the floor, mostly isn't, but it explains the September rejection.* The floor is
  already a bullet (IBTM sized to the amount needed by December 2032) and each payment rung is its own bullet. The barbell lives in
  the repo's September duration-matched IEF/TLT alternative (64.8% / 35.2%, `CLAUDE.md`). ILLUSTRATIVE (zero-coupon toy on the
  26 Sep 2026 curve: 2y 4.81%, 5y 4.98%, 10y 5.17%; a $100 floor target five years out, barbell 62.5% in 2y and 37.5% in 10y
  matched on value and duration; yields change once after purchase and stay there; short leg reinvested for three years, long leg
  sold at the end): parallel moves of +/-1 point *favour* the barbell by about 0.4-0.5%; a curve twist costs it about 1.4% to
  3.1%; the bullet delivers its target in every case. Convexity pays small and symmetric, twist risk costs large and
  one-sided, which is Fong-Vasicek's dispersion point in dollars. For a $150k floor a 2% twist loss is about $3k.
- A subtler hook: the whole ladder is *dispersed* around any single date; it is a barbell of ten horizons judged against one
  date. Fong-Vasicek's risk is per liability, so the right test is payment by payment, a plain way to answer a judge who sees "10-year duration" and calls it unhedged.
- *Rolldown: seems relevant, isn't.* Every bond and every iBond is held to its own date, so the pull to par and the rolldown are
  baked into the yield paid at purchase and are not a separate return Laura collects. The one place rolldown matters is the model: the repo's genius-lab
  note says the coupon-reinvestment model "ignores roll-down", so "own-rung reinvestment is a little optimistic". That is a
  caveat for Jun's model, not a feature of the plan. (Direct T-bills are banned, so a steep short end of the curve cannot be
  harvested the textbook way anyway.)

**5. Fusion hook.** Bullet-per-payment x Taleb's barbell (rival H08) x two pots. Synergy: bullets inside the bond pot, barbell across the two pots (a floor that
cannot fail, a surplus that can), which answers H08 on its own terms and shows why the "middle" mix is the thing avoided.

**6. Logic device.** "Bullets at the bond end, a barbell across risk" in one picture; rolldown as a thing we deliberately do not need a view on.

**7. Lands in.** Final Report, one line: why a ladder beats the September duration match (with the twist numbers once Jun checks
them). Bin rolldown for the IPS; keep the caveat in the model notes. Overlaps R02 #10 and R05 #7, so low novelty and strictly supporting.

---

## 7. Dutch book, applied to inconsistent promises (a range plus a probability)

**1. Verified.**
- Wikipedia (https://en.wikipedia.org/wiki/Dutch_book): a Dutch book is "a set of bets that ensures a guaranteed loss"; credited
  to "Bruno de Finetti and ... Frank P. Ramsey, apparently independently", to justify Bayesian probability.
- Stanford Encyclopedia of Philosophy, Dutch Book Arguments (https://plato.stanford.edu/entries/dutch-book/): violating the
  probability axioms lets a bookie construct bets with a sure loss; objections include "a gap between the agent's degrees of belief
  and the acceptance of bets", and "the trouble with being incoherent cannot be that it will lead to losses" (the "Czech Book" symmetry).
- The no-arbitrage bridge (a floor with upside and no cost would be a free lunch) is standard finance but I did not find a
  page stating it as Dutch-book logic (Wikipedia's page does not). Treat it as my bridge, not a citation.

**2. What it is.** If your stated odds are inconsistent, someone can place bets with you that lose money whatever happens. It is
a test that a set of probability statements hangs together.

**3. Critique.** It tests coherence, not truth; a coherent forecast can be wrong. It assumes you would bet at your stated odds
(SEP's "betting vs belief" gap), and Laura's co-sponsors are not bookmakers. Judges will see it as clever but remote.

**4. Fit to Laura.** Seems relevant, mostly isn't, with one honest use. A range plus a probability ("floor, top, and 3 in 4 to reach it") is
automatically coherent because it is monotone, so no real Dutch book arises. Two real checks remain. (a) **Certainty is probability 1**: by de Finetti's
logic, anyone who states probability 1 must accept any odds against, so a "certain" claim has to be exactly the claim the instruments
back (nominal Treasury dollars on the date held) and nothing wider. This lines up with Keel's rule that stocks are never
called sure and iBond/T-bond language stays exact. (b) **The IPS and the Final Report together are a book**: any number that
appears twice (3 in 4, the floor, the reserve) must be the same event and the same figure, or an attentive judge has found
the sure loss in credibility. The no-arbitrage bridge: an upside "for free" above a guaranteed floor is the one
inconsistent promise, and the plan avoids it by stating the price (the stocks' sleeve is what pays; expected interest forgone), the capital-protected-note-minus-the-option thesis already in V25.

**5. Fusion hook.** Dutch book x R05 #14 (interval scoring, Goodhart cap) x the V25 thesis. Synergy: a consistency audit table
(every probability stated anywhere, the event, the source) that Tess can run on both documents.

**6. Logic device.** "Never state a probability you would not bet at": a sentence that fits on a Final Report slide.

**7. Lands in.** Bin for the IPS. Final Report: one audit line, or a Keel-internal check in `textcheck.py`'s lineage. Do not
present it as a headline idea; it is a discipline, not a feature.

---

## Dropped or not taken up
- **Rolldown as a return source:** see 6. **Contingent immunisation as the plan's name:** see 4 (a lineage, not a label).
- **Rung 1 date error:** gambler's ruin is Pascal's 1656 letter, not "1654 correspondence" (that was the problem of points).
- **Parrondo's, Braess, Simpson's** (rung 1 [12]): not verified this run and no mechanism that changes a decision. Parrondo's
  paradox is linked to rebalancing gains, but Laura's stock sleeve is about $31k with $25 trades and no rebalancing, so it
  would be a flourish. Bin unless Jun finds a mechanism.

## Best synergy from my domain
The chain is: history shows only survivors (Wald, Jorion-Goetzmann) -> averages across paths hide ruin (Peters, gambler's ruin) -> so
safety must be structural, not statistical -> which is a ladder matched payment by payment (bullets), whose guarantee uses no sampled
history. Then Allais shows why that certainty feels right and the repo's R06 D4 shows it is nearly free for Laura, and minimax regret
confirms the one history-dependent number (the top of the range) is not an artefact of one method. One logic line holds the plan up: "the floor needs no history; only the top does, and we say which".
The best single IPS clause is the survivorship one (idea 1), because it explains why the plan is built the way it is and shows judges the team knows what its own numbers rest on.
The Final Report carries ideas 2-5 as a four-step argument (survivors, averages, certainty, regret), each with its illustrative numbers re-run by Jun.
