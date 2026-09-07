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

# WTI: corroborate the ~$91 level a second, independent time
w=rep(w,'The <b>~$91</b> level, which two earlier runs agreed on, is what the row still carries.</td></tr>',
 'The <b>~$91</b> level, which two earlier runs agreed on, is what the row still carries &mdash; and it now has independent corroboration: a return this morning puts <b>WTI October futures around $91.10 a barrel</b> and the contract <b>up roughly 9% on the week</b>. Two sources within 40 cents of each other is the closest this row has come to a settled number, though it is still not published as a settle.</td></tr>')

# Radar: add the Labor Day / reopening item and the Tuesday restart
w=rep(w,'<h2 class="sec">Rates, Bonds &amp; Commodities</h2>',
        '<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')

save('wallstreet-briefing.html',w)
print("ws wti:",N[0])
