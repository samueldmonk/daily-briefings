# -*- coding: utf-8 -*-
"""Edition 2026-09-07-1436 validator."""
import sys, os, re
REPO = sys.argv[1]
R = lambda n: open(os.path.join(REPO, n), encoding="utf-8").read()
CY, WS, MM, IX = R("cyber-briefing.html"), R("wallstreet-briefing.html"), R("mma-briefing.html"), R("index.html")
PAGES = {"cyber": CY, "wallstreet": WS, "mma": MM, "index": IX}
fails, n = [], 0
def ck(name, cond):
    global n; n += 1
    if not cond: fails.append(name)

# ---- structural -----------------------------------------------------------
for k, h in PAGES.items():
    ck("%s div balance" % k, h.count("<div") == h.count("</div>"))
    ck("%s h2 balance" % k, h.count("<h2") == h.count("</h2>"))
    ck("%s h3 balance" % k, h.count("<h3") == h.count("</h3>"))
    ck("%s p balance" % k, h.count("<p") == h.count("</p>"))
    ck("%s no empty h2" % k, '<h2 class="sec"></h2>' not in h)
    for el in ("datestamp", "updated", "edition"):
        ck("%s has #%s" % (k, el), 'id="%s"' % el in h)
    ck("%s five-tab nav" % k, all(x in h for x in
        ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html")))
    ck("%s no bare 'this run'" % k, "this run" not in h)
    ck("%s no broken demotion" % k, not re.search(r'\b(item|reached|read|added|caught|carried|stated|fetched|corrected|New) the 2:15 edition', h))

for k in ("cyber", "wallstreet", "mma"):
    ck("%s has tldr" % k, '<div class="tldr">' in PAGES[k])
    ck("%s has freshline" % k, 'id="freshline"' in PAGES[k])

# ---- live widget blocks (wall street) -------------------------------------
for w in ("ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"):
    ck("ws widget %s" % w, "embed-widget-" + w in WS)
ck("ws three single-quotes", WS.count("embed-widget-single-quote") == 3)
for s in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck("ws ticker symbol " + s, s in WS)

# ---- champions board (CORRECTIONS.md authoritative) ------------------------
CHAMPS = [("Aspinall", "Heavyweight"), ("Ulberg", "Light Heavyweight"), ("Strickland", "Middleweight"),
          ("Makhachev", "Welterweight"), ("Gaethje", "Lightweight"), ("Volkanovski", "Featherweight"),
          ("Yan", "Bantamweight"), ("Van", "Flyweight"), ("Harrison", None), ("Dern", None), ("Gane", None)]
for who, _ in CHAMPS:
    ck("mma champ present: " + who, who in MM)
i = MM.find("Champions Board")
board = MM[i:i + 6000] if i > 0 else ""
ck("mma board: Pereira NOT at LHW", not re.search(r'Light Heavyweight.{0,120}Pereira', board, re.S))
ck("mma board: Chimaev NOT at MW", not re.search(r'>Middleweight</td><td><b>[^<]*Chimaev', board))
ck("mma board: LW is Gaethje not Topuria", not re.search(r'>Lightweight</td><td><b>[^<]*Topuria', board))
ck("mma board: FW not vacant", not re.search(r'Featherweight.{0,80}[Vv]acant', board, re.S))

# ---- standing corrections ---------------------------------------------------
ck("no Nevada 2026 ransomware", not re.search(r'Nevada.{0,200}2026.{0,80}ransomware', CY, re.S))
ck("Parnasse not Contender Series", not re.search(r'Parnasse.{0,300}Contender Series', MM, re.S))
ck("Parnasse spelling", "Saladhine" not in MM)
ck("Dariush not called champion/challenger",
   not re.search(r'Dariush.{0,80}(former champion|title challenger)', MM, re.S))
ck("NetScaler CVSS 9.3 not 9.8", not re.search(r'2026-3055.{0,200}9\.8', CY, re.S))

# ---- this edition's new items ---------------------------------------------
for s in ("Aktulaev", "DarkVNC", "TVRAT", "80,000", "255 fake accounts", "Cyprus"):
    ck("cy Aktulaev detail: " + s, s in CY)
ck("cy Aktulaev framed as prosecution", "indictment, not an intrusion" in CY)
ck("cy Aktulaev carries no CVE claim", "no patch, no CVE, no CVSS and no deadline" in CY)
ck("cy Aktulaev platform unnamed", "Upwork" not in CY and "Freelancer.com" not in CY)

for s in ("Soldic", "Khaos Williams", "21&ndash;4", "Robocop", "KSW", "Sadykhov", "Jefferson Nascimento", "Madison Square Garden"):
    ck("mma new detail: " + s, s in MM)
ck("mma Soldic DDP series stated 1-1", re.search(r'Soldic.{0,2500}1&ndash;1.{0,200}knockout', MM, re.S) is not None)
ck("mma Soldic no odds", not re.search(r'Soldic.{0,1500}Odds:', MM, re.S))
ck("mma UFC334 no record published", "No records, no rankings and no odds are printed" in MM
   and not re.search(r'(Sadykhov|Nascimento)</b>[^<]{0,40}[(]<b>11&ndash;1', MM))
ck("mma UFC334 no headliner claimed", "No main event has been announced for this card" in MM)
ck("mma Soldic not called contender", not re.search(r'Soldic.{0,400}(is a contender|title challenger)', MM, re.S))

for s in ("UTC+8", "1:30 PM ET", "2:30 PM ET", "01:00 UTC+8"):
    ck("ws halt detail: " + s, s in WS)
ck("ws halt arithmetic disclosed", "arithmetic, not the source" in WS)
ck("ws brent 97.68 present", "$97.68" in WS)
ck("ws brent range widened", "roughly $97.27 to $97.68" in WS)
ck("ws brent no single level", "No single Brent level is asserted for today" in WS)
ck("ws 97.93 still the touch", "$97.93" in WS)
ck("ws 97.68 not called a high", "It is <b>not</b> published as a new high" in WS
   and not re.search(r'\$97\.68[^<]{0,60}(?<!not )(?:is|was) (?:the |a )?(?:new |session |intraday )high', WS))
ck("ws no Monday close asserted", not re.search(r'S&amp;P 500 closed (up|down)', WS))

# ---- new-tag ledger integrity ---------------------------------------------
tags = {k: PAGES[k].count('class="t new"') for k in ("cyber", "wallstreet", "mma")}
ck("ledger: cyber 1 new tag", tags["cyber"] == 1)
ck("ledger: wallstreet 1 new tag", tags["wallstreet"] == 1)
ck("ledger: mma 2 new tags", tags["mma"] == 2)
ck("ledger note states four", "Four items are tagged New this edition" in CY)
SNAP = os.path.join(REPO, "archive")
for s, f in [("Aktulaev", "cyber"), ("DarkVNC", "cyber"), ("Soldic", "mma"),
             ("Sadykhov", "mma"), ("Nascimento", "mma"), ("UTC+8", "wallstreet")]:
    p = os.path.join(SNAP, "%s-2026-09-07-1419.html" % f)
    ck("ledger proof absent from 1419 %s: %s" % (f, s),
       os.path.exists(p) and s not in open(p, encoding="utf-8").read())

# ---- index faithfulness ----------------------------------------------------
ck("ix cyber card matches lead", "Aktulaev" in IX and "80,000" in IX)
ck("ix ws card matches lead", "1:30 PM ET" in IX and "2:30 PM ET" in IX)
ck("ix mma card matches lead", "Soldic" in IX and "Sadykhov" in IX)
ck("ix three cards", IX.count("Read the briefing") == 3)
ck("ix no live widgets", "embed-widget" not in IX)

# ---- chronology ------------------------------------------------------------
ck("no 'upcoming' UFC Paris", not re.search(r'[Uu]pcoming.{0,60}UFC Paris', MM))
ck("UFC 332 date consistent", "3 October" in MM or "3&nbsp;October" in MM)
ck("UFC 334 date consistent", "14 November" in MM or "14&nbsp;November" in MM)

# ---- sources ---------------------------------------------------------------
for k in ("cyber", "wallstreet", "mma"):
    ck("%s sources panel" % k, 'class="panel srcs"' in PAGES[k])
    ck("%s disclaimer" % k, any(s in PAGES[k] for s in
       ("Nothing here is investment advice", "subject to change", "Compiled from public reporting")))
for u in ("thehackernews.com/2026/09/extradited-russian-hacker-faces-charges.html",
          "bleepingcomputer.com/news/security/us-charges-russian"):
    ck("cy source url: " + u[:40], u in CY)
for u in ("bloodyelbow.com/2026/09/04/roberto-soldic-signs",
          "si.com/fannation/mma/news/first-fight-booked-ufc-334"):
    ck("mma source url: " + u[:40], u in MM)

print("checks: %d   failures: %d" % (n, len(fails)))
for f in fails: print("  FAIL", f)
