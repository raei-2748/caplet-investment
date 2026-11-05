# The pasted idea list, item by item

AI-generated research (Claude Code), Thu 5 Nov 2026, Sydney night, for the one writer of the Book 12 IPS and for
Caplet. **Not submission text.** Nothing below is an IPS sentence: the "meaning" lines are notes on what a point says
for our plan, written to be understood, not pasted. The list itself is verbatim in `keel/BIBLE.md`, Book 12.

**Where the numbers come from (MODEL arithmetic, not forecasts).** The Treasury par curve of 22 Oct 2026 (the newest
on file), bootstrapped the way `keel/scripts/ladder_pv.py` does it. On that curve the ten payments cost $298,861 on
1 Jan 2027, which matches `keel/models/ASSUMPTIONS.md` row A01. World shares: J.P. Morgan's 7.5% compound return
with 16.78% volatility (A06), lognormal, no fees. Wherever the list uses its own inputs (flat 4% yields, 7%
arithmetic, 16% volatility), I check it on those inputs first and on ours second. The check script was scratch work
and is not in the repo; every formula it used is given in the table below.

**Verdicts.** USE IN IPS (the point strengthens our plan as it stands) | ADAPT (wrong as written, but a corrected version
fits) | FINAL REPORT ONLY (true and useful, but it is numbers, exhibits or method, which Wharton keeps out of the IPS:
"final operating-reserve calculations, detailed portfolio projections, a final facility-contribution range, or the
draft communication to co-sponsors") | REFUSE.

**IPS paragraphs, named by their job:** [Idea] the central idea; [2027] the ladder and what certainty means; [2028] the
deposit and the shares; [2031] the range; [Gap] the reinvestment weakness; [2033] the reserve from 2033 to 2042.

## The short version
- The list was written for a different plan, one that holds shares against the payments and controls the risk with a
  rule that trades as markets move (CPPI, funded-ratio traffic lights, ratchets). About two-thirds of it is either a
  template outline for an IPS or report, or machinery for that other plan. Our plan holds no shares against the
  payments, so most of that machinery would have nothing to do.
- Its arithmetic is nearly all right: 20 of the 22 claims I could check hold on its own inputs. One is a little
  high (64% should be about 60%) and one is muddled (the "93%"). Several numbers are stale, though, because they
  assume flat 4% yields when the curve is near 5%, and that changes one conclusion that matters: Treasuries alone would
  leave about **$192,000** for the building, not $140,000.
- The best of it is not the tools. It is four arguments that, once corrected, explain why our plan is built the way it
  is. **Leverage:** shares held against fixed payments put all their risk on the building money. **Ability over
  willingness:** in January 2027 Laura has almost nothing she can afford to risk. **The Treasury hurdle:** our share
  stake is exactly the cushion, so no fall in markets can break the bottom of the range. **Bodie:** insuring shares
  costs more the longer the horizon.
- Three of its ideas would do real damage: the CPPI governor, the 2033 payout formula, and defining certainty as a
  probability threshold. Each one contradicts our dated rules or the IPS rules.

## 1. The quantitative claims, checked

| # | Claim in the list | Check | Right? | Does it hold for Caplet XR? |
|---|---|---|---|---|
| 1 | Reserve cost on 1 Jan 2033, ten $50k payments, annuity-due, flat 2/3/4/5/6%: $458.1k / $439.3k / $421.8k / $405.4k / $390.1k | 50,000 x [1 + (1 - (1+y)^-9)/y]: $458,112 / $439,305 / $421,767 / $405,391 / $390,085 | Right | Yes, as the reason to buy the reserve in 2027. On the 22 Oct forward curve the 2033 cost is $398,697 |
| 2 | A 1-point fall in yields adds ~$17k (4%); unhedged, rate risk "can erase 10-15% of the facility contribution" | +$17,539 from 4% (4.2%), +$16,375 from 5% (4.0%); $17.5k / $140k = 12.5% | Right | Applies only to a plan that buys the reserve late. Ours bought it in 2027, so 2033 yields no longer matter to it |
| 3 | Risk-free plan at 4%: $300k x 1.04^6 + $150k x 1.04^5 = $562.1k; facility = $140.3k | $562,094 and $140,327 | Right but stale | At 5% flat: $188,080. On the 22 Oct curve (all of the 2028 deposit in Treasuries to Dec 2032, plus the $1,139 left over in 2027): **about $192,400**. Never quote $140k |
| 4 | Master equation: facility = null + G0 x (M - 1.265); table rows A-D | Exact identity for a buy-and-hold stake. Rows B, C', C, D reproduce to within $1k; reserve-short odds 0.00 / 0.01 / 0.37 / 3.43% | Right | Yes. For us G0 is the 2028 cushion ($32,133), T is about 5 years, and Rf is 1.2726 on the curve |
| 5 | Shares trail the risk-free plan "about 40% of the time at any sizing" | P(M < Rf) = 40.5% on the list's inputs; **37.7%** on ours | Right | Yes, and the odds don't depend on how much is in shares: sizing changes how big the regret is, not how likely |
| 6 | At-the-forward put = 2N(σ√T/2) - 1 ≈ 15.5% (σ 16%, T 6) | 15.5%. At σ 16.78%: 6.7% (1 yr), 14.9% (5), 20.9% (10), 25.5% (15), 29.2% (20) | Right | Yes: Bodie's direction holds, and insurance against shares costs more as the horizon gets longer |
| 7 | Gap risk: exposure m x cushion; one sudden fall of 1/m breaches the floor; m ≈ 2 survives a 50% crash | Algebra holds: m 2 → 50%, m 3 → 33%, m 5 → 20% | Right | **Ours is m = 1**: the share stake ($32,133) equals the cushion ($150,000 minus the $117,867 the floor fund costs), so only a 100% fall breaches the bottom |
| 8 | Surplus beta = asset beta x (1 + D/E); a 60/40 (beta 0.6) with D/E ≈ 2 → 1.8 | 0.6 x 600/200 = 1.80. On today's 2033 numbers (reserve $399k, surplus about $195k) a 60/40 on the whole pot gives **1.85** | Right | Ours: about $46k of shares on about $196k of surplus = **0.23** (0.23 in 2028 too: $32k on $137k) |
| 9 | Ladder at flat 5.25% ≈ $295k, modified duration ≈ 9.6; 100bp ≈ $28k; a 60/40 with bond duration 5.5 offsets "about a quarter" | $295,337; 9.58; $28,284; 0.4 x $300k x 5.5% = $6,600, which is 23% | Right | True as a criticism of a 60/40. Our ladder matches payment by payment |
| 10 | Liability from 2027 at 4%: Macaulay ≈ 10.2, modified ≈ 9.8, $326/bp on $333k | 10.18 / 9.79 / $326 on $333,328 | Right | Today's curve: DV01 $296/bp on $298,861 |
| 11 | Reserve-cost chart "with the 5.09% break-even marked" | Flat annual yield at which payments 6-15 years out cost exactly $300k: **5.087%** | Right | The real curve slopes up, so the ladder fit under $300k on 22 Oct with the 10-year at only 4.96% |
| 12 | Surplus framework at 4%: PV of the liability $333.4k; assets $300k + 0.75 x $144.2k = $408.2k; cushion $74.9k; funded ratio 1.22 | $333,328; $408,173 | Arithmetic right, conclusion wrong | On today's curve the cushion in hand on 1 Jan 2027 is **$1,139**. **99.2%** of the total cushion is the 2028 deposit, which she hasn't earned yet (PV $143,430). Using it to justify 50% in shares in 2027 is the human-capital mistake |
| 13 | Merton distance to default, DD ≥ 2.33 as "high certainty" | Formula is standard. Illustration: a 60/40 from Jan 2027 (A/L 1.48 with the 2028 deposit counted in full, σ 10.4%) gives DD 1.78, about 4% short | Right as a formula | Consistent with Keel's rival runs (60/40 short 1.3% in history, 7.6% in the storm world: `keel/models/README.md`, M7). **Undefined for our plan**, because the assets move with the payments |
| 14 | Newsvendor: promise the 1/(1+k) quantile; k = 4 → 20th percentile | 1/(1+4) = 20% | Right | Only once corrected (C1 below) |
| 15 | 8-week window: sd ≈ 6.5% against a premium ≈ 0.6% | 16.5% x √(8/52) = 6.5%; 4% x 8/52 = 0.62% | Right | Final Report only |
| 16 | Arithmetic minus geometric ≈ σ²/2 ≈ 1.3 points | 1.28 points (16%); 1.41 points (16.78%) | Right | Keel's models already use compound returns |
| 17 | Shares beat a locked Treasury zero over 5 years "only about 64%" (8.5% arithmetic, 16.5% volatility) | 60% against 5%, 59% against 5.25%; **62%** on our inputs | Slightly high | "About 6 in 10" is the right figure |
| 18 | 5-year zero = 77.4% of face; 5-year at-the-money call ≈ 23% (17% vol, 1.3% dividends); full protection with full participation ≈ break-even | 1/1.0525^5 = 77.4%; Black-Scholes call 22.6% → 100% participation (97% at 4.8%; 36% at 2020's 1%) | Right | Extra check: per $150k, the note beats simply owning the shares only if prices rise more than **~32%** in five years. Below that, owning them pays more and keeps dividends |
| 19 | "The reserve is 93% of contributions" | $421.8k (a 2033 value at 4%) / $450k = 93.7%: a value in 2033 set against deposits in nominal dollars | Muddled | True versions: the payments' face value ($500k) is **111%** of the deposits ($450k); on 1 Jan 2027 they cost **99.6%** of the first $300k |
| 20 | In 2033 the reserve is ≈ $400k against a surplus of ≈ $200k | $399k against $192-196k | Right | Yes |
| 21 | Liability duration "from 10 to 0" | ~10 years from 2027; from Jan 2033, 4.1 years (flat 5%), then 2.8 (2036), 1.4 (2039), 0 (2042) | Right | Yes: this is the answer to Wharton's composition question (H9) |
| 22 | Damodaran implied ERP 4.23% (start of August); expected equity return ~9-9.5% | His site was blocked by the proxy tonight (HTTP 403) | **UNVERIFIED** | It would sit about 2 points above the 7.5% that every Keel model uses |
| 23 | Japan-style decade: reserve "near $500k" | At 0% yields the reserve equals its $500k face | Right | Our real stress, through reinvestment of coupons (see R) |

These I could not check, because they are outputs of the other AI's own model: CPPI's average weights, its 2008 replay
($168k against $185k), the "-82%" reverse stress, and the 60/40's "5-6%" (that last one is consistent with ours).

## 2. Item by item (list order; trivially related lines grouped)

### A. The opening block (lines 452-462)

**A1. Leverage (Modigliani-Miller, Hamada).** USE IN IPS, with the wording adapted: no beta, no names.
- Meaning: the ten payments are a debt that stands ahead of the building money. Any share held against them puts its
  whole swing on whatever is left, about three times over in 2033. So a "balanced" 60/40 is a geared bet for the
  building, riskier for that money than holding all of it in shares. That is why no share stands behind any payment.
- Strengthens: [Idea] or [2027], as the reason the ladder is all Treasuries. Checks: rows 8 and 20.
- Caveat: Hamada's formula treats the debt's value as fixed. A plan that doesn't hedge rates also carries a rate
  mismatch, so 1.8 understates a 60/40's risk to the surplus. Leave the 1.8 out of the IPS; the logic stands without
  it, and the Final Report can show the arithmetic.

**A2. Merton's structural model; DD ≥ 2.33 as the definition of high certainty.** REFUSE for the IPS; FINAL REPORT
ONLY, as a test applied to rival plans.
- A z-score definition is a model statistic, which the IPS bans. It also assumes lognormal assets, and it is undefined
  for a matched ladder, whose risks are coupon reinvestment and fund drift rather than asset volatility. "One metric
  ties your three deliverables together" is an overclaim.
- What survives is the insight that "the surplus is a call on the assets, struck at the payments", which is A1 in
  option form: for us the strike has already been paid. Final Report: a 60/40's DD of about 1.8 (row 13) as an exhibit
  for "why not a 60/40".

**A3. Duration ($295k, 9.6, $28k per 100bp, a 60/40 offsets a quarter).** FINAL REPORT ONLY. The numbers are right
(row 9), but the point is a criticism of the 60/40, not a feature of our plan. Our ladder matches each payment,
which does better than matching duration: it needs no rebalancing and is safe against twists in the curve, not just
parallel moves. V57 already contrasts the two pension methods. One trap: never call our ladder "duration-matched".

**A4. Roy's safety-first and Sharpe-Tint surplus optimisation.** ADAPT.
- What's wrong: Roy's rule trades expected return against the odds of shortfall within one pot. Our plan makes no such
  trade for the payments. It removes the shortfall by matching, and takes risk only with what is left over.
- Corrected, this is a strict order of claims: the payments first, then the bottom of the range, then its top, then
  what she keeps. Risk is allowed for each claim only once the claim ahead of it is fully owned (in the literature,
  "lexicographic" safety-first).
- Strengthens: [Idea]. The names go to the Final Report's lineage section. The hook is the case's own words, quoted
  exactly: "protecting the capital required for her goals".

**A5. Damodaran's implied equity risk premium (4.23%; ~9-9.5% expected return).** FINAL REPORT ONLY, and UNVERIFIED
(row 22). It is a useful cross-check on J.P. Morgan's 7.5% (Treasury yield plus premium), so it can appear as a "high"
assumption set. In the IPS it would hurt: a 9.5% expected return argues for holding more shares.

**A6. The equity premium is thin against 5%+ Treasuries (64%); Bodie against Siegel.** USE IN IPS (Bodie's point,
merged into the horizon item, top-8 #4). The 64% belongs in the Final Report, corrected to about 60% (row 17).
- Meaning: if shares really were safe over long horizons, insuring them against falling short of Treasuries would get
  cheaper as time passes. It gets dearer (row 6), so a payment due on a fixed date can't rest on shares, however far
  away that date is.
- Strengthens: [2027], as the reason no shares back payments due 6-15 years out. It replaces V57's "a loss rarer, not
  smaller"; use one of the two, not both. Siegel's side belongs in the Final Report, so the case is argued both ways.

**A7. The CPPI governor (90% floor, multiplier 3, 60-80% cap, cash-lock, 2008 replay).** REFUSE.
- Why: it is built for a plan that holds shares against a floor, and it trades as markets move. Our rules are tied to
  dates and never triggered by markets; both V57 and V58 say so. "Branch" is a roots label. Its own failure mode
  (cash-lock, and worse than a static 50/50 in its 2008 replay) is the 1987 problem V57 already names.
- ADAPT the one true thing inside it: our plan is the m = 1 member of the CPPI family. When exposure equals the
  cushion, CPPI is simply buy-and-hold: E = A - F, F grows at the Treasury rate, so nothing ever trades. No fall can
  breach the bottom, and no share ever has to be sold (row 7). This goes into top-8 #3.

**A8. Hurdle rate (the risk-free yield is the hurdle).** USE IN IPS, merged with the risk-free benchmark (top-8 #3).
- Meaning: judge every dollar in shares against what that dollar would have earned in Treasuries. Our shares are
  bought with the interest itself, so against an all-Treasury plan the most they can ever cost her is that interest.
- Strengthens: [2028]. The "Branch" label goes.

### B. The 2033 waterfall (lines 463-468)

**B1. The steps, and the formula C = min(0.9S, max(pledge floor, 0.75S)), rounded down to $5k; "confirm the ten strips";
S = assets - Roots.** REFUSE.
1. STRIPS are banned, and our ladder isn't strips.
2. "Roots" is a banned label.
3. The formula sets the gift from the 2033 surplus, which makes the 2031 range a forecast rather than money she owns.
   That is exactly the overpromising the case warns against. When S falls below floor/0.75, the formula pays
   min(0.9S, floor), which can land below a bottom she has already named.
4. A formula doesn't belong in an IPS that Wharton asks to show a framework.

Our version is simpler and stronger: the gift is the bottom (bought in 2028) plus the promised half (moved into
Treasuries before she names it), capped at the top. Keep the order of claims (A4), not the formula.

**B2. The retained 25% as a real option, which also "covers the floor if S falls short".** ADAPT; FINAL REPORT, with at
most one clause in the IPS.
- What's wrong: 25% is arbitrary. Worse, using the buffer as a backstop for the promise turns flexibility into a fund
  the project expects to draw on.
- Corrected: her kept half is worth most as an option precisely because nobody else can count on it. Promising it to
  the building would destroy the option. This agrees with V58's "never promised to the building".
- Final Report: Damodaran's real-options lectures (the option to expand, delay or abandon) are the natural source.

**B3. Damodaran's dividend framework (S as free cash flow to equity, a 75% payout, signalling, Lintner, Swensen).** Split.
- **Lintner: ADAPT.** A near-miss for the IPS, and an alternative reason to the newsvendor (C1).
  - Meaning: companies set a dividend they are sure they can keep paying, because markets punish a cut far more than
    they reward a rise. Laura's named range behaves like a dividend, so she names only money she already owns.
  - What's wrong as written: the list cites Lintner while proposing a payout set from each year's surplus, which is
    exactly what Lintner's managers avoid.
  - Strengthens: [2031]. Final Report evidence: Lintner (1956), plus the event studies on dividend omissions against
    initiations (e.g. Michaely, Thaler and Womack 1995). The magnitudes are UNVERIFIED; check them before citing.
- **Free cash flow to equity / 75% payout: REFUSE.** Nothing is paid out every year. There is one gift, once.
- **Swensen's spending rule: REFUSE.** It smooths a recurring spend, and Laura's surplus funds no recurring spend.

### C. Lines 469-472

**C1. Newsvendor logic (promise the 1/(1+k) quantile; k = 4 → 20th percentile).** ADAPT (top-8 #5: use the reason).
- What's wrong: "promise the 20th percentile of the surplus" assumes the promise is a market forecast. Ours isn't.
  Both ends are owned before she says them, so the quantile is about zero. That is where the newsvendor rule itself
  ends up when a miss is very costly.
- Corrected meaning: the case itself says promising too much costs more than caution, so the number she names should
  be one she can't miss, which means money she already owns. Owning the top as well is cheap: it costs about two
  years of share growth on the promised half, roughly $1,100-1,200 expected on about $20,000 (MODEL: half the shares
  in Jan 2031 against a 2-year Treasury at 4.65-4.9%).
- Strengthens: [2031]. Final Report: the 1/(1+k) arithmetic, the k of about 3 implied by V25 (top reached 3 times in
  4), and how the 2031 lock changed it (`keel/ips_rewrite/IDEA_BANK.md` rows 5, 84, 88). Drop "sponsors remember a
  missed number longer" unless a source is found.

**C2. Premium Check with honest statistics (8 weeks; Lehrer's "The Truth Wears Off").** FINAL REPORT ONLY
(Articulation). True (row 15): six weeks of WInS say nothing about skill. For us they say even less, because our
WInS book is a ladder whose price moves with the cost of the payments. That "The Truth Wears Off" is on the ECON 252
syllabus is UNVERIFIED.

**C3. Diversification audit (marginal risk, diversification ratio); Taiwan stress screen.** FINAL REPORT ONLY, ADAPT.
- For one world fund plus Treasuries, marginal risk and the diversification ratio are trivial.
- Wharton's "appropriate diversification" is better answered at the level of the residency's funding. Every other
  source the case names (co-sponsors, grants, program fees, business income) shrinks in a recession, so Laura's
  contribution is most useful as the part that doesn't. That comes from Keel's 5 Nov shortlist (idea 3), not from
  this list.
- Taiwan dollars: the payments are fixed in US dollars, so the currency risk falls on what they buy (Final Report,
  next to the inflation table).

**C4. Options as priced insurance (puts, collars, the 77.4% / 22.6% benchmark).** FINAL REPORT ONLY.
- The maths is right (row 18), but derivatives are banned for both contributions, listed options don't run to five
  years, and pricing a collar in the IPS would look like planning a banned trade.
- Final Report exhibit: at today's yields the interest buys roughly full participation in a capital-protected note.
  Owning the shares instead pays more unless prices rise by more than about 32% in five years, keeps the dividends,
  and leaves Laura something when markets fall. That is the honest version of V57's "we would rather she owned the
  shares".

### D. The policy skeleton (lines 473-488)

**D1. Mission line ("Protect the commitment first; let the upside serve the dream").** REFUSE. It is a slogan flip
(banned: `keel/ips_rewrite/drafts/D35/README.md`), and "dream" is corny.

**D2. Dual mandate with separate benchmarks.** ADAPT; FINAL REPORT. "Roots" goes. "Funded ratio ≥ 100%" can't
benchmark a matched ladder, which is at 100% by construction. Corrected: the ladder's test is that each holding pays
its payment, and the shares' benchmark is what Treasuries would have paid (A8).

**D3. Risk metrics: surplus-at-risk and distance to default, not volatility.** REFUSE for the IPS (they are model
statistics). In the Final Report, surplus-at-risk is a fair yardstick for rival plans. Our plan's natural measure
needs no statistics at all: money promised but not yet owned, which is zero at every date.

**D4. Three-part certainty definition.** See Q4.

**D5. Hedge 100% of the liability's rate sensitivity (±2%), rechecked whenever a contribution arrives.** ADAPT; we
already do this. A cash-flow match is a 100% hedge at every payment date, not just on average, so it needs no
rechecks. The one recheck that does exist is the 2028 deposit completing the ladder if yields fell before 2027. No
IPS words are needed beyond what V57 and V58 already say.

**D6. Branch governor (CPPI parameters, dial positions, "beyond about 50% equity").** REFUSE. It is CPPI with a roots
label, and the dial positions contradict a strategy that is frozen once submitted.

**D7. Capital market assumptions (building blocks, CAPE cross-check, haircut, three sets).** FINAL REPORT ONLY
(Portfolio Analysis: "reasonable assumptions"). The IPS point is that the payments and the bottom of the range need
no return assumption beyond the Treasury yields locked in at purchase. Only the size of the top depends on share
returns.

**D8. Facility contribution policy (the waterfall).** Same as B1.

**D9. Co-sponsor communication policy (pledge ladder, annual updates, "expects" not "will", the 2031 lock).** FINAL
REPORT ONLY: Wharton puts the draft communication in the Final Report. "Expects" is the case's own word ("how much
she expects to contribute"), and the 2031 lock is already ours. The pledge ladder collapses for us, because
everything she names is owned.

**D10. Decision rights (investment committee, quorum, a limit on discretionary trades).** REFUSE. Laura is one
person, and the case makes the portfolio manager the final decision-maker. Governance boilerplate wastes words.

**D11. Behavioural guardrails (Ulysses clauses, Nudge, 48-hour cooling-off, mandatory pre-mortem).** ADAPT.
- The 48-hour rule is generic. The real version is already in our plan: rules fixed in advance to dates, never to
  markets. Wharton agrees: a strategy "should not be rewritten simply because markets move".
- Naming Ulysses or Nudge would be packaging (Ray, 5 Nov). A pre-mortem belongs in the Final Report's Articulation
  section, and only if it was a real team event.

**D12. Eligible instruments ("no leverage, no short selling, no sold options, issuer limits").** REFUSE as written.
"No sold options" implies bought options are fine, but all derivatives are banned. Wharton's list (WInS-listed
stocks, ETFs and Treasury bonds; no TIPS, no STRIPS) needs no IPS words.

**D13. If-then trigger table (yields ±100bp, a 20% drawdown, ERP above 5.5%, a missed contribution, geopolitics, a
US downgrade).** REFUSE: market triggers contradict our dated rules. Two rows survive as Final Report stress cases.
- A smaller 2028 deposit comes off the bottom (top-8 #3).
- A US downgrade or fiscal shock is the plan's one remaining credit risk (S&P 2011, Fitch 2023, Moody's 2025;
  verify before citing).

**D14. Review and amendment; version log.** FINAL REPORT ONLY. The plan's review points are its dates: 2028, 2031,
2033.

**D15. Three-number dashboard with traffic lights.** REFUSE. Traffic lights, a roots label, and a funded ratio that is
fixed at 100%.

**D16. Assumption register.** FINAL REPORT ONLY. `keel/models/ASSUMPTIONS.md` already is one.

### E. The report outline (lines 489-499)

FINAL REPORT ONLY, as structure. Three notes:
- **"Executive summary first."** The IPS equivalent is Wharton's first question, the central idea, answered in the
  first paragraph (Book 12 bans retelling the case there). Headline numbers don't belong in the IPS.
- **Restating the client's goals as a balance sheet.** Use it as the frame for A1: the payments are a debt, and the
  facility money is the equity behind it. It also makes a good Final Report exhibit.
- **The rest** (rejected alternatives, WInS attribution, uncertainty, inflation and FX tables, what would change our
  mind, the appendix) belongs in the Final Report.

### F. Exhibits (lines 500-510)

FINAL REPORT ONLY.
- Worth building for us:
  - The reserve's cost against the yield, with the 5.09% flat break-even marked (row 11), next to Keel's 1871-2026
    "price of certainty" chart (`keel/models/README.md`, M1).
  - Duration falling from 10 to 0 (row 21).
  - The surplus distribution, with the all-Treasury line drawn at about $192k, not $140k.
- No use to us:
  - A funded-ratio fan, hedged against unhedged: ours is a flat line at 100%.
  - A pledge ladder: everything she names is owned.

### G. "Letter to Laura" (line 511)

FINAL REPORT at most, under Creativity and Presentation. REFUSE the flourish "her work is about storytelling, so let
the numbers carry a narrative".

### H. A template IPS's sections (lines 512-525)

**H1. Purpose and profile; "quote this directly" for a "responsible" balance.** REFUSE as written, because it is a
misquote. The case says "an appropriate balance between pursuing growth and protecting the capital required for her
goals", and "how much of the remaining portfolio she can responsibly contribute". Book 12 also bans an opening that
retells her profile.

**H2. Objectives (return: grow $450K for a liability plus "optional legacy contribution"; risk).** ADAPT. "Legacy" is
the wrong word; it is a facility contribution. Corrected: the payments' required return is met on the day they are
bought (they cost no more than $300k), so growth is wanted only for the building and her flexibility. This belongs
with the hurdle point in [Idea] or [2027].

**H3. Multi-stage horizon (6-year accumulation, "1-year pivot", 10-year distribution).** ADAPT, then USE (top-8 #4).
The "1-year pivot" is invented. Corrected: she has ten payment dates plus 2031 and 2033, and each holding is matched
to its own date. That is the "risk depends on when the money is needed" point, and Wharton's "changing time horizons
and cash-flow needs".

**H4. Liquidity requirements.** ADAPT, one clause. Accurate but generic. For us, liquidity comes from maturities,
never from sales: no cash buffer is needed for the payments because each January a holding has just matured.
Wharton names liquidity in both of its IPS question lists, so the IPS should name it once, in [2033] or [2027].

**H5. Risk tolerance and allocation ranges, glide path, rebalancing bands.** REFUSE. There is no glide path. The
allocation changes on dates, and by holdings maturing.

**H6. Two sleeves at 2033 (an "immunized" reserve; a residual that "may stay growth-oriented").** ADAPT.
- "Immunized" is the wrong word: the reserve is cash-flow matched.
- It isn't built in 2033. It is bought in 2027 and only renamed in 2033 (top-8 #7).
- Only her kept half stays growth-oriented, and it stays unpromised.

**H7. Executive summary of the headline numbers.** FINAL REPORT ONLY, per Wharton.

**H8. Assumptions log, including the fixed-nominal-payment insight.** FINAL REPORT for the log; the inflation
assumption itself is top-8 #8.

**H9. How the operating reserve changes as payments approach and are made ("does duration shorten? yes, explain it
mechanically").** USE IN IPS. Wharton's fourth question asks exactly this.
- Meaning: the reserve changes only by holdings maturing. Each January the next holding has turned into cash and
  pays, so nothing is ever sold or bought, and its rate sensitivity falls to zero by 2042 (4.1 years in 2033, falling
  to 0; row 21).
- Strengthens: [2033]. V57's "never needs rebalancing" and V58's closing line only half-say it.

**H10. Facility contribution: recommended range, method, bear/base/bull table.** FINAL REPORT ONLY.

**H11. Co-sponsor communication: range, confidence, reasoning.** FINAL REPORT ONLY.

**H12. Draft fundraising excerpt.** FINAL REPORT ONLY: Wharton says it is "not expected" in the IPS.

**H13. The true bear case ("does the facility contribution go to zero while the reserve stays protected?").** ADAPT,
then USE (top-8 #3).
- Wrong for us: in a bear market our facility contribution never goes to zero. It falls to the bottom she already
  owns.
- Meaning: a bad share market lowers the top she names and the half she keeps, never the bottom or a payment.
- Strengthens: [2031]. The case requires it: "how favorable and unfavorable investment outcomes would affect" the
  recommendations.

**H14. Why hold back a buffer.** Already in both drafts.

### I. Chhabra's three buckets (lines 526-529)

REFUSE for the IPS; the Final Report's lineage section only.
- Its labels are invented (banned), and "cite it explicitly" breaks the no-citations rule.
- It puts Laura's flexibility money in the "aspirational" bucket, which is Chhabra's high-risk bucket for moving up in
  wealth. That money's job is the opposite: to stay liquid and unpromised.
- "A second facility gift" would promise that money to the building.
- In the Final Report, map the buckets correctly: the personal-risk bucket is the ladder plus the bottom of the range.

### J. "The core math" (lines 530-570)

**J1. 1.1, the reserve-cost table and its finding.** FINAL REPORT ONLY for the numbers, which are right (rows 1-2).
USE the meaning (top-8 #7). "Discount each payment at its own STRIPS yield" is fine as a pricing method (a zero
curve), though ours bootstraps the par curve instead. We never buy STRIPS.

**J2. 1.2, the null hypothesis (the risk-free plan).** ADAPT. USE the principle (A8); REFUSE the number.
- $140k at 4% is stale; it is about $192k on the 22 Oct curve. "Most teams will never compute it" breaks Book 10's
  ban on "every team will ...".
- The honest consequence for us: our bottom (about $145-150k) sits below the all-Treasury plan by roughly the
  interest that buys the shares. Gift plus what she keeps comes to a median of about $196k against $191k, and about
  $175k in the worst year in twenty (MODEL; rows 3 and 5).
- The answer to that judge question is already drafted as the "hardest question" in
  `keel/ips_rewrite/creativity/2026-11-05_shortlist.md`.

**J3. 1.3, the master equation, its table and four insights.** FINAL REPORT ONLY; all correct (rows 4-7).
- "Sizing changes the size of regret, not its odds" is excellent material for the Final Report's Portfolio Analysis.
- REFUSE the conclusion "certainty is expensive, which is why we buy it with rules (the ratchet) instead of options":
  the rules it means are CPPI.
- Its design point of m ≈ 2, surviving a 50% crash, becomes our m = 1.

**J4. 1.4, the surplus framework (λ = 0.75 haircut, m = 2, "where the 50% starting allocation comes from").** ADAPT.
- The arithmetic is right (row 12) but the conclusion is wrong: it counts the unearned 2028 deposit as cushion and
  puts $150k into shares in 2027.
- Its own haircut paragraph is the human-capital point, and it supports our design: on today's curve the cushion
  Laura actually holds on 1 Jan 2027 is about $1k, and the rest is money she hasn't earned yet. That goes into
  top-8 #2.

**J5. 1.5, liability duration.** FINAL REPORT ONLY (row 10). The list says "your floor sleeve should hedge that
sensitivity, not merely sit in safe bonds". Ours already does more than that: it matches each payment.

### K. "Intellectual lineage" (lines 571-578)

- **Contingent immunisation (Leibowitz-Weinberger).** FINAL REPORT ONLY, as lineage. Ours runs it backwards: it
  immunises first, takes risk only with the cushion that arrives in 2028, and switches on a date with no trigger.
  REFUSE it as a design, because it is trigger-based.
- **CPPI with a TIPP ratchet (Perold, Black-Jones, Estep-Kritzman).** REFUSE as a design. Final Report lineage: our
  2031 lock is a ratchet fixed to a date rather than to a price.
- **Redington (match PV, duration and convexity).** FINAL REPORT ONLY. Ours goes further than Redington: matched cash
  flows survive any move in the curve, not just small parallel ones. Two follow-ups for the report: the coupon risk
  that is left over, and why we price it at zero rather than buying a long bond to immunise it (Keel priced that cure
  at 43-50% of the deposit: `keel/ips_rewrite/IDEA_BANK.md`, row 61).
- **Roy's safety-first.** Final Report lineage (A4).
- **Goals-based investing and behavioural portfolio theory (Shefrin-Statman; Das, Markowitz, Scheid and Statman;
  Chhabra).** Final Report lineage.
- **Lifecycle investing with human capital (Bodie-Merton-Samuelson).** ADAPT, then USE (top-8 #2).
  - Wrong direction for Laura: "bond-like labour income lets you hold more equity early" assumes a steady salary.
    Laura's advances, speaking and licensing behave like shares. Ibbotson and co-authors (2007) say human capital is
    "stock"-like when it is correlated with the market and volatile (`IDEA_BANK.md`, row 170).
  - So the right response is less share risk, and none of the payments resting on the deposit. Both drafts already
    say this ("bet on shares twice").
- **Barbell against ladder.** REFUSE (see "hurt us" #8).

### L. The "CFA-style structure" (lines 579-602)

- **Governance, a Ulysses clause, supermajority, 48-hour cooling-off.** REFUSE (D10, D11).
- **Goal ledger in priority order.** ADAPT, then USE the order. Drop "≥ 99.9%", which is a model statistic. Goal 4
  ("never communicate an amount that is not hedged or supported at the stated confidence") is our 2031 rule, already
  in both drafts.
- **Ability against willingness; a creative-industry income beta; avoid media and publishing stocks.** USE (top-8 #2).
  REFUSE the sector tilt: the plan holds one world fund, the WInS book is locked, and media and publishing are a
  sliver of a world index.
- **Constraints (multi-stage horizon, liquidity, out-of-scope tax and law, Taiwan dollars, one-person governance).**
  FINAL REPORT ONLY.
- **Three sets of capital market assumptions; arithmetic means against geometric.** FINAL REPORT ONLY. The sets are
  stale: they assume Treasuries at 4% and cash at 3.5-4%, against a curve running from 4.1% to 5.3% on 22 Oct.
  σ²/2 checks out (row 16).
- **Allocation table, glide path, trigger table.** REFUSE.
- **Liability-relative benchmark.** FINAL REPORT ONLY.
- **Rebalancing with contributions.** Already ours: the 2028 deposit completes the ladder first.
- **"Reserve Establishment" and "Facility Release" protocols.** REFUSE the labels. The Final Report describes the
  dated rules instead.
- **Monitoring dashboard (funded ratio, cushion, m, VaR and CVaR, tracking error).** REFUSE.

### M. Exhibits and tests (lines 603-614)

FINAL REPORT ONLY.
- **Waterfall diagram.** Fine, if it uses the case's words for the tiers.
- **Surplus distribution with a $140k risk-free line.** Use about $192k instead.
- **Historical stress tests (1973-74, 2000-02, 2008, 2022, 2000-09).** Keel's model suite already covers every start
  month since 1871 (`keel/models/README.md`, M1b and M8).
- **Reverse stress test.** ADAPT.
  - In our plan, even a total wipe-out of the shares touches no payment and no part of a named range.
  - What could break a payment: a US default; fund tracking far worse than history; or a 2028 deposit that fails to
    arrive in a year when the 2027 ladder needed it (the ladder costs more than $300k on 1 Jan 2027 in about 1 case in
    3: `keel/library/ips_numbers_2026-10/IPS_number_sheet.md`).
  - That makes a strong sentence for the Final Report, and one clause in the IPS's definition of certainty.
- **Confidence ladder (Committed / Planning / Stretch).** Ours collapses to "committed".
- **The decision tree for 2031, 2032 and 2033.** A good exhibit. The rules themselves go into the IPS in words.

### N. Stochastic yields; the pedigree citations (lines 615-616)

FINAL REPORT ONLY. Keel's yields move in parallel (row A02 of ASSUMPTIONS.md). A two-factor model would test twists,
but our matched ladder is safe against twists, except for the coupon gap, which is already priced at zero. Merton's
idea of defeasing essential goals with safe assets: USE as the principle, unnamed. It is already the spine of V58.

### O. The four-strategy table (A lock-everything, B surplus-only equity, C dynamic CPPI, D static 60/40) and "recommend C" (lines 617-622)

REFUSE the recommendation; ADAPT the table for the Final Report.
- Ours is a stricter B: shares only from the surplus, and only its interest.
- A's "zero upside beyond ~$140k" is stale; the figure is about $192k.
- D failing a high-certainty test is consistent with Keel's M7.
- The exhibit "why D fails" can be built straight from Keel's rival scoreboard (`keel/models/README.md`).

### P. Brier scores, "resulting", liability-relative performance (lines 623-625)

- **Brier scores.** FINAL REPORT, and only if real forecasts exist. Keel knows of no probabilities that Caplet's
  students logged, and inventing them would breach Wharton ethics. "Almost no team will show calibration" is banned
  wording.
- **Duke's "resulting".** FINAL REPORT, Articulation, using real events only: the 7 Oct mis-click, and the four notes
  on cancelled orders.
- **Liability-relative performance and a "Reserve Cost Ticker".** FINAL REPORT ONLY, and a good one. When yields fell
  in October, our WInS value rose (+1.85% by 23 Oct) while the cost of the ten payments rose with it ($292k on 6 Oct,
  $298.9k on 22 Oct), so the gain wasn't Laura's.

### Q. The second outline (lines 626-654)

- **Purpose and governance.** REFUSE.
- **Client goals as quantitative constraints.** FINAL REPORT.
- **Liability specification "to be met with a probability of at least 99%".** ADAPT: drop the probability. The case
  defines the payment; we define the certainty (Q4).
- **Q4. The four-test definition (structural, probabilistic ≥ 99%, stress, reverse stress).** ADAPT, then USE the
  structural test (top-8 #5).
  - The probabilistic, stress and reverse-stress tests go to the Final Report. The case asks teams to "explain how
    they evaluated that level of certainty". The Final Report can do that in full, and the IPS can name the method:
    by construction, then tested against history and against rates at zero.
  - One correction: "only U.S. government credit risk remains" is not quite true for our holdings. iBond funds pay
    back a net asset value, not a promised par (the locked TNA's wording), and the coupons must be reinvested. Name
    both.
- **"Ability, not willingness, binds (the reserve is 93% of contributions)".** USE (top-8 #2), with the arithmetic
  corrected (row 19).
- **Roots / Canopy / Ballast allocation.** REFUSE: banned labels.
- **Funded-ratio traffic light, yield ratchet, rebalancing toward Roots.** REFUSE.
- **Contribution-shortfall contingency.** USE, as part of top-8 #3.
  - Meaning: a smaller 2028 deposit still completes the ladder first, and the shortfall comes off the bottom almost
    dollar for dollar. The payments are untouched unless the deposit was also needed to finish the ladder (Keel M5).
  - Strengthens: [2028]. The drafts raise the deposit's risk (the human-capital point) but never say who absorbs a
    shortfall.
- **Instrument selection criteria; liability-relative benchmark; assumption register.** FINAL REPORT.
- **Behavioural guardrails for the "Canopy".** REFUSE.
- **One-page decision card.** FINAL REPORT, as the report's first page. REFUSE the labels "Trap Register",
  "Riskless Anchor" and "Ballast".
- **The remaining chapters.** FINAL REPORT structure.

### R. Eight stress scenarios (lines 655-663)

FINAL REPORT ONLY. Our plan's answer to each:
- **Equity scenarios (2008, 2020, the dot-com decade):** they move the top and her kept half, never a payment.
- **2022, stocks and bonds falling together:** costs the ladder nothing, because nothing is sold.
- **1970s, rising yields:** helps with the coupon gap.
- **Japan, near-zero yields:** our real stress, covered by pricing the gap at zero.
- **A contribution shock:** see Q above.
- **2008 plus a contribution shock:** lowers the bottom, not the payments, unless the ladder needed the deposit.

### S. Simulation blueprint, code and averaging assumptions (lines 664-679)

FINAL REPORT ONLY. The code is right (row 3). Keel already has regime, bootstrap and history worlds (`keel/models/`).
Averaging several houses' assumptions is good Final Report practice, since Keel uses J.P. Morgan's alone.

### T. Research library and data (lines 680-690)

FINAL REPORT Works Cited, for sources actually read. Add Perold and Sharpe (1988), on buy-and-hold as the m = 1 case of
CPPI; verify their wording before citing.

## 3. The 8 items that most deserve a place in the IPS (ranked)

| Rank | Item (list source) | The plain so-what | Paragraph | Already in V57 / V58? |
|---|---|---|---|---|
| 1 | **Leverage** (A1, with the balance-sheet restatement from E) | The ten payments are a debt in front of the building money, so any share behind them is geared onto the building. A "moderate" 60/40 would leave the facility money riskier than holding it all in shares. Hence no shares behind any payment | [Idea] or [2027] | No. New, true, and it explains the plan's single biggest choice |
| 2 | **Ability, not willingness** (Q, L), fused with **human capital** (K: BMS corrected; J4) | She is willing to take risk, but in January 2027 the payments cost almost all of her $300,000, so she has nothing yet that she can afford to risk. Her only cushion is a deposit she hasn't earned, from income that falls with the share market. So the shares wait for that deposit, and get only its interest | [2028] (or [2027]) | Human capital yes ("bet on shares twice"); the ability point no |
| 3 | **Risk only the interest, measured against Treasuries** (A8, J2, A7 corrected to m = 1, H13, Q contingency) | Every share must beat what Treasuries would pay. Ours are bought with the interest, so the stake equals the cushion: no fall can breach the bottom, nothing ever has to be sold, and the worst they can cost her against all-Treasuries is that interest. Bad markets lower the top and her kept half; a smaller deposit comes off the bottom; no payment is touched | [2028] + one clause in [2031] | Partly ("roughly the interest"). The m = 1 logic and the bear case are missing |
| 4 | **Safety depends on the date** (H3 corrected; A6 Bodie) | A bond is riskless only for the date it pays. Cash fails a dated payment because rates can fall, and shares fail it because insuring them gets dearer the longer you wait. So each payment gets the one holding that pays on its date | [2027] | V58 has the cash half; V57 had a weaker Bodie line. Use one sentence |
| 5 | **High certainty, defined by ownership** (Q4 structural test; M reverse stress) | Certainty means every payment is owned, as a Treasury holding that matures before it, before any other risk is taken. Name what is left: US credit, the funds paying a net asset value rather than par, and coupon reinvestment priced at zero; plus the one assumption (the 2028 deposit, if 2027 prices need it). The case asks to define it, say how it was evaluated, and give the assumptions | [2027] | The definition yes. What is left and how it was evaluated: no |
| 6 | **Own a number before naming it** (C1 newsvendor corrected; B3 Lintner as the alternative) | The case says a broken promise costs more than a cautious one, so the number to name is one she can't miss: money she already owns. Owning the top too costs only about two years of share growth on the promised half | [2031] | The rule yes; the reason is thin ("co-sponsors count on a number") |
| 7 | **Buy the reserve in 2027, then let it run** (J1; H6, H9) | A reserve set aside only in 2033 is a bet on 2033's rates (a 1-point fall adds about $16-17k). Bought in 2027, it is only renamed in 2033. After that it changes only by holdings maturing: nothing is sold or bought, and its rate sensitivity runs down to zero. That is Wharton's fourth question, answered directly | [2027] for the why; [2033] for the change | Implicit only |
| 8 | **Fixed nominal payments: the inflation assumption** (H8; the case asks for "the effect of inflation on portfolio projections and facility costs") | Inflation can't make a fixed $50,000 cost more, so nominal Treasuries are its exact match; TIPS would add a mismatch, and are banned anyway. The reserve's real rate risk runs the other way, falling rates widening the coupon gap, which is why the gap is priced at zero. Inflation's bite lands on the building and on what each payment buys, which is why the kept half stays in shares and liquid, and is not promised as insurance (only ~5% cover: Keel M4) | One clause in [Gap] or [2031] | No: neither draft states an inflation assumption |

Near-misses: the order of claims (A4), which the dates already imply; Lintner (B3), an alternative to #6, not an
addition; Merton's defeasance (N), already the spine, so it needs no name; liquidity from maturities (H4), one clause
that could ride inside #7.

**Fit.** #5 and #6 are already in both drafts, and #3, #4 and #7 are half there. The new words are #1, the ability half
of #2, the m = 1 and bear-case half of #3, and #8. That is roughly four or five sentences, against a V58 that already
stands at 497 words. They have to come from ideas cut whole. The obvious candidates are the named-concept sentences
Ray called packaging: V57's capital-protected note and 1987 lines, which C4 and A7 move to the Final Report.

## 4. The items that look clever but would hurt us (ranked)

1. **The CPPI governor, its "Branch" dial, the funded-ratio traffic lights, the yield-triggered ratchet, and "recommend
   strategy C" (A7, D6, Q, O).** These would contradict the locked plan (dated rules, never market-triggered), the TNA
   and the drafts' own rejection of portfolio insurance. They bring gap risk and cash-lock with them, carry roots
   labels, and need parameters (90%, ×3, 60-80%) that only a model can justify.
2. **The 2033 payout formula C = min(0.9S, max(floor, 0.75S)) (B1).** It sets the gift in 2033 rather than owning it
   in 2031, so the named bottom can be missed. It uses banned STRIPS ("ten strips") and the banned "Roots", and it cites
   Lintner while breaking Lintner's lesson.
3. **A probability threshold as the definition of "high degree of certainty" (DD ≥ 2.33, ≥ 99%, ≥ 99.9%) (A2, Q4,
   L).** These are model statistics, which the IPS bans. They rest on a normal-distribution assumption and are
   meaningless for a matched ladder, and they would trade our strongest answer (ownership) for a weaker one ("our
   model says").
4. **Chhabra's three buckets "cited explicitly to signal sophistication" (I).** Invented labels plus a citation, both
   banned. It would also file Laura's flexibility money under the high-risk "aspirational" bucket, and its "second
   facility gift" would promise money that is meant to stay unpromised.
5. **Quoting the $140k risk-free null (J2, O).** The figure is stale (about $192k on today's curve), and "most teams
   will never compute it" is banned wording. Quoting the true figure without its answer would hand a judge the
   question "why is your bottom lower than Treasuries alone?"
6. **The surplus framework's m = 2, which "explains" 50% in shares in 2027 (J4).** It treats an unearned, cyclical
   deposit as cushion, which is the very mistake our human-capital point exists to avoid. The real cushion in hand in
   2027 is about $1k.
7. **Options, collars, and pricing the protected note (C4).** Derivatives are banned, and listed options don't reach
   five years. The 2025-26 lesson was "traded assets outside the trading rules", so the IPS must not look as if it is
   planning one.
8. **A barbell for extra convexity (K).** It gives up the exact match, brings twist risk and a need to rebalance, and
   the convexity it buys is already priced (barbells yield less).
9. **"β 1.8" printed in the IPS (A1).** The arithmetic is right, but it is a number without a source in the IPS, and it
   assumes a fixed-value liability. Keep the logic and leave the number for the Final Report.
10. **A 9-9.5% expected return built from Damodaran's premium (A5).** It is unverified, contradicts the 7.5% basis
    used everywhere else, and argues for more shares.
11. **Slogans and coined names: the mission line, "Riskless Anchor", "Trap Register", "Decision Card", "Letter to
    Laura" as storytelling (D1, Q, G).** They read as packaging, which is Ray's 5 Nov complaint exactly.
12. **Institutional governance: committee, quorum, supermajority, 48-hour cooling-off, dashboards (D10, D11, D15, L).**
    It reads like a pension fund's template. Laura is one person, and the case makes the portfolio manager the
    decision-maker.
13. **"Quote 'responsible' balance directly" (H1).** A misquote of the case.
14. **Avoiding media and publishing stocks (L).** It can't be done with one world fund, the WInS book is locked, and
    it would draw attention to a tilt that doesn't exist.

## 5. Notes for the writer, found while checking
- **Three case requirements neither draft states outright:**
  - the inflation assumption (case: "the effect of inflation on portfolio projections and facility costs"): top-8 #8;
  - how favourable and unfavourable outcomes change the gift: top-8 #3;
  - how the reserve's composition changes, which is Wharton's fourth IPS question: top-8 #7.
- **Liquidity.** Wharton names it in both of its IPS question lists; the drafts mention it only as "liquid".
- **Missing file.** `keel/final_report/ERUDITION_PLAN.md`, named in the brief, does not exist in the repo. Nothing
  above depends on it.
- **Unchecked source.** Damodaran's site could not be reached tonight (proxy HTTP 403), so his premium figure stays
  UNVERIFIED.
