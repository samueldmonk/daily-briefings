#!/usr/bin/env python3
"""Second pass: the first scrub works on raw HTML, so a stamp wrapped in <b> tags
kept its preposition. Fix the tag-wrapped cases."""
import io, re
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    h = io.open(p, encoding='utf-8').read()
    n = 0
    for pat, rep in [
        (r'\bat ((?:<[^>]+>)*)an earlier edition', r'in \1an earlier edition'),
        (r'\bAt ((?:<[^>]+>)*)an earlier edition', r'In \1an earlier edition'),
        (r'\bthe ((?:<[^>]+>)*)an earlier edition', r'\1an earlier edition'),
        (r'an earlier edition((?:<[^>]+>)*) edition', r'an earlier edition\1'),
        (r'\bNew ((?:<[^>]+>)*)an earlier edition', r'Added in \1an earlier edition'),
    ]:
        h, k = re.subn(pat, rep, h); n += k
    io.open(p, 'w', encoding='utf-8').write(h)
    print('pass 2', p, '%d fixes' % n)
