# E6 Chief Strategist: final strategy specification for the team vote (Trading Notes and IPS)

Agent E6 (Chief Strategist), insight_v1 run, Phase E. Written 2026-09-28. AI-generated research for Team Caplet:
decisions to vote on, rules, numbers and checklists. **None of it is text to submit.** The six students decide every
point and write every WInS note, reflection, pitch sentence and IPS sentence in their own words. Any AI use goes in the
Final Report's Works Cited (Wharton AI policy, R-W46). Laura appears only through the case and her public professional
record. Nothing here suggests contacting her (R-W16: contact means disqualification).

**Scope (brief s17).** This file serves WInS trading now (as the source of the notes), the Trading Notes Analysis (TN,
due Oct 23) and the IPS (due Nov 6). The IPS freezes the strategy (IPS guide L73-75, VRF), and the Final Report must
apply it without redesign (Guide p.5 L156-159, VRF). So section 4 fixes every decision **rule** the Final Report will
apply. There is no Final Report content: no dollar range, projections, charts or fundraising text.
**Relayed messages:** one, "Try again" (a request to re-run this task). It changes no scope; this file is a fresh run.

**Status labels** (brief s3): **VP** = VERIFIED-PRIMARY; **VRF** = VERIFIED-REPO-FILE; **SNIP** = SNIPPET-UNVERIFIED;
**ASM** = ASSUMPTION; **MODEL** = an assumption-based model output, never a forecast; **INT** = E6's judgement, never a
fact about Laura. Ids: R- = case register, F- = fact register, SH-/BS- = stakeholder map, M- = Phase C question,
P = E1 proposal, F1-F10 = E2 fix, E3-n = E3 change, PM- = E5 cause (all under `research/insight_v1/`).
**Every security named is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (brief s14).

**Scripts.** New: `.venv/bin/python research/insight_v1/scripts/E6_final_checks.py` (about 2 seconds, no network; its
docstring lists every input and label). It re-uses the E4 and D6 engines (seed 20260927, 200,000 paths, the verified
lognormal fit), reproduces E1 P7 row 1 and E4's default row exactly, and puts both finalist designs on one basis
(sections [1]-[7], cited below as E6 [n]). Re-run on 2026-09-28: `E1_split_and_slices.py`, `E3_client_view_numbers.py`,
`E4_rival_numbers.py`; every figure E1-E4 quote reproduces. IBTM facts were re-read on the iShares page on 2026-09-28
with `fetch_text.py --grep` (both quoted sentences found verbatim).

**Evidence read in full** (audit corrections override the text above them): the brief; CLAUDE.md; the v4 prompt; the
case, IPS guide, TN guide, Competition Guide, Infographic and SMApply page; `phase_E/E1`-`E5`; `phase_D/` D1-D12,
D3_model_v2_results, D3_quant, D13c, the D13a summary and rules, all five audit files and every appended correction
list (AX1, AX1b, AX2, AY1, AY2); `phase_D/trading_now_brief.md`, `wins_now/securities_and_allocation_v1.md`,
`wins_now/T2_red_team.md` (it exists: saved 01:09 UTC, after E1-E3 checked), S4's summary; `phase_A/` case register
(summary, R-C, R-I, R-AN, X), fact register, stakeholder map (summary, T-1 to T-8, BS-01 to BS-20, section 7), guardrails
(summary); `phase_C/survivors.json` (all 48) and the parked items M007, M008, M015, M021, M033, M035, M040, M149; the
council chair memo and round-2 ruling (history only).

**Terms (labels for this file only; the team chooses its own words for anything it writes, T2 finding 8):**
- **Operations ladder:** ten zero-coupon U.S. Treasuries (STRIPS), each maturing on 15 November before one $50,000
  payment (2033-2042). A **rung** is one of them.
- **Building minimum:** one zero-coupon Treasury bought in January 2028 that repays the full dollar amount of the second
  deposit shortly before 1 January 2033. It is the least Laura will put toward the building.
