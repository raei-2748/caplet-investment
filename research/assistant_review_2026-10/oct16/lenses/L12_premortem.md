# L12 Pre-mortem: why Caplet did not make the Top 50

Prepared Fri 16 Oct 2026 (Sydney) for Team Caplet. AI-generated analysis (Claude). It is knowledge for the team, not
text to submit. It contains no Trading Notes reflections, IPS text, pitch or Final Report prose. If the team uses any
of it, record that in the Final Report's Works Cited (Wharton AI policy).

**Labels.** VERIFIED = I read it in the primary file or page today. MODEL = a computed estimate. AI ESTIMATE = my
judgement (Wharton publishes no weights or scores). FROM Lxx / FROM KB = taken from a sibling lens or the evidence pack
and not re-opened by me. UNVERIFIED = could not confirm.
**Citations.** Repo files as `path:line` (main repo `/home/user/caplet-investment`); the 16 Oct branch copy as
`caplet-latest/path:line`. Official files are in `competition/official/2026_27/`. Web pages accessed 16 Oct 2026.
**New / known** is relative to the 15 Oct team brief (`scratchpad/oct14/final.md`).

---

## 0. The short version

It is 27 Jan 2027. Caplet is not in the Top 50. The most likely reason is **not** the strategy. The strategy idea is
good. Caplet most likely lost on the parts only students can earn: a true, detailed experience story, an authentic
team voice, and numbers and rules the students own and explain the same way in all three documents. The warning signs
are visible today, and most of the fixes are cheap.

The odds are long. Last year 49 teams were picked from 2,339 final reports (2.1%), and Wharton wants teams that "score
exceptionally well on all five components" (faqs.txt:79). That means the weakest criterion decides. Caplet's weakest
criteria are Articulation and Creativity (voice). Almost all effort so far (about 730,000 words of AI research and
tools) has gone into the strongest ones, Strategy and Portfolio Analysis.

**Three things to do this week:** (1) the whole team votes on what the 16 Oct "[AI] suggestions" rule may cover, before
any suggestion is accepted; (2) decide the number sheet's "pick one" question (how payments are protected after 2033)
before writing the IBTM and VT reflections, because it changes what they can truthfully say; (3) fill the journal's
blanks now, from dated records, while memories are fresh.

---

## 1. The scale and the bar (VERIFIED)

| Fact | Evidence |
|---|---|
| 2025-26 counter on Wharton's main page: 2,339 teams | `data-counter-value="2339"` in the page HTML, https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ (accessed 16 Oct 2026) |
| Top 50 picked "Following the submission of final reports" by "a panel of judges"; Semifinals are "virtual" | same page, text line 382 of my fetch (`oct16/lenses/L12_main.txt:382`) |
| "success is not determined by portfolio performance" | same page, line 380 |
| 2025-26 Top 50 list had 49 teams; 2.1% of reports | FROM KB `KB_what_wins.md:27,67,117` |
| Selection rate falling: 3.8% (2021-22) to 2.1% (2025-26) | FROM KB `KB_what_wins.md:117` |
| "score exceptionally well on all five components of the criteria" | `smapply_public_2026-10-14/faqs.txt:79` |
| Three deliverables evaluated and read together | `deliverables.txt:27`; `Laura_Gao_2026_Client_Profile.txt:161` |
| No Australian team in a Top 50 since 2021-22 | FROM KB `KB_what_wins.md:51-52, 365-369` |

**What this means (AI ESTIMATE).** If 2,300 or more reports arrive again, the Top 50 is the top 2%. Most of the teams in
the top 10% will be competent. Picking 50 from about 230 strong entries is partly noise. So Caplet needs a margin on
every criterion, not a brilliant idea plus gaps. One weak criterion is enough to fall out.

---

## 2. Failure stories, ranked

AI ESTIMATE of how much of the "not selected" outcome each story explains, given today's path. The stories overlap.
Three root causes sit under most of them (section 2.2).

### 2.1 Ranking table

