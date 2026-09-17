# -*- coding: utf-8 -*-
import datetime, os, re, sys

OUT = os.path.dirname(os.path.abspath(__file__))
FAIL, N = [], 0
PAGES = {}
for f in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    PAGES[f] = open(os.path.join(OUT, f)).read()


def ck(cond, msg):
    global N
    N += 1
    if not cond:
        FAIL.append(msg)


# ---- structure ----
for f, h in PAGES.items():
    ck(h.count("<body") == 1, "%s: body count" % f)
    ck(h.count("<!DOCTYPE html>") == 1, "%s: doctype count" % f)
    ck(h.count('<nav class="tabs">') == 1, "%s: nav count" % f)
    ck(h.count('nav.tabs') >= 1, "%s: nav css" % f)
    links = re.findall(r'<nav class="tabs">(.*?)</nav>', h, re.S)[0]
    ck(len(re.findall(r"<a ", links)) == 5, "%s: five nav links" % f)
    ck(len(re.findall(r'class="active"', links)) == 1, "%s: exactly one active tab" % f)
    for target in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                   "mma-briefing.html", "archive.html"):
        ck(('href="%s"' % target) in links, "%s: nav link to %s" % (f, target))
    ck("@@" not in h, "%s: unreplaced placeholder" % f)
    for gid in ('id="edition"', 'id="datestamp"', 'id="updated"'):
        ck(h.count(gid) == 1, "%s: masthead %s" % (f, gid))
    ck('class="pill live"' in h, "%s: LIVE pill" % f)
    ck('id="freshline"' in h, "%s: freshline" % f)
    ck("America/New_York" in h, "%s: stamp js" % f)

# ---- nav glyphs at code-point level ----
for f, h in PAGES.items():
    for cp in (0x26E8, 0x1F5C4, 0x25B2, 0x2298, 0x2605):
        ck(chr(cp) in h, "%s: nav glyph U+%04X" % (f, cp))
    ck(chr(0x26C4) not in h and "&#9924;" not in h, "%s: banned snowman glyph" % f)

# ---- TLDR strips ----
ck('<b>The Wire</b>' in PAGES["cyber-briefing.html"], "cyber: TLDR label")
ck('<b>The Tape</b>' in PAGES["wallstreet-briefing.html"], "ws: TLDR label")
ck('<b>Tale of the Tape</b>' in PAGES["mma-briefing.html"], "mma: TLDR label")
ck('class="tldr"' not in PAGES["index.html"], "index: must carry no TLDR strip")

# ---- index card summaries match each briefing's own TLDR verbatim ----
def tldr_of(f):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', PAGES[f], re.S)
    return m.group(1).strip()

idx = PAGES["index.html"]
for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    t = tldr_of(f)
    ck(t in idx, "index: card summary does not match %s TLDR verbatim" % f)

# ---- TradingView widgets: markets page only ----
ws = PAGES["wallstreet-briefing.html"]
for w in ("ticker-tape", "single-quote", "timeline", "stock-heatmap",
          "mini-symbol-overview", "events"):
    ck(("embed-widget-%s.js" % w) in ws, "ws: missing widget %s" % w)
    for f in ("index.html", "cyber-briefing.html", "mma-briefing.html"):
        ck(("embed-widget-%s.js" % w) not in PAGES[f], "%s: widget %s must not appear" % (f, w))
ck(ws.count("embed-widget-single-quote.js") == 3, "ws: exactly three single-quote widgets")
for keep in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(keep in ws, "ws: ticker tape must retain %s" % keep)
ck('"symbol":"NYSE:GNRC"' in ws, "ws: chart of the day symbol")

