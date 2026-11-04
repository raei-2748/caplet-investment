(Keel is a simulated team, AI-written.) Nora, research note, H-028 round 1, Wed 4 Nov 2026 (Sydney). AI-generated
(Claude Code). Every model number here is MODEL and none goes into an IPS line (Book 11). All web quotes were read
through a fetch tool (a small model reads the page and quotes it), so every quote below is **near-verbatim, via fetch
tool**; where the tool split a sentence I have joined the pieces, and where it summarised the text between quotes I
say so.

## (c) Deletion test: my prediction, written BEFORE running (12:25 Sydney)

What I expect: the seed is fixed (20261016), so the re-run should reproduce Amara's table exactly (S0 and S6: KW-N
wiped = kept, 97.02% / 82.18%, 0 futures worse off; KWN wiped 100.00%, 0 worse off; S9 KWN wiped 97.88%, 3,193 worse
off). A clean re-run proves the script reproduces, not that the plan is true.

The biggest thing I think it leaves out: **the lock V57 actually describes.** The test scores two locks, KW-N (the
lock as the model sized it, coupons from naming day earning 0%) and KWN (C06's words, "as if later bond payments sat
idle", which counts the bonds maturing inside the funds too). V57 says "as if no more interest were reinvested". That
names interest only. Read plainly, it is KW, not KWN: the money inside a fund whose bonds mature during its last year
and then sit in cash until the December close is principal, not interest, and the 0.07% fee isn't interest either.
D36's README backs the V57 lock with L-17 and A33, which both pay the funds as par bonds. So my guess is that the
test shows shares never matter (wiping them changes nothing in S0/S6), but under the lock V57's words describe, some
cheques are short with or without shares, by small amounts. "No payment depends on shares" would then be true while
"high certainty" is a little weaker than the words suggest.

Second thing it leaves out: the funds' real holdings. Exhibit N spreads each fund's maturities evenly over its final
year (its own ASSUMPTION; real weights not read). Third: it wipes shares on one day only (1 Jan 2031), on V54's design,
on one curve (22 Oct).

---

## (a) What a holder of an iBonds Treasury fund gets at its end date

### Find a1. IBTM summary prospectus
- **Source:** iShares iBonds Dec 2032 Term Treasury ETF, Summary Prospectus, BlackRock / iShares Trust, dated
  27 February 2026 (per the document), https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf ,
  read 4 Nov 2026.
- **Quoted (near-verbatim, via fetch tool):**
  - "The iShares iBonds Dec 2032 Term Treasury ETF (the "Fund") seeks to track the investment results of an index
    composed of U.S. Treasury bonds maturing in 2032."
  - "The Underlying Index consists of publicly-issued U.S. Treasury securities that are scheduled to mature between
    January 1, 2032 and December 15, 2032, inclusive."
  - "In the last six months of operation, as the bonds held by the Fund mature, the proceeds will typically be
    reinvested by the Fund in investments already in the Underlying Index but may also be invested in other cash and
    cash equivalents as determined by BFA." (Two fetches gave this sentence slightly differently: the first left out
    "by the Fund in investments already in the Underlying Index". Not sure it is word for word.)
  - "To the extent that the Fund invests in money market or similar funds, it will incur the fees and expenses of such
    funds." / "By December 15, 2032, the Fund is expected to consist almost entirely of cash."
  - "The Fund is a term fund that will terminate on or about December 15, 2032, at which time it will distribute its
    remaining net assets to shareholders pursuant to a plan of liquidation."
  - "After appropriate provision is made for any Fund liabilities, its net assets will be distributed to then-current
    shareholders pursuant to a plan of liquidation."
  - "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions."
  - Fee table: total annual fund operating expenses 0.07% (0.07% after waiver).
  - The summary prospectus states no distribution frequency (the tool: it says only "The Fund intends to make
    distributions that may be taxable to you as ordinary income or capital gains.").

### Find a2. IBTM and IBTO fact sheets (as of 30 Sep 2026) and the IBTM product page
- **Sources:** "iShares iBonds Dec 2032 Term Treasury ETF" fact sheet, iShares, as of 30 Sep 2026,
  https://ishares.com/us/literature/fact-sheet/ibtm-ishares-ibonds-dec-2032-term-treasury-etf-fund-fact-sheet-en-us.pdf ;
  "iShares iBonds Dec 2033 Term Treasury ETF" fact sheet, as of 30 Sep 2026,
  https://ishares.com/us/literature/fact-sheet/ibto-ishares-ibonds-dec-2033-term-treasury-etf-fund-fact-sheet-en-us.pdf ;
  IBTM product page, BlackRock, key facts as of 22 Oct 2026,
  https://www.blackrock.com/us/individual/products/328944/ishares-ibonds-dec-2032-term-treasury-etf ; all read 4 Nov 2026.
- **Quoted (near-verbatim, via fetch tool; IBTO wording, IBTM's matches except the first line):**
  - IBTM: "The iShares® iBonds® ETFs ("Funds") will terminate on or about October or December 15 of the year in each
    Fund's name." (IBTO's sheet: "on or about December 15".)
  - "An investment in the Fund(s) is not guaranteed, and an investor may experience losses, including near or at the
    termination date. Unlike a direct investment in a bond that has a level coupon payment and a fixed payment at
    maturity, the Fund(s) will make distributions of income that vary over time."
  - "In the final months of each Fund's operation, as the bonds it holds mature, its portfolio will transition to cash
    and cash-like instruments. As a result, its yield will tend to move toward prevailing money market rates, and may
    be lower than the yields of the bonds previously held by the Fund and lower than prevailing yields in the bond
    market."
  - "Following the Fund's termination date, the Fund will distribute substantially all of its net assets, after
    deduction of any liabilities, to then-current investors without further notice and will no longer be listed or
    traded. The Funds' distributions and liquidation proceeds are not predictable at the time of investment and the
    Funds do not seek to return any predetermined amount."
  - Data fields: "Distribution Frequency : Monthly" (IBTM and IBTO sheets; the BlackRock page also says Monthly);
    "Expense Ratio 0.07%"; IBTM benchmark "ICE 2032 Maturity US Treasury Index"; IBTM 15 holdings (sheet and page,
    page as of 22 Oct 2026); maturity bucket 5-7 years 99.45%, cash and derivatives 0.55% (sheet). Neither page
    lists the holdings' maturity dates (the page links a holdings file the tool did not open), so **the real spread
    of IBTM's maturities through 2032 is UNVERIFIED**.

### Find a3. How a final distribution actually runs (2025 funds)
- **Source:** "iShares iBonds ETFs Near Final Distribution Dates", press release, BlackRock / iShares, 15 Oct 2025,
  https://www.ishares.com/us/literature/press-release/ibonds-terminations-release.pdf , read 4 Nov 2026.
- **Quoted (near-verbatim, via fetch tool):** "the Fund will distribute substantially all of its net assets, after
  deduction of any liabilities, to then-current investors"; "Shareholders will receive their proceeds from the
  liquidation on or around the listed liquidation date." For IBTF (Dec 2025 Term Treasury) the release lists last
  trading day and final NAV 12/15/25 and liquidation 12/18/25 (tool's summary of a table).

**Mechanism, in two plain sentences.** A fund like IBTM owns about fifteen Treasuries that all mature during 2032; as
each one matures, the cash sits in money-market-type holdings until mid-December, and then the fund pays out whatever
its net assets are, less its 0.07% a year. Before that, it pays monthly income that varies, which the holder has to
reinvest herself.

**V57 sentence tested (P3):** "A Treasury held to maturity pays exactly what it promised, whatever markets do."

**Where it breaks.** It is true of a Treasury bond, including every bond inside the funds. It is not true of a fund
unit: the issuer says the fund does "not seek to return any predetermined amount" and its proceeds "are not
predictable at the time of investment". Five of the ten rungs are funds (2033-37), and the sentence comes straight
after "Treasury funds with fixed end dates", so a judge who knows iBonds reads it as covering them. It also sits
beside Caplet's own locked TNA reflection 2, "their terminal payout is a net asset value, as opposed to a promise of
par" (as quoted in `keel/library/ips_road_2026-10/00_SPINE.md`); all three deliverables are judged together.

**Verdict: TRUE IF** "a Treasury" means the bonds, not the fund units. **Smallest word fix:** add one word, "A
Treasury **bond** held to maturity pays exactly what it promised". The sentence then says only what is true, and the
next sentence ("no payment depends on shares") still covers the funds, because they hold nothing but Treasuries and
cash. (The Window gave TRUE IF on 2 Nov from repo copies, with Kai dissenting; this is the same verdict from the
issuer's own pages read today.)

**Monthly income: yes.** Both fact sheets and the product page say "Distribution Frequency: Monthly", and the sheet
says the distributions "vary over time". So the funds add monthly income that must be reinvested before each end
date, on top of the bonds' half-yearly coupons. That is inside P7's "reinvesting its bonds' interest". What is NOT
inside that phrase is the fund's own last-months cash, whose yield "will tend to move toward prevailing money market
rates": that is reinvested principal, not interest (see section c).

**"each maturing before a January payment": TRUE.** Terminate on or about 15 December; the 2025 example paid out on
18 December.

---

## (b) Cash-flow matching (dedication) against immunisation

### Find b1. Leibowitz (1986), Part I
- **Source:** Martin L. Leibowitz, "The Dedicated Bond Portfolio in Pension Funds - Part I: Motivations and Basics",
  Financial Analysts Journal 42(1), 1986, pp. 68-75, CFA Institute Research and Policy Center summary page,
  https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/the-dedicated-bond-portfolio-in-pension-fundspart-i-motivations-and-basics ,
  read 4 Nov 2026 (summary only; full article paywalled).
- **Quoted (near-verbatim, via fetch tool):** "Cash-matching, the simplest form of dedication, produces a fixed income
  portfolio that provides a stream of payments from coupons, sinking funds and maturing principal payments that
  matches a given liability schedule. In many cases the objective will be to assure fulfillment even under totally
  passive management—that is, no reinvestment. Reinvestment at positive interest rates, however, can lower pension
  fund costs without substantially increasing risk or complexity."

### Find b2. Leibowitz (1986), Part II
- **Source:** Martin L. Leibowitz, "The Dedicated Bond Portfolio in Pension Funds - Part II: Immunization, Horizon
  Matching and Contingent Procedures", Financial Analysts Journal 42(2), 1986, pp. 47-57,
  https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/the-dedicated-bond-portfolio-in-pension-fundspart-ii-immunization-horizon-matching-and-conti ,
  read 4 Nov 2026 (summary only).
- **Quoted (near-verbatim, via fetch tool):** "Immunization calls for the creation of a portfolio of bonds whose value
  coincides with the present value of a given schedule of liabilities and whose duration, or interest rate
  sensitivity, is the same as that of the liabilities." / "Immunization offers greater flexibility than simpler forms
  of dedication, such as cash matching, but it requires portfolio changes over time and is susceptible to certain
  sequences of market movements."

### Find b3. CFA Institute, Level III reading
- **Source:** "Liability-Driven and Index-Based Strategies", CFA Program Level III refresher reading, CFA Institute,
  2026 curriculum (no author named on the page),
  https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/liability-driven-index-based-strategies ,
  read 4 Nov 2026.
- **Quoted (near-verbatim, via fetch tool):** "immunization is achieved by matching the Macaulay duration of the bond
  portfolio to the horizon date." / "As time passes and bond yields change, the duration of the bonds changes and the
  portfolio needs to be rebalanced." / "The techniques and risks associated with LDI are introduced using a single
  liability and then are expanded to cover both cash flow and duration-matching techniques and multiple liabilities."
  The page itself has nothing on cash-flow matching's reinvestment (the tool: "does not cover cash flow matching as a
  separate strategy"). A second CFA page, "Overview of Fixed-Income Portfolio Management"
  (https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2025/overview-fixed-income-portfolio-management ,
  read 4 Nov 2026), adds: "For liability-based fixed-income mandates, portfolio construction follows two main
  approaches—cash flow matching and duration matching—to match fixed-income assets with future liabilities." and
  "Portfolio dispersion captures the variance of the times to receipt of cash flows around the duration."

### Find b4. Society of Actuaries (1988)
- **Source:** Rama Kocherlakota, E.S. Rosenbloom and Elias S.W. Shiu, "Algorithms for Cash-Flow Matching",
  Transactions of the Society of Actuaries 40, Pt. 1, 1988,
  https://www.soa.org/globalassets/assets/library/research/transactions-of-society-of-actuaries/1988/january/tsa88v40pt115.pdf ,
  read 4 Nov 2026 (scanned text; the tool kept its OCR errors).
- **Quoted (near-verbatim, via fetch tool):** "Two important methods for insulating a fixed-income portfolio from
  shifts in the term structure of interest rates are cash-flow matching and immunization." / "The classical
  formulation is to choose fixed-income investments such that, for each period of the planning horizon, the
  investment cash flow will be sufficient to meet the projected liability payment." / "A major variation of the above
  is to allow cash carry-forward (at low or zero interest); this would lower the cost of the bond portfolio." / "To be
  conservative, one would set b, to be large and 1, to be small." (OCR: b_t is the borrowing rate, l_t the rate cash is
  carried forward at.)

### Find b5. Practitioners
- **Western Asset:** Jan Pieterse, "The Final Phase of LDI—Cash Flow Matching", Western Asset Management, 23 Feb 2023,
  https://www.westernasset.com/us/en/research/blog/the-final-phase-of-ldi-cash-flow-matching-2023-02-23.cfm , read
  4 Nov 2026. Heading: "Cash Flow Matching Eliminates Rebalancing, Drawdown and Liquidity Risk". "Cash flow matching
  is an investment approach that closely aligns a portfolio's cash flows (coupons plus principal repayments) with a
  plan's anticipated benefit payments." / "These predictable cashflows from a laddered bond portfolio can be used to
  self-fund benefit payments." / "This lessens the administrative burden of frequent manager withdrawal requests and
  reduces transaction cost of asset allocation recalibration." Nothing on reinvestment (tool).
- **BlackRock UK:** "Views from the LDI Desk: Why Cashflow Match?", BlackRock Investment Management (UK), 2026 (data
  as of March 2026), https://www.blackrock.com/uk/literature/whitepaper/views-from-the-ldi-desk-why-cashflow-matching-matters.pdf ,
  read 4 Nov 2026. "Precise cashflow matching aims to match cashflows exactly, on e.g. a year-on-year basis." /
  "Cumulative cashflow matching aims to cumulatively match cashflows ensuring there is not a shortfall." /
  "Cumulative matching usually provides the best balance of predictability and flexibility, ensuring cashflows are met
  while allowing allocations to shorter-dated assets where more attractive. However, this can introduce reinvestment
  risk and requires the overall duration profile to be carefully managed, often using derivatives, to maintain
  alignment with liabilities."
- **Duke teaching page:** Mark Taranto, "WWWFinance - Bond Immunization" (written Oct 1995), Campbell Harvey's BA350
  pages, https://people.duke.edu/~charvey/Classes/ba350/bondval/immune.htm , read 4 Nov 2026. "Such a portfolio is
  often called a cash matched portfolio, or a dedicated portfolio." / "The portfolio manager who dedicates a portfolio
  can almost forget about managing it." / "It is a good idea to rebalance the portfolio occasionally." / "Sometimes
  new bonds that are cheaper or a better fit will become available." (The tool summarised the text between these.)
  Immunised: "Immunized portfolios need more nurturing."

**Mechanism, in two plain sentences.** Immunisation keeps the bonds' value equal to the payments' value and their
duration equal to the payments' duration, and because duration drifts as time passes and yields move, it has to be
re-traded. Cash-flow matching buys bonds whose coupons and principal arrive in time for each payment and holds them;
any money that arrives early is carried forward, and the cautious convention is to assume it earns little or nothing.

**V57 sentences tested.**

1. P3 "matching their bonds' average timing to the payments'" (as the plain name for duration matching): **TRUE.**
   Macaulay duration is the value-weighted average time of a bond's payments, and the CFA reading defines
   immunisation as matching it ("matching the Macaulay duration ... to the horizon date"; dispersion is measured
   "around the duration"). Leibowitz adds the value match ("whose value coincides with the present value"), which the
   sentence's "cover" carries. No fix.

2. P3 "and rebalancing as rates move": **TRUE.** The CFA line gives two triggers, "As time passes and bond yields
   change"; the sentence names one, and nothing it says is false. No fix.

3. P3 "We do the second, which never needs rebalancing": **TRUE.** Western Asset's heading says it in nearly those
   words; Leibowitz contrasts cash matching, which can run under "totally passive management", with immunisation,
   which "requires portfolio changes over time". Taranto's "rebalance the portfolio occasionally" is optional (cheaper
   bonds appear), not needed. The one trade the plan does make, P7's top-up, happens once, on a fixed date, and
   re-matches nothing. No fix.

4. Is the plan honestly "the second"? **TRUE IF**, with the condition already in P7. The textbook form (Kocherlakota
   et al.'s "classical formulation", Leibowitz's "no reinvestment") has each period's coupons and principal meet that
   period's payment. Laura has no payment until 2033, so six years of interest must be carried forward, which is the
   SOA paper's "major variation": "cash carry-forward (at low or zero interest)", done because it "would lower the
   cost". V57 counts on that interest earning market rates until naming day and prices it at zero from then on. That
   is cumulative cash-flow matching in BlackRock's sense, and BlackRock says it "can introduce reinvestment risk",
   which is exactly P7's weakness. **No word fix**: P7's first clause states the condition, and saying it again in P3
   would cost words to repeat it. A judge who knows dedication will find P7 and nod; one who stops at P3 could say
   "never needs rebalancing, but it does need reinvesting", and P7 answers him.

5. P7 "we price that shortfall as if no more interest were reinvested": **TRUE at source as a convention.** Leibowitz:
   "assure fulfillment even under totally passive management—that is, no reinvestment"; SOA: carry-forward "at low or
   zero interest", and "To be conservative, one would set ... [the carry-forward rate] to be small". Zero is the
   bottom of that convention. Where it breaks is the word "interest", for the funds: see section (c).

---

## (c) Deletion test: the run and what it covers

**Command.** The Kitchen's command, `python3 -B keel/huddles/2026-11-03_the-kitchen-before-the-hand-over/research/amara_r3_deletion_on_funds.py S0 S6 S9`,
writes its results file back into the Kitchen's folder (`f.write_text`, line 156), which is outside the folders I may
write today. So I ran a **byte-identical copy** from this folder (`nora_rerun_amara_r3_deletion_on_funds.py`; `cmp`
identical, sha256 `96b3f088...0d43b` for both). It sits at the same depth, so it resolves the same repo root and loads
the same A33, exhibit N, L-17 chain and saved files. Every other script in the chain writes only under its own
`if __name__ == "__main__"` guard (checked), so nothing else was written. The Kitchen's saved results file is
unchanged (sha256 `123460f1...6964b` before and after).

    cd /home/user/caplet-investment && timeout 540 python3 -B keel/huddles/2026-11-04_checked-only-by-its-writers/research/nora_rerun_amara_r3_deletion_on_funds.py S0 S6 S9

**Run time:** 95 s for all three worlds, exit 0. All four in-run baselines passed, and in every world the
saved-file checks passed against L-17, A33 and exhibit N (`"matches_saved_files": ["L-17", "A33", "exhibit N"]`).
Three RuntimeWarnings ("invalid value encountered in divide") from the shared engine `ips_numbers.py` (lines 255,
256, 542), as Amara reported. Outputs: `nora_rerun_results.json`, `nora_rerun_stdout.txt`, `nora_rerun_stderr.txt`
in this folder. **My results file is identical, key for key, to the Kitchen's saved
`amara_r3_deletion_on_funds_results.json`** (S0, S6, S9 and the stamp).

**Results.** Stamp on every number: **MODEL | V54's design + C06's lock (L-17 KW / exhibit N KWN) | engine L-13 ->
L-14 -> L-16 -> W-08 -> L-17 with A33 + exhibit N + the Kitchen block | curve 22 Oct 2026 (treasury.gov par) |
J.P. Morgan 2027 LTCMA global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 unless S0.** Main floor
convention (floor at NAV); exhibit N's "floor at par" gives the same S0 and S6 rows and S9 within 0.04 points.

| World | Arm | Every cheque in full (MODEL) | Futures worse off than shares kept (MODEL) | Worse by p50 / max (MODEL) | Short p50 / p90 when short (MODEL) |
|---|---|---|---|---|---|
| S0 base | KW-N (lock as the model sized it), wiped | 97.02% (kept: 97.02%) | 0 of 200,000 | - | $1,372 / $2,489 |
| S0 | KWN (C06's words), wiped | 100.00% | 0 | - | - |
| S0 | KWN, halved | 100.00% | 0 | - | - |
| S6 yields 2 pts lower for good | KW-N, wiped | 82.18% (kept: 82.18%) | 0 | - | $2,160 / $3,093 |
| S6 | KWN, wiped | 100.00% | 0 | - | - |
| S6 | KWN, halved | 100.00% | 0 | - | - |
| S9 1 pt lower before build, 2028 deposit halved | KW-N, wiped | 91.83% (kept: 91.97%) | 2,781 (1.39%) | $952 / $3,749 | $1,742 / $7,270 |
| S9 | KWN, wiped | 97.88% (kept: 98.27%) | 3,193 (1.60%) | $1,059 / $4,512 | $5,450 / $16,324 |
| S9 | KWN, halved | 98.08% | 2,788 (1.39%) | $596 / $2,381 | $5,633 / $16,974 |

No future is better off without the shares in any arm (MODEL). With the shares wiped, the floor can't buy the whole
lock in 0% of S0 and S6 futures, and in 3.03% (KW-N) / 4.85% (KWN) of S9 futures (MODEL). Lock drawn from the floor
when the shares are wiped, KWN, p50: $15,858 (S0), $25,340 (S6) (MODEL). The floor fund's own leg, p5/p50/p95:
-$1,122 / $922 / $2,837 in S0 (MODEL).

**My prediction against the result.** Right on both counts: it reproduced to the digit, and the arm that matches
V57's words is the one that misses. A prediction that comes true is still not evidence; it only means I read the
headers properly.

**Does "no payment depends on shares" hold with the five funds as funds?** In the base and the low-yield world,
**yes** (MODEL): wiping every share on naming day leaves 0 of 200,000 futures with any cheque worse off, under either
lock. In S9, where the 2028 deposit is halved, **no** (MODEL): about 1.4-1.6% of futures are worse off, by about
$1,000 at the median, because the lock comes from the kept shares first and the floor alone can't always buy it. P3's
definition survives the funds; it rests on the 2028 deposit arriving, which P5 already says ("first completes the
ladder, if needed").

**Does the test cover V57's lock?** Partly, and not under that name. The arms are C06's: KW-N is L-17's lock
(L-17 header: "each rung's gap if every coupon paid after naming day earns 0%"), scored with the funds at net asset
value; KWN is C06's older words, "as if later bond payments sat idle", which count the bonds maturing inside each
fund in its last year as idle too. **V57's words, "as if no more interest were reinvested", read as KW, not KWN**:
interest only. With the funds as funds, that lock pays every cheque in 97.02% of base futures and 82.18% if yields
fall 2 points for good (MODEL), shares or no shares, short by $1,372 / $2,160 at the median (MODEL). So the deletion
test backs P3 ("no payment depends on shares") and does **not** back the D36/V57 README's claim that the V57 lock "can
only overstate the gap", which rests on L-17 and A33, both run with the funds paid as par bonds.

**Where it breaks, and the word fix (P7, for the room to test).** The issuer says the funds' last months are spent in
cash whose yield "will tend to move toward prevailing money market rates, and may be lower than the yields of the
bonds previously held". That is reinvested principal inside the fund, not interest, so "no more interest" leaves it
out. **Verdict on P7's lock line: TRUE IF** the funds' own last-year cash is counted as idle too. **Smallest word fix:**
"as if ~~no more interest~~ **nothing more** were reinvested", V56's own words (D36). That reads as KWN-w, which in
exhibit N pays every cheque in the base and the low-yield worlds (MODEL), with the 0.07% fee unpriced. This is the
claim I most want attacked: it may be the lock's sizing, not the sentence, that has to change, and a plain reader
hears "nothing more" as "no more interest" anyway, because the clause before is about interest.

**What the test still doesn't cover.** The funds' real maturity dates (an even spread through the last year is
exhibit N's ASSUMPTION; IBTM's holdings list was not readable today, UNVERIFIED); a share fall before or after
naming day rather than on it; V57's design differences from V54, if any (the stamp says V54); any curve but 22 Oct.

---

## Every URL tried (4 Nov 2026)
Opened:
1. https://ishares.com/us/literature/fact-sheet/ibto-ishares-ibonds-dec-2033-term-treasury-etf-fund-fact-sheet-en-us.pdf (two fetches)
2. https://www.ishares.com/us/literature/press-release/ibonds-terminations-release.pdf
3. https://ishares.com/us/literature/fact-sheet/ibtm-ishares-ibonds-dec-2032-term-treasury-etf-fund-fact-sheet-en-us.pdf
4. https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf (two fetches)
5. https://www.blackrock.com/us/individual/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (holdings not shown)
6. https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/liability-driven-index-based-strategies
7. https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2025/overview-fixed-income-portfolio-management (the tool called it the 2026 reading)
8. https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/the-dedicated-bond-portfolio-in-pension-fundspart-i-motivations-and-basics
9. https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/the-dedicated-bond-portfolio-in-pension-fundspart-ii-immunization-horizon-matching-and-conti
10. https://www.soa.org/globalassets/assets/library/research/transactions-of-society-of-actuaries/1988/january/tsa88v40pt115.pdf (two fetches)
11. https://people.duke.edu/~charvey/Classes/ba350/bondval/immune.htm (two fetches)
12. https://www.westernasset.com/us/en/research/blog/the-final-phase-of-ldi-cash-flow-matching-2023-02-23.cfm (two fetches)
13. https://www.blackrock.com/uk/literature/whitepaper/views-from-the-ldi-desk-why-cashflow-matching-matters.pdf (two fetches)

Failed:
- https://www.ishares.com/us/products/328944/ : "failed at its site (client_error)", nothing retrieved.
- https://analystprep.com/study-notes/cfa-level-iii/cash-flow-matching-strategies/ : returned an RSS feed of teasers,
  not the study note. Nothing used; UNVERIFIED.

Not found: no fetchable page for Redington (1952) turned up in two searches; SEC EDGAR not needed once the issuer's
own summary prospectus opened.
