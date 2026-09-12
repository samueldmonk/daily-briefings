#!/usr/bin/env python3
import re, os
OUT = "/sessions/sleepy-hopeful-carson/mnt/outputs"
P = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
D = {f: open(os.path.join(OUT, f), encoding="utf-8").read() for f in P}
ix, cy, ws, mma = D["index.html"], D["cyber-briefing.html"], D["wallstreet-briefing.html"], D["mma-briefing.html"]

ok = fail = 0
def chk(cond, msg):
    global ok, fail
    if cond: ok += 1
    else: fail += 1; print("  FAIL:", msg)

def n(hay, needle):
    """count occurrences not embedded in a longer digit run (for numeric strings)"""
    if needle.replace(",", "").replace(".", "").isdigit():
        return len(re.findall(r"(?<![0-9])" + re.escape(needle) + r"(?![0-9])", hay))
    return hay.count(needle)

# --- structural, all four pages
for f, s in D.items():
    chk(s.lstrip().lower().startswith("<!doctype html>"), f + " doctype")
    chk(s.rstrip().endswith("</html>"), f + " tail")
    for i in ("edition", "datestamp", "updated", "freshline"):
        chk('id="%s"' % i in s, "%s masthead id %s" % (f, i))
    chk(s.count("America/New_York") >= 3, f + " timezone refs")
    for tab in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"):
        chk(('href="%s"' % tab) in s, "%s nav -> %s" % (f, tab))
    chk(s.count('class="on"') == 1, f + " exactly one active tab")
    m = re.search(r'<a class="on" href="([^"]+)"', s)
    chk(m and m.group(1) == f, f + " active tab is self")
    for tag in ("div", "p", "h2", "h3", "ul", "li", "table", "tr", "td", "span", "a", "b", "footer", "nav"):
        chk(s.count("<%s" % tag) >= s.count("</%s>" % tag), "%s tag balance %s" % (f, tag))

# --- TradingView: Wall Street only
chk(ws.count("s3.tradingview.com") == 8, "ws 8 tradingview scripts (got %d)" % ws.count("s3.tradingview.com"))
for f in ("index.html", "cyber-briefing.html", "mma-briefing.html"):
    chk(D[f].count("s3.tradingview.com") == 0, f + " zero tradingview")
chk(ws.count("embed-widget-single-quote") == 3, "ws 3 single-quote widgets")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    chk(sym in ws, "ws symbol " + sym)

# --- index levels asserted exactly once, inside the Scorecard
score = ws.split("<h2>Weekly Scorecard")[1].split("<h2>")[0] if "<h2>Weekly Scorecard" in ws else ""
for lvl in ("7,656.98", "26,333.04", "52,573.29"):
    chk(n(ws, lvl) == 1, "ws level %s asserted once (got %d)" % (lvl, n(ws, lvl)))
    chk(lvl in score, "ws level %s inside Scorecard" % lvl)
# points/percent reconcile
for lvl, pts, pct in (("7656.98", 65.28, 0.86), ("26333.04", 251.31, 0.96), ("52573.29", 509.19, 0.98)):
    close = float(lvl); prior = close - pts
    chk(abs(pts / prior * 100 - pct) < 0.02, "ws reconcile %s" % lvl)
r7=re.search(r"7,666.{0,40}?<b>not</b>\s*published", ws, re.S)
chk(n(ws, "7,666") == 1 and bool(r7), "ws 7,666 refusal guard retained")

# --- oil: new settlement figures
chk(n(ws, "100.05") >= 1, "ws WTI settle 100.05 present")
chk(n(ws, "104.61") >= 1, "ws Brent settle 104.61 present")
chk("(settle)" in ws, "ws settle labels present")
chk(n(ws, "104.02") == 1 and "prior editions carried only the $104.02 open" in ws,
    "ws superseded WTI open named exactly once, inside its supersedes clause")
chk(n(ws, "104.42") == 1, "ws superseded Brent 104.42 named exactly once")
chk("8.7% on the week" in ws and "9.4% on the week" in ws, "ws weekly crude gains")
chk("108.21" in ws and "102.96" in ws, "ws intraday pair printed")
chk("Strait of Hormuz" in ws and "Oman" in ws, "ws oil driver named")
chk("Bank of England" in ws and "Bank of Japan" in ws, "ws three central banks")

# --- cyber: Metabase top story
ts = cy.split("<h2>Top Story</h2>")[1].split("<h2>")[0]
chk("CVE-2026-72898" in ts, "cy top story is Metabase")
chk("reset_password" in ts, "cy Metabase endpoint named")
chk("11 August 2026" in ts, "cy Metabase KEV add date")
chk("Rescana" in ts, "cy ShipMonk attribution qualified")
chk("BlueMoon" not in ts, "cy BlueMoon demoted out of top story")
chk("BlueMoon" in cy, "cy BlueMoon retained as carried card")
body = cy.split("<footer>")[0]
chk(n(body, "10.0") >= 2, "cy two CVSS 10.0 assertions")
# CVE table
tbl = cy.split("<h2>Vulnerability Watch</h2>")[1].split("</table>")[0]
rows = tbl.count("<tr>") - 1
chk(rows == 20, "cy 20 CVE rows (got %d)" % rows)
chk("CVE-2026-72898" in tbl, "cy Metabase row in table")
# KEV consistency
z = len(re.findall(r"(?<![0-9])0 days left", body))
chk(z == 2, "cy anchored '0 days left' exactly twice (got %d)" % z)
chk(body.count("0 days left") == 3, "cy raw '0 days left' is 3 — trap pinned: the third is inside '10 days left'")
chk(len(re.findall(r"(?<![0-9])10 days left", body)) == 1, "cy '10 days left' exactly once and distinct")
chk(body.count("12 September 2026") == 2, "cy today's deadline asserted twice (got %d)" % body.count("12 September 2026"))
chk("22 September 2026" in cy and "10 days left" in cy, "cy 22 Sep KEV deadline")
chk("23 September 2026" in cy and "11 days left" in cy, "cy 23 Sep KEV deadline")
chk("BOD 26-04" in cy, "cy BOD 26-04 present")
chk("BOD 22-01" not in cy or "no longer governs" in cy or "revoked" in cy,
    "cy BOD 22-01 appears only where it is disapplied")
