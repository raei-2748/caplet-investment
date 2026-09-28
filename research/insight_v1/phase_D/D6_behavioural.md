# D6: Client psychology and behavioural finance (M125, M018, M019, M228, M237, M197)

Agent D6 (Client Psychologist / Behavioural Finance), insight_v1 run, Phase D. Written 2026-09-27/28 (the session
ran past midnight UTC). This is AI-generated research for Team Caplet. It gives specifications, evidence, numbers and
checklists. **It contains no text to submit.** The six students decide everything and write every deliverable in their
own words, and they record AI use in the Final Report's Works Cited (R-W46). Laura appears here only through the case
and her public professional record. No personal-life material is recorded. Nothing here suggests contacting her
(R-W16: contact means disqualification).

Script: `research/insight_v1/scripts/D6_behavioural_numbers.py` (run from the repo root with `.venv/bin/python`,
about 3 seconds). It reproduces the verified base exactly: lock-early surplus in 2033 p5/p50/p95 $159k/$207k/$273k,
2031 floor $127k/$165k/$217k (F-401/F-402). All the figures below come from it unless another source is named.

Status labels (brief section 3): **VP** = VERIFIED-PRIMARY (read on the primary page; URL and date in Sources);
**VRF** = VERIFIED-REPO-FILE; **SNIP** = SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION; **DER** = derived by the script
from labelled inputs; **INT** = my interpretation, never a fact about Laura.

## Words used (defined once)

- **Promise money / the ladder:** Treasuries bought in January 2027 that pay the ten $50,000 operating payments
  (2033-2042). About $292k of the $300k (F-101).
- **Growth money (the "sleeve"):** everything the payments do not need, roughly $158k after the 2028 deposit. It pays
  for the facility contribution and for flexibility.
- **Floor:** part of the growth money moved into a 2-year Treasury in January 2031, which is already worth a known
  amount in 2033. The model locks 80% (an open parameter).
- **Risk need / risk-taking ability / behavioural loss tolerance:** the three parts of an investor's risk profile in
  CFA Institute's 2020 guide (VP). *Risk need* is how much risk a goal requires. *Ability* is how much loss the
  investor can bear without hurting her living standard or her goals. *Behavioural loss tolerance* is how she
  feels and acts when she loses money.
- **Willingness vs ability:** everyday names for loss tolerance vs ability.
- **Loss aversion:** people feel a loss more strongly than a gain of the same size. A common estimate is about 2 to
  2.25 times as strongly (SNIP; Tversky & Kahneman 1992, not opened).
- **Myopic loss aversion:** loss aversion combined with checking results often (Benartzi & Thaler, VP).
- **Break-even effect / house-money effect:** after losses, people favour bets that could win back what they lost.
  After gains, they take more risk (Thaler & Johnson 1990, VP).
- **Reference point:** the number a person compares an outcome with to decide whether it feels like a gain or a
  loss.
- **Pre-commitment:** a rule agreed in calm times that decides what happens in a stressful moment.
- **Calibration:** stated confidence matches how often you turn out to be right.
- **p5 / p50 / p95:** in a simulation, the result that 5% / 50% / 95% of paths fall below. p50 is the median.

---

## 0. Summary: top findings, ranked by impact on reaching the semifinals and on making the plan hers

1. **Use a professional risk-profile framework to state Laura's risk tolerance (M019; IPS, tier 2).** The IPS must
   state a risk tolerance (IPS guide L3, VRF), and the case never gives one (R-AN17). CFA Institute's 2020 guide
   (VP) splits a risk profile into three parts: risk need, risk-taking ability and behavioural loss tolerance. Its
   reconciliation rules settle Laura's case without quoting her:
   - The promise money has no risk need: Treasuries cost $292,264 of $300,000 (F-101). Its ability to bear loss is
     nil, because "high degree of certainty" and "may not rely on co-sponsors" (case L91-92, VRF). CFA rule (VP):
     "Higher behavioral loss tolerance can be ignored when both the risk need and risk-taking ability are lower".
     So however willing she is, no market risk goes on the promise.
   - The growth money has a low risk need: there is no facility target (case L104). Its ability to bear loss is
     high: living costs sit outside the portfolio and there are no withdrawals before 2033 (case L61-65, VRF).
     CFA rule (VP): "A lower risk need can be discounted when both risk-taking ability and behavioral loss
     tolerance are higher". So it holds stocks even though no target requires them.
   - Her *investment* loss tolerance is unknown. CFA measures it by interview or by past investing behaviour (VP),
     and we may not contact her. So the plan must not depend on her composure: every bad-year decision is
     pre-committed (finding 4).
2. **The job she hires the firm for is keeping every public number true, with growth second (M228; IPS pitch, tier
   2).**
   - The case uses "growth" once (L73). It uses "certainty" 4 times, "credib-" 3 times and "confiden-" 3 times (DER
     word count, VRF).
   - None of the case's five "must" tests mentions growth (L134-145).
   - Wharton changed the client criterion from "would win him/her over" to "earn her confidence" (B2b, VP).
   - Credibility research (VP) says that once the outcome is known, people judge a source by *calibration*: was its
     confidence justified? Confidence alone does not earn credibility.
   - This mostly confirms stakeholder_map s7 ("promise first" as the central idea). What is new is the evidence
     base and a content spec for the pitch.
3. **A plain two-number rule picks the growth money's stock share (M237; IPS rule, FR table, tier 2).**
   - The medians hardly differ ($201k-$214k from 0% to 100% stock, JPM). So the *rule* decides the weight, and each
     candidate rule gives a different answer:
     - "max median" gives 100%;
     - "max p5" gives 0%;
     - a loss-averse client who compares against the all-Treasury alternative is nearly indifferent under JPM and
       prefers about 20% under Vanguard's lower forecast.
   - The rule that is plainest and closest to "protecting the capital" (case L73-74) is: **hold the most stock that
     still leaves about a 19-in-20 chance that the growth money ends 2033 with at least every dollar Laura put in
     (~$158k).** It picks **60%** under JPM's forecast and **50%** under Vanguard's midpoint (DER). The pick does not
     change with heavier-tailed returns at the 1-in-20 level.
   - This confirms the provisional 60/40 and gives the IPS a checkable reason for it.
