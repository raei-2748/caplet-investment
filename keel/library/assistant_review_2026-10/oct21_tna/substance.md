# TNA substance teardown: the three current reflections, one sentence at a time

Wed 21 Oct 2026 (work done 07:35-08:10 UTC = 18:35-19:10 Sydney). Input: section A of
`SP/oct21/tna/current_draft_21Oct.md` (lines 7-20). No replacement wording anywhere: each item says what is wrong
and what a fix has to achieve. Students write any fix.

**Short names.** SP = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad`.
DRAFT = `SP/oct21/tna/current_draft_21Oct.md`. CASE = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.
TNA = `.../2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt`. GUIDE = `.../2026_27/2026_WGY_Investment_Competition_Guide.txt`.
REG = `SP/oct20/numreg/numbers_register.md`. V4 = `SP/oct20/engine_v3b/vote_table_v4.md`. KIT = `SP/oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md`.
IPS = `SP/oct19/drive/ips_report_live.md` (V5, lines 23-30). RUB = `SP/oct20/rubric/rubric_scoring.md`.
Web copies fetched today with cache-busting, in `SP/oct21/tna/substance/web/`:
- ISH-M = iShares IBTM page, https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (fetched 21 Oct 07:41 UTC; text `ibtm_2026-10-21.txt`)
- ISH-R = iShares IBTR page, https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf (same time; `ibtr_2026-10-21.txt`)
- VGD = Vanguard VT fact sheet, https://fund-docs.vanguard.com/F3141.pdf, data as of 30 Jun 2026 (`vt_factsheet.txt`)
- SA = https://stockanalysis.com/etf/vt/holdings/ (20 Oct close; `vt_sa_hold.txt`)
- TSY = treasury.gov daily par curve CSV for Oct 2026, now including **20 Oct** (`tsy_202610.csv`)
- LAD = my re-run of the team's own `SP/oct20/numreg/scripts/refresh_oct20.py` on the 20 Oct curve (`SP/oct21/tna/substance/data/ladder_cost_by_basis.csv`, `refresh_stdout.txt`). MODEL.

---

## 0. Verdict

The three reflections describe the plan; they do not yet show decisions being **made, tested and changed**, which is
what the TNA asks for (TNA:11-13, 28-31). Three sentences state false or self-contradicting finance (IBTM S4, VT S4,
IBTR S1). The strongest evidence the team owns, a pre-set numeric test in the IBTR note and a real move from about 75%
stocks to under 10%, appears nowhere. Liquidity, one of the six purpose words, is never covered. The set reads as
three parallel descriptions, not one sequence. The 2028 deposit is the hinge of the whole strategy, and no reflection
names it as one.

---

## 1. Finance accuracy, sentence by sentence

Verdicts: TRUE / MISLEADING / FALSE / INCOMPLETE (true, but the reason given is not the reason that does the work).

### 1.1 IBTM (DRAFT:10; 94 words)

| S | Claim | Verdict | Evidence | What a fix must achieve |
|---|---|---|---|---|
| S1 | Zero-coupon Treasuries dropped because of the "week 2 email" limiting Laura's portfolio to WInS securities | TRUE on the rule, MISLEADING on cause | The public FAQ now lists STRIPS as not permitted "for BOTH contributions, the IPS and Final Report" (`smapply_public_2026-10-20/faqs.txt`, via CLAUDE.md status). IBTM was already the WInS stand-in on 29 Sep (`SP/oct19/drive/sheets/wins_notes.md:25`). So the email changed **Laura's real plan**, not the WInS trade | Say what the switch **cost** in finance terms. A STRIPS pays a fixed amount on a fixed date. A term fund pays out a not-fixed amount around 15 Dec, pays its coupons out monthly (those have to be reinvested), and charges 0.07%. That loss is the whole "refined" story, and S4 then denies it. A judge cannot place "week 2"; give the date |
| S2 | WInS lists no individual Treasury maturing in 2032 | TRUE (team record) | "none mature between 15 Feb 2031 and 15 Feb 2036" (`wins_notes.md:25`; KIT:458) | This is the decisive reason for using a fund at all, so it should carry the weight rather than read as an aside ("also"). Re-check the WInS drop-down on submission day |
| S3 | IBTM "therefore became the best alternative" for payment 1 | MISLEADING | No comparison is on record. The real alternatives were the 15 Feb 2031 bond (cash about 23 months early, then reinvested) or a later bond sold early (price risk) | Drop "best", or name the comparison actually made and the trade-off that decided it |
| S4 | IBTM "is cheap, easy to trade, has a clear yield, and matures on a set date" | **Two of four are FALSE**; one is the wrong virtue | Cheap: TRUE, 0.07% (ISH-M:183-184), but that is 0.07% more than a direct bond, so the claim needs a comparison. Easy to trade: TRUE (30-day median spread 0.05%, 30-day average volume 300,754 shares, ISH-M:248-265). But the plan never trades it: it is held to the end. The liquidity that matters is cash arriving before 1 Jan 2033. "Clear yield": FALSE. iShares shows 30-day SEC 4.99%, 12-month trailing 4.06% and average YTM 4.99% (ISH-M:274-302), and "realized yield to fund maturity will be influenced by the yield earned on these proceeds during the final year" (ISH-M:636). "Matures on a set date": FALSE. The fund "will terminate on or about ... December 15", and its "liquidation proceeds are not predictable ... do not seek to return any predetermined amount" (ISH-M:805-806). Its 15 bonds mature through 2032; the weighted average maturity is 5.70 years at 19 Oct 2026, about mid-2032 (ISH-M:268-306). After that the proceeds sit in cash | Remove every claim that the payout or yield is known. It contradicts the team's own filed note ("the final payout is not fixed", DRAFT:8) and the IPS ("rounded down because a fund's payout is not fixed", IPS:29). Replace "easy to trade" with the liquidity that matters (cash in hand about 17 days before payment 1) or cut it |
| S5 | The 2028 deposit buys a second batch of IBTM to ground a minimum, "so a stock crash will not make her promise fail" | Mechanism TRUE; conclusion MISLEADING | Plan: the 2028 deposit **first** completes the ladder if needed, then buys the floor (IPS:27). So the floor is whatever is left after any top-up. A half-point yield fall before Jan 2027 cuts it to about $137-138k from about $150k (REG E2, MODEL, 19 Oct). No stocks sit in the floor, so the narrow claim holds. But (a) the accepted IPS run uses the floor "last" for payment shortfalls (IPS:25), and a crash empties Laura's VT half, the first backstop, so the floor can be reached. (b) "promise" is the case's warning word: "If Laura promises more than she can ultimately contribute, she could damage her credibility" (CASE:114); "Rather than promising one exact amount, she wants to communicate a credible range" (CASE:115-116) | Name what can still move the minimum: yields before the Jan 2027 purchase (through the top-up), and the fund's payout. Name how the plan allows for it (rounded down; IPS:29). No promise or never-fails language. The VT note's "promised minimum" (DRAFT:13) cannot be edited, so a reflection could own that word as something the team has since refined |

Missed mechanism (high value): the top-up and the floor are **the same fund bought from the same deposit**. Laura's
2027 purchase runs 2042 backwards, so any rung left unbought is payment 1 = IBTM. In Jan 2028 the deposit buys IBTM
for whatever payment 1 still lacks, and the rest of its IBTM is the floor. A yield fall simply moves IBTM shares from
the floor column to the payment column. WInS shows this split: 1,142 payment and 3,361 floor shares (REG H6). This one
mechanism joins IBTM's two jobs to IBTR's "facility contribution is lower". It also removes the contradiction over
who absorbs a top-up (factcheck §5 item 5).

### 1.2 VT (DRAFT:15; 99 words)

| S | Claim | Verdict | Evidence | What a fix must achieve |
|---|---|---|---|---|
| S1 | VT "diversifies the portfolio across countries and sectors without costly (and risky) stock picking" | TRUE for the stock part, INCOMPLETE | 10,048 stocks (VGD:79, 30 Jun 2026); 10,242 on 20 Oct (SA:62). But it is cap-weighted: US 61.9%, technology 33.3%, top ten 21.7% (VGD:109-147). It removes single-company risk, not market risk (3-year SD 12.4%, VGD:86; JPM vol 16.78%). "The portfolio" is about 90% Treasuries (REG H3), so VT diversifies only the stock slice. Repeats the note's "one cheap fund diversifies" (DRAFT:13) | Say what diversification does and does not remove, or cut the repeat of the note. If the team actually settled Darren's 5 Oct challenge (picked stocks, EWT Taiwan, GLD; KIT:344, outcome not recorded), that decision is far stronger content than restating the fund's features |
| S2 | Equity kept small "(9% of the portfolio), since we prioritise certainty for Laura's payments" | "9%" MISLEADING; reason INCOMPLETE | 9% is the WInS share (8.84% at cost, 8.65% of the 19 Oct book). In Laura's plan stocks are about 7% of her money (REG H4). The size is not chosen: it is the **remainder** after the payments and then the floor (IPS:27). The payments come from the 2027 deposit whatever size VT is, so what limits VT is the floor, i.e. the credible minimum | Name the portfolio the % refers to and give the real sizing rule (payments, then floor, then stocks). Strongest missing content: the team's **original plan was about 75% stocks**, and modelling showed it missed payments (about 3% of paths, about 14% if the 2028 deposit were $75k; CLAUDE.md lines 97, 181, MODEL, 27 Sep). Telling that test and the change it caused, dated and labelled as model output, is a genuine "tested, refined" story (TNA:12, :29) |
| S3 | VT is the "branch", "the part that grows" | Filler | The metaphor's anchor (Messy Roots, CASE:21-22) appears only in the IPS pitch (IPS:23). In the TNA, "branch" in quotes has no referent | Either anchor the metaphor once in the set, used the same way in all three ("the" root vs "a" root, see 4.2), or spend these 8 words on content |
| S4 | "Its expected return, about 7.5% a year per JPMorgan, can raise the upper bound ..., because half of VT's value is added to that bound" | **Number FALSE; mechanism MISLEADING** | JPM 2026 LTCMA (repo `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`, re-extracted today): AC World Equity **7.00%** compound, 8.28% arithmetic, 16.78% vol; **7.50% is EAFE** (non-US developed). The 2027 edition's 7.5% is US large cap (REG I1). Neither is world stocks. IPS:27 says 7%. The upper bound uses VT's realised **value in 2031** "less any expected payment shortfall" (IPS:29), not its expected return | If a return is cited, it is 7% compound from the 2026 edition, named as an assumption and matching the IPS. The bound depends on what VT is worth in 2031, and the reflection should include the shortfall deduction the IPS states. An expected return quoted with no risk beside it is one-sided |
| S5 | "The other half stays Laura's, giving her flexibility and covering a payment shortfall if reinvested coupons earn less or iBond payouts fall short" | MISLEADING (three problems) | (a) The filed note says stocks "only set how far her gift rises" (DRAFT:13); this sentence gives them two more jobs. (b) The same dollar cannot be both free flexibility and a payment backstop. Model: Laura's kept half is $0 in a 1-in-20 case, and the leftover plus her half fail to cover the coupon gap in 6.5-8.0% of paths (REG F8, F9). (c) "Stays Laura's" reads as money leaving the portfolio, but payments must be portfolio-funded (CASE:91-92). (d) Wrong-way risk: the bond shortfalls it covers come from yields falling and staying low, which tends to happen in downturns, when stocks are also down. V4:93: "D10 helps less where stocks and bonds fall together" (bootstrap worst case stays about $8k) | Pick the half's job(s) to match the IPS vote (D1/D10). Own the note's "only" as a refinement. Keep any backstop money inside the portfolio. Make the cover conditional, not assured. Flexibility in the case is "as the project develops" (CASE:102-103), not personal spending (living costs are outside, CASE:61-63) |

What 0.06% and 10,000 stocks actually buy: index sampling of the FTSE Global All Cap (about 98% of global investable
market cap, VGD:14-17) for about $16 a year on the WInS position (167 × $157.80 = $26.4k × 0.06%; SA, 20 Oct close)
or about $20 a year on Laura's ~$33k (REG E6). The fee is immaterial next to the risk; the breadth is the real point.
Taiwan is 3.5% of VT and TSMC 1.7% (VGD:104, 138). That is far too small to call a hedge of Taiwan costs, so do not.

### 1.3 IBTR (DRAFT:20; 99 words)

| S | Claim | Verdict | Evidence | What a fix must achieve |
|---|---|---|---|---|
| S1 | "IBTR holds 2036 Treasuries that mature in December 2036, just before ... 1 January 2037" | **FALSE** | 4 holdings maturing during 2036; weighted average maturity 9.53 years at 19 Oct 2026, about May 2036 (ISH-R:243-278); effective duration 7.55 years. The **fund** terminates on or about 15 Dec 2036 (ISH-R:699), and the proceeds are not predictable (ISH-R:700). Between the bonds maturing and the fund closing, money sits in cash at money-market rates (ISH-R:699) | Separate the bonds (they mature during 2036) from the fund's close (about mid-December). Admit the final-months cash. The note says nothing about maturity, so this is a new error the reflection introduces |
| S2 | One of five iBond funds for payments 1-5; individual Treasuries for 6-10 | TRUE, but it misses the decision | The WInS gap (no bond 15 Feb 2031 - 15 Feb 2036) explains funds for 2033-36 only. For the 2037 payment WInS **did** list the 4.5% Treasury maturing 15 Feb 2036, the recorded alternative: more fixed cash, no fee, but cash about 10.5 months early (KIT:458, 466; reasons not recorded) | IBTR is the one rung where the team had a real choice. If the team remembers why it picked the fund (timing closer to the payment versus a fixed payout), that trade-off is decision content. If nobody remembers, do not invent one |
| S3 | "Like IBTM, it is a 'root' of our strategy, held to maturity" | MISLEADING (minor) plus filler | A fund has no maturity: it is held until it closes. The point that matters goes unsaid. Holding to the end means price swings in between (the Wharton sample note's stated risk, "interest-rate changes may affect its value", TNA:37-38) do not change the cash at the end, apart from the final-months cash rate and fees | Say why interim price moves do not threaten the payment, and what still can (reinvested monthly distributions; final-months cash). This is also where liquidity belongs: the payment comes from a fund closing, not a sale (IPS:28 makes this point; the TNA never does) |
| S4 | "We bought the ladder from 2042 backwards because the furthest payments are most sensitive to interest rates, which serves her operating commitment 'with a high degree of certainty'" | Fact TRUE; as a reason INCOMPLETE; history MISLEADING; quote attached to the wrong mechanism | Fact: per $50k rung, the 2042 rung moves about $33 per 0.01 point against about $22 for 2033 (modified duration about 14.6 vs 5.9 years; my check, consistent with KIT:178-182). But buying order matters only if (i) the money runs out or (ii) prices move between orders. The reason that does the work is (i): if $300k is short, the rung left unbought should be the one whose price moves least while waiting and which the 2028 deposit can still buy. That is the pending IPS reason (IPS:27). Sensitivity alone cuts both ways: if yields rise, waiting would have been cheaper. History: in WInS the IBTR order was cancelled at 8:31 PM and re-placed at 4:42 AM, **after** IBTM (DRAFT:39), and all filled at the same open. The order describes Laura's Jan 2027 purchase, not the WInS record. Certainty comes from owning Treasuries that mature before each payment (CASE:91), not from the order of purchase | State the order rule as a rule for Laura's January 2027 purchase. Give the reason that actually decides the order: where a shortfall lands, and why that place is safest. Tie "high degree of certainty" to what delivers it. Whatever stays must match the IPS wording the team accepts; the two IPS runs give different reasons (IPS:27) |
| S5 | "If yields fall, the ladder may cost more than $300,000; the 2028 deposit then completes it, so the facility contribution is lower" | TRUE rule, but it repeats the note and drops the test | It restates the note (DRAFT:18). The note set a numeric line on 6 Oct ("more than about 0.2 percentage points by January"). **Test status on the note's own basis (D)**, LAD, MODEL: room 23.0bp on 6 Oct ($293,453), 9.8bp on 19 Oct ($297,162), **6.2bp on 20 Oct ($298,216, room $1,784)**. About three-quarters of the margin is used and the line is **not crossed**. But read as raw yields, it already has been at the long end: 6 to 20 Oct the 20-year fell 0.21 and the 30-year 0.22, the 10-year 0.15, 7-year 0.13, 5-year 0.09 points (TSY). With the 0.07% fund fee counted, the ladder cost about $300.4-300.7k on 19 Oct (REG C1). On 20 Oct it is probably about $301.5k (my estimate: the basis-D move of +$1,054 added on; fee engine not re-run, UNVERIFIED). So the 2028 top-up looks more likely than not (52% of model paths, V4:70) | The reflection must report what happened to the note's own test: a date, the basis (ladder cost, not a single yield), crossed or not, and what the rule does either way. The test is ambiguous (yields at which maturity?), so the reflection should define it by the cost line. The last close the team can see before its Thu 22 Oct 20:00 Sydney submission is 21 Oct (published about Thu morning Sydney). Write it so it is true whichever way that close goes. Name the 2028 deposit's dependence on her income (see 2.3) |

Missing from every reflection: **reinvestment of coupons and fund distributions**. One IPS run calls lower reinvestment
rates "the main risk"; the other names "falling yields and costs in Taiwan" (both on IPS:30). A permanent 2-point fall leaves about $19.5-21.3k uncovered, depending on method (REG
D1, MODEL, 19 Oct). Both iBond funds pay monthly (ISH-M:260, ISH-R:235), so their income leaves the fund and must be
reinvested to reach $50k. The trio mentions this risk once, as a clause inside the growth reflection (VT S5). It
belongs with the ladder.

Missing set-wide: why **nominal** Treasuries are an exact match. Payments are "a fixed $50,000 and ... not adjusted
for inflation" (CASE:90), so a nominal Treasury that repays dollars before each date matches the liability exactly,
and inflation matters only for the facility's real value (REG B3). Nobody says this, and it is the cleanest
one-clause justification of the whole ladder.

---

## 2. Client knowledge: every hook in the case, and who uses it

U = used, P = partly or wrongly, - = missed.

| # | Case fact (CASE line) | IBTM | VT | IBTR | Note |
|---|---|---|---|---|---|
| 1 | Author/illustrator/entrepreneur/educator (5-6, 13-14, 24-26) | - | - | - | Background only |
| 2 | Statistics degree, Wharton 2018 (16) | - | - | - | She can read a probability. Supports stating a tested number or confidence; minor |
| 3 | *Messy Roots* (21-22) | P ("root", no anchor) | P ("branch") | P ("root") | The anchor is only in the IPS pitch (IPS:23) |
| 4 | $300k 2027; $150k 2028 **from publishing advances, speaking, licensing, ventures** (43-45) | P (second deposit, no source) | - | P (2028 deposit, no source) | The IPS uses the income link (IPS:26); the TNA never does |
| 5 | Flows at the start of the year, payments exactly one year apart (59-60) | - | - | U (1 Jan 2037) | |
| 6 | Living costs outside the portfolio; no flows before 2033 (61-65) | - | P ("stays Laura's" muddles it) | - | Shows flexibility is not personal spending |
| 7 | "willing to take thoughtful risks"; wants "an appropriate balance between pursuing growth and protecting the capital required for her goals" (68-74) | - | - (gives only the reason to keep stocks small, never the reason to own any) | - | The IPS uses it (IPS:26) |
| 8 | Taiwan residency, 2033 (76) | - | - | - | |
| 9 | **Artists, writers, designers, entrepreneurs, educators** live, work, teach (77-80) | - | - | - | Human stakes of "reliable support for its early operations" (83). The payments go to operating expenses (88), not artists' pay (KIT:277) |
| 10 | Facility vs operating: portfolio must fund operations, "may also cover part of the facility" (83-86) | U (two jobs) | U (upper bound) | U (facility lower) | |
| 11 | Ten fixed $50k payments 2033-2042, **not inflation-adjusted** (88-90) | U (first payment) | - | U (fifth) | Not-adjusted is unused (see 1.3) |
| 12 | "high degree of certainty"; **no outside funding** (91-93) | - | P ("stays Laura's" risks outside money) | U (quote), P (wrong mechanism) | Why the 2028 deposit, not co-sponsors, is the backstop |
| 13 | Operating reserve set aside in 2033; composition "as the annual payments approach" (94-99) | - | - | - | The ladder runs off naturally; one clause would cover it |
| 14 | Facility contribution after the reserve; "committing all remaining assets could limit her financial flexibility as the project develops" (101-103) | - | P | - | The case's reason for the half-and-half split |
| 15 | Co-sponsors in 2031, two years before (109) | U (note), - (reflection) | U (note) | - | |
| 16 | A meaningful contribution "may signal that the residency is financially viable" (110-112) | - | - | - | Why the floor matters at all |
| 17 | **Over-promising "could damage her credibility"; "credible range" rather than "one exact amount"** (114-116) | **P (inverted: "her promise")** | P (note: "promised minimum") | - | The case's central tension |
| 18 | Range + confidence; favourable/unfavourable outcomes; range must protect the payments (117-120) | - | P (the note covers a rise before 2031; nothing on a fall after 2031) | P | |
| 19 | WInS represents implementation; WInS P&L excluded (129-133) | - | P ("9%" is WInS without saying so) | P ("we bought" mixes WInS and plan) | |
| 20 | Inflation effect on projections and **facility costs** (146-148) | - | - | - | The IPS covers Taiwan costs (IPS:30) |
| 21 | Facility cost undetermined; no budget (164-167) | - | - | - | Do not estimate it |
| 22 | TNA: reserve size, projections, contribution and co-sponsor text are not expected yet (TNA:20-23) | | | | IBTR's "facility contribution is lower" is a mechanism, so fine; do not add numbers for the contribution |

**Which missing hook gains most:** #17 in IBTM. The floor exists **because** over-promising damages credibility. The
minimum is owned in Jan 2028, before co-sponsors are approached in 2031. Today IBTM uses the case's warning word
("promise") as if it were the goal, and a judge who knows the case will notice the inversion. Second: #7 in VT (the
only client reason to own stocks at all, plus the "balance" the case asks for). Third: #4 in IBTR. The top-up
backstop depends on a deposit funded by her creative income. A downturn that pushes yields down (making the ladder
dearer) could also cut speaking and licensing income (making the deposit smaller), so the backstop is weakest exactly
when it is needed. That is the team's own insight ("career risk ... bites via the 2028 deposit", CLAUDE.md, Client
insight). It is reasoning, not data. The case still states the deposit as planned (CASE:43), so frame it as a
dependence, not a doubt.

---

## 3. Against Wharton's own model

### 3.1 Sample-note structure (TNA:36-39): action+role, benefit, stated risk, strategy link (0-2 each). "Adds" = new content the reflection gives beyond its note

| | Role | Benefit | Stated risk | Strategy link | Total /8 | Adds beyond note /2 |
|---|---|---|---|---|---|---|
| IBTM note | 2 | 2 | 2 ("final payout is not fixed") | 2 (2031 minimum) | 8 | |
| IBTM reflection | 2 | 1 (two false benefits) | **0** (denies the risk its own note states) | 1 | 4 | 2 (email history) |
| VT note | 2 | 2 | 2 ("a fall can shrink the extra") | 2 | 8 | |
| VT reflection | 2 | 1 (wrong return) | 1 (stock-picking and coupon risks; never VT's own fall) | 2 | 6 | 1 |
| IBTR note | 2 | 1 ("enough" on 6 Oct, fee-free) | 2 (numeric trigger) | 2 | 7 | |
| IBTR reflection | 2 | 1 (false maturity) | 2 | 2 | 7 | **0.5** (only the order reason is new; the rest restates the note) |

The notes are better than the reflections. Each reflection should do what a note cannot: say what happened next,
what was learned, what changed.

### 3.2 TNA asks and purpose words (0 / 1 / 2)

| Ask (source) | IBTM | VT | IBTR | Set |
|---|---|---|---|---|
| Why the decision (TNA:48) | 2 | 2 | 1 | |
| Aligned with overall strategy (TNA:50) | 1 | 2 | 2 | |
| Client goals, funding needs, risk (TNA:52) | 1 | 1 | 2 | |
| Supporting research or analysis (GUIDE:85) | 1 | 0 (false figure) | 0 (no numbers in the reflection) | weak |
| Supported / tested / refined (TNA:12, :29) | refined (claimed; cause misdated) | supported | supported (the test is set but its result is never reported) | **no "tested"** |
| Growth (TNA:5) | - | 2 | - | 2 |
| Risk | 0 (denied) | 1 | 2 | 1.5 |
| **Liquidity** | 0 ("easy to trade" is the wrong kind) | 0 | 0 | **0** |
| Funding reliability | 2 | 1 | 2 | 2 |
| Financial flexibility | 0 | 1 (contested job) | 0 | 1 |
| Future cash-flow needs | 2 | 0 | 2 | 2 |
| Triggers/rules (Wharton feedback, RUB §2e, TF2324:16-18: "Will certain triggers dictate ...?") | - | P (half rule) | P (the trigger is in the note; the reflection drops it) | 1 |
| **Coverage** | about 12/24 | about 13/24 | about 13/24 | purpose words 8.5/12 |

---

## 4. Set level

### 4.1 Does it read as one story (payments, then floor, then growth)?
No. The order is IBTM (floor + payment 1), VT (growth), IBTR (payments 1-10), which is floor, growth, ladder. The IPS
says "Buy the payments, then the floor, then growth" (IPS:27). A judge reading the TNA alongside the IPS sees the
sequence scrambled. The **2028 deposit** links all three: the IBTR top-up, then the IBTM floor, then VT with what is
left. Each reflection holds one piece and none states the order. Requirements:
- Present the three in the plan's own sequence.
- State the 2028 deposit's order once in the set.
- Give each reflection one distinct job: IBTR = the whole ladder and its rate test; IBTM = the floor and credibility,
  plus the one refinement forced by the rules; VT = growth, flexibility and the refinement from 75% stocks.

### 4.2 Duplicated
- "2028 deposit completes the ladder, so the facility contribution is lower": the IBTR note, the IBTR reflection
  (S5), and implicitly IBTM S5. Same entry, twice.
- "root": IBTM ("the root") and IBTR ("a root", "like IBTM"). Inconsistent article and no anchor. "Branch" in VT.
- Payment certainty as the priority: VT S2 and IBTR S4.
- Reflections restating their own notes: IBTM's two jobs (S3/S5 vs the note), VT's diversification and fee (S1 vs
  the note), IBTR's fifth payment and the top-up rule (S1, S5 vs the note). About 25-30 of the 292 reflection words
  repeat the notes.
- Two of the three picks are payment rungs (IBTM payment 1, IBTR payment 5). That is acceptable only if IBTM
  carries the floor and IBTR carries the whole ladder.

### 4.3 Never said anywhere in the trio
1. What happened to the pre-set test (IBTR note): the only "tested" evidence available.
2. The move from about 75% stocks to the remainder: the biggest strategy change the team made.
3. Liquidity: each payment comes from a fund closing or a bond maturing, not a sale.
4. Why price swings before the end do not matter (the Wharton sample's own stated risk) and what still does
   (reinvested distributions, final-months cash, fees).
5. Why nominal Treasuries: payments are fixed and not inflation-adjusted (CASE:90); default risk is the only
   residual (the IPS says this; the TNA does not).
6. The cost of safety: less stock means a lower typical contribution than the growth-first plan, accepted for a
   better downside (CLAUDE.md lines 97, 181; the trade-off the Guide asks for, "reasoning, assumptions, and
   tradeoffs", RUB §2b).
7. WInS vs Laura's plan: WInS is her post-2028 plan scaled by about 0.64 (REG H5). Without that, "9%" and "we
   bought" mislead.
8. Why a fund rather than the 15 Feb 2036 bond for payment 5, and why one world fund rather than the alternatives
   raised on 5 Oct, if the team decided these.
9. Credibility as the reason for the floor (CASE:114-116).
10. What a fall **after** 2031 does: the contribution moves within the range and never below the minimum (IPS:29;
    REG F7, MODEL: a 40% fall in 2032 lowers a typical contribution by about $7k).

---

## 5. The 15 highest-value changes (requirements only), ranked

| # | Where | Requirement | Expected effect on a judge |
|---|---|---|---|
| 1 | IBTR S5 | Report the outcome of the note's own 0.2-point test: dated, on the ladder-cost basis (not a single yield), crossed or not, and what the rule does either way. Make clear it concerns Laura's Jan 2027 purchase, which the WInS trade rehearses. On 20 Oct: not crossed, about three-quarters of the margin used (LAD). Must stay true after the 21 Oct close | Turns the set's only trigger into the only "tested" decision (TNA:12, :29; TF2324:16-18). Largest single gain in Investment Strategy and Portfolio Analysis |
| 2 | VT S4 | Remove "7.5% per JPMorgan" (it is EAFE or US large cap, not world stocks). Any figure is 7% compound, 2026 edition, labelled as an assumption. Tie the upper bound to VT's 2031 value less any expected shortfall, not to expected return | Removes a checkable false fact that contradicts the IPS judged alongside it |
| 3 | IBTM S4 (+S1) | Remove "clear yield" and "matures on a set date". State what moving from zero-coupons to a term fund cost (payout not fixed, monthly distributions to reinvest, fee, final-months cash) and how the plan absorbs it (minimum rounded down, IPS:29) | Turns a self-contradiction (against the team's own note and iShares) into a real "refined" story |
| 4 | IBTM S5 | Drop promise and never-fails language. Root the floor in the case's credibility logic (CASE:110-116): the minimum is owned in 2028 before co-sponsors hear it in 2031. Name what can still move it (yields before Jan 2027 through the top-up; the fund's payout) | Best client-knowledge gain in the set. Removes the line a finance judge would attack |
| 5 | Set | Put the reflections in the plan's order (payments, then floor, then growth). State once how the 2028 deposit is spent (top-up, then floor, then stocks) | Makes the trio read as one "cohesive portfolio strategy" (TNA:14-15) consistent with IPS:27 |
| 6 | VT S2 | Replace the size rationale with the real one: stocks are the remainder after payments and floor, and the team cut from about 75% after testing showed missed payments (dated, model-labelled). Say which portfolio "9%" refers to (WInS) and that Laura's is about 7% | Adds the biggest true refinement the team made. Fixes a number judges can compare with the IPS |
| 7 | IBTR S1 + S3 | Correct the maturity facts (bonds mature during 2036; fund closes about 15 Dec). Replace "held to maturity" with holding to the fund's close. Say why interim price swings do not change the cash at the end, and that the payment comes from a closing, not a sale | Removes a false fact. Answers the Wharton sample's stated risk. Adds the missing liquidity dimension |
| 8 | IBTR S4 | Give the reason that actually sets the order (where a shortfall lands and why that rung is safest to leave open). Frame it as Laura's Jan 2027 rule, not WInS history (the IBTR order was re-placed after IBTM). Attach "high degree of certainty" to Treasuries maturing before each payment. Match the IPS run the team keeps | A finance judge sees reasoning, not a slogan. Nothing the WInS fill record contradicts |
| 9 | VT S5 | Decide the kept half's job(s) (D1/D10). Own the note's "only" as a refinement. Keep any backstop inside the portfolio. Make the cover conditional (it can be $0 in a bad case, REG F8). Use flexibility "as the project develops" (CASE:102-103) | Removes a contradiction with the note, the case (CASE:91-92) and possibly the IPS |
| 10 | VT | Give the client reason to own stocks at all (CASE:68-74, "thoughtful risks", "balance"). Say what a fall after 2031 does (it moves the contribution within the range, never below the minimum) | Client Knowledge, plus the "unfavourable outcomes" the case asks about (CASE:118-119) |
| 11 | IBTR or IBTM | Name reinvestment of coupons and monthly distributions as the payments' main remaining risk (the IPS names it in both runs, as "the main risk" in one, IPS:30), with the plan's answer | Consistency with the IPS. Shows the team knows how term funds actually pay |
| 12 | IBTR S5 | Name the top-up's dependence on her creative income (CASE:43-45), and why this backstop is weakest when it is most likely needed (a downturn lowers yields and income together; reasoning, not data). Frame it as a dependence, not a doubt | Client Knowledge, and matches IPS:26. Shows the team sees the correlation |
| 13 | IBTR S2 | If the team remembers it, explain why a fund for payment 5 when WInS listed the 4.5% 15 Feb 2036 bond (timing vs fixed payout). If not, do not invent a reason | Real decision content on the one rung where a choice existed |
| 14 | IBTM | Show that the top-up and the floor are the same fund from the same deposit (a yield fall moves IBTM from floor to payment 1). This replaces "a stock crash will not ..." as the protection story | Joins IBTM and IBTR into one mechanism and removes the "who absorbs a top-up" contradiction. An elegant, simple insight of the kind judges reward |
| 15 | All | Pay for the above inside 100 words. Cut the restated note facts (about 25-30 words), the anchorless "root"/"branch" lines (or anchor the metaphor once and use it the same way), "easy to trade" and "the part that grows". Aim for 95 words or fewer each (VT and IBTR are at 99 now) | Without this, items 1-14 cannot fit. The form limit is "100 words or fewer" (TNA:46) |

**If time is short:** do 2, 3 and 7 first (they remove false facts; about 10 minutes), then 1 and 4 (the largest
score gains), then 5 and 6.

## 6. Limits
- Every ladder, floor and odds figure is MODEL output on the treasury.gov curve named, with yields held to 1 Jan 2027
  (basis D). The 20 Oct fee-counted cost is my estimate and was not re-run.
- iShares holdings lists did not download (the page loads them with JavaScript). The maturity facts rest on the
  index description, holdings count and weighted average maturity on the fund pages.
- VGD data are as of 30 Jun 2026. The holdings count on 20 Oct comes from a third party (SA).
- Team history (75% stocks, Darren's 5 Oct challenge, the Feb-2036 alternative) comes from the repo's CLAUDE.md and
  KIT. The students must confirm it from memory before using it.
- Word counts are from `SP/oct21/tna/factcheck/factcheck.md` §1.
