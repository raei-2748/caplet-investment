"""D13a step 2: build the verified list of Laura Gao's own words (Phase B quotes whose speaker is, or is presented
as, Laura Gao) plus the case pull quote, as JSON and as a Markdown file.

Inputs (status labels):
- research/insight_v1/phase_B/quotes_raw.json (Phase B claims; exact text taken from here)
- research/insight_v1/phase_D/D13_mechanical_check.json (script re-fetch results; VERIFIED by script)
- research/insight_v1/phase_D/_work/D13a_contexts.json (made by D13a_laura_quotes_check.py; all 106 found verbatim)
- SOURCES and J below: judgements made by D13a on 2026-09-27 after reading every source page in full (speaker,
  piece date, context, trimming, privacy screen). They are judgements, not script output.
- research/insight_v1/phase_D/_work/D13a_head.md and D13a_tail.md (hand-written prose around the table)
Outputs: research/insight_v1/phase_D/D13a_laura_quotes_verified.json and D13a_laura_quotes_verified.md
Run from the repo root: .venv/bin/python research/insight_v1/scripts/D13a_build_outputs.py
"""
import json
from collections import Counter, OrderedDict

ACCESS = "2026-09-27"
D = "research/insight_v1/phase_D/"
VP, PU, EX = "VERIFIED-PRIMARY", "PARAPHRASE-UNVERIFIED", "EXCLUDE-PRIVACY"

