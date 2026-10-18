// Screenshots each Arabic text element on a page three ways, for check_arabic.py:
//  solo   = only this element visible (its true ink)
//  free   = only this element visible, with every overflow/clip turned off (ink if nothing clipped it)
//  others = everything except this element (the ink it could collide with)
// usage: node arabic_snap.mjs page.html outdir letter|a4
import { createRequire } from 'module';
const require = createRequire(process.env.PW_DIR || '/tmp/claude-0/-home-user-salafi-ecosystem/67afafd4-b7b3-56b1-8a23-be9fbee95a90/scratchpad/pw/');
const { chromium } = require('playwright');
import fs from 'fs';
const [src, out, size = 'letter'] = process.argv.slice(2);
const S = size === 'a4' ? { w: 794, h: 1123 } : { w: 816, h: 1056 };
fs.mkdirSync(out, { recursive: true });
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--headless=new'] });
const p = await b.newPage({ viewport: { width: S.w, height: S.h * 3 }, deviceScaleFactor: 2 });
await p.goto('file://' + src, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
const items = await p.evaluate(() => {
  const ar = /[؀-ۿﭐ-﷿ﹰ-﻿]/;
  const els = [];
  document.querySelectorAll('body *').forEach(el => {
    if (['SCRIPT', 'STYLE'].includes(el.tagName)) return;
    const drawn = el.hasAttribute('data-ar');   // Arabic drawn as shapes (tracing words)
    if (!drawn) {
      if (el.tagName.toLowerCase() === 'svg') return;
      if (el.closest('svg') && el.tagName.toLowerCase() !== 'text') return;
    }
    const own = drawn ? '[drawn ' + el.getAttribute('data-ar') + ' word]' : [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('');
    if (!drawn && !ar.test(own)) return;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) return;
    el.setAttribute('data-arq', String(els.length));
    const cs = getComputedStyle(el);
    const pgEl = el.closest('.page') || document.body; const pr = pgEl.getBoundingClientRect();
    els.push({ i: els.length, text: own.trim().slice(0, 60), x: r.x, y: r.y, w: r.width, h: r.height,
               fs: parseFloat(cs.fontSize), lh: cs.lineHeight, pg: { x: pr.x, y: pr.y, w: pr.width, h: pr.height } });
  });
  // anything that pokes out of its page (e.g. a footer pushed off the bottom)
  const overflow = [];
  document.querySelectorAll('.page').forEach((pgEl, k) => {
    const pr = pgEl.getBoundingClientRect();
    pgEl.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height || el.closest('svg') && el.tagName.toLowerCase() !== 'svg') return;
      if (r.bottom > pr.bottom + 0.5 || r.right > pr.right + 0.5 || r.top < pr.top - 0.5 || r.left < pr.left - 0.5)
        overflow.push({ page: k + 1, tag: el.tagName.toLowerCase(), cls: el.className && el.className.baseVal === undefined ? el.className : '',
                        text: (el.textContent || '').trim().slice(0, 50), by: Math.round(Math.max(r.bottom - pr.bottom, r.right - pr.right, pr.top - r.top, pr.left - r.left)) });
    });
  });
  const pg = document.querySelector('.page') || document.body;
  const pr = pg.getBoundingClientRect();
  return { els, overflow, page: { x: pr.x, y: pr.y, w: pr.width, h: pr.height } };
});
await p.addStyleTag({ content: `.__solo body * { visibility: hidden !important; }
  .__solo [data-arq].__on, .__solo [data-arq].__on * { visibility: visible !important; }
  .__solo, .__solo body, .__solo .page { background: #fff !important; }
  .__free * { overflow: visible !important; clip-path: none !important; contain: none !important; }
  .__others [data-arq].__on, .__others [data-arq].__on * { visibility: hidden !important; }` });
for (const e of items.els) {
  const pad = Math.max(24, e.fs * 1.2);
  const clip = { x: Math.max(0, e.x - pad), y: Math.max(0, e.y - pad), width: e.w + 2 * pad, height: e.h + 2 * pad };
  e.clip = clip;
  for (const mode of ['solo', 'free', 'others']) {
    await p.evaluate(([i, mode]) => {
      document.documentElement.className = mode === 'free' ? '__solo __free' : '__' + mode;
      document.querySelectorAll('[data-arq]').forEach(n => n.classList.toggle('__on', n.getAttribute('data-arq') === String(i)));
    }, [e.i, mode]);
    await p.screenshot({ path: `${out}/${e.i}-${mode}.png`, clip });
  }
}
fs.writeFileSync(`${out}/index.json`, JSON.stringify(items));
await b.close();
