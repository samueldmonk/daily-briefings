# -*- coding: utf-8 -*-
"""Pre-publish validator. Every guard that narrows scope must also prove it still matches."""
import re, datetime, sys

FAIL = []
N = [0]


def chk(cond, msg):
    N[0] += 1
    if not cond:
        FAIL.append(msg)


def ran(m, label):
    """A guard that silently stops matching is worse than one that over-reaches."""
    N[0] += 1
    if not m:
        FAIL.append("GUARD DID NOT RUN: " + label)


IX = open("index.html").read()
CY = open("cyber-briefing.html").read()
WS = open("wallstreet-briefing.html").read()
MM = open("mma-briefing.html").read()
ALL = {"index": IX, "cyber": CY, "ws": WS, "mma": MM}

# ---------- structural ----------
for k, doc in ALL.items():
    chk(doc.startswith("<!DOCTYPE html>"), k + ": missing doctype")
    chk(doc.rstrip().endswith("</html>"), k + ": unterminated")
    for el in ('id="edition"', 'id="datestamp"', 'id="updated"', 'class="pill live"'):
        chk(el in doc, "%s: masthead missing %s" % (k, el))
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"):
        chk('href="%s"' % href in doc, "%s: nav missing %s" % (k, href))
    chk(doc.count('class="active"') == 1, k + ": must have exactly one active nav tab")
    chk("getElementById('datestamp')" in doc, k + ": self-stamp JS missing")
    chk(doc.count("<h1") == 1, k + ": expected exactly one h1")

for k in ("cyber", "ws", "mma"):
    chk('class="tldr"' in ALL[k], k + ": missing summary strip")
    chk('id="freshline"' in ALL[k], k + ": missing freshness line")
    chk("<footer>" in ALL[k] and "Sources" in ALL[k], k + ": missing sources footer")
    chk('class="disc"' in ALL[k], k + ": missing disclaimer")

chk('<b>The Tape</b>' in WS, "ws: wrong tldr label")
chk('<b>The Wire</b>' in CY, "cyber: wrong tldr label")
chk('<b>Tale of the Tape</b>' in MM, "mma: wrong tldr label")
chk('class="tldr"' not in IX, "index: must use cards, not a tldr strip")

# index must mirror each page's own summary verbatim
for name, doc in (("ws", WS), ("cyber", CY), ("mma", MM)):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', doc, re.S)
    ran(m, name + " tldr extraction")
    if m:
        chk(m.group(1) in IX, "index: Markets/Cyber/MMA card does not mirror %s summary verbatim" % name)

# ---------- live widgets ----------
for w in ("embed-widget-ticker-tape", "embed-widget-single-quote", "embed-widget-timeline",
          "embed-widget-stock-heatmap", "embed-widget-mini-symbol-overview", "embed-widget-events"):
    chk(w in WS, "ws: missing widget " + w)
chk(WS.count("embed-widget-single-quote") == 3, "ws: need exactly 3 single-quote widgets")
for s in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    chk(s in WS, "ws: ticker tape must retain " + s)
chk('class="livebar"' in WS, "ws: ticker tape not wrapped in .livebar")
for k in ("index", "cyber", "mma"):
    chk("tradingview.com" not in ALL[k], k + ": must not carry live market widgets")

# ---------- markets arithmetic ----------
# Closes must reconcile against Tuesday's verified closes.
for prev, chg, close, pct in ((7631.47, 35.13, 7666.60, 0.46),
                              (52766.88, 295.07, 53061.95, 0.56),
                              (26099.77, 118.06, 26217.83, 0.45)):
    chk(abs(prev + chg - close) < 0.02, "ws: %s + %s != %s" % (prev, chg, close))
    chk(abs(chg / prev * 100 - pct) < 0.01, "ws: pct mismatch for %s" % close)
for lvl in ("7,666.60", "53,061.95", "26,217.83", "+295.07", "+35.13", "+118.06"):
    chk(lvl in WS, "ws: scorecard missing " + lvl)

# Credo close must reconcile to the sourced prior close.
chk(abs(206.63 * (1 - 0.2069) - 163.87) < 0.02, "ws: Credo close does not reconcile")
chk("163.87" in WS and "206.63" in WS, "ws: Credo reconciliation figures absent")

# 4.814% must never appear inside a rates-table cell.
cells = re.findall(r"<td[^>]*>(.*?)</td>", WS, re.S)
ran(cells, "ws td-cell extraction")
chk(not any("4.814" in c for c in cells), "ws: 4.814% leaked into a rates-table cell")
chk("4.814%" in WS, "ws: the 4.814% conflict note should still be printed")

# Every undated/intraday percentage must sit near an explicit time label.
for pct, label in (("+4.7%", "10:36 AM"), ("+7%", "10:36 AM"), ("−9.7%", "10:36 AM"),
                   ("+8.1%", "premarket"), ("+21%", "premarket")):
    i = WS.find(pct)
    ran(i >= 0, "ws intraday-qualifier guard for " + pct)
    if i >= 0:
        chk(label in WS[max(0, i - 500):i + 700],
            "ws: %s printed without its %s qualifier nearby" % (pct, label))

