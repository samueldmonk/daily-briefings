import re,sys
D='/sessions/youthful-laughing-hamilton/mnt/outputs/'
F=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
H={f:open(D+f).read() for f in F}
ok=fail=0; msgs=[]
def chk(cond,label):
    global ok,fail
    if cond: ok+=1
    else: fail+=1; msgs.append('FAIL: '+label)

# 1. tag balance
for f in F:
    h=H[f]
    for tag in ['div','p','span','h2','h3','h4','h5','table','tr','td','th','ul','li','b','i','a','footer','nav','header','section','script','style']:
        o=len(re.findall(r'<%s[\s>]'%tag,h)); c=len(re.findall(r'</%s>'%tag,h))
        if tag in ('p','li','td','tr','th'):
            chk(c<=o,f'{f} {tag} closers<=openers ({o}/{c})')
        else:
            chk(o==c,f'{f} {tag} balance {o}/{c}')

# 2. masthead / nav / stamp
for f in F:
    h=H[f]
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        chk(i in h, f'{f} has {i}')
    for link in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        chk(f'href="{link}"' in h, f'{f} nav links {link}')
    chk(len(re.findall(r'<a href="[^"]+" class="on">',h))==1, f'{f} exactly one active nav tab')
    chk("America/New_York" in h, f'{f} self-stamp JS present')
    chk('.tldr{' in h or f=='index.html', f'{f} tldr css')

# 3. widgets only on wallstreet
ws=H['wallstreet-briefing.html']
tv=len(re.findall(r's3\.tradingview\.com/external-embedding/embed-widget-([a-z\-]+)\.js',ws))
kinds=set(re.findall(r'embed-widget-([a-z\-]+)\.js',ws))
chk(tv==8,f'wallstreet 8 TradingView scripts (got {tv})')
chk(kinds=={'ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events'},f'six widget blocks: {kinds}')
chk(len(re.findall(r'embed-widget-single-quote\.js',ws))==3,'three single-quote widgets')
for f in ['index.html','cyber-briefing.html','mma-briefing.html']:
    chk('tradingview.com' not in H[f], f'{f} has no widgets')
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    chk(sym in ws, f'ticker keeps {sym}')

# 4. arithmetic
chk(round(52786.07-405.41,2)==52380.66,'Dow close reconciles')
chk(round(7673.52-7636.36,2)==37.16 and abs(37.16/7673.52*100-0.48)<0.01,'S&P reconciles')
chk(round(26421.41-26253.34,2)==168.07 and abs(168.07/26421.41*100-0.64)<0.01,'Nasdaq reconciles')
chk(round(2960.20-2921.50,2)==38.70,'Russell point change 38.70')
r=38.70/2960.20*100
chk(1.295<r<1.315,f'Russell % {r:.3f} rounds to 1.30/1.31')
chk(abs((0.79-0.21)/0.21*100-276.19)<0.01,'AEO surprise 276.19%')

# 5. refused / guarded strings
chk('7,636.59' not in ws,'refused Nasdaq level absent')
chk(ws.count('7,651.18')==1,'stale S&P level only in refusal')
chk('2,921.50' in ws and ws.count('&minus;1.31%')>=3,'Russell close present in lead/table/snapshots')
cy=H['cyber-briefing.html']
chk('Nevada' not in cy,'no Nevada')
chk('CVE-2026-3055' not in cy,'no retracted CVE')
for pair in [('CVE-2026-86218','10.0'),('CVE-2026-82078','9.4'),('CVE-2026-81578','8.8'),('CVE-2026-49869','10.0'),('CVE-2026-82329','9.8'),('CVE-2026-9586','9.3'),('CVE-2026-59822','8.8'),('CVE-2026-48710','6.5'),('CVE-2026-75650','10.0'),('CVE-2026-86206','6.9'),('CVE-2026-86207','7.7')]:
    chk(pair[0] in cy and pair[1] in cy, f'cyber carries {pair[0]} / {pair[1]}')
