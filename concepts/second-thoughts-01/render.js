const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+process.cwd()+'/slides.html');await p.waitForTimeout(800);
const s=await p.$$('.s');for(let i=0;i<s.length;i++){await s[i].screenshot({path:`st${String(i+1).padStart(2,'0')}.png`});}
await b.close()})();
