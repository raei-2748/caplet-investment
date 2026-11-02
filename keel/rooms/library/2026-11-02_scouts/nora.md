# Nora's scout notes (round 6, Mon 2 Nov 2026; Sonnet 5.5) (Keel is a simulated team, AI-written.)

H-015 (`../../../huddles/2026-11-02_the-other-side-of-each-holding/BRIEF.md`), Q14, adjacent scout. Question: why does
the frozen WInS book hold stocks, when V52's pitch and P3 say the first $300,000 buys Treasuries? Text under test: V52
(`../../../ips_rewrite/drafts/D32/ips_V52.txt`, `pitch.txt`). Primary files only; nothing fetched from the web; WInS and
SMApply not opened. Read 2 Nov 2026. Nothing in the repo was edited except this file and the huddle post.

**Limits, said first.** (a) `textcheck.py` reads V52 at **496** on my tree (the brief said 497); every cost below is
relative to that. (b) The WInS pie-chart label ("Long Equities") is Caplet's own note (`competition/COMPETITION.md:117`);
I did not see the chart. (c) The "two-thirds" size is my arithmetic on a flat 5.15% yield (the snapshot's implied yields
run 5.05-5.37%, `competition/wins/2026-10-23_snapshot.md:37-38`), so MODEL, mine, not for any deliverable.

## 1. The two verdicts (a judge with the WInS book and the Trading Notes open)

**Pitch, "Her first $300,000 buys Treasuries that each mature before a January." (`pitch.txt:1`): TRUE IF** "her first
$300,000" is Laura's real January 2027 deposit and "Treasuries" is allowed to take in the five iBond Treasury funds.
Checked against the book: all ten ladder holdings do fall due before their January (funds Dec 2032 to Dec 2036; bonds
Feb-2037, May-2038, Nov-2039, Nov-2040, Nov-2041; `snapshot.md:22-31`). Read as a description of the book it is
**FALSE**: the book's $300,000 also holds VT (8.6%) and a double-job IBTM.

**P3, "In January 2027, her first $300,000 buys a ladder of Treasury bonds and funds that mature like bonds, one rung
falling due before each cheque." (`ips_V52.txt:5`): TRUE IF** the same condition. It is stronger than the pitch line: it
dates itself (the simulator ran Sep-Nov 2026, so "January 2027" cannot be the simulator), it names both kinds of rung,
and it matches the book holding for holding (5 funds + 5 bonds = ten rungs for ten cheques). It is also the IBTR note's
own claim (find F1). One more condition: that $300,000 is enough on the day, a "one-close call" (`00_GROUND_TRUTH.md:88`);
P5's "any rung the first $300,000 couldn't buy" (`ips_V52.txt:9`) already carries it.

## 2. Finds

