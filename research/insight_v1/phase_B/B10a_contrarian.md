# B10a Contrarian: attacking "lock early" from Laura's side

Agent B10a, insight_v1 run, Phase B (question generation). Written 2026-09-27. Lens: Contrarian (attack our own
strategy). Starting angle: **Laura's side.** She "has been willing to take thoughtful risks" and wants "an appropriate
balance between pursuing growth and protecting the capital required for her goals" (R-C37, R-C38). Would she call a
plan that puts ~97% of her first deposit into Treasuries "balance"? Is there a design that keeps the ten payments just
as certain but gives her more upside or more options? The other B10 agent starts elsewhere.

This file is AI-generated research (Claude Code) for Team Caplet, for brainstorming only. It holds questions,
evidence, numbers and checklists. It has **no submission-ready prose**. The six students decide and write every
deliverable in their own words, and must record AI use in the Final Report's Works Cited (R-W46). Laura appears only
through the case and her public professional record. I left out every personal-life detail, including personal
material on pages I opened. Nothing here suggests contacting her (R-W16).

Status labels (brief section 3): **VP** = VERIFIED-PRIMARY (I read it on the primary page on 2026-09-27; URL in
section 6); **VRF** = VERIFIED-REPO-FILE; **SNIP** = SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION; **INT** =
INTERPRETATION (my reading, never a fact); **DER** = derived from the verified simulation with the changes stated
(script in Appendix A; its inputs carry their own labels). Every "hypothesis" below is a **guess**.

Terms used (defined once):
- **Ladder / lock**: buying Treasury bonds that pay out exactly on the ten payment dates, so the payments no longer
  depend on markets.
- **Sleeve / surplus**: the money left after the ladder. It pays for the facility contribution and flexibility.
- **Floor**: part of the sleeve moved into a Treasury maturing just before 2033. It becomes a known minimum facility
  amount.
- **Barbell**: holding only two very different things, safe bonds and stocks, with nothing in between. Here: a bought
  floor plus 100% stocks with the rest.
- **Ratchet**: locking part of a gain on several dates instead of one ("lock in good years").
- **p5 / p50 / p95**: the outcome that 5% / 50% / 95% of simulated paths fall below. p50 is the median.
- **Equity risk premium**: the extra yearly return stocks are expected to earn over safe government bonds.

---

## 0. Summary (read this first)

The attack **mostly fails, and the way it fails is itself the insight.** Three findings change sentences or a design
choice. None of them reopens "lock early vs growth-first" (brief section 8.1).

1. **In 2026, taking risk buys Laura a wider range, not a higher middle.** I tested every Laura-friendly variant I
   could build (DER, Appendix A; payments stay funded in every case where the 2028 deposit arrives):

   | Design (JPM equities, sleeve bonds at 5.0%) | 2033 surplus p5 / p50 / p95 | vs current plan |
   |---|---|---|
   | Current plan (sleeve 60/40, lock 80% of sleeve in a 2-year Treasury in 2031) | $161k / $210k / $277k | - |
   | Sleeve 100% equity | $137k / $214k / $332k | median +$4k, p5 -$24k |
   | Delay the whole lock to Jan 2028 (use both deposits) | $130k / $214k / $331k | median +$4k, p5 -$31k |
   | Stage the 2033-36 rungs to Jan 2028 | $157k / $213k / $293k | median +$3k, p5 -$4k |
   | Ratchet: lock the floor in thirds, 2029/30/31 | $171k / $208k / $259k | median -$2k, p5 +$10k |
   | **Barbell: lock 50% of the sleeve in Jan 2028 in a Treasury maturing before 2033, rest 100% equity** | **$163k / $210k / $293k** | **median same, p5 +$2k, p95 +$16k, floor known 3 years earlier** |
   | All-Treasury (sleeve 0% equity) | $183k / $201k / $222k | median -$9k, p5 +$22k |

   The largest median gain from any extra risk is about **$4k on a ~$210k facility (about 2%)**. Laura's "growth" choice
   this year is really a choice about **spread**: how much p5 she gives up for how much p95.
2. **A second major house says U.S. stocks may not beat today's Treasuries at all.** Vanguard (22 July 2026, model run
   30 June 2026) cut its 10-year expected return for U.S. equities to **4.2%-6.2%** a year (VP). Its midpoint, 5.2%, is
   about the same as the 10-year Treasury yield (5.17%, F-001). Using that midpoint, the sleeve's median is **$201k /
   $204k / $204k** at 0% / 60% / 100% equity. Growth-first's median ($205k) no longer beats lock-early's ($204k), and
   its miss rate rises to 4.5% (DER). The brief's "more equity buys range, not median" (section 8.5) came from one house
   (JPM). **What is new is that a second house removes the median gain entirely.** That gives Laura an honest sentence:
   this year, her growth comes mostly from bond yields.
3. **The one design that beats the current plan without extra risk to the payments is a floor-first barbell.** It
   also matches Laura's documented pattern better than the current plan does. She leapt only after a contract secured
   her base: "So when she got the book deal with HarperCollins, she gave Twitter her notice." (Inverse/Input, 2022, VP).
   Her leap was then total, not 60%. INT: a bought facility floor plus a full-equity remainder is "base first, then
   leap". A 60/40 sleeve is a half-leap. Numbers: same median, slightly better p5, a higher p95, and a floor that is
   known from 2028, not 2031. The cost is a wider 2031 range, because stocks stay at risk until 2033. This needs D3's
   check with fat tails and historical crash sequences before anyone adopts it (Q4, Q17).
4. **Three Laura-side blind spots that change sentences:**
   - **"Balance" must be shown goal by goal.** The whole-portfolio equity share is ~1.5% in 2027, ~20% in 2028-30 and
     ~4% in 2031-32 (DER). Shown as one blended number, it reads as "no growth" (Q3).
   - **What is the firm's fee for?** A 1% fee on all assets cuts the median surplus from $210k to **$177k**. The same
     fee charged on the sleeve only gives **$202k** (DER). A statistics graduate will ask why she pays a manager to hold
     a buy-and-hold ladder (Q1).
   - **Locking at the highest 10-year yield since 2007** (F-004) is a fact she can check, and it deserves a
     pre-commitment against regret: if rates rise 100bp after the lock, the ladder would have cost ~$27k less (F-102)
     (Q16).
5. **The joint tail now has a size.** Suppose the short rungs have to wait until 2028 (because rates fell, or on
   purpose) and the 2028 deposit is **zero**. Then 24-28% of paths leave the payments short by **~$8-10k** on average.
   With a $75k deposit, no path is short (DER, Q7). That answers part of brief section 9's "UNANSWERED" joint tail.

**Top five questions for the next phase:** Q20 (how to choose between designs when the medians are equal), Q4
(barbell), Q2 (two houses), Q3 (balance by goal), Q14 (the all-Treasury rival).

---

## 1. Method

1. Read the brief, v4 Parts 1-3, 5 and 6, CLAUDE.md, the case, the Phase A registers, the WInS week-1 files, and the
   Phase B files that border this lens (B1a, B2a, B4a, B4b, B8a, B8b, B9a, B9b) so that I do not re-ask their
   questions. Where they got there first, I cite them and add only new numbers.