| Rank | Failure story (as told on 27 Jan) | Share | Early warning visible today | Cheapest prevention | Deadline (Sydney) |
|---|---|---|---|---|---|
| 1 | **The Final Report was written in the last days.** Articulation was generic and Portfolio Analysis thin. | 25% | Journal is 421 words and stops 7 Oct, with "[fill in]" blanks (`team/google_drive/final_report.md:16,23,25`); client portrait says "Placeholder for now" (`client_portrait.md:14`); last year 30 of 63 dated comments came in the last two days (my count) | Pre-build before instructions: journal current, owners per section, student-built projection table, WInS records captured | Sun 8 Nov |
| 2 | **The voice read as AI or generic.** Creativity ("authentic team voice") and trust fell. | 20% | IPS V5 comment: "Best version that AI generated" (`ips_report/01_version_5.md:36`); 16 Oct rule lets AI suggest wording (`caplet-latest/CLAUDE.md:26-29`); 13 AI rewrites drafted (`caplet-latest/research/ips_numbers_2026-10/IPS_v5_suggestions.md:9-21`) | Team vote limiting [AI] items to facts, numbers and flags; fresh student IPS from an outline | Vote Sun 18 Oct; outline Wed 28 Oct |
| 3 | **It looked like many other competent ladders.** Nothing stuck in a judge's memory. | 15% | Wharton set a fixed-payment case before (2021-22, FROM KB:290-294); V5 pitch leads with an unsupported co-sponsor claim (`01_version_5.md:16`); distinctive ideas sit in AI files judges never see | Pick three signature ideas; say them the same way in all three documents | IPS outline Wed 28 Oct |
| 4 | **The IPS locked rules with visible holes.** A bond reader saw them; the Final Report could not fix them. | 15% | "High degree of certainty" undefined; V5 says "never below the floor" and "cannot miss" (`01_version_5.md:28,30`); team's own model: range 99.4% sure but a later payment short in 6.3% of paths (`caplet-latest/.../results.json:130,138`) | Decide the protection option; write a one-line certainty definition; drop absolute words | Option by Tue 20 Oct; rules by Tue 27 Oct |
| 5 | **The three documents disagreed.** Numbers, names and claims did not match. | 8% | Two ladder costs on the same curve ($294.5k vs $298.6k, section 3); room fell from $4,007 to $1,372 in one day; the VT note says stocks "only" set the gift (`05_...wins_trading_notes.md:14`) while V5 gives Laura's half more jobs (`01_version_5.md:26,28,30`) | One dated number sheet on the holdings basis; state rules, not point claims | TNA Tue 20 Oct; IPS Wed 4 Nov |
| 6 | **Good, but not top-50 good.** Noise among strong entries. | 7% | No public winner reports exist (FROM KB:47-49); selection rate falling | Make the report easy for a hurried reader: answer first, plain words | Through 4 Dec |
| 7 | **A hard gate failed.** Format, note, letter or submission. | 5% | IPS V5 at 47/50 and 497/500 words; four notes sit on cancelled orders (`05_...:33-40`); school letter not yet requested (15 Oct brief); only the leader can submit | Format checklist with two counters; submit a day early; letter by 20 Nov | 22 Oct, 5 Nov, 20 Nov, 4 Dec |
| 8 | **An integrity flag.** Invented stories, a false AI statement, contact with Laura, or text that matches another team. | 5% | Last year's doc: "Make up stories, and make them sound realistic" (`2025_knox_wharton.md:3827`); disclosure template says students "wrote all submitted text" (`caplet-latest/docs/AI_USE.md:91`); COMPETITION.md says "Laura is a fictional client" (`caplet-latest/COMPETITION.md:49`) | Fill blanks only from records; true AI entry from a real log; fix the "fictional" line | Sun 18-25 Oct |

### 2.2 Root causes under the stories

1. **Effort is pointed at the strongest criteria** (PM-01). About 537,000 words in `research/` and 161,000 in `rab/`
   (my count of .md/.txt files) against a 421-word experience journal.
2. **The team has not yet owned the key calls** (PM-09). "The team deferred to the assistant's evidence-based calls"
   (`CLAUDE.md:75`). Debates are recorded as "[fill in]".
3. **Advice is not turning into action** (PM-08). The day after the 15 Oct brief, none of the repo items it listed
   were done, and its first item was reversed.

---

## 3. The ladder-cost conflict, resolved (VERIFIED by re-running)

I re-ran the evidence pack's script (`oct16/research/KB_verify/num/reconcile.py`) on the official October curve
(`caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`). Same curve, same ten $50,000
payments, same bootstrap. Only the dates priced to and the curve basis change.

| Curve date | Dates priced to | Basis | Cost at 1 Jan 2027 | Room under $300k |
|---|---|---|---|---|
| 15 Oct | payment dates (1 Jan 2033-42) | forward | $294,461 | $5,539 (19.0bp) - **the number sheet** |
| 15 Oct | payment dates | yields unchanged | $295,246 | $4,754 (16.3bp) |
| 15 Oct | maturities Caplet owns (15 Dec 2032-36, Feb-2037, May-2038, Nov-2039/40/41) | forward | $297,847 | $2,153 (7.4bp) |
| 15 Oct | maturities Caplet owns | yields unchanged | $298,628 | $1,372 (4.7bp) - **the lenses** |
| 6 Oct | maturities Caplet owns | yields unchanged | $293,453 | $6,547 (23.0bp) - basis of the IBTR note's "about 0.2" |

