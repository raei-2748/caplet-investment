# Felix's scout notes (round 6, Mon 2 Nov 2026; Opus 5.5) (Keel is a simulated team, AI-written.)

Huddle H-015, round 1, the far scout: the caplet at its Australian sources, and the caplet a bond trader knows. Text
under test: `../../../ips_rewrite/drafts/D32/ips_V52.txt` (P2 and the last line; P5, P8 and P9 for test C; paragraphs numbered P1-P10, P10 being "Do not crush."). Window's W-07
(on `origin/claude/project-thread-apbvb2`) was read first and is not redone here: the US labels (Adderall XR, Effexor XR,
Tylenol 8 HR) and ISMP Canada are its finds. Not for submission. Any wording offered is `AI DRAFT (Claude, 2 Nov 2026)`;
Caplet rewrites in its own words. GPTZero: not yet checked.

**How "exact" works here.** Every page was read through WebFetch on Mon 2 Nov 2026. The tool hands back a small model's
extract and won't quote more than 125 characters at a time, so long sentences came back in two pieces; I asked for
them in order with nothing skipped and joined them, and say so where I did. Where two fetches of different copies
returned the same words (Panadol Osteo, below), I say that too. It's "the words came back in the fetched text", not a
byte check. The Library re-fetches every quote in round 3.

**Count.** `textcheck.py` gives V52 **496** on both counts today (the brief says 497). Nothing below changes it.

---

## Find 1. The Australian caplet: the box says caplet, the leaflet says sustained release, the system says modified release

**Sources (all read 2 Nov 2026).**
- *Panadol Osteo* Consumer Medicine Information, Haleon Australia, "This leaflet was prepared in January 2026."
  Sponsor-hosted copy: https://medsinfo.com.au/consumer-information/document/Panadol_Osteo_CMI . Same words on the
  Australian Commission on Safety and Quality in Health Care's medicine finder ("Published by MIMS March 2026"):
  https://www.safetyandquality.gov.au/medicine-finder/panadol-osteo-modified-release-caplets
- The earlier CMI (Haleon Australia, "This leaflet was prepared in December 2024.", "Published by MIMS February 2025"),
  NPS MedicineWise copy: https://www.nps.org.au/medicine-finder/panadol-osteo-modified-release-caplets
- Healthdirect Australia, *Panadol Osteo* (data: AMT and ARTG "last updated 1 October 2026"):
  https://www.healthdirect.gov.au/medicines/brand/snomed/47941000168100/panadol-osteo
- TGA, "What is modified release paracetamol?" (questions and answers on the June 2020 scheduling change; no page date):
  https://www.tga.gov.au/changes-way-modified-release-paracetamol-products-are-supplied-questions-and-answers
- WA Health, "Don't rush to crush!" (PDF, code ending "SEP'14"; no owner named on the page beyond the domain):
  https://www.health.wa.gov.au/~/media/Files/Corporate/general-documents/safety/PDF/Medication-safety-resources/Dont-rush-to-crush.pdf
- TGA product page, "DIABEX XR 750 metformin hydrochloride 750 mg extended release tablets blister pack (2023-24)",
  sponsor "Alphapharm Pty Ltd": https://tga.gov.au/node/459781 ; Healthdirect, *Diabex XR*:
  https://www.healthdirect.gov.au/medicines/brand/amt,31601000168101/diabex-xr
- *Seroquel XR* CMI, AstraZeneca Pty Ltd, "This leaflet was prepared on 10 October 2019", Healthdirect-hosted copy:
  https://media.healthdirect.org.au/medicines/GuildLink_Information/138922/CMI/apcserxr11019-5.html

**Quoted lines (exact as fetched).**
- Panadol Osteo CMI, Jan 2026 (same words from medsinfo and from safetyandquality.gov.au): "PANADOL OSTEO caplets are a
  white, to off-white, film-coated capsule-shaped tablet with flat edges." and "Do not suck, crush or chew the caplets
  because that may affect its sustained release properties."
- Panadol Osteo CMI, Dec 2024 (NPS), section 4 "How to use it": "Swallow the caplets whole with water or other fluid."
  "Do not crush or chew the caplets." Its product information, section 4.2: "The caplets must not be crushed." and
  "Panadol Osteo is a unique bi-layer tablet incorporating an immediate release and a sustained release dose of
  paracetamol." The word "modified" does not appear in the leaflet.
