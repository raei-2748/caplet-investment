# R20 review (b): Wharton read (Thu 5 Nov 2026, Sydney)

Strict counts: pitch 49/50, IPS 496/500. No TIPS, STRIPS, derivatives or cash as a holding.

## 1. Three judges

**Fixed-income PM. Top 50: yes.** A real dedication with a dated glide path, and it names its own weak point.
- Strategy 8: the 2027, 2028, 2031 and 2033 steps chain together, and the single borrower is a defended choice.
- Client 7: "co-sponsors may help pay for the facility, never for those" reads the case exactly.
- Analysis 6: the levered-surplus point is right. But each bond's interest waits for "the January it was meant for", which builds the gap the plan then patches with shares.
- Articulation 5: no team process visible.
- Presentation 7: plain and in order.
- Remembers: "a second borrower would only add a second way to miss a January."
- Doubts: "From the other half she sets aside enough Treasuries to cover that interest shortfall..." What if that half is too small?

**Growth investor. Top 50: no.** Tidy but timid.
- Strategy 5: shares are about a fifteenth of $450,000. "Thoughtful risks" goes unanswered.
- Client 5: Laura reads as a payment schedule, not an entrepreneur.
- Analysis 5: no share-return assumption, and no price put on the safety.
- Articulation 4: no decision shows the team arguing.
- Presentation 6: the "X for ten, R for redemption" line reads as a label, and the pitch lists mechanics, not an idea.
- Remembers: "just as a company's shares grow riskier as it borrows" (grudgingly).
- Doubts: "The slice left over, about that fund's interest, buys a world index fund." That clause is the whole growth engine.

**Finance professor. Top 50: yes, upper half.** The thesis is in sentence one, and the draft argues from a principle.
- Strategy 7: one thesis, consistently applied, with diversification reasoned about.
- Client 6: certainty is tied to co-sponsor credibility, but several assumption asks get a clause or nothing.
- Analysis 6: certainty is defined, but its evaluation is only implied. The IBTM sizing ("most of the rest") is vague.
- Articulation 5: two roads not taken are named (a balanced mix; buying the bottom in 2031).
- Presentation 7: it makes an argument, not a list.
- Remembers: "no payment depends on a share price, a forecast or a sale before maturity."
- Doubts: "Barring a US default, her contribution will land in the range, and where it lands is her choice." That is true by construction, so it says nothing about how the team judged confidence.

## 2. Wharton's questions and the case's asks

| Item | Mark | Sentence |
|---|---|---|
| Central idea | answered | "buys every amount Laura commits to with Treasuries before she commits to it" |
| Principles | answered, scattered | "no payment depends on..."; "Market moves change nothing in the plan" |
| Balance (growth, risk, liquidity, reliability, flexibility) | thin | liquidity is only "sellable on any trading day", and growth is never weighed against the cost of safety |
| Allocation as needs approach | answered | the 2027, 2028, 2031 ("moves half of her shares into Treasuries") and 2033 steps |
| Protect commitment + flexibility | answered for the commitment, thin on flexibility | "stays out of the range as her financial flexibility" (may be nothing: flag 1) |
| Reserve size | thin (fine: final sizing belongs to the Final Report) | "the ten holdings and the money set aside are her operating reserve" |
| Composition | answered | ten Treasury holdings, the set-aside, the short-term Treasury fund |
| How it changes | thin | "each January's $50,000 comes from the holding redeemed before it" implies run-off but never says so |
| Certainty defined | answered | "near-ironclad" |
| Certainty evaluated | thin | only "assuming the waiting money earns nothing"; no test or result |
| Performance | thin | no share-return assumption |
| Timing | answered | "each maturing in the year before the January it pays for" |
| Outside funding | answered | "never for those" |
| Inflation (projections) | thin | "Fixed payments" is never tied to why nominal Treasuries match them |
| Inflation (facility) | thin | "can grow with building costs in Taiwan" |
| Flexibility | answered, unsized | as above |
| 2031 range | answered | "the top is the bottom plus that half" |
| Confidence | answered (by construction) | "Barring a US default..." |
| Good and bad markets | answered | "A good market before 2031 raises the top and a bad one lowers it" |

## 3. Flags

1. **Internal contradiction (hard).** Paragraph 2 says "no payment depends on a share price", yet paragraph 5 funds the payments' interest gap from her kept shares. Keel's model kept payments whole only "whenever the money to do it existed", and it used up her kept shares in about a quarter of futures (MODEL, `keel/ips_rewrite/final_night/harvest/02c_library_models_record.md` T11). The text never says what gives when the half falls short. Kind of fix: state the order in which a shortfall is absorbed, or narrow paragraph 2's absolute.
2. **Factual (minor).** "whose Treasuries all mature in late 2032": iShares, 25 Sep 2026 (`keel/library/insight_v1/phase_E/E6_final_spec.md:316`), lists 15 Treasuries maturing **Apr-Sep 2032**, and the fund ends about 15 Dec. Kind of fix: date the holdings loosely or drop the clause.
3. **Tension with locked Note 3** ("stocks only set how far her gift rises above her promised minimum"). R20 gives the kept shares a second job, insuring the payments. Kind of fix: frame the cover as a set-aside made from free shares, not a role the shares play.
4. Consistent with the notes: the IBTR conditional, IBTM's two jobs, the short-term Treasury fund (Note 1), the top moving with stocks, and "near-ironclad". The "first $300,000 buys ten" line is properly hedged by paragraph 3 (8bp headroom, 23 Oct close).

## 4. One idea out, one in

- **PM:** cut the naming clause. Add the shortfall waterfall (who absorbs a gap the kept shares can't cover, ending with never a payment), so that flag 1 becomes true rather than hoped for.
- **Growth investor:** cut the one-borrower sentence. Add the cost of safety: the gift a bolder share weight would buy (a sourced MODEL figure), and why her stock-like career income argues against it.
- **Professor:** cut the closing sentence on the November 2041 bond. It describes an individual investment, which Wharton asks teams not to do. Add how certainty was evaluated: the test the team ran (shares at zero, waiting money at zero) and its result.
