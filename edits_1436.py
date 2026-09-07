# -*- coding: utf-8 -*-
"""Edition 2026-09-07-1436 (Midday, Labor Day). Targeted edits onto the 1419 pages."""
import re, sys, os

REPO = sys.argv[1]
P = lambda n: os.path.join(REPO, n)

def rd(n): return open(P(n), encoding="utf-8").read()
def wr(n, s): open(P(n), "w", encoding="utf-8").write(s)

report = []
def sub(tag, hay, old, new, count=0):
    if old not in hay:
        report.append("MISS  %s" % tag)
        return hay
    n = hay.count(old) if count == 0 else count
    report.append("ok    %s  (x%d)" % (tag, n))
    return hay.replace(old, new) if count == 0 else hay.replace(old, new, count)

# ---------------------------------------------------------------- provenance
# Demote every inherited "this edition"/"this run" claim to the edition that made it.
DEMOTE = [
    ("this edition", "the 2:15 edition"),
    ("this run", "the 2:15 run"),
    ("This edition", "The 2:15 edition"),
]

def demote(h):
    n = 0
    for a, b in DEMOTE:
        n += h.count(a)
        h = h.replace(a, b)
    return h, n

# ================================================================ WALL STREET
WS = rd("wallstreet-briefing.html")
WS, n = demote(WS); report.append("ok    ws demote (x%d)" % n)

# --- new item: the rest of the futures complex has now halted too -----------
NEW_WS = (
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t">Holiday session</span></div>\n'
'<h3>The oil tape has stopped too &mdash; and now the whole ticker is static</h3>\n'
'<p>Since the 12:16 edition this page has carried one holiday halt: <b>CME equity-index futures at 12:00 p.m. Central, 1:00 PM ET</b>, sourced from CME. A holiday-schedule return read this edition puts <b>two more</b> alongside it, and both are also now in the past. The return lists <b>ICE Brent crude futures concluding at 01:30 on 8 September UTC+8</b> and <b>CME precious metals and U.S. crude perpetual futures at 02:30 on 8 September UTC+8</b>, against <b>01:00 UTC+8</b> for equity index. '
'<b>Converting UTC+8 to Eastern is this desk&rsquo;s arithmetic, not the source&rsquo;s</b> &mdash; but it is checkable arithmetic, because the third figure converts to a time this page already holds from CME itself: <b>01:00 UTC+8 on 8 September is 1:00 PM ET on 7 September</b>, exactly the equity halt already published here. On the same conversion, <b>Brent stopped at about 1:30 PM ET</b> and <b>CME crude at about 2:30 PM ET</b>. '
'<b>The consequence is the point.</b> The <b>live ticker at the top of this page</b> carries the three U.S. indices, <b>WTI crude</b> and the <b>US 10-year</b>; with equities shut all day, the bond market shut all day, and now both crude contracts halted, <b>every instrument on that strip is displaying a last matched price rather than a live market</b>. Earlier editions could say that of the equity symbols only. <span class="mut">The times are the return&rsquo;s and the conversion is this desk&rsquo;s; the exchange and broker schedules remain the authority and readers should check them directly rather than rely on a relayed time. Nothing here asserts a level or a move for any futures session.</span></p>\n'
'</div>\n'
)

anchor_ws = '<div class="card">'
i = WS.find('Movers &amp; Drivers')
j = WS.find(anchor_ws, i)
if i > 0 and j > 0:
    WS = WS[:j] + NEW_WS + WS[j:]
    report.append("ok    ws new card inserted")
else:
    report.append("MISS  ws new card anchor")

# --- eighth Brent reading ---------------------------------------------------
OLD_BR = 'roughly $97.27 to $97.50, up about 1.0&ndash;1.2%'
NEW_BR = 'roughly $97.27 to $97.68, up about 1.0&ndash;1.45%'
WS = sub("ws brent range (tldr+body)", WS, OLD_BR, NEW_BR)

