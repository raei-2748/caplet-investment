# RAB Kit pre-mortem

WS0, written 2026-09-30 (Sydney) before any stream output exists. Expands RUN_PLAN s6. AI-generated planning
material for Team Caplet; no deliverable text.

**The question.** It is 7am. The RAB Kit failed or embarrassed the team: in Friday's WInS trades (Fri 2 Oct ET), in
the Trading Notes Analysis (due 23 Oct), or later in front of judges. What went wrong?

**Errata, 30 Sep 2026 (Gate D, WS7-fixer).** Written before the Gate A lock. Where an item and this block disagree,
this block wins; later agents quote only `rab/numbers*.yaml` `quote_as` strings.
- **PM-03:** the locked Portfolio book costs $294,764.50 with $200 commission and leaves $5,235.50
  (`wins.portfolio.cost_close_0928`); the cash is used up by a parallel fall of 27.6bp (`wins.portfolio.cash_margin`).
- **PM-22:** the three history claims are REPRODUCED on the STRIPS basis (`history.cost_2020_median` $458,828,
  `history.days_priced_since_2000` 6,688, `history.cheapest_since` 28 May 2002). Closed for code; the basis is
  stated in the Final Report.
- **PM-23:** the reinvestment table is the locked `reinvest.bookL_delivered` (about $503,000 / $479,000 / $466,000 /
  $447,000 at own yields / two points lower / 2% / 0%; $507,000 at curve forwards). The pre-lock figures in the item
  are superseded.
- **PM-32:** reconciled: **about 1 in 3** (`ws4.gap_odds_2027` 0.3266). The 24.2% figure is superseded.

**How to use this file.** Every later agent applies the *Check* column for the items it touches. Gate owners tick
them at Gates A-D. Items marked *Gate C* become automated checks (spec at the end).

**Scale.** L = likelihood if nobody applies the check: H likely, M plausible, L unlikely.
I = impact: **H** = breaks a WInS or Wharton rule, puts a permanent error into a scored deliverable, or makes a
false claim a judge can catch; **M** = costs quality points or forces Friday rework; **L** = cosmetic or easy to undo.
Ratings are WS0 judgement, not measured probabilities.

**Not repeated here.** insight_v1's `phase_E/E5_premortem.md` already covers team-process risks (IPS page fit and
word counts, roles, exam weeks, roster and title page, deadlines). Its "cheap-and-fatal" items still stand. Ray has
said voice and ownership matter from the semifinals, so they are not scored risks here; the AI-citation rule still is.

**Sources read for this file (30 Sep 2026):** RUN_PLAN.md; the official case, Guide, IPS and TN instructions in
`competition/official/2026_27/`; the SMApply FAQ (https://wghsinvcomp.smapply.us/res/p/faqs/, fetched 30 Sep 2026);
the Sheet `1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM` tabs Portfolio, Book L, WInS Notes, Trade Log, TN Analysis
(read-only, 30 Sep); the IPS Google Doc (read-only, 30 Sep) and exemplar v14 on Drive; insight_v1 files named below;
yfinance and Longbridge quotes (30 Sep). WS0's own rough checks: `rab/premortem_checks.py` (no network; output
quoted below as [1]-[3]). Those rough numbers are for sizing risks only. WS1 owns every headline number.

---

## The most likely failure story

The trades went in, but three small things stacked up. The notes named the strategy "Root-and-Branch" while the IPS
the team later wrote said "Roots First". One note, pasted into the 300-character box, lost its last clause and nobody
checked the saved text before submitting the TN Analysis. And a judge who knows fixed income read "cash-flow
matching, needs no rebalancing" next to a WInS book of coupon bonds and bond ETFs, and asked where the coupons get
reinvested. None of these needed new analysis. Each needed one check applied before an irreversible step.

## Top 10 (by likelihood x impact)

