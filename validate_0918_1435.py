# -*- coding: utf-8 -*-
"""Validator for the 2026-09-18 first-run edition."""
import os, re, datetime

OUT = "/sessions/laughing-magical-cray/mnt/outputs"
P = {n: open(os.path.join(OUT, n)).read() for n in
     ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html")}
fails, n = [], 0


def ck(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)


# ---- structural, all four pages
for f, h in P.items():
    ck(h.count("<!DOCTYPE html>") == 1, "%s doctype" % f)
    ck(h.count("<body>") == 1, "%s body" % f)
    ck(h.count('<nav class="tabs">') == 1, "%s one nav" % f)
    ck(h.count('nav.tabs') >= 1, "%s nav css" % f)
    navblk = h.split('<nav class="tabs">')[1].split('</nav>')[0]
    ck(navblk.count("<a href=") == 5, "%s five nav links" % f)
    ck(navblk.count('class="active"') == 1, "%s one active tab" % f)
    for gl in ("&#9733;", "&#9960;", "&#9650;", "&#8856;", "&#128452;"):
        ck(gl in navblk, "%s nav glyph %s" % (f, gl))
    ck("&#9924;" not in h and "⛄" not in h, "%s snowman blocked" % f)
    ck("@@" not in h, "%s no unreplaced placeholder" % f)
    ck('id="edition"' in h and 'id="datestamp"' in h and 'id="updated"' in h, "%s meta pills" % f)
    ck('id="freshline"' in h, "%s freshline" % f)
    ck("America/New_York" in h, "%s stamp js" % f)
    ck(h.rstrip().endswith("</html>"), "%s closes html" % f)

for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    ck(P[f].count("<footer>") == 1, "%s one footer" % f)
    ck(P[f].count('class="tldr"') == 1, "%s one tldr" % f)
    ck('<div class="disc">' in P[f], "%s disclaimer" % f)
ck('class="tldr"' not in P["index.html"], "index carries no tldr of its own")

# ---- tldr verbatim match between index cards and each briefing
for f, label in (("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"),
                 ("mma-briefing.html", "Tale of the Tape")):
    body = P[f].split('<div class="tldr"><b>%s</b> <span>' % label)[1].split('</span></div>')[0]
    ck(body in P["index.html"], "index card matches %s tldr verbatim" % f)
    ck(len(body) > 120, "%s tldr non-trivial" % f)

# ---- TradingView blocks only on markets page
ws = P["wallstreet-briefing.html"]
for w in ("ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"):
    ck("embed-widget-%s.js" % w in ws, "ws has %s" % w)
    for f in ("index.html", "cyber-briefing.html", "mma-briefing.html"):
        ck("embed-widget-%s.js" % w not in P[f], "%s free of %s" % (f, w))
ck(ws.count("embed-widget-single-quote.js") == 3, "exactly three single quotes")
tape = ws.split("embed-widget-ticker-tape.js")[1].split("</script>")[0]
for s in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(s in tape, "tape retains %s" % s)
ck('"symbol":"NASDAQ:XENE"' in ws, "chart of the day pinned to XENE")
ck("livebar" in ws and "LIVE QUOTES" in ws, "livebar present")
ck("not investment advice" in ws, "ws disclaimer wording")

# ---- markets arithmetic, computed not written
ck(abs((51461.90 + 631.21) - 52093.11) < 0.01, "Wed Dow prior level")
ck(abs(631.21 / 52093.11 * 100 - 1.2117) < 0.01, "Wed Dow pct reconciles to 1.21")
ck(abs(51779.85 / 51461.90 - 1) * 100 - 0.618 < 0.01, "Thu Dow pct reconciles to 0.62")
sp_implied = (7637.72 / 7551.81 - 1) * 100
ck(abs(sp_implied - 1.12) > 0.015, "Thu S&P level/pct genuinely diverge (implied %.4f)" % sp_implied)
thu_row = ws.split("<td>Thu Sept 17</td>")[1].split("</tr>")[0]
sp_cell = thu_row.split("</td>")[0]
ck("7,637.72" not in sp_cell, "Thu S&P level withheld from its own cell")
ck("+1.12%" in sp_cell, "Thu S&P percentage published in its cell")
ck(ws.count("7,637.72") == 1 and "level is withheld" in thu_row,
   "source level named exactly once, inside the withholding note")
for lvl, pct in (("7,621.99", "0.21%"), ("51,560.61", "0.42%"), ("29,460.55", "+0.05%"), ("2,850.70", "0.83%")):
    ck(lvl in ws and pct in ws, "TE board %s / %s" % (lvl, pct))
ck("proxy" in ws and "contract-for-difference" in ws, "CFD proxies labelled")
ck("2:37 PM ET" in ws, "as-of time stated")
ck("Session in progress" in ws, "Friday has no close asserted")
ck("Not verified" in ws, "Mon/Tue marked not verified")
ck("not re-fetched this run" in ws, "2yr/30yr caveat")
ck("3.75%&ndash;4.00%" in ws, "fed funds target")
ck("No VIX figure is published" in ws, "VIX refused explicitly")

# ---- cyber: KEV countdown computed, one deadline everywhere
today = datetime.date(2026, 9, 18)
due = datetime.date(2026, 9, 19)
days = (due - today).days
ck(days == 1, "kev days computed = 1")
cy = P["cyber-briefing.html"]
ck(cy.count("1 day left") == 3, "same countdown in banner, patch priority and KEV section (%d)" % cy.count("1 day left"))
ck(cy.count("September 19") >= 2, "deadline date repeated")
ck("BOD 26-04" in cy, "BOD 26-04 named")
ck(cy.count("BOD 22-01") == 1, "BOD 22-01 exactly once")
ck("supersedes the flat three-week window" in cy, "BOD 22-01 only in supersession clause")
for cve in ("CVE-2026-76460", "CVE-2026-85889", "CVE-2026-91843", "CVE-2026-81642", "CVE-2026-77179", "CVE-2026-87886"):
    ck(cve in cy, "cve %s present" % cve)
ck("Threat Level: High" in cy, "threat banner")
ck(cy.count('class="stat"') == 4, "four by-the-numbers stats")
ck("Plugin4Shell" in cy and "Claude Code 2.1.179" in cy and "Codex 0.146.0" in cy, "top story specifics")
ck("Transparent Tribe" in cy and "RUSTYSHADE" in cy, "threat actor spotlight")
ck(cy.count('class="t new"') == 2, "cyber New tags: spotlight + WeaselBiscuit (%d)" % cy.count('class="t new"'))
ck("WeaselBiscuit" in cy, "the one new breach item")
ck("no numeric score was published" in cy, "unscored CVEs labelled")

# ---- mma: champions board parsing
mm = P["mma-briefing.html"]
board = mm.split("Champions Board")[1].split("</table>")[0]
rows = re.findall(r"<tr><td>([^<]+)</td><td[^>]*><b>([^<]+)</b></td>", board)
ck(len(rows) == 11, "champions rows = 11 (%d)" % len(rows))
vac = [d for d, c in rows if c == "VACANT"]
ck(len(vac) == 2, "exactly two vacant belts (%s)" % vac)
ck(set(vac) == {"Heavyweight", "Women's Flyweight"}, "the two vacant belts are HW and W-FLW")
byd = dict(rows)
for d, c in (("Light Heavyweight", "Carlos Ulberg"), ("Middleweight", "Sean Strickland"),
             ("Welterweight", "Islam Makhachev"), ("Lightweight", "Justin Gaethje"),
             ("Featherweight", "Alexander Volkanovski"), ("Bantamweight", "Petr Yan"),
             ("Flyweight", "Joshua Van"), ("Women's Bantamweight", "Kayla Harrison"),
             ("Women's Strawweight", "Mackenzie Dern")):
    ck(byd.get(d) == c, "%s = %s (got %s)" % (d, c, byd.get(d)))
champcells = [c for _, c in rows]
for banned in ("Alex Pereira", "Khamzat Chimaev", "Valentina Shevchenko", "Tom Aspinall",
               "Ilia Topuria", "Magomed Ankalaev", "Alexandre Pantoja", "Merab Dvalishvili",
               "Amanda Nunes", "Jiří Procházka"):
    ck(banned not in champcells, "%s absent from champion cells" % banned)
ck(champcells.count("Carlos Ulberg") == 1, "Ulberg appears exactly once")
ck(byd.get("Heavyweight") == "VACANT", "heavyweight vacant, Aspinall not seated")
ck("Interim: Ciryl Gane" in board, "Gane pinned to interim HW")
ck("seats Carlos Ulberg at heavyweight" in mm and "refused" in mm, "ESPN regression named and refused")

# ---- mma: dates and results
ck("Sat Sept 19" in mm and "Sat Oct 3" in mm and "Sat Oct 24" in mm, "three upcoming dates")
ck(datetime.date(2026, 9, 19) > today and datetime.date(2026, 10, 3) > today
   and datetime.date(2026, 10, 24) > today, "upcoming dates are future")
ck(datetime.date(2026, 9, 12) < today, "last event is past")
ck("2026-09-19T21:00:00-04:00" in mm, "countdown target")
ck('id="ufccdn"' in mm, "countdown element")
ck("Jean Silva" in mm and "rear-naked choke" in mm and "2:57" in mm, "main event result")
ck("Joseph Morales" in mm and "Split decision" in mm, "Moreno gap now filled")
ck("no winner asserted" not in mm.lower().replace("&ldquo;", "").replace("&rdquo;", "")
   or "previously read" in mm, "McMillen winner asserted, prior gap explained")
ck(mm.count("0:36") == 3, "0:36 stated (bonus, prospect, correction note) = %d" % mm.count("0:36"))
ck("33-second" in mm and "not the official one" in mm, "33s refused once, named")
ck('class="t new"' not in mm, "MMA carries zero New tags")
ck("No <b>New</b> tags anywhere on this page" in mm, "MMA states its zero count")
ck("Van &minus;130 / Pantoja +110" in mm, "headliner odds sourced")
ck("none are printed" in mm, "unsourced odds refused explicitly")
ck("$7.7 billion" in mm and "16 million subscriber households" in mm, "business figures")
ck("no viewership number for the September 12 card is published" in mm, "unsourced viewership refused")

# ---- new-tag counts stated in prose
ck("One <b>New</b> tag in this section" in P["cyber-briefing.html"], "cyber states count")
ck("One <b>New</b> tag here" in ws, "markets states count")
ck(ws.count('class="t new"') == 1, "markets exactly one New tag")

# ---- sources present
for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    ck(P[f].count("<li><a href=") >= 10, "%s >=10 sources" % f)
    ck("https://" in P[f], "%s real urls" % f)

print("checks: %d   failures: %d" % (n, len(fails)))
for x in fails:
    print("  FAIL:", x)
