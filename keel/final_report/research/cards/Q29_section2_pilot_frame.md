# Q29: One frame for Section 2 that judges the WInS book as a build, not a bet

Wed 11 Nov 2026 (Sydney, evening run). Report parts: Section 2 (2.0 lead, 2.1 what the book is, 2.5 how well it was
implemented, Table 1), with a bridge to 3e (what to monitor). Builds on card Q17 (escrow verifier, implementation
shortfall); does not redo it.

Notes for the Final Report store, not report prose.

**Claims tested** (from the lead's brief; each to keep, kill or change)
1. Section 2 should judge the WInS book the way medicine judges a pilot or feasibility study: could each part be done,
   at what cost, against success criteria stated in advance, never by outcomes (Eldridge et al., 2016; Thabane et al.,
   2010; Leon et al., 2011). Tests: is it honest when nothing was formally pre-registered (book bought 6-7 Oct ET)? Is it
   apt for a fixed-income reader or a stretch? Does it clash with the IPS, the Trading Notes or CANON?
2. Engineering's scale-model rule (similitude) names what the $300,000 book could not show: fixed $10/$25 fees, $1,000
   bond lots, the 2028 deposit, the passage of time, the 2031 move. Choose at most one frame among this, claim 1 and
   Q17's escrow verifier, or none.
3. The frame's criteria can be stated in about five rows with values already in NUMBERS.md.

**Problem class.** Judging a small, short, simulated build of a long liability plan without treating its short-run
result as evidence. Fields that solved it:
- clinical research: pilot and feasibility trials are judged on feasibility criteria stated in advance, never on effects;
- aircraft and ship model testing: partial similitude, meaning measure what scales, calculate what does not, and add an allowance;
- municipal escrow verification: Q17's tests of dates and sufficiency;
- US adviser regulation: a model portfolio's results are "hypothetical performance" and may be shown only with their
  criteria, assumptions, risks and limitations.

## Verdicts in one screen

- **Claim 1: CHANGE. Keep the logic, drop the label.**
  - *Honest for execution only.* Criteria on file before the fills of 6-7 Oct ET:
    - the 2 Oct ticket file: five stop rules, a 25bp curve band for bonds, cash "Never below $1,000", VT as order 11 after the bonds;
    - the Portfolio tab's target units, priced on 2 Oct closes and 5 Oct bond checks.
  - *Result against them:*
    - 10 of 11 holdings at exactly the target units;
    - VT 167 shares against 164, under its own pre-set sizing rule;
    - bonds -10 to +6bp from the curve at the 5 Oct check, and 2.6-8.8bp at the fills (Q17, MODEL);
    - cash $3,513.79 at the end (NUMBERS 8g).
  - *After the fact.* The sufficiency standard ("sufficient without reinvestment", NUMBERS 0) was adopted on 10 Nov,
    after the freeze, so it must be labelled as a test made afterwards.
  - *The pilot's "progression" step clashes.* Only Thabane's outcome (iii), "continue without modifications, but
    monitor closely", is open to Caplet. "Modify" would revise the IPS (WN s.0; IPS l.17).
  - *Medicine would strike a bond reader as a stretch:* never name it in the report.
- **Claim 2: CHANGE. One frame: the scale model (partial similitude).**
  - Q17's escrow tests become its measures, and the pilot rule (criteria before results) becomes its honesty check.
  - *Coherent, not decoration.* The frozen notes already say "scaled to the model portfolio" (WN l.24), and CANON
    check 9 says "two-thirds scale".
  - *The book was a deliberate similitude trade-off.* The team's 30 Sep choice (D7) kept "all three of Laura's goals"
    at two-thirds scale and gave up the January 2027 step at full size (Book L).
  - *ITTC's split maps one to one:*
    - measured in the book: dates, instruments, order of jobs, price against the curve;
    - calculated in NUMBERS: the 2028 completion ($38,282) and backstop ($34,369) in section 2, the range in section 4,
      the reserve in 8h;
    - the allowance: the 0.5% haircut and the $885 fee cushion (NUMBERS 0, 2).
- **Claim 3: CHANGE. Five criteria; only two are fully in NUMBERS.**

  | Criterion | Result | In NUMBERS? |
  |---|---|---|
  | A. Every instrument bought | 11 of 11 | Yes: 8g |
  | B. A holding pays out before each payment | 10 of 10 | Yes in months: 8h. Exact days only in CANON B8 |
  | C. Cost | $200 in fees | Dollars yes: 8g. Basis points no: Q17, MODEL |
  | D. The rule survives the scaling | Holds as "$0 of promised money in shares, in book and plan" (IPS l.11) | SKELETON 2.1's wording reads as a weight, and as a weight it is false: VT 8.84% of the book vs 6.63% of the plan (8g) |
  | E. Bought as planned before trading | 10 of 11 at the target units | No: team record only |

  Rung coverage of 65.6-70.4% (Q17, MODEL) is also missing from NUMBERS.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A feasibility study asks whether the full study "can be done, should be done, and, if so, how"; a pilot runs the full study "or part of it ... on a smaller scale" | Eldridge et al. (2016), introduction and scope | PROCESS, CERTAINTY | KNOWN | Section 2's question becomes "could each part of Laura's plan be bought and held as the IPS says, at what cost", not "did the book make money" | No later "definitive trial" follows: Laura's January 2027 purchase is the real thing, and the book's result never decides whether it goes ahead | VERIFIED (BMJ full text, main article) | no | https://www.bmj.com/content/355/bmj.i5239 |
| 2 | Pilots do no formal test of effect: "A pilot study is not a hypothesis testing study. Safety, efficacy and effectiveness are not evaluated in a pilot." | Leon et al. (2011), abstract and text; Eldridge et al. (2016), Box 1 ("Formal hypothesis testing for effectiveness (or efficacy) is not recommended") | CERTAINTY | KNOWN | The same rule Wharton sets ("WInS gains and losses are not treated as evidence", WN s.0), reached on its own by another field: the rule is principled, not a convenience | Wharton already says it; quoting medicine adds nothing a judge needs | VERIFIED (PMC author manuscript, full; BMJ full text) | no (agrees with WN s.0) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3081994/ |
| 3 | Small samples give no "meaningful effect size estimate ... due to the imprecision inherent in data from small samples" | Leon et al. (2011) | CERTAINTY, LADDER | KNOWN | A month of WInS prices says nothing about 2027-2042. The fill day was cheap: the ten payments cost $288,510 on 7 Oct (NUMBERS 8b), and the ten cost under $300,000 on only 37 of 214 closes in 2026; NUMBERS 8b calls it "luck of timing, not skill" | Leon is about effect sizes used to plan sample size, not prices; the parallel is the logic (too short to learn the result), not the statistics | VERIFIED (PMC full; NUMBERS 8b) | risk: any line that credits the cheap fill to the team breaks NUMBERS 8b | PMC3081994; NUMBERS 8b |
| 4 | Pilot results shown to funders "tend to be selective, overly optimistic and, at times, misrepresentational"; a public protocol "reduces the chance of selective reporting to suggest 'better' results" | Leon et al. (2011); Eldridge et al. (2016), item 24 | PROCESS, PRESENTATION | KNOWN | Report every pre-set measure, including those that look worse: VT 3 shares over target; four orders cancelled and placed again (SNAP l.42-44); the Feb-2037 bond pays out 10.5 months early (NUMBERS 8h) | Section 2 has 2-3 pages; one table row per measure is enough | VERIFIED (both read in full) | no | PMC3081994; bmj.i5239 |
| 5 | Pre-set criteria decide "whether, or how, to proceed" (item 6c); they are often best read "as guidelines rather than strict thresholds", and many teams use a traffic-light system | Eldridge et al. (2016), items 6c and 22 | PROCESS, PRESENTATION | KNOWN | A "met / partly met" column for the five criteria (rows 29-33); "partly" for the two bond rungs that pay out months early | Coloured lights in a Times New Roman report look like a dashboard; the words are enough | VERIFIED (BMJ full text) | no | bmj.i5239 |
| 6 | Thabane: "It is always important to state the criteria for success of a pilot study"; four outcomes: stop; continue but modify protocol; continue without modifications but monitor closely; continue without modifications | Thabane et al. (2010), section 6 | TWOREASONS, PROCESS | KNOWN | Only outcome (iii) fits: the plan goes ahead as written, and 3e watches named items (the ladder's cost against $300,000 on 1 Jan 2027, the 2028 deposit, the floor fund's payout). A clean hand-off from 2.5 to 3e | Outcome (ii) would be a revision of the IPS | VERIFIED (BMC full text and its 2023 correction) | risk: "modify" clashes with WN s.0 ("not an opportunity to create a new strategy or revise the IPS") and IPS l.17 ("only 2 possible reasons") | https://doi.org/10.1186/1471-2288-10-1 |
| 7 | A pilot report states "implications for progression ... including any proposed amendments" (item 22a) | Eldridge et al. (2016), item 22a | COMPLETE2028, TWOREASONS | KNOWN | The only "amendment" the frozen texts allow is already in the IPS: a ladder costing more than $300,000 is completed with the 2028 deposit (IPS l.13) | A pilot that may amend nothing is not quite a pilot; that is why the label is dropped (claim 1) | VERIFIED (BMJ full text) | clash: only if Section 2 proposes any change to holdings or rules (WN s.0; IPS l.17) | bmj.i5239 |
| 8 | Changes to methods after the start are reported "with reasons" (item 3b) | Eldridge et al. (2016), item 3b | PROCESS | KNOWN | Two in-flight changes are on Caplet's record: four orders cancelled and placed again on 6-7 Oct ET (SNAP l.42-44), and the rule after the 7 Oct mis-click that only Ray places or cancels orders (EXPERIENCE_RECORD l.26). One clause in 2.5; the story belongs to 3f | Overlaps Team Reflection; never tell the event twice | VERIFIED (BMJ; repo files) | risk: double use with 3f | bmj.i5239; `competition/wins/2026-10-23_snapshot.md`; `research/EXPERIENCE_RECORD.md` |
| 9 | Report limitations "and remaining uncertainty about feasibility"; separate limits a full study can overcome from those it cannot; say how far pilot findings carry (items 20, 21) | Eldridge et al. (2016), items 20 and 21 | PROCESS, CERTAINTY | KNOWN | Split what the book could not show into two groups. Calculated elsewhere: the 2028 completion, backstop, waiting money and 2031 move (NUMBERS 2, 4, 8h). Not knowable until the day: the 1 Jan 2027 curve, and whether the 2028 deposit arrives (NUMBERS 5) | The same content as the scale-model split (row 19); use one vocabulary, not two | VERIFIED (BMJ full text) | no | bmj.i5239 |
| 10 | Four reasons to run a pilot: process, resources, management, scientific | Thabane et al. (2010), section 3 | PROCESS | KNOWN | A checklist for notes on what the book tested: process (names, coupons and maturities, stale quotes caught), resources (fees, lots, cash), management (who places orders; a 00:30 Sydney market open). Not scientific: no effect was measured | Four headings is a framework, and Section 2 has no room for one; use it to sort notes only | VERIFIED (BMC full text) | no | 1471-2288-10-1 |
| 11 | A pilot that shows a step cannot work "is a success"; "Can I use the results of a pilot study to treat my patients? Not a good idea!" | Thabane et al. (2010), section 7 | PROCESS | KNOWN | The failed checks were the method working: on 29 Sep WInS prices, the Feb-2038 and Feb-2036 bonds failed the 25bp curve check (-92bp, -111bp, marked "FAIL (stale or wrong)"), and neither was bought | The record does not say IBTR was picked because Feb-2036 failed (CANON D13 says "a choice"); never link the two | VERIFIED (BMC; ticket file l.105-106) | risk: overclaiming IBTR's reason against CANON D13 | `archive/rab/trades/tickets.md` l.105-106 |
| 12 | Pilots measure fidelity and adherence: "Fidelity rates per unit monitored"; "Rates of adherence to protocol" | Leon et al. (2011), Table 1 | PROCESS, LADDER | KNOWN | Book against targets: IBTM 4,503; IBTO 1,024; IBTP 927; IBTQ 894; IBTR 853; bonds 20/20/18/18/20 lots of $1,000. All ten Treasury holdings exactly at target; VT 167 against 164 | The target sheet was exported on 14 Oct, after the fills. Its prices (2 Oct closes, bond checks "5 Oct") show the targets were set before trading, but the repo holds no copy from before the fills | VERIFIED (Leon full; portfolio.csv l.20-31; SNAP l.22-32) | no | `caplet/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv`; SNAP |
| 13 | Execution rules on file before any order: five stop rules "read aloud before the first order" (name; total within the stop band; price, with bonds inside a 25bp curve band; cash "Never below $1,000"; no repeats, no same-day sells) | Pre-trade ticket file (trade date Fri 2 Oct; basis 28 Sep closes) | PROCESS | NICHE | These are the success criteria a pilot needs, and the book met them: bonds -10 to +6bp at the 5 Oct check (portfolio.csv l.25-29), 2.6-8.8bp at the fills (Q17, MODEL); cash $3,513.79 (NUMBERS 8g); no sale ever | The 2 Oct ticket sizes differ (IBTM 4,486; bonds 19/17/18/19/20) and were re-sized on later prices before trading. Whether every rule was read aloud is not recorded | VERIFIED (repo files) | no | `archive/rab/trades/tickets.md` l.7-13 |
| 14 | The order of jobs was set in advance and kept: VT is "order 11, placed in the session after the bonds fill ... so WInS Order History shows the payments and the floor bought before any stocks, as the IPS says", sized "from the cash then left" | Pre-trade notes file, l.12 and l.284 | PROCESS, CEILING | NICHE | Fills: the first two were the longest bonds (Nov-2041 at 7:55 PM ET and Nov-2040 at 7:59 PM ET, 6 Oct), and VT came last (8:27 PM ET, 7 Oct) (SNAP l.48-58). This matches NUMBERS 1's build order, "longest rungs first" | The planned day was Mon 5 Oct ET and the trades ran 6-7 Oct: the order held but the day moved. The four re-placed orders reshuffled the middle | VERIFIED (repo files) | no | `archive/rab/trades/notes.md` l.12, l.284; SNAP |
| 15 | Honesty test: which criteria came before trading and which after | This card; NUMBERS 0; Q17 | PROCESS, REINVEST | NICHE | Before (2-5 Oct): units, band, cash floor, order of jobs. After: Q17's measures (9 Nov) and the completion standard "sufficient without reinvestment" (NUMBERS 0, Tue 10 Nov). In 2.5 the second group carries a label saying it was measured afterwards | A judge may still read tests made afterwards as hindsight; the label is the defence | VERIFIED (repo) | risk: presenting the escrow test as a criterion the book was built to. The book followed WN l.24 ("with reinvested coupons funding part of each") | NUMBERS 0; Q17 |
| 16 | Medicine as a named frame would strike a bond reader as a stretch | Panel bond-desk judge (asks for per-rung coverage, the duration gap, "no provision for reinvestment", cost in bp) | PRESENTATION | KNOWN | Keep the logic (criteria before results; feasibility, not effect) but never the words "pilot", "trial" or "CONSORT". Plain words for fidelity: "bought as planned" | The pilot logic is still the honesty rule behind 2.5 | VERIFIED (panel files) | no | `research/panel/2026-11-09_judge_*.md` |
| 17 | "Any one experimental technique will not satisfy all the similitude requirements"; "Most tests are designed for certain similitude conditions at the expense of other parameters" | Wolowicz et al. (1979), introduction | PROCESS, LADDER, FLOOR, CEILING | NICHE | Caplet's 30 Sep choice was this trade-off. The Portfolio tab book shows "all three of Laura's goals: the payments, the floor (IBTM) and the stock fund (VT)" at two-thirds scale, at the expense of the January 2027 step at full size (Book L, "the literal first step") (D7) | Engineers choose conditions in order to predict full-scale behaviour. Caplet chose them to show the plan's shape, and Wharton bars predicting returns from the book | VERIFIED (NASA TP-1435: introduction, similitude and Reynolds number sections, concluding remarks) | no (agrees with CANON D3 and check 9) | https://ntrs.nasa.gov/api/citations/19790022005/downloads/19790022005.pdf; `archive/rab/decisions/D7_wins_book.md` l.8-16 |
| 18 | "One of the prime factors necessary to determine the limitations of data obtained from a model is the degree to which the similitude requirements have been met" | Wolowicz et al. (1979), introduction | PROCESS, PRESENTATION | NICHE | Gives 2.5 its order. First what matched (dates, instrument types, order of jobs, no promised money in shares), then what did not (lots, fixed fees, the VT weight, time, the 2028 deposit) | "Similitude" is jargon; it never appears in the report | VERIFIED (NASA TP-1435 introduction) | no | NASA TP-1435 |
| 19 | Test what scales, calculate what does not, add an allowance. The model is towed "at speeds corresponding to the same Froude numbers as for the full-scale ship"; the wave part is measured on the model, the friction part is calculated at ship scale from the ITTC-1957 line, and a "model-ship correlation allowance" (C_A) is added | ITTC (2021), sections 3.1-3.6.3 | LADDER, COMPLETE2028, FLOOR, PROCESS | NICHE | Measured in the book: each holding buyable, its maturity before its payment, its price near the curve. Calculated: completion $38,282 and backstop $34,369 (NUMBERS 2), the 2031 range (NUMBERS 4), the reserve (NUMBERS 8h). Allowance: the 0.5% haircut on each range end ("It carries the fund risks a bond does not have", NUMBERS 0) and the $885 fee cushion (NUMBERS 2) | The ship's friction line is a physical law fitted to data; Caplet's calculations are models with stated limits (NUMBERS 7) | VERIFIED (ITTC PDF read in full) | no | https://ittc.info/media/11780/75-02-02-01.pdf |
| 20 | Small-model effects come from granularity: bonds trade in $1,000 lots, so each rung holds 65.6-70.4% of a full $50,000 rung, not exactly 66.7%; scaled up by 1.5, the 2040 rung pays $49,165 ($835 short) | Q17 l.159, l.193 (MODEL, register engine) | LADDER | NICHE | Call it a model-size effect, like Reynolds effects on a small hull: it disappears at full size, where Laura's rungs are bought at $50,000 scale (in the plan: "$0 short in every test", NUMBERS 2) | Not in NUMBERS; Q17 MODEL only. CLAUDE.md's "67-72%" is wrong (Q17) | VERIFIED (Q17 l.159, l.193; MODEL, not in NUMBERS) | no | Q17 |
| 21 | What matched exactly: the dates (each holding ends on its real date, so time is not scaled), instrument types (iBond ETFs for 2033-2037, bonds for 2038-2042), the order of jobs, and the IPS rule "only money you haven't promised yet goes into shares" (IPS l.11) | CANON Table E, D13; NUMBERS 8g, 8h; SNAP | LADDER, FLOOR, CEILING | NICHE | These are the features a judge can check in Table 1 | In the book one IBTM holding does two jobs (1,142 shares for the payment, 3,361 for the floor; portfolio.csv l.38-39); in the plan the floor shares are a second lot bought in January 2028 (CANON Table E) | VERIFIED (repo) | risk: call the book's floor shares a "stand-in" (SNAP), never Laura's floor | CANON; SNAP; portfolio.csv |
| 22 | What did not scale: fixed fees; $1,000 lots (row 20); the VT weight; time (one month of trading against sixteen years); the 2028 deposit; the backstop; waiting money; the 2031 move; the NAV payout (NUMBERS 3) | CANON Table E; NUMBERS 3, 8g | LADDER, COMPLETE2028, MOVE2031, RESERVE2033, REINVEST | NICHE | One list in one place (2.5), each item with where it is calculated. Fees: $200 is 0.07% of $300,000; the same eleven trades would be about 0.04% of $450,000 (arithmetic on 8g, not in NUMBERS). VT: 8.84% of the book, 6.63% of the plan (8g) | WInS fees are the game's, not Laura's broker's; the 0.04% is illustration only | VERIFIED (repo) | risk: Section 2 must never say the frozen weights equal the plan (NUMBERS 8g) | CANON Table E; NUMBERS 8g |
| 23 | The price level on the test day does not carry over: the ten payments cost $288,510 at the fills (7 Oct) and $301,544 on 6 Nov; the ladder's cost moved $37,625 through 2026 | NUMBERS 1, 8b | LADDER, COMPLETE2028, CERTAINTY | KNOWN | Like the weather on a sea trial: a condition of the test day, not a property of the design. The 1 Jan 2027 curve decides Laura's cost, and the IPS's completion clause covers a higher one | None recorded | VERIFIED (NUMBERS 1, 8b) | no | NUMBERS 1, 8b |
| 24 | The disanalogy is useful in itself: a model test predicts full-scale behaviour, but the WInS book must not. Mach-scaled model data "may not be representative" where other conditions were not met | Wolowicz et al. (1979), concluding remarks; WN s.0 | CERTAINTY | KNOWN | The frame holds for building only: the book shows the plan can be bought in the right order at a known cost, and nothing about returns | Without this line the frame could be read as a claim that the book "proves" the plan | VERIFIED (NASA concluding remarks) | no | NASA TP-1435 |
| 25 | Extrapolating model results "alone to full scale could produce highly erroneous results" (C-141 example) | Wolowicz et al. (1979), Reynolds number section | CERTAINTY | KNOWN | Never scale the book's WInS gain, or its cheap fill, up to Laura's money | Repeats rows 3 and 23; keep as support, not as its own report point | VERIFIED (NASA Reynolds number section) | no | NASA TP-1435 |
| 26 | A US regulator's definition: "Hypothetical performance means performance results that were not actually achieved by any portfolio of the investment adviser", including "Performance derived from model portfolios" | 17 C.F.R. § 275.206(4)-1(e)(8) | CERTAINTY, PRESENTATION | KNOWN | The finance version of Wharton's rule: a virtual book is a model portfolio, and its gains are hypothetical in a regulator's sense | The rule governs registered advisers' advertisements. Caplet is not an adviser and the report is not an advertisement; never cite the rule as binding | VERIFIED (eCFR page read in full, up to date as of 5 Nov 2026) | no | https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 |
| 27 | Hypothetical results may be shown only with "sufficient information ... to understand the criteria used and assumptions made" and "the risks and limitations of using such hypothetical performance" | 17 C.F.R. § 275.206(4)-1(d)(6)(ii)-(iii) | PRESENTATION, PROCESS | KNOWN | The three things Table 1's note must carry: the scale (300/450); the prices and dates used (cost at the fills, 6-7 Oct ET); and what the book cannot show (row 22) | The same content as the scale-model split; it adds a source a bond judge knows | VERIFIED (eCFR full) | no | eCFR |
| 28 | Q17's escrow tests become measures inside the frame, not a rival frame. The date test applies to the book (10 of 10). Sufficiency without reinvestment is the plan's standard, met by the 2028 completion and backstop | Q17 (Moody's, 2020); NUMBERS 0, 2, 8a | LADDER, REINVEST, CERTAINTY | NICHE | 2.5 says the book passes the date test as built. Sufficiency belongs to the plan: own rungs $445,405 plus backstop $56,009 at 0% (NUMBERS 8a), "$0 short in every test" (NUMBERS 2) | Two frames would compete for about 650 words; use one frame and one set of measures | VERIFIED (Q17; NUMBERS 2, 8a) | risk: judging the book as failing sufficiency reads as the IPS failing; the book was built to WN l.24 | Q17; NUMBERS |
| 29 | Criterion A: every instrument of the strategy was bought on WInS | NUMBERS 8g (holdings table at cost); SNAP l.48-58 | LADDER, FLOOR, CEILING | TEXTBOOK | 11 of 11 filled on 6-7 Oct ET; none after 8 Oct | "Tested" in SKELETON 2.1 must mean bought and held at the planned size and price, never performance | VERIFIED (NUMBERS 8g present) | no | NUMBERS 8g |
| 30 | Criterion B: each payment has a holding that pays out before it | NUMBERS 8h ("How early each pays out before its payment"); NUMBERS 1 (rung table); CANON B8 | LADDER, CERTAINTY | TEXTBOOK | 10 of 10. iBond ETFs about half a month early; November bonds 1.5 months; May-2038 7.6 months; Feb-2037 10.5 months (NUMBERS 8h) | Exact days (17, 47, 231, 320) are in CANON B8, not NUMBERS, so they are missing there. IPS l.13's "just before it's needed" holds only PARTLY (CANON B8) | VERIFIED (NUMBERS 8h, in months) | risk: "just before" is overstated for two rungs (CANON B8) | NUMBERS 8h l.769 |
| 31 | Criterion C: cost in dollars and in basis points | NUMBERS 8g ($200 commissions; $1,109.42 accrued interest); Q17 l.160 | PROCESS | TEXTBOOK | Dollars are present. Basis points are missing: 0.07% in commissions, bonds 2.6-8.8bp from the curve, and about $250 (0.08%) in all are Q17 MODEL only | The bond-desk judge asks for bp (panel) | VERIFIED (NUMBERS 8g for dollars only; bp are Q17 MODEL) | no | NUMBERS 8g; Q17 |
| 32 | Criterion D: the IPS's rule survives the scaling, worded as "promised money held in shares: $0, in the book and in the plan" | IPS l.11; NUMBERS 8g; SKELETON 2.1 | CERTAINTY, HALFKEPT, CEILING | NICHE | Every promised dollar is in Treasuries in both; shares hold only unpromised money | SKELETON's "promised money's share in Treasuries unchanged" reads as a weight to a fresh reader, and as a weight it is false: Treasuries are 89.55% of the book, and VT is 8.84% of the book against 6.63% of the plan (8g) | VERIFIED (NUMBERS 8g; IPS) | risk: clash with NUMBERS 8g ("Section 2 never says the frozen weights equal the plan") if worded as a weight | NUMBERS 8g; SKELETON l.27 |
| 33 | Criterion E: bought as planned before trading | portfolio.csv l.20-31; SNAP l.22-32; ticket file l.7-13 | PROCESS, LADDER | NICHE | 10 of 11 holdings at exactly the target units; VT 3 shares over, under its own sizing rule; bond prices inside the band; cash never below $1,000 | Missing from NUMBERS: it needs a line in 8g (or a new 8l) before it can be a figure in the report | VERIFIED (repo files) | no | portfolio.csv; SNAP |
| 34 | Table 1's label answers the fresh reader's "is this the real plan or a scaled copy?": name the scale on the exhibit and add a "Pays for" column | Fresh-reader exhibit panel (11 Nov); CANON check 9 | PRESENTATION | KNOWN | The exhibit title names the plan after both deposits, the two-thirds scale, and "at cost on the original $300,000" (wording settled on 27 Nov) | Wharton's table must total $300,000 and 100% (WN s.0); naming the scale does not change that | VERIFIED (panel file; CANON) | no | `research/panel/2026-11-11_fresh_reader_exhibits.md` |

## (b) Cards

**1. Partial similitude: test what scales, calculate what does not, add an allowance (rows 17-25). The frame.**
- *What is it?* Model ships and aircraft cannot match every scaling law at once. Froude and Reynolds numbers cannot
  both be matched on a small hull. So the towing tank matches one (Froude), measures the part that obeys it, calculates
  the rest at full scale by an agreed formula, and adds a correlation allowance for what neither captures (ITTC, 2021).
  NASA's survey says the same of aircraft: "Most tests are designed for certain similitude conditions at the expense of
  other parameters", and the limits of model data depend on "the degree to which the similitude requirements have been
  met" (Wolowicz et al., 1979).
- *Did it work?* Yes. It has been standard towing-tank practice for decades (the ITTC-1957 line is still in the 2021
  procedure). NASA records where it failed: extrapolating one technique alone "could produce highly erroneous results".
- *How is Laura's case like it?* The book is a two-thirds-scale copy of the plan after both deposits (CANON D3, check
  9; WN l.24 "scaled to the model portfolio"). The team chose which conditions to keep on 30 Sep (D7): all three goals
  visible, at the expense of the January 2027 step at full size. The dates, instruments and order of jobs match exactly.
  Lots, fees, time, the 2028 deposit and the 2031 move do not match, and NUMBERS calculates them.
- *How is it not?* A model hull predicts the ship's resistance; the book predicts nothing about returns (WN s.0). The
  frame holds for building only. Engineering's formulas are physical laws; Caplet's are models with stated limits (NUMBERS 7).
- *What Caplet takes.*
  - 2.1: one sentence naming the scale and why.
  - Table 1: the scale in the title, plus a "Pays for" column.
  - 2.5: ordered as matched, then not matched with where each is calculated, then the allowance (0.5% haircut, $885
    fee cushion).
  - No engineering words in the report.

**2. Criteria set before trading, and fidelity to them (rows 12-15, 33). The finding that changes 2.5 most.**
- *What is it?* Pilot science judges a small run on fidelity and adherence to a pre-set protocol (Leon et al., 2011,
  Table 1). It warns that results told afterwards "tend to be selective, overly optimistic".
- *Did it work?*
  - Caplet's record holds criteria dated before the fills: the 2 Oct ticket file (five stop rules, 25bp band, cash
    floor), the order of jobs (VT last), and the Portfolio tab's target units on 2-5 Oct prices.
  - The book met them: 10 of 11 holdings at exactly the target units, VT 3 shares over under its sizing rule, bonds
    inside the band, cash $3,513.79, VT bought last.
