# Q5 research cards: is keeping half of the shares the right amount of flexibility?

Research run, Mon 9 Nov 2026 (Sydney). Notes for the Final Report store, not report prose. Claim tested tonight:
"Keeping half of the shares, about a fifth of the stated contribution in the middle case, is a sensible amount of
flexibility for a building project of this kind." Classified as project cost contingency, and decisions made under
uncertainty. Checked against Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt`), the case
(`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, cited as "case l.N", line numbers of the .txt) and
`keel/final_report/CANON.md`. The plan is frozen: a "yes" in the Clash column is a risk to note in the Final Report,
never a change to propose.

Limits kept: no estimate of Laura's building cost; percentages only. The case says teams "are not expected to
determine the size or investment composition of a separate contingency fund" (case l.106-107) or "estimate that cost"
(case l.164), so everything below is illustration of the kind CANON A31 allows ("What each risk could cost against the
kept half, as illustration only"), not a sizing.

How to read the table:
- Tags as in `../HARVEST_BRIEF.md` (HALFKEPT, INFLATION_TWD, COSPONSOR, MOVE2031, CERTAINTY, OTHER).
- Verified? = VERIFIED (with what I read: full text, a PDF table, an abstract page or a search excerpt of the source
  itself) / UNVERIFIED (not read at the source). "Keel arithmetic" or "Keel inference" = my own sum or reasoning.
- All URLs accessed 9 Nov 2026.
- Kept-half figures come from the number register as it stands today (`keel/final_report/NUMBERS.md` section 4 and
  section 8f, `numbers/results_kept_half.json`). **Correction to tonight's brief:** the $13k / $24k / $45k quoted in the
  brief is the version before the 9 Nov move to J.P. Morgan's 2027 volatility (NUMBERS.md l.203). The register now
  gives $12,150 / $23,831 / $46,746 (house model, 1-in-20 low / median / 1-in-20 high; section 4 rounds to $12k / $24k
  / $47k). Against $110,000-$135,000 that is 9.0%-42.5%, not 10%-40%.
- Store checked first (`../store/insights.jsonl`). Already held and not repeated: Flyvbjerg's mean building overrun
  of about 62% (Q9-025), the Green Book's +51% via NWSSP and the megaproject anecdotes (H7-086), real options via
  Damodaran (H3-052, H6-093, H7-085), the contractor's contingency (H3-072), the order of call in a cost-overrun
  facility (H4-033), and Q9's Weiwuying +28.64% and the "kept half sits in shares" risk (Q9 rows 26 and 30). Rows
  below add primary sources the store lacked (Green Book table, Dixit and Pindyck) or new evidence.

## Verdict on the claim

**CHANGE.** About a fifth is sensible for one risk, building overruns, at middle odds. It is low for high confidence
at Laura's 2031 stage, and low for the three uses the IPS names taken together.

- **Where the kept half sits.** In the middle case it is $23,986, which is 17.8% of $135,000 and 21.8% of $110,000.
  Within any one path it is 9% / 17% / 31% of the top of that path's range (house model; 11% / 19% / 31% on US
  history). In a 1-in-20 bad market it is about a tenth (row 1).
- **Against what public builders hold for overruns alone at an early stage, it is about right.** Examples: Norway's
  reserve between P50 and P85, 13% for buildings (row 19); Denmark's 110 cultural buildings, +13% for 80% confidence
  and about +28% for 90% (row 16); England's "uncomplex buildings", P50 4% and P80 32% with a trimmed mean of 22%
  (row 14); the US GSA's 10% design plus 7% construction contingency, about 17% (row 25); Wisconsin 15% (row 26);
  Taiwan's planning-stage contingency for smaller, simpler buildings, 0-10% (row 24). A fifth sits at or above most of
  these.
- **Against an 80% chance of covering overruns at an early, unbuilt stage, it is low.**
  - AACE Class 5 estimates for buildings run to +30% to +50% at the high end of an 80% band, even after a contingency
    set to give even odds (row 3).
  - The Green Book's upper bound for non-standard buildings is 51% at outline business case, and higher earlier (rows
    8-9).
  - The reference class for buildings behind England's transport guidance needs +84% for 80% confidence at the
    decision to build and +145% at the first business case (row 12).
- **For overruns, a ten-year-high Taiwan dollar and escalation at once, it is low.**
  - The Taiwan dollar back at 27.52 alone needs +19.1% (row 32).
  - Two years of Taiwan cost growth at 3% needs +6.1%.
  - Added to a 13-17% overrun reserve, that is about 38-46% (row 32). Cost engineers keep these three apart, and size
    each one (rows 6-7, 15, 23).
- **Changed claim (a note, not prose).**
  - In the middle case the kept half is about a fifth of the range. That is in line with what public builders hold
    above a budget for overruns alone at an early stage.
  - It is not enough to meet overruns, a much stronger Taiwan dollar and cost growth all at once.
  - In a bad market it is nearer a tenth. It is a first cushion; other unpromised money stands behind it (row 34),
    and so does Laura's own say over scope.

Comparison used for the verdict (kept half: 17.8%-21.8% in the middle case; 9.0%-11.0% at the 1-in-20 low):

