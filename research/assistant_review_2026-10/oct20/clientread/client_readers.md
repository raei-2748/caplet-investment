# Three simulated readers of Caplet's plan: the client and two prospective co-sponsors (Tue 20 Oct 2026)

> **Also (`oct20/verify_cosponsor/verify_cosponsor.md`, 20 Oct):** "the evidence says matching adds little" is wrong (matching raised giving in two US tests; only larger ratios added nothing) - the reason for "no matching offer" is the design, not the evidence; drop the "donor-tested message" label and slogan at the US-funder row (Gneezy 2014 supports it by analogy only); "central value" is INFERENCE, not Du et al.; public grants are paid by stage with final settlement against receipts. **Consistency fix 20 Oct (packaudit §1d):** 3r = about 0.6% short on the agreed engine (0.08/0.32/0.72% marked at market); never quote 0.02%.


> **Verified 20 Oct (`oct20/verify_charts_cr/verify_charts_cr.md`): model numbers and case quotes confirmed; citation fixes apply.** Many co-sponsor (CO) line numbers are wrong (content right; corrected list in the verifier R22). "risk-free" does not occur in V5; "stays with Laura" and "so she cannot miss the range" are in older tabs, not V5:23-30; "the artists" is at V5:57-59, 151, 195, 238, 273; "guaranteed" at V5:185, 213, 233; the notes:339 "quote" is a paraphrase. "Facility costs are in NT$" is INFERENCE, not case:147. Say operations beyond 2042 are "outside the plan's scope (case:92-93)", not "not funded by her"; public funding "expects" a self-funded share (Taipei caps grants at 70%). With the iBond coupon fix, option 1 short is 16.2% (3r unchanged). The "top excludes the reserve" variant (3a_10k) already exists: reach-top 78.6%, top median $155.8k. Never copy the source claim "16 times the largest NCAF grant" (it is 5.1 times). For agreed cross-model numbers use `oct20/reconcile3r/reconcile_3r.md` §5.


**AI-generated research for Team Caplet (Claude Code, 20 Oct 2026, Sydney). SIMULATED READERS (AI). Not text to submit.**
- None of the three readers is a real person. No reaction below was said by Laura Gao or by any funder.
- "Laura" here is a reader built **only** from the official case (`case:n`) and `oct20/client/client_deep.md` (`CD:n`). She has no real-life facts beyond those.
- The two co-sponsor readers are built from the verified Taiwan and donor-research facts in `oct19/cosponsor/cosponsor_research.md` (`CO:n`). Anything beyond those facts is labelled INFERENCE or UNVERIFIED.
- This file drafts no IPS, TNA, Final Report or fundraising wording. It lists what the plan **must make clear**. Students decide the content and write it in their own words.
- Log any use in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, `oct19/office/web/ai_policy_2026-10-19.txt:377`).
- Never contact Laura to "test" any of this ("Teams are not permitted to contact Laura Gao", `client.txt:23`).

**Citation short forms.**
- `case:n` = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.
- `crit:n` = `.../smapply_public_2026-10-14/deliverables.txt`. `IPS:n` = `.../2026_WGY_Investment_Policy-FINAL.txt`.
- `V5:n` = `oct19/drive/ips_report_live.md`, the verbatim live IPS Doc (unchanged since 18 Oct 00:49Z per CD:19). Lines 23-30 hold the accepted text and the pending v12 text run together.
- `UPD:n` = `oct19/out/Caplet_Update_19Oct2026.md`. `CPN:n` = `oct19/coupon/coupon_risk_options.md`. `NR:n` = `oct20/numbers/numbers_refresh.md` (19 Oct close). `INF:n` = `oct20/inflation/inflation.md`. `FRP:n` = `oct19/frprep/final_report_prep.md` (the co-sponsor facts checklist is FRP:439-457, items X1-X15). `JDG:n` = `oct19/judges/findings.md`.
- `oct19/` and `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`.
- `CR` = this folder, `oct20/clientread/`: `scripts/coupon_options.py` (the 19 Oct coupon model plus extra outputs) and `data/coupon_options_results.json`.

**Labels.**
- CASE: stated in the case.
- DERIVED: arithmetic on case numbers.
- MODEL: an AI-built simulation, not a fact.
- VERIFIED: a primary source, cited.
- INFERENCE: the simulated reader's likely reaction; a judgement, not evidence.
- UNVERIFIED: could not be confirmed.

---

## 0. Summary

