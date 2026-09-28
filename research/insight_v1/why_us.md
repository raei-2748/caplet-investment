# Why us: why would Laura choose our firm's strategy over the other firms?

1. Our edge is not "buy the payments first". That is the textbook answer, and many teams will give it (M011, INT). The edge is the Laura-specific rule: each deposit buys one promise when it arrives.
2. Her first deposit buys the ten operating payments. Her second deposit, which is her own career income, buys the building's minimum in 2028 (case L43-45, L91-92, VRF).
3. On one set of model paths, this design (REC) has about the same middle as the 2031-lock design (ALT) and better bad cases: total p5/p50/p95 $182k/$207k/$250k against $168k/$210k/$266k (MODEL, E6 [2], re-run 2026-09-28).
4. It loses on median gift, stock exposure and p95. The simulated client (E3) would choose the firm on substance but could be won by a rival with the same plan in plainer words. So the edge only counts if the words carry it.
5. Limits: every "Laura" here is a simulation grounded only in the case and her verified public words. A blind contest (section 0 below) ranked our strategy first with all 3 simulated evaluators; E2 scored the older E1 design, not this spec.

**Serves:** TN (Oct 23) and IPS (Nov 6). This file holds reasons and evidence only. None of it is text to submit, and the team writes every word.

**Labels:** VP = VERIFIED-PRIMARY; VRF = VERIFIED-REPO-FILE; SNIP = SNIPPET-UNVERIFIED; ASM = ASSUMPTION; MODEL = model output from assumptions, not a forecast; INT = judgement; SIM = simulated-client reaction (a kind of INT, never a fact about Laura). Case lines refer to `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`. E6 [n] is a section of `scripts/E6_final_checks.py`. W3 re-ran it on 2026-09-28 and every figure below that cites it matched. Every ticker named here is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK**; primaries and alternates are in `securities_and_allocation.md` s1-s2. **R1-R8 in this file are reasons, not the spec's decision rules R1-R10** (those live in `ips_spec.md` s(c)).

---


## 0. Blind "Laura's Choice" contest (added 2026-09-28 by the main loop)
**Serves: IPS (strategy choice) and TN (what the notes must show).** Files: `phase_E/tournament/` (firm_A-F.md,
fairness_log.md, eval_L1-L3.md); numbers for the rival firms: `scripts/E7_tournament_field_numbers.py` (MODEL).
Six anonymised one-pagers (300-380 words, same seven sections, loaded words and tells removed by a fairness auditor):
ours (Firm D, the E6 REC design) and five rival approaches (A: typical strong team with a Monte Carlo 95% and staged
reserve; B: growth-first 75% equity; C: themed/values tilts; E: generic 60/40 to 40/60; F: complex optimiser).
Three evaluators (simulations of Laura, grounded ONLY in the case, D13a VERIFIED-PRIMARY lines and the D13c voice map)
ranked all six, each reading them in a different order.

| Evaluator | Ranking (1st -> 6th) | Score for ours (/10) | Next best |
|---|---|---|---|
| L1 | D, A, E, F, C, B | 7.5 | A 6.0 |
| L2 | D, A, E, F, C, B | 8.0 | A 6.5 |
| L3 | D, A, E, B, F, C | 8.0 | A 6.0 |
Borda total (6 points for 1st ... 1 for 6th): **D 18 (maximum)**, A 15, E 12, F 8, B 5, C 5. Ours was first 3/3.

**Why they chose ours (their reasons, with the evidence they cited):**
- The 2031 bottom is money she already owns, so she cannot overpromise (case p.3 credibility warning, L114-115).
- It is the only plan whose payments do not depend on markets until 2033: the market-based plans miss a payment in
  0.3-3.2% of model paths, 7-14% if the 2028 deposit is $75k, and 41-46% if it never arrives (MODEL, E7/strategy_mc) -
  and that deposit comes from income she herself called "unstable" (B8b-Q18, VERIFIED-PRIMARY, Overachiever 2021).
- It names its own costs and gaps (the ~1-in-3 January price risk, the joint tail, lower far upside), which matches how
  she talks about unfinished work and costs (B8b-Q18, B9b-Q09) and her line about not letting down "people who were your
  earliest supporters" (D13a-N01, student-era, Daily Pennsylvanian 2016).
- Medians are nearly equal across plans (ours $207k vs A $206k, E $213k; MODEL), so the market plans mainly buy far
  upside at the price of payment risk.

