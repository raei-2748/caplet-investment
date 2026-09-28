# D9 Communication Analyst: can each idea be said plainly in the notes, the 50-word pitch and the 500-word IPS?

Agent D9, insight_v1 run, Phase D. Written 2026-09-28. Questions M001, M071, M143, M241, M031, M062, M226, M012,
M036, M121, M191, M212 (`research/insight_v1/phase_C/survivors.json`), worked in deadline order.

This is AI-generated research for Team Caplet: specifications, evidence, numbers and checklists. **None of it is text
to submit.** The six students choose and write every word of every WInS note, reflection, pitch and IPS, and record AI
use in the Final Report's Works Cited (R-W46). Nothing here is for the finale. Laura appears only through the case and
her public professional record. Nothing here suggests contacting her.

**Scope (brief section 17).** Only WInS trading (as the source of Trading Notes), the Trading Notes Analysis (TN,
Oct 23) and the IPS (Nov 6) are in scope. Two questions (M031, and the table part of M212) are purely Final Report.
They get one line each in "Later (after Nov 9)". The IPS-relevant part of M191 is kept as an IPS rule.

Scripts (run from the repo root; each docstring lists inputs and status labels):
- `.venv/bin/python research/insight_v1/scripts/D9_numbers.py` covers the vocabulary counts, the horizon odds, the
  price sensitivity with a live curve re-price, the trade-off costs and the independence odds.
- `.venv/bin/python research/insight_v1/scripts/D9_ips_page_fit.py [--draft file]` checks whether pitch + IPS fit on
  two pages.
- `.venv/bin/python research/insight_v1/scripts/D9_draft_checker.py --kind note|reflection|pitch|ips file` (or
  `--demo`) mechanically checks the team's own drafts. It counts words and flags them; it never rewrites anything.

Status labels: **VP** = VERIFIED-PRIMARY (read by D9 on the primary page, 2026-09-28, with `fetch_text.py --grep`,
phrase found verbatim). **VRF** = VERIFIED-REPO-FILE. **DER** = derived by a D9 script from labelled inputs. **ASM** =
ASSUMPTION. **SNIP** = SNIPPET-UNVERIFIED. **INT** = D9's interpretation (a judgement, not a fact). **CITED** = taken
from another agent's file and not re-read by D9 (the file is named).

---

## Summary: top findings, ranked by impact on reaching the semifinals and on making the plan unmistakably Laura's

1. **(IPS compliance, tier 2; new) A full 50 + 500 words may not fit on two pages, and overflowing is an exclusion
   risk.**
   - Microsoft Word's "Double" spacing for Times New Roman 12 is 27.6 pt, because the font's line height is 1.15 em.
   - At that spacing, US Letter with 1-inch margins holds 23 lines a page, 46 on pages 2-3.
   - A full 50-word pitch plus 500-word IPS, laid out like Wharton's sample, needs about 44-46 lines. That leaves 0-2
     spare. The largest IPS that still fits is about 525 words, and longer words shrink it.
   - A4 holds 50 lines (2-4 spare). Wharton's own sample uses a tighter 24 pt pitch, which would leave 8-10 spare.
   - The rule is "2-page maximum", and breaking a format rule means "will not be considered for semifinal
     selection" (IPS guide L82-83, L103-109, VRF).
   - Paper size is not specified. "Formatting choices not specified below are left to the team's discretion" (L101,
     VRF).
   - **Spec:** keep the IPS to about 470-490 words. Add no subtitle lines and no blank lines between paragraphs. Then
     check the exported PDF itself: the text must end on page 3. (DER, `D9_ips_page_fit.py`; line heights ASM.)
2. **(TN, tier 1) Every WInS note needs a research element, and Wharton's own example has none.**
   - The Guide asks each note to capture "the supporting research or analysis" and its "role in growth, liquidity,
     risk management, or future funding" (Guide p.3 L84-86, VRF).
   - Wharton's example note is 59 words and 413 characters. It has no number, no date and no source (DER, draft
     checker `--demo`).
   - Hundreds of teams will copy its wording. The checker's clone test flags any draft that shares several
     three-word phrases with it.
   - **Spec (M001): five elements, about 90 words or fewer.**
     1. The action, and what it is for.
     2. One Guide role word, plus the team's fixed label for that part of the portfolio.
     3. The dated Laura need it serves.
     4. One dated, checkable fact, with its source named in words.
     5. One named risk, and the rule that governs it.
   - Agree this before the first order, because notes cannot be edited (R-AN43, G-list).
3. **(TN and IPS, tier 1) One certainty vocabulary, fixed before the first note (M062).** The official files never say
   "guarantee" or "safe" (0 uses in six documents, DER). The case gives each word a different job:
   - "certainty" belongs to the ten payments (case L91, L98, L136);
   - "confident" belongs to the 2033 contribution falling within the range (L117);
   - "confidence" and "credibility" belong to the people who must trust her: co-sponsors (L114-116), and in the
     criteria, Laura herself ("recommendations that can earn her confidence", SMApply L51);
   - "reliability" is Wharton's portfolio-level word ("funding reliability", IPS guide L20, L59).

   One distinction is new. For Laura's real January 2027 bond ladder, "matched" and "locked" are true. For the WInS
   funds they are false: the funds never mature, so the notes must say "moves like" or "stands in for". Do not call
   the WInS Treasuries "the operating reserve". The case creates the reserve "at the beginning of 2033" (L94-95, VRF).
4. **(IPS, tier 2) Three questions (M241, M226 and M143) collapse into one principle, which saves words.** Risk goes
   only where two things are true: the amount can flex, and others may help. It never goes into the fixed bill that
   only her portfolio may pay.
   - The case supplies the asymmetry. Outside money may cover "any remaining facility cost", but "Teams may not rely
     on co-sponsors ... to meet this requirement" (L84-86 vs L91-92, VRF).
   - The numbers answer the "longer horizon = more stocks" reflex, which Investor.gov states (VP). Under JPM's
     assumptions, stocks end below the Treasury rate that can be locked for the same date in about 4 paths in 10, at
     6, 10 and 15 years alike (40%/39%/39%, DER, ASM lognormal).
   - The reason is that today's locked rates (5.1-5.5%) sit only 1.2-1.6 points below JPM's 6.7% stock forecast, so
     the horizon does not rescue a fixed bill.
   - The client benefit (M143) is the consequence: once the ladder is bought, the promise stops depending on her
     career income.
   - Say that benefit conditionally ("once bought", not "in January 2027"). The ladder fits under $300k in only about
     69-77% of modelled paths (DER from A2/D7/S4, ASM).
5. **(TN, tier 1) The hedge note should lead with the promise, not with volatility (M012).**
   - A 10bp move in rates changes the price of Laura's ten payments by about $2,900.
   - At 2026's realised rate volatility, the typical yearly swing is about $20,000 (DER; DV01 VRF; annualisation ASM).
   - So cash would look steady in WInS while the price of her promise moved. The Treasury funds are the low-risk
     choice *measured against the promise*, even though long bonds swing more in price than intermediate ones (TLT
     3-year standard deviation 13.74% vs IEF 6.54%, F-201/F-202, VRF).
   - **New wording point for gate box (b).** Option (iii), about 98% hedge (S3 ticket), can be described truthfully in
     one clause, because the hedge's size roughly equals the price of the payments.
   - Option (ii) puts 66% in the hedge, about $198k, against a promise that costs about $292k. Every note then needs
     one extra clause saying WInS holds the after-2028 mix scaled to $300k, or a reader sees a $94k gap.
   - That is a communication cost of (ii), not a reason to reject it.
