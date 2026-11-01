# LR-09 results for the huddle (MODEL)

(Keel is a simulated team, AI-written.) From `../../../rooms/lauras_room/LR-09_results.json`, written by
`../../../rooms/lauras_room/LR-09_the_promise_has_no_number.py` (the Lab's L-15 chain unchanged, three outputs added).
Curve 22 Oct 2026; J.P. Morgan 2027 world stocks 7.5%; 200,000 paths per world; seed 20261016; V47's design.

| World | All ten cheques paid in full | Short at any size | Short by over $1,000 | Median gap when short | Gift, mean | Top reached | Same without the 2031 lock? |
|---|---|---|---|---|---|---|---|
| S0 independent | 99.82% | 1 in 551 | 0.03% | $359 | $159,957 | 97.9% | yes |
| S1 linked (rho 0.5) | 99.81% | 1 in 538 | 0.03% | $362 | $159,624 | 97.6% | yes |
| S2 2028 deposit halved, linked | 99.74% | 1 in 381 | 0.05% | $408 | $71,946 | 96.7% | yes |
| S4 yields 1 point lower before the build, linked | 99.95% | 1 in 1,905 | 0.01% | $313 | $125,711 | 96.7% | yes |
| S6 yields fall 2 points just after the build, for good, linked | 99.68% | 1 in 311 | 0.05% | $364 | $141,771 | 96.0% | yes |
| S9 S2 + S4 together, linked (P4's recession) | 98.49% | 1 in 66 | 1.27% | $5,032 | $37,464 | 95.9% | almost (1.503% short without; $5,003) |

S9's gift is under the quoted bottom in 20 paths of 200,000. A missing deposit (the Lab's S3, S5) breaks L-15's sort
of paths into fifths, so it was not run.
