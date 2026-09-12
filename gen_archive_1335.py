#!/usr/bin/env python3
"""Snapshot this edition, prune by FILENAME DATE (not mtime), regenerate archive.html."""
import os, re, shutil, datetime, sys

REPO = "/tmp/db_1789232738"
OUT  = "/sessions/sleepy-hopeful-carson/mnt/outputs"
ARCH = os.path.join(REPO, "archive")
TS   = sys.argv[1]                      # YYYY-MM-DD-HHMM
TODAY = datetime.date(*map(int, TS.split("-")[:3]))

os.makedirs(ARCH, exist_ok=True)
for sec, f in (("cyber", "cyber-briefing.html"),
               ("wallstreet", "wallstreet-briefing.html"),
               ("mma", "mma-briefing.html")):
    shutil.copy(os.path.join(OUT, f), os.path.join(ARCH, "%s-%s.html" % (sec, TS)))

# ---- prune strictly older than 21 days, by the date encoded in the filename ----
PAT = re.compile(r"^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$")
files, pruned, days = [], 0, {}
for fn in os.listdir(ARCH):
    m = PAT.match(fn)
    if not m: continue
    d = datetime.date(int(m.group(2)), int(m.group(3)), int(m.group(4)))
    age = (TODAY - d).days
    if age > 21:
        os.remove(os.path.join(ARCH, fn)); pruned += 1; continue
    files.append((d, m.group(5), m.group(1), fn))
    days.setdefault(d, set()).add(m.group(5))

oldest = min(days) if days else None
print("snapshots: %d across %d days | oldest %s (%d days) | pruned %d"
      % (len(files), len(days), oldest, (TODAY - oldest).days if oldest else -1, pruned))

# ---- regenerate archive.html body, preserving the existing shell ----
ap = os.path.join(REPO, "archive.html")
shell = open(ap, encoding="utf-8").read()
i = shell.find('<h3 class="day">')
j = shell.find("<footer>")
if i == -1 or j == -1:
    raise SystemExit("archive.html shell anchors missing (<h3 class=\"day\"> / <footer>)")
head, tail = shell[:i], shell[j:]

LABEL = {"cyber": "The Cyber Wire", "wallstreet": "The Closing Bell", "mma": "The Octagon"}
ORDER = ["cyber", "wallstreet", "mma"]

def hhmm(t):
    h, mnt = int(t[:2]), t[2:]
    ap_ = "AM" if h < 12 else "PM"
    hh = h % 12 or 12
    return "%d:%s %s ET" % (hh, mnt, ap_)

body = []
for d in sorted(days, reverse=True):
    body.append('<h3 class="day">%s</h3><div class="panel" style="padding:6px 10px"><table>'
                '<tr><th>Edition</th><th>Snapshots</th></tr>'
                % d.strftime("%A, %-d %B %Y"))
    for t in sorted(days[d], reverse=True):
        links = []
        for sec in ORDER:
            fn = "%s-%s-%s.html" % (sec, d.isoformat(), t)
            if os.path.exists(os.path.join(ARCH, fn)):
                links.append('<a href="archive/%s">%s</a>' % (fn, LABEL[sec]))
        body.append("<tr><td><b>%s</b></td><td>%s</td></tr>" % (hhmm(t), " · ".join(links) or "—"))
    body.append("</table></div>")

open(ap, "w", encoding="utf-8").write(head + "".join(body) + tail)
print("archive.html regenerated: %d day sections" % len(days))
