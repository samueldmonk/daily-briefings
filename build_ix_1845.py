# -*- coding: utf-8 -*-
import io, re, common

# Pull each page's tldr sentence so the index cards are byte-identical to them.
def tldr_of(path):
    h = io.open(path, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', h, re.S)
    assert m, path
    return m.group(1)

CY = tldr_of("cyber-briefing.html")
WS = tldr_of("wallstreet-briefing.html")
MM = tldr_of("mma-briefing.html")

p = []
p.append(common.head("Daily Briefings", "index"))
p.append(common.masthead("Daily Briefings",
         "Three desks, refreshed through the day &mdash; security, markets and the fight game"))
p.append(common.META)
p.append('<div class="freshline" id="freshline">&nbsp;</div>')
p.append(common.nav("index"))

p.append('<div class="bigcards">')
p.append('<div class="bigcard" style="border-left:3px solid #22d3a8">'
         '<div class="kic" style="color:#22d3a8">&#9960; The Cyber Wire &middot; The Wire</div>'
         '<h3>Breaches, bugs and what to patch first</h3>'
         '<p>%s</p>'
         '<a class="go" style="color:#22d3a8" href="cyber-briefing.html">Read the briefing &rarr;</a>'
         '</div>' % CY)
p.append('<div class="bigcard" style="border-left:3px solid #caa64a">'
         '<div class="kic" style="color:#caa64a">&#9650; The Closing Bell &middot; The Tape</div>'
         '<h3 style="font-family:Georgia,\'Times New Roman\',serif">The tape, the drivers and what&rsquo;s next</h3>'
         '<p>%s</p>'
         '<a class="go" style="color:#caa64a" href="wallstreet-briefing.html">Read the briefing &rarr;</a>'
         '</div>' % WS)
p.append('<div class="bigcard" style="border-left:3px solid #e84545">'
         '<div class="kic" style="color:#e84545">&#8856; The Octagon &middot; Tale of the Tape</div>'
         '<h3>UFC, prospects &amp; the business of fighting</h3>'
         '<p>%s</p>'
         '<a class="go" style="color:#e84545" href="mma-briefing.html">Read the briefing &rarr;</a>'
         '</div>' % MM)
p.append('</div>')

p.append(common.sec("How this desk works"))
p.append('<div class="panel"><ul class="bul">'
         '<li>Every figure on every page is checked against a source fetched on the run that published '
         'it, or against a sourced entry in this desk&rsquo;s standing corrections file. Anything that '
         'fails that test is dropped.</li>'
         '<li>Where two credible readings of the same number disagree, the disagreement is printed and '
         'named rather than quietly resolved &mdash; and where a figure is refused outright, the page '
         'says which figure and why.</li>'
         '<li>Items carried from an earlier edition rather than re-verified on the current run are '
         'labelled as carried.</li>'
         '<li>Every edition is snapshotted to the <a href="archive.html" style="color:#9aa7b8">archive</a>, '
         'which keeps 21 days of point-in-time pages.</li>'
         '</ul></div>')

p.append(common.footer(
    "Three briefings, rebuilt every 30 minutes between 8 AM and 6 PM Eastern. Markets content is for "
    "information only and not investment advice; security content is not security advice for any "
    "particular environment; fight cards and bouts are subject to change."))
p.append(common.TAIL)

html = "".join(p)
io.open("index.html", "w", encoding="utf-8").write(html)
print("index ok", len(html))
