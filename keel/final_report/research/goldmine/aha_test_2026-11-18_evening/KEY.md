# Cold aha test 7, Wed 18 Nov 2026 (evening): the key (Keel only; the brief tells readers never to open this file)

Notes for the Final Report store, not report prose. Built Wed 18 Nov 19:30 AEDT to `../aha_test_2026-11-18/RESULTS.md`,
"Test 7 (recommended)", and to the lead's brief for tonight: spine row 10 with the 1-in-20 low beside the $19,000 (never
$19,000 alone as the price of "none"); the order of purchase with its wrong "and then the shares" fixed (the rest of the
2028 deposit is split, not ordered after the bottom's fund); the comfort letter head to head with spine row 8 for 3d;
spine row 6's "same 1-in-20 low" given its reason or dropped; new candidates from `../AHA_REGISTER_candidates.md`; one
control repeated word for word; at most eight items.

**What this test carries and what it leaves out.** Test 6's RESULTS asked for nine items (the comfort letter, row 8,
rows 1, 6, 10, 5 cut, 7, the order of purchase, and row 3 as the control), and the lead asked for new candidates within
eight. Two of the nine wait:

- **Row 5 (test 6's K)** is kept as it stands (3.0 / 4.3; the bond confirmed as its first sentence). Its open fixes are a
  density cut that SKELETON 3a's owner decides (room for the bond's two rates), not a reading question.