Day by day on the holdings basis (yields unchanged): 9 Oct room $5,679 (19.9bp); 13 Oct $4,705; 14 Oct $4,007
(13.9bp); 15 Oct $1,372 (4.7bp). **One day (14 to 15 Oct) moved the cost by $2,635, about twice the room left.**

**Why they differ.** The number sheet prices each $50,000 to 1 January of the payment year
(`caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:86`, `dt.date(y, 1, 1)`). Caplet's holdings mature 2 weeks
to 10.5 months earlier, so each $50,000 must be bought for an earlier date and costs more. That explains about $3,400
of the gap. The forward-vs-unchanged basis explains the other ~$800. Neither figure is an arithmetic error.

**Which is right for which claim.**
- Anything about Caplet's plan, WInS book, notes or reflections: the **holdings basis**, about **$298k, room about
  $1.4k-$2.2k (5-7bp) on 15 Oct**, always with its date and basis.
- $294.5k is the cost of an ideal ladder that matures on each payment date. Caplet does not own it. Use it only if the
  sentence says so. The number sheet calls its model "Root-and-Branch on WInS-listed holdings"
  (`IPS_number_sheet.md:5`) but its headline does not price those holdings.
- The sheet's "1 case in 3 (35%)" chance of costing more than $300k is anchored to $294.5k
  (`ips_numbers.py:122`; `results.json:35`), so it is too low for the real holdings. Sibling lenses estimate about
  44-45% (MODEL, FROM L03/L08).
- Pre-mortem point: the room is now smaller than one day's move. Any document that says "the first $300,000 buys all
  ten" or "it does not" will be right or wrong by luck when a judge reads it in December or January. Write the rule
  (what happens either way), not the forecast.

---

## 4. Findings

### PM-01 - The weakest criterion decides, and effort is pointed at the strongest ones (critical, known-deeper)
- **Problem.** Wharton wants teams that "score exceptionally well on all five components" (faqs.txt:79). A strong
  strategy cannot carry a weak Articulation score. Caplet's AI work is huge on Strategy and Portfolio Analysis and
  tiny on Articulation and voice, the two criteria only students can earn.
- **Evidence.** faqs.txt:79; criteria `deliverables.txt:55-59`. My word counts (.md/.txt): `research/` 537,267;
  `rab/` 161,161; `docs/` 26,616. The experience journal: 421 words, last entry 7 Oct (`final_report.md:14-27`). A
  simulated panel scored Articulation 2/10, the lowest of the five (FROM L01, AI opinion). 2,339 reports last season
  (main page counter, VERIFIED).
- **Fix must achieve.** From now to 4 Dec, most team hours go to the student-only work: the journal, decisions
  argued and recorded, own-voice drafting, and students rebuilding the key numbers. No new AI research waves until
  the TNA and IPS are submitted.
- **Deadline.** Agree the split at the Sun 18 Oct meeting.

### PM-02 - Story 1: the Final Report crunch (critical, known-deeper)
- **Problem.** The Final Report alone carries Portfolio Analysis (projections "under varying market outcomes"), most of
  Articulation, and the co-sponsor part of Creativity. It has a 25-day window this year. Last year's Knox report was
  mostly written at the end. If that repeats, the experience story is thin and generic, and the projections are not
  the students' own.
- **Evidence.** Instructions "shared on November 9" (`deliverables.txt:51`); last year's criteria came 46 days before
  the deadline (FROM KB:134-136). My count of dated comments in last year's team doc
  (`team/google_drive/2025_knox_wharton.md`): 63 in total, 30 on 11-12 Dec 2025 (deadline 12 Dec). Journal stops 7 Oct
  with three placeholders (`final_report.md:16,23,25`); "Placeholder for now" (`client_portrait.md:14`). Knox Term 4
  ends Thu 3 Dec, the day before the deadline in ET (FROM L10, not re-opened).
- **Fix must achieve.** By Sun 8 Nov, before the instructions arrive: (a) the journal is current and dated; (b) each
  likely section has a named student owner; (c) a student-built projection table exists for the plan in the IPS
  (good, middle, bad markets; stated return and inflation assumptions; case:146-149); (d) WInS order and transaction
  history is saved privately; (e) notes for the co-sponsor paragraph exist. The draft is complete by about Sun 29 Nov,
  leaving the last week for checking, not writing.
