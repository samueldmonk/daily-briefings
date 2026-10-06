#!/usr/bin/env python3
"""Regenerate archive.html rows (dayh/arch/erow layout) entirely from archive/ filenames."""
import os,re,sys,datetime
D=sys.argv[1]; page=os.path.join(D,'archive.html'); s=open(page,encoding='utf-8').read()
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
LAB={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
snaps={};n=0
for fn in os.listdir(os.path.join(D,'archive')):
    m=pat.match(fn)
    if not m: continue
    n+=1; sec,y,mo,d,hm=m.groups()
    snaps.setdefault((int(y),int(mo),int(d)),{}).setdefault(hm,{})[sec]=fn
out=[]
for dt in sorted(snaps,reverse=True):
    day=datetime.date(*dt)
    out.append('<div class="dayh">%s, %d %s %d</div><div class="arch">'%(day.strftime('%A'),day.day,day.strftime('%B'),day.year))
    for hm in sorted(snaps[dt],reverse=True):
        h,mi=int(hm[:2]),int(hm[2:])
        links=' '.join('<a href="archive/%s">%s</a>'%(snaps[dt][hm][k],LAB[k]) for k in ['cyber','wallstreet','mma'] if k in snaps[dt][hm])
        out.append('<div class="erow"><div class="et">%d:%02d %s ET</div><div class="el">%s</div></div>'%(h%12 or 12,mi,'AM' if h<12 else 'PM',links))
    out.append('</div>')
a=s.index('<div class="dayh">'); b=s.index('<div class="disc">')
open(page,'w',encoding='utf-8').write(s[:a]+''.join(out)+s[b:])
print(len(snaps),'days',n,'files')
