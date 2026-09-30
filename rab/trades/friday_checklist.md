# Friday runbook: first WInS trades (Fri 2 Oct 2026, U.S. session)

WS6, RAB Kit, 30 Sep 2026 (Sydney). AI-generated checklist (Claude Code) for Team Caplet. Suggestions only: the
team decides, and students place every trade ("Students should place trades on WInS, NOT the advisor", Wharton, per
insight_v1 E6 s5.9). Tickets: `rab/trades/tickets.md` (Gate A basis). On Friday, trade from the refreshed output,
not from that file. Every time below comes from `rab/trades/trades_clock.py` (zoneinfo), not from hand arithmetic.

## Timeline

| When (Sydney) | When (U.S. Eastern) | What |
|---|---|---|
| Thu 1 Oct, before the meeting | - | One student logs in read-only (no orders) and copies the whole WInS bond drop-down (all 43 bonds: coupon and maturity) into the WInS Notes tab |
| Thu 1 Oct, team meeting | - | Vote: Portfolio tab or Book L; the one swap rule for same-slot alternates (`M9_selection.md`); the backstop sentence yes/no; the floor's definition; roles; notes drafted |
| **Fri 2 Oct 9:00 PM AEST** | Fri 7:00 AM EDT | Read-only checks in WInS; type prices; run the refresh |
| Fri 2 Oct 11:30 PM AEST | Fri 9:30 AM EDT | U.S. market opens. Watch, do not trade for 15 minutes |
| Fri 2 Oct 11:45 PM AEST | Fri 9:45 AM EDT | Earliest any order may go in, only if Plan A cannot wait (iBonds normally wait for 10:30) |
| **Sat 3 Oct 12:30 AM AEST** | Fri 10:30 AM EDT | **Plan A: orders 1-10 in sequence** (Portfolio book: VT waits) |
| Sat 3 Oct 1:30 AM AEST | Fri 11:30 AM EDT | Plan A should be finished |
| Sat 3 Oct 4:00 AM AEST | Fri 2:00 PM EDT | Plan B start, only if Plan A did not happen |
| Sat 3 Oct 5:30 AM AEST | Fri 3:30 PM EDT | Last order of the day (bonds need to be in before the close) |
| Sat 3 Oct 6:00 AM AEST | Fri 4:00 PM EDT | Close. Bond orders fill at end-of-day prices |
| Sat 3 Oct 8:00 AM AEST or later | Fri 6:00 PM EDT | Check fills, copy notes back, screenshots, Trade Log |
| Sun 4 Oct | - | Sydney moves to AEDT: from Mon 5 Oct the open is 12:30 AM AEDT the next day |
| **Tue 6 Oct 1:30 AM AEDT** | Mon 5 Oct 10:30 AM EDT | **Order 11: VT** (Portfolio book), only once all five bonds show Filled |
| Tue 6 Oct 5:00 AM AEDT | Mon 5 Oct 2:00 PM EDT | VT fallback window, if the first was missed (last order by 3:30 PM EDT) |

## Roles (suggested; each person opts in)

Duties that **need a yes from the person** are marked. Nobody shares the WInS password by message. The trader is
whoever holds the team login.

