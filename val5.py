# -*- coding: utf-8 -*-
import io, os, re, sys, datetime
OUT = os.path.dirname(os.path.abspath(__file__))
F = {k: io.open(os.path.join(OUT, v), encoding="utf-8").read()
     for k, v in {"ix": "index.html", "cy": "cyber-briefing.html",
                  "ws": "wallstreet-briefing.html", "mm": "mma-briefing.html"}.items()}
n = 0; fails = []
def ck(cond, msg):
    global n
    n += 1
    if not cond: fails.append(msg)

# ---- structural, all four pages
for k, s in F.items():
    ck(s.count("<body>") == 1, k + " one body")
    ck(s.count("<!DOCTYPE html>") == 1, k + " one doctype")
    ck(s.count('<nav class="tabs">') == 1, k + " one nav")
    ck(len(re.findall(r'<nav class="tabs">(.*?)</nav>', s, re.S)[0].split("<a ")) - 1 == 5, k + " five nav links")
    ck(len(re.findall(r'<a href="[^"]+" class="active">', s)) == 1, k + " exactly one active tab")
    ck("@@" not in s, k + " no unreplaced placeholder")
    ck('id="edition"' in s and 'id="datestamp"' in s and 'id="updated"' in s, k + " masthead pills")
    ck('id="freshline"' in s, k + " freshline")
    ck("America/New_York" in s, k + " stamp js")
    for g in ["⛨", "\U0001f5c4", "▲", "⊘", "★"]:
        ck(g in s, k + " nav glyph " + repr(g))
    ck("⛄" not in s and "&#9924;" not in s, k + " no snowman")
    ck("archive.html" in s, k + " archive link")

# ---- tldr strips on the three briefings, tailored labels
for k, lab in [("ws", "The Tape"), ("cy", "The Wire"), ("mm", "Tale of the Tape")]:
    m = re.search(r'<div class="tldr"><b>([^<]*)</b> <span>(.*?)</span></div>', F[k], re.S)
    ck(m is not None, k + " tldr present")
    ck(m and m.group(1) == lab, k + " tldr label " + lab)
    ck(m and F["ix"].count(m.group(2)) == 1, k + " tldr verbatim on index")
ck('class="tldr"' not in F["ix"], "index has no tldr strip")