| Norm | Source (row) | Stage | Percentage | Kept half, middle case |
|---|---|---|---|---|
| Taiwan PCC buildings, contingency | Building volume (24) | Planning | 0-10% smaller or simpler; up to 15% larger or complex | above |
| Taiwan PCC major projects, allowable cost variation | General volume (22) | Feasibility / planning | 15-30% / 10-25% | inside |
| US GSA, new construction | P-120 Table 3-1 (25) | Planning and development | 10% design + 7% construction | about equal |
| Pennsylvania DGS | 2025 standards (26) | Programming / concept | 15-20% + about 10% construction | below |
| Norway, P85 minus P50 | NTNU 2026, Table 4-5 (19) | Decision to build | buildings mean 13% (3% to 28%) | above |
| Denmark, cultural buildings | Realdania 2007, Figure B (16) | Decision budget | +13% for 80%; about +28% for 90% | between |
| England, uncomplex buildings | Homes England 2024, Table 4 (14) | Business case | P50 4%; P80 32% | between |
| UK Green Book, buildings | Table 1 (8) | Outline business case, upper bound | standard 24%; non-standard 51% | below non-standard |
| AACE 56R-08, Class 5 | Table 1 (3) | 0-2% of design done | high end +30% to +50% | below |
| DfT/OGP, buildings, P80 | Table 5 (12) | Full / outline / strategic business case | 84% / 101% / 145% | far below |

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | The kept half as a share of the range. Middle case $23,986: 17.8% of $135,000, 21.8% of $110,000. House model 1-in-20 low / median / 1-in-20 high $12,150 / $23,831 / $46,746: 9.0%-11.0%, 17.7%-21.7%, 34.6%-42.5% of $110k-$135k. Within each path, 9% / 17% / 31% of that path's top (history 11% / 19% / 31%) | `keel/final_report/NUMBERS.md` s4 (l.141) and s8f; `numbers/results_kept_half.json` (`kept_as_share_of_top_p5_p50_p95` 0.0939 / 0.1722 / 0.3106 house, 0.1099 / 0.1887 / 0.3059 history) (accessed 9 Nov 2026) | HALFKEPT | NICHE | The number every norm below is compared with | The brief's $13k / $24k / $45k is superseded (NUMBERS l.203); the range is 9%-42.5%, not 10%-40% | Keel arithmetic on the register | no | This run: NUMBERS.md and JSON |
| 2 | In bad markets the kept half shrinks as a share. Shares fell over 2031-33 (28.4% of house paths): median $17,663 = 13.1%-16.1% of the range. Fell more than 20% (7.3%): $14,839 = 11.0%-13.5%. Under $15,000 in 12.9% of paths | NUMBERS.md s8f table (accessed 9 Nov 2026) | HALFKEPT, COSPONSOR | NICHE | Puts Q9 row 30's risk in the same units as the cost norms: in bad years the cushion falls to Taiwan's small-building planning norm (0-10%, row 24) | Adds percentages only; the risk itself is Q9 row 30 | Keel arithmetic on the register | yes, partly: as Q9 row 30, the cushion is smallest when the IPS expects co-sponsors to cut; a risk to note | This run: NUMBERS.md s8f |
| 3 | Cost engineers grade estimates by how much design is done. For buildings (AACE 56R-08 Table 1, 80% confidence band "after application of appropriate contingency (typically to achieve a 50% probability of project overrun versus underrun)"): Class 5 (0-2% defined) -20% to -30% / +30% to +50%; Class 4 (1-15%) -10% to -20% / +20% to +30%; Class 3 (10-40%) -5% to -15% / +10% to +20%; Class 2 (30-75%) -5% to -10% / +5% to +15%; Class 1 (65-100%) -3% to -5% / +3% to +10% | AACE International RP 56R-08, Cost Estimate Classification System: as applied for the building and general construction industries (Rev. 7 Aug 2020), sample and contents PDF https://web.aacei.org/docs/default-source/toc/toc_56r-08.pdf (accessed 9 Nov 2026) | HALFKEPT, MOVE2031, CERTAINTY | KNOWN | In 2031 Laura's building is at Class 5 or at best Class 4, so even after an even-odds contingency, 1 in 10 outcomes lands above +30% to +50% (Class 5) | The band is for the whole project's cost, not Laura's share of it (row 33) | VERIFIED (sample PDF of the RP, Table 1 read) | no, but at Class 5 the high end is above the median kept half; a risk to note if the report calls it "enough" | This run: AACE sample PDF |
| 4 | The same RP: "for weak project systems and complex or otherwise risky projects, the high ranges may be two to three times the high range"; it covers residential, hotels, resorts and offices, and not "one-of-a-kind" buildings "like concert halls, sports stadium" | AACE RP 56R-08, as row 3, https://web.aacei.org/docs/default-source/toc/toc_56r-08.pdf (accessed 9 Nov 2026) | HALFKEPT | NICHE | A small residency where artists "live, work, teach" (case) is nearer housing or a small hotel than a concert hall, which supports using the ordinary building bands; a first-time founder's project system is likely "weak", which argues the other way | Whether Laura's building is converted or new is unknown; refurbishment adds risk (row 9) | VERIFIED (sample PDF) | no | This run: AACE sample PDF |
| 5 | Process plants are wider than buildings: AACE 18R-97 Class 5 -20% to -50% / +30% to +100%; Class 4 -15% to -30% / +20% to +50%; Class 3 -10% to -20% / +10% to +30%. RAND's study of process plants: contingency "as high as 30 to 50 percent for very early estimates to as little as 2 or 3 percent" | AACE RP 18R-97 matrix as reproduced in a Government of Canada tender annex, https://canadabuys.canada.ca/documents/pub/att/2021/10/28/2305b22cf3ce2931a9ca532a8274cba4/appendix_e_-_annex_7.2_-_classification_system_cost_estimate_matrix.pdf ; AACE contents PDF https://web.aacei.org/docs/default-source/toc/toc_18r-97.pdf ; RAND N-2386, https://www.rand.org/content/dam/rand/pubs/notes/2005/N2386.pdf (accessed 9 Nov 2026) | HALFKEPT | KNOWN | Shows that the "about 20%" debate depends on project type: buildings are the narrow end of the scale | RAND is about chemical plants, not buildings | VERIFIED (18R-97 table in the Canada annex; contents PDF); RAND VERIFIED via search excerpt of the PDF only | no | This run: Canada annex PDF, AACE contents PDF, search excerpt of RAND |
| 6 | In cost engineering a contingency is a narrow thing. It "usually excludes: a) Major scope changes such as changes in end product specification, capacities, building sizes, and location ...; b) Extraordinary events ...; c) Management reserves; and d) Escalation and currency effects", and it "is expected to be expended". Money "for discretionary management purposes outside of the defined scope of the project" is a MANAGEMENT RESERVE, sized by risk tolerance | AACE RP 10S-90 Cost Engineering Terminology, https://library.aacei.org/terminology/welcome.shtml and https://library.aacei.org/pgd02/pgd02.shtml ; RP 44R-08 contents PDF https://web.aacei.org/docs/default-source/toc/toc_44r-08.pdf (accessed 9 Nov 2026) | HALFKEPT, INFLATION_TWD, COSPONSOR | NICHE | In AACE's own words the kept half is a management reserve, not a contingency: it covers overruns, currency and a funding gap, and nobody expects it to be spent | Laura is the owner, not a project manager; the terms come from industrial projects | VERIFIED (AACE online terminology pages; 44R-08 contents) | yes, partly: the IPS gives one pot three jobs (overrun, Taiwan dollar, co-sponsor gap) that this vocabulary keeps apart; a risk to note and a word to use, not a change | This run: AACE terminology pages |
| 7 | AACE keeps escalation and currency out of contingency: "contingency specifically excludes escalation"; "Differentiate between escalation, currency and contingency" (58R-10); risk values "excluding escalation, currency, and other primarily monetary or financial risks" (40R-08); "In no event should contingency ever be treated as a source of funds to cover scope changes" (41R-08) | AACE 58R-10 contents https://web.aacei.org/docs/default-source/toc/toc_58r-10.pdf ; 40R-08 contents https://web.aacei.org/docs/default-source/toc/toc_40r-08.pdf?sfvrsn=4 ; 41R-08 as filed with the Muskrat Falls inquiry, https://www.muskratfallsinquiry.ca/files/P-00903.pdf (accessed 9 Nov 2026) | HALFKEPT, INFLATION_TWD | NICHE | The Taiwan dollar and Taiwan cost growth are exactly the "monetary" risks cost engineers price on their own lines; the IPS names the Taiwan dollar separately, which matches | Contents pages only for 58R-10 and 40R-08 | VERIFIED (contents PDFs; 41R-08 text in the inquiry exhibit) | yes, partly: same as row 6 | This run: AACE contents PDFs, inquiry exhibit |
| 8 | The UK Treasury's optimism-bias table (capital cost, upper / lower bound): Standard Buildings 24% / 2%; Non-standard Buildings 51% / 4%; Standard Civil Engineering 44% / 3%; Non-standard Civil Engineering 66% / 6%; Equipment/Development 200% / 10%; Outsourcing 41% / 0%. Works duration: Standard Buildings 4% / 1%, Non-standard 39% / 2%. Worked example: £100m + 51% = £151m | HM Treasury, The Green Book: Supplementary Green Book Guidance, Optimism Bias, Table 1, https://assets.publishing.service.gov.uk/media/5a74dae740f0b65f61322c72/Optimism_bias.pdf (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY | KNOWN | Primary source and the full table behind store H7-086's "+51% via NWSSP". A fifth is near the standard-building upper bound (24%) and below half the non-standard one (51%) | UK public projects, mostly large | VERIFIED (full text, Table 1) | no | This run: gov.uk PDF |
| 9 | The upper bounds "relate to the average historic optimism bias found at the outline business case stage ... Higher optimism bias adjustments may therefore be required at an earlier stage" (para 3.3). Non-standard = "innovative", "mostly unique characteristics" or high complexity (3.6); standard = "most accommodation projects e.g. offices, living accommodation"; non-standard includes "other unique buildings or refurbishment projects" (3.10). "High optimism bias may be acceptable for a strategic outline business case but would not normally be acceptable at the full business case stage" (3.19) | HM Treasury, as row 8, paras 3.3, 3.6, 3.10, 3.19 (accessed 9 Nov 2026) | HALFKEPT, MOVE2031 | KNOWN | In 2031 Laura is at the strategic stage, before any business case; a new small residency is "living accommodation" (standard), a converted old building is "refurbishment" (non-standard) | The guidance expects the uplift to fall as risks are managed, which a founder can do between 2031 and the tender | VERIFIED (full text) | no | This run: gov.uk PDF |
| 10 | Size does not cure optimism: "There is no correlation between project size and optimism bias, however there is a strong relationship between project size and the number of project risks"; "high optimism bias may be acceptable for a strategic outline business case and very small projects (projects below £1 m in value)"; early effort managing risks "tends to result in low optimism bias" | Mott MacDonald (July 2002), Review of Large Public Procurement in the UK, for HM Treasury (50 projects), as filed with the Victorian Parliament, https://www.parliament.vic.gov.au/49e91a/globalassets/sections-shared/get-involved/historical-inquiries/inquiry-into-budget-estimates-2010-11/mott_mcdonald_flyvberg_blake_dawson_waldron_studies.pdf (accessed 9 Nov 2026) | HALFKEPT | NICHE | A small residency does not earn a smaller percentage just by being small; the Treasury's own consultants allowed a high uplift for very small projects | Sample of large projects (over £40m); "very small" is a remark, not a measured class | VERIFIED (full PDF, excerpts read) | no | This run: Victorian Parliament PDF |
| 11 | Flyvbjerg's 2004 guidance for UK transport: uplifts at 50% / 80% confidence, roads 15% / 32%, rail 40% / 57%, fixed links 23% / 55%. Who should use which: "the 50% percentile should be used only in instances where investors are willing to take a high degree of risk ... The upper percentiles (80-90%) should be used when investors want a high degree of certainty that cost overrun will not occur, for instance in stand-alone projects with no access to additional funds beyond the approved budget." Buildings appear only as Mott MacDonald's 4%-51% | Flyvbjerg and COWI for the Department for Transport (2004), Procedures for Dealing with Optimism Bias in Transport Planning, as filed with the Edinburgh Tram Inquiry, https://www.edinburghtraminquiry.org/wp-content/uploads/2017/10/CEC02084257.pdf (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY, COSPONSOR | NICHE | The test for which confidence level to use is whether the project can reach more money. The case lists co-sponsors, grants, collaborators, programme fees and "continued business income" (case l.86), so the project is not stand-alone; Laura's own pledge is | Transport, not buildings | VERIFIED (full PDF) | no | This run: inquiry PDF |
| 12 | Updated reference classes (Table 5, international): Buildings ("Stations, depots, concert halls, office buildings, museums", n=149) mean / 50% certainty (RCF50) / 80% certainty (RCF80): full business case 44% / 13% / 84%; outline 48% / 13% / 101%; strategic outline 70% / 13% / 145%. UK buildings (Table 9, n=25): 26% / 11% / 42%; 29% / 11% / 59%; 51% / 11% / 103%. "The Optimism Bias changes only in the tails." About 7 in 10 buildings overrun | Oxford Global Projects for the Department for Transport (2020 data, published May 2021), Updating the evidence behind the optimism bias uplifts for transport appraisals, https://assets.publishing.service.gov.uk/media/6093d448e90e0726f52fc54c/updating-the-evidence-behind-the-optimism-bias-uplifts-for-transport-appraisals.pdf (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY, MOVE2031 | NICHE | The median building overruns by only 11%-13%, but 80% confidence at the earliest stage needs +103% to +145%. A fifth covers the typical case and very little of the tail | Large public buildings; the earlier stages are adjusted from later data (the median is the same at all three stages) | VERIFIED (full PDF, Tables 5 and 9) | yes, partly: at Laura's stage the kept half is far below an 80% buffer; a risk to note, not a change | This run: gov.uk PDF |
| 13 | The same report: unexpected inflation adds about 4 points at P50 and 10 points at P80 (116 UK projects, nominal minus real overrun); overruns grow with duration (about 13% for 3-year projects, 20% for 5-year, 30% for 10-year); it recommends RCF50 as the low, RCF65 as the middle and RCF80 as the high contingency bound | Oxford Global Projects for DfT (2021), as row 12 (accessed 9 Nov 2026) | INFLATION_TWD, HALFKEPT | NICHE | Inflation is its own line on top of the overrun; Laura's 2031 to 2033 gap is short, but the build itself adds years | Transport and UK data; Taiwan's building costs move at their own pace (NUMBERS s8d: central 3.0%, band 1.5%-5.0%) | VERIFIED (full PDF) | no | This run: gov.uk PDF |
| 14 | England's housing agency split buildings by risk (Table 4): "Uncomplex Buildings (low risk)", "residential, schools, community buildings, GP practices, car parks, small sports centres", n=64: P50 4%, P80 32%, trimmed mean 22%. "Buildings (med risk)", including museums, offices and stadiums, 0-5 years, n=42: P50 9%, P80 69%, trimmed mean 28%. Table 1: buildings overrun 62% on average, 7 in 10 overrun, 20% "black swans" | Homes England (Feb 2024), Optimism bias and contingency at Homes England, by Oxford Global Projects, https://www.gov.uk/government/publications/optimism-bias-and-contingency-at-homes-england/optimism-bias-and-contingency-at-homes-england-accessible-version (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY | NICHE | The closest reference class by type: a small residency is a community and residential building. The middle-case kept half (18%-22%) sits at the class's trimmed mean (22%), between its P50 (4%) and P80 (32%) | Public projects in England; trimmed mean and percentiles from the same OGP database as row 12 | VERIFIED (gov.uk page, Tables 1 and 4) | no | This run: gov.uk page |
| 15 | The same report builds a budget in separate lines: base cost, then a risk allowance, then unanticipated inflation, then planned inflation (Table 3 example: base 100, risk 10%, unanticipated inflation 4%, planned inflation 5%) | Homes England (2024), as row 14 (accessed 9 Nov 2026) | INFLATION_TWD, HALFKEPT | KNOWN | Another public owner keeps risk and inflation apart; the kept half carries both | Illustrative numbers | VERIFIED (gov.uk page) | yes, partly: as row 6 | This run: gov.uk page |
| 16 | Denmark's 110 cultural buildings delivered 2000-2007 (DKK 5.8bn in all, average DKK 53m; 63 new, 47 repairs): 40% at or under the decision budget; 75% within +10%; to be 80% sure the budget holds add 13%, for 90% about 28% (Figure B). Average deviation about 6% from the decision budget and 3% from the budget at construction start. Main cause: changes the client ordered | Realdania and Byggeriets Evaluerings Center, with Bent Flyvbjerg and COWI (March 2007), Budgetafvigelser på kulturbyggerier i Danmark, https://cdn.realdania.dk/media/hsyapzvm/budgetafvigelserrapportpdf.pdf (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY | NICHE | The nearest reference class by purpose: cultural buildings, many small. A fifth sits between the 80% (+13%) and 90% (about +28%) points | The report "does not show whether budget compliance came at the expense of cuts"; Danish public projects, budgets set at the decision to build, not earlier | VERIFIED (full PDF, Danish) | no | This run: Realdania PDF |
| 17 | The same report's tails: of 20 new concert halls and museums, 5 overran by more than 25%, the largest 68%; renovations of that type averaged 69% (simple average). For 18 projects measured at tender, the expected tender price had to rise 28% to match bids, and 42% for 80% confidence (largest 64%, smallest +4%) | Realdania (2007), as row 16, delanalyse 3 and figures 26-27 (accessed 9 Nov 2026) | HALFKEPT, MOVE2031 | NICHE | The tail lives in one-off and refurbished buildings, and the earliest prices are the least reliable; a plain new residency is the safer end | Small samples (20 and 18) | VERIFIED (full PDF, Danish) | no | This run: Realdania PDF |
| 18 | Norway's state project model gives the agency a P50 steering frame and sets the cost frame at P85; the difference is a reserve held by the ministry, not the project | Ministry of Finance, Circular R-108/2025, The State Project Model, https://www.regjeringen.no/globalassets/departementene/fin/2025/statens-prosjektmodell/circular-108-25-the-state-project-model.pdf ; "Hva er KS-ordningen?", https://www.regjeringen.no/no/dokumentarkiv/regjeringen-solberg/fin/Hva-er-KS-ordningen/id2001422 (accessed 9 Nov 2026) | HALFKEPT, COSPONSOR, MOVE2031 | NICHE | The same design as "promised to no one": the builders see only the promised amount, and the owner keeps a reserve above it under its own control | A state with many projects can pool reserves; Laura has one project | VERIFIED (circular PDF and ministry page) | no (supports the IPS's structure) | This run: regjeringen.no |
| 19 | How big Norway's reserve is (Table 4-5, 180 projects): P85 minus P50 averages 14%; buildings and construction (n=137) mean 13%, median 13%, minimum 3%, maximum 28%; most projects 10%-20%. P50 is about 16% above the base estimate. The report cites a review: contingencies from about 5% in simple road and building projects to over 40% in complex early-phase projects, "Several studies report 5-15%"; Norway's road agency adds 16-20% / 10-15% / 3-7% by planning level; Danish roads 30% early, 15% at decision | NTNU Concept research programme (Sep 2026), Kostnadsestimater og usikkerhet i store statlige prosjekter: Fra grunnkalkyle til kostnadsramme, https://www.ntnu.no/documents/1261860271/1262021752/Kostnadsestimater+og+usikkerhet+i+store+statlige+prosjekter.pdf/c5b2a681-f894-474a-cae6-22846e8c2419?t=1790671026867 ; the review is Ammar et al. (2023), Alexandria Engineering Journal, abstract https://consensus.app/papers/details/7576bed8b45b53ec818040b1f297a5b6/ (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY | NICHE | A reserve of about 13% above the median is what a careful state holds for buildings at the decision to build; Laura's middle-case fifth is above that, at an earlier stage | Norwegian projects are large and have passed an outside review (KS2) before these figures are set | VERIFIED (NTNU PDF, Table 4-5); Ammar 2023 abstract only | no | This run: NTNU PDF; Consensus abstract |
| 20 | Did the Norwegian reserve work? Five studies (Table 2.1): 42%-58% of projects finished within P50 and 75%-80% within P85; average result 2.1%-6.0% over P50 and 4.4%-7.6% under P85. "Smaller projects often have a budget closer to P50 ... e.g. the uncertainty reserve set at 10 percent" | NTNU Concept, Rapport 1277 (final report), https://www.ntnu.no/documents/1261860271/1262021752/Rapport+1277_sluttrapport_endelig.pdf/a994c8c9-efd9-87f5-1dc9-782e33761aaf?t=1646918463486 ; Klakegg, State of Norwegian projects 2025, https://www.vfi.is/media/file/Concept_State-of-Norwegian-Projects-2025.pdf (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY | NICHE | A reserve set at P85 delivered about 75%-80% in practice, a little short of 85%; a reserve sized for 85% gives roughly four in five | Big state projects, after outside review | VERIFIED (Rapport 1277 PDF, Table 2.1); Klakegg slides read | no | This run: NTNU PDF, VFI slides |
| 21 | Stage matters more than anything: Norwegian roads' final cost was 53% above the estimate at their first mention in Parliament (n=15), 38% above the transport plan's (n=21) and 1% above the steering frame (n=31); costs rose "several tens of per cent" in the pre-project phase. Sweden 2004-2022: "considerable cost escalation during the planning stages", estimates at decision to build "close to final costs, on average", with a long right tail, because decisions get "locked in" early | NTNU Concept rapport 79 (2025), citing Welde (2014), https://www.ntnu.no/documents/1261860271/1262010703/Concept_79_web.pdf ; Eliasson, J. (2025), "Cost overruns of infrastructure projects: distributions, causes and remedies", Transportation Research Part A, abstract https://consensus.app/papers/details/6d3a2d72d9a95e3eaf54eff8cfee7bae/ (accessed 9 Nov 2026) | MOVE2031, HALFKEPT | NICHE | In 2031 Laura announces a range for a building that is at "first mention": the stage at which costs later grew by half | Roads, not buildings | VERIFIED (Concept 79 PDF); Eliasson abstract only | no | This run: NTNU PDF; Consensus abstract |
| 22 | Taiwan's public works manual: allowable cost variation (經費變動率) by stage, feasibility 15%-30%, comprehensive planning 10%-25%, basic design 3%-10%, detailed design 3%-5%; contingency (工程預備費) for major new projects capped at the same bands; smaller or simpler projects 8%-20% at planning and 3%-5% at design. It warns against relying only on "編列高比例之預備費" (a high-percentage contingency) | Public Construction Commission, 公共建設工程經費估算編列手冊 總則篇 (rev. 23 Feb 2018, 工程技字第10700053180), https://www.pcc.gov.tw/downloadFile?fpath=VXBsb2FkLzI5Ny9yZWxmaWxlLzc2OTMvNDQxNi85ZTYzNTk3NS1kZTVkLTQ1MzMtYjE1MC1iOGMxZWI5NTg4N2QucGRm&sname=2.%E5%85%AC%E5%85%B1%E5%BB%BA%E8%A8%AD%E5%B7%A5%E7%A8%8B%E7%B6%93%E8%B2%BB%E4%BC%B0%E7%AE%97%E7%B7%A8%E5%88%97%E6%89%8B%E5%86%8A%E7%B8%BD%E5%89%87%E7%AF%87107%E5%B9%B42%E6%9C%88%E4%BF%AE%E6%AD%A3%E7%89%88.pdf ; index https://www.pcc.gov.tw/content/index?eid=5202&type=C (accessed 9 Nov 2026) | HALFKEPT, INFLATION_TWD, MOVE2031 | NICHE | Taiwan's own rule for how far an early estimate may move: at feasibility, up to 30%. Weiwuying's +28.64% (Q9 row 26) sits inside that band | Public works; a 2023 revision exists and was not read | VERIFIED (2018 PDF, Chinese) | no | This run: PCC PDF |
| 23 | The same manual prices escalation (物價調整費) separately, from the average of the construction cost index (10 years in 2018; 3-10 years in the 2023 revision), and lists causes of cost change including exchange rates (總.4.10 匯率之變動), special landmark designs (總.4.13) and fundraising (總.4.14 經費籌措) | PCC 總則篇 (2018), as row 22, chapter 4 (accessed 9 Nov 2026) | INFLATION_TWD, COSPONSOR | NICHE | Taiwan's government names the same three risks the IPS names (overruns, the exchange rate, money falling short) and keeps escalation off the contingency line | 2023 revision seen only on the index page | VERIFIED (2018 PDF, Chinese) | no (supports the IPS naming the Taiwan dollar) | This run: PCC PDF |
| 24 | Taiwan's building volume: contingency at the planning stage 0-10% for smaller or simpler buildings, up to 15% for larger or complex ones; basic design 0-5%, complex up to 10%; worked example uses 5%; indirect costs 10%-15%; offshore islands +30%. Scope: offices, classrooms, housing, dormitories | PCC, 公共建設工程經費估算編列手冊 建築工程篇 (第十八篇, 31 Mar 2020, 工程技字第1090200309), https://www.pcc.gov.tw/downloadFile?fpath=VXBsb2FkLzI5Ny9yZWxmaWxlLzc2OTMvNDQxNi9hYWMyYTQxMy1kOGFmLTQ5ZmEtOGRiYi1mMGUzYTY5ZThkMjIucGRm&sname=4.%E5%85%AC%E5%85%B1%E5%BB%BA%E8%A8%AD%E5%B7%A5%E7%A8%8B%E7%B6%93%E8%B2%BB%E4%BC%B0%E7%AE%97%E7%B7%A8%E5%88%97%E6%89%8B%E5%86%8A%E5%BB%BA%E7%AF%89%E5%B7%A5%E7%A8%8B%E7%AF%87109%E5%B9%B43%E6%9C%88%E4%BF%AE%E6%AD%A3%E7%89%88.pdf (accessed 9 Nov 2026) | HALFKEPT | NICHE | For a dormitory-like building in Taiwan the official planning-stage contingency is at most 10%-15%; the middle-case fifth is above it, and even the 1-in-20 low (9%-11%) is near its top | A contingency inside a public budget, on top of separately priced escalation; it is not a reserve above a promise | VERIFIED (2020 PDF, Chinese) | no | This run: PCC PDF |
| 25 | The US federal buildings agency (Table 3-1): design contingency for new construction 10% at planning and development, 7.5%-10% at concept, 5%-7.5% at design development, 0% at final documents (renovation 10%, 10%-15%, 7.5%-10%, 0%); construction contingency 7% new, 10% modernisation. Scope changes "must be accommodated by approved revisions to the project funding and not through the use of construction contingency". 2007 edition: "Contingency is not to be used to avoid making an accurate assessment of expected cost" | GSA, P-120 Cost and Schedule Management Policy Requirements (PBS 1000.6B, 7 Nov 2022), https://www.wbdg.org/FFC/GSA/p120_2022.pdf and https://www.gsa.gov/directives/files?file=2023-06%2FFinal%20Directive_PBS%20Cost%20and%20Schedul%20Management.pdf ; GSA Q&A (18 Jan 2024), https://www.gsa.gov/system/files/Q%26A%20-%20Cost%20Estimating%20and%20Cost%20Management%20Principles%201-18-24.pdf (accessed 9 Nov 2026) | HALFKEPT | KNOWN | About 17% held at planning for a new federal building; the middle-case fifth is about the same | Contingency inside the budget, expected to be spent; GSA is looking at a risk-based model | VERIFIED (P-120 PDF, Table 3-1; Q&A PDF) | no | This run: WBDG and GSA PDFs |
| 26 | US states: Pennsylvania 15%-20% at programming or concept, 10%-15% at schematic, 5%-10% at design development, construction contingency typically 10%, plus an owner's contingency; Wisconsin 15% project contingency, separate from inflation; Colorado 5% of total project cost for new construction, 10% for renovation | Pennsylvania DGS, Cost Estimating Standards (2025), https://www.pa.gov/content/dam/copapwp-pagov/en/dgs/documents/design-and-construction/design/dgs%20cost%20estimating%20standards%20(2025).pdf ; Wisconsin DOA, 2025-27 Capital Budget Instructions, https://doa.wi.gov/DFDM_Documents/State-Building-Program/CapBud/2025-27%20Capital%20Budget%20Instructions.pdf ; Colorado OSA, https://osa.colorado.gov/sites/osa/files/documents/SBP-PROJ-MON-COST-MGMT.pdf (accessed 9 Nov 2026) | HALFKEPT, INFLATION_TWD | KNOWN | Public owners' early-stage allowances run from 5% to about 30% in total; a fifth is mid-range | Contingencies inside budgets; inflation priced apart (Wisconsin) | VERIFIED (three state PDFs) | no | This run: state PDFs |
| 27 | US architects and builders: design contingency 5%-10%, an example owner contingency of 6%; a research-building example where a $100m base becomes $117m with contingencies | AIA, "Managing the contingency allowance", https://www.aia.org/resource-center/managing-the-contingency-allowance ; AGC and AIA, Project Planning Guide for Owners and Project Teams, https://www.agc.org/sites/default/files/Project%20Planning%20Guide%20for%20Owners%20%26%20Project%20Teams.pdf (accessed 9 Nov 2026) | HALFKEPT | KNOWN | Practitioner rule of thumb: about 15%-17% in all | AGC figure read as a search excerpt | VERIFIED (AIA page); AGC VERIFIED via search excerpt of the PDF only | no | This run: AIA page; excerpt of AGC PDF |
| 28 | Fixed percentages are usually too small. Baccarini: "simply adding a 10% 'contingency' ... is typical"; 48 road projects held 5.24% against variations of 9.92%. Water projects (n=228) 8.46% held against 13.58% needed. Love et al.: the amount "is invariably insufficient"; overruns follow a long-tailed curve. An estimate paper calls "around 10%" a "large contingency percentage" at concept. A regression on 75 road networks suggests 59.722% | Baccarini, D. (2004), COBRA conference, https://curate.curtin.edu.au/articles/conference_contribution/Accuracy_in_estimating_project_cost_construction_contingency_-_a_statistical_analysis/31753672 ; Baccarini and Love (2014) as cited in CSCE 2017 paper, https://legacy.csce.ca/elf/apps/CONFERENCEVIEWER/conferences/2017/pdfs/CONSPEC/FinalPaper_247.pdf ; Love et al. (2015), J. Infrastructure Systems, abstract https://consensus.app/papers/details/2941fc28842e51d2ae7ff7a171f21c39/ ; Bozorgmehrnia et al. (2023), abstract https://consensus.app/papers/details/c51aa44c29555ad7b47c1ae8c0cb00ff/ ; Ammar et al. (2024), abstract https://consensus.app/papers/details/eecbe749ca375e0db757e04c77344b1c/ (accessed 9 Nov 2026) | HALFKEPT | KNOWN | The habit of "about 10%" is the thing to avoid; Laura's middle-case fifth is twice the habit | Roads and water, not buildings; abstracts only for three of five | VERIFIED (Curtin abstract page; CSCE paper); Love, Bozorgmehrnia, Ammar 2024 abstracts only | no | This run: Curtin repository, CSCE PDF, Consensus abstracts |
| 29 | The UK surveyors' standard: a percentage addition "should only be used for preparing rough and initial order cost estimates" ("often derived as a percentage ... for example, 5% of capital cost ... can be subjective"); risk allowances fall into four groups (design development, construction, employer change, employer other); reserves are released step by step ("progressive release method") | RICS, Management of risk (1st ed.), https://www.rics.org/content/dam/ricsglobal/documents/standards/management_of_risk_1st_edition_rics.pdf ; RICS NRM1 (2nd ed.), https://www.rics.org/content/dam/ricsglobal/documents/standards/nrm_1_order_of_cost_estimating_and_cost_planning_2nd_edition_rics.pdf ; RICS Cost reporting (1st ed.), https://www.rics.org/content/dam/ricsglobal/documents/standards/cost_reporting_1st_edition_rics.pdf (accessed 9 Nov 2026) | HALFKEPT, MOVE2031 | KNOWN | A rough percentage is the right tool at Laura's 2031 stage, and the profession expects it to be replaced by a list of risks as design firms up; "employer change" is a risk group of its own (as in Denmark, row 16) | Standards, not outcome data | VERIFIED (RICS PDFs) | no | This run: RICS PDFs |
| 30 | The value of waiting: "This lost option value is an opportunity cost that must be included as part of the cost of the investment ... this opportunity cost is highly sensitive to uncertainty"; uncertainty over things like "exchange rates" matters more than over interest rates; in their widget example the right to wait is worth $173 ($773 against $600); economies of scale must be large to justify giving up flexibility | Dixit, A.K. and Pindyck, R.S. (1994), Investment under Uncertainty, Princeton University Press, https://press.princeton.edu/books/hardcover/9780691034102/investment-under-uncertainty ; chapters 1-2 PDF, https://afpc.tamu.edu/courses/643/2018/reading/Dixit-Pindyck-1994-Ch1-2.pdf (accessed 9 Nov 2026) | HALFKEPT, INFLATION_TWD | TEXTBOOK | Primary source the store lacked (H3-052 had none). Promising everything in 2031 would give up an option whose value rises with exactly the uncertainties Laura faces: building cost and the exchange rate | Their projects are irreversible firm investments; Laura's gift is a pledge. The value of the option is not the right size of the reserve | VERIFIED (chapters 1-2 PDF; publisher page) | no | This run: Princeton page, Texas A&M course PDF |
| 31 | Build flexibility in and use it only if needed: "flexibility in design routinely improves performance by 25 percent or more"; the parking garage that "starts small and expands if and when needed"; a case study "shows how designers of infrastructure systems can evaluate flexibility in engineering systems in fairly simple ways". Trigeorgis's book is the standard reference on real options | de Neufville and Scholtes (2011), Flexibility in Engineering Design, MIT Press, https://direct.mit.edu/books/monograph/2955/Flexibility-in-Engineering-Design ; MIT News Q&A with Richard de Neufville (24 Feb 2012), https://news.mit.edu/2012/qa-with-richard-de-neufville ; de Neufville, Scholtes and Wang (2006), "Real options by spreadsheet: parking garage case example", J. Infrastructure Systems 12(2), https://ascelibrary.org/doi/abs/10.1061/(ASCE)1076-0342(2006)12:2(107) ; Trigeorgis (1996), Real Options, MIT Press, https://mitpress.mit.edu/9780262201025/real-options (accessed 9 Nov 2026) | HALFKEPT, MOVE2031 | KNOWN | The kept half lets Laura's building start at the size the promised money buys and grow if the kept half is still there; this is a design choice for the residency, not only for the portfolio | "25 percent or more" is the author's own claim in an interview; the garage numbers were not read | VERIFIED (MIT News page; ASCE abstract page; MIT Press pages); book text not read | no | This run: MIT News, ASCE, MIT Press pages |
| 32 | Adding the three named uses. One overrun reserve at an early stage, 13%-17% (Norway buildings, Denmark 80%, GSA, rows 16, 19, 25); plus Taiwan cost growth over 2031-33, 6.1% at 3% a year (10.25% at 5%; NUMBERS s8d band); plus a Taiwan dollar back at its ten-year strongest, 32.768 / 27.52 - 1 = 19.1% (NUMBERS s8d: $21,000-$26,000). Added, about 38%-46% of the contribution; compounded, about 43%-54%. Without the currency stress, 19%-27% | NUMBERS.md s8d and s4; rows 16, 19, 25 (accessed 9 Nov 2026) | HALFKEPT, INFLATION_TWD | NICHE | The middle-case fifth covers about one of the three named uses at a time, or overruns and two years of cost growth if the Taiwan dollar holds | The three may not peak together; a co-sponsor shortfall cannot be put in percentages without a cost estimate, which the case rules out | Keel arithmetic | yes, partly: the IPS lists three uses for one pot; together they can need about twice the middle case; a risk to note | This run |
| 33 | The norms are percentages of the whole building's cost; the kept half is measured against Laura's share of it. If co-sponsors give fixed sums and Laura covers overruns alone, an overrun of x% of the whole cost is x divided by her share of the cost, as a percentage of her contribution (at a half share, a 13% overrun is 26% of her gift; at a quarter, 52%). If overruns are shared in proportion, it is x% | Keel arithmetic; store H4-033 (the sponsor funds "all or a capped portion" last) (accessed 9 Nov 2026) | HALFKEPT, COSPONSOR | NICHE | Whether "a fifth" is enough depends on who carries overruns, which the 2031 talks with co-sponsors decide | Her share of the cost is unknown and the case says not to estimate it (case l.164-165) | Keel arithmetic | yes, partly: if Laura is the last payer, the kept half is a smaller share of the project than of her gift; a risk to note | This run |
| 34 | The kept half is not the only unpromised money. At today's forward rates the payments overflow by about $27,990 in January 2033 money (20.7%-25.4% of the range; with the middle-case kept half, $51,976 = 38.5%-47.3%), gone if yields fall. The case also lists "continued business income" as a source for remaining facility cost. An all-Treasury plan holding back the same median amount would promise about $134k with certainty | NUMBERS.md s4 (l.155, l.170); case l.86 (accessed 9 Nov 2026) | HALFKEPT, CERTAINTY, RESERVE2033 | NICHE | Behind the kept half stand the ladder's spare money (if rates hold) and Laura's own income, like Norway's ministry reserve behind the agency's frame (row 18) | The overflow arrives with the ladder from 2033 and depends on rates; neither may be counted in the range (CANON A30, D12) | Keel arithmetic on the register | no; never count either in the range | This run: NUMBERS.md, case |

