# -*- coding: utf-8 -*-
import os,re,sys
sys.path.insert(0,'/tmp/build'); from common import css,nav,META,STAMP
SEC={'cyber':('The Cyber Wire','#22d3a8'),'wallstreet':('The Closing Bell','#caa64a'),'mma':('The Octagon','#e84545')}
snaps={}
for f in os.listdir('archive'):
    m=re.match(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$',f)
    if not m: continue
    s,d,t=m.groups(); snaps.setdefault(d,{}).setdefault(t,{})[s]=f
def h12(t):
    h,mn=int(t[:2]),t[2:]
    ap='AM' if h<12 else 'PM'; hh=h%12 or 12
    return '%d:%s %s ET'%(hh,mn,ap)
import datetime
rows=[]
for d in sorted(snaps,reverse=True):
    dt=datetime.date(*map(int,d.split('-')))
    rows.append('<h2 class="sec">%s</h2><div class="panel"><table>'%dt.strftime('%A, %B %-d, %Y'))
    rows.append('<tr><th>Edition</th><th>Snapshots</th></tr>')
    for t in sorted(snaps[d],reverse=True):
        links=' · '.join('<a href="archive/%s">%s</a>'%(snaps[d][t][k],SEC[k][0])
                         for k in ['cyber','wallstreet','mma'] if k in snaps[d][t])
        rows.append('<tr><td class="mono">%s</td><td>%s</td></tr>'%(h12(t),links))
    rows.append('</table></div>')
nd=len(snaps); ne=sum(len(v) for v in snaps.values())
ns=sum(len(x) for v in snaps.values() for x in v.values())
body=('<p class="freshline" id="freshline">&nbsp;</p>'+nav('archive')+
  '<div class="panel"><p style="margin:0">Point-in-time snapshots of every edition. Each file is exactly as it was published at that timestamp — figures, countdowns and live widgets were correct as of then and are <b>not</b> updated afterwards. Covering <b>%d days · %d editions · %d snapshots</b>.</p></div>'%(nd,ne,ns)
  +''.join(rows))
html="""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Archive — Daily Briefings</title>
%s
</head><body><div class="wrap">
  <header class="mast">
    <h1>Archive</h1>
    <p class="tag">Point-in-time snapshots of past editions</p>
    %s
  </header>
%s
</div>
%s
</body></html>"""%(css('index'),META,body,STAMP)
open('archive.html','w',encoding='utf-8').write(html)
print('archive.html %d bytes | %d days %d editions %d snapshots'%(len(html),nd,ne,ns))