- Healthdirect: "Panadol Osteo 665 mg modified release tablet, 96, blister pack"; component line "Tablet, modified release".
- TGA: "Modified release paracetamol (sometimes labelled as sustained release, slow release or extend release)" [the
  sentence goes on: it has 665 mg a tablet against 500 mg; "extend release" came back the same in two fetches, so it is
  the page's own typo]; "In modified release formulations, paracetamol is released into the body more slowly" [then: an
  8-hourly regimen against 4-6-hourly]; the page also lists "PANADOL OSTEO caplets, 665 mg, 96 pack".
- WA Health table, under "Slow release medicines must never be crushed.": "XR" | "Extended release" | "Diabex XR
  (metformin)"; "MR" | "Modified release" | "Diamicron MR (gliclazide)". Also: "Crushing can increase the risk of drug
  toxicity." and "For more information check SHPA Australian's Don't Rush to Crush book or the 'Crush' tab on eMIMS."
- Healthdirect, Diabex XR: "Diabex XR 1 g modified release tablet, 10, blister pack" (pack list) against the TGA's
  "extended release tablets" for the same brand.
- Seroquel XR CMI: "Swallow your SEROQUEL XR tablets whole with a full glass of water." "Do not split, chew or crush the
  tablets." "If you split, chew or crush the tablets they will not work properly."

**Mechanism.** In Australia the caplet you can actually buy with "do not crush" on its leaflet is Panadol Osteo, and the
leaflet calls it a caplet and its timing "sustained release"; the national terminology files the same thing as a
"modified release tablet", and the TGA uses "modified release" as the family name with "extended release" as one of
the labels inside it. The letters XR still expand to "extended release" on a WA Health crushing poster and on a TGA
product title, so a Sydney pharmacist reads XR the way an American one does, even if she'd call the class "modified".

**What it touches in V52.** P2, "To a pharmacist, XR means extended release" (holds here) and "a caplet that delivers its
dose on schedule, labelled do not crush" (an Australian caplet, labelled in those words).

**Where it breaks.** (1) The Australian caplet isn't called XR. Panadol Osteo has no suffix; the do-not-crush caplet and
the XR suffix meet on a US shelf (Tylenol 8 HR, Window W-07), not on ours. V52 never says the caplet is Australian, so
nothing is false. (2) The leaflet is softer than V52: "may affect its sustained release properties", not "the schedule
is gone". (3) The class name differs by country, and if Caplet ever wrote "modified release" it would be the more
Australian word and the less useful one, because it loses the X.

## Find 2. The harm, in an Australian journal: shorter, and all at once

**Source.** Selina Taylor and Beverley Glass, "Altering dosage forms for older adults", *Australian Prescriber* 2018;41:191-3,
published 3 Dec 2018, DOI 10.18773/austprescr.2018.063,
https://australianprescriber.tg.org.au/articles/altering-dosage-forms-for-older-adults.html (read 2 Nov 2026).

**Quoted lines (exact as fetched; the first two came back in two pieces each, joined here).**
- "Controlled-release, slow-release and extended-release products are specifically designed to deliver the drug over a
  prolonged period of time."
- "If a controlled-release formulation is crushed, the duration of the drug's activity is reduced and the entire
  quantity of the drug may be immediately released resulting in toxicity."
- Table, "Examples of drugs unsuitable for dosage-form modification and suitable alternatives", columns "Drug" | "Suitable
  alternative": "Paracetamol 665 mg controlled-release film-coated tablets" | "Paracetamol 500 mg tablets (plain or
  dispersible form)".
- Why people crush: "As many as one in five older patients has difficulty swallowing and may have problems taking
  tablets and capsules."