# Source pages: code -> (short name, speaker check, piece date, canonical URL)
SOURCES = {
    "OA": ("Overachiever Magazine interview", "Laura: her answer in a Q&A (interviewer Zoe Kim)", "2021-03-15",
           "https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid"),
    "WM22": ("Wharton Magazine Q&A", "Laura: answer labelled 'LG:' in a Q&A by Braden Kelner", "2022-04-06",
             "https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/"),
    "PQ": ("Poets&Quants 2018 Best & Brightest profile",
           "Laura: first-person questionnaire answer (profile by Jeff Schmitt; the closing nomination is by Lee Kramer, "
           "not her)", "2018-03-30",
           "https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/"),
    "ND": ("The Nerd Daily Q&A", "Laura: her answer in a Q&A by Elise Dumpleton", "2025-03-08",
           "https://thenerddaily.com/laura-gao-kirbys-lessons-for-falling-in-love-interview/"),
    "BW": ("ABA Indies Introduce Q&A (Bookweb)", "Laura: answer labelled 'LG:' (questions by bookseller Shirley Mullin)",
           "2022-02-07", "https://www.bookweb.org/news/indies-introduce-qa-laura-gao-1627512"),
    "IN": ("Input (Inverse) feature", "Laura: direct quote marked 'she says' in a feature by Annie Graham",
           "2022-03-07", "https://www.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel"),
    "GO": ("Geeks OUT interview", "Laura: her answer in a Q&A by Michele Kirichanskaya", "2022-05-11",
           "https://www.geeksout.org/2022/05/11/interview-with-creator-laura-gao/"),
    "HP": ("The Honey POP interview", "Laura: her answer in a Q&A by Selina (The Honey POP)", "2022-06-02",
           "https://thehoneypop.com/2022/06/02/exclusive-interview-laura-gao-on-messy-roots-lgbtq-representation-and-more/"),
    "PS": ("Pulse Spikes profile", "Laura: direct quote ('she says' / 'she reflects') in a profile by Ishita Shah",
           "2021-06-18", "https://pulsespikes.org/story/laura-gao"),
    "LNM": ("Local News Matters (Bay City News) report", "Laura: direct quote marked 'says Gao' (reporter JL Odom)",
            "2026-02-12 (updated 2026-02-15)",
            "https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/"),
    "MAV": ("The Maverick Show, episode 190, transcript PDF",
            "Laura: turn labelled 'Laura Gao:' in the show's own transcript (host Matt Bowles); transcript has visible "
            "transcription errors and was not checked against the audio",
            "episode 2022-06-23; transcript PDF created 2025-10-22",
            "https://www.themaverickshow.com/wp-content/uploads/2025/10/190_Laura_Gao_Transcript.pdf"),
    "NPR20": ("NPR Goats and Soda report", "Laura: direct quote ('Gao says/said') in a report by Aubri Juhasz",
              "2020-04-04",
              "https://www.npr.org/sections/goatsandsoda/2020/04/04/823825436/the-wuhan-i-know-a-comic-about-the-city-behind-the-coronavirus-headlines"),
    "NPR22": ("NPR Goats and Soda Q&A", "Laura: her answer in a Q&A by Malaka Gharib (edited for length and clarity)",
              "2022-04-24",
              "https://www.npr.org/sections/goatsandsoda/2022/04/24/1093992912/the-pandemic-inspired-a-cartoonist-to-explore-their-wuhanese-roots-and-queer-ide"),
    "HUF": ("HuffPost report", "Laura: direct quote ('she told HuffPost') in a report by Brittany Wong",
            "2020-04-29 (page: Apr 29, 2020, 08:07 PM EDT)",
            "https://www.huffpost.com/entry/chinese-american-illustrator-life-in-wuhan_n_5ea9c739c5b63115cec2be5a"),
    "DP": ("The Daily Pennsylvanian Student Spotlight Q&A", "Laura: answer labelled 'Gao:' in the student newspaper's Q&A",
           "2016-01-28", "https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a"),
    "HEY": ("her website bio ('Hey' page)", "Laura's own site, third-person bio (self-published; quote as her website "
            "bio, not as speech)", "undated live page (accessed 2026-09-27)", "https://lauragao.com/hey/"),
    "ED": ("her website, Editorial page", "Laura's own site, first person ('I co-founded')",
           "undated live page (accessed 2026-09-27)", "https://lauragao.com/editorial"),
    "CV": ("her resume (PDF on her site)", "Laura's own resume (self-authored; claims are self-reported)",
           "PDF created 2024-10-24 (file metadata); live, accessed 2026-09-27",
           "https://lauragao.com/s/Laura-Gao-Resume.pdf"),
    "SPK": ("her Messy Roots Publicity & Speaking Guide (PDF)",
            "Laura's own promotional guide (PDF author field 'Laura Gao'; made in Canva)",
            "PDF created 2024-03-24 (file metadata)",
            "https://lauragao.com/s/Publicity-and-Speaking-Guide-Laura-Gao-e5n7.pdf"),
    "EDU": ("her Messy Roots Educators & Book Clubs Guide (PDF)",
            "Laura: guide with an author's note signed 'Laura Gao' (PDF author field 'Laura Gao')",
            "PDF created 2024-03-24 (file metadata)",
            "https://lauragao.com/s/Educators-Book-Clubs-Guide-Messy-Roots-klc2.pdf"),
    "SIG": ("The Sign.al 5-year anniversary page", "Laura: founder's note signed 'Laura Gao, Founder of The Signal' "
            "(page linked from lauragao.com/editorial)",
            "c. 2022 (ASSUMPTION: 5 years after the January 2017 launch; the page's figures run to 2022)",
            "https://signaltemp.github.io/"),
    "RH": ("her Rewriting Herstory project page", "Laura's own site, first person ('I scraped')",
           "undated (student-era project, ASSUMPTION)", "https://lauragao.com/rewriting-herstory"),
    "DM": ("her 'Evolution of Dance Music' data study", "Laura's own site, first person ('I decided to analyze')",
           "undated (accessed 2026-09-27)", "https://lauragao.com/the-evolution-of-dance-music"),
    "HH": ("'Philly Happy Hours, Deconstructed' project page",
           "her own site, but written as 'we' (co-authors not named): a group project shown on her site",
           "undated; Penn senior year per the text (c. 2017-18, ASSUMPTION)", "https://lauragao.com/philly-happy-hours"),
    "CASE": ("Official case, Client Profile p.1 pull-quote box",
             "NOT confirmed as Laura's words: set as a pull quote with a large opening quote mark, no closing mark and "
             "no speaker line; no primary source found where she says it",
             "2026-09-10 (case PDF creation date)",
             "competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt (lines 31-33; PDF p.1)"),
}

PULL_CTX = ("In the right margin beside the paragraph on The Wuhan I Know, on the page titled "
            "'MEET LAURA GAO / Storyteller, Entrepreneur, and Creative Visionary'.")
PULL_NOTE = ("Wording VERIFIED-REPO-FILE as the case's text (agrees with D13b). Attribution to Laura NOT verified: no "
             "name line (the 2021-22 case printed '— Nichole Jordan' under its client quote), and no public source "
             "found in 8 web searches and 36 pages by or about Laura (see the pull-quote finding). Cite it as the case's words "
             "(Client Profile p.1), never as something Laura said in an interview.")
