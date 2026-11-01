# Kai's checks (H-013, round 1, Sun 1 Nov 2026). Prosecutor, charges 1, 2, 4

Read today (1 Nov 2026), in this order: `keel/members/kai.md` (to "## Agent profile"), `keel/CAST.md`, `keel/VOICE.md`,
`keel/CULTURE.md`, `BRIEF.md`, `exhibits/V50_ips.txt`, `exhibits/V50_pitch.txt`, `keel/WHARTON_WORD.md`, `keel/BIBLE.md`
Book 11 (line 318) and the Ten Commandments (line 341), `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`,
`keel/ips_rewrite/IDEA_LEDGER.md`, `keel/ips_rewrite/drafts/D30/README.md`. No file in `posts/` opened (it was empty).
Not opened: D30 `COLD_READ.md` and `VOICE_READ.md` (the writer's own readers; I wanted fresh eyes).

## Checked
1. **Every quote in the post is exact.** Script check of each quoted string against `exhibits/V50_ips.txt`,
   `exhibits/V50_pitch.txt` or the ledger: all found. Paragraphs numbered by blank-line breaks in V50_ips.txt
   (1 "In January 2033", 2 "We call it", 3 "In January 2027", 4 "Laura carries", 5 "Her 2028 deposit", 6 "In 2031",
   7 "We could put", 8 "The weak point", 9 "From 2033", 10 "Do not crush.").
2. **V50 never says what crushing is.** `grep -i -E "sold|sell|selling"` on V50_ips.txt: zero hits. "crush" x2 (para 2
   label, last line), "break" x1 (para 2), "opened" x1 (para 9), "unwinding" x1 (para 9, line 17), "maturity" x1 (para 3).
   Closest to a meaning is "A Treasury held to maturity pays exactly what it promises" (line 5): a reader has to infer.
3. **The ledger had the meaning and V50 dropped it.** `IDEA_LEDGER.md` line 63, A5: "Do not crush" = no Treasury sold
   before it pays, "IN (heading + 'Nothing is sold before it pays')" as of V31; line 81, B7: ten cheques cost less than
   they pay, the interest covers the rest "if nobody sells early", "also sets up 'do not crush'"; line 53: B7 "cut since
   V32 (no source in the sentence)". Neither is in V50.
4. **Ledger B4 vs V50 para 5.** `IDEA_LEDGER.md` line 78, B4: the 2028 deposit "never carries a cheque". V50 line 9: "Her 2028
   deposit first finishes any rung the first $300,000 couldn't buy." So the deposit can carry a cheque. The page also
   never says whether $300,000 is enough, so para 3 ("We buy them") and para 5 sit uneasily.
5. **The motif contradicts itself.** V50 line 3: "Break it open and you ruin how it works." V50 line 17: "every one
   bought before the first is opened." Same verb, sin in one place and happy ending in the other. "Unwinding" in finance
   means closing a position, which is also selling.
6. **"the gift" is used before it is introduced.** First appearance is in para 4 ("the gift shrinks"). Para 1 says
   "contribute to the building"; para 6 says "her facility contribution". Case wording is "facility contribution"
   (`Laura_Gao_2026_Client_Profile.txt`, "Facility Contribution", p. 3).
7. **"funds that mature like bonds"** is flagged by the writer's own cold reader as a "minor pause"
   (`drafts/D30/README.md` line 69). I count it as a miss, since Commandment IV says one reading.
8. **Wharton quote** in the closing line is verbatim from `keel/WHARTON_WORD.md` section 1, Creativity and Presentation
   (line 34): "a compelling, well-organized narrative".

## Not checked, and why it matters
- **Spinnaker's "over five years ... stocks usually win"** is general market knowledge, not read from a source today. I
  gave no figure on purpose (no model numbers). Felix or Jun should source it before anyone leans on it.
- **No GPTZero.** "Sounds like AI" is by ear. I did not count sentences or use any fingerprint tool as a gate (Book 9).
- **"stocks fall, yields fall, prices rise"** is my plain-words unpacking of "makes bonds more expensive"; standard
  mechanics, not looked up.

## Left out of the post for room (parked, may be useful to Felix)
- "her Taiwan residency" (V50 line 1) can be read as where she lives; `CLAUDE.md` line 229 records that reading as
  "rejected as conflicting with the case". The next sentence ("the building") does not fix it.
- "Nobody else can help." is backed by the case ("Teams may not rely on co-sponsors, grants...", case line 91), but a
  reader without the case open meets it as an unexplained fragment.
- "Caplet XR releases Laura's money on schedule" (pitch) uses "releases" for XR's job; the standing rule is R = redemption.

# Round 2 checks (Sun 1 Nov 2026, Sydney; all repo paths, read 1 Nov)

Read for round 2: `posts/r1_kai.md`, `posts/r1_felix.md`, `posts/r1_amara.md`, `research/felix.md`, `research/amara.md`,
`keel/BIBLE.md` Book 11 (l.318) and the Ten Commandments (l.341), `keel/WHARTON_WORD.md` l.16-100. textcheck on
`posts/r2_kai.md`: 447 by spaces (strict).

1. **"Nobody else can help." (V50 l.1) is the case's rule, not ours.** Case
   `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` l.88-89 (ten payments of $50,000, 2033-2042), l.91-92
   ("All ten payments must be funded by the investment portfolio with a high degree of certainty. Teams may not rely on
   co-sponsors, grants, program fees, or other outside funding to meet this requirement."). l.85-86, Felix's evidence, covers
   "Any remaining facility cost, and any operating support beyond Laura's commitment", i.e. beyond the ten payments. V50 l.1's
   sentence follows the cheques sentence. Verdict: true of the cheques; at most a placement nit, not HARD.
2. **Amara's idea three ("never carries a cheque") is not V50's.** V50 l.9: "Her 2028 deposit first finishes any rung the first
   $300,000 couldn't buy." Ledger B4 (`keel/ips_rewrite/IDEA_LEDGER.md` l.78) has "never carries a cheque"; V50 does not.
3. **The l.9 clash was made by compression.** Older drafts read "Ours swaps the bank's option for shares, which can't expire
   worthless." (`keel/ips_rewrite/judges/panel_C04/judge1_entries.txt` l.66; same line in `panel_V46/judge5_entries.txt` l.34).
   V50 l.9 dropped "the bank's option" ("we prefer shares, which cannot expire worthless"), so "expire" lost its object.
4. **The l.15 slip was made the same way.** V49 `keel/ips_rewrite/drafts/D29/ips_V49.txt` l.7: "cash from bonds that mature
   early earns less while it waits". V50 l.15: "bonds that mature early earn less while waiting". The leak the Lab models is the
   coupons (`keel/ips_rewrite/lab/R08_4_coupons.py` l.5-9, docstring; MODEL, context only, no number used).
5. **How earlier blind panels (simulated readers, older drafts, thinner set-up than V50) read the note v the ending.**
   - Note retold even when it confused: `panel_V43/judge1_scores.md` l.21 ("the clearest explanation of what they are doing that I
     read tonight, and it made the idea easy to repeat"); `panel_V46/judge5_scores.md` l.30 (lists it under "What I learned");
     confused: `panel_V46/judge1_scores.md` l.23, `panel_C04/judge4_scores.md` l.35, `panel_V43/judge2_scores.md` l.17;
     `panel_V43/judge6_scores.md` l.21 ("a loose comparison, since the upside of a real capital-protected note comes from an option
     this plan does not use").
   - Ending: `panel_V43/judge4_scores.md` l.28 ("The ending adds nothing"); `panel_V46/judge1_scores.md` l.22-23 ("the name and
     sign-off were a puzzle"); `panel_C04/judge4_scores.md` l.17, l.29, l.35 ("Do not crush" not understood, three entries) and
     l.50 ("cut the cutesy ending"); `panel_WR31/SUMMARY.md` l.31 (repeat trip J1, J2, J4); `panel_WR31b/judge5_scores.md` l.20
     ("the pharmacy ending asks the reader to do work that Wharton's criteria do not reward").
   - The priority order is retold well: `panel_V46/judge1_scores.md` l.22 ("cheques first, then the floor, then the gift) is a
     rule I would remember"); `panel_V34/judge5_scores.md` l.33. So Felix's "floor counted twice" (V50 l.17) is not on my truth
     list; the pitch's "Never the floor" against V50 l.15 is.
6. **Felix HARD 3 ("regardless", V50 l.5) left off my list.** The sentence's subject is "A Treasury held to maturity", which pays
   its coupons and par whatever markets do. `keel/BIBLE.md` "What this page overruled on Mon 26 Oct": the Archive's A14 objection
   to "exact" cleared for T-bonds held to maturity; standing rule "No hedging". Archive rule A16
   (`keel/ips_rewrite/inbox/2026-10-26_archive.md` l.11-12) bans "markets/rates can't [touch a payment]", which V50 l.5 does not say.
7. **Wharton anchors for the one-job argument.** `keel/WHARTON_WORD.md` l.51 (question 2, principles), l.53-54 (question 4,
   composition "as future funding needs approach and payments are made"), l.67-68 ("managing the operating reserve's asset
   composition over time"), l.34 (Creativity and Presentation, "a compelling, well-organized narrative"); case l.96-97 (reserve
   composition "as the annual payments approach and are made"). Book 11 (`keel/BIBLE.md` l.327): "That was the whole power."

## Changed my mind (round 2)
- Felix's HARD 5 (`posts/r1_felix.md`): the crushing definition must be about the ladder (no rung cashed before its January), not
  about the floor, because V50 l.15 sends a gap to the floor first. Round 1 I had charge 4 as Presentation only.
