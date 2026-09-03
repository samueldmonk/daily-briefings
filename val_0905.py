# -*- coding: utf-8 -*-
"""Guards for the 9:05 AM ET Thursday, September 3, 2026 Morning Edition."""
import io, os, re, sys

OUT = "/sessions/inspiring-practical-pasteur/mnt/outputs"
P = {k: io.open(os.path.join(OUT, v), encoding="utf-8").read()
     for k, v in [("ix", "index.html"), ("cy", "cyber-briefing.html"),
                  ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]}
ALL = "\n".join(P.values())
fails, checks = [], 0

def must(page, needle, why):
    global checks
    checks += 1
    if needle not in P[page]:
        fails.append("MISSING [%s] %s :: %r" % (page, why, needle[:90]))

def never(page, needle, why):
    global checks
    checks += 1
    if needle in P[page]:
        fails.append("FORBIDDEN [%s] %s :: %r" % (page, why, needle[:90]))

def never_re(page, pat, why):
    global checks
    checks += 1
    m = re.search(pat, P[page])
    if m:
        fails.append("FORBIDDEN-RE [%s] %s :: %r" % (page, why, m.group(0)[:90]))

# ---------------------------------------------------------------- structure
for k in P:
    must(k, 'id="edition"', "edition pill")
    must(k, 'id="datestamp"', "date pill")
    must(k, 'id="updated"', "updated pill")
    must(k, 'id="freshline"', "freshness line")
    must(k, 'briefings refresh every 30 minutes', "freshness JS text")
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"):
        must(k, 'href="%s"' % href, "five-tab nav -> " + href)
for k in ("cy", "ws", "mma"):
    must(k, '<div class="tldr">', "summary strip")
must(ws := "ws", "<b>The Tape</b>", "tape label")
must("cy", "<b>The Wire</b>", "wire label")
must("mma", "<b>Tale of the Tape</b>", "tale label")

# ---------------------------------------------------------------- live widgets
for wid in ("ticker-tape", "single-quote", "timeline", "stock-heatmap",
            "mini-symbol-overview", "events"):
    must("ws", "embed-widget-%s.js" % wid, "TradingView block " + wid)
must("ws", 'FOREXCOM:SPXUSD', "S&P widget"); must("ws", 'FOREXCOM:NSXUSD', "Nasdaq widget")
must("ws", 'FOREXCOM:DJI', "Dow widget"); must("ws", 'TVC:USOIL', "oil in tape")
must("ws", 'TVC:US10Y', "10Y in tape")
never("ix", "embed-widget-", "no live widgets on the front page")
never("mma", "embed-widget-", "no live widgets on the MMA page")

# ---------------------------------------------------------------- CYBER facts
must("cy", "CVE-2026-82329", "Artifactory CVE")
must("cy", "CVSS 9.8", "Artifactory CVSS from vendor/coverage")
must("cy", "August 28, 2026", "JFrog disclosure date")
must("cy", "September 5", "Sept 5 KEV deadline")
must("cy", "2 days left", "Sept 5 countdown")
must("cy", "11 days left", "Sept 14 countdown")
must("cy", "13 days left", "Sept 16 countdown")
must("cy", "September 14", "PaperCut deadline in KEV list")
# Patch Priority and the KEV section must agree on the PaperCut date
head = P["cy"].split("<h2 class=\"sec\">Threat Actor Spotlight</h2>")[0]
checks += 1
if "September 14" not in head:
    fails.append("Patch Priority box does not carry the September 14 PaperCut deadline")