MAV_NOTE = ("Verbatim only in the show's own transcript (speaker label 'Laura Gao:'). That transcript has visible "
            "transcription errors ('Yilan and Yulan', 'busing metropolis', 'coal side') and was made in October 2025 "
            "for a June 2022 episode; not checked against the audio. Phase B's 'AI-generated by Outcast AI' could not "
            "be confirmed on the PDF or the episode page.")

# id -> (source code, context line, status, notes)
J = OrderedDict()


def add(ids, src, ctx, status, notes=""):
    for i in ids.split():
        J[i] = (src, ctx, status, notes)


# ---- Overachiever Magazine, 2021-03-15 ----
add("B1b-Q11 B8b-Q19 B8a-Q08", "OA",
    "Answer to 'What pushed you to make the jump?' (from her tech job to full-time comics).", VP,
    "The same answer calls the move 'not an easy thing' and admits imposter syndrome, so it is a considered leap. It is "
    "about a career leap, not about investment risk: do not turn it into a portfolio weight.")
add("B8a-Q09", "OA", "Opening of the same answer: friends call it a big jump; 'In college, I jumped majors almost every "
    "semester.'", VP, "About switching careers and majors.")
add("B8b-Q20", "OA", "Same answer: how she hopes to look back on her life at 80, in contrast to 'I did this one thing "
    "and excelled at it for 50 years'.", VP, "Career and life outlook; no private detail. Spoken filler 'like' is in the "
    "original.")
add("B8a-Q10", "OA", "Same passage as B8b-Q20.", VP,
    "Ends before 'and have so much fun with them'; meaning kept. Prefer the full version (B8b-Q20).")
add("B8b-Q18 B8a-Q07", "OA", "Same answer on leaving her tech job to be self-employed.", VP,
    "Her own words that self-employment means 'unstable income'; useful for why the 2028 deposit (advances, speaking, "
    "licensing) is uncertain. 'Health insurance' refers to job benefits, not her health.")
add("B8b-Q21", "OA", "Answer on handling attacks after 'The Wuhan I Know': why one reader's thank-you note meant more "
    "than metrics.", VP, "Sentence continues ', so seeing something tangible like that makes my whole week.'")
add("B8a-Q11", "OA", "Same passage as B8b-Q21.", VP, "First sentence only; meaning kept.")
add("B8b-Q22", "OA", "Same answer: what she told herself when rereading a reader's supportive comment.", VP,
    "Use as the purpose of her work (who it helps). The surrounding text is about online racist abuse; leave that out.")
add("B8a-Q12", "OA", "Same passage as B8b-Q22.", VP, "Shorter form of B8b-Q22; meaning kept.")
add("B8a-Q13", "OA", "Same answer: she expected abuse because her Twitter job was on the anti-abuse platform.", VP,
    "Continues ', just given what was going on at the time.' Shows she thought about the downside before publishing.")
add("B8a-Q14", "OA", "Answer to 'What's coming up for you?': she pitched her next book as a happy queer love story "
    "'just because there are barely any out there!'", VP,
    "A 'fill the gap yourself' line that matches B2b-Q07. It is about a book (her public work); cite it as a product "
    "decision, never as a reason for an investment choice.")
add("B8b-Q23", "OA", "Answer to 'Introduce yourself!'", EX,
    "Where she lived in March 2021, in an answer that also gives personal details (home life). The case already "
    "places the residency in Taiwan; no quote is needed for that.")

# ---- Wharton Magazine, 2022-04-06 ----
add("B2a-Q12", "WM22", "Answer to 'What do you personally get out of creating comics?': drawing while she worked as a "
    "product manager.", VP,
    "Her shorthand for her degree. The case says 'Statistics & Information Decisions Management'; her resume says "
    "'Statistics and Information Decisions'; P&Q 2018 lists 'Economics with a concentration in Business Analytics'. "
    "Use the case wording for the degree. The sentence before it is private; do not quote it.")
add("B2b-Q10 B8b-Q25", "WM22", "Same answer: a nightly 10-minute comic after work, kept as a 'comics diary'.", VP,
    "A small daily habit that added up to real progress.")
add("B8b-Q24", "WM22", "Answer to 'What is your favorite scene in the memoir, and why?' (the climax of Messy Roots).", EX,
    "Verbatim and hers, but its subject is her personal identity struggle as told in her memoir. It sounds close to the "
    "case pull quote, which makes it tempting; using it to describe how she makes money decisions would turn her "
    "identity into decoration. Cite the book's public theme (identity, belonging) instead.")

