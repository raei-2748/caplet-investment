# R65 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

Keys: CASE = `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`; NOTES = `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`; REC = `keel/ips_rewrite/final_night/harvest/02c_library_models_record.md`; ARC = `keel/rooms/archive.md`; OCT = `keel/rooms/archive_checks/2026-11-05_what_october_allows.md`; RNG = `keel/library/range_2031/README.md`; PACK = `keel/library/assistant_review_2026-10/oct20/casestudy/casestudy_pack.md`; MOD = `keel/models/README.md`. `ladder_pv.py` on the 23 Oct curve: $297,636 = 66.1% of $450,000, 99.2% of $300,000.

| Claim | Verdict | Evidence | What a true version must convey |
|---|---|---|---|
| P1 every committed sum in Treasuries first; payments fixed, portfolio-only | TRUE | REC:249; ARC:95, :101; CASE:90-92 | |
| P1 first $300,000 into ten holdings; 2028 deposit buys whatever it can't | TRUE | NOTES:15, :20; REC:236 | "Repay it" leans on reinvested interest (NOTES:18, :24): keep P4 |
| P2 two thirds of $450,000; balanced mix probably richer by 2042 | TRUE | re-run; MOD:73, :78 (60/40 leaves $229k-$285k, ours $31k-$34k, MODEL) | |
| P2 leftover swings like a borrowed company's shares; ours can't | TRUE | 60/40 of ~$460k puts ~$276k of shares on a ~$150k leftover (~1.8x the market); MOD:78 ($0 gift 1 world in 20) | "Matched", never duration-matched (ARC:102, A34); ours still absorbs the interest gap |
| P3 extra stake in the 2033 payment's fund, pays back about that sum December 2032; rounded down = bottom; difference buys a world fund | TRUE | NOTES:14, :19; ARC:98; PACK:78-79; REC:246, :248 | |
| P3 willing to take risks but can't afford many; payments take nearly all of $300,000 | HALF-TRUE | CASE:68-74 ("has been willing to take thoughtful risks throughout her entrepreneurial career"); REC:187, :235-236 | The case's "thoughtful", in her career; the first deposit has no room for risk, but the 2028 deposit could carry more: the plan risks only its interest by choice |
| P4 interest years early; holdings repay weeks or months before January; waits at short rates; near-zero rates leave payments short | TRUE | PACK:60; NOTES:16-18, :22; REC:242-243 | |
| P4 zero assumed; up to half her shares sold before naming for Treasuries; rest of gap off the bottom, range moves down | TRUE (tested) | ARC:87, :99, :101 (~27 futures in 100, MODEL); REC:244-245 | |
| P5 other half sold same day; top = bottom + what it fetched | TRUE | ARC:95; REC:249; NOTES:14 | |
| P5 left in shares, top missed but never beaten | TRUE via the cap | RNG:26; CASE:114 | True only because the gift is capped; a rise would be hers |
| P5 barring a US default, markets never change what a payment gets | STRAINS | REC:84 ("near-ironclad"); REC:85, NOTES:19-22 (funds "not fixed"); REC:244 (T11); ARC:101 (S9, deposit halved: a cheque worse off in 0.94% of futures) | Price and rate moves land on the range, not the payments, in every modelled future where both deposits arrive; left: a US default, the funds' NAV payouts, the deposit itself |
| P5 every payment leans on the US government alone, because co-sponsors' giving and her earnings are bets on good times | FALSE | CASE:43-45 (the deposit is her earnings); the draft's own P1; NOTES:15, :20; ARC:92 (A24: short in 57% of paths without it); OCT:36 (C5); CASE:91-92 | Only US-government credit, but the payments also rest on the 2028 deposit (the case says it comes); co-sponsors are excluded by the case's rule; her income "can" fall with markets, no more |
| P6 top, or less if the building (Taiwan dollars) needs less, never below the bottom | TRUE, one assumption | RNG:41-45; REC:143 (case names no currency) | Currency is our assumption; nothing says who pays if the building needs more than the top |
| P6 unused shares and zero-rate over-saving stay hers, within reach | STRAINS | ARC:101 rule 4 (FR-only); REC:210 (idea 27); the draft's last sentence puts it in the reserve | Unused shares are liquid in 2033; over-saving appears only as waiting money earns interest, the last after January 2042 |
| P6 reserve = everything still held; redemptions pay down the debt to January 2042 | TRUE | CASE:88-89, :94-97; NOTES:24 | Size and composition only by definition (REC:117) |
| Pitch: debt; Treasuries bought first; top in Treasuries before naming | TRUE | NOTES:15-24; ARC:95 | 50 words split on hyphens (`textcheck.py`): at the limit |
| Pitch: 2028 deposit, after any top-up, comes back in Treasuries as the bottom | STRAINS | REC:248 (T15), :85; NOTES:19; ARC:101 | About that sum comes back; the bottom is it rounded down, lower if the gap reaches it; part buys shares, and the pitch never names growth |

## What the locked record needs that the draft lacks
1. The five payment funds pay NAV, not par (REC:85; NOTES:19-22; ARC:82). Said only of the bottom's stake.
2. The 2028 deposit as an assumption behind the payments (ARC:92, A24). P5 denies it.
3. October's liquidity trade: funds give up a fixed payout for daily liquidity (OCT:37, C6). The form asks for liquidity.
4. Hold to the end, and a rule if a fund's date moves or it closes (REC:83; PACK:86-87).
5. Case asks still open: how certainty was evaluated (CASE:97-99; ARC:101 deletion test), what confidence in the range rests on (CASE:117-118), inflation and overruns (CASE:146-147; REC:251), the good-market path (CASE:118-119; NOTES:14).
6. Where the plan may be wrong (OCT:32): only implied.
