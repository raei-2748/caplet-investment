# L11: Communication, simplicity and the judge experience

Team Caplet, Wharton Global High School Investment Competition 2026-27. Lens written Fri 16 Oct 2026 (Sydney).
AI-generated analysis (Claude). It is knowledge for the team, not text to submit. It drafts no Trading Notes
reflection, IPS sentence, pitch or Final Report prose. If the team uses any of it, record that in the Final Report's
Works Cited.

**Labels.** VERIFIED = I read it in the source today. MODEL = a model estimate. UNVERIFIED = not confirmed.
new / known-deeper / known-repeat = compared with the 15 Oct team brief (`oct14/final.md`). Repo files are cited as
`path:line` (main repo `/home/user/caplet-investment`); the 16 Oct branch copy is `caplet-latest/path:line`. Wharton
pages were read on 16 Oct 2026. Evidence-pack tags like [N12] point to `oct16/research/KB_what_wins.md` section 8.

**Method.** I read IPS V5, Tab 15, the older IPS tabs (V1-V4), all 15 WInS notes, the official IPS and TNA briefs, the
case, the team's own notes, last year's team doc, and commit 412e9e3. I computed readability statistics with a small
script (`oct16/lenses/L11/readab.py`, output `readab.json`), ran the team's own draft checker on V5, applied the 13
[AI] suggestions to V5 to measure their effect, and re-ran the ladder-cost reconciliation on the 15 Oct curve. I
re-opened two judge quotes on Wharton's site today ([N12] "hiding behind fancy terms"; [D5] "Excessive investing
jargon", "make your report memorable"); both FOUND.

---

## 0. Bottom line

1. **The sentence a judge is most likely to remember from V5 is a wrong one.** The punchiest lines are the unsupported
   co-sponsor claim, "never below the floor", "cannot miss the range" and "no dollar asset is safer". The plainest true
   idea in Caplet's files ("money she already owns rather than a forecast"; "never promise money you don't own") is in
   team notes, not in V5.
2. **Sentences are not the problem. Ideas per page are.** V5 reads at about school Year 10-11 (Flesch-Kincaid grade
   10.7). That is plainer than Wharton's own IPS brief (grade 15.9) and the case (13.7). But V5 packs about 18 rules,
   7 different years and 5 dollar figures into 497 words. The team's own spec allowed "at most 12 ideas".
   Simplifying means cutting ideas, not shortening sentences.
3. **Last year's "over-complex" lesson has moved backstage.** The page now carries one strategy name (last year had
   about six named frameworks). But the AI kit the Final Report will draw on is soaked in internal jargon ("RAB" 2,206
   mentions, "p95" 1,110, "gate" 1,055, "REC" 702). The risk peaks between 9 Nov and 4 Dec.
4. **Four "costs" for the same day.** On the 15 Oct curve, the ten payments cost $294,461, $295,246, $297,847 or
   $298,628, depending on the method. For anything about Caplet's own plan, use the figure for the bonds Caplet owns
   (about $298k, room about $1.4k-$2.2k, dated 15 Oct). $294k is the price of an ideal ladder that Caplet does not own.
5. **The 16 Oct [AI] suggestions make the page denser.** Applied to V5, they double the dollar figures (5 to 10).
   They add six shares and odds written four different ways, and stretch the longest sentence to 32 words. That works
   against the brief's "Keep the presentation simple" (IPS:101-102).
6. **What an elegant Caplet story needs:** four true lines (client problem, idea, proof, trade-off), all in the case's
   own words, with no internal names and at most one dated number. V5 has a candidate for each line, but every one has
   a defect (section 5).

---

## 1. Readability numbers (computed 16 Oct 2026)

Script: `oct16/lenses/L11/readab.py` (syllables are estimated; "passive" = a form of *be* + past participle; "num" =
tokens with a digit). FK = Flesch-Kincaid grade (lower is easier). FRE = Flesch Reading Ease (higher is easier; 50-60
is "fairly difficult", 60-70 "plain English").

| Text | Words | Sent. | Avg words/sent. | Longest | % sent. >25 words | FK | FRE | Numbers | Numbers/sent. | Passives |
|---|---|---|---|---|---|---|---|---|---|---|
| IPS V5 pitch (`01_version_5.md:16`) | 47 | 3 | 15.7 | 19 | 0 | 9.6 | 54 | 2 | 0.67 | 0 |
| IPS V5 body (`01_version_5.md:20-30`) | 497 | 26 | 19.1 | 29 | 15 | 10.7 | 52 | 22 | 0.85 | 2 |
| V5 + all 13 [AI] suggestions | 498 | 26 | 19.2 | 32 | - | - | - | 31 | 1.19 | - |
| Tab 15 body | 496 | 27 | 18.4 | 29 | 15 | 10.2 | 55 | 23 | 0.85 | 3 |
| V4 body ("need to humanise") | 484 | 28 | 17.3 | 26 | 7 | 13.7 | 28 | 23 | 0.82 | 5 |
| V1 body | 483 | 26 | 18.6 | 32 | 19 | 11.4 | 46 | 24 | 0.92 | 4 |
| 11 filled WInS notes (`05_...md:14-24`) | 534 | 30 | 17.8 | 27 | 7 | 9.3 | 60 | 60 | **2.00** | 4 |
| Wharton's example note (TNA:36-39) | 59 | 3 | 19.7 | 23 | 0 | 14.7 | 25 | **0** | 0.00 | 0 |
| Wharton IPS brief (IPS:3-10, 45-52) | 200 | 9 | 22.2 | 32 | 22 | 15.9 | 21 | 0 | 0.00 | 1 |
| Laura case (full text) | 1,614 | 91 | 17.7 | 41 | 18 | 13.7 | 28 | 44 | 0.48 | 14 |
| Last year's Knox Final Report tab (`2025_knox_wharton.md:68-242`) | 3,048 | 199 | 15.3 | 55 | 12 | 12.9 | 30 | 100 | 0.50 | 9 |

