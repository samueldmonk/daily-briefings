# -*- coding: utf-8 -*-
import os, re, sys
sys.path.insert(0,'/sessions/modest-elegant-johnson/build')
from common import BASE_CSS, STAMP_JS, meta_row, nav

SEC = {'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
ORDER = ['cyber','wallstreet','mma']
pat = re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')

snaps = {}
for f in os.listdir('archive'):
    m = pat.match(f)
    if not m: continue
    sec, date, hhmm = m.groups()
    snaps.setdefault(date, {}).setdefault(hhmm, {})[sec] = f

MON = ['January','February','March','April','May','June','July','August','September','October','November','December']
def prettydate(d):
    y,m,dd = [int(x) for x in d.split('-')]
    import datetime
    wd = datetime.date(y,m,dd).strftime('%A')
    return "%s, %s %d, %d" % (wd, MON[m-1], dd, y)

def prettytime(h):
    hh, mm = int(h[:2]), h[2:]
    ap = 'AM' if hh < 12 else 'PM'
    h12 = hh % 12 or 12
    return "%d:%s %s ET" % (h12, mm, ap)

CSS = """
.day{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;
 color:#8fa0b0;margin:28px 0 10px;padding-bottom:7px;border-bottom:1px solid var(--line)}
.arow{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px;padding:9px 13px;
 background:var(--panel);border:1px solid var(--line);border-radius:10px;margin-bottom:8px}
.arow .t{font-family:var(--mono);font-size:12.5px;color:#e8edf2;min-width:96px}
.arow a{font-size:13.6px;text-decoration:none;color:#8fa0b0;border:1px solid var(--line);
 border-radius:7px;padding:3px 10px;transition:.15s}
.arow a:hover{color:#e8edf2;border-color:#3a4652}
.arow a.cyber:hover{color:#22d3a8}.arow a.wallstreet:hover{color:#e8c766}.arow a.mma:hover{color:#ff8a5c}
"""

H = ['<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
     '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
     '<title>Archive — Daily Briefings</title>\n<style>%s%s</style>\n</head>\n<body>\n<div class="wrap">\n' % (BASE_CSS, CSS)]
H.append('<div class="masthead">\n<h1>Archive</h1>\n'
         '<p class="tag">Point-in-time snapshots of every edition, newest first</p>\n%s\n</div>' % meta_row())
H.append('<div class="freshline" id="freshline">&nbsp;</div>')
H.append(nav("archive.html", "#8fa0b0"))
H.append('<div class="panel" style="margin-top:4px"><p style="margin:0;font-size:14.5px;color:#c6d2dd">'
         'Each entry below is the page exactly as it was published at that moment. Snapshots are frozen: '
         'the live data widgets on the markets page are not present, and figures reflect what was verified at '
         'the time of that run, not now. Snapshots older than 21 days are pruned automatically.</p></div>')

total = 0
for date in sorted(snaps.keys(), reverse=True):
    H.append('<div class="day">%s</div>' % prettydate(date))
    for hhmm in sorted(snaps[date].keys(), reverse=True):
        row = ['<div class="arow"><span class="t">%s</span>' % prettytime(hhmm)]
        for sec in ORDER:
            f = snaps[date][hhmm].get(sec)
            if f:
                total += 1
                row.append('<a class="%s" href="archive/%s">%s</a>' % (sec, f, SEC[sec]))
        row.append('</div>')
        H.append("".join(row))

H.append('<footer>\n<div class="lab">Note</div>\n<ul>\n<li>%d snapshots indexed across %d days. This page is regenerated from the archive directory on every run.</li>\n</ul>\n' % (total, len(snaps)))
H.append('<p class="disc">Archived editions are historical records and are not updated after publication.</p>\n</footer>\n')
H.append(STAMP_JS)
H.append('\n</div>\n</body>\n</html>\n')

open('archive.html','w').write("\n".join(H))
print("archive.html:", total, "snapshots,", len(snaps), "days")
