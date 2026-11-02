# Felix settles H-015 (round 3, Mon 2 Nov 2026; Opus 5.5) (Keel is a simulated team, AI-written.)

Text under test: `../../../ips_rewrite/drafts/D32/ips_V52.txt` (**496 strict** today, both counts of
`keel/office/tools/textcheck.py`; the team's cap is 497, Wharton's field is 500) and `pitch.txt` (50; no pitch rewrite
offered, the rewrite thread owns it). Paragraphs P1-P10 as in the scouts' notes (P10 = "Do not crush."). Rules applied:
`../../../WHARTON_WORD.md` first; BIBLE Book 11 (no model numbers, no "our model", no team history, no subheadings in any
offered IPS line); Caplet's standing calls not reopened (Caplet XR, X = ten, R = redemption; the funds may be called
"near-ironclad"; a word is wrong only if it is false; no hedging). Every offered wording is **AI DRAFT (Claude, 2 Nov
2026)**. GPTZero: not yet checked. Not for submission: Caplet rewrites in its own words.

Before this round the Library re-fetched every quoted line the round leaned on, Kai's three new ones included
(`README.md`: 45 lines, 45 found). New lines fetched in this round are at the bottom, with what the fetch tool can and
can't promise.

## The three settlements, one line each
1. **P5:** Kai's noun with the thread's verb, "Most of the rest buys a Treasury fund maturing in late 2032. That is her
   floor. The remainder, roughly the interest it should earn, ..." (V52 496 -> 495). Vote 3-1 (Kai for his "is
   expected to earn"). Tess's +11 and the Window's no change both out.
2. **The fifteenth:** swap to "That is under a tenth of her money." (0). Vote 4-0 on the swap; on the reason, 3-1 for
   Kai's (the fifteenth is true at one yield only, so it is a forecast Book 11 keeps out), with Nora's (true of the frozen
   book) recorded as the second reason.
3. **"Do not crush.":** no change. P2 and P3 carry it without P9; P9's clause stays for Wharton's reserve question, not
   as a condition. Vote 3-1 on the reason (Tess: keep P9 as the near anchor), 4-0 on the text.

Whole file after both offers: **495 strict** (scratch copy `/tmp/claude-0/h015/ips_V52_H015.txt`, both counts 495; the
draft itself was not edited).

---

## Settlement 1. P5: which fix, if any?

**The sentence.** V52 P5: "Most of the rest buys Treasuries maturing in late 2032. That is her floor. The remainder,
roughly the interest those Treasuries are expected to earn, goes into one world index fund, spread across thousands of
companies." (36 strict.)

**What decided it: the IBTM prospectus, a line nobody had quoted.** iShares, IBTM summary prospectus (cover 27 Feb 2026),
read 2 Nov 2026: "The Underlying Index consists of publicly-issued U.S. Treasury securities that are scheduled to mature
between" / "January 1, 2032 and December 15, 2032, inclusive." The fund's printed name: "iShares iBonds Dec 2032 Term
Treasury ETF". With the line the Library had already re-checked: "The Fund is a term fund that will terminate on or about
December 15, 2032".

We take that to mean Tess and Kai were each right about a different noun. The Treasuries inside the fund mature right
through 2032, from January, so "Treasuries maturing in late 2032" is false of them. The fund ends on or about 15
December, so "a Treasury fund maturing in late 2032" is true of it. Kai's swap fixes "Treasuries" and "late" in one move.
It also lines up with P3, which has just split the ladder into "Treasury bonds and funds that mature like bonds", and with
the fund's own name ("Term Treasury ETF"). And it stops P3's next sentence, "A Treasury held to maturity pays exactly what
it promises", from being carried onto the floor: "Government backing applies only to government issued securities, and
does not apply to the funds." (iShares iBonds page, re-checked this morning.)

**The four options, counted (whole file, scratch copies, both counts equal):**
| Option | P5 run (strict) | V52 | Verdict |
|---|---|---|---|
| The Window: no change | 36 | 496 | **Out.** Its condition ("Treasuries" covers IBTM) is one P3 breaks by splitting bonds from funds, and "late" is false of the bonds (index line above) |
| Tess: "Most of the rest buys a fund of Treasuries maturing in 2032. It promises no set amount, so that is her floor in value only." | 47 | **507** | **Out.** Over Wharton's 500 as well as our 497. "In value only" repeats P6's "The bottom is her floor, rounded down: money she already owns" as a hedge (Kai, round 2). Its true half, "a fund", survives in the winner |
| Kai: "...buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest it is expected to earn, ..." | 37 | 497 | True; at the cap with nothing spare |
| The thread: same, with "...the interest it should earn..." | 35 | **495** | **Chosen** |

