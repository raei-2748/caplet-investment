# MISSION: Laura Gao Strategy Session (Claude Code)

**Team:** Knox Grammar School, Wharton Global High School Investment Competition 2026–27
**Written:** 25 Sep 2026 (Sydney) · **Owner:** Ray (team leader)

Read this whole file before doing anything. It overrides older docs in `docs/` and older configs where they conflict.

---

## 0. Your role and the rules of this session

You are the team's **analyst and sparring partner**, not its ghostwriter.

- **Wharton AI policy:** AI may be used for brainstorming and idea generation, but "AI-generated work may not be submitted as your own" and must be cited. Therefore:
  - DO produce: models, numbers, charts, decision memos, red-team critiques, checklists, and outlines of *arguments*.
  - DO NOT produce: finished IPS, Trading Notes, or Final Report prose written for submission. Students write those.
  - Log every substantive AI contribution in `docs/AI_USE.md`: date, task, and what the humans must verify or rewrite.
- **No architecture expansion.** The repo already has council, governance and lineage layers built for a demo client. Do not add new frameworks, agents or abstraction layers. Build the smallest code that answers the case questions. Judges warn: "Overly technical strategies are not automatically better."
- **Plain language test:** every conclusion must be explainable to Laura (a Wharton Stats grad and author, not a quant) in three sentences.
- **Checkpoints on disk:** write results to files as you go (see §5). Assume your context may be summarised at any time; the files are the memory.
- **When unsure about a fact, flag it as `UNVERIFIED` rather than assuming.**

---

## 1. Canonical client facts (source: `competition/official/2026_27/client_case_laura_gao_2026.pdf`)

| Item | Fact |
|---|---|
| Client | Laura Gao: bestselling graphic novelist (*The Wuhan I Know*, *Messy Roots*), illustrator, entrepreneur, educator; Wharton BS 2018 (Statistics & Information Decisions Mgmt); born Wuhan, raised Texas |
| Timeline convention | Year number = calendar year − 2026. All cash flows occur at the **beginning** of the year. |
| Contributions | **$300,000** at start of 2027 (Y1); **$150,000** at start of 2028 (Y2), funded by advances, speaking, licensing and other ventures |
| No other flows | No additions or withdrawals before 2033. Living expenses are covered outside the portfolio. |
| Operating commitment | **Ten fixed payments of $50,000**, start of each year **2033–2042**. Nominal, NOT inflation-adjusted. Must be funded by the portfolio "with a high degree of certainty". **No reliance** on co-sponsors, grants, fees or outside funding. |
| Operating reserve | At start of 2033, before the first payment, Laura sets aside a reserve. We must recommend its **size, initial composition, how composition changes** as payments are made, **define "high degree of certainty"**, explain how we evaluated it, and state our assumptions. |
| Facility contribution | After setting up the reserve (2033), how much of the remainder she can **responsibly** contribute to the Taiwan residency facility. No predetermined amount. Preserve financial flexibility. We do NOT size a contingency fund's composition. |
| Co-sponsor communication | In **2031** she tells co-sponsors a **dollar range** for her 2033 facility contribution. We state our **confidence** that the actual figure falls in the range, how good and bad markets affect it, and ensure the range **protects the operating commitment**. We also **draft part of the fundraising materials** (students write the final text). |
| Risk attitude | Willing to take thoughtful risks; wants a balance between growth and protecting the capital her goals require. |
| Projections | Start from $300k (2027) + $150k (2028) with reasonable return assumptions. **WInS gains/losses are NOT added to projections.** |
| Ignore | Taxes, legal/regulatory setup in Taiwan, facility total cost, construction budget, funding gap, residency business plan |
| Must address | Assumptions on returns, cash-flow timing, outside funding, **inflation (portfolio projections and facility costs)**, flexibility; favourable and unfavourable outcomes |

## 2. Competition facts

| Deadline (5pm ET) | Deliverable |
|---|---|
| 9 Oct 2026 | Team roster |
| **23 Oct 2026** | **Trading Notes Analysis**: shows how our investment decisions reflected, tested or refined the developing strategy |
| 6 Nov 2026 | Investment Policy Statement |
| 9 Nov 2026 | Final Report instructions released |
| 4 Dec 2026 | Final Report + school documentation |

- Trading began 28 Sep 2026 on WInS. **WInS performance "has little to do with the final outcome."**
- **Rubric (5 categories):** Investment Strategy · Client Knowledge · Portfolio Analysis · Competition Experience · Creativity & Presentation.
- Judges: Wharton students and Aberdeen Investments professionals. Past judges rewarded "clear thoughtfulness and reasoning behind all the decisions", client values, behavioural finance (client emotions in drawdowns), and the client's total financial picture.
- **UNVERIFIED (ask the humans; do not guess):** WInS starting cash ($100k vs $500k); whether ETFs or bond ETFs are tradeable; the approved securities list; position/trade limits. Put these in `decisions/00_open_questions.md`.

## 3. Prior research (read first, don't redo)