Per note (filled orders): VT FK 7.1, IBTR 8.9, IBTM 9.8. The densest are the Feb-2037 note (3.0 numbers per sentence),
May-2038 (3.0) and Nov-2041 (3.5, FK 13.6). All 11 notes are 252-294 characters, right up against the 300-character
WInS box (`team/google_drive/final_report.md:17`). Wharton's own example is 413 characters and has no numbers.

**What the numbers say.** V5 is already plain at the sentence level: passive voice is rare and sentences average 19
words. The work since V4 made sentences easier (V4 FK 13.7 to V5 FK 10.7). So "write shorter sentences" is not the fix.
The load comes from the number of separate ideas, years, figures and names a reader must hold (finding COMM-02), and
from metaphors (COMM-07).

---

## 2. The memory test: what a tired judge keeps from V5

Imagine reader 900 of about 2,300, reading for 3-4 minutes. They keep the opening, one image and one claim.

| Candidate "sticky" line in V5 | Where | Status |
|---|---|---|
| "co-sponsors who fund the building rarely pay to run it" | `01_version_5.md:16` (first clause of the pitch) | Unsupported. The case says other sources "may" fund operations (case:85-86); no repo source for "rarely" (15 Oct brief section 7; JUDGE-07) |
| "Root-and-Branch", "roots", "branch" | :16, :24 | Image never explained; the phrase means "complete overhaul" in English (Merriam-Webster, VERIFIED 16 Oct) |
| "Markets can shrink the facility contribution, but never below the floor" | :28 | Not literally true: the floor is IBTM, whose "final payout is not fixed" (`05_...md:19`) |
| "so she cannot miss the range" | :30 | Same problem; the number sheet's own text says "'cannot miss' is not literally true" (`caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md:48`) |
| "no dollar asset is safer" | :24 | Vague; the team's own checker flags "safer" ("safe from what?") |
| "This policy governs the portfolio Laura Gao funds with $300,000..." | :20 | Case restatement; the same opening appears in all seven IPS versions (COMM-17) |

