# The Rooftop, Mon 26 Oct 2026: our mistakes moved from dates to certainty words; the case asks for three kinds of sure

AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
(Keel is a simulated team, AI-written.) The roof is fiction; the count and the case reading are real work.
Work order: SD-ROOF-02 | Room: The Rooftop (Tess hosts; everyone; no subagents) | Mon 26 Oct 2026, 20:40 AEDT
Entry: `../../rooms/rooftop.md` (Mon 26 Oct). Serves the IPS rewrite (Draft 1, Fri 30 Oct).

## What we counted
Every catch that changed or blocked a line between Sat 24 Oct 20:30 and Mon 26 Oct 20:30 (outbox memos and the
rewrite inbox). Eleven. One was a date, three were facts or rules, and **seven were the same mistake: a word that
says a holding is surer than it is.**

| # | Catch (room) | The stretched word | What is true (locked text or model) |
|---|---|---|---|
| 1 | A11 (Archive, 25 Oct) | "release" next to a fixed dollar amount, iBonds rungs | Reflection 2: payout is "a net asset value, as opposed to a promise of par" |
| 2 | C-01 (Courtroom, 25 Oct) | the $10k buffer as payment safety ("9 in 100 -> 3 in 100") | Payments covered either way once they come first; the buffer is a $10k lower quote |
| 3 | N2 (Window, 26 Oct) | "floor $150k face" | IBTM is an ETF; IBTM note: "the final payout is not fixed" |
| 4 | A14 (Archive, 26 Oct) | "exact" for the ladder (Library S-04) | Note 1: a "10.5-month gap" with "reinvestment-rate risk" |
| 5 | A15 (Archive, 26 Oct) | 2031 bottom "not a forecast" | Reflection 2's own words: "not merely a forecast" |
| 6 | A16 (Archive, 26 Oct) | "rates/markets can't touch a payment" | Price can't; reinvested coupons meet rates (Nov-2039, Nov-2041 notes) |
| 7 | H1 (Writing Room, 26 Oct) | 2031 bottom "in the bank" | "already bought"; same NAV line as row 1 |

The other four: N1, the 15 Oct ladder still quoted in the rewrite spine (a date); the short-term Treasury ETF not yet
seen on WInS (a listing); "Taiwan residency" for "creative residency" (a case term); "trade only to invest the 2028
deposit" contradicted by the next sentence (a rule). Saturday's Rooftop said our errors were our own dates and
editions. That pattern has moved.

## Why it matters for the IPS
The case does not ask us to sound certain. It asks teams to "define what they consider a high degree of funding
certainty, explain how they evaluated that level of certainty, and identify the assumptions supporting their
recommendation" (case :97-98). Seven word-fixes are one missing answer to that question. Our holdings are sure in
three different ways, and one word has been stretched over all three:

| Strength | Holdings (WInS book, `competition/COMPETITION.md` s8) | What carries the risk | Locked words that already say so |
|---|---|---|---|
| **By contract** | T-bonds Feb-2037, May-2038, Nov-2039, Nov-2040, Nov-2041 (payments 2038-2042), held to maturity | Only reinvested coupons and the 2037 bond's 10.5-month wait meet interest rates | "near-ironclad guarantee"; "matches the liability perfectly"; "reinvestment-rate risk" |
| **By design** | iBonds IBTM, IBTO-IBTR (payments 2033-2037) and IBTM's second job, the 2031 floor | The fund's closing value, not a promised par; small, but not zero | "net asset value, as opposed to a promise of par"; "final payout is not fixed"; "not merely a forecast" |
| **A forecast** | VT | Everything; it only moves the top of the 2031 range | "VT is where we allow ourselves to be wrong"; "about 7.5% a year (as per JPMorgan)" |

Two things follow, both real:
- **The locked "near-ironclad" covers half the payments, not all ten.** Five payments and the whole 2031 floor rest on
  "by design", not "by contract". Saying so is what the Archive meant by "the 'near' in 'near-ironclad', spelled out"
  (A3). It also keeps reflection 1 true: we did provide a near-ironclad guarantee, for the payments a Treasury exists for.
- **It's an answer, not a hedge.** One confident sentence per strength replaces the word-by-word policing (the rewrite
  rules 1-3 in `../../ips_rewrite/inbox/2026-10-26_archive.md` all follow from it). Ray asked us on 25 Oct to stop
  softening words; this is the opposite of softening. It says exactly how sure, which is what the case asks.

## Material for Draft 1 (AI DRAFT, Claude, 26 Oct 2026; 74 strict, `textcheck.py --voice` 0 flags)
`../../drafts/rooftop_2026-10-26/three_kinds_of_sure.txt`:
> Sure comes in three strengths. The 2038-2042 Treasuries are sure by contract: the government owes that principal
> and those coupons, and only what we reinvest ever meets interest rates. The 2033-2037 iBonds and the 2031 floor are
> sure by design – each fund closes in its year and pays what its Treasuries are worth, close to plan but never to
> the dollar. The stock fund is a forecast. It only moves the top.

74 words is 15% of the IPS. If it earns a place, it should replace the certainty definition, not sit beside it. It
fits Caplet XR (Long Room vote B) without a second metaphor: a release schedule is only as sure as its coating.
That line is for the Writing Room to test, not a proposal for the IPS.

## Limits
- The count is Keel's own catches, read from memos; a catch a room didn't write up isn't in it.
- "Sure by design" for the floor depends on D1b (Writing Room H2): under D1a the floor is the last source for a coupon
  gap, so it can be drawn. The vote on Tue 27 Oct decides which.
- Dollar shares by strength aren't computed here (the Genius Lab is asked). No new model numbers in this memo.

Tess: Saturday I said our mistakes were dates. Tonight they're adjectives. The fix isn't fewer adjectives – it's
three honest ones, each on the right holding.
Nora: Good, because I'd rather answer the case's question than keep a list of words we're scared of. Writing Room has
it by Friday.
Kai: "Near-ironclad" covers five payments. Say it before a judge does – and say it like we meant to.
Jun: The middle row is the interesting one. The iBonds' wobble at close is small, and I'll put a number on it before
anyone writes "small" in the IPS.
Amara: The co-sponsors only need one row: the floor's. And it's in the middle row, not the top. That's worth knowing
before Laura pledges it.
Felix: Checked all three against the case wording. It answers :97-98 directly, which nothing in v4 did. It names no
banned security, and "iBonds" is a WInS listing we already hold.
