# E4 Rival strategist: the strongest competing strategy for this case, and where the E1 plan loses to it

Agent E4 (red team, "the best strategist of a rival team that wants the same Top 50 place"), insight_v1 run, Phase E.
Written 2026-09-28. This is AI-generated research for Team Caplet: a competing design, numbers, specifications and
checklists. **None of it is text to submit.** No pitch, IPS sentence, WInS note or reflection is drafted here; every
phrase that names an idea is a content label, not wording to copy. The six students decide every change and write
every word. Any AI use goes in the Final Report's Works Cited (Wharton AI policy, R-W46). Laura appears only through
the case and her public professional record; nothing here suggests contacting her (R-W16).

**Scope (brief section 17).** Only the Trading Notes (TN, Oct 23) and the IPS (Nov 6), plus WInS trading as the source
of the notes. The rival strategy fixes the **decision rules** a Final Report would later apply (reserve, 2031 range
method, facility and flexibility, if-then rules) but gives no Final Report content, no dollar range presented as a
deliverable and no fundraising text. Final Report items are one line each in section 9.
**Relayed messages:** none arrived during this task.

**Status labels** (brief section 3): **VP** = VERIFIED-PRIMARY; **VRF** = VERIFIED-REPO-FILE; **SNIP** =
SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION; **MODEL** = an ASSUMPTION-based model output, not a forecast; **INT** = E4's
interpretation or judgement (never a fact about Laura). Ids: R- = case register, F- = fact register, SH-/BS- =
stakeholder map, M- = Phase C questions, P- = E1 proposals, F1-F10 = E2 fixes (all under `research/insight_v1/`).
Every security named is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (brief sections 4 and 14).

**New script:** `.venv/bin/python research/insight_v1/scripts/E4_rival_numbers.py` (about 5 seconds, no network; the
docstring lists every input with its label). It re-uses D6's engine and random stream (seed 20260927, 200,000 paths),
**reproduces E1's P7 row exactly** (bottom $167k, top $192k, gift $151k/$188k/$238k, kept $16k/$21k/$29k) and then runs
the rival on the same paths and on every historical 6-year window 1928-2025. Sections [1]-[7] of its output are cited
below as E4 [n]. Cross-check: E1's average whole-portfolio stock share over 2027-2032 comes out at 9.7%, the same figure
E3 reports from its own script (E3 [2]).

**Evidence read in full** (audit corrections override the text above them): the brief; CLAUDE.md; the case, IPS guide,
TN guide, Competition Guide, Infographic and SMApply page; `phase_E/E1_change_proposals.md` (the plan being attacked),
`phase_E/E2_judge.md`; D1-D12, `D3_model_v2_results.md`, `D3_quant.md`, D13a, D13c, all five audit files and every
"Audit corrections" appendix (D1 AX1b, D2/D4/D10 AX2, D3 AX1, D5/D6/D12 AY1, D7/D8/D9 AY2); `phase_D/trading_now_brief.md`
and `wins_now/securities_and_allocation_v1.md` (both as revised after T2), `wins_now/T2_red_team.md`, S1-S4;
`phase_A/` case_register (R-C, R-W, R-AN, X), fact_register, stakeholder_map, wins_week1_guardrails;
`phase_C/survivors.json` and parked M007, M008, M015, M021, M033, M035, M040, M149; the v4 prompt parts 2, 3, 5; the
council chair memo and round-2 ruling (history only). `phase_E/E3_laura.md` appeared during this task; its summary was
read and one figure is cross-checked above.

**Terms used (defined once):**
- **Ladder:** ten zero-coupon U.S. Treasury bonds (STRIPS), one maturing shortly before each $50,000 payment
  (2033-2042). Identical in E1 and in the rival.
- **Growth money:** everything the ladder does not need (about $158k on 1 January 2028).
- **Bottom (of the co-sponsor range):** the part of the facility gift that is already bought as a Treasury maturing
  before 1 January 2033, so its dollar value is known in advance. E1 buys it in January 2031; the rival in January 2028.
- **Barbell:** a split into two very different pieces with nothing in between: here a dated Treasury for the bottom
  and 100% world stocks for the rest.
- **Stock fund (rival):** the part of the growth money held in one broad world-stock fund from 2028 to 2033.
- **Cap:** a rule that the 2033 gift never exceeds the top announced in 2031; anything above stays with Laura.
- **Percent-years of stock:** the whole-portfolio stock share added up over 2028-2032 (a rough measure of how much
  stock risk a plan carries over time; divide by 6 for the 2027-2032 average).
- **p5 / p50 / p95:** in a simulation, the value 5% / 50% / 95% of paths fall below (p50 = median).

---

## 0. Summary

**The rival in one paragraph (content, not wording).** Buy each of Laura's promises on the day the money for it
arrives, and put in stocks only the money nobody else relies on. January 2027: her first deposit buys the ten
operating years (the same ladder and the same rates-fall rule as E1). January 2028: her second deposit, which the case
says comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" (case L44-45,
VRF), first finishes any unbought payment, then buys the **building's minimum**: a Treasury maturing before 2033 that
repays exactly the dollar amount of that deposit. What is left (about $40k, about 9% of her money) goes into one world
stock fund and is left alone until 2033. In 2031 nothing is traded: she tells co-sponsors a range whose bottom she has
owned since 2028 and whose top is the bottom plus half of what the stock fund is worth that day; the top is reached if
stocks are not lower two years later, which happened for U.S. stocks in 84% of two-year periods since 1928 (E4 [5], VP
data, derived; 73% in the JPM world-stock model).
In 2033 the ladder becomes the operating reserve, the building gets the minimum plus half the stock fund (never more
than the announced top), and everything else is Laura's flexibility. (Content label for this file, not wording: "every dollar has a date and a job".) No forecast is
needed for any number she will say in public except the one chance attached to the top, and that chance can be checked
against a century of data.

**Scoreboard, same model paths (E4 [2]-[5]; MODEL; JPM AC World 7.00%, growth-money bonds 5.0%, no fee, as E1 P7):**

