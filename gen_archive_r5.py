#!/usr/bin/env python3
"""Regenerate archive.html rows ENTIRELY from archive/ filenames. Keeps shell (head through intro note, and stamp script)."""
import os,re,sys,datetime
D=sys.argv[1]; P=os.path.join(D,'archive.html'); s=open(P,encoding='utf-8').read()
LAB={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}; ORD=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
sn={};nf=0;bad=0
for fn in sorted(os.listdir(os.path.join(D,'archive'))):
    m=pat.match(fn)
    if not m: bad+=1; continue
    nf+=1; sec,y,mo,d,hm=m.groups(); sn.setdefault((int(y),int(mo),int(d)),{}).setdefault(hm,{})[sec]=fn
out=[];ne=0
for dt in sorted(sn,reverse=True):
    day=datetime.date(*dt)
    out.append('<h3 class="day">%s, %d %s %d</h3>\n'%(day.strftime('%A'),day.day,day.strftime('%B'),day.year))
    rows=[]
    for hm in sorted(sn[dt],reverse=True):
        ne+=1;h,mi=int(hm[:2]),int(hm[2:])
        cells=' &middot; '.join('<a href="archive/%s">%s</a>'%(sn[dt][hm][k],LAB[k]) for k in ORD if k in sn[dt][hm])
        rows.append('<tr><td class="tm">%d:%02d %s ET</td><td>%s</td></tr>'%(h%12 or 12,mi,'AM' if h<12 else 'PM',cells))
    out.append('<div class="panel" style="padding:6px 10px"><table><tr><th>Edition</th><th>Snapshots</th></tr>%s</table></div>\n'%''.join(rows))
out.append('<footer class="disc">%d snapshots across %d editions and %d days. Unparsed filenames: %d.</footer>\n'%(nf,ne,len(sn),bad))
a=s.index('<h3 class="day">'); b=s.index('</div>\n<script>(function()')
open(P,'w',encoding='utf-8').write(s[:a]+''.join(out)+s[b:])
print(nf,ne,len(sn),bad)
