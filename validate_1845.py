#!/usr/bin/env python3
# Publish gate for the 2026-08-30 6:45 PM edition.
import re, sys, io, datetime, zoneinfo
REPO = sys.argv[1]
def rd(f): return io.open(REPO+'/'+f, encoding='utf-8').read()
P = {f: rd(f) for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']}
CY, WS, MM, IX, AR = P['cyber-briefing.html'], P['wallstreet-briefing.html'], P['mma-briefing.html'], P['index.html'], P['archive.html']
BRIEFS = {'cyber-briefing.html':CY, 'wallstreet-briefing.html':WS, 'mma-briefing.html':MM}
ALL4 = dict(BRIEFS); ALL4['index.html'] = IX

fails, n = [], 0
def ck(cond, msg):
    global n
    n += 1
    if not cond: fails.append(msg)

def txt(h):
    t = re.sub(r'<script.*?</script>','',h,flags=re.S); t = re.sub(r'<style.*?</style>','',t,flags=re.S)
    return re.sub(r'<[^>]+>',' ',t)

# ---------- 1. chrome: nav, stamps, self-stamp JS
now = datetime.datetime.now(zoneinfo.ZoneInfo('America/New_York'))
date_s = now.strftime('%A, %B %-d, %Y')
for f,h in ALL4.items():
    for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck(('href="%s"' % href) in h, '%s: nav missing %s' % (f, href))
    ck(len(re.findall(r'<nav class="tabs">.*?</nav>', h, re.S)) == 1, f+': not exactly one nav')
    nav = re.search(r'<nav class="tabs">.*?</nav>', h, re.S).group(0)
    ck(nav.count('class="on"') == 1, f+': active tab count != 1')
    for i in ['datestamp','updated','edition','freshline']:
        ck(('id="%s"' % i) in h, '%s: missing id %s' % (f,i))
    ck("America/New_York" in h and "getElementById('datestamp')" in h, f+': self-stamp JS missing')
    ck(date_s in h, f+': masthead date not restamped to '+date_s)
    ck('Data as of' in h and 'refresh every 30 minutes' in h, f+': freshline text')
for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
    ck(('href="%s"' % href) in AR, 'archive.html: nav missing '+href)

# ---------- 2. tldr strips + index mirror
for f,label,acc in [('cyber-briefing.html','The Wire','#22d3a8'),
                    ('wallstreet-briefing.html','The Tape','#caa64a'),
                    ('mma-briefing.html','Tale of the Tape','#e84545')]:
    m = re.search(r'<div class="tldr"><b>%s</b> <span>(.*?)</span></div>' % re.escape(label), BRIEFS[f], re.S)
    ck(m is not None, f+': tldr strip missing/mislabelled')
    if m:
        ck(len(txt(m.group(1))) > 300, f+': tldr too short')
        card = re.search(r'<div class="bigcard c-%s">.*?<p>(.*?)</p>' %
                         {'cyber-briefing.html':'cy','wallstreet-briefing.html':'ws','mma-briefing.html':'mm'}[f], IX, re.S)
        ck(card is not None and card.group(1) == m.group(1), f+': index card does not mirror tldr byte-for-byte')
ck('<div class="tldr">' not in IX, 'index.html must not carry a tldr strip')

# ---------- 3. TradingView widgets: WS only
W = ['ticker-tape','single-quote','timeline','stock-heatmap','mini-symbol-overview','events']
for w in W: ck(('embed-widget-%s.js' % w) in WS, 'WS: missing widget '+w)
ck(WS.count('embed-widget-single-quote.js') == 3, 'WS: single-quote widget count != 3')
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(s in WS, 'WS: tape missing '+s)
for f in ['cyber-briefing.html','mma-briefing.html','index.html']:
    ck('s3.tradingview.com' not in ALL4[f], f+': must carry no live widgets')
ck('s3.tradingview.com' not in AR, 'archive.html: must carry no live widgets')

# ---------- 4. markets arithmetic (closes must reconcile with weekly changes)
for lvl, chg in [('7,711.76','37.39'), ('53,559.99','282.98'), ('26,402.42','221.97')]:
    ck(lvl in WS and chg in WS, 'WS: missing close/weekly pair %s / %s' % (lvl,chg))
ck(abs((7711.76-37.39) - 7674.37) < 2e-3, 'S&P weekly arithmetic')
ck(abs((53559.99-282.98) - 53277.01) < 2e-3, 'Dow weekly arithmetic')
ck(abs((26402.42-221.97) - 26180.45) < 2e-3, 'Nasdaq weekly arithmetic')
ck('26,180.45' in WS, 'WS: corroborated Aug 21 Composite level absent')
# +0.9% may appear only where the +0.8% it competes with is present as the adopted form.
# (Guard narrowed 6:45 PM: it originally accepted loose phrases; it now requires the rival
#  figure in the same window, which is what makes the non-adoption legible to a reader.)
for m in re.finditer(r'\+0\.9%', WS):
    seg = txt(WS[max(0,m.start()-900):m.end()+900])
    ck('+0.8%' in seg or '0.8478' in seg or '0.8407' in seg,
       'WS: +0.9% Nasdaq weekly appears without the adopted +0.8% beside it')
ck('0.8478' in WS and '0.8407' in WS, 'WS: the two Nasdaq weekly percentage identities must both be shown')
# 4.72% must appear only in a refusal / non-adoption context.
# (Guard narrowed 6:45 PM: matching was case-sensitive and missed the "Refused" section tag,
#  and the phrase list lacked "recorded and not adopted", which is this page's standard wording.)
for m in re.finditer(r'4\.72%', WS):
    seg = txt(WS[max(0,m.start()-900):m.end()+900]).lower()
    ck(any(q in seg for q in ['refused','not adopted','undated','does not displace','not promoted','loses to']),
       'WS: 4.72% appears without a refusal/non-adoption context')
ck('4.73%' in WS, 'WS: verified 10-year close 4.73% absent')
# Dow futures must not be promoted into the scorecard table
sc = re.search(r'<h2 class="sec">Weekly Scorecard.*?</table>', WS, re.S)
ck(sc is not None and '53,584' not in sc.group(0) and '53,608' not in sc.group(0),
   'WS: Dow futures level leaked into the Weekly Scorecard')
for fut in ['53,584.00','53,608.00']:
    m = re.search(re.escape(fut), WS); ck(m is not None, 'WS: futures figure '+fut+' missing')
    if m:
        seg = txt(WS[max(0,m.start()-800):m.end()+800])
        ck('futures are not the cash index' in seg or 'not promoted' in seg,
           'WS: futures figure '+fut+' without a not-the-cash-index qualifier')
# no recomputed oil level: Friday levels stay, no new WTI/Brent quote invented
ck('$83.44' in WS and '$88.29' in WS, 'WS: Friday oil levels missing')
ck('$85' not in WS and '$90.0' not in WS, 'WS: a recomputed oil level appears to have been printed')
# calendar dates
for s in ['September 2','5:00 PM ET','September 4','8:30 AM ET','September 7','September 16']:
    ck(s in WS, 'WS: calendar item missing '+s)
ck('September 3' in WS, 'WS: the conflicting Broadcom date must be recorded, not dropped')
# undated 65%-hold must be refused
m = re.search(r'65% chance', WS)
ck(m is not None, 'WS: the 65% hold reading must be recorded')
if m:
    seg = txt(WS[max(0,m.start()-600):m.end()+900])
    ck('refused' in seg and 'undated' in seg, 'WS: 65% hold reading lacks its refusal')

# ---------- 5. cyber: Questel correction, KEV, CVEs
ck('Questal' not in CY.replace('&ldquo;Questal&rdquo;',''), 'CY: stray "Questal" outside the correction note')
ck('Questel SAS' in CY, 'CY: corrected company name absent')
ck('&ldquo;Questal&rdquo;' in CY, 'CY: the correction must name the old spelling')
for s in ['August 2','August 4','Microsoft 365','voice-phishing','Sales SharePoint','134 GB','21 million','147 GB']:
    ck(s in CY, 'CY: Questel detail missing '+s)
m = re.search(r'Salesforce records', CY)
ck(m is not None, 'CY: Salesforce claim missing')
# the confirmation must be paired with a not-in-full qualifier
ck('has not confirmed the\nattacker' in CY or 'not confirmed the attacker' in CY.replace('\n',' '),
   'CY: Questel confirmation printed without the "not in full" qualifier')
# Nevada must stay refused
ck('Nevada' in CY, 'CY: Nevada refusal ledger missing')
nv = txt(CY)[txt(CY).find('Nevada')-200: txt(CY).find('Nevada')+400]
ck('refus' in nv.lower(), 'CY: Nevada mentioned without a refusal')
# KEV deadlines agree between Patch Priority and the KEV board
for s in ['CVE-2023-49105','CVE-2026-53362']:
    ck(CY.count(s) >= 2, 'CY: due-today CVE '+s+' not on both boards')
ck('August 30' in CY, 'CY: today\'s deadline date absent')
ck('0 days left' in CY or '0 days' in CY, 'CY: due-today countdown absent')
ck('overdue' in CY.lower(), 'CY: overdue rows absent')
ck('CVE-2026-8452' in CY and 'CVE-2019-1068' in CY, 'CY: overdue pair absent')
# no same-week/invented deadline: every KEV date stated must be one CISA gave
for bad in ['August 31','September 1 deadline']:
    ck(bad not in CY, 'CY: unsourced KEV deadline '+bad)
# new CVE rows well-formed and non-exploited flagged
for cve in ['CVE-2026-62893','CVE-2026-62818']:
    ck(cve in CY, 'CY: missing '+cve)
m = re.search(r'CVE-2026-62893', CY)
seg = txt(CY[m.start():m.start()+1400])
ck('Not exploited' in seg and 'not KEV-listed' in seg, 'CY: 62893 lacks the not-exploited qualifier')
# CVE well-formedness + liveness
ids = set(re.findall(r'CVE-\d{4}-\d{4,7}', CY))
ck(len(ids) >= 15, 'CY: too few distinct CVEs (%d)' % len(ids))
for i in ids: ck(re.fullmatch(r'CVE-(19|20)\d{2}-\d{4,7}', i) is not None, 'CY: malformed '+i)
# standing CVSS corrections
if 'CVE-2026-3055' in CY: ck('9.3' in CY, 'CY: Citrix CVE-2026-3055 must carry 9.3')
if 'CVE-2026-8037' in CY: ck('9.6' in CY, 'CY: Kemp CVE-2026-8037 must carry 9.6')
# CVE-2026-19490 kept off the deadline board
kev = re.search(r'<h2 class="sec">CISA KEV.*?(?=<footer|</body)', CY, re.S)
ck(kev is not None, 'CY: KEV section not found')
if kev and 'CVE-2026-19490' in kev.group(0):
    for m2 in re.finditer('CVE-2026-19490', kev.group(0)):
        seg = txt(kev.group(0)[max(0,m2.start()-700):m2.end()+700])
        ck(any(q in seg for q in ['not in KEV','not exploited','kept off','no countdown','not given a countdown']),
           'CY: 19490 on the KEV board without a negation')
# ServiceNow fourth identifier still unadopted
ck('CVE-2026-6876' in CY or 'CVE-2026-6875' in CY, 'CY: ServiceNow fourth identifier not discussed')
sn = txt(CY); i = sn.find('four records')
ck(i > 0 and ('not settle' in sn[i:i+600] or 'stays out' in sn[i-900:i+600]),
   'CY: four-record count used to adopt an identifier')
for c in ['CVE-2026-18885','CVE-2026-18886','CVE-2026-74820']: ck(c in CY, 'CY: missing ServiceNow '+c)
# threat level banner
ck(re.search(r'Threat Level', CY) is not None, 'CY: threat-level banner missing')

# ---------- 6. MMA: champions board, Paris, bonuses
CHAMPS = ['Tom Aspinall','Carlos Ulberg','Sean Strickland','Islam Makhachev','Justin Gaethje',
          'Alexander Volkanovski','Petr Yan','Joshua Van','Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']
# Guard narrowed 6:45 PM: the anchor was the bare string "Champions Board", which matches the
# two in-body cross-references that precede the section, so the sweep was reading the RESULTS
# table. Anchored to the section heading's closing tag instead.
cb = re.search(r'Champions Board</h2>.*?</table>', MM, re.S)
ck(cb is not None, 'MM: champions board table not found')
if cb:
    board = cb.group(0)
    for c in CHAMPS: ck(c in board, 'MM: champion missing from board: '+c)
    # forbidden champion cells -- must not appear in the champion column
    for row in re.findall(r'<tr>(.*?)</tr>', board, re.S):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.S)
        if len(cells) >= 2:
            champ = txt(cells[1])
            for bad in ['Alex Pereira','Khamzat Chimaev','Merab Dvalishvili','Alexandre Pantoja','Ilia Topuria','Zhang Weili']:
                ck(bad not in champ, 'MM: FORBIDDEN champion cell "%s"' % bad)
            ck('vacant' not in champ.lower() or 'Featherweight' not in txt(cells[0]),
               'MM: featherweight must not read vacant')
