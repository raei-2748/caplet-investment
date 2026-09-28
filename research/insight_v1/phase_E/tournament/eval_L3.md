# Eval L3: simulated Laura Gao picks a firm

SIMULATION. This is an AI playing Laura, not Laura. It uses only the case
(`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, cited as "case L<line>"), D13a VERIFIED-PRIMARY
quotes (cited by id) and the D13c voice map. Every "she would..." is an inference. We hold no verified statement by her
about investing (D13c V8). Serves: IPS, because the 2031 range and certainty rules are frozen on Nov 6.
Relayed user message: "just cut off the unnecessary bits". Applied by keeping this file short.

## Ranking

| rank | firm | score /10 | one-line verdict (simulation) |
|---|---|---|---|
| 1 | D | 8.0 | The payments and the 2031 floor are bought before anything is promised, and the costs are stated. Growth is thin. |
| 2 | A | 6.0 | Plain and honest glide path. Payments stay exposed to markets until 2033, and the range is wide. |
| 3 | E | 5.5 | Simple, and it under-promises at the top of the range. The bonds do not match the payments, and payments rely on the 2028 deposit. |
| 4 | B | 4.0 | Takes her risk-taking at face value but puts the risk on the people who will rely on her. Its range is a coin flip. |
| 5 | F | 3.5 | A black box with a range too wide to announce. |
| 6 | C | 3.0 | Themed funds "linked to Laura's public work" turn her work into decoration. |

The same gap appears in all six firms. None states an assumption about inflation or about facility costs in Taiwan,
although the case asks for both (case L146-147). None says what a fixed $50k (case L90) buys by 2042.

## Firm by firm

### 1. Firm D (8.0)
Earns confidence:
- **Payments bought in January 2027**, each by a Treasury zero maturing before its payment date. Certainty is defined
  as "bought", not forecast. Case L91 asks for "a high degree of certainty", and case L97-99 asks teams to define it
  and say how they checked it. D13a-N01: letting down "people who were your earliest supporters" is worse than
  letting yourself down.
- **The 2031 floor ($150k) is already owned when she speaks to co-sponsors.** The contribution rule (section 5) caps
  the gift at the top of the range. Case L114-115: "If Laura promises more than she can ultimately contribute, she
  could damage her credibility".
- **It names its own gaps**:
  - about 1 in 3 rate paths push the ladder above $300k;
  - the unfunded part of the 2033 payment is $12k after a half-point rate fall and $31k after a one-point fall, if the
    2028 deposit is also missing;
  - the price of certainty is a p95 surplus of $250k.

  This matches B8b-Q18 (she names the cost, "unstable income", before she leaps) and B9b-Q09 (she labels her own
  results "[unfinished]").
- **$32k is kept in T-bills after 2033.** Case L102-103: "committing all remaining assets could limit her financial
  flexibility".

Loses confidence:
- **The average stock share is 7.5%**, with only about $40k in one stock fund. Case L69-74 says she "has been willing
  to take thoughtful risks" and wants "an appropriate balance". B1b-Q11: "you should always take the jump". On paper
  this reads as timid unless the firm says where the leap is.
- **The whole 2031 floor depends on the 2028 deposit**, which comes from "publishing advances, speaking engagements,
  licensing" (case L44-45) and from income she herself called "unstable" (B8b-Q18). A missing deposit means no floor
  and no stock fund (D's own risk 3).
- **Spurious precision**: "$294,387" and "7.5%" are stated to the dollar and the tenth of a point. D13c R5 warns
  against numbers more precise than the model behind them.

### 2. Firm A (6.0)
Earns confidence:
- **Easy to follow**: five funds, a published glide path, and Treasuries bought in stages from 2030 (D13c V12: she
  taught financial literacy to high-school students, B2b-Q08).
- **Candid about its range**: "its bottom is less than half its median".
- **Growth is real**: the average stock share is 44%, which answers "thoughtful risks" (case L69-74).

Loses confidence:
- **Payments depend on markets until 2033**: a 0.7% miss rate, 8.6% if the 2028 deposit is $75k and 44% with no
  deposit. Case L91 requires funding "with a high degree of certainty", and the deposit is "unstable" income
  (B8b-Q18). D13a-N01 applies: the downside lands on residents, not on her.
- **The range bottom has a 10% model chance of being missed.** Case L114-115 (overpromising). The bottom is a model
  percentile, not money she owns.
- **"High certainty" rests on a model probability.** She would ask which model (B9b-Q09, D13c R5).

### 3. Firm E (5.5)
Earns confidence:
- **Its range tops out at the median**, so a result above the top is as likely as not. That under-promises
  (case L114-115).
- **Three ETFs**, which makes it the simplest firm.
- **It admits that its bond fund "is not matched to the payment dates."**

Loses confidence:
- **The in-range confidence is only about 40%** (90% reach the bottom, 50% exceed the top). Case L117-118 asks how
  confident the team is that her contribution "will fall within that range".
- **The miss rate is 1.1%, rising to 9.6% at a $75k deposit** (B8b-Q18, D13a-N01, as for A).
- **The broad bond fund holds corporate and mortgage bonds**, which adds credit risk to money meant for a nominal
  promise.

### 4. Firm B (4.0)
Earns confidence:
- **Honest numbers**, including a 40.8% miss rate with no deposit.
- **Plain language and four trades.**
- **It takes her risk-taking seriously** (B1b-Q11).

Loses confidence:
- **It reads the case as "willing to take risks"** and drops "thoughtful" and "appropriate balance ... protecting
  the capital required for her goals" (case L69-74).
- **The miss rate is 3.2% (13.7% at $75k)**, the weakest payment protection of the six. It fails case L91 in spirit
  and puts the jump on the people who rely on her (D13a-N01).
- **The 2031 range has 50% confidence**, so half the time her contribution lands outside the range she announced
  (case L114-118).
- **A 2031-32 stock fall lands just before the reserve is bought.** Case L119-120 says the range must "protect the
  portfolio's ability to fund the ten-year operating commitment".

### 5. Firm F (3.5)
Earns confidence:
- **The best payment protection among the market-risk firms**: a 0.3% miss rate.
- **A defined loss limit.**

Loses confidence:
- **An optimiser with 12 funds, factor tilts and gold, reset every quarter**, which the firm itself calls
  "sensitive to small errors". D13c R4 and R5 warn against this. B8b-Q13 says she scrapped drafts that "lost the
  heart" of her work. Our extension is that complexity is not a virtue.
- **The range runs from $59k to $317k.** A top more than five times the bottom is not "a credible range" (case
  L115-116) that co-sponsors can plan around.
- **Nothing in the case calls for gold or factor tilts.** Hype risk (D13c R12, B8a-Q37).

### 6. Firm C (3.0)
Earns confidence:
- **70% of its stock money is a plain world fund.**
- **It admits that its theme funds are more volatile than its model assumes.**

Loses confidence:
- **30% of the stock money goes to funds "linked to Laura's public work"**: creator economy, Taiwan, clean energy
  and ESG. The case names no values screen. Clean energy does not appear in her public work. D13c R3: identity or
  heritage as a reason for a holding is a strong on-sight rejection.
- **A creator-economy fund doubles her career risk.** The 2028 deposit comes from publishing, speaking and licensing
  (case L44-45), so a creator-economy fund can fall just when that income weakens.
- **The range runs from $65k to $335k, and the miss rate is 1.5% (10.6% at $75k)**, the same weaknesses as A, with
  more model error.

## What Firm D must change before simulated Laura signs
1. **Say where the leap is, and price the growth share.** The residency is the leap. Show one alternative with a
   smaller 2028 floor and more in stocks, give its p5 and p50, and explain why D chose its version. Without that, the
   7.5% stock share reads as timid (case L69-74; B1b-Q11).
2. **Add a rule for a smaller or late 2028 deposit.** Set the order: complete the payments first, buy the floor
   next, then fund the stock fund. The 2031 bottom is whatever the deposit actually bought. Announcing in 2031, after
   the deposit, keeps that honest (B8b-Q18; case L119-120).
3. **Give the in-range confidence directly** (case L117-118). Under D's cap rule the 2033 contribution always falls
   inside the range if the 2028 deposit arrives; the top is reached in about 73% of model paths. Also say how
   meaningful $150k-$175k is next to the cost of a facility (case L111-112), without estimating that cost (case
   L164-165).
4. **State inflation and Taiwan cost assumptions**, and what a fixed $50k buys by 2042 (case L90, L146-147).
5. **Round the numbers and grade each one** as a market price or a model estimate. Drop "$294,387"-style precision
   (D13c R5; B9b-Q09).

## What this teaches
A client may admire risk-taking in her own career and still refuse risk that falls on people who trust her. The best
plan here does not rank first for taking the least risk. It ranks first because it makes a promise only after the
money for that promise is bought.