must("cy", "9,540,683", "Aesto exact HHS figure")
must("cy", "December 2 and 18, 2025", "Aesto incident window")
must("cy", "May 26, 2026", "Aesto confirmation date")
must("cy", "August 25, 2026", "McKesson detection date")
must("cy", "$55.2 million", "McKesson ransom demand")
must("cy", "284 million", "McKesson claim reading A")
must("cy", "248 million", "McKesson claim reading B")
never("cy", "284 million patients", "record claim must not be rendered as people")
never("cy", "284 million individuals", "record claim must not be rendered as people")
# refusals
must("cy", "Pennsylvania Attorney", "Penn AG refusal is described")
must("cy", "September 2025", "Penn AG dated to 2025")
never("cy", "5.7 terabyte claim was", "refused claim must not be asserted as fact")
must("cy", "TeamPCP", "TeamPCP refusal recorded")
must("cy", "March 19&ndash;27, 2026", "TeamPCP correct date")
never("cy", "Nevada statewide ransomware incident as a 2026 breach.</div>x", "sentinel")
never_re("cy", r"TeamPCP[^<]{0,200}this week", "TeamPCP must not be called this week's news")
# Elementor must not appear in the federal deadline list
kev = P["cy"].split('CISA KEV &amp; Federal Deadlines')[-1].split('<h5>Sources')[0]
checks += 1
if "CVE-2026-32475" in kev:
    fails.append("Elementor CVE appears inside the federal-deadline section")
never("cy", "Elementor Pro is being actively exploited", "unasserted exploitation")
# no CVSS digit invented for 48710
checks += 1
row = [r for r in P["cy"].split("<tr>") if "CVE-2026-48710" in r]
if row and re.search(r"<td class=\"mono\">\s*\d", row[0].split("</td>")[1] if len(row[0].split("</td>")) > 1 else ""):
    fails.append("CVE-2026-48710 was given a numeric CVSS")
must("cy", "Not stated in sources fetched", "48710 CVSS withheld")
# KEV deadline bullets in chronological order
kevlist = re.findall(r"September (\d+), 2026</b>", kev)
checks += 1
if [int(x) for x in kevlist] != sorted(int(x) for x in kevlist):
    fails.append("KEV deadline bullets out of chronological order: %s" % kevlist)

# ---------------------------------------------------------------- MARKETS facts
must("ws", "53,430.00", "Dow futures level")
must("ws", "7,699.50", "S&P futures level")
must("ws", "29,233.00", "Nasdaq futures level")
must("ws", "206,000", "jobless claims actual")
must("ws", "205,000", "claims consensus")
must("ws", "204,000", "prior week claims")
never("ws", "no actual figure appeared", "claims refusal is obsolete this run")
never_re("ws", r"claims (came in at|rose to) 20[35],000", "claims figure must be 206,000")
must("ws", "7,666.60", "S&P Sept 2 close")
must("ws", "26,217.83", "Nasdaq Sept 2 close")
must("ws", "53,061.95", "Dow Sept 2 close")
must("ws", "+295.07", "Dow points change")
must("ws", "$90.87", "WTI this run")
must("ws", "$95.25", "Brent reading A")
must("ws", "$99.38", "Brent reading B")
must("ws", "4.796%", "10-year prior close")
must("ws", "$1.65 to $1.80", "Campbell's guidance range")
must("ws", "$1.83", "Campbell's FactSet consensus")
must("ws", "$34.8 billion", "Broadcom guide")
must("ws", "$35.03 billion", "Broadcom estimate")
must("ws", "NYSE:SNOW", "Chart of the Day symbol")
must("ws", "&minus;5.60% YTD", "XLC YTD")
must("ws", "&minus;3.02% YTD", "XLY YTD")
must("ws", "+42.32%", "XLE YTD")
must("ws", "thirteenth consecutive edition", "sector refusal count")
# refused sector single-day figures must not be reprinted
never("ws", "7,631.47", "refused sector-piece index level must not be reprinted")
never("ws", "declined 0.71%", "refused sector-piece daily move must not be reprinted")
never("ws", "materials <span", "materials YTD not re-sourced this run")
never("ws", "+15.86%", "materials figure not re-sourced this run")
# superlative scoping: no small-cap numbers reprinted unsourced
never("ws", "44.40%", "unsourced small-cap figure")
never("ws", "44.46%", "unsourced small-cap figure")
never("ws", "29.40%", "unsourced small-cap figure")
# Moderna dropped (no figure sourced this run)
never("ws", "Rothschild", "Moderna downgrade not re-sourced this run")
# pre-open honesty
must("ws", "opening bell is 9:30 AM ET", "pre-open statement")
must("ws", "Pre-open &middot; ~9:05 AM ET", "as-of stamp")
never("ws", "Pre-open &middot; ~8:40 AM ET", "stale as-of stamp")
never_re("ws", r"stocks (are )?(rose|fell) (today|Thursday) (in|during) (the )?session", "no live Thursday session claim")
# eight consecutive fetches
must("ws", "<b>eight</b>", "close-fetch streak count")

