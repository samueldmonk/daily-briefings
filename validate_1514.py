#!/usr/bin/env python3
"""Validation pass, Sunday 2026-08-30 Afternoon Edition (~3:14 PM ET publish)."""
import re, sys, datetime, zoneinfo

D = "/sessions/serene-vigilant-hypatia/mnt/outputs/"
FILES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {f: open(D + f, encoding="utf-8").read() for f in FILES}
IDX, CY, WS, MM = S["index.html"], S["cyber-briefing.html"], S["wallstreet-briefing.html"], S["mma-briefing.html"]
BRIEFS = {"cyber-briefing.html": CY, "wallstreet-briefing.html": WS, "mma-briefing.html": MM}

checks = 0
fails = []

def ok(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def has(s, t, msg):
    ok(t in s, msg)

def hasnt(s, t, msg):
    ok(t not in s, msg)

def near(s, needle, *words, window=1400, msg=None):
    """every occurrence of needle must sit within `window` chars of one of `words`"""
    global checks
    checks += 1
    for m in re.finditer(re.escape(needle), s):
        seg = s[max(0, m.start() - window): m.end() + window]
        if not any(w in seg for w in words):
            fails.append(msg or ("frame failed for " + needle))
            return

# ---- 1. STAMP: derived from the page, identical across all four
m = re.search(r'id="updated"[^>]*>([^<]+)</span>', IDX)
ok(m is not None, "index has no updated stamp")
STAMP = m.group(1).replace(" ET", "").strip()
ok(re.match(r'^\d{1,2}:\d{2} (AM|PM)$', STAMP), "stamp malformed: " + STAMP)
for f, s in S.items():
    has(s, 'id="updated">' + STAMP + ' ET</span>', f + ": masthead stamp not " + STAMP)
    has(s, 'Data as of ' + STAMP + ' ET', f + ": freshline not " + STAMP)
    has(s, 'id="datestamp">Sunday, August 30, 2026</span>', f + ": datestamp wrong")
    has(s, 'id="edition">Afternoon Edition</span>', f + ": edition wrong")

# prose observation stamp may not run ahead of the publish clock
def tomin(t):
    hh, rest = t.split(":"); mm, ap = rest.split(" ")
    h = int(hh) % 12 + (12 if ap == "PM" else 0)
    return h * 60 + int(mm)
ok(tomin("3:10 PM") <= tomin(STAMP), "prose observation stamp 3:10 PM runs ahead of publish clock " + STAMP)

for stale in ["2:47 PM ET", "1:09 PM ET", "2:14 PM ET"]:
    for f, s in S.items():
        hasnt(s, 'id="updated">' + stale, f + ": stale masthead " + stale)
    hasnt(IDX, "Data as of " + stale.replace(" ET", "") + " ET", "index stale freshline " + stale)

# ---- 2. NAV: five tabs, exactly one active, on every page
for f, s in S.items():
    for href, label in [("index.html", "Front Page"), ("cyber-briefing.html", "The Cyber Wire"),
                        ("wallstreet-briefing.html", "The Closing Bell"),
                        ("mma-briefing.html", "The Octagon"), ("archive.html", "Archive")]:
        has(s, 'href="' + href + '"', f + ": nav missing " + href)
        has(s, label, f + ": nav label missing " + label)
    nav = re.search(r'<nav class="tabs">.*?</nav>', s, re.S)
    ok(nav is not None, f + ": no nav")
    ok(len(re.findall(r'class="on"', nav.group(0))) == 1, f + ": not exactly one active tab")

# ---- 3. MASTHEAD ids + self-stamp script
for f, s in S.items():
    for i in ["edition", "datestamp", "updated", "freshline"]:
        has(s, 'id="' + i + '"', f + ": missing id " + i)
    has(s, "America/New_York", f + ": self-stamp script missing")
    has(s, "Afternoon Edition", f + ": edition bucket missing")

# ---- 4. TLDR strips present with correct labels, and index mirrors them exactly
for f, label in [("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"),
                 ("mma-briefing.html", "Tale of the Tape")]:
    m = re.search(r'<div class="tldr"><b>' + re.escape(label) + r'</b>\s*<span>(.*?)</span></div>',
                  BRIEFS[f], re.S)
    ok(m is not None, f + ": tldr missing for " + label)
for cls, f in [("c-cy", "cyber-briefing.html"), ("c-ws", "wallstreet-briefing.html"), ("c-mm", "mma-briefing.html")]:
    label = {"cyber-briefing.html": "The Wire", "wallstreet-briefing.html": "The Tape",
             "mma-briefing.html": "Tale of the Tape"}[f]
    t = re.search(r'<div class="tldr"><b>' + re.escape(label) + r'</b>\s*<span>(.*?)</span></div>',
                  BRIEFS[f], re.S).group(1).strip()
    c = re.search(r'<div class="bigcard ' + cls + r'">.*?<p>(.*?)</p>', IDX, re.S)
    ok(c is not None, "index card missing " + cls)
    ok(c.group(1).strip() == t, "index card " + cls + " does not mirror its tldr")
    has(IDX, 'class="go" href="' + f + '"', "index missing Read the briefing link for " + f)
has(IDX, "Read the briefing", "index missing read-the-briefing text")

# ---- 5. LIVE WIDGETS: all six blocks on Wall Street only
for w in ["embed-widget-ticker-tape", "embed-widget-single-quote", "embed-widget-timeline",
          "embed-widget-stock-heatmap", "embed-widget-mini-symbol-overview", "embed-widget-events"]:
    has(WS, w, "WS missing widget " + w)
    for f in ["index.html", "cyber-briefing.html", "mma-briefing.html"]:
        hasnt(S[f], w, f + ": must carry no live widget " + w)
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    has(WS, sym, "WS ticker missing required symbol " + sym)
has(WS, "NASDAQ:PYPL", "WS Chart of the Day symbol missing")
ok(len(re.findall(r'embed-widget-single-quote', WS)) == 3, "WS needs exactly three single-quote widgets")
has(WS, "Quotes stream live", "WS missing the note line under block B")

# ---- 6. MARKETS: the six close figures, reconciled
for v in ["7,711.76", "26,402.42", "53,559.99", "&minus;0.25%", "&minus;0.52%", "&minus;9.45"]:
    has(WS, v, "WS missing close figure " + v)
ok(abs(9.45 / 53559.99 * 100 - 0.02) < 0.005, "Dow points/percent do not reconcile")
ok(abs(19.23 / 7711.76 * 100 - 0.25) < 0.005, "S&P points/percent do not reconcile")
ok(abs(138.93 / 26541.35 * 100 - 0.52) < 0.005, "Nasdaq points/percent do not reconcile")
# the new arithmetic corroboration
ok(abs((26541.35 - 138.93) - 26402.42) < 0.005, "Thursday-minus-Friday does not land on the Friday close")
has(WS, "26,541.35", "WS missing the Thursday close used for the arithmetic check")
has(WS, "411.16", "WS missing the Thursday point move")
near(WS, "26,541.35", "Thursday", "August 27", "Thu, Aug 27", msg="Thursday close not framed as Thursday")
has(WS, "twenty-second verification", "WS missing the twenty-second verification counter")
hasnt(WS, "twenty-first verification", "WS still carries the stale twenty-first counter")
hasnt(WS, "as of ~", "WS must not carry an intraday as-of while the tape is shut")
hasnt(WS, "After-Hours Movers", "WS must carry no after-hours block on a weekend")
hasnt(WS, "7,673.04", "WS carries a retired S&P level")

# rates family
for v in ["4.73%", "4.34%", "5.20%"]:
    has(WS, v, "WS missing rate " + v)
near(WS, "4.67%", "intraday", "retired", "refused", window=900, msg="4.67% appears outside a rejection frame")
# the four undated figures must be printed only inside the not-published frame
for fig in ["ten of the eleven sectors", "gained 3.2%", "4.35%", "64%"]:
    near(WS, fig, "none of them is published", "not dated to a session", "recorded here and none is carried",
         window=2200, msg="undated figure " + fig + " outside its rejection frame")

# September pricing: ninth read, both venues numbered, no adoption
for v in ["57%", "43%", "3.50&ndash;3.75%", "Polymarket puts a hold at 52%", "Kalshi", "48%",
          "September 16", "ninth read"]:
    has(WS, v, "WS missing September-pricing element " + v)
has(WS, "Still not adopted", "WS must state the September pricing is not adopted")
ok("ninth read" in WS and "Still not adopted" in WS and "ninth consecutive run" in WS,
   "the ninth September read is not paired with an explicit declination on the page")

# payrolls date defended; Sept 5 only ever as a rejection
has(WS, "Friday, September 4", "WS missing the payrolls date")
has(WS, "8:30 AM", "WS missing the payrolls time")
near(WS, "September 5", "Saturday", "rejected", "thrown out", "not possible", "belong to a different year",
     window=900, msg="September 5 appears outside a rejection frame")
hasnt(WS, "payrolls on Friday, September 5", "WS asserts payrolls on the wrong date")
# Labor Day rejection
has(WS, "Monday, September 7", "WS missing the correct Labor Day date")
near(WS, "Labor Day", "September 7", "Rejected", "not adopted", window=1600,
     msg="Labor Day mention outside its rejection frame")
# week-ahead earnings family
for v in ["Palo Alto Networks and Dell Technologies after Tuesday", "ISM Manufacturing PMI",
          "JOLTS", "George Kurtz", "ADP employment report", "ISM Services on Thursday, September 3",
          "Tuesday, September 1", "Wednesday, September 2"]:
    has(WS, v, "WS missing week-ahead element " + v)
ok("Palo Alto Networks and Dell Technologies after Tuesday" in WS
   and "The declination is closed, not deleted" in WS
   and "no reporting date for Palo Alto Networks was stated by anything fetched, so none is printed"
       in WS,  # kept, but only inside the superseded frame
   "the Palo Alto declination is not shown as closed by the date that arrived")
ok(WS.count("No reporting date for Palo Alto Networks was stated") == 0,
   "the Palo Alto declination is still asserted in the present tense")

# ---- 7. CYBER: Patch Priority agrees with the KEV board
has(CY, "expires TODAY, Sunday, August 30", "cyber Patch Priority does not lead with today's deadline")
has(CY, "EXPIRED YESTERDAY", "cyber Patch Priority does not demote the passed Citrix deadline")
hasnt(CY, "Gateway &mdash; federal deadline expires TODAY",
      "cyber Patch Priority still claims the Citrix deadline is today")
has(CY, "OVERDUE", "cyber KEV board missing the overdue row")
has(CY, "0 days left", "cyber KEV board missing the due-today countdown")
has(CY, "10 days left", "cyber KEV board missing the 10-day countdown")
has(CY, "11 days left", "cyber KEV board missing the 11-day countdown")
hasnt(CY, "1 day left", "cyber KEV board carries a stale 1-day countdown")
hasnt(CY, "12 days left", "cyber KEV board carries a stale 12-day countdown")
# the same two CVEs must be the today-item in BOTH places
for c in ["CVE-2023-49105", "CVE-2026-53362"]:
    has(CY, c, "cyber missing today-due CVE " + c)
    ok(CY.count(c) >= 2, "cyber: " + c + " should appear in both Patch Priority and the KEV board")
# deadline dates
for d in ["August 30", "Sept 10", "Aug 29"]:
    has(CY, d, "cyber missing KEV date " + d)

# KEV thirteenth check family
has(CY, "thirteenth check", "cyber missing the thirteenth KEV check")
hasnt(CY, "A twelfth check, at " + STAMP, "cyber mislabels the current check as the twelfth")
for c in ["CVE-2026-66384", "CVE-2026-33824", "CVE-2026-55040", "CVE-2026-59310", "CVE-2026-65400",
          "CVE-2026-20349", "CVE-2026-72898", "CVE-2026-68820"]:
    has(CY, c, "cyber missing KEV-alert CVE " + c)
# 68820 confirmed listed but still gets NO countdown row
near(CY, "CVE-2026-68820", "no countdown", "row remains withheld", "not a deadline it displays",
     "only flaw in that release", "use-after-free", "gets no row", "no row and no countdown", window=2000,
     msg="68820 appears outside its no-countdown / characterisation frame")
has(CY, "Its <b>due date still is not</b>", "cyber must state 68820's due date is still unsourced")
has(CY, "heap-based buffer overflow", "cyber missing the rival 68820 characterisation")
# gap CVEs must never sit in a countdown region
for gap in ["CVE-2026-62815"]:
    for m in re.finditer(re.escape(gap), CY):
        seg = CY[max(0, m.start() - 700): m.end() + 700]
        ok("days left" not in seg, gap + " sits inside a countdown region")

# ServiceNow family incl. the 6875/6876 trap
for c in ["CVE-2026-18885", "CVE-2026-18886", "CVE-2026-74820", "CVE-2026-6876", "CVE-2026-6875"]:
    has(CY, c, "cyber missing ServiceNow CVE " + c)
has(CY, "Searchlight Cyber", "cyber missing the 6875 reporter")
has(CY, "Defused", "cyber missing the 6875 exploitation observer")
has(CY, "not aware of malicious exploitation", "cyber missing the vendor's non-exploitation statement")
CY_BODY = re.sub(r"<footer.*?</footer>", "", CY, flags=re.S)
near(CY_BODY, "CVE-2026-6875", "6876", "exploited and old", "one digit", window=1600,
     msg="6875 appears in the body without its disambiguation from 6876")

# Refused panel: Nevada fifth + the Hugging Face date
has(CY, "Nevada, a fifth time", "cyber Refused panel not advanced to the fifth Nevada refusal")
hasnt(CY, "Nevada, a fourth time", "cyber Refused panel still says fourth")
has(CY, "Five refusals are now logged", "cyber missing the refusal count")
near(CY, "60-plus agencies", "refus", "2025", "permanently excluded", "not adopted", window=2000,
     msg="the Nevada 60-plus-agencies claim sits outside a refusal frame")
near(CY, "Nevada", "refus", "2025", "permanently excluded", "not adopted", "After-Action", window=2200,
     msg="a Nevada mention sits outside a refusal/resolution frame")
has(CY, "publication date wearing an incident date", "cyber missing the Hugging Face date refusal")
near(CY, "&ldquo;on August 29, 2026.&rdquo;", "publication date", "not adopted", "refus", window=1400,
     msg="the Aug 29 Hugging Face date appears outside its refusal frame")
ok(re.search(r"Countdowns above are measured from\s*<b>Sunday, August 30, 2026</b>", CY) is not None,
   "the KEV countdown baseline is not stamped to today")
ok(re.search(r"Countdowns above are measured from\s*<b>Saturday, August 29, 2026</b>\.", CY) is None,
   "the KEV countdown baseline still asserts Saturday")
has(CY, "the July 2026 Incident", "cyber missing the Hugging Face primary dating")
has(CY, "July 19", "cyber missing the exploitation date")
# agent-swarm figures
for v in ["More than 1,200 agents", "roughly 700 agents", "ExploitGym"]:
    has(CY, v, "cyber missing agent-swarm figure " + v)
has(CY, "nothing fetched this run states that 66384 was the channel",
    "cyber must decline to join 66384 to the covert channel")

# attacker-attribution proximity: big figures must sit near an attribution
for fig in ["5.79 TB", "$55,236,150"]:
    if fig in CY:
        near(CY, fig, "claim", "reported", "alleged", "listing", "Rhysida", "according", window=1600,
             msg=fig + " lacks a nearby attribution")
# CVE well-formedness + liveness
bad = [c for c in re.findall(r'CVE-\d{4}-\d+', CY) if not re.match(r'^CVE-(19|20)\d{2}-\d{4,7}$', c)]
ok(not bad, "malformed CVE ids: " + str(bad[:5]))
ok(len(set(re.findall(r'CVE-\d{4}-\d+', CY))) >= 20, "cyber carries fewer than 20 distinct CVEs")
# Patch Tuesday spread
for v in ["398", "421", "751"]:
    has(CY, v, "cyber missing Patch Tuesday count " + v)
has(CY, "one count among three", "cyber must present 421 as one count among three")

# ---- 8. MMA
# champions: names asserted, forbidden cells absent
for n in ["Aspinall", "Ulberg", "Strickland", "Makhachev", "Gaethje", "Volkanovski",
          "Petr Yan", "Joshua Van", "Shevchenko", "Harrison", "Dern"]:
    has(MM, n, "mma champions board missing " + n)
for bad in ["Pereira</b></td>", "Chimaev</b></td>", "Topuria</b></td>"]:
    hasnt(MM, bad, "mma champions board names a superseded champion: " + bad)
near(MM, "vacant", "won", "win the vacant", "for the vacant title", "reject", "NOT vacant",
     "took the belt", window=700,
     msg="a 'vacant' string sits outside a won-the-vacant-title or rejection frame")
has(MM, "sixth</b> consecutive broad, clean return", "mma missing the sixth clean champions run")
has(MM, "sixty-third consecutive edition", "mma board counter not advanced")
hasnt(MM, "a fifth consecutive broad, clean return &mdash; and the first", "mma still leads with the fifth run")
# Dariush descriptor
for m in re.finditer("Dariush", MM):
    seg = MM[max(0, m.start() - 500): m.end() + 500]
    ok("champion" not in seg.lower() or "never" in seg.lower() or "contender" in seg.lower(),
       "Dariush described with a title descriptor")

# UFC 331 family
for v in ["Bet Online", "&minus;115", "&minus;105", "+100", "&minus;120", "&minus;400",
          "13 fights", "September 19", "Crypto.com Arena"]:
    has(MM, v, "mma missing UFC 331 element " + v)
has(MM, "Neither is adopted", "mma must decline to adopt either UFC 331 book")
near(MM, "ended in injury", "not adopted", "does not swap", "recorded as the source", window=1100,
     msg="the 'ended in injury' paraphrase is not framed as unadopted")
ok(MM.count("technical knockout 26 seconds into round one") >= 2,
   "the sourced UFC 323 finish is not stated everywhere the paraphrase appears")
has(MM, "technical knockout 26 seconds into round one", "mma missing the sourced UFC 323 finish")
hasnt(MM, "first defence for Van", "mma miscalls UFC 331 a first defence")

# Paris family
for v in ["BetWay", "&minus;400 / Hooker +300", "&minus;500", "+375", "13 bouts", "Accor Arena",
          "Hooker vs. Parnasse", "23-2", "24-14", "KSW"]:
    has(MM, v, "mma missing UFC Paris element " + v)
has(MM, "fifth consecutive annual visit", "mma missing the Paris visit count")
has(MM, "Imavov vs. Borralho", "mma missing the previous Paris event")
near(MM, "15 fights", "outlier", "13", "re-check", window=900,
     msg="the 15-fight outlier is not framed as rejected")
has(MM, "13 stands", "mma must state the 13-bout count stands")
has(MM, "Still no adoption", "mma must decline to adopt a Paris line")
# the refused name must never appear outside a refusal
near(MM, "Pimenta", "refus", "returned nobody", "NOT published", "no phantom", window=1200,
     msg="a refused fighter name appears outside its refusal frame")

# Shanghai / bonuses
for v in ["Song Yadong", "Umar Nurmagomedov", "1:48", "$400,000", "Bilal Hasan",
          "Rei Tsuruya", "Denise Gomes"]:
    has(MM, v, "mma missing Shanghai element " + v)
# prospect family
for v in ["Mridul Saikia", "45 seconds", "Anthony Wint", "Matt Adams", "34 seconds",
          "Thomas Pagliarulo", "Joe Kropschot", "August 11, 2026", "Nilson Rojas"]:
    has(MM, v, "mma missing Contender Series element " + v)
has(MM, "belongs to the Contender Series fight, not the UFC debut",
    "mma must keep the two Hasan finishes apart")
# countdown bar
has(MM, 'id="ufccdn"', "mma missing the next-card countdown element")

# ---- 9. FOOTERS: sources, no duplicate hrefs, absolute links, disclaimer
for f, s in BRIEFS.items():
    foot = re.search(r'<footer.*?</footer>', s, re.S)
    ok(foot is not None, f + ": no footer")
    hrefs = re.findall(r'href="([^"]+)"', foot.group(0))
    ok(len(hrefs) >= 6, f + ": footer has fewer than 6 source links")
    ok(all(h.startswith("http") for h in hrefs), f + ": footer has a non-absolute link")
    ok(len(hrefs) == len(set(hrefs)), f + ": footer has duplicate source links")
has(CY, "not a substitute for your own vulnerability management", "cyber disclaimer missing")
has(WS, "not investment advice", "wallstreet disclaimer missing")
has(MM, "subject to change", "mma disclaimer missing")

# ---- 10. tag classes must be defined wherever used
for f, s in S.items():
    used = set(re.findall(r'class="tag ([a-z]+)"', s))
    for u in used:
        ok(".tag." + u in s or ".tag ." + u in s,
           f + ": tag class '" + u + "' used but not defined")

print("CHECKS:", checks, "| FAILURES:", len(fails))
for x in fails:
    print("  FAIL:", x)
sys.exit(1 if fails else 0)