## (b) Cards: the seven strongest ideas

### Card 1. What a cost engineer would call the kept half
- **What is it?** AACE International, the cost engineers' body, grades estimates by how much design is done (Class 5,
  0-2% defined, to Class 1) and defines a contingency narrowly: it excludes scope changes, extraordinary events,
  management reserves, escalation and currency, and it "is expected to be expended". Money for discretionary purposes
  outside the defined scope is a "management reserve" (rows 3-7).
- **Did it work?** Its classes are widely used, and 41R-08 was filed as evidence in Canada's Muskrat Falls
  inquiry. For buildings at Class 5, the 80% band still runs to +30% to +50% after an even-odds contingency.
  Where owners used a flat percentage instead of these methods, contingencies came out below the overruns that
  followed (row 28).
- **How is Laura like it?** In 2031 her building is at Class 5 or 4, with almost nothing designed. The kept half is
  money outside any promise, held for the owner's choices, which matches AACE's management reserve.
- **How is she not?** She is a private founder giving a pledge, not an owner running an industrial project. The RPs
  were read only through their sample and contents pages.
- **What Caplet takes:** Call the kept half a reserve for the owner, not a contingency. Say that cost engineers
  would split it three ways (overruns, the Taiwan dollar and Taiwan prices, funding), and show the three as
  illustrations against one pot (Clash: yes, partly; a risk to note).

