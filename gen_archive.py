# -*- coding: utf-8 -*-
"""Self-contained: regenerates archive.html from the snapshots in archive/."""
import os,re,io,collections,datetime,sys

REPO=os.path.dirname(os.path.abspath(__file__))
ARCH=os.path.join(REPO,'archive')
SECT={'cyber':('The Cyber Wire','#22d3a8'),
      'wallstreet':('The Closing Bell','#caa64a'),
      'mma':('The Octagon','#e84545')}
PAT=re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')

eds=collections.defaultdict(dict)   # (date,hhmm) -> {section: filename}
for fn in sorted(os.listdir(ARCH)):
    m=PAT.match(fn)
    if not m: continue
    sec,date,hhmm=m.groups()
    eds[(date,hhmm)][sec]=fn

def pretty_time(hhmm):
    h=int(hhmm[:2]); mi=hhmm[2:]
    ap='AM' if h<12 else 'PM'; hh=h%12
    if hh==0: hh=12
    return '%d:%s %s ET'%(hh,mi,ap)

def pretty_date(d):
    return datetime.date.fromisoformat(d).strftime('%A, %B %-d, %Y')

CSS="""<style>
:root{--bg:#0b0b0d;--panel:#151519;--line:#26262c;--accent:#c9ccd1;--accent2:#e8c766;--ink:#e8e6e3;--mut:#9aa0a6;--mono:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:26px 20px 70px}
.mast{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px;margin-bottom:8px}
.mast h1{margin:0;font-size:34px;letter-spacing:-.5px}
.mast .tag{color:var(--mut);font-size:14.5px}
.meta{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0 4px}
.pill{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 11px}
.pill.live{color:#22c55e;border-color:rgba(34,197,94,.4)}
.pill.live .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#22c55e;margin-right:6px;vertical-align:middle;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
.freshline{font-family:var(--mono);font-size:11px;color:var(--mut);margin:8px 2px 14px;letter-spacing:.04em}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 20px;border-bottom:1px solid var(--line);padding-bottom:14px}
nav a{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;color:var(--mut);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:8px 13px;transition:.15s}
nav a:hover{color:var(--ink);border-color:var(--accent);transform:translateY(-1px)}
nav a.on{color:var(--accent);border-color:var(--accent);background:rgba(255,255,255,.03)}
h2.day{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent2);margin:32px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px;margin-bottom:16px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);text-align:left;padding:9px 10px;border-bottom:1px solid var(--line)}
td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}
td.tm{font-family:var(--mono);white-space:nowrap;color:var(--mut);width:130px}
a.snap{text-decoration:none;font-size:13.5px;margin-right:14px;white-space:nowrap}
a.snap:hover{text-decoration:underline}
.miss{color:#5c6066;font-size:13.5px;margin-right:14px;white-space:nowrap}
.note{font-size:12.5px;color:var(--mut);margin:10px 0 20px;line-height:1.55}
footer{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);font-size:12.5px;color:var(--mut)}
</style>"""

o=['<!doctype html><html lang="en"><head><meta charset="utf-8">',
   '<meta name="viewport" content="width=device-width,initial-scale=1">',
   '<title>Archive &mdash; Daily Briefings</title>',CSS,'</head><body><div class="wrap">',
   '<div class="mast"><h1>Archive</h1><span class="tag">Point-in-time snapshots of every published edition</span></div>',
   '<div class="meta"><span class="pill live"><span class="dot"></span>Live</span>',
   '<span class="pill" id="edition"></span><span class="pill" id="datestamp"></span>',
   '<span class="pill">Updated <span id="updated"></span></span></div>',
   '<div class="freshline" id="freshline"></div>',
   '<nav>',
   '<a href="index.html">&#9733; Front Page</a>',
   '<a href="cyber-briefing.html">&#9960; The Cyber Wire</a>',
   '<a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>',
   '<a href="mma-briefing.html">&#8856; The Octagon</a>',
   '<a class="on" href="archive.html">&#128452; Archive</a>',
   '</nav>']

days=sorted({d for d,_ in eds}, reverse=True)
n_ed=len(eds); n_snap=sum(len(v) for v in eds.values())
o.append('<div class="note">These are frozen copies of each edition exactly as it was published. '
         'They are <b>point-in-time</b>: live widgets, countdowns and market quotes inside a snapshot '
         'reflect the moment it was archived, not now. Currently holding <b>%d editions</b> across '
         '<b>%d snapshots</b> over <b>%d days</b>.</div>'%(n_ed,n_snap,len(days)))

broken=0
for d in days:
    o.append('<h2 class="day">%s</h2>'%pretty_date(d))
    o.append('<div class="panel"><table><thead><tr><th>Edition</th><th>Snapshots</th></tr></thead><tbody>')
    times=sorted({t for dd,t in eds if dd==d}, reverse=True)
    for t in times:
        secs=eds[(d,t)]
        cells=[]
        for key in ('cyber','wallstreet','mma'):
            label,col=SECT[key]
            if key in secs:
                href='archive/'+secs[key]
                if not os.path.exists(os.path.join(REPO,href)): broken+=1
                cells.append('<a class="snap" style="color:%s" href="%s">%s</a>'%(col,href,label))
            else:
                cells.append('<span class="miss">%s &mdash;</span>'%label)
        o.append('<tr><td class="tm">%s</td><td>%s</td></tr>'%(pretty_time(t),''.join(cells)))
    o.append('</tbody></table></div>')

o.append('<footer>Snapshots are pruned after 21 days. Regenerated automatically on every publish &mdash; '
         'this page is never hand-edited.</footer></div>')
o.append("""<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>""")
o.append('</body></html>')

html=''.join(o)
io.open(os.path.join(REPO,'archive.html'),'w',encoding='utf-8').write(html)
print('archive.html: %d bytes | %d days | %d editions | %d snapshots | %d broken hrefs'
      %(len(html),len(days),n_ed,n_snap,broken))
