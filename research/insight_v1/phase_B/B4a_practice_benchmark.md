# B4a Top-Practitioner Benchmark: institutional practice (pensions, insurers, endowments, foundations, Australian funds)

Agent: B4a, insight_v1 run, Phase B (question generation). Written 2026-09-27. Starting angle: how institutions that
owe fixed nominal amounts fund them: cash-flow matching, immunisation, funded-ratio glide paths, hedge ratios, surplus
risk, sponsor backing, spending and pledge policies. The other B4 agent starts from private banks and goals-based
wealth management; I have stayed on the institutional side.

This file is AI-generated research for Team Caplet, for brainstorming only. It holds **no submission-ready prose**.
Where it says what a sentence "must contain", that is a checklist; the students write every word. No securities are
recommended here.

Status labels follow brief section 3. Short forms in dense places: **VP** = VERIFIED-PRIMARY (I read it on the page
on 2026-09-27; URL in section 4), **VRF** = VERIFIED-REPO-FILE, **SNIP** = SNIPPET-UNVERIFIED, **ASM** = ASSUMPTION,
**INT** = INTERPRETATION (my reading, not a fact). R-, F-, BS-, SH- and X- ids point to the Phase A files.

---

## 0. Summary (read this first)

I wrote 25 questions. Six stand out because they rest on primary sources nobody in the repo has used, and because
their answers would change something the team does in the next four weeks:

1. **Q3. The UK pension regulator's own yardstick says Laura's promise is already "mature".** The UK Defined Benefit
   Funding Code (November 2024, VP) says a scheme with no cash-balance benefits reaches "significant maturity" when
   its liability duration is **10 years**. By then the regulator expects a "low dependency" portfolio, hedged to "at
   least 90%". The duration of Laura's ten payments is **about 10 years today** (spot 10.16y, F-105; 9.90y at
   2027-01-01, F-103). A regulator's threshold, reached on day one, is an outside argument for hedging at once
   instead of drifting down a time-based glide path. It needs no model.