| Measure | E1 (50/50 growth money, 80/10/10) | Rival default (bottom = the 2028 deposit) | Rival alternate (a = 2/3, same stock exposure as E1) |
|---|---|---|---|
| Facility + flexibility money in 2033, p5 / p50 / p95 | $168k / $210k / $266k | **$182k** / $207k / $250k | $176k / $208k / $265k |
| Bottom announced in 2031, p5 / p50 / p95 | $134k / $167k / $211k (depends on 2028-30 markets) | **$150k fixed, owned from Jan 2028** | $134k fixed, owned from Jan 2028 |
| Bottom after a bad 2028-30 (worst 10% of 3-year stock returns): median (p5) | $134k ($119k) | **$150k ($150k)** | $134k ($134k) |
| Median top / width | $192k / 1.15x | $175k / 1.17x | $167k / 1.24x |
| Gift p5 / p50 / p95 | $151k / **$188k** / **$238k** | **$165k** / $174k / $188k | $154k / $166k / $183k |
| Kept for the project p5 / p50 / p95 | $16k / $21k / $29k | $16k / **$32k** / **$66k** | $21k / $42k / $86k |
| What the top needs | a model percentile (p90); "about 1 in 10 above" | today's market value; reached in 73% (model) / 84% (history) of 2-year periods | same |
| Whole-portfolio stock share 2028 / 2031 (median) | **17.0%** / 3.5% | 8.7% / **9.1%** | 11.4% / 11.9% |
| Stock percent-years 2028-32 (average 2027-32) | **58 (9.7%)** | 45 (7.5%) | 59 (9.8%) |
| History, every 6-year window 1928-2025 rescaled to JPM: total worst / p10 / median | $120k / $174k / $214k | **$169k / $185k / $214k** | $159k / $180k / $218k |
| Rules the IPS must fix | growth mix 50/60 + band + yearly reset; a, s, q; cap or not; VGSH or dated bond (open); 2028 or 2031 (open) | the minimum rule (set by the case's own number); s = one half; cap | same, with a = 2/3 |

**Where E1 loses to the rival (details and evidence in section 5):**
1. E1's co-sponsor bottom is unknown until 2031 and falls with 2028-30 markets (to about $134k in a bad decile, $93k in
   a 1929-type window); the rival's is fixed and owned three years before she speaks.
2. E1's top rests on a model percentile that D3/AX1 found lands 81-97% "within" across models and history; the rival's
   top is a market value on the day, and its odds come from history, not a model.
3. E1 rejected the 2028 purchase on a comparison that AX1 has withdrawn (E2 E-1); at equal stock exposure the rival is
   better in the bad case and in every historical tail.
4. E1 holds the bond half of the growth money in rolling short Treasuries although its use-dates are known (E2 R1;
   AX1 C18); the rival dates it to December 2032.
5. E1's central idea is a prohibition that its own recommended WInS book breaks on day one (E2 C1); the rival's is a
   positive, dated rule that is true in both books.
6. E1's third Trading Note (VGSH) is its weakest (E2) and may not mention the co-sponsor promise; the rival's third
   note is the most Laura-specific holding in either plan and can name its job honestly.
7. E1 needs about 55 ideas in 550 words (E2 section 3.2); the rival's IPS needs about 10.
8. E1 cannot name anything co-sponsors can count on without a projection; the rival's bottom is set by a number the
   case itself gives (her 2028 deposit).