4. **Bad years are normal, and the plan is built so that none of them can touch the promise (M019 bad-year
   analysis; supports parked M007 and D8's M006).**
   - Under the current plan (DER, ASM rate model):
     - the growth money falls in about 27% of years (2028-2030);
     - at least one down year before 2033 happens in 62% of paths;
     - the whole statement shows a fall in about 1 year in 10, and at least once in half of all paths.
   - The rejected growth-first plan would show Laura a first annual statement (December 2027) with assets *below*
     the value of the ten payments in about 40% of paths.
   - Four documented traps (myopic loss aversion; break-even; house money; long-run regret of inaction) each get one
     pre-commitment (section 2.1, bad-year table). D8's rule set (M006) already holds the rules; D6 adds the
     evidence for them.
5. **Drop "floor-first leap" as Laura's trait (M018; TN/IPS/FR, tier 1).**
   - It rests on a reporter's sentence, and D13 ruled it out (brief s16).
   - The research also says career risk-taking does not predict investment risk-taking: risk attitudes are "highly
     domain-specific" (Weber, Blais & Betz 2002, VP). That is the case's own "Although" (R-AN16).
   - Base the IPS risk sentence on the case and the CFA framework (finding 1), not on her biography.
6. **Checklist for Trading Note reflections (M125; TN, tier 1).**
   - Each "how it serves Laura" line should echo one trait *stated in the case* (the checklist is in section 1.3).
   - Each line should pass the swap test: would it still be true for any other client? If so, it is generic.
   - This is mostly answered already (SH-01 to SH-04, D13c). What is new is the note-by-note mapping.
7. **How wide the 2031 range should be (M197; FR, tier 3).** The 2031 range runs from the bought floor to the p90
   of the 2033 total, and its width is set almost entirely by the lock share:

   | lock share | top ÷ bottom |
   |---|---|
   | 80% | 1.30x |
   | 90% | 1.13x |
   | 70% | 1.52x |
   | 60% | 1.81x |

   - Today's 2026 view (p5-p95) is 1.72x.
   - Research on how people judge ranges (Du et al. 2011, Yaniv & Foster 1995, van der Bles et al. 2020; all VP) says
     people prefer the *narrowest range the evidence warrants* and pay little trust penalty for honest numeric ranges.
   - So quote the 2031-view range, not today's spread. Keep the lock share at 70-90%: below 70% the range tops 1.5x;
     at 100% it becomes the "one exact amount" the case rejects.
   - The exact cut-off where a range becomes "useless" is still an ASSUMPTION (no study gives one for co-sponsors).

---

## 1. TIER 1 (WInS now and Trading Notes, Oct 23)

### 1.1 M125: Which case-stated facts about how Laura thinks should every recommendation visibly mirror?

**One-sentence answer:** Every "how it serves Laura" line should echo one case-stated trait and pass the swap test:
- planning turns her ideas into reality;
- a statistics-trained reader;
- thoughtful risk within an "appropriate balance";
- a product manager's dated steps;
- a public voice whose credibility is an asset;
- flexibility "as the project develops".

This is largely already answered by SH-01 to SH-04 and the D13c checklist. The new part is the mapping to each
Trading Note.

**Evidence**

| claim | source | status |
|---|---|---|
| Criterion 2 rewards recommendations "that can earn her confidence" and tailoring to "Laura's circumstances, priorities, risk considerations, and residency goals" | `competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md` (criteria block) | VRF |
| Case traits: "Thoughtful financial planning and long-term investing will play an important role in turning those ideas into reality" (L38-39); "Statistics & Information Decisions Management … product manager" (L16-17); "willing to take thoughtful risks … appropriate balance" (L69-74); "damage her credibility" (L114); "financial flexibility as the project develops" (L102-103) | `Laura_Gao_2026_Client_Profile.txt` | VRF |
| Past client Ladi Ayoola (2025): "not just about the numbers, but about understanding and connecting with people" | D13b (B2a-Q06), Wharton 2025 finale article | VP (via D13b) |
| The 2022 "never felt more 'seen'" line is a Wharton writer's paraphrase; only "seen" is the client's word | D13b (B2a-Q02) | VP as article text; PARAPHRASE-UNVERIFIED as the client's words |
| No Laura quotes in the Trading Notes or IPS | brief s16; D13c s5.3 | binding rule |
| Swap test: keep a Laura-specific sentence only if it rests on her professional record or the case | D13c s5.1 (from B3b Q12) | rule |
| The TN reflection must explain "How the decision supported the client's goals, funding needs, or risk considerations" in ≤100 words | TN guide L46-52 | VRF |

**Mapping to the three planned WInS notes (securities_v0 ticket).** Elements only; the team writes the words.

| WInS note | case trait it should echo (pick ONE; 100 words is tight) | swap-test check |
|---|---|---|
| Hedge (IEF/TLH) | Planning turns ideas into reality (L38-39): this trade sizes to a specific promise (~$292k for ten $50k payments), so the residency's operating money stops depending on markets | Fails if it says only "reduce volatility" (the guide's own example, which hundreds of teams will copy; M012) |
| Growth (VT) | Thoughtful risk within an appropriate balance (L69-74): stocks hold only money the promise does not need, so a fall shrinks the facility range, never the payments | Fails if it says "Laura likes risk" or "for growth" alone |
| Short Treasuries (VGSH) | Credibility (L114) or flexibility (L102-103): money that can later become an amount she can state to co-sponsors because it is already owned | Fails if it quotes a floor percentage (securities_v0 forbids it) |

