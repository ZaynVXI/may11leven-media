"""May11Leven Labs document system: invoice, proposal, contract (A4).
Layout learned from the editorial invoice/proposal/contract set Zayn shared (brand/refs/documents/):
a quiet header grid of label/value pairs, one oversized word, hairlines, generous air.
Ours: the 11 mark and wordmark, Inter Tight, Plex Mono for every figure and reference, Infrared only on the mark.
Fill the dicts at the bottom (or import build() and pass your own), then: python3 build.py  -> PDFs in out/.
Square-bracket values are placeholders to replace before sending."""
import json, subprocess, pathlib, html
HERE = pathlib.Path(__file__).parent
F = HERE.parent.parent / "fonts"
LOGO = (HERE.parent.parent / "figma" / "may11leven-logo-dark.svg").read_text()
esc = html.escape

STUDIO = {
    "name": "May11Leven Labs",
    "lines": ["[Legal name]", "hello@may11levenlabs.com", "may11levenlabs.com", "[Street address]", "[Postcode, City, Country]", "[VAT or tax ID]"],
    "short": ["May11Leven Labs", "hello@may11levenlabs.com", "may11levenlabs.com"],
}

CSS = f"""
@font-face{{font-family:IT;src:url(file://{F}/InterTight-Light.ttf);font-weight:300}}
@font-face{{font-family:IT;src:url(file://{F}/InterTight-Regular.ttf);font-weight:400}}
@font-face{{font-family:IT;src:url(file://{F}/InterTight-Medium.ttf);font-weight:500}}
@font-face{{font-family:PM;src:url(file://{F}/PlexMono.ttf)}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:IT;font-weight:400;color:#141213;-webkit-font-smoothing:antialiased}}
.page{{width:210mm;height:297mm;padding:17mm 17mm 14mm;position:relative;page-break-after:always;background:#fff;display:flex;flex-direction:column}}
.head{{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm}}
.brand svg{{height:7.2mm;width:auto;display:block}}
.sub{{font-size:17pt;font-weight:300;color:#7A7672;margin-top:4.5mm;letter-spacing:-.01em;line-height:1.15}}
.kv{{display:grid;grid-template-columns:1fr 1fr;row-gap:7mm;font-size:8.6pt;line-height:1.42}}
.kv .k{{color:#7A7672}}
.mono{{font-family:PM;font-size:8pt;letter-spacing:.01em}}
.big{{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;column-gap:8mm;align-items:end}}
.big .w{{font-size:70pt;font-weight:500;letter-spacing:-.055em;line-height:.8;text-align:right;padding-bottom:1mm}}
.big .mark{{font:400 7.4pt PM;color:#7A7672;letter-spacing:.06em;text-transform:uppercase;align-self:end}}
hr{{border:0;border-top:.25mm solid #E4E1DC;margin:6mm 0}}
.rows{{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm;row-gap:5mm;font-size:8.8pt;line-height:1.6}}
.rows .k{{font-weight:500}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;font-size:7.2pt;color:#141213;padding-top:6mm}}
.foot .c{{font-family:PM;color:#7A7672;font-size:6.8pt;letter-spacing:.04em}}
table{{width:100%;border-collapse:collapse;font-size:8.8pt}}
th{{text-align:left;font-weight:500;padding:0 0 3mm}}
td{{padding:1.6mm 0;vertical-align:top}}
.r{{text-align:right}}
.num{{font-family:PM;font-size:8.2pt}}
.tot{{display:grid;grid-template-columns:1fr auto auto;column-gap:10mm;font-size:8.8pt;row-gap:1.4mm;margin-top:6mm}}
.tot .grand{{font-size:12.5pt;font-weight:500;margin-top:2mm}}
.small{{font-size:7.4pt;line-height:1.55;color:#141213}}
h2{{font-size:17pt;font-weight:300;letter-spacing:-.015em;margin-bottom:5mm}}
.clause{{display:grid;grid-template-columns:12mm 1fr 2fr;column-gap:6mm;font-size:8.6pt;line-height:1.6;padding:3.2mm 0;border-top:.25mm solid #E4E1DC}}
.clause .n{{font-family:PM;font-size:7.6pt;color:#7A7672;padding-top:.6mm}}
.clause .t{{font-weight:500}}
.sig{{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm;margin-top:10mm;font-size:8.6pt}}
.sig .line{{border-top:.25mm solid #141213;margin-top:16mm;padding-top:2mm}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);column-gap:5mm;font-size:8.4pt;line-height:1.5}}
.steps .n{{font-family:PM;font-size:7.4pt;color:#FF4A1C}}
.steps .t{{font-size:12pt;font-weight:400;margin:2mm 0 1.5mm;letter-spacing:-.01em}}
.pay .kv{{row-gap:1.6mm}}
.ph{{background:#FFF3EE}}
"""

