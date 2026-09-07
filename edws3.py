# -*- coding: utf-8 -*-
import io
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1; return h.replace(old,new)

w=load('wallstreet-briefing.html')
w=rep(w,'On where they finished Friday the same returns split: <b>58%</b> is stated by two of them, <b>&ldquo;roughly 60%&rdquo; / 60.2%</b> by another. <b>No single post-payrolls probability is asserted.</b>',
 'On where they finished Friday the same returns split: <b>58%</b> is stated by two of them, <b>&ldquo;roughly 60%&rdquo; / 60.2%</b> by another, and a third reading arrived this morning &mdash; a fresh return attributing <b>63%</b> to <b>Bloomberg</b>, citing the same 162,000 payrolls and 4.1% unemployment. <b>No single post-payrolls probability is asserted.</b> Three sources, three numbers, spanning five percentage points.')
save('wallstreet-briefing.html',w)
print("ws odds:",N[0])
