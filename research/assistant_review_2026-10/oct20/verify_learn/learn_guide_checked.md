# Understand our own plan: a study guide for Team Caplet

> **CHECKED COPY (verify_learn, Tue 20 Oct 2026, about 12:10-13:30 Sydney).** An AI verifier (Claude Code) adversarially checked
> the original `oct20/learn/learn_guide.md` and changed it only where it was wrong, out of date or likely to mislead a student
> in front of a judge. Each change is marked **[checked: ...]**. The main changes:
> (1) Chapter 8's "16% vs 32%" example is rewritten to the reconciled explanation and agreed numbers (option 1 about 14.4%,
> 3r about 0.6%, top reached 77% / 45% / 76%; `oct20/reconcile3r/reconcile_3r.md` sections 4-5), and Q8.3 is replaced;
> (2) Chapters 5 and 12 and the glossary now use those agreed numbers in place of 15.6% / 0.02% / 41% / 72%;
> (3) the Spreadsheet Lab Step 7 formula now works as typed (a bare `y` gives an error in Google Sheets);
> (4) concept fixes: Macaulay vs modified duration, interest-on-interest (Q5.2), VT's role as cover, what the case asks
> for in the range, what basis D is. Everything else, including all other numbers and answers, was re-checked and left as it was.
> The full list with reasons is in `oct20/verify_learn/verify_learn.md`. Still AI study material: not text to submit.

**What this is.** Study material written by an AI (Claude Code) on Tue 20 Oct 2026 (Sydney) so that every student can explain Caplet's strategy in their own words. It is **not text to submit** and it drafts no TNA, IPS, Final Report or co-sponsor wording. If you use an idea or number from it in a deliverable, rebuild the number yourself first and log the AI help in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/, read 19 Oct 2026).

**Labels.** CASE = from the official case. MODEL = a computer estimate from AI-built scripts (not a fact). CALC = simple arithmetic done for this guide. UNVERIFIED = nobody could confirm it.

**Data date.** Unless a line says otherwise, numbers use the treasury.gov daily par yield curve for the **Mon 19 Oct 2026 close**: 6-month 4.37, 1y 4.50, 2y 4.77, 3y 4.85, 5y 4.94, 7y 5.04, 10y 5.15, 20y 5.53, 30y 5.48 (3-month bill 4.27). Every market number here will be out of date within days. The golden rule from the numbers desk still applies: **say a number with its date and basis, or not at all** (`oct20/numbers/numbers_refresh.md:310`).

**How to use it.** Do each worked example yourself, by hand or in a spreadsheet, *before* you read the answer. Then do the three self-test questions without looking; answers are at the end. If you can't explain a chapter out loud in two minutes, you don't own it yet. Allow about 6-8 hours for the whole guide; Chapters 1, 4, 5, 8 and 12 matter most for the semifinal questions.

**Paths.** `oct19/` and `oct20/` mean `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`. `case:n` is line n of `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`. The checks for this guide are in `oct20/learn/scripts/` and their printed output in `oct20/learn/data/`.

---

## Our plan on one page (so the chapters have something to hang on)

Source: `/home/user/snap/main/COMPETITION.md:147-168` and the case.

- **The client's money (CASE).** Laura puts in $300,000 at the start of 2027 and $150,000 at the start of 2028 (case:43-45). Nothing else goes in or out before 2033 (case:63-65). From 2033 to 2042 she must pay **ten fixed $50,000 payments**, one each January, "funded by the investment portfolio with a high degree of certainty", with no outside money (case:88-92). In 2031 she tells co-sponsors a **dollar range** for her 2033 facility gift, with a stated confidence (case:117-120).
- **Jan 2027 ($300k): the ladder.** Buy ten Treasury holdings, one maturing just before each payment: the iBond ETFs IBTM, IBTO, IBTP, IBTQ, IBTR for 2033-2037 and five Treasury bonds (4.750% Feb-2037, 4.500% May-2038, 4.375% Nov-2039, 4.250% Nov-2040, 3.125% Nov-2041) for 2038-2042. In 2033 this ladder *is* the operating reserve.
- **Jan 2028 ($150k): top-up, floor, then growth.** First fill any gap in the ladder. Then buy a **floor** in IBTM that repays what is left by Dec 2032 (about $150k). Put the rest (about $33.5k) in **VT**, a world stock fund, untouched until 2033.
- **2031: trade nothing.** Quote a range from the floor (rounded down) to the floor plus half of VT.
- **2033:** the ladder pays the ten payments. The gift = floor + half of VT, capped at the announced top. The rest stays with Laura.
- **WInS** (the competition simulator) holds the same plan scaled down to $300k: 11 filled trades on 7-8 Oct, cash $3,514 (COMPETITION.md:170-188). WInS gains never go into Laura's projections (case:129-133).

---

## Chapter 1. Present value: why $500,000 of payments costs about $297,000

### The idea in 3 sentences
A dollar you receive later is worth less than a dollar today, because today's dollar can earn interest until then. The **present value (PV)** of a future payment is the amount you would have to invest today, at today's interest rates, to have exactly that payment on the day. Laura's ten payments add up to $500,000, but they are spread from 2033 to 2042, so at roughly 5% a year their value on 1 Jan 2027 is only about $293,000-$298,000, depending on exactly how you count.

### Worked example (do it yourself first)
1. **One payment, flat rate.** At 5% a year, what is the 1 Jan 2042 payment worth on 1 Jan 2027 (15 years earlier)? PV = 50,000 / 1.05^15.
2. **All ten, flat rate.** Add 50,000 / 1.05^k for k = 6, 7, ..., 15 (2033 is 6 years after 2027).
3. **The break-even rate.** Find the rate r at which the sum in step 2 equals exactly $300,000. That is the return Laura's first deposit *must* earn to fund the payments on its own.
4. **The real thing.** Caplet does not get one flat rate; each holding ends on its own date at its own yield. Use the table below (19 Oct curve). For each row, PV = 50,000 / (1 + y/200)^(2t), where y is the par yield in percent and t is years from 1 Jan 2027 to the holding's end date. Add the ten rows.

| Payment | Holding | Ends | t (years) | Par yield at t (%) |
|---|---|---|---|---|
| 2033 | IBTM | 15 Dec 2032 | 5.955 | 4.988 |
| 2034 | IBTO | 15 Dec 2033 | 6.954 | 5.038 |
| 2035 | IBTP | 15 Dec 2034 | 7.953 | 5.075 |
| 2036 | IBTQ | 15 Dec 2035 | 8.953 | 5.112 |
| 2037 | IBTR | 15 Dec 2036 | 9.955 | 5.148 |
| 2038 | T 4.750% Feb-2037 | 15 Feb 2037 | 10.125 | 5.155 |
| 2039 | T 4.500% May-2038 | 15 May 2038 | 11.368 | 5.202 |
| 2040 | T 4.375% Nov-2039 | 15 Nov 2039 | 12.871 | 5.259 |
| 2041 | T 4.250% Nov-2040 | 15 Nov 2040 | 13.873 | 5.297 |
| 2042 | T 3.125% Nov-2041 | 15 Nov 2041 | 14.872 | 5.335 |

(The yield column is a straight-line interpolation between the two treasury.gov tenors either side, e.g. 5y and 7y for IBTM. Build it yourself in the Spreadsheet Lab.)

### Answers
1. 50,000 / 1.05^15 = **$24,051**. (For 2033: 50,000 / 1.05^6 = $37,311.)
2. **$302,509** at a flat 5%.
3. **r = 5.087% a year** (5.024% on the semiannual convention Treasuries are quoted in). This is case-derived and does not change with markets (`oct20/numbers/numbers_refresh.md:154`).
4. Simple par method: **$298,641**. The more exact method in Chapter 2 (discounting with zero yields, "basis D") gives **$297,162**: $2,838 under $300,000 (MODEL, 19 Oct close; `numbers_refresh.md:64`). **[checked: what basis D is]** Basis D prices ten zero-coupon $50,000 amounts at the holdings' end dates. The real holdings (coupon bonds, and iBond funds whose bonds mature during the year) cost a little more when each is sized to deliver its $50,000 by its own maturity: about $298.5-299.9k on 19 Oct (coupon study $298,446; `oct20/reconcile3r/reconcile_3r.md` section 3). So $2,838 is the most generous room among the maturity-sized estimates, not a safe margin. The same payments valued on their 1 January payment dates instead of the holdings' end dates cost $293,767 (basis B). The holdings' figure is higher because each holding ends 17 days to 10.5 months *before* its payment, and the cautious basis assumes that waiting cash earns nothing, so you have to buy the money earlier.

### Python check I ran
`oct20/learn/scripts/verify_guide.py` (pure Python, no earlier model code), output in `oct20/learn/data/verify_out.txt`:
```
required annual return ... 5.087%   semiannual 5.024%
flat 5.000% annual: PV of ten payments = $302,509
one payment: 2033 $50k at flat 5% = $37,311; 2042 = $24,051
19 Oct, holdings' end dates: simple par method $298,641; bootstrap zero (basis D) $297,162
19 Oct, payment dates (basis B, yields unchanged): $293,767
10/06/2026: basis D $293,453     10/16/2026: basis D $298,940
```
All five match the numbers desk and the chart pack exactly (`numbers_refresh.md:56-64`; `oct20/charts/charts_data_pack.md:68`).

> **Common misconception: "the ladder costs $297,162, so Laura has $2,838 spare."**
> That figure is true only on one date (19 Oct) and one basis (D). It was $293,453 on 6 Oct and $298,940 on 16 Oct, and it moved $1,778 in one trading day (16 to 19 Oct). Laura buys on 1 Jan 2027, not today. That is why the team rule is to quote no dollar level in the TNA or IPS and to state the *rule* instead: if the ladder costs more than $300k, the 2028 deposit tops it up (`numbers_refresh.md:15`). Also, $450k in and $500k out is not a loss: interest does the extra $50k of work.

### Self-test
- **Q1.1** At a flat 6% a year, what is the 2033 payment worth on 1 Jan 2027?
- **Q1.2** If all yields rose by half a point before January, would the ladder cost more or less than $297,162? Why?
- **Q1.3** Explain in one sentence why the payment-date figure ($293,767) is lower than the holdings figure ($297,162).

---

## Chapter 2. The yield curve, and par yields versus zero yields

