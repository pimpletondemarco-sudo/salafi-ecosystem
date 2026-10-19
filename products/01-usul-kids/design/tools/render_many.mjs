// Renders single-page worksheets to PNG (2x) + PDF. X.html -> X.png + X-letter.pdf ; X-a4.html -> X-a4.png + X-a4.pdf
// usage: PW_DIR=<dir with node_modules/playwright>/ node render_many.mjs page.html [page2.html ...]
import { createRequire } from 'module';
const require = createRequire(process.env.PW_DIR || '/opt/node-tools/');
const { chromium } = require('playwright');
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--headless=new'] });
for (const src of process.argv.slice(2)) {
  const a4 = src.endsWith('-a4.html');
  const S = a4 ? { w: 794, h: 1123, pw: '210mm', ph: '297mm' } : { w: 816, h: 1056, pw: '8.5in', ph: '11in' };
  const p = await b.newPage({ viewport: { width: S.w, height: S.h }, deviceScaleFactor: 2 });
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const stem = src.replace(/\.html$/, '');
  await p.screenshot({ path: stem + '.png' });
  await p.pdf({ path: a4 ? stem + '.pdf' : stem + '-letter.pdf', width: S.pw, height: S.ph, printBackground: true });
  await p.close(); console.log('rendered', stem);
}
await b.close();
