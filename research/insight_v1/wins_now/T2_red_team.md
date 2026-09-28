# T2 red team: attacking the trading-now brief and WInS ticket v1

Agent T2 (adversarial red team), insight_v1 run, written 2026-09-28 (about 01:10-02:00 UTC, before the season's first
U.S. open at 13:30 UTC). Files attacked: `research/insight_v1/phase_D/trading_now_brief.md` ("the brief") and
`research/insight_v1/wins_now/securities_and_allocation_v1.md` ("the ticket"), both by T1.

**Serves:** WInS trading as the source of the Trading Notes (TN, Oct 23) and the IPS consistency points that depend on
it (IPS, Nov 6). No Final Report work (brief s17). **Status:** PROVISIONAL, AI-generated research (findings,
evidence, fixes). It contains no note, reflection or IPS text; every fix below is a specification change to T1's
files. The six students decide and write every word. No relayed user messages arrived during this task. Nothing was
committed.

**Every ticker named here is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (brief s14): listed in the team's WInS
account, and inside the Session Rules position limit. Alternates are the ticket's (section 12) unless stated.

**Labels:** VP = verified on the primary page; VRF = verified in a repo file (path given); SNIP = snippet or secondary;
ASM = assumption or model output, not a forecast; INT = interpretation (a judgement); DER = derived by the T2 script
from labelled inputs.

**Script:** `.venv/bin/python research/insight_v1/scripts/T2_red_team_checks.py` (run from the repo root; sections
[1]-[7] are cited below). I also re-ran `T1_ticket_v1_numbers.py`: every figure in the ticket reproduces.

**Terms:** *hedge / promise money* = the Treasury funds standing in for the ten $50,000 payments. *Growth money* = what
the payments do not need. *Float* = uninvested cash kept for commissions. *Gap* = the price jump between the last close
and the next open. *Position limit / cap* = the most WInS allows in one security. *bp* = 0.01 percentage point.

---

## Summary

**Verdict:** the ticket's arithmetic, rule compliance and day-trading discipline hold (section "What survived"). The
plan survives a single trading session under option (ii) as written. It does **not** yet survive one under option
(iii): its "named third trade" can disappear or fail at the fill. Two decision tables the team will vote on are
also tilted by stale evidence: T1 did not apply audit corrections that were already in the repo.

20 findings: **1 blocking** (option (iii) only), **7 important**, **12 minor**.

| # | Severity | Serves | One line |
|---|---|---|---|
| 1 | **blocking (option iii only)** | WInS-now, TN | The (iii) T-bill "third trade" vanishes if rates fall ~12-16bp before the fill, and can fail for lack of cash if all orders go in before the open |
| 2 | important | WInS-now, TN, IPS | The 50/50 case quotes D6's rule as "picks 50% under both houses"; after its audit (AY1 C1) it picks 55-65% with no fee |
| 3 | important | WInS-now, TN, IPS | The (ii)-vs-(iii) table leaves out the strongest official hint for (iii), one criterion for (ii), and overweights the TN for semifinal selection |
| 4 | important | TN | Under (iii) with no listed rung, the three notes show only two investment decisions (TN guide asks for three) |
| 5 | important | WInS-now, TN, IPS | Option (ii)'s VGSH order and note lock in two choices the D3 audit (AX1 C6, C18) has reopened |
| 6 | important | WInS-now, TN | The 300-character plan: mixed evidence, no zero-risk check, no trim order, and the (ii) promise note's required phrases use ~258 characters |
| 7 | important | TN | The reflection checklist says "at most one number" but the "tested" reflection needs three |
| 8 | important | TN, IPS | Paste-ready clauses and AI-coined labels sit in the ticket; notes are permanent and quoted exactly |
| 9-20 | minor | as marked | Continuous-limit omission, missing IEF alternate and labels, rung mechanics, band denominator, unbranched Session Rules outcomes, over-broad ban, one overclaim, IPS-consistency gaps, a generic growth fact, timing/label gaps, stale notes and citations |

---

## What survived the attack (keep)

