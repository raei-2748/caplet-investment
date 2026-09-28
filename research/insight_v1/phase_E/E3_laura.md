# E3 Red team: "Laura Gao" reads E1's proposals as a client choosing between firms (a simulation)

Agent E3 (red team, client seat), insight_v1 run, Phase E. Written 2026-09-28. This is AI-generated research for Team
Caplet: simulated reactions, evidence, numbers, specifications and checklists. **None of it is text to submit.** The
six students decide every change and write every WInS note, reflection, pitch sentence and IPS sentence in their own
words. AI use goes in the Final Report's Works Cited (Wharton AI policy, R-W46). Laura appears only through the case and
her public professional record. Nothing here suggests contacting her (R-W16: contact means disqualification).

**Relayed messages:** none arrived during this task.
**Scope (brief section 17):** Trading Notes (TN, Oct 23) and IPS (Nov 6) only. Every item says which of the two it
serves. Where the IPS must fix a decision rule that the Final Report will later apply, it is listed under "IPS: rules to
fix before Nov 6". Pure Final Report items are one line each in section 10.
**Evidence read in full:** the brief; CLAUDE.md; the case, IPS guide, TN guide, Competition Guide and SMApply criteria;
`phase_E/E1_change_proposals.md`; `phase_D/` D1-D12, D3_model_v2_results, D13a, D13b flags, D13c, all four audit files
and every "Audit corrections" appendix (corrections override the text above them); `phase_D/trading_now_brief.md`;
`wins_now/securities_and_allocation_v1.md` (and v0, S1-S4 summaries); `phase_A/` case_register (R-C, R-AN),
fact_register, stakeholder_map, wins_week1_guardrails; `phase_C/survivors.json` and parked M007, M008, M015, M021, M033,
M035, M040, M149; the council chair memo and round-2 ruling (history only). `T2_red_team.md` does not exist in the repo on
2026-09-28.

**New script:** `.venv/bin/python research/insight_v1/scripts/E3_client_view_numbers.py` (about 10 seconds, no network;
docstring lists inputs and labels). It re-uses E1's and D6's engine and random stream and prints three client-facing
numbers E1 does not: [1] what the payments cost as a share of her first deposit; [2] the whole-portfolio stock share
year by year 2027-2032 and its six-year average; [3] how much of the likely 2033 gift is already bought when she speaks
in 2031. E1's own script was re-run first and reproduces every figure E1 quotes.

## How to read this file (important)

- **SC = the simulated client.** SC is a reader built only from (a) the official case (VERIFIED-REPO-FILE) and (b) lines
  that D13a marked VERIFIED-PRIMARY, used inside their stated context. SC is **not Laura**. Every reaction below is
  labelled **SIM**: a simulation, i.e. an INTERPRETATION of how a reader holding those stated wishes and public habits
  would likely react. SIM is never a fact about Laura and never her words.
- **Nothing in this file may be quoted, paraphrased or attributed to Laura in any deliverable.** Do not write "Laura
  would feel/say/prefer" in a note, reflection or the IPS. Only D13a VERIFIED-PRIMARY lines are her words, and brief
  section 16 keeps all of them out of the TN and the IPS.
- Reactions are written in the third person on purpose: first-person lines in quotation marks would look like quotes.
- Every phrase that describes content (for example "what the rule makes possible") is **content, not wording**.

**Status labels** (brief section 3): **VP** = VERIFIED-PRIMARY (re-checked on the primary page 2026-09-28 where marked);
**VRF** = VERIFIED-REPO-FILE; **SNIP** = SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION; **MODEL** = an ASSUMPTION-based model
output, not a forecast; **INT** = interpretation (a judgement); **SIM** = simulated client reaction (a kind of INT,
always tied to an anchor). Ids: R- case register, F- fact register, SH-/BS- stakeholder map, M- Phase C, P- E1 proposals.

**Terms used (defined once):**
- **Ladder:** Treasury zero-coupon bonds, one maturing shortly before each $50,000 payment (2033-2042).
- **Growth money:** everything the ladder does not need (about $158k after the 2028 deposit).
- **Bought bottom (2031):** the part of the growth money bought in January 2031 as a Treasury maturing before 2033, so
  its 2033 dollar value is known when she speaks to co-sponsors.
- **Forced caution / chosen caution:** caution the case's own numbers impose (the payments cost almost all of the first
  deposit) versus caution the team chose (the stock share of the growth money, the 2031 lock share, where kept money sits).
- **p5 / p50 / p90:** in a simulation, the value 5% / 50% / 90% of paths fall below.
- **Swap test (D13c):** replace "Laura" with any client's name; if the sentence still works, it is generic.

---

## 0. Summary: the simulated client's verdict and the changes it asks for

**SC verdict (SIM, anchored below).** On substance, SC would very likely choose this firm. E1's design does the three
things SC cares about most while still pursuing some growth (which an all-Treasury rival would not): (1) the residency's
ten operating payments stop depending on markets and on her next contract once they are bought (case L43-45, L91-92,
VRF); (2) she walks into 2031 meetings with a number she never has to walk back (case L114-116, VRF); and (3) it names the
two things it cannot fix (the January 2027 price; what US$ buy in Taiwan).
SC's hesitation is not the architecture. It is that E1 is written from the trading desk outward: parameters, codes and
behavioural traps come first, and what her money does for her residency comes second. A rival with the same architecture
(BS-10) and plainer, warmer, more honest words would win her.

Ranked by impact on reaching the semifinals and on making the plan hers:

