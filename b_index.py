# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
EXTRA = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px;margin-top:6px}
.bcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 21px;transition:.16s;
  display:flex;flex-direction:column}
.bcard:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.4)}
.bcard .kick{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:9px}
.bcard h2{margin:0 0 4px;font-size:22px;letter-spacing:-.3px}
.bcard .sub2{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:12px}
.bcard p{margin:0 0 16px;font-size:14.5px;color:#cfcbc6;line-height:1.55;flex:1}
.bcard a.read{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase}
.bcard.cy{border-top:3px solid #22d3a8}.bcard.cy .kick,.bcard.cy a.read{color:#22d3a8}
.bcard.mk{border-top:3px solid #caa64a}.bcard.mk .kick,.bcard.mk a.read{color:#caa64a}
.bcard.mk h2{font-family:Georgia,'Times New Roman',serif}
.bcard.mm{border-top:3px solid #e84545}.bcard.mm .kick,.bcard.mm a.read{color:#e84545}
"""
CSS = css("#9aa7b4", "#c8d2dc", "#0b0c0e", "#14171a", "#242a30", EXTRA)

BODY = """
%s
<div class="freshline" id="freshline">&nbsp;</div>
%s

<div class="big">

<div class="bcard cy">
<div class="kick">&#9960; The Cyber Wire &middot; The Wire</div>
<h2>Two maximum-severity flaws in play at once</h2>
<div class="sub2">Breaches &middot; Exploits &middot; Federal deadlines</div>
<p>Adobe&#39;s maximum-severity Magento flaw CVE-2026-75650 remains the day&#39;s defining incident with exploitation running since 4 September, and SAP has just patched a second CVSS 10.0 flaw of its own &mdash; while three federal remediation deadlines stay open, the nearest in six days.</p>
<a class="read" href="cyber-briefing.html">Read the briefing &rarr;</a>
</div>

<div class="bcard mk">
<div class="kick">&#9650; The Closing Bell &middot; The Tape</div>
<h2>Lower across the board, with the Dow worst hit</h2>
<div class="sub2">Indices &middot; Movers &middot; Rates &middot; Calendar</div>
<p>Stocks are lower across the board in Tuesday morning trade with the Dow much the weakest of the three, as a renewed crude rally lifts energy to the top of the board and Canada&#39;s retaliatory tariffs on about $20 billion of U.S. goods take effect.</p>
<a class="read" href="wallstreet-briefing.html">Read the briefing &rarr;</a>
</div>

<div class="bcard mm">
<div class="kick">&#8856; The Octagon &middot; Tale of the Tape</div>
<h2>A UFC main card goes free on CBS</h2>
<div class="sub2">UFC &middot; Prospects &middot; The business of fighting</div>
<p>UFC 332 on 3 October will put its entire main card live and free on CBS for the first time ever, headlined by Nat&aacute;lia Silva against Wang Cong for the vacant women&#39;s flyweight title.</p>
<a class="read" href="mma-briefing.html">Read the briefing &rarr;</a>
</div>

</div>

<p class="disc">Three briefings, rebuilt from live sources every thirty minutes between 8 AM and 6 PM Eastern. Each page carries its own sources and its own as-of time; point-in-time snapshots of every edition are kept in the <a href="archive.html">Archive</a>. Nothing on these pages is investment advice or security advice for any specific environment.</p>
""" % (masthead("Daily Briefings", "Security, markets and mixed martial arts &mdash; refreshed through the day"), nav("index"))

html = page("Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)
print("index ok", len(html))
