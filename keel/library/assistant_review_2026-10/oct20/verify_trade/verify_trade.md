# Verification of the pre-trade check pack (oct20/tradecheck/trade_check_pack.md)

**AI-generated verification (Claude Code) for Team Caplet, Tue 20 Oct 2026 (run 19 Oct 22:39-23:00 UTC = 09:39-10:00 Sydney).**
It is not a trade instruction and drafts no trade note, TNA, IPS or Final Report text. Only Ray places orders, and only after a
logged vote. If the team uses this, log it in the AI-use record. It contains no surnames, emails, birthdays or WInS username.

Folder: `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/verify_trade/` (`V/` below).
I used my own code only (`V/scripts/vol.py`, `vbond.py`, `vcards.py`, `vtime.py`, `h2t.py`) and my own fetches (`V/data/`, `V/web/`).
I did not import `tradecheck.py` or `indep_pricer.py`. I read only their input constants, for example the 7 Oct fill prices, which
are the same as `snap/main/COMPETITION.md:174-186`.

---

## 1. Verdict

**PASS WITH CORRECTIONS. No card breaks a Wharton or platform rule, but the pack's case for sizing T1b at 295 shares is wrong.**
- **Rules.** All 14 rule quotes (R1-R14) match the live pages word for word.
- **Arithmetic.** Every cash line reproduces to within $0.02 at the pack's own prices. With my own bond model it is within $20.
- **T0 (no trade)** is ready to use as written.
- **T1b is compliant, and its cash figures are right.** But its "mirrors the plan, same −1.2-point gap" argument rests on a
  double-counting error (E1).
  - The plan takes about 78% of the reserve from the floor and 22% from VT, never 100% from IBTM.
  - Selling 295 IBTM widens the IBTM gap to −1.7 points.
  - About **231 IBTM** keeps the gap at −1.2.
  - The team must choose 295 or 231 before the vote. Both are compliant and both keep more than $1,000 cash.
- **Smaller fixes.** There are 13 lower-severity corrections (E2-E14). None changes a PASS/FAIL result.

## 2. Error table (with exact fixes)