- *How is Laura's case like it?* Section 2 must "evaluate how effectively it implemented the investment strategy" (WN
  s.0). Measuring against the team's own pre-set targets does exactly that and uses no WInS gain.
- *How is it not?* Nothing was registered with a third party. The target sheet in the repo is a 14 Oct export, so the
  pre-fill date of the units rests on their price dates. The sufficiency standard came on 10 Nov.
- *What Caplet takes.*
  - 2.5: one line on "bought as planned" (10 of 11; VT by rule), the measures made afterwards labelled as such, and
    the failed stale-bond checks as the method working.
  - NUMBERS needs the fidelity line before any of this becomes a report figure.

**3. Only "continue as written, monitor closely" (rows 6-7). The bridge to 3e.**
- *What is it?* Thabane et al. (2010) give a pilot four possible outcomes. Eldridge et al. (2016) ask for
  "implications for progression ... including any proposed amendments".
- *Did it work?* Yes in medicine. A progression statement makes the pilot's purpose explicit.
- *How is Laura's case like it?* After 2.5 the reader asks "so what happens in January 2027?" Outcome (iii) answers
  it: the plan goes ahead as written, and the items to watch are 3e's (ladder cost on 1 Jan 2027, the 2028 deposit, the
  floor fund's payout).
- *How is it not?* Caplet may amend nothing (WN s.0; IPS l.17). The IPS's completion clause (l.13) is the only flex,
  and it is not an amendment.
