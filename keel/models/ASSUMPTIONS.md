# Model Suite: assumption log

AI-generated (Claude Code), Tue 27 Oct 2026. MODEL, not a forecast. Every number in `README.md` rests on the rows
below; the code cites them as `[Axx]`. Change one, re-run `run_suite.py`, and say which row moved.

## Market and curve
| # | Assumption | Value / source | Why, and what it does to the answers |
|---|---|---|---|
| A01 | Treasury curve | treasury.gov par curve, **22 Oct 2026** (newest on file: `keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv`). Bootstrapped cost of the ten cheques on 1 Jan 2027 **$298,861**, headroom **$1,139 = 3.8bp**, DV01 $296/bp | Same method as `keel/scripts/ladder_pv.py`; matches the Window's 26 Oct figure |
| A02 | Curve moves | the 22 Oct shape is kept; yields move in parallel (twists only in M3); par yields used as zero rates inside paths, anchored to the bootstrapped headline | As `ips_numbers.py`; roll-down ignored for the ladder (it is held to maturity) |
| A03 | Holdings | the 11 WInS fills: IBTM, IBTO, IBTP, IBTQ, IBTR (Dec 2032-36) and T 4.75% Feb-37, 4.50% May-38, 4.375% Nov-39, 4.25% Nov-40, 3.125% Nov-41. iBond funds treated as par bonds paying their yield, held to their December end (pull to par) | Fund fees (~0.07%) and WInS commissions ignored: a few hundred dollars over the decade |
| A04 | Yield volatility (house model) | random walk, **1.0 point a year** (GS10 12-month change sd 1953-2026 = 1.08) | No mean reversion, so the long tail of the coupon gap is harsher than history (compare M7 history rows) |
| A05 | Yield floor | 0.25% | |
| A06 | World stocks | J.P. Morgan 2027 LTCMA global equities **7.5% compound**; vol **16.78%** (2026 LTCMA AC World); lognormal monthly | The house assumption of every lab run since 27 Oct |
| A07 | VT stand-in in history | Shiller's US S&P Composite total return. US stocks beat the world over 1871-2023, so "raw history" flatters stocks; the "level reset" worlds put the median back to 7.5% | Rivals look better in raw history than in the 7.5% worlds; XR barely moves |
| A08 | Coupon reinvestment | each coupon buys a zero to its bond's own maturity at that day's yield (build yield + parallel move since) | Same as `ips_numbers.py`; this is the "one soft spot" of V25 |
| A09 | Stocks vs yields | independent in the house model (R05 ran rho 0.5); the regime, bootstrap and history worlds carry history's own link (storms pull yields down) | |
| A10 | US inflation | AR(1) on monthly CPI moves fitted 1953-2023, mean reset to J.P. Morgan's 2.5% (house and regime); history's own CPI (bootstrap, replays) | Only M4 uses it: the cheques are fixed dollars |
| A11 | Taiwan dollar | stationary bootstrap (12-month blocks) of real monthly TWD/USD moves Oct 1983-Sep 2026 (FRED H.10 via the Frictionless Data mirror); drift removed in the base case, kept as a sensitivity (the TWD rose ~0.5% a year) | |

## Laura's plan (Caplet XR)
| # | Assumption | Value / source | Why |
|---|---|---|---|
| A12 | Plan modelled | IPS V25 (27 Oct): Jan 2027 the $300k buys the ladder; any gap is the 2028 deposit's first job; any leftover sits in bills | `/mnt/project-files/ips/rewrite/V25/`; rules as `ips_numbers.py` |
| A13 | 2 Jan 2028 | R = deposit - gap; IBTM sized to grow back to R by Dec 2032 (the floor); the rest into VT | |
| A14 | The 2031 range | bottom = R - $3,700 rounded down to $5k; top = R + half of VT (Jan 2031) | M6 varies the share |
| A15 | Jan 2033 re-match | the coupon gap projected at Jan 2033 yields is set aside in bills from cash, then Laura's half, then the gift; bills earn nothing (conservative) | V25's "the reserve changes once" |
| A16 | The cap | the gift never exceeds the top; anything above it, and Laura's half, stays hers in VT | Shark Tank's missing cap (V25 review) |
| A17 | After 2033 | any gap beyond the set-aside is paid from what Laura kept, valued Jan 2042 (the L-10 / `ips_numbers.py` convention). "A cheque short" = more than $1,000 short | R10 counts the gap above the set-aside with no backstop, so its "short" rates are higher than ours |
| A18 | "Lock what you announce" (28 Oct champion) | Jan 2031: the gift's half of VT moves into a Treasury maturing Dec 2032 at the 2-year yield | `keel/ips_rewrite/lab/R08_core.py` |
| A19 | Cushion rule G | $7,500 on top of the projected gap, from cash, then Laura's half, then the gift down to the bottom, never below | `keel/ips_rewrite/lab/R10_lock_cushion.py` |