- **Arithmetic** (DER, script [1]; VP prices of 2026-09-25): every order reproduces with whole shares. (ii) 60/40:
  IEF 783 / TLH 1,365 / VT 384 / VGSH 651 shares, cash left $3,024 after $100 of commissions. (ii) 50/50: VT 318 /
  VGSH 833, cash $3,104. (iii): IEF 1,163 / TLH 2,027 / SGOV 45, cash $1,444 after $75. Cap branches, share counts,
  the TLH-missing weights (IEF 40.9 / TLT 25.1; IEF 60.7 / TLT 37.3), the VTI/VXUS split and the $18 vs $25 T-bill
  economics all reproduce (T1 script re-run).
- **Rule compliance** (VP rules via brief s14): every planned order is cash, an ETF or a U.S. Treasury; none is
  leveraged, inverse, crypto-linked or an ETN; every price is above $5; the largest order is under 0.2% of the
  2x-volume cap on published volumes (AX2 C5); commissions fit; no margin is planned (but see finding 1 on gaps).
- **No day trading planned:** every first-session order is a buy. The later trades the ticket allows (a split
  decision, a duration re-mix, a limit response) involve different securities or later days, and the ticket bans
  same-day round trips and same-day "fixes" (User Guide p.6 "Day Trading: This is not permitted", VP via A4).
- **The gate** (five boxes), the cap-branch table, the calendar and time-zone conversions (Oct 4 AEDT start; Nov 1
  U.S. change; Oct 23 5 p.m. ET = 8 a.m. Sat AEDT), "menu, not quota" for supported/tested/refined, no planned
  rebalance trade, no Laura quotes in notes, the statistics degree out of the VT note, and the banned-word lists all
  match the audited specialist files (D7/AY2, D9/AY2, D2/AX2, S4).
- **Scope:** no Final Report narrative, chart specs or Works Cited plans. Section 11 of the ticket keeps only rule
  content the IPS needs (brief s17 allows that).

---

## Findings

### 1. BLOCKING (option iii only): the named third trade is fragile in two independent ways
**Evidence.**
- The ticket fixes the (iii) hedge at 98% ($294,000) because the Nov-15 STRIPS ladder cost $294,387 on the
  **Sep-25** curve (ticket L77, ASM on a VRF curve). The T-bill leg is whatever is left: about $4,538 after a $1,000
  float and 3 commissions.
- Re-priced for a parallel move before the trade date (DER, script [2]; ladder prices from S4 finding 9, ASM): the
  T-bill leg falls under $1,000 after a **12.2bp** fall, reaches zero after **15.7bp**, and the ladder exceeds $300,000
  after **19.3bp**. With 2026's realised 4.45bp/day (D7, VP data; driftless normal ASM), the chance of a fall that
  shrinks the leg under $1,000 is about **11% by an Oct 2 fill and 19% by the Oct 9 hard stop**; the chance that no
  leftover exists at all is about 6% / 13%.
- In that case the literal January-2027 book has **no leftover**, so a SGOV/BIL note saying the leftover "waits for
  the 2028 deposit" would state something false at that date's prices, in a permanent note. If the team instead keeps
  98% / $4.5k as printed, the book is no longer the literal January-2027 book the IPS will name.
- **Cash at the fill** (DER, script [3]): orders entered while the U.S. market is closed fill at the next open
  (Trading Details R-W62, VP; R-W72: teams "are not expected to stay awake"). Sized at the last close, the (iii)
  orders cost about $291 more per 1bp fall at the open. The $1,444 float is used up by a **5bp** overnight fall
  (about 13% of days; about 29% if the share counts are left at the Sep-25 closes and filled on Oct 1). The T-bill
  order is entered last, so it is the order most likely to be rejected, or to push cash negative (margin is banned,
  VP). Either way (iii) is back to the two-trade problem that AX2 called blocking (D10 C1).
- Option (ii) is not exposed: its float ($3,024-3,104) survives about a 12bp fall plus a 1% stock rise, if the share
  counts are recomputed from the last close (about a 0.4% chance of failing; 8-9% if the Sep-25 counts are used).

**Exact fix** (ticket section 2 and brief s2 item 2; before any (iii) order):
1. Replace "The hedge is 98% of the book" with: under (iii), on the trade date re-price the ladder with
   `D9_numbers.py [3]` or `A2_curve_recheck.py`; hedge = that cost; T-bill leg = $300,000 minus that cost minus the
   $1,000 float minus commissions.