2. **Q2. Laura has no "sponsor", and the case built it that way.** Pensions may take investment risk when an employer
   can make up shortfalls: the UK code says "more risk can be allowed for where the scheme has access to sufficient
   employer cash flows" (VP). Australia's Future Fund chases CPI + 4-5% because the Commonwealth stands behind the
   pensions it pre-funds (VP; its drawdowns start "at least 2032-33", the same year as Laura's first payment). The
   case bans outside money for the payments, and "continued business income" is on the outside list (R-C44, R-C48,
   R-AN24). So Laura's sponsor backing after 2028 is nil. This gives one plain reason to hedge that a judge would
   recognise, and it is honest about why a famous long-horizon fund does the opposite.
3. **Q5. Fees can quietly un-fund a "fully funded" ladder.** JPMorgan's 2021 pension paper warns that hibernation
   strategies "will burn through capital over time" (VP). For Laura the headroom is only $7,736 (F-104). ASM
   arithmetic: a 0.15% fund expense charged on the reserve costs about **$4.4k** in 2027 money (57% of the headroom).
   A 0.5% advisory fee on the reserve costs about **$14.7k** (1.9 times the headroom). A3 (BS-01) modelled fees on the
   sleeve only. The practitioner answer is to hold the reserve as directly owned Treasuries, charge every fee to the
   sleeve, and say so in the IPS.
4. **Q20. Measure the WInS Treasury sleeve the way a pension CIO does: funded status and hedge effectiveness, not
   return.** A weekly log of the change in bond value against the change in the ten payments' present value
   ($289 per basis point, F-103) turns a falling bond fund into evidence that the strategy was "tested". That is the
   guide's own word (R-T20). It must start with the first trade to be usable by Oct 23.
5. **Q6. Australia already has a written rule for "what if the promise is under-funded at purchase".** APRA's SPS 160
   (VP) requires a board-set "shortfall limit" and a "restoration plan" that restores full funding "within ... three
   years". That is the missing rule-if-rates-fall-first (brief section 9; P(cost > $300k) about 24%, F-112) in
   regulator form: trigger, deadline, source of top-up (the 2028 deposit). An Australian angle that earns its place.
6. **Q12. Yale sets each year's spending from its endowment value "from two years ago"** (VP, Yale Provost). The case
   makes Laura name her 2033 contribution two years early, in 2031 (R-C62, R-AN7). The world's best-known spending
   rule uses the same two-year lag, and uses it to make budgets predictable. That is a recognisable precedent for
   stating the 2031 range as a rule rather than a forecast.

Other new evidence:
- The case's list of assumptions (R-C85) nearly matches the legal "prudence" factors for endowment spending under
  UPMIFA (Q13).
- Municipal finance separates "economic" from "legal" defeasance, with an independent "Verification Agent" report
  (Q7). This is new evidence for brief section 8 item 9 ("funded 2027, set aside 2033").
- Morningstar's 2025 study finds that taxable-bond fund investors captured "only about half" of their funds' returns
  (Q19). That is a reason to hold the reserve as individual bonds, not funds.
- Australia's Standard Risk Measure reports risk as "years of negative annual returns over any 20-year period"
  (Q21). ASM: the 60/40 sleeve comes out at about 5.4 of 20, while a hold-to-maturity ladder shows negative years even
  though its payments are certain.

Seed questions extended: 22 (Q9, Q25), 26 (Q1, Q2, Q3), 27 (Q19), 28 (Q24).

---

## 1. Method

1. Read the brief, v4 Parts 1-3, 5 and 6, CLAUDE.md, the official case, the IPS and Trading Notes guides, and the
   Phase A files (case register, fact register, stakeholder map, WInS guardrails). I also read the council's
   judge-panel file and team notes, so as not to repeat them.
2. Checked brief section 8 (already answered). Where a question touches an answered item, I say what is new.
3. Searched for institutional frameworks with WebSearch, then read each page with `fetch_text.py` or curl. Anything I
   could not open is labelled SNIP.
4. Did small arithmetic in Python on verified inputs (F-101, F-104, F-107, F-110, F-301, F-307). No script was saved:
   the calculations are one-liners, reproduced in section 3. Every result is labelled ASM.
5. Blocked or refused sources: the FSC-ASFA Standard Risk Measure guidance PDF (HTTP 403); AustLII (403); the Future
   Fund site (403 per brief; not retried); Powerball's own FAQ gave no matching text (read via Marketplace instead);
   the S&P defeasance criteria were not found on a primary page.

---

## 2. The questions

Format for each: the question; anchors; the official words or verified fact it hangs on; hypothesis (a guess, with
evidence); what would change; deliverables; specialist; seed; north star.

### A. Is the promise "funded" by a practitioner's standard? (WInS-now, TN, IPS)

**Q1. What surplus buffer above 100% funded do pension practitioners require before they call a plan "hibernated",
and is Laura's 102.6% (a 27bp cushion) enough to call the promise "high certainty" before the 2028 deposit
arrives?**
- Anchors: F-117 (funded ratio 1.026), F-104 (headroom $7,736 = 27bp), F-111 (the ladder cost more than $300k on 173
  of 185 trading days in 2026), R-C47.
- Hypothesis (guess):
  - NISA (2021, VP) argues plans "greater than 95% funded" should hibernate now, and that a "105% funded plan has
    essentially no potential contributions (as measured at a 95% confidence level)".
  - Those plans have sponsors who can add money; Laura has none after 2028 (Q2).
  - So a practitioner would call 102.6% "funded but thin", and would count the 2028 deposit as the buffer that turns
    "funded" into "high certainty".
  - The answer probably changes one IPS sentence: certainty is reached when the ladder is bought *and* a stated buffer
    exists (the 2028 deposit, then the sleeve). It does not change the architecture.
- Would change: **sentence** (IPS certainty definition; FR evaluation of certainty). Possibly a **number**: a stated
  buffer target, e.g. ladder cost at most X% of assets.
- Deliverables: IPS, FR. Specialist: D8. Seed: 26.
- North star: shows Laura that "fully funded" was tested against the people who do this for a living, not declared.

**Q2. Because the case forbids outside money for the payments (including "continued business income"), is Laura's
"sponsor backing" effectively nil after 2028? If so, does practitioner logic (the UK code's "employer covenant", and
the contrast with Australia's Future Fund) say the promise must be hedged rather than invested for growth?**
- Anchors: R-C48, R-C44, R-AN24.
- Official words: "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet this
  requirement." (case p.3, VRF)
- Hypothesis (guess): yes.
  - UK DB Funding Code, para 29(a) (VP): risk must be "dependent on their assessment of the employer covenant, where
    more risk can be allowed for where the scheme has access to sufficient employer cash flows and contingent assets to
    support this level of risk".
  - Future Fund (VP, Treasurer's release): "the benchmark return rate will remain at between four and five per cent
    above CPI per annum over the long term". It pre-funds public-servant pensions that the Commonwealth still
    guarantees. Its drawdowns start "at least 2032–33", the same year as Laura's first payment.
  - One fund can chase growth because a government stands behind it. Laura's promise has nobody behind it. That is the
    one-line reason for hedging.
  - The Australian team angle earns its place here: it is a real, dated, checkable contrast, not decoration.
- Would change: **sentence** (the IPS "why this strategy fits her"; an FR alternatives paragraph).
- Deliverables: IPS, FR. Specialist: D8. Seed: 26.
- North star: explains why her plan is not a copy of any famous fund. It follows from her one hard constraint.

**Q3. The UK regulator treats a pension with a liability duration of 10 years as "significantly mature" and expects
it to be in a low-dependency, at-least-90%-hedged portfolio. Laura's promise has a duration of about 10 years from day
one. Should the team use this outside yardstick to justify full hedging in 2027, instead of the gradual time-based
de-risking that Wharton's own Trading Note example suggests?**
- Anchors: F-105 (spot duration 10.16y), F-103 (9.90y at 2027-01-01), R-T25, R-I12, X-2.
- Official words: "This trade supports our plan to balance continued growth with reliable future cash flows as the
  residency funding date approaches." (TN guide p.2, VRF)
- Hypothesis (guess): yes, as Final Report evidence, never as IPS jargon.
  - DB Funding Code para 22(a) (VP): "For schemes with no cash balance benefits, the duration is 10 years."
  - Para 20 (VP): "we expect schemes to target a minimum level of interest rate and inflation hedging of at least 90%".
  - SI 2024/462 reg 5 (VP) defines the low-dependency allocation as "highly resilient to short-term adverse changes in
    market conditions so that further employer contributions are not expected to be required".
  - Laura's case is the no-employer version, so the logic applies more strongly.
  - Caveat: the UK measures duration on its own funding basis. Laura's figure is on Treasury rates. The claim should
    be "about 10 years, at the regulator's threshold", not an exact match.
- Would change: **decision** (confirms hedge-now over glide). **Sentence** in the FR on why the plan departs from the
  Wharton example's gradual path.
- Deliverables: FR, IPS. Specialist: D8 (with D1 for the duration basis). Seed: 26.
- North star: a stranger with authority (a regulator) reaches the same answer as our model, which is what a
  statistics graduate would want to see.

**Q4. Should the IPS say the portfolio follows a funded-status glide path (it de-risks as the funded ratio rises),
not a calendar glide path, and then say plainly what still changes over time?**
- What still changes: the reserve pays itself out; the sleeve moves toward the 2031 floor.
- Anchors: R-I12, R-I21, R-C53, R-AN27, X-2, R-T25.
- Official words: "How will the portfolio’s asset allocation and composition change as future funding needs approach
  and payments are made?" (IPS p.1, VRF)
- Hypothesis (guess):
  - Institutional glide paths are usually triggered by funded status. NISA (VP) writes of "the near ubiquity of
    glidepaths among our clients"; the pension de-risking literature (Russell, BlackRock; SNIP) describes funded-status
    triggers.
  - Laura starts at 102.6% funded, so a funded-status path says "hedge fully now".
  - The Wharton example assumes a calendar path. The IPS must answer the prompt ("changes as funding needs approach")
    without contradicting lock-early.
  - Answer: name the trigger (funded status) and list three planned changes: 2028 top-up, 2031 floor, post-2033
    run-off.
- Would change: **sentence** (IPS answer to prompt 4). **Decision**: which three changes the IPS lists.
- Deliverables: IPS, TN. Specialist: D7 (designer intent) with D8. Seed: 28.
- North star: answers the IPS prompt head-on while keeping the promise safe. Most teams will write a calendar glide
  path by habit.

**Q5. What fees will Laura pay on the reserve, and do they un-fund a ladder that has only $7.7k of headroom? Should the
IPS say the reserve is held as directly owned Treasuries and that all fees come out of the growth sleeve?**
- Anchors: BS-01 (A3), F-104, F-107.
- Rules page (via A1, R-W29, VP): teams operate by the CFA Asset Manager Code. That Code requires fee disclosure
  (F.4.d, per A3).
- What is new vs BS-01: A3 modelled a fee on the sleeve and said the payments are safe "only as long as the fee is paid
  from the sleeve". Here is the size of the risk if it is not.
- Hypothesis (guess, ASM arithmetic):
  - Method: present value of a yearly fee f on the ladder ≈ f × Σ(rung cost × years held) = f × $2,933,301 (F-107
    rung costs; value grows at the curve).
  - Results: 0.07% → $2.1k; 0.15% (IEF/TLT expense) → $4.4k; 0.5% → $14.7k; 1.0% → $29.3k. Against $7,736 headroom.
  - JPMorgan (Oct 2021, VP): "Hibernation strategies will burn through capital over time". Same mechanism.
  - In WInS, funds are fine (a six-week hedge). In Laura's real plan, the reserve should be individual Treasuries or
    STRIPS, with no fund expense, and the firm's fee charged to the sleeve.
- Would change: **number** (the funded ratio net of fees; the FR fee assumption). **Sentence** (an IPS cost
  principle).
- Deliverables: IPS, FR. Specialist: D3 (numbers), D10 (Code disclosure). Seed: null.
- North star: an honest firm shows Laura what it will cost her, and a rival that hides fees overstates her facility
  money.

**Q6. Should the IPS adopt APRA SPS 160's two-part rule as its "rule if rates fall before January 2027"?** The parts:
(a) a stated "shortfall limit" (how far below 100% funded the ladder may start); (b) a "restoration plan" that returns
the promise to 100% funded by a fixed date (1 Jan 2028, from the 2028 deposit first).
- Anchors: F-111, F-112 (about 24% chance the ladder costs more than $300k on 2027-01-01, ASM), F-102, R-C34.
- Official words: "Apart from the two contributions described above, she will neither add to nor withdraw from the
  portfolio before 2033." (case p.2, VRF)
- Hypothesis (guess): yes.
  - SPS 160 (VP) defines a shortfall limit as the dip from which the fund can "reasonably expect ... to be restored to
    a satisfactory financial position within one year".
  - It requires a restoration plan "within a time period that is reasonable in the circumstances of the fund but which
    must not exceed three years".
  - For Laura the restoration deadline is shorter and fixed: the 2028 deposit is the only new money.
  - The rule fits in about 25 IPS words and closes an open item (brief section 9). The council's "waterfall" already
    has the substance; SPS 160 gives it a recognised name and a trigger.
- Would change: **decision** (the rule's parameters: which rungs first, the trigger level). **Sentence** in the IPS.
- Deliverables: IPS, WInS-now (if rates fall during trading, the WInS book shows the same stress), FR. Specialist: D8
  with D1. Seed: null.
- North star: shows Laura the team has a pre-written plan for the one thing that could go wrong before she even
  invests. That is how trustees, not traders, behave.

**Q7. Can the plan borrow municipal finance's distinction between "economic defeasance" (Treasuries bought to cover
the payments) and "legal defeasance" (a formal escrow checked by an independent verification agent)?** It would
explain "funded in 2027, set aside in 2033". Should the Final Report include a one-table "sufficiency check" (each
rung's maturity value against each $50k payment), the way a Verification Agent report does?
- Anchors: R-AN28, R-C50, R-C55.
- Official words: "explain how they evaluated that level of certainty" (case p.3, VRF)
- New evidence for brief section 8 item 9: a named institutional precedent for "bought early, formally set aside
  later".
- Hypothesis (guess): yes.
  - NABL (VP): "The Verification Agent is responsible for independently confirming that the investments purchased for
    the Escrow Fund will be sufficient to fund the Debt Service payments".
  - NABL (VP): "Once Bonds are legally defeased, they are generally considered no longer outstanding".
  - Laura's 2027 purchase is the economic step; the 2033 "set aside" is the formal step. The table is simple, can be
    checked by hand, and answers "how they evaluated" with no model.
- Would change: **sentence** (FR reconciliation). **Decision** (add the sufficiency table to the FR).
- Deliverables: FR. Specialist: D8, D9. Seed: 22.
- North star: a statistics graduate trusts a check she can redo in five minutes more than a simulated percentile.

**Q8. Should the reserve be ring-fenced from 2027: held in a separate, labelled account, with a written rule that it
pays only the ten payments, and a named person who can override the rule (Laura) and under what condition?**
Institutions use trusts and escrow accounts for exactly this.
- Anchors: R-C50, R-C26 ("with an asset management firm"), BS-18 (operational risk), BS-08 (governance continuity).
- Official words: "Laura will set aside a portion of the portfolio to fund the ten payments. This set-aside is called
  the operating reserve." (case p.3, VRF)
- Hypothesis (guess):
  - Yes, as a one-line governance rule. The legal form (trust, escrow) is out of scope, and Taiwan law is excluded.
  - What matters is that the money cannot drift into the facility when the facility runs over budget. That is the most
    likely real-world failure.
  - NABL (VP): escrow for defeased bonds is an "irrevocable Pledge".
- Would change: **decision** (IPS governance clause). **Sentence** (the FR co-sponsor draft can say the operating
  money is held separately).
- Deliverables: IPS, FR. Specialist: D10, D8. Seed: 2.
- North star: protects Laura from her own generosity under pressure, and co-sponsors can see the separation.

**Q9. Where should "high degree of funding certainty" sit next to published institutional standards, and should the
Final Report show that comparison at all?** Standards: EU insurers must survive one year with 99.5% confidence; UK
low-dependency pensions must be at least 90% hedged; planners' "confidence zones" of 75-90% are for adjustable goals.
- Anchors: R-C54, R-AN1, F-117.
- What is new vs brief section 8 item 6: verified external benchmarks to place the model-free definition against.
- Hypothesis (guess):
  - Solvency II Directive (VP): capital to meet obligations with "a confidence level of 99,5 % over a one-year period".
  - TPR code (VP): hedging "at least 90%".
  - The planner confidence zone of 75-90% is SNIP.
  - A bought, cash-flow-matched ladder sits above all three in nominal terms, because it is not a one-year probability.
  - The honest framing: "these standards are probabilities; ours is a purchase". The comparison belongs in the FR, one
    line, to stop a judge asking "why no 95%?". It does not belong in the IPS.
- Would change: **sentence** (FR certainty section).
- Deliverables: FR. Specialist: D8, D9. Seed: 22.
- North star: speaks the language of a statistician: which standard, over which horizon, measured how.

**Q10. US public pensions discount their promises at their assumed return (median 7.0%, NASRA April 2026). At 7%,
Laura's ten payments would "cost" about $250k instead of $292k. Should the Final Report show this $42k gap to explain
why growth-first plans under-reserve?**
- Anchors: F-101, F-110, R-C77.
- Official words: "use reasonable return assumptions consistent with their strategy" (case p.4, VRF)
- New vs brief section 8 item 1: that item decided lock-early. This names the professional mistake behind the
  alternative and prices it.
- Hypothesis (guess, ASM arithmetic):
  - PV at 2027-01-01 of the ten payments at a flat 7%: $250,386. At JPM's 6.7% equity return: $257,485. At the
    Treasury curve: $292,264.
  - The understatement is $41.9k (14.3%) at 7%.
  - NASRA (VP): "the investment return assumption for most plans also serves as the discount rate used to determine the
    present value of the plan’s liabilities" and "A rate set too high will understate liabilities".
  - One FR sentence, possibly one chart bar, makes the case for pricing the promise at Treasury rates without jargon.
- Would change: **number** and **sentence** (FR portfolio analysis; a chart candidate: three bars for the "cost of the
  promise" at 7%, 6.7% and the Treasury curve).
- Deliverables: FR. Specialist: D3, D8. Seed: null.
- North star: shows Laura the trap many professionals fell into, and that her plan avoids it on purpose.

**Q11. Is the lottery annuity the plainest public precedent for "bought, not forecast"?** Powerball funds annuity
jackpots with U.S. Treasury securities, and "the higher the interest rates, the higher the advertised Grand Prize".
Would using it with co-sponsors and judges pass the "no gimmick" test?
- Anchors: R-C83, R-S28, R-AN21.
- Official words: "communicates Laura's potential facility contribution and investment uncertainty clearly and
  credibly to prospective co-sponsors" (SMApply criterion 5, VRF)
- Hypothesis (guess):
  - Useful only as a teaching line in the FR (or in the team's own learning), not in the co-sponsor draft. A lottery
    image sits badly next to a residency's credibility.
  - Marketplace (2022-11-08, VP) reports the annuity is paid "over a span of 30 years and accrues interest from
    investments in U.S. Treasury bonds".
  - It quotes the Powerball FAQ: "The higher the interest rates, the higher the advertised Grand Prize." (FAQ wording
    SNIP: not found on powerball.com today.)
  - The muni escrow (Q7) is the more dignified precedent.
- Would change: **sentence** (whether any everyday analogy appears, and which one).
- Deliverables: FR. Specialist: D9. Seed: null.
- North star: plain English that a creative founder would repeat to a partner. Also a warning against a flashy analogy
  she would find cheap.

### B. The facility, the 2031 range and flexibility: how endowments and foundations do it (FR, some IPS)

**Q12. Yale sets each year's spending from the endowment's value "from two years ago", so budgets are known in
advance. Should the 2031 range be framed as a Yale-style lagged rule: known in 2031, applied in 2033, part locked, part
smoothed? And would naming the precedent help co-sponsors trust it?**
- Anchors: R-C62, R-AN7, R-C67, R-C69.
- Official words: "Laura plans to begin approaching potential co-sponsors in 2031, two years before the residency is
  established." (case p.3, VRF)
- Hypothesis (guess):
  - Yale Provost page (VP): "we apply the targeted spending rate (5.25%) to the endowment’s year-end value from two
    years ago. Then we take 20% of that amount and add it to 80% of the total amount spent in the most recent fiscal
    year."
  - The two-year lag is a deliberate predictability device. The 2031 floor bought in a 2-year Treasury is the same
    idea, taken further (fully locked).
  - Likely use: one FR line citing the precedent. Maybe a rule design where the stretch is a stated share of the
    unlocked sleeve.
- Would change: **decision** (range rule design). **Sentence** (FR, co-sponsor section).
- Deliverables: FR. Specialist: D5, D8. Seed: 8.
- North star: co-sponsors hear a method used by a famous endowment, not a hope.

**Q13. Does the case's word "responsibly" track the legal prudence standard for endowment spending (UPMIFA)?** Its
seven spending factors include "general economic conditions", "effect of inflation or deflation", "expected total
return" and "other resources", almost the case's assumption list. Should the team define "responsible facility
contribution" against those factors?
- Anchors: R-AN18, R-C85, R-C60, R-C84.
- Official words: "Teams should identify and explain their assumptions about investment performance, the timing of
  cash flows, outside funding, the effect of inflation on portfolio projections and facility costs, and the financial
  flexibility Laura should preserve." (case p.4, VRF)
- Hypothesis (guess):
  - NACUBO's UPMIFA summary (VP) lists: "1) duration and preservation of the endowment fund; 2) the purposes of the
    institution and the endowment fund; 3) general economic conditions; 4) effect of inflation or deflation; 5) the
    expected total return from income and the appreciation of investments; 6) other resources of the institution;
    and, 7) the investment policy of the institution."
  - The overlap with R-C85 is close (INT: probably not deliberate, but a ready-made checklist).
  - A definition built from these factors is defensible and short: "responsible = protects the reserve, allows for
    inflation, relies on stated returns, keeps other resources".
- Would change: **sentence** (FR definition of "responsible"; maybe an IPS clause).
- Deliverables: FR, IPS. Specialist: D8, D5. Seed: 28.
- North star: turns an undefined word into a standard that professionals and courts already use.

**Q14. Should Laura's 2031 message have two legally distinct parts: an unconditional floor (already bought) and a
conditional stretch (released only if the portfolio reaches a stated level)?** Under US nonprofit accounting (ASU
2018-08), the residency can book the first as a pledge now and the second only when its condition is met.
- Anchors: R-C69, R-AN9, BS-05 (A3: which verb for floor vs stretch), R-C66.
- Official words: "If Laura promises more than she can ultimately contribute, she could damage her credibility"
  (case p.3, VRF)
- Hypothesis (guess):
  - Yes. It gives the floor/stretch split a precise meaning that a co-sponsor's finance officer already uses.
  - ASU 2018-08 (SNIP, several CPA-firm summaries): a conditional contribution needs "a barrier" and "a right of
    return" or release, and is "recognized when the condition or conditions are substantially met".
  - Taiwan accounting differs, and Taiwan law is out of scope, so use the idea, not the standard's name, in the
    co-sponsor draft.
- Would change: **decision** (range structure). **Sentence** (FR fundraising draft checklist).
- Deliverables: FR. Specialist: D5 (with D10 for scope). Seed: 9.
- North star: co-sponsors can count her floor as real money, which is exactly what the case says a meaningful
  contribution should do.

**Q15. Does the case allow the facility contribution to be committed in 2033 but paid in stages against construction
milestones, as foundations pay capital grants?** If so, does staging raise the responsible amount (the undrawn money
earns Treasury yield and stays available for overruns) or change the 2031 range?
- Anchors: R-C57, R-C58, R-C63, R-AN19.
- Official words: "After establishing the operating reserve in 2033, Laura must decide how much of the remaining
  portfolio she can responsibly contribute toward the cost of establishing the residency facility." (case p.3, VRF)
- Hypothesis (guess):
  - The case fixes the decision in 2033, not the payment date. Staging looks allowed but is not stated (INT).
  - Milestone disbursement is standard grant practice (SNIP; not researched here).
  - If allowed, it lets "flexibility" be a mechanism (unpaid tranches) instead of a sized fund, which the case says
    teams need not size (R-C61).
  - Risk: it complicates the one-number story; the simplicity test may cut it to one FR sentence.
- Would change: **decision** (contribution timing assumption). **Sentence** (FR flexibility).
- Deliverables: FR. Specialist: D10 (case reading), D5. Seed: 11.
- North star: matches how a real building is paid for, which an entrepreneur would recognise at once.

**Q16. Should the growth sleeve lock part of the facility floor whenever it crosses pre-set levels between 2028 and
2031, the way pension plans de-risk on funded-status triggers, instead of locking only in 2031?** How would that change
the 2031 floor distribution (p5/p50) and the chance the 2033 contribution lands inside the stated range?
- Anchors: F-402 (2031 floor p5/p50/p95 $127k/$165k/$217k), R-C67 to R-C71, R-C70.
- Official words: "They should explain how favorable and unfavorable market outcomes could affect the amount she can
  provide." (case p.3, VRF)
- Hypothesis (guess):
  - Ratcheting lifts the p5 floor and cuts the median slightly. It is "lock in good years", the practitioner answer to
    "what if 2029 is great and 2030 crashes?".
  - Not yet modelled. The council's ratchet was for the liability hedge, not the facility floor.
  - It may fail the simplicity test if the gain is under ~$5-10k at p5.
- Would change: **number** (2031 floor p5/p50; confidence of landing within the range). **Decision** (keep one 2031
  lock, or ratchet).
- Deliverables: FR (IPS sentence only if adopted). Specialist: D3. Seed: 9.
- North star: shows the plan protects Laura's good luck as well as her promise.

**Q17. Should "financial flexibility" after 2033 be written as a draw rule on the leftover money, not as a dollar
size?** For example: released first for facility overruns, then capped at X% a year or smoothed, endowment-style
(Yale's 4.0-6.5% band, UPMIFA's 7% presumption).
- Anchors: R-C58, R-C61, R-AN19, R-C84.
- Official words: "Teams are not expected to determine the size or investment composition of a separate contingency
  fund or endowment." (case p.3, VRF)
- Hypothesis (guess):
  - A rule satisfies "preserve flexibility" without sizing a fund.
  - NACUBO (VP): UPMIFA's optional "rebuttable presumption of imprudence if an institution expends an amount greater
    than seven percent of fair market value of a fund, calculated in an averaging formula over three years".
  - Yale's 4.0%/6.5% band is SNIP (a search snippet of the Yale page; the Provost page I read gives only the 5.25%
    rate).
  - Likely one FR sentence.
