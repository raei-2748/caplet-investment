# Cold aha test 6, Wed 18 Nov 2026: the key (Keel only; the readers never see this file)

These are notes for the Final Report store, not report prose. The test is built to `../aha_test_2026-11-17_evening/RESULTS.md`, "Test 6 (recommended)".

Test 5's readers saw all nine items in one file, and its context paragraph gave away two answers (D's standard and F's order). This test fixes both:

- **One file per item.** Each reader opens `01.md` to `08.md` one at a time and writes each answer before opening the next file.
- **No answers in the context.** The context gives the plan's holdings but not what any item tests.

It carries four rows with test 5's fixes, a candidate from the reserves, row 1 beside row 7 for the first time, and row 3 unchanged as the control.

**Where things are**

- The packs are outside the repo, in `/tmp/claude-0/-home-user/cdd961e4-901c-5589-a829-32f064718722/scratchpad/aha6/`:
  - `BRIEF_READER.md`;
  - `X/01.md` to `X/08.md`, `Y/...` and `N/...`;
  - the answer files `ANSWERS_X.md`, `ANSWERS_Y.md` and `ANSWERS_N.md`, which the readers write.
- They were built by `.../scratchpad/aha6_build/build.py` and `orders.py`, kept outside the readers' folder.
- `BRIEF_READER.md` here is an identical copy of the brief.
- `ITEMS.md` here is the record copy of all eight items, in letter order.

**The readers** are three simulated model readers, never people:

| Reader | Role |
|---|---|
| X | Investment professional who builds Treasury portfolios for institutions |
| Y | Finance professor who teaches fixed income |
| N | Finance director of a mid-sized nonprofit arts organisation |

N is the one role from outside fixed income that test 5 asked for. It replaces test 5's Z, a former finalist of a student competition. Test 2 used the same role.

Their scores and recall say how the words read and which figure stands out, never how people remember.

## Which letter is which

Every plan figure comes from `../../../NUMBERS.md` as it stands on Wed 18 Nov morning. That is the Tue 17 Nov evening re-size, which added the 0.5% margin on the payments and the 365.25-day fix. Section 8u was added Wed 18 Nov and moves no figure. A † marks a figure moved by the re-size; the old figure is in the re-size table below.

