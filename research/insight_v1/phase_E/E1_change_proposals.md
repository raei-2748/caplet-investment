# E1 Strategy Architect: change proposals to the "lock early" strategy (for team approval)

Agent E1 (Strategy Architect), insight_v1 run, Phase E. Written 2026-09-28 (the first official WInS trading day).
AI-generated research for Team Caplet: numbered change proposals, numbers, specifications and checklists. **None of it
is text to submit.** The six students decide every change and write every WInS note, reflection, pitch sentence and
IPS sentence in their own words; any AI use is recorded in the Final Report's Works Cited (Wharton AI policy, R-W46).
Laura appears only through the case and her public professional record; nothing here suggests contacting her (R-W16).

**Scope (brief section 17).** Only WInS trading now (as the source of the Trading Notes), the Trading Notes Analysis
(TN, Oct 23) and the IPS (Nov 6). Because the IPS freezes the strategy on Nov 6 and the Final Report must later apply
it without redesign (IPS guide L73-75; Guide p.5 L156-159, VRF), the proposals fix the **decision rules** the Final
Report will apply (reserve, 2031 range method, facility and flexibility, if-then rules), but give no Final Report
content, no dollar range and no fundraising text. Purely Final Report items are one line each in section 5.
**Relayed messages:** none arrived during this task.

**Status labels** (brief section 3): **VP** = VERIFIED-PRIMARY; **VRF** = VERIFIED-REPO-FILE; **SNIP** =
SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION (a modelling or judgement input); **MODEL** = an ASSUMPTION-based model output,
not a forecast; **INT** = E1's interpretation or judgement (an ASSUMPTION, never a fact about Laura). Ids: R- = case
register, F- = fact register, SH-/BS- = stakeholder map, M- = Phase C questions (all under `research/insight_v1/`).
Every security named is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (brief sections 4 and 14).

**New script (this file):** `.venv/bin/python research/insight_v1/scripts/E1_split_and_slices.py` (about 5 seconds;
docstring lists inputs and labels). It re-uses D6's engine and random stream and prints: [1] the sleeve-split test
across two forecasting houses, two bond assumptions and three fee levels; [2] which equity shares pass in every cell;
[3] the whole-portfolio stock share by stage; [4] the 2031 "three slices" at 50/50 and 60/40.

**Evidence read in full for this file:** brief; `phase_D/` D1-D12, D3_model_v2_results, D13a, D13c (sections 1-5),
D13b flags, all four audit files and every "Audit corrections" appendix (corrections override the text above them);
`wins_now/securities_and_allocation_v0.md` and `S4_red_team.md`; and, once they appeared in the repo during this task
(checkpoint commit 32e31ac), `phase_D/trading_now_brief.md` and `wins_now/securities_and_allocation_v1.md` (agent T1).
**The v1 ticket supersedes v0 for trading; where they differ, this file follows v1** ("the ticket" below means v1).
`T2_red_team.md` does not exist in the repo on 2026-09-28. `D3_quant.md` and `D3_model_v2_results.md` carry no audit
appendix yet (a D3 audit was in progress), so D3-only numbers below are pre-audit; the verified-base figures they
reproduce (F-401, F-402) are unaffected. Also read: `S2_growth_sleeve.md` summary; `phase_A/` case_register (R-C, R-I, R-T, R-S, R-AN), fact_register, stakeholder_map
(summary, BS-01 to BS-20, section 7), wins_week1_guardrails (summary); `phase_C/survivors.json` and the parked items
M007, M008, M015, M021, M033, M035, M040, M149; the council chair memo and round-2 referee ruling (history only); the
official case, IPS guide, TN guide and Competition Guide text files.

Terms used (defined once):
- **Ladder:** ten zero-coupon U.S. Treasury bonds (STRIPS), one maturing shortly before each $50,000 payment
  (2033-2042). **Rung:** one of those bonds.
- **Growth money (sleeve):** everything the ladder does not need (about $158k after the 2028 deposit).
- **Floor (2031):** the part of the growth money bought in January 2031 as a Treasury maturing before 1 January 2033,
  so its 2033 value is known in 2031.
- **Funded ratio:** money available divided by the market price of the ten payments on the same day.
- **p5 / p50 / p95:** in a simulation, the value 5% / 50% / 95% of paths fall below (p50 = median).
- **bp:** basis point, 0.01 percentage point.
- **Option (ii) / (iii):** the two candidate WInS books in the ticket: (ii) the plan's mix after both deposits, scaled
  to $300,000; (iii) Laura's literal January 2027 book.

---

## 0. Summary: the proposals ranked by deadline and impact

The architecture does not change: buy the ten payments with Treasuries first, take market risk only with money nobody
else relies on, announce in 2031 only what is already bought (brief section 8 items 1-8 stand). What changes is that
the frozen IPS must carry **rules, parameters and honest wording** that the current strategy (brief section 7) leaves
loose, and that two tier-1 WInS decisions must be taken before the first order.

| # | Change (one line) | Tier / deliverable | Confidence |
|---|---|---|---|
| P13 | WInS book: vote (ii) or (iii) before the first order. E1 leans (ii) with a scaling sentence; (iii) is fully specified as the alternative, with a named third trade | 1: WInS-now, TN, IPS | medium-low (judgement; both comply) |
| P5 | Growth money 50% world stocks / 50% short Treasuries (was 60/40), chosen by one stated rule applied under both published forecasts | 1 if (ii): WInS-now, TN; 2: IPS | medium |
| P14 | Three-note plan per option; note elements from Guide L84-86; "tested" on a pre-registered window; no planned discipline trade; dated rung only where it is genuine | 1: WInS-now, TN | high (method) |
| P2 | Certainty = bought at market prices and held to maturity, in nominal US$, barring a U.S. default, plus the two gaps named plainly | 2: IPS; 1: TN vocabulary | high |
| P1 | Central idea and pitch stated as a rule the firm controls, not a date ("bought in January 2027" and "fits inside $300k" dropped) | 2: IPS; 1: TN consistency | high |
| P3 | January 2027 rule: buy in full on arrival, longest-dated first, finish from the 2028 deposit before any growth money; no staging or yield triggers | 2: IPS | high (direction) |
| P4 | 2028 deposit rule (smaller, late, instalments) with the joint tail stated honestly (corrects D8 rule 1) | 2: IPS | high |
| P7 | 2031 range method: three slices (bought / promised-at-risk / kept), uncapped, two-sided confidence; default 80/10/10, alternate 70/15/15 | 2: IPS | high (method), medium-low (numbers) |
| P8 | Flexibility kept by rule, held in US$ short Treasuries (safety, not growth); US$ binding; no NT$ conversion or hedge before the facility decision | 2: IPS | medium-high |
| P9 | Reserve = the ladder, held to maturity, self-liquidating; "bought 2027, designated 2033" reconciled | 2: IPS | high |
| P6 | Risk tolerance stated goal by goal (need / ability / behaviour), with where her big bets already are | 2: IPS; 1: TN reflections | high |
| P10 | Governance: who decides, review dates, bad-year pre-commitments, worded so it cannot read as permission to revise after Nov 6 | 2: IPS | high |
| P11 | One consolidated if-then rule set (four rules + governance) replacing brief section 7's prose | 2: IPS | high (structure) |
| P12 | Fee principle only (no ongoing fee on the bought payments; all costs from growth money); first clause to cut | 2: IPS | medium |
| P15 | Dated decision log, evidence grades and AI-use log from today | 1: WInS-now, TN | high |
| P16 | IPS word budget, page-fit test on the exported PDF, and a paraphrase test with six readers | 2: IPS | high |

Section 2 (P17) lists what must **not** go into the IPS. Section 3 lists the conflicts E1 could not resolve, with both
sides. Section 4 is the team's decision checklist in date order.

