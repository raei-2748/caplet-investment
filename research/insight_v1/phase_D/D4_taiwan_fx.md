# D4 - Taiwan, FX and geopolitics: what Laura's facility money will actually buy (question M095)

Agent D4, run insight_v1, 2026-09-27. AI brainstorming output for the team: specifications, evidence and numbers,
not submission-ready text. Status labels: VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED (SNIP),
ASSUMPTION (ASM), DERIVED (computed by the script from the labelled inputs).
Script: `research/insight_v1/scripts/D4_facility_purchasing_power.py` (run from the repo root; a full run on
2026-09-27 used live FRED copies and the live DGBAS construction-cost platform).

Terms used below:
- **NT$** = New Taiwan dollar. **US$** = U.S. dollar. "NT$ per US$" going **up** means the Taiwan dollar got weaker,
  so each US$ buys **more** in Taiwan.
- **CCI** = Taiwan's official construction cost index (DGBAS), 2021 = 100.
- **Drift** = the expected, one-directional change (costs usually rise). **Spread** = the two-sided uncertainty around
  it (measured by the standard deviation, "sd", or the 5th-95th percentile band, "p5/p95").
- **Building power** = how much building Laura's money buys = US$ amount x (NT$ per US$) / construction costs. In
  logarithms the three pieces simply add, so they can be compared side by side.

---

## Summary: top findings (ranked by impact on reaching the semifinals and on making the plan hers)

