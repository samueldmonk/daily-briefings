import os,re,sys,collections
D=sys.argv[1]; R=f'/tmp/{D}'
files=[f for f in os.listdir(f'{R}/archive') if re.fullmatch(r'(cyber|wallstreet|mma)-\d{4}-\d{2}-\d{2}-\d{4}\.html',f)]
LBL={'cyber':'The Cyber Wire','wallstreet':'The Closing Bell','mma':'The Octagon'}
ORD=['cyber','wallstreet','mma']
ed=collections.defaultdict(dict)
for f in files:
    sec,y,m,d,hm=re.fullmatch(r'(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html',f).groups()
    ed[(f'{y}-{m}-{d}',hm)][sec]=f
def h12(hm):
    H,M=int(hm[:2]),hm[2:]
    ap='AM' if H<12 else 'PM'; hh=H%12 or 12
    return f'{hh}:{M} {ap} ET'
days=collections.defaultdict(list)
for (day,hm) in ed: days[day].append(hm)
body=[]; links=0; rows=0
for day in sorted(days,reverse=True):
    body.append(f'<div class="dayh">{day}</div><div class="arch">')
    for hm in sorted(days[day],reverse=True):
        rows+=1
        cells=''.join(f'<a href="archive/{ed[(day,hm)][s]}">{LBL[s]}</a>' for s in ORD if s in ed[(day,hm)])
        links+=sum(1 for s in ORD if s in ed[(day,hm)])
        body.append(f'<div class="erow"><span class="etime">{h12(hm)}</span>{cells}</div>')
    body.append('</div>')
BODY=''.join(body)

old=open(f'{R}/archive.html').read()
head_end=old.index('<div class="dayh">')
tail_start=old.rindex('</div>', 0, old.index('</body>'))
# rebuild: keep everything before first dayh, then BODY, then the original closing markup after the last archive div
after=old[old.index('</body>'):]
new=old[:head_end]+BODY+'</div>'+after
# normalise: ensure wrap closes once
open(f'{R}/archive.html','w').write(new)

# assertions
h=open(f'{R}/archive.html').read()
assert h.count('href="archive/')==links==len(files), (h.count('href="archive/'),links,len(files))
assert h.count('class="erow"')==rows==len(ed), (h.count('class="erow"'),rows,len(ed))
assert h.count('class="dayh"')==len(days)
assert h.count('class="active"')==1
for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
    assert f'href="{t}"' in h, t
assert 'tradingview' not in h.lower()
assert h.rstrip().endswith('</html>')
print(f'archive OK: {len(files)} snapshots, {len(ed)} editions, {len(days)} days')
