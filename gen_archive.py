import os, re, datetime, html
ARC="archive"
SEC={"cyber":("The Cyber Wire","#22d3a8"),"wallstreet":("The Closing Bell","#caa64a"),"mma":("The Octagon","#e84545")}
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
data={}  # date(str) -> { hhmm -> {sec->filename} }
files=os.listdir(ARC) if os.path.isdir(ARC) else []
for f in files:
    m=pat.match(f)
    if not m: continue
    sec,y,mo,d,hm=m.groups()
    dk=f"{y}-{mo}-{d}"
    data.setdefault(dk,{}).setdefault(hm,{})[sec]=f
def t12(hm):
    h=int(hm[:2]); mi=hm[2:]
    ap="AM" if h<12 else "PM"
    hh=h%12
    if hh==0: hh=12
    return f"{hh}:{mi} {ap} ET"
WD=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MO=["January","February","March","April","May","June","July","August","September","October","November","December"]
dates=sorted(data.keys(), reverse=True)
total_editions=sum(len(data[dk]) for dk in dates)
total_snaps=sum(len(secs) for dk in dates for secs in data[dk].values())
total_days=len(dates)
rows_html=[]
for dk in dates:
    y,mo,d=[int(x) for x in dk.split("-")]
    dt=datetime.date(y,mo,d)
    head=f"{WD[dt.weekday()]}, {MO[mo-1]} {d}, {y}"
    nED=len(data[dk])
    sec_block=f'<section class="day"><div class="dayhead">{head} <span class="dcount">{nED} edition{"s" if nED!=1 else ""}</span></div><div class="panel" style="padding:4px 14px"><table><tr><th>Time</th><th>Snapshots</th></tr>'
    for hm in sorted(data[dk].keys(), reverse=True):
        secs=data[dk][hm]
        cells=""
        for key in ("cyber","wallstreet","mma"):
            label,color=SEC[key]
            if key in secs:
                cells+=f'<a class="slink" style="--c:{color}" href="{ARC}/{secs[key]}">{label}</a>'
            else:
                cells+='<span class="smiss">—</span>'
        sec_block+=f'<tr><td class="ts">{t12(hm)}</td><td class="lk">{cells}</td></tr>'
    sec_block+='</table></div></section>'
    rows_html.append(sec_block)
sub=f"Point-in-time snapshots of every edition · {total_editions} editions · {total_snaps} snapshots · {total_days} days"
HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Archive · Daily Briefings</title>
<style>
:root{{
  --bg:#080a0e; --panel:#10151b; --line:#1f2730; --ink:#eef3f6; --mut:#8fa1ad;
  --teal:#22d3a8; --gold:#caa64a; --red:#e84545;
  --mono:ui-monospace,'SF Mono','Cascadia Code',Menlo,Consolas,monospace;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:radial-gradient(1200px 640px at 50% -12%,#121a22 0,var(--bg) 60%);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1080px;margin:0 auto;padding:30px 20px 60px}}
a{{color:inherit;text-decoration:none}}
.masthead{{text-align:center;border-bottom:1px solid var(--line);padding-bottom:20px}}
.brand{{font-size:13px;font-family:var(--mono);letter-spacing:.4em;color:var(--mut);text-transform:uppercase}}
.title{{font-size:40px;font-weight:800;letter-spacing:.01em;margin:8px 0 0;
  background:linear-gradient(90deg,var(--teal),var(--gold),var(--red));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.sub{{font-size:14px;color:var(--mut);margin-top:8px}}
.meta{{margin:14px 0 0;display:flex;gap:7px;flex-wrap:wrap;justify-content:center}}
.pill{{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);
  border:1px solid var(--line);border-radius:999px;padding:4px 11px;background:var(--panel)}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 6px;justify-content:center}}
nav a{{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--mut);
  border:1px solid var(--line);border-radius:9px;padding:8px 13px;background:var(--panel);transition:.15s}}
nav a:hover{{transform:translateY(-1px);color:var(--ink);border-color:#2c3a45}}
nav a.active{{color:#06231c;background:var(--teal);border-color:var(--teal);font-weight:700}}
.day{{margin-top:26px}}
.dayhead{{font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);
  margin-bottom:10px;border-left:3px solid var(--teal);padding-left:10px}}
.dcount{{color:var(--mut);font-size:11px;letter-spacing:.1em;margin-left:8px}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:14px}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}
th,td{{text-align:left;padding:10px 10px;border-bottom:1px solid var(--line)}}
th{{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}}
tr:last-child td{{border-bottom:none}}
td.ts{{font-family:var(--mono);color:var(--mut);white-space:nowrap;width:150px}}
td.lk{{display:flex;gap:8px;flex-wrap:wrap}}
.slink{{font-family:var(--mono);font-size:12px;border:1px solid var(--line);border-left:3px solid var(--c);
  border-radius:8px;padding:5px 10px;color:var(--ink);background:#0c1219;transition:.15s}}
.slink:hover{{transform:translateY(-1px);border-color:var(--c)}}
.smiss{{font-family:var(--mono);font-size:12px;color:#3a4650;padding:5px 10px}}
.foot{{margin-top:34px;border-top:1px solid var(--line);padding-top:16px;font-size:12px;color:var(--mut);text-align:center}}
.disc{{margin-top:8px;font-size:11.5px;color:#5d6b74;font-style:italic}}
@media(max-width:640px){{td.ts{{width:auto}}}}
</style>
</head>
<body>
<div class="wrap">
  <div class="masthead">
    <div class="brand">Daily Briefings</div>
    <div class="title">Archive</div>
    <div class="sub">{sub}</div>
    <div class="meta">
      <span class="pill">Snapshots are point-in-time — not live</span>
    </div>
  </div>

  <nav>
    <a href="index.html">★ Front Page</a>
    <a href="cyber-briefing.html">⛨ The Cyber Wire</a>
    <a href="wallstreet-briefing.html">▲ The Closing Bell</a>
    <a href="mma-briefing.html">⊘ The Octagon</a>
    <a href="archive.html" class="active">🗄 Archive</a>
  </nav>

{chr(10).join(rows_html)}

  <div class="foot">
    Each link opens that desk's briefing exactly as it was published at that time. Snapshots are frozen point-in-time captures — figures, odds, and deadlines were current as of the timestamp shown and are <b>not</b> live. For the current edition, use the tabs above.
    <div class="disc">Snapshots older than 21 days are pruned automatically. Generated by script — never hand-curated.</div>
  </div>
</div>
</body>
</html>'''
open("archive.html","w").write(HTML)
print("WROTE archive.html")
print(f"editions={total_editions} snapshots={total_snaps} days={total_days}")
