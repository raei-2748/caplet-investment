# The 2031 "lock-in": a tested alternative, not a change

> **Verified 20 Oct (`oct20/verify_lockin/verify_lockin.md`, independent engine, two seeds): CONFIRMED - every headline reproduces within ~1 point; conclusions safe for the 27 Oct vote (keep "2031: nothing traded"; the top rule is the lever).** Fixes: §9 cost of locking is ~$0.8k on the median (2.2 pts compound) or ~$1.4k on the average (~4 pts/yr) basis - say which; §5 the 3r "$21 per $1" ratio is noise (gift moves only +$40-70); ~30 (not 36) independent two-year periods; "+$1.1k to +$1.8k in falls" - $1.8k is the flat case; history windows use US S&P returns, not world stocks. Under 3r +$0, a lock LOWERS reach on the bootstrap too (90.6 -> 89.0). Side finding: with the reserve marked at market, 3r payment-short odds are 0.08% (MC) / 0.32% (bootstrap) / 0.72% of history windows - quote those, not 0.02%. **Consistency fix 20 Oct (packaudit §1d):** 3r = about 0.6% short on the agreed engine (0.08/0.32/0.72% marked at market); never quote 0.02%; the 0.02% cells below are study-engine, at-cost figures.


AI-generated research for Team Caplet, written by Claude Code on Tue 20 Oct 2026 (Sydney), wave D. These are MODEL numbers, for a Final Report "alternative we considered". They are not text to submit. If the team uses any of it, log it in the AI-use record and cite it in the Final Report's Works Cited (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026). Nothing here changes the IPS unless the team votes for it.

Paths: `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/`. All scripts and outputs are in `oct20/lockin/`.

---

## Verdict: keep "2031: nothing traded"; file the lock-in as a tested alternative

