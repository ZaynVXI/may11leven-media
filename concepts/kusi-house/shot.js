const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await p.goto('file://' + __dirname + '/index.html'); await p.waitForTimeout(2200);
  await p.screenshot({ path: 'qa/full.jpg', fullPage: true, quality: 70, type: 'jpeg' });
  for (const [i, y] of [[0, 0], [1, 900], [2, 1900], [3, 2900], [4, 3700]].entries()) { await p.evaluate(y => scrollTo(0, y), y[1]); await p.waitForTimeout(400); await p.screenshot({ path: `qa/v${i}.jpg`, quality: 80, type: 'jpeg' }); }
  console.log(await p.evaluate(() => document.body.scrollHeight)); await b.close();
})();
