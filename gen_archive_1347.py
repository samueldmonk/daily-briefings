#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory. Never hand-curated.

Keeps the page shell (head/CSS/masthead/nav/intro note) and the trailing stamp script;
replaces every day heading and row between them, derived only from filenames on disk.
"""
import io, os, re, sys, datetime

D = sys.argv[1]
AP = os.path.join(D, 'archive')
page = os.path.join(D, 'archive.html')
s = io.open(page, encoding='utf-8').read()

LABEL = {'cyber': 'The Cyber Wire', 'wallstreet': 'The Closing Bell', 'mma': 'The Octagon'}
COLOR = {'cyber': '#22d3a8', 'wallstreet': '#caa64a', 'mma': '#e84545'}
ORDER = ['cyber', 'wallstreet', 'mma']

snaps, nfiles = {}, 0
pat = re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
for fn in sorted(os.listdir(AP)):
    m = pat.match(fn)
    if not m:
        continue
    nfiles += 1
    sec, y, mo, d, hhmm = m.groups()
    snaps.setdefault((int(y), int(mo), int(d)), {}).setdefault(hhmm, {})[sec] = fn

out, neds = [], 0
for dt in sorted(snaps, reverse=True):
    day = datetime.date(*dt)
    heading = '%s, %d %s %d' % (day.strftime('%A'), day.day, day.strftime('%B'), day.year)
    out.append('<h2 class="sec">%s</h2><table><tr><th>Edition</th><th>Snapshots</th></tr>\n' % heading)
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        cells = []
        for sec in ORDER:
            fn = snaps[dt][hhmm].get(sec)
            if fn:
                cells.append('<a href="archive/%s" style="color:%s">%s</a>' % (fn, COLOR[sec], LABEL[sec]))
            else:
                cells.append('<span style="opacity:.4">%s</span>' % LABEL[sec])
        out.append('<tr><td style="font-family:var(--mono);white-space:nowrap">%d:%02d %s ET</td><td>%s</td></tr>\n'
                   % (h % 12 or 12, mi, 'AM' if h < 12 else 'PM', ' &nbsp;&middot;&nbsp; '.join(cells)))
    out.append('</table>\n')
rows = ''.join(out)

INTRO_END = 'Snapshots older than 21 days are pruned.</p></div>'
head_end = s.index(INTRO_END) + len(INTRO_END)
tail_start = s.index('<script>(function()')
tail = s[tail_start:]

# the wrapper close that sat just before the script, if any
between = s[head_end:tail_start]
wrap_close = '\n</div>\n' if between.rstrip().endswith('</div>') else '\n'

io.open(page, 'w', encoding='utf-8').write(s[:head_end] + '\n' + rows + wrap_close + tail)
print('archive.html rebuilt: %d days, %d editions, %d snapshot files' % (len(snaps), neds, nfiles))
