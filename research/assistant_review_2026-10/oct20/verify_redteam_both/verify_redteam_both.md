# verify_redteam_both: adversarial check of the BOTH red team

AI-generated verification by Claude Code for Team Caplet, Tue 20 Oct 2026 (Sydney), for the 27 Oct vote. Every number here is MODEL output from AI-written code. None of it is text to submit. If the team uses any of it, log it in the AI-use record now and in the Final Report's Works Cited later. No personal data appears (scan below).

**Paths.** `S/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`. **File under test (RB)** = `S/oct20/redteam_both/redteam_both.md`. **My folder** = `S/oct20/verify_redteam_both/`. Its `scripts/` holds unchanged copies of RB's `attack.py`, `common.py`, `engine_v3.py` (patched) and `engine_v3_orig.py`, so that nothing was written into RB's folder. My run is `data/attack_N20000_s424242.txt` and `.json`. E3, VE3, VRM, VP, VV2, R1R, BO, Notes, case and IPS have the same meanings as in RB:5.

## 0. Verdict: SOUND, with fixes. The substance holds; the citations and two summary sentences do not.

1. **Haircut attack: reproduces.** Seed 424242 (20,000 paths) gives 0.205% short for BOTH at a 0.1% miss (inside RB's 0.17-0.24%). At a 1% miss it gives 7.16% for BOTH against 6.01% for 3r-fix, a little outside RB's two-seed bands (6.7-6.8% / 5.7-5.9%). The direction and the gap (BOTH about 1 point more often, by smaller amounts) hold on all three seeds. The haircut is applied once, to the same four payment windows and by the same dollar amount in both options, and only after sizing. There is no double count.
2. **Circularity: confirmed.** The 2033 sizing and the post-2033 payments both use `hold_windows` on the same holdings, with the same coupons and face amounts. The realised side can only add cash (T-bills and the funds' bill stretch, floored at 0%), plus rounding up to $1,000 face.
3. **Instrument attack: reproduces.** Using only held bonds, BOTH is 0% short. Its median re-match cost is $8.7k and its 1-in-20 cost is $25.7k (seed 424242). It buys Nov-41 in 85% of paths and Nov-40 in 49%.
4. **Two summary sentences are wrong.** The first is "about half the worst case at every level"; it is true only at a 1% miss. The second is the IPS word estimate for BOTH, which does not match RB's own element table.
5. **Citations.** About 20 E3 and R1R line references are 2 lines short. All of them point to the right content two lines lower. A few VE3 and engine lines are off by 1-3. The case, IPS and Notes citations are correct.
6. **Labelling and banned items: clean.** The AI lean is labelled and the recommendations are labelled AI opinion. There is no deliverable prose and none of the six banned phrasings. The personal-data scan found 0 hits in RB, its script and its outputs (2 tokens, not printed).

## 1. Error table

| # | Location (RB) | Claim | Evidence | Severity | Exact fix |
|---|---|---|---|---|---|
| 1 | §0 item 4 (line 16); §5c table, 1.00% row (line 150) | "6.7-6.8% against 5.7-5.9%" | Seed 424242: BOTH **7.16%**, worst $2.08k; 3r-fix **6.005%**, worst $4.72k (`data/attack_N20000_s424242.txt`). At 20k paths and about 7%, one standard error is about 0.18 points, so a two-seed band is too narrow | Low | "about 7% against about 6% (three seeds: 6.7-7.2% against 5.7-6.0%); BOTH is short about 1 point more often, by about half as much at worst". Add seed 424242 to §5c and §11 |
| 2 | §5c "What it shows", bullet 2 (line 154) | "BOTH's shortfalls stay smaller than 3r's: about half the worst case at every level" | Worst BOTH / worst 3r-fix over three seeds: 0.1% miss $238-292 / $2.20-2.92k (about **1/10**); 0.25% $538-592 / $2.50-3.23k (about 1/5); 0.5% $1.04-1.09k / $3.03-3.72k (about 1/3); 1% $2.04-2.09k / $4.10-4.72k (0.44-0.51) | Low-Medium (it understates BOTH's advantage at small misses) | "BOTH's worst cases stay smaller than 3r-fix's: about a tenth at a 0.1% miss, rising to about half at a 1% miss" |
| 3 | E3 citations throughout | Line numbers | Each cited E3 line is 2 above the content: BOTH row :283 (not :281, lines 12, 60); robustness rows :291-294 (not :289-292, lines 11, 32, 177); bill-interest sensitivity :296 and its bullet :301 (not :294, :299, lines 59, 131); F9 yield floor :178 (not :176, line 122); BOTH definition :144 (not :142, line 136); 3r $15k :201 and :218 (not :199, :216, line 213); dust row :282 (not :280, line 134); model family :348-352 (not :346-350, line 246); one bond per fund :368 (not :366, line 137) | Medium (about 15 references fail to trace) | Add 2 to every E3 line number. For "Never ran dry" (line 136), cite R1R:146 and BO:3: E3:144 defines the chain but does not say it never ran dry |
| 4 | R1R citations | Line numbers | Each is 2 short: chain runs dry :146 (not :144, line 123); bid-ask $40 :173 (not :171, line 133); WInS needs nothing beyond 3r :195 (not :193, line 108); who does it in 2033 :197 (not :195, line 139); C4 two-stage certainty :207 (not :205, line 79); "Do not claim … zero risk" :222-223 (not :221, a blank line, line 161) | Medium | Replace with the corrected numbers |
| 5 | VE3 citations, lines 59, 123, 131, 133 | Line numbers | 1.93% at 20k paths is VE3:**18** (not :21); the +$22 no-cost result is VE3:**19** (not :20); the chain-order check is VE3:**17** (VE3:20 is the lump convention, cited at line 123 for "short only if the chain cannot pay") | Low | VE3:18; VE3:19; VE3:17 plus R1R:146 |
| 6 | Engine and kit citations, lines 53, 134, 70 | `engine_v3.py:164-169` (carry equalities); `:553-554` (rounding); `ips_writing_kit.md:55-56` | The carry equalities are at :167-172 (the `Aeq[j, K+j]` lines are 170-172). Rounding to $1,000 face with the dust rule is :552 (the cost is :553). The kit's 470 target is at :56 (:55 is the pitch) | Low | `engine_v3.py:167-172`; `:552-553`; `ips_writing_kit.md:56` |
| 7 | §3 table, BOTH row (line 79); §0 item 6 (line 19) | "+10-20 words over 3r's principle (about 40-50 in all); +25-35 with C4" | **Element count.** 3r's principle = 2 elements (R1, R2; VP:333, about 30 words). Full 3r = 5 elements (R1-R5), 50-70 words (VP:333; `S/oct20/redteam3r/redteam_3r.md:199`). RB lists 5 elements for BOTH (R1, R2, R4, R3', R5'), plus optional C4. VP:337 says BOTH's one new rule (R3') carries **four points** by itself. So, as tabled, BOTH has 3 more elements than 3r's principle and about as many as full 3r | Medium-Low (word cost understated; it feeds the "close to cheap" headline) | "BOTH has 3 more elements than 3r's principle, and the same number as full 3r (5; 6 with C4). The minimal form (R1, R2, R3') has 3 elements, one of which carries four points. AI estimate: +15-30 words over the principle for the minimal form; about the same as full 3r (50-70) as tabled; C4 adds about 10-15." State that +10-20 holds only if R4 and R5' stay out of the IPS |
| 8 | §3 Budget (line 70) | "The IPS bans citations and calculations" | IPS:123 bans "formal citations". It does not ban calculations: IPS:51-52 says to focus on the framework "rather than … presenting detailed financial calculations", and IPS:68-70 says final calculations are "not expected" | Low | "The IPS bans formal citations (IPS:123) and asks for the decision framework rather than detailed calculations (IPS:51-52, :68-70)" |
| 9 | §1 table, 10b column, twisted-bootstrap row (line 32) | "stock form 1.0%, worst $23k (VV2:46)" | VV2:46 gives only the $23.3k. The 1.0% is `S/oct20/engine_v3/data/boot_19oct_seed20261021.txt:2` (1.009%, $23.3k) and `boot_19oct_seed8.txt:2` (1.050%, $18.1k) | Low | "stock form 1.0-1.05%, worst $18-23k (engine_v3/data/boot_19oct_seed*.txt:2; VV2:46)" |
| 10 | §1 table, 10b column, money rows (lines 35-36) | 2033 "$0 / $0" and 2042 "$56.3k" under the column headed with the VREC reading (1.6%) | These are option 2 (stock form) figures, VP:123-124. On the VREC reading, Laura's 2042 median is $60.3k (VE3:72) | Low | Label both cells "stock form", or add "VREC reading: $60.3k in 2042 (VE3:72)" |
| 11 | §4 table, IBTO-IBTQ row (line 106); §5b (line 137) | "'Its payout is not fixed' (three notes)"; "'payout not fixed' (Notes:19-22)" | IBTO's note reads "Its December payout is not fixed" (Notes:20). IBTP and IBTQ read "Its payout is not fixed" (Notes:21-22). IBTM reads "the final payout is not fixed" (Notes:19). No note says "payout not fixed" | Low | Quote exactly: "Its payout is not fixed" (Notes:21-22), "Its December payout is not fixed" (Notes:20). In §5b write "payout is not fixed" |
| 12 | §4 table, reinvested-coupons row (line 105) | Lists only Nov-39 and Nov-41 | Nov-40 (Notes:23): "A lower-coupon bond would reduce reliance on reinvested coupons, but WInS lists none for that date". It is the same soft tension, on a bond BOTH buys more of in about half of all paths | Low | Add Nov-40 (Notes:23) to that row |
| 13 | §4 table, IBTM row (line 103) | "'payout not fixed' is the very risk BOTH's 0% ignores (section 5c)" | §5c stresses IBTO-IBTR only. IBTM (the 2033 payment and the floor) was not stressed, and its payout risk falls on every option alike | Low | "IBTM's own payout risk was not stressed. §5c stresses the same caveat as filed for IBTO-IBTQ (Notes:20-22)" |
| 14 | §0 items 6-7 (lines 19-20); §3(c) (line 88) | "As an IPS element it is a real rule"; "not simpler to defend"; "Of all the options it is the most IPS-native answer" | These are judgements, but they are not tagged. RB:3 promises that every opinion is labelled "AI view" | Low | Prefix each with "AI view:" |
| 15 | §4 (line 97) | "Notes cannot be edited (VP:19)" | VP:19 says "assumed, not confirmed". The verified source is the WInS rules entry in `/home/user/caplet-investment/CLAUDE.md` (Key facts: "trade notes cannot be edited, only added to") | Low | Cite CLAUDE.md Key facts instead of VP:19 |
| 16 | §1 heading (line 27) | "one basis: … 100,000 paths" | BOTH 73.0% and 3r-fix 75.4% (units book) are 20,000-path runs (VE3:21-23, :49), and so is the whole §5c attack | Low | Add "(20k paths)" to those cells |

## 2. What holds

- **Check 1 (haircut).** Three seeds, 20,000 paths each, v3 basis, 19 Oct curve:

  | Miss per fund | BOTH short (s20261019 / s7 / s424242) | 3r-fix short |
  |---|---|---|
  | 0.1% (about $50) | 0.170 / 0.235 / 0.205% | 1.925 / 1.955 / 1.920% |
  | 1.0% (about $500) | 6.80 / 6.73 / 7.16% | 5.86 / 5.71 / 6.005% |

  - **The patch is fair.** `diff engine_v3_orig.py engine_v3.py` shows only the two switches plus the cache key. `engine_v3_orig.py` is byte-identical to `S/oct20/engine_v3/scripts/engine_v3.py` (same md5).
  - **The windows match.** BOTH subtracts `h × $50,000` from `Wr[0:4]` once, after the instrument loop (patched lines 691-692, outside the loop at the same indent as the `for`). 3r subtracts the same amount from `D_real[j]` for j = 1-4 (patched line 728). Both are the 2034-37 windows funded by IBTO-IBTR, whose maturities are Dec 2033 to Dec 2036 (`engine_v3.py:114-116`).
  - **Sizing never sees the haircut.** The LP is cached before it, and the cache key has no haircut term.
  - **No double count.** At a 1% miss, Laura's 2042 median falls by $2.67k for BOTH and $2.48k for 3r. That is $2,000 of nominal misses grown at T-bills to 2042, so the haircut was applied once.

- **Check 2 (circularity).**
  - **Sizing.** `bo_cost` (`engine_v3.py:545-555`) sizes on `held(72, wait_real=False)`, with fund bills off, plus `hold_windows(b, J33, 100, c, frozen month-72 shock)`.
  - **Payment.** The loop (`:680-691`) pays from `held(None, wait_real=bill)` plus `hold_windows(b, J33, face_bo, cps_bo, …)`: the same coupons and faces.
  - **Pre-2033 flows are identical.** Freezing at month 72 does not change them (`_shockf`, `:227-229`).
  - **Post-2033 cash can only be larger.** Bill growth is `grow(max(r − fee, 0))` ≥ 1 with `yfloor` = 0 (`:89-91`; DEFAULT `:840`), and face is rounded up.
  - **Residuals.** The only remaining shortfalls are dust (each instrument under $100 is dropped, `:552`; worst $38-92) and an uncovered 2033 bill. RB §5a is right.

- **Check 3 (instruments).** Held bonds only: 0% short on all three seeds.

  | | Seed 20261019 | Seed 7 | Seed 424242 |
  |---|---|---|---|
  | Median cost | $8.5k | $8.4k | $8.7k |
  | 1-in-20 cost | $25.8k | $25.6k | $25.7k |

  Nov-41 is bought in 85% of paths and Nov-40 in 48-49%; Feb-37 or Nov-39 in about 1%. VRM:114-135 confirms that the bonds exist and that the 2033-35 notes are not WInS-listed.

- **Check 5 (filed notes, quoted exactly).**
  - Nov-39 (Notes:18): "Held to maturity, its fixed coupons and principal cover most of it; reinvested coupons fund the rest."
  - Nov-41 (Notes:24): "the last five payments use individual Treasuries, scaled to the model portfolio, with reinvested coupons funding part of each."
  - IBTR (Notes:15): "If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility."
  - Feb-37 (Notes:16): "The 10.5-month gap creates reinvestment-rate risk on the proceeds held in a short-term Treasury ETF."
  - VT (Notes:14): "They only set how far her gift rises above her promised minimum."
  - **RB's readings are fair.** IBTR and Feb-37 are consistent with BOTH. The reinvested-coupon notes describe the plan at purchase, and BOTH still uses reinvestment before 2033 (`hold_windows`, `:312-315`), so the tension is only after 2033. 10b strains the VT note's "only".

- **Check 6 (D10).** Option 1 on call (VREC reading) is 1.59% (1.56%) short, worst $6.8k ($7.1k) (VE3:72). The stock form is 0.82%, worst $12.2k (VE3:73; VP:122), and $23.3k on the twisted bootstrap (seed 20261021; $18.1k on seed 8).

- **Check 7 (case and IPS citations).**
  - case:95-97: "explain how its composition should change, if at all" (:96-97).
  - case:91-92, :97-99, :102-103, :114-120 and :145 are all correct.
  - IPS:47: "planned changes in the portfolio as future funding needs approach". IPS:48-49: "managing the operating reserve's asset composition over time" (it starts at the end of :48).
  - IPS:22-23, :39, :109, :51-52 and :68-70 are correct.
  - IPS:73-74 is exact: "Your team may not revise its investment strategy after the submission deadline."
  - The VP, VRM, VV2, BO, V5 and Notes lines all trace, apart from the items in the table.

- **Check 8 (labels).** The AI lean (RB:230, "AI lean (labelled, weak)"), §9 ("AI opinion; the team decides") and the AI views at lines 64, 90, 183, 191, 198 and 227-228 are all labelled. The only gap is #14.

- **Check 9 (prose and banned items).** There are no drafted IPS, TNA or Final Report sentences: deliverable content is named as elements. The phrases in §5d are quoting rules, not prose. Each of the six banned phrasings listed in the coordinator brief appears 0 times (fixed-string grep; not repeated here). "0%", "zero risk" and "in every run" appear only inside "never quote" warnings.

- **Not tested by RB, and not a defect.** No run stresses an IBTM payout miss. It would hit the 2033 payment and the floor under every option, not BOTH alone.

## 3. AI view: bottom line for the vote (a summary of evidence, not text to submit)

AI view. On the evidence, BOTH and 3r-fix give Laura almost the same results. They have the same $135k median minimum, the same median gift and a top-reach of about three in four, and her money in total is about $2.5k lower under BOTH. BOTH's one measured gain is that interest rates after 2033 stop mattering for the payments: about 0.6% of model paths are short under 3r-fix (more with curve twists), against none under BOTH. That "none" holds by construction, however, because the model pays from the same cash flows it sized. It breaks as soon as something the model does not see goes wrong. If the four iBond funds paid out even 1% less than modelled, BOTH would be short about 7% of the time against about 6% for 3r-fix, though by about half as much at worst. BOTH also needs only bonds the team already holds, and roughly as many IPS elements as the full 3r rule. So the choice is less about money than about which question the team can answer in its own words: "why a $5k margin?" for 3r-fix, or "why size cash at 0%, and what is left uncovered?" for BOTH. Option 1 with Laura's half on call is simpler to hold. Its bad cases come with stock crashes, though, and it ties up her flexibility money to 2042. The team decides.
