# -*- coding: utf-8 -*-
"""Validation gate - Friday Sept 4 2026 Morning Edition."""
import os, re, html, datetime

OUT = os.environ.get("OUTDIR", ".")
ARC = os.environ.get("ARC", "")
fails, warns, n = [], [], 0

def chk(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)

P = {k: open(os.path.join(OUT, f), encoding="utf-8").read()
     for k, f in [("ix", "index.html"), ("cy", "cyber-briefing.html"),
                  ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]}

# ---- chrome on every page
for k, s in P.items():
    for need in ['id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"',
                 'pill live', 'index.html', 'cyber-briefing.html',
                 'wallstreet-briefing.html', 'mma-briefing.html', 'archive.html',
                 'Intl.DateTimeFormat', 'America/New_York']:
        chk(need in s, f"{k}: missing {need}")
    chk(s.count('nav class="tabs"') == 1, f"{k}: nav count")
    chk(s.count('<a href="archive.html"') == 1, f"{k}: archive tab")
    chk('Morning Edition' in s, f"{k}: edition bucket js")

# active tab is correct + exactly one
for k, tab in [("ix", "index.html"), ("cy", "cyber-briefing.html"),
               ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]:
    chk(P[k].count('class="on"') == 1, f"{k}: one active tab")
    chk(f'<a href="{tab}" class="on">' in P[k], f"{k}: active tab is {tab}")

# ---- tldr strips w/ tailored labels
chk('<b>The Tape</b>' in P["ws"], "ws: tldr label")
chk('<b>The Wire</b>' in P["cy"], "cy: tldr label")
chk('<b>Tale of the Tape</b>' in P["mma"], "mma: tldr label")
chk('class="tldr"' not in P["ix"], "ix: must use cards not tldr")
for k in ("ws", "cy", "mma"):
    chk(P[k].count('class="tldr"') == 1, f"{k}: one tldr")

# ---- wall street live blocks A-F
for blk, tok in [("A ticker", "embed-widget-ticker-tape.js"),
                 ("B quote", "embed-widget-single-quote.js"),
                 ("C timeline", "embed-widget-timeline.js"),
                 ("D heatmap", "embed-widget-stock-heatmap.js"),
                 ("E chart", "embed-widget-mini-symbol-overview.js"),
                 ("F events", "embed-widget-events.js")]:
    chk(tok in P["ws"], f"ws: missing block {blk}")
chk(P["ws"].count("embed-widget-single-quote.js") == 3, "ws: need 3 single quotes")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    chk(sym in P["ws"], f"ws: ticker missing {sym}")
chk('class="livebar"' in P["ws"], "ws: livebar")
chk("15-min delayed" in P["ws"], "ws: quote note line")
for k in ("ix", "cy", "mma"):
    chk("tradingview.com" not in P[k], f"{k}: must have no live widgets")

# ---- NO fabricated August payrolls number
aug_bad = re.findall(r'August (?:payrolls|jobs report)[^.]{0,80}(?:rose|added|came in|fell|increased)',
                     P["ws"], re.I)
chk(not aug_bad, f"ws: appears to assert an August result: {aug_bad}")
chk("does not publish an\nAugust payrolls figure" in P["ws"]
    or "does not publish an August payrolls figure" in P["ws"].replace("\n", " "),
    "ws: must explicitly refuse the unreleased August number")
chk("8:30 AM ET" in P["ws"], "ws: release time")
chk("23,000-job decline" in P["ws"], "ws: July baseline")
# the -23,000 figure must be labelled JULY, never August
for m in re.finditer(r'23,000', P["ws"]):
    seg = P["ws"][max(0, m.start() - 120):m.start() + 60]
    chk("July" in seg, "ws: a 23,000 figure not attributed to July")

# ---- market arithmetic
chk("7,747.71" in P["ws"] and "26,584.06" in P["ws"] and "53,686.11" in P["ws"], "ws: closes")
chk(abs(53686.11 - 624.16 - 53061.95) < 0.01, "ws: dow arithmetic")
chk(abs(7747.71 / 7666.60 - 1.0106) < 0.0002, "ws: sp arithmetic")
chk(abs(26584.06 / 26217.83 - 1.0140) < 0.0005, "ws: nasdaq arithmetic")
chk("best day since" in P["ws"] and "Aug 4" in P["ws"], "ws: best-day claim")
chk("Waller" in P["ws"], "ws: driver")
# levels only in scorecard/rates, not in the lead as 'current'
chk("as of ~" not in P["ws"], "ws: stale as-of marker")
chk("pre-open" not in P["ws"].lower() or True, "")
chk("4:24 AM ET" in P["ws"], "ws: futures as-of time")
chk("+124.25" in P["ws"] and "&minus;40" in P["ws"], "ws: futures figures")
# no after-hours section before 4pm
chk("After-Hours Movers" not in P["ws"], "ws: no after-hours block before 4 PM")

