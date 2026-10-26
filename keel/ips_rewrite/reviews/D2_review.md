# D2 review: pitch + IPS (Caplet XR)

AI-generated review (Claude Code), 26 Oct 2026. Not for submission.

Read cold first, then against `00_GROUND_TRUTH.md`, `NORTH_STARS.md`, `INSTRUCTIONS.md` (I01-I12, I34-I37), `R03`,
the case, the IPS instructions, the D1 lab numbers and R02. Sections 1-3 were written before reading the D2 README.

Gut reaction on the cold read: this is the first version that sounds like a team with a point of view rather than a
committee with a template. The one-line "We refuse.", the human-capital line and the home-made note are the
three things that make it. The facility paragraph is where it wobbles: on first read I could not tell what money buys
the stocks, and "the floor last" made me scroll back up to check whether the floor was a promise or not.

---

## 1. Cold read: two mock judges

### (a) Wharton undergraduate evaluator (60-second skim with the rubric, then a full read)

Skim: the first line is a scene, not "This IPS outlines"; the eye drops to "We call it Caplet XR", "To a pharmacist",
then the one-line "We refuse." and the "Ten cheques, ten Januaries" close. That's enough to stop skimming. Full read:
the payment logic is clear inside 30 seconds (one Treasury per payment, bought first, latest first). The "Laura
already owns plenty of stock-market risk – it just isn't in a brokerage account" line is the moment this reader
decides the team understands the client, not just the case. The bank-note paragraph impresses but loses them at
"The rest of the 2028 deposit buys a Treasury fund ... Its expected interest buys one world index fund" – if the rest
of the deposit bought the fund, what bought the stocks? "Do not crush" reads as a typo or an in-joke. They notice
there is no confidence level anywhere and assume (rightly) it is coming in the Final Report.

| Criterion | Score |
|---|---|
| Investment Strategy | 8 |
| Client Knowledge | 8 |
| Portfolio Analysis | 6 (no numbers, by design; the floor arithmetic is unclear) |
| Articulation of Competition Experience | 4 (the IPS can only show this through "Our WInS portfolio is this plan in miniature") |
| Creativity & Presentation | 9 |
| **Total** | **35/50** |

Remembers an hour later: "XR = ten redemptions", "We refuse.", "home-made capital-protected note".
Confused by: what buys the stocks; "do not crush"; "the cheque shrinks" (which cheque? the word meant the $50k
payments two paragraphs earlier, now it means the 2028 deposit).

### (b) Asset-management professional

Reads it as a liability-driven plan: a cash-flow-matched Treasury ladder bought longest-first, then a static floor-plus-
cushion structure (CPPI at a multiplier of 1, no rebalancing, so no gap risk) for the surplus. They recognise the
time-diversification point ("time shrinks the chance of a stock loss, not its size") and like that nobody spelled out
its source. They respect "near-ironclad" for the iBonds because the draft says why (held to the December close, the
bonds inside have matured). Three things irritate them. First, "We keep the bond and drop the rest": the team did
not drop the market exposure, it swapped the option for the stocks themselves, and a professional notices the
difference (linear payoff, no convexity, no premium). Second, "any gap comes from Laura's half first, the floor last"
sits two paragraphs after "her floor, intact even if every share went to zero" and "a number said aloud cannot be
half-kept"; so is the floor a commitment or the last line of defence? Third, "rising Taiwan costs are the index fund's
job" hands inflation protection to a sleeve that is roughly a fifth of the 2028 money and held about five years;
stocks hedge inflation over decades, not reliably over five years (2022 is the counter-example everyone remembers).

| Criterion | Score |
|---|---|
| Investment Strategy | 8 |
| Client Knowledge | 7 (human capital excellent; no confidence statement; inflation line thin) |
| Portfolio Analysis | 6 |
| Articulation of Competition Experience | 4 |
| Creativity & Presentation | 8 |
| **Total** | **33/50** |

Remembers: "ladder bought latest-first; capital-protected note without derivatives; the 2028 deposit is correlated
with the ladder's main risk". Confused by: the floor's priority in a coupon shortfall; "drop the rest"; how a
Treasury fund is "redeemed".

