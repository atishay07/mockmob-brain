// LK69 scroll probe (read-only), v2: one headless browser, 390x844 touch, CDP gestures on the home page's paged sections.
//   node probe.mjs [base=https://www.mockmob.in/] [mode=smoke|main|perf] [browser=chrome|shell] [theme=dark]
// Writes results-<mode>.json, results-<mode>.md and screenshots into this folder. Takes the shared browser lock
// (tmp-devslots/browser.lock, a file holding our label), waits 30 s at a time while someone else holds it, and deletes
// it (only if it is still ours) when the browser closes, also on error.
// v1 (probe-v1.mjs) used chrome-headless-shell, where Input.synthesizeScrollGesture returned without scrolling, and
// measured the stories once at load, before content above the Score Recovery story grew; v2 measures before every run.
import { createRequire } from 'node:module';
import { writeFileSync, readFileSync, rmSync, utimesSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/atish/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core');
const EXES = {
  chrome: 'C:/Users/atish/.cache/puppeteer/chrome/win64-151.0.7922.71/chrome-win64/chrome.exe',
  shell: 'C:/Users/atish/.cache/puppeteer/chrome-headless-shell/win64-151.0.7922.71/chrome-headless-shell-win64/chrome-headless-shell.exe',
};
const OUT = 'C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/scroll';
const LOCK = 'C:/Users/atish/Desktop/mockmob copy/tmp-devslots/browser.lock';
const [BASE = 'https://www.mockmob.in/', MODE = 'main', BROWSER = 'chrome', THEME = 'dark'] = process.argv.slice(2);
const LABEL = `home-1104/scroll LK69 probe (${MODE}) pid ${process.pid} ${new Date().toISOString()}`;
const W = 390; const H = 844;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------- lock
let beat = null;
async function takeLock() {
  for (let i = 0; ; i += 1) {
    try { writeFileSync(LOCK, LABEL, { flag: 'wx' }); break; } catch (e) {
      if (!['EEXIST', 'EISDIR', 'EPERM', 'EBUSY'].includes(e.code)) throw e;
      let who = ''; try { who = readFileSync(LOCK, 'utf8').slice(0, 120); } catch { who = '(a directory or unreadable)'; }
      console.log(`lock busy (${who}); waiting 30 s [${i}]`);
      await sleep(30000);
    }
  }
  beat = setInterval(() => { try { const t = new Date(); utimesSync(LOCK, t, t); } catch { /* gone */ } }, 20000);
  console.log('lock taken');
}
function dropLock() {
  if (beat) clearInterval(beat);
  beat = null;
  try { if (existsSync(LOCK) && readFileSync(LOCK, 'utf8') === LABEL) { rmSync(LOCK, { force: true }); console.log('lock dropped'); } } catch { /* not ours */ }
}
process.on('exit', dropLock);
process.on('SIGINT', () => { dropLock(); process.exit(130); });

// ---------------------------------------------------------------- page helpers
const results = [];
const shots = [];
let page; let cdp; let geo;

const measure = () => page.evaluate(() => {
  const top = (el) => Math.round(el.getBoundingClientRect().top + window.scrollY);
  const names = { lc: 'lab', 'ft-story': 'tour', 'ml-story': 'recovery' };
  const stories = [...document.querySelectorAll('.ss')].map((s, index) => {
    const t = s.querySelector('.ss__track'); const st = s.querySelector('.ss__stage');
    const steps = s.querySelectorAll('.ss__beat').length; const hold = t.offsetHeight - st.offsetHeight;
    const cls = s.className.split(' ')[1];
    return { index, name: names[cls] || cls, cls, top: top(t), trackH: t.offsetHeight, stageH: st.offsetHeight, hold, steps, gap: +(hold / (steps - 1)).toFixed(1), beat: getComputedStyle(s).getPropertyValue('--ss-beat').trim() };
  });
  const st = document.querySelector('.lp-statement'); const grid = st?.querySelector('.lp-statement__grid');
  const sec = (sel, name) => { const el = document.querySelector(sel); return el ? { name, top: top(el), h: el.offsetHeight } : null; };
  const sections = [sec('.lp-hero', 'hero'), sec('.lp-statement', 'statement'), sec('#inside-the-lab', 'lab-section'), sec('#your-prep', 'tour-section'), sec('#score-recovery-lab', 'recovery-section'), sec('#compass', 'compass'), sec('#du-eligibility', 'du'), sec('#exam-experience', 'exam'), sec('#pricing', 'pricing')].filter(Boolean).sort((a, b) => a.top - b.top);
  return { vh: window.innerHeight, docH: document.documentElement.scrollHeight, stories, statement: st ? { top: top(st), h: st.offsetHeight, gridPos: getComputedStyle(grid).position, gridStickyTop: getComputedStyle(grid).top, gridH: grid.offsetHeight } : null, sections };
});
const yNow = () => page.evaluate(() => Math.round(window.scrollY));
async function jump(y) {
  await page.evaluate((v) => window.scrollTo({ top: v, behavior: 'instant' }), Math.round(y));
  await page.evaluate(() => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))));
  await sleep(900);
}
async function settle(quiet = 800, max = 12000) {
  const t0 = Date.now(); let last = await yNow(); let since = Date.now();
  while (Date.now() - t0 < max) {
    await sleep(80);
    const y = await yNow();
    if (y !== last) { last = y; since = Date.now(); } else if (Date.now() - since >= quiet) break;
  }
  await sleep(450); // let the step swap transitions land before reading and shooting
  return { y: await yNow(), ms: Date.now() - t0 };
}
const snap = () => page.evaluate(() => {
  const scale = (m) => { if (!m || m === 'none') return { x: 1, y: 1 }; const v = m.match(/matrix\(([^)]+)\)/); if (!v) return null; const p = v[1].split(',').map(Number); return { x: +p[0].toFixed(3), y: +p[3].toFixed(3) }; };
  const ss = [...document.querySelectorAll('.ss')].map((s) => {
    const st = s.querySelector('.ss__stage').getBoundingClientRect();
    const on = s.querySelector('.ss-fill[data-state="on"]');
    return { step: Number(s.dataset.step), live: s.dataset.live === 'true', stageTop: Math.round(st.top), fill: on ? scale(getComputedStyle(on).transform) : null };
  });
  const words = [...document.querySelectorAll('.lp-statement__w')].map((w) => Number(getComputedStyle(w).opacity));
  return { y: Math.round(window.scrollY), ss, lit: words.filter((o) => o >= 0.95).length, partial: words.filter((o) => o > 0.22 && o < 0.95).length, words: words.length };
});
const takeLog = () => page.evaluate(() => ({ steps: window.__log.splice(0), ys: window.__ys.splice(0) }));
const clearLog = () => page.evaluate(() => { window.__log.length = 0; window.__ys.length = 0; });

