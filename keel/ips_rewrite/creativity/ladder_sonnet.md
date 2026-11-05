> AI-generated research (Claude Code, ideation ladder, Thu 5 Nov 2026), not for submission. Keel is a simulated team, AI-written. Read the shortlist beside this file first.

# Ladder rung 2 (Sonnet): a sceptical PM reads the FINAL IPS (V57)

Inputs read: Laura Gao case (full), WHARTON_WORD.md, FINAL ips.txt (493 words) and pitch.txt (49 words), ERUDITION_PLAN s3 and s5, and targeted greps of IDEA_BANK.md (385 lines). Arithmetic is mine, rough, and labelled MODEL. Scripts: `ladder_sonnet_calc.py` in this folder.

Honest headline first: the team's mechanism space is close to saturated. The bank has about 140 ideas and I could not find a big, untouched mechanism. What I can add is (a) one benchmark the team never ran, which changes how the plan looks, (b) a few moves that live in the client and co-sponsor story, not the portfolio, and (c) a warning that the plan may be over-built for the dollars it actually moves.

---

## 1. What is non-standard, and what a top-50 team also has

**What a typical strong (top-50) team will have** (my guess, from the case and the rules):
- A Treasury ladder or a duration-matched IEF/TLT-style bond sleeve for the ten $50k payments, 70-90% of money, bought in January 2027.
- A growth sleeve of 10-25% in one world or US equity fund, funded by the 2028 deposit.
- "High certainty" defined as a probability from a Monte Carlo (95% or 99% of paths pay every cheque).
- A glide path: shares cut toward 2033, bonds lengthened or shortened as payments approach, annual rebalancing, a T-bill liquidity slice.
- A 2031 range read straight off the simulation: 10th-90th (or 5th-95th) percentile of the 2033 surplus, "we are 80-90% confident it falls between $X and $Y". Usually the bottom is below $150k, because 20-30% equities have a fat left tail.
- Sector or Taiwan/AI tilts in the WInS book that do not match the IPS.

**What is genuinely non-standard in XR** (and real, not packaging):
1. Certainty defined by structure ("no payment depends on shares"), not by a simulated probability. That is a better answer to the case's "define what you consider a high degree of certainty" than a 99% claim, and it is cheap to defend.
2. The note-minus-option reading: the floor is the deposit's principal, only the floor's forgone interest buys shares. Textbook parts, unusual use.
3. The range method: bottom = money already bought; top = half the shares, moved into Treasuries before she names it. This turns the case's "confidence the contribution falls in the range" from a forecast into a held position. Nobody else will do this.
4. Pricing the ladder's reinvestment gap as if waiting cash earned nothing, and paying it from Laura's own spare money before the gift, before a cheque. The senior/junior order is sharp.
5. Tested refusals (CPPI, glide path, buckets, 60/40, immunising with funds). Few teams show why they said no.
6. The "Treasury ladder with coupons" is honestly disclosed as relying on reinvestment. Most teams will not notice.

What is standard underneath: Treasury ladder plus one world fund. The framing, the range method and the gap rule are what is distinctive.

---

## 2. Weaknesses a sharp judge can spot

Each is tied to a case line or an IPS sentence. Severity: H, M, L.

