# -*- coding: utf-8 -*-
"""Self-contained archive index generator for daily-briefings. Deterministic / idempotent."""
import os, re, sys, datetime, io
REPO = sys.argv[1]
SEC = {'cyber': 'The Cyber Wire', 'wallstreet': 'The Closing Bell', 'mma': 'The Octagon'}
ORDER = ['cyber', 'wallstreet', 'mma']

snaps = {}
for f in sorted(os.listdir(os.path.join(REPO, 'archive'))):
    m = re.match(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$', f)
    if not m:
        continue
    s, d, t = m.groups()
    snaps.setdefault(d, {}).setdefault(t, {})[s] = f

def h12(t):
    h, mn = int(t[:2]), t[2:]
    ap = 'AM' if h < 12 else 'PM'
    return '%d:%s %s ET' % (h % 12 or 12, mn, ap)

CSS = """
:root{--bg:#0f0f11;--panel:#17171a;--line:#26262b;--accent:#9aa0a6;--accent2:#cfcdc9;
 --text:#e8e6e3;--muted:#9aa0a6;--up:#22c55e;
 --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);
 font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:980px;margin:0 auto;padding:26px 20px 60px}
a{color:var(--accent2);text-decoration:none}a:hover{text-decoration:underline}
.masthead{border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:4px}
.masthead h1{margin:0 0 2px;font-size:34px;letter-spacing:-.5px;line-height:1.15}
.masthead .tag{color:var(--muted);font-size:14.5px;margin:0}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.pill{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;
 background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 11px;color:var(--muted)}
.pill.live{color:var(--up);border-color:rgba(34,197,94,.35)}
.pill.live .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up);
 margin-right:6px;vertical-align:middle}
.freshline{font-family:var(--mono);font-size:11px;color:var(--muted);margin:9px 2px 4px;letter-spacing:.03em}
nav.tabs{display:flex;flex-wrap:wrap;gap:7px;margin:14px 0 20px;border-bottom:1px solid var(--line);padding-bottom:12px}
nav.tabs a{font-family:var(--mono);font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;
 padding:7px 13px;border:1px solid var(--line);border-radius:8px;color:var(--muted);background:var(--panel);transition:.15s}
nav.tabs a:hover{color:var(--text);border-color:var(--accent);text-decoration:none;transform:translateY(-1px)}
nav.tabs a.active{color:var(--accent2);border-color:var(--accent2);background:transparent}
h2.sec{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent2);
 margin:30px 0 11px;padding-bottom:7px;border-bottom:1px solid var(--line)}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
.panel.intro{padding:16px 18px;margin-bottom:6px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);
 text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);font-weight:600}
td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}
td.mono{font-family:var(--mono);font-size:12.5px;color:var(--muted);white-space:nowrap}
footer{margin-top:40px;border-top:1px solid var(--line);padding-top:16px;font-size:12px;color:var(--muted);font-style:italic}
"""

NAV = ('<nav class="tabs">'
       '<a href="index.html">&#9733; Front Page</a>'
       '<a href="cyber-briefing.html">&#9960; The Cyber Wire</a>'
       '<a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>'
       '<a href="mma-briefing.html">&#8856; The Octagon</a>'
       '<a href="archive.html" class="active">&#128452; Archive</a></nav>')

META = ('<div class="meta"><span class="pill live"><span class="dot"></span>Live</span>'
        '<span class="pill" id="edition">&nbsp;</span><span class="pill" id="datestamp">&nbsp;</span>'
        '<span class="pill">Updated <span id="updated">&nbsp;</span></span></div>')

STAMP = ("<script>(function(){try{var n=new Date();"
 "var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);"
 "var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);"
 "var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);"
 "var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');"
 "document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';"
 "document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');"
 "if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';"
 "}catch(e){}})();</script>")

MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

rows = []
for d in sorted(snaps, reverse=True):
    y, mo, dy = map(int, d.split('-'))
    dt = datetime.date(y, mo, dy)
    rows.append('<h2 class="sec">%s, %s %d, %d</h2><div class="panel"><table>'
                % (DAYS[dt.weekday()], MONTHS[mo - 1], dy, y))
    rows.append('<tr><th>Edition</th><th>Snapshots</th></tr>')
    for t in sorted(snaps[d], reverse=True):
        links = ' &middot; '.join('<a href="archive/%s">%s</a>' % (snaps[d][t][k], SEC[k])
                                  for k in ORDER if k in snaps[d][t])
        rows.append('<tr><td class="mono">%s</td><td>%s</td></tr>' % (h12(t), links))
    rows.append('</table></div>')

nd = len(snaps)
ne = sum(len(v) for v in snaps.values())
ns = sum(len(x) for v in snaps.values() for x in v.values())

body = ('<div class="masthead"><h1>Archive</h1>'
        '<p class="tag">Every past edition of Daily Briefings, exactly as published</p>' + META + '</div>'
        '<div class="freshline" id="freshline">&nbsp;</div>' + NAV +
        '<div class="panel intro"><p style="margin:0">Point-in-time snapshots of every edition. Each file is '
        'exactly as it was published at that timestamp &mdash; figures, countdowns and live widgets were correct as '
        'of then and are <b>not</b> updated afterwards, so an old snapshot may show a deadline that has since '
        'passed or a card that has since been fought. Covering <b>%d days &middot; %d editions &middot; %d '
        'snapshots</b>.</p></div>' % (nd, ne, ns)
        + ''.join(rows)
        + '<footer>Snapshots are historical records and are never edited after publication. For the current '
          'editions, use the tabs above.</footer>')

html = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Archive &mdash; Daily Briefings</title><style>%s</style></head>'
        '<body><div class="wrap">%s</div>%s</body></html>' % (CSS, body, STAMP))

io.open(os.path.join(REPO, 'archive.html'), 'w', encoding='utf-8').write(html)
print("archive.html: %d bytes | %d days / %d editions / %d snapshots" % (len(html.encode('utf-8')), nd, ne, ns))