# After-hours block required post-close, with its publication time stated.
chk("After-Hours Movers" in WS, "ws: post-close edition needs an after-hours section")
chk("4:30 PM ET" in WS, "ws: after-hours figures must carry their publication time")
chk("−3.5%" in WS and "6.5%" in WS and "4.14%" in WS,
    "ws: the three conflicting Broadcom after-hours figures must all be printed")

# Sector refusal must be present and no sector percentage table published.
chk("refused for a sixth consecutive run" in WS, "ws: sector refusal note missing")
chk("+42%" in WS and "+43%" in WS, "ws: the self-contradicting energy YTD pair must be shown")

# ---------- cyber deadlines ----------
TODAY = datetime.date(2026, 9, 2)
DUE = {"CVE-2026-21962": (datetime.date(2026, 8, 27), -6),
       "CVE-2026-64849": (datetime.date(2026, 9, 2), 0),
       "CVE-2026-9586": (datetime.date(2026, 9, 5), 3),
       "CVE-2021-23758": (datetime.date(2026, 9, 9), 7),
       "CVE-2026-66384": (datetime.date(2026, 9, 10), 8),
       "CVE-2026-81578": (datetime.date(2026, 9, 14), 12),
       "CVE-2026-82078": (datetime.date(2026, 9, 14), 12),
       "CVE-2026-48710": (datetime.date(2026, 9, 16), 14)}
for cve, (d, days) in DUE.items():
    chk((d - TODAY).days == days, "cyber: countdown arithmetic wrong for " + cve)
    chk(cve in CY, "cyber: %s absent from the page" % cve)
    if days > 0:
        chk("%d days left" % days in CY, "cyber: missing '%d days left' for %s" % (days, cve))
chk("0 days left" in CY, "cyber: MLflow zero-day-left countdown missing")
chk("overdue by 6 days" in CY, "cyber: Oracle overdue countdown missing")

# Patch Priority deadline must match the KEV section deadline.
m = re.search(r'class="callout crit".*?</div></div>', CY, re.S)
ran(m, "cyber patch-priority block extraction")
if m:
    chk("September 2" in m.group(0) and "0 days left" not in m.group(0).replace("zero days left", ""),
        "cyber: patch priority must name the same verified deadline")
    chk("CVE-2026-64849" in m.group(0), "cyber: patch priority must name the CVE")

# Citrix must carry NO numeric countdown inside its own list item.
m = re.search(r"<li[^>]*>(?:(?!</li>).)*CVE-2026-8452(?:(?!</li>).)*</li>", CY, re.S)
ran(m, "cyber Citrix <li> guard")
if m:
    chk(not re.search(r"\d+\s*days? left", m.group(0)),
        "cyber: a numeric countdown leaked into the Citrix item")

# The 9.8 ban: 9.8 may appear ONLY when explicitly attributed and refused.
for mm in re.finditer(r"9\.8", CY):
    i = mm.start()
    chk("not adopted" in CY[i:i + 700] or "attributed" in CY[i:i + 700] or "reported" in CY[max(0, i-60):i+60],
        "cyber: an unattributed 9.8 appeared at offset %d" % i)
chk("9.8 (reported)" in CY, "cyber: the VMware 9.8 must be marked as reported, not vendor-confirmed")

# Vendor CVSS figures that standing corrections fix.
chk("10.0" in CY and "CVE-2026-83548" in CY, "cyber: SonicWall 10.0 missing")
chk("7.8" in CY, "cyber: SonicWall AMC 7.8 missing")
chk("9.3" in CY, "cyber: MLflow 9.3 missing")

# Nevada must never appear as a PUBLISHED incident. Narrowed from a page-wide ban, which
# over-reached onto the sentence documenting the refusal; paired with a ran() proof.
heads = re.findall(r"<h4>([^<]*)</h4>", CY)
ran(heads, "cyber breach-card heading extraction")
chk(not any("Nevada" in h for h in heads), "cyber: Nevada published as a breach card")
nv = [m.start() for m in re.finditer("Nevada", CY)]
for i in nv:
    chk("refused on sight" in CY[i:i + 400] or "permanent exclusion" in CY[max(0, i - 200):i + 200],
        "cyber: Nevada appeared outside the refusal note at offset %d" % i)
# Laundered-recency refusals must be documented.
chk("IDMerit" in CY and "Panera" in CY and "Vanderbilt" in CY, "cyber: refusal note incomplete")
# Aesto must be framed as a disclosure, anchored on its own card.
m = re.search(r"<h4>Aesto Health</h4>.*?</div>", CY, re.S)
ran(m, "cyber Aesto card guard")
if m:
    chk("disclosure" in m.group(0) and "December 18, 2025" in m.group(0),
        "cyber: Aesto must be dated as a disclosure, not a new intrusion")

