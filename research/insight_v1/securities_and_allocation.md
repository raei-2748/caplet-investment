# Securities and allocation: final WInS holdings and Laura's instrument map (insight_v1, writer W1)

**Summary:** WInS book (ii)R (Laura's plan on 2 Jan 2028, scaled to $300,000): IEF 23.5% + TLH 42.5% (operations hedge), building minimum 24.3% (2032 Treasury note, else IBTM, else VGIT/SPTI), VT 8.7%, cash about 1%. Fallbacks: stand-in minimum, book (iii), or the ALT book. Laura's real plan: a ten-rung STRIPS ladder in 2027; in 2028, completion, then a zero-coupon Treasury repaying the $150,000, then one world stock fund; nothing traded in 2031; the ladder becomes the operating reserve in 2033 and runs down to 2042 (E6 s0, s4, s5; INT).

**Serves: Trading Notes (TN)** (the WInS holdings the notes quote) **and IPS** (the instruments behind blocks B3, B4, B6, B8 and B10; the IPS itself names no ticker). Authority: `research/insight_v1/phase_E/E6_final_spec.md`; fund facts copied from `wins_now/securities_and_allocation_v1.md` s12 ("ticket v1"). Supersedes ticket v1 s1 and s11 for the book and the long-term map (E6 s5.1, s9 #1, #5, #7). PROVISIONAL until the team votes. AI-generated research; no deliverable text.

**Labels:** VP = verified on the primary page (agent and date named); VRF = official repo file; SNIP = snippet; ASM = assumption; MODEL = model output, not a forecast; DER = W1's arithmetic from labelled inputs; INT = judgement; UNVERIFIED = not checked.
**Terms:** *ETF* = fund traded like a share. *Treasury* = U.S. government bond. *STRIPS / zero-coupon* = a Treasury paying one amount on one date. *Rung* = one ladder bond. *Duration* = about the % a bond fund falls if rates rise 1 percentage point. *Position limit* = the most WInS allows in one security. *Expense ratio* = the fund's yearly cost as a % of the money in it. *NAV* = net asset value per share. *bp* = 0.01 percentage point. *Accrued interest* = interest built up since the last coupon, paid by the buyer.

**Every ticker below is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (no separate approved list this season; "Any ETF available on WInS", VP via ticket v1).

---

## 1. Final WInS holdings: recommended book (ii)R (E6 s5.1-5.2)

Illustration at 2026-09-25 closes; recompute shares from the last close (T2 finding 1). $ and shares DER.

| Holding | Job / role word | Weight | $ at $300k | ~Shares | Alternates | 2025-26 list (history only, VRF) |
|---|---|---|---|---|---|---|
| IEF | Operations hedge: future funding | 23.5% | $70,500 | ~783 | VGIT, then SPTI (re-solve: VGIT 16.6 / TLH 49.4) | yes |
| TLH | Operations hedge: future funding | 42.5% | $127,500 | ~1,365 | IEF 40.9 + TLT 25.1 if TLH is missing | no (TLT yes) |
| 4.125% Treasury note 15-Nov-2032 (CUSIP 91282CFV8), else IBTM | Building minimum: risk management or future funding (one word, recorded) | 24.3% | $72,900 | note ≈ $75k face (≈ $72,570 at model 95.27 clean + 1.49 accrued, ASM, D1); IBTM ~3,336 | VGIT (~1,281), then SPTI (~2,669), "moves like, not dated" | IBTM no; VGIT no |
| VT | Stock fund: growth | 8.7% | $26,100 | ~163 | VTI + VXUS 62/38 (~42 / ~114 sh); then ITOT + IXUS | VT, VTI, VXUS yes; ITOT, IXUS not found (W1 grep, 2026-09-28) |
| Cash | Liquidity | ~1% | ~$2,990 after 4 × $25 | - | at least $1,000 | - |

- Why these weights: the plan on 2 Jan 2028 is ladder 65.9%, minimum 25.3%, stock fund 8.7% of about $464k (MODEL, E6 [7]); the float comes out of the minimum (DER).
- Hedge mix 35.6/64.4 gives "about 10 years", like the payments (IEF 6.86y, TLH 11.58y on 9/25, VP via ticket v1; liability 9.90y, VRF).
- Wording constraints for the WInS holdings: never "Laura's portfolio" (Asset Manager Code F.2, VP via D10); the funds "stand in for" / "move like" her bonds.

## 2. Fallback books (E6 s5.10)

| Trigger | Holdings at $300k (illustration, DER) |
|---|---|
| No dated 2032 instrument listed | As section 1 with VGIT (else SPTI) as the minimum's stand-in; never claims a date |
| Two-reader check fails twice → (iii) | IEF 34.9% $104,700 / TLH 63.1% $189,300, re-priced to the trade-date ladder cost; then SGOV (else BIL, SHV) with the leftover only if ≥ $1,000 (~$4,500); otherwise a listed dated payment rung; otherwise revert to (ii)R |
| Team votes ALT | IEF 23.5 / TLH 42.5 / VT 17.0 ($51,000) / VGSH 16.0 ($48,000) / cash 1; growth-money bond choice recorded before the VGSH order |

## 3. Position-limit branches (E6 s5.3; ticket v1 s3)

| Limit shown | Book (ii)R |
|---|---|
| None, or ≥43% | Section 1 |
| 25-42% | IEF 23.5 / TLH at cap − 1 / SPTL rest of hedge; minimum one point under the cap if the cap is under 25.3%. At 25%: IEF 23.5 / TLH 24 / SPTL 18.5 / IBTM 24 / VT 8.7 / cash ~1.3% (5 ETF trades, $125) |
| Under 25% | IEF, TLH, SPTL at cap − 1; VGIT then VGLT take the rest; minimum: IBTM at cap − 1, rest in VGIT (VGIT's two parts count as one holding). 5 or more hedge funds needed (cap ≈ 17% or less): stop and ask Wharton |
| Separate, higher bond limit | The 2032 note may carry the whole minimum |

Never add within one point of a cap; a 20-24% stock fall (or 10-12% plus a 50bp rally) can lift TLH over a 25% cap (T2 [5], ASM).

## 4. The dated Treasury / IBTM item and its fallback (E6 s5.2, D4; ticket v1 s7)

| Choice | Instrument | Facts | Rules |
|---|---|---|---|
| 1 | 4.125% Treasury note, 15 Nov 2032, CUSIP 91282CFV8 | Exists and is strippable (Treasury MSPD Table V, 2026-08-31, VP per S1 via D1); matures 47 days before 1 Jan 2033 (DER); model price 95.27 clean + ~1.49 accrued per 100 on 9/25 (ASM, D1); WInS shows its own price; bond prices update once a day (ticket v1 s7) | Find it in the Bonds drop-down by maturity; $10 commission; buyer pays accrued interest. Listing is UNVERIFIED |
| 2 | IBTM (iShares iBonds Dec 2032 Term Treasury ETF) | NAV $21.83 (9/25); expense 0.07%; effective duration 5.05y; 15 Treasuries maturing Apr-Sep 2032; about $555m net assets; about 216k shares/day. Funds "will terminate on or about October or December 15 of the year in each Fund's name" and "do not seek to return any predetermined amount" (both re-read by E6 on ishares.com, 2026-09-28, VP) | Describe only as "a fund that ends in December 2032"; never "repays $X". Listing is UNVERIFIED |
| 3 | VGIT, then SPTI (undated stand-in, about 4.8-4.9y) | See section 6 | "Moves like a Treasury maturing in late 2032"; never a date. The real plan is unchanged |

## 5. Laura's long-term instrument map (the real plan, not WInS; E6 s1, s4)

| Date | Instrument | Size (MODEL/ASM at the 2026-09-25 curve) | Rule |
|---|---|---|---|
| 1 Jan 2027 | Ten Treasury STRIPS, each maturing 15 Nov 2032 … 15 Nov 2041, before one $50,000 payment (1 Jan 2033-2042). First rung: principal STRIP 912821KC8 (VP per S1 via D1) | Model cost $294,387 for Nov-15 dates, headroom $5,613 (19bp) (VRF inputs, ASM method; a model price, not a STRIPS quote). About 1 in 3 rate paths cost more than $300k (MODEL 30-34%) | R1: buy all at once on arrival; if short, longest-dated first; leftover waits in Treasury bills |
| 1 Jan 2028 | (1) Any unbought rung; (2) the building minimum: a zero-coupon Treasury maturing before 1 Jan 2033 repaying $150,000 face (the 15-Nov-2032 STRIP is the natural candidate, INT); (3) one broad world stock fund (VT-type, about 10,000 companies; alternates VTI + VXUS, ITOT + IXUS) | Minimum costs about $118k at the 5-year 4.98% (ASM); stock fund about $40k = 8.7% of all money (MODEL). Rates -50bp first: fund ~$31k; -100bp: ~$15k; -150bp: no fund, minimum ~$147k (E4 [7], MODEL) | R2: same order if the deposit is smaller or late. Joint tail: if rates fell and the deposit is smaller than the unbought part, all of it completes payments and the unfunded part of the first payment is stated ($11,957 at -50bp or $31,413 at -100bp with no deposit, MODEL) |
| 2028-2032 | Stock fund held | - | R6: never rebalanced against the Treasuries, never sold before 1 Jan 2033 |
| 1 Jan 2031 | Nothing traded | Range method only: bottom = minimum owned; top = minimum + half the stock fund's value that day (no figures here) | R4 |
| 1 Jan 2033 | Ladder named the operating reserve; pays the first $50,000 at once (2032 rung matured 15 Nov, waited in bills) | About $395k market value on today's forwards (ASM), cost ~$292-294k, face $500k | R3: held to maturity; each rung matures about 47 days before its payment and waits in Treasury bills; nothing sold early |
| 1 Jan 2033 | Gift = minimum + half the stock fund, never above the announced top; kept money to U.S. dollar Treasury bills | - | R5: no New Taiwan dollar conversion or currency hedge before the facility decision (a forward is a derivative) |
| 2033-2042 | Reserve run-down: one rung pays each 1 Jan | Empties by 1 Jan 2042 | R3 |

Permitted-instrument reading for the real plan: Treasuries (STRIPS and one zero for the minimum), one broad stock ETF and Treasury bills; no derivatives (R-AN15 safe reading, E6 s8c).

## 6. Fund facts (VP: read by T1 on the issuer pages, 2026-09-28 about 00:35 UTC, per ticket v1 s12; not re-opened by W1 except where stated)

| Ticker | Issuer source | Expense | Duration (as of) | Close (as of) | Other |
|---|---|---|---|---|---|
| IEF | ishares.com/us/products/239456 | 0.15% | 6.86y (9/25) | $90.00 (9/25) | 16 holdings; $41.57bn; 30-day volume 8.83m |
| TLH | ishares.com/us/products/239453 | 0.15% | 11.58y (9/25) | $93.38 (9/25) | 61 holdings maturing 2037-2046, 74.7% after 2042 (S1); $10.53bn; 1.97m/day |
| TLT | ishares.com/us/products/239454 | 0.15% | 14.84y (9/25) | $79.32 (9/25) | 47 holdings maturing 2044-2056 |
| SPTL | ssga.com (SPDR Portfolio Long Term Treasury ETF) | 0.03% gross | 13.65y OAD (9/24) | $24.27 (9/24) | 110 holdings; $10.95bn |
| SPTI | ssga.com (SPDR Portfolio Intermediate Term Treasury ETF) | 0.03% | 4.78y OAD (9/24) | $27.31 (9/24) | - |
| VGIT / VGLT | investor.vanguard.com API | 0.03% | 4.9y / 13.5y (8/31) | $56.90 / $50.98 (9/25) | 102 / 101 bonds |
| IBTM | ishares.com/us/products/328944 | 0.07% | 5.05y (9/25) | $21.85 close; NAV $21.83 (9/25, E6 re-read 2026-09-28) | 15 holdings; ends Dec 2032 |
| VT | investor.vanguard.com API | 0.06% (S2/S3) | n/a | $160.03 (9/25) | 10,088 stocks, 37.7% non-U.S. (8/31); top ten 21.7% (6/30) |
| VTI / VXUS | investor.vanguard.com (VXUS via S3) | 0.03% / 0.05% (S2) | n/a | $379.77 / $86.35 (9/25) | - |
| VGSH / SHY | Vanguard API / ishares 239452 | 0.03% / 0.15% | 1.9y (8/31) / 1.79y (9/25) | $57.59 / $81.21 (9/25) | ALT book only |
| SGOV / BIL / SHV | ishares 314116 / ssga.com / (S1) | 0.09% / 0.1353% / 0.15% | ~0.1y / 0.10y / 0.28y | $100.66 (9/25) / $91.58 (9/24) | (iii) only; BIL yield to maturity 3.94% (9/24) |

ITOT, IXUS: no facts in ticket v1 (UNVERIFIED; read the issuer page before use).

---

## What this teaches
1. A holding is chosen for its job and its date, not its name: the same Treasury fund can be "hedge" or "stand-in" only if the note says which.
2. Every pick needs a pre-agreed substitute, because a security you cannot buy on the day is a plan you do not have.
3. WInS shows one dated snapshot of a longer plan; saying the date out loud keeps the notes honest.