- *What Caplet takes.* The last line of 2.5 hands off to 3e. No "we would change" or "next time we would buy"
  sentence in Section 2, ever.

**4. Hypothetical performance, as a regulator defines it (rows 26-27).**
- *What is it?* The SEC's marketing rule calls results "not actually achieved by any portfolio" hypothetical, model
  portfolios included. They may be shown only with their criteria, assumptions, risks and limitations.
- *Did it work?* It has been law since 2021 (amended 2022); I did not look at how it is enforced.
- *How is Laura's case like it?* It gives a finance-native source for Wharton's rule and for the content of Table 1's note.
- *How is it not?* It binds registered advisers' advertising, which Caplet is not doing.
- *What Caplet takes.* The three-part note under Table 1 (scale; prices and dates; what the book cannot show). Cite
  the rule only if a References entry helps; never as binding.

**5. Five criteria, and the two NUMBERS gaps (rows 29-33).**
- *What is it?* The checklist claim 3 asked for.
- *Did it work?* Partly. A and B are in NUMBERS (8g, 8h). C has dollars but no basis points. D needs rewording. E is
  not in NUMBERS.
- *How is Laura's case like it?* Every criterion is about building the plan, none about returns.
- *How is it not?* B's "before" is weeks to months early for two bond rungs (CANON B8 PARTLY).
- *What Caplet takes.* Table 1's note or a five-line list in 2.5, once NUMBERS holds C's bp, E's fidelity and the
  rung coverage.

