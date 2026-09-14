#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory. Never hand-curated.
Keeps the page shell (head/CSS/masthead/nav/intro note) and the trailing stamp script;
rebuilds every day heading and edition row in between from filenames on disk only."""
import io, os, re, sys, datetime

D = sys.argv[1]
AP = os.path.join(D, "archive")
page = os.path.join(D, "archive.html")
s = io.open(page, encoding="utf-8").read()

LABEL = {"cyber": "The Cyber Wire", "wallstreet": "The Closing Bell", "mma": "The Octagon"}
ORDER = ["cyber", "wallstreet", "mma"]

snaps, nfiles = {}, 0
pat = re.compile(r"^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$")
for fn in sorted(os.listdir(AP)):
    m = pat.match(fn)
    if not m:
        continue
    nfiles += 1
    sec, y, mo, d, hhmm = m.groups()
    snaps.setdefault((int(y), int(mo), int(d)), {}).setdefault(hhmm, {})[sec] = fn

out, neds, nlinks = [], 0, 0
for dt in sorted(snaps, reverse=True):
    day = datetime.date(*dt)
    out.append('<div class="dayh">%04d-%02d-%02d</div><div class="arch">' % dt)
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        ampm = "AM" if h < 12 else "PM"
        h12 = h % 12 or 12
        cells = []
        for sec in ORDER:
            fn = snaps[dt][hhmm].get(sec)
            if fn:
                nlinks += 1
                cells.append('<a href="archive/%s">%s</a>' % (fn, LABEL[sec]))
        out.append('<div class="erow"><span class="etime">%d:%02d %s ET</span>%s</div>'
                   % (h12, mi, ampm, "".join(cells)))
    out.append("</div>")
rows = "".join(out)

anchor = "</div>"
i = s.find('<div class="dayh">')
assert i > 0, "no day heading anchor"
j = s.rfind("</div></div><script>")
assert j > i, "no tail anchor"
head, tail = s[:i], s[j + len("</div></div>"):]
new = head + rows + tail
io.open(page, "w", encoding="utf-8").write(new)

# post-generation assertions
assert new.count('<a href="archive/') == nlinks, "link count != snapshot count"
assert new.count('<div class="erow">') == neds, "edition row count"
assert new.count('<div class="dayh">') == len(snaps), "day heading count"
assert new.count('class="active"') == 1, "exactly one active tab"
for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]:
    assert 'href="%s"' % href in new, "nav link " + href
assert "tradingview" not in new.lower(), "archive must carry no live widgets"
assert new.rstrip().endswith("</html>"), "well formed"
print("archive.html rebuilt: %d days, %d editions, %d snapshot files" % (len(snaps), neds, nfiles))