# stale-cell refutation must be present and explicit
for s in ['former champion','UFC 323','October 24','per cell, not per return','seventieth']:
    ck(s in MM, 'MM: cross-check narrative missing '+s)
for m2 in re.finditer('Merab Dvalishvili', MM):
    seg = txt(MM[max(0,m2.start()-1200):m2.end()+1200])
    ck(any(q in seg for q in ['superseded','stale','trilogy','defend','defence','contender','challenger','Yan']),
       'MM: Dvalishvili mentioned without a superseded/challenger context')
# Paris card
for s in ['Accor Arena','September 5','UFC Fight Night 287','Hooker vs. Parnasse','12 PM ET','3 PM ET',
          'Far&egrave;s Ziam','Axel Sola','Michael Page','Nursulton Ruziboev','Matthieu Duclos','Delphine Benouaich']:
    ck(s in MM, 'MM: Paris detail missing '+s)
for s in ['Hooker +300','&minus;400','Hooker +375','&minus;500']:
    ck(s in MM, 'MM: Paris odds missing '+s)
# bonuses arithmetic
ck('$400,000' in MM and '$125,000' in MM and '$525,000' in MM, 'MM: bonus arithmetic incomplete')
ck(400000 + 5*25000 == 525000, 'MM: bonus sum identity')
for nme in ['Hector Santiago','Francesco Nuzzi','Rei Tsuruya','Kai Asakura','Denise Gomes',
            'Song Yadong','Bilal Hasan','Liu Ce','Levi Rodrigues Jr.']:
    ck(nme in MM, 'MM: bonus name missing '+nme)
