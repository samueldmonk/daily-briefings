#!/usr/bin/env python3
"""Line-by-line validation of all four pages — Sunday Aug 30 2026, seventh run."""
import re, sys, io, os, html as H

D = sys.argv[1]
FILES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
raw = {f: io.open(os.path.join(D, f), encoding='utf-8').read() for f in FILES}

def text(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s)))

txt = {f: text(raw[f]) for f in FILES}
def body(f):                      # body only: strip the sources footer
    t = txt[f]; i = t.find('Sources checked this run')
    return t if i == -1 else t[:i]

checks = 0; fails = []
def ck(cond, msg):
    global checks
    checks += 1
    if not cond: fails.append(msg)
def has(f, s, label=None):
    ck(s in txt[f], f'{f}: missing {label or s!r}')
def hasb(f, s, label=None):
    ck(s in body(f), f'{f} (body): missing {label or s!r}')
def no(f, s, label=None):
    ck(s not in txt[f], f'{f}: FORBIDDEN present {label or s!r}')
def nob(f, s, label=None):
    ck(s not in body(f), f'{f} (body): FORBIDDEN present {label or s!r}')

# ── A. Stamp, derived from the page itself ──────────────────────────────────
stamps = {}
for f in FILES:
    m = re.search(r'id="updated">([^<]+)</span>', raw[f]); ck(bool(m), f'{f}: no updated stamp')
    if m: stamps[f] = m.group(1).strip()
ck(len(set(stamps.values())) == 1, f'stamp mismatch across pages: {stamps}')
PUB = list(stamps.values())[0].replace(' ET', '')
def mins(s):
    m = re.match(r'(\d+):(\d\d) (AM|PM)', s); h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3)
    if ap == 'PM' and h != 12: h += 12
    if ap == 'AM' and h == 12: h = 0
    return h * 60 + mi
PROSE = '3:36 PM'
ck(mins(PROSE) <= mins(PUB), f'prose {PROSE} runs ahead of publish {PUB}')
for f in FILES:
    has(f, f'Data as of {PUB} ET', 'freshline matches stamp')
    has(f, 'Sunday, August 30, 2026', 'datestamp')
    has(f, 'Afternoon Edition', 'edition')
    for i in ('id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"'):
        ck(i in raw[f], f'{f}: masthead {i} missing')
    ck("Intl.DateTimeFormat" in raw[f], f'{f}: self-stamp JS missing')

# ── B. Nav: five tabs, exactly one active ───────────────────────────────────
for f in FILES:
    for href in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                 'mma-briefing.html', 'archive.html'):
        ck(f'href="{href}"' in raw[f], f'{f}: nav link {href} missing')
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', raw[f], re.S)
    ck(bool(nav), f'{f}: no nav')
    if nav: ck(nav.group(1).count('class="on"') == 1, f'{f}: active tab count != 1')

# ── C. Widgets: six TradingView blocks on WS only ───────────────────────────
W = 'wallstreet-briefing.html'
for w in ('ticker-tape', 'single-quote', 'timeline', 'stock-heatmap',
          'mini-symbol-overview', 'events'):
    ck(f'embed-widget-{w}.js' in raw[W], f'WS: widget {w} missing')
ck(raw[W].count('embed-widget-single-quote.js') == 3, 'WS: single-quote count != 3')
for sym in ('FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y', 'PYPL'):
    ck(sym in raw[W], f'WS: ticker symbol {sym} missing')
for f in FILES:
    if f != W: ck('tradingview.com' not in raw[f], f'{f}: unexpected widget')

# ── D. Markets ──────────────────────────────────────────────────────────────
for s in ('7,711.76', '26,402.42', '53,559.99', '26,541.35'):
    has(W, s, 'close level')
has(W, 'twenty-third verification')
has(W, '138.93'); has(W, '411.16')                     # Thursday/Friday identity
has(W, '39.9%', 'dated FedWatch prior')
has(W, 'August 21', 'FedWatch prior date')
has(W, '3.75')                                          # new range
has(W, '57%'); has(W, '43%'); has(W, '52%'); has(W, '48%')
has(W, '3.50')                                          # current range
has(W, 'tenth read')
# seasonality spread — four renderings, none adopted
for s in ('0.7%', '1.2%', '1.17%', '44%', '46%', '200-day', '1.3%', '4.2%', '15%'):
    has(W, s, 'seasonality figure')
