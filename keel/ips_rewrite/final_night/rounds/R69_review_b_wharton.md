# R69 review (b): Wharton read
AI-generated review (Claude, 6 Nov 2026). Not submission text.

Strict counts: IPS 497/500; pitch 50/50 (margin 0; 49 if SMApply counts by spaces).

## Three judges

| | Fixed-income PM | Growth investor | Finance professor |
|---|---|---|---|
| Investment Strategy | 8 | 6 | 8 |
| Client Knowledge | 7 | 5 | 7 |
| Portfolio Analysis | 8 | 6 | 7 |
| Articulation of Experience | 4 | 4 | 4 |
| Creativity & Presentation | 7 | 7 | 8 |
| Top 50 | Yes | No (borderline) | Yes |

**PM.** Remembers: "So the plan assumes it earns nothing." Doubts: "since no Treasury she may buy matures in those years." Treasury notes mature in all of those years, and WInS listed a Feb-2036 bond (rejected for a stale price, `archive/rab/trades/`). "Those years" are never named.

**Growth investor.** Remembers: "A balanced mix of shares and bonds would probably leave her richer by 2042." Doubts: "everything beyond her contribution stays out of every promise and can be sold any day." Every share is sold in 2031 and she contributes "the top". What is left, how big, held in what? For a client "willing to take thoughtful risks", the stocks are a small sleeve that ends two years before the residency opens.

**Professor.** Remembers: "Like the shares of a heavily borrowed company, that leftover would swing far harder than the share market". Doubts: "If that half falls short, the stake behind the bottom pays the rest." Why half? The lab's cash bound (`keel/ips_rewrite/lab/R08_4_coupons_results.json`) puts the zero-earnings gap near $43k over the plan's life, more than half a sleeve worth roughly the deposit minus the stake's cost (my estimate, unchecked). Falling short may be normal, not rare. Check before submitting.

## Wharton's questions and the case's asks

| Ask | Status | Quote |
|---|---|---|
| Central idea | Answered | "keeps every sum Laura commits to in Treasuries before anyone counts on it" |
| Principles | Answered (implicit) | "we treat them as a debt"; "assumes it earns nothing" |
| Balance of growth, risk, liquidity, reliability, flexibility | Thin | Growth vs reliability shown; liquidity only "can be sold any day" |
| Change as needs approach and payments are made | Answered to 2033, thin after | After 2033, only "the final redemption meets the final payment" |
| Protect payments, keep room for the facility | Answered | "falling markets and rates land on the range, not the payments" |
| Risk and return | Thin | No return assumption, not even in words |
| Diversification | Thin | "thousands of companies"; one issuer otherwise |
| Reserve composition and change | Answered / thin | "only on paper, since the Treasuries held for the payments already make it up" |
| Define high certainty | Answered | "Barring a US default and with both deposits made ..." |
| How certainty was evaluated | Thin | Only the zero-earnings assumption; no test is described |
| Responsible contribution | Answered, reasoning thin | "She contributes the top, or less if the building in Taiwan needs less" |
| Flexibility as the project develops | Thin | "stays out of every promise"; size and holding unstated |
| 2031 range method; confidence | Method answered; confidence missing (allowed) | "both ends are owned before she says a word" |
| Good and bad outcomes; range protects payments | Answered | "A rise before then lifts the top"; "the stake behind the bottom pays the rest" |
| Outside funding; timing | Answered | "can come only from her portfolio" |
| Inflation (projections, facility cost) | Missing | none |
| Investment-performance assumption | Missing | none |
| Taiwan residency goals | Thin | "the building in Taiwan" only; nothing on a US-dollar gift paying Taiwan-dollar costs |

## Flags

**Contradictions**
- TNA Note 3: stocks "only set how far her gift rises above her promised minimum". The IPS sends up to half the shares to the payments' gap. The fix must show shares only top up a floor already in Treasuries, or admit the change.
- The opening ("every sum ... in Treasuries before anyone counts on it") clashes with the zero-earnings assumption, under which the payments are short until 2031. The floor stake covers that gap meanwhile; the fix must say so where the claim is made.
- With every share sold in 2031, "She contributes the top" reads like committing everything, which the case warns against ("committing all remaining assets could limit her financial flexibility"). The real slack, the zero-earnings cushion plus any unused shares, is never named.
- Pitch, "half its shares": "its" could mean the range or the deposit.

**Facts that look wrong**
- "no Treasury she may buy matures in those years" (see the PM above).
- "early repayment": Treasuries are not repaid early; the meaning is principal arriving before its payment date.
- Only the stake's payout "isn't fixed"; all five funds' payouts float a little, yet the certainty definition names only a US default.

**Wharton's don'ts**
- No tickers, citations, charts or calculations. There is one figure, sourced to "current Treasury prices".
- "Five are funds..." and "its December 2032 payout" lean toward "describing individual investments".

## One cut, one add per judge

| Judge | Cut | Add (what it must convey) |
|---|---|---|
| PM | The gloss "the X in the name ... the R" (~10 words) | The five funds' payouts are not fixed either, and the zero-earnings cushion absorbs that |
| Growth | "which buildings seldom do" and "Bought in 2028," (~7 words) | What the money beyond her contribution holds after 2031, and the rule for how much is held back |
| Professor | The "Five are funds..." sentence (~16 words) | Payments fixed in dollars are matched by Treasuries fixed in dollars, so inflation falls on the building's cost, not the payments; and how certainty was tested, in words |
