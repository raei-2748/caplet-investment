# Q188. Is Laura's plan "one safe asset plus the whole market", with the safe asset set by her dates instead of by cash? Tobin's separation theorem (1958) and Sharpe and Tint's liabilities (1990), read against the plan

- **Date:** Thu 19 Nov 2026, evening, Sydney. Every source marked VERIFIED was read on Thu 19 Nov 2026.
- **Report parts:** 2.0 (the governing thought and the definition of ink at first use: what "safe" means for Laura), 2.2
  (the allocation is the rule: only two numbers in the plan are choices), 2.3 (her career as the theorem's own named
  exception), 3b (half as one of two free choices), 3c (the range runs the pension rule backwards), 3e and Table 3 (Tobin's
  admitted fiction and the two reasons to change), References.
- Notes for the Final Report store, not report prose.
- **The question answered in five lines.**
  - Yes, it fits, and better than the textbook version: Tobin's own 1958 theorem was about cash against government bonds,
    and shares were outside it, so the plan's "safe asset" is the very asset Tobin treated as risky (idea 1).
  - "The safe asset is several dated holdings, not one" is not a break: Merton (1975) says a "fund" can be a set of bonds,
    and Tobin's own risky "consols" were already a composite (idea 4).
  - "The proportion is set by owned promises, not by risk tolerance" is not a break either, once liabilities exist:
    Rudolf and Ziemba (2004) prove the liability hedge "is independent of preferences" (idea 4). Only two numbers in the
    plan are choices about risk: "most" of the free 2028 money into the late-2032 Treasury fund, and "half" of VT moved.
  - The real break is mean-variance itself: Tobin proved no smooth taste for risk ever holds only the safe asset, and
    Caplet's IPS holds only Treasuries behind every payment, so the rule is a definition, not a degree of caution (idea 2).
  - The second real break is direction: a pension fund is handed its debts and then invests; on the facility side Laura
    buys the Treasuries first and then names only what they will pay (idea 3).