has(W, 'none of the four is adopted')
# the 4.72 refusal must coexist with 4.73 kept
has(W, '4.72%'); has(W, '4.73%'); has(W, '4.67%'); has(W, '4.34%'); has(W, '5.20%')
has(W, 'recorded and not adopted')
nob(W, 'US 10-year Treasury yield 4.72%', '4.72 promoted into the table')
has(W, '$88.29'); has(W, '$83.44')
nob(W, 'Brent crude ~$88 a barrel Fri', 'stale round Brent row')
# calendar family
has(W, 'construction spending'); has(W, 'ISM Manufacturing')
has(W, 'September 4'); has(W, 'September 7', 'Labor Day date')
has(W, 'August 31')
no(W, 'Labor Day weekend on August 28', 'adopted bad holiday framing')
nob(W, 'payrolls Friday, September 5', 'wrong payrolls date')
has(W, 'Palo Alto Networks')
# undated-figure rejection frame must survive
for s in ('ten of the eleven sectors', '3.2%', '4.35%', '64%'):
    has(W, s, 'undated-rejection figure')
has(W, 'none of them is published')

# ── E. Cyber ────────────────────────────────────────────────────────────────
C = 'cyber-briefing.html'
# today's deadlines agree between Patch Priority and the KEV board
for s in ('CVE-2023-49105', 'CVE-2026-53362'):
    ck(body(C).count(s) >= 2, f'C: {s} must appear in both Patch Priority and KEV')
has(C, 'Sunday, August 30')
has(C, '0 days left'); has(C, 'OVERDUE')
has(C, '10 days left'); has(C, '11 days left')
# the demoted Citrix paragraph must no longer claim "today"
nob(C, 'That is today: the countdown below reads', 'Citrix contradiction survives')
has(C, 'EXPIRED YESTERDAY')
has(C, 'fourteenth check')
has(C, 'eighth consecutive check')
has(C, '24 new KEV entries')
# 68820 present, still no countdown row
has(C, 'CVE-2026-68820')
has(C, 'use-after-free'); has(C, 'heap-based buffer overflow')
ck('no row' in body(C) or 'gets no row' in body(C), 'C: 68820 no-row statement missing')
# ownCloud detail
for s in ('WebDAV', '10.13.1', '10.6.0 through 10.13.0', 'November\n2023'.replace('\n', ' '),
          'Chinese-speaking'):
    has(C, s, 'ownCloud detail')
# Cosmos family — and the arithmetic must be stated
for s in ('GHSA-7g4w-cg88-2cq2', '$5.72 million', '$2.87 million', '$2.85 million',
          'integer underflow', 'April 25', 'August 19', 'August 28', '40 networks',
          'three chains halted'):
    has(C, s, 'cosmos detail')
ck(abs((2.87 + 2.85) - 5.72) < 1e-9, 'cosmos arithmetic identity broken')
has(C, 'without a CVE identifier')
nob(C, '<code>GHSA', 'GHSA smuggled into the CVE table')
# Gitea sharpening
for s in ('8,393', 'Shai Rod', 'BOD 26-04', 'diffpatch'):
    has(C, s, 'gitea detail')
# stealer families
for s in ('Vidar', 'LummaC2', 'StealC', 'RedLine'):
    has(C, s, 'stealer family')
# standing refusals
has(C, 'Nevada'); has(C, 'November 5, 2025')
nob(C, '60-plus agencies in 2026', 'Nevada mis-shelved')
has(C, 'July 2026'); has(C, 'August 29 framing is not adopted')
# CVE well-formedness and liveness
cves = set(re.findall(r'CVE-\d{4}-\d{4,6}', txt[C]))
ck(len(cves) >= 20, f'C: only {len(cves)} distinct CVEs')
for c in cves: ck(bool(re.fullmatch(r'CVE-(19|20)\d{2}-\d{4,6}', c)), f'C: malformed {c}')

# ── F. MMA ──────────────────────────────────────────────────────────────────
M = 'mma-briefing.html'
has(M, '24-9-1'); has(M, '23-9-1')
has(M, 'I will work on the mistakes')
has(M, 'finished for the first time in his career')
has(M, 'No. 2'); has(M, 'No. 3'); has(M, 'Neither is adopted')
has(M, '1:48 of round two')
# UFC 333 card
for s in ('Alexander Volkov', 'Rizvan Kuniev', 'Arnold Allen', 'Aaron Pico', 'Dominick Reyes',
          'Azamat Murzakanov', 'Nikita Krylov', 'Abus Magomedov', 'Cam Rowston',
          'Grant Dawson', 'Nurullo Aliev', '2 PM ET', 'Etihad Arena', 'October 24'):
    has(M, s, 'UFC 333 detail')
