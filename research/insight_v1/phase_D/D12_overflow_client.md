# D12 Overflow Researcher (client side): M247, M234, M231

Agent D12, insight_v1 run, written 2026-09-28. AI-generated research for the team: evidence, numbers, specifications
and checklists only. **Nothing here is text to submit.** The team decides and writes every word (Wharton AI policy,
R-W26/R-W27; any AI use goes in the Works Cited, brief section 14).

Scope applied (brief section 17): only the Trading Notes (TN, due Oct 23) and the IPS (due Nov 6). Two of my three
questions were tagged "Final Report" (M231, M234). I kept only the parts that serve TN or the IPS and moved the Final
Report parts to the "Later (after Nov 9)" list at the end. No relayed user messages were received during this task.

Scripts (run from the repo root; each has a docstring listing inputs and status labels):
- `.venv/bin/python research/insight_v1/scripts/D12_note_roles.py` (M247)
- `.venv/bin/python research/insight_v1/scripts/D12_evidence_grades.py` (M231)
- `.venv/bin/python research/insight_v1/scripts/D12_reader_test.py` (M234)

Terms used: **role word** = one of the four jobs the Guide says a Trading Note should name ("growth, liquidity, risk
management, or future funding", Guide p.3). **Hedge** = the Treasury funds standing in for the ten $50,000 payments.
**Growth money** = everything the payments do not need. **Duration** = roughly the % a bond fund falls if rates rise by
1 percentage point. **Paraphrase test** = a reader reads a passage and says in their own words what it means; the
writer notes misreadings and fixes the text.

---

## Summary: top findings, ranked by impact on reaching the semifinals and on making the plan hers

1. **NEW (tier 1, TN): WInS notes may be capped at 300 characters, about 43 words, and Wharton's own example note is
   413 characters.** Stock-Trak's HowTheMarketWorks product says of its Trade Notes "we allow up to 300 characters"
   (VERIFIED-PRIMARY for that product, read 2026-09-28). WInS runs on Stock-Trak (edu.stocktrak.com/wharton). Whether
   the WInS 2026-27 note box uses the same cap is **UNVERIFIED**, and no WInS page states a limit. Wharton's example note
   is 59 words and 413 characters (script). A 300-character cut would lose its last 27%, including the sentence that
   links the trade to the plan. The 2026-27 WInS User Guide says the note is entered on the order-review screen:
   "Enter a Trade Note (these are important!) to discuss how the purchase fits into your overall strategy" (p.8,
   VERIFIED-PRIMARY). **Decision:** plan every note to fit in **300 characters**. On the first order, check the note
   box for a counter or cut-off and record what it shows. The ticket's note checklists (5-6 elements each) do not fit
   in about 43 words, so split them. Four elements go in the note. The rest goes in the 100-word reflection. (Details
   under M247.)
2. **(Tier 1, TN) Three distinct role words are available only if WInS holds growth money (option ii).** Option (ii)
   supports three role words: the hedge is *future funding*, VT is *growth*, and VGSH is *risk management* of the
   facility money (with liquidity). In a 20% stock fall, VGSH makes the growth money lose 12.4% instead of 20%. Option
   (iii), the literal January-2027 book, supports only *future funding* (plus cash as *liquidity*), so its three notes
   would show one role three times. The Guide says "or", so three roles are not required. But the TN guide's first
   sentence asks the notes to show the team's "approach to growth, risk, liquidity, funding reliability, financial
   flexibility". This is a TN reason to prefer (ii), and the team makes the final choice. As far as the repo shows, no
   trade has been placed yet: today is day 1 and the ticket's gate is still open.
3. **(Tier 2, IPS) Grading every number shows that the promise is "bought at market prices" except for four inputs
   nobody can observe yet. The IPS must cover those four with rules, not numbers.** The four are:
   - the ladder's price in January 2027;
   - whether the 2028 deposit arrives in full and on time, which matters for the payments only if that price is above
     $300k;
   - the U.S. Treasury paying;
   - the modelled ~24% chance that the price is above $300k (internal only).

   Only 3 of the 19 key numbers are safe to state in the IPS without the words "we assume" or "history suggests":
   the case's fixed $50,000 payments, the deposits, and the fact that the ladder cost more than $300k on 173 of 185
   trading days in 2026. Laura's own published results table grades every row "Good", "Unsure" or "Bad". She rated 8
   of 14 rows below "Good" and published them under "The [unfinished] results are below." (VERIFIED-PRIMARY). That
   habit is the model. It is a private motivation for the team, not a line for the IPS.
4. **(Tier 2, IPS) A paraphrase test of the 50-word pitch and the IPS rule sentences is worth about 2 student-hours.**
   Use 6 unpaid readers who only restate the text: 3 without a finance background and 3 with one. The U.S.
   plain-language guide says "Conduct between 6 to 9 interviews". Its case study found readers who said a letter was
   clear yet misread one expert term (VERIFIED-PRIMARY). Six readers catch a misreading that half of all readers
   would make 98% of the time, and one that 1 in 5 would make 74% of the time. They often miss rare misreadings (47%
   at 1 in 10). Unpaid help from parents, industry professionals or other adults is allowed (R-W21). Paid "agents"
   are not, and readers must never supply wording (own-words rule).
5. **A caution that is easy to miss:** Wharton's example note uses "reduce portfolio volatility" and "greater
   stability". The wins_now ticket bans those words for our hedge, and the numbers support the ban. The hedge falls
   about 10% if rates rise 1 percentage point: -6.8% of the whole WInS book under (ii), -9.7% under (iii). It "reduces
   risk" only when measured against the payments, whose value falls about 10.2% in the same move. If a note uses
   "risk management" for the hedge, it must say "against the payments".

---

## M247 (tier 1: WInS now + TN). Can three notes from a mostly-Treasury book show distinct official roles, and have we placed a growth trade?

**Canonical question (survivors.json):** "Can our three Trading Notes, drawn from a mostly-Treasury book, show distinct
official roles (future funding, growth, risk management), and have we placed a growth trade with a role-worded note
yet?" Skeptics: judge and stats kept it; "answered" voted kill as already answered (ticket s4, chair memo s6,
guardrails C.12). What is new here: the 300-character finding, a role word for VGSH that no other note uses, the
numeric role test, and the (ii)/(iii) consequence. The rest was already settled by the ticket and by D7 (which dropped
the planned rebalance trade), and I do not repeat it.

