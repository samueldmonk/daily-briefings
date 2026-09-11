import io, re
D = "/sessions/fervent-serene-bohr/mnt/outputs/"

# --- Wall Street sources footer additions ---
P = D + "wallstreet-briefing.html"
s = io.open(P, encoding="utf-8").read()
old = '    <div class="srcline"><b>Sources read this run</b></div>'
assert s.count(old) == 1
s = s.replace(old, old + """
    <div class="srcline">CNBC — Stock market news for Sept. 11, 2026 — <a href="https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html">https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html</a></div>
    <div class="srcline">Yahoo Finance — Dow, S&amp;P 500, Nasdaq end losing week on a high note as Fed rate-hike bets jump — <a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-september-11-dow-sp-500-nasdaq-cpi-inflation-082201751.html">https://finance.yahoo.com/markets/live/stock-market-today-friday-september-11-dow-sp-500-nasdaq-cpi-inflation-082201751.html</a></div>
    <div class="srcline">TheStreet — Stock Market Today (Sept. 11, 2026) — <a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-11-2026">https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-11-2026</a></div>
    <div class="srcline">WTOP — How major US stock indexes fared Friday 9/11/2026 — <a href="https://wtop.com/national/2026/09/how-major-us-stock-indexes-fared-friday-9-11-2026">https://wtop.com/national/2026/09/how-major-us-stock-indexes-fared-friday-9-11-2026</a></div>
    <div class="srcline">Investrade — Market Review: September 11, 2026 — <a href="https://investrade.com/market-review-september-11-2026/">https://investrade.com/market-review-september-11-2026/</a></div>
    <div class="srcline">The Motley Fool — Stock Market Today, Sept. 11: HPE Surges on AI Infrastructure Demand — <a href="https://www.fool.com/coverage/stock-market-today/2026/09/11/stock-market-today-sept-11-hpe-surges-on-ai-infrastructure-demand-and-recently-raised-guidance/">https://www.fool.com/coverage/stock-market-today/2026/09/11/stock-market-today-sept-11-hpe-surges-on-ai-infrastructure-demand-and-recently-raised-guidance/</a></div>
    <div class="srcline">Yahoo Finance — Copart to Acquire ACV, Expanding Position Across the Vehicle Remarketing Ecosystem — <a href="https://finance.yahoo.com/markets/stocks/articles/copart-acquire-acv-expanding-position-201600988.html">https://finance.yahoo.com/markets/stocks/articles/copart-acquire-acv-expanding-position-201600988.html</a></div>
    <div class="srcline">Trading Economics — US 10-Year Treasury Note Yield — <a href="https://tradingeconomics.com/united-states/government-bond-yield">https://tradingeconomics.com/united-states/government-bond-yield</a></div>""")
io.open(P, "w", encoding="utf-8").write(s)

# --- pull each page's summary sentence and mirror it byte-identically onto index.html ---
def tldr(fn):
    t = io.open(D + fn, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', t, re.S)
    assert m, "no tldr in " + fn
    return m.group(1)

cy, ws, mm = tldr("cyber-briefing.html"), tldr("wallstreet-briefing.html"), tldr("mma-briefing.html")

P = D + "index.html"
s = io.open(P, encoding="utf-8").read()
cards = re.findall(r'(<div class="bcard (?:cy|mk|mm)">.*?<p>)(.*?)(</p>)', s, re.S)
assert len(cards) == 3, len(cards)
for (pre, body, post), new in zip(cards, (cy, ws, mm)):
    s = s.replace(pre + body + post, pre + new + post, 1)
io.open(P, "w", encoding="utf-8").write(s)
print("index cards synced; lengths:", len(cy), len(ws), len(mm))