### Card 2. Buildings: a small median and a huge tail
- **What is it?** The reference classes behind UK guidance: Oxford Global Projects' data for the Department for
  Transport (2021) and for Homes England (2024), and HM Treasury's optimism-bias table (rows 8-15).
- **Did it work?** HM Treasury's guidance tells appraisers to apply these uplifts. The 2021 update finds the median building
  overruns by 11%-13% at every stage. 80% confidence needs +42% to +103% (UK) or +84% to +145% (international), and
  "the Optimism Bias changes only in the tails". No outcome study of the uplifts themselves was read.
- **How is Laura like it?** A small residency fits Homes England's "uncomplex buildings" (residential, community
  buildings): P50 4%, P80 32%, trimmed mean 22%. The middle-case kept half (18%-22%) sits at that trimmed mean.
- **How is she not?** The data are public, mostly large projects. Laura's 2031 stage is earlier than any business case.
  The Treasury says higher uplifts may be needed earlier, and its consultants found that small size does not reduce
  optimism (row 10).
- **What Caplet takes:** The kept half covers a typical overrun of a simple building, not a bad one. "About a fifth"
  is a middle-odds cushion; it does not offer 80% confidence.

### Card 3. Denmark's cultural buildings: the closest cousins
- **What is it?** 110 Danish cultural buildings finished 2000-2007, averaging DKK 53m, studied by Realdania with
  Flyvbjerg and COWI (rows 16-17).