1. **The client reader's first worry is the word "certainty".** She would see that the live IPS backs gaps with "her other assets" (V5:25), which the case forbids (case:91-92). Under that wording (coupon option 1), some payment comes up short in **15.6%** of model paths and **29%** of history windows on the strict coupon basis. Under option 3r ($10k in the Nov-2041 bond) it is 0.02% and 0% (MODEL, 19 Oct close; CR json; matches `oct20/numbers/coupon_options_comparison_19Oct.csv`).
2. **New finding today: option 3r roughly halves the chance that the gift reaches the top of the range.** Under option 1 the gift reaches the top (within $1k) in 75% of model paths. Under 3r it does so in **49%** (57% in history windows), because the $10k counts in the top but is released only above need plus a $5k margin. It lands within $6k of the top in 78%. If 3r wins the vote, the top and its stated chance must be redefined together, or the "can reach" line co-sponsors hear will be wrong (MODEL; CR json, run twice with the same result).
3. **The money Laura keeps doubles as the payment backstop, and in bad cases it vanishes.** Under option 1 her kept money in 2033 is $0 at the 5th percentile and under $10k in 17% of paths. Under 3r it is $8.4k at p5 and under $10k in 8% (median about $20.5k either way). The case's flexibility worry (case:102-103) needs a stated bad-case figure, not just "the other half" (MODEL; CR json).
4. **Both co-sponsor readers would ask, before anything else: how much, in what currency, when, paid to whom, how firm, and what is not covered.**
   - The Taiwanese foundation officer thinks in NT$, registered organisations, a self-funded share (自籌) and annual budgets.
   - The US funder thinks in lead gifts and the risk of an operating gap after the money stops.
   - The plan already has strong answers (ten years of operating money pre-funded; a rule-set bottom), but its words ("floor plus half the equity fund", "paths", "Root-and-Branch") do not reach either reader.
5. **The highest-value fixes for Client Knowledge and Creativity** (ranked in Section 6):
   - define certainty inside the portfolio;
   - split risk by goal and show the balance;
   - give the kept money a job, a home and a bad-case size;
   - make the range's top and its chance honest under the chosen coupon option;
   - tie the payments to the residency's early operations and their shrinking real value;
   - show "meaningful" as well as "credible", at a dated NT$ scale;
   - state the currency and who bears it.

---

## 1. The plan the readers are given (current strategy, 19-20 Oct)

What each reader sees: the live IPS wording (V5:23-30) plus the current numbers and the pending coupon decision. Nothing new is invented here.

| Element | Current state | Source |
|---|---|---|
| Ladder | Jan 2027: Treasuries for all ten $50k payments (iBond funds IBTM-IBTR plus five T-bonds), 2042 first; any cost above $300k is topped up from the 2028 deposit | V5:27; UPD:283-285 |
| Ladder cost (cautious basis D) | $297,162 on the 19 Oct close; $2,838 room; 41% odds it costs more than $300k on 1 Jan | NR:12-13 |
| Floor | Jan 2028: IBTM sized to repay about $150k in Dec 2032; costs $116,485; leaves about $33.5k for VT | NR:15, NR §4a |
| Equity | One global fund (VT), about 7% of Laura's money after 2028 (6.9%), about 9% of WInS | UPD:261 |
| 2031 range | Bottom = floor rounded down (the "$145k" rule); top = floor + half of VT, less any projected shortfall | V5:29; CPN basis |
| 2033 gift | Floor + half of VT, capped at the top; Laura keeps "the other half for flexibility" | V5:29 |
| Coupon risk | Undecided: vote set B D1 on Tue 27 Oct; the AI recommendation is 3r ($10k in the Nov-2041 bond), which lowers the bottom to $135k | UPD:297-322 |
| Live wording problems | "her Taiwan residency", "covered by her other assets", "capacity for risk is high" with no qualifier, "depends on publishing and speaking income", "so we buy", "Maturing bonds, not sales", "stays with Laura", "so she cannot miss the range", "Name the residual risks." | V5:23-30; CD:167-183; UPD:138-145 |

**The 19 Oct model outputs used below** (MODEL; CR json, `mc/rho+0.0` and `history_add`; 100,000 paths and 690 history windows; the same model and basis as CPN, re-run on the 19 Oct curve):

| | Option 1: state the risk only (the live text) | **3r: $10k in the Nov-2041 bond** | 4: dedicated rebuild |
|---|---|---|---|
| Some payment short (model / history) | 15.6% / 29.3% | **0.02% / 0%** | 0% / 0% |
| 2031 bottom (median) | $145k | **$135k** | $145k |
| 2031 top: p5 / median / p95 | $141.2k / $167.0k / $183.5k | **$142.3k / $165.8k / $181.3k** | $141.3k / $166.3k / $183.2k |
| Range width at the median (top minus bottom) | $22.0k (15% of the bottom) | **$30.8k (23%)** | $21.3k |
| 2033 gift: p5 / median / p95 | $138.8k / $166.2k / $182.6k | **$136.7k / $163.3k / $180.0k** | $140.7k / $165.5k / $182.3k |
| Gift below the announced bottom | 1.95% | **0.06%** | 0.01% |
| Gift reaches the top (within $1k): model / history | 75.2% / 83.9% | **48.7% / 56.7%** | 78.5% / 88.0% |
| Gift within $6k of the top: model / history | 94.1% / 91.9% | **78.1% / 78.1%** | 97.1% / 94.8% |
| Laura's kept money in 2033: p5 / p10 / median | $0 / $4.8k / $20.5k | **$8.4k / $10.8k / $20.5k** | $8.5k / $11.0k / $21.6k |
| Kept money under $10k | 17.2% | **8.0%** | 7.8% |

