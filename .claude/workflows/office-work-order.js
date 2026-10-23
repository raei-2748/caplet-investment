export const meta = {
  name: 'office-work-order',
  description: 'Caplet Research Office: route one work order to several specialists in parallel, synthesise one page, fact-check, and return the memo',
  whenToUse: 'For a question that needs several desks, when the student asked for the full office. args: {work_order: path, date: "YYYY-MM-DD", workstream: "tna"|"ips"|"final"|"cross-cutting", specialists: [{name, ask}]}',
  phases: [
    { title: 'Specialists', detail: 'named specialists in parallel' },
    { title: 'Synthesis', detail: 'chief of staff one-page draft' },
    { title: 'Verify', detail: 'fact-checker; one revision if held' },
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

const VERDICT = {
  type: 'object',
  properties: {
    ship: { type: 'boolean' },
    table: { type: 'string', description: 'claim | PASS/FAIL/UNVERIFIED | what was checked | fix' },
  },
  required: ['ship', 'table'],
}

const STREAMS = { tna: '1_TNA.md', ips: '2_IPS.md', final: '3_FINAL_REPORT.md' }
const a = args || {}
if (!a.work_order || !a.date || !a.specialists || !a.specialists.length) {
  return 'office-work-order needs args {work_order: path to keel/office/work_orders/WO-NNNN.md, date, workstream, specialists: [{name, ask}]}'
}
const stream = STREAMS[a.workstream] ? ` Workstream file: keel/office/workstreams/${STREAMS[a.workstream]} (read it for dates and gates).` : ''
const wo = `Work order: ${a.work_order} (read it first).${stream}`

phase('Specialists')
const outs = await parallel(a.specialists.map(s => () =>
  desk(s.name, `${wo} Your part: ${s.ask || 'answer the question from your role'}. Half a page at most.`,
    { label: s.name, phase: 'Specialists' })))

phase('Synthesis')
const body = a.specialists.map((s, i) => `## ${s.name}\n${outs[i] || '(no result)'}`).join('\n\n')
let memo = await agent(
  `Read .claude/agents/chief-of-staff.md and keel/office/CHARTER.md. ${wo}\n\nSpecialist results:\n\n${body}\n\n` +
  'Synthesise ONE memo in the CHARTER section 5 format: one page, answer first, at most three findings ranked by score impact. Where specialists disagree, re-check the source; if still open, show both with their basis. Return only the memo text. Do not spawn agents or write files.',
  { label: 'chief-of-staff:synthesis', phase: 'Synthesis' })

phase('Verify')
let check = await desk('fact-checker', `Check this office memo before it ships:\n\n${memo}`, { phase: 'Verify', schema: VERDICT })
if (check && !check.ship) {
  memo = await agent(
    `Read keel/office/CHARTER.md. Revise this memo so every FAIL below is fixed or the claim is removed; mark anything unresolved UNVERIFIED. Return only the memo.\n\nMemo:\n${memo}\n\nFact-check:\n${check.table}`,
    { label: 'chief-of-staff:revise', phase: 'Verify' })
  check = await desk('fact-checker', `Re-check this revised office memo:\n\n${memo}`, { phase: 'Verify', schema: VERDICT })
}
return { date: a.date, work_order: a.work_order, ship: !!(check && check.ship), memo, fact_check: check ? check.table : null }