- **Did it work?** Mostly: 75% finished within +10% of the decision budget. To be 80% sure, add 13%; for 90%,
  about 28%. The tail was in concert halls, museums and renovations (5 of 20 new ones over 25%, the largest 68%;
  renovations averaging 69%). The main cause was changes the client ordered. The report itself warns it cannot tell
  whether budgets were met by cutting.
- **How is Laura like it?** A cultural building for artists, small by public standards, with a founder who can
  change the brief.
- **How is she not?** The Danish budgets were set at the decision to build, after design work. Laura's 2031 figure
  comes earlier. Their prices at tender were 28% above expectations on average (18 projects).
- **What Caplet takes:** For a plain cultural building the kept half sits between the 80% and 90% points of this
  class. The biggest risk the owner controls is her own changes to the brief, which a stated rule can limit.

### Card 4. Norway: the reserve sits above the project, held by the owner
- **What is it?** Norway's state project model: the agency gets a P50 steering frame, the cost frame is P85, and the
  difference is held by the ministry (rows 18-21).
- **Did it work?** Largely. Across five studies, 75%-80% of projects finished within P85 and 42%-58% within P50
  (Table 2.1). For buildings, P85 minus P50 is 13% on average (3% to 28%; Table 4-5). Before the decision stage,
  though, Norwegian roads grew 53% from their first mention in Parliament.