m = re.search(r'\$25,000', MM); seg = txt(MM[m.start()-900:m.start()+900]) if m else ''
ck('single\nsource' in MM or 'single source' in seg.replace('\n',' '), 'MM: $25,000 tier lacks single-source label')
# standing name traps
ck('Cody Salkilld' not in MM and 'Abdul-Rakhman' not in MM and 'Shamil Yakhyaev' not in MM, 'MM: forbidden name form')
if 'Dariush' in MM:
    for m2 in re.finditer('Dariush', MM):
        seg = txt(MM[max(0,m2.start()-350):m2.end()+350])
        ck('champion' not in seg.lower() or 'contender' in seg.lower(), 'MM: Dariush described as a champion/challenger')
# UFC 331
for s in ['Crypto.com Arena','9 PM ET','Renato Moicano','Brian Ortega','Marlon Vera','26 seconds']:
    ck(s in MM, 'MM: UFC 331 detail missing '+s)
# nothing "upcoming" that has already happened
for d in ['August 29','August 22']:
    for m2 in re.finditer(re.escape(d), MM):
        seg = txt(MM[max(0,m2.start()-300):m2.end()+300]).lower()
        ck('upcoming' not in seg, 'MM: past date '+d+' described as upcoming')
# countdown target
ck('ufccdn' in MM, 'MM: next-card countdown element missing')

