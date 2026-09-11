#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory. Never hand-curated.
Keeps the existing page shell (head/CSS/masthead/nav/note) and the trailing stamp script;
rebuilds every day heading and row in between from filenames on disk only."""
import io, os, re, sys, datetime

D = sys.argv[1]
AP = os.path.join(D, 'archive')
page = os.path.join(D, 'archive.html')
s = io.open(page, encoding='utf-8').read()

LABEL = {'cyber': ('The Cyber Wire', '#22d3a8'),
         'wallstreet': ('The Closing Bell', '#caa64a'),
         'mma': ('The Octagon', '#e84545')}
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
    heading = '%s, %s %d, %d' % (day.strftime('%A'), day.strftime('%B'), day.day, day.year)
    out.append('<h2 class="day">%s</h2>\n' % heading)
    out.append('<table><thead><tr><th>Edition</th><th>Briefings</th></tr></thead><tbody>\n')
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        ampm = 'AM' if h < 12 else 'PM'
        h12 = h % 12 or 12
        cells = []
        for sec in ORDER:
            fn = snaps[dt][hhmm].get(sec)
            if fn:
                lab, col = LABEL[sec]
                cells.append('<a href="archive/%s" style="color:%s">%s</a>' % (fn, col, lab))
        out.append('<tr><td class="ts">%d:%02d %s ET</td><td class="lk">%s</td></tr>\n'
                   % (h12, mi, ampm, ' &middot; '.join(cells)))
    out.append('</tbody></table>\n')
rows = ''.join(out)

# head: everything through the intro note div; tail: from the wrapper close before the stamp script
m = re.search(r'<div class="note">.*?</div>\n', s, re.S)
head = s[:m.end()]
head = re.sub(r'\d+ snapshots held\.', '%d snapshots held.' % nfiles, head)
tail_start = s.index('</div>\n<script>(function()')
io.open(page, 'w', encoding='utf-8').write(head + rows + s[tail_start:])
print('archive.html rebuilt: %d days, %d editions, %d snapshot files' % (len(snaps), neds, nfiles))