| # | Finding (one line) | Deliverable | Confidence |
|---|---|---|---|
| 1 | Never call the 2031 stretch "promised". E1's summary table and P7 label the middle slice "promised-at-risk" / "promised but still at risk"; the case says she will describe what she "expects" (L110) and her "potential contribution" (L116), and D9's vocabulary bans "promised" for the upside. Rename the three parts by what each dollar does: bought / expected if markets allow / kept for the project | IPS (rule 3 wording); TN vocabulary | high |
| 2 | Separate forced caution from chosen caution in the IPS. The payments cost 97.4-98.1% of her first deposit at today's prices (E3 [1]), so ~0% stocks in 2027 is arithmetic, not a view of her temperament. Then state each chosen setting with its reason. Without this the plan reads as "cautious client"; with it, she can inspect every choice | IPS (risk passage); TN (the "why so little equity" or scaling line) | high |
| 3 | Say what the stocks are for, in her terms. Against an all-Treasury benchmark, stocks at 50% of the growth money add about $1k at the median and end below it in about half of paths (D3 M034, MODEL). They are a chance at a larger gift and more project flexibility in good markets, paid for with a smaller gift (never the payments) in bad ones. E1 gives a model rule for the split but not its purpose | IPS (rule 2 "because"); TN (growth note/reflection under ii) | high |
| 4 | Keep the fee principle and extend it: costs never come from the payments **or from the announced 2031 bottom**. E1 ranks the fee clause "first to cut", yet E1's own 50% split rests on a fee assumption (with no fee, the same rule under both forecasts gives 55%, E1 [2], MODEL). Cutting it leaves the split's reason unstated and her cost question unanswered | IPS | high (logic); medium (word budget) |
| 5 | Purpose before prohibition in the pitch, and no tense slips. E1's pitch spec opens with "no dollar takes stock-market risk until...". SC would first look for what the plan makes possible. Nothing may read as already bought (in 2026 nothing is) | IPS (pitch) | medium-high |
| 6 | Keep behavioural diagnosis of her out of the TN and IPS ("loss tolerance", "inferred willingness", "house-money", "break-even trap", "composure"). The case says she "understands that investing involves uncertainty and periods of market volatility" (L68-69). Frame pre-commitments as the firm's own discipline and as protection of her public word | IPS (P6, P10); TN reflections | high |
| 7 | The 2031 method passes SC's "never overpromise" test once findings 1 and 4 are applied: at the median 2031 state, 89% of the likely 2033 gift is already bought when she speaks (80/10/10; 82% at 70/15/15), and the lower half of the range is reached in no modelled path (E3 [3], MODEL) | IPS (rule 3) | high (method); medium (numbers) |
| 8 | Option (ii) vs (iii) is a truth-at-a-date question for SC. Whichever book, run a zero-risk pre-trade check: two readers outside the team read the planned note drafts and say what Laura's real money holds in January 2027. If either says "stocks", the (ii) scaling is not carried by the notes | TN (before the first order) | medium |
| 9 | Name which year of the residency any January-2027 gap falls on. Longest-first puts it on the first operating year (2033); the IPS "because" must say why that is still the better rule (smallest, cheapest piece; first use of the next deposit; less of the promise unbought if the deposit never comes) | IPS (rule 1) | medium-high |
| 10 | Proportion: one clause per honest gap, and lead with what is secured. SC wants the plan to read like a launch, not a disclaimer (case L38-39, "turning those ideas into reality") | IPS | medium |

**Does the plan honour "thoughtful risks" AND "protecting the capital required for her goals"? (section 6)** SIM: it
honours "protecting" completely and "thoughtful" genuinely, but "risks" thinly: about 10% of her money sits in stocks on
average over 2027-2032 (9.7% at 50/50 with an 80% lock; 11.7% at 60/40; E3 [2], MODEL). Most of that thinness is forced by
the case's numbers. The part that is chosen is small, defensible and must be owned in words.

**Could she speak to co-sponsors without ever overpromising? (section 7)** SIM: yes in US dollars, barring a U.S.
default, provided four conditions hold: the stretch is never called promised; costs never touch the announced bottom; no
range is announced before all ten payments are bought (E1 P4, already); and US$ is the binding currency (E1 P8, already).

---

## 1. What the simulation is allowed to stand on

### 1a. Case lines SC reads as her stated wishes (all VRF, `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`)

| Case line | What it tells SC | Ids |
|---|---|---|
| L5, L9-10: "a potential client"; "the investment strategy that Laura ultimately chooses" | She is comparing firms; the plan must earn her choice | R-C4, R-C8, R-AN5 |
| L7-8: "seeking thoughtful financial planning"; L37-39: planning will play a role in "turning those ideas into reality" | She hires the firm to make ideas real, not to be told what she cannot do | R-C7, R-C24 |
| L43-45: the $150,000 comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" | Her second deposit rides on her own career | R-C27, R-AN31 |
| L61-65: living costs outside the portfolio; no other flows before 2033 | The growth money can bear losses without touching her life | R-C33, R-C34 |
| L68-74: "understands that investing involves uncertainty and periods of market volatility"; "Although she has been willing to take thoughtful risks ... an appropriate balance between pursuing growth and protecting the capital required for her goals" | She knows markets fall; she wants balance, not a choice of one side | R-C36-R-C38, R-AN16 |
| L83: "reliable support for its early operations" | Operations are the reliability she is buying | R-C41 |
| L85-86 vs L91-92: others may fund the facility and extra operations, never her ten payments | Where outside help may and may not go | R-AN6 |
| L101-103: "Laura must decide how much ... she can responsibly contribute"; "committing all remaining assets could limit her financial flexibility as the project develops" | Her agency in 2033; flexibility is hers | R-C57, R-C58 |
| L110-116: she will "describe how much she expects to contribute"; overpromising "could damage her credibility"; "a credible range for her potential contribution" | Expectation language, not pledge language | R-C63, R-C66, R-C67 |
| L117-120: a dollar range, a confidence, favourable and unfavourable outcomes, protect the payments | What the 2031 method must produce | R-C68-R-C71, R-AN9 |
| L146-148: assumptions on inflation, "portfolio projections and facility costs", flexibility | The currency and building-cost gap must be named | R-C85 |
| L16: "Statistics & Information Decisions Management"; L19-20: first work "Originally intended as a response to misinformation" | A reader who checks numbers and dislikes incomplete stories | R-C12, R-AN32, R-AN33 |

### 1b. Her verified words SC may draw on (D13a VERIFIED-PRIMARY; all nine lines below re-found verbatim on the primary pages with `fetch_text.py --grep`, 2026-09-28). Research evidence only: none of these may appear in the TN or IPS (brief section 16)

