# -*- coding: utf-8 -*-
"""Edition 2026-09-07-1436: grammar repair, New-tag ledger, sources, index sync."""
import re, sys, os
REPO = sys.argv[1]
P = lambda n: os.path.join(REPO, n)
def rd(n): return open(P(n), encoding="utf-8").read()
def wr(n, s): open(P(n), "w", encoding="utf-8").write(s)
rep = []
def sub(tag, h, old, new):
    if old not in h:
        rep.append("MISS  " + tag); return h
    rep.append("ok    %s (x%d)" % (tag, h.count(old)))
    return h.replace(old, new)

# ---- grammar repair after the blanket demotion ----------------------------
GRAM = [
    ("item the 2:15 edition",      "item in the 2:15 edition"),
    ("tagged New the 2:15 edition", "tagged New in the 2:15 edition"),
    ("reached the 2:15 edition",   "reached in the 2:15 edition"),
    ("read the 2:15 edition",      "read in the 2:15 edition"),
    ("added the 2:15 edition",     "added in the 2:15 edition"),
    ("caught the 2:15 edition",    "caught in the 2:15 edition"),
    ("carried the 2:15 edition",   "carried in the 2:15 edition"),
    ("stated the 2:15 edition",    "stated in the 2:15 edition"),
    ("fetched the 2:15 edition",   "fetched in the 2:15 edition"),
    ("corrected the 2:15 edition", "corrected in the 2:15 edition"),
    ("the 2:15 run",               "the 2:15 edition"),
]

LEDGER = (
'<p class="note" style="margin:-4px 0 12px"><b>Four items are tagged New this edition and they are spread across two pages: '
'<b>one here</b> &mdash; the <b>DOJ indictment of Searzhudin Tamirlanovich Aktulaev</b> over a 2016&ndash;17 Excel-macro campaign &mdash; '
'<b>two on the MMA page</b> (<b>Roberto Soldic&rsquo;s UFC signing</b> and the first bout booked for <b>UFC&nbsp;334</b>), '
'and <b>one on the Wall Street page</b> (the <b>ICE Brent and CME crude holiday halts</b>). </b>'
'<span class="mut">Measured against <code>archive/cyber-2026-09-07-1419.html</code>, <code>archive/wallstreet-2026-09-07-1419.html</code> and '
'<code>archive/mma-2026-09-07-1419.html</code>, counting the markup these pages actually emit (<code>class=&quot;t new&quot;</code>) and asserting '
'<b>placement per page</b> rather than a bare total. The 2:15 snapshots carried <b>two</b> New tags &mdash; <b>ShieldBreak</b> (CVE&#8209;2026&#8209;69414) here and '
'<b>Paddy Pimblett&rsquo;s December timeline</b> on the MMA page &mdash; and both items are still on their pages and still correct, but each was in the previous '
'archived edition, so both tags now read <b>Carried</b>. The strings <code>Aktulaev</code>, <code>DarkVNC</code>, <code>Soldic</code>, <code>Sadykhov</code>, '
'<code>Nascimento</code> and <code>UTC+8</code> each return <b>zero matches across all three 2:15 snapshots</b>, which is the test that earns a tag. '
'<b>This is the first edition today in which the Wall Street page has earned a New tag</b>; on every prior run it either carried none or corrected itself, '
'and a correction is tagged as neither. A tag is a statement about the previous snapshot, not about how recently the underlying event happened &mdash; '
'the Aktulaev conduct is nine years old and the Soldic signing was reported on <b>4 September</b>, and both are tagged New, because this desk had never carried either.</span></p>\n'
)

CY = rd("cyber-briefing.html")
for a, b in GRAM: CY = CY.replace(a, b)
old_led = re.search(r'<p class="note" style="margin:-4px 0 12px"><b>One item is tagged New.*?</p>\n?', CY, re.S)
if old_led:
    CY = CY.replace(old_led.group(0), LEDGER); rep.append("ok    cy ledger replaced")
else:
    rep.append("MISS  cy ledger")

CY = sub("cy tldr", CY,
    'The one genuinely new item in the 2:15 edition is an unpatched privilege-escalation zero-day',
    'The one genuinely new item this edition is an <b>indictment rather than an intrusion</b> &mdash; the DOJ has charged an extradited Russian national over a '
    '<b>2016&ndash;17 campaign that sent malicious Excel attachments to about 80,000 users of a freelance-work platform</b>, dropping TVRAT and DarkVNC; '
    'it carries no CVE, no patch and no deadline, and is on the page as tradecraft that is still current rather than as a live threat. '
    'The 2:15 edition&rsquo;s new item, now carried, is an unpatched privilege-escalation zero-day')
wr("cyber-briefing.html", CY)

for f in ("wallstreet-briefing.html", "mma-briefing.html", "index.html"):
    h = rd(f)
    for a, b in GRAM: h = h.replace(a, b)
    wr(f, h)
rep.append("ok    grammar repair across all pages")