**North Star link (INT).** The plan becomes Laura's, not a generic liability match, through five checkable decisions,
each tied to a case line: (1) the payments are bought before her career-income deposit can matter (case L43-45, R-C27);
(2) nothing is announced to co-sponsors that is not already bought (L114-116, R-C66; her income is reputation-driven,
BS-03); (3) certainty is defined by a price she can check, not a model (L16 statistics degree, R-AN32; L97-99);
(4) stock risk sits only where she alone bears the cost (the case's "Although", L69-74, R-AN16); (5) flexibility for a
project that will change is kept by rule, not by leftovers (L102-103, R-C58).

---

## 1. What stays the same (no change proposed)

- Lock the whole ladder; do not tier or roll the 2037-42 payments (brief section 8 items 1-2; F-108 +$20k per -100bp)
  [VRF inputs, MODEL].
- STRIPS rather than coupon Treasuries for Laura's real ladder (coupon reinvestment risk ~$5k, F-113) [ASM method].
- Risk measured on the growth money only; more equity "buys range, not median" (F-407; D3 M034) [MODEL].
- A single dated 2031 floor purchase; no ratchet, no barbell (D3 M055: a plain ~42% equity sleeve matches the ratchet's
  bad case within $2k of median; D3 M238: a 50% barbell can promise only ~$101k bought in 2031 vs ~$165k) [MODEL].
- WInS hedge = IEF + TLH at duration weights (about 10 years), SPTL only if a Session Rules cap is under 44%; broad
  world equity (VT) and short Treasuries (VGSH); no Taiwan, AI, thematic, leveraged or single-country funds (ticket
  sections 1-3; S2; D8 M081) [VP issuer facts via S3/S4].
- The three "never" rules in WInS (never sell the hedge after a rate rise; never trim it after a rate fall; never
  day-trade) and the five-box gate before the first order (ticket) [VP rules via A4].
- No Laura quotes in the TN or the IPS; the case pull quote is the case's words, not hers; no "floor-first leap"
  (brief section 16; D13a; D13c) [VRF/VP].

---

## 2. Change proposals

Each proposal gives: **Change**; **Why** (case R-id or fact F-id, and the Laura link); **Numbers** (script and status);
**Side effects and cost**; **Touches** (TN / IPS / WInS-now); **Complexity** (does it earn its place?);
**Confidence**; **Team decides**.

### P1. Central idea and the 50-word pitch: a rule the firm controls, not a date

**Change.**
- The central idea (IPS guide L16, L35-36, R-I9, R-I17) is stated as a rule: no dollar of Laura's money takes
  stock-market risk until all ten payments are bought (with the 2028 deposit finishing the ladder first if prices
  rise before January 2027). Replace every headline use of "the payments are bought in January 2027" and "the ladder
  fits inside $300,000" (brief section 7) with this rule.
- **Pitch content spec (elements, not wording; 50-word hard cap, R-I16):**
  1. the rule above, in plain words (about 12-15 words);
  2. the client benefit, stated conditionally: once bought, the ten payments no longer depend on markets or on her
     future earnings (about 12-15 words; M143);
  3. what the rest is for: growth toward the facility contribution, with part kept for flexibility (about 10-12
     words);
  4. optional, only if words allow: the 2031 range whose bottom is already bought (about 8-12 words).
- **Must not contain:** a date-certain claim; "fits inside $300,000"; "guaranteed", "risk-free", "100%", "95%";
  jargon (LDI, duration, DV01, STRIPS, liability matching); more than one number (preferably none); any Laura quote,
  the pull quote, identity imagery or book-title puns; "safe" (0 uses in the six official files, D9 M062).
- **IPS opening** (IPS guide L53-57: what, why): repeats the same rule and states the if-rates-fall branch once
  (P3), so the pitch and the IPS cannot drift apart.
- Every phrase in this file that describes the rule or a benefit is **content, not wording** (AY2 correction 13): the
  team writes its own sentences and does not copy these.

**Why.**
- The date claim is false in about 1 path in 3 for the real ladder (P3 numbers), and overpromising is the case's own
  credibility test (L114-115, R-C66) [VRF]. A rule is true in every path by construction (D7 M011) [INT].
- Laura link: her 2028 money comes from "publishing advances, speaking engagements, licensing, and other
  entrepreneurial ventures" (L44-45, R-C27, R-AN31) [VRF], so the benefit that only a client with career-driven
  deposits gets is that the promise stops depending on that income (D9 M143) [INT]. Swap test passes (D13c) [INT].
- The IPS guide asks for "the central idea behind your approach and how it is designed to support your client's
  financial goals and future funding needs" (L35-36) [VRF].

**Numbers.** Word costs: elements 1-3 about 34-42 words, a fourth only in very plain words (D9 pitch table) [INT].
P(ladder > $300k on 2027-01-01) about 1 in 3 for the real Nov-15 ladder (P3) [MODEL]; this is why the date claim goes.

**Side effects and cost.** The pitch loses a vivid date. Under WInS option (ii) the rule is visibly contradicted by a
day-one VT buy unless the IPS carries the scaling sentence (P13) (AY2 rank 1) [VRF].
**Touches.** IPS (pitch, opening); TN (every note must be consistent with it, TN L30-31).
**Complexity.** Zero added words; it replaces a claim with a truer one. Earns its place.
**Confidence.** High that the date claim is unsafe and the rule is true; medium that it is distinctive (rivals'
submissions are unobserved, BS-10) [INT].
**Team decides.** Wording; whether element 4 fits.

### P2. The certainty definition and its two honest gaps

**Change.** Replace "certain in nominal USD, barring U.S. Treasury default" (brief section 7) with a definition that
has three parts and names two gaps. **Elements the IPS must contain (words are the team's):**
1. **Bought, not forecast:** each payment is matched by a Treasury that matures shortly before its date and is held to
   maturity (for Laura's real ladder; in WInS the funds only "move like" the payments, P14).
2. **How it is evaluated:** by price. At purchase the money covers the market price of the ten payments (funded ratio
   at least 1); no model percentage is used for the payments (case L97-99 asks how certainty "was evaluated", R-C54,
   R-C55) [VRF].
3. **The residual risk named:** certain in U.S. dollars, barring a U.S. Treasury default.
4. **Gap (i), the January 2027 price:** if rates fall before January, the ladder can cost more than $300,000; the rule
   (P3) finishes it from the 2028 deposit, so until then part of the earliest payment depends on that deposit.
5. **Gap (ii), nominal US$ vs Taiwan costs:** each payment is a fixed US$50,000 "not adjusted for inflation" (L90,
   R-C46) and the residency spends in Taiwan, so the same payment buys less each year and moves with the exchange
   rate; named, not solved (support beyond her commitment may come from others, L85-86, R-C44) [VRF].
6. **Vocabulary:** "uncertainty" is the official word for what markets can do to both goals (11 uses across the
   official files; case test 3, L140-141) [VRF via AY2]. For the payments it is limited to the named residuals above;
   "certainty" belongs to the payments, "confident" to the 2033 range, "credibility" to Laura's standing (D9 M062)
   [VRF].
7. **Grade words:** every forecast-based statement carries a marker ("we assume", "history suggests"); prices carry
   "at today's prices" (D12 M231) [INT].

**Why.** The case requires teams to "define what they consider a high degree of funding certainty, explain how they
evaluated that level of certainty, and identify the assumptions" (L97-99) [VRF]; a statistics-trained client (L16,
R-AN32) would reject a model "95%" (brief section 8 item 6: no-lock miss rates 3.3-9.3% depending on rate-drift
assumptions) [MODEL]. Brief section 16 makes both gaps binding [VRF]. D13c N4: a client who labels her own results
"[unfinished]" would expect the holes named [INT; the line itself is VP but FR-only].

**Numbers** (IPS carries none of them; they justify the words):
- Gap (i): P3 below.
- Gap (ii): a fixed $50,000 is worth $42,063 (2033) and $33,681 (2042) in 2026 dollars at JPM's 2.5% inflation
  (F-114) [ASM inflation]. Taiwan construction costs rose about 3.54% a year since 2021 and 2.11% a year 2008-2026 (F-508;
  D4) [VP inputs, derived]; a fixed US$ amount buys about 11-20% less building by January 2033 on those paths (D4 table
  A) [ASM]. USD/TWD 31.82 on 2026-09-18; two-year moves sd 6.8% since 2006 (F-510, F-513) [VP inputs, derived].
- Residual credit: Moody's cut the U.S. to Aa1 on 2025-05-16 [SNIP, secondary; not checked on moodys.com].

**Side effects and cost.** About 45-60 IPS words (P16). Naming gap (i) admits that the promise is not complete on
day one in about a third of paths; that is the honest price of not timing rates.
**Touches.** IPS (definition); TN (the certainty vocabulary governs every note from the first trade).
**Complexity.** Earns its place: it answers a "should" in the case directly and removes the one overclaim a
statistics reader would catch.
**Confidence.** High.
**Team decides.** Wording; whether to mention the currency gap in the same clause as inflation (AY2 recommends it).

### P3. The rule if rates fall before January 2027

**Change.** Fix in the IPS (elements, not wording):
1. **Buy in full on arrival** (1 January 2027). No staging, no waiting for a yield level.
2. **Longest-dated payments first** if the money does not cover all ten.
3. **Completion before growth:** any unbought part (always the earliest payment or payments) is the first use of the
   2028 deposit, before any growth investment; if the deposit arrives in instalments, completion comes first from each.
4. **Headline, conditional:** fully bought in January 2027 if prices allow, otherwise when the second deposit arrives
   (the case dates it to the start of 2028). Do **not** write "by 1 January 2028 at the latest" (AX1b item 3).
5. **Dependence stated in words**, a typical case and a bad case, never "at most" (AX1b item 2).
6. **If rates rise instead:** the few thousand dollars left over wait in Treasury bills until 2028, then join the growth
   money (ticket section 8).
7. The reason against staging is the numbers, **not** Guide p.5 (that line governs the post-IPS stage; Guide L89-90
   says the strategy may evolve before the IPS) (AX1b item 4; AX2 D2 C3) [VRF].

**Why.** The case requires "a high degree of certainty" (L91, R-C47) and forbids relying on outside money (L91-92,
R-C48) [VRF]; the 2028 deposit is Laura's own contribution to the portfolio, so using it is not outside funding (D1)
[INT, low risk]. A rule written before the surprise is what lets the Final Report apply rather than redesign (IPS
guide L73-75; Guide p.5) [VRF].

**Numbers** (`D1_purchase_rule.py`, `AX1b_rates_audit.py`, `strategy_mc_v2.py` (a), `D3_joint_tail.py`):
- The real Nov-15 STRIPS ladder costs $294,387 for purchase on 1 January 2027, priced from the 2026-09-25 curve;
  headroom $5,613 (19bp) [VRF inputs, ASM method; D1, D3, S1].
- It would have cost more than $300,000 on 176 of 185 trading days of 2026 so far (173 of 185 for the idealised
  exact-date ladder; F-111) [VP inputs, derived].
- P(cost > $300k on 2027-01-01): 30-34% for the real ladder, 24% for the exact-date ideal [MODEL, zero-drift, 2026
  volatility]; model-free check: the 10-year yield fell 19bp or more over 68 trading days in 32-36% of windows since
  1962/1990 [VP inputs (FRED DGS10), derived; AX1b]. Say **"about 1 in 3"** for the real ladder.
- Gap sizes: -50bp $9,169; -100bp $24,793 (top-up in January 2028 $25,711, 17% of the deposit); the worst 2026 curve
  (Feb 27) $27,631 (68.7% of the 2033 payment waits); a repeat of the worst 3-month fall since 1990 (-167bp, late 2008)
  leaves all of 2033 and ~16% of 2034 waiting, $48.6k (32% of the deposit) [MODEL on VP inputs; D1, AX1b].
- Staging: four quarterly tranches or a "wait for a 5% margin" trigger give no reliable gain in the expected funded
  ratio (+0.2 to -0.5 points, depending on whether rates are assumed to follow today's forwards or stay put) and a
  27-35% chance of ending below 1.00, i.e. of needing the 2028 deposit (tranche p5 0.96-0.97; trigger p5 0.90-0.91),
  against a known 1.02 if bought on the day [MODEL; D1 [7], AX1b item 11].
- Longest-first vs nearest-first: a further -100bp during 2027 adds +$1,265 (+5%) to the top-up vs +$3,831 (+15%);
  if the deposit never comes at -100bp, $31.4k vs $47.7k of payment face is left unbought [MODEL; D1, AX1b item 23].

**Side effects and cost.** In about a third of paths the ladder is complete only in January 2028, and the growth money
starts smaller by the top-up (mean ~$7k when a gap exists; D3 v2 (a)) [MODEL]. Counterpoint (AX1b item 23): under
longest-first any shortfall falls on the residency's first operating year.
**Touches.** IPS (rule 1 of P11). TN: optional by-product only (the hedge reflection may say the hedge was set to what
the first deposit buys at today's prices, with the top-up rule named).
**Complexity.** One rule with branches, about 25-35 words (D8). Earns its place: it binds in about 1 path in 3.
**Confidence.** High on the direction; medium on the odds (model assumptions; history agrees).
**Team decides.** Wording only.

### P4. The 2028 deposit rule (smaller, late, in instalments) and the joint tail

**Change.** Fix in the IPS (elements):
1. The 2028 deposit first completes any unbought payment (P3); only what is left becomes growth money.
2. **Smaller:** the payments are still completed first; the facility range shrinks.
3. **Late or in instalments:** completion comes first from each instalment; growth money starts when the ladder is
   complete; the facility range shrinks slightly.
4. **Joint tail (rates fall before January 2027 *and* the deposit is smaller than the gap):** all of the deposit goes to
   the unbought payments, no growth money is created, no 2031 floor is announced, and the unfunded part of the earliest
   payment is stated. It is **not** true that "only the facility range shrinks" in this case; correct D8 rule 1
   (AY2 rank 2; AX1b) [VRF].
5. **Labelled as the team's own stress scenario:** the case says she "will contribute" (L43-45, R-AN35) [VRF].
6. **No facility floor is announced until all ten payments are bought** (D3 M053) [INT].

**Why.** The deposit comes from income Laura herself described as unstable (VP, D13a B8b-Q18; FR only, never in TN
or IPS) and book advances arrive in instalments (BS-13) [VP via A3]. The Portfolio Analysis criterion asks for
"varying market outcomes" (R-S26) [VRF]. A frozen rule must not overclaim (IPS guide L73-74) [VRF].

**Numbers** (`strategy_mc_v2.py` (b), `D3_joint_tail.py`, `D1_purchase_rule.py` [8]):
- Deposit arrives in full, late (January 2029) or at $75k: payments short in 0% of tested paths [MODEL]. Any deposit
  of about $43k or more fills the gap even after a 150bp fall [MODEL].
- Late by one year: 2033 surplus median -$11k; six months late at -100bp: +$531 extra top-up cost [MODEL].
- $75k deposit: 2033 surplus p5/p50/p95 $73k/$105k/$149k (central case) [MODEL].
- Missing deposit: part of the 2033 payment unbought in about 30% of paths (the gap odds), mean $9.1k, p95 $23.7k; at
  -50bp $11,957 and at -100bp $31,413 of the first payment [MODEL]. A $75k deposit covers every case down to the
  2008-size fall (AX1b) [MODEL].
- Correlation of a cut deposit with a 2027 recession cannot be sourced (no data found on publishing/speaking income in
  recessions, D3 M053) [UNVERIFIED], so report conditional dollars, not a joint probability.

**Side effects and cost.** None to the structure; about 15-20 words inside rule 1.
**Touches.** IPS.
**Complexity.** Folded into rule 1; earns its place (case-specific income source).
**Confidence.** High.
**Team decides.** Wording; whether the joint tail is named in the IPS or only in the Final Report (E1: name it once in
the IPS, because a frozen rule must say what it does in its own worst case).

### P5. Growth-money split: 50% world stocks / 50% short Treasuries, chosen by one stated rule

**Change.** Move the growth money from the provisional 60/40 (brief section 7; CLAUDE.md interview call 1, "weakest
call") to **50/50**, rebalanced once a year within a **45-55%** band, and state the reason as **one rule applied
under both published forecasts**: hold the most stock that still leaves about a 1-in-20 chance that the growth money
ends 2033 with less than the money Laura put into it (~$157.7k). The same 50/50 applies to the unlocked part of the
growth money after the 2031 floor (answers D2 C13).

**Why (this resolves D2 vs D6).** D2 said 50/50 because the median is flat across forecasting houses; D6 said its rule
"picks 60%"; AY1 showed the rule gives 55-70% depending on inputs. E1 ran D6's own rule under both houses, two bond
assumptions and three fee levels: **50% is the largest share that passes under both houses' central forecasts with
market-consistent bonds and a fee of up to 0.5%**; 60% passes only if J.P. Morgan's forecast is right and fees are low.
So D6's rule and D2's two-house insight agree on 50% once the rule is applied to both houses [MODEL].
- Case: "willing to take thoughtful risks" and "an appropriate balance between pursuing growth and protecting the
  capital required for her goals" (L69-74, R-C37, R-C38) [VRF]. INT: risk that is checked against what the safe
  alternative pays, and sized by a stated rule, is a concrete reading of "thoughtful"; the rule always picks the *most*
  stock that passes its test, so it never lands at the minimum, which answers D13c's "not set at the minimum to look
  safe".
- The reason rests on things that do not change with this year's valuations (AX2 D2 C7): the growth money feeds a
  promise made in 2031, the median barely moves, the bad case improves.

**Numbers** (`E1_split_and_slices.py` [1]-[2]; all MODEL, i.i.d. lognormal, JPM 2026 LTCMA [VRF] and Vanguard VCMM
2026-06-30 [VP via D2/AX2]; sleeve bonds 4.0% [VRF, JPM] or 5.0% [ASM, market-consistent]; fees [ASM]):

| Cell (house, bonds, fee) | Rule's pick | P(below money put in) at 50% / 60% | Median 50% / 60% | p5 50% / 60% |
|---|---|---|---|---|
| JPM AC World 7.00%, bonds 5.0%, no fee | 65% | 1.7% / 3.5% | $210k / $211k | $168k / $162k |
| JPM AC World, bonds 5.0%, fee 0.5% | 60% | 2.4% / 4.5% | $206k / $208k | $165k / $159k |
| JPM U.S. 6.70%, bonds 4.0%, fee 1.0% | 50% | 4.5% / 6.9% | $199k / $201k | $159k / $154k |
| Vanguard U.S. midpoint 5.2%, bonds 5.0%, no fee | 55% | 2.8% / 5.4% | $204k / $204k | $163k / $157k |
| Vanguard midpoint, bonds 5.0%, fee 0.5% | 50% | 3.8% / 6.8% | $200k / $201k | $160k / $154k |
| Vanguard U.S. low end 4.2%, bonds 5.0%, no fee | 50% | 3.7% / 7.0% | $200k / $200k | $161k / $154k |

- Robust test [MODEL]: pass in every cell of "both houses' central cases, bonds 5.0%, fee up to 0.5%" = **50%**; all
  JPM cells (both equity rows, both bond cases, all fees) = 50%; both central cases with no fee = 55%; every cell
  including Vanguard's low end = 40%.
- Moving 50% to 60%: median +$0.2k to +$2.1k; p5 -$5k to -$7k (E1 [1]); p95 +$11-14k (D2) [MODEL]; 2031 floor p5
  +$5-6k at 50% (D2) [MODEL].
- Expected extra return of world stocks over the Treasury rate implied for her 2028-2033 dates (~5.2%, **implied,
  not lockable**): central forecasts about 0 (Vanguard midpoint) to +1.8 points (JPM); full published ranges and
  yardsticks about -1.2 to +2.4 points a year (D2 with AX2 C1-C2) [VP inputs, derived].
- WInS option (ii) orders at 50/50 (ticket v1 section 1): IEF 23.5% / TLH 42.5% / VT 17.0% ($51,000, ~318 sh at
  $160.03) / VGSH 16.0% ($48,000, ~833 sh at $57.59) / cash 1% (VT equals the plan's whole-portfolio stock share; the
  cash float comes out of the short-Treasury part); recompute on the trade date [VP prices 9/25; arithmetic].
- Whole-portfolio stock share (E1 [3], median path): 0% in 2027 (leftover in T-bills), **17.0%** after the 2028
  deposit (20.4% at 60/40), **3.5%** after the 2031 floor at an 80% lock (5.2% at 70%) [MODEL].

**Side effects and cost.** Gives up $11-14k at p95 and about $0-2k of median [MODEL]. The whole portfolio looks even
more cautious (17% stocks after 2028 instead of 20%), which sharpens D13c's "timid" tension; P6 answers it by stating
risk goal by goal. Ticket v1 already carries both splits (VT 17.0 / VGSH 16.0, band 45-55 at 50/50); the team ticks
one. D10's equity-gap figure under (ii) becomes +17.0 points (AX2 D10 C7).
**Touches.** WInS-now and TN only if option (ii) is chosen (AX2 D2 C4); otherwise IPS only (rule 2 of P11).
**Complexity.** Zero extra rules: it replaces an unexplained 60% with a stated rule of two numbers (a threshold and "about
1 in 20"), which the IPS needs anyway (IPS guide L46, "approach risk and return") [VRF]. Earns its place.
**Confidence.** Medium. High that the median is flat and the choice is about spread; medium on 50% specifically (the
fee and house assumptions decide between 50 and 60; the model is fee-free and thin-tailed by default).
**Team decides.** 50/50 (passes under both houses) or 60/40 (passes only under JPM with low fees), written as a choice of
spread either way. Decide **before** the VT/VGSH orders if (ii) (a preference, not a rule: a later research-based change
is allowed before Nov 6 and could be a genuine "refined" note, AX2 D2 C3). If the team keeps 60/40, record why.

### P6. Risk tolerance stated goal by goal

**Change.** The IPS states risk tolerance per goal, using the three parts professionals use (CFA Institute 2020: risk
need, risk-taking ability, behavioural loss tolerance) [VP via D6/AY1]. **Elements:**
1. **Payments:** no risk *needed* at today's prices (the Treasuries cost less than her first deposit; if the January
   price is higher, that is a funding need met by the 2028 deposit, not a reason to take market risk, AY1 D6 C8) and
   none *affordable* (high certainty, no outside money, L91-92). So her appetite for risk is deliberately not used here.
2. **Growth money:** low need (no facility target, L104, R-C59), high ability (living costs outside the portfolio,
   L61-63, R-C33; no withdrawals before 2033, L63-65, R-C34; a loss shrinks only the facility range), so it holds real
   stock (P5) even though no target requires it.
3. **The 2031 floor:** once announced, it carries no market risk.
4. **Willingness** in the case's own words ("thoughtful risks", "appropriate balance"); her *investment* loss tolerance
   is the team's inference (it cannot be measured without contacting her, R-W16), so the bad-year decisions are
   pre-committed (P10).
5. **Where her big bets already are:** her career, books and the residency itself; the 2028 deposit already rides on
   them (R-AN31), so the portfolio holds only broad market risk, no tilts (D8 M081; Chhabra 2016 interview, VP).
6. Optional, one clause: the whole-portfolio stock share by stage (about none in 2027, about one-sixth after 2028, a
   few percent after 2031) so a first reader sees where the risk is and why (M033; AY1 D6 C4) [MODEL numbers in P5].
7. **Not** her career story as a reason (risk attitudes are "highly domain-specific", Weber, Blais & Betz 2002, VP via
   D6), not her regret line (AY1 D6 C3), not "risk-averse" (D13a context) [VP].

**Why.** An IPS "outlines an investor's financial goals, risk tolerance" (IPS guide L3, R-I2) and the case never states
one (R-AN17) [VRF]. CFA reconciliation rules [VP]: "Higher behavioral loss tolerance can be ignored when both the risk
need and risk-taking ability are lower" (payments) and "A lower risk need can be discounted when both risk-taking
ability and behavioral loss tolerance are higher" (growth money). Laura link: the case's "Although" (R-AN16) separates
her career risk-taking from what she wants for this money [VRF, INT].

**Numbers** (`D6_behavioural_numbers.py`) [MODEL]: under the plan the growth money falls in about 27% of years
2028-2030; at least one down year before 2033 in 62% of paths; the whole statement shows a fall in about 1 year in 10;
the rejected growth-first plan would show assets below the value of the payments on the first December statement in
about 40% of paths.

**Side effects and cost.** About 35-50 IPS words, merged with the "where risk sits" principle (D9 M241: outside money
may cover the facility, never her ten payments, L85-86 vs L91-92) [VRF].
**Touches.** IPS; TN reflections (each "how it serves Laura" line echoes one case trait and passes the swap test, D6
M125).
**Complexity.** Replaces a one-word label ("moderate") with a structure the IPS guide asks for. Earns its place.
**Confidence.** High.
**Team decides.** Wording; whether to include element 6.

### P7. The 2031 co-sponsor range method: three slices, bought bottom, uncapped, two-sided confidence

**Change.** Replace "a floor bought in a 2-year Treasury plus an upside with a stated probability" (brief section 7)
with a method whose parameters are fixed by Nov 6 (method only; no dollar range in the IPS, IPS guide L68-69):
1. On 1 January 2031 split the growth money into **three slices**: a share **a** is bought as a Treasury maturing before
   1 January 2033 (the bottom of the range); of the rest, a share **s** is promised as the stretch; the other **(1-s)**
   is kept for the project (P8).
2. In 2033 the gift = the bought amount + s × what the rest has become, **uncapped**.
3. The top = the bought amount + s × a stated high percentile of the rest's two-year growth (E1 default: the 90th, so
   "about 1 in 10" above the top).
4. Confidence stated **both ways**: below the bottom only if the U.S. Treasury defaults; above the top about 1 in 10,
   with the model named (in the Final Report).
5. The range is set in 2031 from what is then owned, never from a projection made today (M040).
6. No range is announced until all ten payments are bought (P4); the operating payments are never touched (L119-120,
   R-C71).
- **E1 default: a = 0.8, s = 0.5 ("80/10/10": 80% bought, 10% promised but still at risk, 10% kept).** Alternate
  "70/15/15" (a = 0.7, s = 0.5, D5's candidate) if the team weights flexibility more.

**Why.** Case: "Rather than promising one exact amount, she wants to communicate a credible range" (L115-116, R-C67);
"state how confident they are that her 2033 contribution will fall within that range" (L117-118, R-C69, two-sided per
R-AN9); "explain how favorable and unfavorable market outcomes could affect the amount" (L118-119, R-C70); "committing
all remaining assets could limit her financial flexibility" (L102-103, R-C58) [VRF]. D5's key finding: "promise the
upside" and "keep flexibility" conflict unless one number (s) splits the rest [MODEL/INT, audited]. Laura link: her
credibility with co-sponsors, and through it her reputation-driven income (BS-03), is at stake [VRF, INT].
- Why uncapped (D5 over D3): (i) one rule fewer; (ii) good markets visibly raise the gift, which R-C70 asks teams to
  explain; (iii) "100% within the range" by construction is an empty figure to a statistics reader (SH-04, AY1 X11);
  (iv) over-delivering never costs credibility, under-delivering does (R-C66) [INT].
- Why 80/10/10 as default: the highest bought bottom while still keeping flexibility by rule (R-C64 "meaningful
  personal contribution" vs R-C58); consistent with the verified model's 80% floor (F-402); behavioural evidence favours
  narrow honest ranges (D6 M197: "as precise as warranted", Du et al. 2011, VP); D4's finding that by 2031 markets are
  the smallest uncertainty needs about 70% or more locked (AX2 D4 C2) [MODEL]; the kept 10% is about three years of
  Taiwan building-cost drift at the post-2021 pace (1.0354³ = 1.11) [ASM sanity check, not a contingency fund,
  R-C61].

**Numbers** (`E1_split_and_slices.py` [4]; 50/50 sleeve, JPM AC World, bonds 5.0%, no fee; MODEL):

| Slices (bought / at-risk / kept) | Median bought bottom | Median top (p90) | Width | Gift p5/p50/p95 | Kept p5/p50/p95 |
|---|---|---|---|---|---|
| **80/10/10 (default)** | $167k | $192k | 1.15x | $151k / $188k / $238k | $16k / $21k / $29k |
| 70/15/15 (alternate) | $146k | $183k | 1.26x | $142k / $178k / $226k | $24k / $32k / $43k |
| 80/20/0 (give all, s = 1) | $167k | $216k | 1.30x | $168k / $210k / $266k | $0 / $0 / $0 |
| 90/5/5 | $188k | $200k | 1.07x | $159k / $198k / $251k | $8k / $11k / $14k |

- Width ≈ 1 + s(1-a)/a × ~1.2 (AY1 [2]); the comparable quantity across D5 and D6 is the share promised but still at
  risk, s(1-a): 0.10 (default), 0.15 (alternate), 0.20 (D6/D3 base) [MODEL].
- Without a cap an "80%" top lands within the range 62-93% of the time across models and history; every miss is on the
  upside (D3 v2 (f)) [MODEL]. P(below the bottom) = 0 in every model and history test (bought) [MODEL].
- The bottom moves -3.4% if the 2031 two-year rate is 3.0% instead of 4.81%, +2.3% at 6.0% (AY1 [4]) [ASM rates].
- 90/5/5 is rejected: 1.07x is close to the "one exact amount" the case rejects (L115-116) [INT].

**Side effects and cost.** Three parameters (a, s, q). The range is lopsided by design: outcomes cluster near the top
(D5/AY1 C6), so the Final Report must present a "likely figure", not the midpoint (later list). The 70/15/15 alternate
lowers the bought bottom by about $21k at the median.
**Touches.** IPS (rule 3 of P11). Not TN (the TN guide excludes the facility and co-sponsor draft, L20-21); no floor
share in any WInS note (ticket) [VRF].
**Complexity.** Each parameter moves money a reader cares about (bought / promised / kept); the rule fits two plain
sentences (AY1). Earns its place, because without s the plan's "upside" and "flexibility" contradict each other.
**Confidence.** High on the method; medium-low on the exact slices (a judgement between credibility and flexibility).
**Team decides.** The slices (80/10/10 or 70/15/15), the top percentile (one value only; D5 used 85, D6 90, D3 80),
cap or no cap (section 3, conflict C3).

### P8. The flexibility rule and what the kept money holds

**Change.**
1. Flexibility is **reserved by rule** (the kept slice (1-s) of P7), not "whatever is left" (brief section 7).
2. The kept money is held in **US$ short-term Treasuries / T-bills** from 1 January 2033 (the kept (1-s) part of the
   unlocked growth money moves there on that date), i.e. with safety, not "invested for growth". This corrects the team notes' mapping
   of flexibility to the aspirational bucket (D8 M081; team notes L15-18) [VRF].
3. **US$ is the binding currency** for the promise, the reserve and the range; any NT$ figure is dated and illustrative
   (D4 with AX2 C1) [INT].
4. **No NT$ conversion or currency hedge before the facility decision**: a forward is a derivative, banned in WInS and,
   on the safe reading of "Investments permitted (for BOTH contributions)", in the plan (R-AN15, R-AN49; AX2 D4 C3)
   [VP rules; INT reading]; converting early would also be a currency bet.
5. The IPS **names the assumption** that Taiwan building costs are expected to rise, so a fixed US$ gift buys less (case
   L146-147 asks for "the effect of inflation on portfolio projections and facility costs", R-C85) [VRF]; no numbers,
   no facility cost estimate (L164-165, R-C95).
6. Its purpose in words: changes "as the project develops" (L102-103), not Laura's living costs (outside, L61-63) and
   not a sized contingency fund (L106-107, R-C61) [VRF].

**Why.** Flexibility exists to absorb surprises; putting it in stocks means the money for bad news is most likely to
be down when bad news arrives (D8 M081) [INT]. Laura link: the case's own "as the project develops" (R-C58, R-AN19)
[VRF]. CLAUDE.md's provisional call 3 ("post-2033 leftover mainly as project flexibility/overrun buffer") is kept and
made concrete [VRF].

**Numbers.** Kept money under the default 80/10/10: $16k/$21k/$29k (p5/p50/p95), about 10% of the post-reserve money;
70/15/15: $24k/$32k/$43k (E1 [4]) [MODEL]. Taiwan construction cost index +3.54%/yr since 2021 raises costs about 11% in
three years (F-508; D5) [VP inputs, derived]. Locking NT$ two years ahead would cost about 5.9% at today's rate gap
(D4; Taiwan 2-year yield 1.66% is SNIP) [ASM].
**Side effects and cost.** Kept money earns short-Treasury rates, not equity returns (a small expected cost). About
15-25 IPS words (folded into the certainty/assumption clause and rule 4).
**Touches.** IPS.
**Complexity.** No new rule: it fixes the composition of money the plan already has. Earns its place.
**Confidence.** Medium-high.
**Team decides.** Whether the kept money is short Treasuries (E1) or stays 50/50 (the team's earlier "ventures second"
idea); E1 sees no case line supporting growth for this money.

### P9. The operating reserve: composition over time and which number is "the reserve"

**Change.** Fix in the IPS (elements):
1. The reserve **is the ladder**: bought from January 2027 (completed from the 2028 deposit if needed) and designated
   the operating reserve on 1 January 2033, before the first payment or any facility contribution (L94-95, R-C50,
   R-AN2, R-AN28) [VRF]. One clause reconciles "funded 2027, set aside 2033" (brief section 8 item 9).
2. **Composition over time:** held to maturity; each rung matures on 15 November of the year before its payment and waits
   about 47 days in Treasury bills; nothing is sold early; so the composition changes only as rungs mature (the case
   allows "if at all", L96, R-AN27) [VRF, ASM dates per S3].
3. **No rebalancing between the reserve and the growth money**, written down (CFA 2010 element 4c: "If the policy is not
   to rebalance, this policy should be documented in the IPS", VP via D8/D10).
4. **Which number:** the Final Report reports the reserve at market value on 1 January 2033 (~$395k on today's
   forwards, F-106) alongside its cost and face value; the IPS names the method only.

**Why.** The IPS guide asks the IPS to "establish your strategic approach to ... managing the operating reserve's asset
composition over time" (L48-50, R-I22) [VRF] and "How will the portfolio's asset allocation and composition change as
future funding needs approach" (L22, R-I12) [VRF]. The honest answer is three dated steps (2028 completion and growth
start; 2031 floor; 2033 reserve and facility), not a funded-ratio glide path: once bought, the ladder's funded ratio
stays at 1 barring default, so a "below 100%" trigger can never fire (D10 finding 6; parked M149) [INT].

**Numbers.** Cost $292,264 (exact dates) / $294,387 (Nov-15 STRIPS) at 2027-01-01; forward value $394,930 at
2033-01-01; face $500,000 (F-101, F-106; D3) [VRF inputs, ASM method].
**Side effects and cost.** About 20-30 IPS words, shared with rule 4.
**Touches.** IPS.
**Complexity.** None added; answers a required element. Earns its place.
**Confidence.** High.
**Team decides.** Wording.

### P10. Governance, review dates and bad-year pre-commitments

**Change.** About 30-45 IPS words (D10 M013), elements:
1. **Who decides:** the students' written rules run the portfolio; Laura makes the two choices the case gives her (the
   range she announces in 2031 and the 2033 facility amount), on the team's rule-based recommendation. **No** "our
   portfolio manager/advisor approves" (Rules page: "Advisors may not make decisions on behalf of students", VP; R-AN4).
2. **Review points** at the case's own dates: 1 January 2027 (purchase), 2028 (deposit, completion, growth start), 2031
   (floor, announcement), 2033 (reserve, facility), plus a yearly check of the growth mix.
3. **What may change a rule:** a change in Laura's circumstances, never a market move; worded so it cannot be read as
   permission to revise the strategy after Nov 6 (IPS guide L73-74; AY2 D8 C12) [VRF].
4. **Bad-year pre-commitments** (folded into the rules, no separate clause; D6 bad-year table):
   - stocks fall: only the yearly reset inside the band; the ladder is never sold;
   - before 2031 after losses: the floor is bought on its date, not delayed "until it recovers" (break-even trap,
     Thaler & Johnson 1990, VP via D6);
   - after gains: only the bought amount is announced as the bottom (house-money trap, same source);
   - the hedge in WInS is never sold or trimmed because rates moved; it is only re-mixed to keep its rate sensitivity
     near the payments' (AY2 D7 C7).
5. **Cut:** org chart, firm name or size, reporting frequency, residency-delay trigger, citations (D10 keep/cut).

**Why.** CFA 2010: the IPS offers "an objective course of action to be followed during periods of market disruption"
and a review process "clearly identified in advance" [VP via D8/D10]. Guide p.5: "planned adjustments as funding dates
approach" are allowed, redesign after results is not [VRF]. Laura link: "Laura understands that investing involves
uncertainty and periods of market volatility" (L68-69, R-C36) [VRF]; her investment composure is unknown (P6), so the
plan must not depend on it [INT].

**Numbers.** A down year for the growth money is more likely than not before 2033 (62% of paths) (D6) [MODEL].
**Side effects and cost.** 30-45 words.
**Touches.** IPS; WInS-now (the ticket's "never" rules are the WInS version).
**Complexity.** Earns its place: without it, Final Report actions could read as post-freeze changes (Guide L158) [VRF].
**Confidence.** High.
**Team decides.** Wording.

### P11. One consolidated if-then rule set (replaces brief section 7's prose)

**Change.** The IPS carries four money rules plus governance, each with a trigger, an action and what the Final Report
will later show "fired as written" (D8 M006/M235, with every audit correction applied). Parameters in brackets must be
fixed by Nov 6.

| Rule | Trigger | Action | Covers (case test) |
|---|---|---|---|
| 1. Promise first | Money arrives (Jan 2027; 2028 deposit, each instalment) | Buy the ten payments before anything else; longest-dated first if short; the 2028 deposit completes them before any growth; joint tail stated (P3, P4) | Test 1 certainty (L136); test 3 for the payments |
| 2. Growth mix | Once a year, or when outside the band | Reset the growth money to [50/50] world stocks / short Treasuries, band [45-55]; same mix for the unlocked part after 2031 (P5) | Test 3 (the risk held is the risk stated) |
| 3. The 2031 range | 1 January 2031 | Buy [a = 0.8] of the growth money as a Treasury maturing before 2033 (the bottom); top = bottom + [s = 0.5] × [90th] percentile of the rest; two-sided confidence; no announcement before the ladder is complete (P7) | Tests 3, 4 (L140-143) |
| 4. 2033 order of use | 1 January 2033 | Reserve = the ladder, held to maturity; facility = bottom + [s] × what the rest became (uncapped); the other [1-s] kept in US$ short Treasuries for the project (P8, P9) | Tests 2, 5 (L138, L145) |
| G. Governance | Case dates + yearly | Rules change only for a change in her circumstances, never because markets moved (P10) | IPS guide L73-74; Guide p.5 |

- **Three trade-offs** to name in words, each "gives up X to get Y", inside the rules' "because" clauses (D9 M121;
  Guide p.5 "reasoning, assumptions, and tradeoffs", VRF): T1 some facility money in strong markets for payments that
  cannot miss; T2 some growth after 2031 for an amount she can state in advance; T3 the chance of cheaper bonds if rates
  rise for never paying more because rates fell (buy on arrival). No numbers in the IPS.

**Why.** IPS guide L48-50 names exactly these four approaches (operating commitment, reserve composition, facility
contribution, flexibility) [VRF]; without rule 4, tests 2 and 5 have no rule (D8 M235) [INT]. Rule 2 passes on
governance (the risk held equals the risk stated), not on a lift in the median (AY2 D8 C7) [INT].
**Numbers.** 4 rules × 25-35 words + governance 10-15 ≈ 110-155 words (D8) [INT]. Without a rebalancing rule the growth
money's stock share wanders to p5/p50/p95 50/62/73% by 2031 (D8 script) [MODEL].
**Side effects and cost.** About a quarter to a third of the 500 words.
**Touches.** IPS.
**Complexity.** Four rules is the smallest set that covers all five case tests; each extra candidate (ratchet, calendar
glide path, TWD quote, tilts, funded-ratio trigger) failed the lift test (D8 M235; D3 M055) [MODEL/INT].
**Confidence.** High on structure; parameters as in P5/P7.
**Team decides.** Every bracketed parameter, by Nov 6 (a rule whose parameter is chosen later is a redesign, D8).

### P12. Fees: one cost principle, no number

**Change.** One IPS clause (elements): the bought payments are held directly to maturity with no ongoing charge; every
cost is paid from the growth money, so costs can never reduce the promise; low-cost broad funds as a principle. No fee
number in the IPS. **First clause to cut** if the IPS runs over its word budget (AY2 D8 C13).

**Why.** The case has Laura invest "with an asset management firm" (L43, R-C26) but names no fee [VRF]; no projection
in the repo carried a fee (BS-01) [VRF]. The Asset Manager Code (which the Rules page tells teams to "operate by",
R-W29) recommends plain fee disclosure (F.4.d; "should provide" gross and net returns) [VP via D8, verb per AY2 C11].
A fee taken from the ladder breaks full funding (AY2 D8 C5) [INT].
**Numbers** (`strategy_mc_v2.py` (c); `D8_practice_numbers.py`) [MODEL, ASM fees]: fund expenses (~0.05%) cost about
$0.3k of median; a 0.5% advisory fee on the growth money -$5.3k; 1.0% -$10.2k; 1.0% on all assets paid from the growth
money -$32.4k; with the deposit missing, fees on everything exceed the leftover money in 100% of paths. A typical U.S.
adviser at this size charges about 1.00% (Kitces reporting the 2017 Veres survey, VP; dated) [VP, ASM for 2026].
**Side effects and cost.** About 15-20 words. It is a team policy assumption, not a case fact.
**Touches.** IPS. TN: none (WInS costs are $25 per ETF trade, $10 per bond trade, F-607 [VP]).
**Complexity.** Low value per word; keep only if words allow.
**Confidence.** Medium (principle high; its scoring value unknown).
**Team decides.** Keep or cut.

### P13. Which book WInS shows: vote (ii) or (iii) before the first order

**Change.** Take the vote now (ticket gate box (b)); no book is decision-ready without its conditions:
- **E1 lean: option (ii)** (the plan's mix after both deposits, scaled to $300,000), **conditional on** (1) one IPS
  sentence carrying three elements (ticket v0 section 2 / v1 section 1): the post-2028 mix; scaled to $300,000 with the
  Treasury part set to the payments' rate sensitivity (about 10 years); and the fact that in January 2027 almost all of
  her real $300,000 buys the ladder; (2) each promise-money and growth note (or its reflection) marking the scaling
  ("after both deposits" / "after her 2028 deposit" as content, ticket v1 C2); (3) no note calling the holdings
  "Laura's portfolio" (Asset Manager Code F.2 truthful disclosure, via D10) [VP].
- **Alternative: option (iii)** (her literal January 2027 book, ~98% Treasuries), **conditional on** naming a genuine
  third executed trade in advance: the 2027 leftover in a T-bill fund (SGOV, alternates BIL then SHV, ~1.5%, bought in
  the same session as the hedge, the plan's own T-bill rule), or a dated Treasury rung if WInS lists one (P14); if
  neither is listed, (iii) cannot promise three executed trades, so choose (ii) (AX2 D10 C1, blocking; ticket v1
  section 2) [VRF].
- **Decision test** (T1, adopted): choose (iii) if the team cannot state the (ii) scaling in its own words in about 30
  IPS words. **Cap rule** (ticket v1 section 3): if Session Rules show a single-security cap below 25%, (iii) needs 5-6
  Treasury funds, so switch to (ii) and re-vote, unless a separate higher bond limit and a listed Jul-Dec 2037-2041
  Treasury let one bond carry the excess [MODEL/derived, T1 script].
- E1 and T1 reached the same lean independently from the same evidence (T1: "(ii), medium-low confidence").
- Correct the internal description (CLAUDE.md, brief section 7): "~65% Treasuries / ~35% equity" is hedge / growth money,
  not bonds / stocks; at 50/50 the book is hedge 66% / VT ~17% / VGSH ~16% / cash 1% (F-409; ticket section 2) [VRF].

**Why (both sides; the rules decide neither).**
- Neither book breaks a published rule under no cap, a 35% cap or a 25% cap; Vanguard volumes and caps below 25% are
  unchecked (D10 with AX2 C2) [VP rules; derived]. The binding requirement is consistency: "Your portfolio and Final
  Report should reflect the strategy established in your IPS" (IPS guide L75) [VRF].
- For (ii): the TN guide asks the notes to show the team's "approach to growth, risk, liquidity, funding reliability,
  financial flexibility, and future cash-flow needs" (L4-6) and a "cohesive portfolio strategy" (L14-15) [VRF]; (ii)
  gives three honest role words (future funding, growth, risk management/liquidity, D12) and "funding purposes" as a
  visible kind of diversification (R-AN45) [VP]; "The WInS portfolio represents each team's implementation of its
  investment strategy during the competition" (L129, R-C75) [VRF].
- For (iii): WInS starting cash equals her first deposit exactly and the $150k "will not be added to WInS" (R-AN14,
  SMApply, VP), so (iii) is the only book true at a stated date without scaling; the pitch rule (P1) is visibly true in
  the holdings; its IPS sentence is shorter (~12-20 words vs ~25-30) (D10) [VP, INT].
- Against (ii): WInS shows ~17% stocks while her real 2027 money holds ~0% (equity gap +17.0 points at 50/50) and the
  $198k hedge is 68% of the $292k promise, so every hedge note needs a scaling clause (D9 M012; AY1 [5]) [derived].
- Against (iii): with no cap it gives two orders only; all notes are promise or liquidity notes (no growth decision is
  shown in WInS); ~98% Treasuries may read as timid for a client "willing to take thoughtful risks" (S3; D13c N1) [INT].

**Numbers** (ticket v1 sections 1-3, `T1_ticket_v1_numbers.py`; issuer durations IEF 6.86y, TLH 11.58y on 9/25, VP).
(ii) at 50/50: IEF 23.5% / TLH 42.5% / VT 17.0% / VGSH 16.0% / cash 1%, 4 trades, ~$100. (iii): IEF 34.9% / TLH 63.1%
/ SGOV ~1.5% (~$4,500) / cash ~0.5%, 3 trades, $75; the T-bill leg earns about $18 in the WInS window against a $25
commission, so its reason is the plan's rule, never WInS profit (T1, ASM) [VP prices; derived]. Leftover $4,438-6,636
(1.5-2.2%) before commissions (D10). Securities and alternates (ticket v1 section 12, issuer pages re-read 2026-09-28,
VP): VT (alternates VTI 62% + VXUS 38%, or ITOT + IXUS); VGSH (SHY, or a WInS-listed ~2-year Treasury note); TLH (IEF
+ TLT at duration weights: 40.9/25.1 under (ii)); SPTL (VGLT); SGOV (BIL, SHV). On the 2025-26 list (history only,
VRF): IEF, TLT, VT, VTI, VXUS, VGSH, SHY, BIL, SHV yes; TLH, SPTL, VGLT, VGIT, ITOT, IXUS, SGOV, IBTM no. All PENDING
WInS AVAILABILITY + POSITION-LIMIT CHECK.
**Side effects and cost.** (ii) costs about 25-30 IPS words and 15-20 words per affected note; (iii) costs TN variety
and needs a pre-named third trade.
**Touches.** WInS-now (tier 1), TN, IPS (one sentence naming the date or state WInS represents, required under either
option).
**Complexity.** Either is one sentence of explanation; (ii) is one more trade type to explain. Earns its place either
way because the sentence is required.
**Confidence.** Medium-low on the lean (a judgement; D10 leaned (iii); S3, D12 and T1 lean (ii)).
**Team decides.** (ii) or (iii), recorded with first names, date and reason in the decision log before the first order.

### P14. The three Trading Notes plan (WInS-now and TN)

**Change.** Replace blueprint 01 section 7's planned "discipline/rebalance trade" (D7: no sensible band fires before
Oct 23) with notes drawn only from trades that happen anyway. The slot table, note checklists and banned-word lists are
already in ticket v1 sections 4-7 (T1); this proposal endorses them, with the points below. Also adopt v1's hedge
re-mix band of **±0.25 years from the starting mix** (the old fixed 9.65-10.15 band clashed with the capped mixes at
about 10.5 years; v1 change 5).

**Plan under option (ii)** (orders in one session, hedge first; target fills by Fri Oct 2 ET once the gate is passed):
1. **Hedge note** (TLH, or IEF; SPTL only if a cap forced it, and then it is *not* a "refined" decision, AY2 D7 C1):
   role word "future funding"; its "tested" evidence lives in the reflection.
2. **Growth note** (VT): role word "growth"; only money the promise does not need; a fall shrinks the facility range,
   never the payments; the split stated only if final (P5).
3. **Short-Treasury note** (VGSH): role word "risk management" (of the growth money) or "liquidity"; "short-Treasury
   part of the growth money"; never "the floor", never "already owned" before 2031 (AY2 D9 C1; AX2 D2 C6).
   Alternative third note only if genuine: a research-based change of the split announced in advance (the honest
   "refined" route, D7), or a band trade in a crash.
   A dated rung is optional under (ii) and not recommended (a second "future funding" note; complexity) (AX1b item 7).

**Plan under option (iii):**
1. Hedge note (TLH or IEF, as above; under (iii) it may carry the ~$292-294k price of the payments in one clause,
   because the order is that size).
2. **The 2027 leftover in SGOV** (alternates BIL, SHV; "liquidity"), bought in the same session as the hedge, a plan
   rule, $25 (ticket v1 section 2). One reflection under (iii) must answer "why so little equity": in January 2027
   almost all of her real $300,000 buys the payments, and room for stock risk starts with the 2028 money (D13c N1).
3. **Dated rung** if the WInS Bonds drop-down lists a U.S. Treasury maturing July-December of 2032-2041 (best: the
   4.125% note of 15-Nov-2032, CUSIP 91282CFV8, parent of the ladder's first STRIP), face $50,000, funded from IEF, one
   $10 trade; the 2032 note raises TLH, so skip it under a cap below about 69%, and under a cap below 44% only a
   2039/2040 bond with no new fund (D1 M044 with AX1b items 5-9; ticket v1 section 7) [VP via S1 MSPD; MODEL prices].
   Its reason is implementation (the promise is dated), not display (AX1b item 8). Otherwise the third note is the IEF
   buy (weaker: same role). IBTM (Dec-2032 iBonds) is the last rung fallback and its note must not say "repays
   $50,000" (iShares: the funds "do not seek to return any predetermined amount", VP via AX1b).

**Note element spec (every note; the team writes the words).** Use the ticket v1 section 5 core, which maps the
Guide's four elements (reasoning, alignment, supporting research, role; Guide L84-86) [VRF] into about 300 characters:
C1 one Guide role word plus the fixed team label (alignment); C2 Laura's dated need (reasoning; under (ii) fold the
scaling in: "after both deposits" / "after her 2028 deposit"); C3 one dated research fact with its source named in words
(prefer a price or issuer figure over a forecast); C4 the main risk accepted or the rule that governs it. If a real
limit forces a cut, keep C3 and drop C4 to the reflection (AY1 D12 C1: the Guide names research, not risk).

**Reflection spec (≤100 words each; TN guide L46-52)** [VRF]: answers the three official questions (why; alignment;
how it served her goals, funding needs or risk). The "tested" evidence sits inside them (about 20-25 words): the
10-year rate move over the **pre-registered window** (fill date to the Oct 20 close), the hedge's % change and the
payments' % change on the same dates, and what the rule said to do (hold). Report small moves or poor tracking as they
are; never pick the best day (AY2 D7 C2). No Laura quotes (D13).

**WInS-now checks** (all but (f) are already in ticket v1 gate boxes (b)-(d) and section 10; tick before the first
order):
- (f) split decided (P5) if option (ii) (v1 gate box (b) allows "provisional 60/40, decision by [date]"; E1 prefers a
  final decision now);
- (g) note-box limit checked at zero risk: type a long test text on the order-review screen without pressing Confirm,
  or ask Stock-Trak/Wharton; until seen, draft notes to 300 characters (a sister product's limit, VP for
  HowTheMarketWorks, UNVERIFIED for WInS; Wharton's own example is 413 characters) (AY1 D12 C2);
- (h) screenshot the Bonds drop-down, list Treasuries maturing 2032-2042, record the bond position limit and accrued
  interest (D1);
- (i) data capture: screenshot WInS position values on the fill date and on Oct 20; Treasury curves can be pulled later
  from treasury.gov; value the payments with `D3_funded_status_log.py`, `A2_curve_recheck.py` (spot) or
  `D9_numbers.py` [3], not
  `official_curve_pv.py` (fixed to 2026-09-25) (AY2 D7 C5); check IEF/TLH ex-dividend dates in the window.

**Vocabulary for notes** (D9 M062 with AY2 fixes): WInS Treasury funds "move like / stand in for" the payments; never
"match", "mature in her payment years", "stable", "reduce volatility", "safe", "guaranteed", "risk-free"; never
"known" or "locked" for 2028 rates (AX2 D2 C1); never "halves AI exposure" (AX2 D2 C5); never "the operating reserve"
for WInS holdings (the case creates it in 2033, L94-95) [VRF].

**Why.** "Supported, tested, or refined" is a menu, not a quota (TN guide L12, L29-30; case L152) [VRF]. Staging a trade
to fill a category risks misstating the reasoning (R-W28 reading, INT per AY2 D7 C11). Notes cannot be edited
(Stock-Trak, VP via A4) and are quoted "exactly as it appears in WInS" (TN L44) [VRF]. Wharton's example note has no
number, date or source (59 words, 413 characters; D9) [VRF, derived].
**Numbers** [MODEL]: a 10-year move of 10bp or more between an Oct 1 fill and Oct 20 has about a 53% chance at the end
date (D7, realised 2026 volatility 4.45bp/day [VP inputs]); 10bp moves the payments' value about 1% (~$2,890; DV01
$289, F-103 [VRF]); in 2026 an IEF/TLH hedge stayed within ±0.42% of the payments' % change in 95% of six-week windows
(a lower bound; expect ±0.5-1% with real fund noise, D3 M028) [MODEL on VP inputs]; band firing before Oct 23 is very
unlikely (about 0-2% even in a crisis, AY2) [MODEL]. Role test for +1pp in rates: IEF -6.9%, TLH -11.6%, VGSH -1.9%,
payments -10.2% (D12) [VP durations, derived].
**Side effects and cost.** One extra rung trade ($10) under (iii) if listed; ~10 minutes a week of logging.
**Touches.** WInS-now, TN.
**Complexity.** Removes one planned trade; adds checks. Earns its place.
**Confidence.** High on method; the rung depends on WInS listings (unknown until logged in).
**Team decides.** Which three executed trades become the notes (after Oct 20); who writes and who second-reads each note.

### P15. Decision log, evidence grades and AI-use log from today

**Change.** Start now (WInS-now): one row per trade and per "decided not to trade" moment, with columns: date/time
(ET); ticker, side, shares, fill price; note text exactly as WInS shows it; role word and team label; Laura need;
fact, source and **grade** (CASE / PRICED / HISTORY / ASSUMED, D12 M231); risk and rule; **provisional IPS rule name**
(e.g. "Rule 1", D9 M212); note candidate? Also a dated AI-use log (tool, date, purpose) for the Works Cited (R-W46,
VP). No student surnames or personal data (CLAUDE.md).
**Why.** Consistency across the three deliverables is required (case L161-162, R-C92) and is cheaper to record than to
reconstruct (D9) [VRF, INT]; Articulation needs true process evidence and forbids invented stories (R-S27, R-W28)
[VRF/VP]; the AI policy requires the record [VP]. Parked M021.
**Numbers.** None. **Side effects.** Minutes per trade. **Touches.** WInS-now, TN (feeds reflections), IPS (rule
names). **Complexity.** Process only; earns its place. **Confidence.** High (value depends on the team keeping it).
**Team decides.** The log owner.

### P16. IPS format: word budget, page fit, paraphrase test

**Change.**
1. **Word budget** (owner: whoever writes `ips_spec.md`; AY2 section 5 merged with P1-P13) [INT]:

| Element | Words (estimate) |
|---|---|
| Opening: central idea + what/why (P1) | 30-40 |
| Certainty definition + two gaps + inflation/currency assumption (P2, P8 items 3-5) | 45-60 |
| Rule 1 promise first, incl. rates-fall, deposit and joint-tail branches (P3, P4) | 40-55 |
| Risk by goal + where risk sits (P6) | 35-50 |
| Rule 2 growth mix + its reason (P5) | 25-35 |
| Rule 3 2031 range method (P7) | 30-40 |
| Rule 4 2033 order of use + reserve composition + flexibility (P8, P9) | 35-45 |
| Governance + review + no rebalancing between reserve and growth money (P10) | 20-30 |
| Three trade-offs, inside the rules' "because" clauses (P11) | 0-30 |
| WInS sentence ((ii) 25-30; (iii) 12-20) (P13) | 12-30 |
| Fee principle (P12; cut first) | 0-20 |
| **Total before connecting words** | **about 270-435** |

2. **Page fit:** 50 + 500 words in Times New Roman 12, double-spaced, 1-inch margins leaves 0-2 spare lines on U.S.
   Letter at Word's "Double" (27.6 pt, about 525 IPS words at most) and fails to fit reliably with 7 paragraphs; Wharton's
   own sample is set at 24 pt (8-10 spare lines) (D9; AX2 D10 C3) [VRF measured, ASM line heights]. Spec: paragraph
   spacing 0, no blank lines, no tables or bullet lists, about 470-490 words or fewer, and the **exported PDF** must end
   on page 3; "Exactly 24 pt" is a defensible reading if a draft overflows (INT; the team decides). Non-compliance means
   "will not be considered for semifinal selection" (IPS guide L82-83, R-I39) [VRF].
3. **Paraphrase test** of the pitch and the rule sentences with 6 unpaid readers (3 without finance, 3 with), two rounds
   (about Oct 26-30 and Nov 2-3), readers restate only and never supply words; change a sentence if 2+ misread it or
   anyone gets "what happens to the payments if stocks fall by a third", "what if rates fall before January 2027" or
   "what could still stop a payment" wrong (D12 M234; digital.gov method VP). Unpaid adult help is allowed; paid help is
   not (R-W21) [VP].

**Why.** A breach of the page rule excludes the team regardless of strategy quality [VRF]. **Touches.** IPS.
**Complexity.** Process; earns its place. **Confidence.** High that the layout is tight; medium on exact line counts.
**Team decides.** Letter vs A4, the spacing reading, the reader list.

### P17. What NOT to put in the IPS (checklist)

- Any dollar range, reserve calculation, percentile, miss rate, probability to a decimal or model output (IPS guide
  L68-69; D9 number policy) [VRF]. At most one rounded, dated price fact, graded in words.
- "Bought in January 2027" as a flat claim; "fits inside $300,000"; "by 1 January 2028 at the latest"; "at most part of
  the first payment" (P1, P3).
- "Guaranteed", "risk-free", "100%", "95% certain", "safe", "matched" (for WInS funds), "locked" or "known" for 2028
  rates, "only the facility shrinks" (joint tail).
- Charts, images, tables, footnotes, links, formal citations, framework or code names (LDI, GBWM, Chhabra, CFA, APRA,
  Kresge), house names for return forecasts ("two major published forecasts" is enough) (L123, R-I55) [VRF].
- Laura quotes; the pull quote as hers; "floor-first leap"; her career-regret line as the reason for stocks; "risk-averse";
  identity, heritage or Taiwan as a reason for any holding; book-title or "falling"/"balance" puns (the case's own
  "appropriate balance" is fine) (D13 rules) [VRF].
- The statistics degree more than once across the TN and IPS together (pick one place; E1 suggests the certainty
  definition; ticket v1 has already removed it from the VT note checklist) (AY2 C6) [INT].
- "Our portfolio manager/advisor approves"; org chart; firm name or size; reporting frequency; a residency-delay trigger;
  a "funded ratio below 100%" trigger (P10, P9).
- Tickers, weights to decimals, CUSIPs, fund durations to two decimals ("about 10 years" is the honest precision, S4)
  (IPS guide L51-52) [VRF].
- A fee number; a TWD figure; any NT$ conversion or hedge plan; an EWT or AI tilt.
- Guide p.5 quoted as a reason against staging or against changing the split before Nov 6 (AX2 D2 C3; AX1b item 4).
- WInS P&L, rank or "our winning trade" (Guide p.3: WInS "is not the competition scorecard") [VRF].
- The $150k described as uncertain beyond one labelled stress-scenario clause (the case says "will", R-AN35).

---

## 3. Conflicts E1 could not fully resolve (both sides; the team decides)

| # | Conflict | Side A | Side B | E1 view |
|---|---|---|---|---|
| C1 | WInS book (ii) vs (iii) | (ii): S3, D12, T1 (three roles; shows growth; "funding purposes" diversification; TN guide L4-6, L14-15; copes better with a cap under 25%) | (iii): D10 (true at a stated date; shortest IPS sentence; pitch rule visibly true; R-AN14) | Lean (ii) at medium-low confidence; (iii) needs a pre-named third trade (AX2 blocking) |
| C2 | Growth split 50/50 vs 60/40 | 60/40: D6 rule under JPM; D13c/D9 M071 (a "take the jump" client; do not look timid); CLAUDE.md provisional call | 50/50: D2 (flat median across houses; better p5 and 2031 floor p5); D8 M109 (stocks are for upside, not need; -$41-56k bad case vs +$11-14k middle, AY2) | E1's test (P5) favours 50/50: it is the largest share passing D6's own rule under both houses with a modest fee. The conflict remains a judgement about how much weight JPM deserves |
| C3 | Cap the 2033 gift at the top? | Cap (D3 M039): "within the range" becomes certain barring default; model needed only for P(top reached) (~1 in 5 at p80) | No cap (D5 M107, AY1): a capped "100% within" is empty for a statistics reader; uncapped answers R-C70 and misses only upward (excess median $2k, p95 $8k) | No cap (fewer rules, informative confidence). If the team caps, report "P(top reached)", never "P(within) = 100%" (AY1 X11) |
| C4 | 2031 slices | 80/10/10 (verified model's 80% floor; D6 behavioural 80-90%; D4 needs ≥70% locked; higher bought bottom, R-C64) | 70/15/15 (D5: more flexibility, ~15%, anchored to 3-4 years of building-cost drift; more growth to 2033) | Default 80/10/10; both pass the width test (1.15x vs 1.26x). A judgement between credibility and flexibility |
| C5 | Top percentile q | 80 (D3), 85 (D5, "about 1 in 7") | 90 (D6, "about 1 in 10") | 90 for the roundest honest statement; q barely moves the top because the at-risk slice is small (D5) |
| C6 | Third note under (ii) | VGSH buy (D12: the only "risk management" role; ticket) | Dated rung (D1: a checkable dated cash flow) | VGSH under (ii); rung under (iii) (AX1b item 7) |
| C7 | VGSH role word | "risk management" (D12, the Guide's word, checkable with a number) | "liquidity" / "a different funding purpose" (ticket); "flexibility" as the echoed trait (D6/AY1) | Compatible: one Guide role word, echo "as the project develops", never "the floor" |
| C8 | Flexibility money after 2033 | Short Treasuries (D8 M081: flexibility is closer to safety) | Stays invested for growth / "ventures second" (team notes; CLAUDE.md call 3 wording) | Short Treasuries; no case line supports growth for this money |
| C9 | Longest-first ordering (values) | Longest-first (D1/D3: one-third of the top-up price risk; less face unfunded if the deposit never comes) | Its shortfall falls on the residency's first operating year (AX1b item 23) | Longest-first on the numbers; name the counterpoint in the team's own risk discussion |
| C10 | Note length | Plan to 300 characters (D12, a sister product's limit; ticket v1 four-element core) | No WInS limit is published; Wharton's example is 413 characters (AY1 D12 C2) | Draft to 300 as a precaution and check the box at zero risk before the first note; if a real limit binds, keep the research fact and move the risk to the reflection |
| C11 | Fee clause in the IPS | Keep a principle (D8; BS-01; Asset Manager Code) | Cut first if over budget (AY2; the case is silent) | Keep only if the PDF test leaves room |
| C12 | Whole-portfolio stock share in the IPS | Show it by stage (M033; AY1 D6 C4) so a first reader sees the design | Leave it out; it draws attention to "timid" (INT) | Optional clause; the per-goal statement (P6) is the required part |

Resolved during this synthesis (no longer conflicts): the gap odds ("about 1 in 3" for the real ladder; "1 in 4" only
for the exact-date ideal, AX1b); Guide p.5 applies after the IPS, not before (AX2, AX1b); D8 rule 1's joint-tail wording
(P4); D8 rule 3 must include the give-back share (AY1 X9; P7); the lock-share dispute between D5 and D6 is one number
measured two ways, s(1-a) (AY1 X1); the page-fit estimates of D9 and D10 agree once whole lines and 27.6 pt are used
(AX2 C3); the sleeve-bond model input is market-consistent (~4.8-5.0%), not the old ticket's 3.5-3.9% (AX2 C8; withdrawn in
ticket v1 change 17); the WInS 50/50 weights are VT 17.0 / VGSH 16.0 / cash 1, not 16.5/16.5 (ticket v1 section 1).

---

## 4. What the team must decide, in date order (checklist)

**Before the first WInS order (target this week; fills by Fri Oct 2 ET):**
- [ ] Gate (a): vote on lock-early (first names, date, reason in the log).
- [ ] P13: option (ii) or (iii), with its conditions.
- [ ] P5: split 50/50 or 60/40 (only if (ii)).
- [ ] Gate (c)/(e): Session Rules screenshot (single-security limit; whether ETFs and bonds are covered) and the cap
      branch.
- [ ] P14 (g)/(h): note-box limit checked at zero risk; Bonds drop-down screenshot (rung decision under (iii)).
- [ ] Gate (d): each note drafted by one student to the P14 element spec, read by a second student.
- [ ] P15: decision log and AI-use log started; roles assigned (trader, note-writer, second reader, log owner).

**By Oct 20-23 (Trading Notes):** data capture on the fill date and Oct 20 (P14 (i)); choose three executed trades;
reflections to the P14 spec; consistency check against the provisional IPS rule names.

**By about Oct 26 (first IPS draft):** P1-P12 parameters fixed: pitch elements; certainty definition wording; rule 1
branches; split and band; a, s, q and cap; flexibility composition; review points; fee clause in or out.

**Oct 26-Nov 3:** P16 paraphrase rounds and PDF page-fit test on every draft. **Nov 6, 5:00 p.m. ET:** submit; no
"tidy-up" trades in the last days (ticket).

---

## 5. Later (after Nov 9), one line each (Final Report; not worked here)

- The 2031 range in dollars at the median and weak/strong 2031 states, "likely figure" vs midpoint (D5, D6, E1 [4]).
- The price-of-certainty and riskless-control comparison (~$204k, D3 M034) and the rejected-alternatives table.
- Named historical rows next to the model's p5 (D3 M059).
- Fee assumption and net-of-fee projections (D8 M026, D3 v2 (c)).
- NT$ reference with date and rate; building-power assumption line (D4).
- Fundraising-excerpt checklist and the operations-first lead (D5 M094; M008, M015).
- Reserve at market value on 1 Jan 2033 and the CUSIP-level ladder (S3 Final-Report file).
- At most one or two dated Laura quotes in context (D13a/D13c).
- The decision-log traceability table (D9 M212) and the paraphrase-test log (D12 M234).

---

## Sources (accessed 2026-09-27/28; web sources were read by the specialists and re-opened by the auditors as cited)

Official, in the repo (VRF): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L16, L38-45, L61-74,
L83-120, L126-149, L152-169); `2026_WGY_Investment_Policy-FINAL.txt` (L3, L16-26, L35-36, L45-78, L82-125);
`2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L4-31, L36-53); `2026_WGY_Investment_Competition_Guide.txt` (L84-90,
L154-159, L183-184); `SMApply_Deliverables_Page_2026-09-27.md` (L49-57).

Market data (VRF): `competition/official_market_data/daily-treasury-rates_2026-09.csv`;
`JPM_LTCMA_2026_US_matrix_USD.pdf` p.2.

Primary web (VP, as cited through the specialist files and audits): SMApply Trading Details and FAQ
(https://wghsinvcomp.smapply.us/res/p/trading/, /res/p/faqs/); Wharton Rules & Roles and AI policy
(https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/, /ai-policy/); 2026-27 WInS User
Guide (https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf); Vanguard VCMM
forecasts (https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html); FRED DGS10,
DEXTAUS; treasury.gov 2026 par-curve CSV; iShares IBTM page; CFA Institute *Investment Risk Profiling* (2020), *Elements
of an IPS for Individual Investors* (2010), *Asset Manager Code* (2nd ed.); Weber, Blais & Betz (2002) abstract; Thaler &
Johnson (1990) abstract; Du et al. (2011) abstract; Kitces (2017); Chhabra interview (WealthManagement.com, 2016);
digital.gov paraphrase testing; HowTheMarketWorks trade-notes page. Full URLs are in the cited specialist files.

Secondary / snippet (SNIP): Moody's Aa1 downgrade date (Wikipedia); Taiwan 2-year yield 1.66%; multpl CAPE.

Research files (lower authority; numbers reproduced by their auditors): `research/insight_v1/phase_D/*.md` (D1-D12, D3
model v2, D13a-c, four audits), `phase_D/trading_now_brief.md` (T1); `wins_now/securities_and_allocation_v1.md` (the
ticket, supersedes v0), `securities_and_allocation_v0.md`, `S2_growth_sleeve.md`, `S4_red_team.md`;
`phase_A/{case_register,fact_register,stakeholder_map,wins_week1_guardrails}.md`; `phase_C/survivors.json`,
`parked.json`; `research/council_2026-09-27/01_chair_memo.md`, `round2_referee_ruling.md` (history).

Scripts: `research/insight_v1/scripts/E1_split_and_slices.py` (new); re-used outputs of `T1_ticket_v1_numbers.py`,
`D1_purchase_rule.py`,
`D1_wins_rung.py`, `AX1b_rates_audit.py`, `strategy_mc_v2.py`, `D3_*.py`, `D2_equity_premium.py`,
`D4_facility_purchasing_power.py`, `D5_range_and_flexibility.py`, `D6_behavioural_numbers.py`, `AY1_audit_checks.py`,
`D7_rule_trigger_odds.py`, `D8_practice_numbers.py`, `D9_numbers.py`, `D9_ips_page_fit.py`, `D10_*.py`, `D12_*.py`.

---

## What this teaches

1. **A strategy is mostly its rules, not its holdings.** The portfolio barely changes in these proposals. What changes
   is that every "we would probably..." becomes "if X happens, we do Y", decided before anyone knows whether X happens.
   That is what lets a plan frozen on Nov 6 still be applied honestly in December.
2. **When experts disagree, find the number they are each holding fixed.** D2 and D6 argued 50 against 60 because they
   trusted different forecasters; D5 and D6 argued about the lock share because each held a different give-back share.
   Running the same rule under both assumptions turned two arguments into one test.
3. **Say what you control.** "The payments are bought in January 2027" depends on interest rates; "nothing takes stock
   risk until the payments are bought" depends only on the team. Promises built on rules survive bad luck; promises
   built on dates do not.
4. **Honest gaps are part of the answer.** Naming the January price risk and the nominal-dollar gap costs a few words
   and removes the two objections a careful reader would raise first.
5. **Complexity must earn its place.** Each proposal says what it costs in words or trades. Anything that did not move
   a number a reader cares about (a ratchet, a barbell, a Taiwan tilt, a staged purchase) stayed out.