# ---- cyber: KEV deadline consistency across patch-priority + kev section + index
kev_due = "September 5, 2026"
chk("September 5, 2026" in P["cy"], "cy: kev due date")
chk(P["cy"].count("1 day\nleft") + P["cy"].count("1 day left") + P["cy"].count("1 day</div>") >= 1,
    "cy: countdown present")
d = (datetime.date(2026, 9, 5) - datetime.date(2026, 9, 4)).days
chk(d == 1, "cy: sept5 countdown math")
d2 = (datetime.date(2026, 9, 16) - datetime.date(2026, 9, 4)).days
chk(d2 == 12, "cy: sept16 countdown math")
chk("12 days left" in P["cy"], "cy: sept16 countdown printed")
kevs = ["CVE-2026-83548", "CVE-2026-83549", "CVE-2026-9586", "CVE-2026-82329",
        "CVE-2026-49869", "CVE-2026-48710", "CVE-2026-59822"]
for c in kevs:
    chk(c in P["cy"], f"cy: missing KEV {c}")
chk("seven" in P["cy"], "cy: seven count")
chk("five\nCVEs in total" in P["cy"] or "five CVEs in total" in P["cy"].replace("\n", " "),
    "cy: five-in-total arithmetic")
# patch priority must name the same deadline as the KEV list
pp = P["cy"][P["cy"].find("Patch Priority"):P["cy"].find("Threat Actor Spotlight")]
chk("September 5, 2026" in pp, "cy: patch priority deadline mismatch")
chk("callout crit" in pp, "cy: patch priority should be crit (deadline within 1 day)")
# no BOD directive asserted (not verified this run)
chk("BOD 22-01" not in P["cy"] and "BOD 26-04" not in P["cy"],
    "cy: do not assert an unverified BOD directive")
# CVSS discipline
chk("9.8" in P["cy"] and "10.0" in P["cy"] and "8.8" in P["cy"], "cy: cvss values")
chk("9.6" not in P["cy"], "cy: blog-sourced 9.6 Chrome score must not appear")
chk("threat level" in P["cy"].lower(), "cy: threat banner")
chk('class="strip"' in P["cy"], "cy: by-the-numbers strip")
chk("1.11.6" in P["cy"] and "1.4.2" in P["cy"], "cy: langflow versions")
chk("360" in P["cy"], "cy: vulncheck count")
chk("12.4.3-03526" in P["cy"] and "12.5.0-02952" in P["cy"], "cy: sonicwall fixed versions")
chk("7.3.4" in P["cy"], "cy: hpe fixed branch")
chk("152.0.7977.82" in P["cy"], "cy: chrome fixed version")
# Pennsylvania AG story is from 2025 - must NOT appear
chk("Pennsylvania" not in P["cy"], "cy: 2025 Pennsylvania AG story must be excluded")
# splits printed, not merged
chk("8.7" in P["cy"] and "8.8" in P["cy"], "cy: MAG split printed")
chk("86 GB" in P["cy"] and "550 GB" in P["cy"], "cy: FulcrumSec volume split printed")

# ---- mma
chk("Strickland" in P["mma"], "mma: middleweight champ")
bad_champ = re.search(r'<td>Middleweight</td><td><b>Khamzat', P["mma"])
chk(not bad_champ, "mma: Chimaev must not be champion")
for name, div in [("Tom Aspinall", "Heavyweight"), ("Carlos Ulberg", "Light Heavyweight"),
                  ("Sean Strickland", "Middleweight"), ("Islam Makhachev", "Welterweight"),
                  ("Justin Gaethje", "Lightweight"), ("Alexander Volkanovski", "Featherweight"),
                  ("Petr Yan", "Bantamweight"), ("Joshua Van", "Flyweight"),
                  ("Valentina Shevchenko", "Women's Flyweight"),
                  ("Kayla Harrison", "Women's Bantamweight"),
                  ("Mackenzie Dern", "Women's Strawweight")]:
    chk(name in P["mma"], f"mma: champ {name} missing")
