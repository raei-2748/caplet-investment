(Keel is a simulated team, AI-written.)

# Felix, R1 research: two P5 sentences of V57 at their sources (read Wed 4 Nov 2026, Sydney)

All pages were read through the WebFetch tool, which summarises a page with a small model. So every quote below is
**near-verbatim, via fetch tool**; none was read in a browser. Quote marks mark the fetch tool's quoted strings.

## URLs tried
Fetched OK:
- https://www.finra.org/investors/insights/structured-notes-principal-protection
- https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/structured-notes-principal-protection-note-terms
- https://static.moneysmart.gov.au/files/publications/get-the-facts-capital-guaranteed-or-protected-investments.pdf
- https://www.moneysmart.gov.au/investing/complex-investments/capital-guaranteed-and-capital-protected
- https://www.sechistorical.org/collection/papers/1980/1988_0101_BradyReport.pdf (Brady report, excerpt only: Executive Summary; Chapter Four estimate came through the summary; later chapters did not)
- https://www.federalreservehistory.org/essays/stock-market-crash-of-1987
- https://www.nber.org/chapters/c10958.pdf (Shiller, NBER Macroeconomics Annual 1988)
Failed or empty:
- https://www.investor.gov/introduction-investing/investing-basics/glossary/market-linked-certificates-deposit (page body empty; UNVERIFIED, unused)
- https://moneysmart.gov.au/investment-warnings/capital-protected-products (site error; guessed URL; unused)
Not opened: Leland and Rubinstein's own papers; the SEC's 1988 staff report; Brady chapters beyond the excerpt.

## Find 1: regulators on capital-protected notes (tests P5 sentence (a))
V57: "Banks sell this as a capital-protected note, but they spend the interest on an option that can expire worthless."

Sources, all read 4 Nov 2026:
1. SEC Office of Investor Education, "Structured Notes with Principal Protection: Note the Terms of Your Investment", investor.gov, 2 Jun 2011.
   - "Structured notes with principal protection typically reflect the combination of a zero-coupon bond" and a derivative.
   - "At issuance, any given note will have an estimated fair value based on its structure." / "The issuer generally raises this value by a spread to arrive at the offering price of the product".
   - "Some structured notes with principal protection may have limits or caps on the gains you can earn".
   - "Any promise to repay some or all of the money you invest will depend on the creditworthiness of the issuer of the note"; on bankruptcy holders "are considered unsecured creditors".
   - "Products offering principal protection can be expensive."
2. FINRA, "Understanding Structured Notes With Principal Protection", 12 Apr 2023.
   - "They do so by combining a traditional security, like a bond, with a derivative component."
   - "you might potentially forgo significant gains as a tradeoff for principal protection"; "The initial estimated value is generally less than the price of the note".
   - "You could lose all of your investment if the issuer of your note is unable to pay its obligations or goes bankrupt."
3. ASIC Moneysmart, "Get the facts: Capital guaranteed or protected investments" (PDF, undated).
   - Some products "use a portion of the money you invest to buy a bond to provide capital protection" and "invest the remainder of the money in options and other derivatives."
   - "The guarantee or protection generally only applies if you hold your investment for the full term."
   - "these products are more expensive than simpler investment products"; "Some capital guaranteed or protected investments also limit the capital growth you are entitled to."
4. ASIC Moneysmart web page "capital guaranteed and capital protected": "if the company providing the guarantee goes belly-up, you can still lose money"; "exit fees and a cancellation of the capital protection feature also often apply."

Mechanism, two plain sentences. The bank buys a zero-coupon bond at a discount that grows to the money you put in, and spends what is left on an option on a market. If the option ends out of the money it pays nothing, and you get back only your principal, at the end, if the bank is still standing.