# ---------- 7. footers, disclaimers, hrefs
for f,h in BRIEFS.items():
    s = re.search(r'<div class="srcs">(.*?)</div>', h, re.S)
    ck(s is not None, f+': no sources footer')
    if s:
        hrefs = re.findall(r'<a href="([^"]+)"', s.group(1))
        ck(len(hrefs) >= 6, f+': fewer than 6 footer links')
        ck(len(hrefs) == len(set(hrefs)), f+': duplicate footer hrefs')
        ck(all(u.startswith('https://') for u in hrefs), f+': non-https footer link')
    ck('class="disc"' in h, f+': disclaimer missing')
ck('not investment advice' in WS, 'WS: investment-advice disclaimer missing')
ck('subject to change' in MM, 'MM: cards-subject-to-change disclaimer missing')
# every tag class used is defined in the page CSS
for f,h in ALL4.items():
    css = ''.join(re.findall(r'<style>(.*?)</style>', h, re.S))
    for cls in set(re.findall(r'class="tag ([a-z]+)"', h)):
        ck(('.tag.'+cls) in css, '%s: tag class .%s not defined' % (f, cls))

# ---------- 8. cross-page consistency
ck('Questel' in IX and 'Questal' not in IX.replace('&ldquo;Questal&rdquo;',''), 'index: stale company spelling')
ck('per cell, not per return' in IX, 'index: cross-check finding not summarised')
ck('Strait of\nHormuz' in IX or 'Strait of Hormuz' in IX.replace('\n',' '), 'index: markets lead not summarised')

print('%d checks, %d failures' % (n, len(fails)))
for f_ in fails: print('  FAIL:', f_)
sys.exit(1 if fails else 0)
