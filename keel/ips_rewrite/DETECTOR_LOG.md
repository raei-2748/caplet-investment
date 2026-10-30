# The AI-detector gate (Commandment VI): what was tried, 30 Oct 2026

AI-generated (Claude Code), not for submission.

**The rule (Book 10, Caplet, 30 Oct):** every IPS draft goes through GPTZero before Caplet sees it, and the "human-written
only" probability must be above 50%. Book 9 (27 Oct) had already asked for real detectors instead of our own agents,
and Keel didn't do it. That was a miss, and this log is the fix.

## What we tried from Keel's cloud session (30 Oct)
| Route | Result |
|---|---|
| GPTZero API (`api.gptzero.me/v2/predict/text`) | Answers "Require login or API key". The key needs a paid plan, which Caplet doesn't have. |
| GPTZero's free scanner (gptzero.me, no account) in a headless browser | The page loads and takes the text, but Scan does nothing. The scan relies on Google's reCAPTCHA and analytics hosts, and this session's network policy blocks them. Getting past a CAPTCHA is something Keel may never do, so this route is closed. |
| Other detectors (ZeroGPT, Sapling, Copyleaks, QuillBot, Scribbr, Originality, Writer, Crossplag, Hugging Face models) | All blocked by the network policy (the proxy refuses the connection). |
| Open-source detectors run locally: GPT-2 perplexity and burstiness (GPTZero's original method), Fast-DetectGPT's analytic score, and a ZipPy-style compression score; GPT-2 weights from the ONNX Model Zoo on GitHub; code in `detector/` | **Not valid, so not used.** We calibrated them on Ahaan's essays and Caplet's own messages (human) against our drafts, the simulated rivals, and seven fresh AI controls written in the same genres (essays on Ahaan's three topics, messages, a report section, a plain IPS). Leave-one-source-out accuracy was 44%, worse than a coin. AI essays scored *more* human than Ahaan's, and last year's human-written Final Report scored 22% human. A 2019 model can't tell 2026 AI prose from a person; it only picks out number-dense finance text. |

## What Keel does instead
- No made-up or home-made score stands in for GPTZero (Book 9: "at least do it properly").
- Every draft says **"GPTZero: not yet checked"** until a real scan exists.
- Voice work (Commandment III) carries the load: short, plain sentences; a real team event (our three-quarters-stocks
  first plan, which our model sank); a rhetorical question; one wry line; no slogans, triads or fact-sheet runs.
- **Thursday, 1 minute, no account:** paste the pitch and IPS into the free box on https://gptzero.me. If "human-written
  only" is under 50%, tell Keel the score and Keel rewrites until it passes.