// Where the window is: the section under its middle, and inside or next to a story its state and step phase.
function where(y, g = geo) {
  const mid = y + H / 2;
  let name = 'hero';
  for (const s of g.sections) if (mid >= s.top) name = s.name;
  const story = g.stories.find((s) => y >= s.top - H && y <= s.top + s.hold + H);
  let inStory = null;
  if (story) {
    const d = y - story.top;
    if (d < 0) inStory = { story: story.name, state: 'entering', stageShown: Math.round(H + d) };
    else if (d > story.hold) inStory = { story: story.name, state: 'leaving', stageShown: Math.round(H - (d - story.hold)) };
    else { const phase = d / story.gap; const k = Math.round(phase); inStory = { story: story.name, state: 'held', phase: +phase.toFixed(2), nearestRest: k, offPx: Math.round(d - k * story.gap) }; }
  }
  const st = g.statement;
  const p = st ? (y - st.top) / (st.h - H) : NaN;
  const statement = p > -0.2 && p < 1.2 ? +p.toFixed(2) : undefined;
  return { section: name, ...inStory, ...(statement !== undefined ? { statementProgress: statement } : null) };
}

// Input.synthesizeScrollGesture: a touch drag at `speed` px/s; fling on = lifted while moving (Chrome flings on).
const synth = (dist, speed, fling = true) => cdp.send('Input.synthesizeScrollGesture', {
  x: Math.round(W / 2), y: dist > 0 ? 760 : 110, yDistance: -dist, speed, gestureSourceType: 'touch', preventFling: !fling,
});
// The same flick made of CDP touch events with exact timestamps (8 ms apart), lifted while moving (fling) or held first.
async function tflick(dist, speed, { fling = true } = {}) {
  const x = Math.round(W / 2); const y0 = dist > 0 ? 760 : 110;
  const total = (Math.abs(dist) / speed) * 1000;
  const n = Math.max(3, Math.round(total / 8));
  const dt = total / n;
  let t = Date.now() / 1000;
  await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y: y0 }], timestamp: t });
  for (let i = 1; i <= n; i += 1) {
    t += dt / 1000;
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x, y: Math.round(y0 - (dist * i) / n) }], timestamp: t });
    await sleep(dt);
  }
  if (!fling) { await sleep(300); t = Date.now() / 1000; }
  await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [], timestamp: t + 0.001 });
}
// A slow finger: dist px in 2 px moves every ~25 ms (about 80 px/s), held still 250 ms before lifting (no fling).
async function drag(dist, { stepPx = 2, everyMs = 25, holdMs = 250 } = {}) {
  const x = Math.round(W / 2); const y0 = dist > 0 ? 780 : 100;
  const n = Math.max(1, Math.round(Math.abs(dist) / stepPx));
  await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y: y0 }] });
  for (let i = 1; i <= n; i += 1) {
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x, y: Math.round(y0 - (dist * i) / n) }] });
    await sleep(everyMs);
  }
  await sleep(holdMs);
  await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
}

