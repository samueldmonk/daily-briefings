# -*- coding: utf-8 -*-
import re,html
D='/tmp/db_1787854887/'
def tldr(f):
    s=open(D+f,encoding='utf-8').read()
    m=re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>',s,re.S)
    return m.group(1).strip()
cy,ws,mm = tldr('cyber-briefing.html'), tldr('wallstreet-briefing.html'), tldr('mma-briefing.html')
s=open(D+'index.html',encoding='utf-8').read()
def rep(old,new,n=1):
    global s
    c=s.count(old); assert c==n,"count %d :: %s"%(c,old[:80]); s=s.replace(old,new)

# headlines
rep("<h3>Oracle's deadline expires today — and the ATF confirms a breach</h3>",
    "<h3>Oracle's deadline expires today — and a prompt-injection hole opens in Amazon's agentic IDE</h3>")
rep("<h3>The rally re-accelerates: the Nasdaq adds more than 400 points</h3>",
    "<h3>Tech is carrying the tape alone, and the S&amp;P 500's gain has doubled</h3>")
rep("<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>",
    "<h3>Shanghai fight week — and Noche UFC's replacement headliner finds a home</h3>")

# card bodies -> byte-identical to each page's tldr
for old_marker,new in ((' class="card c-cy"',cy),(' class="card c-ws"',ws),(' class="card c-mm"',mm)):
    i=s.index(old_marker); j=s.index('<p>',i); k=s.index('</p>',j)
    s=s[:j]+'<p>'+new+s[k:]
open(D+'index.html','w',encoding='utf-8').write(s)

# assert sync
t=open(D+'index.html',encoding='utf-8').read()
for name,v in (('cy',cy),('ws',ws),('mm',mm)):
    assert '<p>'+v+'</p>' in t, "index card not synced: "+name
print("index synced OK")
