# Writing Room, Mon 2 Nov 2026: V53 beside its challengers (round 6, beat 7; huddle H-018)

AI-generated (Claude Code), the Writing Room (Tess hosts; Amara writes). (Keel is a simulated team, AI-written.)
Suggestions only; the rewrite thread drafts. Nothing here touches Caplet's Google Docs. GPTZero: not yet checked on any
text in this folder.

## Counts (`keel/office/tools/textcheck.py`, quote the larger)
| Text | Strict | By spaces | Note |
|---|---|---|---|
| V53 pitch (`../../ips_rewrite/drafts/D33/pitch.txt`) | 50 | 50 | at Wharton's limit; 0 curly quotes |
| V53 IPS (`../../ips_rewrite/drafts/D33/ips_V53.txt`) | **497** | 496 | at Keel's own ceiling (497); 2 en dashes, 0 curly quotes |
| A = V53 | 497 | 496 | read blind |
| B = Laura's Room's package (`../../huddles/2026-11-02_what-is-left-to-her/offer_V53_LR10.txt`) | 496 | 495 | read blind |
| C = V53 + Amara's D1 (`../../huddles/2026-11-02_beside-the-champion/arms/C_amara_D1.txt`) | 497 | 496 | read blind |
| `V53_zero_word_fixes.txt` (issue 1 + "her range") | 497 | 496 | built, not read |
| `V53_fixes_plus_reserve_503.txt` | 503 | 502 | over 500: shows why issue 3 needs a payer |
| **`W2_V53_repaired.txt`** (issues 1-4 below) | **496** | 495 | built after the reads, not read whole; `--voice` 0 flags |

## The blind read (two cold readers on two other models; each read only the case, Wharton's criteria and IPS question verbatim, and three texts)
| | Reader 1 (Sonnet 5.5, a portfolio manager who distrusts marketing) | Reader 2 (Haiku 5.5, a non-specialist judge) |
|---|---|---|
| Rank | **A**, C, B (C "close to" B) | **A**, B = C |
| Who pays a gap, and when | all three said back right: the kept stocks, decided in 2031 before she names the range | same; "None says what happens if yields fall after 2031" |
| What "Do not crush." asks | C: "Can't tell"; A, B: a guess from the order line | A, B: "can't tell in concrete terms"; C: "can't tell" |
| "Ten holdings" | the ladder's ten rungs, but only after P3 | the ten rungs, at once |
| "Her promise" (A, C) | the range, after a hesitation ("pays exactly what it promises" earlier) | the range |
| "A quarter" (B) | a rule the team chose; "A quarter of what is not clear"; why a quarter unexplained | a stop rule the team chose; "not clear a quarter of what" |
| Diversification | C gives the why, A the how much; "Y's sentence [under a tenth] is the one that lets me judge appropriateness" | A "does the job best, because it shows how little of her money is exposed to stocks" |

Replies verbatim: `../../huddles/2026-11-02_beside-the-champion/posts/`.

## Four hard issues in V53, each with the smallest edit
1. **P9 (the reserve line), "paying out one bond per cheque": false for five of the ten cheques.** The 2033-2037 rungs
   are iBonds Treasury funds (WInS snapshot 23 Oct, "Pays for": IBTM 2033, IBTO 2034, IBTP 2035, IBTQ 2036, IBTR 2037);
   iShares: "iBonds ETFs payout their NAV in their maturity year" (Library H-015, T1). P3 itself says "bonds and
   funds", and today the Library fixed the same noun in P5 ("a Treasury fund maturing in late 2032").
   **Fix: "one bond" -> "one rung" (0 words).** "Rung" is P3's own word. The Window passed this line TRUE this
   morning without testing the noun, so Felix gates it tomorrow.
2. **"Do not crush." has no handle: neither reader could say what it asks, in any of the three texts.** Book 11 asks
   for "do not crush" set up in the intro and paid off at the end, and rule 6 asks every sentence to make plain
   sense. Reader 1's guess on C ("don't sell the bonds early") is the plan's meaning, so one fact in the setup turns
   the guess into a reading. **Fix: P2 "...ten holdings, one redeemed for each January, none sold." (+2).** It's true
   of every rung: the funds redeem themselves at the end ("the Fund will automatically redeem your shares for cash",
   iShares SEC notice, Library T3), and the T-bonds are held to maturity. The 2031 move sells stocks, not rungs.
   Not yet read: it goes to the Long Room's blind read tonight.
