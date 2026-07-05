import os,re,collections,datetime,sys
D=sys.argv[1]
adir=os.path.join('/tmp',D,'archive')
files=os.listdir(adir)
SEC={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
ORDER=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})\.html$')
data=collections.defaultdict(lambda:collections.defaultdict(dict))
nmatch=0
for fn in files:
    m=pat.match(fn)
    if not m: continue
    nmatch+=1
    sec,y,mo,d,hh,mm=m.groups()
    data[(int(y),int(mo),int(d))][(int(hh),int(mm))][sec]=fn
print("files in dir:",len(files),"| matched:",nmatch)
def h12(hh,mm):
    ap='AM' if hh<12 else 'PM'; h=hh%12; h=12 if h==0 else h
    return f"{h}:{mm:02d} {ap} ET"
days=sorted(data.keys(),reverse=True)
rows=[]; total=0
for dk in days:
    y,mo,d=dk
    hdr=datetime.date(y,mo,d).strftime('%A, %B %d, %Y').replace(' 0',' ')
    rows.append(f'<div class="daysec"><div class="dayhdr">{hdr}</div><div class="tbl">')
    rows.append('<div class="hrow"><span class="ht">Time</span><span class="hl">Editions</span></div>')
    for tk in sorted(data[dk].keys(),reverse=True):
        total+=1; hh,mm=tk; links=[]
        for sec in ORDER:
            if sec in data[dk][tk]:
                links.append(f'<a href="archive/{data[dk][tk][sec]}">{SEC[sec]}</a>')
            else:
                links.append(f'<span class="na">{SEC[sec]}</span>')
        rows.append(f'<div class="row"><span class="tm">{h12(hh,mm)}</span><span class="lk">{" · ".join(links)}</span></div>')
    rows.append('</div></div>')
body="\n".join(rows); ndays=len(days)
T='{'; E='}'
htmlout=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archive — Daily Briefings</title>
<style>
:root{T}--bg:#0a0d12;--panel:#141922;--panel2:#10151d;--line:#232c39;--text:#e7ebf2;--muted:#8a94a6;
--mono:'SF Mono',ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;--teal:#22d3a8;--gold2:#e8c766;--orange:#ff8a5c;--front:#8ab4f8;--up:#22c55e;{E}
*{T}box-sizing:border-box{E}
body{T}margin:0;background:radial-gradient(1200px 600px at 50% -200px,#121826 0,var(--bg) 60%);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased{E}
.wrap{T}max-width:1000px;margin:0 auto;padding:26px 20px 60px{E}
.masthead{T}text-align:center;padding:14px 0 6px{E}
.masthead h1{T}font-family:Georgia,'Times New Roman',serif;font-size:38px;letter-spacing:.5px;margin:0;background:linear-gradient(90deg,var(--teal),var(--gold2),var(--orange));-webkit-background-clip:text;background-clip:text;color:transparent{E}
.masthead .sub{T}color:var(--muted);font-family:var(--mono);font-size:11px;letter-spacing:.26em;text-transform:uppercase;margin-top:7px{E}
.meta{T}display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:13px 0 4px{E}
.pill{T}font-family:var(--mono);font-size:11px;letter-spacing:.09em;color:var(--muted);background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:5px 11px;text-transform:uppercase{E}
.pill.live{T}color:#0a0d12;background:var(--up);border-color:transparent;font-weight:700;display:inline-flex;align-items:center;gap:6px{E}
.pill.live .dot{T}width:7px;height:7px;border-radius:50%;background:#0a0d12;animation:pulse 1.6s infinite{E}
@keyframes pulse{T}0%,100%{T}opacity:1{E}50%{T}opacity:.3{E}{E}
.freshline{T}text-align:center;color:var(--muted);font-family:var(--mono);font-size:11.5px;margin:2px 0 14px{E}
nav.tabs{T}display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:12px 0 22px{E}
.tab{T}font-family:var(--mono);font-size:12.5px;text-decoration:none;color:var(--muted);background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:9px 14px;transition:.15s{E}
.tab:hover{T}color:var(--text);transform:translateY(-1px){E}
.tab.active{T}color:var(--front);border-color:var(--front){E}
.note{T}color:var(--muted);font-size:12px;font-style:italic;text-align:center;margin:0 0 22px{E}
.daysec{T}margin:0 0 22px{E}
.dayhdr{T}font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold2);margin:0 0 9px;padding-bottom:6px;border-bottom:1px solid var(--line){E}
.tbl{T}background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden{E}
.hrow,.row{T}display:grid;grid-template-columns:130px 1fr;gap:10px;padding:9px 14px;align-items:center{E}
.hrow{T}background:var(--panel2);border-bottom:1px solid var(--line){E}
.ht,.hl{T}font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted){E}
.row{T}border-bottom:1px solid var(--line);font-size:13.5px{E}
.row:last-child{T}border-bottom:0{E}
.tm{T}font-family:var(--mono);font-size:12.5px;color:var(--text){E}
.lk a{T}color:#8ab4f8;text-decoration:none;font-size:13px{E}
.lk a:hover{T}text-decoration:underline{E}
.lk .na{T}color:#4a5262;font-size:13px{E}
.foot{T}margin-top:30px;color:var(--muted);font-size:12px;text-align:center;line-height:1.7{E}
</style>
</head>
<body>
<div class="wrap">
  <div class="masthead">
    <h1>Daily Briefings — Archive</h1>
    <div class="sub">Point-in-time editions · Cyber · Markets · MMA</div>
    <div class="meta">
      <span class="pill live"><span class="dot"></span> LIVE</span>
      <span class="pill" id="edition">Morning Edition</span>
      <span class="pill" id="datestamp">—</span>
      <span class="pill">Updated <span id="updated">—</span></span>
    </div>
    <div class="freshline" id="freshline">Data as of — ET · briefings refresh every 30 minutes, 8 AM–6 PM ET</div>
  </div>
  <nav class="tabs">
    <a href="index.html" class="tab">★ Front Page</a>
    <a href="cyber-briefing.html" class="tab">⛨ The Cyber Wire</a>
    <a href="wallstreet-briefing.html" class="tab">▲ The Closing Bell</a>
    <a href="mma-briefing.html" class="tab">⊘ The Octagon</a>
    <a href="archive.html" class="tab active">🗄 Archive</a>
  </nav>
  <div class="note">Every 30-minute edition is snapshotted here as a static, point-in-time page (live widgets are disabled in archived copies). {total} editions across {ndays} days.</div>
  {body}
  <div class="foot">Archived snapshots reflect the data verified at that timestamp and are not updated afterward. Snapshots older than 21 days are pruned automatically.</div>
</div>
<script>(function(){T}try{T}var n=new Date();var et=new Intl.DateTimeFormat('en-US',{T}timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'{E}).format(n);var t=new Intl.DateTimeFormat('en-US',{T}timeZone:'America/New_York',hour:'numeric',minute:'2-digit'{E}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{T}timeZone:'America/New_York',hour:'numeric',hour12:false{E}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET · briefings refresh every 30 minutes, 8 AM–6 PM ET';{E}catch(e){T}{E}{E})();</script>
</body>
</html>'''
open(os.path.join('/tmp',D,'archive.html'),'w',encoding='utf-8').write(htmlout)
print("archive.html written:",total,"editions,",ndays,"days")
