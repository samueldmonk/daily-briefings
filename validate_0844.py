#!/usr/bin/env python3
"""Validation gate for the Aug 29 2026 second Morning Edition."""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
STAMP = sys.argv[2] if len(sys.argv) > 2 else "8:44 AM"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: open(os.path.join(D, p), encoding="utf-8").read() for p in PAGES}
IDX, CY, WS, MM = (S[p] for p in PAGES)

checks = 0
fails = []

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

# ---- 1. nav / stamps ----
for p, s in S.items():
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"):
        ck('href="%s"' % href in s, "%s: nav missing %s" % (p, href))
    ck(s.count('nav.tabs') >= 1 or 'class="tabs"' in s, "%s: no tabs nav" % p)
    ck(len(re.findall(r'<a href="[^"]+" class="on">', s)) == 1,
       "%s: not exactly one active tab" % p)
    for i in ("id=\"edition\"", "id=\"datestamp\"", "id=\"updated\"", "id=\"freshline\""):
        ck(i in s, "%s: missing %s" % (p, i))
    ck("America/New_York" in s and "Morning Edition" in s, "%s: self-stamp JS missing" % p)
    ck("Saturday, August 29, 2026" in s, "%s: date missing" % p)

# ---- 2. tldr / index card parity ----
ck('class="tldr"' not in IDX, "index: tldr strip must be absent")
for name, s in (("cyber", CY), ("ws", WS), ("mma", MM)):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', s, re.S)
    ck(m is not None, "%s: tldr not parseable" % name)
    if m:
        body = norm(m.group(1))
        ck(body in norm(IDX), "%s: index card not byte-identical to tldr" % name)
for lab in ("The Wire", "The Tape", "Tale of the Tape"):
    ck(lab in IDX, "index: missing card label %s" % lab)

# ---- 3. TradingView widgets ----
tv = re.findall(r's3\.tradingview\.com/external-embedding/embed-widget-([a-z-]+)\.js', WS)
ck(len(tv) == 8, "ws: expected 8 TradingView scripts, got %d" % len(tv))
ck(len(set(tv)) == 6, "ws: expected 6 widget types, got %d %s" % (len(set(tv)), sorted(set(tv))))
ck(tv.count("single-quote") == 3, "ws: expected 3 single-quote widgets, got %d" % tv.count("single-quote"))
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(sym in WS, "ws: tape missing %s" % sym)
ck('"symbol":"NASDAQ:PYPL"' in WS, "ws: Chart of the Day must be NASDAQ:PYPL")
for p in ("index.html", "cyber-briefing.html", "mma-briefing.html"):
    ck("tradingview.com" not in S[p], "%s: must contain no live widgets" % p)

# ---- 4. close reconciliation arithmetic ----
ck(abs((53569.44 - 9.45) - 53559.99) < 0.005, "arith: Dow close does not reconcile")
ck(abs((7711.76 / 7730.99 - 1) * 100 + 0.25) < 0.005, "arith: S&P pct does not round to -0.25")
ck(abs((26402.42 / 26541.35 - 1) * 100 + 0.52) < 0.005, "arith: Nasdaq pct does not round to -0.52")
for lvl in ("7,711.76", "26,402.42", "53,559.99", "7,730.99", "26,541.35", "53,569.44"):
    ck(lvl in WS, "ws: scorecard missing level %s" % lvl)

# ---- 5. closed-market discipline ----
ck("as of ~" not in WS, "ws: intraday 'as of ~' marker on a closed-market page")
ck("Monday, August 31" in WS, "ws: must state the reopen date")
ck("7,673.04" not in WS, "ws: rejected level 7,673.04 reappeared")
ck("After-Hours" not in WS and "After Hours" not in WS, "ws: after-hours section on a weekend page")
i182 = WS.find("1.82%")
ck(i182 == -1 or "did not\nreappear" in WS[max(0, i182 - 400):i182 + 400] or
   "stays unpublished" in WS[max(0, i182 - 400):i182 + 400],
   "ws: 1.82% not window-scoped to its rejection text")
ck("$60.50" in WS and "$53 billion" in WS, "ws: PayPal bid terms missing")
ck("premarket" in WS, "ws: PayPal 16% must be labelled premarket")
ck("+58,000" in WS and "4.1%" in WS, "ws: payroll consensus missing")

# ---- 6. CVE whitelist ----
ALLOWED = {"CVE-2026-8452", "CVE-2026-82078", "CVE-2026-81578", "CVE-2026-53362",
           "CVE-2026-66384", "CVE-2023-49105", "CVE-2026-21962", "CVE-2019-1068",
           "CVE-2026-69836", "CVE-2022-0995", "CVE-2021-23758", "CVE-2015-5287",
           "CVE-2015-3246"}
