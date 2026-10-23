# FICTION. Team Keel: token-saving rules (for every session that works on Keel)

> Ray, 23 Oct 2026: Keel lives far more time than Caplet, so it could burn far more tokens. Quality stays first;
> waste goes. These rules say what to load, what to skip and what never to regenerate.

## 1. Load the small files first
| Need | Load | Not |
|---|---|---|
| Who the six are | `CAST.md` (one screen) | all six `members/*.md` |
| The setting, time model, what the story may do | `WORLD.md` | re-deriving it |
| World, rivals, motifs, the season's plot to 5 Dec | `STORY_BIBLE.md`, only for an episode that opens an act or turns a plot point | loading it every day |
| Values, culture, what judges reward | `CULTURE.md` | |
| What has happened | `episodes/INDEX.md` + the summary block of the last 2 episodes | whole episodes |
| Open threads, decisions | `tea_room.md` | old episodes |
| Concepts already debated | `IDEAS.md` | re-arguing an idea that has a verdict |

Open a full member file only for the 1-3 members central to today, and then only its profile part (above
"## Agent profile") or its "Working notes", whichever the task needs. Read a full episode only to quote it.

## 2. Every episode starts with a summary block
Right under the title line: `> **Summary.**` in 3-5 lines, then `**Arcs:** ... **Values:** ... **Ideas:** ...`.
Later sessions read these instead of the episode. Add the episode's row to `episodes/INDEX.md` in the same commit.

## 3. Never regenerate what exists
- Do not rewrite profiles, the world, the values or past episodes to "refresh" them. Change a line when a fact
  changes; add a dated line when a member changes.
- Do not re-price or re-fetch what a script already stores: run `scripts/ladder_history.py` (all closes since 24
  Sep) instead of re-deriving the ladder by hand; only fetch a new curve when a new close exists.
- Do not re-quote an official rule that is already in `members/felix.md` (rule table) or `CULTURE.md`; cite its
  file:line.

## 4. Spend agents only where they buy accuracy
- Daily episode: at most 3 backstage crews, not 6 (`EPISODE_RULES.md`), and only for members whose part needs new
  research that day. A day that needs no new research gets no crews.
- `/keel <name>` answers from the files when the answer is there; spawn a crew only for new research.
- One fact-check pass per episode, on the numbers and quotes only.

## 5. Keep files small
- Episodes 700-1,000 words. Profiles under ~2,500 words; move old working notes to a dated archive section
  rather than growing the file without limit.
- `tea_room.md` holds the current state only; history lives in the episodes and the decision journal.
- Members' "Working notes" keep the newest version of a table, not every version (except Nora's one sentence).

## 6. Quality bar that does not change
Every fact sourced (file:line or URL + date), every number MODEL with inputs, every quote exact. Saving tokens never
means skipping a check, guessing a number or inventing a source.
