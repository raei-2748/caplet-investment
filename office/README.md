# Caplet Research Office

An office of AI desks (Claude Code subagents) that does research and checking for Team Caplet's 2026-27 Wharton
entry. Goal: help the students reach the **Top 50 semifinals**, which are chosen on the written TNA, IPS and Final
Report. The office is built around what the 16 Oct review found is stopping us
(`research/assistant_review_2026-10/04_What_Stops_Us_Winning_16Oct2026.md`): hard gates, one ladder basis,
student ownership, honest certainty wording, and a Final Report started too late.

**Read `office/CHARTER.md` first.** The short version: students decide and write; the office checks, measures and
finds problems; one page per answer; no new research waves before the IPS is in.

## Org chart

Each desk has an AI lead and three AI specialists. Each desk reports to a **student role** (the roles from Part 13
of the 16 Oct review). The team fills in which student holds which role in its private sheet, not here.

```
                         TEAM (votes on strategy, trades, anything submitted)
                                              |
                         Team lead + deputy (student) -- only Ray trades / submits
                                              |
                              chief-of-staff (AI)  +  fact-checker (AI)
          ____________________________________|______________________________________
         |              |               |               |               |             |
  Rules & Integrity  Numbers       Strategy & Risk  Client &        Judging &      Records
  owner: rules,      owner: rates  owner: growth/   Co-sponsor      Editorial      owner: historian /
  format & privacy   analyst       risk analyst     owner: client/  owner: editor  AI-log keeper
  lead                                              co-sponsor lead
  rules-lead         numbers-lead  risk-lead        client-lead     judging-lead   records-lead
   format-gatekeeper  ladder-pricer devils-advocate  case-analyst    mock-judge     ai-use-recorder
   rules-verifier     numbers-     scenario-        cosponsor-      coherence-     evidence-archivist
   integrity-officer   auditor      modeller         reader          checker        decision-log-clerk
                      market-data- trade-checker    taiwan-         final-report-
                       clerk                         researcher      planner
```

26 agents in all. Definitions: `.claude/agents/<name>.md`.

| Desk | What it is for | Busiest | Specialists |
|---|---|---|---|
| Office of the Chief | Takes work orders, routes them, enforces the volume cap, merges desk answers into one page, keeps the ledger | always | `chief-of-staff`, `fact-checker` (re-derives every number and re-opens every quote before a memo ships) |
| Rules & Integrity | Hard gates that can void a deliverable; exact Wharton text; AI policy and privacy | TNA, IPS, FR submit weeks | `format-gatekeeper` (word/char counts, format), `rules-verifier` (exact official text, rule changes, FR instructions on 9 Nov), `integrity-officer` (authorship, AI-use honesty, public-repo privacy) |
| Numbers | One ladder basis, one numbers sheet, every figure dated and labelled | IPS (one basis), 7-9 Nov rebuild | `ladder-pricer` (holdings-basis pricing), `numbers-auditor` (blind re-derivation, contradiction hunt), `market-data-clerk` (Treasury curve, fund facts, cited) |
| Strategy & Risk | Devil's advocate on rules the IPS will freeze; bad-case tests; checks any proposed trade | vote set B (27 Oct) | `devils-advocate`, `scenario-modeller` (joint stock + yield bad cases, MODEL), `trade-checker` (rule check of a pasted ticket; plan is hold) |
| Client & Co-sponsor | Client knowledge: the case read exactly; how a co-sponsor hears the 2031 range; Taiwan context | from Sun 8 Nov | `case-analyst`, `cosponsor-reader`, `taiwan-researcher` |
| Judging & Editorial | Mock judging after the humans score; TNA/IPS/FR consistency; Final Report module plan | 21 Oct, 1 Nov, 22 and 29 Nov | `mock-judge` (5 personas), `coherence-checker`, `final-report-planner` |
| Records | Facts for the AI-use log and the experience journal, from dated records only | every Sunday | `ai-use-recorder`, `evidence-archivist`, `decision-log-clerk` |

## How to use it

1. **Ask a question.** In Claude Code, in this repo:
   ```
   /office <your role>: <one question> | decides: <what it informs> | by: <date>
   ```
   Example: `/office rates analyst: on the 16 Oct close, what is the room under $300k on the holdings basis? | decides: IPS certainty sentence | by: Tue 27 Oct`.
   The Chief of Staff logs a work order (`office/work_orders/`), sends it to the right desk(s), has the
   Fact-checker verify, and writes one memo to `office/outbox/`. You can also call a single agent directly:
   "use the format-gatekeeper agent on ...".
2. **Run a set piece** (saved workflows in `.claude/workflows/`, run by asking Claude to "run the office-gate-check workflow ..."):
   - `office-gate-check`: Rules & Integrity + coherence check of a deliverable before submission. Pass/fail per gate.
   - `office-judge-panel`: five independent mock judges + judging lead. Refuses to run until the humans' own
     scores are logged (16 Oct review item 23).
   - `office-work-order`: the full route for a big question: chosen desks in parallel, each lead synthesises its
     specialists, fact-checker, chief of staff one-pager.
3. **Check text yourself** with no AI at all:
   ```
   python3 office/tools/textcheck.py draft.txt --limit 100
   python3 office/tools/textcheck.py my_paste.txt --compare wins_note.txt
   ```
   It gives two word counts (by spaces, and a stricter one), the character count, curly quotes and other
   non-ASCII characters (Google Docs inserts curly quotes; WInS notes are plain ASCII), the banned-word list and an
   exact-match check with the first differing character.

## The calendar (Sydney time)

| When | Desks working | Set piece |
|---|---|---|
| now - Thu 22 Oct | Rules & Integrity, Judging, Records | gate check of the 3 notes + reflections Thu 22 Oct; judge panel Wed 21 Oct after the outside reader |
| Sat 24 Oct 08:00 | **TNA due** | |
| Sun 25 Oct | Records (AI-log and journal back-fill facts) | |
| Tue 27 Oct | Strategy & Risk and Numbers: half-page options notes for vote set B, only if the owners ask | |
| Wed 28 Oct - Thu 5 Nov | Rules & Integrity, Numbers, Judging | judge panel Sun 1 Nov; gate check Wed 4 Nov |
| Sat 7 Nov 09:00 | **IPS due, trading frozen** (quiet period ends) | |
| Sun 8 - Mon 9 Nov | Numbers (rebuild on the 6 Nov close), Client & Co-sponsor opens, Judging (FR module plan) | |
| Tue 10 Nov | Rules & Integrity reads the Final Report instructions; every FORECAST replaced | |
| to Wed 2 Dec | all desks, on request | judge panels Sun 22 and Sun 29 Nov; gate check Tue 1 Dec |
| Sat 5 Dec 09:00 | **Final Report + school letter due** | |

## Files

| Path | What |
|---|---|
| `office/CHARTER.md` | the house rules every desk follows |
| `office/LEDGER.md` | one row per work order: who asked, which desks, output, what the students decided. Doubles as the source for the AI-use log |
| `office/work_orders/` | the work orders (template: `WO-TEMPLATE.md`) |
| `office/outbox/` | the memos (AI-generated, not for submission) |
| `office/tools/textcheck.py` | counts and exact-copy checks, no AI |
| `.claude/agents/` | the 26 agent definitions |
| `.claude/skills/office/SKILL.md` | the `/office` entry point |
| `.claude/workflows/` | the three set pieces |

The older `ops/routines/` (monitor, rules watcher, mock judges, evidence lab on Ray's Mac) still exist. The office
replaces none of them yet; the team can retire routines once a desk covers them.
