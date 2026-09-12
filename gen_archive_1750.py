import os,re,glob
from collections import defaultdict
from datetime import date, timedelta
D="/tmp/db_1789248931"
AR=os.path.join(D,"archive")
SEC={"cyber":("The Cyber Wire","#22d3a8"),"wallstreet":("The Closing Bell","#caa64a"),"mma":("The Octagon","#e84545")}
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})\.html$')

# --- filename-date prune: strictly greater than 21 days
today=date(2026,9,12); cutoff=today-timedelta(days=21); pruned=0
for f in sorted(os.listdir(AR)):
    m=pat.match(f)
    if not m: continue
    d=date(int(m.group(2)),int(m.group(3)),int(m.group(4)))
    if d<cutoff:
        os.remove(os.path.join(AR,f)); pruned+=1

idx=defaultdict(lambda: defaultdict(dict)); files=0
for f in sorted(os.listdir(AR)):
    m=pat.match(f)
    if not m: continue
    files+=1
    sec,Y,Mo,Dy,H,Mi=m.groups()
    idx[f"{Y}-{Mo}-{Dy}"][f"{H}{Mi}"][sec]=f

def pretty_day(k):
    y,m,d=[int(x) for x in k.split("-")]
    return date(y,m,d).strftime("%A, %B %-d, %Y")
def pretty_time(hm):
    h=int(hm[:2]); mi=hm[2:]
    ap="AM" if h<12 else "PM"; hh=h%12 or 12
    return f"{hh}:{mi} {ap} ET"

days=sorted(idx.keys(),reverse=True)
editions=sum(len(v) for v in idx.values())

rows=[]
for dk in days:
    rows.append(f'<h3 class="dayhead">{pretty_day(dk)}</h3>\n<table>\n<tr><th>Edition</th><th>The Cyber Wire</th><th>The Closing Bell</th><th>The Octagon</th></tr>')
    for hm in sorted(idx[dk].keys(),reverse=True):
        cells=[]
        for sec in ("cyber","wallstreet","mma"):
            f=idx[dk][hm].get(sec)
            name,col=SEC[sec]
            cells.append(f'<td><a style="color:{col}" href="archive/{f}">{name}</a></td>' if f else '<td class="na">—</td>')
        rows.append(f'<tr><td class="mono">{pretty_time(hm)}</td>'+"".join(cells)+"</tr>")
    rows.append("</table>")
body="\n".join(rows)

