# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from build_1530 import S_CY, S_WS, S_MMA, FRESH

OUT = os.path.dirname(os.path.abspath(__file__))
EXTRA = """
.big{display:grid;grid-template-columns:1fr;gap:16px;margin-top:6px}
@media(min-width:820px){.big{grid-template-columns:repeat(3,1fr)}}
.bc{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 21px;transition:.17s;
  display:flex;flex-direction:column}
.bc:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.36)}
.bc .kk{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:9px}
.bc h3{margin:0 0 10px;font-size:21px;line-height:1.22}
.bc p{margin:0 0 16px;font-size:14.5px;color:#cfcbc6;line-height:1.55;flex:1}
.bc .go{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.bc.cy{border-top:3px solid #22d3a8} .bc.cy .kk,.bc.cy .go{color:#22d3a8} .bc.cy:hover{border-color:#22d3a8}
.bc.ws{border-top:3px solid #caa64a} .bc.ws .kk,.bc.ws .go{color:#caa64a} .bc.ws:hover{border-color:#caa64a}
.bc.ws h3{font-family:Georgia,'Times New Roman',serif}
.bc.mm{border-top:3px solid #e84545} .bc.mm .kk,.bc.mm .go{color:#e84545} .bc.mm:hover{border-color:#e84545}
"""
CSS = css("#9aa7b4", "#c3ced9", "#0b0c0d", "#141618", "#252a2e", EXTRA)

BODY = """@@MAST@@
@@FRESH@@
@@NAV@@

<div class="big">

<a class="bc cy" href="cyber-briefing.html">
<div class="kk">&#9960; The Cyber Wire &middot; The Wire</div>
<h3>Record Patch Tuesday, two exploited Windows zero-days</h3>
<p>@@SCY@@</p>
<div class="go">Read the briefing &rarr;</div>
</a>

<a class="bc ws" href="wallstreet-briefing.html">
<div class="kk">&#9650; The Closing Bell &middot; The Tape</div>
<h3>The four-day slide ends as oil retreats and CPI lands in line</h3>
<p>@@SWS@@</p>
<div class="go">Read the briefing &rarr;</div>
</a>

<a class="bc mm" href="mma-briefing.html">
<div class="kk">&#8856; The Octagon &middot; Tale of the Tape</div>
<h3>Thirteen bouts, no misses: Noche UFC makes weight in Glendale</h3>
<p>@@SMM@@</p>
<div class="go">Read the briefing &rarr;</div>
</a>

</div>

<p class="disc">Three briefings, rebuilt from live sources every 30 minutes between 8 AM and 6 PM ET. Each page carries its own sources and as-of times; every claim traces to a source fetched during that run or to a standing sourced correction. Point-in-time snapshots of previous editions are kept in the <a href="archive.html">Archive</a>. Market content is information, not investment advice.</p>
"""

BODY = (BODY.replace("@@MAST@@", masthead("Daily Briefings", "Cybersecurity, markets and MMA &mdash; compiled fresh from live sources"))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("index"))
            .replace("@@SCY@@", S_CY).replace("@@SWS@@", S_WS).replace("@@SMM@@", S_MMA))

io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
    page("Daily Briefings", CSS, BODY))
print("index ok")