| Id | Exact words | Outlet, date, what she was answering | Caveat that travels with it |
|---|---|---|---|
| B8b-Q18 | “It’s not an easy thing to say, “let me give up my incredibly cushy, paying job with health insurance to be self-employed, with unstable income.”” | Overachiever Magazine, 2021-03-15; leaving her tech job | A career move, not investing. Her own word for her income is "unstable". FR only, once |
| B1b-Q11 | “But I always tell myself, you should always take the jump because you’re always going to regret not doing it.” | same answer, 2021-03-15 | A career leap. Never a reason for a stock weight (D6 audit C3). It is the tension the plan must answer |
| D13a-N01 | “It’s actually harder as an entrepreneur because not only are you letting yourself down, but more importantly, you’re also letting other people down — people who were your earliest supporters and were the first to believe in you.” | The Daily Pennsylvanian, 2016-01-28 (**student-era**); challenges of her student laptop-decal business | One source, student years, a small business, not a residency |
| B8a-Q13 | “When I first posted the comic, I expected a way worse reaction” | Overachiever, 2021-03-15; posting The Wuhan I Know | About a public reaction, not money |
| B8b-Q35 | “I can’t think of many art pieces that I didn’t also write some kind of purpose statement for.” | Pulse Spikes, 2021-06-18; how writing and art go together | About her art; applying it to a policy document is INT |
| B8b-Q38 / B8b-Q39 | “…Our No. 1 priority is to get as many diverse voices and stories in the room as possible, no matter the grounds that they start off on” / “We definitely hope to offer more as the festival grows.” | Local News Matters, 2026-02-12; the festival's mini grants ("we" = organisers) | About festival grants; says nothing about residency fees |
| B2b-Q08 | “Mentor for Tech It Out Philly and MoneyThink, two organizations in which I taught web development and financial literacy to high school students in West Philadelphia.” | Poets&Quants, 2018-03-30 (**student-era**); her activities list | Says nothing about her own investing |
| B8b-Q21 | “it’s great having thousands of likes, but at the end of the day, it’s just a number. You never really understand the human connection behind it” | Overachiever, 2021-03-15; one reader's thank-you note | Metrics vs meaning; not a view on finance |

### 1c. Deliberately not used (and why)