## Rival plans
| # | Assumption | Value / source | Why |
|---|---|---|---|
| A20 | Who the rivals are | Keel's own sketches of plans a strong team could file, not any real team's work; only Wharton-allowed instruments (VT, IEF/TLT-style Treasury ETFs, Treasury bills) | The rival-scan thread has the real field; these are the archetypes |
| A21 | Bond ETFs | constant-duration funds: IEF-like D 7 at the 8-year yield, TLT-like D 16 at the 20-year yield; monthly return = yield + roll-down - D x move + D^2/2 x move^2; no fees | Funds never mature: that is their risk |
| A22 | Rival gift (Jan 2033) | 60/40, glide, bucket: everything above a $500,000 reserve (the cheques' face value). Immunisation: everything above 1.05x the cheques' market value. Lock-late: everything not needed to buy the ladder in Jan 2032 (held in bills to 2033) | The commonest "keep enough, give the rest" rules |
| A23 | Rival 2031 range | their own projection of the 2033 gift (7.5% stocks, 8-year yield for bonds), plus or minus 20%; +/-40% as a sensitivity | |
| A24 | Immunisation margin | 5% above the cheques' value | |
| A25 | Pool mechanics | rebalanced each January; cheques drawn pro rata; bucket keeps three cheques in bills, refilled each January | |

## Worlds
| # | Assumption | Value / source | Why |
|---|---|---|---|
| A30 | Regime model | Hamilton two-state Markov model fitted by EM to monthly S&P log total returns, Jan 1871-Jun 2023: **calm** +1.14%/month, sd 2.84%; **storm** -1.75%/month, sd 7.71%; storms start 2.8% of months, last ~5.8 months, cover 14% of history | Fat tails come from both the storms and the t shocks |
| A31 | Shocks inside a regime | Student-t, degrees of freedom by moment matching: calm ~30 (near normal), storm **5.4** | |
| A32 | Yields by regime | fitted 1953-2023 with the smoothed regime odds: calm +0.7bp/month, storm **-4.4bp/month** (flight to Treasuries); drift demeaned so no long-run trend | |
| A33 | Level reset | regime and bootstrap stock paths shifted so the median compound return is 7.5%; "raw" keeps history's 9.2% | |
| A34 | History data | Shiller monthly via `datasets/s-and-p-500` on GitHub (Yale page blocked by the proxy), Jan 1871-Jun 2023 (dividends end there). Before 1953 Shiller's long rate is built from annual data, so its monthly moves are smoother than reality | `data/fetch_data.py`, `data/SOURCES.md` |
| A35 | History on today's curve | history's yield moves are applied **in proportion**: today's 10-year (4.96%) x (yield then / yield at the start) - 4.96%, as a parallel shift. The absolute mapping (also run) pushes 1980s disinflation through the 0.25% floor, which no real 5% curve could do | Both start a path on 1 Jan 2027's curve; history supplies the moves, not the levels |
| A36 | Block bootstrap | Politis-Romano stationary bootstrap, mean block 24 months, of joint (stocks, yield log moves, CPI) months, so each crash keeps its own rates and inflation | |

## Taiwan and price of certainty
| # | Assumption | Value / source | Why |
|---|---|---|---|
| A40 | Taiwan building-cost inflation | **2.0%** (Taiwan CPI Aug 2026 +2.04% y/y) and **3.5%** (construction cost index ~3.5% a year since 2021): both from the verified facts in `CLAUDE.md` (27 Sep 2026 run) | Taiwan CPI history could not be downloaded (World Bank excludes Taiwan; DGBAS blocked) |
| A41 | Inflation top-up | the dollars needed, valued 1 Jan 2033 at 4% a year, to lift each cheque back to what $50,000 bought in Taiwan in Jan 2027 | A yardstick, not a liability: the case fixes the cheques in dollars |
| A42 | Price of certainty, 1871-2026 | ten $50k payments 6-15 years ahead at a flat curve equal to that month's 10-year yield (Shiller to Jun 2023, then FRED GS10) | A flat curve slightly overstates the cost when the curve slopes up |

## Not modelled
Taxes, Taiwan law, the facility's cost (out of scope by the case); credit risk on Treasuries; WInS position limits;
the 1-in-a-hundred operational errors (a mis-click). Rival teams' real plans: see the rival-scan thread.
