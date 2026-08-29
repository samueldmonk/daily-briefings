#!/usr/bin/env python3
"""Validation gate — Saturday 2026-08-29, 1:35 PM ET edition."""
import re, sys, os, collections

D = sys.argv[1] if len(sys.argv) > 1 else '.'
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
H = {f: open(os.path.join(D, f), encoding='utf-8').read() for f in PAGES}
TXT = {f: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)) for f, h in H.items()}

n = 0
fails = []


def ok(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)


def has(f, s, label=None):
    ok(s in H[f], '%s: missing %r' % (f, label or s[:70]))


def hasnt(f, s, label=None):
    ok(s not in H[f], '%s: FORBIDDEN present %r' % (f, label or s[:70]))


def near(f, a, b, w=420, label=''):
    """assert b appears within w chars of every occurrence of a (tag-stripped)."""
    t = TXT[f]
    idxs = [m.start() for m in re.finditer(re.escape(a), t)]
    ok(bool(idxs), '%s: anchor %r not found for near-check %s' % (f, a, label))
    for i in idxs:
        ok(b.lower() in t[max(0, i - w):i + w].lower(),
           '%s: %r not within %d chars of %r (%s)' % (f, b, w, a, label))


# ---------- structural: nav, masthead, self-stamp -----------------------------
for f in PAGES:
    for tab in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                'mma-briefing.html', 'archive.html']:
        has(f, 'href="%s"' % tab, 'nav tab ' + tab)
    ok(H[f].count('class="tabs"') >= 1, f + ': no tab nav')
    for i in ['id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"']:
        has(f, i, 'masthead id ' + i)
    has(f, "America/New_York", 'self-stamp tz')
    has(f, "briefings refresh every 30 minutes", 'freshline text')

# ---------- freshness: 1:35 stamped, 1:05 and 12:35 gone ----------------------
for f in PAGES:
    has(f, 'id="updated">1:35 PM ET</span>', '1:35 masthead fallback')
    has(f, 'id="freshline">Data as of 1:35 PM ET', '1:35 freshline')
    hasnt(f, 'id="updated">1:05 PM ET', 'stale 1:05 masthead')
    hasnt(f, 'id="freshline">Data as of 1:05 PM ET', 'stale 1:05 freshline')
    hasnt(f, 'id="updated">12:35 PM ET', 'stale 12:35 masthead')

# ---------- markets: closes, reconciliation, weekend discipline ---------------
W = 'wallstreet-briefing.html'
for s in ['7,711.76', '26,402.42', '53,559.99']:
    has(W, s, 'close level ' + s)
for s in ['0.25%', '0.52%', '0.02%']:
    has(W, s, 'close pct ' + s)
# Dow points/percent reconciliation
ok(abs((9.45 / 53559.99) * 100 - 0.02) < 0.005, 'Dow points/percent reconciliation failed')
ok(abs(53559.99 + 9.45 - 53569.44) < 0.01, 'Dow prior-close arithmetic failed')
hasnt(W, '7,673.04', 'retired S&P level 7,673.04')
hasnt(W, 'as of ~', 'intraday as-of marker on a closed-market page')
hasnt(W, 'After-Hours', 'after-hours block on a weekend page')
hasnt(W, 'After Hours', 'after-hours block on a weekend page (unhyphenated)')
# thirteenth-check breadth family
has(W, 're-verified a thirteenth time this run', 'thirteenth check')
has(W, 'the three weekly figures together', 'weekly figures in breadth claim')
has(W, 'third consecutive check of that breadth', 'third consecutive breadth')
hasnt(W, 're-verified a twelfth time', 'retired twelfth-check phrasing')
hasnt(W, 'the second consecutive check of that breadth', 'retired second-consecutive phrasing')
# contested December stays marked, no probability published
has(W, 'contested', 'contested December marking')
ok(not re.search(r'above 70% by December[^<]{0,80}(probability|odds) (is|are) \d', TXT[W]),
   'a December probability appears to be published')

