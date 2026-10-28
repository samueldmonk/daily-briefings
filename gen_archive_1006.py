import os,re,datetime
from collections import defaultdict
s=open('archive.html').read()
a=s.index('<h3 class="dayhead">'); b=s.rindex('</table>')+len('</table>')
N=[('cyber','The Cyber Wire','#22d3a8'),('wallstreet','The Closing Bell','#caa64a'),('mma','The Octagon','#e84545')]
d=defaultdict(lambda:defaultdict(set))
for f in os.listdir('archive'):
    m=re.match(r'(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$',f)
    if m: d[m.group(2)][m.group(3)].add(m.group(1))
out=[]
for day in sorted(d,reverse=True):
    dt=datetime.date.fromisoformat(day)
    out.append('<h3 class="dayhead">%s, %s %d, %d</h3>\n<table>\n<tr><th>Edition</th><th>The Cyber Wire</th><th>The Closing Bell</th><th>The Octagon</th></tr>\n'%(dt.strftime('%A'),dt.strftime('%B'),dt.day,dt.year))
    for hm in sorted(d[day],reverse=True):
        h=int(hm[:2]); ap='AM' if h<12 else 'PM'; h12=h%12 or 12
        cells=''.join('<td><a style="color:%s" href="archive/%s-%s-%s.html">%s</a></td>'%(c,k,day,hm,n) if k in d[day][hm] else '<td>—</td>' for k,n,c in N)
        out.append('<tr><td class="mono">%d:%s %s ET</td>%s</tr>\n'%(h12,hm[2:],ap,cells))
    out.append('</table>\n\n')
open('archive.html','w').write(s[:a]+''.join(out).rstrip('\n')+s[b:])
