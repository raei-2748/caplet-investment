# D5 Philanthropy & Co-sponsor Analyst: the 2031 range, its confidence wording, kept flexibility, and the fundraising-excerpt checklist

Agent D5, insight_v1 run, Phase D. Written 2026-09-27. Questions: M003, M091, M107, M094 (from
`research/insight_v1/phase_C/survivors.json`). AI-generated research for Team Caplet, for brainstorming only. This file
contains **no submission-ready prose**: it gives numbers, evidence, decisions to take and "what a sentence must contain"
checklists. The six students choose and write every word (Wharton AI policy: AI use must be recorded in Works Cited;
students "must use their voice and words", R-W26/R-W49). No securities are recommended here (the 2031 two-year note is
already in the wins_now ticket and never appears in WInS). Laura's public professional record only; nothing here
suggests contacting her.

Status labels (brief section 3): **VP** = VERIFIED-PRIMARY (read by me on the primary page on 2026-09-27 with
`fetch_text.py --grep`, phrase found verbatim), **VRF** = VERIFIED-REPO-FILE, **SNIP** = SNIPPET-UNVERIFIED, **ASM** =
ASSUMPTION, **INT** = my interpretation (not a fact). R-, F-, SH-, BS- ids point to the Phase A files.

Terms (defined once):
- **Floor**: the part of the growth money that is bought in January 2031 as a 2-year U.S. Treasury note maturing before
  the 2033 contribution date. Its 2033 value is known in 2031.
- **Lock share (a)**: the share of the growth money ("sleeve") bought as the floor in 2031.
- **Give-back share (s)**: the share of the *unlocked* remainder's 2033 value that is added to the facility gift; the
  other (1 - s) stays uncommitted as financial flexibility.
- **Top of the range**: the gift the rule produces if the unlocked remainder grows at its q-th percentile (q = 85% here).
- **Percentile (p5, p50, p95)**: the value that 5%, 50% or 95% of modelled outcomes fall below. p50 = median.
- **Unconditional / conditional pledge**: a promise with no hurdle attached vs one owed only if a hurdle is cleared.

