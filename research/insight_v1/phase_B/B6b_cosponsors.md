# B6b Co-sponsors and philanthropy: the communication side of the 2031 range

Agent: B6b (lens "Co-sponsors & Philanthropy", starting angle: communication). insight_v1 run, written 2026-09-27.
AI-generated research (Claude Code) for Team Caplet, for brainstorming only. It holds **no submission-ready prose**:
no fundraising paragraph, no IPS or Final Report text. Where it says what a passage "must contain", that is a
checklist. The six students write every word, and any use of this file must be recorded in the Works Cited (AI
policy, R-W46). No securities are named here.

Status labels follow brief section 3: VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED (SNIP),
ASSUMPTION (ASM), PARAPHRASE-UNVERIFIED, INTERPRETATION (INT, my reading, never a fact).

---

## 0. Summary (read this first)

1. **The case asks for a forecast statement to non-specialists, and there is a research field on exactly that.**
   Forecast-communication studies (weather, climate, intelligence, company earnings) give tested rules for how to
   state a range and a confidence level. None of the earlier research files use it (grep of `research/`, 2026-09-27:
   no hits for IPCC, Budescu, Teigen, Gigerenzer, van der Bles). Five findings matter most (all VP, abstracts read):
   - People read verbal probability words ("likely", "very likely") as **closer to 50%** than intended. Adding the
     number next to the word fixes most of this, **in 17 languages** (Budescu et al. 2014). That matters for
     Taiwanese readers (Q1, Q21).
   - A bare percentage is ambiguous unless you say **what it is a percentage of** (Gigerenzer et al. 2005) (Q2).
   - Readers treat a range as a **yes/no category**: a result just outside a narrow edge counts as "wrong", even when
     the range was only a 50% band (Teigen, Løhre & Hohle 2018, the "boundary effect") (Q6).
   - Stating uncertainty **as numbers** barely lowers trust in the source. Verbal hedges lower it more (van der Bles
     et al. 2020). After an "unlikely" outcome happens, communicators who used numbers keep more credibility (Jenkins,
     Harris & Lark 2019) (Q14, Q15).
   - Keeping a promise earns as much credit as exceeding it; breaking it is punished (Gneezy & Epley 2014, via a
     university press release). So **the bottom of the range is the only real promise**, and a high top earns nothing
     (Q7, Q23).
2. **NEW NUMBER: by 2031 about 97% of the uncertainty is gone.** Using the verified model's own assumptions
   (`strategy_mc.py`, lock-early, 60% equity sleeve, 80% floor), I re-ran the paths. Only **2.8%** of the 2026-view
   variance of the 2033 surplus is still unresolved on 1 Jan 2031 (ASM-based, derived; script in section 5). From a
   2031 starting point the 90% band is only about **±4-5% of the median** ($199k-$217k at the median 2031 state),
   against **$159k-$273k** in the 2026 view. The $114k-wide range everyone quotes is a 2026 artefact. The range Laura
   actually says in 2031 can be narrow and honest (Q3, Q18).
3. **NEW NUMBER: locking 100% of the sleeve in 2031 would cost only about $1k of median 2033 value** under the same
   assumptions ($206.1k fully locked vs about $207k at 80% locked). If that holds when D3 checks it, the 2031 "range"
   comes mostly from Laura's own flexibility choice and the exchange rate, not from markets (Q4).
4. **NEW: in NT$ terms, currency swamps market risk.** The USD band at the median 2031 state is about -4%/+5%. The
   2-year USD/TWD move since 2006 has p5/p95 of -12.1%/+10.6% (F-513, VP-derived). Any NT$ figure needs its own label
   or band (Q5).
5. **How a capital funder actually counts a founder's money.** The Kresge Foundation's *Guide to the Challenge Grant*
   (2011, VP) counts only "Written pledges or cash" as money raised. Other sources "should be committed, imminent or
   backstopped", and it wants "a significant amount" pledged "before the general public ever hears about the
   campaign". Read against the case, the **floor** is what a funder can count, **the date the floor is bought**
   matters, and the top of the range counts for nothing (Q9, Q10).
6. **Matching gifts.** In a 50,000-letter field experiment, offering a match raised both giving and response rates,
   but "larger match ratios ... had no additional impact" (Karlan & List 2007, VP). This opens a design option: offer a
   small 1:1 match on the part above the floor only. It still has to pass the complexity test (Q12).
7. **WInS-now item.** Trade notes cannot be edited. The team should fix a short certainty vocabulary now (what is
   "locked", what is "expected", what is "possible"), so that no note written this week says "guaranteed" in a way the
   IPS and Final Report must later walk back (Q19).

Question count: 23 (section 2). Leads for specialists: section 4. Sources: section 6.

---

## 1. What earlier work already covers (so I do not re-ask it)

Already covered in Phase A or other Phase B files. I only add **new evidence** to these:
- Currency labelling "US$" (BS-04); which verb goes with the floor and which with the stretch (BS-05); share of an
  unestimated total (BS-06); overrun answer (BS-16); operating money is what funders least like to give (BS-17).
- Cap the gift at the top of the range, so the confidence depends only on the low end (B1a Q17, B1b Q19).
- A rule in 2031 versus a dollar range fixed today (B1a Q18, B1b Q18). My Q3 adds the 97%-resolved number.
- Pre-announced updates between 2031 and 2033 (B1a Q19).
- Nonprofit sense of "operating reserve" (B1b Q16). Conditional versus unconditional pledge under ASU 2018-08 (B4a
  Q14). Yale's two-year lag (B4a Q12). "Committed plus stretch" in her product-manager language (B2a Q12).
- Brief section 8.7 (floor bought, not a model percentile) and 8.17 (seed-money effect is a mechanism only).

My lens is distinct: **how** the range and confidence are worded, labelled, attributed, dated and shown, and what
a funder can actually count.

---

## 2. Questions (23), grouped by deadline tier

Format for each: question; anchors; official words; hypothesis (a GUESS, with evidence and status); what would
change; deliverables; specialist; seed; North Star.

