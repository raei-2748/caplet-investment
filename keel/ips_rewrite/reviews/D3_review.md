# D3 review: pitch + IPS (second reviewer, cold read)

AI-generated review (Claude Code), 26 Oct 2026. Not for submission.

Draft: `keel/ips_rewrite/drafts/D3/pitch.txt` (47 words) and `ips.txt` (490 words). Read cold first; then
`00_GROUND_TRUTH.md`, `INSTRUCTIONS.md` I01-I12 and I34-I37, `research/R03_voice_study.md`, the case, the D1 lab
note, and the TNA as held (`keel/rooms/archive.md`). Sections 1-3 were written before opening `reviews/` or the
draft README.

**Gut reaction (cold):** this is the first draft that reads like it has a point of view and not a compliance
checklist. The pharmacist paragraph and the bank-note paragraph are the two I would remember on a train. Then
the last third goes slack: three short housekeeping paragraphs and a run of short punchy lines that start to feel
like a copywriter showing off. It sounds clever. It does not yet sound like Ray.

---

## 1. Cut-through test

**Does it stand out in 30 seconds? Yes.** In a pile of 300 IPSs that open "This Investment Policy Statement
governs...", this one opens on a cheque and a rule ("nobody else may help") and gets to the name joke by about
second 20. The lines doing the work, in order of strength:

1. "Laura already owns plenty of stock-market risk – it just isn't in a brokerage account." This is the real
   aha: her income is the equity she already holds, and the next sentence shows it matters for rates too (a slump
   cuts the deposit *and* makes the unbought rungs dearer). Very few teams will reach the correlation between
   her income and the price of the bonds she still has to buy. Keep it word for word.
2. "A bank would sell Laura a capital-protected note: a bond that returns her money, an option on the market,
   and a fee." Taking a retail structured product apart and rebuilding it out of things WInS allows is the
   kind of knowledge applied that north star 4 asks for. A judge from asset management will nod.
3. "To a pharmacist, XR means extended release: a dose let out on schedule, labelled do not crush. To us, X is
   ten and R is redemption." Both meanings, in two sentences, and "redeemed" is the right Treasury word. I34 is met.
4. "a number said aloud cannot be half-kept. / We refuse." The best single line on the 2031 range in the draft.
5. "Until 2033 nothing is sold early. Do not crush." The callback earns the motif. It is a tool here, not decoration.

**Weakest paragraph: "The soft spot is reinvestment."** Three faults in 37 words. (a) "the floor last" puts the
order in the wrong year: the coupon gap appears in 2038-42, but the floor became the facility gift in 2033, so a
judge wonders what floor is left. (b) "We assume stocks beat Treasuries over decades" doesn't fit the plan: the
stocks are held for five years, and the whole design is that nothing *needs* them to beat anything. (c) It reads
as two leftover case requirements (risk, assumptions) stapled together. It has the plan's best line hiding inside
it and doesn't say it: we expect stocks to win, and no payment needs them to.

Runner-up for weakest: "Until 2033 nothing is sold early..." – five unrelated clauses (sales, liquidity, reserve,
review, WInS). It's saved only by "Do not crush."

## 2. Voice test against Ray's own writing

**Verdict: not yet the same person.** Ray's three TNA reflections average **27 words a sentence** (11 sentences,
18 to 54 words, none shorter than 18), with 8 en dashes and 4 brackets in 300 words. D3 averages **13 words**
(37 sentences, **7 of 5 words or fewer**), with 3 dashes and 1 bracket in 490. Ray thinks out loud in long,
dash-hinged sentences ("Every year the bonds sit untouched is a good year – one less year of Laura's money being
exposed to anything the restless markets might decide to do"). He uses connectives ("In other words,",
"Notably –", "The catch is,"), and his adjectives have some weight to them ("restless markets", "the vain illusion",
"a nonexistent inflation risk"). D3 has his moves (a question answered at once, a one-line paragraph, a jokey bracket,
an ending that calls back), but it spends them all at once. So many fragment-kickers stacked together is now one of
the most recognisable AI tells. Ray's essays use one one-word paragraph per essay, not seven.

Sentences a sharp reader would still flag as machine-written (five, with rewrites at equal or shorter length):