6. **(IPS, tier 2) Numbers policy (M036): no tables, and three kinds of number.**
   - Case facts are free, but repeating them wastes words. A past-season Wharton page says "Don't use precious space
     repeating known facts about your client and defining concepts" and "Excessive investing jargon doesn't
     necessarily dazzle the judges" (VP, retired 2023-24 page).
   - Rule parameters are what make the frozen IPS testable later. Examples: the stock share of the growth money and
     its band, the 2031 lock share, and how the 2033 split is decided.
   - Computed results are optional; use at most one, rounded and dated.
   - Use no tables and no bullet lists of numbers. Tables are not named in the ban (L123), but the sample is plain
     paragraphs and the penalty is exclusion (INT).
7. **(IPS, tier 2) Name three trade-offs, each with what Laura gives up (M121).** The Guide p.5 and the Infographic
   both say strong teams explain "reasoning, assumptions, and tradeoffs" (VRF).
   - **T1, certainty vs size.** She gives up about $19k of median 2033 surplus and about $267k of best-case (p95)
     upside. She gains +$139k in the worst 5% of paths. It removes a 3.2% chance of missing a payment (13.7% if the
     2028 deposit is halved).
   - **T2, a 2031 promise vs more growth.** Each 10 points of lock share moves about $20k into the bought floor (D5).
   - **T3, buy all at once vs gradually.** A 100bp fall before purchase costs +$30.6k; a 100bp rise saves $27.4k.
     Waiting is a rate bet.
   - In the IPS, state these without the numbers. The numbers wait for the Final Report.
