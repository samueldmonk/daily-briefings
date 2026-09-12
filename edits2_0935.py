#!/usr/bin/env python3
"""Second pass: MMA business block, Wall Street Adobe + Brent second read,
index.html card sentences resynced byte-for-byte to each page's summary strip."""
import io, os, re, sys
O = sys.argv[1]

def load(n): return io.open(os.path.join(O, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(O, n), "w", encoding="utf-8").write(s)

N = 0
def rep(s, old, new, count=1, label=""):
    global N
    assert s.count(old) == count, "ANCHOR MISS (%d/%d): %s | %.90s" % (s.count(old), count, label, old)
    N += count
    return s.replace(old, new)

# ── MMA: broadcast economics, all figures from TKO / Variety / ESPN reads this run ──
mm = load("mma-briefing.html")
mm = rep(mm,
  "Per UFC.com’s own bonus page: gross revenue <b>$4,365,335</b> from an attendance of <b>15,687</b>, a sell-out and the <b>highest-grossing event in Accor Arena history</b>.",
  "Per UFC.com’s own bonus page: gross revenue <b>$4,365,335</b> from an attendance of <b>15,687</b>, a sell-out and the <b>highest-grossing event in Accor Arena history</b>.</p>"
  "<p>Tonight’s card streams under the first year of Paramount’s <b>seven-year, $7.7 billion</b> rights deal with TKO Group, and the audience figures behind that deal were re-read this run. Paramount+ says <b>16 million subscriber households</b> have watched more than <b>180 million hours</b> of UFC programming since the start of the year, and that viewership runs as much as <b>20 times</b> the pay-per-view average of the previous two years. The first card under the deal, <b>UFC 324</b>, drew <b>4.96 million</b> views; <b>UFC Freedom 250</b> averaged <b>8.2 million</b> and reached an estimated <b>34 million total global viewers</b>, with <b>17 million</b> on Paramount+ across the US and Latin America. TKO posted first-quarter revenue of <b>$1.6 billion</b>, up 26%, with net income of <b>$250 million</b> and adjusted EBITDA of <b>$550 million</b>, up 32%. The partnership extends to <b>Canada from 2027</b>.",
  label="mma business")

mm = rep(mm,
  "<li><a href=\"https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse\">",
  "<li><a href=\"https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse\">",
  count=mm.count("<li><a href=\"https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse\">"),
  label="mma paris source present check") if "ufc-paris-results-hooker-vs-parnasse" in mm else mm

mm = rep(mm, "<footer><h4>Sources</h4><ul>",
  "<footer><h4>Sources</h4><ul>"
  "<li><a href=\"https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse\">UFC.com — Main Card Results | UFC Paris (official methods, rounds and times)</a></li>"
  "<li><a href=\"https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx\">TKO Group Holdings — UFC Freedom 250 Delivers 34 Million Total Global Viewers</a></li>"
  "<li><a href=\"https://variety.com/2026/tv/news/ufc-324-ratings-paramountplus-1236641402/\">Variety — UFC 324 Draws 4.96 Million Views in Paramount+ Debut</a></li>"
  "<li><a href=\"https://variety.com/2026/tv/news/ufc-freedom-250-ratings-1236785493/\">Variety — ‘UFC Freedom 250’ Ratings: 8.2 Million Average Viewers</a></li>"
  "<li><a href=\"https://www.hollywoodreporter.com/business/business-news/tko-earnings-rise-paramount-ufc-deal-1236588117/\">The Hollywood Reporter — TKO Earnings and Income Rise as Paramount UFC Deal Kicks Into Gear</a></li>"
  "<li><a href=\"https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card\">Al Jazeera — UFC 331: Van-Pantoja rematch, Tsarukyan returns and full fight card</a></li>",
  label="mma sources")

# The official UFC.com page gives 2:25; a Yahoo/CBS read gives 2:35. Disclose rather than pick silently.
mm = rep(mm,
  "Stopped <b>Dan Hooker by TKO at 2:25 of round one</b> in the Paris main event",
  "Stopped <b>Dan Hooker by TKO at 2:25 of round one</b> in the Paris main event — UFC.com’s official main-card results page gives 2:25, while a wire read this run gives 2:35, and the official figure is the one carried",
  label="mma parnasse time disclosure")
save("mma-briefing.html", mm)

# ── WALL STREET: Adobe, and a second Brent read ──
ws = load("wallstreet-briefing.html")
ws = rep(ws,
  "<h2 class=\"sec\">Chart of the Day",
  "<h2 class=\"sec\">Adobe, the other side of the earnings tape</h2><div class=\"panel\"><p>Not every reporter was rewarded. <b>Adobe (NASDAQ:ADBE)</b> <b>slid 2%</b> after issuing current-quarter guidance that a movers roundup read this run describes as roughly in line with estimates — the same session in which Oracle’s beat carried its suppliers to records. Also named among the day’s biggest movers, without figures attached in the read: <b>KR</b>, <b>CPRT</b>, <b>EXEL</b>, <b>ZUMZ</b> and <b>CHWY</b>.</p></div><h2 class=\"sec\">Chart of the Day",
  label="ws adobe")
ws = rep(ws,
  "<footer><h4>Sources</h4><ul>",
  "<footer><h4>Sources</h4><ul>"
  "<li><a href=\"https://seekingalpha.com/news/4641936-biggest-stock-movers-friday\">Seeking Alpha — Biggest stock movers Friday: ORCL, ACVA, KR, and more</a></li>"
  "<li><a href=\"https://www.etftrends.com/fixed-income-content-hub/treasury-yields-snapshot-september-11-2026/\">ETF Trends — Treasury Yields Snapshot: September 11, 2026</a></li>"
  "<li><a href=\"https://investrade.com/market-review-september-11-2026/\">Investrade — Market Review: September 11, 2026 (sector breadth)</a></li>"
  "<li><a href=\"https://www.ig.com/en-ch/news-and-trade-ideas/week-ahead--14-september-2026-260911\">IG — Week Ahead: 14 September 2026</a></li>"
  "<li><a href=\"https://tradingeconomics.com/commodity/brent-crude-oil\">Trading Economics — Brent crude oil (second read on Friday’s settle)</a></li>",
  label="ws sources")
save("wallstreet-briefing.html", ws)

# ── INDEX: card sentences must be byte-identical to each briefing's own summary strip ──
def tldr(page):
    s = load(page)
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', s, re.S)
    assert m, "no tldr in " + page
    return m.group(1).strip()

cy_s, ws_s, mm_s = tldr("cyber-briefing.html"), tldr("wallstreet-briefing.html"), tldr("mma-briefing.html")
ix = load("index.html")
cards = re.findall(r'<p class="cardsum">(.*?)</p>', ix, re.S)
assert len(cards) == 3, "expected 3 index cards, got %d" % len(cards)
for old, new in zip(cards, [cy_s, ws_s, mm_s]):
    if old.strip() != new:
        ix = ix.replace('<p class="cardsum">%s</p>' % old, '<p class="cardsum">%s</p>' % new, 1)
        N += 1
save("index.html", ix)

# Verify the sync held.
ix2 = load("index.html")
c2 = [c.strip() for c in re.findall(r'<p class="cardsum">(.*?)</p>', ix2, re.S)]
assert c2 == [cy_s, ws_s, mm_s], "index cards NOT byte-identical to page summaries"
print("OK  replacements=%d  index cards synced" % N)