---

## 2. Hard faults only

Strong but true words ("near-ironclad", "We refuse.", "intact even if every share went to zero") are not flagged.

| # | Line | Fault | Why, precisely | Fix |
|---|---|---|---|---|
| H1 | "The rest of the 2028 deposit buys a Treasury fund maturing in December 2032, sized to grow back to about that sum ... Its expected interest buys one world index fund" | Ambiguity that will confuse every judge; read literally, it is arithmetically impossible | If "the rest" buys the fund, nothing is left for stocks. What the plan does: buy enough of the fund that it grows back to the whole remainder; the difference (the discount, i.e. its expected interest) buys stocks today. "Interest" not yet earned cannot buy anything, so the sentence needs "the difference" as the subject | "Part of what is left of the 2028 deposit buys a Treasury fund maturing in December 2032, sized to grow back to the whole of it – her floor, intact even if every share went to zero. The difference, its expected interest, buys one world index fund of 10,000 companies." |
| H2 | "any gap comes from Laura's half first, the floor last" vs "her floor, intact even if every share went to zero", "a commitment rather than a forecast", "a number said aloud cannot be half-kept" | Internal contradiction (as a judge will read it) | The floor is protected against stocks but, per this sentence, not against a coupon shortfall. A reader who has just been told the bottom is a commitment is then told it can be spent. The lab puts an uncovered coupon gap at ~5.9% of paths (MODEL), so the honest statement exists; it just has to be framed so it does not undo the promise. Vote D1a is still open (ground truth s4) | Either (D1a "no") "any gap comes from Laura's half, never the floor" and quote the 2031 bottom with the D1b margin, or (D1a "yes") say it before the promise: "the bottom is rounded down so that even a coupon shortfall cannot reach it". Do not leave "the floor last" as a bare clause |
| H3 | "We keep the bond and drop the rest." | False as a description of the plan | A capital-protected note = bond + call option + fee. Caplet keeps the bond, replaces the call with the underlying stocks (bought with the discount) and drops the fee. It does not drop the market exposure; the next sentence buys it | "We keep the bond, buy the stocks outright instead of the option, and skip the fee." |
| H4 | Pitch: "Her first $300,000 buys a Treasury for each of ten $50,000 payments." | Stated flat; true in about half of today's model paths | Ladder cost $298,861 on the 22 Oct close, over $300k in 47% of paths (lab (a)). The IPS body has the conditional ("any gap is the second deposit's first job"); the pitch, read alone, does not. The locked IBTR note already says the 2028 deposit may top up. Small, but it is the pitch | Keep as is only if the body keeps the gap clause (it does); otherwise "buys a Treasury for each ... payment, latest first". Low priority |
| H5 | "ten Treasuries, each redeemed in time for one January" | Loose, not false | Five of the ten are iBond ETFs, which liquidate at NAV rather than being redeemed at par. The next paragraph says so ("bond or defined-maturity Treasury fund"), so a judge is not misled. A pro may smile at "redeemed" for an ETF; it is defensible (the fund terminates and pays out) | No change needed; noting it so nobody "fixes" the motif later |
| H6 | "the slump that shrinks that income would likely cut yields too, making bonds dearer just as the cheque shrinks" | Ambiguity | "Cheque" is the motif word for the $50k payments (first and last lines); here it means the 2028 deposit. A skimmer reads "the payment shrinks", which is wrong | "... just as the deposit shrinks" |

No rule breaches: no TIPS, STRIPS, derivatives held, citations, links or charts; the bank note and option are named
only as what the plan avoids. No contradiction with a locked TNA line: IBTM as payment 1 and floor (yes, implicitly),
VT as the only growth, stocks set only how far the gift rises above the minimum, short-term Treasury fund for coupons,
2028 deposit tops up the ladder first, "near-ironclad" (TNA reflection 1 uses it). Case facts all correct (dates,
amounts, no outside funding, the four income sources shortened to two, which is fine).

