# -*- coding: utf-8 -*-
import io, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
PAGES = {n: io.open(os.path.join(D, n), encoding="utf-8").read()
         for n in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html")}
CY, WS, MMA, IX = PAGES["cyber-briefing.html"], PAGES["wallstreet-briefing.html"], PAGES["mma-briefing.html"], PAGES["index.html"]
ok = fail = 0
def chk(cond, msg):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1; print("FAIL:", msg)

# ---- 1. tag balance across element types
TAGS = ["html","head","body","div","p","ul","li","table","tr","td","th","h2","h3","h4","span","b","footer","nav","a","header","script","style","title","code","em"]
for n, h in PAGES.items():
    for t in TAGS:
        o = len(re.findall(r"<%s[\s>]" % t, h)); c = len(re.findall(r"</%s>" % t, h))
        chk(o == c, "%s: <%s> %d open vs %d close" % (n, t, o, c))

# ---- 2. masthead / stamp / nav
for n, h in PAGES.items():
    for el in ('id="edition"', 'id="datestamp"', 'id="updated"', 'pill live'):
        chk(el in h, "%s missing %s" % (n, el))
    chk(h.count("America/New_York") >= 1, "%s missing stamp JS" % n)
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"):
        chk(('href="%s"' % href) in h, "%s nav missing %s" % (n, href))
    chk(h.count('nav class="tabs"') == 1, "%s: not exactly one nav" % n)
    chk(len(re.findall(r'<a href="[^"]+" class="active">', h)) == 1, "%s: not exactly one active tab" % n)
for n in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    chk('id="freshline"' in PAGES[n], "%s missing freshline" % n)
    chk(PAGES[n].count('class="tldr"') == 1, "%s: not exactly one tldr" % n)
chk('id="freshline"' in IX, "index missing freshline")
chk('class="tldr"' not in IX, "index should use cards not tldr")

# ---- 3. TradingView widgets: Wall Street only
TV = "s3.tradingview.com/external-embedding"
chk(WS.count(TV) == 8, "WS: expected 8 TradingView scripts, got %d" % WS.count(TV))
for blk in ("ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"):
    chk(("embed-widget-%s.js" % blk) in WS, "WS missing widget block %s" % blk)
chk(WS.count("embed-widget-single-quote.js") == 3, "WS: need exactly 3 single-quote widgets")
for n in ("index.html", "cyber-briefing.html", "mma-briefing.html"):
    chk(TV not in PAGES[n], "%s must have zero TradingView widgets" % n)
for sym in ('FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y'):
    chk(sym in WS, "WS ticker missing required symbol %s" % sym)
chk('"symbol":"NYSE:HPE"' in WS, "WS Chart of the Day must be NYSE:HPE")
chk('class="livebar"' in WS, "WS missing livebar wrapper")

# ---- 4. markets arithmetic vs Thursday's verified closes
for close, chg, last, pct in ((7591.70, 80.64, 7672.34, 1.06),
                              (26081.72, 309.43, 26391.15, 1.19),
                              (52064.10, 579.62, 52643.72, 1.11)):
    chk(abs(close + chg - last) < 0.01, "level arithmetic %.2f+%.2f!=%.2f" % (close, chg, last))
    chk(abs(chg / close * 100 - pct) < 0.006, "pct arithmetic %.2f/%.2f != %.2f" % (chg, close, pct))
    chk(format(last, ",.2f") not in WS, "intraday level %.2f must not appear (levels belong only in the scorecard)" % last)

# ---- 5. Weekly Scorecard must hold ONLY official closes; no intraday level leaks in
i = WS.rfind("Weekly Scorecard"); j = WS.find("</table>", i)
sc = WS[i:j]
for lvl in ("7,672.34", "26,391.15", "52,643.72"):
    chk(lvl not in sc, "intraday level %s leaked into Weekly Scorecard" % lvl)
for lvl in ("7,591.70", "26,081.72", "52,064.10"):
    chk(lvl in sc, "Weekly Scorecard missing official close %s" % lvl)
    chk(WS.count(lvl) == 1, "official close %s should appear once, got %d" % (lvl, WS.count(lvl)))

# ---- 6. CVE / CVSS pairs read out of their own table rows
rows = re.findall(r"<tr>(.*?)</tr>", CY, re.S)
def cvss_of(cve):
    for r in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
        if len(cells) >= 2 and re.sub(r"<[^>]+>", "", cells[0]).strip() == cve:
            return re.sub(r"<[^>]+>", "", cells[1]).strip()
    return None
PAIRS = {"CVE-2026-86218":"10.0","CVE-2026-20079":"10.0","CVE-2026-49869":"10.0","CVE-2026-83548":"10.0",
         "CVE-2026-82329":"9.8","CVE-2026-9586":"9.3","CVE-2026-19490":"9.3","CVE-2026-59822":"8.8",
         "CVE-2026-42271":"8.7","CVE-2026-83549":"7.8","CVE-2025-25249":"7.3","CVE-2026-48710":"6.5"}
for cve, v in PAIRS.items():
    chk(cvss_of(cve) == v, "CVSS mismatch %s: row says %r, expected %s" % (cve, cvss_of(cve), v))
for cve in ("CVE-2026-81963","CVE-2026-85880","CVE-2026-69730","CVE-2026-69676","CVE-2026-87491","CVE-2026-20316","CVE-2025-14733"):
    chk(cvss_of(cve) == "not stated", "%s must carry 'not stated', got %r" % (cve, cvss_of(cve)))

# ---- 7. KEV deadlines consistent across Patch Priority, KEV list and countdowns
chk(CY.count("11 September 2026") >= 2, "N-able deadline must appear in both callout and KEV list")
chk("0 days left" in CY and "due today" in CY, "N-able countdown must read 0 days / due today")
chk("12 September 2026" in CY and "1 day left" in CY, "Cisco trio deadline/countdown missing")
chk("23 September 2026" in CY and "12 days left" in CY, "Chrome deadline/countdown missing")
chk("16 September 2026" in CY and "5 days left" in CY, "Starlette/LiteLLM deadline/countdown missing")
chk("BOD 26-04" in CY, "must cite risk-based BOD 26-04")
chk("three-week" not in CY and "BOD 22-01" not in CY, "flat three-week BOD 22-01 language must be absent")
chk("no deadline and no countdown are asserted" in CY, "MikroTik refusal must be explicit")
# refused/old stories must be absent
for bad in ("Nevada", "Novo Nordisk", "FulcrumSec"):
    chk(bad not in CY, "refused item '%s' must not appear on cyber page" % bad)

# ---- 8. champion regression guards
STALE = [("Pereira", "Light Heavyweight"), ("Chimaev", "Middleweight"), ("Topuria", "Lightweight"),
         ("Pantoja", "Flyweight"), ("Dvalishvili", "Bantamweight"), ("Shevchenko", "Women&rsquo;s Flyweight")]
crows = re.findall(r"<tr>(.*?)</tr>", MMA, re.S)
def champ_of(div):
    for r in crows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
        if len(cells) >= 2 and re.sub(r"<[^>]+>", "", cells[0]).strip() == div:
            return re.sub(r"<[^>]+>", "", cells[1]).strip()
    return None
POS = {"Heavyweight":"Tom Aspinall","Light Heavyweight":"Carlos Ulberg","Middleweight":"Sean Strickland",
       "Welterweight":"Islam Makhachev","Lightweight":"Justin Gaethje","Featherweight":"Alexander Volkanovski",
       "Bantamweight":"Petr Yan","Flyweight":"Joshua Van","Women&rsquo;s Flyweight":"VACANT",
       "Women&rsquo;s Bantamweight":"Kayla Harrison","Women&rsquo;s Strawweight":"Mackenzie Dern"}
for div, name in POS.items():
    chk(champ_of(div) == name, "champion row %s: got %r, expected %s" % (div, champ_of(div), name))
for name, div in STALE:
    chk(champ_of(div) != name, "STALE CHAMPION REGRESSION: %s seated at %s" % (name, div))
chk("Du Plessis" not in MMA and "Belal Muhammad" not in MMA and "Pe&ntilde;a" in MMA, "champion guard set")

# ---- 9. MMA specifics
chk('id="ufccdn"' in MMA and "2026-09-12T14:00:00-04:00" in MMA, "MMA countdown target missing")
chk("&minus;440" in MMA and "+340" in MMA and "DraftKings" in MMA, "odds must be printed with book named")
chk("TKO, Round 1, 2:25" in MMA, "Paris main event method must be UFC.com's 2:25")
chk("Salahdine Parnasse" in MMA and "Saladhine" not in MMA, "Parnasse spelling")
chk("Contender Series" in MMA and "Parnasse" in MMA, "context")
pi = MMA.find("Parnasse"); seg = MMA[:MMA.find("Prospect Watch")]
chk("Parnasse" not in MMA[MMA.find("Prospect Watch"):MMA.find("Around the Sport")], "Parnasse must not be a DWCS prospect card")
chk("$4,365,335" in MMA and "15,687" in MMA, "verified gate/attendance must appear")
chk("No viewership or TKO Group figure is published" in MMA, "must state absent figures")
chk(MMA.count("<tr>") >= 28, "MMA tables incomplete")

# ---- 10. index card sentences byte-identical to each page's own summary strip
def tldr_text(h):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', h, re.S)
    return m.group(1) if m else None
for label, pg in (("cyber", CY), ("ws", WS), ("mma", MMA)):
    t = tldr_text(pg)
    chk(t is not None, "%s tldr not parseable" % label)
    chk(t in IX, "index card sentence not byte-identical to %s summary strip" % label)

# ---- 11. no stale as-of / no closed-market claim while open
chk("2:18 PM ET" in WS, "WS must carry the as-of time")
chk("closed lower" not in WS and "finished lower" in WS, "no close asserted for an open session")
chk("no 11 September close is published" in WS, "must state no close published")

print("\nVALIDATION: %d checks, %d failures" % (ok + fail, fail))
sys.exit(1 if fail else 0)
