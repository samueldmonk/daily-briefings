#!/usr/bin/env python3
"""Regenerate archive.html day sections + footer count from archive/ filenames; keeps the existing shell."""
import os,re,sys,datetime
D=sys.argv[1]; page=os.path.join(D,'archive.html'); s=open(page,encoding='utf-8').read()
LBL={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}; ORD=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
snaps={};n=0;bad=0
for fn in os.listdir(os.path.join(D,'archive')):
    m=pat.match(fn)
    if not m: bad+=1; continue
    n+=1; sec,y,mo,d,hm=m.groups(); snaps.setdefault((int(y),int(mo),int(d)),{}).setdefault(hm,{})[sec]=fn
out=[];eds=0
for dt in sorted(snaps,reverse=True):
    day=datetime.date(*dt); out.append('<h3 class="day">%s, %d %s %d</h3>'%(day.strftime('%A'),day.day,day.strftime('%B'),day.year))
    rows=[]
    for hm in sorted(snaps[dt],reverse=True):
        eds+=1; h,mi=int(hm[:2]),hm[2:]; ap='AM' if h<12 else 'PM'; h12=h%12 or 12
        links=' &middot; '.join('<a href="archive/%s">%s</a>'%(snaps[dt][hm][k],LBL[k]) for k in ORD if k in snaps[dt][hm])
        rows.append('<tr><td class="tm">%d:%s %s ET</td><td>%s</td></tr>'%(h12,mi,ap,links))
    out.append('<div class="panel" style="padding:6px 10px"><table><tr><th>Edition</th><th>Snapshots</th></tr>'+''.join(rows)+'</table></div>')
i=s.index('<h3 class="day">'); j=s.index('<footer class="disc">'); k=s.index('</footer>',j)+len('</footer>')
s=s[:i]+'\n'.join(out)+'\n'+'<footer class="disc">%d snapshots across %d editions and %d days. Unparsed filenames: %d.</footer>'%(n,eds,len(snaps),bad)+s[k:]
open(page,'w',encoding='utf-8').write(s)
