# Where this skill came from

- **Upstream:** https://github.com/hardikpandya/stop-slop (Hardik Pandya), MIT licence (`LICENSE`, kept as required).
- **Pinned commit:** `8da1f030185bdfe8471220585162991eaeb970e9` (17 Mar 2026, "Add false agency rule"), the latest on
  5 Nov 2026. About 18,600 GitHub stars that day, the most-starred "stop slop" repo; the Chinese and Korean versions
  and "Stop-Slop-v2" all say they are built on this one.
- **Installed:** 5 Nov 2026, for Ray (`keel/INSTRUCTIONS.md` I85), as a project skill so every Claude Code session in
  this repo can load it (`/stop-slop`, or automatically when drafting or reviewing prose).
- **Safety check before install:** seven Markdown files, read in full. No scripts, hooks, settings, MCP servers or
  network calls; nothing in the text asks Claude to do anything except edit prose.
- **What we changed:** `SKILL.md`, `references/phrases.md`, `references/structures.md`, `references/examples.md` and
  `LICENSE` are byte-for-byte upstream, except one section appended to the end of `SKILL.md` ("Keel house rules"). The
  upstream README (an image and install notes) and CHANGELOG were left out.
- **To update:** clone upstream, copy those five files over these, then re-append the "Keel house rules" section.