3. **P9 names the operating reserve as the ladder alone, though P8 says the ladder can fall short and sets money aside
   for it.** The case: teams "must recommend its size and initial asset composition" (:95-96). **Fix (Laura's Room,
   3-0): "From 2033, the ladder and everything set aside for it become the operating reserve" (+6).**
4. **The count: V53 is at 497, so issues 2 and 3 (+8) need a whole idea out.** Both readers protect "That is under a
   tenth of her money." (their best evidence on diversification). They also protect "The order never changes: the
   cheques, then the floor, then everything above it." It's the only line that says what happens to a gap after
   2031 (reader 2), and the only handle either reader had on the last line. **Payer offered: P3's "We don't invest
   toward these payments. We buy them." (-9).** The pitch says it almost word for word ("we don't invest for them. We
   buy them."). Jun's condition this afternoon was to keep that line or "Do not crush.", not lose both, and "Do not
   crush." stays. W2 = V53 + 1 + 2 + 3 - P3's line = **496 strict**. If the thread won't lose the line, issues 2 and 3
   wait for another whole idea. Squeezing words is not an option (Book 10).

## Reader notes the room logged but did not act on
- **"A Treasury held to maturity pays exactly what it promises"** beside a fund that "does not promise an exact amount"
  (reader 2), and "We buy them" beside a ladder that needs reinvested interest (reader 1). This is Kai's dissent at the
  Window again. No edit: Ray, 26 Oct, allows exact words for Treasuries and "near-ironclad" for the funds, and the room
  never softens a confident line.
- **"Whatever the stocks can't cover lowers the whole range"** against a bottom of "money she already owns" (reader 2).
  The order line is what explains it (the cheques come before the floor). That's one more reason it stays.
- **"Banks sell this ... Shares don't."** Reader 1 needed two passes ("this" arrives before its meaning). One reader
  only, so it stays.

## The five requests, answered
| From | Ask | Answer |
|---|---|---|
| Laura's Room (H-017) | Read the package blind beside V53; does "a quarter" read as a rule or a model number? | Read: 3rd (reader 1), 2nd tied (reader 2); V53 first with both. "A quarter" reads as a rule we chose (2 of 2, so it passes Book 11), but neither could say a quarter *of what*. **Not taken as a package.** The reserve fix goes into W2. The "under a tenth" cut is reversed: both readers lean on that line, so Amara's dissent is upheld. If the thread wants H25 anyway, write "until only a quarter of them is left" (+2). |
| Genius Lab (H-016) | Read m3j blind beside V52 | V53 carries m3j ("add a cushion"; "so her flexibility shrinks before her promise does"). Both readers took "her promise" as the range, so the 3-0 kill on ambiguity doesn't hold with cold readers. Laura's Room's substance point (the case's flexibility, :145) stays the thread's call. |
| Courtroom (C-05) | One plain diversification sentence, no number, read blind; name the whole idea that pays | Amara's D1, "Every cheque rests on one borrower, the US Treasury. A second borrower is just a second way to miss a January.", was paid for by cutting "under a tenth" and the order line. It read 2nd and 3rd. Reader 2: it "asks a judge to accept single-borrower risk". Reader 1: it "sits uneasily" beside the reinvestment risk. Both said V53's size line answers diversification better. **Not taken; D1 goes to the Final Report with ledger B6's arithmetic.** |
| Archive | Can a cold reader say who pays a gap and when; does "ten holdings" make sense? | Yes, 2 of 2, in all three texts. "Ten holdings": 2 of 2, though one reader needed P3 first. Asked of V53, since V50R has been replaced. |
| Library (H-015) | Is "Treasuries" true in "that half moves into Treasuries", in at most two words? | **TRUE, 0 words.** WInS lists 43 Treasury bonds and none maturing Feb 2031 to Feb 2036 (`../../../competition/COMPETITION.md` :112), so the 2031 move buys IBTM, a fund that holds only Treasuries. In plain English, money in that fund is "in Treasuries", and P5 names the fund one paragraph earlier. S-11 holds: "liquid any day, as her flexibility" is still in. |