# ---------------------------------------------------------------- MMA facts
must("mma", "Carlos Ulberg", "LHW champ")
never("mma", "<td>Alex Pereira</td>", "Pereira must not be listed as champion")
must("mma", "Sean Strickland", "MW champ")
never("mma", "<td>Khamzat Chimaev</td>", "Chimaev must not be listed as champion")
must("mma", "Alexander Volkanovski", "FW champ, not vacant")
must("mma", "Justin Gaethje", "LW champ")
must("mma", "Islam Makhachev", "WW champ")
must("mma", "Tom Aspinall", "HW champ")
must("mma", "Petr Yan", "BW champ")
must("mma", "Joshua Van", "FLW champ")
must("mma", "Mackenzie Dern", "WSW champ")
must("mma", "Valentina Shevchenko", "WFLW champ")
must("mma", "Kayla Harrison", "WBW champ")
must("mma", "thirtieth time", "stale-list occurrence count")
must("mma", "3:45 of round one", "Ulberg KO time")
must("mma", "Kaseya Center", "UFC 327 venue")
must("mma", "31-7", "Strickland record")
must("mma", "17-1", "Chimaev record")
# Parnasse provenance
must("mma", "KSW featherweight champion", "Parnasse KSW provenance")
never("mma", "Parnasse, who earned his contract on Dana White", "Contender Series regression")
never_re("mma", r"Parnasse[^<]{0,120}Contender Series signee", "Contender Series regression")
must("mma", "not through the Contender Series", "explicit denial retained")
# Salkilld / Dariush standing corrections
never("mma", "Cody Salkilld", "wrong first name")
never_re("mma", r"Dariush[^<]{0,60}(former champion|title challenger)", "Dariush descriptor")
# cards
must("mma", "Quentin Pasley", "DWCS wk5 full name A")
must("mma", "Arlind Berisha", "DWCS wk5 full name B")
never("mma", "gives surnames only", "obsolete surnames caveat")
never("mma", "no date had been sourced", "obsolete missing-date line")
must("mma", "Rosas Jr. vs. Barcelos", "Sept 26 card")
must("mma", "Jose Miguel Delgado", "Noche headliner")
must("mma", "David Mart&iacute;nez", "Noche card addition")
must("mma", "$7.7 billion", "rights deal")
must("mma", "$1.1 billion a year", "annual value")
must("mma", "43 annual UFC live events", "event count")
never("mma", "34 million total global viewers", "viewership not re-sourced this run")
never("mma", "7.0 million", "viewership not re-sourced this run")
never("mma", "8 million viewers", "viewership not re-sourced this run")
# counted-claim guard: "One September title fight" must name exactly one
checks += 1
m = re.search(r"<b>(One|Two|Three) September title fight", P["mma"])
if m:
    seg = P["mma"][m.start():m.start() + 600]
    want = {"One": 1, "Two": 2, "Three": 3}[m.group(1)]
    got = len(re.findall(r"UFC \d{3}|Noche UFC", seg))
    if got < want:
        fails.append("counted claim says %s but names %d events" % (m.group(1), got))
