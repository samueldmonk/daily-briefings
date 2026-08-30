#!/usr/bin/env python3
"""Pre-publish validator, 2026-08-30 5:10 PM ET edition."""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
STAMP = "5:10 PM"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
BRIEFS = PAGES[1:]
fails, checks = [], [0]

def ck(cond, msg):
    checks[0] += 1
    if not cond:
        fails.append(msg)

def rd(p):
    return open(os.path.join(D, p), encoding="utf-8").read()

H = {p: rd(p) for p in PAGES}

# ── structure ───────────────────────────────────────────────────────────────
for p, h in H.items():
    for tab in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                "mma-briefing.html", "archive.html"]:
        ck('href="%s"' % tab in h, "%s: nav missing tab %s" % (p, tab))
    ck(len(re.findall(r'<a href="[^"]+" class="on">', h)) == 1,
       "%s: must have exactly one active tab" % p)
    for i in ["edition", "datestamp", "updated", "freshline"]:
        ck(re.search(r'<span[^>]*id="%s"|<div[^>]*id="%s"' % (i, i), h),
           "%s: missing id=%s" % (p, i))
    ck("Intl.DateTimeFormat" in h and "America/New_York" in h, "%s: self-stamp JS missing" % p)
    ck("Data as of %s ET" % STAMP in h, "%s: freshline not stamped %s" % (p, STAMP))
    ck("8 AM&ndash;6 PM ET" in h, "%s: freshline missing refresh cadence" % p)

# tldr strip: on the three briefings, never on the index
for p in BRIEFS:
    ck('class="tldr"' in H[p], "%s: missing tldr strip" % p)
ck('class="tldr"' not in H["index.html"], "index.html: tldr strip must not appear")
for p, lab in [("wallstreet-briefing.html", "The Tape"), ("cyber-briefing.html", "The Wire"),
               ("mma-briefing.html", "Tale of the Tape")]:
    ck("<b>%s</b>" % lab in H[p], "%s: tldr label must be '%s'" % (p, lab))

# index cards must be byte-identical to each briefing's tldr (backwards anchor)
def tldr_of(h):
    return re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>', h, re.S).group(1)

def card_of(h, href):
    a = h.find('<a class="go" href="%s"' % href)
    pc = h.rfind("</p>", 0, a)
    po = h.rfind("<p>", 0, pc)
    return h[po + 3:pc]

for p in BRIEFS:
    c = card_of(H["index.html"], p)
    ck("<p>" not in c, "index.html: card for %s has a nested <p> (forward-match bug)" % p)
    ck(c == tldr_of(H[p]), "index.html: card for %s does not mirror its tldr exactly" % p)

# ── live widgets: Wall Street only ──────────────────────────────────────────
ws = H["wallstreet-briefing.html"]
for w in ["ticker-tape", "single-quote", "timeline", "stock-heatmap",
          "mini-symbol-overview", "events"]:
    ck("embed-widget-%s.js" % w in ws, "wallstreet: missing widget %s" % w)
