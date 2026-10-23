# Team Caplet: overnight review of the whole repo

Claude Code, Wed 30 Sep 2026 (written overnight, Sydney). This is review and research for the team, not submission
text. Nothing was traded, sent, or typed into WInS, the IPS Doc or the Sheet.

---

## 1. The short version

**The strategy is good, and the maths holds up.** I rebuilt the core numbers from scratch using the official
treasury.gov data and got the same answers as the RAB kit: the ten payments cost **$289,119** on the 28 Sep curve
(the kit's figure, to the dollar), every bond price check matched to 0.1bp, the 2020 "about $460,000" claim holds,
and the floor trade-off comes out the same. Root-and-Branch answers every requirement in the case with a rule instead
of a forecast, and it suits a world where safe bonds pay about 5%.

**The risks that matter now are not the numbers.** In order of how much damage they could do:

1. **Authorship.** The "adopted IPS" in the Google Doc is an AI-written exemplar, and the RAB kit is set up to *edit
   it* sentence by sentence against a word budget. The AI-use log also records it being rewritten to score lower on
   an AI-voice detector. Submitting an edited version of that text is the one thing that could get the team
   dismissed (Wharton: "Plagiarism and any kind of academic cheating are grounds for dismissal"). Separately, the
   ready-made disclosure paragraph in `caplet/docs/AI_USE.md` is false and must never be used.
2. **The repo is public.** It holds the full strategy, 23 example notes, the IPS exemplar's text, a student's school
   email (inside a file path), and, in git history, the WInS username and all six names. It names the school. A
   rival team could copy the kit, and two similar submissions hurt both teams.
3. **Complexity.** About 45,000 lines of Python and 700,000 words of Markdown now sit behind three 300-character
   notes, three 100-word reflections and a 550-word IPS. Last year's lesson was "over-complex". The judges see only
   what you write and can explain in your own words.
4. **Friday.** The Week-One email is unread (it may set a trading-activity rule), the order screen is unseen (limit
   orders? bond units?), only one laptop can run the refresh script, and the plan has people trading at 12:30 am.

**Do these, in this order:**

| When | What | Who |
|---|---|---|
| Thu 1 Oct, before the meeting | One read-only WInS login: read the Week-One email and the Trading Details page (any activity rule), open an order screen (which order types exist, how bond quantity is entered), copy the 43-bond drop-down | 1 student |
| Thu meeting | Adopt Root-and-Branch as a team and minute it; vote the book (I agree with the kit: Portfolio tab); keep the swap rule simple; choose note writers; assign Friday roles including a backup for Ray | Everyone |
| Thu | Decide whether to make the repo private (my advice: yes, now); set a strong WInS password; set the IPS Doc and Sheet to Restricted | Ray |
| Fri 2 Oct (Sat 12:30 am Sydney), or earlier with limit orders | Place the trades from the refreshed tickets; each note is its writer's own words | Friday roles |
| By Fri 9 Oct (Sat 10 Oct 8:00 am Sydney) | Roster (full names, emails, birthdays, grad years, team name, school details). Ask the school for the documentation letter now | Ray + advisor |
| By 6 Nov | Write the IPS from a blank page, together. Use the content checklist, not the exemplar's sentences | Everyone |

---

## 2. What is in the repo now

The repo grew in four waves. Only the last one is current.

| Wave | Dates | Where | Status |
|---|---|---|---|
| wharton-ic "investment operating system" | 19 Sep | `toolkit/src/wharton_ic/`, `toolkit/tests/`, `toolkit/docs/`, `toolkit/config/`, `toolkit/prompts/`, `README.md` | **Obsolete.** A stock-picking demo for a made-up client. Contains invented rules and fake data (section 10). Nothing current uses it |
| "Lock, then grow" session | 25 Sep | `MISSION.md`, `caplet/decisions/`, `caplet/deliverables/`, `archive/model/laura/`, `redteam/`, `Laura_Gao_Strategy_Brief.pdf` | **Superseded.** Useful history; `caplet/decisions/LOG.md` still says "Read this file first" and gives the old plan (80/20 growth sleeve, stock picks) |
| Council + insight_v1 | 27-28 Sep | `keel/library/council_2026-09-27/`, `keel/library/insight_v1/` | **Partly superseded.** The design survives as Root-and-Branch; its WInS book (IEF + TLH) was dropped |
| RAB kit (Root-and-Branch) | 29-30 Sep | `RUN_PLAN.md`, `archive/rab/` | **Current.** Friday tickets, example notes, decision memos, models, gates |

`CLAUDE.md` (the project memory) stopped on 28 Sep and never mentions RAB. It needs a refresh (section 13).

The RAB kit's own "what exists at 7am" list is incomplete: `rab/BRIEF.md` (the one-page summary for the team) and
`rab/POSTMORTEM.md` were never written, and the committed working paper `archive/rab/paper/RAB_working_paper.pdf` is
**truncated** (no end-of-file marker; it will not open). Rebuild it with `archive/rab/paper/build.sh` on Ray's Mac if anyone
needs it. This report can stand in for the missing BRIEF.

---

## 3. The plan in plain English

1. **Roots.** Laura's first $300,000 (January 2027) buys ten dated Treasury holdings, one ending just before each
   $50,000 payment (2033-2042). In WInS these are iShares iBonds funds IBTM-IBTR for 2033-2037 and five individual
   Treasury bonds for 2038-2042, because WInS lists no Treasury maturing between Feb 2031 and Feb 2036.
2. If yields fall before January and the ten cost more than $300,000, the second deposit finishes the job first.
3. **Floor.** The 2028 deposit buys Treasuries that pay back roughly what is left of it (about $150,000) in late 2032.
   That is the least Laura will give the facility.
4. **Branch.** What is left (about $41,000) goes into one world stock fund (VT) and is held to 2033.
5. **2031.** Laura tells co-sponsors a range: from the floor (quoted rounded down, about $145,000) to the floor plus
   half the fund's value then (about $175,000 today's projection).