1. **The answer depends on when you stand. The team has been comparing a 6-year cost drift with a 2-year FX band.
   Fix the horizon and the ranking flips (DERIVED).**
   | Vantage | Market (US$ pool) | USD/TWD | Construction costs |
   |---|---|---|---|
   | Today -> 2033 (the Final Report's projection, 6.3 years) | **largest spread**: sd 0.16, p5/p95 -23%/+32% | sd 0.06 (since 2006) to 0.16 (since 1983) | **largest expected effect**: drift -11% to -20% building power; spread sd 0.11 |
   | 2031 -> 2033 (what Laura tells co-sponsors) | **smallest**: sd 0.027, -3.8%/+5.1% (80% locked) | **largest spread**: sd 0.068, -11.6%/+11.4% | drift -4% to -7%; spread sd 0.058 |
   - Variance shares (independent, ASM): 2026 view market 61% / FX 9% / construction 29%; **2031 view market 8% /
     FX 53% / construction 39%**.
   - So: by the time Laura speaks in 2031, her own portfolio is the *least* uncertain part of what the gift will buy.
     The locked floor did its job. What is left is the exchange rate and Taiwan building costs, which no US$ portfolio
     can remove.
2. **Construction inflation is a drift, not a coin toss: say it as an assumption, with a number (case p.4 L147,
   R-C85).** A fixed US$ amount buys about **11-12% less** building by January 2033 if Taiwan costs rise at CPI-like
   1.9%/yr or the 2008-2026 CCI average (2.11%/yr), and about **20% less** at the post-2021 pace (3.54%/yr). The 2026
   spike (+6.53% y/y) would mean -33% but should not be projected (F-509). This is the one assumption line the case
   explicitly asks for and that most teams will skip.
3. **The US$ range stays binding; any NT$ figure is "an illustration at a dated rate" with its own, wider band.**
   In the 2031 view the NT$ band is about **-11%/+13%**, roughly 2.5-3 times the US$ band (-3.8%/+5.1%). The
   bought US$ floor is certain in US$, but in NT$ it would have come in *below* its dated NT$ value in 51% of past
   2-year windows since 2006, by more than 10% in 7%. B6b's guess is confirmed.
4. **Don't lock NT$ in 2031; don't tilt to Taiwan (confirms the WInS ticket).** Locking NT$ two years ahead costs
   about **5.9%** at today's rate gap (Taiwan 2y 1.66% is SNIP), roughly one FX standard deviation, and it would have
   paid off in only 23% of past 2-year windows. Keeping US$ until contracts are signed also keeps her flexibility.
   Adding Taiwan stocks (EWT) is not a currency hedge worth having (S2 already dropped it).
5. **Two natural cushions and one reinforcer (DERIVED, small samples).** (a) The Taiwan dollar tends to weaken when
   U.S. stocks fall (monthly correlation -0.38, 10 years). So in NT$ terms a bad U.S. market is partly cushioned; the
   2026-view combined sd falls from 0.209 to 0.189. (b) The only real Taiwan Strait crisis in the data (1995-96 missile
   tests) moved NT$ per US$ by at most +4.4%, and the August 2022 drills by about 0%. Both are inside normal 2-year
   noise. (c) Reinforcer: years with a weaker NT$ have tended to be years of lower construction inflation (annual
   correlation -0.36, n=18). That widens the building-power band slightly. None of this covers a blockade or war,
   which is outside the data (ASM).

**Does M095 change the current strategy?** No change to the portfolio, the lock or the WInS ticket. It **adds** one
FR assumption line (building-cost drift), one FR currency rule (US$ binding, NT$ dated), a quantitative reason for
not converting to NT$ in 2031, and one possible FR chart. **Deadline tier 3 (Final Report, Dec 4).**

---

## M095. Which is largest for what the facility money buys by 2033: market risk, USD/TWD, or Taiwan construction inflation? Does any NT$ figure need its own band or an "illustration at a dated rate" label?

**Tier 3 (Final Report). Criterion served most: Client Knowledge and Objectives** (it tells her what her gift will
really buy where she is building it). Secondary: Creativity and Presentation (the case's own standard of
communicating "investment uncertainty clearly and credibly to prospective co-sponsors").

**Is the question well posed?** Partly. The skeptics were right about two things. (1) The horizons must match: the
original comparison put a 7-year cost drift next to 2-year FX and market bands (stats skeptic). (2) The *labelling*
half (US$ on every figure, NT$ dated) was already specified in BS-04 (answered skeptic). The new work here is the
**ranking on matched horizons, the size of the NT$ band, and the drift-vs-spread split**. None of this existed
before.

### One-sentence answer
Seen from today, U.S. market risk is the biggest *uncertainty* and Taiwan construction inflation is the biggest
*expected* loss of building power (about -11% to -20% by 2033). Seen from Laura's 2031 conversation, the locked floor
has made the market the smallest factor, and the exchange rate (sd ~7%) and building costs dominate. So the range is
quoted in US$ as binding, with one purchasing-power assumption line, and any NT$ figure is labelled an illustration at
a dated rate, with a band about 2.5-3 times as wide.

### Evidence
| # | Claim | Source (access 2026-09-27) | Status |
|---|---|---|---|
| E1 | Case requires assumptions on "the effect of inflation on portfolio projections and facility costs" | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` L146-148 (R-C85) | VRF |
| E2 | Teams "are not expected to estimate that cost" | same file L164 (R-C95) | VRF |
| E3 | "Teams must recommend the dollar range Laura should communicate"; no currency named anywhere | same file L117; R-AN10 | VRF |
| E4 | Residency is "in Taiwan" | same file L77 | VRF |
| E5 | 2033 facility pool (lock-early, 60% equity sleeve, 80% floor): p5/p50/p95 $159k/$207k/$273k | `research/verified_2026-09-27/strategy_mc.py` re-run | VRF model; lognormal returns ASM |
| E6 | 2031 view at the median 2031 sleeve ($187.6k): 2033 p5/p50/p95 $199.0k/$206.9k/$217.4k (-3.8%/+5.1%) | D4 script, B6b method | DERIVED (ASM: 2y yield 4.81% in 2031) |
| E7 | USD/TWD 31.82 on 2026-09-18; daily series from 1983 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXTAUS | VP (F-510) |
| E8 | 2-year moves since 2006: p5/p50/p95 -11.6%/-0.2%/+11.4%, sd 0.068; 6.3-year since 2006 -11.6%/-0.4%/+6.9%, sd 0.064; since 1983: 2y -17.5%/+14.5% (sd 0.096), 6.3y -31.7%/+28.4% (sd 0.165) | D4 script on E7 (monthly, overlapping windows) | DERIVED from VP |
| E9 | CCI total reconstructed 2008-01 to 2026-08 (fit error <= 0.16 pts); latest 119.51; CAGR 2008-2026 2.11%/yr; since 2021 base 3.54%/yr; 2026 y/y +6.53% | DGBAS CCI platform https://www.stat.gov.tw/CCI/CCI_Site/CCIPrice/PartialPriceClassesList.aspx via D4 + A2 scripts | VP inputs, derived total (F-508 extended back to 2008) |
| E10 | CCI calendar-year growth: 2009 -9.0%, 2015 -2.9%, 2021 +10.9%, 2022 +7.4%, 2024 +2.0%, 2025 +0.8%, 2026 (Jan-Aug avg) +4.4% | D4 script | DERIVED from VP |
| E11 | CCI 2-year moves p5/p95 -5.0%/+16.4% (sd 0.058); 6.3-year -0.6%/+32.9% (median +6.1%, mean +13.7%, sd 0.113) | D4 script | DERIVED; only 18 years of data, so the 6.3y spread rests on ~3 independent periods |
| E12 | Taiwan CPI forecasts 2027: 1.90% (DGBAS), 1.83% (CBC) | F-504, F-505 (eng.stat.gov.tw; cbc.gov.tw) | VP (Phase A) |
| E13 | corr(monthly NT$-per-US$ change, S&P 500 return) = -0.38 (120 months to Sep 2026); annual -0.60 (n=10); a -10% S&P month ~ +1.4% NT$ per US$ | FRED SP500 https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500 + E7 | DERIVED from VP; FRED holds only 10 years of SP500 |
| E14 | Annual corr(CCI growth, NT$-per-US$ change) = -0.36 (2009-2026, n=18) | D4 script | DERIVED; weak evidence (small n) |
| E15 | Third Taiwan Strait Crisis 21 July 1995 - 23 March 1996 | https://en.wikipedia.org/wiki/Third_Taiwan_Strait_Crisis | SNIP (secondary source, read directly) |
| E16 | NT$ per US$ 26.38 before the crisis, peak 27.55 (+4.4%), 27.31 at its end (+3.5%); Aug 2022 drills ~0.0% | D4 script on E7 | DERIVED from VP; Aug 2022 dates (4-10 Aug) general knowledge, UNVERIFIED |
| E17 | Taiwan 2-year government yield 1.66% (2026-08-10) | search snippet citing https://en.macromicro.me/charts/14586/taiwan-2-year-government-bond-yield | SNIP (page is script-rendered; not read) |
| E18 | U.S. 2y par 4.81% (2026-09-25) | `competition/official_market_data/` curve CSV | VRF |
| E19 | BS-04: "US$" on every figure, NT$ reference with date and rate, one line on which currency is binding | `research/insight_v1/phase_A/stakeholder_map.md` L629-634 | repo (Phase A) |
| E20 | WInS ticket already drops EWT (Taiwan tilt = AI bet + tokenism; $3.3k Taiwan exposure via VT) | `research/insight_v1/wins_now/S2_growth_sleeve.md` L43-48, L206-235 | repo |

### Numbers and where they come from
**A. Building power of a fixed US$ in January 2033 (FX unchanged), from Aug 2026 costs (DERIVED from E9/E12):**
| Cost path (ASM choice) | Cost rise to Jan 2033 | Building a fixed US$ buys |
|---|---|---|
| Taiwan CPI forecast 1.9%/yr | +13% | **-11%** |
| CCI 2008-2026 average 2.11%/yr | +14% | **-12%** |
| CCI since 2021 base 3.54%/yr | +25% | **-20%** |
| 2026 spike 6.53%/yr (do not project; F-509) | +49% | -33% |
Suggested base: **about 2-3.5%/yr, i.e. a fixed US$ buys roughly 12-20% less building by 2033** (ASM: the
18-year average and the post-2021 pace bracket it; CPI alone understates because wages rose 8.1% y/y, F-508).

**B. Spread on matched horizons (log sd; 90% bands ~ +/-1.645 sd; DERIVED):**
| | 2026 -> 2033 | 2031 -> 2033 |
|---|---|---|
| Market (US$ pool) | 0.164 | 0.027 |
| FX, since 2006 | 0.064 | 0.068 |
| FX, since 1983 | 0.165 | 0.096 |
| FX, square-root-of-time from 10y daily vol 4.69% | 0.118 | 0.066 |
| Construction (CCI), since 2008 | 0.113 | 0.058 |
| Combined (independent, FX since 2006) | 0.209 (~-29%/+41%) | 0.094 (~-14%/+17%) |
| Combined with FX-equity corr -0.38 | 0.189 | 0.086 |
Caveat (stats skeptic, F-513): the FX answer depends heavily on the period. Since 2006 the 6-year spread is small
(the central bank has smoothed the rate); since 1983 it includes the 1980s appreciation from ~40 to ~25 NT$ per US$
and is as large as the market spread. **State which period you use.** The 2031-view ranking (FX >= construction >
market) holds under every FX period.

**C. NT$ illustration at the dated rate 31.82 (2026-09-18), FX only (DERIVED):**
- Median 2033 pool US$207k = NT$6.60m; 2-year FX p5/p95 -> NT$5.83m / NT$7.35m.
- Median-state 2031 floor US$165k = NT$5.25m; 2-year FX p5/p95 -> NT$4.64m / NT$5.85m.
- 2031-view NT$ band (market x historical 2-year FX, bootstrapped, independent): **-11.4%/+12.7%**, vs US$
  **-3.8%/+5.1%**.
- The bought US$ floor, restated in NT$, came in below its 2031 NT$ value in 51% of past 2-year windows (since
  2006), by >5% in 27%, by >10% in 7%.

**D. Cost of locking NT$ in 2031 (covered interest parity, ASM; E17 is SNIP):** ((1.0166/1.0481)^2 - 1) = **-5.9%**
fewer NT$ than spot. The realised median 2-year move since 2006 was -0.2%, and NT$ strengthened by more than 5.9% in
only 23% of windows. Locking costs about one FX sd for protection that would rarely have been needed. If the rate gap
narrows by 2031, the cost falls. Re-check then.

### Implications (decision / number / sentence) and deliverable
1. **FR, assumptions section: sentence (number).** A strong assumption line must contain: (a) the facility is paid
   in NT$ and Laura's contribution is in US$; (b) a named cost-growth assumption for Taiwan construction (the team's
   choice in the ~2-3.5%/yr band, citing DGBAS CCI with its date) and **why not CPI** (wages +8.1% y/y; costs ran
   ~3.5%/yr since 2021 but ~2.1%/yr since 2008); (c) what it means: a fixed US$ amount buys roughly 12-20% less
   building by 2033; (d) that the team is **not** estimating the facility cost (case L164). No budget, no cost
   figure.
2. **FR, 2031 range / co-sponsor element: decision.** US$ is the binding currency. Any NT$ figure carries "at
   NT$31.82 per US$ on 18 Sep 2026 (FRED); illustrative only" and, if an NT$ band is shown, it is the wider one
   (~+/-12% in the 2031 view). A strong sentence must say *which* currency is binding and *why the NT$ number moves
   more* (the exchange rate, not her portfolio). Fits the message order already specified for M008 (floor bought,
   conditional stretch, invitation to co-fund).
3. **FR, uncertainty explanation: sentence.** The case asks how "favorable and unfavorable market outcomes" affect
   the amount (L117-118 area). Worth one line: by 2031 the market part is mostly settled (+/-4-5%). What still moves
   the *building* her gift pays for is the exchange rate and Taiwan costs, and co-sponsors budgeting in NT$ face the
   same two. This is honest and specific to her project; a generic team will not have it.
4. **FR, flexibility rationale: sentence.** Keeping the post-floor leftover in US$ until construction contracts are
   signed (no NT$ lock in 2031) costs nothing now, avoids ~5.9% forward cost, and keeps her able to re-scope if costs
   or the project change. This supports the "flexibility as the project develops" reading (case p.3; brief section 7).
5. **FR, optional chart (Creativity and Presentation; the IPS bans charts).** "What moves the building her gift buys,"
   two small grouped bars (2026 view vs 2031 view): market / FX / construction spread (sd) plus a separate marker
   for the construction drift. Data: table B plus table A. One chart, no more.
6. **IPS: none directly** (the IPS guide says the final range and projections are not expected). At most a clause
   in the 500 words that the promise and range are in US$. **TN: none. WInS-now: none** (the EWT drop stands).
7. **Operating payments (adjacent, for the SH-12 erosion owner):** the same logic applies to the fixed $50k a year
   in NT$ terms. Wages (+8.1% y/y) matter more than construction for a residency's running costs. Route to whoever
   owns the erosion sentence; not re-worked here.

### Taiwan Strait contingency (scope note)
- The case puts Taiwan legal and regulatory issues out of scope (case L169, VRF). A geopolitical blockade or conflict
  is outside every historical series used here (ASM). It would threaten the *project*, not the US$ Treasury ladder
  that funds the ten payments.
- Plan consequences already in place: payments in US Treasuries (US-held); no Taiwan tilt (E20); leftover held as US$
  flexibility (implication 4). Nothing more is needed, and anything more would dress up a tail event as a forecast.
  One clause in the FR flexibility rationale is enough.
- Historical check (E16): the 1995-96 crisis moved the currency by at most +4.4%, within normal 2-year noise.
  UNVERIFIED general knowledge: the central bank intervened to stabilise it. Do not present this as evidence about a
  future crisis.

### Confidence
- Ranking by vantage point: **high** (robust to FX period and to the CCI growth choice).
- Size of the construction drift (-11% to -20%): **medium** (18 years of CCI; the regime choice matters).
- NT$ band (~+/-12% in 2031): **medium-high** since 2006; wider if the pre-2006 history is used.
- Hedge cost 5.9%: **low-medium** (Taiwan 2y yield is SNIP; the rate gap may change by 2031).
- Correlations: **low** (short samples).

**Changes current strategy?** No (adds FR content only). **Criterion:** Client Knowledge and Objectives (secondary:
Creativity and Presentation; Portfolio Analysis for the matched-horizon method).

**What this teaches (one line):** compare risks over the same time span, and keep "what we expect to happen" (drift)
separate from "how wrong we might be" (spread). A risk that is certain to erode value belongs in the assumptions, not
the error band.

---

## Sources (all accessed 2026-09-27)
| Source | URL / path | Status |
|---|---|---|
| Official case | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L77, L117, L146-148, L164, L169) | VRF |
| Verified MC model | `research/verified_2026-09-27/strategy_mc.py` | VRF (model inputs JPM LTCMA; ASM lognormal) |
| FRED DEXTAUS (Fed H.10 NT$ per US$) | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXTAUS | VP |
| FRED SP500 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500 | VP |
| DGBAS construction cost index platform | https://www.stat.gov.tw/CCI/CCI_Site/CCIPrice/PartialPriceClassesList.aspx | VP inputs; total derived |
| DGBAS / CBC CPI forecasts | F-504, F-505 in `research/insight_v1/phase_A/fact_register.md` | VP (Phase A) |
| Third Taiwan Strait Crisis dates | https://en.wikipedia.org/wiki/Third_Taiwan_Strait_Crisis | SNIP (secondary) |
| Taiwan 2y yield 1.66% (2026-08-10) | https://en.macromicro.me/charts/14586/taiwan-2-year-government-bond-yield (via search snippet) | SNIP |
| Phase A/B/C files | `research/insight_v1/phase_A/{fact_register,stakeholder_map,case_register}.md`; `phase_B/B6b_cosponsors.md` (Q3, Q5); `phase_C/survivors.json` (M095) | repo |
| WInS growth sleeve (EWT drop) | `research/insight_v1/wins_now/S2_growth_sleeve.md` | repo |
| Script | `research/insight_v1/scripts/D4_facility_purchasing_power.py` (reuses `A2_taiwan_cci.query`) | this run |

Blocked or not read: DGBAS attachment files on ws.dgbas.gov.tw (TLS failure, Phase A); Taipei Exchange / MacroMicro
yield pages (script-rendered, no data in the page text).

## What this teaches
- Laura's gift is decided in US dollars but spent in Taiwan dollars on Taiwan building costs. Three different things
  can shrink it, and they matter at different times: markets before 2031, the exchange rate and building costs after.
- Locking the floor in 2031 turns the biggest uncertainty (markets) into the smallest. That is what "protecting the
  commitment" looks like in numbers.
- Some risks are predictable drifts (costs usually rise). You state them as assumptions. Others are genuine unknowns
  (currencies). You state them as ranges and label the date and rate you used.
- A hedge has a price: locking NT$ early costs about 6% today, roughly the size of the risk it removes. Sometimes the
  right decision is to disclose the risk rather than pay to remove it.