# ---- TradingView widgets only on markets page
W = ["ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]
for w in W:
    ck(("embed-widget-" + w) in F["ws"], "ws has " + w)
    for k in ["ix", "cy", "mm"]:
        ck(("embed-widget-" + w) not in F[k], k + " lacks " + w)
ck(F["ws"].count("embed-widget-single-quote") == 3, "exactly three single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(sym in F["ws"], "ticker keeps " + sym)
ck('"symbol":"NYSE:GNRC"' in F["ws"], "chart of the day = GNRC")

# ---- markets arithmetic, computed not asserted
ck(round(7551.81 + 84.90, 2) == 7636.71, "S&P intraday reconciles")
ck(abs(84.90 / 7551.81 * 100 - 1.12) < 0.01, "S&P pct reconciles")
ck(round(51461.90 + 374.13, 2) == 51836.03, "Dow intraday reconciles")
ck(abs(374.13 / 51461.90 * 100 - 0.73) < 0.01, "Dow pct reconciles")
ck(round(52093.11 - 631.21, 2) == 51461.90, "Wed Dow close reconciles")
ck(abs(631.21 / 52093.11 * 100 - 1.21) < 0.01, "Wed Dow pct reconciles")
# refused strip must NOT appear as a published level
for bad in ["7,630.50", "51,737.00", "29,428.20"]:
    ck(F["ws"].count(bad) <= 1, "refused level " + bad + " appears at most once (in the refusal note)")
ck("At close" in F["ws"] and "not published" in F["ws"], "ws states the refusal")
ck("Super Micro is excluded" in F["ws"] or "omitted entirely" in F["ws"], "ws states SMCI omission")
ck("No Nasdaq Composite percentage is published" in F["ws"], "ws states Nasdaq omission")
ck("7,551.81" in F["ws"] and "51,461.90" in F["ws"] and "25,978.42" in F["ws"], "scorecard closes present")
ck("Nothing on this page is investment advice" in F["ws"], "ws disclaimer")
ck("Information only." in F["ws"], "ws information-only line")

# ---- cyber countdowns computed from today
TODAY = datetime.date(2026, 9, 17)
def days(y, m, d): return (datetime.date(y, m, d) - TODAY).days
ck(days(2026, 9, 17) == 0, "cisco email due today")
ck(days(2026, 9, 14) == -3, "screenconnect overdue 3")
ck(days(2026, 9, 19) == 2, "ise/acronis 2 days left")
ck(days(2026, 8, 21) == -27, "vcenter long past")
ck("0 days left &mdash; due today" in F["cy"], "cy today countdown rendered")
ck("overdue by 3 days" in F["cy"], "cy overdue countdown rendered")
ck("(2 days left)" in F["cy"], "cy 2-day countdown rendered")
ck(datetime.date(2026, 9, 19).strftime("%A") == "Saturday", "19 Sep is Saturday")
ck("a Saturday" in F["cy"], "cy weekday computed")
# patch priority and KEV agree on the same date
ck(F["cy"].count("17 September 2026") >= 2, "same deadline in patch priority and KEV")
ck('class="callout crit"' in F["cy"], "patch priority is crit")
ck("Threat level: High" in F["cy"], "threat banner")
ck(F["cy"].count('class="stat"') == 4, "four stats")
for cve in ["CVE-2026-76461", "CVE-2026-76460", "CVE-2026-59310", "CVE-2026-84869", "CVE-2026-87886", "CVE-2026-58704", "CVE-2026-75650"]:
    ck(cve in F["cy"], "cy has " + cve)
ck("9.8" in F["cy"] and "10.0" in F["cy"] and "9.9" in F["cy"], "cvss present")
ck("not stated" in F["cy"], "cy states missing CVSS explicitly")

# ---- MMA champions board parsed per division
rows = re.findall(r"<tr><td>([^<]+)</td><td[^>]*>([^<]+)</td><td>(.*?)</td></tr>", F["mm"], re.S)
board = {a.strip(): b.strip() for a, b, c in rows if a.strip() in
         ["Heavyweight", "Light Heavyweight", "Middleweight", "Welterweight", "Lightweight",
          "Featherweight", "Bantamweight", "Flyweight", "Women's Flyweight",
          "Women's Bantamweight", "Women's Strawweight"]}
ck(len(board) == 11, "eleven belts, got %d" % len(board))
expect = {"Heavyweight": "VACANT", "Light Heavyweight": "Carlos Ulberg", "Middleweight": "Sean Strickland",
          "Welterweight": "Islam Makhachev", "Lightweight": "Justin Gaethje",
          "Featherweight": "Alexander Volkanovski", "Bantamweight": "Petr Yan",
          "Flyweight": "Joshua Van", "Women's Flyweight": "VACANT",
          "Women's Bantamweight": "Kayla Harrison", "Women's Strawweight": "Mackenzie Dern"}
for d, c in expect.items():
    ck(board.get(d) == c, "champion %s should be %s, got %r" % (d, c, board.get(d)))
ck(sum(1 for v in board.values() if v == "VACANT") == 2, "exactly two vacant")
for banned in ["Alex Pereira", "Khamzat Chimaev", "Valentina Shevchenko", "Tom Aspinall",
               "Ilia Topuria", "Magomed Ankalaev", "Alexandre Pantoja", "Ciryl Gane"]:
    ck(banned not in board.values(), banned + " not in a champion cell")
ck(list(board.values()).count("Carlos Ulberg") == 1, "Ulberg exactly once")
ck(board["Light Heavyweight"] == "Carlos Ulberg", "Ulberg at LHW")
ck("regressed" in F["mm"] and "Aspinall" in F["mm"], "mm names the ESPN regression")

# ---- MMA dates: upcoming not past, last event past
for y, m, d in [(2026, 9, 19), (2026, 10, 3), (2026, 10, 24)]:
    ck(datetime.date(y, m, d) >= TODAY, "upcoming %s-%s-%s not past" % (y, m, d))
ck(datetime.date(2026, 9, 12) < TODAY, "Noche UFC is past")
ck("id=\"ufccdn\"" in F["mm"] and "2026-09-19T21:00:00-04:00" in F["mm"], "mma countdown to UFC 331")
ck("subject to change" in F["mm"], "mm disclaimer")
ck("56%" in F["mm"] and "44%" in F["mm"] and "&minus;130" in F["mm"], "mm odds both presentations")
ck("$100,000" in F["mm"], "mm bonus amounts")
ck("0:36" in F["mm"] and "0:33" not in F["mm"], "King III time is 0:36 not 0:33")
ck("has not pulled out" in F["mm"] or "has not withdrawn" in F["mm"], "mm carries the Van correction")

# ---- New tags: counted and justified
for k in ["ws", "cy", "mm", "ix"]:
    c = F[k].count('class="t new"')
    print("  new-tag count %s = %d" % (k, c))
ck(F["ws"].count('class="t new"') == 1, "ws exactly 1 New tag (Coterra, 0 prior hits)")
ck(F["cy"].count('class="t new"') == 1, "cy exactly 1 New tag (Argentine insurer, 0 prior hits)")
ck(F["mm"].count('class="t new"') == 0, "mm 0 New tags")
ck(F["ix"].count('class="t new"') == 0, "index 0 New tags")

# ---- sources footers
for k in ["ws", "cy", "mm"]:
    ck('class="panel srcs"' in F[k], k + " sources footer")
    ck(F[k].count("<a href=\"http") >= 10, k + " at least 10 source links")
    ck('class="disc"' in F[k], k + " disclaimer")

print("checks: %d, failures: %d" % (n, len(fails)))
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