async function shoot(name) {
  const file = `${name}.png`;
  await page.screenshot({ path: join(OUT, file), scale: 'css' });
  shots.push(file);
  return file;
}

// One measured gesture. start(g) gives the start y from fresh geometry (layout above a story can still grow).
async function run(id, { story = null, start, gesture, kind, dist, speed = null, note = '', shot = false }) {
  await jump(start(geo));
  geo = { ...geo, ...(await measure()) };
  const y0 = start(geo);
  if (Math.abs((await yNow()) - y0) > 2) await jump(y0);
  const before = await snap();
  await clearLog();
  const t0 = Date.now();
  await gesture();
  const gestureMs = Date.now() - t0;
  const s = await settle();
  const after = await snap();
  const log = await takeLog();
  const S = story ? geo.stories.find((g) => g.name === story) : null;
  const si = S ? S.index : -1;
  const changes = si >= 0 ? log.steps.filter((e) => e.i === si) : [];
  const seen = [];
  for (const v of [before.ss[si]?.step, ...changes.map((e) => e.step)]) if (v !== undefined && seen[seen.length - 1] !== v) seen.push(v);
  const ys = log.ys.map((p) => p[1]);
  const r = {
    id, kind, story, dist, speed, note,
    from: { y: before.y, step: si >= 0 ? before.ss[si].step : null, at: where(before.y) },
    to: { y: after.y, step: si >= 0 ? after.ss[si].step : null, at: where(after.y) },
    moved: after.y - before.y, peak: ys.length ? (dist >= 0 ? Math.max(...ys) : Math.min(...ys)) - before.y : 0,
    stepDelta: si >= 0 ? after.ss[si].step - before.ss[si].step : null,
    stepChanges: changes.length, stepsShown: seen,
    otherStories: log.steps.filter((e) => e.i !== si).map((e) => `${geo.stories[e.i]?.name}:${e.step}`),
    fillAfter: si >= 0 ? after.ss[si].fill : null,
    stageTopAfter: si >= 0 ? after.ss[si].stageTop : null,
    words: { before: `${before.lit}+${before.partial}p/${before.words}`, after: `${after.lit}+${after.partial}p/${after.words}` },
    gestureMs, settleMs: s.ms,
  };
  if (shot) r.shot = await shoot(id);
  results.push(r);
  const t = r.to.at;
  console.log(`${id.padEnd(34)} y ${r.from.y}->${r.to.y} (${r.moved >= 0 ? '+' : ''}${r.moved}) step ${r.from.step}->${r.to.step} shown [${seen}] ${t.section}/${t.state || ''} ${t.phase ?? ''} off ${t.offPx ?? ''} sp ${t.statementProgress ?? ''} words ${r.words.before}->${r.words.after}`);
  return r;
}

