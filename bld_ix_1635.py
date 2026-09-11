# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1635 import S_CY, S_WS, S_MMA, FRESH

OUT = os.path.dirname(os.path.abspath(__file__))
EXTRA = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px;margin-top:6px}
.bcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 21px;transition:.16s;
  display:flex;flex-direction:column}
.bcard:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.4)}
.bcard .kick{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:9px}
.bcard h3{margin:0 0 10px;font-size:21px;line-height:1.24}
.bcard p{margin:0 0 16px;font-size:14.5px;color:#cfcbc6;flex:1}
.bcard .go{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase}
.c-cy{border-top:3px solid #22d3a8} .c-cy .kick,.c-cy .go{color:#22d3a8} .c-cy:hover{border-color:#22d3a8}
.c-ws{border-top:3px solid #caa64a} .c-ws .kick,.c-ws .go{color:#caa64a} .c-ws:hover{border-color:#caa64a}
.c-ws h3{font-family:Georgia,'Times New Roman',serif}
.c-mma{border-top:3px solid #e84545} .c-mma .kick,.c-mma .go{color:#e84545} .c-mma:hover{border-color:#e84545}
"""
CSS = css("#9aa8ff", "#c3cbff", "#0b0c10", "#14161c", "#242833", EXTRA)

CARDS = [
 ("c-cy", "&#9960; The Cyber Wire &middot; The Wire", "Breaches, exploited flaws and the federal patch clock",
  S_CY, "cyber-briefing.html"),
 ("c-ws", "&#9650; The Closing Bell &middot; The Tape", "Markets, movers and the macro calendar",
  S_WS, "wallstreet-briefing.html"),
 ("c-mma", "&#8856; The Octagon &middot; Tale of the Tape", "UFC, prospects and the business of fighting",
  S_MMA, "mma-briefing.html"),
]

body = [
    masthead("Daily Briefings", "Three desks, refreshed every 30 minutes from 8 AM to 6 PM Eastern"),
    FRESH,
    nav("index"),
    '<div class="big">',
]
for cls, kick, sub, summ, href in CARDS:
    body.append(
        '<a class="bcard %s" href="%s" style="text-decoration:none;color:inherit">'
        '<div class="kick">%s</div><h3>%s</h3><p>%s</p>'
        '<div class="go">Read the briefing &rarr;</div></a>' % (cls, href, kick, sub, summ))
body.append('</div>')
body.append('<p class="disc">Each briefing is rebuilt from live sources on every run; nothing is carried forward '
            'unverified. Figures carry the time of the read that produced them. The Closing Bell is information only '
            'and is not investment advice.</p>')

html = page("Daily Briefings", CSS, "\n".join(body))
io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
print("ix ok", len(html))
