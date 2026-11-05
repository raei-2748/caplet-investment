# 05 · The review rubric for tonight's final pitch and IPS

AI-generated (Claude Code), Thu 5 Nov 2026, night (Sydney). Not for submission. It holds no IPS sentences. Rows B9-10, B10-4, D6, D17 and E22 were retired by Ray the same evening (INSTRUCTIONS I88) and were not applied.

**What this is.** Every testable expectation the students and Wharton have set for the 50-word pitch and the 500-word
IPS, with its source quoted and a yes/no test. Tonight one writer drafts from scratch, and each round is reviewed against
this page, in Book 12's order: (a) every Bible expectation ("by far the most important, and if my exceedingly high
standards are not met, it's back to the drawing board for you"), (b) Wharton's marking guidelines, (c) "just simply
being AS BRILLIANT AS POSSIBLE".

**Read from:** `keel/WHARTON_WORD.md`; `keel/BIBLE.md` (cover note, Books 1-5, 9, 10 with the 18:21 note, 11, 12 and the
Ten Commandments); `keel/INSTRUCTIONS.md` I01-I87; `keel/NORTH_STARS.md`; `keel/BIBLE_TAKES.md`; the "For every Claude
session" block of `CLAUDE.md`; `keel/ips_rewrite/BIBLE_AUDIT.md`; `keel/ips_rewrite/COMMANDMENTS_CHECK.md`;
`keel/ips_rewrite/drafts/D35/README.md`; every note in the shared memory. For the tests I also used the case
(`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`), `ips_rewrite/00_GROUND_TRUTH.md` (form, locked
trading notes), `voice/06_voice_guide.md`, `VOICE.md`, the Archive's 5 Nov check of October's locked words
(`rooms/archive_checks/2026-11-05_what_october_allows.md`), the 5 Nov creativity shortlist and the WInS snapshot of 23 Oct.
Book 12's pasted AI list is source material only. It appears here as hazards (B12-16), never as expectations.

