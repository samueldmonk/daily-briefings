# -*- coding: utf-8 -*-
"""Mirror each briefing's .tldr sentence into its index.html card, and add this run's sources."""
import re, sys, io, os
D=sys.argv[1]
def rd(f): return io.open(os.path.join(D,f),encoding='utf-8').read()
def wr(f,s): io.open(os.path.join(D,f),'w',encoding='utf-8').write(s)
fails=[]

def tldr_span(f):
    s=rd(f)
    m=re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>',s,re.S)
    if not m: fails.append('no tldr in '+f); return None
    return m.group(1)

pairs=[('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]
idx=rd('index.html')
for f,h3 in pairs:
    body=tldr_span(f)
    if body is None: continue
    pat=re.compile(r'(<h3>'+re.escape(h3)+r'</h3>\s*<div class="sub">[^<]*</div>\s*<p>).*?(</p>)',re.S)
    if len(pat.findall(idx))!=1:
        fails.append('index card anchor %s count=%d'%(h3,len(pat.findall(idx)))); continue
    idx=pat.sub(lambda mo: mo.group(1)+body+mo.group(2), idx, count=1)

# index footer: replace the "Three things changed at 11:35 AM" paragraph lead-in with this run's note
old_marker='Three things changed at 11:35 AM.'
newpara=('Three things changed at 4:06 PM, and each is an addition rather than a correction. '
 'The security briefing added <b>CVE-2026-62878</b>, a 9.8 unauthenticated remote-code-execution flaw in <b>Windows DNS Server</b> that is <b>not</b> under exploitation &mdash; it is on the board for reachability, and the page prints the difference between a flaw researchers call <b>potentially wormable</b> and a flaw anyone reports being wormed. '
 'The markets briefing replaced a second-hand characterisation with <b>two direct quotations</b>: Warsh calling the 2% goal &ldquo;a firm, fixed target&rdquo; and assigning responsibility for &ldquo;65 months of sustained, elevated inflation&rdquo; to the central bank &mdash; and it <b>recorded a Nasdaq 100 close without promoting it</b> into the Composite row it does not belong in. '
 'The MMA briefing filled a gap it had been flagging as empty: the <b>Paris card now has a betting line</b>, in three renderings between &minus;400 and &minus;500 on the favourite, <b>printed as a spread because a hundred points of moneyline is not a rounding difference</b>. '
 'Three things changed at 11:35 AM.')
if idx.count(old_marker)!=1: fails.append('index footer marker count=%d'%idx.count(old_marker))
else: idx=idx.replace(old_marker,newpara)
wr('index.html',idx)

# ---- footer sources for the three briefings ----
SRC={
 'cyber-briefing.html':[
  ('https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/','SecurityWeek &mdash; August 2026 Patch Tuesday'),
  ('https://www.zerodayinitiative.com/blog/2026/8/11/the-august-2026-security-update-review','Zero Day Initiative &mdash; August 2026 Security Update Review (CVE-2026-62878)'),
  ('https://isc.sans.edu/diary/Microsoft+Patch+Tuesday+August+2026/33236/','SANS ISC &mdash; Microsoft Patch Tuesday August 2026'),
  ('https://www.cisa.gov/news-events/alerts/2026/08/07/cisa-adds-one-known-exploited-vulnerability-catalog','CISA KEV &mdash; Aug 7 addition (CVE-2026-8037)'),
  ('https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog','CISA KEV &mdash; Aug 26 additions'),
 ],
 'wallstreet-briefing.html':[
  ('https://www.housingwire.com/articles/warsh-jackson-hole-hawkish-inflation-fed-september-rate-hike/','HousingWire &mdash; Warsh at Jackson Hole (direct quotations)'),
  ('https://www.cnbc.com/2026/08/28/kevin-warsh-jackson-hole-federal-reserve-inflation.html','CNBC &mdash; Warsh warns on inflation at Jackson Hole'),
  ('https://www.investing.com/news/stock-market-news/september-market-outlook-historical-weakness-meets-2026-volatility-93CH-4814892','Investing.com &mdash; September outlook (Nasdaq 100 Friday close)'),
  ('https://tradingeconomics.com/commodity/brent-crude-oil','Trading Economics &mdash; Brent and WTI, Aug 28 close'),
 ],
 'mma-briefing.html':[
  ('https://sports.yahoo.com/articles/ufc-fight-night-287-dan-175030528.html','Yahoo Sports &mdash; UFC Fight Night 287 odds'),
  ('https://www.ufc.com/event/ufc-fight-night-september-05-2026','UFC.com &mdash; UFC Paris event page'),
  ('https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse','UFC Fight Night: Hooker vs. Parnasse &mdash; card'),
  ('https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/','Paramount+ &mdash; UFC 2026 schedule (September cards)'),
 ],
}
for f,links in SRC.items():
    s=rd(f)
    fi=s.find('<footer')
    if fi<0: fails.append('no footer in '+f); continue
    add=''.join('<a href="%s" target="_blank" rel="noopener">%s</a> '%(u,t)
                for u,t in links if u not in s)
    if not add: continue
    # insert right after the first <div class="srcs"...> inside the footer
    mm=re.search(r'(<footer[^>]*>\s*<div class="srcs"[^>]*>)',s[fi:])
    if not mm: fails.append('no srcs div in '+f); continue
    pos=fi+mm.end()
    s=s[:pos]+add+s[pos:]
    wr(f,s)

# duplicate-href sweep across all four
for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=rd(f); hrefs=re.findall(r'href="(https?://[^"]+)"',s)
    dups=[h for h in set(hrefs) if hrefs.count(h)>1]
    if dups: fails.append('DUP HREFS in %s: %s'%(f,dups))
print('FAILS:', fails if fails else 'none')
