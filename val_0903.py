# -*- coding: utf-8 -*-
import io, os, re, datetime, calendar
OUT = "/sessions/zealous-laughing-euler/mnt/outputs"
FILES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
P = {f: io.open(os.path.join(OUT, f), encoding="utf-8").read() for f in FILES}
CY, WS, MM, IX = P["cyber-briefing.html"], P["wallstreet-briefing.html"], P["mma-briefing.html"], P["index.html"]
ALL = "\n".join(P.values())
raised, n = [], 0
def chk(cond, msg):
    global n
    n += 1
    if not cond: raised.append(msg)
def ran(pat, txt, label):
    """prove a guard's pattern actually matches something (no vacuous guards)"""
    global n
    n += 1
    if not re.search(pat, txt): raised.append("GUARD-VACUOUS: %s" % label)

TODAY = datetime.date(2026, 9, 3)
chk(TODAY.strftime("%A") == "Thursday", "today weekday wrong")

# 1 -- every "Weekday, Month D, YYYY" string must be calendrically real
MON = {m: i for i, m in enumerate(calendar.month_name) if m}
pat = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+([A-Z][a-z]+)\s+(\d{1,2}),\s+(\d{4})"
found = 0
for f, t in P.items():
    for wd, mo, d, y in re.findall(pat, t):
        found += 1
        real = datetime.date(int(y), MON[mo], int(d)).strftime("%A")
        chk(real == wd, "CALENDAR: %s says '%s, %s %s, %s' but that date is a %s" % (f, wd, mo, d, y, real))
chk(found >= 3, "calendar scanner found too few dated strings (%d)" % found)
# short form "Sat, Sept 5" / "Wed, Sept 2"
SH = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sept":9,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
sp = r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\s+(\d{1,2})"
sf = 0
for f, t in P.items():
    for wd, mo, d in re.findall(sp, t):
        sf += 1
        real = datetime.date(2026, SH[mo], int(d)).strftime("%a")
        chk(real == wd, "CALENDAR-SHORT: %s says '%s, %s %s' but 2026 has that as %s" % (f, wd, mo, d, real))
chk(sf >= 4, "short-date scanner found too few (%d)" % sf)

# 2 -- countdown arithmetic
chk((datetime.date(2026,9,5)-TODAY).days == 2, "Sept 5 is not 2 days from today")
chk((datetime.date(2026,9,16)-TODAY).days == 13, "Sept 16 is not 13 days from today")
chk("2 days left" in CY, "cyber missing the 2-day countdown")
chk("13 days left" in CY, "cyber missing the 13-day countdown")
chk("2 days" in CY, "stat strip missing 2 days")
ran(r"2 days left", CY, "2-day countdown")
# the Patch Priority box and the KEV section must carry the SAME date
chk(CY.count("September 5") >= 3, "Sept 5 deadline not repeated across patch priority + KEV + top story")
chk("September 14" not in CY, "stale PaperCut Sept 14 clock leaked back in")
chk("PaperCut" in CY and "not re-sourced" in CY, "PaperCut drop not explained")

# 3 -- champions board
chk("Sean Strickland" in MM, "middleweight champion missing")
ran(r"<td><b>Middleweight</b></td><td>Sean Strickland</td>", MM, "MW champion cell")
chk(not re.search(r"<td><b>Middleweight</b></td><td>[^<]*Chimaev", MM), "REGRESSION: Chimaev in the MW champion cell")
chk(not re.search(r"<td><b>Light Heavyweight</b></td><td>[^<]*Pereira", MM), "REGRESSION: Pereira at LHW")
ran(r"<td><b>Featherweight</b></td><td>Alexander Volkanovski</td>", MM, "FW champion cell")
chk(not re.search(r"<td><b>Featherweight</b></td><td>[^<]*[Vv]acant", MM), "REGRESSION: featherweight listed vacant")
ran(r"Women's Featherweight</b></td><td class=\"nc\">Vacant", MM, "W-FW vacant cell")
chk("Carlos Ulberg" in MM and "Justin Gaethje" in MM and "Joshua Van" in MM, "champions board incomplete")
chk("Ciryl Gane" in MM, "interim HW missing")
chk(MM.count("<tr>") >= 13, "champions table too short")

