# Writing Room on V50, Sun 1 Nov 2026, 17:40 Sydney (late in the run)

(Keel is a simulated team, AI-written.) AI-generated check (Claude Code), suggestions only; the rewrite thread drafts.
Edits below are AI DRAFT (Claude, 1 Nov 2026); GPTZero not yet checked.

**Why this page exists.** Ahaan's Book 11 (16:26 Sydney, while this run was reading) rejected V49, and the rewrite
thread rebuilt it as **V50** (`keel/ips_rewrite/drafts/D30/`, branch `claude/project-thread-3ahu9r`, 16:46; copied
here as `base_V50.txt`). This room's W1 was built on V49 and breaks Book 11 four ways (it opens on the rhetorical
question, keeps "our model" and its outputs, keeps "we built it first", and cuts "Do not crush."), so **W1 is
withdrawn** as a package. What it found still counts, and two of its findings are live in V50.

**Counts** (`keel/office/tools/textcheck.py`): V50 IPS **497 strict** (497 by spaces, 495 split), margin 0 under the
497 cap; pitch **40**. Seven en dashes (Caplet's style; not an issue). No model output, no subheading, no opening
question, "do not crush" set up in para 2 and paid off at the end: Book 11 holds.

## Hard issues in V50 (at most five; facts and logic only, no taste)
1. **The top end lost its protection (an idea dropped, and a logic hole).** Para 6: "The top adds half her stocks,
   valued that day." Nothing then moves that half out of stocks, so a fall between naming (2031) and paying (2033)
   comes off a number already said aloud, the very thing para 7 says the plan won't do ("a number said aloud to
   co-sponsors cannot be quietly halved if markets turn"). Every draft from V47 to V49 moved the promised half into
   Treasuries before or on naming day (L-13; Lab L-15; Laura's Room's dated repair, both outside readers' first today);
   IDEA_LEDGER A2 ("each promise made safe no later than the day it becomes one ... top on naming day") is IN.
   V50's README never mentions it, so it reads as lost, not cut. **Fix (+12):** after "valued that day.": "Before any
   co-sponsor hears the number, that half moves into Treasuries too."
2. **The 2028 deposit's first job vanished, so two lines overclaim.** V50 drops V49's "all ten, or nearly" and "the
   2028 deposit that was meant to top it up". Para 3 now says the first $300,000 buys the ladder outright, and para 5
   that the 2028 Treasuries are "sized to grow back to the deposit". If the ladder costs more than $300,000 in January
   2027 (on the 22 Oct curve it fits by $1,139), the deposit finishes the ladder first and the floor is smaller by the
   same amount (number sheet line 14; L-10 `run.py:88`). No figure is needed (Book 11). **Fix (+11):** para 5 opens
   "The 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of the rest buys Treasuries maturing
   in late 2032, sized to grow back to that sum by maturity."
3. **Already filed, not repeated:** "A Treasury held to maturity pays exactly what it promises" sits beside "funds that
   mature like bonds", whose rungs pay their value, not a promised sum (locked reflection 2), and the pitch's
   "releases" (weekly plan K01, PREMORTEMS cause 17 and W3).

**With fixes 1 and 2, V50 is 520 strict: 23 words must go, as whole ideas.** One candidate the room sees: para 8's
second half ("The alternative – exposing the floor to the share market – would swap a small, known weakness for a
large, unknowable one.", 21 words) repeats para 7's case against a stock floor; cutting it leaves 499, two over. The
thread decides.

## What today's reads teach V50 (from W1's huddle; no package)
- **Para 8 already gives the order the readers asked for** ("any gap comes from Laura's kept half before the floor"):
  the set-aside hard issue on V49 is solved in V50.
- **Every reader stumbled on "the rest, the interest they should earn"** in V49; V50's "The rest, roughly the interest
  those Treasuries are expected to earn" is the clearer line.
- **The blind readers are not Caplet's ear.** Both liked V49's opener and its "our model" numbers, and both would cut
  "Do not crush."; Book 11 says the opposite on all three. A Claude reader's taste is a test of clarity, never of voice.