- **Deadline.** Pre-build Sun 8 Nov; full draft Sun 29 Nov; submit Fri 4 Dec (Sydney), a day early.

### PM-03 - Story 2: the voice reads as AI, and the 16 Oct rule makes that more likely (critical, known-deeper)
- **Problem.** Creativity scores "an authentic team voice" (`deliverables.txt:59`). The current IPS is AI-generated by
  the team's own note. The 16 Oct rule lets AI put wording into all three deliverables. The IPS bans citations, so any
  AI sentence accepted into it is judged with no credit shown. An earlier AI run tuned the exemplar IPS against "an
  AI-voice detector", which looks bad if it is ever seen.
- **Evidence.** "Best version that AI generated; We cannot submit as it is" (`ips_report/01_version_5.md:36`). New rule:
  `caplet-latest/CLAUDE.md:26-29`, `caplet-latest/COMPETITION.md:141-143`; but `caplet-latest/START_HERE.md:26` still
  says "The team writes all deliverables". 13 drafted rewrites (`IPS_v5_suggestions.md:9-21`). IPS bans "footnotes, and
  formal citations" (`2026_WGY_Investment_Policy-FINAL.txt:123-125`). "Rewrote the exemplar IPS to remove AI-style
  patterns ... an AI-voice detector" (`docs/AI_USE.md:65`). 2025-26 semifinal answers: "authentic team voice, not
  generated or generic responses" (FROM KB:330).
- **Fix must achieve.** All six students vote on what [AI] suggestions may contain, and the rule files agree. The option
  most consistent with the judging evidence: [AI] items are facts, numbers and flags, never sentences. Students write
  a fresh IPS from a bullet outline with AI drafts closed. Every accepted AI item is logged as it happens.
- **Deadline.** Vote Sun 18 Oct, before any suggestion is accepted.

### PM-04 - Story 4: the IPS locks a rule set that protects the range better than the payments (high, known-deeper)
- **Problem.** The case says the range "must also protect the portfolio's ability to fund the ten-year operating
  commitment" (case:119-120). The team's own 16 Oct model shows the opposite order: the gift lands in the range in
  99.4% of paths, but in 6.3% of paths a later payment needs more than Laura kept. V5 still says "never below the
  floor" and "she cannot miss the range". A fixed-income reader (Aberdeen readers have sat on Top 50 panels; FROM
  KB:43-46) will see this. After 6 Nov the strategy cannot be changed (IPS-FINAL:73-74).
- **Evidence.** `caplet-latest/research/ips_numbers_2026-10/results.json:130` (`p_gift_inside_range 0.9941`), `:138`
  (`p_exceeds_what_laura_kept 0.063`); `IPS_number_sheet.md:47-48` ("'cannot miss' is not literally true"). V5 lines
  `01_version_5.md:28` ("never below the floor") and `:30` ("cannot miss"). The case asks teams to "define what they
  consider a high degree of funding certainty" (case:97-99); V5 has no definition. The team kept "never below the
  floor" because the floor was STRIPS (`final_report.md:24`); STRIPS were ruled out on 6 Oct (`CLAUDE.md` current
  status).
- **Fix must achieve.** The IPS states, in the students' words: a one-line certainty standard; which money stands
  behind the payments after 2033; that payments come before the gift; no absolute words the team's own numbers
  contradict.
- **Deadline.** Protection option chosen Tue 20 Oct (see PM-05); full rule set at vote set B, Tue 27 Oct.

### PM-05 - New sequencing trap: the number sheet's open choice changes what the TNA reflections can say (high, new)
- **Problem.** The 16 Oct sheet asks the team to "pick one" of three options "before 6 Nov". Option 2 keeps Laura's half
  in reserve to 2042; option 3 holds back $10-20k and lowers the floor. Those are exactly the jobs the IBTM reflection
  (the floor) and the VT reflection (what the stocks are for) will describe on 23 Oct. The TNA must be "consistent with
  the strategic approach your team is developing and will later articulate in its IPS" (TNA:29-31). The VT note
  cannot be edited and already says stocks "only set how far her gift rises above her promised minimum".
- **Evidence.** `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md:49-53`;
  `2026_WGY_Trading_Notes_Analysis-FINAL.txt:29-31`; VT note `ips_report/05_trading_note_reflection_wins_trading_notes.md:14`;
  IBTM note `:19` ("provides a floor for her facility contribution").
- **Fix must achieve.** Either the option is chosen before the IBTM and VT reflections are written, or the reflections
  avoid any claim the choice could change. If option 2 or 3 is chosen, the VT reflection must explain, truthfully, how
  "only" in the note relates to the final rule (the note was right for the rule at the time).
