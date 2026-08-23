import re,json,sys,datetime
from html.parser import HTMLParser
O="/sessions/nice-relaxed-galileo/mnt/outputs/"
pages=["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]
fails=[];checks=0
def ck(c,msg):
    global checks
    checks+=1
    if not c: fails.append(msg)
VOID={'meta','link','br','hr','img','input','source','col','area','base','embed','param','track','wbr'}
class P(HTMLParser):
    def __init__(s):
        super().__init__();s.st=[];s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
            s.err.append(t)
        else: s.err.append('stray '+t)
src={}
for p in pages:
    src[p]=open(O+p,encoding='utf-8').read()
    pr=P();pr.feed(src[p])
    ck(not pr.st and not pr.err, f"{p}: unclosed={pr.st[:5]} errs={pr.err[:5]}")

# nav + ids
for p in pages:
    s=src[p]
    for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        ck(f'href="{href}"' in s, f"{p}: missing nav link {href}")
    for i in ["edition","datestamp","updated","freshline"]:
        ck(f'id="{i}"' in s, f"{p}: missing id {i}")
    n=len(re.findall(r'class="on"',s))+ (1 if p=="index.html" and 'border-color:#e8edf2' in s else 0)
    ck(n==1, f"{p}: active tab count {n}")

# tldr labels
for p,lab in [("cyber-briefing.html","The Wire"),("wallstreet-briefing.html","The Tape"),("mma-briefing.html","Tale of the Tape")]:
    ck(f'<b>{lab}</b>' in src[p], f"{p}: tldr label")
ck('class="tldr"' not in src["index.html"], "index must not have tldr")

# tradingview widget JSON
ws=src["wallstreet-briefing.html"]
blocks=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>',ws,re.S)
ck(len(blocks)==8, f"widget block count {len(blocks)}")
for b in blocks:
    try: json.loads(b)
    except Exception as e: fails.append("widget JSON parse: "+str(e)[:60]); checks+=1
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in ws, f"ticker missing {sym}")
ck('"symbol":"NASDAQ:HOOD"' in ws, "Chart of the Day != HOOD")

# scorecard arithmetic
rows=re.findall(r'<tr><td>(?:S&amp;P 500|Dow Jones Industrial Average|Nasdaq Composite|Russell 2000)</td><td>([\d,\.]+)</td><td class="up">\+([\d\.]+)</td><td class="up">\+([\d\.]+)%</td></tr>',ws)
ck(len(rows)==4,f"scorecard rows {len(rows)}")
for close,chg,pct in rows:
    c=float(close.replace(',',''));d=float(chg);p=float(pct)
    calc=d/(c-d)*100
    ck(abs(calc-p)<0.006, f"scorecard math {close}: calc {calc:.4f} vs {p}")

# KEV countdowns
cy=src["cyber-briefing.html"]
today=datetime.date(2026,8,23)
lis=re.findall(r'<li><strong>(CVE-\d{4}-\d+)</strong>.*?due <strong>(\w+ \d+)</strong>\.\s*<span class="(kev-crit|kev-soon|kev-ok)">([^<]+)</span>',cy,re.S)
ck(len(lis)==12, f"KEV rows {len(lis)}")
past=0;duetoday=0
for cve,due,cls,label in lis:
    m,d=due.split();mo={'Aug':8,'Sep':9}[m];dt=datetime.date(2026,mo,int(d))
    delta=(dt-today).days
    if delta<0:
        past+=1
        ck(cls=="kev-crit" and f"{-delta} days PAST DUE"==label, f"{cve}: expected {-delta} past due, got '{label}'/{cls}")
    elif delta==0:
        duetoday+=1
        ck(cls=="kev-crit" and "DUE TODAY" in label, f"{cve}: due-today label '{label}'/{cls}")
    else:
        exp="kev-soon" if delta<=2 else "kev-ok"
        unit="day" if delta==1 else "days"
        ck(cls==exp and label==f"{delta} {unit} left", f"{cve}: expected {delta} {unit} left/{exp}, got '{label}'/{cls}")
ck(past==7, f"past due count {past}")
ck(duetoday==1, f"due today count {duetoday}")
ck("12 entries tracked here, 7 are past due, 1 comes due today and 4 remain" in cy, "KEV summary sentence mismatch")
ck('<div class="n">12</div>' in cy and '<div class="n">7</div>' in cy, "stat strip counts")
# patch priority agrees with KEV
ck("CVE-2026-72529" in cy and "CVSS 9.8" in cy, "patch priority CVE/CVSS")
ck(cy.count("August 23")>=1 or "Aug 23" in cy, "patch priority date")

# champions
mm=src["mma-briefing.html"]
champrows=re.findall(r'<tr><td>(Heavyweight|Light Heavyweight|Middleweight|Welterweight|Lightweight|Featherweight|Bantamweight|Flyweight|Women&rsquo;s Flyweight|Women&rsquo;s Bantamweight|Women&rsquo;s Strawweight)</td><td>([^<]+)</td>',mm)
ck(len(champrows)==11, f"champion rows {len(champrows)}")
ck(not any(n.strip().lower() in ("vacant","tbd","") for _,n in champrows), "vacant champion cell")
exp={"Heavyweight":"Tom Aspinall","Light Heavyweight":"Carlos Ulberg","Middleweight":"Sean Strickland","Welterweight":"Islam Makhachev","Lightweight":"Justin Gaethje","Featherweight":"Alexander Volkanovski","Bantamweight":"Petr Yan","Flyweight":"Joshua Van","Women&rsquo;s Flyweight":"Valentina Shevchenko","Women&rsquo;s Bantamweight":"Kayla Harrison","Women&rsquo;s Strawweight":"Mackenzie Dern"}
for div,name in champrows:
    ck(exp[div]==name, f"champion {div}: {name}")

# results table 13 rows
ck(len(re.findall(r'<tr><td class="win">',mm))==13, "results rows != 13")

# trap greps
traps=["Cody Salkilld","Shamil Yakhyaev","Abdul-Rakhman","MacKenzie","Joshua Vance","Pereira (205)","pay-per-view","former champion at light","Jahmall Emmers def"]
for t in traps:
    for p in pages:
        ck(t not in src[p], f"{p}: trap '{t}' present")
# stale champion cells
for bad in ["<td>Middleweight</td><td>Khamzat","<td>Flyweight</td><td>Alexandre","<td>Bantamweight</td><td>Merab","<td>Lightweight</td><td>Ilia"]:
    ck(bad not in mm, f"stale champion cell {bad}")

# countdown target
ck("2026-08-29T06:00:00-04:00" in mm, "countdown target")
ck('id="ufccdn"' in mm, "ufccdn id")

# no after-hours section (weekend)
ck("After-Hours Movers" not in ws or "No After-Hours Movers section appears" in ws, "after-hours handling")

print(f"CHECKS: {checks}  FAILURES: {len(fails)}")
for f in fails: print("  FAIL:",f)
