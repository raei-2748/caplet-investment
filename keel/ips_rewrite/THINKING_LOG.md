# Thinking log (IPS rewrite, the slow road)

AI-generated (Claude Code). One entry per day, Mon 26 Oct to Thu 29 Oct (Sydney): what was read, what was thought,
what was kept and what was killed. No drafting until Fri 30 Oct. Drafts D1-D4 are sketches, not candidates.

## Mon 26 Oct, night: reset, and what the sketches taught us

**Why the reset.** Ray (26 Oct): "THINK. That's your job. I don't want you to be hasty." Four drafts in one evening
polished one idea (the home-made capital-protected note) instead of finding the best one. The bibles are equal:
voice, motif, the extraordinary, investing knowledge, plus the refinements (subtle motif, human writing, no hedging,
judges are judges, not mini-Lauras).

**What the sketches did teach (kept as evidence, not text):**
1. Mock judges scored D2 at 35/50 and 33/50. Both found the strategy clear, and neither found a moment that made them
   stop. So the plan was not missing clarity; it was missing an aha a judge would repeat to another judge.
2. The concepts in R02 (60 of them) are mostly the standard canon (cash-flow matching, immunisation, safety-first,
   signalling). Using them correctly makes us competent. It does not make us extraordinary. What would: a concept
   used where nobody else thinks to use it, or a connection between two fields that turns out to be exact, not loose.
3. Ray's TNA averages 27 words a sentence; our sketches averaged 13 with many fragments. Short and choppy is an AI
   tell too.

**Thinking tonight: candidate ahas to test (none adopted yet).**
- **A1. Certainty, defined by the bond market's own test.** When a city sets aside Treasuries that mature in time to
  pay a debt, the market treats the debt as already paid ("defeased"; such bonds are usually rated AAA). Laura's ten
  payments are defeased in 2027-28, years before 2033. That turns "a high degree of certainty" from our opinion into
  a standard someone else already uses. (R02 has defeasance as concept 11, but as a label, not as the definition of
  certainty.) Test: is "escrowed to maturity = AAA" true and current? Is the iBond part allowed in that claim?
- **A2. The bottom of the range needs no model.** The 2031 range quotes a confidence. But the floor is bought, so it
  needs no forecast at all; only the top depends on a model. So the confidence figure attaches to one end only, and a
  co-sponsor can check the bottom themselves. That's a sharper reading of the case's "credible range + confidence".
  Test: is it true once the coupon gap is drawn from Laura's half first?
- **A3. The freeze is a feature.** Wharton forbids changing the strategy after 6 Nov. Economists call a rule you
  can't break a commitment device (rules beat discretion when your future self will be tempted). Our plan already
  trades nothing from 2028 to 2033, so the freeze costs us nothing, while it binds teams whose plans rely on judgment
  calls later. Risk: too meta for the IPS? Maybe a Final Report line.
- **A4. Every product a bank would sell Laura, we build from parts.** The ladder is a ten-year annuity-certain; the
  floor + stocks is a capital-protected note; the iBond funds are target-date funds in bond form. We unbundle all
  three and skip three sets of fees and one bank's credit risk. Motif link: a compounding pharmacist mixes one
  patient's prescription from raw ingredients instead of selling a branded pill, and "compounding" is also the
  investor's word. Test: is the pun too cute for Ray's taste? Is "annuity-certain" accurate (yes if the ten payments
  are fixed and certain; check the term)?
- **A5. Extended release is an exact fit, not a loose one.** An extended-release tablet aims for zero-order release,
  the same amount per hour, which is what ten equal cheques are. Immediate release is a lump sum; dose dumping is
  selling early. Pharmacists also measure a tablet's "mean dissolution time", the average time a dose stays in the
  tablet, and that is the same formula as a bond's Macaulay duration without the discounting. If that holds, "XR"
  isn't decoration: the duration match is literally an extended-release profile. Test: verify mean dissolution time
  and zero-order release; check the maths.

**Open questions for the next days.** Which of A1-A5 survives a sceptic? Which is about investing rather than
wordplay (north star 4 over north star 2)? Is there an aha in the case itself we keep missing (Laura's statistics
degree; her books; the Taiwan-dollar cost of the residency; the 2031 timing)?