# new breach items
for t in ("81,000", "347,000", "220 million", "3.5 million", "4.1 million", "67,000"):
    chk(t in cy, "cy figure " + t)
chk("INC Ransom" not in cy, "cy INC Ransom stays removed")
chk("Human and Health Services" not in cy and "Health and Human Services" not in cy, "cy HHS string stays removed")
# patch tuesday: no single number asserted
for c in ("964", "966", "973", "974", "1,169"):
    chk(c in cy, "cy patch count " + c)
chk(n(cy, "973") == cy.count("973") - cy.count("69730"), "cy 973 substring trap pinned")

# --- mma
chk(mma.count("1 PM ET") == 2 and "is retired rather than carried" in mma,
    "mma 1 PM ET appears only inside the clause retiring it (got %d)" % mma.count("1 PM ET"))
chk(mma.count("2 PM ET") >= 2, "mma 2 PM ET prelim time")
chk("1:10 PM ET" in mma, "mma source-check timestamp")
for bad in ("def. ", "defeats ", "submission at", "via TKO", "wins by"):
    chk(bad not in mma.split("<h2>Champions Board</h2>")[0].split("Last Event")[0], "mma no Noche result string: " + bad)
# champions
for c in ("Tom Aspinall", "Carlos Ulberg", "Sean Strickland", "Islam Makhachev", "Justin Gaethje",
          "Alexander Volkanovski", "Petr Yan", "Joshua Van", "Kayla Harrison", "Mackenzie Dern"):
    chk(c in mma, "mma champion " + c)
ct = mma.split("<h2>Champions Board</h2>")[1]
ct = ct.split("<table")[1].split("</table>")[0] if "<table" in ct else ""
# Guard the CHAMPION cell, not the row: Pereira legitimately appears as the man Gane beat,
# and Shevchenko in the VACANT row's explanatory note. Blunt absence checks fire on both.
champ = {}
for row in re.findall(r"<tr>.*?</tr>", ct, re.S):
    cells = [re.sub("<[^>]+>", "", c).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
    if len(cells) >= 2: champ[cells[0]] = cells[1]
chk(ct != "", "mma champions table found")
chk(champ.get("Light Heavyweight") == "Carlos Ulberg",
    "mma LHW champion cell is Ulberg, not Pereira (got %r)" % champ.get("Light Heavyweight"))
chk("Pereira" not in champ.get("Light Heavyweight", ""), "mma LHW regression guard")
chk(champ.get("Women\u2019s Flyweight", "").upper() == "VACANT",
    "mma W-FLW champion cell is VACANT (got %r)" % champ.get("Women\u2019s Flyweight"))
chk(not any("Shevchenko" in v for v in champ.values()), "mma W-FLW regression guard: Shevchenko seats no belt")
chk(not any("Chimaev" in v for v in champ.values()), "mma MW regression guard: Chimaev seats no belt")
chk(champ.get("Featherweight") == "Alexander Volkanovski", "mma FW not vacant")
chk(champ.pop("Division", None) == "Champion", "mma champions header row present")
chk(len(champ) == 11, "mma 11 divisions on the board (got %d)" % len(champ))
chk("VACANT" in mma.upper(), "mma W-FLW vacant guard")
chk(mma.count("stripped") == 1 and "vacated" in mma, "mma 'stripped' trap: exactly one, inside rejecting clause")
chk("no content" in mma, "mma ESPN-unavailable disclosure")
chk("Jose Miguel Delgado" in mma, "mma full challenger name")
chk("Edgar Chairez" in mma or "Edgar Cháirez" in mma, "mma Chairez spelling")
chk("Regina Tarin" in mma and "8-0" in mma, "mma prelim records")

# --- index cards byte-identical to each page's tldr
for f, cls in (("cyber-briefing.html", "c-sec"), ("wallstreet-briefing.html", "c-mkt"), ("mma-briefing.html", "c-mma")):
    t = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', D[f], re.S).group(1)
    card = re.search(r'<a class="%s"[^>]*>.*?<h3>[^<]*</h3><p>(.*?)</p>' % cls, ix, re.S)
    chk(card and card.group(1) == t, "index card == %s tldr" % f)

# --- freshness / disclaimers
for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    chk('class="tldr"' in D[f], f + " has tldr strip")
    chk('class="disc"' in D[f], f + " has disclaimer")
chk("Nothing here is investment advice" in ws, "ws investment disclaimer")
chk("subject to change" in mma, "mma card-change disclaimer")

print("\n%d checks, %d failures" % (ok + fail, fail))
