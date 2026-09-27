# Treasury ETF instruments for Laura Gao's 2033–2042 liability ladder (fact-checked)

**Research date:** 2026-09-27. **Blocked sites:** ishares.com, blackrock.com, sec.gov, pimco.com, investor.vanguard.com, etf.com, etfdb.com, stockanalysis.com, tipranks.com, kiplinger.com, google.com/finance, thefinancebuff.com, and in this pass also prnewswire.com, stocktitan.net and finance.yahoo.com. No issuer page or fact sheet could be opened. Every figure below comes from search snippets only. **Confirm each one on the issuer page before you use it.**

**WInS approved list:** UNVERIFIED. Check every ticker against it.

**Payment timing (from the client file):** Withdrawals happen at the **beginning** of each year, 2033 through 2042. That changes how the ETFs line up with the payments (see §1).

## 1. Defined-maturity Treasury ETFs (iShares iBonds Dec 20XX Term Treasury)

Each fund holds Treasuries maturing in its named year and terminates around mid-December of that year. IBTR, for example, holds Treasuries maturing after Jan 1, 2036 and before Dec 15, 2036 [S3b].

| Fund year | Ticker | Expense ratio | Pays for the payment on | Source |
|---|---|---|---|---|
| 2027 | IBTH | UNVERIFIED | (cash in 2027–28) | [S5, S17] |
| 2028 | IBTI | UNVERIFIED | — | [S4] |
| 2030 | IBTK | UNVERIFIED | — | [S17] |
| **2032** | **IBTM** | UNVERIFIED | **Jan 2033** | [S17] |
| **2033** | **IBTO** | UNVERIFIED | **Jan 2034** | [S4] |
| **2034** | **IBTP** | 0.07% (snippet) | **Jan 2035** | [S2] |
| **2035** | **IBTQ** | 0.07% (snippet) | **Jan 2036** | [S1] |
| **2036** | **IBTR** | **0.07%** (re-verified) | **Jan 2037** | [S3b] |
| 2037–2043 | none found | n/a | — | [S6, S7, S17, S18] |
| 2044/45/46/54/55 | IBGA/IBGB/IBGC/IBGK/IBGL | UNVERIFIED | — | [S4, S5, S6] |

- **Correction on coverage:** A Dec-20XX fund pays out in December, before the payment due on Jan 1 of the next year. So Dec 2032–Dec 2036 funds (IBTM–IBTR) cover the **five payments from 2033 to 2037**, not "2033–2036, four payments". The **five payments from 2038 to 2042** have no exact-year ETF.
- **IBTR 30-day SEC yield of 4.69% (2026-09-03):** UNVERIFIED. My re-search did not find that number. One snippet gave a 3.91% *distribution* yield, which is a different measure [S3b].
- **2037+ maturities:** One iShares snippet says iBonds offer "the only longer term (2037+) maturities" [S18]. No Dec 2037–2043 *Treasury* fund showed up in any search, so that phrase probably refers to the 2044+ funds or to other asset classes. Treat 2037–2043 as nonexistent (UNVERIFIED) until you can check the iShares site.
- **LDRT** (1–5 yr ladder) [S7] and **IBIL** (Oct 2035 TIPS) [S1] exist in search results. Neither fits a fixed nominal payment in 2033–2042.

**Other providers (CORRECTED):** The original report called Invesco BulletShares Treasury funds "likely wrong". That was itself wrong. Several headlines report that **Invesco launched BulletShares *Treasury* ETFs maturing 2027–2031 in June 2026** [S8b]. Tickers and expense ratios are UNVERIFIED because the press-release pages were blocked. These funds are relevant to the 2027/2028 cash, not to the 2033+ payments. The claim that they span "2026–2036" is UNVERIFIED and conflicts with S8b. Vanguard target-maturity ETFs being corporate-only (VBCG, VBCI): UNVERIFIED in this pass.

## 2. Zero-coupon / STRIPS Treasury ETFs

| Ticker | Exposure | Expense ratio | Source |
|---|---|---|---|
| ZROZ (PIMCO) | STRIPS, 25+ yr | 0.15% (snippet); duration UNVERIFIED | [S9] |
| GOVZ (iShares) | STRIPS, 25+ yr | **0.10%** (search summary says multiple sources agree) | [S10b] |
| EDV (Vanguard) | STRIPS, 20–30 yr | **0.05% as of 2025-12-19** (re-verified); duration UNVERIFIED | [S11b] |

All three are much longer than the liabilities.

## 3. Constant-maturity Treasury ETFs

| Ticker | Index | Expense ratio | Duration | Source |
|---|---|---|---|---|
| IEF | 7–10 yr | 0.15% (snippet) | **Conflicting:** 6.95 yr (6/30/2026, first report) vs "near 7.5 yr" (May 2026, secondary blog). UNVERIFIED | [S12, S12b] |
| TLT | 20+ yr | 0.15% (snippet) | 15.31 yr (6/30/2026), UNVERIFIED (fact sheet blocked) | [S12] |
| VGIT | 3–10 yr | 0.03% (snippet) | UNVERIFIED | [S13] |
| VGLT | 10+ yr | 0.03% (snippet) | 14.1 yr, UNVERIFIED | [S13] |
| UTEN / UTWY | 10-yr / 20-yr single-bond | 0.15% (snippet) | UNVERIFIED | [S14] |
| XTEN / XTWY | 10- / 20-yr target duration | UNVERIFIED | stable by design | [S15] |