- **How is Laura like it?** "Promised to no one" is the same design: co-sponsors see a promised range, and the owner
  keeps a reserve above it that she alone releases.
- **How is she not?** Norway sets P85 after an outside review of a worked-up project; Laura's range is announced at
  "first mention". A state pools reserves over many projects; she has one.
- **What Caplet takes:** The structure of the plan has a respected public model. The size (about a fifth) is above
  Norway's 13% for buildings, but Norway's 13% comes later in a project's life than 2031 does for Laura.

### Card 5. Taiwan's own rules: early estimates may move by up to 30%
- **What is it?** The Public Construction Commission's cost manual: allowable cost variation by stage (feasibility
  15%-30%, planning 10%-25%, basic design 3%-10%, detailed design 3%-5%). For buildings, planning-stage contingency
  is 0-10% for smaller or simpler ones and up to 15% for complex ones. Escalation is priced separately, and exchange
  rates and fundraising are named causes of cost change (rows 22-24).
- **Did it work?** Weiwuying ended 28.64% over budget (Q9 row 26): above the planning-stage band and just inside the
  feasibility band. The manual itself warns against covering uncertainty with "a high-percentage contingency" alone.
- **How is Laura like it?** Her building will be built and priced in Taiwan, and judged by people who know these
  rules. The manual names the same risks the IPS names: overruns, the exchange rate and money falling short.
