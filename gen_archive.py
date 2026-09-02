# -*- coding: utf-8 -*-
"""Rebuild archive.html from scratch from the contents of archive/.
No splice, no retained head, so there is no boundary that can drift."""
import os, re, sys, collections
import css as C

SECTIONS = [("cyber", "The Cyber Wire"), ("wallstreet", "The Closing Bell"), ("mma", "The Octagon")]
LABEL = dict(SECTIONS)
CSS = C.base_css("#8a94a6", "#b9c2d0", "#0b0c0e", "#14161a", "#252932") + """
h2.day{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent2);margin:30px 0 11px;padding-bottom:7px;border-bottom:1px solid var(--line)}
td a{margin-right:14px;white-space:nowrap}
td.t{font-family:var(--mono);color:var(--muted);white-space:nowrap}
"""

PAT = re.compile(r"^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$")


def h12(hhmm):
    h, m = int(hhmm[:2]), hhmm[2:]
    ap = "AM" if h < 12 else "PM"
    hh = h % 12 or 12
    return "%d:%s %s ET" % (hh, m, ap)


def main(root="."):
    d = os.path.join(root, "archive")
    files = sorted(os.listdir(d))
    files = [f for f in files if f.endswith(".html")]
    editions = collections.defaultdict(dict)          # (date, hhmm) -> {section: filename}
    parsed = 0
    for f in files:
        m = PAT.match(f)
        if not m:
            sys.exit("UNPARSED FILENAME IN archive/: %s" % f)   # never let one vanish silently
        parsed += 1
        sec, date, hhmm = m.groups()
        editions[(date, hhmm)][sec] = f
    assert parsed == len(files), "parsed %d of %d files" % (parsed, len(files))

    days = sorted({k[0] for k in editions}, reverse=True)

    p = [C.head("Archive — Daily Briefings", CSS)]
    p.append('<div class="masthead"><h1>Archive</h1>'
             '<p class="tag">Every edition, as it was published</p>' + C.meta_row() + "</div>")
    p.append('<div class="freshline" id="freshline">&nbsp;</div>')
    p.append(C.nav("archive"))
    p.append('<div class="panel"><p style="margin:0">Each link below is a <b>point-in-time snapshot</b> of '
             'a briefing exactly as it was published at that timestamp. Figures in an archived edition were '
             'correct to the sources available at that moment and are <b>not</b> updated afterwards; the '
             'live briefings are on the other tabs. Snapshots are kept for 21 days.</p></div>')

    intro_end = len(p)
    n_links = 0
    for day in days:
        stamps = sorted([k[1] for k in editions if k[0] == day], reverse=True)
        p.append('<h2 class="day">%s</h2>' % day)
        rows = []
        for s in stamps:
            got = editions[(day, s)]
            links = []
            for sec, label in SECTIONS:
                if sec in got:
                    links.append('<a href="archive/%s">%s</a>' % (got[sec], label))
                    n_links += 1
            rows.append('<tr><td class="t">%s</td><td>%s</td></tr>' % (h12(s), "".join(links)))
        p.append('<div class="tblwrap"><table><tr><th>Edition</th><th>Briefings</th></tr>'
                 + "".join(rows) + "</table></div>")

    p.append('<footer><h5>About</h5><ul><li>%d snapshots across %d editions and %d days.</li></ul>'
             '<div class="disc">Archived pages are historical records. Do not rely on an archived '
             'market level, CVE deadline or fight card as current.</div></footer>'
             % (len(files), len(editions), len(days)))
    p.append(C.STAMP_JS)
    p.append("</div></body></html>")
    out = "".join(p)

    # assertions
    assert out.count('<h2 class="day">') == len(days), "headings != days"
    assert out.count("<table>") == len(days), "tables != days"
    assert n_links == len(files), "links (%d) != files (%d)" % (n_links, len(files))
    assert out.count('class="active"') == 1, "not exactly one active nav tab"
    assert len(set(re.findall(r'<h2 class="day">([^<]+)</h2>', out))) == len(days), "duplicate headings"
    assert out.index('<h2 class="day">') > out.index("Snapshots are kept"), "headings must follow the intro"
    assert "tradingview.com" not in out, "archive must carry no live widgets"

    open(os.path.join(root, "archive.html"), "w").write(out)
    print("archive.html: %d days / %d editions / %d snapshots / %d bytes"
          % (len(days), len(editions), len(files), len(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
