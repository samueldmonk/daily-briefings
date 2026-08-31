#!/usr/bin/env python3
"""Real page defect: bare clock stamps that survived the day roll and now read
as THIS morning on a page stamped 1:12 PM Monday. None of them can be dated
from anything fetched this run, so they are relabelled 'earlier edition' rather
than given a guessed date. (Same class as the 11:33 fix; different instances.)"""
import io, re

FIXES = {
 'cyber-briefing.html': [
   ('Carried &middot; updated 11:05 AM', 'Carried &middot; updated in an earlier edition'),
   ('Carried &middot; sourced 10:50 AM.', 'Carried &middot; sourced in an earlier edition'),
   ('Carried &middot; sourced 10:50 AM', 'Carried &middot; sourced in an earlier edition'),
 ],
 'mma-briefing.html': [
   ('Carried &middot; updated 10:20 AM', 'Carried &middot; updated in an earlier edition'),
   ('New at 10:50 AM &mdash; what Song did with the microphone',
    'Added in an earlier edition &mdash; what Song did with the microphone'),
   ("re-read on a direct fetch at 10:50 AM",
    "re-read on a direct fetch in an earlier edition"),
 ],
}

for p, subs in FIXES.items():
    h = io.open(p, encoding='utf-8').read()
    n = 0
    for a, b in subs:
        c = h.count(a)
        if c:
            h = h.replace(a, b)
            n += c
            print('  %s: %d x %r' % (p, c, a[:50]))
    io.open(p, 'w', encoding='utf-8').write(h)
    print('%s: %d bare stamps relabelled' % (p, n))

# sanity: no bare "Carried &middot; <clock>" tag remains anywhere
for p in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
          'mma-briefing.html']:
    h = io.open(p, encoding='utf-8').read()
    bad = [m.group(1) for m in re.finditer(r'Carried &middot; ([^<]{0,40})', h)
           if not ('Aug' in m.group(1) or 'August' in m.group(1)
                   or 'earlier edition' in m.group(1) or 'from the' in m.group(1))]
    print('%s: %d bare stamps remaining %s' % (p, len(bad), bad[:5]))
