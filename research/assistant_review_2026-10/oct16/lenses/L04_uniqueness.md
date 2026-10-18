# L04 Special but not stupid: how Team Caplet can stand out without being gimmicky or wrong

Prepared Fri 16 Oct 2026 (Sydney) for Team Caplet. AI-generated analysis (Claude). It is knowledge, not text to
submit. It contains no Trading Notes reflections, IPS sentences, pitch or Final Report prose. If the team uses any of
it, record that use in the Final Report's Works Cited (Wharton AI policy).

Labels: VERIFIED = I read it on the source today; MODEL = a computed estimate; INFERENCE = my reading;
UNVERIFIED = could not confirm. Repo paths are in `/home/user/caplet-investment` unless marked `caplet-latest/`
(the 16 Oct branch copy). "KB" = `oct16/research/KB_what_wins.md`. "15 Oct brief" = `oct14/final.md`.
New / known-deeper / known-repeat is relative to the 15 Oct brief.

My own script and output: `oct16/lenses/L04/hist_ladder.py` and `oct16/lenses/L04/hist_ladder_output.txt`.

---

## 0. Bottom line (eight points)

1. **The case pushes almost everyone to the same safe shape.** Wharton's own example trade note buys an
   intermediate Treasury bond ETF "as the residency funding date approaches" (TNA:36-39). Most competent teams will
   submit a balanced portfolio that glides into bonds before 2033, a Monte Carlo "95%" for certainty and a
   percentile band for 2031. The best teams will also build a bond ladder. So **Caplet's structure alone will not
   set it apart from the teams it must beat.** Caplet's own AI research said so on 28 Sep: against "a same-plan
   rival with warmer, plainer words: we have no structural edge" (`research/insight_v1/why_us.md:90`).
2. **Caplet's best differences are buried.** Judges will see about 300 words of TNA reflections, 550 words of IPS
   and the Final Report. Caplet's distinctive ideas sit in an 831-page record, a 27-page brief and team notes. IPS V5
   shows two of my top eight clearly. It shows the "two deposits, two jobs" idea, the "why now" fact and the
   co-sponsor evidence weakly or not at all.
3. **Pick at most three signature ideas and repeat them in the same words in all three deliverables.** My
   suggestion (the team decides): (a) each deposit has one job; (b) Laura only promises what is already bought; (c)
   a co-sponsor range built on how people actually read promises and uncertainty.
4. **The co-sponsor clause is Caplet's biggest open chance.** It is new to the rubric this year
   (`deliverables.txt:59`). Caplet already holds verified research that most teams will not have (sections 3-4). It
   needs re-checking, which I did for five sources today. It must go in the Final Report, because the IPS allows no
   citations.
5. **A strong "why now" fact survives on the right basis, but the team's version of it is stale.** On Caplet's
   actual holdings, $300,000 would have bought all ten payments on 8.4% of trading days since 2000, and on no day
   from 13 Jul 2007 to 22 Sep 2026 (MODEL, my re-run). The team notes' "cheapest since May 2002", "11% of days" and
   "$289,119" figures use the old STRIPS-style basis and must not be quoted.
6. **Ladder-cost conflict: settled, and it matters for differentiation.** I re-ran both methods on the 15 Oct
   curve. For anything about Caplet's own plan, use the holdings basis: **about $298.6k, room about $1.4k (4.7bp)**.
   The number sheet's $294.5k prices a perfectly dated ladder that Caplet does not own (section 1.3). So "the first
   deposit buys all ten payments" must be stated as a rule with an overflow step, not as a fact.
7. **Two moves in the 16 Oct commit work against standing out.** [AI] suggestion 8 deletes V5's only defence of
   one-issuer concentration, although the Strategy criterion scores "appropriate diversification". Accepting AI
   wording also turns the team's most distinctive asset, its own voice and real experience, into the voice every
   AI-assisted team has.
8. **Clever ideas to avoid** (section 6): themed stock picks (Taiwan ETF, gold), quant showcases, marketing the AI
   "council", the "case PDF was timed to the curve" story (false on the holdings basis), Laura-biography details and
   quotes, Chinese-language text, comic art in the written round, "99.4%"-style precision, and Australian branding.

---

## 1. Step 1: what the modal competent team will submit

### 1.1 Prediction (INFERENCE, with the evidence that drives each part)

| Element | What most competent teams will do | Evidence that pushes them there |
|---|---|---|
| Core shape | Growth now, then a shift into bonds as 2033 nears (a "glide path"); a 2033 reserve carved from whatever has grown | Wharton's example note: an "intermediate-term U.S. Treasury bond ETF ... as the residency funding date approaches" (`2026_WGY_Trading_Notes_Analysis-FINAL.txt:36-39`); IPS prompt "How will the portfolio's asset allocation and composition change as future funding needs approach" (`2026_WGY_Investment_Policy-FINAL.txt:22-23`); "A long-term strategy may include planned adjustments as funding dates approach" (`2026_WGY_Investment_Competition_Guide.txt:156`); the case sets the reserve aside "At the beginning of 2033" (`Laura_Gao_2026_Client_Profile.txt:94-96`) |
| Mix | About 50-70% stocks before 2028, falling later; "balanced" | "an appropriate balance between pursuing growth and protecting the capital" (case:72-74). Caplet's own first instinct was "the team's original ~75% equity + later reserve" (CLAUDE.md, strategy status section) |
| Certainty | "95% probability of funding" from a Monte Carlo | Amity's public Monte Carlo of how long a gift fund lasts (KB 3.2); the AI tournament's "typical strong team" archetype used "a Monte Carlo 95% and staged reserve" (`research/insight_v1/why_us.md:21`) |
| 2031 range | A percentile band (for example p10-p90) with "80% confidence" | Same Monte Carlo habit; the case asks for "the dollar range ... and state how confident" (case:117-118) |
| WInS book | Many trades; stocks and sector ETFs; a bond ETF (IEF, BND, TLT); client-themed picks | Last year's Knox team screened 70 tickers, used ESG scores and themed sleeves (`team/google_drive/2025_knox_wharton.md:188,198-200`); Caplet's own 5 Oct challenge proposed "normal stock and ETF picking; Taiwan (EWT) and gold (GLD)" (`team/google_drive/final_report.md:39`) |
| Packaging | A themed name and metaphor | "at least six football or 'better future' names in the 2026 Top 50" (KB 5.1, P5); Knox 2025 used "Builder Mindset" and Foundation/Construction/Transformation sleeves (`2025_knox_wharton.md:188,846`) |
| Voice | Polished, generic, often AI-assisted | Wharton had to tell 2025-26 semifinalists: "We are looking for your authentic team voice, not generated or generic responses" (KB 4.2, [D1], re-opened) |

