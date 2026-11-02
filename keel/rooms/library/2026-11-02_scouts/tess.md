# Tess's scout notes (round 6, Mon 2 Nov 2026; Haiku 5.5) (Keel is a simulated team, AI-written.)

**Question (Q14, round 6, near scout):** what do the funds and Treasuries in V52 say, and is it true at the funds' own source?
**Text tested:** `keel/ips_rewrite/drafts/D32/ips_V52.txt` (P2, P3, P5, P6) and `keel/ips_rewrite/drafts/D32/pitch.txt` (line 4, "Her first $300,000 buys Treasuries that each mature before a January.").
**Dates read:** 2 Nov 2026. **Method:** WebSearch to find pages, WebFetch to read them (curl not used).

**Limits to know before you rely on a quote.** WebFetch returns a model-extracted version of each page. Every quote below is as WebFetch returned it from the URL named. None has been pulled a second time, and some long sentences are joined from two WebFetch fragments with "...". The chair should re-check each quote against its URL. No WInS page was opened. The holdings check used `competition/wins/2026-10-23_snapshot.md`.

**Labels.** Every plainest-true sentence below is AI DRAFT (Claude, 2 Nov 2026). They contain no model numbers and no "our model". Strict counts come from `python3 keel/office/tools/textcheck.py -`, quoting the larger of the two counts (words by spaces; words split on hyphens).

**Source keys (full list at the bottom):** U1 IBTO partner product page; U2 IBTO fact sheet; U3 iShares press release, 15 Oct 2025; U4 TreasuryDirect FAQ; U5 IBTP fact sheet; U6 IBTR product page; U7 IBTQ semi-annual report; U8 iShares semi-annual financial statements (IBTP, IBGA, IBGK); U9 31 CFR 356.30; U10 IBTM summary prospectus; U11 IBTM fact sheet; U12 to U14 BlackRock individual product pages (IBTO, IBTQ, IBTR); U15 IBTQ product page; U16 iShares iBonds strategy page; U17 iShares bond ladder page; U18 IBTO summary prospectus; U19 IBTQ summary prospectus; U20 IBTR summary prospectus; U21 IBTP product page; U22 IBTP summary prospectus.

**For the chair (not finds; decisions for later rounds).**
1. **Holdings check.** The snapshot (`competition/wins/2026-10-23_snapshot.md`) lists IBTM, IBTO, IBTP, IBTQ, IBTR, the T-bonds Feb-2037, May-2038, Nov-2039, Nov-2040 and Nov-2041, and VT 167. That matches the brief and CLAUDE.md. `keel/CAST.md` ("Current state", 23 Oct) lists four iBonds (no IBTR) and a Feb-2036 T-bond. CAST.md looks out of date. I did not check WInS.
2. **"Near-ironclad" (Standing rule, BIBLE.md).** The fund pages say "An investment in the Fund(s) is not guaranteed, and an investor may experience losses, including near or at the termination date" (U1, U13, U14, U21). The team's phrase is theirs to keep or drop; the funds' own word is "not guaranteed".
3. **"Par".** None of the five summary prospectuses, fact sheets or product pages uses "par" as a term. The nearest is "predetermined amount". Caplet's TNA reflection contrast "a promise of par" is the team's own wording, not the funds'.
4. **"Ladder".** iShares uses the word itself: "build a bond ladder" (U16, U1, U21) and "Access a bond ladder with one ticker" (U17). P3's use is safe on that reading.

---

## Finds

### Find 1. "Mature like a bond" is iShares' own phrase, and the same pages say the payout is not fixed

