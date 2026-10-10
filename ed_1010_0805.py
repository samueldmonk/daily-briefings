import re,datetime,sys
D=sys.argv[1]; today=datetime.date(2026,10,10)
MON={'Jan':1,'January':1,'Feb':2,'Sept':9,'Sep':9,'September':9,'Oct':10,'October':10,'Nov':11,'November':11,'Dec':12,'Aug':8,'August':8}
def rd(p): return open(f'{D}/{p}').read()
def wr(p,t): open(f'{D}/{p}','w').write(t)
def sub1(t,a,b):
    assert a in t,(a[:80]); return t.replace(a,b,1)
# ---- CYBER countdowns
c=rd('cyber-briefing.html')
datere=re.compile(r'(Jan|Feb|Aug|August|Sept|Sep|September|Oct|October|Nov|November|Dec)\.? (\d{1,2}), 2026|2026-(\d\d)-(\d\d)')
def fix(m):
    back=c[max(0,m.start()-400):m.start()]
    ds=list(datere.finditer(back))
    if not ds: return m.group(0)
    d=ds[-1]
    dt=datetime.date(2026,int(d.group(3)),int(d.group(4))) if d.group(3) else datetime.date(2026,MON[d.group(1)],int(d.group(2)))
    n=(dt-today).days
    if n>0: return f'({n} day{"s" if n!=1 else ""} left)'
    if n==0: return '(due today)'
    return f'({-n} day{"s" if n!=-1 else ""} overdue)'
c2=re.sub(r'\((\d+) days? (left|overdue)\)',fix,c)
for a,b in zip(re.findall(r'\(\d+ days? (?:left|overdue)\)',c),re.findall(r'\((?:\d+ days? (?:left|overdue)|due today)\)',c2)): print(a,'->',b)
c=c2
c=c.replace('<b class="warnc">(1 day left)</b>','<b class="warnc">(1 day left &mdash; due tomorrow)</b>')
c=sub1(c,'<div class="n">2 days</div><div class="l">Overdue:','<div class="n">3 days</div><div class="l">Overdue:')
# new Nikkei card at front of breaches
nik=('<div class="card"><span class="tag warnt">New</span> <h3>Nikkei discloses two email-account breaches, one used to send 9,000 phishing messages</h3>'
 '<p>Japanese publishing group Nikkei said an unauthorized party accessed an employee Google Workspace account in late July, potentially exposing the names and email addresses of 1,646 employees and business partners (reader and interviewee data was not included); in September attackers got into a separate Microsoft 365 account and used it on Sept. 30 to send 9,000 emails with malicious links to staff and interviewees. Nikkei reset passwords and says no further unauthorized logins have been confirmed; it has not identified the attackers or said whether the incidents are linked '
 '(<a href="https://www.integrity360.com/cyber-news-roundup-october-9th-2026" style="color:var(--acc2)">Integrity360 roundup, Oct. 9</a>).</p></div>')
c=sub1(c,'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">','<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">'+nik)
c=sub1(c,'CISA has given federal agencies until Sunday, Oct. 11 to patch','CISA&rsquo;s deadline for federal agencies is tomorrow, Sunday, Oct. 11, to patch')
c=c.replace('is now past its Oct. 7 federal deadline','is three days past its Oct. 7 federal deadline',1)
c=re.sub(r'(<div class="srcs">Sources: )',r'\1<a href="https://www.integrity360.com/cyber-news-roundup-october-9th-2026" style="color:var(--acc2)">Integrity360 Cyber News Roundup (Oct 9)</a> · ',c,1)
wr('cyber-briefing.html',c)
# ---- WALL STREET
w=rd('wallstreet-briefing.html')
w=sub1(w,'Closing bell: Dow +0.83%, Nasdaq +0.64%, S&amp;P 500 +0.59% as tech rebounds; real estate and health care lead, telecoms drag communication services',
 'Weekend edition &mdash; markets closed; latest close Fri. Oct 9: Dow +0.83%, Nasdaq +0.64%, S&amp;P 500 +0.59% to cap a winning week, with bank earnings up next')
