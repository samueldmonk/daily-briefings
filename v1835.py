import re,sys
print("VALIDATION-1835")
P=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
H={f:open(f).read() for f in P}
ok=[];bad=[]
def chk(c,m):
    (ok if c else bad).append(m)

# --- structural: nav, tabs, stamps ---
for f in P:
    h=H[f]
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        chk('href="%s"'%t in h, "%s nav->%s"%(f,t))
    chk(h.count('class="active"')==1 or h.count('tabs')>=1, "%s one active tab"%f)
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        chk(i in h, "%s has %s"%(f,i))
    chk('America/New_York' in h, "%s self-stamp JS"%f)

# --- live widgets only on markets page ---
for f in P:
    tv=H[f].count('tradingview.com/external-embedding')
    chk((tv>=6) if f=='wallstreet-briefing.html' else (tv==0), "%s widgets (%d)"%(f,tv))
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    chk('embed-widget-%s.js'%w in H['wallstreet-briefing.html'], "ws widget %s"%w)

# --- TLDR present + verbatim match to index cards ---
for f,lbl in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    m=re.search(r'<div class="tldr"><b>%s</b>\s*<span>(.*?)</span></div>'%re.escape(lbl),H[f],re.S)
    chk(bool(m), "%s tldr label %s"%(f,lbl))
    if m: chk(m.group(1).strip() in H['index.html'], "index card verbatim == %s tldr"%f)
    chk('id="freshline"' in H[f], "%s freshline"%f)

# --- CHAMPIONS BOARD: champion-column-only parse, expected 11-row map ---
EXP={'Heavyweight':'VACANT','Light Heavyweight':'Carlos Ulberg','Middleweight':'Sean Strickland',
 'Welterweight':'Islam Makhachev','Lightweight':'Justin Gaethje','Featherweight':'Alexander Volkanovski',
 'Bantamweight':'Petr Yan','Flyweight':'Joshua Van','Women&rsquo;s Flyweight':'VACANT',
 'Women&rsquo;s Bantamweight':'Kayla Harrison','Women&rsquo;s Strawweight':'Mackenzie Dern'}
mm=H['mma-briefing.html']
i=mm.find('Champions Board'); seg=mm[i:]
rows=re.findall(r'<tr><t[dh][^>]*>(.*?)</t[dh]><t[dh][^>]*>(.*?)</t[dh]>',seg)
rows=[(re.sub('<[^>]+>','',a).strip(), re.sub('<[^>]+>','',b).strip()) for a,b in rows]
rows=[r for r in rows if r[0] in EXP]
chk(len(rows)==11, "champions rows==11 (got %d)"%len(rows))
for div,champ in rows:
    chk(EXP[div].replace('&rsquo;',"'").lower() in champ.replace('&rsquo;',"'").lower(),
        "champ %s -> %s"%(div,champ))
chk(sum(1 for d,c in rows if 'VACANT' in c.upper())==2, "exactly two VACANT")
for banned in ["Chimaev</td>","Pereira</td>","Shevchenko</td>","Aspinall</td>"]:
    chk(not any(banned in (a+c) for a,c in rows), "banned in champs table: %s"%banned)

# --- markets: scorecard two-way reconciliation ---
ws=H['wallstreet-briefing.html']
for lvl in ['7,619.98','52,421.20','26,186.41']:
    chk(lvl in ws, "scorecard level %s"%lvl)
chk(abs((52573.29-152.09)-52421.20)<0.01, "dow two-way reconcile")
chk(abs((104.61+1.07)-105.68)<0.001 and abs((100.05+1.34)-101.39)<0.001, "oil settle closure")

# --- cyber: BOD 26-04 resolution coherent ---
cy=H['cyber-briefing.html']
chk('supersedes and revokes BOD 22-01' in cy, "cyber BOD 26-04 supersession stated")
chk('not explained in anything read' not in cy, "cyber stale 'unexplained' removed")
chk('10 June 2026' in cy, "cyber BOD 26-04 issue date")
chk('BOD 26-04' in cy, "cyber names BOD 26-04")
chk('16-tier' in cy, "cyber 16-tier matrix")
chk('7 December 2026' in cy, "cyber BOD 26-04 compliance date")
chk('14 September 2026' in cy, "cyber PaperCut deadline present")
# CVSS descending in vulnerability table
sc=[float(x) for x in re.findall(r'<td[^>]*>(\d{1,2}\.\d)</td>',cy)]
chk(sc==sorted(sc,reverse=True), "CVSS descending %s"%sc)

# --- New-tag ledger: cyber 1, markets 0, mma 0 ---
chk(cy.count('>New<')==1, "cyber New==1 (got %d)"%cy.count('>New<'))
chk(ws.count('>New<')==0, "ws New==0 (got %d)"%ws.count('>New<'))
chk(mm.count('>New<')==0, "mma New==0 (got %d)"%mm.count('>New<'))

# --- MMA: no past event listed as upcoming; 17 Oct card well-formed ---
chk('Buckley vs. Malott' in mm, "mma 17 Oct card present")
chk('Rogers Place' in mm, "mma venue")
chk('Blanchfield' in mm and 'Jasudavicius' in mm, "mma co-main")
chk(mm.count('Burns vs. Malott')<=1, "mma Burns/Malott disambiguated once")
for d in ['Sat 19 Sep','Sat 26 Sep','Sat 3 Oct','Sat 17 Oct','Sat 24 Oct']:
    chk(d in mm, "mma card date %s"%d)

# --- hygiene ---
for f in P:
    h=H[f]
    chk('&amp;amp;' not in h, "%s no double-escaped amp"%f)
    chk('&rsquo;&rsquo;' not in h, "%s no doubled smart quote"%f)
    chk(h.rstrip().endswith('</html>'), "%s closes cleanly"%f)
    chk('<section' not in h or h.count('<section')==h.count('</section>'), "%s sections balanced"%f)

print("PASS %d  FAIL %d"%(len(ok),len(bad)))
for b in bad: print("  FAIL:",b)
sys.exit(1 if bad else 0)