6. **2033.** She gives the floor plus half the fund's value then, capped at the top she announced, so the gift cannot
   land outside the range. The other half stays with her as a cushion. The ten holdings become the operating reserve
   and simply run off, one per year.

The WInS "Portfolio tab" book is that plan on 2 January 2028 scaled to $300,000: about 66% dated ladder, 24% floor
(inside IBTM), 8.7% VT, 1% cash.

The team's own notes from 27 Sep (`keel/library/council_2026-09-27/team_notes_2026-09-27.md`) already had the heart of
this: "a liability-matching problem with a growth portfolio attached", dedication, a floor for 2031 moved into bonds
maturing before 2033, and a seed-money study. That matters for authorship: the core idea started with you.

---

## 4. Numbers I checked independently

I wrote a new pricer from scratch (no repo code), bootstrapping discount factors from the official treasury.gov par
curves (fetched today). Scripts are in my scratchpad; the table shows the results.

| Claim in the repo | My result | Verdict |
|---|---|---|
| Ten payments cost $289,119.20 today, 28 Sep curve (15-Nov STRIPS basis) | $289,119 | Exact |
| $292,418 forward to 1 Jan 2027; room $7,582; break-even fall 26.2bp | $292,327; $7,673; 26.5bp | Same to within $91 (forward convention) |
| 29 Sep break-even 28.9bp | 29.2bp (cost $291,563 on 1 Jan 2027) | Matches |
| 25 Sep: $294,387, 19bp | $294,335, 19.5bp | Matches |
| "Cost under $300,000 at September yields" | On **22 Sep it did not fit** ($300,485). It fits only after yields jumped 30bp in a week | True today, fragile: date the claim (the kit says so too) |
| Bond price checks vs curve: -15.3, -14.4, -6.6, -5.1, -1.9bp; stale bonds -92, -111bp | Identical to 0.1bp | Exact |
| Bond rungs deliver 84-90% of their $50,000 from set coupons and principal | 86% at 0% reinvestment; 91% at 2%; 99% at 5% | Matches. The Nov-2039/40/41 rungs are about $1,000-2,000 short each even at 5% |
| "About $460,000 at 2020 yields" | 2020 median $460,495 | Matches |
| $300,000 alone covered the ladder on "about 1 day in 9-10 since 2000" | About 9% of days (2000-2002, some of 2006-07, 6 days in 2026) | Matches |
| Total facility + flexibility money p5/p50/p95 $181k/$207k/$252k | $182k/$207k/$251k (my own simple model) | Matches |
| Each $25,000 less floor: +$2-3k typical, -$9-10k in a 1-in-20 bad case | +$2,400 typical, -$9,500 bad case | Matches |
| 2031 top about $175,000 (90% range $165k-$191k); gift at or near the top about 3 times in 4 | By hand: $175k; $166k-$190k; about 72% exactly at the top | Matches |
| IPS fits the format | 50 + 500 words in Times 12, double-spaced, 1-inch margins: 41 of 46 available lines on US Letter (43 of 50 on A4) | Fits, about 5 lines spare. Don't add blank lines between paragraphs |