Script: `research/insight_v1/scripts/D5_range_and_flexibility.py` (run from the repo root; docstring lists inputs and
labels). It uses the same random stream and inputs as the verified `strategy_mc.py` and reproduces its numbers exactly:
2031 floor at a = 0.8 p5/p50/p95 **$127k/$165k/$217k** (F-402) and 2033 surplus **$159k/$207k/$273k** (F-401).
All model outputs below are **ASM-based** (JPM 2026 LTCMA inputs VRF; lognormal i.i.d. returns, 60/40 sleeve, no fees,
2031 two-year rate = today's 4.81%).

---

## 0. Top findings (ranked by impact on reaching the semifinals and on making the plan unmistakably Laura's)

1. **The current plan has a hidden contradiction, and one extra number fixes it (M003, M107; changes the strategy at
   parameter level).** Brief section 7 says "promise a bought floor plus an upside" AND "keep leftover money mainly as
   project flexibility". But with the model's 80% lock, the leftover is only ~20% of the post-reserve money, and every
   dollar of it that is kept as flexibility is a dollar that cannot be the "upside" in the range. If all of it is kept,
   the range collapses to a single number (which the case steers away from, R-C67); if all of it is given, there is no
   flexibility (R-C58, R-C84). The fix is one plain rule with two parameters: **buy a share a of the growth money as the
   floor in 2031; in 2033 give the floor plus half (s = 0.5) of what the rest has grown to; keep the other half
   uncommitted.** Candidate default a = 0.7 (numbers in finding 2). This is the team's decision.
2. **The numbers for the candidate rule (a = 0.7, s = 0.5, q = 0.85), at the median 2031 growth money of $188k (ASM
   model):** range **US$144k - US$180k**; the bottom is bought, so P(below floor) = 0 barring U.S. default; P(above top)
   = 15% (model). Flexibility kept in 2033: **$32k median ($23k p5, $45k p95), about 15% of the post-reserve money**.
   Each 10 points of lock share moves about **$20k** into the counted floor and takes about $10k each from flexibility
   and from the upside (a = 0.6: floor $124k, flexibility 20%; a = 0.8: floor $165k, flexibility 10%, range only 15%
   wide).
3. **A professional co-funder counts only the bought floor as money (M091, confirmed with new primary checks).** Kresge
   counts "Written pledges or cash" and wants other sources "committed, imminent or backstopped" (VP); U.S. nonprofit
   accounting books a conditional promise only when "the barriers to entitlement are overcome" (FASB ASU 2018-08, VP);
   the seed-money experiments work through "an unconditional commitment" (Rondeau & List, VP). So the fundraising
   excerpt leads with the floor. **New: the midpoint is useless as a planning figure, in the conservative direction.**
   Given what is known in 2031, the gift lands below the range's midpoint in ~0% of modelled paths, and between
   **$168k and $184k** in 98% of them (p1-p95). The floor is a guarantee, not a forecast; the funder should plan on the
   floor and be told the likely figure separately.
4. **The range must be a 2031 rule, not dollar figures fixed today (M091, M107).** The case asks for "the dollar range
   Laura should communicate" (R-C69), but the range is communicated in 2031. A floor copied from today's median
   projection ($144k) would be missed in **50%** of modelled paths; even today's p10-p90 band ($143k-$218k) would put
   the 2033 gift below its bottom in **10%** of paths, which is exactly the overpromise the case warns about (R-C66). The
   rule re-bases the floor on what she actually owns in 2031, so its floor is missed in 0%. The Final Report should show
   the rule, then the dollar range it gives at the median path, plus p10/p90 illustrations (**$118k-$147k** and
   **$178k-$223k**).
5. **Do not cap the gift at the top (M107).** If the gift is capped, P(within range) = 100% by construction, an empty
   confidence figure a statistics graduate would spot (SH-04). Uncapped, a good market visibly raises the amount, which
   the case requires ("how favorable ... outcomes could affect the amount", R-C70), and the excess is small (median
   **$2k**, p95 **$8k** above the top when it happens). The confidence statement becomes two-sided and honest: "below
   the floor: only if the U.S. Treasury defaults; above the top: about 1 in 7 (model)". Over-delivering never costs
   credibility; under-delivering does (R-C66).
6. **Minimum fundraising-excerpt checklist (M094): nine must-haves, six things to leave out** (section 4). New items not
   in the Phase A checklist: the floor cannot be handed over before 2033 (the case bans withdrawals, R-C34), so the form
   is "held in a Treasury note maturing before the contribution date"; the 2028-deposit risk is already resolved by
   2031 and need not be mentioned; the likely figure is stated separately from the range; the date prepared and the
   2033 confirmation date.
7. **Tier-2 consequence (IPS, Nov 6): the principle must be in the IPS, the numbers need not.** The IPS guide says the
   Final Report "should reflect the strategy established in your IPS" and the strategy "may not" be revised after Nov 6
   (IPS guide p.2, VRF). A flexibility rule that first appears in the Final Report could read as a new strategy. So the
   IPS needs one line naming the principle (bought floor promised; a stated part of growth beyond it kept uncommitted
   for the project). Numbers and the range stay in the FR (the IPS guide says a "final facility-contribution range" is
   not expected).
8. **Brunel's "10%" is not a benchmark for this (M003, partly mis-posed).** On the primary page it is the example
   family's own wish ("The family also wants to reserve 10 percent of their total wealth ... for what they call
   'opportunistic goals'", VP) and applies to total wealth, not to project money after a pledge. It cannot size Laura's
   flexibility. A better sanity anchor is verified and Laura-specific: Taiwan's construction cost index averaged
   **3.54%/yr** since 2021 (F-508, VP), which erodes a fixed US$ pledge by **7.2% / 11.0% / 14.9%** over 2 / 3 / 4
   years; the 1-sd two-year USD/TWD move is **6.8%** (derived). A ~15% flexibility share is the same order as three to
   four years of building-cost drift on her own pledge (ASM; a sanity check, not a contingency fund, which the case
   does not require, R-C61).

Whether Laura herself ranks flexibility above a bigger gift **cannot be tested** (contacting the client means
disqualification, R-W16). The case gives both sides: she wants a "meaningful personal contribution" (R-C64) and she
"recognizes that committing all remaining assets could limit her financial flexibility as the project develops"
(R-C58). So the answer is a stated middle, with the reason written down as a team ASSUMPTION.

---

## 1. M003 (tier 2 for the IPS line; tier 3 for the numbers): how much of the post-reserve money stays uncommitted as flexibility?

**Question (canonical):** What explicit rule or share of the post-reserve surplus should stay uncommitted as
"financial flexibility", rather than "whatever is left" or simply the unpledged upside, and does she rank it above a
bigger facility contribution?

**One-sentence answer:** Keep flexibility by rule, not by leftovers: buy about 70% of the growth money as the 2031
floor, and in 2033 give the floor plus half of what the remaining 30% has grown to, which keeps about 15% of the
post-reserve money (about $32k at the median, $23k at p5) uncommitted for the project; whether Laura would rank this
above a bigger gift cannot be tested, so it is a stated team assumption.

### Evidence
| Claim | Source (access 2026-09-27) | Status |
|---|---|---|
| "She recognizes that committing all remaining assets could limit her financial flexibility as the project develops." | Case p.3 (R-C58) | VRF |
| Test 5: "Preserves appropriate financial flexibility when determining the facility contribution." | Case p.4 (R-C84) | VRF |
| "Teams are not expected to determine the size or investment composition of a separate contingency fund or endowment." | Case p.3 (R-C61) | VRF |
| Living costs are covered outside the portfolio (so portfolio flexibility is project flexibility, not personal) | Case p.2 (R-C33) | VRF |
| Continued business income is one of the case's listed sources for remaining facility costs | Case p.3 (R-C44) | VRF |
| IPS: FR "should reflect the strategy established in your IPS"; strategy may not be revised after the deadline; a "final facility-contribution range" is not expected in the IPS | `2026_WGY_Investment_Policy-FINAL.txt` p.2 L68-77 | VRF |
| Brunel's example family "also wants to reserve 10 percent of their total wealth ($3.5 million) for what they call 'opportunistic goals'" | Brunel, CFA Institute Conference Proceedings Quarterly, March 2012, https://static1.squarespace.com/static/59e8d89d914e6b37450c946a/t/5c643e15104c7b43f7b84187/1550073366884/CFA+Goals+Based+WM_PDOC.pdf | VP (it is the client family's wish in a worked example, on total wealth: not a practitioner benchmark) |
| Taiwan construction cost index average 3.54%/yr since 2021; +6.53% y/y Aug 2026 is a one-year jump | fact_register F-508, F-509 | VP (per A2) |
| Laura's verified lines about keeping options open ("avoid siloing yourself into an end-all-be-all career situation", Poets&Quants 2018; "I did 50 things...", Overachiever 2021) are about careers, not money | D13a table lines 98, 115 | VP (context: career advice; use at most as character context in the FR, never as an investment rule; D13 limits the FR to 1-2 Laura quotes in total) |

