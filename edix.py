# -*- coding: utf-8 -*-
import io,re
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1; return h.replace(old,new)

# pull the canonical summary sentences straight out of the briefings so they cannot drift
def tldr(f):
    h=load(f)
    m=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>',h,re.S)
    assert m, f
    return m.group(1)

cy,ws,mm = tldr('cyber-briefing.html'), tldr('wallstreet-briefing.html'), tldr('mma-briefing.html')
ix=load('index.html')

# replace the three card paragraphs with the byte-identical summaries
for old_marker,new_text in ((' <p>An unpatched Magento',cy),):
    pass

def swap_card(h, anchor, new_text):
    i=h.find(anchor); assert i>0, anchor
    s=h.find('<p>',i); e=h.find('</p>',s)+4
    return h[:s]+'<p>'+new_text+'</p>'+h[e:]

ix=swap_card(ix,'The Cyber Wire &middot; The Wire',cy)
ix=swap_card(ix,'The Closing Bell &middot; The Tape',ws)
ix=swap_card(ix,'The Octagon &middot; Tale of the Tape',mm)

# headlines
ix=rep(ix,'<h3>An unpatched store zero-day, and a KEV deadline already a day past</h3>',
          '<h3>122,500 exposed routers, and a store zero-day still without a patch</h3>')
ix=rep(ix,'<h3>Payrolls ran hot, and the hike bet swung back above even</h3>',
          '<h3>Closed for Labor Day &mdash; and four days from the number that decides the Fed</h3>')
save('index.html',ix)
print("index:",N[0])
