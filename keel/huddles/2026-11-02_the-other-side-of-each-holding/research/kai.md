# Kai's flaw hunt (H-015 round 2, Mon 2 Nov 2026; Opus 5.5) (Keel is a simulated team, AI-written.)

Text under test: `../../../ips_rewrite/drafts/D32/ips_V52.txt` (**496 strict** today by `keel/office/tools/textcheck.py`;
the README says 497; the team's cap is 497) and `pitch.txt` (no pitch rewrite offered: the rewrite thread owns it).
Paragraphs P1-P10 as in Felix's notes (P10 = "Do not crush."). Verdicts attacked: every TRUE and TRUE IF the three
scouts gave (Tess, Nora, Felix, round 1), plus Tess's two FALSEs and Nora's FALSE-against-the-book. The Window's
read (`origin/claude/project-thread-apbvb2:keel/ips_rewrite/inbox/2026-11-02_window.md`) is cited where it disagrees.
Rules applied: `../../../WHARTON_WORD.md` first; BIBLE Book 11 (no model numbers, no "our model", no team history, no
subheadings in any offered IPS line); standing calls not relitigated (Caplet XR, X = ten, R = redemption; the iBond
funds may be "near-ironclad"; a word is wrong only if it is false). Every offered wording is **AI DRAFT (Claude,
2 Nov 2026)**. Strict counts are `printf '%s' "..." | python3 keel/office/tools/textcheck.py -`, larger count quoted.
New fetches are marked **NEW**; lines re-checked by the chair this morning are marked (re-checked); anything else
from round 1 that I did not fetch is the scout's, as they fetched it.

| # | V52 sentence | Scout's verdict | Kai's verdict | Why, with the source line | Cheapest true sentence, strict cost |
|---|---|---|---|---|---|
| 1 | Pitch: "Her first $300,000 buys Treasuries that each mature before a January." | Tess TRUE IF ("Treasuries" takes in the funds); Nora TRUE IF (and FALSE read as the book) | **UPHELD** (TRUE IF) | Umbrella use: nothing earlier on the page splits bonds from funds, and P3 opens the umbrella ("Treasury bonds and funds that mature like bonds"). Funds: "will terminate on or about December 15" (U18, Tess); T-bonds Feb-2037 to Nov-2041 (snapshot). Case :129-130: the WInS book "does not determine Laura's actual portfolio value at the beginning of 2027", so "read as the book" is not the reading. Still a one-close call on cost (Window). | None offered (pitch is the thread's) |
| 2 | Pitch: "Her 2028 deposit buys a Treasury floor for her building gift" | Tess: same as P5 (FALSE) | **OVERTURNED** (TRUE) | "Treasury" is an adjective here: a floor made of Treasuries. IBTM's index is "composed of U.S. Treasury bonds maturing in 2032" (U10; the chair re-checked five U10 lines). P5's slip is the noun "Treasuries" for one fund, after P3 split the two; the pitch has no such split | Keep; 0 |
| 3 | P2: "To a pharmacist, XR means extended release" | Felix TRUE | **UPHELD** | WA Health poster: "XR" / "Extended release" / "Diabex XR (metformin)" (re-checked x3). The Australian family word is "modified release" (TGA), but the letters still read "extended" | Keep; 0 |
| 4 | P2: "a caplet that delivers its dose on schedule, labelled do not crush" | Felix TRUE | **UPHELD, evidence narrowed** | Felix's Australian line is a leaflet (CMI), not a label: "Do not suck, crush or chew the caplets because that may affect its sustained release properties." (re-checked). The label proof is the Window's US one, TYLENOL 8 HR: "Swallow whole; do not crush, chew, split, or dissolve" (W-07; not fetched by me, UNVERIFIED here). V52 never says which caplet, so either holds | Keep; 0 |
| 5 | P2: "Crush it and the schedule is gone." | Felix TRUE | **UPHELD, on a better source** | Felix stood "gone" on two sources that don't say it: "may affect" (CMI) and "the duration of the drug's activity is reduced" (Aust Prescr). **NEW**, CMAJ 2005 (Cornish): "the sustained-release formulation is designed to deliver the drug gradually over 12 hours." and "Crushing the tablet destroyed the drug's sustained-release properties". Destroyed release = no schedule. Strong true word stays (VOICE, Book 5) | Keep; 0 |
| 6 | P2: "To us, X is ten and R is redemption – ten holdings, one redeemed for each January." | Tess TRUE IF ("redeemed" means "paid out"; holders don't redeem, the funds distribute); Window TRUE | **OVERTURNED** (TRUE, no condition) | Tess's two lines are about the fund's working life, not its end: U1 "Shares of ETFs are bought and sold at market price (not NAV) and are not individually redeemed from the fund." and U8 "Except when aggregated in Creation Units, shares of each Fund are not redeemable." At the end, iShares' own SEC notice for an iBonds Treasury fund, **NEW**: "If you still hold shares of the Fund on December 19, 2024, the Fund will automatically redeem your shares for cash" (IBTE supplement, 17 Oct 2024). T-bonds, **NEW**, TreasuryDirect: "Redeeming – Getting Your Money When a Treasury Marketable Security Matures"; "get the money (redeem it)". Both kinds of rung are redeemed, in the issuer's own word. (Tess is right that the 15 Oct 2025 release says "liquidation" and never "redeem": confirmed NEW on the Business Wire copy. The SEC notice is the one that speaks to shareholders.) | Keep; 0. Tess's "paid out before each January" (+1) not needed |
| 7 | P3: "...a ladder of Treasury bonds and funds that mature like bonds..." | Tess TRUE IF (iShares' sense); offers "designed to" (+1) | **OVERTURNED** (TRUE) | iShares uses "mature" of the fund itself: "iBonds ETFs are designed to cease trading and mature during a specific maturity window like an individual bond." (U3, re-checked). And they do: IBTE paid "Proceeds of the liquidation ... on December 19, 2024" (**NEW**). "Designed to" is the issuer's legal caution; it fixes nothing (the payout is NAV either way), so it is a hedge (Book 5) | Keep; 0 |
| 8 | P3: "In January 2027, her first $300,000 buys a ladder ..., one rung falling due before each cheque." | Nora TRUE IF (her = Laura's Jan 2027 money; "Treasuries" takes in the funds) | **UPHELD** | Case :129-130 (as row 1). P5's "first finishes any rung the first $300,000 couldn't buy" carries the one-close condition (Window). The open "buys a ladder" vs "any rung" item stays with the thread | Keep; 0 |
| 9 | P3: "A Treasury held to maturity pays exactly what it promises, whatever markets do." | Tess TRUE IF ("exactly" = the dollars); Window TRUE IF; **Kai dissented this morning** (+4) | **OVERTURNED** (TRUE). **Kai's dissent dropped, his +4 withdrawn** | 31 CFR 356.30: "We will pay principal on bills, notes, and bonds on the maturity date as specified in the auction announcement." (re-checked). What a Treasury promises *is* dollars on dates, so Tess's "the dollars" (+1) adds nothing. Her "circumstances could arise that could prevent the timely payment" is a government event, not "markets". My +4, "Held to its date, each rung pays what it was bought to pay, whatever markets do.", stretches a promise over the funds, which "do[] not seek to return any predetermined amount at maturity or in periodic distributions" (U10; the chair re-checked five U10 lines): my fix was the false sentence. The certainty definition that follows rests on the T-bonds, with the funds under Caplet's "near-ironclad" (Book 5), not relitigated | Keep; 0 |
| 10 | P5: "Most of the rest buys Treasuries maturing in late 2032. That is her floor." | Tess FALSE (+11); Window TRUE IF ("Treasuries" covers IBTM) | **NARROWED: FALSE in one word** | "late 2032": true of the holding, "terminate on or about December 15, 2032" (U10; the chair re-checked five U10 lines), which is the date the floor needs; the fund's bonds maturing across 2032 changes nothing for Laura. "That is her floor": true by P6's own definition, "The bottom is her floor, rounded down: money she already owns." Tess's "floor in value only" is that sentence again, as a hedge. "Treasuries": false. P3 has just split "Treasury bonds and funds", so a reader takes P5's "Treasuries" as bonds, and it is one fund; iShares: "Government backing applies only to government issued securities, and does not apply to the funds." (U16). The Window's condition is one P3 itself breaks | AI DRAFT (Claude, 2 Nov 2026): "Most of the rest buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest it is expected to earn, goes into one world index fund, spread across thousands of companies." P5 run 36 → 37; **V52 496 → 497** (at cap). The bare swap alone (+2, "those Treasuries" kept) gives 498: over the cap. Thread option: "...the interest it should earn..." (echoes the pitch's "the interest that floor should earn"): 36 → 35, V52 495. Tess's: 14 → 25 (+11) |
| 11 | P5: "That is about a fifteenth of her money." | Nora FALSE against the book (VT 8.6%), swap "under a tenth" (0); Window TRUE (L-14) | **NARROWED: swap, for a different reason** | The fifteenth is the interest rule's output at today's yields, not a chosen allocation (Kai's arithmetic below, MODEL): one in 17.5 at 4%, one in 14.4 at 5%, one in 12.3 at 6% five-year yield in Jan 2028. So it is a 2028 yield forecast in an allocation's clothes (Book 11). "Under a tenth" holds to about 7.5% and of the book (8.6%). The book gap is real but an implementation drift: the book's 8.7% design is older (`keel/library/insight_v1/securities_and_allocation.md:30,33`, Nora's F3), and the case says the book "does not determine Laura's actual portfolio value" (:129-130), which is Nora's own F1. Bridge: Final Report only (agree with Nora; Wharton IPS :54-55 and :79-80, her citations). The rule itself stays in the sentence before ("roughly the interest ... expected to earn") | AI DRAFT (Claude, 2 Nov 2026), Nora's words: "That is under a tenth of her money." 8 → 8; **0** |
| 12 | P6: "Before she names it, that half moves into Treasuries, so every dollar she promises is already in bonds." | Tess FALSE as worded (+4: "Treasury bond funds", "names", "valued that day") | **OVERTURNED** (TRUE) | The subject of "promises" is Laura, not a fund. The case uses the verb for her range: "If Laura promises more than she can ultimately contribute, she could damage her credibility" (case :114). Money in a Treasury fund is "in bonds" (Tess: "The funds are bonds (they hold Treasuries)"; IBTO 99.99% Treasuries, U1). "Valued that day" is already in the sentence before ("The top adds half her stocks, valued that day"). If the 2031 move ends up in IBTM, "moves into Treasuries" carries row 10's slip, but row 10's fix tells the reader the floor is a fund, and "in bonds" is the claim that counts | Keep; 0 |
| 13 | P10: "Do not crush." (payoff of P2) | Felix TRUE IF P9 keeps "paying out one bond at a time" | **NARROWED: condition widened** | Selling a rung early loses the schedule (P9) *and* the amount: sold before its date, a bond fetches the market's price, "the market value of such securities is not guaranteed and may fluctuate" (U10; the chair re-checked five U10 lines), against P3's "held to maturity ... whatever markets do". So the closing has two anchors, P3 and P9, and survives a cut to P9's line. An instruction can't be false; it lands | Keep; 0 |
| 14 | The name: "Caplet" + "floor" x4 (P5, P6, P7, P9) + "option" (P5); Wharton bans derivatives | Felix: harmless pun in the IPS, small gift for the Final Report, not a liability | **UPHELD** | "Each caplet is a kind of call on the 0.5-year rate set 0.5-years before the payment date" (NYU Stern, re-checked; **NEW** re-fetch, same words). P2 defines the caplet as a pill before any finance word; P5's "option" is the bank's, which the plan refuses: to a rates judge that is the defence, not the risk. A disclaimer costs 17 (496 → 513) | 0 |
| 15 | Felix's reading: reinvested coupons = holding caplets and having sold floorlets (cap − floor = swap) | Felix (new reference) | **UPHELD in sign, NARROWED in use** | **NEW** Wikipedia (tertiary): "if the fixed swap rate is equal to the strike of the caps and floors, then we have the following" ... "Cap-Floor = Swap." **NEW** NYU Stern: a collar is "a long position in a cap and a short position in a floor" (no swap parity on those slides). Sign right: the reinvestor gains if yields rise above what the ladder was priced on and loses if they fall. Instrument wrong, as Felix says (short floating resets vs coupons put into fixed-date bonds). Never written as "Laura is short floorlets" (derivative-ban optics); Felix's 45-word Final Report line, which names the floor and STRIPS as banned fixes, is the safe form | Final Report only |

## Kai's arithmetic for row 11 (MODEL, Kai's, never for the IPS)
Assumptions: the floor's face equals the 2028 deposit ($150,000, no rung top-up); stocks = the interest the floor is
expected to earn = 150,000 × (1 − (1 + y)^−4.95) (2 Jan 2028 to 15 Dec 2032, flat yield y); her money = the 2027
ladder grown 4.5% ($313,500) + $150,000. Results: y = 4%: $26,469, 5.7%, one in 17.5; 4.5%: one in 15.8; 5%: $32,184,
6.9%, one in 14.4 (matches the ground truth's "VT ~$32k in Jan 2028"); 5.5%: one in 13.3; 6%: $37,584, 8.1%, one in
12.3; 7.5%: 9.7%; 8%: 10.3%. A top-up from the 2028 deposit shrinks the floor and the stocks with it, so "under a
tenth" only gets safer. Script: one line of Python in the scratchpad, not committed.

## What I changed my mind on, and what did it
- P3 (row 9): dissent dropped. Tess's IBTM prospectus line made my own fix the false sentence.
- "Gone" (row 5): I came to break it and fixed its footing instead (CMAJ).

## Left for Felix in round 3
1. P5 (row 10): Tess's +11, my +1 (or the thread's −1), or the Window's no change?
2. The fifteenth (row 11): keep it (three judges asked how big the stock slice is, D32 README) or "under a tenth", and
   on whose reason, the book's (Nora) or the yield's (Kai)?
3. "Do not crush." (row 13): does the payoff need P9's line, or does P3 carry it?
Please re-fetch the three new lines a judge could lean on: the IBTE "automatically redeem your shares" sentence, the
TreasuryDirect "get the money (redeem it)" line and the CMAJ "destroyed" line.

## Sources fetched (all Mon 2 Nov 2026)
Read with WebFetch, which returns a small model's extract and quotes at most 125 characters at a time, so long
sentences came back in pieces; pieces are joined with "..." where a gap may exist. Not a byte check.

1. **TreasuryDirect, "Redeeming"**: https://treasurydirect.gov/marketable-securities/redeeming-marketable-securities
   (opened today, unlike the two TreasuryDirect pages Tess was refused). Heading: "Redeeming – Getting Your Money When a
   Treasury Marketable Security Matures". "When a security that you own matures, you can either:" / "get the money
   (redeem it), or". "we pay you the value of the security automatically on the day the security matures."
2. **The same page on another Treasury (Fiscal Service) domain**: https://bondpro.gov/marketable-securities/redeeming-marketable-securities.
   Same heading; the second option: "sometimes reinvest the money in another security of the same type"; "If you have
   not told us to reinvest the money from a matured security," ... "we pay you the value of the security automatically
   on the day the security matures."
3. **iShares Trust, Form 497, "iShares ®iBonds ®Dec 2024 Term Treasury ETF*", "Supplement dated October 17, 2024", "to
   the currently effective Summary Prospectus, Prospectus and Statement of Additional Information"** (two fetches):
   https://sec.gov/Archives/edgar/data/1100663/000119312524238913/d894453d497.htm. "If you still hold shares of the Fund
   on December 19, 2024, the Fund will automatically redeem your shares for cash" ... "based on" "the net asset value as
   of the close of business on December 16, 2024, which will include any dividends" "or distributions calculated as of
   that date." Also: "Proceeds of the liquidation are currently scheduled to be sent to shareholders on December 19,
   2024." and "Any liquidation proceeds paid to you should generally be treated as received by you in exchange for your
   shares". (IBTE is a sister fund, not one of Laura's five; IBTM's own notice won't exist until about October 2032.)
4. **iShares Trust, Form 497, iShares iBonds Dec 2023 Term Muni Bond ETF, supplement dated October 2, 2023**:
   https://www.sec.gov/Archives/edgar/data/1100663/000119312523249071/d395638d497.htm. The extract confirms the phrase
   "automatically redeem your shares" is in it (phrase only; a muni fund, so family wording, not evidence for Treasury
   funds on its own).
5. **iShares on Business Wire, "iShares® iBonds® ETFs Near Final Distribution Dates"** (the 15 Oct 2025 release):
   https://www.businesswire.com/news/home/20251015356466/en/iShares%C2%AE-iBonds%C2%AE-ETFs-Near-Final-Distribution-Dates.
   "Shareholders will receive their proceeds from the liquidation on or around the listed liquidation date"; "Following
   the Fund's termination date, the Fund will distribute substantially all of its net assets"; "The Funds' distributions
   and liquidation proceeds are not predictable at the time of investment". The extract reports no "redeem" or
   "redemption" on the page (Tess's point, confirmed).
6. **Patricia Cornish, "'Avoid the crush': hazards of medication administration in patients with dysphagia or a feeding
   tube", CMAJ 2005;172(7):871-872**: https://cmaj.ca/content/cmaj/172/7/871.full-text.pdf. "the sustained-release
   formulation is designed to deliver the drug gradually over 12 hours."; "Crushing the tablet destroyed the drug's
   sustained-release properties"; "led to rapid absorption of the entire 12-hour dose, which resulted in sedation and
   respiratory depression." (print hyphenation removed by the extract.)
7. **Carpenter, NYU Stern, "Caps and Floors" slides**: https://pages.stern.nyu.edu/~jcarpen0/courses/b403333/18capfloor.pdf.
   "Each caplet is a kind of call on the 0.5‐year rate set 0.5‐years before the payment date" (Felix's line, same
   words); a collar is "a long position in a cap and a short position in a floor". The slides have no cap-floor-swap
   parity.
8. **Wikipedia, "Interest rate cap and floor"** (tertiary; a re-check of Felix's unre-checked line):
   https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor. "if the fixed swap rate is equal to the strike of the caps
   and floors, then we have the following" ... "Cap-Floor = Swap."; "The interest rate cap can be analyzed as a series
   of European call options, known as caplets,".

Searches run, results not used: ISMP's do-not-crush list (no primary page returned); "crushing destroys extended-release"
(only the CMAJ hit used).

Local files read: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` :114, :129-130;
`competition/wins/2026-10-23_snapshot.md` (positions, weights); `keel/ips_rewrite/00_GROUND_TRUTH.md` s5;
`keel/ips_rewrite/drafts/D32/README.md`; the three round-1 posts and scout files; the Window's V52 read (branch above).

Not fetched by me, UNVERIFIED here: the TYLENOL 8 HR label (Window W-07); the IBTM product page and its Treasury
share; Felix's Seroquel XR, Baruch, AAII, Healthdirect and TGA Diabex lines; Tess's semi-annual report, fact sheets and
TreasuryDirect FAQ.

(Keel is a simulated team, AI-written.)
