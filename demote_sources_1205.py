import io, re
D = "/sessions/beautiful-zealous-mendel/mnt/outputs/"
PAGES = ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]

# --- demote every stale edition stamp to "Carried" ---
for p in PAGES:
    s = io.open(D + p, encoding="utf-8").read()
    before = s
    s = re.sub(r'<span class="tag new">(?:New|Updated) · (?!12:05)[^<]*</span>', '<span class="tag">Carried</span>', s)
    io.open(D + p, "w", encoding="utf-8").write(s)
    print(p, "demoted:", before.count('tag new') - s.count('tag new'), "| live 12:05 tags:", s.count('tag new'))

# --- add this run's source URLs ---
def append_sources(page, items):
    s = io.open(D + page, encoding="utf-8").read()
    anchor = '<footer><b style="color:var(--ink)">Sources</b><ul class="bul">'
    assert s.count(anchor) == 1, page
    s = s.replace(anchor, anchor + "".join(items))
    io.open(D + page, "w", encoding="utf-8").write(s)
    print(page, "appended", len(items), "sources")

append_sources("wallstreet-briefing.html", [
 '<li><b>Fetched 12:05 PM ET</b> — Yahoo Finance, <a href="https://finance.yahoo.com/markets/live/stock-market-today-thursday-august-27-dow-sp-500-nasdaq-082144520.html">Stock market today: S&amp;P 500, Nasdaq rise as Nvidia, Salesforce earnings boost tech (Aug 27, 2026 live blog)</a> — S&amp;P 500 +0.4%, Nasdaq ~+1%, CRM +11.2%, CRWD +9.4%, NVDA +6%.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — Benzinga, <a href="https://www.benzinga.com/markets/equities/26/08/61454942/stock-market-today-sp-500-nasdaq-100-futures-gain-while-dow-slips-following-nvda-blockbuster-q2-report-crm-crwd-hpq-in-focus">Stock Market Today (Aug 27, 2026)</a> — Dow +147.67 (+0.28%), Nasdaq +279.61 (+1.07%), Russell 2000 +7.64 (+0.25%); 10-yr 4.66%, 2-yr 4.22%; CME FedWatch 36.1% September hike probability; ARM +6.2% at $266.50; ZS +8.7%; PLTR +3.8% at $184.32.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — Yahoo Finance, <a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-today-aug-27-144318504.html">Stock Market Today (Aug. 27, 2026): S&amp;P 500 climbs after Nvidia earnings beat</a> — jobless claims 203,000.</li>',
])

append_sources("cyber-briefing.html", [
 '<li><b>Fetched 12:05 PM ET</b> — SecurityWeek, <a href="https://www.securityweek.com/recent-citrix-netscaler-vulnerability-exploited-in-the-wild/">Recent Citrix NetScaler Vulnerability Exploited in the Wild</a> — CVE-2026-8452 assigned CVSS 8.8 by Citrix; x.php / z.php web shells; KEV due Aug 29.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — Rapid7, <a href="https://www.rapid7.com/blog/post/etr-cve-2026-19490-critical-vulnerability-affecting-citrix-netscaler-adc-and-netscaler-gateway/">CVE-2026-19490: Critical Vulnerability Affecting Citrix NetScaler ADC and NetScaler Gateway</a> — CVSS v4.0 9.3 authentication bypass, advisory Aug 19, 2026, no observed exploitation as of Aug 19.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — The Hacker News, <a href="https://thehackernews.com/2026/08/critical-netscaler-flaw-can-bypass.html">Critical NetScaler Flaw Can Bypass Authentication on Certain Gateway and AAA Servers</a>.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — GBHackers, <a href="https://gbhackers.com/ransomware-hacker-uses-ai/">Ransomware Hacker Uses AI to Plan Attacks and Compromises More Than 20 Organizations</a> — Aurora affiliate, nine countries, April–July 2026, Cursor chat logs, domain access in ≥17 environments, four victims on the leak site.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — CISA, <a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA Adds Six Known Exploited Vulnerabilities to Catalog (Aug 26, 2026)</a>.</li>',
])

append_sources("mma-briefing.html", [
 '<li><b>Fetched 12:05 PM ET</b> — MMAOddsBreaker, <a href="https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161241-opening-betting-odds-for-ufc-shanghai-nurmagomedov-vs-song/">Opening Betting Odds for UFC Shanghai: Nurmagomedov vs. Song</a> — Nurmagomedov −500 / Song +385 opening line.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — Yahoo Sports, <a href="https://sports.yahoo.com/articles/latest-ufc-shanghai-fight-card-133000784.html">Latest UFC Shanghai fight card, Paramount+ start time, date and location</a> — main card: Yan vs. Gomes, Qileng Aori vs. Kai Asakura, Alex Perez vs. Su Mudaerji rematch.</li>',
 '<li><b>Fetched 12:05 PM ET</b> — ESPN, <a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">Current and all-time UFC champions</a> — queried this run; the returned summary was stale on three belts and was rejected (see the Champions Board note).</li>',
])
print("done")