**What all three said ours must still fix (actions for the IPS; the first is the most important):**
1. **"Appropriate balance" is not yet shown** (case L69-74; her "take the jump" line B1b-Q11): stocks average 7.5% of
   all her money 2028-32. State where the leap is (the residency itself; the growth money takes the market risk), give
   the price of certainty in one line (median about equal to the typical plan, give-up only at the far upside: p95
   $250k), and show one tested alternative with a smaller 2028 floor and more in stocks, so the choice is visibly a
   choice. -> team decision D-open (see open_questions.md).
2. **Call the $150k bond the bought floor of the 2031 range, not a "minimum facility contribution"** fixed in 2028 (case
   p.3: no predetermined contribution; flexibility as the project develops) (L2).
3. **State the in-range confidence directly** (case L117-118): under the cap rule the 2033 contribution always lands
   between the owned bottom and the announced top, barring a U.S. default; keep ~73% (model) / 84% (history) only as the
   chance of reaching the top (L1, L3). Say how meaningful a ~$150k-$175k range is (case L111-112).
4. Already in the spec, but must be visible in the IPS: the joint-tail rule (payments first, the floor shrinks, stated
   in dollars; R1-R2) and both certainty gaps (nominal US$ vs Taiwan costs; the inflation assumption; what a fixed $50k
   buys by 2042; case L90, L146-147).

## 0. Honest limits (read first)

- **E3 is a simulation.** Its "client" was built only from the case (VRF) and from D13a VERIFIED-PRIMARY lines used in their context. It is not Laura, and nothing from it may be attributed to her (E3 "How to read").
- **E3 reviewed E1's design, not the final spec.** E1 was the 2031 lock (now ALT). The final REC design came from E4 and E6. So the client-seat verdict covers:
  - the shared core (payments first, certainty by price, named gaps);
  - wording findings that E6 adopted.

  It does not cover REC's 2028 minimum, its cap or its lower stock share (INT).
- **E2 scored E1 as specified:** 7/7/7/5/6 = 32/50, and about 38/50 after its ten fixes (INT). E6 adopted most of those fixes, but no reader has scored the E6 spec.
- **A lean blind contest was run after this file was first written (see section 0).** Three independent simulated-Laura evaluators, each reading six anonymised one-page strategies in a different order, ranked ours first. It is still a simulation (3 evaluators, archetype rivals modelled on one engine; see `phase_E/tournament/fairness_log.md`), not Laura's view.
- **The "rival" became our recommendation.** E4's strongest rival design was adopted as REC. The rivals left to beat are archetypes (growth-first, all-Treasury, the 2031 lock, a same-plan team with better words), not real teams.
- **The model has thin tails** (AX1 C12, VRF audit). That is why history windows are shown beside it. The results also depend on the return input: JPM AC World 7.00% compound (VRF). On a Vanguard-like 5.08% input, REC is $179k/$202k/$242k (E6 [4], ASM hybrid).

---

## 1. The reasons, with evidence, the rival each beats, and where it is close or loses

