import re,sys
p='wallstreet-briefing.html'; s=open(p).read()
cn='https://www.cnbc.com/2026/10/11/stock-market-today-live-updates.html'
para=('<p><span class="tag new">New</span> <b>Sunday-night futures (CNBC, ~6:23 PM ET).</b> Stock futures were little changed Sunday evening after the major averages logged a winning week: S&amp;P 500 futures were up about 0.12% and Nasdaq 100 futures about 0.24%, CNBC reported, as investors looked to a busy week of bank earnings and September CPI and PPI data. FactSet&rsquo;s John Butters projects 29.6% earnings growth for the S&amp;P 500 in the quarter, and Brent crude futures last traded above $104 a barrel, per CNBC (<a href="'+cn+'" style="color:var(--acc2)">CNBC live updates, Oct. 11</a>).</p>\n')
k='<p><b>Record backdrop.</b>'
assert s.count(k)==1; s=s.replace(k,para+k)
s=s.replace('re-checked ~6:05 PM ET).','re-checked ~6:35 PM ET).',1)
old='Markets are closed for the weekend after stocks closed higher Friday'
assert old in s
s=s.replace('with September CPI due Wednesday.</span></div>','with September CPI due Wednesday; S&amp;P 500 futures were up about 0.12% Sunday evening, per CNBC.</span></div>',1)
fs='<div class="srcs">Sources: '
s=s.replace(fs,fs+'<a href="'+cn+'" style="color:var(--acc2)">CNBC &mdash; Live updates (Oct. 11)</a> &middot; ',1)
open(p,'w').write(s)
i=open('index.html').read()
n=i.count('with September CPI due Wednesday.')
i=i.replace('with September CPI due Wednesday.','with September CPI due Wednesday; S&amp;P 500 futures were up about 0.12% Sunday evening, per CNBC.',1)
open('index.html','w').write(i); print('ok',n)