# ---- sources -------------------------------------------------------------
SRC = {
 "wallstreet-briefing.html": [
   ("KuCoin &mdash; U.S. markets closed 7 September for Labor Day; futures trading ends early",
    "https://www.kucoin.com/news/flash/u-s-markets-closed-on-sept-7-for-futures-trading-ends-early"),
   ("Trading Economics &mdash; Brent crude oil price and news",
    "https://tradingeconomics.com/commodity/brent-crude-oil"),
 ],
 "cyber-briefing.html": [
   ("The Hacker News &mdash; Extradited Russian hacker faces charges over Excel malware campaign",
    "https://thehackernews.com/2026/09/extradited-russian-hacker-faces-charges.html"),
   ("BleepingComputer &mdash; US charges Russian for infecting 80,000 freelancers with malware",
    "https://www.bleepingcomputer.com/news/security/us-charges-russian-for-infecting-80-000-freelancers-with-malware/"),
   ("Help Net Security &mdash; Russian man indicted for spreading malware to 80,000 freelancers",
    "https://www.helpnetsecurity.com/2026/09/03/russian-national-indicted-freelance-platform-malware/"),
   ("Infosecurity Magazine &mdash; Russian man extradited over malware campaign targeting freelancers",
    "https://www.infosecurity-magazine.com/news/russian-man-extradited-malware/"),
 ],
 "mma-briefing.html": [
   ("Bloody Elbow &mdash; Roberto Soldic signs: UFC snap up former two-weight champion",
    "https://bloodyelbow.com/2026/09/04/roberto-soldic-signs-ufc-snap-up-former-two-weight-champion-who-knocked-out-dricus-du-plessis/"),
   ("Yahoo Sports &mdash; Former KSW champ Roberto Soldic signs for UFC 332 octagon debut",
    "https://ca.sports.yahoo.com/news/former-ksw-champ-roberto-soldic-202728245.html"),
   ("Bloody Elbow &mdash; UFC 334 gets its first fight at Madison Square Garden",
    "https://bloodyelbow.com/2026/09/03/ufc-334-gets-its-first-fight-as-11-1-former-mma-champion-books-return-at-madison-square-garden/"),
   ("Sports Illustrated &mdash; First fight booked for UFC 334 card at Madison Square Garden",
    "https://www.si.com/fannation/mma/news/first-fight-booked-ufc-334-card-madison-square-garden"),
 ],
}
for f, items in SRC.items():
    h = rd(f)
    i = h.find('<h2 class="sec">Sources')
    j = h.find('</ul>', i)
    if i < 0 or j < 0:
        rep.append("MISS  sources " + f); continue
    add = "".join('<li><a href="%s">%s</a></li>\n' % (u, t) for t, u in items if u not in h)
    h = h[:j] + add + h[j:]
    wr(f, h); rep.append("ok    sources %s (+%d)" % (f, add.count("<li>")))

# ---- index sync ----------------------------------------------------------
IX = rd("index.html")
IX = sub("ix cyber h3", IX,
  "An unpatched zero-day in Microsoft Defender itself",
  "A ten-year-old Excel campaign reaches a courtroom &mdash; and PaperCut is still the box to fix")
i = IX.find("ConnectWise confirmed on 3 September")
if i > 0:
    IX = IX[:i] + ('The one new item today is <b>an indictment, not an intrusion</b>: the DOJ has charged <b>Searzhudin Tamirlanovich Aktulaev</b>, 40, '
    'extradited from Cyprus on 28 August, over a campaign running <b>June 2016 to November 2017</b> that used roughly <b>255 fake accounts</b> to send '
    '<b>malicious Excel attachments to about 80,000 users</b> of a Northern California freelance-work platform, dropping <b>TVRAT</b> and <b>DarkVNC</b>. '
    'It carries no CVE and no deadline. ') + IX[i:]
    rep.append("ok    ix cyber body")
else:
    rep.append("MISS  ix cyber body")

IX = sub("ix ws h3", IX,
  "Brent&rsquo;s holiday session ran both ways, and this page h",
  "The last live tape on the page has stopped &mdash; and Brent&rsquo;s holiday session ran both ways. This page h")
i = IX.find("U.S. stock and bond markets are shut for Labor Day")
if i > 0:
    IX = IX[:i] + ('<b>As of this edition the oil futures have halted too</b> &mdash; a relayed holiday schedule puts <b>ICE Brent at about 1:30 PM ET</b> and '
    '<b>CME crude at about 2:30 PM ET</b>, alongside the <b>1:00 PM ET</b> equity-index halt already carried &mdash; so every symbol on the briefing&rsquo;s '
    'live ticker is now showing a last matched price. ') + IX[i:]
    rep.append("ok    ix ws body")
else:
    rep.append("MISS  ix ws body")

IX = sub("ix mma h3", IX,
  "Pimblett puts December on the record",
  "Soldic signs, and UFC&nbsp;334 gets its first bout")
IX = sub("ix mma body", IX,
  "One new item this edition, and it is not a card:",
  'Two new items today, both roster news: <b>Roberto Soldic</b> &mdash; former two-division KSW champion, 21&ndash;4 with 18 knockouts &mdash; has signed a '
  'multi-fight UFC deal and debuts against <b>Khaos Williams</b> at <b>UFC&nbsp;332</b> on <b>3 October</b>, and <b>UFC&nbsp;334</b> at <b>Madison Square Garden</b> '
  'on <b>14 November</b> has its first booked bout in <b>Nazim Sadykhov vs. Jefferson Nascimento</b>. Carried from the 2:15 edition:')
wr("index.html", IX)

print("\n".join(rep))