- **Not repeated:** store H3-020, H4-115 and H6-069 (Tobin's two funds with cash as the riskless asset), H3-024, H4-118,
  Q1c-033, Q5e-025, Q5e-026, Q33-009, Q33-010 (Sharpe-Tint's hedge credit, via Ang, Chen and Sundaresan), Q1c-032
  (Leibowitz and Henriksson: the immunised fund "takes the place of cash"), Q57-010 and Q57-037 to Q57-044 (Shefrin and
  Statman's layers, Sharpe's lockboxes, Waring and Whitney's "new two-fund theorem", Waring and Siegel), H7-003 and
  Q1c-022 (cash only looks safe; Campbell and Viceira's safe asset), H7-099 and Q17-038 (goal-hedging and
  performance-seeking portfolios), Q33-025 (CFA's two portfolios), Q123-025 and Q123-026 (half as a Kelly fraction),
  Q175 (the copout; Grossman and Stiglitz), Q1c-028 (Merton on human capital, 2014), Q2a-005 (UK LDI fire sales),
  Q1c-031 (Leibowitz 1987). A grep of `store/insights.jsonl` on Thu 19 Nov evening found no row on what Tobin's 1958
  risky asset was, his "plungers", his footnotes, Segal and Spivak, Rudolf and Ziemba, Merton (1975), Tobin's Nobel
  lecture, Buiter (2003), Russell and Brooks (1998) or Sharpe and Tint's k.
- **Problem class:** choosing a portfolio when the riskless asset depends on when the investor needs the money. **Field
  that solved it first:** monetary economics (Tobin 1958, which already noted that the investor's "year" differs); then
  pension finance (Leibowitz 1987-88; Sharpe and Tint 1990); then continuous-time finance (Merton 1973 and 1975; Rudolf
  and Ziemba 2004).

## The ideas, each in three plain sentences

### 1. Tobin's risky asset was a Treasury: an asset is safe only for a date

- (a) In 1958 James Tobin asked why anyone keeps cash, which pays nothing, when the government's bonds pay interest, and
  answered that a bond's price falls when interest rates rise, so an investor who counts his wealth a year from now can
  lose money on a bond and a cautious one keeps some cash. So the paper that first proved "one safe asset plus one mix
  of risky ones" used cash as the safe asset and, as the risky ones, "obligations to pay stated cash amounts at future
  dates, with no risk of default", while shares were left out of the paper on purpose.
- (b) Caplet's plan holds as its safe asset exactly what Tobin treated as risky, because Laura counts her wealth on ten
  dates, each 1 January from 2033 to 2042, and a Treasury that matures just before one of them pays the same dollars
  whatever rates do in between; that is the IPS's "Held to the end, these pay what they say – no price fluctuations for
  us to fear" (l.13). Tobin's investor and Laura are afraid of the same thing, a change in interest rates, and run in
  opposite directions: he runs towards cash, and she runs towards dated Treasuries, because cash kept until 2033-2042
  would earn whatever rates happen to be then.
- (c) Where it breaks: Tobin's theorem needs one safe asset that is the same for everybody, and with dates there is none,
  since Laura's 2041 Treasury is as risky for a one-year investor as Tobin's consol was. Tobin saw the edge himself (the
  "year" for which a portfolio is chosen "is not the same for all investors"; cash is only "relatively riskless"), and
  the break gives Section 2 its first sentence: an asset is not safe or risky by itself, only for a date, which is
  exactly how the report defines ink (a dollar figure owned in Treasuries that will pay it on its date).
- **Decision it serves:** the ten Treasuries bought in January 2027 (IPS l.13) and the Treasury fund maturing in late
  2032 that holds the bottom of her range (l.15). **Part:** 2.0, beside the definition of ink.
- **Source:** Tobin (1958), pp. 66, 67 n. 1, 84-85.
- **Pedigree or aha:** aha. Every finance judge knows "Tobin: T-bills plus the market". Very few know that his original
  risky asset was a default-free government bond and that shares were outside his paper.

### 2. "Plungers do not exist": why no taste for risk produces the IPS's "none"

- (a) In the same paper Tobin proved that an investor who weighs risk in the usual smooth way always holds at least a
  little of the risky asset when it pays more on average, because a very small risk costs such an investor almost
  nothing; holding only the safe asset is a case he showed to be "entirely excluded", and he summed it up as "All
  risk-averters are diversifiers; plungers do not exist." Segal and Spivak (1990) showed the one way out: a person for
  whom even the first small risk has a real cost (a "kink" in how they value outcomes) can sensibly buy complete
  insurance with no deductible, even when that insurance has a price.
- (b) The IPS holds no shares at all behind any of the ten payments ("none of your 10 operating payments will depend on
  a share price", l.11), which is exactly the corner Tobin proved no smooth taste for risk will choose, so the rule
  cannot be read as Laura being very cautious, and the IPS never says it is: its first paragraph says her taste for risk
  alone would "usually own shares" (l.9). The zero comes from the promise, because a payment to the residency is either
  there in full on 1 January or it is not, and a payment that is 98% there is a broken promise: that all-or-nothing edge
  is the kink Segal and Spivak describe (Keel inference).
- (c) Where it breaks: Segal and Spivak's investor still buys the risky asset once its extra return is large enough,
  while the IPS says none at any extra return, so the rule is not a preference at all but a definition of certainty
  (CANON A4: structural, not a probability), and a definition cannot be argued down by a better forecast. Did the smooth
  rule work where it was tried? When Russell and Brooks (1998) ran Sharpe and Tint's mean-variance rule on a fully
  funded promise of dated payments (a state prepaid tuition plan, assets and liabilities both $1,000,000), it put 34.8%
  in the S&P 500, in a field where Michigan's and Wyoming's plans had already "experienced the effects" of falling short.
- **Decision it serves:** the whole first deposit buys the ten (l.13), and the 2028 deposit completes them before
  anything else (l.13). **Part:** 2.0 (one clause), 2.3.
- **Source:** Tobin (1958), pp. 76, 78; Segal and Spivak (1990), abstract, and their working paper's full-insurance
  section; Epstein (1992), section 2.4; Skiadas (2007), section 4.4; Russell and Brooks (1998).
- **Pedigree or aha:** aha. Judges know "Tobin: everyone holds some of the risky asset"; few will have seen it used as
  the theorem's own proof that a rule like the IPS's is not a degree of caution.

### 3. A pension fund owns what it has promised; Laura promises what she owns

- (a) In 1990 William Sharpe and Lawrence Tint told pension funds to judge an investment by what it does to assets minus
  k times liabilities, where the fund chooses k between 0 (ignore what you owe, the old way) and 1 (count every dollar
  owed); a fund that sets k at 1 finds that its safest holding is no longer cash but whatever moves exactly like its
  debts, which for a debt fixed in dollars is a bond maturing when the debt falls due.
- (b) Caplet's plan never sets k between 0 and 1: a payment is either counted in full and owned in Treasuries for its
  date, or nothing is promised against it. For the ten payments the case wrote the debt first, so Caplet bought the
  matching Treasuries in January 2027, as Sharpe and Tint would; for the facility the plan runs them backwards, because
  Caplet buys the Treasuries first (a Treasury fund maturing in late 2032, bought in January 2028, and more of it with
  half of VT before the 2031 meetings) and Laura then names only a figure they will pay ("whatever figure you choose is
  money you already own", l.15).
- (c) Where it breaks, and why the break helps her: a pension fund cannot choose its debts, which is how a 60/40 fund
  fully funded in January 1981 was only 69% funded by June 1986, when falling rates raised what it owed (Leibowitz 1987,
  store Q1c-031). Laura's stated range cannot be outrun by rates in that way, because both ends are owned before they are
  named (NUMBERS 4: after the move nothing changes either end); what can still touch it is a fund's costs or an early
  end of the fund, which the 0.5% margin and NUMBERS 3 deal with.
- **Decision it serves:** the range rule and the move before the 2031 meetings (l.15; NUMBERS 4). **Part:** 2.0 (with the
  definition of ink), 3c.
- **Source:** Sharpe and Tint (1990), as restated by Russell and Brooks (1998, p. 263), Miyamoto (2005, appendix) and
  Shang and Hossen (2019, section 2.1.4), the original being a scan with no text; Leibowitz (1987) via store Q1c-031.
- **Pedigree or aha:** aha. Surplus investing is pedigree to a pension judge, but this run found no source that says the
  rule can be run backwards by an investor who chooses her own debt after buying the asset.

### 4. Two choices, and everything else is dated

- (a) Rudolf and Ziemba (2004) took Merton's version of separation (a safe asset, the market, and a fund that hedges
  changes in interest rates) and gave the investor debts; they found a fourth fund, the liability hedge, whose size "is
  independent of preferences and only depends on the funding ratio" (what the fund owns divided by what it owes).
- (b) In Caplet's plan the Treasuries behind the ten payments would be the same purchase whether Laura were bold or
  timid, as Rudolf and Ziemba predict, and because her first deposit about equals the cost of the ten ($300,000 against
  $301,544 on the 6 Nov curve, NUMBERS 1), nearly all of 2027's money is hedge and none is free. Only two numbers in the
  whole plan are choices about risk rather than consequences of a date: how much of the 2028 money left after the ten
  goes to the late-2032 Treasury fund rather than VT ("most", which Keel reads as 73.3%: $81,244 against $29,594), and
  how much of VT moves into Treasuries before the 2031 meetings ("half"); each is Tobin's one free choice (how much of
  the free money to keep safe), and half sits in the middle of a nearly one-for-one trade, where each $5,000 more of
  stated top costs about $5,300 of what Laura keeps (NUMBERS 8o).
- (c) Where it breaks: the objection that the safe asset is ten Treasuries and a fund rather than one asset is no break,
  since Merton (1975) wrote that "simple financial instruments like bonds may serve the function of some of the funds".
  The real break is time: Rudolf and Ziemba's investor resizes the hedge continuously as the funding ratio moves, while
  Caplet buys each hedge once, holds it to its date and changes the mix only on three dated steps (January 2027, January
  2028, before the 2031 meetings).
- **Decision it serves:** "the allocation is the rule" (SKELETON 2.2); half as Caplet's choice (3b). **Part:** 2.0-2.2.
- **Source:** Rudolf and Ziemba (2004), abstract, introduction and conclusions; Merton (1975), pp. 661, 667; Tobin
  (1958), p. 84; NUMBERS 1, 4 and 8o.
- **Pedigree or aha:** half and half. The four-fund theorem is niche; the count of exactly two choices is new, and it
  tells a judge which numbers to argue with.

### 5. Merton's wages that cannot be sold forward, and the one worker who sells hers

- (a) Robert Merton (1975) named the case where the two-fund theorem gives way: a worker whose "labor income ... he
  cannot sell forward ... because of the moral hazard problem" (a worker paid in advance has less reason to work) should
  hold less of the shares that move with that income, and if no security tracks it he "can do nothing to hedge" and keeps
  the same two funds; in his Nobel lecture (1981) Tobin said the covariances of asset returns with "earnings from human
  capital" are "very relevant to portfolio choice".
- (b) This is IPS l.9 in the theorem's own terms: Laura's career is a large holding she cannot sell, it shrinks in the
  recessions when shares fall, and no fund tracks a graphic memoirist's earnings; so the plan changes how much of the
  market she holds, not which market, and VT stays the plain world fund.
- (c) Where it breaks: authors are the one kind of worker who do sell part of their labour income forward, because a
  publisher's advance buys royalties before the book exists, paid in parts "triggered by actions on your part, such as
  turning in manuscripts" (store Q95 row 14), which is how publishers handle Merton's moral hazard. The case says Laura
  makes her 2028 deposit from "earnings from publishing advances, speaking engagements, licensing, and other
  entrepreneurial ventures", so the one part of her career the plan relies on is partly a forward sale already, and it is
  also the one part the IPS gives a written exit: a missed deposit is one of its two reasons to change (l.17).
- **Decision it serves:** the thesis (IPS l.3, l.9); VT as one plain world fund; the missed deposit as a reason to change
  (l.17). **Part:** 2.3; 3e.
- **Source:** Merton (1975), pp. 666-668; Tobin (1981), Nobel lecture; store Q95 rows 12-14; the case, "Laura's
  Financial Goals".
- **Pedigree or aha:** the human-capital point is pedigree (Bodie, Merton and Samuelson are in the store); the advance as
  the exception Merton's moral hazard predicts is an aha.

### 6. Tobin's admitted fiction, made into a rule

- (a) Tobin's model fixed each portfolio for one "year", and in a footnote he admitted this was a fiction, because "a
  portfolio is never so irrevocably frozen that there are no conceivable events during the period which would induce the
  investor to reconsider", and the investor knows that when choosing.
- (b) The IPS turns Tobin's footnote into a rule: it lists in advance the only two events that would make Caplet
  reconsider, a missed deposit or a Treasury default, and says "A fall in the market is not one of them" (l.17), so a
  theorem proved for one year is made to hold for sixteen by naming the few events that could reopen it.
- (c) Where it breaks: Tobin's investor re-chooses his mix every period by design, so for him holding still is a
  convenience, while for Laura holding still is the point; the break teaches that the theorem says what to hold, not for
  how long, and that the plan's length comes from her dates, not from the theorem.
- **Decision it serves:** the two reasons to change (l.17). **Part:** one clause in 2.0, or 3e and Table 3.
- **Source:** Tobin (1958), p. 67 n. 1.
- **Pedigree or aha:** a small aha: nobody reads Tobin's footnotes, and this one is the IPS's l.17 in 1958.

## Rows for the store

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Tobin's 1958 risky asset was a default-free government bond: the alternatives to cash are "obligations to pay stated cash amounts at future dates, with no risk of default" | Tobin (1958), p. 66 | CERTAINTY, LADDER | NICHE | The asset the founding separation paper treated as risky is the asset Laura's plan treats as safe: a Treasury paying a stated sum on a stated date | Tobin's investor counts his wealth one "year" ahead; Laura counts hers on ten Januaries, 2033-2042 | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com (JSTOR copy with a text layer) |
| 2 | Shares were outside Tobin's paper on purpose: liquidity preference "does not concern the choices investors make between the whole species of monetary assets" and corporate stocks, real estate and the rest; the analysis is "deliberately limited" to monetary assets | Tobin (1958), pp. 66, 85 | PRESENTATION, OTHER | NICHE | "A safe asset plus the share market" is the later CAPM reading (Sharpe, Lintner, Mossin); Tobin's own theorem was cash against bonds, so Laura's plan sits closer to the original than to the textbook | The algebra works for any risky assets; Tobin left the wider choice "to other branches" of theory, not because it fails | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com |
| 3 | Separation in Tobin's own words: "the proportionate composition of the non-cash assets is independent of their aggregate share of the investment balance" | Tobin (1958), p. 84 | CEILING, HALFKEPT | KNOWN | Laura's risky mix is VT at any size; moving half of VT before the 2031 meetings sells half of every holding in it and leaves the mix unchanged | Tobin's composite is built from the investor's own estimates; VT takes the market's weights (card Q175 defends that choice) | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com |
| 4 | Separation needs a riskless asset: "This analysis is applicable only so long as cash is assumed to be a riskless asset", and cash is only "relatively riskless" | Tobin (1958), pp. 84-85 | CERTAINTY, LADDER, REINVEST | NICHE | The theorem hangs on which asset is riskless; for money owed on dates it is the Treasury maturing before each date, while cash kept to 2033-2042 would earn whatever rates are then | Tobin chose cash because his investor's horizon was a year; the limit he named was purchasing-power risk, not dates | VERIFIED (read at source, 19 Nov 2026) | No; agrees with the TNA's reinvestment notes | This run: finance.martinsewell.com |
| 5 | Tobin's footnote on horizons: "the relevant 'year' ahead for which portfolio decisions are made is not the same for all investors" | Tobin (1958), p. 67 n. 1 | CERTAINTY, LADDER | NICHE | The liability view is already latent in Tobin: change the investor's "year" and the safe asset changes; Laura's "year" is ten dates | A footnote about transaction costs, not a theory of liabilities; Leibowitz and Sharpe-Tint built that about thirty years later | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com |
| 6 | Tobin admitted the fixed-period portfolio is a fiction: "a portfolio is never so irrevocably frozen that there are no conceivable events during the period which would induce the investor to reconsider" | Tobin (1958), p. 67 n. 1 | TWOREASONS, PROCESS | NICHE | IPS l.17 names those events in advance (a missed deposit, a Treasury default) and says a market fall is not one: Tobin's footnote made into a rule | Tobin's investor re-chooses every period by design; Laura's plan holds each Treasury to its date | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com |
| 7 | "All risk-averters are diversifiers; plungers do not exist": for an expected-utility investor, holding only the safe asset is "entirely excluded" when the risky asset pays more, because a tiny risk costs almost nothing | Tobin (1958), pp. 76, 78 | CERTAINTY, LADDER, LAURA | NICHE | No setting of caution produces the IPS's zero shares behind every payment (l.11), and IPS l.9 says her taste alone would "usually own shares": the zero must come from the promise | Tobin assumes zero expected capital gain on bonds and smooth preferences; for Laura the extra return given up is the share premium | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com |
| 8 | Segal and Spivak: under expected utility the price of avoiding a small risk is second order (pi'(0) = 0); with a kink it is first order, and "the optimal insurance is complete and there is no deductible" even at a positive price; Epstein: then "a sufficiently large mean excess return is necessary for diversification" | Segal & Spivak (1990), abstract; Segal & Spivak (1988 working paper), full-insurance section; Epstein (1992), sec. 2.4 | CERTAINTY, LADDER | NICHE | The ten payments are held the way Segal and Spivak's investor insures, completely and with no deductible, because a payment 98% there is a broken promise, which is the kink (Keel inference) | Their kinked investor still takes the risky asset when its premium is large enough; the IPS takes none at any premium, so its rule is a definition (CANON A4), not a taste | VERIFIED (abstract read at source; working paper and Epstein excerpts read at source, 19 Nov 2026) | No | This run: cris.tau.ac.il; scispace.com; people.bu.edu |
| 9 | Skiadas: an expected-utility investor "is essentially risk-neutral toward the addition of sufficiently small risks" and "would seek some exposure to all investment opportunities of positive expected excess return"; real investors often do not | Skiadas (2007), sec. 4.4 | CERTAINTY | KNOWN | Row 7 in modern words, for a judge who wants the textbook form of Tobin's proof | A general result with no liabilities in it | VERIFIED (excerpt read at source, 19 Nov 2026) | No | This run: kellogg.northwestern.edu |
| 10 | Russell and Brooks ran Sharpe and Tint's mean-variance surplus rule on a fully funded promise of dated payments (a prepaid tuition plan, assets and liabilities $1,000,000 each) and got 34.8% in the S&P 500; Michigan's and Wyoming's plans had already "experienced the effects of this risk" | Russell & Brooks (1998), pp. 257, 263-270 | CERTAINTY, LADDER, OTHER | NICHE | What a smooth rule does with promised money: it puts a third in shares. Laura's ten, with a first deposit about equal to their cost, hold none | Tuition debts rise with tuition inflation, so their hedge was inflation-indexed Treasuries (banned for Laura's plan; her payments are fixed dollars, TNA l.7); the 34.8% is their illustration, not what those states held | VERIFIED (read at source, 19 Nov 2026) | No; a refused design | This run: openjournals.libs.uga.edu |
| 11 | Sharpe and Tint's k: judge investments by assets minus k times liabilities, with k from 0 (debts ignored, the asset-only way) to 1 (every dollar owed counted); the Society of Actuaries calls the same number H, "the target hedging ratio" | Sharpe & Tint (1990) as restated by Russell & Brooks (1998), p. 263; Miyamoto (2005), appendix; Shang & Hossen (2019), sec. 2.1.4 | CERTAINTY, MOVE2031, COSPONSOR | NICHE | Caplet's plan has no setting between 0 and 1: a payment is counted in full and owned in Treasuries, or nothing is promised against it | A fund's k is a standing choice made by a board; Laura's is settled promise by promise, on dates | UNVERIFIED at source (the hosted original is a scan with no text layer); three restatements read at source agree | No | This run: openjournals.libs.uga.edu; nomurafoundation.or.jp; soa.org |
| 12 | Sharpe and Tint's restated objective, E(R_A) - Var(R_A)/t + 2k(L/A)Cov(R_A, R_L)/t, splits the holdings into a hedge sized by k times L/A that does not depend on risk tolerance t, plus a risky part scaled by t (Keel derivation from the first-order condition, with a riskless asset beside the hedge) | Miyamoto (2005), appendix (the objective); Keel derivation | CERTAINTY, LADDER | NICHE | Even one-period surplus theory says the hedge for money owed is not a matter of taste | Mean-variance and one period; the derivation is Keel's, not in the sources read | Objective VERIFIED (restatement read at source, 19 Nov 2026); derivation Keel arithmetic | No | This run: nomurafoundation.or.jp |
| 13 | Rudolf and Ziemba's four-fund theorem: a riskless asset, the market, a hedge for interest-rate shifts and a liability hedge; "the liability hedge is independent of preferences and only depends on the funding ratio"; "The higher the funding ratio, the lower the necessity for liabilities hedging" | Rudolf & Ziemba (2004), abstract, introduction, conclusions | CERTAINTY, LADDER, COMPLETE2028 | NICHE | The ten Treasuries would be the same purchase for a bold or a timid Laura; with a first deposit about equal to their cost, 2027's money is all hedge, and in 2028 most of the new money is free | Their hedge is resized continuously; Caplet buys each hedge once and holds it to its date | VERIFIED (abstract, introduction and conclusions read at source, 19 Nov 2026) | No | This run: sciencedirect.com |
| 14 | Laura's funding ratio in January 2027 is about 1: $300,000 against the ten's $301,544 on the 6 Nov curve (99.5%, Keel arithmetic; 99.2% against $302,287 on the instruments held) | NUMBERS 1; CANON A11; Keel arithmetic | LADDER, COMPLETE2028 | NICHE | In row 13's terms all of 2027's money is hedge; a mean-variance surplus rule (row 10) would still put a slice in shares, and the IPS puts none in and completes the ten in January 2028 with the $2,388 top-up | Ratios on the latest curve, not on the January 2027 price | VERIFIED (register figures) | No | NUMBERS 1 and 5 |
| 15 | Merton: in the basic model the two funds are set "without knowledge of investors' preferences, wealth levels, or time horizons"; once rates can change it becomes a multifund theorem, and "simple financial instruments like bonds may serve the function of some of the funds" | Merton (1975), pp. 661, 667 | LADDER, FLOOR, PRESENTATION | NICHE | A safe asset made of ten Treasuries and a fund is no break with separation: a "fund" can be a set of bonds | Merton's funds serve everyone; Laura's safe fund is hers alone, built on her dates | VERIFIED (read at source, 19 Nov 2026) | No | This run: robertcmerton.com |
| 16 | Merton: an investor who fears that falling rates will cut his future spending "may hold long maturity bonds", whose gain offsets the fall | Merton (1975), p. 666 | LADDER, REINVEST | KNOWN | The ladder does this exactly, not statistically: once the ten are bought, a later fall in rates changes nothing their T-bonds pay; falling rates still touch interest on money waiting between a maturity and its payment, which the extra Treasuries cover (NUMBERS 2) | Merton's hedge is a correlation reset continuously; Laura's is cash on dates, held; an iBond fund pays its holdings' value at its end, not a fixed sum (NUMBERS 3) | VERIFIED (read at source, 19 Nov 2026) | No | This run: robertcmerton.com |
| 17 | Merton's named exception: "labor income which he cannot sell forward to eliminate its risk because of the moral hazard problem"; a specialised worker holds less of the shares that move with it, and if no security tracks it "he can do nothing to hedge" and keeps the two funds | Merton (1975), p. 668 | CAREER, CEILING | KNOWN | IPS l.9 in the theorem's own terms: her career changes how much of the market she holds, not which market, so VT stays the plain world fund | Merton's worker has one employer; Laura's income shrinks with the whole economy in recessions (IPS l.9) | VERIFIED (read at source, 19 Nov 2026) | No | This run: robertcmerton.com |
| 18 | Tobin's Nobel lecture: "uncertainties of both asset returns and earnings from human capital. Their covariances are very relevant to portfolio choice" | Tobin (1981), Nobel lecture | CAREER | NICHE | Tobin himself named IPS l.9's argument, 23 years after the separation paper | Said inside a model of the whole economy, not as advice to one investor | VERIFIED (lecture passages read at source, 19 Nov 2026) | No | This run: nobelprize.org |
| 19 | The author's exception to Merton: an advance sells labour income forward in part, paid in instalments "triggered by actions on your part, such as turning in manuscripts", and Laura's 2028 deposit comes partly from "publishing advances" | Merton (1975), p. 668; store Q95 rows 12-14; the case, "Laura's Financial Goals" | CAREER, COMPLETE2028, TWOREASONS | NICHE | The one part of her career the plan relies on is partly sold forward already, and IPS l.17 gives it the plan's only written exit tied to her career: a missed deposit | Her contracts are not in the case, so the deposit "can" depend on deliveries, never "does" (card Q95) | Keel inference on sources read at source (Merton this run; Q95 earlier) | No | This run (Merton); store Q95 |
| 20 | Buiter on Tobin: better than Tobin's own "Don't put all your eggs in one basket" is "you will only need two baskets for all your eggs" | Buiter (2003), pp. 3-4 and n. 4 | PRESENTATION | NICHE | Laura holds two baskets, Treasuries and VT, and the safe basket has a date on each egg | Buiter's two baskets share one safe asset common to everyone; Laura's safe basket is hers alone | VERIFIED (read at source, 19 Nov 2026) | No | This run: nber.org |
| 21 | Mean-variance needs quadratic utility or normal returns, and Tobin answered critics that the "extension from one moment to two was never advertised as the complete job or the final word" | Buiter (2003), p. 4, quoting Tobin (1969a) | CERTAINTY | NICHE | The IPS's departure from mean-variance (row 7) sits inside Tobin's own caveat | Tobin (1969a) not read; quoted through Buiter | VERIFIED (Buiter read at source, 19 Nov 2026); Tobin (1969a) UNVERIFIED at source | No | This run: nber.org |
| 22 | Did separation work where it was tried? The CAPM "falls empirically at the first hurdle", because most investors hold few assets and different risky mixes | Buiter (2003), n. 6 | CEILING | KNOWN | Laura's VT is the theorem carried out literally, which few individuals do; US index funds first held more money than active funds at the end of 2023 (store, card Q175) | An index fund holds a market of shares, not "the" market of every risky asset (row 31) | VERIFIED (read at source, 19 Nov 2026) | No | This run: nber.org |
| 23 | Tobin's line stopped at all-bonds: "Negative values of A1 and A2 are excluded by definition", so his investor never borrows; the later CAPM let investors borrow at the riskless rate | Tobin (1958), p. 71 | CERTAINTY, LADDER | NICHE | Like Tobin's 1958 investor, Laura never borrows (margin is banned in WInS too), so her Treasuries are paid for and no price fall can force a sale; UK pension funds that borrowed against their gilt hedge in 2022 were forced to sell (store Q2a-005) | Tobin's reason was institutional (only governments and banks issue cash and consols), not caution | VERIFIED (Tobin read at source, 19 Nov 2026); Q2a-005 read in an earlier run | No | This run: finance.martinsewell.com; store Q2a-005 |
| 24 | Tobin on stages: breaking the choice "into stages ... allocation first among, and then within, asset categories" seems "permissible and perhaps even indispensable" for the investor too | Tobin (1958), p. 85 | PROCESS, PRESENTATION | NICHE | Caplet's plan decides first which dollars are promised (dated, in Treasuries) and only then splits the free dollars between the late-2032 Treasury fund and VT | Tobin's stages were asset classes; Caplet's are promises | VERIFIED (read at source, 19 Nov 2026) | No | This run: finance.martinsewell.com |
| 25 | A pension fund owns what it has promised; Laura promises what she owns: Sharpe and Tint's fund is handed its debts and then invests, while on the facility side Caplet buys the Treasuries first (January 2028, and with half of VT before the 2031 meetings) and Laura names only a figure they will pay | Sharpe & Tint (1990) via rows 11-12; IPS l.15; NUMBERS 4 | COSPONSOR, MOVE2031, FLOOR | NICHE | Why the 2031 range is a rule about what is owned, not a forecast; the ten payments are the one part where the case wrote the debt first | No source found that runs the rule backwards; Keel synthesis | Keel inference | No | This run |
| 26 | Why the backwards order protects her: a 60/40 pension fund fully funded in January 1981 was 69% funded by June 1986 because falling rates raised its debts; a figure named only after its Treasuries are owned cannot be outrun by rates that way | Leibowitz (1987) via store Q1c-031; NUMBERS 3 and 4 | COSPONSOR, FLOOR | KNOWN | After the move nothing changes either end of her range (NUMBERS 4) | A fund's costs beyond its fees and an early end of the fund still touch it, which the 0.5% margin and NUMBERS 3 deal with | From store (read at source in an earlier run); register figures | No | Store Q1c-031; NUMBERS |
| 27 | Only two numbers in the plan are choices about risk rather than consequences of a date: "most" of the 2028 money left after the ten into the late-2032 Treasury fund (Keel's reading, 73.3%: $81,244 against VT's $29,594) and "half" of VT moved before the 2031 meetings | IPS l.15; NUMBERS 4 and 8o | HALFKEPT, FLOOR, CEILING | NICHE | Each is Tobin's one free choice, how much of the free money to keep safe; half sits in the middle of a nearly one-for-one trade, each $5,000 more of stated top costing about $5,300 of what she keeps | Never "optimal": both are Caplet's choices, given in the IPS's order of cause | Keel synthesis on register figures | No | This run |
| 28 | Pencil and ink in Sharpe and Tint's terms: nothing is ever stated at a k between 0 and 1; a figure is stated only once Treasuries she owns will pay it, and VT, owned but pencil, never carries a stated figure | Rows 11 and 25; CONCEIT V2.1 | PRESENTATION, MOVE2031 | NICHE | The conceit's rule has a named twin in pension theory, with the direction reversed | k is a weight on debts and ink is ownership, so this is a parallel, not an identity; never "the entry is ink" for VT | Keel synthesis | No | This run |
| 29 | Tobin's investor and Laura fear the same thing, a change in interest rates, and run opposite ways: he towards cash, because he counts his wealth next year; she towards dated Treasuries, because she counts hers on ten Januaries | Tobin (1958), pp. 66-71; IPS l.13 | CERTAINTY, LADDER | NICHE | A sentence that can open Section 2: an asset is safe or risky only for a date, which is the definition of ink | An iBond fund pays its holdings' value at its end, not a fixed sum (NUMBERS 3), so "safe for a date" is said of the Treasuries, never of a fund's payout | Keel synthesis on a source read at source | No | This run |
| 30 | Preferred habitat: investors with dated needs form "investor clienteles with preferences for specific maturities" (Modigliani and Sutch 1966), a view Vayanos and Vila tie to "Tobin's (1958, 1969) portfolio-balance theory" | Vayanos & Vila (2009), introduction; Vayanos & Vila (2021), introduction | LADDER | KNOWN | Laura is a small investor with ten habitats, one per January | A theory of bond prices, not of one investor's choice; Modigliani and Sutch's own text not read | VERIFIED (Vayanos and Vila read at source, 19 Nov 2026); Modigliani & Sutch (1966) UNVERIFIED (paywalled) | No | This run: nber.org; onlinelibrary.wiley.com |
| 31 | The "whole market" gap: the CAPM's market holds every risky asset, VT holds listed world shares, and Laura's largest risky holding, her career, is outside both | Buiter (2003); Merton (1975), p. 668 | CEILING, CAREER | KNOWN | VT is "the whole market" of shares; the career sits outside it, which is why the plan holds less of the market rather than a different mix | Keel inference | Keel inference | No | This run |

## Sources read

- Buiter, W. H. (2003). *James Tobin: An appreciation of his contribution to economics* (NBER Working Paper No. 9753).
  National Bureau of Economic Research. https://www.nber.org/system/files/working_papers/w9753/w9753.pdf. Retrieved 19
  November 2026 (section 1 and notes 3-6).
- Epstein, L. G. (1992). Behavior under risk: Recent developments in theory and applications. In *Advances in economic
  theory* (Cambridge Collections Online). https://doi.org/10.1017/CCOL0521430194.001; copy at
  https://people.bu.edu/lepstein/files-research/BehaviorUnderRisk-1992.pdf. Retrieved 19 November 2026 (section 2.4).
- Merton, R. C. (1975). Theory of finance from the perspective of continuous time. *Journal of Financial and Quantitative
  Analysis*, November 1975, pp. 659-674 (as printed). https://robertcmerton.com/wp-content/uploads/2015/11/Theory-of-finance-from-continuoustime.1975.pdf.
  Retrieved 19 November 2026.
- Miyamoto, S. (2005). *How households' balance sheets affect their asset allocation* [Conference paper, Nomura
  Foundation, 21-22 November 2005]. https://www.nomurafoundation.or.jp/en/wordpress/wp-content/uploads/2014/09/20051121-22_Sachiko_Miyamoto.pdf.
  Retrieved 19 November 2026 (section 3 and the appendix on the Sharpe-Tint model).
- Rudolf, M., & Ziemba, W. T. (2004). Intertemporal surplus management. *Journal of Economic Dynamics and Control, 28*.
  https://doi.org/10.1016/S0165-1889(03)00058-7. Retrieved 19 November 2026 (abstract, introduction, conclusions; issue
  and pages not checked).
- Russell, J. W., & Brooks, R. (1998). Managing college tuition inflation using a surplus framework methodology.
  *Financial Services Review, 7*, 257-271. https://openjournals.libs.uga.edu/fsr/article/download/3867/3314/10891.
  Retrieved 19 November 2026.
- Segal, U., & Spivak, A. (1990). First order versus second order risk aversion. *Journal of Economic Theory, 51*(1),
  111-125. https://doi.org/10.1016/0022-0531(90)90053-M (abstract at https://cris.tau.ac.il/en/publications/first-order-versus-second-order-risk-aversion);
  working paper, UCLA Economics Working Paper 540 (revised December 1988), https://scispace.com/pdf/first-order-versus-second-order-risk-aversion-49q0b13t6t.pdf.
  Retrieved 19 November 2026.
- Shang, K., & Hossen, Z. (2019). *Liability-driven investment: Benchmark model*. Society of Actuaries.
  https://www.soa.org/globalassets/assets/files/resources/research-report/2019/liability-driven-investment.pdf.
  Retrieved 19 November 2026 (section 2.1.4).
- Sharpe, W. F., & Tint, L. G. (1990). Liabilities: A new approach. *Journal of Portfolio Management, 16*(2), 5-10.
  https://doi.org/10.3905/jpm.1990.409248. NOT read at source: the copy at https://www.andreisimonov.com/NES/SharpeTint1990JPM.pdf
  is a scan with no text layer; its content here rests on Russell and Brooks (1998), Miyamoto (2005) and Shang and
  Hossen (2019).
- Skiadas, C. (2007). *Dynamic portfolio choice and risk aversion* [Handbook chapter].
  https://www.kellogg.northwestern.edu/faculty/skiadas/research/papers/handbook_skiadas_chapter.pdf. Retrieved 19
  November 2026 (section 4.4).
- Tobin, J. (1958). Liquidity preference as behavior towards risk. *The Review of Economic Studies, 25*(2), 65-86.
  https://doi.org/10.2307/2296205; read whole in the JSTOR copy at https://finance.martinsewell.com/capm/Tobin1958.pdf.
  Retrieved 19 November 2026.
- Tobin, J. (1981). *Money and finance in the macro-economic process* [Nobel Memorial Lecture, 8 December 1981].
  https://www.nobelprize.org/uploads/2018/06/tobin-lecture.pdf. Retrieved 19 November 2026 (passages on portfolio
  theory and human capital).
- Vayanos, D., & Vila, J.-L. (2009). *A preferred-habitat model of the term structure of interest rates* (NBER Working
  Paper No. 15487). https://www.nber.org/system/files/working_papers/w15487/w15487.pdf; published in *Econometrica,
  89*(1) (2021), https://onlinelibrary.wiley.com/doi/full/10.3982/ECTA17440. Retrieved 19 November 2026 (introductions).
- The case: *Laura Gao 2026 Client Profile*, "Laura's Financial Goals" (competition file, read 19 Nov 2026).

## Gaps

- **Sharpe and Tint (1990) at source.** The only hosted copy is a scan with no text layer; Firecrawl's credits were spent
  for the day and direct downloads are refused, so it could not be read or OCR'd. Rows 11-12 rest on three restatements.
  Next run: read the scan by eye or OCR it, and check that the paper itself uses k, calls it the importance of
  liabilities, and whether it says anything on fully funded plans.
- **Merton (1973), Econometrica.** The free copies are scans; the three-fund theorem is cited from Merton's own 1975
  summary and from Rudolf and Ziemba's introduction.
- **Modigliani and Sutch (1966)** and **Tobin (1969a)**, the reply quoted by Buiter: paywalled, not read.
- **Tobin (1983), "Liquidity preference, separation and asset pricing"**, *Zeitschrift für Betriebswirtschaft*: Tobin's
  own late look back at separation; not found online.
- **Cass and Stiglitz (1970)** on exactly when separation holds, and **Black (1972)** on separation with no riskless
  asset: not read; either could sharpen idea 1's break (with dates, no common riskless asset exists).
- Not found anywhere: a source that runs Sharpe and Tint's rule backwards, an investor naming her debt after buying its
  hedge (idea 3). That absence is the claim's novelty and its risk; a pension or insurance judge should be asked.

## Best three for the report

1. **Idea 1 with row 29 (2.0).** Tobin's risky asset was a default-free government bond, and Laura's plan holds that same
   asset as its safe one, because her wealth is counted on ten Januaries, not next year; it opens Section 2 with a fact
   most judges have never seen and leads straight into the definition of ink.
2. **Idea 2 with rows 7, 8 and 10 (2.0 or 2.3).** Tobin proved that no smooth taste for risk ever holds only the safe
   asset, so the IPS's "none of your 10 operating payments will depend on a share price" is a definition, not a degree of
   caution; Russell and Brooks's 34.8% in shares against a fully funded promise shows what the smooth rule would have done.
3. **Idea 3 with rows 25 and 26 (2.0 and 3c).** A pension fund owns what it has promised; Laura promises what she owns: the
   facility side runs Sharpe and Tint backwards, which is why her stated range cannot be outrun by rates the way a 1981
   pension fund's could.

Where it lands: Section 2's opening (2.0), where it explains the plan's one governing decision, that every promised dollar is held in Treasuries maturing before its own date and only money promised to nobody yet is held in VT, as Tobin's two baskets with the safe one defined by Laura's dates instead of by cash.