- Would change: **decision** (how flexibility is expressed). **Sentence** (FR).
- Deliverables: FR. Specialist: D5, D8. Seed: 7, 11.
- North star: gives Laura room to adapt "as the project develops" with a guard rail she can explain to partners.

### C. Governance, behaviour and reporting (IPS, FR, TN, WInS-now)

**Q18. Which governance elements from professional IPS templates must the 500-word IPS carry, and which can be
cut?** Candidate elements: who decides and who monitors; dated review points (2028 deposit, 2031, 2033); event
triggers (funded ratio below 100%, deposit short or late, residency delayed); a rebalancing process. The UK requires
pension investment statements to be reviewed "at least every three years" and "without delay after any significant
change".
- Anchors: R-I3, R-C89, X-23, R-AN4, BS-08.
- Official words: "It helps investors stay focused on long-term objectives and make disciplined decisions during
  changing market conditions." (IPS p.1, VRF)
- Hypothesis (guess):
  - CFA Institute, Elements of an IPS for Individual Investors (2010, VP): "2b. Describe the process for reviewing and
    updating the IPS." and "4c. Define the process for rebalancing portfolios to target allocations."
  - UK Occupational Pension Schemes (Investment) Regulations 2005 reg 2 (VP): review "(a)at least every three years;
    and (b)without delay after any significant change in investment policy."
  - The IPS probably needs just three governance lines: event-based review triggers, one rebalancing rule, and "the
    team recommends; the portfolio manager signs off; students decide in WInS" (matching the real rules, R-W19).
