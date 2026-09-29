# Literature base for Root-and-Branch (WS5)

Team Caplet, Wharton GHSIC 2026-27, client Laura Gao. Built 2026-09-30 (Sydney).

20 references. Every DOI below was resolved by WS5 on 2026-09-30 through the doi.org handle API
(response code 1 = resolves; log in `_resolve/doi_check.txt`), and its metadata (authors, year, title,
journal, volume, pages) was taken from Crossref, not typed from memory. Re-check at any time with
`python rab/literature/verify_dois.py`.

**How closely each summary was checked** (column "Read"):
- **A** = WS5 read the abstract or full text (OpenAlex, Crossref, or an open copy).
- **S** = paywalled and no abstract online. Metadata is resolved; the summary rests on a named secondary
  source (given in the entry). Team: do not quote these papers directly without reading them.

The plan elements referred to below: **Root** (the 2027 deposit buys Treasuries dated to the ten $50k
payments), **Floor** (part of the 2028 deposit buys Treasuries that repay that deposit by late 2032),
**Branch** (the rest of the 2028 deposit goes into a global stock fund, VT), **Range** (in 2031 the
co-sponsors are told a range, from the floor up to the floor plus half the stock fund), **Cap** (the 2033
contribution is capped at the top of that range).

---

## 1. Matching dated payments with dated bonds (the Root)

