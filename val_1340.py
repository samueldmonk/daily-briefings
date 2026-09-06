# -*- coding: utf-8 -*-
import os, re, datetime, calendar

D = os.path.dirname(os.path.abspath(__file__))
P = {n: open(os.path.join(D, n), encoding="utf-8").read()
     for n in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]}
ALL = "".join(P.values())
fails = []
n = 0

def ck(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)

# ---- structure required on every page
for name, h in P.items():
    ck(h.startswith("<!DOCTYPE html>"), "%s: no doctype" % name)
    for t in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
              "mma-briefing.html", "archive.html"]:
        ck('href="%s"' % t in h, "%s: nav missing %s" % (name, t))
    ck(h.count('class="active"') == 1, "%s: active tab count != 1" % name)
    for i in ['id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"']:
        ck(i in h, "%s: missing %s" % (name, i))
    ck("pill live" in h, "%s: no LIVE pill" % name)
    ck("America/New_York" in h, "%s: no stamp script" % name)
    ck(h.count("<body>") == 1 and h.count("</body>") == 1, "%s: body tags" % name)
    ck("class=\"disc\"" in h, "%s: no disclaimer" % name)

# ---- tldr on the three briefings only
for name in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    ck(P[name].count('class="tldr"') == 1, "%s: tldr count" % name)
ck('class="tldr"' not in P["index.html"], "index: should not carry a tldr strip")
ck("<b>The Wire</b>" in P["cyber-briefing.html"], "cyber: wrong tldr label")
ck("<b>The Tape</b>" in P["wallstreet-briefing.html"], "ws: wrong tldr label")
ck("<b>Tale of the Tape</b>" in P["mma-briefing.html"], "mma: wrong tldr label")

# ---- index cards mirror the three summaries
ix = P["index.html"]
for frag in ["Elementor Pro", "two-thirds", "162,000", "4.79%", "Parnasse", "Accor Arena"]:
    ck(frag in ix, "index: summary missing %r" % frag)
ck(ix.count("Read the briefing") == 3, "index: not 3 read links")

# ---- wall street live widget blocks A-F
ws = P["wallstreet-briefing.html"]
for w in ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js",
          "embed-widget-timeline.js", "embed-widget-stock-heatmap.js",
          "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]:
    ck(w in ws, "ws: missing widget %s" % w)
ck(ws.count("embed-widget-single-quote.js") == 3, "ws: not 3 single quotes")
ck('"FOREXCOM:SPXUSD"' in ws and '"FOREXCOM:NSXUSD"' in ws and '"FOREXCOM:DJI"' in ws, "ws: index quotes")
ck('"TVC:USOIL"' in ws and '"TVC:US10Y"' in ws, "ws: ticker must keep oil + 10Y")
ck("livebar" in ws and "LIVE QUOTES" in ws, "ws: livebar")
ck("Quotes stream live" in ws, "ws: note line")

# ---- market numbers: internal consistency
ck("7,718.60" in ws and "26,506.99" in ws and "53,414.25" in ws, "ws: index closes")
ck(abs((53686.11 - 271.86) - 53414.25) < 0.005, "ws: Dow arithmetic")
ck("162,000" in ws and "53,000" in ws, "ws: payrolls")
ck("4.79%" in ws, "ws: 10Y")
ck("$96.28" in ws, "ws: Brent")
# no unsourced numbers we refused
for banned in ["4.676", "4.374", "VIX at", "Fed funds range of"]:
    ck(banned not in ws, "ws: refused figure leaked: %s" % banned)
ck("No VIX level is published" in ws, "ws: VIX refusal not stated")
ck("declines to pick a number" in ws, "ws: crude weekly refusal not stated")
# after-hours must NOT appear (weekend)
ck("After-Hours" not in ws and "After Hours" not in ws, "ws: after-hours section on a weekend")
ck("Labor Day" in ws, "ws: Labor Day closure missing")

# ---- cyber
cy = P["cyber-briefing.html"]
ck("Threat level: High" in cy, "cy: threat banner")
ck(cy.count('class="stat"') == 4, "cy: stat strip != 4")
ck('callout crit' in cy, "cy: patch priority must be crit")
ck("CVE-2026-32475" in cy and "9.8" in cy, "cy: top story CVE")
ck("4.2.2" in cy and "19 August" in cy, "cy: fixed version/date")
ck("190,000" in cy, "cy: exploit attempts")
# KEV deadline consistency: same date in patch priority and KEV section
ck(cy.count("5 September 2026") >= 2, "cy: 5 Sep deadline not stated in both blocks")
ck("overdue by 1 day" in cy, "cy: countdown for 5 Sep should be overdue by 1 day")
ck("(10 days left)" in cy, "cy: countdown for 16 Sep should be 10 days")
ck("BOD 26-04" in cy, "cy: BOD 26-04")
ck("BOD 22-01" in cy, "cy: BOD 22-01 supersession note")
# every KEV CVE present in the table
for c in ["CVE-2026-83548", "CVE-2026-83549", "CVE-2026-9586", "CVE-2026-82329",
          "CVE-2026-49869", "CVE-2026-48710", "CVE-2026-59822"]:
    ck(c in cy, "cy: KEV CVE %s missing" % c)
# no deadline asserted for the three non-KEV items
ck("no CISA KEV entry this run could verify" in cy, "cy: Elementor no-KEV statement")
ck("No KEV entry and no deadline asserted" in cy, "cy: non-KEV list")
ck("neither is asserted as the fixed version" in cy, "cy: ASUS refusal")
# breach numbers
ck("8.8 million email addresses" in cy, "cy: MAG 8.8M")
ck("204,341" in cy and "630.4 GB" in cy, "cy: Tata figures")
ck("9.5 million" in cy, "cy: Aesto")
ck("FulcrumSec" in cy, "cy: threat actor")