| # | Draft | Why it reads as machine | Rewrite in Ray's register |
|---|---|---|---|
| V1 | "If that deposit comes in smaller, the facility gift shrinks. A payment never does." (14) | The "X does. Y never does." antithesis is a stock AI closer. It is also wrong (section 3, F5) | "A smaller deposit shrinks the facility gift long before it could reach a payment." (14) |
| V2 | "Moving floor money into stocks would raise the expected gift. But time shrinks the chance of a stock loss, not its size, and a number said aloud cannot be half-kept." (30) | Answers an objection nobody has raised yet. Ray's move 2 is to let the other side speak first in its own blunt words | "Five years rarely loses, says the sceptic: move the floor into stocks. Rarely – but time makes a loss rarer, not smaller, and a number said aloud cannot be half-kept." (29) |
| V3 | "Ten cheques, ten Januaries. Every one bought before the first is written." (12) | A verbless "Ten X, ten Y." pair is the most common AI sign-off there is | "Ten cheques, then – each bought before the first is written." (10) |
| V4 | "We assume stocks beat Treasuries over decades, and inflation cannot touch fixed payments." (13) | A compliance sentence ticking the case's assumptions list, with a wrong horizon | "Stocks should beat Treasuries; no payment needs them to. Inflation can't touch one." (13) |
| V5 | "The catch: a boom pays her less than an option would." (11) | The colon-fragment "The catch:" is the AI version of Ray's own phrase. His TNA reflection 2 says "The catch is," | "The catch is, a boom pays less than an option would." (11) |

Leave alone: "it just isn't in a brokerage account", "picking winners is not on the menu" (a real Ray bracket),
"We refuse." (one one-line paragraph is his; keep this one and let the others go), the pharmacist paragraph.

## 3. Finance pedant

What an FI or derivatives professional would challenge. Strong words that are true are left alone, as Ray asks (I10, I35).

| # | Sentence | Verdict | Exact problem | Fix |
|---|---|---|---|---|
| F1 | "We keep the bond, swap the option for the stocks themselves and skip the fee." | **Loose, and it gives away the best point** | In a capital-protected note the "bond" is the *bank's own* debt, not a Treasury. Holders of Lehman's principal-protected notes became unsecured creditors in Sept 2008. So D3 doesn't keep the bond: it swaps bank credit for Treasury credit, which is the strongest argument for the design, and the draft doesn't make it. "Swap the option for the stocks" is fine as plain English: same dollar budget (the bond discount), same worst case (lose that budget). Note the stocks are 1x exposure on about $32k, where the option is participation on the whole $150k | See section 5 |
| F2 | "The rest, its expected interest, buys one world index fund" | **Acceptable, slightly loose** | Strictly it's the bond *discount* to the target value, and the floor fund pays monthly distributions that must be reinvested for five years to "grow back to the whole". The lab prices that in (1-in-100 payout 98.7% of target). "Expected" carries it. No fix needed. Optional: "The rest – what that fund is expected to earn – buys..." (clearer, section 4) | optional |
| F3 | "a boom pays her less than an option would" | **True, and it undersells the plan** | True in a strong boom: the option gives participation on the full notional. But in a flat, mild or falling market the option expires worthless and the stocks keep their value, and the stocks also collect dividends, which an option on a price index does not. Reviewer's back-of-envelope (Black-Scholes, 16.8% vol, 5 yrs, UNVERIFIED, not for the text): the stocks win unless the index rises roughly 30-40% over the five years. "Boom" is the honest word. No fix needed; the Final Report should show the crossover | none (FR: crossover) |
| F4 | "time shrinks the chance of a stock loss, not its size" | **Half wrong** | Time lowers the *probability* of a loss, but the spread of outcomes widens (by the square root of time), so the worst losses get *bigger*, not the same size. That's why the cost of insuring against a shortfall *rises* with the horizon. "Not its size" understates the case D3 is making | "time makes a stock loss rarer, not smaller" (in V2) |
| F5 | "If that deposit comes in smaller, the facility gift shrinks. A payment never does." | **False on the draft's own argument** | The paragraph has just argued that a slump cuts the deposit *and* cuts yields, which makes the unbought rungs dearer. That's exactly the case where the gap grows while the deposit shrinks. A payment is safe only while the deposit covers the gap (lab: gap about $0 today, $30k at -1pt, $65k at -2pt, against a $150k deposit). "Never" fails in the tail the draft itself describes, and a judge who follows the logic will catch it | V1 |
| F6 | "after 2031 only a two-year stock fall or a payment in need can pull it lower" | **Not exhaustive** | Lab (c): of the 24.4% of paths that end below the top, 3.2 points have *no* stock fall: the floor fund paid a little under its projection, or a coupon gap reached the gift. "Only" makes it false, and "a two-year stock fall" reads as a fall that lasts two years | "In 2033 the same rule sets the gift, capped at that top: only falling stocks, a floor paying short or a payment needing help leave it below." (27, was 29) |
| F7 | "By their December close, they hold nothing but cash." | **Fine** | Strictly cash and cash equivalents (T-bills, money-market funds) in the final months, paid out as final NAV. Ray's I35 position is correct, and "cash" is the right strong word | none |
| F8 | "Every one bought before the first is written." | **Fine, with the soft-spot paragraph next to it** | The 2039-42 payments lean partly on reinvested coupons (the WInS notes say so), so strictly they are *mostly* bought. Because the soft spot is stated two paragraphs up, the line is a fair close, not an overclaim | keep (V3 for voice) |
| F9 | "any gap comes from Laura's half first and the floor last" | **Wrong year** | By the time a coupon gap appears (2038+), the floor has already gone to the facility in 2033. What the plan does is hold the gap back *in 2033*, first from Laura's half and then from the gift. Also the order depends on vote D1a (Tue 27 Oct) | "any gap is held back in 2033, from Laura's half first and the gift last." (pending D1a) |
| F10 | Pitch: "Her first $300,000 buys a Treasury for each of ten $50,000 payments." | **One-close call** | Lab: the ladder costs more than $300k in 47% of paths by January, and the IPS body says so itself ("any gap is the 2028 deposit's first job"). The pitch states as fact what the body treats as conditional. Also five of the ten are iBond funds, not "a Treasury" | "Her first $300,000 buys Treasuries for ten $50,000 payments; her second tops them up, then becomes..." (net +1; pitch goes to 48) |
| F11 | "ten Treasuries, each redeemed" | **Fine for a motif line** | Five are funds that liquidate rather than redeem, but the TNA has already told judges that. Motif licence | none |
| F12 | "a slump that shrinks those would likely cut yields too" | **True as worded** | Holds for demand-led slumps (2001, 2008, 2020), not for 2022, when stocks and bonds fell together. "Likely" is earned, not hedging. Keep | none |