// ---------------------------------------------------------------- main
async function main() {
  await takeLock();
  const browser = await chromium.launch({ executablePath: EXES[BROWSER], headless: true, args: ['--no-first-run', '--disable-extensions', '--js-flags=--max-old-space-size=512'] });
  try {
    const ctx = await browser.newContext({
      viewport: { width: W, height: H }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: THEME,
      userAgent: 'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36',
    });
    await ctx.addInitScript((t) => { try { localStorage.setItem('mm:theme:v1', t); localStorage.setItem('mm:theme-hint:v1', '1'); } catch { /* none */ } }, THEME);
    const errors = [];
    const save = (name, rows, g) => {
      writeFileSync(join(OUT, `results-${name}.json`), JSON.stringify({ base: name === 'proto' ? PROTO : BASE, mode: name, browser: BROWSER, theme: THEME, flick: flickKind, when: new Date().toISOString(), viewport: `${W}x${H} touch, dsf 2`, geo: g, results: rows, shots, errors: errors.slice(0, 20) }, null, 1));
      if (name !== 'perf') writeFileSync(join(OUT, `results-${name}.md`), `flick rows use: ${flickKind}\n\n${table(rows)}`);
    };
    await openPage(ctx, BASE, errors);
    const prodGeo = geo;
    if (MODE === 'smoke') { await smokeRuns(); save('smoke', results, geo); }
    if (MODE === 'main' || MODE === 'all') {
      await chooseFlick();
      await mainRuns(); save('main', results.splice(0), prodGeo);
    }
    if (MODE === 'perf' || MODE === 'all') { await perfRuns(); save('perf', results.splice(0), prodGeo); }
    if (MODE === 'proto' || MODE === 'all') {
      if (!flickFn) await chooseFlick();
      await page.close();
      await openPage(ctx, `${PROTO}`, errors);
      await protoRuns('proto', ''); save('proto', results.splice(0), geo);
      await page.close();
      await openPage(ctx, `${PROTO}?latch=0`, errors);
      await protoRuns('proto-nolatch', 'nolatch'); save('proto-nolatch', results.splice(0), geo);
    }
    await ctx.close();
  } finally {
    try { await browser.close(); } catch { /* gone */ }
    dropLock();
  }
}

const PROTO = pathToFileURL(join(OUT, 'prototype-one-gesture.html')).href;
let flickFn = null; let flickKind = '';

async function openPage(ctx, url, errors) {
  page = await ctx.newPage();
  page.on('pageerror', (e) => errors.push(`pageerror ${e.message.slice(0, 160)}`));
  cdp = await ctx.newCDPSession(page);
  await page.goto(url, { waitUntil: 'load', timeout: 180000 });
  await sleep(url.startsWith('file:') ? 800 : 3000);
  // Warm the page: walk it top to bottom once (lazy images, reveals, content-visibility), then measure.
  const docH = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < docH; y += 700) { await page.evaluate((v) => window.scrollTo({ top: v, behavior: 'instant' }), y); await sleep(120); }
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  await sleep(1500);
  geo = await measure();
  geo.svh = await page.evaluate(() => { const d = document.createElement('div'); d.style.cssText = 'position:absolute;height:100svh;width:1px;visibility:hidden'; document.body.appendChild(d); const h = d.offsetHeight; d.remove(); return h; });
  geo.env = await page.evaluate(() => ({ url: location.href, ua: navigator.userAgent, coarse: matchMedia('(pointer: coarse)').matches, hoverNone: matchMedia('(hover: none)').matches, reduced: matchMedia('(prefers-reduced-motion: reduce)').matches, htmlScrollBehavior: getComputedStyle(document.documentElement).scrollBehavior, snapType: getComputedStyle(document.documentElement).scrollSnapType, scrollTimeline: CSS.supports('animation-timeline: view()') }));
  console.log(JSON.stringify({ stories: geo.stories, statement: geo.statement, env: geo.env, svh: geo.svh, docH: geo.docH }));
  await page.evaluate(() => {
    window.__log = []; window.__ys = [];
    const all = [...document.querySelectorAll('.ss')];
    const mo = new MutationObserver((muts) => { for (const m of muts) window.__log.push({ t: Math.round(performance.now()), i: all.indexOf(m.target), step: Number(m.target.dataset.step), y: Math.round(window.scrollY) }); });
    all.forEach((s) => mo.observe(s, { attributes: true, attributeFilter: ['data-step'] }));
    let last = -1;
    const tick = () => { const y = Math.round(window.scrollY); if (y !== last) { window.__ys.push([Math.round(performance.now()), y]); last = y; } requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  });
}

