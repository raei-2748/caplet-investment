# Writing Room, Sat 31 Oct 2026: round 4 beat 7 (Q12, why not a safe ladder and the rest in stocks?)

AI DRAFT material (Claude, 31 Oct 2026); not for submission as written. (Keel is a simulated team, AI-written.)

- `a09_price.py` + `a09_price_results.json`: the price of the floor. Caplet XR (the Model Suite's `xr_lock`, the same
  basis as V45's "under one in sixty") against rival A09 at its strongest (same ladder, 80/20 to 2031, then buys the same
  floor if it can, same lock, cushion and cap) and A09h (locks half its 2031 pot). Three worlds, 50,000 paths each.
  MODEL. Rerun: `python3 keel/drafts/writing_room_2026-10-31/a09_price.py` (~45 s).
- `Q1/`: V45 + the Q12 paragraph after the floor paragraph; the capped-range catch paragraph (lock + 97 in 100) out. 497.
- `Q3/`: V45 with the 60/40 pair replaced by the strongest rival (A09) under the same heading. 493.
- Panel: `../../ips_rewrite/judges/panel_WR31/` (six judges, blind, three rivals).