- Would change: **decision** (which clauses get IPS words).
- Deliverables: IPS. Specialist: D10, D8. Seed: 2.
- North star: an IPS that still works when nobody from our firm is in the room is what a client hires.

**Q19. What would a private banker pre-commit to for a 2029 bear market? And does holding the reserve as individual
bonds (not bond funds) remove the biggest behaviour trap?** Morningstar 2025 finds bond-fund investors captured only
about half of their funds' returns.
- Anchors: R-I3, R-C36, R-C37.
- Official words: "Laura understands that investing involves uncertainty and periods of market volatility." (case p.2,
  VRF)
- Hypothesis (guess):
  - Morningstar Mind the Gap 2025 (VP): the average dollar earned "7.0% per year" vs funds' "8.2%", a "1.2 percentage
    point 'investor return gap'".
  - Same study: "taxable-bond and municipal-bond fund investors earned the smallest share of their funds’ aggregate
    total returns, capturing only about half".
  - Same study: allocation-fund investors captured "nearly 97%".
  - Vanguard 2022 (VP): behavioural coaching worth "0 to > 200" bps.
  - The pre-commitments would be: report the promise's funded status first; never move money between the hedge and
    the sleeve; rebalance the sleeve inside a band; hold the reserve as individual Treasuries so a bond-price fall is
    never a "loss" she can act on.
  - Morningstar also recommends "slightly haircutting projections" for this drag. That is a candidate FR assumption.
