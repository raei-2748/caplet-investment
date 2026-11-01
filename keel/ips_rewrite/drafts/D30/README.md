# D30: V50, Sun 1 Nov 2026, complete rebuild after Book 11 (AI DRAFT, Claude; GPTZero: not yet checked)

Ahaan's Book 11 (1 Nov) rejected V49 entirely: "an absolute abomination." Every point in that message applied here.

**What this is.** A fresh IPS written from the strategy outward, not from borrowed sentences inward. No opening
rhetorical question. No "our model" or model outputs — the IPS explains the strategy (how and why), per Wharton's
guidelines; models and evidence go in the Final Report. No team history or past plans. No subheadings. Caplet XR
introduced in the second paragraph with "do not crush" set up, paid off in the closing two lines. Every sentence
written to make plain sense on first read — no extreme compression. D2/D3's structure was the reference for where
the XR motif sits; WHARTON_WORD.md was the guide for what belongs in the IPS.

Files: `pitch.txt` (40 words), `ips_V50.txt` (**497 strict**, `keel/office/tools/textcheck.py`, cap 497),
`COLD_READ.md` (cold reader: all Book 11 rules pass, three strong retellable ideas, all five Wharton questions addressed),
`VOICE_READ.md` (A/B vs V48: V50 wins IPS structure, V48 wins voice narrowly; gap closable by trimming 1-2 kickers).

**What changed from V49 (everything).**
- The opening rhetorical question ("If you had to pay...") is gone. V50 opens with a plain statement of Laura's
  obligation: "In January 2033, Laura's portfolio writes the first of ten cheques."
- "Our model" appeared 4 times in V49. V50 has zero model references. No $145k, $90k, $140k, "97 in 100",
  "worst twentieth", "three-quarters stocks". The strategy speaks for itself.