**Who said what.** Two students share the account. **Ahaan** writes the long messages: Books 1-5, 9, 11 and, by
style, 10 and 12 (Keel's files called Books 1-5 "Ray's" until 27 Oct; I48 corrected that). **Ray** (team leader) writes
short, spoken-style messages: I47, I50, I52, I55, I80, I82-I86, the 23 Oct "don't soften" rule, and the 27 Oct
designations of Wharton's files as "BIBLE".

---

## How to use this page

**Codes.** *Applies*: P = pitch, I = IPS, B = both boxes, N = the note Caplet reads beside the draft, R = the review
and process (not the text). *Weight*: **KILL** = a miss sends the draft back to the drawing board (Book 12); **MUST** =
fix it before the draft is handed over; **AIM** = brilliance. Rank drafts that pass every KILL and MUST by their AIMs.

**Order of authority when two rows pull apart.** (1) Hard limits: no trades, no submitting, permitted instruments
only. (2) Wharton's word ("in some senses 'God'", Book 10, 18:21). (3) Book 12 and Ray's 5 Nov points, which Book 12
says to "keep in mind ... because they're really, really important". (4) Books 1-11 and the Commandments: all equal,
but a later book narrows an earlier one where they collide (the cover note: "you can decide all of our instructions
are equal but some are more equal than others, sure! As long as you understand what we're trying to say"). (5) Keel's
own files (the voice guide, VOICE.md). Part E resolves each known collision.

**Reviewer conduct.** These rules come from the books. Break one and the review itself fails.
1. Read the whole draft first, then judge it against the criteria. No single line makes or breaks a draft unless it
   trips a KILL row (Book 10: "Obsessing over a very small and hyper-specific thing is something which only AI does";
   Commandment II).
2. When you score as a Wharton judge would, the only scheme is Wharton's guide (Book 10: "Your only allegiance in terms
   of marking is to the marking guide from Wharton, and ABSOLUTELY NOTHING ELSE"). The compliance pass uses this whole
   page (E25).
3. Never write IPS sentences. Name the fault, quote the line and say what kind of fix it needs ("drop this idea", "say
   what 'this' refers to"). One writer writes everything (Book 12: "There's going to be a single person or agent or
   whatever you call it which writes the entire thing").
4. Never soften a true claim and never propose a hedge. If a strong word is false, say so as a fact, and name the
   equally strong true claim it should become (Ray, 23 Oct: "it would soften our voice"; VOICE.md "Confidence is the voice").
5. Raise no findings on grammar, spelling, punctuation or formatting, other than the word limits (Book 3: "Just don't
   waste your time on that. En dashes are correct in Australia"; Book 9: formatting "DOESN'T MATTER").
6. Give no AI-likelihood score. Name machine-like habits by quoting the line (Book 9: "AI agents are pretty bad at
   detecting themselves"; Book 11: "figure out the fingerprints in your own writing"). See E22.
7. Don't write "if a judge asks" or "be ready to defend" notes. A claim either holds on the page or gets fixed or cut
   (Ray, I82).

---

## A. Wharton's word (ranks first)

### A.1 The form

| ID | Applies · Weight | Expectation | Source (verbatim) | Test (yes = pass) |
|---|---|---|---|---|
| A1 | B · KILL | Two plain-text fields only, pitch and IPS; no title, team name block or headings | Updated IPS instructions (`00_GROUND_TRUTH.md` s0): "Two form fields only."; CLAUDE.md: "an SMApply FORM with two fields, 50-word pitch + 500-word IPS, no title page" | Is the draft exactly two blocks of plain prose, labelled outside the text? |
| A2 | P · KILL | Pitch at most 50 words | "Maximum 50 words." | Is the pitch 50 or under on `office/tools/textcheck.py`'s strict count? |
| A3 | I · KILL | IPS at most 500 words, kept at 497 strict because SMApply's counting is unverified | "Maximum 500 words."; `00_GROUND_TRUTH.md` s0: "Whether SMApply counts words the way `textcheck.py` does is UNVERIFIED" | Is the IPS 497 or under on the strict count? |
| A4 | B · KILL | No charts, images, tables, links, footnotes or citations; no reliance on bold or italics | WHARTON_WORD s2: "No charts, links or citations."; ground truth: "No bold, italics or tables can be relied on" | Does the text work as plain text with none of these? |
| A5 | B · MUST | Research shapes the strategy; no sources are named in the IPS | "Teams should use research and analysis to develop their strategy, but sources do not need to be cited in the IPS." | Does it have no author names, years, journals, study titles, "according to" or "research shows (X)"? |

### A.2 What the pitch must do

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| A6 | P · KILL | States the central idea | Pitch: "Clearly communicate the central idea behind your approach" | Can a cold reader, from the pitch alone, say in one sentence what the strategy does? |
| A7 | P · MUST | Says how the strategy supports Laura's goals and future funding needs | "... and how it is designed to support your client's financial goals and future funding needs." | Does it say how the ten operating payments are secured, and what happens with the facility contribution? |
| A8 | P · MUST | Summarises the strategy, not the case or the name | "Quickly summarize your team's investment strategy." | Is every sentence about what the strategy does, with none spent on case background or on decoding a name? (BIBLE_AUDIT row 109: a pitch that "spends a third of its words explaining a brand name") |
| A9 | B · MUST | Pitch and IPS describe the same plan with the same facts and the same name | Case :161-162: "maintaining a clear and consistent investment strategy across all three"; I06 Window note: "either way, one name in both boxes" | Do the two boxes agree on every fact, date, proportion and name? |

### A.3 What the IPS is for

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| A10 | I · KILL | Explains the strategy and the reasoning behind it | "Clearly explain your team's investment strategy and the reasoning behind it." | Does every move carry its "because" in the same or the next sentence? |
| A11 | I · KILL | States the strategy and the decision-making framework, not a list of investments or sums | "Focus on the strategy and decision-making framework that guide your portfolio rather than describing individual investments or presenting detailed financial calculations." | Is it free of tickers, share counts, prices, yields to decimals and arithmetic, with holdings described by their job? |
| A12 | I · MUST | Tailored to Laura's goals, time horizons and needs | "Your IPS should demonstrate how your strategy is tailored to your client's financial goals, time horizons, and needs." | Is each goal (the payments, the facility, flexibility) tied to a dated decision (2027, 2028, 2031, 2033-2042)? |
| A13 | I · MUST | Approach to risk and return | "Explain how your team will approach risk and return" | Does it say where the plan takes risk, where it refuses to, and what return it looks for from which holding? |
| A14 | I · MUST | Liquidity | "... liquidity ..." | Does it say what is liquid, when, and for what (nothing is needed before 2033; a fixed sum each January from 2033; flexibility money she can reach)? |
| A15 | I · MUST | Portfolio construction and diversification | "... portfolio construction and diversification ..." | Does it explain how the parts fit together and why each part is diversified, or deliberately not? (see A50) |
| A16 | I · MUST | Planned changes as funding needs approach | "... and planned changes in the portfolio as future funding needs approach." | Are the changes dated and tied to needs, from 2027 through to the last payment? |
| A17 | I · MUST | Preparing for the operating commitment | "establish your strategic approach to preparing for the operating commitment" | Is it clear how the ten payments are secured, and from when? |
| A18 | I · MUST | The operating reserve's asset composition over time | "managing the operating reserve's asset composition over time"; case :96-97: "explain how its composition should change, if at all, as the annual payments approach and are made" | Does it say what the reserve holds at the start of 2033 and how that changes as each payment is made? |
| A19 | I · MUST | How a responsible facility contribution is determined | "determining a responsible facility contribution" | Does it state the rule that sets the contribution and the 2031 range (not the figure)? |
| A20 | I · MUST | Preserving appropriate financial flexibility | "preserving appropriate financial flexibility" | Does it say what is kept back, by what rule, and why that much is "appropriate"? |
| A21 | I · MUST | Reflects goals, horizons, liquidity, desired certainty and flexibility | "It should reflect your client's goals, time horizons, liquidity needs, desired degree of funding certainty, and need for financial flexibility." | Does it say in its own words what "a high degree of certainty" means for this plan? (Case :97-98: teams "should also define what they consider a high degree of funding certainty") |
| A22 | I · MUST | Addresses Laura's risk considerations | Form field: "including how the strategy addresses Laura's financial goals, funding needs, and risk considerations." | Does it name the risks specific to her (rates, markets, her own income, the Taiwan-dollar cost of the building) and the plan's answer to each one it raises? |

### A.4 The IPS's own questions (all answered; not necessarily one by one)

| ID | Applies · Weight | Question (verbatim) | Test |
|---|---|---|---|
| A23 | I · KILL | "What is the central idea behind your investment strategy?" | Could a judge quote one sentence in the first paragraph as the central idea? |
| A24 | I · KILL | "What principles will guide your investment decisions?" | Can a reader list two or three principles after one read? |
| A25 | I · KILL | "How does your strategy balance growth, risk, liquidity, funding reliability, and financial flexibility?" | Does each of the five have a home in a sentence, and is the balance between them argued rather than listed? |
| A26 | I · KILL | "How will the portfolio's asset allocation and composition change as future funding needs approach and payments are made?" | Can a reader trace the allocation from 2027 to 2042? |
| A27 | I · KILL | "How will your strategy protect the operating commitment while preserving flexibility for a responsible facility contribution?" | Is the mechanism that protects the payments distinct from the one that keeps flexibility, and are both said? |
| A28 | I · MUST | "make it clear: What your team is trying to accomplish for the client; Why your strategy is appropriate for the client and their financial goals; ..." | Are the aim and the "why for Laura" both explicit? |
| A29 | I · MUST | "You do not need to address these points separately. Your goal is to present a clear, cohesive, and well-supported investment strategy." | Does it read as one argument, with no checklist or one-paragraph-per-question shape? |
| A30 | I · MUST | "Always remember who your strategy is designed to serve. Your client's profile and financial goals should remain at the center of your investment decisions." | Is every decision justified by a fact about Laura or her goals? |

### A.5 What is out, and what is locked

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| A31 | I · KILL | No final reserve sum, projections, final range or co-sponsor text | Not expected: "final operating-reserve calculations, detailed portfolio projections, a final facility-contribution range, or the draft communication to co-sponsors." | Is there no dollar range for 2031, no confidence %, no projected 2033 value and no fundraising wording? |
| A32 | B · KILL | Permitted instruments only | WHARTON_WORD s5: "Not permitted: margin, short selling, stock-secured debt, crypto, derivatives (options, futures, swaps), individual TIPS, individual STRIPS, anything else." | Is everything Laura holds a Treasury bond, a Treasury ETF or a share ETF? Any option is only a foil, plainly not owned. No TIPS, STRIPS, "zeros", puts, collars or leverage |
| A33 | I · MUST | Rules that can't be revised later, so they must be complete now | "Once submitted, the strategy may not be revised."; "Your portfolio and Final Report should reflect the strategy established in your IPS." | Is it free of "we may decide later" and of open options, with every rule written so the Final Report can show it was followed? |
| A34 | I · MUST | Changes tied to dates and needs, never to market moves | Guide: "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply because markets move or hindsight reveals a different outcome." | Is every change triggered by a date or a case event, with none triggered by a price, a yield level or a drawdown? |
| A35 | B · MUST | WInS performance is never part of the plan | Tip: "Do not focus on portfolio performance ... WInS results should not be added to or subtracted from Laura's long-term portfolio projections." | Does it make no mention of WInS gains, losses or value? |

### A.6 Consistency with the locked trading notes, TNA and WInS book (judged together)

October's words are locked and the judges read them beside the IPS (case :161-162; criterion "maintains consistency").
The Archive and a blind checker tested twelve ideas against them on 5 Nov.

| ID | Applies · Weight | Expectation | Locked source (verbatim) | Test |
|---|---|---|---|---|
| A36 | B · KILL | No payment depends on shares | Reflection 3: "VT is where we allow ourselves to be wrong – because it's the only investment not standing between Laura and a payment deadline." | Does every payment rest on a Treasury bond or a fixed-date Treasury fund? |
| A37 | B · KILL | The funds' payout is never called fixed or guaranteed to the dollar | IBTM note: "although the final payout is not fixed"; IBTO note: "Its December payout is not fixed"; reflection 2: "their terminal payout is a net asset value, as opposed to a promise of par" | Is "exactly" said only of a Treasury bond held to maturity, with the funds described in strong but true words (B5-6)? |
| A38 | B · KILL | The minimum facility contribution is never a fixed $150,000 | IBTM note ("not fixed"); case :115: "Rather than promising one exact amount" | Does no sentence put an exact dollar figure on the minimum? |
| A39 | B · KILL | No inflation-linked holdings; inflation is handled by the payments being fixed in dollars | Reflection 1: "a nominal Treasury matches the liability perfectly, meaning we don't need TIPS"; case :90: "not adjusted for inflation" | Is it free of TIPS or "inflation protection" for the payments? |
| A40 | B · KILL | Bonds are held to maturity, never rebalanced as rates move | Reflection 1: "Every year the bonds sit untouched is a good year"; reflection 2: "we'll simply ignore price noise in the interim" | Is it free of any duration rebalancing or of selling a holding before it matures? |
| A41 | B · MUST | Neither claims to duration-match nor rejects it | Reflection 1 says Treasuries remove uncertainty "through duration-matching"; FINAL README: "Don't write 'we don't duration-match'"; memory: say "each payment has its own bond", never that the ladder matches timing | Is it free of both "we match duration" and "we reject (or don't do) duration matching"? Does it describe one holding per payment instead? |
| A42 | B · MUST | Later coupons never pay earlier payments | Nov-2040 note: "A lower-coupon bond would reduce reliance on reinvested coupons" (coupons treated as a weakness inside each bond's own payment) | Is it free of any claim that one bond's coupons fund another year's payment? |
| A43 | B · MUST | A fall in yields costs the facility first, never a payment | IBTR note: "If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility." | Does the 2028 deposit complete the ladder before anything else? |
| A44 | B · MUST | "Before each January", never "just before each payment" or "in January" | Archive check C3: "'Just before each payment' overstates the ladder: the bonds for 2038 and 2039 mature 10.5 and 7.5 months early"; memory: nothing matures in a January | Is every maturity described as "before" a January payment? |
| A45 | B · MUST | Any move of shares to cover a ladder shortfall happens on a stated date, into Treasuries, years before any payment | Reflection 3 (A36); VT note: "They only set how far her gift rises above her promised minimum." (Archive, 5 Nov: a shortfall "paid from" shares contradicts October) | If shares ever cover a gap, does the text say when they move and into what, so that no payment ever waits on a share sale? |
| A46 | B · KILL | Laura commits to no facility amount before 2031, and what she gives in 2031 is a range | Case :104: "There is no predetermined facility contribution."; :101: she decides "After establishing the operating reserve in 2033"; Kitchen check of V58 ("a minimum facility contribution in 2028" is broken) | Is it free of any commitment, pledge or promise in 2027 or 2028, and is the 2031 statement a range? |
| A47 | B · MUST | No share-return figure (and none that contradicts "about 7.5% a year (as per JPMorgan)") | Book 9: "You don't have to use it"; IPS Report doc check (5 Nov): "7% v 7.5%" clash | Is it free of any return figure for shares? |
| A48 | I · MUST | It describes a plan the frozen WInS book already shows | Tip: "Your WInS portfolio should reflect the strategy your team has developed."; WInS 23 Oct: five fixed-date Treasury funds, five Treasury bonds, one world share fund (8.6%), IBTM the largest | Does it need no new trade, and does nothing in it clash with that book? (5 Nov shortlist: "We don't recommend changing the trades this late.") |

### A.7 The five criteria (judged as a whole; the only marking scheme)

| ID | Applies · Weight | Criterion part (verbatim) | Test |
|---|---|---|---|
| A49 | I · KILL | Investment Strategy: "Presents a clear and creative investment thesis" | Is the thesis one sentence long, and is it more than the field's default of "a payment ladder plus stocks plus a lock" (Commandment I)? |
| A50 | I · MUST | "uses appropriate diversification" | Does it argue why the payments rest on one borrower (the US Treasury) and why the shares are spread across thousands of companies? BIBLE_AUDIT W3 found "Why every cheque rests on one borrower is never argued". Diversifying the residency's own funding is an optional extra (shortlist idea 3) |
| A51 | I · MUST | "demonstrates disciplined planning across Laura's changing time horizons and cash-flow needs" | Are there dated rules for 2027, 2028, 2031, 2033 and 2033-2042? |
| A52 | I · MUST | Client Knowledge: "Tailors the strategy to Laura's circumstances, priorities, risk considerations, and residency goals" | Is at least one decision only sensible for Laura (her income's sources, Taiwan, her credibility with co-sponsors), and is Taiwan named? |
| A53 | I · MUST | "demonstrates a thoughtful understanding of the client" | Does it draw at least one inference about Laura beyond the case's facts, stated as "can" when the case doesn't say it (Archive C5: "'can' is the most the IPS may say")? |
| A54 | I · MUST | "presents recommendations that can earn her confidence" | Would a careful reader trust the payments and the range on this text alone? |
| A55 | I · MUST | Portfolio Analysis: "Demonstrates understanding and effective use of investment concepts and tools" | Is each concept used correctly and doing work in the argument (see B4-2)? |
| A56 | I · MUST | "integrates quantitative and qualitative analysis" | Are the quantities (case sums, dates, the plan's proportions and rules) joined to reasons in the same sentences? No model output (B11-2, E7) |
| A57 | I · MUST | "uses reasonable assumptions and projections to evaluate funding reliability, the facility contribution, and financial flexibility under varying market outcomes" | Are the assumptions stated in words? The case :146-148 list is investment performance, timing of cash flows, outside funding, inflation's effect on projections and facility costs, and flexibility. Does it say what a bad market and a good market each do to the payments, the range and the money kept back? (Projections themselves go to the Final Report: A31) |
| A58 | I · MUST | Articulation of Competition Experience | Does it spend no words on team process, which belongs to the Final Report (B11-3)? |
| A59 | I · KILL | Creativity and Presentation: "Presents a compelling, well-organized narrative in an authentic team voice" | Does it read as one ordered argument in a human voice (Part B voice rows)? |
| A60 | I · MUST | "uses data effectively to support conclusions" | Does each number in it prove something in its own sentence? |
| A61 | I · AIM | "demonstrates original thinking and meaningful reflection" | Can a reviewer name the original thought, and is it the plan's, not the prose's (C7)? |
| A62 | I · MUST | "communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors" | Can a reader explain how the range's bottom and top are set, what can move each one, and why co-sponsors can rely on what she says? |

### A.8 What judges look for, and Wharton's advice

| ID | Applies · Weight | Expectation (verbatim) | Test |
|---|---|---|---|
| A63 | I · KILL | "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and tradeoffs behind those decisions." | Is at least one trade-off stated with what Laura gives up for it? |
| A64 | I · MUST | "develop a cohesive strategy in which your investment decisions work together to support the client's objectives across a range of possible market outcomes" | Does each holding's job connect to another's, so that no part stands alone? |
| A65 | I · MUST | "The goal is not simply to identify investments you think will perform well." | Is it free of return forecasts used as reasons? |
| A66 | I · MUST | "Let your investment strategy lead." | Does the IPS open on the strategy, not on the case or the name (B12-7)? |
| A67 | I · MUST | "Know your client. Review the Client Case Study carefully" | Is every case fact right: ten fixed $50,000 payments at the start of each year 2033-2042, "high degree of certainty", "Teams may not rely" on outside money, $300,000 in 2027 and $150,000 in 2028 from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures", co-sponsors approached in 2031, the decision in 2033? |
| A68 | I · MUST | "Explain your decisions ... explain why each investment belongs in your strategy and how it supports Laura's goals." | Does each kind of holding (Treasury bonds, fixed-date Treasury funds, the world share fund) get its reason, including why funds sit beside bonds? (BIBLE_AUDIT W44: that reason "isn't" given) |
| A69 | I · MUST | Case :101-103: "how much of the remaining portfolio she can responsibly contribute ... committing all remaining assets could limit her financial flexibility" | Does part of what's left stay unpromised, for a stated reason? |
| A70 | I · MUST | Case :114-116: "If Laura promises more than she can ultimately contribute, she could damage her credibility ... a credible range" | Does the range rule make over-promising impossible or very unlikely, and say why? |
| A71 | I · MUST | Case :70-73: "willing to take thoughtful risks ... an appropriate balance between pursuing growth and protecting the capital required for her goals" | Does it show where it takes risk on purpose, and why that is the thoughtful amount? (BIBLE_AUDIT W48: "Answered only sideways") |
| A72 | I · MUST | Case :119-120: "The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment." | Is it clear that naming the range can never touch the payments? |
| A73 | I · MUST | Case :136-145, the five musts: supports the payments with high certainty; "Determines a responsible facility contribution"; "Addresses how investment uncertainty could affect both the operating commitment and the facility contribution"; communicates to co-sponsors "clearly and credibly"; "Preserves appropriate financial flexibility" | Is each of the five met in at least one sentence? |
| A74 | I · AIM | Case :146-148: "the effect of inflation on portfolio projections and facility costs" | Does it say why inflation can't change what she owes, and whether it can change what the building costs (Taiwan dollars)? |
| A75 | B · MUST | "Follow the instructions." | Does it pass every A row above? |

---

## B. The Bible, book by book

Rows that repeat a Wharton row point to it. Process rows (applies R) are tested on the round log, not on the text.

### Cover note (Ahaan, Mon 26 Oct, 23:21)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B0-1 | I · AIM | Creative, original, novel, knowledgeable, insightful and plainly widely read | "The level of creativity and originality and novelty and knowledge and insightfulness and exceptionally evident thought-out widely-read nature of our IPS" | Can a reviewer point to the line that shows each of these? |
| B0-2 | N · MUST | Every expectation is met; any one Keel knowingly weighs below another is named, with a reason | "Every single thing I've said throughout all of these 'Bibles' is equal in importance. You can decide to weight certain things above others ... As long as you understand what we're trying to say" | Does the note name each trade-off in one plain line? |
| B0-3 | R · MUST | Deep thought, not haste | "THINK. That's your job. I don't want you to be hasty. That's the worst mistake you could possibly make." | Does the round log show each round changing ideas, not just words? |

### Book 1: the north stars (Ahaan, Fri 23 Oct)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B1-1 | B · KILL | A distinctive team voice that runs through both boxes | "we must have a genuinely distinctive team voice. It must carry throughout. And it must sound unique." | Does the pitch sound like the same person as the IPS, and does neither sound like a template? |
| B1-2 | I · AIM | Cerebral yet witty | "Cerebral yet witty, passionate yet thoughtful, insightful yet confident" | Is there at least one dry line that also argues, and no joke at Laura's expense? |
| B1-3 | I · AIM | Passionate yet thoughtful | same | Are the stakes felt (the residency, the people it serves, her word to co-sponsors) in a plain clause, without sentiment? |
| B1-4 | B · MUST | Insightful yet confident | same | Are claims made flat, with no stacked hedges? |
| B1-5 | B · KILL | Unlike any other team | "we must sound quite unlike any other team" | Cover the team name: are there at least three sentences no other team could have written? |
| B1-6 | I · AIM | Judges enjoy reading it | "I want our work to be the kind of thing they can honestly ENJOY reading." | Does a cold reader call it a pleasure to read, and never get lost? |
| B1-7 | I · MUST | One unifying motif, secondary to the investing | "single unifying extended metaphor or motif"; "this isn't a literature competition; it's an investment competition. So that isn't the primary goal." | If every motif line were deleted, would the investing case be just as strong? (Motif rules: E1-E4) |
| B1-8 | I · KILL | Intellect and investing knowledge over language; both is best | "we would much prefer that you demonstrate an extraordinary intellect and knowledge of investing and strategic thinking and so on than mastery of the English language. But a combination of BOTH ... certainly couldn't do any harm." | Do the strongest sentences carry investing ideas rather than turns of phrase? |
| B1-9 | I · KILL | Truly extraordinary, not just competent | "We cannot make it to the semi-finals of this competition by being just another great competent team with a decent IPS and a good Final Report." | Would a judge put it in the top 50 of 2,300 on its ideas? |
| B1-10 | I · KILL | An "aha" no one else would reach, even teams using AI | "Something which no one else would do or think to do. (Not even the other teams who may also be using AI.) Something to which a judge would think, 'aha'. Insights which make us seem like geniuses." | Can the reviewer name the aha in one sentence, and is it absent from the field's default plan? |
| B1-11 | I · AIM | An unexpected layer of creativity | "That will likely involve an unexpected level and layer of creativity." | Is there one move the reader didn't see coming that still holds up? |

### Book 2: the refinements (Ahaan, Sat 24 Oct)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B2-1 | B · KILL | Nothing roots-themed in the name or the motif | "'Roots and branches' or something similar was actually exceptionally common"; "they might suspect we're all using AI" | Is it free of root, branch, tree, seed, canopy, trunk and grow-from-roots wording? |
| B2-2 | B · MUST | The name is unique to us and to this strategy | "your strategy name must be deeply unique to our team and our strategy"; "a name which only our team could have ... and which could not apply to any other" | Is the name Caplet XR, decoded so that it fits only this plan? |
| B2-3 | B · MUST | The name ties to the motif and plainly fits the strategy | "deeply specific to our extended metaphor / motif. (Whilst still being directly and clearly applicable to our investment strategy, rather than seeming like we're clutching at straws ...)" | Is the decoding literally true of the plan in one sentence (E26)? |
| B2-4 | B · MUST | The name serves us first | "a good strategy is to optimise for OURSELVES first and foremost" | Does the name sound like ours rather than a client brochure? |
| B2-5 | I · KILL | The motif is not in every sentence; a tool, not a crutch | "I probably don't want to see references to it in every single sentence"; "a tool that helps powerfully and distinctively convey our ideas, not a crutch that wastes word count" | Does the motif appear in at most two places, the opening and the close? |
| B2-6 | I · MUST | Subtle, not decorative or bolted on | "I want it to be subtle, though of course without it just seeming decorative or layered on the top as a frantic last-minute addition" | Does each motif line also do an investing job? |
| B2-7 | I · AIM | It builds the narrative arc | "It will help to build our narrative arc."; "perhaps an almost transcendent quality" | Does the close mean more because of the opening? |
| B2-8 | I · MUST | Restrained, because AI over-uses metaphor | "AI has a particular tendency to use such things extended metaphors / motifs far more – and far more eloquently – than humans do. That's the risk." | Is there one image at most, never explained twice (Ray's habit list, `drafts/D35/README.md`: "Metaphor explained twice")? |
| B2-9 | I · AIM | Unexpected connections from uncommon ground | "find unexpected connections, synergies, analogies, syntheses"; "Find uncommon ground – 'the road less taken'" | Is there at least one cross-field connection that holds up as reasoning (C7)? |
| B2-10 | B · KILL | It sounds deeply human | "above all, our IPS and Final Report must sound deeply human" | Read aloud by a stranger, does it sound like a person? |
| B2-11 | B · MUST | Lean, but real and messy | "whilst you must be lean with your writing, you must also sound like real, messy human writing" | Is it free of both padding and the sanded, uniform rhythm of machine prose? |
| B2-12 | B · KILL | Cut the human way, never by rearranging words | "the instinct shouldn't be to just rearrange words so they're more concise. That's exactly what AI has a frustrating tendency to do" | Is it free of telegraphic sentences, dropped articles, noun stacks and colon-joined fragments? |
| B2-13 | B · MUST | Parsimonious and lucid, with no fluff | "we absolutely do want your writing to be parsimonious and lucid. I'm not saying you should insert extra fluff" | Does every sentence do work? |
| B2-14 | R · MUST | A banned-word list is not enough | "Sometimes some aspects of AI writing transcend the kinds of things which you can ban with a neat list of AI tells" | Did the reviewer read by ear as well as checking lists? |
| B2-15 | B · MUST | Written like us, not like the model | "it's important to write like WE write, not like YOU write"; "try to write more like me" | See E9 for how Book 12 reweights this |

### Book 3: Caplet XR and the de-obsessions (Ahaan, Sun 25 Oct)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B3-1 | B · MUST | Caplet XR is used and ties to the team name | "'Caplet XR' is an exceptionally clever name. It's hyper-specific to our team (hence justifying our team name ...)" | Does "Caplet XR" appear (E18)? |
| B3-2 | I · AIM | XR has more dimensions | "the way that you extend it (releases at a certain time, do not crush; I'm sure you could come up with some more dimensions of this!) is VERY effective" | Superseded in part by Ray I85 (E1): are its dimensions now non-medical? |
| B3-3 | I · AIM | A second meaning that sounds like a real investing plan | "You could even come up with ANOTHER potential meaning of the acronym 'XR'"; "label it as something that would sound like a real investing plan" | Is "X = ten, R = redemption" present (E3)? |
| B3-4 | B · MUST | Flair over hedging; overclaim a little, never actively | "We're humans. We DO overclaim a little bit. The problem with AI is that it ALWAYS hedges"; "We want FLAIR. We want VOICE."; "I'm not asking you to ACTIVELY overclaim" | Are true claims said boldly, with no claim beyond the facts? |
| B3-5 | I · MUST | Written for competition judges, not mini-Lauras | "The judges aren't robots who are literally just programmed to do whatever Laura would do ... They're trying to figure out who has the greatest investing knowledge and the best investing strategy." | Is the text aimed at expert judges (mechanism, trade-off, knowledge), not at reassuring Laura (E11)? |
| B3-6 | R · MUST | No time spent on grammar; en dashes stay | "The third is grammar and punctuation and spelling. Just don't waste your time on that. En dashes are correct in Australia and we're going to use them." | Are there no grammar or punctuation findings, and are no en dashes "fixed"? |

### Book 4: rewrite from scratch, and the fourth north star (Ahaan, Mon 26 Oct)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B4-1 | B · KILL | A real rewrite that carries every macro expectation | "A little bit of chopping and changing won't cut it because I've prescribed some macro expectations for the IPS. And I want to see them all implemented." | Is it new writing rather than a reworded V57 or V58 (B12-2)? |
| B4-2 | I · KILL | Extraordinary investing knowledge: a wide range of concepts, niche ones included, applied to build our own plan | "demonstrate truly extraordinary knowledge of investing concepts and strategies"; "applying and explaining a wide range of investing concepts – including potentially niche ones! – and strategies to formulate our own" | Are at least three concepts (at least one niche) each explained in plain words, tied to Laura, and doing work? |
| B4-3 | I · KILL | No name-dropping | "That doesn't mean rapid name-dropping, of course, because that'll just harm our score. Futile." | Is every concept that is named also explained and used, with no list of names and no authors? |
| B4-4 | I · MUST | Used uncited in the IPS and cited in the Final Report | "some can still be used without citation, and instead cited in the Final Report as is appropriate" | Is the IPS uncited, and does the note route each concept's sources to the Final Report? |
| B4-5 | I · MUST | Knowledge supports the narrative and our own case-tailored strategy, never replaces them | "It should SUPPORT and ENHANCE, rather than replace or undercut, the rest of the aspects of our IPS"; "mustn't come at the expense of our actual narrative, nor our ability to express a clear strategy of our own" | Is the strategy clear without the concept names, with the concepts strengthening the reasons? |
| B4-6 | I · MUST | All four north stars are present and equal | "Please don't put this new North Star ahead of all the other ones ... and equally, don't MINIMISE this one ... They are all equal." | Are voice, motif, the extraordinary and knowledge all present? |
| B4-7 | I · AIM | Dazzling | "We want to see something dazzling, something extraordinary, something exceptional" | Would a judge remember it a day later? |

### Book 5: Caplet XR locked; stop hedging; be extraordinary (Ahaan, Mon 26 Oct)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B5-1 | B · KILL | Keep Caplet XR | "Caplet XR is a brilliant name; let's stick with it." | Is the plan's name Caplet XR (E18)? |
| B5-2 | I · MUST | X = 10 | "with 'X' as '10' (which, by the way, is surely going to have to be the most genius name idea of any team ...) definitely keep this meaning" | Does X stand for ten? |
| B5-3 | B · KILL | R is never "release" | "'10 releases' is quite frankly just a weird name for an investing strategy, so please come up with something – literally ANYTHING – else" | Is R = redemption, with the word "release" never used as R's meaning? |
| B5-4 | I · MUST | The name is shown to be clever and thought out | "We've got to make it clear that we've got a clever and thought-out name." | Does one decoding sentence make a judge see why the name fits? |
| B5-5 | I · MUST | Both meanings of XR somewhere; bare bones of the motif in the IPS | "Obviously mention the literal 'extended-release' meaning somewhere in either the IPS or the Final Report or both"; "As long as you include the bare bones of the extended metaphor motif" | Is our meaning in the IPS, and is the literal meaning either in the IPS without medicine imagery or routed to the Final Report in the note (E2)? |
| B5-6 | B · MUST | No fretting over sure words: Treasuries are exact, the fixed-date funds near-ironclad | "it is factually correct to say that iShares iBonds Term Treasury ETFs are as close to guaranteeing an exact amount at an exact date as it gets"; "the iBonds can also be described as 'near-ironclad'" | Is the certainty language for Treasuries and the funds strong and true, never softened? |
| B5-7 | I · MUST | Any distinction between bond and fund is one direct clause | "if you do choose to do so, it should be concise and direct rather than 'nuanced' as you so often have a tendency to do" | Is the distinction, if made, a single clause? |
| B5-8 | B · KILL | Accuracy still matters | "To be clear, accuracy is important, and I'm not asking you to stop looking for inaccurate or exaggerated statements." | Is every factual claim true (D16, D22)? |
| B5-9 | B · KILL | No hedging or "safe" language | "hedging and 'safe' language is a classic habit of AI – one which is instantly recognisable to judges looking for real authenticity" | Is it free of "may", "might", "potentially", "could help to" on any fact the plan controls? |
| B5-10 | B · MUST | A human voice, not a robotic one | "use my voice and style and tone and employ that as your own in the report rather than using your generic and frankly annoyingly robotic AI voice" | See E9 |
| B5-11 | I · KILL | Extraordinary above all | "there's only one real rule above all else. Both our IPS and our Final Report must be truly, exceptionally, stunningly, breathtakingly, extraordinary." | Do the B12-14 checks pass? |
| B5-12 | I · AIM | Distinctive, unique, novel, original, unexpected, insightful, thoughtful, cerebral, erudite, clever | "We have to be distinctive and unique and novel and original and unexpected and insightful and thoughtful and cerebral and erudite and clever!" | Can a reviewer point to a line for erudite, clever, unexpected and insightful? |
| B5-13 | B · MUST | Every expectation met | "We want you to meet EVERY SINGLE EXPECTATION we've set out throughout the entirety of this conversation. Blow us away." | Does it pass every KILL and MUST row on this page? |

### Book 9: intelligence, synthesis, logic; every good idea lands (Ahaan, Tue 27 Oct)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B9-1 | I · KILL | Meets Wharton's requirements; the IPS has one specific job | "Ensure that your IPS meets all of the requirements and expectations set out in that attachment ... the IPS actually has a VERY specific and defined job." | Do all of Part A's KILL and MUST rows pass? |
| B9-2 | R · MUST | No time on formatting | "stop focusing on the formatting requirements of the IPS – that DOESN'T MATTER" | Are there no formatting findings beyond the word limits? |
| B9-3 | I · KILL | Seen as intelligent and knowledgeable through niche strategies | "it's absolutely vital for the judges to see us as INTELLIGENT and KNOWLEDGEABLE"; "existing investing strategies, including those which 99.9% of students our age and indeed investors don't know about" | Is at least one strategy or concept one that most investors wouldn't know, used correctly? |
| B9-4 | I · KILL | Synthesis: borrowed ideas fused into our own | "We can fuse together two completely different niche strategies. We can synthesise dozens of ideas to formulate our own ... We need SYNERGIES" | Does at least one move fuse two borrowed ideas into something neither offers alone? |
| B9-5 | I · KILL | Borrowed ideas are critiqued, not dumped | "don't uncritically dump them into our report. Analyse them. Evaluate them. Critique them."; "it might initially seem relevant to our case but really it's not, and here's why" | Is at least one borrowed idea's blind spot or cost named, and at least one tempting idea turned down with its reason? |
| B9-6 | I · MUST | Our own strategy, unique to our client | "our ability to create our OWN strategy, unique to OUR client and OUR context and situation" | Would the plan make sense for no other client? |
| B9-7 | I · KILL | Logic: causal chains taken to their conclusion | "LOGIC. Analogies, thought experiments, causal chains, logical deduction (including taking a strand of reasoning all the way to its logical conclusion – which can land us in unexpected places ...)" | Is there at least one chain of "which means" that lands somewhere unexpected and true? |
| B9-8 | R · MUST | Voice is judged qualitatively, by ear, not by counts | "voice and style and tone are fundamentally qualitative"; "That's the problem with your analysis of tone. It's far too quantitative." | Did the review judge the voice by reading, with no count used as a gate? |
| B9-9 | R · MUST | The Wall Street writers matter as much as Ahaan's essays | "don't use my essays exclusively ... the funny or eccentric finance gurus of Wall St – but the latter are very useful as well" | Do the voice checks draw on the reading log as well as the essays? |
| B9-10 | R · MUST | Only real web detectors; Keel's agents never stand in | "Rather than getting your own agents to guess these things, outsource it." | Is no agent-made AI score reported (D6)? |
| B9-11 | B · MUST | No anchoring on 7.5% for VT | "you keep obsessing over JPMorgan's 7.5% figure for VT. You don't have to use it." | Is it free of 7.5% (A47)? |
| B9-12 | I · AIM | Not hamstrung by the TNA's content: go further, never against it | "You can go deeper, you can go further, you can do whatever you want. Don't feel hamstrung by what we wrote in the TNAs." | Does it go beyond October's reasoning while passing A36-A48 (E20)? |
| B9-13 | I · AIM | Niche studies and evidence are welcome | "If you're going to use studies or evidence such as that, that's absolutely BRILLIANT" | Narrowed by Book 11 (E8): does a study's finding appear only as plain reasoning, with no numbers or names? |
| B9-14 | I · AIM | Turn findings into arguments | "you've realised something about our plan, and you want to construct an argument around it. This is the kind of pick-up which could genuinely be useful." | Does the argument stand on logic and the case's words, with no model number (E7)? |
| B9-15 | R/N · MUST | Every good idea lands in the IPS or the Final Report | "Every single good idea you have, like these, must end up in either the IPS or the Final Report or both."; "definitely don't just throw ideas out wantonly" | Does each strong idea from the ledger and tonight's harvest have a destination? |
| B9-16 | P · KILL | The pitch is cut the human way | "your elevator pitches FEEL noticeably more AI to me than your actual reports"; "If you really need to cut, cut the HUMAN way, not the AI way." | Read across a table, does the pitch sound like a seventeen-year-old talking, in full sentences with verbs and small words? |
| B9-17 | B/N · MUST | No AI-use fretting or logging | "you don't need to keep obsessing over what was written or reviewed or inspired by AI ... Trust us." | Are both the text and the note free of AI-use logs, warnings or questions? |
| B9-18 | I · MUST | Big picture, not minutiae | "you seem to be too focused on making minute changes ... a small addition to the specific trades we're going to be making in a decade's time"; "They're interested in the big picture." | Is it free of trade-level detail for future years? |
| B9-19 | R · MUST | Judges are human and don't read for word-level precision | "they're also not checking word-for-word whether we've used the exact most precise and technically correct word ... They're humans, not robots." | Is no finding about precision of wording, unless the claim is false? |

### Book 10: judges who disagree, a voice applied, overdrive (Caplet, Fri 30 Oct, 18:15 and 18:21)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B10-1 | R · MUST | Mock judges who genuinely differ | "You've got to create judges that are diverse not just in label but in their evaluations, and who make judgements in vastly, indeed radically different ways." | Does any panel used tonight show disagreement in substance (Commandment IX)? |
| B10-2 | B · KILL | The voice studies are applied, not filed | "I'm not sure you've adopted much from all the 'voice studies' you've supposedly been doing"; "you're simply not applying them" | Can the reviewer quote where at least three voice-guide moves happen (D3)? |
| B10-3 | P · KILL | The pitch must not read as obvious AI | "The elevator pitch is even worse: it's so obvious it's AI, it's kind of concerning." | Read aloud, does it pass B9-16? |
| B10-4 | N · MUST | GPTZero "human-written only" above 50% before Caplet sees it, or the note says it wasn't checked | "every time after you've produced an IPS draft, and before you send it to us, you MUST run it through GPTZero, and the 'human-written only' probability must be above 50%" | Does the note give the score, or say plainly "GPTZero: not yet checked" and ask a student to paste it (D6)? |
| B10-5 | B · MUST | Our own voice matters more than the score | "what's even more important is HAVING OUR OWN UNIQUE VOICE" | Is the voice judged on its own merits, not tuned to a detector? |
| B10-6 | B · KILL | No sentence is so compressed it barely makes sense | "this is beginning to be so excessive that the sentences barely make sense"; "such an extreme level of parsimony ... without any natural human variation or flair or whatever, is a classic AI tell" | Does a cold reader understand every sentence on first reading? |
| B10-7 | R · MUST | Mark only against Wharton's guide; no pet lines | "Your only allegiance in terms of marking is to the marking guide from Wharton, and ABSOLUTELY NOTHING ELSE." | Does every score in a review cite a criterion (E25)? |
| B10-8 | B · KILL | No comparisons with other teams | "referring to things like 'every team will do x' is a bit meta and also a bit arrogant" | Is it free of "every team", "most teams", "other teams", "a typical plan" and "many strategies"? |
| B10-9 | B · KILL | No arbitrary numbers; a model's output is never "we judge" | "don't just randomly throw out lines like 'which we judge three times worse'"; "it's not 'we judge', it's 'we model' or 'we calculate'" | Is it free of unexplained multipliers, ratios and probabilities (E7)? |
| B10-10 | B/N · MUST | No AI-use or "required trading activity" fretting | "can you stop obsessing over random things like AI use?"; "'required trading activity' doesn't mean anything which would contradict our plan" | Is neither topic raised? |
| B10-11 | I · KILL | Not ordinary | "Right now, the IPSs still seem ordinary. Competent, impressive, but not creative, original, novel, thoughtful or insightful, let alone EXTRAORDINARY"; "That's your number one instruction, above all else." | Would the reviewer call it extraordinary, with its three retellable ideas named (D1)? |
| B10-12 | R · MUST | The commandments are followed, not decorative | "it MUST BE FOLLOWED. Right now, they exist for decoration" | Is the check filled with evidence by a reader who didn't write the draft (D11)? |
| B10-13 | R · MUST | Recursive self-improvement: guess what Caplet would say, and fix it first | "You should be able to GUESS what I'm thinking and already have it covered"; "take initiative, take intellectual risks" | Does each round's log hold a "what they'd say next" entry, and does the next draft act on it? |
| B10-14 | R · MUST | No idea from any version is lost; the best ones reach the IPS | "keep a list of every single idea you had in every single version of your IPS and ensure that all of the best ideas end up in the new IPS" | Is the draft checked against `IDEA_LEDGER.md` and tonight's harvest? |
| B10-15 | B · KILL | The final IPS meets every expectation | "Your final IPS MUST satisfy ALL of our expectations." | Does it pass every KILL and MUST row? |
| B10-16 | R · MUST | Wharton's useful words treated with the utmost importance | 18:21: "the stuff that is useful must be treated with the utmost importance" | Was Part A scored in full? |

### Book 11: V49 rejected (Ahaan, Sun 1 Nov)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B11-1 | B · KILL | No opening rhetorical question (safest reading: no question mark at all) | "Opening with a rhetorical question is not only the corniest and most cringeworthy thing I've ever seen – it's also anathema to the nature and style and form of this competition." | Is there no "?" in either box (E14)? |
| B11-2 | B · KILL | No "our model", model outputs, probabilities, simulations, evidence or citations; the IPS is strategy | "why are you referring to 'our model'? ... That's the sort of thing you absolutely can't be doing. Save all those details for the Final Report."; "they're looking for the strategy, the 'how' and the 'why', not the models and the citations." | Is it free of "model", "simulat", "paths", "in N of 100", percentiles, backtests and study statistics? |
| B11-3 | B · KILL | No past plans or team progression | "stop making references to past plans like 'We know this rival because we built it first ...' What on Earth?"; "we're supposed to explain our investment strategy in the IPS. Not our team progression." | Is it free of "originally", "we first", "our earlier plan", "we used to" and "we changed our minds"? |
| B11-4 | I · KILL | A full-circle motif: set up in the introduction, paid off in the conclusion | "the really clever way that you employed the extended metaphor / motif of 'Caplet XR' as a full-circle thing between the introduction and conclusion"; "You've banished it to only the conclusion, which eliminates the whole point" | Does the motif appear near the start and return in the last paragraph, with a payoff that needs its set-up? (Modified by Ray I84-I85: E1) |
| B11-5 | I · MUST | A payoff is never left without its set-up | "the 'do not crush' reference makes no sense anymore. The only reason it made sense in the earlier versions was because you stated in the introduction ..." | Does every callback in the close point to something the opening actually set up? |
| B11-6 | B · KILL | No subheadings; take Ahaan's voice, never his essay structure | "who knows why you're using subheadings. Probably stolen from my essay structure ... yes, of course you ought to adopt my VOICE and STYLE and TONE, but that doesn't mean you adopt my STRUCTURE." | Is it continuous prose, with no headings, pun titles or header-like one-line paragraphs? |
| B11-7 | B · KILL | Every sentence makes plain sense to an ordinary reader | "half of your sentences just DON'T MAKE SENSE"; "a human simply cannot understand what you're trying to say" | Does a cold reader paraphrase every sentence correctly (D4)? |
| B11-8 | B · KILL | No sentence with two plausible meanings or missing context | "what does 'we built it first' mean? Presumably it means 'that was our original plan', but [a] it could mean something else too" | Does every "this", "that" and "it" have one clear referent, with no shorthand that assumes Keel's context? |
| B11-9 | B · KILL | Stop over-compressing | "your extreme obsession with parsimony and concision and brevity in using as few words as possible, to an extent which is deeply unnatural" | Does no sentence drop the words a person would say aloud? |
| B11-10 | B · KILL | Sound human; know your own fingerprints | "You're sounding more AI than ever"; "How hard can it be to figure out the fingerprints in your own writing" | Is it free of every habit in C2 and D36? |
| B11-11 | B · MUST | No lines or styles copied from elsewhere that don't fit here | "you're trying to copy lines and styles which don't work in this context, yet keeping your own style for everything else" | Is it free of sentences that sound lifted from a famous writer or styled as an essay flourish? |
| B11-12 | R · MUST | Wharton's guidelines read and followed | "If you'd actually bothered to take a look at Wharton's guidelines (which we explicitly gave you and told you to pay great attention to) ..." | Does Part A pass? |
| B11-13 | R · MUST | Absolute overdrive; attention to every Bible message | "learn to PAY ATTENTION to what I say in Bible messages"; "at least orders of magnitudes more" | Does the round log show volume and every book checked? |

### Book 12: the absolute final IPS, overnight (Caplet, read as Ahaan, Thu 5 Nov, 22:50)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| B12-1 | B/N · KILL | Truly final: no gaps, holes or open revisions | "There should be no more gaps and no more holes and no more revisions required by the time I take a look tomorrow morning." | Is it free of placeholders, brackets, alternatives, "[NAME]" and unresolved choices in the text? Does the note offer at most a few plain yes/no calls that only students can make? |
| B12-2 | B · KILL | Rewritten from scratch; every old version is inspiration only | "Over the next 12 hours, I want you to entirely rewrite the full IPS from scratch. You will use every single version you've generated so far as just inspiration and nothing more than that." | Is every sentence new writing, with no light edits of V57 or V58 sentences (ideas may return; wording may not)? |
| B12-3 | R · MUST | The best bits of each old version are found and the worst critiqued | "You will read through every single one of them and find the best bits of each and critique the worst bits" | Does the harvest name both for V1-V58? |
| B12-4 | B · KILL | The rooms' unused good ideas are harvested | "a lot of your rooms ... had thousands of good ideas which you just completely ignored or forgot about and clearly did not implement in the IPS. This is shameful." | Is each of the harvest's strongest unused ideas in the draft, or routed with a reason? |
| B12-5 | B · KILL | The generic AI voice is dead; the voice studies come first | "You're going to completely kill your generic AI voice and specifically train yourself using all of the voice studies which you did (and which you completely failed to actually use)" | Do the voice-guide moves (D3, D27-D38) visibly happen? |
| B12-6 | B · MUST | Ahaan's writing is a small secondary pointer, and the text mustn't sound like a generic human either | "this is very much secondary to the voice studies – my voice isn't as good; it's just a small guide in a certain general direction of tone ... so that we don't sound like generic HUMANS" | Does it have a voice of its own, rather than a bland "competent student" register (E9)? |
| B12-7 | I · KILL | The first paragraph carries strategy, not a summary of the case | "spending the whole first paragraph just summarising the case (as you have in v57) is the most stupid use of scarce word count I've ever seen. Please use your brain." | Does the IPS's first sentence state the central idea? Is no paragraph's job to restate the case? (V57 and V58 both open on a case summary.) |
| B12-8 | B · KILL | Not maximum parsimony at all costs: cut whole ideas, never chop words | "don't aim for maximum parsimony at all costs ... Cut things whole, don't chop and snip words here and there to maximise parsimony and concision and brevity" | When the draft went over the limit, was a whole idea dropped rather than words snipped? Is there no squeezed sentence? |
| B12-9 | B · KILL | Every sentence is normal, comprehensible human English | "I swear I literally can't understand half of the sentences in the IPS, because they just don't sound normal or human, let alone being comprehensible by a human. This is genuinely a diabolical situation." | Does a cold human-proxy reader understand 100% of sentences? |
| B12-10 | B · MUST | Every word earns its place; use your brain | "Also just use your brain a little bit" | Is it free of any sentence a judge would skip, and of words repeated between the pitch and the IPS's opening without a reason? |
| B12-11 | R · MUST | Everything read first, then every Bible word, held in mind while writing | "Before you begin writing, you are going to read through every single thing you've produced so far ... And after that, you're going to read through every single word of every single one of the Bibles" | Does the writer's log show the reading done before round 1? |
| B12-12 | R · KILL | One writer for the whole thing | "you're not going to have different parts of Keel writing different bits. There's going to be a single person or agent ... which writes the entire thing." | Is every sentence in the draft the writer's own, with no reviewer-supplied wording pasted in? |
| B12-13 | R · MUST | Review against (a) the books, (b) Wharton, (c) brilliance; then rewrite, many times | "there's going to be a review – against (a) every single one of my expectations ... (b) Wharton's marking guidelines, and (c) just simply being AS BRILLIANT AS POSSIBLE ... And you're going to undergo this process many, many times" | Are there several logged rounds, each with all three passes and a rewrite? |
| B12-14 | I · KILL | Brilliance: extraordinary, erudite, creative, distinctive | "(truly extraordinary, stunning, breathtaking, exceptional; erudite, intellectual, cerebral; creative; distinctive, unique; etc.)"; "it should blow the judges away and absolutely stun them and impress them, leaving them to marvel at our sheer brilliance" | Can the reviewer point to a line for each family: erudite, creative, distinctive? Would a judge "marvel"? |
| B12-15 | I · KILL | Erudition: Damodaran's lectures, Yale ECON 252 and far beyond; ideas analysed in the context of the case to build our own | "demonstrating our breathtaking level of knowledge of investing strategies and concepts and analysing a range of different such ideas in the context of the case to formulate our own. Make sure to do so, no matter what." | Are several concepts used, each judged for fit, at least one turned down for a reason, all fused into our plan? |
| B12-16 | I · MUST | Hazards from the pasted list stay out (source material, "quite generic, or designed for other strategies") | Book 12: "The majority of them are not relevant to our specific strategy"; Keel's note: its "Roots", "Canopy" and "Branch" labels are banned | Is it free of: Roots/Canopy/Branch/Ballast labels; STRIPS or "zeros"; options, puts or collars as holdings; CPPI or a multiplier rule (we refuse portfolio insurance); D/E leverage maths, distance-to-default, 2.33, Brier scores, probabilities; "most teams will never compute it"; the "Mission line" slogan; committees, quorums and 48-hour cooling-off rules not in the case; traffic-light dashboards? |
| B12-17 | R · MUST | Volume: provably more work tonight than in the whole project | "You need to be able to prove to me that you have done more work over the next 12 hours than throughout the entirety of the project so far" | Does the round log record the volume? |
| B12-18 | R · MUST | Nothing but the IPS tonight | "no more regular runs of the Keel rooms and so on. Absolutely nothing but explicitly working on the IPS" | Is all logged work tonight IPS work? |

---

## C. Ray's later rules (and his earlier standing ones)

| ID | Applies · Weight | Expectation | Source (verbatim) | Test |
|---|---|---|---|---|
| C1 | B · KILL | Not AI-sounding and not corny, in tone, phrasing, syntax and taste | I80 (3 Nov): "The writing reads as AI and corny: tone, phrasing, syntax, taste, not the content." | Would Ray, reading it aloud, call any line corny? |
| C2 | B · KILL | Ray's eight AI habits are gone | D35 README: "Slogan flips"; "Two-word kickers at the end of a paragraph"; "'That is X.' staccato"; "Announcing instead of saying"; "Stilted asides" ("That, to us, is what ..."); "Aphorism openers"; "Metaphor explained twice"; "One-line final paragraph"; "The rule underneath all of these: a human paragraph explains and then stops. It does not wind up for a punchline." CLAUDE.md: "no slogan flips, no two-word kickers, no 'That is X.' runs, no one-line endings" | Is it free of each of the eight? Does every paragraph end on its last real point? |
| C3 | N · MUST | Anything written for Caplet is one page of plain English with no internal labels | CLAUDE.md: "Anything written for Caplet is one page of plain English, no internal labels (rooms, beats, huddles, L-/H-/A- codes)"; I80 Window breach: the FINAL note "uses internal codes (I81, Book 11, V56i, S01, Commandments by Roman numeral, folder names)" | Is the note one page, with no room names, codes, version numbers, Roman numerals or folder jargon? |
| C4 | N · MUST | Easy to follow; no overcomplicating | I80: "Keel overcomplicates things and is hard to follow. Show the milestones and the best ideas plainly." | Can a student say, after one read of the note, what changed and what they must decide? |
| C5 | B/N · KILL | Every claim holds on the page; no "if a judge asks" | I82 (4 Nov): "BAN 'be ready to defend it', 'if a judge asks', 'in your own words if pushed' analysis. Nobody gets to answer a judge before the semifinal; the Top 50 is picked on the written work alone." | Does no claim depend on an explanation that isn't in the text? Is the note free of anticipated judge questions? |
| C6 | B · KILL | No invented terms; the case's words or plain English | I83 (4 Nov): "do not invent terms, like floor". Case words: "operating commitment, operating payments, operating reserve, facility contribution, credible range, co-sponsors, high degree of certainty, financial flexibility"; banned coinages: "floor", "building gift", "cheques", "promises" | Is it free of all four? Is every label either a case word or plain English? Is any term of art (such as "ladder") explained by what it is the first time it appears? |
| C7 | I · KILL | Creativity is intellectual, in the strategy and the reasoning, not packaging | I84 (5 Nov, 19:09): "metaphors alone does not count as creativity. We want intellectual creativity, yours just packaging." | Delete every figurative line: does the draft still look creative? Are the three retellable ideas (D1) all strategy ideas? |
| C8 | B · KILL | No rehab or medicine imagery; Laura is not a patient | I85 (19:10): "if you say our strategy is like calculate XR it feels like we're helping Laura for a rehab, but she doesn't need any rehab." | Is it free of tablet, pill, capsule, dose, crush, pharmacist, prescription, label (as on a pill), treatment, patient, cure, remedy, side effect, and "extended release" framed as medicine? |
| C9 | B · KILL | No "do not crush" | Ray, 19:08: "What does do not crush even mean? it sounds so corny." | Is the phrase absent, with any payoff of it absent too? |
| C10 | I · KILL | One strategy, its biggest strength, and why it is very strong, in one connected argument | I86 (21:05): "Your analysis is kind of fragmented. So convince our strategy is the best. So explain what our strategy is. What is the biggest strength our strategy? After all this work, why do you think our strategy is very, very strong?" | After one read, can a reader name the single biggest strength, and does every paragraph serve it? |
| C11 | I · MUST | It convinces: ours is the best plan for Laura | same | Does it argue against at least one serious alternative plan, in that plan's best form, and show why ours serves her better (E12)? |
| C12 | I · KILL | The most creative idea is evident and central | I86 (21:09): "so what is most creative?" | Is the most creative idea in the pitch and in the IPS's first paragraph? |
| C13 | I · MUST | Emotional appeal for Shark Tank judges, not examiners | I50 (27 Oct): "you gotta have emotional appeal man. Judges are not examiners ... judges are shark tanks"; a hook, real stakes, a reason to care about the residency, confidence in us | Is the first line a hook made of strategy, and are the real stakes from the case felt once (E24)? |
| C14 | I · MUST | Not "just telling facts" | I47 (27 Oct): Keel's writing "is just telling facts ... like eating plastic" | Does each paragraph argue an idea, with no paragraph that is a fact sheet? |
| C15 | R · MUST | Never soften a confident claim | Ray, 23 Oct, rejecting 13 softening edits: "clearer, but it would soften our voice" | Is no review finding a hedge or a softer synonym (reviewer rule 4)? |
| C16 | B · MUST | Expression, not only content | I55 (27 Oct): "you are not looking for content and knowledge ... you express it poorly" | Does the expression itself earn praise from a cold reader? |
| C17 | I · MUST | The computer models go to the Final Report | I52 ("i want more COMPUTER MODELS") narrowed by Book 11 | Is there no model content in the IPS (B11-2)? |
| C18 | R · MUST | Stop Slop is not yet a gate on drafts | Ray, 5 Nov, 20:05: "I am not asking you to use stop slop yet, let me have the skill in claude first globally." | Was no draft finding raised only because the Stop Slop skill says so? (Its overlap with C2 and D36 is covered by those rows) |

---

## D. The Ten Commandments and the standing rules

### D.1 The Ten Commandments (30 Oct; enforced; "One fail = the draft is not sent")

| ID | Applies · Weight | Commandment | Source test (verbatim) | Test |
|---|---|---|---|---|
| D1 | I · KILL | I. Be extraordinary, by our own light | "name the three ideas a judge would retell tomorrow; none may be the field's default (a payment ladder plus stocks plus a lock)" | Are three such ideas named, and is none of them the default or a comparison with other teams? |
| D2 | R · KILL | II. Wharton's word is the only marking scheme | "every review argues from criteria, not from favourite lines" | Does each review finding cite a criterion or a row on this page? |
| D3 | B · KILL | III. Write like us, never like a machine | "full sentences with the small words kept; a sentence that builds and a short one that lands; a concession and then 'But'; a wry line; contractions; British spelling; en dashes. No slogans, no triads, no fact-sheet runs."; "read aloud, nothing sounds like a brochure" | Can the reviewer quote the line for each move: a build-then-land pair, a concession followed by "But", a wry line, contractions? Is it free of slogans, reflex triads and fact runs? |
| D4 | B · KILL | IV. Clear on one reading | "A smart adult who knows the case understands every sentence first time. When over the limit, drop a whole idea; never squeeze a sentence into code. No term (ladder, floor, rung) before it is introduced."; "a cold reader on a small model paraphrases every paragraph" | Did a cold small-model reader paraphrase every paragraph correctly? |
| D5 | B · KILL | V. Every number explains itself | "Each number says what it is and where it came from"; "Never 'we judge' for a model's output; no bare multipliers." | Does every number answer "says who?" in its own sentence: the case, our rule, or a dated public fact (E7)? |
| D6 | N · MUST | VI. GPTZero before Caplet | "If GPTZero can't be reached, the draft is labelled 'not yet checked' and Keel says so; Keel never stands its own agents in for a detector." | Does the note carry the score and date, or "not yet checked"? |
| D7 | I · KILL | VII. Few ideas, at full size | "The IPS argues a handful of big ideas well rather than every mechanism briefly"; "after one read, a judge can say the strategy in three sentences" | Can a cold reader say the strategy in three sentences? |
| D8 | I/R · MUST | VIII. Lose no idea; critique every borrowed one | "Each concept used is explained plainly, fused into our own plan and critiqued (what it misses, what it costs us)." | Does each concept used carry its cost or blind spot, and was the draft checked against the ledger? |
| D9 | R · MUST | IX. Judges who actually disagree | "A mock panel differs in method, priors and model, not in name; it reads blind" | Does any panel used tonight report its disagreements? |
| D10 | R · MUST | X. Improve without being asked | "After each round Keel writes down what Caplet would most likely say next, and fixes it before they say it"; "No time on AI-use citations, 'required trading activity', grammar or formatting" | Does each round have a "what they'd say" entry, with the fix visible in the next round? |
| D11 | R · KILL | The check is real | "every draft's README carries a filled ten-line check ... written by a reader who did not write the draft. A draft with a failed line does not go to Caplet."; COMMANDMENTS_CHECK: "A line that says 'pass' with no evidence counts as a fail." | Is the check filled with evidence by a non-writer? (It lives in the record, not in the one-page note: E27) |

### D.2 The standing rules

| ID | Applies · Weight | Rule | Source (verbatim) | Test |
|---|---|---|---|---|
| D12 | B · KILL | Caplet XR: X = 10; R = redemption, never "release" | Commandments "Standing": "Caplet XR is the name (extended release; X = 10; R = redemption, never 'release'), subtle, never in every sentence, nothing roots-themed." | Is it decoded exactly that way? |
| D13 | I · MUST | "Redemption" is plainly the bond sense | BIBLE_AUDIT row 32: "The cold reader took 'redemption' as a moral word" | Does the text make clear that redemption means the day a Treasury repays a bond (E26)? |
| D14 | B · KILL | No hedging; Treasuries held to maturity and the funds held to their December close are said with confidence | Standing: "No hedging: iBonds held to their December close are near-ironclad." I35: "as close to exact sums on exact dates as it gets" | Is every certainty statement strong and true (E10)? |
| D15 | I · MUST | Judges are competition judges, not mini-Lauras | Standing: "Judges are competition judges, not mini-Lauras." | See B3-5 |
| D16 | B · KILL | Real facts and real team events only | Standing: "Real facts and real team events only."; CLAUDE.md: "Wharton ethics: no invented teamwork or experience stories" | Is every factual and historical claim true, and are there no invented events? |
| D17 | N · MUST | The draft is labelled AI DRAFT outside the pasted text | CLAUDE.md: "Label each draft `AI DRAFT (Claude, <date>)`; the team rewrites it in its own words before submitting" | Does the note or file header carry the label, with none inside the boxes? |
| D18 | N · MUST | Times in Sydney first | CLAUDE.md: "state them in Sydney time first (the team is in Sydney), ET in brackets" | Is every time in the note given in Sydney time first? |
| D19 | B/N · KILL | No personal data | CLAUDE.md: "Never commit personal data"; memory: the IPS Report doc header "lists students' names and the WInS username: never copy it" | Is the draft free of surnames, usernames and emails? |
| D20 | B · MUST | The voice is shown, never claimed; no glossy praise of the plan | NORTH_STARS: "Voice is shown, never claimed. No sentence calls the team witty, bold or unique; the sentences are."; VOICE.md tell: "Glossy praise of the plan ... 'an elegant, robust, well-diversified solution'" | Is it free of self-praise words for the plan or the team (elegant, robust, innovative, unique, powerful)? |
| D21 | I · KILL | The "aha" is a true insight, not a flourish | NORTH_STARS: "'Aha' is a true insight, not a flourish. It must survive Kai's 'who says?' and Felix's 'where does it say that?' ... A genius line that is false is the fastest way out of the competition." | Does the aha survive a fact check at source? |
| D22 | B · KILL | Concepts are named for what they are | BIBLE "Kept, because it is accuracy": "a static floor plus a cushion is not CPPI; a cash-flow-matched ladder is not immunisation), and stocks are never called sure" | Is no concept mislabelled, and are shares never called safe over time? |
| D23 | I · MUST | A borrowed finding says only what its evidence shows | Kitchen check, 5 Nov: "the overhead study measured the cost of raising money, not running costs; the crowding-out figure is 75% in the published 2011 paper" | Does any finding used in the plain words stay inside what the study measured? |
| D24 | I · MUST | Ideas are a scalpel mapped to the criteria | I26: "ideas are a scalpel mapped to the judging criteria" | Does every paragraph serve at least one Wharton question or criterion? |
| D25 | N · MUST | Keel proposes; Caplet decides its own calls | CLAUDE.md: "Keel proposes, never decides."; danger-zone decisions "wait for a student" | Are the students' calls (the name, the literal XR meaning, the last sentence) offered as choices, not made silently? |
| D26 | R · MUST | The office's process rules for the night | CLAUDE.md: "No work is finished until the portal shows it"; Book 12 suspends room runs | Once the coordinator publishes the final, is it logged in `pm/CHANGES.md` and VERSIONS? (The coordinator's job; not the writer's) |

### D.3 The voice guide's laws and VOICE.md's tells (judged by ear, never as counts: Book 9)

| ID | Applies · Weight | Law or tell | Source (verbatim) | Test (by ear) |
|---|---|---|---|---|
| D27 | I · MUST | Find the idea before the sentence | Law 1: "Can I say this paragraph's idea without a number or a ticker?" | Can each paragraph's idea be said without a number? |
| D28 | I · MUST | Give a paragraph an opponent | Law 2: "Who disagrees with this paragraph, and did they get to speak?" | Is at least one fair opponent voiced in the IPS? |
| D29 | B · MUST | Build long, land short | Law 3: "Prose where every sentence is the same middling length reads like a form." | Does one sentence carry the reader through a mechanism, and does one short one land it? |
| D30 | I · MUST | Mechanism before label | Law 5: "The toy explanation first. A jargon word only after it, or never"; "Would a smart 14-year-old follow it?" | Does every concept come after, or with, its plain mechanism? |
| D31 | I · MUST | One image, which argues; nothing competes with it | Law 6: "If I delete the image, does the logic break? If not, delete it." | Is there at most one image, and does it argue? |
| D32 | I · MUST | One real limit, admitted plainly | Law 7: "One real confession or limit per piece"; F3: "Accept a cost in public" | Is the plan's one real weakness stated flat, with what it costs and how it is covered (E13)? |
| D33 | B · MUST | Strong words stay strong | Law 8: "A word is wrong only if it is false; then replace it with an equally strong true claim." | Was nothing true softened? |
| D34 | I · MUST | Spend kickers like money | Law 9: "At most 3 in the IPS"; "More than 3 in 500 words is a stand-up set." | Is the number of quotable paragraph endings small, with none bolted on (E16)? |
| D35 | B · MUST | Ration symmetry | Law 10: "'X, not Y' and neat mirrored pairs are where AI hides when it has no argument" | Is each mirrored pair a real turn of thought rather than a rhythm? |
| D36 | B · MUST | VOICE.md's AI tells | "Throat-clearing"; "Fancy verbs" (delve, navigate, leverage, underscore, foster, unlock); "Scenery words" (landscape, realm, journey); "Not only… but also"; "Rule-of-three by reflex"; "Tidy summary closer"; "Hedging stack"; "Empty intensifiers" (crucial, vital, key, robust, seamless, truly); "False balance"; "Colon reveal / hook"; "Passive committee"; "Signpost bloat" (Furthermore, Moreover, In conclusion); "Synonym cycling"; "Never the em dash (—)" | Is it free of every one? |
| D37 | B · AIM | The read-aloud questions | Guide s5: "Is there a sentence only Caplet could have written? (Cover the team name ...)"; "Where does a judge feel something, and what put them there" | Does each of the seven read-aloud questions get a "yes" from a cold reader? |
| D38 | B · AIM | The reading's lessons on the edges | Synthesis 5-6: "the first words carry the argument"; "stop without summing up"; "Numbers are said flat"; "Last lines shorter still, an act rather than a lesson" | Do the first words argue and the last line end on an act, not a lesson? |

---

## E. Tensions, and how to meet both students at once

Each tension gives both sides with quotes, a proposed resolution, and the test a reviewer applies.

**E1. The full-circle motif and "do not crush" against "corny", "rehab" and "packaging".**
*Ahaan (Book 11):* "the really clever way that you employed the extended metaphor / motif of 'Caplet XR' as a
full-circle thing between the introduction and conclusion"; "the 'do not crush' reference ... That was the whole power."
*Ray (5 Nov):* "What does do not crush even mean? it sounds so corny."; "it feels like we're helping Laura for a rehab";
"metaphors alone does not count as creativity." *Book 12 (Ahaan, later the same night):* "Keep in mind all the things Ray
just said, because they're really, really important."
**Resolution.** Keep the name Caplet XR. Drop every medicine image, "do not crush" included. Keep Book 11's real point,
which is structural: the motif appears in the introduction and returns in the conclusion, and nothing pays off that
wasn't set up. Do that with the name's own finance meaning, the ten redemptions. The opening says what X and R stand for
in the plan, and the close lands on a redemption (the last payment, or the plan running out on schedule) as an act, not a
slogan. Keep the substance of "do not crush" as a plain rule, because it's good investing and it matches October's "Every
year the bonds sit untouched is a good year": no holding is sold before it matures. Book 12 came after Ray's points and
endorses them, and Ray objects to the picture, not to the arc. The note tells Ahaan in one plain line that the arc now
runs on the redemptions, since he asked for the tablet's arc on 1 Nov. *Test:* is XR in the first and last paragraphs,
with a payoff that needs its set-up, no medicine, and the hold-to-maturity rule said plainly?

**E2. Both meanings of XR in the IPS against no medicine.**
*Ahaan (Book 5):* "My instinct would be to mention both meanings of XR – the real one, and our one – in the IPS"; but
"either the IPS or the Final Report or both" and "That's completely up to you." *Ray (I85):* the tablet makes Laura
sound like a patient.
**Resolution.** The IPS carries our meaning only (X = ten, R = redemption). The literal "extended release" goes to the
Final Report, where it can be told as the story of the name, or nowhere if Caplet prefers. Book 5 explicitly allows this
split. The note names it as Caplet's call. *Test:* does "extended release" appear nowhere in the IPS, or only without any
medical picture, with the routing said in the note?

**E3. Book 3's second, product-tier meaning against Book 5's dual meaning and the word budget.**
*Ahaan (Book 3):* "come up with ANOTHER potential meaning of the acronym 'XR'"; "label it as something that would sound
like a real investing plan". *Ahaan (Book 5):* the dual meaning is literal plus "X as 10" and a clever R; "bare bones" in
the IPS.
**Resolution.** "X = ten, R = redemption" is itself the meaning that "sound[s] like a real investing plan", so it meets
Book 3's intent. "Caplet XR" already reads like a product edition. Add no third meaning in the IPS; the Final Report can
carry more dimensions. *Test:* is there exactly one decoding sentence, and is it about bonds?

**E4. "A truly elaborate and vast" metaphor against subtle, bare bones and "packaging".**
*Ahaan (Book 1):* "a truly elaborate and vast and expansive metaphor for which almost every corner of our strategy would
be able to be cleverly tied back". *Ahaan (Book 2):* "subtle", "not ... in every single sentence". *Ahaan (Book 5):* "bare
bones" in the IPS. *Ray (I84):* "packaging".
**Resolution.** In the IPS the motif is a frame used twice (open and close). Its elaboration lives only in the Final
Report. The IPS's creativity is carried by the strategy (C7). Book 1 itself ranked the motif below intellect ("that isn't
the primary goal"). *Test:* is the motif in two places at most, with no motif line doing no investing work?

**E5. Parsimony against "don't chop".**
*Ahaan (Book 2):* "we absolutely do want your writing to be parsimonious and lucid". Wharton: 500 words. *Commandment
VII:* "Few ideas, at full size". *Against:* Book 2 ("shouldn't be to just rearrange words"), Book 9 ("cut the HUMAN way"),
Book 10 ("sentences barely make sense"), Book 11 ("extreme obsession with parsimony"), Book 12 ("Cut things whole, don't
chop and snip words").
**Resolution.** Be parsimonious with ideas and generous with words inside each sentence. Choose fewer ideas, write each
in full human sentences with the small words kept, and when over the limit delete a whole idea and send it to the Final
Report. Lucid beats short. *Test:* did the last cut remove an idea? Does every sentence read aloud naturally?

**E6. Erudition against plain English.**
*For erudition:* Book 4 ("truly extraordinary knowledge of investing concepts"), Book 5 ("cerebral and erudite"), Book 9
("99.9% of students ... don't know about"), I81 ("truly extraordinary erudite"; "You must blow us away with how
intelligent you are"), Book 12 ("erudite, intellectual, cerebral"; "Make sure to do so, no matter what"). *For
plainness:* Ray I80 ("plain English"), I83 ("do not invent terms"), Book 11 ("make plain sense to an ordinary reader"),
Book 12 ("normal human English"), Commandment VII (few ideas).
**Resolution.** Erudition shows in the reasoning, not the vocabulary. Each concept is a step in the one argument (C10),
explained like a toy in the same breath (law 5), tied to Laura, and critiqued for what it misses (B9-5). Name the
concept; never name its author (that's the Final Report's job, Book 4). Use three to five concepts at full size rather
than eight in passing, and route the rest to the Final Report. "Erudite" means a reader can tell we know exactly why
each borrowed idea fits or fails, not that we use rare words. *Test:* would a smart fourteen-year-old follow every
concept sentence, and would an expert see the depth?

**E7. "Every number says where it came from" against "no model stats".**
*Book 10 / Commandment V:* "we model" or "we calculate", never "we judge". *Book 11 (later):* "why are you referring to
'our model'? ... Save all those details for the Final Report."
**Resolution.** Book 11 narrows Book 10. The IPS carries no model output at all, so "we modelled" disappears from it and
moves to the Final Report. What numbers remain are case facts, the plan's own rules (ten, half, the dates) and dated
public facts (a crash year). Each still says whose it is in its sentence: the case's, our rule, history's. *Test:* is
there zero model output, and does every remaining number say who it belongs to?

**E8. Studies and evidence against no evidence in the IPS.**
*Ahaan (Book 9):* a donor study is "absolutely BRILLIANT"; the "3 times in 4" asymmetry is "the kind of pick-up which
could genuinely be useful". *Ahaan (Book 11):* "not the models and the citations. Not yet. That's for the Final Report."
*Wharton:* "Teams should use research and analysis to develop their strategy, but sources do not need to be cited".
**Resolution.** A study may shape the reasoning and appear as a plain claim (what funders prefer, why over-promising
costs more than under-promising), with no statistic, author or study name. The study itself goes to the Final Report.
The over-promising asymmetry is argued from the case's own words ("If Laura promises more than she can ultimately
contribute, she could damage her credibility"), never from a multiplier. The plain claim must stay inside what the study
showed (D23). *Test:* is every evidence-based claim number-free and name-free, and true to its source?

**E9. Ahaan's voice against "my voice isn't as good".**
*Ahaan (Books 2, 5):* "try to write more like me"; "use my voice and style and tone and employ that as your own".
*Ahaan (Book 9):* the essays are "not gospel"; use the Wall Street writers too. *Ahaan (Book 11):* voice, never
structure. *Ahaan (Book 12):* "very much secondary to the voice studies – my voice isn't as good".
**Resolution.** The voice studies are the engine: Marks's spine (one idea, an opponent, ending on what we'll do),
Levine's hands (mechanism like a toy), and the 1,000-piece syntheses (first words argue, stop without summing up, a cost
accepted in public, numbers said flat). Ahaan's tone sets the direction: confident, a concession then "But", a long build
then a blunt line, en dashes, British spelling. Never his structure (no pun headings, no one-line paragraphs). He rewrites
in his own words tomorrow, so the draft should be a strong, clean base, not an imitation of him. *Test:* is it neither
generic AI nor generic student, and free of borrowed essay structure?

**E10. "No hedging; overclaim a little" against accuracy and October's "not fixed".**
*Ahaan (Books 3, 5):* "We DO overclaim a little bit"; iBonds "as close to guaranteeing an exact amount at an exact date
as it gets". *Ahaan (Book 5):* "accuracy is important". *Locked October words:* "the final payout is not fixed"; the
Archive's C10 ("guaranteed to the dollar") contradicts them.
**Resolution.** Strong and true. Say "exactly" of a Treasury bond held to maturity. Call the fixed-date funds
near-ironclad, or as close to an exact sum on an exact date as markets offer short of the bond. Never call them "fixed",
"guaranteed" or "to the dollar". If the distinction appears at all, it takes one direct clause. *Test:* is every
certainty claim at full strength and still true of the instrument it names?

**E11. "Judges aren't mini-Lauras" against "keep the client at the centre".**
*Ahaan (Book 3):* "Think about them as judges in a competition, not as mini-me Lauras." *Wharton:* "Your client's
profile and financial goals should remain at the center"; "recommendations that can earn her confidence".
**Resolution.** The audience is expert judges; the subject is Laura's needs. Judge a sentence by "does a judge learn how
this plan serves Laura, and see that we know why?", never by "would Laura feel reassured?". *Test:* is every decision
justified by a fact about Laura, and argued to an expert?

**E12. "Convince our strategy is the best" against "no single correct strategy" and "no comparing with other teams".**
*Ray (I86):* "convince our strategy is the best". *Wharton:* "There is no single correct strategy." *Book 10:* "every team
will do x" is "meta" and "arrogant"; Commandment I: "never by comparing ourselves with other teams".
**Resolution.** Argue superiority against alternative plans as ideas (a balanced fund, investing toward the payments, a
bank's protected note, portfolio insurance), each in its best form and refused for a reason. Never mention other teams.
Claim the plan is best for Laura, with reasons, not the only correct one. *Test:* is at least one alternative refused on
the merits, with no team comparison?

**E13. "No team history" against the voice guide's confession and the Articulation criterion.**
*Ahaan (Book 11):* "Not our team progression." *Voice guide law 7 and s7:* "A real mistake (the STRIPS plan, the
75%-stocks plan)"; "Why this team ... a mistake we fixed". *Wharton:* Articulation of Competition Experience.
**Resolution.** Book 11 wins in the IPS. Articulation belongs to the Final Report, as Wharton's "use each deliverable for
its intended purpose" implies. The one limit the IPS admits is a weakness of the plan, in the present tense, with how it
is covered. *Test:* is there a present-tense limit, and no past plan?

**E14. "Rhetorical questions allowed once" (voice guide) against Book 11.**
*Voice guide s6:* "Allowed once a piece, answered at once". *Ahaan (Book 11):* "the corniest and most cringeworthy thing
I've ever seen".
**Resolution.** Book 11 is the student's word and later. Use no question marks in either box. *Test:* zero "?".

**E15. "Open with a hook" against "no aphorism openers" and "the first paragraph carries strategy".**
*Ray (I50):* "a hook". *Voice guide s4:* "Open with a claim that sounds wrong". *Ray (D35):* "Aphorism openers" banned.
*Book 12:* no case-summary opening.
**Resolution.** The hook is the strategy's central idea, said plainly as what we do and why. It surprises by its
content, not by a rhetorical device. *Test:* is the first sentence a decision about Laura's money, free of aphorism and
case summary?

**E16. "A short sentence that lands" against "no kickers, no one-line endings".**
*Commandment III:* "a sentence that builds and a short one that lands". *Ray (D35):* "Two-word kickers"; "One-line final
paragraph"; "It does not wind up for a punchline."
**Resolution.** Short sentences may land a point inside a paragraph. A paragraph ends on its last real point (a
decision, a rule, a refused alternative), never on a quotable closer. The final paragraph is full sentences. *Test:* does
no paragraph end on a slogan-shaped line, and is the last paragraph more than one line?

**E17. "A real event" (the commandments check) against "no team history".**
*COMMANDMENTS_CHECK, line III:* "a real event". *Book 11:* no team progression.
**Resolution.** A real event means a real-world fact (a dated market episode) or a dated step in the plan, never team
history. *Test:* is any "event" public and true?

**E18. The name: Caplet XR against "Steady Roots".**
*Ahaan (Books 3, 5):* "Caplet XR is a brilliant name; let's stick with it." *Ahaan (Book 2):* no roots names. *Window note
on I06 (5 Nov):* "Ray's 4 Nov pitch drafts name the plan 'Steady Roots'", as do Darren's and the Pitch tab, in the
team's own IPS Report doc.
**Resolution.** Keel's draft uses Caplet XR, as Book 5 locked and no student has revoked; Book 2 bans roots, and Keel
never adopts a roots name on its own. The note flags the name as the team's call in one line, with one rule: whichever
name they choose goes in both boxes. *Test:* is Caplet XR in both boxes, with the choice flagged in the note?

**E19. "Every expectation equal" against "one rule above all else".**
*Ahaan (cover note):* "All are equal." *Ahaan (Books 5, 10):* "there's only one real rule above all else"; "That's your
number one instruction, above all else."
**Resolution.** KILL and MUST rows are the gate: a draft that misses one doesn't go. Among drafts that pass, the
extraordinary decides. *Test:* is every gate passed before any brilliance ranking?

**E20. Consistency with the TNA against "do not invent terms like floor" and "not hamstrung by the TNA".**
*Wharton:* consistency across all three. *October's notes:* "provides a floor for her facility contribution, giving
co-sponsors a minimum figure in 2031". *Ray (I83):* "do not invent terms, like floor". *Ahaan (Book 9):* "Don't feel
hamstrung by what we wrote in the TNAs."
**Resolution.** Consistency is about substance, not vocabulary. Say "minimum facility contribution" (case words and
plain English), which means what October's "floor ... minimum figure" meant. Go further than October, but never against
its locked positions (A36-A48). *Test:* is every October position intact, and is the word "floor" absent?

**E21. "Explain why each investment belongs" against "not describing individual investments".**
*Wharton tip:* "explain why each investment belongs in your strategy". *Wharton IPS:* "rather than describing individual
investments".
**Resolution.** Explain each kind of holding and its job (Treasury bonds held to maturity, fixed-date Treasury funds,
one world share fund, the late-2032 Treasury fund), with no tickers, share counts or trade details. *Test:* does each
holding type have a reason, with no ticker named?

**E22. "Don't use your agents as detectors" against "find your own fingerprints".**
*Ahaan (Book 9):* "AI agents are pretty bad at detecting themselves". *Ahaan (Book 11):* "How hard can it be to figure out
the fingerprints in your own writing".
**Resolution.** Reviewers name concrete machine-like habits by quoting the line (C2, D36), which is fingerprinting. They
never produce an AI-likelihood figure; GPTZero, pasted by a student, is the only score. *Test:* does the review contain
quoted habits and no AI percentage?

**E23. "No case summary up front" against "know your client" and "tailored".**
*Ahaan (Book 12):* the case-summary opening is "the most stupid use of scarce word count". *Wharton:* "Know your client";
"tailored to your client's financial goals, time horizons, and needs".
**Resolution.** Tailoring shows in decisions that use case facts as reasons inside strategy sentences, never in a
preamble. The judges know the case. *Test:* does every case fact appear inside a sentence that decides something?

**E24. Emotional appeal against "corny".**
*Ray (I50):* "you gotta have emotional appeal man". *Ray (I80):* "AI and corny". *Voice guide F1:* "never name the
feeling".
**Resolution.** One plain clause of real stakes from the case (the residency, the people it serves, Laura's word to
co-sponsors), with no feeling-words, sentiment or imagery. *Test:* is there one felt clause, and no "passion", "dream"
or "journey"?

**E25. "Only Wharton's guide" for marking against Book 12's review "against every Bible expectation".**
*Book 10:* "Your only allegiance in terms of marking is to the marking guide from Wharton, and ABSOLUTELY NOTHING ELSE."
*Book 12:* review against "(a) every single one of my expectations ... (b) Wharton's marking guidelines, and (c) ...
brilliance".
**Resolution.** Two passes. When a reviewer plays a judge and ranks drafts, only Wharton's criteria count (A49-A62). The
compliance pass checks every row on this page. Neither pass fixates on a single line outside a KILL row. *Test:* does
the review show both passes, kept apart?

**E26. "X for ten holdings" against accuracy.**
*Book 5:* X = 10. *BIBLE_AUDIT row 32 and row 76c:* a judge asked why "ten holdings" when the late-2032 fund and the
share fund are holdings too; "ten holdings" is the ladder only.
**Resolution.** Decode X against something that is literally ten: the ten operating payments, or the ten Treasury
holdings that pay them, named as such. Never imply the whole portfolio is ten holdings. *Test:* is the decoding literally
true of the plan as written?

**E27. A filled commandments check beside the draft against "one plain page, no internal labels".**
*Commandments:* "every draft's README carries a filled ten-line check". *Ray (I80, CLAUDE.md):* "one page of plain
English, no internal labels"; the Window flagged "Commandments by Roman numeral" in the note on 4 Nov.
**Resolution.** Two files. The note Caplet opens first is one plain page. The filled check, this rubric's scores and the
round log sit in a separate record that the note points to in one line. *Test:* is the note free of codes, with the
check present in the record?

**E28. "Take intellectual risks" against accuracy, October's locked words and the frozen trades.**
*Book 10:* "take intellectual risks". *Book 5:* accuracy. *Wharton:* consistency, and the WInS book reflects the plan.
**Resolution.** Take risks in ideas, framing and argument, never in facts or in plan changes that would need a trade
before Sat 7 Nov 09:00 Sydney (Fri 6 Nov 5 pm ET). *Test:* is the boldest idea true, consistent with October, and free
of any need for a new trade?

**E29. Analogies (Book 9's logic) against "metaphors alone ... packaging".**
*Ahaan (Book 9):* "Analogies, thought experiments". *Ray (I84):* "metaphors alone does not count as creativity".
**Resolution.** An analogy is allowed when it is reasoning: it maps a real mechanism part for part and proves something
(for example, a financial structure the plan rebuilds or refuses). An image that only decorates is cut. *Test:* if the
analogy is deleted, is part of the argument lost?

**E30. "Many concepts" (I81, Book 12) against "fragmented" (Ray I86) and "few ideas" (Commandment VII).**
*I81:* "use many of them to build a strategy of our own". *Ray (I86):* "Your analysis is kind of fragmented."
**Resolution.** Every concept enters only as a step in the one argument for the biggest strength. A concept that can't
be placed in that chain goes to the Final Report. *Test:* does each concept sentence connect to the one before and the
one after it?

---

## F. The kill list: the twenty failures that would most anger them, ranked

Ranked by how recently and how hard the students have said it. Book 12 and Ray's 5 Nov notes come first, then Book 11's
bans, then Book 10. Any one of these sends the draft back.

1. **The IPS opens by retelling the case.** Book 12: "spending the whole first paragraph just summarising the case (as
   you have in v57) is the most stupid use of scarce word count I've ever seen. Please use your brain." (V57 and V58 both
   do it.)
2. **Sentences a human can't follow on one reading.** Book 12: "I swear I literally can't understand half of the
   sentences in the IPS ... This is genuinely a diabolical situation." Book 11: "half of your sentences just DON'T MAKE
   SENSE".
3. **The generic AI voice.** Book 11: "You're sounding more AI than ever, by the way, and it's driving me insane". Book 12:
   "You're going to completely kill your generic AI voice".
4. **Medicine imagery: tablets, doses, "do not crush".** Ray: "What does do not crush even mean? it sounds so corny." and
   "it feels like we're helping Laura for a rehab, but she doesn't need any rehab."
5. **Creativity that is only packaging.** Ray: "metaphors alone does not count as creativity. We want intellectual
   creativity, yours just packaging."
6. **Ordinary: a competent plan with no aha.** Book 10: "Right now, the IPSs still seem ordinary. Competent, impressive,
   but not creative, original, novel, thoughtful or insightful, let alone EXTRAORDINARY".
7. **Model numbers, "our model", probabilities or study statistics.** Book 11: "That's the sort of thing you absolutely
   can't be doing. Save all those details for the Final Report."
8. **Fragmented: no single strategy and biggest strength argued through.** Ray: "Your analysis is kind of fragmented. So
   convince our strategy is the best ... What is the biggest strength our strategy?"
9. **Ray's AI habits: slogan flips, two-word kickers, "That is X." runs, aphorism openers, a one-line ending.** I80:
   "The writing reads as AI and corny"; Ray's habit list: "a human paragraph explains and then stops. It does not wind up for a
   punchline."
10. **Thin erudition, or concepts name-dropped without being used and critiqued.** I81: "You must blow us away with how
    intelligent you are." Book 12: "Make sure to do so, no matter what." Book 4: "rapid name-dropping ... Futile."
11. **Wharton's job left undone: the five questions unanswered, or investments and sums described instead of a
    framework.** Book 11: "If you'd actually bothered to take a look at Wharton's guidelines ... you would've noticed
    that they're looking for the strategy, the 'how' and the 'why' ... Shame on you. Do better."
12. **An opening rhetorical question (or any question).** Book 11: "the corniest and most cringeworthy thing I've ever
    seen ... This is the most ludicrous joke I've ever seen."
13. **Invented terms: "floor", "cheques", "building gift", "promises".** Ray (I83): "do not invent terms, like floor".
14. **Team history or past plans.** Book 11: "stop making references to past plans ... What on Earth? ... Not our team
    progression."
15. **Hedged or softened claims about Treasuries.** Book 5: "hedging and 'safe' language is a classic habit of AI – one
    which is instantly recognisable to judges looking for real authenticity." Ray, 23 Oct: "it would soften our voice."
16. **A contradiction of the locked trading notes, or a false fact.** Wharton: "maintaining a clear and consistent
    investment strategy across all three." Book 5: "accuracy is important". NORTH_STARS: "A genius line that is false
    is the fastest way out of the competition."
17. **The rooms' best ideas missing again.** Book 12: "thousands of good ideas which you just completely ignored or forgot
    about and clearly did not implement in the IPS. This is shameful."
18. **A reworded V57 or V58 instead of a rewrite from scratch.** Book 12: "You will use every single version you've
    generated so far as just inspiration and nothing more than that." Book 4: "A little bit of chopping and changing
    won't cut it".
19. **Gaps, placeholders, open alternatives, or claims that need defending later.** Book 12: "There should be no more
    gaps and no more holes and no more revisions required by the time I take a look tomorrow morning." Ray (I82):
    "Nobody gets to answer a judge before the semifinal".
20. **Comparisons with other teams ("every team will", "most teams", "a typical plan").** Book 10: "a bit meta and also a
    bit arrogant – we should be so good that we are able to differentiate ourselves on our extraordinary-ness".

**Also instant fails, though rarer:** subheadings (Book 11: "who knows why you're using subheadings"); a roots-themed
name (Book 2); R read as "release" (Book 5: "'10 releases' is quite frankly just a weird name"); two different names in
the two boxes; over the word limit; any banned instrument as a holding (Wharton s5).

---

## Scoreboard each reviewer returns (one per round)

1. **Gate:** each failed KILL and MUST row, by ID, with the quoted line and the kind of fix (no new wording).
2. **Wharton as a judge would read it:** one line per criterion (A49-A62), big picture first.
3. **Brilliance:** the three ideas a judge would retell (D1); the biggest strength in one sentence (C10); the most
   creative idea and where it sits (C12); the line that shows erudition (B12-15).
4. **Clarity:** each sentence a cold reader stumbled on, quoted.
5. **What Ahaan and Ray would say next** (D10), in their own register, with the row it maps to.
6. **Tensions touched:** which Part E resolution the draft used, and whether it held.