### 1.2 What the strongest rivals will do (the teams Caplet must beat)

- Wharton set a fixed-payment problem before: in 2021-22 the client had to fund a scholarship "for at least 10
  years" (KB 3.3, [N22], re-opened). How finalists answered is not public (UNVERIFIED). INFERENCE: some strong teams
  will see that Treasuries can lock the ten payments. KB 3.3 reaches the same view: "the edge must come from
  clarity, client insight and defence, not from the idea itself."
- So in the Top 50 pool, Caplet's "buy the payments first" is likely to be one of several ladder answers. Caplet's
  AI research said the same on 28 Sep: "Our edge is not 'buy the payments first'. That is the textbook answer"
  (`research/insight_v1/why_us.md:3`).

### 1.3 The ladder-cost conflict, and which figure each differentiator may use

I re-ran both methods on the official 15 Oct treasury.gov curve
(`caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`) using
`oct16/research/KB_verify/num/reconcile.py`. My output matches the KB exactly:

| Dates priced to | Forward value at 1 Jan 2027 | Curve unchanged on 1 Jan 2027 |
|---|---|---|
| Payment dates, 1 Jan 2033-42 (a perfectly dated ladder) | $294,461; room $5,539 (19.0bp). The number sheet prints $294,453 | $295,246; room $4,754 (16.3bp) |
| Maturities of Caplet's holdings (iBonds 15 Dec 2032-36; Feb-2037, May-2038, Nov-2039/40/41) | $297,847; room $2,153 (7.4bp) | **$298,628; room $1,372 (4.7bp)**: the lenses' figure |

- **Why they differ.** The number sheet prices each payment to `dt.date(y, 1, 1)`
  (`caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:85-87`). Caplet's bonds mature 2 weeks to 10.5 months
  before each payment, so each $50,000 has to be bought for an earlier date and costs more. That date effect is
  about $3,400 of the gap. The curve basis (forward or unchanged) adds about $800. The curve date and the ten
  payments are the same in both.
- **Which is right for which claim.** For any claim about Caplet's plan or WInS book, use the holdings basis: about
  $298k, room about $1.4k-$2.2k (5-7bp), and give the date and the basis. Use $294.5k only for "a ladder dated to
  each payment would cost", which Caplet cannot buy because WInS lists no such bonds.
- **Effect on differentiation.** The "two deposits, two jobs" idea (UNIQ-03) and the "why now" fact (UNIQ-04) both
  rest on "$300k buys all ten". On the holdings basis that is only just true on 15 Oct. The lenses' model gives about
  a 44-45% chance it is untrue by January (MODEL, L03/L08; not re-run by me). So both ideas must be framed as a
  rule (the first deposit buys the payments; any gap is the first call on the second deposit), never as a fact.

---

## 2. Step 2: where Caplet already differs, and whether a judge can see it

| Caplet difference | True today? | Visible to a judge now? | Where it sits |
|---|---|---|---|
| Ten payments matched to dated holdings from day one, not a glide path | Yes (11 filled orders) | **Yes**: WInS notes, IPS V5:20, 24 | TNA, IPS |
| Uses defined-maturity iBond ETFs because WInS lists no Treasury for Feb 2031-Feb 2036 | Yes (journal, `final_report.md:34`) | **Yes**, in four notes (`05_...wins_trading_notes.md:19-22`) | TNA |
| Owned floor plus a capped top for 2031 | Mostly (the IBTM payout is not fixed) | Partly: V5:30 states it as a formula with "cannot miss" | IPS |
| "Each deposit has one job" (savings buy the promise; earnings fund the building) | As a rule, yes; as a fact, only just (1.3) | **No**: in `why_us.md:3` and team notes, not as the idea in V5 | Buried |
| Evidence on how funders count gifts and read uncertainty | Yes, for five sources re-checked today (section 4) | **No**: `research/insight_v1/phase_B/B6a/B6b`, team notes `notes_and_discussions.md:209-228` | Buried |
| Why now: high yields made certainty affordable | Yes on the holdings basis (UNIQ-04) | **No**; team version stale | Buried |
| A pre-set test in a trade note (IBTR "about 0.2 percentage points") | Was true on 6 Oct; nearly used up by 15 Oct | Yes (`05_...md:15`) | TNA |
| Very few trades (11 of 200); hold by design | Yes | Visible in WInS, but can read as passive | TNA, Final Report |
| Real dated changes (sector-minimum myth, STRIPS dropped, stale bond prices caught) | Yes (`final_report.md:32-40`) | **No** until the Final Report | Journal |
| Price of certainty measured (smaller-floor test) | On the old model only | **No** (`notes_and_discussions.md:276-301`) | Buried, stale |

**Reading.** Of the eight ideas I keep in section 5, a judge can see two clearly today (dated matching; iBonds as
dated cash) and one partly (the owned floor). The rest sit in files judges never read.

---

## 3. Step 3: 30 candidate differentiators

