# -*- coding: utf-8 -*-
"""Daily Briefings build - Friday September 4 2026, Morning Edition (pre-open)."""
import sys, os
sys.path.insert(0, os.environ.get("REPO", "."))
from shared import css, nav, META, STAMP, page, sources

OUT = os.environ.get("OUTDIR", ".")

TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:LULU","title":"Lululemon"},{"proName":"NASDAQ:SNOW","title":"Snowflake"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},{"proName":"NASDAQ:DDOG","title":"Datadog"},{"proName":"NASDAQ:HOOD","title":"Robinhood"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""

def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/'
            'embed-widget-single-quote.js" async>{"symbol":"%s","width":"100%%",'
            '"colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)

QUOTES = ('<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD")
          + quote("FOREXCOM:DJI") + '</div>'
          '<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below '
          'reflects the latest edition; official closes are in the Weekly Scorecard.</div>')

TIMELINE = """<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script>
</div>"""

HEATMAP = """<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>
</div>"""

CHART = """<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NASDAQ:LULU","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>"""

EVENTS = """<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script>
</div>"""


# ---------------------------------------------------------------- WALL STREET
WS_SRC = [
 ("TheStreet - Stock Market Today (Sept. 4, 2026): Nasdaq futures edge higher", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-04-2026"),
 ("Reuters via Investing.com - Nasdaq, S&P 500 futures climb ahead of key jobs report", "https://www.investing.com/news/economy-news/nasdaq-sp-500-futures-climb-ahead-of-key-jobs-report-4889040"),
 ("CNBC - August 2026 jobs report: payrolls projected up 53,000", "https://www.cnbc.com/2026/09/03/august-2026-jobs-report-payrolls.html"),
 ("CNBC - Trading the August jobs report: what could affect the number", "https://www.cnbc.com/2026/09/03/trading-jobs-report-what-could-turn-the-number-how-investors-may-respond.html"),
 ("CNN - What to expect from the jobs report today", "https://www.cnn.com/2026/09/04/economy/us-jobs-report-august"),
 ("Benzinga - August jobs report preview: what makes a Fed hike a lock", "https://www.benzinga.com/markets/economic-data/26/09/61615137/august-jobs-report-preview-fed-rate-hike-september-2026"),
 ("Yahoo Finance - Dow, S&P 500 post best day in a month (Sept 3)", "https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-3-dow-sp-500-nasdaq-futures-081525933.html"),
 ("CNBC - Stock market on Sept. 3, 2026", "https://www.cnbc.com/2026/09/02/stock-market-today-live-updates.html"),
 ("CNBC - Lululemon stock plunges on disappointing earnings and outlook", "https://www.cnbc.com/2026/09/03/lululemon-lulu-q2-2026-earnings.html"),
 ("Investing.com - Lululemon Q2 2026 presentation: revenue drops 4%", "https://www.investing.com/news/company-news/lululemon-q2-2026-presentation-revenue-drops-4-stock-plunges-18-93CH-4888642"),
 ("StockAnalysis - Today's premarket stock movers", "https://stockanalysis.com/markets/premarket/"),
 ("Trading Economics - US 10-year Treasury note yield", "https://tradingeconomics.com/united-states/government-bond-yield"),
 ("Fortune - Current price of oil as of September 3, 2026", "https://fortune.com/article/price-of-oil-09-03-2026/"),
 ("Vantage Markets - Brent steadies near $96 as Iran strikes, OPEC+ hikes", "https://www.vantagemarkets.com/market-analysis/brent-wti-crude-oil-price-september-3-2026/"),
 ("Chase - Will the Fed hike rates in September?", "https://www.chase.com/personal/investments/learning-and-insights/article/september-2026-rate-hike-now-expected-amid-energy-shocks"),
]

ws_body = f"""<header class="mast">
<h1 style="font-family:Georgia,'Times New Roman',serif">The Closing Bell</h1>
<p class="tag">Your daily Wall Street briefing &mdash; the tape, the movers and what sets tomorrow</p>
{META}
</header>
<div class="tldr"><b>The Tape</b> <span>Futures are steady to modestly higher before the August
jobs report at 8:30 AM ET &mdash; the print that decides a Fed split 50-50 into the Sept 15&ndash;16
meeting &mdash; after Thursday's Waller-driven rally handed the Dow its best day since Aug 4.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("ws", "")}
{TICKER}
<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>
{QUOTES}

<h2 class="sec">The Lead</h2>
<div class="lead">
<h3 style="font-family:Georgia,'Times New Roman',serif">Before the open: the August jobs report is the
entire session</h3>
<p>The Bureau of Labor Statistics releases the August employment report at <b>8:30 AM ET</b>, an hour
before the opening bell, and it is the one number that matters today. <b>This page does not publish an
August payrolls figure.</b> At the time this edition's sources were fetched the report had not yet
printed, and every source reviewed was still a preview &mdash; so the actual result is deliberately
absent rather than guessed.</p>
<p>What the previews say, and they do not agree: economists polled by <b>Dow Jones expect +53,000</b>
with the unemployment rate at <b>4.1%</b> (CNBC); TheStreet cites a consensus nearer <b>+55,000</b>,
also at 4.1%; other economists look for <b>+65,000</b> and a rate ticking up to <b>4.2%</b>; another
read puts growth near <b>+45,000</b>. The tails are wide &mdash; <b>Oxford Economics at +95,000</b>,
<b>Bank of America at +40,000</b>. July was a <b>23,000-job decline</b>.</p>
<p>JPMorgan's trading desk mapped the reaction in advance: above <b>+95,000</b>, the S&amp;P 500 falls
0.5% to 1.25%; <b>+65,000 to +95,000</b>, down 0.25% to 0.5%; <b>+35,000 to +65,000</b>, anywhere from
&minus;0.25% to +0.5%; <b>+5,000 to +35,000</b>, up 0.25% to 0.75%. Fed funds futures are split
<b>50-50</b> going in, with the FOMC meeting <b>September 15&ndash;16</b>.</p>
<p>Futures at <b>4:24 AM ET</b>: Dow E-minis <span class="down">&minus;40 pts (&minus;0.07%)</span>,
S&amp;P 500 E-minis <span class="up">+4.75 (+0.06%)</span>, Nasdaq 100 E-minis
<span class="up">+124.25 (+0.42%)</span> (Reuters).</p>
<p>That follows a strong Thursday. The S&amp;P 500 rose <span class="up">1.06% to 7,747.71</span>, the
Nasdaq Composite <span class="up">about 1.4% to 26,584.06</span> and the Dow
<span class="up">624.16 points, or 1.18%, to 53,686.11</span> &mdash; its best day since <b>Aug 4</b>.
The trigger was Fed governor <b>Christopher Waller</b> saying pricing pressures showed signs of
improving and signalling he would support holding rates steady this month absent an inflation
surprise; Treasury yields eased off their highs and beaten-down growth stocks caught a bid.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">
<div class="card"><div class="tags"><span class="t new">New</span><span class="t crit">Guidance cut</span></div>
<h3>Lululemon &mdash; the day's biggest single-name break</h3>
<p>CNBC reported the stock <span class="down">plunged 15%</span> on disappointing earnings and outlook;
Investing.com's write-up of the same results says <span class="down">18%</span> after hours, and
StockAnalysis had it at <span class="down">&minus;18.9%</span> in Friday premarket. Those readings are
printed as reported and are <b>not merged</b>. Q2 revenue <b>$2.415B, down 4%</b> against $2.461B
expected, comparable sales <b>&minus;9%</b>; North America revenue <b>&minus;8%</b> with comps
<b>&minus;12%</b>. Full-year revenue guidance cut to <b>$10.35&ndash;10.5B</b> (a 5&ndash;7% decline)
from <b>$11&ndash;11.15B</b>. Interim CEO <b>Meghan Frank</b> cited "negative commentary" on social
media and a greater-than-expected slowdown in core categories including leggings.</p></div>

<div class="card"><div class="tags"><span class="t ok">Beat</span></div>
<h3>Snowflake &mdash; up more than 16%</h3>
<p>Shares popped <span class="up">more than 16%</span> Thursday after better-than-expected
second-quarter earnings and revenue, plus strong guidance (CNBC).</p></div>

<div class="card"><div class="tags"><span class="t ok">Momentum</span></div>
<h3>Robinhood &mdash; about 11%</h3>
<p>Jumped <span class="up">about 11%</span> Thursday, putting the stock on pace for its best day since
<b>Aug 21</b> (CNBC).</p></div>

<div class="card"><div class="tags"><span class="t warn">Soft guide</span></div>
<h3>Broadcom &mdash; down nearly 3%</h3>
<p>Fell <span class="down">nearly 3%</span> following its latest quarterly results after offering a
disappointing revenue forecast for the fiscal fourth quarter (CNBC).</p></div>

<div class="card"><div class="tags"><span class="t new">New</span></div>
<h3>Premarket gainers: Samsara and Datadog</h3>
<p>In Friday premarket trading <b>Samsara</b> was <span class="up">+14.09%</span> and <b>Datadog</b>
<span class="up">+6.08% to $221.96</span>; among S&amp;P 500 names Principal Financial was
<span class="up">+4.25% to $116.04</span> and ServiceNow <span class="up">+3.33%</span>
(StockAnalysis premarket screen).</p></div>

<div class="card"><div class="tags"><span class="t new">New</span><span class="t crit">Margin</span></div>
<h3>Asana &mdash; down 11.5% premarket</h3>
<p><span class="down">&minus;11.5%</span> in Friday premarket as margin pressure offset an earnings
beat (StockAnalysis).</p></div>
</div>

<h2 class="sec">Chart of the Day &mdash; Lululemon (LULU)</h2>
{CHART}
<div class="note">The session's largest single-name move. Intraday chart streams live; the figures in
the card above are as reported by the named outlets.</div>

<h2 class="sec">Sector Heat &mdash; live</h2>
{HEATMAP}
<div class="note">Editorial, sourced: <b>technology stocks led Thursday's advance</b>, helped by falling
bond yields (CNBC). No sector-by-sector percentage table is published this edition &mdash; no source
fetched this run gave one for Thursday's close that reconciled.</div>

<h2 class="sec">The Calendar &mdash; live</h2>
{EVENTS}

<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>
{TIMELINE}

<h2 class="sec">Weekly Scorecard</h2>
<div class="panel" style="padding:5px 7px">
<table>
<tr><th>Index</th><th>Thu Sept 3 close</th><th>Session</th><th>Week to date</th><th>Wed Sept 2 close</th></tr>
<tr><td>S&amp;P 500</td><td class="mono">7,747.71</td><td class="up">+1.06%</td><td class="up">+0.5%</td><td class="mono">7,666.60</td></tr>
<tr><td>Nasdaq Composite</td><td class="mono">26,584.06</td><td class="up">about +1.4%</td><td class="up">+0.7%</td><td class="mono">26,217.83</td></tr>
<tr><td>Dow Jones Industrial Average</td><td class="mono">53,686.11</td><td class="up">+624.16 / +1.18%</td><td class="up">+0.2%</td><td class="mono">53,061.95</td></tr>
</table>
</div>
<div class="note">Official closes only. Week-to-date figures are as reported ahead of Friday's open and
exclude today's session. Arithmetic check: 53,686.11 &minus; 624.16 = 53,061.95, matching Wednesday's
close.</div>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel" style="padding:5px 7px">
<table>
<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>
<tr><td>10-year Treasury</td><td class="mono">4.76%</td><td>Trading Economics, Sept 3. The yield rose past 4.8% in September, its highest since October 2023; it stood at 4.79% on Sept 2.</td></tr>
<tr><td>30-year Treasury</td><td class="mono">5.25%</td><td>Curve snapshot, Trading Economics</td></tr>
<tr><td>2-year Treasury</td><td class="mono">4.35%</td><td>Curve snapshot; 5-year 4.52%, 1-year 4.11%</td></tr>
<tr><td>Fed funds</td><td class="mono">FOMC Sept 15&ndash;16</td><td>Futures split 50-50 between a 25 bp hike and no move; strategists at Chase now expect a 0.25 pt hike as Iran-related supply shocks keep energy costs high</td></tr>
<tr><td>WTI crude</td><td class="mono">$92.90</td><td><span class="up">+2.1%</span> Sept 3 (Fortune/Yahoo). A prior verified reading for the same session was $92.30, +$1.29 / +1.42% &mdash; both are printed, neither is adopted.</td></tr>
<tr><td>Brent crude</td><td class="mono">$95.82</td><td>Sept 3 close</td></tr>
</table>
</div>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><b>August employment report &mdash; 8:30 AM ET today.</b> The single event of the session. Fed
funds futures went in split 50-50; the print is widely described as what makes a September hike a
lock or takes it off the table.</li>
<li><b>FOMC, September 15&ndash;16.</b> Waller's remarks Thursday leaned toward holding; Chase's
strategists have moved to expecting a 25 bp <i>hike</i>, a shift from a prior base case of no rate
change in 2026.</li>
<li><b>Oil supply risk.</b> Thursday's crude gain followed projectile strikes on two oil supertankers
exiting the <b>Strait of Hormuz</b>, reigniting supply-disruption fears. Brent has been steadying
near $96.</li>
</ul>
</div>
"""

ws = page("The Closing Bell &mdash; Daily Briefings", "#caa64a", "#e8c766", "#0f0e0b",
          "#191712", "#2b2820", ws_body + sources(WS_SRC) +
          '<div class="disc">For information only. Nothing here is investment advice, a '
          'recommendation, or an offer to buy or sell any security.</div></footer>',
          extra_css=".mast h1,.lead h3{letter-spacing:-.01em}")
open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(ws)


# ---------------------------------------------------------------------- CYBER
CY_SRC = [
 ("BleepingComputer - Critical Langflow flaw exploited to steal OpenAI and AWS keys", "https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/"),
 ("Qualys ThreatPROTECT - Langflow RCE exploited in attacks (CVE-2026-0768)", "https://threatprotect.qualys.com/2026/09/02/langflow-remote-code-execution-vulnerability-exploited-in-attacks-cve-2026-0768/"),
 ("SecurityAffairs - Hackers target Langflow in CVE-2026-0768 attacks", "https://securityaffairs.com/198270/hacking/hackers-target-langflow-in-cve-2026-0768-attacks.html"),
 ("CISA - Adds seven Known Exploited Vulnerabilities to catalog (Sept 2, 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("CISA - Known Exploited Vulnerabilities Catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("Rapid7 - Critical SonicWall SMA1000 vulnerabilities exploited in the wild", "https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild/"),
 ("SOCRadar - JFrog Artifactory CVE-2026-82329 exploited", "https://socradar.io/blog/jfrog-artifactory-cve-2026-82329/"),
 ("The Hacker News - CISA adds seven exploited flaws as attackers deploy reverse shells", "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
 ("The Hacker News - Google releases Chrome update to patch actively exploited V8 zero-day", "https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html"),
 ("SecurityAffairs - Google fixes the sixth actively exploited Chrome zero-day of 2026", "https://securityaffairs.com/198405/security/google-fixes-the-sixth-actively-exploited-chrome-zero-day-of-2026/"),
 ("CybersecurityNews - Critical HPE Fabric Composer flaws let unauthenticated attackers execute code", "https://cybersecuritynews.com/hpe-fabric-composer-flaws/"),
 ("SOC Prime - CVE-2026-76658: critical HPE Fabric Composer flaw", "https://socprime.com/blog/cve-2026-76658-analysis/"),
 ("SecurityWeek - Manchester Airports Group data on 8.8 million people leaked after ransom refusal", "https://www.securityweek.com/manchester-airports-group-data-on-8-8-million-people-leaked-after-ransom-refusal/"),
 ("BleepingComputer - FulcrumSec claims Manchester Airports hack, theft of 86 GB of data", "https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/"),
 ("Searchlight Cyber - FulcrumSec claims responsibility for Manchester Airport Group breach", "https://www.slcyber.io/blog/beacon-fulcrumsec-claims-responsibility-for-manchester-airport-group-breach"),
 ("ITPro - Manchester Airports Group attack: everything we know so far", "https://www.itpro.com/security/cyber-attacks/manchester-airports-group-attack-everything-we-know-so-far-as-8-7-million-customers-impacted-in-breach"),
 ("BrightDefense - List of recent data breaches in 2026", "https://www.brightdefense.com/resources/recent-data-breaches/"),
]

cy_body = f"""<header class="mast">
<h1>The Cyber Wire</h1>
<p class="tag">Your daily cybersecurity briefing &mdash; breaches, bugs and the patch clock</p>
{META}
</header>
<div class="tldr"><b>The Wire</b> <span>A federal patch deadline for five actively exploited flaws
lands <b>tomorrow</b>, while attackers keep hammering Langflow's unauthenticated root RCE to strip
OpenAI and AWS keys out of environment variables.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("cyber", "")}

<div class="banner"><span class="lvl">Threat level: High</span>
<span class="why">Five of the seven vulnerabilities CISA added to the KEV catalog on <b>Sept 2</b>
carry a federal remediation date of <b>Sept 5</b> &mdash; one day out &mdash; and a CVSS 9.8
unauthenticated root RCE in Langflow is under continuous exploitation with credential theft as the
explicit objective.</span></div>

<div class="strip">
<div class="stat"><div class="n">9.8</div><div class="l">CVSS, Langflow CVE-2026-0768 &mdash; unauthenticated RCE as root</div></div>
<div class="stat"><div class="n">360</div><div class="l">Exploitation attempts logged by VulnCheck honeypots in the UK</div></div>
<div class="stat"><div class="n">1 day</div><div class="l">Until the Sept 5 KEV deadline for five of the seven Sept 2 additions</div></div>
<div class="stat"><div class="n">8.7M</div><div class="l">Manchester Airports Group customers in the leaked data (SecurityWeek reports 8.8M)</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="lead">
<h3>Langflow's CVE-2026-0768 is being exploited to strip OpenAI and AWS keys out of environment
variables</h3>
<p>The flaw carries a <b>CVSS 9.8</b> and sits in the handling of the <code>code</code> parameter
passed to the <code>validate</code> endpoint: a user-supplied string is not properly validated before
being used to execute Python, which lets an unauthenticated attacker run arbitrary code
<b>as root</b>. It affects <b>Langflow 1.4.2 and earlier</b> and was disclosed back in
<b>January</b>.</p>
<p>What makes it today's story is what the traffic is doing. Observed commands go straight for
environment variables &mdash; <code>LANGFLOW_SUPERUSER</code>, <code>OPENAI_API*</code>,
<code>AWS_ACCESS*</code> and <code>AWS_SECRET*</code> &mdash; which between them can hand over
Langflow administrator credentials, OpenAI API keys, AWS access key IDs and AWS secret access keys.
This is not crash-and-crypto-mine; it is credential harvesting against AI infrastructure.</p>
<p>VulnCheck detected the attacks through honeypots in the <b>United Kingdom</b>, logging
<b>360 exploitation attempts</b>, with the majority of attack traffic originating from
<b>Russia</b>. Users are advised to upgrade to <b>version 1.11.6</b>, which patches all known
vulnerabilities in the platform.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>SonicWall SMA1000 &mdash; CVE-2026-83548 and CVE-2026-83549, federal deadline tomorrow</h3>
<p>If you run <b>SonicWall SMA1000</b> appliances, this is the one thing to finish today. CVE-2026-83548
is a server-side request forgery and CVE-2026-83549 an OS command injection; both are confirmed
exploited in the wild and both carry a CISA remediation date of <b>September 5, 2026 &mdash; 1 day
left</b>. Affected models are the <b>6210, 7210 and 8200v</b>; the fixed versions are
<b>12.4.3-03526</b> and <b>12.5.0-02952</b>.</p>
<p>The same Sept 5 date applies to three other flaws in the same batch &mdash; JFrog Artifactory
CVE-2026-82329, Sangoma Switchvox CVE-2026-9586 and Kestra OSS CVE-2026-49869 &mdash;
<b>five CVEs in total</b>. The deadline stated here is the same one used in the KEV section
below.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="card">
<div class="tags"><span class="t crit">Extortion</span><span class="t">Data theft, no encryption</span></div>
<h3>FulcrumSec &mdash; also known as The Threat Thespians</h3>
<p>A financially motivated group that <b>emerged in 2025</b> and has claimed several high-profile
hacks including <b>Novo Nordisk</b> and <b>LexisNexis</b>. Its campaigns focus on stealing sensitive
information and using the threat of disclosure as leverage rather than encrypting systems, and it has
previously been reported to use LLMs to analyse the data it steals.</p>
<p>In the Manchester Airports Group intrusion, FulcrumSec claims initial access came from <b>admin
keys for the customer-engagement platform Iterable, found in the frontend JavaScript of all three MAG
websites</b>. The volume claimed varies by outlet: BleepingComputer reports the group claimed roughly
<b>86 GB</b>, while other reporting describes roughly <b>550 GB</b> of uncompressed data, or "half a
terabyte," published after the extortion attempt failed. Both are printed as reported; neither is
adopted.</p>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card"><div class="tags"><span class="t new">New</span><span class="t crit">Extortion</span><span class="t">Aviation</span></div>
<h3>Manchester Airports Group &mdash; data published after ransom refused</h3>
<p>Affects customers of <b>Manchester, London Stansted and East Midlands</b> airports. Exposed data
covers car park, lounge and Fast Track bookings plus in-airport Wi-Fi sign-ups &mdash; email
addresses, phone numbers, postcodes, vehicle registrations and parking history. <b>Payment
information was not compromised</b>, and airport operations, passenger safety and aviation security
were unaffected. MAG received a ransom demand and refused to pay. Impact is reported as
<b>8.7 million</b> customers by most outlets and <b>8.8 million</b> by SecurityWeek.</p></div>

<div class="card"><div class="tags"><span class="t new">New</span><span class="t warn">Telecom</span></div>
<h3>ShinyHunters claims American Tower Corporation</h3>
<p>The group claims to have breached American Tower Corporation and exfiltrated <b>more than 5.2
million records</b>.</p></div>

<div class="card"><div class="tags"><span class="t new">New</span><span class="t crit">Identity</span></div>
<h3>153 million driver licence images offered on the dark web</h3>
<p>Images from the <b>United States and Canada</b> were put up for sale, likely stolen from
<b>IDScan.net</b>.</p></div>

<div class="card"><div class="tags"><span class="t new">New</span><span class="t warn">API abuse</span></div>
<h3>A stolen Metr API key burned $600,000 of AI credits</h3>
<p>Attackers stole a <b>Metr</b> API key in <b>March</b> and used it for <b>three weeks</b>,
consuming about <b>$600,000</b> worth of AI model credits before it was cut off.</p></div>

<div class="card"><div class="tags"><span class="t ok">Takedown</span></div>
<h3>Sality botnet disrupted</h3>
<p>US and European authorities, with <b>CrowdStrike</b> and <b>Shadowserver</b>, disrupted the
Russia-linked <b>Sality</b> botnet by exploiting its own trusted-peer protocol to isolate roughly
<b>15,000</b> infected machines. Note: the botnet's age is reported inconsistently across outlets and
no figure is adopted here.</p></div>

<div class="card"><div class="tags"><span class="t crit">Ransomware</span><span class="t">Public sector</span></div>
<h3>Berlin refuses Rhysida's blackmail</h3>
<p>The city rejected the ransomware gang's extortion demand outright, and Berlin officials temporarily
cancelled remote work in the wake of the attack.</p></div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel" style="padding:5px 7px">
<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td class="mono">CVE-2026-0768</td><td class="mono">9.8</td><td>Langflow &le; 1.4.2</td><td>Unauthenticated RCE as root via the <code>code</code> parameter on <code>validate</code>. <b>Exploited.</b> Fix: 1.11.6.</td></tr>
<tr><td class="mono">CVE-2026-76657</td><td class="mono">10.0</td><td>HPE Networking Fabric Composer</td><td>Authentication bypass in the Fabric Composer API; remote attacker obtains administrative privileges. CVSS 3.1, assigned by HPE. No confirmed exploitation.</td></tr>
<tr><td class="mono">CVE-2026-76658</td><td class="mono">10.0</td><td>HPE Networking Fabric Composer 7.0.0&ndash;7.3.3</td><td>Flaw in the SSH daemon; unauthenticated remote attacker gains administrative access and runs commands as a privileged OS user. HPE advises upgrading the 7.3 branch to <b>7.3.4</b> or later. No confirmed exploitation.</td></tr>
<tr><td class="mono">CVE-2026-85046</td><td class="mono">8.8</td><td>Google Chrome (V8)</td><td>Type confusion in V8 enabling code execution inside the sandbox via a crafted page. <b>Exploited in the wild</b> &mdash; the sixth actively exploited Chrome zero-day of 2026. Fixed in <b>152.0.7977.82/.83</b> (Windows, macOS) and 152.0.7977.82 (Linux). Reported Aug 4, 2026 by Salvatore Gulizia.</td></tr>
<tr><td class="mono">CVE-2026-83548</td><td class="mono">&mdash;</td><td>SonicWall SMA1000 6210 / 7210 / 8200v</td><td>Server-side request forgery. <b>KEV, due Sept 5.</b> Fixed in 12.4.3-03526 and 12.5.0-02952.</td></tr>
<tr><td class="mono">CVE-2026-83549</td><td class="mono">&mdash;</td><td>SonicWall SMA1000 6210 / 7210 / 8200v</td><td>OS command injection. <b>KEV, due Sept 5.</b> Same fixed versions.</td></tr>
<tr><td class="mono">CVE-2026-82329</td><td class="mono">&mdash;</td><td>JFrog Artifactory</td><td>Improper authentication. JFrog issued patches <b>Aug 28, 2026</b>. <b>KEV, due Sept 5.</b></td></tr>
</table>
</div>
<div class="note">Dashes mean no CVSS was confirmed from a vendor advisory or the NVD in this edition's
sources. Blog-reported scores are deliberately not printed in that column.</div>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>Sept 2, 2026 &mdash; CISA added seven vulnerabilities to the KEV catalog</b>, all on evidence
of active exploitation. Reporting notes that <b>three of the seven</b> are AI-infrastructure
components.</li>
<li><b>Due September 5, 2026 <span style="color:var(--crit)">(1 day left)</span></b> &mdash; five
CVEs: <span class="mono">CVE-2026-83548</span> and <span class="mono">CVE-2026-83549</span>
(SonicWall SMA1000), <span class="mono">CVE-2026-9586</span> (Sangoma Switchvox, SQL injection),
<span class="mono">CVE-2026-82329</span> (JFrog Artifactory, improper authentication) and
<span class="mono">CVE-2026-49869</span> (Kestra OSS, OS command injection).</li>
<li><b>Due September 16, 2026 (12 days left)</b> &mdash; the other two:
<span class="mono">CVE-2026-48710</span> (Kludex Starlette, HTTP request/response smuggling) and
<span class="mono">CVE-2026-59822</span> (BerriAI LiteLLM, improper authentication).</li>
<li>Five plus two is <b>seven</b>, matching CISA's own count for the Sept 2 batch. Countdowns are
computed from today, <b>Friday September 4, 2026</b>.</li>
</ul>
</div>
"""

cy = page("The Cyber Wire &mdash; Daily Briefings", "#22d3a8", "#36c6ff", "#0a0f0e",
          "#111917", "#1e2a27", cy_body + sources(CY_SRC) +
          '<div class="disc">Reported for awareness. Verify every advisory against your own vendor '
          'bulletins before acting; severity scores and remediation dates change.</div></footer>',
          extra_css="code{font-family:var(--mono);font-size:.9em;background:rgba(255,255,255,.05);"
                    "padding:1px 5px;border-radius:4px}")
open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(cy)


# ------------------------------------------------------------------------ MMA
MMA_SRC = [
 ("UFC.com - UFC Fight Night: Hooker vs Parnasse (Sept 5, 2026)", "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
 ("UFC.com - Updates to UFC Paris", "https://www.ufc.com/news/updates-ufc-fight-night-paris-2026"),
 ("Rotowire - Hooker vs Parnasse Sept 5, 2026 odds", "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
 ("MMA Odds Breaker - Opening betting odds for UFC Paris", "https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/"),
 ("Tapology - UFC Fight Night: Hooker vs. Parnasse", "https://www.tapology.com/fightcenter/events/144513-ufc-fight-night"),
 ("UFC.com - UFC Fight Night: Nurmagomedov vs Song (Aug 29, 2026)", "https://www.ufc.com/event/ufc-fight-night-august-29-2026"),
 ("UFC.com - UFC Fight Night Shanghai bonus coverage", "https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage"),
 ("Yahoo Sports - UFC Shanghai bonuses: Song Yadong's upset rewarded with $100,000", "https://sports.yahoo.com/articles/ufc-shanghai-bonuses-song-yadongs-134440846.html"),
 ("Sherdog - UFC Shanghai bonuses: Yadong Song, 3 others earn $100,000", "https://www.sherdog.com/news/news/UFC-Shanghai-bonuses-Yadong-Song-3-others-earn-36100000-202571"),
 ("Tapology - Contender Series 2026: Week 5", "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
 ("UFC.com - Noche UFC (2026)", "https://www.ufc.com/noche-ufc-2026"),
 ("Yahoo Sports - Noche UFC: Jean Silva vs. Jose Delgado odds, what to know", "https://sports.yahoo.com/articles/noche-ufc-jean-silva-vs-125016123.html"),
 ("CBS Sports - UFC 331 fight card: Joshua Van vs. Alexandre Pantoja 2", "https://www.cbssports.com/ufc/news/ufc-331-fight-card-joshua-van-vs-alexandre-pantoja-2-date-location-los-angeles/"),
 ("UFC.com - Crypto.com UFC 331", "https://www.ufc.com/event/cryptocom-ufc-331"),
 ("CBS Sports - 2026 UFC event schedule", "https://www.cbssports.com/ufc/news/2026-ufc-event-schedule-islam-makhachev-ian-machado-garry/"),
 ("Sports Illustrated - UFC signs undefeated knockout machine for short-notice debut", "https://www.si.com/fannation/mma/news/ufc-signs-undefeated-knockout-machine-short-notice-debut-fight-ufc-paris-pavel-andrusca"),
 ("Yahoo Sports - Rosas brother signs short-notice Noche debut", "https://sports.yahoo.com/articles/not-cut-rosas-bro-signs-070000602.html"),
 ("ESPN - Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("Wikipedia - UFC 328", "https://en.wikipedia.org/wiki/UFC_328"),
 ("TKO Group Holdings - UFC Freedom 250 delivers 34 million total global viewers", "https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx"),
 ("ESPN - UFC Freedom 250 at the White House averages 7M viewers in the U.S.", "https://www.espn.com/mma/story/_/id/49111943/ufc-freedom-250-white-house-averages-70m-viewers-us"),
 ("SportsPro - UFC 324 sets streaming records for Paramount+", "https://www.sportspro.com/news/broadcast-ott/ufc-324-streaming-paramount-plus-viewership-january-2026/"),
]

MMA_CDN = """<script>(function(){var t=new Date('2026-09-05T12:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,30000);})();</script>"""

mma_body = f"""<header class="mast">
<h1>The Octagon</h1>
<p class="tag">Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting</p>
{META}
</header>
<div class="tldr"><b>Tale of the Tape</b> <span>It is fight eve in Paris, where Salahdine Parnasse is a
heavy favourite over Dan Hooker and an undefeated short-notice newcomer has moved up a weight class to
fill a hole on the card.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("mma", "")}

<div class="cdn"><span class="lbl">Next card</span><span class="clk" id="ufccdn">&mdash;</span>
<span class="ev">UFC Fight Night: Hooker vs. Parnasse &mdash; Saturday, Sept 5, Accor Arena, Paris.
Prelims 12 PM ET, main card 3 PM ET on Paramount+.</span></div>

<h2 class="sec">Top Story</h2>
<div class="lead">
<h3>Fight eve in Paris: Parnasse a heavy favourite, and an undefeated newcomer moves up to save the
co-feature</h3>
<p><b>UFC Fight Night: Hooker vs. Parnasse</b> lands Saturday at the <b>Accor Arena</b> in Paris with
<b>14 fights</b>. The lightweight main event has <b>Salahdine Parnasse</b> as a heavy favourite over
<b>Dan Hooker</b>: current lines have Parnasse at <b>&minus;620</b> and Hooker at <b>+400</b>, with
DraftKings at <b>&minus;600 / +440</b>. That is a market that has moved hard &mdash; the opening
numbers were <b>&minus;357 / +275</b>.</p>
<p>The card also took a late hit. <b>Mairon Santos</b> was removed from his featherweight bout with
<b>Nathaniel Wood</b> due to illness, and undefeated UFC newcomer <b>Pavel Andrusca</b> steps in on
short notice &mdash; a bantamweight prospect moving <i>up</i> to featherweight for his promotional
debut. On the main card, <b>Fares Ziam</b> is a <b>&minus;155</b> favourite against
<b>Axel Sola</b> at <b>+130</b>.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">
<div class="card"><div class="tags"><span class="t new">This weekend</span></div>
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.13em;color:var(--accent);margin-bottom:7px">SEPT 5 &middot; ACCOR ARENA, PARIS</div>
<h3>UFC Fight Night: Hooker vs. Parnasse</h3>
<p>Salahdine Parnasse vs. Dan Hooker, lightweight. 14 fights; prelims 12 PM ET, main card 3 PM ET on
Paramount+. <b>Odds: Parnasse &minus;620 / Hooker +400</b> (current lines); DraftKings &minus;600 /
+440; opening &minus;357 / +275.</p></div>

<div class="card">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.13em;color:var(--accent);margin-bottom:7px">SEPT 8 &middot; META APEX, LAS VEGAS</div>
<h3>Dana White's Contender Series &mdash; Week 5</h3>
<p>Five fights, 7:00 PM ET on Paramount+. Arlind Berisha vs. Quentin Pasley (LHW), Isaac Moreno vs.
Reginaldo Junior (WW), Martin Koz&aacute;k vs. Christian Echols (MW), Davi Cabral vs. Douglas da Lapa,
Luis Francischinelli vs. Will Rentz (WW).</p></div>

<div class="card">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.13em;color:var(--accent);margin-bottom:7px">SEPT 12 &middot; DESERT DIAMOND ARENA, GLENDALE, AZ</div>
<h3>Noche UFC: Silva vs. Delgado</h3>
<p>Mexican Independence Day weekend. Jean Silva vs. Jose Miguel Delgado, featherweight.
<b>Odds: Silva &minus;450 / Delgado +350.</b> Also Brandon Moreno vs. Joseph Morales and Manon Fiorot
vs. Alexa Grasso. Prelims 11:00 AM PT, main card 2:00 PM PT on Paramount+.</p></div>

<div class="card">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.13em;color:var(--accent);margin-bottom:7px">SEPT 19 &middot; CRYPTO.COM ARENA, LOS ANGELES</div>
<h3>Crypto.com UFC 331: Van vs. Pantoja 2</h3>
<p>Flyweight champion Joshua Van rematches former titleholder Alexandre Pantoja. Co-main: a
five-round lightweight bout, Arman Tsarukyan vs. Mauricio Ruffy. Also Gable Steveson vs. Sean Sharaf,
Marlon Vera vs. Charles Jourdain, Casey O'Neill vs. Eduarda Moura, Ryan Gandra vs. Ozzy Diaz. Prelims
6 PM ET, main card 9 PM ET on Paramount+. No headline odds were stated in sources fetched this
edition.</p></div>

<div class="card">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.13em;color:var(--accent);margin-bottom:7px">SEPT 26 &middot; LAS VEGAS</div>
<h3>UFC Fight Night &mdash; Rosas Jr. vs. Barcelos</h3>
<p>Raul Rosas Jr. vs. Raoni Barcelos, bantamweight. No odds stated in sources fetched this
edition.</p></div>
</div>

<h2 class="sec">Last Event &mdash; Results</h2>
<p style="font-size:14.5px;color:var(--muted);margin-bottom:10px"><b>UFC Fight Night: Nurmagomedov vs.
Song</b> &mdash; Saturday, August 29, 2026, Shanghai. Only bouts confirmed against UFC.com or a
primary result source are listed; this is a verified subset, not the full card.</p>
<div class="panel" style="padding:5px 7px">
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Song Yadong</td><td>def. Umar Nurmagomedov (main event, bantamweight)</td><td>KO (right uppercut), R2 1:48</td></tr>
<tr><td class="up">Kai Asakura</td><td>def. Aoriqileng</td><td>KO (head kick and strikes), R2 0:34</td></tr>
</table>
</div>
<div class="panel" style="margin-top:12px">
<div style="font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:8px">Performance bonuses</div>
<ul class="bul">
<li><b>Song Yadong &mdash; $100,000, Performance of the Night.</b> He was not supposed to win, and the
knockout sent the hometown Shanghai crowd into a frenzy.</li>
<li><b>Bilal Hasan &mdash; $100,000, Performance of the Night.</b></li>
<li><b>Levi Rodrigues Jr. vs. Ce Liu &mdash; $100,000 each, Fight of the Night.</b></li>
</ul>
<div class="note">Four $100,000 bonuses in total, matching Sherdog's "Yadong Song, 3 others earn
$100,000" framing.</div>
</div>

<h2 class="sec">Prospect Watch</h2>
<div class="cards">
<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t new">Debuting Sat</span></div>
<h3>Pavel Andrusca</h3>
<p>Undefeated bantamweight prospect, moving up to featherweight for a short-notice UFC debut against
<b>Nathaniel Wood</b> at UFC Paris on Saturday, replacing Mairon Santos.</p></div>

<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t new">New</span></div>
<h3>Jessie Rosas</h3>
<p><b>8-1</b>. Brother of Raul Rosas Jr., signed on short notice for his first Octagon appearance
against fellow newcomer <b>Sean King</b> at Noche UFC in Glendale on Sept 12.</p></div>

<div class="card"><div class="tags"><span class="t ok">Prospect</span></div>
<h3>Bilal Hasan</h3>
<p>Booked for his promotional debut against <b>Nilson Rojas</b> at UFC Shanghai just days after
earning a UFC contract on Dana White's Contender Series &mdash; and walked out of the event with a
<b>$100,000</b> Performance of the Night bonus.</p></div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>Valentina Shevchenko is out of UFC 332</b> (Oct 3, Delta Center, Salt Lake City) with an
undisclosed injury. <b>She remains champion</b> &mdash; the women's flyweight defence against No. 1
contender Natalia Silva is simply off, leaving the card without a headliner.
<b>Natalia Silva vs. Wang Cong</b> has been targeted for an <b>interim</b> women's flyweight
title.</li>
<li><b>Mairon Santos is off UFC Paris with illness</b>, opening the Nathaniel Wood slot for Pavel
Andrusca.</li>
<li><b>Song Yadong's Shanghai upset put him straight back into the title mix at 135 pounds</b> after
knocking out Umar Nurmagomedov.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<div style="font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:8px">Rankings movement</div>
<ul class="bul">
<li>Song Yadong is back in the bantamweight title conversation on the strength of the Shanghai
knockout.</li>
<li>Alexandre Pantoja gets an immediate rematch for the flyweight belt at UFC 331 after losing it to
Joshua Van.</li>
</ul>
<div style="font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin:20px 0 8px">Business &amp; broadcast</div>
<ul class="bul">
<li><b>UFC Freedom 250</b> (June 14, White House) reached roughly <b>34 million total global
viewers</b> per TKO Group Holdings, including <b>17 million</b> across the U.S. and Latin America. It
averaged <b>8.2 million</b> viewers across the U.S. and Latin America and <b>7.0 million</b> in the
U.S. alone &mdash; the most-watched UFC event ever domestically. The 34 million figure counts anyone
who watched at least one minute; it is not an average.</li>
<li><b>Paramount is in year one of a seven-year, $7.7 billion</b> U.S. media-rights deal with the UFC,
which is owned by TKO Group.</li>
<li><b>UFC 324</b> (January 2026), the promotion's first card on Paramount+, drew an average-minute
audience of <b>4.96 million</b>, reached <b>7.18 million</b> households and peaked at <b>5.93
million</b> concurrent viewers.</li>
</ul>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel" style="padding:5px 7px">
<table>
<tr><th>Division</th><th>Champion</th><th>Won it</th></tr>
<tr><td>Heavyweight</td><td><b>Tom Aspinall</b></td><td>Undisputed since June 21, 2025</td></tr>
<tr><td>Heavyweight (interim)</td><td><b>Ciryl Gane</b></td><td>KO2 Alex Pereira, Freedom 250, Jun 14, 2026</td></tr>
<tr><td>Light Heavyweight</td><td><b>Carlos Ulberg</b></td><td>KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, Apr 11, 2026</td></tr>
<tr><td>Middleweight</td><td><b>Sean Strickland</b></td><td>Split decision over Khamzat Chimaev, UFC 328, May 9, 2026 &mdash; two-time champion</td></tr>
<tr><td>Welterweight</td><td><b>Islam Makhachev</b></td><td>UD Jack Della Maddalena, UFC 322, Nov 15, 2025 &middot; 1 defence (UD Ian Machado Garry, UFC 330)</td></tr>
<tr><td>Lightweight</td><td><b>Justin Gaethje</b></td><td>TKO4 Ilia Topuria, Freedom 250, Jun 14, 2026</td></tr>
<tr><td>Featherweight</td><td><b>Alexander Volkanovski</b></td><td>UD Diego Lopes, UFC 314, Apr 12, 2025 &middot; defended UD Lopes, UFC 325, Jan 31, 2026</td></tr>
<tr><td>Bantamweight</td><td><b>Petr Yan</b></td><td>UD Merab Dvalishvili, UFC 323, Dec 6, 2025</td></tr>
<tr><td>Flyweight</td><td><b>Joshua Van</b></td><td>TKO1 Alexandre Pantoja, UFC 323, Dec 6, 2025 &middot; 1 defence (TKO5 Tatsuro Taira, UFC 328) &middot; rematch Sept 19</td></tr>
<tr><td>Women's Flyweight</td><td><b>Valentina Shevchenko</b></td><td>Reigning champion &mdash; withdrew from the UFC 332 defence with an injury</td></tr>
<tr><td>Women's Bantamweight</td><td><b>Kayla Harrison</b></td><td>Sub2 Julianna Pe&ntilde;a, UFC 316, Jun 7, 2025 &middot; 0 defences</td></tr>
<tr><td>Women's Strawweight</td><td><b>Mackenzie Dern</b></td><td>UD Virna Jandiroba, UFC 321, Oct 25, 2025 &middot; 1 defence (UD Gillian Robertson, UFC 330)</td></tr>
</table>
</div>
<div class="note">This board is built from the individual event results that decided each belt, not
copied from a syndicated "current champions" listing. A syndicated list pulled this edition again
returned <b>Khamzat Chimaev</b> at middleweight &mdash; he lost the title to Sean Strickland by split
decision at UFC 328 on May 9, 2026, which ESPN's own reporting confirms. The same listings keep
showing Alex Pereira at light heavyweight (superseded at UFC 327) and Ilia Topuria at lightweight
(superseded at Freedom 250). None of those three is the champion.</div>
"""

mma = page("The Octagon &mdash; Daily Briefings", "#e84545", "#ff8a5c", "#100c0c",
           "#1a1313", "#322020", mma_body + sources(MMA_SRC) +
           '<div class="disc">Cards and bouts are subject to change &mdash; fighters withdraw, bouts '
           'get reshuffled and odds move right up to the walkout. Betting lines are shown as reported '
           'and are not a recommendation.</div></footer>', extra_js=MMA_CDN)
open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(mma)


# ---------------------------------------------------------------------- INDEX
ix_body = f"""<header class="mast">
<h1>Daily Briefings</h1>
<p class="tag">Three desks, refreshed every 30 minutes &mdash; security, markets and the fight game</p>
{META}
</header>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("index", "")}

<div class="cards">
<div class="card" style="border-left:3px solid #22d3a8">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#22d3a8;margin-bottom:9px">&#9960; The Cyber Wire &middot; The Wire</div>
<h3 style="font-size:19px">A federal patch deadline lands tomorrow</h3>
<p>Five of the seven flaws CISA added to the KEV catalog on Sept 2 must be remediated by
<b>Sept 5</b> &mdash; one day out &mdash; while attackers keep hammering Langflow's CVSS 9.8
unauthenticated root RCE to strip OpenAI and AWS keys out of environment variables.</p>
<p style="margin-top:11px"><a href="cyber-briefing.html" style="color:#22d3a8">Read the briefing &rarr;</a></p>
</div>

<div class="card" style="border-left:3px solid #caa64a">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#caa64a;margin-bottom:9px">&#9650; The Closing Bell &middot; The Tape</div>
<h3 style="font-size:19px;font-family:Georgia,'Times New Roman',serif">The jobs report is the whole session</h3>
<p>Futures are steady to modestly higher before the August employment report at <b>8:30 AM ET</b>, the
print that decides a Fed split 50-50 into Sept 15&ndash;16 &mdash; after Thursday's Waller-driven
rally handed the Dow its best day since Aug 4.</p>
<p style="margin-top:11px"><a href="wallstreet-briefing.html" style="color:#caa64a">Read the briefing &rarr;</a></p>
</div>

<div class="card" style="border-left:3px solid #e84545">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#e84545;margin-bottom:9px">&#8856; The Octagon &middot; Tale of the Tape</div>
<h3 style="font-size:19px">Fight eve in Paris</h3>
<p>Salahdine Parnasse is a heavy favourite over Dan Hooker at the Accor Arena on Saturday, and an
undefeated short-notice newcomer has moved up a weight class to fill a hole on the card.</p>
<p style="margin-top:11px"><a href="mma-briefing.html" style="color:#e84545">Read the briefing &rarr;</a></p>
</div>
</div>

<div class="note" style="margin-top:22px">Every figure on these pages is checked against a source
fetched in the same run that published it. Where two outlets disagree, both readings are printed and
neither is adopted; where nothing could be verified, the item is left off rather than guessed.</div>
"""

ix = page("Daily Briefings", "#c9c4bc", "#e8e3da", "#0d0d0f", "#161619", "#26262b", ix_body +
          '<footer><div class="disc">Independent daily briefings compiled from public reporting. '
          'Not investment advice.</div></footer>')
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(ix)

print("built 4 pages ->", OUT)
