export const meta = {
  name: 'office-work-order',
  description: 'Caplet Research Office: route one work order through several desks (specialists, then each desk lead), fact-check, and ship a one-page memo',
  whenToUse: 'For a question that needs three or more desks, when the student asked for the full office. args: {work_order: path, date: "YYYY-MM-DD", desks: [{lead, specialists: [names], ask}]}',
  phases: [
    { title: 'Desks', detail: 'specialists in parallel, then the desk lead, per desk' },
    { title: 'Merge', detail: 'chief of staff one-page draft' },
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

const a = args || {}
if (!a.work_order || !a.desks || !a.desks.length || !a.date) {
  return 'office-work-order needs args {work_order: path to office/work_orders/WO-NNNN.md, date, desks: [{lead, specialists, ask}]}'
}
const wo = `Work order: ${a.work_order} (read it first).`

phase('Desks')
const deskResults = await pipeline(a.desks,
  d => parallel((d.specialists || []).map(s => () =>
    desk(s, `${wo} Your part: ${d.ask || 'answer the question for your desk'}.`, { label: s, phase: 'Desks' }))),
  (outs, d) => desk(d.lead,
    `${wo} Your desk's part: ${d.ask || 'answer the question for your desk'}.\n\nSpecialist results:\n\n` +
    (d.specialists || []).map((s, i) => `## ${s}\n${outs[i] || '(no result)'}`).join('\n\n') +
    '\n\nSynthesise in your standard return format. Half a page at most.',
    { label: d.lead, phase: 'Desks' }))

phase('Merge')
const deskText = a.desks.map((d, i) => `## ${d.lead}\n${deskResults[i] || '(no result)'}`).join('\n\n')
let memo = await agent(
  `Read .claude/agents/chief-of-staff.md and office/CHARTER.md. ${wo}\n\nDesk results:\n\n${deskText}\n\n` +
  'Merge into ONE memo in the CHARTER section 5 format, one page, answer first, at most three findings. Return only the memo text. Do not spawn agents or write files.',
  { label: 'chief-of-staff:merge', phase: 'Merge' })

phase('Verify')
let check = await desk('fact-checker', `Check this office memo before it ships:\n\n${memo}`, { phase: 'Verify', schema: VERDICT })
if (check && !check.ship) {
  memo = await agent(
    `Read office/CHARTER.md. Revise this memo so every FAIL below is fixed or the claim is removed; mark anything unresolved UNVERIFIED. Return only the memo.\n\nMemo:\n${memo}\n\nFact-check:\n${check.table}`,
    { label: 'chief-of-staff:revise', phase: 'Verify' })
  check = await desk('fact-checker', `Re-check this revised office memo:\n\n${memo}`, { phase: 'Verify', schema: VERDICT })
}
return { date: a.date, work_order: a.work_order, ship: !!(check && check.ship), memo, fact_check: check ? check.table : null }
