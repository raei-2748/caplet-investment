# D6: what share of the stock fund Laura promises in 2031

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws2.md`, coupon checks s9-s10 on both builds).
Keys: `rab/numbers_ws2.yaml` (W), `rab/numbers.yaml` (N).

**Decisions. (1) Keep half. (2) A coupon shortfall is paid by the stock fund first, the floor last.** Ratify (2) at
the 1 Oct vote (it decides WS6's IBTM_R note) and (1) at the 26 Oct meeting.

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
  shortfall across the kit. We tested the two that differ: the whole fund before the range (WS3 stress rule 3), and
  Laura's kept half in 2033.

| Coupons earn | Gap, rung by rung (2031 value) | Largest passing share: fund pays in 2031 / kept half pays in 2033 | Gift below $145,000 if the fund pays |
|---|---|---|---|
| The curve's forward rates | about $500 | 0.46 / 0.45 | never |
| Today's yields | about $1,500 | 0.45 / 0.42 | never |
| 2 points lower | about $17,000 | none / none | at most 1 path in 400 |
| 2% | about $29,000 | none / none | 1-2% of paths |

  Rung by rung ignores what later bonds deliver above $50,000 (about $4,900 at today's yields). Half survives a 2031
  gap up to about $4,700 if the fund pays, about $2,400 (2033 value) if the kept half pays
  (W `ws2.d6.gap_owner_tolerance`, `ws2.d6.ladder_gap_tolerance`). At 2 points lower no share passes, not even
  zero, so the share is not the lever; if the fund pays, the promise holds, the top falls about $8,500, and Laura
  keeps 10% of her gift in about 7 paths in 10.

**Decision.**
1. **Keep half:** the simple share nearest the rule's answer; it never breaks the promise; it stays inside the band
   with Book L at today's yields under either owner; it matches the IPS ("The other half remains with Laura as a
   cushion").
2. **Owner chain:** coupons buy Treasuries for the same payment (WS3 rule 2). In 2031, before the range is set, the
   stock fund fills any shortfall in the ten holdings at that day's prices (WS3 rule 3). After that, the part Laura
   keeps pays; in January 2033 the gift is cut only if that part runs out, and never below the floor. After the
   January 2033 set-aside, Laura's kept money pays. The floor pays only if a shortfall exceeds the whole fund.
   Why: the range must protect the operating commitment (case), so co-sponsors never hear a top that is later cut to
   pay Laura's payments; half holds more securely; it matches WS3.

**Confidence.** High that the rule gives half on its zero-coupon basis (two builds, 11 seeds). Medium-high with
Book L at today's yields (0.45, both builds). Medium on the rule itself: "10% in 95% of cases" is a value judgement.
Low if coupons earn 2 points less for years.

**What would change it**
- **A 2031 gap above about $4,700:** the rule stops picking half. Fix the holdings (lower-coupon bonds where WInS
  lists them, coupons into same-date Treasuries), not the share.
- **Yields falling after 2031:** not modelled; Laura's part carries it. WS7 reports a Japan-style case where it is
  too small (not Gate-B checked).
- **Laura's cushion** (W `ws2.d6.rule_sensitivity`): 5% gives 2/3; 15%, or 10% at 99% confidence, gives 1/5.
- Costs over 1% a year or charged to the floor; stocks and yields falling together (not modelled).

**Implications**
- **IPS: fix-before-6-Nov, no new item.** The share: none. The owner: fold into the Gate A coupon fix of "needs no
  rebalancing" (`rab/assumptions.md` C3), e.g. "any shortfall is filled from the stock fund before the range is set"
  (the team's words). With the cost clause and WS3's rules 1-2 this exceeds the 17 spare words: trim elsewhere.
- **WS6: fix-now if IBTM_R is typed.** It says the half Laura keeps, "not the floor, cover any gap". "Not the floor"
  is right; "the half she keeps" and "any gap" are not: the whole fund pays first, and at 2% the gap exceeds the
  fund in about 3-4% of paths.
- **Final Report: note-in-Final-Report.** Options table as the reason for half; the cushion as the question for
  Laura; the coupon table and owner chain; a shortfall makes a small part of the payments depend on stocks
  (qualifies `rab/assumptions.md` E3).
- **Trading Notes.** No shares, odds or ranges in WInS notes. The VT note may say only half the fund is promised.

v4 adds the owner chain (gate_B_ws2.md s10); v3 the Book L check; v2 corrected "19 in 20 at half" to 93-95%.
