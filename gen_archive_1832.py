import os,re,collections
R='/tmp/db_1789423518'
A=os.path.join(R,'archive')
SEC={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
files=[f for f in os.listdir(A) if f.endswith('.html')]
ed=collections.defaultdict(dict)
for f in files:
    m=re.match(r'(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$',f)
    if not m: continue
    ed[(m.group(2),m.group(3))][m.group(1)]=f
def t12(hhmm):
    h,mi=int(hhmm[:2]),hhmm[2:]
    ap='AM' if h<12 else 'PM'; hh=h%12 or 12
    return '%d:%s %s ET'%(hh,mi,ap)
from datetime import date
days=sorted({d for d,_ in ed},reverse=True)
rows=0;links=0;body=[]
for d in days:
    y,mo,da=map(int,d.split('-'))
    body.append('<div class="dayh">%s</div><div class="arch">'%date(y,mo,da).strftime('%A, %-d %B %Y'))
    for (dd,hh) in sorted([k for k in ed if k[0]==d],key=lambda k:k[1],reverse=True):
        secs=ed[(dd,hh)]
        cells=[]
        for key in ('cyber','wallstreet','mma'):
            if key in secs:
                cells.append('<a href="archive/%s">%s</a>'%(secs[key],SEC[key])); links+=1
            else:
                cells.append('<span class="na">%s</span>'%SEC[key])
        body.append('<div class="erow"><div class="et">%s</div><div class="el">%s</div></div>'%(t12(hh),' '.join(cells)))
        rows+=1
    body.append('</div>')
HTML=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
'<meta name="viewport" content="width=device-width,initial-scale=1">'
'<title>Archive &mdash; Daily Briefings</title><style>'
':root{--bg:#0d1117;--panel:#151b23;--line:#242c38;--fg:#e6edf3;--mut:#8b98a8;--accent:#9fb4cc;--mono:ui-monospace,SFMono-Regular,Menlo,monospace}'
'*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6}'
'.wrap{max-width:1000px;margin:0 auto;padding:26px 20px 60px}'
'.masthead h1{margin:0;font-size:32px;letter-spacing:-.5px}'
'.masthead p{margin:6px 0 0;color:var(--mut);font-size:14px}'
'.meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}'
'.pill{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:3px 11px;font-family:var(--mono);font-size:11px;color:var(--mut)}'
'.pill.live{color:#22d3a8;border-color:#1d4d43}'
'.freshline{font-family:var(--mono);font-size:11px;color:var(--mut);margin:10px 0 2px}'
'nav.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 22px;border-bottom:1px solid var(--line);padding-bottom:12px}'
'nav.tabs a{color:var(--mut);text-decoration:none;font-family:var(--mono);font-size:12px;letter-spacing:.06em;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:7px 12px}'
'nav.tabs a.active{color:var(--accent);border-color:var(--accent)}'
'nav.tabs a:hover{color:var(--fg)}'
'.note{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;padding:11px 15px;font-size:14px;margin-bottom:20px}'
'.dayh{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin:22px 0 8px}'
'.arch{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}'
'.erow{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;padding:9px 15px;border-top:1px solid var(--line)}'
'.erow:first-child{border-top:none}'
'.et{font-family:var(--mono);font-size:12px;color:var(--mut);min-width:96px}'
'.el a{color:var(--fg);text-decoration:none;font-size:13.5px;border-bottom:1px solid var(--line);margin-right:14px}'
'.el a:hover{color:var(--accent);border-color:var(--accent)}'
'.el .na{color:#4a5563;font-size:13.5px;margin-right:14px}'
'.disc{margin-top:22px;font-size:11.5px;color:var(--mut);font-style:italic}'
'</style></head><body><div class="wrap"><div class="masthead"><h1>Archive</h1>'
'<p>Point-in-time snapshots of every edition.</p>'
'<div class="meta"><span class="pill live">&#9679; <span>Live</span></span>'
'<span class="pill" id="edition"></span><span class="pill" id="datestamp"></span>'
'<span class="pill">Updated <span id="updated"></span></span></div></div>'
'<div class="freshline" id="freshline"></div>'
'<nav class="tabs"><a href="index.html">&#9733; Front Page</a>'
'<a href="cyber-briefing.html">&#9960; The Cyber Wire</a>'
'<a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>'
'<a href="mma-briefing.html">&#8856; The Octagon</a>'
'<a href="archive.html" class="active">&#128452; Archive</a></nav>'
'<div class="note">Each link is the page exactly as published at that time &mdash; a point-in-time snapshot, not a live page. '
'Figures, deadlines and countdowns in a snapshot were current when it was written and are not updated afterwards. '
'Snapshots older than 21 days are pruned.</div>'
+''.join(body)+
'<div class="disc">Archived editions are retained for reference. For the current briefings use the tabs above.</div></div>'
'<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat(\'en-US\',{timeZone:\'America/New_York\',weekday:\'long\',year:\'numeric\',month:\'long\',day:\'numeric\'}).format(n);var t=new Intl.DateTimeFormat(\'en-US\',{timeZone:\'America/New_York\',hour:\'numeric\',minute:\'2-digit\'}).format(n);var h=parseInt(new Intl.DateTimeFormat(\'en-US\',{timeZone:\'America/New_York\',hour:\'numeric\',hour12:false}).format(n),10);var ed=h<11?\'Morning Edition\':(h<15?\'Midday Edition\':\'Afternoon Edition\');document.getElementById(\'datestamp\').textContent=et;document.getElementById(\'updated\').textContent=t+\' ET\';document.getElementById(\'edition\').textContent=ed;var fl=document.getElementById(\'freshline\');if(fl)fl.textContent=\'Data as of \'+t+\' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET\';}catch(e){}})();</script>'
'</body></html>')
open(os.path.join(R,'archive.html'),'w').write(HTML)
# post-generation assertions
g=HTML
assert g.count('archive/')==links==len([f for f in files if re.match(r'(cyber|wallstreet|mma)-\d{4}-\d{2}-\d{2}-\d{4}\.html$',f)]), (g.count('archive/'),links,len(files))
assert g.count('class="erow"')==rows==len(ed)
assert g.count('class="dayh"')==len(days)
assert g.count('class="active"')==1
for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
    assert 'href="%s"'%tab in g
assert 'tradingview' not in g.lower()
assert g.rstrip().endswith('</html>')
print('ARCHIVE-1832 OK links=%d rows=%d days=%d'%(links,rows,len(days)))