**One-sentence answer:** Yes under option (ii): the hedge is *future funding*, VT is *growth* and VGSH is *risk
management* of the facility money. Under option (iii) only *future funding* is honestly available. No growth trade has
been placed yet (repo evidence). Every note must fit its role word, Laura's need and the risk accepted into about 300
characters until WInS shows otherwise.

### Evidence
| Claim | Source (access date) | Status |
|---|---|---|
| Note should state its "expected role in growth, liquidity, risk management, or future funding" | `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt` L84-86 (Guide p.3) | VERIFIED-REPO-FILE |
| The TN deliverable should show the "approach to growth, risk, liquidity, funding reliability, financial flexibility, and future cash-flow needs"; the notes "Collectively" show "a cohesive portfolio strategy" | `2026_WGY_Trading_Notes_Analysis-FINAL.txt` p.1 (R-T10) | VERIFIED-REPO-FILE |
| Reflection explains how the decision "supported, tested, or refined" the strategy ("or": no quota) | TN guide p.1; Guide p.3 | VERIFIED-REPO-FILE |
| "Enter a Trade Note (these are important!) to discuss how the purchase fits into your overall strategy." (order-review step, before Confirm) | https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf p.8 (read 2026-09-28) | VERIFIED-PRIMARY |
| "…their "Trade Notes" - a short sentence mentioning why they are placing this trade (almost like a tweet, but we allow up to 300 characters)." | https://www.howthemarketworks.com/updates/trade-notes-justify-trades/ (Stock-Trak, Inc. property; undated; read 2026-09-28, phrase found verbatim) | VERIFIED-PRIMARY for HowTheMarketWorks; **UNVERIFIED for WInS 2026-27** |
| Students "cannot edit or delete" notes but "can add more notes to the same trade (each note has its own timestamp…)" | https://www.stocktrak.com/new-feature-trade-notes/ (2017 blog; read 2026-09-28) | VERIFIED-PRIMARY (vendor, not season-specific) |
| Earlier files said "no character limit is published" | `phase_A/wins_week1_guardrails.md` L49, L97-98; `scripts/D9_draft_checker.py` docstring | VERIFIED-REPO-FILE (now superseded by the row above as a planning cap) |
| Example note: 59 words, 413 characters | `D12_note_roles.py` on TN guide L36-39 | VERIFIED-REPO-FILE (count) |
| Planned weights (ii) IEF 23.6 / TLH 42.4 / VT 20.5 / VGSH 12.5 / cash 1; (iii) IEF 35 / TLH 63 / cash 2 | `wins_now/securities_and_allocation_v0.md` ticket | provisional ticket (team has not voted) |
| No executed WInS trade recorded in the repo (only `decisions/demo/`); ticket gate boxes (a)-(e) still unticked | repo, 2026-09-28 | VERIFIED-REPO-FILE (absence); the team's WInS account is not visible to D12 |