Why 3r lowers the chance of reaching the top: the top counts the whole $10k reserve. But in 2033 the reserve releases only what is above the projected need plus a $5k margin (CR `scripts/coupon_options.py`, lines with `rel = ... - 5000`). So in most paths the gift stops about $5k short of the top. **Check before relying on it:** a top that counts only the releasable part would sit about $5k lower and be reached more often. That is a design choice for the 27 Oct vote; I did not model it.

---

## 2. Reader 1: the client (simulated, AI)

**Who this reader is (case only):**
- A bestselling author, illustrator, entrepreneur and educator with a successful creative business (case:5-7).
- A Wharton statistics graduate and a former product manager (case:16-17).
- Willing to take "thoughtful risks", and she asks her team for "an appropriate balance between pursuing growth and protecting the capital required for her goals" (case:68-74).
- Building a small, community-oriented creative residency in Taiwan for five groups: artists, writers, designers, entrepreneurs and educators (case:76-80).
- She guards her credibility with co-sponsors (case:114-115) and wants flexibility "as the project develops" (case:103).
- She chooses the strategy (case:9) and decides the contribution (case:101).

### 2a. Reading trace of the live IPS (V5:23-30), paragraph by paragraph

| Para | What she would understand | What would confuse or worry her (INFERENCE) | Case anchor |
|---|---|---|---|
| Pitch (V5:23) | Ten payments first, then a minimum for the facility, then growth. The "$500k out, $450k in" problem framing works for her | "Taiwan residency" can read as her own residence status, not the creative residency. "Echoing her memoir *Messy Roots*" may feel like her book is being used as a label, unless the metaphor does work (roots bought first and never sold) | case:76, 21-22; CD:171, 200 |
| Objectives (V5:25) | Payments first, "using only the portfolio" | **"covered by her other assets"**: she has been told outside money cannot fund the payments. This sentence says it will. "Certainty here means each payment is covered at purchase" describes a method, not a level of confidence. She asked for a definition, how it was evaluated, and the assumptions | case:91-92, 97-99 |
| Risk (V5:26) | The 5.1% hurdle on the 2027 deposit is a clear, case-derived number she can check | **"capacity for risk is high"**, followed by a plan that is about 92% Treasuries (66.9% + 24.6% + 0.8%, UPD:261): which is it? **"depends on publishing and speaking income"**: reads as doubt about her career, and drops licensing and "other entrepreneurial ventures". **"Treasuries currently yield about 5.15%, so we buy"**: as a statistician she would spot the non sequitur, because her money arrives in January whatever the yield | case:43-45, 68-74; JDG:41 |
| Ladder (V5:27) | Payments, then floor, then growth, in that order; the 2042 rung first | "If the cost exceeds $300,000": how likely is that? (41% on the 19 Oct close, basis D.) What does a top-up take away from the facility? "assumed to return 7% a year": nominal or real, and whose estimate? | NR:12-13; UPD:285 |
| Hold (V5:28) | Held to maturity; no forced sales | "Maturing bonds, not sales, supply every payment" is false for the 2038 and 2039 payments, which wait in a short-term Treasury fund. "funded from the equity Laura retains": so the money she keeps is not free | UPD:142; case:97 |
| Range (V5:29) | A bottom and a top, with a rule | "half the equity fund's value" (why half?); "less any expected payment shortfall her half cannot cover" (unreadable); "In our simulations ... three of four paths" (which model? what is a path?). Under 3r the "three of four" becomes about one in two (Section 1) | case:117-118; JDG:42, 102 |
| Risks (V5:30) | Falling yields and Taiwan costs named | "Beyond a US default" opens with the scariest, least likely risk. "met from her retained equity" again uses her flexibility money as the backstop. "a stronger Taiwan dollar would raise costs further": so what does she do about it? "Name the residual risks." is a leftover instruction | case:146-148; UPD:136 |

### 2b. What would earn her confidence (INFERENCE from case:97-120, crit:56)

1. **A definition of certainty she can repeat to a co-sponsor.** One sentence on what "high" means, one test, and every gap covered by a named source inside the portfolio. The case asks for exactly these three things (case:97-99).
2. **Her own risk profile read back to her correctly.** The payment money cannot bear risk (fixed, dated, portfolio-only). The money beyond it can (long horizon, living costs met outside). The equity share follows from that split, not from "capacity is high" (CD:65, 105).
3. **The balance named, with its price.** What she gives up by holding about 7% equity, shown as a dial: a larger equity share or a smaller floor against the median and bad-case outcomes. It must still end in one recommendation, because she asked for one (case:72; CD:110).
4. **The choice left with her.** The contribution is hers to decide (case:101). "Floor plus half" should be presented as the recommended setting of a dial. The evidence already shows that the share promised changes her bad-case cushion ($16k at one third, $12k at half, $0 at all of it), not the chance of reaching the top (UPD:332).
5. **A truthful 2031 sentence.** A bottom she can always deliver, a top labelled as "can reach", and a chance beside it that is right for the chosen coupon option (Section 1).
6. **The residency in the plan.** The payments are "reliable support for its early operations" (case:83). People who live, work and teach there rely on them, which is why they come first (CD:113).

