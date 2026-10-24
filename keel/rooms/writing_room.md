# The Writing Room

> Room card: `../OFFICE.md`. Host: Tess (cuts the fat, runs the counts); Amara writes first drafts. Agents:
> `format-gatekeeper`, `final-report-planner`. Tools: `../office/tools/textcheck.py`, `../VOICE.md`.
> Rule: flag only hard issues (limits, rule breaches, facts, numbers, formatting) with minimal edits; never reword
> for taste or soften a confident claim. Suggestions stay in the repo; never touch the Google Docs.

> **State (Sat 24 Oct, afternoon run):** checked `/mnt/project-files/ips/IPS_edits_v2_2026-10-24.md` (pitch 47, IPS
> 494 strict). Open: Caplet picks option A/B/C (inflation rate) and cut package 1/2 by Tue 27 Oct; K4 date fix and
> "bond" -> "holding" waiting for the next draft. Next run: count the next draft (Tab 15 export or v3 suggestions) and
> check whether fix 2 (K4 dates) was taken.

## Runs
| Date | Draft checked | Counts (strict) | Hard issues | Memo |
|---|---|---|---|---|
| Sat 24 Oct | IPS edits v2 (E1-E12 + K1-K5) | pitch 47; IPS 494; +A 508; +A +package 1 +fix 2 = 467 | 4: option A over 500; K4 dates; "secures"; "bond" for ETFs | `../office/outbox/2026-10-24_writing-room_option-a-cut.md` |
| Sat 24 Oct (evening) | IPS v3 (v2 + Lab C1-C3, roots-free, [NAME] placeholder) | pitch 45; IPS 471 (467 by spaces); 0 overclaim; 2 en dashes | K4 dates and "holding" fixed; option A now fits under 500 with no cut; pitch "held to maturity" loose for ETFs; 2 lines flagged as still AI-sounding, both rewritten | `lab/L-05_ips_push/ips_v3.md`, `/mnt/project-files/ips/IPS_edits_v3_2026-10-24.md` |

## Tool changes
- 24 Oct: `textcheck.py` overclaim list now also catches "secures" and "guarantees" (it matched whole words only, so
  "secured" missed "secures").
