# FICTION (the room and the simulated parties) + real arguments. C-05: V50 on trial, "Do not crush"

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), not for submission. Courtroom, round 5 beat 8,
Sun 1 Nov 2026, 18:20-19:15 Sydney. Huddle H-013 `../../huddles/2026-11-01_do-not-crush-on-trial/` (BRIEF, posts,
blind sheet, vote note, the bench's Commandments check). Blind-sheet builder: `C-05_build_sheet.py`.

## The claim on trial
**V50** (`../../ips_rewrite/drafts/D30/`, 497 strict, pitch 40; the rewrite thread's rebuild after Ahaan's Book 11 at
16:26 today, with the Writing Room's two logic fixes). It is the champion, and nobody had prosecuted it yet. Question:
does V50 stand as the draft Caplet reads on Thursday? If not, what is the one change that matters most?

## The charges
| Charge | Who | Finding |
|---|---|---|
| "Do not crush" pays off nothing | Kai (r1), Amara (r1, conceded), Felix (r2, changed his mind) | The page never says "sell" or "sold". "Break it open" is the ruin in para 2, and "bought before the first is opened" is the happy ending in the last para. Ledger A5 ("nothing is sold before it pays") is marked IN but missing. |
| Shares "cannot expire worthless" | Felix (r1, CORD) | Two sentences after "even if every share in the world fell to zero". The option the bank's note spends its interest on is never named. Both blind readers tripped on it, unprompted. |
| "any gap comes from Laura's kept half before the floor" | Felix (r1, CORD) | The kept half is stocks, so a share fall pushes the gap onto the floor, against "own outright" and the pitch's "Never the floor". Both blind readers tripped on it. |
| "Never the floor" (pitch) | Felix, Kai (r2) | Para 8 sends a gap to the floor after the kept half. |
| "bonds that mature early earn less while waiting" | Kai, Felix | The leak is mostly coupons reinvested at lower yields (`../lab/R08_4_coupons.py`), not early maturity. |
| "Nobody else can help." | Felix (r1); Kai said true, then flipped (r3) | Right after "to fund her Taiwan residency", a reader hears the whole residency. The case lets others fund the rest (:83-86) and bars outside money only for the ten payments (:91-92). |
| Forgettable | Kai (r1) | "One and a half ideas". The ladder and "We buy them" are the default. The idea a judge retells is that Laura's income is already a stock. |
| Diversification | Felix (r1); Nora's guess at Caplet's next line | "Uses appropriate diversification" is scored under Investment Strategy. V50 has only "one world index fund". |

## Defence, repair and head-to-head
Amara conceded the skeleton is the default and that the ending lands on nothing. She defended "We buy them" / "not a
probability, but a purchase" (the case asks us to *define* certainty, :97-98), the capital-protected note, and her
income as a stock. Felix hit three of her round-1 claims: "about $300,000" is a market price, not a case fact; interest
pays the rest, not time; and crushing costs the promise, not the interest. She conceded all three. **Her one repair**
(`../../huddles/2026-11-01_do-not-crush-on-trial/exhibits/V50R_ips.txt`, 497 strict) changes the last paragraph: "every
one bought before the first is **redeemed**. Crushing one means selling it before its January, even for the
building." It pays by cutting the time-diversification clause in para 7 to the Final Report (ledger C8).

**Blind head-to-head** (seeded shuffle; A = V50R). Tess (Sonnet 5.5): A, 36 v 35 of 50. On B's ending she wrote: "I
couldn't tell" what it forbids. Outside reader (Haiku 5.5, a financial planner): A, 29 v 28. Both readers retold A's
rule. Both missed the same two lines, which sit in both versions. The outside reader's lowest scores, in both
versions: Articulation 2 and Portfolio Analysis 5 of 10.

## Votes and ruling
- **Vote gate:** Caplet's newest message is Book 11 (Sun 1 Nov, 16:26), "half of your sentences just DON'T MAKE
  SENSE". No model numbers are on the ballot.
- **The repair: PROMOTE 4-0** (Kai, Felix, Amara; Tess's blind pick). Truth fixes: T2, T3 and T6 sent 3-0. T1 and
  T4 sent 2-1, and the bench settled both as send. T5 (the fund rungs) was left 3-0 to the weekly plan's K01. T7
  (Amara's add) was sent by the bench.
- **Nora: AMENDED.** The one change is the ending. It lifts **Creativity and Presentation** ("a compelling,
  well-organized narrative"), and the crushing rule also answers Wharton's second question (principles). The margins
  were one point each, from two AI readers: "a nudge, not proof". The paraphrase carried it.
- **The fixes and what pays** (scratch count copy, 496 strict, not a draft): T1 "Nobody else can pay them." (+1).
  T3 "A bank would call this a capital-protected note, except a bank would spend that interest on an option, which is
  worth nothing if the market just stands still." (+13). T4 "If yields fall and stay low, the interest the bonds pay
  earns less when it is reinvested." (+3). T6 "Any gap comes first out of the stocks Laura keeps. The floor is touched
  last, and only before it goes to the building." (+12). T7 "Laura's career already behaves a lot like a stock." (0).
  Pitch T2: "Stocks move the ceiling. Only a long fall in interest rates could shrink the floor." (40 to 48). They are
  paid by three whole repeats of the purchase idea: "a commitment rather than a forecast" (-6), "The building deserves
  a floor that was bought, not hoped for." (-11), and "We accept that; putting the floor into stocks would be the
  larger gamble." (-13).
- **The bench's check on V50R as written:** I, III and IV fail, which is exactly what the fixes target. II, V and VII
  pass. VI is GPTZero, not yet checked. VIII, IX and X are open. The amended text needs one fresh cold read
  (`../../huddles/2026-11-01_do-not-crush-on-trial/exhibits/V50R_COMMANDMENTS_CHECK.md`).

## Left for the rewrite thread (design, not the bench's call)
T6 says plainly that the floor can shrink after she names it. A bottom she might miss isn't quite a promise, and the
ledger's answer is D6: set the gap aside before naming. The other items: the diversification sentence (ledger B6, no
numbers), "unwinding" next to "selling", the downturn link (the case never says when her income falls), and ledger
row B4 ("never carries a cheque"), which the frozen IBTR note contradicts.

## P04 (each new draft scored as a human judge would)
Lowest scores across both blind reads: Articulation, then Portfolio Analysis. Articulation is the Final Report's job
under Book 11. On Portfolio Analysis, the reader complained there is no return or yield assumption to test the floor
against (the Window flagged the same on V47). The weekly plan dropped a stated return for the IPS, and the repair's
cut costs this criterion a concept (Tess docked the point). So the IPS change that lifts it without a number is the
diversification sentence. It puts a concept on show (every cheque on one borrower on purpose; the spreading done in
the stocks), which serves "effective use of investment concepts", and it answers Investment Strategy's "uses
appropriate diversification" at the same time. To the Writing Room (request filed).
