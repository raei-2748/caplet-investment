# Kai's sources, H-026 round 1 (Tue 3 Nov 2026, about 18:30 Sydney)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), not for submission. Read on 3 Nov 2026. The live
hosts refused this session (HTTP 403 at the egress proxy for www.ishares.com, fred.stlouisfed.org, home.treasury.gov
and www.nber.org, 3 Nov 2026), so every quote below comes from a primary file already saved in the repo, named with
its path. Check each at the live source before the Final Report prints it.

## 1. iShares iBonds Dec 2032 Term Treasury ETF (IBTM), its own product page
- URL: https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf
- Copy read: `archive/rab/data/ishares/IBTM_product_page.html.gz` (saved 30 Sep 2026; page data "as of Sep 28, 2026"). Read 3 Nov 2026.
- Exact words:
  - "The iShares iBonds Dec 2032 Term Treasury ETF seeks to track an index of U.S. Treasury bonds maturing in 2032. The fund offers a way to seek income and stability, build a bond ladder, and manage interest rate risk with a defined maturity."
  - "During the final year of the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the liquidation of the fund. The investor's total realized yield to fund maturity will be influenced by the yield earned on these proceeds during the final year. If the future yield on cash equivalents is lower than the current Average Yield to Maturity for the portfolio’s bonds, the realized yield to fund maturity is also expected to be lower and vice versa."
  - "This estimate also reflects the deduction of the expense ratio (7 basis points)." Expense Ratio shown: "0.07%".
  - "An investment in the Fund(s) is not guaranteed, and an investor may experience losses, including near or at the termination date. Unlike a direct investment in a bond that has a level coupon payment and a fixed payment at maturity, the Fund(s) will make distributions of income that vary over time."
  - "The Funds’ distributions and liquidation proceeds are not predictable at the time of investment and the Funds do not seek to return any predetermined amount."
- The four later funds' pages (`IBTO`, `IBTP`, `IBTQ`, `IBTR` in the same folder) give the same expense ratio, 0.07%, and the same "seeks to track an index of U.S. Treasury bonds maturing in 20XX" line.
- What it means for us: (a) the cash wait inside each fund is iShares' own stated risk, so exhibit N is testing a real
  leg, not a hypothetical; (b) "mature" is iShares' own word ("defined maturity", "fund maturity"), so V54's "funds that
  mature like bonds" was never false and W5's "funds with an end date" was not needed for truth; (c) a sentence saying
  no cheque can be short, next to these funds, needs every rung to be a Treasury held until it pays (Kai's P3 change).

## 2. The same five funds' facts (iShares data, as of 28 Sep 2026)
- Copy read: `archive/rab/data/ishares/ibonds_facts.csv` (from the same iShares pages). Read 3 Nov 2026.
- Average yield to maturity / weighted average maturity / number of holdings: IBTM 5.11% / 5.75 yrs / 15; IBTO 5.14% /
  6.69 yrs / 11; IBTP 5.19% / 7.76 yrs / 4; IBTQ 5.22% / 8.75 yrs / 4; IBTR 5.23% / 9.56 yrs / 4.
- What it means: from 28 Sep 2026, those weighted maturities land in late June 2032, early June 2033, early July 2034,
  late June 2035 and mid-April 2036, so each fund's cash waits about 0.45 to 0.65 years for its 15 December close
  (IBTR longest). The chair's "spread Jan to mid-Dec" gives 0.48 years: close, slightly kind to IBTR.

## 3. The model's own note on the funds
- `keel/library/ips_numbers_2026-10/ips_numbers.py` line 37, verbatim: "# payment year: (holding, maturity, coupon % or
  None = iBond fund modelled as a par bond, coupon = its yield)"; lines 38-40 date each fund's maturity 15 December of
  its year. No fee and no final-year cash appear in the rung list.
- What it means: the "200,000 of 200,000" for the lock (L-17, KW) never looked inside rungs 2033-2037.

## 4. Do interest rates fall in a downturn? (W5 P4: "when interest rates usually fall")
- FRED DGS10, daily 10-year Treasury yield, copy `archive/rab/data/fred/DGS10.csv` (source
  https://fred.stlouisfed.org/series/DGS10). Read 3 Nov 2026. 2022-01-03: 1.63; 2022-06-14: 3.49; 2022-10-24: 4.25;
  2022-12-30: 3.88. So through the 2022 bear market the 10-year yield rose by about 2.6 points.
- FRED GS10, monthly 10-year yield, copy `keel/library/ips_numbers_2026-10/fred_GS10_monthly.csv` (source
  https://fred.stlouisfed.org/series/GS10). Read 3 Nov 2026. Change from each US recession's first month to its last
  month (peak and trough months are NBER's, written from memory because nber.org refused the connection: UNVERIFIED
  until read at https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions):
  1953-07 to 1954-05 -0.56; 1957-08 to 1958-04 -1.05; 1960-04 to 1961-02 -0.50; 1969-12 to 1970-11 -0.81;
  **1973-11 to 1975-03 +1.00 (6.73 to 7.73)**; 1980-01 to 1980-07 -0.55; 1981-07 to 1982-11 -3.73; 1990-07 to 1991-03
  -0.36; 2001-03 to 2001-11 -0.24; 2007-12 to 2009-06 -0.38; 2020-02 to 2020-04 -0.84.
- What it means: the 10-year fell in 10 of 11 recessions and rose in one; 2022 was a bear market in which rates rose
  but not a recession. "Usually" is true; "always" would be false. No case against W5 P4 on truth.

## 5. Kai's arithmetic for the sealed bet (Kai's own, not the model; script in /tmp, not in the repo)
- Each fund sized the model's way (a par bond paying $50,000 on 15 December, bought 1 Jan 2027 at iShares' yield
  above): faces $37,161 / $35,285 / $33,435 / $31,705 / $30,101, total about $167,700.
- Cash wait at a 0% bill rate, face x yield x wait: about $4,140 with the chair's uniform spread (0.48 yrs), about
  $4,420 with iShares' own weighted maturities. Fee at 0.07% a year over each fund's life: about $920.
- Priced on naming day (1 Jan 2031) the way KW prices its lock (cost = gap / (1 + y x years), y about 5%): about
  $3,480 (uniform) to $3,700 (weighted maturities).
- Loss including the fee, by the bill rate in the funds' final years: 4% -> about $1,860; 2% -> $3,460; 1% -> $4,260;
  0.25% (the model's floor) -> $4,860. Compare K0's unzeroed leg, the bill wait the ladder counts on: $4,345 at the
  22 Oct curve (Felix's C4, L-17), which cut base futures paying every cheque from 100% to 95.16% and the low-yield
  world's to 79.90%.
