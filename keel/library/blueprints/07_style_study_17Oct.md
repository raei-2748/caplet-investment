# Style study: why our exemplar read as AI, and what good IPS writing does (17 Oct 2026)

AI-generated research (Claude Code) for Team Caplet. Use it to write the team's own version; it is about technique,
not wording to copy.

## What we read
- **Wharton's own writing for this competition:** the client case, the IPS and TNA instructions and the TNA example note
  (`competition/official/2026_27/`). Wharton publishes no model IPS and no winning written report has ever been
  made public (see `caplet/Winning Team Portrait and Scoresheet.md`, "What we could not find").
- **Real investment policy statements:** Loyola University Maryland endowment IPS (2023),
  https://www.loyola.edu/_media/department/financial-services/documents/investment-policy-statement.pdf ;
  Stephen F. Austin State University Foundation IPS, https://sfasu.edu/docs/development/investment-policy-statement.pdf
  (both fetched 17 Oct 2026).
- **The professional standard:** CFA Institute, *Elements of an Investment Policy Statement for Individual Investors*
  (2010), https://rpc.cfainstitute.org/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
- What judges said of past winners: "simple, elegant ideas", "cut slides, cut words", "clear thoughtfulness and
  reasoning behind all the decisions" (portrait file above).

## What good IPS writing does
| Technique | Where we saw it | Example |
|---|---|---|
| Labelled sections in the standard order: objectives, risk tolerance, allocation, review | CFA paper s3-4; every university IPS | Loyola: "Investment Objective", "Investment Policy Statement Review" |
| The first sentence states the purpose plainly, with the client named | CFA 3a | "The investment program governed by the IPS is intended to supplement the earned income of Marcel Perrold..." |
| Commitments in the future tense: we will, shall | CFA 2b, Loyola | "Ms. Wood shall review the IPS ... no less frequently than annually." |
| One idea per sentence; ordinary words; full phrases | Wharton case | "Laura will make ten annual payments of $50,000 toward the residency's operating expenses." |
| Concrete numbers and dates rather than adjectives | Wharton case, Loyola ("5% over the rate of inflation") | |
| Purpose, then a feature and its caveat, then the link to the plan | Wharton TNA example note | "...to reduce portfolio volatility ... although interest-rate changes may affect its value. This trade supports our plan..." |
| Almost no colons, semicolons or metaphors; no rhetorical contrasts | all of the above | |

## Why the earlier exemplar read as AI (and the fix in v6)
| AI tell | Example from v5 | v6 |
|---|---|---|
| Colons and semicolons used for drama | "The rest is the branch, for growth: one global index fund..." | 0 colons, 0 semicolons in the IPS body |
| Clipped phrases left by word-cutting | "her gift's bottom", "room above it", "where no single Treasury fits" | full ordinary phrases |
| A metaphor carrying the structure | "Our roots are Treasuries." | the name lives in the pitch; the body uses plain labels |
| Every sentence packed with clauses | the 2031 sentence had three clauses and a semicolon | the 2031 rules are four short sentences |
| No visible structure | five unlabelled blocks | six labelled sections a judge can tick off |
| Abstract summary words | "only what both promises leave" | "less than a tenth will be in stocks" |

## Rules for the team's own draft
1. Start each paragraph with its label and a plain topic sentence.
2. Write "we will" for every rule the Final Report has to follow.
3. If a sentence has a colon, split it into two sentences.
4. Say the number, not the adjective ("about $21,000 short", not "a modest gap").
5. Read it aloud. If you would not say it to Laura across a table, rewrite it.

## 5. What the StoryScope paper adds (structure, not wording)

Source: Russell, Rajendhran, Pham, Iyyer and Wieting, "StoryScope: Investigating idiosyncrasies in AI fiction",
COLM 2026, arXiv:2604.03136 (uploaded by Ray, 17 Oct). It studies fiction, so only the general findings transfer.

| Finding (paper, s4.1 and s5) | What it means for our reflections | v7 change |
|---|---|---|
| AI over-explains: narrators state the theme 77% of the time vs 52% for humans | Do not end on the moral ("This keeps her 2031 minimum credible") | Each reflection ends on a concrete consequence |
| AI is linear and tidy; humans use time jumps and leave loose ends | Start where the story starts; admit an open judgement | IBTR opens nine days after the trade; VT says "Half is a judgement" |
| Humans name specific outside things about twice as often (47% vs 24%) | Name the email, the date, the share count | "Wharton's 6 October email", "167 shares", "By 16 October" |
| Claude "keeps it cool": restraint, uniform voice, quiet endings | Vary sentence length; let one sentence be short and blunt | "It is deliberately small." "Half is a judgement." |
| Surface edits barely move detection (93.9% after LAMP rewriting vs 95.5%) | Rewording AI text does not make it the team's; only real decisions and real detail do | See the list below |

**Details only the team can supply** (they make the text genuinely yours; add only if true):
- IBTR: the cancelled 6 Oct order's note said "0.3 percentage points" and the re-placed 7 Oct note says "about 0.2"
  (both in `caplet/google_drive/ips_report/05_...`). If you changed it because yields had moved overnight, that is a
  real "tested" detail.
- IBTM: who chose the zero-coupon Treasury for the floor, and how the team reacted to the 6 Oct email.
- VT: whether anyone argued for more stocks, and what settled it.
- Any doubt you still have. Judges trust a team that names one.

## 6. v8: the paper's findings applied to the whole text

| StoryScope finding | v8 move |
|---|---|
| AI states the theme; humans let facts carry it | The IPS opens on the case's hidden tension instead of a purpose statement: ten payments of $50,000 are $500,000, more than the $450,000 deposited, so interest must close the gap. Nothing then says what that "means". |
| AI resolves neatly; humans keep honest ambivalence | "Why half? It is a judgement." The reason follows in one plain line. |
| AI is linear; humans revisit and correct | IBTR opens on the team's own correction: the note's first draft said 0.3 points and was cut to 0.2 after re-pricing with the bonds WInS lists (0.3 matches the idealised $292k ladder in V2/V3; 0.2 matches the WInS-listed $293k ladder). |
| Humans engage the outside world by name | "starting with 2042", "By 16 October", "Wharton's 6 October email", "167 shares" |
| Claude keeps one cool, even register | Mixed sentence lengths and plain, blunt sentences: "We did not sell anything." "We chose not to." A section headed "What could go wrong." |
| AI over-describes | Cut every sentence that restated an earlier one (the inflation line, "so the payments carry no stock market risk" after "not the place for them") |

Checked again after the rewrite: TNR 12 double-spaced render ends on page 3; the words growth, liquidity and diversified
are present; no colons in any reflection; every number traces to WInS fills, the 16 Oct curve or `keel/library/range_2031/`.
Team to confirm: the reason for the 0.3 to 0.2 change, and "we had chosen" in the IBTM reflection.