**What this means.** The numbers are not the weak point. Three things remain genuinely uncertain, and all three are
already in the kit: January 2027 yields (about a 1-in-3 chance the ladder costs more than $300,000 then), coupon
reinvestment (the one remaining dependency of the "certain" payments), and stock returns (which only move the top of
the range).

---

## 5. Thursday's vote and Friday's trades

### Before the meeting (read-only login)

The kit moved this to Thursday, which is right. Add two things to the list:

- **Order types and durations.** If WInS offers limit orders that can be placed while the market is closed, the team
  can place every order on Friday evening Sydney time at the ticket's max price (day orders) and go to bed, instead of
  trading from 12:30 to 1:30 am. Fills then happen during the U.S. session. An order that doesn't fill simply goes
  in on Monday. Tired people make unit and ticker mistakes; this removes the late session.
- **The activity rule.** The live FAQ (I fetched it today) says teams "must meet the required trading activity and
  portfolio management guidelines throughout the competition" and never defines them. If the Week-One email sets a
  minimum, the plan of about 11 trades in week 1 plus one rule-based October check probably meets it, but read it
  before the vote.

### The three votes

- **Book.** I agree with the kit: the **Portfolio tab**. It shows all three parts of the plan (payments, floor, stock
  fund), it matches the IPS sentence about the scaled-down allocation, and a WInS book with no stocks at all invites
  "this is just bonds".
- **Swap rule.** Keep it simple: if a low-coupon alternate is listed and passes its price check on Friday, buy it;
  otherwise buy the planned bond and move on. I would drop the sell-and-rebuy October trigger D. Its benefit is small
  (one rung) and the refined note does not need it (see section 9).
- **Roles.** Name a backup for every role. Only Ray's Mac runs `refresh_tickets.py` (it is hard-coded to
  `/Users/ray/...`). If it can't run, trade from `archive/rab/trades/tickets.md` (28 Sep basis) using the stop rules: never
  above the max price, and stop if the Preview total is outside the band.

### VT on Friday instead of Monday night

The kit puts VT in a separate session on Mon 5 Oct ET (**Tue 6 Oct, 1:30 am Sydney**) so Order History shows bonds
before stocks. The kit's own worst case (every price at its max) still leaves about $2,445 of cash with VT included,
and its red team marked the "order" reason as presentation only. If the team would rather not do a second late-night
session, placing VT as the last Friday order is safe. Team's choice.

### Things only the trader can learn on Friday

Bond quantity unit (face $ or $1,000 lots): the Preview total tells you; a 10x or 1,000x gap means the unit is wrong.
IBTN in WInS is INSCORP Inc, never a buy. Two bonds had stale WInS prices on 29 Sep. Never re-enter a pending order.
Never sell anything on the day it was bought. The note box silently cuts at 300 characters: copy each note back from
Order History and compare.

---

## 6. Authorship and the Wharton AI policy

This is the part I would fix first, because the cost of getting it wrong is disqualification, not a lower score.

**What the rules say** (quoted in `keel/library/insight_v1/phase_A/wins_week1_guardrails.md`, from the Wharton Rules &
Roles and AI Policy pages): teams may use AI "for brainstorming and idea generation"; "AI-generated work may not be
submitted as your own"; "If you use AI to assist you in any way during the competition, how you use it must be
recorded in your Works Cited pages"; "When students express themselves ... they must use their voice and words."
The evaluation criteria reward "an authentic team voice".

**What the repo shows:**

1. **The IPS.** The Google Doc "IPS Report" is headed "EXEMPLAR ONLY. NOT FOR SUBMISSION." The AI-use log records
   Claude writing it (versions 3 to 12+), then "rewrit[ing] the exemplar IPS to remove AI-style patterns", testing
   it with "an AI-voice detector" and "blind voice tests" (still "~60% likely AI"). The RAB run then called this doc
   "the adopted IPS", quotes its sentences in the example notes, and built an "IPS edit ledger" that plans the 6 Nov
   IPS as a list of word-level edits to it within a 17-word budget. Followed literally, that ledger produces an
   AI-written IPS with student edits.
2. **The notes.** 23 AI example notes exist for Friday. The kit handles this better: writers draft from the brief
   with the example closed, and `note_check.py` flags heavy overlap. Keep that discipline.
