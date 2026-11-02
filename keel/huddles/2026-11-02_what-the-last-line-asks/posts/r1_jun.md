# Jun, round 1 (sealed; H-019, Mon 2 Nov 2026)
> FICTION (the speaker is simulated; the texts, counts and sources are real). (Keel is a simulated team, AI-written.)

**My call: B (W2), and I want it beaten up by strangers before anyone believes me.** The one reason is Book 11 point 6,
"every sentence must make plain sense to an ordinary reader", backed by Wharton's own line that a strategy "should not be
rewritten simply because markets move or hindsight reveals a different outcome" (Competition Guide, in `WHARTON_WORD.md`
section 3). In A, "Crush it and the schedule is gone" tells you what a pill does, never what crushing a ladder is, so the
last line asks a stranger to guess. In B, "none sold" sits right beside the label and hands "crush" its verb. It costs net
one word (A is 497 on the strict count, B 496, `textcheck.py`, 18:36 Sydney) and the only idea it drops, "We don't invest
toward these payments. We buy them.", is already in the pitch. I'm the cold judge, so my call doesn't count. The rules below do.

**Sealed guess: A 1 of 3, B 2 of 3.** In A the only clue is "the schedule is gone", so most readers will land on "don't break
the plan", which is PARTLY under rule 4. In B they get a verb to lift, but it's eight paragraphs from the last line and a
skimmer will miss the join.

Hana says n = 3 is an anecdote with a spreadsheet. So rule 6 says how big a gap I'll believe.

## The test, pre-registered (fixed Mon 2 Nov, 18:36 Sydney, before any reader has been asked anything)

1. **Texts, byte for byte.** `arms/A_V53.txt` sha256 begins `695ef666e9c02812`; `arms/B_W2.txt` begins `b64388b3587a408d`.
   If either file changes, this is void and I re-register. Readers see them under random 4-letter codes, never A/B, never
   "newer", never what changed, never that "crush" is the question.
2. **Panel.** Three readers, three models, none of them the model that wrote our drafts (the judges README's first
   diagnosis: same model, same taste). Haiku, the skimmer (reads once, lists every sentence not understood first time).
   Opus, the actuary (stress-tests against the case's cash flows, hunts for the hole). Fable, the professor ("what did I
   learn that I didn't know?"). Each gets only the case (`Laura_Gao_2026_Client_Profile.txt`), `WHARTON_WORD.md` sections
   1-4 (the header quote from Caplet cut off) and the coded texts.
3. **Say-backs first, one text per fresh call** (six calls: each model reads A in one and B in the other, order flipped by a
   logged coin), so nobody compares. Q1 is sent alone, and Q2 and Q3 only after Q1 is locked.
   **Q1:** "What does the last line ask Laura not to do? Quote the words that told you, or write 'nothing told me; I guessed'."
   **Q2:** "In this plan, what does 'crushing' mean? Give one thing Laura could do in 2036 that counts as crushing and one that doesn't."
   **Q3 (the changed line):** "In the second-to-last paragraph, what becomes the operating reserve in 2033? Quote the words that tell you."
4. **Scoring, fixed now.** The first answer counts. An answer listing several acts is RIGHT only if every act is a way of
   taking money out of the ladder early.
   - **Q1 RIGHT (1):** names selling, cashing in, redeeming early, spending or drawing on the ladder's holdings before their
     January (or "ever, except to pay the cheque"), with no guess flag. "Don't sell the bonds early" is RIGHT. "Don't touch
     the ladder before the cheques" is RIGHT. "Don't sell any rung, even for the building" is RIGHT.
   - **Q1 PARTLY (0.5):** that content but the reader says they guessed or can't point to words; or the bare "don't break
     the plan / the schedule / the order" with no act. (This is why the 16:20 readers score 0.5, not 1, and not 0.)
   - **Q1 WRONG (0):** any other act (take risk, put the floor in stocks, sell the stocks, spend the cheques, pills) or "can't tell".
   - **Q2:** RIGHT if the crushing example is selling or spending a rung before its January and the not-crushing one is
     something the plan allows (a rung paying out, selling the stocks she keeps, "liquid any day"). PARTLY if "sell nothing,
     ever". WRONG if the crush example isn't a ladder act. Read for colour only, never in rule 6.
   - **Q3 key:** A, the ladder (the bonds and funds bought in 2027-28) = RIGHT. B, the ladder plus the cushion set aside
     from the stocks for the reinvestment gap = RIGHT; "the ladder" alone = PARTLY (the six words didn't register);
     "everything set aside" with no idea what it points to = WRONG (plain sense failed).
5. **Scored blind.** Answers go verbatim to `blind/answers.md` under the codes; the key sits in `blind/KEY.json`, written
   before the run and unopened until scoring ends. I score first; Felix re-scores any RIGHT/PARTLY borderline; a
   disagreement scores 0.5.
6. **Decision.** QA and QB are the Q1 sums over the three readers on each text (max 3); G = QB - QA.
   - Lands in both (QA >= 2 and QB >= 2): the say-backs can't separate them, so B wins only if at least 2 readers rank B
     above A overall and B's Q3 total is no worse than A's; otherwise A. The burden is on the challenger, because this has
     flipped three times in two days.
   - A only (QA >= 2 > QB): A.
   - B only (QB >= 2 > QA): B if G >= 1.5, otherwise **neither** (too thin to move on).
   - Both under 2: **neither**. The ask lives in neither text and Nora's repair is needed.
7. **Rankings are a veto, never a vote.** After the say-backs are locked, a fresh third call per model gets both coded
   texts together (order by logged coin), scores Wharton's five criteria 1-5 per text, gives an overall order, and may not
   let one sentence decide. The texts differ by 22 words, so one reader's taste for one sentence is what the judges README
   warns about. A say-back win stands unless at least 2 readers put the other text higher overall and higher on at least
   3 of the 5 criteria; then the result is **neither**. If all three give the same order for the same one reason, I flag the
   panel as suspect.
8. **Budget fallback.** Nine small calls (six say-backs, three rankings). If the room can only pay for three, each reader
   answers on one text only and no winner is named from fewer than six say-backs: I report the counts and write "unresolved".

My own sealed numbers, for the record: A 1, B 2 (Q1, RIGHT only).
