#!/usr/bin/env python3
"""One job: restamp the freshline on all four pages and mirror each tldr into its index card."""
import io, sys, re
REPO = sys.argv[1]
TIME = '6:10 PM'
FRESH = ('<div class="freshline" id="freshline">Data as of %s ET &middot; briefings refresh every '
         '30 minutes, 8 AM&ndash;6 PM ET</div>' % TIME)

PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
for f in PAGES:
    p = REPO + '/' + f
    h = io.open(p, encoding='utf-8').read()
    h2 = re.sub(r'<div class="freshline" id="freshline">.*?</div>', FRESH, h, count=1, flags=re.S)
    assert h2 != h or FRESH in h, f
    io.open(p, 'w', encoding='utf-8').write(h2)
    print('restamped', f)

# mirror tldr -> index card, byte-for-byte on the inner span
idx = io.open(REPO + '/index.html', encoding='utf-8').read()
for src, cls in [('cyber-briefing.html', 'c-cy'),
                 ('wallstreet-briefing.html', 'c-ws'),
                 ('mma-briefing.html', 'c-mm')]:
    h = io.open(REPO + '/' + src, encoding='utf-8').read()
    t = re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>', h, re.S)
    assert t, src
    inner = t.group(1)
    i = idx.find('<div class="bigcard %s">' % cls)
    assert i >= 0, cls
    j = idx.find('<p>', i)
    k = idx.find('</p>', j)
    idx = idx[:j] + '<p>' + inner + idx[k:]
    print('mirrored', src, '->', cls, len(inner), 'bytes')

io.open(REPO + '/index.html', 'w', encoding='utf-8').write(idx)
