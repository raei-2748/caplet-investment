# Forward view: what to expect at the 6 Nov freeze, at 4 Dec and on 1 Jan 2027 (Wave H, Tue 20 Oct 2026, about 10:55-11:50 Sydney)

> **Verified 20 Oct (`oct20/verify_forward/verify_forward.md`): D-basis numbers reproduce; fix before use.** High: basis M2 leaves out the 0.07% iBond fee (copies the reconcile fee bug); fee-counted M2 is **$300,652 on 19 Oct (~$650 OVER the line)**, P(>$300k) ~55% at 6 Nov and ~52% at 1 Jan (matches engine_v3 $300.7k / 52%). The 0.97 correlation is between the book and the 6 Nov reading of the January cost; against the real 31 Dec cost it is ~0.51. "8 of 10 largest moves had no scheduled release" is wrong (28 Mar 2025 PCE, 10 Sep 2026 PPI): say 6 of 10. Jobless claims 22 Oct = Thu 23:30 Sydney; 3 Dec is bond day 31.

**These are AI-generated MODEL numbers and checklists (Claude Code) for Team Caplet. This is not text to submit.** The file contains distributions, decision requirements and an event calendar. It drafts no TNA, IPS or Final Report wording. Where it says what a deliverable "must" contain, the students write it. If a student uses any figure, they re-check it and log the AI help. Wharton's AI Policy says: "If you use AI to assist you in any way during the competition, how you use it must be recorded in your Works Cited pages" (https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).
- **MODEL** means a computer estimate, not a fact.
- **UNVERIFIED** means nobody could confirm it.
- Probabilities are model odds, not forecasts of the market.

**Folder:** `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/forward/`, written `FWD/` below. Sibling folders are written `oct20/<x>/`.

---

## 0. The short version

1. **The 1 Jan 2027 ladder cost has about a 4-in-10 chance of ending above $300,000 on basis D. On the maturity-sizing basis it is a coin flip.**
   - Basis D: 38-41%, median about $297k. The middle 90% runs from $283-312k (2026-like volatility) to $277-319k (σ 1.0).
   - Maturity sizing, engY version (M2): 49-50%. On 19 Oct it was only **$139** under the line.
   - The coupon-study version of maturity sizing (M1) sits between them: 43-45%.
   - At the 6 Nov close the odds of being over are 28-34% (D) and about 49% (M2).
2. **Expect the line to be crossed at some close, even if it is not crossed on the day that counts.**
   - On D, the cost goes over $300k at at least one close before 6 Nov in 46-58% of paths, and before 31 Dec in 69-77%. Paths cross the line about 3 times on average before 31 Dec.
   - On M2 the figures are 83-84% and about 91%.
   - So any sentence such as "the line has not been crossed" is only safe with a date on it.
3. **The $145k bottom (option 1; $135k under 3r) survives January in only 63-68% of paths on D, and 54-57% on M2.**
   - The cost only has to pass $301,300 for the bottom to drop by $5k. On D that takes a 0.14-point fall in yields; on M2 only a 0.05-point fall.
   - It drops by $10k or more in 16-24% (D) and 24-31% (M2) of paths.
   - The rule ("$5k steps") is safe to state. The dollar figure is not.
4. **WInS book at the 6 Nov close: median about $304.1k.**
   - Middle 90%: $298.0-310.4k on 2026-like volatility, or $295.9-312.6k at 1 point a year.
   - P(below $300,000) is 13-21%. P(below the 19 Oct $303.4k) is 42-45%.
   - Carry alone adds about $720 by 6 Nov.
   - Contributions to the change (p5 to p95): IBTM about −$1.1-1.2k to +$1.6-1.7k (−$1.7k / +$2.2k at 1 point a year). VT about ±$1.5-1.7k.
   - **The book and Laura's January cost move together (correlation 0.97).** In about 3 paths in 10 the book is up *and* her ladder is over $300k.
5. **The largest scheduled risk falls on the freeze day itself.** The October jobs report comes out Fri 6 Nov at 8:30 am ET (Sat 7 Nov 00:30 Sydney), 7.5 hours before the freeze close. In 2025-26, jobs days moved the ladder about 1.26× as much as an ordinary day.
   - Other dates in the window: FOMC (28 Oct), GDP and PCE (29 Oct), the midterm elections (3 Nov) and the Treasury refunding (2 and 4 Nov).
   - The November jobs report is on Fri 4 Dec, the Final Report deadline day.
   - **But 8 of the 10 largest one-day moves in 2025-26 came on days with no scheduled release.** The calendar says when to look, not what will happen.

---

## 1. Inputs, bases and method

**Curve.**
- treasury.gov daily par yield curve, 2022-2026 files, fetched 19 Oct 2026 at 23:18-23:20 UTC (`FWD/raw/tsy/`). URL pattern: `https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/<YEAR>/all?type=daily_treasury_yield_curve&field_tdr_date_value=<YEAR>&page&_format=csv`.
- The latest row is **19 Oct 2026**: 1y 4.50, 2y 4.77, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48. It is identical to `oct20/numbers/numbers_refresh.md:28`.
- **20 Oct was not published** at the fetch (19 Oct 19:20 ET, before the 20 Oct session).

**Bases** (each one reproduces its source exactly; `FWD/scripts/check_repro.py`):