2. Add a pre-set rule: if that T-bill leg is under $1,000 (rates about 12bp or more below Sep 25), (iii) has no genuine
   third trade unless a dated rung is listed (section 7); then the gate vote reverts to (ii). Never buy a token sliver.
3. Add to "When": under (iii), enter IEF and TLH first; enter the T-bill order only after both show "Filled", sized to
   the cash actually left (same U.S. session if someone is awake, otherwise the next one; it is still the plan's rule,
   not a note-making trade). Under both options, recompute share counts from the last close before entering orders.
4. SGOV/BIL note, element C3: the leftover as a dollar amount at the trade-date price, never "about 2%".

### 2. IMPORTANT: the 50/50 case misstates D6's rule after its audit, and T1 missed three audit sections
**Evidence.**
- Brief L133-135: D6's rule "picks 60% under JPM and 50% under Vanguard's midpoint. Applied under both published
  forecasts, it picks 50%".
- AY1 C1 on D6 (VRF, `D6_behavioural.md` audit section; `audit_client_cosponsors.md` L54-56): on a 5-point grid the
  same rule picks **60% (JPM, 4% bonds), 65% (JPM, 5% bonds), 55% (Vanguard midpoint), 65-70% with fat tails**, 55-60%
  with a 0.5% fee and 50-55% with a 1.0% fee. "The rule gives a checkable reason for a choice in the 50-70% band; it
  does not confirm 60%." The 50% reading is a 10-point-grid artefact.
- E1 (`phase_E/E1_change_proposals.md` P5, written after T1, not yet audited) reaches 50% under both houses **only with
  a fee of up to 0.5%**; with no fee both central cases give 55%. The case is silent on fees and the fee clause is "the
  first thing to cut" (D8 AY2 item 13, VRF).
- The 60/40 side also omits D3 AX1 C4 (VRF, D3 audit section): medians understate what equity is expected to add.
  Under JPM the *mean* gain of 60% sleeve equity over an all-Treasury benchmark is $6.5-9.4k against a median of about
  $3k; under Vanguard's midpoint it is about zero. It does not decide 50 vs 60, but it belongs on the scale.
- Cause: brief L172-173 says "D5, D6, D12 and D3 had no appended audit section" and `audit_rates_D1.md` "was not in the
  repo". File times (VRF, `ls --time-style=full-iso`, 2026-09-28) show the AY1 sections on D5, D6 and D12 and
  `audit_rates_D1.md` saved at 00:34-00:37 UTC, 11-14 minutes **before** T1's files (00:48). Only D3's AX1 section
  (00:57) came later.

**Exact fix** (brief section 4; before the VT note is drafted, because a note may record "how the split was set"):
- Replace L133-135 with: D6's rule (AY1 C1) gives about 55-70% depending on inputs: 60-65% under JPM, 55% under
  Vanguard's midpoint, 50% only if a 0.5%+ yearly fee is assumed. It is a reason for a choice in the 50-70% band and
  does not separate 50/50 from 60/40.
- Keep the 50/50 case on D2's evidence alone (flat median across houses; p5 +$6-7.5k; p95 -$11-14k; 2031 floor p5
  +$5-6k). Add AX1 C4 (mean vs median gain) to the 60/40 side.
- Update L172-173, re-read the AY1 sections on D5, D6 and D12 and the AX1 section on D3, and list what changed.
- Never let a note or the IPS say the rule "picks 50% under both forecasts" unless the fee assumption is stated.

### 3. IMPORTANT: the (ii)-vs-(iii) table is not balanced
**Evidence.**
- Missing for (iii): Wharton set WInS cash equal to Laura's first deposit, and "The additional $150,000 contribution
  ... will not be added to WInS" (R-W56, R-W59, VP). S4 finding 5 (VRF): read literally, this and the case's "It does
  not determine Laura's actual portfolio value at the beginning of 2027" support (iii) "at least as much as (ii)"; WInS
  runs on the eve of the January 2027 purchase. D10 1.4 (VRF): (iii) shows the plan's central priority in the holdings
  themselves.
- Missing for (ii): the Investment Strategy criterion "uses appropriate diversification" (SMApply L49, VRF) and
  SMApply's own list of diversification kinds, which includes "funding purposes" (R-W71, VP). Only (ii) shows three.
