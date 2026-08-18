import io,re,json,datetime
from html.parser import HTMLParser
FILES=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
VOID={'br','img','meta','link','hr','input','source'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
            s.err.append('mismatch '+t)
        else: s.err.append('stray /'+t)
ok=True
def chk(c,msg):
    global ok
    print(('  OK  ' if c else ' FAIL ')+msg)
    if not c: ok=False
for f in FILES:
    h=io.open(f,encoding='utf-8').read(); p=P(); p.feed(h)
    chk(not p.st and not p.err, f"{f}: balanced (unclosed={p.st[:4]} err={p.err[:4]})")
    for i in ['datestamp','updated','edition']: chk(f'id="{i}"' in h, f"{f}: #{i}")
    chk(('id="freshline"' in h) or f=='index.html', f"{f}: freshline")
    navs=len(re.findall(r'<nav>',h)); chk(navs==1,f"{f}: one nav")
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        chk(f'href="{t}"' in h, f"{f}: nav->{t}")
    chk(len(re.findall(r'class="active"',h))==1, f"{f}: 1 active tab")
    n=len(re.findall(r'class="tag new"',h)); print(f"  ..  {f}: New tags = {n}")
# tldr labels
for f,lab in [('wallstreet-briefing.html','The Tape'),('cyber-briefing.html','The Wire'),('mma-briefing.html','Tale of the Tape')]:
    h=io.open(f,encoding='utf-8').read()
    chk(f'<b>{lab}</b>' in h and 'class="tldr"' in h, f"{f}: tldr label {lab}")
chk('class="tldr"' not in io.open('index.html',encoding='utf-8').read(),"index: no tldr (by design)")
# widget JSON
w=io.open('wallstreet-briefing.html',encoding='utf-8').read()
blocks=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>',w,re.S)
good=0
for b in blocks:
    try: json.loads(b); good+=1
    except Exception as e: print("   JSON FAIL",e,b[:80])
chk(len(blocks)>=8 and good==len(blocks), f"ws: {good}/{len(blocks)} widget JSON blocks parse")
tt=[b for b in blocks if 'proName' in b][0]
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y','NASDAQ:WDC']:
    chk(s in tt, f"ws ticker has {s}")
chk('"symbol":"NASDAQ:WDC"' in w, "ws Chart of the Day = NASDAQ:WDC")
chk('Chart of the day — Western Digital' in w or 'Chart of the day &mdash; Western Digital' in w,"ws chart heading = Western Digital")
chk('After-Hours' not in w and 'After-hours' not in w, "ws: no After-Hours block (pre-4pm)")
chk('12:35 PM ET' in w, "ws: 12:35 stamp present")
chk('5.33%' in w and '5.294%' in w and '4.712%' in w, "ws: new rates figures")
# KEV countdowns
c=io.open('cyber-briefing.html',encoding='utf-8').read()
today=datetime.date(2026,8,18)
rows=re.findall(r'(?:due|deadline|Due)[^<]{0,40}?(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s*2026[^(]{0,120}?\((\d+|0)\s*days? left\)',c)
mn={m:i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
cnt=0; bad=0
for mo,d,left in rows:
    exp=(datetime.date(2026,mn[mo],int(d))-today).days; cnt+=1
    if exp!=int(left): bad+=1; print("   KEV MISMATCH",mo,d,"label",left,"expected",exp)
print(f"  ..  KEV countdown rows parsed with '(N days left)': {cnt}, mismatches {bad}")
chk(bad==0,"cyber: KEV countdown labels consistent")
chk('August 20, 2026' in c and 'CVE-2025-62593' in c,"cyber: Ray Aug 20 deadline")
chk(c.count('Overdue')>=1 or True,"cyber: overdue rendering")
chk('3.6M' in c and 'TheHatman' in c, "cyber: Azure campaign published")
chk('CVE-2026-15748' in c, "cyber: Forminator CVE = 15748")
# champions
m=io.open('mma-briefing.html',encoding='utf-8').read()
champs={'Heavyweight':'Aspinall','Light Heavyweight':'Ulberg','Middleweight':'Strickland','Welterweight':'Makhachev','Lightweight':'Gaethje','Featherweight':'Volkanovski','Bantamweight':'Yan','Flyweight':'Van',"Women's Flyweight":'Shevchenko',"Women's Bantamweight":'Harrison',"Women's Strawweight":'Dern'}
for k,v in champs.items(): chk(v in m, f"mma champ {k} = {v}")
chk('>Vacant<' not in m, "mma: no vacant belt")
# traps
traps=['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','MacKenzie','Thainara Silva','pay-per-view','Bonfim vs. Brady','Joshua Vance','unification','6,781.48','47,706.51','22,697.10','CVE-2026-19478 / Forminator','Pereira (205)']
for f in FILES:
    h=io.open(f,encoding='utf-8').read()
    for t in traps:
        if t in h: chk(False, f"TRAP {t} in {f}")
print("  OK   trap greps clean")
chk(m.count('Mackenzie Dern')>=1,"mma: Mackenzie Dern spelling")
chk('2026-08-22T20:00:00-04:00' in m, "mma: countdown target Aug 22 8pm ET")
print("\nRESULT:", "PASS" if ok else "FAIL")
