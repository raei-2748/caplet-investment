# Genius Lab memo, Mon 26 Oct 2026: the dedicated ladder holds up in 200,000 paths (WO-R1, L-09)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. For Nora's 07:00 brief.

**Result (MODEL, 15 Oct curve).** Sizing Laura's ladder from 2042 backwards, so the long bonds' coupons pay the early
payments, cuts the coupon-reinvestment tail almost in half: p95 shortfall $25,112 -> $14,832, p99 $32,429 ->
$17,584, for $1,486 more on 1 Jan 2027. Audit: the old ladder reproduces R01 exactly and the number sheet's p95
within $364. Residual risk: $85k of pre-2033 coupons waiting in short Treasuries (worst one-year gap $7,923).
**Asks.** Courtroom (WO-R2): does an IPS that sizes this way clash with a WInS book left as it is? Caplet: re-size
WInS (~10 trades, ~$52k each way, Ray only)? Default: no trades. Writing Room: the one true line, if WO-R2 clears it.
Write-up `../../rooms/lab/L-09_dedicated_ladder.md`; rewrite inbox `../../ips_rewrite/inbox/2026-10-26_genius-lab.md`.

Jun: Hypothesis said a third, the paths said almost half. I'd still rather the Courtroom shoot at it before anyone
falls in love – a $1,500 fix that needs ten trades in the last week is a fix with a catch.

Kai: I said they'd moved the leak, not plugged it, and the $85k sitting in cash before 2033 says I was right. I also
said the tail wouldn't move. It moved forty per cent. Half a win, and I'm taking the half I like.
