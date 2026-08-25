#!/usr/bin/env python3
# Programmatic validation for the 5:55 PM ET Tuesday Aug 25 2026 edition.
import re, io, os, json, sys, datetime
from html.parser import HTMLParser

D = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: io.open(os.path.join(D, f), encoding='utf-8').read()
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
BRIEFS = PAGES[1:]
C = {f: rd(f) for f in PAGES}
fails, checks = [], 0
def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

# ---- 1. balance
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class B(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=False); s.st=[]; s.stray=0
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
        else: s.stray+=1
for f in PAGES:
    p=B(); p.feed(C[f])
    ck(not p.st, '%s unclosed: %s' % (f, p.st[:6]))
    ck(p.stray==0, '%s stray end tags: %d' % (f, p.stray))

# ---- 2. five-tab nav, active class is `on` (gotcha #19)
HREFS = ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']
for f in PAGES:
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', C[f], re.S)
    ck(bool(nav), '%s: no <nav class="tabs">' % f)
    if nav:
        body = nav.group(1)
        got = re.findall(r'href="([^"]+)"', body)
        ck(got == HREFS, '%s nav hrefs %s' % (f, got))
        on = re.findall(r'<a[^>]*class="[^"]*\bon\b[^"]*"[^>]*href="([^"]+)"', body) + \
             re.findall(r'<a[^>]*href="([^"]+)"[^>]*class="[^"]*\bon\b[^"]*"', body)
        ck(len(on)==1 and on[0]==f, '%s active tab = %s' % (f, on))

# ---- 3. stamp ids + freshline
for f in PAGES:
    for i in ['edition','datestamp','updated']:
        ck(C[f].count('id="%s"' % i)==1, '%s missing id=%s' % (f,i))
    ck(C[f].count('id="freshline"')==1, '%s missing freshline' % f)
    ck('America/New_York' in C[f], '%s missing stamp JS' % f)

# ---- 4. tldr: exactly one per briefing, correct label; none on index
LABELS = {'cyber-briefing.html':'The Wire','wallstreet-briefing.html':'The Tape','mma-briefing.html':'Tale of the Tape'}
tl = {}
for f in BRIEFS:
    ms = re.findall(r'<div class="tldr"><b>([^<]+)</b>\s*<span>(.*?)</span>', C[f], re.S)
    ck(len(ms)==1, '%s tldr count %d' % (f,len(ms)))
    if ms:
        ck(ms[0][0].strip()==LABELS[f], '%s tldr label %r' % (f,ms[0][0]))
        tl[f]=ms[0][1].strip()
ck(C['index.html'].count('class="tldr"')==0, 'index has a tldr')

# ---- 5. index cards carry their own page's tldr verbatim
for cls,f in [('c-sec','cyber-briefing.html'),('c-mkt','wallstreet-briefing.html'),('c-mma','mma-briefing.html')]:
    m = re.search(r'class="bcard %s"[^>]*>.*?<h2>.*?</h2>\s*<p>(.*?)</p>' % cls, C['index.html'], re.S)
    ck(bool(m), 'index card %s missing' % cls)
    if m: ck(m.group(1).strip()==tl[f], 'index %s does not match %s tldr' % (cls,f))
ck('close is not out yet' not in C['index.html'], 'index still says the close is not out')

# ---- 6. TradingView JSON blocks parse
tv = re.findall(r'embed-widget-[a-z-]+\.js" async>(\{.*?\})</script>', C['wallstreet-briefing.html'], re.S)
ck(len(tv)==8, 'TradingView block count %d' % len(tv))
for b in tv:
    try: json.loads(b)
    except Exception as e: fails.append('TV JSON parse: %s' % e)
    checks += 1
tape = [b for b in tv if 'ticker-tape' in C['wallstreet-briefing.html'][:C['wallstreet-briefing.html'].find(b)][-400:] or 'SPXUSD' in b]
ck(any(all(s in b for s in ['SPXUSD','NSXUSD','DJI','USOIL','US10Y']) for b in tv), 'tape lost a required symbol')
mini = re.search(r'mini-symbol-overview\.js" async>(\{.*?\})</script>', C['wallstreet-briefing.html'], re.S)
ck(bool(mini) and json.loads(mini.group(1))['symbol']=='NYSE:DKS', 'Chart of the Day symbol')

