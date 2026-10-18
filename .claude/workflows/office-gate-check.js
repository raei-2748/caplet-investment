export const meta = {
  name: 'office-gate-check',
  description: 'Caplet Research Office: pass/fail check of a deliverable against the hard gates before submission',
  whenToUse: 'Before submitting the TNA, IPS or Final Report. args: {deliverable: "tna"|"ips"|"final", files: [paths], wins_notes?: path, note: string?}',
  phases: [
    { title: 'Check', detail: 'format, rules, integrity and coherence specialists in parallel' },
    { title: 'Verdict', detail: 'rules-lead gate table' },
  ],
}

// Run a desk agent; if the custom agent type is not registered in this session, fall back to a
// general-purpose agent told to adopt the definition file.
async function desk(name, prompt, opts) {
  const o = Object.assign({ label: name }, opts || {})
  try {
    return await agent(prompt, Object.assign({ agentType: name }, o))
  } catch (e) {
    return await agent(`Read .claude/agents/${name}.md and act as that agent.\n\n${prompt}`, o)
  }
}

const a = args || {}
if (!a.deliverable || !a.files || !a.files.length) {
  return 'office-gate-check needs args {deliverable: "tna"|"ips"|"final", files: [paths of the student draft or exported PDF/text]}'
}
const files = a.files.join(', ')
const base = `Deliverable: ${a.deliverable}. Student files: ${files}.` +
  (a.wins_notes ? ` Notes as copied from WInS: ${a.wins_notes}.` : '') +
  (a.note ? ` Context from the student: ${a.note}.` : '') +
  ' Check only; never reword the draft. Return a table with PASS / FAIL / NOT CHECKABLE per item and evidence.'

phase('Check')
const [fmt, rules, integ, coh] = await parallel([
  () => desk('format-gatekeeper', `${base} Run office/tools/textcheck.py on each part (limits for this deliverable); for notes use --compare against the WInS copy.`, { phase: 'Check' }),
  () => desk('rules-verifier', `${base} Quote the exact official 2026-27 requirement for every format and content gate of this deliverable, from the live page where possible, and say if the live page differs from the repo snapshot.`, { phase: 'Check' }),
  () => desk('integrity-officer', `${base} Check AI-policy and authorship risks in these files and that nothing in them or the repo exposes personal data.`, { phase: 'Check' }),
  () => desk('coherence-checker', `${base} Check these files against the other deliverables, the filled WInS notes and the numbers on a named basis.`, { phase: 'Check' }),
])

phase('Verdict')
const verdict = await desk('rules-lead',
  `${base}\n\nYour specialists reported:\n\n## format-gatekeeper\n${fmt}\n\n## rules-verifier\n${rules}\n\n## integrity-officer\n${integ}\n\n## coherence-checker\n${coh}\n\n` +
  'Produce the gate table (gate | PASS / FAIL / NOT CHECKABLE | evidence | fix | owner role | due) and the single most dangerous item. Where specialists disagree, re-check the source yourself.',
  { phase: 'Verdict' })
return verdict
