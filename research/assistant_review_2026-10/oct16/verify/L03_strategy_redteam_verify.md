# Verifier report: L03 Investment strategy red team

Checked Fri 16 Oct 2026 (Sydney). AI-prepared check for planning only. It is not text to submit. Every finding was re-opened at its cited file and line, or re-run. Verifier scripts: `scratchpad/oct16/verify/L03w/basis.py` (ladder-cost bases) and `build.py` (writes the JSON).

**Result:** 17 findings checked. 10 confirmed, 7 adjusted, 0 refuted, 3 added. The surviving set is in `L03_strategy_redteam.final.json`.

**Overall:** L03's skeleton is sound and its quotes are accurate. It has three weaknesses:
1. It compares ladder figures priced on different bases (see the number conflict below).
2. It does not use the 16 Oct commit 412e9e3. That commit's number sheet already found the post-2033 coupon gap, and it offers a competing fix (a buffer).
3. A few severities and examples are overstated.

No personal data was found in L03's findings. They use first names only, and no username, surname or fork owner appears.

---

## The number conflict: $294k vs $298.6k

Both figures use the same 15 Oct 2026 Treasury par curve. They differ only in **method**. I re-ran the 15 Oct brief's own pricer (`oct14/factcheck/ladder.py`) four ways:

| Discount each $50k to... | Valuation | 15 Oct cost | Room | Break-even |
|---|---|---|---|---|
| holding maturity date (gap cash earns 0%) | today's curve applied unchanged on 1 Jan 2027 ("unch") | **$298,628** | $1,372 | 4.7bp |
| holding maturity date | forward to 1 Jan 2027 | $297,847 | $2,153 | 7.4bp |
| 1 Jan payment date | unch | $295,246 | $4,754 | 16.1bp |
| 1 Jan payment date | forward to 1 Jan 2027 | **$294,461** | $5,539 | 18.8bp |
| maturity date, gap cash at the 3-month yield (4.28%) | forward | $295,329 | $4,671 | about 16bp |

- **The number sheet** (`caplet-latest/research/ips_numbers_2026-10/ips_numbers.py`, `bootstrap_cost()`) uses the payment-date, forward method. Its figure is $294,453.
  - This is V5's basis: 25 Sep recomputes to $292,272, which matches CLAUDE.md's "$292,264".
  - So V5's "about $292,000 at late-September yields" is dated correctly. Like for like, it is now about $294.5k.
- **The lenses (L03/L05/L08)** use the maturity-date, unch method. Two things make it higher:
  - Cash waits between each holding's maturity and the payment, earning nothing: +$3.4k. The gaps are 17 days for iBonds, 10.5 months for Feb-2037, 7.5 months for May-2038 and 1.5 months for the Nov bonds.
  - It assumes no roll-down: +$0.8k.
  - This is the **team's own basis for the IBTR note**: 6 Oct gives $293,453 and 22.7bp, which is COMPETITION.md:153-154's "$293k ... about 0.2 percentage points".
- **Which is right for which claim:**
  - *"What the payments cost" (IPS, Final Report):* use payment-date forward, about $294.5k. The plan puts waiting money in a short-term Treasury ETF (trade notes, 05_…md:16-17), which gives about $295.3k, so this is the realistic figure.
  - *"Has the IBTR note's 0.2-point trigger moved?" (TNA):* use L03's basis, because it matches the note. On that basis the trigger went from 0.23 to 0.05 points. On the payment-date basis it went from 0.38 to 0.19. Either way it has roughly halved or worse.
  - *$298.6k* is a labelled **conservative bound** (waiting cash earns 0%), not the headline.
  - *Odds of costing over $300k on 1 Jan 2027:* L03's 44% applies its 3.15% volatility to the conservative basis. On the payment-date basis the same volatility gives about 28%; the sheet gives 35%. "About 1 in 3" is fair. "Coin flip" is not.
  - Neither method includes coupon-reinvestment risk or the 0.07% iBond fee.
  - The sheet's own `ladder_headroom_bp` (13.4) comes from a third method (par-as-zero, $295,924), but its text says 0.19 points.

---

## Verdicts, finding by finding

**STRAT-02: "High degree of certainty" undefined. ADJUSTED (critical → high).**
- What holds:
  - The case requires a definition (Client_Profile.txt:97-99: "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions").
  - V5 has no definition.
  - V5:20's "depends mainly on the US government" is true for principal only.
