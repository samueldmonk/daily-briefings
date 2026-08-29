import io, re
for p in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s = io.open(p, encoding='utf-8').read()
    s = re.sub(r'(id="updated">)12:35 PM ET<', r'\g<1>1:05 PM ET<', s)
    io.open(p,'w',encoding='utf-8').write(s)
# remove the duplicate CISA link I introduced (keep the pre-existing one)
p='cyber-briefing.html'
s=io.open(p,encoding='utf-8').read()
dup=u'<a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA &mdash; Six KEV additions, August 26 2026</a><br>'
assert s.count(dup)==1, s.count(dup)
io.open(p,'w',encoding='utf-8').write(s.replace(dup,u'',1))
print("FIX2 OK")