C1 "Each deposit has one job" as the central idea. C2 "Promise only what is already bought" as the single rule.
C3 Why now, on the holdings basis. C4 Certainty defined by price, plus named leftover risks, not by a model
percentage. C5 Make C4 literally true (a ladder that is safe even if coupons earn 0%; L03 STRAT-04). C6 The 2031 range
as three numbers: bought bottom, rule-set top, chance of reaching the top (in words and numbers). C7 Lead-gift
evidence for the case's "meaningful contribution" claim. C8 "Bankable bottom": funders count written pledges.
C9 "Operations pre-funded" as the funder-facing headline. C10 Price of certainty against an all-Treasury baseline.
C11 Number labels: market price (dated), model or assumption. C12 A "who absorbs each loss" table of named bad worlds.
C13 The IPS as a short numbered rulebook in time order. C14 Logged decisions *not* to trade, using pre-set triggers.
C15 Three different kinds of decision in the TNA trio (L05 TNA-08). C16 The IBTR reflection: a pre-set test that the
market nearly used up. C17 An honest account of the 7 Oct mis-click. C18 Dated adaptation stories (sector-minimum
myth, 6 Oct email, stale prices). C19 Darren's dissent recorded and answered with numbers. C20 The time-zone detail
(orders at 12:30 AM Sydney; learning about next-open fills). C21 An outsider's currency view (USD promise, NT$ costs).
C22 Strategy name tied to her book *Messy Roots*. C23 The 2021-22 precedent: the same ten-year promise was
unaffordable in 2021. C24 A comic-panel explainer for a graphic-novelist client. C25 Bilingual (Chinese) fundraising
excerpt. C26 Taiwan equity (EWT) or TSMC tilt for "client fit". C27 A Monte Carlo fan chart with "95%" as the headline.
C28 One sentence mapping the WInS book to Laura's plan. C29 A dated "promise card" with a re-quote rule for the
two-year campaign. C30 IBTM as the semifinal ETF case study (the two-job fund).

## 4. Step 4: the "special but not stupid" test

Key: Y = yes, P = partly or with care, N = no. "Cost" = team time (L low, M medium, H high).

