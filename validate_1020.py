#!/usr/bin/env python3
"""Programmatic validation gate — Wed Aug 26 2026, ~10:20 a.m. ET edition."""
import io, re, json, sys, datetime
from html.parser import HTMLParser

PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
ALL = PAGES + ['archive.html']
S = {p: io.open(p, encoding='utf-8').read() for p in PAGES}

fails, checks = [], 0
def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

# ---- 1. balance ------------------------------------------------------------
VOID = {'br','img','hr','meta','link','input','source','col','area','base','embed','param','track','wbr'}
class B(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.st=[]; s.stray=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
            s.stray.append(t)
        else: s.stray.append(t)
for p in ALL:
    b=B(); b.feed(io.open(p, encoding='utf-8').read())
    ck(not b.st and not b.stray, "%s unbalanced: open=%s stray=%s" % (p,b.st[:6],b.stray[:6]))

# ---- 2. five-tab nav -------------------------------------------------------
ORDER=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']
for p in ALL:
    s=io.open(p, encoding='utf-8').read()
    m=re.search(r'<nav class="tabs">(.*?)</nav>', s, re.S)
    ck(m is not None, "%s: no <nav class=\"tabs\">" % p)
    if not m: continue
    nav=m.group(1)
    ck(re.findall(r'href="([^"]+)"', nav)==ORDER, "%s: nav hrefs wrong" % p)
    if p=='archive.html':
        # archive.html marks its own tab with an inline muted style, not class="on"
        ck(re.search(r'<a href="archive\.html" style="color:#8fa0b0', nav) is not None,
           "archive.html: Archive tab not highlighted")
        ck('class="on"' not in nav, "archive.html: unexpected class=on")
    else:
        on=re.findall(r'<a href="([^"]+)"[^>]*class="on"', nav)
        ck(on==[p], "%s: active tab is %s" % (p,on))

# ---- 3. masthead stamp ids + freshness ------------------------------------
for p in PAGES:
    for i in ('edition','datestamp','updated','freshline'):
        ck(S[p].count('id="%s"'%i)==1, "%s: id=%s not exactly once" % (p,i))
    ck('briefings refresh every 30 minutes, 8 AM' in S[p], "%s: freshness string missing" % p)

# ---- 4. tldr strips --------------------------------------------------------
LAB={'wallstreet-briefing.html':'The Tape','cyber-briefing.html':'The Wire','mma-briefing.html':'Tale of the Tape'}
for p,lab in LAB.items():
    ck(S[p].count('<div class="tldr">')==1, "%s: tldr count != 1" % p)
    ck('<b>%s</b>'%lab in S[p], "%s: tldr label %r missing" % (p,lab))
ck(S['index.html'].count('<div class="tldr">')==0, "index: must not carry a tldr")

# ---- 5. index cards mirror each page's tldr verbatim -----------------------
def tldr_body(p):
    m=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', S[p], re.S)
    return m.group(1) if m else None
for cls,page in (('c-sec','cyber-briefing.html'),('c-mkt','wallstreet-briefing.html'),('c-mma','mma-briefing.html')):
    m=re.search(r'<a class="bcard %s"[^>]*>(.*?)</a>'%cls, S['index.html'], re.S)
    ck(m is not None, "index: no bcard %s" % cls)
    if not m: continue
    card=m.group(1)
    body=tldr_body(page)
    ck(body is not None, "%s: tldr body unparsed" % page)
    ck(body and ('<p>%s</p>'%body) in card, "index %s: does not carry %s tldr verbatim" % (cls,page))
    h2=re.search(r'<h2>(.*?)</h2>', card, re.S)
    ck(h2 and h2.group(1).strip(), "index %s: empty h2" % cls)
    ck('Read the briefing' in card, "index %s: no CTA" % cls)

# ---- 6. TradingView blocks parse ------------------------------------------
blocks=re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>', S['wallstreet-briefing.html'], re.S)
ck(len(blocks)==8, "wallstreet: expected 8 TradingView blocks, found %d" % len(blocks))
for i,b in enumerate(blocks):
    try: json.loads(b)
    except Exception as e: fails.append("TradingView block %d does not parse: %s" % (i,e));
    checks += 1

# ---- 7. ticker tape keeps all five mandatory symbols, and drops DKS --------
tape=json.loads(re.search(r'embed-widget-ticker-tape\.js" async>(\{.*?\})</script>', S['wallstreet-briefing.html'], re.S).group(1))
syms=[x['proName'] for x in tape['symbols']]
for req in ('FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y'):
    ck(req in syms, "tape: missing mandatory symbol %s" % req)
ck(len(syms)==len(set(syms)), "tape: duplicate symbols %s" % syms)
ck('NYSE:DKS' not in syms, "tape: DKS is Tuesday's mover and must not ride the Wednesday tape")
ck('NASDAQ:META' in syms, "tape: META (today's lead) not featured")

# ---- 8. chart of the day is scoped to the mini-symbol-overview block -------
mini=json.loads(re.search(r'embed-widget-mini-symbol-overview\.js" async>(\{.*?\})</script>', S['wallstreet-briefing.html'], re.S).group(1))
ck(mini['symbol']=='NASDAQ:INTU', "chart of the day symbol is %s, expected NASDAQ:INTU" % mini['symbol'])
ck('session has not opened' not in S['wallstreet-briefing.html'], "wallstreet: stale 'session has not opened' text survives after the bell")

# ---- 9. KEV board: 14 rows, 10 past due, 0 due today, 4 ahead --------------
spans=re.findall(r'<span class="kevdue([^"]*)">([^<]+)</span>', S['cyber-briefing.html'])
ck(len(spans)==14, "cyber: %d kevdue spans, expected 14" % len(spans))
ahead=[t for c,t in spans if 'ok' in c]
past=[t for c,t in spans if 'crit' in c]
ck(len(ahead)==4, "cyber: %d ahead, expected 4" % len(ahead))
ck(len(past)==10, "cyber: %d past due, expected 10" % len(past))
ck(sorted(int(re.match(r'(\d+)',t).group(1)) for t in ahead)==[1,2,7,8],
   "cyber: days-left set is %s, expected [1,2,7,8]" % ahead)
for c,t in spans:
    ck(('past due' in t) == ('crit' in c), "cyber: kevdue colour/text disagree: %r %r" % (c,t))
ck('The board holds <b>14</b> entries' in S['cyber-briefing.html'],
   "cyber: prose summary must reconcile to 14 entries")
ck('10 are past due, none comes due today and 4 remain ahead' in S['cyber-briefing.html'],
   "cyber: prose split must read 10 past due / 0 today / 4 ahead")
ck(S['cyber-briefing.html'].count('13 entries')<=1, "cyber: '13 entries' appears more than once")

# ---- 10. champions board: 11 rows, no vacancies, no stale names ------------
mm=S['mma-briefing.html']
i=mm.find('Champions board')
if i<0: i=mm.lower().find('champions')
seg=mm[i:mm.find('</table>',i)]
rows=re.findall(r'<tr>(.*?)</tr>', seg, re.S)
ck(len(rows)==12, "mma: %d champion <tr> incl header, expected 12" % len(rows))
champ_col=[re.findall(r'<td>(.*?)</td>', r, re.S)[1] for r in rows[1:] if len(re.findall(r'<td>(.*?)</td>', r, re.S))>1]
ck(len(champ_col)==11, "mma: %d champion cells, expected 11" % len(champ_col))
ck(not any('acant' in c for c in champ_col), "mma: a division is listed vacant")
STALE=['Pereira','Chimaev','Topuria','Pantoja','Dvalishvili','Della Maddalena','O’Malley','Nurmagomedov']
for nm in STALE:
    ck(not any(nm in c for c in champ_col), "mma: STALE NAME %s in the champion column" % nm)
for nm in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van','Shevchenko','Harrison','Dern']:
    ck(any(nm in c for c in champ_col), "mma: %s missing from champion column" % nm)

# ---- 11. MMA countdown target ---------------------------------------------
ck('2026-08-29T06:00:00-04:00' in mm, "mma: countdown target missing/moved")
ck('2026-08-29T00:00:00' not in mm, "mma: countdown regressed to midnight")

# ---- 12. New-tag hygiene ---------------------------------------------------
tags=[]
for p in PAGES:
    tags += [(p,t) for t in re.findall(r'<span class="tag new">([^<]*)</span>', S[p])]
for p,t in tags:
    ck(t=='New &middot; 10:20', "%s: stale/bare New tag %r" % (p,t))
cnt={p:sum(1 for q,_ in tags if q==p) for p in PAGES}
ck(cnt['wallstreet-briefing.html']==1, "WS New count %d, expected 1" % cnt['wallstreet-briefing.html'])
ck(cnt['cyber-briefing.html']==1, "CY New count %d, expected 1" % cnt['cyber-briefing.html'])
ck(cnt['mma-briefing.html']==1, "MMA New count %d, expected 1" % cnt['mma-briefing.html'])
ck(cnt['index.html']==0, "index New count %d, expected 0" % cnt['index.html'])
for p in PAGES:
    ck('New &middot; 9:40</span>' not in S[p] or 'tag new">New &middot; 9:40' not in S[p],
       "%s: undemoted 9:40 New tag" % p)

# ---- 13. index-level reconciliation (Weekly Scorecard) --------------------
PRIOR={'S&amp;P 500':7652.86,'Dow Jones Industrial Average':53417.16,'Nasdaq Composite':25980.19}
ws=S['wallstreet-briefing.html']
seg=ws[ws.find('Weekly scorecard'):]
seg=seg[:seg.find('</table>')]
for name,prior in PRIOR.items():
    m=re.search(r'<tr><td>'+re.escape(name)+r'</td><td>([\d,\.]+)</td><td class="up">\+([\d\.]+)</td><td class="up">\+([\d\.]+)%</td></tr>', seg)
    ck(m is not None, "scorecard: no row for %s" % name)
    if not m: continue
    lvl=float(m.group(1).replace(',','')); pts=float(m.group(2)); pct=float(m.group(3))
    ck(round(lvl-pts,2)==round(prior,2), "%s: level-points != prior close (%.2f vs %.2f)" % (name,lvl-pts,prior))
    ck(abs(pts/prior*100-pct)<0.01, "%s: percent %.2f != points-derived %.4f" % (name,pct,pts/prior*100))
ck(ws.count('53,579.94')==1, "wallstreet: rejected Dow level appears %d times" % ws.count('53,579.94'))
j=ws.find('53,579.94')
ck('NOT published' in ws[j-400:j+400], "wallstreet: 53,579.94 not inside its rejection disclaimer")

# ---- 14. forward dates still in the future --------------------------------
TODAY=datetime.date(2026,8,26)
for lbl,d in (('UFC Shanghai',datetime.date(2026,8,29)),
              ('Oracle KEV due',datetime.date(2026,8,28)),
              ('Jackson Hole',datetime.date(2026,8,28))):
    ck(d>=TODAY, "%s date %s is in the past" % (lbl,d))
ck('August&nbsp;29' in mm, "mma: Aug 29 date marker missing")
ck('Aug 28' in S['cyber-briefing.html'] or 'August&nbsp;28' in S['cyber-briefing.html'],
   "cyber: Oracle Aug 28 deadline marker missing")

# ---- 15. content guards ----------------------------------------------------
MK=['$16.7&nbsp;billion','$16.68&nbsp;billion','up to $16 billion','29 states','Rob Bonta',
    '$1.5&nbsp;billion to $2.1&nbsp;billion','denies the allegations against it',
    '4:20&nbsp;p.m. ET','~10:20&nbsp;a.m. ET','+0.2% m/m, +3.7% y/y','3.3%','LSEG','8:35&nbsp;a.m. EDT',
    '38%','55%','$563.84','3.9%','&minus;11.8%','$315.30','7,677.28','26,151.30','53,577.40',
    'second estimate of second-quarter GDP','Mad Money']
for g in MK: ck(g in ws, "wallstreet: missing %r" % g)
CY=['5.03%','$46.90','20-day low','August&nbsp;25','a global disruption to the Company','Susan Thompson',
    'CVE-2026-69836','CVE-2026-60004','CVE-2026-73570','Fitzpatrick','nothing seen this run' ]
for g in CY[:-1]: ck(g in S['cyber-briefing.html'], "cyber: missing %r" % g)
MG=['Song Yadong','Umar Nurmagomedov','20-1 MMA, 8-1 UFC','23-9-1','Oriental Sports Center',
    '6:00 a.m. EDT','&minus;470','Denise Gomes','If I win this fight, I will get a title shot',
    'media day','shirt off']
for g in MG: ck(g in mm, "mma: missing %r" % g)

# ---- 16. trap greps --------------------------------------------------------
TRAPS=['Cody Salkilld','Abdul-Rakhman','Shamil Yakhyaev','title challenger Beneil','Shanghai Indoor Stadium',
       'Pereira retains','Featherweight vacant','markets closed higher today','@@T@@','UFC Fight Night 286',
       'UFC 336','UFC 335','no source fetched at 8:44','is not printing a number yet','−500 / +380',
       'Figueiro','U.S. markets are still not open','session has not opened','Figueiredo win at both']
for p in PAGES:
    for t in TRAPS:
        ck(t not in S[p], "%s: TRAP %r present" % (p,t))

# ---- 17. disclaimers -------------------------------------------------------
ck('not investment advice' in ws or 'not investment advice' in ws.lower(), "wallstreet: disclaimer missing")
ck('subject to change' in mm, "mma: disclaimer missing")

print("checks run: %d" % checks)
if fails:
    print("FAILURES: %d" % len(fails))
    for f in fails: print("  -", f)
    sys.exit(1)
print("0 failures")
