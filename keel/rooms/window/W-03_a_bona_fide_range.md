# W-03: a range a regulator would call honest (The Window, Fri 30 Oct 2026, round 3 beat 2)

AI-generated (Claude Code). (Keel is a simulated team, AI-written.) Felix's own primary-source find for Q10, "why a
range, and what each end costs". Scout format: claim, source, quote, breaks first, mechanism, could touch, ninety-second rule.

## The find
**The SEC decides how wide an IPO price range may be before it stops counting as a range, and it lets the final price
land outside the range only within a stated tolerance.**

- **Width.** SEC Compliance and Disclosure Interpretation 134.04 (Regulation S-K, Item 501(b)(3)), 16 May 2013, read in
  PwC Viewpoint's mirror of the SEC text,
  https://viewpoint.pwc.com/dt/us/en/sec/cdis/cdis_US/regulation_sk_US/Questions_and_Answers/Section_134_Item_501.html,
  accessed 30 Oct 2026 (sec.gov itself not reached from here). Quote (verified): "For initial public offerings, a price
  range in excess of $2, for offerings up to $10 per share, or in excess of 20% of the high end of the range, for
  offerings over $10 per share, will not be considered bona fide."
- **Tolerance.** 17 CFR 230.430A, Instruction to paragraph (a), Cornell LII, https://www.law.cornell.edu/cfr/text/17/230.430A,
  accessed 30 Oct 2026. Quote (verified): "any increase or decrease in volume (if the total dollar value of securities
  offered would not exceed that which was registered) and any deviation from the low or high end of the range may be
  reflected in the form of prospectus filed with the Commission pursuant to Rule 424(b)(1) ... if, in the aggregate, the
  changes in volume and price represent no more than a 20% change in the maximum aggregate offering price".
  Also (a)(3): the omitted price information must be filed within "fifteen business days after the effective date".
  So the scouts' "Rule 430A tolerance" is no longer UNVERIFIED: it is 20% of the maximum aggregate offering price, in
  volume and price together, not 20% of the share price.

## Breaks first (LS-04)
An IPO range is a forecast made *before* demand is known, and the book then sets the price inside it or outside it
within weeks; a price below the range is the issuer's loss, not a broken promise to anyone. Laura's bottom is a
promise and is never allowed to be missed (0 of 600,000 MODEL paths below it once quoted, L-12). So the SEC rule fits
only the *width* and the *top*: her top is a forecast like an IPO range; her bottom is not. A judge would see at once
that an IPO range has no floor anyone has bought.

## Mechanism
A regulator thinks a range carries information only if it is narrow. Too wide ("$10 to $30") and it says nothing, so
it is not "bona fide"; the 20% cap forces the issuer to commit to a view. Then, because forecasts miss, the same rules
say in advance how far the final number may stray without starting again.

## Could touch
- **The range's why (F8, B3 para 13).** The range is not a hedge; it is the narrowest honest statement of what she owns
  and what she hopes. Laura's width is set by the design: half the stocks that day, over a top of floor + half. With the
  stocks about one dollar in fifteen (R06, 6.5-7.1% to 2032, MODEL) the width is roughly a tenth of the top, inside the
  SEC's 20% in the typical path; a boom widens it. **UNVERIFIED in our own model:** the share of paths where
  (top - bottom) > 20% of the top has never been counted (request to the Genius Lab, Fri 30 Oct).
- **FR, Client Knowledge:** "the range we hand co-sponsors would pass the test the SEC applies to a share float's
  price range" is a line a finance judge can check on sight, if the Lab's count supports it.

## Ninety-second rule
"A range is honest only if it's narrow enough to mean something – ours is the floor she owns, plus half of what she hopes."

## Also gated for today's scouts (not Felix's find; handed over)
- **Kai's rain range: the 50% / 25% pairing is FALSE.** Bureau of Meteorology, "Right as rain: How to interpret the daily
  rainfall forecast", issued 15 May 2026, updated 21 May 2026,
  https://www.bom.gov.au/news-and-media/right-as-rain-how-to-interpret-the-daily-rainfall-forecast, accessed 30 Oct 2026.
  Quote (verified): "The first number has a high (75%) chance of occurring, while the second number has a low (25%)
  chance of occurring." The 50% is shown separately ("the medium (50%) chance"), and "amounts of rain outside of this
  range are still possible." So the bottom of a BoM range is a 75% number and the top a 25% number; Laura's bottom is a
  ~100% number and her top an ~85% one (86.6% S0, 84.8% S1, 44.0% S6, L-12, MODEL). Her range is far more cautious than
  the weather's, except when yields fall for good (S6).
