# Caplet Research Office (run by Team Keel)

An office of 18 AI agents (Claude Code subagents) that does research and checking for Team Caplet's 2026-27 Wharton
entry. The goal is to help the students reach the **Top 50 semifinals**, which are chosen on the three written
deliverables. The office is built around what the 16 Oct review found is stopping us
(`keel/library/assistant_review_2026-10/04_What_Stops_Us_Winning_16Oct2026.md`): hard gates, one ladder basis,
student ownership, honest certainty wording, and a Final Report started too late.

**Team Keel runs the office.** Nora heads it and each Keel member heads a desk (table in `keel/README.md`):
Felix = Rules & Integrity, Jun = Numbers, Kai = Strategy & Risk, Amara = Client & Co-sponsor, Tess = Editorial &
Records. Agents working for a desk read their desk head's file in `keel/members/` first. Caplet's students remain
the clients: they ask, vote and submit.

**Read `keel/office/CHARTER.md` first.** The short version: students decide and write. The office checks, measures and
finds problems. Each answer is one page, and there are no new research waves before the IPS is in.

## Workstreams: one per deliverable

The work is organised by what we submit. Each workstream file lists the official requirements, the student owners,
the dated timeline, which agents are on duty and the "done when" gates.

| Workstream | Due (Sydney) | Internal submit | Agents on duty | File |
|---|---|---|---|---|
| **1. Trading Notes Analysis** | Sat 24 Oct 08:00 | Thu 22 Oct | 10 | `keel/office/workstreams/1_TNA.md` |
| **2. IPS + trading freeze** | Sat 7 Nov 09:00 | Thu 5 Nov | 13 | `keel/office/workstreams/2_IPS.md` |
| **3. Final Report + school letter** | Sat 5 Dec 09:00 | Wed 2 Dec | all 18 | `keel/office/workstreams/3_FINAL_REPORT.md` |

Cross-cutting (any week): records (journal facts, AI-use log), trade checks, privacy scans.

## Org chart

```
                  TEAM (votes on strategy, trades, anything submitted)
                                       |
                  Team lead + deputy (student); only Ray trades and submits
                                       |
                         Nora (Keel): chief-of-staff + fact-checker   
     _____________________________________|__________________________________________
    |               |              |                |                |               |
 Rules &         Numbers        Strategy &       Client &         Judging &       Records
 Integrity       (rates         Risk             Co-sponsor       Editorial       (historian /
 (rules, format  analyst)       (growth/risk     (client/co-      (editor)        AI-log keeper)
 & privacy lead)                analyst)         sponsor lead)
 format-         ladder-pricer  devils-advocate  case-analyst     mock-judge      ai-use-recorder
  gatekeeper     numbers-       scenario-        cosponsor-       coherence-      evidence-archivist
 rules-verifier   auditor        modeller         reader           checker
 integrity-                     trade-checker    taiwan-          final-report-
  officer                                         researcher       planner
```

There are no desk leads. Each desk is a group of specialists, and each desk reports to a **student role** (Part 13
of the 16 Oct review). The chief of staff routes work orders to the specialists directly and writes the single
synthesis. The team fills in which student holds which role in its private sheet, not here.