- What is wrong:
  - The title says certainty was tested "only on banned instruments". That is false. D_certainty_definition.md:33-37 (test 3) tests the WInS-listed Book L: $447k at 0%, with a break-even near 5%. The 16 Oct number sheet now tests V5's exact plan.
  - The 65% replay figure (ws7 output:18) counts any rung short by any amount, with no netting.
    - Starts in the 1980s to 2010s are 91-100% short (output:20), because those decades replay the long 1981-2020 rate fall.
    - The median delivered is $501,704.
    - So quote the size of shortfalls, not only how often they happen.
  - The 15 Oct brief's "420bp" line (final.md:580, :776) is confirmed wrong on the WInS basis.
- Severity: one principle sentence fixes the IPS, and the tests belong in the Final Report. So high, not critical.

**STRAT-03: Post-2033 reinvestment risk not covered by the shortfall order. CONFIRMED (high).**
- Verified:
  - V5:26.
  - D_stress_bad_year.md:48: "beyond it, she adds her own money".
  - Case lines 91-92: "may not rely on co-sponsors, grants, program fees, or other outside funding".
  - L03's model outputs in cf_1015.txt and pooled_1015.txt.
- Independently corroborated: the number sheet (lines 46-48) finds that in 6-7 of 100 paths part of a payment after 2033 is not covered.
- Re-labelled **known-deeper**, because the 16 Oct sheet found it first.
- Extra point: the sheet's 93% assumes that in 2033 the team can already see future shortfalls. It cannot.

**STRAT-01: Room under $300k. ADJUSTED (stays high).**
- All quotes are verified.
- Numbers corrected as set out in the number-conflict section above:
  - room about $5.5k on V5's basis, $1.4k on the 0%-carry basis;
  - odds about 1 in 3, not 44%;
  - V5's $292k is dated correctly, not wrong.
- Still high, because the IBTR note is a suggested TNA pick, due in 7 days, and notes cannot be edited.

**STRAT-05: Laura's kept half is given three jobs. CONFIRMED (high).**
- V5:26, :28 and :30 each give it a job: payment backstop, inflation and Taiwan-dollar defence, and cost-overrun cushion.
- Sizes match sleeve.txt. D_stress_bad_year.md:32 and :48 are verified.
- The IPS brief names "preserving appropriate financial flexibility" as an IPS job (IPS-FINAL.txt:48-50), so high is fair.

**STRAT-06: Growth branch tiny; trade-off stated backwards. ADJUSTED (stays high).**
- The sign error is real. Under gift = floor + half the fund, moving money from the floor to stocks lowers the expected gift. MODEL: median gift $175k with a $150k floor against $152k with a $100k floor.
- COMPETITION.md:164 and V5:28 are verified as stating it the other way round.
- Corrections:
  - VT is about $32-35k (7-8%), not $35.2k. V5 keeps the 2027 leftover as the first buffer, outside VT. The number sheet says about $32k, about 7%.
  - The D_rivals percentiles are on the STRIPS basis, and the 15 Oct brief says not to quote them (final.md:437). Use them as internal evidence only.

**STRAT-04: Dedication instead of the own-rung ladder. ADJUSTED (high → medium).**
- The LP is checked and plausible: $309,634 at 0% carry and $304,102 at 2%. It is a single build, and it treats each iBond as one bond.
- It is an option, not a defect, so medium.
- Two gaps in the fix:
  1. The proposed vote (Tue 27 Oct) falls **after the TNA deadline (23 Oct ET)**. The LP drops the IBTM 2033 rung, which the IBTM note and suggested pick describe (05_…md:19). Decide the direction before the TNA.
  2. It ignores the number sheet's buffer option ($10-20k from the 2028 deposit). On L03's figures, dedication is cheaper. Put both on the same decision list.

**STRAT-10: WInS rungs are about two-thirds of a payment. ADJUSTED (medium).**
- Verified: 05_…md:20, :22 and :24. tickets.md has IBTO 1,016 against 1,503 shares (0.676). COMPETITION.md:177 shows 1,024 filled.
- The fix said to add the mapping to "every reflection". That is too heavy under the 100-word cap (TNA-FINAL.txt:46). Add it only where a reflection discusses a dollar amount.

**STRAT-07: "By construction" can read as a tautology. CONFIRMED (medium).**
- D_range_confidence_2031.md:7, :25 and :32 are verified, and so are case lines 117-118.
- The number sheet now gives the "where it lands" figures: 99.4% inside the range, typical gift about $167k, at or near the top about 3 times in 4. They must be rebuilt for the Final Report.

