#!/usr/bin/env python3
# Restamp masthead/freshline from the clock, and mirror each briefing's tldr into its index card.
import re, sys, io, datetime, zoneinfo
REPO = sys.argv[1]
def rd(f): return io.open(REPO+'/'+f, encoding='utf-8').read()
def wr(f,s): io.open(REPO+'/'+f,'w',encoding='utf-8').write(s)

now = datetime.datetime.now(zoneinfo.ZoneInfo('America/New_York'))
date_s = now.strftime('%A, %B %-d, %Y')
time_s = now.strftime('%-I:%M %p') + ' ET'
h24 = now.hour
edition = 'Morning Edition' if h24 < 11 else ('Midday Edition' if h24 < 15 else 'Afternoon Edition')
fresh = 'Data as of %s &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET' % time_s
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']

# id-first-or-not tolerant: match any <span ...> whose attribute list contains id="X"
def stamp(h, idname, text):
    pat = re.compile(r'(<span\b[^>]*\bid="%s"[^>]*>)(.*?)(</span>)' % idname, re.S)
    h2, n = pat.subn(lambda m: m.group(1) + text + m.group(3), h, count=1)
    assert n == 1, 'stamp failed: ' + idname
    return h2

for f in PAGES:
    h = rd(f)
    h = stamp(h, 'datestamp', date_s)
    h = stamp(h, 'updated', time_s)
    h = stamp(h, 'edition', edition)
    h2, n = re.subn(r'(<div class="freshline" id="freshline">).*?(</div>)',
                    lambda m: m.group(1) + fresh + m.group(2), h, count=1, flags=re.S)
    assert n == 1, 'freshline failed: ' + f
    wr(f, h2)
print('stamped:', date_s, '|', time_s, '|', edition)

# ---- mirror tldrs into index cards (byte-identical)
tl = {}
for f, label in [('cyber-briefing.html', 'The Wire'),
                 ('wallstreet-briefing.html', 'The Tape'),
                 ('mma-briefing.html', 'Tale of the Tape')]:
    m = re.search(r'<div class="tldr"><b>%s</b> <span>(.*?)</span></div>' % re.escape(label), rd(f), re.S)
    assert m, 'no tldr: ' + f
    tl[f] = m.group(1)

idx = rd('index.html')
for f, cls in [('cyber-briefing.html', 'c-cy'), ('wallstreet-briefing.html', 'c-ws'), ('mma-briefing.html', 'c-mm')]:
    pat = re.compile(r'(<div class="bigcard %s">.*?<p>)(.*?)(</p>)' % cls, re.S)
    idx, n = pat.subn(lambda m: m.group(1) + tl[f] + m.group(3), idx, count=1)
    assert n == 1, 'card failed: ' + cls
wr('index.html', idx)

# verify byte equality both ways
idx = rd('index.html')
for f, cls in [('cyber-briefing.html', 'c-cy'), ('wallstreet-briefing.html', 'c-ws'), ('mma-briefing.html', 'c-mm')]:
    m = re.search(r'<div class="bigcard %s">.*?<p>(.*?)</p>' % cls, idx, re.S)
    assert m.group(1) == tl[f], 'MIRROR MISMATCH ' + cls
assert '<div class="tldr">' not in idx, 'index must not carry a tldr strip'
print('index cards mirror all three tldrs byte-for-byte')
