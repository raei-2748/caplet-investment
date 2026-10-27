# R07 FUSIONS: six synergies, the logic arsenal, the rejections, the conflicts, the tests

> **Corrections (Felix, huddle H-003, 27 Oct night):** "as much bound by their contracts as are individuals" is Chief
> Justice Waite's line in the Sinking-Fund Cases (1879), quoted in Perry (1935): cite "Perry, quoting the Sinking-Fund
> Cases". Treasury terms were "rewritten" once (1933), not "broken"; some bill redemptions were paid late in 1979.
> Goetzmann-Jorion measure real price appreciation, not total returns. Lab results for the tests below:
> `../../lab/K07_memo.md`.

> AI-generated research (Claude Code, rung-3 synthesis, Tue 27 Oct 2026). Not for submission. Keel recommends,
> Caplet decides. No IPS prose. Scouts = `scouts/S1`-`S6`; "C" = in `COVERED.md`. Numbers are quoted with their
> source; anything new is a TEST for Jun.

**The finding.** Six fields, one discipline: *sort every dollar by what can fail it, and decide in advance who pays
when it does.* V25 does this by instinct. A and B would change the plan; C-F change the argument.

---

## 1. The synergies

### A. One storm, three holes (common-cause failure × human capital)
- **Parts.** The nuclear single-failure rule, "multiple failures resulting from a single occurrence are considered to
  be a single failure", and Swiss cheese (S6 #2). Human capital, the huddle's 0-of-36 line (C R02 27). Japan's
  negative spread, which shows the coupon gap at full scale (S1 #1). Goldratt's pooled buffer, which saves nothing by
  the square root when risks share a cause (S6 #3).
- **Mechanism.** Laura has four defences: the 2027 headroom, the 2028 deposit, the 2033 re-match and her kept half of
  VT. A disinflationary slump (2008-style) can breach them together. Falling yields make the ladder dearer and widen
  the coupon gap. Her advances and speaking income can shrink. Stocks fall, so the half that covers the gap is
  smallest when the gap is largest. Even the independent model shows the link: the coupon-gap risk climbs from 2% to
  7.5% as the deposit falls from $150k to $50k (Model Suite M5). A 2022-style slump (yields up) *closes* the coupon
  hole.
- **What it changes.** *The argument:* "high degree of certainty" is a claim about independence. Counting layers
  proves nothing; naming the one shared cause does. V25 already half-names it ("the same slump that makes bonds
  dearer"). *The plan, if T1-T2 agree:* the January 2028 deposit shows which storm Laura is in. Price the coupon
  hold-back at that day's yields and buy it in a Treasury before the floor and VT, instead of relying on her VT half
  in 2033.
- **Critique.** The case never measures how her income moves with markets (huddle: "can shrink", never "moves with
  stocks"); the house model makes stocks and yields independent (A09). It fails if T1 finds the joint hole small.
- **Device.** Fukushima Daiichi: 10 of 13 generator cooling systems were in one flooded basement. The single
  air-cooled generator kept running. Diversity worked where numbers did not.
- **Lands in.** IPS (the defences fail for different reasons, except one, which we name) and the Final Report
  (common-cause table). *Portfolio Analysis*; *Client Knowledge*.

### B. Copy what can be copied; reserve the rest early, on a date (Solvency II × Germany × Leibowitz)
- **Parts.** Solvency II Art. 77(4): a cash flow that "can be replicated reliably" is valued at the cost of the copy,
  and the rest carries a margin (S1 #6). Germany's Zinszusatzreserve: the reserve is built when an old promise first
  rises above the reference rate (S1 #4). Equitable Life's option, sold with no price on it (S1 #2). Contingent
  immunisation run backwards, with a calendar trigger in place of a level trigger (S4 #4). One test, three dates
  (C R06 D2).
- **Mechanism.** The ten payments and the floor can be copied with Treasuries, so they are bought, and 1.00x cover
  is enough. The coupons, the stock top and the deposit cannot be copied. Each gets a reserve, set by rule, as soon
  as its gap can be measured. The switches are dated, which avoids the gap risk that broke CPPI in 1987.
- **What it changes.** The bottom of the range now deducts a fixed $3,700 for the coupon gap (Model Suite A14). The
  German rule would **re-measure the gap in January 2031** at that day's yields and deduct it before the range is
  named, so the 2033 re-match becomes a true-up (T3). It also answers "why is the cushion so thin?" (headroom $1,139,
  3.8bp, A01): the copied part needs no cushion, and the reserve belongs to the part that cannot be copied.
- **Critique.** It adds a date, which strains V25's "after that it changes itself". Article 18's "future premium
  counts as zero" does **not** hold for Laura (Conflict 1).
- **Device.** Equitable followed to its end: free option, 1957-88; no reserve, 1993; the Lords rule against it, July
  2000; doors closed, December 2000.
- **Lands in.** IPS: the principle under D2's framework, "bought where it can be, reserved where it can't". The
  Final Report carries the rest. *Investment Strategy* (disciplined planning); *Portfolio Analysis*.

### C. Two numbers, two standards of proof (Brady × project finance × Perry × Wald)
- **Parts.** Brady bonds: principal locked in Treasury zeros, the rest priced on its own, the "stripped yield"
  (S2 #1). Project-finance sizing: lenders size on P50 and P99 and lend the lower (S2 #4). Perry v. US: "as much
  bound by their contracts as are individuals" (S2 #3, S6 #4). Survivorship: US real price appreciation (Goetzmann-Jorion; the 4.73% figure is from the NBER Digest, UNVERIFIED) against a median
  of about 1.5% elsewhere (S4 #1). The newsvendor (C R05 13).
- **Mechanism.** The range's bottom rests on a contract. The only Treasury term ever rewritten was a gold clause (1933; payments were also briefly late in April-May 1979, Felix, H-003), and
  Laura's bonds have none. The top rests on a return distribution: it is the plan's *only* history-dependent number.
  So the bottom must hold in the bad case, and the top only in the expected one.
- **What it changes.** It labels what each 2031 number rests on. It also bars the Model Suite's history-world top
  odds (84%, 5:1, M6) from quotation, because they come from US Shiller data (A07), the survivor market. Quote the
  house and storm worlds instead, with a haircut (T4).
- **Critique.** Brady used zeros (STRIPS are banned), so Laura's coupon bonds bring back the reinvestment risk the
  vault removed: a likeness of structure, not a copy. In Perry the holder won the point and recovered nothing.
- **Device.** "Who is allowed to be wrong?" The bank, never; the sponsor, in the good case. The cheques are the
  bank's, and the gift is the sponsor's.
- **Lands in.** IPS: the floor needs no history; only the top does. Final Report: Brady and Perry boxes. *Portfolio
  Analysis*; *Creativity and Presentation* (uncertainty told credibly).

### D. Laura gets one plane (ergodicity × Allais × refutation science)
- **Parts.** Peters' coin, plus gambler's ruin (S4 #2). The Allais certainty effect, turned on its head (S4 #3).
  Certainty priced like for like (C R06 D4). The O'Keefe and Allen meta-analyses: an argument that refutes the other
  side beats a one-sided one, and an unanswered objection loses to both (S5 #1). The pratfall effect, as a limit on
  style (S5 #2).
- **Mechanism.** Laura's wealth multiplies, but it pays out fixed sums, so the average across paths hides ruin.
  Allais subjects pay a large expected-value price for certainty. Laura pays about nothing at the median ($193k
  against $119-152k for rivals given the cushion they need, R06 D4). Her real price is the best years: about $170k at
  the 95th percentile (huddle).
- **What it changes.** The argument only: it confirms V25's sceptic paragraph (one strongest objection, answered with
  its price; one concession). "The price is the best years" goes to the Final Report.
- **Critique.** Peters is contested (Doctor-Wakker-Wang 2020), and the meta-analyses are second-hand reports. Cite
  Peters with his critics, or not at all.
- **Device.** Model Suite M8, starting January 1923: stocks return about 7% a year for 15 years and beat bonds, yet
  a 60/40 pot still bounces the 1937 and 1938 cheques.
- **Lands in.** IPS (it backs the existing sceptic paragraph) and the Final Report. *Portfolio Analysis*;
  *Creativity*.

### E. The lead gift is load-bearing (fundraising pyramids × the hui × Varian)
- **Parts.** The gift-range chart: the lead gift is 10-20% of the goal and every tier below is sized from it
  (S3 #1). Taiwan's Civil Code Art. 709-7/709-9: the hui organiser is liable for unpaid contributions (S3 #5). Varian
  (1994): a sequential leader can *lower* total giving (S5 #3). Bagnoli-Lipman's refund rule (S5 #4). The newsvendor
  and matching gifts (C R05 13, 18).
- **Mechanism.** The pyramid gives the 3x over-promising penalty a mechanism: a short lead gift shrinks every tier
  below it. Varian pulls the other way: a big headline says "she has it covered". The hui supplies the question a
  Taiwanese co-sponsor will ask: "who stands behind the last payment?" Together: the *owned* bottom is the lead
  commitment, and the top is conditional, matched and refundable to Laura.
- **What it changes.** The 2031 framing: name the bottom as the commitment, and present the top by the gap it leaves
  for others. It also tests the 3x: if the pyramid multiplier is 5-10x, the fractile falls from 25% to 9-17% and the
  top should sit lower (T6).
- **Critique.** The case never says Laura is the lead donor or what the facility costs. The percentages are
  consultants' rules of thumb. Varian assumes no warm glow. It collides with V25 (Conflict 3).
- **Device.** A hui whose organiser is the US Treasury: no 倒會 (collapse) on the owned part. The stocks are where an
  organiser *could* come up short, which is why they are never promised.
- **Lands in.** Final Report (co-sponsor text; Bible rule 8 keeps the range out of the IPS). *Client Knowledge*;
  *Creativity and Presentation*.

### F. Announced money is a vault; unannounced money is a standby, called last
- **Parts.** The overrun facility, "callable only after contingency is fully used", with the sponsor's capped promise
  last (S2 #5). Studebaker 1963: when the pot was short, seniority decided who was paid (S6 #1). The cliff edges that
  undid the Dutch funding zones (S1 #3). Cohen: a world fund answers one firm's bad year, and only a floor answers
  everyone's (S6 #5). The cap as a call spread (C R06 D5).
- **Mechanism.** Every dollar has a place in a queue drawn before any shortfall: the cheques (bought), the bottom
  (owned), the top (locked in 2031), then Laura's half. Her half is a standby, called last, for overruns and the
  Taiwan dollar. Gains above the cap join the standby: a share, with no cliff.
- **What it changes.** It fixes V25's overclaim that the kept half is "the project's second cheque". The half covers
  a full inflation top-up in only about 5% of worlds (21% at 2% inflation, M4). It also says Laura's gift is a capped
  contribution, not a completion guarantee. Flexibility gets the *role* the panel found missing.
- **Critique.** It overlaps huddle item 6 and L-10's hold-back; only the overrun template and Studebaker are new.
- **Device.** Studebaker: about 3,600 retirees paid in full, about 4,000 workers paid about 15%, thousands under 40
  paid nothing. Laura sets the order before the pot exists. The mechanism needs a second source.
- **Lands in.** IPS (flexibility's role) and the Final Report. *Client Knowledge*; *Investment Strategy*.

---

## 2. The logic arsenal
The devices under A-F (Fukushima, Equitable, "who is allowed to be wrong?", 1923, the Treasury hui, Studebaker)
count too; they are not repeated here.
1. **Peters' coin, +50%/-40%** (S4 #2). The average gains, the typical path loses. Proves fixed dollars out need a
   ladder (V25's sceptic paragraph).
2. **Wald's missing planes** (S4 #1). He modelled the planes that never came back. Proves only the top rests on
   history.
3. **The 1989 twin** (S2 #1). Lock what must not fail in dated Treasuries; price the rest on its own. Proves the
   protected-note thesis at national scale.
4. **"Which clause broke in 1933, and does Laura's bond have one?"** (S2 #3). Proves near-ironclad is about the
   contract; the court named the residual risk (buying power), which sits on the facility side.
5. **Ricardo on Pitt's fund**: "No sinking fund can be efficient ... if it be not derived from the excess" (S2 #2).
   Proves the cheques are bought, not saved for; *tests* the 2027 gap (Conflict 1).
6. **Japan's negative spread, whole book against coupons only** (S1 #1). Sizes the one soft spot.
7. **Orange County, Dec 1994** (S6 #6). Liquidation locked in $1.6bn; rates fell about 2.5pt soon after. Proves why
   each holding matures before its January.
8. **The pyramid chain** (S3 #1). A short lead gift shrinks every tier below it. Tests the 3x.

## 3. Seems relevant, isn't
- **Deferred income annuities** (S1 #7): with no mortality pool, an annuity is a ladder plus a margin.
- **The Lundberg ruin model** (S1 #5): it needs random claims, and Laura's are known to the dollar.
- **Tobin's perpetual rule** (S3 #3): Laura's plan spends down by design.
- **Debt sculpting and the debt service reserve account** (S2 #8): her payments are flat and bought, with no revenue
  to disrupt.
- **k-out-of-n redundancy** (S6): the ladder is 10-out-of-10, so the rungs are not spares.
- **Rolldown** (S4 #6): held to maturity, it is already in the purchase yield.
- **Bayesian persuasion as a tool** (S5 #6): it pools good and bad states, the opposite of "credibly".
- **Kreps-Wilson reputation** (S5): it needs many rounds, and Laura names one range.

## 4. Conflicts (adversarial)
1. **"No payment waits on money not yet earned" is false as stated** (S6 #1). So are its relatives: S1 #6, "bought
   from the 2027 money alone" and "would hold if the 2028 deposit never arrived"; and S2 #2. The ladder costs more
   than $300k in 47% of paths, with a median gap of $9.8k when short, filled by the 2028 deposit (R06 K2). The 2033
   coupon gap leans on the VT half, which only the deposit buys. The honest claim: the deposit's *first* dollar goes
   to the cheques. A cheque breaks only if yields fall about 2pt *and* the deposit falls by more than about 56% (M3),
   and with a coverage rule the cheques survive a deposit as small as about $40k (M5).
2. **Which cheque waits.** Buying longest-dated first leaves the **2033** rung short, not 2041-42 as S6 #1 assumes.
   That is defensible (it is filled five years early, and the long rungs are the rate-sensitive ones), but it must
   be stated correctly (T8).
3. **V25's "too low and co-sponsors shrug" against Varian** (E): a high headline can *cut* others' giving, so
   under-promising may cost less than V25 implies.
4. **The 3x, "three in four" and the lock do not agree.** Under the lock the top is reached 87-93% of the time (R10;
   R06 D3). That implies over-promising is judged about 7-13x worse, not 3x. V25's line "whenever stocks are no lower
   in 2033 than in 2031 – about three times in four" becomes untrue under the lock. This is S4 #7's Dutch-book audit,
   caught live. Restate the ratio or re-size the top (T5).
5. **Rule risk.** V25 uses "Treasury bills" for the 2033 set-aside, but direct T-bills are out (huddle item 4). Every
   hold-back in A or B must be a Treasury bond or a WInS Treasury ETF.
6. **Crowd and guardrails.** The lock as a Stackelberg commitment (S5 #3) is still the crowd's move (9 of 12 raw-AI
   rivals). "Two pots" (S4) and "three tiers" (S5) break the no-pots guardrail. Cohen's seeds are too close to roots.
7. **Stale cover.** "102%" and "1.006x" (S1 #3, S2 #4) use the 16 Oct curve; on 22 Oct the cover was 1.004x (A01).

## 5. Tests for Jun (lab model = `ips_numbers.py` patched by `../../lab/K_overnight.py`; Suite = `keel/models/`)
1. **Joint storm (A).** Set `deposit28 = 150k × f`, with f falling with the 2027 stock return and the yield change to
   Jan 2028. Run rho 0 / 0.5 / 0.8, plus a fixed 2008 replay (yields -1.9pt, stocks -40%, deposit -50%). Report:
   P(cheque short by more than $1k), P(gift below the bottom), P(coupon gap > kept half) (base 7.7%).
2. **Jan 2028 hold-back (A).** Price the projected 2033 coupon gap at Jan 2028 yields, plus $7,500, and buy it in
   IBTM or a Dec-2032 Treasury before the floor and VT. Compare with rule G (`R10_lock_cushion.py`) on misses,
   median gift, bottom and the top's odds.
3. **Re-measure in Jan 2031 (B).** Replace A14's fixed $3,700 with the gap re-projected at Jan 2031 yields. Report:
   share inside the range, range width, cheques short.
4. **Survivorship haircut (C, D).** Re-run M6's top odds and M7's rival miss rates in the house and storm worlds at
   7.5% less 0.6pt and less 2.0pt. List every history-world figure that relies on US-only data (A07).
5. **Implied ratio under the lock (Conflict 4).** For V25 and the champion, compute P(top) and k = P/(1-P). Find the
   VT share in the top that restores about 75% under the lock.
6. **Pyramid sensitivity (E).** Newsvendor tops at k = 3, 5 and 10 (fractiles 25%, 17%, 9%) in the house and storm
   worlds: the dollars of top given up.
7. **Deposit × yields grid (Conflict 1).** Deposit $0 / 10k / 25k / 40k / 65k / 150k against a yield move of 0 /
   -1 / -2pt by Jan 2027, with and without the coverage rule. Find the smallest deposit with no cheque more than $1k
   short.
8. **The short rung (Conflict 2).** Under longest-first, which rung is short in Jan 2027, its median size, and the
   extra cost of buying it in Jan 2028.
9. **Two standards (C).** In the house, storm and bootstrap worlds, compare the contribution's 1st percentile with
   V25's bottom and its median with V25's top. Does the lower-of-two-tests rule ever bind?
10. **Which slump (A).** Bootstrap world: split paths by the sign of the 2027-33 stock-yield co-movement, and report
    the coupon gap and the kept half for each group.
