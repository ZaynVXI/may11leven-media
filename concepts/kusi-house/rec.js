const { chromium } = require('playwright'); const fs=require('fs');
(async () => {
  fs.rmSync('frames',{recursive:true,force:true}); fs.mkdirSync('frames');
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1.5 });
  await p.addInitScript(() => { window.__clock = 0; });
  await p.goto('file://' + __dirname + '/index.html'); await p.waitForTimeout(800);
  const H = await p.evaluate(() => document.body.scrollHeight - innerHeight);
  const fps=30, ease=t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;
  // keyframes: [time s, scrollY]
  const arrivalY = await p.evaluate(()=>document.querySelector('.arrival').offsetTop-90);
  const roomsY = await p.evaluate(()=>document.querySelector('.rooms').offsetTop-60);
  const directY = await p.evaluate(()=>document.querySelector('.direct').offsetTop);
  const K=[[0,0],[3.0,0],[5.6,arrivalY],[7.0,arrivalY],[9.2,roomsY],[10.4,roomsY],[12.2,directY],[13.2,directY],[15.4,H],[17.4,H]];
  const T=K[K.length-1][0]; let i=0;
  for(let t=0;t<=T;t+=1/fps,i++){
    let y=0; for(let k=0;k<K.length-1;k++){ const [t0,y0]=K[k],[t1,y1]=K[k+1]; if(t>=t0&&t<=t1){ y=y0+(y1-y0)*ease((t-t0)/(t1-t0)); break; } }
    await p.evaluate(([y,c])=>{ window.__clock=c; scrollTo(0,y); }, [y, t*1000]);
    await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
    await p.screenshot({ path: `frames/f${String(i).padStart(4,'0')}.jpg`, quality: 92, type:'jpeg' });
  }
  console.log('frames',i,'H',H); await b.close();
})();
