# -*- coding: utf-8 -*-
import shared, io

extra = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}
.big .card{padding:20px 21px;border-top:3px solid var(--line)}
.big .card.cy{border-top-color:#22d3a8}
.big .card.ws{border-top-color:#caa64a}
.big .card.mm{border-top-color:#e84545}
.big .kicker{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:9px}
.big .cy .kicker{color:#22d3a8} .big .ws .kicker{color:#caa64a} .big .mm .kicker{color:#e84545}
.big .card h3{font-size:17px;margin:0 0 10px}
.big .ws h3{font-family:Georgia,'Times New Roman',serif;font-weight:600}
.big .card p{font-size:14.5px;color:#d4d0cb;margin:0 0 14px}
.rd{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase}
.big .cy:hover{border-color:#22d3a8}.big .ws:hover{border-color:#caa64a}.big .mm:hover{border-color:#e84545}
"""
css = shared.css("#9aa0a6", "#c9c4be", "#0c0c0e", "#161619", "#28282d", extra)

CY = ("A maximum-severity SonicWall SMA 1000 flaw is confirmed exploited in the wild and can be "
      "chained to remote code execution, while a Chromium V8 zero-day carries a September 18 federal "
      "patch deadline — and Unit 42 has published the anatomy of an AI-directed intrusion that took "
      "root in under ten hours.")
WS = ("U.S. markets are closed for the Labor Day long weekend after a hot August jobs report "
      "knocked the three major indexes lower on Friday and pushed bets on a September Fed rate "
      "hike back toward a coin flip; the next session opens Tuesday, September 8.")
MM = ("Salahdine Parnasse stopped Dan Hooker in the first round of his UFC debut in Paris, took "
      "Performance of the Night and called for Max Holloway — and UFC.com says the win puts him "
      "straight into the lightweight top 15.")

b = io.StringIO(); w = b.write
w(shared.masthead("Daily Briefings", "Security, markets and MMA — verified fresh, every half hour"))
w('<div class="freshline" id="freshline">&nbsp;</div>')
w(shared.nav("index"))

w('<div class="big">')
w(f'<a class="card cy" href="cyber-briefing.html" style="display:block;color:inherit">'
  f'<div class="kicker">⛨ The Cyber Wire &middot; The Wire</div>'
  f'<h3>Today’s security briefing</h3><p>{CY}</p>'
  f'<span class="rd" style="color:#22d3a8">Read the briefing →</span></a>')
w(f'<a class="card ws" href="wallstreet-briefing.html" style="display:block;color:inherit">'
  f'<div class="kicker">▲ The Closing Bell &middot; The Tape</div>'
  f'<h3>Today’s markets briefing</h3><p>{WS}</p>'
  f'<span class="rd" style="color:#caa64a">Read the briefing →</span></a>')
w(f'<a class="card mm" href="mma-briefing.html" style="display:block;color:inherit">'
  f'<div class="kicker">⊘ The Octagon &middot; Tale of the Tape</div>'
  f'<h3>Today’s MMA briefing</h3><p>{MM}</p>'
  f'<span class="rd" style="color:#e84545">Read the briefing →</span></a>')
w('</div>')

w('<h2 class="sec">About this page</h2>')
w('<div class="panel"><p style="margin:0">Three briefings, rebuilt from live web searches every thirty '
  'minutes between 8 AM and 6 PM Eastern. Every claim on every page is checked against a source fetched '
  'during that same run, or against a standing corrections file kept in the publishing repository; anything '
  'that cannot be verified is dropped, and the pages say so where a figure is deliberately withheld. Past '
  'editions are kept in the <a href="archive.html">Archive</a>.</p></div>')

w('<div class="disc">Nothing here is investment, legal or security advice. Market figures are the most '
  'recent verified close or the stated intraday reading; fight cards are subject to change; security items '
  'are a news summary, not an advisory — act on the vendor bulletin and the CISA KEV catalog directly.</div>')

html = shared.page("Daily Briefings", css, b.getvalue())
open("/tmp/build_1788656196/out/index.html","w",encoding="utf-8").write(html)
print("ix bytes", len(html))