BR_NOTE = (
'<p class="note"><b>An eighth Brent reading, and it widens the range upward without breaking it.</b> '
'A return read this edition puts Brent <b>up 1.45% at $97.68</b> alongside the <b>$97.39, up 1.15%</b> this page already carries &mdash; both in the same return, the second of them last. '
'$97.68 sits <b>above the $97.50 top of the range this page had generalised</b>, so the range is restated as <b>roughly $97.27 to $97.68</b>. '
'It is <b>not</b> published as a new high: the intraday touch on this page remains <b>$97.93</b>, reached by two independent routes, and <b>$97.68 is below it</b>. '
'<b>No single Brent level is asserted for today</b> &mdash; that refusal, now in its twenty-eighth consecutive edition, stands, and the Bloomberg reading of <b>$96.15, down 0.1%</b> in the early hours remains the other end of a two-way session.</p>\n'
)
k = WS.find('</p>', WS.find('Rates, Bonds &amp; Commodities'))
if k > 0:
    k = WS.find('</p>', k) + 4
    WS = WS[:k] + BR_NOTE + WS[k:]
    report.append("ok    ws brent note inserted")
else:
    report.append("MISS  ws brent note anchor")

# --- tldr: lead with what changed on the screen -----------------------------
OLD_T = 'U.S. stock and bond markets are shut all day for Labor Day and reopen at 9:30&nbsp;AM ET Tuesday, so the only markets with news in them today are energy ones'
NEW_T = 'U.S. stock and bond markets are shut all day for Labor Day and reopen at 9:30&nbsp;AM ET Tuesday, and as of this edition <b>the oil futures that were still trading have halted as well &mdash; ICE Brent at about 1:30 PM ET and CME crude at about 2:30 PM ET on a relayed schedule &mdash; so every symbol on the live ticker at the top of this page is now showing a last matched price rather than a live market</b>; the only markets with news in them today are energy ones'
WS = sub("ws tldr", WS, OLD_T, NEW_T)

wr("wallstreet-briefing.html", WS)

# ====================================================================== CYBER
CY = rd("cyber-briefing.html")
CY, n = demote(CY); report.append("ok    cy demote (x%d)" % n)

NEW_CY = (
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t">Law enforcement</span><span class="t">Historical campaign</span></div>\n'
'<h3>A ten-year-old Excel campaign reaches a San Francisco courtroom</h3>\n'
'<p><b>This is an indictment, not an intrusion, and the distinction is the item.</b> The U.S. Department of Justice has charged <b>Searzhudin Tamirlanovich Aktulaev</b>, <b>40</b>, a Russian national <b>arrested in Cyprus in May 2025</b> and <b>extradited on 28 August</b>; he made his <b>initial appearance in federal court in San Francisco on 31 August</b> and was remanded to custody. '
'The conduct charged ran <b>from at least June 2016 through November 2017</b>: Aktulaev and co-conspirators are alleged to have built roughly <b>255 fake accounts</b> on a well-known freelance-work platform <b>headquartered in Northern California</b>, posed as prospective clients, and messaged about <b>80,000 of its users</b> with <b>malicious Microsoft Excel attachments</b>. Opening one prompted the victim to <b>enable a macro</b>, which downloaded malware. '
'The payloads named are <b>TVRAT</b> (also tracked as <b>TeamSPy</b> and <b>TVSPY</b>) and <b>DarkVNC</b>, giving remote control through <b>TeamViewer</b> and <b>VNC Viewer</b> respectively. Charges include <b>conspiracy, transmission of malicious code and aggravated identity theft</b>. '
'<span class="mut"><b>Nothing here is a live threat and this desk publishes no patch, no CVE, no CVSS and no deadline for it</b> &mdash; the campaign ended nine years ago and the news is the prosecution. It is carried because macro-borne Excel lures against gig-work platforms are still a current technique, not because this operation is running. The platform is not named in the returns read this edition, so it is not named here. Reported by The Hacker News, BleepingComputer, Help Net Security and Infosecurity Magazine; none was fetched first-hand.</span></p>\n'
'</div>\n'
)

i = CY.find('Breaches &amp; Incidents')
j = CY.find('<div class="card">', i)
if i > 0 and j > 0:
    CY = CY[:j] + NEW_CY + CY[j:]
    report.append("ok    cy new card inserted")
else:
    report.append("MISS  cy new card anchor")

wr("cyber-briefing.html", CY)

# ======================================================================== MMA
MM = rd("mma-briefing.html")
MM, n = demote(MM); report.append("ok    mma demote (x%d)" % n)