| # | Allowed | Serves Laura | One sentence | True and defensible | Cost | Backfire risk | Verdict |
|---|---|---|---|---|---|---|---|
| C1 | Y | Y | Y | P (rule, not fact; 1.3) | L | Low if framed as a rule | **KEEP (top)** |
| C2 | Y | Y | Y | P (IBTM payout not fixed; "bought", not "owned $145k" in 2031) | L | Medium if absolute words return | **KEEP (top)** |
| C3 | Y | Y | Y | Y on holdings basis (UNIQ-04) | L | Low; date it | **KEEP** |
| C4 | Y | Y | Y | P (coupon reinvestment) | L | Medium | **KEEP, depends on C5 or honest wording** |
| C5 | Y | Y | Y | Y (L03 STRAT-04, MODEL) | M (strategy decision before 6 Nov) | Low | Dependency (L03 owns it) |
| C6 | Y | Y | Y | Y (sources re-checked) | M | Low | **KEEP (top)** |
| C7 | Y | Y | Y | Y with caveats (US small donors) | L | Medium if over-claimed | Merge into C6 |
| C8 | Y | Y | Y | Y (one US funder's rules; illustration only) | L | Medium if presented as universal | Merge into C6 |
| C9 | Y | Y | Y | P (supports "funders ask who pays to run it", not "rarely pay") | L | Medium | **KEEP (fix V5 pitch claim)** |
| C10 | Y | Y | Y | Needs re-run on WInS basis | M | Low | **KEEP** |
| C11 | Y | Y | Y | Y | L | Low | **KEEP** |
| C12 | Y | Y | P | Y | M | Low | Known (CLIENT/STRAT lenses); fold into C10 |
| C13 | Y (IPS:66, 101-102) | Y | Y | Y | L | Low if word count checked | **KEEP** |
| C14 | Y | Y | Y | Needs dated logs | L | Reads passive if unlogged | **KEEP** |
| C15 | Y | Y | Y | Y | L | Low | Known (L05) |
| C16 | Y | Y | Y | Y with date | L | Medium if "about 0.2" not dated | Merge into C14 |
| C17 | Y | P | Y | Y | L | **High**: discloses AI operated WInS | Conditional (UNIQ-13) |
| C18 | Y | P | Y | Y (journal) | L | Low | **KEEP (Articulation)** |
| C19 | Y | Y | Y | Needs a logged outcome | L | Low | Known (L10 TP-13); fold into C18 |
| C20 | Y | N (team, not client) | Y | Y | L | Low if brief | Articulation only, one line |
| C21 | Y | Y | Y | Y | M | Low | Known (L02 CLIENT-10); not an "Australian" angle |
| C22 | Y | P | Y | P (idiom collision, UNIQ-14) | L | Medium | Test it |
| C23 | Y | Y | Y | Y (MODEL) | L | Low | Merge into C3 |
| C24 | Format UNVERIFIED for the Final Report; banned in IPS (IPS:123) | N | Y | n/a | H | High (pandering; AI art banned as own work) | AVOID in writing; finale-only option |
| C25 | UNVERIFIED | P | N | Risky (translation) | H | High | AVOID |
| C26 | Y | N | Y | N (not a hedge; strategy frozen) | M | High | AVOID |
| C27 | Y | P | Y | P | M | Looks modal | AVOID as headline |
| C28 | Y | Y | Y | Y | L | Low | Known (L08 COH-06) |
| C29 | Y | Y | Y | Y | L | Low | Merge into C6 |
| C30 | Y | Y | Y | Y | M | Low | **KEEP (finale prep, inside the Final Report)** |

---

## 5. The keepers: eight signature moves (what each must achieve, and where it goes)

No prose here. Each item names the deliverable, what a fix must achieve, the evidence and the likely judge question.

| # | Move | Deliverable | Must achieve | Judge question to rehearse |
|---|---|---|---|---|
| K1 | Each deposit has one job (C1) | IPS pitch and IPS; Final Report headline; TNA IBTM and IBTR reflections use the same words | One sentence a non-finance adult can repeat. Stated as a rule with the overflow step. No dollar figure in the pitch | "What if $300k isn't enough in January?" |
| K2 | Promise only what is already bought (C2 + C8) | IPS rule; Final Report co-sponsor text | Every dollar Laura names in 2031 has a dated holding behind it. Uses "bought, maturing Dec 2032", not "owned $145k" (in 2031 the fund is worth less than its end value) | "IBTM's payout isn't fixed. How can the floor be a floor?" |
| K3 | A co-sponsor range built on evidence about promises (C6, C7, C9, C29) | Final Report (fundraising excerpt plus sources); one principle in the IPS | Three numbers: bought bottom, rule-set top, and the chance of reaching the top in words and a number. Dated, with a re-quote rule. No "99%" | "How confident are you, and why that number?" |
| K4 | Why now (C3 + C23) | Final Report (a history chart is allowed there; IPS bans charts); finale; at most one clause in the IPS | One dated, sourced fact on the holdings basis, plus what the plan does if prices change | "Isn't this just luck with rates?" |
| K5 | Certainty by price, with named leftover risks (C4, depends on C5) | IPS; Final Report | The case's three asks (define, explain how evaluated, assumptions; case:97-99) answered in Caplet's own terms. Every risk word is literally true | "So the payments are risk-free?" |
| K6 | The price of certainty against an all-Treasury baseline (C10) | Final Report | Shows caution as a measured choice: what more stocks add at the middle and cost in bad years, re-run on the WInS basis | "Isn't 7-9% in stocks too timid for an entrepreneur?" |
| K7 | The IPS as a numbered rulebook in time order (C13) | IPS | About six rules, each a decision with its trigger; a reader can find the 2027, 2028, 2031 and 2033 rules at a glance | "What would make you change the plan?" |
| K8 | Dated evidence of discipline and learning (C11, C14, C16, C18, C30) | TNA (IBTR reflection), Final Report (Articulation, Portfolio Analysis), finale | Every number has a date and a basis label. Logged no-trade decisions. Real adaptation stories with who and when. IBTM ready as the ETF case study | "You made 11 trades. What did you actually do?" |

---

## 6. Clever ideas to AVOID, and why

| Idea | Why to avoid | Evidence |
|---|---|---|
| Themed stock picks for "client fit" (Taiwan ETF EWT, TSMC, publishers) and gold (GLD) | Not a hedge for NT$ facility costs (adds Taiwan stock risk); breaks "promise only what's bought"; the strategy freezes on 6 Nov; Wharton calls such tools "NOT investment strategies" | `final_report.md:39`; IPS:72-74; KB 4.2 [D4] |
| A quant showcase (HAR model, optimisers, an "8-model suite") | Judges: "hiding behind fancy terms and formulas"; a nine-stage quant pipeline stopped at the Top 50 | KB 4.2 [N12]; KB 3.2 (Hotchkiss); `notes_and_discussions.md:268-270`; `docs/benchmark_against_previous_teams.md:21-25` |
| Marketing the "AI council of 90 agents" as a strength | Ownership and plagiarism risk ("words or ideas"); paid consultants and agents are a disqualification category; it undercuts the team voice. Disclose it in Works Cited, never sell it | L09 INT-04, INT-07; `notes_and_discussions.md:74-102` |
| "Wharton timed the case PDF to the first day the ladder fell under $300k" | Speculative and presumptuous. **False on the holdings basis**: the first day under $300k in 2026 was 23 Sep, not 10 Sep (my re-run) | `notes_and_discussions.md:173`; `oct16/lenses/L04/hist_ladder_output.txt` |
| A UK pension "mature promise, 90% hedged" standard | UNVERIFIED here; a foreign regulatory frame adds jargon | `notes_and_discussions.md:203` |
| Laura-biography details (internships, CV), her quotes, or the case pull quote as hers | Pull quote not verifiable as hers; extra biography is unchecked and can read as creepy for a real person; no Laura quotes rule | 15 Oct brief §2; L02 CLIENT-15; `notes_and_discussions.md:232-246` |
| Chinese-language (Traditional) fundraising text | Hard to verify; AI translation would be AI work; judges may not read it | INFERENCE |
| Comic-style art in the written round | Images banned in the IPS (IPS:123); the 2026-27 rubric dropped "visually pleasing ... many creative elements" (KB 2.3); AI art cannot be passed off as the team's own | IPS:123; KB 2.3 |
| "99 times in 100" or "99.4%" | The cap makes it true by construction, so it is circular, and it looks like the modal Monte Carlo percentage | `caplet-latest/.../IPS_number_sheet.md:17`; `IPS_v5_suggestions.md:20`; L03 STRAT-07 |
| Australian branding, or "first Australian team" claims | No Australian Top 50 since 2021-22; media "firsts" are often wrong; it does not serve Laura | KB 5.2; R3 4.3 |
| Talking about WInS gains or rank | "Your WInS standings have no impact" | KB 4.2 [X1]; Guide:74-78 |
| A second metaphor layer (tree plus "the Dream" plus sleeve names) | Last year's lesson: "over-complex for the insight"; one image at most | CLAUDE.md "Team" section; `notes_and_discussions.md:117` |

---

## 7. Findings

### UNIQ-01 (high, new). The case funnels competent teams into one shape; Caplet must win on three repeated ideas, not structure
- **Problem.** Wharton's own example note, the IPS prompts and the case's 2033 reserve wording all point to a
  glide path (1.1). Strong teams will also ladder (1.2). Caplet's 28 Sep research admits there is "no structural
  edge" against a same-plan rival with plainer words (`research/insight_v1/why_us.md:90`). With 49 Top-50 places
  from about 2,339 reports last year (2.1%; KB 1.1), "a good ladder" does not make a team memorable.
- **Evidence.** TNA-FINAL.txt:36-39; IPS-FINAL.txt:22-23; Guide:156; case:94-96; `why_us.md:3,90`; KB 3.3.
- **Fix (must achieve).** The team votes on at most three signature ideas (K1-K3 suggested). Each is defined once in
  plain words and used in the same words in the TNA, the IPS and the Final Report. "Maintains consistency with the
  team's IPS" is scored (`deliverables.txt:55`).
- **Deadline.** Vote with vote set A, Sun 18 Oct (Sydney), before TNA reflections are written.

### UNIQ-02 (high, new). The distinctive material is in files judges never see
- **Problem.** Judges see 3 notes plus at most 300 words of reflections, 550 words of IPS, and the Final Report.
  The ideas that set Caplet apart (section 2 table) sit in `research/insight_v1/` (831-page record, 27-page brief),
  `notes_and_discussions.md` and `why_us.md`. IPS V5 shows two of the eight keepers clearly.
- **Evidence.** IPS-FINAL.txt:31-41; TNA-FINAL.txt:46; CLAUDE.md insight_v1 section ("831-page record");
  `team/google_drive/ips_report/01_version_5.md:16-30`.
- **Fix.** A one-page "visibility map" (team-only): each signature idea, the deliverable and paragraph it lives in,
  and the student who owns it. Anything not on the map stays out.
- **Deadline.** Map by Wed 28 Oct (before the IPS outline).

### UNIQ-03 (high, known-deeper). "Each deposit has one job" is the single elegant idea, and V5 does not state it
- **Problem.** The case gives two deposits and two goals (case:43-45, 88-92, 101-107). Caplet's design matches one
  to each. That is client-driven and easy to remember. V5 describes the sequence (V5:24) but its pitch leads with
  "co-sponsors who fund the building rarely pay to run it" (V5:16), which no source supports (UNIQ-09). The idea
  must be framed as a rule: on 15 Oct the holdings basis leaves $1,372 of room (1.3).
- **Evidence.** `why_us.md:3-4`; `01_version_5.md:16,24`; my reconcile run (1.3).
- **Fix.** The pitch and the first IPS rule carry the idea in the students' words: one job per deposit, with the
  overflow step stated. No dollar figure in the pitch. The IBTM and IBTR reflections use the same labels.
- **Deadline.** TNA reflections Tue 20 Oct; IPS outline Wed 28 Oct.

### UNIQ-04 (high, new). The "why now" fact survives only on the holdings basis; the team's figures are stale
- **Problem.** The team's note says the 28 Sep cost was "the cheapest since May 2002" and that $300k bought all ten on
  "only 11% of days since 2000" (`notes_and_discussions.md:309-316`). Those figures use the old Nov-15/STRIPS-style
  basis. I re-priced every treasury.gov par curve from 3 Jan 2000 to 15 Oct 2026 (6,698 days), using Caplet's
  holdings' times to maturity from 1 Jan 2027 and the unchanged-curve basis:
  - $300k covered all ten payments on **562 days (8.4%)**;
  - **no day between 13 Jul 2007 and 22 Sep 2026**; 14 days in 2026 (23 Sep to 15 Oct);
  - median cost in 2021, the year the similar scholarship case ran: **$427,021**; peak 4 Aug 2020: **$472,013**
    (105% of both deposits together);
  - the case-PDF timing story is false on this basis (first sub-$300k day in 2026 = 23 Sep).
- **Evidence.** `oct16/lenses/L04/hist_ladder.py`, `hist_ladder_output.txt` (MODEL; data
  `rab/data/treasury_par_2000_2026/`, September and October 2026 curve files); `notes_and_discussions.md:173,309-316`.
- **Fix.** If used, the fact goes in the Final Report with a chart, date and basis, plus the plan's rule for when
  prices change. The IPS gets at most a figure-free clause. A student re-runs it in a spreadsheet so it is the team's
  own work, and credits the AI in Works Cited.
- **Deadline.** Re-run and log by Sun 15 Nov (Final Report drafting).

### UNIQ-05 (high, new). Co-sponsor communication is the clearest open chance; Caplet holds verified evidence most teams lack
- **Problem.** Creativity now scores communicating "investment uncertainty clearly and credibly to prospective
  co-sponsors" (`deliverables.txt:59`), a clause new this year (KB 2.3). The modal answer is a percentile band.
  Caplet's research found evidence that can shape the message. I re-checked five sources today:
  - **Numbers next to words.** Lay readers in 25 samples, 24 countries and 17 languages read verbal probabilities
    "closer to 50% than intended"; adding numbers fixed much of this (Budescu et al., *Nature Climate Change*, 2014;
    https://www.nature.com/articles/nclimate2194, accessed 16 Oct 2026).
  - **Keeping beats exceeding.** "participants valued keeping a promise more highly than breaking one. However,
    students said exceeded promises made them no happier" (Gneezy and Epley 2014, via Chicago Booth Review,
    https://www.chicagobooth.edu/review/dont-bother-doing-more-than-you-promised, accessed 16 Oct 2026).
  - **Seed money.** "A change in seed money from 10% to 67% of the campaign goal resulted in nearly a sixfold increase
    in contributions" (List and Lucking-Reiley; https://ideas.repec.org/p/van/wpaper/0008.html, accessed 16 Oct
    2026). This supports the case's own claim that a meaningful contribution "may signal" viability (case:110-112).
  - **Announce the lead gift.** Charities "maximize donations given by simply announcing the presence of a lead gift"
    (Huck and Rasul 2011; https://ideas.repec.org/a/eee/pubeco/v95y2011i5-6p351-362.html, accessed 16 Oct 2026).
  - **What counts.** One large U.S. capital funder counts "Written pledges or cash" and wants other sources
    "committed, imminent or backstopped" (Kresge, *A Guide to the Challenge Grant*,
    https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf, accessed 16 Oct 2026).
- **Limits (must be stated).** These are mostly U.S. studies of individual donors or one U.S. foundation. They are
  not about Taiwanese institutional co-sponsors. Use them as reasons for the design, not as forecasts of what
  co-sponsors will give.
- **Fix (must achieve).** The fundraising excerpt (written by students) gives: a dated, bought bottom; a top set by a
  stated rule; the chance of reaching the top in words and a number; what bad markets do; and a re-quote rule for
  the two-year campaign. It must not promise to exceed the top. Sources go in the Final Report. The IPS carries the
  principle only (IPS:68-70, 123-125).
- **Deadline.** Principle into the IPS outline Wed 28 Oct; excerpt drafted by Sun 22 Nov.

### UNIQ-06 (medium, known-deeper). "About 99%" is circular and looks like everyone else's Monte Carlo; the informative number is the chance of reaching the top
- **Problem.** The number sheet's "about 99% (99.4% of 200,000 paths)" holds because the cap stops the gift from
  going above the top (`caplet-latest/.../IPS_number_sheet.md:17`). [AI] suggestion 12 would put "about 99 times in
  100" into the IPS (`IPS_v5_suggestions.md:20`). The same sheet says the gift is at or near the top "in about 3 cases
  in 4" (`IPS_number_sheet.md:18`, MODEL). That is the uncertainty co-sponsors care about.
- **Evidence.** As above; L03 STRAT-07; Budescu 2014 (UNIQ-05).
- **Fix.** Say why the range holds (the rule) and quantify the real uncertainty: where inside the range the gift
  lands. Re-run on the holdings basis before quoting any figure.
- **Deadline.** Before the IPS draft, Sat 31 Oct.

### UNIQ-07 (high, new). The rubric scores "appropriate diversification", and [AI] suggestion 8 deletes V5's only defence of one-issuer concentration
- **Problem.** Caplet is about 90% U.S. Treasuries plus one world fund. A sector-minded reader may mark that down.
  V5:24 has the only defence ("Relying on one issuer ... we accept it, since no dollar asset is safer"). [AI]
  suggestion 8 cuts it "for words" (`IPS_v5_suggestions.md:16`). Its replacement (suggestion 10) is about coupons,
  not diversification.
- **Evidence.** `deliverables.txt:55` ("uses appropriate diversification"); `01_version_5.md:24`;
  `caplet-latest/research/ips_numbers_2026-10/IPS_v5_suggestions.md:16,18`; KB 7.2 #3 ("U.S. government
  concentration" as a likely bond-judge probe).
- **Fix (must achieve).** One plain, student-written reason why matching beats spreading for the payments
  (dollar obligations, dated holdings, one maturity a year) and how the growth money is spread (about 10,000
  stocks; `05_...md:14`, verified 14 Oct per the 15 Oct brief). Keep it in the IPS.
- **Deadline.** IPS draft Sat 31 Oct.

### UNIQ-08 (medium, known-deeper). "Certainty by price, not by model" is distinctive only if it is literally true
- **Problem.** Defining certainty by a checkable price is Caplet's most distinctive answer to case:97-99. But the
  holdings pay coupons that must be reinvested: about $21,000 short if yields fall two points for good
  (`IPS_number_sheet.md:30-36`, MODEL). V5's "depends mainly on the US government" (V5:20) overstates.
- **Evidence.** `why_us.md:78` (R2); `IPS_number_sheet.md:38-48`; L03 STRAT-02, STRAT-04.
- **Fix.** Before 6 Nov, either adopt a design that is safe at 0% reinvestment (L03, about $5-10k of the 2028
  deposit, MODEL) or state the leftover risk and who absorbs it. Then the definition is distinctive and true.
- **Deadline.** Vote set B, Tue 27 Oct.

### UNIQ-09 (medium, known-deeper). "Operations pre-funded" is a real funder-facing edge, but V5's pitch over-claims it
- **Problem.** V5's pitch says co-sponsors "rarely pay to run it" (V5:16). The case says the opposite is possible:
  operating support beyond Laura's commitment "may come from co-sponsors" (case:85-86). The verified kernel is
  weaker but still useful: Kresge asks building applicants "Do you have a plan for sustaining support gained during
  the campaign after it concludes?" (Kresge guide, accessed 16 Oct 2026).
- **Evidence.** `01_version_5.md:16`; case:85-86; Kresge guide.
- **Fix.** Students reframe the claim to what the evidence shows (funders ask who keeps the doors open; Laura can
  answer for ten years). Put it with its source in the Final Report. The pitch must not rest on "rarely".
- **Deadline.** IPS draft Sat 31 Oct.

### UNIQ-10 (medium, new). Answer "too timid" with a measured price of certainty, not more stocks
- **Problem.** All three simulated Lauras called the plan "too timid" (`notes_and_discussions.md:99`). The team has a
  smaller-floor table showing each $25k less floor adds about $2-3k at the middle and costs about $9-10k in a bad case
  (`notes_and_discussions.md:286-301`). It was run on the STRIPS-era model (`research/insight_v1/scripts/F1_floor_variants.py`),
  so it cannot be quoted. Modal teams will just assert a balance.
- **Evidence.** As above; case:69-74 ("appropriate balance"); KB 4.1 (judges reward stated trade-offs).
- **Fix.** Re-run the floor-variant comparison and an all-Treasury baseline on WInS-listed holdings and the
  current curve. In the Final Report, show it as a choice the team made, in a small table or chart.
- **Deadline.** Re-run by Sun 15 Nov.

### UNIQ-11 (medium, new). Write the IPS as a short rulebook in time order: Wharton's own definition of a strategy
- **Problem.** Wharton's feedback: "Your strategy is a set of rules and guidelines; a plan of attack" (KB 4.1,
  [D4]). Its older guidebook warned that a strategy "buried somewhere ... rather than clearly stated ... up front"
  will not be among the strongest (KB 4.1, [W6]). The modal IPS is an essay of considerations. Headings and
  structure are allowed: "You do not need to address these points separately" (IPS:66), and "Formatting choices not
  specified below are left to the team's discretion" (IPS:101-102).
- **Evidence.** As above; 15 Oct brief §7, objective 6 (time order).
- **Fix (must achieve).** About six numbered rules, each a decision with its trigger, in date order (2027, 2028,
  review, 2031, 2033, 2033-42). Count heading words too (target at most 470 IPS words on the higher of two counters;
  15 Oct brief item 21).
- **Deadline.** Outline Wed 28 Oct.

### UNIQ-12 (medium, known-deeper). Make "11 trades and hold" read as discipline: log the decisions not to trade
- **Problem.** The Guide rewards "disciplined decisions" (Guide:181-182). Caplet has pre-set triggers (the IBTR note's
  test; the October rule), but the last logged check in the brief is the 14 Oct close (15 Oct brief item 8). The IBTR
  note's "about 0.2 percentage points" was 22.7bp of room on 6 Oct and 4.7bp on 15 Oct (1.3), which makes it a
  genuine "tested" story.
- **Evidence.** Guide:181-182; `05_...md:15`; 15 Oct brief §10; L05 TNA-01, TNA-04.
- **Fix.** A dated log of each trigger check with the rule's answer ("hold") through 6 Nov. The IBTR reflection
  dates its figure. The Final Report shows the log as evidence of discipline.
- **Deadline.** Log from Sat 17 Oct; IBTR figure fixed to one dated close before Tue 20 Oct.

### UNIQ-13 (medium, new). Real, dated learning stories are a differentiator; the 7 Oct mis-click is double-edged
- **Problem.** Articulation scores "response to challenges" (`deliverables.txt:58`). Caplet has true, specific stories:
  the sector-minimum rule traced to a mislabelled third-party site and checked against the primary page (5 Oct);
  stale WInS bond prices caught and a 25bp yield-check rule adopted (29-30 Sep); "IBTN" found to be an unrelated
  company; STRIPS dropped after the 6 Oct email (`final_report.md:33-40`). Modal teams write generic teamwork lines.
  The 7 Oct mis-click is different: an honest account shows learning, but it also tells judges that an AI browser
  operated WInS (`COMPETITION.md:192-193`). Wharton says "Students should place trades on WInS, NOT the advisor" (written about advisors, but it names students as the traders)
  (`smapply_public_2026-10-14/faqs.txt:34`). AI use must be recorded in Works Cited anyway (KB 4.2, [W5]).
- **Evidence.** As above; L09 INT-08.
- **Fix.** Record who, when, what changed and AI's role for each story. The team decides together, knowingly,
  whether the mis-click goes in the Articulation section with its process fix. Never hide it and never feature it.
  Never invent or polish a story (Ethics rule; 15 Oct brief §2).
- **Deadline.** Journal back-fill Sun 25 Oct.

### UNIQ-14 (low, new). "Root-and-Branch" is an English idiom for a complete overhaul
- **Problem.** Merriam-Webster defines "root-and-branch" as "complete or thorough", with the example "a root and
  branch overhaul of local schools" (https://www.merriam-webster.com/dictionary/root-and-branch, accessed 16 Oct
  2026). A native-English judge may read "radical change" into a plan that holds. The tree image also echoes Laura's
  book title *Messy Roots* (case:22; L02 CLIENT-19), which is a plus. Last year's team used a heavy metaphor set
  (`2025_knox_wharton.md:188,846`).
