# The Window, Mon 26 Oct 2026: the rewrite's ground-truth page checked; every 25 Oct model number re-run

(Keel is a simulated team, AI-written.) AI-generated check by the Keel Office (Claude Code; Felix = Rules & Integrity,
fact-checker role, one subagent re-ran the scripts). Not for submission. Cite in Works Cited. Read only: WInS, SMApply
and the Caplet Google Docs were not opened.

## Breaches and near-breaches (top)
**No breach.** Two near-breaches, both in the new rewrite spine `keel/ips_rewrite/00_GROUND_TRUTH.md`, which every
Draft 1 line will be checked against from 30 Oct:

| # | Item | Status | Fix, by when (Sydney) | Source |
|---|---|---|---|---|
| N1 | s5 still quotes the 15 Oct ladder (~$294-297k). Newest close on file (22 Oct): payment-date basis **$298,861, headroom $1,139 (4bp)**; the other two bases $300,224 / $302,139. "The first $300,000 buys all ten payments" is now a one-close call, not a fact | NEAR-BREACH (stale number in the spine) | Mark s5 stale; the rewrite echoes only the IBTR note's conditional. Trading Desk re-prices before Draft 1, **Thu 29 Oct** | `../checks/2026-10-24.md`; ASK_HUMANS SD-P02 |
| N2 | s5 "floor $150k face". IBTM is an ETF: no face. The locked TNA says its payout is "a net asset value, as opposed to a promise of par" and "not fixed" | NEAR-BREACH (wording that contradicts a locked line) | "IBTM sized to pay about $150k in 2032, quoted at $145k", **before Draft 1, Fri 30 Oct** | Archive A5, A11; `../../rooms/archive.md:33-35` |

## 1. New official files since 25 Oct 08:40
None. `git log` on `competition/` across main, the 25-26 Oct day branches and the rewrite branch shows only the
24 Oct FAQ snapshot filed last run. The 10:30 check's two gaps still stand (Wharton AI clause, Week 2 email; Sat 31 Oct).

## 2. Ground-truth page vs primary text
Every quoted phrase in s1-s3 was found word for word: form (`2026_WGY_Investment_Policy-FINAL.txt`), case
(`Laura_Gao_2026_Client_Profile.txt`), the locked TNA (`../../rooms/archive.md:26-42`) and the WInS notes
(`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15-24`; "filled 6-7 Oct ET" holds,
notes stamped 06-07 Oct ET). What's missing matters more. Six edits, in `../../ips_rewrite/inbox/2026-10-26_window.md`:
the semifinal gate and title-page items (form :82-100); "Your portfolio and Final Report should reflect the strategy
established in your IPS" (form :75), which decides whether a dedicated ladder (R01) needs the frozen book to show it;
"The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment" (case
:119-120); the five-item assumptions list (:146-148); the degree's real name (:16); and N1-N2 above.
Flag for the Final Report: case :4 has the advisor "who makes the final investment decisions" in the role-play; the
FAQ (`smapply_public_2026-10-24/faqs.txt:32`) says students trade and decide. One clause handles it.

## 3. Headline numbers in the 25-26 Oct memos, re-run
Four scripts re-run from a copy of the repo (deterministic seeds; fresh C-01 and LR-02 results byte-identical to the
committed JSON). **All match.**
- Courtroom C-01: 0.75% / 0.11% / 0.11%; top p50 $166,292 -> $156,292; Laura's kept half p5 $0 -> $8,310. OK.
- Laura's Room LR-02: gift below the quoted bottom 0.75 / 0.31 / 0.11% for buffers 0 / $5k / $10k; inside 99.25%. OK.
- Genius Lab P06: 9.0 -> 8.7%, 2.9 -> 2.7%, 29 -> 28%, $140k bottom unchanged. OK.
- Rewrite R01 (15 Oct curve): current ladder shortfall at -2pt **$21,385** (cost $297,457); dedicated, all ten kept,
  face >= $10k: **$10,027** (cost $298,943, +$1,486). "Roughly halves for ~$1.5k" holds. But that claim is written
  only in project memory, not in `keel/`: WO-R1 must put it in `lab/` with its numbers, and re-run it on 22 Oct.
- Library LC-02 (JPM 2027, global equity 7.5%): not re-read; am.jpmorgan.com refused by this session's proxy. Stands
  on the Library's 25 Oct reading; wording rule unchanged ("J.P. Morgan 2027 LTCMA, global equity, 7.5%").

## 4. Labels
All 21 files added since the last run carry "simulated"/"AI-generated"/FICTION labels, except three JSON results
files. Added `LABEL.md` to `keel/rooms/courtroom/` and `keel/rooms/lauras_room/` (P06's folder is labelled by its
README). Rewrite drafts from 30 Oct must carry `AI DRAFT (Claude, <date>)` on line 1.

## Takes
- **Felix:** Nothing broke. The page everyone's about to build on quotes perfectly and leaves out the three sentences that actually bite – the semifinal gate, "the portfolio should reflect the strategy", and "the range must protect the payments". A spine with missing vertebrae still looks like a spine.
