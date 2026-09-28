# S4 red team: attacking `securities_and_allocation_v0.md` (S3's WInS week-1 plan)

Agent S4 (adversarial red team), insight_v1 run, written 2026-09-27. **PROVISIONAL.** The team has not approved the
strategy, and Phases B-E may change it. This is AI-generated research: findings, evidence and fixes. It is not text to
submit, and none of the fixes below is a drafted Trading Note. The team decides and writes every word.

Every ticker named here is **PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading**
(this season that means: listed in WInS, and within the Session Rules position limit).

Files attacked: `wins_now/securities_and_allocation_v0.md` (S3), `wins_now/S1_treasury_sleeve.md`,
`wins_now/S2_growth_sleeve.md`, `wins_now/S1_hedge_weights.py`, `scripts/S3_allocation_numbers.py`.
New script: `research/insight_v1/scripts/S4_red_team_checks.py` (run from the repo root with
`.venv/bin/python research/insight_v1/scripts/S4_red_team_checks.py`). It reproduces every new number below.

---

## Summary

The core of S3's plan survives the attack:
- every fund fact on the primary picks matches the issuer page;
- the arithmetic reproduces;
- the 2025-26 list look-ups are right;
- the insight that "65/35" was really hedge/sleeve, not bonds/stocks, is correct.

It is **not ready to trade as written**. Two findings are blocking:
1. **No approval gate.** The plan places orders at the first U.S. open (Mon Sep 28 ET) on a strategy the team has not
   approved. Trading notes are permanent and Wharton checks them.
2. **A false maturity story.** The Note-1 story "IEF and TLH hold bonds that mature when Laura pays" is wrong for
   three-quarters of TLH. **74.7% of TLH's bond weight matures in 2042-2046, after the last payment.**

Five findings are important:
- the headline allocation is blocked under the only documented position limit (25%), and S3's preferred fallback is its
  most complex one;
- VT is bought on Day 1 while VGSH waits for the same decision;
- Note 3 would write an open parameter (the "80%" floor) into a permanent note;
- option (ii) is defensible but oversold;
- the file is far too long for a Day-1 trade ticket.

The minor findings show one thing: debates about precision (9.90 vs 10.16 vs 8.92 years; $1,352 vs $1,544) are
smaller than the measurement noise in the duration numbers themselves. **"About 10 years" is the honest precision.**

**Verdict:** keep the IEF/TLH + VT + VGSH design and all its fund facts. Before any order, apply the fixes to findings
1-4 and cut the file to a one-page ticket (finding 6).

---

## Terms used (plain English)
- **Duration**: roughly the percentage a bond's price falls if interest rates rise by 1 percentage point.
- **Spot vs forward duration**:
  - The ten payments are worth $288,924 **today**. Their duration today is 10.16 years (the spot duration).
  - Valued as of 2027-01-01 (the forward value) they are worth $292,264, with a duration of 9.90 years.
- **Tracking error**: how many dollars the hedge's change in value misses the payments' change by in a rate scenario.
- **Twist**: short-term and long-term rates move in opposite directions.
- **Position limit**: the most WInS lets you hold in one security, as a share of the portfolio (Session Rules).
- **Gate**: a condition that must be met before an action is allowed.
- **STRIPS**: zero-coupon Treasuries that pay one amount on one date.

---

## 1. What I re-checked, and what held

