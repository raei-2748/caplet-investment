# Tess, round 2: sources read beside Felix's conclusions (H-028)

(Keel is a simulated team, AI-written.) Read 4 Nov 2026 (Sydney). `curl` to hnn.us and authorsguild.org was refused by
the session's proxy (403), so the pages were read with the WebFetch tool. That tool returns short quotes only; where a
sentence was too long to return whole, the fragments below were confirmed to sit in the same sentence.

## 1. Times Online via History News Network, 11 Jun 2009
- URL: https://www.hnn.us/article/98832 (read 4 Nov 2026)
- Headline: "Authors feel the pinch as recession-hit publishers cut advances (England)"
- Exact words found: "Authors are seeing advances reduced to a quarter of what they could have expected two years ago"
  and, in the same sentence, "as publishers react to the recession". Felix's quote is there.
- Cuts against Felix: an unnamed "accomplished history writer" says publishers "were using the recession to take
  advantage of authors" and "book sales are only down by about 5 per cent". The article centres on British historians and
  serious non-fiction (one book's advance falling from about £120,000 to about £30,000). Laura is an American graphic
  novelist. The words "speaking", "licensing" and "stock" do not appear.
- Verdict: quote VERIFIED. Supports "advances dry up in a downturn" for one genre, one country, one recession.

## 2. Authors Guild COVID-19 Survey #3, 18 Feb 2021
- URL: https://authorsguild.org/news/authors-guild-covid-19-survey-3-summary-of-responses/ (read 4 Nov 2026)
- Exact words found: "46.3% reported losing income from speaking engagement cancellations". Felix's quote is there.
  Also: "incomes in the writing profession have continued to decline during the pandemic"; 71.4% said their income
  "(from any source) had declined since the crisis began"; average loss "49% of their regular pre-pandemic income".
- Sample: 669 respondents, Guild members and non-members; the survey's dates are not stated.
- Cuts against Felix: the page contrasts authors with "the strong revenues and sales posted by large trade publishers in
  2020". The words "advances", "licensing" and "royalties" do not appear. The nearest thing to licensing is "film option
  extensions or non-payment" (3.4%); "book contract cancellations or payment delays" is 12.9%.
- Verdict: quote VERIFIED. Supports "speaking income dries up in a downturn"; licensing barely shows.

## 3. PBS NewsHour (AP), 18 Aug 2020 (used to test "rides on shares")
- URL: https://www.pbs.org/newshour/economy/sp-500-closes-at-a-record-erasing-last-of-pandemic-losses (read 4 Nov 2026)
- Exact words found: headline "S&P 500 closes at a record, erasing last of pandemic losses"; "Wall Street clawed back the
  last of the historic, frenzied losses unleashed by the new coronavirus"; "nearly 34% plunge for the S&P 500 from Feb.
  19 through March 23".
- Use: shares were back at a record six months before the Guild's page said writing incomes "have continued to
  decline". In the 2020 downturn the two fell together and then moved apart.

## 4. The case
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:43-45`: "She will contribute an additional $150,000
  at the beginning of 2028, using earnings from publishing advances, speaking engagements, licensing, and other
  entrepreneurial ventures."
- Note: the case states the deposit as a plan ("will"), not as a risk; the risk is our reading. V57 drops "other
  entrepreneurial ventures", which is fine.

## Verdicts on Felix's point 4
| Claim | Verdict | Why |
|---|---|---|
| Times quote | VERIFIED | Words on the page |
| Guild quote | VERIFIED | Words on the page |
| P5: sources "tend to dry up in the same downturns that hit share prices" | VERIFIED (advances, speaking); licensing unsupported | Two downturns, 2008-09 and 2020; licensing only as film options, 3.4% |
| P5: "Her income already rides on shares, so her portfolio shouldn't bet on them twice" | OVERSTATED | The pages show income falling in recessions, not moving with share prices; in 2020 shares recovered by 18 Aug while writing incomes kept falling |
| Fix (a word, count kept) | "shares" to "booms" (496 strict, checked) | "the economy ... it" reads better but costs one word; with Felix's "bond" fix it would be 498, over the 497 house cap |

## Locked TNA (`keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt`) against V57 (`keel/ips_rewrite/drafts/FINAL/ips.txt`)
| TNA words | V57 words | Verdict |
|---|---|---|
| R1: "remove uncertainty, through duration-matching" | P4: "matching their bonds' average timing to the payments' and rebalancing as rates move ... We do the second" | Real but harmless. P4 describes duration-matching as the road not taken; but R2 describes the road taken (below), so a judge reading both sees the right method under the wrong name. Never write "we don't duration-match" |
| R2: "each of Laura's payments rests on a dedicated instrument (not merely a forecast)" | P4: "buying one bond per payment and holding it" | Agrees |
| IBTM note: "the final payout is not fixed"; R2: "their terminal payout is a net asset value, as opposed to a promise of par" | P4: "A Treasury held to maturity pays exactly what it promised, whatever markets do" (after "Treasury bonds and Treasury funds") | Real clash if read as covering the funds. Backs Felix's fix 1, "A Treasury bond" (497) |
| R2's NAV catch; Note 1: "The 10.5-month gap creates reinvestment-rate risk on the proceeds" | P8: "The ladder's one weakness is that it counts on reinvesting its bonds' interest" | Real, small: the TNA names a second weakness (the funds' payout). Fix: "one" to "main", 0 words. Note 1's gap risk is the same family as P8's |
| R1: "a near-ironclad guarantee" | P4: "high certainty means no payment depends on shares" | Two definitions, compatible (P4 is the test, R1 the standard). Harmless |
| Note 1: "the latest WInS bond available beforehand" | P4: "each maturing before a January payment"; "never needs rebalancing" | Agrees (proceeds parked in a short-term fund are not rebalancing) |
| R1: TIPS not needed | No TIPS | Agrees |
| VT note and R3: shares set only how far the gift rises; "the only investment not standing between Laura and a payment deadline" | P4-P7 | Agrees. R3's "about 7.5% a year (as per JPMorgan)" has no echo in V57 (Book 11: no figures) |
