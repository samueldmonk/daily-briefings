import os,re,datetime
s=open('archive.html').read()
a=s.index('<h3 class="day">'); b=s.index('<footer class="disc">'); e=s.index('</footer>',b)+len('</footer>')
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$')
L={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
snaps={};n=0;bad=0
for f in os.listdir('archive'):
    m=pat.match(f)
    if not m: bad+=1; continue
    n+=1; sec,y,mo,d,hm=m.groups(); snaps.setdefault((int(y),int(mo),int(d)),{}).setdefault(hm,{})[sec]=f
out=[];eds=0
for dt in sorted(snaps,reverse=True):
    day=datetime.date(*dt); out.append('<h3 class="day">%s, %d %s %d</h3>\n<div class="panel" style="padding:6px 10px"><table><tr><th>Edition</th><th>Snapshots</th></tr>'%(day.strftime('%A'),day.day,day.strftime('%B'),day.year))
    for hm in sorted(snaps[dt],reverse=True):
        eds+=1;h,mi=int(hm[:2]),hm[2:];lab='%d:%s %s ET'%((h-1)%12+1,mi,'AM' if h<12 else 'PM')
        links=' &middot; '.join('<a href="archive/%s">%s</a>'%(snaps[dt][hm][k],L[k]) for k in ['cyber','wallstreet','mma'] if k in snaps[dt][hm])
        out.append('<tr><td class="tm">%s</td><td>%s</td></tr>'%(lab,links))
    out.append('</table></div>\n')
ft='<footer class="disc">%d snapshots across %d editions and %d days. Unparsed filenames: %d.</footer>'%(n,eds,len(snaps),bad)
open('archive.html','w').write(s[:a]+''.join(out)+ft+s[e:])
print(ft)
