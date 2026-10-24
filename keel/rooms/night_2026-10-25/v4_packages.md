# FICTION (the room) + real drafts. Writing Room, Sun 25 Oct 2026: IPS v4 packages on v3.1
AI DRAFT (Claude, 25 Oct 2026). Suggestions only; the IPS Report doc was not touched. Caplet rewrites in its own words and decides.

Keel is a simulated team, AI-written (Tess cuts and counts; Amara drafts). Base: `v3_1_pitch.txt` (37 strict) and
`v3_1_ips.txt` (489 strict). Files: `v4/` (ten .txt files, exactly as counted). Counts by
`python3 keel/office/tools/textcheck.py FILE --limit 500` (or `--limit 50`). No new numbers, no strategy change, no
banned words; both en dashes kept (P2, P3); no em dash, no question mark in any text.

## 1. Change log, v3.1 to P0 (469 strict)
| # | Old words (v3.1) | New words (P0) | Reason | Strict words | Source room |
|---|---|---|---|---|---|
| 1 | "The rest buys a global index fund of thousands of companies." | "The rest, the interest that ETF will earn, buys a global index fund of thousands of companies." | S1. The stocks are paid for with the floor ETF's interest, not with principal; exact by construction (fund = ETF's gain to maturity). It also explains why the refused trade is refused. Says "the rest" of the remainder, not of the deposit | +6 | Genius Lab, L-07 rung 2 (Sonnet) |
| 2 | "A stock fall after 2031 moves the gift toward the floor she already owns; any rise stays with Laura." | "Stocks ending below their 2031 value move the gift toward the floor she already owns; anything above it stays with Laura." | S2. v3.1 overclaimed: a recovery after a post-2031 fall lifts the gift (23% of model paths). The new line is true both ways and names the cap's reference point | +2 | Genius Lab, L-07 rung 2 |
| 3 | "that sum is Laura's facility floor." | "that ETF's payout is Laura's facility floor." | Defines the floor once as what the ETF pays out, not what goes in (the co-sponsor's "which sum?"). Laura's Room's wording "what that ETF pays out" counts +3 strict, not the +1 it was logged at; "that ETF's payout" says the same at +1 | +1 | Laura's Room |
| 4 | "This is the obvious trade." | (cut) | Whole idea now carried by S1: the reader can see that moving floor money into stocks means spending principal. The concede-then-turn survives ("would raise the expected gift. But...") | -5 | rung 2 / v3.1 cut menu |
| 5 | "Each payment's cash comes from a maturity, not a sale." | (cut) | Said already in the sentence before it ("maturing before it"), in the pitch ("held to maturity") and in the trading rule. Cost, stated plainly: it was the outsider judge's favourite line (L-05 Courtroom asked Caplet to vote on this cut on purpose). Package B restores it as its touch | -10 | rung 2 |
| 6 | "Our WInS portfolio shows this allocation, scaled down." | (cut) | Checked against the official IPS text: "Your portfolio and Final Report should reflect the strategy established in your IPS" binds the portfolio, not the IPS wording; the Final Report is where "how effectively it implemented that strategy" is judged. Not required in the form | -8 | rung 2 (requirement check: Writing Room) |
| 7 | "from the floor, quoted at the 2032 ETF's projected payout rounded down, to" | "from the projected floor, rounded down, to" | With edit 3, "the 2032 ETF's payout" is the floor's definition said a second time (Laura's Room: P4 "then repeats a definition"). The repeat goes; "projected" (rung 2 caveat) and "rounded down" (the credibility rule) stay | -6 | Laura's Room + rung 2 caveat |
| - | Kitchen harvest | none adopted | See below | 0 | Kitchen |
Net: 489 + 6 + 2 + 1 - 5 - 10 - 8 - 6 = **469**. Pitch unchanged (37).

**Kitchen, line by line (the three closest).** Felix's #6 ("It means I can list what can go wrong") is how v3.1's
certainty sentences already work, and the spoken form adds words. Tess's #13 ("a number she's already told people")
costs +1 and swaps "quoted", the word the range uses everywhere, for a synonym. Jun's #14 ("good for someone who owes,
bad for someone who has to buy a future") is the best sentence in the Kitchen and replaces nothing: it would sit on
top of "hurts twice" for about 18 more words. Jun's #15 is false in this text ("doesn't touch the payments at all"
contradicts "Only reinvested coupons... can leave one short"). So no Kitchen line passed all three tests (replaces a
sentence, true as said, adds no words). Jun's line belongs in the Final Report or the finale, said aloud.