### Numbers (script sections [1], [2], [8]; ASM-based model at the median 2031 growth money of $188k)
| Lock a | Give-back s | Floor (bought) | Top (q = 85%) | Range width | Kept flexibility p5/p50/p95 | Share of post-reserve money (median) |
|---|---|---|---|---|---|---|
| 0.6 | 0.5 | $124k | $172k | 39% of floor | $30k/$42k/$60k | 20% |
| **0.7** | **0.5** | **$144k** | **$180k** | **25%** | **$23k/$32k/$45k** | **15%** |
| 0.8 | 0.5 | $165k | $189k | 15% | $15k/$21k/$30k | 10% |
| 0.8 | 0.0 | $165k | $165k (a point) | 0% | $30k/$42k/$60k | 20% |
| 0.8 | 1.0 | $165k | $213k | 29% | $0 | 0% |
| 1.0 | - | $206k | $206k (a point) | 0% | $0 | 0% |

(Flexibility percentiles are across all 2027-2033 paths; the floor/top columns are at the median 2031 value.)

### Implication
- **Decision (team):** choose a (lock share) and s (give-back share). Candidate default a = 0.7, s = 0.5. Alternates:
  a = 0.8 if the team weighs the co-sponsor signal most (floor +$21k, flexibility falls to ~10%); a = 0.6 if it weighs
  flexibility most (~20%). Record the reason in the decision log (Articulation evidence).
- **IPS (Nov 6), one line must contain:** (1) the facility promise is only what has been bought two years ahead;
  (2) a stated part of any growth beyond it is kept uncommitted for the project's changes; (3) the operating payments
  are never touched. No dollar figures needed.
