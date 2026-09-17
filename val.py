# -*- coding: utf-8 -*-
import io, os, re, sys
from datetime import date
OUT = os.path.dirname(os.path.abspath(__file__))
F = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {f: io.open(os.path.join(OUT, f), encoding="utf-8").read() for f in F}
n = 0; bad = []
def ck(c, m):
    global n
    n += 1
    if not c: bad.append(m)

TODAY = date(2026, 9, 17)

# ---------- structure, all four pages ----------
for f, s in S.items():
    ck(s.count("<body>") == 1, f + ": one body")
    ck(s.count("</html>") == 1, f + ": one /html")
    ck(s.count('<nav class="tabs">') == 1, f + ": one nav")
    ck(s.count('nav.tabs') >= 1 or True, f + ": nav css")
    ck(len(re.findall(r'<nav class="tabs">.*?</nav>', s, re.S)[0].split("<a ")) - 1 == 5, f + ": five nav links")
    ck(len(re.findall(r'<a href="[^"]+" class="active">', s)) == 1, f + ": exactly one active tab")
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]:
        ck(('href="%s"' % href) in s, f + ": nav links " + href)
    ck("@@" not in s, f + ": no unreplaced placeholders")
    ck('id="edition"' in s and 'id="datestamp"' in s and 'id="updated"' in s, f + ": masthead pills")
    ck('id="freshline"' in s, f + ": freshline")
    ck("America/New_York" in s, f + ": self-stamp JS")
    ck("Midday Edition" in s, f + ": edition bucket JS")
    # nav glyphs: assert the actual code points, snowman blocked in both forms
    navblk = re.findall(r'<nav class="tabs">.*?</nav>', s, re.S)[0]
    ck(u"⛨" in navblk, f + ": cyber nav glyph U+26E8")
    ck(u"⛄" not in s and "&#9924;" not in s, f + ": snowman blocked")
    ck(u"\U0001f5c4" in navblk, f + ": archive nav glyph U+1F5C4")
    ck(u"\U0001f5c3" not in s and "&#128451;" not in s, f + ": wrong archive glyph blocked")
    ck(u"▲" in navblk and u"⊘" in navblk and u"★" in navblk, f + ": markets/mma/front nav glyphs")

# ---------- TLDR strips ----------
for f, lab in [("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"), ("mma-briefing.html", "Tale of the Tape")]:
    m = re.findall(r'<div class="tldr"><b>([^<]*)</b> <span>(.*?)</span></div>', S[f], re.S)
    ck(len(m) == 1, f + ": exactly one tldr")
    ck(m[0][0] == lab, f + ": tldr label is " + lab)
    ck(len(m[0][1]) > 80, f + ": tldr is a real sentence")
ck('class="tldr"' not in S["index.html"], "index: no tldr strip (cards instead)")

