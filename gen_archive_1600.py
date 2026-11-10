#!/usr/bin/env python3
"""Regenerate archive.html from archive/ snapshots (matches the .arow/.atime shell, Nov 2026)."""
import io,os,re,sys,datetime
D=sys.argv[1]; AP=os.path.join(D,'archive'); page=os.path.join(D,'archive.html')
s=io.open(page,encoding='utf-8').read()
LABEL={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}; ORDER=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$'); snaps={}; n=0
for fn in sorted(os.listdir(AP)):
    m=pat.match(fn)
    if not m: continue
    n+=1; sec,y,mo,d,hm=m.groups(); snaps.setdefault((int(y),int(mo),int(d)),{}).setdefault(hm,{})[sec]=fn
out=[]
for dt in sorted(snaps,reverse=True):
    day=datetime.date(*dt); out.append('<h2 class="sec">%s %d, %d</h2><div class="panel" style="padding:6px 14px">'%(day.strftime('%B'),day.day,day.year))
    for hm in sorted(snaps[dt],reverse=True):
        h,mi=int(hm[:2]),int(hm[2:]); st='%d:%02d %s ET'%(h%12 or 12,mi,'AM' if h<12 else 'PM')
        cells=' &middot; '.join('<a href="archive/%s">%s</a>'%(snaps[dt][hm][k],LABEL[k]) for k in ORDER if k in snaps[dt][hm])
        out.append('<div class="arow"><span class="atime">%s</span><span class="alinks">%s</span></div>'%(st,cells))
    out.append('</div>')
s=re.sub(r'<b>\d+ snapshots across \d+ days\.</b>','<b>%d snapshots across %d days.</b>'%(n,len(snaps)),s,count=1)
a=s.index('<h2 class="sec">'); b=s.index('<footer>')
io.open(page,'w',encoding='utf-8').write(s[:a]+''.join(out)+s[b:])
print('rebuilt',n,'files',len(snaps),'days')