| Rank | ID | Failure | L | I |
|---|---|---|---|---|
| 1 | PM-23 | Coupon reinvestment risk unstated; "cash-flow matching" overclaimed | H | H |
| 2 | PM-12 | A note is silently cut by the 300-character box | M | H |
| 3 | PM-16 | Strategy name differs between permanent notes and the IPS | H | M |
| 4 | PM-24 | Streams quote different ladder costs for the same thing | H | M |
| 5 | PM-22 | IPS history claims ($460k in 2020, "since 2000", "cheapest since 2002") have no code behind them | H | M |
| 6 | PM-15 | A note mixes Laura-scale dollars with WInS-scale holdings | M | M-H |
| 7 | PM-01 | Wrong security bought (IBTN, or the wrong line in the bond drop-down) | M | H |
| 8 | PM-02 | Bond quantity entered in the wrong unit | M | H |
| 9 | PM-13 | An exemplar goes into WInS verbatim and is not cited | M | H |
| 10 | PM-10 | An undefined "required trading activity" rule is missed | L-M | H |

---

## A. Friday trades

| ID | What goes wrong (evidence) | L | I | Check later agents must apply |
|---|---|---|---|---|
| PM-01 | **Wrong security.** IBTN in WInS is INSCORP Inc, not an iBond. The WInS bond drop-down has 43 Treasuries, including matured ones and look-alike coupons (4.375% Feb-2038 is stale; 4.375% Nov-2039 is the one used). Longbridge returns no record at all for IBTN.US, so outside data cannot confirm WInS names. | M | H | Each ticket carries the exact WInS name string, plus coupon and maturity for bonds. At the Preview screen, one student reads ticker, name, quantity and total aloud and a second ticks them. Owner WS6; Gate C (name check against the WInS names in tab `WInS Notes`). |
| PM-02 | **Bond quantity unit.** The Trade Log header and Book L assume "face value $" (e.g. 30,000 = $30,000 face at 97.152). Nobody has seen WInS's Preview for a bond, so the unit (face $, $100 lots or $1,000 bonds) and the minimum lot are UNVERIFIED. A 10x or 1,000x error is possible. | M | H | The ticket shows the expected Preview total. Rule: if the WInS Preview total is more than 1% away from the ticket total, stop, do not submit. Put this first on the Friday checklist. Owner WS6. |
| PM-03 | **Cash goes negative or the last order is rejected.** At 28 Sep prices the Portfolio-tab units cost $294,569 including $200 commission, leaving $5,431 [1]. A parallel fall of about 28bp in yields (about 26bp if VT also rises 2%) uses up all the cash if the units are not re-sized [1]. The Portfolio tab's bond prices are dirty (clean plus accrued) but Book L's are clean, so accrued interest (about $1k on the five bonds) can be counted twice or not at all. Bond orders fill at end-of-day prices (WInS Portfolio FAQ, per tab `WInS Notes`), so cash is committed late. | L-M | M | The refresh script re-sizes units from Friday's WInS prices. It keeps running cash of at least $1,000 after every ticket, counting commission and accrued interest once. It orders ETFs first and bonds last, with bond sizes set from the cash actually left. Owner WS6; Gate C (cash never negative in sequence). |
| PM-04 | **A stale WInS bond price.** On 29 Sep two WInS prices were stale: 4.5% Feb-2036 at 102.95 and 4.375% Feb-2038 at 99.98, about 1pp off curve yields. Per the FAQ, bond prices update once a day at the U.S. open. | M | M | Friday: yield-check every bond price against that day's Treasury par curve, with a tolerance of 25bp; if one fails, use the named alternate. Owner WS1 (method), WS6 (Friday sheet). |
| PM-05 | **Volume rule, fills at the open, duplicate orders.** The Guide says an order must be at most 2x a security's daily volume. The WInS Portfolio FAQ says an order can take at most half of a security's market volume, and larger orders wait (tab `WInS Notes`). If "market volume" means volume so far that day, a thin iBond order placed before the open waits. Planned sizes are only 0.6-3.0% of 20-day median volume, but IBTM's 4,486 shares would be 19% of a partial session (29 Sep, first 45 minutes), and IBTR's median is only 33,500 shares [3]. A student who sees "pending" may re-enter the order and double the position. | M | M | Apply the stricter rule: keep each order at or below 10% of 20-day median volume. Place iBond orders after the first hour if possible. Never re-enter an order without first checking Order History. Owner WS6; Gate C (volume column). |
| PM-06 | **Poor fills in thin ETFs.** Order types (limit or market) are UNVERIFIED. Orders placed while the market is shut fill at the next open (FAQ), which is when spreads in IBTQ/IBTR are widest. | M | L | The ticket gives a reference price and a maximum acceptable price. The team records which order types WInS offers. If limit orders exist, use them. Owner WS6. |
| PM-07 | **Time-zone errors.** Sydney moves to AEDT on Sun 4 Oct and the U.S. moves to EST on Sun 1 Nov. Friday's open is 11:30pm Fri AEST. From 5 Oct the open is 12:30am AEDT the next day; from 2 Nov it is 1:30am AEDT. TN Analysis is due Sat 24 Oct 8:00am AEDT; the freeze is Sat 7 Nov 8:00am AEDT; the IPS is due Sat 7 Nov 9:00am AEDT (zoneinfo check, 30 Sep). | M | M | All times come from a time-zone library and are printed as both ET and Sydney time. No hand arithmetic. Owner WS6, WS8. |
| PM-08 | **Trying to fix a mistake the same day.** Day trading is not allowed (Session Rules). The FAQ says "run with it" and not to scramble to fix errors. | L | H | The checklist says: never sell a security on the day it was bought. Log any mistake, fix it only on a later day, and only if the strategy needs it, with a note that explains it. Owner WS6. |
| PM-09 | **Kit built for a book the team does not adopt.** The Portfolio tab says "Provisional until the team votes on 1 Oct 2026". D7 (Portfolio vs Book L) is open. | M | M | Tickets and the refresh script take the book as an input. Produce both books. Do not hard-code one. Owner WS6. |
| PM-10 | **Undefined activity rule.** The FAQ says teams "must meet the required trading activity and portfolio management guidelines" but does not define them. The Week-One email on the WInS dashboard was not read (tab `WInS Notes`). An 11-trade, one-day, buy-and-hold book could fall short of a minimum nobody has read. | L-M | H | Friday checklist item 1: read the Week-One email and the logged-in Trading Details page. If a minimum exists, meet it with the planned October trade, which must have its own strategy reason. Never add trades just to reach a count. Owner WS6, BRIEF. |
| PM-11 | **The kit calls unseen WInS facts "verified".** Order types, bond units, note editing and whether pending orders reserve cash have never been seen. | M | M | Tag every WInS fact SEEN (date and screen) or UNVERIFIED. The BRIEF's Friday list names every UNVERIFIED one. Owner WS8; Gate C. |

