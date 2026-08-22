#!/usr/bin/env python3
"""Programmatic validation gate for the Aug 22 2026 ~6:05pm ET edition."""
import io, os, re, sys, json, datetime
from html.parser import HTMLParser

D = sys.argv[1]
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'archive.html']
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
fails = []

def chk(cond, msg):
    print(("  PASS  " if cond else "  FAIL  ") + msg)
    if not cond:
        fails.append(msg)

src = {}
for p in PAGES:
    fp = os.path.join(D, p)
    src[p] = io.open(fp, encoding='utf-8').read() if os.path.exists(fp) else ''

# ---- 1. HTML balance
print("\n[1] HTML balance")
class B(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
        else: s.err.append(t)
for p in PAGES:
    if not src[p]: continue
    b=B(); b.feed(src[p])
    chk(not b.st and not b.err, "%s balanced (unclosed=%s errors=%s)" % (p, b.st[:4], b.err[:4]))

# ---- 2. nav + stamp ids
print("\n[2] Five-tab nav, stamp IDs, one active tab")
for p in PAGES:
    if not src[p]: continue
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', src[p], re.S)
    chk(bool(nav), "%s has <nav class=tabs>" % p)
    if nav:
        body = nav.group(1)
        for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
            chk(('href="%s"' % href) in body, "%s nav links %s" % (p, href))
        chk(body.count('border-color:#')==1, "%s nav has exactly 1 active tab (found %d)" % (p, body.count('border-color:#')))
    for i in ['id="edition"','id="datestamp"','id="updated"']:
        chk(i in src[p], "%s has %s" % (p, i))
    if p != 'archive.html':
        chk('id="freshline"' in src[p], "%s has freshline" % p)

# ---- 3. tldr labels
print("\n[3] Summary strips")
for p, lab in [('cyber-briefing.html','The Wire'), ('wallstreet-briefing.html','The Tape'), ('mma-briefing.html','Tale of the Tape')]:
    chk(('<div class="tldr"><b>%s</b>' % lab) in src[p], "%s .tldr labelled '%s'" % (p, lab))
chk('class="tldr"' not in src['index.html'], "index.html has no .tldr (by design)")

# ---- 4. TradingView widgets
print("\n[4] TradingView widget JSON")
blobs = re.findall(r'embed-widget-[a-z-]+\.js" async>(\{.*?\})</script>', src['wallstreet-briefing.html'], re.S)
chk(len(blobs)==8, "8 widget blocks found (got %d)" % len(blobs))
okj=0
for b in blobs:
    try: json.loads(b); okj+=1
    except Exception as e: print("     bad json:", e)
chk(okj==len(blobs), "all %d widget JSON blocks parse" % len(blobs))
tape = [b for b in blobs if '"symbols"' in b]
if tape:
    syms = json.loads(tape[0])['symbols']
    pro = [s['proName'] for s in syms]
    for need in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
        chk(need in pro, "ticker tape retains %s" % need)
mini = [b for b in blobs if 'dateRange' in b]
chk(bool(mini), "Chart of the Day present: %s" % (json.loads(mini[0])['symbol'] if mini else 'NONE'))

# ---- 5. KEV countdowns
print("\n[5] KEV countdowns vs today")
today = datetime.date(2026, 8, 22)
rows = re.findall(r'<li><b>(CVE-[\d-]+)</b>.*?due <b>(\d{4}-\d{2}-\d{2})</b> <span class="kev-(\w+)">\(([^)]+)\)</span>', src['cyber-briefing.html'])
chk(len(rows)>=3, "found %d KEV rows with explicit due dates" % len(rows))
for cve, due, cls, label in rows:
    d = (datetime.date(*map(int, due.split('-'))) - today).days
    if d < 0:
        exp_lbl, exp_cls = "%d day%s PAST DUE" % (abs(d), '' if abs(d)==1 else 's'), 'crit'
    elif d == 0:
        exp_lbl, exp_cls = "due today", 'crit'
    else:
        exp_lbl, exp_cls = "%d day%s left" % (d, '' if d==1 else 's'), ('soon' if d<=3 else 'ok')
    chk(label.strip()==exp_lbl and cls==exp_cls, "%s due %s -> '%s' [%s] (expected '%s' [%s])" % (cve, due, label, cls, exp_lbl, exp_cls))
total_kev = len(re.findall(r'<li><b>CVE-', src['cyber-briefing.html']))
pastdue = src["cyber-briefing.html"].count(chr(60)+chr(115)+"pan class=\"kev-crit\">")
chk(total_kev==10, "10 KEV rows total (got %d)" % total_kev)
chk(pastdue==7, "7 past-due rows (got %d)" % pastdue)
chk('<b>7 are past due</b>' in src['cyber-briefing.html'], "KEV note states 7 past due")
chk('<div class="n">7</div>' in src['cyber-briefing.html'], "stat strip states 7")

# ---- 6. Patch Priority <-> KEV agreement
print("\n[6] Patch Priority consistency")
cy = src['cyber-briefing.html']
pp = re.search(r'<div class="callout crit">(.*?)</div>', cy, re.S).group(1)
chk('CVE-2026-59310' in pp and 'CVE-2026-72529' in pp, "Patch Priority names 59310 (past due) and 72529 (next deadline)")
chk('August 23' in pp, "Patch Priority states Aug 23 for TrueConf")
chk('due <b>2026-08-23</b>' in cy, "KEV section agrees on 2026-08-23")
chk('CVSS 9.3' in pp, "Patch Priority carries the new TrueConf CVSS 9.3")
chk('No CVSS score is printed here for either TrueConf' not in cy, "stale 'no CVSS' note removed")

# ---- 7. Champions board
print("\n[7] Champions board")
mm = src['mma-briefing.html']
champ = re.search(r'Champions Board.*?</table>', mm, re.S)
chk(bool(champ), "champions table present")
if champ:
    body = champ.group(0)
    trs = re.findall(r'<tr>(?!<th)', body)
    chk(len(re.findall(r'<tr>', body))-1 == 11, "11 champion rows (got %d)" % (len(re.findall(r'<tr>', body))-1))
    chk('>Vacant<' not in body, "no Vacant cells")
    for name in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Joshua Van','Shevchenko','Harrison','Dern']:
        chk(name in body, "champions board lists %s" % name)

# ---- 8. Trap greps (past regressions)
print("\n[8] Trap greps (must be absent)")
allsrc = "\n".join(src.values())
traps = ['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','MacKenzie','Joshua Vance',
         'Pereira (205)','pay-per-view','former champion','title challenger',
         'Chimaev</td>','Pantoja</td>','Dvalishvili</td>','Topuria</td>']
for t in traps:
    chk(t not in allsrc, "absent: %r" % t)
chk('not exploited' in src['cyber-briefing.html'].lower(), "Entra ID CVE-2026-69836 still labelled NOT exploited")
chk('exploited zero-day' not in src['cyber-briefing.html'].lower() or 'Entra' not in src['cyber-briefing.html'], "Entra not called an exploited zero-day")

# ---- 9. Weekend rules
print("\n[9] Weekend framing")
ws = src['wallstreet-briefing.html']
chk('After-Hours' not in ws or 'no post-close session' in ws or 'weekend' in ws.lower(),
    "no unsourced after-hours section on a Saturday")
chk('7,674.37' in ws and '53,277' in ws and '26,180' in ws, "Friday Aug 21 closes present")

# ---- 10. Scorecard arithmetic
print("\n[10] Scorecard arithmetic")
for name, lvl, chg, pct in [("S&P 500", 7674.37, 33.21, 0.43),
                            ("Dow", 53277.01, 517.80, 0.98),
                            ("Nasdaq", 26180.45, 113.29, 0.43)]:
    prior = lvl - chg
    calc = chg / prior * 100
    chk(abs(calc - pct) < 0.02, "%s: %.2f - %.2f = %.2f -> %.2f%% (page says %.2f%%)" % (name, lvl, chg, prior, calc, pct))

# ---- 11. MMA no-results rule
print("\n[11] MMA results rule")
chk('No results are published on this page' in mm, "MMA page states no results published")
for w in ['def. Reed','def. Emmers','def. Nzechukwu','def. Padilla','def. Dorsainvil','def. Schultz']:
    chk(w not in mm, "uncorroborated result absent: %r" % w)

print("\n" + "="*60)
print("FAILURES: %d" % len(fails))
for f in fails: print("  - " + f)
sys.exit(1 if fails else 0)
