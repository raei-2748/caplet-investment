# TNA status, Fri 23 Oct 2026 ~15:20 Sydney (due Sat 24 Oct 08:00 Sydney = Fri 23 Oct 5:00 pm ET)

Source: live "IPS Report" Doc, tab "Trading Note Reflection", top "Rewritten" table, read 23 Oct ~15:05 Sydney
(Doc modified 23 Oct 03:36 UTC). Exact text: `oct23/tna_now/tna_now.md`. Compared with `oct21/tna/current_draft_21Oct.md`
section A and the 13 items in `oct21/tna/TNA_Teardown_v2_21Oct2026.md`. Requirements only; no wording supplied.

## What changed since 21 Oct
- **Picks changed:** IBTR is out of the top table. Slot 1 now holds the **Nov-2041 T-bond note** (B-T-3.125-15112041)
  under the heading "Trading Note 1: **B-T-4.750-15022037**" (the Feb-2037 bond). **Its reflection cell is empty.**
- IBTM reflection: the first sentence (zero-coupon plan, week 2 email) was deleted; "the root" became "one of the two roots".
- VT reflection: the last two sentences (half of VT added to the bound; the other half stays Laura's) were deleted.
- Order is now Nov-41, IBTM, VT.
- Wharton's three prompt bullets now sit between the "Trading Note 3: VT" heading and its table.

## Item table (13 teardown items)
| # | Item | Status | Evidence (current text) |
|---|---|---|---|
| 1 | VT "about 7.5% a year per JPMorgan" (false; JPM 2026 world = 7.00%, 7.5% = EAFE; IPS says 7%). Bound depends on VT's 2031 **value** | **NOT FIXED** (worse) | Sentence unchanged: "Its expected return, about 7.5% a year per JPMorgan, can raise the upper bound". The clause linking the bound to half of VT's value was deleted, so the reflection now ties the bound to the forecast only |
| 2 | IBTM "clear yield", "matures on a set date" (false; contradict the filed note "final payout is not fixed") | **NOT FIXED** | "it is cheap, easy to trade, has a clear yield, and matures on a set date" unchanged |
| 3 | IBTR "2036 Treasuries that mature in December 2036" (false) | FIXED (by removal) | IBTR reflection no longer in the top table |
| 4 | IBTM "a stock crash will not make her promise fail" (absolute; case warns overpromising damages credibility) | **NOT FIXED** | Sentence unchanged |
| 5 | IBTR: report the note's pre-set test | **NOT FIXED** (dropped) | IBTR removed. The test has now **crossed** on the 22 Oct close (see IBTR test below), so the strongest evidence is now unused |
| 6 | IBTR "bought the ladder from 2042 backwards" vs WInS order times | FIXED (by removal) | Not in current text. If a Nov-41 reflection says "first", that is consistent: Nov-41 was the first order (10/06 07:55:45 PM) |
| 7 | IBTM "therefore became the best alternative" credits the email; refinement rule (floor quoted rounded down) and ladder-first order missing | **PARTLY** | The false credit to the email is gone with the deleted sentence. Still no refinement: the reflection now shows no decision changed or tested at all, and "second deposit buys a second batch of IBTM" still omits "ladder completed first, if needed" |
| 8 | VT retained half given jobs the note says stocks do not do; "stays Laura's" | FIXED (by removal) | Both sentences deleted |
| 9 | VT "9% of the portfolio" is the WInS share (Laura's plan about 7%); no rejected alternative; no specific downside | **NOT FIXED** | "(9% of the portfolio)" unchanged; no alternative; no downside named |
| 10 | Set: unused material (liquidity; 75% stocks to under 10% refinement; same-deposit trade-off; income-dependent 2028 deposit) | **NOT FIXED** | None of these appears. Liquidity still never mentioned |
| 11 | Set order should read payments, floor, growth; cut repeated note content | **PARTLY** | Order Nov-41 (payment), IBTM (payment + floor), VT (growth) now follows the IPS. VT reflection still repeats its note (diversification, no stock picking) |
| 12 | Word counts ≤95 by spaces | **PARTLY** | IBTM 72, VT 66 (both pass, room for fixes). Slot 1: 0 words (empty) |
| 13 | Paste each note from WInS; "co-sponsors here" typo | **PARTLY** | All three top-table notes match the WInS export exactly (Nov-41 288, IBTM 292, VT 288 chars). But slot 1's **heading names the wrong security** (Feb-2037 bond, note is Nov-2041). The "## VT" working copy still reads "here" |

## Checks on the current text
**Word counts (by spaces / crude counter / characters):**
| Slot | Words | Crude | Chars | Pass ≤100 | ≤95 |
|---|---|---|---|---|---|
| 1 Nov-41 | 0 (empty) | - | - | n/a | n/a |
| 2 IBTM | 72 | 73 | 401 | yes | yes |
| 3 VT | 66 | 69 | 412 | yes | yes |
Curly quotes: IBTM 3, VT 4 (harmless). Overclaim word scan (office/tools/textcheck.py): 0 hits, but the list does not catch "her promise".

**Exact match against the Doc's "WInS Trading Notes" table:** Nov-41 (10/06/2026 07:55:45 PM) identical; IBTM
(10/06/2026 10:01:41 PM) identical; VT (10/07/2026 08:27:19 PM) identical. Slot 1 heading "B-T-4.750-15022037" does
not match its note (that security's note begins "we use the 4.750% Treasury maturing 15 Feb 2037").

**False or misleading facts in the current text (register `oct20/numreg/numbers_register.md`, factcheck `oct21/tna/factcheck/factcheck.md`):**
- FALSE: VT "about 7.5% a year per JPMorgan" (JPM 2026 LTCMA AC World 7.00% compound; IPS V5 uses 7%).
- FALSE: IBTM "has a clear yield" (iShares shows three different yields) and "matures on a set date" (fund closes "on or about" 15 Dec; payout not fixed; contradicts the team's own filed note).
- OVERCLAIM: IBTM "a stock crash will not make her promise fail".
- MISLEADING: VT "9% of the portfolio" (8.84% of the WInS $300k at cost; about 7% of Laura's real plan, register H4).
- NEW, MISLEADING: IBTM "one of the two 'roots'". The IPS V5 pitch has the roots as Treasuries for every payment plus a Treasury floor; IBTM is part of both, not one of two root holdings. Use the metaphor the way the IPS does.
- NEW, minor: VT "the part that grows" implies the Treasuries do not grow (they earn about 5%). It is the only part whose value can rise or fall with markets.
- NEW, not verified: the filed Nov-41 note says "no iBonds Treasury funds maturing in 2037-43". Nothing in the register or factcheck verifies this. The note cannot be edited; if the slot-1 reflection relies on it, one student checks the iShares iBonds Treasury list first. (UNVERIFIED)
- Still true and fine: "WInS lists no individual Treasury maturing in 2032" (team record 29 Sep; re-check the WInS drop-down), "cheap" (0.07%), "easy to trade" (0.05% median spread), VT about 10,000 stocks at 0.06%.

## IBTR test (note: "if yields fall more than about 0.2 percentage points by January")
Data: treasury.gov 2026 daily par curve CSV fetched 23 Oct ~15:15 Sydney (cache-buster, via proxy), latest row
**22 Oct 2026**. Ladder cost on basis D (`oct20/forward/scripts/fwd_lib.py` `cost_D`, $50,000 at each holding's own
maturity, curve treated as the 1 Jan 2027 curve). MODEL. Reproduces the 20 Oct figure ($298,216) exactly.
Script `oct23/tna_now/scripts/ibtr_test.py`, output `oct23/tna_now/ibtr_test_out.csv`.

| Close | Cost (D) | Room vs $300,000 | 10y vs 6 Oct | 20y | 30y |
|---|---|---|---|---|---|
| 6 Oct | $293,453 | $6,547 | 5.27 | 5.68 | 5.64 |
| 20 Oct | $298,216 | $1,784 | -0.15 | -0.21 | -0.22 |
| 21 Oct | $298,004 | $1,996 | -0.14 | -0.21 | -0.22 |
| **22 Oct** | **$302,863** | **-$2,863 (crossed)** | **-0.31** (4.96) | **-0.36** (5.32) | **-0.35** (5.29) |

- **Crossed $300,000? Yes, on the 22 Oct close** (first time since the notes were filed). Cross-check on the coupon basis
  (`cost_M1`): 20 Oct $299,370, 21 Oct $299,128, **22 Oct $303,994**, also over. Log-DF interpolation differs by under $5.
- **10-, 20-, 30-year all fell ≥0.20 points since 6 Oct? Yes** on 22 Oct (-0.31 / -0.36 / -0.35). On 21 Oct only the 20y and 30y had (-0.21 / -0.22); the 10y was -0.14.
- Limits: one day's close; the test runs "by January", so this is a dated observation, not the final result. The 23 Oct close
  is not posted yet. The team's rule is to quote no dollar level. Any use must give the date (22 Oct close).

## Do before submitting (ranked; false items first)
1. **VT: remove the false "7.5% per JPMorgan"** (use the IPS's 7% or no forecast), and tie the upper bound to VT's 2031 value, not its expected return.
2. **IBTM: remove "has a clear yield" and "matures on a set date"**; whatever replaces them must agree with the filed note ("the final payout is not fixed").
3. **Slot 1: fix the heading** so it names the security whose note is pasted (B-T-3.125-15112041), or paste the note that matches the heading. Wharton verifies notes against trades.
4. **Slot 1: the reflection is empty.** Team decision now: keep Nov-41 or restore IBTR.
   - IBTR facts: the note's own test crossed on the 22 Oct close (above), with no trade needed because the rule already sends the gap to the 2028 deposit and the floor. That is the "tested" evidence the TNA is marked on. A restored IBTR reflection must avoid the old false lines (items 3 and 6).
   - If Nov-41 stays: it must answer the three prompts (why, fit with strategy, client goal), and not rely on "no iBonds 2037-43" until a student checks it.
5. **IBTM: remove the absolute** "a stock crash will not make her promise fail". The protection must be stated as the IPS states it (minimum quoted rounded down from a Treasury holding she owns; credibility).
6. **VT: say which portfolio the 9% is** (WInS book; about 7% of Laura's plan) and keep it consistent with the IPS "under one tenth".
7. **IBTM: fix "one of the two roots"** so the metaphor matches the IPS and the other reflections.
8. **Paste hygiene:** do not paste the heading labels, "(Ray)", or the prompt bullets now inside the VT block. Copy notes from WInS or the export table, never from the "## VT" working section ("here").
9. Score gains if time allows (each reflection has 23-29 words of room): one decision that changed (IBTM: floor quoted rounded down because the payout is not fixed; or VT: about 75% stocks to under 10% after modelling showed payment shortfalls), one specific downside for VT, and liquidity once (maturities, not sales, fund each payment). Ladder-first order in IBTM.
10. Recount every reflection by spaces after the edits: ≤100 required, aim for ≤95. A second student checks each pasted note against WInS character by character.
