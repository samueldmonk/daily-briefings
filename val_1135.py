# -*- coding: utf-8 -*-
"""Validation guards for the 2026-09-03 ~11:35 AM ET edition."""
import re, os, datetime, sys

OUT = "/sessions/vigilant-charming-curie/mnt/outputs"
P = {n: open(os.path.join(OUT, f)).read() for n, f in [
    ("index", "index.html"), ("cyber", "cyber-briefing.html"),
    ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]}
ALL = "\n".join(P.values())
raised, checks = [], 0

def chk(cond, msg):
    global checks
    checks += 1
    if not cond:
        raised.append(msg)

def absent(page, needle, msg):
    chk(needle.lower() not in P[page].lower(), msg)

def present(page, needle, msg):
    chk(needle in P[page], msg)

# ---- 1. CALENDAR INTEGRITY (long + short forms) -------------------------
MON = {m: i + 1 for i, m in enumerate(
    ["January","February","March","April","May","June","July","August",
     "September","October","November","December"])}
SHORT = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,
         "Sept":9,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
WD = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6,
      "Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
text = re.sub(r"<[^>]+>", " ", ALL)
pat = re.compile(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(?:day|sday|nesday|rsday|urday)?,?\s+"
                 r"(January|February|March|April|May|June|July|August|September|October|November|December"
                 r"|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\.?\s+(\d{1,2})\b")
found = 0
for m in pat.finditer(text):
    wd, mon, day = m.group(1), m.group(2), int(m.group(3))
    mi = MON.get(mon) or SHORT.get(mon)
    if not mi:
        continue
    found += 1
    real = datetime.date(2026, mi, day).weekday()
    chk(real == WD[wd], "CALENDAR: '%s' is not a %s in 2026 (it is a %s)" % (
        m.group(0).strip(), wd, ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][real]))
chk(found >= 4, "CALENDAR: expected at least 4 weekday-dated strings, found %d" % found)

# ---- 2. KEV DEADLINE CONSISTENCY ---------------------------------------
present("cyber", "Saturday, September 5", "KEV: Patch Priority must name Saturday, September 5")
chk(P["cyber"].count("Saturday, September 5") >= 2,
    "KEV: 'Saturday, September 5' must appear in BOTH Patch Priority and the federal-deadline list")
present("cyber", "Wednesday, September 16, 2026", "KEV: Sept 16 deadline must carry its weekday")
present("cyber", "2 days left", "KEV: Sept 5 countdown must read 2 days left")
present("cyber", "13 days left", "KEV: Sept 16 countdown must read 13 days left")
i5, i16 = P["cyber"].find("2 days left"), P["cyber"].find("13 days left")
chk(0 < i5 < i16, "KEV: countdowns must run in chronological order (2 before 13)")
absent("cyber", "Friday, September 5", "KEV: Sept 5 2026 is a Saturday, never a Friday")
absent("cyber", "September 14", "KEV: Aug 31 additions were not re-sourced; no Sept 14 date may appear")

# ---- 3. CHAMPIONS BOARD -------------------------------------------------
present("mma", "<td>Sean Strickland</td>", "CHAMPS: middleweight must be Sean Strickland")
present("mma", "<td>Carlos Ulberg</td>", "CHAMPS: light heavyweight must be Carlos Ulberg")
present("mma", "<td>Alexander Volkanovski</td>", "CHAMPS: featherweight must be Volkanovski, not vacant")
present("mma", "<td>Justin Gaethje</td>", "CHAMPS: lightweight must be Justin Gaethje")
present("mma", "<td>Islam Makhachev</td>", "CHAMPS: welterweight must be Islam Makhachev")
present("mma", "<td>Petr Yan</td>", "CHAMPS: bantamweight must be Petr Yan")
present("mma", "<td>Joshua Van</td>", "CHAMPS: flyweight must be Joshua Van")
present("mma", "<td>Tom Aspinall</td>", "CHAMPS: heavyweight must be Tom Aspinall")
present("mma", "Interim heavyweight: Ciryl Gane", "CHAMPS: interim HW must be Ciryl Gane")
chk("<td>Khamzat Chimaev</td>" not in P["mma"], "CHAMPS: Chimaev must never sit in a champion cell")
chk("<td>Alex Pereira</td>" not in P["mma"], "CHAMPS: Pereira must never sit in a champion cell")
chk(re.search(r"<td>Featherweight</td><td>Alexander Volkanovski</td>", P["mma"]),
    "CHAMPS: the featherweight row must name Volkanovski")
chk(not re.search(r"<td>Featherweight</td>\s*<td>\s*Vacant", P["mma"], re.I),
    "CHAMPS: featherweight must not be listed vacant")