8. **(IPS, tier 2) Laura in the IPS (M071).** Put her inside the rules as "because" clauses, not in a biography
   paragraph. Use case facts only. Every Laura clause must change a decision (the swap test: if the sentence still
   works with any client's name in it, cut it). Use no quotes (D13 rule; the IPS bans citations).
   - As guidance only, this comes to roughly 40-60 of the 500 words, spread across the rules.
   - The strongest case facts: the 2028 money is career income; the payments are fixed dollars that only her
     portfolio may pay; the co-sponsor promise is about credibility; her statistics degree (used once).
9. **(IPS, tier 2) The confidence method is an IPS rule; the numbers are Final Report (M191).**
   - The IPCC note the question cites advises reporting both sides of a chance to avoid framing bias. It also says
     overwhelming evidence can be stated "as statements of fact without using uncertainty qualifiers" (VP). The
     question's reading (split the two tails) is a stretch, but the core idea survives.
   - Applied here, the bottom of the 2031 range is already bought, so state it as a fact. Only the top needs a stated
     chance.
   - The IPS fixes this method; D5 owns the numbers.
10. **(Tier 1) M212's traceability table is Final Report, but its raw material starts now.** Give the decision log one
    row per trade with the same five fields as the note template (finding 2), plus the provisional rule name the IPS
    will use. The Final Report table is then a copy-out job (later list).

**North Star (INT).** The plan becomes Laura's in words when every sentence answers her question: which of my dated
needs does this serve, and what does it cost me? Generic teams write about the portfolio. Ours writes about her
calendar.

---

## Terms used in this file (plain English)

- **Hedge / "promise money":** the Treasury funds whose value moves like the price of Laura's ten $50,000 payments
  (2033-2042).
- **Ladder:** real Treasury bonds bought in January 2027, one maturing just before each payment. They are "matched" by
  date; WInS funds are not.
- **Growth money ("sleeve"):** everything the payments do not need. It funds the facility contribution and flexibility.
- **Basis point (bp):** 0.01 percentage point. **DV01:** dollars of value change per 1bp move in rates ($289 for the
  ten payments).
- **Floor (2031):** the part of the growth money bought in 2031 as a 2-year Treasury, so the bottom of the co-sponsor
  range is already owned.
- **Percentile (p5/p50/p95):** in a simulation, the bad-case, middle and good-case results.
- **Swap test (D13c):** replace "Laura" with any client's name. If the sentence still works, it is generic and should
  go.

---

## TIER 1: WInS now and the Trading Notes (Oct 23)

### M001: one note template from the first trade

**Question.** Should every WInS note open with a one-line purpose, use the Guide's role words and fixed team labels,
tie itself to one dated cash flow, and carry one dated checkable fact and one named risk?

**One-sentence answer.** Yes, with one adjustment. Five elements, about 90 words or fewer, agreed before the first
order. The research element is the one most teams (and Wharton's own example) will miss. The role word should come
from the Guide's list and be paired with one fixed team label that never changes.

**Evidence**

| Claim | Source | Status |
|---|---|---|
| A note should capture "the reasoning behind the decision, including its alignment with your strategy, the supporting research or analysis, and its expected role in growth, liquidity, risk management, or future funding." | `2026_WGY_Investment_Competition_Guide.txt` p.3 L84-86 | VRF |
| Notes are quoted "exactly as it appears in WInS"; "Yes, we will verify this." | TN guide L44, L53 | VRF |
| Wharton's example is 59 words / 413 characters, has zero digits, no date and no source; it uses the role word "growth" and "reliable future cash flows" | `D9_draft_checker.py --demo` on TN guide L36-39 | DER |
| Notes cannot be edited, only added to | 2026-27 WInS User Guide via A4 (`wins_week1_guardrails.md`, R-AN43) | CITED (A4, VP there) |
| No note character limit is published | A4 section b4; ticket check 7 | CITED |
| The reflection limit (100 words) applies to the reflection; the note is included separately | TN guide L42-46 | VRF |
| Blueprint 01 section 3 lists action, role, reason now and risk; it lacks the "supporting research" element | `research/blueprints/01_trading_notes_blueprint.md` L30-36 | VRF |

**The note spec (elements only; the team writes the words)**

| # | Element | What it must contain | What to avoid |
|---|---|---|---|
| 1 | Action + purpose | buy/sell, instrument type and ticker, rough share of the $300,000, and in the same line what the position is for | starting with the market ("rates rose, so...") |
| 2 | Role | one Guide word (growth / liquidity / risk management / future funding) and the team's fixed label (table below) | switching labels between notes ("hedge", "safe bucket", "reserve", "ladder" read as four strategies, B7b-07) |
| 3 | Laura's dated need | one of: the ten $50,000 payments 2033-2042; the facility contribution in 2033; the amount she can tell co-sponsors in 2031 | generic "diversification" or "long-term growth" |
| 4 | One dated, checkable fact | e.g. the price of the ten payments at that date's Treasury prices (`D9_numbers.py` section [3] re-prices on the latest treasury.gov date), or a fund's duration from the issuer page with its "as of" date; source named in words, not a link | more than one number; undated numbers; forecasts presented as facts |
| 5 | Named risk + rule | the main risk accepted, and the pre-set rule that governs it (e.g. never sell the hedge after a rate rise) | "stable", "safe", "guaranteed" (M062) |

- Length: aim for about 60-90 words and at most about 600 characters. (ASM: no limit is published. Paste the text into
  the WInS field before submitting and check that nothing is cut off.)
- Run `D9_draft_checker.py --kind note` on each draft. It flags overclaim words, missing role words, missing Laura
  anchors and closeness to Wharton's example.

**Fixed labels (one per part of the portfolio; decide once, before trade 1)**

| Team label (INT: proposal, the team may rename) | Guide role word(s) | Laura need | Certainty word it may use (M062) |
|---|---|---|---|
| promise money (IEF, TLH / SPTL) | future funding; risk management | ten $50,000 payments, 2033-2042 | "moves like the price of her payments", "stands in for the bonds she buys in January 2027" |
| growth money (VT) | growth | facility contribution 2033; flexibility | "expected", never "will" |
| short-Treasury part of the growth money (VGSH) | liquidity; future funding | the amount she can promise co-sponsors in 2031 | "already owned" |
| cash float | liquidity | commissions; no margin | none |

**Implication.** *Sentence-level spec for every WInS note from the first trade (WInS-now → TN).* Update blueprint 01
section 3 by adding element 4 (research) and the fixed-label table. Tick gate box (d) in the wins_now ticket only once
the note passes the checker and a second student has read it.
- Deadline tier 1. Confidence: high.
- Changes the strategy? No; this is a communication spec.
- Criterion: Articulation of Competition Experience ("clearly explains the team's research and decision-making
  process").

**What this teaches.** A good record of a decision says why, for whom, on what evidence and at what risk, and it says
so before the outcome is known. Evidence written down after the result is not evidence.

---

### M062: one certainty vocabulary before more notes are saved

**Question.** Should the team fix one certainty vocabulary and tie "certainty", "confidence" and "reliability" to one
object each, so that no note says "guaranteed" or "safe"?

**One-sentence answer.** Yes. The official documents already assign each word to a different object, and never use
"guarantee" or "safe". The team should copy that mapping and add one distinction the documents do not need: the
difference between the WInS stand-in and Laura's real ladder.

**Evidence (DER from `D9_numbers.py` [1], all six official files, VRF)**

| Word | Where the official files use it | Object |
|---|---|---|
| certainty (4 in the case, 1 in the IPS guide, 1 in the Guide) | "funded ... with a high degree of certainty" (case L91); "define what they consider a high degree of funding certainty" (L97-98); "Supports the ten-year operating commitment with a high degree of certainty" (L136); "desired degree of funding certainty" (IPS L10) | **the ten payments** |
| confident / confidence (3 in the case, 1 on SMApply) | "state how confident they are that her 2033 contribution will fall within that range" (L117-118) | **the 2033 facility range** (a stated chance) |
| | "lose the confidence or participation of co-sponsors" (L114-115); "recommendations that can earn her confidence" (SMApply L51) | **people's trust** (co-sponsors; Laura) |
| | "funding confidence" in the list of things teams "may reach different conclusions about" (L126-127) | ambiguous (INT: best read as the facility side, since the payments' level is fixed at "high") |
| reliability / reliable (1 case, 2 IPS guide, 2 TN guide, 4 Guide) | "funding reliability" (IPS L20, L59; TN L5; Guide L104, L144, L173); "reliable support for its early operations" (case L83) | **the portfolio's ability to meet its commitments** (Wharton's umbrella word) |
| credible / credibility (3 in the case, 1 on SMApply) | "damage her credibility" (L114); "a credible range" (L116); "clearly and credibly" (L143) | **Laura's standing with co-sponsors** |
| guarantee / safe | 0 uses in all six files | none; a note that uses them introduces words Wharton never used |

**The vocabulary (spec)**

| Object | Say | Never say | Why |
|---|---|---|---|
| Ten payments, real plan (from January 2027) | bought; locked in at market prices; matched by date; "certain in U.S. dollars, barring a U.S. government default" (chair memo section 4) | guaranteed; risk-free; 100%; "95% certain" | a model percentage for the payments would tell a statistics graduate we read the case carelessly (B1a-11) |
| Payments, WInS stand-in (now) | moves like the price of her payments; stands in for the ladder | matches; locked; mature when she pays; stable; reduces volatility | the funds never mature; three-quarters of TLH matures after 2042 (S3 ticket, red-team fix 2) |
| 2033 facility range | expected; a stated chance with its model named; bottom "already set aside" once bought (BS-05) | promised (for the upside); guaranteed | the case wants a "credible range", and overpromising damages credibility (L114-116) |
| Whole portfolio | funding reliability (Wharton's word) | "safe portfolio" | umbrella term only |
| People | trust; credibility | "confidence" (keep that word for the range's stated chance) | avoids one word carrying two meanings in one sentence |
| WInS Treasuries | the Treasury funds that stand in for the bonds she buys in January 2027 | "the operating reserve" | the case sets the reserve aside "At the beginning of 2033" (L94-95) |

- Evidence that precise wording protects credibility when surprises occur: Jenkins, Harris & Lark (2019), cited by B6b
  as VP (abstract). CITED, not re-read by D9.

**Implication.** *Decision: a one-page certainty glossary (WInS-now, TN, IPS)*, built from the table above. It extends
guardrail item 12, which lists strategy words but no certainty words. `D9_draft_checker.py` flags each of these words
for a second look.
- Deadline tier 1. Confidence: high.
- Changes the strategy? No.
- Criterion: Creativity and Presentation ("communicates ... investment uncertainty clearly and credibly").

**What this teaches.** Careful readers treat different words as different claims. "Certain", "confident" and
"reliable" are three promises of three strengths. Using each for exactly one thing is the cheapest way to show you read
the brief as carefully as the person who wrote it.

---

### M012: what the Treasury (hedge) note leads with

**Question.** Many teams will copy Wharton's example ("reduce portfolio volatility", "begin preparing"). What single
fact and wording should our Treasury note lead with, so that long bonds read as reducing risk to Laura's promise?

**One-sentence answer.** Lead with the promise and its price. The position holds the value of Laura's ten fixed
$50,000 payments, which cost about $X at [trade-date] Treasury prices. Name the risk that cash would leave open: each
0.1 percentage point move in rates changes that price by about $2,900. Never claim the funds are "stable" or "reduce
volatility".

**Evidence and numbers**

| Claim | Number | Source | Status |
|---|---|---|---|
| Wharton's example purpose clause | "to reduce portfolio volatility and begin preparing for Laura's future operating commitment" | TN guide L36-37 | VRF |
| Long Treasury funds are more volatile than intermediate ones | TLT 3y sd 13.74% vs IEF 6.54% | fact sheets 2026-06-30 (F-201, F-202) | VRF |
| Price of the ten payments for 2027-01-01 | $292,264 on the 2026-09-25 curve; re-priced by D9 from the live treasury.gov CSV (latest date 09/25/2026) and matching the verified script | `D9_numbers.py` [3] | DER (inputs VP) |
| Sensitivity | $289 per bp → about $2,890 per 10bp; $7,736 of headroom = 27bp | brief s6; F-101/F-104 | VRF inputs, DER |
| Typical yearly swing of that price | 4.45bp/day realised in 2026 (D7) → about 71bp a year → about $20,400 (1 sd) | `D9_numbers.py` [3] | DER; sqrt-time annualisation ASM |
| Three-week swing (a fill around Oct 1 to reflections around Oct 20) | about 17bp → about $5,000 | same | DER, ASM |
| The ladder cost more than $300k on 173 of 185 trading days of 2026 | Jan 2 $316.5k; Feb 27 $325.6k | F-111 | VP inputs, DER |
| Hedge tracks the payments within about $450 per 100bp (forward-consistent) | S3 ticket section 3 | CITED |
| "Stocks and Treasuries fell together in 2026" (question premise) | stocks were up about 13% YTD while IEF was down 4.20% YTD | B5b (stocks, CITED); IEF -4.20% YTD, F-203 (VP) | premise is loose: do not repeat it |

**Why this wording and not the example's (INT).** For a client with a fixed-dollar bill, the risky position is the one
whose value does *not* move with the bill. Cash keeps the WInS number still, while the price of her promise moves
about $20k in a typical year. The hedge's dollar value moves, but it moves together with the bill. That is one plain
idea: "measured against her payments, not against the screen".

**Option (ii) vs (iii): the words test (new; informs gate box (b), does not decide it)**

| | (ii) after-2028 mix scaled to $300k | (iii) literal January 2027 book |
|---|---|---|
| Hedge size in WInS | 66%, about $198k (S3) | about 98%, about $294k (S3) |
| Can the note say "sized to the price of her ten payments (about $292k)" truthfully in one clause? | No. It needs a second clause (the promise's share once both deposits are in, about two-thirds), or a reader sees a $94k gap | Yes, almost one-for-one |
| Words needed | about 15-20 more words in each hedge note | none extra |

The S3 ticket's (ii) sentence already has the three contents. This finding only prices how many words it costs in a
note. The team decides with gate box (b).

**Checklist for the hedge note (adds to the S3 ticket's note checklist 1)**
- [ ] The first clause says what the position is for (Laura's ten payments, 2033-2042).
- [ ] One dated number: that day's price of the payments (re-run `D9_numbers.py` [3] or `A2_curve_recheck.py` on the
  trade date).
- [ ] "Moves like / stands in for", never "matches"; no "stable", "safe" or "reduce volatility".
- [ ] One named risk and the rule: the value falls if rates rise, but so does the price of the payments, so the team
  never sells after a rise.
- [ ] Under option (ii), one clause explaining the scaled mix.

**Implication.** *Sentence-level spec for the hedge note (WInS-now → TN reflection 1).* Deadline tier 1. Confidence:
high.
- Changes the strategy? No. It gives gate box (b) a communication input.
- Criterion: Portfolio Analysis ("understanding and effective use of investment concepts").

**What this teaches.** "Risky" always means risky *relative to something*. For someone saving toward a fixed bill, the
right yardstick is the bill, not the screen.

---

### M212 (tier 1 part): the decision log that later proves one strategy

**Question.** What single table lets a reader verify in one minute that the TN, IPS, WInS book and Final Report tell
one strategy?

**One-sentence answer.** That table belongs to the Final Report and waits until after Nov 9. The part due now is to log
every trade with the five M001 fields plus a provisional rule name, so the table later copies out rather than being
reconstructed.

**Evidence.**
- "maintaining a clear and consistent investment strategy across all three" (case L161-162, VRF).
- "maintains consistency with the team's IPS" (SMApply L49, VRF).
- "Strong submissions connect the client's goals, research, portfolio decisions, and final recommendations through one
  clear and cohesive investment strategy." (Infographic L40-41, VRF).
- Guardrails items 17-18 already require exact note copies and screenshots (VRF).

**Decision-log columns (spec):**
- date and time (ET);
- ticker, side, shares, fill price;
- note text exactly as WInS shows it;
- role word and team label;
- Laura need;
- fact and source;
- risk and rule;
- **provisional rule name** (e.g. "Rule 1: payments first"; the team names its rules once and reuses the names in the
  IPS);
- note candidate? (yes/no, and why).

**Implication.** *Decision: add the rule-name column now (WInS-now).* The table itself goes on the "Later" list.
- Deadline tier 1. Confidence: medium (the value depends on the team keeping the log).
- Changes the strategy? No.
- Criterion: Investment Strategy (consistency with the IPS).

**What this teaches.** Consistency is easier to record than to reconstruct. A column filled in on the day beats a
paragraph written from memory.

---

## TIER 2: the IPS (Nov 6; the strategy freezes)

### M036: which numbers the words-only IPS carries, and whether tables are allowed

**One-sentence answer.** Use no tables, and carry only three kinds of number:
- case facts, used sparingly because they cost words;
- the rule parameters that make the frozen strategy testable later;
- at most one rounded, dated computed result.

It must also physically fit: about 470-490 IPS words on two pages, checked on the exported PDF.

**Evidence**

| Claim | Source | Status |
|---|---|---|
| "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted." Tables are not named | IPS guide L123 | VRF |
| "Focus on the strategy and decision-making framework ... rather than describing individual investments or presenting detailed financial calculations." | IPS guide L51-52 | VRF |
| Not expected: "final operating-reserve calculations, detailed portfolio projections, a final facility-contribution range" | IPS guide L68-69 | VRF |
| "the IPS becomes the official record"; "may not revise its investment strategy after the submission deadline"; the Final Report "will evaluate how effectively it implemented that strategy" | IPS guide L73-77 | VRF |
| "Formatting choices not specified below are left to the team's discretion. Keep the presentation simple" | IPS guide L101-102 | VRF |
| Non-compliance: "will not be considered for semifinal selection" | IPS guide L82-83 | VRF |
| "Excessive investing jargon doesn't necessarily dazzle the judges. Your report should reflect your team's voice." / "Don't use precious space repeating known facts about your client and defining concepts. However, it is okay to demonstrate that you understand your client beyond the case study." | https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages?slug=judging-and-evaluation (retired 2023-24 judging page, accessed 2026-09-28) | VP (past season, not 2026-27 rules) |
| Official PDFs are US Letter (612 x 792 pt); Wharton's sample IPS uses a 24 pt line pitch, a blank line before the IPS heading, and tab-indented paragraphs | pypdf on `2026_WGY_Investment_Policy-FINAL.pdf` pp.5-6 | VRF (measured) |
| Page fit (see table) | `D9_ips_page_fit.py` | DER; Word line height and Liberation-Serif = TNR widths are ASM |

**Page fit (50-word pitch + 500-word IPS, 1-inch margins; lines needed / available on pages 2-3)**

| Paper | Line height | Needed | Available | Spare | Max IPS words that fit |
|---|---|---|---|---|---|
| US Letter | 27.6 pt (Word "Double", TNR 12) | 44-46 | 46 | **0-2** | about 525 |
| A4 | 27.6 pt | 46-48 | 50 | 2-4 | about 550 |
| US Letter | 24 pt (Wharton's sample) | 44-46 | 54 | 8-10 | about 615 |
| A4 | 24 pt | 46-48 | 58 | 10-12 | about 665 |

Proxy vocabulary averages 13.4 words per line on Letter. A text made only of long words (7+ characters) fits 9.0, so a
draft heavy in words like "contribution" and "Treasury" needs more lines. Run the script with `--draft` on the real
text, and in the end trust only the exported PDF.

**Number policy (spec)**

| Kind | Examples | In the IPS? |
|---|---|---|
| Case facts | $300,000 / $150,000; ten $50,000 payments 2033-2042; 2031 | Only where a rule needs them; each costs words and adds nothing new |
| Rule parameters (policy, not calculation) | stock share of the growth money and its band; share of the growth money bought as the 2031 floor; how the 2033 remainder is split between facility and flexibility (D5's give-back share); how often the plan is reviewed | **Yes.** These make the frozen IPS testable, and the Final Report is judged on implementing them |
| Computed results | "the ten payments cost about $292k at September 2026 prices" | At most one, rounded and dated. Optional. Never "bought in January 2027" as a flat claim (D7 M011) |
| Model outputs | percentiles, miss rates, 4-in-10 odds, range dollars | **No.** These go to the Final Report |

**Format checklist (IPS):**
- [ ] Headings exactly as in the sample.
- [ ] No blank line between IPS paragraphs.
- [ ] No tables and no bullet lists.
- [ ] No quotation marks around anyone's words.
- [ ] No URLs, footnotes or "(Source, year)".
- [ ] Title page on page 1 only; page break before page 2.
- [ ] Word count done with the same tool, with 5-10 words to spare.
- [ ] PDF of 5 MB or less; the text ends on page 3.

**Implication.** *Decision and number:* IPS target about 470-490 words; the numbers limited to the policy above; no
tables (IPS).
- Deadline tier 2. Confidence: high on the policy. Medium on the exact line counts (ASM line heights), which is why the
  PDF check is the binding step.
- Changes the strategy? No.
- Criterion: Creativity and Presentation (and format compliance, a gate for everything else).

**What this teaches.** A limit is physical as well as numerical. "500 words" and "two pages" are two different
constraints, and the tighter one depends on settings nobody told you about.

---

### M143: name, as the client benefit, that the promise stops depending on her future earnings

**One-sentence answer.** Yes. It is the most Laura-specific benefit the plan can claim, and it fits in the pitch. It
must be said as a consequence of a rule ("once the payments are bought"), not a date. In about 23-31% of modelled
paths the ladder needs part of the 2028 deposit.

**Evidence and numbers**

| Claim | Source | Status |
|---|---|---|
| The 2028 $150,000 comes from "earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" | case L43-45 | VRF |
| Laura called going self-employed a move to "unstable income" (2021 interview) | https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid (re-checked 2026-09-28) | VP. **Final Report only**: no quotes in the TN or IPS (D13 rule) |
| The $150k is 33% of all the money she puts in | case L43-45 | DER |
| P(ladder costs > $300k on 2027-01-01): 24.3% (A2), 23% (D7), 30.7% (S4) → the promise is independent of 2028 income from January 2027 in about 69-77% of modelled paths, otherwise from January 2028 | `D9_numbers.py` [5] | DER from ASM-based runs |
| The case says she "will contribute" the $150k, so frame this as resilience, not as fixing a risk the case names | stats skeptic, R-AN35 | CITED |
| Credibility is part of her income (reputation-driven advances and speaking) | stakeholder map BS-03 | CITED (INT) |

**Content spec (pitch and IPS; elements only)**
- The claim: after the payments are bought, neither markets nor her next contract can undo the ten-year promise.
- The condition, in plain words: bought with the first deposit if prices allow, otherwise finished with the second
  (the rule already in brief section 7).
- What still depends on her income: the size of the facility contribution, not the payments.
- Swap test: passes, because only a client with career-driven deposits gets this benefit.

**Implication.** *Sentence content for the 50-word pitch and the IPS opening (IPS); also the "why" of the hedge note
(TN).*
- Deadline tier 2 (content can already shape the hedge note in tier 1). Confidence: high.
- Changes the strategy? No.
- Criterion: Client Knowledge and Objectives ("recommendations that can earn her confidence").

**What this teaches.** The best benefit statement names what the client no longer has to worry about. It stays honest
by saying exactly when that becomes true.

---

### M241: justify where risk sits with the case's own asymmetry

**One-sentence answer.** Yes. It is the case's own reason for the whole design: outside money may fill a facility
shortfall but never Laura's ten payments. One IPS clause should say so in those terms. Note the wording nuance
"never her ten payments", not "never operating costs". The case lets others fund "operating support beyond Laura's
commitment".

**Evidence**

| Claim | Source | Status |
|---|---|---|
| "Any remaining facility cost, and any operating support beyond Laura's commitment, may come from co-sponsors, grants, collaborators, program fees, continued business income, or other sources." | case L85-86 | VRF |
| "All ten payments must be funded by the investment portfolio with a high degree of certainty. Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this requirement." | case L91-92 | VRF |
| The IPS guide asks exactly this: "How will your strategy protect the operating commitment while preserving flexibility for a responsible facility contribution?" | IPS guide L25-26 | VRF |
| Already noted as an anomaly (R-AN6) and as "promise first" (BS-17); not yet used as the justification sentence | case_register, stakeholder_map | CITED |

**Merged principle (INT; with M226).** Risk goes where the amount can flex and others may help. It never goes into
the fixed bill that only her portfolio may pay. This single idea answers M241 (where risk sits), M226 (why the
longest-dated money is the safest) and part of M143 (why the promise is independent). The IPS should state it
**once**, then apply it in each rule. That saves 30-60 words against stating three separate reasons (INT).

**Implication.** *One IPS principle clause (IPS).* Too long for the pitch unless compressed to "risk only where others
can help" (INT).
- Deadline tier 2. Confidence: high.
- Changes the strategy? No.
- Criterion: Investment Strategy ("a clear and creative investment thesis").

**What this teaches.** The strongest justification for a design is often already in the brief. Find the sentence
where the rules treat two things differently, and build around that difference.

---

### M226: why the longest-dated money is the safest (answering "longer horizon = more stocks")

**One-sentence answer.** A fixed-dollar bill is bought, not grown. Horizon earns risk only for money whose amount can
flex. With today's Treasury rates close to JPM's stock forecast, stocks end below the locked amount in about 4 paths
in 10 whether the horizon is 6, 10 or 15 years, so a longer wait does not rescue a fixed bill.

**Evidence and numbers**

| Claim | Number | Source | Status |
|---|---|---|---|
| The reflex a reader brings | "Investors with a longer time horizon may feel comfortable taking on riskier or more volatile investments." | https://www.investor.gov/introduction-investing/getting-started/asset-allocation (accessed 2026-09-28) | VP |
| The bill is fixed | "each payment is a fixed $50,000 and is not adjusted for inflation" | case L90 | VRF |
| Locked rates 2027 → 2033/2037/2042 | 5.08% / 5.24% / 5.48% | brief s6 (forward zeros from the 2026-09-25 curve) | DER from VP |
| JPM U.S. large cap | 6.70% compound, 7.94% arithmetic, 16.47% vol (data 2025-09-30) | brief s6 | VRF |
| P(stocks end below the locked amount), U.S. large cap | 40.3% (6y), 38.7% (10y), 38.5% (15y); simulation check 38.8% (10y, 200k paths, seed 20260927) | `D9_numbers.py` [2] | DER; lognormal i.i.d. ASM |
| Same, AC World (7.00%, 16.78%) | 38.7% / 36.7% / 35.9% | same | DER, ASM |
| Stock premium over the locked rate | 1.6 / 1.5 / 1.2 points a year | same | DER |
| Caveat: JPM's inputs date from when the 10y was 4.16%, about 100bp lower; the 2027 edition is not out | brief s14 | VP there |

**Why the odds barely fall with horizon (INT, plain English).** The usual "time smooths out risk" story works when
stocks are expected to beat the safe rate by a wide margin. Here the margin is only about 1.2-1.6 points a year, so
the extra years add as much uncertainty as they add expected lead. Also, a single missed payment is a broken promise,
not a bad average.

**Content spec (IPS: one clause, no number; the 4-in-10 figure goes to the Final Report).**
- The idea that the payments are a fixed-dollar bill, so they are bought.
- Horizon matters for the money whose size can change (the facility, flexibility).
- Say it with the M241 principle, not as a separate paragraph.

**Implication.** *One IPS clause (IPS).* The number is on the Final Report list.
- Deadline tier 2. Confidence: high on the principle. Medium on the exact odds (model ASM and JPM vintage).
- Changes the strategy? No.
- Criterion: Portfolio Analysis ("integrates quantitative and qualitative analysis").

**What this teaches.** Rules of thumb carry hidden conditions. "Long horizon means more stocks" assumes stocks are
expected to win by a lot and that the goal can bend. Check both before applying it.

---

### M071: how much of the IPS is about Laura, and on what each sentence may rest

**One-sentence answer.** Put Laura inside the rules as "because" clauses, roughly 40-60 of 500 words as guidance
rather than a target, never as a biography paragraph. In the IPS, use only case facts that change a decision. Save
beyond-the-case evidence, with its sources and at most one or two dated quotes, for the Final Report.

**Evidence**

| Claim | Source | Status |
|---|---|---|
| "Always remember who your strategy is designed to serve." / "should demonstrate how your strategy is tailored to your client's financial goals, time horizons, and needs" | IPS guide L27, L45 | VRF |
| "Don't use precious space repeating known facts about your client ... However, it is okay to demonstrate that you understand your client beyond the case study." | retired Wharton judging page (URL above) | VP (past season) |
| "sources do not need to be cited in the IPS. Relevant sources and supporting evidence must be included in the Final Report." | IPS guide L124-125 | VRF |
| "While the client is real, the financial scenario is developed specifically for the competition." | R-W4 | CITED (VP in Phase A) |
| No Laura quotes in TN or IPS; only D13a VERIFIED-PRIMARY lines may be her words; no "investment philosophy" | brief s16, D13c | CITED |
| Swap test | D13c section 8 | CITED |
| The 30-50-word number is false precision; keep the principle | stats skeptic (M071) | CITED |

**Which facts earn a place (spec)**

| Fact | Status | Decision it changes | IPS? |
|---|---|---|---|
| The 2028 money is career income (advances, speaking, licensing) | VRF (case L43-45) | the payments are bought from the first deposit where possible; the facility absorbs a late or smaller deposit | Yes |
| Fixed nominal payments that only her portfolio may fund | VRF (L90-92) | risk sits only in money whose amount can flex (M241) | Yes |
| The 2031 promise must not overpromise; her credibility is at stake | VRF (L114-116) | the bottom of the range is bought, not forecast | Yes |
| Statistics degree | VRF (L16) | certainty defined as testable; every probability names its model | Once at most |
| "Willing to take thoughtful risks" plus "appropriate balance" | VRF (L70-74) | the growth money is real growth, not set at the minimum to look safe (D13c) | Yes, briefly |
| "unstable income" (her 2021 words) | VP | same as the first row | No (a quote): Final Report at most |
| Community/access priority; "earliest supporters" (2016, student-era) | VP (D13a) | 2031 message order | No: Final Report at most |
| Identity, heritage, Taiwan as a personal reason for holdings | n/a | none (tokenism) | Never |

**Implication.** *Number and rule: about 40-60 Laura words across the rules; every Laura clause states a fact and the
decision it changes (IPS).*
- Deadline tier 2. Confidence: medium (the word range is judgement).
- Changes the strategy? No.
- Criterion: Client Knowledge and Objectives.

**What this teaches.** Understanding a client shows in how well the plan fits her, not in how much you say about her.
One "because" per rule does more than a paragraph of biography.

---

### M121: which three trade-offs the IPS names

**One-sentence answer.** Name three things Laura gives up, each in plain words:
- **T1:** some facility money in good markets, for ten payments that cannot miss;
- **T2:** some growth after 2031, for an amount she can promise co-sponsors;
- **T3:** the chance of cheaper bonds if rates rise, for not risking dearer ones if they fall (buying all at once).

State them without numbers in the IPS. The numbers wait for the Final Report.

**Evidence and numbers (`D9_numbers.py` [4])**

| Trade-off | What she gives up | What she gets | Numbers | Status |
|---|---|---|---|---|
| T1 certainty vs size | about $19k of median 2033 surplus ($207k vs $226k); about $267k of p95 upside ($273k vs $540k) | never misses by construction vs 3.2% miss (13.7% if the 2028 deposit is $75k; 40.8% if $0); +$139k in the worst 5% ($159k vs $20k) | brief s6 / F-401 | DER from the verified run (ASM model) |
| T2 bought floor vs growth | each +10 points of 2031 lock share moves about $20k into the floor and takes about $10k each from the upside and from kept flexibility | a range bottom that is already owned | D5 finding 2 | CITED (ASM model) |
| T3 all at once vs gradual | if rates rise 100bp before purchase the payments would have cost $27,374 less | if rates fall 100bp they cost $30,600 more; cost exceeded $300k on 173 of 185 days in 2026 | brief s6; F-111 | VRF / DER |

- **Source consistency warning.** D13c's re-run of the B10b script gives about $11k at the median for a different
  comparison. The team should quote one source only (the verified `strategy_mc.py` run is the reference, brief s8)
  (DER).
- **Not a trade-off: inflation.** Say it as an assumption. The $50,000 is fixed in dollars, so it buys less each year.
  That is the case's design, not a team choice. The IPS names it as an assumption; the Final Report sizes it (case
  L146-147 asks for the effect of inflation on "portfolio projections and facility costs").
- "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and
  tradeoffs behind those decisions." (Guide p.5 L183-184, VRF); "There is no single correct strategy. Strong teams
  explain the reasoning, assumptions, and tradeoffs behind their decisions." (Infographic L42, VRF).
- D13c's candid clash (brief s16): whole-portfolio equity is about 0-2% in 2027, about 20% in 2028-30 and about 4%
  after 2031. T1 is the honest place to answer "is this too cautious for someone who takes the jump?" (INT).

**Implication.** *IPS checklist: three named trade-offs, each "gives up X to get Y" in words (IPS).*
- Deadline tier 2. Confidence: medium-high.
- Changes the strategy? No.
- Criterion: Investment Strategy (the Guide's "reasoning, assumptions, and tradeoffs").

**What this teaches.** Every choice has a price. Saying the price out loud is what makes a recommendation trustworthy,
because the reader can see you looked at the other side.

---

### M191 (IPS part): how the confidence in the 2031 range is stated

**One-sentence answer.** Partly mis-posed. The IPCC advice is about framing (report a chance both ways), not about
splitting the two tails. But the useful rule survives and belongs in the IPS as method:
- the bottom of the range is money already bought in 2031, stated as fact;
- only the top carries a stated chance, with its model named.

D5 owns the numbers (Final Report).

**Evidence**

| Claim | Source | Status |
|---|---|---|
| "Consider reciprocal statements to avoid value-laden interpretations (e.g., report chances both of dying and of surviving)." and "it may be appropriate to describe findings for which evidence and understanding are overwhelming as statements of fact without using uncertainty qualifiers." | IPCC AR5 Guidance Note, https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf (accessed 2026-09-28) | VP |
| "state how confident they are that her 2033 contribution will fall within that range" (two-sided) | case L117-118 | VRF |
| With the floor bought in 2031, P(below) = 0 barring U.S. default; P(above top) = 15% at D5's candidate q = 0.85 | D5 finding 2 | CITED (ASM model) |
| A dollar range fixed today would be missed below in 10-50% of paths | D5 finding 4 | CITED (ASM) |

**Implication.** *IPS rule (method only):* "the range is set in 2031 from what is then owned; its bottom is bought; its
top is a stated chance" (content, not wording). Put the numbers and the two-sided statement on the Final Report list.
- Deadline tier 2. Confidence: medium.
- Changes the strategy? No (it is brief section 7's rule, worded for testing).
- Criterion: Creativity and Presentation ("communicates ... investment uncertainty clearly and credibly to prospective
  co-sponsors").

**What this teaches.** When part of an answer is already certain, say it as a fact, and spend your probability words
only where uncertainty really lives.

---

## The pitch: which ideas fit in 50 words (spec, not text)

Candidate elements and a rough word cost (INT: estimated from typical phrasing lengths, not counted text):

| Element | Why it earns pitch space | Approx. words | Keep? |
|---|---|---|---|
| Central idea: the ten payments bought first with U.S. Treasuries | the IPS guide asks for "the central idea" (L35-36) | 12-15 | Yes |
| Client benefit: the promise stops depending on markets or her future earnings, once bought (M143) | most Laura-specific claim; conditional wording | 12-15 | Yes |
| Growth purpose: the rest invested for growth toward the facility contribution and flexibility | covers "financial goals and future funding needs" | 10-12 | Yes |
| 2031: a range whose bottom is already owned | the credibility theme; distinctive | 8-12 | If words allow |
| Case asymmetry (M241) / horizon logic (M226) | reasons, not the idea | 15+ | No: in the IPS body |
| Any computed number | IPS guide L51-52 | 3-6 | No |

Four elements at the low end already come to about 42-54 words. So a 50-word pitch holds three elements comfortably
and a fourth only in very plain words. `D9_draft_checker.py --kind pitch` counts and flags.

---

## TIER 3: Final Report (out of scope until Nov 9)

### M031: the single co-sponsor chart

**Answer.** Final Report only; the IPS bans charts. Parked under brief section 17. The only action now is D7's point:
capture WInS hedge values and the same-day treasury.gov price of the payments from the fill date, so later analysis
uses data recorded at the time.
- Deadline tier 3. Confidence: n/a.
- Criterion: Creativity and Presentation.

### Later (after Nov 9), one line each
- M031: one chart, ten payment blocks marked "bought" plus the 2031 floor bar, with a band for a weak, median and
  strong 2031 (D5 script data).
- M191: state P(below range) and P(above range) separately, with the model named (D5 numbers).
- M212: a six-row table: IPS rule → WInS trade → note as quoted → Final Report verdict, copied from the decision log.
- M226: the "about 4 in 10 even at 15 years" figure, with its model and JPM vintage stated.
- M121: the T1-T3 numbers, from one model source only.
- M071/M143: at most one or two dated Laura quotes in context (e.g. "unstable income", 2021), per D13a.

---

## Sources (accessed 2026-09-28 unless noted)

**Official, in the repo (VRF):**
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L16, L43-45, L70-74, L83-99, L102-103,
  L114-120, L126-127, L136-147, L161-162)
- `2026_WGY_Investment_Policy-FINAL.txt` (L10, L20, L25-27, L35-36, L45, L51-52, L59, L68-77, L82-83, L101-125) and
  its PDF (page size and sample layout)
- `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L5, L20-23, L36-53)
- `2026_WGY_Investment_Competition_Guide.txt` (p.3 L84-86; p.5 L183-184)
- `2026_WGY_Competition_Infographic.txt` (L40-42)
- `SMApply_Deliverables_Page_2026-09-27.md` (L49-57)

**Primary web (VP, re-read by D9 with `fetch_text.py --grep`):**
- Investor.gov asset allocation page: https://www.investor.gov/introduction-investing/getting-started/asset-allocation
- IPCC AR5 Uncertainty Guidance Note: https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf
- Wharton retired judging page (REST):
  https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages?slug=judging-and-evaluation
- Overachiever Magazine interview (2021-03-15):
  https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid
- treasury.gov daily par yield curve 2026 CSV (live download inside `D9_numbers.py`; latest date 09/25/2026 at run
  time)

**Market data (VRF):** `competition/official_market_data/` (IEF/TLT fact sheets 2026-06-30; the curve CSV).

**Other run files (CITED):**
- `research/insight_v1/_context/brief.md` (s6, s7, s8, s14-s17)
- `phase_A/case_register.md` (R-AN6, R-AN43), `fact_register.md` (F-101, F-104, F-111, F-201-F-203, F-401, F-402,
  F-409), `stakeholder_map.md` (SH-16, BS-03, BS-05, BS-17), `wins_week1_guardrails.md` (section c)
- `wins_now/securities_and_allocation_v0.md`
- `phase_D/D5_cosponsors.md`, `D7_wharton_intent.md`, `D13a_laura_quotes_verified.md`, `D13c_voice_map.md`
- `research/blueprints/01_trading_notes_blueprint.md`, `research/council_2026-09-27/01_chair_memo.md` (sections 4, 7)

**Not re-read by D9:** Jenkins, Harris & Lark (2019), via B6b.

---

## What this teaches

1. **Plain English is a discipline, not a tone.** Each idea must survive three squeezes: a 90-word note written before
   the outcome, a 50-word pitch, and a 500-word IPS that must also fit on two physical pages. An idea that cannot be
   said in one plain clause is usually not yet understood, or not yet one idea. Three of our questions turned out to be
   one principle said three ways.
2. **Words are claims.** "Certain", "confident", "reliable", "matched" and "safe" each promise something different.
   Choosing each word on purpose is part of the investment analysis, because it states exactly what risk remains.
3. **Measure risk against the goal.** For a client with a fixed bill, cash is the risky choice and long bonds are the
   careful one. The yardstick decides the answer.
4. **Write the record while it is cheap.** A dated fact and a named risk in each note, plus one decision-log column,
   cost minutes now and make every later deliverable consistent almost automatically.

---

## Audit corrections (AY2)

Auditor AY2, 2026-09-28. The text above is left unchanged. Each item says what to correct, its severity
(blocking / important / minor), and which deliverable it touches (TN or IPS). Evidence and the cross-file view are in
`research/insight_v1/phase_D/audit_judges_practice_comms.md`.

**Reproduced and confirmed (no change needed):**
- **Scripts:** `D9_numbers.py`, `D9_ips_page_fit.py` and `D9_draft_checker.py --demo` were re-run. Every quoted figure
  reproduces:
  - vocabulary counts; 40.3/38.7/38.5% (simulation 38.8%);
  - $2,890 per 10bp; about $20.4k a year; T3 +$30,600 / -$27,374; 69-77%;
  - 44-46 of 46 lines; about 525 words;
  - 59 words, 413 characters, 0 digits.
- **Sample PDF:** AY2 re-measured Wharton's sample with pypdf. It is US Letter at a 24.0 pt line pitch, with one blank
  line (48 pt) before the IPS heading.
- **Sources re-found verbatim:** Investor.gov; IPCC (two quotes); the retired Wharton judging page (two quotes);
  Overachiever "with unstable income".
- **Official lines as cited:** IPS guide L82, L101, L104, L116, L123-124; case L85 vs L91-92.
- **Extra support for M001:** the TN guide itself says notes "should document the research, analysis, and reasoning
  behind your investment decisions" (TN guide L7-8).

**Corrections**
1. **[important, TN] The VGSH row of the fixed-labels table overclaims.**
   - The row maps VGSH to "the amount she can promise co-sponsors in 2031" and gives "already owned" as its certainty
     word. This brings back the "floor proxy" overclaim the S4 red team removed (ticket, changes after red team, item
     4).
   - In 2026-2030, VGSH is part of the growth money. The 2031 floor is bought only in 2031, from all of the growth
     money.
   - Use: role word "liquidity" (or "future funding"); label "short-Treasury part of the growth money"; Laura need
     "facility contribution and flexibility; the kind of asset a 2031 floor can later be built from" (the ticket's "can
     later become"). No "already owned" before 2031.
   - WInS notes are permanent, so this must be fixed before the first order.
2. **[important, IPS] The certainty vocabulary leaves out "uncertainty".**
   - The official files use "uncertainty" 11 times (AY2 whole-word count): case 2, IPS guide 1, Guide 6,
     Infographic 1, SMApply 1.
   - Case test 3 says a strategy "Addresses how investment uncertainty could affect both the operating commitment and
     the facility contribution" (L137). The Creativity criterion asks for "investment uncertainty clearly and
     credibly".
   - So the vocabulary must not imply that the payments carry no uncertainty. Add a row: "uncertainty" is the official
     word for what markets can do to both goals. For the payments it is limited to named residuals: rates before
     purchase, the 2028 deposit in the rates-fall branch, a U.S. default, and purchasing power in Taiwan.
3. **[important, IPS] The assumption line leaves out currency.** Brief s16, which is binding, requires both certainty
   gaps to be named plainly. One is that "certain" is in nominal U.S. dollars while the residency's costs are in
   Taiwan. Put the USD/TWD purchasing-power point into the same assumption clause as inflation. The words are the
   team's; D4 owns the numbers.
4. **[important, TN] The M012 one-sentence answer is a fill-in sentence for a permanent WInS note.** It reads: "The
   position holds the value of Laura's ten fixed $50,000 payments, which cost about $X at [trade-date] Treasury prices
   ..."
   - WInS notes are quoted exactly and cannot be edited, so a template the team fills in becomes AI-written text in a
     submitted deliverable (Wharton AI policy; brief s4).
   - Recast it as the element list already in the checklist, and mark each quoted phrase "illustrative, do not copy".
   - The same applies to three phrases that are close to pitch- or IPS-ready: "measured against her payments, not
     against the screen" (L288), "risk only where others can help" (L483) and the M143 claim sentence (L445).
5. **[important, IPS] Nobody has added up the IPS elements across D7, D8 and D9.** This file owns the page-fit check.
   - Together the three files ask for about 13-15 IPS elements. Their own estimates sum to roughly 310-475 words before
     connecting words, against this file's 470-490-word cap.
   - The ips_spec owner should set one budget (table in the audit summary, section 5). Merge the return objective into
     rule 2; merge risk tolerance with the M241 principle; fold inflation and currency into the certainty definition.
     Cut the fee clause first.
6. **[minor, IPS] "Locked" is the wrong word for 5.08/5.24/5.48% (L76-78, L497-510).** These are forward rates implied
   by the 2026-09-25 curve for a January 2027 purchase. Nothing is locked until her money arrives; D8 says this
   correctly for its 5.23%. Say "the rates today's curve implies for a January 2027 purchase". The 4-in-10 conclusion
   does not change in kind.
7. **[minor, IPS] T1's "+$139k in the worst 5% of paths" misreads a percentile gap.** It, and "gives up $267k of
   best-case upside", are differences between two strategies' percentiles, not gains in the same paths. Say "the bad
   case (5th percentile) is about $139k higher". These numbers belong on the later list in any case.
8. **[minor, TN] Also fix blueprint 01's risk example.** When blueprint 01 section 3 is updated (M001 implication),
   remove its risk example "bond prices fall if rates rise, which does not matter for held-to-maturity matching"
   (blueprint L35). It is false for WInS funds, which never mature, and it contradicts this file's own vocabulary.
9. **[minor, TN + IPS] Some terms and vocabulary rows state "bought in January 2027" flatly.** Examples: L140 "Ladder:
   real Treasury bonds bought in January 2027"; L195 and L243 "stands in for the bonds she buys in January 2027". Add
   "starting January 2027; completed from the 2028 deposit if prices have risen", to match D7 M011 and this file's
   M143.
10. **[minor, TN] "Hundreds of teams will copy its wording" is D9's judgement.** Label it INT; there is no evidence
    about other teams' notes.
11. **[minor, IPS] Page fit: add a fallback.** (INT) The official sample is set at exactly 24 pt. So "Exactly 24 pt"
    line spacing is a defensible reading of "double-spaced" if a draft overflows under Word's "Double". The team
    decides, and the exported-PDF check stays binding. A common rule of thumb (about 250-300 double-spaced words a
    page) also puts 550 words plus headings right at two pages, which supports the 470-490 target.
12. **[minor, TN + IPS] Using the draft checker counts as AI use.** Running `D9_draft_checker.py` (an AI-built tool) on
    drafts must be logged in the team's AI-use record (R-W46), like any other AI help.
13. **[minor, TN + IPS] Pick one place for the statistics degree.** This file says "once at most" in the IPS, but the
    ticket uses it in the VT note and D7 uses it for the certainty definition. Across the TN and the IPS, pick one
    place (decoration/tokenism risk).
14. **[minor, TN + IPS] The option (ii) word cost (M012) is also a consistency cost.** D7's pitch rule ("no stock risk
    until all ten payments are bought") reads as contradicted by a day-one VT buy next to a $198k hedge, unless the
    scaling clause appears (D7 correction 3). Give gate box (b) both inputs.

**Verdict for D9:** the strongest communication work in the cluster. The page-fit risk is real and confirmed on
Wharton's own sample, and the note template, vocabulary and trade-off specs are well evidenced. Fix items 1-4 before
the first WInS order and before the certainty glossary is adopted. Item 5 is the main cross-file task for whoever
writes `ips_spec.md`.