- "The Society of Hospital Pharmacists of Australia has produced the Australian Don't Rush to Crush Handbook" [the
  sentence goes on: to help with dosage-form changes]. The handbook itself was not read (Advanced Pharmacy Australia,
  the renamed SHPA, sells it: https://adpha.au/publications-resources/drtc); what it says is UNVERIFIED.

**Mechanism.** Crushing does two separate things: the drug stops lasting as long, and the whole amount can arrive at once,
which is where the toxicity comes from. The people who crush are usually helping someone who can't swallow, and the
journal's answer isn't "don't help", it's a second form of the same medicine that is safe to break.

**What it touches in V52.** P2's "Crush it and the schedule is gone" names the first harm and leaves out the second. That
is the right half: selling a rung before it matures (to pay for the building, say) leaves a January without its own
bond; it doesn't poison anyone. The last line, "Do not crush.", borrows P2's harm. And P6 already has the "suitable
alternative": the half that "stays with Laura, liquid any day, as her flexibility, in case the building costs more in
Taiwan dollars". That's the form you may break, so you leave alone the one you mustn't.

**Where it breaks.** (1) The journal's main danger is toxicity, too much at once. That doesn't carry over, and V52 is
right not to say it (the Window's "the whole dose arrives at once" already lost on this, W-07). (2) A rung sold early
pays the market's price that day, not its face value, so the money isn't "the entire quantity" either. (3) The article
is about frail older patients and their carers; Laura is neither, so only the mechanism travels, never the people.

## Find 3. The bond trader's caplet: real, an option, and pointing the other way

**Sources (read 2 Nov 2026).**
- Professor Carpenter, *Debt Instruments and Markets*, NYU Stern lecture slides "Caps and Floors" (no date; readings cited:
  Veronesi pp. 387-392, Tuckman pp. 413-416): https://pages.stern.nyu.edu/~jcarpen0/courses/b403333/18capfloor.pdf
- Andrew Lesniewski, *Interest Rate and Credit Models*, Lecture 5 "Caps, Floors, and Swaptions", Baruch College MFE,
  Spring 2019: https://mfe.baruch.cuny.edu/wp-content/uploads/2019/12/IRC_Lecture5_2019.pdf
- HM Revenue & Customs, Corporate Finance Manual, "CFM13340 - Understanding corporate finance: derivatives: interest
  rate caps and floors" (published 16 Apr 2016, updated 5 Aug 2026):
  https://www.gov.uk/hmrc-internal-manuals/corporate-finance-manual/cfm13340
- Wikipedia, "Interest rate cap and floor" (tertiary; used only for the parity line):
  https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor
- Cara Scatizzi, "Offbeat Offerings: Treasury STRIPS", AAII Journal, May 2008:
  https://www.aaii.com/journal/article/offbeat-offerings-treasury-strips
- Wharton's ban, filed: `../../../WHARTON_WORD.md` s5, "Not permitted: ... derivatives (options, futures, swaps),
  individual TIPS, individual STRIPS, anything else."

**Quoted lines (exact as fetched; HMRC's floor sentence and Carpenter's floor sentence came back in two pieces each).**
- Carpenter: "Each caplet is a kind of call on the 0.5-year rate set 0.5-years before the payment date." and "Each
  floorlet is a kind of put on the 0.5-year rate set 0.5-years before the payment date." and "A floor provides a
  guarantee to the owner of a floating note that the coupon payment each period will be no less than a certain floor
  rate or strike rate."
- Lesniewski: "Caps and floors are baskets of European calls (called caplets) and puts (called floorlets) on LIBOR
  forward rates."
- HMRC: "A cap consists of a series, or strip, of cash-settled options which can be exercised sequentially on set
  dates." and "An interest rate floor is a similar option product which allows an investor to hedge a deposit by being
  guaranteed a minimum rate of interest." and "A premium is payable."
- Wikipedia: "if the fixed swap rate is equal to the strike of the caps and floors, then we have the following put–call
  parity" ... "Cap-Floor = Swap."
- AAII: "Zero-coupon bonds do not have reinvestment rate risk."

**Mechanism.** In fixed income a caplet is one period of an interest-rate cap: an option that pays when a floating rate
ends up above a strike, bought for a premium, and worth nothing if the rate stays below. Its mirror, the floorlet, pays
when rates fall below the strike, which is exactly "guaranteed a minimum rate of interest" on money you have to
reinvest.

**What it touches in V52, and the verdict on the name.**
- *Is anything false under the trader's reading?* No. P2 tells the reader which caplet before any finance word appears,
  and no line says Laura holds an option. Under Wharton's ban (s5) the plan holds none.
- *The co-occurrence a rates judge might smile at.* V52 says "Caplet", then "floor" four times (P5, P6, P7, P9), then
  "option" (P5). In rates those are a cap, a floor and the thing both are. V52's "floor" is defined in plain words
  ("Treasuries maturing in late 2032. That is her floor."), so nobody is misled. P5's "an option, which expires
  worthless if the market stands still" is also, word for word, how a caplet ends when rates sit below its strike;
  harmless, because the IPS is criticising a bank's option, not owning one.
- *The direction.* `../../../ips_rewrite/ideation/rung3_opus_pharmacology.md` s3 already said it: a caplet pays when rates
  rise; V52's stated weak point (P8: "If yields fall and stay low, that interest earns less, and the ladder falls short")
  is a floorlet's job. Checked against two lecture sources and a government manual today. It holds.
- *One reference further (new).* Cap minus floor at the same strike is a swap. So the coupons V52 reinvests, measured
  against the yields the ladder was priced on, have the same shape as holding the caplets and having sold the
  floorlets: better off if yields rise, worse off if they fall. The caplet in her name is the half of that bet that
  helps her; the half that hurts is the floorlet. Two permitted-looking fixes are both banned: the floor itself (an
  option, s5) and the zero-coupon STRIPS bond, which has no coupons to reinvest (AAII). That's why the weak point exists
  at all, and why P8 covers it with money set aside instead of an instrument.
- *Where it breaks.* (1) Laura owns no option: no premium, no strike, no expiry. Her exposure is a straight line, and
  the caplet-plus-floorlet split is an identity, not a holding. (2) Only the reinvested coupons carry it; a rung held to
  maturity pays its face whatever yields do (V52 P3). (3) A caplet's rate is a short floating rate reset each period;
  Laura's coupons go into bonds to fixed dates, so the sign matches and the instrument doesn't. (4) HMRC's "series, or
  strip ... exercised sequentially on set dates" rhymes with ten rungs on ten dates, but "strip" is the banned word's
  root: keep it out of anything Caplet submits. (5) The rung3 file's two "where the pun misfires" points (a caplet caps
  a rate, our top caps a gift; compliance optics) still stand.

**Verdict on the name: a harmless pun in the IPS; a small gift for the Final Report; not a liability.** The IPS should
spend nothing on it. A disclaimer such as rung3's L1, "Despite the name, there are no caplets here: the floor is a
Treasury, the cap a promise." costs 17 words (496 -> 513, over the 500 limit) and invites the reading it denies. For the
Final Report or a judge's question only, one candidate:

> AI DRAFT (Claude, 2 Nov 2026), Final Report only: "Our one open risk, coupons reinvested at lower yields, is what an
> interest-rate floor insures and what a zero-coupon STRIPS bond never carries. Wharton bans both, so we price the gap
> before Laura names her range and set stocks aside to cover it." (45 words strict; checked against V52 P8 and
> WHARTON_WORD s5.)

