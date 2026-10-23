# Team Caplet timeline, 20 Aug to 20 Oct 2026 (verified events only)

> **Verified 20 Oct (`oct20/verify_tl_exp/verify_tl_exp.md`): all time conversions correct; counts wrong because the checkout was a shallow clone.** Totals: 208 commits on 22 branches (not 202 on 23); 103 Claude cloud commits (not 97); the insight_v1 run was 50 commits from Sun 27 Sep 21:38 AEST (first 9c58e98). Row 13 (ND "Big Idea") was written on or after 27 Sep (it only uses the 25 Sep curve). Missing Drive rows: case PDF on the team Drive from Thu 24 Sep 21:55 AEST; instruction PDFs 27 Sep 15:07; Guide/infographic/school template/Rules/Final Report docs 29 Sep 09:14-09:23; an AI scoresheet uploaded to the shared parent folder 29 Sep 13:22. RAB run = 82 commits (63 work + 19 merges). Comment times are "last modified/resolved", not posting times. **TNA disclosure: the VT and Nov-2040 WInS notes each contain a 13-word clause copied word for word from the public 30 Sep AI EXAMPLE notes; IBTP and IBTO share 8-9-word runs.**


AI-generated research (Claude Code, Tue 20 Oct 2026). **Not text to submit.** It lists dated, sourced events so that
students can write the Final Report's "Articulation of Competition Experience" themselves. It drafts no sentence for
any deliverable. If the team uses it, log that use in the AI-use record and the Works Cited (Wharton AI Policy:
"If you use AI to assist you in any way during the competition, how you use it must be recorded in your Works Cited
pages"). Wharton also bans invented "teamwork and experiential stories": where this file says *not recorded*, only a
student's own memory can fill the gap, and if nobody remembers, it stays blank.

## 0. How to read this

**Sources** (all read-only; nothing on Drive, WInS, SMApply or GitHub was changed):
- **Git**: `git -C /home/user/caplet-investment fetch origin` then `git log --all` (202 commits on 23 branches) plus
  the GitHub API for pull requests, PR comments, repo and fork creation dates (read 20 Oct). Dump:
  `oct20/timeline/data/gitlog_all.txt`, converted to Sydney/UTC in `data/git_sorted.txt` by `gitconv.py`.
- **Drive**: metadata (`createdTime`, `modifiedTime`) of every file in the "Caplet Investments" folder and its
  "AI Outputs" sub-folder, read 20 Oct; metadata only for four team docs that sit in the parent "Knox Wharton 2026"
  folder (Team List, Client Portrait, Resource, Rules (README!)). Other Knox teams' folders were not opened. Comment
  timestamps from the 19 Oct live read (`oct19/drive/ips_report_live.md:294-300`); the Final Report journal and
  Strategy Notes were re-read 20 Oct (no comments). Drive's connector shows only the owner account, never who
  created or typed anything, and cannot read version history.
- **Journal** = Google Doc "Final Report", tab "Competition Experience" (live text re-read 20 Oct; identical to
  `snap/main/team/google_drive/final_report.md:14-27`, cited as **J:line**).
- **ND** = Notes & Discussions live copy `oct19/drive/notes_and_discussions_live.md`.
- **WInS** = the 15 trade notes "Copied exactly from the WInS Trade Notes page ... on 13 Oct 2026, with times in US
  Eastern" (`snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:8-40`, cited
  **WN:line**). These are **order** times, not fill times.
- **Official**: Guide, case and instruction PDFs (`competition/official/2026_27/`), SMApply snapshot of 14 Oct
  (`smapply_public_2026-10-14/`, cited **TRD** = trading.txt, **FAQ** = faqs.txt).
- **Wharton emails**: only one is quoted anywhere in the repo (the 6 Oct "Week-2 email", `competition/COMPETITION.md:87-90`).
  No Wharton email is stored in the repo or on the Caplet Drive. A read-only Gmail search of the account this AI
  session runs under found no Wharton email (20 Oct).

**Short forms.** `oct19/` and `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` (and `oct20/`).
`snap/main/` = `/home/user/snap/main/` (main, 19 Oct). `COMP` = `/home/user/caplet-investment/COMPETITION.md`
(identical in main). `CM` = `/home/user/caplet-investment/CLAUDE.md` (14 Oct version). `AIU` = `snap/main/docs/AI_USE.md`.

**Time zones (checked twice with Python `zoneinfo`, script `oct20/timeline/conv.py`).**
- Sydney was **AEST (UTC+10) until 02:00 Sun 4 Oct 2026**, then **AEDT (UTC+11)**. Sydney was 14 hours ahead of
  US Eastern until 4 Oct, 15 hours from 4 Oct to 1 Nov, and is 16 hours ahead from Sun 1 Nov.
- WInS times are EDT (UTC-4). Git times are converted from each commit's own offset (cloud AI sessions commit in
  UTC; commits from the team leader's machine carry +10/+11).
- Dates written only as "29 Sep" in a team doc are left as written; the time zone they mean is not known.

**Who.** A first name appears only when a team record names the person (the journal names Darren and Eric) or
when an AI file attributes something to them (marked "per AI file"). Account names never prove who typed:
- "Ray identity" = commits signed with the git name Ray. 72 of them carry the AI trailer `Co-Authored-By: Claude`
  (71 made by an AI session on that machine, plus one GitHub merge of an AI commit); 30 carry no trailer (merges,
  two stash commits, and the 19 Sep build).
- "Repo-owner account" = the GitHub account that owns the repo and opened or merged most PRs.
- "Harry-named account" = a second GitHub account named after Harry, which owns the fork.
- "Owner account" = the single school Google account that owns every Caplet Drive file. Whether it belongs to the
  team leader is UNVERIFIED.
- Doc comments carry the owner account's display name. The 18 Oct suggestions carry a second display name, matching
  the team leader's first name. Whether these are one person is UNVERIFIED (`oct19/verify/verify_ips_exemplars.md:26-30`).

**Type.** **S** = student decision or student act shown by a team record. **S?** = a decision that only an AI file
records, attributed to the team or a student. **A** = AI output. **X** = external event (Wharton, markets,
calendar). **T** = team file activity whose author is unknown.

**Evidence strength.**
- **Strong** = a system timestamp (git, GitHub, Drive, WInS order time, PDF metadata).
- **Medium** = a dated entry in a team doc, with no author or time.
- **Weak** = only an AI-written file says it.

---

## 1. The timeline

