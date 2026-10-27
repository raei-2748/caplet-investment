# S5 scout: behavioural and decision science [7], game theory, mechanism design and contract theory [8]

> AI-generated research (Claude, scout S5, 27 Oct 2026), not for submission. Keel recommends, Caplet decides.
> No IPS prose below: ideas and arguments only.

**Method and honesty notes.** I opened real pages for every idea I kept. The fetch tool returns a summary of the page, so
the quoted phrases below are as that tool returned them from the page; each is under 15 words. Where I could only reach
a secondary source (a textbook-style summary, a blog report of a meta-analysis) I say so. The shared fetch budget ran dry
twice, so I did not open McGuire's 1961 original or the Kamenica-Gentzkow "Bayes-plausible" proof line; both are marked.
I never use the CLAUDE.md "building minimum" as a fact about the case: the official client profile gives **no facility
cost and no minimum**, so any provision-point argument below is conditional on a threshold we would have to state
ourselves (Jun would need to model it).

**Triage in one screen.** Kept as real (they change what the plan does or how it is argued): 1, 2, 3, 4, 6.
Kept but demoted to "partly decoration": 5, 7. Bin or one-line only: Kreps-Wilson reputation, peak-end, hold-up
as a stand-alone, narrow bracketing as a stand-alone (all in the last section, with reasons). The sharpest finding of
the domain is idea 3: a sequential leader's gift can *lower* total giving.

---

## 1. Refutational two-sided argument (McGuire's inoculation, 1961, and its meta-analyses)

**Verified.**
- McGuire and inoculation: https://en.wikipedia.org/wiki/Inoculation_theory. Quotes: "Threat provides motivation to protect one's attitudes or beliefs."
  and "Refutational preemption provides specific content that receivers can employ to strengthen attitudes". I did not open
  McGuire's 1961 paper itself: UNVERIFIED at source, verified through the review page.
- The part that matters more than McGuire: the meta-analyses of message sidedness. O'Keefe (107 studies, 20,111 people), reported at
  https://www.spring.org.uk/?p=12521: "two-sided arguments are more persuasive than their one-sided equivalents", but only
  "as long as they are refuted"; a two-sided message that leaves the other side unanswered "can be significantly less persuasive than a comparable one-sided argument."
  Allen (1991, 26 studies), summarised at https://customerthink.com/one-sided-vs-two-sided-arguments/: the ranking is
  "two-sided *with* refutation" first, then one-sided, then "two-sided with *no* refutation". (Both are secondary reports, not the papers.)

**What it is.** If you name the strongest objection to your case yourself, and then answer it in the same breath, readers
rate the case more persuasive than if you ignore the objection. Naming it and leaving it hanging is worse than silence.

**Critique.**
- McGuire's engine is *resistance to a later attack*. A judge reads the IPS once; there is no later attack, and the
  effect decays anyway ("after 13 days", same Wikipedia page, a meta-analytic figure it attributes to others). So "inoculation" is the wrong word for the
  mechanism that helps us. The useful finding is the sidedness meta-analysis: refute in the same text.
- The review page itself flags the failure mode: counterarguments "do not necessarily need to be accurately representative", which it calls a
  straw man. An expert judge punishes a weak sceptic. The sceptic paragraph must state the objection a professional would actually raise.
- O'Keefe found no advantage for one-sided messages even with already-agreeing audiences, so there is no "judges already agree, skip it" escape.

**Fit to Laura.** Fits, and it changes the plan's argument, not its holdings. The objections a professional judge has are
specific: (a) "a Treasury ladder gives up growth, why not stocks for a ten-year horizon"; (b) "the floor is not a fixed
$150k" (the iBond funds' payout is not fixed); (c) "stocks above the floor can fall, so the top is not a promise". Each
has a one-line answer already in the plan (the payments are bought first with her own money; the range's bottom is owned and its top
is reached about 3 times in 4). The idea says: pick the single strongest of those and answer it, rather than a generic
"risks" paragraph. It does **not** say add hedging: the Bible (rule 6) forbids it, and refutation is the opposite of hedging.

