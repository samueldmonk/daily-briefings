import os,re,sys,datetime
D=sys.argv[1];p=os.path.join(D,'archive.html');s=open(p,encoding='utf-8').read()
LAB={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
cut=datetime.date(2026,10,7)-datetime.timedelta(days=21)
snaps={};n=0
for fn in os.listdir(os.path.join(D,'archive')):
    m=re.match(r'(cyber|wallstreet|mma)-(\d{4})-(\d\d)-(\d\d)-(\d\d)(\d\d)\.html$',fn)
    if not m: continue
    d=datetime.date(int(m[2]),int(m[3]),int(m[4]))
    if d<cut: os.remove(os.path.join(D,'archive',fn)); continue
    snaps.setdefault(d,{}).setdefault(m[5]+m[6],{})[m[1]]=fn; n+=1
out=[]
for d in sorted(snaps,reverse=True):
    out.append('\n<h2>%s, %d %s %d</h2>\n<table>\n<tr><th>Edition</th><th>Snapshots</th></tr>\n'%(d.strftime('%A'),d.day,d.strftime('%B'),d.year))
    for hm in sorted(snaps[d],reverse=True):
        h=int(hm[:2]);mi=hm[2:];ap='AM' if h<12 else 'PM';h12=h%12 or 12
        links=' · '.join('<a href="archive/%s">%s</a>'%(snaps[d][hm][k],LAB[k]) for k in LAB if k in snaps[d][hm])
        out.append('<tr><td class="mono">%d:%s %s ET</td><td>%s</td></tr>\n'%(h12,mi,ap,links))
    out.append('</table>\n')
eds=sum(len(v) for v in snaps.values())
s=re.sub(r'\d+ editions across \d+ days, \d+ snapshots in total','%d editions across %d days, %d snapshots in total'%(eds,len(snaps),n),s,1)
a=s.index('</div>',s.index('<div class="note">'))+6; b=s.index('\n<footer>')
s=s[:a]+'\n'+''.join(out)+s[b:]
open(p,'w',encoding='utf-8').write(s);print(eds,len(snaps),n)