- Statistics degree (L16): use it at most once, in the FR or IPS where a probability is defined (securities_v0 s1
  already spends it on VT). In a TN it is decoration.
- Product manager (L17): echoed by dated steps (2027 ladder, 2028 deposit, 2031 floor, 2033 reserve). That belongs in
  the IPS, not in a single TN.
- Past-client evidence ("seen"; "not just about the numbers") comes from finale events, which are outside this run's
  scope. Use it only as the reason for the checklist, never in a deliverable.

**Implication:** a sentence checklist for each TN reflection's "how it serves Laura" line (TN, Oct 23), reused for the
IPS client paragraph. **Deadline tier:** 1. **Confidence:** high. **Changes strategy:** no. **Criterion:** Client
Knowledge and Objectives.

**What this teaches:** a note feels tailored when the reader can point to the line in the case it answers. Adjectives
about the client do not do that.

### 1.2 M018: Does Laura's "floor first, then leap" career story justify "lock the promise, then take risk with the surplus"?

**One-sentence answer:** No, the question is mis-posed. Do not use it.
- "Floor first" is a reporter's causal link: its "So" follows personal material, not a financial plan. D13 ruled
  that it must not be presented as her trait (brief s16).
- Research finds that risk-taking is "highly domain-specific", so a career leap says little about investment risk.
- The IPS risk sentence should rest on the case's "Although … appropriate balance" and the CFA risk-profile rules
  (M019).
- Her two verified risk ideas can appear at most once, in the FR (D13c E2):
  - regret of *not* leaping;
  - letting down early backers is worse than failing yourself.

**Evidence**

