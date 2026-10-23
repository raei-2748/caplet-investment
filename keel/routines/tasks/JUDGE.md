# Caplet practice judging panel: instructions

Purpose: score Team Caplet's current draft as Wharton judges would, about a week before the deadline, so the team has time to fix substance (the evening-before gate checks only catch format).

## Hard rules
- Read-only on all team docs. Never message, email or comment to anyone. Never touch WInS orders.
- Give scores, evidence and fixes as bullets. Do not rewrite the team's prose (Wharton AI policy); short quoted phrases to locate a problem are fine.

## Load first
- Memory index `<Claude memory folder>/MEMORY.md` + linked files (official rules and format gates, Laura Gao case, winning-team portrait).
- Scoresheet: `<Google Drive>/Knox Wharton 2026/Winning Team Portrait and Scoresheet.md`.
- Client case: `Knox Wharton 2026/Laura Gao - 2026 Client Profile.pdf`.
- `Knox Wharton 2026/Monitor/RULES_CHANGES.md` for any new rules or released instructions.
- Judge lens: `Knox Wharton 2026/Claude Lab/00-judge-lens/README.md` (who judges, Wharton finance curriculum, concept map, style rules). Give it to judges 3 and 5.

## The draft to judge (mode given in the scheduled prompt)
Read Google Docs with the Drive read_file_content tool.
- **tna**: IPS Report doc `1qtEuzXq_QYdQ9VJlusPY9km2l80E1hkk8FPR0iw71-w`, tab "Trading Note Reflection" > "Deliverables" (drafts) and "WInS Trading Notes" (verbatim notes).
- **ips**: same doc, the newest IPS tab (was "Version 5"; check tab names).
- **final**: Final Report doc `1LYAtmddxSMyS7hnh82r25mqhnlNNq28wSxk5p0DACno` plus the official Final Report instructions (see RULES_CHANGES.md or SMApply). Also look at `Knox Wharton 2026/Claude Lab/` for evidence the draft could be using but isn't.
If the draft is empty or a skeleton, say so at the top, mark status red, and judge whatever outline/notes exist instead.

## Panel
Run 5 independent judges with the Agent tool in parallel. Give each only the draft, the client profile, the official criteria/format and the scoresheet, not each other's output or our team's internal notes (they should judge what a real judge would see):
1. Wharton faculty judge (finance rigour, assumptions, trade-offs).
2. Industry practitioner (wealth manager: client fit, would Laura trust this?).
3. Former finalist student judge (compares against what top-50 entries do).
4. Outsider with no finance background (clarity: can they say back the strategy in one sentence?).
5. Wharton undergraduate finance concentrator (has taken the courses in the judge lens). Checks: are the right textbook concepts used (e.g. cash-flow matching, reinvestment risk, shortfall risk) and used correctly, each explained in plain words; any misused term, jargon pile or overclaim ("risk-free", "guaranteed") that would make them wince; would they think "this team understands what I study"?
Each returns: format-gate pass/fail, 0-3 per scoresheet question with one line of evidence, the single weakest point, and the top 3 fixes.

## Report
Write `Knox Wharton 2026/Monitor/YYYY-MM-DD Judge panel (MODE).md`, under ~700 words:
- status (green/amber/red) and days to deadline;
- gate failures (anything that excludes the entry) first;
- score table (judges x criteria) and where judges disagree by 2+ points;
- a short "concept check" from judge 5: concepts used well, misused, and missing-but-would-resonate;
- top 5 fixes ranked by score impact, each with the evidence and a time estimate;
- comparison with the previous panel for the same deliverable, if any.
Then send Ray a short push notification (PushNotification tool): status + the #1 fix.