**Why the thread's verb over Kai's.** The pitch already says "only the interest that floor should earn goes into world
stocks". VOICE.md's kill list calls synonym cycling a tell: same thing, same word. "Should earn" is the IPS saying what
the pitch says, in the pitch's verb. It also leaves two words under the cap, and the open item in the D32 README (P3's
"buys a ladder" against P5's "any rung the first $300,000 couldn't buy") is going to want them. Kai's case for "expected"
is fair and written down: it is the prospectus's own register ("is expected to consist almost entirely of cash"), and
"should" could be heard as a promise the fund doesn't make ("does not seek to return any predetermined amount"). I don't
think a judge hears it that way next to "roughly", and the pitch has used "should" since V52 without a cold reader
stumbling. A word is wrong only if it is false; neither is.

**The vote (each vote is my reading of the member from their posts, not their words):**
| Member | Vote | One line, as I read them |
|---|---|---|
| Tess | Thread (495) | Her +11 is over the limit; the swap fixes the false noun she found, and she'd rather cut a word than add eleven |
| Nora | Thread (495) | The cheapest true fix, decided today; her own O1 says a real late-2032 floor "can only be a fund too" |
| Kai | His own (497) | "Expected" is the issuer's word; "should" sounds like a promise. Accepts the result |
| Felix | Thread (495) | The index line decides the noun; the pitch decides the verb |

**Decided, 3-1.** Offer O1 below. Owner: the rewrite thread. By: Wed 4 Nov (Sydney), with the final IPS.

---

## Settlement 2. "About a fifteenth" or "under a tenth"?

**The sentence.** V52 P5: "That is about a fifteenth of her money." (8.) Added to V52 because three of the mock judges
asked how big the stock slice is (D32 README).

**What I checked.**
1. *Today's yield.* Treasury, Daily Treasury Par Yield Curve Rates, October 2026 table, read 2 Nov 2026: 10/30/2026, 2 Yr
   4.56, **5 Yr 4.71**, 10 Yr 4.94. (The November page reads "No Results Found" today.) The floor runs from January 2028
   to December 2032, about five years, so the five-year rate is the one that sets "the interest it should earn".
2. *Kai's arithmetic, re-run* (MODEL, Felix's re-run of Kai's, never for the IPS; one script in the scratchpad, not
   committed). Stocks = 150,000 x (1 - (1 + y)^-4.95). Kai's denominator holds the 2027 ladder at $313,500; mine also
   values the ladder at the same flat yield on 2 Jan 2028 (the ten $50,000 cheques, 5 to 14 years away).

| Five-year yield, Jan 2028 | Stocks | Share, Kai's way | Share, ladder at the same yield |
|---|---|---|---|
| 4.0% | $26,469 | one in 17.5 | one in 18.8 |
| 4.71% (30 Oct close) | $30,560 | one in 15.2 | one in 15.6 |
| 5.0% | $32,184 | one in 14.4 | one in 14.5 |
| 6.0% | $37,584 | one in 12.3 | one in 11.7 |
| 7.0% | $42,690 | one in 10.9 | one in 9.8 |
| A tenth is crossed at | | 7.75% | **6.88%** |

**What it shows.** Kai's sense is right: more interest at higher yields means a bigger slice, because the floor costs
less and the rule hands the difference to stocks. His threshold is a little generous, because he held the ladder's value
still while yields rose; a ladder valued at the same higher yields is worth less, so the stock share climbs faster. A
tenth breaks nearer 6.9% than 7.5%. That is still more than two points above the 30 October five-year close.

