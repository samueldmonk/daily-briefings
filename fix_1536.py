#!/usr/bin/env python3
"""Two real defects found by validate_1536: duplicate footer source links introduced
by this run's edits (the same URLs were already in the footers), and nothing else.
Drops the LATER duplicate of each href inside <footer>, keeping the first."""
import re, sys, io, os

D = sys.argv[1]
for fn in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    p = os.path.join(D, fn)
    h = io.open(p, encoding='utf-8').read()
    i = h.find('<footer>')
    head, foot = h[:i], h[i:]
    seen = set(); removed = []
    # each source is an <a ...>...</a> optionally followed by <br>
    def keep(m):
        url = m.group(1)
        if url in seen:
            removed.append(url); return ''
        seen.add(url); return m.group(0)
    foot2 = re.sub(r'<a href="([^"]+)">.*?</a>(?:<br>)?', keep, foot, flags=re.S)
    io.open(p, 'w', encoding='utf-8').write(head + foot2)
    print(f'{fn}: removed {len(removed)} duplicate footer links')
    for u in removed: print('   -', u)
