# E2 Semifinal reader: scoring the E1 strategy as it would appear in three Trading Notes, a 50-word pitch and a 500-word IPS

Agent E2 (semifinal reader), insight_v1 run, Phase E. Written 2026-09-28. This is AI-generated research for Team
Caplet: scores, reasons, numbers and checklists. **None of it is text to submit.** No pitch, IPS sentence, note or
reflection is drafted here. Where a short phrase names an idea, it is a content label, not wording to copy. The six
students decide every change and write every word themselves. Any AI use goes in the Final Report's Works Cited
(Wharton AI policy, R-W46).

**Serves:** Trading Notes (TN, due Oct 23) and the IPS (due Nov 6) only (brief section 17). There is no Final Report
content. Final Report items appear only as one-line "later" entries (section 6).
**Relayed messages:** none arrived during this task.

**Evidence read** (audit corrections override the text above them):
- the brief;
- the official case, IPS guide, TN guide, Competition Guide, Infographic and SMApply page;
- `phase_E/E1_change_proposals.md` (the object being scored);
- D1-D12, D3_model_v2_results, D13a, D13c, and all four audit files;
- every "Audit corrections" appendix. Note that the two D3 files now carry AX1 appendices, which E1 had not seen;
- `wins_now/securities_and_allocation_v1.md` (the ticket), `phase_D/trading_now_brief.md` and `S4_red_team.md`;
- Phase A (case_register R-AN list, stakeholder_map SH-14 to SH-20, fact_register);
- `phase_C/parked.json` items M007, M008, M015, M021, M033, M035, M040 and M149;
- the council chair memo and round-2 ruling (history only).

`T2_red_team.md` does not exist in the repo (checked with `find` on 2026-09-28), so the ticket v1 and
trading_now_brief stand in for it. E1's numbers reproduce: `E1_split_and_slices.py` was re-run on 2026-09-28, and
every figure in E1's P5 and P7 tables matches.

**Status labels:**
- **VP** = VERIFIED-PRIMARY, as carried by the cited file.
- **VRF** = VERIFIED-REPO-FILE.
- **SNIP** = SNIPPET-UNVERIFIED.
- **ASM** = ASSUMPTION.
- **MODEL** = an ASSUMPTION-based model output, not a forecast.
- **INT** = E2's judgement. **Every score in this file is INT.**

**Terms:**
- **Semifinal reader:** the person who scores the written deliverables and picks the Top 50. The task casts this
  person as a Wharton student evaluator or an asset manager. Who reads this season is not published (SH-16, ASM).
- **Fixed-income professional:** someone who manages bonds for a living.
- **Swap test:** put another client's name into a sentence. If it still works, the sentence is generic (D13c).
- **Two-minute test:** what a reader can say back after reading the pitch and the IPS's first paragraph once.
- **Ladder:** Treasury zero-coupon bonds, one for each $50,000 payment.
- **Growth money:** everything the ladder does not need.
- **Option (ii):** WInS shows the plan's mix after both deposits, scaled to $300k.
- **Option (iii):** WInS shows Laura's literal January-2027 book.

---

## 0. Summary

**Verdict (INT).** The substance is of Top-50 quality. The presentation, as E1 specifies it, is not yet.

- **The good news.** No idea in E1 is wrong in a way a reader would punish. The plan does three things most teams
  will not:
  - it defines certainty by a price she can check, not a model;
  - it names its own two gaps;
  - it promises co-sponsors only what is already bought.
- **The problem.** E1 packs about **55 distinct ideas** into a 50-word pitch and a 500-word IPS (my count from
  P1-P13; section 3.2). That is about one new idea every 9 words. Last year's lesson was "strategy packaging was
  over-complex for the insight" (CLAUDE.md, VRF), and E1 repeats it at the level of wording rather than holdings.