- Would change: **decision** (IPS behaviour rule). **Number** (a possible haircut on sleeve return assumptions).
  **Sentence** (FR).
- Deliverables: IPS, FR. Specialist: D6. Seed: 27.
- North star: Laura hires a firm for the bad year, and this shows we planned her bad year in advance.

**Q20. From the first WInS trade, should the team keep a weekly "hedge effectiveness" log?** It would record the
Treasury sleeve's value change against the change in the ten payments' present value (spot curve, about $289 per
basis point). A reflection could then say: "rates rose X bp, our bonds fell $Y, the promise's cost fell $Z, funded
status held".
- Anchors: R-T20, R-T9, F-103, F-105, R-W76, R-W82.
- Official words: "Your reflections should clearly explain how each decision supported, tested, or refined your
  overall investment strategy." (TN guide p.1, VRF)
- Hypothesis (guess):
  - Yes; this is the highest-value WInS-now item in this file.
  - Pension CIOs report funded status and hedge ratio, not return (NISA and JPM papers, VP, frame everything in funded
    status).
  - Treasury funds may lose money during WInS (the 10y is at its highest since 2007, F-004). Without the log, a note
    looks like a loss. With it, the same note is evidence the hedge worked.
  - Needs: the daily par curve (treasury.gov, reachable), the verified PV method (`official_curve_pv.py`), and WInS
    position values. D1/D3 can script it.
