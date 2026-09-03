# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, "/tmp/db_1788465063")
from shared import page, nav, META
OUT = "/sessions/nifty-sweet-cannon/mnt/outputs"
IX = dict(accent="#caa64a", accent2="#e8c766", bg="#0d0d0f", panel="#16161a", line="#26262c")

S_WS  = ("Stocks held a broad rally into the last hour of Thursday's session after Fed Governor "
         "Christopher Waller said he is inclined to support holding rates steady this month, with all "
         "three major indexes up more than 1% and the 10-year Treasury yield down about five basis points.")
S_CY  = ("A working privilege-escalation exploit for CrowdStrike's Falcon Sensor is now public with no "
         "vendor advisory or patch, while federal agencies have two days left to fix the two SonicWall "
         "SMA1000 zero-days and three other flaws CISA added to its exploited-vulnerability catalog.")
S_MMA = ("UFC Paris is two days out with Dan Hooker headlining against UFC debutant Salahdine Parnasse, "
         "while UFC 332 is a month away and still without a main event after Valentina Shevchenko withdrew injured.")

EX = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin-top:6px}
.bigcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 22px;
  transition:transform .16s,border-color .16s;display:flex;flex-direction:column}
.bigcard:hover{transform:translateY(-4px)}
.bigcard .kicker{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:9px}
.bigcard h2{margin:0 0 4px;font-size:23px;line-height:1.2}
.bigcard .sub{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:12px}
.bigcard p{margin:0 0 16px;font-size:14.8px;color:#cfc9c2;flex:1}
.bigcard a.rd{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase}
.c-cy{border-left:3px solid #22d3a8} .c-cy .kicker,.c-cy a.rd,.c-cy h2{color:#22d3a8}
.c-ws{border-left:3px solid #caa64a} .c-ws .kicker,.c-ws a.rd,.c-ws h2{color:#caa64a}
.c-ws h2{font-family:Georgia,"Times New Roman",serif}
.c-mma{border-left:3px solid #e84545} .c-mma .kicker,.c-mma a.rd,.c-mma h2{color:#e84545}
"""

b = []
b.append(f'<header class="mast"><h1>Daily Briefings</h1><p class="tag">Security, markets and MMA &mdash; researched fresh, every half hour</p>{META}</header>')
b.append('<p class="freshline" id="freshline">&nbsp;</p>')
b.append(nav("index", IX["accent"]))
b.append('<div class="big">')
b.append(f"""<div class="bigcard c-cy"><div class="kicker">&#9880; Security</div>
<h2>The Cyber Wire</h2><div class="sub">The Wire</div><p>{S_CY}</p>
<a class="rd" href="cyber-briefing.html">Read the briefing &rarr;</a></div>""")
b.append(f"""<div class="bigcard c-ws"><div class="kicker">&#9650; Markets</div>
<h2>The Closing Bell</h2><div class="sub">The Tape</div><p>{S_WS}</p>
<a class="rd" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>""")
b.append(f"""<div class="bigcard c-mma"><div class="kicker">&#8856; MMA</div>
<h2>The Octagon</h2><div class="sub">Tale of the Tape</div><p>{S_MMA}</p>
<a class="rd" href="mma-briefing.html">Read the briefing &rarr;</a></div>""")
b.append('</div>')
b.append('<footer><p style="margin:0">Every edition is researched from live sources at publication time and archived. '
 'Earlier editions are in the <a href="archive.html">Archive</a>.</p>'
 '<p class="disc">Automated summaries of published reporting. Nothing here is investment advice, and security '
 'guidance should be verified against your own vendor advisories.</p></footer>')

H = page("Daily Briefings", IX["accent"], IX["accent2"], IX["bg"], IX["panel"], IX["line"], "\n".join(b), extra_css=EX)
open(os.path.join(OUT, "index.html"), "w").write(H)
print("index ok", len(H))