| Role | What it involves | Suggested | Needs consent |
|---|---|---|---|
| Trader | Logged in; types every order; submits only after the checker says "tick" | the team member who holds the login | yes: login, awake 12:30-1:30 AM |
| Checker | Reads ticker, WInS name, quantity and Preview total aloud against the ticket; says "tick" or "stop" | Ahaan D. | yes: awake 12:30-1:30 AM Sat, and for VT on Tue 6 Oct (a video call works) |
| Price reader | Fri 9 PM: reads the bond prices, accrued interest and ETF names in WInS (read-only) into the price file | Darren W. | yes: needs the login screen, or the trader shares a screen |
| Refresh runner | Runs `refresh_tickets.py`; posts the new ticket file; re-runs it after the iBonds fill, and on Monday before VT | Ray W. | no (the repo is his) |
| Recorder | Trade Log tab: fills, commissions, cash, the note as saved, screenshots | Harry Y. | no (can be done Saturday morning) |
| Note keeper | Holds the final note texts (the team's own words); counts characters; pastes each note | Eric Z. | yes: awake for Plan A or B |
| Timekeeper and backup | Watches the clock; calls Plan B if Plan A slips; second checker | Young Y. | yes: awake for Plan A or B |

Every student should write at least one note or reflection. Exemplars stay labelled `EXAMPLE - team rewrites`, and
any AI help goes in `docs/AI_USE.md`.

## Thursday 1 Oct (before Friday)

- [ ] **Before the vote: read the whole bond drop-down.** One student logs in (read-only: no order screen is
      submitted) and copies all 43 bonds WInS lists, coupon and maturity, into the WInS Notes tab. WInS lists only
      about 38% of the 113 Treasury bonds outstanding (MSPD Table V, 31 Aug 2026), so whether the 1.375% 15 Nov 2040,
      2.000% 15 Nov 2041 and 5.000% 15 May 2037 are listed is genuinely open. The vote then knows which of SW40, SW41
      and SW37 can happen, and writers draft only those variants. Prices are still checked on Friday against the
      25bp band.
- [ ] Vote on the book: the **Portfolio tab** (11 trades) or **Book L** (10 trades). Record the vote, names and date.
- [ ] Adopt **one swap rule** for the three same-slot alternates (`M9_selection.md`): if WInS lists it and its price
      is inside its 25bp band on Friday, swap it in on Friday (`--swap`); if it is listed but its price fails, buy the
      planned bond and let October trigger D swap only if the price passes later; if it is not listed, buy the planned
      bond. The three: **1.375% 15 Nov 2040** for the 4.250% (notes SW40 / T40s / T40b), **2.000% 15 Nov 2041** for
      the 3.125% (SW41 / T41), **5.000% 15 May 2037** for the 4.750% Feb 2037 (SW37 / T37). Keeping a listed, passing
      bond for October is no longer an option (it would look like a trade made to create a pick; T40c is retired).
- [ ] Decide the **backstop sentence** (wording only; `notes.md` s7): does the policy make the half of the stock
      fund Laura keeps, not the floor, the **first call** on a shortfall from coupons or fund end values? It covers a
      modest shortfall, not any (about $20,000, the size of the 2% gap). Yes, and the IPS draft carries the sentence
      the same day: order 5's note is **IBTM_R** (a "refined" pick), and by 6 Nov the IPS names the order of use
      (first a payment shortfall, then facility costs or co-sponsor gaps). No: it is **IBTM_P** (supported). Nothing
      here edits the IPS.
- [ ] Decide the **floor's definition** (`notes.md` s7): (a) the IPS as written, the floor is what is left of the
      2028 deposit after any top-up (`--floor-rule remainder`), or (b) a $150,000 floor, cut only if the payments need
      more than the stock fund (`--floor-rule fixed`, the kit default). It matters only if yields fall before 2028
      (the IBTR test fails, or October trigger B fires). Record the choice in the vote minutes.
- [ ] The refined pick is then the first that exists: SW40, SW41, OD_B (October), IBTM_R. If none, the team features
      the Nov 2039 bond (T39) as supported, with the reinvestment discovery, and does not force "refined"
      (`notes.md` s6).
- [ ] Laura-lens reason for the vote: Book L shows only the payments, so the floor and the stock fund, two of her
      three goals, never appear in WInS before the 23 Oct Trading Notes Analysis (`notes.md` s6).
- [ ] Strategy name: keep any brand name **out of** WInS notes unless Ray confirms the final name (premortem PM-16).
- [ ] Notes drafted offline: at most 285 characters (295 for the IBTR, IBTM and VT notes, whose names cannot get
      longer: `note_check.py --ticker` applies the right limit), plain ASCII (no curly quotes, dashes, "~", "<="), one
      paragraph. None of the overclaim words on the banned list (`rab/premortem.md`, Gate C check 2; say "backed by
      the U.S. government", and never that an iBonds fund repays a set sum). Dollar figures only as "in Laura's
      plan", otherwise percentages. At most one number per note. Briefs and EXAMPLE notes (labelled `EXAMPLE - team
      rewrites`) are in `notes.md`; draft from the brief, then run `note_check.py --ticker <holding> --text "..."`,
      which also measures overlap with the exemplar. Each writer adds **one thing only WInS showed that day** (the
      exact WInS name string, that its 1 Oct price passed the check, the 1 Oct close premium, or the Preview price as
      the note's one number, dated: the price WInS shows, never a kit reference price). No exemplar can contain it,
      so no note is a copy.
- [ ] Everyone reads the five stop rules at the top of `tickets.md`.

## Friday 9:00 PM AEST (7:00 AM ET): read-only checks, then refresh

Nothing is ordered in this step.

1. [ ] **Read the Week-One email** (dashboard, "26-27 Week-One-Email.pdf") and the logged-in **Trading Details**
   page. If a trading-activity minimum is stated, write it down. Do **not** add trades to meet a count: the October
   rule (`october_trade.md`) is the only planned second trade. If it says something that contradicts this runbook,
   stop and tell the team.
2. [ ] Open an order screen for IBTM (do not submit). Record: **which order types exist** (market, limit, other),
   whether Preview shows the commission, and whether a bond Preview shows accrued interest.
3. [ ] Type **IBTO, IBTP, IBTQ, IBTR** and copy each name exactly as WInS shows it. Type **IBTN** once: it should say
   INSCORP Inc. It is never a buy.
   - [ ] IBTP note: on the iShares IBTP page, read the **Premium/Discount** published for the 1 Oct close (or the
     1 Oct closing price and NAV, and divide). Write it, with its date, in the Trade Log. More than about 0.1% either
     way: the IBTP note says what was found instead of "almost exactly".
4. [ ] Bond drop-down: for each planned bond, find it by **coupon and maturity**. Copy the clean price and accrued
   interest per $100 into `rab/trades/wins_prices_friday.csv` (copy of `wins_prices_friday_TEMPLATE.csv`). Do the
   same for the alternates: 2.000% 15 Nov 2041, 1.375% 15 Nov 2040, 4.500% 15 Aug 2039, 5.000% 15 May 2037, and the
   two stale ones (4.375% 15 Feb 2038, 4.500% 15 Feb 2036). "Not listed" is a useful answer: write it in the file.
5. [ ] Refresh runner:
   ```
   /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/refresh_tickets.py --basis friday \
       --wins-prices rab/trades/wins_prices_friday.csv --book Portfolio      # or --book BookL
   ```
   Under the one swap rule (Thursday), add a `--swap` for each same-slot alternate that is listed and whose price
   passes: `--swap "T 4.250% 15-Nov-2040=T 1.375% 15-Nov-2040"`, `--swap "T 3.125% 15-Nov-2041=T 2.000% 15-Nov-2041"`,
   `--swap "T 4.750% 15-Feb-2037=T 5.000% 15-May-2037"`. The script must end with `0 fail`. Share
   `rab/trades/out/tickets_*.md`. Tell the note keeper which notes this settles (T40b / SW40 / T40s, T41 / SW41,
   T37 / SW37).
   - If a bond **fails the 25bp check**, it is stale: use the alternate named on its ticket, or skip it today and
     buy it on Monday.
   - The script prints "ten payments cost $X on 1 Jan 2027" on the latest curve (the zero-coupon basis of
     `numbers.yaml`), then the room under $300,000, the **break-even fall** and the **words for the IBTR note**
     (under 22.5bp "about a fifth", 22.5-30 "about a quarter", 30-37.5 "about a third"). **These lines are the test
     in the IBTR note** (the "tested" pick): read them aloud and write them in the Trade Log; the note keeper types
     the printed words. The break-even moved from 19.3bp to 28.9bp between 25 and 29 Sep, so never reuse the 28 Sep
     words without looking. If the cost is above $300,000, the script says **IBTR TEST FAILS**: go to "If the IBTR
     test fails" below.
   - The bond prices WInS shows on Friday morning are the 1 Oct closes, so the bond notes say "Its 1 Oct WInS price
     passed our curve check". Bonds fill at end-of-day prices: record each fill price in the Trade Log.
   - If a fetch fails, the script says so, falls back to the committed 28 Sep files and marks those prices STALE
     (the check fails). Type the WInS price for every flagged ETF too (the template has a row for each) and re-run
     until it ends with `0 fail`. Never work out sizes by hand.

### If the IBTR test fails (the refresh says more than $300,000)

The rule, set before anyone knew the answer, now decides the trade. Do not stop trading and do not skip IBTR.

1. [ ] Re-run the refresh with `--split-from-curve` and `--floor-rule <the definition voted on Thursday>` added. It
       sizes the Portfolio book from the plan split the curve prints: the dated holdings get more and VT less,
       because Laura's 2028 deposit tops up the earliest payments first and less is left for the facility (IPS: "A
       moderate fall in yields would leave some payments for the 2028 deposit to complete"). The script also prints
       the split under the other definition. Book L is unchanged (it holds only the ladder).
2. [ ] Trade orders 1-10 from that ticket. Order 1's note is **IBTR_F** (`notes.md` s5), in the team's own words.
3. [ ] On Monday, add `--split-from-curve` to the VT refresh too, so VT gets the smaller share.
4. [ ] Tell Ray; the Friday figure goes in the Trade Log and to WS1 for the re-lock.

## Friday 11:30 PM AEST: open. Plan A from 12:30 AM AEST

Order sequence (see `tickets.md` for the reasons): **1 IBTR, 2 IBTQ, 3 IBTP, 4 IBTO, 5 IBTM, then the bonds
6 Nov-2041, 7 Nov-2040, 8 Nov-2039, 9 May-2038, 10 Feb-2037.** **11 VT goes in the next session** (Mon 5 Oct ET), once
all five bonds show Filled, so WInS Order History shows the payments and the floor bought before any stocks.
(Book L: orders 1-10 only.)

**Every order, the same nine steps:**

1. Trader types the ticker (bonds: pick coupon + maturity from the drop-down).
2. Checker reads the **name WInS shows** aloud against the ticket's "Exact WInS name". A mismatch means stop.
3. For iBonds: look at **today's volume so far** on the quote page. The order must be at most half of it (WInS FAQ).
   If it is not, wait 30 minutes.
4. Enter the quantity from the ticket. Bonds: face value. The WInS unit is UNVERIFIED, so if the Preview total is
   10x or 1,000x off, the unit is wrong: fix the unit, not the ticket.
5. Price: the WInS price must be at or below the ticket's **max price**. If limit orders exist, use one at the ask
   shown, never above the max.
6. **Preview total inside the ticket's stop band?** If not: stop, do not submit, find out why.
7. Note keeper pastes the team's note (at most 285 characters) into the Preview note box. Read it once aloud.
8. Submit. Screenshot the Preview and the confirmation.
9. Order History: Filled or Pending? **Never re-enter a pending order.** Open Add/View Notes and copy the saved note
   back into the Trade Log; compare it with the planned text (the box cuts silently at 300).

**After order 5 (all five iBonds filled):** read the WInS cash. If it is below the ticket's worst-case "Cash after"
for order 5, re-run the refresh with `--cash-after-etfs <cash shown> --book <book>` before the bonds. It trims bond face
$1,000 at a time, earliest payment first, so at least $1,000 of cash is always left.

**Bonds (orders 6-10)** fill at end-of-day prices, so WInS cash will not show them until after the close. Do not treat
"pending" as a failure.

## Plan B (if Plan A did not happen): Sat 4:00-5:30 AM AEST

Same sequence, same steps. The last order goes in by 5:30 AM AEST (3:30 PM ET). If even Plan B slips, trade on
Monday 5 Oct ET, which is Tue 6 Oct from 12:30 AM AEDT. Nothing in the plan depends on Friday itself. VT always goes in the session after the bonds fill.

## Saturday morning (from 8:00 AM AEST)

- [ ] Order History: every order Filled? Record the fill price, commission, accrued interest paid (bonds) and cash in
      the Trade Log. Check that every note was saved exactly as planned.
- [ ] Screenshot all positions. This starts the "tested" window for the notes.
- [ ] Any mistake (wrong security, wrong size): **do not sell it today.** Never sell on the day of purchase. Log it,
      discuss it, and fix it only on a later day, with a note explaining why.
- [ ] Anything unfilled: it becomes trigger A of `october_trade.md`, or is simply placed on Monday.
- [ ] AI-use log: the tickets, checklist and any exemplar wording used (`docs/AI_USE.md`).

## Monday 5 Oct ET (Tue 6 Oct from 1:30 AM AEDT): order 11, VT (Portfolio book only)

1. [ ] Order History: all five bonds **Filled**? If any is still pending, wait: VT goes in only after the bonds.
2. [ ] Read the WInS cash. Refresh runner:
   `/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/refresh_tickets.py --basis friday --trade-date 2026-10-05
   --wins-prices rab/trades/wins_prices_friday.csv --book Portfolio --cash-before-vt <cash shown>` (Friday's price file
   is fine: only the VT row is used; add `--split-from-curve` if the IBTR test failed on Friday). Use **only the VT
   row**: the
   plan share, or fewer shares if the cash would fall below $1,000. Never more than the plan share (spare cash waits
   for October trigger C).
3. [ ] Same nine steps as Friday. The VT note says it was bought last; if VT was placed before the bonds by mistake,
   do not use that wording.

## WInS facts: what is known and what to verify on Friday

| Fact | Status |
|---|---|
| $300,000 cash, 0% interest; $25 per ETF trade, $10 per bond trade; 200 trades; no fractional shares; minimum price $3; no day trading | SEEN 29 Sep (Session Rules, tab `WInS Notes`) |
| Note box holds 300 characters; notes are added at Preview or later from Order History | SEEN 29 Sep |
| Orders placed while the market is closed fill at the next open; bonds fill at end-of-day prices | SEEN 29 Sep (Portfolio FAQ) |
| Volume: the Guide says an order may be at most 2x daily volume; the FAQ says at most half of market volume, and larger orders wait | SEEN (both). Apply the stricter rule, as above |
| No WInS Treasury matures between 15 Feb 2031 and 15 Feb 2036; IBTN is INSCORP Inc | SEEN 29 Sep |
| Order types (market, limit?) | UNVERIFIED: record on Friday |
| Bond quantity unit and minimum lot | UNVERIFIED: the Preview total tells you |
| Whether a bond Preview includes accrued interest; the settlement date used | UNVERIFIED |
| Whether pending orders hold back cash | UNVERIFIED |
| Whether a saved note can be edited | UNVERIFIED: treat the first note as final |
| Exact WInS names of IBTO, IBTP, IBTQ, IBTR and of every bond | UNVERIFIED |
| Whether the low-coupon alternates are listed | UNVERIFIED |
| Whether fund distributions are paid into WInS cash | UNVERIFIED |
| Any "required trading activity" minimum (FAQ mentions one, undefined) | UNREAD: Week-One email and Trading Details, step 1 |
