# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp')
from css import BASE, STAMP, nav, meta
OUT="/sessions/amazing-determined-planck/mnt/outputs/"
ROOT=":root{--bg:#0b0b0d;--panel:#141418;--panel2:#1b1b21;--line:#2a2a32;--fg:#eeeef2;--muted:#83838f;--muted2:#b9b9c4;--accent:#8f9bb3;--accent2:#c9d1e0;--up:#3fbf72;--crit:#e05555;--warn:#e0a13a;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}\n"
EXTRA = """.c-sec{border-left:3px solid #22d3a8}.c-sec .kicker{color:#22d3a8}.c-sec:hover{border-color:#22d3a8}
.c-mkt{border-left:3px solid #caa64a}.c-mkt .kicker{color:#caa64a}.c-mkt:hover{border-color:#caa64a}
.c-mkt h3{font-family:Georgia,"Times New Roman",serif}
.c-mma{border-left:3px solid #e84545}.c-mma .kicker{color:#e84545}.c-mma:hover{border-color:#e84545}
.c-sec .more{color:#22d3a8}.c-mkt .more{color:#caa64a}.c-mma .more{color:#e84545}
"""
h=[]
h.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Daily Briefings</title><style>'+ROOT+BASE+EXTRA+'</style></head><body><div class="wrap">')
h.append('<div class="masthead"><h1>Daily Briefings</h1><p class="tag">Security, markets and mixed martial arts &mdash; rebuilt from live sources every 30 minutes</p>'+meta()+'</div>')
h.append('<div class="freshline" id="freshline">&nbsp;</div>')
h.append(nav("index.html"))
h.append('''<h2>Today&rsquo;s Briefings</h2><div class="big">
<div class="card c-sec"><div class="kicker">&#9880; The Cyber Wire &middot; The Wire</div>
<h3>A CVSS 10 zero-day is being exploited in SonicWall&rsquo;s remote-access gateway</h3>
<p>SonicWall says <b>two SMA1000 zero-days it discovered internally</b> &mdash; one scored <b>CVSS 10</b> &mdash; are already being exploited and appear to have been chained for unauthenticated remote code execution, with hotfixes available, <b>no indicators of compromise published</b> and neither flaw yet in CISA&rsquo;s KEV catalog.</p>
<a class="more" href="cyber-briefing.html">Read the briefing &rarr;</a></div>
<div class="card c-mkt"><div class="kicker">&#9650; The Closing Bell &middot; The Tape</div>
<h3>A split open: the Dow up, small caps down 1.2%</h3>
<p>The opening bell produced a split tape rather than a down one &mdash; the Dow up <b>0.37%</b> and the S&amp;P 500 up <b>0.06%</b> while the Nasdaq slipped <b>0.06%</b> and the Russell 2000 fell <b>1.23%</b> &mdash; after ADP put August private payroll growth at <b>38,000</b>, the smallest since January, with the 10-year Treasury yield touching <b>4.814%</b> and crude reversing lower from a one-month high.</p>
<a class="more" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>
<div class="card c-mma"><div class="kicker">&#8856; The Octagon &middot; Tale of the Tape</div>
<h3>A UFC debutant is a &minus;550 favourite over a ranked veteran</h3>
<p>UFC Paris lands Saturday at the Accor Arena with <b>Salahdine Parnasse a &minus;550 favourite on his UFC debut</b> over the No. 10-ranked Dan Hooker at <b>+400</b> &mdash; the shortest main-event price on a fourteen-bout card &mdash; three days after Song Yadong&rsquo;s second-round upset of Umar Nurmagomedov in Shanghai banked a <b>$100,000</b> Performance of the Night bonus.</p>
<a class="more" href="mma-briefing.html">Read the briefing &rarr;</a></div>
</div>''')
h.append('''<h2>How this works</h2><div class="panel"><p style="margin:0;font-size:14.5px;color:var(--muted2)">Each briefing is rebuilt from sources fetched during that run. Every figure carries the clock and the source it came from; where a number could not be verified in the run that published it, the page says so rather than estimating. Point-in-time snapshots of every edition are kept in the <a href="archive.html">Archive</a>.</p></div>''')
h.append('<div class="disc">Information only. The markets briefing is not investment advice; the MMA briefing carries no wagering advice; the security briefing summarises vendor advisories and does not substitute for them.</div>')
h.append('</div>'+STAMP+'</body></html>')
open(OUT+"index.html","w").write("".join(h))
print("ix ok", sum(len(x) for x in h))
