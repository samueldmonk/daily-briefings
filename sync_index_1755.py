#!/usr/bin/env python3
# Sync each index.html card to its page's .tldr sentence, verbatim.
import re, io, os, sys
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: io.open(os.path.join(D, f), encoding='utf-8').read()

def tldr(f):
    c = rd(f)
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span>', c, re.S)
    assert m, f
    return m.group(1).strip()

pages = {'c-sec': 'cyber-briefing.html', 'c-mkt': 'wallstreet-briefing.html', 'c-mma': 'mma-briefing.html'}
idx = rd('index.html')
changed = []
for cls, page in pages.items():
    t = tldr(page)
    pat = re.compile(r'(class="bcard %s"[^>]*>.*?<h2>.*?</h2>\s*<p>)(.*?)(</p>)' % cls, re.S)
    m = pat.search(idx)
    assert m, cls
    if m.group(2).strip() != t:
        idx = idx[:m.start(2)] + t + idx[m.end(2):]
        changed.append(cls)

# The markets headline pre-dated the close being obtained.
old_h2 = '<h2>The bell has rung and the close is not out yet</h2>'
assert idx.count(old_h2) == 1
idx = idx.replace(old_h2, '<h2>A third straight winning session &mdash; and then the after-hours bill</h2>')
changed.append('c-mkt.h2')

io.open(os.path.join(D, 'index.html'), 'w', encoding='utf-8').write(idx)
print('index synced:', changed)

# verify
idx = rd('index.html')
for cls, page in pages.items():
    t = tldr(page)
    assert t in idx, 'MISMATCH ' + cls
print('all three index cards carry their page tldr verbatim')
