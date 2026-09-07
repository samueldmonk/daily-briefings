# -*- coding: utf-8 -*-
import io,datetime
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt,("COUNT %d!=%d %r"%(h.count(old),cnt,old[:90]))
    N[0]+=1;return h.replace(old,new)
T=datetime.date(2026,9,7)
d18=(datetime.date(2026,9,18)-T).days; d16=(datetime.date(2026,9,16)-T).days; od=(T-datetime.date(2026,9,5)).days
assert (d18,d16,od)==(11,9,2),(d18,d16,od)
c=load('cyber-briefing.html')
c=rep(c,'<span class="down"><b>(overdue by 1 day)</b></span>','<span class="down"><b>(overdue by %d days)</b></span>'%od)
c=rep(c,'<span class="mut">(10 days left)</span>','<span class="mut">(%d days left)</span>'%d16)
c=rep(c,'<span class="mut">(12 days left)</span>','<span class="mut">(%d days left)</span>'%d18)
save('cyber-briefing.html',c)
print("countdowns:",N[0],d18,d16,od)