## 4. Clarity for a tired judge

- **"Laura risks only money she hasn't earned yet."** Read twice, and probably misread. The paragraph before
  says her 2028 deposit comes from book advances she hasn't earned yet, so a judge will hear "she's betting
  the deposit". It also repeats "intact even if every share went to zero". Cut it (section 5 uses the words).
- **"sized to grow back to the whole"** – the whole what? Say "the whole remainder" or "to what she put in".
- **"We take 'a high degree of certainty' to mean by January 2028..."** Needs "that" after "mean". Without it
  the eye trips on "mean by".
- **"a two-year stock fall or a payment in need"** – see F6. "A payment in need" isn't a phrase anyone uses.
- **"the floor last"** – see F9.
- **"latest-dated first"** – the reason (long rungs are the most rate-sensitive, so lock them while the price is
  known) would cost three words in a bracket and turn a procedure into knowledge applied. Optional.
- Undefined terms: none that matter. "Defined-maturity Treasury fund" is self-explaining. "Capital-protected
  note" is known to the judges who matter.

## 5. One upgrade (zero net words)

Use the bank note's own weakness, issuer credit, which D3 currently gives away (F1). It also removes the
ambiguous line from section 4.

**Replace** (22 words, two sentences):
> We keep the bond, swap the option for the stocks themselves and skip the fee.
> ...
> Laura risks only money she hasn't earned yet.

**With** (22 words, one sentence, in place of the first; delete the second):
> We swap the bank's IOU for a Treasury (ask Lehman's customers why), the option for the stocks themselves, and skip the fee.

Why it's the biggest gain for the words: it is knowledge used to argue, not dropped as a name (N4), and the
one-bracket joke is Ray's move 13 (N1). It says *why* Treasuries are near-ironclad and a bank's "protection"
is not, which backs up the definition paragraph. And no other team will turn the 2008 lesson on a retail product
into a reason for its own design (N3). If two brackets in three sentences feel crowded, drop "(picking winners
is not on the menu)" – the TNA's "vain illusion" line has already made that point.

## 6. Verdict

**Ship as near-final for Caplet's review (Sat 31 Oct) after the must-fixes below.** These are surgical, not a
rewrite: the structure, the motif and both ahas hold. Word count stays at or under 490.

**Must-fix**
1. F5/V1 – "A payment never does." is false on the draft's own correlation argument. Use V1.
2. F6 – "only a two-year stock fall or a payment in need" leaves out the floor paying short. Use the F6 line.
3. F4/V2 – "not its size" is wrong (worst losses grow with time). Use V2: "rarer, not smaller", with the
   sceptic voiced.
4. F9 – "the floor last" is the wrong year. Hold the gap back in 2033 (wording follows vote D1a).
5. Section 5 – the bank-IOU/Lehman swap, which also removes "money she hasn't earned yet".
6. Voice – cut the fragment-kickers from seven to two or three (keep "We refuse." and "Do not crush."). Use V3-V5
   and let two or three sentences run long with an en-dash hinge, the way Ray's reflections do.

**Should-fix:** F10 (pitch says the first $300k buys all ten; the body says it may not); "to mean that";
"the whole remainder"; the reason for "latest-dated first".