2. Built each design a smart rival or Laura herself might prefer, and ran it on the verified simulation's engine
   (`research/verified_2026-09-27/strategy_mc.py`: same seed, 200,000 paths, same JPM inputs). I changed one thing at a
   time and labelled each change (Appendix A). The baseline reproduces F-401/F-402 exactly ($159k/$207k/$273k; floor
   $127k/$165k/$217k).
3. Fixed one known inconsistency before comparing designs: the sleeve's bonds earn **5.0%**, not JPM's 4.0%. The
   ladder is priced at ~5.1% forwards, and IEF's yield to maturity is 5.17% (F-012, F-203; B9a raised this). This
   lifts the baseline to $161k/$210k/$277k. All design comparisons in this file use this corrected baseline unless
   stated.
4. Web: the WebSearch budget for this session was already used up (200/200 calls). So I read known primary pages
   directly with `fetch_text.py` (Vanguard VCMM, Inverse, Russell) and grep-checked every quote.
5. Filters for each question: (a) would the answer change a decision, a number or a sentence; (b) is it anchored in
   an R-id or F-id; (c) is it not already answered in brief section 8, or else is there new evidence (stated).

---

## 2. The questions (ranked; 19 kept, 6 parked in section 3)

### Q20 (rank 1). When every design has about the same median, what rule should choose between them: the p5 Laura can accept, the p95 she hopes for, the floor co-sponsors can bank, or the simplest structure?
- Anchors: R-C38, R-C37, R-I11, R-S25; F-401, F-407.
- Official words: "she wants her investment team to recommend an appropriate balance between pursuing growth and
  protecting the capital required for her goals." (case p.2, VRF)
- Why it matters (DER, table in the summary): the medians of seven designs sit within $201k-$214k. Their p5 runs
  from $130k to $183k and their p95 from $222k to $332k. The team currently justifies "60% equity" as a middle
  setting. Given how flat the medians are, that is a **choice of spread**, and the case asks the team to recommend it
  ("recommend an appropriate balance").
- Hypothesis (guess): the rule that is most Laura's is "choose the highest bought floor that still leaves a real
  upside". Her documented pattern is a secured base, then a leap (Inverse 2022, VP). The co-sponsor task punishes a
  missed low end, not a missed high end (R-C66). B9a's "affordable loss" framing gives the p5 test; this question adds
  the tie-break: at equal medians, prefer the design with the higher known floor and fewer moving parts.
- Would change: **decision** (the selection rule written in the IPS: one sentence on how the balance was chosen);
  **sentence** (the IPS answer to R-I11 "How does your strategy balance growth, risk…").
- Deliverables: IPS, FR. Specialist: D6 (with D3 for the numbers). Seed: 29.
- North star: Laura sees her own decision rule (secure the base, then leap) turned into the plan's selection rule,
  not a generic "moderate" label.

### Q4 (rank 2). Should the sleeve become a barbell: in January 2028 lock a facility floor in a Treasury maturing just before 2033, and hold the rest 100% in broad equity, instead of a rebalanced 60/40 sleeve plus an 80% lock in 2031?
- Anchors: R-C62 to R-C71, R-C38, F-402, F-206, F-001 (5-year 4.98%).
- Official words: "Rather than promising one exact amount, she wants to communicate a credible range for her
  potential contribution." (case p.3, VRF)
- Evidence (DER; JPM equities; sleeve bonds 5.0%; lock at the 5-year par yield 4.98%, ASM):

  | Share locked in Jan 2028 | Floor (known 2028), median | 2033 surplus p5 / p25 / p50 / p75 / p95 |
  |---|---|---|
  | Current plan (for reference) | floor known only in 2031: $167k median | $161k / $188k / $210k / $235k / $277k |
  | 50% | ~$100k | $163k / $188k / $210k / $238k / $293k |
  | 65% | ~$131k | $175k / $192k / $208k / $227k / $265k |
  | 80% | ~$161k | $186k / $196k / $205k / $216k / $238k |

  With Vanguard-midpoint equities (5.2%): current $157k / $204k / $269k; barbell 50% $159k / $203k / $280k (DER).
- Why the barbell can match the plan (INT): the current plan cuts its stock exposure sharply in 2031 (whole-portfolio
  equity ~4%, Q3). The barbell keeps stocks on less money for longer, with a hard bought floor underneath. This is
  buy-and-hold with a floor versus constant-mix rebalancing, a classic comparison in the asset-allocation literature.
  Perold & Sharpe's "Dynamic Strategies for Asset Allocation" (1988) is the usual reference; I did not open it (lead
  for D3).
- The cost: in 2031 the equity half still has two years of risk. Rough 2031 range (ASM: lognormal JPM, 2-year log sd
  ~21.5%): a low end of "floor + 75% of the 2031 equity value" is missed only if stocks fall more than 25% in two
  years, about 3% of paths. At medians that low end is roughly $100k + 0.75 × ~$96k ≈ $172k, against the current
  plan's ~$167k floor. **To be verified by D3; not yet simulated.**
- Hypothesis (guess): a barbell with 50-65% locked in 2028 weakly beats the current plan on p5 and p95 at the same
  median. It is also simpler to explain (two instruments, each with one job). It needs a 2031 rule for the equity
  part, and it must survive a fat-tailed or historical-sequence test (Q17).