## 4. T-bill ETFs

| Ticker | Expense ratio | Source |
|---|---|---|
| SGOV | **0.09%** (re-verified) | [S16b] |
| BIL | **~0.135%** (re-verified; 0.14% rounded) | [S16b] |
| XHLF | UNVERIFIED | [S15] |

## 5. Liability duration (recomputed in Python)

Assumptions: flat 4.5% yield, valued at 2026-09-27. The yield is an **unsourced assumption**.
- The first report's figures (PV ≈ $307k, Macaulay ≈ 10.9 yr; 2037–42 PV ≈ $168k, 13.1 yr) **reproduce exactly**, but they assume payments on July 1. The client file says **beginning of year**.
- **Corrected, with payments on Jan 1:**
  - All ten payments: PV ≈ **$313.8k**, Macaulay ≈ **10.4 yr**, modified ≈ **9.95 yr**.
  - Payments 2037–42: PV ≈ $171.5k, Macaulay ≈ 12.6 yr.
- Reserve needed on 2033-01-01 (annuity-due at 4.5%): ≈ **$413.4k**.

## 6. Hold-to-maturity vs constant-duration (conceptual; unchanged)

- **Defined-maturity funds** (IBTM–IBTR) behave like one rung of a bond ladder. Duration falls over time, the fund pays out cash in December, and it then terminates [S3b]. Held to the end, the yield at purchase roughly locks in the value on the payment date. Each fund's proceeds must be kept in cash or T-bills for about two weeks until the Jan 1 payment.
- **Constant-duration funds** (IEF, TLT, XTEN) never mature, and their duration stays roughly constant [S15]. Their value on a payment date depends on rates at that moment. They only hedge the liabilities if the duration is rebalanced downward as the payments get closer.
- **For 2038–2042:** use individual Treasuries or STRIPS if the rules allow them (UNVERIFIED). Otherwise use a duration-matched mix of constant-maturity funds, rebalanced every year.

## Verification notes

- **Re-searched:**
  - Dec 2037+ iBonds: still none found.
  - BulletShares Treasury: **claim reversed**. The funds exist, 2027–2031, launched June 2026.
  - IBTR expense ratio: confirmed 0.07%.
  - IBTR 4.69% SEC yield: not found, so now UNVERIFIED.
  - GOVZ expense ratio: resolved to 0.10%.
  - EDV expense ratio: confirmed.
  - SGOV/BIL expense ratios: confirmed.
  - IEF duration: sources conflict.
- **Arithmetic:** The original figures reproduce under the July 1 assumption. Corrected to beginning-of-year timing as the client file requires.
- **Mapping fix:** Dec-year funds pay for the *following* January's payment. Coverage is now IBTM–IBTR for 2033–2037, and 2038–2042 is uncovered.
- Figures still resting on one snippet (IBTP, IBTQ, VGIT, VGLT, UTEN, ZROZ expense ratios; TLT duration) are marked "(snippet)" or UNVERIFIED.

## Sources (all retrieved 2026-09-27)
- [S1] https://www.ishares.com/us/products/342105/ishares-ibonds-dec-2035-term-treasury-etf (first report)
- [S2] https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf ; https://cbonds.com/etf/229909/ (first report)
- [S3b] https://www.investing.com/etfs/ibtr ; https://www.aaii.com/etf/ticker/IBTR ; https://www.blackrock.com/us/individual/literature/fact-sheet/ibtr-ishares-ibonds-dec-2036-term-treasury-etf-fund-fact-sheet-en-us.pdf (blocked)
- [S4]–[S7], [S9], [S13]–[S15]: as in the first report
- [S8b] https://www.prnewswire.com/news-releases/invesco-increases-optionality-of-its-bulletshares-defined-maturity-etf-suite-by-adding-treasury-bond-etfs-302796172.html (blocked, snippet only) ; https://etfdb.com/innovative-etfs-content-hub/invesco-grows-bulletshares-suite-treasury-etfs/
- [S10b] https://www.aaii.com/etf/ticker/GOVZ ; https://cbonds.com/etf/9375/
- [S11b] https://advisors.vanguard.com/investments/products/edv/vanguard-extended-duration-treasury-etf
- [S12] https://www.ishares.com/us/literature/fact-sheet/ief-ishares-7-10-year-treasury-bond-etf-fund-fact-sheet-en-us.pdf (blocked)
- [S12b] https://gomdorieconomic.com/2026/05/01/ief-ishares-7-10-year-treasury-bond-etf-analysis/
- [S16b] https://etfbff.com/research/compare/sgov-vs-bil/ ; https://www.optimizedportfolio.com/sgov-vs-bil/
- [S17] https://www.ishares.com/us/products/328944/ (IBTM) ; https://www.ishares.com/us/products/314830/ishares-ibonds-dec-2030-term-treasury-etf (IBTK)
- [S18] https://www.kiplinger.com/investing/etfs/best-target-maturity-bond-etfs-for-a-reliable-income-ladder ; https://www.blackrock.com/us/financial-professionals/insights/maturing-ibonds-etfs
- Client file: /home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt (lines 59, 88–90)