**[1] Leibowitz, M. L. (1986).** The dedicated bond portfolio in pension funds, Part I: Motivations and
basics. *Financial Analysts Journal, 42*(1), 68-75. https://doi.org/10.2469/faj.v42.n1.68 (Read: S)
- A "dedicated" (cash-matching) portfolio buys bonds that are held to maturity so that their coupons and
  repayments arrive when the fund's payments fall due. Leibowitz is the main author on the method and
  treated it as the simplest form of immunization. (Secondary source: Wikipedia, "Dedicated portfolio
  theory", History section, read 2026-09-30.)
- **Supports the Root.** This is the Root, in its textbook form: one Treasury per $50k payment, held to
  maturity, so rate moves after purchase do not change what Laura's charity receives.

**[2] Ang, A., Chen, B., & Sundaresan, S. (2013).** Liability-driven investment with downside risk.
*Journal of Portfolio Management, 40*(1), 71-87. https://doi.org/10.3905/jpm.2013.40.1.071 (Read: A)
- Values the shortfall between assets and liabilities as an option and finds the best portfolio. A fund
  whose liabilities are already well covered can afford to put the extra into risky assets. A badly
  underfunded one is pushed to gamble.
- **Supports the Branch.** Once the Root and the Floor are fully funded, putting the rest in stocks is
  what LDI theory recommends, not a gamble. It also explains why we fund the payments first: an
  underfunded plan is the one pushed into risky bets.

## 2. Safety first, a floor plus upside, and portfolio insurance (Floor + Branch)

**[3] Roy, A. D. (1952).** Safety first and the holding of assets. *Econometrica, 20*(3), 431 (first page; registries give no end page).
https://doi.org/10.2307/1907413 (Read: S)
- Proposes choosing the portfolio that makes a "disaster" outcome, a return below a minimum level, as
  unlikely as possible, instead of maximising average return. (Secondary: Wikipedia, "Roy's safety-first
  criterion", read 2026-09-30.)
- **Supports the plan's order of priorities.** For Laura the disaster is a missed $50k payment or losing
  the 2028 deposit. The Root and the Floor push that chance close to zero before any upside is sought.

**[4] Perold, A. F., & Sharpe, W. F. (1988).** Dynamic strategies for asset allocation. *Financial
Analysts Journal, 44*(1), 16-27. https://doi.org/10.2469/faj.v44.n1.16 (Read: A)
- Compares buy-and-hold, constant-mix and portfolio-insurance rules. Buy-and-hold has a minimum return
  set by the amount in safe assets and an upside set by the amount in stocks. Insurance rules (CPPI,
  option-based) sell as markets fall and do badly when markets swing back and forth.
- **Supports Floor + Branch as a buy-and-hold design.** The 2028 book is exactly their buy-and-hold case:
  the worst case is known (the Floor) and the upside follows the stock market. No trading rule is needed,
  so the whipsaw weakness they describe does not apply.

**[5] Black, F., & Perold, A. F. (1992).** Theory of constant proportion portfolio insurance. *Journal of
Economic Dynamics and Control, 16*(3-4), 403-426. https://doi.org/10.1016/0165-1889(92)90043-E (Read: S)
- The formal theory of CPPI: keep a floor, call the value above it the "cushion", and hold stocks worth a
  fixed multiple of the cushion. (Secondary: Wikipedia, "Constant proportion portfolio insurance", which
  credits Black and Perold for equity CPPI, read 2026-09-30.)
- **Supports and places the design.** Root-and-Branch is the simplest member of this family: the floor is
  bought once, in Treasuries, and the stock holding is only the cushion itself (a multiple of 1, never
  rebalanced). We give up the extra upside of a higher multiple, and in return the floor cannot be
  broken by a crash.

**[6] Rubinstein, M. (1988).** Portfolio insurance and the market crash. *Financial Analysts Journal,
44*(1), 38-47. https://doi.org/10.2469/faj.v44.n1.38 (Read: S)
- Written after the October 1987 crash by a co-inventor of portfolio insurance (Wikipedia, "Portfolio
  insurance": pioneered by Leland and Rubinstein). It looks at how dynamic insurance, which sells into
  falling markets, behaved in the crash. Team: read the paper before stating its conclusions.
- **Challenges dynamic insurance, not our plan.** Insurance that relies on trading during a crash is
  fragile. Our Floor is Treasuries held to maturity and needs no trades in a crash. Triage: *ignore*
  (no change). One line in the Final Report could say why we chose a static floor.

**[7] Dybvig, P. H. (1999).** Using asset allocation to protect spending. *Financial Analysts Journal,
55*(1), 49-62. https://doi.org/10.2469/faj.v55.n1.2241 (Read: A)
- For an educational endowment: keep enough in safe assets to fund promised spending, invest the rest in
  risky assets, and so protect spending in down markets while sharing in up markets. Does best when
  markets trend and worst when they zig-zag.
- **Strong support for the whole structure.** This is the closest published match to Laura's problem, a
  charity with promised payouts. Safe assets for the promises (Root), risky assets for the rest (Branch).

## 3. Goals-based investing (why separate "must pay" money from "could grow" money)

**[8] Shefrin, H., & Statman, M. (2000).** Behavioral portfolio theory. *Journal of Financial and
Quantitative Analysis, 35*(2), 127-151. https://doi.org/10.2307/2676187 (Read: A)
- Real investors build "layered pyramids": a low layer to avoid poverty and a high layer for a shot at
  riches, held in separate mental accounts. The best portfolios look like safe bonds plus lottery-like
  upside.
- **Supports the two-layer idea.** Root and Floor are the "avoid disaster" layer and the Branch is the
  upside layer, and donors can see which dollars do which job.

**[9] Chhabra, A. B. (2005).** Beyond Markowitz: A comprehensive wealth allocation framework for
individual investors. *Journal of Wealth Management, 7*(4), 8-34. https://doi.org/10.3905/jwm.2005.470606
(Read: A)
- Splits wealth by the risk each part must handle (personal safety, market, aspirational). Investors can
  accept a slightly lower average return for downside protection plus upside. Main line: risk allocation
  should come before asset allocation.
- **Supports the plan's sequencing.** We decide first what must be certain (the ten payments, the 2028
  deposit) and only then how to invest the rest.

**[10] Das, S., Markowitz, H., Scheid, J., & Statman, M. (2010).** Portfolio optimization with mental
accounts. *Journal of Financial and Quantitative Analysis, 45*(2), 311-334.
https://doi.org/10.1017/S0022109010000141 (Read: A)
- Shows that running separate goal "accounts", each with a threshold and a chance of missing it, adds up
  to a portfolio that is still efficient in the Markowitz sense, and the constraints cost very little.
- **Defends against the critique that one optimised portfolio would beat buckets.** Splitting money by
  goal costs almost nothing in efficiency and is far easier to explain.

**[11] Das, S. R., Ostrov, D., Radhakrishnan, A., & Srivastav, D. (2018).** A new approach to goals-based
wealth management. *Journal of Investment Management, 16*(3), 1-27. SSRN version
https://doi.org/10.2139/ssrn.3117765; open copy https://srdas.github.io/Papers/GBWM.pdf (Read: A, full text)
- Defines risk as the chance of not reaching a goal, not the ups and downs of the portfolio. Their Table 1
  (from Brunel 2015) links goal types to target success rates: needs 90-95%, wants 80-85%, wishes
  65-75%, dreams 50-60%.
- **Supports the Range and the Cap.** The ten payments are "needs" and the Root makes them close to
  certain. The top of the 2031 range is a "wish" or "dream", so capping the 2033 gift at the top of the
  range, rather than promising it, is the honest framing.

**[12] Brunel, J. L. P. (2015).** *Goals-based wealth management: An integrated and practical approach to
changing the structure of wealth advisory practices.* Wiley. https://doi.org/10.1002/9781119025306
(Read: S, via Das et al. 2018, pp. 3-7)
- A practitioner book on goals across several time horizons. It gives equal weight to "avoiding
  nightmares" and "realising dreams" and turns client wording into target probabilities (the table in [11]).
- **Supports how we talk to the co-sponsors.** Give each goal a plain-language tier and a matching
  probability instead of a volatility number.

## 4. Global market-cap stocks as the default risky asset (the Branch)

**[13] Sharpe, W. F. (1991).** The arithmetic of active management. *Financial Analysts Journal, 47*(1),
7-9. https://doi.org/10.2469/faj.v47.n1.7 ; author copy https://web.stanford.edu/~wfsharpe/art/active/active.htm
(Read: A, full text)
- Before costs, the average actively managed dollar must earn the same as the average passive dollar.
  After costs it must earn less. This follows from arithmetic alone.
- **Supports holding the whole market through one low-cost fund (VT)** instead of picking stocks. It also
  fits WInS's $25 commission per trade: fewer trades cost less.

**[14] Doeswijk, R., Lam, T., & Swinkels, L. (2014).** The global multi-asset market portfolio,
1959-2012. *Financial Analysts Journal, 70*(2), 26-41. https://doi.org/10.2469/faj.v70.n2.1 (Read: A)
- Estimates the size of the world's invested market portfolio and argues it is a natural benchmark for
  strategic asset allocation.
- **Supports market-cap weights as the neutral default** for the Branch: a global fund weighted by market
  size makes no bet on any country. Note: their portfolio includes bonds. VT is the equity slice only,
  and our bonds sit in the Root and the Floor.

**[15] Anarkulova, A., Cederburg, S., & O'Doherty, M. S. (2022).** Stocks for the long run? Evidence from a
broad sample of developed markets. *Journal of Financial Economics, 143*(1), 409-433.
https://doi.org/10.1016/j.jfineco.2021.06.040 ; SSRN abstract https://doi.org/10.2139/ssrn.3594660
(Read: A, SSRN abstract)
- 39 developed markets, 1841-2019. Long-run stock results are very uncertain. They estimate a 12% chance
  that a diversified investor with a 30-year horizon loses money after inflation.
- **Challenges any promise about the Branch and supports the Floor and Cap.** Stocks are not safe just
  because the horizon is long, so the Branch must not fund the $50k payments and the 2031 range must
  start at the floor. Triage: *note in Final Report* (the plan already does this; cite this paper as
  the reason).

**[16] Bodie, Z. (1995).** On the risk of stocks in the long run. *Financial Analysts Journal, 51*(3),
18-22. https://doi.org/10.2469/faj.v51.n3.1901 (Read: A)
- If stocks got safer over longer horizons, insuring against them doing worse than safe bonds would get
  cheaper as the horizon lengthens. Bodie shows it gets more expensive. For anyone owing fixed-dollar
  amounts, stocks are not a better hedge for longer-dated debts.
- **Supports dating a Treasury to every payment, even the 2042 one**, instead of assuming stocks will
  "catch up" over 15 years.

## 5. The cost of certainty: nominal Treasuries vs TIPS

**[17] Campbell, J. Y., & Viceira, L. M. (2001).** Who should buy long-term bonds? *American Economic
Review, 91*(1), 99-127. https://doi.org/10.1257/aer.91.1.99 (Read: A)
- For cautious long-term investors the safe asset is a long-term bond, not cash. Inflation-indexed bonds
  are the best version, and nominal bonds can do the job when inflation risk is low.
- **Supports and qualifies the Root.** Long-dated Treasuries, not cash, are the safe asset for payments
  due in 2033-2042. The qualification: Laura's payments are fixed dollars, so nominal Treasuries match
  them exactly, but inflation will shrink the real value of each $50k. Triage: *note in Final Report*
  (state that the payments are fixed in dollars, and show their real value; WS3's stress table covers
  this).

**[18] Fleckenstein, M., Longstaff, F. A., & Lustig, H. (2014).** The TIPS-Treasury bond puzzle. *Journal
of Finance, 69*(5), 2151-2197. https://doi.org/10.1111/jofi.12032 (Read: A)
- A TIPS bond plus an inflation swap can copy a normal Treasury's cash flows. That copy has often been
  cheaper, by more than $20 per $100 at times, so nominal Treasuries are almost always overpriced
  relative to TIPS.
- **Mild challenge to the Root's cost.** In principle an expert could lock in the same dollars more
  cheaply. For us it does not apply: it needs inflation swaps, and whether WInS lists TIPS is
  UNVERIFIED. Triage: *ignore* (no change).

## 6. Telling non-experts about ranges and uncertainty (the Range)

**[19] van der Bles, A. M., van der Linden, S., Freeman, A. L. J., & Spiegelhalter, D. J. (2020).** The
effects of communicating uncertainty on public trust in facts and numbers. *Proceedings of the National
Academy of Sciences, 117*(14), 7672-7683. https://doi.org/10.1073/pnas.1913678117 (Read: A)
- Five experiments (n = 5,780, including a BBC News field test). Showing uncertainty caused only a small
  drop in trust, and the drop was mostly for vague verbal wording, not numeric ranges.
- **Supports giving the co-sponsors a numeric range in 2031** (floor to floor + half the Branch) instead
  of one number or vague words such as "probably around". Triage: *note in Final Report*. Check that the
  IPS states the range in numbers.

**[20] Spiegelhalter, D., Pearson, M., & Short, I. (2011).** Visualizing uncertainty about the future.
*Science, 333*(6048), 1393-1400. https://doi.org/10.1126/science.1191181 (Read: A)
- Reviews how to show probabilities to lay audiences with pictures. The best format depends on how
  comfortable the audience is with numbers, and letting people choose between views helps.
- **Supports the range explorer and a simple picture of the Range** (floor as a solid bar, upside as a
  shaded band) for the co-sponsors, and keeping it plain for non-experts.

---

## Contradiction triage (rule: do not change the strategy)

| Source | Finding that pushes against the plan | Class | What to do |
|---|---|---|---|
| [15] Anarkulova et al. | Stocks can lose after inflation even over 30 years | note in Final Report | Already built in (Range starts at Floor; Cap). Cite as the reason. |
| [17] Campbell & Viceira | Nominal bonds leave inflation risk | note in Final Report | Say the payments are fixed dollars; show their real value (WS3). |
| [18] Fleckenstein et al. | TIPS + swaps can be cheaper than Treasuries | ignore | Not available to us; TIPS on WInS UNVERIFIED. |
| [6] Rubinstein; [4] Perold & Sharpe | Dynamic insurance fails in crashes and choppy markets | ignore | Our floor is static; could be one line of rationale. |
| [19] van der Bles et al. | Vague words cut trust more than numbers | note in Final Report | Check the IPS states the 2031 range as numbers. |

Nothing found is *fix before 6 Nov*.

## Not used (checked and left out)

- Leland (1980), "Who should buy portfolio insurance?", *J. Finance 35*(2), https://doi.org/10.1111/j.1540-6261.1980.tb02190.x.
  Resolves, but WS5 could not access its content, and [4] covers the same ground.
- Redington (1952), immunization, https://doi.org/10.1017/S0020268100052811. Resolves, but it is a
  historical source only.
- Roll (2004), "Empirical TIPS", https://doi.org/10.2469/faj.v60.n1.2591. Resolves, but it is not needed
  beyond [17]-[18].
