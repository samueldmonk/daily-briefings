# -*- coding: utf-8 -*-
import re
ix=open('index.html',encoding='utf-8').read()
def tldr(p):
    s=open(p,encoding='utf-8').read()
    m=re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', s, re.S)
    assert m, "no tldr in "+p
    return m.group(1)
cy,ws,mm = tldr('cyber-briefing.html'), tldr('wallstreet-briefing.html'), tldr('mma-briefing.html')

def swap(cls, headline, summary, label):
    global ix
    m=re.search(r'(<div class="card '+cls+r'">.*?</div>\n)<h3>(.*?)</h3>\n<p>(.*?)</p>', ix, re.S)
    assert m, "card not found: "+label
    ix = ix[:m.start(2)] + headline + ix[m.end(2):]
    m2=re.search(r'(<div class="card '+cls+r'">.*?</div>\n)<h3>(.*?)</h3>\n<p>(.*?)</p>', ix, re.S)
    ix = ix[:m2.start(3)] + summary + ix[m2.end(3):]
    print("ok:",label)

swap('c-cy', "Oracle's federal deadline runs out within the hour — and Saturday's Citrix date is now disputed", cy, 'cyber card')
swap('c-ws', "The Dow's gain has shrunk to 0.15%, and ten of eleven sectors are red", ws, 'markets card')
swap('c-mm', "A fourth Shanghai line moves the favourite out to −550", mm, 'mma card')

open('index.html','w',encoding='utf-8').write(ix)

# assert byte-identical
ix=open('index.html',encoding='utf-8').read()
for cls,t,lab in [('c-cy',cy,'cyber'),('c-ws',ws,'markets'),('c-mm',mm,'mma')]:
    m=re.search(r'<div class="card '+cls+r'">.*?</div>\n<h3>.*?</h3>\n<p>(.*?)</p>', ix, re.S)
    assert m.group(1)==t, "MISMATCH "+lab
    print("byte-identical:",lab)
