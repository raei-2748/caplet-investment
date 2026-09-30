# D6: what share of the stock fund Laura promises in 2031

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws2.md`, coupon checks s9-s10 on both builds).
Keys: `rab/numbers_ws2.yaml` (W), `rab/numbers.yaml` (N).

**Decisions. (1) Keep half. (2) A coupon shortfall is paid by Laura's half first, then the gift above the floor,
then the floor** (WS3 stress rule 3, as in WS6's IBTM_R). Decide (2) with (1) at the 26 Oct meeting, after WS2
re-runs D6 with costs (Gate D moved (2) off the 1 Oct vote: no Friday trade depends on it, so order 5's note on
Friday is IBTM_P and IBTM_R is not typed; `rab/redteam/triage.md`).

**Question.** The 2031 top is the floor plus a share of the stock fund (about $41,000 in 2028,
N `laura.stock_fund_2028_usd.strips`); the 2033 gift is capped there and Laura keeps the rest. Is half right, and
who pays if coupons on the ten holdings earn too little?

**Options** (three return models: fat tails, history, uncertain mean; W `ws2.d6.options`)

| Share promised | Expected gift | Laura keeps at least 10% of her gift | She keeps, in a 1-in-20 bad case |
|---|---|---|---|
| 1/3 | about $166k | 98-99% of paths | about $21k-$22k |
| 0.47 (rule's exact answer) | about $173k | 95-97% | about $16k-$18k |
| **1/2 (adopted)** | **about $174k** | **93-95%** | **about $15k-$17k** |
| 2/3 | about $183k | 69-71% | about $10k-$11k |
| all | about $199k | 17-21% | $0 |

**Evidence**
- **Rule fixed before any result** (`M4_SPEC.md` s5, commit 3d98ce0): the gift stays above the announced $145,000 in
  99.5% of paths; Laura keeps at least 10% of her gift (about three years of Taiwan building-cost rises) in 95%; take
  the largest share passing in all three models; change "half" only if it falls outside 0.40-0.60.
- **Result:** 0.50, 0.47, 0.47, so 0.47 (W `ws2.d6.s_star`), confirmed blind and on 10 more seeds. No path puts the
  gift below $145,000 at any share (W `ws2.d6.p_gift_below_145k_any_share`). Half adds about $1,500 of expected gift
  over 0.47 (W `ws2.d6.half_vs_047_expected_gift`) but passes the 10% test only under fat tails.
- **Coupons** (checked after the rule; W `ws2.d6.gap_owner`). The rule assumes zero-coupon STRIPS; under our rule
  reading (`rab/assumptions.md` R1) Laura's real ladder is Book L, which pays coupons. WS7 found three owners for a
  shortfall across the kit; we tested all three on both builds. Adopted owner, with the whole-fund-first runner-up:

| Coupons earn | Gap, rung by rung (2031 value) | Largest passing share: adopted / whole fund first | 2031 top lowered (adopted) | Gift below $145,000 (adopted) |
|---|---|---|---|---|
| The curve's forward rates | about $500 | 0.45 / 0.46 | never | never |
| Today's yields | about $1,500 | 0.42 / 0.45 | never | never |
| 2 points lower | about $17,000 | none / none | 7-10% of paths | at most 1 path in 300 |
| 2% | about $29,000 | none / none | about 7 in 10 | 1-3% of paths |

  Rung by rung ignores what later bonds deliver above $50,000 (about $4,900 at today's yields). With the adopted
  owner, half survives a 2031 gap up to about $2,200 (whole fund first: about $4,700; W `ws2.d6.gap_owner_tolerance`).
  At 2 points lower no share passes under any owner, not even zero: the share is not the lever.

**Decision.**
1. **Keep half:** the simple share nearest the rule's answer; it never breaks the promise; it stays inside the band
   with Book L at today's yields (0.42, both builds); it matches the IPS ("The other half remains with Laura as a
   cushion").
2. **Owner chain (WS3 rule 3):** Laura's half first, then the gift above the floor, then the floor. In 2031, value
   the holdings against the payments and lower the top by any gap her half cannot cover. From the 2033 gift to the
   last payment she holds her half in Treasuries; beyond it, she adds her own money. Why this, not the whole fund
   first: it keeps the adopted top (floor plus half the fund) unless her half runs out, which never happens at
   today's yields, whereas the whole fund first lowers the top for every dollar of gap. It uses the IPS's existing
   cushion sentence, and it gives WS2, WS3 and WS6 one owner. The cost: Laura's cushion takes coupon risk first.

**Confidence.** High that the rule gives half on its zero-coupon basis (two builds, 11 seeds). Medium with Book L at
today's yields (0.42, just inside the band). Medium on the rule itself: "10% in 95% of cases" is a value judgement.
Low if coupons earn 2 points less for years.

**What would change it**
- **A 2031 gap above about $2,200:** the rule stops picking half. Fix the holdings (lower-coupon bonds where WInS
  lists them, coupons into same-date Treasuries), not the share.
- **The team puts Laura's cushion first:** the whole fund first keeps half more securely (0.45) and, at 2 points
  lower, leaves her 10% in about 7 paths in 10 instead of 4-5. It lowers the top and costs about 10 IPS words.
- **Yields falling after 2031:** not modelled. WS7 reports a Japan-style case where her half is too small (not
  Gate-B checked).
- **Laura's cushion** (W `ws2.d6.rule_sensitivity`): 5% gives 2/3; 15%, or 10% at 99% confidence, gives 1/5.
- Costs over 1% a year or charged to the floor; stocks and yields falling together (not modelled).

**Implications**
- **IPS: fix-before-6-Nov, no new item.** The share: none. The owner: WS3's three words in the cushion sentence
  ("if coupons earn less"), next to the Gate A coupon fix of "needs no rebalancing" (`rab/assumptions.md` C3). The
  team chooses the words; the 17 spare words are shared with the cost clause.
- **WS6: IBTM_R is not typed on Friday (Gate D).** If the policy is adopted by 26 Oct, it goes in the IPS and the
  Final Report, not a WInS note. Its owner is right. "Cover any gap" is not: at 2% her half runs out and the gift
  falls below $145,000 in 1-3% of paths. Name her half as the first cover.
- **Final Report: note-in-Final-Report.** The options table as the reason for half; the cushion as the question for
  Laura; the coupon table with both owners; a shortfall makes a small part of the payments depend on stocks
  (qualifies `rab/assumptions.md` E3).
- **Trading Notes.** No shares, odds or ranges in WInS notes. The VT note may say only half the fund is promised.

v5 adopts WS3's rule 3 (ad74847) as the owner after testing all three (gate_B_ws2.md s10); v4 had briefly chosen the
whole fund first. v3 added the Book L check; v2 corrected "19 in 20 at half" to 93-95%.
