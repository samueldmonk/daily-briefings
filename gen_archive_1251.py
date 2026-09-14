#!/usr/bin/env python3
"""Regenerate archive.html ENTIRELY from the snapshot directory. Never hand-curated."""
import io,os,re,sys,datetime
D=sys.argv[1];AP=os.path.join(D,'archive');page=os.path.join(D,'archive.html')
s=io.open(page,encoding='utf-8').read()
LABEL={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
ORDER=['cyber','wallstreet','mma']
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
snaps={};n=0
for fn in sorted(os.listdir(AP)):
    m=pat.match(fn)
    if not m: continue
    n+=1
    sec,y,mo,d,hhmm=m.groups()
    snaps.setdefault((int(y),int(mo),int(d)),{}).setdefault(hhmm,{})[sec]=fn
out=[];neds=0
for dt in sorted(snaps,reverse=True):
    day=datetime.date(*dt)
    out.append('<h2 class="sec">%s, %s %d, %d</h2><div class="panel" style="padding:6px 8px"><table><tr><th>Edition</th><th>Snapshots</th></tr>'
               %(day.strftime('%A'),day.strftime('%B'),day.day,day.year))
    for hhmm in sorted(snaps[dt],reverse=True):
        neds+=1
        h,mi=int(hhmm[:2]),int(hhmm[2:])
        ampm='AM' if h<12 else 'PM';h12=h%12 or 12
        cells=[]
        for sec in ORDER:
            fn=snaps[dt][hhmm].get(sec)
            if fn: cells.append('<a href="archive/%s" style="color:var(--accent)">%s</a>'%(fn,LABEL[sec]))
        out.append('<tr><td>%d:%02d %s ET</td><td>%s</td></tr>'%(h12,mi,ampm,' &middot; '.join(cells)))
    out.append('</table></div>')
rows=''.join(out)
m=re.search(r'<div class="note" style="margin-bottom:18px">.*?</div>',s,re.S)
head=s[:m.end()]
tail=s[s.index('<footer>'):]
io.open(page,'w',encoding='utf-8').write(head+rows+tail)
print('archive.html rebuilt: %d days, %d editions, %d snapshot files'%(len(snaps),neds,n))
