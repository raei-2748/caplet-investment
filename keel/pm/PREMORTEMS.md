# Pre-mortems (real; run before each deliverable is drafted)

Method (Klein): "It is the day after the deadline and the deliverable failed. Write down why." List causes, rate
likelihood (H/M/L, judgment, not a model), name an early warning, and turn each prevention into a board card or a
risk. Kai attacks; Nora writes it down; the team adds its own causes before reading Keel's.
Source for much of this: `keel/library/assistant_review_2026-10/05_Premortem_Review_16Oct2026.md` (16 Oct).

## TNA (quick, 23 Oct; due Sat 24 Oct 08:00)
| Cause | L | Early warning | Prevention |
|---|---|---|---|
| A note does not match WInS character for character (curly quote, extra space) | M | Pasted from the Google Doc, not from WInS | Paste from WInS as plain text; exact-match check with `keel/office/tools/textcheck.py` |
| A reflection is over 100 words on SMApply's counter | L | Strict count above 95 | Count on the stricter method (hyphens split) |
| Submitted late or the form times out | L | Not submitted by Fri evening | Submit Fri evening, save the confirmation [T01] |
| The wrong IBTR trade note picked | L | Two IBTR notes exist | WO-0001 trap note |

## IPS (v1, 23 Oct; due Sat 7 Nov 09:00; strategy frozen after it)
"It is 8 Nov. The IPS went in, and we already know it will not carry us to the semifinal. Why?"
| # | Cause | L | Early warning | Prevention (card / risk) |
|---|---|---|---|---|
| 1 | It reads as AI text, not the students' voice; or AI wording is in it with no way to cite it (IPS bans citations) | H | Sentences from V5 or the exemplar survive in the outline | Write from the voted rules, close all [AI] suggestions first [T13]; R3 |
| 2 | A rule the Final Report needs is missing (reserve, certainty, sail size, facility rule, 2031 range, review policy, diversification), so the Final Report must change strategy after the freeze | H | Checklist gaps on 27 Oct | IPS rule checklist [T05]; vote set B [T12]; R4 |
| 3 | Figures with no source or on mixed bases ($294k, $21k, 7%, 99 in 100) | M | Any number without a date and basis | Keep numbers out of the IPS (not expected there); P02; R5 |
| 4 | "High certainty" overclaimed ("guaranteed", "only", "one risk") while coupon reinvestment and IBTM's payout are real risks | M | Absolute words in the draft | Vote the certainty wording [T12]; gate check [T09]; R2 Closed 26 Oct as a wording risk: `../BIBLE.md` rule 3 (only a false claim is a risk) |
| 5 | Over the word limit on SMApply's counter, or a field missing on the new form | M | Strict count above 470 / 45 | Check form fields [T15]; strict count margin [T09]; R7 |
| 6 | The WInS book does not match the IPS when it locks, or a needed order fills after the deadline | L | A vote changes the allocation after Mon 2 Nov | Last order by Thu 5 Nov 08:00 [T16]; R8 |
| 7 | Correct but forgettable: an engineered bond ladder with the one creative idea buried | H | Pitch does not say "a range built to hold" or an equivalent idea in the team's words | Mock-judge pass [T08]; pitch tested on an outside reader [T14]; R9 |
| 8 | TIPS or STRIPS mentioned anywhere | L | The words appear in the draft | Gate check [T09] |
| 9 | Students cannot defend a sentence aloud | M | No named author per paragraph | Named authors [T13]; drill P01 |

### IPS v2 update (Sun 25 Oct weekly plan; Kai attacks the v4.1 vote copy, Nora writes it down)
Status of v1 causes: 3 eased (v4.1 holds no model number; vote sheet goes onto one edition Mon 26 Oct, P02/P06);
8 still clean (0 hits for TIPS/STRIPS in v4.1); 1 and 7 are now the top two.
| # | Cause | L | Early warning | Prevention (card / risk) |
|---|---|---|---|---|
| 10 | Keel's v4.1 vote copy becomes the IPS: it is complete and counted, the students have no outline, so it gets pasted | H | No student outline by Wed 28 Oct; v4.1 sentences in the Doc word for word | Version freeze Tue 27 Oct [T23]; outline from the voted rules [T13]; R3 |
| 11 | The IPS says the 2027 deposit goes entirely to the payments while the frozen WInS book holds the floor ETF and VT; a judge sees a contradiction | M | The WInS sentence ("shows the 2028 allocation, scaled down") cut for words | Keep that sentence; coherence check [T07]; R8 |
| 12 | The bond-floor line or "any rise stays with Laura" promises more than an ETF that pays NAV can give | M | "equal to", "stays with", "always" in the draft | Keep the 25 Oct fix; gate check [T09]; R15 |
| 13 | The IPS names a holding WInS does not list (the short-term Treasury ETF where coupons wait) | M | No listing answer by Sat 31 Oct | Ray checks read-only [T24]; R14 |
| 14 | The IPS breaks a locked TNA line (see the coherence list below) | L | A stock-return figure other than 7.5%; inflation said to threaten a payment; a price-triggered sale | Coherence check [T07] against the list below |

