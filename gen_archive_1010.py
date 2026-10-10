#!/usr/bin/env python3
"""Regenerate archive.html from archive/ filenames (dayh/arch/erow layout). Prunes snapshots >21 days old by FILENAME date."""
import os,re,sys,datetime
D=sys.argv[1]; AP=os.path.join(D,'archive'); page=os.path.join(D,'archive.html')
today=datetime.date.fromisoformat(sys.argv[2]); cutoff=today-datetime.timedelta(days=21)
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
snaps={}; pruned=0
for fn in sorted(os.listdir(AP)):
    m=pat.match(fn)
    if not m: continue
    sec,y,mo,d,hm=m.groups(); dt=datetime.date(int(y),int(mo),int(d))
    if dt<cutoff: os.remove(os.path.join(AP,fn)); pruned+=1; continue
    snaps.setdefault(dt,{}).setdefault(hm,{})[sec]=fn
LAB={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
out=[]
for dt in sorted(snaps,reverse=True):
    out.append('<div class="dayh">%s, %d %s %d</div><div class="arch">'%(dt.strftime('%A'),dt.day,dt.strftime('%B'),dt.year))
    for hm in sorted(snaps[dt],reverse=True):
        h,mi=int(hm[:2]),int(hm[2:])
        links=' '.join('<a href="archive/%s">%s</a>'%(snaps[dt][hm][s],LAB[s]) for s in ['cyber','wallstreet','mma'] if s in snaps[dt][hm])
        out.append('<div class="erow"><div class="et">%d:%02d %s ET</div><div class="el">%s</div></div>'%(h%12 or 12,mi,'AM' if h<12 else 'PM',links))
    out.append('</div>')
s=open(page).read()
a=s.index('</div>',s.index('class="note"'))+6
b=s.index('<div class="disc">')
open(page,'w').write(s[:a]+''.join(out)+s[b:])
print('days',len(snaps),'pruned',pruned)