### Phase 1. Before the case (20 Aug to 14 Sep)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 1 | Thu 20 Aug 12:25-12:26 AEST | 20 Aug 02:25:57-02:26:39 | Within 42 seconds, three items are created: the Drive folder "Knox Wharton 2026", its sub-folder "Caplet Investments", and the doc "Team List". The Team List allocates six students to "Caplet" (Ray, Darren, Harry, Eric, Young, Ahaan), alongside three other Knox teams. Its Roles column is blank, and so is its "Disputes / Suggestions" table | Drive metadata; `snap/main/team/google_drive/team_list.md:19-52` | Owner account (who set it up: not recorded; may be school admin) | T / strong |
| 2 | 10 Aug and 11 Sep (dates only) | - | Registration opens 10 Aug and closes 11 Sep; "the team's teacher advisor must complete the official registration" | `team_list.md:97-99, 122` (a school doc, not checked against Wharton) | - | X / UNVERIFIED |
| 3 | Sat 29 Aug 10:59 AEST | 29 Aug 00:59 | Doc "Client Portrait" is created and left empty (1 KB; last edit 22 seconds later) | Drive metadata | unknown | T / strong |
| 4 | 9-14 Sep (ET) | - | Wharton produces the PDFs (PDF creation metadata): Guide 9 Sep 14:22 EDT; IPS instructions 9 Sep 17:01; case and TNA instructions 10 Sep 15:19-15:21; school letter template 11 Sep; infographic 14 Sep | `pypdf` metadata of the files in `competition/official/2026_27/` | Wharton | X / strong (production dates, not release dates) |
| 5 | Fri 11 Sep 11:07 AEST | 11 Sep 01:07 | Doc "Notes & Discussions" is created in the Caplet folder. Nothing in it today is dated before 25 Sep (`oct19/verify/verify_numbers_office_notes.md:64`), so what it first held is unknown | Drive metadata | unknown | T / strong |

### Phase 2. Materials, practice and set-up (15 to 25 Sep)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 6 | 15 Sep ET (Sydney 15-16 Sep; hour not stated) | - | Competition materials are released to team leaders on SMApply, and the WInS practice period begins | Guide:162-165; `team_list.md:99` | Wharton | X / strong (date) |
| 7 | 15-25 Sep | - | Practice trading window, "done" ("All account activity will be cleared after the practice session"). No record shows any Caplet practice trade or login | `COMP:17`; `smapply_public_2026-10-14/wins.txt:27` | - | X / medium; team part not recorded |
| 8 | Sat 19 Sep 11:38 AEST | 19 Sep 01:38 | Doc "Resource" is created (parent folder) | Drive metadata | unknown | T / strong |
| 9 | Sat 19 Sep 11:48 AEST | 19 Sep 01:48:35 | The GitHub repo is created (public). It is still public on 20 Oct | GitHub API `created_at`, `private:false` | Repo-owner account | T / strong |
| 10 | Sat 19 Sep 12:54-16:24 AEST | 19 Sep 02:54-06:24 | Five commits build a generic "wharton-ic institutional investment operating system": about 17,000 lines, 7,445 of them in one commit 19 minutes after the first. It includes a demo client and an AI-use disclosure claiming all text was "authored 100% by student team members" (AIU:49) | `4854759`, `dd5755a`, `3f7cc71`, `b77748a`, `54bda02` (`git show --stat`) | Ray identity, no AI trailer. That volume suggests a code-generation tool (inference; the tool is UNVERIFIED) | A? / strong (commits); weak (tool) |
| 11 | 24 Sep (log date) | - | Claude (Cowork) reads the case and does web research on the WInS rules, past winners and LDI (liability-driven investing) | AIU:86 | AI; who asked: not recorded | A / weak |
| 12 | 25 Sep (log date) | - | Claude (Cowork) writes the mandate YAML, a projection model and decision memos D1-D8. D1 is "Strategy A, 'Lock, then grow'". D3 already uses iBond ETFs IBTM-IBTR for the 2033-37 payments. It ends with outlines for every deliverable. The memos say "The student committee must accept, change or reject each decision" | `caplet/decisions/LOG.md:7-47` as committed in `2b9376c`; AIU:87-90 | AI | A / weak (written 25 Sep per log; committed Tue 29 Sep 10:16 AEST) |
| 13 | 25 Sep (as dated in ND) | - | ND's "Big Idea": buy all ten $50k payments with the first $300k, "about $294,000". ND adds: "The idea came from our AI council run on 27 September" | ND:58-66 | AI idea, per ND itself | A / medium |

