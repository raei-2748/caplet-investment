# The three suggested TNA notes are clean plain text; the paste check has 4 things to verify, and 4 only SMApply/WInS can answer
AI-generated research by the Caplet Research Office (Claude Code). Not for submission. Cite in Works Cited.
Work order: WO-0001 | Asked by: team lead (office set-up test) | Desk(s): Rules & Integrity (format-gatekeeper, rules-verifier), fact-checker | Date: Sun 18 Oct 2026

## Answer
- **Export is clean.** In the 13 Oct copy (exported 14 Oct), IBTR (10/07/2026 04:42:53 AM ET) is 294 characters, IBTM (10/06/2026 10:01:41 PM) is 292 and VT (10/07/2026 08:27:19 PM) is 288. All are under 300. None has curly quotes, any other non-ASCII character, markdown residue, double spaces or escaped `$`/`%`.
- **Wrong-IBTR trap.** The cancelled IBTR note (10/06 08:31:27 PM) is the same text except at character 182: "more than 0.3 percentage points" where the filled note says "more than about 0.2 percentage points". If a paste is 288 characters long or contains "0.3", it is the wrong order.
- **The paste checker verifies on Thu 22 Oct:** (1) each note matches the WInS Trade Notes page character for character (`python3 keel/office/tools/textcheck.py paste.txt --compare wins_copy.txt`); (2) each note belongs to an order WInS shows as executed; (3) each reflection is ≤ 100 words on the stricter count (`--limit 100`); (4) each reflection covers why, fit with the strategy, and the client's goals, funding or risk.

## Evidence
- "Select three (3) Trading Notes from trades your team executed in WInS." / "Include each Trading Note exactly as it appears in WInS." / "100 words or fewer" / "The Trading Notes must correspond to trades executed in WInS. Yes, we will verify this." / "submit ... via the SurveyMonkey Apply form": `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt:42, 44, 46, 53, 54`; the coverage points are at :48, :50, :52.
- Deadline: "Due: October 23; no later than 5:00 p.m. ET" (`smapply_public_2026-10-14/deliverables.txt:22`), which is Sat 24 Oct 08:00 Sydney. The live SMApply deliverables and FAQ text matched the 14 Oct snapshot on 18 Oct 2026 (fetched with `fetch_text.py`).
- Note text: `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:14, 15, 19` (cancelled IBTR :37). The fact-checker extracted the notes independently and got the same lengths and the same difference at character 182.

## Limits
- The export is a copy of WInS, not WInS itself. Whether it is exact is UNVERIFIED until a student copies the notes from WInS.
- The instructions PDF behind the live "Click Here" link was not downloaded again. It was checked against the repo copy only.
- UNVERIFIED: whether the form also wants trade dates or IDs. No official text says.
- NOT CHECKABLE BY THE OFFICE (logged-in only): the SMApply form's fields and limits; "Mark as Complete" vs "Submit" and whether edits are possible afterwards; WInS order status.
- Flag, not a fail: the VT note says "her promised minimum". The note is filed and cannot be edited, so it is quoted as it is. "Promised" is on the overclaim list in `competition/COMPETITION.md` section 7, so the VT reflection's author should know what that minimum rests on.

## For the team
- The submitter opens the TNA form before Thu 22 Oct, with the deputy watching. Screenshot its fields and buttons privately, without submitting (16 Oct review item 7).
- Ray confirms in WInS Order History that all three orders are filled. The paste checker (a second student) runs the four checks on Thu 22 Oct evening.

AI use: Claude Code (Caplet Research Office, 3 sub-agents) checked the three suggested TNA notes' length and characters in the 14 Oct export and quoted the official TNA rules against the live SMApply pages, 18 Oct 2026.
