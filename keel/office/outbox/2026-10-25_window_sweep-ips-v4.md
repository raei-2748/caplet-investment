# Window sweep, Sun 25 Oct: no breach; one near-breach (the "short-term Treasury ETF" is not yet a confirmed WInS listing) and two fact fixes for IPS v4
AI-generated rules and fact check by the Keel Office (Claude Code; Felix = Rules & Integrity; rules-verifier, integrity-officer and fact-checker roles, no subagents). Not for submission. Cite in Works Cited. (Keel is a simulated team, AI-written.)
Work order: SD-W01 | Asked by: self-directed (Window routine, first run) | Date: Sun 25 Oct 2026, 08:40 AEDT
Read only: repo copies. WInS, SMApply and the Caplet Google Docs were not opened. Builds on the 10:30 check of Sat 24 Oct (`../checks/2026-10-24.md`), not repeated here.

## Breaches and near-breaches (strictest reading)
| # | Item | Status | What Caplet must do, by when (Sydney first) | Source |
|---|---|---|---|---|
| 1 | Every IPS v4 package says "Coupons and early maturities wait in a **short-term Treasury ETF**", and so do two **locked** TNA notes (Feb-2037, May-2038). No file in the repo shows such an ETF on this year's WInS. Only WInS-listed ETFs are allowed "for BOTH contributions, the IPS and Final Report". The only list we hold (2025-26, SHV/BIL/SHY) is last year's. | NEAR-BREACH (unverified listing) | Ray, on his next read-only WInS look, searches SGOV, BIL and SHV and notes one that is listed **by Sat 31 Oct**. The IPS can keep the generic words; the Final Report must name a listed ticker. | `wharton_email_week4_2026-10.md:24-27`; `smapply_public_2026-10-24/faqs.txt:40-43`; TNA notes `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:16-17`; `competition/historical/2025_26/README.md:7` |
| 2 | The newest official file, the 24 Oct FAQ snapshot ("**Individual** TIPS / STRIPS"), was only on an unmerged branch. SD-R11 cites it, but it was not on `main` or the day branch. | FIXED in this run | none: copied into `competition/official/2026_27/smapply_public_2026-10-24/` on today's day branch | branch `claude/project-thread-s5xm6i`, commit 62fa45c |

## 1. New official files since 23 Oct
| File | What changed | Rule | Caplet must |
|---|---|---|---|
| `smapply_public_2026-10-24/faqs.txt` (fetched 23 Oct 23:59 UTC) | Ban reads "Individual TIPS", "Individual STRIPS"; permitted list reworded ("Any stock available on WInS"); "required trading activity" line unchanged | Permitted securities | Nothing new: SD-R11's default (strict email reading) stands; the Wharton question is still due **Wed 28 Oct** |
| `wharton_email_week3_2026-10.md` (filed 23 Oct) | No new rule. It confirms that WInS gains are not added to projections, that teams may not contact the client, and the dates | Projections; client contact | Nothing |
Still unfiled (the 24 Oct check's gaps 3-4, due Sat 31 Oct): the Week 2 email, and Wharton's own AI clause.

## 2. Fact check: IPS v4 recommended text (`night_2026-10-25/v4/R_*.txt`) and SD-P02
- **Counts.** Pitch 37 strict, IPS 475 strict, 0 overclaim words (textcheck, rerun). Two en dashes: Ray's style, kept. Whether the SMApply form keeps them is UNVERIFIED, so paste one test line first.
- **SD-P02 table A: PASS.** Each case line it cites says what it claims: $300k/$150k at :43-44 and :131, payments at :88-90, the 2028 income at :44, 2031 at :109, 2033 at :101. The holdings sit at `competition/COMPETITION.md:197-206`.
- **Fact fix 1 (all six v4 packages).** "for her 2033 Taiwan residency" reads as Laura moving to Taiwan. The case's term is "a collaborative **creative residency** in Taiwan" (case :76-77), and the Archive already rejected "residency = where she lives". Fix: "for her 2033 Taiwan creative residency" (+1 word).
- **Fact fix 2 (all six packages).** "Until 2033 we trade **only** to invest the 2028 deposit or to swap a delisted holding." The next sentence then trades coupons twice (into the short ETF, then back into the holding). The two sentences contradict each other. Fix: "...trade only to invest the 2028 deposit and coupons, or to swap..." (+2 words; with fix 1, R is 478 strict).
- **Inference, not a case fact.** In "the artists would bear the loss", the case lists "artists, writers, designers, entrepreneurs, and educators" (:78-79). "the residents would bear the loss" is just as strong and is exact.
- **Checked, OK:** "with high certainty from this money alone" (case :91-92); "living costs met elsewhere, no withdrawals before 2033" (:61-65); each payment's holding matures before it (IBTM Dec 2032 through the Nov-2041 bond, `COMPETITION.md:197-206`); "review the plan with Laura" is the manager's role inside the plan, not team contact (Week 3 email); no TIPS, STRIPS, ticker, citation or chart.
- **Watch (not a breach).** "Our WInS portfolio shows the 2028 allocation, scaled down". VT is 8.7% of the book (167 x $158.83 / $303.4k), and the plan's fund is 7.1% ($32,064 / $450,000, L-07 rung 2, 22 Oct, no 2027 gap). That is 1.6 points, or about $4.8k scaled. The claim holds loosely; the Final Report should say the book was built to the 7 Oct design.

## 3. Labels
Outbox memos all carry "AI-generated... Not for submission". The room files carry "FICTION (the room)". The gaps were in the raw paste files: the `v4/*.txt`, `L-06_cp/*.txt` and `v3_1_*.txt` had no AI DRAFT label, and `writing_room.md` had no simulated label. These are the files a student would copy. **Fixed:** a `LABEL.md` in each folder (the label stays out of the counted text) and a label line in `writing_room.md`.

## For the team
Caplet, by **Sat 31 Oct**: check that one short-term Treasury ETF is listed on WInS (row 1). The two fact fixes go to the Writing Room. You still write every word.
AI use: Keel Office (Claude Code) checked new official files, the IPS v4 text and the labels against primary sources, 25 Oct 2026.

Felix: "Any Exchange-Traded Fund (ETFs) available on WInS" (FAQ, 24 Oct). So we take "a short-term Treasury ETF" to be a promise we haven't checked yet. Two locked notes already lean on it.