- **How is she not?** The rules are for public works with separate escalation lines and public funding. Laura's
  facility is private, and her money arrives in US dollars. The 2023 revision of the building volume was not read.
- **What Caplet takes:** By Taiwan's own planning-stage rule for a smaller building (0-10%), the middle-case fifth is
  generous for overruns alone. The Taiwan dollar is the extra risk that Taiwanese builders do not face, which is why
  the IPS names it.

### Card 6. US public owners: about 15%-20% at the start, inside the budget
- **What is it?** GSA's P-120 (10% design contingency at planning plus 7% construction contingency), Pennsylvania
  (15%-20% at concept plus about 10%), Wisconsin (15%), Colorado (5% or 10%), and the AIA's 5%-10% (rows 25-27).
- **Did it work?** No outcome study was read. GSA says scope changes must be met by new funding, not contingency, and
  that contingency is "not to be used to avoid making an accurate assessment of expected cost". It is now looking at
  a risk-based model.
- **How is Laura like it?** US owners hold about 15%-20% at the earliest stage; the middle-case fifth matches.
- **How is she not?** Those allowances sit inside an approved budget and are meant to be spent. Laura's sits outside
  her promise, unspent unless she chooses. Escalation is priced separately (Wisconsin).
- **What Caplet takes:** A judge from US practice will find "about a fifth" familiar for overruns alone. The
  contribution is not enough for scope changes, which GSA says need new money: in Laura's case, her own decision or a
  co-sponsor's.

### Card 7. The option to wait, and its price
- **What is it?** Real options: Dixit and Pindyck (1994) show that committing now gives up the value of waiting, a
  value "highly sensitive to uncertainty"; uncertainty over prices such as exchange rates matters more to it than
  interest rates do. De Neufville
  and Scholtes (2011) argue for designs that start small and expand "if and when needed" (rows 30-31).
