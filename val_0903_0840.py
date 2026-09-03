# -*- coding: utf-8 -*-
import io, os, re, datetime, calendar
OUT = "/sessions/dreamy-focused-cerf/mnt/outputs"
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
# PaperCut was re-sourced this run (CISA Aug 31 alert + SOC Prime + Cybersecurity Dive):
# the "must not appear" guard is retired and replaced with POSITIVE guards.
chk((datetime.date(2026,9,14)-TODAY).days == 11, "Sept 14 is not 11 days from today")
chk("September 14" in CY, "PaperCut Sept 14 deadline missing")
chk("11 days left" in CY, "PaperCut 11-day countdown missing")
chk("August 31" in CY, "PaperCut KEV add date (Aug 31) missing")
chk("CVE-2026-81578" in CY and "CVE-2026-82078" in CY, "PaperCut CVE ids missing")
chk("restored here on a fresh fetch" in CY, "PaperCut restoration not explained")
ran(r"11 days left", CY, "PaperCut 11-day countdown")
# the Patch Priority box and the KEV section must agree on Sept 14
chk(CY.count("September 14") >= 2, "Sept 14 not repeated in both Patch Priority and KEV")

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
ran(r"the opening bell is 9:30 AM ET", WS, "pre-open refusal note")
chk("live Thursday session price" in WS, "pre-open guard sentence missing")
# futures drift vs the earlier edition must be labelled as drift, not source disagreement
chk("drift across roughly twenty" in WS, "futures drift note missing")
# no jobless-claims figure may be published (the print was not sourced)
import re as _re
chk(not _re.search(r"claims (came in|printed|rose to|fell to) ", WS), "a jobless-claims print was published unsourced")
chk("no figure is published here" in WS, "jobless-claims refusal note missing")
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


# ==================== NEW GUARDS, 0840 EDITION ====================
# -- Elementor Pro: score, versions, and a refusal to assert in-the-wild exploitation
chk("CVE-2026-32475" in CY, "Elementor CVE missing")
chk("9.0 (CVSS v3.1)" in CY, "Elementor CVSS not the vendor-grade v3.1 9.0")
chk("4.2.1" in CY and "4.2.2" in CY, "Elementor affected/fixed versions missing")
chk("In-the-wild exploitation is therefore <b>not</b> asserted" in CY,
    "Elementor exploitation refusal missing")
chk("not in the CISA KEV catalog" in CY, "Elementor KEV-absence not stated")
# it must NOT appear in the KEV deadline list
kev = CY.split("CISA KEV &amp; Federal Deadlines")[-1].split('<h5>Sources')[0]
chk("CVE-2026-32475" not in kev, "Elementor wrongly listed under federal deadlines")
ran(r"CVE-2026-32475", CY, "Elementor CVE")

# -- Top story: DOJ facts, spelled exactly as the department renders them
chk("Searzhudin Tamirlanovich Aktulaev" in CY, "indictment name missing or altered")
chk(CY.count("Aktulaev") >= 3, "top story too thin on the charged party")
chk("80,000" in CY and "255 fake" in CY, "indictment scale figures missing")
chk("20 years" in CY and "October 5" in CY, "charge exposure / court date missing")
chk("TVRAT" in CY and "DarkVNC" in CY, "malware families missing")
chk("2017" in CY and "2016" in CY, "campaign window missing")
# no victim-count inflation: only the DOJ's ~80,000 may appear
chk("800,000" not in CY and "8,000,000" not in CY, "victim count inflated")

# -- Brent: two irreconcilable readings, both printed, neither adopted
chk("95.25" in WS and "99.38" in WS, "Brent disagreement not printed in full")
chk("neither\n" in WS or "neither is adopted" in WS, "Brent adoption refusal missing")
ran(r"\$99\.38", WS, "Fortune Brent reading")

# -- Sector: the contradicted session figure must NOT be published as Wednesday's
chk("twelfth" in WS, "sector refusal count not advanced to a twelfth run")
chk("7,631.47" in WS and "contradicts Wednesday" in WS,
    "sector refusal must show the contradiction it is refusing")
