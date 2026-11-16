# Bond desk 4: part 3c after the fee fix, and the monitoring in 3e and Table 3 after IBTA (Mon 16 Nov 2026, Sydney)

A fixed-income portfolio manager's read for precision: would a bond desk sign each figure and word? I read the plan
blind. I opened nothing else under `research/panel/` and did not open SCORECARD, LESSONS or ARGUMENT_LOG. These are
planning notes, not report prose. I edited no other file and committed nothing.

Note: SKELETON, tables.md and NUMBERS were being edited while I read them (uncommitted changes at 17:38 and later). The
line numbers below are from the working copy at the end of my read. The 3c, 3d and 3e rows and Table 3 did not change
during the read. Table 2's note changed from "the fee" to "the fees".

## What I read

| File | Lines | What for |
|---|---|---|
| Case, `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` | l.94-99, l.109-120, l.146-149 | Reserve; range, confidence, protecting the payments; the five assumption areas |
| FINAL IPS, `keel/final_report/FINAL_IPS_as_submitted.txt` | l.11, l.13, l.15, l.17 | "barring a US default"; the ten; "bare minimum ... without doubt", "the bottom will remain constant", "money you already own"; the two reasons |
| TNA, `keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt` | l.5, l.13, l.15 | Waiting-cash risk; IBTM "final payout is not fixed"; NAV, not par |
| SKELETON | l.42 (3.0), l.45 (3c), l.46 (3d), l.47 (3e) of the density cut; l.204, l.206 (conceit); l.229, l.231 (aha); l.257 (3.0), l.260 (3c), l.261 (3d), l.262 (3e); l.285 (Table 2), l.289 (Table 3) | The plan for 3c and 3e |
| WORDS | l.24, l.29, l.33, l.34, l.35, l.39, l.63 | Names for the standard, the contribution, the range, model runs, the fund payout and waiting cash |
| exhibits/tables.md | l.62-82 (Table 2 and its note), l.84-105 (Table 3, its note and "Not a row") | The exhibits |
| NUMBERS | l.6-17 (Sun 15 Nov changes), l.59-83 (section 0), l.215-273 (section 3), l.275-402 (section 4), l.411-490 (section 5), l.905-984 (8h, cash dates and ended funds), l.1026-1060 (8j), l.1159-1257 (8l), l.1492-1555 (8p) | The register |
| Code | `numbers/completion.py` l.1-60, l.352-575 (the rule, `zero_per_dollar`, `rule`, `owned_test`); `numbers/engine.py` (all); `numbers/plan.py` (all); call sites in `range_rule.py` l.230-238, `range_margin.py` l.88-96, `joint_stress.py` l.169 and l.396 | That the code does what NUMBERS says |
| Card Q3c | rows 7, 8, 10, 14, 17; claim 4; the 0.27% line (l.36) | IBTA and the 0.5% |
| Card Q4c | card 4 (l.153-164) | Basis of the default-size clause (the Chicago Fed's reading of CDS: sourced, no finding) |
| IBTM summary prospectus, 27 Feb 2026 (ishares.com `sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf`; read 16 Nov through a fetch summary, so re-read the PDF before quoting) | n/a | The fund ends "on or about December 15, 2032"; "The Board may extend the termination date ... does not require additional approval by Fund shareholders"; no notice period stated; in the last six months, money from maturing bonds is "typically ... reinvested ... in investments already in the Underlying Index"; "Cash does not earn any reinvestment income while it is held in the Underlying Index"; the fee is 0.07%; the acquired-fund-fee waiver covers funds advised by BFA "through the termination date"; BFA pays every operating cost except litigation, extraordinary expenses and the costs of buying and selling holdings; up to one-third of assets may be lent; it "does not seek to return any predetermined amount" |

## What I re-ran (scratch only, outside the repo)

The scripts are in `/tmp/claude-0/-home-user/cdd961e4-901c-5589-a829-32f064718722/scratchpad/bd4/`. All three import the
repo's engine read-only.

- **check1.py: the central rule, plus an independent pricer.** Built from the bond itself and not from
  `zero_per_dollar`, it gives the following. All of it matches NUMBERS l.9-12 and section 3.
  - What $1 pays at zero interest: floor 1.207415 (1.208257 with the fund's fee alone; 1.212062 with no fee at all);
    moved half 1.070113.
  - Floor money $81,889; moved money $18,495.
  - Zero-interest values: $98,874 (floor) and $19,791 (moved half), $118,666 together.
  - Unrounded ends $98,380 and $118,072; stated ends $95,000 and $115,000.
  - The cut: 4.17% and 2.49% before the 0.5%; 4.65% and 2.98% with it.
  - The fee from the trade day costs the floor 0.314% of value (0.07% x 4.96 years = 0.347% if charged on the principal
    throughout).
  - **The code does what NUMBERS 0 l.77-82 and section 3 say:**
    - the price is the value of the gross holdings;
    - each flow is paid less the 0.07% fee from the trade day, with the principal charged to 15 Dec 2032;
    - each distribution is paid less the bill fund's 0.15% a year to 15 Dec 2032;
    - 0.5% is taken off;
    - the top is the floor's January 2028 value plus the moved half's, rounded down once.
- **check2.py: the house model (200,000 paths, seed 2033).** It reproduces the following:
  - 6.006% of paths with the top missed at 0.75% costs, by at most $402;
  - 3 paths below the bottom;
  - 247 one-figure ranges and 3,032 ranges $5,000 wide;
  - 61.8% of paths with a stated bottom of $95,000 or more, and 59.8% with a stated top of $115,000 or more.

  It adds figures that are not in the register:

  | Measure | Result |
  |---|---|
  | Costs beyond the fees that miss the top, central, at zero interest | 3.09% |
  | The same, at the payout modelled at forward rates | 6.86% |
  | Paths with the top missed at the modelled payout, at 0.75% / 1% / 2% / 3% costs | 0 / 0 / 6 / 469 |
  | Smallest cost cover across paths at the modelled payout | 1.53% |
  | Paths whose 2031 range, from today, is exactly $95,000 to $115,000 | 5.5% |
  | Paths with a 2033 contribution between $95,000 and $115,000, from today | 51.2% |
  | Paths with a contribution of $95,000 or more, from today | 97.3% |
- **check3.py: the floor's cash and the NT$ convention.**
  - Of the floor's $98,874 zero-interest value, $15,569 is paid out as monthly distributions from 2028 to July 2032,
    before the fund ends. The moved half pays out $1,162.
  - "10% stronger" as 10% more US dollars means NT$ per US$ 29.79. Read as NT$ per US$ down 10%, it means 29.49 and
    11.1% more US dollars.

## Job 1: part 3c after the fee fix

**H1 (HIGH). The cost clause of the confidence sentence states a worst-case bound as if it were what happens, and it
leaves out the condition it needs.**
- **The plan's words:**
  - SKELETON l.45: "at the top unless the funds' other costs, beyond their 0.07% yearly fee, take more than 0.5% of
    their value by the end, and then short by about $120 for each tenth of a percent above that". The same words reach
    Laura's passage at l.261: "reached unless the funds' costs beyond their fee exceed the 0.5% cut (then short by
    about $120 for each tenth of a percent above it)".
  - l.260: "at 0.75%, about 1 path in 17 is short of the top by at most $402, still inside the range" and "At fund
    costs of 0.75% the top is missed in about 6% of simulated futures and periods".
- **What is true:**
  - The 0.5% is the smallest cushion in any path. It binds only where the rounding remainder is close to zero.
  - In the central case the top is missed only if costs beyond the fees pass 3.09% of the funds' value with cash
    earning nothing, or 6.86% at the interest the market expects.
  - "Short by about $120 for each tenth above 0.5%" is a ceiling on the slope ("at most", NUMBERS l.269), and it applies
    only once a path's own rounding cushion is used up.
  - The 6% and the $402 hold only when two stresses are stacked: cash waiting earns nothing AND costs reach 0.75%. With
    the funds paying their modelled interest, costs of 0.75% or 1% miss the top in 0 of 200,000 paths (check2).
  - "Still inside the range" is false in 3 of 200,000 paths, which l.260 itself admits two sentences later.
- **A desk would sign:** "Both ends are owned with at least 0.5% of the funds' value to spare for costs beyond the 0.07%
  fee (about 3% on today's figures, because of the rounding down). Only if those costs passed that cushion, with cash
  waiting earning nothing, would the contribution fall short of the top, and then by at most about $120 for each
  further 0.1%."
- **For Laura's passage (3d):** drop the rate and say "the top is owned in Treasuries, with a margin for the funds'
  running costs".
- **Wherever the 0.75% figure survives** (store or note), add "if cash waiting also earned nothing".

**M1 (MEDIUM). "Certain" can attach to "$95,000 to $115,000".**
- **The plan's words:**
  - l.42 has 3.0 give "the standard, the range and the confidence in one figure each".
  - l.45 has 3c open with "about $95,000 to $115,000" and then say "inside the range is certain".
- **Why it matters:** the case asks how confident the team is "that her 2033 contribution will fall within that range"
  (case l.117-118). Measured from today, the contribution lands between $95,000 and $115,000 in about half of the
  simulated futures (51.2%, check2: a check figure, not in the register, never to be printed). The certainty belongs to
  whatever range the rule gives in 2031.
- **The fix:**
  - In 3.0 and in 3c's confidence sentence, the subject of "certain" is "the range she states in 2031, once both ends
    are owned". "$95,000 to $115,000" always travels as "on today's figures" and never sits in the same sentence as
    "certain".
  - If a figure from today is wanted, use the register's: the stated bottom is $95,000 or more in about 62 of 100
    simulated futures and the stated top $115,000 or more in about 60 (NUMBERS l.316-317).

**M2 (MEDIUM). "The bottom is the figure that holds whatever the funds' costs" (l.45, the lay reader's "why state a
bottom?").**
- **Why it fails:**
  - "Whatever" is false. Centrally, costs of about 20% break the bottom (check1).
  - Where the range is one figure, 0.75% breaks it (3 paths, NUMBERS l.1187).
  - It also gives the wrong reason for stating a bottom.
- **What is true by construction:** the bottom rests on the floor alone (it is at most 99.5% of the floor's zero-interest
  value), so it holds even if the shares moved in 2031 paid nothing.
- **The fix:** "the bottom rests on the floor alone, owned since January 2028; it holds even if the half moved in 2031
  paid nothing, so it is the figure co-sponsors count".
- **The same for l.260's "falls below the bottom only if both funds lose about a fifth":** it is central only. Say "on
  today's figures".

**M3 (MEDIUM). "About 0.27% shown by the five ended funds" mixes up sources and double-counts.**
- **The plan's words:** the 3d density row (l.46) says "every cost the five ended Treasury iBond funds showed comes to
  about 0.27%". 3e (l.47) has "card Q3c: about 0.27% shown".
- **Where the 0.27% comes from** (NUMBERS l.82; Q3c l.36), three parts stacked:
  - IBTM's 0.09% premium on 6 Nov 2026, which is not an ended fund;
  - half of a 0.05% spread;
  - five years of IBTF's worst calendar year beyond the fee (0.03 points).
- **What the 0.5% actually carries:** since card Q45 (NUMBERS l.78), "money put in" is units x NAV. The premium and the
  spread are therefore outside the rule. What the ended funds show for the costs the 0.5% carries is at most about 0.15%
  over five years. Over their lives every ended fund trailed its index by less than its fee.
- **The fix:**
  - "The ended funds' worst year beyond the fee, repeated for five years, is about 0.15%, under a third of the cut."
  - Or keep 0.27% and name it "the worst of three measures, one of them today's premium on IBTM".

**L1 (LOW). The waiting fee is missing from 3c's description of the rule.**
- The rule also charges the bill fund's 0.15% a year on the floor's distributions: $69 centrally (NUMBERS l.81).
- 3c (l.45) names only "the 0.07% fee charged separately from each trade day".
- One clause fixes it: "less the funds' 0.07% fee from the trade day and the bill fund's 0.15% while payouts wait".
- Table 2's note now says "the fees", which is enough there.

**L2 (LOW). "Fixed once bought" in NUMBERS.** NUMBERS l.285 labels the floor's payout in the history column "$103,178
(fixed once bought)". An iBond fund's payout is never fixed (TNA l.13). The figure is constant there only because rates
sit at the forwards. Relabel it "(rates at forwards)" before any writer lifts it.

**L3 (LOW). The default clause in 3d.** l.46's list of "what can lower it" includes "a US default". l.261's checklist
says the default "is 3e's one limit, said once there". Keep it once, in 3e (Book 19).

**L4 (LOW). A stale docstring.** `completion.py` l.12-15 still describes the Tue 10 Nov morning rule ("both rounded down
to $5,000", no fee, no 0.5%). The code below it is right. Point the docstring to `rule()` so no reader takes "both
rounded down" as rounding each end's parts.

**What holds (no change):**
- Every 3c figure: $95,000 and $115,000; $98,380 and $118,072; $103,178; $494/$3,380 and $593/$3,072; $119 per 0.1%.
- The bottom fixed in January 2028 and never re-measured.
- The top rounded once (never "each rounded down", which gives $110,000).
- "The bottom is the floor's figure, never what the floor pays".
- The cap and the excess going to her flexibility.
- "No figure stated before the move" (2.9%, 6.2%, 8.7% and 10.7% re-checked in `results_range_rule_2026-11-15.json`).
- Each end dated by part: the bottom to January 2028, the top to the move, her flexibility to January 2033.
- 8p's 40% fall: the top goes to $105,000, the bottom and the payments do not move.
- No "barring a US default" attached in 3c.
- The IBTM prospectus confirms NUMBERS l.242's UNVERIFIED point: costs outside the fee exist (litigation,
  extraordinary expenses, trading costs, securities lending). That clears the way to cite it once in 3e.

## Job 2: monitoring (Table 3, tables.md l.84-105, and 3e, SKELETON l.47, l.262, l.289)

The IBTA points are applied correctly:
- row 4 reads "Ending notice in September to October";
- no plan file says "on schedule" (searched SKELETON, WORDS, tables, NUMBERS, CONCEIT);
- the 19 business days are kept out of the table for space.

Row by row, against the IPS's two reasons (l.17):

| Row | Trigger observable and dated? | Action allowed by the IPS? | Verdict |
|---|---|---|---|
| 1. 2028 deposit | Yes (1 Dec 2027 warning; 31 Mar 2028) | Yes, reason 1 | Sign, after L5 |
| 2. Treasury payments | Yes (five business days) | Yes, reason 2 | Sign, after L6 |
| 3. X-date | Yes (the Treasury's estimate, else the CBO's) | Yes, nothing changes | Sign |
| 4. Fund notices | Partly (M4, M5) | Partly: the action fits a fund that moves past a payment, not an early end | Fix |
| 5. Trade days | Partly (M6) | Yes | Fix |
| 6. Yields and shares | Yes (a watch with no trigger, for scale) | Yes | Sign |
| 7. Her flexibility | Partly (M7) | Yes, an IPS l.15 use | Fix |

**M4 (MEDIUM). Row 4 gives one action for three different events, and it fits an early end badly.**
- **The plan's words:** "its money (paid out or sold) buys a Treasury due by 15 December".
- **Why it fits badly:**
  - An IBTA-type early end pays cash in early December, before the 1 January payment.
  - Buying a two-week Treasury with it is churn.
  - The money should simply wait in the Treasury-bill fund, like every other waiting dollar.
- **The fix:** split the Changes cell:
  - "Ends early: its cash waits in the bill fund to 1 January."
  - "Merges or moves past a payment: sold, and a Treasury due before the payment bought."
- **"Bill fee over 0.15%" has no action at all:**
  - Give it one: "move the waiting money to a cheaper Treasury-bill fund or to bills".
  - Name the bill fund. NUMBERS l.76 still marks its identity UNVERIFIED (it must be WInS-listed), so the row watches
    an unnamed instrument.

**M5 (MEDIUM). Row 4's watch window is too narrow, and "no notice" has no date.**
- The IBTM prospectus (27 Feb 2026) lets the board extend the end date without a shareholder vote and states no notice
  period. A merger or an extension can be announced in any year.
- "Ending notice in September to October" suits only the final-year notice.
- **The fix:**
  - "Normal: every fund filing read as it comes, any year; the ending notice in September to October of its final year."
  - "Act: no ending notice by 31 October of the final year."
- **Add the iBond fee to the trigger.** Put "iBond fee above 0.07%" beside "bill fee over 0.15%". A fee rise is one of
  the costs the 0.5% carries, and it is announced in a notice.

**M6 (MEDIUM). Row 5 has no trigger for a stressed trade day, which the register itself calls a watch item.**
- NUMBERS l.82: "A stressed purchase day (March 2020: government bond ETFs more than 1% off net asset value ...) is
  outside the haircut: a watch item, not a rule change".
- Row 5's only trigger is "A date cannot be kept (a trading halt)", and its normal is "limit orders near each holding's
  value", with "near" left undefined.
- Since card Q45, a premium does not break ownership: the ends are units x NAV. It does lower the bottom (fewer floor
  units) or the top (VT sold at a discount, IBTM bought at a premium).
- **The fix:**
  - Normal: "price within [x]% of net asset value; the ends worked out from that day's published holdings".
  - Act: "further off: limit orders, wait day by day, never past the 2031 meetings".
- The 2031 move is the trade that matters. The same row should say that VT is sold and the late-2032 fund bought on the
  same day, so no part of the top sits uninvested.

**M7 (MEDIUM). Row 7's currency trigger can be read two ways, and its "carry on while" cell is not a condition.**
- **Two readings of "10% stronger":** with "NT$32.768 per US$1" printed beside it, a reader takes "10% stronger" as
  29.49. The register means 29.79: 10% more US dollars, NUMBERS l.1038, which is what the "$11,500" assumes. Print
  "NT$ per US$ below 29.79 (9.1% under its level on the day the range is stated)", with today's level as an example.
- **Not a condition:** "NT$32.768 per US$1 (6 Nov 2026)" is a reference figure, not a condition. Write "within 9.1% of
  its level when the range is stated".
- **Vague date:** "than in 2031" should name the day: the day the range is stated, or the move's trade day.
- **No building-cost trigger:** the building-cost band (1.5% to 5.0% a year) has none to match it.
  - Keep the band and add "Look closer: a year's print above the band is a call on her flexibility, never a plan
    change". That is not a new rule (CANON A34 is about plan changes).
  - Or move the band to the note.

**M8 (MEDIUM). Nothing checks that the cash the bottom counts is kept.**
- About $15,600 of the floor's $98,874 zero-interest value is paid out monthly from 2028 to mid-2032 (check3), before
  the fund ends. The rule counts it waiting in the bill fund until December 2032 (NUMBERS l.81).
- If those payouts are swept into her spending, or into the reserve's account, the stated bottom is not owned.
- **The fix:** one line, in row 5 or in 3e's custody line: "the floor's and the moved half's monthly payouts go to the
  bill fund in the contribution's account and stay there to December 2032; checked each January against the broker
  statement".

**L5 (LOW). Row 1's Changes cell gives consequences, not the change.**
- It reads "no range until money comes; 2033's payment $3,016 short at today's rates". A desk wants the action: "money
  that comes later completes the 2033 payment first, then the extra Treasuries, then the floor and VT; no contribution
  is stated until the floor is bought".
- 3e's prose carries card Q34's point. The cell should not read as the whole response.
- Also: at no interest a missed deposit leaves the ten $57,455 short (NUMBERS l.445). "At today's rates" is right, but
  that is the kinder of the two figures.

**L6 (LOW). Row 2 says "payments ... restated".** Laura's payments are fixed at $50,000 and are never restated. Write
"Changes: each payment's cover and both ends re-checked on what was actually paid; the range restated."

**L7 (LOW). 3e's no-forced-sale clause.** l.47 says "each pays its cash before its payment date". A fund's board can move
that date (prospectus). Write "each is due to pay before its payment date (Table 3 watches a fund whose end moves)".

**L8 (LOW). Custody.**
- The custody line (l.289 item (c)) has no date. It should say "set up before the account passes SIPC's $500,000 (after
  the 2028 deposit)".
- It should name the right layer: two brokers, or confirmed excess cover. The funds' own custodians (JPMorgan, State
  Street) are a separate layer.
- "SIPC's cash limit is $250,000 against December 2032's cash": about $173,500 arrives then centrally ($50,000 for 2033
  plus the $123,476 the two funds pay). Say it sits under the limit, or that it waits in the bill fund.
- Add the yearly check of units against Table 1's targets. It is the "custodian statement" 3d offers co-sponsors as
  proof.

**L9 (LOW). IBTA's dates.** SKELETON l.289 says "15 days before its stated date (cash 3 Dec 2021 ...)".
- Fifteen days is the last trade (30 Nov); the cash came 12 days early (3 Dec), 29 calendar days (19 business days)
  before 1 January.
- Card Q3c l.33 says "paid on 3 Dec 2021, 15 days before the stated date", which contradicts its own row 7.
- Use "stopped trading 15 days early and paid on 3 December".
- WORDS l.39's "about 15 December" should read "on or about 15 December" (iShares' words), which covers IBTA.

**L10 (LOW). The note's 3.60 points.** Table 3's note says "payments hold to a 3.60-point fall before 2027". That is the
no-interest standard (NUMBERS l.431). At the interest the market expects, the figure is 3.89 points. Say which.

**L11 (LOW). The yield assumption behind the simulated futures is never named.**
- The house model moves yields 0.9 points a year in parallel, independent of shares. This is Keel's assumption, not a
  market figure (NUMBERS l.72).
- It sets every simulated-futures spread of the bottom ($85,000 at 1 in 20) and every "of 100 simulated futures"
  figure used beside Table 3's watches.
- 3e's assumption list (l.47) names 7.5%, 17.88% and independence, but not this. Add it in area (1): "yields moving
  about 0.9 points a year (our assumption)".
- Say also that the history percentages are shares of 585 overlapping starting months, not probabilities.

**Nothing else a desk would add as a row:**
- Fund closure notices, the X-date, the 2031 move's date, and the Taiwan dollar each have a row.
- Custody is rightly prose.
- VT's own events (an index change, a closure) touch only her flexibility and can stay in the store.
- None of the five T-bonds is callable.

## Scores

- **3c precision: 3 / 5.**
  - The code, the register and every 3c figure agree to the dollar (checked by an independent pricer).
  - The confidence sentence, which answers the case's own question, states the 0.5% worst-case bound as the
    outcome and drops its "if cash also earns nothing" condition (H1).
  - With H1 and M1 fixed, 3c is a 4.5.
- **3e monitoring precision: 3 / 5.**
  - The two reasons are well defined and dated, and IBTA is handled.
  - Row 4 gives an early end a sale-and-buy action it should not have and watches only Sep-Oct of the final year,
    though the board can act in any year.
  - Row 5 lacks a stressed-trade-day trigger.
  - Row 7's trigger can be read two ways.
  - Nothing checks that the floor's payouts, which the bottom counts, are kept.