- **Deadline.** Tue 20 Oct (reflections are planned for that day in the 15 Oct brief, item 16).

### PM-06 - Story 5: the ladder room is smaller than one day's move, so point claims will go stale (high, known-deeper)
- **Problem.** See section 3. The IBTR note's "about 0.2 percentage points" was true on 6 Oct (23.0bp). On 15 Oct the
  room is 4.7bp, and one day moved it by $2,635. A reflection or IPS sentence that says the first deposit "is enough"
  or "is not enough" can flip before the judges read it. V5's "$292,000 at late-September yields" is on the old basis.
- **Evidence.** Section 3 table (re-run today); IBTR note `05_...:15`; V5 `01_version_5.md:16,24`.
- **Fix must achieve.** In all three documents: state the rule (if the ladder costs more than $300k in January, the 2028
  deposit tops it up first and the floor is lower by the same amount) and, where a figure helps, give the holdings-basis
  figure with its date. Never use $294k for Caplet's holdings. The IPS can carry no figure at all; it is "not expected"
  to (IPS-FINAL:68-70) and should avoid "detailed financial calculations" (IPS-FINAL:51-52).
- **Deadline.** TNA figure fixed on one curve date by Tue 20 Oct; IPS check Wed 4 Nov.

### PM-07 - Story 3: competent but not memorable (high, known-deeper)
- **Problem.** Wharton set a fixed-payment client in 2021-22 ("Should she keep $50,000 in cash?"). Many good teams will
  build a Treasury ladder plus stocks and quote a Monte Carlo confidence. Caplet's edge is clarity and client insight,
  but V5's pitch spends its first words on an unsourced claim about co-sponsors and a stale figure, and "diversif-"
  appears 0 times in V5 although "appropriate diversification" is a named criterion.
- **Evidence.** FROM KB:290-294 (2021-22 case); pitch `01_version_5.md:16` ("co-sponsors who fund the building rarely
  pay to run it"; "about $292,000"); my grep: 0 matches for "diversif" in `01_version_5.md`; criterion
  `deliverables.txt:55`. Judges' repeated message: "simple, elegant ideas" (FROM KB:305), "less is more" (FROM KB:304).
- **Fix must achieve.** At most three signature ideas, said the same way in the TNA, IPS and Final Report. The pitch
  starts from Laura's goal. Diversification is argued in one plain sentence (why one issuer for promises, thousands of
  companies for the rest).
- **Deadline.** IPS outline Wed 28 Oct.

### PM-08 - Root cause: advice is not turning into action, and one rule was reversed in a day (high, new)
- **Problem.** The 15 Oct brief gave dated actions. The 16 Oct commit (the only change since) did none of the
  repo-visible ones and reversed item 1. Without owners and a weekly check, the same list will still be open on 6 Nov.
- **Evidence.** In `caplet-latest` (16 Oct): "AI may fill a ticket up to Preview" still at `COMPETITION.md:194` (brief
  item 2); "Laura is a fictional client" still at `COMPETITION.md:49` (items 7, 28); Feb-2037 bond still "5.000%" at
  `COMPETITION.md:182` (item 28; the note says 4.750%, `05_...:16`); `min_share_price_usd: 3` still in
  `config/competition.yaml:44` and `config/wharton_private_2026_27.yaml:72` (item 28); roster still
  "PENDING_WHARTON_ROSTER_CONFIRMATION" (`config/team_roster.json:9`); repo still public and now forked (item 3).
  Item 1 ("students write every word") was replaced by the [AI] rule (`caplet-latest/CLAUDE.md:26`). Commit stat: only
  the number sheet, rule text and curve changed. Off-repo progress (Google Docs, meetings) is UNVERIFIED.
- **Fix must achieve.** One owner and one date per open item, checked for 15 minutes each Sunday. Team-wide rules change
  only by a recorded team vote.
- **Deadline.** Sun 18 Oct.

### PM-09 - Root cause: the key calls are not yet the students' own (high, known-deeper)
- **Problem.** Articulation scores "the team's research and decision-making process" (`deliverables.txt:58`). The
  record shows the team deferring to AI, and debates without outcomes. Weak ownership shows up as generic reasoning on
  paper and as silence at the semifinal, where every member must speak (FROM KB:211-213).
- **Evidence.** "the team deferred to the assistant's evidence-based calls" (`CLAUDE.md:75`); "AI recommendation: keep
  the $150k floor ... Team vote needed (D2/D6)" (`team/google_drive/notes_and_discussions.md:303`); the 5 Oct "copout"
  debate: "Outcome and reasons: [fill in]" (`final_report.md:23`).