**Fusion hook.** With the pratfall effect (idea 2) and the newsvendor decision (covered, R05 #13): the objection and its
refutation become "the error we chose to risk, and why". Synergy: the sceptic paragraph *is* the newsvendor choice stated aloud.

**Logic device.** The "which mistake would you rather make" test: ask the judge which wrong answer is worse, a range that is
too high or too low, then show the plan already picked its side for a stated reason (about 3x worse to over-promise).

**Lands in:** IPS, one clause (the one strongest objection, refuted, in a human voice); the full sceptic exchange in the
Final Report. Evidence to cite there: O'Keefe and Allen, as reported above (re-check against the originals before citing).

---

## 2. The pratfall effect (Aronson, Willerman and Floyd, 1966)

**Verified** at https://en.wikipedia.org/wiki/Pratfall_effect (secondary). Quotes: "a knowledgeable blunderer was rated to be more attractive."
and the mediocre actor "suffered decreases in their perceived attractiveness." Setup per the page: the capable actor answered about 92% of quiz
questions correctly, the mediocre one about 30%; the blunder was spilling coffee. Boundary: observers with high self-esteem
"will prefer the non-pratfalling highly able individual" over an equally able blunderer.

**What it is.** A visibly competent person who admits one small flaw is liked more; a mediocre person who does the same is liked less.

**Critique.**
- It was a *liking* result on a taped quiz contestant, not a credibility result on a written document. The leap from "more attractive"
  to "more trusted by an expert judge" is ours, not the paper's.
- It only works if competence is already established. A plan whose first paragraphs are weak is not rescued by candour.
- The self-esteem boundary matters for judges: a confident, high-status reader prefers the flawless version. A competition judge
  at Wharton is plausibly that reader. The effect is real but small and fragile; I would not hang a design on it.
- A pratfall is an *accident*. A planned admission is a different act (it is a disclosure), so the experiment does not strictly apply.

**Fit to Laura.** Partly. There is one real soft spot the plan already knows: the coupon-reinvestment gap (about $21k on the 16 Oct
sheet if yields fall 2 points for good) and the "floor is not fixed" fact. The Bible says no hedging. The reconciliation is that a
confident, priced, one-clause concession is not a hedge: it states what the plan does not do and what that costs. It fits only
if the concession is **small relative to the strength shown** and **unique** (one, not five).

**Fusion hook.** With idea 1 (same sentence does both jobs) and with the covered "reinvestment shortfall set aside before the gift": the concession
names a cost and the plan's own mechanism that already absorbs it. Neither idea alone reads as strength; together the admission is the proof of control.

**Logic device.** A pilot who tells you before take-off exactly which instrument is out and why it does not matter on this route:
that briefing raises confidence only because the rest of the cockpit is plainly in order. (An analogy, not a source.)

**Lands in:** IPS, as a *constraint on style* for the sceptic clause (one admission, priced); Final Report for the full version.
Do not cite the effect in the IPS. Honest label: modest evidence, so it is a tiebreak for wording, not a pillar.

---

## 3. Stackelberg commitment, and the warning from Varian (1994) that a leading gift can shrink the total

**Verified.**
- Stackelberg leader/follower, commitment must be believed: standard; I did not need a source for the definition. The idea's *test* is the next one.
- Varian, "Sequential contributions to public goods" (J. Public Economics, 1994), as cited in the CESifo working paper
  https://www.ifo.de/DocDL/cesifo1_wp2602.pdf. Abstract quote: "sequential contributions result in lower overall provision than simultaneous contributions".
  The same paper, footnote 1: "Sequential contribution mechanisms may also be effective when there is a provision point".
- Schelling's commitment logic (burning bridges, tying hands) is the intellectual parent; no separate source opened, so treat as background.

**What it is.** Laura speaks first (the 2031 range); co-sponsors respond. Moving first helps only if the move cannot be undone
and everyone knows it. Varian's theorem is the cold shower: in a pure public-good game, when a leader gives more, followers
give *less*, and the total ends up lower than if everyone had decided at once.

**Critique.**
- Varian's result is for a smooth public good with no fixed cost and no "warm glow". Real donors are not that game; the field and lab
  evidence the CESifo paper discusses is mixed. So it is a warning, not a law.
- It assumes followers see the leader's amount and can top up or cut. Co-sponsors who give for relationship, status or a matching offer do not behave like that.
- "Stackelberg" is often name-dropped for any first mover. It needs two real things: observability and irreversibility.

**Fit to Laura.** Fits, in two parts that pull in opposite directions, which is why it is useful.
1. *Irreversibility is exactly what the January 2031 lock buys.* The Courtroom's "lock what you announce" step (covered as a
   liability-driven de-risking) has a second justification the Courtroom did not use: it converts an announcement
   (cheap talk, covered R02 #45) into a leader's commitment co-sponsors can build on. The bottom is owned, the promised half of stocks is moved to Treasuries; she
   cannot be tempted to retreat. This reframes the lock from "safety" to "credibility", which Wharton's criterion on telling co-sponsors clearly and credibly rewards.
2. *The top of the range could crowd co-sponsors out.* A large headline gift tells a Varian-type follower "she has it covered".
   The case says the rest of the facility may come from co-sponsors, grants and others. So the way the range is *framed* matters:
   frame it by the gap it leaves for others (and by a match), not by how big her gift is. The matching result (Karlan-List, covered R05 #18) is the
   known cure, because a match changes the follower's price of giving instead of competing with it.
   Whether this bites depends on a facility cost the case does not give, so Jun would need to model any numbers.

**Fusion hook.** Stackelberg commitment x matching gift x lock-what-you-announce: *the lock is the leader's commitment; the match is the
anti-crowding-out device; the cap is what stops the leader's gift being read as "fully funded".* Three covered pieces become one mechanism with a reason each.

**Logic device.** The ferry-captain test: a captain who announces "I will not leave until the boat is full" gets a full boat only if
the engines are visibly switched off. The lock is the switched-off engine.

**Lands in:** Final Report (co-sponsor draft and Articulation: why we move first and what makes it credible). IPS: at most one clause
("what she announces, she has already locked"), which is a design fact, not a theory. Varian goes in the Final Report as the honest risk to our own framing.

---

## 4. The assurance contract (Bagnoli-Lipman 1989): pledges refunded if the threshold is missed

**Verified** at https://ideas.repec.org/a/oup/restud/v56y1989i4p583-601..html. Quotes: "The set of undominated perfect equilibrium outcomes of this game is exactly the core of the economy."
Paraphrase of the abstract, which the page returned in pieces: the good is provided only if contributions cover its cost, and contributions are refunded otherwise.

**What it is.** A "provision point with money-back guarantee" (the logic behind crowdfunding). Because nobody loses money if the threshold fails,
giving is never a sucker's bet, and the model shows the efficient outcome can be reached by voluntary gifts.

**Critique.**
- The model is for a complete-information economy and a known cost. We have neither: the case gives no facility cost, and co-sponsors' valuations are private.
- It fixes the free-rider problem on paper; in practice crowdfunding fails often when the threshold is set badly. A threshold that is too low
  funds a building nobody can operate. Here that is a real danger, see idea 7.
- Conditional gifts are already in our covered list (R05 #17 conditional vs unconditional promises; Andreoni seed money, R02 #46). The *refund rule*
  is the only new piece.

**Fit to Laura.** Partly, and for a precise reason. Laura's two layers are already of different kinds: the bottom is owned and unconditional; everything above it
is a promise to give *if* the facility is genuinely going ahead. The refund clause says what happens to the conditional part (it stays hers) and, from the
co-sponsors' side, makes their own pledges safe: they pay in only if the building is real. That is exactly what keeps "committing all her assets" from
crowding out her flexibility (case: "committing all remaining assets could limit her financial flexibility").

**Fusion hook.** With "the cap at the top, the rest stays Laura's" (current plan) and idea 3: the *cap* protects Laura's flexibility; the *refund* protects the co-sponsors'
trust; together they make a two-sided safe commitment neither side can regret. Synergy: flexibility for her, safety for them, one mechanism.

**Logic device.** Kickstarter's all-or-nothing rule as the analogy a judge already knows: "you are only charged if it funds".

**Lands in:** Final Report (co-sponsor text; one paragraph). Not in the IPS: the IPS is a framework and the co-sponsor draft belongs to the Final Report (Bible rule 8).
Dominant assurance contracts (a bonus paid if the threshold fails) I did not verify: UNVERIFIED, drop unless Jun finds the source.

---

## 5. Focal points (Schelling) and precise numbers (Mason et al.; Pope-Simonsohn): which numbers to publish in the range

**Verified.**
- Focal points: https://en.wikipedia.org/wiki/Focal_point_(game_theory). Quotes: Schelling's "noon at (the information booth at) Grand Central Terminal" meeting
  answer; in the divide-$100 game "36 out of 40 chose $50"; limits: "the conspicuousness of the focal point depends on time, place and people themselves."
- Precise first offers: https://sciencedaily.com/releases/2013/06/130601133931.htm (Mason, Lee, Wiley and Ames, 2013). Quotes: "the person making a precise offer is successfully giving the illusion they have done their homework."
  and "When perceived as better informed, the person on the opposite end believes there is less room to negotiate." (Study: 1,254 fictitious negotiators, hypothetical scenarios.)
- Round numbers as goals: https://www.sciencedaily.com/releases/2011/01/110119120552.htm (Pope and Simonsohn). Quote: players are "four times more likely to end a season with a .300 batting average than a .299 average."

**What it is.** Two opposite effects: round numbers are natural meeting points and goals; precise numbers read as "someone did the sums" and anchor harder.

**Critique.**
- The precise-offer study is hypothetical haggling over a car or jewellery, not a pledge drive. The batting-average study is about self-set goals, and the
  same article notes SAT 1390 vs 1400 made no admissions difference: round-number salience can be real and still irrelevant.
- Focal points need common knowledge and shared culture; co-sponsors in Taiwan, the US and elsewhere may not share a "salient" number.
- The two effects conflict, so the evidence does not tell us which wins for co-sponsors.

**Fit to Laura.** Seems relevant, mostly isn't, with one real use. The seed said "round numbers for the 2031 range". But a round top that is the *derived* figure
rounded up is the over-promise risk the newsvendor logic is built to avoid; and the bottom is a computed floor, where precision is honest. The real use: publish
the *bottom* precisely (it is owned and computed) and the *top* as a round, goal-like number that co-sponsors can aim at, **rounded down, never up** (the cap makes
"inside the range" true by construction, covered R05 #14).
Careful of the planned "$145k bottom" (the $150k floor rounded down): that is a deliberate round number, so the plan already does one half of this by instinct.

**Fusion hook.** With the cap/newsvendor (covered): *round down for the bottom, round to a goal for the top* is the only way to be both honest and focal. Weak synergy.

**Logic device.** None strong. The Grand Central story is memorable but only as analogy for "co-sponsors who cannot confer pick the obvious number".

**Lands in:** Final Report (one line in the co-sponsor draft on how the numbers are chosen). Not the IPS. Mark as modest.

---

## 6. Bayesian persuasion (Kamenica and Gentzkow, 2011): how much should the range disclose?

**Verified** at https://web.stanford.edu/%7Egentzkow/research/BayesianPersuasion.pdf. Quotes: "a sender chooses a signal to reveal to a receiver,"
the receiver "then takes a noncontractible action that affects the welfare of both players."
"A key assumption of our model is that Sender cannot distort or conceal information once the signal realization is known."
and, of the prosecutor example: "the judge knows 70 percent of defendants are innocent, yet she convicts 60 percent of them!"
(Example: prior of guilt 0.3; a fully informative investigation convicts 30% of the time, the optimal binary signal 60%.)
The "average posterior equals the prior" property (Bayes-plausibility) is the paper's central constraint, but I did not quote it: UNVERIFIED line, standard result.

**What it is.** The sender can design *what the receiver will learn* (a coarse report instead of the full truth). If done cleverly, the receiver takes the sender's preferred action more often, while still updating correctly.

**Critique.**
- It is a model of persuasion for the sender's gain. Applied to Laura it is ethically backwards: the optimal signal pools bad and good states so the receiver acts when she
  "should not". Wharton's Creativity and Presentation criterion asks for the facility contribution "and its uncertainty told clearly and credibly". A judge who sees "optimal persuasion"
  in the plan will smell manipulation.
- The model needs the sender to commit to the signal in advance and the receiver to be Bayesian. Co-sponsors are people, and Laura has no way to tie herself to a signal structure.
- No transfers or side effects on the receiver's payoff are allowed in the model; matching gifts break that.

**Fit to Laura.** The seed ("how much does the range disclose") fits as a *test*, not a tool. Its one strong result is the martingale idea: a signal cannot raise the receiver's
*average* belief; it can only move probability between outcomes. So, as a calibration check, "if co-sponsors on average end up expecting more than our own central estimate, we have
leaned on them". Applied to the plan: the range should make co-sponsors' *expected* facility gift equal what Laura's own model expects. Jun would need to model that comparison; I have not.

**Fusion hook.** With interval scoring/calibration (covered R05 #14) and the newsvendor (covered): a **one-line honesty test** for the range, stated in the Final Report, that the average co-sponsor belief after the announcement equals our central estimate. Synergy: it turns "credible" from a word into a testable property.

**Logic device.** The 0.3 / 60% prosecutor example as a *cautionary tale*: this is what a range would look like if built to persuade; ours deliberately is not.

**Lands in:** Final Report (a short methods box in the co-sponsor section, or Articulation). Bin for the IPS. Honest verdict: a good argument from the far side of the field, but the plan does not change; it explains why the plan stays plain.

---

## 7. Narrow bracketing (Read, Loewenstein and Rabin, 1999; Rabin and Weizsäcker, 2009)

**Verified** the later paper at https://ideas.repec.org/a/aea/aecrev/v99y2009i4p1508-43.html. Quotes: decision makers who narrowly bracket "can end up choosing a first-order stochastically dominated combination";
"28 percent of participants choose dominated combinations" in a real-stakes lab experiment; "89 percent of people bracketing narrowly" in an estimate. (Quotes returned as paraphrase plus short phrases; the Read-Loewenstein-Rabin 1999 original I did not open.)

**What it is.** If you judge each choice on its own, you can pick a combination that is worse than another in every state of the world, because you treated each bet as separate.

**Critique.**
- The experiments are about lotteries, not ten dated cheques. The leap to liabilities is ours.
- Narrow bracketing is not always an error: when liabilities really are separable, it is the right frame. A ladder of ten separately funded payments is a deliberate
  narrow bracket for the *payments* and a broad bracket for the *whole portfolio*.

**Fit to Laura.** Partly, and mainly as a diagnosis of a rival's mistake. The trap is a plan that treats the floor and the stock sleeve as two separate choices, and so ends up
holding stocks while also paying to insure them in the same account: a dominated pair. Our plan avoids it because the stocks are bought only with the money the floor does not need.
The judges' real framing risk is the opposite: seeing individual WInS *trades* (11 of them, with trade notes) when the argument is the whole plan, which Wharton says to judge together. That tells us what the IPS and trade notes should do: name the bracket.

**Fusion hook.** With mental accounting (covered R02 #25) and Samuelson's fallacy (covered R02 #30): "ten brackets for the payments, one bracket for the portfolio" is a precise way to say what mental accounting does and does not do in the plan. Synergy: a **sentence of design**, not a new idea.

**Logic device.** The two-gambles example from the paper family, shown in plain English, to explain why separate decisions can give a worse whole. Use only if it fits the Final Report; I did not reproduce its payoffs.

**Lands in:** Final Report (Investment Concepts, one paragraph, to show the team knew the trap). Not the IPS. Partly decoration.

---

## Seems relevant, isn't (or is thin): bin or one line

**Kreps-Wilson reputation / the chain-store paradox.** Verified at https://pages.ucsd.edu/~bslantchev/courses/pdf/kreps-jet1982v27n2.pdf. Quotes: the intuition "is not supported in a straightforward game-theoretic model"; the fix is "a 'small' amount of imperfect (or incomplete) information about players' payoffs";
and the worked example: "if there are more than ten stages to go the entrant stays out." So reputation needs a **long string of repeated encounters** and a small chance she is the "tough" type. Laura meets co-sponsors a handful of times, once with this range, and her reputation as a writer lives outside the game.
Verdict: seems relevant (her "word"), isn't: the mechanism needs many rounds. What survives is a one-line point: a range she *keeps* is a cheap way to be believed on the next one; that is common sense without the theory. Bin.

**Hold-up (Klein, Crawford, Alchian, 1978) as stand-alone.** Verified through lecture notes https://www.kellogg.northwestern.edu/faculty/hubbard/htm/research/ec174/lectures/13kca.htm: quasi-rents are "payments in excess of the amount necessary to keep an asset in its current use"; "The entire QR is specialized, and therefore potentially appropriable." The Fisher Body/GM story is one episode with a famous critique that I did not open: UNVERIFIED, so do not use the story as a case study.
There is a real use, which I have moved into the fusion paragraph: once co-sponsors have paid for a building, its value depends on the operating money arriving. That is the hold-up logic behind "operating payments before facility", a reason (not a new instrument) for the case's own ordering.

**Peak-end rule.** Verified at https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule. Quote: "people judge an experience largely based on how they felt at its peak (i.e., its most intense point) and at its end". The same page lists "retrospective evaluations of day-long experiences do not appear to follow the peak-end rule" and a "not an outstandingly good predictor" result. The seed asked whether the 2031 announcement or the 2033 gift is what people remember. Honest answer: it is writing craft for the Final Report (end on the strongest beat) and an unproven claim about donors. No change to the plan. Bin as a theory; keep as a layout habit.

**Also dropped without a source opened:** Holmström-Milgrom multitask and the informativeness principle (the Wharton scoring does not count WInS P&L; interesting as a Final Report footnote on why we held, but name-dropping);
Shapley value for splitting the facility (the case has no cost-sharing split to make); folk theorem (needs repetition); Stackelberg *duopoly* (we are not duopolists).

---

## Best synergy from my domain (5 lines)
The plan's three layers are three different strengths of commitment, and game theory says each needs a different backing: the ten payments (certain, bought first, Treasuries held to maturity) are the *safeguard for co-sponsors' sunk building*, the hold-up reason the operating commitment comes before any facility money;
the bottom of the range (owned) is the *leader's commitment*, made believable by the January 2031 lock (Stackelberg's irreversibility, not just safety); the top (conditional, capped, refunded if the facility does not go ahead) is the *assurance* that stops her gift crowding co-sponsors out (Varian's warning, the cure being a match plus a refund, Bagnoli-Lipman).
Fuse with idea 1: the one strongest objection, refuted in the same clause with its price stated (the newsvendor choice, said aloud), is the most persuasive form of the argument by the sidedness meta-analyses. One caution: "three tiers of sure" resembles the Rooftop's withdrawn proposal (BIBLE, 26 Oct), so keep it as an argument in the Final Report, never as a labelled scheme in the IPS.
