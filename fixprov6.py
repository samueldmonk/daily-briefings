# -*- coding: utf-8 -*-
import io
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(f,h,old,new,cnt=1):
    assert h.count(old)==cnt,("%s COUNT %d!=%d %r"%(f,h.count(old),cnt,old[:90]))
    N[0]+=1;return h.replace(old,new)
m=load('mma-briefing.html')
m=rep('mm',m,'not asserted &mdash; UFC.com re-fetched this run and unchanged',
             'not asserted &mdash; UFC.com unreachable this run; last direct reading 2:25')
m=rep('mm',m,'come from a fightnews.com full-card report fetched this run',
             'come from a fightnews.com full-card report fetched in an earlier edition')
m=rep('mm',m,'Every price above is stated verbatim in a source fetched this run</b>, with the book or aggregator named; none is carried on trust from a previous edition.',
  'Every price above is stated verbatim in a named source</b>, with the book or aggregator attached. The Silva&ndash;Delgado line was <b>re-verified this morning</b>: a fresh return again gives <b>&minus;425 / +355</b> after an opening <b>&minus;450 / +350</b>, unchanged from what is printed. The remaining prices are carried from the editions in which they were sourced, and are labelled as carried rather than as re-checked today.')
m=rep('mm',m,'none appeared on any page fetched this run','none has appeared on any page fetched for it')
save('mma-briefing.html',m)
print("mma:",N[0])
