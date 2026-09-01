# -*- coding: utf-8 -*-
import io,re,sys
D='/tmp/db_1788305419/'
F={k:io.open(D+v,encoding='utf-8').read() for k,v in
   {'idx':'index.html','cy':'cyber-briefing.html','ws':'wallstreet-briefing.html','mma':'mma-briefing.html'}.items()}
raised=[]; checks=0
def ck(cond,msg):
    global checks; checks+=1
    if not cond: raised.append(msg)

# ---- structural: every page ----
for k,s in F.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%tab in s, '%s: nav missing %s'%(k,tab))
    for i in ['datestamp','updated','edition']:
        ck('id="%s"'%i in s, '%s: missing id=%s'%(k,i))
    ck("getElementById('edition')" in s, '%s: self-stamp JS missing'%k)
    ck(s.count('class="on"')==1, '%s: active tab count != 1'%k)
    ck('Morning Edition' in s and 'Afternoon Edition' in s, '%s: edition buckets missing'%k)
for k in ['cy','ws','mma']:
    ck('class="tldr"' in F[k], '%s: tldr missing'%k)
    ck('id="freshline"' in F[k], '%s: freshline missing'%k)
ck('<b>The Tape</b>' in F['ws'],'ws tldr label'); ck('<b>The Wire</b>' in F['cy'],'cy tldr label')
ck('<b>Tale of the Tape</b>' in F['mma'],'mma tldr label')
ck('class="tldr"' not in F['idx'],'index must use cards not tldr')

# ---- live widget blocks A-F on wallstreet ----
for w in ['embed-widget-ticker-tape','embed-widget-single-quote','embed-widget-timeline',
          'embed-widget-stock-heatmap','embed-widget-mini-symbol-overview','embed-widget-events']:
    ck(w in F['ws'], 'ws: widget %s missing'%w)
ck(F['ws'].count('embed-widget-single-quote')==3,'ws: need exactly 3 single-quote widgets')
for req in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(req in F['ws'],'ws: ticker tape missing %s'%req)
ck('class="livebar"' in F['ws'],'ws: livebar wrapper missing')
# chart-of-day widget must be bound to the session mover, not an after-hours name
mini=re.search(r'embed-widget-mini-symbol-overview\.js" async>\{"symbol":"([A-Z:]+)"',F['ws'])
ck(bool(mini),'ws: mini chart symbol unreadable')
if mini: ck(mini.group(1)=='NASDAQ:ALMS','ws: chart bound to %s, expected NASDAQ:ALMS'%mini.group(1))
ck('NYSE:DELL' not in (mini.group(0) if mini else ''),'ws: chart must not be an after-hours name')
ck('ufccdn' in F['mma'],'mma: countdown target missing')
ck('embed-widget' not in F['idx'],'index must carry no live widgets')

# ---- CHAMPIONS BOARD (CORRECTIONS.md authoritative) ----
champs={'Heavyweight':'Tom Aspinall','Light Heavyweight':'Carlos Ulberg','Middleweight':'Sean Strickland',
 'Welterweight':'Islam Makhachev','Lightweight':'Justin Gaethje','Featherweight':'Alexander Volkanovski',
 'Bantamweight':'Petr Yan','Flyweight':'Joshua Van'}
m=F['mma']; tbl=m[m.find('<h2>Champions Board</h2>'):]
tbl=tbl[:tbl.find('</table>')]
for div,ch in champs.items():
    r=re.search(r'<td>%s</td><td><b>([^<]+)</b></td>'%re.escape(div),tbl)
    ck(bool(r) and r.group(1)==ch,'champs: %s = %s (expected %s)'%(div,r.group(1) if r else 'MISSING',ch))
for div,ch in {"Women&rsquo;s Flyweight":'Valentina Shevchenko',"Women&rsquo;s Bantamweight":'Kayla Harrison',
               "Women&rsquo;s Strawweight":'Mackenzie Dern'}.items():
    ck(ch in tbl,'champs: missing %s'%ch)
ck('Ciryl Gane' in tbl,'champs: interim HW Gane missing')
# banned stale pairings must never assert a current belt
ck(not re.search(r'<td>Light Heavyweight</td><td><b>Alex Pereira',tbl),'BANNED: Pereira at LHW')
ck(not re.search(r'<td>Middleweight</td><td><b>Khamzat Chimaev',tbl),'BANNED: Chimaev at MW')
ck(not re.search(r'<td>Lightweight</td><td><b>Ilia Topuria',tbl),'BANNED: Topuria at LW')
ck('Featherweight</td><td><b>Vacant' not in tbl,'BANNED: featherweight vacant')
# every Chimaev mention on the page must sit next to a correction//past-tense marker
# a guard must test the CLAIM, not forbid the NAME: Chimaev is legitimately discussed
# throughout the stale-list narrative. Ban only affirmative present-tense belt assertions.
for pat in [r'Chimaev[^.<]{0,40}\bis\b[^.<]{0,40}(?:middleweight )?champion',
            r'champion[^.<]{0,30}Khamzat Chimaev',
            r'Chimaev[^.<]{0,30}(?:retains|defends|holds)[^.<]{0,30}(?:the )?(?:middleweight )?(?:title|belt)',
            r'reigning[^.<]{0,30}Chimaev']:
    ck(not re.search(pat,m,re.I),'BANNED ASSERTION: Chimaev as current MW champion (%s)'%pat)
_mw=re.search(r'<td>Middleweight</td><td><b>([^<]+)</b></td>',
              m[m.find('<h2>Champions Board</h2>'):].split('</table>')[0])
ck(bool(_mw) and 'Chimaev' not in _mw.group(1),'BANNED: Chimaev in the middleweight champion cell')
ck(bool(_mw) and _mw.group(1)=='Sean Strickland','middleweight champion cell != Sean Strickland')

