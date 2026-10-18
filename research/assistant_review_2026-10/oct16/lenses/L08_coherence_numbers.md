# L08: Do the three deliverables agree, and are the numbers right?

Prepared Fri 16 Oct 2026 (Sydney) from the read-only repo. This is AI review for planning only, not text to submit.
"MODEL" means a computer estimate, not a market fact. "bp" means 0.01 percentage point.
Where a finding repeats the 15 Oct brief, it says so and adds only what is new.

Working files (scripts and data) are in `oct16/lenses/L08/`:
`par2026_live.csv` (official Treasury par curve, downloaded 16 Oct, now includes the **15 Oct close**),
`series_live.csv` (ladder cost each day), `split.py` (the 2028 plan split).

---

## 0. The five things that matter most

1. **The ladder has almost no room left (new).** On the 15 Oct close the ten payments cost **$298,624** on 1 Jan 2027 on the IBTR note's own basis. That leaves **$1,376**, or **4.7bp**. On 6 Oct it was 22.7bp. The IBTR note says "about 0.2 percentage points". V5 says "$292,000". Both are now badly out of date. A rough model puts the odds that the ladder costs more than $300k by January at **about 45%** (MODEL). The 2028 top-up is now a central case, not a tail.
2. **The stock share in the plan has fallen to about 7%, but WInS holds 8.8% (new).** "~9%" and "~$40k" appear in several files. On the 15 Oct curve the plan gives 7.2% and about $33.5k. COMPETITION.md calls the drift "trivial" because it measures against fixed 6 Oct targets.
3. **The VT trade note and IPS V5 disagree about what the stock fund does (new).** The note says stocks "only" set how far the gift rises. V5 also gives Laura's half of the fund three more jobs.
4. **There are six definitions of the floor.** The team's own research memo rejects quoting $150k because the IBTM floor "pays under $150,000 about 2 times in 3". Yet $150k is still the figure in most team files.
5. **"Never below the floor" survives in V5 only because the floor was STRIPS.** The team journal says so. The 6 Oct email removed that reason.

---

## 1. Findings

Severity scale: critical = could cost a Top-50 place; high = clearly lowers the score; medium = a visible weakness; low = polish.

### COH-01. The ladder's headroom has nearly gone, and three deliverables quote old figures (high, new)

**Evidence (recomputed, MODEL):** official par curve, home.treasury.gov CSV, accessed 16 Oct 2026. The 15 Oct row reads 5y 4.91, 7y 5.00, 10y 5.10, 20y 5.48. Repriced with the independent pricer the 15 Oct brief used (`scratchpad/indep_pricer.py`, `oct14/numbers/scripts/series2.py`). Output is in `L08/series_live.csv`.

