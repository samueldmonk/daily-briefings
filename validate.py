# -*- coding: utf-8 -*-
import json, re, sys
from html.parser import HTMLParser

VOID={'br','img','meta','link','hr','input','source','area','base','col','embed','param','track','wbr'}
PAGES=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']
fails=[]

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
            s.err.append('mismatch '+t)
        else: s.err.append('stray </%s>'%t)

for f in PAGES:
    html=open(f,encoding='utf-8').read()
    p=P(); p.feed(html)
    print("%-26s unclosed=%d errors=%d" % (f, len(p.st), len(p.err)))
    if p.st or p.err: fails.append((f,'html balance',p.st[:5],p.err[:5]))
    # nav
    navblk=re.search(r'<nav class="tabs">(.*?)</nav>', html, re.S).group(1)
    n=len(re.findall(r'<a href="(?:index|cyber-briefing|wallstreet-briefing|mma-briefing|archive)\.html"', navblk))
    act=len(re.findall(r'<a href="[a-z\-]+\.html" style="color:', navblk))
    if n!=5: fails.append((f,'nav tabs=%d'%n))
    if act!=1: fails.append((f,'active tabs=%d'%act))
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        if i not in html: fails.append((f,'missing '+i))

# tldr labels
for f,lab in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    h=open(f,encoding='utf-8').read()
    if h.count('class="tldr"')!=1: fails.append((f,'tldr count'))
    if '<b>%s</b>'%lab not in h: fails.append((f,'tldr label'))
if 'class="tldr"' in open('index.html',encoding='utf-8').read(): fails.append(('index.html','tldr present'))

# tradingview widgets
ws=open('wallstreet-briefing.html',encoding='utf-8').read()
blocks=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>', ws, re.S)
ok=0
for b in blocks:
    try: json.loads(b); ok+=1
    except Exception as e: fails.append(('ws','widget json',str(e)[:60]))
print("tradingview widget blocks parsed: %d/%d"%(ok,len(blocks)))
if len(blocks)!=8: fails.append(('ws','widget count=%d'%len(blocks)))
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    if s not in ws: fails.append(('ws','ticker missing '+s))
if '"symbol":"NASDAQ:HOOD"' not in ws: fails.append(('ws','chart of the day'))

# scorecard arithmetic
sc=[('S&P 500',7674.37,33.21,0.43),('Dow',53277.01,517.80,0.98),('Nasdaq',26180.45,113.29,0.43),('Russell',3017.87,25.44,0.85)]
good=0
for name,close,chg,pct in sc:
    prior=close-chg
    calc=chg/prior*100
    if abs(calc-pct)<=0.02: good+=1
    else: fails.append(('ws','scorecard %s calc=%.3f vs %.2f'%(name,calc,pct)))
print("scorecard arithmetic: %d/4 exact"%good)

# kev countdowns
cy=open('cyber-briefing.html',encoding='utf-8').read()
import datetime
TODAY=datetime.date(2026,8,22)
rows=re.findall(r'due <b>(\d{4}-\d{2}-\d{2})</b> <span class="(kev-[a-z]+)">\((.*?)\)</span>', cy)
kok=0
for due,cls,lbl in rows:
    y,m,d=[int(x) for x in due.split('-')]
    delta=(datetime.date(y,m,d)-TODAY).days
    if delta<0: exp=("%d day%s PAST DUE"%(abs(delta),'' if abs(delta)==1 else 's'),'kev-crit')
    elif delta==0: exp=("due today",'kev-crit')
    elif delta<=3: exp=("%d day%s left"%(delta,'' if delta==1 else 's'),'kev-soon')
    else: exp=("%d days left"%delta,'kev-ok')
    if (lbl,cls)==exp: kok+=1
    else: fails.append(('cyber','kev %s got (%s,%s) exp %s'%(due,lbl,cls,str(exp))))
print("kev countdowns with explicit due dates: %d/%d correct"%(kok,len(rows)))
pastdue = cy.count('PAST DUE') + cy.count('window elapsed')
print("kev rows total:", cy.count('<li><b>CVE-'), " past-due markers:", pastdue)
if 'CVE-2026-72529' not in cy or 'August 23' not in cy: fails.append(('cyber','patch priority/kev agreement'))
if 'CVE-2026-59310' not in cy: fails.append(('cyber','patch priority cve'))

# champions board
mm=open('mma-briefing.html',encoding='utf-8').read()
crows=re.findall(r'<tr><td>(?:Heavyweight|Light Heavyweight|Middleweight|Welterweight|Lightweight|Featherweight|Bantamweight|Flyweight|Women\'s Flyweight|Women\'s Bantamweight|Women\'s Strawweight)</td>', mm)
print("champions rows:", len(crows), " vacant cells:", mm.count('>Vacant<'))
if len(crows)!=11: fails.append(('mma','champions rows=%d'%len(crows)))
if mm.count('>Vacant<')!=0: fails.append(('mma','vacant present'))

# trap greps
traps=['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','MacKenzie','Joshua Vance','Pereira (205)','pay-per-view','former champion','title challenger','Chimaev</b></td>','Pantoja</b></td>','Dvalishvili</b></td>','Topuria</b></td>']
allhtml={f:open(f,encoding='utf-8').read() for f in PAGES}
for t in traps:
    hits=[f for f,h in allhtml.items() if t in h]
    print("trap %-22s -> %s" % (t, hits if hits else 'CLEAN'))
    if hits: fails.append(('trap',t,hits))

# after-hours (weekend => explanatory note, no cards)
if 'No after-hours section this edition' not in ws: fails.append(('ws','after-hours note missing'))

print("\n=== FAILURES: %d ==="%len(fails))
for f in fails: print(" ", f)