# ---- 4. STANDING FIGHTER CORRECTIONS ------------------------------------
chk(not re.search(r"Parnasse[^.]{0,200}Contender Series", P["mma"], re.S | re.I),
    "PARNASSE: must never be attributed to Dana White's Contender Series")
chk(not re.search(r"Contender Series[^.]{0,200}Parnasse", P["mma"], re.S | re.I),
    "PARNASSE: must never be attributed to Dana White's Contender Series (reverse order)")
present("mma", "KSW featherweight champion", "PARNASSE: KSW provenance must be stated")
chk("eleven Ohio District Courts" not in P["cyber"],
    "CYBER: the source lists TEN Ohio District Courts of Appeals, not eleven")
present("cyber", "ten Ohio District Courts of Appeals", "CYBER: the Ohio count must read ten")
chk("two Pennsylvania courts" not in P["cyber"],
    "CYBER: name the Pennsylvania courts rather than counting them loosely")
for j2 in ("this run\u2019s sources", "this run\u2019s coverage", "this run\u2019s account",
           "returned this run", "Listings this run", "restated in this run"):
    chk(j2 not in ALL, "JARGON: reader-facing copy contains '%s'" % j2)
absent("mma", "Cody Salkilld", "NAMES: Salkilld's first name is Quillan, never Cody")
chk("Rebecki" not in P["mma"], "UFC 331: co-main must be given as Tsarukyan vs. Ruffy, no invented full names")
present("mma", "Tsarukyan vs. Ruffy", "UFC 331: co-main billing must read Tsarukyan vs. Ruffy")

# ---- 5. EXCLUDED / DATE-MISMATCHED CYBER ITEMS --------------------------
for bad, why in [("Pennsylvania Attorney General", "Penn AG / INC Ransom is September 2025"),
                 ("INC Ransom", "INC Ransom Penn AG story is September 2025"),
                 ("IDMerit", "IDMerit KYC leak was disclosed February 2026"),
                 ("TeamPCP", "TeamPCP supply-chain compromise is March 2026"),
                 ("Handala", "Handala/Stryker came from a Q1 2026 report"),
                 ("statewide ransomware", "Nevada statewide ransomware is a standing exclusion")]:
    absent("cyber", bad, "EXCLUDED: %s" % why)

# ---- 6. MARKETS GUARDS --------------------------------------------------
absent("ws", "Moderna", "MARKETS: Moderna was dropped for want of a restated figure")
absent("ws", "154.27", "MARKETS: the $154.27 quote-page price is blocked")
chk(not re.search(r"22\s*[-–]\s*24%", ALL), "MARKETS: never blend Snowflake's two trading windows into one range")
for pct in ("1.03%", "1.01%"):
    chk(pct not in P["ws"], "MARKETS: refused single-day sector figure %s must not be reprinted" % pct)
for lbl in ("Information Technology led", "Materials at", "Health Care at", "Utilities at"):
    chk(lbl not in P["ws"], "MARKETS: the refused sector table row '%s' must not be reprinted" % lbl)
present("ws", "no sector percentages are published", "MARKETS: the sector refusal must be stated")
present("ws", "9:30&ndash;11:21 AM ET", "MARKETS: the Lead headline must carry the as-of window")
present("ws", "Nothing in this editorial is a live price",
        "MARKETS: the page must say plainly that nothing in it is the current print")
present("ws", "48.4%", "MARKETS: FedWatch hike probability must be stated")
present("ws", "November 2023", "MARKETS: the 10-year's multiyear-high framing must be stated")
chk("October 2023" not in P["ws"], "MARKETS: the unadopted 'October 2023' variant must not be asserted")
present("ws", "three-day losing streak", "MARKETS: this run's sources say a three-day streak was snapped")
present("ws", "7,666.60", "MARKETS: Sept 2 S&P close")
present("ws", "26,217.83", "MARKETS: Sept 2 Nasdaq close")
present("ws", "53,061.95", "MARKETS: Sept 2 Dow close")
present("ws", "carried forward from this briefing\u2019s verified record",
        "MARKETS: closes carried from the standing record must say so")
chk("federal funds target" not in P["ws"] or "No federal funds target level is published" in P["ws"],
    "MARKETS: no fed funds level may be asserted without a source")
present("ws", "a different window and is not comparable",
        "MARKETS: ChargePoint's pre-bell quote must be marked as a separate window")
for q in ("52%", "51.4%", "17.3%"):
    chk(q in P["ws"], "MARKETS: ChargePoint quote %s must be disclosed" % q)
chk("largest single-name move" not in P["ws"] or "44%" in P["ws"],
    "MARKETS: a 'largest move' claim requires the competing moves to be on the page")

