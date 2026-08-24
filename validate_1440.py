import re,json,sys
from html.parser import HTMLParser
F=0;C=0
def ck(cond,msg):
    global F,C
    C+=1
    if not cond: F+=1; print("FAIL:",msg)
P=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
D={p:open(p,encoding='utf-8').read() for p in P}
VOID={'br','img','meta','link','hr','input','source','col','area','base','wbr','embed','track','param'}
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
for p,s in D.items():
    b=B(); b.feed(s)
    ck(len(b.st)==0 and b.bad==0, f"{p} balance unclosed={b.st[:5]} stray={b.bad}")

# nav
for p,s in D.items():
    nav=re.search(r'<nav class="tabs">(.*?)</nav>',s,re.S)
    ck(bool(nav),f"{p} nav")
    if nav:
        hrefs=re.findall(r'href="([^"]+)"',nav.group(1))
        ck(set(hrefs)=={'index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html'},f"{p} 5 tabs {hrefs}")
        ck(len(re.findall(r'class="[^"]*\bon\b[^"]*"',nav.group(1)))==1,f"{p} exactly 1 active tab")
    for i in ('datestamp','updated','edition'):
        ck(f'id="{i}"' in s,f"{p} id={i}")
    ck('id="freshline"' in s,f"{p} freshline")

# tldr
labs={'cyber-briefing.html':'The Wire','wallstreet-briefing.html':'The Tape','mma-briefing.html':'Tale of the Tape'}
for p,l in labs.items():
    t=re.findall(r'<div class="tldr"><b>([^<]+)</b>',D[p])
    ck(t==[l],f"{p} tldr label {t}")
ck('class="tldr"' not in D['index.html'],"index has no tldr")
# index cards carry each tldr verbatim
for p in labs:
    span=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>',D[p],re.S).group(1)
    ck(span in D['index.html'],f"index card matches {p} tldr")

# TradingView widgets
blocks=re.findall(r'embed-widget-[a-z\-]+\.js"\s+async>(\{.*?\})</script>',D['wallstreet-briefing.html'],re.S)
ck(len(blocks)==8,f"8 widget blocks, got {len(blocks)}")
for i,b in enumerate(blocks):
    try: json.loads(b)
    except Exception as e: ck(False,f"widget {i} JSON {e}")
tape=json.loads(re.search(r'embed-widget-ticker-tape\.js"\s+async>(\{.*?\})</script>',D['wallstreet-briefing.html'],re.S).group(1))
syms=[x['proName'] for x in tape['symbols']]
for need in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(need in syms,f"ticker keeps {need}")
mini=json.loads(re.search(r'embed-widget-mini-symbol-overview\.js"\s+async>(\{.*?\})</script>',D['wallstreet-briefing.html'],re.S).group(1))
ck(mini['symbol']=='NASDAQ:AAOI',f"chart of day = AAOI, got {mini['symbol']}")

# KEV countdowns
kev=re.findall(r'<span class="kevdue([^"]*)">([^<]*)<',D['cyber-briefing.html'])
ck(len(kev)==12,f"12 KEV rows, got {len(kev)}")
past=sum(1 for c,t in kev if 'PAST DUE' in t)
today=sum(1 for c,t in kev if 'DUE TODAY' in t)
ahead=len(kev)-past-today
ck((past,today,ahead)==(8,1,3),f"KEV split 8/1/3 got {past}/{today}/{ahead}")

# champions column only
mma=D['mma-briefing.html']
tbl=re.search(r'Champions board.*?<table>(.*?)</table>',mma,re.S).group(1)
rows=re.findall(r'<tr>(.*?)</tr>',tbl,re.S)
champs=[]
for r in rows[1:]:
    tds=re.findall(r'<td[^>]*>(.*?)</td>',r,re.S)
    if len(tds)>=2: champs.append(re.sub('<[^>]+>','',tds[1]))
ck(len(champs)==11,f"11 champion cells, got {len(champs)}")
col=' | '.join(champs)
for n in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van']:
    ck(n in col,f"champion {n} present")
for bad in ['Pereira','Chimaev','Topuria','vacant','Vacant']:
    ck(bad not in col,f"stale champion '{bad}' absent from champion column")

# Friday closes / blacklist absent from lead block only
lead=re.search(r'<div class="lead">(.*?)</div>\s*</section>',D['wallstreet-briefing.html'],re.S).group(1)
for bad in ['7,674.37','53,277.01','7,652.36','53,441.18','25,971.85']:
    ck(bad not in lead,f"'{bad}' absent from lead block")
ck('7,674.37' in D['wallstreet-briefing.html'],"7,674.37 present elsewhere (scorecard)")

# fresh strings
fresh_ws=['2:40 p.m. ET','third consecutive run','fifth time today','5h 6m','0.28%','0.39%','2.06%','$85.33','$4,702.70','Alibaba&rsquo;s AI bill','&#165;380&nbsp;billion','$88.74','Hang Seng TECH']
for f in fresh_ws: ck(f in D['wallstreet-briefing.html'],f"fresh WS string '{f}'")
# stale strings gone
for st in ['As of roughly 2:20 p.m. ET','Two freshness caveats apply','<b>New this edition.</b> The morning','$4,671.09</td>','<td>$84.73</td>']:
    ck(st not in D['wallstreet-briefing.html'],f"stale WS string gone: '{st}'")

# New tag counts
for p,n in [('wallstreet-briefing.html',1),('cyber-briefing.html',0),('mma-briefing.html',0)]:
    c=len(re.findall(r'class="tag new"',D[p]))
    ck(c==n,f"{p} New tags == {n}, got {c}")
# footnote claim matches
ck('Exactly one card is tagged New this edition &mdash; Alibaba' in D['wallstreet-briefing.html'],"movers footnote names the actual tagged card")
ck('the memory complex climbing off its lows &mdash; because it is the only' not in D['wallstreet-briefing.html'],"old footnote claim gone")

# after-hours absent (regular session)
ck(len(re.findall(r'class="lab[^"]*"[^>]*>\s*After-[Hh]ours',D['wallstreet-briefing.html']))==0,"no after-hours SECTION LABEL pre-close")
ck('No After-Hours Movers section appears in this edition' in D['wallstreet-briefing.html'],"page declares after-hours absence")
ck('U.S. markets open in 5h 6m' in D['wallstreet-briefing.html'],"cache tell quoted deliberately")

# trap greps
for p,s in D.items():
    for trap in ['Cody Salkilld','Abdul-Rakhman','Shamil Yakhyaev','title challenger Beneil','Shanghai Indoor Stadium']:
        ck(trap not in s,f"{p} trap '{trap}' absent")
# MMA venue + countdown
ck('Oriental Sports Center' in mma,"Shanghai venue = Oriental Sports Center")
ck('2026-08-29T06:00:00-04:00' in mma,"countdown target intact")
ck('id="ufccdn"' in mma,"ufccdn present")

print(f"\n{C} checks, {F} failures")
sys.exit(1 if F else 0)
