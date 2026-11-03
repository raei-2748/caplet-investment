# H-026 brief: W5 on trial (the Courtroom, Tue 3 Nov 2026, round 7 beat 8)

(Keel is a simulated team, AI-written.) FICTION (the room and the simulated people) + real arguments. AI-generated
(Claude Code), not for submission. The run chairs and assembles; it never writes a member's lines.

## The question
The champion is **V54** (`exhibits/V54_ips.txt`, `../../ips_rewrite/drafts/D34/`, 497 strict, pitch 50). The Writing
Room's **W5** (`exhibits/W5_ips.txt`, 497 strict, pitch untouched) is V54 plus twelve changes, each backed by four
fresh strangers (H-025; table in `../../ips_rewrite/inbox/2026-11-03_writing-room.md` s1). Tomorrow (Wed 4 Nov) the
rewrite thread finalises the IPS for Caplet, and **today is the last day anything new is promoted**. So: does W5 beat
V54 as the page a Wharton judge reads, which of its twelve changes stand, amend or fall, and what is the **one change
that matters most**, mapped to a Wharton criterion? Then Keel votes: promote, park or bin.

## The charges the Courtroom must try (from today's round; `../../loop/rounds/2026-11-03.md` s5-s7)
1. **The actuary's worry (Jun, Lab L-17).** The lock W5 writes into P8 ("we price that gap as if later bond payments
   sat idle") pays every cheque in 200,000 of 200,000 model futures once bought, but that is *true by construction*:
   the model zeroes every leg it can see. K0 showed one unzeroed leg (the bill wait, 0.9% of the cheques) cut 100% to
   95.16%. One leg is known to be unzeroed: **the model pays the five fund rungs (IBTM-IBTR, the 2033-37 cheques) at
   par, like bonds maturing on 15 December.** iShares says the funds "do not seek to return any predetermined amount"
   (`../../ips_rewrite/research/R04_fact_checks.md` row 8); in its last year each fund's bonds mature through the year
   and the cash waits for the December close. What can still leave a cheque short after naming day, and do W5's words
   ("later bond payments") cover the bonds *inside* the funds, or only the model's par bonds? The chair runs the test
   (exhibit N) between rounds 1 and 2.
2. **Does W5 still let a reader think a cheque can be short after naming day?** (Writing Room seed: one stranger said
   "possibly yes"; no text says it in words.) And should the page say it, beside five funds that pay net asset value?
3. **Where does the unused lock go?** About $18,000 at the median goes back to Laura as the rungs pay (L-17, LR-11,
   MODEL); P9 is silent. Is the silence a hard issue (case: "committing all remaining assets could limit her financial
   flexibility as the project develops") or a Final Report line?
4. **Any of the twelve changes false, or worse for a judge?** Candidates, not findings: "funds with an end date" beside
   P2's "selling it before it matures"; "a bet that expires worthless unless the market rises"; "in a downturn, when
   interest rates usually fall, making bonds cost more" (2022 was a downturn when rates rose); "under a tenth of her
   $450,000"; "Stocks don't expire."; "a range for her gift to the building"; dropping "first" and "over the long run".
5. **The Courtroom's two standing charges:** "this reads as AI" and "competent but forgettable". Did plain words sand
   off the voice (Book 11 item 6 asks for plain sense; Books 1-5 and Commandment III ask for Ahaan's voice)?

## What everyone reads (and nothing else unless named)
- The two texts: `exhibits/V54_ips.txt`, `exhibits/W5_ips.txt`; the pitch `exhibits/pitch_V54.txt` (unchanged).
- The Writing Room's offer: `../../ips_rewrite/inbox/2026-11-03_writing-room.md` (the twelve changes and why).
- The case: `../../../competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (lines 85-120 matter most).
- Wharton's word: `../../WHARTON_WORD.md` (ranks first). Caplet's rules: `../../BIBLE.md` Book 11 and the Ten
  Commandments (section near line 348).
- The lock's evidence: `../../rooms/lab/L-17_interest_that_earns_nothing.md` s4-s5; `../../rooms/lauras_room/LR-11_parked_not_spent.md`.
- Your own member file in `../../members/<name>.md`, `../../CAST.md`, `../../VOICE.md`.

## Rules for every post
- Book 11: no model numbers or "our model" in the IPS; no team history; no opening question; the Caplet XR circle
  stays (P2 setup, "Do not crush." at the end); every sentence plain; no subheadings.
- No softening (Caplet's standing rule): never propose a hedge or a milder word; a wrong strong word is fixed with an
  equally strong true one.
- Any wording offered is counted with `python3 keel/office/tools/textcheck.py <file>` (the larger, hyphen-split count
  is the one that counts; house cap 497).
- Every number says where it came from (design, engine, curve). Real sources only, quoted with URL and date read.
- **One repair** for the defence, in round 2, after the attack. Nothing else changes the text.

## Roles and budget (nine agent calls)
| Round | Who | Job | Model |
|---|---|---|---|
| 1 (sealed, parallel) | Kai (prosecutes; may play the simulated rival Team Spinnaker) | The strongest honest case against W5, charge by charge; sealed bets on exhibit N and on what the readers pick | Opus 5.5 |
| 1 | Nora (bench; cold judge's sheet) | The judge sheet, written before any reader runs: pass mark, questions, sealed key, decision rule | Sonnet 5.5 |
| 1 | Tess (defence; W5's builder) | W5's opening: what it fixes for a judge, what she concedes in advance | Sonnet 5.5 |
| chair | the run | Exhibit N: the five fund rungs as funds, not bonds (`../../rooms/courtroom/C-06_w5_on_trial/`) | code |
| 2 | Tess | Answers Kai by name; her one repair (W5R), counted | Opus 5.5 |
| 2 (parallel, blind) | Two readers who never saw either text: J, a competition judge; S, the weakest stranger | V54 and W5R as X and Y, seeded order; Nora's sheet | Fable 5.1, Haiku 5.5 |
| 3 | Kai | Replies by name to Tess, the readers and exhibit N; concede or press; vote | Opus 5.5 |
| 3 | Tess | Last word and vote | Sonnet 5.5 |
| 3 | Nora | Rules (stands, amend or fall), the one change that matters most, the champions row; vote | Opus 5.5 |

## Vote gate (room rule, Sun 1 Nov)
1. Caplet's newest message: **Ahaan, Sun 1 Nov 2026, 16:26 Sydney (Book 11); no change since** (checked against
   `../../INSTRUCTIONS.md`, newest row I79, and `../../pm/ASK_HUMANS.md` at 18:30 Tue 3 Nov). The sentence that bears
   on this vote: "half of your sentences just DON'T MAKE SENSE" (Book 11 item 6).
2. Every number on the ballot carries its design and engine: word counts are `textcheck.py`, hyphen-split; model
   figures are V54's design via the L-13 -> L-14 -> L-16 -> W-08 -> L-17 chain, 22 Oct 2026 treasury.gov curve,
   J.P. Morgan 2027 LTCMA global equities 7.5%, 200,000 paths, seed 20261016 (MODEL), plus exhibit N's added leg.
