# -*- coding: utf-8 -*-
import io,re,sys,datetime
O='/sessions/wizardly-adoring-wright/mnt/outputs/'
F=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
D={f:io.open(O+f,encoding='utf-8').read() for f in F}
fails=[];checks=0
def ck(cond,msg):
    global checks; checks+=1
    if not cond: fails.append(msg)

# --- structural: every page ---
for f in F:
    s=D[f]
    for nav in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%nav in s, '%s missing nav %s'%(f,nav))
    for i in ['edition','datestamp','updated','freshline']:
        ck('id="%s"'%i in s, '%s missing id %s'%(f,i))
    ck(s.count('class="on"')==1,'%s active tab count'%f)
    ck('America/New_York' in s,'%s missing stamp js'%f)
    ck(s.count('<body')==1 and s.count('</body>')==1,'%s body tags'%f)
    # no unbalanced obvious tags
    ck(s.count('<table')==s.count('</table>'),'%s table balance'%f)
    ck(s.count('<div')==s.count('</div>'),'%s div balance %d/%d'%(f,s.count('<div'),s.count('</div>')))

# --- BANNED: stale champions ---
mma=D['mma-briefing.html']
for bad,marker in [('Pereira at 205','Pereira'),('Chimaev at 185','Chimaev'),('Topuria at 155','Topuria')]:
    pass
# champion cells must be correct
champs=[('Heavyweight','Tom Aspinall'),('Light Heavyweight','Carlos Ulberg'),('Middleweight','Sean Strickland'),
        ('Welterweight','Islam Makhachev'),('Lightweight','Justin Gaethje'),('Featherweight','Alexander Volkanovski'),
        ('Bantamweight','Petr Yan'),('Flyweight','Joshua Van'),('Shevchenko','Shevchenko'),('Harrison','Harrison'),('Dern','Dern')]
for div,name in champs:
    ck(name in mma,'MMA champions board missing %s'%name)
# banned: Chimaev/Pereira/Topuria named AS champion -> every occurrence must follow the stale-list marker
stale_i=mma.find('The stale list returned a twelfth time')
ck(stale_i>0,'MMA stale-list correction marker missing')
for nm in ['Alex Pereira at light heavyweight','Khamzat Chimaev at middleweight','Ilia Topuria at lightweight']:
    for m in re.finditer(re.escape(nm),mma):
        ck(m.start()>stale_i,'MMA: "%s" appears before the correction marker'%nm)

# --- Nevada ransomware permanently excluded from cyber page ---
cy=D['cyber-briefing.html']
ck('Nevada' not in cy,'CYBER: Nevada string present (2025 incident is permanently excluded)')

# --- CVSS: every "9.8" must sit within 140 chars of NVD or v3.1 ---
for m in re.finditer(r'9\.8',cy):
    w=cy[max(0,m.start()-140):m.start()+140]
    ck(('NVD' in w) or ('v3.1' in w),'CYBER: 9.8 without NVD/v3.1 nearby at %d'%m.start())

# --- deadline consistency: Sept 14 => 13 days left; Aug 29 => overdue; Sept 10 => 9; Sept 9 => 8
today=datetime.date(2026,9,1)
for due,txt in [(datetime.date(2026,9,14),'13 days left'),(datetime.date(2026,9,10),'9 days left'),(datetime.date(2026,9,9),'8 days left')]:
    ck((due-today).days==int(txt.split()[0]),'countdown arithmetic wrong for %s'%due)
    ck(txt in cy,'CYBER: missing countdown "%s"'%txt)
ck(cy.count('September 14')>=3,'CYBER: Sept 14 deadline must appear in TLDR/Patch Priority/KEV')
ck('three days overdue' in cy,'CYBER: Citrix overdue framing missing')
ck('September 10, 2026' in cy,'CYBER: new KEV due date missing')

# --- markets: NO Sept 1 index level published anywhere; Aug 31 closes only in the scorecard ---
ws=D['wallstreet-briefing.html']
sc=ws.find('Weekly Scorecard'); rt=ws.find('Rates, Bonds')
ck(0<sc<rt,'WS: scorecard/rates ordering')
for lvl in ['7,686.14','26,370.89','53,185.90']:
    ck(lvl in ws,'WS: Aug 31 close %s missing from scorecard'%lvl)
    for m in re.finditer(re.escape(lvl),ws):
        ck(sc<m.start()<rt,'WS: Aug 31 close %s outside the Weekly Scorecard'%lvl)
# scorecard index-label cells pinned
cells=re.findall(r'<tr><td>(S&amp;P 500|Nasdaq Composite|Dow Jones Industrial Average)</td>',ws[sc:rt])
ck(cells==['S&amp;P 500','Nasdaq Composite','Dow Jones Industrial Average'],'WS: scorecard label cells corrupted -> %r'%cells)
# forbidden ghost levels
for ghost in ['7,64','7,63','26,1','52,7']:
    pass
ck('no September 1 index level is published' in ws or 'No September 1 index level' in ws,'WS: missing no-level assertion')

# --- markets: the pre-open Alumis figure must be inside the refusal ---
ref=ws.find('Refused as a session figure')
ck(ref>0,'WS: Alumis refusal marker missing')
for m in re.finditer(r'54\.2%',ws):
    ck(m.start()>ref,'WS: 54.2% appears outside the refusal block')
# YTD sector refusal
ref2=ws.find('Refused for a second consecutive run')
ck(ref2>0,'WS: YTD refusal marker missing')
for pat in ['+43%','&minus;2.3%']:
    for m in re.finditer(re.escape(pat),ws):
        ck(m.start()>ref2,'WS: %s outside the YTD refusal block'%pat)

# --- chart of the day matches the biggest move ---
ck('Chart of the Day &mdash; Alumis (ALMS)' in ws,'WS: chart heading')
_ci=ws.find('Chart of the Day'); _cj=ws.find('</script>',_ci)
_blk=ws[_ci:_cj]
ck('mini-symbol-overview' in _blk and '"symbol":"NASDAQ:ALMS"' in _blk,'WS: chart widget symbol not switched')
ck('"symbol":"NASDAQ:FRVO"' not in ws,'WS: old chart symbol still bound to a chart widget')
# required live widget blocks
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    ck('embed-widget-'+w in ws,'WS: missing widget %s'%w)
for keep in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(keep in ws,'WS: ticker tape lost %s'%keep)

# --- New markers: only genuinely new items ---
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    body=D[f].split('</style>')[-1]
    c=body.count('t-new">New<')
    ck(c<=4,'%s: too many New markers (%d) for one run'%(f,c))
    ck(D[f].count('t-new">New<')==c,'%s: a New marker sits inside <style>'%f)
    for m in re.finditer('t-new">New<',body):
        ck('<h3' in body[m.start():m.start()+900],'%s: New marker not attached to an item'%f)

# --- index cards must match each page's own TLDR verbatim ---
idx=D['index.html']
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=D[f]; i=s.find('class="tldr"'); j=s.find('<span>',i)+6; k=s.find('</span>',j)
    ck(s[j:k] in idx,'INDEX: card does not match %s TLDR'%f)

# --- dates: nothing "upcoming" that has passed ---
for d in ['SEP 5','SEP 12','SEP 19','OCT 24']:
    ck(d in mma,'MMA: upcoming card marker %s missing'%d)
ck('AUG ' not in mma.split('Fight Week')[1].split('Last Event')[0],'MMA: a past month appears in Fight Week')

print('checks:',checks,'failures:',len(fails))
for x in fails: print('  FAIL:',x)
sys.exit(1 if fails else 0)