chk(cy.count('11 September')>=3,'KEV 11 Sep deadline consistent')
chk('16 September 2026' in cy,'16 Sep deadline')
chk(cy.count('id="kevcdn"')==1 and cy.count('id="kev2cdn"')==1,'two countdown spans in strip')
chk('440 servers across 395 organisations in 48 countries' in cy,'PaperCut figures')
chk('3.5 million' in cy and 'The Gentlemen' in cy,'Veradigm claim carried as attacker claim')
chk(cy.count('<span class="t new">New</span>')==2,'exactly two New cards on cyber')

# 6. MMA guards
mm=H['mma-briefing.html']
chk('Salahdine Parnasse' in mm and 'Saladhine' not in mm and 'Cody Salkilld' not in mm,'Parnasse spelling')
chk('stripped' not in mm,'"stripped" absent')
chk('athletic commission' not in mm,'no unverified commission detail')
chk('Contender Series' in mm and 'He did <b>not</b> come through the Contender Series.' in mm,'Contender Series refusal kept')
for champ in ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje','Alexander Volkanovski','Petr Yan','Joshua Van','Kayla Harrison','Mackenzie Dern']:
    chk(champ in mm, f'champion row {champ}')
chk(re.search(r'Light Heavyweight</td>\s*<td><b>Carlos Ulberg',mm) is not None,'LHW = Ulberg')
chk(re.search(r'Middleweight</td>\s*<td><b>Sean Strickland',mm) is not None,'MW = Strickland')
chk(re.search(r"Women&rsquo;s Flyweight</td><td[^>]*><b>Vacant</b>",mm) is not None,'125lb vacant')
chk(mm.count('<span class="t new">Updated</span>')==1,'exactly one Updated card on MMA')
chk('<span class="t new">New</span>' not in mm,'zero New tags on MMA')
chk('&minus;440' in mm and '+340' in mm and 'DraftKings' in mm,'fresh odds present')
chk('Josh Hokit' in mm and 'no bout involving any of the three has been announced' in mm,'callouts carried as unbooked')
chk('ufccdn' in mm,'MMA countdown target present')

# 7. index cards match tldrs
def strip(s): return re.sub(r'<[^>]+>','',s).strip()
ix=H['index.html']
cards=[strip(m) for m in re.findall(r'<p>(.*?)</p>',ix,flags=re.S)]
for f,accent in [('cyber-briefing.html',None),('wallstreet-briefing.html',None),('mma-briefing.html',None)]:
    t=re.search(r'class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span>',H[f],flags=re.S)
    chk(t is not None,f'{f} tldr present')
    if t: chk(strip(t.group(1)) in cards, f'index card matches {f} tldr')

# 8. sources footers
for f in F:
    chk(H[f].count('<footer>')==1 and 'Sources' in H[f], f'{f} sources footer')
    chk(len(re.findall(r'<a href="https?://',H[f]))>=10, f'{f} has source links')
chk('nothing here is investment advice' in H['wallstreet-briefing.html'].lower(),'markets disclaimer')
chk('subject to change' in H['mma-briefing.html'],'MMA disclaimer')
chk('not security advice' in cy,'cyber disclaimer')

# 9. freshness / structure order on wallstreet
chk(ws.find('After-Hours Movers')>ws.find('Live Market Headlines'),'after-hours after headlines block')
chk(ws.find('<h2 class="sec">Weekly Scorecard')>ws.find('<h2 class="sec">After-Hours Movers'),'scorecard section after after-hours section')
chk(ws.find('LIVE QUOTES')<ws.find('The Lead'),'ticker tape before lead')
chk(cy.find('Threat level')<cy.find('Top Story')<cy.find('Patch Priority')<cy.find('Threat Actor Spotlight')<cy.find('Breaches &amp; Incidents')<cy.find('Vulnerability Watch')<cy.find('CISA KEV'),'cyber section order')
chk(mm.find('Next card')<mm.find('Top Story')<mm.find('Fight Week')<mm.find('Last Event')<mm.find('Prospect Watch')<mm.find('Around the Sport')<mm.find('Champions Board'),'mma section order')

print(f'{ok+fail} checks, {fail} failures')
for m in msgs: print(m)
sys.exit(1 if fail else 0)