# ---- market arithmetic computed, not asserted ----
sp_prev, sp_chg = 7551.81, 84.90
dow_prev, dow_chg = 51461.90, 374.13
sp_lvl = round(sp_prev + sp_chg, 2)
dow_lvl = round(dow_prev + dow_chg, 2)
sp_pct = round(sp_chg / sp_prev * 100, 2)
dow_pct = round(dow_chg / dow_prev * 100, 2)
ck(sp_lvl == 7636.71, "ws: S&P level arithmetic")
ck(dow_lvl == 51836.03, "ws: Dow level arithmetic")
ck(sp_pct == 1.12, "ws: S&P percent arithmetic")
ck(dow_pct == 0.73, "ws: Dow percent arithmetic")
ck("{:,.2f}".format(sp_lvl) in ws, "ws: S&P level on page")
ck("{:,.2f}".format(dow_lvl) in ws, "ws: Dow level on page")
ck("%.2f%%" % sp_pct in ws.replace("&amp;", "&"), "ws: S&P percent on page")
# Nasdaq 100 row reconciles too
n100_prev, n100_chg = 28945.06, 482.91
ck(abs((n100_prev + n100_chg) - 29427.97) < 0.02, "ws: Nasdaq 100 level arithmetic")
ck(abs(n100_chg / n100_prev * 100 - 1.67) < 0.01, "ws: Nasdaq 100 percent arithmetic")
# refusals present
ck("not published" in ws, "ws: refusal wording present")
ck("VIX" in ws and "cannot both describe" in ws, "ws: VIX refusal stated")
ck("8.81" in ws, "ws: opening-bell refusal named")
ck("7,596" in ws, "ws: superseded snapshot named")
ck("Nasdaq Composite" in ws, "ws: Nasdaq Composite handled")
# no unsourced Thursday close
ck("no Thursday close is shown" in ws, "ws: must state no Thursday close")
ck(not re.search(r"Thursday(?:'s| ) ?clos(?:e|ed) at", ws), "ws: must not claim a Thursday close")

# ---- cyber: KEV countdowns computed from date, not written ----
today = datetime.date(2026, 9, 17)
cy = PAGES["cyber-briefing.html"]
cases = [
    (datetime.date(2026, 9, 17), "due today &mdash; 0 days left"),
    (datetime.date(2026, 9, 19), "2 days left"),
    (datetime.date(2026, 9, 14), "overdue by 3 days"),
    (datetime.date(2026, 8, 21), "overdue by 27 days"),
]
for due, expect in cases:
    d = (due - today).days
    if d == 0:
        got = "due today &mdash; 0 days left"
    elif d < 0:
        got = "overdue by %d days" % abs(d)
    else:
        got = "%d days left" % d
    ck(got == expect, "cyber: countdown math for %s (%s vs %s)" % (due, got, expect))
    ck(expect in cy, "cyber: countdown text missing for %s" % due)
ck(datetime.date(2026, 9, 19).strftime("%A") == "Saturday", "cyber: 19 Sep weekday")
ck("Saturday" in cy, "cyber: Saturday weekday stated")
# patch priority matches the KEV section
ck(cy.count("CVE-2026-76461") >= 3, "cyber: patch priority CVE also in KEV + table")
ck("Patch Priority" in cy and 'callout crit' in cy, "cyber: patch priority is crit-bordered")
# CVSS sourced from vendor
for cve, score in (("CVE-2026-20329", "9.9"), ("CVE-2026-20330", "9.9"),
                   ("CVE-2026-20332", "9.0"), ("CVE-2026-76460", "10.0"),
                   ("CVE-2026-76461", "9.8"), ("CVE-2026-60004", "9.8")):
    ck(cve in cy and score in cy, "cyber: %s / %s" % (cve, score))
ck("actively exploited" in cy.lower(), "cyber: exploitation stated")
ck("refused" in cy.lower(), "cyber: vendor-vs-summary refusal stated")
ck("BOD 22-01" not in cy, "cyber: must not revive the revoked flat three-week rule")
ck("three weeks" not in cy, "cyber: must not assert a three-week window")
ck("Nevada" not in cy, "cyber: permanently excluded Nevada 2025 incident must be absent")
ck('class="banner"' in cy and "Threat level" in cy, "cyber: threat-level banner")
ck(cy.count('class="stat"') == 4, "cyber: four stat tiles")

# ---- mma: champions board ----
mma = PAGES["mma-briefing.html"]
rows = re.findall(r"<tr><td><b>([^<]+)</b></td><td>(.*?)</td><td class=\"mut\">", mma, re.S)
champ_rows = [r for r in rows if r[0] in (
    "Heavyweight", "Light Heavyweight", "Middleweight", "Welterweight", "Lightweight",
    "Featherweight", "Bantamweight", "Flyweight", "Women&rsquo;s Flyweight",
    "Women&rsquo;s Bantamweight", "Women&rsquo;s Strawweight")]