- **Stock fund:** one broad world stock fund holding everything the ladder and the minimum do not need.
- **Kept money:** whatever the 2033 rule does not give to the building. It is Laura's flexibility.
- **REC / ALT:** the recommended design (this file) and the alternative (E1's 2031 lock).
- **p5 / p50 / p95:** in a simulation, the value 5% / 50% / 95% of paths fall below (p50 = median). **bp:** 0.01
  percentage point.

---

## 0. Summary (read this first)

**The call (INT).** Keep the heart of "lock early": the first deposit buys all ten payments before any money takes
stock-market risk (brief s8 items 1-8 stand). Change the facility half:
- **January 2028:** the second deposit first finishes any unbought payment. It then buys a Treasury that repays the
  deposit's full dollar amount just before 2033: the building minimum. Everything left goes into one world stock fund,
  which is left alone until 2033.
- **2031:** nothing is traded. Laura announces the minimum she already owns, up to the minimum plus half of what the
  stock fund is worth that day.
- **2033:** the ladder becomes the operating reserve. The building gets the minimum plus half of the fund, never more
  than the announced top. The rest stays hers.

**Why this beats E1's 2031 lock** (MODEL on JPM AC World 7.00%, bonds 5.0%, no fee; E6 [2]-[5]):
1. **Same middle, better bad cases.** Total facility-plus-flexibility money p5/p50/p95 is $182k/$207k/$250k, against
   $168k/$210k/$266k for the 2031 lock. On the same paths the 2031 lock is ahead in only 53% of cases, by a median $1k,
   and it loses up to $23k at p5. Compared at equal stock exposure (E4's two-thirds variant): p5 +$8k, median -$2k,
   p95 -$1k. Across every six-year window of U.S. history since 1928, rescaled to JPM: worst $169k against $120k, and
   the same median ($214k). The plan already follows this rule elsewhere (E1 P5, D2): when the middle ties, take the
   better bad case.
2. **The bottom co-sponsors hear is fixed three years before she speaks.** It is set by a number the case gives: her
   second deposit, $150,000 (case L43-45, VRF). Under the 2031 lock it is 80% of whatever 2028-30 markets leave: p5
   $134k, falling to $93k in a 1929-type window.
3. **Simpler and model-free.** This removes the growth-mix rule (the 50/60 debate, band and yearly reset), the top
   percentile q, and the question of short versus dated bonds. The 2031 top is a market value on the day, and its odds
   can be checked against history, not only against a model.

**What it costs (stated plainly):**
- **Less stock.** About 9% of her money is in stocks from 2028 to 2032, against 17% in 2028-30 then 3.5% under the 2031
  lock. Six-year averages: 7.5% against 9.7%. The p95 is $16k lower.
- **A smaller median gift but more kept money.** The median gift is $174k (against about $186-188k) because half the
  stock fund is kept: kept money median $32k (against about $21-24k). Because of the cap, strong markets add to her kept
  money, not to the announced gift.
- **WInS listing.** The WInS stand-in for the minimum (the 15-Nov-2032 note or IBTM) is UNVERIFIED as listed. The
  fallback is in section 5.10.

**This week (tier 1, before any order; target fills by Fri Oct 2 ET, hard stop Fri Oct 9 ET):** the three gate votes
(lock-early; REC or ALT; WInS book (ii)R), each preceded by every student's own-words note. Then the Session Rules
screenshot, the IBTM search and the Bonds drop-down check, the zero-risk note-box test, roles, and the decision and
AI-use logs. The note drafts are written by students from element lists, copy-checked, and read by two outside readers
(section 5.4).

**The biggest risks to the semifinal are not the strategy** (E2 verdict; E5 top 10, INT). They are:
- ownership and voice (PM-01);
- a format breach (PM-02, fatal);
- density (PM-03: E1 specified about 55 ideas; this spec caps the IPS at 10 blocks and ≤470 words);
- AI wording in permanent notes (PM-04);
- notes that contradict the IPS (PM-06).

Section 6 ranks every change by deadline and impact.

---

## 1. The strategy in one plain paragraph

*(This paragraph is for the team to understand and explain. It is not wording for any deliverable. Labels: case facts
VRF; dollar sizes MODEL/ASM at the 2026-09-25 curve; fund size VP via ticket v1.)*

Laura adds $300,000 at the start of 2027 and $150,000 at the start of 2028. She has promised her residency $50,000 at
the start of each year from 2033 to 2042. The first $300,000 buys ten U.S. government bonds, each timed to pay just
before one of those payments. From that day, nothing that happens to stock markets, or to her book and speaking income,
can take the payments away. If bond prices rise before January 2027 and the money falls a little short, the latest
payments are bought first, and the second deposit finishes the job before it does anything else. When the $150,000
arrives, the plan buys one more government bond that gives back the whole $150,000 just before the residency opens.
That is the least she will put toward the building, and markets cannot shrink it. Whatever is left, about $40,000, goes
into one fund that owns about 10,000 companies worldwide, and nobody touches it until 2033. In 2031, when she starts
asking partners to join, she can say exactly what she already holds for the building, and how much more to expect if
stocks simply keep their value. In 2033 the ten bonds become her operating reserve and pay the residency year by year.
The building gets its minimum plus half of the stock fund. The rest stays with her for whatever the project needs next.

---

## 2. The central idea and what the 50-word pitch must contain (IPS; also governs every TN note)

**Central idea (content, not wording): a split of jobs.**
- Money other people will rely on is bought when her money arrives and held to its date. That means the ten operating
  payments, and the building minimum she will announce. It never takes stock-market risk.
- Money nobody relies on is invested fully in world stocks.
- Consequences:
  - once bought, the payments depend neither on markets nor on her next contract (her second deposit is career income,
    case L43-45, VRF);
  - she tells partners only what she already owns, plus a stretch whose odds anyone can check.

**Why a split of jobs, and not a time-worded ban** (E2 F4, C1; E4 L5; AY2 rank 1; VRF): a ban such as "no stock risk
until all ten payments are bought" is visibly broken by the WInS book, which buys world stocks on day one, and the
notes are read before the IPS exists. A split of jobs is true of Laura's real plan and of the WInS book. The ordering
("payments first") lives inside the 2027 and 2028 rules, not in the pitch.

**Pitch specification (IPS guide L31-36, R-I16/R-I17, VRF: "Maximum 50 words", "Clearly communicate the central idea
... and how it is designed to support your client's financial goals and future funding needs").**

| # | Element (content; the team writes the words) | Must contain | About (INT) |
|---|---|---|---|
| 1 | **Purpose first** (E3-5; E2 F3; D13c checklist "purpose comes first") | What the plan secures for the residency, named by what it secures (its ten years of operations), before any instrument or prohibition | 12-15 words |
| 2 | **The Laura-specific rule** (M143; E4 1.2) | Each of her two deposits buys a promise when it arrives: the first, the operating years; the second, the building's minimum from her own earnings. Once bought, neither depends on markets or on her next contract | 15-18 words |
| 3 | **What the rest does, plus credibility** (M008; E1 P1 item 3) | Only money nobody relies on is in world stocks, for a larger gift and her flexibility. She tells partners only what she owns | 12-15 words |

- **Hard limits:** at most 48 words by two word counters, using the higher count (E5 PM-02). No numbers; at most one if
  it is essential. Tense stays future or conditional: nothing is bought in 2026 (E3-5).
- **Must not contain** (E1 P1/P17; D9 M062; D13 rules; E3 4c):
  - "bought in January 2027" or "fits inside $300,000" as a flat claim;
  - "guaranteed", "risk-free", "safe", "100%", "95%", or "certain" without its qualifier;
  - "promise" or "promised" for the stretch above the minimum;
  - jargon: barbell, LDI, duration, STRIPS, ladder, funded ratio, percentile, glide path, liability matching;
  - fund names or tickers, or a return target;
  - any quotation, the case pull quote, "Laura said";
  - identity, heritage or Taiwan as a reason;
  - book-title, "falling" or "balance" metaphors (the case's own "appropriate balance" is fine);
  - the statistics degree; "innovative"; a probability.
- **Tests:**
  - six unpaid readers can restate all three elements after one read (D12 M234 protocol);
  - no reader thinks anything is already bought;
  - no reader thinks the WInS stocks contradict the pitch (ask after showing the three notes, E2 s5).

---

## 3. IPS content map (IPS, Nov 6): what fills each required element, and the word budget

**Rules for the whole IPS** (IPS guide L51-52, L68-70, L123; D9 M036; E2 F1-F2; E5 PM-02, PM-03; VRF / INT):
- **Structure:** at most 12 ideas in 10 blocks, built on the four case dates (2027, 2028, 2031, 2033). Each date gets
  one action and one "because" tied to Laura or the case.
- **Length:** at most 470 IPS words and at most 48 pitch words, by two counters.
- **Numbers:** case facts only where a rule needs them; rule parameters in words ("half", "the full amount of her
  second deposit"); at most one rounded, dated computed figure. The recommended one is the forced-caution fact (block
  B5). No percentiles, probabilities, dollar ranges, tables or lists.
- **Words:** no framework or house names, no tickers, no Laura quotes. Every forecast carries a grade word ("we
  assume", "history suggests"); every price carries "at [month] 2026 prices" (D12 M231).
- **Proportion:** at most about 15% of the words describe what could go wrong (E3-11, ASM ceiling). Each gap gets one
  clause.

### 3.1 The ten blocks (content elements only; the team writes every sentence)

| Block | Answers (IPS guide lines; case lines; all VRF) | Content the team's sentences must carry | Words (INT) |
|---|---|---|---|
| **B1 Purpose and central idea** | IPS L16 (central idea), L18 (principles), L27-28 (client at the centre), L53-57 (what and why), L45-46 (tailored) | What the plan secures for the residency (ten operating years, then the building's minimum, then growth). The split of jobs (section 2). The Laura-specific benefit: her second deposit is her own career income, so once bought the payments no longer depend on markets or on her next contract, and her own earnings are kept whole for the building | 40 |
| **B2 Certainty: definition, evaluation, residual risk, two gaps** | IPS L9-10 ("desired degree of funding certainty"); case L91, L97-99 (define, evaluate, assumptions); L90 (not inflation-adjusted); L146-148; R-AN10 (no currency named) | (a) Bought, not forecast: each payment is matched by a Treasury maturing shortly before its date and held to maturity. (b) Evaluated by price: on the purchase date the money covers the market price of all ten, with no model percentage. (c) Residual risk: certain in U.S. dollars, barring a U.S. Treasury default. (d) Gap (i): if rates fall before January 2027, the price can exceed the first deposit, and the earliest payment then waits for the second deposit. (e) Gap (ii): each payment is a fixed U.S. dollar amount, so rising prices and Taiwan's costs and exchange rate mean it buys less over time. This gap is named, not solved | 50 |
| **B3 January 2027: buy the payments** | IPS L22-23 (planned changes), L48-50 (preparing for the operating commitment); case L91-92 | Buy all ten on arrival, with no waiting for better yields, because waiting is a bet on rates. If money is short, buy the longest-dated payments first. Because: the piece left waiting is the smallest and least rate-sensitive, and less would stay unbought if the next money never came. Counterpoint, stated: the waiting piece is the residency's first operating year (E3-7; E2 F7c). Any leftover waits in Treasury bills | 35 |
| **B4 January 2028: finish, then the building's minimum, then stocks** | IPS L22-23, L46-47, L48-50; case L43-45, L101-104, L110-112 | The second deposit first completes any unbought payment. It then buys a Treasury repaying the deposit's full dollar amount just before 2033 (the building minimum; the case's "meaningful personal contribution"). Everything else goes into one broad world stock fund, left alone until 2033. **One** labelled stress clause, as the team's own scenario (the case says she "will", R-AN35): a smaller or later deposit follows the same order, and the minimum is smaller or later. If rates fell first and the deposit is smaller than the unbought part, all of it completes the payments and the unfunded part of the first payment is stated (P4; AY2 rank 2) | 45 |
| **B5 Risk and return, goal by goal** | IPS L3 (risk tolerance), L20 and L59 (balance), L46 (risk and return); case L61-74; R-AN16, R-AN17 | **Forced caution:** at September 2026 prices the payments cost about 98% of her first deposit (the one allowed number), so 2027 holds no stocks by arithmetic (E3-2). **Chosen:** the minimum takes no market risk because partners will rely on it; money nobody relies on takes full stock-market risk. **What stocks are for:** a larger gift and more flexibility if markets are good (E3-3). **The most markets can take:** the stock fund, which is roughly what her deposits would have earned safely. Never the payments or the minimum (E4 L10). **Portfolio fact, not a diagnosis:** her income already rides on publishing and speaking, so the plan adds no themed or single-country bets (D8 M081; E3 finding 6). **Returns** are a range across two published forecasters, not a target (D8 M109) | 45 |
| **B6 Diversification and liquidity** | IPS L46 (construction and diversification), L9-10 (liquidity); SMApply criterion "appropriate diversification"; R-AN45 ("funding purposes", VP) | Diversified by funding purpose and by date: ten dated payment bonds, one dated building bond, and one fund of about 10,000 companies worldwide. Holding U.S. Treasuries for the promises is deliberate, because the bills are in U.S. dollars and dated. Liquidity: no withdrawals before 2033 (case L63-65), and each year's payment comes from its own maturing bond (E2 F5) | 25 |
| **B7 January 2031: the co-sponsor range (method only)** | IPS L25-26, L64-65; case L109-120 | Nothing is traded, and she speaks only once the payments and the minimum are owned. Range: bottom = the minimum she owns; top = the minimum plus half of the stock fund's value that day. Confidence both ways: below the bottom only if the U.S. Treasury defaults; the top is reached if world stocks are no lower two years later (graded "history suggests"; the numbers go in the Final Report). Words by tier: owned / expected if stocks hold their value (never "promised", E3-1). U.S. dollars are binding | 40 |
| **B8 January 2033: reserve, gift, flexibility** | IPS L48-50 (reserve composition over time; responsible facility contribution; flexibility); case L94-107 | The reserve is the ladder, bought from 2027 and named the operating reserve on 1 Jan 2033, before the first payment (P9). It is held to maturity, and its composition changes only as bonds mature. The case allows "if at all" (L96). The gift is the minimum plus half the stock fund, never above the announced top. Everything else is kept, moved to U.S. dollar Treasury bills, and hers to use "as the project develops" (L102-103). There is no conversion to New Taiwan dollars or currency hedge before the facility decision. Taiwan building costs are expected to rise, so a fixed dollar gift buys less (L146-147) | 45 |
| **B9 Governance and costs** | IPS L5, L61-62, L73-74; Guide p.5 L156-159; case L101, L110 | The team's written rules run the portfolio. Laura makes the two calls the case gives her, within the rules: what she announces in 2031 (never more than the rule allows) and the 2033 amount and use of kept money. Rules change only if her circumstances change, never because markets moved. The stock fund is never sold to protect a gain or to wait for a recovery. There is no rebalancing between the three parts (CFA 2010 element 4c, VP via D8). The bought Treasuries carry no ongoing charge, and any cost is paid from the stock fund (E3-4) | 35 |
| **B10 The WInS sentence** | IPS L75 ("Your portfolio ... should reflect the strategy"); D10 1.5 | WInS shows her plan on the day both deposits are in, scaled to $300,000. The Treasury funds stand in for her bonds: they move like them but do not mature on her dates. In January 2027 almost all of her real first deposit buys the payments (ticket v1 s1; T2 16a) | 25 |
| | | **Content words, before connecting words** | **about 385** |
| | | **Connecting words (INT allowance)** | **about 70** |
| | | **Target total (hard cap 500; plan ≤470)** | **about 455** |

**Paragraph plan (at most 7 paragraphs, D10 2.3):**
1. B1 and B2;
2. B3;
3. B4;
4. B5 and B6;
5. B7;
6. B8;
7. B9 and B10.

The IPS guide says "You do not need to address these points separately" (L66, VRF), so no headings inside the IPS.

### 3.2 Coverage check (every IPS-guide and case "should" item has a home; tick against the draft)

| Requirement (VRF) | Block |
|---|---|
| Goals, time horizons, liquidity needs, desired degree of funding certainty, need for flexibility (IPS L9-10) | B1 (goals; horizons via the four dates), B6 (liquidity), B2 (certainty), B8 (flexibility) |
| Central idea (L16); principles (L18) | B1; B5, B9 |
| Balance of growth, risk, liquidity, funding reliability, flexibility (L20, L59) | B5, B6, B2, B8 |
| How allocation and composition change as needs approach and payments are made (L22-23; L46-47 "planned changes") | B3, B4, B7, B8 (the four dates; rungs mature) |
| Protect the operating commitment while preserving flexibility for a responsible facility contribution (L25-26, L64-65) | B7, B8 |
| Risk tolerance (L3); risk and return (L46) | B5 |
| Portfolio construction and diversification (L46) | B6 |
| Preparing for the commitment; reserve composition over time; responsible facility contribution; flexibility (L48-50) | B3-B4; B8; B8; B8 |
| Framework, not individual investments or detailed calculations (L51-52) | Number policy above; no tickers |
| What, why, how guided as needs change (L53-62) | B1, B9 |
| Official record; no revision after the deadline; portfolio reflects the IPS (L73-75) | B9, B10 |
| Define high degree of funding certainty; how evaluated; assumptions (case L97-99) | B2 |
| Assumptions on investment performance, timing of cash flows, outside funding, inflation's effect on projections and facility costs, flexibility (case L146-148) | B5 (graded returns); B3-B4 (timing); B1-B2 (no outside money for the payments); B2 and B8 (inflation, building costs, currency); B8 (flexibility) |
| Favorable and unfavorable outcomes; the range protects the payments (case L118-120) | B7 (method only; the numbers are in the Final Report) |
| Not expected in the IPS: final reserve calculation, projections, final range, co-sponsor draft (L68-69) | Excluded |

### 3.3 Format checks (non-compliance = "will not be considered for semifinal selection", IPS guide L82-83, VRF)

- [ ] **Title page (page 1 only):**
  - the official team name, exactly as on the submitted roster;
  - members as "First Name, Last Initial", exactly as on the roster;
  - the **WInS username**, not the team name (IPS guide L84-100, VRF);
  - these are copied from the roster screenshot and the WInS login, character for character (PM-18).
- [ ] **Pages 2-3:** the headings "Investment Strategy Elevator Pitch" and "Investment Policy Statement", as in the
  sample. Pitch ≤48 words and IPS ≤470 words by two counters; the higher count wins.
- [ ] **Type and layout:**
  - Times New Roman 12 everywhere, headings included;
  - double-spaced using Word's "Double", on U.S. Letter with 1-inch margins;
  - paragraph spacing 0, no blank lines, at most 7 paragraphs.
- [ ] **No banned items:** no tables, bullet lists, charts, images, links or URLs, footnotes, citations, or quotation
  marks around anyone's words (L123).
- [ ] **PDF checks:**
  - export the PDF and open the exported file itself;
  - exactly 3 pages; the text ends on page 3 with at least 2 spare lines;
  - the font list shows Times New Roman; file ≤5 MB;
  - search it for "http", "www" and brackets.
- [ ] **Line spacing:** "Exactly 24 pt" (Wharton's sample pitch) is a documented last resort only, never the plan
  (D9; AY2; E5 C4).
- [ ] **Dates** (AEDT; E5 [1]): words frozen Tue Nov 3; two-student PDF check Wed Nov 4; submit Thu Nov 5. The
  deadline is Sat Nov 7 09:00 AEDT (Fri Nov 6, 5 p.m. ET).

---

## 4. Decision rules fixed before Nov 6 (IPS; the Final Report later shows each one "fired as written")

Every parameter is fixed here, because a rule whose parameter is chosen after Nov 6 is a redesign (D8 M006; IPS guide
L73-74, VRF). "Record" is the decision-log entry that makes the later check possible.

| Rule | Trigger | Action | Record | Anchor (VRF unless marked) |
|---|---|---|---|---|
| **R1 Buying the payments (the rates-fall rule)** | The first deposit arrives, 1 Jan 2027 | (1) Buy the ten-rung ladder at that day's prices, all at once: no staging, no yield trigger. (2) If the money is short, buy the longest-dated payments first. The unbought part is always the earliest payment, and it is the first use of the next money. (3) If money is left over, it waits in Treasury bills until 2028. (4) Headline, conditional: bought in January 2027 if prices allow, otherwise when the second deposit arrives. Never "by 1 January 2028 at the latest" (AX1b item 3) | Purchase-day ladder cost against cash; which payments were bought; the gap or leftover | Case L91-92, L43-45. Numbers: the real Nov-15 ladder costs $294,387 on the 2026-09-25 curve, headroom $5,613 (19bp) (VRF inputs, ASM method). About 1 in 3 rate paths cost more than $300k (MODEL 30-34%; history: ≥19bp falls in 32-36% of 68-day windows since 1962/1990, VP data, derived). Staging gives no reliable gain (+0.2 to -0.5 points) and a 27-35% chance of needing the deposit (MODEL). Longest-first carries a +5% top-up price rise against +15% for nearest-first, and leaves $31.4k of face unbought against $47.7k if the deposit never came, at -100bp (MODEL; D1, AX1b) |
| **R2 The second deposit** | The deposit arrives (1 Jan 2028 per the case; each instalment if late) | In this order: (1) complete any unbought payment; (2) buy a zero-coupon Treasury maturing before 1 Jan 2033 that repays the deposit's dollar amount (the building minimum), or all that is left if less; (3) put everything else, including the 2027 leftover, into one broad world stock fund. **Smaller or late:** same order; the minimum is smaller or later. **No building minimum and no stock fund exist until all ten payments are bought.** **Joint tail** (the team's own stress case): if rates fell before January 2027 and the deposit is smaller than the unbought part, all of it goes to the payments, there is no minimum and no stock fund, and the unfunded part of the first payment is stated | Deposit amount and date; top-up cost; the minimum's face and price; the stock fund's starting value | Case L43-45 ("will contribute"), L110-112, L101-104. MODEL: growth money $158k; the minimum costs $118k at the 5-year 4.98% (ASM that it holds); stock fund $40k = 8.7% of all money. A -50bp fall first leaves the fund at about $20-23k; -100bp at about $1-7k; -150bp leaves no fund and a minimum of about $127-137k (E6 [8], which corrects E4 [7]'s $31k / $15k / $147k; the range depends on whether the 5-year rate also falls; MODEL). Joint tail with no deposit: $11,957 (-50bp) or $31,413 (-100bp) of the 2033 payment unfunded (D1/D3). A deposit of about $43k or more covers a 150bp fall, about $51k the worst 98-day fall since 1990 if rates do not fall further (AX1 V4). $75k deposit: minimum $75k, total $94k/$109k/$135k (E4 [4]) |
| **R3 The operating reserve** | 1 Jan 2033, before the first payment or any facility contribution | The ladder is named the operating reserve and pays the first $50,000 at once (the 2032 rung matured on 15 Nov and waited in bills). It is held to maturity. Each rung matures about 47 days before its payment and waits in Treasury bills. Nothing is sold early, and there is no rebalancing between the reserve, the minimum and the stock fund. The reserve empties itself by 1 Jan 2042 | The reserve's market value, cost and face on 1 Jan 2033 (the Final Report reports market value first) | Case L94-97 ("if at all", L96); IPS L48-50; P9. About $395k market value on today's forwards (VRF inputs, ASM), cost about $292-294k, face $500k |
| **R4 The 2031 co-sponsor range (method; no figures in the IPS)** | 1 Jan 2031, when she begins approaching co-sponsors (case L109) | **Condition:** all ten payments and the minimum are owned; otherwise no range is stated (only "aspiration"). **Nothing is traded.** **Bottom** = the minimum she owns. **Top** = the minimum plus half of the stock fund's market value on 1 Jan 2031, set once and not reset later. **Confidence, both sides:** below the bottom only on a U.S. Treasury default (and only if no fee is ever charged to it, R8); the top is reached if the stock fund is no lower on 1 Jan 2033 than on 1 Jan 2031, with the history and the model named in the Final Report. **Words:** owned / expected if stocks hold their value / kept; never "promised" or "pledged" for the stretch (E3-1; BS-05). **U.S. dollars are binding;** any New Taiwan dollar figure is dated and illustrative | The stock fund's value on 1 Jan 2031; the stated range | Case L110-120; R-AN9; AX1 C2-C3 (a capped range is reported with the chance of reaching the top, never "100% within"). MODEL at the median: bottom $150k, top $175k (width 1.17x); 86% of the median gift already owned when she speaks; the top is reached in 73% of model paths (67% on the Vanguard-type input). U.S. stocks' two-year total return was zero or positive in 84% of 97 overlapping periods 1928-2025 (89% since 1950) (VP data, derived; E4 [5]) |
| **R5 The 2033 facility contribution and flexibility** | 1 Jan 2033, after R3 | (1) Gift = the minimum plus half of the stock fund's value, never more than the announced top. (2) Kept money = everything else (the other half, plus any growth above the top). It moves the same day to U.S. dollar Treasury bills and is Laura's to use "as the project develops"; she may choose to add to the gift, which is her decision and not counted by co-sponsors (AX1 C15). (3) No conversion to New Taiwan dollars and no currency hedge before the facility decision: a forward contract is a derivative, banned in WInS and, on the safe reading of "Investments permitted (for BOTH contributions)", in the plan (R-AN15); early conversion would also be a currency bet | Gift, kept money and the date of the facility decision | Case L101-107 (she decides; flexibility; no contingency fund required), L118-119. MODEL: gift $165k/$174k/$188k; kept $16k/$32k/$66k, about 15% of the post-reserve money at the median, the size of three or four years of Taiwan building-cost drift (F-508 3.54%/yr since 2021; ASM sanity check, not a contingency fund, D5) |
| **R6 The stock fund's conduct** | Every day, 2028-2032 | One broad world stock fund. It is never rebalanced against the Treasuries and never sold before 1 Jan 2033, whether to protect a gain or to "wait for a recovery". A fall shrinks only the stretch above the minimum, never the payments or the minimum | Yearly check that holdings match R2-R6 | Case L69-74, L61-65. MODEL: the fund falls in about a quarter of years; in a bottom-decile 2031-32 the gift is $169k at the median and stays at or above the announced bottom in 100% of paths (E6 [3]) |
| **R7 Governance** | The four case dates, plus a yearly check | **Who decides:** the students' written rules. The advisor is administrator only; never write "our portfolio manager approves" (R-W19, VP). Laura makes the two calls the case gives her, within the rules (L101, L110). **What may change a rule:** a change in Laura's circumstances (for example, a different deposit amount or date), never a market move. Worded so that it cannot read as permission to revise after Nov 6 (AY2 D8 C12) | Dated decision log: what fired, when, the numbers | IPS L73-74; Guide p.5 L156-159; CFA 2010 elements 2a-2b (VP via D8/D10) |
| **R8 Costs** | Any fee or trading cost | The bought Treasuries (the ladder and the minimum) are held to maturity with no ongoing charge. Every cost is paid from the stock fund, never from the payments or the minimum. The Final Report states the fee assumption, its base and its rate, and shows the effect | The fee assumption | Case L43 ("with an asset management firm"); Rules page to the Asset Manager Code F.4.d (VP via D8; "should provide"). MODEL (E6 [6]): a 1% fee charged on the stock fund only costs about $3k of the median total; the same rate charged on all assets but paid from the fund costs about $31k. It could still be paid from the fund in every model path (thin-tailed model). The fee base is the assumption that matters |
| **R9 The certainty definition and the stated assumptions** | Fixed in the IPS | Block B2's five parts. Assumptions: returns as a range across two published forecasters (graded); flows at the start of each year (case L59); no outside money for the payments (L91-92); payments fixed in dollars (L90), Taiwan building costs expected to rise (L146-147), U.S. dollars binding; flexibility kept by R5 | None (the IPS is the record) | Case L97-99, L146-148 |
| **R10 WInS conduct (consistency with the IPS)** | Each trading day to Nov 6 | The book is (ii)R (section 5). The operations hedge is never sold after a rate rise or trimmed after a fall. It is re-mixed IEF-against-TLH only if its rate sensitivity drifts more than a quarter-year from its start (ticket v1 s8). The minimum and the stock fund are held. No day trades; no "tidy-up" trades after the words freeze (Tue Nov 3) | Every trade, and every "decided not to trade" moment | IPS L75; User Guide "Day Trading: This is not permitted" (VP via A4) |

---

## 5. The WInS book and the three Trading Notes plan (tier 1: WInS now and TN, Oct 23)

### 5.1 Which book: (ii)R = Laura's plan on 2 January 2028, scaled to $300,000

**Decision (INT; team vote at the gate): (ii)R.**
- **For:**
  - It is the first day all three jobs exist, so the notes show three distinct decisions with three jobs: operations,
    the building minimum, growth (TN guide L4-6, L11, VRF).
  - It shows "funding purposes" diversification in the holdings (R-W71, VP).
  - It survives one trading session as written (T2 one-session test), and it copes with a position cap better than
    (iii) (ticket v1 s3).
  - Its building-minimum note is the most Laura-specific holding in any book (E4 L6).
- **Against (iii):** with no listed dated rung it gives two decisions plus a T-bill leftover note that earns about $18
  against a $25 commission, which reads as filler (T2 finding 4; E2 F4, ASM).
- **Conditions:**
  1. the central idea is worded as a split of jobs (section 2);
  2. each operations note and stock note carries its scaling marker inside the note ("after both deposits" / "after her
     2028 deposit") (ticket C2);
  3. block B10 is in the IPS;
  4. no note calls the WInS holdings "Laura's portfolio" (Asset Manager Code F.2, VP via D10);
  5. the two-reader check passes (5.4).

### 5.2 Orders (illustration at the 2026-09-25 closes; recompute every share count from the last close, T2 finding 1)

| Order | Holding | Weight | ~Shares | Job / Guide role word | Primary, then alternates (all PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK) | 2025-26 list (history only, VRF) |
|---|---|---|---|---|---|---|
| 1 | IEF (7-10y Treasuries) | 23.5% | ~783 | Operations: future funding | IEF; VGIT, then SPTI (ticket v1 s12) | IEF yes |
| 1 | TLH (10-20y Treasuries) | 42.5% | ~1,365 | Operations: future funding (IEF and TLH are one duration-weighted decision) | TLH; IEF + TLT at duration weights (40.9/25.1) if TLH is missing | TLH no, TLT yes |
| 2 | **Building minimum:** the 4.125% Treasury note of 15-Nov-2032 (CUSIP 91282CFV8), **or** IBTM (iShares iBonds Dec 2032 Term Treasury ETF) | 24.3% | note ≈ $75k face; IBTM ~3,336 | Building minimum: risk management (it takes the minimum out of market risk) or future funding; one word, recorded | 1) the 2032 note ($10 trade); 2) IBTM ($25); 3) if neither is listed, an undated ~5-year stand-in (VGIT, then SPTI), noted as "moves like, not dated" | IBTM no; VGIT no |
| 3 | VT (world stocks) | 8.7% | ~163 | Stock fund: growth | VT; VTI + VXUS (62/38); ITOT + IXUS | VT, VTI, VXUS yes |
| | Cash float | ~1% (~$2,990 after 4 × $25) | | Liquidity | Keep at least $1,000 | |

- **Weights:** ladder 65.9%, minimum 25.3% and stock fund 8.7% of the plan's $464k on 2 Jan 2028 (MODEL arithmetic,
  E6 [7]). The hedge mix IEF 35.6% / TLH 64.4% of the hedge gives "about 10 years" of rate sensitivity, like the
  payments' (issuer durations IEF 6.86y, TLH 11.58y on 9/25, VP; 9.90y liability, VRF).
- **Order of entry:** IEF and TLH first, then the minimum, then VT, all in one session. The time stamps then show
  promise-first (D7). Orders placed while the market is closed fill at the next open (R-W62, VP), so size them from
  the last close.
- **Instrument facts (VP):**
  - IBTM: NAV $21.83 on 9/25; expense 0.07%; effective duration 5.05y; 15 Treasuries maturing Apr-Sep 2032; about $555m
    of net assets; about 216k shares a day. Both sentences below were re-read on ishares.com on 2026-09-28: the funds
    "will terminate on or about October or December 15 of the year in each Fund's name", and they "do not seek to return
    any predetermined amount".
  - VT: 10,088 stocks, 37.7% outside the U.S. (8/31); expense 0.06% (ticket v1 s12).
  - The 2032 note's model price is 95.27 clean plus about 1.49 accrued per 100 on 9/25 (ASM, D1). WInS shows its own
    price.

### 5.3 Position-limit branches (read both Session Rules lines before any order; ticket v1 s3)

| Single-security limit shown | Book (ii)R |
|---|---|
| None, or 43% or more | As in 5.2 |
| 25-42% | IEF 23.5 / TLH at the cap minus 1 / SPTL the rest of the hedge. The minimum is held one point under the cap if the cap is under 25.3%. At a 25% cap: IEF 23.5 / TLH 24 / SPTL 18.5 / IBTM 24 / VT 8.7 / cash about 1.3% (5 ETF trades, $125) (E6 [7]) |
| Under 25% | Hedge as ticket v1 s3 (IEF, TLH, SPTL at the cap minus 1; VGIT then VGLT take the rest). Minimum: IBTM at the cap minus 1, the rest in VGIT. **If 5 or more hedge funds would be needed (a cap of about 17% or less), stop and ask Wharton (Contact Us) before trading** |
| A separate, higher bond limit is shown | The 2032 note may carry the whole minimum |

Never add to a holding within one point of the cap. A 20-24% stock fall, or a 10-12% fall with a 50bp rally, can lift
TLH above a 25% cap (T2 [5], ASM that WInS re-checks the limit).

### 5.4 Gate: tick every box before the first order (owners are roles; E5 section 5 calendar)

- [ ] **(a) Votes**, each recorded with first names, date and reason, **after** every student has written 3-5 lines in
  their own words with no AI file open (R-W51; PM-01):
  - lock-early;
  - REC or ALT (section 7, D2);
  - book (ii)R or (iii).
- [ ] **(b) Session Rules screenshot:** single-security limit, any bond or type limit, the day-trading tooltip, trades
  allowed, commissions. Also read the logged-in Trading Details page. If it shows an activity minimum or a cap on a whole
  security type, stop and ask Wharton; never add trades to meet a count (T2 finding 13; PM-15).
- [ ] **(c) Listings:** search IEF, TLH, VT, IBTM (and SPTL, VGIT). Check the Bonds drop-down for every U.S. Treasury
  maturing Jul-Dec 2032, recording coupon, price and accrued interest; search by maturity, not by a built-up symbol
  (AX1b item 10).
- [ ] **(d) Note-box test at zero risk:** type about 450 characters on the order-review screen, see whether they are
  cut, clear them, and do **not** press Confirm. Until a limit is seen or ruled out, notes are drafted to 300
  characters (UNVERIFIED for WInS; a sister product caps at 300, VP; Wharton's own example is 413 characters, VRF).
- [ ] **(e) Notes** are drafted offline by students from the 5.6 elements, with no research file open (PM-04).
  - A second student restates each note's role in one sentence.
  - The second student then searches every five-word run of the draft in `research/`; any hit is rewritten.
  - Two readers outside the team read all three drafts and say what Laura's real money holds in January 2027. If either
    says "stocks" or "a building bond", fix the drafts (E3-10).
- [ ] **(f) Roles:**
  - one trader plus a backup (only they place orders);
  - note writers; a second reader; a log keeper; a data owner;
  - every student drafts at least one note or reflection and one IPS block (PM-05; R-W38, VP).
- [ ] **(g) Cash:** at least $1,000 left after orders at the next open's prices. No sells on the day anything is bought.
- [ ] **(h) Labels:** the team names its own labels for the three parts in a meeting, and logs that the proposals came
  from an AI source (E2 F10; T2 finding 8).

### 5.5 The three notes: which trades, and supported / tested / refined (a menu, not a quota: TN guide L12, L29-30, VRF)

| Slot | Trade | Shows | The reflection's one extra job (E2 F9) |
|---|---|---|---|
| A | TLH (operations; IEF was bought with it as one decision) | **Supported and tested** | Tested: over the pre-registered window (fill-date close to the Oct 20 close), exactly three numbers, each labelled as the team's own calculation from the WInS screen and the treasury.gov curve (T2 finding 7). They are: the 10-year rate move in bp; the hedge's % change; the payments' % change. Then what the rule said to do (hold). A 10bp-or-larger move has about a 52% chance for an Oct 2 fill and about 40% for an Oct 9 fill (T2 [4], ASM). Report small moves and poor tracking as they are (AY2 D7 C2) |
| B | The building minimum (2032 note, IBTM or the stand-in) | **Refined**, only if the decision log shows, dated before this order, the change from "a floor bought in 2031" (the council plan in CLAUDE.md) to "the minimum bought when the 2028 money arrives", with the reason in the students' words. Otherwise **supported** | Refined: what changed, and the research that changed it (tested at equal stock risk: about the same middle, better bad cases; at most one number). Otherwise: why a dated holding (an amount on a date, not only a price that moves) |
| C | VT (stock fund) | **Supported** (it carries out the plan as refined) | The true refinement story (E2 F8). The first plan (growth-first, about 75% stocks) was tested and dropped because it could miss a payment (about 3 in 100 modelled futures; about 4 in 10 if the 2028 deposit never came; F-401, F-404, VRF, MODEL). Now stock risk sits only where nobody relies on the money, and all of that money is in stocks: the "why so little stock" answer, stated by goal (ticket s6; E1 P6). One number at most |

### 5.6 What each WInS note must contain (elements in noun phrases, not wording; ≤300 characters until the box test)

The Guide wants a note to capture "the reasoning behind the decision, including its alignment with your strategy, the
supporting research or analysis, and its expected role" (Guide p.3 L84-86, VRF). The trade record already shows the
ticker, side and quantity.

**Every note has four cores.**
- **C1:** one Guide role word, plus the team's own label.
- **C2:** Laura's dated need, including the scaling marker.
- **C3:** one dated, checkable fact, with its source named in words.
- **C4:** the rule or risk. If space runs short, C4 and the label move to the reflection (AY1 D12 C1).

| Note | C2 need (with marker) | C3 one fact (pick one) | C4 rule / risk | Never say |
|---|---|---|---|---|
| A operations | The ten $50,000 payments 2033-2042; her operations money after both deposits (about two-thirds of her **total** money; never of the payments, E3-10) | The pair's rate sensitivity is about 10 years, set to the payments' (issuer durations, dated; the team's calculation); or TLH's own effective duration (iShares, dated) | Never sold after a rate rise or trimmed after a fall; re-mixed only if the sensitivity drifts more than a quarter-year | match, matched, "mature in her payment years" (74.7% of TLH matures after 2042, VRF), stable, safe, reduce volatility, guaranteed, locked, operating reserve, "bought in January 2027", "fits in $300k" |
| B building minimum | The least she will put toward the building in 2033, sized to repay her second deposit; "after her 2028 deposit" | The note: matures 15 Nov 2032, 47 days before 1 Jan 2033 (Treasury, dated). Or IBTM: holds Treasuries maturing Apr-Sep 2032 and ends around December 2032 (iShares, dated) | Held to its end; never sold because rates moved | "repays $X" for IBTM; guaranteed; risk-free; "locked 5%"; any 2031 range or top; promised; pledged |
| C stock fund | The building's stretch and her flexibility in 2033, from money nobody else relies on; "after her 2028 deposit" | All of the plan's stock money, about 9% of her money after both deposits (the team's calculation); or VT's stock count and share outside the U.S. (Vanguard, dated) | Held until 2033, never sold for market reasons. A fall shrinks only the stretch above the minimum, never the payments or the minimum | a return forecast, overvalued, CAPE, "halves AI exposure", "known/locked 5.2%", "Laura likes risk", the statistics degree, promised |

### 5.7 What each ≤100-word reflection must contain (written by students after the trades, without AI; TN guide L46-52, VRF)

- [ ] The three official answers: **why**; **how it aligned** with the strategy; **how it served** her goals, funding
  needs or risk. For A, the alignment answer includes the scaling in plain words: WInS shows her plan after both
  deposits, scaled; the funds stand in for the bonds she buys.
- [ ] Which of supported / tested / refined it shows, true to what happened (5.5).
- [ ] Exactly one extra job (5.5).
- [ ] ≤95 words by two counters. At most one number, except the tested reflection, which carries exactly three. Every
  number is dated and graded in words.
- [ ] One case-stated trait that passes the swap test (D6 M125):
  - A: fixed payments only her portfolio may fund (L91-92);
  - B: a figure partners will rely on (L114-116);
  - C: "thoughtful risks" within "an appropriate balance" (L69-74).
- [ ] **Not in any reflection:**
  - Laura quotes; the pull quote as hers; her career story or regret line as a reason;
  - behavioural-trap vocabulary ("loss tolerance", "break-even", "house money", "composure");
  - the statistics degree;
  - reserve size, a facility range or a 2031 figure;
  - WInS profit or rank.
- [ ] The same rule names the IPS will use (a decision-log column, D9 M212).

### 5.8 Data capture (the only thing that must be done on the day)

- Screenshot every WInS position on the fill date and at the Oct 20 close (Wed Oct 21, 07:00 AEDT).
- Curves can be pulled later from treasury.gov. Value the payments with `A2_curve_recheck.py` or `D9_numbers.py` [3],
  never `official_curve_pv.py`, which is fixed to 2026-09-25 (AY2 D7 C5).
- Check the IEF and TLH ex-dividend dates in the window; a distribution of about 0.4% is large next to a signal of
  about 1%.

### 5.9 Never (WInS)

- Never place an order before the gate, and never let the advisor place a trade ("Students should place trades on
  WInS, NOT the advisor", VP).
- Never buy and sell the same security on one U.S. trading day, or "fix" an error the same day ("run with it", VP).
- Never lengthen the hedge to bet on rates (EDV, ZROZ, GOVZ, TLT alone).
- Never buy leveraged, inverse, crypto-linked, thematic or single-country funds, ETNs, or stocks under $5. No Taiwan or
  AI tilt.
- Never put a reserve size, facility range or 2031 figure in a note.
- Never trade for rank, and never tidy up after Tue Nov 3.

### 5.10 Fallbacks (decided in advance)

- **No dated 2032 instrument is listed.**
  - Use the undated stand-in (VGIT, then SPTI, about 4.8-4.9 years).
  - Note B says it moves like a Treasury maturing in late 2032; it never claims a date.
  - The real plan is unchanged: the minimum is a real Treasury bought in January 2028.
- **The two-reader check fails twice after redrafting.** Choose (iii), Laura's literal January-2027 book.
  - Orders: IEF 34.9 / TLH 63.1, re-priced on the trade date, plus the leftover in SGOV or BIL only if it is at least
    $1,000 at trade-date prices. Otherwise a listed dated payment rung; otherwise revert to (ii)R (ticket v1 s2; T2
    finding 1).
  - One reflection answers "why so little stock" with the forced-versus-chosen content.
- **The team votes ALT.** Use ticket v1 (ii) at 50/50: IEF 23.5 / TLH 42.5 / VT 17.0 / VGSH 16.0 / cash 1. Note C
  becomes the VGSH note, never "the floor" or "already owned". Record the growth-money bond choice (short or dated,
  AX1 C18) before the VGSH order.

---

## 6. Changes against the current strategy (brief s7 and CLAUDE.md), ranked; and what was rejected

### 6.1 Accepted changes, ranked by deadline (TN first), then by impact on reaching the semifinals (impact grades INT)

| Rank | Change | Serves / by | Impact | Evidence and numbers | Side effects |
|---|---|---|---|---|---|
| 1 | Gate votes this week, each after own-words notes; roles; decision log (rule-name and evidence-grade columns); AI-use log backfilled | WInS/TN; Tue Sep 29-Thu Oct 1 AEST | High | CLAUDE.md "The team has not read the memos yet" (VRF); PM-01, PM-05, PM-08 (E5, INT); R-W46, R-W51 (VP) | Hours this week, during NSW school holidays if they apply (UNVERIFIED for the team, E5) |
| 2 | Central idea worded as a split of jobs; scaling markers inside notes; the two-reader check | TN and IPS; before the first note | High | E2 C1 and F4; AY2 rank 1; E3-10 (VRF/INT) | 15-20 characters per note |
| 3 | WInS book (ii)R: operations hedge, dated building minimum, stock fund (replaces the "~65% Treasuries / ~35% equity" mirror, which was hedge/growth, not bonds/stocks, F-409) | WInS/TN; by Fri Oct 2 ET | High | Section 5.1; E4 L6; T2 one-session test | VT shows 8.7%, not 17%; IBTM or the note is unconfirmed |
| 4 | Notes drafted by students from elements; ≤300 characters; zero-risk box test; five-word copy check; the team's own labels | TN; every order | High (PM-04 is severe) | T2 findings 6 and 8; AY1 D12 C1-C2; R-W26/R-W49 (VP) | None |
| 5 | Three-note plan: A tested, B refined only if logged, C carries the growth-first story; one extra job per reflection | TN; reflections Oct 21-22 AEDT | Medium-high (Articulation) | E2 F8-F9 (INT); D7 with AY2 | None |
| 6 | One vocabulary: "certainty" for the payments, "confident" for the range, "credibility" for her standing; "moves like / stands in for"; never "promised" for the stretch | TN and IPS | Medium | D9 M062 with AY2 C2; E3-1 | None |
| 7 | Data capture on the fill date and at the Oct 20 close | TN | Medium | AY2 D7 C5 | Ten minutes |
| 8 | Format stance: Letter at Word "Double"; ≤470/≤48 words by two counters; PDF checks; title page copied from the roster | IPS; every draft from Oct 26 | **Fatal if missed** | IPS guide L82-123 (VRF); D9/AX2 C3 (0-2 spare lines at 27.6 pt); E5 PM-02, PM-18 | Fewer words than E1 budgeted |
| 9 | At most 12 ideas in 10 blocks on four dated decisions (replaces "Rule 1-4 + G" and E1's ~55 ideas) | IPS; idea list Sat Oct 24 | High | E2 F1-F2; PM-03; last year's lesson (CLAUDE.md, VRF) | Some true points move to the Final Report |
| 10 | Pitch: purpose first, three elements, no numbers, no date claims | IPS | High | E2 F3; E3-5; D7 M011 (the date claim fails in about 1 path in 3, MODEL) | Loses the vivid date |
| 11 | **Architecture change:** the building minimum (= the second deposit's dollar amount) is bought in January 2028; the rest is one world stock fund held to 2033; nothing is traded in 2031. This replaces "growth sleeve ~60% equity + 80% of the sleeve locked in a 2-year Treasury in 2031" | IPS (and WInS now) | High (strategy and credibility) | E6 [2]: total p5/p50/p95 $182k/$207k/$250k vs $168k/$210k/$266k; the bottom is fixed at $150k vs $134k/$167k/$211k. On the same paths ALT minus REC: p5 -$23k, p50 +$1k, p95 +$32k. History (rescaled): worst $169k vs $120k; p10 $185k vs $174k; median equal ($214k). No path ends below the money put in ($157,736), against 1.7% (MODEL). AX1 C6 withdrew the old "$101k vs $165k" rejection | Stock share about 9% in every year 2028-32 (average 7.5% vs 9.7%); p95 -$16k; median gift $174k vs $186-188k; kept money $32k vs $21-24k; the gift is capped at the top |
| 12 | 2031 range: owned minimum up to minimum + half the fund's value that day, capped; the chance of reaching the top is stated (history and model named in the Final Report). Replaces "upside with a stated model probability" and E1's uncapped p90 top | IPS | High (Creativity and Presentation; Client Knowledge) | E6 [2]; E4 [5]; AX1 C2-C3; D5 finding 5 met by reporting P(top reached), never "100% within" | Strong markets raise kept money, not the gift; she may add in 2033 |
| 13 | Certainty definition with two gaps, one clause each (the January 2027 price; nominal dollars against Taiwan costs and currency) | IPS | Medium-high | Brief s16 (binding); E1 P2; AY2 D9 C2-C3; F-114: $50k is worth $42,063 (2033) and $33,681 (2042) in 2026 dollars at 2.5% (ASM) | About 50 words |
| 14 | Risk by goal: forced vs chosen, what stocks are for, the most markets can take; no CFA labels, trap words or diagnosis; the statistics degree used zero times | IPS; TN reflections | Medium-high (PM-07) | E3 findings 2, 3 and 6; E3-9; D3 AX1 C19; payments cost 97.4-98.1% of the first deposit (E3 [1]) | None |
| 15 | 2027 rule: buy on arrival, longest-first with its reason and the first-year counterpoint; no staging; leftover in bills | IPS | Medium | D1 with AX1b; E3-7; E2 F7c | One clause |
| 16 | 2028 deposit rule: completion first; one labelled stress clause; joint tail named once (replaces "only the facility shrinks") | IPS | Medium | AY2 D8 C1; P4; E2 C6 (the $150k doubted once, R-AN35) | None |
| 17 | Diversification (purpose and date) and liquidity clause | IPS | Medium | IPS L46 (VRF); E2 F5; M035 | About 25 words |
| 18 | 2033 order of use: reserve composition over time; gift ≤ top; kept money in U.S. dollar bills; U.S. dollars binding; no New Taiwan dollar hedge; building-cost drift named | IPS | Medium | P8-P9; AX2 D4 C1, C3; IPS L48-50 (VRF) | None |
| 19 | Governance: what stays hers; never because markets moved; reviews on the four dates; no rebalancing between parts | IPS | Medium | P10; E3-8; CFA 2010 2a-2b, 4c (VP via D8/D10) | None |
| 20 | Cost principle kept as one clause (extended to protect the minimum) | IPS | Low-medium | E3-4; E6 [6]; BS-01 | About 15 words |
| 21 | Paraphrase test (6 unpaid readers, two rounds) and the explain-back check | IPS | Medium-high | D12 M234 (digital.gov method, VP); E2 F10; PM-01, PM-03 | About 2 student-hours per round |

### 6.2 Rejected or not chosen (one line each, with the reason)

| Proposal | Why not (evidence) |
|---|---|
| **ALT: E1's 2031 lock** (50/50 growth money reset yearly, then 80% bought in 2031) | On the same basis it is REC plus a bet: p5 -$23k, median +$1k, p95 +$32k. Its bottom depends on 2028-30 markets (p5 $134k; $93k in a 1929 window). It needs a growth-mix rule, a band and a percentile. Its best points (more stock in 2028-30, a higher median bottom) are real; it stays as the documented alternative (section 7, D2) |
| Growth sleeve ~60% equity (CLAUDE.md call 1) | Superseded by the architecture. The shares D6's rule picks (55-70%) depend on the fee and the forecaster (AY1 C1); the median ties |
| 50/50 vs 60/40 debate (E1 P5, D2, D6) | Moot under REC. For ALT, 50/50, owned as a choice of spread, with no fee-dependent claim (T2 finding 2) |
| E1's slices 80/10/10 or 70/15/15; top percentile q of 80/85/90 | Moot: REC has no lock share and no model percentile |
| Uncapped gift with a model top (D5, E1 P7) | The top would rest on a model that has too few very bad years (AX1 C12): "80%" tops landed within the range 62-93% of the time across models and history. A capped market-value top needs no model |
| "Give 90%, capped" (D3 M039) | It promises less than is bought (AX1 C3) |
| A minimum sized as a share (two-thirds or 0.8) instead of the deposit amount | A free parameter. The deposit amount is case-anchored (E4 C2). Two-thirds is kept only as the equal-risk sensitivity (bottom $134k) |
| s = ¾ or s = 1 | s = 1 leaves nothing kept whenever stocks fall, failing case test 5 (L145; E4 2.1). s = ¾ matches E1's median gift but its kept money at p5 is only $8k (E4 [2], MODEL) |
| Ratchet (lock in thirds, 2029-31) | A second rule for $2-6k (AX1 C11) |
| Staged purchase or a yield trigger in 2027 | No reliable gain; a 27-35% chance of needing the 2028 deposit (D1 [7], AX1b item 11) |
| Nearest-dated payments first | More top-up price risk (+15% vs +5%) and more face unbought if the deposit never comes (AX1b item 23) |
| Rolling the 2037-42 payments short ("tiering"); partial locks of the payments | +$20k per -100bp (F-108); partial locks fail in 13-26% of paths without the deposit (D3 M243) |
| TIPS for the payments or the minimum | The promise is fixed in nominal dollars; TIPS track U.S. prices, not Taiwan's costs or the exchange rate (brief s8 item 10; E4 1.4) |
| Converting to, or hedging into, New Taiwan dollars in 2031 | A forward is a derivative (banned in WInS; the safe reading for the plan, R-AN15); about 5.9% cost at today's rate gap (ASM; the Taiwan 2-year yield is SNIP) |
| EWT, AI, thematic or single-country tilts | Tokenism and concentration (D8 M081; D13c R3; S2) |
| The "middle path" WInS book (a 0.9% VT sliver) | A weak note, and it reverses the T-bill rule (D10) |
| (iii) as the default book | Two decisions plus filler without a rung (T2 finding 4; E2 F4). It stays the fallback (5.10) |
| A planned "discipline/rebalance" trade; the SPTL split as a "refinement" | A band fires before Oct 23 in about 0-2% of cases even in a crisis (AY2); a pre-planned split is not a refinement (AY2 D7 C1) |
| A payment rung under (ii) | A second future-funding note (AX1b item 7) |
| A funded-ratio "below 100%" trigger | It can never fire once the payments are bought (D10 finding 6) |
| A fee number, a New Taiwan dollar figure, stage-by-stage stock shares, a "letter to Future You", CFA labels, "our portfolio manager approves", the statistics degree, any Laura quote | Words that do not change a decision, or that break the D13, IPS or advisor rules (E1 P17; E2 F1; E3-6, E3-9; R-W19) |

---

## 7. Team decisions still open: recommended default and the test for choosing

| # | Decision | Default (INT) | Test for choosing | By (AEST/AEDT unless ET) |
|---|---|---|---|---|
| D1 | Adopt lock-early (gate a) | Adopt | Every student writes, with no AI file open, why the payments are bought first. The vote is logged with those reasons | Gate, Thu Oct 1 |
| D2 | REC (minimum bought in 2028) or ALT (2031 lock) | **REC** | **(1) Values:** each student states which matters more for Laura. Either a building minimum no market can lower from 2028, with better bad cases for about the same middle outcome; or more stock in 2028-30 and a higher announced bottom in typical markets, at the price of a worse bad case. **(2) Explain-back:** every student explains the chosen design's four dates in two minutes without notes. If only one design passes for all six, choose it. The numbers the team sees are E6 [2] and [5] | Gate, before any building or stock order |
| D3 | WInS book | **(ii)R** | The two-reader check (5.4e), and whether the team can state the scaling in its own words in about 25 IPS words (E1 P13 decision test). Two failures lead to (iii) | Gate |
| D4 | WInS instrument for the minimum | The 2032 note, then IBTM, then VGIT | Whichever is listed, in that order (5.2) | Gate |
| D5 | The team's labels for the three parts | The team's own words (no default wording is given) | The labels survive the explain-back and appear identically in the notes, the log and the IPS | Before the first note |
| D6 | Share of the stock fund added to the gift (s) | **One half** | The kept money at the median is about three years of Taiwan building-cost drift on the gift (s = ½: $32k against about 11% of $174k; ASM check, not a contingency fund). It is the plainest split to explain | Section-4 vote, Mon Oct 26 |
| D7 | Cost clause in the IPS | **Keep (one clause)** | If the PDF has fewer than 2 spare lines, compress it inside the governance sentence; cut it only if the fee base in the Final Report will never touch the promises (R8) | Oct 26; Nov 4 |
| D8 | Statistics degree | **Zero uses** in the TN and IPS | Use it once only if it changes a decision, never as a compliment (E3-9; AX1 C19) | Idea list, Oct 24 |
| D9 | Paper and line spacing | **U.S. Letter, Word "Double"** | The exported PDF ends on page 3 with at least 2 spare lines. "Exactly 24 pt" is a documented last resort | Nov 4 |
| D10 | Joint tail in the IPS | **One clause** | A reader answering "what could still stop a payment?" gives: a rate fall before January combined with a missing deposit, or a U.S. default (D12 M234) | Oct 26 |
| D11 | Repository visibility until Dec 4 | The team leader decides; revisit and log | The PM-30 trade-off (copying, AI-record accuracy) against the team's earlier acceptance (CLAUDE.md) | Fri Oct 2 |
| D12 | Roles | Assign now | Every student owns at least one note or reflection and one IPS block | Tue Sep 29 |

**Calendar anchors** (E5 [1], derived with zoneinfo):
- Roster due Sat Oct 10 08:00 AEDT; submit it Wed Oct 7.
- TN due Sat Oct 24 08:00 AEDT; submit it Thu Oct 22.
- IPS due Sat Nov 7 09:00 AEDT; submit it Thu Nov 5. U.S. clocks change on Nov 1.
- Brisbane is 1 hour earlier; Perth 3 hours earlier.

---

## 8. Three final checks

### (a) Every decision traces to Laura or the case: **PASS**

The two judgement calls are flagged (ASM/INT, each still anchored to the case).

| Decision | Case line or Laura fact (VRF unless marked) |
|---|---|
| Buy all ten payments first, with Treasuries held to maturity | L88-92 (fixed $50k; "high degree of certainty"; no outside money) |
| Buy on arrival; longest-first; completion from the second deposit | L91; L43-45 ("will contribute" at the start of 2028); L59 (flows at the start of the year) |
| Building minimum = the second deposit's dollar amount, bought when it arrives | L43-45 (her career earnings); L110-112 ("meaningful personal contribution" signals viability); L114-116 (overpromising damages credibility); L69-74 ("protecting the capital"). *Judgement call 1 (INT): reading "protecting the capital" as returning her contribution whole for the building* |
| All money nobody relies on in one world stock fund | L69-74 ("thoughtful risks", "pursuing growth"); L61-65 (living costs outside; no withdrawals); L85-86 vs L91-92 (others may help the facility, never the payments) |
| No tilts; broad funds | R-AN34 (no values or theme in the case); brief s4 tokenism rule |
| 2031 range method and two-sided confidence | L109-120 |
| Cap, and kept money for flexibility | L101-103 (she decides; "as the project develops"); L118-119. *Judgement call 2 (ASM): half, sized against Taiwan building-cost drift (F-508, VP inputs)* |
| Reserve = the ladder, named in 2033, changing only as bonds mature | L94-97 ("if at all") |
| Certainty by price, with two gaps; U.S. dollars binding; no New Taiwan dollar hedge | L97-99; L90; L146-148; R-AN10; R-AN15; WInS derivatives ban (VP) |
| Governance: she decides her two calls; rules change only for her circumstances | L101, L110; IPS L73-74; Guide p.5 |
| Cost principle | L43 ("with an asset management firm"); R-W29 (VP). The case is silent on fees, so this is labelled a team assumption |
| WInS book (ii)R and the scaling sentence | L129 (WInS = implementation); IPS L75; R-W71 (VP) |
| No Laura quotes, no identity reasons, no degree hook | Brief s16 (D13 rules); D13c section 5 |

### (b) Nothing is more complex than it needs to be: **PASS**, with one watched item

- **Money rules:** four dated decisions plus governance. **Parameters:** the minimum's size (set by a case number) and
  "half". The cap is a yes/no that replaces a model percentile.
- **Removed from E1:** the growth-mix rule, band and yearly reset; the lock share; q; the uncapped/cap debate; the
  VGSH-versus-dated question; six E1-C conflicts. The IPS drops from about 55 specified ideas to 10 blocks (E2 3.2, INT).
- **Complexity that stays, and why it earns its place:**
  - the rates-fall branch binds in about 1 path in 3 (MODEL);
  - the joint-tail clause is required for a frozen rule not to overclaim (AY2 rank 2);
  - the WInS scaling sentence is required for consistency (D10 1.5);
  - the cap branches are forced by a rule the team cannot see yet.
- **Watched item:** book (ii)R costs 15-20 characters of scaling marker per note. That cost is earned only if the
  two-reader check passes; otherwise the fallback is (iii) (D3 test).

### (c) Nothing requires trading outside the WInS rules: **PASS**, conditional on the gate

| Rule (VP: SMApply Trading Details and FAQ; 2026-27 User Guide) | How the plan complies |
|---|---|
| Permitted: cash, stocks ≥$5, "Any ETF available on WInS", government/Treasury bonds available on WInS | Only ETFs (IEF, TLH, SPTL, IBTM, VT; alternates VGIT, SPTI, VTI, VXUS), one possible Treasury note, and cash. Each is pending the listing check (gate c) |
| Banned: margin, short selling, stock-secured debt, crypto, derivatives, "anything else" | None used. No leveraged, inverse, options-based or crypto-linked fund (R-AN49), no ETN. Cash float ≥$1,000 at next-open prices (T2 finding 1) |
| "Day Trading: This is not permitted." | First session is buys only. No same-day sells. Any later re-mix happens on another day |
| No trade above 2× a security's daily volume | The largest orders are tiny against volume (IBTM ~3,336 shares vs ~216k a day; TLH ~1,365 vs ~1.97m; VP volumes via ticket v1/E4). Vanguard volumes are read in WInS |
| Up to 200 trades; commissions $25 per ETF and $10 per bond | 4-6 trades, $50-150 |
| Position limit (Session Rules) | Branches decided in advance (5.3); stop and ask below about 17% |
| Activity minimum (undefined publicly, R-W23) | If one exists: ask Wharton, and meet it only with plan-consistent, logged trades; never staged ones (PM-15) |
| The real plan (not WInS), under the safe reading of "Investments permitted (for BOTH contributions)" (R-AN15) | Treasuries (STRIPS and one zero for the minimum), one broad stock ETF and Treasury bills. No forwards or other derivatives |

---

## 9. Conflict register: every conflict, which side wins, and why

| # | Conflict (sources) | Winner | Why (evidence) |
|---|---|---|---|
| 1 | Floor timing, 2028 or 2031 (E4 C1; AX1 C6; E2 R2 and section 5; T2 finding 5; ticket gate b) | **2028 (REC)** | The same median with a better bad case and better history, on the same basis (E6 [2], [5]). This is the plan's own tie-break rule. It also removes three rules. E1's rejection rested on a withdrawn figure (AX1 C6) |
| 2 | Size of the bottom: the deposit amount or a share (E4 C2) | **Deposit amount** | Set by a case number, with no free parameter. The IPS can name it as a rule output |
| 3 | Capped market-value top or uncapped model top (E1 C3/C5; E4 C3; D3/D5; AY1 C11; AX1 C2-C3) | **Capped market-value top, reporting P(top reached)** | Model-free and checkable against history. D5's "100% within is empty" is met by reporting the chance of reaching the top. Money above the top stays hers (AX1 C15) |
| 4 | Growth split 50/50 or 60/40 (E1 C2; E3 K6; E5 C6; T1; T2 finding 2; D2 vs D6) | **Moot under REC** (50/50 for ALT) | The stock fund is 100% stocks. The split is set by the jobs, not a probability rule |
| 5 | Short or dated bonds for the growth money (AX1 C18; E2 R1; E4 L4) | **Dated** (the minimum matures before 2033) | The money has a known use-date; a dated instrument removes reinvestment risk. VGSH is dropped |
| 6 | WInS book (ii) or (iii) (E1 C1; E3 K3; E5 C1; D10 vs T1/D12; T2 finding 3) | **(ii)R**, with the two-reader check as the tie-breaker | Three decisions and jobs; funding-purpose diversification; survives one session; copes with caps. (iii)'s literal truth is kept as the fallback |
| 7 | The third note: VGSH or a dated rung (E1 C6; D1 vs D12; AX1b item 7) | **The dated building minimum** | A distinct job, Laura-specific and dated (E4 L6) |
| 8 | VGSH role word (E1 C7; AY1 C10) | Moot | VGSH is not in the REC book |
| 9 | Kept money after 2033: bills or invested (E1 C8) | **U.S. dollar Treasury bills** | Flexibility is for surprises; no case line supports growth for this money (D8 M081) |
| 10 | Where the longest-first counterpoint lives (E1 C9; E3 K8) | **In the IPS rule's "because"** (E3) | A client would ask which operating year is exposed (E3 Q2); it costs one clause |
| 11 | Note length (E1 C10) | **Draft to 300 characters, and test at zero risk** | The evidence is mixed (AY1 D12 C2) |
| 12 | Fee clause (E1 C11/P12; AY2 C13; E3-4/K2; E5 C2) | **Keep one clause** (E3) | It protects both bought amounts (E3 condition 2), and the Final Report's fee base is decisive (E6 [6]). Under REC the growth reason no longer rests on a fee |
| 13 | Stock shares by stage in the IPS (E1 C12; E2 3.4) | **Leave them out**; use one forced-caution price fact | Four shares confuse a first reader (E2); under REC the share is about 9% in every year after 2027 anyway |
| 14 | Label of the 2031 middle slice (E3 K1) | **Owned / expected / kept; never "promised"** | Case L110, L116 ("expects", "potential contribution"); D9 M062 |
| 15 | Statistics degree once or never (E1 P17; E3 K4; E5 C3; AY2 C6) | **Never** | It risks being a persuasion lever (AX1 C19); the certainty definition shows the respect anyway |
| 16 | Pitch order (E3 K5) | **Purpose first** | E3-5; E2 F3; the D13c communication checklist |
| 17 | Central idea as a timing ban or a split of jobs (E1 P1 vs E2 F4, E4 L5) | **Split of jobs** | True in the plan and in the WInS book (AY2 rank 1) |
| 18 | IPS structure: "Rule 1-4 + G" or four dated decisions (E1 P11 vs E2 F2) | **Four dated decisions** | The order a reader expects; the rule names live in the log |
| 19 | Density: E1's elements or about 12 ideas (E1 P16 vs E2 F1; PM-03) | **10 blocks, ≤470 words** | The page-fit ceiling (D9; AX2 C3); last year's lesson |
| 20 | Risk tolerance in CFA three-factor terms or in plain goal-by-goal terms (E1 P6 vs E3) | **Plain, goal by goal**; the CFA framework stays internal | The IPS bans citations; E3's "analysed, not understood" risk |
| 21 | Bad-year pre-commitments framed as behavioural traps or as the firm's discipline (E1 P10 vs E3-6) | **The firm's discipline and her public word** | Case L68-69: she already understands volatility |
| 22 | The $150k doubted in three places or one (E1 P2-P4 vs P17; E2 C6) | **One labelled stress clause** | Case "will" (R-AN35). Gap (i) mentions the deposit only as the completer |
| 23 | "Fully funded by 1 Jan 2028 at the latest" (D1) | **"When the second deposit arrives"** | AX1b item 3 |
| 24 | "Only the facility shrinks" (D8 rule 1; chair memo) | **Joint tail stated** | AY2 D8 C1; D1 finding 4 |
| 25 | Guide p.5 as a reason against changes before Nov 6 (D1, D2) | **It does not apply before Nov 6** | AX2 D2 C3; AX1b item 4; Guide L89-90 |
| 26 | The SPTL cap split as a "refinement" (D7) | **Not a refinement** | It is decided before the first order (AY2 D7 C1) |
| 27 | "The hedge is never traded" vs the ticket's re-mix band (D7) | **Never sold or trimmed; only re-mixed** | AY2 D7 C7 |
| 28 | P(ladder > $300k): 1 in 4 or 1 in 3 | **About 1 in 3** for the real Nov-15 ladder | AX1b item 1; AX1 C8/V5; 176 of 185 days in 2026 |
| 29 | Hedge target 9.90 or 10.16 years | **"About 10 years"** | S4 finding 8: issuer durations sit 0.2-0.3y below full-revaluation durations |
| 30 | The all-Treasury comparison called "riskless" (D3) | "**All-Treasury benchmark**" (Final Report) | AX1 C5: not riskless seen from today |
| 31 | "Needs met at today's yields" (D8 headline) | **Corrected**: the payments need what the bought ladder earns; the facility has no required size | AY2 D8 C2 |
| 32 | VGSH "already owned" / "the amount she can promise" (D9, ticket v0) | Moot | VGSH is not in the REC book; the wording ban stays for ALT (AY2 D9 C1) |
| 33 | Council's nearest-first vs longest-first (brief s10) | **Longest-first** | D1 [3]; AX1b item 23 |
| 34 | "Fits inside $300k" / "bought in January 2027" as headlines (brief s7) | **Dropped** | D7 M011; D1; true in only about 2 of 3 rate paths |
| 35 | Stock fund rebalanced or not (D8 rule 2 vs E4) | **Not rebalanced; written down** | Its risk is the risk stated (100% stocks in money nobody relies on); CFA 4c: a no-rebalance policy is documented |
| 36 | Semifinal basis: IPS + Final Report or all three (E5 C7; X-8) | **Treat all three as scored**; weight hours to the IPS after Oct 23 | R-AN41; the SMApply page |
| 37 | Paper and spacing (E5 C4-C5; AY2) | **Letter, Word "Double"** | Fitting under the strictest reading removes the question |
| 38 | Public repository (E5 C8) | **Team leader's call; revisit and log** | Outside strategy; PM-30 |
| 39 | The rival's "stock fund 100% after she speaks" vs E1's lower post-2031 stock | **Accepted** | Bad 2031-32: the gift is $169k at the median and stays at or above the bottom in 100% of paths (E6 [3]); the cost is the stretch only |
| 40 | E1's lean on (ii) at 17% VT vs E3/E5's timidity worry | **Answered by framing, not by more stock** | Forced vs chosen; "all money nobody relies on is fully in stocks"; the most markets can take is stated. The team may still choose ALT for more stock (D2) |

---

## 10. Later (after Nov 9), one line each (Final Report; not worked here)

- The 2031 range in dollars at weak, median and strong 2031 states; the likely figure beside it, not the midpoint.
- The chance of reaching the top: U.S. history (two-year periods since 1928) and the model, both named.
- Named historical windows beside the model's p5 (E4 [5]; E6 [5]).
- The all-Treasury benchmark and the rejected alternatives (growth-first, the 2031 lock, the uncapped percentile top).
- The fee assumption, its base and net-of-fee figures (R8; E6 [6]).
- A New Taiwan dollar reference at a dated rate; the building-power assumption line (D4).
- The reserve's market value on 1 Jan 2033, with cost and face; the rung-by-rung ladder (S3).
- The fundraising excerpt order: operations funded for ten years; the minimum owned since 2028; the stretch and its odds;
  what is not promised; U.S. dollars binding (M008, M015, BS-17).
- The decision-log traceability table and the paraphrase-test log.
- At most one or two dated, verified Laura lines in context (D13a/D13c).

---

## Sources (accessed 2026-09-27/28)

**Official, in the repo (VRF):**
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`: L16, L43-45, L59-74, L83-120, L123-133, L136-148,
  L161-169.
- `2026_WGY_Investment_Policy-FINAL.txt`: L3-28, L31-41, L45-78, L82-125.
- `2026_WGY_Trading_Notes_Analysis-FINAL.txt`: L4-31, L36-53.
- `2026_WGY_Investment_Competition_Guide.txt`: L70-94, L154-159, L181-186.
- `2026_WGY_Competition_Infographic.txt`.
- `SMApply_Deliverables_Page_2026-09-27.md`: L8-17, L49-57.

**Market data (VRF):** `competition/official_market_data/daily-treasury-rates_2026-09.csv` (row 09/25/2026);
`JPM_LTCMA_2026_US_matrix_USD.pdf` p.2.

**Primary web (VP):**
- iShares IBTM, https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf. Re-read by E6 on
  2026-09-28: NAV $21.83 (9/25), expense 0.07%, and both quoted sentences found verbatim.
- Carried by the cited files, not re-opened by E6:
  - SMApply Trading Details and FAQ, https://wghsinvcomp.smapply.us/res/p/trading/ and /res/p/faqs/;
  - Wharton Rules & Roles and the AI policy;
  - the 2026-27 WInS User Guide;
  - issuer pages for IEF, TLH, TLT, SPTL, VT, VGIT, VGSH, SGOV, BIL (ticket v1 s12);
  - Damodaran histretSP (via the D3 snapshot); FRED DGS10 and DEXTAUS;
  - the Vanguard VCMM page;
  - CFA Institute, *Elements of an IPS* (2010) and *Asset Manager Code*;
  - digital.gov paraphrase testing;
  - the NSW term and HSC pages (via E5).

**Research files (lower authority; audit corrections applied):**
- `research/insight_v1/phase_E/E1_change_proposals.md`, `E2_judge.md`, `E3_laura.md`, `E4_rival.md`,
  `E5_premortem.md`.
- `phase_D/` D1-D12, D3_quant and D3_model_v2_results (AX1), D13a, D13c, `audit_*.md`, `trading_now_brief.md`.
- `wins_now/securities_and_allocation_v1.md`, `T2_red_team.md`, `S4_red_team.md`.
- `phase_A/case_register.md`, `fact_register.md`, `stakeholder_map.md`, `wins_week1_guardrails.md`.
- `phase_C/survivors.json`, `parked.json`.
- `research/council_2026-09-27/01_chair_memo.md`, `round2_referee_ruling.md` (history); CLAUDE.md.

**Scripts:** `research/insight_v1/scripts/E6_final_checks.py` (new). Re-run: `E1_split_and_slices.py`,
`E3_client_view_numbers.py`, `E4_rival_numbers.py`. Figures quoted from D1, D3, D4, D8, D9, T1 and T2 are as reproduced
by their auditors.

---

## What this teaches

1. **Keep the insight; change what earns nothing.** The winning idea was right from the council onward: buy the
   payments first. What changed is the part added around it. A balanced growth sleeve that is locked later turned out
   to be a coin flip on top of a simpler design, with the same middle and a worse bad case. When two designs tie in the
   middle, the one with the better bad case and fewer rules wins. That rule was already in the plan; this file only
   applied it consistently.
2. **Compare designs on one basis before choosing.** The early lock looked worse until it was compared at the same
   stock risk, on the same simulated paths and on a century of real history. Most arguments between experts dissolve
   once everyone uses the same yardstick.
3. **A number the client already knows is the most credible number.** Her second deposit is a figure she, her partners
   and the case all share. Building the bottom of the range on it needs no forecast. Only the top carries a chance, and
   that chance can be checked against history.
4. **Put all the risk where it belongs, and none where it doesn't.** "Half stocks, half bonds everywhere" dilutes
   twice. "Nothing at risk that others rely on; everything else fully invested" is easier to explain, and it answers
   "thoughtful risk" in a way a reader can see.
5. **The scored thing is the written page.** The strategy survived every audit. What decides the semifinal is whether
   six students own it, write it in their own words, keep the notes and the IPS saying one thing, and fit it on two
   pages. Most of this file is about those joints, because that is where plans usually fail.