// Does Input.synthesizeScrollGesture move this page? If not, flick rows use CDP touch events with exact timestamps.
async function chooseFlick() {
  const lab = geo.stories[0];
  await jump(rest(lab, 1));
  const y0 = await yNow();
  await synth(300, 1200, true);
  const s = await settle();
  const ok = Math.abs(s.y - y0) > 50;
  flickFn = ok ? synth : tflick;
  flickKind = ok ? 'Input.synthesizeScrollGesture (touch, preventFling false)' : 'CDP touch events with exact timestamps (synthesizeScrollGesture did not move the page)';
  console.log(`synthesizeScrollGesture moved ${s.y - y0}px -> flick rows use ${flickKind}`);
  results.push({ id: 'synth-check', calibrate: true, y: s.y, step: `moved ${s.y - y0}`, want: 'synth 300px@1200' });
}

const S_ = (name) => (g) => g.stories.find((s) => s.name === name);
const rest = (S, k) => S.top + Math.round((S.hold * k) / (S.steps - 1));
const at = (name, k, off = 0) => (g) => rest(S_(name)(g), k) + off;

async function smokeRuns() {
  // Calibration: each story's resting places show their own step.
  for (const S of geo.stories) for (let k = 0; k < S.steps; k += 1) {
    await jump(at(S.name, k)(geo));
    const s = await snap();
    console.log(`calibrate ${S.name} rest ${k} y ${s.y} -> step ${s.ss[S.index].step}`);
    results.push({ id: `calibrate-${S.name}-${k}`, y: s.y, step: s.ss[S.index].step, want: k });
  }
  await run('smoke-lab-synth-300-1200', { story: 'lab', start: at('lab', 1), kind: 'synth touch, fling on', dist: 300, speed: 1200, gesture: () => synth(300, 1200, true) });
  await run('smoke-lab-tflick-300-1200', { story: 'lab', start: at('lab', 1), kind: 'touch events, fling on', dist: 300, speed: 1200, gesture: () => tflick(300, 1200) });
}