html=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive — Daily Briefings</title>
<style>
:root{{--bg:#0b0d0e;--panel:#141718;--line:#262b2c;--ink:#ecebe6;--mute:#9aa09e;--teal:#22d3a8;--gold:#caa64a;--red:#e84545;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}}
.wrap{{max-width:1040px;margin:0 auto;padding:26px 20px 60px}}
.masthead{{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px;justify-content:space-between}}
h1{{font-family:Georgia,"Times New Roman",serif;font-size:38px;margin:0;letter-spacing:-.015em}}
h1 .ic{{color:var(--mute)}}
.tag-sub{{color:var(--mute);font-size:14px;margin:5px 0 0}}
.meta{{display:flex;flex-wrap:wrap;gap:7px;margin-top:10px}}
.pill{{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 10px;color:var(--mute)}}
.pill.live{{color:var(--teal);border-color:rgba(34,211,168,.4)}}
.pill.live::before{{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--teal);margin-right:6px;vertical-align:middle}}
.freshline{{font-family:var(--mono);font-size:11px;color:var(--mute);margin:12px 2px 16px;letter-spacing:.04em}}
nav.tabs{{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 24px;border-bottom:1px solid var(--line);padding-bottom:14px}}
nav.tabs a{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;color:var(--mute);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:8px 13px;transition:.15s}}
nav.tabs a:hover{{color:var(--ink);border-color:var(--mute)}}
nav.tabs a.active{{color:#0b0d0e;background:var(--ink);border-color:var(--ink);font-weight:700}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 22px}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:13px 15px}}
.stat .n{{font-family:Georgia,serif;font-size:24px;color:var(--ink)}}
.stat .l{{font-size:11.5px;color:var(--mute);line-height:1.45;margin-top:3px}}
.dayhead{{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);margin:26px 0 9px;padding-bottom:7px;border-bottom:1px solid var(--line)}}
table{{width:100%;border-collapse:collapse;margin:0 0 8px;font-size:14px}}
th{{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);text-align:left;padding:7px 9px;border-bottom:1px solid var(--line);font-weight:400}}
td{{padding:8px 9px;border-bottom:1px solid #1c2021;vertical-align:top}}
td a{{text-decoration:none}}
td a:hover{{text-decoration:underline}}
td.mono{{font-family:var(--mono);font-size:12px;color:var(--mute);white-space:nowrap}}
td.na{{color:#4a4f4e}}
.note{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 15px;font-size:13px;color:#c3c8c6;margin:4px 0 22px}}
footer{{margin-top:44px;border-top:1px solid var(--line);padding-top:20px;font-size:12.5px;color:var(--mute)}}
footer h5{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);margin:0 0 9px}}
</style>
</head>
<body>
<div class="wrap">

<div class="masthead">
  <div>
    <h1><span class="ic">&#128452;</span> Archive</h1>
    <p class="tag-sub">Every edition of the three briefings, kept as a point-in-time snapshot</p>
  </div>
  <div class="meta">
    <span class="pill live">Live</span>
    <span class="pill" id="edition">Edition</span>
    <span class="pill" id="datestamp">Date</span>
    <span class="pill">Updated <span id="updated">&mdash;</span></span>
  </div>
</div>

<div class="freshline" id="freshline">Data as of &mdash; ET</div>

<nav class="tabs">
  <a href="index.html">&#9733; Front Page</a>
  <a href="cyber-briefing.html">&#9960; The Cyber Wire</a>
  <a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>
  <a href="mma-briefing.html">&#9216; The Octagon</a>
  <a href="archive.html" class="active">&#128452; Archive</a>
</nav>

<div class="stats">
  <div class="stat"><div class="n">{files}</div><div class="l">snapshots held</div></div>
  <div class="stat"><div class="n">{editions}</div><div class="l">editions, each a set of three briefings</div></div>
  <div class="stat"><div class="n">{len(days)}</div><div class="l">days covered, newest first</div></div>
  <div class="stat"><div class="n">21</div><div class="l">day retention; older snapshots are pruned automatically</div></div>
</div>

<div class="note">Each link opens the briefing <strong>exactly as it was published at that time</strong>, including figures later corrected or retired and refusals later withdrawn. Snapshots are never edited after the fact, so an older edition may contradict a newer one — that is the point of keeping them. Live market widgets are absent from archived pages; only the front page and the three current briefings carry them. This index is regenerated from the snapshot directory on every run rather than maintained by hand.</div>

{body}

<footer>
  <h5>About the archive</h5>
  <p>Briefings are rebuilt from live web research every thirty minutes between 8 AM and 6 PM Eastern, and every edition is snapshotted here before it is replaced. Retention is 21 days by filename date; pruning ran this build and removed <strong>{pruned}</strong> file(s).</p>
</footer>

</div>
<script>(function(){{try{{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}}).format(n);var t=new Intl.DateTimeFormat('en-US',{{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{{timeZone:'America/New_York',hour:'numeric',hour12:false}}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}}catch(e){{}}}})();</script>
</body>
</html>
"""
open(os.path.join(D,"archive.html"),"w",encoding="utf-8").write(html)

# ---- post-generation assertions against the inventory
disk=[f for f in os.listdir(AR) if pat.match(f)]
assert files==len(disk), f"file count {files} != {len(disk)}"
assert html.count('href="archive/')==files, f"links {html.count(chr(34).join(['href=','archive/']))} != {files}"
assert html.count("tradingview")==0, "live widgets in archive"
assert html.count('class="active"')==1 and 'href="archive.html" class="active"' in html
for t in ("index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"):
    assert f'href="{t}"' in html, t
assert html.count("<table>")==html.count("</table>")==len(days)
print(f"OK  days={len(days)} editions={editions} snapshots={files} pruned={pruned}")