### 2c. Numbers she would want (all exist; each needs a date and a basis)

| Number | Value (MODEL unless stated) | Where | Note |
|---|---|---|---|
| Return needed on the 2027 deposit alone / on both deposits | 5.087% / 1.046% | DERIVED, CD:61 | The clearest client number; not stale |
| Chance a payment is short, under the chosen cover | 15.6% (option 1) vs 0.02% (3r) | CR json | The certainty level she asked for (case:98) |
| Ladder cost and the chance of a top-up | $297.2k; 41% chance it exceeds $300k (19 Oct, D) | NR:12-13 | Final Report only, re-priced on the 6 Nov close |
| Range bottom and top, and the chance of landing inside | $145k or $135k bottom; top about $166-167k; inside the range about 98% (option 1, coupon model; 99.3% in the number sheet, NR §4b) to 99.9% (3r) | NR §4b; CR json | IPS gives the rule; Final Report gives the figures |
| Chance of reaching the top | 75% (option 1) / 49% (3r) | CR json | Changes with the D1 vote |
| What she keeps in 2033, typical and bad case | About $20.5k median; $0 (option 1) or $8.4k (3r) at p5 | CR json | The case's flexibility test (case:102-103) |
| A bad-market example | 40% stock fall in 2032: typical contribution $169k → $162k (V5:29; 16 Oct basis; re-run before use) | V5:29 | case:118-119 |
| Real value of the payments | 2042 payment buys 80% of the 2033 one at 2.5% US inflation; about 84% with Taiwan CPI at 1.9% and FX flat | INF:12-14 | Residency planning; not a cost estimate |
| Currency effect on the facility contribution | 2-year moves since 2000: p5 −10% / p95 +12% in NT$ terms | CO:154-162 | Who bears it must be stated |

### 2d. Words that would land badly with her (and what concept replaces each)

| Word or phrase | Where | Why it lands badly | Concept instead |
|---|---|---|---|
| "her Taiwan residency" | V5:23, 25 | Sounds like her immigration status | "the creative residency in Taiwan" (case:76) |
| "covered by her other assets" | V5:25 | Breaks her own stated rule | A named backstop inside the portfolio |
| "capacity for risk is high" | V5:26 | Contradicts the 92% Treasury plan she is reading | High for money beyond the payments; low for the payments |
| "depends on publishing and speaking income" | V5:26 | Doubts a "successful" career (case:6) | Timing: not yet received in January 2027 |
| "so we buy" | V5:26 | A non sequitur a statistician would catch | The plan does not bet on rates |
| "her other holdings", "her retained equity", "stays with Laura" | V5:25, 28, 47 | Unclear whether this money is inside the portfolio or hers to spend | Say where it sits and what it is for |
| "cannot miss", "guarantee", "risk-free" | V5:158, 202, 264, 275 (older tabs) | An over-promise, the very thing she fears (case:114) | A stated confidence level |
| "paths", "simulations" with no model named | V5:29 | Statistics without a method | Name the model and its main assumptions once (Final Report) |
| "the artists" as payees | V5:43, 57-59 | Five groups use the space, and the payments fund operating expenses, not wages | "the residency's operating expenses" (case:88) |
| "gift", "minimum gift", "building" | V5:40, 59 | Not the case's words | "facility contribution", "facility" |
| "the Dream", "money for a dream" | notes:203, 378 | Patronising | "long-term goals", "future vision" (case:8, 10) |
| "as a statistics graduate she will appreciate" | notes:339 | Presumptuous | Let the case's demand for method justify the numbers |

---

## 3. Reader 2: a programme officer at a Taiwanese corporate foundation (simulated, AI)

**Who this reader is (built from verified facts, CO §1):**
- Corporate foundations in Taiwan (examples: 建弘文教基金會, 研華文教基金會) mostly sponsor projects. Many give through NCAF's arts-business schemes, at NT$0.5-0.8m per scheme in 2025 (CO:35, 72).
- A company's donation to NCAF or a city/county culture foundation counts as a donation to government and is deductible without limit. Gifts to other registered cultural bodies are capped at 10% of income (CO:82-87).
- Public funding comes in single years, is paid after spending against receipts, goes to registered organisations, and requires a self-funded share (自籌) (CO:41-53, 64).
- These foundations' own grant criteria are **UNVERIFIED** (CO:35). So every reaction below is INFERENCE.

**What they read:** the co-sponsor facts checklist (FRP:439-457, X1-X15), as it would surface in the fundraising excerpt.

