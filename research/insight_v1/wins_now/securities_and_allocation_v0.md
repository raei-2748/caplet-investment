# Securities and allocation v1: WInS week-1 ticket, and Laura's long-term instrument map

Agent S3 (Allocation Architect), insight_v1 run. First written 2026-09-27; **revised the same day after the S4 red team**
(`research/insight_v1/wins_now/S4_red_team.md`). This is a **PROVISIONAL week-1 recommendation**. The team has not
approved the strategy, and Phases B-E may change it. Everything here is AI-generated research: tables, numbers,
reasons and checklists. None of it is text to submit. The team decides and writes every word, including every WInS
note.

**Every WInS security in this file is PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before
trading.** This season there is no separate approved list; "Any ETF available on WInS" is allowed (SMApply Trading
Details, VERIFIED-PRIMARY, read 2026-09-27). So the check is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK**: is
the ticker listed in the team's WInS account, and does the order fit the Session Rules position limit?

Scripts (run from the repo root):
- `.venv/bin/python research/insight_v1/scripts/S3_allocation_numbers.py` (weights, dollars, share counts, bands;
  section 10 is the capped-hedge rule added after the red team);
- `.venv/bin/python research/insight_v1/scripts/S4_red_team_checks.py` (maturity profiles, forward-consistent tracking).

Moved out of this file: the CUSIP-level STRIPS ladder and the 2033-2042 reserve run-down now live in
`research/insight_v1/wins_now/S3_final_report_ladder_and_reserve.md` (Final Report material, not week-1).

---

## THE TICKET (one page)

### Gate: tick all five before the first order
- [ ] **(a) Team vote on "lock early".** The team has read a short version of the plan and recorded a vote to adopt it
      (or not), with first names and date, in the team's decision log. If the vote is "no", stop: this ticket does not
      apply.
- [ ] **(b) Option chosen: (ii) or (iii)** (section 2), using the stated test, and recorded.
- [ ] **(c) Session Rules screenshot saved** (Portfolio Summary > Session Rules): position limit (single position, and
      by security type if shown), day trading, trades allowed, commissions.
- [ ] **(d) Each WInS note drafted by a student, in that student's own words**, from the checklists below, and read by a
      second student before submitting. Notes cannot be edited after submission (Stock-Trak, via A4).
- [ ] **(e) Position-limit branch picked in advance** (the rule below), so nobody improvises at 11:30 p.m.

**When:** aim for fills in **week 1 once the gate is passed**, for example by **Fri Oct 2 ET**. There is no reason to
rush for Mon Sep 28. SMApply says "The competition does not require frequent or same-day trading" (R-W73,
VERIFIED-PRIMARY), and WInS gains and losses are not judged (R-W75). The "first trade by Oct 10" claim is still
UNVERIFIED: check the logged-in Trading Details page.

### Session Rules branch (decided in advance)
| Single-security limit shown in Session Rules | Hedge orders (share of the $300,000) |
|---|---|
| **44% or more, or no limit** | IEF 23.6% / TLH 42.4% |
| **Under 44%** (any cap from 25% up) | IEF 23.6% / **TLH one point under the cap** / **SPTL the rest of the 66%** (alternate VGLT). At a 25% cap: IEF 23.6 / TLH 24.0 / SPTL 18.4 |

The hedge stays 66% of the portfolio and "about 10 years" in every branch.

### Orders, option (ii), at $300,000 (share counts at 2026-09-25 closes; recompute on the trade date)
| # | Order | Weight | Dollars | ~Shares | Job |
|---|---|---|---|---|---|
| 1 | BUY IEF | 23.6% | $70,744 | ~786 | The promise (hedge), part 1 |
| 2 | BUY TLH (capped: TLH ~771 sh + SPTL ~2,276 sh) | 42.4% | $127,256 | ~1,362 | The promise (hedge), part 2 |
| 3 | BUY VT | 20.5% | $61,500 | ~384 | Growth: 60% of the money the promise does not need |
| 4 | BUY VGSH | 12.5% | $37,500 | ~651 | Short-Treasury part of the growth money |
| | Cash float | 1% | $3,000 | | Commissions; no margin allowed |

