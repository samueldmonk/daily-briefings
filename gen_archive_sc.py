#!/usr/bin/env python3
"""Self-contained archive.html regenerator: rebuilds the row list from archive/*.html.

Preserves the existing head/CSS/masthead/nav/intro block and the trailing footer+stamp
script, and regenerates ONLY the day headings and snapshot rows in between.
"""
import io, os, re, sys, datetime

D = sys.argv[1]
AP = os.path.join(D, 'archive')
page = os.path.join(D, 'archive.html')
s = io.open(page, encoding='utf-8').read()

SEC = {'cyber': ('cyber', 'The Cyber Wire'),
       'wallstreet': ('wallstreet', 'The Closing Bell'),
       'mma': ('mma', 'The Octagon')}

# collect: {(date, hhmm): {section: filename}}
snaps = {}
pat = re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
for fn in os.listdir(AP):
    m = pat.match(fn)
    if not m:
        continue
    sec, y, mo, d, hhmm = m.groups()
    snaps.setdefault(((int(y), int(mo), int(d)), hhmm), {})[sec] = fn

# group by day, descending; times descending within a day
bydate = {}
for (dt, hhmm), secs in snaps.items():
    bydate.setdefault(dt, {})[hhmm] = secs

out = []
for dt in sorted(bydate, reverse=True):
    day = datetime.date(*dt)
    out.append('<div class="day">%s</div>' % day.strftime('%A, %B %-d, %Y'))
    for hhmm in sorted(bydate[dt], reverse=True):
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        ampm = 'AM' if h < 12 else 'PM'
        h12 = h % 12 or 12
        row = ['<div class="arow"><span class="t">%d:%02d %s ET</span>' % (h12, mi, ampm)]
        for sec in ('cyber', 'wallstreet', 'mma'):
            fn = bydate[dt][hhmm].get(sec)
            cls, label = SEC[sec]
            if fn:
                row.append('<a class="%s" href="archive/%s">%s</a>' % (cls, fn, label))
            else:
                row.append('<span class="t" style="opacity:.45">%s —</span>' % label)
        row.append('</div>')
        out.append(''.join(row))

rows = "\n".join(out)

# splice: keep everything up to and including the intro panel, and the footer onward
head_end = s.index('</div>', s.index('Snapshots older than 21 days are pruned automatically.')) + len('</div>')
tail_start = s.index('<footer') if '<footer' in s else s.index('<script>(function()')
new = s[:head_end] + "\n" + rows + "\n" + s[tail_start:]
io.open(page, 'w', encoding='utf-8').write(new)

ndays = len(bydate)
nrows = sum(len(v) for v in bydate.values())
print("archive.html rebuilt: %d days, %d timestamped rows, %d snapshot files"
      % (ndays, nrows, len(os.listdir(AP))))