## (c) Verdicts

**Claim 1, the pilot frame: CHANGE.**
- *Apt in logic.* Three independent sources say a small early run is judged on feasibility against stated criteria,
  never on effect (Eldridge Box 1; Thabane s.6; Leon abstract). That is Wharton's rule for WInS gains.
- *Honesty test, partly passed.*
  - Before the fills: the 2 Oct ticket file (five stop rules, 25bp band, cash floor) and the pre-trade notes file (VT
    as order 11, sized from cash left).
  - Priced before the fills: the Portfolio tab's target units (2 Oct closes, 5 Oct bond checks), though the export
    holding them is from 14 Oct.
  - After the fact: the sufficiency standard (NUMBERS 0, 10 Nov) and Q17's measures (9 Nov). Label them as measured
    afterwards. Never imply they were the book's design target; the book followed WN l.24.
- *Clash.* A pilot's progression step invites "modify". The frozen texts allow only "continue as written". Thabane's
  outcome (iii) is the safe form and leads into 3e.
- *Aptness for a bond reader.* A stretch. The panel's bond-desk judge asks for coverage per rung, the duration gap and
  cost in bp. "Pilot" and "trial" would read as borrowed. Keep the logic; drop the words.

**Claim 2, the scale model: CHANGE (choose it as the one frame).**
- *Why this frame over the other two:*
  - It is Caplet's own description already: WN l.24 "scaled to the model portfolio"; CANON check 9 "two-thirds scale";
    D7's choice.
  - A bond reader knows "model portfolio".
  - It answers the fresh reader's first confusion ("is this the real plan or a scaled copy?").
  - It sorts 2.5's limits list without extra words.
