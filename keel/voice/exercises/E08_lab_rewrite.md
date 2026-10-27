# E08 · Rescue a Genius Lab finding: L-10 "last in line", rewritten for a reader

> Exercise, AI DRAFT (Claude, 27 Oct 2026). Practice, not IPS text, not for submission. Brief: same facts as the Lab's
> 27 Oct memo (`../../ips_rewrite/inbox/2026-10-27_genius-lab.md`, points 1-2), in prose a judge would enjoy. Numbers
> are the Lab's MODEL figures (22 Oct curve, 200,000 paths), rounded.

**Before (the Lab's memo, point 1):** "The ten payments are the plan's weakest promise, not its strongest. A payment
comes up short after 2033 in 6.8% of paths (8.4% if yields and stocks fall together), median about $3,200. The gift
leaves in 2033; the coupon leak runs to 2042 with only Laura's kept half (in stocks) behind it."

**After:**

We had assumed the payments were the safe part of the plan. They are not quite – and the reason is a matter of timing rather than of risk.

The facility gift leaves in 2033. The payments run until 2042. In between, the coupons from Laura's later bonds have to be reinvested at whatever rates the 2030s happen to offer, and if those rates are low the last few cheques come up a few thousand dollars light. In our model that happens about once in every 15 futures, and the typical gap is around $3,200.

A few thousand dollars is not a disaster. A missed payment is, because the case says nobody else may pay it.

So we borrowed a rule from the people who package loans into bonds, where the senior investors are paid before anyone junior sees a cent. Before a single dollar goes to the facility in 2033, the plan checks that the payments are covered with $10,000 to spare. If they aren't, the gift waits its turn. In the model, that one rule takes the chance of a short payment from about 1 in 12 to about 1 in 10,000 – and leaves the typical gift exactly where it was.

## Critique
- **What changed:** the finding now has a story (we were wrong about which part was safe), a mechanism a judge can
  follow (the gift leaves early, the coupons keep needing a home), a one-line paragraph that says why it matters, and
  a borrowed rule explained by what it does, not by its acronym ("CLO coverage test" became "the people who package
  loans into bonds"). Numbers fell from nine to five, each rounded and each doing a job.
- **What stayed true:** 6.8% ≈ 1 in 15; 8.4% (the worse case) ≈ 1 in 12; 0.01% = 1 in 10,000; median gift
  unchanged at about $165k (Lab, point 2). The "1 in 12" quotes the stressed case on purpose, because that is the
  number the rule is built for; the Final Report must say so.
- **Still plastic:** "a matter of timing rather than of risk" is a slightly false distinction (timing *is* the risk).
  Better: "and the reason is a calendar, not a crash." Check that line against the Lab before reuse.
- **Lesson for the Lab:** keep the stamps in the lab file; write the memo's first paragraph as if to a judge. A finding
  nobody can feel is a finding nobody uses.