- **Did it work?** In engineering cases, de Neufville reports that flexibility "routinely improves performance by 25
  percent or more" (his own claim). The garage case shows the method fits in a spreadsheet.
- **How is Laura like it?** In 2031 she promises the floor and the moved half, and keeps the rest unpromised until
  the building's cost and the Taiwan dollar are clearer. A residency can also be built in stages.
- **How is she not?** The theory values the option; it does not size the reserve. Holding the option in shares makes
  its size uncertain too, smallest in bad years (row 2; Q9 row 30). The register shows the same flexibility could be
  held in Treasuries, at a certain promise of about $134k (row 34).
- **What Caplet takes:** The kept half buys time to see the real cost before spending. It belongs with a building
  that can start at the promised size and grow, so overruns become choices rather than shortfalls.

## (c) What would surprise a judge
1. **The typical building overruns by only 11%-13%, but 80% confidence at the earliest stage needs +103% to +145%.**
   The median is the same at every stage; only the tail grows ("The Optimism Bias changes only in the tails"; DfT and
   Oxford Global Projects 2021, Tables 5 and 9). A fifth covers the typical case, not the bad one (row 12).
2. **In cost engineering's own words, the kept half is not a contingency.** AACE excludes scope changes, escalation,
   currency and funding from contingency. Money held outside scope, at the owner's discretion, is a "management
   reserve" (rows 6-7).
3. **Norway runs its biggest projects the way the IPS runs Laura's gift.** Agencies get the P50 figure, and the
   ministry keeps the reserve up to P85: 13% for buildings, which held in 75%-80% of cases (rows 18-20).
4. **Taiwan's own manual expects early estimates to move by 15%-30%, and names exchange rates and fundraising as
   causes.** Weiwuying's +28.64% fits inside the feasibility band (rows 22-23).
5. **In Denmark's cultural buildings, the main cause of overruns was the client's own changes**, and 75% finished
   within +10% (row 16).
6. **Smallness does not protect a project from optimism.** The Treasury's consultants found no link between size and
   optimism bias, and allowed high uplifts for very small projects (row 10).

## (d) Gaps (what I could not verify)
- The Construction Industry Institute's owner-contingency research was not found in a readable form; AACE 42R-08
  (contingency by parametric model) was not read. AACE 56R-08, 18R-97, 40R-08 and 58R-10 were read only through
  sample or contents pages.
- No study was found of contingency or overruns for artist residencies or small private cultural buildings in
  Taiwan; Weiwuying and the Taichung theatre (Q9) are large public buildings.
- The Homes England and DfT/OGP classes are mostly public and large; the Danish class (row 16) is the only one built
  of small cultural buildings, and it is from 2000-2007.
- Flyvbjerg and Gardner's base-rate table is still read only on a secondary site (Q9-025); not re-checked tonight.
- Trigeorgis (1996) and de Neufville and Scholtes (2011): publisher pages only; the parking garage figures were not
  read. Dixit and Pindyck: chapters 1-2 only.
- RAND N-2386 and the AGC/AIA guide: search excerpts only. Love et al. (2015), Ammar et al. (2023, 2024), Bozorgmehrnia
  et al. (2023) and Eliasson (2025): abstracts only. Baccarini and Love (2014): only as cited in a 2017 CSCE paper.
- The authors of the NTNU 2026 report were not recorded; Welde (2017), "final cost 7% below budget on average", was
  seen only in a search excerpt of Concept report 51 and is left out of the table.
- The PCC's 2023 revision of the general volume (escalation over 3-10 years) was seen only on its index page; the
  2023 building volume, if any, was not read.
- No source gives a norm for the Taiwan dollar risk in a reserve; the 19.1% is the register's stress (NUMBERS s8d),
  not a market forecast.
- Who carries overruns between Laura and co-sponsors (row 33) is unknown and depends on the 2031 talks.

## Sat 14 Nov: the half, researched in support of Caplet's choice (cards Q5b to Q5e)

The IPS froze the split at half (l.15), so today's question was not "is half right?" but "what does the evidence
support saying about half?", researched fairly, with what cuts the other way kept. Four new cards; notes, not prose.

**Verdict: KEEP half as Caplet's choice, and CHANGE how it is defended.** The 9 Nov verdict above stands on size (about
a fifth is enough for one risk at middle odds, not for three at once); today adds why keeping it unpromised is sound.

1. **The numbers (card Q5b, NUMBERS 8o).** Half is the middle of a nearly one-for-one trade, not an optimum: each
   $5,000 more of stated top would cost about $5,300 of what Laura keeps, and her total barely moves (within about
   $1,100 at the median on every basis). Moving 70% would leave her flexibility alone enough for a 10% stronger Taiwan
   dollar in about half the simulated futures (93 in 100 at half): worse for l.15's named uses. Moving 30% is a smaller
   promise for a larger cushion, so preferring half over it is Caplet's judgment on a "meaningful" contribution (card
   Q32), not a model result. Never "optimal".
2. **The theory (card Q5c).** Money kept unpromised is worth something only because bad news may come after the
   promise (Bernanke, 1980, the working paper read), and all three uses are bad news that arrives after 2031 (the tender, the rate on the day,
   written pledges). A promise can be raised later but not taken back (Arrow and Fisher, 1974). A minimum with full
   freedom above it is the best simple rule when news is expected (Amador, Werning and Angeletos, 2006): the plan's own
   shape, the ten and the bottom fixed, her flexibility free. Waiting has a price, a smaller promise now, which is why
   only half is kept back (McDonald and Siegel, 1982, the working paper read).
3. **The practice (card Q5c).** Lead donors keep a later gift unannounced: one "decides later" to give again when a
   campaign falls short or overruns make the goal too low, and no one should count on it (Klein, 2001). NASA promises
   outside at 70% confidence and holds its reserve above the project. The announced "first and last" gift is a promise
   and is never copied (CANON A30).
4. **The size (card Q5d).** For small and renovated buildings, measured from an approved budget, about a fifth of the
   stated top sits above the middle overrun (about the 60th percentile) and below the 90th; Laura in 2031 is earlier
   than any approved budget, so the same money covers less. Funders cap their grants and owners pay overruns (England's
   arts lottery: about two-thirds fell on the organisations; Taiwan's venue programme: the owner raises anything over
   the approved budget), which is why the flexibility is Laura's. Small size is never a comfort: small buildings
   overrun by more.
5. **The correlation (card Q5e).** Not a hedge: in the year shares fall, building costs more often rise (-0.31 to
   -0.34), and over Laura's two-year windows the link is about nothing. The uses take turns (a slump hits giving; an
   inflationary fall hits building costs; the Taiwan dollar is unlinked, +0.09); 1973-75 hit two at once. The steady
   part of what she keeps is the money the funds pay above the stated top.

**Changed claim for the report (notes, not wording).** Half is Caplet's chosen middle of a nearly one-for-one trade
between what Laura promises and what she keeps. It keeps enough for one use at middle odds (a 10% stronger Taiwan
dollar in about 93 of 100 simulated futures; about the 60th percentile of small-building overruns from an approved
budget), not for all three at once, which the report says. It stays unpromised because a promise can be raised later
but not taken back, which is how lead donors keep their last gift.