3. **The disclosure template.** `caplet/docs/AI_USE.md` sections 1-4 describe the retired wharton-ic system and give a
   ready-to-paste Final Report statement that says the AI "check[ed] fact citations against SEC filings" (the code
   never did) and that everything was "conceived, debated, and authored 100% by student team members". That is not
   what happened. `toolkit/outputs/ai_use_log.jsonl` has 242 entries and every one is a fake demo record (`is_mock: true`).
   Put a warning at the top of `caplet/docs/AI_USE.md` (or delete sections 1-4); the real record is its section 5-6 table.

**What I would do:**

- **Write the IPS from a blank page as a team.** Use the lists of what the IPS must cover (the case, the IPS
  instructions, `keel/library/insight_v1/ips_spec.md`, the "what each edit must achieve" column of
  `archive/rab/decisions/D_ips_edit_ledger.md`), but not the exemplar's sentences. Close the exemplar while drafting. Keep
  the Google Docs version history; it shows who wrote what.
- **Same for the notes and reflections.** Each writer drafts from the facts. If a writer has read an example, say so
  in the AI log.
- **Disclose honestly and specifically in the Final Report.** Something like: which tools (Claude Code, ChatGPT),
  what for (brainstorming, building and checking models, red-teaming, example wording the team did not submit), and
  what the students did (decisions, all submitted writing, checking the numbers). The Wharton checklist question
  "Did I understand the key learnings and how to arrive at the answers without the assistance of generative AI
  tools?" is the one to be able to answer yes to.
- **Own the key numbers.** Rebuild five of them in your own Sheet (section 11 lists them). Then the Final Report's
  numbers are yours, with the AI models cited as a cross-check, and the semifinal Q&A (all six must present) gets
  much easier.

---

## 7. Public repo and privacy

Facts (from a full scan of every branch and all history):

- **High.** A student's school email address is embedded in a hard-coded Google Drive path in
  `archive/rab/rescued/r4_hist_original.py` line 6 (current files, all pushed branches). Deleting that one line fixes the
  current files; it stays in history until the history is rewritten or the repo is made private.
