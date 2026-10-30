# Panel 1 (new design), Fri 30 Oct 2026: six judges, six blind entries

AI-generated (Claude Code). Design: `../README.md`. Entries: V31 (fresh rewrite, `drafts/D11`), V29, V25, and three
simulated rivals of different strategies (A09 "Promise First, Then Grow", the field's default plan in plain student
prose; H19 the near-twin; H03 a 70% -> 30% stock glide path). Each judge saw a different random order, only Wharton's
word and the case, and no note from us. Key: `KEY.json`; rankings: `rankings.json`.

| Judge | Model | Ranking (1st -> 6th) |
|---|---|---|
| J1 skimmer | Haiku | V31 > V29 > V25 > A09 > H19 > H03 |
| J2 growth hawk | Sonnet | A09 > H19 > V25 > V31 > V29 > H03 |
| J3 actuary | Opus | V25 > V29 > V31 > A09 > H19 > H03 |
| J4 teacher | Sonnet | A09 > V31 > H19 > V29 > V25 > H03 |
| J5 professor | Fable | V25 > V29 > V31 > H19 > A09 > H03 |
| J6 programme manager | Haiku | V25 > V31 > V29 > A09 > H19 > H03 |

**Agreement: mean Kendall tau 0.34** (pairs range from -0.20 to +0.87). Three different entries came first (V31, A09,
V25). The only unanimous call is H03 last: every judge said a glide path that keeps stocks in the reserve does not
deliver "a high degree of certainty". That agreement is about the case, not about taste, so the panel passes the
Commandment IX test (mean tau under 0.6, more than one #1, different reasons).

Mean rank: V25 2.33 · V31 2.50 · V29 3.00 · A09 3.17 · H19 4.00 · H03 6.00.

## What each judge actually rewarded (their reasons, not ours)
- **J1 (one read, non-specialist):** V31 first: "one promise, one hope" is a plan she could explain to a friend; the
  career-is-a-stock point ties it to Laura; marked down for no confidence on the range and light numbers.
- **J2 (growth):** the plain 80%-stocks rival first. All three of ours "protect against a risk the case does not ask her
  to avoid" and leave a risk-taking client "with a nearly-bond portfolio". Wants the upside given away stated.
- **J3 (actuary):** V25 first because it "defines high certainty by naming the joint stress that breaks it". V31
  "asserts the safety rather than testing it"; unclear whether the coupon cushion protects the cheques or the gift.
- **J4 (teacher):** the plain rival first because it "sounds like students explaining what they decided"; V31 second,
  "the deepest understanding of Laura" but "a little too neat, with headings and refrains". V29 "reads more like a
  product spec than a team explaining itself".
- **J5 (originality):** V25 > V29 > V31, the three share "the best ideas in the set" (career as equity, the note
  without the bank, the capped range as a one-sided bet, the named weakness); V25 wins on the sceptic answered and
  certainty by failure condition. Wants Laura's risk appetite given "a place in the design instead of arguing it away"
  and "rough dollars".
- **J6 (instructions):** V25 first (certainty defined, a number on the range, the strongest objection answered); V31
  "the easiest to follow" but "leaves the certainty claim undefined".

## What Keel did with it (V32, `drafts/D12`)
Kept V31's plain, readable shape (J1, J4, J6). Brought back V25's two analytic wins (certainty by its breaking point;
the sceptic's "ten one-year bills"), which three judges named. Added a confidence for the top (about 97 in 100, MODEL,
with the lock and the coupon set-aside), the coupon leak in one plain sentence (J3), the honest cost against a
balanced portfolio (J2: "richer on average, a broken promise one time in four", Model Suite M7), and a place for
Laura's appetite for risk ("the residency is the boldest bet of her life", J2, J5). Dropped the four headings and
refrains (J4, J5). Not taken: J2's 80% stocks (it breaks a promise about one time in four in our model) and J4's wish
for a plainer, list-like voice (Caplet asked for our own voice; the teacher's point is to stay clear, not to go flat).