- Would change: **decision** (sleeve structure and floor timing, before the IPS freezes on Nov 6); **number** (FR range
  tables); **WInS-now** (the sleeve's bond slot: Q11).
- Deliverables: WInS-now, TN, IPS, FR. Specialist: D3. Seed: 9.
- North star: a plan that mirrors how Laura actually took her biggest career risk (secure the base, then leap fully)
  is one she would recognise as hers. A 60/40 half-leap is what 6,000 other teams will write.

### Q2 (rank 3). With Vanguard's June-2026 model giving U.S. equities 4.2%-6.2% a year (about today's 10-year Treasury yield) and JPM giving 6.7%, should the FR show both houses, and should the IPS say plainly that this year Laura's growth comes mostly from bond yields, with stocks adding range?
- Anchors: F-301, F-317, F-315, F-004, R-C77 ("reasonable return assumptions"), R-S26.
- Official words: "use reasonable return assumptions consistent with their strategy." (case p.4, VRF)
- New evidence (VP, Vanguard VCMM page dated 22 July 2026, read 2026-09-27): "our 10-year expected annualized return
  for U.S. equities declined from a range of 4.9%–6.9% to a range of 4.2%–6.2%". Developed ex-U.S. 4.5%-6.5%;
  emerging markets "2%–4%". Vanguard also warns that "valuations tend to be poor predictors of performance over the
  short or even intermediate term".
- DER with the Vanguard midpoint (5.2% compound, JPM volatility kept, ASM):
  - lock-early sleeve at 0/60/100% equity: medians **$201k / $204k / $204k**; p5 $183k / $157k / $130k;
  - growth-first: median **$205k**, p5 $5k, **miss 4.5%**; lock-early: $157k / $204k / $269k.
  - Under JPM (bonds 5%): growth-first median $238k vs lock-early $210k, miss 2.7%.
- What is new versus brief section 8.1/8.5: those rest on JPM alone. The second house takes away growth-first's only
  advantage (its median) and removes any median reward for sleeve equity.
- Hypothesis (guess): show a two-house table in the FR, and state the returns as a range, not a point. The decision
  does not change, but the "why" gets stronger and more honest. It is a statistician's move: show that the
  conclusion survives the assumption that matters most.
- Would change: **number** (FR projection tables and assumptions list); **sentence** (IPS risk/return line).
- Deliverables: IPS, FR. Specialist: D2 (with D3). Seed: 26.
- North star: Laura, a statistics graduate, sees a plan that says what it does not know. Rivals quoting one 7-10%
  equity number will look naive next to it.

### Q3 (rank 4). Should the IPS describe "balance" goal by goal (promise: no market risk; facility floor: none after it is bought; upside: full market risk), because the blended whole-portfolio equity share (~1.5% in 2027, ~20% in 2028-30, ~4% in 2031-32) would read to Laura as "no growth"?
- Anchors: R-C37, R-C38, R-I11, R-I12, F-409, R-AN45 ("funding purposes" as diversification).
- Official words: "Although she has been willing to take thoughtful risks throughout her entrepreneurial career, she
  wants her investment team to recommend an appropriate balance" (case p.2, VRF)
- Evidence (DER, medians): 2027 equity = 60% × $7.7k of $300k = **1.5%**. 2028: **20.4%** (matches F-409). 2031 after
  the 80% lock: sleeve ~$187k, 20% of it at 60% equity, against a $356k ladder = **4.1%**.
- Hypothesis (guess): stated per goal, the plan is "full protection where others cannot help, real risk where they
  can" (Q10), which reads as balance. As one blended percentage, it reads as a bond fund. The SMApply page's
  "diversification across … funding purposes" (R-AN45) is the official hook for per-goal language.
- Would change: **sentence** (IPS risk-tolerance and balance sentences; FR allocation chart: show three pots over
  time, not one blended equity line).
- Deliverables: IPS, FR, TN (reflections name the pot each trade serves). Specialist: D9 (with D6). Seed: 1.
- North star: Laura feels her "thoughtful risks" were heard and placed where they belong, rather than ignored.

### Q1 (rank 5). What does Laura pay our firm for when about two-thirds of her money sits in a hold-to-maturity ladder, and should the IPS say that the fee applies to the sleeve only (or is a flat fee)?
- Anchors: R-C26 ("invest $300,000 with an asset management firm"), R-W29 (CFA Asset Manager Code), R-C8, R-S25.
- Official words: "At the beginning of 2027, Laura plans to invest $300,000 with an asset management firm." (case p.2,
  VRF)
- Evidence (DER; ASM: fee paid yearly out of the sleeve; ladder untouched): no fee median $210k; **0.5%** on the sleeve
  only $206k, on all assets $193k; **1.0%** on the sleeve only $202k, on all assets **$177k (-16%)**. A3 found no fee
  assumption anywhere (BS-01) and that the Code requires fee disclosure (F.4.d, VP via A3).
- Hypothesis (guess): a firm that charges a percentage on a buy-and-hold Treasury ladder charges for work it does not
  do. A statistics graduate who ran A/B tests (B9b) will compare against the "control" of buying the ladder herself.
  An honest fee line (sleeve only, or flat) plus a list of what the firm actually does (the 2027 purchase rule, the
  floor rule, the 2031 statement, rebalancing, the co-sponsor numbers) answers "why us" better than any return claim.
- Would change: **sentence** (IPS or FR fee/governance line); **number** (FR surplus tables net of the stated fee).
- Deliverables: IPS, FR. Specialist: D8 (with D10 for the Code). Seed: 1.
- North star: she chooses the firm that is honest about what it earns and why. Almost no team will mention its own fee.

### Q14 (rank 6). Would a rival that holds the whole sleeve in Treasuries (facility fully bought by 2028) beat us on "Investment Strategy", being simpler and more certain, or would judges mark it down for ignoring "pursuing growth"?
- Anchors: R-C38, R-S24, R-S25, R-C73 ("no single correct strategy"), F-409.
- Official words: "Teams may reach different conclusions about risk, asset allocation, liquidity, return
  expectations, funding confidence, the facility contribution, and the financial flexibility Laura should preserve."
  (case p.4, VRF)
- Evidence (DER): all-Treasury sleeve $183k / $201k / $222k (p5/p50/p95), against our $161k / $210k / $277k. Under the
  Vanguard midpoint the all-Treasury median ($201k) is only $3k below ours ($204k). The rival could state an almost
  exact 2033 figure in 2027.
- Hypothesis (guess): the all-Treasury plan is the strongest "attack from safety". It loses on the case's own words:
  "pursuing growth" (R-C38) and "willing to take thoughtful risks" (R-C37). It also nearly removes the uncertainty the
  case asks teams to explain (R-C65, R-C70). Our answer must show *why* we keep some risk: the upside is where
  flexibility "as the project develops" comes from (Q9). "Because the case says growth" is not enough.
- Would change: **sentence** (FR "alternatives considered" section: name this rival and the reason we did not choose
  it); possibly a **decision** if the team finds the reason weak.
- Deliverables: FR (IPS one clause). Specialist: D7 (with D6). Seed: 29.
- North star: showing the rejected safe alternative, and why, proves our risk was a choice made for her.

### Q6 (rank 7). If 80-100% of the sleeve is a bought floor in 2031, the co-sponsor "range" shrinks toward one number. Does that dodge the case's uncertainty task, and should the FR show how the range narrows from the 2027 view to the 2031 view to 2033?
- Anchors: R-C65, R-C67, R-C69, R-C70, R-AN9, R-S28, F-402.
- Official words: "In 2031, however, the value of her portfolio in 2033 remains uncertain." (case p.3, VRF)
- Evidence (DER, JPM, bonds 5%): floor 100% in 2031 gives surplus = floor (a point); floor 80% gives floor $129k /
  $167k / $219k, with the surplus at least 25% above the floor in 58% of paths; floor 50% gives a $104k median floor.
  From 2027, the 2033 outcome spans $161k-$277k (p5-p95).
- Hypothesis (guess): our structure *answers* the uncertainty by buying most of it away. A judge reading only the 2031
  number could still think we skipped it. Showing the funnel (2027: wide; 2031: floor bought, narrow upside; 2033:
  known) makes "how favorable and unfavorable market outcomes could affect the amount" visible. It also fits the
  criterion's "investment uncertainty clearly and credibly" (R-S28).
- Would change: **sentence/chart** (a FR funnel chart; data: p5/p50/p95 by year, from Appendix A); **decision** (floor
  share: 80% vs a lower share that keeps a real range).
- Deliverables: FR. Specialist: D3 (with D9). Seed: 9.
- North star: co-sponsors see the uncertainty shrink on a schedule. That is credibility shown, not claimed.

### Q9 (rank 8). Should the 2031 pledge be tied only to money already bought, with the equity upside labelled as Laura's flexibility money (never promised), so the range cannot be missed at the low end and flexibility grows in good markets?
- Anchors: R-C58, R-C66, R-C71, R-C84, R-AN19, R-I13.
- Official words: "She recognizes that committing all remaining assets could limit her financial flexibility as the
  project develops." (case p.3, VRF)
- Hypothesis (guess): yes. The design then answers two case demands with one split. The bought floor is the credible
  pledge (overpromising becomes impossible at the low end). The unbought upside is the flexibility (R-C58), which is
  largest exactly when markets were kind. It fits her "Always start small" staging (B8a/B8b, VP there): the pledge is
  the first stage, and more can follow "as the project develops". The barbell (Q4) makes this split physical.
- Would change: **decision** (what the 2031 range's top end is made of; whether the top end is "may add" language);
  **sentence** (FR fundraising-draft checklist: verbs "set aside" for the floor, "may add" for upside; BS-05).
- Deliverables: FR (IPS one rule). Specialist: D5 (with D6). Seed: 11.
- North star: Laura never has to un-promise anything, and her upside becomes an option she controls. That is what an
  entrepreneur values.

### Q5 (rank 9). Should the facility floor be built by a ratchet (lock a third of the target each January 2029, 2030, 2031) instead of on one date in 2031, to protect Laura against a crash in the year before she pitches co-sponsors?
- Anchors: R-C62, R-C65, R-C70, F-402, F-318; extends B4a Q16 (not modelled there).
- Official words: "They should explain how favorable and unfavorable market outcomes could affect the amount she can
  provide." (case p.3, VRF)
- New numbers (DER, JPM, bonds 5%, lock rates 4.96/4.94/4.81% ASM from F-001):
  - one-date 2031: surplus $161k / $210k / $277k; floor $129k / $167k / $219k;
  - thirds: surplus **$171k / $208k / $259k**; floor **$137k / $165k / $201k**;
  - after a bottom-decile 2030: floor median **$142k (one date) vs $156k (thirds)**.
- Hypothesis (guess): the ratchet buys +$10k at p5 and +$14k in the "crash just before the pitch" world, for -$2k at
  the median and -$18k at p95. Under a barbell (Q4) the question disappears, since the floor is bought in 2028. So
  decide Q4 first.
- Would change: **decision** (floor timing rule); **number** (FR floor distribution).
- Deliverables: FR (IPS one clause if adopted). Specialist: D3. Seed: 9.
- North star: it protects Laura's good luck as well as her promise, at the moment her credibility is on the line.

### Q7 (rank 10). If the ladder costs more than $300k on purchase day, is "buy the long rungs now, buy the 2033-36 rungs with the 2028 deposit" nearly riskless, and how big is the joint tail if the deposit then fails?
- Anchors: F-111, F-112, F-102, F-107, R-AN35, brief section 9 (joint tail "UNANSWERED").
- Official words: "She will contribute an additional $150,000 at the beginning of 2028" (case p.2, VRF)
- New numbers (DER; ASM: 2027 yield change sd 71bp (F-014), duration of the 2033-36 rungs seen from 2028 5.2-6.4
  years; stock-rate correlation 0 or 0.4):
  - deposit $150k or $75k: payments short in **0%** of paths;
  - deposit $0: short in **24-28%** of paths, average shortfall **$8-10k** (1.6-2.0% of the $500k);
  - done deliberately when the ladder *is* affordable, staging adds only +$3k at the median.
- Hypothesis (guess): the current "longest rungs first, top up in 2028" rule is sound. The joint tail is small and
  can be stated in one line. The rule should be written as a funded-ratio rule, not a price cap (B2a Q4/Q5 made the
  wording point; this adds the size of the tail).
- Would change: **number** (FR risk register: joint tail ~$8-10k in ~1 in 4 zero-deposit paths); **sentence** (IPS
  contingent rule).
- Deliverables: IPS, FR. Specialist: D3 (with D1). Seed: 4.
- North star: the plan names its one residual weakness and its size. Laura's statistics training rewards that.

### Q8 (rank 11). Does any lock timing (for example buying the whole ladder with both deposits in January 2028) give Laura materially more upside?
- Anchors: F-101, F-106, F-110, R-C26, R-C27, brief section 8.1 (new variant only).
- Official words: "For long-term projections, teams should begin with Laura's $300,000 investment in 2027, add the
  $150,000 contribution in 2028" (case p.4, VRF)
- New numbers (DER, ASM as Q7, duration 9.9): a 2028 lock gives median **+$4k**, p95 +$54k, p5 **-$31k**. With a $75k
  deposit, payments are short in 0.6-1.6% of paths; with $0, in 37-39% (average short $24-29k).
- What is new: brief 8.1 compared growth-first to 2033 and partial locks with no deposit. This tests the one-year
  delay *with* the deposit. It still buys almost no median.
- Hypothesis (guess): no. The equity risk premium over 5% Treasuries is too thin to pay for a year's delay. Keep one
  FR sentence ("we tested waiting a year; it adds ~$4k at the median and puts the payments at risk if the deposit
  fails").
- Would change: **sentence** (FR alternatives considered). Confirms the decision.
- Deliverables: FR. Specialist: D3. Seed: 4.
- North star: shows Laura we tried to find her more upside before recommending safety.

### Q11 (rank 12). In WInS, should the "short Treasury in the growth money" slot be a defined-maturity fund ending December 2032 (the facility date) rather than a 1-3 year Treasury fund, so every holding has a job tied to a date?
- Anchors: F-206, R-AN45, R-C88, R-T (the guide's example note ties the bond to the commitment), G-ids in
  `wins_week1_guardrails.md` (position limit).
- Official words (Trading Notes guide example): "an intermediate-term U.S. Treasury bond ETF to reduce portfolio
  volatility and begin preparing for Laura's future operating commitment" (VRF)
- Candidates (**PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading**; this season:
  listed in WInS and within the Session Rules position limit):
  - Primary: **IBTM**, iShares iBonds Dec 2032 Term Treasury ETF. Per S1 (VP there, 2026-09-24/25): 15 notes maturing
    Apr-Sep 2032, effective duration 5.05y, YTM 5.09%, 0.07% fee, $555m, ~216k shares/day. **Not** on the 2025-26 list
    (historical only).
  - Alternate 1: a Treasury note or principal STRIP maturing in late 2032 (bonds are a permitted type, R-W; S1 lists
    CUSIPs; $10 commission).
  - Alternate 2: keep **VGSH** (the current ticket; on the 2025-26 list, line 1113, VRF). Weaker date story.
- Hypothesis (guess): if the team adopts a floor bought early (Q4) or keeps the 2031 floor as a dated bond, a
  Dec-2032 holding makes the WInS book show three dated jobs: payments (IEF/TLH), facility floor (Dec 2032), upside
  (VT). The equity weight stays at ~17-20%. Watch the overlap: IBTM also funds the Jan 2033 payment rung in S1's ladder
  map.
- Would change: **decision** (WInS-now: one security swap before notes are written); **sentence** (a TN candidate
  about the facility floor).
- Deliverables: WInS-now, TN. Specialist: D1 (with D10). Seed: null.
- North star: every holding answers "which of Laura's dates is this for?", which is the question she will ask.

### Q16 (rank 13). Should the plan state that it locks at the highest 10-year Treasury yield since 2007, and pre-commit to no regret if rates rise after the lock?
- Anchors: F-004, F-003, F-102, F-007.
- Evidence: 10-year 5.18% on 2026-09-24, the highest close since 2007-07-06 (F-004, VP). If rates rise 100bp after
  the purchase, the same ladder would have cost $264,890 instead of $292,264 (F-102): a "regret" of ~$27k that is
  invisible to the payments. The Fed's longer-run funds-rate median is 3.2% (F-007, VP).
- Hypothesis (guess): Laura's regret rule is "you're always going to regret not doing it" (Overachiever 2021, VP via
  B8a). Locking at a 19-year high fits it. Writing the no-regret rule down in advance stops a 2027 wobble if rates keep
  rising. One checkable fact beats a forecast.
- Would change: **sentence** (a TN reflection on the first hedge trade; the IPS "why now").
- Deliverables: TN, IPS. Specialist: D1 (with D6). Seed: 26.
- North star: gives Laura a fact she can check and a rule that protects her from second-guessing, not a rate forecast.

### Q12 (rank 14). Should the WInS hedge be built in two dated steps under a rule written in advance (for example half now, half on a set date or if the 10-year falls below a stated level), so the Trading Notes rehearse Laura's January-2027 lock decision and show a strategy "tested or refined", without inventing a decision?
- Anchors: R-C88, R-AN40, R-AN43, F-111, F-112, R-W73.
- Official words: "This shows how selected investment decisions reflected, tested, or refined the team's developing
  strategy." (case p.4, VRF)
- Hypothesis (guess): the current ticket buys everything in one session. That is correct economically, but it gives
  three notes that say the same thing. Laura's real problem is rate risk *before* the lock (the ladder cost more than
  $300k on 173 of 185 days in 2026, F-111), so a pre-written two-step rule is not a gimmick: it is the January rule in
  miniature. Risks: day-trading ban, position limit, and making a move for the sake of notes (B8a "No more gimmicks").
  The test: would the team make the split if notes did not exist?
- Would change: **decision** (WInS-now order plan); **sentence** (TN note 1-2 content).
- Deliverables: WInS-now, TN. Specialist: D10 (with D7). Seed: null.
- North star: the notes show Laura's hardest real decision practised in public, not a one-click portfolio.

### Q10 (rank 15). Should the IPS justify where the risk sits with the case's own asymmetry: outside money may fill a facility shortfall but never an operating shortfall?
- Anchors: R-C44, R-C48, R-AN6, R-I13, BS-17 (funders underfund operations).
- Official words: "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this
  requirement." (case p.3, VRF) and "Any remaining facility cost … may come from co-sponsors, grants, collaborators,
  program fees, continued business income, or other sources." (case p.3, VRF)
- Hypothesis (guess): "risk sits only where others can help" is a one-clause, case-derived reason for the whole
  architecture. It turns "lock early" from a technique into a reading of Laura's situation. R-AN6 notes the asymmetry,
  but no file uses it as the justification for *where the risk sits*.
- Would change: **sentence** (IPS principle; pitch candidate content).
- Deliverables: IPS, FR. Specialist: D9 (with D5). Seed: 5.
- North star: the plan's logic comes from her case, not from a textbook.

### Q25 (rank 16). Is part of "pursuing growth" growth of what the residency can raise, since a bought, credible floor may pull in co-sponsor money, and should the IPS say so without overclaiming?
- Anchors: R-C64, R-C38, brief section 8.17 (seed-money effect = mechanism, not prediction).
- Official words: "A meaningful personal contribution may signal that the residency is financially viable,
  demonstrate Laura's commitment to the project, and make potential co-sponsors more willing to contribute." (case p.3,
  VRF)
- Hypothesis (guess): yes, as a *mechanism* only (brief 8.17). A floor that cannot be missed is worth more to
  co-sponsors than an expected value that might be. So certainty is itself a growth tool for the project. The risk is
  that this becomes the fancy framing last year's lesson warns against. Keep it to one clause.
- Would change: **sentence** (IPS balance sentence; FR fundraising checklist).
- Deliverables: IPS, FR. Specialist: D5 (with D6). Seed: 1.
- North star: reframes Laura's "growth" as growth of her residency, which is what she actually wants to grow.

### Q13 (rank 17). A pension at ~152% funded grows its surplus with no spending date. Laura's surplus has a date (2033) and a public promise (2031). Is the right professional analogue a pension "surplus glidepath" or a dated floor-plus-upside, and which would a judge recognise?
- Anchors: brief section 8 (pension logic accepted), F-117, B9a Q1 (152%), B4b (Russell 2026).
- Evidence (VP, Russell Investments, July 2026): "lock down the benefits promised, then grow surplus assets with a
  prudent process and disciplined understanding of risk."
- Hypothesis (guess): Russell's phrase fits the promise half. The pension analogue under-serves the surplus, because
  a pension's surplus has no deadline and no audience. Laura's does, which is exactly why a dated floor (Q4/Q5) is
  needed. One FR sentence on "where we depart from pension practice, and why" is a strong Client Knowledge signal.
- Would change: **sentence** (FR professional-practice paragraph).
- Deliverables: FR. Specialist: D8. Seed: 26.
- North star: shows the team knows the professional template and where Laura differs from it.

### Q17 (rank 18). Do the barbell's and ratchet's advantages survive fat tails and real crash sequences (2000-02, 2008, 2022), or are they artefacts of the i.i.d. lognormal model?
- Anchors: brief section 11 (model gaps), F-316, F-318.
- Hypothesis (guess): the barbell's p5 should hold or improve (its floor is bought regardless of path). Its p95 depends
  on long bull runs. The 60/40 sleeve's rebalancing does better in choppy, mean-reverting markets. A block bootstrap
  on historical U.S. equity/Treasury returns would settle it.
- Would change: **decision** (adopt the barbell or not, Q4); **number** (FR tables).
- Deliverables: FR (IPS decision). Specialist: D3. Seed: null.
- North star: a statistics graduate trusts a design that was tried on history, not only on a smooth model.

### Q18 (rank 19). Which single Laura-specific claim would make a judge who has read 50 "lock + growth sleeve" plans say ours is different, and can it be stated as one checkable fact?
- Anchors: R-S24 ("clear and creative investment thesis"), R-S25, BS-10 (rivals may converge), R-C8.
- Official words: "Your team hopes to develop the investment strategy that Laura ultimately chooses" (case p.1, VRF)
- Candidates (INT): (a) "the co-sponsor floor is bought in 2028, so the low end of the range cannot be missed"
  (needs Q4); (b) "we show two return houses and our conclusion survives both" (Q2); (c) "risk sits only where others
  can help" (Q10); (d) "our fee does not touch the promise" (Q1).
- Hypothesis (guess): (a) or (c). Each is checkable, comes from the case and matches her pattern. (b) and (d) are
  supporting evidence.
- Would change: **sentence** (pitch content checklist; IPS thesis line).
- Deliverables: IPS, FR. Specialist: D7. Seed: 29.
- North star: this is the North Star itself: one reason Laura can repeat to a co-sponsor.

---

## 3. Parked (logged, not carried forward)

- **Seed 5 (the 2033 ordering "before making the first operating payment or contributing to the facility").** Under
  lock-early the ladder *is* the reserve, so the order is met automatically. Brief 8.9 already reconciles "funded 2027,
  set aside 2033" in one sentence. No decision changes. Q10 uses the priority idea instead.
- **WInS mirror at the literal 2027 book vs the post-2028 target.** B1a Q1 owns it. New evidence for B1a: the plan's
  whole-portfolio equity share is ~1.5% / ~20% / ~4% in 2027 / 2028-30 / 2031-32 (DER, Q3). So the WInS ticket's
  ~20% VT matches only the 2028-30 window. That is fine if the notes say which year the book represents.
- **Is a small facility (~$11k with no 2028 deposit) still "responsible"?** Brief 8.8 settled it ("correct failure
  mode").
- **Whether a broad index is "thoughtful risk" or "no view".** Folded into Q3 and Q20. Both houses rank developed
  ex-U.S. at or above U.S. (JPM EAFE 7.5% vs U.S. 6.7%, F-301/F-303; Vanguard 4.5%-6.5% vs 4.2%-6.2%, VP), which
  supports the global fund already in the ticket. No change.
- **Designers' intent from the case PDF date (2026-09-10).** B2a found it (the ladder cost > $300k almost all year).
  Q7 adds the tail size; not re-asked.
- **Post-2033 use of flexibility money (option to expand vs buffer).** B9a Q8 and B4a Q17 own it; Q9 adds only the
  "unbought upside = flexibility" link.

---

## 4. Evidence found in this pass (with status)

| # | Fact | Value | Status | Source |
|---|---|---|---|---|
| E1 | Vanguard 10-year U.S. equity expected return | 4.2%-6.2% a year (down from 4.9%-6.9%); VCMM run 30 June 2026; page dated 22 July 2026 | VP | Vanguard VCMM page (section 6) |
| E2 | Vanguard developed ex-U.S. / emerging | 4.5%-6.5% / 2%-4% | VP | same |
| E3 | Vanguard caveat | "valuations tend to be poor predictors of performance over the short or even intermediate term" | VP | same |
| E4 | Laura's leap after a secured base | "So when she got the book deal with HarperCollins, she gave Twitter her notice." (reporter's account) | VP (re-grepped by me) | Inverse/Input, 2022-03-07 |
| E5 | Russell surplus glidepath | "lock down the benefits promised, then grow surplus assets with a prudent process and disciplined understanding of risk." | VP (re-grepped by me) | Russell Investments, July 2026 |
| E6 | Baseline reproduction | $159k/$207k/$273k; floor $127k/$165k/$217k | VRF (same as F-401/F-402) | Appendix A, section A |
| E7 | Corrected baseline (sleeve bonds 5.0%) | $161k/$210k/$277k; floor $129k/$167k/$219k | DER | Appendix A, B/D |
| E8 | Design table (summary item 1) | see summary | DER | Appendix A, B-K |
| E9 | Vanguard-midpoint results | L sleeve 0/60/100%: medians $201k/$204k/$204k; G median $205k, miss 4.5% | DER (ASM: JPM vol kept) | Appendix A, C and G |
| E10 | Ratchet vs one date | p5 $171k vs $161k; bad-2030 floor median $156k vs $142k | DER | Appendix A, E |
| E11 | Joint tail (short rungs wait, deposit $0) | 24-28% of paths short, mean $8-10k; $0 short at a $75k deposit | DER (ASM rate vol/duration/correlation) | Appendix A, F |
| E12 | Lock delayed to 2028 | median +$4k, p5 -$31k; 0.6-1.6% miss at $75k, 37-39% at $0 | DER | Appendix A, I |
| E13 | Fee drag | 1% on all assets: median $177k; on the sleeve only: $202k | DER (ASM fee mechanics) | Appendix A, H |
| E14 | Whole-portfolio equity share at medians | 1.5% (2027), 20.4% (2028), 4.1% (2031) | DER | Appendix A, J |
| E15 | Barbell | 50% locked 2028: $163k/$210k/$293k, floor ~$100k known in 2028 | DER (ASM 5y 4.98%) | Appendix A, K |
| E16 | IBTM facts | Dec 2032 iBonds; duration 5.05y; YTM 5.09%; $555m; ~216k sh/day; not on the 2025-26 list | VP per S1 (not re-opened by me); list VRF | `wins_now/S1_treasury_sleeve.md` section 1c |

Not reached: WebSearch (session budget spent, 200/200); Perold & Sharpe (1988) not opened; the JPM 2027 LTCMA is not yet
out (F-315).

---

## 5. Leads for the specialists

- **D3 (quant):**
  1. Add three designs to the verified model: barbell (lock X% of the sleeve in Jan 2028 to Dec 2032), ratchet
     (thirds 2029-31), and the current plan. Report p5/p25/p50/p75/p95 and the 2031 range + confidence for each
     (Q4, Q5, Q6).
  2. Fix the sleeve-bond yield to ~5% (B9a flag; E7).
  3. Run the Vanguard midpoint and range ends (4.2%/6.2%) next to JPM (Q2).
  4. Replace i.i.d. lognormal draws with a historical block bootstrap (Q17).
  5. Simulate the barbell's 2031 range rule (low end = floor + 75% of the equity value?) and its miss rate.
  Code base: Appendix A.
- **D2 (equity):** Vanguard VCMM page (E1-E3). Check whether Vanguard publishes a U.S. Treasury 10-year figure on the
  same run (the interactive table did not load as text). Check GMO/AQR/Research Affiliates 2026 numbers only if they
  change the "range, not median" conclusion.
- **D6 (client psychology):** the Inverse 2022 line (E4) plus B8a's regret quote (Overachiever 2021) are the
  Laura-side evidence for "secured base, then a full leap" (Q4, Q16, Q20). Do not use the surrounding personal
  material on the Inverse page (privacy rule).
- **D8 (practice):** fee practice for LDI/ladder mandates vs balanced mandates (Q1); Russell July 2026 (E5); where a
  dated surplus departs from pension practice (Q13); Perold & Sharpe 1988 for buy-and-hold vs constant-mix (Q4).
- **D1/D10 (rates, compliance):** IBTM availability in WInS, and the position limit when IBTM also serves the Jan 2033
  payment rung (Q11). Also a two-step hedge rule that respects the day-trading ban (Q12).
- **D5 (co-sponsors):** does a floor "set aside since 2028" read as stronger than "set aside in 2031"? Wording tiers
  "set aside" vs "may add" (Q9; A3 BS-05).
- **D7 (competition):** whether past Top-50 IPSs used "safe bucket + growth bucket" wording (tests BS-10 and Q18).

---

## 6. Sources (all accessed 2026-09-27)

| Source | URL / path | Status |
|---|---|---|
| Vanguard, "Vanguard Capital Markets Model® forecasts", 22 July 2026 | https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html | VP (phrases grep-verified 13:10 UTC) |
| Input/Inverse, feature on Laura Gao, 2022-03-07 | https://nc.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel | VP (one sentence grep-verified; personal content ignored) |
| Russell Investments, pension surplus article, July 2026 | https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html | VP (phrase grep-verified) |
| Overachiever Magazine interview, 2021-03-15 (regret quote) | https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid | VP per B8a (not re-opened) |
| Case, IPS guide, TN guide, SMApply page | `competition/official/2026_27/` | VRF |
| Case PDF metadata (created 2026-09-10) | `Laura_Gao_2026_Client_Profile.pdf`, read with pypdf | VRF |
| Verified model | `research/verified_2026-09-27/strategy_mc.py` | VRF |
| Phase A registers | `research/insight_v1/phase_A/*.md` | run files |
| Phase B neighbours | B1a, B2a, B4a, B4b, B8a, B8b, B9a, B9b in `research/insight_v1/phase_B/` | run files |
| WInS week-1 files | `research/insight_v1/wins_now/` (S1, S3, S4) | run files |
| 2025-26 ETF list (historical only) | `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` line 1113 (VGSH) | VRF |

---

## Appendix A. Script (run from the repo root; not saved as a separate file because this agent may write only this file)

Save as `research/insight_v1/scripts/B10a_contrarian_checks.py` if the main loop wants it kept. Run with
`.venv/bin/python research/insight_v1/scripts/B10a_contrarian_checks.py` (about a minute).

```python
"""B10a contrarian checks (scratch; code copied into phase_B/B10a_contrarian.md appendix).
Inputs: same as research/verified_2026-09-27/strategy_mc.py (VERIFIED-REPO-FILE: ladder $292,264, 2y 4.81%,
JPM LTCMA 2026 US large cap 6.70/7.94/16.47, intermediate Treasuries 4.00/4.06/3.48, rho -0.01).
New inputs: Vanguard VCMM 30 Jun 2026 U.S. equities 10y 4.2-6.2% (VERIFIED-PRIMARY, midpoint 5.2% used, ASSUMPTION
that JPM vol applies); sleeve bonds at 5.0% (ASSUMPTION ~ today's forward/yields F-012/F-203); par yields 3y 4.94,
5y 4.98 (F-001); 10y yield vol 71bp/yr (F-014); rung costs F-107. Run: .venv/bin/python B10a_checks.py
"""
import numpy as np
P, SEED = 200_000, 20260927
LAD = 292_264; LONG = 155_408; SHORT = 136_856   # F-107: 2037-42 and 2033-36 rungs at 2027-01-01
def lp(c, a):
    return np.log(1 + c), np.sqrt(2 * np.log((1 + a) / (1 + c)))
def draws(eq_c=0.067, eq_a=0.0794, bd_c=0.04, bd_a=0.0406, rho=-0.01, seed=SEED):
    rng = np.random.default_rng(seed)
    z1 = rng.standard_normal((P, 6)); z2 = rng.standard_normal((P, 6)); z3 = rng.standard_normal((P, 6))
    EQ = lp(eq_c, eq_a); BD = lp(bd_c, bd_a)
    zb = rho * z1 + np.sqrt(1 - rho**2) * z2
    return np.exp(EQ[0] + EQ[1] * z1) - 1, np.exp(BD[0] + BD[1] * zb) - 1, z1, z3
def pct(x, ps=(5, 25, 50, 75, 95)):
    return [int(round(np.percentile(x, p), -3) / 1000) for p in ps]
def lock_early(req, rbd, eq_w=0.6, floor_share=0.8, dep=150_000, y2=0.0481, ratchet=None, start=None):
    s = np.full(P, 300_000.0 - LAD if start is None else start)
    locked = np.zeros(P)
    for y in range(6):                   # 2027..2032
        if y == 1: s = s + dep
        if ratchet is not None and y in ratchet:          # lock share of CURRENT sleeve into Treasury maturing 2033
            share, rate = ratchet[y]
            amt = share * s; s = s - amt; locked = locked + amt * (1 + rate) ** (6 - y)
        if ratchet is None and y == 4:
            amt = floor_share * s; s = s - amt; locked = locked + amt * (1 + y2) ** 2
        s = s * (1 + eq_w * req[:, y] + (1 - eq_w) * rbd[:, y])
    return locked + s, locked
req, rbd, z1, z3 = draws()
print("A. Baseline reproduce (JPM, bonds 4.0%):", pct(lock_early(req, rbd)[0]), "floor", pct(lock_early(req, rbd)[1], (5, 50, 95)))
reqB, rbdB, _, _ = draws(bd_c=0.05, bd_a=0.0506)
print("B. Sleeve bonds at 5.0% (forward-consistent):")
for w in (0.0, 0.6, 1.0):
    print(f"   eq {w:.0%}: surplus p5/25/50/75/95 {pct(lock_early(reqB, rbdB, eq_w=w)[0])}")
reqV, rbdV, _, _ = draws(eq_c=0.052, eq_a=0.052 + (0.0794 - 0.067) * 1.0, bd_c=0.05, bd_a=0.0506)
print("C. Vanguard midpoint equities 5.2% compound, bonds 5.0%:")
for w in (0.0, 0.6, 1.0):
    print(f"   eq {w:.0%}: surplus {pct(lock_early(reqV, rbdV, eq_w=w)[0])}")
print("D. Floor share x sleeve equity (JPM equities, bonds 5.0%): surplus p5/25/50/75/95 | floor p5/50/95 | 2031 range width p50 (surplus p95 - floor p5 proxy)")
for fs in (0.5, 0.8, 1.0):
    for w in (0.6, 1.0):
        sur, fl = lock_early(reqB, rbdB, eq_w=w, floor_share=fs)
        print(f"   floor {fs:.0%} eq {w:.0%}: {pct(sur)} | floor {pct(fl,(5,50,95))} | P(surplus>=1.25*floor) {np.mean(sur>=1.25*fl):.2f}")
print("E. Ratchet vs one-date lock (both lock 80% of the sleeve by 2031, eq 60%, bonds 5.0%):")
one, fl1 = lock_early(reqB, rbdB)
# lock 1/3 of the target each Jan 2029, 2030, 2031 (shares of current sleeve that give 80% cumulative if no returns)
rat = {2: (0.8 / 3 / 1.0, 0.0496), 3: ((0.8 / 3) / (1 - 0.8 / 3), 0.0494), 4: ((0.8 / 3) / (1 - 1.6 / 3), 0.0481)}
two, fl2 = lock_early(reqB, rbdB, ratchet=rat)
print("   one-date 2031: surplus", pct(one), "floor(2031)", pct(fl1, (5, 50, 95)))
print("   thirds 2029/30/31: surplus", pct(two), "floor(2031)", pct(fl2, (5, 50, 95)))
# crash-in-2030 conditional: equity return in 2030 (y=3) below its 10th percentile
bad = req[:, 3] < np.percentile(req[:, 3], 10)
badB = reqB[:, 3] < np.percentile(reqB[:, 3], 10)
print("   given a bottom-decile 2030: one-date floor p50", int(np.median(fl1[badB]) / 1000), "k; thirds floor p50", int(np.median(fl2[badB]) / 1000), "k")
print("F. Staged lock: 2027 buy only 2037-42 rungs; 2033-36 rungs bought Jan 2028 (deposit + sleeve).")
D_SHORT = 5.2   # ASSUMPTION: approx duration of 2033-36 rungs seen from 2028 (5-8y zeros, PV-weighted ~6.4y); test 6.4 too
for dur in (5.2, 6.4):
  for corr in (0.0, 0.4):
    for dep in (150_000, 75_000, 0):
        dy = 0.0071 * (corr * z1[:, 0] + np.sqrt(1 - corr**2) * z3[:, 0])   # 2027 yield change; +corr: stocks down, yields down
        cost28 = SHORT * 1.045 * np.exp(-dur * dy)
        s = (300_000 - LONG) * (1 + 0.6 * reqB[:, 0] + 0.4 * rbdB[:, 0]) + dep
        short_fall = np.maximum(cost28 - s, 0)
        s = np.maximum(s - cost28, 0)
        for y in range(1, 6):
            if y == 4:
                fl = 0.8 * s; s = s - fl
            s = s * (1 + 0.6 * reqB[:, y] + 0.4 * rbdB[:, y])
        sur = fl * 1.0481**2 + s
        base, _ = lock_early(reqB, rbdB, dep=dep)
        print(f"   dur {dur} corr {corr} dep {dep//1000}k: P(payments short) {np.mean(short_fall>0):.3f}, mean short ${short_fall[short_fall>0].mean() if (short_fall>0).any() else 0:,.0f}; surplus p5/50/95 {pct(sur,(5,50,95))} vs lock-all {pct(base,(5,50,95))}")
print("G. Growth-first vs lock-early median gap under JPM vs Vanguard equities (G = 75% eq to 2030, then 60/40; reserve at flat 5.26% +/- 1pp)")
def growth_first(req, rbd, dep=150_000, seed=SEED):
    rng = np.random.default_rng(seed + 1)
    rate = 0.0526 + 0.01 * rng.standard_normal(P)
    res = sum(50_000 / (1 + rate) ** t for t in range(10))
    v = np.full(P, 300_000.0)
    for y, w in enumerate((0.75, 0.75, 0.75, 0.75, 0.6, 0.4)):
        if y == 1: v += dep
        v *= 1 + w * req[:, y] + (1 - w) * rbd[:, y]
    return v - res
for nm, (a, b) in {"JPM eq, bonds 4%": (req, rbd), "JPM eq, bonds 5%": (reqB, rbdB), "Vanguard 5.2% eq, bonds 5%": (reqV, rbdV)}.items():
    g = growth_first(a, b); l = lock_early(a, b)[0]
    print(f"   {nm}: G miss {np.mean(g<0):.3f}; G p5/50/95 {pct(g,(5,50,95))}; L p5/50/95 {pct(l,(5,50,95))}")
print("H. Fee drag: 0.5%/1.0% a year on the sleeve only vs on all assets (ladder fee paid from sleeve)")
for fee in (0.005, 0.01):
    s = np.full(P, 300_000.0 - LAD); lad = LAD
    s2 = s.copy()
    for y in range(6):
        if y == 1: s = s + 150_000; s2 = s2 + 150_000
        if y == 4: fl = 0.8 * s; s = s - fl; fl2 = 0.8 * s2; s2 = s2 - fl2
        r = 1 + 0.6 * reqB[:, y] + 0.4 * rbdB[:, y]
        s = s * r * (1 - fee)                                # fee on sleeve only
        s2 = s2 * r - fee * (s2 + lad + (fl2 if y >= 4 else 0)); lad *= 1.0508  # fee on all assets, from sleeve
        if y >= 4: fl = fl * 1.0481; fl2 = fl2 * 1.0481
    print(f"   fee {fee:.1%}: sleeve-only median {int(np.median(fl+s)/1000)}k; all-assets median {int(np.median(fl2+s2)/1000)}k")
print("I. Delay the whole lock to Jan 2028 (2027: all $300k at 60/40), ladder bought with both deposits; dur 9.9, dy sd 71bp")
for corr in (0.0, 0.4):
    for dep in (150_000, 75_000, 0):
        dy = 0.0071 * (corr * z1[:, 0] + np.sqrt(1 - corr**2) * z3[:, 0])
        cost28 = 306_077 * np.exp(-9.9 * dy)
        s = 300_000 * (1 + 0.6 * reqB[:, 0] + 0.4 * rbdB[:, 0]) + dep
        short = np.maximum(cost28 - s, 0); s = np.maximum(s - cost28, 0)
        for y in range(1, 6):
            if y == 4: fl = 0.8 * s; s = s - fl
            s = s * (1 + 0.6 * reqB[:, y] + 0.4 * rbdB[:, y])
        sur = fl * 1.0481**2 + s
        base, _ = lock_early(reqB, rbdB, dep=dep)
        print(f"   corr {corr} dep {dep//1000}k: P(short) {np.mean(short>0):.3f} mean short ${short[short>0].mean() if (short>0).any() else 0:,.0f}; surplus p5/50/95 {pct(sur,(5,50,95))} vs lock-2027 {pct(base,(5,50,95))}")
print("J. Whole-portfolio equity share at medians: 2027, 2028-30, 2031-32")
s28 = (300_000 - LAD) * 1.05 + 150_000
print(f"   2027: {0.6*(300_000-LAD)/300_000:.1%}; 2028: {0.6*s28/(306_077+s28):.1%}; 2031: sleeve~{s28*1.057**3:,.0f}, equity share {0.6*0.2*s28*1.057**3/(356_384+s28*1.057**3):.1%}")
print("K. Barbell: Jan 2028 lock share X of the sleeve in a Treasury maturing Jan 2033 (5y par 4.98%), rest 100% equity to 2033")
for eqset, (a, b) in {"JPM": (req, rbdB), "Vanguard mid": (reqV, rbdV)}.items():
    base, _ = lock_early(a, b)
    print(f"   [{eqset}] current plan (60/40, 80% floor 2031): p5/25/50/75/95 {pct(base)}")
    for X in (0.5, 0.65, 0.8):
        s28 = (300_000 - LAD) * (1 + 0.6 * a[:, 0] + 0.4 * b[:, 0]) + 150_000
        fl = X * s28 * 1.0498 ** 5
        e = (1 - X) * s28
        for y in range(1, 6): e = e * (1 + a[:, y])
        sur = fl + e
        print(f"   [{eqset}] X={X:.0%}: floor known in 2028 p50 {int(np.median(fl)/1000)}k; surplus {pct(sur)}; P(below plan median 210k) {np.mean(sur<210_000):.2f}")
```

Printed results (2026-09-27 run, seed 20260927, 200,000 paths): the summary table, Q2, Q4, Q5, Q7, Q8, Q1 and Q3
numbers above are copied from this output unchanged.

---

## What this teaches

1. **Attack your own plan with the client's words, not only with rival models.** "Is this balance?" is a sharper
   test than "is this optimal?". Here it showed that the plan was right, but that we had been *describing* it wrongly
   (one blended equity number instead of three jobs).
2. **When expected returns are close together, risk choices are about spread, not about the average.** In 2026 safe
   bonds pay about what stocks are expected to pay. Extra stocks mostly widen the range of outcomes. Say this out
   loud rather than implying that stocks add growth.
3. **Check an important assumption against a second independent source.** JPM and Vanguard disagree by about 1.5
   points on U.S. stocks. A conclusion that survives both is one you can defend. One that needs the higher number is
   a bet.
4. **The simplest structure can be as good as the clever one.** A bought floor plus stocks (a barbell) did as well as
   a rebalanced mix plus a later lock, and it is easier to explain. Complexity has to earn its place, even inside a
   good plan.