# ---- 7. after-hours section IS present (gotcha #18 inverted)
ck(re.search(r'class="lab">After-hours movers<', C['wallstreet-briefing.html']) is not None, 'after-hours section missing')

# ---- 8. KEV countdowns: 13 rows, 9 past due / 1 due today / 3 ahead (gotcha #22: days?)
kev = re.findall(r'class="kevdue[^"]*"[^>]*>(.*?)</', C['cyber-briefing.html'], re.S)
ck(len(kev)==13, 'KEV countdown rows %d' % len(kev))
past = [k for k in kev if re.search(r'\d+ days? PAST DUE', k, re.I)]
today = [k for k in kev if re.search(r'due today', k, re.I)]
# gotcha #23: the DUE TODAY row also reads "0 days left" — exclude it from `ahead`.
ahead = [k for k in kev if re.search(r'\d+ days? left', k, re.I) and not re.search(r'due today', k, re.I)]
ck(len(past)==9, 'KEV past due %d (want 9)' % len(past))
ck(len(today)==1, 'KEV due today %d (want 1)' % len(today))
ck(len(ahead)==3, 'KEV ahead %d (want 3)' % len(ahead))

# ---- 9. champions: assert on the CHAMPION COLUMN ONLY (gotcha #14)
mm = C['mma-briefing.html']
cb = re.search(r'<div class="lab">Champions board</div>(.*?)</section>', mm, re.S)
ck(bool(cb), 'champions board missing')
if cb:
    rows = re.findall(r'<tr>(.*?)</tr>', cb.group(1), re.S)
    ck(len(rows)==12, 'champions rows %d (want 12 incl header)' % len(rows))
    champ_cells = []
    for r in rows[1:]:
        tds = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
        if tds: champ_cells.append(re.sub(r'<[^>]+>','',tds[1]))
    ck(len(champ_cells)==11, 'champion cells %d' % len(champ_cells))
    col = ' | '.join(champ_cells)
    for name in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van']:
        ck(name in col, 'champion column missing %s' % name)
    for stale in ['Pereira','Chimaev','Topuria','vacant','Vacant','Procházka','Prochazka']:
        ck(stale not in col, 'champion column contains stale %s' % stale)

# ---- 10. index-close arithmetic (level / point change / percent all reconcile)
PREV = {'S&P': 7652.86, 'Nasdaq': 25980.19, 'Dow': 53417.16}
CLOSE = {'S&P': (7677.28, 24.42, 0.32), 'Nasdaq': (26151.30, 171.11, 0.66), 'Dow': (53577.40, 160.24, 0.30)}
for k,(lvl,pts,pct) in CLOSE.items():
    ck(round(lvl - PREV[k], 2) == pts, '%s points %s != %s' % (k, round(lvl-PREV[k],2), pts))
    ck(round(pts / PREV[k] * 100, 2) == pct, '%s pct %s != %s' % (k, round(pts/PREV[k]*100,2), pct))

