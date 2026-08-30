# -*- coding: utf-8 -*-
import io,re,sys
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)

def tldr(path,label):
    s=rd(path)
    i=s.find(u'class="tldr"><b>'+label+u'</b> <span>')
    j=s.find(u'</span></div>', i)
    assert i>0 and j>0, path
    return s[i+len(u'class="tldr"><b>'+label+u'</b> <span>'):j]

cy=tldr('cyber-briefing.html','The Wire')
ws=tldr('wallstreet-briefing.html','The Tape')
mm=tldr('mma-briefing.html','Tale of the Tape')

x=rd('index.html')
def swap(x, cls, body):
    i=x.find(u'<div class="bigcard '+cls+u'"')
    assert i>0, cls
    p=x.find(u'<p>', i); q=x.find(u'</p>', p)
    assert p>0 and q>0
    return x[:p+3]+body+x[q:]

x=swap(x,'c-cy',cy); x=swap(x,'c-ws',ws); x=swap(x,'c-mm',mm)
wr('index.html',x)

# verify equality
x=rd('index.html')
for cls,body,name in (('c-cy',cy,'cyber'),('c-ws',ws,'ws'),('c-mm',mm,'mma')):
    i=x.find(u'<div class="bigcard '+cls+u'"'); p=x.find(u'<p>',i); q=x.find(u'</p>',p)
    assert x[p+3:q]==body, name
print('OK index mirrors all three tldrs')