- `docs/research_laura_gao_and_wins.md`: professional frameworks (LDI/surplus investing, cash-flow matching, Chhabra risk buckets, funded-status glide paths), yields as of Sep 2026 (10Y ≈ 5.1%, 7Y ≈ 5.05%, TIPS 10Y real ≈ 2.63%), iBonds term Treasury ETFs (maturities to 2036), fundraising signalling literature, Taiwan CPI (~1.8–2.2%), and strategy options A/B/C.
- Key prior numbers (re-derive them in the model; don't trust blindly):
  - PV of the 10 payments at start of 2033: ≈ $439k at 3%, $422k at 4%, $405k at 5%, $500k at 0%.
  - Cost to lock all payments at start of 2027 at ~5.2%: ≈ $297k, almost all of the first contribution.
  - Rough simulation: more equity raises the median 2033 value only modestly but raises P(value < reserve cost) from ~4% (40/60) to ~14% (100% equity).

Only do new web research to fill a specific gap named in a decision memo. Cite sources with URLs.

---

## 4. The work: stage-gated

Complete each stage's outputs before moving on. At the end of each stage, append a 5-line summary to `decisions/LOG.md`.

### Stage 1: Housekeeping (short)
1. Replace the demo client in `config/client_mandate.yaml` with Laura's mandate (§1). Keep the old file as `config/demo_client_mandate.yaml` if it isn't already there.
2. Add the 23 Oct Trading Notes deadline to `config/wharton_public_2026_27.yaml`.
3. Write `decisions/00_open_questions.md` (the unverified items plus anything else only humans can answer).

### Stage 2: The core model (most important output)
Build `model/` (Python, simple, tested, runnable in one command) that:
- Values the liability at any date and yield curve (flat and term-structure versions).
- Simulates portfolio value from 2027 to 2033 (and 2031) for a set of allocations, with **stated, sourced capital-market assumptions** (expected return, volatility, correlations for US equity, international equity, Treasuries, cash, and optionally REITs/TIPS). Use a conservative base case plus bull and bear cases.
- Includes **rate risk**: the reserve cost in 2033 depends on 2033 yields, and simulated bond returns must be consistent with simulated yield changes.
- Implements the three strategies:
  - **A. Lock early:** buy the full Treasury ladder in 2027 (and top it up with 2028 money if needed).
  - **B. Staged hedge:** a hedge-ratio glide path with funded-status triggers (pension style); define the triggers explicitly.
  - **C. Build at 2033:** growth portfolio until 2033, then buy the ladder.
- Outputs for each strategy:
  - P(reserve fully funded)
  - Distribution of the 2033 facility surplus (p5/p10/p25/p50/p75/p90)
  - Expected shortfall
  - Worst historical-style stress results: replay 2008 and 2022, plus a 1970s-style inflation and rates path
- Implements the **2031 → 2033 "announce then protect" rule**: given 2031 portfolio value, compute the range to announce, then move the floor into 2033-maturing Treasuries, and measure P(actual contribution within range).
- Reports facility figures in **nominal and 2027 dollars**, and notes TWD/USD sensitivity (a simple ±15% scenario is enough).
- Has tests: cash-flow timing (beginning of year), PV correctness vs a hand calculation, and reproducible seeds.
- Produces a handful of clean charts in `outputs/charts/laura/`. Fewer is better: one fan chart, one strategy comparison, one funded-ratio glide-path chart.

### Stage 3: Structured debates (one per decision)
For each decision below, run **at most 3 rounds**: Advocate → Opponent → Judge. The Judge scores against the 5 Wharton rubric categories, plays a sceptical Aberdeen portfolio manager, and **must pick a side**. Every debate ends in a written decision.

| # | Decision |
|---|---|
| D1 | Strategy A vs B vs C (use Stage 2 numbers, not intuition) |
| D2 | Definition of "high degree of certainty": a probability threshold plus a mechanism, and why |
| D3 | Reserve composition: individual Treasuries vs iBonds ETFs vs TIPS vs a mix; how it changes 2033–2042 |
| D4 | Growth-portfolio design: asset mix, equity approach (broad index core + stock picks?), how many holdings, role of values alignment (identity, education, community, creators, Taiwan/Asia) without compromising the finance |
| D5 | Facility contribution rule: what % of the post-reserve surplus, and how big a flexibility buffer (and why that number) |
| D6 | 2031 co-sponsor range: which percentiles, the stated confidence, the protect-the-floor mechanism, and how to explain it honestly |
| D7 | How the WInS account represents the strategy given the platform constraints (stocks-only vs ETFs allowed: have a plan for both) |
| D8 | Stress-test the $150k 2028 contribution arriving late or smaller (case says she "will contribute"; decide whether and how to mention it) |

Each memo `decisions/NN_topic.md` contains, in this order:
- The question
- The options
- The evidence, with numbers from `model/`
- The strongest counter-argument
- **Decision**
- What would change our mind
- A three-sentence plain-English version for Laura

### Stage 4: Red team
Write `redteam/judge_review.md`: a harsh review of the whole strategy by (a) an Aberdeen PM, (b) Laura herself, (c) a co-sponsor deciding whether to trust her range. List the top 10 weaknesses with fixes, and check consistency across the three deliverables.

### Stage 5: Deliverable scaffolding (outlines only)
- `deliverables/trading_notes_plan.md`:
  - which trades to make in WInS in the next 3 weeks, and **why each one tests or refines the strategy**
  - the evidence each note should cite
  - a template the students fill in
- `deliverables/ips_outline.md`: section-by-section bullet outline with the numbers to use and their source in `model/`
- `deliverables/final_report_outline.md`: a provisional outline (instructions arrive 9 Nov)
- `deliverables/cosponsor_talking_points.md`: bullet facts only; students write the prose

---

## 5. Output map

```
MISSION.md                      ← this file
config/client_mandate.yaml      ← Laura (Stage 1)
model/                          ← Stage 2 code + tests + README
outputs/charts/laura/           ← ≤ 5 charts
decisions/LOG.md                ← running stage summaries
decisions/00_open_questions.md
decisions/01..08_*.md           ← Stage 3 memos
redteam/judge_review.md         ← Stage 4
deliverables/*.md               ← Stage 5 outlines
docs/AI_USE.md                  ← append log entries
```

## 6. Definition of done
- `model/` runs in one command, tests pass, and every number in `decisions/` traces to it.
- D1–D8 each have a clear decision.
- A student can read `decisions/LOG.md` in 10 minutes and explain the whole strategy.
- Nothing in the repo is finished submission prose.