- **Fix.** Ask two native-English adults outside the team what the name suggests. If kept, the image is explained
  once and nothing else is themed.
- **Deadline.** With vote set A, Sun 18 Oct.

### UNIQ-15 (medium, known-deeper). iBond ETFs as "dated cash" are a true trade-level edge; prepare IBTM as the ETF case study
- **Problem.** WInS lists no Treasury maturing Feb 2031 to Feb 2036, so Caplet used defined-maturity funds
  (`final_report.md:34`). That is cash-flow matching under the WInS-only rule, while many teams will use
  duration-matched IEF/TLT (INFERENCE). Past semifinals required "a case study of one stock or ETF" and banned new
  material (KB 2.4, [D1]). A fixed-income or credit judge sat on the 2024-2026 finale panels (KB 2.2).
- **Evidence.** As above; the iShares disclaimer "the Funds do not seek to return any predetermined amount"
  (iShares page cached 14 Oct, `oct14/wins7/ibtp.html`).
- **Fix.** The Final Report explains IBTM's two jobs, what it holds, why its payout is not fixed, and what happens in
  its final months, in plain words. That makes it available for a semifinal case study.
- **Deadline.** Final Report, Sat 5 Dec 09:00 Sydney.

### UNIQ-16 (medium, new). Label every number with its basis and date; this is cheap and directly marked
- **Problem.** Portfolio Analysis scores "reasonable assumptions and projections" (`deliverables.txt:57`). Caplet
  already has two "ladder costs" for the same day ($294.5k and $298.6k; 1.3). A simple, visible convention (market
  price with date / model estimate / assumption) is rare in student work (INFERENCE) and prevents that error.
