// Summarize results-<name>.json files from probe.mjs: per story, per gesture family, how many steps each gesture moved,
// whether it stopped off a resting place, and how many steps flashed by on the way.
//   node summarize.mjs main proto proto-nolatch perf
import { readFileSync, existsSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const OUT = 'C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/scroll';
const names = process.argv.slice(2);
const lines = [];
const say = (s = '') => { lines.push(s); console.log(s); };

for (const name of names) {
  const file = join(OUT, `results-${name}.json`);
  if (!existsSync(file)) { say(`## ${name}: missing`); continue; }
  const data = JSON.parse(readFileSync(file, 'utf8'));
  say(`## ${name} (${data.base}, ${data.viewport}, flick rows: ${data.flick || 'n/a'})`);
  if (name === 'perf') {
    for (const r of data.results) say(`- ${r.id}: moved to y ${r.y} in ${r.gestureMs} ms; ${r.frames} frames, p50 ${r.p50} ms, p95 ${r.p95} ms, max ${r.max} ms, >25 ms ${r.over25}, >50 ms ${r.over50}, long animation frames ${r.loaf?.length ?? 0}${r.loaf?.length ? `; top: ${r.loaf.slice().sort((a, b) => (b.d || 0) - (a.d || 0)).slice(0, 3).map((l) => `${l.d}ms [${(l.scripts || []).join(' | ')}]`).join(' ; ')}` : ''}`);
    continue;
  }
  const cal = data.results.filter((r) => r.calibrate || String(r.id).includes('calibrate') || r.id === 'synth-check');
  const bad = cal.filter((r) => r.want !== undefined && typeof r.want === 'number' && r.step !== r.want);
  say(`calibration: ${cal.length} rows, ${bad.length} off (${bad.map((r) => `${r.id} got ${r.step}`).join(', ')})`);
  const synthCheck = cal.find((r) => r.id === 'synth-check');
  if (synthCheck) say(`synth check: ${synthCheck.step}`);
  const rows = data.results.filter((r) => !(r.calibrate || String(r.id).includes('calibrate') || r.id === 'synth-check'));
  const fam = (r) => {
    const id = r.id.replace(/^proto(-nolatch)?-/, '');
    if (/enter/.test(id)) return 'enter from 500 px above';
    if (/exitUp/.test(id)) return 'exit up from first step';
    if (/exit/.test(id)) return 'exit from last step';
    if (/\+\d+/.test(id)) return 'same flick, start offset';
    if (/two/.test(id)) return 'two flicks';
    if (/Up/.test(id)) return 'flick up';
    if (/slowdrag|tiny/.test(id)) return 'slow drag';
    if (/NoFling/.test(id)) return 'drag, no fling';
    if (/touch-/.test(id)) return 'touch-event flick';
    return 'flick';
  };
  const groups = new Map();
  for (const r of rows) {
    const key = `${r.story || 'statement'} | ${fam(r)}`;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(r);
  }
  for (const [key, list] of groups) {
    if (key.startsWith('statement')) {
      say(`- ${key}: ${list.map((r) => `${r.dist}px${r.speed ? `@${r.speed}` : ''} -> moved ${r.moved}, words ${r.words.after}, ${r.to.at.statementProgress !== undefined ? `progress ${r.to.at.statementProgress}` : r.to.at.section}`).join('; ')}`);
      continue;
    }
    const deltas = list.map((r) => r.stepDelta);
    const hist = {};
    for (const d of deltas) hist[d] = (hist[d] || 0) + 1;
    const off = list.filter((r) => r.to.at.state === 'held' && Math.abs(r.to.at.offPx) > 3).length;
    const left = list.filter((r) => r.to.at.state && r.to.at.state !== 'held').length;
    const outside = list.filter((r) => !r.to.at.state).length;
    const flashed = list.filter((r) => r.stepsShown.length > 2).length;
    say(`- ${key}: ${list.length} gestures; step change histogram ${JSON.stringify(hist)}; stopped off a resting place ${off}; story partly off screen ${left}; left the story ${outside}; >1 step shown on the way ${flashed}`);
    for (const r of list) say(`    ${r.id}: y ${r.from.y}->${r.to.y} (${r.moved >= 0 ? '+' : ''}${r.moved}), step ${r.from.step}->${r.to.step}, shown [${r.stepsShown}]${r.otherStories?.length ? ` +${r.otherStories.join(',')}` : ''}, end ${r.to.at.state ? `${r.to.at.state}${r.to.at.state === 'held' ? ` phase ${r.to.at.phase} off ${r.to.at.offPx}` : ` stage ${r.to.at.stageShown}px`}` : r.to.at.section}${r.fillAfter ? `, fill x${r.fillAfter.x}/y${r.fillAfter.y}` : ''}`);
  }
}
writeFileSync(join(OUT, `summary-${names.join('-')}.txt`), `${lines.join('\n')}\n`);
