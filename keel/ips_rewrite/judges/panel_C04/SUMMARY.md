# Panel C04 (Sat 31 Oct 2026, the Courtroom, round 4 beat 8). AI-generated (Claude Code), not for submission.

(Keel is a simulated team, AI-written; judges are simulated readers, tests not quotes.) The Courtroom's trial of
LR-08's paragraph (`../../../huddles/2026-10-31_the-whole-price/`). Entries: **V45** (`../../drafts/D25/`), **LRa**
(LR with the defence's one fix, "$9,000" -> "$10,000", 485 strict; `../../../rooms/courtroom/C-04_LRa_ips.txt`),
**LR2** (Felix's one repair: the paragraph moved after the range paragraph, the whole price as a 2042 mean, the payoff in
dollars, "promise" -> "name", donors clause dropped; 497 strict; `../../../rooms/courtroom/C-04_LR2_ips.txt`), plus
rivals A09, S01, H24. Fresh judges, new seed (`build_panel.py panel_C04 4104 ...`); tally `tally.py` -> `rankings.json`.

| Judge | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| J1 skimmer (Haiku) | S01 | LRa | V45 | LR2 | H24 | A09 |
| J2 growth hawk (Sonnet) | **LR2** | S01 | LRa | A09 | V45 | H24 |
| J3 actuary (Opus) | **LR2** | LRa | S01 | V45 | A09 | H24 |
| J4 teacher (Sonnet) | V45 | LR2 | LRa | S01 | A09 | H24 |
| J5 professor (Fable) | **LR2** | LRa | V45 | S01 | H24 | A09 |
| J6 programme manager (Haiku) | S01 | LR2 | LRa | V45 | A09 | H24 |

**Agreement:** mean Kendall tau 0.50 (under the 0.6 alarm). **Mean rank:** LR2 1.83, LRa 2.5, S01 2.5, V45 3.33,
A09 5.17, H24 5.67. Head to head: LR2 beats LRa 5-1, V45 4-2, S01 4-2, A09 6-0.

**What it taught.**
- The whole price wins. Three substance judges (hawk, actuary, professor) put LR2 first for the same reason in three
  different words: it concedes the rival "usually wins", prices that at a mean (~$19,000 by 2042), then shows the tail
  in dollars ($90,000 named v $140,000; over $40,000 behind). The hawk, last panel's V45 voter, moved to LR2.
- V45's "ten one-year bills" is still the line three judges could retell (J1, J4, J6); the teacher put V45 first for it.
  But four judges called V45's 60/40 "a straw man" for dated liabilities. The idea is good; the rival it is aimed at isn't.
- Clarity costs: J5 couldn't place "$145,000 at the median" beside "our $140,000" (the 2031 coupon set-aside, unexplained);
  J1 and J6 found the XR entries dense (Articulation 5/10). S01 (CPPI) is the rival that still beats us with two judges.
- **Blind voice reader** (`../../../rooms/courtroom/C-04_voice_reader.md`, paragraphs only, against Caplet's essays):
  V45's paragraph first, LR2 second ("a results table read aloud": ten figures in four sentences, no image, no number
  reacted to), LRa third (no concession, so no "But"; dangling "Set to promise").
