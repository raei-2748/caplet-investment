# AY2 cluster audit: Wharton intent (D7), practice benchmark (D8), communication (D9)

Agent AY2, insight_v1 run, Phase D audit. Written 2026-09-28. This is an AI-generated audit for Team Caplet. It checks
three specialist files before they reach the strategy team. It holds no submission-ready prose. The team decides and
writes every word of every note, reflection, pitch and IPS.

Relayed user question ("what would be delivered at the end of this task?"): this audit step delivers this summary,
one "## Audit corrections (AY2)" section appended to the end of each of D7, D8 and D9, and one script,
`research/insight_v1/scripts/AY2_audit_checks.py`. Nothing is committed.

Scope applied: brief section 17 (Trading Notes and IPS only). Every correction below says which deliverable it serves:
**TN** (Trading Notes, Oct 23) or **IPS** (Nov 6).

Status labels as in brief section 3: VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED (SNIP),
ASSUMPTION (ASM), INT (AY2's judgement).

---

## 1. Verdict

**Pass with corrections. No blocking errors.** Every number the three specialists quote reproduces from their scripts.
Every decision-relevant quote I re-opened (30 checks) is verbatim on its source. The strategic direction of all three
files holds. None of them changes the lock-early architecture.

The problems are in four areas:
- **Overclaims inside rule wording:**
  - D8 rule 1 says only the facility shrinks if the 2028 deposit is small, which is false in the joint tail.
  - D8's headline says "needs met at today's yields", but it compares the wrong horizon and treats the facility as a
    need.
  - D9 lets VGSH carry the 2031 promise and uses "already owned".
- **Cross-file contradictions:**
  - D7's pitch rule clashes with the WInS book under option (ii).
  - D7's "refined" candidate clashes with the ticket's gate.
  - D7's IPS hedge clause clashes with the ticket's duration band.
- **Missing official vocabulary:** "uncertainty" (11 official uses, and case test 3) and the currency gap that brief
  s16 makes binding.
- **Text that is too close to submission-ready:** mainly D9's fill-in sentence for a permanent WInS note, plus slogans
  in D7, D8 and D9.

There is also one collective risk: the three files together ask the 500-word IPS for 13-15 elements. That needs one
word budget (section 5).

Confidence: high on the reproductions and the source checks. Medium on the word-budget estimate, which is built from
the specialists' own guesses.

---

## 2. What was re-run and re-opened

**Scripts (all re-run 2026-09-28 from the repo root; every quoted figure reproduced):**

| Script | Figures checked | Result |
|---|---|---|
| `D7_rule_trigger_odds.py` | 4.45bp/day; band odds 0.00/0.12/0.29%; drift ~0.08y; 76/53/35/12% moves; 83% "touched"; P(ladder > $300k) ~23% | Reproduced (live treasury.gov CSV, latest 09/25/2026) |
| `D8_practice_numbers.py` | $292,264 and $394,930 checks; IRRs 1.05/5.09%; $203,998; +$8.9k/+$10.7k/+$12.5k; fees -$2.6k to -$33.9k; 0.6x/2.1x/4.2x; drift p5/50/95 50/62/73%, 49% outside | Reproduced |
| `D9_numbers.py` | vocabulary counts; 40.3/38.7/38.5%; $2,890 per 10bp; ~$20.4k a year; T3 +$30,600 / -$27,374; 69-77% | Reproduced |
| `D9_ips_page_fit.py` | 44-46 lines needed of 46 (Letter, 27.6pt); ~525 max IPS words | Reproduced (assumptions labelled in the script) |
| `D9_draft_checker.py --demo` | 59 words, 413 characters, 0 digits, 57 shared three-word phrases | Reproduced |
| **New:** `AY2_audit_checks.py` | [1] consistent-input growth-money percentiles; [2] fat-tail and crisis-volatility band odds | See section 4 |

Also measured: Wharton's sample IPS PDF, with pypdf. It is US Letter at a 24.0 pt line pitch, with one blank line
before the IPS heading (VRF). This confirms D9.

**Sources re-opened with `fetch_text.py --grep`.** All were served from the helper's cache of 2026-09-27/28 pages,
which are the primary bytes fetched in this run. All returned **FOUND VERBATIM** unless noted.

| # | Claim (file) | Source | Result |
|---|---|---|---|
| 1 | FOMC "October 27-28" (D7) | federalreserve.gov FOMC calendar | VP |
| 2 | "Can you tweak it? Absolutely!" / "Your strategy should be unique to your team." (D7) | globalyouth.wharton.upenn.edu/developing-strategy/ | VP (older season) |
| 3 | "simple, elegant ideas" (D7) | Wharton 2025 top-10 article | VP. Speaker: Hahn, "a judge for the semifinals", who also praised the "written reports". D7's "videos only" caveat is too narrow |
| 4 | 2021-22 case "for at least 10 years" (D7) | Wharton 2021-22 case page | VP. It also shows a past case with a 10-year payment stream |
| 5 | "less is more, and having an explainable strategy" (D7) | Wharton 2023 tales article | VP |
| 6 | CFA IPS 2010: "objective course of action ... market disruption"; "clearly identified in advance"; no-rebalance "should be documented"; "required real growth rate of 4 percent" (D8) | CFA IPS PDF | VP (4 of 4) |
| 7 | Asset Manager Code: B.5.a; "expressly understood and agreed to"; "gross- and net-of-fees returns"; B.6.a "ability and willingness" (D8) | CFA AMC PDF | VP. B.6.a first failed only because the PDF text layer has a line break ("ri sk") |
| 8 | Russell: "lock down the benefits promised ..."; "additional risk taken only on assets above a defined surplus threshold"; "surplus glidepath" (D8) | russellinvestments.com 2026-07 | VP |
| 9 | Kitces: "really is 1%"; "1.75% for portfolios up to $500k"; "almost 1.25%" (D8) | kitces.com 2017 | VP (the survey is from 2017) |
| 10 | Chhabra 2016 "being really good at what you do, your passion"; CFA 2015 blog line (D8) | wealthmanagement.com; blogs.cfainstitute.org | VP |
| 11 | APRA SPS 160 "within one year" / "must not exceed three years"; BofA "at set trigger points"; NISA trigger points (D8) | apra.gov.au; bofa.com; nisa.com | VP |
| 12 | Yale "from two years ago" (D8) | provost.yale.edu | VP, **but trimmed**: it is the 20% leg of an 80/20 smoothing rule |
| 13 | FCA FG11/05 "capacity for loss" definition (D8) | fca.org.uk PDF | VP |
| 14 | Retired Wharton judging page: "Excessive investing jargon ..."; "precious space repeating known facts ..." (D9) | Wharton wp-json page | VP (past season) |
| 15 | IPCC: "reciprocal statements"; "statements of fact without using uncertainty qualifiers" (D9) | ipcc.ch AR5 note | VP |
| 16 | Investor.gov "longer time horizon may feel comfortable ..." (D9) | investor.gov | VP |
| 17 | Overachiever 2021 "with unstable income" (D7, D9) | overachievermagazine.com | VP. The full line opens "It's not an easy thing to say, ..." (D13a); it is Final Report only |

**Official files (VRF, line-checked):**
- TN guide L7-8, L12, L29-30, L36-39, L44, L53;
- Guide L70, L85, L89, L156-158, L183;
- Infographic L24-25, L41-42;
- IPS guide L10, L20, L25, L35-36, L45-57, L59, L68-69, L73-74, L82, L101-104, L116, L123-124;
- case L16, L44, L63, L70-73, L85, L90-99, L114-119, L129-130, L136-143, L152, L161-162;
- SMApply L49-57.

All say what the specialists say, with these exceptions:
- **TN guide L12 and case L152** use "aligned with, tested, or refined" and "reflected, tested, or refined". D7's
  summary says every official text reads "supported, tested, or refined".
- **"Certainty" counts:** the case has 4 "certainty" plus 2 "uncertainty". D7's "6" counts both words.

**Not reproducible here:**
- **D7's two WebSearch results** ("no public discussion of the case"): these are not decision-relevant and are left
  as D7 labelled them.
- **Word's 27.6 pt "Double" line height:** this cannot be tested without Word. It stays ASM, and the exported-PDF check
  stays binding.
- **A historical fat-tail check on real S&P 500 data:** the data download was not permitted in this session. It was
  replaced by a model sensitivity (section 4), labelled ASM.

---

## 3. Corrections, ranked (full list at the end of each file)

| Rank | File | Severity | Deliverable | Correction (short) |
|---|---|---|---|---|
| 1 | D7 + D9 (and ticket) | important | TN + IPS | Under option (ii), D7's pitch rule "no stock-market risk until all ten payments are bought" is visibly contradicted by a day-one VT buy next to a ~$198k hedge against a ~$292k promise. D7's own TN plan assumes (ii). So under (ii), the ticket's three-element scaling sentence must appear in the IPS, and a scaling clause in the hedge and growth notes. Under (iii), the rule is visibly true but there is no growth note. This is a new input to gate box (b); it does not decide it. |
| 2 | D8 | important | IPS | Rule 1's "only the facility range shrinks" is false in the joint tail: rates fall **and** the 2028 deposit is smaller than the shortfall (about $7k at -50bp, $23k at -100bp; brief s6). The frozen rule must say what then happens. |
| 3 | D9 | important | TN | VGSH is mapped to "the amount she can promise co-sponsors in 2031", with "already owned" as its certainty word. That re-introduces the "floor proxy" overclaim S4 removed. Before 2031, VGSH is growth money; use the ticket's "can later become". |
| 4 | D7 | important | TN | Refinement candidate (a), the TLH/SPTL cap split, is not a "refined" decision. The ticket's gate fixes the cap branch before the first order, so presenting SPTL as a refinement would misdescribe a planned buy. |
| 5 | D7 | important | TN | "Tested" must use a pre-registered window (fill to Oct 20) and the end-date odds (~53%). The "83% touched at some close" figure only applies if the team picks the best date, which is cherry-picking. |
| 6 | D9 | important | TN | The M012 answer gives a fill-in sentence for a permanent WInS note ("... cost about $X at [trade-date] ..."). Recast it as elements, and mark quoted phrases "illustrative, do not copy". |
| 7 | D9 | important | IPS | The vocabulary omits "uncertainty": 11 official uses, and case L137 asks how uncertainty affects **both** the payments and the facility. Name the payments' residual uncertainties rather than implying none. |
| 8 | D9 | important | IPS | The assumption line names inflation but not currency. Brief s16 (binding) requires the nominal-USD vs Taiwan-costs gap to be named. |
| 9 | D8 | important | IPS | "Needs met at today's yields" / "4.81% is below today's 5-year (4.98%)" compares the wrong horizon (2026-31 vs 2028-33). The facility has no required amount (case L104). Compare with the 5.23% forward instead, and say it is not lockable. |
| 10 | D7 | important | IPS | Pitch spec (b), "payments certain in US$", must be conditional: once bought, barring U.S. default. |
| 11 | D7/D8/D9 | important | IPS | There is no joint word budget; see section 5. |
| 12 | D7 | minor | TN | `official_curve_pv.py` cannot value other dates. Use `A2_curve_recheck.py` or `D9_numbers.py` [3]. Curves can be pulled later; only WInS screenshots are needed on the day. Check ex-dividend dates in the window. |
| 13 | D7 | minor | IPS | "The hedge is never traded because rates moved" conflicts with the ticket's duration band. Say "never sold or trimmed; only re-mixed to keep its rate sensitivity". |
| 14 | D7 | minor | TN | Band odds to two decimals are false precision (section 4). The conclusion holds. |
| 15 | D8 | minor | IPS | The fee clause is a team assumption the case never raises. Cut it first if words run short. "0.15% = 0.6x" does not "exceed" the headroom. |
| 16 | all | minor | TN + IPS | Scope (s17): D7's and D8's Final Report items move to the one-line "later" list. D9 already complies. |
| 17 | D7, D8, D9 | minor | TN + IPS | Several ready-made phrases need marking as illustrative (listed per file). |

---

## 4. Upgrades and downgrades from AY2's own checks

- **D8's devil's advocate: UPGRADED (confirmed on one input set).** D8 set a Treasury-forward middle case ($204k)
  against a p5 from a different model ($159k), and called the gap an order of magnitude. `AY2_audit_checks.py` [1]
  re-runs it with one input set. Inputs (ASM): AC World 7.00% compound, 16.78% vol; bonds at the 5.23% forward,
  deterministic; 200k paths.
  - At 60% stocks: p5 **$155k (-$49k)** against Treasury-only $204k; median **+$13k**; p95 +$104k.
  - At 50% / 70%: p5 -$41k / -$56k; median +$11k / +$14k.
  - So the argument stands: stocks buy upside, not need. Read it as "about +$11-14k in the middle vs -$41-56k in a
    bad case".
  - Caveat: bond rates are held fixed, so the uncertainty in the 2028 reinvestment rate is ignored.
  - The opposite risk must travel with it: D13c/brief s16 say the plan already looks very cautious for a client who
    "takes the jump", and the case asks for "pursuing growth". Neither argument decides the 50/60/70 weight.
- **D7's band odds: conclusion CONFIRMED, precision DOWNGRADED.** `AY2_audit_checks.py` [2] re-runs D7's window
  under other assumptions.

  | Assumption (ASM) | 55-65 band | 57-63 band | Whole book +/-2 points |
  |---|---|---|---|
  | Fat tails (Student-t, 3 degrees of freedom) | 0.1% | 0.7% | 0.7% |
  | Crisis-level 35% volatility | 1-2% | 11-15% | 11-15% |

  - "Do not plan a discipline trade" holds.
  - Write "very unlikely (about 0-2% even in a crisis)", not "0.00%".
  - If a tighter band does fire in a crash, that is a genuine rule-triggered note, not staging.
- **D8's four-rule structure: UPGRADED.** The IPS guide itself asks the IPS to "establish your strategic approach to
  preparing for the operating commitment, managing the operating reserve's asset composition over time, determining a
  responsible facility contribution, and preserving appropriate financial flexibility" (L48-50, VRF). That is a more
  direct reason for rule 4 than the test matrix.
- **D9's research element in every note: UPGRADED.** The TN guide says notes "should document the research, analysis,
  and reasoning behind your investment decisions" (L7-8, VRF). This is in addition to Guide p.3.
- **D9's page-fit risk: CONFIRMED on the sample.**
  - Wharton's own sample is set at exactly 24 pt.
  - (INT) "Exactly 24 pt" is therefore a defensible reading of "double-spaced" if a draft overflows under Word's
    "Double". The team decides; the exported PDF is the test.
  - A common rule of thumb, about 250-300 double-spaced words a page, also puts 550 words plus headings right at two
    pages (INT).
- **Downgrades:**
  - **D7's "past cases were growth/return targets":** the 2021-22 case also had a ten-year payment stream.
  - **D7's "111%":** this is face value. At today's prices the payments cost $292k, 97% of the first deposit.
  - **D7's "certainty 6":** this count includes "uncertainty".
  - **D8's Yale analogy:** it rests on a trimmed quote.
  - **D8's "Code F.4.d requires":** the Code says "should provide".
  - **D9's "hundreds of teams will copy":** this is INT, not evidence.

---

## 5. One IPS word budget (cross-file; the ips_spec owner should fix it before drafting)

The IPS must fit about 470-490 words (D9, from the page-fit check). The three files each ask for "one clause", but
nobody has added them up. The table uses the specialists' own estimates. It is INT, not counted text.

| IPS element | Asked for by | Their estimate (words) | AY2 suggestion |
|---|---|---|---|
| Central idea + rates-fall branch (rule 1) | D7, D8 | 25-35 | Keep. Add the joint-tail branch (correction 2) |
| Growth mix, band, yearly reset (rule 2) | D8, D7 | 25-35 | Keep. Fold the return objective into its "because" |
| 2031 range method (rule 3) | D8, D9 M191 | 25-35 | Keep |
| 2033 order of use / reserve composition (rule 4) | D8; IPS guide L48-50 | 25-35 | Keep (required by the guide) |
| Governance line | D8 | 10-15 | Keep. Word it so it cannot read as permission to revise after Nov 6 |
| Where risk sits (M241/M226/M143 merged) | D9 | ~30 | Merge with the risk-tolerance sentence |
| Return objective per goal | D8 M109 | ~25-30 | Merge into rule 2 |
| Risk tolerance by goal (ability/willingness) | D8 M063/M081 | ~30-40 | Merge with "where risk sits" |
| Fee/cost principle | D8 M026 | ~20 | Cut first if over budget (case silent on fees) |
| Certainty definition | brief s7; D9 M062 | ~20-25 | Keep. Absorb inflation + currency here |
| Three trade-offs, "gives up X to get Y" | D9 M121 | 36-60 | Keep at about 12 words each |
| Laura "because" clauses | D9 M071 | 40-60 | Inside the rules, not extra |
| Inflation (+ currency) assumption | D9; brief s16 | 10-15 | Inside the certainty definition |
| Option (ii) scaling sentence | ticket s2 | 25-30 | Only if (ii) is chosen |
| "What / why" framing (IPS guide L53-57) | IPS guide | 30-40 | Opening lines |
| **Sum before connecting words** | | **about 310-475** | **Merging brings it to about 300-380, leaving room for plain connecting prose** |

---

## 6. Cross-specialist contradictions and tensions

| # | Between | Issue | Resolution (decision owner) |
|---|---|---|---|
| C1 | D7 M011 pitch rule vs ticket option (ii) vs D7 M002 TN plan | See rank 1 | Gate box (b), team |
| C2 | D7 refinement (a) vs ticket gate (c)+(e) | The cap branch is decided before trade 1, so it is not a refinement | Drop (a); keep (b), the pre-announced provisional split |
| C3 | D7 IPS hedge clause vs ticket duration band | "Never traded" vs the IEF/TLH re-mix | Reword (rank 13) |
| C4 | D9 VGSH label vs ticket red-team fix 4 | "Already owned" 2031 promise vs "can later become" | Use the ticket's wording |
| C5 | D8 M109 (low end of the band) vs D13c / D9 M071 ("not set at the minimum to look safe") | Opposite pressures on the equity weight | Show both sides to the team. Section 4 numbers apply to both |
| C6 | Statistics degree used in three places (ticket VT note; D7 certainty definition; D9 "once at most") | Decoration risk | Pick one place across TN + IPS |
| C7 | D9 "locked rates" vs D8 "forward, not lockable" | Vocabulary | Use D8's wording |
| C8 | D7 "certainty 6" vs D9 "certainty 4" | Counting method | Use 4 (standalone word) and report "uncertainty" separately |
| C9 | Blueprint 01 section 3 risk example ("does not matter for held-to-maturity matching") vs D9 vocabulary | False for WInS funds | Fix when blueprint 01 is updated |

No contradiction was found with the brief section 14 facts ($300k WInS cash, rules, P(ladder > $300k) ~24%, durations,
FOMC). All three files respect the D13 quote rules: no Laura quotes in the TN or IPS; "unstable income" is Final
Report only and verified.

---

## 7. Privacy, tokenism, jargon, submission-ready prose

- **Privacy:** a scan of all three files for family, personal and student-data terms found nothing. Laura appears only
  through the case and her public professional record. No student surnames, emails or rankings.
- **Tokenism:** no identity- or Taiwan-based holdings; D8 and D9 both rule them out. The only risk is the statistics
  degree used as a hook in several places (C6).
- **Jargon:** D8's framework vocabulary (LDI, GBWM, glide path) is defined, and D8 keeps it out of the IPS. D7 bans
  "LDI, duration, DV01" from the pitch. D9's checker flags jargon.
- **Submission-ready prose (mark as illustrative):**
  - D7 L23-24 and L159-160 (the rule sentence in italics), and L121;
  - D8 L134-135 (a reflection clause);
  - D9 L266-269 (the note template), L288, L445 and L483.

  None is a full drafted pitch, note or IPS paragraph. They are short enough to be copied straight into a 50-word
  pitch or a permanent note, which the AI policy forbids.

---

## 8. What goes to the strategy team (checklist)

- [ ] Gate box (b): decide (ii) vs (iii) with both new inputs: D9's word cost and D7's pitch-rule consistency (C1).
- [ ] TN plan: three real trades. "Refined" only via a pre-announced split decision. "Tested" on a pre-registered
      window, with WInS screenshots on the fill date and the end date.
- [ ] Label table for notes: VGSH as "short-Treasury part of the growth money" (C4); certainty words from D9 plus
      "uncertainty".
- [ ] IPS rules 1-4 plus governance, with the joint-tail branch in rule 1 and the reworded hedge clause.
- [ ] One word budget (section 5) before the first IPS draft.
- [ ] One place for the statistics degree.
- [ ] The Final Report items from D7 and D8 go to the one-line "later (after Nov 9)" list.

---

## Sources (accessed 2026-09-28 via `research/insight_v1/scripts/fetch_text.py --grep`, helper cache of 2026-09-27/28)
- https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- https://globalyouth.wharton.upenn.edu/developing-strategy/
- https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
- https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/
- https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/
- https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages?slug=judging-and-evaluation
- https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
- https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/amc/asset-manager-code-and-guidance-2nd-ed.pdf
- https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html
- https://www.kitces.com/blog/independent-financial-advisor-fees-comparison-typical-aum-wealth-management-fee/
- https://www.wealthmanagement.com/investment-news/q-a-with-ashvin-chhabra-you-re-investing-all-wrong
- https://blogs.cfainstitute.org/investor/2015/08/05/ashvin-chhabra-on-wealth-management-the-value-proposition-lies-in-understanding-client-goals/
- https://handbook.apra.gov.au/standard/sps-160 ; https://business.bofa.com/en-us/content/workplace-benefits/glidepaths-for-pension-plans.html ; https://www.nisa.com/perspectives/dldi/
- https://provost.yale.edu/how-exactly-does-spending-policy-work
- https://www.fca.org.uk/publication/finalised-guidance/fsa-fg11-05.pdf
- https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf
- https://www.investor.gov/introduction-investing/getting-started/asset-allocation
- https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid

Repo files (VRF):
- `competition/official/2026_27/` (the case; IPS, TN and competition guides; infographic; SMApply page) and the IPS
  sample PDF;
- `research/insight_v1/_context/brief.md`;
- `phase_A/{case_register,fact_register}.md`;
- `phase_D/{D5_cosponsors,D13a_laura_quotes_verified,D13b_other_quotes_verified,D13c_voice_map}.md`;
- `wins_now/securities_and_allocation_v0.md`;
- `research/blueprints/01_trading_notes_blueprint.md`;
- `research/council_2026-09-27/team_notes_2026-09-27.md`;
- `research/verified_2026-09-27/official_curve_pv.py`.

Scripts:
- `research/insight_v1/scripts/{D7_rule_trigger_odds,D8_practice_numbers,D9_numbers,D9_ips_page_fit,D9_draft_checker}.py`
  (re-run);
- `research/insight_v1/scripts/AY2_audit_checks.py` (new).

---

## What this teaches
1. **Re-running is cheap; re-reading is where errors hide.** Every number reproduced. The errors were in the words
   around the numbers: "only the facility shrinks", "locked" for a forward rate, "already owned" for money not yet
   promised.
2. **Two correct files can still contradict each other.** D7's pitch rule and the WInS option (ii) are each sensible
   alone. Together they tell a reader two different stories, so consistency has to be checked across files, not only
   within them.
3. **Compare like with like.** A middle case from one set of inputs against a bad case from another can mislead. Here
   the one-input re-run happened to confirm the point (about -$49k at p5 for +$13k in the middle). You only know that
   after doing it.
4. **Probabilities have a shape, not just a size.** "0.00%" from a thin-tailed model becomes 1-2% in a crisis, and
   11-15% for tighter bands. Say "very unlikely", and know what would change it.
5. **A word limit is shared.** Five good one-clause ideas from three people can still overflow 500 words. Someone has
   to own the budget.