ck(len(champ_rows) == 11, "mma: eleven belts parsed (got %d)" % len(champ_rows))
vac = [r for r in champ_rows if "VACANT" in r[1]]
ck(len(vac) == 2, "mma: exactly two vacant belts (got %d)" % len(vac))
cells = " | ".join(r[1] for r in champ_rows)
for banned in ("Pereira", "Chimaev", "Shevchenko", "Aspinall", "Topuria",
               "Ankalaev", "Pantoja", "Gane"):
    ck(banned not in cells, "mma: %s must not appear in any champion cell" % banned)
ck(sum(1 for r in champ_rows if r[1] == "Carlos Ulberg") == 1, "mma: Ulberg once")
ck([r[1] for r in champ_rows if r[0] == "Light Heavyweight"] == ["Carlos Ulberg"], "mma: LHW = Ulberg")
ck([r[1] for r in champ_rows if r[0] == "Middleweight"] == ["Sean Strickland"], "mma: MW = Strickland")
ck([r[1] for r in champ_rows if r[0] == "Lightweight"] == ["Justin Gaethje"], "mma: LW = Gaethje")
ck([r[1] for r in champ_rows if r[0] == "Featherweight"] == ["Alexander Volkanovski"], "mma: FW = Volkanovski")
ck([r[1] for r in champ_rows if r[0] == "Flyweight"] == ["Joshua Van"], "mma: FLW = Van")
ck("VACANT" in [r[1] for r in champ_rows if r[0] == "Heavyweight"][0], "mma: HW vacant")
ck("interim" in mma.lower() and "Ciryl Gane" in mma, "mma: interim HW named outside champion cell")

# ---- mma: dates chronological ----
for d in (datetime.date(2026, 9, 19), datetime.date(2026, 10, 3), datetime.date(2026, 10, 24)):
    ck(d > today, "mma: upcoming card %s must be in the future" % d)
ck(datetime.date(2026, 9, 12) < today, "mma: Noche UFC must be in the past")
ck("19 September 2026" in mma or "19 Sep" in mma, "mma: UFC 331 date")
ck("ufccdn" in mma and "2026-09-19T21:00:00-04:00" in mma, "mma: countdown script + target")
# names / spellings pinned by the ledger
ck("Manel Kape" in mma, "mma: Kape first name per ledger")
ck("Jose Miguel Delgado" in mma, "mma: Delgado full name")
ck("0:36" in mma and "0:33" not in mma, "mma: King III time is 0:36")
ck("Waldo Cortes Acosta" in mma, "mma: Cortes Acosta spelling")
ck("Dooho Choi" in mma and "Doo Ho Choi" in mma, "mma: both Choi renderings stated")
ck("Robelis Despaigne" in mma and "Robelois Despaigne" in mma, "mma: both Despaigne renderings stated")
ck("Salkilld" not in mma or "Quillan Salkilld" in mma, "mma: Salkilld first name if present")
ck("former champion" not in mma.lower() or "Pantoja" in mma, "mma: descriptor guard")
ck("$100,000" in mma and "Yahoo Sports and Forbes" in mma, "mma: bonus amount attributed")
ck("Fight of the Night" in mma and "No amount is stated" in mma, "mma: FOTN amount withheld")

# ---- New tags reflect a real prior-snapshot comparison ----
ck(cy.count('class="t new"') == 2, "cyber: exactly two New tags (got %d)" % cy.count('class="t new"'))
ck(ws.count('class="t new"') == 1, "ws: exactly one New tag (got %d)" % ws.count('class="t new"'))
ck(mma.count('class="t new"') == 0, "mma: zero New tags this run (got %d)" % mma.count('class="t new"'))

# ---- sources ----
for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    h = PAGES[f]
    ck('class="panel srcs"' in h, "%s: sources block" % f)
    ck(len(re.findall(r'<div class="panel srcs">(.*?)</div>', h, re.S)[0].split("href=")) >= 8,
       "%s: at least seven source links" % f)
    ck('class="disc"' in h, "%s: disclaimer" % f)
ck("not investment advice" in ws, "ws: investment-advice disclaimer")
ck("subject to change" in mma, "mma: cards-subject-to-change disclaimer")

print("VALIDATION: %d checks, %d failures" % (N, len(FAIL)))
for m in FAIL:
    print("  FAIL:", m)
sys.exit(1 if FAIL else 0)