**Started tonight.** Three background workers: a fact-check of A1-A5 plus the old queue (Lehman notes, Bodie, the
7.5% basis, iBond liquidation) -> `research/R04_fact_checks.md`; the ladder's Sonnet rung (deeper on the pharmacology
seam and on A4) -> `ideation/rung2_sonnet.md`; an Opus wide-reading rung for niche investing concepts that R02 misses
and that fit this case -> `research/R05_wide_reading.md`.

**Decided elsewhere tonight (I40, Ray: "make your own call"):** D1a the floor is the last source for a coupon gap
(yes); D1b quote the 2031 bottom with a margin, no separate $10k buffer; no re-sizing trades for the dedicated ladder
(`../pm/DECISIONS.md`). So the dedicated ladder stays a Final Report idea unless the Courtroom finds a reason.

**Fact-check back (R04, `research/R04_fact_checks.md`; most web pages blocked, so many items are title-level only).**
- A1 defeasance survives in a smaller form. Escrowed debt takes the US government's rating, and that is no longer AAA
  (AA+/Aa1). An ETF almost certainly can't sit in a defeasance escrow, so only the T-bond rungs pass the strict test.
  Say "funded the way a defeasance is funded", never "defeased" and never "AAA".
- A5 holds exactly: Macaulay duration is mean dissolution time with discounting. Laura's ten payments: 10.5 years
  undiscounted vs 9.90 years discounted. "Zero-order" fits as the same amount each year (stepped, not continuous).
  So far this is the one cross-domain link that is exact, not loose.
- A4's pun is wounded. Compounded drugs are not FDA-approved, so "compounding pharmacist" cuts against a safety story.
  The unbundling idea (annuity-certain + protected note + target-date fund, built from parts) stands without the pun.
  Say "build", not "replicate", since the iBond payout and reinvested coupons make it approximate.
- The 7.5% the locked TNA attributes to JPMorgan is the EAFE figure. AC World is 7.00% compound / 8.28% arithmetic.
  The IPS must not repeat 7.5%. If a return is quoted at all, use about 7% and check for a 2027 edition first.
- iBond end-of-life confirmed from iShares: a fund terminates around 15 Dec and pays out net assets in cash, so IBTM's
  cash arrives before 1 Jan 2033.
- Seed money: raising seed from 10% to 67% of the goal gave "nearly a sixfold increase" in giving. That's lab
  evidence for the case's own claim, but no percentage can be claimed for Laura.

**Sonnet rung back (`ideation/rung2_sonnet.md`).** The best find is an investing argument that happens to be
pharmacology, not a pun:
- **Zero-order vs first-order release = fixed dollars vs fixed percent.** A first-order drug releases a fixed
  share of what's left; an endowment spending a fixed % of its balance is first-order and can never run dry, so it
  can hold stocks. Laura's ten cheques are zero-order: $50,000 whatever the balance. A fixed-dollar draw on a volatile
  pot is exactly what sequence risk punishes. So "why Treasuries for the payments?" has a one-line answer that also
  explains XR: the case asked for zero-order release, and only a matched ladder delivers it. This is now the lead
  candidate for the motif's investing job (with A2, the bottom of the range needs no model).
- Mean residence time = Macaulay duration (10.5 years undiscounted, ~10.1 at 5%). The second moment (spread 8.25
  years squared) is why a duration match is not a funding match: the textbook case for cash-flow matching over
  immunisation, in a pharmacist's units. For the Final Report.
- 80-125% bioequivalence: 0.8 x 1.25 = 1, the same arithmetic as "a 20% fall needs a 25% rise". Final Report aside.
- Downgraded: "do not crush" and dose dumping are partial (an early sale changes the amount, not just the timing).
  Killed: half-life, flip-flop kinetics, and the target-date-fund leg of A4 (those funds rebalance; ours never do). So
  unbundling counts 2 products (a deferred period-certain annuity, a principal-protected note), and the real edge is
  a Treasury guarantee instead of an issuer's or insurer's. "Compounding pharmacist" is out.
- The R: redemption stays first ("ten redemptions"; the Treasury redeems the bond so Laura can redeem her pledge).
  Runway is true (10 years of burn) but fails "ten ___s". "Receipts"/Rx (Latin recipe; XR reversed is Rx) are
  Final Report asides at most.
