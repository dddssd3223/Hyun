// 우리 자료의 문항 요소를 그대로 캡처: node cap.js <html> <n> <out.png> [kind]
// kind: q (시험지·모의고사 .q), it (문제집 빈칸/OX .it), fq (문제집 자료 .fq)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const jobs = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch();
  const pages = {};
  for (const j of jobs) {
    if (!pages[j.file]) {
      const p = await b.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 2.5 });
      await p.goto('file://' + j.file, { waitUntil: 'networkidle' });
      if (await p.$('script')) { try { await p.waitForSelector('body[data-ready="1"]', { timeout: 15000 }); } catch (e) {} }
      await p.waitForTimeout(300);
      pages[j.file] = p;
    }
    const p = pages[j.file];
    const h = await p.evaluateHandle(({ kind, n }) => {
      if (kind === 'q') return Array.from(document.querySelectorAll('.q')).find(q => { const x = q.querySelector('.no'); return x && x.textContent.replace(/\D/g, '') === String(n); });
      if (kind === 'it') return Array.from(document.querySelectorAll('.it')).find(q => { const x = q.querySelector('.n'); return x && x.textContent.replace(/\D/g, '') === String(n); });
      if (kind === 'fq') return Array.from(document.querySelectorAll('.fq')).find(q => { const x = q.querySelector('.fn'); return x && x.textContent.replace(/\D/g, '') === String(n); });
    }, { kind: j.kind, n: j.n });
    const el = h.asElement();
    if (!el) { console.log('MISSING', j.file, j.kind, j.n); continue; }
    await el.screenshot({ path: j.out });
    console.log('ok', j.out);
  }
  await b.close();
})();
