# Kai, round 3 research notes (H-014, Sun 1 Nov 2026)

(Keel is a simulated team, AI-written.) Repo lines were read with sed/grep at the file. Web pages were read tonight through
WebFetch, which returns a small model's extract, so quotes are near-verbatim, not checked character by character (LS-09).
Anything not read at a page is marked UNVERIFIED.

## Fight 2: does WHARTON_WORD line 71 support cutting instrument words? No. Kai loses.
- `keel/WHARTON_WORD.md` line 71-72, read: "Focus on the strategy and decision-making framework that guide your portfolio
  rather than describing individual investments or presenting detailed financial calculations."
- V50 (`keel/ips_rewrite/drafts/D30/ips_V50.txt`) names no ticker and no fund. It says "Treasury bonds and funds that mature
  like bonds" and "one world index fund": types, not individual investments. The only line that reads as instrument
  description is the pitch/para 2's "ten Treasuries", which is untrue of five rungs, not a surplus.
- Same page, line 111 (Wharton's tips): "Explain your decisions ... explain why each investment belongs in your strategy".
  s1 (Investment Strategy criterion) ends "maintains consistency with the team's IPS". The TNA and IPS are judged together
  (s1, last line), so the judge holds the TNA beside the IPS whatever V50 leaves out.
- The TNA words a judge holds (`keel/ips_rewrite/00_GROUND_TRUTH.md` s3, locked 23 Oct): reflection 2 says iBonds "behave a
  lot like bonds when held to their end"; "each of Laura's payments rests on a dedicated instrument (not merely a
  forecast)"; terminal payout "is a net asset value, as opposed to a promise of par" (Archive A11 quotes the same).
  IBTM note (`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`): "the final payout is not fixed".
- Result: cutting "funds that mature like bonds" from para 3 would leave a bare "Treasury bonds" ladder beside five fund
  notes. The cut that is also true is F1's swap: "ten holdings" (Archive A11: para 2 0 words, pitch "ten Treasury
  holdings" +1). Say it truly wins; Amara is right.
- CORD (Kai, r2): I used line 71 as if it banned instrument words. It says "individual investments"; V50 has none.

## Fight 3: "not a probability, but a purchase" for 2033-37
- Book 5 (`keel/BIBLE.md` lines 189-222, read): iBonds "are as close to guaranteeing an exact amount at an exact date as it
  gets in the world of investing other than literal T-Bonds"; "'near-ironclad'. If we simply hold the ETF until iShares
  officially shuts it down in mid-December [which we will, every year], we will receive the exact Net Asset Value (NAV) of
  the cash inside ... virtually identical in safety to a direct Treasury maturity, minus the fund's tiny management fee.
  Of course, if we were to decide to manually sell our iBonds shares on the stock exchange BEFORE the final liquidation
  date, we would be exposed to fluctuations, but that's not our strategy anyway. ... it should be concise and direct".
  Standing line, line 397: "No hedging: iBonds held to their December close are near-ironclad."
- So Book 5 settles "exact" and "no hedging" for the funds: Kai's "late half's boast" was wrong on Caplet's terms.
  CORD (Kai, r1 and r2): "pays exactly is the late half's boast" and "'Pays exactly' holds from 2038".
- Book 5 does not settle "not a probability": its word is "near-ironclad", and it carries a condition (held to the
  December close; selling early exposes you to fluctuations). V50 para 3 states neither.
- IBTM summary prospectus, https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf,
  re-read Sun 1 Nov (extract): "The Fund does not seek to return any predetermined amount at maturity or in periodic
  distributions." "Direct obligations of the U.S. Treasury have historically involved little risk of loss of principal if held
  to maturity." (Even the issuer says "little risk", not none.) Net assets "will be distributed to then-current shareholders
  pursuant to a plan of liquidation". The word "par" was not found. Only IBTM read; IBTO-IBTR are Tess's.
- "A purchase" is true for every rung (the fund shares are bought in January 2027). "Not a probability" is stronger than
  Ahaan's "near-ironclad", reflection 1's "near-ironclad guarantee" (GROUND_TRUTH s3) and the issuer's "little risk".
  The true sentence missing is Book 5's own condition for the funds (held to the December close), one clause, not a hedge
  (Book 5 allows it: "concise and direct"). The Window gates the words and the 500 cap.

