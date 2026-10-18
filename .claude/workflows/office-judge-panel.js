export const meta = {
  name: 'office-judge-panel',
  description: 'Caplet Research Office: five independent mock judges score a draft, then the judging lead compares them with the students\' own scores',
  whenToUse: 'About a week before a deadline, after two students and the outside reader have scored the draft. args: {deliverable: "tna"|"ips"|"final", draft: path, human_scores: path}',
  phases: [
    { title: 'Judge', detail: 'five personas, blind to each other' },
    { title: 'Synthesis', detail: 'judging-lead ranks fixes by score impact' },
  ],
}

async function desk(name, prompt, opts) {
  const o = Object.assign({ label: name }, opts || {})
  try {
    return await agent(prompt, Object.assign({ agentType: name }, o))
  } catch (e) {
    return await agent(`Read .claude/agents/${name}.md and act as that agent.\n\n${prompt}`, o)
  }
}

const a = args || {}
if (!a.human_scores) {
  return 'Not run: humans score first. Two students and the outside reader must mark the draft against the official criterion text and save the scores (pass the file as args.human_scores). 16 Oct review item 23.'
}
if (!a.deliverable || !a.draft) {
  return 'office-judge-panel needs args {deliverable, draft, human_scores}'
}

const PERSONAS = ['faculty', 'practitioner', 'former-finalist', 'outsider', 'finance-undergrad']
phase('Judge')
const scores = await parallel(PERSONAS.map(p => () =>
  desk('mock-judge',
    `Persona: ${p}. Deliverable: ${a.deliverable}. Draft: ${a.draft}. Judge it as a real judge would, using only the inputs listed in your definition (do not open ${a.human_scores} or any office memo). Never suggest new wording.`,
    { label: `judge:${p}`, phase: 'Judge' })))

phase('Synthesis')
const body = PERSONAS.map((p, i) => `## ${p}\n${scores[i] || '(no result)'}`).join('\n\n')
return await desk('judging-lead',
  `Deliverable: ${a.deliverable}. Draft: ${a.draft}. Students' own scores: ${a.human_scores} (read it now).\n\nMock judges:\n\n${body}\n\n` +
  'Produce your standard return. Add a column comparing the AI median with the student scores per criterion; gaps of 2+ points are findings. Look in office/outbox/ for the previous panel on this deliverable and report the change.',
  { phase: 'Synthesis' })