**Coherence with what is locked** (submitted TNA, 11 WInS notes; Archive register A1-A10, 24 Oct: 0 contradictions,
3 WATCH). The IPS must keep: (A1) any stock return stated is 7.5% from the 2027 J.P. Morgan LTCMA, as the VT
reflection says, or none; (A2) inflation belongs to facility and overrun costs, never to the fixed nominal payments;
(A4) a payment holding is replaced only if it becomes unavailable, never because of its price ("every year the bonds
sit untouched is a good year"); (A10) the spine, "commit only money she already owns". Pitch, IPS and Final Report
tell one story: the promise bought first, growth only from what is left, a 2031 range no higher than what she owns.

### IPS v3 update (Sun 1 Nov weekly plan, on V47; Kai attacks, Nora writes it down)
"It is 8 Nov. Caplet submitted, and we already know it won't make the 50. Why?" Causes 1-14 above were written for a
student-drafted IPS; Book 9-10 changed the process (Keel drafts, Caplet rewrites), so this list replaces them.
| # | Cause | L | Early warning | Prevention (card / risk) |
|---|---|---|---|---|
| 15 | It sounds like a machine: a results table in prose, colons doing the joints, Caplet rejects it Thursday or rewrites it in a panic | H | Voice reader 10 ranked V47 last of four ("model-speak") | Voice pass that drops no idea [K01]; GPTZero Wed [K02]; R3 |
| 16 | A judge holds the IPS beside the frozen WInS book and sees VT bought with money the IPS says buys only Treasuries | M | No WInS clause in the final | One clause [K01]; R8 |
| 17 | Two floors on one page ($150,000 then $145,000) and no stated return: the judge stops trusting the numbers (PA: "reasonable assumptions") | M | Window 1 Nov near-breach; V46 Bible check W11 | Bridge clause and 7.5% stated [K01]; R15 |
| 18 | The rival paragraph wins the argument it was meant to lose: "it usually wins ... about $15,000 more" is a mean, the typical lead is about $10,000, and the worst-twentieth slice is the S0 world | M | "on average" dropped in a voice edit | Keep "on average" and the slice named; Window re-reads the paragraph after the voice pass |
| 19 | The draft that wins Wednesday is a coin-flip between panel and ear, chosen in the last hour | M | A new champion on Wed 4 Nov | Dial 0 : 3; nothing new after Tue 3 Nov; R17 |
| 20 | It breaks a locked TNA line (list below) | L | See the coherence list | Window reads the final against it Wed 4 Nov |

**Coherence of V47 with what is locked** (`ips_rewrite/00_GROUND_TRUTH.md` section 3; checked 1 Nov 17:00):
consistent on the ladder matched to each payment (note 1, reflection 1), IBTM's two jobs, payment and floor (note 2),
VT as the only growth and the top moving with stocks (note 3), the reinvestment leak (note 1: "cash paid early earns
less"), "near-ironclad" read as a list of ways to fail, and the 2028 deposit topping up the ladder first ("or nearly";
IBTR note). Inflation appears only as a dearer building in Taiwan dollars, never as a threat to a cheque (A2). Two
watch items: (W1) the WInS book holds VT with the first $300,000 (cause 16); (W2) the VT reflection says "about 7.5% a
year (as per JPMorgan)" and V47 states no return; stating 7.5% fixes cause 17 and matches the locked line (A1). The
spine holds: buy the promise first, grow only what is left, name a range no higher than what she owns.

## Final Report (seed, 23 Oct; complete by Wed 11 Nov [T10])
Likely causes to test once the instructions are out (10 Nov): school letter missing or not on letterhead (R6);
projections without a stated basis or that contradict the IPS (R5); strategy changed after the freeze (R4); AI use
not recorded in the Works Cited (R3); a competition-experience story that is invented or generic (never invent:
Wharton ethics); rushed in the last week (R10); the 2031 range promised above what Laura owns.
