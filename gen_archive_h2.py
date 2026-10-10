import os,re,sys,datetime
D=sys.argv[1]; AP=D+'/archive'; P=D+'/archive.html'
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})\.html$')
snaps={}
for fn in sorted(os.listdir(AP)):
    m=pat.match(fn)
    if not m: continue
    s,y,mo,d,h,mi=m.groups(); snaps.setdefault(datetime.date(int(y),int(mo),int(d)),{}).setdefault(h+mi,{})[s]=fn
LAB=[('cyber','The Cyber Wire'),('wallstreet','The Closing Bell'),('mma','The Octagon')]
out=[]; ned=0; nsn=0
for dt in sorted(snaps,reverse=True):
    out.append('<h2>%s, %d %s %d</h2>\n<table>\n<tr><th>Edition</th><th>Snapshots</th></tr>'%(dt.strftime('%A'),dt.day,dt.strftime('%B'),dt.year))
    for hm in sorted(snaps[dt],reverse=True):
        h,mi=int(hm[:2]),int(hm[2:]); t='%d:%02d %s ET'%((h%12) or 12,mi,'AM' if h<12 else 'PM')
        e=snaps[dt][hm]; ned+=1; nsn+=len(e)
        out.append('<tr><td class="mono">%s</td><td>%s</td></tr>'%(t,' · '.join('<a href="archive/%s">%s</a>'%(e[k],l) for k,l in LAB if k in e)))
    out.append('</table>')
s=open(P).read(); a=s.index('<h2>'); b=s.rindex('</table>')+len('</table>')
s=s[:a]+'\n'.join(out)+s[b:]
s=re.sub(r'\d+ editions across \d+ days, \d+ snapshots in total','%d editions across %d days, %d snapshots in total'%(ned,len(snaps),nsn),s,1)
open(P,'w').write(s)
hrefs=re.findall(r'href="archive/([^"]+)"',s); assert all(os.path.exists(AP+'/'+h) for h in hrefs)
print(ned,len(snaps),nsn,len(hrefs))
