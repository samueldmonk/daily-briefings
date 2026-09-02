# -*- coding: utf-8 -*-
import os,re,sys,collections
sys.path.insert(0,'/tmp')
from css import BASE, STAMP, nav, meta
D="/tmp/db_1788357956"
ROOT=":root{--bg:#0b0b0d;--panel:#141418;--panel2:#1b1b21;--line:#2a2a32;--fg:#eeeef2;--muted:#83838f;--muted2:#b9b9c4;--accent:#8f9bb3;--accent2:#c9d1e0;--up:#3fbf72;--crit:#e05555;--warn:#e0a13a;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}\n"
LBL={"cyber":"The Cyber Wire","wallstreet":"The Closing Bell","mma":"The Octagon"}
COL={"cyber":"#22d3a8","wallstreet":"#caa64a","mma":"#e84545"}
pat=re.compile(r'^(cyber|wallstreet|mma)-(\d{4}-\d{2}-\d{2})-(\d{4})\.html$')
snap=collections.defaultdict(lambda: collections.defaultdict(dict))
for f in sorted(os.listdir(os.path.join(D,"archive"))):
    m=pat.match(f)
    if m: snap[m.group(2)][m.group(3)][m.group(1)]=f
def t12(hhmm):
    h=int(hhmm[:2]);mm=hhmm[2:]
    ap="AM" if h<12 else "PM"; hh=h%12 or 12
    return "%d:%s %s ET"%(hh,mm,ap)
import datetime
def datehead(d):
    y,m,dd=map(int,d.split("-"))
    return datetime.date(y,m,dd).strftime("%A, %B %-d, %Y")
h=[]
h.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Archive &mdash; Daily Briefings</title><style>'+ROOT+BASE+'.ed{font-family:var(--mono);font-size:12px;color:var(--muted2);white-space:nowrap}.lk{margin-right:14px}</style></head><body><div class="wrap">')
h.append('<div class="masthead"><h1>Archive</h1><p class="tag">Point-in-time snapshots of every edition &mdash; kept for 21 days</p>'+meta()+'</div>')
h.append('<div class="freshline" id="freshline">&nbsp;</div>')
h.append(nav("archive.html"))
h.append('<div class="note">Each row is one publishing run. Snapshots are <b>point-in-time</b>: the live data widgets inside them still stream current quotes, but all editorial, figures and timestamps are frozen as published. Editions older than 21 days are pruned.</div>')
tot=0
for d in sorted(snap.keys(),reverse=True):
    h.append('<h2>%s</h2><table><tr><th>Edition</th><th>Snapshots</th></tr>'%datehead(d))
    for hhmm in sorted(snap[d].keys(),reverse=True):
        cells=[]
        for sec in ["cyber","wallstreet","mma"]:
            f=snap[d][hhmm].get(sec)
            if f:
                cells.append('<a class="lk" style="color:%s" href="archive/%s">%s</a>'%(COL[sec],f,LBL[sec]))
                tot+=1
        h.append('<tr><td class="ed">%s</td><td>%s</td></tr>'%(t12(hhmm),"".join(cells) or '<span class="flat">&mdash;</span>'))
    h.append('</table>')
h.append('<div class="disc">%d snapshots across %d days. Archive index is regenerated from the files on disk on every run &mdash; it is never hand-curated.</div>'%(tot,len(snap)))
h.append('</div>'+STAMP+'</body></html>')
open(os.path.join(D,"archive.html"),"w").write("".join(h))
print("archive.html ok:",tot,"snapshots,",len(snap),"days")
