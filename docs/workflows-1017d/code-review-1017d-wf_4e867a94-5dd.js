export const meta = {
  name: 'code-review-1017d',
  description: 'Adversarial code review: 6 release targets x 5 dimensions (security and privacy, correctness, money and AI cost, performance, accessibility and truth), each finding re-checked by a skeptic',
  phases: [ { title: 'Review' }, { title: 'Verify' } ],
}
const ROOT = 'C:\\Users\\atish\\Desktop\\mockmob copy'
const HY = `RULES: read only. Do not edit, commit, run servers, builds or browsers. Read code from git objects (git -C <worktree> diff <base> <head>, git -C <worktree> show <head>:<path>) because other agents are editing these worktrees right now. Return findings as text or the schema.`
const TARGETS = [
  { key: 'web-start', wt: 'wt-fx-start', base: 'f725a422', head: 'df7cf860', what: 'website fix branch: Start, Practice and runner owner-ledger fixes' },
  { key: 'web-pricing', wt: 'wt-fx-pricing', base: 'f725a422', head: '2ee6deea', what: 'website fix branch: pricing, help, copy and W-093 to W-099 (incl. W-098 AI cost)' },
  { key: 'web-mob', wt: 'wt-mobfix', base: '$(git -C wt-mobfix merge-base 1f5d2f4a f725a422)', head: '1f5d2f4a', what: 'the Mob web and server (group study: invites, papers, sharing, Free vs Pro, rate limits, reports, privacy)' },
  { key: 'app-v13', wt: 'wt-v13', base: '29abcf75', head: 'e92266bd', what: 'Flutter app v13 repair round (glass, bar, Today, result, review) plus the whole v13 Mob client under lib/features/social' },
  { key: 'landing', wt: 'wt-land2', base: 'f725a422', head: '9e3ceab7', what: 'the new landing page (src/app/page.js, src/components/landing)' },
  { key: 'web-lr', wt: 'wt-lr17', base: 'f725a422', head: '5d1969c7', what: 'Learn and Review: GET /api/me/review, review_input, the revise_cards.mode migration, the Review page' },
]
const DIMS = [
  { key: 'security', model: 'opus', ask: 'security and privacy: auth on every route, one student reading another student\'s data, RLS and service-role use, invite codes and enumeration, rate limits, injection, secrets in client bundles, minors\' data, logging of personal data' },
  { key: 'correctness', model: 'sonnet', ask: 'correctness bugs: wrong logic, unhandled states, race conditions, double submits, off-by-one, timezone (IST) and 12-hour clock errors, null handling, broken error paths, tests that do not test what they claim' },
  { key: 'money', model: 'sonnet', ask: 'money and AI cost: credits charged twice or not at all, atomic credit RPCs bypassed, paid entitlements, the per-user AI cap (Rs 5 paid, Rs 1 free; only gpt-6-luna and claude-haiku-5-5) skipped on any AI call, retries that multiply cost, Pro-only features reachable by Free' },
  { key: 'performance', model: 'sonnet', ask: 'performance: N+1 or unbounded Supabase queries, missing indexes, large client bundles, layout shift, heavy re-renders, for the app jank on a 2-4 GB budget phone (BackdropFilter and shader cost, rebuild storms, unbounded lists)' },
  { key: 'a11y-truth', model: 'sonnet', ask: 'accessibility and truth: WCAG 2.2 AA (contrast, focus, labels, targets, reduced motion), and any user-facing copy that claims something the product does not do (data/capabilities.js gates), hype, build talk, ALL-CAPS labels, wrong numbers' },
]
const FIND = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['high', 'medium', 'low'] }, file: { type: 'string' }, line: { type: 'string' }, what: { type: 'string' }, scenario: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'what', 'scenario', 'fix'] } } }, required: ['findings'] }
const VER = { type: 'object', properties: { real: { type: 'boolean' }, why: { type: 'string' } }, required: ['real', 'why'] }
phase('Review')
const jobs = TARGETS.flatMap(t => DIMS.map(d => ({ t, d })))
const results = await pipeline(jobs,
  (j) => agent(`${HY}\n\nYOU ARE a ${j.d.key} reviewer for ${j.t.what}. Worktree ${ROOT}\\${j.t.wt}; review the change from ${j.t.base} to ${j.t.head} (run the base expression in Git Bash from ${ROOT} if it is a $(...) expression) and the code it touches. Focus only on ${j.d.ask}. Report only real, concrete problems with a failure scenario (inputs or state, then the wrong result), severity, file and line, and a concrete fix. No style nits.`, { label: `${j.t.key}:${j.d.key}`, phase: 'Review', model: j.d.model, effort: 'high', schema: FIND }),
  (r, j) => r && (r.findings || []).length ? parallel((r.findings || []).filter(f => f.severity !== 'low').map(f => () => agent(`${HY}\n\nYOU ARE a skeptic. Try to REFUTE this ${j.d.key} finding about ${j.t.what} (worktree ${ROOT}\\${j.t.wt}, head ${j.t.head}): ${JSON.stringify(f)}. Read the code at ${j.t.head}. real=true only if you confirm the failure scenario can happen; default to real=false if uncertain.`, { label: `verify:${j.t.key}:${j.d.key}`, phase: 'Verify', model: 'sonnet', effort: 'medium', schema: VER }).then(v => ({ ...f, target: j.t.key, dim: j.d.key, verdict: v })))).then(vs => ({ target: j.t.key, dim: j.d.key, confirmed: vs.filter(Boolean).filter(x => x.verdict && x.verdict.real), lows: (r.findings || []).filter(f => f.severity === 'low') })) : { target: j.t.key, dim: j.d.key, confirmed: [], lows: [] }
)
const all = results.filter(Boolean)
return { confirmed: all.flatMap(x => x.confirmed.map(c => ({ target: x.target, dim: x.dim, severity: c.severity, file: c.file, line: c.line, what: c.what, scenario: c.scenario, fix: c.fix }))), lows: all.flatMap(x => x.lows.map(l => ({ target: x.target, dim: x.dim, file: l.file, what: l.what, fix: l.fix }))) }