found = set(re.findall(r"CVE-\d{4}-\d{4,6}", CY))
ck(found <= ALLOWED, "cyber: unlisted CVE id(s) %s" % sorted(found - ALLOWED))
ck(len(found) >= 13, "cyber: expected >=13 CVE ids, got %d" % len(found))
ck("9.8" not in CY, "cyber: forbidden CVSS 9.8 present")
ck("10.0" in CY and "CVE-2026-69836" in CY, "cyber: Entra ID 10.0 row missing")

# ---- 7. Citrix builds, both sets ----
for b in ("14.1-73.32", "13.1-63.21", "14.1-72.61", "13.1-63.18", "13.1-37.272", "CTX696604"):
    ck(b in CY, "cyber: missing Citrix build/advisory %s" % b)

# ---- 8. KEV countdowns and directives ----
for cd in ("0 days left", "1 day left", "11 days left", "12 days left"):
    ck(cd in CY, "cyber: missing KEV countdown '%s'" % cd)
ck("BOD 26-04" in CY, "cyber: BOD 26-04 missing")
j = CY.find("BOD 22-01")
ck(j != -1 and "superseded" in CY[j:j + 400], "cyber: BOD 22-01 not marked superseded")
ck("Saturday, Aug 29" in CY and "Wednesday, Sept 9" in CY, "cyber: KEV due dates missing")
ck("36 exploitation attempts" in CY, "cyber: Citrix telemetry missing")
ck("170,000" in CY and "UAT-10147" in CY, "cyber: UAT-10147 spotlight missing")
ck("21,019" in CY and "7,701" in CY, "cyber: CISA review figures missing")

# ---- 9. champions board ----
rows = re.findall(r"<tr><td>([^<]+)</td><td><b>([^<]+)</b></td><td>(.*?)</td></tr>", MM, re.S)
ck(len(rows) >= 11, "mma: champions board has %d rows" % len(rows))
champs = {d.strip(): c.strip() for d, c, _ in rows}
EXPECT = {"Heavyweight": "Tom Aspinall", "Light Heavyweight": "Carlos Ulberg",
          "Middleweight": "Sean Strickland", "Welterweight": "Islam Makhachev",
          "Lightweight": "Justin Gaethje", "Featherweight": "Alexander Volkanovski",
          "Bantamweight": "Petr Yan", "Flyweight": "Joshua Van"}
for div, who in EXPECT.items():
    ck(champs.get(div) == who, "mma: %s champion is %r, expected %r" % (div, champs.get(div), who))
cells = " ".join(champs.values())
for bad in ("Pereira", "Chimaev", "Topuria", "vacant", "Vacant"):
    ck(bad not in cells, "mma: regression %r appears in a champion cell" % bad)
for trap in ("Shamil Yakhyaev", "Cody Salkilld", "Abdul-Rakhman"):
    ck(trap not in MM, "mma: trap string %r present" % trap)

# ---- 10. MMA results discipline ----
ck(MM.count("<b>Undecided</b>") == 1, "mma: expected exactly 1 Undecided row, got %d" % MM.count("<b>Undecided</b>"))
ck("Not resulted in any source fetched this run" in MM, "mma: undecided reason text missing")
ck("Denise Gomes" in MM and "4:49 of round 1" in MM, "mma: co-main result missing")
ck("KO (elbows and punches)" in MM, "mma: co-main method missing")
ck("catchweight" in MM, "mma: catchweight label missing")
ck("guillotine choke" in MM and "rear-naked choke" in MM, "mma: both submission methods must appear")
ck("20% of his purse" in MM, "mma: purse forfeit missing")
for form in ("Aoriqileng", "Qileng Aori", "Sumudaerji", "Su Mudaerji"):
    ck(form in MM, "mma: spelling form %r missing" % form)
ck(MM.count('class="tag pros"') == 4, "mma: expected 4 prospect tags, got %d" % MM.count('class="tag pros"'))
ck("2026-09-20T01:00:00Z" in MM, "mma: countdown target changed")
ck("Accor Arena" in MM and "Hooker" in MM and "Parnasse" in MM, "mma: Paris card missing")
# no bout may be labelled with a division the primary sources did not state
ck("(prelim)</td>" not in MM, "mma: a prelim row still carries no division label")

# ---- 11. freshness: every 'tag new' carries this edition's stamp ----
for p, s in S.items():
    for tag in re.findall(r'<span class="tag new">(.*?)</span>', s):
        ck(STAMP in tag, "%s: stale 'New' tag %r (expected %s)" % (p, tag, STAMP))
    ck(OLD_ABSENT := ("8:40 AM" not in s), "%s: previous edition stamp 8:40 AM still present" % p)

# ---- 12. Aug 29 present broadly ----
ck(sum(1 for s in S.values() if "August 29" in s or "Aug 29" in s) >= 4,
   "Aug 29 not present on all four pages")

print("validate: %d checks, %d failures" % (checks, len(fails)))
for f in fails:
    print("  FAIL " + f)
sys.exit(1 if fails else 0)
