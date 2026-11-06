export const meta = {
  name: 'app-ledger-precheck-1017d',
  description: 'App ledger pre-check: 19 agents check every F1-F18 and L01-L39 item against the v13 code (read-only) and write exact fix specs for walk 2 and the final fixers',
  phases: [ { title: 'Check' } ],
}
const ROOT = 'C:\\Users\\atish\\Desktop\\mockmob copy'
const NEXT = `${ROOT}\\mockmob-next`
const BR = `${NEXT}\\docs\\brain`
const DD = `${NEXT}\\docs\\design-decisions`
const IDS = [...Array.from({ length: 18 }, (_, i) => 'F' + (i + 1)), ...Array.from({ length: 39 }, (_, i) => 'L' + String(i + 1).padStart(2, '0'))]
const groups = []; for (let i = 0; i < IDS.length; i += 3) groups.push(IDS.slice(i, i + 3))
const R = { type: 'object', properties: { items: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, status: { type: 'string', enum: ['done', 'partial', 'missing', 'web-only'] }, evidence: { type: 'string' }, gap: { type: 'string' }, fix: { type: 'string' } }, required: ['id', 'status', 'evidence'] } } }, required: ['items'] }
phase('Check')
const out = await parallel(groups.map((g, i) => () => agent(`RULES: read only; do not edit, commit or run Flutter; read the app code from git objects (git -C "${ROOT}\\wt-v13" show e92266bd:<path>, git grep at e92266bd) because fixers are editing that tree. Return the schema.\n\nYOU ARE app ledger checker ${i + 1}. Items: ${g.join(', ')}. F items are in ${BR}\\OWNER-FEEDBACK-2026-10-17.md (the owner's 17 Oct words), L items in ${BR}\\APP-OWNER-LEDGER-2026-10-16.md (his 16 Oct words with steps). Design docs: ${DD}\\pass-1017. Walk-1 evidence: ${NEXT}\\tmp\\resume-1017c\\wf_e62f61a8-c85-walk-1.json and its screenshots under ${NEXT}\\tmp\\app-walk-1017\\v13-1. For each item decide from the code (and the walk-1 shots) whether v13 does what he asked: done, partial, missing, or web-only (not an app item). Give the evidence (file and line, or the screenshot), the exact gap, and an exact fix (file, widget, change).`, { label: `check-${g[0]}-${g[g.length - 1]}`, phase: 'Check', model: 'sonnet', effort: 'high', schema: R })))
const items = out.filter(Boolean).flatMap(o => o.items || [])
return { done: items.filter(i => i.status === 'done').length, gaps: items.filter(i => i.status === 'partial' || i.status === 'missing') }
