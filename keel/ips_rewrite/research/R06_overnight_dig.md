# R06 The overnight dig: investing ideas past R02 and R05, each tested in the model

> **Read `../../BIBLE.md` first.** This page feeds the rewrite. It drafts no IPS prose.

AI-generated (Claude Code), Tue 27 Oct 2026, night (Sydney), thread "Out-think every rival team for semis". Not for
submission. MODEL numbers come from `../lab/K_overnight.py` (`../lab/K_overnight_results.json`): the 22 Oct 2026
curve, J.P. Morgan's 2027 world-stocks figure of 7.5% compound with 16.78% volatility, 200,000 paths and seed 20261016,
the same set-up as `R05_joint.py`. K4 uses a separate, simpler annual model and says so.

## Result
R02 and R05 already cover the 80 textbook ideas: LDI, cash-flow matching, immunisation, horizon duration, defeasance,
pull-to-par, reinvestment risk, convexity, key-rate duration, sequence risk, glide paths, CPPI and OBPI, time
diversification, Kelly, human capital, signalling, the newsvendor and the rest. Re-reading them would add nothing.
So tonight's dig asked a different question: **which ideas would change what the IPS says, and does the model agree?**
Four were tested. Two are kept for the IPS, one is kept for the Final Report, and one is binned.

1. **KEEP (IPS): the stock share rises as the payments are made (a rising equity glide path, no trades).** Every
   rival that glides goes the other way. See D1.
2. **KEEP (IPS, slot C13): one funding test on three dates.** This is the pension de-risking glidepath, and Laura
   reaches its end state on day one. It gives the IPS the "decision-making framework" Book 7 asks for, which no draft
   has had yet. See D2.
3. **BIN (IPS) / note for the Final Report: a ratchet that locks in stock gains before 2031.** It is worth about
   $2,000 to the bottom of the range. See D3.
4. **KEEP (Final Report): the price of certainty against the rival plans.** The ladder costs about $35k of median
   contribution against a 60/40 plan, and it removes a 1-in-5 chance of missing a payment. See D4.

Also below: D5 (why the cap costs the contribution nothing: option arithmetic, not modelled) and D6 (the false
certainty claim most rivals make).

---

### D1. The rising equity glide path ("the stocks rise as the bonds run off")
- **The idea.** Pfau and Kitces (2014) found that for a retiree drawing fixed amounts, an equity share that starts
  low and *rises* through retirement lowers both the chance and the size of failure. That is the reverse of a
  target-date fund. Their shape is a U: "the stock allocation is the lowest at the point" when the spending goal is
  most vulnerable. The cause is sequence risk. (Kitces later called the low point a "bond tent".)
- **Laura's plan, tested (K1, median path, the stock share of everything she owns each 1 January):** 4.6% in 2028,
  5.9% in 2032, 5.1% in 2033 after the contribution, 11% in 2037, 19% in 2039, 28% in 2040 and 45% in 2041. The
  share is lowest exactly when the promise is most exposed (2028-2033, before the first payment) and rises
  ninefold by the last payment. **No share is bought or sold to make that happen.** Each January a bond matures and
  pays a cheque, the bonds run off, and what is left is Laura's own stake in VT.
- **Every rival goes the other way.** Most of the 36 simulated rivals step stocks *down* toward 2031-2033
  (`../rivals/RIVAL_MAP.md` s2). They de-risk at the end. Caplet XR de-risks on day one, and then risk rises on its own.
- **What it does to the IPS.** It answers Book 7's "How will the portfolio's asset allocation and composition change
  as future funding needs approach and payments are made?" with an aha instead of a schedule: *the allocation
  changes by itself, and in the opposite direction from everyone else, because the safest moment is the start.*
  It also corrects R02 #33 ("this plan does not glide"). It glides, upward, without a trade.
- **The honest difference.** Pfau and Kitces' retiree raises equity by buying stocks, which works partly as dollar-cost
  averaging into a falling market. Laura's share rises because her bonds are spent, not because she buys. Say
  "rises", never "we buy more stocks".