- **Evidence.** 1.3; `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md:12-13`; L08 COH-08.
- **Fix.** One student-owned numbers sheet; each figure in the TNA and Final Report carries its date and type. The
  IPS keeps very few figures (IPS:51-52).
- **Deadline.** Before TNA reflections, Tue 20 Oct.

### UNIQ-17 (high, known-deeper). AI wording is the modal 2026 voice; the [AI] suggestion rule gives away Caplet's most distinctive asset
- **Problem.** Creativity scores "an authentic team voice" (`deliverables.txt:59`). Wharton flagged "generated or
  generic responses" in 2025-26 (KB 4.2, [D1]). The 16 Oct rule lets the AI edit all three deliverables as [AI]
  suggestions (`caplet-latest/CLAUDE.md:26-30`), and 13 sentence rewrites already exist (`IPS_v5_suggestions.md:9-21`).
  V5 itself is described by a team comment as "Best version that AI generated" (`01_version_5.md:36`). A team whose
  analysis is largely AI-built can still stand out through its own words and its real story. Accepting AI wording
  removes that.
- **Evidence.** As above; L09 INT-01; L10 TP-08.
- **Fix.** AI items limited to facts, numbers and flags. Students write every submitted sentence. Accepted AI ideas
  are credited in Works Cited.