### 1a. Fund facts on the issuer's primary pages (S4 re-opened them with curl on 2026-09-27, ~12:28-12:35 UTC)
| Fund | S3's claim | Issuer page today | Status |
|---|---|---|---|
| IEF | 0.15%; 6.86y (9/24); 16 notes; $41.57bn; 8,830,020 sh/day; SEC yield 4.84% | 0.15%; effective duration 6.86 yrs (Sep 24); 16 holdings; net assets $41,570,344,536 (Sep 25); 30-day average volume 8,830,020; 30-day SEC yield 4.84%; YTM 5.17%; closing price $90.00 | **Match**. VERIFIED-PRIMARY, https://www.ishares.com/us/products/239456/ |
| TLH | 0.15%; 11.59y; 61 bonds; $10.53bn; 1,969,419 sh/day; 5.29% | 0.15%; 11.59 yrs (Sep 24); 61 holdings; $10,528,708,140; 1,969,419; 5.29%; 3-year standard deviation 11.35%; closing price $93.38 | **Match**. VERIFIED-PRIMARY, https://www.ishares.com/us/products/239453/ |
| TLT (alt.) | 0.15%; 14.88y; 47 bonds | 14.88 yrs (Sep 24); 47 holdings | **Match**. VERIFIED-PRIMARY, /239454/ |
| SHY (alt.) | 0.15%; 1.79y; 91 notes | 1.79 yrs; 91 holdings | **Match**. VERIFIED-PRIMARY, /239452/ |
| VT | 0.06% (as of 2026-02-27); 10,088 stocks (8/31); 37.7% non-U.S.; $81.9bn; $160.03 | expenseRatio 0.0600 as of 2026-02-27; numberOfStocks 10088 (2026-08-31); foreignHolding 37.7; share class $81.9 billion; market price 160.03 (9/25) | **Match**. VERIFIED-PRIMARY, https://investor.vanguard.com/vmf/api/VT/{expense,characteristic,price} |
| VT top-10 | 21.7% (fact sheet 6/30) | "Top ten as % of total net assets 21.7%"; Taiwan 3.5%; TSMC 1.7%; U.S. 61.9% (as of June 30, 2026) | **Match**. VERIFIED-PRIMARY, https://fund-docs.vanguard.com/F3141.pdf |
| VGSH | 0.03% (2025-12-19); 1.9y (8/31); 92 bonds; $34.8bn; SEC yield 4.55% | 0.0300 as of 2025-12-19; averageDuration 1.9 years (8/31); numberOfBonds 92; $34.8 billion; yieldPct 4.55 (9/24); $57.59 | **Match**. VERIFIED-PRIMARY, https://investor.vanguard.com/vmf/api/VGSH/{...} |
| BIL (optional) | 0.1353%; 0.10y OAD; 33 T-bills; $47.92bn; renamed "State Street SPDR…" | 0.1353% gross; fund OAD 0.10 years (index 0.09); 33 holdings; $47,922.72M (Sep 24); page title "State Street® SPDR® Bloomberg 1-3 Month T-Bill ETF" | **Match**. VERIFIED-PRIMARY, ssga.com (redirected URL) |

Holdings maturity dates could not be re-downloaded. The iShares holdings endpoint returned an HTML page to my curl
today. For maturities I used S1's snapshot, `S1_fund_holdings_snapshot.csv` (iShares holdings as of 2026-09-24,
VERIFIED-PRIMARY per S1). On that data **S3 and S1 misquote the ranges** (finding 2).

### 1b. The 2025-26 list (historical only, VERIFIED-REPO-FILE)
I searched `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` by ticker and by name. Every line
number S3 cites is correct:
- IEF #88 (line 1053); TLT #87 (1041); VT #23 (273, 0.06); VTI #22 (261); VXUS #51 (603, 0.07);
- VGSH #93 (1113, merged with its name, 0.04); SHY #86 (1029); BIL #92 (1101); SHV #90 (1077); VNQ #21 (249).

TLH, SGOV, SPTI, SPTL, VGIT, VGLT, ITOT and IXUS are absent. No "10-20" Treasury fund appears anywhere on the list.

### 1c. WInS rules (SMApply Trading Details, re-read by S4 2026-09-27, VERIFIED-PRIMARY)
S3's quotes are exact:
- $300,000 virtual cash;
- "The additional $150,000 … will not be added to WInS";
- 200 trades;
- "no more than twice a security's current daily trading volume";
- "Any ETF available on WInS";
- "There is no required sector allocation or minimum number of sectors";
- "not simply to own a large number of securities".

### 1d. The arithmetic
I re-ran `S1_hedge_weights.py` and `S3_allocation_numbers.py` with `.venv/bin/python`. Both reproduce:
- $292,264, 9.90y and DV01 $289/bp;
- IEF/TLH 35.7/64.3 and IEF/TLT 62.1/37.9;
- twist errors $1,352 / $3,619;
- ladder cost $294,387;
- 2028 plan split 65.9 / 20.4 / 13.6;
- all dollar amounts, share counts, band triggers (-18.5% / +23.8%) and reserve values.

I also checked the hand formulas: 0.357 × 6.86 + 0.643 × 11.59 = 9.90, and the portfolio duration of 6.77y.

What failed is a method choice and a wording claim (findings 2 and 8), not the arithmetic.

---

## 2. Findings