# ---- Poets&Quants, 2018-03-30 ----
add("B2b-Q07 B8a-Q01", "PQ", "Answer to 'What is the biggest lesson you gained from studying business?'; she goes on "
    "to say she nearly transferred out of Wharton and created The Sign.al instead.", VP,
    "Her clearest short line on her entrepreneurial method. The same idea recurs in 2021 (B8a-Q14). Student-era (2018).")
add("B8a-Q02", "PQ", "Same answer: why she stayed at Wharton and founded The Sign.al and a design seminar.", VP,
    "The sentence before it contains family material; do not quote or paraphrase it. 'The problem' is the mismatch "
    "between her interests and the expected Wharton path; her response was to build something.")
add("B2b-Q08 B8a-Q06", "PQ", "Her list of college activities in the profile.", VP,
    "First person ('I taught'), in a list she supplied. She taught financial literacy to high-school students; it says "
    "nothing about her own investing.")
add("B8a-Q03 B8b-Q40", "PQ", "Answer to 'What advice would you give to a student looking to major in a business-related "
    "field?'", VP,
    "'risk-adverse' is her spelling [sic]. It is about the vague, unstructured nature of a business major, NOT about "
    "investment risk; using it to describe her risk tolerance would trim it into a new meaning. Phase B's B8b-Q40 "
    "status (SNIPPET-UNVERIFIED) is now confirmed on the page.")
add("B8a-Q04", "PQ", "Same answer; continues 'Instead, use college as your playground to explore as many interests as "
    "you can and stay open to new opportunities.'", VP, "Career advice to students (2018).")
add("B8a-Q05", "PQ", "Answer on her proudest achievement, The Sign.al: describing the people its articles featured.", VP,
    "Describes OTHER people (Sign.al interviewees), not Laura. Never present it as a self-description.")
add("B8b-Q41", "PQ", "Answer to 'What has surprised you most about majoring in business?'", VP,
    "A joke; low value. Phase B marked it SNIPPET-UNVERIFIED because the old helper dropped this page's text; now "
    "verbatim with the current helper and read on the page.")

# ---- The Nerd Daily, 2025-03-08 ----
add("B8b-Q12 B8a-Q29", "ND", "Answer to 'Did you face any challenges whilst writing and illustrating?' about her first "
    "fiction book, Kirby's Lessons for Falling (In Love).", VP, "Shows she will throw away finished work that is wrong.")
add("B8b-Q13", "ND", "Same answer: why she scrapped her early drafts after trying 'something wildly different'.", VP,
    "Em dash as on the page.")
add("B8a-Q28", "ND", "Same answer.", VP,
    "'Gimmicks' means the high-concept fantasy premises of the dropped drafts, not anything financial.")
add("B8b-Q14", "ND", "Same answer.", VP,
    "Three words cut from a longer passage: quote B8a-Q28 instead. On its own it invites a meaning the page does not "
    "support (for example, 'she dislikes financial gimmicks').")
add("B8b-Q15", "ND", "Answer on her illustration process for Kirby's Lessons: describing the book's characters.", VP,
    "About her fictional characters, not herself. The lines just before it are personal; do not quote them.")
add("B8b-Q16 B8a-Q30", "ND", "Answer on what comes next after Kirby (March 2025).", VP,
    "A dated plan. California College of the Arts is reported to close in 2027 (D13b items B3a-Q05, B3b-Q14), so this "
    "teaching role may end; check before relying on it.")

# ---- Bookweb, 2022-02-07 ----
add("B8b-Q17 B8a-Q31", "BW", "Answer to 'Is there anything in Messy Roots that you now wish you had not included?': how "
    "to show Wuhanese Mandarin to English readers.", VP,
    "'Tradeoffs' and 'explain myself' are about language choices as a bilingual author, not about how she wants "
    "decisions explained to her.")

# ---- Input / Inverse, 2022-03-07 ----
add("B8b-Q26 B8a-Q15", "IN", "On the release of Messy Roots: her working life after leaving her tech job.", VP,
    "inputmag.com now redirects to inverse.com/input/...; the two copies are identical. The sentences around it "
    "describe her travels; do not use them.")

