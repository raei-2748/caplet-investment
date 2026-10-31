# H-006 The whole price (Courtroom, Sat 31 Oct 2026, round 4 beat 8). FICTION (the people) + real arguments.

(Keel is a simulated team, AI-written.) Chair: Nora (bench). Flaw-hunter / prosecutor: Tess (named at 07:00). Spinnaker
(the simulated rival, growth side): Kai. Defence: Amara (LR-08's author). Builder (one repair): Felix. Cold judging:
the six-judge blind panel (`../../ips_rewrite/judges/README.md`). Budget: 13 agent calls (2 + 2 + 6 + 3).

## On trial
**LR-08's paragraph** (Laura's Room, offered for the IPS). It replaces V45's heading "Sell low, by appointment" and
the two paragraphs under it, whole (V45 496 -> LR 485 on the strict count; the limit Keel works to is 497).
Two blind panels have already preferred it: LR beat V45 4-2 and the Writing Room's Q3 5-1 (panel WR31b, mean rank
1.83 v 3.0). The Writing Room asked the Courtroom to try LR against V45 tonight. Nobody has yet tried it for truth of
its price, for voice, or for what it throws away.

**LR's paragraph (on trial):**
> There is a serious case against all this, and we made it first: our first plan was three-quarters stocks, until our
> own model sank it. Laura is willing to take thoughtful risks, so the strongest rival keeps our ladder and puts the
> rest in stocks, fixing the gift's bottom only in 2031. Set to promise the same $145,000 in a typical year, in our
> model it has to promise under $100,000 about one time in thirteen, because its bottom falls with the market, in the
> years donors give less. Ours, about one in 150. That floor costs Laura about $9,000 of her own money in a typical
> 2033, and we'd pay it.

**What it replaces (V45):**
> Sell low, by appointment
>
> There is a serious case against all this, and we made it first: our first plan was three-quarters stocks, until our
> own model sank it. Laura is willing to take thoughtful risks, and in our model, with world stocks at 7.5% a year, a
> 60/40 portfolio usually ends 2042 almost $200,000 ahead of ours.
>
> But "usually" is the whole trick: about one time in three the 60/40 misses a cheque or breaks its word to
> co-sponsors; ours, under one in sixty. Laura doesn't owe one ten-year bill. She owes ten one-year bills, and a crash
> in the wrong year forces a sale at the bottom – selling low, on a timetable printed years in advance.

Full texts: V45 `../../ips_rewrite/drafts/D25/ips_V45.txt`; LR `../../drafts/writing_room_2026-10-31/LR/ips.txt`.

## Exhibits (all MODEL: curve 22 Oct 2026; J.P. Morgan 2027 LTCMA world stocks 7.5% compound, 16.78% vol; 50,000 paths
in each of three worlds + every start month since 1871; engine `keel/models/xr_core.py`)
- **LR-08** (`../../rooms/lauras_room/LR-08_the_bad_naming_day.md`, house world): both plans name a median bottom of
  $145k; A09 names under $100k in 7.5% of paths (one in thirteen; 3.4-8.6% across four worlds), XR in 0.69% (one in
  150; 0-0.69%). Worst twentieth of 2028-30 stock markets: XR names $135-145k, A09 $80-95k. Median (gift + what
  Laura keeps, 2033): XR $182.4k, A09 $191.9k: the "$9,000". A09 p95 gift ~$250k v XR ~$182k. A cheque short by
  over $1k after 2033: XR 0.19%, A09 0.004% (house).
- **C-04, tonight** (`../../rooms/courtroom/C-04_the_whole_price.py`, same engine, same paths, A09 minus XR per path):

| MODEL, A09 minus XR | House | Storms | Bootstrap | History |
|---|---|---|---|---|
| Gift + kept, 2033: median / **mean** | $9.8k / **$13.9k** | $12.7k / **$12.2k** | $11.5k / **$14.1k** | $15.3k / **$18.9k** |
| Gift + Laura's money left in 2042: median / **mean** | $14.1k / **$18.6k** | $16.4k / **$16.6k** | $16.3k / **$19.2k** | $21.3k / **$26.0k** |
| Paths where XR leaves her ahead (2033) | 38% | 34% | 36% | 32% |
| Worst twentieth of 2028-30 stocks, 2033: XR ahead by (median) | $43.7k | $51.7k | $47.9k | $41.9k |
| Same, by 2042 | $41.1k | $49.2k | $44.3k | $35.2k |

## Rules for everyone
- Only Wharton's word (`../../WHARTON_WORD.md`) and the case decide what a judge rewards (Commandment II). Argue from
  the criteria and the big picture, never from one favourite line.
- The Ten Commandments bind (`../../BIBLE.md`, "The Ten Commandments"): especially III (voice), IV (clear on one
  reading; drop whole ideas, never squeeze), V (every number says who says so), VII (few ideas at full size), VIII
  (lose no idea: anything cut goes to the Final Report, named).
- No hedging; confident claims are kept (Caplet rejects softening). No "every team will ...".
- Simulated people are tests, never quotes. Nothing a member says goes into a Caplet deliverable as Caplet's
  experience. Real numbers only, from the exhibits above.
