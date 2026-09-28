# IPS specification: what the 50-word pitch and the 500-word IPS must contain (no drafted text)

**Summary (5 lines)**
1. Central idea = a **split of jobs**: money other people will rely on (ten operating payments, the building minimum) is bought when her money arrives and held; money nobody relies on is fully in world stocks (E6 s2, INT).
2. The IPS = 10 content blocks on the four case dates (2027, 2028, 2031, 2033), ≤470 words, pitch ≤48 words, by two word counters (E6 s3, INT); every guide requirement is mapped below with its line (VRF).
3. Ten decision rules (R1-R10) must be fixed by vote and logged by Mon Oct 26 AEDT, because the strategy freezes at the deadline and the Final Report may only apply them (IPS guide L73-74, VRF).
4. Format breaches are fatal ("will not be considered for semifinal selection", L82-83, VRF): Letter, Times New Roman 12, Word "Double", 1-inch margins, exactly 3 PDF pages, ≤5 MB, no charts/links/footnotes/citations/quotes.
5. Due Fri Nov 6, 5:00 p.m. ET = Sat Nov 7, 09:00 AEDT (SMApply L10, VRF; conversion DER, E5 [1]); team targets: words frozen Tue Nov 3, PDF check Wed Nov 4, submit Thu Nov 5 (ASM team rule, E6 s3.3).

**Serves: IPS** (Trading Notes only through the consistency checks in section (i)).

W2 writer, insight_v1 run, 2026-09-28. **Authority:** `research/insight_v1/phase_E/E6_final_spec.md` (cited "E6 s<n>"). This file re-states its decisions for the IPS; it decides nothing new. **Nothing here is text to submit.** The six students write every pitch and IPS sentence in their own words; Wharton's AI policy requires any AI use to be credited in the Final Report's Works Cited (R-W46, VP via E6). No Laura quotes appear in the IPS (brief s16, binding). Everything below assumes the team adopts lock-early and **REC** (E6 decision D1-D2, both still open votes); if the team votes ALT, sections (c) R2/R4 and (k) change as E6 s5.10 and s7 say.

**Status labels** (brief s3): **VP** = VERIFIED-PRIMARY (read on the primary page); **VRF** = VERIFIED-REPO-FILE (official or primary file in the repo, with line); **SNIP** = SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION (a chosen input or team rule); **MODEL** = output of an assumption-based simulation, never a forecast; **DER** = derived by arithmetic or a script from labelled inputs; **INT** = E6's or this writer's judgement, never a fact about Laura; **UNVERIFIED** = not yet checked. Line numbers: "L" alone = the IPS guide `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`; "case L" = `Laura_Gao_2026_Client_Profile.txt`.