wk=('<p><span class="tag warnt">New</span> <b>Weekend (Sat. Oct 10, ~8 AM ET).</b> U.S. markets are closed until Monday; the figures below are Friday&rsquo;s. &ldquo;All three major averages posted weekly gains to cap a volatile week,&rdquo; Yahoo Finance wrote, after a surge in long-dated bond yields and higher oil prices that both eased Friday &ldquo;though they remained elevated.&rdquo; &ldquo;Investors now turn to earnings season, which kicks off next week with results from the biggest banks&rdquo; (<a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-october-9-dow-sp-500-nasdaq-080148117.html" style="color:var(--acc2)">Yahoo Finance</a>). '
 'Monday is Columbus Day: banks and the bond market are closed, but &ldquo;it is not a stock market holiday and the stock market is open.&rdquo; Kiplinger&rsquo;s calendar has Wells Fargo reporting Tuesday morning with analysts expecting $1.85 a share (+11.4% year over year) on $22.4 billion in revenue, and Johnson &amp; Johnson expected at $2.51 a share (&minus;10.4%) on $25.4 billion (+5.8%) (<a href="https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks" style="color:var(--acc2)">Kiplinger, updated Oct. 9</a>).</p>\n')
i=w.index('<p><b>Official close (4 PM ET).</b>'); w=w[:i]+wk+w[i:]
w=sub1(w,'Stocks closed higher Friday &mdash;','Markets are closed for the weekend after stocks closed higher Friday &mdash;')
w=w.replace('Category 3 storm forecast to make landfall late Friday near the Alabama&ndash;Florida line;','as of Friday, a Category 3 storm forecast to make landfall late Friday near the Alabama&ndash;Florida line;',1)
w=w.replace('<li><b>Out at 10 AM ET:</b> University of Michigan','<li><b>Released Friday:</b> University of Michigan',1)
w=re.sub(r'(<div class="srcs">Sources: )',r'\1<a href="https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks" style="color:var(--acc2)">Kiplinger earnings calendar (Oct 12&ndash;16)</a> · ',w,1)
wr('wallstreet-briefing.html',w)
# ---- MMA
m=rd('mma-briefing.html')
m=m.replace('<span class="tag good">Updated</span>','',1)
m=sub1(m,'Main event set: Brendan Allen (186) and Christian Leroy Duncan (185) both made weight Friday for Saturday&rsquo;s middleweight headliner at Meta APEX',
 'Fight night: Brendan Allen (186) and Christian Leroy Duncan (185) headline tonight at Meta APEX (main card 8 PM ET) after both made weight Friday')
odds=(' <span class="tag warnt">New</span> Latest: BetOnline, via <a href="https://clutchpoints.com/betting/brendan-allen-vs-christian-leroy-duncan-prediction-odds-pick-for-ufc-vegas-122" style="color:var(--acc2)">ClutchPoints</a> (Oct. 9, 8:06 PM ET), has Allen &minus;117 / Duncan +100, rounds 3.5 (Over &minus;115 / Under &minus;101) &mdash; the line has tightened toward Duncan through fight week.')
m=sub1(m,'On the main card, Matheus Camilo is −198 against Jai Herbert (+164).','On the main card, Matheus Camilo is −198 against Jai Herbert (+164).'+odds) if 'Matheus Camilo is −198' in m else sub1(m,'On the main card, Matheus Camilo is &minus;198 against Jai Herbert (+164).','On the main card, Matheus Camilo is &minus;198 against Jai Herbert (+164).'+odds)
m=re.sub(r'(<div class="srcs">Sources: )',r'\1<a href="https://clutchpoints.com/betting/brendan-allen-vs-christian-leroy-duncan-prediction-odds-pick-for-ufc-vegas-122" style="color:var(--acc2)">ClutchPoints (Allen&ndash;Duncan odds, Oct 9)</a> · ',m,1)
wr('mma-briefing.html',m)
# ---- INDEX: sync summaries
ix=rd('index.html')
def tl(t): return re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>',t,re.S).group(1)
ps=re.findall(r'<p>.*?</p>',ix,re.S)
for old,new in zip(ps[:3],[tl(c),tl(w),tl(m)]): ix=ix.replace(old,'<p>'+new+'</p>',1)
wr('index.html',ix)
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    print(f, tl(rd(f)))
