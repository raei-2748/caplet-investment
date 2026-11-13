# Q10c research cards: Taiwan building costs, seismic codes, and where a small residency's building risk sits

Sat 14 Nov 2026, Sydney. Report parts: 3b (her flexibility and its three uses), 3d (the contribution described), 3e
(assumption area 4, inflation and Taiwan building costs; the "money, not the site" clause) and Table 3 row 7 ("Her
flexibility's three uses"). These are notes for the Final Report store, not report prose.

**Checked against:**
- Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.15, frozen: half the shares' value "promised to
  no one ... for building costs that overrun, a stronger Taiwan dollar or a co-sponsor falling short").
- The Trading Notes, through CANON C15: "nonexistent inflation risk" is about the payments, and it holds.
- `CANON.md`: A31 (three uses named; no contingency fund sized, case l.106-107; no facility cost estimated) and C15.
- `NUMBERS.md`, sections 4 and 8d. Every plan figure here is quoted from there and is MODEL.
- `numbers/inflation_inputs.json` (the Taiwan construction block).
- `exhibits/tables.md`, Table 3 row 7.
- `SKELETON.md`, rows 3b, 3d and 3e.
- The cards this one builds on, cited rather than repeated:
  - Q10, rows 15-22: CPI and the September 2026 index, its two headline splits, and the 5-, 10- and 25-year rates.
  - Q9, rows 24-27: Flyvbjerg's building overruns and the Taichung theatre.
  - Q9b, row 3: Yaddo's buildings at 22.9% of expenses.
  - Q9c, rows 22-31: the residencies that lost their sites.
  - The store's INFLATION_TWD and RESIDENCY rows: Set in Stone, Weiwuying, the Taipei Performing Arts Center, the PCC
    cost manual (Q5-022, Q5-023), and the Legislative Yuan's 64.71% of plans revised (Q24-032).

**Scope.** The case puts facility cost estimates, taxes and Taiwan legal questions out of scope. This card reports
rates, percentages and code facts. It never gives a cost for Laura's building and never gives legal advice. Building
costs quoted for other buildings describe those buildings only.

**The plan is frozen.** A "risk" in the Clash column is a risk to record, never a change to propose.

**Claims tested**
1. Keep, kill or change: "Taiwan building costs over 2027-2033 are best read from the DGBAS construction cost index's
   long record (about 3% a year), and the 2026 spike (+7.29% on a year) is a cycle, not a new trend."
2. Keep, kill or change: "Seismic code changes after the 1999 Chi-Chi earthquake and the April 2024 Hualien earthquake
   raise what it costs to build or renovate a small cultural building in Taiwan, which is a reason an owner keeps
   flexibility."
3. Keep, kill or change: "Construction risk for a small residency comes mostly from the site and the building's age,
   not from the national cost index."

**The problem and the fields that answer it.** The problem is cost escalation on a small building project over six or
seven years, plus regulatory risk on an older building turned to public use. Four fields answer it:
- **Construction economics and cost engineering.** How a price index is built and weighted, how escalation clauses
  work, and reference-class forecasting.
- **Seismic engineering and building regulation.** Design codes for new buildings; evaluation and retrofit of
  existing ones.
- **Heritage conservation practice.** The risk of hidden conditions when an old building is repaired.
- **Public audit.** The Legislative Yuan Budget Center's reviews of real projects.

Taiwan's own practitioners hold the primary record:
- DGBAS: the index.
- The PCC: price adjustment.
- NCREE: the design code.
- The MOI National Land Management Agency: the codes and the retrofit programmes.
- The Legislative Yuan Budget Center: audits.

US practice (NIBS, FEMA, NIST, MIT 1976) gives the cost-share evidence Taiwan has not published.

## Verdicts in one screen

1. **Claim 1: CHANGE.** About 3% a year is still the right central rate (2000-2025: 3.0% a year on DGBAS yearly
   averages, Keel arithmetic; Q10 row 20 has 3.19% to September 2026). Three parts of the claim are wrong.
   - **Costs rise in bursts.** Six of the 25 years from 2001 to 2025 each rose more than 7% (2004, 2006, 2007, 2008,
     2021, 2022). Together they carried about 80% of the index's rise. The other 19 years averaged 0.8% a year.
   - **A burst usually raises the price level for good.** The yearly rate fell back within a year or two of every burst,
     but the level came down only once: 2009 gave back 8.9% after 2008's metal spike, and the 2008 average was not
     reached again until 2018. The 2004 level and the 2021-22 rise of 19.1% stayed.
   - **2026's burst is led by wages, not materials.** In 2021 materials rose +13.74% against labour +6.36%. In September
     2026 wages rose +9.29% against materials +7.27%, against a shortage of 46,151 workers and a migrant quota that is
     fully allocated. Wages are the part least likely to fall back.
   - **Better wording:** "about 3% a year central; a burst like 2026's raises the price level for good even when the
     rate slows."
2. **Claim 2: CHANGE.** The codes are real and verified. The claim gets wrong where the cost lands.
   - **After Chi-Chi.** The code was revised on 29 Dec 1999 (two zones, Z = 0.33 and 0.23; design forces raised across
     the board). That date became Taiwan's line between "old" and "new" buildings: every retrofit programme since 2016
     targets buildings applied for on or before 31 Dec 1999.
   - **Hualien 2024 changed no design rule.** The latest revision is dated 1 Mar 2024, a month before the quake. What
     followed Hualien was money and speed for damaged homes: evaluation subsidies, weak-storey retrofit up to NT$15m a
     building and at most 85%, and a fast path to rebuilding.
   - **For a new small building the code adds little.** NCREE puts its 2022 near-fault provisions at about 5% of
     construction cost; NIBS puts today's US codes at about 1% over 1990's.
   - **For an older building the cost can be large.** Retrofit runs about 12-20% of replacement value in the literature
     (FEMA's North Hall: 20%), more for small, old or historic buildings.
   - **Better wording:** "seismic rules add little to a new small building; they bear on renovating a pre-2000 building
     for public use, one more way a building's age turns into cost."
3. **Claim 3: CHANGE (the direction holds; drop "mostly").** No Taiwan study measures the shares, so "mostly" cannot be
   kept. What the evidence shows:
   - **The national index is the predictable part, and the plan already shows it** (NUMBERS 8d; Table 3 row 7). At 3%
     it adds about 19% over six years (Keel arithmetic).
   - **The parts no national rate shows are larger in one month or one job:**
     - In October 2026 Taichung's index rose 10.61% on a year and Kaohsiung's 5.61%: five points apart, more than the
       plan's whole band of 1.5% to 5.0%.
     - The Control Yuan's own heritage repair overran 22.47% on cost and 37.03% on time, from rot found only once the
       roof was opened. The PCC had warned of exactly that in writing beforehand.
     - Small heritage repairs fail to draw bidders (three failed tenders in Tamsui).
   - **Better wording:** "the part of building risk the plan cannot show comes from the site and the building's age and
     condition; the national index is the part already shown."
4. **Clash: none with the FINAL IPS or the TNA.** IPS l.15's "building costs that overrun" is supported, not changed.
   - **Risk to record (no change):** Table 3 row 7 tests "building costs 1.5% to 5.0% a year". That is a band for the
     rate. A burst window can run faster: 2003-2008 ran 8.9% a year (Keel arithmetic), and the 6-year maximum in
     `numbers/inflation_inputs.json` is 8.18%.
   - SKELETON 3e's sentence (building costs "tested against her flexibility ... not model inputs") still holds.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | What the index measures: base 2021 = 100; materials 659.24 per mille, services 340.76 (wages 238.32, equipment rent 102.44); building construction weighted 645.67 materials / 354.33 services; prices from large suppliers in seven cities including Hualien; released about 5 working days after month end, revisable for 3 months | DGBAS (2026a, 2026b); REFERENCES #40, #41 | INFLATION_TWD | KNOWN | The index prices big-contract inputs; a small renovation buys more labour and less bulk material than its weights (Keel inference) | Labour share of a small Taiwan renovation not found (gap) | VERIFIED (file notes read) | no | cci.xls / ccispl.xls notes |
| 2 | Costs rise in bursts: six of 25 years (2004 +14.1%, 2006 +7.3%, 2007 +9.0%, 2008 +14.0%, 2021 +10.9%, 2022 +7.4%) carried about 80% of the index's 2000-2025 rise; the other 19 years averaged 0.8% a year | DGBAS (2026b) yearly averages; Keel arithmetic (log changes) | INFLATION_TWD, HISTORY | NICHE | "About 3% a year" averages quiet years and bursts; for 2027-2033 the question is whether a burst lands inside the window, which is why 6-year windows ran -0.1% to 8.2% (Q10 row 20) | "Above 7%" is Keel's cut-off; yearly averages, not December to December | VERIFIED data; Keel arithmetic | no | ccispl.xls, yearly rows 2000-2025 |
| 3 | A burst usually raises the price level for good: the 2004 level was never revisited; the 2021-22 rise of +19.1% held and 2023-2025 added 1.5% a year; only 2008's partly reversed (2009 -8.9%), and the 2008 average was not passed again until 2018 | DGBAS (2026b); Keel arithmetic | INFLATION_TWD, HISTORY | NICHE | "A cycle, not a trend" is half right: the rate returns, the level does not. NT$ buying power lost in a burst stays lost; that is what her flexibility meets | The one reversal followed a global commodity crash; 3 bursts is a small sample | VERIFIED data; Keel arithmetic | risk: Table 3 row 7's band is a rate; a burst is a level step (record only) | ccispl.xls |
| 4 | After every burst the yearly rate fell back within one or two years: 2005 +0.7%; 2010-11 +3.2% and +3.3% after 2009's fall; 2023-2025 +1.7%, +2.0%, +0.8% | DGBAS (2026b); Keel arithmetic | INFLATION_TWD | KNOWN | Supports 3.0% as the central rate for a window that starts in a burst year; 3e's band stays | No forecast of when 2026's rate slows was found from DGBAS or the central bank | VERIFIED data | no | ccispl.xls |
| 5 | 2026 so far: September 120.26 is 7.1% above the 2025 average (Keel arithmetic); September +0.65% on the month; the January-September average +4.87% on a year | DGBAS (2026a) | INFLATION_TWD, MONITOR | KNOWN | The "today's construction" prices behind NUMBERS 8d's NT$2.59m-NT$3.14m already hold most of this burst (Keel inference) | One partial year | VERIFIED | no | cci.xls, September 2026 sheet |
| 6 | October 2026 national index: +7.18% on a year (September 7.29%); next update 8 Dec 2026. DGBAS's database lists October as published, but the downloadable files still ended in September on 14 Nov | MacroMicro (n.d.); DGBAS (n.d.) database page | INFLATION_TWD, MONITOR | KNOWN | NUMBERS 8d's "+7.29%" stays the latest figure read at source; update when DGBAS's file posts | Secondary aggregator; October components not seen | UNVERIFIED (secondary) | no | MacroMicro series 502; nstatdb A030502015 |
| 7 | Inside September's materials (beyond Q10 row 19): metal products +7.57%, plastics +18.14%, electrical machinery +18.03%, asphalt +15.12%; cement -0.79%, sand and gravel -0.40%; services +7.32% (equipment rent only +2.83%) | DGBAS (2026a) | INFLATION_TWD | NICHE | The 2026 materials rise is in fittings, cable and asphalt (copper, oil), not concrete; a fit-out-heavy renovation feels it more than a new frame does (Keel inference) | Sub-group weights in a small job unknown | VERIFIED | no | cci.xls |
| 8 | The building sub-index runs gentler than the headline: September building construction 116.86 (+5.93%; materials +6.60%, services only +4.77%) against civil engineering 124.60 (+8.88%; services +10.61%); since the 2021 average, buildings +16.9% against the whole index's +20.3% (Keel arithmetic) | DGBAS (2026a) | INFLATION_TWD | NICHE | A residency is a building; Table 3 row 7's band sits on the gentler series. Q10 row 19 has the two headline rates; this row adds the services split and the gap since 2021 | Civil works (fabs, public works) lead the wage surge now and may pass it to buildings | VERIFIED; Keel arithmetic | no | cci.xls |
| 9 | 2021-22 was materials-led: 2021 materials +13.74% against labour +6.36% (wages +6.54%), metal products +28.82%; 2022 materials +8.51% against labour +5.36% (wages +4.79%) | LY Budget Center (2022, 2023a) | INFLATION_TWD, HISTORY | NICHE | The burst that eased fastest (metal from late 2022) was materials; contrast with row 10 | Even this burst's level held (row 3) | VERIFIED | no | LY PCC 2023 budget assessment item 3; LY 2023 report table 3-3-1 |
| 10 | 2026 is wage-led: August wages +8.12% on a year, the highest since September 2021; services +6.45%, the highest since April 2022. DGBAS's section chief named young people unwilling to enter the trade, an ageing workforce and plant-building demand: pressure "由材料端向勞務端擴散" (spreading from materials to labour). Copper is held up by AI data-centre power demand; steel and asphalt follow oil | 經濟日報 (2026); September wages +9.29% in Q10 row 19 | INFLATION_TWD, MONITOR | NICHE | Wages rarely fall in money terms (Keel inference), so this burst is less likely to reverse than 2008's; it argues for keeping the band's top, not lowering it | News report quoting the official; no wage sub-index history before 2021 was read | SECONDARY (named DGBAS official quoted) | no | udn.com, 9 Sep 2026 |
| 11 | Claim seen and not used: September wages "highest since March 1993" and the index "highest on record" | ainews24 (2026a, 2026b) | INFLATION_TWD | KNOWN | The record-level part agrees with DGBAS's series as read (September 2026 is above every yearly average and every 2026 month); the 1993 part is not checked | AI-written news site | UNVERIFIED | no | ainews24.info, 17 and 20 Oct 2026 |
| 12 | The shortage in numbers: MOI's survey (2,358 firms) puts construction vacancies at 46,151, 70.5% of them basic labour (32,525: about 9,917 ordinary, 22,000 skilled); central Taiwan 10,248, north 9,977, south 8,082; the 15,000 migrant quota opened Aug 2023 is fully allocated, yet 92.7% of firms employ no migrant workers (81.6% of firms with 300+ staff do) | 工商時報 (2026a), citing MOI's construction economic survey | INFLATION_TWD, RESIDENCY | NICHE | A small job competes with fabs and public works for the same crews; small builders, who hire no migrants, feel the shortage most (Keel inference) | Survey estimate; regional split is vacancies, not rates | SECONDARY (MOI survey via newspaper) | no | ctee.com.tw, 3 Aug 2026 |
| 13 | April 2026 causes: shortage above 50,000 (MOI estimate), worst in masonry, formwork and rebar; oil prices from the US-Iran war lifted "幾乎100%的營造物料" (almost 100% of building materials, contractors' association); soil-disposal costs (土方之亂); the carbon fee, indirectly | 工商時報 (2026b) | INFLATION_TWD | KNOWN | Several of 2026's causes are local and structural (labour, soil disposal), not only world prices | Trade-association view | SECONDARY | no | ctee.com.tw, 20 Apr 2026 |
| 14 | Outlook: steel and asphalt-concrete costs "短期內難以快速回到衝突前水準" (unlikely to return quickly to pre-conflict levels) with soil-disposal fees still high (an analyst at 台經院, the Taiwan Institute of Economic Research); CIER sees AI demand spilling over into "cost disruptions" across services with labour shortages | 自由時報 (2026); CIER (2026) | INFLATION_TWD, MONITOR | KNOWN | No source read expects the 2026 level to fall; a watch for 3e: if the AI build-out turns, labour pressure eases | Analyst views, not forecasts of the index | SECONDARY | no | estate.ltn.com.tw; cier.edu.tw |
| 15 | Regional spread in one month: October 2026 Taichung city index 125.05, +10.61% on a year (labour +16.67%, wages +20.96%), against Kaohsiung 117.25, +5.61% (wages +2.30%) | 臺中市政府 (2026); 高雄市政府主計處 (2026) | INFLATION_TWD, RESIDENCY | NICHE | Two cities sit five points apart in one month, more than the plan's whole band (1.5% to 5.0%); where the residency stands can matter more than the national rate (claim 3) | City indices use their own samples and weights; one month | VERIFIED (each city's own release) | no | Taichung release (EPB repost); Kaohsiung press release PDF |
| 16 | Public works contracts usually reprice once the index moves 2.5%; price-adjustment payments ran NT$135.6m (2018), NT$436.7m (2019), NT$147.7m (2020), NT$467.0m (2021), NT$1,513m (2022) and NT$819m in January-April 2023: 634 cases and NT$3.52bn in all | LY Budget Center (2023a) | INFLATION_TWD | KNOWN | In public works the owner carries index moves above a threshold; the index is Taiwan's escalation yardstick (the PCC manual prices escalation from it, store Q5-023). Who carries it in a private job is a contract question, out of scope | Public contracts only | VERIFIED | no | LY 2023 report, price-adjustment table |
| 17 | Of 98 central projects over NT$1bn revised from 2021 to July 2023, 41 raised budgets for construction prices or wages; Kinmen Bridge went from NT$5.705bn to NT$9.662bn (+69%, Keel arithmetic) over four revisions, with repeated failed tenders | LY Budget Center (2023b) | INFLATION_TWD, HISTORY | KNOWN | In the last burst about 4 in 10 big-project revisions named prices or wages; distinct from store Q24-032 (165 of 255 plans revised) | Huge infrastructure, not a small building | VERIFIED | no | LY 2024 central budget assessment, item 62 |
| 18 | In a burst the first thing a job meets is no bidders: Taipei City found failed-tender rates on its large projects moved closely with the index; the index rose 19.77% from Dec 2019 to Mar 2022 (materials +24.31%, labour +12.34%); rebar rose 49.35% in nine months | 曾俊傑 & 范汝欣 (2022) | INFLATION_TWD, RESIDENCY | NICHE | A burst shows up as delay before it shows up as price; a residency opening around 2033 meets time risk as well as cost risk | Large public contracts in one city | VERIFIED | no | Taipei City statistical analysis report 111-22 |
| 19 | Consumer prices, October 2026: +2.33% on a year, core +2.23%, January-October +1.98%, confirmed in DGBAS's Chinese release; next release 8 Dec 2026. The 2026 gap between building costs and CPI is about 5 points (7.29 - 2.33, Keel arithmetic) against 1.85 a year over 2000-2025 | DGBAS (2026c); REFERENCES #44; Q10 row 15; `numbers/inflation_inputs.json` | INFLATION_TWD | KNOWN | No change to Q10's inputs; it shows why the case's "inflation" for the facility is building costs, not CPI | One year's gap | VERIFIED | no (C15 holds: the payments are fixed dollars) | newstotal11510.pdf |
| 20 | Code history: seismic forces first in 1974; importance factor I added 1982; Taipei basin raised in 1989 after the 1986 Hualien quake; first stand-alone code 1997 (four zones); 29 Dec 1999 emergency revision after Chi-Chi; microzones and near-fault rules in 2005 (revised 14 Dec 2004, in force 1 Jul 2005); Taipei basin re-zoned 2011; new code in force 1 Oct 2022; partial revision 1 Mar 2024 | NLMA (n.d.-b); 劉勛仁 et al. (2014); LY Budget Center (2016, 2020); MOI (2024a) | RESIDENCY, HISTORY | KNOWN | Six revisions in 50 years; a building's design year says which rules it met | MOI's regulation page dates a 2005 version 21 Dec 2005 (in force 1 Jan 2006); two MOI pages differ on 2005 | VERIFIED | no | NLMA programme page; NCREE 2014 paper; LY reports |
| 21 | After Chi-Chi the zones were cut to two: A (Z = 0.33: Taichung, Nantou, Hualien, Taitung, Tainan, Chiayi, Yunlin, Changhua, Miaoli, Hsinchu, Yilan) and B (Z = 0.23: Taipei, New Taipei, Keelung, Taoyuan, Kaohsiung, Penghu), and design forces were "全面提高" (raised across the board) | CWA (n.d.); 劉勛仁 et al. (2014) | RESIDENCY | NICHE | A 1990s building in central or eastern Taiwan was designed well below today's forces for its zone | Zones replaced by microzones in 2005; Laura's site is unknown | VERIFIED | no | CWA FAQ 19; NCREE 2014 paper section 1 |
| 22 | The 31 Dec 1999 line: on 25 Feb 2016, after the Meinong quake, the Executive Yuan set every public and private seismic check-and-retrofit programme on buildings applied for on or before 31 Dec 1999, "基於921震災後有關提高耐震設計之規範，實施日期為88年12月底" (because the post-921 code took effect at the end of Dec 1999) | NLMA (n.d.-c), Executive Yuan letter of 28 Dec 2017 | RESIDENCY | NICHE | One date sorts Taiwan's buildings into old and new for seismic purposes; a residency in a building applied for before 2000 sits on the old side | Programme scope, not a legal duty on any one building | VERIFIED | no | NLMA "建築物實施耐震能力評估及補強方案（公有建築物）" |
| 23 | Older buildings flagged: of 37,402 pre-2000 reinforced-concrete buildings of six floors or more screened from plans in 2017-2021, 3,750 (about 10%, Keel arithmetic) showed possible danger | LY Budget Center (2022b) | RESIDENCY, HISTORY | NICHE | A base rate for "old building" risk: about one in ten older mid-rise concrete buildings flagged | Six floors or more, mostly housing; a small residency is likely low-rise | VERIFIED | no | LY report on building safety, item 3 |
| 24 | Once a public building is evaluated in detail, work usually follows: the pre-2000 public-buildings programme logged 31,227 preliminary and 17,037 detailed evaluations, 9,912 retrofits and 2,415 demolitions by Sep 2024; retrofits plus demolitions equal 72% of detailed evaluations, demolitions 14% (Keel arithmetic on cumulative counts) | MOI (2024c) | RESIDENCY | NICHE | For an older public-use building, an evaluation is usually the start of works, not the end of a check | Cumulative counts, not one cohort; public buildings of classes I = 1.5 and 1.25 | VERIFIED; Keel arithmetic | no | MOI sub-plan update, 18 Oct 2024 |
| 25 | For buildings open to the public the question can come from the regulator: seismic evaluation is part of the public safety inspection since 1 Jul 2019 (art. 7 amended 21 Feb 2018), and Building Act art. 77-1 (amended 11 May 2022) lets authorities order existing public-use buildings below current rules to improve or change use | MOI (2024b, 2024c) | RESIDENCY | NICHE | A residency open to visitors is a building used by the public; the age of the building can turn into required works, not optional ones (code fact, no legal advice) | As MOI describes it; statute text not read; which inspection class a residency falls in is out of scope | VERIFIED (MOI's description) | no | MOI sub-plan updates, 30 Jun and 18 Oct 2024 |
| 26 | Hualien 2024 changed no design rule: the last revision is MOI's order of 1 Mar 2024, a month before the 3 Apr 2024 quake | MOI (2024a); NLMA (n.d.-b) | RESIDENCY | NICHE | Kills claim 2's "after Hualien 2024" for design costs; the report must not say the code was tightened after Hualien | No revision after 1 Mar 2024 found on NLMA's list (updated 8 May 2025) | VERIFIED (dates) | no | MOI order 台內國字第1130801422號; NLMA regsearch/175 |
| 27 | What followed Hualien: evaluation subsidies (preliminary up to NT$15,000, detailed up to NT$400,000); weak-storey retrofit for red- or yellow-tagged homes up to NT$15m a building (six floors or fewer NT$7.5m), at most 85%; tagged buildings may go straight to 危老 rebuilding; 50 weak-storey cases approved in Hualien within a year | MOI (2024d, 2025a, 2025b); Executive Yuan (2024) | RESIDENCY | NICHE | Aid targets homes; the general weak-storey subsidy covers buildings at least half residential, so an arts building is mostly outside (as read; eligibility is a legal question, out of scope) | Housing programme; Hualien-specific rules | VERIFIED | no | MOI press releases 11 Apr 2024, 31 Mar 2025; 作業規定 (11 Jun 2024, amended 21 Aug 2025); EY briefing |
| 28 | Strengthening comes in stages: New Taipei's slides note a weak-storey retrofit cuts collapse risk sharply, but meeting the design earthquake "未來仍需進行整幢完整補強" (later still needs full retrofit of the whole building, art. 77-1). One 2019 job: NT$1,732,532 with one design change adding NT$80,000 (4.6%, Keel arithmetic) and 6 days; a Hualien building NT$8,316,676 | 新北市政府都市更新處 (2024) | RESIDENCY | NICHE | A partial fix may not end the question; an owner of an older building can face a second round | Housing cases; never a figure for Laura's building | VERIFIED | no | NTPC Urban Renewal Office slides, May 2024 |
| 29 | Renewal-maintenance subsidy schedule: seismic retrofit NT$4,000 per square metre, up to 55%; facade repairs NT$1,500 per square metre, up to 50% | 新北市政府都市更新處 (2024) | RESIDENCY | KNOWN | Shows public money exists for older-building works, mostly for housing and renewal schemes | Eligibility and scope not checked (legal) | VERIFIED (slide) | no | NTPC slides, "中長期重建協助措施" |
| 30 | New-build code cost in Taiwan: NCREE says the 2022 near-fault provisions raise new buildings' seismic capacity 20-30% "而工程造價成本僅增加約5%" (while construction cost rises only about 5%); buildings with isolation or damping rose from 80 (2009) to over 1,000 (2022); the chance of a magnitude-7 quake within 50 years "可能高達三成" (may be as high as 30%) | NCREE (2022) | RESIDENCY, CERTAINTY | NICHE | For a new small building the code adds a few percent at most; the seismic cost question is about old buildings (claim 2) | Near-fault sites; NCREE is the code's author | VERIFIED | no | NARLabs press slides, 15 Nov 2022 |
| 31 | US evidence on new-build code cost: today's model codes add "only about 1%" to construction cost over 1990 standards (earthquake design: $0.6bn a year of cost for $7bn of benefit); one 1976 steel building: seismic design added 2.8% | NIBS (2019); Larrabee & Whitman (1976) | RESIDENCY | KNOWN | Same order as NCREE's 5%: code cost is small on a new building | US codes and prices | VERIFIED (fact sheets and report pages read) | no | NIBS Mitigation Saves; MIT report No. 28 |
| 32 | Retrofit cost as a share of a new building: FEMA's UCSB North Hall, $11.76 per sq ft against about $60 to replace (about 20%); estimating heuristics use 12% and 20% of replacement value; reinforcing costs are "higher for older buildings, smaller buildings and historic buildings", and Los Angeles replaced school buildings once reinforcing passed 70-80% of new | FEMA (2021); Fung et al. (n.d.); Larrabee & Whitman (1976) | RESIDENCY, HALFKEPT | NICHE | The order of magnitude for an older building: a tenth to a fifth of new, more if small, old or historic; never a figure for Laura's building | US and Greek cases; no Taiwan figure found (gap) | VERIFIED (pages read) | no | FEMA case study; NIST manuscript; MIT 1976 |
| 33 | A retrofit pulls in other work: total cost includes non-seismic work the job triggers (disability access, asbestos removal, system upgrades), design fees and permits | Fung et al. (n.d.), summarising FEMA 156 | RESIDENCY, HALFKEPT | NICHE | The route by which a building's age becomes cost is a chain, not one item; an "overrun" in an old building is often triggered work | FEMA 156 itself not read; Taiwan's triggers are legal questions | VERIFIED (secondary summary of FEMA 156) | no | NIST/PMC manuscript, cost categories |
| 34 | Importance factor (code fact): a building used only for assembly needs I = 1.25 only if its total floor area is 1,000 m² or more; mixed use: assembly under 1,000 m² gives 1.0, 3,000 m² or more 1.25, and 1,000-3,000 m² 1.25 only if assembly is 20% or more of the floor area. Section 8.3: an existing building, after detailed evaluation or retrofit, must reach the 475-year design earthquake times I, or a stated performance target | MOI (2024a) | RESIDENCY | NICHE | A small residency probably sits under the 1,000 m² line, so the code's extra margin for assembly would not apply (Keel inference; whether its rooms count as assembly is an engineer's call) | Code fact only; no advice on any building | VERIFIED | no | MOI order of 1 Mar 2024, sections 2.8 and 8.3 |
| 35 | Hidden conditions in old-building repair: the Control Yuan's own heritage building (roof and facade) was planned at NT$74.0m and 640 days; after three design changes for work found during the job (rotten roof trusses found beam by beam) it cost NT$90.627m and took 877 days: +22.47% cost, +37.03% time; the first tender failed for too few bidders | LY Budget Center (2019, 2020) | RESIDENCY, HALFKEPT, HISTORY | NICHE | The clearest Taiwan record of the overrun IPS l.15 names; the risk sits in the building, not the index | A national heritage building; much larger than a residency | VERIFIED | no (supports l.15's "building costs that overrun") | LY Control Yuan final-accounts assessments, 2018 and 2019 accounts |
| 36 | The PCC warned beforehand: "如屋頂未拆解前，無法詳細預估桁木損壞數量" (until a roof is taken apart, the number of damaged timbers cannot be estimated), so design changes would follow | PCC letter of 31 Mar 2015, quoted in LY Budget Center (2020) | RESIDENCY, HALFKEPT | NICHE | Old-building overrun risk is known in advance and cannot be sized in advance: the case for money promised to no one rather than a sized contingency (CANON A31) | One agency's letter on one building | VERIFIED (as quoted by the LY) | no | LY 2020 report, footnote 3 |
| 37 | Small heritage repairs struggle to draw bidders: the Tamsui house (淡水木下靜涯舊居) failed three tenders before award on 30 Dec 2019; it and Tainan's 三山國王廟 both changed total budget and schedule during works | LY Budget Center (2021) | RESIDENCY | NICHE | For a small old building, delay arrives before cost; a 2033 opening carries time risk | Budget changes not sized in the report | VERIFIED | no | LY MOF 2020 final-accounts assessment, item 2 |
| 38 | Treasure Hill's build time: an artist-village idea in 1999, listed 2004, works from late 2006, opened 2 Oct 2010 "following a four-year-long renovation and rebuilding project"; no cost figure found in what was read | Ministry of Culture (2015); Taipei Artist Village (n.d.) | RESIDENCY | KNOWN | Four years of works and eleven from idea to opening for an arts conversion of old self-built houses; Q9c has its budgets and contract, this row adds the time | A whole settlement, not one building | VERIFIED (dates); cost UNVERIFIED (not found) | no | MOC English page; artistvillage.org "About" |
| 39 | Both Taipei city residencies were re-used buildings: Taipei Artist Village was a four-storey former maintenance-office building re-used in 2001 (閒置空間再利用); its site went to urban renewal and it left at the end of 2023 (closure in Q9c row 22) | Taipei Artist Village (n.d.) | RESIDENCY | KNOWN | In Taiwan an older building is the usual home of a residency, so site and age risk is the norm, not the exception (Keel inference from two cases plus Q9c's five) | Small sample | VERIFIED | no | artistvillage.org "About" |
| 40 | Synthesis for claim 3: the national index at 3% adds about 19% over six years (1.03^6, Keel arithmetic), and the plan already shows it (NUMBERS 8d; Table 3 row 7); the parts no national rate shows are at least as large in single cases (a 5-point city gap in one month, row 15; a 22.47% heritage overrun, row 35; repeated failed tenders, rows 18 and 37) | Rows 15, 18, 35-37; NUMBERS 8d | RESIDENCY, HALFKEPT, INFLATION_TWD | NICHE | Rewrite claim 3 without "mostly": the risk the plan cannot show comes from the site and the building's age and condition | No measured shares; cases are larger buildings | Keel inference | no | This card |

## (b) Cards

**Card 1. Building costs move in bursts, and a burst usually stays (DGBAS yearly averages, 2000-2025; Keel arithmetic).**
- **What is it?** DGBAS's construction cost index, read as yearly averages, rose 3.0% a year from 2000 to 2025, but the
  rise was not steady:
  - **Six years carried about 80% of it.** Each of 2004, 2006, 2007, 2008, 2021 and 2022 rose more than 7%. The other
    19 years averaged 0.8% a year.
  - **The 2003-2008 run** went 8.9% a year.
  - **The 2021-22 pair** added 19.1% in two years.
- **Did it work as a "cycle"?** Only for the rate:
  - **The rate fell back every time:** +0.7% in 2005; +3.2% and +3.3% in 2010-11; +1.7%, +2.0% and +0.8% in 2023-25.
  - **The level fell back once:** 2009 gave back 8.9% after 2008's metal spike, and the 2008 average was not passed
    again until 2018.
  - **The 2004 and 2021-22 levels never came down.**
- **How is Laura's case like it?**
  - The contribution is paid around December 2032 and buys Taiwan construction then.
  - NUMBERS 8d turns the range into NT$2.59m-NT$3.14m of today's construction at 3%.
  - A burst between now and 2033 moves that level once and keeps it there; this is the "building costs" risk IPS
    l.15 names.
- **How is it not?**
  - The index prices large-contract inputs in seven cities, not one small renovation (row 1).
  - Three bursts are a small sample.
  - 2026 is already a burst year, so some of the step is already in "today's" prices.
- **What Caplet takes:**
  - In 3e, if a clause is spent, "about 3% a year on the long record, though costs rise in bursts that stay": no new
    number, so no NUMBERS entry is needed.
  - Table 3 row 7 stays: its band is a rate, and the record of a level step goes to the store.
  - Never "a cycle, not a trend".

**Card 2. 2026 is a wage burst; 2021 was a materials burst (DGBAS September 2026; LY Budget Center 2022, 2023; udn 9
Sep 2026; Commercial Times 3 Aug 2026).**
- **What is it?** The two bursts had different causes.
  - **2021-22:** materials led (+13.74% and +8.51%) and labour lagged (+6.36%, +5.36%), driven by metal (+28.82% in
    2021) and world commodities.
  - **2026:** wages lead. They rose +8.12% in August (the most since September 2021) and +9.29% in September. Services
    rose +7.32%, while materials rose +7.27%, mostly plastics, electrical machinery and asphalt.
  - **DGBAS's own reading:** the pressure is "spreading from materials to labour". The causes it names are young
    people unwilling to enter the trade, an ageing workforce and plant-building demand.
  - **The MOI survey's numbers:** 46,151 vacancies, 70.5% of them basic labour; the 15,000 migrant quota is full, yet
    92.7% of firms hire no migrant workers.
- **Did it work?** The 2021 materials burst slowed within a year: metal eased from late 2022, and the rate fell to
  +1.7% in 2023. No source read expects 2026's wage pressure to reverse:
  - An analyst expects steel and asphalt "unlikely to return quickly" to pre-conflict levels.
  - CIER describes labour shortages spreading with AI demand.
- **How is Laura's case like it?**
  - A small residency job is labour-heavy and uses small builders, which hire no migrant workers.
  - The wage part of 2026 is the part most likely to stay in the price of her residency's building work (Keel
    inference).
- **How is it not?**
  - The wage surge is sharpest in civil works: services +10.61% against building services +4.77%.
  - It is sharpest in some cities: Taichung's wages +20.96% against Kaohsiung's +2.30%.
  - A building in a quieter market may see far less.
- **What Caplet takes:**
  - The store, and one word in 3e at most ("led by wages").
  - For NUMBERS 8d, nothing changes: the band's top of 5.0% is above the 6-year p90 of 4.56% and stays sensible.
  - The watch for the report's "what to monitor" is the wage line in DGBAS's monthly release, not the headline.

**Card 3. The 31 December 1999 line, and what Hualien 2024 did and did not change (MOI and NLMA; CWA; NCREE; Executive
Yuan 2016 decision).**
- **What is it?**
  - **29 Dec 1999.** After Chi-Chi (21 Sep 1999), MOI revised the seismic code in an emergency revision. Zones went to
    two, A (0.33g) and B (0.23g), and design forces were raised across the board.
  - **25 Feb 2016.** After the Meinong quake, the Executive Yuan set every public and private check-and-retrofit
    programme on buildings applied for on or before 31 Dec 1999, for that reason.
  - **Later revisions** came in 2005 (microzones, near-fault), 2011, 2022 and 1 Mar 2024.
  - **The 3 Apr 2024 Hualien quake** brought no design-rule change. It brought subsidies and speed for damaged homes:
    evaluation subsidies; weak-storey retrofit up to NT$15m a building and at most 85%; a direct path to 危老
    rebuilding for tagged buildings.
- **Did it work?** The line is used everywhere:
  - The public-buildings programme logged 17,037 detailed evaluations and 12,327 retrofits or demolitions by Sep 2024.
  - A screening of 37,402 older mid-rise concrete buildings flagged 3,750.
  - Seismic evaluation has been part of public-safety inspection since July 2019.
  - Building Act art. 77-1 (2022) lets authorities order older public-use buildings to improve.
- **How is Laura's case like it?** A residency housed in a building applied for before 2000 sits on the old side of the
  line, and a residency is used by the public. That is the most direct route by which a building's age becomes required
  work.
- **How is it not?**
  - Laura's site, building and use class are unknown, and the case leaves them to others.
  - Most of the money and the screening targets housing and buildings of six floors or more.
  - A small new building meets the current code at little extra cost (card 4).
- **What Caplet takes:**
  - Claim 2's "after Hualien 2024 the code raised costs" must never appear.
  - For 3e or 3d, at most a half-clause (lead's call): "a building older than 2000 may need strengthening before the
    public uses it". Store-first: the page budget is tight, and the plan secures the money, not the building.

**Card 4. What seismic rules cost: a few percent on a new building, a tenth to a fifth or more on an old one (NCREE 2022;
NIBS 2019; Larrabee and Whitman 1976; FEMA; Fung et al.).**
- **What is it?** Five sources, for new and old buildings:
  - **NCREE (new buildings):** the 2022 near-fault provisions raise new buildings' seismic capacity 20-30% for about 5%
    more construction cost.
  - **NIBS (new buildings):** US model codes today add "only about 1%" to construction cost over 1990's.
  - **MIT 1976 (new building):** one steel building, +2.8%.
  - **Old buildings:**
    - FEMA's North Hall retrofit cost about 20% of replacement.
    - Estimating heuristics use 12% and 20% of replacement value.
    - MIT 1976 found reinforcing costs higher for older, smaller and historic buildings; Los Angeles replaced schools
      once reinforcing passed 70-80% of new.
  - **Triggered work:** a retrofit pulls in non-seismic work (access, hazardous materials, systems), plus fees and
    permits.
- **Did it work?** NIBS finds code adoption saves about $11 per $1 and seismic retrofit about $13 per $1 across the
  US. FEMA's North Hall came through a 1978 quake with minor damage two years after its retrofit.
- **How is Laura's case like it?** Her flexibility exists for "building costs that overrun" (IPS l.15). Strengthening an
  older building, and the work it triggers, is a cost of that kind that no estimate can fix before the building is
  opened up.
- **How is it not?**
  - The US and Greek shares are not Taiwan's.
  - The case puts facility costs out of scope, so none of these percentages may become a figure for Laura's building.
- **What Caplet takes:**
  - The store, plus one framing for the team: seismic cost is an age question, not a code-year question.
  - It is a reason to keep money promised to no one rather than a sized contingency (CANON A31: none is sized).

**Card 5. The overrun nobody could count before the roof came off (LY Budget Center, Control Yuan accounts 2018-2019;
PCC letter of 31 Mar 2015).**
- **What is it?** The Control Yuan repaired its own national-heritage building (roof and facade).
  - **The plan:** NT$74.0m and 640 days.
  - **The changes:** three design changes, for work found only once the work began. The roof trusses were checked beam
    by beam and many were rotten. The first tender also failed for too few bidders.
  - **The result:** NT$90.627m and 877 days, +22.47% on cost and +37.03% on time.
  - **The warning:** the PCC had written beforehand that until a roof is taken apart, the number of damaged timbers
    cannot be estimated.
- **Did it work?** The building was finished (31 Dec 2019), but only by moving money between budget lines, drawing on
  the second reserve fund and extending the deadline three times. The LY's lesson is to survey more before tendering.
  The PCC's letter shows the remaining risk is irreducible.
- **How is Laura's case like it?**
  - A residency in an older building has the same kind of hidden-condition risk.
  - Like the PCC, an owner can know it in advance without being able to size it: that is what money "promised to no
    one" (IPS l.15) is for.
  - The Tamsui house's three failed tenders and Taipei City's failed-tender finding add time risk.
- **How is it not?** A national monument is far larger, slower and more tightly regulated than a small residency.
  There is no published study of overruns on small arts conversions in Taiwan (the team's own finding of 8 Nov stands),
  so this is one case, not a rate.
- **What Caplet takes:**
  - The best Taiwan example for "building costs that overrun", for the store and possibly 3b, in Keel's view: a clause
    with one figure at most, which would need a NUMBERS 0 entry as a quoted source figure.
  - It supports claim 3's rewritten form.

## (c) Verdicts

**Claim 1: CHANGE.**
- **Keep: about 3% a year as the central rate.**
  - DGBAS yearly averages give 3.0% a year from 2000 to 2025 (Keel arithmetic).
  - Q10 row 20 gives 3.19% to September 2026, 3.27% over five years and 3.91% over ten.
  - The 6-year window median since 1991 is 3.01% (`numbers/inflation_inputs.json`).
  - NUMBERS 8d's central 3.0% and band of 1.5% to 5.0% stand.
- **Change: "a cycle, not a new trend".**
  - The rate is cyclical: it fell back within one or two years of every burst (row 4).
  - The level mostly is not: 2004's and 2021-22's steps stayed, and only 2008's partly reversed (row 3).
  - Six burst years carried about 80% of the 25-year rise (row 2).
- **Change: what drives 2026.** The surge is led by wages (rows 10, 12), unlike 2021's materials surge (row 9). Wages
  are the part least likely to reverse (Keel inference).
- **Also note:**
  - The building sub-index runs below the headline (row 8).
  - Cities differ by five points in one month (row 15).
- **October 2026 at the source:** DGBAS's file was not yet posted; MacroMicro shows +7.18% (row 6, UNVERIFIED).
- **CPI October +2.33%** is confirmed at the source (row 19).
- **Rewrite:** "About 3% a year on the long record is the central rate for 2027-2033; Taiwan building costs rise in
  bursts that raise the level for good, and 2026's (+7.29% in the year to September) is led by wages."

**Claim 2: CHANGE.**
- **Keep: the codes changed after Chi-Chi.** The emergency revision of 29 Dec 1999 raised design forces and set the 31
  Dec 1999 line that every retrofit programme uses (rows 20-22).
- **Kill: "after the April 2024 Hualien earthquake" as a code change.**
  - No design rule changed after Hualien; the last revision is 1 Mar 2024 (row 26).
  - What changed was subsidies and fast rebuilding, mostly for homes (row 27).
- **Change: where the cost lands.**
  - **New small building:** a few percent at most (NCREE about 5% near faults; NIBS about 1%; rows 30-31).
  - **Older building used by the public:** evaluation, possible required improvement (art. 77-1), staged retrofit,
    and work the retrofit triggers (rows 24, 25, 28, 33). Retrofit costs run about 12-20% of a new building's, more
    for small, old or historic buildings (row 32).
- **Keep: "a reason an owner keeps flexibility".** It matches IPS l.15's "building costs that overrun" and CANON A31
  (no sized fund).
- **Rewrite:** "Seismic rules add little to a new small building; they bear on renovating a building designed before
  2000 for public use, one more way a building's age turns into cost, and one reason an owner keeps flexibility."

**Claim 3: CHANGE (the direction holds; drop "mostly").**
- **Keep: the direction.** The national index is the predictable part, and the plan already shows it (NUMBERS 8d;
  Table 3 row 7). The site and the building's age and condition are where the unshown risk sits. In single cases each
  is at least as large as six years of index drift (about 19% at 3%):
  - a five-point city gap in one month (row 15);
  - a 22.47% heritage overrun from hidden rot (row 35);
  - failed tenders that turn into delay (rows 18, 37);
  - required seismic work on older public-use buildings (rows 22-25).
- **Kill "mostly".** No Taiwan study measures the shares. The team's 8 Nov finding ("no study of overruns on small
  Taiwan cultural buildings") still stands after today's search.
- **Rewrite:** "The part of a small residency's building risk that the plan cannot show comes from the site and the
  building's age and condition; the national index is the part it already shows."
- **Builds on Q9c, without repeating it:** Q9c showed that losing the site ended residencies. This card adds that the
  building's age and condition raise its cost and time.

**Clash with FINAL or TNA: none.**
- IPS l.15 names "building costs that overrun" among her flexibility's three uses, and every finding here supports
  that use.
- TNA's "nonexistent inflation risk" is about the payments (CANON C15) and is untouched.
- **Risk to record (no change):** Table 3 row 7's "building costs 1.5% to 5.0% a year" is a band for the rate.
  - A burst is a step in the level, and a burst window can run faster than 5.0%: 2003-2008 at 8.9% a year; a 6-year
    maximum of 8.18%.
  - The plan answers with her flexibility (about $21,300, or $29,800 with anything above the top; NUMBERS section 4),
    which is sized as half the shares, not to a cost (CANON A31).

## (d) Gaps

- **DGBAS's October 2026 index was not read at the source.** The cci.xls and ccispl.xls files still ended in September
  on 14 Nov, though DGBAS's database lists October as published. MacroMicro's +7.18% stands as secondary. Re-read the
  DGBAS file before NUMBERS 8d is next touched; its next update is 8 Dec 2026 with November.
- **The wage sub-index before 2021 was not read.** So "wage-led rises do not reverse" rests on inference, and ainews24's
  "highest since March 1993" is unchecked.
- **The labour share of a small renovation in Taiwan was not found.** Row 1's "more labour than the index weights" is
  inference.
- **No Taiwan figure for retrofit cost as a share of rebuilding was found.** Rows 32-33 use US and Greek heuristics.
  FEMA 156 itself was not read, only Fung et al.'s summary of it. The authors and year of the Fung et al. manuscript
  were not read in full (PMC9890378; NIST pub 928704).
- **The text of the 29 Dec 1999 revision was not read at the source.** It was read through MOI's programme text,
  NCREE's 2014 paper, the CWA FAQ and LY reports. The 2005 revision has two dates on two MOI pages (row 20).
- **No published overrun figures for small arts conversions in Taiwan (閒置空間再利用).** None for Treasure Hill,
  Taipei Artist Village or Bamboo Curtain either. Control Yuan or National Audit Office reports on the idle-space
  re-use programme were searched for and not found.
- **DGBAS's late-November outlook and the central bank's December statement are not out yet.** Q10 row 16 holds the
  latest forecasts read (CPI only; neither forecasts the construction index).
- **Not kept:**
  - A Federation of Industries (工總) request to double the construction migrant quota appeared in this run's earlier
    notes. Its source was not found again, so it is not in the table.
  - "Public works budget +15% in 2026" was not found at a source.

## Sources (APA 7; all accessed 14 Nov 2026, Sydney)

**Already in `../REFERENCES_APA.md`** (use those entries):
- #40: DGBAS (n.d.-a), *The changes of construction cost indices in Taiwan area*.
- #41: DGBAS (n.d.-b), *Time series of construction cost indices in Taiwan area*.
- #44: DGBAS (2026b), *The price indices for October 2026*.

**Already in card Q10's sources:** the central bank's 17 Sep 2026 board statement.

**New, read at the source.** [full] means the whole page, file or relevant chapter was read; [part] means only the
relevant section was read.

1. 行政院主計總處 [Directorate-General of Budget, Accounting and Statistics]. (2026a). *營造工程物價指數* [Construction
   cost indices, monthly table with components, to September 2026; file cci.xls] [Data set].
   https://ws.dgbas.gov.tw/001/Upload/464/relfile/10320/2710/cci.xls [full]
2. 行政院主計總處. (2026b). [Construction cost indices, yearly averages from 1991 and monthly 2026; file ccispl.xls]
   [Data set]. https://ws.dgbas.gov.tw/001/Upload/463/relfile/10315/2703/ccispl.xls [full]
3. 行政院主計總處. (2026c, November 5). [Press release on the October 2026 price indices, Chinese edition;
   newstotal11510.pdf]. https://ws.dgbas.gov.tw/001/Upload/463/relfile/10980/236836/newstotal11510.pdf (release page
   https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=236836) [full]
4. 行政院主計總處. (n.d.). *總體統計資料庫：營造工程物價指數* [Macro statistics database: construction cost indices].
   https://nstatdb.dgbas.gov.tw/dgbasAll/webMain.aspx?funid=A030502015&sys=210 [part]
5. MacroMicro. (n.d.). *Taiwan - construction cost index YoY* [Data series].
   https://en.macromicro.me/series/502/tw-construction-cost-yoy [full]
6. 經濟日報 [Economic Daily News]. (2026, September 9). 營造成本壓力未退 工資年漲8.12%五年最高 [Construction cost
   pressure has not eased; wages up 8.12% on a year, a five-year high]. 聯合新聞網.
   https://udn.com/news/story/7238/9744417 [full]
7. 工商時報 [Commercial Times]. (2026a, August 3). 建商叫苦連天！營造業缺工4.6萬人 逾92％中小企業沒請移工 [Builders
   complain: construction is short 46,000 workers; over 92% of firms hire no migrant workers].
   https://www.ctee.com.tw/news/20260803700087-439901 [full]
8. 工商時報. (2026b, April 20). 缺工、建材成本上漲 營造廠今年獲利受挑戰 [Labour shortages and rising material costs
   challenge contractors' profits this year]. https://www.ctee.com.tw/news/20260420701252-430503 [full]
9. 自由時報地產天下 [Liberty Times Estate]. (2026, September 25). 原料貴、土方貴、房子賣不掉……營造業未來半年憑什麼
   「逆風暴賺」？ [Dear materials, dear soil disposal, unsold homes: how will builders profit in the next six months?].
   https://estate.ltn.com.tw/article/28923 [full]
10. Chung-Hua Institution for Economic Research. (2026, August 10). *"Cost disruptions" sweep through manufacturing and
    services as AI demand spills over & labor shortages and inflationary pressures emerge*.
    https://www.cier.edu.tw/en/institution-en/32368 [part]
11. 臺中市政府 [Taichung City Government]. (2026, November). 10月營造物價指數較上月上漲0.11% 較上年同月上漲10.61%
    [October construction price index up 0.11% on the month and 10.61% on a year] [Press release, reposted by the
    city's Environmental Protection Bureau]. http://cleaner.epb.taichung.gov.tw/newsmain.aspx?n_id=26298 [full]
12. 高雄市政府主計處 [Kaohsiung City Government, Budget, Accounting and Statistics Office]. (2026, November).
    [Press release on Kaohsiung's construction cost index for October 2026].
    https://orgws.kcg.gov.tw/001/KcgOrgUploadFiles/261/RelFile/15632/543516/0a5db214-c57c-4d55-a49b-e9ffab4c66f7.pdf [full]
13. 立法院預算中心 [Legislative Yuan Budget Center]. (2022a, October). 三、營造工程物價指數持續攀升，允宜持續關注營建物料
    價格上漲對工程之影響並預為研議有效措施 [Item 3: The construction cost index keeps rising; watch its effect on works].
    In *行政院公共工程委員會112年度單位預算評估報告* [Public Construction Commission: assessment of the 2023 budget].
    https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~%2FFile%2FAttach%2F222214%2FFile_19747846.pdf [full]
14. 立法院預算中心. (2022b). 三、允宜提高建築物消防設備及安全檢查強度 [Item 3: Building fire and safety inspection should
    be strengthened]. In *我國政府近年推動建築物安全及智慧綠建築管理執行成效之研析* [Results of recent government work on
    building safety and smart green buildings].
    https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~%2FFile%2FAttach%2F220141%2FFile_19744396.pdf [part]
15. 立法院預算中心. (2023a). *近年中央政府有關公共建設計畫預算執行及其管控機制之探討* [Budget execution and control of
    central government public construction plans in recent years].
    https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~%2FFile%2FAttach%2F230676%2FFile_19786950.pdf [part]
16. 立法院預算中心. (2023b). 六二、受近年營造工程物價上漲之影響，部分公共工程採購案件多次流標，甚修正計畫調增經費
    [Item 62: Rising construction prices made some public works tenders fail repeatedly and plans be revised upward].
    In [Assessment of the 2024 central government budget].
    https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~%2FFile%2FAttach%2F231952%2FFile_19788953.pdf [full]
17. 曾俊傑, & 范汝欣. (2022, September). *嚴重特殊傳染性肺炎（COVID-19）疫情前後營造工程物價變化及對公共工程招標之影響*
    [Construction prices before and after COVID-19 and their effect on public works tenders] (統計應用分析報告 No.
    111-22). 臺北市政府主計處 [Taipei City Government, Department of Budget, Accounting and Statistics].
    https://www-ws.gov.taipei/Download.ashx?icon=.pdf&n=MTExMTPnlqvmg4XliY3lvoznh5%2FpgKDlt6XnqIvnianlg7nororljJblj4rlsI3lhazlhbHlt6XnqIvmi5vmqJnkuYvlvbHpn78ucGRm&u=LzAwMS9VcGxvYWQvMzY3L3JlbGZpbGUvNDUwMDAvODc0NDY4OC83ZGJhMjlhZi00ZjEzLTQ5MjUtOWRhNC01NjI4ZGU2ZWJjODMucGRm [part]
18. 內政部 [Ministry of the Interior]. (2024a, March 1). *修正「建築物耐震設計規範及解說」部分規定* [Partial amendment of
    the Seismic Design Code for Buildings and Commentary] (台內國字第1130801422號令). Reprinted at
    https://www.ntcaa.org.tw/Content/Files/Bulletin/a6ab1c8dae934518b67dd81d1af81df2.pdf [full]
19. 內政部. (2024b). 老舊建物及救災據點結構與非結構物耐震補強分項推動方案 [Sub-plan for seismic retrofit of old buildings
    and disaster-response sites] (updated 30 Jun 2024) [內政部函].
    https://www.nlma.gov.tw/uploads/files/d917f121eea1049ab9b88ae8af29adbf.pdf [part]
20. 內政部. (2024c). Same sub-plan (updated 18 Oct 2024) [內政部函].
    https://www.nlma.gov.tw/uploads/files/ada3375350bc634759fbf9e73f876c1d.pdf [part]
21. 內政部. (2024d, April 11). 中央地方攜手合作 加速0403震後國內復原工作 [Central and local governments work together to
    speed recovery after the 3 April earthquake] [Press release].
    https://www.moi.gov.tw/News_Content.aspx?n=4&s=314741&sms=9009 [full]
22. 內政部. (2025a, March 31). 0403震災將屆滿周年 中央已協助花蓮縣完成多項家園復原及重建工作 [A year after the 3 April
    earthquake, central government has helped Hualien complete home recovery and rebuilding work] [Press release].
    https://www.moi.gov.tw/News_Content.aspx?n=4&s=326831&sms=9009 [full]
23. 內政部. (2025b). *中華民國一百十三年四月三日震災張貼危險標誌住宅耐震弱層補強補助作業規定* [Rules for weak-storey
    retrofit subsidies for homes tagged dangerous after the 3 April 2024 earthquake] (issued 11 Jun 2024; amended 21
    Aug 2025). https://www.nlma.gov.tw/ch/legislation/regsearch/7043 [full]
24. 行政院 [Executive Yuan]. (2024). 「花蓮地震災後復原重建工作－建築物損毀情形及家園重建」懶人包 [Briefing: Hualien
    earthquake recovery, building damage and home rebuilding]. https://www.ey.gov.tw/File/CF3DE0EFAE85153C?A=C [part]
25. 內政部國土管理署 [National Land Management Agency]. (n.d.-b). *建築物耐震設計規範及解說* [Seismic Design Code for
    Buildings and Commentary: revision list] (page updated 8 May 2025).
    https://www.nlma.gov.tw/ch/legislation/regsearch/175 [full]
26. 內政部國土管理署. (n.d.-c). *建築物實施耐震能力評估及補強方案（公有建築物）* [Programme for seismic evaluation and
    retrofit of buildings (public buildings)] (approved in principle by the Executive Yuan, 28 Dec 2017).
    https://www.nlma.gov.tw/ch/titlelist/areasw/4854 [full]
27. 新北市政府都市更新處 [New Taipei City Urban Renewal Office]. (2024, May). *建築物共用部分修繕補助* [Subsidies for
    repairs to buildings' common parts; slides with seismic retrofit cases].
    https://www.uro.ntpc.gov.tw/Uploads/PageServiceFileGroup/2024-05/f836a6ea-d206-42c4-96c5-aa307a616d97.pdf [part]
28. 國家實驗研究院國家地震工程研究中心 [National Center for Research on Earthquake Engineering, NARLabs]. (2022,
    November 15). *新版建築物耐震設計規範及解說正式上路* [The new seismic design code takes effect] [Press conference
    slides].
    https://www.niar.org.tw/files/file_pool/1/0M319508609981071655/20221115%E6%96%B0%E7%89%88%E5%BB%BA%E7%AF%89%E7%89%A9%E8%80%90%E9%9C%87%E8%A6%8F%E7%AF%84%E6%AD%A3%E5%BC%8F%E4%B8%8A%E8%B7%AFNCREE.pdf [full]
29. 劉勛仁, et al. (2014, August). 設計地震整合系統發展與應用 [Development and application of a design earthquake
    integrated system] [Conference paper]. 中華民國第十二屆結構工程研討會暨第二屆地震工程研討會. Co-authors not read.
    https://seaport.ncree.org/static/pdf/sederes/%E5%8A%89%E5%8B%9B%E4%BB%812014_12NCSE_1126.pdf [part]
30. 中央氣象署地震測報中心 [Central Weather Administration Seismological Center]. (n.d.). *FAQ for earthquake 19: What
    is the classification of earthquake-resistant standards for buildings in Taiwan?*
    https://scweb.cwa.gov.tw/en-US/Guidance/FAQdetail/194 [full]
31. 林靜玟, & 沈寧衛. (2016, July). 九、建築物耐震設計規範未臻完備 [Item 9: The seismic design rules are incomplete].
    In *我國災害防救財源籌措與經費執行成效之探討* [Disaster prevention funding and its results]. 立法院預算中心.
    http://www.ly.gov.tw/Pages/Detail.aspx?nodeid=10344&pid=142778 [full]
32. 楊慧敏. (2020, July). 二、我國建築物耐震、都市更新及危老重建相關規範 [Seismic, urban renewal and dangerous-old-building
    rules]. In *我國建築物之耐震、危老重建及都市更新計畫實施成效探討*. 立法院預算中心.
    http://www.ly.gov.tw/Pages/Detail.aspx?nodeid=43937&pid=198706 [full]
33. 卓庭鈺. (2019, October). 二、辦理國定古蹟屋頂、外牆去漆等修復工程計畫進度未符預期 [Item 2: The national-heritage roof
    and facade repair is behind schedule]. In *監察院107年度單位決算評估報告* [Control Yuan: assessment of the 2018
    accounts]. 立法院預算中心. https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=33500&pid=187600 [full]
34. 鍾俊華. (2020, October). 一、監察院辦理國定古蹟屋頂、外牆去漆等修復工程計畫執行情形未臻理想 [Item 1: The Control
    Yuan's national-heritage roof and facade repair performed poorly]. In *監察院108年度單位決算評估報告* [Control Yuan:
    assessment of the 2019 accounts]. 立法院預算中心.
    https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=44111&pid=202348 (PDF:
    https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~%2FFile%2FAttach%2F202348%2FFile_277454.pdf) [full]
35. 立法院預算中心. (2021, September). 二、國產署及所屬109年度歲出保留逾1,700萬餘元，係2項歷史建物修復及再利用工程延宕所致
    [Item 2: Two historic-building repair and re-use projects delayed]. In *財政部主管109年度單位決算評估報告* [Ministry
    of Finance: assessment of the 2020 accounts].
    https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~/File/Attach/211815/File_19729610.pdf [full]
36. National Institute of Building Sciences. (2019). *Natural hazard mitigation saves: 2019 report* (with the
    earthquake fact sheets). https://nibs.org/wp-content/uploads/2025/04/mitigationsaves2019_complete.pdf;
    https://nibs.org/wp-content/uploads/2025/04/ms_v3_adopts_earthquake.pdf [part]
37. Larrabee, R. D., & Whitman, R. V. (1976). *Costs of reinforcing existing buildings and constructing new buildings
    to meet earthquake codes* (Seismic Design Decision Analysis Report No. 28). Massachusetts Institute of
    Technology. https://nehrpsearch.nist.gov/static/files/NSF/PB259189.pdf [part]
38. Federal Emergency Management Agency. (2021, February 11). *Seismic retrofitting of buildings* [Case study].
    https://www.fema.gov/case-study/seismic-retrofitting-buildings [full]
39. Fung, J. F., et al. (n.d.). *The total costs of seismic retrofits: State of the art* [Author manuscript]. National
    Institute of Standards and Technology. https://pmc.ncbi.nlm.nih.gov/articles/PMC9890378;
    https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=928704 (full author list and year not read) [part]
40. Ministry of Culture. (2015, July 8). *Treasure Hill Art Village*.
    https://www.moc.gov.tw/en/News_Content2.aspx?n=501&s=18329 [part]
41. 財團法人台北市文化基金會藝術村營運部 [Taipei Culture Foundation, Artist Village Department]. (n.d.). *關於藝術村*
    [About the artist villages]. https://www.artistvillage.org/about.php [full]

**Seen, not relied on:**
- ainews24. (2026a, October 17). *Construction cost index Sep 2026 120.26*.
  https://ainews24.info/2026/10/17/construction-cost-index-sep-2026-120-26
- ainews24. (2026b, October 20). *Trade cost monthly Sep 2026: CCI subcategories by trade*.
  https://ainews24.info/2026/10/20/trade-cost-monthly-sep-2026-cci-subcategories-by-trade
- These are AI-written news pages; the claims in row 11 are UNVERIFIED.
