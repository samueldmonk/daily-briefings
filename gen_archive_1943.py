#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory. Never hand-curated.

Preserves the page shell (head/CSS/masthead/nav) and the trailing stamp script; replaces
the intro count line and every day heading + row between them.
"""
import io, os, re, sys, datetime
D = sys.argv[1]
AP = os.path.join(D, 'archive')
page = os.path.join(D, 'archive.html')
s = io.open(page, encoding='utf-8').read()

LABEL = {'cyber': 'The Cyber Wire', 'wallstreet': 'The Closing Bell', 'mma': 'The Octagon'}
ORDER = ['cyber', 'wallstreet', 'mma']

snaps = {}
pat = re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
nfiles = 0
for fn in sorted(os.listdir(AP)):
    m = pat.match(fn)
    if not m: continue
    nfiles += 1
    sec, y, mo, d, hhmm = m.groups()
    snaps.setdefault((int(y), int(mo), int(d)), {}).setdefault(hhmm, {})[sec] = fn

out = []
neds = 0
for dt in sorted(snaps, reverse=True):
    day = datetime.date(*dt)
    out.append('<h2>%s</h2><table><tr><th>Edition</th><th>Snapshots</th></tr>'
               % day.strftime('%A, %B %d, %Y').replace(' 0', ' '))
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        ampm = 'AM' if h < 12 else 'PM'
        cells = []
        for sec in ORDER:
            fn = snaps[dt][hhmm].get(sec)
            if fn:
                cells.append('<a href="archive/%s">%s</a>' % (fn, LABEL[sec]))
            else:
                cells.append('<span style="opacity:.45">%s</span>' % LABEL[sec])
        out.append('<tr><td class="ts">%d:%02d %s ET</td><td>%s</td></tr>'
                   % (h % 12 or 12, mi, ampm, ' &middot; '.join(cells)))
    out.append('</table>')
rows = ''.join(out)

# 1. intro count line, regenerated from what is actually on disk
s = re.sub(r'<b>\d+ snapshots across \d+ editions and \d+ days\.</b>',
           '<b>%d snapshots across %d editions and %d days.</b>' % (nfiles, neds, len(snaps)),
           s, count=1)
# 2. splice rows between the intro note and the stamp script
head_end = s.index('</div>', s.index('never hand-curated')) + len('</div>')
tail_start = s.index('<script>(function()')
# the rows sit inside the page wrapper; keep whatever closing tags precede the script
tail = s[tail_start:]
wrap_close = '</div>' if s[:tail_start].count('<div class="wrap"') else ''
io.open(page, 'w', encoding='utf-8').write(s[:head_end] + rows + wrap_close + tail)
print('archive.html rebuilt: %d days, %d editions, %d snapshot files' % (len(snaps), neds, nfiles))