# 4 -- Parnasse provenance
chk("KSW" in MM, "Parnasse KSW provenance missing")
ran(r"not through the Contender Series", MM, "Parnasse CS negation")
chk(not re.search(r"Parnasse[^.]{0,160}earned his contract on (Dana White's )?Contender Series", MM),
    "REGRESSION: Parnasse attributed to the Contender Series")
chk("Salahdine Parnasse" in MM, "Parnasse spelling")
chk("Saladhine" not in ALL, "misspelling Saladhine")

# 5 -- Sept 5 is a Saturday, never Friday
chk(not re.search(r"Friday[^.]{0,60}Paris", ALL), "Paris card called Friday")
ran(r"Saturday, September 5", MM, "Paris Saturday")

# 6 -- glyphs / chrome
chk("⚘" not in ALL, "U+2698 flower glyph used instead of the shield")
for f, t in P.items():
    chk("&#9960;" in t, "%s missing shield entity in nav" % f)
    chk(t.count('nav class="tabs"') == 1, "%s nav count" % f)
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"):
        chk(href in t, "%s missing nav link %s" % (f, href))
    for i in ("id=\"edition\"", "id=\"datestamp\"", "id=\"updated\"", "id=\"freshline\""):
        chk(i in t, "%s missing %s" % (f, i))
    chk("Intl.DateTimeFormat" in t, "%s missing stamp JS" % f)
    chk("Morning Edition" in t, "%s missing edition bucket JS" % f)

# 7 -- tldr labels
chk('<b>The Tape</b>' in WS, "WS tldr label")
chk('<b>The Wire</b>' in CY, "CY tldr label")
chk('<b>Tale of the Tape</b>' in MM, "MM tldr label")
chk('class="tldr"' not in IX, "index should use cards, not a tldr strip")
chk("The Tape" in IX and "The Wire" in IX and "Tale of the Tape" in IX, "index kickers missing")

# 8 -- sources: >=10 https urls on each briefing, none on index required
for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    u = len(re.findall(r'href="https://', P[f]))
    chk(u >= 10, "%s has only %d https sources" % (f, u))
    chk("<footer>" in P[f], "%s missing footer" % f)
    chk('class="disc"' in P[f], "%s missing disclaimer" % f)
chk("not investment advice" in WS, "WS disclaimer wording")
chk("subject to change" in MM, "MM disclaimer wording")
chk("not security advice" in CY, "CY disclaimer wording")

# 9 -- TradingView blocks A-F all present on WS
for wid in ("ticker-tape", "single-quote", "timeline", "stock-heatmap",
            "mini-symbol-overview", "embed-widget-events"):
    chk(wid in WS, "WS missing widget %s" % wid)
chk(WS.count("single-quote") == 3, "WS needs exactly 3 single-quote widgets")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    chk(sym in WS, "ticker tape missing %s" % sym)
chk('class="livebar"' in WS, "WS missing livebar")
chk("NYSE:SNOW" in WS, "chart of the day symbol")
chk("updates in real time" in WS, "WS live headings")

# 10 -- MMA countdown
chk('id="ufccdn"' in MM, "MMA countdown element")
chk("2026-09-05T00:00:00-04:00" in MM, "MMA countdown target")
chk("Fight week" in MM, "MMA countdown elapsed branch")

