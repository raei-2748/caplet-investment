# Session summary: cloud session, Thu 5 Nov 2026 (Sydney)

Branch `claude/sleepy-euler-xqnclv`. IPS due Sat 7 Nov 09:00 Sydney (Fri 6 Nov 5 pm ET).

## 1. First rewrite of V57 (stop-slop + writing-process)
Ray pasted V57 (the FINAL, `keel/ips_rewrite/drafts/FINAL/`) and asked for a rewrite with the stop-slop and
writing-process skills. Same ideas, cleaner wording: removed the "not X, Y" flips, quotable lines, "Nor do we...",
"to us", and the tablet one-liner ending. Pitch 48, IPS 495. Superseded by section 3.

## 2. New rule (Ray), committed and pushed
Ray banned the detector check and the draft label (row **I85** in `keel/INSTRUCTIONS.md`; rule at the top of the
every-session section of `CLAUDE.md`; the old instructions for both removed from `CLAUDE.md`). Older files that still
mention them are history, not instructions.
- PR: https://github.com/raei-2748/caplet-investment/pull/149 (draft, check green, mergeable). **Needs merging to main**
  for the rule to reach every session.

## 3. Second rewrite: "the IPS is still very weak" (palumbo-voice + stop-slop), then an official-rules check
Rebuilt around one central idea instead of a run of mechanisms (answers Ray's I84: creativity in the strategy, not
the metaphor): **a dollar with a fixed job goes into Treasuries that mature in time to do it; a dollar without one
goes into shares; the mix changes only when money takes on a new job (2027, 2028, 2031, 2033), never because markets
move.** Pitch 49 words; IPS 495 (499 split on hyphens). Not yet in the repo.

### Pitch
Each dollar with a fixed job goes into Treasuries maturing in time: Laura's first $300,000 for the ten $50,000 operating payments, her 2028 deposit for any shortfall and a minimum facility contribution. Only money without a job sits in world shares, where it can grow her contribution and flexibility.

### IPS
From 2033 Laura's portfolio has to pay $50,000 each January for ten years, with a high degree of certainty and no outside money, and what she then gives the facility must leave her flexibility. One rule runs the strategy: a dollar with a fixed job goes into Treasuries that mature in time to do it, and a dollar without one goes into shares. Her money takes on new jobs in 2027, 2028, 2031 and 2033, so its mix changes then and never because markets move.

We take high certainty to mean no payment, when it falls due, depends on shares. Shares can stay down for years, and payments can't wait. The risk is sharper for Laura, since her 2028 deposit comes from publishing advances, speaking and licensing, which can dry up in the downturns that sink shares.

In 2027 her first $300,000 buys a ladder of ten Treasury holdings, five bonds and five fixed-date Treasury funds, one maturing before each payment. Pension funds either match only the average timing of their bonds to the payments, rebalancing as rates move, or match each payment with its own bond and hold it; we chose the second, since bonds held to maturity pay known sums, and fixed-date funds nearly so, with no trading.

In 2028 the second deposit first completes the ladder if yields have fallen. Most of the rest buys more of the December 2032 Treasury fund, whose payout becomes her minimum contribution. The remainder, roughly the interest that fund will earn, goes into one world index fund of thousands of companies. Banks sell the same mix as a capital-protected note but spend the interest on an option that can expire worthless; Laura owns the shares instead. We assume 7.5% a year from them, J.P. Morgan's 2027 estimate for global shares, and no payment relies on it. That gives up some growth for a client willing to take thoughtful risks, but if shares fall, only her contribution shrinks. Our WInS portfolio holds this mix, scaled to $300,000.

In 2031 Laura names a range to co-sponsors, and the top becomes a commitment once they plan around it. The bottom is the 2032 fund's payout rounded down, money she already owns; the top adds half her shares, which we move into Treasuries before she names it. The ladder's weakness is that its later payments count on reinvesting interest, which low rates would cut, so we price the gap as if every dollar waiting for a payment earned nothing and move that amount from the half she keeps into Treasuries. If that half can't cover it, she names a lower range. The rest stays invested and liquid, a cushion if the building costs more in Taiwan dollars.

In 2033 she gives the facility the 2032 fund's payout and the half moved in 2031. The ladder and the Treasuries bought for the gap become her operating reserve, losing a holding each year as it matures, since no Treasury is sold early.

### Independent check (a separate agent read it against the IPS instructions, case, Guide, criteria page, Week 4/5 emails, the submitted TNA lines and the 23 Oct WInS snapshot)
- **Hard rules: pass.** Within limits; no charts, links or citations; only permitted holdings (Treasury bonds,
  fixed-date Treasury funds, one world stock fund); no individual TIPS/STRIPS, derivatives or margin; no "floor",
  "gift", "cheque" or "promises".
- **Fixed after the check:**
  - Pitch overclaim (ladder fits under $300k by only $2,364 on the 23 Oct curve): now says the 2028 deposit covers "any shortfall".
  - "No payment depends on shares" clashed with covering the reinvestment gap from shares: the gap money now moves into Treasuries, and the definition reads "when it falls due".
  - TNA Note 1 credits "duration-matching": the pension sentence now chooses the stricter form (one bond per payment) instead of rejecting matching.
  - "A bond pays what it promised" doesn't hold for iBonds funds (TNA Note 2: payout "not fixed"): now "fixed-date funds nearly so".
  - WInS holds VT now while the IPS adds shares in 2028: added "Our WInS portfolio holds this mix, scaled to $300,000."
  - Wording: "Banks sell the same mix", "the Treasuries bought for the gap" (was a coined label), "five bonds and five fixed-date Treasury funds".
  - 7.5%: the checker flagged it against the JPM 2026 table (ACWI 7.00%). Kept, because the office confirmed JPM's 2027 report says global equity 7.5% on p. 8 (`keel/pm/REQUESTS.md`, 25 Oct). Now named as "J.P. Morgan's 2027 estimate for global shares", matching the submitted TNA.
- **Still thin (left out for word count):** liquidity and diversification (one line each); why "half" the shares go into the range; the range's confidence and how good or bad markets would move it (the instructions leave these to the Final Report).

### Caplet's calls
1. The tablet image, the name Caplet XR, portfolio insurance and the 1987 crash were cut to fit the fixes (in line with I84). Bringing the name back costs about 15 words.
2. Explaining why half the shares go into the range costs about 20 words.
3. Whether to file this as V58 next to `keel/ips_rewrite/drafts/FINAL/` (not yet done).

## Files
- Drafts (this cloud session only): `scratchpad/v2/pitch.txt`, `scratchpad/v2/ips.txt` (full text copied above).
- Repo changes: `CLAUDE.md`, `keel/INSTRUCTIONS.md` (PR above).