- **One visible contradiction.** The recommended pitch rule is worded as a ban ("no stock risk until all ten payments
  are bought"). The recommended WInS book (option ii) buys world stocks on day one. A reader who meets the notes first
  sees the rule broken before the IPS explains the scaling.

**Scores as specified by E1** (INT; the scale is defined in section 2):

| Criterion (SMApply wording, VRF) | Score | One-line reason |
|---|---|---|
| Investment Strategy | **7** | Excellent dated planning and pre-set rules. But "creative" is modest, diversification is never argued, and there is a consistency risk under (ii) |
| Client Knowledge and Objectives | **7** | Strongest Laura links (2028 career income, credibility) are real. But the pitch omits the residency, the plan looks timid, and the growth rule reads as loss-avoidance |
| Portfolio Analysis | **7** | Certainty by price, named residual risks, a pre-registered "tested" window. Three fixed-income slips; little visible data by design |
| Articulation of Competition Experience | **5** | Almost nothing in the TN shows challenge or change. The one true refinement story (growth-first dropped after testing) is unused |
| Creativity and Presentation | **6** | "Announce only what is bought" is original. But the IPS reads as a rulebook, is dense with jargon, and has no memorable line |
| **Total** | **32/50** | Competitive, but not a safe Top-50 read |

**After the ten fixes in section 4 (INT): about 8 / 8 / 8 / 6 / 8 = 38/50.** Most of the gain comes from presentation
and consistency, not from changing the strategy. Three fixes do change a rule or a parameter: F6 (the growth-share
yardstick), F7 (floor timing and the growth money's bonds) and F4 (how the central idea is worded).

**The ten fixes, ranked by score gained per hour:**
1. **F1.** Cut the IPS to about 12 ideas and at most ~380 content words.
2. **F2.** Build the IPS on four dated decisions (2027, 2028, 2031, 2033), not "Rule 1-4 + G".
3. **F3.** Rebuild the pitch around a positive central idea, the residency, and "only promise what is owned".
4. **F4.** Word the central idea as a split of jobs, so it is true of both books, and put the scaling marker inside
   each (ii) note.
5. **F5.** Add the two IPS-guide items E1 never budgets: diversification and liquidity.
6. **F6.** Fix the growth-share rule's yardstick (money put in vs the safe alternative) and say what stocks are for.
7. **F7.** A fixed-income correction pack:
   - withdraw the $101k/$165k barbell figure;
   - add the "floor in 2028 or 2031?" choice;
   - give reasons for short bonds and for longest-first;
   - put "about" on the ladder price and name the model behind any odds.
8. **F8.** Use the true refinement history in one reflection.
9. **F9.** Give each note one checkable fact, and each reflection one extra job.
10. **F10.** A plain-language and authenticity pass: jargon table, paraphrase test aimed at the 2031 method, the
    team's own labels, and the statistics degree used at most once.

---

## 1. What the reader actually sees (reconstructed from E1's specification; elements, not text)

The reader has about 2,300 finished submissions in the pile. Last season, "Some 2,300 teams from 79 countries
submitted final reports" (R-W99, VP via Phase A; R-AN60). The Top 50 is roughly the top 2% (arithmetic; INT that the
same share applies this year).

| Piece | What E1 puts there | What a reader takes away in about two minutes (INT) | Main risk |
|---|---|---|---|
| Note A: hedge (TLH/IEF) | Role "future funding"; the ten payments; a rate-sensitivity fact ("about 10 years"); the rule "never sold after a rate rise". Under (ii), "after both deposits" | "A Treasury ETF for the operating payments", the same trade as Wharton's own example (TN guide L36-39, VRF). It stands out only if the fact and the rule are there | Reads like the example (R-AN44). Under (ii), a careful reader sees a ~$198k hedge against a ~$292k promise (AY1 [5], derived) |
| Note B: VT | Role "growth"; only money the payments do not need; "after her 2028 deposit"; one fund fact or the split | "A world index fund for growth" | Generic unless it says whose money is at risk. Under (ii) it visibly breaks a ban-worded pitch rule |
| Note C: VGSH | "Risk management" or "liquidity"; the short-Treasury part of the growth money | "Short Treasuries to lower risk" | The weakest note. Its effect is the ordinary effect of not holding stocks (AY1 C10) |
| Reflections (≤100 words) | The three official answers, plus "tested" numbers, plus scaling, plus a case trait passing the swap test, plus one number | Crowded. Six jobs in 100 words reads mechanical | Each reflection tries to do everything (section 3.2) |
| Pitch (50 words) | The rule, the client benefit, what the rest is for, and optionally the 2031 bought bottom | "They buy the payments first and then invest the rest" | A prohibition as the central idea; no residency; the most distinctive idea (element 4) is optional |
| IPS (≈480 words) | Four money rules plus governance, certainty with two gaps, risk by goal, three trade-offs, the WInS sentence, a fee principle, currency and building costs, bad-year pre-commitments | Reads like a policy manual. The reader can restate the first rule, but not the 2031 method | Density, jargon and page overflow (section 3.2) |

**The two-minute test** (four questions adapted from D12 M234; answers predicted INT):
1. What is bought first, and why? **Likely answered.**
2. What is the rest for? **Likely answered.**
3. What will Laura tell co-sponsors in 2031, and why will she never have to walk it back? **Likely missed.**
   E1 puts this in rule 3 as "a, s, q, uncapped". That is the plan's most original idea, and it is the least legible.
4. What could still stop a payment? **Partly answered.** E1 names gap (i), gap (ii), the joint tail, and late,
   smaller or instalment deposits in three different places. The reader loses the thread.

---

## 2. Scores per criterion, with reasons

**Scale (ASM, used for all five criteria):**
- **1-3:** missing or wrong.
- **4-5:** competent and generic, like a typical finished report.
- **6-7:** clearly above the field.
- **8:** stands out in a pile.
- **9-10:** among the few best a reader sees.

**Two limits on the scores:**
- A Top-50 read probably needs about 8 on the first three criteria (INT).
- The TN and IPS carry only part of what the Final Report will show, so Articulation and co-sponsor communication are
  capped here by format, not by quality.

### 2.1 Investment Strategy: 7/10

Official wording (SMApply L49, VRF): "Presents a clear and creative investment thesis; demonstrates disciplined
planning across Laura's changing time horizons and cash-flow needs; uses appropriate diversification; and maintains
consistency with the team's IPS."

**Earns points:**
- **Disciplined planning across changing horizons** is the plan's best fit to any criterion. There is a dated action
  at each case date (2027 purchase; 2028 completion and growth; 2031 bought bottom; 2033 reserve and gift), each
  decided before Nov 6 (E1 P11, P3, P7, P9).
- The Guide says a strategy may include "planned adjustments as funding dates approach" (L156, VRF). E1's rules are
  exactly that.
- Pre-set if-then rules answer the IPS guide's "planned changes" and "operating reserve's asset composition over time"
  (L46-50, VRF).

**Loses points:**
- **Creativity is modest at the thesis level.** "Buy the promise, grow the surplus" is standard pension practice
  (D8 framework map; the Russell 2026 "surplus glidepath" wording is VP). D13c N7 already says: "Say so … Do not call
  the plan 'innovative'."
  - The creative parts are narrower: a 2031 range whose bottom is bought, and a promise that stops depending on her
    career income. E1 buries the first in rule 3 and makes it optional in the pitch.
- **"Appropriate diversification" is never argued.**
  - The IPS guide asks for "portfolio construction and diversification" (L46, VRF).
  - The 2027 book is ~97-98% one issuer (M035, parked high-priority; ticket section 2).
  - E1's word budget (P16) has no diversification line. The official "funding purposes" diversification (R-AN45, VP)
    appears only as a reason for option (ii) in P13.
- **Consistency risk.** E1 recommends both a ban-worded central idea (P1) and option (ii) (P13). E1 itself says the
  rule is "visibly contradicted by a day-one VT buy unless the IPS carries the scaling sentence" (P1 side effects).
  But the notes are read first and are permanent (TN guide L44, VRF).
- **One withdrawn number.** E1 still cites the D3 comparison "$101k vs ~$165k" (E1 L97-98). AX1 C6 withdrew it: it
  compares a 50% lock with an 80% lock, and the barbell is not dominated (section 3.8, E-1).

**What moves it to 8:**
- F2 (dated spine);
- F3 (the bought-bottom idea in the pitch);
- F4 (no visible contradiction);
- F5 (a diversification sentence);
- F7 (the withdrawn figure removed; the floor-timing choice made).

### 2.2 Client Knowledge and Objectives: 7/10

Official wording (SMApply L51, VRF): "Tailors the strategy to Laura's circumstances, priorities, risk considerations,
and residency goals; demonstrates a thoughtful understanding of the client; and presents recommendations that can earn
her confidence."

**Earns points:**
- **The 2028 deposit is career income.** It comes from "publishing advances, speaking engagements, licensing, and
  other entrepreneurial ventures" (case L44-45, VRF). So buying the payments first makes her promise independent of
  that income. This passes the swap test, and it is the most Laura-specific benefit in the run (D9 M143; D7 M011).
- **Credibility is tied to her reputation-driven income** (BS-03, INT from VRF), not only to co-sponsors.
- **Risk is stated goal by goal** with the three-part CFA profile (P6; D6 finding 1, VP source). This beats the
  one-word "moderate" most teams will write (SH-01, INT).
- **Her two decisions are left to her.** Laura makes the choices the case gives her: the range she announces and the
  2033 amount (P10). That is respectful and matches the case (L101, L110, VRF).

**Loses points:**
- **The residency is missing from the pitch spec.**
  - E1's pitch elements speak of "ten payments", "markets", "earnings" and "facility contribution" (P1).
  - The criterion names "residency goals". Laura's newest verified priority is people "in the room" (D13c V6, VP).
  - A reader wants to see what the money is for before how it is invested (D13c communication checklist: "purpose
    comes first").
- **The plan looks timid, and 50/50 sharpens it.** Whole-portfolio stocks are:
  - 0% in 2027;
  - 17.0% after 2028 (20.4% at 60/40);
  - 3.5% after the 2031 floor at an 80% lock (E1 [3], MODEL, reproduced).

  The case's growth wish ("pursuing growth", L73, VRF) and her own verified "take the jump" line (D13c V1, VP) pull
  the other way. E1's answer, risk goal by goal, is right but costs words.
- **The share rule reads as capital protection, not "thoughtful risk".** The rule is "at most about 1-in-20 chance of
  ending below the money put in". E1's own "why" says the rule checks risk "against what the safe alternative pays"
  (P5). It does not (section 3.6, R3).
- **The $150k is doubted too often.** The case says "She will contribute" (L43, VRF; R-AN35).
  - E1's P17 limits doubt to "one labelled stress-scenario clause".
  - Yet P2 (gap i), P3 (completion from 2028) and P4 (smaller; late or in instalments; joint tail) spend about 40-70
    IPS words on it (P16 budget).
  - A reader may see a team that does not trust the client's own plan (INT).
- **Statistics-degree hook.** E1 spends it on the certainty definition (P17). AX1 C19 warns against using it as a
  "persuasion lever". Once, in passing, is the maximum (AY2 C6).

**What moves it to 8:** F3 (residency and purpose first), F6 (positive reason for the stocks), and F10 (one clause for
the $150k; the degree used once or not at all).

### 2.3 Portfolio Analysis: 7/10

Official wording (SMApply L53, VRF): "Demonstrates understanding and effective use of investment concepts and tools;
integrates quantitative and qualitative analysis; and uses reasonable assumptions and projections to evaluate funding
reliability, the facility contribution, and financial flexibility under varying market outcomes."

**Earns points:**
- **Certainty by price, not model.** Each payment is "bought, not forecast", with the residual risk named (P2). The
  case asks teams to "define … explain how they evaluated … identify the assumptions" (L97-99, VRF).
- **The hedge is described by rate sensitivity** ("moves like", "about 10 years"), with banned words kept out (P14;
  ticket section 5).
- **The "tested" reflection** uses a pre-registered window (fill date to the Oct 20 close) and percentage changes (P14;
  AY2 C2). That is real use of a tool, visible in the TN.
- **Varying outcomes are handled by rules**: rates fall, the deposit is short, markets are good or bad (P3, P4, P7).
- **Forecast language is graded** in words (P2 item 7; D12 M231).

**Loses points:**
- **Little visible data, by design.** The IPS carries at most one number (P17), and a reflection one. This is correct
  for the format, but it caps the score before the Final Report.
- **Three fixed-income slips a professional would mark** (section 3.6):
  - short Treasuries for money with a known 2031/2033 use, with no reason given;
  - the growth rule measured against "money put in";
  - longest-first with no stated reason.
- **Model-based odds in the IPS** ("about 1 in 20", "about 1 in 10") need "under our assumptions". The IPS cannot cite
  a model (L123, VRF). D3 found the model "has too few very bad years" (AX1 C12, MODEL).

**What moves it to 8:** F6, F7, and F9 (one checkable number per note).

### 2.4 Articulation of Competition Experience: 5/10 (capped by what the TN and IPS can show)

Official wording (SMApply L55, VRF): "Demonstrates teamwork, communication, and learning; clearly explains the team's
research and decision-making process; and reflects meaningfully on the team's growth and response to challenges."

**Earns points:**
- Notes written to an element specification before any order (ticket gate d).
- A dated decision log, including "decided not to trade" rows (P15).
- An honest "tested" window.

**Loses points:**
- **E1's TN plan makes three "supported" notes the likely outcome.** "Refined" happens only if a pre-announced split
  decision or an unforeseen limit occurs (P14). That is honest, but the reader sees no change of mind.
- **The strongest true story is unused.** The team's first plan (~75% equity, growth-first) was tested and dropped:
  - it left a 3-8% chance of a payment shortfall;
  - that chance was ~41-55% if the 2028 deposit is missing (CLAUDE.md; brief s8 item 1; VRF).

  That is a genuine "refined" history (D13c E6: "True event, not a metaphor"). The TN guide asks how decisions
  "aligned with, tested, or refined" the strategy (L12, VRF). E1 never routes this story to a reflection.
- **No roles are assigned yet** (CLAUDE.md open item, VRF), so teamwork is invisible in the notes.
- **The research behind the plan is overwhelmingly AI-produced.** The risk is an IPS that reads as "artificial
  sophistication". Readers fear AI-written text (SH-16, ASM; R-W26, VP).

**What moves it to 6:** F8 (use the true story once), F10 (the team's own labels and voice). Most of this criterion is
Final Report (instructions Nov 9; later list).

### 2.5 Creativity and Presentation: 6/10

Official wording (SMApply L57, VRF): "Presents a compelling, well-organized narrative in an authentic team voice; uses
data effectively to support conclusions; demonstrates original thinking and meaningful reflection; and communicates
Laura's potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors."

**Earns points:**
- **Original thinking.** In 2031 she announces only what is already bought, plus a stated chance of more (P7). This
  answers the case's credibility warning (L114-116, VRF).
- **Uncertainty communicated credibly.** The two named certainty gaps (P2) match calibration research: honest numeric
  uncertainty costs "only a small decrease in trust" (van der Bles et al. 2020, VP via D6).

**Loses points:**
- **The IPS is organised as a rulebook** (four rules, triggers, governance, pre-commitments, trade-offs), not as a
  narrative.
- **No single memorable sentence** survives the two-minute test (section 1).
- **Jargon density** (section 3.3). A past-season Wharton judging page says "Excessive investing jargon doesn't
  necessarily dazzle the judges" (VP, retired 2023-24 page, via D9). A 2025 semifinal judge praised "simple, elegant
  ideas" (VP via D7/AY2, past season).
- **Page-fit risk at E1's upper budget** (section 3.2). Non-compliance means "will not be considered for semifinal
  selection" (IPS guide L82-83, VRF).
- **The co-sponsor part of this criterion is mostly Final Report**, so it is capped here.

**What moves it to 8:** F1, F2, F3 and F10.

---

## 3. Attack sheet

### 3.1 What reads generic (fails the swap test or copies the field)

| Item | Where in E1 | Why it reads generic (INT) | What would make it Laura's |
|---|---|---|---|
| Hedge note as "a Treasury ETF for the operating payments" | P14 note A | It is Wharton's own example trade (TN guide L36-39, VRF). Many teams will copy it (R-AN44; S4 finding 7, INT) | Lead with the dated payments it stands for and one checkable rate-sensitivity fact. Add the never-sell rule. No "volatility" |
| VT note "world stocks for growth" | P14 note B | Any client, any team | Whose money is at risk: only money her payments do not need; a fall shrinks the facility, never the payments; after her 2028 deposit |
| VGSH note "short Treasuries to reduce risk" | P14 note C | Its effect is the ordinary effect of not holding stocks (AY1 C10) | A checkable number, e.g. a 20% stock fall costs the growth money ~10% at 50/50 (ticket section 5, ASM). Or replace it with a genuine third decision (F9) |
| "Yearly review", "low-cost broad funds", "rebalance within a band" | P10, P12, P5 | Boilerplate in any IPS | Keep only what changes a decision: rules change for her circumstances, never because markets moved (P10 item 3) |
| "Risk is measured on the surplus" | P6, P11 | True of every surplus-based plan | Tie it to her: the payments may never use outside money (L91-92, VRF), while the facility may (L85-86, VRF). That asymmetry is the case's own (D9 M241) |
| Pitch without the residency | P1 | "Ten payments" could be any liability | Name what the payments secure (years of the residency's operations: "what the numbers secure", D13c V8) |

### 3.2 What reads over-complex

**1. About 55 distinct ideas are specified for the pitch plus the IPS** (E2 count of the numbered elements in P1-P13,
INT; many overlap). Grouped:
- the central rule and its benefit (2);
- certainty (3) and its gaps (2);
- the January rule (5);
- the 2028 deposit branches (4);
- the growth mix (4);
- risk by goal (6);
- the 2031 method (6);
- flexibility and currency (4);
- the reserve (3);
- governance (3) and bad-year pre-commitments (4);
- trade-offs (3);
- fees (1);
- the WInS sentence (3).

At about 480 words that is one idea per ~9 words. A plain-English target is about 12 ideas (F1 lists them).

**2. The budget does not fit its own page limit.**
- E1's P16 totals 270-435 words "before connecting words" (VRF, E1 table).
- The page-fit ceiling is about 470-490 IPS words. It may be lower on Letter paper with Word's 27.6 pt "Double"
  spacing (D9; AX2 D10 C3: "about 480 words may be too many").
- At E1's upper end only ~35-55 words remain to join the ideas into sentences. The IPS then either overflows or reads
  as a list (INT).
- The pitch has the same problem: elements 1-3 cost ~34-42 words, and adding element 4 reaches 42-54 against a
  50-word cap (E1 P1; D9 pitch table, INT estimates).

**3. The 2031 method has three parameters (a, s, q), is uncapped, and states confidence both ways.** It is correct and
it earns its place as money-moving logic (AY1 section 5). But a non-specialist cannot restate it in two minutes (D12's
paraphrase questions 5 and 6). See F10 for how to simplify it without losing the rule.

**4. Rule 1 carries five branches:**
- buy on arrival;
- longest-first;
- completion before growth;
- instalments;
- the joint tail.

E1 budgets 40-55 words for them. The joint tail is also named in P2 gap (i). This is double coverage.

**5. Each ≤100-word reflection is asked to carry**:
- the three official answers;
- supported, tested or refined;
- the pre-registered "tested" numbers (~20-25 words);
- the scaling under (ii);
- a case trait passing the swap test;
- at most one number (ticket section 6; P14).

That is six jobs in 100 words.

**6. Four bad-year pre-commitments and three trade-offs** are listed as separate IPS content (P10 item 4; P11). Each
is sound, but together they are about 40-60 words that restate the rules.

### 3.3 Jargon a reader would stumble on (plain replacement = concept, not wording)

| Term | Where E1 would put it | Plain concept (the team words it) | Keep? |
|---|---|---|---|
| funded ratio (at least 1) | P2 item 2 | the money covers today's price of all ten payments | Concept yes, term no |
| nominal (US$) | P2, P8 | fixed in dollars, not adjusted for rising prices | Once, defined |
| percentile / "90th" / p5 | P7 | "about 1 in 10 chance of more than the top" | Words only |
| give-back share *s*, lock share *a*, *q* | P7, P11 | the part bought; the part of the rest added to the gift; the part kept | Letters never appear |
| uncapped | P7 | if markets do better, she can give more | Concept yes |
| rate sensitivity / duration / "about 10 years" | P13, P14 notes | its price moves like the price of her payments when rates change | In notes, one short fact; in the IPS, the concept only |
| designated (the reserve) / self-liquidating | P9 | bought in 2027, named the reserve in 2033; each bond pays out in its year | Concept yes |
| band 45-55 | P5 | reset once a year if stocks drift far from half | One number at most |
| STRIPS, LDI, CUSIP, DV01, glide path, twist | E1 bans these in the IPS (P17) | none | No. Keep the ban |
| "risk need / ability / behavioural loss tolerance" | P6 | how much risk each goal needs, can bear, and how she might feel | Concepts yes; the CFA labels no (no framework names, P17) |
| "promise money", "growth money", "three slices", "short-Treasury part of the growth money" | E1 and ticket labels | the team's own labels | See F10: AI-coined labels in permanent notes are a voice risk (R-W26, VP) |

### 3.4 What is unclear in two minutes

1. **"Longest-dated first."** A lay reader's instinct is to fund the nearest payment first (INT). Without a reason, it
   reads backwards. The reasons are short and on file:
   - the long payments carry most of the price risk, so the unbought piece is the smallest and least rate-sensitive;
   - the price risk of the waiting part is +5% vs +15% (D1; AX1b item 23, MODEL);
   - less face value is left unfunded if the deposit never comes ($31.4k vs $47.7k at -100bp, MODEL).

   The honest counterpoint also belongs in one clause: the waiting piece is the residency's first year (AX1b item 23).
2. **The 2031 method** (section 3.2 point 3).
3. **Under (ii), why WInS holds 17% stocks** when the pitch says no stock risk before the payments are bought (3.5,
   row 1).
4. **Which number is the reserve.** It is bought in 2027 and named in 2033 (case L94-95 vs the plan). E1 budgets one
   reconciling clause (P9), which is right: a case-literal reader flags this first (R-AN28).
5. **Four different stock shares for one client:**
   - WInS (ii) 17%;
   - real 2027 0%;
   - 2028-30 ~17%;
   - after 2031 ~3.5%.

   These appear if P6 element 6 is used alongside the WInS sentence. Pick one frame (F1).

### 3.5 Contradictions across the notes and the IPS

| # | Claim in one place | Clashes with | Severity (INT) | Resolution |
|---|---|---|---|---|
| C1 | Pitch/IPS: a ban on stock risk "until all ten payments are bought" (P1) | Option (ii) buys VT on day one; the notes are read before the IPS | **High** | F4: word the central idea as a split of jobs (true of both books), and put "after her 2028 deposit" inside the VT note |
| C2 | IPS: the promise costs about $292-294k | (ii) hedge is $198k (66%) | Medium | "after both deposits" inside the hedge note (ticket C2); the price of the promise goes in the reflection |
| C3 | The VT note states the split | The IPS rule 2 split; the frozen Nov 6 book must reflect the IPS (L75, VRF) | Medium | Decide the split before the VT order, or log a pre-announced research-based change and trade it before Nov 6 (AX2 D2 C3) |
| C4 | The VGSH note ("risk management/liquidity") | The IPS 2031 bottom is bought from all of the growth money | Low if the banned words are kept | Never "floor", "already owned" or "the amount she can promise" in a note (ticket section 5) |
| C5 | Notes: "moves like / stands in for" | The IPS certainty definition: "bought and held to maturity" | Low | The WInS sentence says the funds are stand-ins (P13; D10) |
| C6 | E1 P17: the $150k is doubted in at most one clause | E1 P2, P3 and P4 doubt it in three places | Medium | F10: one labelled stress clause; the rest lives in the rules' "if" branches without repeating "uncertain" |
| C7 | E1 P5 "why": the rule checks risk against "what the safe alternative pays" | The rule's yardstick is the money put in (~$157.7k), not the safe alternative | Medium (a stats-trained reader) | F6 |
| C8 | A reflection explains a split change "because we researched" | The governance line says rules never change "because markets moved" | Low | Allowed before Nov 6 (AX2 D2 C3). The reflection must name the research, not a price move |

### 3.6 What a fixed-income professional would mark wrong (red pen)

| # | Mark | Severity; deliverable | Evidence | Fix |
|---|---|---|---|---|
| R1 | **Short Treasuries (about 1.9-year duration) hold the bond half of money whose use dates are known (2031 purchase, 2033 gift).** A professional asks why the rate is not locked to those dates. Rolling short bonds adds reinvestment risk that is never mentioned | Important; IPS (rule 2), TN (VGSH note) | D3 AX1 C18: locking the bond part to 2033 is worth about $4-9k at the median (MODEL). VGSH duration 1.9y (VP via ticket) | F7(b): give one reason (the yearly reset and the 2031 purchase need money that holds its value), or make "short vs dated bonds for the growth money" a team choice before Nov 6 |
| R2 | **The barbell rejection rests on a withdrawn comparison.** "$101k bought in 2031 vs ~$165k" compares a 50% lock with an 80% lock | Important; IPS (rule 3 timing) | AX1 C6 on `D3_quant.md` (VRF): at the same 80% share, the bought floors are $161k (known in 2028) vs $165k (known in 2031). An 80% barbell beats a 20%-equity plan at every percentile (MODEL) | F7(a): withdraw it. Decide "is the facility floor bought in January 2028 or January 2031?" before Nov 6, with the surviving reasons (more money growing in 2028-30; the case's "pursuing growth"; a bad 2031-32 hits a barbell's all-stock remainder harder) |
| R3 | **The growth-share rule's yardstick is too low to test whether risk is paid.** "At most ~1 in 20 below the money put in" uses a ~$157.7k line. The same money in Treasuries at today's implied rates reaches about $204k | Important; IPS (rule 2) | $157,736 (brief s7 arithmetic, VRF); ~$204k Treasury-only (D8, MODEL; implied, not lockable; seen from today it too varies, $170k/$201k/$233k, AX1 C5). At 50/50 the rule's p5 is $168k (E1 [1], MODEL). Paths ending below the Treasury-only outcome: 42-43% (JPM) and 51-52% (Vanguard mid) at 50-60% stocks (AX2 D2 C10, MODEL) | F6 |
| R4 | **Longest-first is stated without its reason** | Minor; IPS (rule 1) | D1; AX1b item 23 (MODEL) | F7(c): one "because" clause, plus the first-year counterpoint |
| R5 | **The ladder price is a model price** from a fitted par curve, not a STRIPS quote, so the ~19bp headroom is approximate | Minor; IPS (at most one rounded price fact) | AX1 C25 (VRF inputs + ASM method) | "about", and re-price on the day (a 2027 action) |
| R6 | **"Risk management" for the hedge** is true only measured against the payments. In absolute terms the whole (ii) book falls about 6.8% per +1pp | Minor; TN | D12 finding 5 (VP durations, derived) | Keep "future funding" as the hedge's role word (ticket), and say "against the payments" if "risk" appears |
| R7 | **Odds without a model.** "about 1 in 20" (rule 2) and "about 1 in 10 above the top" (rule 3) are model properties. The model understates crash years | Minor; IPS | AX1 C12, D3 v2 (MODEL). The IPS bans citations (L123, VRF) | Mark them "under our return assumptions"; name the model in the Final Report (later list) |
| R8 | **VGSH's "12.4% instead of 20%" effect is presented as a special property** | Minor; TN | AY1 C10 | Present it as the ordinary effect of holding about half in Treasuries |

Not marked (these hold up): the certainty definition with "barring a U.S. Treasury default" (P2); STRIPS for the real
ladder (brief s8 item 11); no rolling of the 2037-42 payments (brief s8 item 2); "about 10 years" as the honest
precision (S4); US$ binding with no NT$ forward (a derivative; AX2 D4 C3); no rebalancing between reserve and growth
money, written down (CFA 2010 element 4c, VP via D8).

### 3.7 What fails "earn her confidence"

The criterion changed from "would win him/her over as a client" (2022-24) to "earn her confidence" (VP via AY1 #16;
SMApply L51, VRF). Confidence is earned by calibration, not by volume (Tenney et al. 2008, VP via D6). Against that:

- **Failing items:**
  - **Too many caveats.** At least six named risks in 480 words:
    - gap (i);
    - gap (ii);
    - the joint tail;
    - a late deposit;
    - a smaller deposit;
    - U.S. default;
    - plus building costs and currency.

    Honesty helps, but a document that is mostly about what could go wrong reads defensive (INT). Two gaps plus one
    residual, stated once, is enough for the IPS. The rest lives in the rules or the Final Report.
  - **The growth side is undersold.** E1 never tells her what she gains if markets are good, beyond "the range
    shrinks or grows". The case asks for "pursuing growth" (L73, VRF). Her verified risk words are about leaping (D13c
    V1, VP; never quoted in the TN or IPS).
  - **"Her big bets are her career."** As a diagnosis of her life, this can read presumptuous (INT). As a portfolio
    fact, it is fine: her 2028 deposit already rests on her books and speaking, so the portfolio does not add a
    second bet on the same things (D8 M081, with AY2 C14 recast as content).
  - **The statistics degree used as a lever** to make the certainty definition persuasive (AX1 C19; AY2 C6).
  - **The residency missing** from the first 50 words (2.2).
- **Passing items (keep):**
  - announce only what is bought;
  - she makes the two decisions;
  - costs never touch the bought payments (P12, if words allow);
  - no quotes, identity hooks or puns (D13 rules).

### 3.8 Errors and stale items inside E1 (for the main loop)

| # | Item | Evidence | Status |
|---|---|---|---|
| E-1 | E1 L97-98 cites D3 M238 "a 50% barbell can promise only ~$101k … vs ~$165k". Withdrawn by AX1 C6. E1 L97 also says the ratchet "matches … within $2k of median". AX1 C11: at the same p5 the ratchet is better by $2k at the median and $6k at p95. It is not dominated; the rejection stands only on the design principle | `D3_quant.md` Audit corrections (AX1) C6, C11 (VRF) | E1 predates the D3 audit (E1 L32-34 says D3 had "no audit appendix yet") |
| E-2 | P5 "why" misdescribes the rule's yardstick (money put in vs the safe alternative) | E1 P5; D6 s2.3 (VRF) | 3.6 R3 |
| E-3 | P17 limits the $150k to one clause, but P2, P3 and P4 spend three | E1 P16/P17 | 3.5 C6 |
| E-4 | P16's upper budget plus connecting words exceeds the page-fit target | D9; AX2 D10 C3 | 3.2 point 2 |
| E-5 | D3-only numbers used by E1 are pre-audit. Example: "$43k covers a 150bp fall" should add "about $51k for the worst 98-day fall since 1990, if rates do not fall further in 2027" | AX1 V4 on `D3_model_v2_results.md` (VRF) | Minor |
| E-6 | The IPS guide's explicit asks for "liquidity" and "portfolio construction and diversification" (L46, VRF) have no line in P16 | IPS guide L45-47 | F5 |
| E-7 | E1's section-4 decision checklist lacks AX1 C6's genuine team choice (floor bought in 2028 or 2031) and D3 C18's (short vs dated bonds for the growth money) | AX1 C6, C18 (VRF) | F7 |
| E-8 | `T2_red_team.md` is still absent (the task lists it as evidence) | `find`, 2026-09-28 | Informational |

---

## 4. The ten fixes that would most raise the score (ranked by score gained per hour; all INT)

Each fix says what to change, which deliverable (TN or IPS), which criteria move, and what it costs. Nothing here is
wording. The students decide.

**F1. Cut the IPS to about 12 ideas and at most ~380 content words (IPS; C&P +1, IS +0.5).**
- **Keep:**
  1. purpose and central idea;
  2. certainty definition;
  3. both gaps in one sentence;
  4. the 2027 purchase rule with its one rates-fall branch;
  5. 2028: finish the payments first, then the growth mix and its reason;
  6. risk by goal, including why so little stock and where her big bets already are;
  7. diversification and liquidity (F5);
  8. the 2031 method;
  9. 2033: reserve = the ladder, the gift, and flexibility held safely;
  10. what can change a rule;
  11. US$ binding and the building-cost assumption;
  12. the WInS sentence.
- **Cut or fold:**
  - the fee clause (AY2 C13 already says cut first);
  - the four bad-year pre-commitments as a list (fold them into "never because markets moved");
  - the three trade-offs as separate sentences (at most one "gives up X to get Y" inside rules 1 and 3);
  - P6 element 6 (stage stock shares);
  - separate deposit branches (one stress clause);
  - repeated certainty vocabulary.
- **Test:** the exported PDF ends on page 3 with at least 2 spare lines (D9/D10 checklists).

**F2. Build the IPS on four dated decisions (IPS; IS +0.5, C&P +0.5, Client +0.5).**
- Replace "Rule 1-4 + G, trigger/action" with a prose timeline: January 2027, January 2028, January 2031, January 2033.
- Each date gets one action and one "because" tied to Laura or the case. Branches become subordinate "if" clauses.
- This answers the IPS guide's "planned changes … as future funding needs approach" (L46-47, VRF) in the order a
  reader expects.
- It fits her record of dated steps (a product manager, case L17, VRF; D6 M125, INT).
- The rules' content does not change. The Final Report can still show each rule "fired as written".

**F3. Rebuild the pitch around a positive central idea (IPS; Client +0.5, C&P +0.5, IS +0.5).**
- **Elements (at most three; zero numbers; the team words them):**
  1. what is secured first, named by what it secures for the residency (years of operation), not by instrument;
  2. why only Laura gets this benefit: once bought, the promise no longer depends on her career income or on markets
     (P1 element 2; D9 M143);
  3. what the rest does, merged with the credibility idea: it grows for her facility gift, and she will tell partners
     only the part already bought.
- **Drop:** the prohibition framing as the lead (see F4); "fits inside $300k"; any date-certain claim (E1 P1 bans are
  right).
- **Test:** a reader can restate all three elements after one read (D12 protocol).

**F4. Remove the (ii) contradiction at its root (TN and IPS; IS +0.5).**
- Word the central idea as a split of jobs: the payments' money is bought and never takes stock risk; stock risk sits
  only in money the payments do not need.
- This is true of Laura's real plan and of the (ii) snapshot, where the scaled hedge is the bought promise and VT sits
  only in growth money. A time-worded ban is broken by a day-one VT buy.
- Keep the ordering (payments first) in the 2027/2028 rule, not in the pitch.
- Under (ii), the VT and hedge notes each carry their scaling marker **inside the 300 characters**, because a note is
  read before the IPS exists (ticket C2).
- **Judge lean on the book (INT):** (ii). It gives the only TN set with a growth decision, and the TN guide's first
  sentence asks for the "approach to growth" (L4-6, VRF).
  - Choose (iii) only if the team cannot state the scaling in its own words (E1's decision test).
  - (iii) with a dated rung is competitive; (iii) with only a ~$4.5k T-bill note is weak to a reader. That note earns
    about $18 against a $25 commission (ticket section 2, ASM), so it reads as filler unless the leftover rule is
    stated.

**F5. Add a diversification clause and a liquidity clause (IPS; IS +0.5, PA +0.25).**
- **Diversification content:**
  - diversified by funding purpose (R-AN45, VP);
  - the Treasury concentration is deliberate, because the bill is in US$ and dated;
  - the growth money holds one fund of about 10,000 companies worldwide (VT 10,088 stocks, VP via ticket).
- **Liquidity content:**
  - no withdrawals before 2033 (L63-65, VRF);
  - each year's payment cash arrives when its bond matures;
  - the money kept for the project sits in short Treasuries.
- About 25-35 words, paid for by F1's cuts. This answers M035 (parked, high priority) and the criterion's "uses
  appropriate diversification" (L49, VRF).

**F6. Fix the growth-share rule's yardstick and say what stocks are for (IPS; TN if (ii); Client +0.5, PA +0.5).**
- **Either** keep the loss-limit rule and describe it truthfully: a limit on the chance of losing her own money, not
  a test of whether stock risk is paid.
- **Or** add the comparison a statistics-trained client would expect: the growth mix against the all-Treasury
  alternative. Under JPM, 60% stocks add about $7-9k on average, and nothing on average under Vanguard's midpoint
  (AX1 C4, MODEL).
- **Either way, add the positive reason.** The facility has no required size (L104, VRF), and she wants growth
  (L73). So stocks are there for a bigger gift in good markets, and a bad market costs facility money only.
- **50 vs 60:** E1's robust test picks 50%. The "earn her confidence" risk (timid) points up. The median barely moves
  (+$0.2-2.1k, E1 [1], MODEL). A reader will accept either if the reason is stated as a choice of spread (AX2).
- **Judge lean (INT):** whichever the team picks, record why. Do not justify 50% by "safety" alone.

**F7. The fixed-income correction pack (IPS; PA +0.5, IS +0.25).**
- (a) Delete the $101k/$165k barbell figure (E-1). Put "facility floor bought in January 2028 or January 2031?" on
  the pre-Nov 6 decision list with the surviving reasons (R2). It is a rule the Final Report must later apply, so it
  must be fixed in the IPS (brief s17).
- (b) One clause on why the growth money's bonds are short (R1), or make "short vs dated" a pre-Nov 6 choice.
- (c) One "because" for longest-first, plus its first-year counterpoint (R4).
- (d) "About" on any ladder price (R5), and "under our assumptions" on any odds (R7).

**F8. Put the true refinement story in one reflection (TN; Articulation +1).**
- **Content:** the first plan (growth-first, ~75% equity) was tested against the case's certainty test and dropped;
  this trade is the refined plan in action (CLAUDE.md and brief s8 item 1, VRF numbers).
- Only one reflection carries it, in the team's words. It must be true as told (R-W28, VP).
- The (ii)/(iii) vote and the split decision are also real decisions with dates. Log them (P15) even if no note uses
  them.
- Assign roles before the first order (trader, note writer, second reader, log owner; E1 section 4), so the record
  shows six people.

**F9. One checkable fact per note, one extra job per reflection (TN; PA +0.25, Client +0.25).**
- **Note (≤300 characters until the box is checked):** in AY1 C1's order, Laura's dated need, then which part of the
  plan, one checkable fact, then the role word. The risk goes to the reflection if space is short.
  - **Hedge:** the payments it stands for, plus "about 10 years" rate sensitivity.
  - **VT:** only money the payments do not need, plus "after her 2028 deposit".
  - **VGSH:** its checkable number (R8 framing). Or replace it with the split-decision trade if that genuinely
    happens. Under (iii), use a listed dated rung.
- **Reflections:** the three official answers, plus exactly one of the following:
  - tested numbers (hedge);
  - scaling (under ii);
  - why so little equity (under iii);
  - the refinement story (F8).

  Assign which reflection carries which before Oct 19.

**F10. Plain-language and authenticity pass (TN and IPS; C&P +0.5, Client +0.25).**
- Apply the section 3.3 jargon table.
- Run D12's paraphrase test, with two extra target questions: restate the 2031 method, and say why longest-first.
- If 2 of 6 readers misread the 2031 method, present it by its effect (a bought bottom; part of the rest added; part
  kept) and let "about 1 in 10" carry the top. Fix q in the decision log before Nov 6, so no parameter is chosen after
  the freeze (D8).
- The team chooses its own labels for the parts of the portfolio in a meeting and logs the choice. AI-coined labels in
  permanent notes are a voice risk (R-W26, VP; SH-16).
- Use the statistics degree once or not at all (AY2 C6).
- The $150k gets one labelled stress clause (E-3).

---

## 5. Checklists (tick before submitting)

**Two-minute test (pitch + first IPS paragraph; 6 unpaid readers, D12 protocol):**
- [ ] A reader can say what is bought first and what it secures for the residency.
- [ ] A reader can say why this matters for Laura in particular (her career income).
- [ ] A reader can say what Laura will tell partners in 2031 and why it will not be walked back.
- [ ] A reader can say what could still stop a payment (two gaps plus a U.S. default), without a list of six.
- [ ] No reader thinks the WInS book contradicts the pitch (ask them after showing the three notes).

**TN trio (Oct 23):**
- [ ] Three executed trades with three different jobs, or a stated reason why not (TN L42, L53, VRF).
- [ ] Every note passes the swap test and differs from Wharton's example by one checkable fact.
- [ ] Under (ii), the scaling marker is inside the hedge and VT notes.
- [ ] Exactly one reflection is "tested", on the pre-registered window; one carries the refinement story (F8); no
      reflection does all jobs.
- [ ] No banned words (ticket section 5 list; E1 P14 vocabulary). No floor share, reserve size or range.

**Consistency (TN ↔ IPS ↔ frozen book on Nov 6):**
- [ ] The central idea is worded as a split of jobs and matches every note (3.5 C1).
- [ ] The split in the VT note equals IPS rule 2, or a logged research-based change was traded before Nov 6 (C3).
- [ ] The IPS WInS sentence names the date or state the book shows (D10, VRF requirement).
- [ ] The same labels appear in the notes, the log and the IPS (D9 M001).

**IPS: rules to fix before Nov 6 that E1 leaves open, from the reader's side** (brief s17; the Final Report must apply
them without redesign):
- [ ] The facility floor is bought in January 2028 or January 2031 (AX1 C6).
- [ ] Short vs dated Treasuries for the growth money's bond half (AX1 C18).
- [ ] The growth share (50 or 60) and the yardstick its reason uses (F6).
- [ ] a, s and q fixed in the log, cap or no cap (E1 C3-C5), stated in words in the IPS.
- [ ] The completion order (longest-first) with its reason (F7c).

---

## 6. Later (after Nov 9), one line each

- Articulation evidence beyond the notes (decision-log table, paraphrase-test log): Final Report.
- Co-sponsor communication (range in dollars, likely figure vs midpoint, fundraising excerpt): Final Report.
- The all-Treasury comparison and the named model behind every "1 in X": Final Report.
- Charts proving the "bought first" claim: Final Report (the IPS bans charts, L123).

---

## Sources

**Official files (VERIFIED-REPO-FILE; all under `competition/official/2026_27/`):**
- `Laura_Gao_2026_Client_Profile.txt`: L17, L43-45, L61-74, L85-107, L110-120, L129-133.
- `2026_WGY_Investment_Policy-FINAL.txt`: L3, L16-26, L35-36, L45-78, L82-83, L101-123.
- `2026_WGY_Trading_Notes_Analysis-FINAL.txt`: L4-31, L36-53.
- `2026_WGY_Investment_Competition_Guide.txt`: L70-90, L154-159, L183-184.
- `2026_WGY_Competition_Infographic.txt`: L40-42.
- `SMApply_Deliverables_Page_2026-09-27.md`: L49-57.

**Primary web sources, as carried and re-verified by the cited files** (not re-opened by E2):
- Wharton retired judging page (jargon line), https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages?slug=judging-and-evaluation
  (via D9/AY2).
- 2025 top-10 article (Hahn, "simple, elegant ideas"), https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
  (via D7/AY2).
- Rules & Roles and the AI policy (R-W26, R-W28; via Phase A and D10).
- SMApply Trading Details, "funding purposes" (R-AN45; via Phase A and AX2).
- van der Bles et al. 2020 and Tenney et al. 2008 (via D6/AY1).
- Russell 2026 (via D8/AY2).
- Vanguard VT facts (via the ticket).

**Research files (lower authority; audit corrections applied):**
- `research/insight_v1/phase_E/E1_change_proposals.md`.
- `phase_D/` D1-D12, D3_model_v2_results, D3_quant (AX1 appendix), D13a, D13c, and the four audit files.
- `phase_D/trading_now_brief.md`; `wins_now/securities_and_allocation_v1.md`; `wins_now/S4_red_team.md`.
- `phase_A/case_register.md` (R-AN28, R-AN35, R-AN44, R-AN45, R-AN60); `phase_A/stakeholder_map.md` (SH-16, SH-18,
  BS-03).
- `phase_C/parked.json` (M035, M033, M149).
- `research/council_2026-09-27/01_chair_memo.md` and `round2_referee_ruling.md` (history).
- CLAUDE.md.

**Script re-run:** `.venv/bin/python research/insight_v1/scripts/E1_split_and_slices.py` (2026-09-28; reproduces E1
[1]-[4]). No new script was written for this file. E2's own counts (ideas, words) are INT, from E1's text.

---

## What this teaches

1. **A reader scores what reaches them, not what you know.** The run's research is deep and mostly correct. A
   semifinal reader sees 3 × 300 characters, 3 × 100 words, 50 words and 500 words. The skill is choosing which dozen
   ideas travel.
2. **Density is a risk, like any other.** Fifty-five good ideas in 500 words scores lower than twelve clear ones,
   because the reader cannot restate any of them. Complexity must earn its place in words as well as in holdings.
3. **Word a rule so it is true everywhere the reader will look.** A rule about timing (no stocks before a certain
   step) is true of Laura's plan but visibly false in a WInS book that buys stocks on day one. A rule about which
   money may carry stock risk is true in both.
4. **Check what a rule measures before you praise it.** A rule that limits the chance of ending below the money put in
   does not test whether stock risk is worth taking. For that, the yardstick is the safe alternative.
5. **Audits keep arriving.** E1 was written before the D3 audit and still carries a withdrawn number. Before anything
   is frozen, re-read the latest corrections, even for files you already know.