# ---- Geeks OUT, 2022-05-11 and The Honey POP, 2022-06-02 ----
add("B8b-Q30", "GO", "Answer to 'What advice might you have to give to other aspiring creators?', headed 'Post terrible "
    "work!'", VP, "The same sentences appear three weeks later in The Honey POP (a written answer she reused).")
add("B8b-Q31", "GO", "Same answer.", VP, "Also verbatim in The Honey POP (B8a-Q26); cite the earlier Geeks OUT piece.")
add("B8b-Q32", "GO", "Same answer.", VP,
    "The answer ends: if she had kept the comic in drafts 'trying to get it perfect', she would never have published "
    "it and gotten the book deal. Also in The Honey POP (B8a-Q27).")
add("B8a-Q25 B8b-Q33", "HP", "Answer to 'What advice would you give to young artists looking to create their own "
    "webcomic?'", VP, "Opening line of the answer; the rest repeats her Geeks OUT answer word for word.")
add("B8a-Q26", "HP", "Same answer.", VP, "Duplicate of B8b-Q31 (Geeks OUT).")
add("B8a-Q27", "HP", "Same answer.", VP, "Duplicate of B8b-Q32 (Geeks OUT).")
add("B8b-Q34", "HP", "Answer to 'What's some advice you have for young LGBTQ+ readers who are still trying to find "
    "themselves?'", EX,
    "Coming-out advice (sexuality, relationships), not her professional work. Turning it into a 'build a safe base "
    "before a big move' investment rule would use her identity as decoration.")

# ---- Pulse Spikes, 2021-06-18 ----
add("B8b-Q35 B8a-Q17", "PS", "Profile of her work: how writing and art go together for her.", VP, "")
add("B8a-Q18", "PS", "End of the profile, on her plans to keep writing and working with technology; continues 'It "
    "doesn't matter what medium I choose.'", VP, "")
add("B8a-Q19", "PS", "On her data project Rewriting Herstory (matching famous men with lesser-known women).", VP,
    "'[story]' is Pulse Spikes' insertion.")
add("B8b-Q36", "PS", "Same passage as B8a-Q19.", VP, "Keeps the page's trailing comma; drop it when quoting.")

# ---- Local News Matters, 2026-02-12 ----
add("B8b-Q37", "LNM", "On the growth of Pride in Panels, the free San Francisco queer comics festival she co-organizes "
    "(second edition, 2026).", VP, "Trailing comma is the page's punctuation before 'says Gao'; drop it when quoting.")
add("B8a-Q35", "LNM", "Same passage as B8b-Q37.", VP, "First sentence only; meaning kept.")
add("B8b-Q38", "LNM", "On the festival's new mini grants to 20 comic creators ('says Gao about the grants').", VP,
    "The paper printed it with a leading ellipsis ('…Our No. 1 priority'), so the paper already cut words before it; "
    "keep the ellipsis to be exact. Trailing comma is page punctuation.")
add("B8b-Q39 B8a-Q36", "LNM", "Same passage: the mini grants.", VP, "'We' means the festival organizers.")

# ---- The Maverick Show transcript ----
add("B8a-Q20", "MAV", "Travel podcast: answer on how Taiwan was for her, including where she lived.", EX,
    "About where she has lived and likes to travel (home life). Use the case for the Taiwan link. " + MAV_NOTE)
add("B8a-Q21", "MAV", "Lightning round, 'top three favorite travel destinations': recommending Yilan, Taiwan "
    "(monasteries, art residencies, tea farms).", PU,
    MAV_NOTE + " A travel tip, not a statement of plans: do not infer a site or model for her residency from it.")
add("B8a-Q22", "MAV", "Answer to 'what is one travel hack?': where she makes local friends when travelling alone.", EX,
    "A personal travel habit, not her professional work. " + MAV_NOTE)
add("B8a-Q23", "MAV", "Answer to 'What impact do you think all of that travel has had on you?'", EX,
    "Personal lifestyle (home life). Tempting as a clue to her attitude to money, but do not use it to set risk levels. "
    + MAV_NOTE)
add("B8a-Q24", "MAV", "On her future agent emailing her after the 2020 NPR interview, which led to the two-book "
    "HarperCollins deal.", PU,
    MAV_NOTE + " For a quotable line on the career leap, use the Overachiever answer (B8b-Q18, B1b-Q11).")

