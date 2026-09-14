import sys
fails=[]
def ins(fn, anchor, add, label):
    h=open(fn).read()
    if h.count(anchor)!=1: fails.append("MISS %s (%d)"%(label,h.count(anchor))); return
    open(fn,'w').write(h.replace(anchor, anchor+add,1))

A='<footer><h4>Sources &mdash; fetched this run</h4><div class="srcs">'
ins('cyber-briefing.html', A,
 '<a href="https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk" target="_blank" rel="noopener">CISA &mdash; BOD 26-04: Prioritizing Security Updates Based on Risk</a>'
 '<a href="https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk" target="_blank" rel="noopener">CISA &mdash; BOD 26-04 implementation guidance</a>'
 '<a href="https://www.runzero.com/blog/bod-26-04/" target="_blank" rel="noopener">runZero &mdash; BOD 26-04: a new era of prioritized remediation</a>'
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog" target="_blank" rel="noopener">CISA &mdash; Adds two KEVs to catalog (31 August 2026)</a>','cyber srcs')

ins('wallstreet-briefing.html', A,
 '<a href="https://www.cnbc.com/2026/09/14/10-year-us-treasury-is-closing-in-on-5percent.html" target="_blank" rel="noopener">CNBC &mdash; 10-year Treasury yield hits 5% before reversing as traders await Fed meeting</a>','ws srcs')

ins('mma-briefing.html', A,
 '<a href="https://www.ufc.com/event/ufc-fight-night-october-17-2026" target="_blank" rel="noopener">UFC.com &mdash; UFC Fight Night: Buckley vs. Malott</a>'
 '<a href="https://www.rogersplace.com/ufc-fight-night-october-17-2026/" target="_blank" rel="noopener">Rogers Place &mdash; UFC Fight Night, 17 October 2026</a>'
 '<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Buckley_vs._Malott" target="_blank" rel="noopener">UFC Fight Night: Buckley vs. Malott &mdash; card and co-main</a>','mma srcs')

if fails: print("FAILED:",fails); sys.exit(1)
print("SOURCES-1835 OK")