- The case pull quote "The only person who needs to believe in something is yourself." is the case's words
  (VRF), not verified as hers (D13a: PARAPHRASE-UNVERIFIED as Laura's words). SC reads it as the case's framing only.
- "risk-adverse" (about choosing a business major), "No more gimmicks." on its own (about fantasy drafts), "explain
  myself" (about language choices), "diminishing returns" (about dance songs): context breaks (D13a).
- "[unfinished]" and "A/B testing": verified, but reading them as habits for financial numbers over-reads single words
  (D3 audit C19; D12 audit C7). Used here at most as INT, never as a lever.
- D13c candidates C1-C8: verbatim, but D13a has not ruled on them. Not used.
- The "floor-first leap": a reporter's sentence, barred by D13 (brief section 16).
- Privacy exclusions (ids only): B3b-Q09, B8b-Q23, B8b-Q24, B8b-Q34, B8a-Q20, B8a-Q22, B8a-Q23, plus the four D13c
  additions. There is **no verified statement by Laura about investing**: SC has no "investment philosophy" and none is
  invented here.

---

## 2. E1, proposal by proposal, from the client's chair

Reaction codes: **U** = feels understood; **A** = feels analysed (treated as a subject); **S** = feels sold to;
**R** = a line she would reject on sight if it reached a deliverable; **N** = neutral (necessary, not felt).

| E1 item | SC reaction (SIM) | Anchor | What would fix it (spec, not wording) | Serves |
|---|---|---|---|---|
| P1 pitch as a rule | **U** on honesty (a rule she controls cannot be falsified by rates); **A/S** on order (it opens with a prohibition, which reads as caution-first to a founder) | case L38-39, L69-74; B8b-Q35 (purpose statement, art context, INT) | Element order: (1) what the plan makes possible for the residency, (2) the rule, (3) what the rest is for. No word may imply anything is bought in 2026; the optional 2031 element must be future/conditional | IPS pitch |
| P2 certainty + two gaps | **U**: a definition she can check at a market price, plus the two holes named | case L97-99; L146-148 | Keep; one clause per gap; graded words ("at today's prices", "we assume") | IPS; TN vocabulary |
| P3 January 2027 rule | **U** for "buy on arrival, no rate bets"; **question**: which operating year carries a gap | case L91-92; AX1b item 23 | The "because" must say why the first operating year is the one left waiting (section 5, Q2) | IPS rule 1 |
| P4 2028 deposit + joint tail | **U**: it treats her income honestly without doubting the case ("will", L43) | case L43-45; B8b-Q18 (FR only) | Keep to one clause, labelled the firm's own stress case | IPS rule 1 |
| P5 growth split 50/50 by a two-forecast rule | **A/S**: a model-selection argument, not a purpose; SC would ask what stocks are for and why her split depends on a fee nobody told her | case L72-74; E1 [2] (no fee → 55%), D3 M034 | Purpose first (finding 3); state the fee assumption (finding 4); own the choice as "a steadier 2031 bottom" if 50/50 is kept | IPS rule 2; TN if (ii) |
| P6 risk by goal | **U** for "where her big bets already are" (her career, the residency); **A** if written as a scored assessment of her ("need low / ability high / willingness inferred") | case L69-71 ("throughout her entrepreneurial career"); R-AN17 | Write each pot's job and what it can bear; say the payments carry no market risk however much appetite anyone has; no three-factor vocabulary | IPS; TN reflections |
| P7 2031 three slices | **U** on method (bought bottom, uncapped, two-sided); **R** on the word "promised" for the at-risk slice; **A** on codes (80/10/10, p90) | case L110, L114-116; D9 M062 vocabulary | Rename the parts by what each dollar does (finding 1); no codes in the IPS | IPS rule 3 |
| P8 flexibility in US$ T-bills; US$ binding; no NT$ hedge | **U**: flexibility kept by rule, and the firm noticed where the money is spent | case L102-103, L146-148 | Keep | IPS rule 4 / certainty clause |
| P9 reserve = ladder | **N/U**: one sentence reconciling "funded 2027, designated 2033" answers the question she would ask | case L94-96 | Keep | IPS |
| P10 governance, bad-year pre-commitments | **U** that she makes the 2031 and 2033 calls; **A** where the reason for pre-commitment is a trap she might fall into | case L68-69, L101 | Frame as firm discipline and protection of her public word (finding 6) | IPS |
| P11 four rules + governance | **N**: the right skeleton | IPS guide L48-50 | Keep; rename rule 3's parts | IPS |
| P12 fee principle, cut first | **S** (hidden cost) if cut; **U** if kept and extended | B2b-Q08 (student-era, INT); BS-01 | Keep; extend to the announced bottom (finding 4) | IPS |
| P13 WInS (ii) vs (iii) | **S** risk under (ii) if any note or line lets a reader think her January 2027 money holds stocks; **timid** risk under (iii) unless the forced-vs-chosen answer is given | case L19-20 (misinformation origin, INT); R-AN14 | Pre-trade two-reader check (finding 8); "two-thirds" must attach to her total money, never to the payments | TN; IPS WInS sentence |
| P14 three notes plan | **U** on "no staged trades" and honest "tested" windows; **A** if reflections become rate-tracking statistics | TN guide L15-16 | One tracking clause at most; each reflection names her need, not her personality | TN |
| P15 decision log | **N/U** | TN guide L7-9 | Keep | TN |
| P16 page fit, paraphrase test | **U** for the paraphrase test; **N** for the page-fit lawyering | IPS guide L82-83 | Keep; add SC's questions (section 5) to the readers' list | IPS |
| P17 what not to put | **U**: it removes most of what SC would reject | brief s16 | Add the items in section 4 | IPS; TN |

---

## 3. What makes her feel understood, and why each passes the swap test

Each item is SIM, tied to a case line; her verified words are supporting context only (Final Report at most).

1. **Once bought, the promise stops depending on her next contract** (E1 P1 element 2; D9 M143). Anchor: case L43-45
   (VRF); her own word "unstable" for self-employed income (B8b-Q18, 2021, VP, FR only). Swap test: passes, because only
   a client whose second deposit is career income gets this benefit. SIM: the single strongest "understood" signal in E1.
   Condition: said conditionally ("once bought"), never as a date (E1 P1).
2. **Nothing is announced to co-sponsors that is not already bought when she speaks** (E1 P7 items 5-6; P4 item 6).
   Anchor: case L114-116 (VRF); D13a-N01 (2016, student-era, VP): she ranks letting down early backers above letting herself down.
   Swap test: passes weakly on the case alone; strongly once BS-03 is added (her income is reputation-driven, so a
   walked-back number costs her twice, INT).
3. **Her risk-taking is located, not denied** (E1 P6 element 5): her concentrated bets are her career, her books and the
   residency, and the 2028 deposit already rides on them, so the portfolio holds only broad market risk. Anchor: case
   L69-71, L43-45 (VRF); D8 M081 (Chhabra 2016, VP). SIM: this is how the plan can honour "thoughtful risks" without
   pretending 17% stocks is bold.
4. **She keeps the two decisions the case gives her** (E1 P10: the range she announces in 2031; the facility amount in
   2033). Anchor: case L101, L110 (VRF). SIM: a founder choosing a firm wants a firm that recommends, not one that decides
   for her.
5. **Operations come first, in the case's own order** (reserve, then facility, then flexibility). Anchor: case L83,
   L94-103 (VRF). Context only: her newest public priority is access for people "in the room" (B8b-Q38, 2026, festival
   grants, VP, INT link). SIM: the payments read as what keeps the residency running for its first decade, which fits
   that priority.
6. **The firm noticed where the money is spent** (E1 P2 gap ii, P8): US$ is binding, Taiwan building costs are expected to
   rise, no NT$ bet. Anchor: case L76-77, L146-148 (VRF). Swap test: passes (Taiwan is the case's location, not her
   identity).
7. **Every number says what kind of number it is** (E1 P2 element 7: price vs history vs assumption). Anchor: case
   L97-99 (VRF, "identify the assumptions"). SIM: a reader trained in statistics (case L16) trusts a graded number more
   than a precise one. INT only: her student-era project labels its own results "[unfinished]" (B9b-Q09); never cite
   that as a reason in a deliverable.
8. **She is not treated as a theme** (E1 P17; D13c R3): no Taiwan tilt, no identity-based holding, no book puns. SIM: the
   absence is felt.

---

## 4. What feels like being analysed or sold to, and what she would reject on sight

### 4a. Analysed (treated as a subject rather than a client) — fixes are specs, IPS and TN

| Trigger in E1 | Why SC reacts (SIM) | Anchor | Fix |
|---|---|---|---|
| Pre-commitments justified by "break-even trap", "house-money trap", "loss tolerance", "composure" (P6.4, P10.4, via D6) | Implies she may panic; the case says she already understands volatility | case L68-69 (VRF) | Keep the rules; give their reason as the firm's discipline and the protection of her public word. None of the trap vocabulary in the TN or IPS |
| E1 P6.4's point that her investment loss tolerance is the team's inference, if phrased as a finding about her | Reads as a diagnosis written about her, not to her | R-AN17 (case states no risk tolerance) | State it as a design property: the one place her appetite for risk cannot reach is the payments; the growth money's share is set by a stated rule |
| Her statistics degree as a hook (P2 "Why"; P17 "one place") | Flattery or a persuasion lever ("because you studied statistics, we...") | case L16 (VRF); D3 audit C19 | Prefer zero explicit uses in TN + IPS; let the checkable definition show the respect. If used once, it must change a decision (every probability names its model), not compliment her |
| Codes: "80/10/10", "p90", "1-in-20", "45-55 band", "±0.25 years" | Trading-desk shorthand for her own money | D13c V12, R4 (INT) | Each parameter appears once, in plain words, next to what it does |
| "Thoughtful risk = risk that is paid" (D2 via P5) as a gloss on the case's phrase | The firm redefining her words | case L70 (VRF) | Present it as the firm's reading of the case, never as what she means |

### 4b. Sold to (a pitch, not advice)

- **The fee clause cut first** (P12). SIM: a firm that does not say what it costs, or which pot pays, is selling.
  Anchor: B2b-Q08 (she taught financial literacy, student-era, VP, INT link); BS-01; D3 v2 (c): a 0.5% fee on the growth
  money costs about $5k of median; 1% on everything about $32k (MODEL, ASM fees).
- **A growth split whose stated reason is a model contest** (P5) rather than what it does for her residency.
- **Option (ii) WInS holdings described as "her portfolio"** (E1 P13 already bans this; keep the ban absolute).

### 4c. Reject on sight (checklist for every note, reflection, pitch and IPS draft)

- [ ] "Promised", "committed" or "pledged" for money that is still at market risk (the 2031 stretch).
- [ ] Any word implying the payments or the 2031 bottom are already bought (in 2026 nothing is); "bought in January
      2027" or "fits inside $300,000" as flat facts (E1 P17).
- [ ] Costs taken from the payments or from an announced bottom.
- [ ] A range reported as "100% within" because of a cap (E1 C3, D3 audit C2).
- [ ] A model percentage for the payments ("95% certain"); "guaranteed", "safe", "risk-free".
- [ ] An NT$ figure presented as a commitment.
- [ ] Identity, heritage or Taiwan as a reason for a holding; book-title or "falling" puns; the pull quote as hers; the
      "floor-first leap"; her career-regret line as the reason for stocks.
- [ ] Behavioural-trap or risk-profile vocabulary applied to her.
- [ ] WInS funds called "the operating reserve", "matched" or "stable".
- [ ] The growth split justified by valuations ("stocks are expensive"): a reason that will change (AX2 on D2, C7).

---

## 5. The questions she would ask (SIM), and where the answer must already live

Each question is a SIM of what a client holding the case's wishes would ask a firm before choosing it. "Gap" means E1
does not yet give the IPS the content to answer it.

| # | Question (content, not wording) | Where it must be answered | E1 status |
|---|---|---|---|
| Q1 | What exactly is bought, when, and what happens if January 2027 prices are worse? | IPS rule 1 | Answered (P3): buy on arrival, longest-dated first, finish from the 2028 deposit before any growth; about 1 in 3 modelled rate paths need part of the deposit (MODEL, AX1b) |
| Q2 | If a gap opens, which year of the residency is exposed, and why that year? | IPS rule 1 "because" | **Gap.** Longest-first leaves the 2033 payment waiting. Reasons it still wins: the waiting piece is the smallest and least rate-sensitive, it is the first thing the next deposit buys (top-up price risk about one third of nearest-first), and if the deposit never came less of the promise would be unbought ($31.4k vs $47.7k at a 100bp fall; MODEL, AX1b item 23, D3 M053). The IPS needs the reason in its own "because" |
| Q3 | If the middle outcome barely changes, what are the stocks for? | IPS rule 2 "because"; TN growth note (ii) | **Gap.** At 50% of the growth money, the median lift over an all-Treasury benchmark is about +$1.4k and about 48% of paths end below it; on the same path the bad case is about $41k lower and the good case about $57k higher (D3 M034, MODEL; the benchmark itself is not riskless from today, D3 audit C5). So the stocks buy a chance at a larger gift and more flexibility in good markets |
| Q4 | What do I pay, and from which money? | IPS cost clause | **Gap/conflict** (P12 cut first). See finding 4 |
| Q5 | What will I say in 2031, and is every word true in a bad market? | IPS rule 3 | Answered in method (P7); needs the vocabulary fix (finding 1) |
| Q6 | In a strong market, where does the extra go, and who decides? | IPS rules 3-4 | Answered (uncapped: half to the gift, half kept, P7); add that money above the top is her decision in 2033 under the rule, so co-sponsors do not count it (D3 audit C15) |
| Q7 | Is "certain" certain in Taiwan? | IPS certainty clause | Answered (P2 gap ii, P8): certain in US$ barring a U.S. default; a fixed $50k is worth about $42k (2033) to $34k (2042) in 2026 dollars at 2.5% inflation (F-114, ASM); a fixed US$ buys about 11-20% less building by 2033 (D4, ASM on VP inputs) |
| Q8 | Would you change my plan if markets crash in 2029? | IPS governance | Answered (P10): only her circumstances change a rule, never a market move. A down year for the growth money is more likely than not before 2033 (62% of paths at 60/40, D6, MODEL), and the case says she knows it (L68-69) |
| Q9 | Why does WInS show what it shows? | IPS WInS sentence; TN notes | Answered if the date sentence is written (P13); see finding 8 |
| Q10 | What remains mine to decide? | IPS governance | Partly (P10). Content: the rules set the most she can responsibly announce; she decides whether and how to announce within it, and the use of kept money after 2033 |
| Q11 | Why you, and not a firm that buys Treasuries with everything, or one that invests for growth and buys the payments in 2033? | IPS trade-offs (T1-T2 in P11) | Answered in principle. The all-Treasury rival is simpler and has a similar median but cannot "pursue growth" (L72-73) or offer co-sponsors any upside; growth-first misses a payment in 3.2% of modelled paths (13.7% if the 2028 deposit is $75k) (F-401, F-403, MODEL). The IPS names both trade-offs without numbers |
| Q12 | What happens after 2042, or if the residency is delayed? | Out of scope (case L92-93; R-AN34) | Later list (section 10) |

Add Q2, Q3, Q4 and Q10 to the P16 paraphrase-test question list: if a reader cannot answer them from the draft IPS, the
IPS is missing content, not only clarity (IPS).

---

## 6. Test 1: does the plan honour "thoughtful risks" AND "protecting the capital required for her goals"?

**Numbers SC would look at** (E3 script unless stated; MODEL on VRF/VP inputs, JPM AC World 7.00%, bonds 5.0%, no fee):

| Stage (Jan 1) | Whole-portfolio stock share, 50/50, lock 0.8 | 60/40, lock 0.8 | Stock share of the growth money only (50/50) |
|---|---|---|---|
| 2027 | 0.0% (leftover waits in T-bills) | 0.0% | n/a |
| 2028-2030 | 17.0-17.2% | 20.4-20.7% | 50% |
| 2031-2032 (after the bottom is bought) | 3.5% | 4.2% | 10% |
| **Six-year average** | **9.7%** | **11.7%** | |

At a 0.7 lock the six-year average is 10.3% (50/50) and 12.4% (60/40). In dollars, about $79k of her ~$158k growth money
would be in world stocks in 2028 at 50/50 (D2, ASM).

**Forced vs chosen (the distinction SC most needs):**

| Caution | Forced or chosen? | Evidence |
|---|---|---|
| ~0% stocks in 2027 | **Forced.** The ten payments cost $292,264-$294,387, i.e. 97.4-98.1% of the $300,000 first deposit, on the 2026-09-25 curve | E3 [1]; F-101; S1 (VRF inputs, ASM method) |
| Payments bought first, all ten | **Forced by the case's standard**, cheap by the numbers: a full lock gives up about $0.6-3.3k of median facility money against partial locks under JPM and nothing under Vanguard, and partial locks fail in 13-26% of paths if the 2028 deposit does not come | D3 M243 (MODEL; D3 audit C16: about $0.9-5.2k on forwards) |
| Growth money at 50% (or 60%) stocks | **Chosen.** The rule picks 40-65% across the 24 tested cells of forecast, bonds and fee; 55% under both houses' central forecasts with no fee; 50% once a fee of up to 0.5% is assumed | E1 [1]-[2] (MODEL, reproduced) |
| 80% (or 70%) of the growth money bought in 2031 | **Chosen**, for her credibility, not for "capital required" | E1 P7; case L114-116 |
| Kept money in US$ T-bills after 2033 | **Chosen**, for flexibility "as the project develops" | E1 P8; case L102-103 |

**SC's reading (SIM):**
- "Protecting the capital required for her goals": fully honoured. The capital her goals *require* is the payments
  (there is "no predetermined facility contribution", L104). They are bought, held to maturity, carry no fee, and the
  joint tail is named. SC would add that the 2031 lock protects something else she cares about, her word, and the IPS
  should say which of the two each protection serves (the D4 audit C6 makes the same distinction).
- "Thoughtful risks": honoured in kind (risk only where she alone bears the cost; set by a stated rule; not trimmed to
  the minimum) but thin in size. One dollar in ten in stocks on average is low for a client described through her
  career risk-taking. The honest defence is that most of it is forced, and that her real leap, the residency, is not in
  the portfolio at all. The IPS must make that visible, or the plan reads as a verdict on her nerve.
- **Where SC would call E1 too timid:**
  1. *In words more than weights.* E1's budget gives up to about 60-80 of ~470 IPS words to the certainty definition
     with its two gaps plus the joint-tail clause (E1 P2, P4, P16 estimates; INT count), and opens the pitch with a
     prohibition. Honest, but the proportion and order make the plan sound defensive. Lead with what is secured and
     made possible; one clause per gap (ASM: about 15% of the IPS is a sensible ceiling).
  2. *Stacked cautious filters on the split.* E1 picks 50% by requiring the rule to pass under the gloomier forecaster
     *and* a fee of up to 0.5% *and* market-consistent bonds. Each filter is reasonable; together they land near the low
     end of the 40-65% range the rule gives across E1's tested cells. If the team keeps 50/50, it should own it as a choice (a steadier 2031 bottom, simpler to
     explain), not present it as what "the rule" forces.
  3. *Cost transparency treated as optional* (P12 cut first).