- **Deadline.** Team decision Sun 18 Oct.

### UNIQ-18 (medium, new). Several tempting "clever" ideas would cost marks or credibility
- **Problem and evidence.** See section 6. The most dangerous are the themed picks (EWT, GLD), the case-timing story
  (false on the holdings basis), marketing the AI council, Laura-biography details, and "99%"-style precision.
- **Fix.** The team agrees a "do not use" list with vote set A, and the TNA editor checks drafts against it.
- **Deadline.** Sun 18 Oct.

### UNIQ-19 (low, new). The Australian angle earns a place only in Articulation, as authentic detail
- **Problem.** No Australian school has made a Top 50 since Brisbane State High in 2021-22 (KB 5.2). That is
  motivation, not content. The one true, client-neutral detail is trading a U.S. market overnight: orders were placed
  while the U.S. market was closed and filled at the next open (15 Oct brief §5), and the journal records a member
  asleep at 12:30 AM (`final_report.md:43`). Australian framing of the strategy (for example superannuation
  analogies, `notes_and_discussions.md:205`) does not serve Laura.
- **Fix.** At most one line in Articulation, about what the team learned (order timing, next-open fills). No
  "first Australian" claims.
- **Deadline.** Final Report.

### UNIQ-20 (medium, known-deeper). Ladder-cost basis for every differentiator that uses it
- **Problem.** K1 and K4 depend on whether $300k covers the payments. The 16 Oct number sheet's $294k and $5.5k room
  (`IPS_number_sheet.md:12-13`) price an ideal ladder dated to each payment (`ips_numbers.py:85-87`). Caplet's
  holdings cost about $298.6k on 15 Oct, with $1,372 (4.7bp) of room (my re-run, 1.3). The sheet's "1 case in 3" is
  scaled to the lower figure (`ips_numbers.py:122`).
