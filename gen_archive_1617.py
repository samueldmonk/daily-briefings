# -*- coding: utf-8 -*-
import os,re,sys,collections
REPO=sys.argv[1]; AD=os.path.join(REPO,"archive")
SEC={"cyber":"The Cyber Wire","wallstreet":"The Closing Bell","mma":"The Octagon"}
ORDER=["cyber","wallstreet","mma"]
files=[f for f in os.listdir(AD) if f.endswith(".html")]
snap=collections.defaultdict(dict)
for f in files:
    m=re.match(r"(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$",f)
    if not m: continue
    snap[(m.group(2),m.group(3))][m.group(1)]=f
days=collections.defaultdict(list)
for (d,hm) in snap: days[d].append(hm)
def pretty(hm):
    h=int(hm[:2]); mi=hm[2:]; ap="AM" if h<12 else "PM"; hh=h%12 or 12
    return "%d:%s %s ET"%(hh,mi,ap)
def dhead(d):
    y,mo,da=[int(x) for x in d.split("-")]
    import datetime
    dt=datetime.date(y,mo,da)
    return dt.strftime("%A, %-d %B %Y")
rows=0; links=0; secs=0
out=[]
for d in sorted(days,reverse=True):
    secs+=1
    out.append('<h2>%s</h2>\n<table>\n<tr><th>Edition</th><th>Snapshots</th></tr>'%dhead(d))
    for hm in sorted(days[d],reverse=True):
        rows+=1
        cells=[]
        for s in ORDER:
            f=snap[(d,hm)].get(s)
            if f:
                links+=1
                cells.append('<a href="archive/%s">%s</a>'%(f,SEC[s]))
        out.append('<tr><td class="mono">%s</td><td>%s</td></tr>'%(pretty(hm)," · ".join(cells)))
    out.append('</table>')
CSS="""<style>
:root{--bg:#0b0d0e;--panel:#141718;--line:#262b2c;--ink:#ecebe6;--mute:#9aa09e;--ac:#9aa09e;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:26px 20px 60px}
.masthead{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px;justify-content:space-between}
h1{font-family:Georgia,"Times New Roman",serif;font-size:38px;margin:0;letter-spacing:-.015em}
.tag-sub{color:var(--mute);font-size:14px;margin:5px 0 0}
.meta{display:flex;flex-wrap:wrap;gap:7px;margin-top:10px}
.pill{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 10px;color:var(--mute)}
.pill.live{color:#22d3a8;border-color:rgba(34,211,168,.4)}
.pill.live::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:#22d3a8;margin-right:6px;vertical-align:middle}
.freshline{font-family:var(--mono);font-size:11px;color:var(--mute);margin:12px 2px 16px;letter-spacing:.04em}
nav.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 24px;border-bottom:1px solid var(--line);padding-bottom:14px}
nav.tabs a{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;color:var(--mute);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:8px 13px;transition:.15s}
nav.tabs a:hover{color:var(--ink);border-color:var(--mute)}
nav.tabs a.active{color:#0b0d0e;background:var(--ink);border-color:var(--ink);font-weight:700}
h2{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--mute);margin:30px 0 10px;padding-bottom:8px;border-bottom:1px solid var(--line)}
table{width:100%;border-collapse:collapse;background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-bottom:8px}
th{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);text-align:left;padding:10px 14px;border-bottom:1px solid var(--line)}
td{padding:10px 14px;border-bottom:1px solid var(--line);font-size:14px;vertical-align:top}
tr:last-child td{border-bottom:none}
td.mono{font-family:var(--mono);font-size:12.5px;color:var(--mute);white-space:nowrap}
td a{color:#ecebe6;text-decoration:none;border-bottom:1px solid var(--line)}
td a:hover{color:#22d3a8;border-bottom-color:#22d3a8}
.note{font-size:12.5px;color:var(--mute);margin:10px 2px 0}
footer{margin-top:44px;border-top:1px solid var(--line);padding-top:20px;font-size:12.5px;color:var(--mute)}
.disc{margin-top:12px;font-size:11.5px;color:#767b79;line-height:1.6}
</style>"""
NAV="""<nav class="tabs">
  <a href="index.html">&#9733; Front Page</a>
  <a href="cyber-briefing.html">&#9960; The Cyber Wire</a>
  <a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>
  <a href="mma-briefing.html">&#8856; The Octagon</a>
  <a href="archive.html" class="active">&#128452; Archive</a>
</nav>"""
STAMP="""<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>"""
html=u"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive &mdash; Daily Briefings</title>
%s
</head>
<body>
<div class="wrap">

<div class="masthead">
  <div>
    <h1>&#128452; Archive</h1>
    <p class="tag-sub">Point-in-time snapshots of every edition, newest first</p>
  </div>
  <div class="meta">
    <span class="pill live">Live</span>
    <span class="pill" id="edition">Edition</span>
    <span class="pill" id="datestamp">Date</span>
    <span class="pill">Updated <span id="updated">&mdash;</span></span>
  </div>
</div>

<div class="freshline" id="freshline">Data as of &mdash; ET</div>

%s

<div class="note">%d editions across %d days, %d snapshots in total. Each link opens the page exactly as it was published at that time &mdash; figures, countdowns and &ldquo;live&rdquo; wording are frozen at the moment of the snapshot and are not updated afterwards. Any streaming widget inside an archived page will still show current data, because it is fetched by your browser rather than stored.</div>

%s

<footer>
  <p>Generated from the snapshot directory on every run, never hand-curated. Snapshots older than 21 days are pruned by filename date.</p>
  <p class="disc">Archived pages are historical records. Do not read an old markets snapshot as a current quote, an old security snapshot as a current deadline, or an old fight card as a current result.</p>
</footer>

</div>
%s
</body>
</html>
"""%(CSS,NAV,rows,secs,links,"\n".join(out),STAMP)
open(os.path.join(REPO,"archive.html"),"w").write(html)
assert secs==len(days), "day sections"
assert rows==len(snap), "rows"
assert links==len(files), "links %d vs %d"%(links,len(files))
assert html.count('class="active"')==1 and html.count('nav.tabs a')>0
assert len(re.findall(r'<a href="(index|cyber-briefing|wallstreet-briefing|mma-briefing|archive)\.html"',html))==5
print("archive.html: %d day sections, %d edition rows, %d snapshot links"%(secs,rows,links))
