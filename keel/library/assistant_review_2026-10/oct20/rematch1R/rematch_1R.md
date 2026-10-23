# Option 1R with a real 2033 re-match: what it costs, and 3r vs 1R vs both

> **Verified 20 Oct (`oct20/verify_rematch/verify_rematch.md`): main numbers and ranking confirmed (1R ~8x worse than 3r for the minimum; BOTH 0% short).** Corrections: "Laura 2042 -$13k" under BOTH is bookkeeping (0% cash vs market reinvestment); credited the same way it is about -$2k. The LP understates the re-match: realistic book premium +$4.0k median / +$7.5k 1-in-20, BOTH top-reach ~76% (not 80%). RM:191 is wrong for cost: at today's T-bill rates the buy-only top-up at unchanged yields is ~$0. Nov-2033/34/35 notes exist; Nov-2036/37/38 do not yet (trim/full depend on them; reject both). Patch LP:143 (iBond coupon bug) before quoting. **Consistency fix 20 Oct (packaudit §1d):** 3r = about 0.6% short on the agreed engine (0.08/0.32/0.72% marked at market); never quote 0.02%; the 0.02% figures below are study-engine, at-cost. BOTH has no top-reach advantage (about the same, 73-77%, as 3r-fix; verify_engine3).

AI-generated research for Team Caplet, Tue 20 Oct 2026 (Sydney). Claude Code wrote this. These are MODEL numbers for the Tue 27 Oct vote. They are not text to submit. If the team uses any of it, log it in the AI-use record and later in the Final Report's Works Cited (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).

Paths: `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/`. My folder is `oct20/rematch1R/`: scripts in `scripts/`, every output in `toolkit/data/`.

---

## Verdict: BOTH, in a specific form. Fallback: 3r-fixed. Not 1R on its own.

1. **The red team's unknown is now measured, and it is small.** I built a proper Jan-2033 re-match: a linear programme that re-sizes the Treasuries so each 2034-2042 payment is met by cash arriving in the 12 months before it, with nothing ever reinvested. On 100,000 paths it costs only a little more than the red team's "frozen" estimate:
   - **Keep everything and only buy** ("buy-only"): +$2.1k at the median and +$5.8k at the 1-in-20 high. It needs 1-2 trades.
   - **Sell parts of IBTO-IBTR** ("trim"): +$0.4k / +$2.6k. It needs 9 trades.
   - So 1R's "0% short" is real. Payments were never short in any run: both seeds, both curves, bootstrap, history, correlation +0.5 and every cost and curve sensitivity.
