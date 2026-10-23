# Blind M1 check: notes for Gate A

WS1-blind-pricer, 2026-09-30 (Sydney). AI-generated verification (Claude Code) for Team Caplet; no deliverable text.
Files: `blind_pricer.py` (own code, written from the spec), `results.json` (every number), `RESULTS.md` (tables).
Run: `/Users/ray/Research/rab-ws/.venv/bin/python blind_pricer.py` (about 1 second).

## Blindness statement

- Read: `rab/models/M1_METHOD.md`, the raw inputs in `rab/data/` (2026 curve row, Portfolio CSV, WInS price CSV,
  iShares facts, Book L page text, 1990-2026 curve files), `RUN_PLAN.md`.
- Not read: `rab/models/*.py`, any insight_v1 script, `rab/numbers.yaml`, `rab/inventory.md`.
- Seen before pricing, unavoidably: the WS1 milestone line in `rab-ws/STATUS.md` (where progress must be logged),
  which quotes the ladder ($289,119 / $292,418, 26 bp), the Portfolio cost ($294,765, cash $5,236), the 2020 median
  ($459k), "cheapest since 28 May 2002" and the May-2038 accrued typo. The code was written and run once from the
  spec; nothing was tuned towards those figures. The Sheet's own totals (Book L $292,244 / $175 / $7,581) and
  quantities are in the raw inputs and served as a second, independent check.

## Agreement with references I could see (to the dollar)

| Quantity | Mine | Reference seen | Agree |
|---|---|---|---|
| Ten payments, Nov-15 basis, spot 28 Sep 2026 | $289,119.20 | $289,119 (STATUS) | yes |
| Same, value on 1 Jan 2027 | $292,418.11 | $292,418 (STATUS) | yes |
| Break-even parallel fall, Nov-15 basis | 26.20 bp | 26 bp (STATUS) | yes |
| Portfolio tab cost, `close_0928` prices, incl. $200 commissions | $294,764.50 | $294,765 (STATUS) | yes |
| Portfolio cash left, `close_0928` | $5,235.50 | $5,236 (STATUS) | yes |
| Book L ladder value, `sheet_as_read` prices | $292,243.81 | $292,244 (Sheet Book L tab) | yes |
| Book L cash left, `sheet_as_read` | $7,581.19 | $7,581 (Sheet Book L tab) | yes |
| Book L sizes (10) and Portfolio quantities (11) from the B4 sizing rule at `sheet_as_read` prices | 21/21 | Sheet | yes |
| 2020 median, Nov-15 spot | $458,828 | "$459k" (STATUS) | yes |
| Cheapest since (spot, both bases) | 28 May 2002 | 28 May 2002 (STATUS) | yes |

Not yet compared (no reference seen; for WS0 to check against `numbers.yaml`): exact basis spot $287,016.47,
1 Jan 2027 $290,291.38, 1 Jan 2028 $304,295.32, break-even 33.22 bp; Nov-15 1 Jan 2028 $306,524.65; the
`sheet_as_read` and `close_0928_model_accrued` book costs; the seven yields in C; the F split; the G shares.

## Findings and triage (strategy not reopened)

1. **May-2038 accrued is a typo** (recorded 0.530 per $100; actual/actual to 28 Sep gives 1.663; the other four
   recorded figures are within 0.011 of the model). Effect: Portfolio cost understated by $215 (19,000 face),
   Book L by $329 (29,000 face). Cash buffer covers it. *Fix before 6 Nov*: correct the Sheet cell; re-read the WInS
   accrued on the trade day. Independently confirms the WS1 flag.
2. **Two WInS bond prices confirmed stale.** 4.500% Feb-2036 at 102.95: -111 bp against the curve (-104 bp if the
   figure is a dirty price); model dirty about 95.20, so the WInS price is about 8 points too high. 4.375% Feb-2038
   at 99.98: -92 bp (-86 bp dirty reading; the Book L note says "about 85bp"). Both exceed the 25 bp flag. *Fix
   before 6 Nov*: do not trade either; the book already uses the alternates (4.750% Feb-2037, 4.500% May-2038).
3. **In-book bond prices pass** the 25 bp test: gaps -15.3, -14.4, -6.6, -5.1, -1.9 bp (WInS price minus curve, in
   yield; negative = WInS slightly rich). The Portfolio tab's status labels ("-8bp", "+6bp", "+13bp", "+14bp",
   "+15bp") are not reproduced: my gaps are all negative and smaller. The Sheet figures were probably computed
   against a different benchmark or day. *Note in Final Report* (wording only; no trade changes).
4. **Portfolio tab "$" column shows targets, not units x price.** The eleven displayed values sum to $296,700 with
   $3,300 cash; units x displayed price gives $294,377 + $200 commissions = $294,577 and $5,423 cash. More cash, not
   less, so harmless; but the tab's "Cash 1.1%" line understates the cash left by about $2,100. *Note* for WS6/WS8
   when the RAB Tickets tab is built (running cash must use quantity x price).
5. **Model-risk band (A4)** moves the spot value by at most -$480 (PCHIP) and +$8 (zero-rate interpolation); the
   1 Jan 2027 value by -$490 to +$8. Headline numbers are robust to these choices.
6. **Plan split (F)** on the current curve: 66.0% / 25.2% / 8.8% (Nov-15 basis), against the Sheet's typed 65.9% /
   25.3% / 8.7%. Consistent within rounding.
7. **History (G)**, same time to maturity, 9,191 curve days 1990-2026: 2020 median $458.8k (Nov-15 spot), all-time
   high $470.2k on 4 Aug 2020; the 1 Jan 2027 value was at or below $300k on about 10% of days since 2000 and 33-34%
   since 1990; the deposit check finds an unfunded part on about 2% of days (all in 2020), at most about $20.6k.

## Out of scope here

Sections D (ETF look-through, needs the insight_v1 holdings snapshot outside `rab/data/`), E (coupon reinvestment,
"$466k vs $500k at 2%") and B5 (cash margin) were not rebuilt. E carries a headline claim and deserves its own
blind check.