# ---- NPR 2020, NPR 2022, HuffPost 2020, Daily Pennsylvanian 2016 ----
add("B8a-Q32", "NPR20", "On deciding in March 2020 to share 'The Wuhan I Know'.", VP,
    "The quote continues: 'But I got all kinds of responses that really warmed my heart.'")
add("B8a-Q33", "NPR20", "On how people knew Wuhan only through the virus headlines.", VP,
    "Continues: 'About the virus and about the wet markets that people always want to bash on and point fingers at.'")
add("B3b-Q09", "NPR22", "Answer to a question about her family members and the book.", EX,
    "The question was about her family, and the sentence continues with a clause about them. Phase B's context "
    "('whether Messy Roots reached China') trimmed it into a new meaning. If the market fact matters (no Mandarin "
    "edition as of April 2022), state it in your own words as a fact about the book, without quoting her.")
add("B8a-Q34", "HUF", "On media coverage of Wuhan early in the pandemic.", VP,
    "Phase B dated it 2020-04-30 (the UTC date); the page shows Apr 29, 2020, 08:07 PM EDT.")
add("B8a-Q37", "DP", "Answer to 'What are your long-term and short-term goals?' for Draw Street Journal, her "
    "laptop-decal business, in its first week.", VP,
    "Her own rhetorical question; she answers it with a plan (marketing, a new design every month). Phase B's link to "
    "the case's 'small business' is plausible but an ASSUMPTION: the case does not name the business.")

# ---- Her own site and documents ----
add("B8b-Q02", "HEY", "First sentence.", VP,
    "Third-person bio on her own site. It names a private person (a teacher): if used, cut the parenthetical with an "
    "ellipsis, or use her first-person version from The Nerd Daily (2025-03-08): 'living proof that doodling on your "
    "Geometry homework can indeed get you somewhere in life!' (verified 2026-09-27). Low value for investment writing.")
add("B8b-Q03", "HEY", "Second paragraph.", VP,
    "Her bio uses they/their; her site says she uses she/her and they/them (the case uses she/her). Cite as the theme "
    "of her public work only, never as a reason for an investment choice.")
add("B9b-Q14", "HEY", "The line on her teaching role.", VP,
    "Present tense on a live page; CCA is reported to close in 2027 (D13b items), so check before relying on it.")
add("B8b-Q09", "ED", "Describing The Sign.al, 'An \u201cAnti-Culture Culture Club\u201d I co-founded "
    "at the University of Pennsylvania'.", VP, "'Our' means The Sign.al club.")
add("B8b-Q10", "SIG", "Her founder's note: how the club began as alumni interviews.", VP, "'We' means she and her co-founders (named on the page; not recorded here).")
add("B8b-Q11", "SIG", "Last sentence of her founder's note.", VP,
    "She handed the venture to a team that kept it running.")
add("B3a-Q02 B3b-Q03", "CV", "LG Studios entry: her HarperCollins graphic novels.", VP,
    "Her own claim on her own resume (the line continues ', and featured on NPR and New York Times'); verified as her "
    "words, not independently. Her Wharton Magazine answer (2022) also mentions the Indie Bestseller List.")
add("B3a-Q03", "CV", "Same entry.", VP,
    "Self-reported. Her site bio says 'A Harvey and Goodreads Choice Award honoree'; her speaking guide says "
    "'finalist'. Say finalist, not winner.")
add("B3b-Q04", "CV", "LG Studios (her freelance studio, 2020 to present): first client listed.", VP,
    "A line break follows 'Clients include:' in the PDF; identical once whitespace is collapsed.")
add("B9b-Q06", "CV", "Her description of the client Retainit.", VP, "Fragment of B3b-Q04.")
add("B9b-Q05", "CV", "LG Studios entry, under the client Retainit.", VP,
    "MVP = minimum viable product (a first working version). Self-reported.")
add("B9b-Q04", "CV", "LG Studios client M3 (My Mask Movement), 3D-printed medical masks.", VP,
    "Quote as written ('National Institute of Health'; the agency is the National Institutes of Health).")
add("B9b-Q01", "CV", "Twitter Product Manager entry, 2018-2020.", VP,
    "DAU = daily active users. Self-reported; the line continues with examples (Breaking News updates, moderation "
    "tools).")
add("B9b-Q07", "CV", "Her Twitter teams ('Abuse & Safety (2019-2020), Growth ML (2018-2019)').", VP,
    "ML = machine learning.")