**The lines that should stick are not in V5.** The team's Strategy Notes say the bottom of the range "is money she
already owns rather than a forecast" (`team/google_drive/strategy_notes.md:20`). The team scoresheet names "a simple
rule we can state ('never promise money you don't own')" (`team/Winning Team Portrait and Scoresheet.md:56`). Both are
the right idea for this case, which warns that promising more than she can contribute "could damage her credibility"
(case:114-115). Who wrote those lines is UNVERIFIED, and the same note overclaims nearby ("can't break her word",
strategy_notes.md:20). The idea is the asset, not the wording. Students must say it in their own words.

---

## 3. Complexity count: is last year happening again?

**What last year's team wrote about itself:** "elegant frameworks are not always effective frameworks ... Clarity beats
complexity" (`team/google_drive/2025_knox_wharton.md:222`). Ray's lesson: "strategy packaging was over-complex for the
insight" (`CLAUDE.md:40`).

| Measure | Last year (Knox 2025-26) | This year, on the page (V5) | This year, backstage (AI kit) |
|---|---|---|---|
| Named frameworks | about 6: Greenox Matrix, Point-Line-Plane, Stewardship Surface, 3P Sleeves (Preserve / Pursue / Pioneer), Investing as Renovation (`2025_knox_wharton.md:636, 654, 670, 844`) | 1 (Root-and-Branch) plus the roots / branch image | REC, ALT, gates G1-G6, triggers A-D, vote sets A-B, sleeves, two-clock, RAB |
| Separate rules or decisions a reader must hold | n/a | **about 18** in 497 words (table below) | 10 decision memos, about 9 models (STRAT-15) |
| Distinct years | n/a | 7 (2026, 2027, 2028, 2031, 2032, 2033, 2042) | - |
| Dollar figures | n/a | 5 (4 distinct) | - |
| Names for one thing | n/a | stock fund 5-6 names; floor 4; the gift 3 (JUDGE-15, IPS-17) | - |
| WInS book | many stocks and funds | 11 lines, 3 kinds (iBond ETFs, T-bonds, one stock ETF) | - |

The 18 rules in V5, in order: (1) fund ten payments from the two deposits alone; (2) match each payment with a Treasury
or iBond fund maturing before it; (3) a floor plus growth for the facility; (4) buy the latest payments first; (5) the
2028 deposit fills any gap if the cost passes $300k; (6) the 2028 remainder buys a 2032 fund sized to return it, which
is the floor; (7) the rest goes into a world stock fund; (8) accept one issuer; (9) hold without trading, reinvesting
income in the holding that paid it; (10) a January review, acting only on two events, by switching to an earlier
Treasury; (11) in 2033 the payment bonds become the operating reserve; (12) a three-step shortfall order; (13) WInS
is a scaled-down copy; (14) never move floor money into stocks; (15) Laura's half defends against inflation and the
Taiwan dollar; (16) the 2031 range runs from the floor (rounded down) to floor + half the fund; (17) the 2033 gift is
floor + half the fund, capped; (18) the other half stays with Laura. Source: `01_version_5.md:20-30`.

That is one rule every 28 words. The team's own AI spec set "at most 12 ideas in 10 blocks"
(`research/insight_v1/ips_spec.md:70`). The scoresheet already saw the risk: "our plan looks like a pile of engineering
(four dates, a cap rule, a half-of-fund rule) ... The IPS should read as one idea plus a few rules"
(`team/Winning Team Portrait and Scoresheet.md:58`).

**Verdict.** On the page, packaging is much simpler than last year. The new risk is rule count on the page and jargon
backstage. Several of the 18 are implementation details the brief says to leave out ("rather than describing
individual investments", IPS:51-52). Rules 4, 8, 10 (the substitution clause) and 13 could move to the Final Report
without losing the strategy. The team decides.

---

## 4. Findings

### COMM-01. The lines a judge will remember are the wrong ones (high; known-deeper)
- **Problem.** A screening reader keeps one or two lines. In V5 the most quotable lines are the unsupported co-sponsor
  claim, "never below the floor", "cannot miss the range" and "no dollar asset is safer". Each is false or unsupported
  by Caplet's own numbers. The 15 Oct brief listed these as wording faults. The deeper point is that they are also the
  memorable ones, so they shape the judge's whole impression. The true, simple idea ("owned, not forecast"; "never
  promise money you don't own") is not in V5.
- **Evidence.** `01_version_5.md:16, :24, :28, :30`; `strategy_notes.md:20`; `Winning Team Portrait and Scoresheet.md:56`;
  case:114-116 ("If Laura promises more than she can ultimately contribute, she could damage her credibility");
  `IPS_number_sheet.md:48` ("'cannot miss' is not literally true"). [N12] Ko Hahn 2025: "the best solutions are made up
  of simple, elegant ideas" (re-opened today, FOUND).
- **Fix (what it must achieve).** The team picks one central idea that is literally true. Put it in the pitch and in
  the first two sentences of the IPS body. Make it the line repeated in the TNA reflections and the Final Report.
  Test: three non-finance adults read the pitch once; a day later each can repeat the idea, and none repeats a claim
  the team cannot prove.

### COMM-02. Readable sentences, overloaded page: about 18 rules, 7 years, 5 dollar figures in 497 words (high; new)
- **Problem.** V5 scores FK 10.7 and Flesch 52: plainer than Wharton's own brief (FK 15.9) and the case (FK 13.7). So
  the team may think it is "simple enough". But a judge must hold about 18 separate rules, 7 different years and 5
  dollar figures, which is one rule every 28 words. That is where "over-complex for the insight" comes back.
- **Evidence.** Section 1 table and section 3 count; `ips_spec.md:70` ("at most 12 ideas in 10 blocks"); IPS:51-52
  ("Focus on the strategy and decision-making framework ... rather than describing individual investments or presenting
  detailed financial calculations"); IPS:101-102 ("Keep the presentation simple and focus on communicating the
  investment strategy clearly"); [D3] "Why use 25 words to explain something when three will do?"
- **Fix.** Cut ideas, not words. Target: no more than about 10-12 rules, each one a decision with its trigger, in time
  order. Implementation details (latest-first buying, the substitution rule, WInS scaling, accepting one issuer) go to
  the Final Report unless the team judges them central. Re-count after each draft: rules, distinct years, dollar
  figures, names per idea.

### COMM-03. No line of the four-line story is both true and present in V5 (high; known-deeper)
- **Problem.** Wharton says judges want "the reasoning, assumptions, and tradeoffs" (Guide:183-184; Infographic:42;
  faqs.txt:83). An elegant story needs four lines: client problem, idea, proof, trade-off. V5 has a candidate for each,
  but each is flawed. Problem = the unsupported co-sponsor claim. Idea = at word 166, inside a metaphor. Proof = a stale
  "$292,000" on the wrong basis. Trade-off = a sentence other lenses show runs the wrong way (IPS-18).
- **Evidence.** Section 5 table; `01_version_5.md:16, :24, :28`; IPS-08 (idea at word 166), IPS-18.
- **Fix.** Use the structure and tests in section 5. Each line passes its test before any sentence is polished.

### COMM-04. Ladder cost: which number to say, and why the gap changes the message (high; known-deeper)
- **Problem.** On the same 15 Oct curve, Caplet's files give "about $294,000 / $5,500 headroom" (number sheet) and
  "$298,624 / $1,376" (lenses). They are both correct, for different questions. To a reader they say opposite things:
  "comfortable room" against "almost no room". The number sheet's "1 case in 3" (35%) is tied to the $294k basis. The
  lenses' MODEL for the owned bonds is about 44-45% (not re-run here), which turns "unlikely" into "nearly a coin
  flip".
- **Evidence (re-run today, `oct16/research/KB_verify/num/reconcile.py` on
  `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`, 15 Oct row):**

  | Dates priced to | Forward value at 1 Jan 2027 | Curve unchanged to 1 Jan 2027 |
  |---|---|---|
  | Payment dates (1 Jan 2033-42) | $294,461, room $5,539 (19.0bp) = the number sheet | $295,246, room $4,754 (16.3bp) |
  | Maturities of the bonds Caplet owns (iBonds 15 Dec 2032-36; T-bonds Feb-2037, May-2038, Nov-2039/40/41) | $297,847, room $2,153 (7.4bp) | $298,628, room $1,372 (4.7bp) = the lenses |

  Cause: about $3,400 comes from the dates (Caplet's bonds mature 0.5 to 10.5 months before each payment, so each
  $50,000 is bought for an earlier date and costs more). About $800 comes from the curve basis (forward vs unchanged).
  The number sheet prices to `dt.date(y, 1, 1)` (`caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:87`), yet
  says it models "WInS-listed holdings" (`IPS_number_sheet.md:5`).
- **Which is right for which claim.**
  - About Caplet's plan, the WInS book, the IBTR note or the shortfall rule: use the owned-bonds basis (about $298k,
    room about $1.4k-$2.2k on 15 Oct). State the date and "using the bonds we own".
  - About what a perfect ladder would cost, as a benchmark: $294.5k, labelled as an ideal ladder Caplet does not own.
  - The IBTR note's "about 0.2 percentage points" (6 Oct) was on the owned-bonds basis and true when written (KB
    section 7.1(a)). The note cannot be edited, so a reflection must date it.
- **Fix.** One dated figure, on the owned-bonds basis, used the same way in all three documents, or no figure in the
  IPS at all (the IPS "is not expected to include ... detailed portfolio projections", IPS:68-70). With only about
  $1,400 of room, rounding to $5,000 would erase the point. Say the margin as a rate move ("about 0.05 percentage
  points"), not as dollars.

### COMM-05. V5 does not sound like the team, and "fixing the tells" is not the fix (high; known-deeper)
- **Problem.** Creativity scores "an authentic team voice" (deliverables.txt:59). Wharton's 2025-26 semifinal rules
  asked for "your authentic team voice, not generated or generic responses" [D1]. V5 carries a doc comment, "Best
  version that AI generated" (`01_version_5.md:36`). Its rhythm follows the AI spec's own recipe, "one action and one
  'because' per case date" (`ips_spec.md:70`): four "since", one "given that" and one causal "as" in 26 sentences. It
  has three concede-then-justify sentences (:24 "may look like a weakness, but we accept it, since"; :28 "would raise
  ... but we do not, as"; :30 "We prefer ... since"). And there is no sentence only this team could have written.
- **Evidence.** As above; my word counts on `01_version_5.md:20-30`. Wharton AI policy: students "must use their voice
  and words" [W5].
- **Fix.** Do not edit AI text to hide its style. That would still be AI work presented as the team's (the 15 Oct
  brief already says rewording does not make it yours). The team writes fresh from a bullet outline. Real, team-only
  material exists for the Final Report's Articulation section: the 12:30 AM market opens in Sydney
  (`final_report.md:27`); the 5 Oct "copout" debate whose outcome is still "[fill in]" (:23); tracing the false sector
  rule to its source (:22). These are facts to tell in the students' words, not lines to copy.

### COMM-06. Complexity has moved backstage, and the Final Report will draw from it (high; known-deeper)
- **Problem.** The team's own documents are nearly free of internal jargon. The AI kit is not. The Final Report has
  25 days (9 Nov to 4 Dec) and needs projections, which live in that kit. Copying its words would bring back last
  year's problem in the one document with no word cap.
- **Evidence (grep counts, 16 Oct):** "RAB" rab/ 2,206; "p95" rab/ 1,110, research/ 479; "gate" rab/ 1,055; "rung" rab/
  724, research/ 476; "REC" rab/ 702; "STRIPS" rab/ 543, research/ 330; "bp" rab/ 350; "sleeve" research/ 1,708. In
  `final_report.md`, `strategy_notes.md` and V5: zero REC, ALT, RAB, DV01, p95, bp. Last year's own verdict:
  `2025_knox_wharton.md:222`. Volume of AI research: about 745,000 words (TP-11).
- **Fix.** Before 9 Nov, the team agrees a one-page glossary (section 6). Every Final Report number comes from one
  student-owned numbers sheet with plain labels. No term from the kit enters a deliverable unless it is on the glossary.

### COMM-07. Five image families and a literal "facility floor" (medium; known-deeper)
- **Problem.** V5 mixes a tree (roots, branch), a building (floor, top, capped), furniture (cushion), the military
  (defense) and, in the notes, a ladder. The case is about a real building, the residency facility. V5 says "facility
  floor" three times (`01_version_5.md:22` "Above the facility floor"; :24 "a facility floor" and "Laura's facility
  floor"). Read fast, that is the floor of the building. The case never uses "floor" (grep of the case text, 16 Oct).
- **Evidence.** `01_version_5.md:16-30`; the case's facility wording (case:83-86, 100-107); the "Suggested three" text
  also says "facility floor" (`05_...md:28`). IPS-17 and JUDGE-15 found the term drift. The literal reading is new.
- **Fix.** One image family at most, explained once in plain words, or none. Name the minimum gift by what it is (the
  case's own nouns: "facility contribution", plus a plain word for the minimum). Never put "facility" next to "floor".

### COMM-08. The 16 Oct [AI] suggestions double the dollar figures and mix four number formats (medium; new)
- **Problem.** Applied to V5, the 13 suggestions keep length the same (497 to 498 words) but raise digit tokens from 22
  to 31 and dollar figures from 5 to 10. They add six shares or odds written four ways ("two-thirds", "a quarter",
  "under a tenth", "7%", "two points", "99 times in 100"), and the longest sentence grows from 29 to 32 words. Suggestion
  7 alone puts "$32,000" and three fractions in one 29-word sentence. Suggestion 11's "today" has no date, and it gives
  a 2031 range the IPS "is not expected to include" (IPS:68-70).
- **Evidence.** `caplet-latest/research/ips_numbers_2026-10/IPS_v5_suggestions.md:9-21`; my script output (section 1
  table, row "V5 + all 13 [AI] suggestions"); IPS:51-52, 101-102.
- **Fix.** If the team takes facts from that file, take facts, not sentences (authorship: COMM-05; INT-01). Keep the
  IPS to principles, with at most one dated figure on the right basis (COMM-04).

### COMM-09. "Secure in about 93-95 cases in 100" says two opposite things at once (medium; new)
- **Problem.** The number sheet's option 1 wording puts a certainty word next to a failure rate: "payments are secure
  in about 93-95 cases in 100 from the plan alone" (`IPS_number_sheet.md:50`). Suggestion 12 puts "about 99 times in
  100" on the co-sponsor range (`IPS_v5_suggestions.md:20`). Side by side, a reader sees the range described as surer
  than the payments, the reverse of the case's priority (case:91-92; JUDGE-03). This is a wording trap even before it
  is a strategy question.
- **Evidence.** As above; case:91 ("All ten payments must be funded by the investment portfolio with a high degree of
  certainty").
- **Fix.** Certainty words only where they are literally true. Any probability says "in our model", gives its date,
  and is stated once, in one format (COMM-16). The team decides whether a probability belongs in the IPS at all.

### COMM-10. The team's own draft checker passes V5's jargon, and V5 breaks the team's own word rules (medium; new)
- **Problem.** `research/insight_v1/scripts/D9_draft_checker.py` reports V5's pitch "Jargon ... none" and "Overclaim
  ... none". Its jargon list targets backstage words (DV01, p95, sleeve, STRIPS: lines 56-61). It misses the words V5
  actually uses: "secure(s)", "never", "cannot", "defined-maturity", "rate-sensitive", "issuer", "equities", "facility
  floor", and the unsupported "rarely". Separately, V5 uses words the team's own spec told it to avoid: "We match each
  payment" (V5:20) against "avoid ... 'matched'" (`ips_spec.md:157`); the IBTR note's "top up the ladder" (`05_...md:15`)
  against the banned list "ladder" (`ips_spec.md:53`, which applies to the pitch).
- **Evidence.** Checker run today on `01_version_5.md:16` and `:20-30` (read-only; it only flagged "safer", "match",
  "certainty" in the body and quotation marks in the pitch).
- **Fix.** Do not treat a clean checker run as a plain-English pass. Use the human tests in section 5 and the blacklist
  in section 6. If anyone updates the checker, its list should be the words in the drafts, not the words in the kit.

### COMM-11. Not all jargon costs the same: judges know "Treasury"; nobody knows "the branch" (medium; new)
- **Problem.** The Top 50 readers in 2025-26 were "Wharton School student evaluators" and "a professional review panel
  of asset managers from Aberdeen Investments" [N14]. They know "Treasury", "yield", "ETF" and "ladder". What costs
  marks is the team's own words that need decoding: roots, branch, floor, cap, the half, the 2027 leftover, the 2028
  remainder. These cost a judge effort and a lay reader even more. The co-sponsor text is judged on being "clear and
  credibl[e] to prospective co-sponsors" (deliverables.txt:59), who are not finance readers. The team's own client
  notes say: "Avoid finance-bro tone and jargon. She left that world on purpose." (`notes_and_discussions.md:544`).
- **Evidence.** As above; [D5] "Excessive investing jargon doesn't necessarily dazzle the judges" (re-opened today,
  FOUND); [N20] Roberts, "the jargon and acronyms are just obfuscating the elegant simplicity of finance" (FROM R1).
- **Fix.** Three tiers. Standard finance words: fine in the IPS and TNA, used correctly, once defined if unusual.
  Team-made words: banned unless defined once and used identically everywhere. Co-sponsor material: everyday words
  only, tested on a non-finance adult ([D3] "someone that has no prior investing knowledge").

### COMM-12. Use the case's words for the case's ideas (medium; known-deeper)
- **Problem.** The judges wrote the case's terms, so those terms need no definition. V5 swaps several for its own. It
  says "high certainty" for the case's "high degree of funding certainty" (case:91, 98). It says "cushion" and "the
  half Laura keeps" where the case says "financial flexibility" (case:103). The pitch says "building" where the case
  says "facility". Each swap costs a reader a translation step and loses the match to the criteria wording.
- **Evidence.** `01_version_5.md:16, :20, :30`; case:83-107; criteria wording deliverables.txt:55-59 ("funding
  reliability", "financial flexibility", "facility contribution"). CLIENT-01 and CLIENT-16 found the dropped
  concepts. The point here is the cost to the reader.
- **Fix.** Make a term map: each case idea, the case's exact word, and the one word the team will use. Coin a word only
  where the case has none (for example, the minimum gift). Use the map in all three deliverables.

### COMM-13. The notes are packed to the 300-character limit; the reflections must breathe (medium; new)
- **Problem.** The 11 filled notes run 252-294 characters, with 60 numbers in 30 sentences (2.0 per sentence).
  Wharton's example note has none. The TNA quotes each note "exactly as it appears in WInS" (TNA:44), then 100 words
  of reflection. If the reflections also average two numbers a sentence, the judge reads about 450 words of figures
  with no plain "why". Each note starts with a Wharton role word ("Future funding:", "Growth:"), which matches the
  Guide's own list (Guide:85-86). That is a strength to keep.
- **Evidence.** Character counts and readability table (section 1); `05_...md:14-24`; TNA:36-39, 44-52;
  `final_report.md:17` (300-character box).
- **Fix.** Each reflection carries the reason in plain words. Use at most one dated number per reflection, labelled
  as market price or model. Do not repeat a number already in the quoted note unless it is updated with a date.

### COMM-14. The clearest trade-off in the whole entry is already in a filled note (medium; known-deeper)
- **Problem.** The IBTR note gives a concrete if-then rule with a client consequence: "If yields fall more than about
  0.2 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility"
  (`05_...md:15`). That is the shape judges reward ("tradeoffs", Guide:184). V5's own trade-off sentence (:28) is the
  one other lenses show runs the wrong way (IPS-18). The note's number is stale: about 4.7-7.4bp of room on 15 Oct on
  the owned-bonds basis (COMM-04).
- **Evidence.** As above; 15 Oct brief section 6 (IBTR pick).
- **Fix.** Make the IPS and Final Report trade-off use the same structure and the same words as the note (cause,
  rule, cost to Laura), so the three documents agree. The IBTR reflection dates the note's figure and gives the
  current one on the same basis.

### COMM-15. Dates and time zones: Sydney dates in a reflection will not match WInS (medium; new)
- **Problem.** WInS shows US Eastern times in US numeric format ("10/07/2026 04:42:53 AM" is 7 Oct, `05_...md:15`). To
  an Australian, "10/07" reads as 10 July. The team lives in Sydney time (journal: "Oct7: ... 12:30 AM that the market
  would open", `final_report.md:27`; that is 6 Oct in New York). Team files describe the same trades as "filled 7-8
  Oct" (`CLAUDE.md:8`; `COMPETITION.md:172`), while the orders were placed 6-7 Oct ET (`05_...md:14-24`). Wharton
  says "we will verify" the notes against WInS (TNA:53). A reflection that says "on 7 October we bought IBTM" (Sydney)
  will not match WInS's 10/06 (ET).
- **Evidence.** As above. Clock check: Sydney is on AEDT (UTC+11) from Sun 4 Oct 2026; US Eastern moves from EDT
  (UTC-4) to EST (UTC-5) on Sun 1 Nov 2026. So the gap is 15 hours until 1 Nov and 16 hours after.
- **Fix.** In deliverables, give WInS events in ET as WInS shows them, with month names ("6 Oct 2026, ET"). Market
  data uses the US date of the close. Team deadlines use Sydney time with ET in brackets. Say "placed" or "filled",
  not both loosely.

### COMM-16. Odds and shares are written six ways; pick one (medium; new)
- **Problem.** Across the number sheet and suggestions: "1 case in 3 (35%)", "99.4% of 200,000 paths", "about 99 times
  in 100", "93-95 cases in 100", "about 1 in 50", "3 cases in 4", "90% band", "0.19 points of yield", "0.1 point", plus
  "percentage points" in the notes and "bp" in team memos. Mixed formats make a reader convert, and conversion is where
  trust drops.
- **Evidence.** `IPS_number_sheet.md:12-19, :42-50`; `IPS_v5_suggestions.md:15, :18, :20`; `05_...md:15`.
- **Fix.** The number rules in section 7. One odds format ("X in 100"), "percentage points" for yield changes, never
  "bp" in a deliverable, and every model number labelled with its date.

### COMM-17. The same case-restating first sentence survived seven drafts (medium; known-deeper)
- **Problem.** Every IPS body, V1 to V5 and Tab 15, opens "This policy governs ..." and restates the two deposits and
  the residency (V1-V3, V5, Tab 15: "the portfolio Laura Gao [will] fund(s) with $300,000 in January 2027 and $150,000 in
  January 2028 for the Taiwan creative residency..."; V4 words it slightly differently). The first words a
  judge reads are the facts the judge wrote. Wharton warned: "Don't use precious space repeating known facts about your
  client" [D5, re-opened today], and a strategy "buried ... rather than clearly stated, defined and articulated up front"
  will "not be among the strongest teams" [W6]. The idea first appears at word 166 (IPS-08).
- **Evidence.** `01_version_5.md:20`; `15_tab_15.md:10`; `02_v4_need_to_humanise.md:20`; `08_old_versions_v3.md:20`;
  `11_old_versions_v2.md:22`; `13_old_versions_v1.md:20`.
- **Fix.** The first sentence of the IPS body states the team's central idea, not the case. Swap test: if the first
  sentence would still be true for every team in the competition, replace it.

### COMM-18. Names a bond judge reads differently: "Caplet", "cap", "floor", "root-and-branch" (low; new)
- **Problem.** To a fixed-income reader, a caplet is one period of an interest-rate cap. That is an option, a
  derivative, and WInS bans derivatives. "Cap" and "floor" are also the names of interest-rate derivatives. V5 uses
  "floor" 10 times and "capped" once, under a team named Caplet. Separately, "root and branch" means "complete or
  thorough" ("a root and branch overhaul") in Merriam-Webster, an odd label for a hold strategy. A credit specialist
  sat on the 2024-2026 finale panels [N10][N13][N16]. The team name is fixed by the roster. The strategy words are not.
- **Evidence.** https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor (accessed 16 Oct 2026): "The interest rate
  cap can be analyzed as a series of European call options, known as caplets"; https://www.merriam-webster.com/dictionary/root-and-branch
  (accessed 16 Oct 2026): "complete or thorough". Trading Details: derivatives not permitted (CLAUDE.md key facts,
  VERIFIED 27 Sep). Strategy-name drift: COH-09.
- **Fix.** Ask two outside adults, one with finance training, what the strategy name suggests. Use plain words for
  the top of the range (avoid the noun "cap"). Explain any name once, literally. Optional: the team can decide to own
  the joke in a presentation. That is their call.

### COMM-19. Mixed US and Australian spelling (low; new)
- **Problem.** V5 and Tab 15 use the US "defense" (`01_version_5.md:28`; `15_tab_15.md:18`); V4 used the Australian
  "prioritise" (`02_v4_need_to_humanise.md:24`). Small, but a mix inside one team's documents reads as several authors
  or tools.
- **Fix.** Pick one convention (Australian spelling is the team's real voice) and apply it to all three deliverables.

---

## 5. Structure of an elegant Caplet story (a test, not text)

What winners and judges said they value (KB section 4): "less is more" and "Cut slides, cut words, cut minutes" [N3];
"an explainable strategy" [N7]; "simple, elegant ideas" and not "hiding behind fancy terms and formulas" [N12];
"connect the client's objectives to an investment strategy" [N9]; a strategy is "a set of rules and guidelines; a plan
of attack" [D4]; "Choose active language, illustrate with examples and make your report memorable" [D5].

| Line | What it must contain | Pass test | V5 today | Status |
|---|---|---|---|---|
| **1. Client problem** | The case's own problem in the case's words: ten fixed $50,000 payments, from the portfolio alone, with a "high degree of funding certainty"; and in 2031 she must name a range without overpromising | Every noun can be found in the case (case:88-92, 110-116). No claim about co-sponsors' habits. A judge nods, nothing to check | "co-sponsors who fund the building rarely pay to run it" (:16) | Fails (unsupported; not the case's stated problem) |
| **2. The idea** | One rule, in verbs, that a 12-year-old could repeat. It must explain both the payments and the range | Swap test (false for any other client). Explain-back by a non-finance adult after one read. No team-made word needing a definition | "secures the roots, the payments and a facility floor, before investing in the branch" (:24, word 166) | Partly (right idea, buried, in metaphor) |
| **3. The proof** | One fact that stays true until 4 Dec and that a judge can check. Best: structural (what was bought, matched to which year), not a market number. If a number: owned-bonds basis, dated, labelled | A judge could check it in WInS or on treasury.gov. It is still true on 4 Dec. It matches the TNA notes | "At late-September 2026 yields they cost about $292,000" (:24) | Fails (stale; wrong basis; COMM-04) |
| **4. The trade-off** | What Laura gives up, in her terms, in the right direction, and why she accepts it (the case's credibility warning) | States a cost a client would feel. The direction is right by the team's own model. Same words as the IBTR note's rule (COMM-14) | "Moving floor money into equities would raise the expected contribution, but we do not" (:28) | Fails (direction disputed, IPS-18; the real trade-off is unstated) |
| (optional) **5. Bad year** | What Laura sees in a bad market year | Answers the 2024 judge prompt about clients' emotions in a downturn [N10, paraphrase, FROM R1] | :28 "Markets can shrink ... never below the floor" | Fails (absolute) |

**Whole-story tests (pass all before polishing):**
- The four lines fit on one index card and use no word from the blacklist (section 6).
- Three outside readers (one non-finance) restate lines 1-4 after one read. Unpaid readers only (paid help is banned).
- The same four lines, in the same words, appear in the IPS pitch and body, the TNA reflections where relevant, and
  the Final Report (consistency with the IPS is scored, deliverables.txt:55; the three are read together, case:161).
- Each line is literally true by the team's own numbers on the date stated.
- Each student can say all four lines aloud, without notes, in their own words (semifinal: "All team members must
  participate", faqs.txt:89).

---

## 6. Jargon blacklist with plain replacements (single words or phrases)

Tier A = team-made words (ban in deliverables unless defined once and used identically). Tier B = finance terms (fine
for judges if correct; replace in co-sponsor text). Tier C = overclaims (replace always).

| Avoid | Tier | Plain replacement |
|---|---|---|
| RAB, Root-and-Branch vs Roots First (two names) | A | one agreed strategy name, or "our plan" |
| roots | A | "the payment bonds" |
| branch | A | "the world stock fund" |
| floor, facility floor | A | "minimum gift" / "minimum" |
| cap, capped (noun or verb) | A | "upper limit" / "top of the range" |
| cushion, the half Laura keeps | A | "Laura's flexibility money" / "her share" |
| 2027 leftover | A | "spare cash from 2027" |
| 2028 remainder | A | "the rest of the 2028 deposit" |
| sleeve, tranche | A | "part" / "fund" |
| gate, trigger, vote set, REC, ALT | A | never in a deliverable; "decision", "rule" |
| MODEL / holdings basis | A | "our estimate" / "using the bonds we own" |
| headroom | A | "money to spare" |
| rung | A | "bond for one year" |
| global index fund / equity fund / equity half / equities | A/B | "the world stock fund" / "stocks" |
| operating payments, high certainty | A | the case's words: "operating commitment", "high degree of funding certainty" |
| building | A | "facility" (the case's word) |
| defined-maturity Treasury ETF, iBond | B | "a Treasury fund that pays out in a set year" |
| ladder | B | "bonds maturing each year" (judges know "ladder"; define once) |
| rate-sensitive, duration | B | "moves most when interest rates change" |
| reinvestment-rate risk | B | "risk that interest earned later is lower" |
| coupon | B | "interest payment" |
| proceeds | B | "the money repaid" |
| issuer | B | "borrower" / "the US government" |
| yield curve, Treasury curve | B | "Treasury interest rates on [date]" |
| premium (fund price) | B | "price above what it holds" |
| bp, basis points | B | "percentage points" |
| DV01 | B | "cost of a 0.01-point fall in rates" |
| p5 / p50 / p95, percentile, band, paths | B | "bad case / typical / good case", "simulated futures" |
| Monte Carlo | B | "simulated futures" (Final Report only) |
| liability-driven, LDI, cash-flow matching, immunisation | B | "buy the payments first" |
| glide path | B | "shift to bonds over time" |
| scaled to the model portfolio | B | "a smaller copy of Laura's plan" |
| payout is not fixed | B | "the final amount can vary slightly" |
| secure, guaranteed, risk-free, never, cannot miss, promised (for the upside) | C | "bought", "owned", "designed to", "in our model, in X of 100 cases" |
| no dollar asset is safer | C | name the risk removed: "backed by the US government" |
| rarely (co-sponsor habits) | C | the case's "may" |

---

## 7. Rules for numbers

1. **One claim, one figure, everywhere.** The same dated figure in the TNA, IPS and Final Report. A different figure
   needs a stated reason (a new date).
2. **Date and type on every market or model number.** "15 Oct 2026 US close, using the bonds we own" or "our model, 15
   Oct curve". Never a bare "today" (suggestion 11 says "today").
3. **Right basis.** Caplet's plan = the owned-bonds basis (COMM-04). Ideal-ladder figures only as a labelled benchmark.
4. **Rounding.** Dollars in text to the nearest $1,000. Ranges to the nearest $5,000. Shares to whole percent. Yields
   and fees to two decimals ("0.06%"). Never six-figure precision ("$294,453") outside a table or the Works Cited.
5. **Small margins.** When rounding would erase the point, give the margin as a rate move ("about 0.05 percentage
   points of room on 15 Oct") rather than in dollars.
6. **Rates.** "Percentage points" for changes in yields. "%" for levels, fees and returns. Never "bp", and never
   "points" on its own.
7. **Odds.** One format: "X in 100". Always "in our model". No probabilities in the pitch. In the IPS only if the team
   decides (the brief does not ask for one, IPS:68-70).
8. **Plan vs WInS scale.** Say which: Laura's plan ($300k plus $150k) or the WInS copy ($300k; smaller rungs, about
   $33-34k each, STRAT-10, TNA-20).
9. **Currency.** "$" means US dollars. Write "US$" once at first use if Taiwan dollars appear; write "NT$" for Taiwan
   dollars.
10. **Dates.** Day, month name, year ("1 Jan 2033"). Never numeric dates (10/07/2026). Years as digits.
11. **Time zones.** WInS events in ET as WInS shows them. Market data by US close date. Team deadlines in Sydney with ET
    in brackets. 15 hours apart until Sun 1 Nov, 16 hours after.
12. **Fewer numbers in the IPS.** Each figure like "$292,000" may count as one or two words depending on the counter
    (UNVERIFIED; 15 Oct brief section 7). Fewer numbers also means fewer things that go stale before 6 Nov.

---

## 8. Does commit 412e9e3 change these conclusions?

- **Numbers.** It adds a third "cost" to the conversation ($294k, on the ideal-ladder basis). This makes COMM-04 more
  urgent, not different.
- **[AI] suggestions.** They increase number density (COMM-08), mix formats (COMM-16) and insert a probability that
  reads as surer than the payments (COMM-09). They do not change the memory-test result: the pitch is untouched
  (`IPS_v5_suggestions.md:23`), so its unsupported first clause stays.
- **The rule change** (`caplet-latest/CLAUDE.md:26-30`). From a communication view, accepted AI sentences cannot
  produce "an authentic team voice" (deliverables.txt:59). Authorship is covered in depth by INT-01, IPS-01 and JUDGE-02.
- **No change** to the findings on concept density, metaphors, case words, dates and time zones.

---

## 9. Files produced

- `oct16/lenses/L11/readab.py` (readability script) and `oct16/lenses/L11/readab.json` (all statistics).
- `oct16/lenses/L11/v5_pitch.txt`, `v5_body.txt`, `v5_after_ai.txt` (inputs used for the measurements).
- `oct16/lenses/L11/web/wp3778.json` (fresh copy of Wharton's Judging and Evaluation page, 16 Oct 2026).