### Numbers (script `D12_note_roles.py`)
| Number | Value | From |
|---|---|---|
| Example note length | 59 words / 413 characters; 27% would be cut at 300 | TN guide text, counted |
| 300 characters in words | about 43 words (7.0 characters per word, spaces included) | example note's own ratio (ASSUMPTION that team notes are similar) |
| Role test, rates +1 percentage point (first-order) | IEF -6.9%, TLH -11.6%, VGSH -1.9%, VT 0 (ASSUMPTION), payments' value -10.2% | issuer durations 6.86/11.59/1.9y; spot payment duration 10.16y (brief s14) |
| Role test, world stocks -20% (ASSUMPTION) | VT -$12,300; the growth money (VT+VGSH, $99,000) -12.4% instead of -20%; payments unaffected | ticket weights, option (ii) |
| Whole book, rates +1pp | (ii) -$20,312 (-6.8%); (iii) -$29,108 (-9.7%) | same |
| Role words the positions can honestly carry | (ii) 3 of 4 (future funding, growth, liquidity/risk management); (iii) 2 of 4 (future funding, liquidity) | same |
| Days left | 19 U.S. weekdays from Mon Sep 28 to Thu Oct 22; 15 to Fri Oct 16 (leaves a week for reflections) | calendar; Columbus Day Oct 12 counted as an ETF trading day (ASSUMPTION) |

### Implication
- **Decision (WInS-now, before the first order):** the 300-character rule. Draft each note to 300 characters or fewer
  (count with `D9_draft_checker.py --kind note`, which prints characters). On the first order, record in the decision
  log whether the note box shows a counter or cuts text off. If WInS shows a larger limit, the team may use it, but
  shorter still reads better. **Do not plan on a second "added" note to finish a sentence.** It carries a later
  timestamp, and the TN guide asks for each note "exactly as it appears in WInS". How Wharton treats added notes is
  UNVERIFIED; ask through Contact Us before relying on one.
- **Specification (TN): four elements must be in each ≤300-character note** (the team writes the words):
  1. the action and instrument type;
  2. **one role word** from the Guide's list;
  3. Laura's specific need it serves;
  4. the main risk accepted, or the rule that governs the position.

  Everything else in the ticket's checklists moves to the reflection: the ~$292k sizing, "closer to her dates",
  "stand-in for the January 2027 ladder", and the provisional 60/40 split with its decision date (D7).
- **Role word per planned note (option ii):**

  | Note | Role word | What the note must let a reader check | Never say |
  |---|---|---|---|
  | Hedge (TLH, or SPTL if the position limit forces a split) | future funding | Its value moves with the cost of the ten fixed payments | "match", "mature in her payment years", "stable", "reduce volatility" (ticket) |
  | VT | growth | Only money the promise does not need; a fall shrinks the facility amount, never the payments | a return forecast |
  | VGSH | risk management (of the facility money), with liquidity as the second word | Keeps part of the growth money out of stocks, so a 20% stock fall costs that money about 12% instead of 20%, and that part stays close to its value (-1.9% per +1pp) | a floor percentage; "the 2031 floor" (ticket) |

  This gives VGSH a role word the other two notes do not use. D6 (line 155) suggested "credibility or flexibility" for
  VGSH; "risk management" is the Guide's own word and can be checked with a number. The team chooses.