- **Fix.** Use the holdings basis for every Caplet claim, dated, in all three deliverables. Use the ideal-ladder figure
  only as a labelled comparison. [AI] suggestion 5 ("about $294,000") must not go into the IPS on that basis.
- **Deadline.** Before the IBTR reflection, Tue 20 Oct.

---

## 8. Checklist: is a differentiator "special but not stupid"?

Before the team adopts any distinctive idea, all six answers must be yes:
- [ ] Allowed by this year's official rules and formats (IPS: no charts, citations or links).
- [ ] It makes Laura's outcome or understanding better, not just the team look clever.
- [ ] A non-finance adult can repeat it after hearing it once.
- [ ] Every number in it has a date and a basis, and it survives the question "is that literally true?"
- [ ] The team can build it in under a day, and a student can rebuild any number in it.
- [ ] Nothing in it contradicts the IBTR, IBTM or VT notes, which cannot be edited.

## 9. What this teaches (for Ray's learning goal; not for any deliverable)

- Being different is only worth something if the difference is visible where the judge looks, and true when the
  judge pushes.
- The same "cost" can be two honest numbers if the dates or method differ. Always say which question a number
  answers.
- Evidence about how people hear promises (keep it, don't oversell it, use numbers with words) is as much a part of
  investing for a client as the bonds are.

## 10. Sources (all accessed 16 Oct 2026 unless a repo file)

- Official: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, `2026_WGY_Investment_Policy-FINAL.txt`,
  `2026_WGY_Trading_Notes_Analysis-FINAL.txt`, `2026_WGY_Investment_Competition_Guide.txt`,
  `smapply_public_2026-10-14/deliverables.txt`, `faqs.txt`.
- Team files: `team/google_drive/ips_report/01_version_5.md`, `05_trading_note_reflection_wins_trading_notes.md`,
  `final_report.md`, `strategy_notes.md`, `notes_and_discussions.md`, `2025_knox_wharton.md`;
  `research/insight_v1/why_us.md`; `docs/benchmark_against_previous_teams.md`; `COMPETITION.md`.
- 16 Oct commit: `caplet-latest/CLAUDE.md:26-30`; `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md`,
  `IPS_v5_suggestions.md`, `ips_numbers.py`; `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`.
- Evidence pack: `oct16/research/KB_what_wins.md` (tags [D1], [D4], [W5], [W6], [N12], [N22] etc. as cited there).
- Web: Budescu et al. 2014 https://www.nature.com/articles/nclimate2194 ; List and Lucking-Reiley
  https://ideas.repec.org/p/van/wpaper/0008.html ; Huck and Rasul 2011
  https://ideas.repec.org/a/eee/pubeco/v95y2011i5-6p351-362.html ; Gneezy and Epley 2014 via
  https://www.chicagobooth.edu/review/dont-bother-doing-more-than-you-promised ; Kresge
  https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf ; Merriam-Webster
  https://www.merriam-webster.com/dictionary/root-and-branch .
- My computations: `oct16/lenses/L04/hist_ladder.py` and `hist_ladder_output.txt`;
  `oct16/research/KB_verify/num/reconcile.py` (re-run, 15 Oct close).

UNVERIFIED in this file: what the 2021-22 finalists did; the 2026-27 Final Report format (images, page range); how
common AI-written submissions are; the lenses' 44-45% chance that the holdings ladder costs more than $300k by
January; the modal-team prediction (INFERENCE from the evidence in 1.1).
