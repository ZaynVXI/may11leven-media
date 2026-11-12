F="../../brand/fonts/"
doubts=[("Instagram is enough.","You rent Instagram.<br>You own your website."),
("Our site works fine.","Open it on a cheap phone.<br>Then wait."),
("People find us on WhatsApp.","Then where do they<br>check you're real?"),
("A website is expensive.","So is every customer<br>who leaves yours."),
("We'll do it later.","Your customers are<br>deciding now."),
("Where do we start?","One page. One price.<br>One button.")]
N=len(doubts)+2
def frame(i,body,cls=""):
    return f'''<section class="s {cls}"><header><span>May11Leven Labs</span><span>Second Thoughts</span><span>No. 01</span></header>{body}<footer><span>Websites</span><span>{i:02d} / {N:02d}</span></footer></section>'''
html=f'''<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:IS;src:url({F}InstrumentSerif-Regular.ttf)}}
@font-face{{font-family:ISI;src:url({F}InstrumentSerif-Italic.ttf)}}
@font-face{{font-family:IT;src:url({F}InterTight-Light.ttf);font-weight:300}}
@font-face{{font-family:IT;src:url({F}InterTight-Regular.ttf);font-weight:400}}
@font-face{{font-family:PM;src:url({F}PlexMono.ttf)}}
*{{margin:0;box-sizing:border-box}}body{{background:#000}}
.s{{width:1080px;height:1350px;position:relative;background:#141213;color:#ECEAE4;overflow:hidden}}
.s.ir{{background:#FF4A1C;color:#141213}} .s.bone{{background:#ECEAE4;color:#141213}}
header,footer{{position:absolute;left:32px;right:32px;display:flex;justify-content:space-between;font:400 15px/1 PM;letter-spacing:.08em;text-transform:uppercase}}
header{{top:32px;padding-bottom:14px;border-bottom:1px solid currentColor}}
footer{{bottom:32px;padding-top:14px;border-top:1px solid currentColor;opacity:.75}}
header span::before{{content:"■ "}} .s:not(.ir) header span::before{{color:#FF4A1C}}
.lab{{position:absolute;left:32px;font:400 15px/1 PM;letter-spacing:.08em;text-transform:uppercase;opacity:.6}}
.d{{position:absolute;left:312px;right:48px;top:188px;font:400 104px/.98 IS;letter-spacing:-.01em}}
.a{{position:absolute;left:370px;right:48px;top:820px;font:300 46px/1.18 IT;letter-spacing:-.015em;}}
.a i{{position:absolute;left:-58px;font-style:normal}}
.big{{position:absolute;left:32px;right:32px;top:300px;font:400 220px/.86 IS;letter-spacing:-.02em}}
.big em{{font-family:ISI;font-style:normal}}
.sub{{position:absolute;left:312px;top:860px;font:300 46px/1.18 IT;letter-spacing:-.015em}}
</style>'''
html+=frame(1,'<div class="lab" style="top:230px">Issue 01</div><div class="big">Second<br><em>Thoughts</em></div><div class="lab" style="top:878px">Websites</div><div class="sub">Six doubts before<br>you build a website.</div>',"ir")
for k,(d,a) in enumerate(doubts):
    html+=frame(k+2,f'<div class="lab" style="top:226px">Doubt {k+1:02d}</div><div class="d">{d}</div><div class="lab" style="top:838px">Answer</div><div class="a"><i>→</i>{a}</div>')
html+=frame(N,'<div class="lab" style="top:226px">May11Leven Labs</div><div class="d">Websites that load, show a price and take the booking.</div><div class="lab" style="top:838px">Next</div><div class="a"><i>→</i>Comment 11.<br>We\'ll look at yours, free.</div>',"bone")
open("slides.html","w").write(html)