| # | Where in the pack | What is wrong (evidence) | Severity | Exact fix |
|---|---|---|---|---|
| E1 | §4 T1b (3) plan-ratio table; §3 summary row T1b; §0 item 1 | **"Plan with 3r" double-counts the reserve.** The pack takes the whole $10k off IBTM (31.55%) *and* $2.2k off VT (6.44%). That column adds up to only 99.5%. The 3r plan rows show something else (`oct20/charts/c5_plan_composition.csv`, 2 Jan 2028): the floor drops 117,807 → 109,953 (−$7,854, 78.5%) and VT drops 32,193 → 30,047 (−$2,146, 21.5%). So the correct plan-3r IBTM = (39,140 payment rung + 109,953) / 465,797 = **32.01%**, VT = **6.45%**, Nov-41 7.25%, leftover 0.64% (sums to 100.0%). After selling 295, IBTM is 30.32%, a gap of **−1.69** points, not "the same −1.2". | **Medium** (changes what the vote sizes; compliance unaffected) | Replace the IBTM row with "32.01% ((39,140 + 109,953) / 465,797)" and VT with "6.45% (30,047 / 465,797)". Replace "the same −1.2-point gap" with: "295 funds the whole scaled reserve ($6,440) from IBTM. The plan takes $5,058 from IBTM and $1,382 from VT (×0.644). An IBTM-only mirror sells **231** (IBTM 30.78%, gap −1.23 as today; cash after ≈ **$2,302** = 0.76%, nearer the plan's 0.64%). The exact two-leg mirror is T1e." In §0 item 1, delete "the version that mirrors the plan". |
| E2 | §1 R6, "How this pack applies it" | "Largest position after any card is IBTM at 30-33%; all bonds stay at 29-42%" is wrong for two cards. **T6 → IBTM 34.19%. T3 → all bonds 45.01%.** T4's largest position is IBTM at 12.1%. | Low (still far under 200% / 100%) | "Largest single position after any card: 12-34% (T6 highest, IBTM 34.2%). All bonds together: 28.9-45.0% (T3 highest)." Note that only T6 goes above the 32.5% that the 7 Oct fill proves indirectly. |
| E3 | §6 step 7, bond units | It says "the Sheet's R19 note says face dollars". In fact Portfolio R19's entry column reads **"Type into WInS (shares; bonds in $1,000 units)"** (value 20), which agrees with competition/COMPETITION.md:82. Face dollars appear in the "Target units" column (20000) and in the Trade Log header ("face value $ for bonds"). | Low | "competition/COMPETITION.md:82 and the Portfolio tab's 'Type into WInS' column say $1,000 units. The Trade Log and 'Target units' columns record face dollars. The preview total decides." Supporting fact: the 7-8 Oct fills reconcile to the $3,513.79 cash balance only with $1,000 units (my check: within $26, with rounded ETF fills). |
| E4 | §2 "Scale"; card T1c; §3 row T1c | It treats 0.667 as a live alternative ("Pick one"). Numbers register row H5 has already decided this: about 0.64 ($300k / plan value on 2 Jan 2028). 0.667 = 300/450 is the ratio of the deposits and "overstates the WInS ladder by about $7k". It says do not use 300/450 (`oct20/numreg/numbers_register.md:167`). | Low | Cite H5. Mark T1c "not valid (H5)". Sizing is robust anyway: 0.643/0.644/0.645 give 294/295/295 shares and 8 bonds. |
| E5 | §2 ETF prices | "These match Yahoo to the cent and the share count" is false. Nasdaq's IBTM volume of 160,242 includes after-hours trades; Yahoo shows 159,350. Nasdaq's official VT close is $157.12; Yahoo shows $157.11. | Trivial | "Match within 1 cent and 0.6% of volume." |
| E6 | §0 item 6; §8 bullet 4 | "page.py caches forever" is now out of date. `oct16/tools/page.py` was changed at 22:38 UTC and now expires its cache after 1 hour (line 9). | Low | "page.py now expires its cache after 1 h (since 19 Oct 22:38 UTC). For rules pages, still use plain curl with a cache-busting query." |
| E7 | §7 item 9 | `oct20/reconcile3r/reconcile_3r.md` now exists (22:45 UTC). I searched it for IBTM sale sizes and WInS orders and found no change to WInS order sizing. Its "top fix" is about the 2031 top, not the reserve's funding. `rematch1R` still has no .md. | Low | Update the item accordingly. |
| E8 | §4 T1b (5), bond check | **Two different thresholds.** "Pass if 76.0-77.5" works out to −2.6 to +14.7 bp around par. "Stop if more than 0.25 points from the curve" works out to 75.15-79.50 on the 19 Oct curve. That leaves a grey zone. Second issue: WInS bond prices "are updated once daily at U.S. market open" (FAQ:63; UG p.11). A pre-open check on Thu 29 Oct therefore shows a price set on Wed 28 Oct, which is **before the FOMC statement** (14:00 EDT, 28 Oct). | Low/process | One rule: **STOP** if the yield implied by WInS differs by more than 0.25 points from the treasury.gov par yield at 15.0 years, **taken from the curve of the last trading day before the WInS price was set**. Treat 76.0-77.5 as the "expected" range, not as the pass test. |
| E9 | §1 R12 | It cites only "adjusted ... as best it can" (PFAQ:46). The same FAQ also says an order can be "System Cancelled ... generally due to insufficient buying power" (PFAQ:85). An under-funded buy may be cut **or** cancelled. | Low | Add the PFAQ:85 quote. The sequencing rule stays the same. |
| E10 | §4 T0 (2) | "$3,513.79 = 1.16% ... within the 1.1% target": 1.16% is 0.06 points *above* the target. | Trivial | "About the 1.1% target." |
| E11 | §2 "Book value now" | "Whether WInS counts accrued interest is UNVERIFIED". UG p.11 says accrued interest paid "will then be accounted for on your account summary". | Low | "UG p.11 says accrued is shown in the account summary. Whether the portfolio value includes it is UNVERIFIED." |
| E12 | §1 R10 | "Notes cannot be edited, only added" is stated as fact (competition/COMPETITION.md:84). The team's own Session record says "Whether a saved note can be edited later is not confirmed. Treat the first note as final" (WInS Notes tab R17). | Low | Label it "assumed (not confirmed); treat as final". The conservative behaviour stays the same. |
| E13 | §4 T1b, T1e; T4 cash | Cent rounding: 295 × 21.865 = 6,450.175, so cash after T1b is **$3,701.61**. T1e is $3,647.51 and T4 is $8,520.61. | Trivial | Optional. |
| E14 | §0 item 4 and T1b (5) vs the §6 timing table | The fallback is listed as "Tue 3 / Wed 4 Nov" in two places, but the table also lists Mon 2 Nov. A sell-then-buy pair that starts Wed 4 Nov breaks the buffer, because the bond would go in on Thu 5 Nov, after the last entry. | Low | "Fallback pair: sale Mon 2 or Tue 3 Nov 22:00 Sydney, bond the next evening; nothing entered after Wed 4 Nov 22:00." |