**F1. Wharton itself says the simulator is not Laura's real money, and hands the "did you implement it" check to the
Final Report.**
- Source: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:129-130`: "The WInS portfolio represents each
  team’s implementation of its investment strategy during the competition. It does not determine Laura’s actual
  portfolio value at the beginning of 2027." And `UPDATED_2026_WGY_Investment_Policy_FINAL.txt:79-80`: "Your portfolio and
  Final Report should reflect the strategy established in your IPS. In the Final Report, your team will evaluate how
  effectively it implemented that strategy".
- Mechanism: judges are told, in the case they hold, that the book is an implementation and not her January 2027
  portfolio. So P3's dated "January 2027" sentence is a statement about the plan, and a book on a different date cannot
  falsify it; the comparison of book to plan is assigned to the Final Report.
- Touches in V52: pitch sentence 2, P3 (`ips_V52.txt:5`), and any bridge sentence.
- Where it breaks: the same figure, $300,000, stands on both sides, and the IBTR note sitting in WInS says "On the 6 Oct
  Treasury curve, her first $300,000 is enough to buy Treasuries for all ten payments."
  (`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15`). A judge who lays that note beside
  a book holding VT and rungs about two-thirds size sees the gap. Wharton does not forbid that comparison; it just says
  where it is settled.

**F2. The book is the finished plan on a later date and at about two-thirds size, and that is written down only in the
repo and in one note that is not among the three submitted.**
- Source: `competition/COMPETITION.md:225-226`: "The WInS portfolio mirrors Laura's plan scaled to $300k."; the Nov-2041
  trade note (`05_trading_note_reflection_wins_trading_notes.md:24`): "With no iBonds Treasury funds maturing in 2037-43,
  the last five payments use individual Treasuries, scaled to the model portfolio, with reinvested coupons funding part
  of each."; the IBTM row (`snapshot.md:22`): "IBTM (iBonds Dec 2032) | 4,503 | 22.055 | 21.65 | 99,313.67 | ... | 2033
  payment + floor stand-in" (the "Pays for" column is the repo's, not WInS's; the WInS note says "does two jobs",
  `05_...md:19`).
- Mechanism: the book was built as Laura's plan after both deposits (ladder + a 2032 floor + a small world fund), then
  shrunk to WInS's $300,000. My arithmetic: the nine non-IBTM rungs cost $175,305 (`snapshot.md:23-31`), against about
  $258,700 for nine $50,000 cheques (2034-2042) at a flat 5.15%, a ratio of 0.68.
- Touches in V52: P3's "one rung falling due before each cheque" (right in number, short in size) and P2's "ten
  holdings" (`ips_V52.txt:3`).
- Where it breaks: a judge who sizes IBTO (1,024 sh, $23,936; the note says "IBTO is for Laura's second $50,000
  payment") against a $50,000 cheque finds about half. Also the WInS pie chart reportedly calls the iBond funds "Long
  Equities" (`COMPETITION.md:117`: "The WInS pie chart labels the iBond ETFs "Long Equities" (61.6%). The true mix is
  about 91% Treasuries. Explain this in the Final Report."). Only the Final Report can explain either.

**F3. "About a fifteenth" is not what the book holds.**
- Source: `ips_V52.txt:9`: "That is about a fifteenth of her money." Against `snapshot.md:36`: "Weights on the $305,558
  portfolio value: IBTM 32.5%, other iBonds 29.0%, T-bonds 28.3%, VT 8.6%, cash 1.1%, accrued interest 0.4%." and
  `snapshot.md:32` (VT 167 sh, $26,138.84).
- Mechanism: a judge divides 26,139 by 305,558 and gets 8.55% (one in 11.7), not one in 15 (6.7%). Scaling keeps
  proportions, so "scaled down" cannot excuse it. The book's 8.7% comes from the older plan (`keel/library/insight_v1/
  securities_and_allocation.md:30,33`: "stock fund 8.7% of about $464k"); V52's fifteenth follows the post-6-Oct plan
  ("VT ~$32k in Jan 2028", `00_GROUND_TRUTH.md:89-90`, about 7%).
- Touches in V52: P5, the sentence after "goes into one world index fund" (`ips_V52.txt:9`).
- Where it breaks: only for a judge who does the one division. It is the only line in V52 that gives a proportion the
  book can contradict, and it is checkable in five seconds.

## 3. Is a "scaled" bridge needed in the IPS? No. Final Report only.

From Wharton's words, not taste:
1. The IPS is told what not to do: "Focus on the strategy and decision-making framework that guide your portfolio rather
   than describing individual investments or presenting detailed financial calculations."
   (`UPDATED_2026_WGY_Investment_Policy_FINAL.txt:54-55`). A sentence about what the WInS book holds, and at what scale,
   is a sentence about the book.
2. The check is assigned elsewhere: "In the Final Report, your team will evaluate how effectively it implemented that
   strategy" (`:79-80`), and the numbers wait there too: "These elements will be developed and supported in the Final
   Report using the strategy established in the IPS." (`:70-71`).
3. Wharton separates the two portfolios for the judges (case `:129-130`, F1), and the Guide calls WInS "a tool for
   implementing your investment strategy. It is not the competition scorecard" (`2026_WGY_Investment_Competition_Guide.txt:70`).
4. What judges must find across all three is a consistent strategy: "Teams should use each deliverable for its intended
   purpose while maintaining a clear and consistent investment strategy across all three." (case `:161-162`). V52 and the
   book hold the same three things in the same order: a ladder first, a 2032 floor second, one small world fund last. The
   VT note ("They only set how far her gift rises above her promised minimum", `05_...md:14`) is V52 P6 in other words.
5. "Your WInS portfolio should reflect the strategy your team has developed" (`wharton_email_week5_2026-10.md:42`) is met by
   content, and the book contains each piece V52 names. V52 also dates itself (2027, 2028, 2031, 2033), so it never
   claims the simulator is her January.
6. P3's own words ("funds that mature like bonds") already do half the job of the pie-chart label: the IPS tells the
   judge the iBond funds behave as bonds.
7. The IPS is "the official record" and "may not be revised" (`:76-77`). A sentence about the book would lock an
   implementation detail into the strategy record, and the book can still change until the freeze.

The counter, which I take seriously: a judge scoring "maintains consistency with the team's IPS" (`WHARTON_WORD.md:18-20`)
may check holdings against P3. They find a book that holds stocks bought with "the first $300,000". That is a reading
risk, not a contradiction, and it is small because P5 says where the stocks come in (the 2028 deposit).

**Zero-cost IPS repair (what I would do):** swap F3's line for "That is under a tenth of her money." Same 8 words,
496 stays 496 (measured). True of the plan (about 7%, MODEL) and of the book (8.6%, WInS). AI DRAFT (Claude, 2 Nov 2026).

**If a later round overrules me and wants a bridge** (AI DRAFT, Claude, 2 Nov 2026; no number, no "our model", no team
history):
- Words: **"In WInS we hold this finished plan, scaled down."**
- Strict cost: **+9** (measured: 496 to 505).
- Where: the end of P5 (`ips_V52.txt:9`), straight after "...but the cheques never depend on it.", because P5 is where
  the plan is finished, so "finished plan" has something to point at.
- Pay with a whole idea, not a squeeze: cut P3's "We don't invest toward these payments. We buy them." (9 strict,
  `ips_V52.txt:5`). The pitch already says it almost word for word ("so we don't invest for them. We buy them.",
  `pitch.txt:1`), and the D32 README lists the pair as the open "set piece" (`D32/README.md`, "Still open"). Measured:
  bridge in, mirror out = 496. The 13-word version ("Our WInS portfolio shows the plan once both deposits are in,
  scaled down.") gives 509, or 500 after the same cut: over the cap. Not recommended.
- It only works if F3 is fixed too: "scaled" promises proportions, and 8.6% against a fifteenth breaks the promise.

**What the Final Report carries instead** (the whole bridge, with numbers): the book is Laura's plan on 2 Jan 2028 scaled
to WInS's $300,000; IBTM is rung one plus the floor stand-in; the iBond funds stand in because WInS lists no bond
maturing Feb 2031 to Feb 2036 (`COMPETITION.md:112`); the pie chart's "Long Equities" against the true Treasury share
(about 91%, `COMPETITION.md:117-118`); VT 8.6% against the plan's share.

## 4. Other contradictions, checked word by word against the submitted notes and the book

- **O1. "Treasuries maturing in late 2032. That is her floor." (`ips_V52.txt:9`) against IBTM.** The book's floor is a fund,
  and the IBTM note says "although the final payout is not fixed" (`05_...md:19`). WInS lists "none maturing Feb 2031 to
  Feb 2036" (`COMPETITION.md:112`), and Laura's real plan may use only WInS-listed instruments
  (`COMPETITION.md:93-96`), so a real late-2032 floor can only be a fund too. V52 P6 ("rounded down", `:11`) absorbs the
  payout risk; the word "Treasuries" is Tess's lane (F17). The IBTM note's "does two jobs" is **not** contradicted: V52
  buys the first rung in 2027 and the floor in 2028 and never says they are different securities.
- **O2. VT note "They only set how far her gift rises above her promised minimum" (`05_...md:14`) against P8, "set it aside
  from the stocks Laura keeps; whatever they can't cover lowers the whole range" (`ips_V52.txt:15`).** In the tail the stocks
  can lower the bottom too, so "only" fails there. This is the Archive's A19 (`keel/rooms/archive.md:85`, closed 28 Oct as
  "a reading", reopened 1 Nov for the missing date; V52 has the date, "Before she names the range"). Reflection 3's "the only
  investment not standing between Laura and a payment deadline" (`archive.md:52`) is the same tension. WATCH, not new.
- **O3. "A Treasury held to maturity pays exactly what it promises, whatever markets do." (`ips_V52.txt:5`) against four notes
  that say the fund's payout is "not fixed"** (IBTM `:19`, IBTO `:20`, IBTP `:21`, IBTQ `:22`) and Reflection 2's "terminal payout
  is a net asset value, as opposed to a promise of par" (`archive.md:45`). True as written, since it says "A Treasury"; but the
  next sentence ("That, to us, is what “a high degree of certainty” means") defines certainty by a promise that five of the ten
  rungs make only approximately. P8 names coupon reinvestment as the weak point and not the funds' payout. Archive A3
  (`archive.md:69`) already guards "don't harden it". WATCH.
- **O4. "ten holdings, one redeemed for each January" (`ips_V52.txt:3`).** True of the ten rungs; the book has eleven positions
  (VT is never redeemed). Fine if "holdings" means rungs, which P3 makes clear.
- **O5. Not contradicted:** VT note's "one cheap fund diversifies" and "a rise before 2031 lifts the top" against P5 and P6; the
  IBTR note's top-up against P5's "first finishes any rung"; Reflection 1's reinvestment-rate risk (Feb-2037 note) against P8
  (the notes' risk is the 10.5-month gap, V52's is coupons; V52 names the second, not the first, which is a gap in V52 and
  not a contradiction).

## 5. What I leave open

Whether the swap to "under a tenth" is itself a number the Book 11 rule would let through (it is an allocation, like L-14's
fifteenth). Whether Ray should ever trim VT toward the plan's share: that is a WInS order, a danger-zone decision for a
student, and I do not propose it for a two-point gap.

(Keel is a simulated team, AI-written.)
