# 04a. Lecture harvest: Damodaran (NYU Stern corporate finance) and Shiller (Yale ECON 252, 2011)

AI-generated research (Claude Code), Thu 5 Nov 2026, Sydney night, for the one writer of the Book 12 IPS. **Not
submission text and not an IPS draft.** The "plain idea" lines are notes on what a point means for Laura, phrased so
a 16-year-old could say it uncited. They are not sentences to paste. The IPS cites nothing; every source below goes to
the Final Report (due Sat 5 Dec 09:00 Sydney).

**How this was read.** curl is blocked, so every page was read with WebFetch on 5 Nov 2026. Damodaran's site loaded
(earlier tonight the proxy had refused it with HTTP 403: `IDEA_LIST_VERDICTS.md`). WebFetch gives quotes of at most
125 characters, so some quotes below are fragments, marked "[fragment]". Its extraction runs through a small model, so
before the Final Report quotes any line, someone should open the source and check the wording. Where the tool said it
was paraphrasing, I say so. Pages read in full or in part:
- Damodaran: `cflect.htm`; both lecture packets (`cfpacket1spr26.pdf`, `cfpacket2spr26.pdf`); the topic decks risk&ret,
  hurdlerate, invretA, invretB, capstruchoices, capstr, debtdesign, divintro, divassessment, valuation; the papers
  "What is the riskfree rate?" (Dec 2008), "Into the Abyss: What if nothing is risk free?" (Jul 2010) and "Equity Risk
  Premiums" (2008 edition, `ERPfull.pdf`); his home page (implied ERP for 1 Nov 2026); the investment-fable page
  "Stocks always win in the long term"; blog posts of 8 Oct 2008, 6 Feb 2010, 18 Feb 2011, 28 Jan 2026 and 3 Nov 2026.
- Shiller: the overview and chapter list of all 23 lectures. Transcripts read for 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
  12, 13, 14, 15, 16, 17, 18, 20, 21, 22 and 23; lecture 19's tail (Q&A only). Geanakoplos's leverage-cycle lecture is
  **not in ECON 252**: it is ECON 251 (Financial Theory) lecture 26, read too.

**Numbers.** None of the figures below are for the IPS. The IPS's numbers come from Keel's own curve and models.

---

## 0. The short version

1. **Two independent sources define "riskless" the way our ladder does.** Damodaran: the riskfree rate is "the rate
   on a zero coupon default-free bond matching the time horizon of the cash flow". Shiller (lecture 4): a 1-year
   government bond is riskless for a 1-year horizon "because the maturity matches my investment horizon"; a 10-year
   bond is not, "because the market price goes up and down". So safety comes from matching the date, not from the
   label on the asset.