- **High.** The WInS username (and all six names as "First name, last initial") is still in git history in an old
  version of `archive/rab/trades/data/ips_doc_text_2026-09-30.txt`. It was redacted on 30 Sep, but the kit's own rule "never
  push a archive/rab/* branch" was then broken: every rab branch was pushed, the kit was merged into `main`, and the
  interrupted stash was pushed as its own branch (`wip/ws7-stash-2026-09-30`). The WInS username cannot be changed, so the password is the only protection.
- **Medium.** The school is named in `MISSION.md`, `caplet/docs/research_laura_gao_and_wins.md`,
  `Laura_Gao_Strategy_Brief.pdf`, Drive folder names in several files, and the GitHub repo description. With the six
  first names, that identifies minors at a named school.
- **Medium.** The IPS Doc and team Sheet IDs are in 15 files. Harmless if both are set to Restricted; public if either
  is shared as "anyone with the link".
- **Low.** An old research file in history holds the client's (Laura Gao's, a real person) résumé phone number and
  email, and 7 quotes the research run itself tagged EXCLUDE-PRIVACY (family, health, home life) are still in
  `keel/library/insight_v1/phase_D/`. `aussef_complete_experiment_record.pdf` at the repo root is an unrelated personal
  research project.
- **Competitive.** Everything the team plans to do, and the example wording, is readable by any team that searches
  "Laura Gao Wharton".

My advice: **make the repo private now** (Settings, General, Danger Zone, Change visibility). It is reversible,
takes one minute, and stops further exposure. After that, a history rewrite is optional. Also: a strong WInS
password that is never sent by message; set the IPS Doc and Sheet to Restricted; remove the school name from the repo
description; delete the AUSSEF PDF and the EXCLUDE-PRIVACY quotes.

---

## 8. Devil's advocate: what a tough judge will ask

| Question | Answer that holds up |
|---|---|
| "91% Treasuries? Laura is willing to take thoughtful risks." | Her payments are fixed dollars, so dollar bonds are the natural match; they use about $290k of her first $300k at today's yields. The only free money is the 2028 deposit. Moving $25,000 of the floor into stocks would add about $2,400 to her typical outcome and cost about $9,500 in a 1-in-20 bad market. With safe bonds near 5%, the reward for stock risk is small. |
| "Your own model says All-Treasury gives the facility more at every percentile. Why hold stocks at all?" | The kit says this openly (`archive/rab/decisions/D_rivals.md`). The comparison gives All-Treasury's whole pot to the facility while Root-and-Branch keeps half the fund for Laura. The fund is her flexibility money: it has the longest horizon, it is the only part that can keep up with facility-cost inflation, and it is the "balance" she asked for. Have this answer ready; it is the sharpest question on the table. |
| "The payments depend 'essentially on the US government'? What about reinvesting coupons?" | Fix the wording (the kit flags it): the government owes most of each payment; the rest depends on reinvesting coupons at roughly today's yields. At 2% for years the ten holdings deliver about $466,000 of $500,000. The kit proposes Laura's kept half as the first cover (team decision by 26 Oct). |
| "100% confidence in the range sounds like a trick." | It is by design: the bottom is bonds she already owns, the top is a cap she sets. Say it that way, then say where the gift will probably land (at or near the top about 3 times in 4). |
| "What if her 2028 deposit doesn't come?" | This is a strength. Her income is lumpy (advances, speaking, licensing). At today's yields the payments are funded by the 2027 deposit alone, so the promises don't depend on her next book. A growth-first plan missed a payment in about 4 paths in 10 without the deposit (`keel/library/verified_2026-09-27/strategy_mc.py`). |
| "The residency is in Taiwan." | The facility gift is in dollars and the costs are in Taiwan dollars. Say so in the Final Report and name who bears it (Laura's kept half). |
| "Inflation?" | The payments are fixed by the case. At about 2.3% inflation the 2042 payment buys what about $35,000 buys in 2027; in a 1970s-style decade, about $18,000. The kept half and the stock fund carry the inflation risk, not the promises. |

**One gap worth adding.** The co-sponsor section can lean on the research your own 27 Sep notes found: a visible lead
gift raises what others give (List and Lucking-Reiley 2002: raising seed money from 10% to 67% of the goal raised
giving about sixfold; Andreoni 1998 and Vesterlund 2003 on lead gifts as a signal of quality). That is exactly the
case's line about a "meaningful personal contribution" signalling viability, and it explains why a credible floor
matters more than a bigger but shaky number. I checked all three in Crossref (DOIs in the appendix). None is in the
RAB literature list.

---

## 9. The three deliverables

### Trading Notes Analysis (due Fri 23 Oct = Sat 24 Oct 8:00 am Sydney)

The kit's picks are IBTR (tested), a low-coupon bond swap if one happens (refined), and VT (supported). Two changes
I would consider:

- **A stronger "refined" story already exists.** Until 28 Sep the plan used bond ETFs (IEF and TLH) matched to the
  payments' duration. Then the plan changed after a check found most of TLH's bonds mature after Laura's last
  payment in 2042 (74.7% by weight, from the iShares holdings snapshot in
  `keel/library/insight_v1/securities_and_allocation.md:81`), and a bond fund never matures, so it cannot end when a payment is due. The strategy changed from duration matching to
  one dated holding per payment. That is a real change of strategy with a clear reason, a judge gets it in one
  sentence, and it ties to the IPS line contrasting cash-flow matching with immunization. It needs no luck with WInS
  listings. If you want it, decide on Thursday which holding's note carries it (a bond rung such as the Nov 2041 bond
  works), because notes are typed on Friday and cannot be edited.
- **Make "tested" vivid.** The kit's test ("do the ten payments still cost less than $300,000 at the latest yields?")
  had about a 1% chance of failing on Friday (the kit's own red team, `archive/rab/redteam/triage.md` D8). What actually tested the plan is that on 22 Sep the ladder did not fit
  and a week later it fit with about $8,000 to spare. That swing is why the IPS needs its rule for a gap, and the
  14 Oct re-check reports it again.

Also: Wharton's own example note is 413 characters, plain, and uses words like "stability". Your notes are capped at
300. Keep them simple; the kit's banned-word list is stricter than Wharton needs.

### IPS (due Fri 6 Nov = Sat 7 Nov 9:00 am Sydney; trading freezes one hour earlier)

- Write it yourselves (section 6). The content decisions the kit lists are the right ones: define "high degree of
  certainty" honestly (bonds owed by the government plus a named cover for reinvestment), say who pays costs, quote
  the floor rounded down, date the "under $300,000" claim, soften "cannot fall outside it" or keep it with its
  conditions.
- Keep calculations out; one or two figures at most. No charts, citations, footnotes or links.
- Page fit is fine (section 4). Title page: official team name, names as "First name, Last initial" exactly as on the
  roster, and the WInS username.

### Final Report (instructions 9 Nov; due Fri 4 Dec = Sat 5 Dec 9:00 am Sydney, with the school documentation)

Ready in the repo: reserve size and composition, the certainty evidence, the floor trade-off, stress tests with real
values, the 2031 range and where the gift lands, rivals, the bad-year rules. Still missing: the co-sponsor fundraising
text (students write it), the seed-money argument, currency, the experience section (keep a short team journal from
now: who did what, what you learned, what went wrong), and honest AI disclosure. Ask the school for its
documentation letter now; the FAQ says not to leave it late.

---

## 10. Housekeeping and code

- **Tests:** 73 pass (59 in `toolkit/tests/`, 14 in `archive/model/tests`) on Python 3.12. The README says 58 and 47, and "Python
  3.11+", but `toolkit/src/wharton_ic/strategy/memory.py:85` does not parse on 3.11. Every pytest run appends fake entries to
  the tracked `toolkit/outputs/ai_use_log.jsonl`.
- **`toolkit/src/wharton_ic` should be archived.** Nothing current imports it. It returns made-up company financials seeded
  from the ticker's letters and labelled FY2025 (`data/yfinance_provider.py:132-164`), enforces an invented "Wharton
  approved" 31-security list that rejects IEF, TLT, VT and IBTM (`universe/engine.py:82-85`), and uses invented rules
  (25% sector cap, 15% asset limit, $100,000 starting cash, a 9% hurdle). `report audit-ai`, `rules conflicts` and
  the evidence audit cannot fail. Several documented commands do not exist. Its charts and "AUDITED ... Client: Laura
  Gao" report pack could mislead anyone who runs it.
- **`keel/library/verified_2026-09-27/strategy_mc.py`** anchors the 2033 reserve cost on a flat 5.26%, which overstates
  it by about $6,400 and slightly penalises the growth-first rival (miss rate 3.2% becomes 2.8% when re-anchored).
  The lock-early conclusion is unchanged. `archive/model/laura` checks out by hand.
- **Stale files a teammate could trip on:** `caplet/decisions/LOG.md` ("Read this file first", old plan),
  `caplet/decisions/04_growth_sleeve.md` ("DECIDED 80%" equity), `Laura_Gao_Strategy_Brief.pdf` at the root (old plan),
  `toolkit/config/competition.yaml` and `toolkit/config/wharton_private_2026_27.yaml` (still "awaiting official material", all
  rules null), `toolkit/config/wharton_public_2026_27.yaml:28` (still lists "sector minimum equal to team size" as open; the
  official rules have no sector minimum), insight_v1's IEF + TLH book. Duplicate copies of the official PDFs sit in
  `competition toolkit/docs/` and `toolkit/literature/`.
- **Stale branches:** `claude/zealous-turing-l19aqc` (pre-insight_v1), `wip/ws7-stash-2026-09-30` (edits the kit
  says never to apply), and the `rab/ws*` branches, all pushed.

- **Reproducibility.** On a clean Linux machine the pinned environment installs exactly, and `make -C rab all
  PY=<python>` rebuilds the Friday tickets byte for byte ($294,764.50 Portfolio, $292,580.89 Book L) with the
  `numbers.yaml` hash unchanged. But `make -C rab checks` fails anywhere except Ray's Mac: Gate C opens
  `/Users/ray/Research/rab-kit/rab/numbers.yaml` (`archive/rab/trades/check_gate_c.py:163`), so it crashes and its self-test
  reports a false FAIL, and Gate B for WS2 needs gitignored files that only `make all` creates. "Only run stamps
  change on a rebuild" is not quite true off the Mac: float noise, re-drawn figures, and the Bayesian blind refit move
  some blind-check values by up to a few hundred dollars. No ticket or decision value moves.

**Stale files that could cause a wrong trade, a rule breach, or a wrong deliverable** (from a sweep of the whole
repo; the full list has 24 rows):

| File | Says | Actually |
|---|---|---|
| `caplet/deliverables/ips_outline.md:17` | "Show chart 02" in the IPS | Charts are banned in the IPS, and a breach means no semifinal |
| `toolkit/docs/wharton_workflow_v2.md`, `toolkit/docs/wharton_rule_system.md`, `decisions/07` | Trading Notes due 4 Dec; trading closes 4 Dec | TN Analysis 23 Oct; trading ends 6 Nov |
| `keel/library/insight_v1/securities_and_allocation.md`, `trading_notes_pack.md`, `E6_final_spec.md`, the 27-page Strategy Brief PDF, `keel/library/blueprints/01_trading_notes_blueprint.md` | The IEF + TLH (or IEF + TLT) WInS book, VTI/VXUS, sector funds | Dated ladder + IBTM + VT (`archive/rab/trades/tickets.md`) |
| `caplet/deliverables/trading_notes_plan.md`, `decisions/04`, `decisions/07` | "DECIDED" 80/20 sleeve, 8-12 stock picks, 10-14 stocks across 8 sectors | No individual stocks; growth money is VT only |
| `keel/library/council_2026-09-27/team_notes_2026-09-27.md:48`, `01_chair_memo.md` | "at least 6 unique sectors" | There is no sector minimum. Check the team's live Google Doc too |
| `competition/official/README.md`, the `competition toolkit/docs/` folder (last season's approved ETF list) | "All trading must be drawn from this authorized list" | There is no approved list this year |
| `toolkit/docs/architecture.md:75`, `toolkit/docs/methodology.md:96`, `toolkit/config/portfolio.yaml` | "Official Wharton rules": 10-20 stocks, 15% max weight, 25% sector cap | Invented. IBTM at 32.5% of the book is allowed (Session Rules: 200% per ETF) |
| `keel/library/insight_v1/trading_notes_pack.md:48` | Test the note box by typing about 450 characters | The limit (300) is already known; skip it, a slip on the order screen could place an order |
| `caplet/docs/research_laura_gao_and_wins.md:73` | "IBTO 2033 ... first four payments" | IBTM pays 2033 ... IBTR pays 2037 |
| `caplet/decisions/02_high_certainty_definition.md:39`, `decisions/08` | Coupon reinvestment is "small"; payments "funded by the first cheque alone" | Reinvestment is the weakest assumption; about a 1-in-3 chance the 2028 deposit is needed |

**Safe reading order for a teammate:** the official case and instructions (`competition/official/2026_27/*.txt`),
then `RUN_PLAN.md` section 0, `archive/rab/STATUS.md` sections 3-4, `archive/rab/decisions/D7_wins_book.md`,
`archive/rab/trades/friday_checklist.md`, `archive/rab/trades/tickets.md`, `archive/rab/trades/notes.md` (briefs, not the example wording),
`archive/rab/decisions/D_certainty_definition.md` and `D6_cap_share.md`. Everything else is history.

---

## 11. What this teaches (for the team's own understanding)

1. **A ladder turns bills into a shopping list.** If you owe $50,000 every January, buy something that pays out just
   before each January. That is cash-flow matching (dedication).
2. **Coupons have to be reinvested.** A coupon bond pays you along the way, so what it is worth at the end depends
   on what those coupons earn. A zero-coupon bond has no such risk; a low-coupon bond has less of it.
3. **When safe bonds pay 5%, stocks have to work harder to be worth it.** The expected edge of world stocks over
   Treasuries here is about 2% a year, small next to a bad year that can take 30-50%. That is why the plan takes
   stock risk only with money no promise depends on.
4. **A floor and a cap together make a promise you can keep.** The gift is "floor plus half the fund, but never above
   the announced top". Giving up some upside buys a range that cannot break.
5. **Lead gifts are signals.** People give more when a credible leader commits first, so a smaller certain gift can
   do more for the residency than a bigger uncertain one.
6. **Write the rule before you see the answer.** The October trade rule and the "keep half" rule were fixed before
   the results. That protects you from fooling yourselves.

**Five numbers to rebuild in your own Sheet** (so they are yours): the ladder cost from treasury.gov yields (price
each $50,000 as a zero: 50,000 / (1 + y/2)^(2t)); the floor cost (what $150,000 in late 2032 costs in January
2028); the 2031 range top (floor + half of about $41,000 grown three years); a bad-case gift (the fund falls 40%
before 2033); and the floor trade-off (move $25,000 of floor into stocks and compare). Each is a few spreadsheet
cells.

---

## 12. Calendar (Sydney time; Sydney moves to daylight time on Sun 4 Oct, the U.S. on Sun 1 Nov)

| Sydney | U.S. Eastern | What |
|---|---|---|
| Thu 1 Oct | Wed 30 Sep - Thu 1 Oct | Read-only login; team meeting and votes |
| Fri 2 Oct, 9:00 pm | Fri 7:00 am | Refresh tickets from the latest prices |
| Fri 2 Oct, 10:30 pm | Fri 8:30 am | U.S. jobs report (prices can jump) |
| Sat 3 Oct, 12:30 am | Fri 10:30 am | Kit's Plan A orders (or limit orders placed the evening before) |
| Tue 6 Oct, 1:30 am | Mon 5 Oct 10:30 am | Kit's VT order (or place it Friday) |
| Sat 10 Oct, 8:00 am | Fri 9 Oct 5:00 pm | **Roster due** |
| Thu 15 Oct, 7:00 am | Wed 14 Oct close | October check (rule-based; no trade is a valid result) |
| Sat 24 Oct, 8:00 am | Fri 23 Oct 5:00 pm | **Trading Notes Analysis due** (aim for Thu 22 Oct) |
| Sat 7 Nov, 8:00 am | Fri 6 Nov 4:00 pm | Trading ends; portfolio frozen |
| Sat 7 Nov, 9:00 am | Fri 6 Nov 5:00 pm | **IPS due** |
| Tue 10 Nov | Mon 9 Nov | Final Report instructions |
| Sat 5 Dec, 9:00 am | Fri 4 Dec 5:00 pm | **Final Report + school documentation due** |

---

## 13. Fixes I recommend but did not make

The permission system stopped me from editing files in the repo (it treats the team's repo as a shared resource),
so I changed nothing there. These are the fixes I would make, smallest first. Say the word and I can do them, or
anyone on the team can.

1. **Delete line 6 of `archive/rab/rescued/r4_hist_original.py`** (the local path that contains a student's school email),
   or delete `archive/rab/rescued/`. Nothing uses it.
2. **`archive/rab/trades/friday_checklist.md:38`:** replace the leader's name and initial with "the team leader" (the file's
   own rule says names stay out).
3. **`caplet/docs/AI_USE.md`:** a warning above sections 1-4 ("obsolete, describes the retired wharton-ic system; do not
   use in the Final Report"), and a row for tonight's review.
4. **`archive/rab/trades/check_gate_c.py:163`:** fall back to `archive/rab/numbers.yaml.sha256` when the Mac-only path is missing,
   so any teammate can run the Friday checks. Make `checks` depend on `blind-paths` in `archive/rab/Makefile`.
5. **`CLAUDE.md`:** it is two days behind. Replace the "Strategy status" and "insight_v1" sections with the adopted
   Root-and-Branch plan and the RAB kit; add the WInS facts seen on 29 Sep (300-character note box, 200%/100%
   position limits, half-of-volume rule, $3 minimum price, no Treasury maturing Feb 2031-Feb 2036, IBTN is
   INSCORP); the Gate A numbers; the decision calendar (1, 9, 14, 20, 22, 26 Oct and 6 Nov); the privacy state; and
   collapse the finished open items.
6. **Label or move the superseded files** (section 10 table, `caplet/decisions/LOG.md`, `MISSION.md`,
   `Laura_Gao_Strategy_Brief.pdf`) into an `archive/` folder with one README line saying what replaced them.
7. **Team decisions:** make the repo private; delete `aussef_complete_experiment_record.pdf` and the EXCLUDE-PRIVACY
   quotes; take the school name out of the repo description; archive `toolkit/src/wharton_ic`; delete the stale branches
   (`claude/zealous-turing-l19aqc`, `wip/ws7-stash-2026-09-30`); rebuild the truncated working paper on Ray's Mac.

---

## Appendix: sources checked tonight

- Official FAQ, fetched 30 Sep 2026: https://wghsinvcomp.smapply.us/res/p/faqs/ ("Investments permitted (for BOTH
  contributions)"; "required trading activity and portfolio management guidelines"; "Students should place trades on
  WInS, NOT the advisor"; semifinal presentations need every member).
- Treasury par yield curves 2026, fetched 30 Sep 2026 from home.treasury.gov (latest 29 Sep: 5y 5.06%, 10y 5.26%).
- Crossref, 30 Sep 2026: List & Lucking-Reiley (2002), *Journal of Political Economy* 110(1):215-233,
  doi:10.1086/324392; Andreoni (1998), *JPE* 106(6):1186-1213, doi:10.1086/250044; Vesterlund (2003), *Journal of
  Public Economics* 87(3-4):627-657, doi:10.1016/S0047-2727(01)00187-6.
- Official case, Trading Notes and IPS instructions, Competition Guide, SMApply deliverables page:
  `competition/official/2026_27/`.