# countdown script
must("mma", "ufccdn", "countdown target")
must("mma", "2026-09-05T00:00:00-04:00", "countdown date")

# ---------------------------------------------------------------- cross-page summary fidelity
checks += 1
if "Artifactory" not in P["ix"]:
    fails.append("index Security card does not reflect the cyber lead")
checks += 1
if "206,000" not in P["ix"]:
    fails.append("index Markets card does not reflect the markets lead")
checks += 1
if "Shevchenko" not in P["ix"]:
    fails.append("index MMA card does not reflect the MMA lead")
checks += 1
for tok in ("Artifactory", "72 hours"):
    if tok not in P["cy"].split('<div class="tldr">')[1][:600] and tok not in P["cy"]:
        fails.append("cyber summary strip drifted from the lead: " + tok)

# ---------------------------------------------------------------- standing corrections
never("cy", "Nevada statewide ransomware attack in August 2026", "Nevada incident permanently excluded")
never("cy", "60+ agencies", "Nevada incident detail")
never("cy", "28-day recovery", "Nevada incident detail")
never("cy", "CVSS 9.8</td><td>NetScaler", "Citrix score")
never("ws", "Snowflake jumped roughly 22", "blended trading windows")
never_re("ws", r"2[24]\s*(&ndash;|-|to)\s*24%", "blended after-hours/pre-market range")
never("mma", "featherweight title is vacant", "FW vacancy regression")
never("mma", "Interim: Alex Pereira", "Pereira interim regression")

# ---------------------------------------------------------------- disclaimers + sources
must("ws", "not investment advice", "markets disclaimer")
must("cy", "not security advice", "cyber disclaimer")
must("mma", "subject to change", "MMA disclaimer")
for k in ("cy", "ws", "mma"):
    must(k, "<h5>Sources", "sources footer")
    checks += 1
    if P[k].count("https://") < 15:
        fails.append("[%s] too few source URLs" % k)

# ---------------------------------------------------------------- read-through guards (0905)
never("cy", "one a supply-chain server that", "C1: a flaw is not a server")
never("cy", "incidents disclosed this week", "C1: disclosure timing overstated")
never("cy", "HIPAA Journal calls it", "C2: unverifiable outlet attribution")
never("cy", "restated in a search return dated today", "C3: desk jargon in reader copy")
never("cy", "5.7 terabyte", "C4: refused figure must not be reprinted")
must("cy", "claimed figure is not", "C4: refusal states the withholding")
must("cy", "CVSS 8.8", "C5: PaperCut 81578 score re-sourced")
must("cy", "9.4", "C5: PaperCut 82078 score re-sourced")
must("cy", "hands-on-keyboard", "C5: PaperCut escalation detail")
never("cy", "dropped from the earlier edition this morning", "C5: stale restoration line")
must("ws", "gives the pre-market move as 24%", "W1: Snowflake percentage reconciled")
never("ws", "the last trading day before September 2, and", "W2: false trading-day claim")
must("ws", "September 1 was itself a", "W2: correction printed")
never("ws", "<b>Also this morning &mdash; July international trade", "W3: pre-release framing")
must("ws", "No actual print appeared in anything fetched", "W3: trade balance withheld")
never("mma", "Coverage fetched for this edition puts it plainly", "M1: desk jargon")
never("mma", "Only the bouts re-sourced in this run", "M2: overstated sourcing claim")
must("mma", "carried from this desk", "M2: honest provenance")
never("mma", "pound-for-pound board in aggregated", "M3: aggregated rankings dropped")
must("mma", "No pound-for-pound or divisional ranking is asserted", "M3: replacement stated")
never("mma", "<td>Champion since April 11, 2026.</td>", "M4: bare LHW date")
must("mma", "files its report under April 12", "M4: UFC 327 discrepancy printed")

print("checks:", checks)
if fails:
    print("RAISED %d" % len(fails))
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("ALL CLEAR")