- Would change: **decision** (start the log now). **Sentence** (TN reflections; FR "how effectively it implemented
  that strategy", R-I37).
- Deliverables: WInS-now, TN, FR. Specialist: D1, D3. Seed: 30.
- North star: proves in six weeks, with real data, that the plan behaves as promised. Nobody can do that with a
  growth-first book.

**Q21. Should the Final Report report risk as "expected negative years out of 20", as Australian super funds must
(the Standard Risk Measure)?** It would also say why this label and volatility both misstate the reserve's risk: a
held-to-maturity ladder can show negative years while every payment stays certain.
- Anchors: R-S26, R-S28, R-C82.
- Official words: "uses reasonable assumptions and projections to evaluate funding reliability, the facility
  contribution, and financial flexibility under varying market outcomes" (criterion 3, VRF)
- Hypothesis (guess):
  - ART (VP): the SRM is "based on the number of expected years of negative annual returns over any 20-year period".
  - ASM arithmetic with JPM inputs (F-301, F-307, F-314; lognormal): 100% U.S. large cap ≈ 6.7 negative years in 20;
    the 60/40 sleeve ≈ 5.4; intermediate Treasuries ≈ 2.5.
  - SRM bands (1 = fewer than 0.5 years ... 7 = 6 or more) are SNIP; the guidance PDF refused access.
  - Useful as one plain-English line for Laura and co-sponsors. The contrast (a market-value measure vs payment
    certainty) is itself an insight about what "risk" means for her.
- Would change: **number** and **sentence** (FR uncertainty communication).
- Deliverables: FR. Specialist: D9, D3. Seed: 18.
- North star: reports uncertainty in words a non-investor understands, and shows why the usual risk number would
  mislead her.

**Q22. Australian law (the Retirement Income Covenant, 2022) makes super trustees "achieve and balance" three
objectives: maximise expected income, manage risks to its "sustainability and stability", and keep "flexible
access".** These are Laura's growth, funding certainty and flexibility. Should the IPS's central idea state a
priority order among the three (promise first, then flexibility, then growth), not a "balance"? And would naming the
covenant as the team's inspiration (in the Articulation section) earn its place?
- Anchors: R-I11, R-I26, R-C38, X-16.
- Official words: "How does your strategy balance growth, risk, liquidity, funding reliability, and financial
  flexibility?" (IPS p.1, VRF)
- Hypothesis (guess):
  - Treasury's explanatory memorandum (exposure draft 2021, VP): trustees must "assist beneficiaries to achieve and
    balance three objectives: maximizing their expected retirement income; managing expected risks to the
    sustainability and stability of their expected retirement income; and having flexible access to expected funds
    during retirement."
  - The enacted wording is not checked (AustLII 403); SNIP summaries match.
  - A strict order is stronger than a balance, because the case itself orders things (the reserve comes "before" the
    payment and the facility, R-AN2).
  - The covenant is a genuine, dated Australian parallel for the Final Report's story of how the team thought. Leave
    it out of the IPS.
- Would change: **sentence** (IPS central idea; FR Articulation).
- Deliverables: IPS, FR. Specialist: D8, D7. Seed: 28.
- North star: our home country's law on long promises supports Laura's order of priorities. That is an authentic
  team-voice detail no other team has.

**Q23. Chhabra's framework says "risk allocation should precede asset allocation" across personal, market and
aspirational risk. Is Laura's aspirational-risk bucket already full (her creative business, future books, the
residency itself)?** If so, should the portfolio hold only personal-risk assets (the reserve) and market-risk assets
(a broad sleeve), and refuse aspirational-style bets (themes, single stocks, country tilts)?
- Anchors: R-C37, R-AN16, R-C27, R-AN31.
- Official words: "Although she has been willing to take thoughtful risks throughout her entrepreneurial career"
  (case p.2, VRF)
- Hypothesis (guess):
  - Yes. This challenges the team notes' mapping of "flexibility = aspirational bucket".
  - Chhabra (2005, Journal of Wealth Management; SNIP abstract via search): personal, market and aspirational risk;
    "risk allocation should precede asset allocation".
  - Her entrepreneurial risk lives outside the portfolio, and her 2028 income depends on it. So the portfolio should
    not add more of the same kind of risk. This is the institutional mirror of the human-capital argument (B3 lens),
    stated in a framework a private-bank judge would recognise.
- Would change: **decision** (no thematic or Taiwan/AI tilts in WInS or the plan). **Sentence** (IPS principle).
- Deliverables: WInS-now, IPS, FR. Specialist: D6, D2. Seed: 17, 20.
- North star: "you already take the big bets in your life; our job is to make sure they never threaten your promise".
  That reads as her, not generic.

**Q24. Which named frameworks map to which part of the plan, and which (if any) should be named in the IPS?** Candidates:
liability-driven cash-flow matching (reserve), funded-status de-risking (timing), goals-based buckets (reserve /
sleeve), Yale-style lagged rules (2031 range), UPMIFA prudence (facility, flexibility).
- Anchors: R-S26 ("effective use of investment concepts and tools"), R-I23, R-S24.
- Official words: "Focus on the strategy and decision-making framework that guide your portfolio rather than describing
  individual investments or presenting detailed financial calculations." (IPS p.2, VRF)
- Hypothesis (guess):
  - The IPS names none of them and describes each in plain words. The council judge panel already warned against
    "LDI" and "defeasance" in the IPS.
  - The FR carries one mapping table (a chart-free visual) showing each rule's professional ancestor.
  - This shows "effective use of investment concepts" without jargon in the scored 500 words.
- Would change: **decision** (naming policy per deliverable). **Sentence**.
- Deliverables: IPS, FR. Specialist: D8, D9. Seed: 28.
- North star: judges see professional depth in the FR, while Laura reads an IPS in her own language.

**Q25. Would a pension CIO at least consider buying the promise from an insurer (a deferred 10-year period-certain
annuity, the "buyout" option)? And what one reason rejects it for Laura?** Candidate reasons: insurer credit risk
above Treasury risk; permitted-investment wording "for BOTH contributions"; no liquidity if the residency changes;
less transparency.
- Anchors: R-AN15, R-C74, R-C73.
- Official words: "Teams may reach different conclusions about risk, asset allocation, liquidity, return expectations,
  funding confidence, the facility contribution, and the financial flexibility Laura should preserve." (case p.4,
  VRF)
- Hypothesis (guess):
  - Rejected. The SMApply FAQ lists permitted investments "for BOTH contributions" (R-AN15; reading 1 = the list binds
    the plan). An annuity is not on it.
  - A Treasury ladder can be sold if the residency is delayed or changes (BS-07). An annuity usually cannot.
  - Worth one FR line under "alternatives considered". It pre-empts the obvious "why not just buy an annuity?".
- Would change: **sentence** (FR alternatives).
- Deliverables: FR. Specialist: D8, D10. Seed: 26.
- North star: shows the team chose Treasuries over a real alternative for Laura-specific reasons: flexibility, and
  certainty that does not depend on an insurer.

---

## 3. Evidence and arithmetic

