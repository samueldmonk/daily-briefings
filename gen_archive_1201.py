# -*- coding: utf-8 -*-
import os,re,collections
REPO='/tmp/db_1789660241'
SEC={'cyber':('The Cyber Wire','cyber-briefing.html'),
     'wallstreet':('The Closing Bell','wallstreet-briefing.html'),
     'mma':('The Octagon','mma-briefing.html')}
files=[f for f in os.listdir(REPO+'/archive') if f.endswith('.html')]
idx=collections.defaultdict(lambda: collections.defaultdict(dict))
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')
bad=0
for f in files:
    m=pat.match(f)
    if not m: bad+=1; continue
    s,d,t=m.groups(); idx[d][t][s]=f
def h12(t):
    hh,mm=int(t[:2]),t[2:]
    ap='AM' if hh<12 else 'PM'; h=hh%12 or 12
    return '%d:%s %s ET'%(h,mm,ap)
head=open(REPO+'/index.html').read()
head=head[:head.find('</head>')+7].replace('<title>Daily Briefings</title>','<title>Archive &mdash; Daily Briefings</title>')
head=re.sub(r'<title>.*?</title>','<title>Archive &mdash; Daily Briefings</title>',head,count=1)
nav=('<nav class="tabs"><a href="index.html">&#9733; Front Page</a>'
 '<a href="cyber-briefing.html">&#9960; The Cyber Wire</a>'
 '<a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>'
 '<a href="mma-briefing.html">&#8856; The Octagon</a>'
 '<a href="archive.html" class="active">&#128452; Archive</a></nav>')
META=('<div class="meta"><span class="pill live"><span class="dot"></span>Live</span>'
 '<span class="pill" id="edition">&nbsp;</span><span class="pill" id="datestamp">&nbsp;</span>'
 '<span class="pill">Updated <span id="updated">&nbsp;</span></span></div>')
STAMP = """<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>"""
MONTH=['January','February','March','April','May','June','July','August','September','October','November','December']
body=['<body><div class="wrap"><div class="masthead"><h1>Archive</h1>'
 '<div class="tag">Point-in-time snapshots of every edition &mdash; each file is the page exactly as it was published</div>'
 +META+'</div><div class="freshline" id="freshline">&nbsp;</div>'+nav]
links=0; editions=0
for d in sorted(idx,reverse=True):
    y,m,dd=d.split('-')
    body.append('<h2 class="sec">%s %d, %s</h2><div class="panel"><table><tr><th>Edition</th><th>Snapshots</th></tr>'%(MONTH[int(m)-1],int(dd),y))
    for t in sorted(idx[d],reverse=True):
        editions+=1
        cells=[]
        for s in ['cyber','wallstreet','mma']:
            f=idx[d][t].get(s)
            if f: cells.append('<a href="archive/%s">%s</a>'%(f,SEC[s][0])); links+=1
            else: cells.append('<span style="color:var(--muted)">%s &mdash;</span>'%SEC[s][0])
        body.append('<tr><td>%s</td><td>%s</td></tr>'%(h12(t),' &nbsp;&middot;&nbsp; '.join(cells)))
    body.append('</table></div>')
body.append('<footer><h5>About the archive</h5><ul>'
 '<li>Snapshots are point-in-time: each file is frozen as published and is <b>not</b> updated afterwards, so figures inside an older snapshot may since have been corrected on the live pages.</li>'
 '<li>Live market widgets are deliberately absent here and on snapshots older than the current edition where they would render present-day data into a past page.</li>'
 '<li>Snapshots older than 21 days are pruned automatically.</li>'
 '</ul><div class="disc">%d snapshots across %d editions and %d days.</div></footer></div>'%(links,editions,len(idx)))
body.append(STAMP+'</body></html>')
out=head+''.join(body)
open(REPO+'/archive.html','w').write(out)
print('links=%d editions=%d days=%d unparsed=%d size=%.1fKB'%(links,editions,len(idx),bad,len(out)/1024))
