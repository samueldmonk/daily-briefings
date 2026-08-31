#!/usr/bin/env python3
"""Fact-check / structure guards for the 1:41 PM ET edition, Aug 31 2026."""
import io, re, sys
FAIL=[]; N=[0]
def ck(c,m):
    N[0]+=1
    if not c: FAIL.append(m)
P={p:io.open(p,encoding='utf-8').read() for p in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
IDX,CY,WS,MM=P['index.html'],P['cyber-briefing.html'],P['wallstreet-briefing.html'],P['mma-briefing.html']
def strip_footer(h):
    i=h.find('<footer'); return h[:i] if i>0 else h
def unlinked(h):
    return re.sub(r'<a\b[^>]*>.*?</a>',' ',strip_footer(h),flags=re.S)

# ---------------- 1. universal structure
for p,h in P.items():
    ck('id="edition"' in h, p+': edition pill')
    ck('id="datestamp"' in h, p+': datestamp pill')
    ck('id="updated"' in h, p+': updated pill')
    ck('>1:41 PM ET<' in h, p+': not restamped to 1:41 PM ET')
    ck('id="freshline"' in h, p+': freshline')
    ck('Data as of 1:41 PM ET' in h, p+': freshline not restamped')
    ck(h.count('<nav class="tabs">')==1, p+': exactly one nav')
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"'%t in h, '%s: nav missing %s'%(p,t))
    ck('>1:12 PM ET<' not in h, p+': stale 1:12 stamp survived')
    ck('Monday, August 31, 2026' in h, p+': datestamp text')
    ck('Midday Edition' in h, p+': edition text')
    ck('1:41 PM' in h, p+': run marker absent')
    # exactly one tldr / summary strip on briefings
    if p!='index.html':
        ck(h.count('<div class="tldr">')==1, p+': exactly one tldr')

# ---------------- 2. no bare clock stamps from runs that did not happen today
TODAY_RUNS={'11:33','11:50','12:24','12:51','1:12','1:31','1:41','1 PM','4 PM','8 PM','5 PM','7 PM','9 PM','2:00 PM'}
BAD_STAMPS=['10:20 AM','10:50 AM','11:05 AM','8:19','9:35','5:15 PM','5:48 PM','6:45 PM','5:38 PM','2:39 PM','12:05']
for p,h in P.items():
    u=unlinked(h)
    for s in BAD_STAMPS:
        for m in re.finditer(re.escape(s),u):
            w=u[max(0,m.start()-200):m.start()+90]
            after=u[m.end():m.end()+14]
            dated=any(after.lstrip().startswith(d) for d in
                      ('Saturday','Sunday','Monday','Friday','Thursday','ET'))
            ck(dated or ('Carried' in w) or ('earlier edition' in w) or ('Aug 30' in w)
               or ('Aug 29' in w) or ('Aug 31' in w) or ('August 30' in w)
               or ('August 29' in w) or ('Recorded' in w) or ('Refused' in w),
               '%s: bare clock stamp %r without a date or carried label'%(p,s))

# ---------------- 3. Wall Street: the refusal must stay a refusal
for lvl in ['53,885.10','7,711.76','26,402.42']:
    for m in re.finditer(re.escape(lvl), unlinked(WS)):
        w=unlinked(WS)[max(0,m.start()-1400):m.start()+900]
        ck(('Refused' in w) or ('refused' in w) or ('mis-shelved' in w) or ('verified close' in w)
           or ('Friday' in w) or ('Weekly Scorecard' in w),
           'WS: level %s appears outside a refusal or Friday-close context'%lvl)
ck('does not close until 4 PM ET' in WS, 'WS: clock-adjacency guard for the refusal')
ck('refused' in WS.lower(), 'WS: refusal language present')
ck('fifth and a sixth time' in WS or 'fifth and sixth time' in WS, 'WS: sixth refusal recorded')
# PayPal percentage must sit in a refusal window
for m in re.finditer(r'PayPal[^<]{0,80}12\.7', unlinked(WS)):
    w=unlinked(WS)[max(0,m.start()-1200):m.start()+600]
    ck(('Refused' in w) or ('refused' in w) or ('Friday' in w),
       'WS: PayPal -12.7% asserted outside a refusal/Friday window')
# no live index LEVEL published
ck('no index level is published for the live session' in WS
   or 'no index level published' in WS.lower(), 'WS: live-level abstention stated')
# 1:31 snapshot present and time-anchored
ck('1:31 PM EDT' in WS, 'WS: 1:31 PM EDT snapshot missing')
for m in re.finditer(r'1:31 PM EDT', WS):
    w=WS[max(0,m.start()-500):m.start()+500]
    ck('0.5%' in w and '0.4%' in w and '0.3%' in w, 'WS: 1:31 snapshot figures incomplete')
# yields: live figures must name their baselines
ck('4.76%' in WS and '4.35%' in WS, 'WS: live yields missing')
for m in re.finditer(r'4\.76%', WS):
    w=WS[max(0,m.start()-300):m.start()+400]
    ck('4.73%' in w, 'WS: 4.76% published without its 4.73% Friday baseline')
for m in re.finditer(r'4\.35%', WS):
    w=WS[max(0,m.start()-300):m.start()+400]
    ck('4.34%' in w, 'WS: 4.35% published without its 4.34% Friday baseline')
# the seven-times-refused undated 4.72% must not be promoted
for m in re.finditer(r'4\.72%', unlinked(WS)):
    w=unlinked(WS)[max(0,m.start()-800):m.start()+500]
    wl=w.lower()
    ck('undated' in wl or 'refus' in wl or 'not promoted' in wl or 'recorded' in wl
       or 'not adopted' in wl or 'loses to the one already' in wl,
       'WS: undated 4.72% appears outside its refusal window')
# EIX/PCG two-reading handling
ck('21.0%' in WS and '22.3%' in WS, 'WS: both EIX readings present')
ck('20.0%' in WS and '16.7%' in WS, 'WS: both PCG readings present')
for m in re.finditer(r'21\.0%', WS):
    w=WS[max(0,m.start()-1600):m.start()+2600]
    ck('open session' in w or 'moment' in w or 'quoted this run' in w,
       'WS: EIX 21.0% without the open-session qualifier')
ck('Chart of the Day &mdash; Edison International (NYSE:EIX)' in WS, 'WS: Chart of the Day heading')
ck('NYSE:EIX' in WS, 'WS: Chart widget symbol')
# oil
ck('$92' in WS and 'near $86' in WS, 'WS: crude figures')
for m in re.finditer(r'\$80', unlinked(WS)):
    w=unlinked(WS)[max(0,m.start()-900):m.start()+700]
    ck('refus' in w or 'not printed' in w or 'cannot be reconciled' in w,
       'WS: $80 crude outside its refusal window')
# live widgets
for blk in ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
            'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']:
    ck(blk in WS, 'WS: missing live widget '+blk)