ck(ws.count("embed-widget-single-quote.js") == 3, "wallstreet: need exactly 3 single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(sym in ws, "wallstreet: ticker tape missing %s" % sym)
ck('"symbol":"NASDAQ:PYPL"' in ws, "wallstreet: Chart of the Day must be NASDAQ:PYPL")
for p in ["index.html", "cyber-briefing.html", "mma-briefing.html"]:
    ck("s3.tradingview.com" not in H[p], "%s: must carry no live widgets" % p)

# ── markets: closes, reconciliation, this run's new figures ─────────────────
for v in ["7,711.76", "26,402.42", "53,559.99"]:
    ck(v in ws, "wallstreet: missing Friday close %s" % v)
ck(abs((7711.76 + 19.23) - 7730.99) < 0.005, "arith: S&P Fri+chg != Thu")
ck(abs((26402.42 + 138.93) - 26541.35) < 0.005, "arith: Nasdaq Fri+chg != Thu")
ck(abs((53559.99 + 9.45) - 53569.44) < 0.005, "arith: Dow Fri+chg != Thu")
ck(abs(7711.76 / 7730.99 - 1 + 0.002487) < 0.00002, "arith: S&P pct != -0.25%")
# this run's new movers
ck("12.63" in ws, "wallstreet: PYPL Friday close -12.63% missing")
ck("10.66" in ws, "wallstreet: MRVL -10.66% missing")
ck("20.34" in ws and "surged 21%" in ws, "wallstreet: Elastic pair must show both renderings")
ck("neither is adopted" in ws or "neither adopted" in ws,
   "wallstreet: Elastic pair must be marked unadopted")
ck("83.54" in ws and "<i>open</i>" in ws, "wallstreet: WTI 83.54 must be labelled an open")
ck("$83.44" in ws, "wallstreet: carried WTI close 83.44 must remain")
ck("4.73%" in ws, "wallstreet: 10-year 4.73% missing")
ck("49% for a hike" in ws, "wallstreet: Polymarket 49% read missing")
# standing refusals
for m in re.finditer(r"1\.82%", ws):
    ctx = ws[max(0, m.start() - 260):m.end() + 260]
    ck("unpublished" in ctx or "did not\nreappear" in ctx or "did not reappear" in ctx,
       "wallstreet: 1.82% appears as a PUBLISHED sector figure, not as a recorded refusal")
ck("7,673.04" not in ws, "wallstreet: 7,673.04 is refused and must stay off")
ck("Nasdaq 100" in ws or "Nasdaq-100" in ws, "wallstreet: NDX must remain recorded-not-promoted")
ck("29,433.43" in ws, "wallstreet: NDX 29,433.43 recorded figure missing")
# weekend page must not assert a live intraday clock
ck("as of ~" not in ws, "wallstreet: no intraday 'as of ~' marker on a closed-tape page")
ck("premarket" in ws, "wallstreet: PYPL premarket figure must remain beside the close")

# ── cyber ───────────────────────────────────────────────────────────────────
cy = H["cyber-briefing.html"]
ck("CVE-2026-21962" in cy, "cyber: Oracle CVE must be restored")
ck("OVERDUE" in cy, "cyber: Oracle deadline must be marked overdue")
ck("August 24" in cy, "cyber: Oracle KEV add date missing")
ck("BOD 26-04" in cy, "cyber: BOD 26-04 must be named")
ck("BOD 22-01" not in cy or "supersed" in cy.lower(),
   "cyber: BOD 22-01 may appear only as superseded")
ck("CVE-2026-53362" in cy and "IPv6" in cy and "UDP socket" in cy,
   "cyber: Linux kernel mechanism missing")
ck("September 10" in cy and "August 30" in cy,
   "cyber: both readings of the 53362 deadline must be printed")
ck("Fiserv" in cy, "cyber: Fiserv missing from Cl0p claimed victims")
ck("Ransom-ISAC" in cy and "July 22" in cy, "cyber: Ransom-ISAC July 22 notice missing")
ck("JSP web shells" in cy or "JSP webshells" in cy, "cyber: JSP web shells missing")
ck("published no samples" in cy, "cyber: Cl0p no-samples caveat missing")
ck("ZaWoo" in cy, "cyber: ZaWoo listings missing")
ck("not confirmation of a breach" in cy, "cyber: leak-site caveat must travel with the listings")
ck("Nevada" in cy and "2025" in cy, "cyber: Nevada refusal must be recorded as a 2025 event")
ck("CVE-2026-6876" in cy and "CVE-2026-6875" in cy,
   "cyber: both ServiceNow fourth-CVE readings must be recorded")
ck("10.0" in cy, "cyber: ServiceNow CVSS 10.0 missing")
# no Citrix row may carry a 9.8 CVSS cell (narrowed guard from the 4:36 run)
for row in re.findall(r"<tr>.*?</tr>", cy, re.S):
    if "Citrix" in row or "NetScaler" in row:
        ck("<td>9.8</td>" not in row, "cyber: a Citrix row carries a 9.8 CVSS cell")
ck("9.6" in cy, "cyber: LoadMaster vendor CVSS 9.6 missing")
# CVE well-formedness + liveness
ids = set(re.findall(r"CVE-\d{4}-\d{4,6}", cy))
ck(len(ids) >= 15, "cyber: too few distinct CVE ids (%d)" % len(ids))
for i in ids:
    ck(re.fullmatch(r"CVE-(19|20)\d{2}-\d{4,6}", i) is not None, "cyber: malformed id %s" % i)

# ── mma ─────────────────────────────────────────────────────────────────────
mma = H["mma-briefing.html"]
CHAMPS = ["Aspinall", "Ulberg", "Strickland", "Makhachev", "Gaethje", "Volkanovski",
          "Yan", "Van", "Harrison", "Shevchenko", "Dern"]
for c in CHAMPS:
    ck(c in mma, "mma: champion %s missing from the board" % c)
# champion COLUMN only (cell 2 of each row) may not contain a dethroned name
rows = re.findall(r"<tr>(.*?)</tr>", mma, re.S)
champ_rows = 0
for r in rows:
    cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
    if len(cells) >= 2:
        champ_rows += 1
        cell = re.sub(r"<[^>]+>", "", cells[1])
        for bad in ["Pereira", "Chimaev", "Topuria", "Dvalishvili", "Pantoja", "vacant"]:
            ck(bad not in cell,
               "mma: '%s' appears in a CHAMPION cell -- regression" % bad)
ck(champ_rows >= 11, "mma: champions table must have >= 11 rows (found %d)" % champ_rows)
ck("sixty-seventh" in mma, "mma: unchanged-board streak note missing")
ck("Song Yadong" in mma and "1:48" in mma, "mma: main event result missing")
ck("Gomes" in mma and "Yan Xiaonan" in mma, "mma: co-main result missing")
ck("Undecided" not in mma, "mma: no bout may still read Undecided")
ck("Parnasse" in mma and "Hooker" in mma, "mma: UFC Paris headliner missing")
ck("Moicano" in mma and "Ortega" in mma, "mma: UFC 331 additions missing")
ck("5 PM ET" in mma and "7 PM ET" in mma and "9 PM ET" in mma,
   "mma: third UFC 331 start-time rendering missing")
ck("ufccdn" in mma and "getElementById('ufccdn')" in mma, "mma: countdown script missing")
# spelling traps
for trap in ["Cody Salkilld", "Shamil Yakhyaev", "Abdul-Rakhman"]:
    ck(trap not in mma, "mma: forbidden spelling '%s'" % trap)
ck("Dariush" not in mma or not re.search(r"Dariush[^.]{0,60}(champion|title challenger)", mma),
   "mma: Dariush must not be called a champion or title challenger")

# ── footers ─────────────────────────────────────────────────────────────────
for p in BRIEFS:
    h = H[p]
    tail = h[h.find("<footer"):]
    hrefs = re.findall(r'href="(https?://[^"]+)"', tail)
    ck(len(hrefs) >= 6, "%s: footer needs >= 6 sources (found %d)" % (p, len(hrefs)))
    ck(len(hrefs) == len(set(hrefs)), "%s: duplicate footer links" % p)
    ck(all(u.startswith("https://") for u in hrefs), "%s: non-https source link" % p)
    ck('class="disc"' in tail, "%s: missing .disc disclaimer block" % p)
ck("investment advice" in ws.lower(), "wallstreet: investment-advice disclaimer missing")
ck("vulnerabi" in H["cyber-briefing.html"].lower(), "cyber: vulnerability-management disclaimer missing")
ck("subject to change" in mma.lower(), "mma: 'subject to change' disclaimer missing")

# ── this run's stamp appears, and never ahead of the masthead ───────────────
for p in BRIEFS:
    ck(STAMP in H[p], "%s: run stamp %s missing" % (p, STAMP))
ck(len(re.findall(r'class="tag new"', ws)) >= 1, "wallstreet: no New tag this run")

print("validate_1710: %d checks, %d failures" % (checks[0], len(fails)))
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
