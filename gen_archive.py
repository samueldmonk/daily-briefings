# -*- coding: utf-8 -*-
"""Regenerate archive.html whole from the snapshots present in archive/."""
import datetime, os, re, sys
from common import head, masthead, nav, STAMP_JS, FOOT

REPO = sys.argv[1]
ARCH = os.path.join(REPO, "archive")

PAL = """
:root{
  --bg:#0a0a0b; --panel:#141414; --line:#262626;
  --accent:#8fb3c8; --accent2:#e8c766;
  --txt:#ece9e3; --muted:#9b9690;
  --up:#22c55e; --down:#ef4444; --warn:#f0b429; --crit:#ef4444;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
h3.day{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent2);margin:26px 0 8px}
td.tm{font-family:var(--mono);white-space:nowrap;width:120px}
"""

SECTIONS = [("cyber", "The Cyber Wire"), ("wallstreet", "The Closing Bell"), ("mma", "The Octagon")]
PAT = re.compile(r"^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})\.html$")

editions = {}
unparsed = []
files = sorted(os.listdir(ARCH)) if os.path.isdir(ARCH) else []
for fn in files:
    if not fn.endswith(".html"):
        continue
    m = PAT.match(fn)
    if not m:
        unparsed.append(fn)
        continue
    sec, y, mo, d, hh, mm = m.groups()
    key = (datetime.date(int(y), int(mo), int(d)), int(hh), int(mm))
    editions.setdefault(key, {})[sec] = fn

def ampm(hh, mm):
    h12 = hh % 12 or 12
    return "%d:%02d %s ET" % (h12, mm, "AM" if hh < 12 else "PM")

days = {}
for (dt, hh, mm), got in editions.items():
    days.setdefault(dt, []).append((hh, mm, got))

o = []
o.append(head("Archive &mdash; Daily Briefings", PAL))
o.append(masthead("Archive", "Point-in-time snapshots of every edition, newest first"))
o.append('<div class="freshline" id="freshline">&nbsp;</div>\n')
o.append(nav("archive"))
o.append('<p class="note" style="margin-bottom:18px">Each row is a snapshot of the pages exactly as they were '
         'published at that moment. Snapshots are point-in-time and are never edited afterwards, so figures in an '
         'older edition describe the hour it was published and not the present. Snapshots older than 21 days are '
         'pruned. This index is regenerated in full on every run.</p>\n')

links = 0
for dt in sorted(days, reverse=True):
    o.append('<h3 class="day">%s</h3>\n' % dt.strftime("%A, %-d %B %Y"))
    o.append('<div class="panel" style="padding:6px 10px"><table>'
             "<tr><th>Edition</th><th>Snapshots</th></tr>")
    for hh, mm, got in sorted(days[dt], key=lambda x: (x[0], x[1]), reverse=True):
        cells = []
        for sec, label in SECTIONS:
            if sec in got:
                cells.append('<a href="archive/%s">%s</a>' % (got[sec], label))
                links += 1
            else:
                cells.append('<span class="mut">%s &mdash; not archived</span>' % label)
        o.append('<tr><td class="tm">%s</td><td>%s</td></tr>' % (ampm(hh, mm), " &middot; ".join(cells)))
    o.append("</table></div>\n")

o.append('<footer class="disc">%d snapshots across %d editions and %d days. '
         'Unparsed filenames: %d.</footer>\n' % (len(files), len(editions), len(days), len(unparsed)))
o.append(FOOT % STAMP_JS)

html = "".join(o)
with open(os.path.join(REPO, "archive.html"), "w") as f:
    f.write(html)

# --- self-check ---
hrefs = re.findall(r'href="archive/([^"]+)"', html)
broken = [h for h in hrefs if not os.path.exists(os.path.join(ARCH, h))]
linked = set(hrefs)
unlinked = [f for f in files if f.endswith(".html") and f not in linked and PAT.match(f)]
assert html.count("<body") == 1, "body count"
assert html.count("<footer") == 1, "footer count"
assert "tradingview" not in html.lower(), "no live widgets in archive"
assert not broken, "broken links: %s" % broken[:5]
assert not unlinked, "unlinked snapshots: %s" % unlinked[:5]
assert len(hrefs) == len(linked), "duplicate links"
print("archive ok: %d snapshots, %d editions, %d days, %d links, %d unique, "
      "0 broken, 0 unlinked, %d unparsed, %.1f KB"
      % (len(files), len(editions), len(days), len(hrefs), len(linked), len(unparsed), len(html) / 1024.0))