## 3. Confirmed facts (checked independently)

**Rules (live fetch, plain curl with a cache-busting query, 19 Oct 22:39 UTC; `V/web/`).**
- **The three SMApply pages** (trading, faqs, wins) match the compliance desk's 21:59 UTC copies word for word; only whitespace
  differs. Every line the pack cites (TRD:26/29/35/42/43/46-48; FAQ:41/44/45/47/54-56/63/65/80; WP:25/45) says what the pack
  says.
  - Volume = "no more than twice a security's current daily trading volume".
  - Commission = "flat $25 commission and treasury bonds are charged $10 ... only on a trade that clears".
  - TIPS and STRIPS are banned (FAQ:54-55).
- **Stock-Trak portfolio FAQ** (https://edu.stocktrak.com/wharton/portfolio-faq/): every quote matches.
  - Day trading = "buy and sell the same stock on the same day" (PFAQ:128). It goes on: "Whether day trading is allowed is
    dependent on the tournament you are in."
  - Volume: "trade up to half of the volume" (PFAQ:94) and "must be double the amount you are attempting to trade" (PFAQ:102).
    An order over 50% "will remain pending" (PFAQ:51). It is held, not rejected.
  - Default position limit 25% (PFAQ:95).
  - "Adjusted ... as best it can" (PFAQ:47).
  - Restricted funds on closed-market market orders (PFAQ:107).
  - Bonds "executed at end of day prices" (PFAQ:137).
  - Open and cancelled orders do not count as trades (PFAQ:139).
- **2026-27 WInS User Guide PDF.** It has the same MD5 as the pack's copy (f43f05e3...).
  - p.6: "Position Limit: This is how much of your portfolio you can invest in one single stock." and "Day Trading: This is not
    permitted."
  - p.10: "Review Order", then the Trade Note, then "trying to buy fewer shares than have actually traded in the market today".
  - p.11: bond prices are updated at the open, and accrued interest is paid to the seller.
  - One text layer on p.11 mentions "approved lists ... HERE". It looks like old-year text. The live 2026-27 SMApply wording
    ("Any ETF available on WInS") governs. Which layer is visible: UNVERIFIED (I had no PDF renderer).
- **Session record** (WInS Notes tab, typed 29 Sep): day trading, margin and shorting "Not allowed"; position limit 200% per ETF
  and 100% for bonds; 300-character note box; $3 minimum price. The Portfolio tab repeats these at R14 and R15. A screenshot is
  still missing (UNVERIFIED).

**Market data.**
- **Yahoo** (own fetch, 22:41 UTC): 19 Oct closes and volumes, plus the lowest and median volume of the last 21 sessions
  (21 Sep-19 Oct), match the pack's table exactly:
  - IBTM 21.865 / 159,350 / low 85,700 / median 268,100;
  - IBTO 66,600 low; IBTP 51,000; IBTQ 45,200; IBTR 17,000;
  - VT 157.11 / low 1,167,700.
- **Nasdaq historical API** (own fetch) agrees day by day to Yahoo's rounding, for example 21 Sep IBTM 85,726. Its 19 Oct row is
  not published yet.
- **Treasury curve.** The treasury.gov par curve for 19 Oct is the latest row: 10y 5.15, 20y 5.53, 30y 5.48. The 20 Oct curve is
  not published; it is only 20:40 EDT on 19 Oct.

**Bond model** (own bootstrap, 30 Oct settlement, 19 Oct curve; `V/data/vbond_out.json`).
- **Nov-2041:**
  - Model clean 77.008 (pack 76.967).
  - Gap at the 7 Oct fill −0.559 (pack −0.552), so the WInS estimate is **76.450** (pack 76.415).
  - Accrued **1.4266** (168/184 days × 1.5625), the same as the pack.
  - Model YTM 5.372% (pack 5.377%); WInS-est YTM 5.437% (pack 5.441%).
  - Par at maturity **5.342%** (same).
  - Cost per unit $778.76 (pack $778.42); $0.863 per unit per bp (pack $0.87).
  - At a 20 Oct settlement: 76.970 / 1.3417, against the numbers desk's 76.965 / 1.342.
- **Other bonds:** accrued interest matches to 0.001 (0.981 / 2.054 / 1.997 / 1.940). Par at maturity matches. Model prices
  differ by ≤ 0.05.
- **Yield-check table:** all 12 points match the pack to 0.001 (for example 76.00 → 5.489, 77.50 → 5.316, 78.00 → 5.260).
- **Caveat:** if the 7 Oct WInS fill used a price set from the 6 Oct close, the Nov-41 gap is −0.75, not −0.56. That is about
  $13 on 8 bonds.
- **Instrument check:** CUSIP 912810QT8 is a nominal 3.125% Treasury bond maturing 15 Nov 2041. TreasuryDirect shows
  securityType "Bond" and no TIPS flag (`V/data/td_912810QT8.json`).

**Cash, fees, counts, volume and positions** (`V/data/vcards_out.json`).
- **Cash.** All cards reproduce at the pack's unit costs:
  - T1a: $531.18 and $93.88;
  - T1b: $3,701.61; at the model price $3,657.44; under the stress case $3,581.61;
  - T1c: $3,513.54; T1e: $3,647.51; T2: $1,168.53 and $390.11;
  - T3: $1,898.07; T4: $8,520.61; T5: $3,629.56; T6: $3,514.20.
- **Fees and trade counts:** $35 / 13, $60 / 14, $10 / 12, $175 / 21, $200 / 22, $50 / 13. All correct.
- **Smallest IBTM sale that keeps $1,000** with 8 bonds: **172** (WInS-est.) to **174** (model). Correct.
- **Sizing:** $10,000 × 0.644 = $6,440.57. That is 294.5 IBTM shares, so 295, and 8.27 bonds, so 8. Correct.
- **Volume:** largest is 3.29% of the 21-session low (T4, IBTM 2,820). T1b is 0.34% of the low and 0.19% of 19 Oct volume.
  Correct.
- **Weights after T1b:** IBTM 30.32%, Nov-41 7.18%, VT 8.65%, cash 1.22%, all bonds 30.93%. Correct.
- **Starting book:** IBTM 32.44%, Nov-41 5.13%, VT 8.65%, cash 1.16%, total ≈ $303.5k. Correct.

**Time conversions** (zoneinfo America/New_York and Australia/Sydney; `V/scripts/vtime.py`). Every row of the §6 table is
correct.
- **Clock changes:** Sydney moved to AEDT on Sun 4 Oct, 03:00 local. The US goes to EST on Sun 1 Nov, 02:00 → 01:00. The gap is
  14 h before 4 Oct, 15 h from 4 Oct to 31 Oct, and 16 h from 1 Nov.
- **FOMC:** the meeting is 27-28 Oct (federalreserve.gov calendar, read 19 Oct 22:45 UTC). Statements are released at 2:00 p.m.
  ET; the 16 Sep 2026 release says "For release at 2:00 p.m. EDT". 28 Oct 14:00 EDT = **Thu 29 Oct 05:00 Sydney**. The October
  release time itself is the Fed's standard practice, not yet published (UNVERIFIED).
- **Deadlines:** TNA 23 Oct 17:00 EDT = Sat 24 Oct 08:00. Freeze 6 Nov 16:00 EST = Sat 7 Nov 08:00. IPS deadline Sat 7 Nov 09:00.
  Final Report 4 Dec 17:00 EST = Sat 5 Dec 09:00.
- **The pack's competition/COMPETITION.md:13 fix** ("14 to 16" should be "15 to 16") is right.

**Filed notes** (`/home/user/snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`).
- Every note quote and line reference in the pack is exact:
  - VT ":14" ("They only set how far her gift rises above her promised minimum", "A fall can shrink the extra");
  - IBTR ":15";
  - Feb-2037 ID B-T-4.750-15022037 ":16";
  - Nov-2039 ":18" ("reinvested coupons fund the rest");
  - IBTM ":19" ("does two jobs", 10/06 10:01:41 PM);
  - IBTO ":20";
  - Nov-2040 ":23" ("consistent with the Treasury yield curve");
  - Nov-2041 ":24" (B-T-3.125-15112041, 10/06 07:55:45 PM).
- 11 filled notes = 11 trades used.
- The TNA picks are IBTM, IBTR and VT (lines 28-30).
- The TNA rule "exactly as it appears in WInS" is `2026_WGY_Trading_Notes_Analysis-FINAL.txt:44`.
- competition/COMPETITION.md:181 says 5.000% for Feb-2037. That is wrong; it is 4.750% (the pack's correction holds).

**Sheet** (`oct19/drive/sheets/portfolio.md`, export of 17 Oct).
- R31 "Keep at least $1,000". R13 cash target 0.011. R14 position limit 2.0 ("200% stocks/ETFs; 100% bonds"). R15 note limit 300.
- R38-39 IBTM split 1,142 / 3,361. After T1b: 3,066 floor shares. With 231 sold: 3,130.
- H20 uses FLOOR, so it rounds down.
- H7 "Trades outside the plan" uses COUNTIF on the names in the Trade Log, so exact names matter.
- R&B Tickets R7 is $1,000; R14 IBTM name SEEN 29 Sep; R15 CUSIP 912810QT8.
- **The Trade Log tab is still empty** (R2-R23 blank), so Portfolio B7/C7 still show $300,000, not the live book.

**Content and privacy checks.**
- **No drafted trade-note text.** §4 and §5 are checklists of facts to cover. Two T1b bullets ("Its new job: ...", "Why this
  holding ...") are close to sentences. Keep them as points; students choose all wording.
- **No personal data.** A scan against `oct16/tools/.pii_tokens` (tokens not printed) found **0 hits** in the pack,
  `tradecheck_out.json` and `tradecheck.py`. No emails. The only first name used is Ray.

## 4. Still UNVERIFIED
1. A Session Rules screenshot (position limit, day-trading line).
2. The live WInS Nov-41 price, accrued interest and last coupon date.
3. The WInS volume rule for bonds.
4. Whether an under-funded order is shrunk or System Cancelled.
5. Whether a pre-open Day limit order stays live for that session, and which order types bonds allow.
6. "Required trading activity" (FAQ:80).
7. Which User Guide p.11 text layer is visible.
8. The October FOMC release time (standard practice is 2:00 p.m. ET).

---

## 5. Go/no-go card (one page): T0 and T1b, with the corrected numbers

**Common gate (both):**
- A logged team vote with a DL-ID.
- A Session Rules screenshot, with the username cropped.
- No open orders in Order History.
- "Required trading activity" (FAQ:80) is undefined. Never trade just to meet it.

**T0: No trade. GO as written.**
- **State now:** cash $3,513.79 (1.16% of about $303.5k); 11 of 200 trades used; IBTM 32.4%, VT 8.65%, all bonds 28.9%.
- **Rules:** nothing to enter. Holding is allowed: the WInS page says teams are not evaluated on "How many trades you make".
- **Record:** a decision-log entry (date, option, alternatives rejected, reason, dissent by role) and the freeze-day saves:
  WInS screenshots before and after Fri 6 Nov 16:00 EST (Sat 7 Nov 08:00 Sydney).
- **Words:**
  - Under 3r-A, say "about mirrors". The reserve is about $6.4k (2.1% of the book) and sits inside IBTM.
  - Under option 2, fix the conflict with the VT note's "only" in words, never by adding a note.
  - Add **no** note to the IBTM, IBTR or VT orders before the TNA is in (23 Oct 17:00 EDT = Sat 24 Oct 08:00 Sydney).

**T1b: 3r option B. GO only if all of the checks below pass. Compliant either way.**

*Decide the size before the vote:*
- **295 shares** puts the whole scaled reserve on IBTM.
- **231 shares** is the IBTM share of the plan.

| | Sell 295 IBTM (pack) | Sell 231 IBTM (IBTM-leg mirror) |
|---|---|---|
| Order 1: SELL IBTM, Day limit about 0.3% under the last close (e.g. $21.80 on $21.865) | gross $6,450.18, −$25 | gross $5,050.82, −$25 |
| Cash after order 1 | $9,938.97 | $8,539.61 |
| Order 2 (next evening, after "Filled"): BUY **8** units (= $8,000 face) of 3.125% 15-Nov-2041 | preview ≈ $6,237 incl. accrued + $10 | same |
| Cash after (WInS est. / model / at the 79.50 stop edge) | **$3,702** / $3,657 / $3,455 | **$2,302** / $2,258 / $2,055 |
| IBTM / Nov-41 / VT / cash after | 30.32% / 7.18% / 8.65% / 1.22% | 30.78% / 7.18% / 8.65% / 0.76% |
| Against plan-3r (×0.644): 32.01% / 7.25% / 6.45% / 0.64% | IBTM gap −1.69 (today −1.25) | IBTM gap −1.23 (unchanged) |
| Fees / trades used | $35 / 13 of 200 | $35 / 13 of 200 |
| Volume (vs the 85,700 low; vs 19 Oct) | 0.34% / 0.19% | 0.27% / 0.14% |

- **Floor for the house rule:** at least 172-174 IBTM must be sold to end with $1,000 or more.
- **T1e** (229 IBTM + 9 VT, $60, 14 trades, cash $3,648) is the only exact mirror on every line. It needs a third note.

*Rules:*
- **R1 instrument:** CUSIP 912810QT8 is a nominal bond, not TIPS or STRIPS. IBTM is held.
- **R3 volume:** under 50%.
- **R5 day trading:** different securities on different days. Never buy IBTM back on the sale day.
- **R6 position limit:** 30-31% against a 200% ETF limit and 100% for bonds (session record).
- **R7 trades:** 13 of 200.
- **R9 shorting:** choose "Sell", not "Short"; 295 or 231 is at most 4,503 held.
- **R12 buying power:** buy only once cash ≥ preview total + $1,000 (about $7,240).

*Bond STOP checks:* stop the evening's order if any one fails. Check the bond before selling IBTM.
1. **Name.** Coupon 3.125% (not the 2.000% of the same date), maturity 15 Nov 2041, last coupon 15 May 2026. Accrued about
   $14.3 per unit at 30 Oct ($14.5 if it settles 2 Nov).
2. **Yield.** Yield implied by the WInS clean price minus the treasury.gov par yield at 15.0 years, from the curve of the
   trading day before the WInS price update, is no more than 0.25 points either way. On the 19 Oct curve: par 5.342%, so stop
   below 75.15 or above 79.50. Expected 76.0-77.5 (5.49-5.32%).
3. **Preview total** within ±$100 of the ticket. Clean 76.0-77.5 gives $6,204-$6,324. Commission shows $10. Quantity 8, not
   8,000.

*Timing* (Sydney = ET + 15 h until Sat 31 Oct; ET + 16 h from Sun 1 Nov):

| Sydney | ET | Step |
|---|---|---|
| Thu 29 Oct 20:00 | 05:00 EDT | M6 go/no-go and post-FOMC re-price (FOMC statement Thu 05:00 Sydney) |
| **Thu 29 Oct 22:00** | 07:00 EDT | Enter the sale. Fills at the 09:30 EDT open = Fri 00:30 Sydney |
| Fri 30 Oct, after 07:00 | after the 16:00 EDT close | Check "Filled" and cash |
| **Fri 30 Oct 22:00** | 07:00 EDT | Enter the bond (end-of-day price). Check Sat 31 Oct after 07:00 |
| Mon 2 or Tue 3 Nov 22:00, then the next evening | 06:00 EST | Fallback pair (sale, then bond) |
| Wed 4 Nov 22:00 | 06:00 EST | Last entry of anything |
| Sat 7 Nov 08:00 | Fri 6 Nov 16:00 EST | Freeze |

*NO-GO if any of these:*
- no DL-ID;
- no Session Rules screenshot;
- the bond fails a STOP check;
- the sale has not filled;
- an open order exists;
- cash < buy total + $1,000;
- the two notes are not final, student-written and at most 300 characters (counted by a second student);
- after 4 Nov 22:00 Sydney.

---

## 6. Reproduce
- **Volumes:** `venv/bin/python -I V/scripts/vol.py V/data` (Yahoo JSON in `V/data/yahoo/`, Nasdaq in `V/data/nasdaq/`).
- **Bonds:** `venv/bin/python -I V/scripts/vbond.py V/data/tsy_202610.csv V/data/vbond_out.json`.
- **Cards:** `venv/bin/python -I V/scripts/vcards.py V/data`. Time conversions: `V/scripts/vtime.py`.
- **Rules text:** `V/web/*.txt`, made from `*.html` and `ug.pdf` by `V/scripts/h2t.py` and pypdf.

## 7. What this teaches (for Ray)
- A trade can obey every rule and still be the wrong size. The rules check (here: all PASS) and the "does it match our plan"
  check are two different tests.
- When a number is "taken off" one holding, check that the table still adds up to 100%. Here it added up to 99.5%, which is how
  the double count showed itself.
