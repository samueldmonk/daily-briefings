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

# 1) Lead headline + holiday framing
w=rep(w,'<h3 style="margin:0 0 9px;font-size:21px">A hot jobs number closed the week &mdash; but the vote now turns on Friday&rsquo;s CPI</h3>',
        '<h3 style="margin:0 0 9px;font-size:21px">Labor Day: no session today, and four days to wait for the number that decides the Fed</h3>')

w=rep(w,'<p style="margin:0 0 10px"><b>Markets are closed.</b> It is Sunday, and U.S. equity and bond markets are shut again on <b>Monday 7 September for Labor Day</b>, with the next session on <b>Tuesday 8 September</b>.',
        '<p style="margin:0 0 10px"><b>Markets are closed.</b> Today is <b>Monday 7 September, Labor Day</b>: the New York Stock Exchange and Nasdaq are shut all day, and the U.S. bond market is closed too per SIFMA. The NYSE reopens at normal hours, <b>9:30 AM ET on Tuesday 8 September</b>.')

# 2) revisions + "strongest since March" + the 55,000 trap, appended to the payrolls paragraph
w=rep(w,'and carried the <b>2-year yield to its highest level since January 2025</b>. <span class="mut">A level for the 2-year is still not published &mdash; the direction is sourced, the number is not.</span></p>',
 'and carried the <b>2-year yield to its highest level since January 2025</b>. <span class="mut">A level for the 2-year is still not published &mdash; the direction is sourced, the number is not.</span> '
 'Two details newly sourced this morning put the beat in context: it was the <b>strongest monthly gain since March</b>, and the two prior months were revised <i>up</i> &mdash; June from 20,000 to '
 '<b>31,000</b> and July from a loss of 23,000 to a gain of <b>21,000</b>, leaving June and July combined <b>55,000 higher</b> than previously reported. '
 '<span class="mut">A caution attached to that last figure, because this desk nearly published it as something else: one return this run described the consensus as &ldquo;55,000,&rdquo; which collides '
 'with the two-month revision total. The consensus is <b>53,000</b> &mdash; independently re-confirmed this run and now verified thirteen times &mdash; and 55,000 is the revision, not the forecast. '
 'The two numbers are a coincidence, not a correction.</span></p>')

save('wallstreet-briefing.html',w)
print("ws part1:",N[0])