### Finding 1 (BLOCKING): there is no gate between "strategy not approved" and "Day-1 orders"
**Evidence.**
- S3's calendar puts IEF, TLH and VT at "Day 1 (orders fill at the Mon Sep 28 ET open)". That is 11:30 p.m. AEST on
  Sep 28, about a day and a half from now.
- CLAUDE.md says the strategy is "NOT YET DECIDED BY THE TEAM. The team has not read the memos yet."
  (VERIFIED-REPO-FILE).
- Trade notes are permanent. The Trading Notes guide says "Include each Trading Note exactly as it appears in WInS … Yes,
  we will verify this" (VERIFIED-REPO-FILE, p.2). Stock-Trak says students "cannot edit or delete their trade notes"
  (via A4).
- No rule requires a Day-1 trade. SMApply says "The competition does not require frequent or same-day trading. Make
  thoughtful, well-researched decisions" (VERIFIED-PRIMARY, re-read today). "First trade by Oct 10" is still
  unverified.
- WInS gains and losses are not judged (R-W75). Waiting a few days therefore costs nothing that counts.
- A hasty note is permanent. It is also the exact failure the team had last year: rules and complexity got ahead of
  understanding (CLAUDE.md, Team).
- S3's Step 0 only asks the team to choose among mirror options (i)/(ii)/(iii). That assumes lock-early is already
  approved.

**Exact fix.** Replace Step 0 with a gate of five boxes, all ticked before the first order:
- (a) the team has read a short version of the plan and recorded a vote to adopt "lock early" (or not), with names
  and date;
- (b) the team has chosen (ii) or (iii) (finding 5);
- (c) a Session Rules screenshot is saved (position limit for single positions and by security type; day trading);
- (d) each WInS note has been drafted **by a student, in the student's words**, from the checklists, and read by a
  second student;
- (e) the fallback in finding 3 has been picked in advance.

Target the first orders for **any U.S. session in week 1 once the gate is passed** (for example, fills by Fri Oct 2 ET),
not "Day 1". Change the "Why this order" cell for step 1 so it does not imply urgency.

### Finding 2 (BLOCKING before any hedge note is written): "the bonds mature when Laura pays" is false for most of TLH
**Evidence** (S1 holdings snapshot 2026-09-24, VERIFIED-PRIMARY per S1; computed by `S4_red_team_checks.py` section 3):
- **TLH:** 61 bonds maturing 2037-02-15 to **2046-08-15**. By weight: 2037 0.9%, 2038 1.2%, 2039 3.0%, 2040 8.6%, 2041
  11.6%, then 2042 13.3%, 2043 20.1%, 2044 17.0%, 2045 14.7%, 2046 9.3%. So **74.7% matures after the last payment
  (2042-01-01)**.
- **IEF:** 16 notes maturing **2033-05-15 to 2036-08-15**.
- S3's section A.2 and S1's table say "Aug-2033 to May-2036" and "Feb-2037 to May-2046". Both ranges are misquoted
  against S1's own data.
- In the combined hedge (IEF 35.7% / TLH 64.3%), about **52%** of the bonds mature in 2033-2041 and about **48%**
  mature after 2042. The first four payments are 46.8% of the payments' value, but IEF is only 35.7% of the hedge.
- The duration match still works because the late TLH bonds make up for the shortfall in 2037-2041 bonds. It works
  "on average", not "year by year".
- The wording that overclaims:
  - S3 A.2: TLH is "Operating-commitment hedge, part 2: owns bonds maturing Feb-2037 to May-2046, covering the later
    payments";
  - S1 summary: "Together they own bonds that mature in the same years as Laura's ten payments";
  - S1 "What this teaches": "owns bonds maturing in exactly those years".
- Also, IEF and TLH are constant-maturity funds. They never mature and keep rolling into newer bonds. A reader who opens
  TLH's holdings page (the note is "verified") can check all of this.

**What stays true** (the honest case for TLH over TLT):
- Laura's payments are 6-16 years away.
- TLH's bonds are 10-20 years away. TLT's are 18-30 years away (TLT: 2044-05-15 to 2056-08-15).
- TLH sits closer to the payments. Its twist error is about 60% smaller than IEF/TLT's in both measurement methods:
  $1,544 vs $3,812 forward-consistent; $1,352 vs $3,619 S1 method.