1. **The LDI review is right about the asymmetry, but it is there by design.** Between 2031 and 2033 the gift's half of VT can fall but cannot rise past the cap. The upside is not lost: it goes to Laura's kept money. The cap decides *who* carries the stock risk. It does not change how much money there is.
2. **The case's own test does not move.** The case asks how confident the team is that the 2033 gift falls *within the range* (case:117-118). That is 98.1% under option 1 and 99.9% under 3r, with or without a lock. The lock improves something else: the chance of reaching the *top*.
3. **Under option 1 the lock does what it says, at a price.** The chance of reaching the top rises from 68% to 88% (Monte Carlo; 71% to 81% bootstrap). Each $1 of extra expected gift costs Laura about $3 of expected kept money ($6 on history). It also needs a new rule and two trades in 2031.
4. **Under 3r with the top fix (+$5k) the lock barely helps:** 73% to 77%. On the history windows it makes things worse (73.5% to 68%). Most misses under 3r come from the reserve's $5k share of the top, which a stock lock cannot touch.
5. **The cheaper way to a surer top is how the top is set, not a 2031 trade.**
   - A narrower top (count ¾ of VT's half) reaches 89-90% with no trade and no loss of total money. The cost is a median gift about $4k lower.
   - Under 3r, counting **$0** of the reserve in the top gives 92% with no lock (side finding, section 8).
   - Which way to go is a values call for the team, not a modelling question.

---

## 0. How it was tested

- **Engine.** `oct20/lockin/scripts/lock_engine.py` is a copy of the red team's `oct20/redteam3r/scripts/rt_engine.py` with one addition: an optional 1 Jan 2031 lock and a narrower-top switch.
- **The lock as modelled.**
  - On the day the range is set, VT worth the cost is sold *from the gift's half*.
  - That money buys a Treasury maturing 15 Dec 2032 at that day's 2-year yield, sized to repay the stock-dependent part of the top (top − floor).
  - Laura's half of VT is never touched.
  - In 2033: gift = min(top, floor repaid + lock repaid + the gift's leftover VT).
- **Validated before use.** With the lock off, it reproduces the red team path by path: max difference 1e-10 dollars over 100,000 paths (`data/validate_lock_19oct.txt`, `data/validate_lock_16oct.txt`).
  - 19 Oct curve, option 1: 15.58% short, max $6,179, top median $166,996, gift median $166,177, reaches top 68.4%, below bottom 1.95%.
  - 3r with top +$5k: 0.02% short, max $613, top median $160,807, gift median $160,160, reaches top 73.0%.
  - These are exactly the red team's `data/verify2_out.txt` figures. On the 16 Oct curve it also matches their `validate_out.txt` (16.45%, $6,121, $165,259; 3r 0.02%, $162,190; 3b 4.85%).
- **Basis.**
  - Treasury par curve of 19 Oct 2026 (`oct20/redteam3r/data/tsy_202610_fetch20oct.csv`, fetched from treasury.gov 19 Oct 21:42 UTC). The ladder costs $298,446 on it.
  - Holdings' dates. Waiting cash at 0%. Random-walk yields at 1.0 point a year; VT at 7.0% compound, 16.78% volatility, 0.06% fee.
  - 100,000 paths, seed 20261019.
  - Also run on: the 12-month block bootstrap (20,000 paths, real curve twists, seed 20261021, as the red team), the 690 overlapping 16-year history windows from 1953 with real curves, and a stock-yield correlation of +0.5.
- **Verified twice.**
  1. Everything was re-run with seed 7, with a fresh bootstrap seed (`data/lockin_19oct_s7.txt`). Monte Carlo headlines moved by 0.2 points or less, and bootstrap headlines (new seed, 20,000 paths) by 0.6 or less.
  2. Five deterministic cases were recomputed by hand from scratch formulas (`scripts/verify_hand.py`). Every figure matches to the dollar (`data/verify_hand_out.txt`).
  3. A built-in accounting check also passes. Under option 1, total money with the lock minus total without equals the lock bond's 2031-33 return minus the stock return on the same dollars, to 1e-10 on every path (column "inv" in the outputs).
- **One accounting fix you should know about.** The red team's "L33" (`laura_free33`) leaves out the gift side's money above the cap, which belongs to Laura.
  - Under option 1 that omission is a mean of $4,856 (median $3,110). Under 3r it is $1,614 (`data/keptcheck_out.txt`).
  - "Kept" below uses the corrected figure: Laura's half less any payment set-aside, plus anything above the cap. So option 1's kept median here is $23,161, where the red team's L33 gives $20,451.

---

## 1. The asymmetry, in one picture
- **The 2033 rule:** gift = min(top, floor + half of VT).
- **A fall after 2031** lowers the gift.
- **A rise after 2031** lifts the gift only up to the top. Everything above it is Laura's.
- **Deterministic check** (stocks +7% a year to Jan 2031, then one 2031-33 return, yields unchanged; option 1). Top $170,274, bottom $145,000; the lock sells $18,496 of VT for a 4.757% two-year note repaying $20,274:

| 2031-33 stock return | Gift, no lock | Gift, full lock | Laura kept, no lock | Laura kept, full lock |
|---|---|---|---|---|
| −40% | $162,164 | **$170,274** | $12,164 | $13,231 |
| −20% | $166,219 | $170,274 | $16,219 | $17,641 |
| 0% | $170,274 | $170,274 | $20,274 | $22,051 |
| +14.5% (7%/yr) | $170,274 | $170,274 | $26,149 | $25,247 |
| +40% | $170,274 | $170,274 | $36,492 | **$30,872** |

- **Reading it.**
  - In falls, the lock protects the gift *and* leaves Laura slightly better off, because the money parked in a bond did not fall.
  - In rises, Laura gives up the stock gain on about $18.5k.
  - V5's line "a 40% fall in world stocks during 2032 lowers a typical contribution from $169,000 to $162,000" (`oct19/drive/ips_report_live.md:29`) matches the no-lock column ($170.3k → $162.2k on this basis).

---

## 2. Main table (19 Oct curve, Monte Carlo 100,000 paths, seed 20261019)

**Reading guide.**
- "Reach" = gift reaches the announced top. ">$5k" = gift ends more than $5k below the top. "Below bottom" = gift under the announced bottom (only payment set-asides can cause it).
- "Kept" = Laura's money left in Jan 2033 (corrected). "2042" = money returned to Laura after the last payment. "Short" = chance any payment is short by more than $100.
- "2031 trades" = expected orders in Laura's real plan that year.
- Cost columns are mean changes against (a) on the same paths.

### Option 1 (no reserve)

| Variant | Reach | >$5k | Below bottom | Gift p50 | Top p50 | Kept p5 / p50 | 2042 p50 | Short | 2031 trades | Mean Δ gift / Δ kept / Δ total | "2031: nothing traded" becomes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (a) plan, no lock | 68.4% | 7.9% | 1.95% | $166,177 | $166,996 | $4,812 / $23,161 | $8,024 | 15.6% (max $6.2k) | 0 | — | unchanged |
| (b) full lock | **88.3%** | 3.3% | 1.94% | $166,924 | $166,996 | $4,438 / $22,632 | $8,024 | 15.6% | 2 | +$728 / −$2,068 / −$1,340 | "sell the gift's promised share of VT, buy a Treasury maturing by Dec 2032" |
| (c) half lock | 77.2% | 3.7% | 1.94% | $166,720 | $166,996 | $4,607 / $22,738 | $8,024 | 15.6% | 2 | +$518 / −$1,188 / −$670 | same, half the amount |
| (d1) lock if VT ≥ its 2028 cost | 84.1% | 3.7% | 1.95% | $166,784 | $166,996 | $4,589 / $23,101 | $8,024 | 15.6% | 1.50 | +$619 / −$1,759 / −$1,141 | same, plus a trigger rule |
| (d2) lock if VT up ≥ 22.5% | 79.2% | 4.5% | 1.95% | $166,495 | $166,996 | $4,693 / $23,300 | $8,024 | 15.6% | 0.99 | +$458 / −$1,292 / −$834 | same, plus a trigger rule |
| (d3) lock if VT up ≥ 40% | 75.7% | 5.4% | 1.95% | $166,342 | $166,996 | $4,748 / $23,253 | $8,024 | 15.6% | 0.64 | +$328 / −$906 / −$578 | same, plus a trigger rule |
| (e1) narrower top (¾ of VT's half) | 90.4% | 3.4% | 2.37% | $162,357 | $162,436 | $7,229 / $27,422 | $8,024 | 15.6% | 0 | −$4,417 / +$4,417 / $0 | unchanged; top formula changes |
| (e2) narrower top (½ of VT's half) | 93.9% | 3.3% | 2.92% | $157,970 | $157,983 | $10,363 / $32,376 | $8,024 | 15.6% | 0 | −$9,486 / +$9,486 / $0 | unchanged; top formula changes |

### 3r ($10k Nov-2041 reserve, top counts $5k of it: the red team's fix)

| Variant | Reach | >$5k | Below bottom | Gift p50 | Top p50 | Kept p5 / p50 | 2042 p50 | Short | 2031 trades | Mean Δ gift / Δ kept / Δ total |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) plan, no lock | 73.0% | 7.4% | 0.10% | $160,160 | $160,807 | $8,421 / $20,759 | $24,005 | 0.02% (max $613) | 0 | — |
| (b) full lock | 77.1% | 6.1% | 0.10% | $160,220 | $160,807 | $8,402 / $20,473 | $23,874 | 0.02% | 2 | +$71 / −$1,496 / −$1,067 |
| (c) half lock | 77.0% | 5.7% | 0.10% | $160,313 | $160,807 | $8,405 / $20,495 | $24,216 | 0.02% | 2 | +$174 / −$976 / −$494 |
| (d1) lock if VT ≥ 2028 cost | 76.4% | 5.9% | 0.10% | $160,194 | $160,807 | $8,405 / $20,622 | $24,045 | 0.02% | 1.51 | +$88 / −$1,354 / −$861 |
| (d2) lock if VT up ≥ 22.5% | 75.5% | 6.0% | 0.10% | $160,150 | $160,807 | $8,408 / $20,695 | $24,192 | 0.02% | 1.00 | +$88 / −$1,063 / −$591 |
| (d3) lock if VT up ≥ 40% | 74.7% | 6.2% | 0.10% | $160,165 | $160,807 | $8,416 / $20,728 | $24,216 | 0.02% | 0.64 | +$81 / −$783 / −$389 |
| (e1) narrower top (¾) | 89.1% | 1.3% | 0.13% | $156,442 | $156,579 | $8,528 / $22,531 | $27,395 | 0.02% | 0 | −$4,090 / +$2,494 / +$1,069 |
| (e2) narrower top (½) | 96.1% | 0.3% | 0.17% | $152,429 | $152,442 | $8,880 / $26,828 | $28,623 | 0.02% | 0 | −$8,659 / +$6,467 / +$1,453 |

**Also tested, no gain.** "Lock everything above the announced *bottom*" (b2) reaches 87.7% under option 1 and 76.9% under 3r. It is capped by the gift's half of VT, so it cannot do better than (b).

**What changes and what does not.**
- **Payments are untouched.** No lock or narrower top changes payment shortfalls (15.6% under option 1, 0.02% under 3r) or the 2042 money under option 1. The lock never touches Laura's half or the post-2033 cover chain.
- **Source:** `data/lockin_19oct_s20261019.txt` and `.json`.

---

## 3. Robustness (reach top / gift more than $5k below top)

| Variant | MC seed 20261019 | MC seed 7 | MC, stock-yield corr +0.5 | Bootstrap 20k | Bootstrap, seed 7 | History 690 windows |
|---|---|---|---|---|---|---|
| Opt 1 (a) | 68.4 / 7.9 | 68.4 / 7.8 | 66.9 / 9.2 | 71.3 / 9.1 | 70.8 / 9.2 | 80.0 / 9.6 |
| Opt 1 (b) full lock | 88.3 / 3.3 | 88.1 / 3.4 | 86.4 / 4.5 | 81.4 / 4.5 | 81.0 / 4.8 | **80.0 / 3.2** |
| Opt 1 (c) half | 77.2 / 3.7 | 77.2 / 3.7 | 75.7 / 4.9 | 77.6 / 5.2 | 77.6 / 5.3 | 81.9 / 3.9 |
| Opt 1 (d1) trigger | 84.1 / 3.7 | 84.0 / 3.8 | 84.0 / 5.1 | 80.5 / 5.0 | 79.9 / 5.2 | 83.9 / 3.2 |
| Opt 1 (e1) narrower | 90.4 / 3.4 | 90.4 / 3.5 | 88.9 / 4.6 | 88.8 / 4.9 | 88.7 / 5.0 | 89.1 / 3.3 |
| 3r (a) | 73.0 / 7.4 | 73.2 / 7.3 | 73.9 / 8.0 | 73.0 / 7.9 | 72.9 / 7.9 | 73.5 / 5.5 |
| 3r (b) full lock | 77.1 / 6.1 | 77.1 / 6.0 | 77.0 / 6.6 | 75.3 / 9.5 | 75.3 / 9.6 | **68.0 / 12.0** |
| 3r (c) half | 77.0 / 5.7 | 77.3 / 5.6 | 77.5 / 6.5 | 75.5 / 6.8 | 75.5 / 6.8 | 74.2 / 5.7 |
| 3r (e1) narrower | 89.1 / 1.3 | 89.1 / 1.3 | 87.6 / 1.8 | 88.3 / 2.5 | 88.0 / 2.5 | 89.3 / 3.2 |

**Mean change in total money from the full lock (option 1):**

| Basis | Change |
|---|---|
| Monte Carlo | −$1,340 (seed 7: −$1,356) |
| Bootstrap | −$1,159 |
| History | −$2,633 |

**The history windows overlap.** They hold only about 36 non-overlapping two-year 2031-33 periods (`history_nonoverlap_2y_windows_2031_33`).

---

## 4. Why the lock helps less than "close to certain"
There are three separate reasons a gift misses the top. The lock fixes only the first (`data/diag_out.txt`, MC):

| Cause | Option 1, no lock | Option 1, full lock | 3r, no lock | 3r, full lock |
|---|---|---|---|---|
| Stocks fell after 2031 (gift-side assets short) | 25.5% | 5.6% (median miss $412) | 26.2% | 22.1% (median $4.3k) |
| Yields fell, and the 2033 payment set-aside took money from the gift | 6.1% | 6.1% | 0.9% | 0.9% |
| **Total misses** | 31.6% | 11.7% | 27.1% | 22.9% |

1. **Stock risk.** The lock removes most of it under option 1.
2. **Rate risk.** If yields fall between 2031 and 2033, the 2033 projection needs more for the payments, and the cover chain takes it from Laura's half first, then from the gift (`oct19/coupon/coupon_risk_options.md`, option 1 chain). The lock cannot stop that: the locked note is sold for the payments like any other gift money.
   - The worst historical misses are all of this kind. Plan-2031 dates from Oct 1985 to Jul 1988 (falling yields) give a gift of about $96-109k against tops of $123-132k, *identical* with and without the lock (`history_worst_gap_opt1`).
   - This is what 3r is for: 6.1% falls to 0.9%.
3. **The floor fund's payout and the reserve's share.**
   - Under option 1, the small leftover misses (median $412) come from IBTM paying out a little under its target when yields fall. That is the same reason the bottom is rounded down.
   - Under 3r, the top counts $5k of the reserve. When the 2033 release rule holds that money back for the payments, the top is missed by about $4-5k, whatever was locked.
   - On history the lock makes this worse. Without a lock, strong 2031-33 stock gains on the gift's half often filled that $5k. With a lock there is almost nothing left in stocks to fill it.

**Plain English:** "the lock turns stock risk into certainty, but the top also depends on interest rates and on the reserve, and the lock does nothing for those."

---

## 5. What a co-sponsor gains, what Laura loses (option 1, full lock)
**Co-sponsor gains**
- **The top becomes much more likely.** The chance the gift reaches the announced top goes from about 2 in 3 to about 9 in 10 (MC). On the bootstrap it goes from 7 in 10 to 8 in 10.
- **Fewer big misses.** Ending more than $5k below the top falls from about 8% to about 3%.
- **A 2032 crash stops mattering.** A 40% fall during 2032 no longer moves the gift ($162k → $170k in the deterministic case).
- **But "within the range" does not change** (98.1% both ways). On average the gift rises only $728, because most misses were small (median $2.7k).

**Laura loses**
- **The stock gain on about $18k.** The median amount sold is $17,770, held for two years. In the best 5% of paths she keeps at least $11.4k less in 2033.
  - The worst history window is a plan-2031 date of Mar 1985: VT +75% over 2031-33 costs her $22.9k (`history_worst_laura_cost_opt1`).
- **On average:** −$2,068 in kept money and −$1,340 in total money. The total loss is the expected extra return of stocks over two-year Treasuries on about $18k for two years.
- **In falling markets she gains a little** (+$1.1k to +$1.8k in the deterministic falls). She is better off in 40% of paths and worse off in 55%.
- **Ratio:** about $2.8 of Laura's expected money for each $1 of expected extra gift (MC). It is $3.0 on the bootstrap and $6.1 on history. Under 3r +$5k it is about $21.

**In one line:** the lock moves stock risk from the co-sponsors' side to Laura's, and charges Laura the stock premium on about $18k for two years. The capped design already gives co-sponsors the *range* the case asks for, and gives Laura the upside, which is the flexibility the case asks the team to protect (case:102-103, 145).

---

## 6. Trades, and the "2031: nothing traded" rule
- **Laura's real plan, counted as WInS-style orders:**
  - Jan 2027: 10 buys.
  - Jan 2028: 2 (IBTM, VT), or 3 with 3r (+ the Nov-2041 bond).
  - 2031: 0 under (a) and (e); 2 under (b) and (c), sell VT and buy the note; under (d), 0 or 2, expected 0.6-1.5.
  - 2033: the gift's VT sale gets smaller (or disappears) under (b).
- **Cost at WInS rates:** $25 for the VT sale plus $10 for a bond, or $25 for an IBTM purchase (commissions per `/home/user/caplet-investment/CLAUDE.md`, "Key facts"). That is $35-50, trivial.
- **WInS now:** no change and no trade.
  - The lock would be a 2031 action in Laura's real plan, and WInS freezes on 6 Nov 2026.
  - The WInS book already holds IBTM, so the vehicle is listed. A real 2032 note's availability in 2031 is UNVERIFIED.
- **How the rule changes:**
  - From "2031: nothing is traded; Laura announces what she owns" (`/home/user/snap/main/research/insight_v1/phase_E/E6_final_spec.md:59`; `ips_spec.md:118`, "Nothing traded").
  - To "2031: one switch, in a fixed amount, on the day the range is set" (b or c), or to a switch with a trigger (d).
  - (e) keeps the rule and changes only the top formula.

---

## 7. Conflicts with filed notes, the case, V5 and the September research
- **Filed WInS notes: no conflict.**
  - The VT note (7 Oct, 8:27 PM ET) says "A fall can shrink the extra, and a rise before 2031 lifts the top of the range co-sponsors hear". That stays true, since a lock acts only from 2031.
  - The IBTM note ("giving co-sponsors a minimum figure in 2031") is unchanged (`/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:14,19`).
  - Nothing filed is contradicted, and the TNA due 23 Oct is unaffected.
- **Case, credibility (case:114-116).**
  - The lock answers "promises more than she can ultimately contribute" only if co-sponsors hear the *top* as the promise.
  - The case asks for a range and a confidence that the gift falls *within* it (case:117-118). That is already about 98-99.9%.
  - A full lock makes the outcome close to one number. That sits awkwardly with presenting a wide range "because 2033 is uncertain" (case:112-113, 115-116). It is a tension, not a breach.
- **Case, flexibility (case:102-103, 145).** Laura's half is never touched. The cost is her expected upside: −$2.1k on average and −$11k or worse in strong markets. If adopted, the team would have to state this trade-off.
- **Case, payments (case:91-92, 119-120).** Unchanged in every variant.
- **V5 (`oct19/drive/ips_report_live.md:29`): if adopted, three statements would change:**
  1. "Her 2033 contribution is the floor plus half the fund, capped at the upper bound".
  2. "about three of four simulated paths" (it would be about 9 in 10 under option 1).
  3. The "40% fall ... $169,000 to $162,000" example (it would show no change).
  - Line 28, "Maturing bonds, not sales, supply every payment", still holds: the lock sells stock, for the gift, not a bond for a payment.
- **September research.**
  - ALT (E6:64-80, 480) was a different design: the 2031 lock *replaced* the 2028 floor, so its bottom depended on 2028-30 markets. The present lock keeps the 2028 floor, so that rejection does not apply directly.
  - The closer precedent is the rejected "Ratchet (lock in thirds, 2029-31): a second rule for $2-6k" (E6:488). These numbers say the same: a second rule for about $0.5-0.7k of expected gift.
  - The IPS spec also chose to word the top as "expected if stocks hold their value ... never 'promised'" (`ips_spec.md:118`). The design handled the asymmetry with words, at no cost, rather than with a trade.

---

## 8. Side finding for the 27 Oct vote: the top rule under 3r matters more than any lock
- **The red team recommended** counting $5k of the reserve in the 2031 top (`oct20/redteam3r/redteam_3r.md` §3b, §11 item 2).
- **What that does.** On these paths, the $5k is the main reason the gift misses the top under 3r (22% of paths, section 4).
- **Counting $0, no lock and no trade** (`data/lockin_extra_3r0k.txt`):

| Basis | Reach top | Gift median |
|---|---|---|
| Monte Carlo | **92.3%** | $155,684 |
| Bootstrap | 91.7% | $155,843 |
| History | 93.6% | $160,557 |

- **Why it works.** The 2033 release rule then uses the reserve to fill a stock-driven gap below the top. The reserve already acts as a lock-in.
- **The cost:** about $4.5k off the median gift against top +$5k (MC: $155.7k against $160.2k), and that money goes back to Laura.
- **Adding a lock** on top of 3r +$0 adds little: 92.3% → 93.6% (MC). On history it goes down: 93.6% → 87.1%.
- **For the team:** if a surer top matters, this is the lever to vote on, not a 2031 trade.

---

## 9. What this teaches (for Ray)
- **A cap moves risk; it does not remove it.** "Gift = floor + half, capped" means co-sponsors carry the stock falls after 2031 and Laura gets the stock rises. Total money is the same either way.
- **Locking costs about the stock premium on the amount locked.** Here that is roughly 2.2 points a year on about $18k for two years: about $1.3k expected. It is cheap in expectation but expensive in boom markets ($11-23k).
- **Know which risk a tool hedges.** The lock hedges stock risk. The 3r reserve hedges interest-rate risk. Neither does the other's job. The worst historical misses were rate-driven, and the lock changed none of them.
- **Read the question you are being graded on.** The case asks for confidence that the gift lands *within the range*, not *at the top*. A tool that improves a metric nobody asked for has to earn its complexity.
- **Promising less is the free hedge.** A narrower top buys the same certainty with no trade and no lost money. It just hands the money back to Laura instead of to the gift.

---

## 10. Decisions for the team (students decide; the AI only suggests)
1. **Keep "2031: nothing traded" in the IPS?**
   - Suggested: yes.
   - Numbers to weigh: option 1 lock 68% → 88% reach top, Laura −$2.1k on average and −$11k in boom markets, 2 trades; under 3r +$5k only 73% → 77%.
2. **The top rule** (links to red team decision 2 on 27 Oct): top +$5k (73% reach, gift median $160.2k), top +$0 (92%, $155.7k), or a narrower VT share. This is the real "how sure is the top" choice.
3. **Final Report "alternative we considered":** include the lock-in? The team writes it. Content it would need:
   - the asymmetry;
   - what a lock would buy (reach top, the 40%-fall example);
   - what it costs Laura (expected and boom-market);
   - why the case's "within the range" test did not need it;
   - the trade and rule it adds.
4. **Wording guard.** If the lock is mentioned at all, avoid "guaranteed top" or "locked contribution". A fall in yields can still cut the gift through the payment set-aside (6% of option 1 paths).

---

## 11. Limits and UNVERIFIED
- **Same model family as the coupon study and the red team.** One curve plus shifts, no roll-down, lognormal or bootstrapped stocks, no taxes, no costs outside WInS.
  - Selling VT in 2031 could realise a taxable gain in a real account. Taxes are out of scope per the case and were not modelled.
- **The lock is modelled at one date** (1 Jan 2031). It is a par note maturing 15 Dec 2032 at the base 2-year yield (4.757% on the 19 Oct curve) plus the path shift, with coupons reinvested on the path.
  - Real 2-year notes mature at month-end. Which issue would be available in 2031 is UNVERIFIED.
  - IBTM would behave much the same, but its payout is not fixed.
- **Funding.** The lock is funded only from the gift's half of VT. Funding from Laura's half, or locking the reserve's $5k, was not tested beyond (b2).
- **Triggers** are tested at Jan 2031 only. A rolling 2031-33 trigger, a stop-loss after falls (which sells low), was not tested.
- **Corrected definition.** "Kept" corrects the red team's L33 (section 0). Red-team tables that compare Laura's 2033 money understate option 1 by about $3-5k. The red team's gift, top, shortfall and 2042 figures are unaffected.
- **History** is 690 overlapping windows, about 36 independent two-year 2031-33 periods. The bootstrap re-centres stock returns to 7%.

---

## 12. Reproduce (from `oct20/lockin/scripts/`, with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`)
- `validate_lock.py ../../redteam3r/data/tsy_202610_fetch20oct.csv 10/19/2026 20261019` (and the `tsy_202610.csv` with `10/16/2026`) produce `data/validate_lock_*.txt`.
- `run_lockin.py ../../redteam3r/data/tsy_202610_fetch20oct.csv 10/19/2026 20261019 ../data/lockin_19oct_s20261019.json all` produces the `.txt` and `.json` outputs. With seed `7` it gives the second pass. Adding the extra argument `extra` gives the 3r +$0 side test.
- `diag.py <curve> 10/19/2026 20261019` (miss causes), `verify_hand.py <curve> 10/19/2026 ../data/lockin_19oct_s20261019.json` (hand check), and `keptcheck.py <curve> 10/19/2026` (the L33 gap).
- `dbg.py` was used for debugging only.