- T1's first reason for (ii) (brief L117) is that the TN is "the first judged deliverable". The Rules & Roles page says
  the Top 50 are chosen on "the strength of their Investment Policy Statement (IPS) and Final Reports" (VP; conflict
  X-8 in `phase_A/case_register.md`). The TN's weight in semifinal selection is uncertain, so (iii)'s IPS economy
  (12-20 words vs 25-40; the IPS barely fits, AX2 C3) may count for more than the brief implies (INT).

**Exact fix** (brief section 3 table): add two rows, "Official hints" and "What the holdings show on their own", with the
points above on each side. Re-word L117 to "The TN is scored (SMApply, case) but may not count for semifinal selection
(Rules & Roles, X-8); if it does, (ii) gives three roles". Keep T1's lean if it still holds after the rows are added.

### 4. IMPORTANT (option iii): three notes, but only two investment decisions
**Evidence.** The TN guide asks the team to "select three investment decisions that best illustrate your team's
strategic thinking" (L11, VRF) and to show "a cohesive portfolio strategy" (L14-15). Under (iii) with no listed rung,
the ticket's slots are TLH, IEF ("weaker, same role", ticket L121) and SGOV. IEF and TLH are one decision (a
duration-weighted pair bought together); a reader sees two notes with the same need, fact type and rule. D12 (VRF)
already said (iii) notes can differ only by supported/tested/refined, not by role.

**Exact fix.** Brief section 3, column (iii), row "Trades before Oct 23": add "without a listed rung: three trades
but two decisions (TN guide L11)". Ticket section 4 slot B under (iii): "the dated rung if listed; otherwise the team
must accept, at the gate vote, that two notes describe one decision". Record that acceptance in the decision log.

### 5. IMPORTANT (option ii): the VGSH order and note pre-commit two choices the D3 audit reopened
**Evidence.** D3's AX1 section (VRF, saved after T1): C6 "The barbell is not dominated" and adds a team choice for the
IPS: "Is the facility floor bought in January 2028 or January 2031?"; C18 logs "VGSH or a dated Dec-2032 Treasury fund
for the growth money's bonds?" as an open question. Under (ii), the ticket buys VGSH now and its note element C2 is
"the kind of asset a later promised amount can be built from" (ticket L148), which assumes a floor bought later from
short Treasuries. Notes are permanent and must be consistent with the IPS (TN guide L30-31, VRF).

**Exact fix.** Gate box (b), if (ii): the team also records "floor bought in 2031, growth-money bonds in short
Treasuries" (or its alternative) before the VGSH order. If it has not decided, the VGSH note uses only the
"facility contribution and flexibility" need, with no reference to a later promised amount. Add both questions to
the IPS "rules to fix before Nov 6" list (owner: ips_spec).

### 6. IMPORTANT: the 300-character plan needs a zero-risk check and a trim order
**Evidence.**
- AY1 C2 on D12 (VRF): the 300 cap comes from a sister product only; Wharton's own 413-character example is counter-
  evidence; "Verify at zero risk before the first real note" (ask Stock-Trak Live Chat or Wharton, or type a long
  test text on the order-review screen and do not press Confirm). The ticket's check is made while typing the first
  real note (brief L40; ticket check 8), and the first note is the promise note, the longest.
- The ticket's own required element phrases for a (ii) promise note (role word, label, need, scaling marker, dated
  research fact with source, rule) use about **258 characters before any connecting words** (DER, script [7]; phrases
  taken from ticket section 5, not a drafted note). That leaves about 40 characters for grammar under a 300 cap.
- AY1 C1 on D12 (VRF) sets a priority: need, alignment, research, role word; "the risk accepted moves to the
  reflection if space is short". The ticket keeps C4 (risk/rule) in the core and gives no trim order.

**Exact fix.** Gate box (c): add AY1 C2's zero-risk test before any order. Ticket section 5: add a trim order for any
note over the limit: keep C2 (need, with the (ii) scaling marker) and C3 (dated fact) and the Guide role word; move C4
and the team label to the reflection. Keep "promise money first" as the order of entry (D7 uses the time stamps as
evidence of promise-first); do not reorder trades to test the box.