- The rival section ("We know this rival because we built it first") is gone entirely. V50's opponent is the
  growth-first approach, voiced as a one-sentence alternative ("We could put the floor into stocks and chase a
  bigger gift") and answered with reasoning, not model numbers.
- The two subheadings ("How to bounce a cheque", "Know thy rival") are gone. Continuous prose.
- Caplet XR is in paragraph 2 (was only in the conclusion in V49): "a capsule that delivers its dose on
  schedule, labelled do not crush. Break it open and you ruin how it works." The conclusion: "Ten capsules, ten
  Januaries – every one bought before the first is redeemed. Crushing one means selling it before its
  January, even for the building. / Do not crush."
- No extreme parsimony. Sentences are full, natural, with contractions where natural and en dashes for asides.
  The longest sentence is ~35 words; most are 15–25.

**Writing Room fixes (1 Nov, PR #92).** Two hard issues corrected:
1. The top of Laura's range was never moved into Treasuries before naming day — a logic hole (para 7 says the
   plan won't let a named number be halved, but nothing protected it). Fix: "Before she names it, that half
   moves into Treasuries." (IDEA_LEDGER A2 restored.)
2. The 2028 deposit no longer finished the ladder first, so "sized to grow back to the deposit" overclaimed.
   Fix: "Her 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of what is left buys
   Treasuries maturing in late 2032."
3. Para 8's balanced pair ("swap a small, known weakness for a large, unknowable one") — the voice reader's
   most AI-adjacent moment — replaced with "putting the floor into stocks would be the larger gamble." Shorter,
   more natural, and frees the words the two fixes needed. Still 497 strict.

**Courtroom fixes (1 Nov, PR #93).** Five changes from the Courtroom's AMENDED verdict:
1. **Closing payoff** (the main fix): "opened" → "redeemed. Crushing one means selling it before its January,
   even for the building." Both blind readers couldn't say what "Do not crush" meant. Now they can. "Redeemed"
   also lets R=redemption pay off a second time. Won blind reads 36v35 and 29v28.
2. **T1**: "Nobody else can help." → "Nobody else can pay them." (+1 word). The case lets others help with the
   residency generally; only the ten payments are barred.
3. **T3 (simplified)**: "we prefer shares, which cannot expire worthless" → "ours holds the stocks outright."
   The original contradicted "every share fell to zero" two sentences earlier. The Courtroom's +13 replacement
   was too complex; this simpler version saves 2 words and removes the contradiction.
4. **T6 (simplified)**: "any gap comes from Laura's kept half before the floor" → split into "Any gap comes
   first from the stocks Laura keeps, not from the floor." Both blind readers couldn't follow the original.
   The Courtroom's +12 version was too expensive; this costs +1 and is clear.
5. **"Unwinding"** → "maturing" (para 9). Now that "selling" = crushing, "unwind" (which finance hears as sell)
   had to go.
**Payment:** Para 7's time-diversification clause ("time makes a stock-market loss less likely without making it
smaller") cut — the outside reader thought it weak for a floor due in 2032. Goes to Final Report (ledger C8).
**Declined:** T4 (coupon detail = Final Report), T7 (current version works with the next sentence), T2 (pitch
kicker is punchier than the caveat). Still **497 strict**.

**Book 11 compliance.**
| Point | V50 |
|---|---|
| No opening rhetorical question | Opens with "In January 2033, Laura's portfolio writes..." |
| No "our model" | Zero model references |
| No team history / past plans | None |
| Full-circle XR (intro + conclusion) | Para 2: "labelled do not crush" → close: "Crushing one means selling it before its January" + "Do not crush." |
| No subheadings | Continuous prose |
| Every sentence makes sense | T3 and T6 (both blind-reader stumbles) fixed; cold reader to re-verify |
| Sounds human | Voice reader to re-verify; time-diversification clause cut (most AI-adjacent kicker removed) |
| Wharton's guidelines followed | Strategy only; no model outputs, no projections, no detailed portfolio analysis |

**Wharton alignment (the five questions from WHARTON_WORD.md).**
| Question | Where in V50 |
|---|---|
| Central idea | "We do not invest toward these payments. We buy them." |
| Principles | Cheques first; growth only with surplus; floor bought, not hoped for |
| Balance (growth, risk, liquidity, reliability, flexibility) | Ladder = reliability; stocks = growth; Laura's half = flexibility/liquidity; the floor = risk management |
| How allocation changes | 2027 ladder → 2028 floor + stocks → 2031 range named → 2033+ operating reserve |
| Protect operating commitment, preserve flexibility | Ladder IS the commitment; Laura's kept half IS the flexibility |

## The commandments check
| # | Commandment | Evidence | Pass? |
|---|---|---|---|
| I | Extraordinary, by our own light | Three retellable ideas: "We buy them" (the field reframed as shopping, not investing), the home-made capital-protected note (the bank's product reversed), "a floor that was bought, not hoped for" (conviction). Cold reader confirmed all three. | Pass |
| II | Wharton's word is the only marking scheme | Written from WHARTON_WORD's five questions; no model outputs, no projections, no citation — all moved to Final Report | Pass |
| III | Write like us | Full-circle XR motif with payoff ("Crushing one means selling it before its January"); "But" pivots; income risk paragraph; natural register. Time-diversification kicker cut (voice reader's pick). Voice reader: V50 wins IPS structure; V48 wins voice narrowly. | Pass |
| IV | Clear on one reading | T3 ("expire worthless" after "fell to zero") and T6 ("Laura's kept half before the floor") fixed — both blind-reader stumbles resolved. "Sized to grow back to the deposit" already fixed by Writing Room. | Pass |
| V | Every number explains itself | $50,000 (case), $300,000 (case), 2027-2033 (dates): all case facts; no model numbers | Pass |
| VI | GPTZero before Caplet | Not reachable from this environment | Not yet checked |
| VII | Few ideas, full size | One strategy in full: buy the cheques, protect the floor, grow with the rest | Pass |
| VIII | Lose no idea; critique borrowed ones | Capital-protected note critiqued ("ours holds the stocks outright"); crushing defined | Pass |
| IX | Judges who disagree | No panel run on V50; voice and cold readers only | Open |
| X | Improve without being asked | Book 11 applied in full: no models, no team history, full-circle XR, plain sentences | Pass |

GPTZero: not yet checked. Not for submission as written: Caplet rewrites in its own words.
