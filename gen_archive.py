# -*- coding: utf-8 -*-
# Self-contained archive index generator (no external build module).
import os, re, io, datetime
SEC={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
ORDER=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')
snaps={}
for f in os.listdir('archive'):
    m=pat.match(f)
    if not m: continue
    sec,date,hhmm=m.groups()
    snaps.setdefault(date,{}).setdefault(hhmm,{})[sec]=f
MON=['January','February','March','April','May','June','July','August','September','October','November','December']
def prettydate(d):
    y,m,dd=[int(x) for x in d.split('-')]
    return "%s, %s %d, %d"%(datetime.date(y,m,dd).strftime('%A'),MON[m-1],dd,y)
def prettytime(h):
    hh,mm=int(h[:2]),h[2:]
    ap='AM' if hh<12 else 'PM'; d=hh%12 or 12
    return "%d:%s %s ET"%(d,mm,ap)
rows=[]
for date in sorted(snaps,reverse=True):
    rows.append('<h2 class="sec">%s</h2><div class="panel"><table><tr><th>Time</th><th>Editions</th></tr>'%prettydate(date))
    for hhmm in sorted(snaps[date],reverse=True):
        links=[]
        for s in ORDER:
            f=snaps[date][hhmm].get(s)
            if f: links.append('<a href="archive/%s">%s</a>'%(f,SEC[s]))
        rows.append('<tr><td><b>%s</b></td><td>%s</td></tr>'%(prettytime(hhmm),' &middot; '.join(links) or '&mdash;'))
    rows.append('</table></div>')
src=io.open('cyber-briefing.html',encoding='utf-8').read()
css=src[src.find('<style>'):src.find('</style>')+8]
stamp=src[src.rfind('<script>'):src.rfind('</script>')+9]
head=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1">'
 '<title>Archive &mdash; Daily Briefings</title>'+css+'</head><body><div class="wrap">'
 '<header><h1>Archive</h1><p class="tag-line">Point-in-time snapshots of every edition</p>'
 '<div class="meta"><span class="pill live"><span class="dot"></span>Live</span>'
 '<span class="pill" id="edition">Afternoon Edition</span>'
 '<span class="pill" id="datestamp">Saturday, August 29, 2026</span>'
 '<span class="pill">Updated <span id="updated">9:42 PM ET</span></span></div></header>'
 '<div class="freshline" id="freshline">Data as of 9:42 PM ET</div>'
 '<nav class="tabs"><a href="index.html">&#9733; Front Page</a>'
 '<a href="cyber-briefing.html">&#9880; The Cyber Wire</a>'
 '<a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>'
 '<a href="mma-briefing.html">&#8856; The Octagon</a>'
 '<a href="archive.html" class="on">&#128451; Archive</a></nav>'
 '<div class="note">Each snapshot is the page exactly as it was published at that time and is '
 'not updated afterwards. Figures inside a snapshot were current then, not now.</div>')
foot='</div>'+stamp+'</body></html>'
io.open('archive.html','w',encoding='utf-8').write(head+''.join(rows)+foot)
print("archive.html: %d days, %d snapshots"%(len(snaps),sum(len(v) for v in snaps.values())))