All four go in **one session**, hedge orders entered first. Overnight orders all fill at the next U.S. open. Cost: 4-5
trades, $100-125. **Option (iii)** instead: IEF 35.0% / TLH 63.0% / cash 2.0%, with no VT or VGSH (section 2).

### Three note checklists (elements only; the team writes the words)
1. **Hedge note (TLH, or SPTL if capped).** Sized to a specific promise: ten fixed $50,000 payments, 2033-2042, which
   cost about $292k to lock in for January 2027 at today's Treasury prices. TLH's bonds are *closer* to her payment dates than a 20+ year fund's. The
   pair moves like her payments when rates change (about 10 years). The funds stand in for the ladder she buys in
   January 2027. The rule: never sell the hedge after a rate rise. **Never** say the funds "match" the payments, that
   their bonds mature in her payment years, or "stable"/"reduce volatility".
2. **Growth note (VT).** Equity is 60% of the money the promise does not need, not a share of the total. It serves the
   facility contribution and flexibility. One global index: a concentration argument, not a return forecast. The risk:
   a fall shrinks the facility range, never the payments.
3. **Short-Treasury note (VGSH).** A different funding purpose: money that can later become an amount Laura can
   promise co-sponsors before 2033, because it is already owned. Split recorded as provisional (60/40). **No floor
   percentage in the note.**