- **Decision input for gate box (b), (ii) vs (iii):** under (iii), all three candidate notes are hedge pieces (IEF,
  TLH, SPTL) with the same role word. The growth argument then lives only in the IPS. This is a real TN cost of (iii),
  but not a rule breach ("or" in the Guide). If the team chooses (iii), the notes must differ by what they show
  (supported / tested / refined, per D7), not by role.
- **Status check:** no growth trade has been placed, and none should be until gate boxes (a)-(e) are ticked. The
  ticket's target (fills by Fri Oct 2 ET) leaves 14 of the 19 weekdays for anything that must be tested or refined
  before Oct 23.

Deliverables: WInS-now, TN. Deadline tier 1. Confidence: **high** on the role mapping and the (iii) consequence;
**medium** on the 300-character cap (the vendor states it for a sister product; WInS itself is unconfirmed). Changes
current strategy? **Not the strategy; yes the ticket**: the note checklists split into note (4 elements, ≤300
characters) and reflection; VGSH gets the role word "risk management"; (iii) now has a named TN cost. Criterion served
most: **Portfolio Analysis** ("explain why each security belongs"), then Investment Strategy (consistency).

**What this teaches:** a job title is only honest if the position behaves like it. A 1-point rate rise and a 20% stock
fall hit each of the three funds very differently, so each note's role word can be checked with a number.

---

## M231 (tier 2: IPS; the Final Report column is a later item). Should every key number carry an evidence grade, as her own "Match Quality" column does?

**Canonical question:** "Should every key number in the Final Report carry an evidence grade (observed price /
historical estimate / assumption, plus a quality word), as her own 'Match Quality' column does?" All three skeptics
kept it (priority 3). Under brief s17 the Final Report column is a later item. The part in scope: **what grading does
to the IPS**.

**One-sentence answer:** Yes, in a light form. Grade every number now in the team's decision log. In the IPS, say the
grade in words ("at today's prices", "history suggests", "we assume"). The exercise shows that the ten-payment promise
rests on market prices except for four inputs nobody can observe yet, and the IPS must cover each of those with a
rule.

### Evidence
| Claim | Source (access date) | Status |
|---|---|---|
| Her page: "The [unfinished] results are below." and a column headed "Match Quality" graded Good/Unsure/Bad; counts 6 Good, 5 Unsure, 3 Bad of 14; her "Initial takeaways" explain why weaker matches happened | https://lauragao.com/rewriting-herstory (undated; student-era per the page's "Wharton freshman" remark, ASSUMPTION), read 2026-09-28 | VERIFIED-PRIMARY (also D13a B9b-Q09) |
| Case: teams "identify the assumptions supporting their recommendation" and "identify and explain their assumptions about investment performance, the timing of cash flows, outside funding, the effect of inflation…" | case p.3 L98-99 (R-C56), p.4 L146-148 (R-C85) | VERIFIED-REPO-FILE |
| Portfolio Analysis criterion: "uses reasonable assumptions and projections" | SMApply page L53 (R-S26) | VERIFIED-REPO-FILE |
| IPS: "Focus on the strategy and decision-making framework … rather than … presenting detailed financial calculations"; no charts, footnotes or formal citations | IPS guide p.2, p.3 (R-I55) | VERIFIED-REPO-FILE |
| D13 rules: no Laura quotes in TN or IPS; the Rewriting Herstory line is safe only with context | brief s16; D13a/D13c | VERIFIED-REPO-FILE |
| Ladder cost more than $300k on 173 of 185 trading days of 2026; P(> $300k on 2027-01-01) ~24% | brief s14 | VERIFIED (days, from treasury.gov curves) / ASSUMPTION (probability) |