## Fight 1: is public budgeting needed for the WInS line (pre-mortem 16)? No. Kai loses.
- `keel/pm/PREMORTEMS.md` line 54: the risk is a judge seeing VT in the frozen WInS book beside "first $300,000 buys a
  ladder". Cure listed there: "One clause, strategy words only".
- Already in submitted words: VT note (trade note, filled 7 Oct): "so one cheap fund diversifies Laura's stocks. They only
  set how far her gift rises above her promised minimum." Reflection 3: "VT is where we allow ourselves to be wrong –
  because it's the only investment not standing between Laura and a payment deadline" (Archive A19 row quotes it).
  That is money without a deadline, in Caplet's own submitted words, which is what the Washington SSJR 8208 find says
  ("stocks only for money without a deadline", `keel/loop/TERRITORY.md` line 62; whether voters passed it UNVERIFIED).
- `keel/WHARTON_WORD.md` line 110: "Use WInS to demonstrate your strategy. Your WInS portfolio should reflect the strategy your
  team has developed." Line 111 asks why each investment belongs. `competition/COMPETITION.md` s8: "The WInS portfolio
  mirrors Laura's plan scaled to $300k". V50 para 5 already says the plan holds "one world index fund".
- The IPS needs no source (WHARTON_WORD s2: "sources do not need to be cited in the IPS"), so a budgeting source would
  sit under the draft where no judge can see it. Primary sources carry it.

## The chair's caplet find: does it make the motif true at the source?
- Merriam-Webster, https://www.merriam-webster.com/dictionary/caplet, read Sun 1 Nov (extract): "a capsule-shaped medicinal
  tablet"; "The name Caplets was formerly a U.S. registered trademark." (Also `keel/rooms/night_2026-10-25/library_checks.md` row 1.)
- ISMP Canada, https://safemedicationuse.ca/newsletter/newsletter_NotBeCrushedSplitChewed.html, re-read Sun 1 Nov (extract):
  "Slow-release medicines may be labelled as 'long-acting', 'extended-release', 'controlled-release' or other similar
  terms." "Slow-release tablets are generally intended to be swallowed whole." "If a slow-release tablet is crushed, split,
  or chewed, a large amount of the medicine may be released all at once." "This could cause serious harm." The capsule
  sentence is only "Always check with your pharmacist before crushing, splitting, or chewing any tablet or capsule or
  before opening any capsule." No "XR" or "caplet" on the page.
- A real extended-release caplet with the direction: Tylenol 8 HR Arthritis Pain Extended Release Caplets,
  https://espanol.tylenol.com/products/tylenol-8hr-arthritis-pain, read Sun 1 Nov (extract): title "TYLENOL 8 HR Arthritis
  Pain Extended Release Caplets"; Directions: "Swallow whole; do not crush, chew, split, or dissolve." US product; no
  Australian label read (UNVERIFIED for Sydney).
- Result: "capsule" to "caplet" in V50 paras 2 and 9 makes "labelled do not crush" true at a real label, and puts ISMP's
  "all at once" on the right object (a tablet). It is one word twice. But V50's next sentence, "Break it open and you ruin how
  it works", is a capsule verb (ISMP: tablets are "crushed, split, or chewed"). That sentence needs the source's own reason:
  crush it and the dose arrives all at once. Felix needs no page for the motif.
- Does "all at once" fit selling a rung early? In shape, yes (the schedule goes). In harm, it is "early, at the market's
  price", not "all at once": IBTM prospectus (extract): "sell Fund shares at a time when the market price is at a discount
  to NAV, you may pay significantly more or receive significantly less than the underlying value of the Fund shares";
  Book 5: sell before the liquidation date "we would be exposed to fluctuations". For the five T-bonds an early-sale
  source was not read (UNVERIFIED; Book 5 only).
- Loose wording to give the Window (gate for "true of every rung?"): "selling it before its January" is loose: every rung
  matures before its January (Trading Note 1: Feb-2037 bond, "10.5-month gap"; May-2038 note: 7.5 months; Nov-2039 note: "47 days
  before"; funds close in December). "Before it matures" is true of all ten.

## Votes
- Fight 1: primary sources (VT note, reflection 3, line 110); no budgeting.
- Fight 2: say it truly ("ten holdings"; "caplet"); not "say less".
- Fight 3: keep "a purchase"; add Book 5's condition (held to the December close) for the funds; drop "not a probability" only if the Window cannot find the words.
