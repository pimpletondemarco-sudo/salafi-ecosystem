import { chromium } from 'playwright';
// usage: render2.mjs src.html out.png out.pdf letter|a4
const [src, png, pdf, size = 'letter'] = process.argv.slice(2);
const S = size === 'a4' ? { w: 794, h: 1123, pw: '210mm', ph: '297mm' } : { w: 816, h: 1056, pw: '8.5in', ph: '11in' };
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--headless=new'] });
const p = await b.newPage({ viewport: { width: S.w, height: S.h }, deviceScaleFactor: 2 });
await p.goto('file://' + src, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
await p.screenshot({ path: png });
await p.pdf({ path: pdf, width: S.pw, height: S.ph, printBackground: true });
await b.close(); console.log('rendered', size);
