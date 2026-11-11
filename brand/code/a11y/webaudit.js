const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch();const out=[];
 for (const f of process.argv.slice(2)){
  const html=fs.readFileSync(f,'utf8');
  const ids=[...html.matchAll(/class="scr[^"]*" id="([^"]+)"/g)].map(m=>m[1]);
  const hashes=ids.length?ids:[''];
  for(const h of hashes){
   const p=await b.newPage({viewport:{width:1440,height:900}});
   await p.goto('file://'+f+(h?'#'+h:''));await p.waitForTimeout(300);
   const r=await p.evaluate(()=>{
    const L=c=>{const v=c.map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4});return .2126*v[0]+.7152*v[1]+.0722*v[2]};
    const P=s=>{const m=s.match(/[\d.]+/g);return m?m.map(Number):null};
    const bgOf=el=>{while(el){const s=getComputedStyle(el);const c=P(s.backgroundColor);if(c&&(c.length<4||c[3]>0.5))return c.slice(0,3);if(el.tagName==='IMG')return null;el=el.parentElement}return [255,255,255]};
    const res=[];
    for(const el of document.querySelectorAll('body *')){
      const isSvg=el instanceof SVGElement;if(!isSvg&&!el.offsetParent&&getComputedStyle(el).position!=='fixed')continue;if(isSvg&&el.tagName.toLowerCase()!=='text'&&el.tagName.toLowerCase()!=='tspan')continue;
      const t=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim();if(!t)continue;
      const s=getComputedStyle(el);const fg=P(isSvg?s.fill:s.color);let op=1,e=el;while(e){op*=+getComputedStyle(e).opacity;e=e.parentElement}
      const bg=bgOf(el);if(!bg)continue;
      const fgc=fg.slice(0,3).map((v,i)=>v*(fg[3]!==undefined?fg[3]:1)*op+bg[i]*(1-(fg[3]!==undefined?fg[3]:1)*op));
      const a=L(fgc),bb=L(bg);const ratio=(Math.max(a,bb)+.05)/(Math.min(a,bb)+.05);
      const sz=parseFloat(s.fontSize),wt=+s.fontWeight;const large=sz>=24||(sz>=18.66&&wt>=700);
      const need=large?3:4.5;
      if(ratio<need||sz<12)res.push({t:t.slice(0,30),sz,ratio:+ratio.toFixed(2),need,fg:s.color,bg:'rgb('+bg+')'});
    }return res});
   r.forEach(x=>out.push({file:f.split('/').slice(-2).join('/'),scr:h,...x}));await p.close();
  }}
 console.log(JSON.stringify(out,null,0).replace(/},{/g,'},\n{'));await b.close();
})();