async function mainRuns() {
  const SPEEDS = [400, 1200, 3000, 6000];
  const DISTS = [60, 150, 300, 600];
  const SHOT = new Set(['lab-r1-synth-150-400', 'lab-r1-synth-300-3000', 'lab-r1-synth-600-6000', 'tour-r1-synth-300-3000', 'tour-r1-synth-600-6000', 'recovery-r1-synth-300-3000', 'statement-synth-150-400', 'statement-synth-300-1200', 'statement-synth-600-3000']);
  // 0. Calibration rows.
  for (const S of geo.stories) for (let k = 0; k < S.steps; k += 1) {
    await jump(at(S.name, k)(geo));
    const s = await snap();
    results.push({ id: `calibrate-${S.name}-${k}`, calibrate: true, y: s.y, step: s.ss[S.index].step, want: k });
  }
  // 1. Touch flicks (finger speed = release speed, fling on) from step 1's resting place of each story.
  for (const S of geo.stories) {
    for (const speed of SPEEDS) for (const dist of DISTS) {
      const id = `${S.name}-r1-synth-${dist}-${speed}`;
      await run(id, { story: S.name, start: at(S.name, 1), kind: 'flick, fling on', dist, speed, gesture: () => flickFn(dist, speed, true), shot: SHOT.has(id) });
    }
    await run(`${S.name}-r1-synthNoFling-300-1200`, { story: S.name, start: at(S.name, 1), kind: 'drag at speed, no fling', dist: 300, speed: 1200, gesture: () => (flickFn === synth ? synth(300, 1200, false) : tflick(300, 1200, { fling: false })) });
    await run(`${S.name}-r2-synthUp-300-3000`, { story: S.name, start: at(S.name, 2), kind: 'flick up, fling on', dist: -300, speed: 3000, gesture: () => flickFn(-300, 3000, true) });
  }
  // 2. The statement (phones: a 180svh sticky scrub), from where its hold starts.
  for (const speed of SPEEDS) for (const dist of DISTS) {
    const id = `statement-synth-${dist}-${speed}`;
    await run(id, { start: (g) => g.statement.top, kind: 'flick, fling on', dist, speed, gesture: () => flickFn(dist, speed, true), shot: SHOT.has(id) });
  }
  // 3. Flicks made of CDP touch events with exact timestamps (the same physics a finger gives Chrome).
  for (const S of geo.stories) for (const [dist, speed] of [[150, 1200], [300, 3000], [200, 2500], [600, 6000]]) {
    await run(`${S.name}-r1-touch-${dist}-${speed}`, { story: S.name, start: at(S.name, 1), kind: 'touch events, lifted moving', dist, speed, gesture: () => tflick(dist, speed), shot: S.name === 'tour' && dist === 200 });
  }
  // 4. Slow drags (2 px every 25 ms, held still, lifted: no fling).
  for (const S of geo.stories) {
    for (const dist of [150, 300]) await run(`${S.name}-r1-slowdrag-${dist}`, { story: S.name, start: at(S.name, 1), kind: 'slow touch drag ~80px/s, held, lifted', dist, gesture: () => drag(dist), shot: dist === 300 });
    const half = Math.round(S.gap * 0.6);
    await run(`${S.name}-r1-slowdrag-${half}`, { story: S.name, start: at(S.name, 1), kind: 'slow touch drag ~80px/s, held, lifted', dist: half, note: '0.6 of a step gap', gesture: () => drag(half), shot: S.name === 'lab' });
  }
  await run('statement-slowdrag-300', { start: (g) => g.statement.top, kind: 'slow touch drag ~80px/s, held, lifted', dist: 300, gesture: () => drag(300), shot: true });
  // 5. One gesture, different start points inside one step's band: does it switch or not?
  for (const off of [0, 150, 300, 450, 600]) {
    await run(`lab-r1+${off}-synth-150-1200`, { story: 'lab', start: at('lab', 1, off), kind: 'flick, fling on', dist: 150, speed: 1200, note: `start ${off}px past rest 1`, gesture: () => flickFn(150, 1200, true) });
  }
  // 6. Arriving from above.
  for (const S of geo.stories) {
    await run(`${S.name}-enter-synth-300-1200`, { story: S.name, start: (g) => S_(S.name)(g).top - 500, kind: 'flick, fling on', dist: 300, speed: 1200, gesture: () => flickFn(300, 1200, true), shot: S.name === 'lab' });
    await run(`${S.name}-enter-slowdrag-300`, { story: S.name, start: (g) => S_(S.name)(g).top - 500, kind: 'slow touch drag ~80px/s, held, lifted', dist: 300, gesture: () => drag(300), shot: S.name !== 'tour' });
  }
}

