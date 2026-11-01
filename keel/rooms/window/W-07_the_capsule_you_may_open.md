# W-07: the capsule you're told to open (the Window, Mon 2 Nov 2026, round 6 beat 2)

(Keel is a simulated team, AI-written.) Real sources, read by the Window through WebFetch on Mon 2 Nov 2026 (the fetch
tool returns a small model's extract, so "verbatim" means the words came back in the fetched text, not a byte-level
check). Felix's own primary-source find for Q14 ("is everything V52 says about the caplet true at its source?").
Lens 6, the other side: the drug-makers' own labels. Not for submission. Any wording here is an
`AI DRAFT (Claude, 2 Nov 2026)` offer; Caplet rewrites in its own words. GPTZero: not yet checked.

## The sentence tested
V52 para 2 (`../../ips_rewrite/drafts/D32/ips_V52.txt`, unchanged since V50): "To a pharmacist, XR means extended
release: a capsule that delivers its dose on schedule, labelled do not crush. Break it open and you ruin how it works."

## What the labels say
| Product | Source (owner, revision) | Their words | What it does to V52 |
|---|---|---|---|
| Adderall XR (amphetamine), extended-release **capsule** | Prescribing information and Medication Guide, distributed by Takeda Pharmaceuticals America, Inc., "Revised: 4/2026"; read as reproduced at https://Drugs.com/pro/adderall-xr.html | "ADDERALL XR extended-release capsules may be taken whole"; "the capsule may be opened and the entire contents sprinkled on applesauce."; Medication Guide: "If you or your child cannot swallow the capsule whole, open it and sprinkle the medicine on applesauce."; "Do not chew the applesauce and medicine mixture." | The best-known XR capsule's own guide tells a child's parent to break it open. "Break it open and you ruin how it works" is **FALSE** of it |
| Effexor XR (venlafaxine), "capsule, extended release" | Pfizer's own labeling site, "Revised: 8/2022", https://labeling.pfizer.com/showlabeling.aspx?id=100 | "Capsules should be taken whole; do not divide, crush, chew, or dissolve"; "The capsule may also be administered by carefully opening the capsule and sprinkling the entire contents on a spoonful of applesauce."; "This drug/food mixture should be swallowed immediately without chewing" | "Labelled do not crush" is **TRUE** of it; "Break it open" is **FALSE** of it: the label allows opening and forbids crushing and chewing the pellets inside |
| TYLENOL 8 HR Arthritis Pain, "acetaminophen 650mg extended-release **caplets**" | Tylenol's own product page (US, Spanish-language site), https://espanol.tylenol.com/products/tylenol-8hr-arthritis-pain (re-read today; first read by the Kitchen, 1 Nov) | "Swallow whole; do not crush, chew, split, or dissolve"; "unique bi-layer design delivers fast, strong relief that lasts up to 8 hours" | A real XR caplet, and its label carries the words. "A caplet ... labelled do not crush" is **TRUE** at a real label |
| Why crushing is the harm | ISMP Canada, "Some Medicines Should Not Be Crushed, Split, or Chewed!" (2013), https://safemedicationuse.ca/newsletter/newsletter_NotBeCrushedSplitChewed.html (the Kitchen's read, 1 Nov; not re-fetched today) | "If a slow-release tablet is crushed, split, or chewed, a large amount of the medicine may be released all at once." | The source's harm is *all at once*, said of a tablet, which is what a caplet is ("a capsule-shaped medicinal tablet", Merriam-Webster, Library 25 Oct) |

## The "so"
1. V52's object is wrong in the one place a reader might know better. A judge whose child takes Adderall XR has opened
   the capsule over applesauce, because the Medication Guide says to. The motif's setup is the one sentence in V52 a
   lay judge can check from their own kitchen.
2. What the labels forbid is crushing and chewing, and ISMP says why: the dose comes "all at once". That is the
   sentence V52 should carry, and it maps onto the plan without an explainer: the next sentence already says "one
   redeemed for each January", so crushing is the ten arriving at once, cashed early at whatever the market pays.
3. The team's name fixes the object. An extended-release caplet is a real thing on a real shelf with "do not crush" on
   its label. Caplet XR stops being a pun on a pill and becomes the pill.

## The offer (zero words; strict count 497 -> 497, `../../office/tools/textcheck.py`)
"To a pharmacist, XR means extended release: a caplet that delivers its dose on schedule, labelled do not crush.
**Crush it and the whole dose arrives at once.**"

- "capsule" -> "caplet" (Kitchen F18, bank #122; now forced, not optional: the capsule line is false at its label).
- "Break it open and you ruin how it works." -> "Crush it and the whole dose arrives at once." (9 words for 9; the
  source's own harm, ISMP's "all at once").
- The last line, "Do not crush.", needs nothing: the setup now names crushing and says what it does.
- What it doesn't fix: "labelled" is true of the Tylenol caplet and Effexor XR, not of every XR product (Library row 2,
  25 Oct); "To a pharmacist" carries it. Felix's Library scout (12:10) checks the Australian wording (TGA, NPS, SHPA).

## Verdicts for the round (Q14, format of the scouts)
- "a capsule ... labelled do not crush": TRUE IF the capsule is Effexor XR-like; not on Adderall XR's label as fetched.
- "Break it open and you ruin how it works": **FALSE** for the two best-known XR capsules (labels above).
- "a caplet ... labelled do not crush. Crush it and the whole dose arrives at once.": TRUE (Tylenol 8 HR label; ISMP).
- Wharton line: "Presents a clear and creative investment thesis" (`../../WHARTON_WORD.md` s1). Creativity that a
  judge can falsify from their own medicine cabinet is a liability; this makes it true.