### The idea in 3 sentences
The **yield curve** shows the interest rate the US government pays for each length of borrowing; on 19 Oct it slopes upward (1-year 4.50%, 10-year 5.15%, 20-year 5.53%) and dips slightly at 30 years (5.48%). Treasury.gov publishes **par yields**: the coupon at which a new bond of that length would sell for exactly $100, a blend of many payment dates (every coupon plus the final $100). A **zero (spot) yield** is the rate for one single payment on one date, which is the right rate for discounting one $50,000 payment; you get zero yields from par yields by **bootstrapping**.

### Worked example
Bootstrapping works one half-year at a time. Let d(t) be the price today of $1 paid at time t (a "discount factor"). Use par yields as decimals, c = par/100.
1. **0.5 years.** A 6-month par bond pays 100 + c/2 × 100 at 0.5 years and costs 100. So d(0.5) = 1 / (1 + c/2) with c = 0.0437. Compute d(0.5).
2. **1 year.** A 1-year par bond (c = 0.0450) pays c/2 at 0.5 years and 1 + c/2 at 1 year, and costs 1: c/2 × d(0.5) + (1 + c/2) × d(1) = 1. Solve for d(1).
3. **The pattern.** For every later half-year n: d(n) = (1 − c/2 × [sum of all earlier d's]) / (1 + c/2). The Spreadsheet Lab does all 60 rows.
4. **Compare at the 2042 rung (t = 14.872).** The par yield there is 5.335%. Is the zero yield higher or lower? Why?

### Answers
1. d(0.5) = 1 / 1.02185 = **0.978617**.
2. d(1) = (1 − 0.0225 × 0.978617) / 1.0225 = **0.956461**. The 1-year zero yield is 4.501%, almost the same as the 4.50% par yield (short bonds have few coupons, so par ≈ zero).
3. —
4. Higher: the zero yield at 14.872 years is **5.431%** against par 5.335%. When the curve slopes up, a 15-year par bond's coupons are paid at earlier dates whose rates are *lower*; for the whole bond to still yield 5.335%, the rate on the last date must be *higher*. Discounting at the higher zero yields makes long payments cheaper. That is why the zero method total ($297,162) is **$1,479 below** the simple par method ($298,641).

| t (years) | 1 | 2 | 5 | 10 | 14.872 | 20 | 30 |
|---|---|---|---|---|---|---|---|
| Par yield, 19 Oct (%) | 4.500 | 4.770 | 4.940 | 5.150 | 5.335 | 5.530 | 5.480 |
| Zero yield, MODEL (%) | 4.501 | 4.778 | 4.954 | 5.191 | 5.431 | 5.726 | 5.558 |

### Python check I ran
```
d(0.5) = 0.978617  [1/(1+0.0437/2) = 0.978617]
d(1.0) = 0.956461  [(1 - 0.045/2*d0.5)/(1+0.045/2) = 0.956461]
t=14.872: par 5.335%  zero(semi) 5.431%
simple minus zero total: $1,479
```
The 14.872-year zero (5.431%) matches the chart pack's MODEL column (`oct20/charts/c1_payment_map.csv`, row 10).

> **Common misconception: "Treasuries yield 5.15%, so that's our ladder's yield."**
> 5.15% was the 19 Oct **10-year par yield**. The ladder's own yield (its internal rate of return: the one rate that makes ten $50,000 payments on their 1 January dates worth exactly $297,162) is **5.185%** on basis D, against the 5.087% Laura needs: a margin of only about 0.10 points (`numbers_refresh.md:155-160`; my check: `oct20/learn/data/irr_out.txt`). An earlier IPS draft's "about 5.15%" matched the 10-year on 19 Oct by coincidence and was undated (`numbers_refresh.md:161`). Comparing the ladder yield with 5.087% is the same test as comparing its cost with $300,000.

### Self-test
- **Q2.1** Interpolate the 8-year par yield from the 7-year (5.04) and 10-year (5.15) points.
- **Q2.2** If the curve were completely flat at 5%, would par and zero yields differ?
- **Q2.3** On a downward-sloping curve, would long zero yields sit above or below par yields?

---

## Chapter 3. Coupon bonds, iBond ETFs and STRIPS (and why STRIPS were out for us)

### The idea in 3 sentences
There are three ways to have Treasury money arrive near a date: a **coupon bond** pays interest every six months plus $100 at the end, so you must reinvest the coupons along the way; a **STRIPS** (a zero-coupon Treasury) pays one sum on one date, with nothing to reinvest; an **iBond ETF** is a fund that holds many Treasuries maturing in one year, pays out monthly, and winds up on or about 15 December of its year. STRIPS would be the neatest match, but the rules exclude them: Wharton's 6 Oct email limits "both contributions" to "eligible stocks, ETFs and Treasury bonds available on WInS" (COMPETITION.md:87-90), and the live FAQ, re-read on 19 Oct, lists "STRIPS (Separate Trading of Registered Interest and Principal of Securities)" under "The following are NOT permitted" for "BOTH contributions, the IPS and Final Report" (`oct19/askwharton/web/faqs.txt:44-55`). WInS lists no Treasury bonds maturing between Feb 2031 and Feb 2036, so the iBond ETFs fill the 2033-2037 payments (COMPETITION.md:93-94).

### Worked example: three ways to fund the 2042 payment
1. **STRIPS (not allowed, but the benchmark).** One $50,000 on 15 Nov 2041, discounted at the 14.872-year zero yield of 5.431%: 50,000 / (1.027155)^(2 × 14.872). Compute it.
2. **The coupon bond we hold (3.125% Nov-2041).** It pays $1.5625 per $100 face every 15 May and 15 Nov: 30 coupons from May 2027 to Nov 2041, plus $100 at the end. If every coupon is reinvested at the bond's own yield (5.365%, MODEL), $100 of face grows to 1.5625 × ((1 + y/2)^30 − 1)/(y/2) + 100 by maturity. Compute that, then the face needed for $50,000, then the cost (face × 77.644/100, the MODEL dirty price).
3. **WInS.** WInS holds 20 units ($20,000 face) of this bond. How much is each coupon? And: WInS holds 1,142 IBTM shares for the 2033 payment; at the 19 Oct close of $21.865, what are they worth?

### Answers
1. **$22,536** (the chart pack's basis D cost for this rung).
2. 170.63 per $100 face, so face = 50,000 / 1.7063 = **$29,303**, costing **$22,751** (`oct20/charts/charts_data_pack.md:199-201`). The coupon bond costs $215 more than the zero here, but price is not the real difference: the bond delivers $50,000 **only if** its coupons earn 5.365% for 15 years (Chapter 5).
3. 20,000 × 3.125% / 2 = **$312.50** each 15 May and 15 Nov (the chart pack lists $312.50 for the 16 Nov coupon, `charts_data_pack.md:273-274`). 1,142 × 21.865 = **$24,970**. That is about 0.67 of the plan's $37,287 for this rung: each WInS payment holding covers about two-thirds of a $50,000 rung (`charts_data_pack.md:103-106`). **[checked: scale]** The whole-book scale is a different number, about 0.64 ($300k ÷ Laura's plan value on 2 Jan 2028), and it is never 300/450 (`oct20/numreg/numbers_register.md` row H5).

### Python check I ran
```
T 3.125 Nov-41  cpn 3.125% own ytm 5.365% face $29,302 cost $22,752 (zero-coupon equivalent $22,536)
annuity formula: 1.5625*((1+y/2)^30-1)/(y/2)+100 = 170.63 per 100 (y = 5.365%)  face 29,303
Nov-41: coupons 30 ... WInS 20 units -> $312.50 each half-year
IBTM 1,142 x 21.865 = $24,970
```
My independent rebuild of the coupon study's ten-rung sizing gives $298,453 against the study's $298,446 (`numbers_refresh.md:191`): a $7 difference from rounding.

> **Common misconception: "STRIPS were banned because they are risky," or "iBond ETFs are stocks."**
> STRIPS carry the same US-government credit as any Treasury (their prices swing more than coupon bonds', but held to maturity they are the cleanest match) **[checked: wording]**; they are out simply because the rules allow only WInS-listed stocks, ETFs and Treasury bonds, and the FAQ now names them. The iBond ETFs hold Treasuries; WInS's pie chart labels them "Long Equities", but the real mix of the book is about 90% Treasuries (COMPETITION.md:98; `numbers_refresh.md:301-302`). And an iBond ETF is not a promise of a dollar amount: iShares says the funds "do not seek to return any predetermined amount" (`charts_data_pack.md:98-99`).

### Self-test
- **Q3.1** How much does each coupon on our 18 units of the 4.375% Nov-2039 bond pay?
- **Q3.2** Why does a zero-coupon bond need no assumption about reinvestment?
- **Q3.3** Two of our bonds end long before their payment and need a short-term Treasury ETF to hold the cash. Which, and for how long?

---

## Chapter 4. Duration and DV01: the "$290 per 0.01 point"

### The idea in 3 sentences
**DV01** ("dollar value of one basis point") is how many dollars a price moves when yields move by 0.01 percentage point (1 basis point, "1bp"). **Duration** is the same idea in percent. **[checked: two kinds of duration]** **Macaulay duration** is the present-value-weighted average time until the money arrives, in years; **modified duration** = Macaulay ÷ (1 + y/2) is the percentage change in value for a 1-point change in yields. For one zero-coupon payment, Macaulay duration is just its maturity. The durations in this guide (9.71 years for the ladder cost, 9.90 years for the payments) are modified (effective) durations found by repricing; the payments' Macaulay duration on 19 Oct is about 10.0 years (CALC, `oct20/verify_learn/rerun/indep_out.txt`). For Laura, what matters is the *cost* of the ladder on 1 Jan 2027: it rises about **$290 for every 0.01-point fall** in yields, so falling yields make her January purchase dearer.

### Worked example
1. **One rung by hand.** A single payment's DV01 ≈ PV × t / (1 + y/2) × 0.0001. The 2042 rung: PV $22,851 (simple method), t = 14.872, y = 5.335%. The 2033 rung: PV $37,287, t = 5.955, y = 4.988%. Compute both.
2. **The room in basis points.** The room under $300k on 19 Oct was $2,838 (basis D). How big a fall in yields uses it up?
3. **Big moves.** Use the Spreadsheet Lab's shift cell to reprice the whole ladder at +0.5, −0.5, +1 and −1 points. Are the up and down moves the same size?

### Answers
1. 2042 rung: 22,851 × 14.872 / 1.02668 × 0.0001 = **$33.1** per bp. 2033 rung: **$21.7** per bp. Long payments move more, which is one reason the plan buys the 2042 rung first (`oct19/out/Caplet_Update_19Oct2026.md:284`). Adding all ten rungs this way gives $287.1.
2. 2,838 / 288.5 ≈ **9.8bp**, a 0.098-point fall (`numbers_refresh.md:12`).
3. Full repricing (basis D, 19 Oct):

| Parallel shift | +1.0 pt | +0.5 pt | 0 | −0.5 pt | −1.0 pt |
|---|---|---|---|---|---|
| Ladder cost | $269,825 | $283,122 | $297,162 | $311,991 | $327,657 |
| Change | −$27,338 | −$14,040 | — | +$14,829 | +$30,495 |

Falls hurt more than rises help. That curve in the price line is called **convexity**.

### Python check I ran
```
DV01 (bootstrap, +/-1bp par shift) = $288.5 per 0.01 pt; duration = 9.71 years
room / DV01 = 9.8 bp
by hand T 3.125 Nov-41: ... DV01 $33.1      by hand IBTM: ... DV01 $21.7
10/14/2026->10/15/2026: $+2,636     10/16/2026->10/19/2026: $-1,778
```
The numbers desk reports $288-291 (`numbers_refresh.md:69`); the inflation study's rougher method gives $289 and ±50bp ≈ −$14.1k / +$14.9k (`oct20/inflation/inflation.md:208`).

> **Common misconception: "$290 per point," and "our WInS bonds went up, good news."**
> It is $290 per **0.01** point, about $27,000-$30,000 per full point. And a bond *gain* in WInS happens when yields fall, which is exactly when Laura's real January purchase gets more expensive. Never present a WInS bond gain as good news for her (`numbers_refresh.md:304`).

### Self-test
- **Q4.1** Yields fall 0.25 points before 1 Jan. Estimate the new ladder cost with DV01, and the top-up needed from the 2028 deposit.
- **Q4.2** Which single rung is most rate-sensitive, and why?
- **Q4.3** From 6 Oct to 19 Oct the basis-D cost rose $3,710. Roughly how far did yields fall on average? Does that fit the 10-year moving from 5.27% to 5.15%?

---

## Chapter 5. Reinvestment risk and the coupon gap

### The idea in 3 sentences
A coupon bond only reaches its promised end value if **every coupon is reinvested at the bond's own yield** until maturity. If yields fall and stay down, the coupons earn less, and the rung arrives short of $50,000; this is **reinvestment risk**, and across Caplet's ten rungs it is called the **coupon gap**. Holding to maturity removes the risk of a *price* fall, not this one.

### Worked example: the 2042 rung (3.125% Nov-2041, face $29,303)
1. Value at maturity per $100 face if coupons earn r: FV = 1.5625 × ((1 + r/2)^30 − 1)/(r/2) + 100. Do it for r = 5.365% (own yield), 4.365%, 3.365% and 2.365%, and for 0% (coupons just pile up: 1.5625 × 30 + 100).
2. Multiply each by 293.03 (= 29,303/100) to get dollars on 15 Nov 2041. How short of $50,000 is each?
3. **Waiting cash.** Each holding ends before its payment (17, 17, 17, 17, 17, 320, 231, 47, 47 and 47 days). Simple interest on $50,000 at the 19 Oct 3-month bill rate of 4.27%: 50,000 × 0.0427 × days / 365. Add the ten. The cautious models assume this interest is zero.

### Answers
1-2.

| Coupons reinvested at | Own yield 5.365% | −1 pt | −2 pts | −3 pts | 0% |
|---|---|---|---|---|---|
| Per $100 face | 170.63 | 165.23 | 160.33 | 155.88 | 146.875 |
| Delivered | $50,000 | $48,418 | $46,982 | $45,677 | $43,039 |
| Short | $0 | $1,582 | $3,018 | $4,323 | $6,961 |

Source: `oct20/charts/c3_one_rung_rebuild_Nov2041.csv`. This one rung is about $3.0k of the whole ladder's gap at −2.

**Whole ladder, yields fall on 2 Jan 2027 and never recover (MODEL, 19 Oct):** about **$10.1k / $19.5k / $28.2k** short at −1 / −2 / −3 points on the coupon study's holdings basis (after the iBond-coupon fix, VIN E1; about $19.5-21.3k at −2 depending on method) [consistency fix 20 Oct, row 10], or **$21,287** at −2 on the number sheet's basis E, which also loses the interest on waiting cash (`numbers_refresh.md:167-172`). Always name the basis.

3. **$4,545** (simple interest). The coupon study's figure is $4,492 (`numbers_refresh.md:179`). This is a cushion the cautious basis does not count. It shrinks when rates fall.

**A second way to see the gap.** The holdings' market value moves about **$230 per bp**, while the payments' value moves about **$291 per bp** (19 Oct; 16 Oct: $232 vs $293, the same as the red team's figures, `oct20/redteam3r/redteam_3r.md:110`). Coupons return money early, so the holdings are "shorter" than the payments. A gap of about $61 per bp is the coupon problem in one number.

**What the team is deciding on Tue 27 Oct** (facts only; the team decides): **[checked: agreed numbers]** option 1 states the risk only (on the reconciled, agreed basis a payment is short in about 14% of model paths, typically by about $1.6k, worst about $10k; only if Laura's half is free after 2033; about 1.6%, worst about $7k, if it stays on call; D10 [consistency fix 20 Oct, row 11]); option 3r sets aside $10k of the 2028 deposit in the Nov-2041 bond (about 0.6% of paths short, worst about $3.3k, on the plan as written with realistic holdings; about 0.01% in the study's own engine; 2-6% if two plan rules on sizing and the 2033 reserve are not written down); option 4 rebuilds the ladder so later coupons pay earlier payments (the −2 gap falls to $5,596) (`oct20/reconcile3r/reconcile_3r.md` sections 0, 5 and 7; `numbers_refresh.md:210-223`; `oct19/coupon/coupon_risk_options.md:106-144`). The older 15.6% and 0.02% each rest on unstated model rules: do not quote them (reconcile_3r.md section 7). The red team's verdict on 3r is MODIFY, and its reasons are in Chapter 8.

### Python check I ran
```
Nov-41 rung delivers $50,000 / $48,418 / $46,981 / $45,675 at own yield +0/-1/-2/-3   (annuity formula: $46,982 at -2)
at 0% reinvestment: 146.875 -> $43,039
simple interest on waiting $50k at 4.27% bill: $4,545
holdings DV01 $230/bp vs payments (payment dates) DV01 $291/bp; gap $61
whole ladder shortfall at -2 (independent rebuild): $19,487
```
**One difference I found.** My independent rebuild of the whole ladder gives $10,095 / $19,487 / $28,233, about $560 more than the study. The study sizes each iBond fund with one coupon but pays it out at its slightly higher yield, so each iBond rung delivers about $112-119 too much with no rate change (the red team flagged this, `redteam_3r.md:81-85`). Switching that on in my code reproduces the study to the dollar ($9,537 / $18,951 / $27,717; `oct20/learn/data/quirk_out.txt`). So the study's coupon-gap figures are slightly optimistic, by about $0.5k.

> **Common misconception: "We hold to maturity, so interest rates can't hurt the payments."**
> Holding to maturity protects the $100 at the end, not the coupons. A second one: "the 3r reserve works because its price rises when yields fall." The red team found most of 3r's protection comes from the reserve money *itself* being locked at about 5.3% until 2041; the price gain is the smaller part (`redteam_3r.md:92-105`). **[checked: caveat]** "Locked" is too strong: the reconciliation found the red team measured this with a formula that lets the bond's own coupons earn the purchase yield for ever. The Nov-2041 bond's coupons face reinvestment risk too (less than cash does), so the locked-yield share is somewhat overstated (`oct20/reconcile3r/reconcile_3r.md` section 6, item 2).

### Self-test
- **Q5.1** WInS holds 20 units ($20,000 face) of the Nov-2041 bond. Using the per-$100 values above, how much does that position deliver at the own yield and at −2 points?
- **Q5.2** Why is the coupon gap bigger for the long rungs than for the 2033 rung?
- **Q5.3** If yields *rise* after January 2027 and stay up, what happens to the coupon gap?

---

## Chapter 6. Cash-flow matching versus duration matching (LDI)

### The idea in 3 sentences
**Liability-driven investing (LDI)** means building the assets around the payments you owe, as pension funds do. **Cash-flow matching** (also called dedication) buys assets whose cash arrives when each payment is due, so nothing has to be sold; **duration matching** (immunisation) buys assets whose duration equals the payments' duration, so small parallel moves in yields cancel out, but it must be rebalanced and can fail when the curve twists. Caplet's ladder is cash-flow matching for each rung's principal; the coupons are the part that is not matched (Chapter 5), and the team's own wording rule is "the ladder is cash-flow matching (not immunisation)" (COMPETITION.md:168).

### Worked example
1. **A duration match with two funds.** Before the 6 Oct email limited Laura's plan to WInS-listed securities, the AI insight_v1 research looked at matching with IEF (duration 6.86 years) and TLT (14.88 years) (fund data of 24 Sep, `/home/user/snap/main/CLAUDE.md:163`). The payments' duration on payment dates is 9.90 years (19 Oct, my check; the same 9.90 as on the 25 Sep curve). Find the IEF weight w with w × 6.86 + (1 − w) × 14.88 = 9.90.
2. **Test it (toy).** Replace the two funds with two zero-coupon bonds of 7 and 15.5 years, weighted to match the payments' duration and value (a toy, not a real proposal). Reprice both sides after four yield changes: parallel −1, parallel +1, a steepener (short yields −1.5, long unchanged) and a flattener (short unchanged, long −1).
3. **Why a ladder instead?** List two things a duration-matched fund pair needs that a held-to-maturity ladder does not.

### Answers
1. w = (14.88 − 9.90) / (14.88 − 6.86) = **62.1% IEF, 37.9% TLT** (CLAUDE.md:163 has 62.2/37.8 from rounder inputs).
2. Toy results (19 Oct curve, MODEL):

| Move | Payments' value | Matched pair | Mismatch |
|---|---|---|---|
| Parallel −1 pt | $324,539 | $325,191 | +$653 |
| Parallel +1 pt | $266,242 | $265,940 | −$302 |
| Steepener (short −1.5, long 0) | $321,834 | $319,987 | **−$1,846** |
| Flattener (short 0, long −1) | $305,444 | $307,159 | +$1,715 |

Parallel moves almost cancel. Twists do not. **[checked]** (The −1 and +1 rows are not mirror images partly because a small first-order mismatch remains: the weights use zero-yield durations while the shock moves par yields. The "steepener" and "flattener" are straight-line tilts from 6 months to 30 years.)

3. (a) Funds like IEF and TLT never mature, so every payment means selling at that day's price. (b) The payments' duration shrinks each year, so the weights must be rebalanced again and again. (c) It protects against small parallel moves only. A ladder's rungs simply mature.

**Where Caplet sits.** The principal is cash-flow matched. The coupons leave a duration gap of about $61 per bp (Chapter 5). The red team calculated that $10k of the Nov-2041 bond (option 3r) closes about 19% of that gap, and closing all of it would take about $54k (`redteam_3r.md:109-112`). Option 4 is the "full dedication" version of LDI: it cuts the −2-point gap from $19,488 (after the iBond-coupon fix, VIN E1) to $5,596 [consistency fix 20 Oct, row 10] but needs about 10 more WInS trades and conflicts with 3-4 filed notes (`oct19/coupon/coupon_risk_options.md:136-170`; `numbers_refresh.md:167-172`).

### Python check I ran
```
19 Oct payments (payment dates) duration 9.90y -> IEF 62.1% TLT 37.9% (24 Sep fund durations)
toy: zeros at 7.0y (mod dur 6.83) and 15.5y (15.09); weights 62.8/37.2
parallel -1 ... mismatch $+653 | parallel +1 ... $-302 | steepener ... $-1,846 | flattener ... $+1,715
```
Whether IEF and TLT are listed on WInS was never confirmed (UNVERIFIED); this chapter uses them only to teach the idea.

> **Common misconception: "Same duration means same risk," or "our ladder is immunised."**
> Matching duration matches only the first-order response to a *parallel* move. Twists, the passage of time and the need to sell all break it. Say "cash-flow matched ladder", not "immunised".

### Self-test
- **Q6.1** Redo Q1 of the example for a target duration of 10.16 years.
- **Q6.2** Why must a duration-matched portfolio be rebalanced even if yields never move?
- **Q6.3** Which part of Caplet's plan is cash-flow matched, and which part is not?

---

## Chapter 7. The equity risk premium, VT and why "about 7%"

### The idea in 3 sentences
Stocks are expected to earn more than safe bonds over long periods as a reward for their ups and downs; that extra is the **equity risk premium (ERP)**. Caplet's stock assumption is J.P. Morgan's 2026 Long-Term Capital Market Assumptions (data as of 30 Sep 2025): world stocks (AC World) **7.00% a year compound** with **16.78% volatility**; cash 3.10%; US intermediate Treasuries 4.00%; inflation 2.50% (`/home/user/snap/main/CLAUDE.md:148-150`). VT is one fund that owns thousands of companies covering most of the world's stock-market value **[checked: wording]**, with a 0.06% fee; in Laura's plan it is only about 7% of her money in Jan 2028 (66.5% payment Treasuries, 24.5% floor, 1.2% leftover, 7.0% VT; `numbers_refresh.md:322`).

### Worked example
1. **The premium.** Compute 7.00% minus JPM cash (3.10%), minus JPM intermediate Treasuries (4.00%), and minus the ladder's own 19 Oct yield (5.185%).
2. **Compound versus average.** "Compound" (geometric) 7% means the *median* path grows at 7% a year. The simple *average* of yearly returns is higher, roughly 7% + volatility²/2. Estimate it. Check the method on JPM's US large-cap figures: 6.70% compound, 16.47% volatility, stated arithmetic average 7.94%.
3. **VT in the plan.** About $33,515 goes into VT in Jan 2028 (MODEL, 19 Oct). Grow it at 7% for 3 years (to the Jan 2031 announcement) and 5 years (to the Jan 2033 gift). The top of the range is 150,000 + half of VT in 2031. What happens to the gift (150,000 + half of VT in 2033, capped at the top) if stocks fall 40% during 2032?
4. **A bad five years.** With 16.78% yearly volatility, a 1-in-20 bad five-year stretch averages about ln(1.0694) − 1.645 × 0.1678 / √5 a year in log terms. Convert it to a yearly return.

### Answers
1. **3.9** points over cash, **3.0** over intermediate Treasuries, but only about **1.8** points over the ladder's 5.185%. With Treasury yields near 5%, the safe choice pays almost what stocks are expected to pay, which is part of why the plan puts the payments in Treasuries. **[checked: mixed dates]** A judge may object that this mixes dates: JPM's 7% was set on Sep 2025 data, when its intermediate-Treasury figure was 4.00%, while 5.185% is an Oct 2026 yield; in building-block estimates, expected stock returns tend to rise when yields rise. So say "about 2 points, comparing a 2025 stock estimate with today's bond yield".
2. Rough rule: 7.00 + 16.78²/200 = 8.41%. The exact lognormal conversion gives **8.28%**. Checking the method on US large cap: 6.70% compound with 16.47% volatility gives **7.94%**, exactly JPM's figure.
3. 33,515 × 1.07³ = **$41,057** in 2031, so the top = 150,000 + 20,529 = **$170,529**. 33,515 × 1.07⁵ = **$47,007** in 2033, so the gift reaches the cap. With −40% in 2032: 150,000 + ½ × 33,515 × 1.07⁴ × 0.6 = **$163,179**, which is lower but still far above the bottom. That matches the numbers desk's "$170.5k → $163.2k" (`numbers_refresh.md:146-147`).
4. About **−5.5% a year** (and +21.0% a year for a 1-in-20 good five years). The sensitivity study uses exactly these (`oct20/sensitivity/sensitivities.md:72`). The range audit notes that the exact conversion of 16.78% to a log volatility is 0.154, not 0.1678 (`oct20/rangeaudit/range_audit.md:45`); with 0.154 the band is −4.5% to +19.8%. That is a small modelling choice, and a slightly cautious one.

### Python check I ran
```
US large cap 6.70% compound, 16.47% vol -> arithmetic 7.94% (JPM states 7.94%)
AC World 7.00% compound, 16.78% vol -> arithmetic 8.28%; log-vol 0.1541
ERP vs JPM cash 3.10: 3.90; vs JPM interm. Treasuries 4.00: 3.00; vs 19 Oct ladder IRR (D) 5.186: 1.81
top = 150,000 + half VT2031 = $170,529; gift with -40% in 2032 = $163,179
1-in-20 five-year average (sigma 0.1678): -5.5%/yr to 21.0%/yr
sim: 5-yr growth median 1.4016 (1.07^5=1.4026), mean 1.4884, p5 0.7939, share below 1 16.3%
```
The last line is a 200,000-path simulation: even at 7% a year, about 1 five-year path in 6 ends below where it started.

> **Common misconception: "7% means stocks will return 7% every year," or "VT is the risky heart of our plan."**
> 7% is one firm's long-run estimate (2026 edition), not a forecast for any year. JPM's 2027 edition is out, and its public page gives US large cap 7.5%, but its inflation figure is UNVERIFIED, so say "2026 edition" when you quote 7% (`oct20/inflation/inflation.md:48`). And VT is about 7% of Laura's money: the payments' principal never depends on it. **[checked: VT is also cover]** But Laura's half of VT is the second line of cover for coupon gaps, after the 2027 leftover (COMPETITION.md:161-162), so in bad reinvestment paths part of it does pay for payments. Mostly it sets the size of the gift above the floor.

### Self-test
- **Q7.1** If VT earned only 4% a year from 2028 to 2031, what would the top of the range be?
- **Q7.2** Why is the gift capped at the announced top instead of including all of half of VT?
- **Q7.3** Explain in one sentence why a 1.8-point premium over the ladder is a reason to keep stocks small *in this plan*.

---

## Chapter 8. Monte Carlo: paths, "41%" and why models disagree

### The idea in 3 sentences
A **Monte Carlo model** invents thousands of possible futures, called **paths**, by drawing random yield moves and stock returns that follow chosen rules (for example, yields wander about 1 point a year with no pull back to normal; stocks 7% compound with 16.78% volatility). It then counts how often something happens: "41%" means "in 41 of every 100 invented futures". The answer is only as good as the rules, and two careful models with different hidden rules can disagree by a factor of two or more.

### Worked example A: the 41% by hand
The question: what are the odds the ladder costs more than $300,000 on 1 Jan 2027 (MODEL, 19 Oct)?
1. The room is 9.8bp (Chapter 4).
2. Time from 19 Oct 2026 to 1 Jan 2027 = 74 days = 0.2026 years.
3. If yields move like a random walk with 1.0 point a year of volatility, the typical (one standard deviation) move by 1 January is 1.0 × √0.2026 points. Compute it in bp.
4. The chance of a fall bigger than 9.8bp is the normal-distribution probability below −9.8 / (your answer to step 3). In Google Sheets: `=NORM.S.DIST(-9.83/45.0, TRUE)`.
5. Repeat with the 2026 realised volatility of 0.71 points a year.

### Answers A
3. √0.2026 = 0.450, so **45.0bp**.
4. z = −9.83 / 45.0 = −0.218, giving **41.4%** (`numbers_refresh.md:96`).
5. 32.0bp, giving **37.9%**.

What "41%" means: in 41 of 100 model futures, Laura's January purchase needs a **top-up from the 2028 deposit**, the rule already written into the IBTR note (`oct19/out/Caplet_Update_19Oct2026.md:285`). It is *not* a 41% chance of missing a payment. **[checked: basis]** 41% is on basis D (register row C3). Priced with the real holdings sized to their own maturities, the reconciliation puts the January top-up at about a coin flip (50%) on the same day (`oct20/reconcile3r/reconcile_3r.md` sections 3 and 5). The 1-in-20 top-up is about $20-22k (`oct20/rangeaudit/range_audit.md:74`; `oct20/sensitivity/sensitivities.md:13`).

### Worked example B: why models said 16%, 32% and, once reconciled, about 14% **[checked: rewritten]**
All the models asked: "under option 1 (state the coupon risk, no reserve), how often is some payment short?"
- The coupon study said **16.4%** (16 Oct curve) / **15.6%** (19 Oct) (`oct19/coupon/coupon_risk_options.md:38`; `numbers_refresh.md:212`).
- The independent range audit said **32.3%** (19 Oct) (`oct20/rangeaudit/range_audit.md:86, 133`).
- A reconciliation ran both engines on identical random paths, switched one assumption at a time, then fixed one agreed basis (the plan's rules read literally, realistic pricing of the real holdings). On that basis option 1 is **about 14.4%** (14.5% on a second random seed), typical gap about $1.6k, worst about $10k (only if Laura's half is free after 2033; about 1.6%, worst about $7k, if it stays on call; D10) [consistency fix 20 Oct, row 11] (`oct20/reconcile3r/reconcile_3r.md` sections 1 and 5). Neither 16% nor 32% is "the" answer.

Where the study-to-audit gap of about 16.5 points comes from (option 1, 19 Oct; reconcile_3r.md section 4b):
1. **The unused 2027 leftover: +7.9 points.** The study's code keeps it in cash until 2042, a hidden extra reserve, although the study's own description says nothing is committed after 2033. The audit gives it back to Laura.
2. **How the iBond funds are modelled: +5.8 points.** The study treats each fund as one bond ending 15 Dec. The audit uses the funds' real holdings, which mature during the year and then sit in T-bills until 15 Dec.
3. **Waiting cash: net +3.1 points.** Counting T-bill interest in the rung sizing (+5.4) and in the projections (+12.3), while the cash really earns it (−14.4).
4. **Smaller items:** measuring the 2033 need in today's value (+1.0), counting "any one payment short" instead of the ten-payment total (−1.9), engine details.

For option 3r the leftover rule is worth **0.00**. Its 0.02% → 6.1% gap comes mainly from measuring the 2033 need in today's value instead of dollars (+2.0), sizing the rungs counting T-bill interest (+1.1) and the iBond model (+2.7) (reconcile_3r.md section 4a). The range audit's own explanation blamed the leftover for 3r; the reconciliation found that attribution wrong (section 6, item 9).

Three lessons: each figure rests on rules nobody wrote down; when many rules differ at once, the order in which you switch them changes how big each one looks, so "which single rule explains it" often has no answer; and, in the audit's words, "a probability is only as good as its smallest hidden rule" (`range_audit.md:202`).

Two more things to check whenever someone quotes a model:
- **How big, not just how often.** Under option 1, the typical gap when a payment is short is about $1.1k in the coupon study (`oct20/sensitivity/sensitivities.md:52`; JSON `unc_med_if_miss` 1,138) and about $1.6k on the agreed basis, worst about $10k (`reconcile_3r.md` section 5) **[checked]**. A 14% chance of a $1,600 gap is a different problem from a 14% chance of a $50,000 gap.
- **How many really independent tries.** "0 of 690 history windows" sounds strong, but the 690 sixteen-year windows overlap heavily: 882 months of data hold only 4 non-overlapping 16-year windows (`oct20/redteam3r/redteam_3r.md:73`). With real curve shapes, 2 of the 690 windows were short by about $177 under 3r (`redteam_3r.md:74-77`). **[checked]** On the agreed basis, 7 of 688 overlapping windows (additive replay, all starting Aug 1984-May 1985) were short under 3r, worst about $1.0k; 0 of 688 with the proportional replay (`reconcile_3r.md` section 5).

### Python check I ran
```
time to 1 Jan 2027 = 0.2026 y; room = 9.83 bp
sigma 0.71: sd of shift 32.0 bp; P(fall > room) = 37.9%
sigma 1.0: sd of shift 45.0 bp; P(fall > room) = 41.4%
full-repricing break-even shift -9.78 bp -> P (sigma 1.0) = 41.4%
simulated 100,000 paths (linear DV01): 41.41% ; sampling s.e. 0.16 pts
s.e. of 0.02% with 100k paths: 0.0045 pts (= 20 paths)
history windows: 882 months / 192-month windows -> 4 non-overlapping; overlapping starts 690
```
I also read the 16.4%, 15.6% and 32.3% straight from the models' saved results (`oct19/coupon/data/coupon_options_results.json`: p_miss 0.16447; `oct20/numbers/data/coupon19/coupon_options_results.json`: 0.15578; `oct20/rangeaudit/data/results.json`: 0.32269 and 3r 0.06162).

> **Common misconception: "41% is the chance Laura misses a payment," or "100,000 paths makes it accurate."**
> 41% is the chance of a top-up. And 100,000 paths makes the answer *precise* (±0.16 points of sampling noise), not *accurate*: if the rules are wrong, a million paths give the wrong answer very precisely.

### Self-test
- **Q8.1** Redo Example A with 1.2 points a year of volatility.
- **Q8.2** On 6 Oct the room was about 20-23bp. With the same 45bp standard deviation, roughly what would the odds have been for a 20bp room?
- **Q8.3** **[checked: replaced]** Name the largest single piece of the 16% → 32% gap for option 1. Does the same rule matter for option 3r?

---

## Chapter 9. Inflation and the real value of fixed payments

### The idea in 3 sentences
Inflation means prices rise, so a fixed $50,000 buys less each year; the **real value** of a future amount = nominal amount / (1 + inflation)^years. The case fixes the payments at $50,000 "not adjusted for inflation" (case:90), and the ladder is also in fixed dollars, so **inflation cannot make a payment short**; it only changes what the payments buy. The Treasury inflation-protected kind (TIPS) is not permitted anyway (`oct19/askwharton/web/faqs.txt:54`), and it would mismatch fixed-dollar payments even if it were.

### Worked example (base date 1 Jan 2027; US inflation 2.5% = JPM 2026)
1. Real value of the 2033 payment (6 years) and the 2042 payment (15 years).
2. Real value of all ten payments together. Repeat at 2.0% and 3.5%.
3. What share of the 2033 payment's buying power does the 2042 payment have?
4. **The floor.** The floor is bought in Jan 2028 and pays out in Dec 2032. How much real value does it lose at 2.5% over 5 years? Over 6 years (from Jan 2027)?
5. **Real yield.** The ladder yields 5.185% (Chapter 2) and the market's 10-year breakeven inflation was 2.35% on 19 Oct. Real yield ≈ (1.05185 / 1.0235) − 1.

### Answers
1. **$43,115** and **$34,523**.
2. **$386,777** at 2.5%; $406,790 at 2.0%; $350,118 at 3.5% (`oct20/inflation/inflation.md:118-131`).
3. 1.025^−9 = **80.1%**.
4. **11.6%** over 5 years, **13.8%** over 6. An IPS draft said "about 12% by 2033": right only if measured from the Jan 2028 purchase, so always name the start date (`inflation.md:193`).
5. About **2.77%** real, close to the 7-10-year TIPS yields of 2.67-2.80% on 19 Oct (`inflation.md:210`).

**Taiwan is a different inflation.** The residency spends in Taiwan. Taiwan CPI was +2.73% year on year in Sep 2026, but construction costs (DGBAS index) were **+7.29%** year on year, and 2.5-3.6% a year over long windows (`inflation.md:23-25`). Between a 2031 quote and the 2033 gift, normal building-cost drift takes about 4.8% (at 2.5% a year) to 6.8% (at 3.6%) off what a fixed US$ amount builds.

### Python check I ran
```
2.0%: total $406,790 ... 2.5%: total $386,777; 2033 $43,115; 2042 $34,523; 2042/2033 80.1% ... 3.5%: total $350,118
floor real loss 5y at 2.5%: 11.6%; 6y: 13.8%
real ladder yield: (1.05186/1.0235)-1 = 2.77%
building drift 2031->2033 (2 yrs): 2.5% 4.8%, 3.6% 6.8%, 7.3% 13.1%
```

> **Common misconception: "Inflation could stop Laura paying," or "the stock half protects her against inflation."**
> The payments are fixed dollars and so is the ladder, so inflation decides what the money buys, not whether it arrives. As for stocks: in the highest-inflation fifth of 5-year windows since 1950, US stocks' median real return was only about 0.7% a year, and 47% of those windows lost real value (`inflation.md:28`). Stocks protect against inflation over decades, not over five years.

### Self-test
- **Q9.1** What is the 2038 payment worth in Jan-2027 dollars at 2.5%?
- **Q9.2** Give one reason, apart from the rules, why TIPS would be a poor match for Laura's payments.
- **Q9.3** A $168,000 top is quoted in Jan 2031. If Taiwan building costs rise 3.6% a year to Jan 2033, how much building (in US$) does it lose?

---

## Chapter 10. Currency risk: NT$ and US$

### The idea in 3 sentences
Laura's portfolio is in US dollars, but the residency will pay builders and staff in New Taiwan dollars (NT$), so the exchange rate decides how much building each US dollar buys. On 19 Oct the rate was **NT$32.445 per US$** (central bank closing rate); if the NT$ strengthens, each US$ buys fewer NT$, which is *bad* for money spent in Taiwan. Locking the rate with a currency forward would be a derivative, which the rules ban, so the plan can only state the risk and say who carries it (`inflation.md:199`). **[checked]** (Holding NT$ assets, such as a Taiwan stock fund if WInS lists one, UNVERIFIED, would add stock risk, so it is not a clean hedge.)

### Worked example
1. Convert $145,000 and $50,000 to NT$ at 32.445.
2. Over 2-year windows since 2000, the NT$ per US$ rate changed by −10.4% at the 5th percentile and +11.5% at the 95th, with a worst of −15.0% and a best of +16.7% (`inflation.md:106`). What would $145,000 be in NT$ at each?
3. Combine currency *and* building costs: over 2-year windows since 2000, a fixed US$ amount's Taiwan building power changed by −22% (5th percentile), −5.2% (median) and +12.5% (95th) (`inflation.md:181`). Express $145,000 in "today's NT$ of building" for each.

### Answers
1. **NT$4.705m** and **NT$1,622,250**.
2. −10.4%: rate 29.07, **NT$4.22m**. +11.5%: rate 36.18, **NT$5.25m**. Worst −15.0%: **NT$4.00m**. Best +16.7%: **NT$5.49m**.
3. **NT$3.67m / NT$4.46m / NT$5.29m**, matching the inflation study (`inflation.md:184`). The two-year currency-plus-cost band is much wider than the uncertainty in the US$ floor itself.

A surprising fact (HIST): since 2000 Taiwan prices rose about 1.25% a year and US prices about 2.63%, which "should" have pushed the rate to about 21.5 NT$ per US$ (purchasing-power parity), but the actual rate was 31.85 in Sep 2026 (`inflation.md:20-21`). So don't assume the currency drifts in one direction.

### Python check I ran
```
$145k x 32.445 = NT$4.705m; $50k = NT$1,622,250
NT$/US$ -10.4% -> rate 29.07; $145k = NT$4.22m   ...   +11.5% -> rate 36.18; NT$5.25m
building power p5 -22.0% -> NT$3.67m ... median -5.2% -> NT$4.46m ... p95 +12.5% -> NT$5.29m
PPP from Jan 2000 (30.75) using 1.25% vs 2.63% for 26.67 yrs -> 21.43 (file: 21.48; actual 31.85)
```

> **Common misconception: "A stronger Taiwan dollar is good for Laura," or "we'll just hedge it."**
> A stronger NT$ means each US$ buys less in Taiwan. Hedging needs a derivative (not permitted). The case asks for a **dollar** range (case:117), so the range stays in US$, with any NT$ figure dated (the rate goes stale within weeks; `inflation.md:110`).

### Self-test
- **Q10.1** What is one $50,000 payment in NT$ if the rate is 29.20 (each US$ buys 10% fewer NT$, i.e. the NT$ is about 11% stronger) **[checked: wording]**?
- **Q10.2** If the range is quoted in US$, who carries the currency risk?
- **Q10.3** Why do the studies look at **2-year** currency windows in particular?

---

## Chapter 11. Risk capacity versus risk willingness (client analysis)

### The idea in 3 sentences
**Risk willingness** is how much risk a client *wants* to take; **risk capacity** is how much risk her goals and money can actually *absorb* without breaking a promise. Laura is willing: she "has been willing to take thoughtful risks throughout her entrepreneurial career" (case:69-70); but the payments have almost no capacity: they are fixed, must be funded by the portfolio alone "with a high degree of certainty", and may not lean on outside money (case:88-92). Good client analysis puts the risk where her willingness can be used *without* touching what she cannot afford to lose, which in Caplet's plan means risk only in the money above the payments.

### Worked example
1. **How much of the first deposit is spoken for?** Divide the 19 Oct ladder cost ($297,162) by $300,000. Compare the ladder's 5.185% yield with the required 5.087%.
2. **The "willingness only" test (CALC).** Suppose all $300,000 went into VT for 6 years instead (7% compound, 16.78% volatility, lognormal). Work out the median value in Jan 2033 (300,000 × 1.07⁶) and a 1-in-20 low (300,000 × e^(6 × ln 1.07 − 1.645 × 0.154 × √6)). Compare with what the ten payments are worth on 1 Jan 2033 at a flat 5% ($405,391).
3. **The second deposit.** The $150,000 comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" (case:44-45). The sensitivity study tested a missing or smaller deposit (MODEL, 19 Oct): $0 → some payment short in 55.3% of model paths; $75k → payments unchanged, but the median gift falls from $166.1k to $82.2k (`oct20/sensitivity/sensitivities.md:13-14, 68`). What does that tell you about where Laura's career risk enters the plan?

### Answers
1. **99.1%** of the first deposit, with only about a 0.10-point yield margin. Almost no room for risk in the payment money.
2. Median **$450,219**, 1-in-20 low **$242,012**. In this simple model there is about a **39%** chance of ending below the $405,391 the payments need. Willingness says yes; capacity says no.
3. The deposit is the hinge. The payments depend on it only for a top-up of the January ladder, while the gift depends on it almost entirely. Her career income is a kind of **human capital**, and a market slump could hit book and speaking income at the same time, so the portfolio should not add risk that moves with her career (a team client insight: `/home/user/snap/main/CLAUDE.md:133-134`; how closely her income tracks markets is an interpretation, UNVERIFIED). The plan answers this by funding the payments from the first deposit (the second only tops up the ladder if needed), and putting risk only in VT (about 7% of her money).

### Python check I ran
```
share of $300k spoken for by ladder (D): 99.1%
all $300k in VT for 6 yrs (median): $450,219        (1-in-20 low): $242,012
need in 2033 at flat 5% $405,391; P(all-VT 2033 value below it) = 39.1%
```
(The CALC test uses 0.154 as the log volatility, the exact conversion of 16.78%. It is an illustration, not a strategy the team considered in this form.)

> **Common misconception: "She's an entrepreneur, so she wants an aggressive portfolio."**
> Willingness is one input. The case asks for "an appropriate balance between pursuing growth and protecting the capital required for her goals" (case:71-74), and capacity is set by the goals, not her personality. Also, her living costs are covered outside the portfolio (case:61-63), but outside money may not fund the payments (case:91-92). So "she has other money" is never a cover for a shortfall.

### Self-test
- **Q11.1** If yields were 0.5 points higher on 1 Jan 2027, roughly how big would the 2027 leftover be (basis D)?
- **Q11.2** Sort these into willingness or capacity: (a) "willing to take thoughtful risks"; (b) ten fixed payments with no outside money; (c) the 2028 deposit depends on her career earnings; (d) she wants growth.
- **Q11.3** Why is the 2028 deposit called the hinge of the plan?

---

## Chapter 12. How to read a range with odds (co-sponsor communication)

### The idea in 3 sentences
In 2031 Laura gives co-sponsors a range: a **bottom** that the plan is built to deliver and a **top** she *can* reach. **[checked: what the case asks]** The case asks for a dollar range and how confident the team is that the 2033 contribution will fall within it, and says the range must protect the ten payments (case:115-120). Giving a second number, the chance of reaching the top, is Caplet's own addition. In Caplet's plan the bottom comes from a rule (the Treasury floor repayment R, minus $3,700, rounded down to the nearest $5,000), the top is R plus half of VT's value in 2031, and the 2033 gift is R plus half of VT then, capped at the top. There are **two different odds** to keep apart, "lands inside the range" (about 99%) and "reaches the top" (about 3 in 4), and *neither* is the payment certainty.

### Worked example
1. **The bottom.** R = $150,000 when no top-up is needed. Compute floor((150,000 − 3,700) / 5,000) × 5,000. What is the smallest R that still gives $145,000? So what is the most the January 2027 ladder can cost before the bottom drops?
2. **The top.** From Chapter 7: 150,000 + ½ × 41,057 = $170,529 on a single "everything as expected" path. The model's median top is lower, about $167.2k. Why might that be?
3. **Reading the model's odds** (MODEL, basis D, 200,000 paths, 19 Oct; `oct20/charts/charts_data_pack.md:130-134`): the bottom is $145,000 in 61.1% of paths; the gift lands inside the range in 99.33% of paths; it lands within $1k of the top in 75.8%. Put each into plain words.
4. **The 3r twist.** If the team adopts option 3r as written, the reserve counts in the top, but in 2033 only the part above "need + $5k" is released. **[checked: agreed numbers]** On the agreed basis the gift then reaches the top in under half of model paths [consistency fix 20 Oct, row 31] (study engine 42%; range audit 34%, because its top counts the reserve's 2031 market value, about $11.5k). Counting only $5k of the reserve in the top brings it back to about three in four (study engine 73%), against about three in four with no reserve (`oct20/reconcile3r/reconcile_3r.md` sections 4e and 5; earlier figures 41% / 72%: `redteam_3r.md:153-159`). What does that do to a co-sponsor's trust?

### Answers
1. 146,300 / 5,000 = 29.26, rounded down to 29, giving **$145,000**. The smallest R is **$148,700** (148,700 − 3,700 = 145,000 exactly), so the ladder may cost up to about **$301,300** before the bottom falls to $140,000 (ignoring a little interest on the top-up; `numbers_refresh.md:140`).
2. In many model paths yields move before January, so part of the 2028 deposit tops up the ladder and leaves less for the floor and VT. With the January shift fixed at zero, the sensitivity study's median top is $170.0k; with random moves it is $167.0k (`sensitivities.md:53, 143`).
3. "In about 6 of 10 model futures the bottom is still $145,000 in 2031." "In about 99 of 100, the 2033 gift is at least the announced bottom." "In about 3 of 4 it reaches the top." None of these says "the payments are safe": that is a separate claim with its own evidence (Chapters 5 and 8).
4. A top reached less than half the time (about 45 in 100) **[checked]** is the "promised more than she gave" pattern the case warns about (case:114-115). The fix is in the top rule, not in more stocks.

**What research on communicating ranges says** (from the team's co-sponsor study; Western samples, not Taiwan funders; `oct19/cosponsor/cosponsor_research.md:118-125`):
- People treat a range as right if the outcome lands inside it. Label the bottom as firm and the top as what she "can" reach (Teigen et al. 2018).
- Words like "likely" mean different things to different readers. Put a number beside every probability word, in every language version (Budescu et al. 2014).
- Breaking a promise is judged worse than beating it is judged good (Gneezy & Epley 2014). So the bottom matters more than the top.
- Quote the range in US$, with its date, and any NT$ figure dated beside it (Chapter 10).

**Where the gift lands when markets crash** (MODEL, `sensitivities.md:160-171`): the bottom survives every crash timing, because it is a Treasury floor. A crash before the 2031 announcement lowers the range itself. A crash just before the 2033 gift (trough Jan 2033) leaves the gift about $9.5k under the announced top: still inside the range, but below the top.

### Python check I ran
```
R $150,000 -> bottom $145,000 | R $148,700 -> $145,000 | R $148,699 -> $140,000 | R $145,000 -> $140,000
ladder cost threshold for $145k bottom: 300,000 + (150,000 - 148,700) = $301,300
top (no 3r) $170,529
```
The 61.1%, 99.33% and 75.8% were read from the saved model output (`oct20/numbers/data/sheet/s19_D.json`: bottom_mode_share_145k 0.611, p_gift_inside_range 0.9933, p_gift_at_top_within_1k 0.758).

> **Common misconception: "99% confident in the range" means "99% sure she gives the top," or "the range confidence proves the payments are safe."**
> 99% is about landing at or above the bottom. The top is reached about 3 times in 4 (plan without 3r). Payment certainty is a third, separate number. A related trap: "$145,000" is not a promise anyone can make today. It is what the rule gives if the January ladder costs under about $301,300, which happens in 61-72% of model paths depending on basis (`numbers_refresh.md:130`).

### Self-test
- **Q12.1** The January 2027 ladder costs $305,000 and the $5,000 gap comes out of the 2028 deposit (ignore interest). What are R and the bottom?
- **Q12.2** Which part of the range is the "firm" part, and what makes it firm?
- **Q12.3** Rewrite "Laura will probably reach the top" so that it passes the Budescu test (a number beside the word) and names what the number measures. (Your own words; this is practice, not deliverable text.)

---

## Answers to the self-tests

**Chapter 1**
- Q1.1: 50,000 / 1.06⁶ = **$35,248**.
- Q1.2: **Less.** Higher yields mean each future dollar is discounted more. About $290 less per 0.01 point (Chapter 4), so roughly $14,000 less for half a point.
- Q1.3: The holdings end 17 days to 10.5 months *before* the payments, so on the cautious basis you buy each $50,000 earlier (and the waiting cash earns nothing). Earlier money costs more today.

**Chapter 2**
- Q2.1: 5.04 + (1/3) × (5.15 − 5.04) = **5.077%**.
- Q2.2: **No.** On a flat curve every date has the same rate, so par = zero.
- Q2.3: **Below.** The earlier coupons are discounted at higher short rates, so the last date's rate must be lower.

**Chapter 3**
- Q3.1: 18,000 × 4.375% / 2 = **$393.75** each 15 May and 15 Nov.
- Q3.2: It pays one sum on one date and nothing before, so there is nothing to reinvest. Held to maturity, the yield you buy at is the yield you get **[checked]**.
- Q3.3: **Feb-2037** (ends 15 Feb 2037, pays 1 Jan 2038: 320 days, 10.5 months) and **May-2038** (ends 15 May 2038, pays 1 Jan 2039: 231 days, 7.6 months). Which short-term Treasury ETF is WInS-listed is UNVERIFIED (`charts_data_pack.md:100-102`).

**Chapter 4**
- Q4.1: 297,162 + 25 × 288.5 ≈ **$304,375** (full repricing $304,475), so a top-up of about **$4.4-4.5k** from the 2028 deposit.
- Q4.2: The **2042** rung (3.125% Nov-2041): its money is furthest away, so its DV01 is largest (about $33 per bp).
- Q4.3: 3,710 / 289 ≈ **12.8bp**. Yes: the 10-year fell 12bp (5.27 → 5.15), and the 20- and 30-year fell 15-16bp.

**Chapter 5**
- Q5.1: 20,000 × 1.706303 = **$34,126** at the own yield; 20,000 × 1.60331 = **$32,066** at −2: about **$2,060** short on this position.
- Q5.2: Long rungs have more coupons, reinvested for longer, so more of the end value depends on reinvestment. **[checked: interest-on-interest]** For the 2042 rung, 170.63 per $100 = 100 face + 46.875 of coupons (fixed, paid whatever happens) + about 23.75 of interest earned on reinvested coupons. Only that 23.75 depends on future yields: it is the most reinvestment risk can take away (at 0%, 146.875 per $100, $6,961 short on this rung).
- Q5.3: The coupons earn *more* than assumed, so the rungs deliver more than $50,000: a surplus, not a gap.

**Chapter 6**
- Q6.1: (14.88 − 10.16) / (14.88 − 6.86) = **58.9% IEF**, 41.1% TLT (matches CLAUDE.md:163).
- Q6.2: Time passes, so the payments' duration shrinks each year while the funds' durations stay roughly constant. The weights drift out of match.
- Q6.3: Each rung's principal is cash-flow matched (it matures just before its payment). The coupons and fund distributions are not: they must be reinvested, and that leaves a duration gap of about $61 per bp.

**Chapter 7**
- Q7.1: 33,515 × 1.04³ = $37,700, so the top = 150,000 + 18,850 = **$168,850**.
- Q7.2: So the gift can never exceed what she announced, and the rest of VT stays hers for flexibility (case:101-103). Promising less and giving more is safe; the reverse damages credibility.
- Q7.3: For only about 1.8 extra points a year over the ladder, stocks would add 16.78% volatility to payments that cannot absorb any shortfall, so the plan uses stocks only for the money above the payments.

**Chapter 8**
- Q8.1: Standard deviation = 1.2 × 0.450 = 54.0bp; z = −9.83/54.0, giving **42.8%**.
- Q8.2: z = −20/45 = −0.444, giving about **32.8%**: roughly 1 in 3. (Team notes also contain "1 in 3" and "1 in 4"; those were other dates and bases, so never reuse them.)
- Q8.3: **[checked: replaced]** Keeping the unused 2027 leftover in cash until 2042 (+7.9 of about 16.5 points), with the iBond-fund model (+5.8) a close second; waiting-cash interest is a net +3.1 once all three of its effects are counted. For 3r the leftover rule is worth 0.00 (`oct20/reconcile3r/reconcile_3r.md` sections 0, 4a-4b). No single rule explains "most" of either gap, and the order of switching changes the sizes.

**Chapter 9**
- Q9.1: 50,000 / 1.025¹¹ = **$38,107**.
- Q9.2: TIPS pay more when inflation is high, but the payments are fixed dollars; you'd be hedging a risk the payments don't have, and taking on real-yield risk instead.
- Q9.3: 168,000 × (1 − 1.036⁻²) ≈ **$11,500** (`inflation.md:176`).

**Chapter 10**
- Q10.1: 50,000 × 29.20 = **NT$1,460,000**, about NT$162,000 less than at 32.445.
- Q10.2: Whoever budgets the building in NT$: the residency and its co-sponsors. Laura's US$ amount is unaffected. The plan should say who bears it.
- Q10.3: The range is quoted in 2031 and the gift is paid in 2033: two years.

**Chapter 11**
- Q11.1: At +0.5 points the basis-D cost is $283,122, so a leftover of about **$16,900**. The sensitivity study's own basis gives $15.6k.
- Q11.2: (a) willingness; (b) capacity; (c) capacity; (d) closest to willingness. **[checked]** Strictly, "she wants growth" is a *return objective*; an IPS lists return objectives and risk tolerance separately, and willingness is how much risk she accepts to pursue that growth.
- Q11.3: It is the only source of money for a January top-up, the floor and VT. If it is late or small, the range shrinks; if it never comes, payments can be short. Everything above the ladder depends on it.

**Chapter 12**
- Q12.1: R = 150,000 − 5,000 = **$145,000**; (145,000 − 3,700) / 5,000 = 28.26, rounded down to 28: bottom **$140,000**.
- Q12.2: The bottom. It is firm because it is the Treasury floor (IBTM bought in Jan 2028), rounded down for drift, and nothing in it depends on stocks. It is a rule, not a dollar amount owned today (IBTM's payout is not fixed). **[checked]** It is also the last line of cover for coupon gaps, so in very rare model paths (about 0.04% for option 1 on the agreed basis) the gift falls below it (`reconcile_3r.md` section 5).
- Q12.3: Any answer that puts a number next to the word and says what it counts works, for example "in about 3 of 4 model futures (19 Oct inputs) the gift reaches the top". Write it yourself, and remember the number changes once the team votes on the coupon option.

---

## Glossary (one page)

- **Basis (A-E):** the five ways the team prices the ladder. A/B: on the 1 January payment dates. C/D: on the holdings' end dates. B and D: curve unchanged to January (A and C use forward rates). D is the most cautious of A-E; estimates with the real holdings sized to their own maturities run about $298-301k **[checked]**. E: real coupons, reinvested at each rung's yield. Always name the basis.
- **Basis point (bp):** 0.01 percentage point. 9.8bp = 0.098 points.
- **Bootstrapping:** working out zero yields from par yields, one half-year at a time.
- **Breakeven inflation:** nominal Treasury yield minus TIPS yield; the market's price for future inflation (2.35% at 10 years on 19 Oct).
- **Cash-flow matching (dedication):** owning assets whose cash arrives when each payment is due.
- **Compound (geometric) return:** the steady yearly rate that gives the same end value; the median path's growth. **Arithmetic:** the simple average of yearly returns (higher).
- **Convexity:** price moves are not straight lines; falls in yields raise the ladder cost more than equal rises lower it.
- **Coupon:** the interest a Treasury bond pays every six months, quoted per $100 of face.
- **Coupon gap:** the shortfall if coupons are reinvested at lower yields than assumed (about $19-22k at a permanent −2 points, by basis; register row D1) **[checked]**.
- **Discount factor d(t):** today's price of $1 paid at time t.
- **Duration:** **Macaulay**: the present-value-weighted average time to the cash, in years. **Modified** (= Macaulay ÷ (1 + y/2)): the percentage change in value for a 1-point yield move. The 9.71 and 9.90 years in this guide are modified (effective) durations **[checked]**.
- **DV01:** dollar change for a 0.01-point yield move (about $290 for the ladder cost).
- **Equity risk premium (ERP):** expected stock return minus a safe return.
- **Face (par) value:** what a bond repays at maturity ($1,000 per WInS unit).
- **Floor:** the IBTM holding bought in Jan 2028 to repay what is left of the deposit (about $150k) by Dec 2032; the basis of the range's bottom.
- **iBond ETF (IBTM-IBTR):** a fund of Treasuries maturing in one year that winds up on or about 15 Dec and pays monthly; no promised amount.
- **IRR (internal rate of return):** the single rate at which the cash flows' PV equals the price (ladder 5.185% on 19 Oct, basis D).
- **LDI:** liability-driven investing: building assets around the payments owed.
- **Leftover:** any part of the $300k not needed for the ladder in Jan 2027; first cover for shortfalls.
- **Lognormal:** a model where returns compound, so values never go below zero.
- **Monte Carlo / path:** a model that invents many random futures (paths) and counts outcomes.
- **Net-minimum rule:** cut the 2031 bottom by any projected shortfall the named reserves can't cover.
- **Nominal vs real:** dollars as written vs dollars adjusted for inflation to a base date.
- **Operating reserve:** the money set aside in Jan 2033 for the ten payments (in our plan, the ladder).
- **Par yield:** the coupon at which a new bond of that length sells for $100 (what treasury.gov publishes).
- **Percentile (p5, p50, p95):** 5%, 50% (median) and 95% points of the model results.
- **PPP (purchasing-power parity):** the idea that exchange rates move to offset inflation gaps (it did not, for NT$ since 2000).
- **Present value (PV):** what a future amount is worth today at today's rates.
- **Reinvestment risk:** the risk that money received early earns less than assumed.
- **Room:** $300,000 minus the ladder cost on a stated date and basis.
- **Sampling error:** the noise from using a finite number of paths (±0.16 points at 41% with 100,000 paths).
- **STRIPS:** zero-coupon Treasuries; "NOT permitted" in this competition.
- **Top-up:** money from the 2028 deposit that completes the ladder if it cost more than $300k.
- **3r:** the AI-suggested $10k reserve in the Nov-2041 bond (not voted on; red team: MODIFY). Agreed basis: about 0.6% of paths short (worst about $3.3k); minimum $135k; top reached under half as written, about three in four if the top counts only $5k of the reserve [consistency fix 20 Oct, row 31] (`reconcile_3r.md` section 5) **[checked]**.
- **TIPS:** inflation-protected Treasuries; "NOT permitted".
- **Volatility:** the standard deviation of returns or yield changes (stocks 16.78% a year; yields about 1.0 point a year in the models, 0.71 realised in 2026).
- **WInS:** the competition's trading simulator; our book is Laura's plan scaled to $300k. Its gains never enter her projections.
- **Yield curve:** yields for each maturity on one day.
- **Zero (spot) yield:** the rate for a single payment on a single date.

---

## Appendix A. Spreadsheet lab: rebuild the ladder cost from the treasury.gov curve (Google Sheets)

Goal: reproduce **$298,641** (simple par method) and **$297,162** (bootstrap zeros, basis D), then the DV01 (**about $288.5**) and the 41% odds, for the 19 Oct 2026 close. Then do it again yourself on the 6 Nov close. Allow about 60-90 minutes.

**Step 0. Get the data.** Download the October 2026 daily par yield curve CSV from treasury.gov: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv (for November, change both `202610`s to `202611`). Find the row for your date. Use the 6 Mo, 1 Yr, 2 Yr, 3 Yr, 5 Yr, 7 Yr, 10 Yr, 20 Yr and 30 Yr columns.

**Step 1. Tab "Curve".**
- A1 `t`, B1 `par %`, C1 `shift %`. In C2 type `0` (you will change it later).
- A2:A10: `0.5, 1, 2, 3, 5, 7, 10, 20, 30`.
- B2:B10 for 19 Oct: `4.37, 4.50, 4.77, 4.85, 4.94, 5.04, 5.15, 5.53, 5.48`.
- D1 `par used %`. D2: `=B2+$C$2`, then fill down to D10.

**Step 2. Tab "Ladder" (simple par method).**
- A1:F1 headers: `holding`, `end date`, `t`, `i`, `par %`, `PV simple`.
- A2:B11: the ten holdings and end dates: IBTM 2032-12-15; IBTO 2033-12-15; IBTP 2034-12-15; IBTQ 2035-12-15; IBTR 2036-12-15; T 4.750% 2037-02-15; T 4.500% 2038-05-15; T 4.375% 2039-11-15; T 4.250% 2040-11-15; T 3.125% 2041-11-15. Type dates as real dates (Format > Number > Date).
- C2: `=(B2-DATE(2027,1,1))/365.25`
- D2 (which tenor is just below t): `=MATCH(C2,Curve!$A$2:$A$10,1)`
- E2 (straight-line interpolation): `=INDEX(Curve!$D$2:$D$10,D2)+(C2-INDEX(Curve!$A$2:$A$10,D2))*(INDEX(Curve!$D$2:$D$10,D2+1)-INDEX(Curve!$D$2:$D$10,D2))/(INDEX(Curve!$A$2:$A$10,D2+1)-INDEX(Curve!$A$2:$A$10,D2))`
- F2: `=50000/(1+E2/200)^(2*C2)`
- Fill C2:F2 down to row 11. F12: `=SUM(F2:F11)` gives **$298,641**. Check E2 = 4.988 and E11 = 5.335.

**Step 3. Tab "Zero" (bootstrap: 60 half-year rows).**
- A1:E1: `t`, `i`, `par %`, `d`, `z (continuous)`.
- A2: `0.5`; A3: `=A2+0.5`; fill down to A61 (= 30).
- B2: `=MATCH(A2,Curve!$A$2:$A$10,1)`, fill down to B60.
- C2: the same interpolation as Ladder!E2 but with A2 and B2: `=INDEX(Curve!$D$2:$D$10,B2)+(A2-INDEX(Curve!$A$2:$A$10,B2))*(INDEX(Curve!$D$2:$D$10,B2+1)-INDEX(Curve!$D$2:$D$10,B2))/(INDEX(Curve!$A$2:$A$10,B2+1)-INDEX(Curve!$A$2:$A$10,B2))`, fill down to C60. In **C61** type `=Curve!D10` (at exactly 30 years there is no tenor above, so the formula would error).
- D2: `=1/(1+C2/200)`. D3: `=(1-C3/200*SUM(D$2:D2))/(1+C3/200)`, fill D3 down to D61.
- E2: `=-LN(D2)/A2`, fill down to E61.
- Check: D2 = 0.978617, D3 = 0.956461.

**Step 4. Back on "Ladder" (zero method = basis D).**
- G1:J1: `k`, `z at t`, `DF`, `PV zero`.
- G2: `=MATCH(C2,Zero!$A$2:$A$61,1)`
- H2: `=INDEX(Zero!$E$2:$E$61,G2)+(C2-INDEX(Zero!$A$2:$A$61,G2))*(INDEX(Zero!$E$2:$E$61,G2+1)-INDEX(Zero!$E$2:$E$61,G2))/0.5`
- I2: `=EXP(-H2*C2)`; J2: `=50000*I2`. Fill G2:J2 down to row 11.
- J12: `=SUM(J2:J11)` gives **$297,162**. K12: `=300000-J12` gives the room, **$2,838**.
- Optional: the semiannual zero yield in K2: `=2*(I2^(-1/(2*C2))-1)*100` (2042 rung: **5.431**).

**Step 5. DV01 and convexity.**
- Set Curve!C2 to `0.01` (that is +1bp, because the yields are in percent) and write down J12. Set it to `-0.01` and write it down again. DV01 = (cost at −0.01 − cost at +0.01) / 2 ≈ **$288.5**.
- Try `0.5`, `-0.5`, `1`, `-1`. You should get $283,122, $311,991, $269,825 and $327,657. **Set C2 back to 0** when you finish.

**Step 6. The odds (Chapter 8).**
- Room in bp: `=K12/288.5` (about 9.8).
- Years to 1 Jan 2027: `=(DATE(2027,1,1)-DATE(2026,10,19))/365.25` (0.2026).
- Standard deviation in bp at 1.0 point a year: `=100*1.0*SQRT(0.2026)` (45.0).
- Probability: `=NORM.S.DIST(-9.83/45.0,TRUE)` gives **41.4%**. Try 0.71 instead of 1.0 (37.9%).

**Step 7. One coupon rung (Chapter 5).** **[checked: formula fixed]** On a new tab, type `0.05365` in B1 and, in A1, `=1.5625*((1+B1/2)^30-1)/(B1/2)+100`: it gives 170.63. Change B1 to `0.03365`: 160.33. In A2, `=A1*293.03` gives $50,000 (49,999 before rounding) and $46,981. (Do not type a bare `y` in the formula: Google Sheets reads it as an unknown range name and shows an error.)

**If you don't match:** check that dates are real dates (not text); that yields are in percent in the "Curve" tab but divided by 200 in the formulas; that C61 is typed; and that the shift cell is back to 0. Differences of a few dollars mean an interpolation or rounding slip. Differences of thousands mean a wrong date or tenor.

**Then move on, by yourself:** re-run the whole lab on the **6 Nov close** before quoting any figure in the Final Report (`oct19/out/Caplet_Update_19Oct2026.md:100`), and have a second student check it.

---

## Appendix B. How the numbers in this guide were checked

- **Independent code.** `oct20/learn/scripts/verify_guide.py` (pure Python, written from scratch, no earlier model imported) rebuilds Chapters 1-12's worked examples from the 19 Oct treasury.gov CSV (`oct20/learn/data/tsy_202610.csv`, copied from the chart pack's 19 Oct fetch). Output: `oct20/learn/data/verify_out.txt`. Run: `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/venv/bin/python -I verify_guide.py ../data/tsy_202610.csv` from `oct20/learn/scripts/`.
- **Second check of the Spreadsheet Lab:** `sheet_emulation.py` copies Appendix A's formulas cell by cell (MATCH, INDEX, LN, EXP) and gives $298,641 / $297,162 / DV01 $288.5 / the four shifted costs (`sheet_emulation_out.txt`).
- **Self-test answers:** `answers_check.py` gives `oct20/learn/data/answers_out.txt`. **Ladder IRR:** `irr_check.py` gives `irr_out.txt`. **The coupon-study quirk:** `quirk_check.py` gives `quirk_out.txt`.
- **What matched exactly:** the required return (5.087% / 5.024%); basis D for 6, 16 and 19 Oct ($293,453 / $298,940 / $297,162); basis B ($293,767); the simple method ($298,641); every rung cost; the Nov-2041 rung table; the 41.4% / 37.9% odds; the IEF/TLT weights; the inflation tables; the NT$ conversions; the $145k rounding rule and $301,300 threshold; the 40%-crash gift ($163,179).
- **Small differences, explained:** DV01 $288.5 (desk: $288-291); the coupon-study ladder $298,453 (study: $298,446); the whole-ladder coupon gap $19,487 at −2 (study: $18,952, because of the iBond coupon quirk; with the quirk switched on I get $18,951); the floor cost by hand, 150,000 / (1.0256)^(2 × 4.953) ≈ $116.8k (number sheet: $116,485, because it prices IBTM as a coupon bond on the forward curve; the sensitivity study's own hand check also gives $116.8k, `sensitivities.md:44`); the ladder IRR 5.185% (desk: 5.186%).
- **[checked] Superseded since this guide was written:** the option-1, 3r and "reaches the top under 3r" figures were reconciled on 20 Oct (`oct20/reconcile3r/reconcile_3r.md` section 5: option 1 about 14.4%, 3r about 0.6%, top reached 77% / 45% / 76%). The checked copy uses those; the older figures below remain correct outputs of their own models only.
- **Read from saved model output, not re-simulated:** the 15.6% / 16.4% / 32.3% / 6.2% / 0.02% payment-short odds, the 99.33% / 75.8% / 61.1% range odds, the 41% / 34% / 72% "reaches the top" under 3r, and the deposit and crash tests. The payment-short and range odds were checked against the models' saved JSON (paths in Chapters 8 and 12); the rest were checked against their source tables at the cited lines.
- **Not re-checked here (cited only):** the inflation and currency history (FRED, DGBAS, CBC data in `oct20/inflation/`), the JPM figures (verified from the PDF on 27 Sep per CLAUDE.md), and the co-sponsor research findings.

## Appendix C. Things this guide could not confirm (UNVERIFIED)

- Whether IEF or TLT is listed on WInS (Chapter 6 uses them only as teaching examples).
- Which short-term Treasury ETF is WInS-listed for the 2037-38 waiting cash.
- When WInS credits coupons and fund distributions, and whether its total counts accrued interest.
- JPM 2027 LTCMA's inflation figure (login wall).
- How closely Laura's career income moves with markets (Chapter 11's human-capital point is an interpretation).
- Whether the FAQ's TIPS/STRIPS ban also covers ETFs built on them (on the batch-2 Wharton question list).
