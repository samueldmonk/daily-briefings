import os,re,datetime,collections
AD='archive'; SRC='archive.html'
h=open(SRC).read()
files=[f for f in os.listdir(AD) if re.match(r'(cyber|wallstreet|mma)-\d{4}-\d{2}-\d{2}-\d{4}\.html$',f)]
byed=collections.defaultdict(dict)
for f in files:
    sec,rest=f.split('-',1); date=rest[:10]; hm=rest[11:15]
    byed[(date,hm)][sec]=f
days=sorted({k[0] for k in byed},reverse=True)
n_snap,n_ed,n_day=len(files),len(byed),len(days)
COL={'cyber':('#22d3a8','The Cyber Wire'),'wallstreet':('#caa64a','The Closing Bell'),'mma':('#e84545','The Octagon')}
def h12(hm):
    H,M=int(hm[:2]),hm[2:]
    ap='AM' if H<12 else 'PM'; d=H%12 or 12
    return f'{d}:{M} {ap} ET'
out=[]
for d in days:
    head=datetime.date.fromisoformat(d).strftime('%A, %B %-d, %Y')
    out.append(f'<h3 class="dayhead">{head}</h3>\n<table>\n<tr><th>Edition</th><th>The Cyber Wire</th><th>The Closing Bell</th><th>The Octagon</th></tr>')
    for hm in sorted({k[1] for k in byed if k[0]==d},reverse=True):
        cells=''
        for sec in ('cyber','wallstreet','mma'):
            fn=byed[(d,hm)].get(sec); c,label=COL[sec]
            cells += f'<td><a style="color:{c}" href="{AD}/{fn}">{label}</a></td>' if fn else '<td class="mono" style="color:#9aa09e">&mdash;</td>'
        out.append(f'<tr><td class="mono">{h12(hm)}</td>{cells}</tr>')
    out.append('</table>')
body='\n'.join(out)
a=h.find('<h3 class="dayhead">'); b=h.find('<footer>')
assert a>0 and b>a
h=h[:a]+body+'\n\n'+h[b:]
# stats
st=h.find('<div class="stats">'); se=h.find('</div>',h.find('day retention'))+6
stats=(f'<div class="stats">\n  <div class="stat"><div class="n">{n_snap}</div><div class="l">snapshots held</div></div>\n'
 f'  <div class="stat"><div class="n">{n_ed}</div><div class="l">editions, each a set of three briefings</div></div>\n'
 f'  <div class="stat"><div class="n">{n_day}</div><div class="l">days covered, newest first</div></div>\n'
 f'  <div class="stat"><div class="n">21</div><div class="l">day retention; older snapshots are pruned automatically</div></div>\n</div>')
h=h[:st]+stats+h[se:]
open(SRC,'w').write(h)
# post-generation assertions
g=open(SRC).read()
assert g.count('<h3 class="dayhead">')==n_day, 'day headings'
assert g.count('archive/')==n_snap, f"link count {g.count('archive/')} vs {n_snap}"
assert f'<div class="n">{n_snap}</div>' in g and f'<div class="n">{n_ed}</div>' in g and f'<div class="n">{n_day}</div>' in g
assert 'archive.html" class="active"' in g, 'archive tab active'
for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']: assert t in g
assert 'tradingview' not in g.lower(), 'no live widgets'
print(f'ARCHIVE OK  days={n_day} editions={n_ed} snapshots={n_snap}')
