# AY1 audit: co-sponsors (D5), client psychology (D6) and client-side overflow (D12)

Agent AY1 (cluster auditor), insight_v1 run, 2026-09-28. This is an adversarial check of three specialist files before
they reach the strategy team. It is AI-generated research: findings, numbers and checklists, not text to submit. The
team decides and writes every word. Status labels follow brief section 3 (VERIFIED-PRIMARY = VP, VERIFIED-REPO-FILE =
VRF, SNIPPET-UNVERIFIED, ASSUMPTION = ASM, INT = interpretation).

**What this task delivers**
- This file.
- An "## Audit corrections (AY1)" section appended to the end of each of the three specialist files. Their own text is
  unchanged; where it conflicts with the corrections, the corrections win.
- One check script, `research/insight_v1/scripts/AY1_audit_checks.py` (about 5 seconds; it re-uses the D5 and D6
  engines and random streams, so every difference is in what is computed, not in the simulation).
- The corrections list and verdict returned to the run. Nothing was committed.

Files audited:
- `research/insight_v1/phase_D/D5_cosponsors.md` (M003, M091, M107, M094: 2031 range, flexibility, co-funders)
- `research/insight_v1/phase_D/D6_behavioural.md` (M125, M018, M019, M228, M237, M197: risk profile, bad years, stock
  share rule, range width)
- `research/insight_v1/phase_D/D12_overflow_client.md` (M247, M231, M234: note roles and length, evidence grades,
  reader test)

Scope applied (brief s17): only what serves the Trading Notes (TN, Oct 23) or the IPS (Nov 6). D5 and most of D6 were
written before s17 (2026-09-28), so their Final Report parts are routed to the "later" list below, not audited in depth.

---

## Verdict (short)

