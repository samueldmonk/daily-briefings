#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory.

Replaces gen_archive_1943.py, which SILENTLY DOUBLED the whole listing on this run. Its splice
boundary was `s.index('</div>', s.index('never hand-curated'))` -- but the "never hand-curated"
sentence lives in the count line at the FOOT of the page, not in the intro note. So the "head"
it kept was the entire existing page including every previously generated row, and the fresh rows
were appended after them. 477 files rendered as 38 day headings.

This version uses boundaries that are unambiguous and idempotent:
  prefix = everything before the FIRST <h2>   (all generated content starts at the first <h2>)
  tail   = the trailing stamp <script> onward
Nothing between them survives a run, so the output cannot accumulate.
"""
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

if not snaps:
    sys.exit("no snapshots found - refusing to write an empty archive")

out, neds = [], 0
for dt in sorted(snaps, reverse=True):
    day = datetime.date(*dt)
    out.append('<h2>%s</h2><table><tr><th>Edition</th><th>Snapshots</th></tr>'
               % day.strftime("%A, %B %d, %Y").replace(" 0", " "))
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        ampm = "AM" if h < 12 else "PM"
        cells = []
        for sec in ORDER:
            fn = snaps[dt][hhmm].get(sec)
            cells.append('<a href="archive/%s">%s</a>' % (fn, LABEL[sec]) if fn
                         else '<span style="opacity:.45">%s</span>' % LABEL[sec])
        out.append('<tr><td class="ts">%d:%02d %s ET</td><td>%s</td></tr>'
                   % (h % 12 or 12, mi, ampm, " &middot; ".join(cells)))
    out.append("</table>")
rows = "".join(out)

foot = ('<div class="disc">%d snapshots across %d editions and %d days. Archive index is regenerated '
        'from the files on disk on every run &mdash; it is never hand-curated.</div></div>'
        % (nfiles, neds, len(snaps)))

prefix = s[:s.index("<h2>")]
tail = s[s.index("<script>(function()"):]
new = prefix + rows + foot + tail

# idempotence assertions: one heading per day, one table per day, no duplicates
assert new.count("<h2>") == len(snaps), "day headings (%d) != days (%d)" % (new.count("<h2>"), len(snaps))
assert new.count("<table>") == len(snaps), "tables != days"
assert new.count('href="archive/') == nfiles, "links (%d) != files (%d)" % (
    new.count('href="archive/'), nfiles)
assert new.count('class="on"') == 1, "nav active tab count != 1"
assert len(re.findall(r"<h2>[^<]+</h2>", new)) == len(set(re.findall(r"<h2>[^<]+</h2>", new))), \
    "duplicate day headings"

io.open(page, "w", encoding="utf-8").write(new)
print("archive.html rebuilt: %d days, %d editions, %d snapshot files, %d bytes"
      % (len(snaps), neds, nfiles, len(new)))
