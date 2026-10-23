# Delta check: did the team change anything after the 20 Oct baseline? (Wave G)

Checked Tue 20 Oct 2026, 10:08-10:15 Sydney (19 Oct 23:08-23:15 UTC). Read-only on GitHub (`gh api` GET only) and Drive
(search, metadata and read tools only). AI-generated research, not for submission.

Baseline the 20 Oct work assumed: GitHub `main` = f191d6e; Drive IPS Report modifiedTime 2026-10-18T00:49:32Z.

## Bottom line

**Nothing has changed.** Since the baseline the team has made no commit, branch, PR, review or comment on GitHub, and
no edit, new file or comment in the Caplet Drive folder. No 20 Oct file is stale because of team activity. There are
still no student-written TNA reflections or IPS text beyond what the 19 Oct copies already held, and the pending AI
suggestions in the IPS Report have been neither accepted nor rejected. Re-run the checks in the last section shortly
before the final synthesis; the TNA is due Sat 24 Oct 08:00 Sydney.

## 1. GitHub (raei-2748/caplet-investment)

| Check | Result | Evidence |
|---|---|---|
| `main` head | Still **f191d6e** (merge of PR #11, 19 Oct 10:28 Sydney) | `gh api repos/.../branches` |
| Commits since 19 Oct 00:00 UTC, every branch (22 branches) | Only 3, all on `claude/ecstatic-wright-76bbun`: 39c37c3, 6b820d2, 1559f43, 19 Oct 20:35-20:37 Sydney (AI "Office WO-0002" memo on why IPS V5 would not reach the semis, plus its fact-check fixes) | `gh api repos/.../commits?sha=<b>&since=2026-10-19T00:00:00Z` |
| Was that already in the 20 Oct baseline? | **Yes.** The local snapshot `/home/user/snap/claude_ecstatic-wright-76bbun` matches 1559f43 byte for byte (checked: `office/outbox/2026-10-19_WO-0002_...md`, `keel/office/LEDGER.md`, `keel/office/work_orders/WO-0002.md`). Five 20 Oct files already cite it (`compliance/compliance_matrix.md`, `artic/artic_bank.md`, `timeline/timeline.md`, `ailog/ai_use_register.md`, `exposure/exposure_audit.md`) | `git show origin/...:<f> \| diff` |
| New branches | None. The 22 GitHub branch tips match the local `origin/*` refs exactly | branch list vs `git for-each-ref` |
| PRs opened or updated | Only #12 (that WO-0002 branch; opened 19 Oct 20:35 Sydney, still a **draft**, open, not merged, no reviews, no comments). #9, #8 and #7 are still open and untouched since 17-18 Oct | `gh api .../pulls?state=all&sort=updated` |
| Comments or reviews since 18 Oct | One automated code-review bot summary on #11 (19 Oct 10:28 Sydney, "no findings"). No human comments. No PR review comments | `.../issues/comments?since=`, `.../pulls/comments?since=` |
| Repo activity | Last push 19 Oct 20:37 Sydney (the WO-0002 branch). The one fork was last pushed 19 Oct 09:41 Sydney (18 Oct 22:41 UTC), before the window | `gh api repos/...`, `.../forks`, `.../events` |

What this means for the files named in the brief:
- `COMPETITION.md` on main is identical to the snapshot, so the coupon facts there have not changed.
- `caplet/docs/AI_USE.md` is unchanged on main (main has not moved). There is no root-level `AI_USE.md` on any branch.
- `keel/office/workstreams/` (1_TNA, 2_IPS, 3_FINAL_REPORT) is unchanged on main.
- No TNA text has been committed anywhere.

No throwaway clone was needed: the local `origin/*` refs already hold every current branch tip.

## 2. Google Drive (Caplet Investments folder <team-Drive-folder-ID>)

### Inventory and modified times (no item modified after 2026-10-18T00:49:32Z)

| Item | Last modified (Sydney) | Changed since baseline? |
|---|---|---|
| IPS Report (Doc) | Sun 18 Oct 11:49 (2026-10-18T00:49:32.025Z) | No: this is the baseline timestamp itself |
| Portfolio and Trading Notes (Sheet) | Sat 17 Oct 12:28 | No |
| Notes & Discussions (Doc) | Sat 17 Oct 14:05 | No |
| PM Dashboard (Sheet) | Sun 11 Oct 19:45 | No (still an empty sheet) |
| Final Report (Doc) | Wed 7 Oct 10:28 | No |
| Strategy Notes (Doc) | Wed 30 Sep 10:24 | No |
| Caplet IPS PDF | Wed 30 Sep 17:20 | No |
| AI Outputs folder (11 files) | 28-29 Sep | No |

A Drive-wide search for `modifiedTime > 2026-10-18T00:49:32Z` turned up no Caplet files. It did turn up the parent
folder "Knox Wharton 2026": its modifiedTime and its "shared with me" time are both 19 Oct 19:57 Sydney. That looks
like a sharing or permission event, not a content change (UNVERIFIED). None of the parent folder's own files changed
after 18 Oct. Its team-wide AI subfolders (.claude, Monitor, Claude Lab) hold no files modified after the cutoff. I saw
the other Knox teams' folders only as names in the parent listing and did not open them.

### Content re-read and diff (comments do not change Drive's modifiedTime, so each file was read again)

- **IPS Report**: re-read with comments. With the WInS username blanked, the body text (all tabs) is **identical** to
  `oct19/drive/ips_report_live.md`; the only diff lines are the comment summary the 19 Oct copy appended. There are
  still 3 comment threads with the same IDs, statuses and timestamps (2 resolved, 1 open; the newest is 17 Oct 18:03
  Sydney). No new comments.
  - **Pending AI suggestions: unchanged, neither accepted nor rejected.** The run-together double wordings the 19 Oct
    copy flagged are still there. Example: Version 5's pitch still has both wordings fused, at the words
    "growing branch.Our Root-and-Branch". Version 5 still carries its "[AI]" label.
  - Saved copy: `oct20/delta/data/ips_report_20oct.md` (WInS username removed; the threads summary has no author
    names).
- **Notes & Discussions**: re-read with comments. A word-level comparison against the 19 Oct copy gives a 0.992
  similarity. Every difference comes from the export format (a link URL shown differently, and two images shown as
  "image" here versus the text descriptions in the 19 Oct copy). No text edits. Still no comment threads.
- **Portfolio and Trading Notes**: modifiedTime unchanged. The re-read shows "No anchored comments". The "TN Analysis"
  tab in the sample the tool returned still has an empty Reflection cell and Word count 0 (pick 1). The tool shows only
  sample rows, so picks 2-3 were not re-read, but an unchanged modifiedTime means no cell changed.
- **PM Dashboard**: still "Empty Sheet", no comments.

### Student-written text now present?

**No new student text anywhere.**
- The TNA reflection cells in the sheet are still empty.
- The IPS Report's "Trading Note Reflection" tab is unchanged from 19 Oct. It still holds the same mix of AI-exemplar
  wording and team-edited wording that the 19 Oct copy described.
- IPS Version 5 is unchanged.

## 3. Which 20 Oct files are now stale?

**None, as far as team activity goes.** Every 20 Oct output assumed `main` = f191d6e, the WO-0002 branch at 1559f43,
the IPS Report at 18 Oct 00:49:32Z, Notes at 17 Oct and the sheets at 17 Oct and 11 Oct. All of those still hold.
This includes:
- `oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md`, `.pdf` and `.html`
- the tnakit2, ipsfix, compliance, timeline, ailog and exposure folders

Three things can still go stale on their own clock, whatever the team does:
- statements like "X days until the TNA deadline"
- market-price snapshots
- the line "PR #12 is a draft"

## 4. Limits of this check

- Drive revision history and the accept/reject state of suggestions are not visible through the read tools. I
  inferred "unchanged" from the identical text and the unchanged modifiedTime: accepting or rejecting a suggestion
  changes both.
- Sheets were checked by modifiedTime and comment anchors, not by a full cell-by-cell export.
- The check reflects state at 10:15 Sydney, 20 Oct. The team works mostly in the evenings (the last edits were on
  17-18 Oct), so the next likely window for changes is tonight before the 24 Oct TNA deadline.

## 5. How to re-run (about 2 minutes)

- GitHub: `gh api "repos/raei-2748/caplet-investment/branches?per_page=100"` and compare the tips with the table
  above, especially `main` = f191d6e. Then `gh api "repos/raei-2748/caplet-investment/pulls?state=all&sort=updated&direction=desc&per_page=5"`.
- Drive: run `search_files` with `parentId = '<team-Drive-folder-ID>' and modifiedTime > '2026-10-18T00:49:33Z'`.
  An empty result means no edits. Then `read_file_content` (includeComments) on the IPS Report and run
  `oct20/delta/scripts/cmp_doc.py <saved json> oct19/drive/ips_report_live.md <out>`.
  Scripts: `oct20/delta/scripts/cmp_doc.py` (IPS Report diff plus comment-thread summary) and
  `oct20/delta/scripts/cmp_words.py` (word-level diff for Notes & Discussions).