for sym in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    ck(sym in WS, 'WS: ticker tape missing '+sym)
ck('not investment advice' in WS or 'not investment' in WS, 'WS: disclaimer')
ck('Weekly Scorecard' in WS, 'WS: scorecard section')
ck('53,559.99' in WS, "WS: Friday's verified Dow close retained")

# ---------------- 4. Cyber
ck('Fire Ant' in CY, 'CY: Fire Ant spotlight missing')
ck('Cisco IOS XR' in CY and 'TACACS' in CY, 'CY: Fire Ant targets')
ck('ValleyRAT' in CY and 'Silver Fox' in CY and 'QN Wallpaper' in CY, 'CY: Silver Fox item')
ck('Kaspersky' in CY, 'CY: Silver Fox attribution')
ck('CloudSEK' in CY and 'Gambit Security' in CY, 'CY: Aurora attribution')
# the SpaceX descriptor may appear ONLY inside the refusal
for m in re.finditer(r'SpaceX', CY):
    w=CY[max(0,m.start()-400):m.start()+900]
    ck('refused' in w or 'Refused' in w or 'is not' in w,
       'CY: SpaceX descriptor outside its refusal window')
ck('the vendor is not' in CY, 'CY: vendor-attribution abstention stated')
# KEV
ck('twenty-fifth check' in CY, 'CY: KEV check count')
ck('eighteenth consecutive run' in CY, 'CY: KEV consecutive-run count')
ck('nothing on CISA&rsquo;s catalog is dated later' in CY, 'CY: KEV recency framing')
for cve in ['CVE-2015-3246','CVE-2015-5287','CVE-2019-1068','CVE-2021-23758','CVE-2022-0995','CVE-2026-8452']:
    ck(cve in CY, 'CY: KEV identifier missing '+cve)