**What E1 would need to win back (section 6):** decide the open gate question now (ticket v1 gate box (b): "is the
facility floor bought in January 2028 or January 2031?") and, if 2031 is kept, say in the IPS why the bottom may
depend on 2028-30 markets; date the growth money's bond half (IBTM or a Jul-Dec 2032 Treasury, not VGSH); make the top
checkable without a model; give the bottom a case-anchored meaning; lead the pitch with a positive dated idea; cut the
IPS to about a dozen ideas.

**Where the rival loses to E1 (section 7, honest):** a lower median bottom (E1's is higher in 78% of paths) and a
smaller median gift ($174k vs $188k); less stock over 2028-32 (45 vs 58 percent-years) and a lower p95; a cap that stops
strong markets from visibly raising the gift; a 100% stock fund that is still at risk after Laura has spoken; and an
instrument (IBTM or a 2032 note) whose WInS availability is unknown. The rival is not a free improvement; it is a
different bet on **when** risk is taken and **what** is promised.

**North Star link (INT).** A client choosing between two firms that both buy her payments first would see the
difference in 2031: one firm can tell her in 2028 the exact minimum she will be able to put on the table, sized to her
own 2028 earnings; the other tells her it depends on the next three years.

---

## 1. The rival strategy (specification, not wording)

### 1.1 Design principle (one line each)
- **Each promise is bought the day its money arrives** (2027: operations; 2028: the building's minimum).
- **Only money nobody relies on takes stock risk, and it takes it fully** (one world stock fund, no bond dilution, no
  rebalancing, held to 2033).
- **Nothing is traded in 2031**: the range is read off what she owns (a bought minimum and a market value), so no
  forecast is announced.
- Every decision traces to a case line: L43-45 (two deposits, the second from her career), L91-92 (payments from the
  portfolio alone), L101-103 (flexibility), L110-120 (range, credibility, confidence), L94-96 (reserve), L69-74
  (thoughtful risk, balance) (all VRF).

### 1.2 Four dated decisions (the IPS spine; E2 F2 asks for exactly this shape)

| Date | Rule (trigger, action) | Why (case line; Laura link) | Status of the reason |
|---|---|---|---|
| 1 Jan 2027 | The first deposit buys the ten payments on arrival; if it falls short, longest-dated first; any unbought part is the first use of the next money; any leftover waits in T-bills | Same as E1 P3 (L91-92; the ladder cost more than $300k on 176 of 185 days of 2026 and "about 1 in 3" rate paths, AX1b) | VRF case; VP inputs, MODEL odds |
| 1 Jan 2028 | The second deposit (each instalment if late) first completes the ladder; then buys a Treasury maturing before 1 Jan 2033 that repays the deposit's dollar amount (or all that is left, if less); the rest goes into one world stock fund | Her 2028 money is career income (L44-45); the case says "A meaningful personal contribution may signal that the residency is financially viable, demonstrate Laura’s commitment to the project" (L110-112); the stock fund is money nobody relies on | VRF case; INT reading |
| 1 Jan 2031 | Nothing is traded. Range = [the minimum, the minimum + one half of the stock fund's value that day]. Confidence stated two ways: below the bottom only on a U.S. Treasury default; the top reached if the stock fund is not lower two years later (history and model odds named) | "credible range", "how confident", "favorable and unfavorable" (L115-119); "In 2031, however, the value of her portfolio in 2033 remains uncertain" (L112-113) | VRF case; VP data (history), MODEL odds |
| 1 Jan 2033 | The ladder is designated the operating reserve, held to maturity (self-liquidating). Gift = minimum + one half of the stock fund, never above the announced top. Everything else (the other half, plus any gain above the top) is her flexibility, moved to short Treasuries; she decides its use | L94-96 ("if at all"), L101-107 (she decides; flexibility; no contingency fund required) | VRF case |

- **Governance line (element):** the rules change only for a change in her circumstances, never because markets moved;
  the stock fund is never sold before 2033 to "protect" a gain or "wait for a recovery"; no rebalancing between the
  three parts, written down (CFA 2010 element 4c, VP via D8/D10); students decide, Laura makes the two choices the case
  gives her (range she announces; 2033 amount) (R-AN4; D10 M013, VP).
- **The parameters and their reasons:**
  - **Bottom = the 2028 deposit's dollar amount.** Not a free choice: the case supplies the number. It makes the
    minimum knowable in the IPS as a rule output, conditional only on the deposit arriving (the case says she "will",
    R-AN35) and on no extreme rate fall before January 2027 (E4 [7]: at -100bp the top-up of about $26k comes out of
    the stock fund and the minimum stays whole; only at about -150bp, a late-2008-size move, does it dip to about
    $147k; such 98-day falls occurred in about 0.1% of windows since 1990 and 1.4% since 1962, AX1 V4, VP data).
    At a lower January-2028 five-year rate the minimum stays the same and the stock fund shrinks (4.0%: about $35k
    instead of $40k, E4 [4], MODEL/ASM).
  - **s = one half** of the stock fund goes to the building (up to the top); the other half is kept. Reason (INT): by
    2031 the uncertainties that dominate what the gift buys are the exchange rate and Taiwan building costs, not
    markets (D4 finding 1; true for lock shares of about 70% or more, AX2 D4 C2; the rival locks about 74%), so a real
    share is kept by rule for "as the project develops" (L102-103). Kept money is at least E1's at every percentile and
    larger at the median and p95 (E4 [2]).
  - **Cap at the announced top.** Makes the top a ceiling that needs no forecast. The informative confidence number is
    then the chance of reaching the top, never "100% within" (AX1 C2; D5 audit C11).
- **What the rival drops from E1 (and why it can):** the growth-money mix (50/50 vs 60/40), its 45-55 band and yearly
  reset, the percentile q, the uncapped give-back rule, VGSH, and the "bought in 2031 from a sleeve that moved for three
  years" dependency. None of these is needed when the only risky money is one stock fund held to a date.

### 1.3 Certainty, risk and currency (IPS content elements; the same honesty as E1 P2, applied to two promises)
- **Certainty definition (elements):** bought at market prices and held to maturity; evaluated by price, not a model;
  certain in nominal US$ barring a U.S. Treasury default. Applies to the ten payments **and** to the building's
  minimum. The two gaps named once each: (i) the January-2027 price (the next money completes the ladder first);
  (ii) a fixed US$ amount buys less each year in Taiwan (named, not solved) (brief section 16, binding).
- **Risk stated goal by goal (elements; CFA 2020 three-part profile via D6, VP; no framework name in the IPS):**
  operations: no risk needed, none affordable; building minimum: none once bought; stock fund: all of it, 100% stocks,
  sized so that even a total loss leaves every promise intact. This is a **maximum-loss statement**, not a probability:
  the most she can lose to markets is the stock fund, about 9% of her money in 2028 (E4 [6], MODEL arithmetic on VRF
  inputs). E1's equivalent rests on a model threshold ("about 1 in 20 below the money put in"), which E2 R3 says uses a
  weak yardstick.
- **Forced vs chosen caution (element; E3 finding 2):** the low stock share in 2027 is the case's arithmetic (the
  payments cost about 97-98% of the first deposit, F-101, S1); the chosen part is the minimum rule and s.
- **Currency and building costs (elements; AX2 D4 C1):** US$ is binding for every promise; any NT$ figure is dated and
  illustrative (Final Report); no NT$ conversion or hedge before the facility decision (a forward is a derivative,
  banned in WInS and, on the safe reading of R-AN15, in the plan); the assumption that Taiwan building costs are
  expected to rise is named (case L146-147).
- **Diversification and liquidity (elements; E2 F5; R-AN45 "funding purposes", VP):** diversified by funding purpose
  and by date (a 2032 minimum, ten dated rungs 2032-2041, one undated stock fund of about 10,000 companies worldwide);
  the Treasury concentration is deliberate because the bills are in US$ and dated; no withdrawals before 2033 (L63-65);
  each year's payment cash arrives when its bond matures.

### 1.4 Considered and rejected by the rival (one line each)
- **TIPS for the building's minimum:** protects U.S. CPI, not Taiwan building costs or the exchange rate, and makes the
  minimum's dollar amount unknown in 2028 (INT; brief section 8 item 10 for the payments).
- **A second lock in 2031 on top of the 2028 minimum:** a second rule for a narrower range; the design principle says
  no (AX1 C11 logic).
- **Uncapped top at a model percentile (E1/D5):** see section 7, X3; it is E1's better answer to "favorable outcomes".
- **Taiwan, AI or thematic tilts; EWT:** tokenism and concentration (D8 M081; S2; D13c R3).
- **Justifying the barbell by her career:** banned ("floor-first leap" is not her trait; career risk does not transfer,
  Weber et al. via D6; brief section 16). The rival's reasons are case lines only.

---

## 2. Numbers behind the scoreboard (all MODEL unless labelled; E4 script)

### 2.1 Same model, every design (E4 [2])
- Inputs: JPM 2026 LTCMA AC World 7.00% compound / 8.28% arithmetic (VRF); growth-money bonds 5.0% (ASM,
  market-consistent, as E1/D6 case B); rival bottom locked at today's 5-year par 4.98% (VRF curve; ASM that it holds in
  January 2028, the D3 barbell convention); E1 bottom at today's 2-year par 4.81% (ASM, as E1); no fees; i.i.d.
  lognormal returns (ASM).
- The grid (rival capped, s = 1/2 unless stated): a = 0.50 total $164k/$212k/$297k, bottom $101k; a = 0.60 total
  $171k/$210k/$278k, bottom $121k; a = 2/3 $176k/$208k/$265k, bottom $134k; default (a ≈ 0.744) $182k/$207k/$250k,
  bottom $150k; a = 0.80 $186k/$206k/$240k, bottom $161k. Every row's total is at or above E1's p5 except a = 0.50, and
  the medians sit within $4k of E1's $210k.
- **s changes only the split between gift and kept money:** default rule at s = 3/4 gives gift $172k/$186k/$207k and
  kept $8k/$19k/$50k (E1-sized gift at the median, a thinner cushion in bad markets); at s = 1 the kept money is zero
  whenever stocks fall, which would breach case test 5 (L145), so s = 1 is out.
- **Share of E1's paths whose 2031 bottom is below the rival's:** 22% against the default ($150k); 5% against a = 2/3
  ($134k); 40% against a = 0.8 ($161k) (E4 [2]).
- **Share of the median 2033 gift already owned when she speaks in 2031:** rival default 86% (E4 [7]); E1 89% (E3 [3]).
  Both announce mostly bought money; the rival's bought part was fixed three years earlier.

### 2.2 Stress (E4 [3])
- **Bad 2028-2030** (worst 10% of three-year stock returns, before she speaks): E1 bottom median $134k (p5 $119k), gift
  $151k, total $168k. Rival default: bottom $150k (p5 $150k), gift $165k, total $186k.
- **Bad 2031-2032** (worst 10% of two-year returns, after she has spoken): E1 gift median $185k (from $188k), total
  $203k; rival default gift $169k (from $174k), total $189k. Both stay at or above the announced bottom in 100% of these
  paths (bought). The rival's stock fund carries more of the damage in dollars of total money (-$18k vs -$7k at the
  median), which is its main weakness (section 7, X4).

### 2.3 History, every 6-year window 1928-2025 placed in 2027-2032 (E4 [5]; Damodaran S&P 500 total return, VP dataset
page via D3 snapshot; bond proxy 50% bills + 50% 10-year, ASM as D3)
- **Raw history (93 windows):** total worst / p10 / median: E1 $123k (1929 start) / $180k / $221k; rival default
  $171k / $190k / $223k; rival a = 2/3 $162k / $187k / $230k. Bottom worst: E1 $95k; rival $150k.
