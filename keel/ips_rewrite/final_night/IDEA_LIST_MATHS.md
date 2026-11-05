# Idea-list maths and verdicts (R7, final night, Fri 6 Nov 2026)

(Moved here from `IDEA_LIST_VERDICTS.md` at the Chief of Staff's request; that filename belongs to the Writer's own agent.)

The list Caplet pasted into Book 12 (`../../BIBLE.md`, lines ~451-690) is judged here item by item against our plan as
it actually stands: static cash-flow matching (a Treasury holding per payment, held to the end; locked reflections 1-2),
a late-2032 Treasury fund that sets the facility minimum, one world share fund bought with roughly that fund's
interest, and a 2031 range whose top is moved into Treasuries before it is named. The plan is **not CPPI, not
immunisation, not dynamic**, uses only WInS stocks, ETFs and Treasuries (no options, no STRIPS, no TIPS), and changes
only on dates. "Roots / Canopy / Branch / Ballast" labels are banned (Book 2), and so are "floor" and other coined terms (I83).

Verdicts: **IPS** = worth a sentence or clause in the IPS (concept explained plainly, no citation, no number);
**FR** = Final Report only; **REJECT** = wrong for this plan, contradicts the locked record, or inaccurate.
Maths first (sections 1-3, the python in section 3), then the item-by-item verdicts (section 5).

## 1. The most important number on the list, re-run on today's curve

The list's "riskless anchor" (all money in Treasuries, reserve bought in 2033, the rest is the facility contribution)
is computed at 4%. **Its arithmetic is right; its rate is stale.**