# ---------- markets: all six TradingView widget blocks ------------------------
for w in ['embed-widget-ticker-tape', 'embed-widget-single-quote', 'embed-widget-timeline',
          'embed-widget-stock-heatmap', 'embed-widget-mini-symbol-overview', 'embed-widget-events']:
    has(W, w, 'TradingView ' + w)
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    has(W, sym, 'ticker symbol ' + sym)
has(W, 'NASDAQ:PYPL', 'Chart of the Day symbol PYPL')
ok(H[W].count('embed-widget-single-quote') == 3, 'expected exactly 3 single-quote widgets')
for f in ['index.html', 'cyber-briefing.html', 'mma-briefing.html']:
    ok('tradingview.com/external-embedding' not in H[f], f + ': live widgets must not appear here')

# ---------- cyber: ServiceNow pair discipline (carried from 1:05) -------------
C = 'cyber-briefing.html'
for cve in ['CVE-2026-18885', 'CVE-2026-18886', 'CVE-2026-74820', 'CVE-2026-6876', 'CVE-2026-6875']:
    has(C, cve, 'ServiceNow ' + cve)
near(C, 'CVE-2026-6875', 'exploited', 420, 'ServiceNow 6875 status')
near(C, 'CVE-2026-6876', 'not exploited', 420, 'ServiceNow 6876 status')
has(C, 'August 27', 'ServiceNow batch date')

# ---------- cyber: NEW OpenAI / Hugging Face family ---------------------------
has(C, 'Hugging Face', 'Hugging Face item')
has(C, 'not a new intrusion', 'HF freshness disclaimer')
has(C, 'July 21', 'HF disclosure date')
has(C, 'August 26, 2026', 'HF post-mortem date')
has(C, '38-page technical post-mortem', 'HF report description')
has(C, 'JFrog Artifactory', 'HF escape vector')
has(C, 'improvised message board', 'HF coordination detail')
has(C, '1,200 agents', 'HF agent count')
has(C, '70,000', 'HF message count')
# the three declinations
has(C, 'neither id is carried', 'HF CVE-id declination')
has(C, 'is <b>not printed</b>', 'HF timeline declination')
has(C, 'this page does not connect them', 'HF / KEV-66384 declination')
# 66384 appears three times (KEV board, Vulnerability Watch row, new card). EVERY one
# must decline the identification with the Hugging Face zero-day — this is the guard
# that found the page was already carrying the incident, so it stays per-occurrence.
for m in re.finditer('CVE-2026-66384', TXT[C]):
    w = TXT[C][max(0, m.start() - 700):m.start() + 700]
    ok('does not connect them' in w,
       'cyber: a CVE-2026-66384 mention lacks the non-identification note')
ok(len(re.findall('does not connect them', TXT[C])) >= 3,
   'cyber: expected the non-identification note on all three 66384 mentions')
# and the distinction must be stated on the merits, not only as absence of evidence
ok('requires an authenticated user' in TXT[C] or 'needs an authenticated user' in TXT[C],
   'cyber: 66384 distinction not stated on the merits')
# the page must acknowledge it already carried the incident
has(C, 'CVE-2026-53362', 'Linux kernel row tied to the OpenAI agents')
has(C, 'first contact with the incident', 'card acknowledges prior coverage')
# the incident must never be framed as fresh
hasnt(C, 'Hugging Face breach today', 'HF framed as today')
near(C, 'Hugging Face&rsquo;s production infrastructure', 'July', 900, 'HF dated to July')

# ---------- cyber: Hasbro recorded, not run ----------------------------------
has(C, 'Hasbro', 'Hasbro item')
has(C, 'March 28, 2026', 'Hasbro incident date')
has(C, 'April 1, 2026', 'Hasbro SEC date')
has(C, '436 Massachusetts employees', 'Hasbro MA AG figure')
has(C, 'it is not a new one', 'Hasbro not-new framing')
# The real requirement is that NO mention of Hasbro anywhere reads as a fresh breach.
# The card carries the Aflac comparison; the summary strip carries the March dating.
# Either frame satisfies it, so test for either rather than forcing one string on both.
for m in re.finditer('Hasbro', TXT[C]):
    w = TXT[C][max(0, m.start() - 900):m.start() + 900].lower()
    ok(('aflac' in w) or ('march' in w) or ('not a new one' in w),
       'cyber: a Hasbro mention lacks any not-fresh frame')