- **Claim in 15 words:** "Every January a bond retires, so her stock share rises – the reverse of a target-date fund."
- Source: W. D. Pfau and M. E. Kitces, "Reducing Retirement Risk with a Rising Equity Glide Path", *Journal of
  Financial Planning* 27(1), Jan 2014, pp. 38-45,
  https://www.financialplanningassociation.org/article/journal/JAN14-reducing-retirement-risk-rising-equity-glide-path
  (read 27 Oct 2026; quoted: "have the potential to actually reduce both the probability of failure and the
  magnitude of failure"; "more like the letter U").

### D2. One funding test, three dates (the pension glidepath, with Laura already at the end)
- **The idea.** A pension fund's de-risking glidepath "lowers risk in a pension's asset mix as its funded level rises
  ... by gradually shifting from growth assets to liability-hedging assets" (Bank of America, *Demystifying de-risking
  glidepaths for pension plans*, March 2026). The end state of that path is a fund that holds bonds matched to its
  payments and takes risk only with its surplus.
- **Laura's twist.** She can start at the end state, because her payments are known and small next to her deposits.
  So the whole plan is one test, run on fixed dates: *are the ten payments fully covered by Treasuries we will hold
  to maturity? If not, the next dollar closes the gap, the longest-dated payment first. If so, every other dollar
  belongs to the contribution: the floor first, then stocks bought with the floor's interest.*
- **How often the test has to act (K2, MODEL):**

  | Checkpoint | The test fails when | How often | Typical size |
  |---|---|---|---|
  | Jan 2027, first deposit | the ladder costs more than $300k | 47% of paths | median gap $9.8k when short |
  | Jan 2028, second deposit | a gap is left after the $150k | 0.0% | none |
  | Jan 2033, reserve set aside | coupons reinvested at lower yields leave a gap over $1k | 47% | 95th percentile $22k; covered by the 2027 leftover plus Laura's half in 93% |

  After January 2033 nothing is tested again: the reserve changes itself.
- **What it does to the IPS.** It fills champion slot C13 (`../../loop/CHAMPIONS.md`: "no draft has a framework a
  judge can point to"). It joins three V25 paragraphs (the 2028 deposit fills the gap, the floor and the stocks, the
  2033 re-match) into one rule. It is the "principles that will guide your investment decisions" Book 7 asks about.