- **Rescaled to JPM's median returns:** E1 $120k / $174k / $214k; rival default $169k / $185k / $214k; rival a = 2/3
  $159k / $180k / $218k.
- **Named windows (rescaled):** 1929-34 E1 total $120k (bottom $93k) vs rival $170k (bottom $150k); 2000-05 E1 $174k
  (bottom $139k) vs rival $186k; 2007-12 E1 $179k (bottom $142k) vs rival $188k; 1973-78 E1 $210k (bottom $170k) vs
  rival $194k (E1 wins when the crash is early and the recovery lands before 2031).
- **Top reached (the rival's only probability):** the S&P 500's two-year total return was zero or positive in 84% of
  97 overlapping periods 1928-2025, 86% of non-overlapping ones, 89% since 1950 (E4 [5], VP data, derived); the JPM
  lognormal model gives 73% for world stocks (MODEL). History is U.S. only; VT is global (limit, labelled).

### 2.4 Sensitivities (E4 [4], [7])
- January-2028 five-year rate 4.00% / 4.98% / 5.23% (the 5.23% is the forward implied today, not lockable, AX2 C1):
  stock fund $35k / $40k / $42k; total median $199k / $207k / $209k; the minimum stays $150k in all three.
- Deposit $75k (beyond-case stress, labelled as the team's own, R-AN35): minimum $75k by rule; total $94k/$109k/$135k
  (E1 P4 reports $73k/$105k/$149k for the same stress).
- Rates fall before January 2027: -50bp and -100bp leave the minimum at $150k (the top-up comes out of the stock fund,
  which falls to about $31k and $15k); -150bp leaves about $147k and no stock fund (E4 [7], VRF top-up table from D1/D3,
  ASM parallel shifts).

---

## 3. The rival's WInS book and Trading Notes plan (TN; tier 1)

### 3.1 Which book: the plan on 2 January 2028, scaled to $300,000 (the rival's version of option (ii))
- **Why this date (INT):** it is the first day all three jobs exist (operations, the building's minimum, the stock
  fund). The rival's central idea is a split of jobs, not a ban on stocks before a date, so a day-one stock purchase in
  WInS does not contradict it (the fix E2 F4 asks E1 to make).
- **The consistency sentence the IPS must carry (elements; D10 1.5):** the date WInS shows (after both deposits);
  scaled to $300,000; stand-in funds, not the ladder itself; in January 2027 almost all of her real $300,000 buys the
  payments.

### 3.2 Orders (illustration at the 2026-09-25 closes; recompute every share count from the last close before
entering orders, T2 finding 1; E4 [7])

| # | Holding | Weight | ~Shares at 9/25 | Job (Guide role word) | Primary / alternates | 2025-26 list (history only, VRF) |
|---|---|---|---|---|---|---|
| 1 | IEF (7-10y Treasuries) | 23.5% | ~783 | operations: future funding | IEF; VGIT then SPTI (ticket v1 s12) | IEF yes |
| 2 | TLH (10-20y Treasuries) | 42.5% | ~1,365 | operations: future funding | TLH; IEF + TLT at duration weights; SPTL under a cap (ticket v1 s3) | TLH no, TLT yes |
| 3 | **The building's minimum:** a Jul-Dec 2032 U.S. Treasury (best: 4.125% note of 15-Nov-2032, CUSIP 91282CFV8) or **IBTM** (iShares iBonds Dec 2032 Term Treasury ETF) | 24.3% (24.0% under a 25% cap) | note: about $75k face; IBTM ~3,336 | building minimum: future funding (and liquidity on the gift date) | 1) the 2032 note (one $10 trade); 2) IBTM ($25); 3) if neither is listed, an undated stand-in of similar duration (IEI, 4.20y) labelled "moves like, not dated" | IBTM no; IEI no |
| 4 | VT (world stocks) | 8.7% | ~163 | stock fund: growth | VT; VTI + VXUS (62/38); ITOT + IXUS | VT, VTI, VXUS yes |
| | Cash float | about 1% ($2,990 after 4 x $25) | | liquidity | | |

- Issuer facts (VP): IEF 6.86y, TLH 11.58y effective duration, both 0.15% (9/25, ticket v1); VT 0.06%, 10,088 stocks,
  37.7% non-U.S. (8/31; ticket v1); **IBTM NAV $21.83 (9/25), expense 0.07%, 30-day SEC yield 4.79% (9/24)** (re-read
  on https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf on 2026-09-28 with the fetch
  helper); IBTM effective duration 5.05y, 15 notes maturing Apr-Sep 2032, net assets about $555m, about 216k shares a day
  (9/24-9/25, VP via D1/S1). The page also says the funds "will terminate on or about October or December 15 of the
  year in each Fund's name" and "do not seek to return any predetermined amount" (both found verbatim, 2026-09-28).
  The 2032 note's model price (95.27 clean, about 1.5 accrued per 100 on 9/25) is D1's (ASM); WInS shows its own price.
- **Compliance:** every order is an ETF, a U.S. Treasury or cash (permitted, R-W67-R-W69, VP); no leverage, inverse,
  crypto-linked or thematic fund; each order is far below twice daily volume on published volumes (D10/AX2 C5; IBTM
  3,336 shares vs about 216k a day); four or five trades; no same-day round trips (User Guide "Day Trading: This is not
  permitted", VP). Under a single-security cap: IBTM held at the cap minus one point; TLH split per the ticket's cap
  table. A separate bond limit, if shown, governs the 2032 note (read both Session Rules lines, ticket gate (c)).
- **What the book says at a glance (INT):** three jobs, three instruments. The building's minimum is dated (it ends in
  late 2032); the operations stand-ins (IEF/TLH) never mature but move like the dated payments (a listed 2032-2041
  Treasury rung would add a second dated holding, ticket v1 s7); the stock fund is the smallest holding and the only one
  whose fall no promise's value mirrors.

### 3.3 The three notes (elements only; the team writes every word; ≤300 characters until the box is checked at zero
risk, ticket gate (c))