| Basis (cost on 1 Jan 2027) | 6 Oct | 14 Oct | **15 Oct** |
|---|---|---|---|
| WInS-listed maturities, yields unchanged (the IBTR note's basis) | $293,448 (22.7bp) | $295,988 (13.9bp) | **$298,624 (4.7bp)** |
| WInS-listed, forward rates | $292,327 (26.6bp) | $295,076 (17.0bp) | **$297,778 (7.7bp)** |
| Old Nov-15 STRIPS, forward rates (superseded) | $291,039 (31.0bp) | $293,798 (21.4bp) | **$296,506 (12.0bp)** |

Since the trades, yields have fallen about 15-20bp: 7y 5.15 to 5.00, 10y 5.27 to 5.10, 20y 5.68 to 5.48. The 6 Oct levels are from `ops/routines/MONITOR.md:22`.

**Rough odds that the ladder costs more than $300k on 1 Jan 2027:** about 45% (44.8-46.3%). Method: a driftless normal move. The daily change in the 7-20y yield has a standard deviation of about 4.5-5bp in 2026 (calculated from the same CSV). There are about 52 bond trading days left in 2026. This is a rough MODEL, not a forecast.

**Where the old numbers sit:**
- IBTR note (filled order, 7 Oct 4:42 AM ET), `team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15`: "If yields fall more than about 0.2 percentage points by January". The note was true on 6 Oct and cannot be edited.
- Pick rationale, `05_...md:29`: "Yields have fallen slightly since the trade". The fall is now 15-20bp, which is not "slight".
- IPS V5 pitch and body, `01_version_5.md:16` and `:24`: "about $292,000 of Treasuries" and "At late-September 2026 yields they cost about $292,000".
- COMPETITION.md:153-154: "It costs about $293k on the 6 Oct curve; a fall in yields of about 0.2 percentage points would push it above $300k."
- MONITOR.md:22 uses a fixed 6 Oct baseline. `ops/monitor_reports/2026-10-13 Caplet check.md:7` says "about 20bp is left".

**Why it costs us:**
- Judges read all three deliverables together (Client_Profile.txt:161-162). A TNA reflection that says "slightly", an IPS that says $292k and a Final Report that says about $299k would look like three different plans.
- Worse, V5 treats the top-up as a side case ("if falling yields push that above $300,000"). It is now close to a coin toss.
- Under V5's own rule, a top-up shrinks the floor, because the floor is "sized to return that remainder" (V5:24). Every file that says "$150k floor" then becomes wrong in about half the outcomes. A 25bp fall from the 15 Oct curve adds about $7.3k to the cost (DV01 about $290/bp; CLAUDE.md:121-122). That means a top-up of about $6k and a floor of about $144k.

**What a fix must achieve:**
- Every ladder figure carries a date and a basis, and the team uses one basis everywhere.
- The IBTR reflection uses a re-run figure dated by the writer (the 15 Oct brief already planned this as item 14).
- The IPS either uses no point estimate or gives a figure that survives a ±25bp move, and it treats the top-up as an expected branch with a stated effect on the floor.
- The Final Report shows the cost path from 6 Oct to the freeze.

**Deadline:** TNA re-run Mon 19 Oct; IPS by Wed 4 Nov; FR re-price on the 6 Nov close.

---

### COH-02. The plan's stock share is now about 7.2%, but WInS holds 8.8% VT (high, new)

**Evidence (MODEL, `L08/split.py`):** Laura's money on 1 Jan 2028, same curve, floor = IBTM-like holding returning $150k at 15 Dec 2032.

| Curve | 2027 leftover | Floor cost | Stock fund | Ladder / floor / fund share |
|---|---|---|---|---|
| 6 Oct | $6,552 | $117,171 | $39,381 | 66.5% / 25.1% / **8.4%** |
| 14 Oct | $4,012 | $117,369 | $36,643 | 67.0% / 25.1% / **7.8%** |
| 15 Oct | $1,376 | $117,894 | $33,483 | 67.6% / 25.3% / **7.2%** |

**Where the figures conflict:**
- WInS: VT 167 shares at $158.83, which is 8.84% of $300k at cost (COMPETITION.md:186; `ops/routines/portfolio_check.py:9`).
- Sheet target: 8.7% (`team/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv:12`).
- "~9% of all money": COMPETITION.md:156 and CLAUDE.md:96.
- "about $40k": `notes_and_discussions.md:109` and `:118`; CLAUDE.md:92; Tab 7 "40K goes to growth" (`09_old_versions_v3_tab_7.md:20`); Strategy Brief p.3 "~$40,000".
- COMPETITION.md:188-189: "Every weight is within 0.2 pt of target … drift is trivial". That compares against fixed 6 Oct targets, not against the re-priced plan.
- The team's own October rule sizes VT to "the new stock-fund share the refresh prints" (`rab/trades/october_trade.md:39`, trigger B). That assumes WInS should track the re-priced plan.

**Why it costs us:**
- The frozen 6 Nov book is the "implementation" the Final Report must evaluate (IPS-FINAL.txt:75-78).
- If the report says the plan is about 7% stocks while WInS shows about 9%, judges see drift.
- The cause is that the 2027 leftover shrank from about $8k (Tab 7) to about $1.4k. A further rally pushes the fund toward about 6%.

**What a fix must achieve:**
- A recorded team decision on what the WInS mirror is pinned to. Either it is the 6 Oct trade-date snapshot, with a stated tolerance band, or it is re-priced, which would need a vote, a second check and Ray placing it by Wed 4 Nov 4:00 pm ET.
- Every "9%" or "$40k" in team files is replaced by a dated figure.
- The Final Report explains the gap in one line.

**Deadline:** decision by Tue 27 Oct (vote set B); IPS Fri 6 Nov.

---

### COH-03. The VT trade note says stocks "only" affect the gift, but V5 gives Laura's half four jobs (high, new)

**Evidence:**
- VT note (filled, 7 Oct 8:27 PM ET), `05_...md:14`: "They only set how far her gift rises above her promised minimum."
- V5 makes the stock money do more:
  - The second source for any payment shortfall: "first from the 2027 leftover, then the half Laura keeps, then the contribution above the floor" (`01_version_5.md:26`).
  - The defence against inflation and the Taiwan dollar: "the equity half Laura keeps is her defense" (`:28`).
  - A cushion: "The other half stays with Laura as a cushion if costs rise or co-sponsors fall short" (`:30`).
- The "2027 leftover" (first source) is itself stock money. Tab 15's notes record "Tab 7 的计算（40K = 32K + 8K）显示它进了增长部分" ("Tab 7's calculation shows it went into the growth part") (`15_tab_15.md:34`). The sheet's 8.7% VT weight matches the $40k (32k + 8k) figure.
- Size, MODEL: the fund is about $33.5k in 2028 (COMPETITION.md / COH-02). Grown at JPM's 7.0% compound for All Country World (CLAUDE.md:126), it is about $47k by 2033. Laura's half is then about **$23k**. The 2027 leftover is about **$1.4k** on the 15 Oct curve, and $0 if the ladder costs more than $300k.

**Why it costs us:**
- The VT note cannot be edited, and the TNA must be "consistent with the strategic approach your team … will later articulate in its IPS" (TNA-FINAL.txt:30-31).
- A judge reading both sees one fund doing four jobs. About $23k cannot back payment shortfalls, inflation, a stronger Taiwan dollar and co-sponsor shortfalls all at once.
- The first line of defence (the leftover) is close to zero and is invested in stocks.

**What a fix must achieve:**
- One ordered list of what Laura's half is for, with the size of each claim stated or bounded.
- The VT reflection explains the note's "only" honestly, as "true for the gift, not for her cushion", without repeating it.
- The IPS says where the 2027 leftover waits and whether it is safe money.

**Deadline:** vote set A/B (Sun 18 Oct / Tue 27 Oct); TNA Thu 22 Oct.

---

### COH-04. Six different floor definitions, and the team's own memo rejects the most common one (high, known-deeper)

| Definition | Where |
|---|---|
| "$150k" face, "already owns", "locked into a Treasury" | `team/google_drive/strategy_notes.md:47`; `notes_and_discussions.md:110`, `:121`, `:302`; Strategy Brief p.3 "the $150,000 she owns"; `final_report.md:21` "backed the $150k floor" |
| IBTM "sized to return about $150k by 2033" | COMPETITION.md:155-156 |
| "a 2032 Treasury ETF sized to return that remainder" (shrinks if the ladder is topped up) | V5 `01_version_5.md:24` |
| bottom "quoted rounded down after any expected shortfall" | V5:30; COMPETITION.md:158-159 |
| bottom "quoted at the 2032 ETF's projected payout rounded down" | Tab 15 `15_tab_15.md:16` (its note :30 explains the change) |
| "the floor holding's worst case, rounded down to $5,000 ($145,000 today)" | `rab/decisions/D_range_confidence_2031.md:8` |

- The same memo rejects option B, "'Cannot fall outside', floor quoted at $150,000 face", because "the iBond-fund floor pays under $150,000 about 2 times in 3" (`D_range_confidence_2031.md:18`). Its typical payout is about $149k and its worst about $146k (`:23-24`; STRIPS-era 28 Sep MODEL, re-run before quoting).
- V5 also contradicts itself. Line 26's shortfall order never touches the floor ("… then the contribution above the floor"). Line 30 says the bottom is the floor "rounded down after any expected shortfall", which implies the shortfall does come out of the floor. Tab 15:30 flagged the two readings.

**Why it costs us:** the bottom of the 2031 range is the number the case cares most about. It says "If Laura promises more than she can ultimately contribute, she could damage her credibility" (Client_Profile.txt:114-115). Three deliverables with three different bottoms is the inconsistency judges are told to look for.

**What a fix must achieve:**
- One sentence-level definition that covers: what the floor holding is (IBTM), what it is sized to (fixed $150k, or the remainder), what number is quoted (rounded down how far, and why), and what happens to it after a top-up (COH-01).
- The team uses the same definition in all three deliverables and retires the "$150k she owns" phrasing in team files.

**Deadline:** vote set A Sun 18 Oct (before the IBTM reflection).

---

### COH-05. "Never below the floor" lost its reason on 6 Oct (high, new angle)

**Evidence:**
- Team journal, `team/google_drive/final_report.md:24`: "5 Oct: … we realised the facility floor counted inside the operating reserve. We fixed four phrases and kept 'never below the floor' on purpose (STRIPS in real life, IBTM as the WInS stand-in)."
- The 6 Oct email removed STRIPS: "may include only approved investment types: eligible stocks, ETFs and Treasury bonds available on WInS" (COMPETITION.md:87-90). IBTM is now the real floor (COMPETITION.md:155), and the IBTM note says "the final payout is not fixed" (`05_...md:19`).
- V5:28 still says "Markets can shrink the facility contribution, but never below the floor".
- Several files still call IBTM a "stand-in" or "building-minimum stand-in": COMPETITION.md:176 "2028 floor stand-in"; CLAUDE.md:97-98.
- The journal has no 6 Oct entry (it jumps from 5 Oct to "Oct7").

**Why it costs us:**
- The certainty claim is worded as if the old instrument were still used.
- The Articulation criterion rewards "response to challenges" (deliverables.txt:58). The 6 Oct change is the team's best real "challenge" story, and it is missing from the journal.

**What a fix must achieve:**
- Every absolute word about the floor in the IPS matches the IBTM note.
- The journal records, in the students' words and with the date, what the 6 Oct email changed (STRIPS to IBTM; "stand-in" to "real holding") and how the wording changed.

**Deadline:** journal entry by Sun 25 Oct; IPS Fri 6 Nov.

---

### COH-06. What the WInS book stands for is stated three ways, and the notes skip the scale (high, known-deeper)

**Evidence:**
- Official: "The $300,000 is your team's WInS simulator balance" (`smapply_public_2026-10-14/trading.txt:26`), and "The WInS portfolio represents each team's implementation of its investment strategy" (Client_Profile.txt:129).
- COMPETITION.md:70 adds its own gloss: "$300,000 virtual (= Laura's 2027 deposit; the $150k is NOT added)". CLAUDE.md repeats it.
- The book actually traded is "Laura's plan on 2 Jan 2028, after both deposits, scaled to WInS's $300,000" (`portfolio.csv:2`). The scale factor is about **0.643** ($300k ÷ about $467k; COH-02 table). So each WInS rung is sized for about $32k of a $50k payment. For example, IBTO's $23.4k grows to about $32k by Dec 2033, not $50k.
- Notes: 9 of the 11 filled notes speak of "Laura's $50,000 payment" or "payment" without scale. Only Nov-2041 says "scaled to the model portfolio" (`05_...md:24`). The cancelled Nov-2039 note said "scaled 2040 payment" (`:40`), but the filled version says "$50,000 payment" (`:18`).
- The IBTR note says "her first $300,000 is enough to buy Treasuries for all ten payments" (`:15`), while WInS put only 65.9% of its $300k into the ladder (`portfolio.csv:10`).
- V5:26 says "Our WInS portfolio shows this allocation, scaled down" but gives no factor or date.
- `deliverables/ips_outline.md:3` says "WInS is the real ladder", which is wrong.

**Why it costs us:** Wharton verifies the notes against executed trades (TNA-FINAL.txt:53). A judge who checks IBTO's size against "$50,000 payment" finds a gap. Unless the scale is explained once and the same way everywhere, it reads as a sizing error.

**What a fix must achieve:**
- One stated mapping, the same in all three deliverables: which date's plan, the scale (about 64 cents of WInS per plan dollar), and why VT and the floor are in WInS although the $150k is not.
- COMPETITION.md:70 drops the "= 2027 deposit" gloss.

**Deadline:** TNA Thu 22 Oct (one clause in the IBTR or IBTM reflection); IPS Fri 6 Nov.

---

### COH-07. V5 says each payment "depends mainly on the US government", but the trade notes admit two more risks (medium-high, known-deeper)

**Evidence:**
- V5:20: "so once bought, each payment depends mainly on the US government paying its debts".
- Notes on filled trades say otherwise:
  - "reinvested coupons fund the rest" (Nov-2039, `05_...md:18`);
  - "reinvested coupons funding part of each" (Nov-2041, `:24`);
  - "reinvestment-rate risk on the proceeds" (Feb-2037, `:16`);
  - "the final payout is not fixed" (IBTM, IBTO, IBTP and IBTQ, `:19-22`).
- Recomputed (WInS holdings, scale 0.643, so the target per rung is about $32,150; MODEL):

| Bond rung | Principal as share of target | Delivered if coupons earn 0% / 2% / 4.5% |
|---|---|---|
| 4.750% Feb-2037 | 62% | 93% / 98% / 105% |
| 4.500% May-2038 | 62% | 96% / 101% / 109% |
| 4.375% Nov-2039 | 56% | 89% / 94% / 101% |
| 4.250% Nov-2040 | 56% | 90% / 96% / 105% |
| 3.125% Nov-2041 | 62% | 92% / 98% / 106% |

So 38-44% of each bond-funded payment comes from coupons and what they earn. The break-even rate is about 2-4%. (The rab kit's 28 Sep figures, "$466k if coupons earn 2%, $447k at 0%" (`rab/assumptions.md:11`), are on another basis. Re-run them before quoting.)

**Why it costs us:** the case asks teams to "define what they consider a high degree of funding certainty … and identify the assumptions" (Client_Profile.txt:97-99). The TNA notes already name reinvestment risk, so an IPS that names only default risk contradicts our own executed evidence.

**What a fix must achieve:**
- The IPS certainty standard names the residual risks: issuer, coupon reinvestment, iBond payout variation and the early-maturity wait. It also says which money covers each.
- The Final Report quantifies them with dated numbers.

**Deadline:** vote set B Tue 27 Oct; IPS Fri 6 Nov.

---

### COH-08. "$292,000" has no stated basis, and CLAUDE.md marks a superseded figure "VERIFIED" (medium; corrects the 15 Oct brief)

**Evidence:**
- The 15 Oct brief said V5's "$292,000 at late-September yields" uses the old STRIPS basis (final.md §2). That is only half right. It reproduces on two bases:
  - the STRIPS/idealised value of $292,264 on the 25 Sep curve (CLAUDE.md:121);
  - the WInS-listed forward basis on 29-30 Sep: $292,844 and $291,850 (`L08/series_live.csv`).
- On the IBTR note's basis (WInS-listed, yields unchanged), late September was $293,025-296,704.
- So the real defect is a missing date and basis label.
- CLAUDE.md contradicts itself. Lines 121-122 list "headroom … $7.7k = 27bp" under "VERIFIED". Lines 106-107 correct it ("$294,387 … headroom $5,613 (19bp), not $7.7k/27bp").
- Other ladder costs in team files:
  - $294,000 (`notes_and_discussions.md:65`);
  - $289,119 (`:318`);
  - $297k (`:362`);
  - $298k (`deliverables/ips_outline.md:20`; `final_report_outline.md:5`).

**What a fix must achieve:**
- One named basis: "WInS-listed maturities, priced on [date] curve, yields unchanged to 1 Jan 2027".
- Every older figure is labelled superseded in the team's numbers sheet.
- The "VERIFIED" label on CLAUDE.md:121-122 is corrected.

**Deadline:** Mon 19 Oct (before the reflections).

---

### COH-09. One strategy, six names (medium, known-repeat with additions)

| Name | Where |
|---|---|
| Root-and-Branch | IPS V5 `01_version_5.md:16`, `:24`; V4; Tab 15; journal "Strategy name settled as Root-and-Branch (earlier 'Roots First')" (`final_report.md:21`) |
| Roots First | COMPETITION.md:147 (section heading of the "single source of truth") and :204 ("Make the Messy Roots -> 'Roots First' link visible") |
| Lock early | CLAUDE.md:65 |
| Keep every promise, grow the rest | `research/insight_v1/Team_Caplet_Strategy_Brief.pdf` p.1 title |
| Lock, then grow | `deliverables/ips_outline.md:18` |
| "two cheques" | `deliverables/final_report_outline.md:5` |

**Why it costs us:** "maintains consistency with the team's IPS" is part of the Investment Strategy criterion (deliverables.txt:55). The team's own source of truth still uses the retired name, so a teammate who checks it will copy the wrong one.

**What a fix must achieve:** one name (the team's vote), used identically in the TNA, the IPS and the FR; the Messy Roots link stated once.

**Deadline:** vote set A Sun 18 Oct.

---

### COH-10. The Feb-2037 coupon is wrong in COMPETITION.md, and that changes any yield worked out from it (medium, known-repeat + consequence)

**Evidence:**
- COMPETITION.md:181 says "5.000% T-bond Feb-2037".
- WInS shows `B-T-4.750-15022037` (`05_...md:16`). The sheet has "T 4.750% 15-Feb-2037" (`portfolio.csv:25`), and so does `portfolio_check.py:12`.
- The 5.000% issue is the May-2037 bond, which WInS did not list (`trading_notes.csv:129`, "WInS does not list the 5.000% May-2037 (checked 5 Oct)").
- Recomputed: at the 96.019 fill on 8 Oct, the 4.750% coupon gives a 5.25% yield. A 5.000% coupon would give 5.51%, which is 26bp off the curve (`scratchpad/oct14_ytm.py`).

**Why it costs us:** a student who uses the source of truth to describe the holding, or to compute its income, puts a false fact into the Final Report's implementation review.

**Fix:** correct the line and add the coupons to rows 183-185. **Deadline:** before FR drafting (10 Nov), sooner is better.

---

### COH-11. The operating reserve's size is never defined, and old figures conflict (medium, new)

**Evidence:**
- The case requires the team to "recommend its size and initial asset composition and explain how its composition should change" (Client_Profile.txt:94-97).
- Team figures:
  - "median value ≈ $413k" (`deliverables/ips_outline.md:52`);
  - "the reserve costs about $439k instead of $422k" (`notes_and_discussions.md:349`, an older growth-first model);
  - "That's $500,000 in total" (`:51`).
- V5 only says "In 2033 the payment Treasuries become the operating reserve" (`:26`).
- Recomputed (MODEL, 15 Oct curve): market value on 1 Jan 2033 of the ten payments (first included) is **about $396k** on forward rates, or about $405k if today's curve still applies in 2033.
- The composition path is not written anywhere:
  - each iBond fund turns to cash in its December;
  - the Feb-2037 and May-2038 proceeds wait in "a short-term Treasury ETF" (`05_...md:16-17`), which V5 never mentions (Tab 15 flagged this at `15_tab_15.md:35`).

**Why it costs us:** the reserve's size is one of the case's named outputs. Three different numbers (or none) across the IPS and the FR read as not having done it.

**What a fix must achieve:**
- One definition of "reserve size": market value on 1 Jan 2033, or the face of the holdings, or the $500k of payments.
- One composition path from 2033 to 2042, matching the trade notes.
- Old numbers retired.

**Deadline:** IPS principle by 6 Nov; FR numbers by 4 Dec.

---

### COH-12. The shortfall order is different in V5 and in the research memos, and V5 drops the 2031 check (medium, known-deeper)

**Evidence:**
- V5:26 and Tab 15:20: 2027 leftover, then Laura's half, then the contribution above the floor.
- `rab/decisions/D6_cap_share.md:79` says "Name her half as the first cover".
- `D_range_confidence_2031.md:44-45`, condition 5, says "Laura's half pays first, then the gift above the floor". `:47` adds "the 2031 check lowers the top before it is announced if Laura's half cannot cover a shortfall". V5 has no such check.
- The 15 Oct brief noted that rab memos end in "her own money", which the case forbids.
- Effect: under V5 a large coupon shortfall is absorbed in 2033, after the 2031 top has been quoted.

**What a fix must achieve:**
- One complete order: from first source to last, with the floor's place stated.
- A decision on whether the 2031 quote is adjusted for a known shortfall.
- The same order in the IPS and the FR.

**Deadline:** vote set A/B.

---

### COH-13. "Income reinvested … held without trading" fits neither WInS nor the trade notes (medium, known-repeat)

**Evidence:**
- V5:26: "Until 2033 the portfolio is held without trading, with income reinvested in the holding that paid it."
- WInS plan: hold, no more trades. iBond distributions and coupons arrive as cash at 0% (COMPETITION.md:80, :188-190).
- Bond coupons arrive in amounts smaller than a $1,000 unit. A $475 half-year coupon on $20k of the 4.750% bond cannot buy another unit (COMPETITION.md:82).
- The Feb-2037 and May-2038 notes put early proceeds in "a short-term Treasury ETF" (`05_...md:16-17`).
- The sheet's research brief says the money "waits in Treasury bills (0% in WInS)" (`trading_notes.csv:129`). T-bills are not on WInS, so they are not allowed after 6 Oct.
- Tab 15 itself noted that "held without trading" clashes with the 2028 purchase (`15_tab_15.md:29`).

**What a fix must achieve:** one rule for income and early proceeds that is true in Laura's plan and explained for WInS (cash at 0%, accepted on purpose or not).

---

### COH-14. "Latest payments first" versus the order timestamps (low-medium, new)

**Evidence:**
- V5:24: "The 2027 deposit buys the payments latest first".
- The order times in WInS:
  - Nov-2041 and Nov-2040 went in first (6 Oct 7:55 and 7:59 PM);
  - then IBTQ, IBTP, IBTO and IBTM, for 2033-36 (8:36-10:01 PM);
  - then the re-placed Nov-2039, May-2038, Feb-2037 and IBTR (6 Oct 11:45 PM to 7 Oct 4:42 AM) (`05_...md:14-24`).
- Two of the suggested picks show it: IBTM (6 Oct 10:01 PM, 2033 payment) went in before IBTR (7 Oct 4:42 AM, 2037 payment).
- The kit's tickets say the trade order was "for cash control only. It is not the IPS rule 'latest payments first'" (`rab/trades/tickets.md:17`). All the ETFs filled at the same 7 Oct open.

**Why it costs us:** this is a small trap. A judge comparing timestamps with the IPS could think the trades broke the rule.

**Fix:** the team can explain in one line, if asked or in the FR, that the rule is about which payments a short deposit funds, not the order of trades. Do not claim WInS followed it.

---

### COH-15. Out-of-date team files will feed the Final Report (medium, known-deeper)

**The files most likely to be reused:**
- `team/google_drive/notes_and_discussions.md` (the export has a banner only at the top):
  - $294k and "$5,600 to spare" (`:65`, `:71`);
  - "1 time in 3" (`:71`) against "about a 1 in 4 chance" (`:322`) in the same document;
  - All-Treasuries "$204k" (`:193`) against "$202k" (`:295`);
  - "$289,119, the cheapest since May 2002" (`:318`);
  - "we buy ten US Treasury bonds. One matures in 2033 …" (`:596`), which is false because WInS has no 2031-36 bonds (COMPETITION.md:94);
  - "a $150k building floor she already owns" (`:121`).
- `research/insight_v1/Team_Caplet_Strategy_Brief.pdf` has **no superseded notice inside the PDF**. A text search finds no "STRIPS" or "superseded". It says, for example:
  - p.3 "ten U.S. government bonds, one maturing just before each $50,000 payment";
  - "a bond that repays $150,000 … money … she owns outright";
  - "~$40,000";
  - "about $294,000".
  - CLAUDE.md:101 presents it as the team's readable report.
- `research/insight_v1/trading_notes_pack.md` (no banner) recommends "IEF + TLH". The README for that folder has no banner either. CLAUDE.md:85-86 calls these "the two primary files".
- `deliverables/cosponsor_talking_points.md` (a "committed minimum … ≈ $113k") and `final_report_outline.md:5` ($298k, $113k).

**What a fix must achieve:**
- Before 9 Nov, every file a student might open for the FR either carries a dated "superseded" notice or is archived.
- One dated numbers sheet is the only source of Final Report figures. The 15 Oct brief's item 25 already says this; these are the specific files.

---

### COH-16. The IPS outline tells students to "show chart 02", which the IPS rules ban (low-medium, new)

**Evidence:**
- `deliverables/ips_outline.md:19`: "Show chart 02 (certainty vs facility)".
- Official: "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted" (IPS-FINAL.txt:123).
- Non-compliant submissions "will not be considered for semifinal selection" (:82-83).

**Fix:** remove or banner the line. Charts belong only in the Final Report, if its 9 Nov instructions allow them (UNVERIFIED until then).

---

### COH-17. Rule statements that go beyond the official wording (low, new)

- **What decides the Top 50.**
  - The live Rules & Roles page (accessed 16 Oct 2026) says: "The top 50 teams will be selected as semifinalists based on the strength of their Investment Policy Statement (IPS) and Final Reports."
  - SMApply says: "Your Trading Notes Analysis, Investment Policy Statement and Final Report are evaluated" (deliverables.txt:28). The case says "Evaluators will consider the three deliverables together" (Client_Profile.txt:161).
  - CLAUDE.md:26 states as fact that the Top 50 is "chosen on the written Trading Notes, IPS and Final Report".
  - Keep treating all three as scored, as the scoresheet does (`team/Winning Team Portrait and Scoresheet.md:19-20`). Do not repeat CLAUDE.md's version as a rule.
- **The semifinal format.**
  - COMPETITION.md:26 says "short video presentation, all members present".
  - The FAQ says "a short presentation (via video conference for the Semifinals) … All team members must participate" (faqs.txt:89).
  - The Rules page bans "Video recording … during the Semifinals". So it is a live video call, not a recorded video.

---

### COH-18. "About 91% Treasuries" uses a different basis from other files (low, new)

**Evidence:**
- COMPETITION.md:98 and `ops/monitor_reports/2026-10-13 Caplet check.md:16`: "about 91% Treasuries".
- The kit's ledger: "dated holdings incl. floor 89.51% (tab target 90.2%)" (`rab/trades/tickets.md:124`).
- At cost the book is about 90% Treasuries if cash is counted, and about 91% if it is not.

**Fix:** state the basis once in the FR, where the "Long Equities" pie-chart point will be explained.

---

### COH-19. Several numbers and sources go stale before 6 Nov and 4 Dec, and no re-price rule exists (medium, new)

| Item | Last value in team files | Changes | Re-price rule a fix must set |
|---|---|---|---|
| Ladder cost and room | $293k / 0.2pp (6 Oct) | daily, about $290 per bp | One basis. Price on the 6 Nov close for the IPS/FR and on the writer's date for the TNA. Always quote with the date. |
| Odds of a top-up | "1 in 3", "1 in 4 to 1 in 3" | daily | Re-run with the cost, or describe without a number. |
| 2027 leftover, floor cost, stock fund, plan split | $8k / $118k / $40k / 66-25-9 | daily | Recompute from the same run as the ladder (COH-02). |
| WInS value and weights | $301,950, 13 Oct | daily; iBond distributions as cash near 6 Nov (COMPETITION.md:190) | FR uses the frozen 6 Nov book only. |
| Fed decisions | 3.75-4.00% after 16 Sep (CLAUDE.md:139) | next FOMC 27-28 Oct, per Chicago Fed listings found by search on 16 Oct; the Fed marks dates tentative | Re-check on 29 Oct, before the IPS is finalised. |
| JPM LTCMA return assumptions | 2026 edition, data 30 Sep 2025 (CLAUDE.md:126) | a newer edition may come out before 4 Dec. Not found in a 16 Oct search (UNVERIFIED) | Check JPM's site before FR drafting; state the edition and its data date. |
| VT stocks and fee; IBTP premium | 10,088 (31 Aug); 0.06%; 0.07% (2 Oct) | monthly / daily | Dated, as the notes already are. Re-check fact sheets for the FR. |
| Taiwan CPI, USD/TWD | Aug 2026; 18 Sep (CLAUDE.md:139-140) | monthly / daily | Re-pull for the FR inflation section. |

---

### COH-20. The same things go by different names across the TNA notes and the IPS (medium, known-deeper)

**Evidence:**
- The facility money goes by six names:
  - "facility contribution" (V5:20, :28);
  - "gift" (V5:16; VT note `:14`);
  - "minimum contribution" (V5:16);
  - "promised minimum" (VT note);
  - "minimum figure" (IBTM note `:19`);
  - "building money" (Strategy Brief p.3).
- The payments are "running costs" (pitch) and "operating payments" (V5:20).
- "secure" (V5:16) and "promised" (VT note) are on the 15 Oct brief's list of words to avoid.

**What a fix must achieve:**
- A short glossary of about six terms (payments, ladder, reserve, floor, quoted bottom, top, gift, Laura's half), used the same way in all three deliverables.
- Where a filled note used a different word, the reflection maps it once.

---

## 2. Cross-location table (quick reference)

| Topic | Location A | Location B | Which is right |
|---|---|---|---|
| Feb-2037 coupon | COMPETITION.md:181 "5.000%" | WInS `B-T-4.750-15022037` (05_...md:16) | 4.750% |
| VT shares | sheet target 164 (portfolio.csv:30) | WInS 167 (COMPETITION.md:186) | 167 (actual); the reason is still unrecorded (15 Oct brief) |
| Ladder cost | V5 "$292,000" (:16, :24) | 15 Oct close $298,624 (MODEL) | Neither is "right"; date and basis needed |
| Headroom | IBTR note "about 0.2" (:15) | 4.7bp on 15 Oct (MODEL) | Dated; the note was true on 6 Oct |
| Floor | "$150k" (strategy_notes.md:47) | "remainder" (V5:24); "$145k" (D_range:8) | Team decision; the memo rejects $150k face |
| Stock share | "~9%" (COMPETITION.md:156) | 7.2% on 15 Oct (MODEL); WInS 8.8% | Dated figure plus a mirror rule |
| Who covers a shortfall first | 2027 leftover (V5:26) | Laura's half (D6:79) | Team decision |
| VT's role | "only" the gift (VT note :14) | three more jobs (V5:26, :28, :30) | Must be reconciled |
| WInS mapping | "= 2027 deposit" (COMPETITION.md:70) | 2 Jan 2028 plan × 0.643 (portfolio.csv:2) | The latter (what was traded) |
| Strategy name | Roots First (COMPETITION.md:147) | Root-and-Branch (V5; journal 1 Oct) | Root-and-Branch per journal; team to confirm |
| Headroom (CLAUDE.md) | $7.7k / 27bp "VERIFIED" (:121-122) | $5,613 / 19bp correction (:106-107) | Both superseded; use COH-01 |
| Top-50 basis | TNA+IPS+FR (CLAUDE.md:26) | IPS + Final Reports (Rules page, 16 Oct) | Official pages differ; treat all three as scored |

## 3. What was checked and what was not

Checked:
- COMPETITION.md, START_HERE.md, CLAUDE.md;
- IPS V5, V4, Tab 15 and Tab 7;
- all 15 trade notes;
- the journal, strategy notes, notes and discussions, client portrait and team info pack;
- the sheet exports (portfolio, trading_notes, rb_tickets);
- rab tickets, numbers.yaml, D6, D_range and the October rule;
- insight_v1 README and trading_notes_pack, and the Strategy Brief PDF (text extracted);
- deliverables/ outlines; config/client_mandate.yaml; ops MONITOR and the 13 Oct report; portfolio_check.py;
- the official case, the TNA and IPS instructions and the SMApply snapshots;
- the live Rules & Roles page (16 Oct);
- the Treasury par curve to the 15 Oct close.

UNVERIFIED:
- the 2026 FOMC dates on the Fed's own page (search results only);
- whether a newer JPM LTCMA edition is out;
- how WInS treats the November iBond distributions;
- the exact 6 Nov freeze-day prices.

All odds and splits are MODEL figures from a simple parallel-shift pricer. They are good enough to show direction and size, not for quoting to the cent.