And the fifteenth is **not false today**: at 4.71% the rule gives about one in fifteen and a half. It is true at one
yield, fourteen months before the money is spent (4% gives one in nineteen, 5.5% one in thirteen). We take that to mean
it's a forecast in an allocation's clothes, which is Kai's reason, and the reason that holds even if nobody ever opens
WInS. "Under a tenth" is a band the rule stays inside for any five-year yield up to about 6.9%, and every
five-year close on file since September has been between 4.52% and 5.06% (`competition/official_market_data/`, Sep and
Oct 2026 files, plus the 4.71% above), so it describes the strategy rather than one day's curve. Wharton's own line is on that side: "Focus on the strategy and
decision-making framework ... rather than describing individual investments or presenting detailed financial
calculations." (`WHARTON_WORD.md` s2.)

Nora's reason is true and comes second. The frozen book holds VT at 8.6% (snapshot :36), which a fifteenth contradicts
and a tenth doesn't. On its own it wouldn't decide it, because the case says the WInS portfolio "does not determine
Laura's actual portfolio value at the beginning of 2027" (case :129-130, Nora's own F1). But a judge scoring "maintains
consistency with the team's IPS" (`WHARTON_WORD.md` s1) can now divide 26,139 by 305,558 and find the IPS still true. The
three judges who asked how big still get an answer: under a tenth is a size, said without a forecast. No number enters
the IPS that wasn't there.

**The vote (my reading):**
| Member | Swap? | Whose reason | One line, as I read them |
|---|---|---|---|
| Nora | Yes | Hers (the book) | Same eight words, true of the plan and the book, checkable in five seconds |
| Kai | Yes | His (the yield) | The fifteenth is the interest rule's output at today's yields; Book 11 keeps those out |
| Tess | Yes | Kai's | The sentence's job is to say the stocks are small; the tenth does that job and can't be caught by one division |
| Felix | Yes | Kai's, Nora's second | Checked: the fifteenth is true only at one yield; the tenth holds to about 6.9% |

**Decided, 4-0 on the swap; reason 3-1 for Kai's.** Offer O2 below. Owner: the rewrite thread. By: Wed 4 Nov.

---

## Settlement 3. Does "Do not crush." need P9's line?

**My round-1 verdict** was TRUE IF P9 keeps "paying out one bond at a time as each cheque is written". Kai widened it:
selling a rung early also costs the amount, which P3 carries. I've changed my mind, and here's what did it.

**What decided it.**
1. *P3 already holds both halves of the harm.* The schedule: "one rung falling due before each cheque". The amount: "A
   Treasury held to maturity pays exactly what it promises, whatever markets do." Sold early, a rung fetches whatever
   markets do (IBTM prospectus, re-checked: "the market value of such securities is not guaranteed and may fluctuate").
2. *Ahaan said where the power is* (BIBLE Book 11, his words): "The only reason it made sense in the earlier versions was
   because you stated in the introduction that the pills are labelled with 'do not crush' and then you used that phrase
   again in the conclusion. That was the whole power." The last line points back to P2's label, not to the sentence
   before it. My worry that, without P9's clause, "Do not crush." would point at "the order never changes" reads the
   payoff as a reply to its neighbour. Ahaan reads it as an echo of the introduction, and the introduction is what a
   judge remembers.
3. *An instruction can't be false* (Kai). It only has to land, and it lands on P2 and P3.

