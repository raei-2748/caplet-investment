# Team Keel

**This repository is Team Keel's.** Keel is a simulation: six AI contestants with their own memories, convictions and
voices, written to be the best high-school team in the Wharton Global High School Investment Competition 2026-27,
and set on one goal: **the Top 50 semifinal**. Client: Laura Gao.

Keel leads the work. **Team Caplet** (Ray, Ahaan, Darren, Harry, Eric, Young) is the real team that enters: Keel
plans, researches, checks and drafts; Caplet votes, rewrites in its own words and submits. Start with
[`keel/README.md`](keel/README.md). Rules, dates and formats: [`competition/COMPETITION.md`](competition/COMPETITION.md). Claude sessions
read [`CLAUDE.md`](CLAUDE.md) first.

**Talk to Keel:** `/keel status` · `/keel kai: attack our IPS` · `/keel meeting: how big is the sail?`

## Deadlines (Sydney time)
| Due | What |
|---|---|
| Sat 24 Oct 08:00 | Trading Notes Analysis |
| Sat 7 Nov 09:00 | IPS (an SMApply form) · trading ends, portfolio locks (last U.S. fill 08:00) |
| Tue 10 Nov 01:00 | Final Report instructions released |
| Sat 5 Dec 09:00 | Final Report + school documentation |

## The repo
```
keel/          ★ Team Keel: the leaders, and everything they run
  members/       nora · felix · jun · kai · amara · tess (each has a home room in the Office)
  episodes/      the daily diary: what Keel did, and what Caplet should check
  tea_room.md    the Long Room wall: plan, decision journal, open threads
  road_to_semifinal.md · drafts/ · scripts/
  OFFICE.md      the Keel Office: twelve rooms, who sits where, which agents work where (map + diagram)
  office/        charter, ledger, work orders, outbox, workstreams, tools
  routines/      scheduled checks and their reports
  library/       all AI research so far (assistant reviews, blueprints, models, insight_v1, council)
caplet/        The real team's work: Drive snapshots, deliverables, decisions, AI-use log
competition/   Official Wharton files (case, instructions, emails, SMApply snapshots, market data)
toolkit/       The September wharton-ic Python demo (cd toolkit && pytest)
archive/       Superseded material, incl. the history of every deleted branch
.claude/       Agent definitions, the /office skill and workflows
```

## Who does what
| | Keel (simulated) | Caplet (the students) |
|---|---|---|
| Agenda, deadlines, road to the semifinal | sets them | approves |
| Research, numbers, checks, drafts | does them | asks, reads, challenges |
| Strategy and trade decisions | proposes, with options | **votes** |
| Words sent to Wharton | drafts, labelled AI DRAFT | **rewrites and submits** |
| WInS orders | checks the ticket | **Ray places them** |
| Experience stories | never Caplet's | real events only |

## House rules (short version)
- Wharton's rules make every strategy decision the students' own, and submitted work must be in their own words.
  Keel never decides or submits for Caplet. Every AI use is logged for the Works Cited (`caplet/docs/AI_USE.md`,
  `keel/office/LEDGER.md`).
- Keel's files are labelled FICTION; Keel's invented events never go into Caplet's deliverables.
- Only Ray places or cancels WInS trades. Only WInS-listed stocks, ETFs and Treasury bonds; no TIPS or STRIPS.
- Facts come from official Wharton files or dated primary sources; anything else is UNVERIFIED.
