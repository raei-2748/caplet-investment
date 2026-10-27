# FICTION. Huddles: how Keel actually talks to itself

> **Read `../BIBLE.md` first.** Started Tue 27 Oct 2026 at Ray's request: "once you have a lot of agents, you can
> constantly discuss and bounce off ideas to each other ... after all this compounding and bouncing around the ideas,
> you can eventually have a creative idea that is actually valuable ... rather than just generate in one round."
> Keel is a simulated team, AI-written. Its events are fiction and never enter a Caplet deliverable as Caplet's experience.

A **huddle** is one question argued over several rounds by several members, each played by its own agent, each
reading what the others actually said. It is the opposite of one session writing six people's lines in one go. Every
room run holds one (`../pm/runbooks/README.md`, step 3b). The six call it "the thread" in the group chat; the files
say huddle.

## The shape (at least 3 rounds, at least 3 members)
1. **Go away and read** (in parallel, nobody sees anyone else's work): each member researches the question their own
   way, from real sources, and posts a take. Disagreement here is the point: if all three say the same thing, the
   chair has asked a bad question or picked the wrong three.
2. **Reply by name**: each reads every round-1 post and answers people, not the question. Three moves, at least one
   each: **steal** (take someone's idea and make it better), **hit** (attack the weakest claim, with a reason) and
   **yes, and** (build on one). Say if you changed your mind and what did it.
3. **Settle it**: the chair names the one to three real disagreements. The people on each side go and check (a
   source, a number from Jun's sheet, a Lab test), then post what they found, including when it proves them wrong.
4. **Land it** (optional fourth round, or the end of round 3): a vote, or a decision to leave it open on purpose,
   with the next question written down as a **seed**. Tess writes the essence.

Compounding happens across huddles, not only inside one: every huddle ends with at least one seed, and the next run
starts from an open huddle or a seed before it invents a new question (`INDEX.md` lists both). A huddle may stay open
across several runs and days; each run adds a round.

## Who plays whom
- One agent per member per round. It is given: that member's profile (`../members/<name>.md`, the part above
  "## Agent profile"), `../CAST.md`, `../VOICE.md`, `../CULTURE.md`, the huddle's `BRIEF.md` and every earlier post.
  It writes its own post and research note to the folder. The chair (the room's run) never writes a member's lines.
- Models, per the ideation ladder (`../office/IDEATION.md`): round 1 wide on Sonnet (or Haiku for a pure idea
  sprint), replies and the settle round on Opus, where the cross-domain connections happen.
- Size: a room run uses 3 members over 3 rounds (about 9 agent calls). The Long Room's big questions take all six.
  Token rules: `../TOKEN_RULES.md` section 4.

## The folder: `huddles/<YYYY-MM-DD>_<slug>/`
| File | What | Who writes it |
|---|---|---|
| `BRIEF.md` | The question, why it matters, who reads what, the rules | Chair |
| `posts/r<N>_<name>.md` | One post per member per round, headed `**Name** (round N)` | That member's agent |
| `research/<name>.md` (or `<name>_r3.md`) | Sourced notes: URL, date read, what it says, what it means for us | That member's agent |
| `transcript.md` | The conversation in order, round by round, with links to the research | Chair (assembled, not rewritten) |
| `todo.md` | `- [x] Task (Owner; done 27 Oct)` / `- [ ] Task (Owner; by Thu 29 Oct)` | Chair, ticked as things get done |
| `huddle.json` | The card the portal reads (schema below) | Chair; to-do counts by the builder |

```json
{
  "id": "H-001", "title": "Steal like a Year 11", "question": "...", "room": "Long Room", "chair": "Nora",
  "opened": "2026-10-27", "status": "open | closed", "closed": "2026-10-27",
  "members": ["Nora", "Felix"], "serves": "which north star and which Wharton criterion",
  "rounds": [{"n": 1, "name": "Go away and read", "date": "2026-10-27", "posts": ["posts/r1_nora.md"]}],
  "essence": ["One to three plain sentences: what we argued, what we decided, what it changes for Caplet."],
  "decided": ["..."], "seeds": ["The next question this leaves open"], "changes": ["Files changed because of it"],
  "todos": {"done": 0, "total": 0}
}
```

After writing or ticking anything, run `python3 keel/scripts/build_today.py`: it rebuilds `../today/<date>.md` (the
day in plain words), `../today/feed.json` (the portal's Today page) and `INDEX.md`.

## The essence (how Keel talks to Caplet)
Ray asked for "clear essence ... very clear, simple". Each huddle's essence is at most three sentences a Year 11 could
read on the bus: what we argued about, what we decided (or why we left it open), and what it changes in the IPS or
the Final Report. No jargon, no room names, no file paths. The detail is one click away.