- **Claim in 15 words:** "One test, three Januaries: are the cheques fully bought? If not, buy them first."
- Source: Bank of America Workplace Benefits, "Demystifying de-risking glidepaths for pension plans" (March 2026),
  https://business.bofa.com/content/dam/flagship/workplace-benefits/demystifying-glide-paths/glidepaths-for-pension-plans.pdf
  (read 27 Oct 2026). The UK "low dependency" funding target (R05 #4) is the same end state, set by a regulator.

### D3. A ratchet that locks in gains before 2031 (BINNED for the IPS)
- **The idea.** Structured notes often add a "lock-in" or ratchet: once the index rises far enough, part of the gain
  becomes guaranteed. Seven of the twelve AI rivals do a crude version, moving stocks into Treasuries on a schedule
  before 2031. Caplet XR could do it by rule instead: each January from 2029 to 2031, if the contribution's stocks are
  at a new high, move half of the new gain into a Treasury maturing in December 2032. The bottom of the range could
  then only rise.
- **Tested (K3, MODEL).** The mean bottom rises by $2,400 (from $138.9k to $141.4k), the median stays at $145k, the
  chance of reaching the top goes from 76.7% to 77.4%, the median range narrows by $1,500, and the bottom rises by
  $5k or more in 42% of paths.
- **Verdict: bin for the IPS.** The contribution's stocks are only about $15k (half of a VT stake near $31k), so a
  ratchet is a rule for a rounding error. The real lock-in already happened in January 2028, when the floor was bought
  before a single share. **Keep as Final Report material** ("considered and rejected, and why"), which shows a
  decision rather than a feature list.

### D4. The price of certainty, against the rival plans (Final Report)
- **The test (K4).** This is a simpler, separate model with annual steps. Stocks are as above. One yield starts at the
  22 Oct 10-year rate of 4.96% and follows a random walk of 1pp a year. Each rival keeps its mix. In January 2033 each
  sets aside a reserve worth the ten payments' market value plus a 10% cushion, gives the rest, and then runs the
  reserve its own way. A miss is any January from 2033 to 2042 when the reserve cannot pay $50,000 in full.

  | Plan (rival archetype) | Misses a payment | Median 2033 contribution | Contribution zero |
  |---|---|---|---|
  | 60/40 total return (H15) | 18% | $203k | 6% |
  | Glide 70 -> 30 (H03, and most AI rivals' growth sleeves) | 9% | $198k | 5% |
  | Three buckets, 3 years in bills (H01) | 11% | $194k | 4% |
  | Barbell 90/10 (H08) | 1.7% | $152k | 0% |
  | All in a duration-6 bond fund (H18, H23-style) | 4.1% | $139k | 0% |
  | **V25 (the main model)** | **about 0** with the 2033 re-match and its cushion (`../../rooms/lab/L-10_last_in_line.md`: 6.8% -> 0.01%) | **$166k** (bottom $145k, top $166k) | 0% |

  If the 2028 deposit is $75k instead of $150k, the 60/40 plan misses 23% of the time and gives nothing 21% of the time.
- **Reading.** V25 beats the barbell and the bond fund on both counts: more contribution and fewer misses. Against
  the growth-tilted plans it gives up about $30-40k of median contribution and in return removes a 1-in-5 to 1-in-11
  chance of breaking a promise made in person. That is the price of certainty, paid once, in public. It is the
  Final Report's answer to the sceptic, with Bodie's (1995) point (R02 #29) that insuring stocks costs more the
  longer you hold them.
- **The IPS gets at most one clause of this** (the rewrite thread's limit of one or two numbers stands), for example
  the sceptic paragraph's "a withdrawal of fixed dollars is a forced sale at the bottom", now backed by a number.

### D5. Why the cap costs the contribution nothing (option arithmetic; the Shark Tank's "missing cap")
The contribution is the floor plus half the stocks, **capped at the top named in 2031**. In option terms it is a
bond plus a call spread: long the stocks up to the top, short them above it. Above the cap the contribution's
exposure to stocks is zero. Every extra dollar goes to Laura's half, the money that pays for overruns and the
Taiwan dollar. So the cap is not a limit on generosity. It turns a lucky market into her flexibility, and it keeps the
case's "within that range" true in a boom. One clause: "Above the top, every extra dollar stays hers."

### D6. The false certainty claim most rivals make
Most rivals define certainty as "every payment backed by a Treasury held to maturity, so the only risk left is a US
government default" (`../rivals/RIVAL_MAP.md` s3). For a ladder of **coupon** Treasuries that is false: the coupons
are reinvested at unknown rates (a gap above $1k in January 2033 in 47% of model paths), and the ladder costs more
than $300k in 47% of paths. V25's "we can name exactly where it breaks" is the honest, stronger version. It wins on
accuracy without hedging. Keep it, and make it plain that it answers a claim the reader has already seen ten times.

## Sources (read 27 Oct 2026)
- Pfau, W. D., & Kitces, M. E. (2014). Reducing retirement risk with a rising equity glide path. *Journal of
  Financial Planning*, 27(1), 38-45. https://www.financialplanningassociation.org/article/journal/JAN14-reducing-retirement-risk-rising-equity-glide-path
- Bank of America Workplace Benefits (March 2026). Demystifying de-risking glidepaths for pension plans.
  https://business.bofa.com/content/dam/flagship/workplace-benefits/demystifying-glide-paths/glidepaths-for-pension-plans.pdf
- Already in R02's reading list, now applied: Leibowitz & Weinberger (1982), contingent immunisation (the floor plus a
  cushion invested elsewhere is its static form); Bodie (1995), the cost of insuring stocks; Perold & Sharpe (1988),
  buy-and-hold payoffs need no rebalancing.
- Not reached (the network blocked kitces.com): Kitces' "bond tent" articles. The term is his; cite the 2014 paper
  for the finding.