- **Row 7 (test 6's L)** is kept (3.0 / 4.0). Its one change that needs a reader, the join with row 1's 57 in 100, is
  carried in item A's last sentence.
- **Row 1 stays in** although the lead's list did not name it: "why a range" was asked by all three readers for the
  third test running, and register row 1 sets the trigger ("retest in test 7, and if it is still asked the lead weighs
  NUMBERS 4's framing D").
- **One new candidate fits: Florida's prepaid plan (item E, 3a).** It is the highest-rated of the seven Wed 18 Nov
  candidates (Q126-036, 24) and is verified at source. The other six wait, each for a reason given under "Next in line".

**Where things are.** Everything is in this folder:

- `BRIEF_READER.md`: the readers' brief. It names only itself, the reader's own pack and the reader's answer file.
- `packs/X/01.md` to `08.md`, `packs/Y/...`, `packs/N/...`: one item and its eight questions per file, in each reader's
  order.
- `ITEMS.md`: the record copy of all eight items in letter order.
- The answer files the readers write: `READER_X.md`, `READER_Y.md`, `READER_N.md`.
- The packs and `ITEMS.md` are built by one script from one source of text:
  `/tmp/claude-0/-home-user/cdd961e4-901c-5589-a829-32f064718722/scratchpad/aha7_build/build.py`, with orders from
  `orders.py` beside it. Both sit outside the repo; the control's text and the context are read from test 6's build
  script, so neither can drift.

**The readers** are three simulated model readers, never people. The roles are test 6's, so scores compare across tests 6
and 7:

| Reader | Role |
|---|---|
| X | Investment professional who builds Treasury portfolios for institutions |
| Y | Finance professor who teaches fixed income |
| N | Finance director of a mid-sized nonprofit arts organisation |

Their scores and recall say how the words read and which figure stands out, never how people remember (standing order
22).

## Which letter is which

Every plan figure comes from `../../../NUMBERS.md` as it stands on Wed 18 Nov evening: the Tue 17 Nov evening re-size,
plus 8u and 8v, added Wed 18 Nov morning, and the block added beside 8q this evening (card Q131, uncommitted when this
test was built). None of the three moves an existing figure.

| Letter | Internal key | Register row | Status | Part and Wharton's job | Last read cold |
|---|---|---|---|---|---|
| A | R1 | Spine row 1 (Neyman) | Fixed: test 6's M fixes 1-3, 5 and 6, with the case's form said | 3c: the range's confidence | Test 6: 4.0 / 3.3 |
| B | OP | Reserve: the order of purchase (GOLDMINE #39) | Fixed: test 6's T fixes 1-4 | 2.3 or 3e: the 2028 deposit as the one input not owned | Test 6: 3.0 / 4.3 |
| C | J7 | Reserve: the comfort letter | Fixed: test 6's J fixes 1-5, plus the chronology | 3d: why the co-sponsor words will be believed (head to head with V) | Test 6: 3.0 / 4.0 |
| D | R6 | Spine row 6 | Fixed: test 6's P fixes 1-7 (the same 1-in-20 low kept, with its reason) | 3b: the split of the building money, tested from both sides | Test 6: 3.7 / 3.0 |
| E | FL | New candidate: Florida's prepaid plan (Q126-036, with Q126-037) | First cold read | 3a: why the payments are owned in Treasuries, IPS l.11's rule in an institution's words | Never |
| F | R3 | Spine row 3 | **Control**: test 6's item W (test 5's item B), word for word (checked by script); only its letter changes | 2.5: what really set the cost | Test 6: 3.3 / 4.0; test 5: 4.0 / 4.0 |
| U | R10 | Spine row 10, version B as reframed Tue 17 Nov evening | Fixed: test 6's R fixes 2-4 and 6, and the price clause in Keel's form | 3f, Team Reflection: thinking that changed | Test 6: 3.7 / 4.0 |
| V | R8 | Spine row 8 | Fixed: cold test 2's fixes | 3d: why the co-sponsor words will be believed (head to head with C) | Test 2: 3.3 (aha strength only) |

Letters were drawn by `random.Random(20261120)` from A-H, Q, S, U and V. The draw left out test 6's eight letters, the
reader letters N, X, Y and Z, and I and O.

### Sources, item by item

**A (row 1).**

- The case's form: case l.114-118 ("Rather than promising one exact amount, she wants to communicate a credible range";
  teams "state how confident they are that her 2033 contribution will fall within that range").
- The top as her contribution and the figure co-sponsors count, the bottom as the part owned since January 2028:
  `../../meta/WHY_A_RANGE_2026-11-16.md`, option (b) and 4a-4b.
- Neyman 1937, zero or one: card Q74 row 2 (p. 349).
- 59% of 118 researchers: card Q74 row 7 (Hoekstra et al. 2014).
- The range rule (fees, the 0.5% margin, whole $5,000 steps rounded down): NUMBERS 3 and 4; WORDS l.33-34.
- "The room under the top" (the margin plus the rounding, about 2%, 2.32%): NUMBERS 3, bond desk 4's check figures; 8u;
  WORDS l.35 ("the margin" is the 0.5% alone).
- At most about $120 per further 0.1%: NUMBERS 3 ($118, "a ceiling on the slope").
- 91 and 57 in 100 at 7.5%: NUMBERS 4, the odds table (91.2%, 57.2%).
- "Which forecast ... barely moves today's estimate of the top" rests on NUMBERS 4's 4%-10% table (unrounded $115,296 to
  $118,537, stated $115,000 throughout) and 8p (13 of 15 houses give $115,000).
  - 8v adds the honest edge: from yield, growth and valuation about 5% a year, still $115,000; at 3.1%, $110,000. So
    "barely", never "does not move".

**B (order of purchase).**

