import re
def rep(s,a,b,n=1):
    assert s.count(a)==n,(a[:80],s.count(a)); return s.replace(a,b)
f='wallstreet-briefing.html'; s=open(f).read()
old_tldr=re.search(r'<div class="tldr"><b>The Tape</b><span>(.*?)</span></div>',s).group(1)
new_tldr="As of 1:30 PM ET Friday stocks were extending gains &mdash; the Dow up about 420 points (0.82%), with the Nasdaq up roughly 0.5% and the S&amp;P 500 about 0.4% &mdash; as oil fell on Iran&rsquo;s offer to reopen the Strait of Hormuz and Treasury yields eased from multi-decade highs."
s=rep(s,old_tldr,new_tldr)
h=re.search(r'<div class="lead"><h3>(.*?)</h3>',s).group(1)
s=rep(s,h,"As of 1:30 PM ET: Dow up 0.82%, Nasdaq up ~0.5%, S&amp;P 500 up ~0.4% as oil slides and yields ease")
s=rep(s,"Wall Street is ending a volatile week on a firmer note. At 1:00 PM ET the Dow Jones Industrial Average was up about 370 points, or 0.72%, the Nasdaq Composite was up 0.46% and the S&amp;P 500 was up 0.39% &mdash; a little below the session&rsquo;s midday readings.",
"Wall Street is ending a volatile week on a firmer note. At 1:30 PM ET the Dow Jones Industrial Average was up about 420 points, or 0.82%, with the Nasdaq Composite up roughly 0.5% and the S&amp;P 500 up about 0.4% &mdash; firmer than the 1:00 PM ET reading (Dow +0.72%, Nasdaq +0.46%, S&amp;P 500 +0.39%).")
s=rep(s,"The 1:00 PM ET index moves are from a time-stamped quote reading returned by this 1:03 PM ET refresh&rsquo;s market search (Dow +370.34 points, Nasdaq +123.74 points &mdash; both consistent with Thursday&rsquo;s official closes); the 12:15 PM ET comparison is Yahoo Finance&rsquo;s quote strip.",
"The 1:30 PM ET Dow move is from a time-stamped quote reading returned by this 1:33 PM ET refresh&rsquo;s market search (Dow +419.67 points, consistent with Thursday&rsquo;s official close); the approximate Nasdaq and S&amp;P 500 moves accompany it in the same Yahoo Finance-sourced result. The 1:00 PM ET and 12:15 PM ET comparisons are from the previous refreshes.")
open(f,'w').write(s)
f='cyber-briefing.html'; s=open(f).read()
s=s.replace('<span class="tag good">New</span> ','').replace('<span class="tag good">New</span>','')
open(f,'w').write(s)
f='index.html'; s=open(f).read()
s=rep(s,old_tldr,new_tldr)
open(f,'w').write(s)
print('ok')