**W1 (H). The share sleeve moves almost no dollars, yet the plan is built around it.** IPS paras 9-13 (floor, shares, halving, lock, gap order, naming rule). MODEL, Laura's $150k deposit, 4.9 years, 5-year Treasury 4.98% (growth 1.269), world shares 7.5% and 16.5% volatility (growth 1.426, sd of 4.9-year log return about 36%):
- All Treasuries: $190k, certain.
- XR (shares about $32k, 21% of the deposit): bottom $150k, p5 about $174k, median $192-195k, mean $195-198k.
- So the whole sleeve adds about $3-8k of expected 2033 money (1-2% of Laura's $450k), with about a 38-45% chance the shares end below what Treasuries would have given. Shares are only about 7% of her money.
- The team's own 2025-26 lesson (CLAUDE.md) was "strategy packaging was over-complex for the insight". XR has about nine moving parts (ladder, floor, shares, lock, halving, gap pricing, kept-shares order, re-match, naming rule) steering about $25k of discretionary money.
- The bank prices the floor only against growth-heavy rivals (#99-#103, A09 at 80% stocks). I found no comparison against the Treasuries-only twin (grep: "only Treasur / all Treasur / frontier / marginal": nothing relevant).

**W2 (H). The announced bottom is below what Treasuries alone certainly give.** IPS para 11 "The bottom is that fund's payout, rounded down: money she already owns". The deposit in a 5-year Treasury is about $190k at the Sep-2026 curve and above $165k even at a 2% yield (150 x 1.02^4.9). The XR bottom is about $145-150k. A judge doing this sum asks why she voluntarily owns $40k less than she could, to chase a few thousand of equity premium. The IPS's answer is implicit ("we would rather she owned the shares"). It never says what the shares buy.

**W3 (M-H). "Her first $300,000 buys ..." is stated as fact (pitch, IPS para 5), but the ladder fits in $300k only about half the time.** The team's own headroom is about $2k (about 7 basis points; DV01 about $290 per basis point). With a three-month yield change standard deviation of 20-50bp and zero drift, P(cost over $300k) is 37-45% and the average overspend, given it happens, is $1.5-5k (my calc). The fallback is the 2028 deposit, which para 7 says "can dry up". So in roughly two worlds in five the plan leans on the money it just called unreliable. The size is small, but the words conflict.

**W4 (M). Certainty's definition has a hole.** Para 5: "high certainty means no payment depends on shares." Para 13: the gap is paid by moving her kept shares into Treasuries, and if that fails "she names a lower range". So in the tail a cheque does depend on shares (the bank records about 0.03% of paths). Also para 5 says "buying one bond per payment ... pays exactly what it promised", but a $300k ladder cannot cover $500k of cheques one bond each: each cheque is covered by its own bond plus other bonds' coupons. In my dedication model at a 5.2% coupon, about 23% of the ladder's cost (PV of coupons that arrive before 2033 and wait) is money that must be reinvested. Para 13 admits this, but para 5's sentence over-claims.

**W5 (M). Flexibility is the weakest of the five case bullets.** Case: "committing all remaining assets could limit her financial flexibility". XR commits about 88% of expected free money (top $170k of about $195k). What is kept is half the shares: about $22k median, and only about $10-13k in a bad tape (the bank's own wrong-way point, #13, left to "FR; IPS one clause"). So flexibility vanishes in exactly the states where she needs it. Case also says "Teams are not expected to determine the size ... of a separate contingency fund", so this will not be marked down hard, but a Statistics-trained client may notice.

**W6 (M). Five of the ten "bonds" are funds.** Para 5: "A Treasury bond held to maturity pays exactly what it promised." The first five rungs (IBTM-IBTR in the book) are iBond ETFs: they pay NAV at termination, charge about 0.07-0.10% a year, and reinvest inside the fund. The bank knows (#168 on waiting cash). The sentence still reads as if all ten are bonds.

**W7 (L-M). Book versus IPS stage 1.** Para 5: first $300k buys a ladder, para 7: no shares from that money. The frozen book holds 8.6% VT and uses IBTM as both a rung and the floor (bank #142: "the book is the finished plan at two-thirds size"; decision N1 upheld 3-0 that the IPS needs no bridge). A judge told to read the deliverables "together" may still see shares on day one. One clause ("the portfolio we traded is the plan as it will stand in January 2028, scaled to $300,000") would pre-empt it. The team has ruled against; I flag it as the one place their ruling could cost a point.

**W8 (L). Inflation is absent from the IPS.** The case lists "the effect of inflation on portfolio projections and facility costs" among the assumptions to identify. The IPS has a Taiwan-dollar line only. Taiwan construction costs are running about 6.5% year on year (about 3.5% since 2021, per CLAUDE.md), against a 5% nominal floor. The bank has it (#19, FRB-41) but the IPS does not say it.

**W9 (L). The Taiwan-dollar cushion is not a hedge.** Para 11: the other half "stays hers and liquid, as a cushion if the building costs more in Taiwan dollars". A world fund gives only a faint USD/TWD offset (foreign holdings gain in dollars when the dollar falls, about 40% of the fund). It is a money cushion, not a currency hedge, and it is smallest when stocks are down.

**W10 (L). The range is a commitment rule, not a forecast.** The case: "state how confident they are that her 2033 contribution will fall within that range". In XR both ends are owned, so the confidence is about 100% by construction. That is clever, but a judge could say the question was dodged. The IPS says nothing about confidence. Wharton says the final range is a Final Report item, so this is low risk.

**Case facts, dates, cash flows the plan misses:** none that break it. The timing (beginning of year, Nov or Dec maturities, 2028 floor in a 2032 fund) is handled. The real gaps are W3 (purchase-day yield), W5 and W8. One more: if the residency slips a year, a hold-to-date ladder is rigid. The case fixes 2033, so this is only a Final Report line.

---

## 3. The five strongest strategy-level moves

Ranked by how much a sharp investor would say "that's clever", with honest sizes. I also say where I would not bother (end of section).

### Move 1. Buy the owned bottom at its market price, and give the gift only Treasuries
**Idea.** Stop sizing the share sleeve by "the interest forgone" (principal protection, which is a mental-account number: $150k is just the deposit). Size it by a loss budget instead, and benchmark every version against the Treasuries-only twin. Corollary: the gift is made only of Treasuries; shares hold only Laura's kept money, which has the long horizon (project overruns can come any time to 2042).

**Mechanism and arithmetic (MODEL; deposit $150k, 4.9 years, Treasuries 4.98%, shares 7.5% mean and 16.5% volatility, ladder fits, no gap charge):**

| Shares as share of deposit | Owned bottom | p5 | Median | p95 | Mean |
|---|---|---|---|---|---|
| 0% (Treasuries only) | $190k | $190k | $190k | $190k | $190k |
| 10% ($15k) | $171k | $182-183k | $191-193k | $208-210k | $193-194k |
| 21% (XR, about $32k) | $150k | $173-175k | $192-195k | $227-232k | $195-198k |
| 40% | $114k | $158-161k | $194-200k | $260-270k | $200-206k |

Moving from 21% to 10% lifts the owned bottom by $21k and lifts the announced range from about $145-170k to about $165-180k (top = floor + half the 2031 share value, locked: $171k floor + about $10k). It costs about $2-4k of expected 2033 money: 10 to 19 cents of expected value per $1 of extra owned bottom. Shares in the first $15k are the best-priced; in the next $17k they are poor (about $2-4k for about $20k of bottom). At today's 5% Treasury yield the equity premium is only about 2.5 points, so certainty is cheap and growth is expensive. It would not be so at a 2% yield.

**Cost or downside.** p95 falls by about $20k; less "growth" optics for a judge who counts equity weight; a smaller share sleeve means the "thoughtful risks" bullet is thinner. The 2028 yield is unknown (plus or minus 100bp moves the all-Treasury figure by about $9k), so the numbers shift but the shape holds.

**Typical strong team.** Reads the range off a Monte Carlo with 20-30% equities, so the bottom is below $150k and nobody asks what Treasuries alone give.

**Change to traded portfolio?** Not required: it is a rule for the 2028 purchase (floor face = nine-tenths of what the whole deposit grows to in Treasuries). Cleaner if the book matches: sell about half the VT (167 shares, $26k) and add to IBTM before the 6 Nov freeze (two trades, $50). I would not do that last step; the book is a stand-in.

**In IDEA_BANK?** Partly. Sizing rules exist (#36 "risk only the interest", Merton 21% of the deposit; #127 "under a tenth of her money"; #47 haircut on the lock). Floor priced against growth rivals (#99-#103). I found nothing on the marginal price of owned bottom, a Treasuries-only benchmark, or "gift all Treasuries, shares kept only" (greps: frontier, marginal, per dollar, only/all Treasur, bigger floor: no relevant hits).

**IPS change.** Replace "roughly the interest that fund will earn" with: "We buy shares only with what is left after her bottom keeps nine-tenths of what Treasuries alone would give her; at today's yields that is under a twentieth of her money."

### Move 2. Make the top of the range a match, not a pledge
**Idea.** Bottom unconditional (owned). The part between bottom and top is released only if co-sponsors have raised an equal amount by a set date ("Laura puts in $X; up to $Y more, dollar for dollar").

**Mechanism.** Two of the case's five required bullets are about co-sponsors and flexibility: "communicates ... clearly and credibly" and "preserves appropriate financial flexibility". A conditional top does both: Karlan and List (2007, already cited in bank #6) found a 1:1 match raised revenue per solicitation by about 19% and response by about 22%, and ratios above 1:1 add nothing. It also leaves the top about $20-25k of Laura's own money if the co-sponsors do not turn up.

**Arithmetic (illustrative, not forecast).** XR's top band is about $20-25k ($150k to $170k). If the chance that co-sponsors have not matched by the date is 40%, expected extra flexibility is about $8-10k, on top of the $22k kept half, at no cost to the portfolio. That is about 40% more flexibility money for zero dollars.

**Cost or downside.** The case asks for the range of "her 2033 contribution", and a match makes the contribution depend on others. A judge may read it as hedging the very answer asked for. Mitigate by making the *bottom* the committed range and the match only the top band, and by keeping the whole range owned (the plan's key strength). It also adds a rule to a crowded IPS.

**Typical strong team.** A simulated range with a confidence level and a plain "Laura will contribute between $X and $Y".

**Change to traded portfolio?** None. It is the 2031 message and the Final Report's co-sponsor text.

**In IDEA_BANK?** Partly: #6 (donor study, seed money; Karlan-List cited as a fact), #23 (bottom unconditional, top by rule; "don't write 'only if stocks hold'"). The match-triggered top itself: not found (greps: conditional, matching, co-sponsors raised: no).

**IPS change.** "The bottom is the part she already owns; the rest she releases dollar for dollar as co-sponsors give."

### Move 3. Ask Laura to sign the first part of her 2028 deposit, in order of contractedness
**Idea.** The plan's one soft leg is the 2028 deposit (it finishes the ladder in about two worlds in five and, by the bank's own numbers #50, #92, backs the coupon gap when it is above about $85k). The case says the deposit comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures". A publishing advance is a signed contract; speaking and licensing are not. Ask Laura to earmark contracted advances first and tell us, by 31 Dec 2026, how much of the $150k is signed.

**Mechanism.** Turns "can dry up" (IPS para 7) from a worry into a checked fact. If at least about $85k is contracted, the cheques need no further insurance in the bank's tests; if not, the plan says in advance what changes (the 2033 rung waits, the kept half is bigger).

**Arithmetic.** Bank #92: a cheque is short by more than $1k at a 2028 deposit of $50k with unchanged yields in about 0.45% of paths, and a deposit of about $100k clears a 1pt fall. So the question is not "does she have $150k" but "does she have $85-100k under contract". It costs nothing. The ladder-fit problem (W3, average excess $1.5-5k) is also covered.

**Cost or downside.** Not an investment move; a client conversation. Contracts can still be breached, and advances may be paid in tranches after 2028. The IPS must not invent facts about her contracts (Wharton ethics): it can only say "we will ask".

**Typical strong team.** Treats the $150k as given (the case says to) or ignores the risk.

**Change to traded portfolio?** None.

**In IDEA_BANK?** The threshold is (#92, #50, #73, #171 on order as a hedge). The ask itself, tied to the contract status of advances versus speaking and licensing, I did not find (greps: contracted, earmark, signed, royalt).

**IPS change.** "We will ask her to put signed publishing advances in the 2028 deposit first."

### Move 4. Pick the shares by what Laura already owns too much of
**Idea.** Laura's human capital is US creative-market income (US publishing advances, US speaking, licensing, her tech-industry past). A cap-weighted world fund is about 60% US, so it doubles up on her biggest existing exposure. Hold the sleeve as world ex-US, or tilt it.

**Mechanism.** A hedge by diversification away from her income, plus a weak USD offset against Taiwan-dollar cost (a falling USD lifts foreign holdings in dollar terms), plus J.P. Morgan's own assumptions (US large cap 6.7%, EAFE 7.5%, from the repo's notes).

**Arithmetic.** If the sleeve is $16-32k and ex-US earns 0.8 points more for 4.9 years: +$0.6-1.3k expected. The correlation benefit is real but small: ex-US versus US equities correlation is about 0.8-0.9 (my assumption). **This is small.** It matters as reasoning, not as dollars.

**Cost or downside.** Gives up the "one world fund by arithmetic" simplicity (bank FRB-42); the foreign-hedge point was already judged "worth a few hundred dollars" (ERUDITION_PLAN 3b). Emerging Taiwan concentration (one big chip company) is a risk if the ex-US fund is heavy there.

**Typical strong team.** VT, VTI or an S&P fund, or sector tilts.

**Change to traded portfolio?** Yes if wanted: swap VT 167 shares for an ex-US fund (WInS listing UNVERIFIED), two trades. Otherwise a rule for 2028.

**In IDEA_BANK?** Human capital as a share yes (#7, #170, #171). Ex-US tilt as the answer: not found (greps ex-US, VXUS, home bias, international: no relevant hits).

**IPS change.** "Her income already rides on American creative markets, so her shares sit mainly outside America."

### Move 5. Buy the thinnest-coupon Treasury for each date (promote an idea the team already has)
**Idea.** The ladder's weak point is coupons that arrive years before the cheque they pay for and must be reinvested. Where the same maturity exists twice, buy the 2020-21 low-coupon issue (1.375% Nov 2040, 1.875% Feb 2041, 2% Nov 2041), which is the nearest legal thing to the banned zero.

**Mechanism and arithmetic.** My dedication model (annual coupons, spot curve bootstrapped from the Sep-2026 par curve): PV of coupons that wait before 2033 is about 23% of ladder cost at a 5.2% coupon, 16% at 3%, 9% at 1.5%, about 0% at zero. But only about two rungs have thin twins (the bank agrees: #55), so the real saving is about 15% of the gap: roughly $21k to $17-18k at the team's "yields down 2 points for good". **Small.** Yield pickup on off-the-run issues (5-15bp, UNVERIFIED) would also raise headroom by $1.5-4k, helping W3.

**Cost or downside.** Thin issues are less liquid, WInS listing unverified, the filed Trade Notes name fat bonds so an IPS sentence invites "why not in WInS?" (the bank's own caution).

**Typical strong team.** Buys the on-the-run or most liquid bond for each date.

**Change to traded portfolio?** No for the plan; yes only if the book is to show it (not worth it).

**In IDEA_BANK?** Yes: #55 (thin-coupon twin, Window W-01) and #152 (the gap is about a tenth of the cheques). It was kept for the Final Report. I include it only as a promotion candidate.

**IPS change.** "Where a date has two bonds, we buy the one with the smaller coupon."

### Tested and not recommended
- **Put the share sleeve into long Treasuries (a hedge for the coupon gap and the deposit).** Gap cover on a 2pt fall: $32k x duration 11.5 x 2% = about $7.4k against a $21k gap (about 35%). Expected cost: 32k x (1.075^4.9 - 1.055^4.9) = about $4k. Cover pays only in a roughly 7% tail. Negative value; reject. (Bank #61 already priced the full version, $64-74k of 30-year, and turned it down.)
- **TIPS or TIPS ETFs for the facility's inflation exposure.** The FAQ bans TIPS and STRIPS as securities; the "individual" wording in WHARTON_WORD makes ETFs ambiguous. Not worth the integrity risk.
- **Buy the cheques in tranches in 2027.** Exposure runs until each purchase, so it lengthens risk, not shortens it.
- **Fund the 2027 money's floor first and cheques in 2028.** Puts duration-10 exposure on the 2028 curve. The current order (cheques first, floor second) is right and #171 argues it.

---

## 4. Recommendation

**Do Move 1, and say so in the IPS: price the bottom against Treasuries alone.** It is the only item that changes what a sharp reader concludes about the team's intelligence. Today the IPS shows a plan that is careful but silent about the dollars: a judge can derive that the share sleeve adds about $3-8k and lowers the owned bottom by about $40k. If the IPS shows the team saw that first (a smaller sleeve, a bottom that keeps nine-tenths of what Treasuries give, shares only with what Laura can lose), the plan reads as someone who knows where the money is and where it is not. It also removes the biggest "over-complex for the insight" exposure by cutting what the lock rules must defend, and it is a rule for 2028, not a change to the traded book.

**Pair it with Move 3 (the signed-advance ask).** It costs nothing, is pure client knowledge (Wharton's second criterion), and it makes the plan's one soft leg checkable instead of argued. Fourteen words.

**If only one sentence of room:** Move 1.

**What I would not do:** add anything (Moves 4 and 5 are reasoning, not dollars; Move 2 is clever but strains the case's wording). The IPS is at 493 of 500 words, and every new sentence needs one old one cut. The cleanest cut is the "pension funds" comparison (para 5) or part of the bank sentence in para 9, not any of the plan's own rules.

Files: this note; `ladder_sonnet_calc.py` beside it (arithmetic). Nothing in the repo was edited.