def mark_ph(s):
    """Highlight [placeholders] softly so nothing goes out unfilled."""
    out = esc(s)
    import re
    return re.sub(r"\[([^\]]+)\]", r'<span class="ph">[\1]</span>', out)

def kv(pairs):
    return '<div class="kv">' + "".join(f'<div class="k">{"<br>".join(esc(x) for x in k.split(chr(10)))}</div><div>{"<br>".join(mark_ph(x) for x in (v if isinstance(v, list) else [v]))}</div>' for k, v in pairs) + "</div>"

def header(sub, pairs, word, ref):
    return f'''<div class="head"><div class="brand">{LOGO}<div class="sub">{esc(sub)}</div></div>{kv(pairs)}</div>
<div class="big" style="margin-top:22mm"><div class="mark">{esc(ref)}</div><div class="w">{esc(word)}</div></div><hr>'''

def foot(i, n, ref):
    return f'<div class="foot"><span>May11Leven Labs</span><span class="c">{esc(ref)}</span><span>Page {i} of {n}</span></div>'

def page(inner):
    return f'<section class="page">{inner}</section>'

def rows(pairs):
    return '<div class="rows">' + "".join(f'<div class="k">{esc(k)}</div><div>{mark_ph(v)}</div>' for k, v in pairs) + "</div>"

# ---------------- invoice
def invoice(d):
    lines = "".join(f'<tr><td>{mark_ph(a)}</td><td class="num">{esc(q)}</td><td class="r num">{esc(t)}</td></tr>' for a, q, t in d["lines"])
    tot = "".join(f'<span></span><span>{esc(k)}</span><span class="r num">{esc(v)}</span>' for k, v in d["totals"])
    pay = kv([(k, v) for k, v in d["payment"]])
    body = f'''{header(f"Invoice {d['number']}", [("From", STUDIO["lines"]), ("Billed to", d["client"]), ("Invoice date\nDue date\nProject", [d['date'], d['due'], d['project']])], "Invoice", d["number"])}
<table><tr><th style="width:50%">Service</th><th>Quantity × rate</th><th class="r">Amount {esc(d["currency"])}</th></tr>{lines}</table>
<div class="tot">{tot}<span></span><span class="grand">Total {esc(d["currency"])}</span><span class="grand r num" style="font-size:12pt">{esc(d["total"])}</span></div>
<hr><div style="font-size:8.6pt;font-weight:500;margin-bottom:3mm">Payment details</div><div style="width:60%" class="pay">{pay}</div>
<div style="margin-top:auto" class="small"><b>Terms.</b> {mark_ph(d["terms"])}</div>{foot(1, 1, d["number"])}'''
    return [page(body)]

