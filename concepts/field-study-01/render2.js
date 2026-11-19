const { chromium } = require('playwright'); const fs=require('fs');
(async () => {
  const html=fs.readFileSync('report2.html','utf8').replace('__VALUES__', fs.readFileSync('/home/claude/lcp_values.json','utf8'));
  fs.writeFileSync('report2_built.html',html);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/report2_built.html'); await p.waitForTimeout(600);
  for (let i=1;i<=8;i++){ await p.locator('#p'+i).screenshot({ path:`v${i}.jpg`, type:'jpeg', quality:92 }); }
  await b.close();
})();
