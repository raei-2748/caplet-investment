# Repo revisit, 23 Oct 2026 (AI check, read-only on GitHub; nothing pushed)

Work clone: `oct23/repo/work`, branch `claude/dazzling-galileo-fx6bbm` (HEAD 640fd0f before the patch; patch commit
1b436c4). Patch: `oct23/repo/email_facts.patch` (1 commit, 6 files, +65 / -28). The live repo at
`/home/user/caplet-investment` was not touched (its `git status` is clean).
Tests in the clone: **64 passed**, 21 warnings (Python 3.12 venv at `oct23/repo/venv`; system python 3.11 is below
the package's `>=3.12` and has no pytest). The test run appended 8 lines to the tracked `outputs/ai_use_log.jsonl`;
that was reverted, so the clone holds only the patch commit.

## 1. What changed on GitHub since 20 Oct (f191d6e -> origin/main fb41d9b)

`main` moved by 37 commits (21-23 Oct), through PRs #12-#17, all merged; #17 last, 23 Oct 02:08 UTC:
- #12, #13, #9, #8 (consolidation, merged 22 Oct 22:52 UTC): office WO-0002 to WO-0005, the 2031 range model,
  the IPS/TNA blueprints, North Star memo. This branch (640fd0f) was also merged into main as part of #14.
- #14 (22 Oct): consolidates every branch, tidies the root (stray files into `archive/`, `rab/`), files the Wharton
  Week 4 email as `competition/official/2026_27/wharton_email_week4_2026-10.md`, gives deadlines in Sydney time
  first, changes the AI-use rule (commit 3e02d2e), and adds "Team Keel", a fictional mirror team of six personas.
- #15/#16 (22-23 Oct): rate checks to 22 Oct ("ladder cost crosses $300k; October rule did not fire"), an archive
  of branch history, fuller Keel profiles.
- #17 (23 Oct): **repo restructured** into five top folders: `keel/` (office, routines, library), `caplet/`
  (team exports, deliverables, decisions), `competition/`, `toolkit/` (src, tests, config), `archive/`. `office/`
  is now `keel/office/`, `ops/` is `keel/routines/`, `research/` is `keel/library/`, `team/` is `caplet/`.
- The GitHub repo is now **private** (API: `private=true`); main's CLAUDE.md says Ray made it private on 23 Oct.
- Branches on GitHub: main, this branch, `claude/admiring-curie-2qgurz`, `claude/stoic-planck-lih8tw`,
  `claude/zealous-turing-l19aqc`, `rab/ws4`-`rab/ws8`, `research/f1-floor-variants`. No open PRs.

What main already has from the emails: the IPS-as-a-form change (COMPETITION.md section 5, keel 2_IPS.md, CLAUDE.md)
and the TIPS/STRIPS ban, both sourced to the filed Week 4 email, whose header says "Exact send date: UNVERIFIED".
The emails give it: Mon 19 Oct 23:46 Sydney = 08:46 EDT. Main still has the **4:00 pm / Sat 08:00 freeze**,
"~Tue 10 Nov" for the FR instructions, no submit windows, no 7,300+ teams, no credential rule.

**The patch does not apply cleanly to main.** A test `git am -3` on fb41d9b handled the office -> keel/office
renames but conflicted in CLAUDE.md, COMPETITION.md, START_HERE.md and keel/office/workstreams/2_IPS.md (1_TNA and
3_FINAL_REPORT applied). Rebase it by hand onto main before any PR.

## 2. What the patch changes, line by line (new line numbers in the patched files)

Marking: each changed item ends with "(Wharton email, <ET send date>)". A wrapped item carries the mark once, at
its end. ET and Sydney send dates are the same day for every email cited except the 15 Sep SMApply invitation
(16 Sep Sydney).

**COMPETITION.md**
- 3-4: header says the marked lines were updated on 23 Oct from the emails of 15 Sep-19 Oct (ET dates).
- 15 (new): weekly emails on Mondays, also posted on WInS (28 Sep).
- 22 TNA row: submissions open Mon 12 Oct; no late submissions (24 Sep; 16 Oct).
- 23 freeze row: **4:00 pm -> 5:00 pm ET; Sydney 08:00 -> 09:00** (19 Oct).
- 24 IPS row: an SMApply form, not a PDF; open from Mon 26 Oct (24 Sep; 19 Oct).
- 25 FR instructions row: "Mon 9 Nov" -> "Mon 9 Nov, 9:00 am"; "~Tue 10 Nov" -> "Tue 10 Nov 01:00" (12 Oct; 19 Oct).
- 26 FR row: open from Mon 9 Nov (24 Sep).
- 31-32 (new): the freeze is one hour after the 4:00 pm close; orders after the close fill at the next open, so the
  last real-time fill is at the close (marked as inference).
- 43: "not scored" list adds beating other teams (12 Oct).
- 50-51 (new): participation credential only with all requirements and all deliverables (28 Sep); "more than 7,300
  teams this year" (28 Sep).
- 57-58: client contact quoted as "Teams are not permitted to contact the client" (12 Oct); unclear points go to
  the advisor (19 Oct).
- 84 trading window: 6 Nov 4:00 pm -> 5:00 pm ET (19 Oct).
- 88 allowed: Week 1 still said >= $5; Week 4 says "Any stock available on WInS", no floor (28 Sep; 19 Oct).
- 89 bonds: fixes the old claim that "the 6 Oct email says US Treasuries". Week 1/4 say "Any Government/Treasury
  Bond available on WInS", Week 2 "Treasury bonds available on WInS"; only the session rules say US (28 Sep; 5 Oct; 19 Oct).
- 90 banned: TIPS/STRIPS also sourced to the Week 4 email (19 Oct).
- 99-101: the Week 2 email was sent **Mon 5 Oct** (ET and Sydney), not 6 Oct; adds its "may not recommend or assume
  investments ... outside the approved competition universe" (5 Oct).
- 111-112 (new): the Week 4 email repeats the permitted list ("for BOTH contributions, the IPS and Final Report")
  and the NOT-permitted list (19 Oct).
- 132-133 (new): TNA opened 12 Oct; "We will not accept any late submissions" (24 Sep; 16 Oct).
- 144-147: replaces "TNR 12 ... PDF <= 5 MB, via SMApply" with: IPS is an SMApply form, "You will not submit a
  PDF. All other requirements remain the same."; the instruction's font/spacing/margins/PDF rules (`:112-122`) may
  not apply as written; how the title page and two-page limit are entered is UNVERIFIED; open from Mon 26 Oct (24 Sep; 19 Oct).
- 155-156: FR instructions Mon 9 Nov 9:00 am ET = Tue 10 Nov 01:00 Sydney; submissions open 9 Nov (24 Sep; 19 Oct).
- 158 (new): "Be sure to document your research, decision-making, and reasoning throughout the competition." (5 Oct)
- 167-168 (new): team leaders are final (28 Sep); no members added; a removal needs the advisor's written request
  and Wharton's approval, or the team is disqualified (12 Oct).
- 261 (new, sources table): the emails as a source, not filed on this branch; SMApply is "the primary source for
  essential competition information" (15 Sep; 28 Sep).

**START_HERE.md**
- 30 (new): never contact the client; case questions go to the advisor (12 Oct; 19 Oct).
- 60: IPS + freeze now "Sat 7 Nov 09:00 Sydney (Fri 6 Nov 5 pm ET)"; IPS a form, open from 26 Oct (24 Sep; 19 Oct).
- 61 (new): FR instructions Tue 10 Nov 01:00 Sydney (Mon 9 Nov 9 am ET) (19 Oct).
- 63 (new): weekly emails on Mondays (ET), also on WInS (28 Sep).

**CLAUDE.md** (deadlines paragraph only, lines 85-91): TNA open from Oct 12; IPS an SMApply form, open from Oct 26;
TNR 12 double-spaced may not apply to a form (UNVERIFIED); trading ends 5:00 p.m. ET = Sat 7 Nov 09:00 Sydney; FR
instructions Mon Nov 9, 9:00 a.m. ET = Tue 10 Nov 01:00 Sydney; FR + school documentation open from Nov 9;
participation credential rule; weekly emails on Mondays, also on WInS. Each item marked.

**office/workstreams/1_TNA.md**
- 17-18 (new): TNA opened 12 Oct; "We will not accept any late submissions." (24 Sep; 16 Oct)

**office/workstreams/2_IPS.md**
- 3: adds "Submissions open Mon 26 Oct" (24 Sep).
- 4-5: freeze "4:00 pm ET close, probably about Sat 08:00 (an inference)" -> 5:00 pm ET = Sat 7 Nov 09:00 Sydney,
  portfolio final (19 Oct); the 4:00 pm close kept as the last real-time fill (inference).
- 17-20: format line replaced by the Week 4 quote (form, no PDF, all other requirements the same); the PDF-era
  format rules (`:112-122`) may not apply; title page and two-page limit UNVERIFIED until the form opens (19 Oct).
- 47 (Wed 4 Nov row): "Format check on the exported PDF, on Letter paper" -> check of the plain text for the form (19 Oct).
- 59 (gate): "The PDF fits ... 5 MB or less" -> text fits the form's fields and limits; page/paper checks only if
  the form still asks; no graphics, links, footnotes or citations (19 Oct).

**office/workstreams/3_FINAL_REPORT.md**
- 4: instructions Mon 9 Nov 9:00 am ET = Tue 10 Nov 01:00 Sydney; submissions open 9 Nov (24 Sep; 19 Oct).
- 20-22 (new): participation credential needs all deliverables, so the school documentation is required too
  (28 Sep); the "document your research, decision-making, and reasoning" quote (5 Oct).
- 42 (Tue 10 Nov row): "Instructions posted 01:00 Sydney" (19 Oct).

No file under `team/google_drive/` or `deliverables/` was touched. No name, email or ID was added.

## 3. Other inconsistencies with the emails, found but not fixed

1. **WInS username in plain text.** `ops/routines/MONITOR.md:33` and `ops/routines/WATCHER.md` contain the team
   username with the 8-digit number. Main still has it in `keel/routines/tasks/MONITOR.md` and `WATCHER.md`
   (`git grep` hit count: 2 files on each). COMPETITION.md says the username is kept out of the repo. The emails
   say the same number is shared by the school's teams. Redact it, and check git history if it matters.
2. **Old freeze time (4:00 pm ET / Sat 08:00) in 37 files**, e.g. `ops/routines/MONITOR.md:17`,
   `research/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md:113,199`,
   `.../oct20/compliance/compliance_matrix.md:50`, `.../oct20/ops/operating_plan.md:38`,
   `.../oct20/tradecheck/trade_check_pack.md:543` ("Any order still open never fills"), and main's
   COMPETITION.md:21,76 and keel 2_IPS.md:4. The 4:00 pm close is still the last fill time; the freeze is 5:00 pm.
3. **IPS as a PDF** is still assumed in `ops/routines/MONITOR.md:17` ("PDF <= 5 MB"),
   `.claude/agents/format-gatekeeper.md:21` (page, TNR 12, Letter, PDF <= 5 MB),
   `config/wharton_private_2026_27.yaml:133` (`file: "PDF", max_file_mb: 5`), and main's keel 2_IPS.md:46,58.
4. **"6 Oct email"**: about 150 files cite the Week 2 email as 6 Oct (e.g. CLAUDE.md:23, `office/CHARTER.md:34`,
   `config/wharton_private_2026_27.yaml:81`, `config/competition.yaml`, `.claude/agents/scenario-modeller.md:13`,
   many `rab/` and `decisions/` files). It was sent Mon 5 Oct (08:07 EDT = 23:07 Sydney). Only COMPETITION.md was fixed.
5. **"US Treasuries" vs the email wording**: `office/CHARTER.md:34` says only "US Treasuries" may be assumed (citing
   the 6 Oct email). The emails say "Treasury bonds" (Week 2) and "Government/Treasury Bond available on WInS"
   (Weeks 1 and 4). Only the WInS session rules say US.
6. **FR instructions time**: `config/wharton_private_2026_27.yaml:140` and `config/wharton_public_2026_27.yaml:40`
   hold the date only. Several `research/assistant_review_2026-10/` files say "Mon 9 Nov ET" or "about Tue 10 Nov";
   the time is 9:00 am ET = Tue 10 Nov 01:00 Sydney.
7. **Public/private**: this branch's CLAUDE.md, START_HERE.md and COMPETITION.md still say the repo is public. GitHub
   says it is private. This is not an email fact, so it was not changed.
8. **CLAUDE.md "Last updated: 2026-10-20"** and COMPETITION.md section 9 "(as of 14 Oct)" were left as they were.
   The CLAUDE.md rule asks for the date to be bumped, but the task limited CLAUDE.md edits to the deadlines paragraph.
9. **Tests write to a tracked file**: `pytest` appends to `outputs/ai_use_log.jsonl`. CLAUDE.md says demo runs write
   only to git-ignored `outputs/demo/` and `decisions/demo/`.
10. **Week 4 send date** on main: `wharton_email_week4_2026-10.md` says "Exact send date: UNVERIFIED (received by
    22 Oct)". From the emails it was Mon 19 Oct 23:46 Sydney (08:46 EDT).
11. No repo file mentions the IPS opening date (Mon 26 Oct), the 7,300+ teams figure or the credential rule outside
    this patch. The 2025-26 figure "6,300+ teams" (CLAUDE.md:171) is last year's and is correct as stated.
