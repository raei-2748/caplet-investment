# Lab candidates for the IPS, after rungs 1-3 (Sat 24 Oct 2026). To be stress-tested.

Context: BRIEF.md (same folder). Current full IPS draft (494 strict words, pitch 47) is the "Full text" section of
/mnt/project-files/ips/IPS_edits_v2_2026-10-24.md (read it). Rung files: rung1A.md, rung1B.md, rung2.md, rung3.md.
All numbers MODEL on the 22 Oct 2026 Treasury close unless marked HISTORY. The IPS carries no numbers or citations.

## Verified outside facts (fetched 24 Oct 2026)
- FASB Statement No. 76 (Nov 1983, since completely superseded): debt treated as extinguished when the debtor
  "irrevocably places cash or other assets in a trust" solely for the scheduled payments, the assets "essentially risk
  free as to the amount, timing, and collection of interest and principal" (direct US government obligations), with
  cash flows that "approximately coincide, as to timing and amount" with the debt payments, and the chance of further
  payment by the debtor "remote". https://storage.fasb.org/fas76.pdf
- NSW Water Allocation Methodology, Murrumbidgee Regulated River (PUB20/832, Mar 2022): opening allocation of 95%
  to high security; "Only when these opening allocations have been made, can allocations begin to accrue to general
  security entitlements"; "High security allocation is always greater than general security allocations until they
  both reach 100% of entitlement"; general security rises through the year as inflows arrive (e.g. 30% -> 50%); a
  second-year reserve is held "to ensure the required opening allocation to high priority commitments", planned
  against inflows no drier than the driest observed drought; carryover of unused water exists.
  https://www.water.nsw.gov.au/sites/default/files/2025-08/water-allocation-methodology-murrumbidgee.pdf
- "Firm yield" (water supply): the volume available from storage "during a specified critical dry period to meet
  water needs under a predetermined demand schedule" (Montana definition, lawinsider.com/dictionary/firm-yield).
- Caplet are Sydney students (Australian); the case has nothing about Australia.

## Candidates (idea -> proposed IPS words, at most ~25 words each)
| # | Idea | Rests on | Criterion / ask | Proposed IPS words (AI DRAFT) |
|---|---|---|---|---|
| C1 | Define "high degree of certainty" as defeasance with one named leak | FAS 76; locked TNA "near-ironclad guarantee, and we provide exactly that" | HC "define", CK, IS | "By high certainty we mean defeasance: Treasuries matched to each payment in timing and amount. The one leak is that coupons arrive early and must be reinvested." |
| C2 | A rate fall before we buy lands on the facility, never on a payment | rung2 #1: -100bp +$31.4k, +100bp -$28.0k; cost $293.9k->$298.9k in one day | BAL, HC, PR | "If yields fall before we buy, the facility floor shrinks dollar for dollar; the payments are bought first and never shrink." |
| C3 | The operating reserve is bought in 2027 and only renamed in 2033; it shortens by one payment a year | rung2 #4 (DV01 $296 -> $161 in 2033 -> $0 in 2042) | RES "composition over time", ALLOC | "The operating reserve is bought in 2027 and renamed in 2033, not rebuilt; it is all Treasuries and shortens by one payment each year." |
| C4 | The payments need only what Treasuries already pay; no return forecast funds them | rung2 #2: IRR 5.09-5.13% = the curve | ASM "returns" | "The payments need only the yield Treasuries pay today; no forecast of ours funds them." |
| C5 | The range is set by the rules, so the honest confidence is how often the gift reaches the top; stocks rising after 2031 change nothing | rung3 B2, range_2031 README (~3 in 4 reach top; ~99% inside) | CK co-sponsors, HC, R (range method; final range not expected in IPS) | "The rules keep the gift inside the range, so the confidence we will state is how often it reaches the top, not whether it lands inside." |
| C6 | The half Laura keeps backs two risks that rarely arrived together in US history | L-04 HISTORY: 1954-2011 cost spike given lasting yield fall 20% vs 51.5% otherwise; joint 8.6% vs 16.3% if independent; 1871-2011 weaker 21% vs 31%; US CPI not Taiwan costs | BAL, ASM inflation, FLEX | "Her half backs two risks, lasting falls in yields and rising building costs, that seldom arrived together in US history." |
| C7 | Cash timing: holdings mature up to eleven months early; the waiting cash earns bill rates, so expect a small January gap | rung2 #5: +$0.8k, headroom ~$0.3k | ASM "timing of cash flows", LIQ | "Holdings mature up to eleven months before their payment; that cash waits in a short-term Treasury ETF." (exists partly) |
| C8 | Laura's 2028 income is most likely short in the paths that need it most (yields fall in slowdowns, fees shrink); the plan copes because the longest bonds are bought first with money she already owns | case :2 (2028 money from advances, speaking, licensing); 47-57% of paths need a top-up (MODEL); slowdown link INFERRED | CK, IS | "Her 2028 deposit comes from fees that shrink in the same slowdowns that raise our costs, so it fills the gift, never a first payment." |
| C9 | Motif, used once: the NSW water licence. Payments = high security, filled first from water already stored, with next year's reserve held back; the gift above the floor = general security, rising only as inflows (markets) allow, up to 100% of entitlement (the cap) | NSW WAM (verified); Caplet is Australian; cold test: 0 of 24 water names | CP, IS, CK (weaker: not Laura's world) | "Australian rivers ration water this way: high-security licences are filled first from storage; general security rises only with the rain. Laura's payments are high security." |
| C10 | Name candidates from C9 / firm yield: "Firm Yield"; "General Security"; "Dry-Year Rules"; "Opening Allocation". Rival: print run (Keel's Monday default) | as above | CP, north star 2 | (name only) |

Already in the draft and still standing: K2 "One yield sets both the ladder's January price and what its coupons earn
later, so a lasting fall works twice." C1 and C2 may replace or merge with K2.