| Question | Their likely reading (INFERENCE) | Checklist item | Gap |
|---|---|---|---|
| **How much, in our money?** | They budget in NT$. "US$135,000-166,000" means little without a dated rate. At NT$32.40 (FRED DEXTAUS, 16 Oct 2026, the latest in `oct20/inflation/raw/DEXTAUS.csv`) the range is about NT$4.37m-5.37m (3r) or NT$4.70m-5.41m (option 1) | X1, X11 | X11 says "who bears FX" but not "give a dated NT$ equivalent". Add it |
| **How firm is the bottom?** | "Floor", "rounded down because a fund's payout is not fixed" is unclear in English and opaque in translation. Their test is simple: is the bottom a commitment or a hope? | X2 | Define the bottom by its rule, and say once that it is not a dollar sum owned in 2027 (UPD:361) |
| **What is "can reach"?** | A top with a chance beside it fits how Taiwanese funders read numbers. Probability words alone are read nearer 50% (Budescu 2014, which included Chinese samples but not Taiwan) | X3, X4 | X4 still says "about 3 of 4". Under 3r it is about 1 in 2 (Section 1). Make X4 conditional on the D1 vote |
| **When is it paid, and to whom?** | Their money and the public money all go to a Taiwan-registered organisation, against a dated plan. They would ask when her contribution lands (January 2033) and what is committed in 2031-32 | X1 (date of the projection only) | Missing: the payment date of the contribution, and a plain note that the receiving body is outside the plan's scope (case:168-169). Never imply Laura personally qualifies for Taiwan grants (CO:93-98) |
| **Is this the self-funded share?** | Her facility contribution plus ten years of operating money looks like a large 自籌 share. Public applications in late 2032 will show the same number, so it must match what co-sponsors were told | X7, X13 | Whether a grant may count her gift as its self-funded share is UNVERIFIED (CO:142). Do not claim it |
| **How big is this by local standards?** | NT$1.62m a year of operating money is about 1.8 times the largest 2025 NCAF visual-arts organisation operating grant (NT$900k) and about 54% of the MOC artist-village per-application cap (NT$3m, 2019 text). The bottom (NT$4.4-4.7m) is a lead gift by Taiwan standards (DERIVED from CO:35-37, 76) | X7 | Usable in the Final Report as dated, cited scale. Never as a "multiplier" or "unlocks" claim (CO:143) |
| **What does a new residency lack?** | No operating record. MOC asks for usage rates, members and an operating budget, and multi-year money needs three funded years first (CO:57, 182) | X7 | Ten pre-funded years of operations is the plan's best answer to a missing track record (INFERENCE). It must not become a cost estimate (case:164-167) |
| **What if markets fall?** | They want one sentence and one number, not the mechanism | X5 | Fine as listed; keep to one example |
| **Does the number change during the campaign?** | Different numbers in different years, or to different funders, would worry them most | — (CO §3 item 3) | **Missing from X1-X15:** one valuation date and one re-quote rule (UPD:334). Add it |
| **Bilingual consistency** | If a Chinese version exists, the numbers must be identical and probabilities given as numbers | — (CO §3 item 8) | Missing from X1-X15. Add it |