## B. Trading Notes and the TN Analysis

| ID | What goes wrong (evidence) | L | I | Check later agents must apply |
|---|---|---|---|---|
| PM-12 | **A note is cut.** The WInS note box has maxlength 300 (seen 29 Sep), so pasted text over 300 is cut without warning. Curly quotes, dashes, symbols such as "<=" or "~", and line breaks may count differently or be altered. The TN Analysis must quote each note "exactly as it appears in WInS" (TN guide). | M | H | Exemplars are at most 285 characters, counted as JavaScript string length, plain ASCII only, one paragraph. After saving, copy the note back from WInS into the Trade Log and diff it against the planned text. Owner WS6; Gate C. |
| PM-13 | **An exemplar is typed in verbatim and not cited.** Exemplars are authorised for this run and labelled `EXAMPLE - team rewrites`. Wharton's AI policy requires AI work to be cited, not passed off as the students' own. A note is permanent and is quoted in a scored deliverable. | M | H | Label every exemplar. Log it in `docs/AI_USE.md`. Ship a similarity check the team can run (flag 50% or more word overlap with any exemplar). The BRIEF says: if exemplar wording is used, the Final Report's Works Cited discloses it. Owner WS6, WS8. |
| PM-14 | **Overclaim words in a permanent note.** Examples: "guaranteed", "risk-free", "locked", "match/matched" (for ETFs), "repays $X" for IBTM (iShares: it "does not seek to return any predetermined amount", insight_v1 open_questions s3), "cash-flow matched" (see PM-23), and "I bond", which is a different U.S. savings bond. | M | M | Banned-word linter, reusing `trading_notes_pack.md` s6.2 plus the words above. On first mention, name iBonds by their full WInS name. Owner WS6; Gate C. |
| PM-15 | **Scale confusion.** WInS holds Laura's Jan-2028 plan scaled to $300k. The ladder is 65.9% of the book ($197.7k) and IBTM is $97,591, carrying the 2033 payment and the floor together (Portfolio tab). A note that says "$289k buys the ten payments" or "IBTM holds her $150k floor" next to those holdings contradicts the order it is attached to. | M | M-H | Every dollar figure in a note is tagged in `numbers.yaml` as either Laura's plan or WInS book. Notes use percentages, or say "in Laura's plan". The linter fails any untagged dollar figure. Owner WS6; Gate C. |
| PM-16 | **Strategy name drift.** The name is "Roots First" in exemplar v13-v14 (Drive) and team memory, "Root-and-Branch" in the IPS Google Doc and RUN_PLAN, and just "Roots" in Ray's doc comment. Notes typed Friday are permanent. The IPS is not frozen until 6 Nov. | H | M | Keep the brand name out of WInS notes unless Ray confirms the final name before Friday. Describe the idea in plain words ("the payments first, then growth"). Put this in the BRIEF as a decision to ratify. Owner WS6, WS8. |
| PM-17 | **Notes contradict the IPS.** The IPS says "needs no rebalancing", "latest payments first" and "scaled down". A rebalancing-style October trade, or a note claiming a date the ETF cannot promise, reads as inconsistent. Judges read the three deliverables together (Guide p4). | M | M | Each exemplar and the October-trade memo quotes the IPS sentence it carries out. WS7 runs a consistency table (note vs IPS). Owner WS6, WS7. |
| PM-18 | **A dated claim goes stale, or WInS gains or losses appear.** "Costs less than $300,000" is true at September yields but can be false by November. WInS P&L must never enter projections (Guide p4, FAQ). | M | L-M | A number in a note is either a design fact (ten $50k payments) or dated ("at 2 Oct prices"). No WInS return figures appear in notes or reflections. Owner WS6; Gate C. |
| PM-19 | **The three picks fail.** A pick points to an order that never filled, or has no saved note. Or all three show the same thing: the TN guide asks how decisions "aligned with, tested, or refined" the strategy. | M | M | Pick only Filled trades with saved notes, and keep two alternates. Cover different roles across the three. The October trade is the natural "tested/refined" candidate. Owner WS6. |
| PM-20 | **The superseded insight_v1 book leaks in.** insight_v1's tickets and note elements are built on IEF+TLH, book "(ii)R", the "9.90" duration match, VGSH and "building minimum" labels. 74.7% of TLH matures after 2042. | M | M | Grep all kit outputs for `IEF|TLH|VGSH|(ii)R|duration match|9.90`. Any hit in a ticket or exemplar fails. Owner WS6; Gate C. |
| PM-21 | **Laura facts misused.** The case pull quote cannot be verified as hers (insight_v1 D13a). Her statistics degree was ruled "zero uses" (insight_v1 open_questions, team decision D8). | L | M | No Laura quotes in notes. Only case facts, cited to the case page. Owner WS6. |

