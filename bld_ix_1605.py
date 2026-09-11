# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1605 import S_CY, S_WS, S_MMA, FRESH

OUT = os.path.dirname(os.path.abspath(__file__))
EXTRA = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}
.big .card{padding:20px 21px}
.big .kicker{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:9px}
.big .card h3{font-size:21px;margin:0 0 11px;line-height:1.28}
.big .card p{font-size:14.5px;color:#cfcbc6;margin:0 0 14px}
.big .go{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase}
.c-sec{border-left:3px solid #22d3a8}
.c-sec .kicker,.c-sec .go{color:#22d3a8}
.c-sec:hover{border-color:#22d3a8}
.c-mkt{border-left:3px solid #caa64a}
.c-mkt .kicker,.c-mkt .go{color:#caa64a}
.c-mkt h3{font-family:Georgia,'Times New Roman',serif}
.c-mkt:hover{border-color:#caa64a}
.c-mma{border-left:3px solid #e84545}
.c-mma .kicker,.c-mma .go{color:#e84545}
.c-mma:hover{border-color:#e84545}
"""
CSS = css("#9aa6b2", "#c3cdd8", "#0a0b0d", "#141619", "#242830", EXTRA)

CARDS = [
 ("c-sec", "⛨ The Cyber Wire &middot; The Wire", "Security", S_CY, "cyber-briefing.html"),
 ("c-mkt", "▲ The Closing Bell &middot; The Tape", "Markets", S_WS, "wallstreet-briefing.html"),
 ("c-mma", "⊘ The Octagon &middot; Tale of the Tape", "MMA", S_MMA, "mma-briefing.html"),
]


def cards():
    out = ['<div class="big">']
    for cls, kicker, title, summary, href in CARDS:
        out.append('<div class="card %s"><div class="kicker">%s</div><h3>%s</h3><p>%s</p>'
                   '<a class="go" href="%s">Read the briefing &rarr;</a></div>'
                   % (cls, kicker, title, summary, href))
    out.append('</div>')
    return "".join(out)


BODY = """@@MAST@@
@@FRESH@@
@@NAV@@

@@CARDS@@

<h2 class="sec">About these briefings</h2>
<div class="panel">
<p style="margin:0 0 10px">Three briefings, rebuilt from live web searches every thirty minutes between 8 AM and
6 PM Eastern. Each one leads with the single most important thing that has changed since the last edition, and every
figure on every page is carried only if a source read for that edition states it.</p>
<p style="margin:0">Earlier editions are kept as point-in-time snapshots in the <a href="archive.html">Archive</a>, so
you can see what the page said at any given hour rather than only what it says now.</p>
</div>
"""

body = (BODY.replace("@@MAST@@", masthead("Daily Briefings", "Security, markets and the fight game &mdash; refreshed every thirty minutes"))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("index"))
            .replace("@@CARDS@@", cards()))

html = page("Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
print("index ok", len(html))
