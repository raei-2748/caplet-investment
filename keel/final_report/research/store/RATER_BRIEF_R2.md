# Rating new card rows into the store: the brief for raters (Mon 16 Nov 2026)

The store (`insights.jsonl`, built by `build_store.py` from every card's table rows) keeps every idea; raters judge the
new rows so the best rise and the rest stay findable. Read first: `../ROUND2_WORKER_BRIEF.md` (the plan, the rules and
the bans), `../../NUMBERS.md` section 4's headline figures, `../../SKELETON.md` (the parts 2.0-2.5, 3.0, 3a-3f) and
`../goldmine/AHA_REGISTER.md`. Then read each card you are given whole.

## What to write

One CSV file, `digest/ratings_R2_<your letter>.csv`, no header, one line per row of each card you rate:

`<id>,<F>,<R>,<S>,<C>,<status>,<merged_into>,"<note>"`

- **id**: the card id and row number, three digits: `Q48-001`, `Q48-002` ... (the row number is the table's `#`).
- **F, fit, 1-5**: how much it explains or tests a decision in Caplet's IPS or answers something the case or Wharton's
  Final Report instructions ask. 5 = a SKELETON part would be weaker without it; 1 = true but serves no part.
- **R, rarity, 1-5**: 1 textbook, 3 known to practitioners, 5 niche or from another field (start from the card's Niche?
  column and correct it if it is wrong).
- **S, source, 1-5**: 5 verified at source with a quote or table; 3 partly verified, or Keel arithmetic on verified
  figures; 2 unverified; 1 no source or shown false.
- **C, clarity, 1-5**: how plainly it can be said to a smart reader in one sentence.
- **status**: `keep`; `adapt` (true but its wording or a figure needs fixing before use: say what in the note);
  `refuse` (breaks a rule in the brief, contradicts the IPS or TNA, or is false: say why); `merged` (a twin of a
  stronger row: give that row's id in merged_into, which may be in the store already: grep `insights.jsonl`).
- **note**: start with "Mon 16 Nov:", then one short line: the SKELETON part it serves and why, or what must change.
  Use double quotes around the note and no double quotes inside it.

Score = 2F + R + S + C. Be strict: a row that only restates the store, or a parallel that breaks under its own
disanalogy column, is not a keep at F 4. Check every figure that claims to be the plan's against NUMBERS; a plan figure
that is not in NUMBERS is `adapt`.

Do not edit any card or any other file. Report back in under 150 words: rows rated, counts by status, and the five
highest-scoring ids with one line each.
