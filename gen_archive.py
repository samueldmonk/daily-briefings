import os,re,html
from collections import defaultdict
_BASE=os.path.dirname(os.path.abspath(__file__))
ARCH=os.path.join(_BASE,"archive")
OUT=os.path.join(_BASE,"archive.html")
SEC={"cyber":("The Cyber Wire","cy"),"wallstreet":("The Closing Bell","mk"),"mma":("The Octagon","mm")}
rx=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
data=defaultdict(lambda:defaultdict(dict))
for f in os.listdir(ARCH):
    m=rx.match(f)
    if not m:continue
    sec,y,mo,d,hm=m.groups()
    data[f"{y}-{mo}-{d}"][hm][sec]=f
def t12(hm):
    h=int(hm[:2]);mi=hm[2:];ap="AM" if h<12 else "PM";h12=h%12 or 12
    return f"{h12}:{mi} {ap} ET"
def dhead(ds):
    import datetime
    dt=datetime.date(*map(int,ds.split("-")))
    return dt.strftime("%A, %B %-d, %Y")
dates=sorted(data.keys(),reverse=True)
rows=[]
for ds in dates:
    rows.append(f'<div class="day"><div class="dh">{dhead(ds)}</div><div class="ed">')
    for hm in sorted(data[ds].keys(),reverse=True):
        secs=data[ds][hm]
        links=[]
        for key in ("cyber","wallstreet","mma"):
            if key in secs:
                nm,cl=SEC[key]
                links.append(f'<a class="s {cl}" href="archive/{html.escape(secs[key])}">{nm}</a>')
            else:
                links.append('<span class="s off">—</span>')
        rows.append(f'<div class="row"><span class="tm">{t12(hm)}</span><div class="lk">{"".join(links)}</div></div>')
    rows.append('</div></div>')
body="\n".join(rows)
total=sum(len(v) for v in data.values())
doc=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily Briefings — Archive</title>
<style>
:root{{--bg:#0a0d13;--panel:#12161f;--panel2:#151b26;--line:#232a36;--text:#e6e9ef;--muted:#8a94a6;
--mono:'SF Mono',ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;--teal:#22d3a8;--gold:#e8c766;--orange:#ff8a5c;--up:#3ad07f;}}
*{{box-sizing:border-box}}
body{{margin:0;background:radial-gradient(1200px 600px at 50% -200px,#141a26 0,var(--bg) 60%);color:var(--text);
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.55;padding:26px 18px 60px}}
.wrap{{max-width:1080px;margin:0 auto}}
.masthead{{text-align:center;margin-bottom:14px}}
.masthead h1{{font-size:40px;letter-spacing:.02em;margin:0 0 4px;font-weight:800}}
.masthead .sub{{color:var(--muted);font-family:var(--mono);font-size:12px;letter-spacing:.26em;text-transform:uppercase}}
.meta{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:14px 0 2px}}
.pill{{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-family:var(--mono);
font-size:11px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase}}
.pill.live{{color:var(--up);border-color:#1f5d3f}}
.dot{{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up);margin-right:5px;animation:pulse 1.8s infinite}}
@keyframes pulse{{0%{{box-shadow:0 0 0 0 rgba(58,208,127,.55)}}70%{{box-shadow:0 0 0 7px rgba(58,208,127,0)}}100%{{box-shadow:0 0 0 0 rgba(58,208,127,0)}}}}
.freshline{{text-align:center;color:var(--muted);font-family:var(--mono);font-size:11px;letter-spacing:.04em;margin:10px 0 18px}}
nav.tabs{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 26px}}
nav.tabs a{{display:flex;align-items:center;gap:7px;text-decoration:none;color:var(--muted);background:var(--panel);
border:1px solid var(--line);border-radius:10px;padding:9px 14px;font-size:13.5px;font-weight:600;transition:.15s}}
nav.tabs a:hover{{color:var(--text);border-color:#313a4a;transform:translateY(-1px)}}
nav.tabs a.active{{color:#fff;border-color:#3a4557;background:linear-gradient(180deg,#1a212e,#12161f)}}
.intro{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:10px;
padding:11px 15px;margin:0 0 20px;font-size:14px;color:#d3d8e2}}
.day{{margin-bottom:22px}}
.dh{{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);
margin:0 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}}
.ed{{display:flex;flex-direction:column;gap:7px}}
.row{{display:flex;flex-wrap:wrap;align-items:center;gap:12px;background:var(--panel);border:1px solid var(--line);
border-radius:11px;padding:9px 14px}}
.tm{{font-family:var(--mono);font-size:12px;color:var(--muted);min-width:78px}}
.lk{{display:flex;flex-wrap:wrap;gap:8px}}
.s{{text-decoration:none;font-size:12.5px;font-weight:600;border:1px solid var(--line);border-radius:8px;padding:5px 11px;transition:.15s}}
.s:hover{{transform:translateY(-1px)}}
.s.cy{{color:var(--teal);border-color:#1d4a44}}
.s.mk{{color:var(--gold);border-color:#4a4020}}
.s.mm{{color:var(--orange);border-color:#4a2c22}}
.s.off{{color:#39424f;border-style:dashed;pointer-events:none}}
footer{{max-width:1080px;margin:30px auto 0;color:var(--muted);font-size:12px;text-align:center;line-height:1.7}}
</style>
</head>
<body>
<div class="wrap">
  <div class="masthead">
    <h1>Daily Briefings — Archive</h1>
    <div class="sub">Point-in-time editions</div>
    <div class="meta">
      <span class="pill live"><span class="dot"></span> ARCHIVE</span>
      <span class="pill">{total} editions</span>
      <span class="pill">{len(dates)} days</span>
    </div>
    <div class="freshline">Snapshots are captured every 30 minutes, 8 AM–6 PM ET · each is frozen at its timestamp</div>
  </div>
  <nav class="tabs">
    <a href="index.html">★ <span>Front Page</span></a>
    <a href="cyber-briefing.html">⛨ <span>The Cyber Wire</span></a>
    <a href="wallstreet-briefing.html">▲ <span>The Closing Bell</span></a>
    <a href="mma-briefing.html">⊘ <span>The Octagon</span></a>
    <a href="archive.html" class="active">🗄 <span>Archive</span></a>
  </nav>
  <div class="intro">Each row is one refresh. Links open that edition exactly as it was published — a point-in-time snapshot, not live data. Live widgets are omitted from archived pages.</div>
  {body}
  <footer>Daily Briefings aggregates public reporting for information only. Archived editions are historical snapshots and may contain figures that were later updated.</footer>
</div>
</body>
</html>'''
open(OUT,"w",encoding="utf-8").write(doc)
print("archive.html written:",len(doc),"bytes;",total,"editions across",len(dates),"days")