add("B9b-Q03", "CV", "Amazon Data Analyst entry, 2017 (Recommended Ads).", VP, "Self-reported.")
add("B9b-Q02", "CV", "Skills section.", VP, "A/B testing = trying two versions with real users to see which works "
    "better.")
add("B9b-Q08", "CV", "Skills section.", VP, "A professional skill as listed; relevant only as a working language.")
add("B3a-Q04", "SPK", "Booking panel ('Email to book').", VP,
    "Her own promotional document. No fee amounts are published, so speaking income cannot be sized from it.")
add("B8b-Q05 B8a-Q38", "SPK", "Booking panel.", VP, "Second sentence of B3a-Q04.")
add("B8b-Q04", "SPK", "'Popular topics and Q&A' page, under the talk 'Taking the Leap to Pursue Art "
    "Full-Time from a Traditional Tech Job'.", VP,
    "A sample audience question she lists, NOT a statement by her. Write 'her speaking guide lists the question ...'. "
    "It shows she frames her own story as leaving 'a secure job'.")
add("B8b-Q06", "SPK", "Offer to schools, libraries and bookstores.", VP, "Promotional copy.")
add("B8b-Q07", "EDU", "Her signed author's note ('Teaching graphic novels'): what she asks educators who doubt "
    "graphic novels.", VP,
    "Phase B's date 'c.2022' is too early: the PDF was created 2024-03-24 and its bio says Kirby 'will be released in "
    "2025'. A both-and habit of mind; do not stretch it into an asset-allocation claim.")
add("B3b-Q13", "EDU", "Same author's note: the activities she created for the discussion guide.", VP,
    "Fragment of 'Many of the activities I've created in the Discussion Guide below exercise students' creativity in "
    "less daunting ways than traditional essay writing.' Meaning kept.")
add("B8b-Q08", "EDU", "Discussion exercise for Chapter 10 ('Home is where the art is').", VP,
    "A writing prompt for students, not a statement about her own planning.")
add("B9b-Q09", "RH", "Text-analysis project matching famous men with women in their field.",
    VP, "The square brackets are hers. Her results table grades each match Good, Unsure or Bad: she labels her own "
    "uncertainty.")
add("B9b-Q10", "DM", "Method section.", VP, "")
add("B9b-Q11", "DM", "'Takeaways' section.", VP, "")
add("B9b-Q12", "DM", "Findings on what makes a song danceable.", VP,
    "About songs, not finance. Do not present it as evidence that she thinks in investment terms.")
add("B9b-Q13", "HH", "A Tableau data project on Philadelphia happy hours.", VP,
    "Written as 'we' (co-authors not named), so it is a group project shown on her site. Student-era and about bars: "
    "low value, and not a subject to feature in writing for a client.")

# ---- Case pull quote ----
add("B2a-Q13 B2b-Q11 B8b-Q01 B8a-Q39", "CASE", PULL_CTX, PU, PULL_NOTE)

# ---- New quotes found by D13a while searching for the pull quote's source ----
NEW = OrderedDict([
    ("D13a-N01", ("DP", "It\u2019s actually harder as an entrepreneur because not only are you letting yourself down, but "
                  "more importantly, you\u2019re also letting other people down \u2014 people who were your earliest "
                  "supporters and were the first to believe in you.",
                  "Answer to 'What were some major challenges you've had with Draw Street Journal?'", VP,
                  "NEW (found by D13a; not in Phase B). The only place in 36 pages by or about Laura where she uses "
                  "'believe' about other people's support. Student-era (2016). The sentences before it describe a "
                  "stressful day; do not quote them.")),
    ("D13a-N02", ("DP", "As girls, it is easy for us to put too much weight on other people\u2019s opinions. There\u2019s a "
                  "social stigma that many women aren\u2019t mentally brave or prepared enough to explore the unknown "
                  "alone. I don\u2019t think any of that matters though, if you are able to get past the hardest part: "
                  "actually launching the venture.",
                  "Answer to 'Do you have any advice for your peers who also hope to start their own company?'", VP,
                  "NEW (found by D13a). The closest verified match in her own words to the pull quote's idea: other "
                  "people's doubts matter less than launching. Three consecutive sentences, quoted whole. The gender "
                  "framing is hers; cite it as advice to new founders, not as a basis for any investment rule.")),
])