### 7. IMPORTANT: the reflection checklist contradicts itself
**Evidence.** Ticket L157: "At most one number". Ticket L158-160: a tested reflection carries the rate move in bp, the
hedge's % change and the payments' % change, which is three numbers. D7 AY2 C15 (VRF) fits those three inside the
official questions in about 20-25 words.

**Exact fix.** Replace L157 with: at most one number, except a "tested" reflection, which carries exactly three (bp
move; hedge % change; payments' % change), each dated, and labelled as the team's own calculation from the WInS screen
and the treasury.gov curve (D3 AX1 C7, VRF).

### 8. IMPORTANT: paste-ready clauses and AI-coined labels in a ticket for permanent notes
**Evidence.**
- The ticket says it "contains no note, reflection or IPS text" (L11), but section 5 contains complete clauses a
  student could type into WInS unchanged: "A fall shrinks the facility range, never the payments." (L147); "Never sold
  after a rate rise (the payments got cheaper too); only re-mixed to keep about 10 years" (L146); "Held to maturity, so
  later prices do not change what it repays" (L150).
- D9 AY2 C4 and D7 AY2 C13 (VRF) classed the same pattern as important: a template the team fills in "becomes
  AI-written text in a submitted deliverable" (Wharton AI policy: students "must use their voice and words", VP via
  A4). Notes are quoted "exactly as it appears in WInS" (TN guide L44, VRF) and cannot be edited.
- The fixed labels ("promise money", "growth money", "short-Treasury part of the growth money", "the 2027 leftover")
  are D9's proposals ("INT: proposal, the team may rename", D9 M001, VRF). The brief presents them as fixed (L75).

**Exact fix.** Ticket section 5: recast each quoted clause as an element in noun phrases (for example "risk element:
what a stock fall changes (the facility range) and what it does not (the payments)"), and mark every remaining phrase
"illustrative, do not copy". Brief item 5: "the team chooses its own label words (D9's are proposals) and logs the AI
source". Gate box (d): the second student checks that no clause in the draft repeats ticket wording.

### 9. MINOR: the continuous-limit check ignores a stock fall
**Evidence** (DER, script [5]; ASM that WInS re-checks the limit as prices move): under (ii) at a 25% cap, TLH placed at
24% crosses 25% after a **20%** stock fall (60/40) or **24%** (50/50) with rates unchanged, or after only a **10-12%**
stock fall combined with a 50bp rally (a typical flight to safety). Ticket L106 names only a 101bp rate fall.
**Exact fix.** Add the stock-fall path to L106-107. The rule "never add to a position near the cap" is unchanged.

### 10. MINOR: IEF has no alternate in v1, and the brief carries no availability label
**Evidence.** v1 supersedes v0 for trading (ticket L4) but dropped v0's substitute table: TLH, SPTL, VT, VGSH and SGOV
have alternates, IEF has none (v0 section 6 had VGIT, then SPTI). The brief names tickers throughout and never carries
the "PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK" label (0 occurrences, DER).
**Exact fix.** Ticket section 12: add "IEF alternate: VGIT (4.9y), then SPTI (4.78y); re-solve with the section 10
formula using the substitute's duration". Brief: one label line under the title.

### 11. MINOR: dated-rung mechanics
**Evidence.** "Fund it from IEF" (ticket L176) is wrong for rows 2-3: re-solved with the ticket's own formula, a
2039/2040 bond lowers TLH more than IEF. The IBTM row (L185) gives no IEF/TLH split or cap rule: it leaves TLH at about
**67.8%** under (iii) and **45.7%** under (ii) (DER, script [6]; IBTM 5.05y VP), so it breaks the same caps as row 1.
If a rung is added after IEF/TLH have filled, "funding" it means selling them, which must never happen on their fill
day (day-trading rule, VP).
**Exact fix.** Replace "Fund it from IEF" with "size IEF and TLH after pricing the rung in the drop-down, in the same
session, from the formula". Copy row 1's cap rule to row 3. Add: "a rung found later is bought with a separate
re-mix on a later day; never sell a fund on its fill day".

### 12. MINOR: the growth band's denominator is undefined
**Evidence** (DER, script [1]): at 60/40 VT is 62.1% of VT+VGSH but 60.3% including the cash float; at 50/50, 51.5% vs
49.9%. The 55-65 band starts 2.9 points from its top on the first reading. D3 AX1 C17 (VRF) found the same convention
gap.
**Exact fix.** Ticket L73: "VT ÷ (VT + VGSH + cash float); starts at about 60% or 50%".

### 13. MINOR: two Session Rules outcomes have no branch
**Evidence.** "Teams must meet the required trading activity and portfolio management guidelines" (Rules & Roles, VP)
is undefined publicly; a Stock-Trak setting may cap a whole security type (A4 f.1 asks to record it). The plan's
low-trade design has no branch for either.
**Exact fix.** Gate box (c): "If the logged-in pages show an activity minimum or a cap on a whole security type (all
ETFs, all bonds), stop and ask Wharton (Contact Us) before any order; never add trades to meet a count".

