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

w=rep(w,'the <b>seventh consecutive run</b> in which these three figures have come back unchanged',
        'the <b>eighth consecutive run</b> in which these three figures have come back unchanged')
w=rep(w,'<b>No after-hours session this edition:</b> it is Sunday and the next U.S. session is Tuesday 8 September, so there is no extended-hours tape to report and none is published.',
        '<b>No after-hours session this edition:</b> it is Labor Day, U.S. equity and bond markets are closed all day, and the next session is Tuesday 8 September &mdash; so there is no extended-hours tape to report and none is published. These figures will remain the most recent close for a third calendar day.')
w=rep(w,'<li><b>Monday 7 September &mdash; Labor Day.</b> U.S. stock and bond markets closed. Next session Tuesday 8 September.</li>',
 '<li><b>Today, Monday 7 September &mdash; Labor Day.</b> The NYSE and Nasdaq are closed for the full session and the U.S. bond market is closed as well, per SIFMA. The NYSE reopens at its normal <b>9:30 AM ET</b> on <b>Tuesday 8 September</b>, which gives the market three sessions to position before Friday&rsquo;s CPI.</li>')

save('wallstreet-briefing.html',w)
print("ws5:",N[0])
