# -*- coding: utf-8 -*-
"""Self-contained archive.html generator. No external imports beyond css.py."""
import os, re, sys, datetime
import css as C

REPO = sys.argv[1]
ARCH = os.path.join(REPO, "archive")
SECT = {"cyber": ("The Cyber Wire", "#22d3a8"),
        "wallstreet": ("The Closing Bell", "#caa64a"),
        "mma": ("The Octagon", "#e84545")}
ORDER = ["cyber", "wallstreet", "mma"]

snaps = {}
pat = re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
for f in sorted(os.listdir(ARCH)):
    m = pat.match(f)
    if not m: continue
    sec, y, mo, d, hm = m.groups()
    day = "%s-%s-%s" % (y, mo, d)
    snaps.setdefault(day, {}).setdefault(hm, {})[sec] = f

def pretty_time(hm):
    h, mi = int(hm[:2]), hm[2:]
    ap = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    return "%d:%s %s ET" % (h12, mi, ap)

def pretty_day(day):
    dt = datetime.date(*map(int, day.split("-")))
    return dt.strftime("%A, %B ") + str(dt.day) + dt.strftime(", %Y")

CSS = C.base_css("#c8c4bd", "#e8e6e3", "#0c0d0f", "#15171a", "#242830") + """
.day{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--text);
  margin:30px 0 11px;padding-bottom:7px;border-bottom:1px solid var(--line)}
.ed{display:flex;flex-wrap:wrap;align-items:baseline;gap:9px;padding:9px 12px;border:1px solid var(--line);
  border-radius:10px;background:var(--panel);margin-bottom:8px;transition:.15s}
.ed:hover{border-color:#5a6270;transform:translateY(-1px)}
.ed .t{font-family:var(--mono);font-size:12px;color:var(--muted);min-width:96px}
.ed a{font-size:13.5px;font-family:var(--mono);letter-spacing:.05em;padding:3px 9px;border:1px solid var(--line);
  border-radius:7px}
.ed a:hover{text-decoration:none}
.a-cyber{color:#22d3a8}.a-cyber:hover{border-color:#22d3a8}
.a-wallstreet{color:#caa64a}.a-wallstreet:hover{border-color:#caa64a}
.a-mma{color:#e84545}.a-mma:hover{border-color:#e84545}
.miss{font-size:13.5px;font-family:var(--mono);letter-spacing:.05em;padding:3px 9px;color:#4d525c;
  border:1px dashed var(--line);border-radius:7px}
"""

H = [C.head("Archive &middot; Daily Briefings", CSS)]
H.append('<header class="masthead"><h1>Archive</h1>'
         '<p class="tag">Every edition, kept as a point-in-time snapshot</p>' + C.meta_row() + '</header>')
H.append('<div class="freshline" id="freshline">&nbsp;</div>')
H.append(C.nav("archive"))

days = sorted(snaps.keys(), reverse=True)
ned = sum(len(v) for v in snaps.values())
nsn = sum(len(t) for v in snaps.values() for t in v.values())
H.append('<div class="panel"><p style="font-size:14.5px;margin:0">'
         '<b>%d days &middot; %d editions &middot; %d snapshots.</b> Each entry is the page exactly as it was published at that '
         'time &mdash; figures, deadlines and countdowns are frozen at that moment and are <i>not</i> updated afterwards. '
         'For the current briefings use the tabs above. Snapshots older than 21 days are pruned.</p></div>'
         % (len(days), ned, nsn))

for day in days:
    H.append('<div class="day">%s</div>' % pretty_day(day))
    for hm in sorted(snaps[day].keys(), reverse=True):
        row = ['<div class="ed"><span class="t">%s</span>' % pretty_time(hm)]
        for sec in ORDER:
            label = SECT[sec][0]
            f = snaps[day][hm].get(sec)
            if f:
                row.append('<a class="a-%s" href="archive/%s">%s</a>' % (sec, f, label))
            else:
                row.append('<span class="miss">%s &mdash;</span>' % label)
        row.append('</div>')
        H.append("".join(row))

H.append('<footer><h5>Note</h5><ul>'
         '<li>Snapshots are historical records. A deadline countdown, a &ldquo;live&rdquo; marker or an intraday '
         'figure inside an old snapshot reflects the moment of publication, not today.</li>'
         '<li>The date and time pills inside a snapshot are rendered by the browser clock, so they will show '
         '<i>today</i>; the authoritative timestamp for a snapshot is the one in this index.</li>'
         '</ul><div class="disc">Assembled from public reporting. Provided for information only.</div></footer>')
H.append('</div>' + C.STAMP_JS + '</body></html>')

out = os.path.join(REPO, "archive.html")
open(out, "w").write("".join(H))
print("archive.html: %d days / %d editions / %d snapshots / %d bytes" % (len(days), ned, nsn, os.path.getsize(out)))