ck('September 9' in CY and 'September 10' in CY, 'CY: KEV countdown targets')
ck('CVE-2026-66384' in CY, 'CY: JFrog identifier')
ck('BOD 22-01' in CY, 'CY: BOD reference')
ck('an omission from one search is not a retraction' in CY, 'CY: Aug 27 omission handled')
# GiveWP must stay disclosed-not-exploited
for m in re.finditer(r'CVE-2026-82222', CY):
    w=CY[max(0,m.start()-600):m.start()+2000]
    ck('4.16.7.2' in w or 'not' in w, 'CY: GiveWP context')
ck('4.16.7.2' in CY, 'CY: GiveWP fixed version')
ck('Patch Priority' in CY, 'CY: patch priority section')
ck('Threat Actor Spotlight' in CY, 'CY: spotlight section')
ck('Vulnerability Watch' in CY, 'CY: vuln section')
# Nevada 2025 must never appear as a 2026 incident
for m in re.finditer(r'Nevada', unlinked(CY)):
    w=unlinked(CY)[max(0,m.start()-500):m.start()+500]
    wl=w.lower()
    ck('2025' in w or 'refus' in wl or 'rejected' in wl or 'resolved' in wl,
       'CY: Nevada mentioned without its 2025 date or a refusal context')

# ---------------- 5. MMA champions board (CORRECTIONS.md authority)
board=MM[MM.find('Champions Board</h2>'):]
tbl=board[board.find('<table'):board.find('</table>')]
CH={'Heavyweight':'Aspinall','Light Heavyweight':'Ulberg','Middleweight':'Strickland',
    'Welterweight':'Makhachev','Lightweight':'Gaethje','Featherweight':'Volkanovski',
    'Bantamweight':'Yan','Flyweight':'Van'}
for div,name in CH.items():
    ck(name in tbl, 'MM: champions table missing '+name)
for bad in ['Pereira','Chimaev','Topuria','Pantoja']:
    for m in re.finditer(bad, tbl):
        w=tbl[max(0,m.start()-300):m.start()+300]
        ck('over' in w or 'beat' in w or 'KO' in w or 'TKO' in w or 'decision' in w or 'interim' in w.lower(),
           'MM: %s appears in a champions cell without a defeated-opponent context'%bad)
ck('Ciryl Gane' in MM or 'Gane' in MM, 'MM: interim heavyweight')
ck('Harrison' in tbl and 'Shevchenko' in tbl and 'Dern' in tbl, 'MM: women champions rows')
ck('nineteenth cross-check' in MM.lower() or 'Nineteenth cross-check' in MM, 'MM: cross-check count')
ck('an omission from a later search is not evidence against a row' in MM, 'MM: omission rule stated')
ck('seventy-sixth consecutive edition' in MM, 'MM: board-unchanged count')
# Dariush rule
for m in re.finditer(r'Dariush', unlinked(MM)):
    w=unlinked(MM)[max(0,m.start()-400):m.start()+400]
    if 'champion' in w or 'challenger' in w:
        wl=w.lower()
        ck('contender' in wl or 'never' in w or 'miscalled' in wl or 'standing rule' in wl
           or 'the descriptor is omitted' in wl,
           'MM: Dariush described as champion/challenger')
# unqualified "title challenger" is forbidden
for m in re.finditer(r'title challenger', unlinked(MM)):
    w=unlinked(MM)[max(0,m.start()-260):m.start()]
    wa=unlinked(MM)[m.start():m.start()+400].lower()
    ck(('former' in w.lower()) or ('refus' in w.lower()) or ('ex-UFC' in w)
       or ('is not described here' in w.lower()) or ('descriptor is omitted' in wa),
       'MM: unqualified "title challenger" descriptor')
# Salkilld regression guard
for m in re.finditer(r'Salkilld', MM):
    w=MM[max(0,m.start()-300):m.start()+300]
    ck('Quillan' in w, 'MM: Salkilld rendered without the correct first name')
ck('Cody Salkilld' not in MM, 'MM: wrong Salkilld first name')
# new content
ck('TUF 34 Bantamweight Finale' in MM, 'MM: Sept 26 event name')
ck('Meta APEX' in MM, 'MM: Sept 26 venue')
for n in ['Mehemmedeli Osmanli','Ilimbek Akylbek Uulu','Rodolfo Vieira','Robert Bryczek',
          'Brady Hiestand','Rinya Nakamura','Jonny Parsons']:
    ck(n in MM, 'MM: booking name missing '+n)
