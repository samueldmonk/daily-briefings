import os,re,datetime,sys
D=sys.argv[1]; A=D+'/archive'
cut=(datetime.date(2026,11,4)-datetime.timedelta(days=21))
for f in os.listdir(A):
    m=re.match(r'(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$',f)
    if m and datetime.date.fromisoformat(m.group(2))<cut: os.remove(os.path.join(A,f))
s=open(D+'/archive.html').read()
head=s[:s.find('<h3 class="day"')]; tail=s[s.find('</div>\n<script>'):]
ed={};bad=0;n=0
for f in os.listdir(A):
    m=re.match(r'(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$',f)
    if not m: bad+=1; continue
    n+=1; ed.setdefault(m.group(2),{}).setdefault(m.group(3),{})[m.group(1)]=f
names=[('cyber','The Cyber Wire'),('wallstreet','The Closing Bell'),('mma','The Octagon')]
out=[]
for d in sorted(ed,reverse=True):
    dt=datetime.date.fromisoformat(d)
    out.append(f'<h3 class="day">{dt.strftime("%A")}, {dt.day} {dt.strftime("%B %Y")}</h3>\n<div class="panel" style="padding:6px 10px"><table><tr><th>Edition</th><th>Snapshots</th></tr>')
    for hm in sorted(ed[d],reverse=True):
        h,mi=int(hm[:2]),hm[2:]; lab=f'{(h-1)%12+1}:{mi} {"AM" if h<12 else "PM"} ET'
        links=' &middot; '.join(f'<a href="archive/{ed[d][hm][k]}">{t}</a>' for k,t in names if k in ed[d][hm])
        out.append(f'<tr><td class="tm">{lab}</td><td>{links}</td></tr>')
    out.append('</table></div>')
ne=sum(len(v) for v in ed.values())
out.append(f'<footer class="disc">{n} snapshots across {ne} editions and {len(ed)} days. Unparsed filenames: {bad}.</footer>\n')
open(D+'/archive.html','w').write(head+'\n'.join(out)+tail)
print(n,ne,len(ed),bad)