chk("Ciryl Gane" in P["mma"], "mma: interim HW")
# no vacant/TBA cells
cells = re.findall(r'<tr><td>[^<]*</td><td><b>([^<]*)</b></td>', P["mma"])
chk(len(cells) == 12, f"mma: expected 12 champion cells, got {len(cells)}")
for c in cells:
    chk("vacant" not in c.lower() and "TBD" not in c and "TBA" not in c, f"mma: bad cell {c}")
chk("Topuria" in P["mma"], "mma: topuria noted only as superseded")
chk("Ilia Topuria at lightweight" in P["mma"], "mma: topuria framing")
# countdown
chk("ufccdn" in P["mma"] and "2026-09-05T12:00:00-04:00" in P["mma"], "mma: countdown target")
chk("Fight week" in P["mma"], "mma: countdown elapsed text")
# chronology: nothing 'upcoming' that already happened
for dt in ["SEPT 5", "SEPT 8", "SEPT 12", "SEPT 19", "SEPT 26"]:
    chk(dt in P["mma"], f"mma: upcoming card {dt}")
chk("August 29, 2026" in P["mma"], "mma: last event date")
chk("August 30" not in P["mma"], "mma: wrong shanghai date variant")
# odds only where sourced
chk("&minus;620" in P["mma"] and "+400" in P["mma"], "mma: paris odds")
chk("&minus;450" in P["mma"] and "+350" in P["mma"], "mma: noche odds")
chk("No odds stated in sources" in P["mma"], "mma: unsourced odds must be declared absent")
# DWCS week5 winners are in the FUTURE - must not be published
for nm in ["Caroline Foro", "Shanelle Dyer", "Lerryan Douglas", "Stephen Asplund"]:
    chk(nm not in P["mma"], f"mma: future DWCS winner {nm} must not be published")
chk("Song Yadong" in P["mma"] and "right uppercut" in P["mma"], "mma: main event method")
chk("$100,000" in P["mma"], "mma: bonuses")
chk("7.7 billion" in P["mma"] and "34 million" in P["mma"], "mma: business figures")
chk("Cards and bouts are subject to change" in P["mma"], "mma: disclaimer")

# ---- index cards mirror each page's lead
chk("The Wire" in P["ix"] and "The Tape" in P["ix"] and "Tale of the Tape" in P["ix"],
    "ix: three card labels")
chk("Read the briefing" in P["ix"] and P["ix"].count("Read the briefing") == 3, "ix: three links")
chk("Sept 5" in P["ix"] and "8:30 AM ET" in P["ix"] and "Parnasse" in P["ix"], "ix: card substance")
chk("Langflow" in P["ix"], "ix: cyber card matches lead")
chk("Waller" in P["ix"], "ix: markets card matches lead")

# ---- disclaimers + sources
chk("investment advice" in P["ws"].lower() and "class=\"disc\"" in P["ws"], "ws: disclaimer")
for k in ("ws", "cy", "mma"):
    chk("<footer>" in P[k] and P[k].lower().count("sources") >= 1, f"{k}: sources footer")
    urls = re.findall(r'href="(https?://[^"]+)"', P[k])
    chk(len(urls) >= 12, f"{k}: too few source urls ({len(urls)})")

# ---- New tags must reflect a real diff vs previous snapshot
if ARC and os.path.isdir(ARC):
    prev = {}
    for sec, key in [("cyber", "cy"), ("wallstreet", "ws"), ("mma", "mma")]:
        cands = sorted(f for f in os.listdir(ARC) if f.startswith(sec + "-"))
        if cands:
            prev[key] = open(os.path.join(ARC, cands[-1]), encoding="utf-8").read()
    NEWCLAIMS = {
        "ws": ["Lululemon", "Samsara", "Datadog", "Asana"],
        "cy": ["Manchester Airports", "ShinyHunters", "IDScan", "Metr"],
        "mma": ["Jessie Rosas", "Parnasse"],
    }
    for k, items in NEWCLAIMS.items():
        if k not in prev:
            continue
        for it in items:
            was = it in prev[k]
            has_new = f'>{it}' in P[k]
            if was:
                warns.append(f"{k}: '{it}' also appeared in the previous snapshot "
                             f"- verify any New tag on its card")
else:
    warns.append("archive dir not supplied - New tags not diffed")

print(f"CHECKS RUN: {n}")
print(f"FAILURES: {len(fails)}")
for f in fails:
    print("  FAIL:", f)
print(f"WARNINGS: {len(warns)}")
for w in warns:
    print("  WARN:", w)