### Tier 1: WInS now and the Trading Notes (Oct 23)

**Q19. Before more WInS notes are saved (they cannot be edited), should the team fix a three-tier certainty
vocabulary: words for bought/locked amounts, for model-based expectations, and for mere possibilities? The aim is
that no trade note uses "guaranteed" or "safe" in a way the IPS and Final Report must later qualify.**
- Anchors: R-T28 ("Include each Trading Note exactly as it appears in WInS."), R-T21, R-C92, A4 checklist item 12
  (strategy glossary), brief section 7 ("residual risk U.S. default").
- Official words: "Teams should use each deliverable for its intended purpose while maintaining a clear and
  consistent investment strategy across all three." (case p.4, VRF)
- Hypothesis (GUESS):
  - Yes. A4's glossary covers strategy words (growth, liquidity, and so on). It does not cover **certainty words**.
    Those are the words co-sponsors, a statistician client and the judges will test.
  - The team's own certainty definition is "certain in nominal USD, barring U.S. Treasury default" (brief section
    7). So "guaranteed" is already too strong for a note. "Locked in at today's prices" or "matched" is defensible.
  - Evidence: numeric and precise wording keeps credibility when surprises come (Jenkins et al. 2019, VP abstract).
    Readers treat range edges as right/wrong lines (Teigen et al. 2018, VP).
  - This costs nothing and prevents an inconsistency that cannot be fixed later.
- Would change: **sentence** (wording of every trade note from now on); **decision** (a one-page certainty glossary
  shared by TN, IPS and FR).
- Deliverables: WInS-now, TN, IPS, FR. Specialist: D9 (with D10). Seed: null.
- North Star: Laura, a statistics graduate, sees the same careful words in October that she sees in December.

### Tier 2: the IPS (Nov 6), which fixes the rules

**Q4. Locking 100% of the sleeve in 2031 would cost only about $1k of median 2033 value under the verified model's
assumptions. Should the 2031 lock share rise from 80% toward 100%, so that the co-sponsor range reflects Laura's
flexibility choice and the exchange rate rather than market risk?**
- Anchors: R-C65, R-C71, F-402, F-013, brief section 9 ("share of sleeve locked as floor").
- Official words: "In 2031, however, the value of her portfolio in 2033 remains uncertain." (case p.3, VRF)
- Hypothesis (GUESS):
  - My re-run (section 5, derived from the VERIFIED script with its ASSUMPTIONS): at the median 2031 state, 80% locked
    gives 2033 p5/p50/p95 of about $199k/$207k/$217k. 100% locked gives **$206.1k with no market spread**. The median
    cost is about $1k.
  - The reason: over two years, the unlocked 20% (about $37k) earns only a little more in expectation than a 4.81%
    two-year Treasury.
  - Caveat (ASM): the model fixes the 2031 two-year yield at today's 4.81%. If 2031 yields are much lower, locking
    gives up more. D3 should test 2031 yields of 3% and 4%.
  - If the result holds, the case's "remains uncertain" is answered by a design choice: the USD amount is almost
    known in 2031. The range then describes how much Laura *chooses* to keep as flexibility (R-C58), plus currency
    for NT$ readers.
- Would change: **number** (floor share 80% vs 90-100%); **decision** (IPS 2031 rule).
- Deliverables: IPS, FR. Specialist: D3 (with D1). Seed: 8.
- North Star: Laura can tell co-sponsors a number that is already bought, which is the strongest possible credibility.

**Q10. Should the 2031 floor be bought before Laura's first co-sponsor conversation (on the first trading days of
2031), so that the first number any funder hears is already "committed, imminent or backstopped"? And what document
would prove it to a funder's due-diligence team?**
- Anchors: R-C62 ("begin approaching potential co-sponsors in 2031"), R-C66, R-AN7, BS-08 (records).
- Official words: "Laura plans to begin approaching potential co-sponsors in 2031, two years before the residency is
  established." (case p.3, VRF)
- Hypothesis (GUESS):
  - Yes. Kresge's guide (VP) advises: "Have a significant amount of your campaign pledges committed before the general
    public ever hears about the campaign". It also says non-gift sources "should be committed, imminent or
    backstopped".
  - A floor bought in, say, March 2031, after conversations have begun, means her first stated number was a forecast.
  - Proof of the floor would be an account statement or holding record. Its content (not its form) belongs in the
    IPS rule as "trigger, action, record" (BS-08).