| Agent | Desk | Job | Workstreams |
|---|---|---|---|
| `chief-of-staff` | Chief | Triage, routing, the one-page synthesis, the ledger | all |
| `fact-checker` | Chief | Re-opens every quote; re-derives every number before a memo ships | all |
| `format-gatekeeper` | Rules & Integrity | Word, character and page counts; curly quotes; exact-copy checks | 1 2 3 |
| `rules-verifier` | Rules & Integrity | Exact official text; rule changes; the Final Report instructions on 10 Nov | 1 2 3 |
| `integrity-officer` | Rules & Integrity | AI policy, authorship evidence, public-repo privacy | 1 2 3 |
| `ladder-pricer` | Numbers | Market data with sources, plus ladder pricing on a named basis | 1 2 3 |
| `numbers-auditor` | Numbers | Blind second calculation; finds the same figure stated two ways | 1 2 3 |
| `devils-advocate` | Strategy & Risk | Strongest case against a rule; vote set B options notes | 2 3 |
| `scenario-modeller` | Strategy & Risk | Bad cases, including stocks and yields falling together (MODEL) | 2 3 |
| `trade-checker` | Strategy & Risk | Checks a pasted ticket against the WInS rules (plan is hold) | 2 |
| `case-analyst` | Client & Co-sponsor | What Laura's case says, word for word | 1 2 3 |
| `cosponsor-reader` | Client & Co-sponsor | Reads a range or claim the way a funder would | 3 |
| `taiwan-researcher` | Client & Co-sponsor | Verified Taiwan facts; opens 8 Nov | 3 |
| `mock-judge` | Judging & Editorial | Five personas; runs only after the humans have scored | 1 2 3 |
| `coherence-checker` | Judging & Editorial | The TNA, IPS, Final Report and filed notes tell one story | 1 2 3 |
| `final-report-planner` | Judging & Editorial | Criterion map and modules before 9 Nov; re-map after 10 Nov | 3 |
| `ai-use-recorder` | Records | AI-use log rows for the Works Cited | cross-cutting |
| `evidence-archivist` | Records | Dated journal facts and decision-log rows (the "hold" checks) | cross-cutting |

Definitions: `.claude/agents/<name>.md`. On 19 Oct the office was merged from 26 agents to 18. The six desk leads
were dropped (the chief of staff synthesises instead), market data went into `ladder-pricer`, and decision-log
rows went into `evidence-archivist`.

## How to use it

1. **Ask a question.** In Claude Code, in this repo:
   ```
   /office <your role>: <one question> | decides: <what it informs> | by: <date>
   ```
   Example: `/office rates analyst: on the 16 Oct close, what is the room under $300k on the holdings basis? | decides: IPS certainty sentence | by: Tue 27 Oct`.
   The chief of staff logs a work order (`keel/office/work_orders/`), assigns it to a workstream, sends it to the right
   specialists, has the fact-checker verify the answer, and writes one memo to `keel/office/outbox/`. You can also
   call one agent directly: "use the format-gatekeeper agent on ...".
2. **Run a set piece.** These are saved workflows in `.claude/workflows/`. Ask Claude to "run the office-gate-check
   workflow ...":
   - `office-gate-check`: pass/fail for each hard gate of one deliverable before submission.
   - `office-judge-panel`: five independent mock judges, then a synthesis. It refuses to run until the students'
     own scores are logged (16 Oct review item 23).
   - `office-work-order`: the full route for a big question. The named specialists run in parallel, then the
     chief of staff writes the one-pager and the fact-checker checks it.
3. **Check text yourself** with no AI at all:
   ```
   python3 keel/office/tools/textcheck.py draft.txt --limit 100
   python3 keel/office/tools/textcheck.py my_paste.txt --compare wins_note.txt
   ```
   It gives two word counts (by spaces, and a stricter one), the character count, curly quotes and other
   non-ASCII characters, overclaim words, and an exact-match check that shows the first differing character.

## Files

| Path | What |
|---|---|
| `keel/office/CHARTER.md` | the house rules every agent follows |
| `keel/office/workstreams/` | one file per deliverable: requirements, owners, timeline, agents on duty, gates |
| `keel/office/LEDGER.md` | one row per work order; also the source for the AI-use log |
| `keel/office/work_orders/` | the work orders (template: `WO-TEMPLATE.md`) |
| `keel/office/outbox/` | the memos (AI-generated, not for submission) |
| `keel/office/tools/textcheck.py` | counts and exact-copy checks, no AI |
| `keel/office/CLAUDE_APP_PROMPT.md` | paste-in rules for teammates using the Claude app instead of Claude Code |
| `.claude/agents/` | the 18 agent definitions |
| `.claude/skills/office/SKILL.md` | the `/office` entry point |
| `.claude/workflows/` | the three set pieces |

The older `keel/routines/tasks/` (monitor, rules watcher, mock judges and evidence lab on Ray's Mac) still exist. The
office replaces none of them yet; the team can retire a routine once the office covers it.
