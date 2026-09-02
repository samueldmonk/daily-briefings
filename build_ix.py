# -*- coding: utf-8 -*-
# index.html is generated FROM the three pages' own summary strings so the cards
# are byte-identical to the strips they echo.
import shared, io, re

def grab(path):
    h = io.open(path, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', h, re.S)
    if not m:
        raise SystemExit("no tldr in " + path)
    return m.group(1)

CY = grab("cyber-briefing.html")
WS = grab("wallstreet-briefing.html")
MM = grab("mma-briefing.html")

EXTRA = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.big .card{padding:20px 22px;display:flex;flex-direction:column}
.big .card .kicker{font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  margin-bottom:9px}
.big .card h3{font-size:24px;margin:0 0 4px;letter-spacing:-.01em}
.big .card .sub{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);margin-bottom:12px}
.big .card p{flex:1;font-size:15px;color:#cfc9c2;margin:0 0 15px}
.big .card .go{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase}
.c-cy{border-top:3px solid #22d3a8} .c-cy .kicker,.c-cy .go,.c-cy h3{color:#22d3a8}
.c-cy:hover{border-color:#22d3a8}
.c-ws{border-top:3px solid #caa64a} .c-ws .kicker,.c-ws .go{color:#caa64a}
.c-ws h3{font-family:Georgia,'Times New Roman',serif;color:#e8c766}
.c-ws:hover{border-color:#caa64a}
.c-mm{border-top:3px solid #e84545} .c-mm .kicker,.c-mm .go,.c-mm h3{color:#ff8a5c}
.c-mm:hover{border-color:#e84545}
"""

body = []
A = body.append
A('<header class="mast">')
A('<h1>Daily Briefings</h1>')
A('<p class="tag">Three desks, refreshed through the day &mdash; security, markets and mixed martial arts</p>')
A(shared.META)
A('</header>')
A('<p class="freshline" id="freshline">&nbsp;</p>')
A(shared.nav("index", "#c9c2b8"))

A('<div class="big">')
A(f'''<div class="card c-cy">
<div class="kicker">&#9960; Security</div>
<h3>The Cyber Wire</h3>
<div class="sub">The Wire</div>
<p>{CY}</p>
<a class="go" href="cyber-briefing.html">Read the briefing &rarr;</a>
</div>''')
A(f'''<div class="card c-ws">
<div class="kicker">&#9650; Markets</div>
<h3>The Closing Bell</h3>
<div class="sub">The Tape</div>
<p>{WS}</p>
<a class="go" href="wallstreet-briefing.html">Read the briefing &rarr;</a>
</div>''')
A(f'''<div class="card c-mm">
<div class="kicker">&#8856; MMA</div>
<h3>The Octagon</h3>
<div class="sub">Tale of the Tape</div>
<p>{MM}</p>
<a class="go" href="mma-briefing.html">Read the briefing &rarr;</a>
</div>''')
A('</div>')

A('<h2 class="sec" style="color:#c9c2b8">About this edition</h2>')
A('<div class="panel">')
A('<p style="margin:0 0 10px">Each briefing is rebuilt from live web searches every thirty minutes between '
  '8 AM and 6 PM Eastern. Every claim, figure and name on these pages is checked against a source fetched in '
  'the same run; anything that cannot be verified is dropped, and where sources disagree the disagreement is '
  'printed rather than resolved silently.</p>')
A('<p style="margin:0"><a href="archive.html">Browse the archive &rarr;</a> &mdash; every past edition is kept '
  'as a point-in-time snapshot for three weeks.</p>')
A('</div>')

A('<footer>')
A('<p style="margin:0">Compiled from public reporting. Nothing here is investment advice, and security '
  'guidance should be verified against the relevant vendor advisory and the CISA KEV catalog. Full source '
  'lists appear at the foot of each briefing.</p>')
A('</footer>')

html = shared.page("Daily Briefings", "#c9c2b8", "#e9e6e1",
                   "#0d0d0e", "#151517", "#26262a", "\n".join(body), EXTRA)
io.open("index.html", "w", encoding="utf-8").write(html)
print("index ok", len(html))
