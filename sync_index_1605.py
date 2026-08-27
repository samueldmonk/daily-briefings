import re,sys
def tldr(p):
    h=open(p).read()
    m=re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>',h,re.S)
    if not m: sys.exit("no tldr "+p)
    return m.group(1)
cy,ws,mm=tldr('cyber-briefing.html'),tldr('wallstreet-briefing.html'),tldr('mma-briefing.html')
h=open('index.html').read()
heads={'c-cy':("The Oracle deadline has expired — Citrix on Saturday is now the top of the board",cy),
       'c-ws':("The bell has rung: Nasdaq +1.31%, S&amp;P +0.66% — and only 156 of 503 stocks higher",ws),
       'c-mm':("Sacramento&rsquo;s Fight of the Night winners were both suspended six months",mm)}
n=0
for cls,(hd,summ) in heads.items():
    pat=re.compile(r'(<div class="card '+cls+r'"><div class="lbl">.*?</div>\n)<h3>.*?</h3>\n<p>.*?</p>',re.S)
    m=pat.search(h)
    if not m: sys.exit("card not found "+cls)
    h=h[:m.start()]+m.group(1)+'<h3>'+hd+'</h3>\n<p>'+summ+'</p>'+h[m.end():]
    n+=1
open('index.html','w').write(h)
print("index cards synced:",n)
# verify byte-identical
h=open('index.html').read()
for cls,txt in (('c-cy',cy),('c-ws',ws),('c-mm',mm)):
    assert txt in h, "MISMATCH "+cls
print("VERIFIED: all three index cards byte-identical to their page tldr")
