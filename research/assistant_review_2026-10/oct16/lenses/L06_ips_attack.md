# L06: IPS attack (IPS Version 5 against the official brief, the criteria and a professional IPS)

Fri 16 Oct 2026 (Sydney). AI-generated analysis (Claude) for Team Caplet. It is knowledge, not text to submit. It
contains no IPS wording, no pitch and no reflections: every fix says what the students' own version must achieve. If
the team uses it, record that in the Final Report's Works Cited.

Basis: main repo at 2affd4c (read-only) plus branch copy `caplet-latest/` (commit 412e9e3, 16 Oct). Web pages
accessed 16 Oct 2026. MODEL = a model output, not a fact. UNVERIFIED = could not confirm.

Scripts and outputs for this lens: `oct16/L06/` (`wc.py` word counts, `fit.py` page fit with Liberation Serif, which
has the same widths as Times New Roman; `L06_bonds.py` bond-sizing check; `cfa_ips.txt` saved CFA text).
LibreOffice would not open files in this sandbox, so page fit is computed from font widths, not from a rendered PDF.

---

## 0. Bottom line

1. **V5 passes the format gate, just.** My recount: pitch 47 words (50 if hyphenated words split), IPS 497 (505).
   It fits 41 of 46 double-spaced lines on Letter paper and 41 of 50 on A4. A blank line between paragraphs makes it
   48 lines, which spills to a 4th page on Letter. Nothing else in the format rules fails, except that the title
   page still has to be copied exactly from the roster and the WInS login.
2. **V5 cannot be the base text.** A student's own Doc comment says it is AI-generated (`01_version_5.md:36`). The
   16 Oct `[AI]` suggestion rule does not change this. The IPS bans citations, so any AI wording in it is undisclosed
   on the day it is judged (IPS brief :123-125). The students write a fresh version. This lens says what that
   version must contain and avoid.
3. **The biggest content flaw is now a rule flaw, not a wording flaw.** On the team's own 16 Oct model, V5's rules
   pay the facility floor in full in every path, keep the gift inside the range in 99.4% of paths, but leave a later
   operating payment short in about 6-7% of paths (MODEL). The case says the range "must also protect the
   portfolio's ability to fund the ten-year operating commitment" (case :119-120). The students' IPS must fix the
   priority order through 2042, not only in 2033.
4. **"High degree of certainty" is still undefined and untested** (case :97-99). V5 says "high certainty" once and
   never says what it means or how it was checked. The 30 Sep draft had a definition and a since-2000 test; V5
   dropped both.
5. **Nine plain questions about the 2031 and 2033 rules have no answer in V5** (section 4). After 6 Nov the Final
   Report must compute from these rules and may not change them (IPS brief :73-74).
6. **V5 lacks most of a professional IPS.** It has no return objective, no allocation or ranges, no stated
   rebalancing policy, no liquidity statement, no eligible-securities constraint, no measurable review triggers and
   no "who does what". These cost few words: the payments need about 5.1% a year on $300k (MODEL, section 6).
7. **V5 hides its strategy.** It names its approach only after 165 of 497 words. About 40-65 words restate case
   facts. Wharton's own guidance warns against both (section 10).
8. **Number conflict, resolved for the IPS.** $294,453 (number sheet) and $298,624-$298,628 (lenses) use the same
   15 Oct curve and the same ten payments. The gap comes from the dates priced to (payment dates against the
   maturities Caplet actually holds), plus forward against unchanged yields. For any claim about Caplet's plan, use
   the holdings basis. Better still, put no ladder figure in the IPS at all (section 6.2).