- **Fix must achieve.** Each student owns one decision and one number, can explain it without AI, and can rebuild the
  number in a spreadsheet. Votes are logged with who argued what. The growth-first plan that was tested and dropped is
  told as the team's own learning, with AI's role stated.
- **Deadline.** Owners Sun 18 Oct; votes logged by Tue 27 Oct.

### PM-10 - Integrity: the journal's blanks invite invented stories (high, known-deeper)
- **Problem.** The journal has "[who argued what]", "[fill in]" and "[Keep adding ...]". Last year's team doc asked
  people to invent stories. Under deadline pressure, blanks get filled from memory or made up. Wharton's ethics rules
  bar invented teamwork stories (15 Oct brief section 2; FROM KB:468-469).
- **Evidence.** `final_report.md:16,23,25`. Last year: "Make up stories, and make them sound realistic"
  (`2025_knox_wharton.md:3827`) and "expand the story, make up some facts" (`:3852`).
- **Fix must achieve.** Every blank is filled this month from a dated record (chat, meeting notes, WInS log), or left
  out. Nothing in Articulation that the team cannot point to.
- **Deadline.** Sun 25 Oct.

### PM-11 - Integrity: the ready-made AI disclosure is already untrue (high, known-deeper)
- **Problem.** The disclosure text kept for the Final Report says students "made all decisions, and wrote all submitted
  text". The record shows AI-built models, AI decision memos, AI example notes behind the WInS notes, and now AI
  wording suggestions. A false Works Cited statement is worse than an honest, specific one.
- **Evidence.** `caplet-latest/docs/AI_USE.md:91`; AI wrote "23 EXAMPLE notes ... 17 of 23 rewritten" and "decision
  memos for the team to ratify" (`caplet-latest/docs/AI_USE.md:70-73`); deferral (`CLAUDE.md:75`). Wharton: AI use
  "must be recorded in your Works Cited pages" (FROM KB:81).
- **Fix must achieve.** The Works Cited AI entry is built from a real log, names what AI did (research, models, numbers,
  example notes, any accepted wording) and is literally true.
- **Deadline.** Log back-filled Sun 18 Oct; entry drafted by Sun 29 Nov.

### PM-12 - Story 7: hard gates (medium, known-repeat)
- **Problem.** Low chance, total loss. Each gate below has already been flagged; they are listed so none is dropped.
- **Evidence and gate list.**
  - IPS: "Submissions that do not meet the requirements below will not be considered for semifinal selection"
    (IPS-FINAL:82-83); 50/500 words, 2 pages, TNR 12, double-spaced, 1-inch margins, PDF, 5 MB (IPS-FINAL:103-122);
    title page names "First Name, Last Initial" matching the roster, plus the WInS username (IPS-FINAL:84-100). V5 is at
    47/50 and 497/500 (15 Oct brief section 3).
  - TNA: notes "exactly as it appears in WInS"; "Yes, we will verify this" (TNA-FINAL:44,53). Four notes sit on
    cancelled orders, including a second IBTR note with "0.3" (`05_...:33-40`).
  - Final Report: a page range with a "not reviewed" or "disqualified" rule is likely (FORECAST, FROM KB:387).
  - School letter on letterhead, signed by an administrator, all names (`2026_27_School_Documentation_Template.txt:1-28`);
    Knox term ends Thu 3 Dec (FROM L10).
  - Submission: only the team leader submits; deadlines fall on Saturday mornings in Sydney; US clocks change Sun 1 Nov.
- **Fix must achieve.** A two-person checklist for each submission, done a day early.
- **Deadline.** TNA Thu 22 Oct; IPS Thu 5 Nov; letter in hand Fri 20 Nov; Final Report Fri 4 Dec (Sydney).

### PM-13 - Integrity: Laura is real, but the team's "single source of truth" says she is fictional (medium, known-repeat)
- **Problem.** Contacting the client means disqualification. A team file that calls her "fictional" lowers the guard.
- **Evidence.** "Laura is a fictional client" (`caplet-latest/COMPETITION.md:49`). Wharton: "While the client is real,
  the financial scenario is developed specifically for the competition" (main page, `L12_main.txt:374`, VERIFIED).
- **Fix must achieve.** The line is corrected and all six students know: no message, tag, follow or comment.
- **Deadline.** Sun 18 Oct.

