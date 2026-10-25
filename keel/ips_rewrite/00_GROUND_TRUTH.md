# Ground truth for the rewrite (read 26 Oct 2026, Sydney)

AI-generated (Claude Code). Every new IPS line must survive this page.

## 1. What the IPS form asks (official, `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`)
- Pitch, max 50 words: "the central idea behind your approach and how it is designed to support your client's
  financial goals and future funding needs".
- IPS, max 500 words: goals, why the strategy fits, the balance of growth / liquidity / funding reliability / risk /
  flexibility, how it guides construction and decisions as needs change, how it protects the payments while
  supporting a responsible facility contribution; the operating commitment, the reserve's composition over time,
  determining the contribution, preserving flexibility. "Focus on the strategy and decision-making framework ...
  rather than describing individual investments or presenting detailed financial calculations."
- Not expected in the IPS: final reserve calculations, projections, a final range, the co-sponsor text (Final Report).
- No graphics, links, footnotes, formal citations. Strategy may not be revised after submission.
- Week 4 email: now an SMApply form, "all other requirements remain the same"; TIPS and STRIPS banned for both
  contributions.

## 2. Case facts the strategy rests on (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`)
- $300k at the start of 2027; $150k at the start of 2028 "using earnings from publishing advances, speaking
  engagements, licensing, and other entrepreneurial ventures". No other flows before 2033.
- Ten fixed nominal $50k payments, start of 2033-2042, "high degree of certainty", no outside funding.
- Operating reserve set aside at the start of 2033; teams recommend size, initial composition, how it changes;
  define high certainty, how it was evaluated, assumptions.
- Facility contribution: "how much of the remaining portfolio she can responsibly contribute"; "committing all
  remaining assets could limit her financial flexibility as the project develops".
- 2031: a credible dollar range + confidence; "A meaningful personal contribution may signal that the residency is
  financially viable, demonstrate Laura's commitment ... and make potential co-sponsors more willing to contribute";
  "If Laura promises more than she can ultimately contribute, she could damage her credibility".
- "willing to take thoughtful risks"; wants "an appropriate balance between pursuing growth and protecting the capital
  required for her goals". Living costs outside the portfolio. Statistics degree (Wharton 2018), product manager,
  graphic novelist (The Wuhan I Know, Messy Roots), residency for artists, writers, designers, entrepreneurs, educators.
- Taxes, Taiwan law, facility cost estimates: out of scope. Inflation's effect on projections and facility costs:
  in scope as an assumption.

## 3. The submitted TNA (locked 23 Oct; IPS Report Doc, tab "Trading Notes", read 26 Oct). Lines the IPS must not contradict
- Note 1 (Feb-2037 T-bond): "latest WInS bond available beforehand"; "reinvestment-rate risk on the proceeds held in
  a short-term Treasury ETF". Reflection: Treasuries "won't create wealth, but they will remove uncertainty, through
  duration-matching"; "we take Laura's requested 'high degree of certainty' to mean a near-ironclad guarantee, and we
  provide exactly that"; "Every year the bonds sit untouched is a good year"; nominal Treasury "matches the liability
  perfectly", no TIPS.
- Note 2 (IBTM): "does two jobs": first payment + "a floor for her facility contribution, giving co-sponsors a minimum
  figure in 2031"; "final payout is not fixed". Reflection: iBonds "behave a lot like bonds when held to their end";
  "each of Laura's payments rests on a dedicated instrument (not merely a forecast)"; terminal payout is NAV not par,
  "in return we gain a level of liquidity which no odd-lot bond offers".
- Note 3 (VT): ~10,000 stocks, 0.06% fee; stocks "only set how far her gift rises above her promised minimum"; "a rise
  before 2031 lifts the top of the range co-sponsors hear". Reflection: "VT is where we allow ourselves to be wrong";
  "the vain illusion that we can pick winners"; "about 7.5% a year (as per JPMorgan)"; "how generous can the facility
  contribution be?"
- WInS notes (all 11 filled 6-7 Oct ET): IBTM/IBTO/IBTP/IBTQ/IBTR for 2033-2037 payments; T-bonds Feb-2037, May-2038,
  Nov-2039, Nov-2040, Nov-2041 for 2038-2042; VT. IBTR note: "If yields fall more than about 0.2 percentage points
  by January, the 2028 deposit would top up the ladder, leaving less for the facility." Nov-2039 note: "reinvested
  coupons fund the rest". Nov-2041 note: "reinvested coupons funding part of each".
- So the IPS is bound to: Treasuries/iBonds matched to each payment; IBTM as payment 1 AND the facility floor; VT as
  the only growth; a promised minimum; a 2031 range whose top moves with stocks; 2028 deposit tops up the ladder first.

## 4. Open Caplet votes that change the text (vote set B, Tue 27 Oct)
D1a (floor is the last source for a coupon gap), D1b (quote the 2031 bottom with a margin), "artists" -> "residents",
and the D2-D7 rows of ballot v1. The rewrite follows the votes once logged; until then it uses Keel's leans, marked.

## 5. Numbers (MODEL; re-run before any figure goes in)
`keel/library/ips_numbers_2026-10/` (15 Oct curve): ladder ~$294-297k; floor $150k face, quoted ~$145k; VT ~$32k in
Jan 2028; range ~$145k-$168k; ~99% inside; coupon shortfall ~$21k if yields fall 2pt for good.
New: `lab/R01_dedication.py` (this folder).