- The premise: IPS l.9.
- About $39,000: NUMBERS 5 ($39,162).
- The split, "the fund always taking the larger part" (Keel's reading of "most", NUMBERS 4; true at every deposit in
  NUMBERS 5's table):
  - $150,000 deposit: floor $81,244, VT $29,594;
  - $112,500: floor $56,251, VT $17,087;
  - $75,000: the floor takes all of what is left, VT $0.
- 73.9% "on the market close of 6 November 2026": NUMBERS 5 and 8u (8u's rule: "about three-quarters" only at today's
  rates, the curve's date beside the figure).
- About $60,000 and about 60%: NUMBERS 5 (b), $60,393; Keel arithmetic 59.7%.
- $112,500: the bottom from $95,000 to $65,000, and the shares from about $30,000 to about $17,000 (NUMBERS 5 table).
- The missed deposit:
  - $57,455 at 0%, added across the ten dates: NUMBERS 5, 8s and 8u;
  - $3,016 in the 2033 payment at today's market rates, never quoted alone: NUMBERS 5;
  - "leaves nothing for the building, which she would know three years before the meetings": NUMBERS 5;
  - "one of the plan's two named reasons": IPS l.17.
- "Yields often fall in a slump": NUMBERS 7; CANON D8.
- No rule added: CANON A34, D9.

**C (comfort letter).**

- The case:
  - card Q99 row 1: the letter's sentence; the Court of Appeal, 2 Feb 1989; Hirst J's £12.26m with interest;
  - row 4: the tin collapse of October 1985 and the telex of 3 Dec 1985;
  - row 36: Laura's words as a fact plus a promise;
  - row 4's guard: never that her words bind her.
- The written form funders count, a signed letter naming the facility: card Q99 rows 18 and 34-35; WHY_A_RANGE 4c;
  SKELETON 3d.
- A broker statement shows the funds held and their end dates, not the counted figure: test 6 J flag 1. That a 2031
  statement shows less than the counted figure while rates are above zero is Keel inference, not in NUMBERS, and is not
  printed.
- $115,000 and January 2028: NUMBERS 4.
- Late 2032: NUMBERS 4 (the floor and the moved shares pay in mid-December 2032).
- Counted at what the funds pay if cash waiting earns nothing, after fees and the 0.5% margin: NUMBERS 3 and 4, the range
  rule.

**D (row 6).**

- The half promised to no one and its three uses, in the IPS's order: IPS l.15; WORDS l.28.
- $110,000 with the same flexibility held back (the median half kept, $20,486, "about $20,000"): NUMBERS 4, C8.
- $115,000 central top: NUMBERS 4.
- $130,000, one figure: C8; 8n option A.
- Less in all in about 63 futures in 100 (62.8%), with a median difference of about $4,000 over all futures: C8; 8n's
  "Against the plan, future by future" (A: 37%, -$4,000).
- About the same at the 1-in-20 low: C8 ($112,375 against $112,035) and 8n (all money $159,000 each).
  - The reason, that the all-Treasury figure moves with yields to January 2028 ($112,035 / $139,541 / $168,598), is from
    C8.
  - The plan's low comes from shares and yields together: the house model (NUMBERS 7).
- "Most of the 2028 deposit, at today's rates": NUMBERS 4 (54.2%); WORDS, numbers in prose.
- 75% in shares, a $30,000 bottom: 8n option D.

**E (Florida's prepaid plan; new).** Card Q126:

- the shape (a fixed promise, money invested partly in shares): claim 1, as the card words it, never "the institutional
  version of our first plan";
- Alabama's 72% share target: row 3;
- 97.6% (Sep 2007) and 62.3% (Sep 2009): row 5;
- tuition rising in the same years: row 8;
- the 2011 settlement at Fall 2010 tuition, families paying any difference: rows 13-14 (board-approved rises have since
  narrowed the cut; the item says what the settlement did);
- state money:
  - Alabama $547.6m: row 10;
  - Illinois $280m: row 30;
  - Texas about $813.6m, Keel arithmetic: row 33;
  - so "from $280 million to about $814 million";
- Florida's matched bonds: row 35;
- Florida's June 2006 rule, quoted whole: row 36;
- the reserve from 12.9% to an estimated 4.9%, no promise cut: row 37;
- Laura's sentence: IPS l.11, quoted.

**F (control).** The figures are test 6's and test 5's, from NUMBERS 8e, 8b, 8g and 5, re-checked tonight:

- 731 of 6,716 days (10.9%);
- one day from June 2007 to August 2026, Thu 19 Oct 2023;
- $470,217 on 4 Aug 2020;
- 5 Oct 2026 the cheapest since 21 May 2002;
- $200 of commissions;
- $325,563 and $287,938;
- 3.57 points, "about 3.6".

**U (row 10).**

- "A high degree of certainty": the case.
- The first plan (75% shares to 2030, 40% in 2032, the ten bought on 1 Jan 2033) and its figures: NUMBERS 8s:
  - 3.2265%, 1 in 31.0;
  - US shares at 6.7% compound;
  - 5.5% at 5.0%;
  - a median miss of $27,695;
  - with a $75,000 deposit 13.693%, 1 in 7.3.
- 96.8 is Keel arithmetic (100 - 3.2265).
- The anchors: judges about 90% (card Q120 rows 1, 6), and the SEC's "reasonable certainty means a high degree of
  confidence ... If probabilistic methods are used, there should be at least a 90% probability" (row 15, 17 CFR
  210.4-10(a)(24)).
- The reason, IPS l.9, in the team's words: CANON A3. "None" from January 2028 rests on NUMBERS 2 and 8s.
- "The first quarter or so": NUMBERS 5 (26.1%); WORDS l.66 and l.74.
- None at today's rates with half the deposit: NUMBERS 5 (the standard survives a 73.9% cut); 8s (99.965% of simulated
  futures).
- The price, NUMBERS 8s, "What none cost Laura" (Keel arithmetic, MODEL):
  - at the 1-in-20 low: 27 Sep model $159,224 against $19,990; today's engine, the plan as built, $158,942 against $280
    ("almost nothing");
  - at the median: 27 Sep model $207,290 against $226,096 ($18,806, "about $19,000"); today's engine $191,066 against
    $256,543 ($65,477, "about $65,000"), "which keeps more out of shares" (8s's own reading).
- "The team's current ones (world shares at 7.5% a year)": 8s, today's engine.

**V (row 8).**

- 60 to 80%: card Q11b row 34 (AFP 2021 as summarised; Capital Campaign Pro). The advisers' word "secured" is said as
  "raised", since "secured" is banned for Laura's figure.
- MacDowell's $13 million campaign, announced in 2010 with "more than $10 million has already been raised": row 5. That
  is at least 77% in hand (Keel arithmetic, not printed).
- Set in Stone (University of Chicago Cultural Policy Center and NORC, 2012; US cultural buildings 1994-2008): theatres
  about 92% above the first budget, the publicly perceived rise about 19%, managers "were clever about when to announce
  their budgets publicly": row 26.
- "Her own share, not the building's cost": cold test 2 reader A's flag. "Held for her in Treasuries, the bottom and the
  top": NUMBERS 4 (both ends owned after the move).

**Context paragraph.** Word for word test 6's (the same script text). It gives no item's answer away: no order of the
2028 deposit, no first-part figure, no "even if cash waiting earns nothing".

## Figures changed since each item's last test

No NUMBERS figure has moved since test 6 (Wed 18 Nov morning): 8u, 8v and this evening's 8q block added figures and
moved none. Row 8's
figures are card figures, unchanged since test 2. The table lists what each item gained or lost.

| Item | Figure | Last test | This test | Source |
|---|---|---|---|---|
| A | "The two figures record how long each part has been held, not a margin for error" | In (test 6) | Out; replaced by the case's form | RESULTS test 6, M fix 2; WHY_A_RANGE 4b |
| A | "About 2%" | "at least 0.5% ... (about 2%)", then "that margin" | "the room under the top, that margin plus the rounding (about 2% ...)" | WORDS l.34-35 (coherence reader 9, H3, Wed 18 Nov) |
| B | "and then the shares" | In | Out; "split ..., the fund always taking the larger part" | NUMBERS 4, 5 |
| B | 73.9% | "(73.9%)" | "(73.9% on the market close of 6 November 2026)" | NUMBERS 5, 8u |
| B | $3,016 in the 2033 payment at today's market rates | None | Beside $57,455 | NUMBERS 5 |
| B | Shares about $30,000 to about $17,000 at a $112,500 deposit | None | Added | NUMBERS 5 ($29,594, $17,087) |
| B | "A deposit a quarter smaller" | In | "A deposit of $112,500 instead of $150,000" | WORDS l.66 (one phrase, one quantity) |
| C | 0.5% margin | None | "after fees and a 0.5% margin for other fund costs" | NUMBERS 3 |
| D | $159,000 (same 1-in-20 low) | In | Out (no figure; "about the same", with its reason) | C8; 8n |
| D | 64 in 100; about 95 in 100; $9,000 against $29,000; $15,000 for $20,000 | In | Out (density, fix 7) | 8n; C8 |
| D | Median difference about $4,000 | None | Added | 8n |
| D | "About three-quarters / about a quarter" (the split) | In | "most of the 2028 deposit, at today's rates"; "75% of the building money" | WORDS l.36, l.66 |
| U | "About three-quarters of the money in shares" | In | "75% of the money in shares" | WORDS l.36 (M3) |
| U | 1 in 7 against none with half the deposit | None | Added | 8s (13.7%); NUMBERS 5 |
| U | $65,000 (today's engine, the plan as built); $280 ("almost nothing") | None | Added beside $19,000 and $20,000 | 8s |
| V | MacDowell $13 million, more than $10 million | None | Added | Card Q11b row 5 |
| V | 92% and 19% | "theatres" in a sentence on "new arts buildings" | "the theatres" in the study, with the study's own words for the cause | Card Q11b row 26 |
| F | (all) | Test 6's W | Identical | NUMBERS 8e, 8b, 8g, 5 |

## Fixes applied, and from which flag

Flag numbers are test 6's (`../aha_test_2026-11-18/RESULTS.md`) unless said otherwise.

**A (row 1).**

- **M1, a change of category (X, Y, N):** applied: "Laura's 2031 range is not an estimate at all: once half the shares
  have moved ..., both ends are Treasuries she owns, and there is nothing left to estimate."
- **M2, "why a range" (all three, third test):** the case's own form first ("a credible range rather than one exact
  amount", case l.115-116), then option (b): she states the range she owns and gives its top. The "how long each part
  has been held" sentence is out.
- **M3, "certain" first:** "is certain: each end is counted at ...", with the condition after it. The subject is the
  range she states, once both ends are owned.
- **M4, fund events:** the item claims the margin covers "other fund costs" only.
- **M5, the join with row 7:** applied as the last sentence.
- **M6, Neyman in one sentence and the 59% in a clause:** applied.

**B (order of purchase).**

- **T1, split, not ordered:** applied as "only what is left is split between the Treasury fund for the bottom of her
  range and the shares, the fund always taking the larger part". The quarter-cut example now shows both parts falling.
  RESULTS's wording ("about three-quarters and a quarter, the fund always taking more than half the deposit") is not
  used, for two reasons:
  - WORDS keeps "about three-quarters" for the deposit cut in any part that prints it, and "about a quarter" for the first
    $39,162 alone;
  - WORDS never prints a label saying the floor's written minimum binds.
  "The larger part" is true at every deposit in NUMBERS 5's table.
- **T2, 73.9% as false precision (Y):** "about three-quarters" in the sentence, 73.9% in brackets with the curve's date.
- **T3, the basis of $57,455:** "if cash waiting earns nothing", with $3,016 at today's market rates beside it.
  - $58,775 (8u, with the short-term ETF's fee) is 3e's figure and is not used, so B compares with tests 5 and 6.
- **T4, what a missed deposit changes (X):** "and leaves nothing for the building, which she would know three years
  before the meetings".
- **T5, a late deposit:** not applied. It is not in NUMBERS (open for the numbers owner).

**C (comfort letter).**

- **J1, the broker statement:** "which a broker statement shows as the funds held and their end dates".
- **J2, "no fall in markets" against row 1's condition:** "after fees and a 0.5% margin for other fund costs, so no fall
  in markets can take it lower".
- **J3, "since" (X):** "from the time half the shares moved into Treasuries".
- **J4, what stops the fact changing:** "The promise, in a signed letter naming the facility". The last line stays: the
  fact does not bind her.
- **J5 (Y):** "the fact it gave was only an intention".
- **Beyond the flags, the chronology.** Test 6 put the High Court award before the October 1985 collapse; it came after
  it. The collapse and the telex now come first.
- "Policy" stays on Malaysia Mining's side; no conceit turn.

**D (row 6).**

- **P1, the same 1-in-20 low (X, Y):** kept, with its reason in a clause and no figure. The $159,000 is out, so D no
  longer shares a figure with U.
- **P2, medians do not add (Y):** the total on one base, "in about 63 futures in 100 (the median difference over all
  futures is about $4,000)". "$15,000 for $20,000" is out.
- **P3:** folded into P2's sentence.
- **P4 (X):** "what its Treasuries for the building pay above its top". WORDS bans "the two funds" unnamed.
- **P5 (X):** "held back as much as that unpromised half, about $20,000, in the same Treasury fund".
- **P6 (N):** the half kept is the plan's choice, with IPS l.15's three uses in its own order.
- **P7 (Y, N), density:** led with the sentence all three carried, then the all-Treasury comparison, then the more-shares
  side in one clause (the $30,000 bottom only).

**E (new).** The candidate's guards (`../AHA_REGISTER_candidates.md`):

- never "only Florida";
- the rule quoted whole, never the 15% alone;
- "a fixed promise backed by shares", never "the institutional version of our first plan" (card Q126, claim 1);
- placed in 3a, so the team's reason for its first plan stays IPS l.9's (CANON A3);
- **open before any use in the report:** confirm the rule at the Florida Prepaid College Board's own record. Card Q126
  read it in the State of Florida CAFR (2015) at source and the Board's 2012 report through a copy site.

**F (control).** No fixes, deliberately: test 5's B flags 1-6 and test 6's added flags (the window sentence in two, the
basis named, the 2027 clock) stay unapplied, so F reads against test 6's 3.3 / 4.0 and test 5's 4.0 / 4.0.

**U (row 10).**

- **R2, the SEC (Y):** as the SEC writes it: "defines reasonable certainty as 'a high degree of confidence' and, where
  probabilities are used, asks for at least 90%". The judges stay as the first anchor.
- **R3, one model's numbers:** named once ("the team's 27 September simulations, run before any trade with US shares
  growing 6.7% a year"). "5.5% if shares grew 5.0% a year" is said in words.
- **R4, the premise's own case (X, Y):** "and with half the second deposit, about 1 in 7 against none at today's rates".
  40.8% is never set against none.
- **The price clause in Keel's form (RESULTS; the lead's brief):** the low first, which both models agree on. At the
  median each model gives its own figure: the 27 Sep $19,000, and $65,000 for the plan as built. Never $19,000 alone.
- **R6:** U's $159,000 carries its two models; D prints no $159,000.
- **WORDS M3:** "75% of the money in shares", never "three-quarters", since B prints "about three-quarters smaller".

**V (row 8), with cold test 2's fixes (`../aha_test_2026-11-16b/RESULTS.md`) and the register's.**

- **92% is theatres (B):** said as "the theatres" of the study. Card Q51 (Mon 16 Nov) gave no announced-against-final
  pair for small arts buildings, so the theatres' pair stays, named.
  - The register's "the costliest kind" is not printed: no row in cards Q11b, Q51 or Q5d sources it.
- **The campaign contrast only:** row 4's principle is not restated as a rule.
- **One donor's share against a campaign's whole goal (reader A):** "Laura's figure is her own share of the building, not
  its cost, and co-sponsors still raise theirs."
- **Cause stated as settled (reader A):** now "which the study put down to managers who 'were clever about when to
  announce ...'".
- **3d must not contradict 3e:** V claims nothing about her flexibility against an overrun of that size.
- **MacDowell added:** a residency's own launch at at least 77%.

## Orders and seed

- **Method** (`orders.py`, outside the repo):
  1. All 8! orders were filtered by the constraints below, which left 1,176 valid orders.
  2. They were shuffled with `random.Random(20261119)`.
  3. The first triple by `itertools.combinations` was taken (shuffled indices 0, 1, 21), with every item in a different
     position for each reader, at least one order with F before B and one with B before F, and at least one with C
     before V and one with V before C.
- **Constraints:**
  - A is read before C and V in every order, so "why a range" is read before either 3d item answers part of it.
  - These pairs are never adjacent:
    - C with V (the head to head);
    - C with A (test 6's J and M clash);
    - A with V;
    - B with U, B with D and B with F (the deposit's first part, the split, and the control's last sentence);
    - E with U (share-led fixed promises against Treasuries first);
    - D with U (shares against Treasuries for the building).

| Reader | Order (letters) | Files |
|---|---|---|
| X | B, A, F, C, E, D, V, U | `packs/X/01.md` ... `08.md` |
| Y | D, F, A, E, V, U, C, B | `packs/Y/01.md` ... `08.md` |
| N | A, D, V, F, U, C, B, E | `packs/N/01.md` ... `08.md` |

| Letter | X | Y | N |
|---|---|---|---|
| A | 2 | 3 | 1 |
| B | 1 | 8 | 7 |
| C | 4 | 7 | 6 |
| D | 6 | 1 | 2 |
| E | 5 | 4 | 8 |
| F | 3 | 2 | 4 |
| U | 8 | 6 | 5 |
| V | 7 | 5 | 3 |

- **The control and the order effect.** X reads B (the order of purchase) before F, as every reader did in test 6; Y and
  N read F before B.
- **The head to head.** X reads C first (C 4th, V 7th); Y and N read V first (Y: V 5th, C 7th; N: V 3rd, C 6th).

## Scoring key: the figure each reader should recall

Fields are as in test 6: surprise 1-5 with the old "aha strength" anchors, conviction 1-5, the prior and how sure
(0-100), the figure recalled from memory after the filler task, repeat tomorrow, three after 40 reports, and clashes.
Scores are read by role and never pooled as one audience.

| Item | Key figure | Also accept |
|---|---|---|
| A | Zero or one: the range is not an estimate once both ends are owned | 1937; 59% of 118 researchers; 0.5%; about 2%; about $120 per 0.1%; $5,000 steps; 7.5%; 91 in 100; 57 in 100; January 2028 |
| B | About three-quarters smaller (73.9%) | about $39,000; about $60,000 or about 60%; $112,500; $95,000 to $65,000; about $30,000 to about $17,000; $57,455; $3,016; three years |
| C | $115,000 held for her in Treasury funds (the fact behind the promise) | "a statement of present fact and not a promise as to future conduct"; £12.26m; October 1985; 1989; January 2028; late 2032; 0.5% |
| D | $110,000 with the same flexibility held back, against the plan's $115,000 | $20,000; $130,000; 63 in 100; about $4,000; 75%; $30,000; $95,000 |
| E | "The lesser of 15% of the total fund, or the actuarial reserve" | 15%; June 2006; 12.9% to 4.9%; 72%; 97.6% and 62.3%; Fall 2010; $280 million to about $814 million |
| F | One day from June 2007 to August 2026 (19 October 2023) | 10.9% of days since 2000; $470,217; $200 against $37,625; $325,563 and $287,938; May 2002; 3.6 points |
| U | About 1 in 31 against none | 96.8 in 100; about 90%; 6.7%; 5.5% at 5.0%; $27,695; 1 in 7; the first quarter or so; $159,000 against $20,000; $19,000; $65,000 |
| V | 100% held when she names it, against 60 to 80% raised when a campaign is announced | 92% and 19%; 1994-2008; $13 million and $10 million; MacDowell; 2010 |

## What to read beside the scores

- **The control.** F scored 3.3 / 4.0 in test 6 and 4.0 / 4.0 in test 5.
  - If Y and N, who read F before B, give 4 on surprise and X gives 3, test 6's drop was the order.
  - If all three give 3, the one-file panel runs lower, and the other items read against that.
- **C against V for 3d.** Compare surprise, conviction, listings after 40, recall and repeat-tomorrow. V has never been
  scored for conviction.
  - The one that wins on conviction and listings is first for 3d; the other is a clause or the store.
  - Read each against its position (C 4th, 7th, 6th; V 7th, 5th, 3rd).
- **A and "why a range".** Count the readers who still ask it, in A or anywhere. If two or more do, the lead weighs
  NUMBERS 4's framing D, the plain figure (register row 1).
- **D's conviction** against test 6's 3.0: do X and Y now believe "about the same at the 1-in-20 low" with its reason?
  If not, the clause goes.
- **U's price.** Does any reader carry $19,000 alone as what the plan cost, and does conviction hold at test 6's 4.0 with
  $65,000 beside it?
- **B.** Has the split clash with D gone (test 6's N)? Surprise and conviction against test 6's 3.0 / 4.3.
- **E against row 5.** Row 5 is 3a's spine row (test 6: 3.0 / 4.3). A candidate takes no spine slot before a second
  cold read.

## Checks made for this pack

- **One item per file** (script): each pack file holds one `**Item` line, its eight questions and a pointer to the next
  file only.
- **The control** is identical to test 6's W (script, whitespace-normalised).
- **Text checks on the items, the packs and the context:**
  - no question marks; no em or en dashes; no curly quotes (the only non-ASCII character is £);
  - none of: "optimal", "natural hedge", CPPI, "portfolio insurance", "capital-protected", "full funding", "prudent",
    "fail-safe", "secured", "endowment", "cushion", "barring a US default", "in her name", "ended on schedule", TIPS,
    STRIPS, "building blocks", "led lately", "upper third", "the consensus", "only two things", "hedge", "backstop",
    "paths", "forward rates", "guarantee", "the two funds", "about a quarter", "IPS", "Caplet" or "Keel" (the brief's
    folder path holds the repo's name and nothing else);
  - "certain" appears in items only with the range she states, once both ends are owned, as its subject (A);
    "certainty" appears only in the case's phrase and the SEC's "reasonable certainty" (U).
- **No banned framing:**
  - J.P. Morgan is not named, and 7.5% appears only as "world shares assumed to earn 7.5% a year" (A) and "world shares
    at 7.5% a year" (U), never as the top or the consensus;
  - world shares bought in January 2000 do not appear;
  - nothing says "only two things can break the plan" or that 3.2% fails "high".
- **Arithmetic:**
  - 96.8 = 100 - 3.2265;
  - $65,477 = $256,543 - $191,066;
  - $18,806 = $226,096 - $207,290;
  - 26.1% = 39,162 / 150,000;
  - 59.7% = 1 - 60,393 / 150,000;
  - $37,625 = $325,563 - $287,938;
  - 2.32% = 1 - 115,000 / 117,731;
  - Texas $813.7m = 87.7 + 211.0 + 271.2 + 243.8 (the card's $813.6m uses the exact 2021 figure).

## Next in line: the new candidates not in this test

| Candidate (store row) | Part | Why it waits |
|---|---|---|
| A wait for higher yields is a bet against today's market rates; a date takes no bet (Q125-011, Q125-004; 22) | 3a | E takes 3a's one new slot; first for the next test |
| The aircraft lessor's reserve against Laura's (Q133-002; 20) | 3a | E takes 3a's slot |
| A publisher can promise floors because it pools thousands of books (Q127-012; 20) | 2.3 clause | B is 2.3's item in this test; a clause, never "her bottom is an advance" |
| The IPCC's Chinese "unlikely" as 不可能 (Q128-002, Q128-007; 20) | 3c | Guard first: the Taiwan (TCCIP) rendering of "unlikely" is unchecked; A is 3c's item |
| A stronger Taiwan dollar came with dearer building, a median 22.3% (Q131-015, Q131-014; 20) | 3b; Table 3 row 7 | Its guard is now met: the figures were entered beside 8q on Wed 18 Nov evening, while this test was built (22.3% in 30 strong windows of 406; the need at the median, $25,607 on the top, leaves $3,075). It waits only because D holds 3b's slot here; it is first for the next 3b or 3e test, never "offset" or "a natural hedge" |
| Accident investigators drop the single cause (Q130-012; 19) | 3e | Lowest rated; best read beside 8u in a 3e test, never "only two things can break the plan" |

## Limits and open items

- **The packs sit inside the repo**, beside `ITEMS.md` and this file; test 6's sat outside it. The brief names only
  itself, the reader's pack and the answer file, and forbids listing or opening anything else.
  - Read as a breach: an answer that cites a letter not yet read, a register term (spine, reserve, row, card), a source
    the items do not give, or another reader's answers.
  - The folder's name says "aha test", as test 6's scratch folder did.
- **Recall is asked only at the end.** U is read last by X and E last by N; read recall against position.
- **Three readers cannot balance the head to head.** One reads C first, two read V first.
- **One new candidate only.** E is a first read and takes no spine slot from it.
- **Open for owners:**
  - E's rule confirmed at the Florida Prepaid College Board's own record (research);
  - what a late deposit costs (numbers owner; B's flag 5);
  - `first_plan.py` to carry today's engine's $65,000 and $280 (numbers owner; they are Keel arithmetic written in 8s);
  - room for the bond's two rates in 3a (SKELETON 3a's owner; row 5, not in this test).
- **Simulated readers.** Recall after the filler task is only what each reader reports, never a measure of human memory
  (standing order 22).
