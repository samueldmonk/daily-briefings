# -*- coding: utf-8 -*-
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_1605 import S_CY, S_WS, S_MMA

OUT = os.path.dirname(os.path.abspath(__file__))
FAIL = []
N = [0]


def chk(cond, msg):
    N[0] += 1
    if not cond:
        FAIL.append(msg)


def rd(f):
    return io.open(os.path.join(OUT, f), encoding="utf-8").read()


PAGES = {f: rd(f) for f in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]}
CY, WS, MM, IX = PAGES["cyber-briefing.html"], PAGES["wallstreet-briefing.html"], PAGES["mma-briefing.html"], PAGES["index.html"]

# ---------- structural ----------
for f, h in PAGES.items():
    chk(h.startswith("<!DOCTYPE html>"), f + ": doctype")
    chk(h.count("</html>") == 1, f + ": one </html>")
    for tag in ["div", "p", "table", "thead", "tbody", "tr", "td", "th", "ul", "li", "span", "h2", "h3", "nav", "header", "script", "b", "a"]:
        o = len(re.findall(r"<%s[\s>]" % tag, h))
        c = h.count("</%s>" % tag)
        chk(o == c, "%s: <%s> %d open vs %d close" % (f, tag, o, c))
    # masthead + stamp
    for i in ["id=\"edition\"", "id=\"datestamp\"", "id=\"updated\"", "pill live", "freshline"]:
        chk(i in h, "%s: missing %s" % (f, i))
    chk("America/New_York" in h, f + ": stamp script")
    # five-tab nav, one active
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]:
        chk(('href="%s"' % href) in h, "%s: nav link %s" % (f, href))
    chk(h.count('class="active"') == 1, f + ": exactly one active tab")

# tldr strips on the three briefings only
for f in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    chk('class="tldr"' in PAGES[f], f + ": tldr strip")
chk('class="tldr"' not in IX, "index: no tldr strip (uses cards)")
chk("The Wire" in CY, "cyber: tldr label")
chk("The Tape" in WS, "ws: tldr label")
chk("Tale of the Tape" in MM, "mma: tldr label")

# ---------- index cards byte-identical to page summaries ----------
chk(S_CY in IX and S_CY in CY, "S_CY on index and cyber")
chk(S_WS in IX and S_WS in WS, "S_WS on index and ws")
chk(S_MMA in IX and S_MMA in MM, "S_MMA on index and mma")