# ---------------- proposal
def proposal(d):
    p1 = f'''{header(d["title"], [("Prepared by", STUDIO["short"]), ("For", d["client"]), ("Reference\nDate", [d["ref"], d["date"]])], "Proposal", d["ref"])}
{rows([("Project", d["project"]), ("The problem", d["problem"]), ("Overview", d["overview"])])}{foot(1, 3, d["ref"])}'''
    deliv = "".join(f'<div class="clause"><span class="n">{i+1:02d}</span><span class="t">{esc(a)}</span><span>{mark_ph(b)}</span></div>' for i, (a, b) in enumerate(d["deliverables"]))
    steps = "".join(f'<div><div class="n">{i+1:02d}</div><div class="t">{esc(a)}</div><div>{mark_ph(b)}</div></div>' for i, (a, b) in enumerate(d["process"]))
    p2 = f'''<h2>What we will make</h2>{deliv}<div style="border-top:.25mm solid #E4E1DC"></div>
<h2 style="margin-top:12mm">How we work</h2><div class="steps">{steps}</div>{foot(2, 3, d["ref"])}'''
    inv = "".join(f'<tr><td>{mark_ph(a)}</td><td class="num">{esc(b)}</td><td class="r num">{esc(c)}</td></tr>' for a, b, c in d["investment"])
    nxt = "".join(f'<div class="clause"><span class="n">{i+1:02d}</span><span class="t">{esc(a)}</span><span>{mark_ph(b)}</span></div>' for i, (a, b) in enumerate(d["next"]))
    p3 = f'''<h2>Investment</h2><table><tr><th style="width:50%">Item</th><th>Timing</th><th class="r">Amount {esc(d["currency"])}</th></tr>{inv}</table>
<div class="tot"><span></span><span class="grand">Total {esc(d["currency"])}</span><span class="grand r num" style="font-size:12pt">{esc(d["total"])}</span></div>
<p class="small" style="margin-top:4mm;color:#7A7672">{mark_ph(d["price_note"])}</p>
<h2 style="margin-top:14mm">Next steps</h2>{nxt}<div style="border-top:.25mm solid #E4E1DC"></div>
<p class="small" style="margin-top:6mm">This proposal is valid for {esc(d["valid"])}. A full contract follows once you confirm.</p>{foot(3, 3, d["ref"])}'''
    return [page(p1), page(p2), page(p3)]

# ---------------- contract
def contract(d):
    cl = d["clauses"]; first, rest = cl[:6], cl[6:]
    def block(items, start):
        return "".join(f'<div class="clause"><span class="n">{start+i:02d}</span><span class="t">{esc(a)}</span><span>{mark_ph(b)}</span></div>' for i, (a, b) in enumerate(items))
    n = 3
    p1 = f'''{header(d["title"], [("Studio", STUDIO["lines"][:3] + STUDIO["lines"][3:5]), ("Client", d["client"]), ("Reference\nDate", [d["ref"], d["date"]])], "Contract", d["ref"])}
{rows([("Parties", d["parties"]), ("Project", d["project"])])}{foot(1, n, d["ref"])}'''
    p2 = f'''<h2>Terms</h2>{block(first, 1)}<div style="border-top:.25mm solid #E4E1DC"></div>{foot(2, n, d["ref"])}'''
    p3 = f'''<h2>Terms, continued</h2>{block(rest, 7)}<div style="border-top:.25mm solid #E4E1DC"></div>
<div class="sig"><div><div class="line">For May11Leven Labs<br><span style="color:#7A7672">Name, role, date</span></div></div>
<div><div class="line">For {mark_ph(d["client"][0])}<br><span style="color:#7A7672">Name, role, date</span></div></div></div>{foot(3, n, d["ref"])}'''
    return [page(p1), page(p2), page(p3)]

def render(name, pages):
    out = HERE / "out"; out.mkdir(exist_ok=True)
    src = out / f"{name}.html"
    src.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{src}');await p.waitForTimeout(600);await p.pdf({{path:'{out}/{name}.pdf',format:'A4',printBackground:true}});
await p.setViewportSize({{width:794,height:1123}});const els=await p.$$('.page');
for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{out}/{name}-p'+(i+1)+'.png'}});await b.close()}})()"""
    subprocess.run(["node", "-e", js], check=True)

if __name__ == "__main__":
    data = json.loads((HERE / "sample.json").read_text())
    render("invoice", invoice(data["invoice"]))
    render("proposal", proposal(data["proposal"]))
    render("contract", contract(data["contract"]))
    print("done")