// The proposed controller on the prototype bench (prototype-one-gesture.html: the landing's ScrollStory geometry, a 4-step
// story at 76svh beats like the Lab and a 10-step story at 58svh like the tour), same gestures as on production.
async function protoRuns(tag, variant) {
  const SPEEDS = [400, 1200, 3000, 6000];
  const DISTS = [60, 150, 300, 600];
  const names = geo.stories.map((s) => s.name);
  for (const S of geo.stories) for (let k = 0; k < S.steps; k += 1) {
    await jump(at(S.name, k)(geo));
    const s = await snap();
    results.push({ id: `${tag}-calibrate-${S.name}-${k}`, calibrate: true, y: s.y, step: s.ss[S.index].step, want: k });
  }
  if (variant === 'nolatch') {
    for (const name of names) {
      await run(`${tag}-${name}-enter-flick-600-6000`, { story: name, start: (g) => S_(name)(g).top - 500, kind: 'flick, fling on (no latch)', dist: 600, speed: 6000, gesture: () => flickFn(600, 6000, true), shot: name === names[0] });
      await run(`${tag}-${name}-enter-flick-300-1200`, { story: name, start: (g) => S_(name)(g).top - 500, kind: 'flick, fling on (no latch)', dist: 300, speed: 1200, gesture: () => flickFn(300, 1200, true) });
    }
    return;
  }
  for (const name of names) {
    for (const speed of SPEEDS) for (const dist of DISTS) {
      await run(`${tag}-${name}-r1-flick-${dist}-${speed}`, { story: name, start: at(name, 1), kind: 'flick, fling on', dist, speed, gesture: () => flickFn(dist, speed, true), shot: name === names[1] && dist === 600 && speed === 6000 });
    }
    await run(`${tag}-${name}-r2-flickUp-300-3000`, { story: name, start: at(name, 2), kind: 'flick up, fling on', dist: -300, speed: 3000, gesture: () => flickFn(-300, 3000, true) });
    for (const dist of [40, 150, 300]) await run(`${tag}-${name}-r1-slowdrag-${dist}`, { story: name, start: at(name, 1), kind: 'slow touch drag ~80px/s, held, lifted', dist, gesture: () => drag(dist) });
    await run(`${tag}-${name}-r1-tiny-20`, { story: name, start: at(name, 1), kind: 'tiny touch nudge, held, lifted', dist: 20, gesture: () => drag(20) });
    await run(`${tag}-${name}-r1-twoQuickFlicks`, { story: name, start: at(name, 1), kind: 'two 300px@3000 flicks 150 ms apart', dist: 600, gesture: async () => { await flickFn(300, 3000, true); await sleep(150); await flickFn(300, 3000, true); } });
    await run(`${tag}-${name}-r1-twoFlicks-700ms`, { story: name, start: at(name, 1), kind: 'two 300px@3000 flicks 700 ms apart', dist: 600, gesture: async () => { await flickFn(300, 3000, true); await sleep(700); await flickFn(300, 3000, true); } });
    await run(`${tag}-${name}-enter-flick-600-6000`, { story: name, start: (g) => S_(name)(g).top - 500, kind: 'flick, fling on', dist: 600, speed: 6000, gesture: () => flickFn(600, 6000, true), shot: name === names[0] });
    await run(`${tag}-${name}-enter-flick-300-1200`, { story: name, start: (g) => S_(name)(g).top - 500, kind: 'flick, fling on', dist: 300, speed: 1200, gesture: () => flickFn(300, 1200, true) });
    await run(`${tag}-${name}-enter-slowdrag-300`, { story: name, start: (g) => S_(name)(g).top - 500, kind: 'slow touch drag ~80px/s, held, lifted', dist: 300, gesture: () => drag(300) });
    await run(`${tag}-${name}-exit-flick-300-3000`, { story: name, start: (g) => rest(S_(name)(g), S_(name)(g).steps - 1), kind: 'flick from the last step, fling on', dist: 300, speed: 3000, gesture: () => flickFn(300, 3000, true) });
    await run(`${tag}-${name}-exitUp-flick-300-3000`, { story: name, start: at(name, 0), kind: 'flick up from the first step, fling on', dist: -300, speed: 3000, gesture: () => flickFn(-300, 3000, true) });
  }
}

