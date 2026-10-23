# Exposure audit: what Team Caplet has public right now (Tue 20 Oct 2026, 08:50 Sydney)

> **Verified 20 Oct (`oct20/verify_tl_exp/verify_tl_exp.md`): facts confirmed; clean-up plan needs fixes.** (X1, HIGH) While the fork is public, EVERY commit in the network - including the exemplar branch and the commit carrying the client's contact details - can be fetched through the fork by SHA (tested anonymously): delete the fork first. (X2) "Untick Allow forking" does not exist for a personal-account repo; forks of a private repo stay private. (X4) On GitHub Free, Traffic disappears once private - screenshot it first. (X5) `--replace-text` cannot clean the 5 exemplar .docx files (binary): drop them by path. (X6) BFG protects HEAD (commit deletions first or use --no-blob-protection). (X8, HIGH for the TNA) The "reassuring check" is wrong: the VT and Nov-2040 notes each hold a 13-word verbatim clause from the public 30 Sep AI EXAMPLE notes - disclose if picked (VT is a suggested pick). Client contact blob reachable from 19 of 22 upstream and 16 of 19 fork branches. Stars are erased on going private. 3 text files on main + 2 on other branches hold the WInS username.


AI-generated research for the team (Claude Code). Not for submission. Locations only: this file contains no surnames, emails, WInS username or account number, phone numbers or birthdays. First names only.

## 0. Summary

1. **Everything is still public, in two places.** The repo `raei-2748/caplet-investment` is `"private": false`, with 22 branches, 16 pull-request refs and 208 commits. Its one fork is also `"private": false`. It has 19 branches: 17 of the main repo's 22 (all except the five newest `claude/*` branches, so not the exemplar branch) plus two that the main repo no longer lists. Its `main` stops at 16 Oct, and it was last pushed 18 Oct 22:41 UTC. Checked with the GitHub API on 19 Oct 21:40 UTC. The fork holds no commit that is not also in the main repo (0 fork-only commits). Deleting it loses nothing.
2. **The worst AI-authorship evidence is a measurable match.** The live Google Doc "Trading Note Reflection" tab, unchanged since 18 Oct 00:49 UTC, holds the three reflections tagged `[AI]`. In each, about half the text matches word for word a dated, public AI file on branch `claude/trusting-euler-gms43m`: 47-63% of 12-word runs. Each live cell shows two wordings run together, so in effect one complete wording per reflection is the public AI exemplar. Wharton's AI policy says: "Don't use AI for personal reflection or opinion-based tasks."
3. **New personal data found since the 15-16 Oct checks.** (a) A team member's personal email, and in one commit their full name, sits in the author fields of 3 commits on `main`. Anyone can read these through the API or by adding `.patch` to a commit URL. (b) An old blob in history holds the real client's personal phone number and personal email, scraped from her website. (c) The known items are still there: the WInS username in 4 text files, 5 .docx, 2 PDFs, the .xlsx, a PDF file name and the git history; a school email inside a file path; the .xlsx "last modified by" full name and school OneDrive path.
4. **Search engines: no hit found, but the test was weak.** Bing (HTML and RSS) ignored `site:` and quote operators from this network, even on a control query, and DuckDuckGo returned a bot check. The Wayback Machine has no snapshot of either repo and Software Heritage has no record of either. Whether the repo is indexed is UNVERIFIED. GitHub's own search is the likelier way in: the team found three past teams' repos that way (`toolkit/docs/THIRD_PARTY.md:35-37`).
5. **The fix order matters.** First save the traffic data and a private backup. Then Harry deletes the fork, and only after that does Ray make the repo private. GitHub: "A public repository is deleted: An active public fork becomes the new upstream", and "A public repository is made private: Its public forks stay public". Do not rewrite history to remove AI evidence. It is the team's dated provenance, and deleting it would read as concealment. Rewrite history only for personal data, and only if the repo will ever be public again.

---

## 1. What was checked (and how)