def main():
    quotes = {q["id"]: q for q in json.load(open("research/insight_v1/phase_B/quotes_raw.json"))}
    mech = {r["id"]: r["result"] for r in json.load(open(D + "D13_mechanical_check.json"))}
    ctx = json.load(open(D + "_work/D13a_contexts.json"))
    assert set(J) | set(NEW) == set(ctx), sorted(set(ctx) ^ (set(J) | set(NEW)))
    # duplicates = same normalised text and same source code
    groups = OrderedDict()
    for i, (src, _, _, _) in J.items():
        key = (src, " ".join(quotes[i]["exact_text"].split()))
        groups.setdefault(key, []).append(i)
    for key, ids in groups.items():  # identical quotes must carry one judgement (the table prints one row per group)
        assert len({J[i] for i in ids}) == 1, ids
    rows = []
    for i, (src, c, status, notes) in J.items():
        name, speaker, date, url = SOURCES[src]
        q = quotes[i]
        dups = [d for d in groups[(src, " ".join(q["exact_text"].split()))] if d != i]
        rows.append(OrderedDict([
            ("id", i), ("exact_text", q["exact_text"]), ("url", url), ("piece_date", date),
            ("context", f"{name}. {c}"), ("status", status), ("notes", notes),
            ("speaker_check", speaker), ("same_text_as", dups), ("phase_b_agent", q["agent"]),
            ("phase_b_url", q["url"]), ("phase_b_claimed_status", q["fetch_status"]),
            ("mechanical_result", mech[i]), ("d13a_recheck", "VERBATIM" if ctx[i]["found"] else "NOT_FOUND"),
            ("access_date", ACCESS), ("new_in_d13a", False)]))
    for i, (src, text, c, status, notes) in NEW.items():
        name, speaker, date, url = SOURCES[src]
        rows.append(OrderedDict([
            ("id", i), ("exact_text", text), ("url", url), ("piece_date", date), ("context", f"{name}. {c}"),
            ("status", status), ("notes", notes), ("speaker_check", speaker), ("same_text_as", []),
            ("phase_b_agent", None), ("phase_b_url", None), ("phase_b_claimed_status", None),
            ("mechanical_result", None), ("d13a_recheck", "VERBATIM" if ctx[i]["found"] else "NOT_FOUND"),
            ("access_date", ACCESS), ("new_in_d13a", True)]))
    json.dump(rows, open(D + "D13a_laura_quotes_verified.json", "w"), indent=1, ensure_ascii=False)

    # Markdown table: one row per group of identical quotes (ids joined), in the order of J, then NEW.
    def cell(s):
        return str(s).replace("|", "\\|").replace("\n", " ")
    seen, lines = set(), []
    lines.append("| id(s) | exact text | speaker check | URL | piece date | context | status | notes |")
    lines.append("|---|---|---|---|---|---|---|---|")
    by_id = {r["id"]: r for r in rows}
    for r in rows:
        if r["id"] in seen:
            continue
        ids = [r["id"]] + r["same_text_as"]
        seen.update(ids)
        link = r["url"] if r["url"].startswith("http") else r["url"]
        lines.append("| " + " = ".join(ids) + " | " + " | ".join(cell(x) for x in (
            "\u201c" + r["exact_text"] + "\u201d", r["speaker_check"], link, r["piece_date"], r["context"],
            "**" + r["status"] + "**", r["notes"])) + " |")
    open(D + "_work/D13a_table.md", "w").write("\n".join(lines) + "\n")
    head = open(D + "_work/D13a_head.md").read()
    tail = open(D + "_work/D13a_tail.md").read()
    open(D + "D13a_laura_quotes_verified.md", "w").write(head.rstrip() + "\n\n" + "\n".join(lines) + "\n\n" +
                                                      tail.lstrip())
    c_all = Counter(r["status"] for r in rows)
    c_b = Counter(r["status"] for r in rows if not r["new_in_d13a"])
    print("rows:", len(rows), "table rows:", len(lines) - 2, "| all:", dict(c_all), "| Phase B ids only:", dict(c_b))
    print("unique Phase B quote texts (same source):", len(groups))
    changed = [(r["id"], r["phase_b_claimed_status"], r["status"]) for r in rows
               if not r["new_in_d13a"] and r["phase_b_claimed_status"] != r["status"]]
    print("status changed vs Phase B claim:", len(changed), changed)
    print("sources used:", len({r["url"] for r in rows}))


if __name__ == "__main__":
    main()