| Note | C1 role + the team's own label | C2 Laura's dated need (with the scaling marker) | C3 one checkable fact (dated, source in words) | C4 the rule (or move to the reflection) | Never say |
|---|---|---|---|---|---|
| A. Building's minimum (the 2032 note or IBTM) | future funding (liquidity on the gift date) | the minimum of her 2033 building gift, sized to her 2028 deposit, "after her 2028 deposit" | the note's maturity (15 Nov 2032, 47 days before 1 Jan 2033) or IBTM's holdings (Apr-Sep 2032 notes) and end date (about Dec 15 2032) (iShares, dated) | bought the day its money arrives; never sold because rates moved | "repays $X" for IBTM (AX1b item 6); "guaranteed", "risk-free", "locked 5.2%"; any range or 2031 top |
| B. Stock fund (VT) | growth | the building's upside and her flexibility, from the money left after the minimum, "after her 2028 deposit" | its share of the book (about 9%: all the stock the plan holds); or VT's stock count / top-ten share (Vanguard, dated) | held to 2033, never rebalanced or sold for market reasons; a fall shrinks the upside, never a promise | a return forecast; "halves AI exposure" (AX2 C5); "Laura likes risk"; the statistics degree |
| C. Operations (TLH, or IEF) | future funding | the ten $50,000 payments 2033-2042, "after both deposits" | the security's own effective duration (TLH 11.58y or IEF 6.86y, iShares, dated); the mix of the two (about 9.9y at 23.5/42.5) is what moves about 10% per 1-point rate change, as the payments' value does (9.90y, VRF; the team's own calculation) | never sold after a rate rise; only re-mixed to keep about 10 years | match, matched, mature in her years, stable, reduce volatility, operating reserve |

- **Reflections (≤100 words each; TN guide L46-52, VRF):** the three official answers, plus exactly one extra job each
  (E2 F9): note C carries the pre-registered **tested** window (fill date to the Oct 20 close: rate move in bp, hedge %
  change, payments' % change, labelled as the team's own calculation; ticket v1 s6); note A carries the **scaling** and
  the forced-vs-chosen caution line; note B carries the **refined** story that is true for this team (the first plan,
  growth-first at about 75% equity, was tested and dropped: 3.2% miss, 40.8% if the 2028 deposit is missing; F-401,
  F-404, VRF; E2 F8). Never invent a refinement (R-W28).
- **Order of entry:** operations first, then the minimum, then VT, in one session (the time stamps show promise-first,
  D7). If a Jul-Dec 2032 note is listed, price it in the drop-down first (ticket v1 s7).
- **Distinctiveness check (INT):** note A differs from Wharton's own example (an intermediate Treasury ETF "to reduce
  portfolio volatility", TN guide L36-39, VRF) by a date, a person and a job; neither E1 note under (ii) can say what
  note A says, because E1's bottom is not bought until 2031 and its VGSH note is banned from naming it (ticket v1 s5).

### 3.4 Gate decisions the rival would take before the first order (ticket v1 gate (b) already lists the first two)
- [ ] Facility bottom bought in **January 2028** (not 2031): yes.
- [ ] Growth money's bond part: **dated to December 2032** (the 2032 note or IBTM), not VGSH.
- [ ] The minimum rule (= the 2028 deposit's amount) and s = one half, decided and logged with first names, date and
      reason, because note A records the rule permanently (TN guide L30-31: notes must be consistent with the later IPS).
- [ ] Bonds drop-down screenshot: every U.S. Treasury maturing Jul-Dec 2032 (and 2033-2041 for an optional rung).
- [ ] If neither a 2032 Treasury nor IBTM is listed: the undated stand-in is weak; the rival would then accept E1's
      (ii) book with the same notes' logic, or ask Wharton (Contact Us) before trading.

---

## 4. The rival's IPS (IPS; tier 2): elements, budget and rules to fix before Nov 6

### 4.1 Pitch content (≤50 words; zero numbers; no Laura quote, no pull quote, no puns; the team words it)
1. What the plan secures for the residency, and when: its ten operating years, then the building's minimum, each bought
   the day its money arrives.
2. Whose money does what: the first deposit for operations; her own 2028 earnings for the building's minimum.
3. What the rest is for: only money nobody relies on is in world stocks, for a larger gift and her flexibility, so in
   2031 she tells partners only what she already owns (the fourth idea only if words allow; E2 F3 caps the pitch at
   three).
- Must not contain: a date-certain claim about the ladder; "fits inside $300,000"; "guaranteed", "risk-free", "100%",
  "safe"; jargon (barbell, LDI, duration, STRIPS); identity imagery (D13c section 5).

### 4.2 The ideas the IPS carries (about 10; E2 F1 target about 12), with a rough word budget (INT estimates)

| # | Idea (content) | Words |
|---|---|---|
| 1 | Purpose and central idea: each promise bought on arrival; stocks only where nobody relies on the money | 30-40 |
| 2 | 2027 rule with its one rates-fall branch (longest-first, completed from the next money, one "because") | 30-40 |
| 3 | 2028 rule: complete the ladder, buy the minimum equal to her deposit, one stock fund held to 2033 | 30-40 |
| 4 | 2031 rule: nothing traded; the bottom is owned; the top is today's value of half the stock fund; confidence both ways, history named in words | 35-45 |
| 5 | 2033 rule: reserve = the ladder, held to maturity; gift up to the announced top; the rest hers, in short Treasuries | 30-40 |
| 6 | Certainty definition with the two gaps (price in January 2027; US$ in Taiwan) | 40-55 |
| 7 | Risk by goal, as a maximum-loss statement; forced vs chosen caution | 30-40 |
| 8 | Diversification by purpose and date; liquidity by maturity dates | 20-30 |
| 9 | Governance: what may change a rule; no rebalancing between parts; who decides | 20-30 |
| 10 | The WInS date sentence (after both deposits, scaled, stand-ins) | 20-30 |
| | **Total before connecting words** | **about 285-390** |

- Leaves room for connecting prose inside the 470-490-word page-fit target (D9; AX2 D10 C3). The exported PDF must end
  on page 3 (IPS guide L82-83, L103-109, VRF).
- **Trade-offs to name inside the "because" clauses (Guide p.5 "reasoning, assumptions, and tradeoffs", VRF):** less
  stock in 2028-30 for a bottom that does not depend on those years; a top that cannot be exceeded for a top that needs
  no forecast; the chance of cheaper bonds after 2028 for never paying more because rates fell.

### 4.3 Rules the rival fixes before Nov 6 (so the Final Report applies, never redesigns; IPS guide L73-75, VRF)
- The four dated rules and the governance line (section 1.2), with: the minimum = the 2028 deposit's dollar amount
  (or what is left after completing the ladder, if less); s = one half; the cap at the announced top; the stock fund is
  one broad world fund, never rebalanced or sold before 2033; the kept money moves to short Treasuries on 1 Jan 2033.
- The certainty definition, the currency rules and the building-cost assumption (section 1.3).
- The confidence method for the top: history named in words (U.S. stocks, two-year periods since 1928) and the model
  named in the Final Report; never "100% within".
- No fee in the IPS; if the team keeps a cost clause, costs are paid from the stock fund, never from the ladder or the
  minimum (E3 finding 4; D8 M026).

---

## 5. Where the E1 plan loses to the rival (precise; each with evidence and the criterion it costs)

| # | E1 weakness | Evidence | What the rival does instead | Criterion (SMApply L49-57, VRF) |
|---|---|---|---|---|
| L1 | **The co-sponsor bottom is not known until 2031 and moves with 2028-30 markets.** E1 bottom p5/p50/p95 $134k/$167k/$211k; after a bad 2028-30, median $134k (p5 $119k); worst historical window $93-95k (1929 start); 2000-05 $139k | E4 [2], [3], [5] (MODEL; VP history); D3 M059 history table (before-lock crashes cut the facility money 19-48%) | A bottom equal to her 2028 deposit, owned from January 2028; worst historical window $150k | Investment Strategy ("disciplined planning across Laura's changing time horizons"); Creativity & Presentation (co-sponsor credibility) |
| L2 | **The top is a model property.** E1's top uses a percentile q of a model that "has too few very bad years" (AX1 C12); an 80-90% top lands within the range 62-97% of the time across models and history (D3 v2 (f)); E1 must also still choose q (E1 C5) | D3 v2 (f), AX1 C12, E2 R7 | The top is a market value she can read on the day; its only probability comes from history (84% since 1928) and can be checked by a statistics graduate or a co-sponsor's accountant | Portfolio Analysis ("reasonable assumptions"); Client Knowledge (a statistics-trained client, R-AN32) |
| L3 | **E1's reason for not buying the bottom in 2028 has been withdrawn.** E1 L97-98 cites "$101k vs ~$165k", which compares a 50% lock with an 80% lock; at the same 80% share the bottoms are $161k (2028) vs $165k (2031), and the barbell beats the plan at every percentile at equal stock exposure | AX1 C6 (VRF audit); E2 E-1, R2; ticket v1 gate (b) now lists "January 2028 or January 2031?" as open | At equal stock exposure (a = 2/3, 59 vs 58 percent-years) the rival's total is p5 +$8k, median -$2k, p95 -$1k in the model, and better in every historical summary (worst $159k vs $120k; p10 $180k vs $174k; median $218k vs $214k, rescaled) | Investment Strategy; Portfolio Analysis |
| L4 | **Money with a known use-date sits in rolling short Treasuries (VGSH)** | E2 R1; AX1 C18 (locking the bond part to 2033 is worth about $4-9k at the median); T2 finding 5 | The bottom is dated to December 2032, the month before the gift | Portfolio Analysis ("understanding and effective use of investment concepts") |
| L5 | **The central idea is a prohibition that E1's own WInS book breaks on day one** (a time-worded ban next to a day-one VT buy) | E2 C1 and F4; AY2 D7 C3; E3 finding 5 | A split-of-jobs idea that is true in the 2027 plan, the 2028 plan and the WInS book | Investment Strategy ("consistency with the team's IPS"); Creativity & Presentation |
| L6 | **E1's third note is the weakest in the set** (VGSH: "the ordinary effect of not holding stocks", AY1 C10) and may not name the promise it prepares for (ticket v1 s5 bans "the 2031 floor", "already owned") | E2 section 1, 3.1; ticket v1 s5 | Note A names a dated holding for the building's minimum, sized to her 2028 earnings; it is honest because that promise is bought in 2028 under the rule | Portfolio Analysis ("why each security belongs"); Client Knowledge |
| L7 | **Density.** About 55 distinct ideas for the pitch plus IPS (one per ~9 words), the growth-mix debate (50 vs 60, band, reset), a, s, q, cap or no cap | E2 section 3.2 | About 10 ideas; parameters: the minimum rule (set by a case number), one half, the cap | Creativity & Presentation ("a compelling, well-organized narrative"); last year's lesson (v4 Part 2) |
| L8 | **Nothing co-sponsors can count on can be named in the IPS** without a projection; E1 P17 correctly bans dollar ranges | E1 P7, P17; IPS guide L68-69 | The rule's output is a number the case already gives (her 2028 deposit), so the IPS can name what the building will at least receive as a rule, conditional on the deposit | Client Knowledge ("recommendations that can earn her confidence") |
| L9 | **The $150k is doubted in three places** (P2 gap (i), P3, P4 branches) | E2 C6, E-3 | One clause: the minimum is sized to whatever arrives; a smaller or later deposit gives a smaller or later minimum; the payments come first | Client Knowledge (R-AN35 "will") |
| L10 | **E1's risk statement for the growth money is a model threshold with a weak yardstick** ("about 1 in 20 below the money put in") | E2 R3, F6; AX1 C4 (median vs mean) | A maximum-loss statement that needs no model: at most the stock fund, about 9% of her money in 2028 | Portfolio Analysis; Client Knowledge |
| L11 | **E1 cuts stocks to about 3.5% of her money in 2031** and holds almost none after she has spoken | E1 P5 [3]; D13c N1 | The rival's stock fund stays invested to 2033 (about 9% rising); "pursuing growth" continues to the gift date (partial win only: see X2) | Client Knowledge ("thoughtful risks") |

---

## 6. What E1 would need to win back (precise changes, in deadline order)

**Tier 1, before the VGSH order (WInS-now and TN):**
1. **Take the open gate decision explicitly** (ticket v1 gate (b); AX1 C6; T2 finding 5): "facility floor bought in
   January 2028 or January 2031?". If 2028: E1 becomes the rival's structure and should adopt section 3.2 row 3 and
   note A. If 2031: E1 must record why (the two surviving reasons, AX1 C6: more money growing in 2028-30 and less stock
   at risk after Laura has spoken) and accept L1 in writing.
2. **Replace VGSH with a dated December-2032 instrument** even if the bottom stays in 2031 (AX1 C18; E2 R1): the 2032
   note or IBTM holds the growth money's bond half to a known date; the note then carries a checkable date instead of
   "the ordinary effect of not holding stocks".
3. **Reword the central idea as a split of jobs** before any note is saved (E2 F4), so no permanent note contradicts
   the IPS.

**Tier 2, IPS by about Oct 26 (first draft):**
4. **Make the top checkable without a model**, or at least name the history check next to q (D3 v2 (f): a p90 top lands
   within in 81% of raw history), and drop "promised" for the stretch (E3 finding 1).
5. **Give the bottom a case-anchored meaning** the IPS can name (for example, relating the bought share to her 2028
   deposit), so co-sponsors hear a rule with a known output, not "a share of whatever the sleeve is worth in 2031".
6. **Cut to about a dozen ideas** (E2 F1): if the bottom moves to 2028, the growth-mix rule, its band and the 50/60
   debate disappear (the stock fund is simply "all of what is left").
7. **Say E1's real advantages out loud** (section 7): a higher median bottom and gift, more stock in 2028-30, and an
   uncapped upside that visibly answers "favorable outcomes" (L118). If the team keeps E1, these are its answer to the
   rival, and they belong in the rules' "because" clauses.

---

## 7. Where the rival loses to E1 (honest), and what each side should steal

| # | Rival weakness | Evidence | Size | What would fix it |
|---|---|---|---|---|
| X1 | **Lower median bottom and gift.** E1's 2031 bottom exceeds $150k in 78% of model paths (median $167k); median gift $188k vs $174k | E4 [2] | -$17k bottom, -$14k gift at the median | Raise s to 3/4 (gift median $186k; kept p5 falls to $8k) or lock more (a = 0.8: bottom $161k, less stock) |
| X2 | **Less stock over 2028-32** (45 vs 58 percent-years; 8.7% vs 17% of her money in 2028); lower p95 (-$16k total, -$50k gift) | E4 [2] | A real "pursuing growth" and "thoughtful risks" cost (L70-73; D13c N1) | The a = 2/3 alternate equalises stock exposure (59 percent-years) at the price of a $134k bottom |
| X3 | **The cap:** strong markets add to her flexibility, not to the gift; co-sponsors never see more than the top. D5 argued uncapped is the more honest answer to "how favorable ... outcomes could affect the amount" (L118) | D5 finding 5; AX1 C3 | Excess above the top goes to Laura (her decision, AX1 C15) | Keep the cap but let Laura decide in 2033 to give more (a choice, not a promise) |
| X4 | **The stock fund is 100% stocks after she has spoken.** A bad 2031-32 cuts the rival's total by $18k at the median vs $7k for E1; the gift stays within the range in both | E4 [3]; D3 M238 | The bottom is untouched; the gift slides toward it | Accept as the price of a bottom fixed in 2028, or add a 2031 partial lock (a second rule; rejected on simplicity) |
| X5 | **Kept money sits in stocks until 2033** (D8 M081 says flexibility belongs with safety) | D8 M081 | The kept money is still at least E1's at every percentile ($16k/$32k/$66k vs $16k/$21k/$29k) | It moves to short Treasuries on 1 Jan 2033 (both plans) |
| X6 | **WInS availability:** no individual 2032 Treasury may be listed; IBTM is thin (about $555m), not on the 2025-26 list, and "does not seek to return any predetermined amount" | D1; AX1b; iShares (VP) | Note A would lose its date if only an undated stand-in is available | Check the Bonds drop-down and search IBTM before the gate; otherwise ask Wharton |
| X7 | **The January-2028 five-year rate is unknown.** At 4.0% the stock fund is about $35k, not $40k | E4 [4] (ASM) | Smaller upside; the minimum is unchanged | None needed; the rule adapts |
| X8 | **Novelty and explanation risk.** A barbell can read as a "structured product"; the rival must never use the word or justify it by her career | D13c section 3.4; brief section 16 | Word cost, not money | Describe it by its jobs and dates only |

**What the rival would steal from E1:** P2 (certainty with two named gaps), P3/P4 (the 2027 rule, longest-first, the
joint tail named once), P6 (risk by goal), P8 (US$ binding; no NT$ hedge), P10 (governance wording that cannot read as
permission to revise), P15 (decision and AI logs), P16 (page-fit test and paraphrase test). E1 is right on all of these,
and the rival adopts them unchanged.
**What E1 should steal from the rival even if it keeps the 2031 bottom:** the dated December-2032 bond part (L4), the
split-of-jobs central idea (L5), the maximum-loss framing of stock risk (L10), and the four-date IPS spine (E2 F2).

---

## 8. Open conflicts for the team (both sides; the team decides)

| # | Conflict | For the rival | For E1 | E4 view (INT) |
|---|---|---|---|---|
| C1 | When is the facility bottom bought? | 2028: fixed three years before she speaks; better bad case and history tails (L1, L3) | 2031: more stock in 2028-30, higher median bottom and gift (X1, X2) | A genuine choice of **when** to take risk; the rival's version is easier to say and to check. Decide before the VGSH order |
| C2 | Size of the bottom | Her 2028 deposit (a case number, no free parameter) | 80% of a sleeve value (a share, output unknown until 2031) | The deposit rule is more tailored; a = 2/3 or 0.8 are the numeric alternates |
| C3 | Top: capped market value or uncapped model percentile | No forecast; one historical probability | Good markets visibly raise the gift; D5's two-sided statement | Either is honest if the capped version reports only P(top reached) |
| C4 | Stock exposure 2028-32 | 45 percent-years (default) or 59 (a = 2/3) | 58 | Pick the default for credibility, the alternate for growth; say which in one "because" |
| C5 | WInS third note | Building minimum (dated, Laura-specific) | VGSH (risk management of growth money) | The rival's note is stronger if a dated instrument is listed |

---

## 9. Later (after Nov 9), one line each (Final Report; not worked here)
- The co-sponsor range in dollars at median, weak and strong 2031 states, and the "share already owned" figure.
- The history table (named windows) next to the model's p5, for both designs.
- The fundraising-excerpt order (operations bought, minimum owned since 2028, the top and its historical odds, what is
  not promised, US$ binding) as the team's own checklist.
- NT$ illustration of the minimum at a dated rate, with the 2031-view exchange-rate band (D4).
- The rejected-alternatives table (growth-first, E1's 2031 lock if not chosen, uncapped percentile top, TIPS minimum).

---

## Sources (accessed 2026-09-28 unless noted)

**Official, in the repo (VRF):** `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L43-45, L61-74,
L83-120, L126-149, L161-162); `2026_WGY_Investment_Policy-FINAL.txt` (L20-26, L45-52, L68-75, L82-83, L101-123);
`2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L11-15, L25-31, L36-53); `2026_WGY_Investment_Competition_Guide.txt`
(L84-90, L154-159, L183-184); `SMApply_Deliverables_Page_2026-09-27.md` (L49-57).

**Market data (VRF):** `competition/official_market_data/daily-treasury-rates_2026-09.csv` (row 09/25/2026: 2y 4.81,
5y 4.98); `JPM_LTCMA_2026_US_matrix_USD.pdf` p.2 (AC World 7.00/8.28/16.78).

**Primary web (VP):**
- iShares IBTM page, https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (read by E4
  on 2026-09-28 with `research/insight_v1/scripts/fetch_text.py`; NAV, expense ratio, SEC yield and both quoted
  sentences found verbatim).
- Damodaran, Historical Returns on Stocks, Bonds and Bills,
  https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html (snapshot
  `research/insight_v1/scripts/data/D3/damodaran_histretSP_1928_2025.csv`, VP per D3 and AX1).
- SMApply Trading Details and FAQ, https://wghsinvcomp.smapply.us/res/p/trading/ , /res/p/faqs/ (via case_register
  R-W56-R-W92); 2026-27 WInS User Guide (via A4, D1, AY1); Wharton Rules & Roles and AI policy (via Phase A); CFA
  Institute *Elements of an IPS* (2010) and *Investment Risk Profiling* (2020) (via D6, D8, D10). Not re-opened by E4.
- Issuer facts for IEF, TLH, TLT, VT, VTI, VXUS, IEI, VGIT, SPTI, SPTL as carried by `wins_now/securities_and_allocation_v1.md`
  and `wins_now/S1_treasury_sleeve.md` (VP there; not re-opened by E4).

**Research files (lower authority; audit corrections applied):** `research/insight_v1/phase_E/E1_change_proposals.md`,
`E2_judge.md`, `E3_laura.md` (summary); `phase_D/` D1-D12, D3_model_v2_results, D3_quant (AX1), D13a, D13c, and
`audit_rates_quant.md`, `audit_rates_D1.md`, `audit_markets_rules.md`, `audit_client_cosponsors.md`,
`audit_judges_practice_comms.md`; `phase_D/trading_now_brief.md`; `wins_now/securities_and_allocation_v1.md`,
`T2_red_team.md`, `S1_treasury_sleeve.md`, `S2_growth_sleeve.md`, `S3_final_report_ladder_and_reserve.md`,
`S4_red_team.md`; `phase_A/case_register.md` (R-AN4, R-AN6, R-AN9, R-AN14, R-AN15, R-AN20, R-AN32, R-AN35, R-AN45,
R-AN52, R-W67-R-W92), `fact_register.md` (F-101-F-117, F-401-F-409), `stakeholder_map.md` (SH-04, SH-05, BS-03, BS-13,
BS-17); `phase_C/parked.json` (M008, M015, M033, M035, M040, M149); `research/council_2026-09-27/01_chair_memo.md`,
`round2_referee_ruling.md` (history).

**Scripts:** `research/insight_v1/scripts/E4_rival_numbers.py` (new); re-used engine `D6_behavioural_numbers.py`;
reproduces `E1_split_and_slices.py` [4] row 1; top-up costs from `D1_purchase_rule.py` / `D3_joint_tail.py` tables.

---

## What this teaches

1. **The same money can be promised at different times.** E1 and the rival buy the same payments (and, at the rival's a = 2/3
   alternate, hold the same stock exposure); the difference is *when* the facility bottom is bought. Buying it in 2028 fixes it before three
   years of markets; buying it in 2031 lets those years raise or lower it. That timing is a strategy choice, not a
   detail.
2. **Compare designs at equal risk before calling one better.** At the same stock exposure, the dated barbell has a
   better bad case and better historical tails; at lower exposure it trades growth for certainty. Line options up on
   the same risk first (AX1's lesson, applied).
3. **A number with no forecast in it is the most credible number you can say in public.** A bought minimum and a
   market value on the day need no model; only the chance of reaching the top does, and history can check it.
4. **Let the client's own facts set your parameters.** The case already gives a number that means something to Laura
   and to her partners (what her 2028 work earns); using it removes a free parameter and makes the plan visibly hers.
5. **A good rival shows you your own weak joints.** Most of what the rival wins comes from choices E1 left open
   (floor timing, a dated bond, a model-based top, a prohibition as the central idea). Closing those joints, whichever
   way the team decides, is what makes the plan hard to beat.