9. **The 16 Oct `[AI]` suggestion list would add errors** if accepted: a new false absolute (#2), a floor described
   as "normally $150,000" that is below $150k in 35-45% of modelled paths (#6), a disclosed $21k shortfall with no
   owner (#10), and a range plus "99 times in 100" that the brief does not ask for and that make the inversion in
   point 3 visible in writing (#11-12) (section 9).

---

## 1. What I checked

- Official: `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` (IPS brief), `Laura_Gao_2026_Client_Profile.txt`
  (case), `2026_WGY_Investment_Competition_Guide.txt`, `smapply_public_2026-10-14/deliverables.txt` and `faqs.txt`;
  live SMApply FAQ (re-fetched 16 Oct).
- Team: `team/google_drive/ips_report/01_version_5.md` (V5), `05_trading_note_reflection_wins_trading_notes.md`
  (the 11 filled notes), `COMPETITION.md`, `rab/decisions/D_ips_edit_ledger.md`.
- New commit: `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md`, `results.json`, `ips_numbers.py`,
  `IPS_v5_suggestions.md`; `caplet-latest/CLAUDE.md:27-30`; `caplet-latest/COMPETITION.md:141-143`.
- Professional benchmark: CFA Institute, *Elements of an Investment Policy Statement for Individual Investors* (May
  2010), https://rpc.cfainstitute.org/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
  (accessed 16 Oct 2026; text saved in `oct16/L06/cfa_ips.txt`).
- What wins: `oct16/research/KB_what_wins.md` (its UNVERIFIED items stay UNVERIFIED). I re-opened three Wharton
  quotes myself (section 10).
- Prior reviews (not repeated unless re-verified): `oct14/final.md` section 7, `oct14/ips_merge.md`; sibling lenses
  L01-L05, L08-L10.

---

## 2. Format gate audit (IPS brief :82-125; "Submissions that do not meet the requirements below will not be considered for semifinal selection", :82-83)

| Rule (exact source) | V5 status | Evidence | What the final must do |
|---|---|---|---|
| Title page, 1 page max (:84-85) | Pass if alone on page 1 | V5:6-12 | Page break after the username line |
| "Official team name ... same as what you submitted with your official team roster" (:88-90) | UNVERIFIED | V5:8 "Caplet"; COMPETITION.md:117 says Caplet; the roster record is not in the repo | Copy from the SMApply roster record, not from memory |
| "Finalized team member names ... Format: First Name, Last Initial" (:92-96) | Format matches the sample ("Jordan A." :130) | V5:10 | Same spellings as the roster (legal vs preferred first names UNVERIFIED) |
| "WInS username" (:98-100) | Placeholder in export | V5:12 "[removed]" | Copy from the WInS login; two students check |
| Pages 2-3, 2-page max (:103-105) | Pass: 41 of 46 lines (Letter), 41 of 50 (A4) | `oct16/L06/fit.py` | With a blank line between the 9 blocks: 48 lines, so 2 lines onto page 4 on Letter. No blank lines, or use A4 (paper size is not specified) |
| Pitch max 50 words (:33, :107) | 47 by spaces; 50 with hyphens split | `oct16/L06/wc.py` | 45 or fewer on the higher count |
| IPS max 500 words (:39, :109) | 497 by spaces; 505 with hyphens split | `wc.py` | 470 or fewer on the higher count, headings included |
| TNR 12, double-spaced, 1-inch margins (:112-118) | Not checkable from Markdown | - | Check the fonts embedded in the exported PDF |
| PDF via SurveyMonkey Apply, 5 MB max (:120-122) | - | - | Export from a one-tab Doc; check the size |
| No graphics, charts, images, attachments, links, footnotes, formal citations (:123) | Pass | V5 has none | Also no tickers as evidence, no "according to [source]" (section 11, IPS-19) |
| Headings | The official sample itself shows "Investment Strategy Elevator Pitch" and "Investment Policy Statement" (:135, :139) | V5:14, :18 match | Keep those two headings word for word. Whether they count toward 50/500 is UNVERIFIED, so count them |
| File name | The brief sets no naming rule (searched: "name" appears only for team and member names) | IPS brief | Choose a name with no personal data; the SMApply field may say more (UNVERIFIED) |

Word counts by paragraph (spaces / hyphens split): P1 98/100, P2 67/67, P3 112/116, P4 87/87, P5 52/52, P6 81/83.
26 sentences, average 19.1 words, longest 29 (V5:20.3).

---

## 3. Coverage maps

### 3.1 The official brief's own checklist

The brief says the IPS "should also establish your strategic approach to" four things (:48-50), and should "make it
clear" five things (:53-65). It also asks for the approach to "risk and return, liquidity, portfolio construction and
diversification, and planned changes" (:45-47).

| Official item | Where V5 handles it | Grade | Gap the students' version must close |
|---|---|---|---|
| Preparing for the operating commitment (:48) | V5:20.3, 24.2-24.3 | Good | Re-date or drop the cost figure |
| Managing the operating reserve's asset composition over time (:49) | V5:26.3 ("shrinking as each payment is made") | Thin | Say whether the composition changes, and why not; where maturing money and coupons wait (in a permitted asset) until each 1 January |
| Determining a responsible facility contribution (:49) | V5:30.2 (a formula) | Thin | A stated test of "responsible": why this share, what Laura keeps in a bad case |
| Preserving appropriate financial flexibility (:50) | V5:30.4 ("cushion") | Thin | What flexibility is for, its rough size, its priority against the payments |
| Risk and return (:46) | Risk V5:22.x; return never stated ("return" appears once, as a verb, V5:24.4) | Half | One return objective and one return assumption |
| Liquidity (:46) | Absent (0 uses) | Missing | When cash is needed (each 1 Jan from 2033) and how it is there |
| Diversification (:46) | V5:24.6 (one-issuer concession) | Thin | Why the payment money deliberately holds one issuer and where diversification sits |
| Planned changes as needs approach (:47, :22-23) | V5:26.1-26.3 | Thin | The allocation at each stage, and why the stock fund is not cut before 2033 |
| Protect payments while supporting the contribution (:64-65) | V5:26.4, 28.1 | Contradicted by the team's model | See IPS-02 |

Key-word count, official brief vs V5 (my count; `wc.py`):

| Word stem | IPS brief | Case | V5 pitch + body |
|---|---|---|---|
| flexib- | 6 (:10, 20, 25, 50, 59, 77) | 5 | **0** |
| responsib- | 3 (:25, 49, 64) | 4 | **0** |
| liquidity | 4 (:10, 20, 46, 59) | 1 | **0** |
| diversif- | 1 (:46) | 0 | **0** (also scored: "uses appropriate diversification", deliverables.txt:55) |
| inflation | 0 | (case :147) | 1 |

Words are not marks. But a reader with a checklist looks for these ideas, and V5 never names three of the brief's
central ones.

### 3.2 Professional IPS elements (CFA Institute 2010) against V5

The official brief opens: an IPS "outlines an investor's financial goals, risk tolerance, and guidelines for managing a
portfolio" (:3-4). The SMApply FAQ says the IPS should "Define your client's investment objectives, risk tolerance,
and overall investment strategy" (faqs.txt:74). The CFA paper lists the parts a professional IPS has.

| CFA element (section) | Fits Laura? | V5 | What the students' version needs (in principle, few words) |
|---|---|---|---|
| Governance: who sets, carries out and monitors the policy; how the IPS is reviewed (2a-2b) | Yes, briefly | "Each January we review it with Laura" (V5:26.2) | Who decides what (Laura approves goals and the 2031 quote; the team manages). The CFA example: review "no less frequently than annually" |
| Overall objective; return, distribution and risk requirements (3a-3b) | Yes: the core | Objectives stated (V5:20.2, 20.4); no return requirement | The return the payments need (about 5.1% a year on $300k; section 6) and that Treasuries bought now lock about that |
| Risk tolerance (3c). CFA: "account for known liabilities to lend some quantitative basis to the risk tolerance assessment" | Yes | Ability vs willingness (V5:22) but based on a degree and an inference | Base it on case :68-74 and the fixed liability; state what loss is unacceptable (a missed payment; a broken quote) |
| Constraints (3d): time horizon, liquidity, tax, legal | Yes, one line | Horizon implied; no liquidity, tax or legal | Stages (2027, 2028, 2031, 2033-42); cash each 1 Jan; taxes ignored by the case (:168-169); eligible securities only (FAQ, IPS-14) |
| Policy portfolio: targets "with allowable ranges around the targets" (3b) | Yes, as shares | None | The rough mix at each stage, with a range for the one asset that drifts (stocks) |
| Rebalancing (4c): "If the policy is not to rebalance, this policy should be documented in the IPS." | Yes: Caplet's policy is not to rebalance | "held without trading" (V5:26.1) contradicts the 2028 purchase and the coupon rule | State the no-rebalancing policy and why, and the only trades it allows (2028 purchase, waiting cash, substitution) |
| Performance measurement, risk metrics (4a-4b) | Yes | None measurable | Two or three yearly checks (ladder delivery vs $500k at current yields; floor holding vs quote; stock fund vs top), each with what it triggers |

---

## 4. Rule-ambiguity test: questions a judge (or the Final Report author) cannot answer from V5

Each rule binds after 6 Nov (IPS brief :73-74; Guide :60-61). The Final Report must compute ranges, confidence and
flexibility from these rules (case :117-120; IPS brief :68-70).

| # | Question | Why V5 cannot answer it | Evidence |
|---|---|---|---|
| Q1 | How big is the floor? | "sized to return that remainder" (V5:24.4). The remainder is $150k less any ladder top-up, so the floor is unknown until Jan 2028. The number sheet calls it "$150,000 face", yet its own model has the floor below $150k in 35.2% of paths | V5:24.3-24.4; `IPS_number_sheet.md:14`; `results.json:115` |
| Q2 | What is the 2031 bottom? | "the floor, quoted rounded down after any expected shortfall" (V5:30.1). Expected by what method, on what date, and why does a payment shortfall cut the floor when V5:26.4 says shortfalls are paid from other money first? | V5:26.4 vs V5:30.1 |
| Q3 | On which day in 2031 is "the equity fund's value then" measured, and can the top be re-quoted to later co-sponsors? | No date and no re-quote rule; the case says she will "begin approaching" co-sponsors in 2031 | V5:30.1; case :109 |
| Q4 | In 2033, is "the floor" the holding's actual payout or the quoted figure? | Both are called "the floor" | V5:28.1, 30.2 |
| Q5 | "Half the fund's value": half of the whole stock fund, or half of what is left after the shortfall chain has used "the half Laura keeps"? | The same half is named as the first payment backstop and as Laura's cushion | V5:26.4, 30.2, 30.4 |
| Q6 | What covers a payment shortfall that appears after the 2033 gift? | The order applies to a shortfall "expected in 2033" only; most reinvestment happens after 2033 (sibling STRAT-03: about 72%, MODEL) | V5:26.4 |
| Q7 | Where does the 2027 leftover sit, and how big is it? | Named as the first buffer, never placed or sized. On the holdings basis it is about $1.4k on the 15 Oct curve (section 6) | V5:26.4 |
| Q8 | Where do coupons and early maturities wait? | "income reinvested in the holding that paid it" (V5:26.1), but the trade notes say proceeds wait "in a short-term Treasury ETF" | V5:26.1; notes `05_...md:16-17` |
| Q9 | What happens if the ladder costs more than $300k on 1 Jan 2027, or the 2028 deposit is late or smaller? | Only the first is covered (V5:24.3), with no rule for the year between | V5:24.3; case :43-45 |

What a fix must achieve: each question has one answer in the students' IPS, as a rule a stranger could apply. The
numbers stay in the Final Report.

---

## 5. "High degree of certainty": define, test, rank

The case requires teams to "define what they consider a high degree of funding certainty, explain how they evaluated
that level of certainty, and identify the assumptions supporting their recommendation" (case :97-99). V5:20.2 says
"with high certainty" and gives no standard and no test.

What the team's 16 Oct model shows (MODEL; `caplet-latest/research/ips_numbers_2026-10/results.json`; 200,000 paths;
parallel rate moves; payment-date cost anchor):

| Measure | Value | Line |
|---|---|---|
| Ladder delivers at least about $500k if yields stay put | $500,000 | `IPS_number_sheet.md:32` |
| If yields fall 2 points and stay there | $478,793 (about $21k short) | `results.json` stress block; sheet :34 |
| Chance a ladder shortfall exceeds $1,000 | 47.1% | `results.json` `ladder_shortfall` |
| 1-in-20 shortfall | $25,476 | same |
| A payment needs more than the leftover plus Laura's half | 7.08% | `results.json:146` |
| A post-2033 shortfall exceeds what Laura kept | 6.3% (median uncovered $3,150) | `results.json:138` |
| The floor holding pays below the quoted bottom | 0.0% | `results.json:133` |
| 2033 gift inside the 2031 range | 99.41% | `results.json:130` |
| Laura keeps in 2033, 5th percentile | $0 | `results.json:147` |

Reading (my inference): under V5's rules the co-sponsor quote is more certain than the operating payments, and in a
bad case Laura keeps nothing while the gift is paid in full. That reverses the case's order: payments with "a high
degree of certainty" (case :91), the range "must also protect" them (:119-120), and committing everything "could
limit her financial flexibility" (:102-103). The number sheet itself lists three fixes, each a rule rather than a
trade: state the risk, keep Laura's half to 2042, or hold a $10-20k buffer from the 2028 deposit (sheet :49-54).
Sibling STRAT-04 adds a fourth: buy the ladder so it needs less reinvestment.

What the students' IPS must contain on certainty (no wording here):
- the standard (the payments are bought in advance with Treasuries held to maturity, not left to expected returns);
- the test (one named test, run on the WInS-listed holdings) and its key assumption (reinvestment yields);
- the risks that remain, named: US default; iBond ETF payouts not fixed; coupon reinvestment; waiting cash; yields
  falling before 1 Jan 2027; the 2028 deposit;
- which money absorbs each, in order, through 2042, with every payment ranked above every facility dollar,
  including the floor, or an explicit, defended exception.

---

## 6. Numbers audit

### 6.1 Every number in V5

| V5 figure | Status | Evidence |
|---|---|---|
| $300,000 Jan 2027; $150,000 Jan 2028 | Correct ("beginning of 2027/2028") | case :43-45 |
| Ten $50,000 payments, each January 2033-2042 | Correct | case :88-90 |
| "about $292,000" at "late-September 2026 yields" (pitch and V5:24.3) | **Stale and on a superseded basis**: the 25 Sep idealised value ($292,264). On the 15 Oct curve: $294,461 on the payment-date basis; $298,628 on the basis of the holdings Caplet owns | CLAUDE.md Key facts; section 6.2 |
| "a 2032 Treasury ETF" | Correct (IBTM, iBonds Dec 2032) | COMPETITION.md:176 |
| "thousands of companies" | Safe (the VT note says "about 10,000 stocks") | `05_...md:14` |
| "half" | A rule, not a fact; no stated reason | V5:30.1-30.4 |

Return objective (my calculation, MODEL): $300,000 on 1 Jan 2027 funds ten $50,000 payments 6-15 years later only if
it earns **5.09% a year**. At the 15 Oct holdings-basis cost ($298,628) the ladder locks in about **5.13%**; at the
payment-date cost ($294,461), 5.28%. This is the cleanest one-line return objective available: the payments need
roughly what Treasuries pay today, so no growth asset is needed for them. Re-compute in the week of 6 Nov if used.

### 6.2 The ladder-cost conflict: $294k vs $298.6k

| | Forward value at 1 Jan 2027 | 15 Oct curve held unchanged to 1 Jan 2027 |
|---|---|---|
| Priced to payment dates (1 Jan 2033-42) | $294,461 (room $5,539): the number sheet's $294,453 | $295,246 |
| Priced to the maturities Caplet holds (iBonds 15 Dec 2032-36; Feb-2037, May-2038, Nov-2039/40/41) | $297,847 (room $2,153) | **$298,628 (room $1,372, 4.7bp)**: the lenses' figure |

Source: `oct16/research/KB_verify/num/reconcile.py` (KB section 7.1). The number sheet prices to `dt.date(y, 1, 1)`
(`ips_numbers.py:87`); the lens pricer prices to the holdings' maturities (`oct14/factcheck/ladder.py`, list `BUY`).
Same curve date, same ten $50,000 payments, same bootstrap. The difference is the dates (Caplet's bonds mature 0.5 to
10.5 months early, so each $50,000 must exist earlier) plus the curve basis.

My extra check (`oct16/L06/L06_bonds.py`): with coupons reinvested at each bond's own yield, the five WInS T-bond
positions deliver $33,151 to $35,306 at their own maturity against the $33,333 WInS-scale payment. So the book was
sized to have each payment by maturity, roughly the holdings basis. The 6 Oct "executable" $293,447
(`ops/routines/MONITOR.md:22`) and the IBTR note's "about 0.2 percentage points" (22.7bp) were on that basis too. A
fourth figure, $295,924 (`results.json`, `ladder_cost_1jan2027_today_curve`), is the model's own par-as-zero cost.
Its leftover is $4,076.

Which figure for which IPS claim:
- "The first deposit buys all ten payments" and "the 2027 leftover is the first buffer": holdings basis. On 15 Oct
  that is barely true ($1,372). The sheet's chance of over $300k (35.2%, `results.json`) is anchored to $294,453
  (`ips_numbers.py:122`), so it is too low for the real holdings (siblings estimate about 44%, MODEL, not re-run here).
- "An ideal ladder costs about $294k": true, but Caplet does not own it. Do not use it for Caplet's claims.
- **In the IPS itself: preferably no ladder figure.** The brief asks for the framework "rather than ... presenting
  detailed financial calculations" (:51-52). The figure will move again before 6 Nov and again before 4 Dec. A rule
  (if the payments cost more than $300k, the 2028 deposit completes them first and the floor shrinks by the same
  amount) stays true. If a figure is kept: one, dated, holdings basis, identical in the TNA and the Final Report.

---

## 7. IPS vs the uneditable trade notes (the TNA quotes these word for word; the three documents are read together, case :161)

| Topic | Trade note (filled orders) | V5 | Conflict? |
|---|---|---|---|
| Floor certainty | IBTM: "although the final payout is not fixed" (`05_...md:19`) | "never below the floor" (V5:28.1); "cannot miss the range" (V5:30.2) | Yes |
| What stocks do | VT: "They only set how far her gift rises above her promised minimum" (`:14`) | Laura's half also backs payments (V5:26.4) and defends against inflation/TWD (V5:28.3) | Yes ("only") |
| First deposit covers all ten | IBTR: "her first $300,000 is enough ... If yields fall more than about 0.2 percentage points" (`:15`) | "if falling yields push that above $300,000 ... the 2028 deposit completes them" (V5:24.3) | Consistent in logic; the threshold is now about 0.05 points (holdings basis) |
| Where maturing money waits | Feb-2037 / May-2038: "proceeds held in a short-term Treasury ETF" (`:16-17`) | "income reinvested in the holding that paid it" (V5:26.1) | Yes |
| Coupons | Nov-2039 / Nov-2041: "reinvested coupons fund the rest" (`:18`, `:24`) | "depends mainly on the US government" (V5:20.3) | Partly |
| Scale | Notes say "$50,000 payment" while WInS holds about $33k per payment | "Our WInS portfolio shows this allocation, scaled down" (V5:26.5), with no date or scale | Unclear: WInS mirrors the post-2028 plan at about two-thirds; the 30 Sep draft said "after both deposits" (`D_ips_edit_ledger.md` L9) |
| Stock share | WInS VT about 8.8% (167 x $158.83 / about $301.9k; COMPETITION.md:186-188) | Plan about 6.9% in Jan 2028 (`results.json:155`) | A 2-point gap to explain or accept |

What a fix must achieve: the IPS describes the floor, the role of stocks, the waiting cash and the WInS scale exactly
as the picked notes do, or the reflections explain the difference. Settle the words before the TNA reflections are
written (TNA due Sat 24 Oct 08:00 Sydney).

---

## 8. Sentence audit (flags only; the students write their own sentences)

| V5 ref | Flag | Why it costs marks |
|---|---|---|
| 20.1 (27w) | Case restatement | Repeats case :43-45, :76; Wharton: "Don't use precious space repeating known facts about your client" |
| 20.3 | Jargon + overclaim | "defined-maturity Treasury ETF" is never explained; "depends mainly on the US government" ignores reinvestment |
| 22.3 | Unsupported | A degree is not evidence of risk appetite; "the artists would bear the loss" is an inference |
| 22.4 | Unsupported judgement | "above average" with no basis, while the plan holds about 7% stocks |
| 24.1 | Metaphor stacking, two meanings | "roots" = payments + floor here; in the pitch the roots "cover ten $50,000 payments" and "further Treasuries" secure the minimum |
| 24.2 | Jargon | "rate-sensitive" is undefined |
| 24.6 | AI pattern (concede-then-dismiss) + absolute | "may look like a weakness, but we accept it, since no dollar asset is safer" |
| 26.1 | Contradiction | "held without trading" vs the 2028 purchase, the coupon rule and the substitution rule |
| 26.2 | Untestable trigger | "acting only if her goals change": no measure |
| 26.4 | Ambiguous scope | "expected in 2033" (Q6) |
| 28.1 | Absolute, false by own numbers | "never below the floor" (IBTM payout not fixed) |
| 28.2 | Wrong | "would raise the expected contribution": under the plan's own rule a smaller floor lowers the median gift (15 Oct brief, MODEL) |
| 28.3 | Unsupported + double use | "is her defense": the same half already backs the payments |
| 30.2 | Absolute, false by own numbers | "cannot miss the range" (99.4% in the team's model) |
| 30.3 | AI pattern (stated preference + comparison) | "We prefer a range built to hold, since missing a narrower one would harm her credibility more" |

Term drift (count in V5): the stock fund has 5 names ("global index fund", "branch", "equities", "the equity half",
"the equity fund"); the floor has 4 ("floor", "facility floor", "minimum contribution", "a number Laura has quoted");
the gift has 3 ("gift", "facility contribution", "contribution above the floor"). The case says "high degree of
funding certainty"; V5 says "high certainty".

---

## 9. The 16 Oct `[AI]` suggestions (`caplet-latest/research/ips_numbers_2026-10/IPS_v5_suggestions.md`)

Judged against the IPS brief, the case and the criteria (not against word count). I give no replacement wording.

| # | Effect | Verdict | Evidence |
|---|---|---|---|
| 1, 3, 4 | Word trims | Harmless in content, but AI wording | file :9, :11, :12 |
| 2 | Changes "mainly" to "only", for principal | **Adds a false absolute**: 5 of 10 rungs are iBond ETFs whose payout "is not fixed" (note `05_...md:19`); iShares: an iBond ETF "does not seek to return any predetermined amount" (quoted in `IPS_number_sheet.md:72-73`) | :10 |
| 5 | Re-dates the cost to $294,000 | **Wrong basis** for Caplet's holdings (section 6.2) | :13 |
| 6 | "normally $150,000" | The floor is below $150k in 35.2% of the model's own paths (`results.json:115`), and more often on the holdings basis; "normally" overstates it | :14 |
| 7 | Adds $32,000 and the mix | Matches the sheet (VT p50 $32,296; 6.9%), but adds two figures that will change before 6 Nov | :15 |
| 8 | Cuts the one-issuer sentence | Removes V5's only diversification argument (criterion: "appropriate diversification", deliverables.txt:55) | :16 |
| 9 | Cuts the review rule | Removes the only monitoring and substitution rule (CFA 2b, 4a) | :17 |
| 10 | Discloses about $21,000 short at -2 points; keeps "not below the floor" | Says the payments can be short while the floor is protected, with no owner for the gap: the inversion of section 5, now in writing | :18 |
| 11 | Adds "$145,000 to $168,000 today" | The brief says the IPS "is not expected to include ... a final facility-contribution range" (:68-70); the figure will differ by 4 Dec | :19 |
| 12 | Adds "about 99 times in 100" | Quotes range confidence with no payment confidence beside it (payments: about 93 in 100 covered by the chain, sheet :46-48) | :20 |
| 13 | Drops "if costs rise" | Removes the cushion's cost-overrun job, which the case raises (:103, :147) | :21 |

Also: the file's header says "494 after all twelve" (:5) but lists 13 suggestions. Overall the commit does not change
my conclusions. It sharpens two: the payment-vs-range inversion now has the team's own figures, and the number
conflict is now in a file that proposes IPS text.

---

## 10. What judges and past evidence emphasise vs V5

No winning IPS or final report is public ("We do not release final reports from previous winners", KB [D8]).
So the comparison is with what Wharton and judges say they want.

| Evidence (re-opened 16 Oct unless marked) | V5 against it |
|---|---|
| "if you provide us with a team strategy that is buried somewhere ... rather than clearly stated, defined and articulated up front, you will not be among the strongest teams" (https://globalyouth.wharton.upenn.edu/developing-strategy/) | The approach is named at word 166 of 497 (V5:24.1), after 165 words of restatement and risk profile |
| "Your strategy is a set of rules and guidelines; a plan of attack." (https://globalyouth.wharton.upenn.edu/wp-content/uploads/2023/11/Technical-Feedback-23-24.pdf) | V5 has rules, but 9 of them are ambiguous (section 4) |
| "Excessive investing jargon doesn't necessarily dazzle the judges." / "Don't use precious space repeating known facts about your client and defining concepts." (https://globalyouth.wharton.upenn.edu/wp-json/wp/v2/pages/3778, 2022-24 judging page) | About 40-65 words restate case facts (V5:20.1 27 words; part of 20.2; the opening clause of 22.1); jargon left unexplained (section 8) |
| "successful teams communicate their reasoning, assumptions, tradeoffs" (faqs.txt:83); "the reasoning, assumptions, and tradeoffs behind those decisions" (Guide :183-184) | One trade-off sentence, and it is wrong (V5:28.2); no assumptions stated |
| "an authentic team voice" (deliverables.txt:59); 2025-26 semifinal: "not generated or generic responses" (KB [D1]) | Doc comment: "Best version that AI generated" (V5:36) |
| "simple, elegant ideas" (2025 semifinal judge, KB [N12]); "less is more" (2023 champions, KB [N7]) | The core idea is simple; the page buries it under metaphors and restatement |
| Bond specialists on finale panels 2024-26 (KB 2.2) | Coupon reinvestment, the iBond payout and the maturity gaps are where a bond reader will press; V5 glosses all three |

---

## 11. Findings

Severity: critical = likely blocks a Top-50 place; high = materially lowers the score; medium = noticeable; low =
polish. "Known" refers to the 15 Oct brief (`oct14/final.md`, `oct14/ips_merge.md`).

### IPS-01 (critical, known-deeper). V5 is AI-generated; the 16 Oct [AI] rule does not make AI wording usable in the IPS
- **Problem.** The team's own comment calls V5 "Best version that AI generated" (V5:36). The new rule lets the AI put
  `[AI]` suggestions into the IPS Doc (`caplet-latest/CLAUDE.md:27-30`). But the IPS allows no citations
  (IPS brief :123-125), so accepted AI wording would sit undisclosed in a judged document until the 4 Dec Works
  Cited. Wharton: AI work may not be submitted as the students' own; students "must use their voice and words" (KB
  [W5]). Creativity scores "an authentic team voice" (deliverables.txt:59).
- **Fix.** The students write a fresh IPS from their own decision outline, with V5 and the suggestion list closed.
  AI is used only for fact and number checks and format counts. Each paragraph has a student author who can defend it
  aloud.
- **Deadline.** Outline by Tue 27 Oct; student draft by Sat 31 Oct; submit Thu 5 Nov (Sydney).

### IPS-02 (critical, known-deeper). V5's rules protect the floor and the range ahead of the operating payments
- **Problem.** V5:26.4 pays a shortfall from the leftover, then Laura's half, then the gift above the floor. It
  never touches the floor and only acts in 2033. The team's 16 Oct model: floor below the quote 0.0% of paths, gift
  in range 99.41%, a payment needing more than the leftover plus Laura's half 7.08%, post-2033 shortfall beyond what
  she kept 6.3%, Laura keeps $0 at the 5th percentile (`results.json:130-147`). The case puts payments first
  (:91), says the range "must also protect" them (:119-120) and warns against committing everything (:102-103).
- **Fix.** Before 6 Nov the team chooses one rule (sheet :49-54, or a less reinvestment-dependent ladder) so payment
  certainty is at least as high as range certainty. The IPS states the order of protection through 2042 as a
  principle. No range confidence is quoted anywhere without the payment confidence beside it.
- **Deadline.** Vote set B, Tue 27 Oct (the floor wording feeds the TNA, so settle the floor description by Sun 18 Oct).

### IPS-03 (high, known-deeper). "High degree of certainty" has no definition, no test and no assumptions; V5 dropped the earlier ones
- **Problem.** The case requires all three (:97-99). V5 has two words, "high certainty" (V5:20.2). The 30 Sep text had a
  definition sentence and "We tested this on every Treasury curve since 2000" (`rab/decisions/D_ips_edit_ledger.md`
  L1 and cuts table); V5 lost both. Under the WInS-only rule, reinvestment is real: a 1-in-20 shortfall of about $25k
  (MODEL).
- **Fix.** The IPS states a standard, one test on WInS-listed holdings with its key assumption, the remaining risks
  and who absorbs each (section 5). Detailed results go in the Final Report.
- **Deadline.** Vote set B, Tue 27 Oct.

### IPS-04 (high, known-deeper). Absolute words are false by the team's own numbers, and the [AI] list adds another
- **Problem.** "secure" (pitch), "depends mainly on the US government" (V5:20.3), "never below the floor" (V5:28.1),
  "cannot miss the range" (V5:30.2). The model puts the gift outside the range in 0.6% of paths; the IBTM note says
  the payout "is not fixed" (`05_...md:19`). COMPETITION.md:168 bans "risk-free" and "guaranteed", which mean the same.
  `[AI]` #2 adds "only" for principal, which is false for the five iBond rungs.
- **Fix.** Every certainty word is literally true on the WInS-listed holdings and matches the TNA. Where something is
  very likely but not certain, say so with a stated level or a stated condition.
- **Deadline.** Banned and allowed words agreed by Sun 18 Oct (before the TNA reflections).

### IPS-05 (high, new). Nine ambiguities in the floor, range, gift and shortfall rules
- **Problem.** Section 4: floor size (Q1), the 2031 bottom (Q2), valuation date and re-quote rule (Q3), "the floor"
  meaning two things (Q4), which "half" (Q5), post-2033 shortfalls (Q6), the leftover (Q7), waiting cash (Q8), a late or
  small 2028 deposit (Q9). The rules become binding on 6 Nov, and the Final Report must compute from them.
- **Fix.** Each question has exactly one answer in the IPS, written as a rule a stranger could apply. Test: a student
  who did not write that paragraph applies the rule to one made-up good market and one bad market and gets the same
  numbers as the author.
- **Deadline.** Rules decided at Vote set B (Tue 27 Oct); stranger test Sat 31 Oct.

### IPS-06 (high, new). Most elements of a professional IPS are missing, though each costs few words
- **Problem.** Against the CFA Institute's 2010 elements (section 3.2), V5 lacks a return requirement, targets "with
  allowable ranges", a stated rebalancing policy (CFA: "If the policy is not to rebalance, this policy should be
  documented in the IPS"), liquidity and legal constraints, measurable review metrics and who-does-what. The official
  brief defines an IPS as goals, risk tolerance and "guidelines for managing a portfolio" (:3-4); the FAQ adds
  "investment objectives" (faqs.txt:74).
- **Fix.** The students' version covers each element in principle: the return the payments need (about 5.1% a year,
  section 6.1); the mix at each stage; the no-rebalancing policy and the few trades it allows; liquidity each 1 Jan;
  eligible securities; two or three yearly checks with triggers; who decides.
- **Deadline.** In the outline, Tue 27 Oct.

### IPS-07 (high, known-deeper). Three of the brief's four required approaches are thin; four key words never appear
- **Problem.** The brief says the IPS should "establish" the approach to preparing for the commitment, managing the
  reserve's composition over time, a responsible contribution, and appropriate flexibility (:48-50). V5 covers the
  first well and the other three in one sentence each. "flexib-", "responsib-", "liquidity" and "diversif-" appear 6, 3,
  4 and 1 times in the brief and 0 times in V5 (section 3.1).
- **Fix.** Tick the students' draft against the 4 + 5 official items (section 3.1) and the scored word "diversification".
  Each is handled as a principle, in the students' words.
- **Deadline.** Check on Sat 31 Oct; second check Wed 4 Nov.

### IPS-08 (high, new). The strategy is not up front, and about a tenth of the IPS restates the case
- **Problem.** V5 names its approach at word 166 of 497 (V5:24.1). The first 27-word sentence (V5:20.1) and the
  opening clause of V5:22.1 restate case facts (case :43-45, :61-65, :76). Wharton: a strategy "buried somewhere ...
  rather than clearly stated, defined and articulated up front" will not be among the strongest; and "Don't use
  precious space repeating known facts about your client" (section 10, both re-opened 16 Oct). The brief's first
  question is "What is the central idea behind your investment strategy?" (:16).
- **Fix.** The central idea appears in the first two sentences of the IPS body. Case facts appear only where a rule
  needs them. Target: no more than 20 words of pure restatement.
- **Deadline.** Draft, Sat 31 Oct.

### IPS-09 (high, known-deeper). Laura's kept half has three jobs, and "responsible" is never tested
- **Problem.** The half is the first payment backstop (V5:26.4), the cushion for costs and co-sponsors (V5:30.4) and the
  inflation and Taiwan-dollar defence (V5:28.3). Model: median kept $27,860 against a median gift of $167,001 (about
  86% of the unreserved money given), and $0 kept at the 5th percentile (`results.json`). The case: committing all
  remaining assets "could limit her financial flexibility" (:102-103).
- **Fix.** One job list in priority order, one source for each job, and one stated test of "responsible" and
  "appropriate flexibility" (case :145) that holds in a bad case.
- **Deadline.** Vote set B, Tue 27 Oct.

### IPS-10 (high, known-deeper). The cost figure is stale and on the wrong basis; the leftover "first buffer" is nearly empty
- **Problem.** "$292,000" (pitch; V5:24.3) is the 25 Sep idealised value. On 15 Oct, Caplet's holdings cost about
  $298.6k, leaving about $1.4k (4.7bp) (section 6.2). The leftover is V5's first shortfall buffer (V5:26.4) against a
  1-in-20 shortfall of about $25k (MODEL). The sheet's $294k and its 35% are on the ideal-ladder basis.
- **Fix.** Prefer no ladder figure in the IPS (brief :51-52), only the rule for what happens if the ladder costs more than
  $300k. If a figure stays: one, dated, holdings basis, identical in all three documents. Do not name a buffer that may
  be about zero as the first line of defence.
- **Deadline.** Re-price in the week of 2-4 Nov if any figure is kept.

### IPS-11 (medium, new). Accepting the 16 Oct [AI] suggestions would add errors and remove scored content
- **Problem.** Section 9: #2 false absolute; #5 wrong basis; #6 "normally $150,000" against 35% of paths below; #8 and
  #9 delete the diversification and monitoring rules; #10 writes down a payment shortfall while keeping the floor
  protected; #11-12 add a range and a 99% figure the brief does not expect and that will differ by 4 Dec; #13 drops a
  case-relevant job. The header miscounts its own rows (twelve vs 13).
- **Fix.** If any item is used, judge it against the brief and the criteria first. Use facts and flags only; the students
  write the sentences (IPS-01).
- **Deadline.** Before the drafting session, Wed 28 Oct.

### IPS-12 (medium, known-deeper). Liquidity: V5's income rule cannot work as written, and waiting cash has no permitted home
- **Problem.** "income reinvested in the holding that paid it" (V5:26.1). WInS bonds trade in $1,000-face units
  (COMPETITION.md:181, "20 units ($20k face)"). The Feb-2037 bond's half-year coupon on that position is $475 (my
  arithmetic, 4.750%), too small to buy one unit, so cash must wait somewhere. The notes park proceeds in "a
  short-term Treasury ETF" (`05_...md:16-17`). The live FAQ's permitted list has stocks, ETFs and Treasury bonds, but
  not cash (FAQ, re-fetched 16 Oct). The word "liquidity" never appears.
- **Fix.** One liquidity principle: when cash is needed (each 1 Jan from 2033), where coupons and early maturities
  wait (a type of permitted asset, matching the notes), and that nothing needs selling before maturity.
- **Deadline.** Vote set B, Tue 27 Oct.

### IPS-13 (medium, known-deeper). The allocation path, the WInS scale and the no-de-risking choice are not stated
- **Problem.** The brief asks how "allocation and composition change as future funding needs approach" (:22-23). V5
  has no shares. Model shape: Jan 2027 about 98% payment Treasuries and 2% leftover; Jan 2028 about 67% payment
  Treasuries, 25% floor, 1% leftover, 7% stocks (`IPS_number_sheet.md:58-62`; `results.json:155`). WInS holds the
  post-2028 shape at about two-thirds scale, with VT at about 8.8%. V5:26.5 says only "scaled down". Why the stock fund
  is not cut before 2033 is not said.
- **Fix.** The rough mix at each stage (with a range for stocks); which date the WInS book mirrors; one principle on
  de-risking the stock fund before 2033.
- **Deadline.** Outline, Tue 27 Oct.

### IPS-14 (medium, new). The eligible-securities constraint now names the IPS; state it as the plan's legal constraint
- **Problem.** The live FAQ now reads "Investments permitted (for BOTH contributions, the IPS and Final Report)", which
  is stocks, ETFs and Government/Treasury bonds "available on WInS" (re-fetched 16 Oct; the 14 Oct repo copy,
  faqs.txt:42, lacks "the IPS and Final Report"). This is the binding constraint behind the iBond-ETF-plus-bonds
  design (the 6 Oct email removed zero-coupon STRIPS), but V5 never states it. Taxes: the case says teams "do not need
  to account for" them (:168-169).
- **Fix.** One constraint line: only WInS-listed stocks, ETFs and Treasury bonds; taxes excluded by the case. Never name
  cash, STRIPS or any non-listed instrument as part of Laura's plan.
- **Deadline.** Outline, Tue 27 Oct.

### IPS-15 (medium, known-deeper). The risk profile rests on a degree and an inference, not on the case and the liability
- **Problem.** "As a statistics graduate and entrepreneur she accepts measured risk", "the artists would bear the loss",
  "we judge her tolerance above average" (V5:22.3-22.4). The case's words are "willing to take thoughtful risks" and "an
  appropriate balance" (:69-73). CFA: use "known liabilities to lend some quantitative basis to the risk tolerance
  assessment". "Above average" sits beside a plan with about 7% stocks.
- **Fix.** Willingness from the case's words; ability from the case's facts (no withdrawals before 2033; living costs
  covered); the unacceptable outcomes named (a missed payment, a broken quote); why a small stock share still fits a
  risk-willing client (it is what is left after two promises are bought).
- **Deadline.** Draft, Sat 31 Oct.

### IPS-16 (medium, known-deeper). The pitch leads with an unsupported claim and a stale number and omits the credibility idea
- **Problem.** "co-sponsors who fund the building rarely pay to run it" is not in the case (the case says other sources
  "may" fund operations, :85-86). "$292,000" is stale (section 6). It uses "minimum contribution" and "gift", terms
  the body does not use. The brief asks the pitch to give "the central idea" and how it supports the client's goals
  and future funding needs (:35-36). The credible-range logic, the case's main co-sponsor worry (:114-116), is absent.
- **Fix.** The pitch states the central idea in Laura's terms, links to her payments and her credibility, has no
  dollar figure, uses the same terms as the body, and is 45 words or fewer.
- **Deadline.** Each student drafts one alone, Sat 31 Oct; the team chooses.

### IPS-17 (medium, known-deeper). Term drift and metaphor load
- **Problem.** 5 names for the stock fund, 4 for the floor, 3 for the gift; "roots" means payments only in the pitch but
  payments plus floor in V5:24.1; "high certainty" vs the case's "high degree of funding certainty"; jargon left
  unexplained (section 8). "Root-and-Branch" is also an English idiom for a complete overhaul (sibling UNIQ-14).
- **Fix.** One name per idea, defined at first use, identical in the TNA, IPS and Final Report. Keep the strategy name
  only if it explains the structure in one clause.
- **Deadline.** Name and terms by Sun 18 Oct (they appear in the TNA).

### IPS-18 (medium, known-deeper). The one trade-off sentence is wrong, and the real trade-off is missing
- **Problem.** V5:28.2 says moving floor money into stocks "would raise the expected contribution". Under the plan's
  own cap rule a smaller floor lowers the median gift; only total wealth rises (15 Oct brief, MODEL). The brief, the
  Guide and the FAQ all ask for trade-offs (Guide :183-184; faqs.txt:83).
- **Fix.** One true trade-off, stated once: what Laura gives up (expected growth) for what she gets (payments bought in
  advance, a quote she can keep), with the rejected alternative named.
- **Deadline.** Draft, Sat 31 Oct.

### IPS-19 (medium, new). Attribution and tickers: keep the IPS free of citations, sources and security-level detail
- **Problem.** The IPS bans "formal citations" and says sources "do not need to be cited" (:123-125). It should
  "Focus on the strategy ... rather than describing individual investments" (:51-52). The number sheet's return line
  names "J.P. Morgan 2026 long-term estimate" (`IPS_number_sheet.md:64-65`). Copying that into the IPS would amount
  to an in-text citation. V5 currently complies (no tickers, no sources).
- **Fix.** Assumptions are stated as the team's assumptions, with no named source. Sources go in the Final Report.
  No tickers or bond coupons in the IPS.
- **Deadline.** Format check, Wed 4 Nov.

### IPS-20 (medium, known-deeper). The monitoring rule has no measures and misses the two likeliest events
- **Problem.** "acting only if her goals change or a holding becomes unavailable" (V5:26.2). There is no number to check
  and no trigger for the ladder costing more than $300k on 1 Jan 2027 (about 44% on the holdings basis, sibling MODEL)
  or the 2028 deposit arriving late or small (case :43-45 says "will"; the plan leans on it).
- **Fix.** Two or three yearly checks, each with a stated consequence, including those two events. The rule must also
  fit the frozen WInS book (no trades after 6 Nov).
- **Deadline.** Vote set B, Tue 27 Oct.

### IPS-21 (low, known-repeat). Format margins and title page (re-verified)
- **Problem.** 47/50 and 497/505 words; 41 of 46 lines on Letter; a blank line between paragraphs spills to page 4 on
  Letter; team name and names to match the roster; username placeholder.
- **Fix.** Pitch 45 or fewer and IPS 470 or fewer on the higher count, headings included; no blank lines, or A4; title
  page copied from the roster record and the WInS login, checked by two students on the exported PDF.
- **Deadline.** Wed 4 Nov; submit Thu 5 Nov (Sydney).

### IPS-22 (low, new). The official sample shows the expected headings; there is no file-naming rule
- **Problem.** The brief's sample page uses exactly "Investment Strategy Elevator Pitch" and "Investment Policy
  Statement" (:135, :139), and its title page shows only the team name, the names and the username (:129-131). The
  brief has no file-name rule. Teams sometimes add extra headings or a long title, which eats words.
- **Fix.** Use the two official headings word for word; add other headings only if they earn their words (count them).
  Name the PDF with no personal data.
- **Deadline.** Wed 4 Nov.

---

## 12. Must contain / must avoid (prioritised)

**Must contain (in this priority order)**
1. Student authorship: fresh text, a named author per paragraph, every sentence defensible aloud (IPS-01).
2. A protection order through 2042 that ranks the payments above every facility dollar, or a defended exception
   (IPS-02).
3. The certainty standard, one test, its key assumption, the named remaining risks and who absorbs each (IPS-03).
4. The central idea in the first two sentences of the body (IPS-08).
5. One unambiguous answer to each of Q1-Q9 (IPS-05).
6. The approach to the reserve's composition over time, a responsible contribution and appropriate flexibility
   (IPS-07, IPS-09).
7. A return objective and one return assumption (IPS-06).
8. Liquidity: cash each 1 Jan, where coupons and early maturities wait (IPS-12).
9. The mix at each stage, the no-rebalancing policy, the de-risking choice and which date the WInS book mirrors
   (IPS-13).
10. Constraints in one line: horizon stages, eligible WInS-listed securities, taxes excluded (IPS-14).
11. Risk profile from the case's words and the fixed liability (IPS-15).
12. One true trade-off with the rejected alternative named (IPS-18).
13. Yearly checks with triggers, including ladder over $300k and the 2028 deposit (IPS-20).
14. Why the payment money holds one issuer and where diversification sits (IPS-07; criterion text).
15. The same terms and floor description as the TNA reflections (section 7; IPS-17).

**Must avoid**
1. Any AI-generated sentence, including accepted `[AI]` suggestions (IPS-01, IPS-11).
2. "never", "cannot", "secure", "guaranteed", "risk-free", "only" applied to anything the team's own numbers show can
   miss (IPS-04).
3. A range confidence without the payment confidence beside it (IPS-02).
4. Any ladder-cost figure not on the holdings basis or not dated; preferably none (IPS-10).
5. A final dollar range, a reserve calculation or the co-sponsor text (brief :68-70).
6. Case facts repeated for their own sake (IPS-08).
7. Unsupported claims about co-sponsors, Laura's psychology or her degree (IPS-15, IPS-16).
8. Undefined jargon ("defined-maturity", "rate-sensitive", "liability-driven", "immunisation") and more than one name
   per idea (IPS-17).
9. Naming sources, tickers or coupons (IPS-19).
10. Any rule that needs a WInS trade after 6 Nov, or that names cash, STRIPS or a non-listed instrument as part of
    Laura's plan (IPS-14, IPS-20).
11. Blank lines between paragraphs on Letter paper; extra headings that eat words (IPS-21, IPS-22).

---

## 13. Word budget (targets; higher of two counters; headings counted)

| Part | Words |
|---|---|
| Pitch: central idea | 15 |
| Pitch: payments link | 12 |
| Pitch: facility / credibility link | 12 |
| Pitch: strategy name (optional) | 3 |
| **Pitch total (cap 45)** | **42** |

| IPS section (time order) | Words |
|---|---|
| Heading "Investment Policy Statement" | 3 |
| 1. Central idea and objectives, incl. return objective | 70 |
| 2. Certainty: standard, test, remaining risks, who absorbs (through 2042) | 60 |
| 3. Laura's ability and willingness to take risk | 45 |
| 4. Constraints line (horizon stages, liquidity, eligible securities, taxes) | 30 |
| 5. 2027 build; where coupons and early maturities wait | 45 |
| 6. 2028: completion rule, floor-size rule, stock fund and diversification | 60 |
| 7. Hold policy (no rebalancing) and yearly checks with triggers | 45 |
| 8. 2031 range rule (date, bottom, top, re-quote, how confidence is judged) | 45 |
| 9. 2033: reserve path, gift, cap, cushion's job, "responsible" test | 42 |
| 10. Trade-off accepted; inflation and Taiwan dollar in proportion | 25 |
| **IPS total (cap 470)** | **470** |

Page check: V5 puts 544 words in 41 lines (about 14 words per full line, plus a part-line at the end of each of its 9
blocks). 512 words in 12 blocks comes to about 40-43 of 46 lines on Letter. Keep blank lines out and re-check on the PDF.

---

## 14. UNVERIFIED

- How Wharton counts words, and whether the two official headings count.
- The exact team name and name spellings on the submitted roster; the WInS username (not printed here).
- Whether the SMApply IPS upload field sets a file name or asks for anything else.
- Page fit on a rendered PDF (computed from font widths; LibreOffice would not run here).
- The sibling estimate of about 44% for the ladder costing more than $300k on the holdings basis (not re-run here).
- All model outputs from `results.json` (the team's 16 Oct model; I read them, I did not re-run the Monte Carlo).
- Who wrote V5's predecessors and Tab 15.
