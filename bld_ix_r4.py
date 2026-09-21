# -*- coding: utf-8 -*-
import io, re, common_r4 as C

OUT = "/sessions/youthful-bold-tesla/mnt/outputs/index.html"
BASE = "/sessions/youthful-bold-tesla/mnt/outputs/"

def tldr_of(fn):
    s = io.open(BASE + fn, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', s, re.S)
    return m.group(1)

CY = tldr_of("cyber-briefing.html")
WS = tldr_of("wallstreet-briefing.html")
MM = tldr_of("mma-briefing.html")

CARDS = [
    ("#22d3a8", "&#9960; The Cyber Wire &middot; The Wire", "Security", CY, "cyber-briefing.html", ""),
    ("#caa64a", "&#9650; The Closing Bell &middot; The Tape", "Markets", WS, "wallstreet-briefing.html",
     ";font-family:Georgia,'Times New Roman',serif"),
    ("#e84545", "&#8856; The Octagon &middot; Tale of the Tape", "MMA", MM, "mma-briefing.html", ""),
]

b = []
b.append(C.head("Daily Briefings", "index"))
b.append(C.masthead("Daily Briefings", "Three desks, rebuilt from live sources every 30 minutes"))
b.append(C.META)
b.append('<div class="freshline" id="freshline">&nbsp;</div>')
b.append(C.nav("index"))
b.append('<div class="bigcards">')
for colour, kicker, h3, summary, href, extra in CARDS:
    b.append('<div class="bigcard" style="border-left:3px solid %s">'
             '<div class="kic" style="color:%s">%s</div>'
             '<h3 style="color:%s%s">%s</h3><p>%s</p>'
             '<a class="go" style="color:%s" href="%s">Read the briefing &rarr;</a></div>'
             % (colour, colour, kicker, colour, extra, h3, summary, colour, href))
b.append('</div>')
b.append(C.sec("How these pages are made"))
b.append('<div class="panel"><p style="margin:0 0 10px;font-size:14.5px">Every edition is rebuilt from live web '
         'searches run at publication time. Nothing appears on these pages unless a source fetched in that same run '
         'states it, or a standing correction in this desk&rsquo;s own record covers it. Where two sources disagree, '
         'both readings are printed and named rather than averaged into one number; where a figure could not be '
         'verified, the page says so instead of guessing.</p>'
         '<p style="margin:0;font-size:14.5px" class="mut">Editions are snapshotted to the '
         '<a href="archive.html" style="color:inherit">Archive</a> and kept for 21 days.</p></div>')
b.append('<footer><div class="dv">Daily Briefings</div><div class="srcs">Each briefing carries its own sourced '
         'footnotes and disclaimers. Market figures are information only and not investment advice; security '
         'deadlines should be verified against your own vendor advisories; fight cards are subject to change.'
         '</div></footer>')
b.append(C.TAIL)

io.open(OUT, "w", encoding="utf-8").write("".join(b))
print("wrote", OUT)
