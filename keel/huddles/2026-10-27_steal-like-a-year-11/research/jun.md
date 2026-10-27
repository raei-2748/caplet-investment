# FICTION. Research note: Jun on Toyota and Project Aristotle (H-001, round 1)

> Keel is a simulated team, AI-written. Read 27 Oct 2026. Quotes are exact as returned by the fetch tool unless
> marked "paraphrase". Anything not checked at the primary source is marked UNVERIFIED. I (Jun) could not open
> Toyota's own site or Google's original 2015 write-up in full; see the Sources list for what I actually read.

## Part 1. Toyota

### What it actually is
- **Andon.** A signal any worker on the line can trigger (button, cord, or a machine's own sensor). At Toyota it is
  NOT a "stop everything" switch. Per Harada's account as relayed by Lean Blog: yellow light = "I expect a delay";
  if the team can't recover in time, "the light turned red and the line stopped." The page's own wording:
  "The line stops at a designated point only if the problem cannot be resolved within the remaining work cycle."
  The team leader is expected to come over straight away. (Lean Blog, Aug 2026.)
- **Where it came from is fuzzy.** Same page: Toyota's first andon was a call button on an engine-machining line,
  dated about 1957 by other accounts; the earliest *cord* the author found is at Ford's River Rouge plant (1931 book).
  The author says Ford influence is plausible but NOT proven. So "Toyota invented the cord" is UNVERIFIED.
- **At NUMMI (the GM-Toyota joint plant in Fremont, 1984 on).** NPR's Frank Langfitt describes "a thin nylon rope
  that hangs on hooks along the assembly line, the andon cord." Worker Earl Ferguson: "These set of cords hanging
  down, that's the andon cord. It will stop the line." (NPR transcript of This American Life, 2010.) The cord even
  plays "a surprisingly cheerful little song that workers can select" (Langfitt, same transcript).
- **5 whys.** Ask "why?" about a fault repeatedly (about five times) until you reach a cause you can fix.
  Wikipedia says the technique was "originally developed by Sakichi Toyoda" and the only line it attributes to Ohno's
  1988 book is "the basis of Toyota's scientific approach by repeating why five times." Its worked example: bolts
  cross-threaded in an engine block -> threads badly cut -> cutting tool not changed -> replacement bin empty ->
  parts rolled under the shelves -> a shelf foot rusted and failed. (Wikipedia, secondary; I did not read Ohno.)
- **Genchi genbutsu ("go and see").** Lean Enterprise Institute (John Shook's article): "one of the five foundational
  principles of the Toyota Way", firsthand investigation of a situation and its causes. Akio Toyoda quoted there:
  "Genchi genbutsu means 'the actual place', 'the actual thing'." and "Some things can only be felt when you are at
  the gemba." Shook's point (paraphrase): the principle matters more than physically visiting; Toyoda also says
  "we need to clarify under what conditions it is necessary to actually go see."

### Evidence it works, and where copying failed
- **The old GM Fremont plant, before Toyota** (NPR transcript, verbatim): Haggerty: "The line could never stop, never
  stop the line." Madrid: "I saw a guy fall in the pit and they didn't stop the line." Lee: "You saw a problem, you
  stop that line, you are fired." Langfitt: "The result? Tons of defects."
- **IndustryWeek**: "If signaling a problem gets you punished, or gets you nothing at all," people learn to hide it
  ("you learn very quickly to stop making the bad news visible"). Its advice: leaders should "come toward a problem
  and help, not assign blame."
- **Copying the cord without the culture.** A blog (paperplanes.de, 2014; a secondary opinion piece, treat as
  UNVERIFIED on facts) says that in other GM plants workers were "reprimanded for stopping the production line",
  that the cord was "cut down so it was harder to reach", and managers were "paid by volume of cars leaving the
  factory". The same-direction fact I did verify in the transcript: the old plant fired people for stopping the line.
  Also: NUMMI was closed in 2010 (the TAL page was published days before closure and does not confirm it). The TAL
  episode page poses, but doesn't answer here, "Why did it take so many years for GM to begin implementing the
  lessons of NUMMI across the company?" (from the page's own Act Two blurb, via the fetch tool).
- **Pull counts.** Lean Blog cites a 2007 BBC report: about 2,000 pulls a week at Toyota's Georgetown plant versus
  about two at Ford's Dearborn truck plant. Second-hand; UNVERIFIED (I did not find the BBC piece). The point it
  makes: a healthy cord is pulled a lot. Silence means fear, not quality.
- **Criticism of 5 whys** (Wikipedia, quoting others): Teruyuki Minoura called it "too basic a tool to analyze root
  causes at the depth necessary to ensure an issue is fixed"; Alan J. Card: "The arbitrary depth of the fifth why is
  unlikely to correlate with the root cause"; it tends "to stop at symptoms" and "to isolate a single root cause,
  whereas each question could elicit many different root causes."

### Stealable habits (Toyota), translated

1. **A yellow cord in the group chat, not a red one.** Anyone types `CORD: <what I'm stuck on / what looks wrong>`
   in the Keel chat. Rule: a person walks over (replies in the chat or calls within the same evening; on the 389,
   leans over) and the work only stops if it can't be fixed in the time left. First reply is a thank-you, never
   "why didn't you...". Cost: ten seconds to type. For me: when the model has run past midnight and I am on "one more
   scenario", that is the moment to type it. Weekday exams from 9 Nov are the test: a cord pulled in exam week must
   cost the puller nothing.
2. **The 5-whys chain, on paper, after a miss, with two people.** Not "who got it wrong" but "why did the system let
   it through". Example I'd run: my off-hand "$150k-$200k" nearly reached a draft. Why? I typed it from memory.
   Why? The chat is fast. Why was no one checking? Nobody owns the "does this have a MODEL tag" look. Why? Rule was
   only in my head. Fix: the tag rule on the pinned message. Ten minutes at lunch, bench by the library, two people;
   because the criticism above says one person stops at the first symptom. Stop when you reach something we can change.
3. **Go and see the real thing, not the message about it.** Before a number goes into the IPS draft, someone who did
   NOT compute it opens the raw file (the Treasury par-curve file, the WInS snapshot, the case PDF page) and reads
   the line out. Free period, 15 minutes, once for each number in the 50-word pitch and 500-word IPS. This is
   Felix's habit with my inputs, made two-way: I open his source too.
4. **A pull is never scored.** Do not count pulls as points. The Georgetown/Dearborn gap says "more is healthier",
   but a leaderboard in a six-person team turns into a joke or a shame. Just notice if the cord goes quiet for a
   week; that is the warning light.

### What I would refuse from Toyota
- **A real stop-everything switch.** Six people with a shift, a recital and the ATAR: a hard stop costs someone their
  Saturday 6 a.m. at the bakery. Yellow first; stop only if it can't be fixed.
- **The word "root cause" as a trophy.** The 5-whys critics are right that "five" is arbitrary. Stop when it's fixable.

## Part 2. Google's Project Aristotle

### What it actually is
- **The study.** Google's re:Work page: researchers "identified 180 teams to study" ("115 project teams in
  engineering and 65 pods in sales"). NYT (Duhigg, 2016): looked first at who was on teams (socialising outside
  work, hobbies, education) and Abeer Dubey concluded: "The 'who' part of the equation didn't seem to matter."
- **The five dynamics, in Google's order of importance (re:Work, verbatim):** 1 psychological safety ("a shared belief
  held by members of a team that the team is safe for interpersonal risk taking", Edmondson's definition);
  2 dependability ("members reliably complete quality work on time"); 3 structure and clarity; 4 meaning;
  5 impact ("the subjective judgment that your work is making a difference").
- **Two norms** the NYT article names from Woolley's research: "equality in distribution of conversational
  turn-taking" and "average social sensitivity."
- **Google's own check question** for psychological safety: "If I make a mistake on our team, it is not held against
  me." (re:Work sample item.)
- **Edmondson's 1999 paper.** Office-furniture manufacturer (about 5,000 people); surveys to 53 teams, 427 members
  from 51 teams answered, managers outside each team rated learning and performance. Definition as above; she
  separates it from cohesiveness and trust (Field Guide summary, secondary).
- **Edmondson's 1996 hospital study** (summary page, not the paper): 8 nursing units, 2 hospitals, 6 months. Units
  with better manager coaching and relationships had MORE detected errors (r about .74), and a blind observer's
  "openness" ranking matched error reporting. The page's own reading: "what it does show is willingness to report
  varying systematically with the perceived openness of the leader" and it cannot show open units made fewer errors.
  Eight units only.

### Criticism and limits
- **psychsafety.com's critique (a site that sells training; weigh it):** the study is correlational and self-report;
  performance rated partly by managers and executives; no effect sizes or tests reported in the write-up; one company;
  "psychological safety" was added after the first four-factor model left gaps, "a post hoc interpretation", and the
  "most important" label doesn't come from a ranking test. The NYT piece is what spread it.
- **Sanner and Bunderson (2015)**, per the Field Guide summary (secondary): a meta-analysis of 51 studies (about
  3,700 teams) says safety's effect on learning "is not unconditional", depends on people being motivated to learn,
  and the headline effect sizes are "probably inflated" because most studies sampled complex, creative work. The
  summary itself flags that "motivation to learn" was inferred, not measured. UNVERIFIED at the paper.
- **Not "be nice".** Safe to say a mistake is not the same as comfortable. Aristotle's own list keeps dependability
  and clarity next to safety.
- **Size.** Google's teams ranged from 3 to 50, median 9 (psychsafety.com). Ours is six friends, who already like
  each other. Our risk is not unfriendliness; it is people who protect the others by staying quiet (Tess sitting on a
  problem; me working alone).

### Stealable habits (Aristotle), translated

1. **The one-mistake open.** At each Sunday-night call (Nora's photo of the board goes round that evening), whoever
   has the biggest number or draft goes first with one thing they got wrong that week. Two minutes. I already did it
   with Amara ("the bad row first", 25 Oct); make it the default. Costs nothing.
2. **Turn-taking on the clock.** Lunch huddles: each person gets 60 seconds uninterrupted, then the questions. Same
   idea as Nora's speak-first, but counted so the loudest two (Kai and I, in a good week) can't drift past the others.
   One timer on a phone.
3. **One question, Sunday, for ten seconds.** Re:Work's "If I make a mistake on our team, it is not held against me",
   answered 1 to 5 on a slip of paper in a pencil case. Six people cannot be anonymous in a chat poll (UNVERIFIED which
   apps hide voters), so use paper and report only the lowest score and the middle, never names. I'd refuse to
   graph it. If the lowest is 2 or under, we talk.
4. **Dependability said out loud.** "When my teammates say they'll do something, they follow through" (re:Work).
   Translate: if you can't do it before the bus on Thursday because of the shift or the recital, say it in the chat
   that day (value 4, "Say it the day you see it"). Not a confession: a calendar.

### What I would refuse from Aristotle
- **Treating safety as the whole answer.** The meta-analysis says it is conditional. Keel still needs the checks.
- **Scoring each other.** No rankings of teammates (repo rule). The slip survey reports a number, never a name.
- **Quoting "the top factor" to the judges as proof.** The data are one company, correlational. In our documents the
  habit shows as a changed decision, not a citation.

## How it serves Caplet before Sat 7 Nov
Eleven days to the IPS. The cord plus the two-person "go and see" catch the kind of slip that nearly cost us in the
off-hand-number week, and the one-mistake open gives the Final Report's Articulation section true material (an error
caught, with its cause) without any invented teamwork story. Keel's own events stay fiction; Caplet's own team would
need its own real versions logged.

## Sources (all read 27 Oct 2026 via the fetch tool, which summarises pages; exact quotes are as returned)
- NPR transcript of This American Life, "NUMMI": https://www.npr.org/transcripts/125229157 (read 27 Oct 2026; quotes re-requested verbatim)
- This American Life episode 403 page: https://www.thisamericanlife.org/403/nummi (read 27 Oct 2026)
- Lean Blog, "Where Was Toyota's First Andon Cord?": https://www.leanblog.org/2026/08/where-was-the-first-andon-cord/ (read 27 Oct 2026)
- IndustryWeek, "Andon Is a Signal, But Leadership's Response Is the Critical Part": https://www.industryweek.com/operations/continuous-improvement/article/55394935/andon-is-a-signalbut-leaderships-response-is-the-critical-part (read 27 Oct 2026)
- Lean Enterprise Institute, Akio Toyoda and genchi genbutsu: https://www.lean.org/the-lean-post/articles/keep-calm-and-manage-stably-akio-toyodas-response-to-crisis/ (read 27 Oct 2026)
- Wikipedia, Five whys: https://en.wikipedia.org/wiki/Five_whys (read 27 Oct 2026; secondary)
- paperplanes.de, "you can't replicate culture": https://www.paperplanes.de/2014/9/17/you-cant-replicate-culture (read 27 Oct 2026; blog, UNVERIFIED facts)
- Google re:Work, Understand team effectiveness: https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness (read 27 Oct 2026)
- NYT, Duhigg, "What Google Learned From Its Quest to Build the Perfect Team" (St Olaf PDF copy): https://pages.stolaf.edu/csci-263-fall19/wp-content/uploads/sites/1376/2018/02/What-Google-Learned-From-Its-Quest-to-Build-the-Perfect-Team-The-New-York-Times.pdf (read 27 Oct 2026)
- psychsafety.com, "Google's Project Aristotle": https://psychsafety.com/googles-project-aristotle/ (read 27 Oct 2026; vendor, weigh it)
- Field Guide summary, Edmondson 1999: https://explore.psychsafety.com/n/edmondson-1999/ (read 27 Oct 2026; secondary)
- Field Guide summary, Edmondson 1996: https://explore.psychsafety.com/n/edmondson-1996.md (read 27 Oct 2026; secondary)
- Field Guide summary, Sanner and Bunderson 2015: https://explore.psychsafety.com/n/sanner-bunderson-2015.md (read 27 Oct 2026; secondary)
