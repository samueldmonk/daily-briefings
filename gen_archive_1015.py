# -*- coding: utf-8 -*-
# Self-contained archive index generator: reuses the existing page head, regenerates all rows.
import io, os, re, datetime
SEC = {'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
old = io.open('archive.html', encoding='utf-8').read()
head = old[:old.find('<div class="panel"><p style="margin:0">')]
tail = '</div>\n' + old[old.rfind('<script>'):]

snaps = {}
for f in os.listdir('archive'):
    m = re.match(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$', f)
    if not m: continue
    s, d, t = m.groups()
    snaps.setdefault(d, {}).setdefault(t, {})[s] = f

def h12(t):
    h, mn = int(t[:2]), t[2:]
    return '%d:%s %s ET' % (h % 12 or 12, mn, 'AM' if h < 12 else 'PM')

rows = []
for d in sorted(snaps, reverse=True):
    dt = datetime.date(*map(int, d.split('-')))
    rows.append('<h2 class="sec">%s</h2><div class="panel"><table>' % dt.strftime('%A, %B %-d, %Y'))
    rows.append('<tr><th>Edition</th><th>Snapshots</th></tr>')
    for t in sorted(snaps[d], reverse=True):
        links = ' · '.join('<a href="archive/%s">%s</a>' % (snaps[d][t][k], SEC[k])
                           for k in ['cyber', 'wallstreet', 'mma'] if k in snaps[d][t])
        rows.append('<tr><td class="mono">%s</td><td>%s</td></tr>' % (h12(t), links))
    rows.append('</table></div>')

nd = len(snaps)
ne = sum(len(v) for v in snaps.values())
ns = sum(len(x) for v in snaps.values() for x in v.values())
intro = ('<div class="panel"><p style="margin:0">Point-in-time snapshots of every edition. Each file is exactly as it '
         'was published at that timestamp — figures, countdowns and live widgets were correct as of then and are '
         '<b>not</b> updated afterwards. Covering <b>%d days · %d editions · %d snapshots</b>.</p></div>' % (nd, ne, ns))
io.open('archive.html', 'w', encoding='utf-8').write(head + intro + ''.join(rows) + tail)
print('archive.html: %d days / %d editions / %d snapshots' % (nd, ne, ns))