- *Why not the escrow verifier as the frame:* it judges sufficiency, which the book was never built to. Its tests
  serve as measures inside the scale model: the date test on the book, sufficiency on the plan.
- *Why not the pilot as the frame:* it supplies the honesty rule and the hand-off to 3e, but its vocabulary is
  medical (claim 1).

**Claim 3, five criteria from NUMBERS: CHANGE.**
- A (11 of 11, 8g) and B (10 of 10 in months, 8h) are ready.
- C has dollars (8g) but its bp sit in Q17 MODEL.
- D's SKELETON wording ("promised money's share in Treasuries unchanged") reads as a weight, and as a weight it is
  false (8.84% vs 6.63%, 8g). Reword it as "$0 of promised money in shares, in book and plan".
- E (fidelity) is not in NUMBERS at all.
- Two register additions are needed before 27 Nov: basis-point costs and rung coverage from Q17, and the fidelity
  line from the team record.

## (d) Gaps

- **Finance sources not read at the source here:**
  - GIPS 2020's provisions on model, hypothetical or simulated performance;
  - Evans (2010) on mutual-fund incubation bias (Journal of Finance 65(4));
  - Perold (1988), carried from Q17 and REFERENCES_APA entry 102 without re-reading;
  - Moody's (2020), carried from Q17.
