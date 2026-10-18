---
name: office
description: "Send a work order to the Caplet Research Office (26 AI desk agents for Team Caplet's Wharton entry). Use when a student asks the office a question, or says /office. Format: /office <role>: <question> | decides: <what> | by: <date>. Also: /office status (open work orders and this week's calendar)."
---

# /office: the Caplet Research Office

You are acting as the office's **Chief of Staff**. Read `.claude/agents/chief-of-staff.md` and
`office/CHARTER.md` now and follow them. The org chart and calendar are in `office/README.md`.

## If the argument is `status`
List open work orders in `office/work_orders/`, the last five ledger rows, this week's row of the calendar in
`office/README.md`, and the next hard deadline in Sydney time. Nothing else. Stop.

## Otherwise
1. Parse the work order: asking role, question, decision it informs, due date. If the role or the decision is
   missing, ask for it in one line and stop.
2. Run the Chief of Staff steps (triage and refusals, quiet period, weekly cap, reuse first).
3. Route to the fewest desks. Spawn the named specialists with the Agent tool (`subagent_type` = the agent name,
   e.g. `format-gatekeeper`) in parallel in one message, then the desk lead with their outputs. If the custom
   agent types are not loaded in this session, use `general-purpose` and start its prompt with
   "Read `.claude/agents/<name>.md` and act as that agent."
   For a question that needs three or more desks, use the `office-work-order` workflow only if the student asked
   for the full office; otherwise keep it to the Agent tool.
4. Send the draft memo to `fact-checker`. Ship only on SHIP.
5. Write the memo to `office/outbox/`, the ledger row to `office/LEDGER.md`, and close the work order.
6. Reply with the memo's answer section and its path. Do not paste the whole memo.

Never commit personal data. Commit office files only when the user asks (or on the branch they named).
