import { chromium } from 'playwright';
// usage: render_pages.mjs src.html outstem letter|a4  -> outstem.pdf + outstem-p1.png, -p2.png ... (one PNG per .page)
// Waits for fonts inside iframes too (answer-key pages embed the filled student page).
const [src, stem, size = 'letter'] = process.argv.slice(2);
const S = size === 'a4' ? { w: 794, h: 1123, pw: '210mm', ph: '297mm' } : { w: 816, h: 1056, pw: '8.5in', ph: '11in' };
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--headless=new'] });
const p = await b.newPage({ viewport: { width: S.w, height: S.h }, deviceScaleFactor: 2 });
await p.goto('file://' + src, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
for (const f of p.frames()) { try { await f.evaluate(() => document.fonts.ready); } catch (e) {} }
await p.waitForTimeout(400);
const pages = await p.$$('.page');
for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${stem}-p${i + 1}.png` });
await p.pdf({ path: `${stem}.pdf`, width: S.pw, height: S.ph, printBackground: true });
await b.close(); console.log('rendered', size, pages.length, 'pages');