### PM-14 - Exposure: the repo is not search-indexed today, so the real risk is similarity with another team (medium, new)
- **Problem.** I searched Bing (RSS endpoint) for "caplet-investment", "Root-and-Branch" with Laura Gao Wharton, and
  "Laura Gao Wharton investment competition github". No result pointed to the repo or the fork on 16 Oct. So a judge
  finding it by chance is unlikely now. The live risk is another team reading the public strategy and AI text and
  submitting something similar; that can pull both teams into a plagiarism question. Public forks stay public if the
  parent goes private (FROM L09).
- **Evidence.** My searches on 16 Oct 2026 (results: unrelated pages only). Fork created 15 Oct (task brief). Plagiarism
  is "grounds for dismissal" (15 Oct brief section 2).
- **Fix must achieve.** The team decides, on the record, whether the strategy and drafts stay public until 4 Dec, and
  asks the fork's owner to delete or privatise the fork if not.
- **Deadline.** Sun 18 Oct.

### PM-15 - "Too timid for an entrepreneur" and "one issuer" will be asked, and V5 does not answer them (medium, known-deeper)
- **Problem.** Laura is an entrepreneur; the plan holds about 7-9% in stocks and about 91% in one issuer's debt. That is
  defensible, but only if the IPS says why in client terms. [AI] suggestion 8 would cut V5's only sentence on
  one-issuer risk.
- **Evidence.** V5 risk sentence `01_version_5.md:24` ("Relying on one issuer ... we accept it"); suggestion 8 "(cut)"
  (`IPS_v5_suggestions.md:16`); stock share about 7.2% on the 15 Oct basis (FROM L08); criterion "appropriate
  diversification" (`deliverables.txt:55`).
- **Fix must achieve.** One plain reason for the stock share (money nobody relies on carries the stock risk; promised
  money does not), and one for the issuer choice. Keep both through every edit.
- **Deadline.** IPS outline Wed 28 Oct.

### PM-16 - The TNA is not where the Top 50 is won; time-box it (medium, known-deeper)
- **Problem.** Wharton's rules page names the IPS and Final Report for the Top 50 (FROM KB:68); SMApply says the TNA is
  evaluated too (`deliverables.txt:27`). The TNA's weight is unknown. The team has spent heavy effort on notes (15
  notes, AI example notes, three AI judge panels). Polishing three 100-word reflections past "solid" costs IPS time.
- **Evidence.** `deliverables.txt:27`; FROM KB:68,170-172; AI note work in `caplet-latest/docs/AI_USE.md:70-73`.
- **Fix must achieve.** TNA done to a clear standard by Thu 22 Oct, then all effort moves to the IPS rule set.
- **Deadline.** Thu 22 Oct.

### PM-17 - Commit 412e9e3 changes the ranking, not the story (medium, new)
- **Problem.** The commit adds useful numbers but moves two risks up: voice (story 2) and inconsistency (story 5). It
  also opens a strategy choice (PM-05) with a deadline later than the TNA that depends on it.
- **Evidence.** `caplet-latest/CLAUDE.md:26-29`; `IPS_number_sheet.md:5,13,49-53`; section 3 above.
- **Fix must achieve.** Treat the sheet's numbers as MODEL inputs for students to check, re-based on the holdings, and
  decide the open option before the TNA.
- **Deadline.** Tue 20 Oct.

---

## 5. Reverse pre-mortem: it is the finale, and Caplet won

What three things most plausibly made the difference (AI ESTIMATE, built on what judges said they reward).

1. **One rulebook a 15-year-old can repeat, written by the students, the same in all three documents.** Wharton:
   "Your strategy is a set of rules and guidelines; a plan of attack" (FROM KB:316). Judges: "simple, elegant ideas"
   and "less is more" (FROM KB:304-305). Consistency with the IPS is scored (`deliverables.txt:55`). Caplet's natural
   version: each deposit has one job; Laura only promises what is already bought; payments come first, and the
   certainty standard says how sure, in one line. The winning IPS has no absolute words and no number the team cannot
   rebuild.
2. **The most honest uncertainty message in the field.** This year Creativity scores communicating "investment
   uncertainty clearly and credibly to prospective co-sponsors" (`deliverables.txt:59`), and the case warns that
   overpromising damages credibility (case:114-116). A range whose bottom is already owned, a stated confidence, and
   the chance of reaching the top (the informative number) is rare and fits the client. The team's sourced evidence on
   how funders read commitments is an edge most teams lack (FROM L01, L04).