### Numbers (script `D12_evidence_grades.py`; four grades: CASE, PRICED, HISTORY, ASSUMED)
- 19 key numbers registered. The **promise** rests on 2 CASE, 6 PRICED, 1 HISTORY and 4 ASSUMED inputs. The four
  ASSUMED inputs:
  1. the January 2027 ladder price (not yet observable);
  2. the ~24% chance that it is above $300k (a model);
  3. the U.S. Treasury paying (the stated residual risk);
  4. the 2028 deposit arriving in full and on time. This one matters for the payments only if the January 2027 price
     is above $300k.
- The **facility outcome** rests on 1 CASE, 1 PRICED, 3 HISTORY and 4 ASSUMED inputs (JPM 7.00% AC World forecast,
  equity share, model percentiles, deposit).
- Only **3 of 19** can go into the IPS as plain facts: the fixed $50,000 × 10 payments, the $300k + $150k deposits,
  and "the ladder cost more than $300k on most trading days this year" (173 of 185). Every other number needs its
  grade said in words or should stay out. That fits the IPS guide's "no detailed calculations" and the stakeholder
  map's "IPS: at most one rounded number" (SH-16).
- Laura's own grades: 57% of her published rows were below "Good", and she published them.

### Implication
- **IPS: rules to fix before Nov 6** (the content a strong IPS passage must contain; the team writes it):
  1. The certainty definition is in words and names its grade: bought at market prices at purchase, not forecast.
  2. **Rule for input 1:** if the ladder costs more than $300k in January 2027, buy the longest-dated payments first
     and finish the ladder from the 2028 deposit before anything else. This is the current strategy (brief s7);
     grading makes it compulsory to state.
  3. **Rule for input 4:** if the 2028 deposit is late or short, the unfinished payments come first and the growth
     money waits. The facility amount absorbs the shortfall; the payments never do. This matches brief s8 item 8.
     State it as a rule.
  4. **Input 3** is named once as the only residual risk ("barring U.S. Treasury default", brief s7).
  5. Any forecast-based statement (growth, the 2031 range method) carries a word that marks it as assumed.
- **Decision log now (cheap, feeds TN reflections and the later FR):** add a "grade" column (CASE / PRICED / HISTORY /
  ASSUMED) to every number the team records. A TN reflection may use at most one number (blueprint 01 s4). Prefer a
  PRICED one, such as "about $292k at today's Treasury prices", and say that it is a price.
- **Do not** mention Laura's Match Quality column in the IPS or the notes. It would be decoration and a citation the
  IPS bans. It stays as the team's private reason for the habit.