**Exact fix.**
1. S3 A.2 and the F.1 tables: correct the ranges to IEF "May-2033 to Aug-2036" and TLH "Feb-2037 to Aug-2046". Drop
   "covering the later payments" and replace it with "10-20-year bonds, closer to the payment dates than TLT".
2. S1 summary item 1 and "What this teaches": replace "in the same years"/"exactly" with "closer to"/"spanning".
3. Note-1 checklist (S3 B.2). Replace "Why this fund: its bonds mature 2037-2046 …" with these elements:
   - the fund's bonds are *closer to* Laura's payment dates than a 20+ year fund's;
   - the pair is blended to move like her payments when rates change (about 10 years);
   - the funds are a stand-in: they never mature, and the real plan buys a ladder in January 2027.

   **Must not claim** that the funds' bonds mature in the payment years, or that the funds "match" the payments.

### Finding 3 (IMPORTANT): the headline allocation is blocked under the only documented position limit, and the preferred fallback is the most complex
**Evidence.**
- Stock-Trak's generic FAQ says "The default position limit is 25% which means you cannot put more than 25% of your
  portfolio value in a single security" (VERIFIED-PRIMARY via A4, `phase_A/wins_week1_guardrails.md` line 282).
- This season's value is unknown. The 2024-25 screenshot showed only a bond limit of 100% [PRIOR].
- TLH at 42.4% breaks a 25% limit, and so does IEF at 41.0% in the TLT fallback.
- S3's section 0 calls the capped mix "the best one": IEF 22.6% / TLH 24.0% / **the 3.125% Treasury due 2041-11-15**
  19.4%. That mix needs three things that are uncertain or awkward:
  - (a) bonds must have their own higher limit (UNVERIFIED);
  - (b) the bond must be in the WInS drop-down (UNVERIFIED);
  - (c) a second order screen, with prices that "are updated once daily".
- The ETF-only version has four Treasury funds, one of which (SPTI 4%, about $12k) exists only to fix the duration.
- So on Day 1, at 11:30 p.m. AEST, the team would walk a three-level decision tree.

**Exact fix.** Pre-choose one rule that works for any cap from 25% to 43%:
- IEF stays at its formula weight (23.6%, under a 24% working cap);
- TLH is held one point under the cap;
- SPTL takes the rest of the 66% (VGLT as its alternate; both PENDING APPROVAL CHECK).

Forward-consistent results (script section 2; the same S1 scenarios; ASSUMPTION: instantaneous shocks):

| Cap | Mix (share of total portfolio) | Hedge duration (issuer) | Worst 50bp twist | Worst ±100bp |
|---|---|---|---|---|
| none / ≥43% | IEF 23.6 / TLH 42.4 | 9.90y | $1,544 | $451 |
| 40% | IEF 23.6 / TLH 39 / SPTL 3.4 | 10.00y | $1,775 | $472 |
| 35% | IEF 23.6 / TLH 34 / SPTL 8.4 | 10.16y | $2,117 | $967 |
| 25% | IEF 23.6 / TLH 24 / SPTL 18.4 | 10.47y | $2,801 | $1,956 |
| 25% (S3 row 2, for comparison) | IEF 24 / TLH 24 / SPTL 14 / SPTI 4 | 9.89y | $2,269 | $765 |

- Every error is below 1% of a $292k hedge. Because WInS P&L is not judged (R-W75), one extra ticker beats two extra
  tickers.
- Every duration is still "about 10 years", so the note wording does not change.
- Delete D.1b row 1 (the individual bond) and the IBGA row from the week-1 plan. Keep the bond idea only as a
  Final-Report illustration, if at all.

### Finding 4 (IMPORTANT): VT is bought on Day 1 but VGSH waits for "the same decision", and Note 3 locks an open parameter into a permanent note
**Evidence.**
- VGSH is held in cash until week 2 because "the 2031 rule and the sleeve split (50/60/70) are open team decisions"
  (S3 B.1).
- But VT's size depends on the **same** split: 17% / 20.5% / 24% of the portfolio (S3 A.1). Buying VT at 60% on Day 1
  presumes the split that VGSH supposedly waits for.
- S3 itself says "Do not create a decision just to get a note". The staggered timing does exactly that.
- The Note-3 checklist suggests naming the rule "about 80% of the sleeve locked two years before 2033".
  - The 2031 floor share is listed as **open/disputed** (brief section 9).
  - The Trading Notes guide says teams are "not expected to … determine Laura's facility contribution" at this stage
    (VERIFIED-REPO-FILE, p.1).
  - A permanent WInS note that names 80% forces the IPS (Nov 6) to match it.