Where the sentence breaks, and where it holds:
- "Interest" is the right economic name. A zero-coupon bond has no coupons; the discount to face IS the interest it earns, and the money not needed to buy the bond is that discount. But no regulator uses the word "interest" for what buys the option. They say "the remainder of the money". So "the interest" is our word, true in effect.
- Not every bank note works this way. Regulators list notes with barriers, buffers, caps; Moneysmart also lists life-insurer and bank-guarantee versions. "Banks sell this" is true of the zero-coupon-plus-option type only.
- "Can expire worthless" holds (derivative component pays nothing if it ends out of the money). Neither regulator page I read says it in those words; Amara's 3 Nov post found the flat-market case on the SEC page; I did not re-find it today. The claim is mechanical, not quoted.
- The sentence skips what every regulator flags: issuer credit risk (unsecured creditor), a spread/fees between fair value and price, upside caps, protection only if held to the end. The comparison "we would rather she owned the shares" is made without these, but the sentence does not claim our version is free of risk, so the omission is a gap, not an error. Our own fund version carries no issuer risk, which is a point in our favour that the sentence does not use.

Verdict: **TRUE IF** the note is the zero-coupon-bond-plus-option kind the SEC describes, and "the interest" is read as the bond's discount (what the money not needed for the bond would earn). Smallest word fix, if the room wants one: "Banks sell this" to "Banks sell a version of this", or "the interest" to "that interest". Nothing is FALSE. Leaving it as is is defensible: a judge who knows the product would nod at "interest" and could only quibble at "Banks sell this".

## Find 2: the Brady report and portfolio insurance (tests P5 sentence (b))
V57: "Nor do we copy portfolio insurance, which sells shares as they fall and helped deepen the 1987 crash."

Sources, read 4 Nov 2026:
1. Report of the Presidential Task Force on Market Mechanisms (the Brady report), Jan 1988, hosted at sechistorical.org (URL above). Excerpt only.
   - Executive Summary: "This initial decline ignited mechanical, price-insensitive selling by a number of institutions employing portfolio insurance strategies" (fetch tool cut the rest of the sentence).
   - Reactive selling by portfolio-insurance followers "played a prominent role in the market break" (this phrase came through the fetch summary as a quote; I did not see its surrounding page).
   - On 19 October: "Sell programs by three portfolio insurers accounted for just under $2 billion in the stock market"; in futures, "$2.8 billion of stock".
   - Chapter Four (via fetch summary): the formulas "dictated the sale of $20 to $30 billion of equities over this short time span."
   - Also names mutual funds reacting to redemptions and "aggressive" trading-oriented institutions; says insurers adopted strategies needing "liquidity far in excess of what the market could supply".
2. Federal Reserve History, "Stock Market Crash of 1987": portfolio insurance "included extensive use of options and derivatives and accelerated the crash's pace as initial losses led to further rounds of selling." It lists other likely causes (foreign investment, settlement mismatches, exchanges powerless).
3. Robert J. Shiller, "Portfolio Insurance and Other Investor Fashions as Factors in the 1987 Stock Market Crash", NBER Macroeconomics Annual 1988 (vol. 3), pp. 287-297.
   - "Cascade effects of portfolio insurance might be one important factor, but the simple story does not settle the issue."
   - "Portfolio insurance appears even in 1987 still to have been a small part of stop-loss behavior among investors" (survey: 5.5% of institutions used it, 10.2% had some stop-loss policy).
   - Quotes Leland calling it "nothing more than a rationalization of policies already in existence". Kenneth French (discussant): little portfolio insurance was actually executed.

Mechanism, two plain sentences. Portfolio insurance sells shares (or index futures) when prices fall, to copy a put option on the portfolio. In a sharp drop, those sales add to the pressure, which prompts more sales.

Where it breaks: "sells shares as they fall" is right, though much of it was done in futures, not shares (Brady: $2.0bn in stocks, $2.8bn in futures by three insurers on 19 Oct). "Helped deepen" is the softest honest claim: Brady's own wording is stronger ("played a prominent role"; it blamed the trigger on news events and insurers' selling) and it is not the sole cause. It is disputed in degree: Shiller says it was a small share of stop-loss behaviour and that "the simple story does not settle the issue". I did not open Leland or Rubinstein themselves or the SEC's 1988 staff study, so how they would say it is UNVERIFIED.

Verdict: **TRUE**. "Helped" already carries the condition (one cause among several, with the size debated). Optional safer wording, only if the room wants the dispute marked: "helped deepen" to "is blamed for deepening". Not needed.

## For the Final Report
Cite SEC investor.gov 2011 (zero-coupon bond plus derivative; spread; caps; issuer credit), FINRA 2023, Moneysmart "Get the facts"; the Brady report with Shiller 1988 as the dissent.