Deliverables: IPS (and the decision log feeding TN). Tier 2. Confidence: **high** on the dependency finding;
**medium** that judges reward the grading as such (no public scoring evidence). Changes current strategy? **No.** It
makes two existing rules (inputs 1 and 4) mandatory IPS content. Criterion: **Portfolio Analysis** ("reasonable
assumptions", R-S26), then Client Knowledge.

**What this teaches:** sorting numbers into "bought", "history" and "assumed" shows exactly where a promise can still
break. That is where a rule is needed.

---

## M234 (tier 2: IPS; the co-sponsor paragraph test is a later item). Should the team usability-test its wording with about five non-finance readers?

**Canonical question:** "Before submitting, should the team usability-test the co-sponsor paragraph and the IPS rules
with about five non-finance readers and report what changed, as she tested products with nurses and doctors?" The
stats skeptic voted kill ("trivial"; n=5 is anecdotal). That criticism is right about statistics but not about the
purpose: the test *finds misreadings*; it does not measure a rate. Under brief s17 the co-sponsor paragraph and the FR
Articulation report are later items. In scope: the **50-word pitch and the IPS rule sentences**.

**One-sentence answer:** Yes. Before Nov 6, run one paraphrase test of the pitch and the IPS rules with 6 unpaid
readers (3 without finance, 3 with). Readers only restate, never reword. Fix what two or more misread, retest with
fresh readers, and log it for the Final Report later.

### Evidence
| Claim | Source (access date) | Status |
|---|---|---|
| "Conduct between 6 to 9 interviews"; ask readers "to tell you in their own words what that section means… Do not correct the participant"; a Veterans Benefits Administration test where readers "all said that it was clear" yet read the term "service-connected disability" in different ways | https://digital.gov/guides/plain-language/test/paraphrase-testing (U.S. plain-language guide), read 2026-09-28 | VERIFIED-PRIMARY |
| Typical share of problems found per test user "is 31%"; "testing no more than 5 users"; five users find "85%"; with distinct groups, "3 users from each category if testing three or more groups", "3–4 users from each category if testing two groups" | https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ (Jakob Nielsen, 2000-03-18), read 2026-09-28 | VERIFIED-PRIMARY |
| Her resume: "Collaborated with researchers at National Institute of Health for usability tests with nurses and doctors"; "Beta-tested MVP with 300K+ users…" | https://lauragao.com/s/Laura-Gao-Resume.pdf (D13a B9b-Q04/Q05) | VERIFIED-PRIMARY (self-reported claims) |
| "Teams may seek guidance from a parent, industry professional, or other adult serving as a secondary advisor… However, the use of paid advisors, education consultants, or other agents is prohibited." | Rules & Roles (R-W21) | VERIFIED-PRIMARY via case_register |
| Students must use their own voice and words; no invented teamwork stories | R-W26-R-W28; brief s14 | VERIFIED-PRIMARY via case_register |
| IPS pitch "Clearly communicate the central idea"; "Keep the presentation simple and focus on communicating the investment strategy clearly" | IPS guide p.1, p.3 | VERIFIED-REPO-FILE |
| Semifinal readers fear jargon; who they are is not published | stakeholder_map SH-16 | ASSUMPTION/judgement |

### Numbers (script `D12_reader_test.py`)
- Share of problems found (Nielsen-Landauer, L = 31%): 3 readers 67%, 5 readers 84%, 6 readers 89%, 9 readers 96%.
- One specific misreading that a share p of readers would make, seen by at least 1 / at least 2 of 6 readers:
  p = 50%: 98% / 89%; p = 31%: 89% / 60%; p = 20%: 74% / 34%; p = 10%: 47% / 11%. So the test reliably catches the
  big misreadings and often misses rare ones. Report "k of 6 read X as Y" as a problem found, never as a percentage of
  people.
- Cost: about 60 reader-minutes, about 2 student-hours per round (ASSUMPTION: 10 minutes per reader, 2 students per
  session).

### Implication
- **IPS: test protocol (checklist, no drafted text):**
  - [ ] Window: after the TN are in (Oct 23). Round 1 about Oct 26-30 on the team's own draft; round 2 about Nov 2-3
        with **fresh** readers on the revised text. Submit by Nov 6, 5:00 p.m. ET (5:00 p.m. EST = 9:00 a.m. Sat Nov 7 AEDT; U.S. clocks change Nov 1).
  - [ ] Readers: 6 unpaid adults or students **not** in any competing team. 3 with no finance background (like most
        co-sponsor readers; Laura's degree is in statistics, case p.1 L16, and her career is product work and
        art, not finance) and 3 with some
        finance background (closer to semifinal readers, who are unknown). The two groups follow Nielsen's
        guidance for distinct groups. The advisor may be one reader ("sounding board", R-W20).
  - [ ] Readers restate only. They never suggest words. The team does not correct them during the session.
  - [ ] Questions to ask (open, not yes/no):
        (1) "In your own words, what is this plan trying to do for Laura?"
        (2) "If stocks fell by a third next year, what happens to the $50,000 payments?" (intended answer: nothing)
        (3) "If interest rates fall before January 2027, what does the team do?" (intended: longest payments first,
            the rest from the 2028 money)
        (4) "What could still stop a payment?"
        (5) "What will Laura be able to tell co-sponsors in 2031, and how sure will it be?" (the method, not numbers)
        (6) "What might confuse someone else?" (plain-language guide's indirect question)
  - [ ] Terms most likely to be misread (they carry expert meanings like "service-connected"): "fully funded",
        "high degree of certainty", "locked in", "hedge", "duration", "floor", "operating reserve", "nominal",
        "growth money/surplus". Check each one used in the draft.
  - [ ] Change rule: change a sentence if 2 or more readers misread it the same way, or if any reader gets question
        2, 3 or 4 wrong (the promise's rules must be unmistakable).
  - [ ] Log it without personal data: date, reader type (finance / non-finance), no names, which sentence was
        misread, what the team changed. This is true process evidence for the FR later (R-S27), and nothing may be
        invented (R-W28).
- **TN (optional, one line):** before an order, one person outside the note's author restates the note's role in one
  sentence. This sits inside the ticket's existing gate box (d) ("read by a second student").
- **Why this is Laura's way, internally only:** her resume records usability testing with the actual users. Do not
  write that link into the IPS; it would be decoration.

Deliverables: IPS (and a small TN gate step). Tier 2. Confidence: **high** that the method finds big misreadings
cheaply and is allowed; **low-medium** on how much semifinal readers reward the clarity (not observable). Changes
current strategy? **No** (a process step). Criterion: **Creativity and Presentation** (clear, credible communication,
R-S28), then Articulation (R-S27, later).

**What this teaches:** a reader saying "it's clear" is not proof. Asking them to say it back in their own words is.
Six people are enough to find the big misunderstandings, and the fixes matter more than the count.

---

## Later (after Nov 9), one line each (Final Report; not worked here)
- M231: a grade column (CASE / PRICED / HISTORY / ASSUMED) in the FR assumptions table. Possibly one context-safe
  mention of her "Match Quality" habit (student-era, D13 rules).
- M234: paraphrase-test the co-sponsor fundraising paragraph with non-finance readers. Report "k of n misread X, so we
  changed Y" in the Articulation section.

## Sources (all accessed 2026-09-28 unless noted)
- Stock-Trak / HowTheMarketWorks: https://www.howthemarketworks.com/updates/trade-notes-justify-trades/ (undated;
  "300 characters" found verbatim); https://www.stocktrak.com/new-feature-trade-notes/ (2017);
  https://www.stocktrak.com/faq/what-are-trading-notes/ ;
  https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf (p.8).
  (https://education.howthemarketworks.com/trade-notes-justify-trades/ returned HTTP 404.)
- Laura's public professional record: https://lauragao.com/rewriting-herstory ; https://lauragao.com/s/Laura-Gao-Resume.pdf
  (via D13a, 2026-09-27).
- Plain-language testing: https://digital.gov/guides/plain-language/test/paraphrase-testing ;
  https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ (2000-03-18).
- Repo (VERIFIED-REPO-FILE): `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt` (L84-86),
  `2026_WGY_Trading_Notes_Analysis-FINAL.txt`, `2026_WGY_Investment_Policy-FINAL.txt`, `Laura_Gao_2026_Client_Profile.txt`
  (via R-C56, R-C85); `research/insight_v1/phase_A/{case_register,wins_week1_guardrails,stakeholder_map}.md`;
  `research/insight_v1/wins_now/securities_and_allocation_v0.md`; `research/insight_v1/phase_D/{D7_wharton_intent,
  D6_behavioural,D13a_laura_quotes_verified,D13c_voice_map}.md`; `research/insight_v1/phase_C/survivors.json`.
- Search used to find URLs (not evidence): WebSearch, 2026-09-28.

## What this teaches
1. **Read the box before you write in it.** The best-researched note fails if the software cuts it at 300
   characters. The small practical check (is there a limit?) comes before the clever content.
2. **A role is a behaviour, not a label.** "Future funding", "growth" and "risk management" are believable because
   each fund reacts differently to the same shock, and a reader can check that with one number.
3. **Say what kind of number it is.** A price you can check today, a pattern from history and a forecast deserve
   different words. Sorting them shows where the plan still needs a rule.
4. **Test understanding, not approval.** People say "clear" to be polite. Asking them to repeat the idea in their own
   words shows what they actually took away.