- **Source:** iShares iBonds strategy page (iShares/BlackRock; https://www.ishares.com/us/strategies/ibonds; read 2 Nov 2026; U16). iShares bond ladder page (https://ishares.com/us/strategies/bond-etfs/build-better-bond-ladders; read 2 Nov 2026; U17). iShares press release dated 15 Oct 2025 (https://www.ishares.com/us/literature/press-release/ibonds-terminations-release.pdf; read 2 Nov 2026; U3).
- **Quoted lines:**
  - Ladder page, meta description: "iBonds ETFs are designed to mature like a bond, trade like a stock, and diversify like a fund."
  - Press release: "iBonds ETFs are designed to cease trading and mature during a specific maturity window like an individual bond."
  - Strategy page: "Unlike a direct investment in a bond that has a level coupon payment and a fixed payment at maturity," then "...the Fund(s) will make distributions of income that vary over time."
  - Ladder page: "iBonds ETFs payout their NAV in their maturity year."
- **Mechanism:** "Mature like a bond" describes the end date. Each fund stops in a set December, and the bonds inside it mature on the way. The payout is the fund's net asset value, not a fixed sum, and the same pages say so.
- **Touches V52:** P3, "funds that mature like bonds", and the next sentence, "A Treasury held to maturity pays exactly what it promises".
- **Where it breaks:** A judge who hears "mature like bonds" as "pays a fixed sum at maturity" has misread it, and iShares contradicts that reading on the same page. "Matures like a bond" and "bond-like" are not on any fund page, fact sheet or prospectus fetched (NOT FOUND).

### Find 2. IBTM is expected to be almost all cash by its end, and it promises no amount

- **Source:** IBTM summary prospectus, cover dated 27 Feb 2026 (https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf; read 2 Nov 2026; U10).
- **Quoted lines:** "The Fund is a term fund that will terminate on or about December 15, 2032, at which time it will distribute its remaining net assets to shareholders pursuant to a plan of liquidation." "By December 15, 2032, the Fund is expected to consist almost entirely of cash." "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions."
- **Mechanism:** The bonds inside IBTM mature through 2032. By mid-December the fund is expected to be almost all cash, and holders receive its net assets, not a set sum.
- **Touches V52:** P5, "Most of the rest buys Treasuries maturing in late 2032. That is her floor." The same word appears in pitch.txt: "Her 2028 deposit buys a Treasury floor for her building gift" (same verdict). The WInS book uses IBTM as the floor stand-in (snapshot row: "2033 payment + floor stand-in").
- **Where it breaks:** "late 2032" (the holdings mature across the year, and the fund is cash by December) and "floor" (no promised amount). The other four funds use the same wording (table below).

### Find 3. Holders do not redeem the funds; the funds distribute

- **Source:** iShares/BlackRock IBTO product page (https://www.blackrock.com/us/partner/products/332291/ishares-ibonds-dec-2033-term-treasury-etf; read 2 Nov 2026; U1). iShares semi-annual financial statements covering IBTP, IBGA and IBGK, six months to 30 Apr 2026 (https://www.ishares.com/us/literature/semi-annual-financial-statements/safs-ishares-ibonds-dec-treasury-etfs-04-30-en.pdf; read 2 Nov 2026; U8).
- **Quoted lines:** "Shares of ETFs are bought and sold at market price (not NAV) and are not individually redeemed from the fund." "Except when aggregated in Creation Units, shares of each Fund are not redeemable."
- **Mechanism:** A holder either sells shares on the market or holds to the end and receives the fund's distribution of its net assets. In the termination wording we fetched, iShares uses "distribute" and "liquidation" for the end of a fund, and never "redeem".
- **Touches V52:** P2, "R is redemption – ten holdings, one redeemed for each January." The five Treasury bonds in the book are paid on their maturity dates (31 CFR 356.30, U9: "We will pay principal on bills, notes, and bonds on the maturity date as specified in the auction announcement.").
- **Where it breaks:** "one redeemed" for the funds. R = redemption is a standing team name, so the chair decides whether to keep it. The plain verb for what the funds do is "paid out".

### The five funds' wording (question e: do they differ from IBTM's?)

The summary prospectus wording is identical for all five funds. The differences are the year, the cover date, and what each product page says.

| Fund | Objective (iShares' words) | Summary prospectus (cover date) | Termination | Payout wording | Product page or fact sheet |
|---|---|---|---|---|---|
| IBTM (Dec 2032) | "...index composed of U.S. Treasury bonds maturing in 2032." | 27 Feb 2026 (U10) | "on or about December 15, 2032" | "does not seek to return any predetermined amount at maturity or in periodic distributions" | Product page not fetched. Fact sheet (U11, as of 30 Sep 2026): "terminate on or about October or December 15 of the year in each Fund's name." |
| IBTO (Dec 2033) | "...maturing in 2033." | 27 Feb 2026 (U18) | "on or about December 15, 2033" | same as IBTM | Product page (U1): "not individually redeemed from the fund". Treasuries 99.99% (29 Oct 2026). |
| IBTP (Dec 2034) | "...maturing in 2034." | 27 Feb 2026 (U22) | "on or about December 15, 2034" | same as IBTM | Product page (U21): "During the final year of the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the liquidation of the fund." |
| IBTQ (Dec 2035) | "...maturing in 2035." | 27 Feb 2026 (U19) | "on or about December 15, 2035" | same as IBTM | Product page (U15, as of 6 Jul 2026): same "final year" sentence, no termination date. Semi-annual report (U7): no termination or payout wording. |
| IBTR (Dec 2036) | "...maturing in 2036." | Cover 25 Mar 2026; text says "both dated February 23, 2026" (U20) | "on or about December 15, 2036" | same as IBTM | Product page (U6, as of 12 Jun 2026): no termination or payout wording at all. |

**Treasury side (U4, U9).** TreasuryDirect's FAQ says (WebFetch extraction): "the full faith and credit of the U.S. government guarantees that interest and principal payments will be paid on time." Two TreasuryDirect pages (treasury-notes and understanding-pricing) refused WebFetch on robots grounds, so the held-to-maturity wording comes from the federal rule (U9) and from the iShares summary prospectuses (U10, U18 to U22).

---

## Verdicts

| # | Where | V52 sentence (as in the file) | Source line | Verdict | Plainest true sentence (AI DRAFT, Claude, 2 Nov 2026) | Strict count (old to new) |
|---|---|---|---|---|---|---|
| 1 | Pitch | "Her first $300,000 buys Treasuries that each mature before a January." | U2: "The iShares iBonds Dec 2033 Term Treasury ETF seeks to track an index of U.S. Treasury bonds maturing in 2033." U1: "Treasuries" 99.99% of market value (as of 29 Oct 2026). Funds: "will terminate on or about December 15" (U18). T-bonds: dates from the 23 Oct snapshot. | **TRUE IF** "Treasuries" takes in the five iBonds funds. They hold Treasury bonds and end in December. The five T-bonds mature 15 Feb 2037 to 15 Nov 2041, each before a January. | "Her first $300,000 buys Treasury bonds and Treasury bond funds, each ending before a January." | 11 to 15 (+4) |
| 2 | P2 | "To us, X is ten and R is redemption – ten holdings, one redeemed for each January." | U1: "...are not individually redeemed from the fund." U8: "...shares of each Fund are not redeemable." | **TRUE IF** "redeemed" means "paid out when it ends". For the funds, holders do not redeem shares. R = redemption is a team name; the plain verb is "paid out". | "To us, X is ten and R is redemption – ten holdings, one paid out before each January." | 17 to 18 (+1) |
| 3 | P3 | "In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung falling due before each cheque." | U17 (meta): "iBonds ETFs are designed to mature like a bond, trade like a stock, and diversify like a fund." U3: "...designed to cease trading and mature during a specific maturity window like an individual bond." | **TRUE IF** "mature like bonds" means iShares' sense: a set end month, not a fixed sum. | "In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds designed to mature like bonds, one rung falling due before each cheque." | 25 to 26 (+1) |
| 4 | P3 | "A Treasury held to maturity pays exactly what it promises, whatever markets do." | U10, U18, U19, U20, U22 (all five summary prospectuses name the same text): "Direct obligations of the U.S. Treasury have historically involved little risk of loss of principal if held to maturity, but the market value of such securities is not guaranteed and may fluctuate." And: "Although U.S. Treasury obligations are backed by the full faith and credit of the United States, circumstances could arise that could prevent the timely payment of interest or principal." U9: "We will pay principal on bills, notes, and bonds on the maturity date as specified in the auction announcement." | **TRUE IF** "exactly" means the nominal dollars and dates the Treasury sets. The source says "little risk", not no risk, and says timely payment "could" be prevented in unusual circumstances. It says nothing about reinvesting coupons. | "A Treasury held to maturity pays exactly the dollars it promises, whatever markets do." | 13 to 14 (+1) |
| 5 | P5 | "Most of the rest buys Treasuries maturing in late 2032. That is her floor." | U10: "...an index composed of U.S. Treasury bonds maturing in 2032." U10: "By December 15, 2032, the Fund is expected to consist almost entirely of cash." U10: "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions." | **FALSE.** It is a fund, not Treasuries. The bonds mature across 2032, and the fund is expected to be almost all cash by mid-December. It promises no amount. | "Most of the rest buys a fund of Treasuries maturing in 2032. It promises no set amount, so that is her floor in value only." | 14 to 25 (+11) |
| 6 | P6 | "Before she names it, that half moves into Treasuries, so every dollar she promises is already in bonds." | U10 and U18: "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions." U16: "Government backing applies only to government issued securities, and does not apply to the funds." U1: "An investment in the Fund(s) is not guaranteed, and an investor may experience losses, including near or at the termination date." | **FALSE as worded.** The funds are bonds (they hold Treasuries), but they promise nothing, and government backing does not reach them. **TRUE IF** "promises" means the figure she names, valued that day. | "Before she names it, that half moves into Treasury bond funds, so every dollar she names is in bonds, valued that day." | 18 to 22 (+4) |

Row 5's verdict also applies to the pitch line "Her 2028 deposit buys a Treasury floor for her building gift", which is not one of the six.

---

## URLs fetched (all read 2 Nov 2026 unless marked)

- U1 https://www.blackrock.com/us/partner/products/332291/ishares-ibonds-dec-2033-term-treasury-etf (IBTO product page, partner; 29 Oct 2026 holdings date)
- U2 https://ishares.com/us/literature/fact-sheet/ibto-ishares-ibonds-dec-2033-term-treasury-etf-fund-fact-sheet-en-us.pdf (IBTO fact sheet, as of 30 Sep 2026)
- U3 https://www.ishares.com/us/literature/press-release/ibonds-terminations-release.pdf (iShares press release, 15 Oct 2025)
- U4 https://treasurydirect.gov/help-center/faqs/marketable-faqs/ (TreasuryDirect FAQ; WebFetch extraction)
- U5 https://www.ishares.com/us/literature/fact-sheet/ibtp-ishares-ibonds-dec-2034-term-treasury-etf-fund-fact-sheet-en-us.pdf (IBTP fact sheet, as of 30 Sep 2026)
- U6 https://www.ishares.com/us/products/350028/ (IBTR product page; as of 12 Jun 2026)
- U7 https://www.ishares.com/us/literature/semi-annual-report/sar-ibtq-en.pdf (IBTQ semi-annual report, period to 30 Apr 2026; no termination wording found)
- U8 https://www.ishares.com/us/literature/semi-annual-financial-statements/safs-ishares-ibonds-dec-treasury-etfs-04-30-en.pdf (IBTP, IBGA, IBGK financial statements, six months to 30 Apr 2026)
- U9 https://www.law.cornell.edu/cfr/text/31/356.30 (31 CFR 356.30, Cornell LII copy)
- U10 https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf (IBTM summary prospectus, cover 27 Feb 2026)
- U11 https://ishares.com/us/literature/fact-sheet/ibtm-ishares-ibonds-dec-2032-term-treasury-etf-fund-fact-sheet-en-us.pdf (IBTM fact sheet, as of 30 Sep 2026)
- U12 https://www.blackrock.com/us/individual/products/332291/ishares-ibonds-dec-2033-term-treasury-etf (IBTO product page, individual; read for its document list)
- U13 https://www.blackrock.com/us/individual/products/342105/ishares-ibonds-dec-2035-term-treasury-etf (IBTQ product page, individual)
- U14 https://www.blackrock.com/us/individual/products/350028/ishares-ibonds-dec-2036-term-treasury-etf (IBTR product page, individual)
- U15 https://www.ishares.com/us/products/342105/ (IBTQ product page; as of 6 Jul 2026)
- U16 https://www.ishares.com/us/strategies/ibonds (iShares iBonds strategy page)
- U17 https://ishares.com/us/strategies/bond-etfs/build-better-bond-ladders (iShares bond ladder page)
- U18 https://www.blackrock.com/us/individual/literature/summary-prospectus/sp-ishares-ibonds-dec-2033-term-treasury-etf-10-31.pdf (IBTO summary prospectus, cover 27 Feb 2026)
- U19 https://www.blackrock.com/us/individual/literature/summary-prospectus/sp-ishares-ibonds-dec-2035-term-treasury-etf-10-31.pdf (IBTQ summary prospectus, cover 27 Feb 2026)
- U20 https://www.blackrock.com/us/individual/literature/summary-prospectus/sp-ishares-ibonds-dec-2036-term-treasury-etf-10-31.pdf (IBTR summary prospectus, cover 25 Mar 2026)
- U21 https://www.blackrock.com/us/individual/products/337745/ishares-ibonds-dec-2034-term-treasury-etf (IBTP product page, individual)
- U22 https://www.blackrock.com/us/individual/literature/summary-prospectus/sp-ishares-ibonds-dec-2034-term-treasury-etf-10-31.pdf (IBTP summary prospectus, cover 27 Feb 2026)

Fetch failed (refused on robots grounds, nothing retrieved): https://treasurydirect.gov/marketable-securities/treasury-notes and https://treasurydirect.gov/marketable-securities/understanding-pricing/

Local file read (not a web page): `competition/wins/2026-10-23_snapshot.md`. No WInS page was opened.

Not fetched: the IBTM product page; the IBTQ and IBTR fact sheets (the search did not return them).

Full finds: `keel/rooms/library/2026-11-02_scouts/tess.md` (this file).