ck('corroborating source, not a reconciliation' in MM, 'MM: Sept 26 name-reconciliation caveat')
# Paris odds must stay inside the carried band
ck('&minus;428' in MM and '+300' in MM, 'MM: new Paris odds renderings')
for m in re.finditer(r'&minus;428', MM):
    w=MM[max(0,m.start()-1400):m.start()+1400]
    ck('range is unchanged' in w or 'inside the carried range' in w
       or 'already carries both pairs' in w or 'printed as a range' in w
       or 'No line is adopted' in w or 'no line is adopted' in w or 'none of the' in w
       or 'not carried' in w or 'no single figure is adopted' in w,
       'MM: -428 published without the carried-range framing')
ck('subject to change' in MM, 'MM: disclaimer')
ck('ufccdn' in MM, 'MM: countdown element')
ck('2026-09-05' in MM, 'MM: countdown target date')
# nothing "upcoming" that already happened
for past in ['August 29','August 15']:
    for m in re.finditer(past, MM[:MM.find('Prospect Watch')]):
        w=MM[max(0,m.start()-300):m.start()+200]
        ck('Result' in w or 'result' in w or 'Carried' in w or 'week ending' in w or 'tracker' in w,
           'MM: past date %s inside the upcoming-cards region'%past)

# ---------------- 6. index mirrors the pages
ck('Fire Ant' in IDX and 'Silver Fox' in IDX, 'IDX: cyber card not mirrored')
ck('1:31 PM EDT' in IDX, 'IDX: markets card not mirrored')
ck('TUF 34 Bantamweight Finale' in IDX, 'IDX: MMA card not mirrored')
ck('twenty-fifth check' in IDX, 'IDX: KEV count stale')
ck('nineteenth champions cross-check' in IDX, 'IDX: champions count stale')
ck('seventy-sixth consecutive edition' in IDX, 'IDX: board count stale')
ck('embed-widget' not in IDX, 'IDX: must carry no live widgets')
for lvl in ['53,885.10','7,711.76','26,402.42']:
    ck(lvl not in unlinked(IDX), 'IDX: refused level %s leaked onto the front page'%lvl)
ck('eighteenth consecutive' in CY, 'CY: run count')

# ---------------- 7. sources footers refreshed
for p,h in P.items():
    ck('1:41 PM' in h[h.find('<footer'):], p+': sources footer not restamped')
    ck(h[h.find('<footer'):].count('<a href="http')>=5, p+': too few source links')


# ---------------- 8. guards added this run
ck('already carries both pairs' in MM, 'MM: odds re-confirmation framing missing')
ck('&minus;357' in MM and '&minus;550' in MM, 'MM: full carried odds set')
ck('quoted in reporting this run' not in MM, 'MM: stale "this run" on the carried odds block')
ck('(three books at the time)' in MM, 'MM: odds range not re-qualified')
ck('quoted in reporting this run has Parnasse' not in MM, 'MM: stale "this run" on a carried odds block')
ck('Two more renderings for' not in MM, 'MM: withdrawn "two more renderings" wording survived')
for m in re.finditer(r'the \d{1,2}:\d{2} edition', unlinked(WS)+unlinked(CY)+unlinked(MM)):
    ck(False, 'bare "the H:MM edition" reference survived')
for m in re.finditer(r'\(1[012]:\d{2}\)', unlinked(MM)):
    ck(False, 'bare parenthetical run stamp survived on MM')
ck('nothing lands outside the band' not in MM, 'MM: superseded odds claim survived')
ck('an earlier edition edition' not in CY+WS+MM, 'scrub artefact "an earlier edition edition"')
ck('at an earlier edition' not in re.sub('<[^>]+>','',CY+WS+MM), 'scrub artefact "at an earlier edition"')
ck('a return is not clean or dirty as a whole' in WS, 'WS: sixth-refusal lesson stated')
ck('nearly 65%' in WS, 'WS: breadth figure')
ck('Brent crude just over $92' in WS, 'WS: Brent level')
ck('QN Wallpaper' in CY, 'CY: Silver Fox lure named')
ck('an omission is not evidence against a row' in IDX, 'IDX: MMA omission rule mirrored')

print('%d checks, %d failures'%(N[0],len(FAIL)))
for f in FAIL: print('  FAIL:',f)
sys.exit(1 if FAIL else 0)
