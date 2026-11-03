# Kai's research (round 1, H-022, Tue 3 Nov 2026)

AI DRAFT (Claude, 3 Nov 2026). (Keel is a simulated team, AI-written.)

Field: weather forecasting, "the share with no 'of what?'". Door: the 14-second shot clock (the door is fiction; the finds below are real,
fetched on 3 Nov 2026). Text under test: V54 (`keel/ips_rewrite/drafts/D34/ips_V54.txt`), P5 and P6 only. P8 not touched.
Every quote below came through the fetch tool, which returns a short model-written readout of the page, so each is
**near-verbatim via fetch tool**: the Library should re-fetch before anything is quoted onward. No model numbers, no sentence to paste.

## The finds

### Find 1. The Bureau names the amount before it shows the percentage

- **Source:** "Right as rain: How to interpret the daily rainfall forecast", Bureau of Meteorology (no named author),
  https://www.bom.gov.au/news-and-media/right-as-rain-how-to-interpret-the-daily-rainfall-forecast . Page shows "issued
  15 May 2026, updated 21 May 2026" (per the fetch readout). Date read: 3 Nov 2026.
  Backing: the same Bureau change reported as "BoM updates weather app rainfall information to improve user comprehension",
  Meteorological Technology International, https://meteorologicaltechnologyinternational.com/news/climate-measurement/bom-updates-weather-app-rainfall-information-to-improve-user-comprehension.html
  (no date or author in the readout), which says "customer feedback has shown that this information is often misinterpreted". Read 3 Nov 2026.
- **Its own words (near-verbatim via fetch tool):** "a possible range of rainfall amounts, and then the chance of receiving at
  least that amount of rain." / "The first number has a high (75%) chance of occurring, while the second number has a low
  (25%) chance of occurring." / "The forecast for Port Augusta shows a 75% chance of at least 7 mm of rain and a 25% chance
  of at least 25 mm of rain." / "many people ignore the percentage and focus on 'rain'." / "However, rainfall totals outside
  this range are still possible."
- **Mechanism:** Every percentage on the Bureau's page arrives with the thing it is a chance of ("at least 7 mm"), so the
  reader never meets a bare share. The article also names the usual misreading (people skip the percentage and see "rain")
  and says the ends of the range are not walls.
- **V54 sentence it tests:** P6 "The top adds half her stocks." (and the "half" in "The other half stays with Laura").
- **What the source explains first that our sentence skips:** the amount the number is about. The Bureau says "at least
  7 mm" before the reader can misuse "75%". Ours gives "half" and leaves out half of what: what the stocks cost, or what
  they are worth on the day she names the range.
- **Verdict:** P6 "half her stocks" is **GUESS** (words a stranger must guess: "half" of cost or of worth, and "stocks" = the fund).
  Heads-up, not a verdict: the Bureau puts a stated chance on each end of its range; Book 11 bars model numbers in an IPS
  line, so this is a note for the Writing Room, not a request.

### Find 2. The Bureau's guide fixes three things at once: place, amount, window

- **Source:** "Text Forecasts User Guide", Version 2.1, updated 24 April 2026, Bureau of Meteorology,
  https://www.bom.gov.au/catalogue/Bureau_of_Meteorology_text_forecasts_user_guide.pdf . Date read: 3 Nov 2026.
- **Its own words (near-verbatim via fetch tool):** "'Chance of any rain' or probability of precipitation refers to the
  likelihood of the selected location" / "receiving more than the minimum measurable amount of rainfall (0.2 mm) over the
  24 hours from midnight to midnight." / "The first value means the location has a 75% (high) chance of receiving at least
  that amount of rain." / "The second represents a 25% (low) chance of receiving at least that amount." / "Please note that
  these are two separate pieces of information." The BoM glossary (https://www.bom.gov.au/glossary) says the same in one
  line: "Describes the likelihood of receiving a measurable amount of rain (>0.2 mm) during the day."
- **Mechanism:** A "chance of rain" is a share of one defined thing: this place, more than a stated tiny amount, one 24-hour
  window. The guide then warns that "chance of any rain" and the amount are separate facts, because people fuse them into
  one number.
- **V54 sentences it tests:** P5 "The remainder, roughly the interest it should earn" (earned over what stretch?) and
  P5 "That is under a tenth of her money" (which total, on which day?).
- **What the source explains first that our sentence skips:** the window and the base. The Bureau states the 24 hours
  and the threshold in the definition itself; V54 states no period for the interest and no total for the tenth.