### Three "never" rules
1. Never sell the hedge after a rate rise (the payments got cheaper too).
2. Never trim the hedge after a rate fall (it grew because the payments cost more).
3. Never day-trade: never buy and sell the same security on the same U.S. trading day ("Day Trading: This is not
   permitted", 2026-27 WInS User Guide p.6, via A4).

---

## Terms used (plain English)
- **Hedge (the "promise" money):** the Treasury funds that stand in for the ten fixed $50,000 payments due 2033-2042.
  Their value moves with the cost of those payments.
- **Growth money (the "sleeve"):** everything the payments do not need. It pays for the facility contribution and for
  flexibility.
- **Duration:** roughly the % a bond fund's price falls if interest rates rise by 1 percentage point. The payments'
  duration is about 10 years.
- **Basis point (bp):** 0.01 percentage point.
- **Position limit:** the most WInS lets you hold in one security, as a share of the portfolio (Session Rules).
- **Twist:** short-term and long-term rates move in opposite directions.
- **Stand-in:** in WInS, funds that behave like Laura's real ladder without being it. The funds never mature; they keep
  rolling into newer bonds.
- **Rebalancing band:** a range around a target. The team trades only when a weight leaves it.

---

## 1. The securities (primary, alternates, facts)
Key facts are from issuer primary pages, **accessed 2026-09-27** (as-of dates in brackets). "Re-read" means S3 opened
the page again during this revision (12:40-12:50 UTC); other facts were read by S3/S4 earlier the same day. 2025-26 list
= `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` (historical only, VERIFIED-REPO-FILE; searched by
ticker and by name, since some lines merge them).

| Role | Primary (PENDING APPROVAL CHECK) | Key facts (issuer page) | Alternates, same type (PENDING APPROVAL CHECK) | 2025-26 list |
|---|---|---|---|---|
| Hedge, part 1 | **IEF** iShares 7-10 Year Treasury Bond ETF | 0.15%; effective duration 6.86y [9/24]; 16 notes maturing 2033-05-15 to 2036-08-15 (S1 holdings snapshot 9/24); net assets $41.57bn; 30-day avg volume 8,830,020; close $90.00 [9/25]. ishares.com/us/products/239456, re-read, VERIFIED-PRIMARY | VGIT (0.03%, 4.9y [8/31], 102 bonds; Vanguard API, re-read). SPTI (0.03%, 4.78y; ssga.com, S1) | IEF yes (#88, line 1053). VGIT, SPTI no |
| Hedge, part 2 | **TLH** iShares 10-20 Year Treasury Bond ETF | 0.15%; 11.59y [9/24]; 61 bonds maturing 2037-02-15 to 2046-08-15, **74.7% of bond weight after 2042-01-01** (S4 script on S1 snapshot); $10.53bn; 1,969,419/day; close $93.38 [9/25]. ishares.com/us/products/239453, re-read, VERIFIED-PRIMARY | TLT (0.15%, 14.88y, 47 bonds maturing 2044-05-15 to 2056-08-15; $45.75bn; re-read). SPTL/VGLT (below) | **TLH no**; TLT yes (#87, line 1041) |
| Hedge, part 3 **only if capped** | **SPTL** State Street SPDR Portfolio Long Term Treasury ETF | 0.03% gross [8/31]; option-adjusted duration 13.65y [9/24]; 110 holdings; Bloomberg Long U.S. Treasury Index (10+ years); AUM $10,949.50M [9/24]; prior-day exchange volume 1,088,651; close $24.27. ssga.com (spdr-portfolio-long-term-treasury-etf-sptl), re-read 12:42 UTC, VERIFIED-PRIMARY | VGLT Vanguard Long-Term Treasury ETF (0.03%; 13.5y [8/31]; 101 bonds; $15.1bn; price ~$50.94 [9/25]; Vanguard API, re-read) | SPTL, VGLT no |
| Growth | **VT** Vanguard Total World Stock ETF | 0.06% [as of 2026-02-27]; 10,088 stocks, 37.7% non-U.S. [8/31]; FTSE Global All Cap Index; fund total net assets $101.7bn [8/31]; market price $160.03 [9/25]; top-10 21.7% [fact sheet 6/30, S2/S4]. investor.vanguard.com/vmf/api/VT, re-read. **Vanguard does not publish volume** (check in WInS) | VTI 62% + VXUS 38% of the equity (two funds); ITOT + IXUS in the same split (S2, iShares pages) | VT yes (#23, line 273); VTI yes (#22); VXUS yes (#51); ITOT, IXUS no |
| Short Treasuries in the growth money | **VGSH** Vanguard Short-Term Treasury ETF | 0.03% [as of 2025-12-19]; 1.9y [8/31]; 92 bonds; Bloomberg U.S. 1-3 Year Treasury Index; fund total net assets $39.3bn [8/31]; SEC yield 4.55% [9/24]; price $57.59 [9/25]. Vanguard API, re-read. Volume not published | SHY (0.15%, 1.79y, 91 notes, $26.18bn; ishares.com/239452, re-read). A WInS-listed ~2-year U.S. Treasury note ($10 commission; prices update once a day) | VGSH yes (#93, line 1113, merged with name); SHY yes (#86, line 1029) |
| Cash float | Cash | none | BIL (0.1353%, 0.10y; ssga.com; page now titled "State Street SPDR Bloomberg 1-3 Month T-Bill ETF"), SGOV (0.09%) | BIL yes (#92); SGOV no |

Why these and not others (each traced to Laura or the case):
- **Low-cost, broad, transparent, liquid** (brief section 4). No leverage, inverse, thematic or single-country funds:
  nothing in the case justifies them. A Taiwan tilt would be tokenism (S2).
- **TLH over TLT:** Laura's payments are 6.3-15.3 years away. TLH's bonds are 10.4-19.9 years away; TLT's are
  17.6-29.9 years away. So TLH sits **closer** to her dates. Measured consistently, its worst 50bp-twist error is about
  60% smaller than IEF/TLT's ($1.5k against $3.8k on a $292k hedge; S4 method). It is a closer fit, **not** a
  year-by-year match: three-quarters of TLH matures after her last payment.
- **VT as one fund:** 10,088 stocks and a 21.7% top-10 share (S2). Laura holds a statistics degree ("Statistics &
  Information Decisions Management", case line 16, VERIFIED-REPO-FILE). One index she can check against one published
  assumption fits that background. Use this once, in one place, not as decoration.
- **VGSH:** short Treasuries are what any future promised amount would be built from; they keep part of the growth money
  safe and available.

## 2. What the $300,000 represents: (ii) and (iii) as equals
Plan numbers at 2028-01-01 (script section 3; ASSUMPTION: today's forwards and JPM returns are realised): hedge 65.9%,
equity 20.4%, short/other sleeve bonds 13.6% at a 60/40 sleeve. So the old "65/35" was hedge/sleeve, not bonds/stocks.
Option (i) (34% equity) is dropped: no version of the plan holds it.

| | **(ii) The mix after both deposits, scaled to $300k** | **(iii) The literal January 2027 book** |
|---|---|---|
| Hedge (about 10 years) | 66% | 98% (ladder $294,387 of $300,000) |
| VT / VGSH / cash | 20.5% / 12.5% / 1% | 0% / 0% / 2% (the 2027 leftover waits in T-bills; VT starts in 2028) |
| Case support | "implementation of its investment strategy during the competition" (case line 129): shows the whole strategy, including growth and flexibility | "It does not determine Laura's actual portfolio value at the beginning of 2027" (case line 129-130) and the $150,000 "will not be added to WInS" (SMApply, VERIFIED-PRIMARY): WInS is the $300k on the eve of the January 2027 purchase |
| Notes it gives | Three different funding purposes (promise, growth, short Treasuries); SMApply lists "funding purposes" as a kind of diversification (R-W71) | Hedge notes only; the growth argument has to come from the IPS |
| Under a 25% position limit | 5 positions (IEF, TLH, SPTL, VT, VGSH) | 5 Treasury funds: IEF 24 / TLH 24 / SPTL 24 / VGIT 17.6 / VGLT 8.4 (script section 10; twist error $2.8k, about 1% of the hedge) |
| Main weakness | WInS shows about 20% stocks while Laura's real 2027 money is almost all ladder; must be explained | A reader may see about 98% Treasuries as timid for a client who "has been willing to take thoughtful risks" (case line 70) |

**The test the team applies:** "Which reading of 'implementation during the competition' would we defend in the Final
Report, in our own words?" Pick one and record why. S3's lean is (ii), because it shows growth and flexibility as well
as the promise, but (iii) is fully defensible.

**If (ii), the team's one explanatory sentence (IPS or Final Report) must contain three things:**
1. WInS holds the mix Laura's portfolio reaches after both deposits, scaled to $300,000;
2. the Treasury part is set to the payments' sensitivity to rates today, about 10 years;
3. in January 2027 almost all of her real $300,000 buys the ladder.

Consistency across the three deliverables means **the same rules and rough shares**, not one table of weights. The IPS
guide asks teams to "Focus on the strategy and decision-making framework … rather than describing individual
investments or presenting detailed financial calculations" (`2026_WGY_Investment_Policy-FINAL.txt` line 51,
VERIFIED-REPO-FILE).

## 3. The hedge: weights, duration, behaviour, capped rule
- **Weights:** IEF weight = (D_TLH - 9.90) / (D_TLH - D_IEF) with the issuer "effective duration" on the trade date.
  Today: IEF 35.7% / TLH 64.3% of the hedge (23.6% / 42.4% of the total).
- **Why a 9.90 target, and why that is right (reason corrected after the red team):** a hedge bought today should match
  the payments' **spot** duration, 10.16 years (brief section 14). Issuer effective durations sit about 0.2-0.3 years
  below full-revaluation model durations (TLH 11.59 issuer vs 11.87 model). So the mix weighted to 9.90 on issuer
  numbers is about 10.1 years in model terms, close to 10.16, and tracks the payments within about $450 per 100bp
  (forward-consistent, S4 script). Weighting to 10.16 on issuer numbers would overshoot ($1,035 per 100bp). **One line
  for brief section 14:** "use spot duration (10.16) as the target; on issuer durations, the 9.90 weights hit it."
- **Precision:** the gap between two honest duration measures (0.28 years for TLH) is as large as the debate about the
  target. **Say "about 10 years" in every deliverable; never quote the hedge's duration to two decimals.**
- **What it does in WInS:** the $198k hedge moves about $20k per 1 percentage point of rates (first-order). The value of
  Laura's payments moves by about the same percentage in the same direction. Judged against the payments the hedge is
  close to risk-free; judged in dollars alone it is not.
- **Capped rule (only if Session Rules show a limit under 44%).** IEF stays at 23.6%; TLH one point under the cap; SPTL
  takes the rest. Script section 10, forward-consistent tracking:

| Cap | Mix (share of total) | Duration (issuer) | Worst 50bp twist error |
|---|---|---|---|
| none | IEF 23.6 / TLH 42.4 | about 10y | $1,544 |
| 35% | IEF 23.6 / TLH 34.0 / SPTL 8.4 | about 10y | $2,120 |
| 25% | IEF 23.6 / TLH 24.0 / SPTL 18.4 | about 10.5y | $2,803 |

  Every error is under 1% of the hedge. One extra fund beats the old four-fund or individual-bond variants, which are
  dropped from the week-1 plan. If SPTL's share would be under 2% of the portfolio (a cap of 43-44%), put that sliver in
  IEF instead (duration moves under 0.1 year). ASSUMPTION: the limit is checked when an order is placed; if WInS applies
  it continuously, the 1-point buffer on TLH lasts until rates fall about 1 percentage point (script arithmetic).
- **If TLH is not in WInS:** IEF 41.0% / TLT 25.0% (both on the 2025-26 list; twist error $3.8k). If TLH is missing
  **and** a 25% cap applies: IEF 24 / SPTL 24 / VGIT 9.5 / VGLT 8.5 (about 10 years; twist error $3.3k; script
  section 10). That is the only four-fund case, and it arises only if two checks fail together.

## 4. Sequence and calendar
Times: U.S. open 9:30 a.m. ET. For the team (ASSUMPTION: the team's Australian state is not recorded):
- until Sat Oct 3: 11:30 p.m. AEST the same date;
- from Sun Oct 4 (NSW/Victoria daylight saving; Queensland does not change): 12:30 a.m. AEDT the next date;
- **from Mon Nov 2 (U.S. daylight saving ends Sun Nov 1, 2026): 1:30 a.m. AEDT** (12:30 a.m. AEST in Queensland). The
  Nov 6 close (4:00 p.m. EST) is **8:00 a.m. AEDT on Sat Nov 7**.
Orders entered in the Australian daytime fill at the next U.S. opening price (SMApply FAQ, VERIFIED-PRIMARY).

| Step | When | Action |
|---|---|---|
| 0 | Before any order | The five-box gate; the WInS checks in section 7 |
| 1 | Week 1 once the gate is passed (target fills by Fri Oct 2 ET) | Orders 1-4 in one session, hedge first. Split recorded as provisional 60/40 |
| 2 | Weekly (same weekday) | Check bands (section 5); trade only if one is breached |
| 3 | Oct 19-23 | Duration refresh: recompute IEF/TLH weights; trade only if the hedge is outside 9.65-10.15 on issuer numbers |
| 4 | Oct 23 | Trading Notes due: choose the best 3 executed trades |
| 5 | Nov 6 | IPS due; WInS freezes. No "tidy-up" trades in the last days |

**Where the third note comes from:** the VGSH buy itself (a distinct funding purpose). A genuine later decision can
replace it: a duration refresh, a change of the split after the team's research, or a band trade. Do not create a
decision just to get a note. Log "we decided not to trade" moments for the Final Report.

## 5. Rebalancing rule for WInS
| What | Target | Band | How to fix |
|---|---|---|---|
| Hedge duration | about 10y (9.90 on issuer numbers) | 9.65-10.15y; **never trade to fix a smaller gap** | IEF against TLH (or SPTL) only |
| Hedge vs growth money | set once at purchase | **No band.** The hedge's share rises when rates fall because the payments cost more; that is correct | Never move money between them |
| Inside the growth money | VT 60% / VGSH 40% (provisional) | VT at 55-65% | VT against VGSH only. Triggers only if stocks move about -18.5% or +23.8% relative to bonds |
| Cash float | about 1% | at least $1,000, at most about 2% | Excess distributions go to VGSH |

The full "never" list (the ticket's three plus): never sell the hedge to buy stocks; never lengthen duration to bet on
rates (TLT alone, EDV/GOVZ/ZROZ, foreign government bonds whose currency does not match a USD promise); no thematic,
leveraged, inverse or single-country funds; no trading for ranking or in the last days; never write or edit a note after
the fact; the advisor never places trades (R-W87); cash never negative (no margin); never push a position above the
Session Rules limit; never re-weight to the June fact-sheet durations.

## 6. Substitutes if a pick is not in WInS
| If this fails | First substitute | Second | 2025-26 list |
|---|---|---|---|
| TLH | IEF 41.0 / TLT 25.0 (capped at 25%: IEF 24 / SPTL 24 / VGIT 9.5 / VGLT 8.5) | SPTI + SPTL, or VGIT + VGLT, at duration weights | TLT yes; others no |
| IEF | VGIT (re-weight to about 10y with TLH) | SPTI | no / no |
| SPTL (capped branch) | VGLT | TLT (duration longer; re-run section 10) | VGLT no; TLT yes |
| VT | VTI 62% + VXUS 38% of the equity | ITOT + IXUS | VTI, VXUS yes |
| VGSH | SHY | a WInS-listed ~2-year U.S. Treasury note | SHY yes |

No sector rule exists this season ("There is no required sector allocation or minimum number of sectors", SMApply,
VERIFIED-PRIMARY); a broad fund already holds all 11 sectors, so no sector-fund fallback is needed.

## 7. Checks in WInS before the first order
- [ ] 1. Official account, not practice (practice trades were reset, R-W77). A student places every trade (R-W87).
- [ ] 2. Session Rules screenshot (gate box c). Pick the branch.
- [ ] 3. Re-read SMApply Trading Details and FAQ that morning; note any change to cash, trades, volume or commissions.
- [ ] 4. Search each ticker: it must show as an **ETF**, with the issuer's full name (BIL is now "State Street SPDR…";
      SPTL is "State Street SPDR Portfolio Long Term Treasury ETF"). All picks are U.S.-listed.
- [ ] 5. **Volume:** read **today's** volume in WInS for each ticker; the rule is "no more than twice a security's
      current daily trading volume" (SMApply, VERIFIED-PRIMARY). An overnight order fills at the open, when the day's
      volume so far is smallest. If an order is rejected, split it across days. Never switch to a thinner fund to get it
      through.
- [ ] 6. Commission shown ($25 per ETF trade, ASSUMPTION that ETFs count as "stock"); cash stays positive after all orders.
- [ ] 7. Note field: check for a character limit (none published). Write the note before pressing submit; copy it word
      for word into the decision log straight after.
- [ ] 8. Record which U.S. Treasuries appear in the bond drop-down (for the Final Report only).
- [ ] 9. Check whether WInS pays interest on cash (decides cash vs BIL for money that waits more than about 3 weeks).
- [ ] 10. Recompute the IEF/TLH weights from the issuer pages on the trade date; record numbers and time.
- [ ] 11. Anything ambiguous: ask Wharton through the official channel. Never contact Laura (R-W16).

## 8. Laura's long-term instrument map (not WInS)
| Date (start of year) | Money | Instruments | Rule |
|---|---|---|---|
| Jan 2027 | $300,000 | Ten Treasury STRIPS, $50k face each, maturing each Nov 15 2032-2041, ~$294,387 (detail in the Final-Report file). The ~$5.6k left over waits in T-bills (SGOV/BIL) | If rates fall first and the ladder costs more than $300k, buy the longest rungs first and the rest from the 2028 deposit |
| Jan 2028 | +$150,000 | Growth money (~$158k): 60% VT / 40% VGSH (provisional) | Rebalance once a year, band 55-65 |
| Jan 2031 | Growth money | Part of it moves into a 2-year Treasury note maturing 2032-12-31 (the promised amount for co-sponsors). The share is an **open team parameter** (brief section 9; the model uses 80%). It never appears in a WInS note | The promised amount is bought, not forecast |
| Jan 2033 | Ladder (~$394.9k market value on forwards) + note + rest | The ladder is the operating reserve; the note matures into cash for the facility decision | Payments come from maturing rungs only |
| 2033-2042 | Reserve runs down | Each Nov-15 rung waits about 47 days in T-bills, then pays Jan 1 | Nothing sold early |

- **Caveat (red-team finding 9):** in about 3 of 10 rate paths the real ladder needs part of the 2028 deposit;
  certainty for the first rungs then depends on that deposit arriving (ASSUMPTION-based: zero drift, 7.24% volatility).
  The joint tail (rates fall **and** the deposit is missing) is passed to Phases B-E. Not a week-1 note topic.
- **2031 note maturity:** Treasury's auction data show the December 2025 two-year note matures 2027-12-31 (CUSIP
  91282CPS4; api.fiscaldata.treasury.gov, VERIFIED-PRIMARY 2026-09-27). That the pattern holds in December 2030 is an
  ASSUMPTION. Alternates: the Nov 15 2032 principal STRIP (912821KC8); iBonds IBTM (Dec 2032).
- **Model inputs to align before the Final Report (finding 10):** `strategy_mc.py` should use JPM AC World (7.00% /
  16.78%) for equity and an explicit short-Treasury ASSUMPTION (about 3.5-3.9%) for sleeve bonds, so the model holds
  what WInS holds. Effect on the median is under about $2k (S2, S3).

## Changes after red team
| # | Severity | Finding (short) | What S3 did |
|---|---|---|---|
| 1 | Blocking | No gate before Day-1 orders | **Fixed.** Five-box gate at the top of the ticket; target "week 1 once the gate is passed (e.g. fills by Fri Oct 2 ET)", not Day 1 |
| 2 | Blocking | "Bonds mature when Laura pays" false; ranges misquoted | **Fixed.** Ranges corrected (IEF May-2033 to Aug-2036; TLH Feb-2037 to Aug-2046; TLT May-2044 to Aug-2056); 74.7% after-2042 figure stated; Note-1 checklist rewritten to "closer to / moves like / stand-in", with a "never claim" line. Same wording fixed in S1's summary, fund table, scale check and "What this teaches" (marked in S1) |
| 3 | Important | 42.4% TLH blocked by a 25% limit; fallback too complex | **Fixed.** One pre-chosen rule for any cap (IEF 23.6 / TLH cap-1 / SPTL rest; VGLT alternate), computed in script section 10. Individual 2041 bond, four-fund mix, two-issuer mix and IBGA rows removed. Added a 2% sliver rule and the continuous-limit ASSUMPTION |
| 4 | Important | VT on Day 1, VGSH waits; "80%" in Note 3; "floor proxy" overclaims | **Fixed.** VT and VGSH bought together at a provisional 60/40; VGSH relabelled "short-Treasury part of the growth money"; no percentage in Note 3; the third note is the VGSH buy or a genuine later decision |
| 5 | Important | Option (ii) oversold | **Fixed.** (ii) and (iii) presented as equals with a stated test; three-element sentence for (ii); "one set of numbers" replaced by "same rules and rough shares"; option (i) dropped (no plan version holds 34% equity) |
| 6 | Important | 538-line dossier, not a ticket | **Fixed.** One-page ticket at the top; $100k/$500k columns, A.4, D.1b rows, D.2 sector table, D.3, drift illustrations and all but one twist comparison cut; E.2 and E.5 moved to `S3_final_report_ladder_and_reserve.md` |
| 7 | Important | Could read as a generic Treasury + world-index portfolio | **Fixed.** Checklists require promise-sizing (~$292k) and the no-sell rule in the hedge note, ban "stable"/"reduce volatility", frame equity as 60% of the free money; "funding purposes" used once (section 2); statistics degree used once (section 1) |
| 8 | Minor | 9.90 anchor justified wrongly; mixed spot/forward tracking | **Fixed.** New reason (issuer vs model durations); 8.92 discussion deleted; one reconciling line for brief section 14; "about 10 years" rule; figures now forward-consistent ($1,544 / $451). S1's own `tracking()` left unchanged (optional; its ranking is the same) |
| 9 | Minor | Ladder fits under $300k less often (30.7%) | **Fixed.** One caveat line in section 8 and in the Final-Report file; joint tail passed to Phases B-E |
| 10 | Minor | Model holds different assets | **Passed on.** Section 8 states the two model changes for the main loop; S3 does not edit `strategy_mc.py` (verified script, outside S3's path) |
| 11 | Minor | Volume check used 30-day averages | **Fixed.** Check 5 now reads today's volume in WInS; split across days if rejected; never a thinner fund |
| 12 | Minor | Calendar missed the U.S. clock change | **Fixed.** Nov 2 open 1:30 a.m. AEDT; Nov 6 close 8:00 a.m. AEDT Sat Nov 7 |
| 13 | Minor | Stale statements, 2027 leftover, label, S1 formula and TLT range | **Fixed.** Stale CLAUDE.md/brief statements and open issue deleted; one leftover rule (T-bills in 2027, so (iii) holds VT 0%); label now "PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK" alongside the brief section 4 wording; S1 formula relabelled "IEF weight" and TLT range corrected |
| 14 | Minor | ±0.25y band narrower than duration uncertainty | **Fixed.** Band kept; "never trade to fix a smaller gap" and "never quote two decimals in a deliverable" added |

Nothing was rejected.

## Open issues for Phases B-E and the team
1. Team vote on lock-early, then (ii) vs (iii) (gate boxes a and b).
2. Session Rules position limit and the day-trading definition; WInS availability of TLH, SPTL, VT, VGSH; note-field
   limit; interest on cash.
3. Sleeve equity 50/60/70% and the 2031 share: both open; 60/40 is provisional.
4. Joint tail: rates fall before January 2027 **and** the 2028 deposit is missing or late.
5. Model alignment (AC World equity; short-Treasury sleeve bonds) before the Final Report.
6. "First trade by Oct 10": still UNVERIFIED.

## Sources (all accessed 2026-09-27)
- **SMApply (VERIFIED-PRIMARY, curl):** https://wghsinvcomp.smapply.us/res/p/trading/ ;
  https://wghsinvcomp.smapply.us/res/p/faqs/ (via `phase_A/case_register.md` R-W56-R-W94).
- **iShares (VERIFIED-PRIMARY, re-read 12:45 UTC):** https://www.ishares.com/us/products/239456/ishares-710-year-treasury-bond-etf
  (IEF), /239453/ishares-1020-year-treasury-bond-etf (TLH), /239454/ishares-20-year-treasury-bond-etf (TLT),
  /239452/ishares-13-year-treasury-bond-etf (SHY). Holdings maturities: `wins_now/S1_fund_holdings_snapshot.csv`
  (iShares holdings as of 2026-09-24, per S1).
- **State Street (VERIFIED-PRIMARY, re-read 12:42 UTC):**
  https://www.ssga.com/us/en/intermediary/etfs/spdr-portfolio-long-term-treasury-etf-sptl (SPTL);
  https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil (BIL, S3/S4 earlier).
- **Vanguard (VERIFIED-PRIMARY, re-read):** https://investor.vanguard.com/vmf/api/{VT,VGSH,VGLT,VGIT}/{profile,expense,characteristic,price};
  VT fact sheet https://fund-docs.vanguard.com/F3141.pdf (June 30, 2026; via S2/S4).
- **U.S. Treasury (VERIFIED-PRIMARY):** https://www.treasurydirect.gov/marketable-securities/treasury-notes/ ;
  https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query (2-year notes).
- **Repo files (VERIFIED-REPO-FILE):** `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (lines 16,
  70-74, 114, 129-133); `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (lines 14, 20, 30, 36, 44, 53);
  `2026_WGY_Investment_Policy-FINAL.txt` (line 51); `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt`
  (lines as cited); `research/insight_v1/phase_A/wins_week1_guardrails.md` (A4: user guide, Session Rules, Stock-Trak
  25% default and note permanence); `research/insight_v1/wins_now/S1_treasury_sleeve.md`, `S2_growth_sleeve.md`,
  `S4_red_team.md`.

## What this teaches
1. **Check the story against the holdings.** "The bonds mature when she pays" sounded right and was wrong for
   three-quarters of TLH. The fund was still the right choice, for a humbler reason: its bonds sit closer to her dates
   than the alternative's. A note that a reader can check must say only what the holdings show.
2. **Decide the rule before the surprise.** A position limit could appear at 11:30 p.m. on the first trading night.
   Choosing one simple fallback in advance ("TLH one point under the cap, SPTL takes the rest") turns a scramble into a
   look-up, and costs under 1% of the hedge in tracking.
3. **Approval comes before orders.** Trade notes are permanent. The cheapest protection is a gate: the team agrees,
   checks the rules, and writes its own notes, and only then trades. Waiting a few days costs nothing that is judged.
4. **Honest precision is "about 10 years".** When two fair ways of measuring the same fund differ by 0.28 years,
   quoting 9.90 versus 10.16 is decoration. Simple, checkable words carry more weight with a reader than extra decimals.
