import sys,re
p=sys.argv[1]+'/wallstreet-briefing.html'
s=open(p,encoding='utf-8').read()
a='<p><span class="tag new">New</span><b>Data consensus.</b>'
assert s.count(a)==1
s=s.replace(a,'<p><b>Data consensus.</b>')
L='https://www.lpl.com/research/blog/weekly-market-performance-october-9-2026.html'
par=('<p><span class="tag new">New</span><b>Sector scoreboard (LPL, week to Fri. 3:25 PM ET).</b> Defensives led the week: consumer staples gained 3.96%, utilities 3.88% and energy 3.71%, while industrials (&minus;0.32%) and information technology (&minus;0.11%) were the only S&amp;P 500 sectors lower, per LPL Research&rsquo;s Bloomberg data stamped 10/9/26 at 3:25 p.m. ET. On the same snapshot the Russell 2000 fell 0.76% for the week and the S&amp;P 500&rsquo;s year-to-date gain stood at 14.19%; LPL said &ldquo;U.S. bonds snapped a five-week losing streak,&rdquo; with the Bloomberg U.S. Aggregate up 0.41%, and that attention was turning &ldquo;to the upcoming start of earnings season&rdquo; (<a href="'+L+'" style="color:var(--acc2)">LPL Research, Oct. 9</a>).</p>\n')
b='<p><b>JPMorgan bar.</b>'
assert s.count(b)==1
s=s.replace(b,par+b)
s,n=re.subn(r'Week ahead \(Sun\. Oct 11, re-checked ~[0-9:]+ [AP]M ET\)','Week ahead (Sun. Oct 11, re-checked ~1:10 PM ET)',s); assert n==1
f='<div class="srcs">Sources: '
assert s.count(f)==1
s=s.replace(f,f+'<a href="'+L+'" style="color:var(--acc2)">LPL Research Weekly Market Performance (Oct 9, data 3:25 PM ET)</a> &middot; ')
open(p,'w',encoding='utf-8').write(s)
print('ok')