### Phase 3. The AI research burst and the plan (26 Sep to 1 Oct)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 14 | Sat 26 Sep 20:29 AEST | 26 Sep 10:29 | First cloud Claude Code session: the official case is put in the repo (manifest `received_date: 2026-09-26`) | `d0dde73`; `manifest.yaml` | AI | A / strong |
| 15 | Sun 27 Sep 08:52 AEST | 26 Sep 22:52 | AI commit "remove fictional client and invented Wharton rules" from the 19 Sep build | `5ae851f` | AI | A / strong |
| 16 | Sun 27 Sep 14:36 AEST | 27 Sep 04:36 | Roster file: six first names, Ray as "Team Leader", source "TEAM_LEADER_PROVIDED" | `734d466`; `toolkit/config/team_roster.json` | AI recording the team leader's input | S? / strong (file) |
| 17 | 27 Sep (snapshot date) | - | The team's own working doc (Google Doc "2026 Wharton Global High School Investment Competition") is copied in as council input, labelled "Student-authored brainstorming". It sets out LDI; "2 clocks"; three buckets; a glide path from ~75% equity; an "Entry 0 pre-mortem (2026-09-27)"; and three options: "lock everything early / lock part now and raise it by rules (author leans to this) / wait until 2033". It also notes the sector-minimum claim as UNVERIFIED | `keel/library/council_2026-09-27/team_notes_2026-09-27.md:1-60` | Students per the AI's label; individual authors not named. The doc is not in the Caplet folder today (location unknown) | S / medium |
| 18 | 27 Sep | - | The AI reviews two team docs ("Why Wharton chose Laura", "Client Profile: Laura Gao"), "written by the team from public sources". It keeps some ideas and rejects others as conflicting with the case | `keel/library/team_materials/review_why_laura_and_public_profile.md:1-30`; CM:136 | Team (per AI); AI review | S / weak; A |
| 19 | Sun 27 Sep 19:54-20:44 AEST | 27 Sep 09:54-10:44 | AI strategy council, rounds 1-2 (Lock-early vs Growth-first). The team's original growth-first plan "failed: 3-8% payment shortfall" in the AI model. Official market data and a verified ladder cost are added | `5429887`, `bfb4e03`, `bae7303`; CM:63-71; `keel/library/council_2026-09-27/README.md` | AI | A / strong |
| 20 | Sun 27 Sep 20:38 AEST | 27 Sep 10:38 | "Interview part 2": "the team deferred to the assistant's evidence-based calls", with four provisional calls (60% equity, floor plus upside, leftover as flexibility, no roles assigned) | `fdd7412`; CM:75-80 | "the team" per AI file; who answered: not recorded | S? / weak |
| 21 | Sun 27 Sep 20:39-21:16 AEST | 27 Sep 10:39-11:16 | AI files record, as the team leader's instructions: semifinals-first priority; the mandate; last year's lessons ("over-complex", "traded assets outside the trading rules"); the advisor "handles administrative work only" | `c44a601`, `e083f75`, `ade6d06`; CM:32-45 | Attributed to Ray (per AI file) | S? / weak |
| 22 | Sun 27 Sep 22:11 to Tue 29 Sep 09:34 AEST | 27 Sep 12:11 - 28 Sep 23:34 | "insight_v1" AI run, 44 commits (main work to Mon 28 Sep 15:59; report layout to 29 Sep 09:34): 472 questions, 48 surviving, specialists, red teams, chief strategist. Its 27 Sep fact register already quotes the public FAQ line "Investments permitted (for BOTH contributions)" and lists it as open question 10 | `9990a98` ... `fe9717d`; `keel/library/insight_v1/phase_A/wins_week1_guardrails.md:194, 518` | AI | A / strong |
| 23 | Mon 28 Sep 09:51 AEST | 27 Sep 23:51 | Scope narrowed to "Trading Notes and IPS only; no Final Report" | `a4c1e40`, `883d48a`; CM:84 ("scope set by Ray") | Attributed to Ray | S? / weak |
| 24 | Mon 28 Sep 09:55 AEST | 27 Sep 23:55 | Google Doc "IPS Report" is created | Drive metadata | unknown | T / strong |
| 25 | Mon 28 Sep 15:16-15:19 AEST | 28 Sep 05:16-05:19 | An AI tool server (Serena MCP) is added (PR #2). OpenAI's Codex review bot posts its first review | `9722876`, `8f8a69e`; PR #2 comments | AI; merged by repo-owner account | A / strong |
| 26 | Mon 28 Sep 15:22-15:38 AEST | 28 Sep 05:22-05:38 | The AI's final strategy spec ("REC"): 2027 buys the ten payments; 2028 tops up the ladder, buys a floor of about $150k and puts about $40k in one world fund; the 2031 range runs from the floor to the floor plus half the fund. In a blind "Laura's Choice" contest, 3 of 3 AI evaluators rank it first | `5ea5875`, `2854ce1`; CM:86-93 | AI | A / strong |
| 27 | Mon 28 Sep 18:29-18:30 AEST | 28 Sep 08:29:55-08:30:21 | Folder "AI Outputs" is created in the Caplet Drive, holding six insight_v1 files (trading_notes_pack, ips_spec, why_us, strategy_changes, securities_and_allocation, open_questions) | Drive metadata | Uploader unknown; AI content | A / strong |
| 28 | Mon 28 Sep 23:30 AEST | 28 Sep 13:30 (09:30 EDT) | Official WInS trading begins | TRD:24; COMP:18 | Wharton | X / strong |
| 29 | Tue 29 Sep 09:19 and 09:23 AEST | 28 Sep 23:19, 23:23 | Docs "Rules (README!)" (parent folder) and "Final Report" (the journal) are created | Drive metadata | unknown | T / strong |
| 30 | Tue 29 Sep 09:32-09:35 AEST | 28 Sep 23:32-23:35 | PR #1 (all research so far, plus a 27-page client report) is merged into main "at Ray's request" (AI file) | GitHub PR #1 `merged_at`; CM:112 | Merged by repo-owner account | S? / strong (merge), weak (request) |
| 31 | Tue 29 Sep 11:43 AEST | 29 Sep 01:43 | Doc "Strategy Notes" is created; last edited Wed 30 Sep 10:24 AEST | Drive metadata | unknown | T / strong |
| 32 | Tue 29 Sep 12:05 AEST | 29 Sep 02:05 | AI test of smaller floors (answering "reads as timid"): it recommends keeping $150k. "Pending team vote (D2/D6)" | `830cef0`; AIU:60 | AI | A / strong |
| 33 | Tue 29 Sep 13:03 AEST | 29 Sep 03:03 | Ladder re-priced on the 28 Sep curve. A second AI (ChatGPT, "GPT-6 Astra") gets a blind brief; the Claude session "entered it in ChatGPT" | `84e7010`; AIU:61-62 | AI (two vendors) | A / strong |
| 34 | 29 Sep (date in team docs) | - | First WInS session-rules read: minimum price $3, not $5; 300-character note box; no WInS Treasury maturing Feb 2031-Feb 2036, so iBond ETFs; "IBTN" is an unrelated company. A "Week 1 email" PDF is on the WInS dashboard and is "not read here" | J:17-18; `sheets/portfolio_and_trading_notes/wins_notes.csv:1-19` ("read 29 Sep 2026, no orders placed") | "we" (J); wins_notes author unknown (its style reads like AI) | T / medium |
| 35 | Tue 29 Sep 21:48-23:24 AEST | 29 Sep 11:48-13:24 | Five AI "IPS Exemplar" .docx files (v3, v7, v12, v13 and v14, the last two titled "Roots First") are uploaded to AI Outputs. The AI log says v3 was written "at the team leader's request" and later versions were rewritten "to remove AI-style patterns" and tested with "an AI-voice detector" | Drive metadata; AIU:64-66 | AI; request attributed to the team leader | A / strong |
| 36 | 29-30 Sep | - | Two WInS bond prices are found stale (~1 point of yield off). New rule: yield-check every bond within 25bp; swap Feb-2038 for May-2038 | J:19 | "we"; who found it: not recorded | S / medium |
| 37 | Wed 30 Sep 00:09-17:33 AEST | 29 Sep 14:09 - 30 Sep 07:33 | Overnight "RAB" AI run: 8 workstreams, about 90 commits, gates A-D. It produces models, decision memos "for the team to ratify", Friday trade tickets and 23 "EXAMPLE - team rewrites" notes. At 10:15 AEST it writes two tabs ("RAB Tickets", "RAB Notes") into the team Sheet via the Sheets connector | `35d2c3a` ... `156a682`; `0141438`; AIU:67-76 | AI on the Ray-identity machine | A / strong |
| 38 | Wed 30 Sep (overnight, Sydney) | - | An AI repo review says: "The 'adopted IPS' in the Google Doc is an AI-written exemplar" | `snap/main/research/assistant_review_2026-10/03_Repo_Review_30Sep2026.md:3, 22-24` | AI | A / medium (file dated in text; committed 16 Oct) |
| 39 | Wed 30 Sep 17:20-17:23 AEST | 30 Sep 07:20-07:23 | An IPS draft PDF is uploaded to the Caplet folder (two PDFs dated 30 Sep are in `caplet/ips_drafts/`) | Drive metadata | unknown | T / strong |
| 40 | 30 Sep | - | The IBTR order ticket errors; after-hours iBond spreads are very wide; plan for limit orders in market hours; Treasuries are entered in $1,000-face units | J:20 | "we" | S / medium |
| 41 | Wed 30 Sep 21:28-21:35 AEST | 30 Sep 11:28-11:35 | RAB working paper PDF; every branch merged into main (PR #4). **Git then goes silent for 14 days** (next commit Wed 14 Oct 21:16) | `5c0a861`, `b232000`; PR #4 | Ray identity | T / strong |
| 42 | 1 Oct | - | Journal: "model check backed the $150k floor and 50/50 split; IPS content locked. Strategy name settled as Root-and-Branch (earlier 'Roots First')". An AI 3-page brief was "sent before the first trades". An AI-planned "1 Oct vote (book, swap rule, roles)" has no recorded result | J:21; `snap/main/research/assistant_review_2026-10/README.md` (row for `02_...1Oct2026.pdf`); AIU:72, 75 | "we"; no names, vote count or dissent | S / medium (the lock); A (brief) |
| 43 | Late Sep (undated) | - | Journal: the strategy changed from "lock the ladder in 2027, 80/20 growth sleeve, two-tier lock in 2031" to "a bought Treasury floor plus a world fund ... Reason: better outcomes in bad years. [who argued what]" | J:16 | "we"; "[who argued what]" still blank | S / medium |

### Phase 4. Trading (2 to 9 Oct)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 44 | Fri 2 Oct ET (Fri 2 Oct 23:30 AEST open) | 2 Oct 13:30 | The planned trading day ("RAB Tickets: Friday 2 Oct 2026 WInS orders"). **No order is recorded that day.** The first recorded order is 6 Oct 7:55 PM ET. Why trading slipped is not recorded | `sheets/portfolio_and_trading_notes/rb_tickets.csv:1`; WN:14-40 | - | gap / strong (absence of orders in WInS notes) |
| 45 | Sun 4 Oct 02:00 | 3 Oct 16:00 | Sydney daylight saving starts: Sydney is now 15 hours ahead of ET | NSW DST rule (zoneinfo) | - | X / strong |
| 46 | Mon 5 Oct (journal date) | - | **Three journal entries.** (a) "a teammate found a rule requiring one stock per sector per team member", traced to a mislabelled third-party site; the official page says there is no sector minimum. (b) "**Darren argued the world fund is a 'copout'** and proposed normal stock and ETF picking; Taiwan (EWT) and gold (GLD) were also raised. Outcome and reasons: [fill in]". (c) The facility floor was found to sit inside the operating reserve; "four phrases" were fixed | J:22-24 | (a) an unnamed teammate; (b) Darren; (c) "we" | S / medium |
| 47 | Mon 5 Oct 16:50 and 17:00 AEDT | 5 Oct 05:50, 06:00:57 | "Rules (README!)" is last edited. Ten minutes later, the current Sheet "Portfolio and Trading Notes" is created. It already holds the RAB tabs that AI wrote to "the team Sheet" on 30 Sep, so it is a copy or a rebuild (how: not recorded) | Drive metadata; `sheets/portfolio_and_trading_notes/rb_tickets.csv:1-2` | unknown | T / strong |
| 48 | 6 Oct (Sheet date) | - | "AUDIT REVIEW — 6 OCT 2026" is added to the Sheet's Trading Notes tab: "33 reviewed entries"; "These are AI-assisted proposals from the completed desk review", with "Proposed note — AI draft, not saved in WInS" for each order. Its source folder (`audit/2026-10-06_full_notes_review/`) is not in any repo branch | `sheets/portfolio_and_trading_notes/trading_notes.csv` rows 1-4, columns R-U | AI | A / medium |
| 49 | 6 Oct (email date; arrival time not recorded) | - | Wharton "Week-2 email": "Portfolio construction and recommendations for both contributions may include only approved investment types: eligible stocks, ETFs and Treasury bonds available on WInS." STRIPS and single zero-coupon Treasuries are now out of Laura's real plan | COMP:87-90 (quote only; the email itself is not stored) | Wharton | X / weak-medium (text quoted by AI file; arrival time UNVERIFIED) |
| 50 | **Wed 7 Oct 00:30 AEDT** | 6 Oct 13:30 (09:30 EDT, 6 Oct open) | Journal: "Oct7: **Eric** fall in sleep because our time is freaking 12:30 AM that the market would open". The journal was last edited at Wed 7 Oct 10:28 AEDT, so this entry must refer to the 00:30 open on Wed 7 Oct Sydney (inference from timestamps). **No note-bearing order was placed in that session**: the first is 10 hours later. "Zoom meetings and discussions on the portfolio" (J:26) is undated | J:26-27; Drive `modifiedTime` 2026-10-06T23:28:33Z; WN:24 | Eric named; writer unknown | S / strong (timestamps) + medium (entry) |
| 51 | **Wed 7 Oct 10:55-13:01 AEDT** | 6 Oct 23:55 - 7 Oct 02:01 (6 Oct 7:55-10:01 PM EDT, after the close) | **First order pass, 10 orders from 2042 backwards**, each with a note: Nov-2041 (7:55 PM), Nov-2040 (7:59), Nov-2039 (8:02), May-2038 (8:13), Feb-2037 (8:17), IBTR (8:31), IBTQ (8:36), IBTP (8:45), then a 73-minute gap, IBTO (9:58), **IBTM (10:01:41 PM)** | WN:18-24, 37-40 | "placed by Ray" (COMP:172, an AI-written file). An AI browser was also working the WInS screens (COMP:192-193). Who clicked each order: not recorded | S (trades) / strong (times); weak (who) |
| 52 | Wed 7 Oct 11:02-19:42 AEDT | 7 Oct 00:02-08:42 | **Four orders cancelled and re-placed with edited notes**: Nov-2039 (new order 6 Oct 11:45 PM EDT = 14:45 AEDT), May-2038 (12:22 AM EDT 7 Oct = 15:22), Feb-2037 (12:24 AM = 15:24), IBTR (4:42:53 AM = 19:42). The IBTR note's test changes from "more than 0.3 percentage points" to "more than about 0.2". The Nov-2039 note's "scaled 2040 payment" becomes "$50,000 payment on 1 Jan 2040" | WN:15-18 vs WN:37-40 | unknown | S? / strong (times); reasons not recorded |
| 53 | Wed 7 Oct, between 11:13 and 15:22 AEDT (window from order times) | 7 Oct 00:13-04:22 | **Mis-click**: "an AI browser click cancelled the wrong order (May-2038) because the page had scrolled". Rule since: "only Ray places or cancels WInS orders. AI may fill a ticket up to Preview". Wharton's FAQ advice on errors: "we encourage you to run with it" | COMP:192-193; FAQ:66 | AI caused it; the rule is a team rule (who set it: not recorded) | A + S? / weak (one AI-written line; time window is inference) |
| 54 | Thu 8 Oct 00:30 AEDT | 7 Oct 13:30 (09:30 EDT) | US open. "Orders placed while the market is closed are filled at the security's opening price when the market reopens", so the ten ladder orders probably filled on 7 Oct ET; WInS bonds "fill at end-of-day prices" | TRD:33, :52 ("You are not expected to stay awake during the night to trade"); `wins_notes.csv:15` | WInS | X / fill times UNVERIFIED |
| 55 | **Thu 8 Oct 11:27 AEDT** | 8 Oct 00:27 (7 Oct 8:27:19 PM EDT) | **VT order** (167 shares) with its note. Probable fill at the 8 Oct open (Fri 9 Oct 00:30 AEDT; UNVERIFIED). After it: 11 of 200 trades, cash $3,513.79, "Plan: hold, no more trades" | WN:14; COMP:172-189 | Order: see row 51. "Plan: hold": who decided not recorded | S / strong (order); weak (plan) |
| 56 | By Fri 9 Oct 5:00 PM EDT (Sat 10 Oct 08:00 AEDT) | by 9 Oct 21:00 | Roster submitted and locked | COMP:19 ("submitted") | Submitter and time not recorded | S / weak |
| 57 | 28 Sep to 9 Oct | - | NSW spring school holidays; Term 4 begins Tue 13 Oct; HSC written exams start Tue 13 Oct. "All trading happened in the Knox holidays" | `snap/main/research/assistant_review_2026-10/oct16/lenses/L10_team_process.md:33, 120-127` (sources accessed 16 Oct) | - | X / medium |

### Phase 5. Quiet week (10 to 14 Oct)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 58 | Sun 11 Oct 19:41-19:45 AEDT | 11 Oct 08:41-08:45 | Sheet "... Project Management Dashboard" is created. It has been empty ever since | Drive metadata; `oct19/drive/pm_dashboard_live.md` | unknown | T / strong |
| 59 | 13 Oct (date in text) | - | The 15 WInS notes are copied "exactly from the WInS Trade Notes page" into the IPS Doc (tab "WInS Trading Notes"), with three suggested picks (IBTM, re-placed IBTR, VT) | WN:8, :26-31 | unknown (style reads like AI) | T / medium |
| 60 | 13 Oct | - | A scheduled AI routine writes its "baseline" check: "AMBER ... the Deliverables tab is still empty". It runs from the team leader's machine (`/Users/ray/Research/caplet-monitor/`) | `snap/main/ops/monitor_reports/2026-10-13 Caplet check.md:1-4`; `keel/routines/tasks/scheduled_tasks/*.md` | AI | A / medium |
| 61 | **Tue 13 Oct 19:11 AEDT** | 13 Oct 08:11:17 | Comment on the V4/V3 page: "This page is for us to humanise V3" (still open) | `oct19/drive/ips_report_live.md:298` | Owner account (who typed: UNVERIFIED) | T / strong |
| 62 | **Tue 13 Oct 19:15 AEDT** | 13 Oct 08:15:50 | Comment "Content is LOCKED but we need to rewrite by ourselves", resolved at the same timestamp | `oct19/drive/ips_report_live.md:299-300` | Owner account | T / strong |
| 63 | Wed 14 Oct 21:16-21:50 AEDT | 14 Oct 10:16-10:50 | Onboarding commit: `competition/COMPETITION.md`, `caplet/START_HERE.md`, read-only exports of all team Docs/Sheets, STRIPS banners, scheduled routines (including mock-judge panels on 19 Oct, 1 Nov, 22 and 30 Nov). PR #5 merged 21:50. Codex bot reviews it | `44f1296`, `2affd4c`; PR #5; COMP:29-30 | Ray identity + AI trailer; merged by repo-owner account | A / strong |
| 64 | after 14 Oct | - | Notes & Discussions gets no new content after this (only a tab rename on 17 Oct) | `oct19/verify/verify_numbers_office_notes.md:63` | - | T / strong |

### Phase 6. AI suggestions and exemplars in the Doc (15 to 18 Oct)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 65 | Fri 16 Oct 09:09-09:10 AEDT | 15 Oct 22:09-22:10 | The Harry-named account forks the repo (fork public) and opens PR #6: AI review 30 Sep-15 Oct, including a 15 Oct team brief. Merged Fri 16 Oct 20:59 by the repo-owner account | `cf43a9d`; GitHub forks and PR #6 | Harry-named account; AI content (labelled so) | A / strong |
| 66 | Fri 16 Oct 12:24 AEDT | 16 Oct 01:24 | AI IPS number sheet on the 15 Oct curve, plus an "[AI] suggestion rule" described as "Ray's 16 Oct rule" (PR #7, still open) | `412e9e3`; PR #7 body | AI; rule attributed to Ray | A + S? / strong, weak |
| 67 | **Fri 16 Oct 21:05-21:15 AEDT** | 16 Oct 10:05-10:15 | AI writes 13 [AI]-tagged suggestions into IPS V5. Its log: "At Ray's request removed every [AI] tag"; suggestions 1-4, then 5-13, "Accepted by the team". These rows exist only on the unmerged branch | `3544562`, `11218fd`, `dec13d1`; `git show origin/claude/fervent-edison-sqk1ry:caplet/docs/AI_USE.md` rows 77-79 | AI; request and acceptance attributed (no names) | A + S? / strong (commits), weak (acceptance) |
| 68 | Fri 16 Oct 21:45-22:43 AEDT | 16 Oct 10:45-11:43 | AI North Star memo (built on "Ray's competition tips"), pre-mortem, number checks (PR #8, open) | `0f1b129`, `a356283`, `a6323d1`; PR #8 body | AI | A / strong |
| 69 | 16 Oct | - | AI review "What stops us winning" (recommends a Sun 18 Oct meeting with five votes) | R16 (`snap/main/research/assistant_review_2026-10/04_What_Stops_Us_Winning_16Oct2026.md`) | AI (this review series) | A / strong (merged 19 Oct) |
| 70 | **Sat 17 Oct 11:56 to Sun 18 Oct 11:50 AEDT** | 17 Oct 00:56 - 18 Oct 00:50 | AI session, 16 commits: 2031 range model; 12:11 an edit sheet saying "No replacement wording"; 12:24 an exemplar pitch, IPS and three TNA reflections, versions v1 to v12 in about 23 hours "(Ray's request ...) also in the IPS Report Doc as SUGGESTIONS only ... Ray reviews all". At 18:15-18:22 a style study adds "AI tells" and the StoryScope paper | `fa08d47` ... `1ed9130`; `git show origin/claude/trusting-euler-gms43m:CLAUDE.md` lines 19-21; PR #9 | AI; request attributed to Ray | A / strong |
| 71 | Sat 17 Oct 12:12 AEDT | 17 Oct 01:12 | Reply on PR #9 from the repo-owner account: "Fixed in the next commit (not yet pushed)..." (reads like the AI session) | PR #9 review comments | Repo-owner account | T / strong (time) |
| 72 | Sat 17 Oct 12:28 AEDT | 17 Oct 01:28 | Sheet last edited: the TN Analysis tab gets the three pick rows; "Owner" and the reflections stay blank | Drive metadata; `oct19/verify/verify_tna_judges_sheets.md:47-48` | unknown | T / strong |
| 73 | Sat 17 Oct 14:05 AEDT | 17 Oct 03:05 | Notes & Discussions tab renamed "⭐ STRATEGY" | Drive metadata; `oct19/notes/decision_log.md:6` | unknown | T / strong |
| 74 | **Sat 17 Oct 18:03 AEDT** | 17 Oct 07:03:48 | Comment on V5 "Best version that AI generated; We cannot submit as it is and we still need to refine and proofread it" is resolved, 4 minutes before the AI's exemplar-v5 commit (18:07) | `oct19/drive/ips_report_live.md:296-297`; `1b1327c` | Owner account | T / strong |
| 75 | Sat 17 Oct 23:03 to Sun 18 Oct 11:49 AEDT | 17 Oct 12:03 - 18 Oct 00:49 | V5 is replaced by exemplar v11 (lightly cut; who accepted or cut it: UNVERIFIED). At 11:49:31 AEDT, 20 tracked changes (v12) appear under the display name matching the team leader's first name, 32 seconds before the v12 commit. The Doc has not been edited since | `oct19/verify/verify_ips_exemplars.md:17-40`; Drive `modifiedTime` 2026-10-18T00:49:32Z | AI insertion through a signed-in account (per the AI's own file); reviewer UNVERIFIED | A / strong |
| 76 | Sun 18 Oct | - | The meeting the 16 Oct review asked for: **no record** that it happened | `oct19/notes/decision_log.md:39` | - | gap |

### Phase 7. Rule reversal and outside feedback (19 to 20 Oct)

| # | Sydney | UTC | What happened | Evidence | Who | Type / strength |
|---|---|---|---|---|---|---|
| 77 | Mon 19 Oct 09:41-09:45 AEDT | 18 Oct 22:41-22:45 | The 16 Oct review is pushed and merged (PR #10) | `0ad520b`, `e5322d3`; PR #10 | Harry-named account pushed; merged via GitHub by an account named Harry | A / strong |
| 78 | **Mon 19 Oct 09:56-10:28 AEDT** | 18 Oct 22:56-23:28 | "Caplet Research Office": 26 AI agents cut to 18; main CLAUDE.md now says AI must "Never write, rewrite or suggest wording for anything submitted ... even if asked"; checking work only until the IPS. PR #11 merged 10:28. No team vote recorded; the charter itself requires "a logged whole-team vote" | `4bccffd` ... `f191d6e`; `snap/main/CLAUDE.md:6-17`; AIU:77-78 ("At the team leader's request") | AI; merged by repo-owner account | A + S? / strong |
| 79 | Mon 19 Oct 19:57 AEDT | 19 Oct 08:57 | The "Knox Wharton 2026" Drive folder is shared with the personal Google account this AI review series runs under; the 19-20 Oct Drive reads start after this | Drive `sharedWithMeTime`; Gmail notification | A school account shared it (who: not reproduced) | T / strong |
| 80 | Mon 19 Oct 20:35-20:37 AEDT | 19 Oct 09:35-09:37 | Office memo WO-0002: "a former Wharton judge told the team that the IPS cannot reach the semifinals. The judge's reasons were not passed on". "Asked by: team lead (Ray, assumed from the account)". PR #12 open | `git show origin/claude/ecstatic-wright-76bbun:keel/office/outbox/2026-10-19_WO-0002_judging_ips-v5-why-not-semifinal.md` lines 1-6; office LEDGER | The judge's verdict: team report, UNVERIFIED (when, who met them, and what they saw: not recorded) | X (reported) + A / weak |
| 81 | Tue 20 Oct 00:04 AEDT | 19 Oct 13:04 (re-checked 13:32) | The live Wharton FAQ now lists TIPS and STRIPS as "NOT permitted", and "over 10 weeks of trading" has become "over six weeks". The cached 16 Oct copy lacks these lines | `oct19/askwharton/questions_for_wharton.md:63-74` | Wharton (seen by AI session) | X / strong (seen time); change time UNVERIFIED |
| 82 | 19 Oct 23:30 to 20 Oct | - | AI "Caplet update 19 Oct" plus kits (TNA, IPS, Final Report prep, defence drill, coupon study, co-sponsor research, questions for Wharton); this timeline (20 Oct 08:40 wave) | `oct19/out/`; this file | AI (this review series) | A / strong |

**Coming deadlines (for context):** TNA Fri 23 Oct 5:00 pm EDT = Sat 24 Oct 08:00 AEDT; trading freeze Fri 6 Nov
4:00 pm EST = Sat 7 Nov 08:00 AEDT; IPS Fri 6 Nov 5:00 pm EST = Sat 7 Nov 09:00 AEDT; Final Report Fri 4 Dec 5:00 pm
EST = Sat 5 Dec 09:00 AEDT (COMP:15-24; converted with `conv.py`).

---

## 2. What the record shows overall (patterns, all checkable)

- **Records by kind.** Of 202 commits, 97 are by Claude in cloud sessions and 72 are by the Ray identity with an AI
  trailer (71 local, 1 GitHub merge). 30 are Ray-identity commits without a trailer (the 19 Sep build, merges and two stash commits), and 3 are
  by Harry-named accounts (1 push without a trailer, 1 with one, 1 GitHub merge). No commit is clearly a student
  writing in their own words. Counts: `data/git_sorted.txt`.
- **Two silent stretches.** Git: none between Wed 30 Sep 21:35 and Wed 14 Oct 21:16 AEDT, which covers all the
  trading. Drive: no Caplet file was changed after Sun 18 Oct 11:49 AEDT (Drive metadata, 20 Oct).
- **Student voice on record**, as opposed to AI text or unattributed "we":
  - the 27 Sep team notes doc, labelled student-authored by the AI that copied it;
  - Darren's 5 Oct challenge (J:23);
  - the Eric entry (J:27);
  - three Doc comments (13 and 17 Oct), whose author is UNVERIFIED;
  - about 230-240 words of informal notes in ND (`oct19/verify/verify_numbers_office_notes.md:65`).
- **Every decision row lacks** a vote count, names or dissent, except Darren's challenge, which has a name but no
  outcome.

---

## 3. (a) Real turning points, with evidence strength

Ranked by how much they changed the plan or the process. "Strength" applies to *that it happened when stated*.
"Missing" is what a student must add before using it in the Final Report.

| # | Turning point | Date (Sydney) | Evidence | Strength | Missing / caution |
|---|---|---|---|---|---|
| TP1 | **From the team's growth-first "two clocks" plan (about 75% equity, reserve bought later) to buying all ten payments first** | 25-27 Sep (AI Cowork D1 on 25 Sep; council and "deferred" interview on 27 Sep) | Rows 12, 17, 19, 20; CM:63-80 | Strong that AI recommended it; **weak** that the team decided it (only "the team deferred", in an AI file) | Who agreed, and why. Credit the idea as AI-originated (ND:62 already says so). The team's own notes already leaned to "lock part now" (row 17): that nuance is true and checkable |
| TP2 | **Floor plus world fund, range = floor to floor + half** (replacing the 2031 two-tier lock-in) | 28 Sep (AI spec) to 1 Oct (journal "locked") | Rows 26, 32, 42, 43 | Medium (journal dates it; no vote) | "[who argued what]" (J:16); the vote, if any |
| TP3 | **First WInS login changed the building blocks**: no 2031-36 Treasuries, so iBond ETFs; session rules differ from the public guide; stale bond prices led to a yield-check rule | 29-30 Sep | Rows 34, 36, 40 | Medium (journal plus a WInS read file) | Who found each one. Note: AI memo D3 had already proposed iBond ETFs on 25 Sep (row 12), so "we discovered" needs care |
| TP4 | **Darren's "copout" challenge** (stock picking; EWT, GLD) | 5 Oct | Row 46 | Medium (named, dated, team doc) | The outcome and reasons, from Darren and the team. The strongest true dissent story on record |
| TP5 | **Wharton's 6 Oct email removed STRIPS from Laura's real plan**; IBTM became the real floor holding, not a stand-in | 6 Oct | Row 49; J:24 vs COMP:155 | Weak-medium (quoted text only; arrival time unknown) | Who read it, when, and what the team did that day. The "for BOTH contributions" line was already public and flagged as an open question on 27 Sep (row 22): a fair "what we'd do differently" point |
| TP6 | **The trading night**: 14 order events, 4 cancel-and-re-place, IBTR's test tightened from 0.3 to "about 0.2", an AI mis-click, then "only Ray trades" | Wed 7 to Thu 8 Oct (6-7 Oct ET) | Rows 50-55 | Strong for times; weak for the mis-click and the rule (one AI-written line); none for the reasons behind 3 of the 4 re-placements | Who was awake; who typed each note; why each re-placement; how the mis-click was found. Also: the note words came from AI drafts (row 48; the VT note's last clause matches the AI exemplar word for word, `oct19/verify/verify_tna_judges_sheets.md:56`), so disclose that with the TNA |
| TP7 | **"Rewrite by ourselves" (13 Oct) turned into AI suggestions and exemplars inside the Doc (16-18 Oct)** | 13 Oct 19:11 to 18 Oct 11:49 | Rows 61-62, 67, 70, 74-75 | Strong (timestamps) | Who wrote the comments; who asked for and accepted the AI text. Usable as a growth story **only if** the students' own rewrite really happens and the Works Cited matches |
| TP8 | **AI-never-writes rule merged; outside judge says the IPS won't reach the semis; Wharton bans STRIPS/TIPS in the FAQ** | 19-20 Oct | Rows 78, 80, 81 | Strong (rule merge, FAQ); weak (judge, second-hand) | A logged team vote on the AI rule; what the judge saw and said; what the team decides by 27 Oct |

**Often claimed, but not a turning point on the record:**
- "1 Oct: IPS content locked" (J:21). On 30 Sep the Doc's IPS was an AI exemplar (row 38), and V5's wording was later
  replaced by AI exemplar v11 (row 75).
- "13 Oct: content LOCKED". The comment is resolved, but the content kept changing.
- The 2 Oct "Friday trades". They never happened (row 44).

---

## 4. (b) Gaps where the record is silent (students fill these from memory only)

Each gap gives what is known and what is missing. If nobody remembers, leave it blank. Do not reconstruct a gap from
this file.

| # | Period | Known | Silent: students must supply |
|---|---|---|---|
| G1 | 20 Aug - 14 Sep | Folders and Team List created 20 Aug; Client Portrait created empty 29 Aug; ND created 11 Sep | How the team formed and got its name; who registered (the advisor, per the school doc); first meetings; what ND first held |
| G2 | 15-25 Sep | Materials released 15 Sep ET; practice window | Who first read the case, and when (the repo only has it from 26 Sep); any practice trades or lessons |
| G3 | by 27 Sep | Team notes doc (LDI, two clocks, three buckets, "author leans to" partial lock) | Who wrote which part; where the doc is now (not in the Caplet folder); whether AI helped write it |
| G4 | 27 Sep | "the team deferred to the assistant's evidence-based calls" | Who answered the interview; whether everyone agreed; any disagreement |
| G5 | 28 Sep - 1 Oct | AI spec 28 Sep; journal "late Sep" change and "1 Oct ... locked" | Was there a 1 Oct meeting? What was voted (book, swap rule, roles)? "[who argued what]" |
| G6 | 2-6 Oct | Planned trades on Fri 2 Oct; first order 6 Oct 7:55 PM ET | Why trading slipped by four days |
| G7 | 6 Oct | Email text quoted | When the email arrived and who read it; did it arrive before the IBTM order (6 Oct 10:01 PM ET)? This decides whether IBTM "refined" the strategy |
| G8 | Night of 6-7 Oct ET | Order times; one cancellation by AI click | Who stayed up for the 00:30 open on Wed 7 Oct and why no order went in then; who typed and submitted each order; why Nov-2039, Feb-2037 and IBTR were re-placed; why "0.3" became "about 0.2"; how the mis-click was noticed |
| G9 | 7-8 Oct ET | "filled 7-8 Oct" | Exact fill times and prices from WInS Transaction History (screenshot it) |
| G10 | by 9 Oct | "submitted" | Who submitted the roster and when; the exact team-name form |
| G11 | undated | "Zoom meetings and discussions on the portfolio" (J:26) | Dates, who attended, what was decided |
| G12 | 5 Oct | Darren's challenge | Outcome and reasons |
| G13 | 5 Oct | The current Sheet created; the RAB tabs from 30 Sep inside it | What happened to the earlier Sheet, and who rebuilt it |
| G14 | 10-14 Oct | PM Dashboard created and left empty (11 Oct); notes copied 13 Oct; comments 13 Oct | What the dashboard was for; who wrote the 13 Oct comments; the "13 Oct V5 decision" |
| G15 | undated (before 14 Oct) | Tab 15 holds first-person Chinese edit notes from an AI tool no log records | Which tool, who used it, when |
| G16 | 16-18 Oct | AI says "At Ray's request", "accepted by the team", "Ray reviews all" | Who asked; who accepted v11 and made the cuts; who reviewed the v12 suggestions; whether any student objected |
| G17 | 18 Oct | No record of the planned meeting | Did it happen? What was decided? |
| G18 | 19 Oct | Judge's verdict reported; AI rule merged | Who spoke to the former judge, when, and what was shown and said; whether the team voted on the AI rule |
| G19 | whole period | School letter "not yet requested as of 13 Oct" (COMP:132) | The advisor's actual admin steps and dates |
| G20 | whole period | One time-zone story (row 50) | Other real experiences of working at night Sydney time, or across six schedules. Only what students remember |

---

## 5. (c) AI-use log rows this timeline implies (for the Works Cited)

Columns follow the AI-use log in AIU §5. "In log?" means whether main's `caplet/docs/AI_USE.md` already has a row.
"Who asked" and "Student decision" are left for students to fill unless a record names them; an AI file's "at Ray's
request" is quoted, not confirmed.

| # | Date (Sydney) | Tool | What the AI did | Output / where | Who asked (record) | In log? |
|---|---|---|---|---|---|---|
| L1 | Sat 19 Sep | Code-generation tool (UNVERIFIED which) | Built the generic "wharton-ic" platform (about 17k lines) with a demo client, invented rules (removed 27 Sep) and a false "100% student" disclosure | Commits `dd5755a`-`54bda02`; AIU:49 | not recorded | No. Also remove or banner AIU:49 |
| L2 | 24-25 Sep | Claude (Cowork) | Case reading, web research, mandate YAML, projection model, memos D1-D8, deliverable outlines | `caplet/decisions/`, `archive/model/laura/`, `caplet/deliverables/` | not recorded | Yes (AIU:86-90) |
| L3 | 26-27 Sep | Claude Code (cloud) | Ingested the case and instructions; verified market data; ran council rounds 1-2; ran the interview; wrote the Trading Notes blueprint and research prompts | 22 commits `d0dde73`-`ade6d06`; `keel/library/council_2026-09-27/` | not recorded | No |
| L4 | 27-29 Sep | Claude Code (multi-agent "insight_v1", about 90 agents) | Strategy research, final spec (REC), notes pack, IPS spec, 27-page client report, 831-page record; five files copied to Drive "AI Outputs" (28 Sep 18:30) | `keel/library/insight_v1/`; Drive AI Outputs | "scope set by Ray" (CM:84) | No |
| L5 | 28 Sep - 19 Oct | OpenAI Codex review bot; Serena MCP | Automated code reviews on PRs #1-5, #9, #11; tool server config | PR comments | not recorded | No |
| L6 | 29 Sep | Claude Code; ChatGPT (GPT-6 Astra) | Floor-size test; ladder re-pricing with an independent GPT check; past-winners research and self-scoresheet; IPS exemplars v3-v12 (plus v13 and v14 "Roots First" on Drive, not logged) | AIU:59-66; Drive AI Outputs | v3 "at the team leader's request" | Partly (v13 and v14 missing) |
| L7 | 29 Sep | unknown, possibly AI | Read the WInS Session Rules and listings into `wins_notes.csv` | Sheet tab "WInS Notes" | not recorded | No. Find out who did it |
| L8 | 30 Sep | Claude Code (RAB run, 8 workstreams) | Models, decision memos, tickets, 23 EXAMPLE notes, red teams; wrote two tabs into the team Sheet | AIU:67-76 | not recorded | Yes |
| L9 | 30 Sep - 1 Oct | Claude Code | Overnight repo review; 3-page brief before the first trades | `research/assistant_review_2026-10/03_...`, `02_...` | not recorded | No |
| L10 | 6 Oct | AI (tool UNVERIFIED) | "Desk review" of 33 trade notes with an AI-drafted note for each order | Sheet Trading Notes tab, columns R-U | not recorded | No |
| L11 | 6-7 Oct ET | AI browser agent (product UNVERIFIED) | Operated WInS screens (ticket filling "up to Preview"); one wrong cancellation (May-2038) | COMP:192-193 | not recorded | **No. Must be logged** (the WInS record shows the cancellation) |
| L12 | 6-7 Oct ET | (from L8 and L10) | The executed note wording draws on AI EXAMPLE and audit drafts (the VT note's last clause matches the exemplar word for word) | WN:14-24; `oct19/verify/verify_tna_judges_sheets.md:56` | - | **No. Needed for the TNA itself** |
| L13 | from 13 Oct | Claude scheduled routines (monitor, rules watcher, mock judges, evidence lab) on the team leader's machine | Twice-weekly checks; the 13 Oct baseline; planned mock-judge panels | `keel/routines/` | not recorded | No (whether they still run: UNVERIFIED) |
| L14 | 14 Oct | Claude Code | `competition/COMPETITION.md`, `caplet/START_HERE.md`, Drive exports, STRIPS banners | `44f1296` | not recorded | No |
| L15 | before 14 Oct (undated) | unknown AI tool(s) | IPS tabs V1-V4 and Tab 10 hold AI exemplar text (V1 "EXEMPLAR ONLY"); Tab 15 holds Chinese AI edit notes | IPS Doc; `oct19/verify/verify_ips_exemplars.md:62-66` | not recorded | No |
| L16 | 15-16 Oct and 19 Oct | Claude Code (this review series) | Review 30 Sep-15 Oct, 15 Oct brief, 16 Oct "What stops us winning" | PRs #6, #10 | not recorded | No (main's log jumps from 30 Sep to 18 Oct) |
| L17 | 16 Oct | Claude Code | IPS number sheet; 13 [AI] suggestions written into V5; [AI] tags removed; compliance suggestions | Branch `claude/fervent-edison-sqk1ry` | "Ray's 16 Oct rule", "At Ray's request" | Only on the unmerged branch (rows 77-79). Merge those rows |
| L18 | 16 Oct | Claude Code | North Star memo, pre-mortem, number checks | Branch `claude/dreamy-planck-0cvtxp` | "Ray's competition tips" | No |
| L19 | 17-18 Oct | Claude Code | 2031 range model; exemplar pitch, IPS and three TNA reflections, v1-v12; "AI tells"/StoryScope style study; harsh review; v12 written into the IPS Doc as suggestions (18 Oct 11:49) | Branch `claude/trusting-euler-gms43m`; IPS Doc | "Ray's request" | **No row anywhere** |
| L20 | 19 Oct | Claude Code | Research Office (26 to 18 agents), WO-0001, WO-0002 | `keel/office/`; AIU:77-78 | "the team leader's request" | Yes (WO-0002 only in the branch LEDGER) |
| L21 | 19-20 Oct | Claude Code (this review series) | 19 Oct update and kits, coupon study, co-sponsor research, questions for Wharton, this timeline; read-only Drive reads | `oct19/out/`, `oct20/` | not recorded | No |
| L22 | undated | Claude (artifact) | The "Research Summary" artifact linked at the top of ND | ND:12 | not recorded | No |

**Consistency check for the Works Cited:** every TNA reflection or IPS sentence that came from L6, L8, L10, L12, L15,
L17 or L19 is AI-generated work. The policy says such work "may not" be submitted as the students' own. Logging it
does not make it the students' work. Students rewriting from their own understanding is the only fix.

---

## 6. Checks run on this file

- **Time conversions** were done twice: once by `gitconv.py` from each commit's own offset, once by `conv.py` from the
  UTC or ET source.
  - Spot checks: IBTM 6 Oct 10:01 PM EDT = 7 Oct 02:01 UTC = Wed 7 Oct 13:01 AEDT; the journal edit at 06 Oct 23:28
    UTC = Wed 7 Oct 10:28 AEDT; the Team List at 20 Aug 02:26 UTC = Thu 20 Aug 12:26 AEST.
  - The DST switch (Sun 4 Oct) is applied: all September Sydney times are AEST.
- **Commit counts** (202 total; 97 Claude; 72 Ray identity with an AI trailer; 30 Ray identity without one; 3 by
  Harry-named accounts) come from `data/gitlog_all.txt`. They add up: 97 + 72 + 30 + 3 = 202.
- **Drive times** are from metadata read on 20 Oct. No Caplet file's `modifiedTime` has changed since the 19 Oct read.
- **Not checked:**
  - Drive version history (the connector cannot read it);
  - WInS Transaction History;
  - SMApply;
  - the school Gmail inbox (where Wharton mail goes);
  - the team leader's machine (`~/Research/caplet-monitor/`, the 6 Oct audit folder).