**Official requirements checked before cutting** (`2026_WGY_Investment_Policy-FINAL.txt`): reserve composition over
time (kept: "renamed rather than rebuilt: five Treasury ETFs... five bonds"); planned changes as needs approach (kept:
trading rule, 2033 sentence); flexibility (kept: inflation/FX sentence); protect the operating payments (kept: the
certainty definition and its short list). The WInS tie is not an IPS-text requirement. The annual review is not
required either, but nothing in the official text makes it redundant ("make disciplined decisions during changing
market conditions" is what it schedules), so it stays in all five.

## 2. The cuts, and why each was a whole idea
- **P0 (all five texts):** edits 4-7 above. Each removes an idea stated somewhere else in the same pitch and IPS, or
  (WInS) one the official text puts on the portfolio rather than the form. No sentence was squeezed shorter.
- **The motif's price (A, B and C only).** A name plus two touches costs 28-34 words over P0 (A +28, B +34, C +29),
  so every package also takes the same two cuts, so they stay comparable:
  1. **The second objective's preview.** "The second objective is a facility contribution with a floor Laura can quote
     to co-sponsors and growth above it." becomes "The second objective is a responsible facility contribution." (-12).
     The floor, the growth above it and the quote to co-sponsors are each said in full in P3-P4 and in the pitch;
     "responsible" is the official text's own word. **Cost:** "the floor" now appears one sentence before it is
     defined (P3, "lowers the floor, not a payment"). A careful reader resolves it in the next line, but it is a cost.
  2. **The coupon-and-cash sentence.** "Coupons and early maturities wait in a short-term Treasury ETF; coupons then
     buy more of the holding that paid them." (-21). Half of it repeats P1 ("reinvested coupons"); the rest is
     mechanics the official text steers away from ("rather than describing individual investments"). Gemini's point 7
     cannot come back, because no sentence left says how a coupon buys a bond. **Cost:** where early cash waits is no
     longer said; the Final Report must say it.
  - Not chosen instead: "A lasting fall in yields hurts twice" (-20). It repeats P3 and P1 in part, but it is the
    only line that says one risk reaches both halves of the plan, and it is A's touch, so cutting it would make the
    packages unequal.
- **Package-specific:** B puts back edit 5 ("Each payment's cash is released by a maturity, not a sale.", its touch 1).
  Nothing else differs beyond each package's name, two touches and closing line.
- **Kai's amendments, still applied:** A uses the name as a label ("our Press Day plan", pitch and P3); B's kicker
  reads "No payment Treasury is sold to raise cash." (consistent with v3.1's trading rule: swapping a delisted holding
  for an earlier Treasury is a swap, not a sale to raise cash, and investing the 2028 deposit sells nothing); C reads
  "Our pre-registered plan buys" and its kicker ends "It makes the range believable, which co-sponsors need in 2031."
  v3's "so she never gives more than she quoted" appears nowhere.
- **Pitches** are ported onto v3.1's pitch (not v3's binned "fund the building without paying to run it"): A and C add
  only the name (C also its closing rule line); B adds the name and its one-line simile; D adds the name.
- **D's name, "Maturity Match"**, is plain and describes the payment half only: no ladder, rung, floor-and-fund,
  certainty word, cap or collar, nothing botanical or nautical. Not a recommendation. **Note for the Courtroom:** D is
  P0 plus a name, as briefed, so it keeps the 33 words the packages gave up. Scoring A/B/C against D measures the
  motif plus that loss, not the motif alone.

## 3. Counts (strict; by spaces in brackets)
| Text | Pitch (limit 50) | IPS (limit 500; cushion 470) | Non-ASCII | Overclaim words |
|---|---|---|---|---|
| v3.1 (base) | 37 (36) | 489 (484) | 2 en dashes | 0 |
| P0 Plain v4 | **37** (36) | **469** (464) | 2 en dashes | 0 |
| A Press Day | **40** (39) | **464** (461) | 2 en dashes | 0 |
| B Caplet XR | **49** (47) | **470** (466) | 2 en dashes | 0 |
| C Pre-Registered | **48** (46) | **465** (458) | 2 en dashes | 0 |
| D No motif | **38** (37) | **470** (465) | 2 en dashes | 0 |
All ten pass. B's IPS sits exactly on 470 and its pitch has one word of margin; C's pitch has two.

## 4. The five texts
### P0 Plain v4 ([NAME] placeholder)
**Pitch**

Laura's ten $50,000 operating payments cannot lean on co-sponsors, so [NAME] buys them first, in Treasuries held to maturity. More Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift.

**IPS**

This policy governs Laura Gao's $450,000 for her 2033 Taiwan residency. Its first objective is to fund ten $50,000 operating payments, each January of 2033-42, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a facility contribution with a floor Laura can quote to co-sponsors and growth above it.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

[NAME] buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that ETF's payout is Laura's facility floor. The rest, the interest that ETF will earn, buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range from the projected floor, rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top. Stocks ending below their 2031 value move the gift toward the floor she already owns; anything above it stays with Laura.