# ---------- TradingView widgets: Wall Street only ----------
chk(WS.count("s3.tradingview.com") == 8, "ws: 8 tradingview scripts, got %d" % WS.count("s3.tradingview.com"))
for w in ["ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]:
    chk(("embed-widget-" + w) in WS, "ws: widget " + w)
chk(WS.count("embed-widget-single-quote") == 3, "ws: three single-quote widgets")
for f in ["index.html", "cyber-briefing.html", "mma-briefing.html"]:
    chk("tradingview" not in PAGES[f], f + ": no tradingview widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    chk(sym in WS, "ws: required ticker " + sym)
chk('"symbol":"NYSE:HPE"' in WS, "ws: chart of the day = HPE")
chk('class="livebar"' in WS and "LIVE QUOTES" in WS, "ws: livebar")
chk("Quotes stream live" in WS, "ws: note line")

# ---------- markets: no intraday levels on the page ----------
for lv in ["7,672", "26,391", "52,643", "7,671", "52,642", "26,423", "52,560", "80.64", "309.43", "579.62"]:
    chk(lv not in WS, "ws: intraday level %s must be absent" % lv)
# official closes exactly once, inside the scorecard
sc = WS[WS.index("Weekly Scorecard"):WS.index("Rates, Bonds")]
for lv in ["7,591.70", "26,081.72", "52,064.10", "&minus;44.66", "&minus;316.56"]:
    chk(WS.count(lv) == 1, "ws: %s appears once (got %d)" % (lv, WS.count(lv)))
    chk(lv in sc, "ws: %s inside scorecard slice" % lv)
# arithmetic reconciliation of Thursday's closes
chk(abs((44.66 / (7591.70 + 44.66)) * 100 - 0.5849) < 0.01, "ws: S&P pct reconciles")
chk(abs((316.56 / (52064.10 + 316.56)) * 100 - 0.6043) < 0.01, "ws: Dow pct reconciles")
# as-of stamp present
chk("2:18 PM ET" in WS, "ws: as-of time stated")
chk("527 points" in WS, "ws: CNBC point read")
# oil settlements consistent in card and table
chk(WS.count("$100.05") == 2 and WS.count("$104.61") == 2, "ws: oil settlements in card and table")
chk("nearly 10%" in WS and "8.6%" in WS, "ws: weekly oil moves")
# CPI figures
for v in ["0.4%", "3.4%", "0.3%", "2.4%"]:
    chk(v in WS, "ws: CPI component " + v)
chk("85.6%" in WS and "86%" in WS, "ws: both hike-probability reads")
# every curve tenor
for t in ["4.341%", "4.63%", "4.712%", "4.775%", "4.859%", "4.959%", "5.377%", "5.346%"]:
    chk(t in WS, "ws: tenor " + t)
chk(WS.count("52-week high") == 8, "ws: seven tenor flags plus the note, got %d" % WS.count("52-week high"))
# no unsourced Fed funds range
chk("3.50" not in WS and "3.75%" not in WS, "ws: no unverified fed funds range")
chk("not investment advice" in WS, "ws: disclaimer")

# ---------- cyber: CVE/CVSS pairs read from the FIRST cell of their row ----------
rows = re.findall(r"<tr><td><b>(CVE-[\d\-]+)</b></td><td>(.*?)</td>", CY)
pairs = dict(rows)
want = {
    "CVE-2026-20079": "10.0",
    "CVE-2026-19490": "9.3",
    "CVE-2025-25249": "7.3",
    "CVE-2026-59822": "8.8",
    "CVE-2026-48710": "6.5",
}
for cve, cvss in want.items():
    chk(pairs.get(cve) == cvss, "cyber: %s CVSS should be %s, table says %r" % (cve, cvss, pairs.get(cve)))
for cve in ["CVE-2026-85706", "CVE-2026-81963", "CVE-2026-85880", "CVE-2026-69414"]:
    chk("Not stated" in (pairs.get(cve) or ""), "cyber: %s must read Not stated" % cve)
chk(len(rows) == 9, "cyber: nine CVE rows, got %d" % len(rows))

# KEV deadline consistency across callout, list and countdown
chk(CY.count("12 September 2026") >= 3, "cyber: 12 Sept date in callout, list and top story")
chk("1 day left" in CY, "cyber: 1-day countdown")
chk("16 September 2026 &mdash; 5 days left" in CY, "cyber: 16 Sept = 5 days left")
chk("overdue by 6 days" in CY, "cyber: 5 Sept batch overdue by 6 days")
chk("BOD 26-04" in CY, "cyber: live directive named")
chk("22-01" not in CY, "cyber: retired directive not named")
chk("three-week" not in CY and "three weeks" not in CY, "cyber: retired flat window not referenced")
# threat level + stats strip
chk('class="banner"' in CY and "Threat level: High" in CY, "cyber: threat banner")
chk(CY.count('class="stat"') == 4, "cyber: four stat tiles")
chk('class="callout crit"' in CY, "cyber: patch priority is crit")
# refusals
chk("Nevada" in CY and "August 2025" in CY, "cyber: Nevada refusal stated in refusal paragraph")
chk("Novo Nordisk" not in CY, "cyber: Novo Nordisk absent")
# sourced numbers
for v in ["966", "974", "153 million", "4.1 million", "347,000", "2,500", "395", "178", "3,000 IP", "56 exploitation attempts"]:
    chk(v in CY, "cyber: figure " + v)
chk("UAT-12197" in CY and "UAT-11823" in CY and "UAT-11988" in CY, "cyber: three Cisco clusters")
chk(CY.count('class="t new">New</span>') == 5, "cyber: five New tags, got %d" % CY.count('class="t new">New</span>'))
chk(WS.count('class="t new">New</span>') == 1, "ws: one New tag, got %d" % WS.count('class="t new">New</span>'))
chk(MM.count('class="t new">New</span>') == 2, "mma: two New tags, got %d" % MM.count('class="t new">New</span>'))

# ---------- mma: champions, positive assertions ----------
CHAMPS_OK = [
    ("Heavyweight", "Tom Aspinall"), ("Light Heavyweight", "Carlos Ulberg"),
    ("Middleweight", "Sean Strickland"), ("Welterweight", "Islam Makhachev"),
    ("Lightweight", "Justin Gaethje"), ("Featherweight", "Alexander Volkanovski"),
    ("Bantamweight", "Petr Yan"), ("Flyweight", "Joshua Van"),
    ("Women&rsquo;s Bantamweight", "Kayla Harrison"), ("Women&rsquo;s Strawweight", "Mackenzie Dern"),
]
for div, name in CHAMPS_OK:
    chk(("<td><b>%s</b></td><td>%s</td>" % (div, name)) in MM, "mma: champion row %s = %s" % (div, name))
chk("<td><b>Women&rsquo;s Flyweight</b></td><td><span style=\"color:var(--warn)\">Vacant</span></td>" in MM,
    "mma: women's flyweight vacant")
chk("Ciryl Gane" in MM and "Interim heavyweight" in MM, "mma: interim HW Gane")
# stale-champion regression guards
for bad in ["Pereira</td>", "<td>Alex Pereira</td>", "<td>Khamzat Chimaev</td>",
            "Featherweight</b></td><td><span style=\"color:var(--warn)\">Vacant",
            "<td>Valentina Shevchenko</td>", "<td>Ilia Topuria</td>", "<td>Merab Dvalishvili</td>"]:
    chk(bad not in MM, "mma: stale champion regression %r" % bad)
chk("Shevchenko is NO LONGER" not in MM, "mma: no correction-file phrasing leaked")
chk("vacated" in MM and "stripped" not in MM, "mma: vacated wording, never stripped")
# odds
chk("&minus;430" in MM and "+320" in MM and "FanDuel" in MM, "mma: sourced odds with book")
chk(MM.count("FanDuel") >= 1, "mma: book named")
# no unsourced odds for UFC 331
u331 = MM[MM.index("UFC 331:"):MM.index("UFC 332:")]
chk("Odds:" not in u331, "mma: no invented UFC 331 moneyline")
# countdown
chk('id="ufccdn"' in MM and "2026-09-12T14:00:00-04:00" in MM, "mma: countdown to Saturday")
chk("Fight week" in MM, "mma: countdown elapsed branch")
# results table
chk(MM.count('<td class="up"><b>') == 6, "mma: six result rows")
chk("TKO, Round 1, 2:25" in MM, "mma: Parnasse method and time from UFC.com")
chk("2:35" not in MM, "mma: superseded 2:35 time absent")
chk("four Performance of the Night awards and no" in MM, "mma: bonus structure")
chk("$100,000" in MM, "mma: only the sourced Salkilld bonus figure")
chk("Contender Series" in MM and "Parnasse" in MM, "mma: both present")
# Parnasse must never be attributed to the Contender Series
seg = MM[MM.index("Parnasse arrived exactly as advertised"):]
seg = seg[:seg.index("</li>")]
chk("Contender Series" not in seg, "mma: Parnasse not tied to Contender Series")
chk("KSW" in MM, "mma: Parnasse KSW pedigree")
# Dariush descriptor guard
chk("Dariush" not in MM or "challenger" not in MM, "mma: no Dariush title-challenger claim")
# business figures
chk("$4,365,335" in MM and "15,687" in MM, "mma: sourced UFC Paris business figures")
chk("13" in MM and "thirteen-bout" in MM, "mma: card size")
chk(MM.count('<tr><td><b>') >= 13, "mma: weigh-in + champions rows")
chk("subject to change" in MM, "mma: disclaimer")
chk("Waldo Cortes Acosta" in MM and "Cortes-Acosta" not in MM, "mma: primary-source name rendering")
chk("Salahdine Parnasse" in MM and "Saladhine" not in MM, "mma: Parnasse spelling")
chk("Quillan Salkilld" in MM and "Cody Salkilld" not in MM, "mma: Salkilld spelling")
chk("Mateusz Gamrot" in MM, "mma: Salkilld latest opponent, not an older one")

# dates chronological / nothing 'upcoming' that has passed
chk(MM.index("12 September") < MM.index("19 September"), "mma: cards in date order")
chk(MM.index("19 September") < MM.index("3 October"), "mma: cards in date order 2")
chk(MM.index("3 October") < MM.index("24 October"), "mma: cards in date order 3")

print("checks: %d   failures: %d" % (N[0], len(FAIL)))
for f in FAIL:
    print("  FAIL:", f)
sys.exit(1 if FAIL else 0)