### 3.1 Primary-source quotes used (all read 2026-09-27)
| # | Exact text | Source | Status |
|---|---|---|---|
| E1 | "For schemes with no cash balance benefits, the duration is 10 years." | TPR, Defined benefit funding code of practice, Nov 2024, "Significant maturity" para 22(a) | VP |
| E2 | "we expect schemes to target a minimum level of interest rate and inflation hedging of at least 90% on a low dependency funding basis." | same code, para 20 | VP |
| E3 | "dependent on their assessment of the employer covenant, where more risk can be allowed for where the scheme has access to sufficient employer cash flows and contingent assets to support this level of risk" | same code, journey planning para 29(a) | VP |
| E4 | "Low dependency investment allocation means the assets of a scheme are invested in such a way that the value of the assets relative to the value of the scheme’s liabilities is highly resilient to short-term adverse changes in market conditions so that further employer contributions are not expected to be required to make provision for the scheme’s liabilities." | SI 2024/462 reg 5 (legislation.gov.uk) | VP |
| E5 | "a ‘shortfall limit’ is the extent to which an RSE licensee considers that a fund can be in an unsatisfactory financial position with the RSE licensee still being able to reasonably expect that, because of corrections to temporary negative market fluctuations in the value of fund assets, the fund can be restored to a satisfactory financial position within one year." | APRA SPS 160 (APRA handbook) | VP |
| E6 | "within a time period that is reasonable in the circumstances of the fund but which must not exceed three years from the valuation date" | APRA SPS 160 | VP |
| E7 | "the Government won’t start any drawdowns from the Fund until at least 2032–33" / "the benchmark return rate will remain at between four and five per cent above CPI per annum over the long term" | Treasurer's media release "Future of the Future Fund" (date not shown in the captured text; search indicates late Nov 2024, SNIP) | VP (text) |
| E8 | "confidence level of 99,5 % over a one-year period." | Directive 2009/138/EC (Solvency II), EUR-Lex HTML | VP |
| E9 | "The Verification Agent is responsible for independently confirming that the investments purchased for the Escrow Fund will be sufficient to fund the Debt Service payments on the Refunded Bonds" | NABL, Bond Basics: Verification Agent | VP |
| E10 | "Once Bonds are legally defeased, they are generally considered no longer outstanding from the Issuer’s perspective." | NABL, Bond Basics: Defeasance | VP |
| E11 | "To determine the year’s spending, we apply the targeted spending rate (5.25%) to the endowment’s year-end value from two years ago. Then we take 20% of that amount and add it to 80% of the total amount spent in the most recent fiscal year." | Yale Office of the Provost FAQ | VP |
| E12 | "1) duration and preservation of the endowment fund; 2) the purposes of the institution and the endowment fund; 3) general economic conditions; 4) effect of inflation or deflation; 5) the expected total return from income and the appreciation of investments; 6) other resources of the institution; and, 7) the investment policy of the institution." | NACUBO, UPMIFA topic page | VP |
| E13 | "a rebuttable presumption of imprudence if an institution expends an amount greater than seven percent of fair market value of a fund, calculated in an averaging formula over three years." | NACUBO, UPMIFA topic page | VP |
| E14 | "Because the investment return assumption for most plans also serves as the discount rate used to determine the present value of the plan’s liabilities" ... "A rate set too high will understate liabilities" ... "the median return assumption declined from 8.0 percent to 7.0 percent. The median rate has remained at that level since FY 21" | NASRA Issue Brief, April 2026 | VP |
| E15 | "for plans that are greater than 95% funded[2], we see a compelling case to move to a hibernation portfolio – now." | NISA, "95% is the new 105%" (c. 2021) | VP |
| E16 | "Hibernation strategies will burn through capital over time, squandering hard-won pension funding gains." | J.P. Morgan AM, "Rethinking the pension plan endgame", Oct 2021 | VP |
| E17 | "That 1.2 percentage point 'investor return gap'" / "taxable-bond and municipal-bond fund investors earned the smallest share of their funds’ aggregate total returns, capturing only about half." / "slightly haircutting projections" | Morningstar, Mind the Gap 2025 (US) | VP |
| E18 | "Behavioral coaching ❹ 0 to > 200" (bps) | Vanguard, "Putting a value on your value: Quantifying Vanguard Advisor's Alpha" (2022) | VP |
| E19 | "2b. Describe the process for reviewing and updating the IPS." / "4c. Define the process for rebalancing portfolios to target allocations." | CFA Institute, Elements of an IPS for Individual Investors (2010) | VP |
| E20 | "(a)at least every three years; and (b)without delay after any significant change in investment policy." | UK SI 2005/3378 reg 2 | VP |
| E21 | "The Standard Risk Measure assigns a Risk Label from Very low to Very high, and a corresponding Risk Band from 1 to 7 for each option, based on the number of expected years of negative annual returns over any 20-year period." | Australian Retirement Trust, SRM page | VP (industry page, not regulator) |
| E22 | "assist beneficiaries to achieve and balance three objectives: maximizing their expected retirement income; managing expected risks to the sustainability and stability of their expected retirement income; and having flexible access to expected funds during retirement." | Treasury (Aus), Explanatory Memorandum, exposure draft, Sept 2021 | VP (exposure draft; enacted wording SNIP) |
| E23 | "“The higher the interest rates, the higher the advertised Grand Prize. ...,” says an FAQ on the website for the game." / "accrues interest from investments in U.S. Treasury bonds" | Marketplace, 2022-11-08 | VP (news page); Powerball FAQ wording SNIP |

### 3.2 Arithmetic (ASM; inputs verified)
- **Fee drag on the reserve (Q5).** Rung costs at 2027-01-01 (F-107) × years to payment (6..15): Σ = $2,933,301
  (implied Macaulay duration 10.04y). PV of a yearly fee f ≈ f × $2,933,301 (continuous approximation; the fee is
  charged on the market value, which grows at the curve).
  - f = 0.07% (a defined-maturity Treasury fund, F-207): $2,053
  - f = 0.15%: $4,400
  - f = 0.5%: $14,667
  - f = 1.0%: $29,333
  - Compare the headroom of $7,736 (F-104).
- **Discount-rate comparison (Q10).** PV at 2027-01-01 of 10 × $50k (2033-2042) at a flat 7%: $250,386; at 6.7%:
  $257,485; at 5.36% flat: $292,245 (≈ F-101 $292,264, as F-109 says). The 7% understatement vs the curve is
  $41,878 (14.3%).
- **SRM-style counts (Q21).** P(negative calendar-year return) × 20, lognormal:
  - U.S. large cap (6.70% compound, log sd 0.152 per F-316): P = 0.335 → 6.7 of 20.
  - Intermediate Treasuries (4.0%, 3.4%): P = 0.124 → 2.5.
  - 60/40 sleeve (arithmetic 6.39%, sd 9.97%, correlation -0.01): P = 0.269 → 5.4.
  - These are model properties, not forecasts.
- **Duration vs UK threshold (Q3).** Macaulay ≈ 10.04y at 2027 (above); modified 9.90y (F-103); spot 10.16y (F-105).
  The UK threshold is 10 years (E1), measured on its own funding basis, so the comparison is approximate.

---