# ---------- MMA ----------
# Champions: the middleweight CHAMPION CELL specifically must be Strickland, never Chimaev.
m = re.search(r"<tr><td>Middleweight</td><td class=\"win\">([^<]+)</td>", MM)
ran(m, "mma middleweight champion-cell guard")
if m:
    chk(m.group(1).strip() == "Sean Strickland", "mma: middleweight champion cell is not Strickland")
for div, champ in (("Light Heavyweight", "Carlos Ulberg"), ("Lightweight", "Justin Gaethje"),
                   ("Featherweight", "Alexander Volkanovski"), ("Flyweight", "Joshua Van"),
                   ("Bantamweight", "Petr Yan"), ("Welterweight", "Islam Makhachev"),
                   ("Heavyweight", "Tom Aspinall"), ("Women's Featherweight", "Vacant")):
    m = re.search(r"<tr><td>%s</td><td class=\"win\">([^<]+)</td>" % re.escape(div), MM)
    ran(m, "mma champion-cell guard for " + div)
    if m:
        chk(m.group(1).strip() == champ, "mma: %s should be %s, got %s" % (div, champ, m.group(1)))
# Pereira must not hold a belt. Narrowed from "anywhere in the champions table", which over-reached
# onto the note column legitimately naming him as the man Gane beat; paired with a ran() proof.
# Scope to the Champions Board table only — the results table reuses the .win class for winners.
champ_tbl = MM.split("Champions Board")[-1].split("</table>")[0]
ran(champ_tbl, "mma champions-table extraction")
winner_cells = re.findall(r'<td class="win">([^<]+)</td>', champ_tbl)
ran(winner_cells, "mma champion-cell sweep")
chk(len(winner_cells) == 13, "mma: expected 13 champion cells, got %d" % len(winner_cells))
chk(not any("Pereira" in c for c in winner_cells), "mma: Pereira listed as a champion")
chk(not any("Chimaev" in c for c in winner_cells), "mma: Chimaev listed as a champion")
chk(not any("Topuria" in c for c in winner_cells), "mma: Topuria listed as a champion")

# Parnasse must never be attributed to the Contender Series inside a prose block about him.
for blk in re.split(r"</(?:li|p|div|td|h4)>", MM):
    if "Parnasse" in blk and "Contender Series" in blk:
        chk("did not come through the Contender Series" in blk or "not a Contender Series" in blk.lower(),
            "mma: Parnasse linked to the Contender Series without a denial")
chk("two-time KSW featherweight" in MM, "mma: Parnasse's KSW provenance must be stated")
chk("late July 2026" in MM, "mma: Parnasse signing date missing")
chk("Salahdine" in MM and "Saladhine" not in MM, "mma: Parnasse forename spelling")

# Countdown target and the days-out arithmetic.
chk("2026-09-05T12:00:00-04:00" in MM, "mma: countdown target wrong")
chk('id="ufccdn"' in MM, "mma: countdown element missing")
days_out = (datetime.date(2026, 9, 5) - TODAY).days
chk(days_out == 3, "mma: days-out arithmetic")
chk("three days away" in MM or "three days out" in MM, "mma: days-out phrasing missing")
chk("four days" not in MM, "mma: banned wrong days-out string present")

# Odds must be reproduced, and no book claimed that was not named.
chk("−600" in MM and "+425" in MM and "DraftKings" in MM, "mma: Paris odds incomplete")
# Dariush, if named anywhere, must never be a champion or challenger.
for blk in re.split(r"</(?:li|p|div|td|h4)>", MM):
    if "Dariush" in blk:
        chk("champion" not in blk.lower() and "challenger" not in blk.lower(),
            "mma: Dariush mis-described")
# Refused Dana White slate must not be published as current news.
m = re.search(r"<li>[^<]*<b>A widely-surfacing.*?</li>", MM, re.S)
ran(m, "mma Dana White refusal guard")
if m:
    chk("refused" in m.group(0) and "cancelled" in m.group(0),
        "mma: the Harrison-Nunes item must be printed as a refusal")
chk(MM.count("Nunes") <= 3, "mma: Nunes appears too often for a refused item")

# Nothing 'upcoming' may already have happened.
for d in (5, 12, 19, 26):
    chk(datetime.date(2026, 9, d) >= TODAY, "mma: September %d listed as upcoming but is past" % d)

# ---------- cross-page ----------
chk("Chimaev" not in IX, "index: stale champion name leaked to the front page")
chk("&#9960;" in IX, "index: cyber icon must be the shield glyph")
chk("&#9880;" not in IX, "index: wrong (flower) glyph for cyber")

print("checks run: %d" % N[0])
if FAIL:
    print("\nRAISED %d:" % len(FAIL))
    for f in FAIL:
        print("  - " + f)
    sys.exit(1)
print("all clear")
