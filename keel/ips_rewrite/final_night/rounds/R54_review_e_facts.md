# R54 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

IPS 493 strict; pitch 50 (limit). `ladder_pv.py`, 23 Oct close: ladder $297,636 (66% of $450,000); Jan 2028, $117,641 buys a $150,000 Dec-2032 payout, leaving $32,359 (MODEL).

| Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|
| P1 payments "are a debt ... fixed in dollars and payable only from her portfolio" | TRUE; "debt" STRAINS | case:88-92; refl. 1 "the liability" (archive.md:36) | "Debt" is analogy (no lender); the case says commitment |
| P1 "only figures she already holds in Treasuries" | TRUE with P4-P5 | A5 archive.md:73; A18 :86 | She holds at least the rounded-down bottom, not that exact sum |
| P2 "two thirds of her $450,000" | TRUE | re-run; 00_GROUND_TRUTH.md:86-88 | "Today" = 23 Oct close |
| P2 mix "richer by 2042"; facility money "swing far harder" | TRUE (MODEL) | models/README.md:73, :78-80 | Leverage holds (~3x); there payments also fall short (1.3-7.6%) |
| P3 bond or fund per payment, "repaid in the year before", 2028 top-up | TRUE; "repaid" HALF-TRUE | snapshot:22-31; IBTR note 02c:56-58; casestudy:79 | Funds pay net assets, no "predetermined amount"; P4's caveat covers them only if read back |
| P3 "Every holding lends only to the US government" | HALF-TRUE | casestudy:61, :86-87; archive.md:79 (backing "does not apply to the funds") | False of the world index fund. Five funds lend via iShares, adding non-default risks (unfixed payout; Board can move end date) |
| P3 "barring a US default, no payment depends on a share price or on selling a bond early" | TRUE only with P5 | 02c:245 (T12); A33 archive.md:101 | Also assumes the 2028 deposit arrives (case:43-44), unstated; A33's halved-deposit corner breaks it (0.94%) |
| P4 deposit from "a career of thoughtful risks in publishing, speaking and licensing, whose earnings can dry up in the same slump" | HALF-TRUE | case:43-45, :69-71; october_allows:36 (C5); 02c:261 | Case: "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" (last dropped); risk-taking is a separate sentence. No income-market link in the case: "can" is the ceiling, "dry up" overreaches |
| P4 stake in the 2033 payment's fund, "rounded down", sets the bottom; rest ≈ "what the stake will earn" | TRUE | IBTM note archive.md:41; A30 :98; 02c:246, :248 | |
| P4 "If every share were lost, the stake would still return about all she put into both" | TRUE (literal) | construction; A33 (lock then from the floor, median $12,688) | A loss before 2031 sends the gap to the stake, lowering the bottom |
| P5 "One gap is left": interest and early repayments wait at short rates | TRUE | Note 1 archive.md:34; 02c:59-77, :243; A16 :84 | Must include cash inside the five funds (casestudy:81-82; A33 rule 2) |
| P5 half for the gap at zero earnings; half for the top; top cut before bottom | TRUE (design) | 02c:244; A19 :87; A27 :95; A31 :99 | Dated, into Treasuries, price stated: meets A19/A33 |
| P6 "no market can move her outside the range" | TRUE (design), absolute | 02c:249 (T16, older design); range_2031/README.md:41-45 | Rests on rounding down covering payout drift; not re-run on this design |
| P6 "the building's cost ... decides how far above it" | STRAINS | VT note archive.md:48 ("They only set how far her gift rises above her promised minimum"); range_2031:26 | Shares set the top before naming; gift following the facility's remaining need is a rule October never stated |
| P6 flexibility "comes after the payments and her promise" | TRUE | case:101-103; A19 | Applies on naming day; after 2033 kept shares never back a payment |
| P7 reserve "needs no trade"; "one redemption a year until the tenth" | HALF-TRUE; TRUE | case:94-97; Note 1; Nov-2041 note 02c:75-77 | Set-aside needs no trade; paying does (the waiting short-term Treasury fund is sold). Size never given |
| Pitch "every dollar Laura promises into Treasuries before anyone counts on it" | TRUE with IPS rules | rows above | Interest share covered only at the 2031 set-aside, still before 2033 |
| Pitch "first $300,000 buys Treasuries for her ten ... payments" | HALF-TRUE | 02c:236, :260 | One-close call (under by $2,364 on 23 Oct; over on 22 Oct holdings bases); IBTR note's sentence, so allowed |
| Pitch "Most of her 2028 deposit buys the bottom"; "half her shares, sold then, set its top" | TRUE | 02c:246; VT note; A27 | After any top-up; the other half is sold too |

## What the locked record needs that the draft lacks
1. **The good-market path:** a rise before 2031 lifts the top (VT note; 02c:90). Implied, never said; case:118-119 asks.
2. **Assumptions beyond a US default:** deposit arrives; start-of-year flows; no outside money; inflation hits the facility, not payments (case:146-148; 02c:160-162).
3. **How certainty was evaluated** (case:98) and **the reserve's size** (case:96).
4. **Replacement rule** (A4, archive.md:72): a Board moving a fund's end date (casestudy:86-87) is the one event that could force P3's excluded "early sale".
5. **"Other entrepreneurial ventures"** (case:45); the funds' **liquidity trade** (refl. 2; C6).

Nothing contradicts a submitted word outright; P6's "building's cost decides" and P3's "Every holding" come closest.