---

## Verdicts (V52)

| | Line | Verdict | Why (source) | Plainest true sentence, cost |
|---|---|---|---|---|
| (i) | "To a pharmacist, XR means extended release" | **TRUE** | WA Health: "XR" = "Extended release"; TGA title "DIABEX XR 750 ... extended release tablets". In Australia the family is "modified release" (TGA, Healthdirect), but the letters still read "extended" | Keep; 0 |
| (ii) | "a caplet that delivers its dose on schedule, labelled do not crush" | **TRUE** | Panadol Osteo CMI: "caplets"; "Do not suck, crush or chew the caplets because that may affect its sustained release properties"; earlier CMI "Do not crush or chew the caplets". US: Tylenol 8 HR (W-07) | Keep; 0 |
| (iii) | "Crush it and the schedule is gone" | **TRUE** | Aust Prescr: "the duration of the drug's activity is reduced and the entire quantity of the drug may be immediately released"; Seroquel XR CMI: "they will not work properly". The leaflet's "may affect" is softer; "gone" stands on the journal's "entire quantity ... immediately released", and a strong true word stays (VOICE) | Keep; 0 |
| (iv) | Closing "Do not crush." pays off the same harm | **TRUE IF** P9 keeps "paying out one bond at a time as each cheque is written" | The one act that crushes the plan, selling a rung before it matures, breaks both the schedule (P2's harm) and the order (P9's "the cheques, then the floor, then everything above it"). V52 shows the schedule side only in that first P9 sentence. Cut it for words and "Do not crush." points at a priority order, which no label speaks to | Keep "Do not crush." (3 words); 0. The explicit version, "Sell a rung early and a January loses its bond." (10 words), would take V52 to 506: not offered |

No model numbers, no "our model", no paragraph rewritten. Nothing here changes the strict count.

---

## Candidate reading slip (the Library's one for today; Felix's test and Verdict left for round 3)