- **Purdue partial-similarity lecture notes (Wassgren):** seen only in search excerpts. UNVERIFIED and not used.
- **NASA TP-1435:** read the introduction, the similitude and Reynolds number sections and the concluding remarks,
  not every table and nomograph.
- **Retraction checks:**
  - Crossref records (which carry Retraction Watch data) show no retraction for Eldridge et al. (2016), Thabane et al.
    (2010) or Leon et al. (2011).
  - Thabane has a 2023 correction that changes only a worked sample-size example (75 to 289 patients), not anything
    used here.
  - The Retraction Watch database itself was not queried directly.
- **Timing of the targets:** no copy of the target units dated before the fills is in the repo (the export is 14 Oct,
  and git history begins with a 26 Oct merge). Their pre-fill date rests on their price dates and on the 2 Oct ticket
  file.
- **Whether the five stop rules were read aloud** on the night is not recorded.
- **Laura's real broker costs** are outside the case. WInS fees are the game's, so fee comparisons across scales are
  illustration only.
- **NUMBERS lacks:** fidelity to target units; costs in basis points; rung coverage 65.6-70.4%; exact days early per
  rung (CANON B8 has them).
- **REFERENCES_APA.md** holds none of this card's new sources. Entries are below for the lead to add.

## Sources (APA 7; all accessed 11 Nov 2026)