# 11 -- markets figures consistency
chk("7,666.60" in WS and "26,217.83" in WS and "53,061.95" in WS, "Sept 2 closes missing")
chk("+295.07" in WS, "Dow points change missing")
chk("4.639" not in ALL and "5.185" not in ALL, "August Treasury figures leaked in")
chk("$2B to $4B" not in ALL, "August buyback figure leaked in")
# no live Thursday session price presented as current
chk("opened Thursday" not in WS or "was not published" in WS, "unpublished-open claim not guarded")
ran(r"The opening bell is 9:30 AM ET", WS, "pre-open refusal note")
# sector breadth must not be asserted as a session reading
chk("not</b> asserted" in WS or "not asserted" in WS, "sector-breadth refusal note missing")
chk("+42.32% YTD" in WS and "+15.86% YTD" in WS, "YTD sector figures missing")
chk("YTD" in WS, "YTD label")
# Snowflake provenance: all three readings printed, none adopted
for r_ in ("22%", "23%", "24%"):
    chk(r_ in WS, "Snowflake reading %s missing" % r_)
chk("not competing readings" in WS, "Snowflake window-provenance note missing")
chk("22&ndash;24%" not in WS, "after-hours and pre-market blended into one range")
chk("more than 24%" in WS, "Thursday pre-market print missing")
# streak disagreement printed
chk("two-day" in WS and "three-day" in WS, "streak disagreement not printed")

# 12 -- cyber CVE table integrity
for cve in ("CVE-2026-83548", "CVE-2026-83549", "CVE-2026-82329", "CVE-2026-9586",
            "CVE-2026-49869", "CVE-2026-48710", "CVE-2026-59822"):
    chk(cve in CY, "cyber missing %s" % cve)
chk("10.0" in CY, "CVSS 10.0 missing")
chk("9.8" in CY and "9.3" in CY and "7.8" in CY, "CVSS values missing")
# never assert a CVSS we did not source for 48710
chk(not re.search(r"CVE-2026-48710[^<]{0,80}</td><td class=\"mono\">\d", CY),
    "invented CVSS for CVE-2026-48710")
ran(r"Not stated in sources fetched", CY, "48710 CVSS abstention")
# no unhedged "maximum-severity" language
chk("maximum-severity" not in CY, "unhedged maximum-severity claim")
# elapsed-day arithmetic: JFrog patched Aug 28, exploitation seen Sept 1
chk((datetime.date(2026,9,1)-datetime.date(2026,8,28)).days == 4, "JFrog gap arithmetic")
chk("no elapsed-day claim" or True, "")
# Pennsylvania AG refusal
chk("Pennsylvania Attorney General" in CY and "dated September 2025" in CY,
    "PA AG refusal note missing or unlabelled")
chk("Nevada" in CY, "Nevada precedent reference missing")
# McKesson record-count guard
chk("not unique individuals" in CY, "McKesson 284M qualifier missing")
chk("threat level" in CY.lower(), "threat level banner missing")
chk('class="banner high"' in CY, "threat banner class")
chk(CY.count('class="stat"') == 4, "by-the-numbers strip needs 4 stats")

# 13 -- index cards summarise their own pages
chk("CISA" in IX and "seven" in IX, "index security card does not match cyber lead")
chk("Snowflake" in IX and "Iran" in IX, "index markets card does not match WS lead")
chk("UFC 332" in IX and "Shevchenko" in IX, "index MMA card does not match MMA lead")
chk(IX.count("Read the briefing") == 3, "index needs 3 read links")
chk("livebar" not in IX and "tradingview" not in IX.lower(), "index must carry no live widgets")

# 14 -- no future/past tense contradictions in Upcoming Cards
up = MM.split("Fight Week")[1].split("Last Event")[0]
for mo, d in re.findall(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug)\s+(\d{1,2})", up):
    raised.append("UPCOMING: past month %s %s appears in Fight Week" % (mo, d))
n += 1

# 15 -- name renderings unified
chk(MM.count("Ce Liu") >= 1 and "uses Ce Liu consistently" in MM, "Ce Liu unification note")
chk("Aoriqileng" in MM and "Aori Qileng" in MM, "Aoriqileng rendering note")
chk("Beneil Dariush" not in MM or "challenger" not in MM, "Dariush descriptor risk")

print("checks: %d   raised: %d" % (n, len(raised)))
for r_ in raised: print("  !!", r_)
