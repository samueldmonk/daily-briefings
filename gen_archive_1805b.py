#!/usr/bin/env python3
"""Regenerate archive.html from archive/ filenames only (keeps shell, day = h3.day, rows td.tm)."""
import os,re,sys,datetime
D=sys.argv[1]; AP=os.path.join(D,'archive'); page=os.path.join(D,'archive.html')
s=open(page,encoding='utf-8').read()
a=s.find('<h3 class="day">'); b=s.find('<footer class="disc">'); e=s.find('</footer>',b)+len('</footer>')
L={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}; O=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
snaps={};n=0;bad=0
for fn in os.listdir(AP):
    m=pat.match(fn)
    if not m: bad+=1; continue
    n+=1; sec,y,mo,d,hm=m.groups(); snaps.setdefault((int(y),int(mo),int(d)),{}).setdefault(hm,{})[sec]=fn
out=[];eds=0
for dt in sorted(snaps,reverse=True):
    day=datetime.date(*dt)
    out.append('<h3 class="day">%s, %d %s %d</h3>\n<div class="panel" style="padding:6px 10px"><table><tr><th>Edition</th><th>Snapshots</th></tr>'%(day.strftime('%A'),day.day,day.strftime('%B'),day.year))
    rows=[]
    for hm in sorted(snaps[dt],reverse=True):
        eds+=1;h=int(hm[:2]);mi=hm[2:];ap='AM' if h<12 else 'PM';h12=h%12 or 12
        links=' &middot; '.join('<a href="archive/%s">%s</a>'%(snaps[dt][hm][k],L[k]) for k in O if k in snaps[dt][hm])
        rows.append('<tr><td class="tm">%d:%s %s ET</td><td>%s</td></tr>'%(h12,mi,ap,links))
    out.append(''.join(rows)+'</table></div>')
foot='<footer class="disc">%d snapshots across %d editions and %d days. Unparsed filenames: %d.</footer>'%(n,eds,len(snaps),bad)
s=s[:a]+'\n'.join(out)+'\n'+foot+s[e:]
open(page,'w',encoding='utf-8').write(s); print(foot)