| claim | source | status |
|---|---|---|
| "So when she got the book deal with HarperCollins, she gave Twitter her notice." is the Input reporter's sentence (2022-03-07), and its "So" follows personal material | D13b line 254; D13c s3.4 and s7c | VP (reporter's words, not Laura's) |
| Binding: "Do NOT describe a 'floor-first leap' … as Laura's trait" | brief s16 | rule |
| Risk-taking "was highly domain-specific, i.e. not consistently risk-averse or consistently risk-seeking across all content domains" (financial investing is scored separately from social and other domains) | Weber, Blais & Betz 2002, *J. Behav. Decis. Making* 15(4):263-290, abstract on Princeton research portal | VP (abstract) |
| The case itself separates career risk from portfolio risk: "Although she has been willing to take thoughtful risks throughout her entrepreneurial career, she wants her investment team to recommend an appropriate balance…" | case L69-74; R-AN16 | VRF |
| Her verified risk words: "you should always take the jump because you're always going to regret not doing it" (Overachiever 2021) and "letting other people down — people who were your earliest supporters and were the first to believe in you" (Daily Pennsylvanian 2016, student-era) | D13a/D13c (B1b-Q11, D13a-N01) | VP (via D13a; re-checked by D13c) |
| Long-term regrets centre on failures to act; recent regrets on mistaken actions (Gilovich & Medvec 1995, as summarised by a 2023 replication, which found the interaction but a different exact pattern) | Richardson & Gilovich 2023, *R. Soc. Open Sci.* (PMC10282588) | VP (replication paper's summary; the 1995 original was not opened) |

**Numbers:** none needed. The question fails on evidence, not on arithmetic.

**Implication (decision, TN/IPS/FR):**
- No WInS note, TN reflection or IPS sentence cites her career timeline or the book deal.
- The IPS risk sentence uses the case plus the three-part risk profile (M019).
- In the FR, at most one pair of her verified lines, dated and in context (D13c E2).

The honest link to her regret rule runs the other way. Long-run regret is about *not acting*. That is the reason the
growth money holds real stock (M237) rather than the minimum.

**Deadline tier:** 1 (notes cannot be edited once saved). **Confidence:** high. **Changes strategy:** no (it changes
the evidence and the wording only). **Criterion:** Client Knowledge and Objectives.

**What this teaches:** a person who takes big career risks may still want her savings handled carefully. Risk
attitudes differ by domain, and the case's "Although" is signalling exactly that.

---

## 2. TIER 2 (IPS, Nov 6: the strategy freezes)

### 2.1 M019: How should the IPS state a risk tolerance the case never gives?

**One-sentence answer:** State it goal by goal in the three parts professionals use:
- **promise money:** risk need nil, ability nil, so no market risk whatever her appetite;
- **growth money:** risk need low, ability high, investment loss tolerance inferred and unknowable without an
  interview, so real but bounded stock exposure (50-60%, set by the M237 rule);
- **the announced 2031 floor:** ability nil once it is promised.

Name what would change the view, and pre-commit the bad-year decisions so that the plan does not depend on her
composure.

**Evidence**

| claim | source | status |
|---|---|---|
| IPS definition: "outlines an investor's financial goals, risk tolerance, and guidelines…" and helps "make disciplined decisions during changing market conditions" | IPS guide L3-5 | VRF |
| The case states no risk tolerance, benchmark or return target | R-AN17 (word check) | VRF |
| Case risk wording: "Laura understands that investing involves uncertainty and periods of market volatility." (L68-69); "willing to take thoughtful risks … appropriate balance between pursuing growth and protecting the capital required for her goals" (L69-74) | case | VRF |
| Ability inputs: living costs "covered by income and financial resources outside the portfolio"; no additions or withdrawals before 2033 except the two deposits (L61-65); payments "with a high degree of certainty" and teams "may not rely on co-sponsors…" (L91-92) | case | VRF |
| Three risk-profile factors: risk need, risk-taking ability, behavioural loss tolerance | CFA Institute, *Investment Risk Profiling: A Guide for Financial Advisors* (2020), Introduction and Figure 1 | VP |
| "Higher behavioral loss tolerance can be ignored when both the risk need and risk-taking ability are lower" | same, "Reconciling and relating the IRP to a portfolio strategy" | VP |
| "A lower risk need can be discounted when both risk-taking ability and behavioral loss tolerance are higher." | same | VP |
| "Risk-taking ability sets an upper volatility bound … Because risk-taking ability changes (especially as the goal time horizon shortens), this factor must be reassessed regularly." | same | VP |
| "Consequence of failure … refers to the financial and emotional threats an investor faces if a goal is not achieved" | same, Risk Need section | VP |
| "Risk composure refers to the likelihood that in a perceived or actual crisis, an investor will exhibit behavior fundamentally different from her past actions … measured by evaluating an investor's past decisions and actions." | same | VP |
| "Where possible, the IPS should account for known liabilities to lend some quantitative basis to the risk tolerance assessment" and "More nuanced approaches may attempt to define multiple levels of risk associated with … meeting a specific future financial goal" | CFA Institute, *Elements of an Investment Policy Statement for Individual Investors* (2010), s3c | VP |
| Risk as "the probability of failing to reach the threshold level in each mental account, and attitudes toward risk that vary by account" | Das, Markowitz, Scheid & Statman 2010, *JFQA* 45(2):311-334, abstract | VP |
| Contacting the client means disqualification | R-W16 | VP (Phase A) |
| Team docs' "moderate to low capacity" conflates career income risk with portfolio capacity | B4b-05 (FCA FG11/05: capacity for loss is judged by the effect on "standard of living") | VP via B4b |

**Numbers (DER; current plan: growth money 60% stock, 80% locked in 2031; JPM inputs; ASM rate model)**

| measure | value |
|---|---|
| Promise: Treasury cost vs money available (risk need) | $292,264 of $300,000 (F-101): no return above Treasuries is needed |
| Growth money: chance a given year 2028-2030 is down | 27% |
| Growth money: chance of at least one down year 2028-2032 | 62% |
| Growth money: worst single year 2028-2032, median path | about -$3k (-2%) |
| Growth money: worst single year, bad case (p5) | about -$21k (-12%) (thin-tailed model; 2008-type years were worse, D3/M059) |
| Ladder marked to market: chance a given year shows a fall | 14% (p5 fall about -$9k), but the payments' value falls by the same dollars, so they stay 100% covered |
| Whole statement: chance a given year 2027-2032 shows a fall | 10%; at least one down year in 50% of paths |
| 2033 growth money p5 / p50 / p95 | $159k / $207k / $273k (F-401) |
| For contrast, rejected growth-first plan: chance the Dec-2027 statement shows assets below the value of the ten payments | 40% (before the 2028 deposit); 5.4% at some Jan 1 2028-2033 after it |

**Reading (INT):**
- Ability on the growth money is high: a bad year costs facility dollars only, and none of her living costs depend
  on it.
- Ability on the promise is nil.
- Willingness for *investment* losses cannot be measured. CFA measures it by interview or by past investing
  behaviour (VP); we may not interview her, and her public record contains no investing behaviour (D13c V8: "We
  hold no verified statement by Laura about investing").

So the IPS must say the stock share is the team's inference. The design makes that inference low-stakes: if she
turns out to be less composed than assumed, the worst action she could take (selling after a fall) can only shrink
the facility range. It cannot touch the payments, because the ladder is not for sale under the plan's rules.

**What a strong IPS risk passage must contain (spec, not text):**
1. Risk tolerance stated **per goal**, not as one label ("moderate" is what most teams will write; SH-01).
2. For the payments: no risk *needed* (Treasuries already cost less than her deposit) and none *affordable* (the case
   demands high certainty with no outside help). So her appetite for risk is deliberately not used here.
3. For the growth money: she can bear losses (living costs are outside the portfolio; nothing is withdrawn before
   2033), so it holds stocks even though no facility target requires them. The share is set by a stated rule
   (M237).
4. For the 2031 floor: once announced, it carries no risk.
5. That the investment-willingness part is inferred, with what would change it (list below).
6. Case words only (no Laura quotes, no citations: IPS guide L123).

**What would change the inference (the FR's "what would change our view" line):**
- A smaller or later 2028 deposit: ability falls before 2028 (already handled: the payments come first).
- A named facility target or date pressure (the case has none, L104): risk need rises, and the growth money should
  lock earlier rather than take more risk (CFA rule: need cannot exceed ability).
- Evidence that she prefers a larger *certain* facility to a chance at a bigger one: a lower stock share, down to
  the all-Treasury control.
- A lower equity outlook (for example the Vanguard midpoint, section 2.3): the same rule gives 50%, not 60%.
- Nothing she says about career risk: domain-specific (M018).

**Bad-year behaviour and pre-commitments (what Laura will feel and do; my domain).**

Each trap below is documented. Each pre-commitment is one rule. Several already exist for WInS (securities_v0 s5,
parked M007). The 2031 ones are new.

| moment | documented trap (source, status) | what she might feel or do (INT) | pre-commitment (spec) | already covered? |
|---|---|---|---|---|
| Rates rise; the ladder's statement value falls (14% of years) | Myopic loss aversion: investors "distinctly more sensitive to losses than to gains" who "evaluate their portfolios frequently" (Benartzi & Thaler, NBER w4369, VP) | "We lost $9k on the safe part" | Report "10 of 10 payments covered" first and market value second; never sell the ladder after a rate rise | Partly: securities_v0 never-rule 1 (WInS); BS-09 (report funded status first) |
| Stocks fall in 2029-2030, before the 2031 pitch | Break-even effect: after losses, "outcomes which offer a chance to break even are especially attractive" (Thaler & Johnson 1990, VP) | Delay the 2031 lock "until it recovers", or add stock to catch up | The 2031 lock happens on its date (or by its pre-set ratchet, M055) whatever markets did; the stock share only rebalances within its band | Yes, in D8 (written in parallel): rule 3's trigger is the date 2031-01-01, and its governance line says rules change "never because markets moved" (`phase_D/D8_practice.md`, M006). New here: the documented reason (the break-even trap), which the FR can cite |
| Stocks rose strongly before 2031 | House-money effect: "increased risk seeking in the presence of a prior gain" (same, VP) | Announce more than is bought, or keep more in stock | Only the bought amount is announced as the floor; any upside is labelled with its model probability | Partly: brief s8.7 (floor bought), BS-05 (verbs by tier) |
| Long run (2033 and after) | Long-run regrets centre on "failures to act" (Richardson & Gilovich 2023 summary, VP) | "We played it too safe" | The growth money's stock share is set by the M237 rule, never cut to the minimum to look safe | New link (D13c N1 raised the tension) |
| Any year | Contested size of the "behaviour gap": Morningstar estimates investors earned 7.0% vs funds' 8.2% a year (2015-2024), a 1.2-point gap; a 2026 FAJ study of the same sample finds poor timing costs "only 0.10% per year". Morningstar: allocation-fund investors kept "nearly 97%" of the funds' return | Trading on news | Rules above; yearly review on a fixed date. Claim them as **cheap insurance**, not as a proven 1.2%-a-year gain | New evidence; the size is disputed, so do not quote 1.2% as fact |

The Guide supports this framing: "A long-term strategy may include planned adjustments as funding dates approach, but
it should not be rewritten simply because markets move or hindsight reveals a different outcome." (Guide p.5
L156-157, VRF).

**Implication:**
- IPS: a risk passage built per goal (spec above). The 2031 lock's date trigger and "never because markets moved"
  already sit in D8's rule set (M006); D6 supplies the reason.
- FR: the what-would-change list; a one-row "bad year" illustration (growth money -12% in a p5 year means facility
  range smaller by about $21k; payments unchanged).

**Deadline tier:** 2. **Confidence:** high for the framework and the structure; medium for the inferred share.
**Changes strategy:** no. It confirms "risk only in the sleeve", and gives the evidence for D8's 2031 date trigger.
**Criterion:** Client Knowledge and Objectives (also Investment Strategy).

**What this teaches:** "risk tolerance" is not one number. Professionals ask three questions: how much risk a goal
*needs*, how much loss the investor *can* bear, and how she *feels* about losing. When the answers differ between
goals, each pot of money gets its own answer.

### 2.2 M228: What job is Laura hiring an asset manager to do?

**One-sentence answer:** Both jobs, in a fixed order. First, make every number she will say in public true: ten
years of operating money bought in 2027, and a floor bought in 2031. Second, grow what is left so that her facility
contribution is as large as she can responsibly make it. The IPS pitch should name the first job as the central idea
and the second as its purpose. This is largely already answered (stakeholder_map s7 "promise first"); what is new is
the evidence base below.

**Evidence**

| claim | source | status |
|---|---|---|
| Word count in the case: "growth" 1 (L73, "pursuing growth"); "certainty" 4 (L91, L98 twice, L136); "uncertain-" 3; "credib-" 3 (L114, L116, L143); "confiden-" 3; "responsib-" 4; "flexib-" 5 | `D6_behavioural_numbers.py` [5] on the case text | DER from VRF |
| The five things the strategy must do (L134-145): support the payments with high certainty; a responsible facility contribution; address uncertainty; communicate "clearly and credibly"; preserve flexibility. None says "maximise growth" | case | VRF |
| "If Laura promises more than she can ultimately contribute, she could damage her credibility and lose the confidence or participation of co-sponsors." | case L114-115 | VRF |
| Her 2028 money comes from reputation-driven work ("publishing advances, speaking engagements, licensing"), so credibility is part of her income | case L43-45; BS-03 | VRF + INT (Phase A) |
| Criterion wording changed from "would win him/her over as a client" (2022-23, 2023-24) to "can earn her confidence" (2026-27) | B2b s0 | VP (via B2b) |
| "whether a person is seen as credible ultimately depends on whether the person demonstrates good calibration. Credibility depends on whether sources were justified in believing what they believed." | Tenney, Spellman & MacCoun 2008, *JESP* (author PDF, in-press version) | VP |
| After an error, confident witnesses lose more credibility than unconfident ones | Tenney, MacCoun, Spellman & Hastie 2007, *Psychological Science* 18(1) | SNIP (abstract in search results; PubMed and SAGE blocked) |
| Communicating numeric uncertainty caused "only a small decrease in trust in numbers and trustworthiness of the source, and mostly for verbal uncertainty communication" | van der Bles et al. 2020, *PNAS* 117(14):7672-7683, abstract on the University of Groningen portal | VP |

**Reading (INT):**
- In 2031 and 2033 co-sponsors will *see the outcome*. That is exactly the setting where calibration, not
  confidence, decides credibility.
- A firm whose job is "grow her money" will be judged on returns.
- A firm whose job is "make her promises keepable" is judged on whether the numbers held. The case scores the second
  (R-C66, R-S25, R-S28).
- The either/or in the question is false (stats skeptic): R-C38 asks for a balance. So the answer is "promise
  first, then growth", never "not growth".

**What the 50-word pitch and the IPS's first line must contain (spec):**
1. What is secured, and when: the ten payments are bought in 2027, before any risk is taken.
2. What the rest is for: growth for the facility contribution, with flexibility kept.
3. The credibility link: anything announced to co-sponsors in 2031 is already owned.

Exclude: return targets, fund names, "maximise", "guaranteed" without its qualifier, and any Laura quote.

**Implication:** the IPS pitch's central idea (IPS guide L16, "What is the central idea…") and the FR's opening. The
FR could also open from the 2031 conversation and work backwards (B9b idea). That is a presentation choice for the
team.

**Deadline tier:** 2. **Confidence:** high for the direction; the "jobs to be done" label is optional.
**Changes strategy:** no. **Criterion:** Client Knowledge and Objectives (and Creativity & Presentation for the pitch).

**What this teaches:** ask what a client could lose that she cannot get back. For Laura, money can be regrown but a
broken public promise cannot. That tells you which job comes first.

### 2.3 M237: When the designs tie on the median, what rule should choose between them?

**One-sentence answer:** State a two-number safety-first rule: hold the most stock in the growth money that still
leaves about a 19-in-20 chance that it ends 2033 with at least every dollar Laura put in (~$158k). That picks **60%**
stock under JPM's forecast and **50%** under Vanguard's lower midpoint, and it holds with heavier-tailed returns.
- Max-median and max-p5 rules give the extremes (100% and 0%).
- A loss-averse client who compares against the all-Treasury alternative is almost indifferent under JPM.

So the *reference point* decides, and the IPS should name the one it uses.

**Evidence**

| claim | source | status |
|---|---|---|
| Medians barely move with the stock share; more stock buys range, not median | F-407; brief s8.5; B10a | VRF / DER |
| Risk defined as "the probability of failing to reach the threshold level in each mental account" | Das et al. 2010, *JFQA*, abstract | VP |
| People's risk-taking depends on prior gains and losses relative to a reference (house money / break-even) | Thaler & Johnson 1990, *Management Science* 36(6):643-660, abstract on EconPapers | VP |
| "Risk-taking ability sets an upper volatility bound to a portfolio recommendation." | CFA Institute 2020 | VP |
| Vanguard (model run 2026-06-30): U.S. equities 4.2%-6.2% a year over 10 years | B10a s0 item 2 | VP via B10a |
| JPM 2026 LTCMA: U.S. large cap 6.70% compound (7.94% arithmetic, 16.47% vol) | F-301 | VRF |
| Case asks the team to "recommend an appropriate balance" | case L72-73 | VRF |

**Numbers: design table.** Case B inputs: JPM equities 6.70%; sleeve bonds 5.00%, following B10a's correction that
today's Treasury yields are ~1pp above JPM's bond assumption (F-317; ASM). 80% of the growth money is locked in 2031.
Riskless control (the whole growth money in Treasuries to 2033) ≈ $203k (DER from F-012). Money put in = $157,736.

| stock share in growth money | 2033 p5 | p50 | p95 | P(ends below money put in) |
|---|---|---|---|---|
| 0% | $183k | $201k | $222k | 0.0% |
| 20% | $182k | $205k | $231k | 0.0% |
| 40% | $173k | $208k | $252k | 0.6% |
| 50% | $167k | $209k | $264k | 1.8% |
| **60% (current)** | **$161k** | **$210k** | **$277k** | **3.6%** |
| 70% | $155k | $211k | $290k | 5.9% |
| 80% | $149k | $212k | $303k | 8.3% |
| 100% | $137k | $214k | $332k | 12.9% |

Case C uses Vanguard's midpoint (5.2%, JPM vol kept; ASM). Its medians are $201k-$204k for **every** share from 20% to
100%, and the p5 falls from $180k to $130k. P(below money put in) at 50/60/70% is 2.8/5.4/8.4%.

**Which design each rule picks (DER):**

| rule | JPM (B) | Vanguard midpoint (C) |
|---|---|---|
| Maximise the median | 100% | 70% (a flat tie from 20% to 100%) |
| Maximise the bad case (p5) | 0% | 0% |
| **Most stock with P(below money put in) ≤ 5%** | **60%** | **50%** |
| Same at ≤ 10% | 80% | 70% |
| Most stock with P(below $160k) ≤ 5% (ASM threshold) | 60% | 50% |
| Same with $170k | 40% | 20% |
| Loss-averse (λ = 2.25) vs the riskless control | flat: 40-100% all within about $2k of each other; 0% worst | 20% |
| Loss-averse (λ = 2.25) vs money put in | 100% | 80% |
| Fat-tail check (Student-t, 4 degrees of freedom, same volatility): P(below money put in) at 60% / 70% | 3.2-3.8% / 4.9-5.5%: pick unchanged at 60% | not run |

**Reading (INT):**
- Laura's "growth" choice this year is a choice about spread. The rule, not the forecast, decides the share.
- The reference point matters most:
  - Measured against what she put in, almost every design "gains", and a loss-averse reader wants lots of stock.
  - Measured against the all-Treasury alternative (which the FR should show, M034), roughly half of all paths "lose"
    at any stock share, because the median gain over the control is only about $2-9k.
- The money-put-in rule is the simplest to explain and to check. Its two numbers are a threshold and a probability,
  the form a statistics graduate expects (Das et al.).
- It sits closest to the case's "protecting the capital" (INT: "capital required for her goals" mainly means the
  payments, so this is an extension, not the case's definition).
- It answers her long-run inaction regret: it does not set stocks to the minimum.
- **The threshold and the 1-in-20 are team choices (ASM).** The table shows what other choices would pick.

**Implication:**
- **Decision (IPS):** one rule sentence in the team's words. It must contain the threshold (money put in), the
  probability (about 19 in 20) and what it applies to (the growth money only).
- **Number:** growth-money stock share 60% if the team keeps JPM as its base; 50% if it adopts the more cautious
  house view. Do not quote the probability to one decimal in the IPS.
- **FR:** the design table (four rows is enough: 0/40/60/100%) with the all-Treasury control as a reference line.
  Chart: a p5-p50-p95 "whisker" per design, with the median band nearly flat (data: the table above).

**Deadline tier:** 2. **Confidence:** medium. The numbers are model properties; the rule is a judgement.
**Changes strategy:** no. It confirms the provisional 60/40 (WInS VT 20.5% / VGSH 12.5% unchanged) and gives it a
stated reason. It would move to 50% only if the team adopts the Vanguard view.
**Criterion:** Investment Strategy (also Portfolio Analysis).

**What this teaches:** when two choices have the same middle outcome, you are really choosing how wide the good and
bad outcomes spread. Say what you are measuring against before you say what you chose.

---

## 3. TIER 3 (Final Report, Dec 4)

### 3.1 M197: How wide can the stated 2031 range be before non-specialists find it useless?

**One-sentence answer:** Quote the range Laura would state *in 2031*: from the bought floor to about the 90th
percentile of her 2033 total. At an 80% lock share that is about 1.3x top-to-bottom ($165k-$215k at the median
state), not today's 1.7x spread.
- Research says people prefer ranges "as precise as warranted by the information available, but not more precise",
  and honest numeric ranges cost little trust.
- Keep the lock share between 70% and 90%. Below 70% the range tops 1.5x; at 100% it becomes the "one exact amount"
  the case rejects.
- The exact point at which a range becomes "useless" is not established by any study we can verify (ASM).

**Evidence**

| claim | source | status |
|---|---|---|
| Investors' preference for (im)precision "peaks for low levels of imprecision and diminishes when the range gets wider"; they "favor forecasts that are as precise as warranted by the information available, but not more precise" | Du, Budescu, Shelly & Omer 2011, *OBHDP* 114(2):179-189, abstract on RePEc | VP (both phrases verbatim) |
| "Coarse (imprecise) judgments are less informative than finely grained judgments; however, they are likely to be more accurate"; people "might accept errors in the interest of securing more informative judgments" | Yaniv & Foster 1995, *J. Exp. Psych.: General* 124(4):424-432, p.424 (author-hosted scan, read as an image) | VP |
| Numeric uncertainty caused only a small trust decrease, "mostly for verbal uncertainty communication" | van der Bles et al. 2020, *PNAS*, abstract | VP |
| Credibility depends on calibration once outcomes are known | Tenney, Spellman & MacCoun 2008 | VP |
| Case: "Rather than promising one exact amount, she wants to communicate a credible range"; "state how confident they are that her 2033 contribution will fall within that range" | case L115-118 | VRF |
| The confidence statement is two-sided: a range wide enough to be safe becomes useless; one narrow enough to be useful becomes risky | R-AN9 | VRF |
| Du et al. studied earnings forecasts read by investors, not arts co-sponsors, and no numeric threshold appears in the abstract | stats skeptic note, M197 | limit |

**Numbers (DER; stock 60% of the unlocked part; top = p90 of the 2033 total, given the 2031 state)**

| lock share in 2031 | top ÷ bottom (p90 top) | (p95 top) | median ÷ floor |
|---|---|---|---|
| 60% | 1.81x | 1.85x | 1.68x |
| 70% | 1.52x | 1.55x | 1.44x |
| **80% (model)** | **1.30x** | **1.32x** | **1.25x** |
| 90% | 1.13x | 1.14x | 1.11x |
| 100% | 1.00x (one amount) | 1.00x | 1.00x |

- With 100% stock in the unlocked part the ratios barely change: 1.34x at an 80% lock.
- The ratio does not depend on the sleeve's size in 2031, only on the lock share and the unlocked part's mix.
- In dollars (80% lock; 2033 US$; model, not forecasts):
  - weak 2031 state (sleeve p10): floor $134k, top $175k;
  - median state: floor $165k, top $215k;
  - strong state (p90): floor $204k, top $265k.
- Today's 2026 view of the 2033 surplus (p5-p95): $159k-$273k, 1.72x.
- Confidence "within the range" at the 2031 view:
  - about 0% chance of falling below the floor (it is bought; residual risk U.S. default);
  - about 10% chance of landing above the top.

  So it is "about 9 in 10", two-sided, with the model named (R-AN9, SH-04).

**Reading (INT):**
- Du et al.'s "as precise as warranted" is the key idea. In 2031 the information *warrants* a narrow range, because
  80% of the money is already a bought Treasury and only two years of risk remain on the rest.
- Quoting today's 1.7x spread would be less precise than the information allows, and would read as "we don't know".
- A single number would be more precise than warranted, and the case forbids it.
- The Final Report must still give a dollar range now (R-C68). So present it as a rule plus the three illustrative
  2031 states above (parked M040's answer), not as one 1.7x band.

**Implication:**
- **Number (FR):** range = bought floor to about the p90 of the 2033 total, about 1.3x at an 80% lock.
- **Decision input for D3's M060 (lock share):** behavioural evidence supports 80-90% and argues against anything
  below 70%. It cannot choose between 80% and 90%.
- **Chart (FR):** three bars (weak, median and strong 2031 states). Each shows the floor as a solid block and the
  upside to p90 as a lighter block, labelled "about 9 in 10 within". Data: the dollar rows above.

**Deadline tier:** 3. **Confidence:** medium (the ratios are model properties; the usefulness threshold is ASM).
**Changes strategy:** no. It supports the 80% lock share already in the model. **Criterion:** Creativity and
Presentation ("communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to
prospective co-sponsors").

**What this teaches:** a range is useful when it is as narrow as your knowledge honestly allows. By 2031 the
bought floor is what makes a narrow range honest.

---

## 4. Cross-question notes for the main loop

- **Consistency:**
  - The M237 rule gives 60% under the same JPM inputs that produce F-401. The WInS ticket (VT 20.5% / VGSH 12.5%)
    needs no change.
  - If D3's model v2 adopts sleeve bonds near 5%, the rule's pick is unchanged (case B).
  - If the team adopts Vanguard's view, the pick is 50%: VT about 17% / VGSH about 16% of the WInS book (ASM
    arithmetic on securities_v0's 33% growth money), for S3 to recompute.
- **The 2031 clause is already in D8's rule set:** a dated trigger (2031-01-01) plus a governance line saying rules
  change "never because markets moved" (`phase_D/D8_practice.md`, M006). D6 adds the behavioural evidence for why it
  matters (break-even after a fall; house money after a rise). No second clause is needed; the FR can cite the
  evidence when it reports that the rule "fired as written".
- **Quotes:** none of the six answers needs a Laura quote in the TN or IPS. The FR may use the D13c E2 pair once.
- **Parked items this supports:** M007 (bad-year rule), M033 (goal-by-goal risk to the first reader), M040 (range as
  a rule with an illustration).

---

## 5. Sources (accessed 2026-09-27/28 UTC)

Primary pages read with `research/insight_v1/scripts/fetch_text.py` (VP) unless marked:
- Du, Budescu, Shelly & Omer (2011), "The appeal of vague financial forecasts", *OBHDP* 114(2):179-189. RePEc
  abstract: https://ideas.repec.org/a/eee/jobhdp/v114y2011i2p179-189.html (both quoted phrases grep-verified).
- Yaniv & Foster (1995), "Graininess of Judgment Under Uncertainty: An Accuracy-Informativeness Trade-Off", *JEP:
  General* 124(4):424-432. Author-hosted scan: https://deanfoster.net/research/YanivFoster1995JEPG.pdf (no text
  layer; page 424 read as an image).
- van der Bles, van der Linden, Freeman & Spiegelhalter (2020), *PNAS* 117(14):7672-7683. Abstract:
  https://research.rug.nl/en/publications/the-effects-of-communicating-uncertainty-on-public-trust-in-facts/ (PNAS
  returned 403).
- Tenney, Spellman & MacCoun (2008), "The benefits of knowing what you know (and what you don't): How calibration
  affects credibility", *JESP*. Author PDF:
  https://gspp.berkeley.edu/archived/files/research/pdf/TenneySpellmanMacCoun_JESP_inpress.pdf
- Tenney, MacCoun, Spellman & Hastie (2007), *Psychological Science* 18(1): SNIP only (PubMed bot check; SAGE 403;
  eScholarship returned no text): https://pubmed.ncbi.nlm.nih.gov/17362377/
- CFA Institute (2020), *Investment Risk Profiling: A Guide for Financial Advisors*:
  https://rpc.cfainstitute.org/sites/default/files/-/media/documents/survey/investment-risk-profiling.pdf
- CFA Institute (2010), *Elements of an Investment Policy Statement for Individual Investors*:
  https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
  (it does not itself use the words "ability and willingness"; that phrasing is the CFA curriculum's, SNIP).
- Das, Markowitz, Scheid & Statman (2010), *JFQA* 45(2):311-334:
  https://ideas.repec.org/a/cup/jfinqa/v45y2010i02p311-334_00.html
- Benartzi & Thaler, "Myopic Loss Aversion and the Equity Premium Puzzle", NBER w4369 (1993; *QJE* 1995):
  https://www.nber.org/papers/w4369
- Thaler & Johnson (1990), *Management Science* 36(6):643-660:
  https://econpapers.repec.org/RePEc:inm:ormnsc:v:36:y:1990:i:6:p:643-660
- Weber, Blais & Betz (2002), *J. Behav. Decis. Making* 15(4):263-290:
  https://collaborate.princeton.edu/en/publications/a-domain-specific-risk-attitude-scale-measuring-risk-perceptions-
  ("highly domain-specific" grep-verified; the abstract's other findings are not used).
- Richardson & Gilovich (2023), replication of Gilovich & Medvec, *Royal Society Open Science* (PMC10282588):
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10282588/ (the 1995 original was not opened: its host failed TLS).
- Morningstar, *Mind the Gap 2025* (US):
  https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/blt2c5c4d9171638c42/689b424311f3880edc4b4813/US_Mind_the_Gap_2025.pdf
- Fulkerson, Jordan, Riley & Yan (2026), "Bad Timing Does Not Cost Investors 15% of Their Funds' Returns", *FAJ*,
  abstract: https://rpc.cfainstitute.org/research/financial-analysts-journal/2026/bad-timing-does-not-cost-investors-funds-returns
- Tversky & Kahneman (1992), *J. Risk Uncertainty* 5:297-323: loss-aversion coefficient 2.25 is SNIP (the paper was
  not opened; the value is only a tested parameter here).

Repo files (VRF or labelled): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L16-17, L38-39,
L43-45, L61-74, L91-92, L102-104, L114-118, L134-145); `2026_WGY_Investment_Policy-FINAL.txt` (L3-5, L16, L20, L123);
`2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L46-53); `2026_WGY_Investment_Competition_Guide.txt` (L35, L70,
L156-157, L182-183); `SMApply_Deliverables_Page_2026-09-27.md` (criteria); `research/insight_v1/phase_A/`
(case_register R-AN9/R-AN16/R-AN17; fact_register F-101, F-301, F-317, F-401-F-409; stakeholder_map SH-01 to SH-05,
BS-03, BS-09, s7); `phase_B/B10a_contrarian.md`, `B2b_why_laura_intent.md`, `B4b`, `B6b_cosponsors.md` (Q18);
`phase_C/survivors.json`, `parked.json`; `phase_D/D13a*, D13b*, D13c_voice_map.md`;
`wins_now/securities_and_allocation_v0.md`; `research/verified_2026-09-27/strategy_mc.py` (engine reproduced).
Script: `research/insight_v1/scripts/D6_behavioural_numbers.py`.

---

## What this teaches

- **Ask three risk questions, not one.** How much risk does the goal need? How much loss can she bear? How will she
  feel when she loses? For Laura the answers differ between the promise and the growth money, so each gets its own
  answer. That is what "tailored" means.
- **A bold career does not mean a bold portfolio.** Risk attitudes differ by domain. The case's "Although" says the
  same thing in one word.
- **Plan for the bad year before it arrives.** A down year is more likely than not before 2033. The plan's
  strength is that every bad year has one meaning (a smaller facility range) and one pre-agreed response. That is
  easier to live with than a plan whose bad years raise the question "are the payments still safe?"
- **When the middle outcome ties, the comparison point decides.** Say what you measure against (the money she put
  in, or the all-Treasury alternative) before you pick a number.
- **Honest ranges earn trust.** People trust sources whose confidence proves justified. Give the narrowest range your
  bought floor supports, say how sure you are on both sides, and name the model.
- **Evidence can be contested.** The famous "1.2% a year behaviour gap" has a serious 2026 rebuttal. Use rules
  because they are cheap insurance, not because a disputed number says they pay.
