import re,json
from html.parser import HTMLParser
FAIL=[];N=0
def ck(c,m):
    global N;N+=1
    if not c: FAIL.append(m)
P={f:open(f,encoding='utf-8').read() for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
VOID={'br','img','meta','link','hr','input','source','col'}
class B(HTMLParser):
    def __init__(s):super().__init__();s.st=[];s.bad=0
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
        else: s.bad+=1
for f,h in P.items():
    b=B();b.feed(h)
    ck(b.bad==0,f+" stray close tags: %d"%b.bad)
    ck(len(b.st)==0,f+" unclosed: %s"%b.st[:6])
    nav=re.search(r'<nav class="tabs">(.*?)</nav>',h,re.S)
    ck(bool(nav),f+" no nav")
    if nav:
        ck(nav.group(1).count('class="on"')==1,f+" active tab count")
        for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
            ck('href="%s"'%t in nav.group(1),f+" nav missing "+t)
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        ck(i in h,f+" missing "+i)
    ck("America/New_York" in h, f+" missing stamp JS")
# tldr
for f,lab in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    m=re.search(r'<div class="tldr"><b>([^<]+)</b>',P[f]); ck(bool(m) and m.group(1)==lab,f+" tldr label")
    t=re.search(r'<div class="tldr">.*?</div>',P[f],re.S)
    inner=re.sub(r'<[^>]+>','',t.group(0))
    ck(inner.strip() != '', f+" tldr empty")
ck('class="tldr"' not in P['index.html'],"index has tldr")
# index cards carry each page's tldr sentence
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>',P[f],re.S).group(1)
    ck(s in P['index.html'], "index card missing "+f+" tldr verbatim")
# TradingView widgets
w=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>',P['wallstreet-briefing.html'],re.S)
ck(len(w)==8,"widget count %d"%len(w))
for j in w:
    try: json.loads(j)
    except Exception as e: FAIL.append("widget JSON parse: %s"%e)
    N+=1
tick=[x for x in w if 'ticker-tape' not in x or True]
tt=[x for x in w if '"symbols"' in x][0]
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(s in tt,"ticker missing "+s)
ck('"symbol":"NASDAQ:AAOI"' in P['wallstreet-briefing.html'],"chart of day AAOI")
ck('"symbol":"NASDAQ:SNDK"' not in P['wallstreet-briefing.html'],"SNDK should be absent as widget symbol")
# KEV countdowns
cy=P['cyber-briefing.html']
kev=re.findall(r'<span class="kevdue([^"]*)">([^<]*)<',cy)
ck(len(kev)==12,"KEV rows %d (want 12)"%len(kev))
past=sum(1 for c,t in kev if 'PAST DUE' in t); today=sum(1 for c,t in kev if 'DUE TODAY' in t)
ahead=sum(1 for c,t in kev if 'left' in t and 'DUE TODAY' not in t)
ck(past==8,"KEV past due =%d (want 8)"%past)
ck(today==1,"KEV due today =%d (want 1)"%today)
ck(ahead==3,"KEV ahead =%d (want 3)"%ahead)
# champions: champion column only
mma=P['mma-briefing.html']
i=mma.find('Champions board'); seg=mma[i:i+9000]
rows=re.findall(r'<tr><td>[^<]*</td><td>([^<]*)</td>',seg)
ck(len(rows)==11,"champion rows %d"%len(rows))
champs=' | '.join(rows)
for n in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van']:
    ck(n in champs,"champion missing "+n)
for n in ['Pereira','Chimaev','Topuria','vacant','Vacant']:
    ck(n not in champs,"stale champion cell: "+n)
# after-hours label
ck('<div class="lab">After-hours movers' not in P['wallstreet-briefing.html'],"after-hours section should be absent")
# new tag counts
ws_new=P['wallstreet-briefing.html'].count('<span class="tag new">New</span>')
cy_new=cy.count('<span class="tag new">New</span>')
mm_new=mma.count('<span class="tag new">New</span>')
ck(ws_new==2,"WS New tags %d (want 2)"%ws_new)
ck(cy_new==0,"CY New tags %d (want 0)"%cy_new)
ck(mm_new==0,"MMA New tags %d (want 0)"%mm_new)
ck(P['wallstreet-briefing.html'].count('<b>New this edition.</b>')==2,"WS 'New this edition' count")
ck(cy.count('<b>New this edition.</b>')==0,"CY 'New this edition' should be 0")
# dropped tags gone
for s in ['<span class="tag down">MRNA −7%</span><span class="tag">Profit-taking</span><span class="tag new">New</span>',
          '<span class="tag down">Drones, quantum</span><span class="tag">Risk appetite</span><span class="tag new">New</span>']:
    ck(s not in P['wallstreet-briefing.html'],"dropped WS tag still present")
# fresh figures present
ws=P['wallstreet-briefing.html']
for s in ['Operation Economic Outcast','0.18%','0.40%','0.23%','$84.73','$92.44','more than 60 entities','economic asphyxiation','1:35 p.m. ET','660 million barrels']:
    ck(s in ws,"WS missing fresh: "+s)
for s in ['Operation Economic Outcast','conduct cyber operations']:
    ck(s in cy,"CY missing fresh: "+s)
ck('Operation Economic Outcast' in P['index.html'],"index missing Operation Economic Outcast")
# stale removal
for s in ['As of roughly 1:15 p.m. ET','The event risk is on the podium','Bessent takes the podium','press conference this afternoon','press conference begins at 1 p.m. ET']:
    ck(s not in ws+cy+P['index.html'],"stale string still present: "+s)
# cached blacklist absent from lead block only
lead=re.search(r'<div class="lab">The lead</div>(.*?)</section>',ws,re.S).group(1)
for s in ['7,652.36','53,441.18','25,971.85','7,674.37','53,277.01','26,180.46']:
    ck(s not in lead,"cached/Friday figure in lead: "+s)
ck('7,674.37' in ws,"Friday close should remain in scorecard")
# trap greps
for s in ['Cody Salkilld','Abdul-Rakhman','Shamil Yakhyaev','title challenger Beneil','2 p.m.']:
    for f,h in P.items():
        ck(s not in h,"trap '%s' in %s"%(s,f))
ck('1 p.m. ET' in ws and '1 p.m. ET' in cy,"1 p.m. ET must be on WS and CY")
print("CHECKS:",N,"FAILURES:",len(FAIL))
for f in FAIL: print("  FAIL:",f)
