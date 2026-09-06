# -*- coding: utf-8 -*-
import re, sys
tl = {}
for k, f in [('cy','cyber-briefing.html'), ('ws','wallstreet-briefing.html'), ('mma','mma-briefing.html')]:
    t = open(f).read()
    tl[k] = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', t, re.S).group(1)

t = open('index.html').read()
cards = re.findall(r'<p>(.*?)</p>\n<a class="read"', t, re.S)
if len(cards) != 3: sys.exit("expected 3 index cards, got %d" % len(cards))
for old, new in zip(cards, [tl['cy'], tl['ws'], tl['mma']]):
    t = t.replace('<p>%s</p>\n<a class="read"' % old, '<p>%s</p>\n<a class="read"' % new, 1)

# Card headlines resynced to this edition's leads
def head(old, new):
    global t
    if old not in t: sys.exit("MISS headline: " + old[:60])
    t = t.replace(old, new, 1)

head('<h3>An unpatched Magento zero-day is backdooring stores now</h3>',
     '<h3>The only StyleSmuggler fixes are unofficial &mdash; and two devs wrote the same one</h3>')

open('index.html','w').write(t)

# verify
t2 = open('index.html').read()
for k in ('cy','ws','mma'):
    assert tl[k] in t2, "card not synced: " + k
print("index synced; 3 cards match their tldrs verbatim")
