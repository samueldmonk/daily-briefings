#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory. Never hand-curated.
Usage: gen_archive_1635.py <repo-dir>"""
import io, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

D = sys.argv[1]
AP = os.path.join(D, "archive")

LABEL = {"cyber": ("The Cyber Wire", "#22d3a8"),
         "wallstreet": ("The Closing Bell", "#caa64a"),
         "mma": ("The Octagon", "#e84545")}
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

rows, neds = [], 0
for dt in sorted(snaps, reverse=True):
    day = datetime.date(*dt)
    rows.append('<h2 class="day">%s, %s %d, %d</h2>\n'
                % (day.strftime("%A"), day.strftime("%B"), day.day, day.year))
    rows.append('<div class="panel" style="padding:6px 10px"><table><thead><tr>'
                '<th>Edition</th><th>Briefings</th></tr></thead><tbody>\n')
    for hhmm in sorted(snaps[dt], reverse=True):
        neds += 1
        h, mi = int(hhmm[:2]), int(hhmm[2:])
        ampm = "AM" if h < 12 else "PM"
        h12 = h % 12 or 12
        cells = []
        for sec in ORDER:
            fn = snaps[dt][hhmm].get(sec)
            if fn:
                lab, col = LABEL[sec]
                cells.append('<a href="archive/%s" style="color:%s">%s</a>' % (fn, col, lab))
        rows.append('<tr><td class="ts">%d:%02d %s ET</td><td class="lk">%s</td></tr>\n'
                    % (h12, mi, ampm, " &middot; ".join(cells)))
    rows.append("</tbody></table></div>\n")

EXTRA = """
h2.day{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);
  margin:30px 0 11px;padding-bottom:7px;border-bottom:1px solid var(--line)}
td.ts{font-family:var(--mono);font-size:12.5px;color:var(--muted);white-space:nowrap;width:150px}
td.lk{font-size:13.5px}
"""
CSS = css("#9aa8ff", "#c3cbff", "#0b0c10", "#14161c", "#242833", EXTRA)

body = [
    masthead("Archive", "Every published edition, kept as a point-in-time snapshot"),
    '<div class="freshline" id="freshline">&nbsp;</div>',
    nav("archive"),
    '<div class="note" style="margin-bottom:18px">Each link opens the briefing exactly as it was published at that '
    'time &mdash; figures, deadlines and countdowns are frozen at that moment and are not refreshed. Snapshots older '
    'than 21 days are pruned. %d snapshots held.</div>' % nfiles,
    "".join(rows),
    '<p class="disc">Archived editions are historical records. Do not rely on a snapshot for a current market level, '
    'patch deadline or fight card.</p>',
]

io.open(os.path.join(D, "archive.html"), "w", encoding="utf-8").write(
    page("Archive &mdash; Daily Briefings", CSS, "\n".join(body)))
print("archive.html rebuilt: %d days, %d editions, %d snapshot files" % (len(snaps), neds, nfiles))
