# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
EXTRA = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px;margin-top:6px}
.big .card{padding:20px 21px;border-top:3px solid var(--line)}
.big .card .kick{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:9px}
.big .card h3{font-size:20px;margin:0 0 9px}
.big .card p{font-size:14.5px;color:#cfcbc6;margin:0 0 14px}
.big .card a.go{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.c-cy{border-top-color:#22d3a8} .c-cy .kick,.c-cy a.go{color:#22d3a8}
.c-ws{border-top-color:#caa64a} .c-ws .kick,.c-ws a.go{color:#caa64a} .c-ws h3{font-family:Georgia,'Times New Roman',serif}
.c-mm{border-top-color:#e84545} .c-mm .kick,.c-mm a.go{color:#e84545}
.c-cy:hover{border-color:#22d3a8} .c-ws:hover{border-color:#caa64a} .c-mm:hover{border-color:#e84545}
"""
CSS = css("#8b93a1", "#c8cdd6", "#0b0c0e", "#141619", "#242830", EXTRA)

BODY = """@@MAST@@
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="big">
<div class="card c-cy">
<div class="kick">&#9880; The Cyber Wire &middot; The Wire</div>
<h3>Routers are being taken over by attackers who got a head start on the patch</h3>
<p>An SSH authentication bypass in MikroTik RouterOS, chained for full administrative takeover and exploited in the wild since 2 September, is now the most urgent unpatched exposure on the internet-facing edge, with more than 122,000 devices showing exposed SSH interfaces.</p>
<a class="go" href="cyber-briefing.html">Read the briefing &rarr;</a>
</div>
<div class="card c-ws">
<div class="kick">&#9650; The Closing Bell &middot; The Tape</div>
<h3>Two unrelated shocks, one lower market</h3>
<p>Stocks are lower across the board into Tuesday afternoon with the Dow much the weakest of the three, as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags the health care sector down more than 2%.</p>
<a class="go" href="wallstreet-briefing.html">Read the briefing &rarr;</a>
</div>
<div class="card c-mm">
<div class="kick">&#8856; The Octagon &middot; Tale of the Tape</div>
<h3>A win on Saturday, off the rankings by Monday</h3>
<p>Michael Page has been pulled from the UFC rankings less than two days after winning at UFC Paris with a release reportedly looming, while Valentina Shevchenko has been stripped of the women&#39;s flyweight title after telling the promotion she would be unable to compete for at least a year.</p>
<a class="go" href="mma-briefing.html">Read the briefing &rarr;</a>
</div>
</div>

<h2 class="sec">About these briefings</h2>
<div class="panel">
<p style="margin:0 0 9px">Three briefings, rebuilt from live web search every thirty minutes between 8 AM and 6 PM Eastern. Each page carries its own as-of stamp, its own source list, and its own record of what it refused to publish and why.</p>
<p style="margin:0" class="note">Nothing on any of these pages is fetched first-hand; everything is compiled from public reporting gathered during the run that produced it. Where two sources disagreed, both reads are shown rather than averaged. Point-in-time snapshots of every edition are kept in the <a href="archive.html">Archive</a>. The markets page is information only and is not investment advice.</p>
</div>
"""

BODY = (BODY.replace("@@MAST@@", masthead("Daily Briefings", "Security, markets and MMA &mdash; refreshed every 30 minutes, 8 AM&ndash;6 PM ET"))
            .replace("@@NAV@@", nav("index")))

html = page("Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
print("index ok", len(html))
