# V39 (D19): AI DRAFT (Claude, 30 Oct 2026). GPTZero: not yet checked. Current best.

Pitch 48 / IPS 500 (498 by spaces with spaced dashes; 500 with hyphenated words as two; `keel/office/tools/textcheck.py`).

## How it got here (Fri 30 Oct, night round)
- **V37a** (`../D17/ips_V37a.txt`) = V36 + the Archive's A25 fix: the break point on this plan's own design is a 2028
  deposit of about **$125,000** after a two-point fall, not $85,000 (that was V25's design; `../../../rooms/archive_checks/A25_results.json`).
- **V37b** tested an answer to the Rooftop's Q12 ("why not the ladder and the rest in stocks?") in place of the 60/40
  sentence. Panel 5 (`../../judges/panel_V37/SUMMARY.md`): V37a beat V37b with four of six judges; a new rival, S01
  (Treasury ladder + CPPI sleeve), took three #1s on stated assumptions and a stated range confidence.
- **V38** (`../D18/`) = V37a + the assumption ("world stocks at 7.5% a year") + the 60/40 number corrected (one time
  in **three** in the 7.5% worlds, not four) + a redundancy cut. Its cold read (`../D18/COLD_READ.md`) failed IV, V,
  VIII and X; its voice edit (`../D18/VOICE_EDIT.md`) found 7 of 35 sentences off-voice.
- **V39** applies both: the certainty answer made true and short ("only two things break a cheque. The US government
  defaults. Or her 2028 deposit can't fill the gap"); the leak in plain words ("early cash earns less if yields fall",
  which also covers the two bonds that mature months early, Archive A16); "before she names her range"; the 60/40 as a
  concession then "But", saying what it breaks; "grow back into all of it"; "So we built Caplet XR"; liquidity back
  ("to sell any day"). Paid for by splitting off "the rare miss" and dropping one "So".
- Panel 6 (`../../judges/panel_V39/SUMMARY.md`): V39 mean rank 2.0 (best), V37a 2.17, S01 3.0; 3-3 head to head with
  V37a; tau 0.34. V39 kept because it is also the true one.

## Every number and its source (Commandment V)
| In the draft | Source |
|---|---|
| $50,000 every January 2033-2042; $300,000; $150,000 in 2028 | the case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`) |
| three-quarters in stocks missed a cheque in about one future in thirty | the team's first plan in the 27 Sep model (`keel/library/verified_2026-09-27/strategy_mc.py`: growth-first, 3.2% miss; 6.7% US-stocks basis) |
| after a two-point fall the deposit needs about $125,000 | A25 grid on this plan's design: $125k 0.19% of model paths short, $100k 5.0%, $85k 19.2% |
| about a fifteenth of everything she owns | the floor's discount: about $31k of $450k (cold read rebuilt it at about 1/14.4); no single run file yet, to add |
| world stocks at 7.5% a year | J.P. Morgan 2027 LTCMA global equities (`keel/models/ASSUMPTIONS.md` A06; the VT trade note's reflection quotes the same) |
| a 60/40 portfolio misses a cheque or lands below its own range about one time in three | Model Suite M7, `keel/models/results/suite_results.json`, "balanced", p_any_promise_broken 36% / 32% / 35% (lognormal / storms / bootstrap, all 7.5%) |
| the gift reaches its top about 97 times in 100; the rare miss about $1,000 | Lab L-13 (`keel/rooms/lab/L-13_slide_the_range.md`): 96.0-97.9%, $865-$1,194 |

## Commandments check
The filled check is V38's (`../D18/COLD_READ.md`, by a reader who did not write it). V39 applies its three fixes; the
next round's cold read checks V39 itself. VI stays **not yet checked** (`../../DETECTOR_LOG.md`): a student pastes the
pitch and IPS into gptzero.me (no account, about a minute) and needs "human-written only" above 50%.

## Still open
See panel 6's list: "$125,000 of its $150,000" measured against what; the 60/40 sentence's subject; the cost of safety
in dollars (M7: the 60/40 leaves her about $226k by 2042 against our $30k, with a similar median gift); the Lab's A09
run (Sat 31 Oct).