NEW_MMA = (
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t">Signing</span></div>\n'
'<div class="dv">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>\n'
'<h3>Roberto Soldic signs, and debuts at UFC&nbsp;332</h3>\n'
'<p><b>Roberto Soldic</b>, <b>31</b>, the Croatian knockout puncher nicknamed <b>&ldquo;Robocop&rdquo;</b>, has signed a <b>multi-fight UFC contract</b> and will make his octagon debut against <b>Khaos Williams</b> at <b>UFC&nbsp;332</b>, the <b>3 October</b> card at the <b>Delta Center in Salt Lake City</b> this page already carries. He enters at <b>welterweight</b> per his UFC.com profile, with a record given as <b>21&ndash;4, 18 by knockout</b>. '
'He is a <b>former two-division KSW champion</b> &mdash; welterweight and middleweight &mdash; who <b>declared free agency after leaving ONE Championship in August</b>, where returns put him at <b>1&ndash;1 with one no contest</b>. '
'<span class="mut"><b>One widely repeated line is worth stating precisely.</b> Headlines describe Soldic as the man who knocked out <b>Dricus Du Plessis</b>; the fuller returns have them meeting <b>twice</b> in KSW and finishing <b>1&ndash;1</b>, with <b>each man scoring a knockout</b>. This page prints the series, not the half of it that travels. Williams is <b>32</b> and <b>16&ndash;5</b> overall, <b>7&ndash;4</b> in the UFC across eleven promotional fights, and comes in off a <b>first-round knockout in May</b>. <b>No odds were printed in any return, so none is published.</b> Reported by Bloody Elbow (4 September), Yahoo Sports, MMA Weekly, MMA Mania, BJPenn and MiddleEasy; none was fetched first-hand. Neither man is called a contender or a challenger, because no ranking or title implication was stated.</span></p>\n'
'</div>\n'
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t">Booking</span></div>\n'
'<div class="dv">Sat 14 Nov &middot; Madison Square Garden, New York</div>\n'
'<h3>UFC&nbsp;334 gets its first bout</h3>\n'
'<p><b>Nazim Sadykhov</b> meets <b>Jefferson Nascimento</b> at <b>lightweight</b> &mdash; the <b>first fight booked</b> for <b>UFC&nbsp;334</b> at <b>Madison Square Garden</b> on <b>14 November</b>, and the first November date to appear on this page. Sadykhov announced it himself on Instagram before the promotion did. '
'<span class="mut">Reported by Bloody Elbow (3 September), Sports Illustrated, Sherdog, Yahoo Sports, Heavy and MiddleEasy; none was fetched first-hand. <b>No records, no rankings and no odds are printed</b> &mdash; one return attaches an &ldquo;11&ndash;1 former MMA champion&rdquo; line to the booking without stating unambiguously which man it describes, so this desk publishes neither the record nor the title claim rather than guess between them. <b>No main event has been announced for this card</b>, and none is implied here.</span></p>\n'
'</div>\n'
)

i = MM.find('Fight Week &mdash; Upcoming Cards')
j = MM.find('<div class="card">', i)
if i > 0 and j > 0:
    MM = MM[:j] + NEW_MMA + MM[j:]
    report.append("ok    mma new cards inserted")
else:
    report.append("MISS  mma new card anchor")

OLD_M = 'the one new item this edition is not a card at all'
OLD_M2 = 'the one new item the 2:15 edition is not a card at all'
NEW_M = 'the two new items this edition are both roster news &mdash; <b>Roberto Soldic</b>, the former two-division KSW champion, signs a multi-fight deal and debuts against <b>Khaos Williams</b> at UFC&nbsp;332 on 3 October, and <b>UFC&nbsp;334 at Madison Square Garden on 14 November</b> gets its first booked bout in <b>Nazim Sadykhov vs. Jefferson Nascimento</b>; the item carried from the 2:15 edition is not a card at all'
if OLD_M2 in MM:
    MM = sub("mma tldr", MM, OLD_M2, NEW_M)
else:
    MM = sub("mma tldr", MM, OLD_M, NEW_M)

wr("mma-briefing.html", MM)

print("\n".join(report))
