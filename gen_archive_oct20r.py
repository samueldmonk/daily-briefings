import os,re,datetime
from collections import defaultdict
s=open('archive.html').read()
a=s.index('<h2 class="day">'); b=s.index('<p class="disc">')
NAMES=[('cyber','The Cyber Wire','#22d3a8'),('wallstreet','The Closing Bell','#caa64a'),('mma','The Octagon','#e84545')]
d=defaultdict(lambda:defaultdict(set))
for f in os.listdir('archive'):
    m=re.match(r'(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$',f)
    if m: d[m.group(2)][m.group(3)].add(m.group(1))
out=[]
for day in sorted(d,reverse=True):
    dt=datetime.date.fromisoformat(day)
    out.append('<h2 class="day">%s, %s %d, %d</h2>\n<div class="panel" style="padding:6px 10px"><table><thead><tr><th>Edition</th><th>Briefings</th></tr></thead><tbody>\n'%(dt.strftime('%A'),dt.strftime('%B'),dt.day,dt.year))
    for hm in sorted(d[day],reverse=True):
        h,mi=int(hm[:2]),hm[2:]; ap='AM' if h<12 else 'PM'; h12=h%12 or 12
        links=' &middot; '.join('<a href="archive/%s-%s-%s.html" style="color:%s">%s</a>'%(k,day,hm,c,n) for k,n,c in NAMES if k in d[day][hm])
        out.append('<tr><td class="ts">%d:%s %s ET</td><td class="lk">%s</td></tr>\n'%(h12,mi,ap,links))
    out.append('</tbody></table></div>\n\n')
open('archive.html','w').write(s[:a]+''.join(out)+s[b:])
