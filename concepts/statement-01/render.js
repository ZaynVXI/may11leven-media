const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
await p.goto('file://'+process.cwd()+'/statement.html');await p.waitForTimeout(1200);
for(let i=1;i<=9;i++){await (await p.$('#p'+i)).screenshot({path:'s'+i+'.png'});}await b.close()})();
