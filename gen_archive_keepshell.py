# Regenerate archive.html list from archive/ snapshots, keeping the existing page shell.
import os,re,sys,datetime
R=sys.argv[1]; A=os.path.join(R,'archive'); P=os.path.join(R,'archive.html')
s=open(P).read()
i=s.index('<h2 class="sec">'); j=s.index('<footer>')
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})\.html$')
names={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
ed={}
for f in os.listdir(A):
    m=pat.match(f)
    if not m: continue
    sec,y,mo,d,hh,mm=m.groups(); ed.setdefault((y,mo,d),{}).setdefault(hh+mm,{})[sec]=f
out=[];n=0
for k in sorted(ed,reverse=True):
    dt=datetime.date(int(k[0]),int(k[1]),int(k[2]))
    out.append('<h2 class="sec">%s %d, %d</h2><div class="panel"><table><tr><th>Edition</th><th>Snapshots</th></tr>'%(dt.strftime('%B'),dt.day,dt.year))
    for t in sorted(ed[k],reverse=True):
        h=int(t[:2]);m_=t[2:];ap='AM' if h<12 else 'PM';h12=h%12 or 12
        links=' &nbsp;&middot;&nbsp; '.join('<a href="archive/%s">%s</a>'%(ed[k][t][sc],names[sc]) for sc in ('cyber','wallstreet','mma') if sc in ed[k][t]); n+=sum(1 for sc in ed[k][t])
        out.append('<tr><td>%d:%s %s ET</td><td>%s</td></tr>'%(h12,m_,ap,links))
    out.append('</table></div>')
s=s[:i]+''.join(out)+s[j:]
neds=sum(len(v) for v in ed.values())
s=re.sub(r'<div class="disc">\d+ snapshots across \d+ editions and \d+ days\.</div>','<div class="disc">%d snapshots across %d editions and %d days.</div>'%(n,neds,len(ed)),s)
open(P,'w').write(s); print(n,neds,len(ed))