has(M, 'Abdul Rakhman Yakhyaev')
no(M, 'Abdul-Rakhman', 'hyphenated Yakhyaev')
no(M, 'Shamil Yakhyaev', 'wrong Yakhyaev first name')
# champions board — the historically wrong belts
for s in ('Tom Aspinall', 'Carlos Ulberg', 'Sean Strickland', 'Islam Makhachev',
          'Justin Gaethje', 'Alexander Volkanovski', 'Petr Yan', 'Joshua Van',
          'Valentina Shevchenko', 'Kayla Harrison', 'Mackenzie Dern'):
    has(M, s, 'champion name')
nob(M, 'Light Heavyweight Alex Pereira', 'Pereira as LHW champ')
nob(M, 'Middleweight Khamzat Chimaev', 'Chimaev as MW champ')
nob(M, 'Featherweight Vacant', 'featherweight vacant')
nob(M, 'featherweight is vacant', 'featherweight vacant prose')
# descriptors
nob(M, 'former champion Beneil Dariush', 'Dariush miscast')
nob(M, 'title challenger Beneil Dariush', 'Dariush miscast')
# carried families that must survive this run's edits
for s in ('Bet Online', 'DraftKings', 'Tsarukyan', 'BetWay', 'Parnasse', 'Hooker'):
    has(M, s, 'odds family')
has(M, '13 fights'); has(M, 'Sept 5')
ck('id="ufccdn"' in raw[M], 'M: MMA countdown element missing')
# no adopted booking language
has(M, 'booked nothing after UFC 333') if 'booked nothing after UFC 333' in txt[M] else \
    ck('no title fight after UFC 333 has been booked' in txt[M], 'M: booking declination missing')

# ── G. Index mirrors each tldr exactly ──────────────────────────────────────
def tldr(f):
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', raw[f], re.S)
    return m.group(1) if m else None
for f, cls in [('cyber-briefing.html', 'c-cy'), ('wallstreet-briefing.html', 'c-ws'),
               ('mma-briefing.html', 'c-mm')]:
    t = tldr(f); ck(bool(t), f'{f}: tldr not found')
    i = raw['index.html'].find(f'<div class="bigcard {cls}">')
    ck(i != -1, f'index: card {cls} missing')
    if t and i != -1:
        ps = raw['index.html'].find('<p>', i); pe = raw['index.html'].find('</p>', ps)
        ck(raw['index.html'][ps+3:pe] == t, f'index: {cls} card does not mirror {f} tldr')
for lbl, f in [('The Wire', 'cyber-briefing.html'), ('The Tape', 'wallstreet-briefing.html'),
               ('Tale of the Tape', 'mma-briefing.html')]:
    ck(f'<b>{lbl}</b>' in raw[f], f'{f}: tldr label {lbl} missing')

# ── H. Footers ──────────────────────────────────────────────────────────────
for f in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    foot = raw[f][raw[f].find('<footer>'):]
    hrefs = re.findall(r'href="([^"]+)"', foot)
    ck(len(hrefs) >= 6, f'{f}: footer has {len(hrefs)} links')
    ck(all(u.startswith('http') for u in hrefs), f'{f}: relative href in footer')
    dupes = {u for u in hrefs if hrefs.count(u) > 1}
    ck(not dupes, f'{f}: duplicate footer hrefs {list(dupes)[:3]}')
    ck('not investment advice' in txt[f] or 'subject to change' in txt[f]
       or 'prints none rather than estimating one' in txt[f],
       f'{f}: disclaimer missing')
ck('not investment advice' in txt[W], 'WS: investment disclaimer missing')
ck('subject to change' in txt[M], 'MMA: change disclaimer missing')

# ── I. Tag classes are defined in CSS ───────────────────────────────────────
for f in FILES:
    css = ' '.join(re.findall(r'<style.*?</style>', raw[f], re.S))
    used = set()
    for m in re.finditer(r'class="tag ([a-z]+)"', raw[f]): used.add(m.group(1))
    for c in used:
        ck(f'.tag.{c}' in css or f'.tag.{c},' in css, f'{f}: tag class .tag.{c} undefined')


# ── J. Cross-page consistency ───────────────────────────────────────────────
ck('Five names, one punch' in txt[M], 'M: five-names statement missing')
ck('five different names' in txt['index.html'], 'index: punch count must mirror the MMA page')
ck('three different names across at least four reports' not in txt['index.html'],
   'index: stale three-names claim contradicts the MMA page')
ck('7,711.76' in txt['index.html'] and '7,711.76' in txt[W], 'index/WS close mismatch')
ck('$5.72 million' in txt[C] and '$5.72 million' in txt['index.html'], 'index/cyber cosmos mismatch')
ck('24-9-1' in txt[M] and '24-9-1' in txt['index.html'], 'index/MMA record mismatch')

print(f'validate_1536: {checks} checks, {len(fails)} failures')
for x in fails: print('  FAIL:', x)
sys.exit(1 if fails else 0)
