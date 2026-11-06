# V63: the IPS built from Caplet's own paragraphs

This folder holds V63, the final draft (the same text as `../D43/`). `ips.txt` is the IPS (496 on the strictest count, limit 500); `pitch.txt` is the pitch (49, limit 50).
`../D43/user_text.txt` is the text Caplet wrote by hand on Fri 6 Nov (244 words), which is the base.

**What happened.** On Fri 6 Nov Caplet wrote the only part of V62 it accepts and dropped the rest from the strategy.
V63 keeps those sentences as written (one "it" became "them") and adds only what a reader needs to follow them:
why Treasuries suit fixed payments, how each rung is sized, why price swings don't matter when a holding is kept to
maturity, that the ladder is the operating reserve and needs no change in 2033, and what the world index fund is
for, why it can hold shares, how it spreads risk, and what a fall would cost. Nothing from earlier versions came back.
The pitch was rewritten to match, because the old one described the 2031 range.

**Points for Caplet to decide (not changed in the text):**
1. The trading notes submitted on 23 Oct say IBTM also gives co-sponsors a minimum figure in 2031 and that VT sets how
   far the gift rises above it. This IPS no longer says that, and judges read the notes and the IPS together.
2. The text says no payment is ever at risk. Interest that arrives before 2033 has to wait for the payments; if rates
   fall and stay low it earns less while waiting, and the ladder could come up somewhat short.
3. Wharton asks the IPS to explain how she will decide a responsible facility contribution. The text says the fund
   pays for it but not how much she gives.

**Facts checked.** "About $300,000": $302,163 on the 5 Nov Treasury curve, the newest on file, and $303,269 priced with the bonds and
funds actually held (MODEL, `keel/scripts/ladder_history.py`, `keel/scripts/holdings_ladder.py`; 23 Oct was $297,636).
$500,000 less that is about $197,000, so "roughly $200,000 in interest" holds, and the 2028 deposit would fill a gap of
about $3,300.
The plan matches what is already held in WInS: the ten-rung ladder and VT.