// Lag: one long constant-speed drag through the statement and the Lab at 4x CPU slowdown (a mid-range phone), with every
// frame's interval and the long animation frames (and their scripts) recorded; then the same with no slowdown.
async function perfRuns() {
  for (const rate of [4, 1]) {
    await cdp.send('Emulation.setCPUThrottlingRate', { rate });
    await jump(geo.statement.top - 600);
    await page.evaluate(() => {
      window.__frames = []; window.__loaf = [];
      let last = performance.now(); let on = true;
      const tick = (t) => { window.__frames.push(+(t - last).toFixed(1)); last = t; if (on) requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
      window.__stopFrames = () => { on = false; };
      try {
        window.__po = new PerformanceObserver((list) => { for (const e of list.getEntries()) window.__loaf.push({ d: Math.round(e.duration), block: Math.round(e.blockingDuration || 0), render: Math.round((e.startTime + e.duration) - (e.renderStart || e.startTime)), scripts: (e.scripts || []).map((s) => `${Math.round(s.duration)}ms ${s.invoker || ''} ${(s.sourceURL || '').split('/').pop()}:${s.sourceFunctionName || ''}`).slice(0, 4) }); });
        window.__po.observe({ type: 'long-animation-frame', buffered: false });
      } catch { window.__loaf.push({ error: 'no LoAF' }); }
    });
    const t0 = Date.now();
    // 4200 px at 1000 px/s, finger held at the end (no fling): synthesized when that works, else six 700 px touch drags.
    if (flickFn === synth) await cdp.send('Input.synthesizeScrollGesture', { x: W / 2, y: 760, yDistance: -4200, speed: 1000, gestureSourceType: 'touch', preventFling: true });
    else for (let i = 0; i < 6; i += 1) await tflick(700, 1000, { fling: false });
    const ms = Date.now() - t0;
    await sleep(600);
    const perf = await page.evaluate(() => { window.__stopFrames(); window.__po?.disconnect(); const f = window.__frames.slice(2); const sorted = [...f].sort((a, b) => a - b); return { frames: f.length, p50: sorted[Math.floor(f.length * 0.5)], p95: sorted[Math.floor(f.length * 0.95)], max: sorted[f.length - 1], over25: f.filter((v) => v > 25).length, over50: f.filter((v) => v > 50).length, loaf: window.__loaf.slice(0, 40), y: Math.round(scrollY) }; });
    results.push({ id: `perf-cpu${rate}x`, gestureMs: ms, ...perf });
    console.log(`perf ${rate}x: moved to ${perf.y} in ${ms} ms; ${perf.frames} frames p50 ${perf.p50} p95 ${perf.p95} max ${perf.max} >25ms ${perf.over25} >50ms ${perf.over50} loaf ${perf.loaf.length}`);
  }
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 1 });
}

function table(rows) {
  const fmtAt = (a) => (a.state === 'held' ? `${a.story} held, phase ${a.phase} (${a.offPx >= 0 ? '+' : ''}${a.offPx}px from rest ${a.nearestRest})` : a.state ? `${a.story} ${a.state}, stage ${a.stageShown}px shown` : a.statementProgress !== undefined ? `statement, progress ${a.statementProgress}` : a.section);
  const lines = ['| id | gesture | start | end | page moved (peak) | step | steps shown on the way | statement words lit+partial | fill after | settle ms | shot |', '|---|---|---|---|---|---|---|---|---|---|---|'];
  for (const r of rows) {
    if (r.calibrate || r.id.startsWith('calibrate')) { lines.push(`| ${r.id} | jump to rest ${r.want} | y ${r.y} | step ${r.step} | | | | | | | |`); continue; }
    const g = `${r.kind}${r.dist != null ? `, ${r.dist}px` : ''}${r.speed ? ` @${r.speed}px/s` : ''}${r.note ? ` (${r.note})` : ''}`;
    const fill = r.fillAfter ? `x${r.fillAfter.x} y${r.fillAfter.y}` : '';
    lines.push(`| ${r.id} | ${g} | y ${r.from.y}: ${fmtAt(r.from.at)} | y ${r.to.y}: ${fmtAt(r.to.at)} | ${r.moved >= 0 ? '+' : ''}${r.moved} (${r.peak}) | ${r.from.step ?? ''}->${r.to.step ?? ''} | ${r.stepsShown.join(',')}${r.otherStories.length ? ` (+${r.otherStories.join(' ')})` : ''} | ${r.words.before} -> ${r.words.after} | ${fill} | ${r.settleMs} | ${r.shot || ''} |`);
  }
  return `${lines.join('\n')}\n`;
}

main().catch((e) => { console.error(e); dropLock(); process.exit(1); });
