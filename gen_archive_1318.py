# -*- coding: utf-8 -*-
# Builds archive.html ENTIRELY FROM SCRATCH from the contents of archive/.
# There is no head to retain, so there is no splice boundary that can drift.
import os,re,collections
ROOT=os.path.dirname(os.path.abspath(__file__)); AD=os.path.join(ROOT,'archive')
SEC={'cyber':('The Cyber Wire','#22d3a8'),'wallstreet':('The Closing Bell','#caa64a'),'mma':('The Octagon','#e84545')}
PAT=re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')
MON=['January','February','March','April','May','June','July','August','September','October','November','December']

files=sorted(f for f in os.listdir(AD) if f.endswith('.html'))
data=collections.defaultdict(lambda: collections.defaultdict(dict)); parsed=0
for f in files:
    m=PAT.match(f)
    assert m, "UNPARSED FILE IN archive/: %s"%f      # an unparsed file would otherwise vanish silently
    sec,d,hm=m.groups(); data[d][hm][sec]=f; parsed+=1
assert parsed==len(files), "parsed %d of %d"%(parsed,len(files))

def pretty_date(d):
    y,mo,dd=d.split('-'); return "%s %d, %s"%(MON[int(mo)-1],int(dd),y)
def pretty_time(hm):
    h=int(hm[:2]); mi=hm[2:]; ap='AM' if h<12 else 'PM'; h12=h%12 or 12
    return "%d:%s %s ET"%(h12,mi,ap)

rows=0
body=[]
for d in sorted(data,reverse=True):
    body.append('<h2 class="day">%s</h2>\n<table>\n<tr><th>Edition</th><th>Snapshots</th></tr>'%pretty_date(d))
    for hm in sorted(data[d],reverse=True):
        links=[]
        for sec in ('cyber','wallstreet','mma'):
            f=data[d][hm].get(sec)
            if f:
                name,col=SEC[sec]
                links.append('<a href="archive/%s" style="color:%s">%s</a>'%(f,col,name))
        body.append('<tr><td class="ts">%s</td><td>%s</td></tr>'%(pretty_time(hm),' &nbsp;·&nbsp; '.join(links)))
        rows+=1
    body.append('</table>')

CSS="""
:root{--bg:#0b0b0d;--panel:#15151a;--line:#25252c;--accent:#8ab4ff;--ink:#e9e6e1;--mut:#9a958e;
--mono:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;line-height:1.6}
.wrap{max-width:1040px;margin:0 auto;padding:26px 20px 60px}
.masthead{border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:12px}
.mast-title{font-size:34px;font-weight:800;letter-spacing:-.02em;margin:0 0 4px;color:var(--accent)}
.mast-tag{color:var(--mut);font-size:14px;margin:0 0 12px}
.meta{display:flex;flex-wrap:wrap;gap:8px}
.pill{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);
background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:4px 11px}
.pill.live{color:#3ddc97;border-color:rgba(61,220,151,.35)}
.dot{width:7px;height:7px;border-radius:50%;background:#3ddc97;display:inline-block}
.freshline{font-family:var(--mono);font-size:11px;color:var(--mut);margin:8px 2px 16px;letter-spacing:.04em}
nav.tabs{display:flex;flex-wrap:wrap;gap:7px;margin:14px 0 20px}
nav.tabs a{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;
color:var(--mut);background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:8px 13px}
nav.tabs a:hover{color:var(--ink);border-color:var(--accent)}
nav.tabs a.on{color:#0b0b0d;background:var(--accent);border-color:var(--accent);font-weight:700}
.intro{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;
padding:11px 15px;margin:6px 0 8px;font-size:14.5px}
h2.day{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);
margin:30px 0 10px;padding-bottom:7px;border-bottom:1px solid var(--line)}
table{width:100%;border-collapse:collapse;font-size:14px;background:var(--panel);
border:1px solid var(--line);border-radius:12px;overflow:hidden}
th{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);
text-align:left;padding:9px 14px;border-bottom:1px solid var(--line)}
td{padding:9px 14px;border-bottom:1px solid rgba(255,255,255,.045)}
tr:last-child td{border-bottom:none}
td.ts{font-family:var(--mono);font-size:12.5px;color:var(--mut);white-space:nowrap;width:150px}
a{text-decoration:none}a:hover{text-decoration:underline}
.foot{font-family:var(--mono);font-size:10.5px;color:var(--mut);border-top:1px solid var(--line);
margin-top:28px;padding-top:14px;line-height:1.7}
"""
NAV=('<nav class="tabs">'
 '<a href="index.html">★ Front Page</a>'
 '<a href="cyber-briefing.html">⛨ The Cyber Wire</a>'
 '<a href="wallstreet-briefing.html">▲ The Closing Bell</a>'
 '<a href="mma-briefing.html">⊘ The Octagon</a>'
 '<a href="archive.html" class="on">\U0001f5c4 Archive</a></nav>')

STAMP="""<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>"""

html=("""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Archive — Daily Briefings</title><style>%s</style></head>
<body><div class="wrap">
<header class="masthead"><h1 class="mast-title">Archive</h1>
<p class="mast-tag">Every edition, kept exactly as it was published</p>
<div class="meta"><span class="pill live"><span class="dot"></span> Live</span>
<span class="pill" id="edition">&nbsp;</span><span class="pill" id="datestamp">&nbsp;</span>
<span class="pill">Updated <span id="updated">&nbsp;</span></span></div></header>
<div class="intro">Point-in-time snapshots. Each link opens a briefing exactly as it read at that timestamp — figures, refusals and all — and is never edited afterwards. This page is generated from the contents of the archive directory, never hand-curated, and carries no live widgets.</div>
<div class="freshline" id="freshline">&nbsp;</div>
%s
%s
<div class="foot">%d days &middot; %d editions &middot; %d snapshots. Snapshots older than 21 days are pruned.</div>
</div>
%s
</body></html>""" % (CSS, NAV, "\n".join(body), len(data), rows, len(files), STAMP))

# ---- assertions
assert html.count('<h2 class="day">')==len(data), "headings != days"
assert html.count('<table>')==len(data), "tables != days"
assert html.count('href="archive/')==len(files), "links != files"
assert html.count('class="on"')==1, "not exactly one active nav tab"
heads=re.findall(r'<h2 class="day">(.*?)</h2>',html)
assert len(heads)==len(set(heads)), "duplicate day headings"
assert html.index('<h2 class="day">')>html.index('never hand-curated'), "headings must follow the intro"
open(os.path.join(ROOT,'archive.html'),'w').write(html)
print("archive.html: %d days / %d editions / %d snapshots / %d bytes"%(len(data),rows,len(files),len(html)))
