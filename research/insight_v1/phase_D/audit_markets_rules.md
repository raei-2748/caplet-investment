# AX2 audit: equity (D2), Taiwan/FX (D4) and compliance (D10)

Agent AX2 (cluster auditor), insight_v1 run, 2026-09-28. This is an adversarial check of three specialist files before
they reach the strategy team. It is AI-generated research: findings, numbers and checklists, not text to submit.
The team decides and writes every word. Status labels follow brief section 3.

**What this task delivers**
- This file.
- An "## Audit corrections (AX2)" section appended to the end of each of the three specialist files. Their own text is
  unchanged.
- One check script, `research/insight_v1/scripts/AX2_audit_checks.py`, which reproduces every number AX2 added.
- The corrections list and verdict returned to the run.

Nothing was committed.

Files audited:
- `research/insight_v1/phase_D/D2_equity_ai.md` (M030, sleeve equity weight)
- `research/insight_v1/phase_D/D4_taiwan_fx.md` (M095, FX and building costs)
- `research/insight_v1/phase_D/D10_compliance.md` (M005 WInS book, M013 IPS governance)

---

## Verdict (short)

All three files **pass with corrections**. Every script reproduces. Every web source I re-opened says what the
specialists quote. None of the problems is a fabricated fact. They are overclaims, one inconsistent yardstick, one
misapplied rule, scope drift, and one gap that could break the Trading Notes deliverable.

| File | Verdict | What changes |
|---|---|---|
| D2 | Pass with corrections (0 blocking, 8 important, 6 minor) | The 50/50 option survives as a team choice. The evidence line "three sources agree the premium is about 0" is withdrawn: across sources it is about -1.2 to +2.4 points a year, still small and uncertain. The "known/locked 5.2%" wording is withdrawn. "Decide once or break the Guide" is a preference, not a rule. |
| D4 | Pass with corrections (0 blocking, 3 important, 8 minor) | Numbers are sound. Most of the file is Final Report material and is parked. Three IPS rules go forward (US$ binding; no NT$ conversion or hedge before the facility decision; building-cost drift named as an assumption). The "2031 ranking" holds only if at least ~70% of the growth money is locked in 2031. |
| D10 | Pass with corrections (1 blocking, 2 important, 10 minor) | The M005 and M013 answers stand. The lean to option (iii) is **not decision-ready**: with no cap, (iii) gives only two trades, and three executed trades are needed for the Oct 23 notes. The page-fit numbers are optimistic; the IPS layout is tighter than D10 says. |

---

## 1. Scripts re-run (2026-09-28)

| Script | Result |
|---|---|
| `D2_equity_premium.py` | Reproduces exactly: hurdles 5.14/5.20/5.23/5.10%; all premiums; all percentile tables; crash stress; equity shares 13.7/17.1/20.5%; VT $51,000 ~318 sh / VGSH $48,000 ~833 sh. One text error: the 40%-vs-60% median has the wrong sign for one case (D2 C9). |
| `D4_facility_purchasing_power.py` (live FRED and DGBAS) | Reproduces exactly. DEXTAUS latest 31.82 (2026-09-18). CCI latest 119.51. Every sd, share, drift, correlation, band and hedge figure matches. |
| `D10_wins_book_compliance.py` | Reproduces, except that the worst volume use is 0.17%, not 0.19% (D10 C5). |
| `D10_ips_page_fit.py` | Every table row reproduces. The A4 range is 89.5-101.0%, not 89-99% (D10 C6). The model itself is optimistic (D10 C3). |
| `AX2_audit_checks.py` (new) | (1) 2031-view market spread by floor share. (2) D2 yardsticks like-for-like. (3) D2 sleeve vs a Treasury-only comparator. (4) Page fit with whole lines and a 27.6pt line. |
| `D9_ips_page_fit.py` (cross-check only) | At Word's 27.6pt double line: 0-2 spare lines on Letter (about 525 IPS words at most). At Wharton's own 24pt sample line: 8-10 spare. This agrees with AX2's re-run of the D10 model. |

## 2. Sources re-opened (the most decision-relevant claims)

Read with `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL --grep "..."` on 2026-09-28, unless the row
says it is a repo file.