| Letter | Register row | Status | Part and Wharton's job |
|---|---|---|---|
| J | Reserve: the comfort letter (test 5's H) | Fixed, test 5's flags 1-4 | 3d: why the co-sponsor words will be believed |
| K | Spine row 5 (test 5's D), with the 1982 bond (test 5's E) as its first sentence | Fixed, D's fixes 1-5 and E's 1-4 | 3a: the operating reserve, sized by a test with history |
| L | Spine row 7 | Retest; last read cold in test 2, at 3.7 | 3c: what moves the stated range, and why she speaks only after the move |
| M | Spine row 1 (Neyman) | Retest beside row 7, as test 5's KEY planned; last read in test 3, at 3.7 | 3c: the range's confidence |
| P | Spine row 6 (test 5's G) | Fixed, fixes 1-4 | 3b: the split of the building money, tested from both sides |
| R | Spine row 10, version B as reframed Tue 17 Nov evening (test 5's I) | Fixed, fixes 1-3, plus the price of "none" | 3f, Team Reflection: thinking that changed |
| T | Reserve: the order of purchase (test 5's F; GOLDMINE #39) | Fixed, fixes 1-5 with the zero-rate bound | 2.3 or 3e: the 2028 deposit as the one input not owned |
| W | Spine row 3 (test 5's B) | **Control**, word for word test 5's item B (checked by diff) | 2.5: what really set the cost |

### Sources, item by item

**J (comfort letter).**

- The case:
  - card Q99 row 1: the letter's sentence; the Court of Appeal, 2 Feb 1989, "a statement of present fact and not a promise as to future conduct"; £12.26m with interest;
  - row 4: October 1985; the later telex's "our policy at that time" and "no assurance";
  - row 36: Laura's 2031 words as a fact plus a promise, the fact making the promise believable;
  - row 4's guard: never that her words bind her.
- The top, $115,000 on today's figures: NUMBERS 4.
- Each end counted at what its Treasuries pay with no more interest, after fees: NUMBERS 3 and 4, the range rule.
- The bottom held since January 2028, and "funds ending in late 2032": NUMBERS 4 and 8g.
- The top as "her contribution and the figure co-sponsors count": `../../meta/WHY_A_RANGE_2026-11-16.md`, option (b).

**K (row 5 with the 1982 bond).**

- The bond:
  - card Q104 row 41 (Renberg, Baltimore Sun, 10 May 1992, "locked in");
  - row 42 (9.29% a year with coupons rolled in six-month bills; Keel arithmetic on FRED DGS6MO).
- "Reinvested coupons fund the rest": WN l.18 (CANON A17).
- $302,287: NUMBERS 1.
- 5.12% flat break-even, between forwards of 4.67% and 5.43%: NUMBERS 8a.
- 585 starting months:
  - NUMBERS 2 finding 1: more often than not for starts since 1981, about 1 in 6 for 1962-80 (17.1%);
  - design A: when short, a median of $16,055; $34,555 at 1 in 20; $45,266 at worst, a July 2007 start.
- Under 0.15% in 90 of the 222 months from January 2008 to June 2026: NUMBERS 8a (card Q81).
- The escrow verifier's "sufficient without reinvestment": NUMBERS 2 finding 3.
- The bill fund's 0.15% fee: NUMBERS 0 and 2.
- The 0.5% margin on every fund payout: NUMBERS, the Tue 17 Nov evening box, and section 2. †
- "About $39,000": NUMBERS 2 and 5 ($39,162, 26.1%; the register's own wording is "about $39,000"). †
- "The first $2,400 or so": the $2,388 top-up (IPS l.13; WORDS l.66).
- "About $46,600 in 1 January 2033 money if rates hold, all of it Laura's by the last payment in 2042": NUMBERS 8h and 8k ($46,566). †
- "None beyond that 0.5% margin": NUMBERS 2, design H_plain:
  - at 0% with the fee, $1,177 spare, and that $1,177 is the margin;
  - with the fee and 0.5% fund costs, nothing spare.

**L (row 7).**

- 7.5% (J.P. Morgan), "above the middle of published forecasts (median about 6.5%)": CANON B15, card Q117 (Goldman Sachs's 7.7% was missing from the fifteen), card Q6b and NUMBERS 8p.
- The rule, whole $5,000 steps rounded down: NUMBERS 4, the range rule.
- Fifteen houses from GMO's -2.5% to BlackRock's 9.0%; thirteen give $115,000; GMO and Ninety One give $110,000: NUMBERS 8p. †
- 2.9%, 6.2%, 8.6% and 10.6% for a top named 1, 3, 6 or 12 months early: NUMBERS 4, "Why nothing is stated before the move". † (Rows 698 and 719 of the void table confirm 6.2%, not 6.3%.)
- GAO's "The very act of obligating ...": card Q43 row 9 and card Q58 row 33, B-300480.

**M (row 1, Neyman).**

- Neyman 1937, zero or one: card Q74 rows 2 and 10.
- 59% of 118 researchers endorsed "There is a 95% probability that the true mean lies ..." (Hoekstra et al. 2014): card Q74 row 7.
- At least 0.5% to spare for costs beyond the fees: NUMBERS 3, the Bond desk 4 check figures.
- About 2% on today's figures (2.32%): the same section. †
- At most about $120 per further 0.1%: the same section's "about $118 ... a ceiling on the slope". † The register's row 1 rounds it to about $120.
- 91 and 57 in 100 at 7.5%: NUMBERS 4, the odds table (91.2%, 57.2%). †
- "The two figures record how long each part has been held, not a margin for error": WHY_A_RANGE option (b). It moved here from J under test 5's H fix 4.

**P (row 6).**

- The split, "about three-quarters / about a quarter" of the building money: NUMBERS 4. The floor takes the larger of 73.3% of what is left and $75,001.
- Three-quarters in shares: NUMBERS 8n, option D, a bottom of $30,000 and the contribution under $95,000 in 64% (was 62%). †
- The all-Treasury option:
  - section 4 C8 and NUMBERS 8n option A: $130,000, a stated figure above the plan's top in 94.8% (about 95);
  - the median flexibility of $9,000 against $29,000: 8n, options A and B;
  - contribution plus flexibility smaller in 62.8% (about 63): C8;
  - the trade, "$15,000 of the median contribution for $20,000 more median flexibility, at the same 1-in-20 low of all money ($159,000)": 8n's reading;
  - "$110,000" with the same flexibility: C8.

**R (row 10).**

- "A high degree of certainty" is the case's phrase.
- The first plan (75% shares to 2030, 40% in 2032, the ten bought on 1 Jan 2033) and its figures: NUMBERS 8s:
  - 3.2% short, 3.2265%, 6,453 of 200,000, 1 in 31.0;
  - 6.7% US large-cap compound;
  - 5.5% at 5.0%;
  - a median miss of $27,695.
- 96.8 is Keel arithmetic (100 - 3.2265).
- About 90% (judges), and the SEC's "a high degree of confidence" as at least 90%: card Q120 rows 1, 6 and 15; register row 10.
- The reason, IPS l.9, in the team's words: CANON A3.
- "None" from January 2028: NUMBERS 2 and 8s ("none" rests on the standard, not on the 27 Sep code).
- "Once the first quarter or so of the second deposit is in": NUMBERS 5 ($39,162, 26.1% of $150,000). †
- The price of "none": NUMBERS 8s, "What none cost Laura" (Keel arithmetic, MODEL, 27 Sep pair):
  - $207,290 against $226,096 at the median, about $19,000;
  - at the 1-in-20 low, $159,224 against $19,990.

**T (order of purchase).**

- The premise: IPS l.9.
- "About $39,000": NUMBERS 5. †
- 73.9%: NUMBERS 5, the table row "None (6 Nov close)". †
- The zero-rate bound, from NUMBERS 5, "When 'most' cannot hold", answer (b): even at zero rates in January 2028 the first part costs $60,393 (about $60,000). †
- "About 60% smaller" is Keel arithmetic: 1 - 60,393 / 150,000 = 59.7%. †
- "Yields often fall in a slump": NUMBERS 7 and CANON D8.
- The missed deposit:
  - $57,455 at 0%, added across the ten dates: NUMBERS 5 and 8s;
  - "one of the plan's two named reasons to change course": IPS l.17.
- $112,500 gives a bottom of $65,000: NUMBERS 5.
- No rule added: CANON A34 and D9.

**W (control).** The figures are test 5's, from NUMBERS 8e, 8b, 8g and 5. "About 3.6 points" still holds after the re-size (3.57, was 3.60).

**Context paragraph.** IPS l.9 (paraphrased), l.11, l.15 and l.17; NUMBERS 4 (the range at 6 Nov 2026 rates).

## Figures changed from test 5 because of the re-size

| Item | Test 5 | Test 6 | NUMBERS |
|---|---|---|---|
| K, T | about $38,000 ($38,282) | about $39,000 ($39,162) | 2, 5 |
| K | about $45,500 back ($45,456) | about $46,600 ($46,566) | 8h, 8k |
| K | (none) | a 0.5% margin on every fund payout; "none beyond that 0.5% margin" | 2 |
| T | 74.5% | 73.9% | 5 |
| T | 69.8% after a two-point fall | dropped; the zero-rate bound $60,393 (about $60,000), 59.7% (test 5 RESULTS quoted $59,172, 60.6%) | 5 (b) |
| P | 62 in 100 under $95,000 | 64 in 100 | 8n |
| P | $111,718 of building money | dropped from the item ($110,838) | 4 |
| M | 92 and 60 in 100 | 91 and 57 in 100 | 4 |
| M | about 3% | about 2% | 3 |
| M | about $120 per 0.1% (the morning's $119) | about $120 ($118) | 3 |
| L | 14 of 15 houses | 13 of 15 (Ninety One joins GMO at $110,000) | 8p |
| L | 8.7% and 10.7% | 8.6% and 10.6% | 4 |
| R | "the second deposit's first dollars" | "the first quarter or so" (26.1%) | 5, 8s |
| W | 3.60 points | unchanged in the text ("about 3.6"); now 3.57 | 5 |

Moved in NUMBERS but kept out of the items: the $37,500-deposit shortfall ($782 to $1,662) and the plan's top at $130,000 or more (22.1% to 20.3%).

## Fixes applied, and from which flag

Flag numbers are test 5's, in `../aha_test_2026-11-17_evening/RESULTS.md`.

**K (row 5 with the 1982 bond)**

- **D1, every dollar (X):** applied. The text reads "only if the interest they pay before the payments earns today's forward rates ..., or a flat 5.12% a year on every waiting dollar". Forward rates are glossed once for reader N.
- **D2, forwards as a forecast (Y):** applied. The forecast is the team's own trade note; the item never calls forward rates the market's forecast.
- **D3, one rate cycle (X, Z):** applied, as "for start dates since 1981, the years rates fell".
- **D4, the IRS clause:** cut, which is the fix's second option. The 1982 bond now carries the history, and the IRS test stays in 3a's evidence and References.
- **D5, the price bundles two costs (Z):** applied, as "the first $2,400 or so of it completing the ten" (WORDS l.66).
- **D7, two near figures (X):** kept to separate sentences. They are now $45,266 and about $46,600.
- **D8 and E1:** applied. The standard is named as an escrow verifier's arithmetic plus "a condition history has met" (90 of 222 months). The fee comes below zero, and "strictest" is gone.
- **E2:** applied, as "the bond and its interest together returned 9.29% a year".
- **E3:** applied, as "as the plan's own waiting cash would be".
- **E4, one sentence inside D, story first:** applied.

**T (order of purchase)**

- **F1 (X):** applied: "only a deposit more than about three-quarters smaller would leave them short of it". The missed deposit is said separately.
- **F2 (X, Y, Z):** applied, as "$57,455 short of the $500,000 they owe, added across their ten dates, if cash waiting earns nothing".
- **F3 (Z):** applied, with one step only ($112,500: from $95,000 to $65,000).
- **F4 (X):** the zero-rate bound replaces the two-point case, as the spec asks. This also answers B's flag 4 ("two clocks"), since the bound is dated "during 2027, after the ten are bought".
- **F5 (X, Y, Z):** applied, as "The plan adds no rule for a smaller deposit; the same order simply runs".
- **Test 5's F verdict:** the order and its consequence are said together, on a context that no longer states the order (Y's prior 30).

**P (row 6)**

- **G1 (X, Z):** applied, in the RESULTS wording.
- **G2 (Y, Z):** applied. The trade is said ($15,000 for $20,000, the same $159,000 low), and so is what lowers the figure (half the shares promised to no one; $110,000 with the same flexibility). The plan's choice is never called "optimal".
- **G3 (Y), WORDS l.28:** applied. The text names both flexibility quantities: "what the fund pays above her one figure" against "the plan's unpromised half of the shares and what its funds pay above its top".
- **G4 (Z):** applied, as "the ten payments are the same in every split".
- **G6:** each base is named in words. "Contribution and flexibility together" is C8's base (63 in 100); "all the money left to her beyond the ten payments" is 8n's ($159,000).

**R (row 10)**

- **I1 (X, Y, Z):** applied. "It was not the reason for it" is gone. The reason (how a writer is paid) comes first, then "A test run on 27 September, before any trade, priced the change".
- **I2 (X, Y, Z):** applied, as "With US shares growing 6.7% a year ... (5.5% at 5.0% a year)".
- **I3 (X, Z):** applied, as "once the first quarter or so of the second deposit is in".
- **Register row 10's reframe** (the lead's call, Tue 17 Nov evening, on coherence reader 8 H1, CANON A4) is applied:
  - 96.8 in 100 passes the usual reading of "high" (about 90%), so "high" did not rule the first plan out;
  - the aha is the price of going a step further: about 1 in 31 against none;
  - never "3.2% fails 'high'".

**J (comfort letter)**

- **H1 (X, Y):** applied (card Q99 row 36):
  - Malaysia Mining gave only a fact, and its fact was an intention;
  - Laura's words have two parts;
  - the fact makes the promise believable and does not bind her (row 4's guard).
- **H2 (X):** "named for the facility" is dropped. The text says "held for her in Treasury funds ending in late 2032, which a broker statement shows".
- **H3 (Y, Z):** applied, as "each end is counted at what its Treasuries pay if they earn no more interest, after fees, so no fall in markets can take it lower".
- **H4 (X, Y, Z):** "why a range" leaves J. Option (b)'s sentence sits in M, and J is read straight after M in every order.
- "Policy" appears only on Malaysia Mining's side.

**M (row 1).** This is register row 1's wording on the re-sized figures:

- the condition in bond desk 4's signed form;
- "certain" with the range she states, once both ends are owned, as its subject;
- no "95%" or "confidence interval" label on Laura's range;
- the base named ("simulated futures").

**L (row 7).** This is register row 7 with cold test 2's fixes:

- "would turn out larger than the move could buy", never "not yet owned";
- one forecast test, the fifteen houses;
- the $5,000 steps said once as what they are;
- the Act as a parallel, never "the same rule".

## Fixes not applied, and why

- **D6, dedication (Y):** not applied. It is outside the spec's fixes 1-5. It is a 3a note for a bond reader: design B costs about $16,000 less but buys eight Treasuries, which breaks the IPS's ten and IBTM for the first payment (NUMBERS 2 finding 2).
- **E's other figures:** $6,144, $15,690, about 9.5% a year and the STRIPS clause are left out. The spec asks for E as one sentence.
- **G5 (optional):**
  - Not applied. Option D's "more in all in about 63 in 100" would put a second 63 in the item, for the opposite side from the all-Treasury 63, so it is left out to avoid the clash.
  - $111,718 (now $110,838) is dropped for the same density reason.
- **L:** three things are left out to keep one parallel and one forecast test:
  - J.P. Morgan's disclaimer;
  - the 4%-10% sweep ($3,241, about 0.65 of a step);
  - the Scottish-notes bridge (card Q58 row 14).
- **W:** test 5's B flags 1-6 are deliberately not applied. W is the control, so its score reads against test 5's 4.0 / 4.0. It still says "whatever ... unless" (B2) and "a rare year" (B1).
- **I4:** moot. The payments now carry the 0.5% margin, and the item claims nothing about early fund ends.
- **Beyond the fixes, in R:** R adds the price of "none" in the 27 Sep model's terms (register row 10; test 4 and test 5 readers asked for it). Caplet's own plan on today's engine gives up about $65,000 at the median, not $19,000 (8s). If this clause lands, 3f names the model it comes from.

## Orders and seed

- **Method** (`orders.py`, outside the readers' folder):
  1. All 8! orders were filtered by the constraints below, which left 106 valid orders.
  2. They were shuffled with `random.Random(20261118)`.
  3. The first triple, by `itertools.combinations` over the shuffled list, in which every item sits in a different position for each reader, was taken (shuffled indices 0, 1, 16).
- **Letters:** `random.Random(20261119)` shuffled J, K, L, M, P, R, T and W onto the eight items.
- **Constraints:**
  - L, M, J are read as one block in that order: row 1 beside row 7, and the comfort letter right after 3c's range sentence.
  - T comes before R and before W. R's "first quarter or so" and W's last sentence would show T's mechanism.
  - These pairs are never adjacent: W with K (both on what the ten cost); T with R (both lean on the deposit and the premise); P with J (test 5's G-H clash).

| Reader | Order |
|---|---|
| X | P, T, K, L, M, J, R, W |
| Y | T, K, R, P, W, L, M, J |
| N | L, M, J, K, T, P, W, R |

| Letter | X | Y | N |
|---|---|---|---|
| J | 6 | 8 | 3 |
| K | 3 | 2 | 4 |
| L | 4 | 6 | 1 |
| M | 5 | 7 | 2 |
| P | 1 | 4 | 6 |
| R | 7 | 3 | 8 |
| T | 2 | 1 | 5 |
| W | 8 | 5 | 7 |

## The context paragraph: what changed from test 5

**Taken out:**

- "$38,282";
- "even if cash waiting earns nothing";
- the second deposit's spending order ("The first $38,282 of the second deposit completes them ... Most of the rest buys ...").

**What it says now:** the second deposit "buys three things", named without amounts or order: more of the same Treasuries for the payments, a Treasury fund ending in late 2032, and VT.

**Kept:**

- the premise (IPS l.9, paraphrased);
- "may not rely on any outside money";
- the half moved before the 2031 meetings and the three uses of her flexibility (IPS l.15);
- the range at 6 Nov 2026 rates;
- the two named reasons to change course (IPS l.17), said as reasons to change course, never as the only ways the plan can fail (card Q109).

The words "Investment Policy Statement" are never used.

## Scoring key: the figure each reader should recall

Fields are as in test 5:

- surprise 1-5, with the old "aha strength" anchors;
- conviction 1-5;
- the prior and how sure, 0-100;
- the figure recalled from memory after the filler task;
- repeat tomorrow;
- three after 40 reports, and clashes.

Scores are read by role and never pooled as one audience.

| Item | Key figure | Also accept |
|---|---|---|
| J | $115,000 held for her in Treasury funds (the fact behind the promise) | "a statement of present fact and not a promise as to future conduct"; £12.26m; October 1985; 1989; January 2028; late 2032 |
| K | 5.12% on every waiting dollar | $302,287; 585 months; since 1981, about 1 in 6 before; $16,055; $34,555; $45,266 or July 2007; 14.25% and 9.29%; 1982 or 1992; 90 of 222 months; 0.15%; 0.5%; about $39,000; about $2,400; about $46,600 |
| L | 13 of 15 houses give the same $115,000 top | 7.5% against a median of about 6.5%; -2.5% and 9.0%; $110,000; $5,000 steps; 2.9%, 6.2%, 8.6% or 10.6%; 1, 3, 6 or 12 months |
| M | Probability zero or one: the range known to hold | 1937; 59% of 118 researchers; 0.5%; about 2%; about $120 per 0.1%; 7.5%; 91 in 100; 57 in 100; January 2028 |
| P | All-Treasury: less in all in about 63 futures in 100 | $30,000 bottom; 64 in 100 under $95,000; $130,000 one figure; about 95 in 100; $9,000 against $29,000; $15,000 for $20,000; $159,000; $110,000 |
| R | About 1 in 31 against none | 3.2%; 96.8 in 100; about 90%; 6.7%; 5.5% at 5.0%; $27,695; the first quarter or so; about $19,000; $159,000 against $20,000; 27 September; 1 January 2033 |
| T | About three-quarters smaller (73.9%) | about $39,000; about $60,000 or about 60%; $57,455; $112,500 to $65,000; $95,000 |
| W | One day from June 2007 to August 2026 (19 October 2023) | 10.9% of days since 2000; $470,217; $200 against $37,625; $325,563 and $287,938; May 2002; 3.6 points |

**What to read beside the scores**

- **The control:** W scored 4.0 / 4.0 in test 5. If W falls well below that, the one-file packs or the new role (N) make this panel harsher, and the other items are read against it.
- **K against test 5's D (2.7 / 4.7):** this shows what the bond-first sentence and the fixes add, now that the context no longer gives the standard away.
- **T against test 5's F (3.3 / 4.7):** this shows whether the order still surprises when it is not stated first.
- **R's reframe:** it has not been read cold before. Watch whether readers take "passes the usual reading of 'high'" as the team excusing the first plan or as the price of the step.
- **L and M side by side:** read whether either is marked a repeat of the other. M ends on the range's two figures, and J opens straight after.

## Checks made for this pack

- **One item per file:** each reader file holds one item, its eight questions, and a pointer to the next file only.
- **Text checks, on the items and the context:**
  - No question marks.
  - No em or en dashes and no curly quotes (Python check over the packs and this folder).
  - None of "optimal", "natural hedge", CPPI, "portfolio insurance", "capital-protected", "full funding", "prudent", "fail-safe", "secured", "endowment", "cushion", "barring a US default", "in her name", "ended on schedule", TIPS or STRIPS.
  - "Certain" appears in items only as "the range she states, once both ends are owned, is certain" (M). Elsewhere it is the case's phrase or the 0-100 anchor.
  - No iBond fund payout is called fixed.
  - J.P. Morgan's 7.5% is never "the top" or "the consensus".
- **The context** does not hold "even if cash waiting earns nothing", any order of the 2028 deposit or any first-dollars figure.
- **W** is identical to test 5's item B (diff).
- **Arithmetic:**
  - 59.7% = 1 - 60,393 / 150,000;
  - 96.8 = 100 - 3.2265;
  - $37,625 = $325,563 - $287,938;
  - 26.1% = 39,162 / 150,000.

## Limits and open items

- **The refrain still repeats.** "Even if cash waiting earns nothing" appears in K, T, R and W:
  - W carries it because it is the unchanged control;
  - K holds it in full, which is its home in 3a;
  - T and R need it to state the standard.
  - Expect a repeat flag. If one comes, the report says it in full once (3a) and points back elsewhere.
- **Recall is asked only at the end**, as in test 5. Items read last are recalled more easily, so the recall is read against each item's position.
- **One-file release cannot be enforced.** The brief tells each reader to write an answer before opening the next file, never to open a later file early, never to go back, and never to open any other file. A flag that cites a later item is read as a breach.
- **Wording to watch in K:** "as the plan's own waiting cash would be" is test 5's E3 wording. The plan's waiting cash sits in a Treasury-bill fund of 0-3 month bills (NUMBERS 0), not in six-month bills. If a reader flags it, say "in Treasury bills, where the plan's own waiting cash would sit".
- **R's price clause is from the 27 Sep model.** Caplet's own plan gives up about $65,000 at the median on today's engine (8s). That figure is Keel arithmetic, not yet in `first_plan.py`, and stays an open item for the numbers owner.
- **Simulated readers.** Recall after the filler task is only what each reader reports, never a measure of human memory.
