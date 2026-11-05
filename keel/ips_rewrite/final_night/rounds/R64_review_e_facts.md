# R64 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

`keel/scripts/ladder_pv.py`, 23 Oct close (newest on file): payments $297,636 (66.1% of $450,000); a stake paying $150,000 in December 2032 costs about $117,600 in January 2028, leaving $32,400 (MODEL). "02c" = `harvest/02c_library_models_record.md`; "notes" = `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`.

| Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|
| P1 "keeps every sum Laura commits to in Treasuries before anyone counts on it" | TRUE (design) | `archive.md:87` (A19), `:95` (A27), `:101` (A33) | Holds because P4 dates the cover, but never says it sits in Treasuries (A19: date and home) |
| P1 fixed, portfolio-only, so a debt; X and R | TRUE | case `:90-92` | – |
| P1 2028 deposit buys "whatever $300,000 couldn't if prices have risen" | HALF-TRUE | `00_GROUND_TRUTH.md:87-88` (22 Oct holdings bases $300,224 / $302,139); 02c `:236`, `:260`; notes `:15` | On the real holdings $300,000 was already slightly short on 22 Oct: the top-up isn't only for a rise |
| P2 balanced mix "probably" richer by 2042 | TRUE (MODEL) | `keel/models/README.md:73`, `:78` (older design) | – |
| P2 "about two thirds of her $450,000" | TRUE | re-run (66.1-67.1% across bases) | "Current" = 23 Oct; re-check on the last close |
| P2 leftover swings "far harder than the share market" | TRUE (reasoning) | `IDEA_LIST_VERDICTS.md:74-80`; my rough check about 2x at 60/40, 1.6x at 50/50 | – |
| P3 five funds: one year's Treasuries, December payout, "sell more easily" | TRUE, half the trade | casestudy `:55`, `:78`, `:86`; 02c `:43` | Reflection 2 pairs liquidity with its price: net asset value, not a promised sum (02c `:85`) |
| P3 stake "big enough to get that money back in December 2032" | STRAINS | notes `:19` ("final payout is not fixed"); casestudy `:79` | Sized to pay back about that sum; the payout isn't fixed |
| P3 bottom "starts from that sum, rounded down" | TRUE | 02c `:248` (T15); `range_2031/README.md:36-38` | Rounding must clear the fund's drift (the model takes a 2.5% worst case first) |
| P3 stake costs less; shares get the difference; thousands of companies | TRUE | re-run; 02c `:246`; notes `:14` | – |
| P3 next to all-Treasury "they can only cost her that difference" | STRAINS | re-run: $32,400 left in that fund is about $41,300 by December 2032; 02c `:280` | At worst, the share money plus its forgone Treasury interest (about a quarter more) |
| P4 interest years early; repays "weeks or months" before January; waits at short-term rates, funds included; near-zero rates leave payments short | TRUE | notes `:16-18`, `:22`; casestudy `:81-84`; 02c `:242-243` | – |
| P4 cover bought in 2031 before naming, sized at zero interest, up to half her shares | TRUE (tested) | `archive.md:101` (0 of 200,000 worse off); `lab/L-17...md:56`, `:61` | Say it is bought in Treasuries |
| P4 shortfall "comes out of the bottom, moving the whole range down" | TRUE | L-17 `:56`, `:61` (range lowered in 26.9% of base futures, 71.9% if yields stay 2 points lower) | "If" reads as rare; it is common (A33 rule 3) |
| P5 other half sold the same day sets the top | TRUE | A27; `range_2031/README.md:25` | – |
| P5 "A named top left in shares could only disappoint" | HALF-TRUE | the cap in P6 | It could be missed, never beaten; it can still be met |
| P5 credibility clause | TRUE | case `:114-115` | – |
| P5 "Barring a US default, no payment ever waits on shares, interest rates or an early sale" | STRAINS | 02c `:93` (never "rates can't touch a payment"), `:85`; A24 `archive.md:92` | Shares: true with the dated cover. Rates change the cover's cost, never a payment. Also conditional on the 2028 deposit (case `:43-44`) and five funds paying NAV, not par |
| P5 other money "is already a bet on good times" | STRAINS | 02c `:261`; `what_october_allows.md:36`, `:68` (C5) | The case never ties her income or co-sponsors to markets: "can shrink in bad times" is the ceiling |
| P6 top or less, "never less than the bottom"; "priced in Taiwan dollars" | TRUE (MODEL) | `range_2031/README.md:41-45`; 02c `:143` | The currency is our assumption; the case says only "dollar range" |
| P6 keeps the rest and unused cover shares | TRUE | L-17 `:56` (kept shares all gone in 28%) | – |
| P6 reserve "is what's still waiting to be redeemed"; no trade; repaid in full by January 2042 | HALF-TRUE | casestudy `:137-138` (IBTM pays out about 18 Dec 2032); A33 | By January 2033 the first payment's money is already redeemed: the reserve is that money, nine unredeemed holdings, waiting interest and the cover, not the facility money from the same fund. "No trade", "in full" hold (MODEL) |
| Pitch: a debt; "buys Treasuries to repay it" | TRUE | – | – |
| Pitch: "Her 2028 deposit comes back as the bottom" | HALF-TRUE | notes `:15`; 02c `:91` (1C #10) | What's left after any ladder top-up, via a fund whose payout isn't fixed, rounded down, less any cover shortfall |
| Pitch: half the shares set the top; "both ends are Treasuries before she names it in 2031" | TRUE (design) | A27, A33 | – |

## What the locked record needs that the draft lacks
1. The funds' price for liquidity: five payments rest on net asset value, not par (reflection 2; notes `:19-22`).
2. Favourable outcomes (case `:118-119`): the VT note's "a rise before 2031 lifts the top" is implied, never said.
3. Assumptions and how certainty was evaluated (case `:97-99`, `:146-148`): only "Barring a US default". Missing: the 2028 deposit arrives, start-of-year flows, no outside money, and the test (wipe the shares, no payment worse off, A33).
4. The lock's price in words (A33 rule 3).
5. The waiting place, a short-term Treasury fund (Note 1; 1C #11).
6. Living costs sit outside the portfolio (case `:61-65`): why nothing is sold early.