All three files **pass with corrections**. Every script reproduces. Every web source I re-opened says what the
specialists quote (one link built on a source is withdrawn: D5's Kresge "backstopped" claim). No fabricated facts, no
privacy or tokenism problem, and no submission-ready prose. The problems are one arithmetic slip, one misused source
word, one rule claim that holds only on a coarse grid, two note-wording issues that matter because notes are permanent,
and scope drift.

| File | Verdict | What changes |
|---|---|---|
| D5 | Pass with corrections (0 blocking, 4 important, 7 minor) | The key finding stands: promising the upside and keeping flexibility conflict unless a rule splits the post-2031 growth (give-back share s). The rule method goes to the IPS; the numbers, NT$ figures and the excerpt checklist go to the later list. "Guarantee" becomes "bought, not forecast, barring U.S. default". Kresge's "backstopped" link is withdrawn. 98% becomes 94%. |
| D6 | Pass with corrections (0 blocking, 6 important, 5 minor) | The per-goal risk profile (CFA framework) is the best IPS input in the cluster and stands. The stock-share rule gives about **55-70%** depending on inputs, not "60%, robust to fat tails". The hedge-note row loses "sized to ~$292k" (under option ii) and "stops depending on markets". Her career-regret line is context, not the reason for stocks. The pitch spec must allow for the ladder finishing from the 2028 deposit and must name the nominal-US$ limit. |
| D12 | Pass with corrections (0 blocking, 4 important, 6 minor) | The note-element spec is re-based on the Guide's own list (it had dropped "supporting research or analysis"). The 300-character cap is a precaution with mixed evidence; check it at zero risk before the first note. Option (iii) gives two trades, not three, without a cap. The IPS rule list gains the nominal-US$ item. |

---

## 1. Scripts re-run (2026-09-28)

| Script | Result |
|---|---|
| `D5_range_and_flexibility.py` | Reproduces exactly (floor $127k/$165k/$217k and surplus $159k/$207k/$273k reconcile with F-401/F-402; every (a, s) row; $118k-$147k / $178k-$223k; 50% / 10%; P(above top) 15%; excess $2k/$8k; NT$4.59m; 7.2/11.0/14.9%). One text slip: "$168k-$184k in 98% (p1-p95)" is 94% (D5 C4). |
| `D6_behavioural_numbers.py` | Reproduces exactly (design tables A/B/C; every rule pick on its 10-point grid; bad-year figures 27/62/14/10/50%, -$3k/-$21k/-$9k; growth-first 40% / 5.4%; M197 ratios; word counts, re-checked by grep on the case). |
| `D12_note_roles.py`, `D12_evidence_grades.py`, `D12_reader_test.py` | Reproduce exactly; the binomial detection figures were also recomputed by hand. |
| `AY1_audit_checks.py` (new) | [1] D5 conditional gift percentiles; [2] range width as a function of lock share a AND give-back share s; [3] D6 rule on a 5-point grid (cases A, B, C; fat tails); [3b] same with a 0.5% / 1.0% yearly fee (ASM); [4] floor vs the 2031 two-year rate; [5] WInS hedge dollars vs the $292k ladder. |

Key new numbers (AY1 script; all model properties under the specialists' labelled ASSUMPTIONS):
- D6's rule ("most stock with P(2033 growth money < money put in, $157.7k) <= 5%") on a 5-point grid: JPM + 4% bonds
  **60%**; JPM + 5% bonds (D6's own case B) **65%**; Vanguard midpoint **55%**; fat tails **65% / 70%** (A / B); JPM
  with a 0.5% fee **55-60%**, with 1.0% **50-55%**.
- Range width top/bottom (p90 top): (a 0.7, s 0.5) **1.26x**; (0.8, 1.0) **1.30x**; (0.7, 1.0) **1.52x**; (0.6, 0.5)
  1.40x. Width ≈ 1 + s(1 - a)/a x 1.21.
- D5 gift given the median 2031 state: p1/p5/p50/p95/p99 = $167.8k / $169.8k / $175.8k / $183.7k / $187.6k; below the
  range midpoint in 0.00% of paths (the unlocked money would have to lose ~36% in two years).
- Floor vs the 2031 two-year rate: -3.4% at 3.0%, +2.3% at 6.0% (vs 4.81%).
- Option (ii) WInS hedge $198,000 = 68% of the $292,264 ladder (the ladder is 64.9% of both deposits, scaled).

## 2. Sources re-opened (the most decision-relevant claims)

Read with `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL --grep "..."` on 2026-09-28 unless marked.

| # | Claim (file) | Source | Result | Status |
|---|---|---|---|---|
| 1 | "we allow up to 300 characters" (D12) | https://www.howthemarketworks.com/updates/trade-notes-justify-trades/ | Verbatim. It is a sister product | VP for that product; UNVERIFIED for WInS |
| 2 | "Enter a Trade Note (these are important!) to discuss how the purchase fits into your overall strategy" (D12) | https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf | Present (PDF text reads "T rade"); PDF **page 10**, not p.8; no character limit anywhere in the guide. Also: "Position Limit: This is how much of your portfolio you can invest in one single stock." | VP |
| 3 | Notes cannot be edited or deleted; more notes can be added, each timestamped (D12) | https://www.stocktrak.com/new-feature-trade-notes/ | Verbatim; also "Required" notes option; no length limit | VP (vendor, 2017) |
| 4 | No note limit on Stock-Trak's FAQ | https://www.stocktrak.com/faq/what-are-trading-notes/ | No limit stated | VP (absence) |
| 5 | "Conduct between 6 to 9 interviews"; "Do not correct the participant"; "service-connected disability"; "all said that it was clear" (D12) | https://digital.gov/guides/plain-language/test/paraphrase-testing | All verbatim | VP |
| 6 | L = "31%"; "3-4 users from each category if testing two groups" (D12) | https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ | Verbatim | VP |
| 7 | "The [unfinished] results are below."; "Match Quality"; 6 Good / 5 Unsure / 3 Bad (D12) | https://lauragao.com/rewriting-herstory | Verbatim; recount matches | VP (public professional page; student-era, ASM) |
| 8 | Kresge: "Written pledges or cash ..."; "committed, imminent or backstopped" (D5) | https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf | Verbatim, but the "backstopped" sentence covers only financing, government funds, organizational funds and bequests; glossary defines backstopping as the grantee's own alternative resources | VP; D5's "describes Laura's floor exactly" withdrawn |
| 9 | "barriers to entitlement are overcome"; "did not receive a promise to give" (D5) | https://storage.fasb.org/ASU%202018-08.pdf | Verbatim | VP |
| 10 | "A challenge gift is an unconditional commitment by a donor ..." (D5) | https://www.nber.org/system/files/working_papers/w13728/w13728.pdf (+ abstract page) | Verbatim | VP |
| 11 | Brunel: family "wants to reserve 10 percent of their total wealth"; Das 2018 Table 1 Wants 80-85 / Needs 90-95 (D5) | squarespace-hosted Brunel PDF (URL in D5); https://srdas.github.io/Papers/GBWM.pdf | Verbatim / table present | VP |
| 12 | CFA 2020 reconciliation rules; "upper volatility bound"; risk composure measured from past actions (D6) | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/survey/investment-risk-profiling.pdf | All verbatim | VP |
| 13 | "highly domain-specific" (D6) | Princeton research portal (URL in D6) | Verbatim | VP (abstract) |
| 14 | Calibration drives credibility; "as precise as warranted"; "only a small decrease in trust" (D6) | Tenney et al. 2008 author PDF; RePEc Du et al.; RUG portal van der Bles et al. | Verbatim (Tenney's 2nd sentence has a PDF ligature) | VP; applicability to co-sponsors INT |
| 15 | House-money / break-even; myopic loss aversion; Morningstar 7.0% vs 8.2%, "nearly 97%"; FAJ "0.10% per year" (D6) | EconPapers; NBER w4369; Morningstar PDF; CFA FAJ page | All verbatim | VP |
| 16 | Old criterion "would win him/her over as a client" (D6 via B2b) | globalyouth.wharton.upenn.edu WordPress REST, slug judging-and-evaluation (modified 2024-06-03) | Verbatim (not in the rendered page text; only via REST) | VP (historical) |
| 17 | Case word counts; five "must" tests; R-C34, R-C58, R-C61, R-C66-R-C70; Guide L84-86; TN guide L1-5, L44; IPS guide L60-77 | repo official files | Match | VRF |

Not re-checked: Yaniv & Foster 1995 (image-only scan); Tenney et al. 2007 (already SNIPPET-UNVERIFIED in D6).

## 3. Do the implications follow? (the case wins)

- **D5 finding 1 (flexibility needs a rule) follows** from case L102-107 ("committing all remaining assets could limit
  her financial flexibility"; no contingency fund required) and test 5 (L144). It is the most useful new result in the
  cluster. The give-back share s earns its place: s = 0 collapses the range to "one exact amount" (case L115 rejects it),
  s = 1 leaves no flexibility.
- **D5 finding 3 overreaches** (D5 C2, C3): the case says she will "describe how much she expects to contribute"
  (L110). An expectation is not a pledge, so no co-sponsor can "count" anything unless Laura chooses to pledge it. The
  sound part is the direction: lead with what is already bought.
- **D6 finding 1 follows** (CFA rules applied per goal; case L61-74, L91-92). **D6 finding 3 does not** follow as
  stated: the rule does not pin 60% (D6 C1). **D6's M018 reasoning** (career risk ≠ investment risk) is right, but the
  same file then uses her career-regret line as the reason for stocks (D6 C3).
- **D12 finding 2 follows** for option (ii); for (iii) the premise (three hedge trades) is wrong without a position cap
  (D12 C3). **D12 finding 1's element split conflicts** with the official Guide's own list of what a note should
  capture (D12 C1). **D12 finding 3 follows** and matches D8 rules 1 and brief s8 item 8.

## 4. Contradictions found (and how they resolve)

| # | Between | Contradiction | Resolution |
|---|---|---|---|
| X1 | D5 vs D6 | D5 candidate lock share a = 0.7; D6 "supports 80-90%, argues against anything below 70%" | D6's widths assume s = 1. Measured the same way, D5's (0.7, 0.5) range is *narrower* (1.26x) than D6's (0.8, 1.0) at 1.30x. The comparable choice is the promised-but-at-risk share s(1 - a): 0.15 vs 0.20. Both pass D6's width test; the team picks. (AX2's D4 C2 "70% locked" threshold also assumed s = 1.) |
| X2 | D5 vs D6 | Top of range at the 85th percentile (D5) vs the 90th (D6) | One percentile in the IPS method; the money difference is small (top $180k vs $182k at the median state). |
| X3 | D6 vs D2 (AX2 audit) | D6 "confirms 60%"; D2's 50/50 survives as a team option | The rule itself gives 50-70% across inputs (50% with JPM and a 1% fee). Both are inside; neither is "confirmed". |
| X4 | D6 vs ticket | Hedge "sizes to ~$292k"; ticket option (ii) hedge is 66% = $198k | Scale wording (D6 C2). |
| X5 | D12 vs ticket | (iii) "IEF, TLH, SPTL" notes; ticket buys SPTL only under a cap below 44% | Two trades without a cap (D12 C3; same as AX2's blocking finding on D10). |
| X6 | D12 vs D6 vs ticket (and AX2 D2-C6) | VGSH: "risk management" / "credibility or flexibility" / "a different funding purpose" | Compatible: one Guide role word ("risk management" or "liquidity"), echo "flexibility as the project develops", never "the floor". Team records its choice. |
| X7 | D12 vs Guide L84-86 | Note spec omits "supporting research or analysis" | Guide wins (D12 C1). |
| X8 | D6 / D12 vs brief s16 | Pitch spec says the payments are "bought in 2027"; IPS rule lists omit the nominal-US$ gap | Both certainty gaps must be named (D6 C4, D12 C4). |
| X9 | D8 rule 3 vs D8 rule 4 / D5 | Rule 3: "top = [stated percentile] of the rest" (all of it promised); rule 4 and D5 promise only a share s | Flag to the main loop: rule 3 should read "top = bought amount + [share] x [stated percentile] of the rest". D8 not edited (outside this cluster). |
| X10 | D12 vs guardrails L49 | "No character limit is published" vs "plan to 300" | Both true: no WInS limit is published; 300 is a sister-product figure used as a precaution. |
| X11 | D5 vs D3 model v2 (written in parallel) | D5 "never cap the gift"; D3 lists capped rules with P(within) 100% | Report a capped rule with "P(top reached)" (about 20% in D3), never "P(within) 100%". D3's "floor + half of the excess" row equals D5's a 0.8 / s 0.5 row, so the engines agree. D3 also reports the model understates crash years (supports D6 C1). |

Consistent with brief s14 and the ticket: $292,264; 173 of 185 days; ~24% (ASM); spot duration 10.16y; IEF 6.86y /
TLH 11.59y; the 66% hedge; "never" rules; no Laura quotes in TN or IPS; no "floor-first leap".

## 5. Overclaims, jargon, precision, complexity, privacy

- **Overclaims fixed:** "guarantee" / "bottom guaranteed" / "never below it" without "barring U.S. Treasury default"
  (D5 C3); "backstopped describes Laura's floor exactly" (D5 C2); "stops depending on markets" for bond funds (D6 C2);
  "confirms the provisional 60/40", "pick unchanged with fat tails" (D6 C1); "WInS notes may be capped at 300" stated as
  the headline (D12 C2). No file calls the funds "matched".
- **False precision:** "3 of 19" (D12 C6); "60%" from a 10-point grid (D6 C1); "98%" (D5 C4); tautological 50%/10%
  (D5 C8). Probabilities to one decimal are fine internally; D6 already bans decimals in the IPS.
- **Jargon to define or drop if any of it reaches the team pack:** "i.i.d.", "lognormal", "Student-t with 4 degrees of
  freedom", "λ (loss-aversion coefficient)", "calibration" (D6 defines the last). D5 and D12 define their terms.
- **Complexity:** D5's rule has three parameters (a, s, q). Each earns its place (a sets what is bought, s sets
  flexibility, q sets the top), and the whole rule fits in two plain sentences. D6's eight-rule comparison table is
  analysis, not IPS content: the IPS needs one rule.
- **Privacy and tokenism:** none found. Laura appears only through the case and her public professional record; D12's
  "Match Quality" and usability-testing links are kept private and labelled; no identity-based investment choice.
- **Submission-ready prose:** none. D5's quoted confidence line ("below the floor: only if ...; above the top: about
  1 in 7") is the nearest thing to a sentence; treat it as a content spec, and the team writes its own.

## 6. The corrections (full wording in each file's appendix)

| File | # | Severity | One line |
|---|---|---|---|
| D5 | C1 | important | Scope: keep the range/flexibility METHOD as IPS rules; move numbers, NT$, excerpt checklist to "later" |
| D5 | C2 | important | Withdraw "Kresge's 'backstopped' describes Laura's floor exactly"; the phrase covers other source types |
| D5 | C3 | important | "Guarantee" → "bought, not forecast, in US$, barring U.S. default"; "co-funders count the floor" is INT |
| D5 | C5 | important | Lock-share conflict with D6 resolved via s(1 - a); D5's rule passes D6's width test |
| D5 | C4, C6-C11 | minor | 98% → 94%; lopsided range; 2031 rate sensitivity; tautologies; cost vs buying power; harmonise q and D8 rule 3; capped rules in D3 need "P(top reached)" |
| D6 | C1 | important | Stock-share rule gives ~55-70%, not a robust 60%; fat-tail check is not a stress test |
| D6 | C2 | important | Hedge-note row: no "$292k" as the WInS size under (ii); no "stops depending on markets" |
| D6 | C3 | important | Career-regret line is not the reason for stocks (same domain transfer D6 rejects) |
| D6 | C4 | important | Pitch/IPS spec: payments may finish from the 2028 deposit; name the nominal-US$ limit; whole-portfolio stock share |
| D6 | C5 | important | Width criterion must use s(1 - a) or the width, not the lock share alone |
| D6 | C6 | important | Scope: M197 numbers and FR charts to "later" |
| D6 | C7-C11 | minor | VGSH wording; "risk need nil at today's prices"; "10 of 10 covered" timing; applicability labels; harmonise q |
| D12 | C1 | important | Note elements must follow Guide L84-86 (reasoning, alignment, supporting research, role) |
| D12 | C2 | important | 300-character cap: mixed evidence; verify at zero risk before the first note |
| D12 | C3 | important | Option (iii) without a cap = two trades; a third note needs a planned genuine decision |
| D12 | C4 | important | Add the nominal-US$ gap to the IPS rules |
| D12 | C5-C10 | minor | PDF page 10; "3 of 19" precision and dating of 173/185; Match Quality = INT; Nielsen = analogy; Queensland time; VGSH wording |

## 7. What goes forward (the part that serves TN and the IPS)

**TN pack (tier 1; notes are permanent):**
- [ ] Before the first order: confirm the note-box limit at zero risk (Stock-Trak/Wharton support, or a long test text
      on the review screen without pressing Confirm). Draft to 300 characters until then.
- [ ] Each note carries the Guide's four elements: Laura's need (reasoning); which part of the plan it is (alignment);
      one checkable fact (supporting research); one role word.
- [ ] Hedge: role "future funding"; "moves with the value of her payments when rates change (about 10 years)"; the
      ~$292k real-plan cost goes in the reflection; never "match", "mature in her years", "stable", "reduce volatility",
      "stops depending on markets".
- [ ] VT: role "growth"; only money the promise does not need; a fall shrinks the facility amount, never the payments.
- [ ] VGSH: role "risk management" or "liquidity"; flexibility as the project develops; never "the floor".
- [ ] If option (iii): plan the genuine third decision now (without a cap there are only two orders).
- [ ] Each "how it serves Laura" line passes the swap test (D6 s1.1). No Laura quotes; no career story as a reason.

**IPS: rules to fix before Nov 6 (tier 2):**
1. Risk tolerance per goal (D6 finding 1, CFA 2020): payments need no market risk at today's prices and can bear none;
   growth money can bear losses (living costs outside; no withdrawals before 2033); her investment willingness is
   inferred, not observed; what would change the view.
2. Two certainty gaps named plainly (brief s16): if the ladder costs more than $300k in January 2027, the longest
   payments are bought first and the rest is completed from the 2028 deposit before any growth money is invested; a
   late or short 2028 deposit hits the facility amount, never the payments; "certain" means nominal US$, barring a U.S.
   Treasury default, and a fixed $50k buys less each year in Taiwan.
3. Stock share of the growth money set by one stated rule (a threshold and a probability, e.g. "about 19 in 20 chance
   of ending 2033 with at least the money put in"), giving about 55-70% on current inputs; the team states its pick
   (e.g. 60%, or 50% on cautious inputs) and the whole-portfolio stock share by stage.
4. 2031 range method: buy a share a of the growth money as a Treasury note maturing before 2033 (the bottom = the
   amount bought); in 2033 give that plus a share s of what the rest has become, uncapped; keep the other (1 - s) for the
   project; top = the bought amount + s x a stated percentile of the rest; confidence stated on both sides with the
   model named; operating payments never touched. Choose (a, s) by "how much of the promised gift is still at market
   risk in 2031", s(1 - a) (candidates: D5 0.7/0.5; model 0.8/1.0).
5. Every forecast-based statement carries a word marking it as assumed; no dollar range or percentile in the IPS.
6. Paraphrase test of the 50-word pitch and rule sentences with 6 unpaid readers, two rounds (D12 M234), logged
   without personal data.

**Later (after Nov 9), one line each:** D5 fundraising-excerpt checklist (M094); NT$ reference band; "likely figure"
presentation and the lopsided-range wording; p5/p50/p95 floor/added/kept visual; Kresge pledge-window note; D6 M197
dollar states and bar chart; bad-year illustration; design-table chart; FR opening from the 2031 conversation; D12's
own later items (grade column; co-sponsor paragraph paraphrase test).

**Flags to the main loop (outside this cluster):** D8 rule 3 wording should include the give-back share (X9); the
ticket's VGSH note wording should match X6; the Session Rules screenshot should record whether the "one single stock"
position limit covers ETFs.

## Sources

All web sources in section 2 were accessed 2026-09-28 with `research/insight_v1/scripts/fetch_text.py` (plus curl on
the Wharton WordPress REST endpoint https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages?slug=judging-and-evaluation).
Repo files (VRF): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L10-20, L40-50, L59-75, L86-120,
L130-150); `2026_WGY_Investment_Competition_Guide.txt` (L80-90, L150-160); `2026_WGY_Trading_Notes_Analysis-FINAL.txt`
(L1-53); `2026_WGY_Investment_Policy-FINAL.txt` (L60-80); `SMApply_Deliverables_Page_2026-09-27.md` (L51);
`research/insight_v1/phase_A/case_register.md` (R-W16, R-W20, R-W21); `wins_now/securities_and_allocation_v0.md`;
`phase_D/D8_practice.md` (rule table); `phase_D/audit_markets_rules.md`; `phase_D/D13a_laura_quotes_verified.md`,
`D13c_voice_map.md`. Scripts: `D5_range_and_flexibility.py`, `D6_behavioural_numbers.py`, `D12_*.py`,
`AY1_audit_checks.py`.

## What this teaches

- **Re-run the numbers on a finer grid before you call a result "robust".** A rule that "picks 60%" on 10-point steps
  picked 65% on 5-point steps with the same file's own inputs. Robustness is shown by moving the inputs, not asserted.
- **A quote can be exact and still be misused.** Kresge really wrote "backstopped", but for a different kind of money.
  Read the sentence around a word, and the glossary, before borrowing it.
- **Two experts can both be right and still disagree on paper.** D5 and D6 argued about the lock share because each
  held a different second number fixed. Name every parameter, and the disagreement often disappears.
- **The official guide beats a clever shortcut.** A 300-character plan that dropped "supporting research" would have
  saved space by cutting what Wharton asked for. Check the source text first, then optimise.
- **Promises need the right verbs.** "Bought" and "barring a U.S. default" are true; "guaranteed" and "stops depending
  on markets" are not. For a client whose public credibility is part of her income, the verb is part of the risk
  management.