3. **Six students who could each defend a number live, and a true story of change.** A 2025 Aberdeen finale judge: what
   distinguished managers was "clear thoughtfulness and reasoning behind all the decisions" (FROM KB:307). Finales have
   about five minutes of questions (FROM KB:226-229); semifinals required every member to speak (FROM KB:211-213). The
   real story is strong: growth-first tested and dropped; the 6 Oct WInS-only email forced a redesign from STRIPS to
   iBonds; the sector-minimum myth traced to the primary source; 12:30 a.m. Sydney trading; the 7 Oct mis-click and the
   new rule it produced (`final_report.md:16-27`). Told honestly, including what AI did, it scores Articulation.

---

## 6. Stop doing (effort that does not move the score)

| Stop or cap | Why it does not move the score | Evidence |
|---|---|---|
| New AI research waves and long AI reports | Strategy is already the strongest criterion; ~700k words already exist that judges never read | word counts (PM-01) |
| Tracking WInS value, profit or ranking | "You are not being evaluated based on ... Your portfolio ranking ... Whether your portfolio makes money" | Guide:74-78 |
| Trading to show activity, or re-running the October trade rule repeatedly | "How many trades you make" is not evaluated; plan is hold. One logged check per rule is enough | Guide:76; 15 Oct brief item 8 |
| AI mock-judge scores as targets | Wharton publishes no weights and gives no feedback; four judge routines score drafts | faqs.txt:78; `ops/routines/scheduled_tasks/caplet-judge-*.md` |
| "Humanising" AI drafts or testing against AI detectors | Rewording AI text does not make it the students' work; detector tuning is an integrity risk | `ips_report/README.md:11`; `docs/AI_USE.md:65` |
| More decimals in the Monte Carlo (200,000 paths, 99.4%) | The IPS is "not expected" to include a range or projections; the range's confidence is near-certain by design | IPS-FINAL:68-70; `results.json:130` |
| Building more PDFs and briefs (27-page brief, 831-page record) | Judges read only the three deliverables | `CLAUDE.md` insight_v1 section |
| Debating names and metaphors | Six strategy names already in files; one plain name is enough | FROM L08 (COH-09) |
| Using last year's "Final Report AI Judge" rubric | It lists "four formal assessment categories"; Wharton has five | `2025_knox_wharton.md:3149` |
| Polishing the TNA past a clear standard | The Top 50 is named on the IPS and Final Report | PM-16 |

---

## 7. Checklist by date (Sydney)

| Date | What | Story it prevents |
|---|---|---|
| Sun 18 Oct | Team vote on the [AI] rule scope; owners for every open item; fix "fictional"; decide repo/fork; back-fill the AI log | 2, 8, root causes |
| Tue 20 Oct | Pick the number sheet's protection option; fix one curve date and the holdings-basis figure for the TNA | 4, 5 |
| Thu 22 Oct | Submit the TNA after a two-person check (notes on filled orders only) | 7 |
| Sun 25 Oct | Journal blanks filled from dated records | 1, 8 |
| Tue 27 Oct | Vote set B: certainty standard, post-2033 back-up, floor, waiting cash, no absolute words | 4 |
| Wed 28 Oct | Student bullet outline with three signature ideas | 2, 3 |
| Wed 4 Nov | Format check, two word counters, title page from the roster | 7 |
| Thu 5 Nov | Submit the IPS a day early | 7 |
| Sun 8 Nov | Final Report pre-build ready | 1 |
| Fri 20 Nov | School letter in hand | 7 |
| Sun 29 Nov | Full Final Report draft; AI entry from the real log | 1, 8 |
| Fri 4 Dec | Submit (Sydney), a day early | 7 |

---

## 8. Verification log (16 Oct 2026)

- Wharton main page fetched with `oct16/tools/page.py`; saved text `oct16/lenses/L12_main.txt`; raw HTML counter
  `data-counter-value="2339"`. Lines 374 (client is real), 380 (not portfolio performance), 382 (panel of judges, 50
  semifinalists, virtual Semifinals).
- Ladder costs re-run with `oct16/research/KB_verify/num/reconcile.py` on
  `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv` for 6, 9, 13, 14 and 15 Oct.
- Number sheet method read at `caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:70-89,115-126`; results at
  `results.json:35,130,138`.
- Last year's comment dates counted from `team/google_drive/2025_knox_wharton.md` (63 dated comments; 26 on 11 Dec, 4
  on 12 Dec 2025).
- Bing RSS searches (3 queries) returned no repo or fork result.
- Word counts: `find <dir> -name '*.md' -o -name '*.txt' | xargs cat | wc -w`.
- Not re-opened by me (FROM KB / FROM Lxx): past Top 50 counts and judges' quotes, Knox term dates, fork behaviour,
  the 44-45% over-$300k estimate, stock share 7.2%.