Moving floor money into stocks would raise the expected gift. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hurts twice: the payment Treasuries cost more in January, and their coupons earn less afterwards. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Until 2033 we trade only to invest the 2028 deposit or to swap a delisted holding for an earlier Treasury. Coupons and early maturities wait in a short-term Treasury ETF; coupons then buy more of the holding that paid them. Each January we review the plan with Laura. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42.

### A Press Day
**Pitch**

Laura's ten $50,000 operating payments cannot lean on co-sponsors, so our Press Day plan buys them first, in Treasuries held to maturity. More Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift.

**IPS**

This policy governs Laura Gao's $450,000 for her 2033 Taiwan residency. Its first objective is to fund ten $50,000 operating payments, each January of 2033-42, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a responsible facility contribution.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

Our Press Day plan buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that ETF's payout is Laura's facility floor. The rest, the interest that ETF will earn, buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range from the projected floor, rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top. Stocks ending below their 2031 value move the gift toward the floor she already owns; anything above it stays with Laura.

Moving floor money into stocks would raise the expected gift. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hits like dearer paper on a print run: hardest in January, our press day, when the payment Treasuries cost more, then again as their coupons earn less. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Until 2033 we trade only to invest the 2028 deposit or to swap a delisted holding for an earlier Treasury. Each January we review the plan with Laura. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42. After press day, the payment Treasuries should be the dullest thing Laura owns.

### B Caplet XR
**Pitch**

Laura's ten $50,000 operating payments cannot lean on co-sponsors, so Caplet XR buys them first, in Treasuries held to maturity. Like an extended-release pill, they release one payment each January. More Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift.

**IPS**

This policy governs Laura Gao's $450,000 for her 2033 Taiwan residency. Its first objective is to fund ten $50,000 operating payments, each January of 2033-42, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. Each payment's cash is released by a maturity, not a sale. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a responsible facility contribution.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

Caplet XR buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that ETF's payout is Laura's facility floor. The rest, the interest that ETF will earn, buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range from the projected floor, rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top. Stocks ending below their 2031 value move the gift toward the floor she already owns; anything above it stays with Laura.

Moving floor money into stocks would raise the expected gift. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hurts twice: the payment Treasuries cost more in January, and their coupons earn less afterwards. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Until 2033 we trade only to invest the 2028 deposit or to swap a delisted holding for an earlier Treasury. Each January we review the plan with Laura. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42. Like any extended-release caplet, the plan comes with one instruction: do not crush. No payment Treasury is sold to raise cash.

### C Pre-Registered
**Pitch**

Laura's ten $50,000 operating payments cannot lean on co-sponsors, so our pre-registered plan buys them first, in Treasuries held to maturity. More Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift. Her 2031 range follows a rule written now.

**IPS**

This policy governs Laura Gao's $450,000 for her 2033 Taiwan residency. Its first objective is to fund ten $50,000 operating payments, each January of 2033-42, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a responsible facility contribution.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

Our pre-registered plan buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that ETF's payout is Laura's facility floor. The rest, the interest that ETF will earn, buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range, set by this pre-registered rule: from the projected floor, rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top. Stocks ending below their 2031 value move the gift toward the floor she already owns; anything above it stays with Laura.

Moving floor money into stocks would raise the expected gift. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hurts twice: the payment Treasuries cost more in January, and their coupons earn less afterwards. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Until 2033 we trade only to invest the 2028 deposit or to swap a delisted holding for an earlier Treasury. Each January we review the plan with Laura. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42. Pre-registering a rule does not improve the result. It makes the range believable, which co-sponsors need in 2031.

### D No motif (control name: Maturity Match)
**Pitch**

Laura's ten $50,000 operating payments cannot lean on co-sponsors, so Maturity Match buys them first, in Treasuries held to maturity. More Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift.

**IPS**

This policy governs Laura Gao's $450,000 for her 2033 Taiwan residency. Its first objective is to fund ten $50,000 operating payments, each January of 2033-42, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a facility contribution with a floor Laura can quote to co-sponsors and growth above it.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

Maturity Match buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that ETF's payout is Laura's facility floor. The rest, the interest that ETF will earn, buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range from the projected floor, rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top. Stocks ending below their 2031 value move the gift toward the floor she already owns; anything above it stays with Laura.

Moving floor money into stocks would raise the expected gift. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hurts twice: the payment Treasuries cost more in January, and their coupons earn less afterwards. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Until 2033 we trade only to invest the 2028 deposit or to swap a delisted holding for an earlier Treasury. Coupons and early maturities wait in a short-term Treasury ETF; coupons then buy more of the holding that paid them. Each January we review the plan with Laura. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42.

## 5. Tess's note
I wouldn't cut the annual review, "No stock has to rise" or the line about a fall in yields hurting twice, because
each is the only place the IPS says that thing. The maturity line went because the sentence before it already says
it; the outsider judge loved it, and B gets it back. The motif isn't free. Every package paid about thirty words for
it, and if Monday thinks that's too dear, the answer is P0, not a package squeezed until it fits.