2. **But 1R on its own moves the risk onto the minimum Laura announces to co-sponsors.** The re-match is paid from Laura's stock half first, then from the gift.
   - The gift falls below the announced minimum in **1.2% of paths, against 0.11% for 3r**. With stocks and yields falling together it is 1.8-1.9% against 0.19%. On the bootstrap it is 2.3% against 1.0%.
   - Laura's own money is much thinner. In the worst 1 path in 20 she keeps $1.3k (buy-only), against $13.0k under 3r.
   - The case warns that over-promising "could damage her credibility" (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:115`). It also says the range "must also protect the portfolio's ability to fund" the payments (`:119-120`).
3. **BOTH works best.** Keep 3r's $10k Nov-41 reserve from the 2028 deposit, with the top counting $5k. Then in Jan 2033 replace 3r's release rule ("projected need + $5k margin") with one buy-only re-match. Fund it from the leftover first, then the reserve. Release whatever is left of the reserve to the gift, up to the top.
   - Against 3r-fixed on the same 30,000 paths, BOTH gives payments short 0% (3r: 0.03%), with the same minimum protection (gift below the minimum 0.16% vs 0.15%).
   - The gift reaches the 2031 top in **80% of paths instead of 72%**. The gift median is about $0.3k higher.
   - The cost is Laura's 2042 money: $9.7k median instead of $22.5k. That is about $13k in 2042 dollars, or roughly $8k in 2033 money (APPROXIMATE).
   - That is the price of the last 0.02-0.3% of payment certainty (0.02% model, 0.18% bootstrap, 0.29% history) and of a gift that reaches the top more often. The team should vote on that trade knowingly.
   - The re-match turns the reserve's guessed $5k margin into an exact calculation. That is why more of the reserve can be released.
4. **For the IPS this changes almost nothing.** The 2028 step, the minimum ($135k), the WInS book and the filed notes are all as in 3r-fixed. The only addition is one 2033 rule. The case invites it: "explain how its composition should change, if at all" (`Laura_Gao_2026_Client_Profile.txt:96`).
   - If the team finds BOTH too complex, 3r-fixed is still a sound plan. The gap between them is small: 0.02% vs 0% of paths, and 72% vs 80% reach-top.
5. **Do not use the full re-match.** It sells about 60% of the book in 11 trades. It is not "held to maturity". Its apparent cheapness is mostly an artefact of the 0% waiting-cash assumption (section 4).

---

## 1. What I built, and checks that it is faithful

**The engine and paths: the red team's own.**
- My folder holds copies of `rt_engine.py`, `coupon_options.py` and `indep_pricer.py`.
- With the new code switched off, my copy reproduces the red team's baseline **exactly**: a byte-identical diff of `validate.py` output against `oct20/redteam3r/data/validate_out.txt`, re-run after every patch (`data/validate_out_final.txt`):
  - option 1: 16.45% short, worst $6,121;
  - 3r: 0.02% short, gift median $162,190.
- The two additions are clearly marked branches in `run2`: "1RLP" and "BOTH". Every other line is unchanged.
- **Basis:** as the study and the red team: 16 Oct curve held to 1 Jan 2027; seed 20261019; 100,000 paths; waiting cash at 0%; parallel random walk at 1.0 point a year, floor 0.25%; VT at 7% compound with 16.78% volatility.

**The LP (`scripts/rematch_lp.py`). One run per path on 1 Jan 2033.** It is also run as projected on 1 Jan 2031 with yields frozen, which sets the 2031 top in the same way as option 1.
- **The book.** The nine remaining rungs use the engine's own faces and coupons, plus the engine's pre-2033 reinvested coupons. IBTM has already paid, so its gap or surplus against the 2033 payment is cash.
- **Prices.** "Engine-consistent" curve: each maturity date keeps its 2027 yield plus that path's change. These are exactly the yields the engine reinvests at, floored at 0.25%.
  - Sensitivity: today's curve shape at 2033 tenors (roll-down).
- **What it may buy.** Only instruments that plausibly exist in 2033 (universe "B"):
  - more of the nine held rungs;
  - Treasury notes maturing 15 Nov 2033-2041 at a par coupon. These are 10-year notes issued Nov 2023-Nov 2031; their future issuance is UNVERIFIED but routine.
  - Universe "A" also allows new iBond-type funds for Dec 2037-41. That is UNVERIFIED: the filed Nov-41 note says there are "no iBonds Treasury funds maturing in 2037-43" (`oct19/drive/ips_report_live.md:117`).
- **The rule it must meet.** Cash arriving in each 12-month window (after 1 Jan of the previous year, up to 1 Jan) must cover that payment. Any surplus carries forward at 0%. Nothing is reinvested, so after the re-match no rate move can make a payment short.
- **Costs** (all added to the 2033 cost):
  - bid-ask: base **0.10% each way**, stress 0.50%. Both are UNVERIFIED retail assumptions;
  - **$10 per bond ticket and $25 per fund ticket**, as a WInS-like proxy;
  - buys rounded up to $1,000 face (bonds) or one ~$25 share (funds). The extra face is a 2033 cost; its later cash is credited to Laura in 2042;
  - trades under $100 are ignored.
- **Three forms:**
  - **full**: may sell any holding;
  - **trim**: may sell only IBTO-IBTR;
  - **buy-only**: sells nothing.

**Independent check (`scripts/verify_lp.py` → `data/verify_lp_out.txt`).** Each re-matched portfolio's cash flows were rebuilt date by date, without using the LP's matrices, for 300 paths and all three forms:
- every 2034-2042 payment is met (worst surplus after a payment: $0.00);
- the longest wait is 0.88 years;
- the LP cost is never below the perfect-zero-coupon lower bound;
- IBTM's delivery matches the engine to $0.00000000001.

**Checked twice.** Every headline number was re-run with seed 7 (`data/r1_seed7_16oct_stdout.txt`) and on the **19 Oct 2026 curve** (`oct20/redteam3r/data/tsy_202610_fetch20oct.csv`, ladder $298,446; `data/r1_19oct_stdout.txt`). Conclusions are unchanged (table 3).

---

## 2. The comparison: row for row on the same 100,000 paths

Basis: 16 Oct curve, seed 20261019, 100,000 parallel random-walk paths. "Short" = some payment is short by more than $100. "Below min" = the gift is below the announced 2031 minimum. "Below net min" = below the minimum after the net-minimum rule. Laura's money: "2033" = her half left free in 2033; "2042" = what returns to her in 2042. Each figure is a median; medians do not add up.

| Option | Short | Worst short | 2033 re-match cost: median / 1-in-20 high | Minimum | Gift median | Gift 1-in-20 low | Gift reaches top | Below min / below net min | Laura 2033 / 2042 / total | Trades in 2033 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 state only | 16.45% | $6,121 | — | $145k | $165.3k | $135.8k | 68.1% | 2.15% / 0.59% | $19.9k / $7.0k / $30.2k | 0 |
| **3r $10k, top +$5k (red-team fix)** | **0.02%** | $666 | — (release rule) | $135k | **$159.2k** | $132.5k | 71.7% | **0.11% / 0.01%** | $20.1k / **$22.8k** / **$44.2k** | about 1 (reserve sale) |
| 1R as the red team modelled it (frozen) | 0% | $0 | $0 premium (assumed) | $135k | $165.3k | $135.8k | 68.1% | 1.00% / 0.06% | $19.9k / $7.0k / $30.1k | not modelled |
| **1R-LP buy-only** | **0%** | $0 | **$5.5k / $21.7k** (premium over frozen: +$2.1k / +$5.8k) | $135k | **$165.2k** | $134.8k | 67.1% | **1.16% / 0.08%** | $18.6k / **$1.7k** / $23.2k | **1 (2 at 1-in-20; max 4)** |
| 1R-LP trim | 0% | $0 | $2.2k / $22.1k (+$0.4k / +$2.6k) | $135k | $165.2k | $135.1k | 67.6% | 1.21% / 0.11% | $19.5k / $6.3k / $29.0k | 9 |
| 1R-LP full | 0% | $0 | $0.2k / $21.9k (−$1.4k / +$1.6k) | $135k | $165.2k | $135.6k | 68.0% | 1.13% / 0.12% | $19.9k / $8.3k / $31.1k | 11 (60% of the book) |

**BOTH** (first 30,000 of the same paths; `data/r1_extra_16oct_stdout.txt`). 3r on those same paths: 0.03% short, gift median $159.1k, reaches top 71.8%, below min 0.15%, Laura total $43.9k.

| Option | Short | Gift median | Gift 1-in-20 | Reaches top | Below min / net | Laura 2033 / 2042 / total |
|---|---|---|---|---|---|---|
| **BOTH: 3r $10k (top +$5k) + buy-only re-match in 2033** | **0%** | $159.3k | $132.7k | **80.2%** | **0.16% / 0.03%** | $19.8k / $9.7k / $31.5k |
| BOTH: 3r $10k (top +$5k) + trim re-match | 0% | $159.5k | $132.9k | 83.9% | 0.20% / 0.03% | $19.9k / $15.8k / $37.1k |
| BOTH with a $5k reserve (top +$0), buy-only | 0% | $160.2k | $132.9k | 84.8% | 1.03% / 0.25% | $19.8k / $5.5k / $28.1k (minimum $140k) |

**What the tables say:**
- **Payments.** Every re-match row is 0% short. 3r is 0.02%. The difference is real but tiny.
- **The minimum.** 1R alone breaks the announced minimum about 10 times as often as 3r: 1.2% vs 0.11%. With the net-minimum rule it is 0.08-0.12% vs 0.01%.
  - The cause is that 1R's top-up is drawn from Laura's stock half first. In a stock crash that half is small, so the top-up comes out of the gift.
  - The $10k cut to the minimum is still needed: with no cut, 1R-LP breaks the minimum in 2.3-2.6% of paths (`data/r1_base_16oct_stdout.txt`).
- **Who carries the cost.** 3r costs the gift about $6k at the median and gives Laura about $14-21k more in 2042. 1R keeps the gift and costs Laura, mostly in 2042.
- **BOTH sits between them.** It gives 3r's gift and minimum protection, a higher top-reach than either, payments 0%, and about $13k less to Laura in 2042 than 3r.
- **Totals across different years.** Adding the gift and Laura's money mixes 2033 dollars with 2042 dollars. 3r's 2042 dollars include 9 years of locked interest.
  - Discounting 2042 money roughly at 5% a year (factor about 0.64; APPROXIMATE, built from medians), the gift plus Laura's money is about:
    - **3r: $194k**;
    - 1R full: $190k;
    - option 1: $190k;
    - 1R trim: $189k (BOTH trim about the same);
    - BOTH buy-only: $185k;
    - 1R buy-only: $185k.
  - So the choice is mostly about **who** carries the risk.
  - But a re-match is not free. Its insurance premium (about $2-6k) and the reinvestment upside it gives up after 2033 are real money. 3r keeps the most in total, because its reserve earns a locked long yield to 2041.

### What the re-match costs, by where yields are in Jan 2033 (buy-only; 100k paths; `data/r1_base_16oct.json`)

| Change in yields by Jan 2033 | Share of paths | Frozen estimate (red team) | Real buy-only cost | Premium |
|---|---|---|---|---|
| more than 3 points lower | 11% | $19.0k | $20.4k | +$1.1k |
| 1.5-3 lower | 16% | $10.1k | $13.1k | +$2.5k |
| 0.5-1.5 lower | 15% | $4.3k | $8.4k | +$3.7k |
| about unchanged (±0.5) | 16% | $0 | $5.7k | **+$4.2k** |
| 0.5-1.5 higher | 15% | $0 | $3.0k | +$3.0k |
| 1.5-3 higher | 16% | $0 | $0.3k | +$0.3k |
| more than 3 higher | 12% | $0 | −$0.6k (surplus) | −$0.6k |

- **The re-match is insurance.** It costs most when nothing happens.
- **At unchanged yields** it costs $5.9k. That is the red team's naive $6.8k estimate (`oct20/redteam3r/data/rematch_cost_out.txt`), done properly. The trim form costs $2.2k and the full form $0.1k.
- **The worst 2033 cost** is about $43k (1-in-100: $30k). Nearly all of that is the frozen shortfall every option faces when yields have fallen far before 2033, not a re-match premium.

### Deterministic cases: yields move once in Feb 2027 and stay there (`scripts/det_shifts.py` → `data/det_shifts_out.txt`)
The 2033 re-match cost, with the frozen estimate for comparison. Costs are on the 16 Oct curve; the 19 Oct curve is within $50 in every cell.

| Permanent shift | Frozen estimate (= option 1's shortfall) | Buy-only | Trim | Full |
|---|---|---|---|---|
| −2 points | $18.9k | $20.5k (2 trades) | $19.7k (9) | $18.3k (11) |
| −1 point | $9.5k | $13.4k (2) | $10.4k (9) | $8.2k (11) |
| 0 | $0 | $5.9k (1) | $2.2k (9) | $0.1k (11) |
| +1 point | $0 | −$0.5k (0 trades: surplus) | −$6.3k (8) | −$8.4k (11) |
| +2 points | $0 | −$0.9k (0) | −$14.2k (8) | −$15.3k (11) |

A negative cost is money released. Buy-only cannot release, because it sells nothing. Its surplus stays in the bonds and reaches Laura in 2042.

### Reconciliation with the agreed numbers (`oct20/reconcile3r/reconcile_3r.md` §5)
- **Different engine, different numbers.** The agreed basis uses the 19 Oct curve, engY pricing and the plan read as written: option 1 is 14.5% short (seed 7: 14.4%); 3r 0.63% (0.64% with the top fix); top reached 77% / 45% / 76%.
- **My engine is the red team's study engine:** 16.45% / 0.02%; top reached 68% / 41% / 72%.
  - §5's own "same rules in the study engine" row gives 3r 0.010% and top reached 73%, the same low end as mine.
- **I did NOT run the LP inside the engY engine.** There was not enough time. 1R's figures on the agreed basis are UNVERIFIED.
- **What should still hold there:**
  - After the re-match nothing is reinvested, so 1R and BOTH stay at 0% short there too. The only way to be short is that the funding chain runs dry, which never happened in any run here.
  - The extra cost over the frozen estimate is mainly about the timing of coupons against the holding. That should carry over approximately: buy-only about +$2k median and +$6k at the 1-in-20 high.
- **On the agreed basis the case for a 2033 re-match is stronger.** There 3r alone is short in about 0.6% of paths (worst $3.3k), against 0.02% here. BOTH would remove that.
- **Expect the minimum gap to persist.** The agreed basis puts gift below the minimum at 0.01-0.04% for every option. The comparison of 1R against 3r on that measure has to be re-run on engY before it is quoted.
- **For the vote pack.** Replace "1R's cost UNVERIFIED" (`oct20/votepack/votepack.md:38, 151, 162`) with "about $2-6k above the frozen estimate (buy-only, 1-2 trades in 2033) on the study engine; not yet run on the agreed engine".

---

## 3. Robustness: does 1R stay at 0%, and does its minimum weakness persist?

Payments short / gift below the announced minimum. The 1R columns use the minimum cut by $10k.

| Run | 1 | 3r +$5k | 1R buy-only | 1R trim | BOTH buy-only |
|---|---|---|---|---|---|
| MC 100k, seed 20261019 (base) | 16.45% / 2.15% | 0.02% / 0.11% | 0% / 1.16% | 0% / 1.21% | 0% / 0.16% (30k) |
| **MC 100k, seed 7** | 16.42% / 2.28% | 0.01% / 0.14% | 0% / 1.23% | 0% / 1.29% | — |
| **MC 100k, 19 Oct curve** | 15.58% / 1.95% | 0.02% / 0.10% | 0% / 1.03% | 0% / 1.10% | — |
| MC 30k, stocks and yields fall together (+0.5) | 16.50% / 3.20% | 0.03% / 0.19% | 0% / 1.76% | 0% / 1.88% | 0% / 0.26% |
| Block bootstrap 20k, real-curve twists | 15.16% / 3.51% | 0.18% / 0.97% | 0% / 2.31% | 0% / 2.36% | 0% / 1.01% |
| History, 690 overlapping windows (about 4 independent), real curves | 25.5% / 3.62% | 0.29% / 1.74% | 0% / 2.46% | 0% / 2.46% | 0% / 1.74% |
| MC 50k, bid-ask 0.50% each way | 16.56% / 2.14% | 0.03% / 0.11% | 0% / 1.18% | 0% / 1.24% | — |
| MC 50k, 2033 curve = today's shape (roll-down) | same as above | same | 0% / 1.22% | 0% / 1.34% | — |

**Notes on the runs:**
- **Re-match premium over the frozen estimate**, median / 1-in-20 high:
  - buy-only: +$2.1k / +$5.8k on every MC run (both seeds, both curves, both bid-ask levels and both curve bases); +$1.5k / +$5.9k on the bootstrap; +$1.6k / +$5.4k in history;
  - trim: +$0.3k-0.8k / +$2.6k-3.3k.
- **Bid-ask** at 0.50% adds about $40 to buy-only and about $900 to the full re-match.
- **Universe A** (new iBond funds, UNVERIFIED) only makes the *full* re-match cheaper (−$2.5k median). It needs 14 trades and 103% turnover.
- **Worst history window for the 2033 cost:** start Jul 1984 (yields fall about 5 points): $38-40k, paid without a short payment.
- Sources: `data/r1_*_stdout.txt` and `data/r1_extra_16oct_stdout.txt`.

---

## 4. Is 1R still "held to maturity"? How many trades does it need?

At unchanged yields, 16 Oct curve (`scripts/run_1r.py`, deterministic scenario "0"; trade lists from the LP):

| Form | 2033 trades | Share of the book traded | Is "held to maturity" true? |
|---|---|---|---|
| **buy-only** | **1** (buy about 7 more of the 3.125% Nov-41, about $5.4k); 2 when yields have fallen (adds a Nov-40 note); at most 4 | 1-5% | **Yes.** Nothing is sold. V5's "Bonds are held to maturity ... a maturity, not a sale" (`oct19/drive/ips_report_live.md:28`) and "the operating reserve remains invested to maturity" (`:45`) still hold. |
| trim | 9: sell parts of IBTO, IBTP, IBTQ and IBTR (about $26k); buy more Nov-39/40/41 and small Nov-37/38 notes | about 14% | **Partly.** Between 7% and 30% of each of the four fund positions is sold years early. The "not a sale" line would need an exception. |
| full | 11: also sells the **whole** Feb-37 and May-38 positions, replaced by new Nov-37/Nov-38 notes | about 60% | **No.** It is a rebuild, not a top-up. |

**Why the full form looks cheap, and why not to trust it.**
- With waiting cash at 0%, a bond maturing in Feb 2037 for a Jan 2038 payment wastes 10.5 months of interest. The LP "earns" that by swapping into a Nov note.
- With waiting cash in T-bills, which the filed Feb-37 note says ("held in a short-term Treasury ETF", `ips_report_live.md:109`), most of that gain disappears. What remains is turnover and tickets.
- Trim and buy-only do not depend on this artefact.

**In WInS.** None of this happens in WInS. It is a 2033 action, after the 6 Nov freeze. No new WInS trade and no new trade note is needed for 1R. BOTH needs only what 3r already needs: the red team's option A or B (`oct20/redteam3r/redteam_3r.md` section 8).

**Who does it.** In real life it is a January 2033 decision with Laura, one or two orders. The "only Ray trades" rule covers WInS only.

---

## 5. How it would have to be described: requirements, not wording

**The IPS (principle only; no figures or citations).** The IPS asks for "the strategy and decision-making framework ... rather than ... detailed financial calculations" (`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt:51-52`), and it bans citations and charts (`:123`). For BOTH, the principle must cover four things in the students' own words:
1. **What happens.** A one-time 2033 action: when the operating reserve is set, the Treasuries are topped up once, so each remaining payment is covered by cash arriving within the year before it. After that, nothing depends on reinvesting income.
2. **Where the money comes from.** In this order: the 2027 leftover, then the reinvestment reserve, then Laura's half, then the gift above the floor. What is left of the reserve goes to the contribution, up to the announced top.
3. **"Held to maturity" still holds.** The top-up only adds bonds. The reserve is the one holding that may be sold.
4. **The certainty definition changes slightly.** Before 2033, certainty rests on the reserve. After the 2033 top-up, it rests only on the US government paying. This replaces V5's "covered at purchase" (`ips_report_live.md:25`).

For 1R alone, drop the reserve parts. Then say plainly that the cost of the top-up falls on Laura's half first and then on the gift, which is why the minimum is cut.

**Do not put in the IPS:** the LP, the instrument list, the $5.5k figure, percentages of paths or bid-ask assumptions. They break the IPS rules above and use up the ~470-word budget (`oct19/ipskit/ips_writing_kit.md:56`).

**The Final Report (evidence goes here).** It should contain:
- the method in one paragraph: a cash-flow-matching LP, windows of a year or less, waiting cash at 0%, instruments limited to Treasury notes that will exist;
- the 2033 cost distribution (section 2) and the 2033 trades (section 4);
- the comparison table on one basis (section 2);
- the four stated assumptions: 0% waiting cash, the bid-ask level (UNVERIFIED), the curve basis, and the model family;
- why not the full re-match (turnover; the 0%-waiting artefact);
- the AI-use citation.
- It is also a good "how the composition changes" answer for the Client Knowledge and Portfolio Analysis criteria.

**Do not claim:**
- "zero risk": the re-match removes reinvestment risk after 2033 only;
- that the re-match is free: it is about $2-6k of insurance at the median;
- that 1R alone protects the minimum as well as 3r: about 10 times worse in the model.

---

## 6. What this teaches (for Ray)

**Locking costs most when nothing happens.**
- Buying certainty in 2033 is like insurance. The premium is highest when yields end up unchanged: about $4k over the frozen estimate. It is almost nothing when yields have already crashed or soared.

**Where the risk goes.**
- Any plan that "tops up later" protects the payments by spending whatever is left over at that time.
- Laura's stock half is smallest exactly when stocks have crashed. So "top up later" quietly moves the risk onto the co-sponsor promise.
- A reserve set aside in advance (3r) protects that promise, because its money is already there.
- The best plan uses both: set aside a little early, then do the exact sum once in 2033. Then the guessed safety margin is no longer needed.

**A cheap answer can be a modelling artefact.**
- The LP liked selling bonds that mature months before their payment, only because the model pays 0% on waiting cash.
- When an optimiser loves a trade, check which assumption it is exploiting.

---

## 7. Decisions for the Tue 27 Oct vote (student decisions; AI suggests, the team decides)

1. **Family.**
   - (a) 3r-fixed (red team);
   - (b) 1R alone, with no 2028 reserve and the minimum cut $10k;
   - (c) **BOTH**: 3r's reserve plus a once-only 2033 top-up replacing the "+$5k margin" release rule.
   - AI suggestion: (c). It pays every payment in every test and keeps 3r's minimum protection. Its price is about $13k of Laura's 2042 money at the median (about $8k in 2033 money).
   - Fallback (a), if the team prefers simplicity and more money for Laura.
   - Reject (b) unless the team decides the 2031 promise matters less than a $6k bigger median gift.
2. **If any 2033 re-match: which form?** AI suggestion: **buy-only**. It needs 1-2 trades and keeps "held to maturity". Trim releases about $3.5k more at the median but needs 9 trades and sells fund shares early. Do not use the full form.
3. **The top rule.** Keep "the top counts $5k of the reserve" under BOTH, as in 3r-fixed. BOTH then reaches the top in about 80% of paths. Would V5's "about three of four" become "about four of five"? That is the team's call, on one stated basis.
4. **Reserve size.** Keep $10k. A $5k reserve under BOTH raises the minimum to $140k but breaks it in about 1.0% of paths (vs 0.16%).
5. **Waiting cash.** State that the sizing assumes waiting cash earns 0%, and that T-bill interest is a bonus. This matters more under a re-match, because the full-form "saving" comes from that assumption.
6. **No WInS action follows from this file.** The WInS choice (red team option A or B by 6 Nov) is unchanged.

---

## 8. Limits and UNVERIFIED

**The model family is the study's.**
- One yield per maturity plus parallel or six-node shifts.
- iBond funds treated as semiannual par bonds.
- Stocks lognormal or bootstrapped.
- No taxes.
- The engine's convention that pre-2033 reinvested coupons are fixed amounts paid at the rung's maturity is kept in the LP.

**The 2033 curve is an assumption.**
- Base: maturity-date yields plus the path's change (engine-consistent).
- Roll-down sensitivity: today's shape at 2033 tenors. It gives the same conclusions: buy-only premium +$2.2k median.

**UNVERIFIED:**
- Retail bid-ask (0.10% base, 0.50% stress).
- That 15-Nov notes for every year 2033-41 will be outstanding in 2033. This is routine 10-year issuance, but the 2026-2031 auctions have not happened yet.
- That iBond-type funds for 2037-41 will exist. Used only in universe A.
- Real brokers' minimum face and increments. I assumed $1,000.
- That $10/$25 tickets match Laura's real broker, which may be cheaper.

**Simplifications:**
- **Medians.** Medians are not additive. "Totals" across 2033 and 2042 are approximate.
- **Smaller samples.** BOTH and the correlation +0.5 rows use the first 30,000 paths. The bid-ask, roll-down and universe-A sensitivities use the first 50,000.
- **History** has about 4 independent 16-year periods (red team section 1c).
- **The 2031 top for 1R** uses the LP's own projection, made in 2031 with yields frozen. It rarely binds.
- **Housekeeping slip, fixed.** One script briefly overwrote my *copy* of `shiller_monthly.csv` *after* all runs had read it. I restored it from `oct20/redteam3r/data/` and checked it byte for byte. The extra run was repeated and gave identical output (`data/r1_extra_16oct_stdout_run1.txt` against `data/r1_extra_16oct_stdout.txt`).

---

## 9. Reproduce

Run these from `oct20/rematch1R/scripts/` with `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I`:
- `validate.py ../data`: must match `../data/validate_out.txt` exactly.
- `verify_lp.py`: the independent LP check.
- `run_1r.py ../data/tsy_202610.csv 10/16/2026 20261019 ../data/r1_base_16oct.json mc,det,boot,hist` (about 17 minutes on 4 cores).
- `run_1r.py ... mctc,mcR,mcA` (sensitivities).
- `run_1r.py ../data/tsy_202610.csv 10/16/2026 7 ... mc`
- `run_1r.py ../data/tsy_202610_fetch20oct.csv 10/19/2026 20261019 ... mc,det`
- `run_extra.py ../data/tsy_202610.csv 10/16/2026 ../data/r1_extra_16oct.json` (BOTH, and correlation +0.5).
- `det_shifts.py` (deterministic −2/−1/0/+1/+2, both curves).
- The batch script is `run_all.sh`.
