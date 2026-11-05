# R09 review (e): facts and locked record

AI-generated (Claude, 5 Nov). 02c = `harvest/02c_library_models_record.md`; Oct = `keel/rooms/archive_checks/2026-11-05_what_october_allows.md`; arch = `keel/rooms/archive.md`. Re-runs on the 23 Oct curve: the ladder costs $297,636 (headroom $2,364, matching GT:87-95); in the 2028 fund, $117,641 grows to $150,000, leaving a share slice of $32,359 (MODEL).

| # | Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|---|
| 1 | "each redeemed, or repaid by the US government, in the year before the January" (P1) | HALF-TRUE | The timing holds for all ten (snapshot:22-31; 02c:242), but the gloss fits only the five bonds: the funds pay NAV, "not fixed" (02c:38, :42-43, :66) | Each holding ends before its January. Five are funds paying their value, not a government promise |
| 2 | "Shares nearly always beat Treasuries over ten years" (P2) | FALSE | Below the Treasury rate about 4 in 10 (02c:265, MODEL); shares win 79-86% of paths (`keel/models/results/suite_results.json:1624,1629`); at 7.5% v 5.00%, ~1 in 3 lose (my calc) | Usually, not nearly always |
| 3 | "with shares mixed in ... swing harder than the share market itself" (P2) | HALF-TRUE | Size, not mixing, decides it: the leftover swings harder only when share dollars exceed it (any shares in 2027; over ~33% from 2028, MODEL). True for 60/40 (~1.8x); false for R09's ~7% (~0.2x) | A large share weight beside fixed payments magnifies the leftover's swings |
| 4 | "a payment could fail only if the US government missed one of its own" (P2) | CLASHES WITH RECORD | It is C10's twin (Oct:41). The funds are "not fixed"; Refl. 1 says "near-ironclad" (02c:31, :84); reinvested coupons are a named risk (:93), and R09's own P5 says so | Payments rest on Treasuries already bought; the leftover risks (NAV, reinvested interest) are priced at worst and set aside |
| 5 | "tops up ... if falling yields made them cost more than $300,000" (P3) | HALF-TRUE (timing) | The cost that matters is the January 2027 build: "by January" (IBTR, 02c:56-58) | It tops up whatever the first $300,000 couldn't buy in January 2027 |
| 6 | "priced to grow back to roughly the whole deposit" (P3) | HALF-TRUE | Only with no top-up; after one the minimum is "smaller" (02c:270, :239) | It grows back to about what's left of the deposit after any top-up |
| 7 | "the worst they can do is hand back her deposit" (P3) | HALF-TRUE | False after a top-up (#6), or if shares hit zero after rates fall, since the gap then comes off the floor (R09 P5; arch:101) | At worst: the deposit, less any top-up and any interest gap |
| 8 | Bottom "is what the 2032 fund will pay" (P4) | HALF-TRUE | "Rounded down ... not fixed" is TRUE (02c:248); the flat "is" is undone by P5 and #6 | The bottom: the payout, less any top-up and gap, rounded down |
| 9 | 2031 order: half the shares to Treasuries (P4); the gap "from her shares" (P5) | HALF-TRUE; STRAINS VT note + Refl. 3 | FINAL and the tested design use the *kept* shares (arch:101; `drafts/FINAL/ips.txt:13`); R09 drops "kept" and the order. Dated and into Treasuries, so no C2 breach (Oct:33; arch:87). No WInS T-bond matures 2031-35 (`competition/COMPETITION.md:112`), so these are funds | The gap comes from the kept half, before naming |
| 10 | "ten years of running costs are already bought, so the building ... won't stand empty" (P4) | FALSE | Her $50k goes "toward" running costs, and co-sponsors may add more (case:85-86, :88). Being used isn't about money | Her share of ten years' running costs is paid for |
| 11 | "every overrun would become a claim on it" (P6) | HALF-TRUE | Theory: keep "tends to" (02c:264) | Could, not would |
| 12 | "it stays her flexibility" (P6) | HALF-TRUE | The kept shares are gone by 2033 in about 28 in 100 futures (A33 rule 3, arch:101) | What the gap leaves |
| 13 | "From 2033 the ten holdings are her operating reserve" (P6) | FALSE (omits) | FINAL `ips.txt:15`: "the ladder and the money set aside". The case asks for size and composition (case:94-97) | Reserve = ten holdings + set-aside |
| 14 | "each January one is redeemed" (P6) | FALSE | Contradicts P1 and the holdings | Each was redeemed the year before |
| 15 | Pitch: "Her first $300,000 buys Treasuries maturing before each..." | HALF-TRUE | One-close call (GT:87-90; 02c:260); five are funds | Keep the IPS's "if needed" logic |
| 16 | Pitch: "buys Treasuries for her minimum ... puts only their interest into world shares" | HALF-TRUE | The deposit tops up the ladder first (02c:91). Read literally, the interest is swept into shares as it's paid, so the fund couldn't grow back. P3 has it right | A slice equal to the interest, put in at the start |

TRUE: "$300,000 is about what the ten holdings cost" (02c:236); "no payment depends on a share price, a forecast or an early sale" (02c:245, given P5); "about the interest that fund will earn" (02c:246); "Treasuries alone would leave her a larger sure sum" (02c:280); "near-complete confidence" (02c:249); "nothing changes because markets move" (02c:31; WHARTON_WORD.md:121-122); the pitch's "never names a number she doesn't already own" and "which can raise it" (VT note, 02c:46).

On the rules and October's clashes, R09 is clean: no TIPS, STRIPS, derivatives or "cash" (WHARTON_WORD.md:137-139; 1C#11 02c:92), and no C4, C8, C11 or C12.

## Missing that the locked record requires
1. **The set-aside inside the reserve** (#13); without it the reserve falls short in P5's falling-rate world.
2. **Which shares pay the gap, and when**: "kept", with the order (#9).
3. **Where waiting money sits**: a short-term Treasury fund, never cash (Note 1; May-2038 note; 1C#11). Two holdings mature 10.5 and 7.5 months early.
4. **IBTM's two jobs** (02c:36; 1C#5 :86; Oct C7). The minimum's fund is the first payment's fund, which is why it is 32.5% of the frozen book (snapshot:22, :36). R09 reads as an eleventh holding.
5. **Liquidity**, which Wharton asks for four times (WHARTON_WORD.md:54, :59, :73, :84). FINAL said "liquid"; October's C6 trade (Refl. 2) goes unused.
6. **A rise before 2031 lifts the top** (VT note; 1C#9; case:118-119), and **a top-up leaves less for the facility** (IBTR note): both only implied.
7. **Five payments sit in funds paying NAV, not par** (1C#4 02c:85): see #1.