| Check | Method | Result |
|---|---|---|
| Visibility, forks, branches, PRs, comments, wiki, releases, Actions, stars | `gh api repos/raei-2748/caplet-investment{,/forks,/branches,/pulls?state=all,/issues/comments,/pulls/comments,/releases,/actions/runs,/stargazers}`, 19 Oct 21:40 UTC | Public; description names the school; `allow_forking: true`; 1 fork; 1 star (starred 30 Sep); 12 PRs (4 open: #7, #8, #9, #12); 7 issue comments and 4 review comments, all from an OpenAI Codex review bot except one reply from the repo owner; no wiki repo, releases, Actions runs or Pages |
| Fork | `git ls-remote` + full fetch of the fork (anonymous; the session's API access to it is blocked) | Public; 19 branches, including `docs/assistant-review-2026-10` and `docs/assistant-review-2026-10-16`, which the main repo no longer lists; it lacks the five newest `claude/*` branches; fork `main` = 6144dd7 (16 Oct), which already includes the username files, the .docx exemplars and the humanise tabs |
| Every file ever committed | Bare mirror of all upstream branches, all `refs/pull/*` and all fork branches (`oct20/exposure/work/mirror.git`); 1,793 unique blobs dumped and scanned (`oct20/exposure/scripts/dump_blobs.py`, `bin_scan.py`) | 1,460 distinct paths in history; 1,191 files on `main` (66 MB) |
| Office/PDF metadata | Unzipped .docx/.xlsx core and workbook XML; PDF metadata and text (pypdf) | See section 2 |
| Commit metadata | `git log --all --format='%an|%ae|%cn|%ce'` | 6 identities; one is a personal Gmail; see 2.2 |
| Live Drive vs public files | Drive `get_file_metadata` (read-only) on the IPS Report; 6-, 8- and 12-word overlap (`oct20/exposure/scripts/overlap.py`) between the 19 Oct verbatim copy (`oct19/drive/ips_report_live.md`) and the public exemplar | IPS Report `modifiedTime` 2026-10-18T00:49:32Z, unchanged since the 19 Oct copy; see 3.1 |
| Google links in the repo | Anonymous `curl` of all 14 Doc/Sheet IDs found on any branch | 11 return 401 (restricted); 3 of last year's files return 200 (open to anyone with the link); see 2.6 |
| Search and archives | Bing HTML + RSS (17 queries + control), DuckDuckGo HTML, Wayback availability API, Software Heritage origin API | No hits; Bing operators not honoured (control failed); DDG returned "anomaly"; Wayback `archived_snapshots: {}` for both repos; Software Heritage "Origin ... not found" for both |
| Not checkable from here | Repo traffic (views, clones, referrers): API 403. Collaborator list: proxy 403. GitHub search: blocked | Owner must look in Insights > Traffic (step 1 below) |

---

## 2. Personal data (locations only)

Status codes: **MAIN** = in the current `main` (and so in the fork); **BR** = only on other branches; **HIST** = only in older commits, still reachable through the history of every branch.

### 2.1 WInS username / account number

| Location | Status |
|---|---|
| `COMPETITION.md:3`, `:117` | MAIN, fork, every branch since 14 Oct |
| `keel/routines/tasks/MONITOR.md:33`, `keel/routines/tasks/WATCHER.md:13` | MAIN |
| `keel/library/blueprints/06_ips_wharton_compliance_17Oct.md:14` | BR (`claude/trusting-euler-gms43m`) |
| `archive/rab/trades/data/ips_doc_text_2026-09-30.txt:14` | BR (`rab/ws6`, `wip/ws7-stash-2026-09-30`) |
| The **file names** `caplet/ips_drafts/Caplet-<number>_IPS_2026-09-30{,_v2}.pdf`, plus page-1 text | MAIN |
| All 5 `caplet/ai_outputs/IPS Exemplar v3/v7/v12/v13/v14 (AI, not for submission).docx`, in `word/document.xml` (title page) | MAIN |
| `caplet/Portfolio_and_Trading_Notes_snapshot.xlsx`: `xl/sharedStrings.xml` (2 hits), `xl/comments4.xml` | MAIN |
| The 15 Oct brief, which lists every location above in one place (`keel/library/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md:518-548`) | MAIN |

The username is not secret by itself, since it goes on the IPS title page. But it is half of the login for a shared account that trades until 6 Nov, and only Ray may place orders (CLAUDE.md, 7 Oct mis-click).

### 2.2 Emails and full names

| What | Location | Status |
|---|---|---|
| **Personal Gmail of the fork owner, in commit author/committer fields** | commits cf43a9d (16 Oct), 0ad520b (19 Oct), and e5322d3 (merge of PR #10, which also carries the **full name with surname**) | MAIN (in `main`'s history), fork, PR refs #6-#12. **New.** Readable via `api.github.com/repos/.../commits/<sha>` or `github.com/.../commit/<sha>.patch` |
| A student's school email, written with dashes inside a cloud-drive path | `archive/rab/rescued/r4_hist_original.py:6` (also contains a `/Users/<first name>` path) | MAIN |
| Full name in "Surname, First" form | `caplet/Portfolio_and_Trading_Notes_snapshot.xlsx` → `docProps/core.xml` `cp:lastModifiedBy` | MAIN |
| School OneDrive personal URL (encodes a school account) | same .xlsx → `xl/workbook.xml` `absPath` | MAIN |
| Google account display names (first name + surname initial) of 4 people, including one who is not one of the six students | Comment lists in `caplet/google_drive/ips_report/01_version_5.md:36`, `02_v4_need_to_humanise.md:36`, other `caplet/google_drive/*.md` exports | MAIN |
| 15 students from the school's three other teams (first name + surname initial) | `caplet/google_drive/team_list.md:32-51` | MAIN |
| People outside the team named in last year's doc comments | `caplet/google_drive/2025_knox_wharton.md` (e.g. comment list near :3816-3846) | MAIN |
| The repo description names the school; the school is named in many tracked files | repo metadata; e.g. `COMPETITION.md:3` | MAIN |

No literal student email address, phone number, birthday, signature, school letter or roster screenshot was found in any of the 1,793 blobs. The only images are 47 charts. The emails in `.env.example`, `toolkit/config/data.yaml` and `toolkit/pyproject.toml` are placeholders. No API keys or tokens were found; the five regex hits are URL fragments.

### 2.3 The real client's personal contact details (new)

- An old version of `keel/library/insight_v1/phase_D/_work/D13a_contexts.json` (blob 86a99ee, added in be64a94 and replaced in 9e8bbdb, both 27 Sep) contains **Laura Gao's personal phone number and personal email** (2 instances), scraped from her personal website. **Status: HIST.** It is reachable from every branch, including `main` and the fork. The current version on `main` does not have them.
- Why it matters: she is a real person, and "Teams may not contact the Competition client. Teams that violate this rule will be disqualified" (Rules & Roles, live 19 Oct). Holding her contact details is not contact. But a public file of them, next to a detailed public profile of her (`research/insight_v1/phase_B/B3a/B3b_lauras_world.md`, `B8a/B8b_voice_of_laura.md`, `phase_A/stakeholder_map.md`), is a bad look and puts temptation one click away.
- `keel/library/insight_v1/phase_D/_work/D13b_contexts.json:447, :501` contain an organisation's phone number (a third party, low risk). MAIN.

### 2.4 Unrelated personal material

- `aussef_complete_experiment_record.pdf` (repo root, added 29 Sep in 2b9376c) is a 12-page record of the team leader's unrelated research project. Its metadata Author is a first name, its pages carry `/Users/<first name>/Research/...` paths, and it names the adult it was "Prepared for". MAIN. It has no link to the competition. Remove it.

### 2.5 Credentials

`caplet/google_drive/2025_knox_wharton.md`: the WInS username/password cells for last year are `[removed]` (:80, :282, :400, :3111-3113). There is only one version of this file in history (44f1296), so no earlier unredacted copy exists. It still contains a working ChatGPT share link (:3805).

### 2.6 Google files open to anyone with the link (linked from the public repo)

| File (by title) | Link location | Anonymous status 19 Oct |
|---|---|---|
| "Copy of Wharton Investment Competition '25 - GREENOX" (Doc) | `2025_knox_wharton.md:3418` | **200, readable.** Its text has 18 "username" and 6 "password" mentions and 4 email addresses at another school's domain (values not read) |
| "Final Report. Gambler" (Doc) | `:3351` | 200 |
| "Greenox Matrix Stock Tracker" (Sheet) | `:757`, `:2126` | 200 |
| This year's IPS Report, Notes & Discussions, Portfolio sheet, PM Dashboard, team list and 6 other Docs | various | 401 (restricted). Good, but the repo publishes their IDs. If anyone switches one to "Anyone with the link", it is public at once |

Who owns the three open files is UNVERIFIED. "Copy of ..." suggests a Knox account copied another school's document.

---

## 3. AI-authorship evidence a forensic reviewer would find

Wharton (Rules & Roles, live 19 Oct): "AI-generated work may not be submitted as your own"; "reserves the right to engage ... forensic analysts". AI policy page: "they must use their voice and words"; "Don't use AI for personal reflection or opinion-based tasks." These are reasons to make the work honest. They are not reasons to hide it. Nothing below should be deleted to avoid detection (see section 5, rule R1).

### 3.1 Exemplar reflections for the exact three notes (highest risk)

- **Public file:** `keel/library/blueprints/04_exemplar_ips_tna_17Oct.md` (1,550 words; branch `claude/trusting-euler-gms43m`, open PR #9 "...and AI exemplar"). Sections ":50 VT 10/07/2026 08:27:19 PM ET", ":54 IBTR 10/07/2026 04:42:53 AM ET", ":58 IBTM 10/06/2026 10:01:41 PM ET" are full reflections for the three notes the team picked. There are 12 dated versions in commit history: 87ba928 → 1ed9130, 17-18 Oct, with messages such as "Exemplar v8: full StoryScope-informed rewrite of IPS and IBTR".
- **Reflection outlines** for the same three orders: `keel/library/blueprints/03_tna_reflection_outlines_17Oct.md:19, :36, :53` (same branch).
- **Match to the live Doc (new measurement).** IPS Report, tab "Trading Note Reflection" (Drive `modifiedTime` 2026-10-18T00:49:32Z), share of word runs found word for word in the public exemplar:

| Reflection | Words in cell (two wordings run together) | 6-word runs | 8-word runs | 12-word runs |
|---|---|---|---|---|
| VT | 180 | 60% | 56% | 51% |
| IBTR | 189 | 54% | 51% | 47% |
| IBTM | 177 | 73% | 69% | 63% |
| IPS "Version 5" tab (vs exemplar IPS section) | 1,065 | 55% | 52% | 46% |

  All three cells start with `\[AI\]`. The Drive tool shows pending suggestions as inserted and deleted text together, so about half of each cell is the public exemplar verbatim. Which half is the accepted text cannot be told from the API. The 19 Oct verify notes say the first run matches exemplar v12 word for word (`oct19/drive/ips_report_live.md:7-12`). If either wording reaches SMApply, a reviewer with the public file can prove a dated AI origin in minutes.
- **Reassuring check.** The three **WInS trade notes** themselves (the text the TNA must quote) are **not** copies of the AI "EXAMPLE" notes. Their best match in any non-export public file is 14% of 8-word runs (`archive/rab/trades/notes.md`, `trading_notes.csv`). The 100% matches are only the team's own exports and outlines of those notes.

### 3.2 "Humanise", style study and detector work

- `caplet/google_drive/ips_report/02_v4_need_to_humanise.md` and `03_v4_need_to_humanise_notes.md`: the tab names, plus the comments "This page is for us to humanise V3" and "Best version that AI generated; We cannot submit as it is..." (`01_version_5.md:36`), each with a display name. MAIN.
- `keel/library/blueprints/07_style_study_17Oct.md` (`claude/trusting-euler-gms43m`): ":30 Why the earlier exemplar read as AI", ":31 | AI tell | Example from v5 | v6 |", ":47 What the StoryScope paper adds", ":58 Surface edits barely move detection", ":68 v8: the paper's findings applied to the whole text". `09_house_style_17Oct.md` (same branch).
- `caplet/docs/AI_USE.md:65` (MAIN): "Rewrote the exemplar IPS to remove AI-style patterns (measured with a script ...)".
- `keel/office/tools/textcheck.py` and `keel/office/workstreams/*.md` (MAIN) are a text checker and AI desk rules. `.claude/agents/*.md` (18 agent personas, MAIN).
- Our own reviews are public and point straight at all of this. `keel/library/assistant_review_2026-10/oct16/lenses/L09_integrity_compliance.md` lists the INT-01 AI rewrites and the INT-06 "AI-detector and 'remove AI-style patterns' testing" with file paths. `01_Caplet_Team_Brief_15Oct2026.md:518-548` maps the personal data. Both are on MAIN, so they are a ready index for a reviewer or a rival.

### 3.3 Commit and log trail

- 176 of the 208 upstream commits carry "Co-Authored-By: Claude", and 104 link a claude.ai session. Since 16 Oct, Claude authored 30 of 35 commits.
- AI_USE gaps (MAIN `caplet/docs/AI_USE.md`): the dated rows run 24-30 Sep, then jump to one row each on 18 and 19 Oct. Not logged: exemplars v1-v12 (17-18 Oct), the style study, the [AI] Doc suggestions and the Tab 15 edit (confirmed in `oct19/verify/verify_ips_exemplars.md:59-61`). Also not logged, and new: the **OpenAI Codex review bot**, which reviewed PRs #1-#5, #9 and #11 (10 bot comments, 28 Sep-18 Oct). `caplet/docs/AI_USE.md` never mentions Codex. The 16 Oct rows exist only on the unmerged `claude/fervent-edison-sqk1ry` branch.
- `caplet/docs/AI_USE.md:49` still holds a quoted "100% by students"-style claim that the 16 Oct review called false. MAIN.
- Last year's doc (`caplet/google_drive/2025_knox_wharton.md`) holds comments about making up stories. Wharton's ethics text bans "invent teamwork and experiential stories". It is the same school and team leader, and it is public.

---

## 4. Strategy material a rival could copy, and conflicts with the rules

### 4.1 Copyable now (before the 6 Nov IPS and trading freeze)

| Material | Where (MAIN unless noted) | Size |
|---|---|---|
| Full plan, numbers and decisions | `COMPETITION.md`, `START_HERE.md`, `keel/library/insight_v1/phase_E/E6_final_spec.md`, `ips_spec.md`, `trading_notes_pack.md` | 2,600 + 572 + 13,918 + 8,008 + 5,078 words |
| 27-page strategy brief and 831-page research record | `keel/library/insight_v1/Team_Caplet_Strategy_Brief.pdf`, `Team_Caplet_insight_v1_research_record.pdf`; root `Laura_Gao_Strategy_Brief.pdf` | PDFs |
| The team's IPS drafts V1-V5 and reflections | `caplet/google_drive/ips_report/*.md` (14 Oct export), `caplet/ips_drafts/*.pdf`, `caplet/ai_outputs/*.docx` | |
| Holdings and every order | `caplet/google_drive/sheets/portfolio_and_trading_notes/trade_log.csv`, `.xlsx` | |
| Models | `archive/rab/` (working paper, M1-M8), `keel/library/range_2031/` (PR #9 branch) | |
| Judge-style critique and past-winner research | `keel/office/outbox/2026-10-19_WO-0002_judging_ips-v5-why-not-semifinal.md` (PR #12 branch), `keel/library/assistant_review_2026-10/oct16/research/KB_what_wins.md` (8,898 words), `04_What_Stops_Us_Winning_16Oct2026.md` (16,027 words) | |

Who could find it: the school's three other teams, named in `team_list.md`, and any team that searches GitHub, as this team did for past repos (`toolkit/docs/benchmark_against_previous_teams.md:13-36`, which also grades named students' public repos by school). Copied trades do Caplet little harm, since judging is on the written work. The real cost is (a) a rival taking the "promise a floor, show the upside" 2031 idea into its own IPS, and (b) any similarity check that pairs a rival's text with Caplet's. The dated history would show Caplet came first, which is another reason to keep it.

### 4.2 Conflicts with Wharton rules

| Item | Rule text (Rules & Roles / AI policy, live 19 Oct) | Status |
|---|---|---|
| AI exemplar reflections + `[AI]` text in the live reflection cells | "AI-generated work may not be submitted as your own"; "Don't use AI for personal reflection or opinion-based tasks" | **Not yet a breach** (nothing submitted). It becomes one if submitted. TNA is due Fri 23 Oct 5 pm ET |
| Style study / "remove AI-style patterns" | "Don't use AI to paraphrase or rewrite plagiarized content"; ethics: forensic analysts | Looks like evasion; not a rule breach by itself |
| Public posting in general | FAQ: "Create a social media profile ... tag us in posts" (`smapply_public_2026-10-14/faqs.txt:92`) | **Allowed.** Publishing a repo is not banned |
| Presentations | "Video recording, audio recording, photography, screenshots, or posting presentations or participants online during the Semifinals or Global Finale is strictly prohibited" | **No breach now** (no slides, videos or recordings in any branch). It becomes one if semifinal decks, recordings or screenshots are ever committed or posted |
| Republishing registered-team materials | The repo's own manifest marks the client profile, IPS and TNA instruction PDFs `OFFICIAL_PRIVATE_VERIFIED` (`competition/official/2026_27/manifest.yaml`); `toolkit/config/wharton_private_2026_27.yaml` is headed "Official Private Registered-Team Materials" | No explicit rule found. Whether these PDFs are public elsewhere is UNVERIFIED. Appearance risk only |
| Client research | "Teams may not contact the Competition client" | Not contact; see 2.3 |
| Third-party AI on the repo | AI must be cited | Codex bot use is uncited (3.3) |

---

## 5. Clean-up plan (in order)

Ground rules:
- **R1.** Do not delete or rewrite the AI record (exemplars, style study, office, AI_USE, commit trailers) to avoid detection. It is the team's dated proof of what AI did and what the students did. Make the repo private for privacy and rival reasons only, and disclose AI use honestly in the Works Cited.
- **R2.** Rewrite history only for personal data (2.1-2.4), and only if the repo will ever be public again or shared beyond the six students and the advisor.
- **R3.** Assistants (including Claude Code) do not change Drive, Docs or GitHub settings. These steps are for named students.

| # | When | Owner | Action | Why / detail |
|---|---|---|---|---|
| 1 | Tue 20 Oct, before step 3 | **Ray** (repo owner) | Screenshot **Insights > Traffic** (views, unique visitors, clones, referring sites, popular content; GitHub keeps 14 days) and Insights > Forks. Save to the restricted team Drive | This is the only evidence of whether outsiders visited or cloned, and whether visits came from Google or Bing. Visibility changes can affect it. The API refused this session (403) |
| 2 | Tue 20 Oct | **Ray** | Make a private, complete backup: `git clone --mirror https://github.com/raei-2748/caplet-investment caplet.git && git -C caplet.git bundle create ../caplet_2026-10-20.bundle --all`. Store it in the restricted team Drive | Keeps the dated record (R1) and the PR refs before anything else changes |
| 3 | Tue 20 Oct | **Harry** (fork owner) | Delete the fork: fork > Settings > General > Danger Zone > **Delete this repository**. Already verified: 0 fork-only commits; its two extra branches are merged into `main` (PRs #6, #10) | If the parent went private first, GitHub says public forks "stay public in a separate network"; if the parent were deleted, the fork "becomes the new upstream". Deleting the fork first avoids both |
| 4 | Tue 20 Oct, right after 3 | **Ray** | Settings > Collaborators: add the five other students (write access). Then Settings > General > Danger Zone > **Change visibility > Private**. Untick "Allow forking" (currently `true`) | Private hides files, branches, history, PRs and comments. Stars and watchers are affected. Teammates lose fork-based PRs, so they push branches directly |
| 5 | Tue 20 Oct | **Ray** | Settings > Integrations (GitHub Apps): review which apps can read the repo (the OpenAI Codex connector reviewed PRs; Claude's app runs sessions). Remove any not needed | Fewer third-party copies; any kept app's use gets logged (step 8) |
| 6 | Tue 20 Oct | **Harry** | GitHub > Settings > Emails: tick **"Keep my email addresses private"** and **"Block command line pushes that expose my email"**; set `git config --global user.email` to the GitHub noreply address | Stops the personal email reaching new commits. Old commits stay as they are unless step 10 is done |
| 7 | By Wed 21 Oct | **Privacy lead (not Ray)** + one checker | Ordinary commits in the now-private repo. Remove `aussef_complete_experiment_record.pdf`; remove `caplet/ips_drafts/*.pdf` and `caplet/Portfolio_and_Trading_Notes_snapshot.xlsx`; replace the username in `COMPETITION.md:3, :117`, `keel/routines/tasks/MONITOR.md:33`, `WATCHER.md:13` with a pointer to the private Drive note (and re-point the MONITOR check); blank the path in `archive/rab/rescued/r4_hist_original.py:6`; leave the AI exemplar .docx in place but note in `caplet/ai_outputs/README` that their title page shows the username | Cleans the current tree. Does not touch history (R2) |
| 8 | By Sun 25 Oct | **Historian / AI-log keeper**; each student checks their own rows | Back-fill `caplet/docs/AI_USE.md`: exemplars v1-v12 and the style study (17-18 Oct), the [AI] Doc suggestions, the Tab 15 edit, the Codex PR reviews (28 Sep-18 Oct), and the 16 Oct rows from `claude/fervent-edison-sqk1ry:caplet/docs/AI_USE.md:77-79`. Banner or remove the false line at `:49` | The Works Cited must be true and complete (Rules & Roles: "AI-generated material ... must be properly cited") |
| 9 | **Before the TNA (Fri 23 Oct 5 pm ET)**, not an exposure step but the reason exposure matters | **The three reflection writers** | Students write each reflection fresh from their own outline, with the exemplar and the `[AI]` cells closed. Reject or delete the `[AI]` suggestions in the Doc yourselves (R3). Two students check that no 12-word run matches `04_exemplar_ips_tna_17Oct.md` (the overlap script at `oct20/exposure/scripts/overlap.py` can be pointed at a student draft) | 47-63% of 12-word runs in today's cells are the public AI text. This step removes the breach risk. Making the repo private does not, because clones and the team's own record keep the exemplar |
| 10 | Optional; decide by Sun 25 Oct | **Ray** + privacy lead | Only if R2 applies: history rewrite for personal data, done in a fresh mirror clone (see 5.1). Then open a GitHub Support ticket to purge PR refs and cached views. Then every student and every Claude Code environment deletes old clones and re-clones | GitHub: "If you only rewrite your history and force push it, the commits with sensitive data may still be accessible ... in any clones or forks ... in cached views ... through any pull requests". Support "will only assist in the removal of sensitive data". A personal email and a client phone number may qualify; ordinary files will not |
| 11 | Tue 20 Oct | **Whoever owns them** (UNVERIFIED; check Drive "Owner") | Set the three open 2025 Google files (2.6) to Restricted | They hold another school's emails and credential mentions, and are linked from the repo |
| 12 | Ongoing | **Everyone** | Never commit or post: semifinal or finale slides, recordings or screenshots (Recording Policy); the school letter; the roster; the final IPS PDF; surnames or emails | Rules & Roles "Recording Policy"; CLAUDE.md working rules |
| 13 | If a search hit ever appears | **Privacy lead** | After the repo is private (GitHub then returns 404), use Google Search Console "Remove outdated content" and Bing Webmaster "Content Removal Tool" for the URL | No hit found today, but the test was weak (section 1) |

### 5.1 If step 10 goes ahead: how (git filter-repo; BFG as an alternative)

Do this in a throw-away mirror clone, never in a teammate's working copy. Keep the step-2 bundle as the untouched record.

```
# needs git-filter-repo >= 2.47 (for --sensitive-data-removal)
git clone --mirror https://github.com/raei-2748/caplet-investment caplet-clean.git && cd caplet-clean.git

# 1. Drop whole files from all history
git filter-repo --sensitive-data-removal --invert-paths \
  --path aussef_complete_experiment_record.pdf \
  --path caplet/Portfolio_and_Trading_Notes_snapshot.xlsx \
  --path-glob 'caplet/ips_drafts/*.pdf'

# 2. Replace strings everywhere (replacements.txt kept OFF the repo; one line per value):
#    literal:<WInS username>==>[WInS username removed]
#    literal:<dashed school email in r4_hist_original.py>==>[path removed]
#    literal:<client phone>==>[removed]
#    literal:<client personal email>==>[removed]
git filter-repo --sensitive-data-removal --replace-text ../replacements.txt

# 3. Fix commit author fields (mailmap kept OFF the repo):
#    Harry <NNN+login@users.noreply.github.com> <personal email>
git filter-repo --sensitive-data-removal --mailmap ../mailmap.txt

grep -c '^refs/pull/.*/head$' .git/filter-repo/changed-refs   # number of PRs affected, for the Support ticket
git push --force --mirror origin                              # PR refs are read-only; Support handles those
```

BFG alternative for steps 1-2: `bfg --delete-files 'aussef_complete_experiment_record.pdf'` and `bfg --replace-text replacements.txt caplet-clean.git`, then `git reflog expire --expire=now --all && git gc --prune=now --aggressive`. BFG cannot rewrite author emails; use filter-repo `--mailmap` for those.

Costs to weigh before doing it:
- Every commit SHA changes. SHAs cited in `caplet/docs/AI_USE.md` (e.g. 104476c, cc887b3, ef8aaf6) and in our reviews stop resolving. Keep `.git/filter-repo/commit-map` with the bundle so old SHAs can be traced.
- The 4 open PRs (#7, #8, #9, #12) get new diffs. Merge or close them first, as GitHub advises.
- One teammate pushing an old clone puts everything back. Claude Code cloud sessions hold clones too (e.g. `/home/user/caplet-investment`).
- **Copies outside GitHub cannot be recalled:** anyone who cloned or downloaded a ZIP, or any tool that indexed it. Wayback and Software Heritage hold nothing as of 19 Oct.

---

## 6. What stays UNVERIFIED

- Whether any search engine has indexed either repo (Bing ignored operators from this network; DDG blocked).
- Who visited or cloned (needs the owner's Insights > Traffic, step 1).
- Who the one stargazer is (starred 30 Sep) and who the current collaborators are (the API was refused).
- Whether the client profile and the IPS/TNA instruction PDFs are public outside SMApply's logged-in area.
- Who owns the three open 2025 Google files, and whether the "password" mentions in one of them include values (not read).
- Which of the two wordings in each live reflection cell is the accepted text and which the pending suggestion (open the Doc in Suggesting view).

## 7. Sources

- GitHub API, repo/forks/branches/pulls/comments/stargazers, read 19 Oct 2026 21:40 UTC; `git ls-remote` and fetch of both repos, same time.
- GitHub Docs, "Removing sensitive data from a repository" (accessed 19 Oct 2026): https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository (sections "Side effects of rewriting history", "Fully removing the data from GitHub").
- GitHub Docs, "What happens to forks when a repository is deleted or changes visibility" (accessed 19 Oct 2026): https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility
- Wharton Rules & Roles (accessed 19 Oct 2026): https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ ("Use of Generative AI", "Recording Policy", "Ethics", client-contact rule).
- Wharton AI policy (accessed 19 Oct 2026): https://globalyouth.wharton.upenn.edu/ai-policy/
- `competition/official/2026_27/smapply_public_2026-10-14/faqs.txt:89-92`.
- Wayback availability API and Software Heritage origin API, 19 Oct 2026 21:50 UTC.
- Prior work this builds on: `snap/main/research/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md` §9; `oct16/lenses/L09_integrity_compliance.md` (INT-05, INT-06, INT-19, INT-20); `oct19/verify/verify_numbers_office_notes.md:54`; `oct19/verify/verify_ips_exemplars.md`; `oct19/drive/ips_report_live.md`.
- Working files: `oct20/exposure/scripts/` (dump_blobs.py, bin_scan.py, overlap.py, notes_overlap.py); `oct20/exposure/work/` (mirror.git, blobs/, search/). The `work/blobs` folder holds raw repo content, including the personal data above. Delete it when this audit has been read.
