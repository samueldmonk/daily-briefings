import os,re,datetime
from collections import defaultdict
s=open('archive.html').read()
a=s.index('<h3 class="day">'); b=s.index('</footer>',s.index('<footer class="disc">'))+len('</footer>')
NAMES=[('cyber','The Cyber Wire'),('wallstreet','The Closing Bell'),('mma','The Octagon')]
rx=re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')
d=defaultdict(lambda: defaultdict(set)); n=0; bad=0
for f in os.listdir('archive'):
    m=rx.match(f)
    if not m: bad+=1; continue
    d[m.group(2)][m.group(3)].add(m.group(1)); n+=1
out=[]; eds=0
for day in sorted(d,reverse=True):
    dt=datetime.date.fromisoformat(day)
    out.append(f'<h3 class="day">{dt.strftime("%A")}, {dt.day} {dt.strftime("%B %Y")}</h3>\n<div class="panel" style="padding:6px 10px"><table><tr><th>Edition</th><th>Snapshots</th></tr>')
    for hm in sorted(d[day],reverse=True):
        eds+=1; h=int(hm[:2]); mi=hm[2:]
        t=f'{(h%12) or 12}:{mi} {"AM" if h<12 else "PM"} ET'
        links=' &middot; '.join(f'<a href="archive/{k}-{day}-{hm}.html">{nm}</a>' for k,nm in NAMES if k in d[day][hm])
        out.append(f'<tr><td class="tm">{t}</td><td>{links}</td></tr>')
    out.append('</table></div>\n')
out.append(f'<footer class="disc">{n} snapshots across {eds} editions and {len(d)} days. Unparsed filenames: {bad}.</footer>')
open('archive.html','w').write(s[:a]+''.join(out)+s[b:])