## 4. Sources (all accessed 2026-09-27)
| Source | URL | Status |
|---|---|---|
| TPR DB funding code of practice (Nov 2024) | https://www.thepensionsregulator.gov.uk/-/media/thepensionsregulator/files/import/pdf/db-funding-code-of-practice.ashx | VP |
| UK SI 2024/462 reg 5 | https://www.legislation.gov.uk/uksi/2024/462/regulation/5/made | VP |
| UK SI 2005/3378 reg 2 (SIP review) | https://www.legislation.gov.uk/uksi/2005/3378/regulation/2 | VP |
| APRA SPS 160 Defined Benefit Matters | https://handbook.apra.gov.au/standard/sps-160 | VP |
| Retirement Income Covenant EM (exposure draft) | https://treasury.gov.au/sites/default/files/2021-09/c2021-209553-explan_memorandum.pdf | VP |
| Retirement Income Covenant enacted text (AustLII) | http://www6.austlii.edu.au/cgi-bin/viewdoc/au/legis/cth/num_act/ccivfaoma2022678/sch9.html | Refused (403) |
| Future Fund release (Treasurer) | https://ministers.treasury.gov.au/ministers/jim-chalmers-2022/media-releases/future-future-fund | VP |
| Future Fund (Wikipedia, background only) | https://en.wikipedia.org/wiki/Future_Fund | VP (secondary) |
| Future Fund Investment Mandate Direction 2024 explanatory statement | https://www.finance.gov.au/sites/default/files/2024-11/F2024L01477ES.pdf | Fetch returned almost no text; not verified |
| Solvency II Directive 2009/138/EC | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009L0138 | VP |
| NABL Verification Agent / Defeasance | https://www.nabl.org/bond-basics/verification-agent/ ; https://www.nabl.org/bond-basics/defeasance/ | VP |
| Yale Provost spending FAQ | https://provost.yale.edu/how-exactly-does-spending-policy-work | VP |
| NACUBO UPMIFA | https://www.nacubo.org/Topics/Endowment-Management/Uniform-Prudent-Management-of-Institutional-Funds-Act | VP |
| NASRA return assumptions brief (Apr 2026) | https://www.nasra.org/files/Issue%20Briefs/NASRAInvReturnAssumptBrief.pdf | VP |
| NISA "95% is the new 105%" | https://www.nisa.com/perspectives/95-is-the-new-105-why-plans-should-consider-accelerating-their-glidepath/ | VP |
| JPM "Rethinking the pension plan endgame" (Oct 2021) | https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/institutional/insights/portfolio-insights/portfolio-strategy/Rethinking-the-pension-plan-endgame.pdf | VP |
| Morningstar Mind the Gap 2025 | https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/blt2c5c4d9171638c42/689b424311f3880edc4b4813/US_Mind_the_Gap_2025.pdf | VP |
| Vanguard Advisor's Alpha 2022 | https://www.vanguardsouthamerica.com/content/dam/intl/americas/documents/latam/en/2022/08/mx-sa-2335954-putting-a-value-on-your-value-quantifying-vanguard-advisors-alpha.pdf | VP |
| CFA Institute IPS elements (individual) | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf | VP |
| CFA Institute IPS elements (institutional) | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-institutional-investors.pdf | SNIP (not opened) |
| ART Standard Risk Measure | https://www.australianretirementtrust.com.au/disclaimers-and-disclosures/standard-risk-measure | VP |
| FSC-ASFA SRM guidance 2011 | https://www.superannuation.asn.au/wp-content/uploads/2023/09/FSC-ASFA_StandardRiskMeasures_July2011.pdf | Refused (403) |
| Marketplace on Powerball and Treasuries (2022-11-08) | https://www.marketplace.org/story/2022/11/08/why-high-interest-rates-are-partly-responsible-for-the-2-04-powerball-jackpot | VP |
| ASU 2018-08 summaries (CPA Journal, JMCO) | https://www.cpajournal.com/2019/05/10/fasbs-new-guidance-for-contributions-received-and-contributions-made/ ; https://www.jmco.com/articles/nonprofit/conditional-contributions-asu-2018-08/ | SNIP |
| Chhabra, Beyond Markowitz (2005) | https://www.ssrn.com/abstract=925138 | SNIP (SSRN blocked) |
| Planner "confidence zone" 75-90% | search results (T. Rowe Price, MoneyGuidePro manuals) | SNIP |
| Pension glide-path guides (Russell, Cambridge Associates, BlackRock) | https://russellinvestments.com/-/media/files/us/insights/institutions/defined-benefit/pension-de-risking-glide-paths.pdf ; https://www.cambridgeassociates.com/insight/liability-hedging-handbook-a-guide-to-best-practices-for-us-pension-plans/ | SNIP (not opened) |

---

## 5. Leads for the specialists

- **D1 / D3 (rates, quant): Q20 hedge-effectiveness log.** Inputs: the daily par curve CSV (home.treasury.gov,
  reachable), the method in `research/verified_2026-09-27/official_curve_pv.py`, and WInS position values. Output: a
  weekly table of Δ(Treasury sleeve value), Δ(PV of the ten payments, spot, $289/bp now) and the funded ratio. Start
  with the first trade date.
- **D3: Q5 fee drag.** Replace my continuous approximation with year-by-year fees on the forward value path
  (F-106 values). Report net-of-fee funded ratios for 0.07/0.15/0.5/1.0%.
- **D3: Q16.** Add funded-status triggers to the sleeve in `strategy_mc.py`: lock X% of the sleeve into Treasuries
  maturing Jan 2033 whenever the sleeve exceeds pre-set levels, 2028-2031. Compare the 2031 floor p5/p50 and
  P(2033 contribution within the range) with the single 2031 lock (F-402).
- **D8: Q2/Q3.** The TPR code's "Significant maturity" and "Low dependency investment allocation" modules are the
  cleanest outside benchmark. Paragraph numbers: 17-22 (LDIA; hedging "at least 90%") and 22(a) of the maturity
  module (10 years). The "up to 15% growth assets" figure is only in a search snippet (Gateley summary of the
  consultation); verify it in TPR's "Regulatory approach" document before use.
- **D8 / D1: Q6.** SPS 160 paragraphs on "Shortfall limit" and "Unsatisfactory financial position" (APRA handbook).
  SPG 160 (the practice guide PDF on apra.gov.au) gives worked shortfall-limit examples; not read.
- **D8: Q7.** NABL bond-basics pages (reachable). If a real escrow verification report is wanted as a template, the
  City of Austin 2021 escrow agreement came up in search (services.austintexas.gov); not opened.
- **D5: Q12/Q14/Q17.** Yale Provost FAQ (VP). The Yale slide deck "Introduction to the Endowment Spending Policy"
  (your.yale.edu, Nov 2024) holds the 4.0%/6.5% band; not opened. NACUBO UPMIFA page (VP). For ASU 2018-08, read the
  FASB standard or a Big-4 guide before quoting.
- **D6: Q19.** Morningstar Mind the Gap 2025 PDF (VP): the investment-style section has the bond-fund "about half"
  finding. Vanguard 2022 Advisor's Alpha PDF (VP): the behavioural coaching section cites Bennyhoff (2018).
- **D9: Q21.** ART page (VP) for the SRM definition. The band thresholds need the FSC-ASFA 2011 guidance (403 here);
  try an APRA or fund PDS copy.
- **D7: Q4/Q22.** Wharton's own TN example (R-T23 to R-T25) implies a calendar glide path. Check whether past Wharton
  cases or guides used "glide path" wording, to judge whether the designers expect it.
- **D10: Q15/Q25.** Case reading on staged facility payments (R-C57, R-C63). The "for BOTH contributions" FAQ line
  (R-AN15) decides whether an insurer annuity is even in scope.
- **Blocked:** the Future Fund site and AustLII refuse (403). The Treasurer's release and the Treasury EM are good
  substitutes.

---

## What this teaches

- Institutions that owe fixed amounts ask two questions before choosing investments: "Is the promise already paid
  for at market prices?" and "Who pays if we fall short?" When the answer to the second is "nobody", as for Laura,
  professionals hedge, and they take risk only with the surplus.
- The same idea shows up under many names: pensions ("low dependency", "hibernation"), insurers ("99.5% over one
  year"), municipal finance ("defeasance" with a "verification agent"), endowments ("spending rules") and Australian
  super ("shortfall limit", "restoration plan", the three-way "balance"). Recognising one idea in five disguises is
  what makes a framework feel familiar to a judge.
- Small costs matter most when the margin is small: a fee that looks tiny (0.15%) can eat more than half of a thin
  safety buffer over ten years.
- How you measure risk changes what you see. A bond held to maturity can "lose money" on paper in a year while its
  payment stays exactly as promised.