**Terms (defined once; for the team's understanding, not IPS vocabulary):**
- **Treasury:** a bond issued by the U.S. government. **Zero-coupon Treasury (STRIPS):** pays one fixed dollar amount on one date and nothing before. **Treasury bills:** Treasuries maturing within a year, used here as a cash place.
- **Ladder / rung:** ten zero-coupon Treasuries, each maturing on 15 Nov before one $50,000 payment (2033-2042); a rung is one of them (E6 terms).
- **Building minimum:** one zero-coupon Treasury bought in January 2028 that repays the second deposit's full dollar amount shortly before 1 Jan 2033 (E6 terms, INT design).
- **Stock fund:** one broad world stock fund (an **ETF**, a fund traded like a share) holding all money the ladder and the minimum do not need.
- **Kept money:** whatever the 2033 rule does not give to the building; Laura's flexibility.
- **Default:** the U.S. government failing to pay a Treasury in full and on time. **Nominal:** in plain dollars, not adjusted for rising prices (inflation).
- **Rate sensitivity (duration):** roughly how much a bond fund's price moves when interest rates move; "about 10 years" means about 10% per 1 percentage point.
- **bp:** 0.01 percentage point. **p5 / p50 / p95:** the value 5% / 50% / 95% of simulated paths fall below (p50 = median).
- **Co-sponsor:** a partner Laura will ask to help fund the facility from 2031 (case L109-116, VRF). **Derivative / forward:** a contract whose value depends on another price, e.g. an agreement to swap currencies later; banned in WInS (VP via E6 s8c).

---

## (a) The central idea and the 50-word pitch

### a1. Central idea (content, not wording) (E6 s2, INT)
- **A split of jobs.** Money others will rely on (the ten operating payments; the building minimum she will announce) is bought when her money arrives and held to its date, never taking stock-market risk. Money nobody relies on is invested fully in world stocks.
- **Consequences the idea must let a reader see:** once bought, the payments depend neither on markets nor on her next contract (her second deposit is career income: "using earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial ventures", case L43-45, VRF); she tells partners only what she already owns, plus a stretch whose odds anyone can check.
- **Why not a time-worded ban** ("no stock risk until all ten payments are bought"): the WInS book buys world stocks on day one and the notes are read before the IPS, so a ban reads as a contradiction; a split of jobs is true of both Laura's plan and the WInS book (E2 C1/F4; AY2 rank 1; INT). The "payments first" ordering lives inside the 2027 and 2028 rules, not in the pitch.

### a2. What the pitch must contain (official requirement: "Maximum 50 words" L33; "Quickly summarize your team's investment strategy. Clearly communicate the central idea behind your approach and how it is designed to support your client's financial goals and future funding needs." L35-36, VRF)

| # | Element (the team writes the words) | Must carry | About (INT) |
|---|---|---|---|
| 1 | **Purpose first** | What the plan secures for the residency, named by what it secures (its ten years of operations), before any instrument or prohibition (E3-5; E2 F3; D13c checklist) | 12-15 words |
| 2 | **The Laura-specific rule** | Each of her two deposits buys a promise when it arrives: the first, the operating years; the second, the building's minimum from her own earnings. Once bought, neither depends on markets or on her next contract | 15-18 words |
| 3 | **What the rest does + credibility** | Only money nobody relies on is in world stocks, for a larger gift and her flexibility; she tells partners only what she owns | 12-15 words |

### a3. Hard limits and banned content (E6 s2; D9 M062; D13 rules; E3 4c; all INT/ASM team rules unless marked)
- **Length:** ≤48 words, counted by two counters (e.g. Word and `D9_draft_checker.py --kind pitch`), the higher count wins (E5 PM-02). Official cap 50 (L33, VRF).
- **Numbers:** none; at most one if essential. **Tense:** future or conditional; nothing is bought in 2026.
- **Banned words and content:**
  - flat claims "bought in January 2027" or "fits inside $300,000" (false in about 1 rate path in 3, MODEL 30-34%, E6 R1);
  - "guaranteed", "risk-free", "safe", "100%", "95%", a probability, or "certain" without its qualifier;
  - "promise"/"promised" for the stretch above the minimum;
  - jargon: barbell, LDI, duration, STRIPS, ladder, funded ratio, percentile, glide path, liability matching;
  - fund names, tickers, a return target;
  - any quotation, the case pull quote, "Laura said";
  - identity, heritage or Taiwan as a reason; book-title, "falling" or "balance" metaphors (the case's own "appropriate balance" is fine);
  - the statistics degree; "innovative".

### a4. Tests a pitch draft must pass (E6 s2; D12 M234; INT)
- [ ] Six unpaid readers outside the team restate all three elements after one read (paraphrase test; unpaid because paid help is banned, R-W21/R-W28, VP via E5).
- [ ] No reader thinks anything is already bought.
- [ ] Shown the three WInS notes first, no reader thinks the WInS stocks contradict the pitch (E2 s5).
- [ ] Swap test: the pitch fails if it still reads true with another client's name in it (D6 M125, INT).
- [ ] Run `D9_draft_checker.py --kind pitch` (flags jargon/overclaim words; a flag is a prompt to look, not an error, ASM).

---

## (b) IPS content map: guide requirement -> block -> word budget -> evidence

**Whole-IPS rules** (E6 s3, INT unless marked): at most 12 ideas in 10 blocks; one action and one "because" per case date; ≤470 IPS words (hard cap 500, L39, VRF); case facts only where a rule needs them; rule parameters in words ("half", "the full amount of her second deposit"); at most **one** rounded, dated computed figure (the forced-caution fact in B5); no percentiles, probabilities, dollar ranges, tables or lists; every forecast graded ("we assume", "history suggests"); every price dated ("at September 2026 prices"); at most about 15% of words on what could go wrong (ASM ceiling, E3-11); no headings inside the IPS ("You do not need to address these points separately", L66, VRF).

### b1. The ten blocks (content only)

| Block | Requirement it fills (quoted, VRF) | Content the team's sentences must carry (E6 s3.1) | Words (INT) | Evidence (file; status) |
|---|---|---|---|---|
| **B1 Purpose + central idea** | "What is the central idea behind your investment strategy?" (L16); "What your team is trying to accomplish for the client" (L55); "Your client's profile and financial goals should remain at the center" (L27-28) | What the plan secures (ten operating years, then the building minimum, then growth); the split of jobs; her second deposit is her own career income, so once bought the payments no longer depend on markets or her next contract | 40 | Case L43-45, L88-92 (VRF); E6 s2 (INT) |
| **B2 Certainty** | "desired degree of funding certainty" (L10); case: "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" (case L97-99) | (a) bought, not forecast: each payment matched by a Treasury maturing shortly before its date, held to maturity; (b) evaluated by price: on the purchase date the money covers the market price of all ten, no model percentage; (c) residual risk: certain in U.S. dollars barring a U.S. Treasury default; (d) gap (i) January 2027 price; (e) gap (ii) fixed dollars vs Taiwan costs and exchange rate, named not solved | 50 | Case L90-92, L146-148 (VRF); brief s16 (binding); section (e) below |
| **B3 Jan 2027: buy the payments** | "How will the portfolio's asset allocation and composition change as future funding needs approach and payments are made?" (L22-23); "preparing for the operating commitment" (L48) | Buy all ten on arrival, no waiting for better yields (waiting is a bet on rates); if short, longest-dated first, because the waiting piece is smallest and least rate-sensitive and less stays unbought if the next money never came; counterpoint stated: the waiting piece is the first operating year; leftover waits in Treasury bills | 35 | Case L91-92 (VRF); rule R1; D1/AX1b (MODEL) |
| **B4 Jan 2028: finish, minimum, stocks** | "planned changes in the portfolio as future funding needs approach" (L46-47); "determining a responsible facility contribution" (L49) | Second deposit first completes any unbought payment; then buys a Treasury repaying the deposit's full dollar amount just before 2033 (the building minimum; the case's "meaningful personal contribution", case L111); the rest into one broad world stock fund left alone to 2033; **one** labelled stress clause (smaller or later deposit follows the same order; joint tail stated once) | 45 | Case L43-45, L101-104, L110-112 (VRF); rule R2; E4 [7] (MODEL) |
| **B5 Risk and return, goal by goal** | "risk tolerance" (L3); "How does your strategy balance growth, risk, liquidity, funding reliability, and financial flexibility?" (L20, also L59); "approach risk and return" (L46) | Forced caution: at September 2026 prices the payments cost about 98% of her first deposit (the one allowed number), so 2027 holds no stocks by arithmetic; chosen: the minimum takes no market risk because partners rely on it; stocks are for a larger gift and flexibility; the most markets can take = the stock fund; portfolio fact: her income already rides on publishing and speaking, so no themed or single-country bets; returns as a range across two published forecasters, not a target | 45 | Case L68-74 (VRF); E3 [1]: 97.4-98.1% (DER); section (d) |
| **B6 Diversification + liquidity** | "portfolio construction and diversification" (L46); "liquidity needs" (L10); SMApply criterion "uses appropriate diversification" (SMApply page L49, VRF) | Diversified by funding purpose and by date: ten dated payment bonds, one dated building bond, one fund of about 10,000 companies worldwide; U.S. Treasuries for the promises are deliberate (dollar-denominated, dated); liquidity: no withdrawals before 2033, each payment from its own maturing bond | 25 | Case L63-65 (VRF); VT 10,088 stocks, 37.7% non-U.S. at 8/31 (VP via ticket v1 s12; PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK; alternates VTI + VXUS, then ITOT + IXUS) |
| **B7 Jan 2031: co-sponsor range (method only)** | "How will your strategy protect the operating commitment while preserving flexibility for a responsible facility contribution?" (L25-26, L64-65); the final range is NOT expected (L68-69) | Nothing traded; she speaks only once payments and minimum are owned; bottom = the minimum owned; top = minimum plus half the stock fund's value that day; confidence both ways (below bottom only on a Treasury default; top reached if world stocks are no lower two years later, graded "history suggests"); words by tier: owned / expected if stocks hold their value, never "promised"; U.S. dollars binding | 40 | Case L109-120 (VRF); rule R4; numbers go to the Final Report (E6 s10) |
| **B8 Jan 2033: reserve, gift, flexibility** | "managing the operating reserve's asset composition over time, determining a responsible facility contribution, and preserving appropriate financial flexibility" (L48-50) | Reserve = the ladder, bought from 2027, named the operating reserve on 1 Jan 2033 before the first payment; held to maturity; composition changes only as bonds mature (case allows "if at all", case L96); gift = minimum + half the stock fund, never above the announced top; everything else kept in U.S. dollar Treasury bills, hers "as the project develops" (case L102-103); no New Taiwan dollar conversion or hedge before the facility decision; Taiwan building costs expected to rise, so a fixed-dollar gift buys less | 45 | Case L94-107 (VRF); rules R3, R5 |
| **B9 Governance + costs** | "What principles will guide your investment decisions?" (L18); "disciplined decisions during changing market conditions" (L4-5); "How your strategy will guide portfolio construction and investment decisions as the client's needs change" (L61-62); "may not revise its investment strategy after the submission deadline" (L73-74) | Written rules run the portfolio; Laura makes the two calls the case gives her, within the rules (2031 announcement, never above what the rule allows; the 2033 amount and use of kept money); rules change only if her circumstances change, never because markets moved; stock fund never sold to protect a gain or wait for a recovery; no rebalancing between the three parts; bought Treasuries carry no ongoing charge; any cost paid from the stock fund | 35 | Case L101, L110 (VRF); rules R6-R8; CFA 2010 elements (VP via D8) |
| **B10 The WInS sentence** | "Your portfolio and Final Report should reflect the strategy established in your IPS." (L75) | WInS shows her plan on the day both deposits are in, scaled to $300,000; the Treasury funds stand in for her bonds (move like them, do not mature on her dates); in January 2027 almost all of her real first deposit buys the payments | 25 | D10 1.5; ticket v1 s1; T2 16a (INT); rule R10 |
| | | **Content words** | **about 385** | E6 s3.1 (INT) |
| | | **Connecting words allowance** | **about 70** | INT |
| | | **Target total (plan ≤470; hard cap 500)** | **about 455** | ASM page-fit margin, section (h) |

**Paragraph plan (≤7 paragraphs, D10 2.3, ASM):** (1) B1+B2; (2) B3; (3) B4; (4) B5+B6; (5) B7; (6) B8; (7) B9+B10.

### b2. Coverage tick-list (every "should" has a home; tick each against a sentence number in the draft)
- [ ] Goals, horizons, liquidity, certainty, flexibility (L9-10) -> B1, four dates, B6, B2, B8.
- [ ] Central idea (L16); principles (L18) -> B1; B5, B9.
- [ ] Balance of growth, risk, liquidity, reliability, flexibility (L20, L59) -> B5, B6, B2, B8.
- [ ] Allocation changes as needs approach and payments are made (L22-23, L46-47) -> B3, B4, B7, B8.
- [ ] Protect the operating commitment while keeping flexibility for a responsible facility contribution (L25-26, L64-65) -> B7, B8.
- [ ] Risk tolerance (L3), risk and return (L46) -> B5. Construction and diversification (L46) -> B6.
- [ ] Preparing for the commitment; reserve composition over time; facility contribution; flexibility (L48-50) -> B3-B4; B8.
- [ ] Framework, not individual investments or detailed calculations (L51-52) -> number policy; no tickers.
- [ ] What / why / how as needs change (L53-62) -> B1, B9. Official record; portfolio reflects IPS (L73-75) -> B9, B10.
- [ ] Case: define and evaluate certainty, name assumptions (case L97-99) -> B2.
- [ ] Case: assumptions on performance, cash-flow timing, outside funding, inflation on projections and facility costs, flexibility (case L146-148) -> B5; B3-B4; B1-B2; B2+B8; B8.
- [ ] Case: favorable and unfavorable outcomes; range protects the payments (case L118-120) -> B7 (method only).
- [ ] Excluded on purpose (L68-69, VRF): final reserve calculation, projections, the final range, the co-sponsor draft.

---

## (c) Decision rules to fix before Nov 6 (trigger / action / record) (E6 s4; all parameters fixed now, because a parameter chosen after Nov 6 is a redesign: L73-74 and Guide p.5 L156-159, VRF)

Vote each by **Mon Oct 26 AEDT** with first names, date and reason in the decision log (E5 s4, ASM team rule). The IPS states each rule in words only; the numbers in the right column are for the team's understanding and the Final Report.

| Rule | Trigger | Action | Record | Evidence (status) |
|---|---|---|---|---|
| **R1 Buy the payments (rates-fall rule)** | First deposit arrives, 1 Jan 2027 | Buy all ten rungs at that day's prices, all at once (no staging, no yield trigger). If short, buy longest-dated first; the unbought part is always the earliest payment and is the first use of the next money. Leftover waits in Treasury bills. Headline stays conditional: "if prices allow, otherwise when the second deposit arrives" (never "by 1 Jan 2028 at the latest") | Purchase-day ladder cost vs cash; which payments were bought; gap or leftover | Real Nov-15 ladder $294,387 at the 2026-09-25 curve, headroom $5,613 = 19bp (VRF inputs, ASM method). About 1 in 3 rate paths cost more than $300k (MODEL 30-34%; history: ≥19bp falls in 32-36% of 68-day windows since 1962/1990, VP data, DER). Staging: no reliable gain, 27-35% chance of needing the deposit (MODEL). Longest-first: +5% top-up price risk vs +15%, $31.4k vs $47.7k face unbought at -100bp if no deposit (MODEL, D1/AX1b) |
| **R2 The 2028 deposit** | Deposit arrives (1 Jan 2028 per case; each instalment if late) | In order: (1) complete any unbought payment; (2) buy a zero-coupon Treasury maturing before 1 Jan 2033 repaying the deposit's dollar amount (the building minimum), or all that is left if less; (3) everything else, including the 2027 leftover, into one broad world stock fund. Smaller or late: same order, minimum smaller or later. No minimum and no stock fund until all ten payments are bought. **Joint tail** (team's own stress case): rates fell before Jan 2027 and the deposit is smaller than the unbought part -> all of it to the payments, no minimum, no stock fund, unfunded part of the first payment stated | Deposit amount and date; top-up cost; minimum's face and price; stock fund's starting value | Case "will contribute" (case L43, VRF). Growth money $158k; minimum costs $118k at 5y 4.98% (ASM that it holds); stock fund $40k = 8.7% of all money (MODEL). -50bp first: fund about $20-23k; -100bp: about $1-7k; -150bp: no fund, minimum about $127-137k (E6_final_checks.py [8], MODEL; corrects E4 [7]'s $31k/$15k/$147k). Joint tail with no deposit: $11,957 (-50bp) or $31,413 (-100bp) of the 2033 payment unfunded (MODEL, D1/D3) |
| **R3 Operating reserve** | 1 Jan 2033, before the first payment or any facility contribution | Ladder named the operating reserve; pays the first $50,000 at once. Held to maturity; each rung matures about 47 days before its payment and waits in bills; nothing sold early; no rebalancing between reserve, minimum and stock fund; the reserve empties itself by 1 Jan 2042 | Reserve market value, cost and face on 1 Jan 2033 | Case L94-97 (VRF). About $395k market value on today's forwards, cost about $292-294k, face $500k (VRF inputs, ASM) |
| **R4 2031 co-sponsor range: METHOD only (no figures in the IPS)** | 1 Jan 2031, when she begins approaching co-sponsors (case L109) | **Condition:** all ten payments and the minimum owned, otherwise no range, only "aspiration". Nothing traded. **Bottom** = the minimum owned. **Top** = minimum + half the stock fund's market value on 1 Jan 2031, set once, not reset. **Confidence both sides:** below the bottom only on a U.S. Treasury default (and only if no fee is ever charged to it, R8); the top is reached if the stock fund is no lower on 1 Jan 2033 than on 1 Jan 2031 (history and model named in the Final Report). **Words:** owned / expected if stocks hold their value / kept; never "promised" or "pledged" for the stretch. U.S. dollars binding; any New Taiwan dollar figure dated and illustrative | Stock fund value on 1 Jan 2031; the stated range | Case L110-120 (VRF). Illustration only, NOT for the IPS: median bottom $150k, top $175k; top reached in 73% of model paths (67% on a Vanguard-type input) (MODEL); U.S. stocks' two-year total return ≥0 in 84% of 97 overlapping periods 1928-2025 (VP data, DER, E4 [5]) |
| **R5 2033 facility contribution + flexibility** | 1 Jan 2033, after R3 | (1) Gift = minimum + half the stock fund's value, never above the announced top. (2) Kept money = the rest (other half plus any growth above the top), moved the same day to U.S. dollar Treasury bills, hers "as the project develops"; she may choose to add to the gift (her decision, not counted by co-sponsors). (3) No New Taiwan dollar conversion and no currency hedge before the facility decision (a forward is a derivative; banned in WInS and, on the safe reading of "Investments permitted (for BOTH contributions)", in the plan, R-AN15) | Gift, kept money, date of the facility decision | Case L101-107 (VRF; no contingency fund required, L106-107). Gift p5/p50/p95 $165k/$174k/$188k; kept $16k/$32k/$66k (MODEL). "Half" sized against Taiwan building-cost drift 3.54%/yr since 2021 (F-508, VP inputs; ASM sanity check, not a contingency fund) |
| **R6 Stock fund conduct** | Every day 2028-2032 | One broad world stock fund; never rebalanced against the Treasuries; never sold before 1 Jan 2033, to protect a gain or to "wait for a recovery". A fall shrinks only the stretch above the minimum | Yearly check that holdings match R2-R6 | Case L69-74 (VRF). Bottom-decile 2031-32: gift $169k at the median, at or above the announced bottom in 100% of paths (MODEL, E6 [3]) |
| **R7 Governance + reviews** | The four case dates, plus a yearly check | Who decides: the students' written rules; the advisor is administrator only, never "our portfolio manager approves" (R-W19, VP). Laura makes the two calls the case gives her, within the rules (case L101, L110). A rule changes only if Laura's circumstances change (e.g. a different deposit amount or date), never a market move; worded so it cannot read as permission to revise after Nov 6 | Dated decision log: what fired, when, the numbers | L73-74 (VRF); Guide p.5 L156-159 (VRF); CFA 2010 elements 2a-2b (VP via D8/D10) |
| **Rebalancing (inside R3/R6)** | n/a | **None between the three parts.** Composition changes only as bonds mature. This is written down as a deliberate no-rebalance policy | Yearly check | CFA 2010 element 4c (VP via D8): a no-rebalance policy is documented; E6 conflict 35 |
| **R8 Costs** | Any fee or trading cost | Ladder and minimum held to maturity with no ongoing charge; every cost paid from the stock fund, never from the payments or the minimum; the Final Report states the fee assumption, base and rate | The fee assumption | Case L43 "with an asset management firm" (VRF); case silent on fees, so a team assumption (ASM). 1% on the stock fund only costs about $3k of the median total; the same rate on all assets paid from the fund about $31k (MODEL, E6 [6]) |
| **R9 Certainty definition + assumptions** | Fixed in the IPS | B2's five parts; assumptions: returns a range across two published forecasters (graded); flows at the start of each year (case L59); no outside money for the payments (case L91-92); payments fixed in dollars (case L90); Taiwan building costs expected to rise (case L146-147); U.S. dollars binding; flexibility kept by R5 | The IPS itself | Case L97-99, L146-148 (VRF) |
| **R10 WInS conduct to Nov 6** | Each trading day | Book (ii)R (E6 s5). The operations hedge is never sold after a rate rise or trimmed after a fall; re-mixed IEF-against-TLH only if its rate sensitivity drifts more than a quarter-year. Minimum and stock fund held. No day trades; **no tidy-up trades after the words freeze (Tue Nov 3)** | Every trade and every "decided not to trade" moment | L75 (VRF); User Guide "Day Trading: This is not permitted" (VP via A4). All securities PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK; alternates in `securities_and_allocation.md` s1-s2 |

---

## (d) Risk tolerance, goal by goal (E6 B5, R4-R6; E3; content for B5, not wording)

**Risk tolerance** here = how much loss each pot of money can bear, given what it is for. The case gives the frame: "willing to take thoughtful risks" but wants "an appropriate balance between pursuing growth and protecting the capital required for her goals" (case L69-74, VRF).

| Goal (case line, VRF) | Tolerance (INT) | Why (evidence) | What the IPS must show |
|---|---|---|---|
| Ten $50k operating payments, 2033-2042, "high degree of certainty", no outside money (case L88-92) | **None** for market risk | Fixed nominal amounts others rely on; payments cost about 98% of the first deposit at September 2026 prices (DER, E3 [1]), so there is nothing spare to risk in 2027 | Caution here is **forced by arithmetic**, not chosen timidity |
| Building minimum (her announced bottom) | **None** for market risk | Partners will rely on it; overpromising "could damage her credibility" (case L114-116) | Chosen caution, with the reason named (reliance) |
| Facility stretch and kept money | **Full** stock-market risk | Nobody relies on it; living costs are outside the portfolio and there are no withdrawals before 2033 (case L61-65); a five-year horizon (the stock fund is bought in January 2028 and held to January 2033) | What stocks are **for** (a larger gift, more flexibility) and **the most markets can take** (the stock fund, roughly what her deposits would have earned safely; never the payments or the minimum) |
| Her income (outside the portfolio) | Already exposed to publishing and speaking (case L43-45) | Adding themed or single-country bets would stack risk | A portfolio fact, not a diagnosis of her: no themed, AI or Taiwan tilts (D8 M081; brief s4 tokenism rule) |

- **The honest cost (E6 s0, MODEL):** about 9% of her money is in stocks 2028-2032; the p95 is $16k lower than the 2031-lock alternative; in exchange the p5 total is better ($182k vs $168k). The IPS names the trade-off in principle only; no percentiles (number policy).
- **Her regret line** (B1b-Q11, section f) is why the plan must answer "why so little stock" by goal, not by temperament; it is **not** quoted in the IPS (brief s16).
- **Return assumptions:** a range across two published forecasters (e.g. JPM 2026 LTCMA AC World 7.00% compound, VRF `JPM_LTCMA_2026_US_matrix_USD.pdf` p.2; the Vanguard-type input, 5.08% compound, an ASM hybrid built on VP inputs, E6 [4]), graded "we assume", never a target.
- **Banned in B5 (E6 s6.2; E3):** CFA "ability/willingness" labels, "loss tolerance", "break-even", "house money", "composure", "Laura likes risk", the statistics degree.

---

## (e) Stating certainty and its named gaps honestly, without jargon (B2; brief s16 binding)

**What a strong B2 must contain (elements, not wording):**
1. **The definition:** "high certainty" means each payment is **bought**, not forecast: a U.S. Treasury maturing shortly before each payment date, held to maturity (case L97, VRF; E6 R9).
2. **How it was evaluated:** by **price**, not by a model: on the purchase date the money covers the market price of all ten. No percentage (INT; MODEL percentages are not "certainty").
3. **The residual risk:** certain in U.S. dollars, barring a U.S. Treasury default (INT).
4. **Gap (i), one clause:** if rates fall before January 2027 the ten can cost more than the first deposit (about 1 in 3 modelled paths, MODEL; the ladder cost more than $300k on 173-176 of 185 trading days in 2026, VRF/DER), and the earliest payment then waits for the second deposit (career income, case L43-45, VRF). The IPS mentions the deposit only as the completer (E6 conflict 22). Background for the team only, never in the IPS or the notes: her own word for self-employed income (B8b-Q18, section f).
5. **Gap (ii), one clause:** each payment is a fixed U.S. dollar amount (case L90, VRF), so rising prices, Taiwan's costs and the exchange rate mean it buys less over time. Named, not solved. Illustration for the team only: $50k is worth $42,063 (2033) and $33,681 (2042) in 2026 dollars at 2.5% inflation (ASM, F-114).
6. **The joint tail, once (B4):** what could still stop a payment = a rate fall before January combined with a missing deposit, or a U.S. default (D12 M234 test, E6 D10).

**Plain-word rules:** say "bought", "owned", "held to its date", "barring a U.S. government default"; avoid "guaranteed", "risk-free", "100%", "matched", "immunised", "funded ratio". Use "certainty" only for the payments, "confident" for the range, "credibility" for her standing (E6 s6.1 rank 6, INT). Keep all what-could-go-wrong content to about 15% of the words (ASM ceiling).

---

## (f) The client understanding the IPS must show

### f1. The client picture (case facts, VRF)
- $300,000 at the start of 2027 "with an asset management firm"; +$150,000 at the start of 2028 from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" (case L43-45).
- Living costs outside the portfolio; no other additions or withdrawals before 2033 (case L61-65). Flows at the start of each year (case L59).
- "Thoughtful risks" with "an appropriate balance" between growth and "protecting the capital required for her goals" (case L68-74).
- A collaborative, community-oriented creative residency in Taiwan from 2033 (case L76-80).
- Ten fixed $50k operating payments 2033-2042, not inflation-adjusted, portfolio-funded "with a high degree of certainty", no outside money (case L88-93).
- Operating reserve set aside at the start of 2033, composition "if at all" changing (case L94-97); facility contribution decided after that, with flexibility "as the project develops"; no contingency fund required (case L101-107).
- In 2031 she needs a credible **range** with stated confidence that protects the payments; overpromising damages credibility (case L109-120).

### f2. What the case designers test (INT reading of the case's own "must" list, case L134-148, VRF)
1. Payments supported "with a high degree of certainty" (L136) -> **does the team define and evaluate certainty?** (B2)
2. "a responsible facility contribution" (L138) -> **a rule, not a wish** (R5).
3. "how investment uncertainty could affect both" (L140-141) -> **both goals under good and bad markets** (B5, B7).
4. Communicates to co-sponsors "clearly and credibly" (L143) -> **no overpromising; confidence both ways** (R4).
5. "Preserves appropriate financial flexibility" (L145) -> **kept money exists even when stocks fall** (why s = ½, not 1; E6 s6.2).
6. Assumptions on performance, timing, outside funding, inflation on projections **and facility costs**, flexibility (L146-148) -> R9.
7. Hidden tests (INT): reconcile "bought 2027" with "set aside 2033" (E5 PM-24); the second deposit is career income (does the plan protect against a smaller one?); fixed U.S. dollars vs Taiwan costs; WInS gains not added to projections (case L132-133).

### f3. Laura's values from her verified words (BACKGROUND FOR THE TEAM ONLY; never quoted in the IPS, brief s16)
All rows are D13a **VERIFIED-PRIMARY** (verbatim on the primary page, accessed 2026-09-27; `phase_D/D13a_laura_quotes_verified.md`). Readings are INT (D13c). None is a statement about investing: there is **no** verified Laura investment philosophy.

| Id | Value it suggests (INT) | Source (URL), year | Context caveat |
|---|---|---|---|
| D13a-N01 | Accountable to early backers -> "announce only what is bought" | Daily Pennsylvanian, https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a , 2016 | **Student-era**; about entrepreneurship, not money management |
| B1b-Q11 | Regret-driven leaps -> the plan must answer "why so little stock" | Overachiever, https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid , 2021 | About leaving a job for her art career |
| B8b-Q18 (= B8a-Q07) | She called self-employment income "unstable" -> why the 2028 deposit is not assumed and payments are bought first | Overachiever (same URL), 2021 | Same career answer; use once, never speculate about her finances |
| B8b-Q38 | Access first ("diverse voices ... in the room") -> operations first | Local News Matters, https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/ , 2026 | About festival grants, not the residency |
| B8b-Q37 | Growth after community support -> shape of the 2031 message | Local News Matters (same URL), 2026 | About the comics festival |
| B8b-Q10 | Validate, then build | Sign.al founder's note, https://signaltemp.github.io/ , c. 2022 (date ASM) | About a student-advice product |
| B8b-Q21 | Meaning over metrics -> report what numbers secure | Overachiever (same URL), 2021 | About social-media likes |
| B8b-Q13 | Authenticity over clever concepts -> cut what is only for show | The Nerd Daily, https://thenerddaily.com/laura-gao-kirbys-lessons-for-falling-in-love-interview/ , 2025 | About novel drafts; never "No more gimmicks." alone (B8b-Q14) |
| B8b-Q12 | Scraps what is wrong -> honest about the dropped growth-first plan | The Nerd Daily (same URL), 2025 | About drafts of a novel |
| B8b-Q31 | Deadlines by rule | Geeks OUT, https://www.geeksout.org/2022/05/11/interview-with-creator-laura-gao/ , 2022 | About posting art |
| B8b-Q35 | Purpose statement first -> the IPS opens with purpose | Pulse Spikes, https://pulsespikes.org/story/laura-gao , 2021 | About art pieces |
| B8a-Q19 | Data inside a story | Pulse Spikes (same URL), 2021 | About a comic |
| B9b-Q09 | Labels unfinished results and grades them -> grade numbers, name gaps | https://lauragao.com/rewriting-herstory , undated | Her website project |
| B8a-Q13 | Plans for the downside | Overachiever (same URL), 2021 | About reactions to her comic |
| B2b-Q08 | Taught financial literacy to high-schoolers -> plain, honest about costs | Poets&Quants, https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/ , 2018 | **Student-era** resume line |
| B3a-Q04, B8b-Q39 | Access on need ("Pro-bono visits") | Speaking guide, https://lauragao.com/s/Publicity-and-Speaking-Guide-Laura-Gao-e5n7.pdf , 2024 | About her speaking fees |

**Never:** "risk-adverse" (B8a-Q03, VP) as investment risk (it is about choosing a business major); the case pull quote as her words (VRF as the case's text only); a "floor-first leap" trait; any EXCLUDE-PRIVACY or PARAPHRASE-UNVERIFIED line (D13a; brief s16).

---

## (g) What NOT to put in the IPS (E6 s3, s6.2; D13 rules; L68-69, L123)
- Final reserve calculation, projections, the final 2031 dollar range, the co-sponsor draft (L68-69, VRF: "not expected").
- Tables, bullet lists, charts, images, links, URLs, footnotes, citations, quotation marks around anyone's words (L123, VRF).
- Laura quotes, the pull quote, her career or regret story as a reason; identity, heritage or Taiwan as a reason; book-title puns; private details (brief s4, s16).
- Tickers, fund names, CUSIPs; percentiles, probabilities, stage-by-stage stock shares, a fee number, a New Taiwan dollar figure, a return target.
- House names or frameworks: barbell, LDI, "Rule 1-4 + G", CFA labels, "letter to Future You", "two clocks".
- "Our portfolio manager approves" or anything implying the advisor decides (R-W19, VP).
- WInS profit, loss or rank; WInS gains added to projections (case L132-133, VRF).
- "Only the facility shrinks" (false in the joint tail); "fully funded by 1 Jan 2028 at the latest"; "fits inside $300,000"; "guaranteed"/"risk-free"/"safe"; "promised" for the stretch; the statistics degree; "innovative".
- The rejected alternatives and the growth-first history (Final Report and TN reflection C territory, E6 s5.5, s10).

---

## (h) Format and compliance checklist ("Submissions that do not meet the requirements below will not be considered for semifinal selection", L82-83, VRF)

**Title page (page 1, "1 page maximum", L84-85, VRF)**
- [ ] "Official team name" (L88), "the same as what you submitted with your official team roster" (L90). Copy from the roster confirmation screenshot, character for character (PM-18, ASM process). Team name UNVERIFIED until the roster is submitted (due Oct 9 5 p.m. ET; team target Wed Oct 7 AEDT).
- [ ] "Finalized team member names", same as the roster (L92-94), "Format: First Name, Last Initial" (L96). Wharton's sample separates names with " | " (L130, VRF). (Names are not stored in this repo: privacy rule.)
- [ ] "WInS username" = "the team's username for logging into the WInS platform" (L98-100), **not** the team name (SMApply FAQ, VP via A4); copy from the WInS login screen.

**Pages 2-3 ("2-page maximum", L103-104, VRF)**
- [ ] Headings as in the sample: "Investment Strategy Elevator Pitch" and "Investment Policy Statement" (L135, L139, VRF).
- [ ] Pitch ≤50 (plan ≤48) and IPS ≤500 (plan ≤470) words (L107-109, VRF), by two counters, higher wins.
- [ ] "Font: Times New Roman" (L112), "Size: 12-point" (L114) everywhere, headings included.
- [ ] "Spacing: Double-spaced" (L116): Word "Double"; paragraph spacing 0 before/after; no blank lines; ≤7 paragraphs.
- [ ] "Margins: 1 inch on all sides" (L118); U.S. Letter (E6 D9; paper size is team discretion, L101, VRF).
- [ ] No "Graphics, charts, images, attachments, external links, footnotes, and formal citations" (L123).

**Page-fit evidence (why ≤470 words, not 500)**
- Word "Double" for TNR 12 = 27.6 pt line (ASM: font line height 1.15 em); Letter with 1-inch margins holds 23 lines a page, 46 on pages 2-3 (DER, `D9_communication.md` L34-35).
- A full 50 + 500 words needs 44-46 lines -> **0-2 spare lines on Letter**; about 525 words max (DER, D9 table L387). A4 leaves 2-4 spare; Wharton's own sample is Letter at a 24 pt pitch (VRF measured with pypdf, D9 L380) and leaves 8-10.
- Audit re-run: Letter, 7 paragraphs, 0 pt spacing, 27.6 pt: median 100.0% of the two pages, so 500 words "does not reliably fit"; Word's default 8 pt after-paragraph spacing adds overflow (DER, D10 s2.3 and audit C3).
- Long words cut capacity (13.4 words/line average; 9.0 for 7+ letter words, DER), so run `.venv/bin/python research/insight_v1/scripts/D9_ips_page_fit.py --draft <file>` on the real text (first paragraph = pitch) and then trust only the exported PDF.
- "Exactly 24 pt" line spacing (Wharton's sample) is a documented last resort only, never the plan (E6 D9).

**PDF check (two students, Wed Nov 4 AEDT; E6 s3.3, ASM team rule)**
- [ ] Export to PDF and open the exported file itself: **exactly 3 pages**; text ends on page 3 with ≥2 spare lines.
- [ ] Font list shows Times New Roman only; "Maximum file size: 5 MB" (L122).
- [ ] Search the PDF for "http", "www", "[", "(" citations and quotation marks.
- [ ] "Submit as a PDF through SurveyMonkey Apply" (L120). Open the IPS form in SMApply early and record its fields and who can submit (PM-23; by Mon Oct 12 AEDT, ASM).

**Deadline:** Fri Nov 6, 5:00 p.m. ET, no extensions (SMApply L10, VRF) = **Sat Nov 7, 09:00 AEDT** Sydney (U.S. clocks change Nov 1; Brisbane 08:00, Perth 06:00) (DER, E5 [1]). Trading ends and the portfolio locks at the same deadline (CLAUDE.md, VRF via SMApply). Team targets (ASM): words frozen Tue Nov 3; last rule-driven trade by Fri Oct 30 ET; PDF check Wed Nov 4; submit Thu Nov 5.

---

## (i) Consistency checks between the Trading Notes and the IPS
Why: "maintains consistency with the team's IPS" (SMApply criterion L49, VRF); the TN analysis "should be consistent with the strategic approach your team is developing and will later articulate in its IPS" (TN guide L30-31, VRF via E5); notes cannot be edited, only added to (VP via A4). Run on Thu Oct 22 and Tue Nov 3 AEDT (E5 PM-06, ASM).

- [ ] **Central idea:** the notes and the IPS both express the split of jobs; no time-worded ban anywhere.
- [ ] **Scaling:** every operations and stock note carries "after both deposits" / "after her 2028 deposit" inside the note; B10 states the scaling and the stand-in funds (E6 s5.1 conditions).
- [ ] **Labels:** the team's own labels for the three parts are identical in notes, log and IPS (E6 D5); one label per holding.
- [ ] **Rule names:** each note's rule matches the IPS rule (a decision-log column: note -> IPS rule -> label, D9 M212).
- [ ] **Vocabulary:** "certainty" / "confident" / "credibility" used the same way; "moves like / stands in for" for WInS funds; never "matched" or "operating reserve" for a WInS fund; never "promised" for the stretch.
- [ ] **Numbers:** any number in a reflection (e.g. about 9% stocks after both deposits; about 98% of the first deposit) matches the IPS's forced-caution fact and date.
- [ ] **Refined story:** if note B shows "refined", the log shows, dated before the order, the change from a 2031 floor to the 2028 minimum; the IPS describes only the current rule.
- [ ] **Frozen book reflects IPS (L75):** on Nov 4 compare WInS holdings with B10; no tidy-up trades after Tue Nov 3 (R10).
- [ ] **Two-reader check:** outside readers who read the notes and then the IPS describe one strategy, and say Laura's real January 2027 money holds bonds, not stocks (E3-10).

---

## (j) Top IPS risks and preventions (E5, ranked; ratings INT/ASM)

| Rank | Risk (E5 id) | Prevention | Owner (role) / by |
|---|---|---|---|
| 1 | Not the students' own; reads AI-made (PM-01, severe) | Own-words notes before every vote; blank-page drafting from this element list; explain-back of the four dates without notes | Team leader; IPS draft Mon Oct 26 AEDT |
| 2 | Format breach (PM-02, **fatal**) | Section (h); ≤470/≤48 words by two counters; PDF check by two students | Format checker; every draft from Oct 26, final Wed Nov 4 |
| 3 | Over-complex, jargon-dense (PM-03) | 10 blocks, ≤12 ideas; four-date spine; 6-reader paraphrase test | IPS lead writer; idea list Sat Oct 24; tests Oct 26-30, Nov 2-3 |
| 4 | Notes contradict the IPS (PM-06) | Section (i) | Log keeper + IPS lead; Oct 22, Nov 3 |
| 5 | Reads timid, or as a study of her (PM-07) | Purpose first; forced vs chosen caution; what stocks are for; one stress clause for the $150k | Client lead; Oct 24, Oct 30 |
| 6 | Generic thesis (PM-09) | Swap test on each paragraph; lead with the three Laura-specific decisions | Client lead; Oct 26-Nov 3 |
| 7 | Required element missing (PM-11) | Tick-list b2 with the sentence number that covers each item | IPS lead |
| 8 | Rules left open, so the Final Report looks like a redesign (PM-12) | Section (c) voted and logged | Team leader; Mon Oct 26 |
| 9 | Overclaiming words (PM-10) | Banned lists (a3, e, g); `D9_draft_checker.py --kind ips` | Second reader; every draft |
| 10 | Title-page mismatch (PM-18, fatal) or missed deadline (PM-13, fatal) | Copy from roster and WInS login; submit Thu Nov 5 AEDT; two people with SMApply access | Admin liaison; Nov 4-5 |
| 11 | Frozen book does not reflect the IPS (PM-22) | R10; Nov 4 holdings check | Trader + IPS lead |
| 12 | AI use unlogged (PM-08) | Dated AI-use log, reconciled with repo history, credited later in Works Cited | Log keeper; weekly |

---

## (k) Open team decisions (default from E6 s7, INT; the team decides)

| # | Decision | Default | Test for choosing | By |
|---|---|---|---|---|
| D1 | Adopt lock-early | Adopt | Every student writes, with no AI file open, why the payments are bought first; vote logged with reasons | Gate, Thu Oct 1 |
| D2 | REC (minimum bought 2028) or ALT (2031 lock) | **REC** | (1) Values: which matters more for Laura, a minimum no market can lower from 2028 with better bad cases, or more stock 2028-30 with a worse bad case; (2) explain-back of the four dates in two minutes; if only one design passes for all six, choose it | Gate, before any building or stock order |
| D3 | WInS book | (ii)R | Two-reader check passes, and the scaling fits in about 25 IPS words; two failures -> (iii) | Gate |
| D5 | The team's labels for the three parts | Team's own words | Survive the explain-back; identical in notes, log and IPS | Before the first note |
| D6 | Share of the stock fund added to the gift (s) | **One half** | Median kept money ≈ three years of Taiwan building-cost drift on the gift ($32k vs about 11% of $174k, ASM check); plainest split to explain | Section-4 vote, Mon Oct 26 |
| D7 | Cost clause in the IPS | **Keep (one clause)** | If the PDF has <2 spare lines, compress inside governance; cut only if the fee base will never touch the promises | Oct 26; Nov 4 |
| D8 | Statistics degree | **Zero uses** | Use once only if it changes a decision | Oct 24 |
| D9 | Paper and line spacing | **U.S. Letter, Word "Double"** | Exported PDF ends on page 3 with ≥2 spare lines | Nov 4 |
| D10 | Joint tail in the IPS | **One clause** | A reader asked "what could still stop a payment?" answers: a rate fall before January with a missing deposit, or a U.S. default | Oct 26 |
| D12 | Roles | Assign now | Every student owns at least one IPS block (and one note or reflection) | Tue Sep 29 |

(D4 WInS instrument and D11 repository visibility are E6 decisions that do not change IPS content; see E6 s7.)

---

## What this teaches
- A policy statement is judged on whether a stranger can see the rules that will run the money, so the pitch leads with purpose and the IPS is organised around four dated decisions rather than around products.
- Honesty about certainty is a strength: saying how certainty was defined, how it was checked, and the two gaps that remain earns more trust than "guaranteed".
- A rule has to be fixed before the outcome is known. Once the strategy freezes, any parameter chosen afterwards looks like hindsight.
- The layout counts as much as the words: two pages at 27.6 pt leaves 0-2 spare lines, so a correct IPS that runs onto a fourth PDF page is never read.