2. **The same definition names our one weak point.** Damodaran: "Even a 5-year treasury bond is not risk free, since
   the coupons on the bond will be reinvested" [fragment]. The textbook cure, a zero-coupon Treasury, is STRIPS, which
   Wharton bans. So the plan uses coupon bonds and prices the coupons as if they earned nothing. US cash rates sat just above zero
   (a 0-0.25% target) from Dec 2008 to Dec 2015, and Shiller teaches zero as the floor ("no one would lend at a
   negative interest rate").
3. **The best new framings come from public finance and pensions, not from markets.** These are operating budget
   versus capital budget (Shiller 22) and defined benefit versus defined contribution (Shiller 20). Each maps exactly
   onto the case's two pots: the ten payments must balance with no borrowing, and the gift is whatever is owned.
4. **The 2031 lock has a precise reason in Damodaran's own words.** "Companies that lock themselves into fixed
   dividends are in effect turning their equity into quasi bonds" (blog, 18 Feb 2011). Once Laura names the top, that
   half of her shares is already a quasi-bond, so she turns it into a real one. Shiller (lecture 9, naming Lintner):
   "Once they start paying a dividend, they've got to keep paying it."
5. **A fixed payment funded by shares works like a margin call that falls due on a known date.** Geanakoplos's
   leverage cycle crushes whoever must sell into a fall. Greenberg (lecture 14), on AIG: "I don't care how big you
   are, you run out of cash." Because of the ladder, Laura never has to sell a share to pay a January.

---

## 1. Damodaran

Verdicts: **USE** (sharpens the plan or its argument as it stands) | **ADAPT** (true, but needs bending to fit) |
**REFUSE** (looks relevant but isn't) | **FR** (Final Report only).

### 1A. The riskfree rate: the plan's foundation

| # | What he says (source) | How it bears on Caplet XR | Verdict |
|---|---|---|---|
| D1 | Two conditions: "There can be no default risk, which generally implies that the security has to be issued by the government." and "There can be no uncertainty about reinvestment rates, which implies that it is a zero-coupon security with the same maturity as the cash flow being analyzed." "The riskfree rate is the rate on a zero coupon default-free bond matching the time horizon of the cash flow being analyzed." (packet 1; hurdlerate deck) | The ladder is this definition made real: for each January, one Treasury holding that pays out before that date. Riskless is a property of the match, not of the asset. | **USE** |
| D2 | "A six-month treasury bill rate, while default free, will not be risk free, because there is the reinvestment risk of not knowing what the treasury bill rate will be in six months." (riskfree paper, p. 6). "The risk free rate for a five-year time horizon has to be the expected return on a default-free (government) five-year zero coupon bond." (p. 6) | Cash is not riskless for a dollar Laura owes in 2038, and "holding cash to be safe" fails a dated payment. | **USE** (with D1) |
| D3 | "Even a 5-year treasury bond is not risk free, since the coupons on the bond will be reinvested" [fragment; the tool paraphrased the rest as reinvestment at rates that "cannot be predicted today"] ("Into the Abyss", p. 5) | This is our weak point, in the definition itself. A coupon bond held to maturity is exact on its principal but not on its coupons, because they arrive early and wait. The zero-coupon fix (STRIPS) is banned, so we price the waiting coupons at zero. | **USE**: the single best find |
| D4 | "A purist's view of risk free rates would then require different risk free rates for each period" ("Into the Abyss", p. 5). The practical shortcut: "we could use a variation on this duration matching strategy, where we use one riskfree rate on all of the cash flows, but set the duration of the default-free security" [fragment] (riskfree paper, p. 9) | This is the academic version of the pension-fund sentence already in the FINAL IPS. Duration matching (one rate, rebalanced) is the practitioner's shortcut. One bond per payment is the purist's answer, and Laura can afford the purist's answer. | **USE** (as the FR source for the existing sentence) |
| D5 | "While government bonds may offer returns that are risk free in nominal terms, they are not risk free in real terms" and "An inflation-indexed treasury security (TIPs) does not offer a guaranteed nominal return to buyers" (riskfree paper). "If the cash flows are nominal (real), the discount rate has to be nominal (real)." (invretA) | Laura's payments are fixed nominal dollars, so a nominal Treasury is their exact riskless match. A TIPS would add risk to a nominal liability, so the ban costs this plan nothing. This fills the gap the verdict file found: no draft states an inflation assumption. Inflation can't change a fixed $50,000. It lands on what each payment buys and on the building, and that is why the unpromised half stays in shares. | **USE** |
| D6 | "The riskfree rate that you use in an analysis should be in the same currency that your cashflows are estimated in." (packet 1). "If cash flows are in dollars ($R), the discount rate has to be a dollar ($R) discount rate" [fragment]. His own worked example: "The Rio Disney Theme Park analysis was done in dollars, even though the project will be based in Brazil" (invretA). Across currencies, "the only significant factor that can cause differences is expected inflation" (riskfree paper, p. 12). | The promise is written in US dollars, so its riskless asset is a dollar Treasury. A residency in Taiwan funded in dollars is Damodaran's Rio case. The Taiwan-dollar risk is real, but it sits on the building and on what each payment buys there, not on the funding. The FINAL IPS already has "a cushion if the building costs more in Taiwan dollars". | **ADAPT** (one clause at most; it supports the existing line) |
| D7 | "Note, however, that not all governments can be viewed as default free." (hurdlerate). His home page for 1 Nov 2026 uses "the US treasury rate of 5.29% used as the riskfree rate in US dollars" and a US default spread of 0.22%, "to get to an adjusted dollar riskfree rate of 5.07%". Moody's cut the US to Aa1 in 2025 (blog, 28 Jan 2026: "lowered its rating, albeit marginally to Aa1"). | The residual risk is US default, and one careful analyst prices it at about a fifth of a point. That's worth naming as the one risk left (the verdict file's top-8 #5), not worrying over. | **FR** (one clause in the IPS at most: "US credit" as the risk left) |
| D8 | "the absence of a riskfree investment will make investors collectively more risk averse" ("Into the Abyss") | Interesting, but about markets, not Laura. | **REFUSE** for the IPS |

### 1B. Debt design, mirrored

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D9 | "The objective in designing debt is to make the cash flows on debt match up as closely as possible with the cash flows that the firm makes on its assets. By doing so, we reduce our risk of default, increase debt capacity and increase firm value." (debtdesign, slide 109; joined from two fragments) His design tree runs Duration/Maturity, Currency Mix, Fixed vs. Floating, Straight vs. Convertible (slide 119). | The ladder is the same rule turned around: firms match debt to their assets, and Laura matches assets to her debt. His "increase debt capacity" has a twin: once the payments are matched, everything left can carry risk without touching a payment. All four of his branches fit: maturity (one per January), currency (dollars), fixed (nominal $50k, so fixed-coupon Treasuries), straight (no options, which are banned anyway). | **USE** as an argument; **FR** for the name |
| D10 | "The perfect financing instrument will have all the tax advantages of debt while preserving the flexibility offered by equity" (slide 112; joined from fragments) | The gift's version: the perfect gift instrument would have a bond's certainty and equity's upside. Banks sell exactly that as a capital-protected note, which the FINAL IPS already rejects for owned shares. Damodaran gives the frame, but it isn't needed in the IPS. | **FR** |
| D11 | Mismatch examples: Disney's assets "collectively have a duration of about 2.33 years"; "The perfect debt for this theme park would have a duration of roughly 19 years" (slides 125, 140) | Illustration only. | **FR** |

### 1C. Hurdle rates and the investment principle

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D12 | "Invest in assets that earn a return greater than the minimum acceptable hurdle rate"; "If you cannot find investments that make your minimum acceptable rate, return the cash to owners of your business" (packet 1, "Maximize the value of the business") | For Laura, every share must beat the Treasury rate for the same date. For the payment money, the hurdle includes the cost of a missed payment, which no share clears, so no share sits behind a payment. For the gift money, her shares are bought only with the floor fund's interest, so the worst they can cost her against all-Treasuries is that interest. This is the verdict file's "Treasury hurdle" (#3), now with its textbook root. | **ADAPT** |
| D13 | "Use cash flows rather than earnings. You cannot spend earnings." (invretA) | Its twin for Laura: a held bond's price between now and maturity changes the statement, not the cheque. She can't spend a market value either, only what matures. | **ADAPT** (supports idea bank FRB-62) |
| D14 | "Caveat 1: When analyzing the effects of changing a variable, we often hold all else constant." "In the real world, variables move together." (invretA, sensitivity slide) | One line of theory behind "her income and share prices fall together" (human capital). | **FR** |
| D15 | The cost of capital as "the Swiss Army Knife of finance"; hurdles "set about 2-3% higher than justified by market numbers" (blog, 3 Nov 2026) | About companies. | **REFUSE** |

### 1D. Capital structure: flexibility has a price

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D16 | Costs of debt include "Loss of Future Flexibility: Using up debt capacity today will mean that you will not be able to draw on it in the future." Proposition 5: "Other things remaining equal, the more uncertain a firm is about its future financing requirements and" [fragment; it ends, in substance, "the less debt it should use"] (capstr, slides 13, 23) | A promise is Laura's version of debt. The more uncertain the Taiwan building's needs, the less of her surplus she should promise. That's why half her shares stay unpromised: it's what the case means by "preserving flexibility", argued rather than asserted. | **USE** |
| D17 | A CFO survey ranks "Maintain financial flexibility" first, at 4.55 out of 5 (packet 2, slide 24). "Managers value flexibility." (slide 30) | Evidence that flexibility is what real finance chiefs rank first. | **FR** |
| D18 | Debt "Adds discipline to management" (capstr, slide 13) | One stretch: the ten payments discipline Laura, because they can't be raided. The motif already carries this. | **REFUSE** for the IPS (no need) |
| D19 | Debt's "contractually pre-set payments that have to be made, no matter what the firm's financial standing" (capstruchoices, slide 10) | This is what Laura's ten payments are: a fixed claim, ahead of everything else. It's the verdict file's leverage point (#1) in Damodaran's words. | **ADAPT** (FR source for "the payments are a debt in front of the building money") |

### 1E. Dividends: why a named number must be owned

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D20 | "The best way to describe dividend policy at most US and European companies is that dividends are sticky." "Companies that lock themselves into fixed dividends are in effect turning their equity into quasi bonds" (blog, "Dividend Policy for the 21st century", 18 Feb 2011). "Cutting dividends is viewed as an action of last resort, when all else has been tried and failed." | This is the cleanest reason for the 2031 lock. Once Laura names a top, the half of her shares behind it has become a quasi-bond: a fixed claim held in a volatile asset. Turning it into a real bond (Treasuries) before she names it just makes the asset match the promise. The FINAL IPS's "a number said aloud can't quietly be halved after a bad year" gets its mechanism. | **USE** (strong) |
| D21 | His fix for sticky dividends is to "tie dividends to residual cash flows, computed after reinvestment needs have been met", which "preserves the commitment feature of conventional dividends without the inflexibility"; and contingent dividends, "partially or fully tied to movements in oil prices" (same post) | Laura's range has this shape: a bottom that is committed (owned) and a top set by what is left (half the shares), fixed only when owned. Her kept half is the uncommitted residual. Don't cite the "residual payout" idea as a yearly payout: there is one gift, once. | **ADAPT** |
| D22 | "Inertia: Companies seem to hate to let of their past [sic], when it comes to dividend policy." "Me-too-ism" (divintro, slide 150). 2020: increases or initiations "vastly exceeded the number that cut or suspended dividends (69)" [fragment] (slide 152; the slide gives both 287 and 298 for increases and doesn't reconcile them) | Evidence of stickiness. Don't use the S&P counts: the slide's numbers disagree with each other. | **FR** (qualitative only) |
| D23 | "Dividends can be signals to the market that you believe that you have good cash flow prospects in the future." (divintro, slide 176) | ADAPT, inverted: Laura doesn't need to signal, because she can disclose. The bottom of her range is a Treasury fund that co-sponsors can be told about. A verifiable fact beats an inferred signal (Shiller 12: "the SEC is built around disclosure"). | **ADAPT** (FR, for the co-sponsor text) |
| D24 | The bird-in-hand argument: "Dividends now are more certain than capital gains later. Hence dividends are more valuable than capital gains." The counter: "The appropriate comparison should be between dividends today and price appreciation today." (divintro, slide 173) | **Devil's advocate a judge could raise:** isn't moving half the shares into Treasuries in 2031 a bird-in-hand fallacy that gives up return for comfort? No. The lock isn't about valuing certainty more. Naming the top creates a new fixed claim, and a fixed claim needs a matched asset (D20). The cost is about two years of share growth on the promised half (verdict file, C1). | **FR** (answer kept ready) |
| D25 | "The Cash/Trust Nexus": "Evaluate whether you can trust the managers of the company as custodians of your cash." (divassessment, slide 189) | Co-sponsors judge Laura the same way: trust follows from her never having to cut. | **FR** |

### 1F. Valuation consistency

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D26 | "the discount rate used should be consistent with both the riskiness and the type of cashflow being discounted." "Errors in estimating the discount rate or mismatching cashflows and discount rates can lead to serious errors in valuation." (valuation, slide 237) | Value the range's bottom at the Treasury rate (it is owned). Never value a promised top with a share forecast. This supports defining certainty by ownership, not by a model probability. | **USE** (inside find 9 below) |
| D27 | "The Numbers People" have the illusion that "Precision: Data is precise"; "The Narrative People" believe "If the story is good, the investment will be." (valuation, slide 232) | A method note for the team: every number needs its story, and every story needs its number. | **FR** |

### 1G. The equity risk premium and "stocks for the long run"

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D28 | "Implied ERP on November 1, 2026 = 4.41% (Trailing 12 month, with adjusted payout)", with the 5.29% US Treasury rate (home page, read 5 Nov 2026). | This replaces the unverified 4.23% in `IDEA_LIST_VERDICTS.md` (A5). **Conflict:** his blog of 3 Nov 2026 uses "the 10-year treasury rate of 4.9% on October 26, 2026". The two can't both be the same rate, so check before quoting either. Adding the 4.41% premium to the 5.29% rate (about 9.7% expected for US shares) is not comparable with Keel's 7.5% compound world-share basis. | **FR only**, and the 5.29% vs 4.9% conflict is **UNVERIFIED** |
| D29 | Standard errors of historical premiums (Table 2, 2008 edition): 8.94% (5 years of data), 6.32% (10), 4.00% (25), 2.83% (50), 2.23% (80). "Even using the entire Ibbotson data (approximately 80 years) yields a substantial standard error of 2.23%." (`ERPfull.pdf`, p. 19). The arithmetic is a 20% yearly standard deviation divided by the square root of the years. | Even a century of data pins the share premium down only to about plus or minus 2 points. That's the best reason why nothing Laura says aloud rests on a forecast of share returns. It supports the FINAL IPS's choice to make both ends of the range owned. | **USE** (as an argument; never the number in the IPS) |
| D30 | "Stocks always win in the long term" (investment fables page): stocks beat bonds over "any twenty-year period that you look at since 1926" in US data, but "While a conservative advisor may mean 20 years or longer when he talks about long term," aggressive advisors shorten it. Pro-equity books "peaked in 1999 at the height of one of the great bull markets of all time." | This supports the FINAL IPS's "time makes a loss rarer, not smaller" line, and its source for the critique of Siegel. Note that the fable page itself does not discuss Japan, survivor bias or starting valuations. | **USE** (supports an existing line); **FR** for the source |
| D31 | Dimson, Marsh and Staunton's 17 markets from 1900: the 16-market average premium over long governments was 4.04% against 4.52% for the US, and "the difference in returns captures the survivorship bias." (`ERPfull.pdf`, pp. 26-27; this is the 2008 edition and its numbers are stale) | US history is the luckiest market's history (idea bank #24 already says so). | **FR** (use the latest DMS yearbook, not these figures) |
| D32 | Negative serial correlation: "the arithmetic average return is likely to over state the premium." (`ERPfull.pdf`, p. 22) | Keel's models already use compound returns. | **REFUSE** (already done) |

### 1H. Real options and flexibility

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D33 | The options to delay, expand and abandon; "The value of these rights increases with the volatility of the underlying business." "These options all add value to projects and may make a 'bad' project (from traditional analysis) into a good one." (invretB) | Laura's unpromised half is an option: to cover a cost overrun, to expand, or to wait. Its value rises with how uncertain the building is, and promising it would kill the option. The verdict file (B2) reached the same view. | **ADAPT**: one clause in the IPS at most (the reason, never the word "option"); **FR** for the theory |
| D34 | "An opportunity cost arises when a project uses a resource that may already have been paid for by the firm." (invretB) | The 2031 lock's cost is an opportunity cost: the share growth given up on the promised half. Name it in the FR. | **FR** |

### 1I. Risk and return, and diversification

| # | What he says | Bearing | Verdict |
|---|---|---|---|
| D35 | "Firm-specific risk can be reduced, if not eliminated, by increasing the number of investments in your portfolio"; "Market-wide risk cannot." (risk&ret) | Supports "one world index fund holding thousands of companies". The fund removes firm risk, and the ladder keeps market risk away from the payments. | **USE** (it's the existing line's logic; it needs no new words) |
| D36 | "This market has tested the core belief in diversification." "The correlation across equity markets has risen dramatically." "I think that not diversifying is a deadly mistake for most investors." "we need to temper the sales pitch." (blog, 8 Oct 2008) | Diversifying across shares doesn't protect a dated payment in a crash, because correlations rise just when it matters. That's one more reason the payments hold no shares (see Swensen, S6). | **ADAPT** (fused into find 11) |
| D37 | "making risk a mix of danger and opportunity. You cannot have one, without the other." (risk&ret, the slide on the Chinese symbols for risk) | **REFUSE.** It's a cliché, and the "Chinese characters for crisis mean danger plus opportunity" claim is disputed by linguists. A reader who knows that would mark it down. | **REFUSE** |

---

## 2. Shiller, Yale ECON 252 (Financial Markets, spring 2011), all 23 lectures

| L | Title (guest) | What it says, with verified quotes | How it bears on Laura's plan | Verdict |
|---|---|---|---|---|
| 1 | Introduction | Finance "is about allocating resources through space and time"; "it's about managing risks". On wealth with a purpose: a fortune is "meaningless unless you give it away"; Carnegie said the rich should "take their fortune and give it all away before they die"; Gates and Buffett "commit to give most of their wealth away, while they're still alive". | "Space and time" fits Laura exactly: 2027 money moved to 2033-2042, and US dollars moved to a Taiwan residency. But as an IPS line it's a slogan. | **FR** (opening of the Final Report) |
| 2 | Risk and financial crises | "independence is something that apparently breaks down at times like these"; "there might be episodes when everything goes wrong at the same time." On fat tails: the 1987 crash "went down 20.47% in one day"; "If you believe in normality, October 19, 1987 couldn't happen." On the geometric mean: "if there's ever a year in which the return is minus 100%, then the geometric mean is 0." "Because you care a lot, if the guy wipes you out." Survivorship: "for every one of them that you read about, there's 1,000 of them that got squashed." | (a) Her income and share prices can fall together, because independence fails in a crisis: the theory behind "bet on shares twice". (b) The normal curve underrates crashes, so defining "high certainty" as a model probability is fragile, and ownership isn't. | **USE** (a and b, as arguments) |
| 3 | Technology and invention in finance | "Finance is all about inventions." The first indexed bond: "issued in the state of Massachusetts in 1780"; the US revived them only in 1997. Chile's Unidad de Fomento (1967). "There's a slowness to understand or appreciate invention." | TIPS are banned, and a nominal liability doesn't need them (D5). | **REFUSE** for the IPS; **FR** footnote at most |
| 4 | Portfolio diversification | "there is no best investment. There's only a trade-off between risk and return." The riskless asset: "It's not risky, because the maturity matches my investment horizon. I know exactly what I'm going to get." Ten-year bonds held for a year: "they're risky, because the market price goes up and down. They're not riskless." Norway: about "70% of its portfolio in oil"; "if the market for oil collapses, Norway is in big trouble. They're not diversifying enough." His fix: "You can short the futures market for oil". CAPM: "Risk is covariance. It's co-movements." | (a) This is the second, independent source for riskless = matched date (with D1). (b) Norway is human capital on a national scale: wealth already exposed to one risk shouldn't buy more of it. Laura's book, speaking and licensing income is her North Sea oil. His remedy, a derivative, is banned for her, so the plan's defence is to never put shares behind a payment. | **USE** (a); **ADAPT** (b: supports the existing line; the Norway story goes to the FR) |
| 5 | Insurance | "The fundamental concept, again, is risk pooling." Moral hazard: you "take out fire insurance on your house, and then you burn it down deliberately." AIG: "it was almost entirely due to a failure of the independence assumption"; "$182 billion committed to bail out AIG"; "The company lost over 90% of its shareholder value". Life insurance: "What it really insures, is your family against the loss of a bread winner." Counterparty: "you have to look at the insurance company that you buy insurance from." | (a) Laura is her own breadwinner, and the 2028 deposit depends on her career. So the plan buys the payments with money she already has and asks the deposit only to complete the ladder and buy the floor. (b) "Look at the insurer": a bank's capital-protected note is only as good as the bank (see find 12). | **ADAPT** (a supports an existing line); **USE** (b) |
| 6 | David Swensen (Yale endowment) | "Asset allocation is far and away the most important tool that we have available to us as investors." "in a panic, only two things matter: risk and safety." "Investors sold everything that had risk associated with it to buy U.S. Treasuries." "The only diversification that would matter in that instance is owning U.S. Treasuries." But a holding of "25, 30, 35%" in Treasuries means that "under normal circumstances ... you're paying a huge opportunity cost." Horizon: endowments have "a longer time horizon than any investor that I know"; the mission is "to preserve the purchasing power of the portfolio in perpetuity"; "if you've got a long time horizon, you should be rewarded by accepting equity risks." Individuals should "implement it using index funds, which are low-cost ways of mimicking the market". "an individual has almost no chance of beating the market." 1987: "they sold stocks and bought bonds. Same thing, buying high, selling low." **Not in this lecture:** spending rules, the 80/20 smoothing rule, a 5.25% rate, an illiquidity premium by name. | This explains why an investor who admires Yale still doesn't copy it. Yale treats Treasuries as costly insurance because its money is needed forever. Laura's payment money is needed on ten dated Januaries, so for that money a Treasury isn't insurance, it's the match, and its "opportunity cost" is the price of certainty. Her surplus does what Swensen tells individuals to do: one low-cost index fund, no market timing. | **USE** (strong, niche) |
| 7 | Efficient markets | The hypothesis is "a half-truth": "It's a half-truth, it's half true. Remember that, but don't put too much faith in it, either." "The insight is that people get deceived when they look at stock price charts." "You can beat the market, but simple trading rules like Edwards and McGee are not powerful, short-run profit opportunities." | The plan makes no market calls: it holds an index fund and changes only on dates. That's safe whether markets are efficient or not. | **ADAPT** (supports "never on a market move"; needs no new words) |
| 8 | Theory of debt, its proper role, leverage cycles | "Present discounted value is one of the most fundamental concepts in finance." "Anything in the future is worth less." A coupon bond: "That means that it's really an annuity and a discount bond together". Term structure: "Expectations theory says that the forward rate equals the expected spot rate"; Hicks added a risk premium, so forward rates tend to sit above expected spot rates. Böhm-Bawerk's three causes of interest; usury, from *usura*. **Leverage cycles: despite the title, none of the transcript I read discusses them** (the chapters are interest-rate theory, present value, the term structure, usury, and Elizabeth Warren). | (a) "An annuity and a discount bond together" is the plainest way to see our weak point. The discount-bond part pays on its date; the annuity part (the coupons) arrives early and waits. (b) Pricing the waiting coupons at zero is more cautious than any forward rate the market quotes. | **USE** (a); **FR** (b) |
| 8b | Geanakoplos, *The Leverage Cycle and Crashes* (**ECON 251** lecture 26, 2009, not ECON 252) | "in order to guarantee that you're going to keep your promise you have to put up collateral"; "Leverage means high prices." "the leveraged buyers get crushed, go out of business and leverage collapses." "So the most optimistic people in the economy, they're just out of the economy." "It's because the thing has fallen into more pessimistic hands." From the overview: the drop in prices "is amplified far beyond what any market participant would expect from the news alone." | Whoever must sell in a fall gets crushed. A portfolio that owes $50,000 every January out of shares is a forced seller on a timetable, and with the ladder Laura never is. (Margin is banned, but the point isn't margin. A fixed payment due from shares acts like a margin call on a known date.) | **USE** (fused with L14: find 5) |
| 9 | Corporate stocks | "There's a famous article by John Lintner." (no year given: "It was a long time ago"). Firms "think they should pay out a certain fraction of their earnings, because the shareholders will get mad"; "they don't want to adjust upward quickly if earnings shoot up." "one thing we don't ever want to do is cut our dividends." "Once they start paying a dividend, they've got to keep paying it." Price "ought to be ... the present value of expected future dividends." | Lintner's managers raise a dividend only when they're sure they can keep it. Laura's named range is that kind of dividend, so she names only money she owns. A verified classroom source for the FINAL IPS's 2031 reason, fused with D20. | **USE** (with D20) |
| 10 | Real estate | Pre-1934 mortgages "tended to be two to five years, and they were balloon payment": "You come back to us and we'll do it again, if we feel like it". In the Depression: "The bank says no dice; you're not going to get renewed." "You're forced to dump your house on the market." The 1934 fix: FHA-insured mortgages "must be 15 years or longer" and "cannot be a balloon payment mortgage"; by the 1950s, 30-year mortgages with "no surprises". Moral hazard in origination: "I'll sell the mortgage to someone else, and I'm out of here." | Buying a short bond and rolling it is the balloon mortgage in reverse, because each renewal depends on that year's terms. The ladder never rolls: each January's money is in place from 2027. It's a vivid history behind "cash is not safe for a dated payment" (D2). | **ADAPT**: near-miss for the IPS; **FR** story |
| 11 | Behavioral finance | Prospect theory: "We don't weigh gains and losses linearly." "The kink means that people are very conscious of little changes in their wealth and they're spooked by them." Framing "is presentation"; "I can give the same prospect to people, but word it in different ways that suggests a different reference point." Anchoring: "That wheel has nothing to do with the answer." Regret: "people fear the pain of regret"; "You may make bad decisions, because you're overly worried about regret." Overconfidence: "everyone is overconfident." Herding: "This herd behavior creates big swings in the stock market". **Not in this lecture:** the equity premium puzzle and myopic loss aversion. | (a) The 2031 number becomes co-sponsors' reference point. Falling below it feels like a loss, which hurts more than an equal surprise above it pleases, so the bottom must be owned. That's the behavioral reason under Lintner. (b) Regret pulls the other way: after a rally in 2031 Laura may want to keep all her shares. The dated rule decides for her. (c) Overconfidence is why no promised number rests on our own forecast. | **USE** (a, fused into find 7); **ADAPT** (b, c) |
| 12 | Misbehavior, crises, regulation | "So, the SEC is built around disclosure." Brandeis: "Sunshine is the best disinfectant." Prospectuses "that no one could understand without a law degree"; "He wanted plain English." (who "he" is was not checked: **UNVERIFIED**) | Co-sponsors are better served by disclosure than by a signal (D23). Plain words in the co-sponsor text. | **FR** |
| 13 | Banks | "But banks offer liquidity by borrowing short and lending long." "The banks, in normal circumstances, generate liquidity, but they create a system that's vulnerable." Diamond-Dybvig: "Their model has a good equilibrium and a bad equilibrium, and it depends on expectations." "all it takes is for people to suddenly change their expectations, and then it all falls apart because you have a run." "As long as people believe the bank system is sound, it is sound." | The ladder is the opposite of a bank: no maturity mismatch, since every holding pays out before the payment it serves. So its soundness doesn't depend on anyone's belief, and nobody can run on it. Co-sponsors' confidence follows from ownership instead of holding the plan up. | **USE** (niche) |
| 14 | Hank Greenberg (former AIG chief) | "I don't care how big you are, you run out of cash, which they did." The CDS trigger changed so that "the instrument didn't have to default, it simply had to lose value." "I would not have responded to the call for collateral, when you couldn't tell what the price discovery really was." "More diversification in your business provides greater stability." | AIG fell because a fall in value triggered calls for cash. Laura's ladder held to maturity has no trigger: a price fall changes nothing she owes or owns at maturity. | **USE** (fused with 8b: find 5) |
| 15 | Forward and futures markets | "I can lock in this price today, because that's what the futures market does." On oil: "If you bought an oil futures contract, you weren't impacted by this." Contango and backwardation defined. "speculation is just business." | Buying the ladder in 2027 locks in the cost of the 2033-2042 payments, as a forward would, with no derivative: a bond held to maturity is a forward you own outright. This is the verdict file's #7 ("buy the reserve in 2027, then let it run"). | **ADAPT** (supports #7; one clause at most) |
| 16 | Laura Cha (Hong Kong regulator, HSBC) | China, Hong Kong, HSBC and Basel III; "the renminbi is still a non-convertible currency". Nothing on Taiwan or the Taiwan dollar. | None. | **REFUSE** |
| 17 | Options markets | Put-call parity: "it says that the stock price equals the call price minus put price plus exercise price on the last day". "Because if it didn't hold, there would be an arbitrage, profit opportunity." "insurance is like options, and insurance gives you peace of mind." Implied volatility is "the options market's opinion as to how variable the stock market will be". First options exchange: "the Chicago Board Options Exchange, which came in in 1973." Two purposes of options: completing markets, and "attention anomalies and salience". | Rearranged, parity says a guaranteed amount plus a call equals the shares plus a put. Caplet XR builds the floor-plus-upside out of owned pieces: a Treasury for the floor, shares bought with its interest for the upside. No option, no bank, and the dividends stay hers. It explains the FINAL IPS's capital-protected note line. Derivatives are banned, so the IPS must not look as if it plans one. | **FR** (theory behind an existing line) |
| 18 | Monetary policy | Spring 2011: "Right now, they've set it virtually at zero, because the economy is so weak." "the current federal funds rate in the United States is 0.13%". "It can't go below zero, because you can't have negative interest rates--no one would lend at a negative interest rate." Central bank independence exists because "a government might want to inflate the currency." Bank of England "founded in 1694". | Pricing the waiting coupons at zero isn't an invented stress, because US cash rates sat just above it for seven years (verified: target range 0-0.25% from 16 Dec 2008, FRED; "until December 2015", Chicago Fed; back on 15 Mar 2020, Chicago Fed). And zero is a true floor for someone who can hold cash. (Euro and yen rates later went below zero, so the "can't go below zero" line is a 2011 view. Dollar cash held as cash still can't earn less than zero.) | **USE** (inside find 1) |
| 19 | Investment banks (Q&A read: guest Jon Fougner) | Facebook, Goldman's client focus, careers. Nothing on Treasuries or underwriting in the part read. | None. | **REFUSE** |
| 20 | Professional money managers | ERISA's "prudent man rule" requires "care, skill, prudence, and diligence"; the law makes managers "behave, not as they would behave, but as they think other people would behave", creating "a class of institutional investors, who live in fear of laws". Defined benefit: "They defined the benefit that you would receive when you retired"; hitting that target is "kind of a tricky problem, if you're a manager." Defined contribution: "a defined contribution pension plan doesn't promise what you'll get in retirement." Spendthrift trust: "the child cannot get at the assets, only the income." Yale: "In 1825, Yale University put its entire endowment in an investment in the Eagle Bank of New Haven." "It went to zero." Yale "had no endowment after 1825." Family offices: "if you have $100 million in assets, 5% income is $5 million a year." **Not in this lecture:** *Harvard College v. Amory* and Justice Putnam. | (a) **DB versus DC:** the ten payments are a defined benefit, a fixed target, so they're matched with bonds. The gift is a defined contribution, whatever the shares become, until 2031, when only owned money is turned into a promise. (b) The Eagle Bank is a vivid diversification story for the shares. It also raises the obvious question about the ladder, all of it with one issuer, which D7 answers: that issuer prints the dollars it owes, and its default is priced at about 0.2 of a point. (c) The spendthrift trust is the ladder's shape, releasing each January's payment and never the principal early, but the motif already carries it. | **USE** (a); **FR** (b, c) |
| 21 | Exchanges, brokers, dealers, clearinghouses | "There had been a development of programs that were called portfolio insurance sell strategies." "They called it portfolio insurance, but it wasn't really insurance. It was an automatic sell strategy." "It's like a stop loss order, but a more sophisticated one that could be executed in continuous time by a program." The Brady Commission "concluded that program trading, computer trading, had played a big role in the drop." Dealers: "all it takes is a few bad moves, and you can be wiped out." | Verified source for the FINAL IPS's 1987 line. The plan's floor is bought, not manufactured by selling as prices fall, so it never has to sell into a crash. | **USE** (verifies an existing line; FR source) |
| 22 | Public and non-profit finance | State and local governments "typically have two budgets": "an operating budget and a capital budget." "The operating budget is what has to be balanced, according to their constitutions." "they cannot plan to run a deficit in some states." "If a city builds a new school, for example, that's not an operating expense, right? It's a capital expense." "it's building something that will last through the ages". Rainy-day funds: "the city has an endowment, which can help tide them over through difficult times." "But recently, most of the rainy day funds have been exhausted." Nonprofits have "no owners, in the sense that there's no shareholders." Social entrepreneurs "do things out of a sense of mission, beyond making money". "People respond to incentives, but they respond to pleas to their morality as well." | **Operating versus capital budget is the case's structure in public-finance terms.** The ten payments are the residency's operating budget. It must balance and must never rely on borrowing or on a good year, so it's fully funded first. The facility is a capital project, a building "that will last", so it's sized from what's left and may flex. The operating reserve from 2033 is the residency's rainy-day fund, and Shiller's warning that rainy-day funds get "exhausted" is why it's matched rather than merely saved. | **USE** (strong, new) |
| 23 | Finding your purpose | "you have to think about the next five decades"; "maintain an orientation toward history in the making"; "it seems unrewarding just to give to charity" (he points instead to building institutions, such as Grameen Bank); "we haven't finished democratizing finance"; livelihood insurance: "I think that we can insure those things". | Laura is building an institution, not just giving, which fits the Final Report's client story. | **FR** |

**Asked for but not found in the 2011 transcripts I read** (lectures 2, 4, 6, 7, 9, 11): the equity premium puzzle
(Mehra-Prescott), myopic loss aversion, Jeremy Siegel and *Stocks for the Long Run*, Shiller's 1981 excess-volatility
result, Samuelson's dictum, and Swensen's spending rule. Don't attribute these to this course. If the Final Report
wants them, cite the original papers, checked first. The critique of Siegel is covered by Damodaran (D30).

---

## 3. Cross-source fusions (where two sources make one sharper point)

- **F1. Riskless is a date, and the coupon is the crack** (D1 + D2 + D3 + L4 + L8 + L18). Both professors define the
  riskless asset as one that pays when you need it. Damodaran adds that even a Treasury held to maturity isn't fully
  riskless, because its coupons must be reinvested. Shiller adds that a coupon bond is "an annuity and a discount bond
  together", and that cash rates once sat just above zero for seven years. Put together, the plan's only crack is the annuity
  half, and it is priced at the floor cash rates have actually touched.
- **F2. A named number is a quasi-bond, so make it a real one** (D20 + L9 + L11). Lintner's managers never cut. A firm
  that fixes its dividend has turned its equity into a quasi-bond. Prospect theory says the named number becomes the
  reference point, and falling short of it hurts more than beating it pleases. The 2031 lock follows: turn the
  quasi-bond into a Treasury before saying the number.
- **F3. A dated payment out of shares is a scheduled margin call** (8b + L14 + D36). In a crash, correlations rise,
  leveraged and forced sellers get crushed, and the price falls further than the news justifies. Paying a fixed
  January out of shares makes Laura a forced seller on a timetable. The ladder removes the forced sale.
- **F4. Operating budget, defined benefit; capital budget, defined contribution** (L22 + L20 + D16 + D19). Public
  finance and pensions draw the same line the case draws. Fixed operating claims are funded in advance and matched.
  Capital projects and gifts are sized from what's owned and kept flexible. The more uncertain the future need, the
  less is promised.
- **F5. Yale's opportunity cost is Laura's match** (L6 + D1). Swensen says Treasuries are the only diversification in
  a panic, but a costly one for a fund that lives forever. Laura's payment money doesn't live forever, so for it the
  Treasury isn't a hedge with a cost, it's the liability's twin. Her surplus follows Swensen's advice for individuals:
  one low-cost index fund.
- **F6. Protection is only as good as the protector** (L5 + L17 + L21 + the Lehman notes). Shiller: "look at the
  insurance company that you buy insurance from"; portfolio insurance "wasn't really insurance"; parity shows a floor
  can be built from owned pieces. FINRA fined UBS $2.5 million and ordered $8.25 million in restitution (11 Apr 2011)
  over sales of Lehman's "100% Principal-Protection Notes", saying UBS "failed to emphasize they were unsecured
  obligations of Lehman Brothers" (ThinkAdvisor, 11 Apr 2011). Laura's floor is a Treasury she owns, not a bank's
  promise. (How much Lehman note buyers lost isn't documented in the article: **UNVERIFIED**.)
- **F7. Even a century can't pin down the share premium** (D29 + L2 + D26). An 80-year sample leaves a 2.2-point
  standard error, normal curves say 1987 "couldn't happen", and valuing a promise with a forecast mismatches risk and
  rate. Certainty by ownership, not by probability.

---

## 4. The 12 best finds for the IPS

Ranked by how much each sharpens Caplet XR, given what the FINAL already says. Each is a plain idea with its so-what for
Laura, not a sentence to paste. Several only strengthen a line that's already there, which costs no words.

1. **The weak point, in finance's own definition** (F1).
   - Idea: a Treasury held to maturity pays its principal on the day, but its interest arrives early and has to wait.
     That waiting money is the only part that isn't certain.
   - So-what: the textbook cure (a zero-coupon Treasury) is banned, so the plan prices the waiting money at zero
     interest, about where US cash rates sat (a 0-0.25% target) from 2008 to 2015.
   - Source for the FR: Damodaran, "Into the Abyss" (2010), p. 5, and "What is the riskfree rate?" (2008), p. 6;
     Shiller, ECON 252, lectures 8 and 18.
2. **A named number is a quasi-bond** (F2).
   - Idea: a company that fixes its dividend has turned its shares into a bond-like promise. Once Laura names the top
     of her range, the shares behind it are already a promise, so she swaps them for Treasuries before she says it.
   - So-what: this is the mechanism under "a number said aloud can't quietly be halved".
   - Source for the FR: Damodaran, "Dividend Policy for the 21st century" (blog, 18 Feb 2011); Shiller, lecture 9
     (Lintner) and lecture 11 (prospect theory).
3. **Operating budget versus capital budget** (L22).
   - Idea: cities must balance their operating budget but may borrow for a new school. Laura's ten payments are her
     residency's operating budget, so they're funded in full before anything else. The building is a capital project,
     sized from what's left.
   - So-what: it explains the order of the whole plan with one public-finance rule, and it shows Client Knowledge
     (the residency is an institution with running costs and a building).
   - Source for the FR: Shiller, lecture 22, ch. 5.
4. **Defined benefit for the payments, defined contribution for the gift** (L20).
   - Idea: a pension that promises a fixed income has to hit a target, so it's matched. One that promises only
     contributions doesn't. Her payments are the first kind and her gift is the second, until 2031, when only money
     she owns becomes a promise.
   - So-what: it answers "how do favourable and unfavourable outcomes change the gift" in one stroke. Payments never
     move; the gift does.
   - Source for the FR: Shiller, lecture 20, ch. 7. Pick 3 or 4 for the IPS, not both, unless they fuse into one
     clause.
5. **No forced sale, ever** (F3).
   - Idea: in a crash, the people who get hurt most are those who must sell. A plan that pays each January out of
     shares must sell on a timetable, crash or not. Because of the ladder, Laura never sells a share to pay a January.
   - So-what: it says why "no payment depends on shares" matters beyond averages.
   - Source for the FR: Geanakoplos, Yale ECON 251, lecture 26 (2009); Greenberg in Shiller, ECON 252, lecture 14.
6. **Riskless means "pays on the day you need it"** (D1, D2, L4).
   - Idea: a bond is safe only for the date it matures on. Cash is risky for a 2038 bill because rates can fall, and a
     long bond is risky for a one-year need because its price moves. So each January gets the one holding that pays
     out before it.
   - So-what: high certainty gets a mechanism, not an adjective.
   - Source for the FR: Damodaran, hurdle-rate deck and riskfree paper; Shiller, lecture 4, ch. 7.
7. **Nominal promise, nominal match: the inflation assumption** (D5, D6).
   - Idea: inflation can't change a fixed $50,000, so ordinary Treasuries match it exactly, and inflation-linked bonds
     would add a mismatch. Inflation, and the Taiwan-dollar exchange rate, bite on what each payment buys and on the
     building, which is why the half she keeps stays in shares.
   - So-what: fills the case's stated requirement that no draft yet meets ("the effect of inflation").
   - Source for the FR: Damodaran, riskfree paper and invretA (the Rio Disney example: a Brazil project analysed in
     dollars).
8. **The more uncertain the building, the less she promises** (D16, D33).
   - Idea: firms facing uncertain future needs borrow less, to keep room to act. Laura's unpromised half is that room.
     It's worth most because no one else can count on it, so promising it would destroy it.
   - So-what: "preserving flexibility" (the case's words) becomes an argued choice.
   - Source for the FR: Damodaran, capstr (Proposition 5; CFO survey ranking flexibility first) and invretB (real
     options).
9. **No promise rests on a forecast** (F7).
   - Idea: even 80 years of data leaves the share premium uncertain by about two points either way, and normal-curve
     models said 1987 couldn't happen. So both ends of the range are money she owns, not a forecast.
   - So-what: it defends defining certainty by ownership, not by a model probability (the verdict file's hurt-list #3).
   - Source for the FR: Damodaran, ERP paper (2008 edition), Table 2; Shiller, lecture 2, ch. 6.
10. **Why we don't copy Yale** (F5).
    - Idea: Yale holds few Treasuries because its money must last forever, and Treasuries cost it growth. Laura's
      payment money has ten dates, so for it a Treasury is the match, not a cost. Her spare money does what Yale's own
      investor tells individuals to do: a cheap index fund, no timing.
    - So-what: it shows the judges the team knows the famous model and why it doesn't fit.
    - Source for the FR: Swensen in Shiller, lecture 6, ch. 5 and Q&A.
11. **The opposite of a bank** (L13).
    - Idea: banks borrow short and lend long, so they're sound only while people believe they are. Laura's ladder
      never has money due before it has money arriving, so it stays sound whatever anyone believes.
    - So-what: co-sponsors' confidence rests on ownership, not on hope.
    - Source for the FR: Shiller, lecture 13, chs. 2, 4, 5 (Diamond-Dybvig).
12. **Protection is only as good as the protector** (F6).
    - Idea: a bank's capital-protected note is a promise from the bank, and Lehman's "100% principal-protected" notes
      were unsecured Lehman debt when it failed in 2008. Laura's floor is a Treasury she holds herself.
    - So-what: adds a second, sharper reason to the protected-note line already in the FINAL (it's not only the
      option that can expire worthless).
    - Source for the FR: Shiller, lecture 5, ch. 6 ("look at the insurance company") and lecture 21, ch. 6 (portfolio
      insurance); FINRA's 2011 UBS settlement, as reported by ThinkAdvisor, 11 Apr 2011.

**Near-misses** (true, but each repeats a better find or costs words the IPS lacks):
- Balloon mortgages and rollover (L10): the history behind find 6.
- Debt design mirrored (D9): the frame behind find 6.
- A bond held to maturity as a forward you own (L15): supports "buy the reserve in 2027".
- Regret and the dated 2031 rule (L11).
- Disclosure rather than signalling (D23, L12).
- The Treasury hurdle (D12): already the verdict file's #3.

---

## 5. Final Report only

- Damodaran's implied ERP, 4.41% on 1 Nov 2026 (home page), and the 0.22% US default spread (adjusted dollar riskfree
  rate 5.07%). Resolve the 5.29% (home page) vs 4.9% (blog, 26 Oct 2026) Treasury-rate conflict first.
- Damodaran on duration matching vs one riskfree rate per cash flow (riskfree paper, p. 9; "Into the Abyss", p. 5),
  as the source for the pension-fund sentence.
- Damodaran's debt-design tree (maturity, currency, fixed or floating, straight or convertible) applied in reverse to
  the ladder; the "perfect financing instrument" as the frame for the capital-protected note.
- The CFO survey ranking "Maintain financial flexibility" first (packet 2, slide 24).
- Damodaran's bird-in-hand slide, as a devil's-advocate question and the team's answer (D24).
- The cash/trust nexus (divassessment) for the co-sponsor communication.
- "The story and the numbers" (valuation, slide 232) as a note on the team's method.
- Dimson-Marsh-Staunton survivorship (use the current yearbook, not the 2008 numbers) and "Stocks always win in the
  long term" (Damodaran's fables page) for the history section.
- Shiller 1: finance as "allocating resources through space and time"; Carnegie and the Giving Pledge for the client
  story.
- Shiller 2: Apple's ride and the Yale class of 1954's $90 million gift, a survivorship story about why the gift isn't
  staked on stock picks.
- Shiller 3: the 1780 Massachusetts indexed bond and Chile's UF, in a short note on why TIPS weren't needed even before
  the ban.
- Shiller 4: Norway's oil fund (human capital on a national scale).
- Shiller 5: AIG and the failure of independence; life insurance as insurance against "the loss of a bread winner".
- Shiller 6: Swensen's full passage on Treasuries in a panic and their opportunity cost; index funds for individuals.
- Shiller 8: forward rates and Hicks's term premium, to explain why pricing the coupon gap at zero is more cautious
  than the market's own forecast.
- Geanakoplos (ECON 251, 26) and Greenberg (ECON 252, 14): the forced-seller story in full.
- Shiller 10: balloon mortgages and the 1934 FHA fix (rollover risk).
- Shiller 12: disclosure, Brandeis, plain English (for the co-sponsor text).
- Shiller 13: Diamond-Dybvig.
- Shiller 15: the forward lock.
- Shiller 17: put-call parity, for the capital-protected note.
- Shiller 18: the zero lower bound in 2011 and its later breach abroad.
- Shiller 20: Yale's 1825 Eagle Bank loss; the spendthrift trust; the prudent man rule ("live in fear of laws") as
  the reason teams copy a 60/40 template.
- Shiller 21: portfolio insurance and the Brady Commission.
- Shiller 22: rainy-day funds "exhausted".
- Shiller 23: building an institution rather than only giving.
- Lehman principal-protected notes: FINRA's 2011 UBS settlement (find 12).

## 6. Refused (looks relevant, isn't)

- **"Risk = danger + opportunity" (the Chinese characters slide).** A cliché, and the etymology is disputed.
- **Swensen's spending rule.** Not in his lecture, and Laura's surplus funds no recurring spend (agrees with the
  verdict file).
- **The equity premium puzzle, Siegel, Samuelson, and excess volatility as Shiller-course material.** Not found in the
  2011 transcripts read.
- **Laura Cha (16) and the investment-bank Q&A (19).** Nothing on Taiwan, Treasuries or the case.
- **Inflation-indexed bonds as a tool.** Banned, and wrong for a nominal liability (D5).
- **Shiller's Norway remedy (shorting oil futures).** Derivatives are banned. Keep the principle, drop the remedy.
- **Free cash flow to equity or a yearly payout ratio.** There is one gift, once (agrees with the verdict file, B3).
- **Damodaran's 2020 S&P dividend counts.** His own slide gives two figures for increases (287 and 298).
- **An expected share return built from the implied ERP (about 9.7%).** It isn't comparable with Keel's 7.5% compound
  basis, and it would argue for more shares.
- **Debt as discipline.** True for firms; for Laura the motif already does the work.

## 7. Verification notes

- **Checked tonight (5 Nov 2026):**
  - every quote above, read from the source page through WebFetch;
  - the fed funds target range: 0-0.25% from 16 Dec 2008 (FRED DFEDTARU), "until December 2015" and again from
    15 Mar 2020 (Chicago Fed);
  - the FINRA/UBS Lehman settlement (ThinkAdvisor, 11 Apr 2011).
- **UNVERIFIED or open:**
  - the end date of the 2020-22 zero range (16 Mar 2022, from memory);
  - which Treasury rate Damodaran uses for 1 Nov 2026 (5.29% on his home page vs 4.9% in his 3 Nov post);
  - the size of losses on Lehman principal-protected notes;
  - who "He wanted plain English" refers to in lecture 12;
  - the year of Lintner's article (the standard citation is the *American Economic Review*, May 1956; Shiller says
    only "a long time ago");
  - the year of Geanakoplos's ECON 251 lecture (2009, inferred from the archive path);
  - the full wording of every "[fragment]" quote.
- **Read in part only:** lecture 19 (the Q&A part only). Lecture 2's first section was unreadable, but the transcript
  read from offset 100,000 covers its chapters 1-6.
- **Nothing here was committed or pushed.** This file is the only output, as asked.

## 8. Sources (all read 5 Nov 2026)

- Damodaran, lecture notes page: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/cflect.htm
- Damodaran, packets: https://pages.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket1spr26.pdf and
  https://pages.stern.nyu.edu/~adamodar/pdfiles/cfovhds/cfpacket2spr26.pdf
- Damodaran, topic decks (all at https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/): risk&ret.pdf,
  hurdlerate.pdf, invretA.pdf, invretB.pdf, capstruchoices.pdf, capstr.pdf, debtdesign.pdf, divintro.pdf,
  divassessment.pdf, valuation.pdf
- Damodaran, "What is the riskfree rate? A Search for the Basic Building Block" (Dec 2008):
  https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/riskfreerate.pdf
- Damodaran, "Into the Abyss: What if nothing is risk free?" (Jul 2010):
  https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/nothingisriskfree.pdf
- Damodaran, "Equity Risk Premiums (ERP): Determinants, Estimation and Implications" (2008 edition):
  https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/ERPfull.pdf
- Damodaran, home page (implied ERP, 1 Nov 2026): https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm
- Damodaran, "Stocks always win in the long term":
  https://pages.stern.nyu.edu/~adamodar/New_Home_Page/invfables/stockswinstory.htm
- Damodaran, blog: https://aswathdamodaran.blogspot.com/2008/10/diversification-why-is-it-not-working.html ;
  https://aswathdamodaran.blogspot.com/2010/02/thoughts-on-riskfree-rate.html ;
  https://aswathdamodaran.blogspot.com/2011/02/dividend-policy-for-21st-century.html ;
  https://aswathdamodaran.blogspot.com/2026 (Data Update 3 for 2026, 28 Jan 2026) ;
  https://aswathdamodaran.blogspot.com/2026/11/the-anthropic-feedback-loop-cost-of.html
- Shiller, ECON 252 (2011): https://oyc.yale.edu/economics/econ-252 ; lectures at
  https://oyc.yale.edu/economics/econ-252-11/lecture-N (N = 1-23)
- Geanakoplos, ECON 251 lecture 26: https://oyc.yale.edu/economics/econ-251/lecture-26
- FRED, federal funds target range upper limit: https://fred.stlouisfed.org/data/DFEDTARU
- Chicago Fed, the federal funds rate: https://www.chicagofed.org/research/dual-mandate/the-federal-funds-rate
- ThinkAdvisor, "UBS to Pay FINRA Fine, Restitution to Investors in Lehman PPNs" (11 Apr 2011):
  https://thinkadvisor.com/2011/04/11/ubs-to-pay-finra-fine-restitution-to-investors-in-lehman-ppns