Not a fault, but a professional will challenge it: "rising Taiwan costs are the index fund's job" (see judge (b)).
It is a defensible assumption, not a false one; it would be stronger if it said what the plan does when costs outrun
the stocks (the gift is a dollar range, so the facility budget, not the reserve, absorbs the difference).

---

## 3. North-star audit

### Star 1, voice: 7/10
What already matches R03:
- Move 1 (opens on a concrete scene): "In January 2033 Laura's portfolio writes the first of ten $50,000 cheques". Yes.
- Move 5 (one-line paragraph after a long one): "We refuse." Exactly Ray's "We do." Best line in the draft.
- Move 2 (voice the other side, then dismantle): "Moving floor money into stocks would raise the expected gift. But
  ..." Good, though the sceptic speaks in the team's register, not their own.
- Move 14 (one rhetorical question, answered at once): "Why every payment before a single share? Because ...". Yes.
- Move 10 (wry line in a formal register): "it just isn't in a brokerage account". Yes.
- Move 18 (ending calls back to the opening): "Ten cheques, ten Januaries". Yes.
- Rhythm is lumpy (sentences from 2 to 36 words). Good.

What still reads as AI, and why:
- **Balanced semicolon antitheses** (six semicolons in 487 words). "The price is a smaller boom; the reward, nothing that
  can expire worthless." is the purest machine sentence in the draft: gapped verb, perfect parallel, moral at the end.
  Ray's essays don't balance; they land.
- **"X, not Y" / "X rather than Y" four times**: "never all at once", "a commitment rather than a forecast", "over
  decades, not every two years", "the chance ... not its size", plus the pitch's "Stocks move the ceiling. Never the
  floor." R03 says use it once. Keep "not its size" (it carries an idea) and the pitch line; cut the rest.
- **Nested parenthetical with em-dash pair inside a colon**: the 36-word 2031 sentence. Hard to parse, and it is the
  sentence carrying the range rule.
- **Participial opener + semicolon + explanation**: "Held to their December close, the funds are near-ironclad too;
  their bonds have matured into cash." Correct, airless.
- **No numerals, no joking bracket (move 13), no personal connective (move 16).** "ten" is fine (motif), but there is
  no "Alas", no "(a non-exhaustive list)" wink anywhere. One bracket would do more for "human" than any word swap.

Three worst sentences, rewritten in Ray's voice, equal or shorter:
1. "The price is a smaller boom; the reward, nothing that can expire worthless." (13)
   -> "The catch? A boom pays her less. Nothing here can expire worthless." (12) *(note: this would be the
   second rhetorical question; if kept, change "Why every payment before a single share?" to a statement, or use
   "The catch: a boom pays her less. Nothing here can expire worthless.")*
2. "Held to their December close, the funds are near-ironclad too; their bonds have matured into cash." (16)
   -> "The funds are near-ironclad too. By their December close, they hold nothing but cash." (14)
3. "In 2031 Laura gives co-sponsors a range: from the floor's projected payout, rounded down – money she already holds,
   a commitment rather than a forecast – to that plus half her stocks' value on the day." (36)
   -> "In 2031 Laura names a range. The bottom is the floor's payout, rounded down: money she already holds. The top
   adds half her stocks, valued that day." (27)

Single change that raises voice most: kill the balanced semicolon sentences (rewrite 1 and 2) and add one joking
bracket somewhere it earns a laugh and a fact, e.g. after "one world index fund of 10,000 companies (picking winners
is not on the menu)" – which also echoes TNA note 3's "vain illusion that we can pick winners".

### Star 2, motif: 7/10
Bare bones are all there and done with restraint: both meanings of XR in two sentences, X = ten (Roman numeral),
R = redemption (a real bond word, which fixes I34's "ten releases" problem), "releases ... on schedule" in the pitch,
"do not crush" as a late callback, "ten cheques, ten Januaries" at the close. It never takes over a sentence that has
investing work to do. That is exactly the "subtle, not a crutch" brief.
Weakness: "do not crush" is a callback to something that was never planted. Readers who don't know XR pill labels
will not get it, and the line it sits in ("nothing is sold early") is the plan's one hard discipline rule.
Single change: plant it in the pharmacist sentence – "To a pharmacist, XR means extended release: a dose let out on
schedule, never all at once, and a label that says do not crush." – then the later "do not crush" pays off. (+8 words;
fund it from the cut in section 6.) Alternative at zero words: delete "– do not crush" and lose the joke.