- The "2031 floor proxy" label overclaims:
  - in 2026 the VGSH position is 40% of the sleeve;
  - the floor in 2031 is about 80% of the sleeve, and a different instrument (a 2-year note).

**Exact fix.**
1. Buy VT and VGSH together, once the gate (finding 1) is passed, at the provisional 60/40 split. Record the split as
   provisional (CLAUDE.md shows the team accepted 60% provisionally).
2. Relabel VGSH everywhere as "the short-Treasury part of the growth money". Say its intended future use (it can become
   a guaranteed amount before Laura talks to co-sponsors) without a percentage.
3. Delete "about 80% …" from the Note-3 checklist.
4. The third note can be the VGSH buy itself (a distinct job: flexibility and credibility), or a genuine later decision:
   - a duration refresh;
   - a change of the split after the team's research;
   - the (ii)/(iii) decision, if it is made after a first trade.

   Log any "we did not trade" decisions for the Final Report.

### Finding 5 (IMPORTANT): option (ii) is defensible but oversold; its rationale mixes dates and overstates what the IPS needs
**Evidence.**
- The case says: "The WInS portfolio represents each team's implementation of its investment strategy during the
  competition. It does not determine Laura's actual portfolio value at the beginning of 2027" (case p.4,
  VERIFIED-REPO-FILE). SMApply adds that the $150,000 "will not be added to WInS" (VERIFIED-PRIMARY).
- Read literally, this supports (iii), the ~97% ladder book, at least as much as (ii).
- S3 says (iii) "describes 1 of the 6 pre-2033 years". But WInS runs in Sep-Nov 2026, the eve of the January 2027
  purchase. (iii) describes exactly that moment.
- (ii) takes its **size** from 2028-01-01 (hedge 65.9%) but its **duration** from 2027-01-01 (9.90y). The brief
  (section 14) says to hedge the WInS book to the spot duration (10.16y). So three dates are in play.
- S3 A.1 reason 4 says the WInS weights, the IPS percentages and the model inputs "must be one set of numbers". The IPS
  guide asks teams to "Focus on the strategy and decision-making framework … rather than describing individual
  investments or presenting detailed financial calculations" (VERIFIED-REPO-FILE, p.2). The consistency needed is about
  rules and rough shares, not a table of weights.

**Exact fix.**
- Keep (ii) as S3's recommendation if the team wants to show growth and flexibility, but present (ii) and (iii) as
  equals. The team picks with a stated test, for example: "Which reading of 'implementation during the competition'
  would we defend in the Final Report?"