- Would change: **decision** (date of the 2031 purchase in the IPS rule); **sentence** (FR: "already set aside on
  [date]" as a required element).
- Deliverables: IPS, FR. Specialist: D5 (with D8). Seed: 8.
- North Star: she never has to walk back a number, because nothing is said before it is bought.

### Tier 3: the Final Report (Dec 4), fundraising part and range

**Q1. Which confidence level should the 2031 statement carry, and should it use "dual format": a calibrated word
plus a number (the IPCC's "very likely" with its numeric band), never a word alone?**
- Anchors: R-C69, R-AN32 (statistics degree), R-S28 (criterion 5: "clearly and credibly").
- Official words: "state how confident they are that her 2033 contribution will fall within that range." (case p.3,
  VRF)
- Hypothesis (GUESS):
  - A numeric level of about 90%, always shown with its number. 90% matches the IPCC's "very likely" band.
  - Evidence:
    - Budescu et al. 2014 (VP abstract), 25 samples, 24 countries, 17 languages: "laypeople interpret IPCC statements
      as conveying probabilities closer to 50% than intended". Supplementing the words "with numerical ranges
      increases the correspondence".
    - Budescu et al. 2009 (VP abstract): readers deviated from the guidelines "even when the respondents had access to
      these guidelines".
    - IPCC AR5 guidance note (VP): "When there is sufficient information, it is preferable to specify the full
      probability distribution or a probability range (e.g., 90-95%) without using the terms in Table 1."
  - The exact IPCC table values ("very likely" 90-100%, "likely" 66-100%) were garbled in the PDF text layer. The
    paragraph I read confirms "likely" = "≥66% ... to 100%". The other bands are SNIP until D9 reads the table.
  - A bare "likely" would be read as about a coin flip, which undersells a bought floor.
- Would change: **number** (the stated confidence level); **sentence** (the dual-format rule in the draft
  checklist).
- Deliverables: FR. Specialist: D9. Seed: 9.
- North Star: Laura and a co-sponsor read the same probability from the same words.

**Q2. What exactly does the confidence percentage refer to (paths of a stated model? past two-year periods?), and
must the fundraising part name that reference class?**
- Anchors: R-C55 ("explain how they evaluated that level of certainty"), R-C69, R-AN32.
- Official words: "They should also define what they consider a high degree of funding certainty, explain how they
  evaluated that level of certainty" (case p.3, VRF)
- Hypothesis (GUESS):
  - Yes, in one clause, for example "in N of 10 simulated market paths under [named assumptions]". That is a
    frequency with its source. The team writes the wording.
  - Evidence: Gigerenzer et al. 2005 (VP abstract): "even numerical probabilities can be interpreted by members of
    the public in multiple, mutually contradictory ways ... experts need to specify the reference class".
  - Natural frequencies ("9 in 10") are easier for non-specialists. The percentage and method can sit in the FR
    method box for Laura, the statistician.
- Would change: **sentence** (FR method line and fundraising checklist element).
- Deliverables: FR. Specialist: D9 (D3 supplies the class). Seed: 9.
- North Star: a statistician client sees her own discipline, "what is the denominator?", applied to her promise.

**Q3. How much of the 2033 uncertainty is still unresolved when Laura speaks in 2031? Should the Final Report show the
2031 range as a narrow band for each of three 2031 starting states (about ±5% of the median) instead of the 2026-view
band ($159k-$273k)?** (New evidence on B1a Q18 / B1b Q18.)
- Anchors: R-C62, R-C65, R-C68, R-C70, F-401, F-402.
- Official words: "They should explain how favorable and unfavorable market outcomes could affect the amount she can
  provide." (case p.3, VRF)
- Hypothesis (GUESS, derived numbers labelled):
  - My re-run of the verified model's paths (ASM inputs as in `strategy_mc.py`) finds that only **2.8%** of the 2026-view
    variance remains after 2030.
  - Conditional on the 2031 sleeve, 2033 p5-p95 is:

    | 2031 state | 2033 p5 | 2033 p95 | 90% width | Bought floor |
    |---|---|---|---|---|
    | Weak (p10 sleeve) | $162k | $177k | $15k | $134k |
    | Median | $199k | $217k | $18k | $165k |
    | Strong (p90 sleeve) | $246k | $269k | $23k | $204k |

    The 90% width is about 8.9% of the median in each state.
  - So the "favorable and unfavorable market outcomes" the case asks about are mostly 2027-2030 outcomes, which Laura
    already knows by 2031.
  - A three-row table is simple, and it answers both the "dollar range" and the "rule" readings of the case.
- Would change: **number** (the range width in the FR); **decision** (present a three-state table, not one wide
  band).
- Deliverables: FR. Specialist: D3. Seed: 8.
- North Star: shows that two years was enough time to make her promise precise, which is what the timing of the case
  allows.

**Q5. In NT$ terms, does exchange-rate risk over 2031-2033 swamp the market uncertainty left in the USD range? Should
any NT$ figure therefore get its own wider band, or be labelled as an illustration at a stated date and rate?**
- Anchors: R-AN10, F-510, F-512, F-513, F-514, BS-04, SH-06, SH-07.
- Official words: "Teams must recommend the dollar range Laura should communicate" (case p.3, VRF). No currency is
  named anywhere (R-AN10).
- Hypothesis (GUESS):
  - Yes. The USD band at the median 2031 state is about -3.9%/+4.8% (Q3). USD/TWD 2-year moves since 2006 have p5/p95
    of -12.1%/+10.6% (F-513, VP-derived).
  - Combined as independent (ASM), the NT$ band is roughly ±12%, about 2.5 times the USD band.
  - This does not change the USD promise. It changes what a Taiwanese partner should be told: the binding figure is
    US$. NT$ is a dated illustration, and its swing is larger than the market swing.
- Would change: **sentence** (FR currency element); possibly **number** (an NT$ band).
- Deliverables: FR. Specialist: D4. Seed: null.
- North Star: respects partners who budget in NT$, without tokenism: a practical currency fact, not an identity
  gesture.

**Q6. How should the ends of the range be labelled? Readers treat a result just outside a hard edge as a broken
promise (the "boundary effect"), yet a soft word like "can" or "up to" makes the top sound likely.**
- Anchors: R-C66, R-C67, R-AN9.
- Official words: "Rather than promising one exact amount, she wants to communicate a credible range for her
  potential contribution." (case p.3, VRF)
- Hypothesis (GUESS):
  - Teigen, Løhre & Hohle 2018 (VP abstract): outcomes "falling outside a narrow range were deemed to be incorrectly
    predicted, in proportion to the magnitude of deviation". But "When the upper limit of a range is described as a
    value that 'can' occur ..., outcomes both below and beyond this value were regarded as consistent with the
    forecast."
  - Teigen & Filkuková ("Can > will"): "can" statements pick extreme values that listeners still judge probable. SNIP:
    title and topic from a University of Oslo project listing only; D9 should read the paper.
  - Guess: the bottom is a hard edge (bought). The top is a soft edge described **with its probability of being
    reached**, not with "up to" or "can", which readers take as the likely amount.
- Would change: **sentence** (labels of the two ends in the draft).
- Deliverables: FR. Specialist: D9. Seed: 9.
- North Star: nothing she says can be read later as a broken promise.

**Q7. Exceeding a promise earns no more credit than keeping it, while breaking it is punished. So should the draft
treat the bottom as the only promise, and should it show a "best estimate" at all?**
- Anchors: R-C66, R-C64, R-AN9, BS-03 (credibility is part of her income).
- Official words: "If Laura promises more than she can ultimately contribute, she could damage her credibility and
  lose the confidence or participation of co-sponsors." (case p.3, VRF)
- Hypothesis (GUESS):
  - The ScienceDaily release of Gneezy & Epley 2014 (VP for the release; the paper itself SNIP, SSRN blocked) says:
    "exceeding a promise isn't viewed any more highly than keeping a promise". Also: "Promises can be hard to keep,
    and promise makers should spend their effort keeping them wisely."
  - So a high top adds no credibility. Its only use is to help co-sponsors plan.
  - Dieckmann, Peters & Gregory 2015 (VP abstract): "including a best estimate increases perceptions that the
    distribution is roughly normal". A central number helps understanding, but it may become the number people
    remember.
  - Guess: show the floor and the range with its probability in the co-sponsor part. Keep the median in the FR
    analysis for Laura.
- Would change: **decision** (best estimate shown or not); **sentence**.
- Deliverables: FR. Specialist: D6. Seed: 15.
- North Star: the plan protects her from the most expensive mistake a founder can make in public.

**Q8. Should the confidence statement give the chance of missing the range on each side separately (below the floor,
above the top), following the IPCC's advice to give reciprocal statements?**
- Anchors: R-AN9, R-C69, R-C66, R-C71.
- Official words: "state how confident they are that her 2033 contribution will fall within that range." (case p.3,
  VRF)
- Hypothesis (GUESS):
  - The IPCC AR5 note (VP), paragraph 4: "a 10% chance of dying is interpreted more negatively than a 90% chance of
    surviving ... Consider reciprocal statements".
  - At the median 2031 state, a range from the bought floor ($165k) to the conditional p90 ($215k) gives, in my re-run
    (ASM, derived): P(inside) 0.900, **P(below) 0.000**, P(above) 0.100.
  - A single "90%" hides that every miss is on the harmless side. Two separate numbers make that visible.
  - This complements B1a Q17 (cap at the top) with the communication form.
- Would change: **sentence and number** (two numbers instead of one).
- Deliverables: FR. Specialist: D9 (numbers from D3). Seed: 9.
- North Star: co-sponsors see that the only surprise possible is a good one.

**Q9. Would a capital funder count any part of Laura's range as money already raised, or only a written floor? Should
the fundraising part therefore lead with the floor, not the range or its midpoint?**
- Anchors: R-C64, R-C67, BS-05, B4a Q14.
- Official words: "A meaningful personal contribution may signal that the residency is financially viable,
  demonstrate Laura’s commitment to the project, and make potential co-sponsors more willing to contribute." (case
  p.3, VRF)
- Hypothesis (GUESS):
  - Kresge's counting list (VP) starts with "Written pledges or cash from individuals, corporations, businesses and
    foundations". Its glossary defines a challenge grant as "Money pledged by Kresge that will be paid when grant
    conditions are met."
  - A forecast range is not on the list. The part a funder can count is the floor, if it is stated as a written
    commitment.
  - This is the same logic as ASU 2018-08 (B4a Q14, SNIP) from a funder's practice rather than from accounting.
  - So the "meaningful" signal (R-C64) is carried by the size of the floor. That links this question back to Q4.
- Would change: **sentence** (the headline number of the draft); **decision** (floor size matters more than the
  midpoint).
- Deliverables: FR. Specialist: D5. Seed: 9.
- North Star: her number is one a funder can put in its own spreadsheet.

**Q11. Kresge-style funders expect "project-cost estimates are firm" before a capital grant, yet the case says the
facility cost is undetermined. What must the fundraising part say so her contribution reads as sized from her
portfolio, not as a share of an unknown budget? And what happens to it if costs change?** (New evidence on BS-06 and
BS-16.)
- Anchors: R-C94, R-C95, R-C60, BS-06, BS-16.
- Official words: "The total cost of the facility has not been determined." (case p.4, VRF)
- Hypothesis (GUESS):
  - Kresge's readiness indicator 2 (VP): "Your project-cost estimates are firm and construction timetables have been
    established."
  - In 2031 Laura will be early in that process. The draft should not pretend otherwise.
  - Elements: sized from what her portfolio can responsibly give; independent of the final cost; does not rise if
    costs rise; the project scope adjusts. No cost estimate or budget (scope).
- Would change: **sentence** (two checklist elements).
- Deliverables: FR. Specialist: D5. Seed: 6.
- North Star: she sounds like a founder who knows what a funder will ask, without inventing a budget.

**Q12. Should part of Laura's above-floor amount be offered as a 1:1 match for co-sponsor gifts? Field evidence shows
a match raises giving, but larger ratios add nothing.**
- Anchors: R-C64 ("make potential co-sponsors more willing to contribute"), R-C44 (outside money may fund the
  facility), R-C71.
- Official words: "Any remaining facility cost ... may come from co-sponsors, grants, collaborators, program fees,
  continued business income, or other sources." (case p.3, VRF)
- Hypothesis (GUESS):
  - Karlan & List 2007 (VP, NBER abstract): "the match offer increases both the revenue per solicitation and the
    probability that an individual donates ... larger match ratios (i.e., $3:$1 and $2:$1) relative to smaller match
    ratios ($1:$1) had no additional impact."
  - That result is for direct-mail donors, not institutions. Brief 8.17 already warns against over-applying such
    results.
  - Guess: at most one line offering a 1:1 match on the above-floor part, and only up to an amount already bought. It
    must never touch the operating reserve.
  - This may fail "complexity must earn its place". D5 should decide whether institutions respond to founder matches.
    If unclear, drop it.
- Would change: **decision** (match or no match).
- Deliverables: FR. Specialist: D5. Seed: null.
- North Star: turns her upside into a lever for others' giving, but only if that is simple and honest.

**Q13. Should the fundraising part state a two-way "no substitution" rule: co-sponsor money never replaces Laura's ten
operating payments, and her operating reserve is never drawn for the building?**
- Anchors: R-C48, R-C44, R-AN6, R-C71, BS-17.
- Official words: "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this
  requirement." and "The proposed range must also protect the portfolio’s ability to fund the ten-year operating
  commitment." (case p.3, VRF)
- Hypothesis (GUESS):
  - Yes, as one element. The case's asymmetry is a firewall in both directions.
  - Funders of buildings fear being asked for running costs (BS-17, SSIR, VP via A3). Founders' personal promises can
    also be quietly "backfilled" by donor money. Stating both directions answers both fears.
  - "Supplement, not supplant" is a U.S. public-grant phrase for the same idea (ASM: general knowledge, not verified
    here; D10 to check before any use).
- Would change: **sentence** (one checklist element).
- Deliverables: FR. Specialist: D5 (with D10). Seed: 6.
- North Star: shows we understood why the case splits the money the way it does.

**Q14. How can the fundraising part sound confident without overpromising? People prefer confident advisers but do
not dislike advice given as ranges, and numeric uncertainty barely dents trust in the source.**
- Anchors: R-AN30 (pull quote vs co-sponsor task), R-S28, R-C66.
- Official words: "communicates Laura's potential facility contribution and investment uncertainty clearly and
  credibly to prospective co-sponsors" (SMApply criterion 5, VRF)
- Hypothesis (GUESS):
  - Gaertig & Simmons 2018 (VP abstract): participants "did not dislike advisors who expressed uncertainty by
    providing ranges of outcomes, giving numerical probabilities", while advisers who were "not sure" were judged
    worse. The authors conclude: "Advisors benefit from expressing themselves with confidence, but not from
    communicating false certainty."
  - van der Bles et al. 2020 (VP abstract): "only a small decrease in trust in numbers and trustworthiness of the
    source, and mostly for verbal uncertainty communication".
  - Rule: be confident about the method and the floor, and give uncertainty as numbers. Ban vague hedges
    ("hopefully", "should be able to", "we are not sure").
  - This resolves seed 15 in communication terms: private conviction becomes public proof through a number already
    bought. The pull quote itself is still unattributed (R-AN30); do not quote it as hers until verified.
- Would change: **sentence** (tone rules for the draft).
- Deliverables: FR. Specialist: D9 (with D6). Seed: 15.
- North Star: sounds like Laura at her best, sure of the plan and honest about the numbers.

**Q15. Which two or three drivers of change should the 2031 statement name in advance? Explaining uncertainty up front
protects trust when the numbers later change.**
- Anchors: R-C70, R-C86, R-C65.
- Official words: "They should explain how favorable and unfavorable market outcomes could affect the amount she can
  provide." (case p.3, VRF)
- Hypothesis (GUESS):
  - Dries et al. 2024 (VP abstract): "communicating uncertainty buffers against a loss of trust when evidence changes.
    Moreover, explaining uncertainty does not appear to harm trust."
  - Jenkins, Harris & Lark 2019 (VP abstract, RePEc): perceptions were "least affected by the 'erroneous' prediction
    when it was expressed numerically".
  - Candidate drivers, if Q4 keeps some market exposure: returns on the unlocked part; for NT$ readers, the exchange
    rate; and Laura's own flexibility choice.
  - Name them once, with the direction each one moves the amount. Nothing more.
- Would change: **sentence** (the "what moves it" element).
- Deliverables: FR. Specialist: D9. Seed: null.
- North Star: if a number changes in 2032, co-sponsors were told why it might.

**Q16. Should the fundraising part attribute the range and confidence to Laura's investment team, with a date, the main
assumptions and the limits of the projection, the way regulated advisers must disclose hypothetical projections?**
- Anchors: R-C72, R-C69 ("how confident *they* are": the team's confidence), R-W29 (CFA Asset Manager Code), SH-25.
- Official words: "Each team must also draft part of Laura’s fundraising materials describing this potential
  contribution for prospective co-sponsors." (case p.4, VRF)
- Hypothesis (GUESS):
  - The case places the confidence with the team ("how confident they are"). The materials are Laura's. One
    attribution line ("assessment prepared by her investment team, as of [date]") resolves who speaks.
  - An independent-looking assessment is also more credible than a founder grading herself (INT).
  - Disclosure standards give a ready checklist:
    - The CFA Asset Manager Code requires disclosures that are "truthful, accurate, complete, and understandable"
      (VP via A3, stakeholder map).
    - The SEC Marketing Rule requires advisers showing hypothetical performance to disclose "criteria used and
      assumptions made" and "risks and limitations" (SNIP; sec.gov returned 403, eCFR 406).
  - The Marketing Rule does not apply to a fundraising letter (INT). Its elements are borrowed as a checklist, not as
    a legal claim.
- Would change: **sentence** (attribution and as-of line); **decision** (whose voice).
- Deliverables: FR. Specialist: D10 (with D8). Seed: null.
- North Star: a fictional firm acting like a real, regulated one, which the Rules page asks for (R-W29).

**Q17. What minimum checklist must the "part of Laura's fundraising materials" meet to be credible to a funder's
finance reader and a non-specialist at once, and what should be left out?**
- Anchors: R-C72, R-AN21, R-S28, R-C83, R-C64-R-C71.
- Official words: "Communicates Laura’s potential facility contribution to co-sponsors clearly and credibly." (case
  p.4, VRF)
- Hypothesis (GUESS), a checklist, not text:
  - **Contains:**
    1. The floor: amount in US$, "already set aside" on a stated date, and in what form (Q9, Q10).
    2. The range above it, with the probability of reaching the top in dual format and its reference class (Q1, Q2,
       Q6).
    3. The chance of missing on each side (Q8).
    4. What moves the amount, named in advance (Q15).
    5. That ten years of operating payments are funded separately from her portfolio alone, with the two-way
       firewall (Q13).
    6. That it is sized from her portfolio, not from a facility budget, and does not rise with cost overruns (Q11).
    7. Currency: US$ binding; NT$ as a dated illustration (Q5).
    8. Who prepared the assessment and when, plus key assumptions and limits (Q16).
    9. When it will next be updated (B1a Q19).
  - **Leave out:** facility cost or funding gap (scope); model jargon (percentiles, lognormal) in the co-sponsor part
    (keep it in the FR method box); any claim about legal enforceability (not the team's question, BS-05); any
    personal detail about Laura (privacy); drafted text from AI (AI policy).
  - Length test: a non-specialist should get elements 1-5 in one reading (SH-09).
- Would change: **sentence** (structure of the FR fundraising part).
- Deliverables: FR. Specialist: D5 (with D9). Seed: 9.
- North Star: a co-sponsor finishes reading knowing exactly what Laura will give, how sure it is, and what is
  already done.

**Q18. How wide can the stated range be before non-specialists find it useless?**
- Anchors: R-AN9, R-C67, R-C69.
- Official words: "she wants to communicate a credible range for her potential contribution." (case p.3, VRF)
- Hypothesis (GUESS):
  - Evidence:
    - Du, Budescu, Shelly & Omer 2011 (VP abstract): investors' preference for imprecision "peaks for low levels of
      imprecision and diminishes when the range gets wider". Investors "favor forecasts that are as precise as
      warranted by the information available, but not more precise".
    - Yaniv & Foster 1995 (SNIP, from a search summary): people often prefer an informative wrong interval to a
      correct wide one.
  - Derived ratios (top divided by bottom):
    - the 2026-view band $159k-$273k: about 1.72;
    - the median-2031 band from floor to p90 ($165k-$215k): about 1.30;
    - p5-p95 at the median 2031 state: about 1.09.
  - Guess: a ratio well under about 1.3 reads as informative; 1.7 reads as "we don't know". That threshold is ASM
    until D6 finds evidence.
- Would change: **number** (range width and how the FR presents it).
- Deliverables: FR. Specialist: D6 (with D3). Seed: 9.
- North Star: a range narrow enough to plan with is the difference between a pledge and a shrug.

**Q20. Which single Final Report chart shows co-sponsors the floor, the range and the confidence most clearly: a fan
chart from 2027, or a bar (bought floor) with a range whisker for three 2031 starting states?**
- Anchors: R-S28 ("uses data effectively"), R-C70, brief section 13 (charts in the FR only).
- Official words: "uses data effectively to support conclusions" (SMApply criterion 5, VRF)
- Hypothesis (GUESS):
  - Dieckmann et al. 2015 (VP abstract): "simple graphical representations can decrease the variance in
    distributional perceptions".
  - The Fed's projection fan charts show 70% bands "based on historical forecast errors" (VP, SEP 2026-09-16 notes).
    That is a model, but a fan from 2027 visually repeats the misleading 2026-view width (Q3).
  - Guess: the bar plus whisker at three 2031 states is for co-sponsors. A fan chart, if any, goes in the method
    section for Laura. Data: the three rows in Q3 plus the floor.
- Would change: **decision** (which chart; data needed).
- Deliverables: FR. Specialist: D9. Seed: null.
- North Star: one picture a co-sponsor could redraw from memory.

**Q21. Numbers survive translation and verbal probability words do not. Should every probability in the fundraising
part be numeric, so a Mandarin-reading Taiwanese partner reads the same confidence as an English reader, without the
team translating anything?**
- Anchors: R-AN10, BS-12, R-C69, SH-06, SH-07.
- Official words: "In 2033, Laura plans to establish a collaborative creative residency in Taiwan." (case p.2, VRF)
- Hypothesis (GUESS):
  - Budescu et al. 2014 (VP abstract): under the dual format, "interpretations of the terms in various languages are
    more similar".
  - Translation stays out of scope (BS-12). Numeric probabilities make the text translation-proof at zero cost.
  - This is a practical point, not identity decoration (tokenism rule).
- Would change: **sentence** (a rule in the checklist).
- Deliverables: FR. Specialist: D9 (with D4). Seed: null.
- North Star: the plan works for the people in Taiwan who will actually read it.

**Q22. Should the 2031-2033 band be cross-checked against actual past two-year outcomes of a sleeve-like mix (as the
Fed's projection bands use past forecast errors), not only the lognormal model, so that both a statistician and a
funder's finance reader accept the confidence number?**
- Anchors: R-C55, R-S26 ("reasonable assumptions"), R-AN32, brief section 11 (i.i.d. lognormal, no fat tails).
- Official words: "explain how they evaluated that level of certainty, and identify the assumptions supporting their
  recommendation." (case p.3, VRF)
- Hypothesis (GUESS):
  - The Fed notes (VP) say its band "is based on root mean squared errors of various private and government forecasts
    made over the previous 20 years", and warn it "may not reflect ... current assessments".
  - With only about 20% of the sleeve unlocked for two years (Q4), even a 2008-type fall should move the 2033 amount
    by a few percent. D3 computes it from a long history of monthly returns (for example, FRED or published index
    data).
  - A historical worst case beside the model p5 is cheap and persuasive.
- Would change: **number** (the stated confidence, and the bottom of the market band if not fully locked).
- Deliverables: FR. Specialist: D3. Seed: 9.
- North Star: Laura can check our "9 in 10" against history herself.

**Q23. Should every sentence of the fundraising part pass a "floor test": still true if 2033 lands exactly at the
floor? This would be a one-line pre-submission check against overpromising.**
- Anchors: R-C66, R-C71, R-AN9.
- Official words: "If Laura promises more than she can ultimately contribute, she could damage her credibility"
  (case p.3, VRF)
- Hypothesis (GUESS):
  - Yes. It turns the Gneezy & Epley asymmetry (Q7) and the boundary effect (Q6) into a check a student can run in
    five minutes.
  - Also run a "top test": no sentence implies the top is expected.
- Would change: **decision** (review rule for the FR draft).
- Deliverables: FR. Specialist: D9. Seed: null.
- North Star: nothing in the letter she sends could ever become untrue.

### Parked (fail the "would change" filter or out of scope; logged only)
- Legal enforceability of a founder's pledge in Taiwan or the U.S. (out of scope: Taiwan legal; BS-05).
- Translating the draft into Mandarin (out of scope and complexity; Q21 covers it at zero cost).
- Donor-recognition and naming rights (no case anchor).
- Finale-style questions on how judges would challenge the range (scope: semifinals only).

---

## 3. Evidence found (claims with status)

| # | Claim | Status | Source |
|---|---|---|---|
| E1 | Laypeople read IPCC probability words as closer to 50% than intended; numbers alongside words fix it across 17 languages | VP (abstract) | Budescu, Por, Broomell & Smithson, *Nature Climate Change* 4:508-512, 2014-04-20 |
| E2 | Respondents deviated from IPCC guidelines "even when the respondents had access to these guidelines" | VP (abstract via Europe PMC) | Budescu, Broomell & Por, *Psychological Science*, 2009 |
| E3 | "likely" = "≥66% ... to 100%"; prefer "a probability range (e.g., 90-95%)" when information allows; "Consider reciprocal statements" | VP (paragraphs 4 and 10; the Table 1 text layer is garbled) | IPCC AR5 Uncertainty Guidance Note (Mastrandrea et al. 2010) |
| E4 | Reference class must be specified for single-event probabilities | VP (abstract via Europe PMC) | Gigerenzer et al., *Risk Analysis*, 2005 |
| E5 | Boundary effect; "can" label softens the upper edge | VP (abstract, open access) | Teigen, Løhre & Hohle, *Judgment and Decision Making* 13(4):309-321, July 2018 |
| E6 | "Can" predictions are extreme but believed probable | SNIP | Teigen & Filkuková (UiO project listing) |
| E7 | Numeric uncertainty causes only a small drop in trust, mostly for verbal formats | VP (abstract) | van der Bles et al., *PNAS* 117:7672-7683, 2020 |
| E8 | Numbers protect credibility after "unlikely" outcomes | VP (abstract on RePEc) | Jenkins, Harris & Lark, *Journal of Risk Research* 22(5):537-554, 2019 |
| E9 | Uncertainty communicated up front buffers trust loss when evidence changes | VP (abstract) | Dries et al., *Public Understanding of Science*, 2024 |
| E10 | People do not dislike uncertain advice given as ranges or probabilities; "not sure" advisers are judged worse | VP (abstract) | Gaertig & Simmons, *Psychological Science*, 2018 |
| E11 | Preference for range precision peaks at low imprecision | VP (abstract on RePEc) | Du, Budescu, Shelly & Omer, *OBHDP* 114(2):179-189, 2011 |
| E12 | Informativeness is often preferred over accuracy (730-780 vs 700-1500 miles) | SNIP | Yaniv & Foster, *JEP: General*, 1995 |
| E13 | A best estimate shifts perceived distribution toward normal; simple graphics reduce variance of perceptions | VP (abstract) | Dieckmann, Peters & Gregory, *Risk Analysis*, 2015 |
| E14 | Exceeding a promise is not valued above keeping it | VP for the press release; paper SNIP | ScienceDaily / Chicago Booth release, 2014-07-18 |
| E15 | Match offers raise giving; 2:1 and 3:1 no better than 1:1 | VP (abstract) | Karlan & List, NBER w12338 / *AER* 97(5), 2007 |
| E16 | Kresge counted "Written pledges or cash"; other sources "committed, imminent or backstopped"; pledges committed before the public hears; cost estimates "firm"; 20-50% of the private goal raised before applying | VP (PDF read) | Kresge Foundation, *A Guide to the Challenge Grant*, updated 2011-06-30 |
| E17 | Fed SEP bands: 70% intervals from 20 years of forecast errors, with a caveat on current conditions | VP | FOMC SEP accessible version, 2026-09-16 |
| E18 | SEC Marketing Rule: disclose "criteria used and assumptions made" and "risks and limitations" of hypothetical performance | SNIP (sec.gov 403; eCFR 406) | search summaries of Rule 206(4)-1 |
| E19 | 2.8% of 2026-view variance unresolved in 2031; conditional 90% widths $15k/$18k/$23k; full lock costs about $1k median; P(below floor)=0, P(above p90)=0.10 at the median state | Derived from VRF script; inputs ASM | section 5 script (scratchpad), `strategy_mc.py` |

---

## 4. Leads for the specialists

**D5 (philanthropy & co-sponsors)**
- Kresge *Guide to the Challenge Grant*: https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf (VP,
  2026-09-27).
  - Readiness indicators 1-7, pages 5-6 of the PDF text.
  - "What Gifts Count?" is page 8.
  - Glossary: "Backstopping" and "Challenge grant".
  - Use these for Q9, Q10, Q11.
- Kresge centennial page on its first challenge grants (1929): https://kresge.org/centennial/ (SNIP; not opened).
- Karlan & List 2007 abstract: https://www.nber.org/papers/w12338 (VP) for Q12. Check whether any study covers
  institutional (not individual) responses to founder matches. If none, recommend dropping Q12's match.
- A3's sources W-3 (SSIR starvation cycle) and W-6 (PKF funder due-diligence bulletin) pair with Q13 and Q11.

**D9 (communication & plain English)**
- IPCC AR5 guidance note PDF: https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf.
  Paragraphs 4 and 10 are VP. Table 1 needs reading from the rendered page (the text layer is garbled).
- Budescu 2014: https://www.nature.com/articles/nclimate2194 (abstract VP).
- Budescu's IPCC 2016 slides: https://www.ipcc.ch/site/assets/uploads/2016/02/Budescu_IPCC_Communication_Meeting_OSLO_February_2016.pdf
  (not opened).
- Teigen et al. 2018 (open access, CC-BY):
  https://www.cambridge.org/core/journals/judgment-and-decision-making/article/boundary-effect-perceived-post-hoc-accuracy-of-prediction-intervals/AED4A7230EA737078997644325739C38
  Experiment 5 is the "can" label result.
- Europe PMC REST API works through the proxy where PubMed blocks. For example:
  `curl "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22...%22&format=json&resultType=core"`.
  It returns full abstracts.
- Nature Climate Change 2025 "Negative verbal probabilities undermine communication of climate science":
  https://www.nature.com/articles/s41558-025-02472-1 (title only, SNIP). Relevant to directional words ("not
  certain" vs "possible").
- Irwin 2023 *Risk Analysis* on verbal vs numeric formats for expert and non-expert readers:
  https://onlinelibrary.wiley.com/doi/abs/10.1111/risa.14009 (title only, SNIP).

**D3 (quant modelling)**
- Re-run section 5 with the 2031 two-year yield at 3%, 4% and 5%. Report the median cost of a 100% lock (Q4).
- Add a historical two-year worst case for a 60/40 sleeve (Q22).
- Report the three-state table (Q3) and the side-split miss probabilities (Q8).
- Label every output as model-based with ASSUMPTION inputs.

**D4 (Taiwan & FX)**
- Combine F-513's 2-year USD/TWD distribution with the Q3 USD band to give an NT$ band (Q5). State the independence
  ASSUMPTION or estimate the correlation of USD/TWD with U.S. equities.

**D6 (behavioural)**
- Gneezy & Epley paper (SSRN https://www.ssrn.com/abstract=2233670 blocked; try the SAGE DOI
  10.1177/1948550614533134) for Q7.
- Du et al. 2011 and Yaniv & Foster 1995 (PDF: https://deanfoster.net/research/YanivFoster1995JEPG.pdf, not opened)
  for a width threshold (Q18).

**D10 (compliance)**
- SEC small-business guide on adviser marketing (403 here): try another route to the rule text (for example
  federalregister.gov, final rule release IA-5653) to verify E18 before Q16 cites it.
- Confirm that A3's CFA Code F.2 quote is exact.

---

## 5. Script used (kept in the scratchpad; the numbers are reproducible)

`b6b_vantage.py` (scratchpad, not committed): it imports `research/verified_2026-09-27/strategy_mc.py` (VRF),
regenerates the same 200,000 paths (seed 20260927, JPM LTCMA inputs, lognormal ASM, 2031 two-year yield 4.81% ASM,
60% equity sleeve, 80% floor) and reports:

| Measure | Result |
|---|---|
| 2026-view 2033 sleeve p5/p50/p95 | $159k / $207k / $273k (matches F-401) |
| Variance still unresolved on 1 Jan 2031 | 2.8% |
| Weak 2031 (p10 sleeve $153k): floor, p5-p95 | $134k; $162k-$177k |
| Median 2031 (sleeve $188k): floor, p5-p95 | $165k; $199k-$217k |
| Strong 2031 (p90 sleeve $232k): floor, p5-p95 | $204k; $246k-$269k |
| Floor share 50% / 80% / 100% at the median state | p5-p95 $188k-$234k / $199k-$217k / $206.1k exactly |
| Range [floor, conditional p90] at the median state | P(in) 0.900, P(below) 0.000, P(above) 0.100 |

Main loop (for D3 to re-create):
`s` = sleeve grown 2027-2030 with the 2028 deposit; `g2` = two-year sleeve growth for 2031-2032;
`total_2033 = f*s*1.0481**2 + (1-f)*s*g2`; conditional bands use quantiles of `g2` at fixed `s`.

---

## 6. Sources (all accessed 2026-09-27)

| Source | URL | Status |
|---|---|---|
| Official case, IPS guide, TN guide, SMApply page | `competition/official/2026_27/` | VRF |
| Phase A registers (R-, F-, SH-/BS-, G ids) | `research/insight_v1/phase_A/` | repo |
| Budescu et al. 2014 | https://www.nature.com/articles/nclimate2194 | VP (abstract) |
| Budescu et al. 2009; Gigerenzer et al. 2005; van der Bles et al. 2020; Gaertig & Simmons 2018; Dries et al. 2024; Dieckmann et al. 2015 | Europe PMC REST API, https://www.ebi.ac.uk/europepmc/webservices/rest/search | VP (abstracts) |
| IPCC AR5 Uncertainty Guidance Note | https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf | VP (paragraphs 4, 10) |
| Teigen, Løhre & Hohle 2018 | cambridge.org URL in section 4 | VP (abstract and intro) |
| Jenkins, Harris & Lark 2019 | https://ideas.repec.org/a/taf/jriskr/v22y2019i5p537-554.html | VP (abstract) |
| Du et al. 2011 | https://ideas.repec.org/a/eee/jobhdp/v114y2011i2p179-189.html | VP (abstract) |
| Gneezy & Epley 2014 (press release) | https://www.sciencedaily.com/releases/2014/07/140717094556.htm | VP (release); paper SNIP |
| Karlan & List 2007 | https://www.nber.org/papers/w12338 | VP (abstract) |
| Kresge *Guide to the Challenge Grant* (2011) | https://kresge.org/sites/default/files/GuidetoChallengeGrant.pdf | VP |
| FOMC SEP 2026-09-16 | https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm | VP |
| Teigen & Filkuková "Can > will" | https://www.sv.uio.no/psi/forskning/prosjekter/subjektive_sannsynligheter/ (search listing) | SNIP |
| Yaniv & Foster 1995 | https://philpapers.org/rec/YANGOJ (search summary) | SNIP |
| SEC Marketing Rule summaries | https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/investment-adviser-marketing (403) | SNIP |
| Blocked or refused | sec.gov (403), eCFR (406), PubMed (browser check), SSRN (per brief) | reported, not guessed |

Web search budget ran out during this task (200/200). Further lookups used direct fetches and the Europe PMC API.

---

## What this teaches

A forecast is only as good as the way it is heard. Research on weather, climate and earnings forecasts shows three
things:
- People read words like "likely" as a coin flip.
- They treat the edges of a range as a pass/fail line.
- They reward a kept promise as much as a beaten one.

So the credible way to state Laura's 2031 contribution is:
- a bottom that is already bought;
- a range narrow enough to plan with (and by 2031 it can be, because about 97% of the uncertainty has already played
  out);
- probabilities written as numbers with what they are "out of";
- each side of a possible miss stated separately.

Funders count written, committed money, not forecasts. That is why the floor, and the date it is bought, matter more
than how high the top of the range is.