### Star 3, extraordinary / "aha": 8/10
Four real ahas in 487 words: (i) the facility gift as a home-made capital-protected note with the option and fee
stripped out; (ii) Laura already holds equity risk through her career, and it is correlated with the ladder's main
risk; (iii) time shrinks the chance of a loss, not its size; (iv) "Laura risks only money she hasn't earned yet". No
other team will have (i) and (ii) together. What is missing is the aha that answers the case's hardest question
directly: how confident can co-sponsors be in the range? (See section 5.)
Single change: replace a weaker line with the two-year-window sentence in section 5.

### Star 4, investing knowledge applied: 8/10
Applied without names: liability-driven investing, cash-flow matching, latest-maturity-first, defined-maturity ETF
(NAV), pull-to-par (implicitly, via the December close), human capital (Bodie-Merton-Samuelson), principal-protected
note decomposition, static CPPI at multiplier 1, time-diversification fallacy (Bodie), reinvestment risk, maturity-
before-payment liquidity. That's a professional's toolkit, used rather than listed.
Two dents: "drop the rest" (H3) is wrong in exactly the place where knowledge is on display, and the inflation line
leans on a short-horizon stock hedge that a pro will question.
Single change: fix H3 to "keep the bond, buy the stocks outright instead of the option, and skip the fee". That one
clause shows the team knows why a call and a cushion of stocks differ, and costs 4 words.

---

## 4. Requirements coverage (IPS instructions p.2, plus the case's reserve and certainty asks)

| Item | Covered? | Where / gap |
|---|---|---|
| What the team is trying to accomplish | Yes | Opening scene (ten payments, nobody else may help) + the facility paragraph + "for flexibility" |
| Why the strategy suits the client | Yes, strongly | Human-capital paragraph is the best client-fit argument any team will make. Could tie once to her "thoughtful risks" (case p.2); not needed |
| Balance: growth | Yes | One world index fund bought with the floor's interest |
| Balance: liquidity | Yes | "something matures before every January, and the funds trade daily" |
| Balance: funding reliability | Yes | Definition paragraph |
| Balance: risk | Yes | "The soft spot is reinvestment"; "We refuse." |
| Balance: flexibility | Thin | One clause: "the other half stays with Laura, for flexibility". It never says what the flexibility is FOR (the case: "as the project develops"). Three words would fix it: "for flexibility as the project grows" |
| Guides construction and decisions as needs change | Partly | Rules present: payments first, latest first, 2028 deposit fills the gap first, nothing sold early, coupons parked, reserve rolls down, yearly review. Gap: what happens if the 2028 deposit is smaller, or yields move before Jan 2028? The rule already answers it (the floor is sized to whatever is left; higher yields mean a bigger stock budget, lower yields a smaller one, lab (b)) but the draft never says so. That self-sizing property is a free decision rule worth a clause in the Final Report at least |
| Protects payments while supporting the contribution | Yes, strongly | The whole architecture; "Stocks move the ceiling. Never the floor." (pitch) |
| Reserve composition over time | Yes | "the payment holdings become the operating reserve, one fewer each January"; coupons in a short-term Treasury fund. Size is implicit (the ladder) and the IPS is not asked for the number |
| Definition of high certainty | Yes | Structural: every payment in its own Treasury bond or term Treasury fund maturing before its date, by Jan 2028. Gap: the case also asks how it was evaluated; one clause ("tested against falling yields and a missing deposit") would signal the Final Report's work. Optional at 500 words |
| Assumptions: investment performance | Yes | "stocks beat Treasuries over decades, not every two years" |
| Assumptions: timing of cash flows | Implicit | Start-of-year payments and maturities before each January; fine |
| Assumptions: outside funding | Yes | "nobody else may help" |
| Assumptions: inflation on projections AND facility costs | Yes, but weak | Payments: correct (nominal). Facility: "rising Taiwan costs are the index fund's job" (see section 2 note). Better: say the gift is in dollars, so cost overruns fall on the facility budget and co-sponsors, which is exactly why Laura keeps half |
| Portfolio construction and diversification (p.2) | Yes | "one world index fund of 10,000 companies" |
| Range + confidence | Not required in the IPS | The case asks for a confidence level; the IPS has none and is not required to. Section 5 gives the sentence that sets it up |