| # | Claim (file) | Source | Result | Status |
|---|---|---|---|---|
| 1 | Vanguard U.S. equities 4.9%-6.9% -> 4.2%-6.2%; dev ex-U.S. 4.5%-6.5%; EM 2%-4%; July 22, 2026; June 30, 2026 run; geometric (D2 E4) | https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html | All verbatim | VERIFIED-PRIMARY |
| 2 | "valuations tend to be poor predictors ... should not serve as a primary reason for changing portfolio allocations" (D2 E5) | same | Verbatim | VERIFIED-PRIMARY |
| 3 | Forward P/E 19.2; 5-yr 19.8; 10-yr 19.0; 20.4 on June 30; +2.7% price, +8.9% EPS; trailing 25.8 (D2 E7) | FactSet Earnings Insight 25 Sep 2026 PDF (URL in D2) | All present | VERIFIED-PRIMARY |
| 4 | CY2026 +32.0%, CY2027 +15.4%, Q2 2027 +1.7%, IT +63.5%, semis +126%, IT ex-semis +24.2% (D2 E8) | same | Present, but these are **analyst projections and estimates**, not outcomes | VERIFIED-PRIMARY (as projections) |
| 5 | 10y 4.44% on 2026-06-30; 4.16% on 2025-09-30; 5.18% on 2026-09-24; Feb 27 low 3.97%; breakeven 2.34% (D2 E6, D10 F-003) | FRED DGS10, T10YIE CSV | All match | VERIFIED-PRIMARY |
| 6 | CAPE 41.48; mean 17.42; max 44.19 Dec 1999 (D2 E9) | https://www.multpl.com/shiller-pe | Matches | SNIPPET-UNVERIFIED (secondary read directly) |
| 7 | JPM AC World 7.00/8.28/16.78; correlation with intermediate Treasuries 0.00 (D2 E3) | `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` p.2 | Matches | VERIFIED-REPO-FILE |
| 8 | "willing to take thoughtful risks" / "appropriate balance" (D2 E13) | Case L69-74 | Verbatim | VERIFIED-REPO-FILE |
| 9 | Guide p.5 "should not be rewritten simply because markets move" (D2 E14, D10 G7) | Guide L156-159 | Verbatim, but it sits in the **post-IPS evaluation stage**. Guide L89-90 and TN guide L18-19 say the strategy "may continue to evolve" before the IPS | VERIFIED-REPO-FILE (D2 misapplies it) |
| 10 | Case asks for "the effect of inflation on portfolio projections and facility costs"; cost not to be estimated; "dollar range"; Taiwan legal out of scope (D4 E1-E4) | Case L146-148, L164, L117, L169 | Verbatim | VERIFIED-REPO-FILE |
| 11 | "$150,000 ... will not be added to WInS"; no sector minimum; "funding purposes"; "does not require frequent or same-day trading"; 2x volume; 200 trades (D10 E2, E3) | https://wghsinvcomp.smapply.us/res/p/trading/ | All verbatim | VERIFIED-PRIMARY |
| 12 | "Advisors may not make decisions on behalf of students ..." (D10 G1) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ | Verbatim | VERIFIED-PRIMARY |
| 13 | CFA IPS elements: 2a; "no less frequently than annually"; 4c no-rebalance policy "should be documented in the IPS"; "objective course of action" (D10 G9) | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf | All verbatim | VERIFIED-PRIMARY |
| 14 | AI use "must be recorded in your Works Cited pages" (D10 s.3) | https://globalyouth.wharton.upenn.edu/ai-policy/ | Verbatim | VERIFIED-PRIMARY |
| 15 | IPS format: 2-page maximum; TNR 12; double-spaced; 1-inch margins; non-compliance "will not be considered for semifinal selection"; formatting not specified "left to the team's discretion" (D10 G10) | IPS guide L82-123 (L101 for discretion) | Verbatim | VERIFIED-REPO-FILE |
| 16 | Three notes "from trades your team executed in WInS" / "Yes, we will verify this" | TN guide L42, L53 | Verbatim | VERIFIED-REPO-FILE |
| 17 | "Investments permitted (for BOTH contributions)" (R-AN15; used by AX2 against D4's NT$ forward) | https://wghsinvcomp.smapply.us/res/p/faqs/ (line 42 of the text) | Present | VERIFIED-PRIMARY |
| 18 | USD/TWD 31.82; CCI 119.51; S&P monthly correlation -0.38 (D4) | Live FRED DEXTAUS/SP500 and DGBAS CCI through the D4 script | Match | VERIFIED-PRIMARY inputs, derived |

Not re-opened, and still labelled as the specialists had them:
- Taiwan 2-year yield 1.66% (SNIPPET-UNVERIFIED; the page is script-rendered).
- Wikipedia dates for the 1995-96 crisis (secondary).
- The CFA Asset Manager Code quotes (via SH-25/D8).
- The 2021-23 case wording for the "portfolio manager" line (via B1a).
- The Stock-Trak blog and FAQ (via A4).

## 3. The corrections that matter most (full lists are appended to each file)

**Blocking**
1. **D10 C1: under option (iii), nothing guarantees a third executed trade before Oct 23.** With no cap there are two
   orders. The duration refresh and a position-limit response happen only if a band or cap is hit. The fix is to name
   a genuine third trade in advance. The plan's own rule gives one: the 2027 leftover "waits in T-bills", so buying
   BIL or SGOV for about 2% of the portfolio is a liquidity-role trade (PENDING WInS AVAILABILITY + POSITION-LIMIT
   CHECK). The alternative is option (ii).

**Important**
2. **D2 C1: "the hurdle is known" / "can lock about 5.2%" is wrong as worded.** The 5.2% is implied by today's curve
   for money that arrives in 2028. It cannot be locked now: there is no money yet, and forwards are derivatives, which
   are banned. Call it a market-implied hurdle.
3. **D2 C2: the forward earnings-yield yardstick compares a real yield with a nominal rate.** D2 adds inflation to its
   CAPE yardstick but not to this one. Like-for-like it gives about +2.3 points, not about 0. Across sources the premium
   is about -1.2 to +2.4 points a year: still small and uncertain, but no longer "about 0".
4. **D2 C3: Guide p.5 does not forbid changing the split before Nov 6.** The official texts expect the strategy to
   evolve until the IPS. A research-based change could even be a strong note, and the ticket already says so.
5. **D2 C5 and C6 would matter in permanent notes.** First, "VT halves AI exposure" overstates: top-10 concentration
   falls about 44%, and VT holds Asian AI chip makers outside its top ten. Second, "half in short Treasuries for the
   amount Laura may promise" conflicts with the plan's 2031 rule, which buys the floor from a share of the whole sleeve.
6. **D2 C8 contradicts the ticket on the sleeve-bond return.** D2 uses 4.8% (market-consistent) and the ticket asks
   for 3.5-3.9%. The main loop must pick one; AX2 favours the market-based figure.
7. **D4 C1 (scope).** Implications 1-5 and the chart spec are Final Report material (brief section 17). Three IPS
   rules survive.
8. **D4 C2.** "By 2031 the market is the smallest factor" is true only if about 70% or more of the growth money is
   locked in 2031. That share is an open team parameter.
9. **D4 C3.** An NT$ forward is a derivative, banned in WInS and (safe reading of R-AN15) in the plan. This is the
   first reason not to lock NT$; the 5.9% cost is the second. The "23% of windows" figure is a counterfactual.
10. **D10 C2.** The claim that both books pass "whatever the position limit" was tested only for no cap, 35% and 25%.
    Vanguard volumes are unchecked.
11. **D10 C3.** The page fit is tighter than stated. With whole lines and Word's likely 27.6pt line, 550 words fill
    about 98-100% of two Letter pages even with 0pt spacing. D9 agrees. Test the real PDF early; the word target may
    need to be below 480.

## 4. Contradictions found

| Between | Contradiction | Resolution (AX2 recommendation; the team decides) |
|---|---|---|
| D2 vs WInS ticket | Sleeve equity 50/50 (D2) vs 60/40 provisional (ticket) | A proposed change, not an error. Put it to the team as a choice of spread: median about equal, p5 +$6-7.5k, p95 -$11-14k at 50/50. |
| D2 vs WInS ticket | "Changing the split later contradicts the Guide" (D2) vs "a change of the split after the team's research" as a genuine note (ticket section 4) | The ticket is right (Guide L89-90; TN guide L18-19). |
| D2 vs WInS ticket | Sleeve-bond model return 4.8% (D2) vs "about 3.5-3.9%" (ticket section 8) | Use a market-consistent figure (VGSH SEC yield 4.55%, forwards 4.8-5.1%) with an ASSUMPTION label. The main loop updates the ticket line. |
| D2 vs D10 | D2's tier-1 action (set the split before VT/VGSH orders) vs D10's lean to (iii) (no VT/VGSH orders) | The split is tier 1 only if (ii) is chosen; otherwise it is an IPS rule. |
| D10 vs WInS ticket | D10 leans (iii); the ticket (S3) leans (ii) | Both are compliant; this is a team vote (gate box b). The vote should see: (iii) is shorter to explain in the IPS but needs a named third trade (D10 C1) and shows no growth role in WInS. (ii) shows three roles but needs the three-element scaling sentence. |
| D10 numbers vs D2 | D10's +20.5-point equity gap and 20.4% real equity assume 60/40 | At 50/50: +17.0 points and 17.0% (F-409). |
| D10 vs D9 | Page fit 92-105% (D10) vs "fits, spare 0-2 lines at 27.6pt; 8-10 at 24pt" (D9) | Same message once whole lines and 27.6pt are used: tight with Word defaults. Use one merged checklist, with D9's `--draft` tool on the team's own text. |
| D4 vs brief section 17 | D4 routes almost everything to the Final Report, including a chart spec | Park it as "later (after Nov 9)"; three IPS rules go forward (D4 C1). |
| D4 vs brief section 14 | None found. D4 uses CPI 2.04%, CCI 3.54%/yr since 2021 and the "3.2x is a one-year spike" reading. | No action needed. |
| D2/D10 vs brief section 16 | D10 quotes 24% only for the ladder costing more than $300k | Quote about 24-31% ("roughly 1 in 4 to 1 in 3"). |

## 5. Overclaims, jargon, privacy, tokenism and prose check

- **Overclaim words.** "Known" and "lock" for 2028 rates (D2); "halves" (D2); "free improvement" (D2 as routed);
  "certain to erode" (D4); "most likely way to lose" and "whatever the position limit" (D10); "cost the whole scenario
  analysis its legitimacy" (D10). All are corrected in the appended sections. No file calls the WInS funds a "match"
  for the payments: D10 correctly says "stand-in funds that move like her payments". D10 C12 adds that "cash-flow
  matched" applies to the real STRIPS ladder only.
- **False precision.** D4's variance shares (8/53/39%) and D10's page-use percentages rest on small samples or a
  layout model. Both are labelled, but they should be read as rough rankings. D4's "51% of windows" is a coin flip, not
  a finding.
- **Jargon.** D4: covered interest parity, log sd, variance share, bootstrapped. D2: SEC yield, i.i.d., lognormal.
  Define them or cut them.
- **Labels.** "SECONDARY-READ" (D2), "DERIVED" (D4) and "INTERPRETATION" (D10) are not brief labels. Map them to
  SNIPPET-UNVERIFIED or ASSUMPTION. INTERPRETATION is acceptable if it is defined in the file, as D10 does.
- **Privacy.** No problems. Only her public professional record is used; there is no personal data and no student
  surnames.
- **Tokenism.** D4 correctly keeps Taiwan as a case fact (where the building is), not an identity theme. D10 uses a
  student-era Laura quote ("earliest supporters", 2016) to argue for a WInS book. Label it and do not use it that way
  (D10 C10).
- **Submission-ready prose.** One quotable sentence in D10 section 1.3 (C9). D2's note elements are close to prose
  but acceptable as a checklist. Neither file drafts a note, a reflection or IPS text.

## 6. What survives and where it goes

Only Trading Notes (TN) and IPS items go forward (brief section 17).

- **WInS / TN (tier 1)**
  - Vote (ii) or (iii) first. If (iii), name the third trade: the T-bill leftover.
  - If (ii), choose the split before the VT and VGSH orders if the team can. A later, research-based change is
    allowed and can be a note.
  - Note wording must avoid: "known/locked" rates; "halves AI exposure"; "half = the promise"; "match". Use: "stand-in
    funds"; "the market-implied Treasury rate for her dates"; "a fall shrinks the facility range, never the payments".
- **IPS (tier 2): rules to fix before Nov 6**
  - Sleeve split, with its reason based on the 2031 promise and the flat median, not on "this year's premium".
  - One sentence naming the date WInS represents.
  - Governance in about 30-45 words (D10 keep/cut table, verified).
  - No rebalancing between promise money and growth money, stated in words (CFA 4c).
  - US$ is the binding currency.
  - No NT$ conversion or hedge before the facility decision.
  - Building-cost drift named as an assumption.
  - Format: space-after 0; test the PDF on the first draft; set the word target from the real PDF.
- **Later (after Nov 9), one line each:** D4 implications 1-5 (assumption line, co-sponsor currency sentence,
  uncertainty sentence, flexibility sentence, chart); D2's two-house projection table.

## What this teaches

1. **Re-running the numbers is not the same as checking the argument.** Every script here reproduced to the decimal.
   The real errors were in the words around the numbers: a rate called "known" that is only implied, a yield compared
   with the wrong kind of rate, and a rule quoted from the wrong stage of the competition.
2. **Compare like with like.** An earnings yield is roughly a return after inflation. A Treasury yield is before
   inflation. Put them on the same basis before subtracting one from the other; here that moved the answer by more
   than 2 points.
3. **Read the sentence around the quote.** "Should not be rewritten simply because markets move" is real Wharton
   wording, but it applies after the IPS is submitted. Two pages earlier the same guide says the strategy may still
   evolve. Where a quote sits decides what it permits.
4. **Ask what a conclusion depends on.** "By 2031 the market is the smallest risk" is true because the plan locks 80%
   of the growth money. Change that open choice and the ranking changes too. A finding is only as robust as its
   least-settled input.
5. **Check deliverables, not just rules.** A WInS book can obey every trading rule and still leave the team one
   executed trade short of the three notes due on Oct 23. Compliance means being able to submit what is required.