ok('Aflac' in TXT[C], 'cyber: Hasbro card must invoke the standing Aflac correction')
ok('Checked, not carried' in H[C], 'Hasbro card lacks the not-carried tag')

# ---------- cyber: KEV board -------------------------------------------------
for cve in ['CVE-2026-8452', 'CVE-2019-1068', 'CVE-2015-3246', 'CVE-2026-66384']:
    has(C, cve, 'KEV ' + cve)
has(C, 'BOD 26-04', 'risk-based BOD reference')
has(C, 'BOD 22-01', 'superseded BOD reference')
near(C, 'BOD 22-01', 'superseded', 420, 'BOD 22-01 marked superseded')
has(C, 'Re-checked again at 1:35 PM', '1:35 KEV recheck')
has(C, 'no CISA alert dated later than August 26', 'KEV liveness bound')
has(C, 'not the same as CISA having published none', 'KEV liveness caveat')
has(C, '0 / 1 / 11 / 12', 'KEV countdowns unchanged')
# Oracle still not carried
if 'CVE-2026-21962' in TXT[C]:
    near(C, 'CVE-2026-21962', 'not carried', 420, 'Oracle not-carried')
# CVE well-formedness + liveness
cves = re.findall(r'CVE-\d{4}-\d{4,6}', TXT[C])
ok(len(set(cves)) >= 15, 'expected >=15 distinct CVEs on the cyber page, saw %d' % len(set(cves)))
for c in set(cves):
    ok(re.fullmatch(r'CVE-\d{4}-\d{4,6}', c) is not None, 'malformed CVE id ' + c)

# ---------- cyber: PaperCut chain -------------------------------------------
for s in ['CVE-2026-81578', 'CVE-2026-82078', 'Emergency Patch Release 2']:
    has(C, s, 'PaperCut ' + s)

# ---------- MMA: champions board vs standing correction ----------------------
M = 'mma-briefing.html'
CHAMPS = ['Tom Aspinall', 'Carlos Ulberg', 'Sean Strickland', 'Islam Makhachev', 'Justin Gaethje',
          'Alexander Volkanovski', 'Petr Yan', 'Joshua Van', 'Valentina Shevchenko',
          'Kayla Harrison', 'Mackenzie Dern', 'Ciryl Gane']
for c in CHAMPS:
    has(M, c, 'champion ' + c)
# the three historical regressions must not reappear as current titles
# NB: this sweep was case-sensitive and hyphen-literal in its first form, so it missed
# "Interim:" and "Split decision" and fired on a page that was correct. The semantic
# requirement is unchanged; only the matching is fixed.
FRAMES = ['no longer', 'vacated', 'vacant title', 'lost', 'superseded', 'regression',
          'former', 'interim', 'stripped', 'took the belt from', 'upset',
          'split decision', 'split-decision', 'corrected', 'ko2', 'knocked out']
for bad, ctx in [('Pereira', 'Light Heavyweight'), ('Chimaev', 'Middleweight')]:
    for m in re.finditer(bad, TXT[M]):
        w = TXT[M][max(0, m.start() - 420):m.start() + 420].lower()
        ok(any(k in w for k in FRAMES),
           'MMA: %r appears without a corrective frame near %r' % (bad, ctx))

# Featherweight: the board must name Volkanovski, and no sentence may assert the belt is
# vacant. The earlier test read 300 chars after the LAST mention of "featherweight",
# which landed inside the passage REJECTING a false vacancy claim — it tested prose
# adjacency, not the assertion. Test the assertion instead.
ok(re.search(r'Featherweight\s+Alexander Volkanovski', TXT[M]) is not None,
   'MMA: champions board does not show Volkanovski at featherweight')
