# -*- coding: utf-8 -*-
import io, os, re, sys, datetime
D = os.path.dirname(os.path.abspath(__file__))
PAGES = {n: io.open(os.path.join(D, n), encoding="utf-8").read()
         for n in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html")}
n = 0; fail = []
def ck(cond, msg):
    global n
    n += 1
    if not cond: fail.append(msg)

TODAY = datetime.date(2026, 9, 17)

# ---------- structural, all four pages ----------
for name, s in PAGES.items():
    ck(s.count("<body>") == 1, name + ": one <body>")
    ck(s.count("</body>") == 1, name + ": one </body>")
    ck(s.startswith("<!DOCTYPE html>"), name + ": doctype")
    ck(s.rstrip().endswith("</html>"), name + ": clean close")
    ck(s.count('<nav class="tabs">') == 1, name + ": one nav")
    ck(s.count('nav.tabs') >= 1, name + ": nav css")
    ck(len(re.findall(r'<nav class="tabs">.*?</nav>', s, re.S)[0].split("<a ")) - 1 == 5, name + ": five nav links")
    ck(s.count('<a href="index.html"') == 1, name + ": index tab")
    ck(s.count('<a href="cyber-briefing.html"') >= 1, name + ": cyber tab")
    ck(s.count('<a href="wallstreet-briefing.html"') >= 1, name + ": ws tab")
    ck(s.count('<a href="mma-briefing.html"') >= 1, name + ": mma tab")
    ck(s.count('href="archive.html"') >= 1, name + ": archive tab")
    ck(len(re.findall(r'<a href="[^"]+" class="active">', s)) == 1, name + ": exactly one active tab")
    ck('id="edition"' in s, name + ": edition pill")
    ck('id="datestamp"' in s, name + ": datestamp pill")
    ck('id="updated"' in s, name + ": updated pill")
    ck('pill live' in s, name + ": live pill")
    ck('id="freshline"' in s, name + ": freshline")
    ck("briefings refresh every 30 minutes" in s, name + ": freshline text in stamp")
    ck("America/New_York" in s, name + ": ET stamp")
    ck("Morning Edition" in s and "Midday Edition" in s and "Afternoon Edition" in s, name + ": edition buckets")
    # nav glyphs (past bug: snowman)
    ck("\u26e8" in s or "&#9960;" in s, name + ": cyber glyph U+26D8")
    ck("\u26c4" not in s and "&#9924;" not in s, name + ": no snowman glyph")
    ck("\U0001f5c4" in s or "&#128452;" in s, name + ": archive glyph")
    ck("\U0001f5c3" not in s and "&#128451;" not in s, name + ": no file-box glyph")
    # no leftover placeholders
    ck("@@" not in s, name + ": no unreplaced placeholders")
    ck("TODO" not in s and "TKTK" not in s, name + ": no TODO")

# ---------- TLDR strips ----------
for name in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    ck('<div class="tldr">' in PAGES[name], name + ": tldr present")
    ck(PAGES[name].count('<div class="tldr">') == 1, name + ": exactly one tldr")
ck("<b>The Wire</b>" in PAGES["cyber-briefing.html"], "cyber tldr label")
ck("<b>The Tape</b>" in PAGES["wallstreet-briefing.html"], "ws tldr label")
ck("<b>Tale of the Tape</b>" in PAGES["mma-briefing.html"], "mma tldr label")
ck('<div class="tldr">' not in PAGES["index.html"], "index has no tldr strip")

# index cards string-match the briefing TLDRs verbatim
def tldr(fn):
    m = re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', PAGES[fn], re.S)
    return m.group(1)
for fn in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    ck(tldr(fn) in PAGES["index.html"], "index card matches %s tldr verbatim" % fn)

# ---------- TradingView widgets: markets page only ----------
ws = PAGES["wallstreet-briefing.html"]
for w in ("embed-widget-ticker-tape.js", "embed-widget-single-quote.js", "embed-widget-timeline.js",
          "embed-widget-stock-heatmap.js", "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"):
    ck(w in ws, "ws has " + w)
    for other in ("index.html", "cyber-briefing.html", "mma-briefing.html"):
        ck(w not in PAGES[other], other + " free of " + w)
ck(ws.count("embed-widget-single-quote.js") == 3, "exactly three single-quote widgets")
ck('"FOREXCOM:SPXUSD"' in ws and '"FOREXCOM:NSXUSD"' in ws and '"FOREXCOM:DJI"' in ws, "three index quote symbols")
ck('class="livebar"' in ws, "livebar wrapper")
ck("LIVE QUOTES" in ws, "livebar label")
ck('"TVC:USOIL"' in ws, "ticker keeps WTI")
ck('"TVC:US10Y"' in ws, "ticker keeps 10Y")
ck('"NYSE:GNRC"' in ws, "chart of the day = GNRC")
ck(ws.count('"NYSE:GNRC"') == 2, "GNRC in tape and chart")
ck("Quotes stream live" in ws, "note line present")

# ---------- KEV countdowns computed, not asserted ----------
def days(y, m, d):
    k = (datetime.date(y, m, d) - TODAY).days
    if k > 0:  return "%d day%s left" % (k, "" if k == 1 else "s")
    if k == 0: return "0 days left"
    return "%d day%s overdue" % (-k, "" if -k == 1 else "s")
cy = PAGES["cyber-briefing.html"]
D1, D2, D3 = days(2026, 9, 17), days(2026, 9, 19), days(2026, 9, 14)
ck(D1 == "0 days left", "76461 due today computes to 0")
ck(D2 == "2 days left", "76460 due 19 Sep computes to 2")
ck(D3 == "3 days overdue", "84869 due 14 Sep computes to 3 overdue")
ck(cy.count(D1) >= 2, "0-days countdown appears in banner-area and ledger")
ck(D2 in cy, "2-days countdown present")
ck(D3 in cy, "overdue countdown present")
ck("BOD 22-01" not in cy, "no unsourced BOD 22-01 string")
ck("1 day left" not in cy, "stale '1 day left' blocked")
ck("3 days left" not in cy, "stale '3 days left' blocked")
# the 19 September date must read identically everywhere it appears
ck(cy.count("19 September") >= 2, "19 September consistent in Patch Priority + KEV ledger")
ck("17 September 2026" in cy, "today's deadline stated with year")

# ---------- cyber facts ----------
ck("23.62 million" in cy or "23.62M" in cy, "Gyazo record count")
ck("490 million" in cy and "490M" in cy, "metadata count both places")
ck("CVE-2026-76461" in cy and "CVE-2026-76460" in cy, "both Cisco CVEs")
ck("9.8" in cy, "76461 CVSS 9.8 present")
ck("10.0" in cy, "76460 CVSS 10.0 present")
ck("15.5.5-014" in cy and "16.0.4-302" in cy and "16.5.0-780" in cy, "email gateway fixed versions")
ck("3.1 P12" in cy and "3.2 P11" in cy and "3.3 P12" in cy and "3.4 P7" in cy and "3.5 P4" in cy, "ISE fixed versions")
ck("3.4 Patch 2" not in cy and "3.3 Patch 7" not in cy, "superseded hotfix list blocked")
ck("not stated in sources fetched this run" in cy, "empty CVSS cells declared")
ck(cy.count("not stated in sources fetched this run") >= 2, "two blank CVSS cells")
ck("CVE-2026-59310" in cy and "361" in cy and "47 countries" in cy, "vCenter figures")
ck("GRIMWEDGE" in cy and "UTA0560" in cy and "Volexity" in cy, "GRIMWEDGE attribution")
ck("CVE-2026-85046" in cy and "CVE-2026-87491" in cy and "CVE-2026-85880" in cy, "chain CVEs")
ck("Medusa" in cy and "67" in cy, "Medusa spotlight")
ck("146" in cy and "61 new ransomware groups" in cy, "ransomware baseline")
ck("Threat level: High" in cy, "threat banner")
ck(cy.count('class="stat"') == 4, "four stat tiles")
ck("Patch Priority" in cy, "patch priority section")
ck('class="callout crit"' in cy, "patch priority is crit (deadline today)")

# ---------- markets facts + arithmetic ----------
ck("51,783.71" in ws and "321.81" in ws and "51,461.90" in ws, "Dow triple")
ck(round(51783.71 - 321.81, 2) == 51461.90, "Dow reconciliation computes")
ck(abs(321.81 / 51461.90 * 100 - 0.63) < 0.01, "Dow pct computes to 0.63")
ck("26,400.63" in ws and "422.20" in ws, "Nasdaq pair")
ck(abs(422.20 / (26400.63 - 422.20) * 100 - 1.63) < 0.01, "Nasdaq pct computes to 1.63")
ck("7,596" in ws and "0.59%" in ws, "TE S&P snapshot")
ck("0.9%" in ws, "AP/Yahoo S&P snapshot")
ck("session in progress" in ws, "Thursday scorecard row open")
ck("3.75%" in ws and "4.00%" in ws, "fed funds range")
ck("12" in ws and "25 basis points" in ws, "vote and size")
ck("4.72%" in ws, "2-year")
ck("4.943%" in ws, "10-year morning read")
ck("$103.38" in ws and "2.3%" in ws, "Brent")
ck("$100.70" in ws, "WTI morning read labelled")
ck("196,000" in ws and "10,000" in ws, "jobless claims")
ck("$8 billion" in ws and "$2.4 billion" in ws, "Generac deal scale")
ck("not" in ws and "booked revenue" in ws, "8bn qualifier present")
ck("$2.4 billion" in ws and "$2.9" in ws, "Fluence guidance cut")
ck("46.11%" in ws and "6.14%" in ws, "energy YTD / 1-month")
ck("Bitcoin" in ws, "Bitcoin named once in omission sentence")
ck(ws.count("Bitcoin") == 1, "Bitcoin exactly once")
ck("not investment advice" in ws, "ws disclaimer")
ck("7,601" not in ws, "old 7601 trap absent")
ck("8.81%" not in ws, "refused incoherent Dow figure absent")
i = ws.find("+0.93%")
ck(i != -1 and ws.count("+0.93%") == 1, "refused S&P parenthetical named exactly once")
ck(i != -1 and "refused" in ws[i:i+260], "the +0.93% mention is inside its refusal sentence, not a published figure")
ck("&ldquo;+0.93%&rdquo;" in ws, "the refused figure is quoted, not asserted")

# ---------- MMA: champions board parsed per division ----------
mm = PAGES["mma-briefing.html"]
rows = re.findall(r'<tr><td>([^<]+)</td><td[^>]*>(?:<b>)?([^<]+?)(?:</b>)?</td><td>(.*?)</td></tr>', mm, re.S)
champ = {}
for div, who, note in rows:
    if div.strip() in ("Heavyweight","Light Heavyweight","Middleweight","Welterweight","Lightweight",
                       "Featherweight","Bantamweight","Flyweight","Women&#39;s Flyweight",
                       "Women&#39;s Bantamweight","Women&#39;s Strawweight"):
        champ[div.strip()] = who.strip()
expect = {
 "Heavyweight":"VACANT", "Light Heavyweight":"Carlos Ulberg", "Middleweight":"Sean Strickland",
 "Welterweight":"Islam Makhachev", "Lightweight":"Justin Gaethje", "Featherweight":"Alexander Volkanovski",
 "Bantamweight":"Petr Yan", "Flyweight":"Joshua Van", "Women&#39;s Flyweight":"VACANT",
 "Women&#39;s Bantamweight":"Kayla Harrison", "Women&#39;s Strawweight":"Mackenzie Dern"}
ck(len(champ) == 11, "eleven belts parsed, got %d" % len(champ))
for k, v in expect.items():
    ck(champ.get(k) == v, "champion %s == %s (got %r)" % (k, v, champ.get(k)))
ck(sum(1 for v in champ.values() if v == "VACANT") == 2, "exactly two VACANT")
# blocked names must never occupy a champion cell
for bad in ("Pereira", "Chimaev", "Shevchenko", "Aspinall", "Topuria", "Ankalaev", "Pantoja", "Gane", "Ulberg"):
    cells = [v for k, v in champ.items() if bad in v]
    if bad == "Ulberg":
        ck(cells == ["Carlos Ulberg"], "Ulberg only at light heavyweight")
    else:
        ck(cells == [], bad + " not in any champion cell")
ck("Gane" in mm, "Gane appears in the heavyweight note")
ck("interim" in mm, "interim HW noted")

# ---------- MMA: results table ----------
res = re.findall(r'<tr><td class="win">([^<]+)</td><td>def\. ([^<]+)</td><td>(.*?)</td></tr>', mm, re.S)
ck(len(res) == 7, "seven result rows, got %d" % len(res))
names = [r[0] for r in res]
ck("Sean King III" in names, "King III tabled now that his method is sourced")
ck("Tommy McMillen" in names, "McMillen full name restored")
ck(any("Marwan Rahiki" in r[1] for r in res), "Rahiki full name restored")
ck("33 seconds" in mm, "King III method")
ck("Finish, round 1" not in mm, "vague method string blocked")
for bad in ("Brandon Moreno", "Chris McMillen", "Rafael Rahiki", "Rob Martinez", "Cody Salkilld"):
    ck(bad not in mm, "invented name blocked: " + bad)
ck("$100,000" in mm and "$25,000" in mm, "bonus amounts")
ck("Fight of the Night" in mm and "Performance of the Night" in mm, "bonus categories")

# ---------- MMA: cards, countdown, odds ----------
ck('id="ufccdn"' in mm, "countdown target")
ck("2026-09-19T21:00:00-04:00" in mm, "countdown datetime")
ck("Fight week" in mm, "countdown elapsed string")
ck("UFC 331" in mm and "UFC 332" in mm and "UFC 333" in mm, "three cards")
ck("Crypto.com Arena" in mm and "Delta Center" in mm, "venues")
ck("&minus;130" in mm and "+110" in mm, "main event odds")
ck("&minus;290" in mm and "+235" in mm, "co-main odds")
ck("Covers" in mm, "book named")
ck(mm.count("no source fetched this run states a line") == 2, "two cards declare no odds")
ck("subject to change" in mm, "mma disclaimer")
ck("3 October" in mm and "24 October" in mm and "19 September" in mm, "card dates")
# chronology: nothing 'upcoming' that already happened
ck("12 September" in mm and "Last Event" in mm, "Noche filed as last event")

# ---------- sources footers ----------
for name in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    s = PAGES[name]
    ck('class="panel srcs"' in s, name + ": sources panel")
    ck(s.count("https://") >= 15, name + ": >=15 source URLs")
    ck('class="disc"' in s, name + ": disclaimer")

print("checks: %d, failures: %d" % (n, len(fail)))
for f in fail: print("  FAIL:", f)

# ================= POST-REPAIR ASSERTIONS (read-through fixes) =================
P = {n: io.open(os.path.join(D, n), encoding="utf-8").read()
     for n in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html")}
n2 = 0; f2 = []
def ck2(cond, msg):
    global n2
    n2 += 1
    if not cond: f2.append(msg)

# R1 -- 19 September 2026 is a Saturday
ck2(datetime.date(2026, 9, 19).strftime("%A") == "Saturday", "19 Sep 2026 really is a Saturday")
ck2(datetime.date(2026, 9, 17).strftime("%A") == "Thursday", "17 Sep 2026 really is a Thursday")
for nm in ("index.html", "cyber-briefing.html"):
    ck2("expire today and on Saturday." in P[nm], nm + ": tldr says Saturday")
    ck2("today and Friday" not in P[nm], nm + ": no 'today and Friday'")
ck2("today and on Saturday the 19th" in P["cyber-briefing.html"], "banner says Saturday the 19th")
ck2("Friday" not in P["cyber-briefing.html"], "cyber page free of the word Friday")

# R2 -- New tags reflect a real 0-hit comparison against the 741 archived snapshots
cy2 = P["cyber-briefing.html"]
ck2(cy2.count('class="t new">New<') == 2, "cyber New count == 2, got %d" % cy2.count('class="t new">New<'))
i_tel = cy2.find("Telenor")
ck2(i_tel != -1 and 'class="t new">New<' in cy2[max(0, i_tel - 700):i_tel], "Telenor card carries the New tag")
i_val = cy2.find("CEVA")
ck2(i_val != -1 and 'class="t new">New<' in cy2[max(0, i_val - 700):i_val], "Valve/CEVA card carries the New tag")
i_gw = cy2.find("GRIMWEDGE")
ck2('class="t new">New<' not in cy2[max(0, i_gw - 400):i_gw], "GRIMWEDGE card no longer tagged New (3 prior snapshots)")
i_cp = cy2.find("CenterPoint")
ck2('class="t new">New<' not in cy2[max(0, i_cp - 400):i_cp], "CenterPoint no longer tagged New (5 prior snapshots)")
ws2 = P["wallstreet-briefing.html"]
ck2(ws2.count('class="t new">New<') == 0, "markets New count == 0 (Fluence is no longer 0-hit)")
ck2(P["mma-briefing.html"].count('class="t new">New<') == 0, "mma New count == 0")
ck2(P["index.html"].count('class="t new">New<') == 0, "index New count == 0")

# R3-R6 -- markets repairs landed
ck2("same two that hurt yesterday" not in ws2, "unsourced yesterday-drivers inference removed")
ck2("The two drivers named are" in ws2, "drivers stated plainly")
ck2("Yahoo live blog" not in ws2, "over-specific attribution removed")
ck2("Another read of the session has the" in ws2, "neutral attribution in place")
ck2("cuts guidance by half a billion" not in ws2, "computed 'half a billion' headline removed")
ck2("cuts its full-year guidance to $2.4 billion" in ws2, "Fluence headline uses the stated figure")
ck2("opposite of how it is trading" not in ws2, "over-reaching energy comparison removed")
ck2("XLE was slightly lower" in ws2, "energy line now matches the sourced move")

# R7-R8 -- mma repairs landed
mm2 = P["mma-briefing.html"]
ck2("breaks his silence" not in mm2, "Aspinall headline no longer asserts more than the source")
ck2("Nothing fetched this run states what the update says" in mm2, "Aspinall item states its own limit")
ck2("Season 10 is the show" not in mm2, "tautological DWCS line cut")

# cross-page date coherence: the MMA page already had Saturday 19 September
ck2("Saturday 19 September" in mm2, "mma card weekday agrees with the calendar")
ck2("Sat 19 Sep" in mm2, "mma dateline agrees")

print("post-repair checks: %d, failures: %d" % (n2, len(f2)))
for x in f2: print("  FAIL:", x)
sys.exit(1 if (fail or f2) else 0)
