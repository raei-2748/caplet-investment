# Gate D (red team): PASS. Every fix-now item is fixed; the rest is triaged with an owner and a deadline

WS7-fixer, RAB Kit, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet. Nothing was run against WInS
and no order was placed. The IPS Google Doc and the Sheet were not edited; nothing was pushed. The strategy is
unchanged: every fix is wording, sequencing, tooling or evidence.

## What was reviewed

Four WS7 reports on rab/integration 32168d2: red team round 4 (three-judge panel), devil's advocate round 5, key
assumptions round 3 and fact audit round 2. Their 56 items deduplicate to 43 distinct items:
**17 fixed, 25 deferred, 1 rejected** (`rab/redteam/triage.md`). All 17 raw fix-now items (13 distinct) are fixed.

## Fixed (details and files in `triage.md` s.A)

1. **The 1 Oct vote settles three things only:** the book, the one swap rule, roles. The backstop sentence moves to
   the 26 Oct D6 decision, so order 5's Friday note is IBTM_P (IBTM_R is never typed). The floor's definition is
   decided by 14 Oct; until then `refresh_tickets.py --floor-rule` defaults to `remainder`, the IPS as written.
2. **Both books compared before the vote:** `rab/decisions/D7_wins_book.md` (kit recommendation: the Portfolio
   tab). In Book L, October triggers B and C give no trade.
3. **Week-One email and Trading Details read on Thursday**, in the same read-only login as the bond drop-down, before
   the vote.
4. **Featured notes:** IBTR's EXAMPLE now names what was bought ("this Dec 2036 Treasury fund", 293 characters);
   IBTR_F the same. IBTP no longer claims a fair fill; "not paying extra" is a banned phrase.
5. **Swap rule branch (b)** for a listed alternate whose Friday price fails: wait in cash and buy one bond by 14 Oct,
   instead of selling a Treasury two weeks after buying it. The team chooses (a) or (b) at the vote.
6. **Friday tooling:** the price parser accepts "$23.49" and "not listed"; the U.S. jobs report (8:30 AM EDT =
   10:30 PM AEST Fri 2 Oct; Longbridge calendar, BLS UNVERIFIED) is in the clock and the checklist, with a re-check of
   ETF prices against their max after it.
7. **Records:** AI-use log brought up to date; WInS username and names redacted from the tracked IPS snapshot and the
   checklist; assumptions.md and premortem.md carry a dated errata block; hedge memo no longer tells the T41 note to
   say "latest payments first"; fixed-floor wording qualified in WS3/WS4 memos.

## Checks re-run after the fixes (ws7, before the merge)

| Check | Result |
|---|---|
| `refresh_tickets.py` (Gate A basis) | 83 pass, 0 fail; `tickets.csv` byte-identical; `tickets.md` gains the jobs-report row only |
| `refresh_tickets.py --basis friday` in a scratch copy, 29 Sep curve, "$23.49" and "not listed" typed | Portfolio 40 pass / 0 fail; a planned bond typed "not listed" fails a check with a WARNING (no crash) |
| `build_notes.py` | 0 fail; 32 rows; longest exemplar 293; pick openings 0 shared; variety pass; IPS quotes verbatim |
| `note_check.py --self-test` | pass; the new IBTR exemplar passes every content check with `--pick` |
| `check_gate_c.py` | 488 checks, **0 FAIL**, 18 UNVERIFIED, 16 CONDITIONAL, 32 STALE (live tab); `--self-test` 10 of 10 |
| `build_numbers_ws3.py --check` | 142 memo figures, 0 untraced; `numbers_ws3.yaml` unchanged |
| `numbers.yaml` | unchanged, sha256 `492ed3203958...` (matches `numbers.lock` and rab-kit) |

## Open before Friday (not done here: this gate worked only inside the ws7 worktree)

1. **Live Sheet tab "RAB Notes" is stale** for the rows changed here (IBTR, IBTR_F, IBTP exemplars; IBTM_P, IBTM_R,
   T40s, T40b, VT briefs). WS6/WS8 rewrites it from `rab/sheets/rab_notes.json` before Fri 2 Oct (Gate C G8 lists
   them). The "RAB Tickets" tab is unaffected (`tickets.csv` unchanged).
2. **`git stash` on rab/ws7 (`stash@{0}`, "interrupted ws7 fix agent WIP", 30 Sep 15:19)** holds ticket edits (IBTM
   split in two, VT as order 12). It is NOT applied: `tickets.csv` on integration is final for Friday. Never
   `git stash pop` it.
3. **Never push a rab/* branch.** The old IPS snapshot blob with the WInS username stays in git history; squash
   before any merge to a pushed branch.
4. The team reads the changed Thursday agenda (`friday_checklist.md`) and `D7_wins_book.md` before the vote.

## Deferred, most important first (full list in `triage.md` s.B)

- **Coupon-shortfall owner chain** (D1, D2, D3): rule 3 locks Laura's whole kept half in Treasuries to 2042 and ends
  in "her own money", which the case forbids relying on. Decide with D6 by 26 Oct; never write "her own money" in a
  deliverable.
- **No memo defines "a high degree of certainty"** (D5), although pick 2's reflection publishes one on 22 Oct. WS8
  adds one decision to the BRIEF by 20 Oct.
- **IPS word budget** (D6): about 40-50 words of edits against 17 spare; WS8 keeps one ledger with paired cuts.
- **D6 "keep half"** (D10, D11): holds on Book L only with no cost charged to the stock fund (WS7 scratch); WS2
  re-runs with costs before 26 Oct.
- **October trigger B** (D12) sells VT after a fall; decide by 14 Oct.