## C. Claims a judge will test

| ID | What goes wrong (evidence) | L | I | Check later agents must apply |
|---|---|---|---|---|
| PM-22 | **History claims with no code.** The IPS doc says the payments "would have cost about $460,000" at 2020 yields, and "We tested this on every Treasury curve since 2000". The run brief adds "cheapest since 2002". No committed script or output for any of these was found in either checkout (grep, 30 Sep). D1 [4] is consistent in direction only: on the 28 Sep curve shape, the ladder exceeds the whole 2028 deposit only after a 428bp parallel fall (10-year 0.89%). | H | M | WS1/WS3 reproduce each claim from treasury.gov or FRED history with code, the curve date and the method. Until then they are UNVERIFIED in every output. If one cannot be reproduced, classify it fix-before-6-Nov (IPS wording). Owner WS1, WS3. |
| PM-23 | **Coupon reinvestment risk is unstated.** The ladder is priced as zero-coupon bonds ($289k), but the instruments available in WInS are coupon Treasuries and iBond ETFs that pay monthly income. Under the safe reading of the FAQ, the real plan may use only WInS-listed instruments; STRIPS are not seen on the WInS list (UNVERIFIED). WS0 rough check on Book L [2]: the ten holdings deliver about $505k if coupons are reinvested at today's yields, about $483k if reinvestment rates are 2pp lower, about $470k at 2% and about $453k at 0%, against $500k owed. (Assumptions: iBonds modelled as 4% bullets, flat rates.) insight_v1's "~$5k" (fact_register F-113) counted coupons only up to 2033. The IPS says "This cash-flow matching, unlike immunization, needs no rebalancing" and "once bought it depends essentially on the US government". | H | H | M1 must build a real cash-flow schedule for the implementable ladder and report its cost under stressed reinvestment (0%, 2%, today's yield minus 2pp), plus the extra cost of making it robust. Classify: **fix-before-6-Nov** (IPS wording, the team decides) and note-in-Final-Report (the numbers). Do not change the strategy. Owner WS1, WS7. |
| PM-24 | **Number basis mixing.** Several different ladder figures exist: $289,003 / $289,119 (bought today, zero-coupon model), $292,214 / $292,418 (forward to 1 Jan 2027, 15 Nov maturities), $290,291 (exact-date forward), $292,226 (Book L at WInS prices), $294,387 (25 Sep curve). Streams will pick different ones. | H | M | Each `numbers.yaml` entry carries value, curve date, valuation date, maturity convention, instrument basis, source and a single "quote as" string (e.g. "about $290k"). Gate C greps every output for dollar figures that are not in the yaml. Owner WS1; Gate C. |
| PM-25 | **Confidence stated wrongly.** By construction, the 2033 gift cannot leave the range if three things hold: the floor holdings pay, the 2028 deposit arrives, and the gift is capped. A model percentile misreads that, and a bare "100%" hides the conditions. The floor sits in IBTM (no WInS Treasury matures Feb 2031-Feb 2036), and IBTM's final payout is not predetermined. | M | M | WS2 states "certain by construction if..." with the conditions listed. It adds the chance of landing in the top or bottom half of the range. It suggests announcing the floor rounded down. Owner WS2. |
| PM-26 | **The kit quietly redesigns the strategy.** The D6 optimiser prefers a share other than half, a rival beats the plan on one metric, or a different floor looks better. | M | H | Every memo carries a triage label (fix-before-6-Nov / note-in-Final-Report / ignore). The BRIEF lists these as "decisions to ratify". Nothing is applied to the IPS or the Sheet. Owner all; Gate D. |
| PM-27 | **False precision.** Percentiles given to the dollar, thin-tail lognormal outputs quoted as odds, a Sobol analysis on a handful of inputs. Judges reward simple ideas; the 831-page record is the counter-example. | M | L-M | Round to $1k (ranges to $5k). Label model outputs MODEL. At most one number per note. BRIEF of one page or less. Owner WS2-WS4, WS8. |
| PM-28 | **Treasury credit overstated.** Notes call Treasuries "risk-free" although the U.S. is below AAA at all three agencies (Moody's Aa1, May 2025: insight_v1 SNIP, not re-checked). | L | M | Wording: "backed by the U.S. government". Mention the default risk once in the Final Report. Owner WS6, WS7. |

## D. Numbers and models

| ID | What goes wrong (evidence) | L | I | Check later agents must apply |
|---|---|---|---|---|
| PM-29 | **Data-handling errors.** yfinance's default `auto_adjust` gives dividend-adjusted closes, which sit below the traded price for bond ETFs that pay monthly. Other traps: par yields mixed with zero yields; day count (the $116 D1-vs-GPT gap is 365.25 vs 365); an old curve file (`official_curve_pv.py` is fixed to 25 Sep). | M | M | Use `auto_adjust=False`. Ticket prices come only from WInS or a last-trade quote with a timestamp. Every model prints its curve date and conventions. Owner WS1. |
| PM-30 | **The blind check is not blind.** Both builders read insight_v1's code or `numbers.yaml`, so they share the same mistake (seed 8). | M | M | The second builder gets only the spec and the raw inputs, and logs every file it read. A disagreement is explained, not averaged. Owner WS0 (Gate B). |
| PM-31 | **Stale repo facts leak in.** $100k and $0 commission (`config/competition.yaml`), "Dec 4" trading, $500k/$100k, "no Treasuries on WInS", $5 vs $3 minimum price, the old "17%" position-limit branches. | M | M | Audit grep before every gate. The source-of-truth order in RUN_PLAN s0 wins. Owner WS7; Gate C. |
| PM-32 | **The rate-risk numbers disagree.** The model chance the ladder costs more than $300k on 1 Jan 2027 is 24.2% on the 28 Sep curve (D1 [6], zero-drift lognormal). Older text says "about 1 in 3". Both could appear. | M | M | WS4 reconciles and gives one number with its date and method. Retire the other. Owner WS4. |
| PM-33 | **Fake or unresolvable references**, or any citation in the IPS (not allowed there). | M | M | WS5 resolves every DOI or URL. References go only in the Final Report. Owner WS5. |

## E. The run itself

| ID | What goes wrong (evidence) | L | I | Check later agents must apply |
|---|---|---|---|---|
| PM-34 | **A forbidden external write.** Existing Sheet tabs overwritten, the IPS doc edited, a push, a message sent. The Sheets and Drive connectors returned 503 errors several times during this task, which invites "retry with a write". | L | H | Write only to new `RAB ` tabs, or to CSV in `rab/sheets/` (the default while connectors fail). Never update an existing range. Never push. Owner all. |
| PM-35 | **`numbers.yaml` drifts after lock.** Several streams edit it, or merges overwrite it. | M | M | WS1 is the only writer. The hash is re-checked at Gates C and D. Changes after lock go through WS0 with a changelog line. Owner WS1, WS0. |
| PM-36 | **Rebuilding instead of reusing; usage or crash stops the run** (seeds 2, 10, 12). | M | M | `rab/inventory.md` is read first. P0 streams (WS1, WS6) run first. Every stream commits often and logs progress in STATUS.md. Owner WS0. |
| PM-37 | **Output flood** (seed 7). | M | M | BRIEF at most 1 page. Paper at most 20 pages. Everything else goes in appendices. Owner WS8. |
| PM-38 | **Privacy or public exposure.** The public repo, student surnames or emails, kit exemplars published. | L | M | Local branches only. No personal data in commits. The Artifact stays private. Owner all. |

---

## Automated checks for Gate C (spec for WS6/WS8)

1. **Note length:** JavaScript-style length of 285 or less; ASCII only; no line breaks (PM-12).
2. **Banned words:** the s6.2 list plus guaranteed, risk-free, locked, matched, "repays $", "cash-flow match", "I bond", CAPE, forecast (PM-14, PM-23).
3. **Traceability:** every number in a note, ticket or memo is found in `numbers.yaml` (value plus scale tag) or has a cited URL and date (PM-15, PM-24).
4. **Superseded book:** no `IEF|TLH|VGSH|(ii)R|duration match` in tickets or exemplars (PM-20).
5. **Stale facts:** no `100,000|\$100k|Dec 4|500k|no Treasuries|\$0 commission` (PM-31).
6. **Names:** each ticket's WInS name matches tab `WInS Notes`; IBTN never appears as a buy (PM-01).
7. **Cash walk:** running cash of $1,000 or more after every ticket, with commission ($25 per ETF, $10 per bond) and accrued interest counted once (PM-03).
8. **Volume:** each order at or below 10% of 20-day median volume, else a split plan (PM-05).
9. **Bond sanity:** each bond's price implies a yield within 25bp of that day's curve; the Preview total is printed for the 1% stop rule (PM-02, PM-04).
10. **Status tags:** every WInS fact is SEEN (date) or UNVERIFIED (PM-11).
11. **Exemplar overlap:** a tool the team can run to compare its rewritten note with each exemplar (PM-13).
