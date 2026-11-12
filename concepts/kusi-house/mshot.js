const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3 });
  await p.addInitScript(() => { window.__clock = 99999; });
  await p.goto('file://' + __dirname + '/index.html'); await p.waitForTimeout(600);
  const tops = await p.evaluate(()=>({arr:document.querySelector('.arrival .txt').offsetTop-90, rooms:document.querySelector('.room').offsetTop-80, direct:document.querySelector('.direct').offsetTop}));
  const shots=[['m_hero',0],['m_arrival',tops.arr],['m_room',tops.rooms],['m_direct',tops.direct]];
  for (const [n,y] of shots){ await p.evaluate(y=>scrollTo(0,y),y); await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))); await p.waitForTimeout(900); await p.screenshot({path:`qa/${n}.png`}); }
  await b.close();
})();
