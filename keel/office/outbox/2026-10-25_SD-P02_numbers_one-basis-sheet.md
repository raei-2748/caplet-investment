# Every number in the IPS v4 text is a case fact or a holding; the vote copy mixes two curves and two J.P. Morgan editions
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
Work order: SD-P02 | Asked by: self-directed (board card P02; Rooftop request, Sat 24 Oct) | Desk(s): Numbers (Jun; numbers-auditor role, no subagents) | Date: Sun 25 Oct 2026 (Sydney)

## Answer
- **The IPS v4 text (pitch 37, IPS 475 strict; `keel/rooms/night_2026-10-25/ips_v4.md`) carries no modelled
  number.** Every figure is a case fact or a WInS holding (table A). Keep it that way: no model number has to be
  re-dated before 7 Nov if none goes in.
- **The vote copy for Tue 27 Oct does carry model numbers, on mixed bases** (table B). Two curves (15 Oct and
  22 Oct) and two J.P. Morgan editions (2026: 7.0%; 2027: 7.5%) sit side by side. Every tail figure below was run at
  7.0%, while the Archive's default for any stated return is 7.5% (`keel/pm/ASK_HUMANS.md`, Sat 24 Oct).
- **Rule for the working copy:** a number goes in the margin as `value | source | edition or curve date | basis |
  MODEL/HISTORY/CASE`, and the margin is struck before pasting into SMApply.

**A. Numbers in the IPS v4 text (all pass)**
| Number in the text | Source | Edition / date | Label |
|---|---|---|---|
| $450,000 (= $300,000 in 2027 + $150,000 in 2028) | `Laura_Gao_2026_Client_Profile.txt`:43-44, :131 | 2026-27 case | CASE |
| ten $50,000 payments, each January 2033-42 | case :89-90 | 2026-27 case | CASE |
| 2028 deposit from "publishing advances, speaking engagements" | case :44 | 2026-27 case | CASE |
| 2031 range, 2033 contribution | case :109, :101 | 2026-27 case | CASE |
| "2032 Treasury ETF" (floor) | IBTM, iBonds Dec 2032; `competition/COMPETITION.md`:197 | WInS fill 7-8 Oct | HOLDING |
| "five Treasury ETFs for 2033-37, then five bonds for 2038-42" | `competition/COMPETITION.md`:197-206 | WInS fills 7-8 Oct | HOLDING |

**B. Numbers in the vote copy (SD-T03, SD-T04, SD-T12, Monday ballot, L-07)**
| Figure | Curve | Return edition | Basis / script | Flag |
|---|---|---|---|---|
| Ladder cost $298,861 / $300,224 / $302,139 | 22 Oct | n/a | payment-date (zero-coupon) / holdings zero-rate / holdings forward (`ladder_history.py`, `ips_numbers.py`, `range_2031.py`) | Three bases: quote one, name it |
| P(ladder over $300k) 47% | 22 Oct | n/a | `ips_numbers.py`, 1.0 pt/yr rate vol | MODEL; vol is an assumption |
| Floor / quoted bottom ~$140k ($145k on 16 Oct) | 22 Oct | **2026 (7.0%)** | `range_2031.py` | MODEL |
| Coupon miss 9.0% of paths; buffer $10k -> 2.9% | 22 Oct | **2026 (7.0%)** | `L-02_buffer_run.py` | MODEL |
| Coupon gap ~$21,000 if yields fall 2 pt for good | **15 Oct** | n/a | `IPS_number_sheet.md`:34 | Older curve than every figure beside it |
| Stock fund $32,064 of a $150,000 remainder | 22 Oct (fwd 4.92%) | n/a | `L-07_lunch_line/rung2.md`:12; assumes no 2027 gap | MODEL; with a gap the remainder is smaller |
| 29% of paths end below the 2031 top | 22 Oct | **2026 (7.0%)** | L-07 rung 2:29, 200,000 paths, 16.78% vol | MODEL |
| Stock return 7.5% | n/a | **2027**, press release 19 Oct | WO-0003:7; matrix not yet read at source | UNVERIFIED at source (Library request open) |

## Evidence
Files and lines as cited above; `keel/office/outbox/2026-10-24_SD-T03_numbers_ladder-22oct.md` (Sources: "J.P. Morgan
2026 AC World 7.00%"); `keel/rooms/archive.md`:51 (A1); `keel/pm/REQUESTS.md` (Rooftop and Archive requests, 24 Oct).

## Limits
- No model was re-run. Whether 7.5% moves the 9.0%, 2.9%, 29% or $140k is untested; the direction should be small
  and favourable (higher stock growth), but that is a guess until the scripts run (new card P06).
- 22 Oct is still the newest curve: treasury.gov is blocked from these sessions (P03).

## For the team
For information before vote set B (Tue 27 Oct): vote the rules, not the percentages, and if a number is read aloud,
read it with its curve date. Unless you say otherwise, Keel's Lab re-runs the four MODEL tail figures at 7.5% by
Mon 26 Oct, so Tuesday's sheet is on one edition.
AI use: Keel Office (Claude Code) listed every number in IPS v4 and the vote copy with source, date, edition and basis, 25 Oct 2026.

Jun: Table A is the best news of the week: a text with no model numbers can't go stale.
Kai: Table B is why I don't trust a sheet read aloud. Two editions on one page is how a judge catches you.