**Ruling.** No change. P9's clause stays because it answers Wharton's own brief ("managing the operating reserve's asset
composition over time", `WHARTON_WORD.md` s2), not because the last line leans on it. If a later cut ever needs the words,
the clause can be judged on that job alone.

**The vote (my reading):**
| Member | P3 carries it? | Text | One line, as I read them |
|---|---|---|---|
| Kai | Yes | No change | Two anchors, P3 and P9; survives a cut to either |
| Felix | Yes (changed) | No change | P3 holds the schedule and the amount; Book 11 puts the power in the echo of P2 |
| Nora | Yes | No change | Keep P9's clause anyway, for the reserve question Wharton asks |
| Tess | No, needs both | No change | A reader meets "Do not crush." two lines after P9, not seven paragraphs after P3; keep the near anchor |

**Decided, 4-0 on the text; 3-1 on the reason.** No offer.

---

## The offers for the rewrite thread (AI DRAFT, Claude, 2 Nov 2026)

| # | Where | Old | New | Strict cost |
|---|---|---|---|---|
| O1 | P5, sentences 2-4 | "Most of the rest buys Treasuries maturing in late 2032. That is her floor. The remainder, roughly the interest those Treasuries are expected to earn, goes into one world index fund, spread across thousands of companies." | "Most of the rest buys a Treasury fund maturing in late 2032. That is her floor. The remainder, roughly the interest it should earn, goes into one world index fund, spread across thousands of companies." | 36 -> 35, **-1** |
| O2 | P5, sentence 5 | "That is about a fifteenth of her money." | "That is under a tenth of her money." | 8 -> 8, **0** |

**Whole file with both: 496 -> 495 strict** (both counts; `/tmp/claude-0/h015/ips_V52_H015.txt`). Pitch unchanged at 50.
Word diff against V52: "Treasuries" -> "a Treasury fund"; "those Treasuries are expected to" -> "it should"; "about" ->
"under"; "fifteenth" -> "tenth". Nothing else moves. No model number, no "our model", no team history, no subheading.

**No change, with the one-line reason:**
| Line | Verdict | Why |
|---|---|---|
| Pitch: "Her first $300,000 buys Treasuries that each mature before a January." | Keep (thread's call) | TRUE IF "Treasuries" takes in the funds, which P3 says outright; case :129-130 keeps the book from being the reading |
| Pitch: "Her 2028 deposit buys a Treasury floor for her building gift" | Keep | "Treasury" is an adjective here, and it now agrees with O1's "a Treasury fund" |
| P2: "To a pharmacist, XR means extended release" | Keep | WA Health: "XR" / "Extended release" (re-checked) |
| P2: "a caplet that delivers its dose on schedule, labelled do not crush" | Keep | Panadol Osteo PI: "The caplets must not be crushed." (re-checked); the US Tylenol 8 HR label is the Window's |
| P2: "Crush it and the schedule is gone." | Keep | CMAJ 2005: "Crushing the tablet destroyed the drug's sustained-release properties" (re-checked) |
| P2: "ten holdings, one redeemed for each January" | Keep | IBTE's SEC notice: "the Fund will automatically redeem your shares for cash"; TreasuryDirect: "get the money (redeem it)" (both re-checked). Tess's "paid out" (+1) not needed |
| P3: "funds that mature like bonds" | Keep | iShares: "designed to cease trading and mature ... like an individual bond"; adding "designed to" (+1) copies the issuer's legal caution, a hedge |
| P3: "A Treasury held to maturity pays exactly what it promises, whatever markets do." | Keep | 31 CFR 356.30 (re-checked); "the dollars" (+1) adds nothing; Kai's +4 withdrawn by Kai |
| P6: "every dollar she promises is already in bonds" | Keep | "She" is Laura; the case uses the verb for her ("If Laura promises more than she can ultimately contribute", case :114). Tess's +4 out |
| P9: "paying out one bond at a time as each cheque is written" | Keep | Not a condition for the last line any more; it stays for Wharton's reserve question |
| P10: "Do not crush." | Keep | Lands on P2 and P3 (settlement 3) |
| The name against the trader's caplet (an option) | Keep | Nobody is misled; a disclaimer costs 17 and puts the file over 500. Final Report line only |
| A "scaled" bridge sentence (Nora's +9 fallback) | Not in the IPS | Wharton: the IPS is "rather than describing individual investments"; the Final Report evaluates "how effectively it implemented that strategy" |
| Tess's "floor in value only" (+11) | Out | 507, over Wharton's 500; repeats P6's "rounded down" |

---

## Reading slip S-11 (the Library's one slip today; row in the room file's column order)

| # | Date | Reader | Source | Reminds me because... | Part for part | Felix | Kai | Verdict |
|---|---|---|---|---|---|---|---|---|
| S-11 | Mon 2 Nov | Felix (far scout, Opus 5.5; tested in round 3, after Kai's round 2) | (1) Selina Taylor ("Rural pharmacy academic, Mount Isa Centre for Rural and Remote Health, James Cook University") and Beverley Glass ("Professor of Pharmacy, College of Medicine and Dentistry, James Cook University"), "Altering dosage forms for older adults", *Australian Prescriber* 2018;41:191-3, "3 December 2018", DOI 10.18773/austprescr.2018.063, https://australianprescriber.tg.org.au/articles/altering-dosage-forms-for-older-adults.html, accessed 2 Nov 2026, re-checked by the Library (3/3) and re-fetched in round 3 (4 more lines): "The limited availability of oral liquids, patches and suppositories means that crushing tablets and emptying powder from capsules is very common, particularly in aged-care facilities and nursing homes."; "If the medicines are essential, find out if there are alternative formulations."; "If a controlled-release formulation is crushed, the duration of the drug's activity is reduced and the entire quantity of the drug may be immediately released resulting in toxicity."; table: "Paracetamol 665 mg controlled-release film-coated tablets" / "Paracetamol 500 mg tablets (plain or dispersible form)". (2) Panadol Osteo CMI, Haleon Australia, "prepared in January 2026", https://www.safetyandquality.gov.au/medicine-finder/panadol-osteo-modified-release-caplets, accessed 2 Nov 2026, re-checked: "Do not suck, crush or chew the caplets because that may affect its sustained release properties." | People crush a slow-release tablet when there's no other form to give, and the pharmacist's fix is not a sterner label but a second form you're allowed to break; Caplet XR keeps the "do not crush" rule believable the same way, by handing Laura a half she may sell any day | "Specifically designed to deliver the drug over a prolonged period of time" = the ladder, one rung falling due before each cheque (P3, P9). The "do not crush" caplet = the rungs and the last line (P2, P10). "Limited availability of oral liquids" = a cash need before 2033 with nothing liquid to meet it, the building costing "more in Taiwan dollars" (P6). Crushing = selling a rung before its date. "Duration ... reduced" = a January left without its bond ("the schedule is gone", P2). "Find out if there are alternative formulations" / the plain 500 mg tablet = the half of her stocks that "stays with Laura, liquid any day, as her flexibility" (P6) | **Holds in the mechanism, not just the surface:** the journal's crushing happens because no other form exists, and the fix is to supply one. V52 does exactly that: the only cash need the case gives Laura before 2033 besides the cheques is the building, and P6 meets it with money she may sell, so nobody has to touch a rung. **Breaks:** (1) the journal's main harm, toxicity from "the entire quantity ... immediately released", doesn't carry; a rung sold early pays the market's price, and V52 rightly says only "the schedule is gone". (2) The journal's alternative is the same drug (500 mg plain does the 665 mg's job with more doses); Laura's half is not the same medicine: stocks can't pay a cheque on a date. It takes the pressure off the rungs; it doesn't stand in for them. (3) **This one matters:** the alternative can be partly used up. P8 sets the reinvestment gap aside "from the stocks Laura keeps", which is the same half P6 calls "her flexibility", so in the bad case (yields low for years) the breakable form is smaller just when a rung looks tempting. That's the D32 README's open item, now with a reason. (4) The people don't travel: frail older patients and their carers in aged care; Laura is neither. (5) The leaflet says "may affect", softer than "gone"; this slip doesn't stand on "gone" (CMAJ does, Kai's find) | "Who says?": a peer-reviewed independent bulletin, by a rural pharmacy academic and a Professor of Pharmacy at an Australian university; the caplet's own sponsor, on the national safety commission's medicine finder. Every line re-fetched today. True of the plan? Yes: P6's half exists "in case the building costs more", which is the one pre-2033 need the case gives her. "So what?" As a picture in the IPS: yes, so what (a second medical image, and aged care on a page about a philanthropist; DROP). As a check: no. It says P6's liquid half and "Do not crush." are one idea, not two, which is Wharton's own question ("How will your strategy protect the operating commitment while preserving flexibility for a responsible facility contribution?"), and it turns break (3) into a question the Lab can answer | **KEEP narrowly** (Investment Strategy; the IPS question on protecting the operating commitment while preserving flexibility): no new words. A rule for the Writing Room: while "Do not crush." stays, P6's "liquid any day, as her flexibility" clause stays with it, because a rule against breaking is believed only when there is something she may break. To the Long Room before any use. **DROP** for the IPS and pitch: the journal, aged care, toxicity, "alternative formulation". **Final Report:** break (3), sized by the Lab (how much of the flexible half the reinvestment gap can take) |

---

## Seeds (left open on purpose)
1. **P6's "that half moves into Treasuries", the same check as P5.** WInS lists no Treasury bond maturing Feb 2031 to Feb
   2036 (ground truth s5, from `COMPETITION.md`), so the half that moves in 2031 for a gift paid in January 2033 can only go
   into a fund like IBTM, or into bills if WInS lists them. Is "Treasuries" there the noun O1 just fixed in P5? Kai ruled
   the line TRUE ("in bonds" is the claim that counts). The Library checks what the 2031 move actually buys before the
   final IPS (end of Wed 4 Nov, Sydney). Any fix has two words under the cap.
2. **The flexible half's two jobs (S-11, break 3).** P6 calls the kept stocks "her flexibility"; P8 makes them the first
   payer of the reinvestment gap. How much of the "alternative formulation" is left in the bad case? For the Lab
   (sized, MODEL) and the Final Report; for the IPS only if one plain clause fits in the two words of room, which it
   probably doesn't.
3. **The Final Report's bridge to the book.** The WInS book is the finished plan scaled to $300,000 (rungs about
   two-thirds size; IBTM doing two jobs); the pie chart calls the iBond funds "Long Equities" (61.6%) when they're about
   91% Treasuries (`COMPETITION.md`:117-118); VT at 8.6% against the plan's share; and my floorlet line ("Our one open
   risk, coupons reinvested at lower yields, is what an interest-rate floor insures and what a zero-coupon STRIPS bond
   never carries. Wharton bans both ...", AI DRAFT, round 1). Owner when the instructions land: Tue 10 Nov 01:00 Sydney.

---

## New source lines fetched in round 3 (all read Mon 2 Nov 2026)
WebFetch hands back a small model's extract and quotes at most about 125 characters at a time, so long sentences came
back in pieces, asked for in order and joined here with " / " where the join is mine. "Found" means the words came back
in the fetched text, not a byte check.

1. **iShares, IBTM summary prospectus** (cover "FEBRUARY 27, 2026"),
   https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf: "The
   Underlying Index consists of publicly-issued U.S. Treasury securities that are scheduled to mature between" / "January
   1, 2032 and December 15, 2032, inclusive."; "By December 15, 2032, the Fund is expected to consist almost entirely of
   cash."; fund name as printed: "iShares iBonds Dec 2032 Term Treasury ETF".
2. **U.S. Department of the Treasury, "Daily Treasury Par Yield Curve Rates"**, October 2026 text view,
   https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610:
   rows (2 Yr / 5 Yr / 10 Yr) 10/26/2026 4.68 / 4.84 / 5.00; 10/27/2026 4.70 / 4.82 / 4.99; 10/28/2026 4.67 / 4.85 / 5.05;
   10/29/2026 4.61 / 4.78 / 4.98; **10/30/2026 4.56 / 4.71 / 4.94**. The November view
   (`...field_tdr_date_value=202611`) returned "No Results Found." Found from
   https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics.
3. **Taylor and Glass, *Aust Prescr* 2018** (URL in S-11): authors as printed, "Rural pharmacy academic, Mount Isa Centre
   for Rural and Remote Health, James Cook University, Queensland" and "Professor of Pharmacy, College of Medicine and
   Dentistry, James Cook University, Townsville, Queensland"; "3 December 2018"; "DOI: 10.18773/austprescr.2018.063";
   "As many as one in five older patients has difficulty swallowing and may have problems taking tablets and capsules.";
   "The limited availability of oral liquids, patches and suppositories means that crushing tablets and emptying powder
   from" / "capsules is very common, particularly in aged-care facilities and nursing homes."; "It is important to consider
   whether the medicines are still necessary."; "If the medicines are essential, find out if there are alternative
   formulations."; "finding an alternative commercially available dosage form, for example liquid dosage form" (part of a
   longer sentence).
4. **Repo, read at the line:** BIBLE Book 11 (Ahaan, 1 Nov), "The only reason it made sense in the earlier versions was
   because you stated in the introduction that the pills are labelled with 'do not crush' and then you used that phrase
   again in the conclusion. That was the whole power."; `pitch.txt`, "only the interest that floor should earn goes into
   world stocks"; snapshot :36, "VT 8.6%".

Counts: `printf '%s' "..." | python3 keel/office/tools/textcheck.py -` for each sentence (P5 run 36 / 35 / 37 / 47; the
fifteenth and the tenth 8 each), and whole-file scratch copies (V52 496; Kai 497; thread 495; Tess 507; tenth only 496;
both offers 495; Kai's verb + tenth 497). The draft in `D32/` was not touched.

(Keel is a simulated team, AI-written.)