| | List (4%) | Recomputed at 4% | On the 4 Nov curve (flat-equivalent 5.07%, from the team's $300,608 ladder cost, FACTS N1) |
|---|---|---|---|
| Pot in 2033 ($300k×(1+y)^6 + $150k×(1+y)^5) | $562.1k | $562,094 | $595,578 |
| Reserve in 2033 (annuity due, 10×$50k) | $421.8k | $421,767 | $404,355 |
| Facility left, all-Treasury | $140.3k | $140,327 | **about $191,000** |

What this means for us. Our plan is the all-Treasury plan except for the world share fund (about $30.9k bought in Jan
2028, FACTS N8). Over five years at 7.0% expected (JPM 2026 basis, FACTS N5) and 16% volatility, that fund's median
value is about $41.0k against $39.6k had it stayed in Treasuries at 5.07%: **a median gain of roughly $1.4k, and about a
54% chance of beating Treasuries at all.** (At 7.5%: median $42.0k, 57%.) The list's broader claim, "risk buys very
little" at today's yields, holds for us too, and it is the honest reason the share fund is small. It is also the
contrarian's best attack ("then why hold shares at all?"). The defensible answer, for the FR: the case asks for growth
and "thoughtful risks"; the share fund costs the bottom of the range nothing; and its upside lifts the top. Do **not**
print the $191k or the 54% in the IPS (no model outputs, Book 11); both belong in the FR's "rejected alternative".

## 2. Recomputed values against the list's claims

| List's claim | List's value | Recomputed | Verdict |
|---|---|---|---|
| Reserve in 2033, 10×$50k annuity due, 2% / 3% / 4% / 5% / 6% | $458.1k / $439.3k / $421.8k / $405.4k / $390.1k | $458.1k / $439.3k / $421.8k / $405.4k / $390.1k | Exact |
| Closed form 50,000×[1+(1−(1+y)^−9)/y] at 4% | $421,767 | $421,767 | Exact |
| Riskless facility at 4% ($300k×1.04^6 + $150k×1.04^5 − reserve) | $140.3k | $140,327 | Exact, but the rate is stale |
| Same on the 4 Nov curve (flat-equivalent 5.07%, from the team's $300,608 ladder cost) | n/a | **≈ $191,223** | The list's headline is $51k too low today |
| A 1pt fall raises the reserve ≈ $17k | $17k | $17.5k (4%→3%) | Right |
| Ladder ≈ $295k at 5.25%, modified duration ≈ 9.6 | $295k / 9.6 | $295,337 / 9.58 ($283/bp) | Right |
| On the 4 Nov curve | n/a | $300,608 / 9.61 / ≈ $289/bp flat (FACTS: $299/bp bootstrapped) → ≈ $29-30k per 100bp | Updated |
| Liability duration from 2027 at 4%: Mac 10.2, mod 9.8, $326/bp | 10.2 / 9.8 / $326 | 10.18 / 9.79 / $326 | Right at 4%; 10.09 / 9.61 today |
| 60/40 bond sleeve (dur 5.5) offsets about a quarter | ≈ 25% | $6.6k vs $28.9k per 100bp → **22%** | Right |
| Hamada surplus beta, 60/40 β 0.6, D/E 2 | 1.8 | 1.80 | Right (if the liability is fully hedged) |
| Equities beat a locked 5y zero (8.5%, 16.5% vol, 5.25%) | ≈ 64% | **61%** | Slightly high |
| Same on our inputs (7.0%, 16%, 5.07%, 5y) | n/a | **≈ 55%** | |
| P(underperform the riskless plan) independent of size (7%, 16%, 4%, 6y) | ≈ 40% | 38.7%; median multiple 1.40, mean 1.50 | Right |
| At-forward put cost 2N(σ√T/2)−1, σ 16%, T 6 | ≈ 15.5% | 15.54% | Right |
| 5y zero at 5.25% | 77.4% | 77.43% | Right |
| 5y ATM call (17% vol, 1.3% yield, 5.25%) | ≈ 23% | 22.93%; zero + call = 100.35% | Right: protected structures are about break-even |
| Arithmetic − geometric gap ≈ σ²/2 at 16% | ≈ 1.3pt | 1.28pt | Right |
| Newsvendor: k = 4 → promise the 20th percentile | 0.20 | 0.20; our modelled top reached 76% → quoted near p24 → k ≈ 3.2 | Right; explains our own "about 3 times" |
| Reserve is 93% of contributions | 93% | 93.7% at 4%, 89.9% today | Arithmetic right, but it mixes 2033 dollars with 2027-28 dollars: don't quote it |
| Our share fund ($30,926 from Jan 2028) vs Treasuries by 2033 | n/a | median $41.0k vs $39.6k (+$1.4k), P(beat) 54% at 7.0%; at 7.5%: $42.0k, 57% | **The key number: risk buys very little at today's yields** |
| CPPI beaten by static 50/50 in 2008 ($168k vs $185k); 60/40 shortfall 5-6%; reverse stress −82% | as stated | not reproducible from the list (its designs, not ours) | UNVERIFIED |

## 3. The python (run 6 Nov, python3, standard library only; lognormal with arithmetic mean and volatility matched)

```python
from math import log, sqrt, exp, erf
N=lambda x:0.5*(1+erf(x/sqrt(2)))
def reserve(y): return sum(50_000/(1+y)**t for t in range(10))
def anchor(y): return 300_000*(1+y)**6+150_000*(1+y)**5-reserve(y)
print("1.1 reserve table (list vs recomputed):")
for y,lst in [(.02,458.1),(.03,439.3),(.04,421.8),(.05,405.4),(.06,390.1)]:
    print(f"  {y:.0%} list {lst}k  calc {reserve(y)/1e3:.1f}k  residual(562k) {562-reserve(y)/1e3:.1f}k")
print(f"  closed form 4%: {50000*(1+(1-1.04**-9)/.04):.0f}")
print(f"1.2 anchor 4%: pot {300000*1.04**6+150000*1.04**5:.0f} reserve {reserve(.04):.0f} anchor {anchor(.04):.0f}")
# flat yield implied by team's 4 Nov cost 300,608 for payments t=6..15 from Jan 2027
pv=lambda y: sum(50000/(1+y)**t for t in range(6,16))
lo,hi=0.01,0.1
for _ in range(100):
    m=(lo+hi)/2
    lo,hi=(m,hi) if pv(m)>300608 else (lo,m)
y=m; print(f"implied flat yield from $300,608: {y:.4%}")
print(f"  anchor at that yield: {anchor(y):.0f}; pot {300000*(1+y)**6+150000*(1+y)**5:.0f}; reserve2033 {reserve(y):.0f}")
mac=sum(t*50000/(1+y)**t for t in range(6,16))/pv(y); md=mac/(1+y)
print(f"  Macaulay {mac:.2f} mod {md:.2f} DV01 ${pv(y)*md/1e4:.0f}/bp, per 100bp ${pv(y)*md/100:.0f}")
for yy in (.04,.0525):
    mac=sum(t*50000/(1+yy)**t for t in range(6,16))/pv(yy)
    print(f"  at {yy:.2%}: cost {pv(yy):.0f} Mac {mac:.2f} mod {mac/(1+yy):.2f} $/bp {pv(yy)*mac/(1+yy)/1e4:.0f}")
print(f"duration offset: 60/40 bond sleeve 5.5 on 40% of 300k: $/100bp {0.4*300000*5.5/100:.0f}")
# Hamada / surplus beta
A=600e3; R=400e3; S=A-R; print(f"surplus beta 60/40 beta0.6: {0.6*A/S:.2f} (D/E={R/S:.1f})")
# put cost
s,T=.16,6; print(f"at-forward put 2N(s*sqrtT/2)-1: {2*N(s*sqrt(T)/2)-1:.4f}")
# 5y zero + call
r=.0525;q=.013;sig=.17;T=5;S0=K=1
z=exp(-r*T)*1; zz=1/(1+r)**5
d1=(log(S0/K)+(r-q+sig**2/2)*T)/(sig*sqrt(T)); d2=d1-sig*sqrt(T)
call=S0*exp(-q*T)*N(d1)-K*exp(-r*T)*N(d2)
print(f"5y zero at 5.25% annual {zz:.4f} (cont {z:.4f}); BS ATM call {call:.4f}; zero+call {zz+call:.4f}")
# prob equities beat locked zero over 5y: arith 8.5%, vol 16.5%, rf 5.25%
for (mu,sg,rf,T) in [(.085,.165,.0525,5),(.07,.16,.04,6),(.07,.16,.05,5)]:
    m=log(1+mu)-0.5*(sg**2)/(1+mu)**2  # approx lognormal annual log-mean
    sl=sqrt(log(1+sg**2/(1+mu)**2))
    m=log(1+mu)-sl**2/2
    p=1-N((T*log(1+rf)-T*m)/(sl*sqrt(T)))
    print(f"  P(equity beats zero) mu{mu} vol{sg} rf{rf} T{T}: {p:.3f}; median multiple {exp(T*m):.3f}, mean {(1+mu)**T:.3f}")
print(f"arith-geo gap sigma^2/2 at 16%: {.16**2/2:.4f}")
# newsvendor: top reached 76% -> quoted at 24th pct -> k
p=0.24; print(f"newsvendor k implied by quoting p24: {(1-p)/p:.2f}; k=4 -> quantile {1/(1+4):.2f}")
# share of contributions
print(f"reserve/contribs nominal 4%: {reserve(.04)/450e3:.1%}; at implied y: {reserve(y)/450e3:.1%}; cost today/300k {300608/300e3:.1%}")
# riskless vs plan: VT ~30.9k bought Jan 2028 replaced by Treasuries for 5y
vt=30926
for mu in (.07,.075):
    sl=sqrt(log(1+.16**2/(1+mu)**2)); m=log(1+mu)-sl**2/2
    print(f"  VT {vt} 5y at {mu}: median {vt*exp(5*m):.0f} mean {vt*(1+mu)**5:.0f}; in Treasuries at {y:.2%}: {vt*(1+y)**5:.0f}; P(VT beats) {1-N((5*log(1+y)-5*m)/(sl*sqrt(5))):.2f}")
```

## 4. The three items worth an IPS sentence

1. **Ability vs willingness to bear risk** (list: "Risk: ability versus willingness … State that ability, not
   willingness, binds"). The case says Laura is "willing to take thoughtful risks"; her portfolio's *ability* to bear
   risk is near zero for any dollar already owed and high for money nobody counts on. One clause turns "too timid"
   into a reason: her appetite is honoured exactly where her ability allows it. This is CFA-standard IPS vocabulary
   (Wharton: "risk considerations", "tailors the strategy to Laura's circumstances"), and it grows from locked
   reflection 3 ("VT is where we allow ourselves to be wrong") (Archive C1). Strongest answer to the contrarian judge.
2. **Pre-commitment (a "Ulysses" rule), and the riskless hurdle behind it** (list: "Ulysses clauses … default is
   stay the course"; "Hurdle rate (Damodaran): … the Treasury … yield. Risk assets must justify themselves against it").
   Our plan already behaves this way: every rule binds in advance and fires on a date, never on a price. Stated as
   reasoning ("the plan decides now what it will do in 2028, 2031 and 2033, so a crash or a boom can't talk Laura out
   of it"), it answers Wharton's own line that a strategy "should not be rewritten simply because markets move".
   The hurdle half is already the IPS's centre ("one honest cost: the price of Treasuries"), so it needs no new words.
3. **A named figure behaves like a dividend (Lintner)** (list: "a pledge cut is punished the way a dividend cut is
   (Lintner)"). Companies set dividends they can keep paying and raise them slowly, because markets punish a cut far
   more than they reward a rise. That is the reasoning behind buying the top of Laura's range before she says it, and
   it is the creative link Ray asked for (I84/I86): an idea from corporate finance, not a picture. The IPS can say it
   in one plain sentence without the name; the FR cites Lintner (1956) and the evidence on dividend cuts.

Runners-up for the IPS if a sentence frees up: the **Bodie point** (time makes a loss rarer, not smaller), which
is already in V57/R-drafts and should stay; and **"the contribution is the part of the residency's money that doesn't
shrink"** (a diversification argument at the level of the residency; shortlist idea 3, not on this list).

## 5. Item-by-item verdicts

| # | Item (list's words, shortened) | Verdict | Why, for this case | Maths / accuracy |
|---|---|---|---|---|
| 1 | Leverage, Modigliani-Miller / Hamada: surplus beta = asset beta × (1 + D/E); a 60/40 makes the facility money β≈1.8 | **FR** | A brilliant way to show why a "moderate" 60/40 is aggressive for the facility money, so it belongs in the FR's rejected-alternatives section. It does not describe our plan: the reserve is cash-flow matched, so the facility's beta is just the share fund's weight in it | Correct: 0.6 × 600/200 = **1.80** with D/E = 2.0, if the liability is riskless and fully hedged. Strictly it is asset β × A/S, which equals β(1+D/E) |
| 2 | Merton structural model; distance-to-default ≥ 2.33 as the definition of "high degree of certainty" | **REJECT** (IPS), FR footnote at most | Our certainty is structural (no payment depends on a share price), not statistical. Against a matched ladder the surplus volatility tied to the payments is near zero, so DD is huge and tells a judge nothing. A probability target also brings model output into the IPS (Book 11) | Formula correct; 2.33 is the one-tailed 99% z |
| 3 | Duration: ladder ≈ $295k at 5.25%, modified duration ≈ 9.6, ≈ $28k per 100bp; a 60/40 bond sleeve (dur 5.5) offsets about a quarter | **FR** | Strong FR exhibit for why "safe bonds" are not a hedge: only a matched ladder moves with the payments. Not IPS (numbers). Never call our ladder "immunised" | At 5.25%: cost **$295,337**, Mac 10.08, mod **9.58**, $283/bp ✓. On the 4 Nov curve: $300,608, mod 9.61, DV01 ~$289 (FACTS says $299 on the bootstrapped curve) → **≈ $29-30k per 100bp**. 60/40 on $300k: 0.4×$300k×5.5 = $6.6k per 100bp, about **22%** of the liability's move ✓ ("a quarter", roughly) |
| 4 | Roy's safety-first / Sharpe-Tint: minimise shortfall on the senior claim first, then optimise the junior one | **FR** (the idea is already in the IPS's order of operations) | Our sequencing (payments bought first, facility from what's left) *is* lexicographic safety-first. Naming Roy belongs in the FR | n/a |
| 5 | Damodaran's implied ERP 4.23% (start of Aug), expected equity return ≈ 9%, ≈ 9.5% at a 5.25% 10-year | **FR, after verification** | Useful as a second capital-market assumption beside JPM. The figure is **UNVERIFIED** here; the Damodaran reader (R4) should confirm the latest monthly value. Ahaan (Book 9): don't lean on a single forecaster's number | Arithmetic is just ERP + 10y yield; no check possible without the source |
| 6 | Thin equity premium: shares beat a locked Treasury zero over 5 years only ≈ 64% of the time; Bodie's time-diversification critique beats "stocks for the long run" (present Siegel too) | **IPS (Bodie, already in) + FR (the number)** | The Bodie point is already the IPS's best erudite line ("time makes a loss rarer, not smaller"); keep it. The probability goes to the FR | Re-run (lognormal, 8.5% arithmetic, 16.5% vol, 5.25% zero, 5y): **61%**, not 64%. Today's case (7.0%, 16%, 5.07%): **55%** |
| 7 | CPPI governor (Black-Jones), floor 90%, multiplier 3, equity cap 60-80%, annual rebalance | **REJECT** | Contradicts the locked record (reflections 1-2: hold, ignore price noise; Archive C4) and the FINAL, which rejects portfolio insurance by name. CPPI sells after falls: path-dependent, and exposed to "cash-lock". The list itself admits CPPI lost to a static 50/50 in its own 2008 case | Claim (CPPI $168k vs static $185k in a 2008 path) not reproducible from the list; treat as UNVERIFIED |
| 8 | Average equity weight ≈ 30-37% of the facility money, ≈ 11% of capital | **REJECT** | Belongs to the CPPI design above. Our share weight is about 8.6% of the WInS book (FACTS) and falls further at the 2031 lock | n/a |
| 9 | "The floor turns the pledge into a risk budget automatically" | **REJECT** (wording) / idea already in | "Floor" is banned (I83). The idea (the minimum contribution bought in Treasuries limits what the shares can cost) is already the plan | n/a |
| 10 | Hurdle rate (Damodaran): the Treasury yield; risk assets must beat it | **IPS (already central)** | This is our pricing rule ("one honest cost") in Damodaran's words. No new sentence needed; cite Damodaran in the FR | See section 1: at today's yields the hurdle is high (≈5.1%) and the shares clear it by little |
| 11 | 2033 waterfall: C = min(0.9S, max(pledge, 0.75S)), rounded down to $5k; retained 25% is a real option | **REJECT** (formula) / **FR** (real-option framing) | Our rule is different and stricter: the range's two ends are bought before it is named, and the kept half of the shares is promised to no one. A formula paying out of the 2033 surplus contradicts the locked VT note ("only set how far her gift rises above her promised minimum") if read as funding promises from shares. The "real option to expand, delay or abandon" framing of the kept half is good FR material | Formula is internally consistent |
| 12 | Damodaran's dividend framework / Lintner: a pledge cut is punished like a dividend cut; Swensen spending rules | **IPS (one sentence, no name)** + FR | See section 4 item 3. It explains *why* we buy the top before naming it, which is the plan's most original move | n/a |
| 13 | Newsvendor logic: if over-promising costs k× under-promising, promise the 1/(1+k) quantile; k=4 → 20th percentile | **FR** | Excellent FR argument, and it explains a number we already have: our modelled top is reached about 76% of the time (FACTS N5), i.e. quoted near the 24th percentile, which implies **k ≈ 3.2**. Book 9 praised exactly this ("over-promising as roughly 3 times worse"); Book 10 warns it must say "we modelled", never "we judge". Not in the IPS (model number) | 1/(1+4) = 0.20 ✓; (1−0.24)/0.24 = 3.17 |
| 14 | Premium check with honest statistics: 8-week window sd ≈ 6.5% vs premium ≈ 0.6%; judge process not outcomes | **FR** (experience section) | Fits Wharton's "do not focus on portfolio performance"; good for "Articulation of Competition Experience" | 16.5%×√(8/52) ≈ 6.5% ✓; 4.23%×8/52 ≈ 0.65% ✓ |
| 15 | Diversification audit (Shiller lecture 4, Markowitz): marginal risk contribution; Taiwan-stress screen (Taiwan ETF, USD/TWD) | **FR** | The Taiwan screen is a nice client-specific touch (the facility is in Taiwan). R5 should confirm the Shiller lecture number | n/a |
| 16 | Options as priced insurance: 5-year zero ≈ 77.4%, 5-year ATM call ≈ 23%, so "protected full participation" ≈ break-even | **FR** (as the reason we own shares rather than a bank's protected note) | Options are banned for modelling (WHARTON_WORD §5), so only as a benchmark. It is the maths behind V57's "capital-protected note" line | Re-run: zero at 5.25% annual = **0.7743** ✓; Black-Scholes ATM call (17% vol, 1.3% yield, 5.25%, 5y) = **0.2293** ✓; sum 1.0035, i.e. break-even ✓ |
| 17 | Mission line "Protect the commitment first; let the upside serve the dream" | **REJECT** | A slogan (voice guide §9; Ray I84: packaging) | n/a |
| 18 | Dual mandate, separate benchmarks (funded ratio ≥ 100%; riskless 2033 value + premium) | **FR** | Good evaluation frame for the implementation review | n/a |
| 19 | Risk metrics: surplus-at-risk and distance-to-default, not volatility | **FR** (surplus-at-risk only) | See item 2 for DD | n/a |
| 20 | Hedge ratio 100% of rate sensitivity (±2%), rechecked at each contribution | **REJECT** (as written) | We match cash flows, which is stronger than a duration hedge and needs no rechecking. "Rechecked" implies rebalancing (Archive C4). FR can contrast the two | n/a |
| 21 | Decision rights: investment committee, quorum, limit on discretionary trades | **REJECT** | Laura decides alone; the IPS is a strategy, not a governance charter. The useful part (rules bind in advance) is item 22 | n/a |
| 22 | Behavioural guardrails: Ulysses clauses, Nudge-style default "stay the course", 48-hour cooling-off, mandatory pre-mortem | **IPS (the pre-commitment idea)** + FR (the rest) | See section 4 item 2. The 48-hour clause and pre-mortem are governance trivia for the IPS; FR at most | n/a |
| 23 | Eligible instruments: no leverage, no shorting, no sold options, issuer limits | **REJECT** (IPS) | True of us by Wharton's rules, so it adds nothing and spends words | n/a |
| 24 | If-then trigger table (yields ±100bp, 20% drawdown, ERP > 5.5%, downgrade, …) | **REJECT** | Market triggers contradict the plan's core rule (dates, never market moves) and the locked "ignore price noise". Only date-based rules survive | n/a |
| 25 | Review and amendment, version log tied to trading notes | **FR** | Implementation-review material | n/a |
| 26 | Three-number dashboard for Laura (funded ratio, surplus, pledge confidence), traffic lights | **FR** | Nice exhibit; the FR's co-sponsor section could reuse it | n/a |
| 27 | Assumption register (owner, source, update trigger) | **FR** | Satisfies Commandment V for the FR | n/a |
| 28 | FR structure: executive summary with the three answers first; client as a balance sheet; design logic and rejected alternatives; WInS as attribution kept apart from projections; certainty tests; waterfall; co-sponsor text; favourable/unfavourable cases, reverse stress, tornado; inflation and FX; what would change our mind; appendix | **FR** (structure) | Mostly sound and matches Wharton's FR brief. Two fixes: "waterfall" → our "bought before named" rule; "inflation tables" are a non-issue for nominal payments (locked reflection 1: TIPS "would hedge against a nonexistent inflation risk"), so one line explains why, no table | n/a |
| 29 | Exhibits: balance-sheet reframe, reserve cost vs yield (5.09% break-even), duration 10→0, funded-ratio fan, surplus histogram, scenario table, tornado, cone narrowing, range ladder, waterfall | **FR** | All usable. Update the break-even: on 4 Nov the ladder costs $300,608, i.e. **already $608 over** $300k (FACTS N1), so "break-even at 5.09%" is stale; the flat-equivalent yield is 5.07% | see FACTS N1 |
| 30 | One-page plain-English "Letter to Laura" | **FR** | The case already requires draft co-sponsor text; a letter is optional. Book 3: judges are not mini-Lauras, so keep it short | n/a |
| 31 | Purpose & client profile; quote her "responsible" balance | **FR** | Book 12: no IPS paragraph spent retelling the case | n/a |
| 32 | Objectives: return objective + risk objective | **REJECT** (IPS) | Template structure; no subheadings (Book 11). The IPS states them inside the argument | n/a |
| 33 | Time horizon is multi-stage (accumulation, pivot, distribution): "yours needs three" | **IPS (already implicit)** | True and answers Wharton's "changing time horizons". Our plan's three dates (2027, 2028, 2031) are the stages; no new sentence needed beyond the date-by-date structure | Note: the list's "6-year accumulation" is 2027-2033 ✓ |
| 34 | Liquidity: near-zero 2027-32, annual 2033-42, lump sum 2033 | **FR** | Correct reading of the case. In the IPS, liquidity is answered by the funds' daily tradability (Archive C6) and the kept half of the shares | n/a |
| 35 | Risk tolerance & allocation ranges, glide path, rebalancing bands | **REJECT** | Static plan; no glide-path bands (Archive C4) | n/a |
| 36 | Two-sleeve structure at 2033: reserve "immunized" + facility/flexibility | **REJECT** (word) / idea already in | Ours is cash-flow matched, not immunised (BIBLE :419). The two parts exist already | n/a |
| 37 | Assumptions log: note the fixed-nominal-payment insight | **IPS (already in, keep)** | "Inflation can make $50,000 buy less; it cannot make $50,000 cost more" is one of the voice guide's beliefs and locked reflection 1 | n/a |
| 38 | Reserve evolves: duration shortens each year as the ladder is drawn | **IPS (already in R4's last paragraph)** | Answers Wharton's "how will the composition change as payments are made" | n/a |
| 39 | Facility contribution: amount, methodology, bear/base/bull | **FR** | Wharton: no final range in the IPS | n/a |
| 40 | Draft fundraising excerpt | **FR** | Required there, not in the IPS | n/a |
| 41 | True bear case: contribution can go to zero while the reserve stays protected, "state this plainly" | **REJECT as stated** | Under our plan the contribution doesn't go to zero: the minimum is bought in Treasuries in 2028; only the top above it depends on shares, and a yield fall can lower the range (C9). Saying "zero" would understate our own design | n/a |
| 42 | Why hold back a buffer rather than commit 100% | **IPS (already in: "the other half … promised to no one")** | Answers "preserving appropriate financial flexibility" | n/a |
| 43 | Chhabra's three risk buckets (personal / market / aspirational) | **FR** | Maps cleanly (payments / bought range / kept shares) and is citable pedigree. The bucket idea itself is common, so it is not our creativity; the FR should say how we differ (our buckets are filled on dates and bought before promised) | n/a |
| 44 | Core maths 1.1: reserve cost table, "1pt fall raises reserve cost ≈ $17k (4%)" | **FR** | Table verified exactly (2%: $458.1k … 6%: $390.1k). 4%→3%: +$17.5k ✓. Note: our ladder is bought now, so this rate risk is already removed; the table shows what we avoided | ✓ |
| 45 | 1.2 Null hypothesis, the riskless plan ≈ $140k "and most teams will never compute it" | **FR** (re-run) | See section 1: on today's curve it is **≈ $191k**. "Most teams will never …" is banned (Book 10) | ✓ at 4%; stale rate |
| 46 | 1.3 Master equation: facility = riskless + G₀(M − 1.265); sizing table A-D; "≈40% chance of underperforming at any size"; insuring costs ≈15% of the sleeve; gap risk 1/m | **FR** (equation, the "size changes regret, not its likelihood" insight) / **REJECT** (gap-risk part: CPPI) | The equation is exactly our design's logic and the cleanest FR exhibit for "why the share fund is small". The 40% claim is right: P(M < riskless) doesn't depend on G₀ | 1−0.613 = **38.7%** at 7%/16%/4%/6y ✓; median 1.40, mean 1.50 ✓ (list: 1.39 / 1.50); put 2N(0.16·√6/2)−1 = **0.1554** ✓. The A-D table assumes a 4% "locked floor" and static hold: re-run on today's curve before use |
| 47 | 1.4 Sharpe-Tint surplus at 2027 with λ = 0.75 haircut on the 2028 deposit; m = 2 gives the 50% start | **FR** (haircut idea) / **REJECT** (the 50% start) | The haircut on a "risky receivable" is a sharp way to say why the 2028 deposit shouldn't be counted on for promises, which agrees with the plan. But the case never links her income to markets (Archive C5: "can" is the limit). The 50% equity start contradicts our holdings | Arithmetic ✓ at 4% |
| 48 | 1.5 Liability duration from 2027: Mac ≈ 10.2, mod ≈ 9.8, ≈ $326/bp | **FR** | ✓ at 4% (10.18 / 9.79 / $326). On today's curve: 10.09 / 9.61 / ≈ $289-299/bp | ✓ stale rate |
| 49 | Lineage: contingent immunisation (Leibowitz-Weinberger) | **FR (as contrast)** | Not our design (it switches on a trigger); good "what we considered" | n/a |
| 50 | Lineage: CPPI with ratchet (TIPP) | **REJECT** | As item 7 | n/a |
| 51 | Lineage: Redington immunisation (match PV, duration, convexity) | **FR (as contrast)** | We go a step further than Redington: cash-flow matching needs no rebalancing. Note that locked reflection 1 says "duration-matching" (Archive A34), so the FR should explain the word | n/a |
| 52 | Lineage: safety-first (Roy) | **FR** | As item 4 | n/a |
| 53 | Lineage: goals-based / behavioural portfolio theory (Shefrin-Statman; Das-Markowitz-Scheid-Statman; Chhabra) | **FR** | Citable pedigree for "different goals, different risk" | n/a |
| 54 | Lineage: lifecycle investing with human capital (Bodie-Merton-Samuelson): bond-like future contribution allows more equity early | **FR, with the sign reversed** | Applied honestly, Laura's 2028 income is equity-like, not bond-like (sources the case lists), which argues for *less* equity, our position. The case doesn't state the link (Archive C5), so use "can" | n/a |
| 55 | Barbell vs ladder (convexity), converge to an exact ladder by 2031 | **REJECT** | We already hold the exact ladder; a barbell would mean trading it (contradicts the locked hold) | n/a |
| 56 | CFA-style IPS structure, Ulysses clause, supermajority, 48-hour cooling-off | **REJECT** (structure) / see item 22 | Wharton wants one cohesive argument, no subheadings (Book 11) | n/a |
| 57 | Goal ledger: Goal 1 ≥ 99.9% certainty; Goal 2 range with one-sided confidence; Goal 3 minimum liquidity; Goal 4 never communicate an unhedged amount | **IPS (Goal 4 only, already in)** | Goal 4 is exactly "both ends bought before anyone hears it". Goal 1's percentage is a model output (Book 11) | n/a |
| 58 | Risk: ability vs willingness; avoid overweighting media/publishing/consumer-discretionary stocks given her income | **IPS (ability vs willingness)** / **FR (sector point)** | See section 4 item 1. The sector point is clever and client-specific; VT already holds about 10,000 stocks, so it needs only an FR line | "Reserve is 93% of contributions": **93.7%** at 4% (2033 reserve ÷ $450k nominal), 89.9% on today's curve; mixes 2033 dollars with 2027-28 dollars, so don't quote it |
| 59 | Constraints: multi-stage horizon, no withdrawals before 2033, taxes out of scope, TWD exposure, single-person governance | **FR** | TWD: the payments are fixed US dollars; FX touches only the building's cost (a reason to keep the unpromised half liquid). FR line | n/a |
| 60 | CMAs in three sets (base / low / stagflation); arithmetic for expectations, geometric for projections (gap ≈ σ²/2 ≈ 1.3pt) | **FR** | Good method. Our model uses JPM 2026 7.0%; TNA reflection 3 uses 7.5% (FACTS N5): the FR must reconcile | σ²/2 at 16% = **1.28pt** ✓ |
| 61 | SAA table, glide path and trigger table | **REJECT** | Static plan | n/a |
| 62 | Liability-relative benchmark | **FR** | As item 18 | n/a |
| 63 | Rebalancing: band-based, use contributions to rebalance (the 2028 check) | **REJECT** (bands) / **IPS already** (using the 2028 deposit first to complete the ladder, Archive C9) | n/a | n/a |
| 64 | Reserve Establishment / Facility Release protocols | **FR** | Our dates already are the protocol | n/a |
| 65 | Monitoring dashboard: funded ratio, cushion, m, DV01, surplus VaR/CVaR, tracking error, P(goal), liquidity | **FR (subset)** | Drop "m" (CPPI). DV01 and funded ratio are useful | n/a |
| 66 | Exhibits: tranche waterfall, reserve cost vs yield & benefit of pre-locking, surplus distribution with the riskless line, fan chart, tornado, stress tests (1973-74, 2000-02, 2008, 2022, lost decade), reverse stress (≈ −82% growth-sleeve loss) | **FR** | "Benefit of pre-locking" is our best exhibit: the ladder cost moved from about $294k (mid-Oct) to $300,608 (4 Nov, FACTS N1), which is exactly the risk buying early removed. The −82% reverse stress belongs to the list's 50%-equity design, not ours; recompute | Reverse-stress figure not checkable for our design |
| 67 | Co-sponsor confidence ladder (committed / planning / stretch) | **FR** | Fits our range: bottom bought (committed), top bought on naming day, kept half (never promised). Avoid "stretch" if it implies a promise | n/a |
| 68 | Implementation review: WInS v shadow portfolios, calibration | **FR** | Never add WInS P&L to projections (Wharton) | n/a |
| 69 | "What would change our mind" + model-risk humility | **FR** | Voice guide F6: doubt the forecast once, state the plan flat | n/a |
| 70 | Decision tree 2031-2033 with the rule at each node | **FR** | Our three dates map onto it | n/a |
| 71 | Stochastic yields (Nelson-Siegel / two-factor) | **FR (method note)** | The named weakness (reinvestment if rates fall and stay low) is the only rate risk left; the FR should model it | n/a |
| 72 | Cite Chhabra, Das et al., Shefrin-Statman, Merton on defeasing essential goals | **FR** | Merton's "defease essential goals with safe assets" is the closest published statement of our core rule: cite it first | n/a |
| 73 | Strategy spectrum A (all Treasuries) / B (surplus-only equity) / C (dynamic CPPI) / D (static 60/40); recommend C | **FR (the spectrum)** / **REJECT (recommending C)** | Our plan is close to B with the minimum bought: say so. The A-vs-ours comparison is the honest heart of §1. D failing our own certainty test is a strong exhibit | D's "5-6% shortfall" is the list's own back-of-envelope, UNVERIFIED |
| 74 | Brier-score our forecasts (Tetlock) | **FR** (experience) | Only if we have stated probabilities to score; TNA reflection 2's 0.3pp note is one candidate | n/a |
| 75 | Process vs outcome (Duke's "resulting"), 2×2 | **FR** (experience) | Matches Wharton's "do not focus on portfolio performance" | n/a |
| 76 | Liability-relative performance; "Reserve Cost Ticker" beside P&L | **FR** | See item 66: the ticker shows why we bought on 6-8 Oct | n/a |
| 77 | Purpose & governance; client translation; "Trap Register"; one-page Decision Card | **FR** | The Decision Card idea suits the FR's first page | n/a |
| 78 | Definition of "high degree of certainty" with four tests (structural, probabilistic ≥ 99%, stress, reverse stress) | **IPS (structural test only, already in)** + **FR (the other three)** | The IPS's "no operating payment depends on a share price" is the structural test. The case asks teams to *explain* certainty; the probabilities are model output and go in the FR (FACTS N6: 100% base, 98.71% in a bad world, so never "guaranteed") | n/a |
| 79 | Liability spec "to be met with probability ≥ 99%" | **REJECT** (IPS) | As item 78 | n/a |
| 80 | Funded-ratio traffic light; yield-triggered ratchet; no rebalancing up in Red/Orange | **REJECT** | Market triggers (item 24) | n/a |
| 81 | Contribution-shortfall contingency: if the 2028 deposit is smaller, the reserve first, the facility absorbs it | **IPS (already implied)** | Same rule as the IBTR note (Archive C9). The case fixes the deposit at $150k, so no new sentence | n/a |
| 82 | Instrument selection criteria (cost, liquidity, size, tracking, counterparty) | **FR** | Locked reflection 2 already argues the iBonds this way | n/a |
| 83 | Eight stress scenarios (2008, 2020, 2022, 1970s, Japan, dot-com, contribution shock, combined) | **FR** | "Japan-style decade of near-zero yields" is our one named weakness: run it first | n/a |
| 84 | Simulation blueprint: block bootstrap from 1926, regime-switching correlation, two-factor curve, 10,000 paths, rolling windows | **FR** (method) | Our lab already runs 200,000 paths (FACTS N5); the FR should state the method once | n/a |
| 85 | Minimal python: reserve(0.04) ≈ 421,767; riskless_anchor(0.04) ≈ 140,327 | **FR** | Verified exactly: **421,767** and **140,327** | ✓ |
| 86 | Average several published CMAs (Vanguard, JPM, BlackRock, Research Affiliates), show the dispersion | **FR** | Answers Ahaan's Book 9 point about not leaning on one JPM figure | n/a |
| 87 | Research library (Redington 1952; Fisher-Weil 1971; Sharpe-Tint 1990; Black-Perold 1992; Chhabra 2005; Das et al. 2010; Bodie-Merton-Samuelson 1992; Campbell-Viceira; Merton; Tetlock; Duke); data (FRED, Treasury, Shiller, Damodaran, Fama-French) | **FR** (bibliography) | Drop Black-Perold except as the rejected alternative. Add Lintner (1956) and Roy (1952) | n/a |

## 6. Stale or wrong on the list (so the Writer doesn't inherit them)
- Every dollar figure assumes **4%**. On the 4 Nov curve the flat-equivalent yield is **5.07%**: the riskless facility
  is about **$191k**, not $140k, and the ladder already costs **$608 more than $300k** (FACTS N1).
- "Equities beat a locked zero ≈ 64%": re-run gives **61%** on the list's own inputs, **≈ 55%** on ours.
- "Reserve is 93% of contributions" mixes 2033 dollars with 2027-28 dollars; don't quote it.
- CPPI, glide paths, trigger tables, barbells, hedge-ratio rechecks and the 50% equity start all contradict the
  locked record (Archive C4) and the FINAL's rejection of portfolio insurance.
- "Floor", "Roots / Canopy / Branch / Ballast", "immunized" and "most teams will never compute it" are banned words or
  claims (I83, Book 2, BIBLE :419, Book 10).
- "Facility contribution goes to zero in a bear case" understates our design: the minimum is bought in 2028.
