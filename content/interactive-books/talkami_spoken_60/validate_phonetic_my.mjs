#!/usr/bin/env node
// Run: node validate_phonetic_my.mjs 47 48
// Optional: node validate_phonetic_my.mjs --all
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const dir = dirname(fileURLToPath(import.meta.url));
const catalog = JSON.parse(readFileSync(join(dir, 'catalog.json'), 'utf8'));
const entries = catalog.zones.flatMap(z => z.themes);
const args = process.argv.slice(2);
if (!args.length) {
  console.error('Usage: node validate_phonetic_my.mjs <theme_id> [theme_id ...] | --all');
  process.exit(2);
}
const ids = args[0] === '--all' ? entries.filter(e => e.status === 'available').map(e => e.theme_id) : args;
let failed = 0;
for (const id of ids) {
  const errors = [];
  const entry = entries.find(e => e.theme_id === id);
  try {
    if (!entry || entry.status !== 'available') throw Error('theme not available');
    const raw = readFileSync(join(dir, 'packs', id + '.json'));
    const pack = JSON.parse(raw.toString('utf8'));
    const src = JSON.parse(readFileSync(join(dir, 'source', id + '.json'), 'utf8'));
    const cards = pack.lessons.flatMap(l => l.phrases);
    const originals = new Map(src.phrases.map(p => [p.id, p]));
    if (cards.length !== entry.phrase_count || cards.length !== originals.size) errors.push('card count mismatch');
    for (const p of cards) {
      if (!p.pinyin?.trim() || !p.phonetic_my?.trim()) {
        errors.push(p.id + ': missing pinyin or phonetic_my'); continue;
      }
      const py = p.pinyin.trim().split(/\s+/);
      const mm = p.phonetic_my.trim().split(/\s+/);
      if (py.length !== mm.length || mm.some(x => !/[\u1000-\u109f]/u.test(x)) || /[A-Za-z]/.test(p.phonetic_my))
        errors.push(p.id + ': Burmese phonetic syllables unpaired or contain Latin letters');
      const srcCard = originals.get(p.id);
      if (!srcCard || JSON.stringify(srcCard) !== JSON.stringify(p))
        errors.push(p.id + ': source/web card mismatch');
    }
    const hash = createHash('sha256').update(raw).digest('hex');
    if (entry.data_sha256 !== hash || entry.data_size !== raw.length) errors.push('catalog SHA-256/size mismatch');
  } catch (e) {
    errors.push(String(e.message || e));
  }
  if (errors.length) { failed++; console.error(id + ': FAIL (' + errors.length + ')\n' + errors.slice(0, 20).join('\n')); }
  else console.log(id + ': PASS - complete pinyin and Burmese phonetics');
}
if (failed) process.exitCode = 1;
