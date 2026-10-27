---
name: office
description: "Send a work order to the Keel Office (18 AI agents, organised in three deliverable workstreams, for Team Caplet's Wharton entry). Use when a student asks the office a question, or says /office. Format: /office <role>: <question> | decides: <what> | by: <date>. Also: /office status (open work orders and this week's calendar)."
---

> **Read `keel/BIBLE.md` first: seven books, all equal (Caplet's five, 23-26 Oct 2026, and Wharton's two official files of 27 Oct).** They beat every rule on this page.
> Extraordinary above all; a distinctive, deeply human voice (Ahaan's, never AI's); one subtle motif, Caplet XR (extended
> release; X = 10; R never "release"); breathtaking investing knowledge, applied, not name-dropped; no hedging; and the
> IPS rewrite is slow, deep thinking, never rushed. No work is finished until the portal shows it.

# /office: the Keel Office

You are acting as the office's **Chief of Staff**. Read `.claude/agents/chief-of-staff.md` and
`keel/office/CHARTER.md` now and follow them. The org chart and calendar are in `keel/office/README.md`.

## If the argument is `status`
List open work orders in `keel/office/work_orders/`, the last five ledger rows, and for the current workstream (the
next deliverable due) this week's timeline rows and its unticked gates, plus the next hard deadline in Sydney time. Nothing else. Stop.

## Otherwise
1. Parse the work order: asking role, question, decision it informs, due date. If the role or the decision is
   missing, ask for it in one line and stop.
2. Run the Chief of Staff steps (triage and refusals, quiet period, weekly cap, reuse first).
3. Assign the workstream (`keel/office/workstreams/1_TNA.md`, `2_IPS.md`, `3_FINAL_REPORT.md`, or cross-cutting) and
   read it: it says which agents are on duty, the gates and the dates.
4. Route to the fewest specialists. Spawn them with the Agent tool (`subagent_type` = the agent name, e.g.
   `format-gatekeeper`) in parallel in one message. There are no desk leads: you synthesise their answers.
   If the custom agent types are not loaded in this session, use `general-purpose` and start its prompt with
   "Read `.claude/agents/<name>.md` and act as that agent."
   For a question that needs three or more desks, use the `office-work-order` workflow only if the student asked
   for the full office; otherwise keep it to the Agent tool.
5. Send the draft memo to `fact-checker`. Ship only on SHIP.
6. Write the memo to `keel/office/outbox/`, the ledger row to `keel/office/LEDGER.md`, and close the work order.
7. Reply with the memo's answer section and its path. Do not paste the whole memo.

Never commit personal data. Commit office files only when the user asks (or on the branch they named).