- If (ii), the one-sentence explanation (the team's words) must contain:
  - WInS holds the target mix Laura's portfolio reaches after both deposits, scaled to $300k;
  - the Treasury part is set to the payments' interest-rate sensitivity today, about 10 years;
  - in January 2027 almost all of her real $300k buys the ladder.

  The IPS must say the last point too, so a reader is not surprised that WInS holds about 20% stocks.
- Delete "must be one set of numbers" from A.1. Replace it with "must follow the same rules and roughly the same
  shares".

### Finding 6 (IMPORTANT): unearned complexity. The file is a research dossier, not a trade ticket
**Evidence.**
- S3's file is 538 lines (55 KB). It contains:
  - three mirror options × three cash levels, although cash is known to be $300k;
  - three capped hedges plus a rejected IBGA row;
  - a 12-fund sector fallback for a rule that does not exist;
  - a CUSIP-level STRIPS ladder;
  - a ten-row reserve run-down;
  - twist errors quoted to the dollar.
- SMApply: "The goal is to build an intentional mix of investments appropriate for your strategy, not simply to own a
  large number of securities" (VERIFIED-PRIMARY).
- Last year's lesson: "strategy packaging was over-complex for the insight" (CLAUDE.md).

**Exact fix.**
1. **Cut:**
   - the $100k and $500k columns (A.2, A.4, B);
   - A.4 entirely;
   - D.1b rows 1 and 3 and the IBGA row (use finding 3's one-line rule);
   - D.2 (replace with one line: "no sector rule exists; a broad fund already holds all 11 sectors");
   - D.3 (keep one checklist line: record which U.S. Treasuries are in the drop-down);
   - C's illustrative duration drifts;
   - every twist figure except one comparison sentence.
2. **Move** E.2 (CUSIP ladder) and E.5 (reserve run-down) to a Final-Report research file. They are Dec-4 material.
   The Trading Notes guide says the reserve size is "not expected" now.
3. **Put a one-page ticket at the top** with:
   - the gate (finding 1);
   - Session Rules → mix A (no cap) or the one-line capped rule;
   - four orders (IEF, TLH, VT, VGSH);
   - three note checklists;
   - the three "never" rules: never sell the hedge after a rate rise, never trim it after a fall, never day-trade.

### Finding 7 (IMPORTANT): a semifinal reader could see this as a generic "Treasury ETF + world index" portfolio unless the notes carry the Laura-specific logic
**Evidence.**
- Wharton's own example note buys "an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin
  preparing for Laura's future operating commitment" (Trading Notes guide p.2, VERIFIED-REPO-FILE).
- Thousands of teams read the same example. A Treasury-ETF note is therefore the most common note in the field. VT is a
  default global fund.
- WInS under (ii) is about 79% Treasuries. The case calls Laura someone who "has been willing to take thoughtful risks"
  (case p.2). A skim can read 79% Treasuries as timid.
- What is genuinely distinctive and correct here:
  - (a) the hedge is sized to a specific promise (ten fixed $50,000 payments, valued at about $292k), not to "lower
    volatility";
  - (b) the second fund is chosen by distance to the payment dates (finding 2's honest version);
  - (c) a rule is committed in advance: no selling the hedge after rate rises, because the payments got cheaper too;
  - (d) risk is measured on the surplus: 60% of the money the promise does not need is in world stocks;
  - (e) the official phrase "funding purposes" (R-W71) as a kind of diversification.

**Exact fix.** Each hedge note must contain (a) and (c), and must avoid "reduce volatility"/"stable" (S3 already
warns about this). The growth note must frame equity as a share of the free money (d), not of the total. One note or
reflection should use (e). Laura's statistics degree ("Statistics & Information Decisions Management", case p.1 line
16, VERIFIED-REPO-FILE) supports "one index she can check against one published assumption". That is a real Client
Knowledge link. Use it once, not as decoration.

### Finding 8 (MINOR): the 9.90-year anchor is right in practice but justified wrongly; S1's tracking method mixes spot and forward
**Evidence** (script sections 1-2; model outputs on VERIFIED inputs):
- A hedge bought **today** must match the payments' **spot** duration, 10.16y. Its forward value moves 0.27y less, just
  as the payments' forward value does. S3's reason ("the sensitivity of that forward cost is 9.90") is therefore not the
  right test. This agrees with brief section 14.
- But the issuer's effective durations run below full-revaluation durations: TLH 11.59 issuer vs 11.87 model; IEF 6.86
  vs 6.90. So the issuer-weighted "9.90" mix is **10.09y** in model terms, close to 10.16.
- Measured forward-consistently (hedge forward value vs liability forward value):
  - the S3 mix misses by at most **$451 per ±100bp**;
  - weighting to 10.16 on issuer numbers misses by $1,035;
  - weighting to 8.92 (the 2028 view) misses by $3,260.
- S1's `tracking()` compares fund **spot** returns with the liability's **forward** change. Recomputed consistently:
  - IEF/TLH worst twist is $1,544 (not $1,352);
  - IEF/TLT is $3,812 (not $3,619);
  - ±100bp is $451 / $860 (not $991 / $1,274).
- The ranking TLH > TLT > SPTI/SPTL is unchanged.

**Exact fix.**
- Keep the issuer-weighted 9.90 target. Replace S3 A.3's reason with: "issuer durations sit about 0.2-0.3 years below
  full-revaluation durations, so the 9.90 issuer mix is about 10.1 years, close to the payments' spot duration of
  10.16; it tracks within about $500 per 100bp".
- Delete the 8.92 discussion, which tracks worst.
- The main loop should add one line to brief section 14 so the two files agree.
- Optionally switch S1's `tracking()` to the forward-consistent version in `S4_red_team_checks.py`.
- In every deliverable say "about 10 years".

### Finding 9 (MINOR for WInS; IMPORTANT for the Final Report): the real ladder fits inside $300k less often than the brief says
**Evidence** (script section 5; ASSUMPTION: the brief's zero-drift lognormal with 7.24% volatility):
- S1's Nov-15 STRIPS ladder costs $294,387, so the headroom is about 19bp, not 27bp.
- P(cost > $300k on 2027-01-01) is **30.7%**, against 24.3% for exact-date zeros.
- Cost at -25 / -50 / -100bp: $301,676 / $309,169 / $324,793.
- In those paths, S3 E.1's rule ("buy the longest rungs first and the rest from the 2028 deposit") means the nearest
  payments depend on the 2028 deposit. That is the brief's unanswered "joint tail" (section 9). STRIPS dealer mark-ups
  are unknown and would add to the cost (S1, UNVERIFIED).

**Exact fix.** Add one line to S3 E.1: "in about 3 of 10 rate paths the ladder needs part of the 2028 deposit;
certainty for the first rungs then depends on that deposit arriving". Pass the joint tail to Phases B-E. None of this
belongs in a week-1 note.

### Finding 10 (MINOR): the model and WInS hold different assets
**Evidence.**
- `research/verified_2026-09-27/strategy_mc.py` models the sleeve's bonds as JPM U.S. intermediate Treasuries (4.00%
  compound, 3.48% volatility; line 27) and its equity as U.S. large cap.
- WInS holds VGSH (1.9y) and VT (global). S2 and S3 both flag this (S3 open issue 4).

**Exact fix.** Before the Final Report, the main loop changes two model inputs:
- equity: JPM AC World 7.00% / 16.78%;
- sleeve bonds: an explicit short-Treasury ASSUMPTION (S3 suggests about 3.5-3.9%).

Keep VGSH in WInS: short Treasuries are what the 2031 floor will be built from. The effect on the median is under about
$2k (S2, S3).

### Finding 11 (MINOR): the volume check uses the wrong denominator
**Evidence.**
- The rule is "no more than twice a security's **current daily** trading volume" (SMApply, VERIFIED-PRIMARY, re-read
  today).
- S3 compares orders with 30-day **average** volume (e.g. "0.035% of TLH's volume cap").
- An overnight order that fills at the open may be tested against the volume traded so far that day.
- At these sizes (largest 1,362 TLH shares against about 2m a day) it should still pass, but the stated check is not
  the rule.

**Exact fix.** Reword F.2 item 5: read today's volume in WInS. If an order is rejected for volume, split it across
days. Never switch to a thinner fund to get it through.

### Finding 12 (MINOR): the calendar misses the U.S. clock change
**Evidence.**
- U.S. daylight saving ends Sunday Nov 1, 2026 (the first Sunday of November).
- From Mon Nov 2 the U.S. open is **1:30 a.m. AEDT**. The Nov 6 close (4:00 p.m. EST) is **8:00 a.m. AEDT on Sat
  Nov 7**.
- S3's calendar stops at the Oct 4 Australian change (ASSUMPTION: the team is in an AEDT state; its state is not
  recorded).

**Exact fix.** Add the line to B.1. It matters only if the team trades in the last week, which S3 already advises
against.

### Finding 13 (MINOR): stale or internally inconsistent statements in S3
**Evidence and fixes.**
- S3 section 1 says "CLAUDE.md and brief sections 6 and 9 still carry the old third-party claim" about a sector minimum.
  S3 open issue 5 asks the main loop to add the $300k cash. CLAUDE.md and brief section 14 already say both
  (VERIFIED-REPO-FILE). **Fix:** delete both statements.
- S3 E.1 puts the 2027 leftover (~$5.6k) in T-bills. But option (iii) holds VT 1.5%, and the script grows the leftover
  at the 60/40 sleeve rate. **Fix:** pick one rule. The simplest is T-bills in 2027 and VT from 2028; then (iii) holds
  VT about 0%.
- The label is still brief section 4's wording. **Fix:** use brief section 14's "PENDING WInS AVAILABILITY +
  POSITION-LIMIT CHECK".
- S1 section 2 labels "(D_TLH − 9.90)/(D_TLH − D_IEF)" as the "IEF/TLH weight". It is the **IEF** weight. **Fix:**
  relabel it.
- S1 gives TLT's range as "Aug-2044 to May-2056". The snapshot says 2044-05-15 to 2056-08-15. **Fix:** correct it.

### Finding 14 (MINOR): the hedge rebalancing band is narrower than the uncertainty in the duration number
**Evidence.** The band is 9.90 ± 0.25y (S3 C). The issuer-vs-model gap for TLH alone is 0.28y (finding 8).

**Exact fix.** Keep the band, since it will rarely trigger and that is the point. Never quote the hedge's duration to
two decimals in a deliverable, and never trade to fix a gap smaller than 0.25y.

---

## 3. What survived the attack (keep)
- **All primary-pick fund facts** (section 1a) and the 2025-26 list look-ups (1b).
- **The hedge/sleeve decomposition**: 65.9% hedge / 20.4% equity / 13.6% sleeve bonds at 2028 (reproduced). This is the
  real fix for the brief's 35%-vs-20% inconsistency.
- **TLH over TLT** as the second hedge fund. It still wins in a consistent recomputation, as long as it is justified by
  "closer to the payments", not "matures when she pays".
- **VT as the single growth fund**: 0.06%, top-10 21.7% against 38.8% for the S&P 500 (S2). No Taiwan tilt, no sector
  funds, no leverage.
- **The "never" rules**: never sell the hedge after a rate rise, never trim it after a fall, never move money between
  the sleeves, never day-trade, never trade for ranking.
- **The Session Rules check before the first order**, and copying each note into the decision log.
- **Cash over BIL** for short waits (the $50 round trip needs about 14 days of BIL yield).

## 4. Which findings each deliverable depends on
| Deliverable | Findings that must be fixed first |
|---|---|
| WInS week 1 (now) | 1, 2, 3, 4 (blocking/important), then 6 |
| Trading Notes (Oct 23) | 2, 4, 7 |
| IPS (Nov 6) | 5, 8 ("about 10 years"), 10 |
| Final Report (Dec 4) | 9, 10; the moved E-sections from finding 6 |

## Sources (all accessed 2026-09-27 by S4 unless marked)
- iShares product pages (VERIFIED-PRIMARY, curl ~12:28 UTC): https://www.ishares.com/us/products/239456/ (IEF),
  /239453/ (TLH), /239454/ (TLT), /239452/ (SHY). The holdings endpoint
  `.../1467271812596.ajax?fileType=csv` returned an HTML page to curl today, so maturities come from S1's snapshot.
- Vanguard (VERIFIED-PRIMARY): https://investor.vanguard.com/vmf/api/VT/{profile,expense,characteristic,price},
  the same for VGSH; fact sheet https://fund-docs.vanguard.com/F3141.pdf (as of June 30, 2026).
- State Street (VERIFIED-PRIMARY):
  https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil (redirected from
  the old spdr-… URL).
- SMApply Trading Details (VERIFIED-PRIMARY): https://wghsinvcomp.smapply.us/res/p/trading/
- Repo files (VERIFIED-REPO-FILE):
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (lines 16, 68-74, 88-103, 114, 129-133, 161);
  - `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (pp.1-2);
  - `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` (p.2);
  - `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` (lines as cited);
  - `research/verified_2026-09-27/strategy_mc.py` (line 27);
  - `research/insight_v1/phase_A/wins_week1_guardrails.md` (lines 33-42, 234-239, 282-283);
  - `research/insight_v1/phase_A/case_register.md` (R-W66, R-W71, R-W75);
  - `research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv`;
  - CLAUDE.md.
- Scripts re-run: `research/insight_v1/wins_now/S1_hedge_weights.py`,
  `research/insight_v1/scripts/S3_allocation_numbers.py`. New: `research/insight_v1/scripts/S4_red_team_checks.py`.

## What this teaches
1. **Check a story against the holdings.** "The bonds mature when she pays" sounded right and was repeated in three
   places. Adding up the holdings by year took one line of code and showed that three-quarters of TLH matures after
   Laura's last payment. The fund was still the right choice, but for a different reason: its bonds are closer to her
   dates than the alternative's.
2. **Precision has a floor.** The team debated 9.90 vs 10.16 vs 8.92 years. The gap between two honest ways of
   measuring the same fund's duration (0.28 years for TLH) is as big as that debate. "About 10 years" is the true
   precision. Anything finer is decoration.
3. **Order of operations is part of compliance.** Last year the team traded outside the rules. This year the rules are
   clearer, but the same failure can come back as permanent notes written before the team understands its own
   strategy. The cheapest fix is a gate: approve, check Session Rules, draft the note, then trade.
4. **A red team should say what survived.** Most of this plan is right. The work is to remove the few claims that
   would not survive a careful reader, and to cut everything a high-school team cannot explain in its own words.