| # | Reason (content, not wording) | Evidence (status) | Rival it beats | Where it is close or loses |
|---|---|---|---|---|
| R1 | **Once bought, the ten payments depend neither on markets nor on her next contract** | Fixed $50k payments funded only by the portfolio, with "high degree of certainty" (case L88-92, VRF). The 2028 deposit comes from advances, speaking and licensing (L43-45, VRF). Research only, not for the TN or IPS: she called self-employment "unstable income" (B8b-Q18, VP, 2021); letting down "earliest supporters" is worse than letting herself down (D13a-N01, VP, student-era 2016). Growth-first misses a payment in 3.2% of paths, 13.7% if the deposit is $75k, and 40.8% if it is $0; lock-early misses none in that model, which buys at the 2026-09-25 curve (MODEL, `strategy_mc.py`, VRF script). Lock-early is not miss-proof: if rates fall before January 2027 and the deposit never comes, part of the 2033 payment is unfunded ($11,957 at -50bp, $31,413 at -100bp; joint tail, E6 R2, MODEL) | **Growth-first** (about 75% stocks, reserve bought later; the team's original plan) | **Loses on upside.** Growth-first's 2033 surplus p50 is $226k against $207k and its p95 $540k against $273k (MODEL, `strategy_mc.py`; those lock-early figures are the council's 60%-equity design, not REC, whose p50/p95 on the E6 basis are $207k/$250k, E6 [2]). **Close:** every lock-early team has this reason, so it is not a differentiator alone (M011, INT). About 1 path in 3 costs more than $300k in January 2027, so the "bought" date can slip to 2028 (MODEL 30-34%) |
| R2 | **Certainty is defined by a price she can check, and the plan names its own two gaps** | Case L97-99 asks the team to define and evaluate certainty (VRF). E2 lists "defines certainty by a price, not a model" and "names its own two gaps" among three things most teams will not do (INT). Gap 1: the real Nov-15 ladder costs $294,387, so headroom is $5,613 (19bp) on the 2026-09-25 curve (VRF inputs, ASM method). Gap 2: a fixed $50k is worth $42,063 in 2033 and $33,681 in 2042, in 2026 dollars at 2.5% inflation (ASM, F-114) | Rivals that state certainty as a model probability ("95%") or say "guaranteed" | **Close:** a strong rival can copy it once seen. **Risk:** too much caveat reads as a disclaimer. The spec caps it at about 15% of IPS words (E3-11, ASM) |
| R3 | **The building's minimum is fixed in January 2028, sized to her own second deposit, three years before she speaks to co-sponsors** | $150k deposit (L43-45, VRF); a "meaningful personal contribution" signals viability (L110-112, VRF); overpromising damages credibility (L114-116, VRF). REC bottom: $150k fixed. ALT bottom: p5/p50/p95 $134k/$167k/$211k, $134k after a bad 2028-30, and $93k in the 1929-start window (MODEL; VP data, derived; E6 [2], [3], [5]) | **ALT, the 2031 lock** (the council plan in CLAUDE.md, and E1) | **Loses on the typical case:** ALT's bottom is above $150k in 78% of paths (median $167k), and its median gift is $186-188k against $174k (MODEL, E4 [2], E6 [2]). The WInS stand-in (2032 note or IBTM) is UNVERIFIED as listed |
| R4 | **Same middle, better bad cases, in the model and in a century of history** | Total money for the facility plus flexibility: REC $182k/$207k/$250k, ALT $168k/$210k/$266k. On the same paths ALT is ahead in 53% of cases, by a median $1k, and behind by $23k at p5 (MODEL, E6 [2]). Every 6-year window from 1928, rescaled to JPM: worst $169k against $120k, p10 $185k against $174k, median $214k for both (VP data, derived, E6 [5]). No REC path ends below the $157,736 put in; 1.73% of ALT paths do (MODEL) | ALT; any "balanced sleeve locked later" design | **Loses at the top:** p95 is $16k lower and the stock share averages 7.5% against 9.7% over 2027-32 (MODEL). This is a different bet on when risk is taken, not a free improvement (E4 s0, INT) |
| R5 | **In 2031 she tells partners only what she owns, plus a stretch whose odds anyone can check** | Case L109-120 asks for a range and a confidence that protect the payments (VRF). The top is the minimum plus half the stock fund's value that day, capped. It is reached in 73% of model paths (MODEL). U.S. stocks' two-year return was zero or positive in 84% of 97 periods from 1928 to 2025 (VP data, derived, E4 [5]). 86% of the median gift is already owned when she speaks (MODEL, E6 [2]). Before E6's wording fixes, E3 still found the 2031 method passes "never overpromise" (SIM, E3 finding 7) | Rivals with an uncapped model top: an "80%" top landed within the range 62-93% of the time across models and history (AX1 C12, D3 v2, VRF audit) | **Loses on visible upside:** the cap means strong markets raise her kept money, not the announced gift. D5 argued an uncapped top answers "favorable outcomes" (L118) more honestly (E4 X3, INT). Answer: the excess stays hers, and she may add it in 2033 |
| R6 | **Risk sits only where she alone bears it, and all of that money is fully in stocks** | The payments cost 97.4% (exact-date) to 98.1% (Nov-15 STRIPS) of the first deposit (MODEL on the 2026-09-25 curve, VRF). So 2027 holds no stocks by arithmetic (E3 finding 2, SIM). D13c V1/V2 read her two verified risk ideas (take the jump, B1b-Q11, VP 2021; do not fail early supporters, D13a-N01, VP 2016) as: her own risk is fine, risk on people who trusted her is not (INT) | A timid all-Treasury firm (no "pursuing growth", L72-73, VRF); a "balanced everywhere" firm | **Close to all-Treasury:** at 50% stocks, the growth money beats an all-Treasury benchmark by only about $1k at the median and ends below it in about 48% of paths (MODEL, D3 M034). **Looks timid:** about 9% stocks overall from 2028. D13c N1 warns that a "take the jump" founder may read caution as unlike her (INT) |
| R7 | **Simpler to read: four dated decisions, a case number and "half"** | E2 counted about 55 ideas in E1 (INT). The spec has 10 blocks, ≤470 words, and one number (E6 s3). The growth-mix rule, band, reset, lock share and percentile are all removed (E6 8b). Last year's lesson: "over-complex for the insight" (CLAUDE.md, VRF) | Our own E1 version; rivals with dense frameworks | **Close:** a disciplined rival can be as simple. Simplicity only shows if the draft stays under the cap (PM-03, E5) |
| R8 | **The notes and the IPS say one thing** | The central idea is a split of jobs, true of both the WInS book and the real plan. A ban worded in time ("no stocks until...") is broken by a day-one VT buy (E2 C1/F4; AY2 rank 1; VRF audit) | Any team whose notes contradict its later IPS (E5 PM-06) | **Close:** only works if every note carries its scaling marker and passes the two-reader check (E6 5.4e) |

**Net verdict (INT).**
- **Against growth-first:** we win on the case's own test ("high degree of certainty") and lose only on upside.
- **Against the all-Treasury firm:** we win on "pursuing growth" and co-sponsor upside, but only narrowly on money.
- **Against the 2031 lock:** we trade about $12-14k of median gift and some stock exposure for a bottom that is fixed and owned early, and a better worst case.
- **Against a same-plan rival with warmer, plainer words:** we have no structural edge. E3's main finding (SIM) is that this is where Laura would be lost.

---

## 2. What the simulated client (E3) and the reader (E2) add

- **E3 (SIM, anchored to case lines):**
  - would very likely choose the firm on substance;
  - hesitates because E1 is "written from the trading desk outward".

  E3's fixes are all in the spec: never "promised" for the stretch (E3-1); forced versus chosen caution (E3-2); what stocks are for (E3-3); the cost clause protects the minimum too (E3-4); the pitch puts purpose first (E3-5); no behavioural diagnosis of her (E3-6); the longest-first counterpoint is named (E3-7).
- **E2 (INT):** substance is "of Top-50 quality", presentation is "not yet". Most of the +6 points from the fixes come from presentation and consistency, not strategy. Articulation was the weakest score (5/10), because the one true refinement story (growth-first dropped after testing) was unused. E6 now puts it in note C.
- **D13c (INT on VP quotes):** the plan feels like hers if it:
  - makes the leap certain for the people who will rely on it;
  - takes risk only where she alone bears the cost;
  - says its costs and gaps out loud;
  - sounds like a teacher, not a trading desk.

  None of her words may appear in the TN or IPS (brief s16).

---

## 3. What the Trading Notes and IPS must make visible for these reasons to land

**Trading Notes (Oct 23):**
- [ ] Three notes, three jobs:
  - operations (TLH with IEF);
  - the dated building minimum (2032 note or IBTM);
  - the stock fund (VT).

  Each note carries a Guide role word, one dated checkable fact and its rule (E6 5.6). This makes R3, R6 and R8 visible.
- [ ] Every note carries its scaling marker ("after both deposits" or "after her 2028 deposit"). Two outside readers still say Laura's real January 2027 money holds only bonds (R8).
- [ ] Note B names a date, not a price: "held to its end". Never "guaranteed" or "promised" (R3, R5).
- [ ] Reflection A is the tested one: three pre-registered numbers and "the rule said hold" (R2).
- [ ] Reflection C tells the true refinement: growth-first was tested and dropped because it could miss a payment, and all money nobody relies on is now in stocks. This covers R1, R6 and Articulation.
- [ ] No reserve size, 2031 figure, Laura quote or statistics degree anywhere.

**IPS (Nov 6):**
- [ ] The pitch puts purpose first and states the Laura-specific rule: each deposit buys one promise, and her second buys the building's minimum from her own earnings. No numbers, and no claim that anything is already bought (R1, R3).
- [ ] B2 defines certainty by price, names the residual risk and gives the two gaps one clause each (R2).
- [ ] B5 separates forced caution (the one allowed number: about 98%) from chosen caution. It says what stocks are for and the most markets can take (R6).
- [ ] B4 and B7 give the minimum rule, the 2031 method, confidence on both sides, and the words "owned / expected if stocks hold their value / kept" (R3, R5).
- [ ] B8 and B9 cover the cap, where kept money goes, "rules change only if her circumstances change", and no rebalancing between the parts (R4, R5).
- [ ] B10 is the WInS scaling sentence (R8).
- [ ] 10 blocks, ≤470 words by two counters, and six unpaid readers can restate the three pitch elements (R7).

---

## What this teaches

- "Why us" is a comparison, so it needs named rivals, a common yardstick and an honest list of where we lose. A reason every team shares (buy the payments first) is necessary but does not win.
- A simulated client and a model can sharpen a plan, but they are not the client or the future. Label them, and let the written page show the reasoning.