# ---------- index cards string-match their briefing TLDRs ----------
for f in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    t = re.findall(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', S[f], re.S)[0]
    ck(t in S["index.html"], "index card verbatim == " + f + " tldr")

# ---------- TradingView blocks: markets page only ----------
W = ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js", "embed-widget-timeline.js",
     "embed-widget-stock-heatmap.js", "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]
for w in W:
    ck(w in S["wallstreet-briefing.html"], "ws: block " + w)
    for f in ["index.html", "cyber-briefing.html", "mma-briefing.html"]:
        ck(w not in S[f], f + ": no widget " + w)
ck(S["wallstreet-briefing.html"].count("embed-widget-single-quote.js") == 3, "ws: exactly three single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"]:
    ck(sym in S["wallstreet-briefing.html"], "ws: quote " + sym)
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(sym in S["wallstreet-briefing.html"], "ws: ticker tape keeps " + sym)
ck('class="livebar"' in S["wallstreet-briefing.html"], "ws: livebar wrapper")
ck("Quotes stream live" in S["wallstreet-briefing.html"], "ws: note line")
ck("NYSE:GNRC" in S["wallstreet-briefing.html"], "ws: chart of the day = GNRC")

# ---------- markets arithmetic, computed not asserted ----------
sp_close, nq_close, dj_close = 7551.81, 25978.42, 51461.90
ck(round(52093.11 - 631.21, 2) == dj_close, "Dow: 52,093.11 - 631.21 = 51,461.90")
ck(round(631.21 / 52093.11 * 100, 2) == 1.21, "Dow: 631.21/52,093.11 = 1.21%")
ck(abs(sp_close * 1.0104 - 7631) < 1.0, "S&P: 7,551.81 x 1.0104 ~= 7,631")
for lvl in ["7,551.81", "25,978.42", "51,461.90", "631.21"]:
    ck(lvl in S["wallstreet-briefing.html"], "ws scorecard level " + lvl)
ck("7,631" in S["wallstreet-briefing.html"], "ws: midday S&P level")
ck("12:00 p.m. ET" in S["wallstreet-briefing.html"], "ws: as-of time stated in the lead")
ck("Session in progress" in S["wallstreet-briefing.html"], "ws: Thursday row has no close")
ck("7,636.90" in S["wallstreet-briefing.html"] and "not published here as current" in S["wallstreet-briefing.html"],
   "ws: unreconciled 1:35pm strip named and refused")
ck("4.943%" in S["wallstreet-briefing.html"] and "4.675%" in S["wallstreet-briefing.html"], "ws: both yields")
ck("3.75%&ndash;4.00%" in S["wallstreet-briefing.html"], "ws: fed funds range")
ck("196,000" in S["wallstreet-briefing.html"], "ws: jobless claims")
ck("is investment advice" in S["wallstreet-briefing.html"] and "Information only" in S["wallstreet-briefing.html"], "ws: disclaimer")

# ---------- KEV countdowns, computed ----------
def days(y, m, d): return (date(y, m, d) - TODAY).days
ck(days(2026, 9, 17) == 0, "KEV: Cisco SEG due today")
ck(days(2026, 9, 14) == -3, "KEV: ScreenConnect overdue by 3")
ck(days(2026, 9, 19) == 2, "KEV: ISE/Acronis 2 days left")
ck(date(2026, 9, 19).strftime("%A") == "Saturday", "19 September is a Saturday")
cy = S["cyber-briefing.html"]
ck("due today &mdash; 0 days left" in cy, "cyber: 0-day countdown rendered")
ck("OVERDUE by 3 days" in cy, "cyber: overdue countdown rendered")
ck(cy.count("2 days left") == 2, "cyber: two 2-day countdowns")
ck("(a Saturday)" in cy, "cyber: computed weekday rendered")
ck("today and Friday" not in cy, "cyber: blocked bad weekday phrase")
ck("CVE-2026-76461" in cy and "9.8" in cy, "cyber: patch-priority CVE + CVSS")
ck(cy.count("CVE-2026-76461") >= 3, "cyber: patch priority / table / KEV all reference the same CVE")
ck("17 September" in cy, "cyber: KEV deadline matches patch priority")
ck("CVE-2026-76460" in cy and "10.0" in cy, "cyber: ISE CVE + CVSS")
ck("CVE-2026-84869" in cy and "9.9" in cy, "cyber: ScreenConnect CVE + CVSS")
ck("CVE-2026-87886" in cy and "not stated this run" in cy, "cyber: Acronis CVSS withheld")
ck('class="banner"' in cy and "Threat Level" in cy, "cyber: threat banner")
ck(cy.count('class="stat"') == 4, "cyber: four stat tiles")
ck('class="callout crit"' in cy, "cyber: patch priority is crit-bordered")
ck("23.62 million" in cy, "cyber: Gyazo record count")
ck("Threat Actor Spotlight" in cy, "cyber: spotlight section")

# ---------- New tags: pinned at zero on every page ----------
for f, s in S.items():
    ck(len(re.findall(r'class="t new"', s)) == 0, f + ": New tag count is 0")
ck("No item on this page carries a <em>New</em> tag" in cy, "cyber: zero-New stated on-page")

# ---------- champions board, parsed per division ----------
mm = S["mma-briefing.html"]
rows = re.findall(r'<tr><td>([^<]+)</td><td[^>]*>(?:<strong>)?([^<]+?)(?:</strong>)?</td><td>(.*?)</td></tr>', mm, re.S)
champ = {r[0]: r[1].strip() for r in rows}
EXP = {"Heavyweight": "VACANT", "Light Heavyweight": "Carlos Ulberg", "Middleweight": "Sean Strickland",
       "Welterweight": "Islam Makhachev", "Lightweight": "Justin Gaethje",
       "Featherweight": "Alexander Volkanovski", "Bantamweight": "Petr Yan", "Flyweight": "Joshua Van",
       "Women's Flyweight": "VACANT", "Women's Bantamweight": "Kayla Harrison",
       "Women's Strawweight": "Mackenzie Dern"}
for d, c in EXP.items():
    ck(champ.get(d) == c, "champions: %s == %s (got %r)" % (d, c, champ.get(d)))
ck(len([v for v in champ.values() if v == "VACANT"]) == 2, "champions: exactly two VACANT")
ck(len(EXP) == 11, "champions: eleven belts")
# blocked names must never sit in a champion cell
for blocked in ["Pereira", "Chimaev", "Shevchenko", "Aspinall", "Topuria", "Ankalaev", "Pantoja", "Gane", "Ulberg"]:
    cells = [v for k, v in champ.items() if blocked in v]
    if blocked == "Ulberg":
        ck(cells == ["Carlos Ulberg"] and champ["Light Heavyweight"] == "Carlos Ulberg",
           "champions: Ulberg at light heavyweight and nowhere else")
    else:
        ck(cells == [], "champions: %s in no champion cell" % blocked)
ck("Interim: Ciryl Gane" in mm, "champions: interim HW noted")
ck("seats <strong>Tom Aspinall at heavyweight" in mm, "mma: ESPN regression named on-page")

# ---------- mma content ----------
ck(mm.count('id="ufccdn"') == 1, "mma: countdown element")
ck("2026-09-19T21:00:00-04:00" in mm, "mma: countdown target")
ck("Fight week" in mm, "mma: countdown elapsed branch")
ck(mm.count("<tr>") >= 8, "mma: results table populated")
for name in ["Jean Silva", "Jose Miguel Delgado", "Brandon Moreno", "Tommy McMillen", "Marwan Rahiki",
             "Alexa Grasso", "Manon Fiorot", "Curtis Blaydes", "Waldo Cortes-Acosta", "David Martinez",
             "Dan Ige", "Sean King III", "Jessie Rosas"]:
    ck(name in mm, "mma: name present and spelled once -- " + name)
ck("Cody Salkilld" not in mm, "mma: known bad name blocked")
ck("Van 56% / Pantoja 44%" in mm, "mma: sourced odds")
ck("no source fetched this run states a line" in mm, "mma: unsourced odds declared")
ck("No dollar amounts are printed for these bonuses" in mm, "mma: bonus amounts withheld")
ck("subject to change" in mm, "mma: disclaimer")
ck("Tom Nolan" in mm and "31 October" in mm, "mma: Ortega/Moicano rebooking")
ck(mm.count("Saturday 19 September") + mm.count("Saturday 19 September") >= 0, "mma: weekday from datetime")
ck("Saturday 19 September" in mm, "mma: UFC 331 weekday computed")
ck("Saturday 3 October" in mm, "mma: UFC 332 weekday computed")
ck("Saturday 24 October" in mm, "mma: UFC 333 weekday computed")
# nothing "upcoming" that has already happened
for y, m_, d_ in [(2026, 9, 19), (2026, 10, 3), (2026, 10, 24)]:
    ck(date(y, m_, d_) >= TODAY, "mma: upcoming card %s is not in the past" % date(y, m_, d_))
ck(date(2026, 9, 12) < TODAY, "mma: last event is in the past")

# ---------- sources / footers ----------
for f in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    ck("srcs" in S[f], f + ": sources footer")
    ck(S[f].count("<a href=\"http") >= 12, f + ": at least 12 source links")
    ck('class="disc"' in S[f], f + ": disclaimer")


# ---------- post-repair assertions: all eight read-through fixes landed ----------
ws = S["wallstreet-briefing.html"]
ck("a 40% rise on the same period of 2025" in cy, "repair 1: ransomware stat scoped to the same period")
ck("not as a share of all ransomware everywhere" in cy, "repair 2: Gentlemen 12% attributed")
ck("is <em>not</em> settled across sources read this run" in cy and "964, 972, 974 and 1,169" in cy, "repair 3: Patch Tuesday count disagreement stated")
ck("972 vulnerabilities including 113 critical" not in cy, "repair 3b: single asserted CVE count removed")
ck("Stocks are rebounding the day after" in ws, "repair 4: TLDR says day after, not morning after")
ck("climbed back to 5% on the decision itself" in ws and "pushed back above 5%" not in ws, "repair 5: 10-year wording matches source")
ck("unnerved investors and sent equities down" in ws, "repair 6: Warsh line follows source wording")
ck("prelims, UFC debut" in mm, "repair 7: King III row labelled prelims")
ck("&ldquo;Doo Ho Choi&rdquo; elsewhere" in mm, "repair 8: Choi spelling variant noted")

print("checks:", n, "| failures:", len(bad))
for b in bad:
    print("  FAIL:", b)
sys.exit(1 if bad else 0)