- Eldridge, S. M., Chan, C. L., Campbell, M. J., Bond, C. M., Hopewell, S., Thabane, L., & Lancaster, G. A. (2016).
  CONSORT 2010 statement: Extension to randomised pilot and feasibility trials. *BMJ, 355*, Article i5239.
  https://doi.org/10.1136/bmj.i5239 (read in full at https://www.bmj.com/content/355/bmj.i5239; Crossref: no
  retraction or update recorded.)
- International Towing Tank Conference. (2021). *Resistance test* (ITTC Recommended Procedures and Guidelines
  7.5-02-02-01, Rev. 05). https://ittc.info/media/11780/75-02-02-01.pdf (read in full.)
- Investment adviser marketing, 17 C.F.R. § 275.206(4)-1 (2022).
  https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 (eCFR text up to date as of 5 Nov
  2026; adopted 86 FR 13024, 5 Mar 2021, amended 87 FR 22447, 15 Apr 2022; read in full.)
- Leon, A. C., Davis, L. L., & Kraemer, H. C. (2011). The role and interpretation of pilot studies in clinical
  research. *Journal of Psychiatric Research, 45*(5), 626-629. https://doi.org/10.1016/j.jpsychires.2010.10.008 (read
  in full as the PMC author manuscript, https://pmc.ncbi.nlm.nih.gov/articles/PMC3081994/; Crossref: no retraction
  recorded.)