### 14. MINOR: "reduce volatility" is banned for the one fund it describes
**Evidence.** The ban covers all WInS funds (brief L68; ticket L146). For VGSH, the ticket's own C3 number (the growth
money falls about 10-12% instead of 20% in a 20% stock fall) is exactly lower volatility, and Wharton's example note
uses the phrase (TN guide L36, VRF). The ban is right for the promise money (S4 finding 7, D9 M012).
**Exact fix.** Scope the ban to the promise money; for VGSH allow "lowers the growth money's swings" only with the
number beside it (AY1 C10: it is the ordinary effect of holding Treasuries, not a VGSH property).

### 15. MINOR: one overclaim in decision 1
**Evidence.** Brief L21: "the only design whose certainty rests on today's prices". The ladder is bought at January 2027
prices, and in about 1 in 3 rate paths part of it waits for the 2028 deposit (AX1b item 1, ASM; brief s16).
**Exact fix.** "whose certainty rests on market prices on the purchase date, not a forecast (and, in about 1 in 3 rate
paths, partly on the 2028 deposit)".

### 16. MINOR (IPS consistency): three gaps between permanent notes and the IPS spec
**Evidence and exact fixes.**
- (a) D10 1.5 (VRF) requires the IPS date sentence to say WInS holds **stand-in funds, not the ladder**, under either
  option. Brief section 3 "Words needed" omits it. Add it to both columns.
- (b) Under (iii), the SGOV note depends on the rule "any leftover waits in T-bills until 2028" (D1 M004 rule 7). AY2's
  IPS word budget (`audit_judges_practice_comms.md` s5, VRF) has no line for it. Add "(iii) only: T-bill leftover
  clause, about 8-10 words" to the budget handed to ips_spec.
- (c) D13c N1(e) (VRF) says "either way" one reflection answers "why so little equity?". The ticket asks for it under
  (iii) only (L125, L163). Under (ii), at 17-20.5% stocks, add to the growth reflection checklist: risk stated goal by
  goal (promise money: no stock risk; growth money: the chosen share), as E1 P6 also proposes.

### 17. MINOR: the growth note's research element is the most generic one available
**Evidence.** Ticket L147 offers VT's stock count and top-ten share: any team can cite them. The Laura-specific, dated,
checkable market fact is the rate the Treasury curve implies for her 2028-2033 growth-money dates, about 5.2% a year
(D2 E2 with AX2 C1: "market-implied, not locked"; VRF curve), which is what the stock share must beat.
**Exact fix.** Add it as the first C3 option for the growth note, with the words "implied by the [date] curve" and the
existing ban on "known/locked".

### 18. MINOR: timing and labelling details for the "tested" evidence
**Evidence.** The chance of a 10bp or larger move from the fill to the Oct 20 close is about 52% for an Oct 2 fill but
about **40%** at the Oct 9 hard stop (DER, script [4]; ASM). The brief says earlier fills give "more days" but not
how much the test weakens. Brief s14 still says "use spot duration (10.16y)" while the ticket targets 9.90 on issuer
numbers; S4 finding 8 (VRF) reconciled them but its one line was never added.
**Exact fix.** Brief timing paragraph: add the 52% vs 40% figures. Ticket header: add S4's line "9.90 on issuer
durations is about 10.1 in full revaluation, close to the 10.16 spot duration".

### 19. MINOR: model prices shown as prices
**Evidence.** "$294,387" and the (iii) note's "$292-294k at [trade-date] Treasury prices" are par-curve model prices,
not STRIPS quotes (D3 AX1 C25, VRF).
**Exact fix.** Ticket section 5 promise row: "the payments' value on the [date] Treasury curve (our calculation)".

