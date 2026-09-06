# -*- coding: utf-8 -*-
"""Self-contained archive index generator. Idempotent."""
import os, re, sys, datetime, collections
REPO = sys.argv[1]
ARC = os.path.join(REPO, "archive")
SEC = {"cyber": ("The Cyber Wire", "#22d3a8"),
       "wallstreet": ("The Closing Bell", "#caa64a"),
       "mma": ("The Octagon", "#e84545")}
PAT = re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')

# --- filename-date prune (>21 days). mtimes are useless on a fresh clone. ---
today = datetime.date.today()
pruned = 0
files = []
for fn in sorted(os.listdir(ARC)):
    m = PAT.match(fn)
    if not m:
        continue
    d = datetime.date(int(m.group(2)), int(m.group(3)), int(m.group(4)))
    if (today - d).days > 21:
        os.remove(os.path.join(ARC, fn)); pruned += 1; continue
    files.append((d, m.group(5), m.group(1), fn))

editions = collections.defaultdict(dict)   # (date, hhmm) -> {section: filename}
for d, hhmm, sec, fn in files:
    editions[(d, hhmm)][sec] = fn

bydate = collections.defaultdict(list)
for (d, hhmm) in editions:
    bydate[d].append(hhmm)

def ampm(hhmm):
    h, mi = int(hhmm[:2]), hhmm[2:]
    suf = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    return f"{h12}:{mi} {suf} ET"

CSS = """
:root{--bg:#0c0c0e;--panel:#161619;--line:#28282d;--txt:#e9e6e2;--muted:#9aa0a6;--accent:#9aa0a6;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:15.5px;line-height:1.62}
.wrap{max-width:1000px;margin:0 auto;padding:26px 20px 70px}
a{color:#c9c4be;text-decoration:none}a:hover{text-decoration:underline}
.masthead{border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:14px}
.masthead h1{margin:0 0 4px;font-size:34px;letter-spacing:-.5px}
.masthead .sub{color:var(--muted);font-size:14px;margin:0}
.meta{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}
.pill{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 11px;color:var(--muted)}
.pill.live{color:#22c55e;border-color:rgba(34,197,94,.35)}
.pill.live .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#22c55e;margin-right:6px;vertical-align:middle}
nav.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 20px}
nav.tabs a{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:8px 13px;color:var(--muted);transition:.15s}
nav.tabs a:hover{color:var(--txt);border-color:var(--accent);text-decoration:none;transform:translateY(-1px)}
nav.tabs a.active{color:#e9e6e2;border-color:#e9e6e2;background:rgba(255,255,255,.03)}
.freshline{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;color:var(--muted);margin:9px 0 2px}
h2.day{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:#c9c4be;margin:32px 0 11px;padding-bottom:7px;border-bottom:1px solid var(--line)}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 16px;margin-bottom:14px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);text-align:left;padding:9px 8px;border-bottom:1px solid var(--line)}
td{padding:10px 8px;border-bottom:1px solid var(--line)}
tr:last-child td{border-bottom:none}
td.tm{font-family:var(--mono);color:var(--muted);white-space:nowrap;width:130px}
.lnk{display:inline-block;margin-right:14px}
.mut{color:var(--muted)}
.disc{font-size:12px;color:var(--muted);border-top:1px solid var(--line);margin-top:26px;padding-top:14px}
@media(max-width:640px){.masthead h1{font-size:26px}.wrap{padding:18px 14px 50px}td.tm{width:auto}}
"""
TABS = [("index.html","★ Front Page",0),("cyber-briefing.html","⛨ The Cyber Wire",0),
        ("wallstreet-briefing.html","▲ The Closing Bell",0),("mma-briefing.html","⊘ The Octagon",0),
        ("archive.html","\U0001f5c4 Archive",1)]
STAMP = """<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>"""

o = []
a = o.append
a('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">')
a('<meta name="viewport" content="width=device-width,initial-scale=1">')
a('<title>Archive — Daily Briefings</title>')
a(f'<style>{CSS}</style></head><body><div class="wrap">')
a('<header class="masthead"><h1>Archive</h1>')
a('<p class="sub">Every edition published, newest first — point-in-time snapshots</p>')
a('<div class="meta"><span class="pill live"><span class="dot"></span>Live</span>'
  '<span class="pill" id="edition">&nbsp;</span><span class="pill" id="datestamp">&nbsp;</span>'
  '<span class="pill">Updated <span id="updated">&nbsp;</span></span></div></header>')
a('<div class="freshline" id="freshline">&nbsp;</div>')
a('<nav class="tabs">')
for href, label, act in TABS:
    cls = ' class="active"' if act else ''
    a('<a href="%s"%s>%s</a>' % (href, cls, label))
a('</nav>')

ndays = len(bydate); neds = len(editions); nsnaps = len(files); nbroken = 0
a(f'<div class="panel" style="padding:14px 16px"><p style="margin:0;font-size:14px">'
  f'<strong>{neds}</strong> editions across <strong>{ndays}</strong> days, '
  f'<strong>{nsnaps}</strong> snapshots. Each link opens the page exactly as it was published at that '
  f'time — figures, countdowns and “new” tags are frozen at that moment and are '
  f'<em>not</em> updated. Snapshots older than 21 days are pruned automatically. There are no live '
  f'widgets on this page.</p></div>')

for d in sorted(bydate, reverse=True):
    a(f'<h2 class="day">{d.strftime("%A, %B %-d, %Y")}</h2>')
    a('<div class="panel"><table>')
    a('<tr><th>Edition</th><th>Snapshots</th></tr>')
    for hhmm in sorted(bydate[d], reverse=True):
        secs = editions[(d, hhmm)]
        links = []
        for key in ("cyber", "wallstreet", "mma"):
            if key in secs:
                name, col = SEC[key]
                fn = secs[key]
                p = os.path.join(ARC, fn)
                if not os.path.exists(p):
                    nbroken += 1
                links.append(f'<a class="lnk" style="color:{col}" href="archive/{fn}">{name}</a>')
            else:
                links.append(f'<span class="lnk mut">{SEC[key][0]} —</span>')
        a(f'<tr><td class="tm">{ampm(hhmm)}</td><td>{"".join(links)}</td></tr>')
    a('</table></div>')

a('<div class="disc">Snapshots are point-in-time captures. A market level, a KEV countdown or a fight '
  'card in an old edition was correct when published and may have been superseded since — always read the '
  'current briefings for live figures. Nothing here is investment, legal or security advice.</div>')
a('</div>')
a(STAMP)
a('</body></html>')

html = "\n".join(o)
open(os.path.join(REPO, "archive.html"), "w", encoding="utf-8").write(html)
print(f"archive.html {len(html)} bytes | {ndays} days | {neds} editions | {nsnaps} snapshots | "
      f"pruned {pruned} | broken hrefs {nbroken}")