# ---- Parnasse standing correction ----
ck('Saladhine' not in m,'MISSPELLING: Saladhine')
ck('Salahdine' in m,'Parnasse first name missing')
# Parnasse and the Contender Series legitimately co-occur (the page CORRECTS the link, and
# both appear in the source list). Ban only an affirmative attribution.
for pat in [r'Parnasse[^.<]{0,80}(?:through|on|via|out of|off)[^.<]{0,20}(?:Dana White(?:&rsquo;|\')s )?Contender Series',
            r'Contender Series[^.<]{0,60}(?:produced|graduate|alum)[^.<]{0,40}Parnasse',
            r'Parnasse[^.<]{0,60}(?:won|earned|secured)[^.<]{0,40}contract[^.<]{0,40}Contender Series']:
    for mo in re.finditer(pat,m,re.I):
        ctx=m[max(0,mo.start()-260):mo.end()+120]
        ck(any(t in ctx for t in ['did <i>not</i>','did  not','not  reach','It is not.','was wrong','previously credited','not through the Contender Series','directly out of KSW']),
           'BANNED ATTRIBUTION: Parnasse credited to the Contender Series')
ck('signed directly out of KSW' in m or 'signed with the UFC in late July 2026' in m,
   'Parnasse KSW provenance sentence missing')
ck('KSW' in m,'Parnasse KSW provenance missing')

# ---- markets arithmetic (levels must back out to Monday) ----
w=F['ws']
for lvl in ['7,631.47','26,099.77','52,766.88']: ck(lvl in w,'ws: missing close %s'%lvl)
ck(abs((53185.90-52766.88)-419.02)<0.005,'Dow points do not reconcile')
ck(abs((7686.14-7631.47)-54.67)<0.005,'S&P points do not reconcile')
ck(abs((26370.89-26099.77)-271.12)<0.005,'Nasdaq points do not reconcile')
# the Sep-1-wrap trap: Monday's closes must never be labelled as Sept 1 closes in the scorecard
_sci=w.find('<h2>Weekly Scorecard')
ck(_sci>0,'ws: Weekly Scorecard heading missing')
sc=w[_sci:_sci+1600]
ck('7,686.14' in sc and '53,185.90' in sc,'scorecard prior-close column missing')
ck(not re.search(r'<td>7,686\.14</td><td class="down">&minus;54\.67',sc),'TRAP: Monday level in Sept 1 column')

# ---- KEV deadlines: stated, never derived ----
c=F['cy']
ck('September 14' in c or 'Sept 14' in c,'cy: PaperCut Sept 14 deadline missing')
ck('August 29' in c,'cy: Citrix Aug 29 deadline missing')
ck('three days overdue' in c,'cy: Citrix overdue count missing')
ck('September 21' not in c,'cy: derived 21-day PaperCut date present')
ck(c.count('8.8')>=1 and c.count('9.4')>=1,'cy: PaperCut CVSS pair missing')
ck('9.8' in c,'cy: JFrog CVSS missing')

# ---- "New" markers: cap + must attach to a real h3, never inside <style> ----
for k in ['cy','ws','mma']:
    s=F[k]; sty=s[s.find('<style>'):s.find('</style>')]
    ck('>New<' not in sty,'%s: New marker inside <style>'%k)
    for mo in re.finditer(r'class="tag t-new">New</span>',s):
        ck('<h3' in s[mo.end():mo.end()+400],'%s: New marker not attached to an h3'%k)
    ck(s.count('class="tag t-new">New</span>')<=6,'%s: too many New markers'%k)

# ---- chronology: nothing "tonight" that has started ----
ck('runs tonight' not in m,'mma: stale "runs tonight" for a started card')
ck('under way' in m,'mma: DWCS live state missing')
ck('fourteenth' in m,'mma: stale-list counter not incremented')

# ---- index cards must mirror each page's own tldr lead ----
for name,frag in [('Dell','Dell reported record quarterly revenue of $47 billion'),
                  ('phantom','phantom'),('fourteenth','fourteenth')]:
    ck(frag in F['idx'],'index card missing %s'%name)
ck('Dell' in w and '60.9' in w,'ws: Dell order book figure missing')
ck('$95' in w,'ws: Dell backlog figure missing')
ck('$192' in w,'ws: Dell guidance figure missing')
ck('286.3' in w,'ws: GitLab revenue missing')
ck('771.8' in w,'ws: MongoDB revenue missing')

# ---- provenance convention must be stated wherever "this run" is used at scale ----
for k in ['cy','ws','mma']:
    if F[k].count('this run')>5:
        ck('A note on the words' in F[k],'%s: uses "this run" at scale without the provenance note'%k)
def _live_markers(s):
    return len(re.findall(r'(?<!&ldquo;)\bNew this run\b(?!&rdquo;)',
                          re.sub(r'&ldquo;New this run&rdquo;','',s)))
ck(_live_markers(F['cy'])==0,'cy: asserting "New this run" marker present')
ck(_live_markers(F['mma'])==0,'mma: asserting "New this run" marker present')
ck(_live_markers(F['ws'])<=1,'ws: more than one asserting "New this run" marker')
# and the one that remains must be the Japan 2-year row added in THIS edition
if _live_markers(F['ws'])==1:
    _w=re.sub(r'&ldquo;New this run&rdquo;','',F['ws'])
    _i=_w.find('New this run')
    ck(_i>0 and 'Japan 2-year' in _w[max(0,_i-260):_i],'ws: surviving marker is not this edition\'s addition')

print('checks:',checks,'raised:',len(raised))
for r in raised: print('  !!',r)
sys.exit(1 if raised else 0)