| Field | Draft |
|---|---|
| Date, reader | Mon 2 Nov 2026; Felix (far scout, Opus 5.5) |
| Source | Selina Taylor and Beverley Glass, "Altering dosage forms for older adults", *Australian Prescriber* 2018;41:191-3, DOI 10.18773/austprescr.2018.063, https://australianprescriber.tg.org.au/articles/altering-dosage-forms-for-older-adults.html, read 2 Nov 2026: "If a controlled-release formulation is crushed, the duration of the drug's activity is reduced and the entire quantity of the drug may be immediately released resulting in toxicity."; table columns "Drug" / "Suitable alternative": "Paracetamol 665 mg controlled-release film-coated tablets" / "Paracetamol 500 mg tablets (plain or dispersible form)". With the caplet's own leaflet (Panadol Osteo CMI, Haleon Australia, Jan 2026, https://medsinfo.com.au/consumer-information/document/Panadol_Osteo_CMI): "Do not suck, crush or chew the caplets because that may affect its sustained release properties." |
| "This reminds me of Laura's plan because..." | The person who crushes a slow-release tablet is nearly always trying to help, and the pharmacist's answer is not "don't help" but "use this other form, the one you're allowed to break" – which is what V52 does when the building needs money: it points at Laura's liquid half, not at a rung. |
| Part for part | "designed to deliver the drug over a prolonged period of time" = the ladder, one rung falling due before each of ten Januaries (P3, P9). Crushing, done because "one in five older patients has difficulty swallowing" = selling a rung before it matures because the building needs money now (P6, "in case the building costs more in Taiwan dollars"). "the duration of the drug's activity is reduced" = the later Januaries lose their own bonds (P2, "the schedule is gone"). "the entire quantity ... may be immediately released" = the sale's cash arrives at once, at that day's market price, not the bond's face value. "resulting in toxicity" = BREAKS: early cash isn't poison; the plan's harm is a January with no bond. "Suitable alternative" (the plain 500 mg tablet for the 665 mg controlled-release one) = Laura's half, "liquid any day, as her flexibility" (P6). The 665 mg controlled-release paracetamol (Panadol Osteo, "caplets", "Do not suck, crush or chew") = the name and the last line, "Do not crush." |
| Felix's test | (round 3, after Kai) |
| Verdict | (round 3, after Kai) |

---

## Every URL fetched (all 2 Nov 2026)

1. https://www.nps.org.au/medicine-finder/panadol-osteo-modified-release-caplets (Panadol Osteo CMI + PI, Dec 2024; two fetches)
2. https://medsinfo.com.au/consumer-information/document/Panadol_Osteo_CMI (Panadol Osteo CMI, Jan 2026)
3. https://www.safetyandquality.gov.au/medicine-finder/panadol-osteo-modified-release-caplets (same CMI, MIMS Mar 2026)
4. https://www.healthdirect.gov.au/medicines/brand/snomed/47941000168100/panadol-osteo
5. https://www.tga.gov.au/changes-way-modified-release-paracetamol-products-are-supplied-questions-and-answers (two fetches)
6. https://www.health.wa.gov.au/~/media/Files/Corporate/general-documents/safety/PDF/Medication-safety-resources/Dont-rush-to-crush.pdf (two fetches)
7. https://tga.gov.au/node/459781 (Diabex XR 750 product title)
8. https://www.healthdirect.gov.au/medicines/brand/amt,31601000168101/diabex-xr
9. https://media.healthdirect.org.au/medicines/GuildLink_Information/138922/CMI/apcserxr11019-5.html (Seroquel XR CMI)
10. https://australianprescriber.tg.org.au/articles/altering-dosage-forms-for-older-adults.html (four fetches)
11. https://shpa.org.au/drtc3 (302 redirect to 12)
12. https://adpha.au/publications-resources/drtc (Don't Rush to Crush product page; no modified-release text)
13. https://anmj.org.au/revised-guide-for-safely-administering-oral-medicines/ (ANMJ, 13 Aug 2018: DRTC 3rd edition; no modified-release text)
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC6299174 (blocked by a reCAPTCHA page; nothing read)
15. https://safemedicationuse.ca/newsletter/newsletter_NotBeCrushedSplitChewed.html (ISMP Canada, 2013-07-09; re-read today: "If a slow-release tablet is crushed, split, or chewed, a large amount of the medicine may be released all at once." "This could cause serious harm.")
16. https://pages.stern.nyu.edu/~jcarpen0/courses/b403333/18capfloor.pdf
17. https://mfe.baruch.cuny.edu/wp-content/uploads/2019/12/IRC_Lecture5_2019.pdf
18. https://www.gov.uk/hmrc-internal-manuals/corporate-finance-manual/cfm13340 (two fetches)
19. https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor
20. https://www.aaii.com/journal/article/offbeat-offerings-treasury-strips

Seen in search results only, not fetched (UNVERIFIED): "Panadol Extend" 665 mg caplets in Singapore and Malaysia
(ndf.gov.sg, doctoroncall.com.my), the same caplet under another name. Not used.
