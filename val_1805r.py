# -*- coding: utf-8 -*-
import re,sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
P=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
D={f:open(O+f,encoding='utf-8').read() for f in P}
fails=[];n=0
def chk(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)
def has(f,t,msg=None): chk(t in D[f], msg or ('%s missing %r'%(f,t[:70])))
def hasnt(f,t,msg=None): chk(t not in D[f], msg or ('%s SHOULD NOT contain %r'%(f,t[:70])))
def cnt(f,t,k): chk(D[f].count(t)==k, '%s count %r = %d, want %d'%(f,t[:50],D[f].count(t),k))

# --- structural balance ---
for f in P:
    s=D[f]
    for tag in ['div','p','table','tr','td','h2','h3','span','ul','li']:
        o=len(re.findall(r'<%s[\s>]'%tag,s)); c=len(re.findall(r'</%s>'%tag,s))
        chk(o==c,'%s <%s> unbalanced open=%d close=%d'%(f,tag,o,c))
    # container opened first closes last
    chk(s.rstrip().endswith('</body></html>') or s.rstrip().endswith('</html>'), f+' bad tail')

# --- nav / masthead / stamp on every page ---
for f in P:
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html',
              '★ Front Page','⛨ The Cyber Wire','▲ The Closing Bell','⊘ The Octagon','🗄 Archive']:
        has(f,t)
    for t in ['id="edition"','id="datestamp"','id="updated"','id="freshline"',
              "America/New_York",'Morning Edition','Midday Edition','Afternoon Edition',
              'briefings refresh every 30 minutes']:
        has(f,t)

# --- tldr labels ---
has('cyber-briefing.html','<b>The Wire</b>'); has('wallstreet-briefing.html','<b>The Tape</b>')
has('mma-briefing.html','<b>Tale of the Tape</b>')
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    has(f,'<div class="tldr">')

# --- TradingView blocks (WS) ---
ws='wallstreet-briefing.html'
for t in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    has(ws,t)
cnt(ws,'embed-widget-single-quote.js',3)
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    has(ws,sym)
has(ws,'livebar-label')

# --- MMA countdown ---
has('mma-briefing.html','ufccdn')

# --- champions: cell-anchored, four banned regressions absent ---
mm='mma-briefing.html'
for cell in ['<td><b>Carlos Ulberg</b></td>','<td><b>Sean Strickland</b></td>',
             '<td><b>Justin Gaethje</b></td>','<td><b>Alexander Volkanovski</b></td>']:
    has(mm,cell,'champions cell missing: '+cell)
for bad in ['<td><b>Alex Pereira</b></td>','<td><b>Khamzat Chimaev</b></td>',
            '<td><b>Ilia Topuria</b></td>','<td><b>Valentina Shevchenko</b></td>']:
    hasnt(mm,bad,'BANNED champion regression present: '+bad)

# --- this run's new literal strings ---
cy='cyber-briefing.html'
for t in ['CVE-2026-51693','TOTOLINK T6','no vulnerability class, no affected build and no fixed version',
          'cvebrief.com/archive/2026/09/07/','this 6:05&nbsp;PM edition']:
    has(cy,t)
for t in ['about five hours in the past','The reopen has happened.','closed five-hour interval',
          '1:00&nbsp;PM to 6:00 PM ET, five hours','this 6:05&nbsp;PM edition',
          'is-the-stock-market-open-on-labor-day']:
    has(ws,t)
for t in ['forced to vacate the title due to injury','up to a year','three returns deep',
          'Alex Pereira</b> at light heavyweight','Khamzat Chimaev</b> at middleweight',
          'vacant-title-fight-headlines-ufc','this 6:05&nbsp;PM edition','<b>fourth</b> consecutive sweep']:
    has(mm,t)
for t in ['CVE-2026-51693','TOTOLINK T6','6:05&nbsp;PM','has now happened','closed five-hour interval',
          'forced to vacate the title due to injury','Ulberg','Strickland']:
    has('index.html',t)

# --- stale clock bans (previous edition's figures) ---
for f in [ws,'index.html']:
    hasnt(f,'four and a half hours','STALE clock figure')
hasnt(ws,'roughly <b>twenty minutes</b> from','STALE countdown')
hasnt(ws,'reopen is roughly <b>twenty minutes</b> away','STALE countdown 2')

# --- demotion bans: no page may claim the prior run is this run ---
for f in P:
    hasnt(f,'this 5:38')
    hasnt(f,'this run')

# --- New-tag ledger: cyber 1, ws 0, mma 0, index 0 ---
cnt(cy,'class="t new"',1)
cnt(ws,'class="t new"',0)
cnt(mm,'class="t new"',0)
cnt('index.html','class="t new"',0)

# --- Brent refusal counter still present ---
chk(D[ws].count('$97.93')>=1,'Brent $97.93 touch missing')
chk(D[ws].count('97.39')>=1,'Brent 97.39 print missing')

# --- PaperCut deadline consistency: 14 September, 7 days ---
for t in ['14 September','7 days out','PaperCut']:
    has(cy,t)
hasnt(cy,'6 days out')
hasnt(cy,'8 days out')

# --- grammar defect bans ---
for f in P:
    for bad in [' in in ',' the the ',' item the ',' and and ',' is is ']:
        hasnt(f,bad,'grammar defect %r in %s'%(bad,f))

# --- disclaimers ---
chk('investment advice' in D[ws],'WS disclaimer missing')
chk('subject to change' in D[mm],'MMA disclaimer missing')

# --- markets-closed facts ---
for t in ['Labor Day','9:30&nbsp;AM ET Tuesday']:
    has(ws,t)


# --- ADDED: ledger + counters (6:05 run) ---
for f in [cy,ws,mm]:
    has(f,'<b>1</b> cyber + <b>0</b> markets + <b>0</b> MMA = <b>1</b>')
    has(f,'archive/cyber-2026-09-07-1744.html')
    hasnt(f,'2 cyber + 1 markets')
    hasnt(f,'a run that finds something after three that did not is.')
has(cy,'1 tag on this page in this 6:05&nbsp;PM ET edition')
hasnt(ws,'sixth consecutive edition in which a futures-halt')
has(ws,'eighth consecutive edition in which a futures-halt')
for f in [ws,'index.html']:
    hasnt(f,'thirty-second consecutive edition')
cnt(ws,'thirty-third consecutive edition',2)
cnt('index.html','thirty-third consecutive edition',1)
has(mm,'<b>fourth consecutive edition</b>')
has(mm,'twenty consecutive editions without a champions regression')
hasnt(mm,'nineteen consecutive editions without a champions regression')
for f in P:
    hasnt(f,'this <b>5:38')
    hasnt(f,'in this 5:38')
has(ws,'As this <b>6:05&nbsp;PM</b> edition publishes')

print('CHECKS: %d   FAILURES: %d'%(n,len(fails)))
for x in fails: print('  FAIL:',x)
sys.exit(1 if fails else 0)