| Basis | Definition | 19 Oct cost | Room under $300k | Fall that uses it up | DV01 | Source it reproduces |
|---|---|---|---|---|---|---|
| **D** | $50k zero-coupon at each holding's maturity date, yields unchanged to 1 Jan; linear zero-rate interpolation | **$297,162** | $2,838 | 9.8bp | $289/bp | `oct20/numbers/numbers_refresh.md:67` ($297,162) |
| **M1** | Maturity sizing, coupon-study version: coupon bonds (iBond funds as par bonds ending 15 Dec), sized to $50k at maturity with income reinvested at their own yield; log-DF interpolation | **$298,446** | $1,554 | 5.4bp | $288/bp | `numbers_refresh.md:194` ($298,446) |
| **M2** | Maturity sizing, engY version: iShares holdings (coupon less 0.07% fee, maturing at the fund's average maturity); income reinvested at the zero rate for the remaining term; the fund's own bill interest to 15 Dec counts; 0% to the 1 Jan payment | **$299,861** | **$139** | **0.5bp** | $290/bp | engY `rung_terms` at zero shift: $299,861 (`FWD/scripts/check_engY_M2.py`); `oct20/reconcile3r/reconcile_3r.md:202` "$299.9k / 50%" |

- Reconcile §3 says that if the team keeps maturity sizing, the honest cost is "about $298.5-299.9k" (`reconcile_3r.md:92`). M1 and M2 are those two ends. **M2 is the realistic one** (real iBond holdings).
- At ±0.25 points M2 matches engY within $50 ($307.2k / $292.7k against engY's $307,148 / $292,768).

**Horizons.**
- I counted bond-market days with SIFMA's 2026 US holidays: Veterans Day Wed 11 Nov, Thanksgiving Thu 26 Nov and Christmas Fri 25 Dec are closed (https://www.sifma.org/resources/general/holiday-schedule/, read 19 Oct 2026; `FWD/web/sifma.txt:43-52`).
- That gives **14 trading days** from 19 Oct to the 6 Nov close, 33 to the 3 Dec close and **50** to the 31 Dec close. The 31 Dec close stands in for "1 Jan".

**Methods** (`FWD/scripts/forward_sim.py`). Each uses 20,000 paths and was run on two seeds (20261020 and 7):

| Code | What moves the curve |
|---|---|
| P071 / P076 / P100 | Parallel shift, normal; σ 0.71 (2026 realised), 0.76 (63-day) and 1.00 (the number sheet's assumption) points a year |
| **E26** | Bootstrap of **whole-curve** daily changes from the 199 trading days of 2026 (non-parallel, real shapes). Demeaned, so 2026's yield rise is not projected forward |
| E23 / E23b | The same from 949 days, Jan 2023 - Oct 2026. E23b uses 5-day blocks to keep short-run momentum. 10-year volatility in this sample is 0.92 points a year |
| ED | Bootstrap and normal of the demeaned daily D-cost changes in `oct20/numbers` (SD $1,365 in 2026, $1,616 over the last 21 days). Basis D only |

- **"Yields unchanged" means each day's curve is treated as the 1 Jan curve.** So the 6 Nov value of a basis is "what the 1 Jan cost looks like on the 6 Nov curve".
- **The 2026 drift was removed:** the mean daily D change was −$141. Keeping it would mechanically project a further rise in yields of about 0.24 points by 31 Dec.

---

## 2. Laura's ladder cost: distributions (MODEL)

Every row below is seed 20261020; the seed-7 values differ by 1 point or less (`FWD/data/tables_out.md`). The parallel rows match the closed-form normal quantiles within $100 and 0.5 points (§6). The ranges use E26 (2026 behaviour) to P100 (the sheet's σ); E23 sits between them.

### 2a. At the 6 Nov close (the freeze and the Final Report's valuation date)

| Basis | Method | p5 | p25 | p50 | p75 | p95 | P(>$300k) | P(>$301.3k) | P(>$306.3k) |
|---|---|---|---|---|---|---|---|---|---|
| **D** | E26 | $289.5k | $294.0k | $297.2k | $300.4k | $305.0k | **27.8%** | 19.4% | 2.9% |
| D | P071 | $289.2k | $293.9k | $297.1k | $300.4k | $305.2k | 27.7% | 19.7% | 3.1% |
| D | E23 | $287.3k | $293.0k | $297.1k | $301.4k | $307.6k | 32.1% | 25.2% | 7.4% |
| D | P100 | $286.2k | $292.6k | $297.2k | $301.8k | $308.4k | **33.7%** | 27.2% | 9.1% |
| D | ED (21-day SD) | $287.3k | $293.1k | $297.2k | $301.3k | $307.1k | 32.0% | 24.7% | 6.6% |
| M1 | E26 / P100 | $290.7k / $287.5k | $295.3k / $293.9k | $298.5k | $301.7k / $303.1k | $306.3k / $309.7k | 38.0% / 41.1% | 27.8% / 33.6% | 5.1% / 12.5% |
| **M2** | E26 | $292.2k | $296.7k | $299.9k | $303.1k | $307.7k | **49.4%** | 38.9% | 8.7% |
| M2 | P100 | $288.9k | $295.3k | $299.9k | $304.5k | $311.1k | **49.4%** | 41.9% | 17.4% |

### 2b. At 1 Jan 2027 (the 31 Dec close, when the real purchase is priced)

| Basis | Method | p5 | p25 | p50 | p75 | p95 | P(>$300k) | P(>$301.3k) | P(>$306.3k) | Mean top-up |
|---|---|---|---|---|---|---|---|---|---|---|
| **D** | E26 | $282.7k | $291.2k | $297.1k | $303.3k | $312.1k | **37.5%** | 32.4% | 15.9% | $2.4k |
| D | P071 | $282.6k | $291.1k | $297.2k | $303.3k | $312.7k | 38.1% | 32.6% | 16.1% | $2.5k |
| D | E23 | $278.6k | $289.3k | $297.2k | $305.1k | $316.9k | 40.6% | 36.3% | 22.0% | $3.5k |
| D | P100 | $277.1k | $288.7k | $297.1k | $305.9k | $318.7k | **41.3%** | 37.4% | 23.9% | $3.9k |
| M1 | E26 / P100 | $284.0k / $278.4k | $292.4k / $290.0k | $298.4k | $304.6k / $307.2k | $313.5k / $320.0k | 42.9% / 45.1% | 37.4% / 41.2% | 19.6% / 27.1% | $2.9k / $4.5k |
| **M2** | E26 | $285.4k | $293.9k | $299.8k | $306.0k | $314.8k | **49.0%** | 43.4% | 24.0% | $3.5k |
| M2 | P100 | $279.6k | $291.3k | $299.8k | $308.6k | $321.5k | **49.4%** | 45.6% | 31.0% | $5.2k |

- **Cross-check against earlier work.** D at σ 1.0 gives 41.3%, against 41.4% in `numbers_refresh.md:99`; σ 0.71 gives 37.9-38.1% against 37.9%. M2 gives 49-50%, against "50%" in `reconcile_3r.md:202`.
- **The 3 Dec close** (last full close before the Final Report deadline): D 34.7-38.7% over $300k; M2 49%. This matters only for WInS tracking, because the Final Report's projections use the 6 Nov close (`oct20/frblue/fr_prep_v2.md` §4.1, lines 288-313 as of 20 Oct 11:45 Sydney).

### 2c. Bands, as odds (used by the decision table in §4)

Odds that the cost sits in each band; E26 to P100, seed A (seed B within 1 point; `FWD/data/bands_out.txt`).

| Band (cost) | Yield move from 19 Oct, parallel (D / M2) | D at 6 Nov | M2 at 6 Nov | D at 1 Jan | M2 at 1 Jan |
|---|---|---|---|---|---|
| A1: ≤ $295,000 | rise ≥ 7.5bp / ≥ 16.9bp | 32-37% | 15-24% | 41-43% | 29-35% |
| A2: $295,000-300,000 | rise 7.5bp to fall 9.8bp / rise 16.9bp to fall 0.5bp | 29-40% | 27-36% | 15-22% | 15-22% |
| A3: $300,000-301,300 (over, bottom intact) | fall 9.8-14.2bp / 0.5-4.9bp | 7-9% | 8-10% | 4-5% | 4-6% |
| A4: $301,300-306,300 (bottom −$5k) | fall 14.2-31.1bp / 4.9-21.9bp | 16-18% | 24-30% | 13-17% | 15-19% |
| A5: > $306,300 (bottom −$10k or more) | fall > 31.1bp / > 21.9bp | 3-9% | 9-17% | 16-24% | 24-31% |

- In 10-year terms (parallel, from 5.15% on 19 Oct): D goes over $300k at about 5.05%; the bottom loses $5k at about 5.01% and $10k at about 4.84%.
- On M2 the corresponding levels are about 5.145%, 5.10% and 4.93%.

### 2d. Path-wise odds: being crossed is likely even when ending over is not

| Basis | Method | Over at some close by 21 Oct | by 22 Oct | **by 6 Nov** | **by 31 Dec** | Over on 6 Nov *and* 31 Dec | Under 6 Nov, over 31 Dec | Over 6 Nov, under 31 Dec | Crossings to 31 Dec (mean) |
|---|---|---|---|---|---|---|---|---|---|
| D | E26 | 6.1% | 11.8% | **46.0%** | **69.2%** | 17.6% | 19.9% | 10.2% | 2.9 |
| D | P100 | 16.0% | 23.8% | **57.5%** | **76.5%** | 21.5% | 19.7% | 12.2% | 3.3 |
| M2 | E26 | 59.0% | 65.7% | **83.3%** | **91.1%** | 33.1% | 16.0% | 16.3% | 3.8 |
| M2 | P100 | 60.3% | 67.1% | **84.4%** | **91.7%** | 33.1% | 16.3% | 16.3% | 3.9 |

- **TNA window.** The "by 21 Oct" column covers the 20 and 21 Oct closes, the last ones the team can see on Thu 22 Oct evening Sydney. It gives 6-16% on D, which matches the verifier's "6.5-15.6%, about 1 in 8" (`oct20/verify_infl_num/verify_infl_num.md`, E4). On M2 it is 59-60%.
- **Being under at the freeze settles nothing.** About 1 path in 5 is under on 6 Nov and over on 31 Dec, on either basis.
- Daily repricing was done for D and M2 only; M1 sits between them.

### 2e. The 2031 bottom implied by the 1 Jan cost (rule: (150k − reserve − top-up − $3.7k), rounded down to $5k)

The rule is from `numbers_refresh.md:143` and `oct19/coupon` `coupon_options.py:15-18`. Values are E26 to P100, seed A; seed B is within 0.4 points.

| Basis | Option | Stays at the 19 Oct value | One $5k step down | Two or more steps down |
|---|---|---|---|---|
| D | Option 1 ($145k) | **63-68%** | 13-17% ($140k) | 16-24% (≤ $135k) |
| D | 3r ($135k) | 63-68% | 13-17% ($130k) | 16-24% (≤ $125k) |
| M2 | Option 1 ($145k) | **54-57%** | 15-19% ($140k) | 24-31% (≤ $135k) |
| M2 | 3r ($135k) | 54-57% | 15-19% ($130k) | 24-31% (≤ $125k) |

- My 63-68% (D) sits beside the number sheet's "61-72%" (`numbers_refresh.md:133`). Theirs includes later steps to 2031; mine is the January step only.
- **The step is $5k for any cost change across a boundary**, even $1. The boundaries are $301,300, $306,300, $311,300 and so on. That is the "minimum steps of $5k".

### 2f. If the 6 Nov close shows cost X: odds for 1 Jan (36 more bond days; parallel normal)

D and M2 give the same numbers to within 0.1 point, because the DV01s are equal.

| 6 Nov cost | P(1 Jan > $300k), σ 0.71 / 1.0 | P(1 Jan > $301.3k), σ 0.71 / 1.0 | P(1 Jan > $306.3k), σ 1.0 |
|---|---|---|---|
| $290.0k | 10% / 18% | 7% / 15% | 7% |
| $295.0k | 26% / 32% | 21% / 28% | 15% |
| $297.0k | 35% / 39% | 29% / 35% | 20% |
| $298.5k | 42% / 45% | 36% / 40% | 24% |
| $300.0k | 50% / 50% | 43% / 45% | 29% |
| $301.3k | 57% / 55% | 50% / 50% | 33% |
| $303.0k | 65% / 61% | 59% / 56% | 38% |
| $306.3k | 79% / 71% | 74% / 67% | 50% |

### 2g. Does the IBTR note's plain-words test match the cost test?

The filed note reads: "If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder" (`oct20/tnakit2/tna_fact_kits_v2.md:428`). Its "about 0.2" is basis D measured from the 6 Oct curve (`tna_fact_kits_v2.md:224-226`).
- Take the literal reading: the 10-year falls more than 0.20 below its 6 Oct 5.27%.
  - That happens by 31 Dec in 40-43% of paths, against 38-41% for D > $300k.
  - **The two tests disagree in 1.6-2.8% of paths.** Non-parallel moves cause this.
  - At 6 Nov the literal test is met in 31-37% of paths.
- **Requirement:** any reflection or report that cites the test must say what it measures (the cost of the ladder on the note's basis) and must not reduce it to a 10-year yield level.

---

## 3. WInS book at the 6 Nov close (MODEL; the WInS screen may differ, see 3c)

### 3a. Inputs
- **Start:** $303,393.47 at the 19 Oct close, including bond accrued interest (`oct20/attrib/attribution_pack.md` §3, Total row), with holdings values as at `attribution_pack.md §3`.
- **Book DV01:** $190/bp in my run, against $187/bp in the pack (`attribution_pack.md §4, "Rate sensitivity"`, at 7 Oct values).
- **VT:** 167 shares, $26,237, 8.65% of the book (`numbers_refresh.md:302`).
- **T-bonds** are fully repriced on the simulated curve for 9 Nov settlement (6 Nov is a Friday). Fill gaps are held constant.
- **iBond funds** use iShares effective duration (5.02 / 5.68 / 6.39 / 7.03 / 7.56) on their own tenor. Carry is at iShares average YTM (4.94-5.08%) less the 0.07% fee, over 18 days (`oct20/ldi/data/ibond_keyfacts_live.txt`, "as of Oct 16, 2026").
- **The 2 Nov ex-date / 5 Nov pay date distribution** is $600.81 at October rates (`attribution_pack.md §1 Distributions row; §8c`; future amounts UNVERIFIED). The base case assumes it is in cash by 6 Nov.
- **VT returns:** Yahoo daily adjusted closes (`FWD/raw/px/yh_VT.json`, fetched 19 Oct 23:20 UTC). Bootstrap methods draw the curve change and the VT return from the **same historical day**.
- **Stocks and bonds this year:** the correlation between the 10-year change and the VT return is −0.48 in 2026 (−0.13 over two years). Stocks fell when yields rose, so this year **VT has not hedged the bonds**.

### 3b. Distribution and contributions

| Method | p5 | p25 | p50 | p75 | p95 | P(< $300k) | P(< 19 Oct $303.4k) | IBTM change p5 / p50 / p95 | VT change p5 / p50 / p95 |
|---|---|---|---|---|---|---|---|---|---|
| E26 (2026 days, joint) | $298.0k | $301.6k | $304.2k | $306.7k | $310.3k | **13.0%** | 41.8% | −$1,236 / +$254 / +$1,716 | −$1,442 / −$13 / +$1,523 |
| E24 (Oct 2024-Oct 2026, joint) | $298.1k | $301.7k | $304.1k | $306.6k | $310.3k | 12.9% | 42.2% | −$1,305 / +$231 / +$1,830 | −$1,525 / −$11 / +$1,603 |
| P071 (σ 0.71, VT 16.78%, ρ −0.48) | $298.0k | $301.6k | $304.2k | $306.7k | $310.4k | 13.6% | 41.6% | −$1,097 / +$258 / +$1,602 | −$1,663 / −$20 / +$1,745 |
| P100 (σ 1.0) | $295.9k | $300.7k | $304.0k | $307.5k | $312.6k | **20.7%** | 44.7% | −$1,669 / +$225 / +$2,184 | −$1,680 / −$22 / +$1,733 |

- **No-move value** (curve unchanged, VT flat): **$304,112**. Carry and roll-down add T-bonds +$268 and iBonds +$451, of which IBTM is +$236.
- **Spread (SD):** T-bond sleeve $1.3-2.0k, iBond sleeve $1.8-2.5k, VT $0.9-1.0k, IBTM $0.8-1.2k.
- **IBTM and VT:** IBTM is 32% of the book and carries about a quarter of its rate risk ($49/bp). VT is under 9% of the book but is the largest single source of risk not driven by rates.
- **The trap:** the book and the basis-D ladder cost move together (correlation 0.965-0.984). The book is up *and* Laura's ladder is over $300k in 28-33% of paths. A WInS gain therefore usually means a dearer January purchase (`attribution_pack.md §4 checklist; §6c`).

### 3c. What the WInS screen may show instead (each UNVERIFIED until the team screenshots WInS)

| Screen effect | Size at 6 Nov | Source |
|---|---|---|
| Distribution not yet credited to cash on 6 Nov | −$601 (median not-credited value $303.6k) | iShares schedule ex 2 Nov / pay 5 Nov (`attribution_pack.md §1 Distributions row`); the FAQ says "at the time they are issued" |
| Total excludes accrued interest | −$1,711 at 9 Nov settlement (median $302.5k) | Own calculation (`FWD/data/tables_out.md`) |
| May-2038 run on a Feb/Aug schedule | −$225 (fixed until 15 Nov) | `attribution_pack.md §8a-8b` |
| Bond marks set at the US open, not the close ("updated once daily at U.S. market open", Wharton FAQ) | 1 SD about $360 (ordinary day) to $480 (jobs day) on the $88k T-bond sleeve. The 6 Nov open comes after the 8:30 jobs release | `verify_infl_num.md` E5; event-day SD in §5d |
| ETF screen price from a different moment | about $1.0-1.6k a day | `attribution_pack.md §8a` |

---

## 4. Decision table: what each outcome means for the rules already set (requirements only, no wording)

### 4.0 The rules this table applies (already set; cited)
- **R1. Quote no level in the TNA or IPS; state the rule.** Every basis also carries about ±$500 of curve-method uncertainty (`numbers_refresh.md:3, 18`; `verify_infl_num.md` E3).
- **R2. The IBTR note** (filed; cannot be edited) reads: "On the 6 Oct Treasury curve, her first $300,000 is enough to buy Treasuries for all ten payments. If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility." (`tna_fact_kits_v2.md:428`). Its basis is D from 6 Oct (`:224-226`).
- **R3. IPS V5 top-up order.** If the cost exceeds $300,000, the 2028 deposit completes the ladder first; "Its remainder buys the floor"; the balance goes to VT (`tna_fact_kits_v2.md:213`). "The 2027 deposit alone is sized" is true only through this rule (`:239-241`).
- **R4. The 2031 bottom** = (R − $3,700) rounded down to $5k. That is $145k (option 1) or $135k (3r) only while the 1 Jan cost is under about $301,300. "Freeze the rule, not the dollars" (`numbers_refresh.md:143`; `fr_prep_v2.md:265`).
- **R5. Final Report:** one valuation date, the 6 Nov close; no mixing of closes; one named basis per quantity; Laura's projections do not move after the 6 Nov re-price (`fr_prep_v2.md` §4.1 items 1-7).
- **R6. WInS gains or losses are never added to Laura's projections** (case:132-133; Guide:70-72). The team is not judged on whether the portfolio makes money (Guide:74-79).
- **R7. If maturity sizing is adopted on 27 Oct:** stop quoting the payment-date cost and "her first $300,000 is enough"; the IPS and Final Report carry the correction (`reconcile_3r.md:308-311`).
- **R8. Judging:** "Evaluators will consider the three deliverables together" (case:161). A TNA or IPS statement that a later market move makes false must be reconciled in the Final Report.
- **Timing fact.** The IPS goes in at 09:00 Sydney on Sat 7 Nov, one hour after the freeze close. The 6 Nov treasury.gov row probably posts after that (`attribution_pack.md §0 item 5; §7 timing table`, UNVERIFIED). **The IPS can never reflect the 6 Nov close.** The latest curve it can see is 5 Nov. So every IPS requirement below must hold in **all** bands.

### 4.1 Ladder cost at the 6 Nov close (basis D; the M2 odds apply if maturity sizing is adopted)

| If on 6 Nov the cost is... | Odds at 6 Nov: D / M2 | IBTR note (R2) | IPS (already submitted; must hold in every band) | The Final Report must... | 2031 bottom on that day: option 1 / 3r |
|---|---|---|---|---|---|
| **A1: ≤ $295,000** | 32-37% / 15-24% | The condition is not met at the valuation date. The first sentence is dated 6 Oct and stays true | The principle holds. Check that no IPS line implies the ladder is already bought or secured | State the 6 Nov cost once, with its date and basis (R5). Still give the odds that the top-up rule triggers by January (§2f: about 10-32% for 6 Nov costs of $290-295k). Not call the payments "locked" or "secured": the purchase is in January, after the report | $145k / $135k, quoted as the rule's output on 6 Nov, with the distance to the next $5k step |
| **A2: $295,000-300,000** | 29-40% / 27-36% | Not met. The room is under 0.17 points (D) | Holds, provided "covered" or "sized" statements carry the top-up clause (R3) | Do all of A1. Give the room in dollars and in yield terms on the named basis. Give the 1 Jan odds (26-50% across this band, §2f). Name the top-up rule as the safeguard | $145k / $135k. Say the 1 Jan odds of losing a step: 21-45% |
| **A3: $300,000-301,300** | 7-9% / 8-10% | The condition is met at the valuation date on the note's basis (D) | Holds only if it contains the top-up order (R3) and gives no fixed dollar bottom. "First deposit alone" without the clause would be false | State that the note's trigger was reached at the valuation date and that R3 applies. State the top-up size (≤ $1.3k) and who absorbs it, on the **same reading** as the IPS and the IBTM and VT reflections (`tna_fact_kits_v2.md:210-221`). State that the bottom is one small move from the next step (1 Jan odds 43-50%) | $145k / $135k, on the edge |
| **A4: $301,300-306,300** | 16-18% / 24-30% | Met | Holds only if it stated the bottom as a rule, not "$145,000" | State the bottom produced by the rule on 6 Nov ($140k / $130k) and explain the $5k step. Correct, explicitly, any $145k / $135k quoted as fixed in the TNA, IPS or a filed note (R8). Show the top-up ($1.3-6.3k) and how much the floor fell. Show that the payments are still fully covered through the 2028 deposit (case:91-92) | $140k / $130k |
| **A5: > $306,300** | 3-9% / 9-17% | Met, by a wide margin | As A4 | Do all of A4. Show the larger top-up (> $6.3k) and the knock-on to the 2031 range and to the confidence statement (case:116-120). Re-check that the cover chain still protects the payments (case:120). State that the risk landed where the plan says it lands (facility, not payments) | ≤ $135k / ≤ $125k |

**Rows that apply in every band:**
- **TNA (submitted 23 Oct, before any of this):**
  - No level (R1).
  - No undated "not crossed" or "enough". The cost touches $300k by 6 Nov in 46-58% (D) and 83-84% (M2) of paths.
  - The IBTR reflection must stay true in A1-A5 (R8).
- **If maturity sizing is adopted (27 Oct):**
  - Every band above is read on M2, where ending over is a coin flip.
  - "Her first $300,000 is enough" may not be repeated in the IPS or Final Report (R7).
  - The Final Report must carry the correction of the filed note's figure, with its basis.
- **The 1 Jan purchase happens after the Final Report** (deadline Sat 5 Dec 09:00 Sydney). The report may not present the January cost or the bottom as known. It must state the rule plus the 6 Nov illustration and odds (§2f).
- **Fees:** the D and M1 bases leave out the 0.07% iBond fee (about $1.4k on the ladder; `fr_prep_v2.md` §4.1 item 4). M2 includes it. The report must name the basis, so the reader knows which applies.

### 4.2 WInS book at the 6 Nov close

| If on 6 Nov the book is... | Odds (E26 to P100) | The Final Report must... |
|---|---|---|
| **B1: ≥ $303,400** (above 19 Oct) | 55-58% | Attribute the gain (mainly yields, plus carry of about $0.7k). Pair it with the fact that the same move made Laura's January ladder dearer (correlation 0.97; R6). Use the liability or policy benchmark, not the S&P (`attribution_pack.md §6`). Never call the gain good news for Laura |
| **B2: $300,000-303,400** | 24-29% | As B1. State that carry is part of the change |
| **B3: < $300,000** | 13-21% | Attribute the loss (rising yields on a book that is about 90% Treasuries, and/or VT). State that the same move made Laura's purchase cheaper, so the room grew. State that WInS is not the scorecard (Guide:70-79). Show no trade to "recover": the plan is hold, and trading is frozen |
| **Screen differs from the model** (3c) | Likely | Record the WInS value with its date, its source (screen or model) and its accrued basis. Record whether the distribution has been credited (−$601), the May-2038 schedule (−$225) and the open-price bond marks. Fix none of these by trading |

### 4.3 Scheduled events and the rules

| Event | Requirement |
|---|---|
| Jobs report Fri 6 Nov, 8:30 ET (Sat 7 Nov 00:30 Sydney), before the freeze close | Do not finalise IPS numbers from the 6 Nov session. The IPS states rules only (R1) |
| FOMC 28 Oct (statement time UNVERIFIED) | The Final Report must not explain WInS or ladder moves by "the Fed" unless the move is dated and checked against the curve |
| 6 Nov treasury.gov row (expected Sat 7 Nov about 09:30-10:00 Sydney, UNVERIFIED) | Run the Final Report re-price only once the row exists (`fr_prep_v2.md` §4.1 item 1) |
| Jobs report Fri 4 Dec, 8:30 ET (Sat 5 Dec 00:30 Sydney) | No Final Report number may depend on 4 Dec prices. R5 already fixes the valuation date at 6 Nov |
| FOMC 8-9 Dec, CPI 10 Dec (after the deadline, before 1 Jan) | The report cannot know the January cost. See §4.1 "every band" |

---

## 5. US events that could move yields, to 6 Nov, to 4 Dec and to 31 Dec

**Sydney times:** Sydney is UTC+11 throughout. US clocks go back on **Sun 1 Nov 2026**, so ET → Sydney is +15 hours until 31 Oct and **+16 hours from 1 Nov** (`attribution_pack.md §0 item 5; §8e`).

**FRED release times:** FRED lists releases at "7:30 am". BLS and BEA release at 8:30 am ET, so FRED appears to show US Central time (my inference, UNVERIFIED).

**Fetch window:** all pages were fetched 19 Oct 2026, 23:20-23:35 UTC, with plain curl (`FWD/web/`).

### 5a. To the 6 Nov freeze

| Date (ET) | Sydney | Event | Source (URL, read 19 Oct 2026) |
|---|---|---|---|
| Wed 21 Oct, 1:00 pm | Thu 22 Oct 04:00 | 20-year bond auction (reopening, $13bn) | TreasuryDirect upcoming auctions JSON, `https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json` (competitive close 01:00 PM) |
| Thu 22 Oct | Fri 23 Oct | 5-year TIPS auction; weekly jobless claims (8:30) | Treasury tentative auction schedule, `https://home.treasury.gov/system/files/221/TentativeAuctionScheduleQ32026.xml`; FRED claims calendar, `https://fred.stlouisfed.org/releases/calendar?rid=180&y=2026` |
| Fri 23 Oct, 5:00 pm | Sat 24 Oct 08:00 | **TNA deadline** | PREAMBLE |
| Mon 26 / Tue 27 / Wed 28 / Thu 29 Oct | +1 day 04:00 | 2-year, 5-year, 2-year FRN and 7-year auctions (announced 22 Oct) | Tentative auction schedule XML |
| Tue 27 - **Wed 28 Oct** | Thu 29 Oct (about 05:00 if the usual 2:00 pm statement; time UNVERIFIED) | **FOMC meeting** (no projections; the next SEP is December) | `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm` ("October 27-28"; "December 8-9*"; "* Meeting associated with a Summary of Economic Projections") |
| **Thu 29 Oct, 8:30 am** | Thu 29 Oct 23:30 | **GDP Q3 advance estimate, and Personal Income and Outlays for September (PCE)** | BEA, `https://www.bea.gov/news/schedule` |
| Sun 1 Nov | | US clocks go back | — |
| Mon 2 Nov (3:00 pm in Aug; Nov time UNVERIFIED) | Tue 3 Nov (about 07:00) | **Treasury financing estimates** (quarterly refunding, part 1). iBond ex-date the same day | `https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/most-recent-quarterly-refunding-documents` ("The next release is scheduled for November 2, 2026") |
| **Tue 3 Nov** | Wed 4 Nov (results through the Sydney day) | **US midterm elections.** JOLTS (September), 10:00 am ET | 2 U.S.C. §7, "The Tuesday next after the 1st Monday in November, in every even numbered year" (`https://www.law.cornell.edu/uscode/text/2/7`); 3 Nov 2026 is my calendar computation. FRED JOLTS calendar, rid=192 |
| **Wed 4 Nov** (8:30 am in Aug; Nov time UNVERIFIED) | Thu 5 Nov (about 00:30) | **Quarterly refunding statement** (sizes of the 3/10/30-year auctions). BEA trade balance (8:30) | Treasury page above ("The next release is scheduled for November 4, 2026"); BEA schedule |
| Thu 5 Nov | Fri 6 Nov | iBond distribution paid; jobless claims | `attribution_pack.md §1 Distributions row`; FRED rid=180 |
| **Fri 6 Nov, 8:30 am** | **Sat 7 Nov 00:30** | **Employment Situation (October)** | FRED, `https://fred.stlouisfed.org/releases/calendar?rid=50&y=2026` ("Friday November 06, 2026"). The BLS page itself returned **403** to curl (`https://www.bls.gov/schedule/news_release/empsit.htm`): BLS-direct confirmation UNVERIFIED |
| Fri 6 Nov, 4:00 pm / 5:00 pm | Sat 7 Nov 08:00 / 09:00 | **Freeze close / IPS deadline** | PREAMBLE; `attribution_pack.md §7 timing table` |

### 5b. 7 Nov to the 4 Dec Final Report deadline (moves WInS tracking and the odds, not the 6 Nov valuation)

| Date (ET) | Event | Source |
|---|---|---|
| Mon 9 / Tue 10 / Thu 12 Nov | **Refunding auctions: 3-year / 10-year / 30-year** | Tentative auction schedule XML |
| **Tue 10 Nov, 8:30 am** (Wed 11 Nov 00:30 Sydney) | **CPI (October)** | FRED, `https://fred.stlouisfed.org/releases/calendar?rid=10&y=2026` ("Tuesday November 10, 2026"); BLS page 403 (`https://www.bls.gov/schedule/news_release/cpi.htm`) |
| Wed 11 Nov | Veterans Day: bond market closed, stocks open, no treasury.gov curve | SIFMA |
| Fri 13 Nov | PPI (October) | FRED rid=46 |
| Mon 16 Nov | T-bond coupons ($1,538.75; 15 Nov is a Sunday) | `attribution_pack.md §7 timing table` |
| Tue 17 Nov | Retail sales (October) | FRED rid=9 |
| Wed 18 Nov | 20-year auction. **FOMC minutes of 27-28 Oct**: computed from the Fed's "released three weeks after the date of the policy decision", not yet listed | Auction XML; Fed calendar page |
| Thu 19 Nov | 10-year TIPS reopening auction | Auction XML |
| Mon 23 - Wed 25 Nov | 2-year, 5-year, 7-year and 2-year FRN auctions | Auction XML |
| **Wed 25 Nov, 8:30 am** | **GDP Q3 second estimate; Personal Income and Outlays for October (PCE)** | BEA schedule |
| Thu 26 Nov / Fri 27 Nov | Thanksgiving closed / bond market early close 2:00 pm | SIFMA |
| Tue 1 Dec | JOLTS (October); iBond ex-date | FRED rid=192; `attribution_pack.md §7 timing table` |
| **Fri 4 Dec, 8:30 am** (Sat 5 Dec 00:30 Sydney) | **Employment Situation (November)**; iBond distribution paid; **Final Report deadline 5:00 pm** (Sat 5 Dec 09:00 Sydney) | FRED rid=50 ("Friday December 04, 2026"); PREAMBLE |

### 5c. After the deadline, before the 1 Jan purchase
- **FOMC 8-9 Dec** (with projections).
- **CPI Thu 10 Dec.**
- PPI Tue 15 Dec; retail sales Wed 16 Dec.
- GDP third estimate and PCE for November, Wed 23 Dec.
- Bond market early closes on 24 and 31 Dec; closed 25 Dec and 1 Jan.
- Sources: Fed calendar, FRED rid=10/46/9, BEA, SIFMA.

### 5d. How much bigger are event days? (Jan 2025 - 19 Oct 2026, 449 days; `FWD/scripts/events_vol.py`, `FWD/data/events_vol_out.txt`)

Each day's whole-curve change was applied to the 19 Oct curve and basis D repriced.

| Day type | n | SD of the D move | Mean absolute move | Largest | 10y SD | × ordinary day |
|---|---|---|---|---|---|---|
| No scheduled CPI, jobs or FOMC | 393 | $1,336 | $1,064 | $4,265 | 4.6bp | 1.00 |
| Jobs report | 21 | $1,686 | $1,391 | $3,864 | 6.0bp | **1.26** |
| CPI | 21 | $1,480 | $1,199 | $3,594 | 5.0bp | 1.11 |
| FOMC decision | 14 | $1,219 | $1,112 | $2,438 | 4.4bp | 0.91 |

- **What the window contains.** The 20 Oct-6 Nov window holds one FOMC and one jobs day. With event days at their own SD, the 14-day SD is $5,074, against $5,080 if all days are average. **The event mix does not widen the freeze distribution.**
- **The ten largest one-day moves** were: 7 Apr 2025 (−$4,265); 23 Sep 2026; 20 Mar 2026; 1 Aug 2025 (jobs); 3 Apr 2025; 15 May 2026; 15 Jan 2025 (CPI); 8 Apr 2025; 10 Sep 2026; 28 Mar 2025. **8 of the 10 had no scheduled release.**
- **Limits:** small samples, 2025-26 only. FRED returned the 2025 calendar for the 2023/2024 requests, so earlier years were not tested.

---

## 6. Verification ("verify twice")

| Check | Result |
|---|---|
| Reproduction of levels, own pricer (`fwd_lib.py`, written from scratch) | D $297,162 (linear zero) = numbers desk; D $297,158 (log-DF) = the indep_pricer figure; M1 $298,446 = coupon study exactly; M2 $299,861 = engY exactly. DV01 $289 / $288 / $290 per bp |
| Second implementation for M2 | engY's own `rung_terms` (read-only import): $299,861 at 0, $307,148 at −25bp, $292,768 at +25bp. Mine: $299,861 / $307.2k / $292.7k |
| One bug of mine found and fixed during checking | My coupon-date generator lost the principal for holdings maturing on the 29th-31st (IBTQ, IBTR). It was found because M2 was $548 off engY; fixed (`fwd_lib.py` `coupon_dates`, `k == 0` → maturity date) |
| Two seeds (20261020 and 7; 20,000 paths each) | Every probability within 1.0 point, every quantile within about $150 (`tables_out.md` brackets) |
| Monte Carlo against closed-form (parallel methods) | D at 6 Nov σ 0.71: MC 27.7% / 27.9% against analytic 27.9%; 1 Jan σ 1.0: 41.3% / 41.0% against 41.3%; quantiles within $100 |
| Against earlier waves | D 1 Jan odds 37.9% (σ 0.71) and 41.3% (σ 1.0) against 37.9% / 41.4% (`numbers_refresh.md:99`). D over at the 20 or 21 Oct close 6.1-16.0% against 6.5-15.6% (verifier E4). M2 49-50% against REC "50%". Bottom survival 63-68% against 61-72% (different horizon) |
| Book: simulation against analytic normal | σ 0.71: SD $3,786; p5/p95 $297.9k / $310.3k analytic against $298.0k / $310.4k simulated. σ 1.0: $295.8k / $312.4k against $295.9k / $312.6k. IBTM SD $827 analytic against $826 simulated. Distribution $600.81 against the pack's $600.95 (rounding of the per-share amounts) |
| Calendar counts | Bond days computed in code with the SIFMA holidays, and matched by hand: 14 to 6 Nov, 50 to 31 Dec |

---

## 7. Limits and UNVERIFIED
- **The models.**
  - The rate models are random walks with no drift. The yield shape is fixed in the P methods and taken from history in the E methods. There is no regime change and no jump model beyond what is in the 2023-26 data.
  - E23 (0.92-point 10-year volatility) includes the volatile 2023, so it is the "rougher market" case.
- **"Yields unchanged" bases (D, M1, M2)** take no credit for roll-down or forward drift. The forward bases (A, C) sit lower; see `numbers_refresh.md:57-67`.
- **WInS book.**
  - The T-bond prices are MODEL.
  - The iBond funds use a duration approximation with fund-level convexity guessed as D(D+0.5); the effect is under $20.
  - VT has zero drift over 14 days; the 7% expected return would add about $70-90.
  - Not modelled: how WInS treats the distribution, accrued interest, the May-2038 schedule, and the timing of bond marks (all UNVERIFIED; §3c).
- **Event times.** The FOMC statement time, the refunding release times in November and the treasury.gov posting time are UNVERIFIED. The BLS calendars could not be read directly (HTTP 403); the dates come from the St. Louis Fed's FRED release calendar.
- **20 Oct close not yet published** at the fetch. Any one-day move of about $1.3-1.6k changes the 19 Oct starting point. **Re-run on the 20 Oct curve before relying on any odds:** `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I FWD/scripts/forward_sim.py SEED 20000 FWD/data/out` after replacing `FWD/raw/tsy/tsy_2026.csv` and changing `D0` in `forward_sim.py`. It runs in about 5 minutes per seed.

## 8. What this teaches (plain English)
- **"Will it end above the line?" and "will it touch the line?" are different questions.** A price sitting just under a line touches it far more often than it ends above it. Write sentences that stay true either way.
- **A rule with steps turns a small move into a big one.** A $1 change in January cost can move the announced bottom by $5,000. That is why the rule is stated, not the dollar figure.
- **Scheduled news is less dangerous than people think, and unscheduled news is more.** Jobs days are about a quarter more volatile. But most of the biggest days in the last two years had no release at all.
- **One trade-off appears in both books.** The same fall in yields makes the WInS book look good and makes Laura's real purchase more expensive.

## 9. Files (all under `FWD/`)
- `forward_view.md` (this file).
- **Scripts (`scripts/`):**
  - `fwd_lib.py`: curve, the three bases, T-bond pricing.
  - `forward_sim.py`: all distributions and the book.
  - `tables.py`: tables plus the analytic checks and the §2f conditional table.
  - `bands.py`, `events_vol.py`, `check_repro.py`, `check_engY_M2.py` (cross-check), `h2t.py` (HTML to text).
  - `dbg_m2.py` and `dbg_engY.py` (debug runs that found the coupon-date bug).
- **Outputs (`data/`):**
  - `fwd_seed20261020.json`, `fwd_seed7.json`, `tables_out.md`, `bands_out.txt`, `events_vol_out.txt`;
  - `run_seed*.log`, `fetch_times_utc.txt`;
  - `ladder_cost_2026_daily_A_D.csv` (copied from `oct20/numbers/data/`).
- **Raw (`raw/`):** `tsy/tsy_2022-2026.csv` (treasury.gov) and `px/yh_VT.json`, `yh_IBTM.json` (Yahoo).
- **Web (`web/`):**
  - `fomc.html/.txt`, `tsy_qr_recent.html/.txt`, `auction_q3.xml`, `td_upcoming.json`, `bea_sched.html/.txt`;
  - `fred_rel_{10,50,46,9,180,192}*.html/.txt`, `sifma.html/.txt`, `usc2_7.html/.txt`;
  - `bls_*.html` (the 403 responses, kept as evidence).
