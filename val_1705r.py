# -*- coding: utf-8 -*-
import re, sys
FILES=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
H={f:open(f,encoding='utf-8').read() for f in FILES}
fails=[]; n=0
def ck(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)

# --- structural: tag balance ---
for f in FILES:
    h=H[f]
    for tag in ['div','p','table','tr','td','h2','span']:
        o=len(re.findall(r'<%s[ >]'%tag,h)); c=len(re.findall(r'</%s>'%tag,h))
        ck(o==c, "%s: <%s> balance %d open / %d close"%(f,tag,o,c))

# --- five-tab nav on every page ---
for f in FILES:
    for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%href in H[f], "%s: nav missing %s"%(f,href))

# --- masthead pills + stamp JS ---
for f in FILES:
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        ck(i in H[f], "%s: missing %s"%(f,i))
    ck("America/New_York" in H[f], "%s: stamp JS missing"%f)
for f in FILES[1:]:
    ck('id="freshline"' in H[f], "%s: freshline missing"%f)
    ck('class="tldr"' in H[f], "%s: tldr missing"%f)

# --- tldr labels ---
ck('<b>The Wire</b>' in H['cyber-briefing.html'],"cyber tldr label")
ck('<b>The Tape</b>' in H['wallstreet-briefing.html'],"ws tldr label")
ck('<b>Tale of the Tape</b>' in H['mma-briefing.html'],"mma tldr label")

# --- TradingView blocks on wall street ---
ws=H['wallstreet-briefing.html']
for w in ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']:
    ck('embed-widget-%s.js'%w in ws, "ws: widget %s missing"%w)
ck(ws.count('embed-widget-single-quote.js')==3, "ws: need 3 single-quote widgets, have %d"%ws.count('embed-widget-single-quote.js'))
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(s in ws, "ws: ticker symbol %s missing"%s)
ck('class="livebar"' in ws,"ws: livebar missing")

# --- MMA countdown ---
ck('ufccdn' in H['mma-briefing.html'],"mma: countdown element missing")

# --- CHAMPIONS BOARD (cell-anchored) + banned regressions ---
mma=H['mma-briefing.html']
for champ in ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
              'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']:
    ck(champ in mma, "mma: champion name missing: %s"%champ)
for bad in ['<td><b>Alex Pereira</b></td>','<td><b>Khamzat Chimaev</b></td>','<td><b>Ilia Topuria</b></td>']:
    ck(bad not in mma, "mma: BANNED champion cell present: %s"%bad)
ck('Women&rsquo;s Flyweight</td><td><b>Vacant</b>' in mma or 'Vacant</b>' in mma, "mma: W-FLY vacant row missing")

# --- this edition's NEW content, literal strings ---
cy=H['cyber-briefing.html']
for s in ['12.4.3-03453','12.5.0-02835','SNWLID-2026-0016','unintended alternate access path']:
    ck(s in cy, "cyber: new string missing: %s"%s)
ck('12.4.3-03526' in cy and '12.5.0-02952' in cy, "cyber: fixed hotfix builds lost")
# refusal present
ck('Adobe Commerce and Magento</b> form submission' in cy or 'Adobe Commerce and Magento</b>' in cy, "cyber: conflation refusal missing")
ck('which has <b>no CVE at all</b>' in cy, "cyber: StyleSmuggler no-CVE clause missing")
# Elementor product must never be stated as Magento affirmatively
ck('CVE-2026-32475</td><td class="down"><b>9.8</b></td><td>Elementor Pro' in cy, "cyber: CVE table row product changed")

# --- new-tag ledger: exactly 1 New tag site-wide, and it is on cyber ---
tot=sum(H[f].count('class="t new"') for f in FILES)
ck(tot==1, "ledger: expected 1 New tag site-wide, found %d"%tot)
ck(H['cyber-briefing.html'].count('class="t new"')==1, "ledger: the New tag is not on cyber")
for f in ['wallstreet-briefing.html','mma-briefing.html','index.html']:
    ck(H[f].count('class="t new"')==0, "ledger: stray New tag on %s"%f)
for f in FILES[1:]:
    ck('5:05&nbsp;PM ET edition' in H[f], "%s: ledger/sources not stamped 5:05"%f)

# --- clock recomputation: stale halt figures banned ---
ck('about two and a half hours in the past' not in ws, "ws: STALE halt elapsed figure (two and a half hours)")
ck('about an hour and a quarter in the past' not in ws, "ws: STALE halt elapsed figure (hour and a quarter)")
ck('about four hours in the past' in ws, "ws: current halt elapsed figure missing")
ck('<b>3:35&nbsp;PM</b> edition publishes' not in ws, "ws: stale edition self-reference in halt sentence")
ck('<b>5:05&nbsp;PM</b> edition publishes' in ws, "ws: current edition self-reference missing")
ck('5:00 p.m. CT is 6:00 PM ET' in ws, "ws: reopen conversion missing")

# --- Brent refusal counter advanced and consistent ---
ck('thirtieth consecutive edition' not in ws, "ws: stale Brent refusal counter (thirtieth)")
ck(ws.count('thirty-first consecutive edition')==2, "ws: Brent refusal counter not 2x thirty-first (%d)"%ws.count('thirty-first consecutive edition'))
ck('thirtieth consecutive edition' not in H['index.html'], "index: stale Brent counter")
ck('thirty-first consecutive edition' in H['index.html'], "index: Brent counter not synced")
ck('97.93' in ws, "ws: $97.93 touch lost")

# --- demote pass: no un-demoted inherited claims, no grammar breakage ---
for f in FILES:
    for bad in ['item the 5:05','item the 4:35','in in ','the the ','edition edition']:
        ck(bad not in H[f], "%s: grammar defect %r"%(f,bad))

# --- MMA / WS zero-new assertions present ---
ck('second consecutive sweep returned nothing new' in H['index.html'] or 'A second consecutive sweep returned nothing new' in H['index.html'], "index: mma zero-new line missing")
ck('nothing on this page is tagged New' in ws, "ws: zero-new assertion missing")

# --- disclaimers (anchored on the pages' actual wording) ---
ck('investment advice' in ws, "ws: disclaimer missing")
ck('subject to change' in mma, "mma: disclaimer missing")

# --- sources footers exist on all three briefings ---
for f in FILES[1:]:
    ck('<h2 class="sec">Sources</h2>' in H[f], "%s: sources footer missing"%f)
    ck('http' in H[f], "%s: no source URLs"%f)

# --- KEV deadline consistency: 14 September must agree everywhere it appears ---
ck('14 September' in cy, "cyber: PaperCut deadline missing")
ck('7 days out' in cy or 'seven days out' in cy, "cyber: PaperCut countdown missing")
ck('seven days out' in H['index.html'] or '7 days out' in H['index.html'], "index: PaperCut countdown missing")

print("checks run: %d"%n)
if fails:
    print("FAILURES (%d):"%len(fails))
    for x in fails: print("  -",x)
    sys.exit(1)
print("ALL PASS")
