#!/usr/bin/env python3
# Freshness hygiene: in a 6:06 edition, nothing stamped with an EARLIER time may still call itself new.
# Covers BOTH the <span class="tag new"> form and the inline prose form ("New · 5:36").  Deferred write.
import os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
STALE = ['3:50', '4:14', '4:15', '4:36', '5:06', '5:36', '5:50',
         '10:20', '10:45', '10:55', '11:05', '11:37', '12:35', '12:50', '12:58',
         '1:05', '1:35', '1:40', '2:40', '3:05', '3:12', '3:38']
out, total = {}, 0
for p in PAGES:
    h = open(os.path.join(D, p)).read()
    n = 0
    for t in STALE:
        # tag form
        a = '<span class="tag new">New &middot; %s</span>' % t
        b = '<span class="tag">%s</span>' % t
        n += h.count(a); h = h.replace(a, b)
        # prose form
        a2 = '&#9679; New &middot; %s' % t
        b2 = '&#9679; %s' % t
        n += h.count(a2); h = h.replace(a2, b2)
    out[p] = h
    total += n
    print('%-26s demoted %d stale new-markers' % (p, n))
for p, h in out.items():
    open(os.path.join(D, p), 'w').write(h)
print('total demoted:', total)
