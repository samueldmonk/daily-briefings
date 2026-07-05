import os, re, glob, html
from datetime import datetime
root="."
files=glob.glob(os.path.join(root,"archive","*.html"))
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})\.html$')
secmap={"cyber":("The Cyber Wire","#22d3a8"),"wallstreet":("The Closing Bell","#e8c766"),"mma":("The Octagon","#ff6a4d")}
data={}  # date -> hhmm -> {section:filename}
for f in files:
    b=os.path.basename(f); m=pat.match(b)
    if not m: continue
    sec,Y,Mo,D2,H,Mi=m.groups()
    date=f"{Y}-{Mo}-{D2}"; hhmm=H+Mi
    data.setdefault(date,{}).setdefault(hhmm,{})[sec]=b
def fmt_time(hhmm):
    h=int(hhmm[:2]); mi=hhmm[2:]; ap="AM" if h<12 else "PM"; h12=h%12 or 12
    return f"{h12}:{mi} {ap} ET"
def fmt_date(d):
    return datetime.strptime(d,"%Y-%m-%d").strftime("%A, %B %-d, %Y")
dates=sorted(data.keys(),reverse=True)
rows=[]
for d in dates:
    rows.append(f'<div class="dayhead">{fmt_date(d)}</div>')
    rows.append('<div class="daypanel">')
    for hhmm in sorted(data[d].keys(),reverse=True):
        secs=data[d][hhmm]
        links=[]
        for sec in ("cyber","wallstreet","mma"):
            if sec in secs:
                nm,col=secmap[sec]
                links.append(f'<a class="slink" style="color:{col};border-color:{col}55" href="archive/{secs[sec]}">{nm}</a>')
            else:
                nm,col=secmap[sec]
                links.append(f'<span class="slink off">{nm}</span>')
        rows.append(f'<div class="trow"><span class="ttime">{fmt_time(hhmm)}</span><span class="tlinks">{"".join(links)}</span></div>')
    rows.append('</div>')
body="\n".join(rows)
total=sum(len(v) for v in data.values())
tpl=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive — Daily Briefings</title>
<style>
:root{{--bg:#0a0b0d;--panel:#14161a;--line:#252a31;--text:#e9edf2;--muted:#8b95a3;--mono:'SF Mono',ui-monospace,Menlo,Consolas,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:radial-gradient(1200px 520px at 50% -240px,#161a20 0,var(--bg) 60%);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.55}}
.wrap{{max-width:1000px;margin:0 auto;padding:24px 18px 60px}}
.masthead{{text-align:center;padding:10px 0 2px}}
.masthead h1{{font-family:Georgia,serif;font-size:34px;margin:0}}
.masthead .sub{{color:var(--muted);font-family:var(--mono);font-size:11px;letter-spacing:.24em;text-transform:uppercase;margin-top:8px}}
nav.tabs{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:16px 0 22px}}
.tab{{font-family:var(--mono);font-size:12.5px;text-decoration:none;color:var(--muted);background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:9px 13px;transition:.15s}}
.tab:hover{{color:var(--text);transform:translateY(-1px)}}
.tab.active{{color:var(--text);border-color:#3a424d}}
.note{{color:var(--muted);font-size:12px;font-style:italic;text-align:center;margin-bottom:20px}}
.dayhead{{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:22px 0 8px}}
.daypanel{{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
.trow{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:11px 15px;border-bottom:1px solid var(--line)}}
.trow:last-child{{border-bottom:0}}
.ttime{{font-family:var(--mono);font-size:12.5px;color:var(--text);min-width:92px}}
.tlinks{{display:flex;flex-wrap:wrap;gap:8px}}
.slink{{font-family:var(--mono);font-size:11.5px;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:4px 9px;transition:.15s}}
.slink:hover{{transform:translateY(-1px)}}
.slink.off{{color:#4d545e;border-color:var(--line);opacity:.5}}
.foot{{margin-top:28px;color:var(--muted);font-size:12px;text-align:center}}
</style></head>
<body><div class="wrap">
<div class="masthead"><h1>🗄 Archive</h1><div class="sub">Point-in-time briefing snapshots</div></div>
<nav class="tabs">
<a href="index.html" class="tab">★ Front Page</a>
<a href="cyber-briefing.html" class="tab">⛨ The Cyber Wire</a>
<a href="wallstreet-briefing.html" class="tab">▲ The Closing Bell</a>
<a href="mma-briefing.html" class="tab">⊘ The Octagon</a>
<a href="archive.html" class="tab active">🗄 Archive</a>
</nav>
<div class="note">Each snapshot is a point-in-time capture of a briefing as it was published; live widgets and countdowns are not preserved. {total} editions across {len(dates)} days.</div>
{body}
<div class="foot">Snapshots are retained for 21 days.</div>
</div></body></html>'''
open(os.path.join(root,"archive.html"),"w").write(tpl)
print("archive.html written:",os.path.getsize(os.path.join(root,"archive.html")),"bytes;",total,"editions across",len(dates),"days")