- **FR (Dec 4):** a small table of gift vs kept flexibility at p5/p50/p95 (a chart candidate: stacked bars "floor /
  added in 2033 / kept flexible" for p5, p50, p95); the reason for the share in one sentence tied to R-C58 ("as the
  project develops") and to building-cost drift (F-508), labelled as an assumption; one sentence that her living
  costs are outside the portfolio, so this is project flexibility.
- Deliverables: IPS, FR. Not TN (the TN guide excludes the facility contribution) and not WInS-now.

**Deadline tier:** 2 (IPS principle), then 3. **Confidence:** medium (the model reproduces verified outputs; the share
itself is a judgement). **Changes current strategy:** yes, at parameter level: adds the give-back share s and moves
the lock share from 0.8 to a candidate 0.7; resolves the brief section 7 tension. The wins_now ticket is unaffected (the
2031 share "never appears in a WInS note"). **Criterion:** Client Knowledge and Objectives (tailors to her
"flexibility as the project develops"); also Portfolio Analysis (financial flexibility under varying outcomes).
**What this teaches:** flexibility is only real if a rule reserves it before the money arrives; "whatever is left" is
a hope, not a policy.

---

## 2. M091 (tier 3): does a co-funder count anything beyond the bought floor, and should the excerpt lead with the floor?

**One-sentence answer:** No: professional funders count written, unconditional money, so the bought floor is the
headline planning figure, the upper part is information with a stated probability, and the midpoint should never be
used because, given 2031 knowledge, the gift almost always lands well above it.

### Evidence
| Claim | Source (access 2026-09-27) | Status |
|---|---|---|
| Kresge counts as initial funds "Written pledges or cash from individuals, corporations, businesses and foundations ... All pledges must be paid within five years from your fundraising end date." | Kresge Foundation, *A Guide to the Challenge Grant* (updated 2011), https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf | VP (2011 document; whether Kresge still uses it is not checked) |
| Kresge: some sources "should be committed, imminent or backstopped" | same | VP |
| Kresge asks capital applicants: "Do you have a plan for sustaining support gained during the campaign after it concludes?" | same | VP |
| Conditional contributions are "unrecognized initially, that is, until the barriers to entitlement are overcome" | FASB ASU 2018-08, https://storage.fasb.org/ASU%202018-08.pdf | VP (U.S. nonprofit accounting; Taiwanese co-sponsors may follow other rules: UNVERIFIED) |
| 958-605-55-51: a communication that "specified an intention to give" meant the charity "did not receive a promise to give" | same | VP (the example is a will that can be changed; applying it to Laura's upper figure is INT) |
| "A challenge gift is an unconditional commitment by a donor, or set of donors, to provide a given sum of money to the cause." | Rondeau & List, NBER w13728, https://www.nber.org/system/files/working_papers/w13728/w13728.pdf | VP |
| "challenge gifts positively influence contributions in the field, but matching gifts do not" | https://www.nber.org/papers/w13728 (abstract) | VP |
| Charities "maximize donations given by simply announcing the presence of a lead gift" | Huck & Rasul 2011 abstract, https://ideas.repec.org/a/eee/pubeco/v95y2011i5p351-362.html | VP |
| The case: she will "describe how much she expects to contribute"; she will "neither add to nor withdraw from the portfolio before 2033" | Case p.2-3 (R-C34, R-C63) | VRF |

### Numbers (script [3], [7] and the conditional check; ASM model)
- Given the median 2031 growth money and rule a = 0.7, s = 0.5: gift p1/p5/p50/p95 = **$168k / $170k / $176k /
  $184k**; floor $144k; top $180k; midpoint $162k, below which the gift falls in ~0% of paths.
- A floor fixed today at the median ($144k) is missed in 50% of paths; the 2031-rule floor in 0%.
- Kresge's five-year pledge window vs Laura's 2031 statement paid in 2033: two years, inside it (INT).

### Implication
- **Decision:** the FR fundraising excerpt leads with the floor (US$, form, date); the range follows; the confidence is
  split into P(at least the floor) and P(above the top). Also state the **likely figure** (the model median) as a
  separate, labelled number, because the range is deliberately lopsided (bottom guaranteed, outcomes cluster near the
  top). Do not present the midpoint.
- Wording choice for the team (no prose here): which verb goes with which tier (BS-05): the floor is "held/committed",
  the rest is "expected". Because of R-C34 she cannot hand money over in 2031, so do not imply the floor is already
  transferred or escrowed.
- New link worth one clause in the FR: Kresge's own word "backstopped" describes Laura's floor exactly (a pledge backed
  by a Treasury she owns) (INT).
- Deliverable: FR only. Tier 3.

**Confidence:** high on "lead with the floor" (three independent primary sources agree); medium on how Taiwanese
public funders count pledges (not verified). **Changes current strategy:** no (it confirms brief 8.7 and the chair
memo's "at least F; up to U"); it adds the "likely figure, not midpoint" point. The Phase C "answered" skeptic was right
that the direction was known; what is new is the evidence and the lopsided-range number. **Criterion:** Creativity and
Presentation ("communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to
prospective co-sponsors"). **What this teaches:** a number means what the reader's own books let it mean: a funder can
only budget on money that is promised without conditions.

---

## 3. M107 (tier 3): where does good-market money above the top go, and what does it do to the confidence figure?

**One-sentence answer:** Let the rule run uncapped, so in the ~15% of paths where markets beat the top the gift
exceeds it by a small amount (median $2k, p95 $8k) and the rest stays as flexibility; the confidence is then stated on
both sides ("below the floor only if the U.S. defaults; above the top about 1 in 7"), whereas capping the gift would
make "100% within range" true by construction and meaningless.

### Evidence
| Claim | Source | Status |
|---|---|---|
| "state how confident they are that her 2033 contribution will fall within that range" (two-sided) | Case p.3 (R-C69, R-AN9) | VRF |
| "explain how favorable and unfavorable market outcomes could affect the amount she can provide" | Case p.3 (R-C70) | VRF |
| "If Laura promises more than she can ultimately contribute, she could damage her credibility" (the risk is one-sided: overpromising) | Case p.3 (R-C66) | VRF |
| Statistician reader: a confidence that counts only the low end loses trust | stakeholder_map SH-04 | VRF (Phase A judgement) |
| Brunel/Das goal-probability table: "Wants" 80-85%, "Needs" 90-95% | Das et al. 2018, https://srdas.github.io/Papers/GBWM.pdf, Table 1 | VP (a practitioner scale, used here only to justify q = 85% as a "want", not a "need") |

### Numbers (script [4], [7]; ASM model; a = 0.7, s = 0.5, median 2031 value)
| q (top percentile) | Top | P(below floor) | P(above top) |
|---|---|---|---|
| 80% | $179k | 0 barring default | 20% |
| **85%** | **$180k** | **0** | **15%** |
| 90% | $182k | 0 | 10% |

When above the top: excess median $2k, p95 $8k; kept flexibility in those paths median $38k. The choice of q barely
moves the top (the unlocked part is small), so q is a wording choice more than a money choice.

### Implication
- **Decision:** no cap. The top is "the most co-sponsors should plan on", not a limit on her generosity. The rule itself
  answers R-C70: bad markets move the gift toward the floor (never below it, never into the operating reserve); good
  markets move it to or slightly past the top, and grow the kept flexibility.
- **Sentence the FR must contain (checklist, not prose):** both tail probabilities with the model named; the direction
  of the only possible miss (upward); who decides about money above the top (Laura in 2033, under the stated rule).
- Deliverable: FR. Tier 3.

**Confidence:** high on "no cap / two-sided statement" (logic plus case wording); medium on q = 85% (a judgement).
**Changes current strategy:** minor: replaces the chair memo's one-sided "up to U with about 90% model confidence" with
the two-sided statement and fixes the destination of excess money. **Criterion:** Portfolio Analysis ("reasonable
assumptions and projections to evaluate ... the facility contribution, and financial flexibility under varying market
outcomes"). **What this teaches:** a confidence number is only informative if the event it describes can actually fail;
design the rule first, then ask which way it can miss.

---

## 4. M094 (tier 3): the minimum checklist for the fundraising excerpt

**One-sentence answer:** Nine items make the excerpt credible to a finance reader and a non-specialist in one reading
(floor, form, likely figure, range with two-sided confidence, good/bad markets, operations already funded, what is not
promised, currency, date); leave out the model mechanics, facility-cost estimates, share-of-campaign figures, legal
claims, personal details and any AI-drafted wording. (Partly already answered by stakeholder_map SH-05/BS-04 to BS-17;
this merges and cuts it, and adds three new items.)

### Must contain (each maps to a source)
1. **The floor in US$, its form and maturity**: held in a U.S. Treasury note bought in January 2031 that matures
   before the 2033 contribution date; not transferable before 2033 (R-C34; new).
2. **The likely figure** (model median, labelled as a model number), separate from the range (M091; new).
3. **The range US$ floor - US$ top**, with the confidence on both sides: below the floor only on U.S. default; above the
   top about 1 in 7 (model named in one clause) (R-C69, R-AN9, SH-04).
4. **What good and bad markets do** in one line each: bad → toward the floor, never below it; good → at or slightly
   above the top, and the rest stays with the project as flexibility (R-C70, M107).
5. **Ten years of operating payments are already funded separately from her portfolio alone**, so co-sponsor money can
   go to the building (R-C48, BS-17; Kresge's "plan for sustaining support" question, VP).
6. **What is not promised**: facility cost overruns (her contribution does not rise beyond the stated range; scope
   adjusts), operating support beyond US$50k a year, anything after 2042 (BS-16, R-C49; PKF 2019, VP: funders want to
   know "how the grantee would respond to any unexpected revenue shortfalls or cost overruns").
7. **Currency**: "US$" on every figure; one NT$ reference with date and rate (at the median floor of US$144k:
   NT$4.59m at 31.82 on 2026-09-18; NT$4.30m-4.90m for a 1-sd two-year currency move of 6.8%) and one line that US$ is
   binding (BS-04, F-510; script [6]).
8. **Date prepared and next confirmation** (2031 statement; confirmed at the 2033 contribution) (new; keeps corporate
   and public funders' calendars, SH-08).
9. **Sized from her portfolio, not as a share of a budget** (BS-06; R-C95 says teams need not estimate facility cost).

### Leave out (and why)
- Monte Carlo mechanics, return assumptions, percentile tables → FR analysis section, not the excerpt (SH-09:
  non-specialist in one reading).
- The 2028-deposit risk → resolved before 2031; the floor already reflects it (new).
- Facility cost, budget, funding gap, campaign share → out of scope (R-C95).
- Legal enforceability claims → not the team's question (BS-05).
- Laura's personal details or quotes → privacy rule, and the excerpt is written as her material (D13 rules).
- Any AI-drafted wording → Wharton AI policy; the students write it.

### Implication
- **Sentence-level spec for the FR** (students write it). Length target: short enough to read in one pass; final
  format waits for the FR instructions released Nov 9 (R-C93). If space is tight, drop item 8, then item 9 (fold it into
  item 6).
- A good visual for the FR (not the excerpt): one horizontal bar per scenario (p5/p50/p95 of the 2031 growth money)
  split into "bought floor / added in 2033 / kept flexible".

**Deadline tier:** 3. **Confidence:** high (each item traces to the case or a primary source). **Changes current
strategy:** no. **Criterion:** Creativity and Presentation (co-sponsor communication is named in its wording).
**What this teaches:** credibility comes from saying exactly what is certain, what is likely and what is not promised,
in the reader's own units.

---

## 5. Sources (all accessed 2026-09-27)

Official / repo (VRF): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (pp.2-4);
`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` (p.2 L60-77);
`competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L20-21: co-sponsor draft not expected in TN);
`competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md` (L49-57 criteria);
`research/insight_v1/phase_A/{case_register,fact_register,stakeholder_map}.md`;
`research/insight_v1/phase_C/survivors.json`; `research/insight_v1/phase_D/D13a_laura_quotes_verified.md`;
`research/insight_v1/wins_now/securities_and_allocation_v0.md`; `research/council_2026-09-27/01_chair_memo.md` s5;
`research/verified_2026-09-27/strategy_mc.py`.

Web (VP, each phrase checked verbatim with `fetch_text.py --grep` on 2026-09-27):
| Source | URL |
|---|---|
| Kresge Foundation, *A Guide to the Challenge Grant* (2011) | https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf |
| FASB, ASU 2018-08 (Topic 958), June 2018 | https://storage.fasb.org/ASU%202018-08.pdf |
| Rondeau & List, "Matching and Challenge Gifts to Charity", NBER w13728 | https://www.nber.org/system/files/working_papers/w13728/w13728.pdf ; https://www.nber.org/papers/w13728 |
| Huck & Rasul (2011), "Matched fundraising", J. Public Econ. 95(5-6), abstract | https://ideas.repec.org/a/eee/pubeco/v95y2011i5p351-362.html |
| PKF O'Connor Davies, "Best Practices: Due Diligence on Grantees", July 2019 | https://www.pkfod.com/wp-content/uploads/2019/07/Best-Practices-Due-Diligence-on-Grantees-v4.pdf |
| Brunel, "Goals-Based Wealth Management in Practice", CFA Institute Conference Proceedings Quarterly, March 2012 (hosted copy) | https://static1.squarespace.com/static/59e8d89d914e6b37450c946a/t/5c643e15104c7b43f7b84187/1550073366884/CFA+Goals+Based+WM_PDOC.pdf |
| Das, Ostrov, Radhakrishnan & Srivastav (2018), *J. Investment Management* 16(3), Table 1 | https://srdas.github.io/Papers/GBWM.pdf |

Not verified by me: Taiwanese funders' pledge-counting rules (no primary source found; MOC pages refuse curl, per
Phase A); whether Kresge still uses the 2011 guide.

---

## What this teaches

A co-sponsor range is a promise design problem before it is a forecasting problem. Decide what is bought (the floor),
what is shared (half of the growth beyond it) and what is kept (the other half), and the confidence statement writes
itself: it can only miss upward. The same two numbers answer three case requirements at once: a credible range,
favourable and unfavourable outcomes, and preserved flexibility. And the reader decides what a number means: a funder
counts only money promised without conditions, so the plan should lead with exactly that.

---

## Audit corrections (AY1)

Auditor AY1 (cluster auditor: client psychology and co-sponsors), 2026-09-28. The text above is left unchanged; where
it conflicts with these corrections, the corrections win. Full audit: `research/insight_v1/phase_D/audit_client_cosponsors.md`.
Check script: `research/insight_v1/scripts/AY1_audit_checks.py` (reuses this file's engine and random stream).

**Reproduction.** `D5_range_and_flexibility.py` re-run 2026-09-28: every number in sections 0-4 reproduces exactly
(floor $127k/$165k/$217k and surplus $159k/$207k/$273k reconcile with F-401/F-402; the (a, s) table; $118k-$147k and
$178k-$223k; 50% / 10%; P(above top) 15%, excess $2k/$8k; NT$4.59m/4.30m/4.90m; 7.2/11.0/14.9%), except C4.
**Sources re-opened 2026-09-28** (fetch helper, `--grep` found verbatim): Kresge guide ("Written pledges or cash", "All
pledges must be paid within five years", "committed, imminent or backstopped", "plan for sustaining support"); FASB ASU
2018-08 ("barriers to entitlement are overcome"; 958-605-55-51 "did not receive a promise to give"); Rondeau & List ("an
unconditional commitment by a donor"; abstract sentence); Huck & Rasul abstract; PKF 2019 ("how the grantee would
respond to any unexpected revenue shortfalls or cost overruns"); Brunel 2012 ("reserve 10 percent of their total
wealth"; "opportunistic goals"); Das et al. 2018 Table 1 (Wants/Fears 80-85, Needs/Nightmares 90-95). All
VERIFIED-PRIMARY. Case lines R-C34, R-C58, R-C61, R-C66-R-C70 and IPS guide p.2 L68-77, VERIFIED-REPO-FILE.

| # | Severity | Issue | Correction |
|---|---|---|---|
| C1 | important | **Scope (brief s17, 2026-09-28, written after this file).** Sections 2-4 are Final Report material; the fundraising-excerpt checklist (section 4, M094) is named as out of scope ("fundraising excerpt drafts or checklists"). | Keep for the IPS only the METHOD, as "IPS: rules to fix before Nov 6": (1) in 2031 buy a share a of the growth money as a Treasury note maturing before the 2033 contribution; that bought amount is the bottom of the range; (2) in 2033 the gift = the bought amount + a share s of what the rest has become, uncapped; the other (1 - s) stays uncommitted for the project; (3) the top = the bought amount + s x a stated percentile of the rest; confidence stated on both sides with the model named; (4) the operating payments are never touched. Move to the "later (after Nov 9)" list, one line each: the excerpt checklist (section 4), the NT$ reference, the "likely figure" presentation, the p5/p50/p95 visual, the midpoint point, Kresge's pledge window. |
| C2 | important | **Withdrawn: "Kresge's own word 'backstopped' describes Laura's floor exactly" (s2 implication).** Kresge's glossary: "Backstopping–Formal use of specific alternative resources to cover anticipated government funds, planned gifts or long-term financing. These alternative resources often are organizational money, which will be replaced once the expected funding is available." The "committed, imminent or backstopped" sentence applies only to "long-term financing, government funds (if a substantial amount), organizational funds or bequests", not to individual pledges (VERIFIED-PRIMARY, re-read). | Laura's floor is her own asset behind her own expected gift, not a backstop of someone else's funding. Drop the clause. Finding 3 should say: Kresge counts "Written pledges or cash" from individuals; it wants *certain other source types* (financing, government, organizational funds, bequests) committed, imminent or backstopped. |
| C3 | important | **"Guarantee" overclaim** (finding 3 "The floor is a guarantee, not a forecast"; s2 "bottom guaranteed"; s3/s4 "never below it"). The floor is not a legal guarantee: she cannot transfer it before 2033 (R-C34), and the case says she will "describe how much she expects to contribute" (case L110, VERIFIED-REPO-FILE). By the FASB logic this file cites (958-605-55-51, an "intention to give" is not a promise to give), a co-sponsor could book even the floor only if Laura states it as a written, unconditional pledge, which is her legal and communication choice (out of scope). | Use "bought, not forecast", always with "in US$, barring a U.S. Treasury default". Downgrade "a professional co-funder counts only the bought floor as money" from a finding to INT: "funders count unconditional written pledges; the bought floor is the only part Laura *could* state that way". |
| C4 | minor | **Arithmetic.** "between $168k and $184k in 98% of them (p1-p95)": p1 to p95 spans 94% of paths by definition. | AY1 check [1]: 94.4% of paths fall in $168k-$184k; p1/p99 = $167.8k/$187.6k. Say "about 94% (p1-p95)" or "98% (p1-p99, $168k-$188k)". |
| C5 | important | **Cross-file contradiction with D6 on the lock share, resolved.** D5 proposes a = 0.7; D6 says the behavioural evidence "supports 80-90% and argues against anything below 70%". D6's widths assume s = 1 (all unlocked money promised). The width depends on both: top / bottom ≈ 1 + s(1 - a)/a x 1.21 (q = 90%; AY1 check [2]). | D5's (a 0.7, s 0.5) gives 1.25-1.26x, narrower than D6's own base (a 0.8, s 1.0) at 1.29-1.30x. The comparable quantity is the share of the growth money that is promised but still at market risk in 2031, s(1 - a): 0.15 (D5) vs 0.20 (D6 base) vs 0.30 (a 0.7, s 1.0). D5's rule passes D6's width test. Present one team choice: "how much of the promised gift is still at market risk in 2031", not the lock share alone. (AX2's D4 C2 threshold of "70% locked" was also computed with s = 1.) |
| C6 | minor | **The range is lopsided by design** (worth knowing before choosing wording). The lower half of US$144k-US$180k is reached only if the unlocked money loses about 36% in two years (AY1 [1]); the lowest ~65% of the width (floor to p1) is reached in under 1% of modelled paths. A reader who anchors on the midpoint is misled, and D6's evidence (Du et al.: "as precise as warranted") pulls the other way. | Not a rule change. For the IPS method, name the bottom as "the amount already bought", never as a low-case forecast. The "likely figure" vs a narrower stressed bottom is a Final-Report presentation choice (later list). |
| C7 | minor | **Model input.** The floor assumes the 2031 two-year rate equals today's 4.81% (ASSUMPTION). | At 3.0% the floor is 3.4% lower; at 6.0% it is 2.3% higher (AY1 [4]). Small; another reason the IPS states the method and no dollar floor. |
| C8 | minor | **Tautology presented as evidence** (finding 4). "A floor copied from today's median is missed in 50% of paths" and "the p10-p90 bottom is missed in 10%" are true by the definition of a median and a percentile. | Keep the conclusion (the range must be a 2031 rule); label the two numbers "by definition", not as findings. |
| C9 | minor | **Precision** (finding 8). 7.2/11.0/14.9% are cost *increases*; the pledge's buying power falls 6.7/9.9/13.0%. The index is in NT$, so US$ buying power also moves with USD/TWD. | Correct the wording if used; this is Final-Report material (later list). |
| C10 | minor | **Harmonise the top percentile.** D5 uses q = 85% ("about 1 in 7 above the top"); D6 uses p90 ("about 9 in 10"); D8 rule 3 says "the top = [stated percentile] of the rest", which omits the give-back share s. | Pick one percentile for the IPS method. D8 rule 3 should read "top = bought amount + [share] x [stated percentile] of the rest" so that it matches D8 rule 4 and this file (flagged to the main loop; D8 not edited). |
| C11 | minor | **Cross-check with D3 model v2** (`phase_D/D3_model_v2_results.md` s4, written in parallel). D3 lists *capped* rules ("give 90%, capped": P(within) 100%) next to uncapped ones; D5 finding 5 says never cap. D3's "floor + half of the excess" row at an 80% floor share ($143k/$186k/$245k) matches D5's a = 0.8, s = 0.5 row exactly. | Compatible if a capped rule is reported with D3's "P(top reached)" (about 20%), never with "P(within) = 100%". D5's preference for no cap stands as the simpler honest statement; the team chooses. |

**Status after audit.** Finding 1 (hidden contradiction between "promise the upside" and "keep flexibility") stands:
it is the most useful new result in the cluster. Findings 2 and 5 reproduce (5 stands). Finding 3: direction stands
("lead with what is bought"); the Kresge "backstopped" link is withdrawn and the "counts" claim is INT (C2, C3).
Finding 4 stands with C8. Finding 6 is parked to the later list (C1). Finding 7 stands and is the part that goes
forward. Finding 8 stands (Brunel is not a benchmark). Candidate a = 0.7 / s = 0.5 survives as a team choice and is
compatible with D6 once the width is measured by s(1 - a) (C5).