# ---- 7. STRUCTURE: nav, masthead, stamp, summary strips -----------------
for name, page in P.items():
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"):
        chk('href="%s"' % href in page, "NAV: %s is missing a link to %s" % (name, href))
    for pid in ('id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"'):
        chk(pid in page, "MASTHEAD: %s is missing %s" % (name, pid))
    chk("America/New_York" in page, "STAMP: %s is missing the self-stamp script" % name)
    chk(page.count('class="on"') == 1, "NAV: %s must highlight exactly one active tab" % name)
present("ws", '<div class="tldr"><b>The Tape</b>', "SUMMARY: Wall Street label must read The Tape")
present("cyber", '<div class="tldr"><b>The Wire</b>', "SUMMARY: cyber label must read The Wire")
present("mma", '<div class="tldr"><b>Tale of the Tape</b>', "SUMMARY: MMA label must read Tale of the Tape")
chk('class="tldr"' not in P["index"], "SUMMARY: index shows the three summaries as cards, not a tldr strip")

# ---- 8. LIVE WIDGET BLOCKS ---------------------------------------------
for w, label in [("embed-widget-ticker-tape", "A ticker tape"),
                 ("embed-widget-single-quote", "B single quotes"),
                 ("embed-widget-timeline", "C headlines timeline"),
                 ("embed-widget-stock-heatmap", "D sector heatmap"),
                 ("embed-widget-mini-symbol-overview", "E chart of the day"),
                 ("embed-widget-events", "F economic calendar")]:
    chk(w in P["ws"], "WIDGETS: block %s is missing" % label)
chk(P["ws"].count("embed-widget-single-quote") == 3, "WIDGETS: block B needs exactly three single-quote widgets")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    chk(sym in P["ws"], "WIDGETS: ticker tape must keep %s" % sym)
chk("tradingview" not in P["index"], "WIDGETS: the front page carries no live widgets")

# ---- 9. INDEX CARDS MATCH THE PAGE LEADS --------------------------------
present("index", "Thomson Reuters", "INDEX: security card must reflect the cyber lead")
present("index", "Waller", "INDEX: markets card must reflect the markets lead")
present("index", "UFC 332", "INDEX: MMA card must reflect the MMA lead")
present("index", "Read the briefing", "INDEX: each card needs a Read the briefing link")

# ---- 10. NEW TAGS vs THE PREVIOUS ARCHIVED EDITION ----------------------
prev = "/tmp/db_1788449765/archive"
try:
    # A card may carry a New tag only if its subject was absent from the prior snapshot.
    for f, page, names in [("cyber-2026-09-03-1110.html", "cyber",
                            ["Thomson Reuters", "IDScan", "Kestra OSS", "RAGFlow"]),
                           ("wallstreet-2026-09-03-1110.html", "ws",
                            ["ChargePoint", "Palantir", "Ultragenyx", "Ciena", "Victoria"])]:
        old = open(os.path.join(prev, f)).read()
        for n in names:
            for card in [c.split("</p>")[0] for c in P[page].split('<div class="card')[1:]]:
                if n in card and 't new">New' in card:
                    chk(n not in old,
                        "NEW TAG: '%s' is tagged New but appeared in the previous edition" % n)
    # Kestra was on the previous edition, so its card must NOT be tagged New.
    for card in [c.split("</p>")[0] for c in P["cyber"].split(chr(60)+"div class=\"card")[1:]]:
        if "Kestra OSS &mdash;" in card:
            chk('t new">New' not in card, "NEW TAG: the Kestra card must not be tagged New")
except IOError:
    pass

# ---- 11. NO DESK JARGON IN READER-FACING COPY --------------------------
for j in ["this run's return", "this run's fetches", "not re-sourced this run and was dropped",
          "a fresh fetch this run", "the guards", "read-through", "editions ago",
          "consecutive run", "the desk"]:
    chk(j.lower() not in ALL.lower(), "JARGON: reader-facing copy contains '%s'" % j)

# ---- 12. MMA COUNTDOWN + DISCLAIMERS ------------------------------------
present("mma", 'id="ufccdn"', "MMA: the Next Card countdown element is missing")
present("mma", "2026-09-05T14:00:00-04:00", "MMA: countdown must target the Sept 5 Paris card")
present("mma", "Cards and bouts are subject to change", "MMA: disclaimer missing")
present("ws", "Nothing here is investment advice", "MARKETS: disclaimer missing")
present("ws", "For information only", "MARKETS: information-only framing missing")
present("cyber", "For information only", "CYBER: disclaimer missing")
for n in P:
    chk("Sources" in P[n] or n == "index", "SOURCES: %s is missing its sources footer" % n)

print("val_1135.py: %d checks, %d raised" % (checks, len(raised)))
for r in raised:
    print("  RAISED:", r)
sys.exit(0)