for pat in [r'featherweight (title |belt |)is vacant',
            r'featherweight[^.]{0,40}currently vacant',
            r'vacant featherweight']:
    ok(re.search(pat, TXT[M], re.I) is None,
       'MMA: featherweight asserted vacant (%s)' % pat)
has(M, 'fifty-sixth consecutive edition', 'champions counter advanced')
hasnt(M, 'fifty-third consecutive edition', 'stale champions counter')

# ---------- MMA: Shanghai result + bonuses -----------------------------------
has(M, 'Song Yadong', 'Shanghai winner')
has(M, 'Marc Goddard', 'referee')
has(M, '1:48', 'finish time')
has(M, 'knockout (punch)', 'official method')
has(M, '$100,000', 'bonus figure')
has(M, '$400,000', 'bonus total')
ok(4 * 100000 == 400000, 'bonus arithmetic')
# the descriptions-not-findings discipline
has(M, 'descriptions rather than findings', 'method-description rule')
has(M, 'Checked again at 1:35 PM, and nothing moved', '1:35 MMA check')
has(M, 'first MMA check today to add nothing at all', 'null-result recorded')
has(M, 'a check that confirms is not a check that found something', 'null-result framing')
# the 12:35 finding must no longer claim to be from this run
hasnt(M, 'newly sourced this run, Song ran straight', 'mis-scoped 12:35 finding')
has(M, 'sourced at 12:35 PM, Song ran straight', 're-scoped Jon Jones finding')
hasnt(M, 'at cageside', 'forbidden unsourced descriptor')

# ---------- MMA: cards are in the future / countdown -------------------------
has(M, 'id="ufccdn"', 'countdown element')
has(M, 'UFC 331', 'next numbered card')
has(M, 'UFC 333', 'Oct 24 card')
has(M, '2026-09-20T01:00:00Z', 'countdown target')
for d in ['Sept 5', 'Sept 19', 'Oct 24']:
    has(M, d, 'upcoming date ' + d)

# ---------- index cards mirror the tldrs exactly -----------------------------
for f, cls in [('cyber-briefing.html', 'c-cy'), ('wallstreet-briefing.html', 'c-ws'),
               ('mma-briefing.html', 'c-mm')]:
    body = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', H[f], re.S).group(1)
    card = re.search(r'<div class="bigcard ' + cls + r'">.*?<p>(.*?)</p>', H['index.html'], re.S).group(1)
    ok(body.strip() == card.strip(), 'index card for %s does not mirror its tldr' % f)
for f in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    ok('class="tldr"' in H[f], f + ': missing tldr strip')
for lab in ['The Wire', 'The Tape', 'Tale of the Tape']:
    ok(any(lab in H[f] for f in PAGES), 'missing tldr label ' + lab)
has('index.html', 'Read the briefing', 'index card links')

# ---------- footers: links absolute, no duplicates ---------------------------
for f in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    foot = H[f][H[f].rfind('<footer'):]
    hrefs = re.findall(r'href="(http[^"]+)"', foot)
    ok(len(hrefs) >= 20, '%s: only %d source links in footer' % (f, len(hrefs)))
    dupes = [u for u, c in collections.Counter(hrefs).items() if c > 1]
    ok(not dupes, '%s: duplicate footer hrefs: %s' % (f, dupes[:3]))
    for u in hrefs:
        ok(u.startswith('http'), '%s: non-absolute footer href %s' % (f, u))

# ---------- disclaimers ------------------------------------------------------
ok('not investment advice' in TXT[W].lower() or 'information only' in TXT[W].lower(),
   'wallstreet: missing disclaimer')
ok('subject to change' in TXT[M].lower(), 'mma: missing disclaimer')

print('%s: %d checks, %d failures' % (os.path.basename(__file__), n, len(fails)))
for x in fails:
    print('  FAIL', x)
sys.exit(1 if fails else 0)