**STRAT-08: The floor rule can make the branch vanish. ADJUSTED (medium; confidence high → medium).**
- The two readings are verified: V5:24 says "remainder", COMPETITION.md:155-156 says "about $150k". This is known from final.md:431.
- Corrections:
  - Under V5's "remainder" reading the stock fund is a fixed share of what is left, about 14% at a 3% five-year yield. It shrinks but does not vanish unless yields are very low.
  - L03's $6k example mixes a 2-point yield fall with a top-up sized for a small fall.
  - On 2 Jan 2026 the ladder cost $317-325k depending on basis, not just $325k.

**STRAT-09: iBond mechanics glossed. CONFIRMED (medium).**
- I re-fetched the IBTM page on 16 Oct 2026: "Weighted Avg Maturity 5.71 yrs as of Oct 14, 2026", fee 0.07%.
- The IBTR page text is verified: "do not seek to return any predetermined amount", "transition to cash and cash-like instruments", net assets $109,148,633.
- About 61% of the WInS book is in iBonds (from the COMPETITION.md:176-180 fills).

**STRAT-11: Operating reserve size and composition. CONFIRMED (medium).**
- Verified: case line 96, IPS-FINAL.txt:48-49, V5:26, and SGOV at wins_notes.csv:33.
- The annuity values are recomputed and correct.
- The public permitted list (faqs.txt:42-45) has no "cash" line, so naming an ETF for waiting money is the safe reading.

**STRAT-12: Facility-cost inflation not measured. CONFIRMED (medium).**
- The arithmetic is recomputed: $117.5k at 3.54% a year, $96.4k at 6.53%.
- Caveats:
  - The 6.53% is a *derived* total (fact_register.md:206), not read on a primary page.
  - The case says teams need not estimate facility cost (lines 165-166). So show purchasing power, not a cost estimate.

**STRAT-15: Overbuilt behind the scenes, under-explained on the page. CONFIRMED (medium).**
- The word "liquidity" appears nowhere in V5.
- IPS-FINAL.txt:46 names liquidity.

**STRAT-13: Taiwan-dollar risk. ADJUSTED (medium → low).**
- The numbers are verified.
- The case never names a currency or asks for FX analysis, and V5:28 already names the risk. One assumption line in the Final Report is enough.

**STRAT-16: Return assumptions rest on one year-old house view. CONFIRMED (low).**
- A web search on 16 Oct 2026 again returned only the 2026 (30th) edition (https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/pb-ltcmas).
- Whether a 2027 edition exists is still UNVERIFIED.

**STRAT-14: TIPS and tax. CONFIRMED (low).**
- Case lines 90 and 168 are verified.
- Whether WInS lists any TIPS is UNVERIFIED.

**STRAT-17: Long-bond timing and price swings. CONFIRMED (low, known-repeat).**

---

## Findings L03 missed (added)

1. **VER-L03-01: Two ladder-cost bases are in circulation (high, TNA 23 Oct).**
   - The problem is set out in the number-conflict section above.
   - The team must pick one headline basis, label every figure, and keep $298.6k only as a labelled conservative bound. This must happen before any TNA reflection mentions the IBTR trigger.

2. **VER-L03-02: The 16 Oct commit steers dated numbers into the IPS (medium).**
   - caplet-latest/COMPETITION.md:202-203 tells the team to use the number sheet "for the dollar range, the confidence, the allocation and the return assumption" in the IPS.
   - The IPS brief says the opposite. It asks for focus on strategy "rather than describing individual investments or presenting detailed financial calculations" (IPS-FINAL.txt:51-52). It also says the IPS "is not expected to include ... a final facility-contribution range" (IPS-FINAL.txt:68-70).
   - Numbers frozen in the IPS on one day's curve will go stale. Put rules in the IPS and figures in the Final Report.

3. **VER-L03-03: Wrong-way risk in the shortfall backstop (medium).**
   - The coupon shortfall comes from yields falling and staying low. That often happens in recessions, when the stock half Laura keeps is also small. The kit's 2008 replay shows the gap beyond her half is $12,047 (D_stress_bad_year.md:32).
   - Both the number sheet and L03 assume rates and stocks are independent (ips_numbers.py:97; IPS_number_sheet.md:69-70), so their cover figures are probably optimistic.
   - Test any coupon-risk rule on a joint bad case, and prefer a cover that does not depend on stocks.

## Does commit 412e9e3 change L03's conclusions?

Yes, in four places:
- **STRAT-03:** the commit corroborates it, so it becomes known-deeper.
- **STRAT-04:** it adds a competing buffer option that the team must weigh.
- **STRAT-01:** it supplies the like-for-like headline figure ($294.5k).
- **VER-L03-02:** it creates a new risk of numbers being frozen in the IPS.

The new rule allowing "[AI]" Google Docs suggestions changes none of the strategy findings. No L03 fix contains drafted deliverable prose.