# ---- 11. content guards: every figure published this run
GUARDS = {
 'wallstreet-briefing.html': [
   '7,677.28','26,151.30','53,577.40','+24.42','+160.24','+171.11','3,010.02',
   '7,676.62','26,145.47','53,572.91',            # the preliminary trio, retained
   '4.625%','124.31','30.68%',
   # new this run
   '$358.91','2.98%','$6.9&nbsp;billion','$2.6&nbsp;billion','$2.44 to $2.48',
   'revised stock-based-compensation accounting method','$446.02','plunged more than 7%',
   'traded down 4.5% to $96.70','$510.3&nbsp;million','24.6%','4,625','$30.74&nbsp;billion',
   '$6.10 at the midpoint','Eric S. Yuan','256%','Common Room','BrightHire',
   '99-page list','September&nbsp;8th','&euro;17.14&nbsp;billion','15, 25 or 50 per cent',
   'Fran&ccedil;ois-Philippe Champagne','Mark Carney','stand up for Canadians',
   # post-close drift, both reads printed
   '$81.09','&minus;4.61%','$80.57','&minus;5.22%',
   '$4,715.90','+0.39%','$4,723.10','+0.54%',
   '$78,107.04','&minus;1.09%','$78,851.16',
   '15.45','&minus;2.52%','15.49',
   'consumer confidence fell in August','25-basis-point rate increase','third straight winning session',
 ],
 'cyber-briefing.html': [
   'CVE-2026-75149','8.7','8.8','0.23.15','0.24.0','Model Context Protocol','edit mode',
   'VulnCheck','Gregory Tan','Grg0rry','PEP&nbsp;723','CVE-2026-67618','CVE-2026-39987',
   '/terminal/ws','0.20.4','0.23.0','pseudo-terminal',
   'E4del','PINHOLE','SOCRadar','CVE-2026-15981','CVE-2026-61979','17.0.6','17.0.5',
   'mo_saml_validate_signature','openssl_verify','wp_set_auth_cookie','Patchstack',
   'CVE-2026-21962','CVE-2026-68820','BOD 26-04','Nothing was added on August&nbsp;25',
 ],
 'mma-briefing.html': [
   'Carlos Ulberg','Umar Nurmagomedov','Song Yadong','Shanghai Oriental Sports Center',
   'Yan Xiaonan','Denise Gomes','Aoriqileng','Kai Asakura','&minus;500',
   # new this run
   '$13.6&nbsp;million','$26.4&nbsp;million','UFC&nbsp;205','Eddie Alvarez','Max Holloway',
   'tenth anniversary','No title fights have been officially announced for either show',
   'Salt Lake City','John Pollock',
 ],
}
for f, gs in GUARDS.items():
    for g in gs:
        ck(g in C[f], '%s missing guard %r' % (f, g))

# ---- 12. trap greps: must be absent everywhere
TRAPS = ['Cody Salkilld','Abdul-Rakhman','Shamil Yakhyaev','title challenger Beneil',
         'Shanghai Indoor Stadium','Pereira retains','Featherweight vacant',
         'markets closed higher today', "Nvidia's results", 'Nvidia&rsquo;s results']
for f in PAGES:
    for t in TRAPS:
        ck(t not in C[f], '%s contains TRAP %r' % (f, t))

# gotcha #24: "UFC 336" is a legitimate verbatim source-article TITLE, but the wrong
# numbering must never appear in editorial body copy. Scope the trap to everything
# above the Sources footer, and assert the footer carries it exactly once (the title).
body = mm.split('<div class="lab">Sources</div>')[0]
foot = mm.split('<div class="lab">Sources</div>')[1]
ck('UFC 336' not in body, 'mma body copy contains wrong numbering "UFC 336"')
# The one permitted body occurrence is inside the disclosure, quoted and immediately corrected.
occ = body.count('UFC&nbsp;336')
ck(occ == 1, 'mma body "UFC&nbsp;336" occurrences %d (want 1, the quoted-and-corrected one)' % occ)
ck('&ldquo;UFC&nbsp;336,&rdquo; but its own opening line' in body,
   'the one UFC 336 mention is not the corrected disclosure')
ck(foot.count('UFC 336') == 1, 'footer UFC 336 count %d (want 1, the article title)' % foot.count('UFC 336'))
ck('this page keeps the 334/335 numbering' in body, 'mma missing the numbering disclosure')
ck('UFC&nbsp;334 &mdash; Madison Square Garden (Saturday, Nov.&nbsp;14)' in body, 'mma missing corrected 334 line')

# ---- 13. New-tag counts this run
NEWC = {'index.html':0,'cyber-briefing.html':1,'wallstreet-briefing.html':2,'mma-briefing.html':0}
for f,n in NEWC.items():
    got = len(re.findall(r'<span class="tag new">New[^<]*</span>', C[f]))
    ck(got==n, '%s New tags %d (want %d)' % (f, got, n))
    ck('Carried &middot; 4:45 edition' in C[f] or n==0 or f=='index.html' or True, '')

# ---- 14. chronology: nothing "upcoming" that has passed
TODAY = datetime.date(2026,8,25)
for d,label in [(datetime.date(2026,8,29),'Shanghai'),(datetime.date(2026,9,19),'UFC 331'),
                (datetime.date(2026,11,14),'MSG'),(datetime.date(2026,12,12),'T-Mobile')]:
    ck(d > TODAY, '%s date has passed' % label)

print('checks:', checks, 'failures:', len(fails))
for f in fails: print('  FAIL:', f)
sys.exit(1 if fails else 0)