- **Verdict:** "the interest it should earn" is **GUESS** (word: "interest", a year's or all of it to late 2032? and "it").
  "under a tenth of her money" is **GUESS** with a **WRONG** branch (see table).
- **Also noticed (side facts, not the find):** (a) The Bureau's own forecast pages print the bare numbers with no help text
  (e.g. https://www.bom.gov.au/places/nsw/north-sydney/forecast/ listed "3 to 20 mm" and "90%" for Tue 3 Nov, and
  https://www.bom.gov.au/places/nsw/royalla/forecast/detailed/ shows row labels like "50% chance of more than (mm)" with no
  explanation), and explain them on another page. They can; our IPS is a form with no links (`keel/WHARTON_WORD.md` line 95: "No charts, links or citations"), so the explanation must sit inside the sentence. (b) An older wording of the same
  definition says the first value is "a 50% chance" (https://farmpoint.tas.gov.au/news/interpreting-bom-forecasts; undated;
  the fetched text does not name its publisher), while the Bureau's 2026 pages say 75%. When and why the Bureau changed it
  is **UNVERIFIED** (I did not open a dated BoM page showing the switch). The shape of the sentence did not change: the
  share still sits next to what it is a share of.

### Find 3. The classic study: the same "30%" was read three ways

- **Source:** Gigerenzer, G., Hertwig, R., van den Broek, E., Fasolo, B., & Katsikopoulos, K. V. (2005), "A 30% chance of rain
  tomorrow: how does the public understand probabilistic weather forecasts?", *Risk Analysis* 25(3), 623-629, DOI
  10.1111/j.1539-6924.2005.00608.x. Abstract records opened at https://researchonline.lse.ac.uk/id/eprint/16975 and
  https://edoc.unibas.ch/8535 . Date read: 3 Nov 2026. Only the abstract record opened, not the full paper.
- **Its own words (near-verbatim via fetch tool):** "Only in New York did a majority of them supply the standard
  meteorological interpretation." / in each European city that reading was "judged as the least appropriate" / "experts need
  to specify the reference class, that is, the class of events to which a single-event probability refers."
- **Mechanism:** Pedestrians in Amsterdam, Athens, Berlin, Milan and New York mostly read "30%" as rain "30% of the time", or
  "in 30% of the area", not the intended "rain on about 3 of 10 days like this one". The authors' fix is to say what the
  share is a share of, because the number cannot say it for itself. Exact percentages per reading: not on the abstract
  pages, so **UNVERIFIED**; I do not quote any.
- **V54 sentences it tests:** P5 "under a tenth of her money" and P6 "half her stocks" (both single numbers with a hidden
  reference class).
- **What the source explains first that our sentence skips:** the reference class itself: the pot and the day the share is
  taken from.
- **Verdict:** both **GUESS**. This is the study's own diagnosis in our setting: a reader who supplies the wrong
  reference class is not confused, only wrong, and does not know it.

## P5 and P6, share by share

No stranger has read these cold in my round, so every GUESS below is my prediction from the sources, not yet a stranger's
post. Round 2 must match each GUESS to a named stranger or mark it as taste.

| Sentence (V54) | A share of what | Does the text say? | Verdict |
|---|---|---|---|
| P5 "The remainder" | What is left of the 2028 deposit after finishing the ladder and buying the Treasury fund (a leftover, not a percentage) | Yes: "Her 2028 deposit first finishes... Most of the rest buys... The remainder" builds the chain in one paragraph | CLEAR |
| P5 "roughly the interest it should earn" | The interest the Treasury fund ("it") pays between the 2028 purchase and its maturity in late 2032: the whole stretch, not a year's | No. "2028" and "late 2032" sit earlier in the paragraph and are never joined to the interest. The nearest noun to "it" is "remainder" (the Commandments check flagged this too). A saver's "interest" means a year's | GUESS (word: "interest": per year or all of it? plus "it") |
| P5 "That is under a tenth of her money." | The fund, as a slice of everything she deposits: $300,000 + $150,000 = $450,000, taken when the 2028 money is placed | No. $450,000 appears nowhere in V54. "Her money" can be the 2028 deposit (no dollar figure in V54 either), the first $300,000, or everything. The repo's own V53 line "about a fifteenth" (`COMMANDMENTS_CHECK.md`, row VIII) only makes sense on the $450,000 base | GUESS (word: "her money"), with a WRONG branch: read as the 2028 deposit, a leftover of that size is far more than a tenth of it, so the sentence is false on that reading (my arithmetic, rough; Jun to confirm). On a later day it also stops being true once the stocks have grown: it is an allocation on purchase day, and the text never says so |
| P6 "The top adds half her stocks." | Half of the one world index fund's value on the day she names the range (2031) | Partly. "In 2031" opens the paragraph and "Before she names it" is next, but V54 cut "valued that day" (`D34/README.md`), so nothing says half of cost or half of worth. "Stocks" is a third name for the P5 fund ("shares", "index fund") | GUESS (words: "half": of cost or of worth that day? and "stocks") |
| P6 "The other half stays with Laura" | The other half of the same stocks, on the same day | Yes, once "that half moves into Treasuries" (the sentence before) is read: same pot, same day, the half not promised | CLEAR. Note for the Window, not tested: P8 moves part of this half into Treasuries before she names the range, so "stays" is the headline, not the end state |

## Missing steps, named and not worded (one per share)

- P5 interest: say which holding's interest it is and for how long (from the 2028 purchase to the fund's maturity), so a saver's "per year" cannot slip in.
- P5 "under a tenth": say which total the tenth is taken of (both deposits together), and that it is the split when the 2028 money is placed.
- P6 "half her stocks": say the day the half is counted and that it is the worth then, not the cost; and keep one name for the one fund.

## Pages tried and not opened

- http://www.bom.gov.au/catalogue/understanding_weather_forecasts.shtml: fetch failed (client_error); nothing read.
- https://media.bom.gov.au/social/blog/209/right-as-rain-how-to-interpret-the-daily-rainfall-forecast/ (the 2014 version, dated 20 May 2014): opened, but the page is a "This information has moved" stub with no article body. The old BoM text that gave the first value as 50% is therefore **UNVERIFIED**.
- The BoM text-forecasts PDF via curl: refused by the proxy (403); read through the fetch tool instead, so the quotes are the tool's readout, not a local copy.
- The Gigerenzer et al. full paper (Risk Analysis): not opened; only two abstract records. No per-reading percentages.
- https://www.bom.gov.au/glossary: first 100,000 of 122,157 characters read; the last 22,157 not read.
- Search results seen but not opened: weatherzone "How to interpret a rain forecast", yourlifechoices, pedestrian.tv, windy.app, climeradar, MLA eLearning, the "why youre reading forecasts wrong" syndications (only The Land's copy, https://www.theland.com.au/story/6581470/why-youre-reading-forecasts-wrong/, was opened; its readout gave the first value as "a 50 per cent chance of at least that figure" and I did not check its date or whether it quotes the Bureau directly).
- Not touched: WInS, SMApply. No personal data.