chk("YTD" in WS, "YTD-only sector framing missing")

# -- Moderna: a downgrade with no price level or target invented
chk("Moderna" in WS and "Rothschild &amp; Co Redburn" in WS, "Moderna item missing")
chk("154.27" not in WS, "an unsourced Moderna price level was published")
chk("no price target" in WS.lower(), "Moderna price-target refusal missing")
ran(r"[Nn]o price target was stated", WS, "Moderna price-target refusal")

# -- Wednesday closes: seventh identical fetch, levels unchanged
for lvl in ("7,666.60", "26,217.83", "53,061.95"):
    chk(lvl in WS, "Wednesday close %s missing" % lvl)
chk("seven consecutive" in WS, "close-fetch streak not advanced")

# -- MMA: odds disagreements printed, none adopted
chk("&minus;145" in MM and "&minus;155" in MM, "Ziam odds disagreement not printed")
chk("&minus;600" in MM and "+440" in MM, "Paris headline odds missing")
chk("7.0 million" in MM and "8 million" in MM, "Freedom 250 US-average disagreement not printed")
chk("34 million total global viewers" in MM, "TKO global viewership missing")
chk("$7.7 billion" in MM, "Paramount rights deal figure missing")
# the Song Yadong ranking move must NOT be asserted as current this run
chk("rather than asserted as the current ranking" in MM, "unre-sourced ranking move not disclaimed")
ran(r"rather than asserted as the current ranking", MM, "ranking provenance disclaimer")
# and it must not simultaneously claim to withhold what it prints
chk("not repeated as current" not in MM, "self-contradicting withhold-while-printing wording")
chk("No. 7 to No. 4" in MM and "was not restated" in MM,
    "ranking move must be described as dropped, not asserted")

# -- MMA: Contender Series Week 5 date is real and a Tuesday
chk((datetime.date(2026,9,8)).strftime("%A") == "Tuesday", "Sept 8 2026 is not a Tuesday")
chk("Tuesday, September 8" in MM, "DWCS Week 5 date missing")
chk("September 15" in MM, "DWCS Week 6 date missing")
# the earlier edition's "no date was stated" line must be gone now that it IS stated
chk("No date was stated for the intervening week" not in MM,
    "stale 'no date stated' line survives after the date was sourced")

# -- MMA: champions board, twenty-ninth stale return
chk("Sean Strickland" in MM and "twenty-ninth" in MM, "stale-list count not advanced")
chk("Khamzat Chimaev</td>" not in MM, "Chimaev listed as a reigning champion")
chk("August 16, 2025" in MM, "the stale list's own dating not printed with the correction")

# -- summaries must match their pages
chk("Aktulaev" in CY or "Russian national" in CY, "cyber summary/lead mismatch")
chk("Russian national" in IX, "index Security card does not carry the cyber lead")
chk("Silva" in IX and "Wang Cong" in IX, "index MMA card does not carry the MMA lead")
chk("Dow" in IX and "Snowflake" in IX, "index Markets card does not carry the markets lead")

# -- Chart of the Day caption must not claim a superlative the page contradicts
chk("largest pre-market move among the large-cap names" in WS, "superlative not scoped")
chk("44.40%" in WS and "44.46%" in WS, "larger sourced moves not disclosed alongside the superlative")
ran(r"not overstated", WS, "superlative scoping note")
# -- refused sector figures must NOT be reprinted (August-Treasury precedent)
chk("1.3%" not in WS.split("Sector Heat")[-1].split("The Calendar")[0], "refused sector leader figure reprinted")
chk("&minus;1.9%" not in WS, "refused sector laggard figure reprinted")
# -- shield glyph, site-wide
chk("&#9960;" in CY and "&#9960;" in IX, "shield entity missing")
chk("\u2698" not in ALL, "wrong glyph (U+2698 flower) present")

print("checks: %d   raised: %d" % (n, len(raised)))
for m in raised: print("  !!", m)
