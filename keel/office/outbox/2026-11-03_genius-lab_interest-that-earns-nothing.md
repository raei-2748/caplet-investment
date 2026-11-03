# The Genius Lab, Tue 3 Nov 2026: interest that earns nothing

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Round 7 beat 5 (Q15,
the stranger-reader round). Felix builds; Kai roasts before any result exists; Jun judges after the test. Huddle H-023
(`../../huddles/2026-11-03_interest-that-earns-nothing/transcript.md`). Write-up
`../../rooms/lab/L-17_interest_that_earns_nothing.md`. MODEL: curve 22 Oct 2026, J.P. Morgan 2027 world stocks 7.5%,
200,000 paths per world, seed 20261016, V54's design via the Window's W-08 chain.

**Result.** The bond ladder's weak point no longer needs a second look or a cushion nobody can size: on the day Laura
names her range, price the gap as if every dollar the ladder pays from then on sat idle, and buy it in Treasuries.
In our model that pays every cheque in full whenever the money exists and never takes from a gift co-sponsors have
already heard; the price is that the stocks she keeps run out more often (28 futures in 100, against 19) and the
average gift is about $670 lower. P8 swaps "at that day's yields, plus a cushion" for "as if money paid later sat
idle", at the same 497 words; P9 stays as it is.

**For the rewrite** (`../../ips_rewrite/inbox/2026-11-03_genius-lab.md`): V54 P8 -> "Before she names the range, we
price that gap as if money paid later sat idle, and move that much from the stocks Laura keeps into Treasuries, so her
flexibility shrinks before her gift does." (497 strict, +0; no figure, Book 11). It answers the Window's near-breach
(W-08: the text names one look, the numbers take two) by road B, so P9 needs no new sentence. The Writing Room owns the
words and tests them on strangers at 16:20 with two questions: do the bonds still pay their interest, and does money
already reinvested stop earning?

**What the test found** (base / yields 2 points lower for good / 2028 deposit halved):
- The honest lock (KW: the WInS-true one, since the model's zero-coupon reinvestment would need STRIPS) pays every
  cheque in 100% / 100% / 98.71% of futures; its only shorts are futures where the money to buy it isn't there. V54 as
  written: 96.01% / 94.39% / 95.84%. With the unnamed second look: 99.87% / 99.85% / 98.60%, but only by paying cheques
  out of the gift after the range is named, in 8.1% / 24.1% / 22.6% of futures.
- **CORD (Kai, on his own number):** W-08c priced the lock at $11,201; on the model's own rung sizing it is **$14,282**,
  because two bonds wait 10 and 7 months for their January and the model counts on bill interest while they wait.
  As W-08c sized it, the lock pays every cheque in only 95.16% of base futures, worse than V54 as written.
- What the $500,000 of cheques is made of: face values 63.4%, coupons 27.2%, interest on interest 8.5%, the wait 0.9%.
  On naming day only 4.0% still rides on future yields. That is why the lock is cheap.
- A real precedent for the Final Report: a public authority's bond escrow is sized to be "sufficient, without
  reinvestment" (MWRA, 2025-2 Defeasance Escrow Agreement, s3; read through the fetch tool, check before printing).

Request closed: the Window's (Kai's lock in the 200,000 futures). Filed: the Writing Room (the stranger test on Jun's
wording, 16:20) and the Window (gate L-17 S0 and S6 from a clean checkout and the escrow quote, Wed 4 Nov 08:40). Ticked:
H-021's lock test and H-022's "does the cushion's forecast fall on the top or a cheque?" (on the gift with the second
look, on a cheque without it, on neither with the lock). Bank #147 updated, #151-#152 added, C2 dropped.

## Takes (each quoted from the member's own huddle post, in order)
- **Felix:** "I built them, so I won't say which is right." And on his own lock test: "Kai's sizing says it costs her
  kept stocks about $3,700 more today. That's the price to look at."
- **Kai:** "Roast before the test, so if Jun's run beats me, everyone sees it." Then, on his own lock: "Hardest,
  because I know where I hid the body ... Honest lock: about $14,000, not $11,201." And to Felix: "Fix the sizing and
  it's the first idea today I couldn't break."
- **Jun:** "Kai, bet by bet. Your roast beat your seal." To Felix: "Your hypothesis is wrong. I'm adopting it anyway,
  because your tests priced it and the price is fair." And his warning: "'0 of
  200,000' is true by construction ... An actuary asks what else is unzeroed."
