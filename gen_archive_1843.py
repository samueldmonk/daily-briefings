#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory — never hand-curated.
Matches the CURRENT page shell: the intro <div class="panel"><p style="margin:0…"> panel
(whose counts this script rewrites) followed by one <h2 class="sec"> + panel-wrapped table
per day, and the trailing stamp script. Rewritten from gen_archive_2040.py, whose
'Snapshots older than 21 days are pruned.' anchor no longer exists in the shell."""
import io, os, re, sys, datetime

D = sys.argv[1]
AP = os.path.join(D, 'archive')
page = os.path.join(D, 'archive.html')
s = io.open(page, encoding='utf-8').read()

LABEL = {'cyber': 'The Cyber Wire', 'wallstreet': 'The Closing Bell', 'mma': 'The Octagon'}
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
    out.append('\n  <h2 class="sec">%s, %s %d, %d</h2>\n' %
               (day.strftime('%A'), day.strftime('%B'), day.day, day.year))
    out.append('  <div class="panel" style="padding:6px 10px">\n  <table>\n')
    out.append('    <tr><th>Edition</th><th>Snapshots</th></tr>\n')
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        stamp = '%d:%02d %s ET' % (h % 12 or 12, mi, 'AM' if h < 12 else 'PM')
        cells = ['<a href="archive/%s">%s</a>' % (snaps[dt][hhmm][sec], LABEL[sec])
                 for sec in ORDER if sec in snaps[dt][hhmm]]
        out.append('    <tr><td class="num">%s</td><td>%s</td></tr>\n'
                   % (stamp, ' &middot; '.join(cells)))
    out.append('  </table>\n  </div>\n')
rows = ''.join(out)

# rewrite the counts inside the intro panel, then swap everything between it and the tail
s = re.sub(r'<b>\d+ days · \d+ editions · \d+ snapshot files\.</b>',
           '<b>%d days · %d editions · %d snapshot files.</b>' % (len(snaps), neds, nfiles), s, count=1)
intro = re.search(r'<div class="panel"><p style="margin:0[^\n]*</p></div>\n', s)
assert intro, 'intro panel anchor not found — shell changed again'
tail = s.index('</div>\n<script>(function()')
io.open(page, 'w', encoding='utf-8').write(s[:intro.end()] + rows + '\n' + s[tail:])
print('archive.html rebuilt: %d days, %d editions, %d snapshot files' % (len(snaps), neds, nfiles))