### 20. MINOR: stale notes and one citation
**Evidence and exact fixes.** Brief L172-173 (see finding 2): correct it. Ticket L57 cites "SMApply FAQ" for fills at the
next open; the source is SMApply Trading Details (R-W62, VP). Correct the citation.

---

## The one-session test (does the plan survive if the team trades only once this week?)

| | Option (ii) | Option (iii) |
|---|---|---|
| Orders in one session | 4 buys (5-7 under a cap); all fill at one open | 3 buys (4 with a rung) |
| Three executed trades by Oct 23? | Yes; three distinct roles | Only if the T-bill leg exists at trade-date prices **and** the last order fits the cash (finding 1: roughly 1 in 9 to 1 in 5 that the honest leg is under $1,000; about 1 in 8 that a 5bp overnight fall leaves too little cash if all orders go in before the open; ASM) |
| Three distinct decisions? | Yes | Only with a listed rung (finding 4) |
| Day-trade risk | None (buys only) | None (buys only) |
| "Tested" window | ~52% chance of a 10bp+ move (Oct 2 fill); ~40% at the Oct 9 hard stop | same |
| Needs a second session later? | Only if the split was provisional (decision by Oct 16) or an order was rejected | Only for the fix in finding 1 step 3 |

**Reading (INT):** with findings 1 and 6 fixed, both options survive one session. As written, only (ii) does.

## Sources (accessed 2026-09-28)
- T1 files attacked (VRF): `research/insight_v1/phase_D/trading_now_brief.md`,
  `research/insight_v1/wins_now/securities_and_allocation_v1.md`; script `scripts/T1_ticket_v1_numbers.py` (re-run).
- Inputs read (VRF, with their own labels): `wins_now/securities_and_allocation_v0.md`, `wins_now/S4_red_team.md`,
  `phase_A/wins_week1_guardrails.md`, `phase_A/case_register.md` (R-W56, R-W59, R-W62, R-W71, R-W72, X-8);
  `phase_D/D1_rates.md` (+AX1b), `D2_equity_ai.md` (+AX2), `D3_quant.md` (+AX1), `D5_cosponsors.md` (+AY1),
  `D6_behavioural.md` (+AY1), `D7_wharton_intent.md` (+AY2), `D8_practice.md` (+AY2), `D9_communication.md` (+AY2),
  `D10_compliance.md` (+AX2), `D12_overflow_client.md` (+AY1), `D13c_voice_map.md`, `audit_markets_rules.md`,
  `audit_client_cosponsors.md`, `audit_judges_practice_comms.md`, `audit_rates_D1.md`; `phase_C/survivors.json`
  (M001, M002, M004, M005, M012, M028, M034, M044, M062, M212, M238, M247); `phase_E/E1_change_proposals.md` (P5, P13;
  written after T1, not yet audited).
- Official (VRF): `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L11-16, L30-31, L36-53),
  `2026_WGY_Investment_Competition_Guide.txt` (p.3, p.5), `2026_WGY_Investment_Policy-FINAL.txt` (L73-75),
  `Laura_Gao_2026_Client_Profile.txt` (L61-74, L91-92, L102-103, L129-130), `SMApply_Deliverables_Page_2026-09-27.md`.
- Primary web rules (VP, via Phase A and the audits, not re-fetched by T2): SMApply Trading Details and FAQ; Wharton Rules &
  Roles; 2026-27 WInS User Guide.
- New script: `research/insight_v1/scripts/T2_red_team_checks.py`.

## What this teaches
1. **A fix can have its own failure mode.** The T-bill trade solved "only two trades" on Friday's prices. Re-pricing it
   for a small rate move showed it can vanish, so the fix needs its own rule written down before trading.
2. **Timing is part of the arithmetic.** An order typed in Sydney fills hours later at a new price. A thin cash float
   turns an ordinary overnight move into a rejected order.
3. **Read the corrections, not just the conclusions.** One stale sentence ("the rule picks 50% under both forecasts")
   was enough to tilt a vote. The audit that fixed it was already in the repo, fourteen minutes old.
4. **A fair comparison lists the other side's best argument.** For the WInS book, that argument sits in Wharton's own
   words: the simulator holds exactly her first deposit, and the second one is never added.