# ---- mma
mm = P["mma-briefing.html"]
ck('id="ufccdn"' in mm and "2026-09-12T17:00:00-04:00" in mm, "mma: countdown")
ck(mm.count("<tr>") >= 20, "mma: tables too small")
# champions table exactly 12 champion rows + header
champ = mm.split('<h2 class="sec">Champions Board</h2>')[1]
ck(champ.count("<tr>") == 13, "mma: champions table must be 12 rows + header, got %d" % (champ.count("<tr>") - 1))
for c in ["Tom Aspinall", "Carlos Ulberg", "Sean Strickland", "Islam Makhachev",
          "Justin Gaethje", "Alexander Volkanovski", "Petr Yan", "Joshua Van",
          "Valentina Shevchenko", "Kayla Harrison", "Mackenzie Dern", "Ciryl Gane"]:
    ck(c in champ, "mma: champion missing %s" % c)
# regression guards
for bad in [("Pereira", "Light Heavyweight"), ("Chimaev", "Middleweight")]:
    row = [l for l in champ.split("<tr>") if bad[1] in l]
    for l in row:
        ck(bad[0] not in l.split("</td>")[1] if "</td>" in l else True,
           "mma: REGRESSION %s listed at %s" % bad)
# Featherweight row only. A blanket "vacant" scan over the whole table is wrong:
# Ulberg legitimately "won the vacant belt", and the FW row carries its own
# "Not vacant." disclaimer.
fw = [r for r in champ.split("<tr>") if "<td>Featherweight</td>" in r]
ck(len(fw) == 1, "mma: featherweight row not found exactly once")
ck(fw and "Alexander Volkanovski" in fw[0], "mma: featherweight champion must be Volkanovski")
ck(fw and "Not vacant" in fw[0], "mma: featherweight row must state Not vacant")
ck("0 defences</b>" in champ or "<b>0 defences</b>" in champ, "mma: Harrison 0 defences")
# Parnasse guards.
# Sentence-scoped, not block-scoped: block scope produced two false positives
# (the explicit denial in Top Story, and an unrelated broadcast note in
# Rankings & Business). Any sentence that ties Parnasse to the Contender Series
# WITHOUT negating it is the real defect.
plain = re.sub(r"<[^>]+>", " ", re.sub(r'href="http[^"]*"', "", mm))
plain = plain.replace("&rsquo;", "'")
for sent in re.split(r"(?<=[.!?])\s+", plain):
    if "Parnasse" in sent and "Contender Series" in sent:
        ck(" not a Dana White" in sent or "not a Dana White" in sent,
           "mma: Parnasse tied to Contender Series without negation: %r" % sent[:140])
ck("is <b>not</b> a Dana White" in mm, "mma: Parnasse non-DWCS statement")
ck("Salahdine" in mm and "Saladhine" not in mm, "mma: spelling")
ck("2:25" in mm and "2:35" in mm and "not asserted" in mm, "mma: stoppage-time conflict must be stated")
ck("KO, R1 1:40" in mm, "mma: Sola time")
ck("R2 0:55" in mm, "mma: Pinto time")
ck("$4,365,335" in mm and "15,687" in mm, "mma: gate/attendance")
ck("no Fight of the Night" in mm, "mma: bonuses")
ck("No betting odds are published" in mm, "mma: odds refusal")

# ---- calendar sanity: every stated weekday must match the real date
CAL = [("Monday", 2026, 9, 7), ("Tuesday", 2026, 9, 8), ("Wednesday", 2026, 9, 9),
       ("Thursday", 2026, 9, 10), ("Friday", 2026, 9, 11), ("Tuesday", 2026, 9, 15),
       ("Wednesday", 2026, 9, 16), ("Saturday", 2026, 9, 12), ("Saturday", 2026, 9, 19),
       ("Saturday", 2026, 9, 5), ("Wednesday", 2026, 9, 2), ("Saturday", 2026, 9, 5),
       ("Thursday", 2026, 9, 17), ("Tuesday", 2026, 9, 22)]
for wd, y, m, d in CAL:
    ck(calendar.day_name[datetime.date(y, m, d).weekday()] == wd,
       "calendar: %s %d-%02d-%02d is actually %s" % (wd, y, m, d,
        calendar.day_name[datetime.date(y, m, d).weekday()]))

# ---- "New" tags: compare against the previous archived edition
PREV = "/tmp/db_1788716130/archive"
prev = {}
for sec, key in [("cyber", "cyber"), ("wallstreet", "wallstreet"), ("mma", "mma")]:
    cands = sorted([f for f in os.listdir(PREV) if f.startswith(sec + "-")])
    if cands:
        prev[key] = open(os.path.join(PREV, cands[-1]), encoding="utf-8").read()

newtags = {"cyber-briefing.html": cy.count('class="t new"'),
           "wallstreet-briefing.html": ws.count('class="t new"'),
           "mma-briefing.html": mm.count('class="t new"')}
print("New tags per page:", newtags)
if "cyber" in prev:
    ck("Tata Electronics" not in prev["cyber"], "cy: Tata tagged New but was in prior edition")
    ck("8.8 million" not in prev["cyber"], "cy: MAG 8.8M tagged New but was in prior edition")
    ck("FulcrumSec" in prev["cyber"], "cy: FulcrumSec expected in prior edition - re-check the not-New note")
if "wallstreet" in prev:
    ck("Cybercab" not in prev["wallstreet"], "ws: Tesla tagged New but was in prior edition")
ck(mm.count('class="t new"') == 0, "mma: should carry no New tags this edition")

print("checks:", n, "failures:", len(fails))
for f in fails:
    print("  FAIL:", f)