Pitch (47 words): states the central idea and how it supports the goals. Passes. It is the plainest text in the
submission; it has the motif only in "releases ... on schedule". Fine: the pitch's job is clarity.

---

## 5. The one missing idea

The case's hardest ask is confidence in the 2031 range, and the draft's structure already contains the best answer
to it without saying so: once the top is named in 2031, the gift is the top minus half a put on world stocks struck at
that day's level. So the only window in which stocks can make Laura miss her top is the final two years, not the six
she holds them (within-horizon risk, measured at the point where the promise is made). That is a finance judge's
"aha", it turns "how confident?" from a feeling into a two-year question, and the lab confirms it (MODEL: below the
top in 24.4% of paths; 21.2 points of that are stock falls in the window, the other 3.2 points are a payment needing
help or IBTM paying slightly short).

Exact sentence (21 words), placed straight after "In 2033 the same rule sets the gift, capped at that top; the other
half stays with Laura, for flexibility.":

> After 2031, the gift misses its top only if world stocks fall over the last two years or a payment needs help.

It replaces "The price is a smaller boom; the reward, nothing that can expire worthless." (13 words), the most AI
sentence in the draft (section 3). Net +8 words, funded by section 6. Do not add "and never below the bottom": with
D1a "yes" a coupon gap can reach the floor (gift inside the range 99.2%, MODEL), so that clause would be false.

Runner-up (if the team prefers a ladder insight): "Cash is not safe for Laura; it is the one rate she cannot
predict." (the riskless asset is the bond that matches the liability). Good, but the two-year window answers a case
requirement; this one doesn't.

---

## 6. Word budget

Cut one whole idea:
- **"So we start at the end and work backwards." (9 words).** It announces a method the next four paragraphs
  demonstrate ("latest-dated first", "any gap is the second deposit's first job"), and "start at the end" is a stock
  phrase. The opening scene goes straight into the name paragraph without loss; if anything, "nobody else may help."
  followed by "We call it Caplet XR." is a better turn.

Do not cut: "we review the plan with Laura yearly" (judges look for a review clause; its loss was flagged in the
16 Oct pre-mortem), "and the funds trade daily" (the only liquidity point beyond maturities, and it echoes TNA note 2),
"Our WInS portfolio is this plan in miniature" (the IPS's only link to the frozen book and to Articulation).

Tally if every fix in this review is taken (by spaces, from 487):

| Change | Words |
|---|---|
| Cut "So we start at the end and work backwards." | -9 |
| Rewrite 2 (December close) | -2 |
| Rewrite 3 (2031 range) | -9 |
| Section 5 sentence replaces "The price is a smaller boom ..." | +8 |
| H1 fix (what buys the stocks) | +4 |
| H3 fix ("buy the stocks outright instead of the option, and skip the fee") | +7 |
| H6 ("deposit" for "cheque") | 0 |
| Flexibility "as the project grows" | +4 |
| **Net** | **+3 -> about 490** |

The "do not crush" plant (+8) would take it to about 498 by spaces, too close to 500 on the strict count. My call:
plant it anyway, because Ray named "do not crush" as an extension that works and a callback half the judges miss is
wasted. Fund it by folding the rhetorical question into its answer: "Why every payment before a single share? Because
Laura already owns ..." -> "Every payment comes before a single share, because Laura already owns ..." (-3), and
write the flexibility fix as "the other half stays with Laura, for a project still growing" (+1 instead of +4).
That lands at about 492 by spaces.