- **Where SC would call E1 too clever:**
  1. Codes and parameters (80/10/10, a/s/q, p90, 1-in-20, "uncapped", "two-sided") where a sentence about what each
     dollar does would carry the same rule.
  2. The (ii) "mix after both deposits, scaled to $300,000" book: correct, but a model of her plan rather than her money
     on any day; it needs explaining in every note that touches it.
  3. The CFA three-factor risk vocabulary if it reaches the IPS (E1 P17 already bans framework names; keep it out of
     the words too).
  4. Reflections that turn into rate-tracking statistics (bp moves and % changes) instead of her need; one clause is
     enough.
- **Not too timid** (SC would accept on sight): the ladder bought first, the 2031 bottom bought before she speaks, the
  kept money in T-bills. Each protects something other people will rely on, which is where her student-era words put
  the higher stake (D13a-N01, VP, INT link, FR only).

---

## 7. Test 2: could she speak to co-sponsors in 2031 without ever overpromising?

**The 2031 message at the median 2031 state** (E3 [3]; 50/50 split, JPM AC World, bonds 5.0%, no fee, top = 90th
percentile of the unlocked money's two-year growth; MODEL):

| Parts (bought / expected if markets allow / kept) | Bought bottom | Likely 2033 gift | Top | Share of the likely gift already bought when she speaks | Gift lands in the lower half of the range | Kept for the project (median) |
|---|---|---|---|---|---|---|
| 80/10/10 (E1 default) | $167k | $188k | $192k | **89%** | needs a 35% two-year fall in the unlocked money: 0.0% of modelled paths | $21k |
| 70/15/15 (E1 alternate) | $146k | $178k | $183k | **82%** | same threshold: 0.0% of modelled paths | $32k |

Across all paths (E1 [4], reproduced): 80/10/10 gift p5/p50/p95 $151k/$188k/$238k; kept $16k/$21k/$29k. The gift is
at or above the bottom in every modelled path because the bottom is bought (residual risk: a U.S. Treasury default). Above the top:
about 1 in 10 at the median state, by construction. The model is thin-tailed, so check history: D3's replays of five
crash episodes placed after the 2031 purchase (1929-31, 1973-74, 2000-02, 2008, 2022) cut the facility money by only
about 4-6% (D3 M059, 60/40 split, MODEL on VP data). In the worst row (1929-31) that is roughly an 18% fall in the
unlocked money (INT arithmetic from D3's $164k bottom and $195k total), well short of the ~35% fall needed to reach the
lower half.

**SC's reading (SIM):** the method lets her say three things that can all stay true: what is already bought, what she
expects if markets allow, and what she keeps for the project. Almost nine-tenths of what she expects to give is owned
when she speaks, so the range is narrow and honest ("as precise as warranted", Du et al. 2011, VP via D6; its
applicability to arts co-sponsors is INT). **She can speak without overpromising in US$, barring a U.S. default, if and
only if:**
1. **The stretch is never "promised"** (finding 1). The case's verbs are "expects" (L110) and "potential contribution"
   (L116). A promise of at-risk money is exactly the overpromise the case warns against (L114-115).
2. **Costs never touch the announced bottom** (finding 4). A fee deducted from the bought 2031 Treasury would make the
   2033 amount fall short of the announced bottom; D3's audit lists "fees charged to the floor" among the ways the
   bottom could be missed (D3 audit C2; D3 v2 (c), MODEL).
3. **No range before all ten payments are bought** (E1 P4 item 6, keep).
4. **US$ is the binding currency; any NT$ figure is dated and illustrative** (E1 P8, keep). In NT$ terms nothing is
   certain: two-year USD/TWD moves have a standard deviation of about 6.8% since 2006 (F-513, VP inputs, derived).

**Two residual discomforts SC would voice (SIM), neither a reason to change the method:**
- The range is lopsided: the likely figure sits about $4k under the top and about $21k above the bottom. A co-sponsor who
  plans on the midpoint under-plans, which costs credibility nothing (FR presentation: later list).
- At 80/10/10 the kept money is thin (about $21k median, roughly 11% of the likely gift). That is roughly two to three
  years of Taiwan building-cost drift at the post-2021 pace (3.54%/yr, F-508, VP inputs; ASM sanity check, not a
  contingency fund, which the case does not require, L106-107). SC would still lean 80/10/10 because the part others can
  bank on is larger (89% vs 82% bought), and the case lists "continued business income" among the project's other
  possible sources (L86). Team decides (E1 C4).

---

## 8. Changes E3 asks E6 to adopt (ranked; each is a spec, the team writes the words)

| # | Change | Why (anchor) | Serves | Word cost | Conflict with E1? |
|---|---|---|---|---|---|
| E3-1 | Rename rule 3's parts by what each dollar does: *bought* / *expected if markets allow* / *kept for the project*. Remove "promised" from every internal label so it cannot drift into drafts | case L110, L114-116; D9 M062 | IPS rule 3; TN vocabulary | 0 | Yes: E1 P7 uses "promised but still at risk" |
| E3-2 | IPS risk passage distinguishes forced caution (payments cost ~97-98% of the first deposit at today's prices; one graded price fact) from chosen settings (split, 2031 lock share, kept money), each with its reason | case L69-74; E3 [1]; E1 P17 allows one dated price fact | IPS; TN (iii) "why so little equity" or (ii) scaling | ~10-15 (reuses the one allowed number) | Refines P6 |
| E3-3 | Rule 2's "because" states the purpose of stocks (a chance at a larger gift and more flexibility in good markets; a smaller gift, never the payments, in bad ones) before the rule that sets the share | case L72-74, L110-112; D3 M034 | IPS rule 2; TN growth note (ii) | ~10 | Refines P5 |
| E3-4 | Keep the cost principle (do not cut first) and extend it: costs come only from money not yet promised to anyone, never from the payments or the announced 2031 bottom. State the fee assumption the split rests on, or re-state the split's reason without it (no fee, the rule gives ~55%) | E1 [2]; D3 audit C2; BS-01; B2b-Q08 (INT) | IPS | +3-5 on P12's 15-20 | Yes: E1 P12 and AY2 rank it first to cut |
| E3-5 | Pitch order: purpose (what the plan makes possible for the residency) → rule → what the rest is for; nothing reads as already bought | IPS guide L35-36; B8b-Q35 (INT) | IPS pitch | 0 | Refines P1 (order only) |
| E3-6 | No behavioural diagnosis of her in the TN or IPS; pre-commitments framed as the firm's discipline and the protection of her public word | case L68-69; R-AN17 | IPS (P6, P10); TN reflections | 0 | Refines P6/P10 |
| E3-7 | Rule 1's "because" names that any January-2027 gap waits on the first operating year and why that is still the better order | AX1b item 23; D3 M053 | IPS rule 1 | ~8-12 | Refines P3 (E1 kept the counterpoint to "the team's own risk discussion") |
| E3-8 | Governance says what stays hers: whether and how to announce within the rule in 2031; the facility amount and the use of kept money in 2033; money above the top is her decision under the rule | case L101, L110; D3 audit C15 | IPS governance | ~8-10 | Refines P10 |
| E3-9 | Statistics degree: zero explicit uses in TN + IPS preferred; if one, it must change a decision | D3 audit C19; AY2 C6 | IPS; TN | saves ~6-10 | Yes: E1 P17 suggests one use in the certainty definition |
| E3-10 | Pre-trade two-reader check of the note drafts (what does her real money hold in January 2027?); the (ii) "about two-thirds" must attach to her total money after both deposits, never to the payments | case L161-162 (consistency); R-AN14 | TN (before the first order) | 0 | New check; compatible with P13/P14 |
| E3-11 | Proportion: one clause per honest gap; lead with what is secured; ~15% of IPS words as a ceiling for "what could still go wrong" | case L38-39 | IPS | saves words | Refines P2/P4/P16 |

---

## 9. IPS: rules to fix before Nov 6 (client-seat content only; E1 P11 is the skeleton)

- **Rule 1 (promise first):** add the "because" for longest-first (E3-7); keep the joint tail to one labelled clause.
- **Rule 2 (growth mix):** purpose first (E3-3); the split and band fixed once, with the fee assumption it rests on
  stated or removed (E3-4); frozen against market moves (E1 P10).
- **Rule 3 (2031 range):** bought / expected if markets allow / kept (E3-1); set from what she owns in 2031; no range
  before the ladder is complete; uncapped with two-sided confidence and the model named (FR numbers later); costs never
  from the announced bottom (E3-4).
- **Rule 4 (2033 order of use):** reserve, then gift (bottom + the stated share of the rest), then kept money in US$
  short Treasuries; money above the top is her call under the rule (E3-8).
- **Governance:** who decides, including what stays hers (E3-8); rules change only for a change in her circumstances;
  no behavioural diagnosis (E3-6).
- **Certainty clause:** bought at market prices, held to maturity, in US$, barring a U.S. default; gap (i) January
  price, gap (ii) Taiwan buying power, one clause each (E1 P2; E3-11).
- **Cost clause:** kept and extended (E3-4).
- **Risk passage:** forced vs chosen (E3-2); where her big bets already are (E1 P6.5).
- **Pitch:** purpose, rule, what the rest is for (E3-5).

**TN checklist additions (before the first order and at reflection time):**
- [ ] E3-10 two-reader check done and logged (no names, reader type only).
- [ ] No "promised", "committed" or "pledged" for any growth-money holding; no "two-thirds of the payments".
- [ ] Each reflection's "how it serves Laura" names her need (payments, facility, flexibility, timing of her deposits),
      not her personality; passes the swap test; no trap vocabulary; no degree.
- [ ] Under (iii): the "why so little equity" reflection gives the forced-vs-chosen answer (E3-2) in content.
- [ ] Under (iii), SIM: a dated Treasury rung repaying $50,000 near the first payment date (if WInS lists one) is the most
      tangible single holding a non-specialist can point at; under (ii) its face is scaled (~$34k), so it loses that
      tangibility (securities_v1 section 7).

---

## 10. Later (after Nov 9), one line each (Final Report; not worked here)

- The "likely figure" beside the range, not the midpoint (89% bought at the median 2031 state, E3 [3]).
- At most one or two dated Laura lines in context (candidates: D13a-N01 beside the bought bottom; B8b-Q18 beside the
  promise-first rule), each labelled with outlet, year and, for 2016, "student-era".
- The real-terms and Taiwan building-power sentence (F-114; D4 table A).
- One line on a delayed residency and on money after 2042 (BS-07; case L92-93).
- One line naming the operational controls behind "certain" (BS-18).
- The fee assumption and net-of-fee projections (D8 M026; D3 v2 (c)).

---

## 11. Conflicts E3 could not resolve (both sides; the team decides)

| # | Conflict | Side A | Side B | E3 view (SIM/INT) |
|---|---|---|---|---|
| K1 | Label for the 2031 middle slice | E1 summary table and P7 (and AY1's metric s(1-a)): "promised but still at risk" | D9 M062 vocabulary; case L110/L116: never "promised" for the upside | Rename (E3-1); the metric can stay internal |
| K2 | Fee clause | E1 P12 / AY2: cut first (case silent on fees) | E1 P5's 50% rests on a fee assumption; SC's cost question; announced bottom exposed | Keep and extend (E3-4); if cut, re-state P5's reason |
| K3 | WInS book | E1/T1/D12 lean (ii): three roles, a visible growth decision | D10 lean (iii): true at a stated date; SC values literal truth and a tangible $50,000 rung | SC is close to neutral, slightly toward (iii) on credibility; the E3-10 check is the tie-breaker the team can run today |
| K4 | Statistics degree | E1 P17 / D7: once, in the certainty definition | D3 audit C19 / SC: zero is safer | Prefer zero (E3-9) |
| K5 | Pitch order | E1 P1: rule first (true in every path) | SC: purpose first, rule second | Reorder (E3-5); both elements stay |
| K6 | Growth split | E1/T1/D2: 50/50 (passes under both houses with a fee ≤0.5%) | D6/D13c: 60/40 (JPM; do not look set at the minimum); E1 [2]: 55% with no fee under both houses | SC cares less about the number than about the purpose and an honest reason; whichever is chosen, own it as a choice of spread |
| K7 | 2031 parts | 80/10/10: larger bought share (89% of the likely gift) | 70/15/15: more kept flexibility ($32k vs $21k median) | SC leans 80/10/10 (others rely on the bought part); flexibility is thin but not required to be sized (L106-107) |
| K8 | Where the longest-first counterpoint lives | E1 P3: in the team's own risk discussion | SC: in the IPS rule's "because" | IPS (E3-7), one clause |

---

## Sources (accessed 2026-09-28 unless noted)

**Official, in the repo (VRF):** `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (L5-10, L16, L19-20,
L25-26, L38-39, L43-45, L61-74, L76-77, L83-120, L123, L136-148, L169); `2026_WGY_Investment_Policy-FINAL.txt` (L3-5,
L16-28, L35-36, L45-78, L82-83, L101-125); `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L3-31, L36-53);
`2026_WGY_Investment_Competition_Guide.txt` (L70-94, L156-159, L181-186); `SMApply_Deliverables_Page_2026-09-27.md`
(criteria). Market data: `competition/official_market_data/daily-treasury-rates_2026-09.csv` (row 09/25/2026).

**Laura's words (VP; D13a register, each re-found verbatim with `research/insight_v1/scripts/fetch_text.py --grep` on
2026-09-28):**
- Overachiever Magazine, 2021-03-15 (B8b-Q18, B1b-Q11, B8a-Q13, B8b-Q21):
  https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid
- The Daily Pennsylvanian, 2016-01-28 (D13a-N01, student-era): https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a
- Local News Matters, 2026-02-12 (B8b-Q38, B8b-Q39):
  https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/
- Pulse Spikes, 2021-06-18 (B8b-Q35): https://pulsespikes.org/story/laura-gao
- Poets&Quants for Undergrads, 2018-03-30 (B2b-Q08, student-era):
  https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/
- B9b-Q09 ("[unfinished]", lauragao.com/rewriting-herstory) is cited from D13a (VP there) and used as INT only.

**Research files (lower authority; numbers reproduced where stated):** `research/insight_v1/phase_E/E1_change_proposals.md`
(and `scripts/E1_split_and_slices.py`, re-run 2026-09-28, every figure reproduces); `phase_D/D1_rates.md` (+AX1b),
`D2_equity_ai.md` (+AX2), `D3_quant.md` and `D3_model_v2_results.md` (+AX1), `D4_taiwan_fx.md` (+AX2),
`D5_cosponsors.md`, `D6_behavioural.md`, `D12_overflow_client.md` (+AY1), `D7_wharton_intent.md`, `D8_practice.md`,
`D9_communication.md` (+AY2), `D10_compliance.md` (+AX2), `D13a_laura_quotes_verified.md`, `D13c_voice_map.md`, the four
audit files, `trading_now_brief.md`; `wins_now/securities_and_allocation_v1.md`, `S1`-`S4`;
`phase_A/{case_register,fact_register,stakeholder_map,wins_week1_guardrails}.md`; `phase_C/survivors.json`, `parked.json`;
`research/council_2026-09-27/01_chair_memo.md`, `round2_referee_ruling.md` (history).

**Scripts:** `research/insight_v1/scripts/E3_client_view_numbers.py` (new; reuses `E1_split_and_slices.py`,
`D6_behavioural_numbers.py`, `A2_curve_recheck.py`).

---

## What this teaches

1. **A client reads a plan from the outside in.** Analysts build from rules and parameters; a client first asks what her
   money will do for the thing she cares about, then what it costs, then what could go wrong. The same strategy can feel
   like advice or like a rulebook depending only on that order.
2. **Separate what the numbers force from what you chose.** When the payments cost 98% of the first deposit, holding
   almost no stocks in 2027 is arithmetic, not a judgement about the client. Saying so replaces an implied verdict on
   her temperament with a short list of choices she can inspect one by one.
3. **Verbs are part of risk management.** "Bought", "expected" and "kept" are three different promises. Calling at-risk
   money "promised" would recreate the one mistake the case warns about, even though the numbers underneath are sound.
4. **Understanding a client is not analysing her.** Behavioural research is useful for designing rules; applied to the
   client in her own document, it tells her she is being studied. Design the rules with it; explain them with her goals.
5. **Simulating a real person needs a fence.** Every reaction here rests on the case or on her verified words in their
   own context, and none of it may be put in her mouth. That fence is what makes the exercise honest rather than
   invented.
