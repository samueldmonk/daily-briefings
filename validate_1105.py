import io, re, json, datetime
from html.parser import HTMLParser

FILES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
VOID = {'meta','link','br','img','hr','input','source','wbr'}
TODAY = datetime.date(2026, 8, 18)
ok = True
def bad(*a):
    global ok; ok = False; print('  ✗', *a)

class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.stack=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.stack.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.stack and s.stack[-1]==t: s.stack.pop()
        else: s.err.append('mismatch:'+t)

print('== 1. structure ==')
texts = {}
for f in FILES:
    txt = io.open(f, encoding='utf-8').read(); texts[f] = txt
    p = P(); p.feed(txt)
    if p.stack or p.err: bad(f, 'unclosed', p.stack[:5], 'errs', p.err[:5])
    else: print('  ✓ %-24s balanced' % f)
    for req in FILES + ['archive.html','id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        if req not in txt: bad(f, 'missing', req)
    n_active = txt.count('class="active"')
    if n_active != 1: bad(f, 'active tabs =', n_active)

print('== 2. tldr labels ==')
for f, lbl in [('cyber-briefing.html','The Wire'), ('wallstreet-briefing.html','The Tape'), ('mma-briefing.html','Tale of the Tape')]:
    if '<div class="tldr">' not in texts[f]: bad(f, 'no .tldr')
    elif '<b>%s</b>' % lbl not in texts[f]: bad(f, 'wrong tldr label, want', lbl)
    else: print('  ✓ %-24s %s' % (f, lbl))
if 'class="tldr"' in texts['index.html']: bad('index.html has a .tldr (should use cards)')
else: print('  ✓ index.html            no .tldr, by design')

print('== 3. tradingview widgets ==')
ws = texts['wallstreet-briefing.html']
wid = re.findall(r'embed-widget-[a-z-]+\.js" async>(\{.*?\})</script>', ws, re.S)
print('  widget blocks:', len(wid))
if len(wid) != 8: bad('expected 8 widget blocks')
for w in wid:
    try: json.loads(w)
    except Exception as e: bad('widget JSON parse fail', e)
else: print('  ✓ all widget JSON blocks parse')
tape = [w for w in wid if 'ticker-tape' in ws[max(0,ws.index(w)-160):ws.index(w)]]
tape_json = json.loads(tape[0]) if tape else {}
syms = [s['proName'] for s in tape_json.get('symbols', [])]
for need in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    if need not in syms: bad('ticker tape missing', need)
print('  ✓ ticker tape symbols:', ', '.join(syms))
cod = re.search(r'mini-symbol-overview\.js" async>\{"symbol":"([^"]+)"', ws)
print('  ✓ Chart of the Day =', cod.group(1) if cod else 'MISSING')
if not cod: bad('no chart of the day')

print('== 4. KEV countdowns recomputed vs', TODAY, '==')
cy = texts['cyber-briefing.html']
MON = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
rows = re.findall(r'Due <strong>(\w{3}) (\d+), (\d{4})</strong>\. <span class="cd (\w+)">\(([^)]+)\)</span>', cy)
if not rows: bad('no KEV rows parsed')
for mo, d, y, cls, lbl in rows:
    due = datetime.date(int(y), MON[mo], int(d))
    days = (due - TODAY).days
    if days < 0:
        want_cls, want_lbl = 'late', 'past due'
    elif days == 0:
        want_cls, want_lbl = 'late', '0 days left'
    else:
        want_cls = 'soon' if days <= 3 else 'ok'
        want_lbl = '%d day%s left' % (days, '' if days == 1 else 's')
    if cls != want_cls or lbl != want_lbl:
        bad('KEV %s %s %s -> class=%s label=%s, want class=%s label=%s' % (mo, d, y, cls, lbl, want_cls, want_lbl))
    else:
        print('  ✓ %s %s %s  %-12s %s' % (mo, d, y, lbl, cls))
print('  KEV rows:', len(rows))

print('== 5. patch priority / KEV agreement ==')
pri = re.search(r'class="priority">.*?</p>', cy, re.S).group(0)
if 'CVE-2025-62593' in pri and 'August 20, 2026' in pri and 'Aug 20, 2026' in cy:
    print('  ✓ Ray CVE-2025-62593 due Aug 20 in both Patch Priority and KEV list')
else: bad('patch priority / KEV deadline mismatch')

print('== 6. scorecard arithmetic ==')
sc = re.findall(r'<td>([^<]+)</td><td class="num">([\d,]+\.\d\d)</td><td class="num down">−([\d,]+\.\d\d)</td><td class="num down">−([\d.]+)%</td><td class="num">([\d,]+\.\d\d)</td>', ws)
if not sc: sc = re.findall(r'<td>([^<]+)</td>\s*<td class="num">([\d,]+\.\d\d)</td>\s*<td class="num down">&minus;([\d,]+\.\d\d)</td>\s*<td class="num down">&minus;([\d.]+)%</td>\s*<td class="num">([\d,]+\.\d\d)</td>', ws)
n_ok = 0
for name, last, chg, pct, prior in sc:
    L=float(last.replace(',','')); C=float(chg.replace(',','')); PR=float(prior.replace(',','')); PC=float(pct)
    if abs((PR - C) - L) > 0.02: bad('scorecard level mismatch', name)
    elif abs((C/PR*100) - PC) > 0.02: bad('scorecard pct mismatch', name, round(C/PR*100,3), PC)
    else: n_ok += 1; print('  ✓ %-30s %s - %s = %s  (%s%%)' % (name, prior, chg, last, pct))
if n_ok != 3: bad('expected 3 scorecard rows, verified', n_ok)

print('== 7. champions board ==')
mma = texts['mma-briefing.html']
champ = re.search(r'Champions board</h2>.*?</table>', mma, re.S).group(0)
crows = re.findall(r'<tr>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>', champ, re.S)
print('  champion rows:', len(crows))
if len(crows) != 11: bad('expected 11 champion rows')
stale = 0
for word in ['Pereira','Chimaev','Topuria','Vacant','Dvalishvili','Pantoja']:
    hits = [c[0] for c in crows if word in c[1]]
    if hits:
        stale += 1; bad('stale name in the CHAMPION cell of:', hits, '->', word)
if not stale:
    print('  ✓ no stale champion names in the champion column (notes cells may cite them)')
    for div, ch in crows: print('     %-26s %s' % (re.sub('<[^>]+>','',div), re.sub('<[^>]+>','',ch)))
for want in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Joshua Van','Shevchenko','Harrison','Mackenzie Dern']:
    if want not in champ: bad('champions board missing', want)
print('  ✓ all 11 expected champions present')

print('== 8. trap greps ==')
allt = ''.join(texts.values())
TRAPS = ['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','MacKenzie','Thainara Silva',
         'pay-per-view','Dayforce','Paylocity','32.4%','11.3%','4.5%','Klarna',
         'Bonfim vs. Brady','Joshua Vance','6,781.48','47,706.51','22,697.10','>Vacant<',
         'unification','54,215','7,720.01']
for tr in TRAPS:
    n = allt.count(tr)
    if n: bad('TRAP HIT %r x%d' % (tr, n))
print('  ✓ %d traps all zero' % len(TRAPS))
if allt.count('Mackenzie Dern') < 1: bad('Mackenzie Dern missing')
print('  ✓ "Mackenzie Dern" x%d' % allt.count('Mackenzie Dern'))
# Forminator must be 15748, not 19478
fm = re.search(r'CVE-2026-(\d+)</td><td class="score s-crit">9.8</td>\s*<td>Forminator', cy)
if not fm or fm.group(1) != '15748': bad('Forminator CVE is not 15748')
else: print('  ✓ Forminator = CVE-2026-15748 (not the GitLab 19478)')

print('== 9. after-hours (pre-4pm ET) ==')
n_ah = allt.count('After-Hours') + allt.count('After-hours')
if n_ah: bad('After-Hours block present before 4 PM ET')
else: print('  ✓ absent, correct for an 11 AM edition')

print('== 10. New tags ==')
for f in FILES:
    print('  %-24s New tags: %d' % (f, texts[f].count('tag new')))

print('== 11. Lazarus top story wiring ==')
for need in ['Lazarus','CVE-2026-68820','FudModule','MISTPEN','Operation Dream Job','Check Point Research']:
    if need not in cy: bad('cyber page missing', need)
if 'Lazarus' not in texts['index.html']: bad('index card missing Lazarus')
print('  ✓ Lazarus story present on cyber + index')

print()
print('RESULT:', 'ALL CHECKS PASSED' if ok else 'PROBLEMS FOUND')
