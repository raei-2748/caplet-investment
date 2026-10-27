# Ground truth for the rewrite (read 26 Oct 2026, Sydney)

AI-generated (Claude Code). Every new IPS line must survive this page.

## 0. SUPERSEDED IN PART (27 Oct): the updated IPS instructions (Ray: "THIS IS BIBLE")
`competition/official/2026_27/UPDATED_2026_WGY_Investment_Policy_FINAL.txt` (v2.0). Pages 1-2 are word-for-word the
same as v1 (purpose, the list of what to cover, "focus on the strategy and decision-making framework", what's not
expected, "may not be revised"). Page 3 is replaced:
- **Two form fields only.** Pitch: "Maximum 50 words. Quickly summarize your team's investment strategy. Clearly
  communicate the central idea behind your approach and how it is designed to support your client's financial goals
  and future funding needs." IPS: "Maximum 500 words. Clearly explain your team's investment strategy and
  decision-making framework, including how the strategy addresses Laura's financial goals, funding needs, and risk
  considerations."
- **Gone:** the title page (team name, "First Name, Last Initial", WInS username), the gate sentence ("Submissions
  that do not meet the requirements below will not be considered"), Times New Roman / 12pt / double spacing /
  margins, "Submit as a PDF", the 5 MB limit, the two-page limit and the sample layout.
- **Kept:** no graphics, charts, images, attachments, external links, footnotes or formal citations; sources go in
  the Final Report.
- **So:** plain text in a form box. No bold, italics or tables can be relied on; any heading is plain text and costs
  words. Whether SMApply counts words the way `textcheck.py` does is UNVERIFIED: aim for 490 by the strict count.

## 1. What the IPS form asks (official v1, `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`; page 3 superseded by s0)
- Pitch, max 50 words: "the central idea behind your approach and how it is designed to support your client's
  financial goals and future funding needs".
- IPS, max 500 words: goals, why the strategy fits, the balance of growth / liquidity / funding reliability / risk /
  flexibility, how it guides construction and decisions as needs change, how it protects the payments while
  supporting a responsible facility contribution; the operating commitment, the reserve's composition over time,
  determining the contribution, preserving flexibility. "Focus on the strategy and decision-making framework ...
  rather than describing individual investments or presenting detailed financial calculations."
- Not expected in the IPS: final reserve calculations, projections, a final range, the co-sponsor text (Final Report).
- No graphics, links, footnotes, formal citations. Strategy may not be revised after submission.
- (v1 only, removed in v2: the gate sentence and the title page; see s0.)
- Coherence (form :75): "Your portfolio and Final Report should reflect the strategy established in your IPS." The
  WInS book freezes with the IPS, so any change to what the ladder IS (e.g. R01's dedicated sizing) must show in the
  frozen book or be stated plainly as the Jan 2027 build.
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
  "If Laura promises more than she can ultimately contribute, she could damage her credibility"; "Rather than
  promising one exact amount ... a credible range" (:115-116); explain "how favorable and unfavorable market outcomes
  could affect the amount" (:118-119); "The proposed range must also protect the portfolio's ability to fund the
  ten-year operating commitment" (:119-120).
- "willing to take thoughtful risks"; wants "an appropriate balance between pursuing growth and protecting the capital
  required for her goals". Living costs outside the portfolio. degree in "Statistics & Information Decisions Management" (Wharton 2018), product manager,
  graphic novelist (The Wuhan I Know, Messy Roots), residency for artists, writers, designers, entrepreneurs, educators.
- Taxes, Taiwan law, facility cost estimates: out of scope. No contingency fund or endowment sizing expected (:106-107).
- Assumptions to identify (:146-148): investment performance, timing of cash flows, outside funding, inflation's effect
  on projections AND facility costs, and the flexibility to preserve.

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
STALE: `keel/library/ips_numbers_2026-10/` is on the 15 Oct curve. Newest close on file (22 Oct, The Window 26 Oct):
ladder $298,861 on the payment-date basis, headroom $1,139 (4bp); other bases $300,224 / $302,139. So "the first
$300,000 buys all ten payments" is a one-close call, not a fact: echo only the IBTR note's conditional. IBTM has no
face value: say "IBTM sized to pay about $150k in 2032, quoted at $145k". Older 15 Oct figures: VT ~$32k in
Jan 2028; range ~$145k-$168k; ~99% inside; coupon shortfall ~$21k if yields fall 2pt for good.
New: `lab/R01_dedication.py` (this folder).

## 6. Halfway-point newsletter (27 Oct; `competition/official/2026_27/wharton_email_week5_2026-10.md`)
"Updated IPS instructions" are linked (Box) but could not be opened here: the form's fields and limits are
UNVERIFIED until a student downloads them. Bans now read "Individual TIPS" / "Individual STRIPS". Official tips:
"Let your investment strategy lead"; "Explain why each investment belongs in your strategy". All current holdings
comply. Build the draft to the form once its fields are known.