- Thabane, L., Ma, J., Chu, R., Cheng, J., Ismaila, A., Rios, L. P., Robson, R., Thabane, M., Giangregorio, L., &
  Goldsmith, C. H. (2010). A tutorial on pilot studies: The what, why and how. *BMC Medical Research Methodology, 10*,
  Article 1. https://doi.org/10.1186/1471-2288-10-1 (read in full; Crossref: no retraction.)
- Thabane, L., Ma, J., Chu, R., Cheng, J., Ismaila, A., Rios, L. P., Robson, R., Thabane, M., Giangregorio, L., &
  Goldsmith, C. H. (2023). Correction: A tutorial on pilot studies: The what, why and how. *BMC Medical Research
  Methodology, 23*, Article 59. https://doi.org/10.1186/s12874-023-01880-1 (read in full.)
- Wolowicz, C. H., Bowman, J. S., Jr., & Gilbert, W. P. (1979). *Similitude requirements and scaling relationships as
  applied to model testing* (NASA Technical Paper 1435). National Aeronautics and Space Administration.
  https://ntrs.nasa.gov/api/citations/19790022005/downloads/19790022005.pdf (read in part: introduction, similitude
  requirements, Reynolds number section, concluding remarks.)
- Carried from other cards, not re-read in this run:
  - Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *The Journal of Portfolio Management,
    14*(3), 4–9. https://doi.org/10.3905/jpm.1988.409150 (REFERENCES_APA entry 102.)
  - Moody's (2020), as cited in card Q17.
- Repo records used (not references):
  - `caplet/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv`;
  - `archive/rab/trades/tickets.md`, `archive/rab/trades/notes.md`, `archive/rab/decisions/D7_wins_book.md`;
  - `competition/wins/2026-10-23_snapshot.md`;
  - `keel/final_report/NUMBERS.md` (sections 0, 1, 2, 3, 4, 7, 8a, 8b, 8g, 8h), `CANON.md`, `SKELETON.md`;
  - panel files of 9 and 11 Nov.