**Words that would land badly with this reader (INFERENCE; check translations with a fluent speaker, UNVERIFIED):**
- **"residency"** rendered as 居留 (legal residence). Taiwan's arts system uses 駐村 / 藝術村 (CO:41, 57: "藝術村營運扶植", "進駐"). The wrong word makes the project read as an immigration plan.
- **"gift" / "donation"** for her contribution. In their world money moves through registered bodies and counted shares. "Facility contribution" (the case's term) is safer.
- **"half the equity fund", tickers (IBTM, VT), "paths", "Monte Carlo"**: noise to a programme officer.
- **"Root-and-Branch" / "Messy Roots"**: may not translate. It is a creativity asset for judges, not for this reader.
- **"US default"**: alarming and irrelevant to them.
- **Geopolitics or her reasons for choosing Taiwan**: never (CD:122, 193).
- **"guaranteed"** (保證): the over-promise problem in a second language.

---

## 4. Reader 3: a US arts funder (simulated, AI)

**Who this reader is:** a programme officer at a US private foundation that funds artist residencies.
- Verified anchors: Kresge's 2011 challenge-grant guide asks "Are they leading with their own gifts?" and looks at "annual operating needs" (CO:127, US, 2011, by analogy only). Donor research finds an announced lead gift raises giving and matching adds little (List & Lucking-Reiley 2002; Rondeau & List 2008; Karlan & List 2007; CO:104-108). Telling donors that overhead is already covered raises giving (Gneezy et al. 2014; CO:109).
- Everything else about how such a funder behaves is INFERENCE.

| Question | Their likely reading (INFERENCE) | Checklist item | Gap |
|---|---|---|---|
| **Is the founder leading with her own money?** | Yes, twice over: $500k of operating money over ten years, plus a facility contribution. To them this is the strongest line in the package | X6, X7 | X7 lists it. Put it first: "running costs are already paid for" is the donor-tested message (CO:109) |
| **Is the bottom a pledge?** | They think in pledges and gift agreements. A "range" with a firm bottom and an uncertain top reads like a firm pledge plus a hoped-for amount | X2, X3 | The legal form is out of scope (case:168-169). The plan must still say what is firm (the bottom's rule) and what is not (the top) |
| **How wide is the range?** | $135k-$166k is a 23% spread on the bottom. Wide ranges lose appeal (Du et al. 2011, CO:117). They would want a central value | X4 | Give the central value (median gift about $163k under 3r, $166k under option 1) beside the range |
| **Where is the money held?** | "In US Treasuries until 2032" is instantly credible to them | X2 | One plain line, no tickers |
| **What happens after 2042, and if costs grow?** | Their classic worry is the operating gap when the founder's money stops. The payments are fixed nominal, and the 2042 payment buys about 20% less than the 2033 one | X7 (partly) | **Missing:** say plainly that operations above $50k a year and after 2042 are not funded by her (CO §3 item 7; case:85-86, 92-93). Honest, and the reason co-sponsors are needed |
| **Would she match us?** | No match is offered, and the evidence says matching adds little | — (CO §3 item 4) | Missing from X1-X15. Add "no matching offer" |
| **Currency** | They give in US$ to a Taiwan project, so they face the same NT$ cost risk as Laura | X11 | Fine as listed |
| **Is the research honest?** | They know US fundraising studies. Citing them with scope (US households, a university campaign) builds trust; over-claiming does not | X12 | Fine as listed |

**Words that would land badly with this reader (INFERENCE):**
- **"cannot miss", "her word can't break", "guaranteed"** (X10, X15): seasoned funders distrust certainty claims about markets.
- **"half the equity fund's value, less any expected payment shortfall her half cannot cover"**: an unreadable formula. They want amounts and dates.
- **"Beyond a US default"**: reads as either alarmist or jargon.
- **"floor"** is fine if it is defined once as the bottom of the range. **"seed money"** is acceptable US vocabulary, but no study supports a stated multiplier.
- **"the artists"**: they would ask whether payments are stipends. The case says operating expenses (case:88).

---

## 5. Where the three readers pull in different directions

| Tension | Laura (client) | Taiwanese officer | US funder | What the plan must decide |
|---|---|---|---|---|
| Range width vs safety | Wants a bottom she can always deliver (case:114) | Wants a firm NT$ number for a budget | Wants a narrow range with a central value | Under 3r the bottom falls $10k and the range widens to about $31k. Choose the coupon option knowing its effect on the 2031 message, not only on payment safety |
| The chance of reaching the top | Wants it honest (case:117-118) | Wants a number, not a word | Discounts a wide upside (Exley 2016: risk as "an excuse not to give", CO:121) | One figure, tied to the chosen option: 75% (option 1) or about 49% (3r), unless the top is redefined |
| Currency | Facility costs are in NT$ (case:147) | First question | Secondary | State who bears FX, once, in both the Final Report and the excerpt |
| Number density | Wants method and numbers (case:97-99, 117-118) | Wants few numbers, in NT$ | Wants amounts and dates | The IPS gives principles (IPS:68-70). The Final Report holds the numbers. The excerpt has at most about 5 figures |
| The metaphor | Must not look like a label on her book | Untranslatable | Neutral | Keep it only if it carries the logic (JDG:103, 132) |

---

## 6. What the plan must make clear, ranked by likely gain in Client Knowledge and Creativity scores

How to read the table:
- **Gain** is the AI's estimate for the two criteria: H = likely +1 point on a 10-point criterion; M = about +0.5; L = less. It draws on the mock judges' scores of Client 6/6/6 and Creativity 6/6/5 and their fix lists (JDG:117-131).
- **Where:** IPS = a principle only (no figures beyond 1-2 dated anchors, no citations, IPS:68-70, 123). FR = the Final Report, with figures and method. EX = the co-sponsor excerpt inside the Final Report.
- Each item says what must be clear, never the wording.

| Rank | What the plan must make clear | Readers | Criterion phrase it serves | Gain (Client / Creativity) | Where | Evidence and numbers | Decision needed first |
|---|---|---|---|---|---|---|---|
| 1 | **Certainty is defined, tested and covered inside the portfolio.** What "high degree" means, the one test used, and the order of cover for a payment gap, every step inside the portfolio. No outside assets, no co-sponsors | Laura, both funders (X6) | "recommendations that can earn her confidence" (crit:56); case:91-92, 97-99 | H / M | IPS principle; FR figure plus method | Option 1: 15.6% / 29% short; 3r: 0.02% / 0%; option 4: 0% (CR json). The live V5:25 "her other assets" breaks case:91-92 | D1 coupon option; D3 certainty standard (UPD:297, 329) |
| 2 | **Risk is set per goal, and the balance is named and priced.** Low capacity for the payment money, high for the rest. Why about 7% equity fits "thoughtful risks" and "an appropriate balance". What more equity would buy and cost, shown as a dial ending in one recommendation | Laura | "risk considerations"; "tailors ... to Laura's circumstances" (crit:56); case:68-74 | H / M | IPS principle (split by goal); FR dial | CD:65, 105, 110; JDG:41, 120 (+1-2 Client) | None for the IPS line; D9 if the floor size reopens |
| 3 | **The money Laura keeps has a stated job, a home and a bad-case size.** Whether it backs payments (and until when), where it sits to 2042, and how much is left in a bad case | Laura | "Preserves appropriate financial flexibility" (case:145); "priorities" (crit:56) | H / L | IPS principle; FR figures | Median about $20.5k; p5 $0 (option 1) vs $8.4k (3r); under $10k in 17% vs 8% (CR json). The V5 half has two jobs (V5:29-30) | D2 (UPD:328) |
| 4 | **The 2031 range: a bottom set by a rule, a top labelled as "can reach" with a chance that is right for the chosen option, and a central value.** If 3r wins, either redefine the top (count only the releasable reserve) or restate the chance (about 1 in 2) | Laura, both funders (X2-X4) | "communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors" (crit:59) | M / H | IPS rule; FR and EX figures | Reach-top: 75% vs 49%; within $6k: 94% vs 78%; width $22k vs $31k (CR json). X4's "about 3 of 4" is option-1-only | D1, D4, D8 |
| 5 | **Why the payments come first, in residency terms.** The payments are "reliable support for its early operations" for five groups who live, work and teach there. They are fixed in dollars, so their real value falls (the 2042 payment buys 80-84% of the 2033 one). Operations above $50k a year and after 2042 are not funded by her | Laura, US funder | "residency goals" (crit:56); "original thinking" (crit:59) | H / M | IPS: one principle sentence; FR: the real-value figure; EX: what is not covered | case:83, 88-90; INF:12-14; CD:109, 113; JDG:51, 99 | None |
| 6 | **Language matches the case and passes the "would she be comfortable reading this" test.** Run the swap lists (Section 2d here; CD:167-183) before any other edit | All three | "thoughtful understanding of the client"; "authentic team voice" (crit:56, 59) | M / M | IPS and FR | 12 live problems in V5:23-30 (Section 2a) | None; cheap to do |
| 7 | **"Meaningful" as well as "credible".** What her contribution signals (ten years of operating money from her own portfolio, plus a facility contribution), at a dated local scale, with no facility-cost estimate and no multiplier claim | Both funders, Laura | case:110-112; crit:59 | M / H | FR and EX only | NT$1.62m a year ≈ 1.8 × the largest 2025 NCAF organisation operating grant; bottom ≈ NT$4.4-4.7m at NT$32.40 (16 Oct) (DERIVED, CO:35-37). "meaningful" appears 0 times in V5 (CD:107) | None |
| 8 | **Currency: the range in US$, a dated NT$ equivalent, who bears FX, and one sensitivity.** | Taiwanese officer, Laura | "residency goals"; "investment uncertainty ... clearly" (crit:56, 59); case:147 | M / M | IPS: one principle (D8); FR/EX figures | 2-year moves since 2000: p5 −10% / p95 +12% (CO:154-162). The live V5:30 names the risk but says nothing about who bears it | D8 (currency and who bears it) |
| 9 | **Laura decides; the plan recommends.** "Floor plus half" is presented as a recommended setting, with what the other settings cost her | Laura | "presents recommendations that can earn her confidence" (crit:56); case:9, 101, 126-128 | M / L | FR | Share promised changes the bad-case cushion ($16k / $12k / $0), not the reach-top chance (UPD:332) | D6 |
| 10 | **One valuation date and one re-quote rule for the 2031-33 campaign**, so every co-sponsor hears the same number, and later grant applications match it | Both funders | "clearly and credibly" (crit:59); case:109 | L / M | IPS rule; EX | CO §3 item 3; missing from FRP X1-X15 | D8 |
| 11 | **The operating reserve's size, starting make-up and run-off from 2033, including where early maturities wait** (the 2037 and 2038 bonds park in a short-term Treasury fund) | Laura | case:94-97 (a required answer) | M / L | IPS principle; FR table | "Maturing bonds, not sales" is false for 2038/2039 (UPD:142); parking rule (JDG:126) | Smaller choice: the parking clause |
| 12 | **The real reason for buying in January:** the money arrives then, and the plan does not bet on rates. Not "yields are high, so we buy" | Laura | "thoughtful understanding" (crit:56); Strategy | L / M | IPS | JDG:37, 123 (2 of 3 judges) | None |
| 13 | **The 2028 deposit as timing, not doubt:** "will contribute" (case:43-44), not yet received in January 2027 | Laura | "circumstances" (crit:56) | M / L | IPS | V5:26; CD:62, 104, 181 | None |
| 14 | **Every number dated, its basis named, and one model named once; the same numbers in the IPS, the Final Report and the excerpt** | Laura, US funder | "uses data effectively" (crit:59) | L / M | FR; IPS anchors | FRP X13; UPD:244-248; NR:17 (quote no ladder level in the TNA or IPS) | Basis choice for the FR |
| 15 | **The metaphor either carries the logic** (roots are bought first and never sold) **or goes.** Never implies Laura endorsed it | Laura, Taiwanese officer | "compelling ... narrative", "original thinking" (crit:59) | L / M | IPS pitch | JDG:103, 132; CD:200 | Strategy name (UPD:336) |

**Additions to the co-sponsor facts checklist (FRP:439-457), from the two funder readers:**
- **X1b.** A dated NT$ equivalent beside the US$ range. X11 covers who bears FX but not the conversion.
- **X3b / X4b.** The stated chance of reaching the top must be the one for the coupon option the team votes on: about 3 in 4 under option 1, about 1 in 2 under 3r. Otherwise redefine the top.
- **X16.** When the contribution is paid (January 2033), with one sentence that the receiving organisation is outside the plan's scope. Never imply that Laura herself qualifies for Taiwan grants.
- **X17.** One valuation date and one re-quote rule (CO §3 item 3).
- **X18.** No matching offer (CO §3 item 4).
- **X19.** What is not covered: operations above $50k a year, after 2042, and the falling real value of fixed payments (CO §3 item 7).
- **X20.** If a Chinese version is made: identical numbers, probabilities given as numbers, and "residency" rendered as 駐村 / 藝術村, not 居留 (translation UNVERIFIED; check with a fluent speaker).
- **X21.** A central value beside the range (Du et al. 2011, CO:117).

---

## 7. What this teaches (plain English)

- **The same fact needs a different first sentence for each reader.** Laura needs to hear that her payments are safe and that she still has room to decide. A Taiwanese funder needs the amount in NT$, the date and how firm it is. A US funder needs to hear that the running costs are already paid. The facts stay the same; the order and the units change.
- **Every safety choice moves a message.** The $10k coupon reserve makes the payments almost certain, but it also widens the range and halves the chance of reaching its top. A plan is only consistent when its numbers and its promises move together.
- **A "backstop" that is also "flexibility money" is really neither until its job is named.** In the bad cases under the current wording, it is exactly when Laura needs flexibility that her flexibility money is gone.

---

## 8. Limits and verification

- **The readers are simulated.** Laura's reactions are inferred only from case:1-169 and CD. The funders' reactions are inferred from verified sources in CO plus judgement. Corporate foundations' own criteria are UNVERIFIED (CO:35). No real person was consulted or contacted.
- **The model** is the coupon-options model (CPN basis: the 19 Oct curve held flat to 1 Jan 2027; holdings' dates; waiting cash at 0%; parallel random-walk rates at 1.0 point a year; VT at 7.0% compound and 16.78% volatility; 100,000 paths; 690 history windows). I copied it from `oct20/numbers/scripts/coupon_options.py` and added outputs only: kept-money percentiles, the reach-top share (within $1k and $6k), top and gift p5/p95. The logic is unchanged.
  - **Check 1:** my run reproduces the sibling 19 Oct table exactly on the shared fields. Option 1 gift median $166,177, p5 $138,777, short 15.58%. 3r gift median $163,343, p5 $136,671, top median $165,807, below the bottom 0.06% (`oct20/numbers/coupon_options_comparison_19Oct.csv`).
  - **Check 2:** a second full run gave identical outputs (`CR/data/stdout.txt`, `stdout2.txt`). The history windows tell the same story: reach-top 83.9% (option 1) vs 56.7% (3r).
- **Model limits** (CPN:184-198): no pull back to normal rates; the $5k release margin is the model's choice; iBond funds are modelled as par bonds; WInS coupon timing is UNVERIFIED. The reach-top drop under 3r comes from the release rule. A different top definition was not modelled.
- **Arithmetic:**
  - NT$ at 32.40 (FRED DEXTAUS, 16 Oct 2026, file `oct20/inflation/raw/DEXTAUS.csv`, last row): $135k = NT$4.374m; $145k = NT$4.698m; $165.8k = NT$5.372m; $50k = NT$1.62m.
  - Against NCAF's NT$900k: 1.80 times. Against the MOC NT$3m cap (2019 text, current cap UNVERIFIED): 0.54 times.
  - Range widths: $30,807 (22.8% of $135k) and $21,996 (15.2% of $145k).
  - The 2042 payment in 2033 money: $40,036 at 2.5% and $42,209 at 1.9% (Python, run once and cross-checked against CD:261).
- **Line references** in V5 were confirmed with `grep -n` on 20 Oct (lines 23, 25-30). The V5 copy is current as of 20 Oct (CD:19).
- **UNVERIFIED:**
  - the right Chinese term for "residency" in fundraising text (native-speaker check needed);
  - whether a Taiwan grant may count Laura's contribution as the self-funded share;
  - whether NCAF would accept a designated gift for one private residency facility;
  - US funder norms beyond the cited studies;
  - whether Laura attends any 2027 event.
