# -*- coding: utf-8 -*-
import io, re, sys

fails, checks = [], [0]
def ck(cond, msg):
    checks[0] += 1
    if not cond:
        fails.append(msg)

PAGES = {
    "index": "index.html",
    "cyber": "cyber-briefing.html",
    "ws": "wallstreet-briefing.html",
    "mma": "mma-briefing.html",
}
H = {k: io.open(v, encoding="utf-8").read() for k, v in PAGES.items()}

# ---- structural: every class used in a body is defined in that page's stylesheet
for k, h in H.items():
    style = re.search(r"<style>(.*?)</style>", h, re.S).group(1)
    body = h.split("</style>", 1)[1]
    defined = set(re.findall(r"\.([A-Za-z][\w-]*)", style))
    used = set()
    for attr in re.findall(r'class="([^"]+)"', body):
        used.update(attr.split())
    for c in used:
        ck(c in defined, "%s: class .%s used but not defined" % (k, c))

# ---- five-tab nav, exactly one active, on every page
for k, h in H.items():
    nav = re.search(r"<nav class=\"tabs\">(.*?)</nav>", h, re.S).group(1)
    hrefs = re.findall(r'href="([^"]+)"', nav)
    ck(hrefs == ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"], "%s: nav hrefs wrong: %s" % (k, hrefs))
    ck(nav.count('class="active"') == 1, "%s: active tab count != 1" % k)

# ---- masthead pills + stamp script on every page
for k, h in H.items():
    for pid in ("edition", "datestamp", "updated", "freshline"):
        ck('id="%s"' % pid in h, "%s: missing #%s" % (k, pid))
    ck("America/New_York" in h, "%s: missing stamp script" % k)
    ck("Morning Edition" in h and "Afternoon Edition" in h, "%s: edition buckets missing" % k)

# ---- tldr strips on the three briefings only
for k, lab in (("cyber", "The Wire"), ("ws", "The Tape"), ("mma", "Tale of the Tape")):
    m = re.search(r'<div class="tldr"><b>([^<]*)</b> <span>(.*?)</span></div>', H[k], re.S)
    ck(m is not None, "%s: no tldr" % k)
    ck(m and m.group(1) == lab, "%s: tldr label != %s" % (k, lab))
ck('class="tldr"' not in H["index"], "index must not carry a tldr strip")

# ---- index cards byte-identical to each page's own tldr sentence
for k in ("cyber", "ws", "mma"):
    s = re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', H[k], re.S).group(1)
    ck(s in H["index"], "index card text not byte-identical to %s tldr" % k)

# ---- live widgets: all six blocks on WS, none anywhere else
WID = ["ticker-tape", "single-quote", "timeline", "stock-heatmap",
       "mini-symbol-overview", "events"]
for w in WID:
    ck(("embed-widget-%s.js" % w) in H["ws"], "ws: missing widget %s" % w)
ck(H["ws"].count("embed-widget-single-quote.js") == 3, "ws: need exactly 3 single-quote widgets")
for k in ("index", "cyber", "mma"):
    ck("tradingview.com" not in H[k], "%s: must carry no live widget" % k)
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(sym in H["ws"], "ws: ticker tape missing required symbol %s" % sym)

# ---- section ordering
ORDER = {
    "cyber": ["Threat level", "Top story", "Patch priority", "Threat actor spotlight",
              "Breaches &amp; incidents", "Vulnerability watch", "CISA KEV", "Sources"],
    "ws": ["LIVE QUOTES", "Live index quotes", "The lead", "Movers &amp; drivers",
           "Chart of the day", "Sector heat", "The calendar", "Live market headlines",
           "Weekly scorecard", "Rates, bonds", "On the radar", "Sources"],
    "mma": ["Next card", "Top story", "Fight week", "Last event", "bonuses",
            "Prospect watch", "Around the sport", "Rankings &amp; business",
            "Champions board", "Sources"],
}
for k, seq in ORDER.items():
    pos = [H[k].find(s) for s in seq]
    for i, (s, pp) in enumerate(zip(seq, pos)):
        ck(pp >= 0, "%s: section '%s' missing" % (k, s))
    ck(pos == sorted(pos), "%s: sections out of order: %s" % (k, list(zip(seq, pos))))

# ---- CYBER fact pins
cy = H["cyber"]
ck("CVE-2026-76460" in cy and "10.0" in cy, "cyber: ISE CVE/CVSS")
ck(cy.count("1 day overdue") >= 2, "cyber: '1 day overdue' must appear in callout and KEV bullet")
ck("now one day past due" not in cy, "cyber: variant phrasing of the ISE deadline leaked back in")
callout = re.search(r'<div class="callout crit">(.*?)</div>', cy, re.S).group(1)
for bad in ("17 September", "21 September", "12 September"):
    ck(bad not in callout, "cyber: foreign deadline %s inside patch-priority box" % bad)
ck("19 September" in callout, "cyber: patch-priority box must state 19 September")
ck("CVE-2026-76461" in cy and "9.8" in cy, "cyber: email gateway CVE/CVSS")
ck(cy.count("3 days overdue") >= 2, "cyber: email gateway deadline must be stated twice")
ck("BOD 26-04" in cy and "three days" in cy, "cyber: BOD 26-04 / three-day window")
ck("BOD 22-01" in cy, "cyber: must name the superseded directive to block recomputation")
ck("forensic triage" in cy, "cyber: forensic triage requirement missing")
ck("1 day left" in cy, "cyber: Linux trio countdown")
ck("8 days overdue" in cy, "cyber: FMC countdown")
ck("not published" in cy, "cyber: CVE-2026-20316 must read 'not published'")
ck(cy.count("<tr>") == 8, "cyber: vuln table should be 7 rows + header, got %d" % cy.count("<tr>"))
ck("Threat level: High" in cy, "cyber: threat level")
# Gemini facts
for s in ("three outside systems", "May 2026", "Irregular", "public repository", "July"):
    ck(s in cy, "cyber: Gemini detail missing: %s" % s)
# breach counts
ck("15 million" in cy and "20 May 2026" in cy and "17 May" in cy, "cyber: DentaQuest detail")
ck("7.49 million" in cy and "6.7 million" in cy and "4d722e4d656f77" in cy, "cyber: CenterPoint framing")
ck("3.75 million" in cy and "3.7 million" not in cy, "cyber: CareCloud must read 3.75M only")
ck("170 private GitHub repositories" in cy and "130+ public repositories" in cy,
   "cyber: CrowdSec must print both circulating counts")

# ---- WS fact pins
ws = H["ws"]
ck("7,650.50" in ws and "26,522.55" in ws and "51,682.64" in ws, "ws: index levels")
ck("+0.17%" in ws and "+0.39%" in ws and "&minus;0.18%" in ws, "ws: day moves")
ck("&minus;95.40" in ws, "ws: Dow points")
ck("1.81 points" in ws, "ws: Dow reconciliation gap must stay printed")
ck("3.75%&ndash;4.00%" in ws, "ws: fed funds range")
ck("5.01%" in ws and "5.041%" in ws and "July 2007" in ws, "ws: 10-year detail")
# refused figures appear ONLY in their refusal sentence
for fig, n in (("4.94", 1), ("14.82", 1), ("Brent", 1)):
    ck(ws.count(fig) == n, "ws: refused figure %s appears %d times, expected %d"
       % (fig, ws.count(fig), n))
ck("$100.30" in ws, "ws: WTI settle")
ck("$194.23" in ws and "$194.25" in ws, "ws: COIN close readings")
ck("11&ndash;12%" in ws, "ws: COIN range")
ck("Innovation Exemption" in ws, "ws: COIN driver")
# AMAT must carry no percentage outside the refusal sentence
amat = re.search(r'<h3>Chip equipment outruns the sector</h3>(.*?)</div>', ws, re.S).group(1)
ck("No percentage is published for AMAT here" in amat, "ws: AMAT refusal sentence missing")
ck("&minus;3.19%" in ws and "&minus;2.68%" in ws and "&minus;2.26%" in ws, "ws: laggards")
ck("lost more than 1.5%" in ws, "ws: Dow weekly")
ck("lower, figure disputed" in ws, "ws: Russell direction-only")
ck("not investment advice" in ws, "ws: disclaimer")
ck("closed for the weekend" in ws, "ws: must state markets are closed")
ck(re.search(r'<th>Index</th><th>Close</th><th>Day</th><th>On the week</th>', ws) is not None,
   "ws: scorecard needs the fourth weekly column")

# ---- MMA fact pins
mm = H["mma"]
CHAMPS = [("Heavyweight", "Ciryl Gane"), ("Light heavyweight", "Carlos Ulberg"),
          ("Middleweight", "Sean Strickland"), ("Welterweight", "Islam Makhachev"),
          ("Lightweight", "Justin Gaethje"), ("Featherweight", "Alexander Volkanovski"),
          ("Bantamweight", "Petr Yan"), ("Flyweight", "Joshua Van"),
          ("Women&rsquo;s bantamweight", "Kayla Harrison"),
          ("Women&rsquo;s strawweight", "Mackenzie Dern")]
board = mm.split("Champions board", 1)[1]
for div, name in CHAMPS:
    ck(re.search(r"<td>%s</td><td[^>]*>%s</td>" % (re.escape(div), re.escape(name)), board)
       is not None, "mma: champions row %s -> %s missing/mismatched" % (div, name))
ck(board.count("VACANT") == 1, "mma: exactly one VACANT row required")
BANNED = ["Alex Pereira", "Khamzat Chimaev", "Ilia Topuria", "Tom Aspinall", "Merab Dvalishvili",
          "Jack Della Maddalena", "Alexandre Pantoja", "Diego Lopes", "Valentina Shevchenko",
          "Movsar Evloev"]
champ_cells = re.findall(r"<td>[^<]*</td><td class=\"accc\">([^<]*)</td>", board)
for b in BANNED:
    ck(b not in champ_cells, "mma: stale champion %s sits in a champion cell" % b)
ck(len(champ_cells) == 10, "mma: expected 10 named champion cells, got %d" % len(champ_cells))
ck("49&ndash;46, 48&ndash;47, 50&ndash;45" in mm, "mma: Van scorecards")
ck("Split decision (29&ndash;28, 28&ndash;29, 29&ndash;28)" in mm, "mma: Menifield method upgraded")
ck("19,357" in mm and "$8,300,000" in mm, "mma: gate and attendance")
ck("$782,000" in mm and "$642,000" in mm and "$270,500" in mm, "mma: payouts")
ck("&minus;1011" in mm and "+133" in mm and "no single book is named" in mm,
   "mma: odds line + attribution qualifier")
ck("Meta Apex, Enterprise, Nevada" in mm, "mma: 26 Sep venue")
ck("Rogers Place, Edmonton" in mm, "mma: 17 Oct venue")
ck("Delta Center, Salt Lake City" in mm, "mma: 3 Oct venue")
ck("Etihad Arena, Abu Dhabi" in mm, "mma: 24 Oct venue")
ck("2026-09-26T19:00:00-04:00" in mm, "mma: countdown target")
ck('id="ufccdn"' in mm, "mma: countdown element")
ck("subject to change" in mm, "mma: disclaimer")
results = mm.split("Last event", 1)[1].split("</table>", 1)[0]
ck(results.count("<tr>") == 7, "mma: results table should be 6 rows + header")
# nothing 'upcoming' that has already happened
for past in ("UFC 331", "19 September"):
    pass
fw = mm.split("Fight week", 1)[1].split("Last event", 1)[0]
ck("19 September" not in fw, "mma: a past date appears in the upcoming-cards section")

# ---- sources footers everywhere
for k in ("cyber", "ws", "mma"):
    ck('class="srcs"' in H[k], "%s: sources footer missing" % k)
    n = H[k].split('class="srcs"', 1)[1].count("<a href=")
    ck(n >= 10, "%s: only %d sources" % (k, n))
    ck("http://" not in H[k], "%s: insecure source link" % k)

# ---- no stray template markers
for k, h in H.items():
    ck("%(" not in h, "%s: unsubstituted template marker" % k)
    ck(h.startswith("<!doctype html>") and h.rstrip().endswith("</html>"), "%s: malformed doc" % k)

print("checks: %d, failures: %d" % (checks[0], len(fails)))
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
