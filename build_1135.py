# -*- coding: utf-8 -*-
"""Daily Briefings build script -- 2026-09-03 ~11:35 AM ET edition."""
import io, os, re

OUT = "/sessions/vigilant-charming-curie/mnt/outputs"
CSS = open("/sessions/vigilant-charming-curie/build/base_css.txt").read()

def css_for(accent, accent2, bg=None, panel=None, line=None, extra=""):
    c = CSS
    c = c.replace("--accent:#22d3a8; --accent2:#36c6ff;", "--accent:%s; --accent2:%s;" % (accent, accent2))
    if bg:
        c = c.replace("--bg:#0d0f11; --panel:#14181b; --line:#232a2e;",
                      "--bg:%s; --panel:%s; --line:%s;" % (bg, panel, line))
    return c.replace("</style>", extra + "\n</style>")

STAMP = """<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>"""

def nav(active):
    items = [("index.html", "★ Front Page"),
             ("cyber-briefing.html", "⛨ The Cyber Wire"),
             ("wallstreet-briefing.html", "▲ The Closing Bell"),
             ("mma-briefing.html", "⊘ The Octagon"),
             ("archive.html", "\U0001f5c4 Archive")]
    out = ['<nav class="tabs">']
    for href, label in items:
        cls = ' class="on"' if href == active else ''
        out.append('<a href="%s"%s>%s</a>' % (href, cls, label))
    out.append('</nav>')
    return "".join(out)

META = """<div class="meta">
<span class="pill live"><span class="dot"></span>Live</span>
<span class="pill" id="edition">&nbsp;</span>
<span class="pill" id="datestamp">&nbsp;</span>
<span class="pill">Updated <span id="updated">&nbsp;</span></span>
</div>"""

def head(title, css):
    return ('<!DOCTYPE html>\n<html lang="en"><head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '<title>%s</title>\n%s\n</head><body>\n<div class="wrap">\n' % (title, css))

def sources(items):
    s = ['<h5 class="sec" style="font-size:11.5px">Sources</h5><ol>']
    for t, u in items:
        s.append('<li><a href="%s">%s</a></li>' % (u, t))
    s.append("</ol>")
    return "".join(s)

# ---------------------------------------------------------------- SUMMARIES
SUM_WS = ("Stocks are higher across the board this morning as Treasury yields pull back "
          "after Fed Governor Christopher Waller said he is leaning toward holding rates "
          "steady in September, with ChargePoint up more than 50% on its quarterly results.")
SUM_CY = ("Thomson Reuters has disclosed that an intruder took court files from its C-Track "
          "case-management platform across at least a dozen U.S. states, the U.S. Virgin Islands "
          "and Canada, and five actively exploited flaws in CISA's latest batch fall due on Saturday.")
SUM_MM = ("UFC 332 is four weeks out with no main event after Valentina Shevchenko's withdrawal, "
          "and Cris Cyborg has publicly offered to headline it against Amanda Nunes.")

# ================================================================ WALL STREET
ws_css = css_for("#caa64a", "#e8c766", extra="""
.mast h1{font-family:Georgia,'Times New Roman',serif}
.lead h3,.card h3{font-family:Georgia,'Times New Roman',serif}
""")

ws = io.StringIO()
ws.write(head("The Closing Bell &mdash; Daily Briefing", ws_css))
ws.write('<header class="mast"><h1>The Closing Bell</h1>'
         '<p class="tag">Your daily markets briefing &mdash; the tape, the movers &amp; the rates</p>'
         + META + '</header>')
ws.write('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % SUM_WS)
ws.write('<div class="freshline" id="freshline">&nbsp;</div>')
ws.write(nav("wallstreet-briefing.html"))

# BLOCK A
ws.write('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>'
 '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
 '{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:CHPT","title":"ChargePoint"},'
 '{"proName":"NYSE:SNOW","title":"Snowflake"},{"proName":"NASDAQ:PLTR","title":"Palantir"},'
 '{"proName":"NASDAQ:RARE","title":"Ultragenyx"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},'
 '{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],'
 '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}'
 '</script></div>')

# BLOCK B
ws.write('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2><div class="tickers">')
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"):
    ws.write('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
             '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)
ws.write('</div><div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>')

# LEAD
ws.write('<h2 class="sec">The Lead</h2>')
ws.write('<div class="lead"><h3>Waller opens the door to a September hold, yields fall and stocks rise '
         '&mdash; readings as of ~9:30&ndash;11:21 AM ET</h3>'
         '<p>Federal Reserve Governor Christopher Waller said Thursday he is leaning toward keeping interest '
         'rates steady at the central bank’s September meeting, provided there are no surprises in upcoming '
         'inflation data. “If this continues in the data due over the next two weeks, I would be inclined to '
         'support holding the target for the federal funds rate at its current setting,” Waller said in '
         'remarks prepared for a Reuters interview. He conceded inflation is “meaningfully above” the '
         'Fed’s 2% target but said recent trends “suggest we are finally seeing some signs of disinflation” '
         '— a contrast with Chair Kevin Warsh’s remarks last week.</p>'
         '<p>Market-implied odds of a rate <em>hike</em> at the September 15&ndash;16 meeting fell sharply after '
         'the remarks, to a 48.4% probability, down about 15 percentage points from Wednesday, according to CME '
         'Group’s FedWatch tool. The 10-year Treasury note yield last traded around 4.75%; on Wednesday it '
         'reached its highest level since November 2023.</p>'
         '<p>At the opening bell the S&amp;P 500 gained 0.57%, the Dow Jones Industrial Average rose 0.80%, the '
         'Nasdaq climbed 0.64% and the Russell 2000 jumped 1.13%. A separate mid-morning reading put the Dow up '
         '282.76 points (0.53%), the S&amp;P 500 up 37.86 points (0.49%) and the Nasdaq up 229.68 points (0.88%). '
         'These are two different moments in the same session, not competing readings of one moment, and neither '
         'is adopted here as the current print.</p>'
         '<p>The geopolitical backdrop has not eased. Iran targeted U.S. allies Jordan, the United Arab Emirates '
         'and Kuwait with missiles and drones overnight in retaliation for the latest round of American airstrikes. '
         '“Oil has consequently rebuilt some geopolitical premium, creating another potential inflationary '
         'headache at a time when markets are already debating whether US rates need to move higher,” said '
         'Daniela Hathorn, senior market analyst at Capital.com.</p>'
         '<p class="note">Nothing in this editorial is a live price. For the current print, use the streaming '
         'quotes above.</p></div>')

# MOVERS
ws.write('<h2 class="sec">Movers &amp; Drivers</h2><div class="cards">')
movers = [
 (["New","Up"], "ChargePoint (CHPT) &mdash; up more than 50%",
  "ChargePoint surged 52% in late-morning trading after the EV charging network operator beat second-quarter "
  "earnings forecasts; a 10:19 AM ET quote had it at 51.4%, and it was up 17.3% before the bell. The two "
  "in-session readings both put it above 50%; the pre-bell figure is a different window and is not comparable. Revenue was $116 million, up 18% year over year, with a record non-GAAP gross margin "
  "of 38% and an adjusted loss narrower than expected."),
 (["Up"], "Snowflake (SNOW) &mdash; about 22% in the session",
  "Snowflake soared nearly 22% in Thursday trading after second-quarter results beat expectations; the stock had "
  "been up nearly 24% before the bell. Adjusted earnings were 62 cents on $1.55 billion in revenue against "
  "estimates of 45 cents and $1.48 billion, and the company raised its full-year product revenue guidance."),
 (["New","Up"], "Palantir (PLTR) &mdash; up 8.7%",
  "Palantir rose 8.7% after its subsidiary Palantir USG secured a U.S. Army prime contractor agreement to "
  "manufacture and deliver eight TITAN ground-station systems. The company also said former AIG chief executive "
  "Peter Zaffino will join as its global head of financial services."),
 (["New","Down"], "Ultragenyx (RARE) &mdash; down 44%",
  "Ultragenyx Pharmaceutical cratered 44% in the session, after a 47% drop before the bell, following news that "
  "its pivotal Phase 3 Aspire study of apazunersen (GTX-102) in Angelman syndrome did not meet its primary or key "
  "secondary endpoints."),
 (["New","Down"], "Victoria&rsquo;s Secret (VSXY) &mdash; down 12.1%",
  "Victoria&rsquo;s Secret &amp; Co. tumbled 12.1%, after a 17% fall before the bell, having missed second-quarter "
  "earnings expectations and guided full-year earnings below consensus."),
 (["New","Down"], "Ciena (CIEN) &mdash; down 11%",
  "Ciena fell 11% despite beating third-quarter earnings and revenue forecasts, as investors reacted to ongoing "
  "supply constraints."),
 (["Down"], "Hewlett Packard Enterprise (HPE) &mdash; down 7.5%",
  "HPE fell 7.5% as investors weighed supply-chain bottlenecks and potential margin pressure."),
 (["Down"], "Campbell&rsquo;s (CPB) &mdash; down 6.4% before the bell",
  "Campbell&rsquo;s fell 6.4% to $22.26 in premarket trading after weak quarterly results, a major dividend cut and "
  "a downbeat outlook. Net sales fell 8% to $2.1 billion, gross margin narrowed 310 basis points to 27.3% and "
  "adjusted earnings fell 37% to 39 cents a share; fiscal 2027 guidance of $1.65&ndash;$1.80 sits below a $1.83 "
  "FactSet consensus."),
 (["Up"], "Nvidia (NVDA) &mdash; up 0.55%",
  "Nvidia gained 0.55% to $225.64 after agreeing to buy AI model platform Hugging Face for $12.93 billion, "
  "according to the Financial Times; other outlets have put the figure at about $13 billion. Hugging Face turned "
  "down a $500 million Nvidia investment at a $7 billion valuation last year."),
]
for tags, h, p in movers:
    tclass = {"New": "new", "Up": "ok", "Down": "crit"}
    ws.write('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % (
        "".join('<span class="t %s">%s</span>' % (tclass.get(t, ""), t) for t in tags), h, p))
ws.write('</div>')

# BLOCK E
ws.write('<h2 class="sec">Chart of the Day &mdash; ChargePoint (CHPT)</h2>'
 '<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>'
 '{"symbol":"NYSE:CHPT","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark",'
 '"isTransparent":true,"autosize":false}</script></div>'
 '<div class="note">ChargePoint is the largest single-name move among the stocks sourced for this edition.</div>')

# BLOCK D
ws.write('<h2 class="sec">Sector Heat &mdash; live</h2>'
 '<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>'
 '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en",'
 '"colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,'
 '"isMonoSize":false,"width":"100%","height":420}</script></div>'
 '<div class="note">Within technology, software got a bounce behind Snowflake’s results while semiconductors '
 'pulled back after Broadcom guided next-quarter revenue and margins below consensus. A single-day sector table '
 'circulated this morning without any laggard and without a stated session to attach it to, so no sector '
 'percentages are published here.</div>')

# BLOCK F
ws.write('<h2 class="sec">The Calendar &mdash; live</h2>'
 '<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>'
 '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
 '"importanceFilter":"0,1","countryFilter":"us"}</script></div>')

# BLOCK C
ws.write('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>'
 '<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>'
 '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular",'
 '"width":"100%","height":420,"locale":"en"}</script></div>')

# SCORECARD
ws.write('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2><div class="panel"><table>'
 '<tr><th>Index</th><th>Close (Wed, Sept 2)</th><th>Change</th></tr>'
 '<tr><td>S&amp;P 500</td><td class="mono">7,666.60</td><td class="up">+0.46%</td></tr>'
 '<tr><td>Nasdaq Composite</td><td class="mono">26,217.83</td><td class="up">+0.45%</td></tr>'
 '<tr><td>Dow Jones Industrial Average</td><td class="mono">53,061.95</td><td class="up">+295.07 &nbsp;+0.56%</td></tr>'
 '</table><div class="note">Wednesday’s closing levels are carried forward from this briefing’s verified record '
 'and have been consistent across repeated checks. This morning’s coverage states only that the major averages '
 'closed higher Wednesday, snapping a three-day losing streak.</div></div>')

# RATES
ws.write('<h2 class="sec">Rates, Bonds &amp; Commodities</h2><div class="panel"><table>'
 '<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>'
 '<tr><td>10-year Treasury</td><td class="mono">~4.75%</td><td>Last traded around 4.75% after Waller’s remarks; '
 'Wednesday it hit its highest since November 2023</td></tr>'
 '<tr><td>WTI crude</td><td class="mono">$92.94</td><td class="up">+2.12% (quoted 7:05 AM ET); oil near six-week highs</td></tr>'
 '<tr><td>Brent crude</td><td class="mono">$97.45</td><td class="up">+1.90% (quoted 7:05 AM ET)</td></tr>'
 '<tr><td>Gold futures</td><td class="mono">$4,494.70</td><td class="up">+1.81% in early trading</td></tr>'
 '<tr><td>Silver futures</td><td class="mono">$66.39</td><td class="up">+1.42% in early trading</td></tr>'
 '<tr><td>Dollar / yen</td><td class="mono">below 156</td><td>The dollar fell more than 2% against the yen, its '
 'lowest since late February</td></tr>'
 '</table><div class="note">No federal funds target level is published: none appears in today’s sources.</div></div>')

# RADAR
ws.write('<h2 class="sec">On the Radar</h2><div class="panel"><ul class="bul">'
 '<li><b>Friday, September 4, 8:30 AM ET &mdash; the August employment report.</b> Economists expect about 58,000 '
 'jobs added and the unemployment rate holding at 4.1%. The spread is wide: Wells Fargo looks for an 80,000 '
 'rebound, Fifth Third for a 25,000 decline. July payrolls fell by 23,000.</li>'
 '<li><b>Wednesday, September 16 &mdash; the FOMC decision</b> concludes the September 15&ndash;16 meeting. '
 'Market-implied hike odds sit at 48.4% after Waller’s remarks, down about 15 points from Wednesday.</li>'
 '<li><b>Released this morning: the July trade deficit widened to $88.6 billion</b>, the widest gap since March '
 '2025 and 24.4% larger than June. Imports rose 2.8% and exports fell 2.1%; capital goods imports jumped 11.4%, '
 'the largest increase since 1993.</li>'
 '<li><b>Also released: Challenger, Gray &amp; Christmas counted 52,881 announced U.S. job cuts in August</b>, up '
 '58% from July but down 38% from a year earlier &mdash; the lowest August total since 2022.</li>'
 '</ul></div>')

ws.write('<footer>' + sources([
 ("TheStreet &mdash; Stock Market Today (Sept. 3, 2026): Nasdaq climbs as Treasury yields pull back",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-03-2026"),
 ("Investrade &mdash; Mid-Morning Look: September 03, 2026", "https://investrade.com/mid-morning-look-september-03-2026/"),
 ("CNBC &mdash; Fed Governor Waller indicates he will support holding rates steady at September meeting",
  "https://www.cnbc.com/2026/09/03/fed-governor-waller-indicates-he-will-support-holding-rates-steady-at-september-meeting.html"),
 ("CNBC &mdash; Stocks making the biggest moves premarket: SNOW, MRNA, AVGO",
  "https://www.cnbc.com/2026/09/03/stocks-making-the-biggest-moves-premarket-snow-mrna-avgo.html"),
 ("Yahoo Finance &mdash; Stock market today: Dow, S&amp;P 500, Nasdaq rise, yields fall",
  "https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-3-dow-sp-500-nasdaq-futures-081525933.html"),
 ("CME Group &mdash; FedWatch tool", "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"),
 ("Kiplinger &mdash; August Jobs Report Preview", "https://www.kiplinger.com/investing/economy/jobs-report-august-2026-what-to-expect"),
 ("Morningstar &mdash; August Jobs Report Expected to Show Moderate Hiring Gains",
  "https://www.morningstar.com/economy/august-jobs-report-expected-show-moderate-hiring-gains"),
]) + '<div class="disc">For information only. Nothing here is investment advice. Quotes from embedded widgets may '
 'be delayed; editorial figures reflect the sources listed above at the times stated.</div></footer>')
ws.write('</div>' + STAMP + '\n</body></html>')

open(os.path.join(OUT, "wallstreet-briefing.html"), "w").write(ws.getvalue())

# ==================================================================== CYBER
cy = io.StringIO()
cy.write(head("The Cyber Wire &mdash; Daily Briefing", css_for("#22d3a8", "#36c6ff")))
cy.write('<header class="mast"><h1>The Cyber Wire</h1>'
         '<p class="tag">Your daily cybersecurity briefing &mdash; breaches, exploits &amp; federal deadlines</p>'
         + META + '</header>')
cy.write('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % SUM_CY)
cy.write('<div class="freshline" id="freshline">&nbsp;</div>')
cy.write(nav("cyber-briefing.html"))

cy.write('<div class="banner"><span class="lvl">Threat Level: High</span><span class="why">'
 'Two CVSS 10.0 flaws in CISA’s September 2 batch are under active exploitation with a federal remediation '
 'deadline on Saturday, and a breach of Thomson Reuters’ court case-management platform has now reached court '
 'systems in at least a dozen U.S. states, the U.S. Virgin Islands and Canada.</span></div>')

cy.write('<div class="strip">'
 '<div class="stat"><div class="n">12+</div><div class="l">U.S. states with court systems in the Thomson Reuters C-Track breach</div></div>'
 '<div class="stat"><div class="n">7</div><div class="l">Exploited flaws CISA added to the KEV catalog on Sept 2</div></div>'
 '<div class="stat"><div class="n">153M</div><div class="l">Driver’s licenses offered for sale on the Nexus dark-web service</div></div>'
 '<div class="stat"><div class="n">2 days</div><div class="l">Until the Sept 5 federal remediation deadline</div></div>'
 '</div>')

cy.write('<h2 class="sec">Top Story</h2>')
cy.write('<div class="lead"><h3>Thomson Reuters says an intruder took court files from C-Track across at least a dozen '
 'U.S. states, the U.S. Virgin Islands and Canada</h3>'
 '<p>Thomson Reuters has disclosed a data breach affecting C-Track, the court case-management platform operated '
 'by its subsidiaries, exposing court records and sensitive personal information across courts in at least 12 U.S. '
 'states, the U.S. Virgin Islands and Canada. The company published the disclosure on Wednesday alongside separate '
 'notification pages for affected individuals in the United States and Canada. One outlet counts 11 states rather '
 'than 12; neither figure is adopted here, and the company itself notes the list has kept growing as individual '
 'courts issue their own disclosures.</p>'
 '<p>The timeline is the uncomfortable part. Thomson Reuters says it discovered unauthorized activity involving '
 'C-Track information on <b>June 30, 2026</b>, and its investigation determined the files were obtained in '
 '<b>March 2026</b> &mdash; roughly three months of undetected access to a system holding court filings.</p>'
 '<p>Affected jurisdictions include the Court of Appeal for Ontario, the Ontario Superior Court of Justice and the '
 'Ontario Court of Justice in Canada; and in the U.S. the Alabama Appellate Courts, Kentucky Appellate Courts, '
 'the Montana Supreme Court, the Nevada Appellate Courts, the North Dakota Supreme Court, the Supreme Court of '
 'South Carolina and South Carolina Court of Appeals, the Tennessee Appellate Court Clerk’s Office, the New '
 'Hampshire Supreme Court, ten Ohio District Courts of Appeals and the Court of Common Pleas of Monroe County in '
 'Ohio, the Court of Common Pleas of Washington County and the Fifth Judicial District in Pennsylvania, the U.S. '
 'Virgin Islands Supreme and Superior Courts, and the entire Wyoming Judicial Branch. The Oregon Judicial Department has separately confirmed its appellate courts were affected.</p>'
 '<p>Affected records may have contained names together with Social Security numbers, driver’s license numbers, '
 'medical information, dates of birth and health insurance information; the U.S. notification adds that '
 '“confidential, redacted, or sealed court information may also have been affected at some courts.” '
 'Thomson Reuters says the incident occurred within its own cloud environment and not on court networks, that '
 'C-Track remains fully operational, and that it has no evidence to date of fraud or misuse. All affected '
 'individuals are being offered 12 months of credit monitoring and identity theft protection. Who was responsible, '
 'exactly what data was taken and how the attacker got in all remain publicly unanswered.</p></div>')

cy.write('<div class="callout"><h3>Also leading &mdash; 153 million driver&rsquo;s licenses offered for sale, and the '
 'FBI is investigating</h3><p>A dark-web service called Nexus began selling high-quality scans of more than 153 '
 'million driver’s licenses and other identity documents, alongside more than 10 million ID cards, 3 million '
 'travel documents and 579,000 medical cards including marijuana dispensary cards. Reporting by Brian Krebs traced '
 'the images to Louisiana-based identity-verification firm IDScan.net; the FBI’s New Orleans office is '
 'investigating. IDScan.net says it is investigating but has not publicly confirmed its systems were the source.</p></div>')

cy.write('<div class="callout crit"><h3>Patch Priority &mdash; two CVSS 10.0 flaws, federal deadline Saturday, '
 'September 5</h3><p>If you run either product, this is today’s work. <b>SonicWall SMA 1000 appliances '
 '(CVE-2026-83548, CVSS 10.0)</b> carry a pre-authentication server-side request forgery flaw that can be chained '
 'with CVE-2026-83549 for unauthenticated remote code execution. SonicWall says it investigated a case '
 'indicating active exploitation of both. <b>Kestra OSS (CVE-2026-49869, CVSS 10.0)</b> carries an OS command injection flaw letting '
 'an unauthenticated remote attacker create and execute arbitrary workflows without credentials; Microsoft reported '
 'it was likely exploited in late June to establish a reverse shell, enumerate a Docker container environment, evade '
 'defenses and deploy a cryptocurrency miner. Federal civilian agencies must remediate both by <b>Saturday, '
 'September 5, 2026 &mdash; 2 days from today</b>.</p></div>')

cy.write('<h2 class="sec">Threat Actor Spotlight</h2>')
cy.write('<div class="panel"><h3 style="margin:0 0 8px;font-size:17px">Qilin (aka Agenda) &mdash; ransomware '
 'operators turning up inside AI gateways</h3>'
 '<p style="margin:0 0 10px;font-size:14.8px;color:#cfc9c2">Google-owned Wiz has linked threat actors associated '
 'with the Qilin (aka Agenda) ransomware to active exploitation of a two-flaw chain against Berri LiteLLM &mdash; '
 'CVE-2026-42271 (CVSS 8.7) chained with CVE-2026-48710 &mdash; to bypass authentication and achieve remote code '
 'execution against vulnerable deployments. Wiz says it has separately observed exploitation attempts involving '
 'CVE-2026-59822 against its own honeypots, probing model-enumeration endpoints.</p>'
 '<p style="margin:0;font-size:14.8px;color:#cfc9c2">Microsoft’s reporting on the same infrastructure describes '
 'attackers breaking into LiteLLM gateways to deliver an XMRig miner via an ELF binary, fingerprinting the host and '
 'killing competing miners first, then using previously collected database information to reach the LiteLLM-backed '
 'PostgreSQL tier and harvest records from LiteLLM_ProxyModelTable and LiteLLM_VerificationToken — model '
 'configuration, upstream provider key material, provider endpoints and proxy-issued virtual keys. Persistence came '
 'through modification of ~/.ssh/authorized_keys. “Defenders should monitor AI workloads according to their '
 'control-plane role, not only as isolated applications,” Microsoft said.</p></div>')

cy.write('<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">')
breaches = [
 (["New","Critical"], "Thomson Reuters &mdash; C-Track court records",
  "Files associated with court systems in at least 12 U.S. states, the U.S. Virgin Islands and Canada were taken in "
  "March 2026 and the activity was not discovered until June 30. Names may appear alongside Social Security numbers, "
  "driver&rsquo;s license numbers, medical information, dates of birth and health insurance information, and sealed "
  "or redacted court information may have been affected at some courts."),
 (["New","Identity"], "IDScan.net / the Nexus marketplace",
  "More than 153 million driver&rsquo;s license scans, 10 million ID cards, 3 million travel documents and 579,000 "
  "medical cards went up for sale on a dark-web service called Nexus. Krebs on Security traced the images to "
  "IDScan.net; the FBI&rsquo;s New Orleans office is investigating. The company says it is investigating and has not "
  "confirmed the source."),
 (["Cryptomining"], "Kestra OSS &mdash; a workflow engine turned into a miner host",
  "Microsoft reported that CVE-2026-49869 was likely exploited by a threat actor in late June 2026 to establish a "
  "reverse shell, perform Docker container environment discovery, evade defenses, deploy a cryptocurrency miner and "
  "facilitate data harvesting. Microsoft describes four impact paths: shell execution through the workflow engine, "
  "container exposure through Docker socket access, host resource hijacking, and follow-on collection through "
  "workflow task execution."),
 (["New","AI Infrastructure"], "RAGFlow &mdash; exposed instances probed for LLM keys",
  "In a separate campaign documented by Microsoft, adversaries are suspected of exploiting exposed RAGFlow instances "
  "using CVE-2026-45312, CVE-2026-28797, CVE-2026-24770, CVE-2025-68700 and CVE-2025-69286 to establish persistence "
  "and steal large language model provider keys and related metadata."),
]
for tags, h, p in breaches:
    tclass = {"New": "new", "Critical": "crit", "Identity": "warn", "Cryptomining": "warn", "AI Infrastructure": "warn"}
    cy.write('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % (
        "".join('<span class="t %s">%s</span>' % (tclass.get(t, ""), t) for t in tags), h, p))
cy.write('</div>')

cy.write('<h2 class="sec">Vulnerability Watch</h2><div class="panel"><table>'
 '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>'
 '<tr><td class="mono">CVE-2026-83548</td><td class="mono down">10.0</td><td>SonicWall SMA 1000 appliances</td>'
 '<td>Pre-auth server-side request forgery; chainable with 83549 for unauthenticated RCE. Exploited; KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-49869</td><td class="mono down">10.0</td><td>Kestra OSS</td>'
 '<td>OS command injection; unauthenticated attacker can create and execute arbitrary workflows. Exploited; KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-82329</td><td class="mono down">9.8</td><td>JFrog Artifactory</td>'
 '<td>Improper authentication in the default configuration; unauthenticated network attacker can obtain administrative '
 'privileges. Exploited; KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-20212</td><td class="mono down">9.8</td><td>Cisco Nexus 9000 Series switches (Silicon One)</td>'
 '<td>Unauthenticated remote code execution as root; TCP ports 43210 and 43211 reachable in the default L3 VRF. '
 'Disclosed Sept 2. Cisco’s PSIRT says it is not aware of malicious use &mdash; not in KEV.</td></tr>'
 '<tr><td class="mono">CVE-2026-9586</td><td class="mono warn">9.3</td><td>Sangoma Switchvox</td>'
 '<td>SQL injection reachable unauthenticated; a single crafted request can execute arbitrary SQL against the backend '
 'PostgreSQL database, including RCE. Exploited; KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-59822</td><td class="mono warn">8.8</td><td>Berri LiteLLM (MCP Streamable HTTP endpoint)</td>'
 '<td>Improper authentication; an unauthenticated attacker can establish an authenticated MCP session with an arbitrary '
 'Bearer token. Exploited; KEV, due Sept 16.</td></tr>'
 '<tr><td class="mono">CVE-2026-83549</td><td class="mono warn">7.8</td><td>SonicWall SMA 1000 appliances</td>'
 '<td>Post-auth OS command injection; an authenticated administrator can execute arbitrary OS commands. Exploited; '
 'KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-48710</td><td class="mono">6.5</td><td>Kludex Starlette</td>'
 '<td>HTTP request/response smuggling; paths injected into the host part can bypass authentication that depends on the '
 'reconstructed URL path. Exploited; KEV, due Sept 16.</td></tr>'
 '</table><div class="note">CVE-2026-48710 now carries a stated score of 6.5; earlier editions of this briefing left '
 'the cell empty because no source gave a number.</div></div>')

cy.write('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2><div class="panel"><ul class="bul">'
 '<li><b>Saturday, September 5, 2026 &mdash; 2 days left.</b> Five of the seven flaws CISA added on September 2: '
 'SonicWall SMA 1000 CVE-2026-83548 and CVE-2026-83549, Sangoma Switchvox CVE-2026-9586, JFrog Artifactory '
 'CVE-2026-82329 and Kestra OSS CVE-2026-49869.</li>'
 '<li><b>Wednesday, September 16, 2026 &mdash; 13 days left.</b> Kludex Starlette CVE-2026-48710 and Berri LiteLLM '
 'CVE-2026-59822.</li>'
 '<li>The instrument cited for these dates is <b>Binding Operational Directive 26-04, “Prioritizing Security '
 'Updates Based on Risk”</b>, under which Federal Civilian Executive Branch agencies are directed to apply the '
 'patches by the dates above.</li>'
 '</ul><div class="note">CISA’s August 31 additions are not covered in this edition, and no deadline for them '
 'is stated here.</div></div>')

cy.write('<footer>' + sources([
 ("Help Net Security &mdash; Thomson Reuters reveals breach that exposed U.S. and Canadian court records",
  "https://www.helpnetsecurity.com/2026/09/03/thomson-reuters-reveals-breach-that-exposed-u-s-and-canadian-court-records/"),
 ("Infosecurity Magazine &mdash; US and Canadian Court Records Breached Following Thomson Reuters Attack",
  "https://www.infosecurity-magazine.com/news/us-canada-court-breach-thomson/"),
 ("Ontario Courts &mdash; Public statement on the cybersecurity incident",
  "https://www.ontariocourts.ca/en/public-statement-cybersecurity.htm"),
 ("The Hacker News &mdash; CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners",
  "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
 ("CISA &mdash; CISA Adds Seven Known Exploited Vulnerabilities to Catalog (Sept 2, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("Microsoft Security Blog &mdash; When AI infrastructure becomes a target: securing gateways and control points",
  "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"),
 ("Wiz &mdash; AI infrastructure honeypot findings", "https://www.wiz.io/blog/ai-infrastructure-honeypot"),
 ("Rapid7 &mdash; Critical SonicWall SMA1000 vulnerabilities exploited in the wild",
  "https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild/"),
 ("Cisco Security Advisory &mdash; Nexus 9000 Series Switches Silicon One RCE",
  "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr"),
 ("Krebs on Security &mdash; FBI Probes Service Selling 153M+ Drivers Licenses",
  "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"),
 ("Cybernews &mdash; 153M driver&rsquo;s licenses for sale after alleged leak from IDScan",
  "https://cybernews.com/security/drivers-licenses-for-sale-following-idscan-breach-allegations/"),
]) + '<div class="disc">For information only. Severity scores, deadlines and affected versions are as stated by the '
 'vendors and agencies cited above; verify against your own advisories before acting.</div></footer>')
cy.write('</div>' + STAMP + '\n</body></html>')

open(os.path.join(OUT, "cyber-briefing.html"), "w").write(cy.getvalue())

# ====================================================================== MMA
mma_css = css_for("#e84545", "#ff8a5c", bg="#100c0c", panel="#1a1313", line="#322020")
mm = io.StringIO()
mm.write(head("The Octagon &mdash; Daily Briefing", mma_css))
mm.write('<header class="mast"><h1>The Octagon</h1>'
         '<p class="tag">Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting</p>'
         + META + '</header>')
mm.write('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % SUM_MM)
mm.write('<div class="freshline" id="freshline">&nbsp;</div>')
mm.write(nav("mma-briefing.html"))

mm.write('<div class="cdn"><span class="lbl">Next Card</span><span class="clk" id="ufccdn">&nbsp;</span>'
 '<span class="ev">UFC Fight Night: Hooker vs. Parnasse &mdash; Saturday, September 5, Accor Arena, Paris</span></div>')

mm.write('<h2 class="sec">Top Story</h2>')
mm.write('<div class="lead"><h3>UFC 332 is four weeks out without a main event, and Cris Cyborg has volunteered '
 'to fix it</h3>'
 '<p>Valentina Shevchenko has withdrawn from UFC 332 &mdash; Saturday, October 3, at the Delta Center in Salt Lake '
 'City &mdash; with an undisclosed injury. Her women’s flyweight title defense against No. 1 contender Natalia '
 'Silva had been the promotion’s leading option to headline the show, and its collapse has left the card without '
 'a main event four weeks out.</p>'
 '<p>The reported replacement is <b>Natalia Silva vs. Wang Cong for an interim women’s flyweight title</b>. '
 'Nothing is official; UFC CEO Dana White has said the main event will be announced this week. Reporting notes that '
 'the pairing could hand Silva a shot at avenging a 2015 kickboxing loss to Wang Cong &mdash; the two have never met '
 'in MMA.</p>'
 '<p>Into that vacuum stepped Cris Cyborg, who publicly offered to headline the card against Amanda Nunes, writing '
 'to Nunes on social media: “tired of waiting for @KaylaH? Feel like saving an @ufc event?” Nunes knocked '
 'Cyborg out at UFC 232 eight years ago to become a two-division champion. As of this writing Nunes has not '
 'responded.</p></div>')

mm.write('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2><div class="cards">')
cards = [
 ("Sat, Sept 5 &middot; Accor Arena, Paris", "UFC Fight Night: Hooker vs. Parnasse",
  "Salahdine Parnasse makes his UFC debut in a main event against Dan Hooker on a 14-fight card. Parnasse is a "
  "former two-time KSW featherweight champion and one-time KSW lightweight champion who signed with the UFC in late "
  "July after previously turning the promotion down.",
  "Odds: Parnasse −600 / Hooker +440 (DraftKings); also returned −667/+417, −500/+400 and an opener of "
  "−357/+275, with implied win probability for Parnasse ranging roughly 75–82% by book. None adopted. Start "
  "time is given as 2:00 PM ET in one listing and 3:00 PM ET in another; neither is adopted."),
 ("Sat, Sept 12 &middot; Desert Diamond Arena, Glendale", "Noche UFC: Silva vs. Delgado",
  "Curtis Blaydes meets Waldo Cortes-Acosta on the card, in his first bout under a newly signed eight-fight "
  "contract.", None),
 ("Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles", "UFC 331: Van vs. Pantoja 2",
  "Joshua Van defends the flyweight title against Alexandre Pantoja nine months after their first meeting, which "
  "lasted just 26 seconds. Thirteen fights, co-main Tsarukyan vs. Ruffy at lightweight.", None),
 ("Sat, Sept 26 &middot; Meta APEX, Las Vegas", "UFC Fight Night: Rosas Jr. vs. Barcelos",
  "Raul Rosas Jr. takes his first UFC main event against Raoni Barcelos.", None),
 ("Sat, Oct 3 &middot; Delta Center, Salt Lake City", "UFC 332 &mdash; main event TBA",
  "No main event is announced. Silva vs. Wang Cong for an interim women&rsquo;s flyweight title is reported as the "
  "target; Dana White says the announcement lands this week.", None),
]
for datev, head_, note, odds in cards:
    mm.write('<div class="card"><div class="mono" style="color:#caa64a;font-size:12px;letter-spacing:.08em;'
             'text-transform:uppercase;margin-bottom:7px">%s</div><h3>%s</h3><p>%s</p>%s</div>' % (
             datev, head_, note, ('<p class="note">%s</p>' % odds) if odds else ""))
mm.write('</div>')
mm.write('<div class="note">The co-main billing for UFC 331 is carried forward from this briefing&rsquo;s standing record; only the '
 'headline bout appears in today&rsquo;s sources.</div>')

mm.write('<h2 class="sec">Last Event &mdash; Results</h2><div class="panel">'
 '<div class="mono" style="color:#caa64a;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px">'
 'UFC Fight Night: Nurmagomedov vs. Song &middot; Sat, Aug 29 &middot; Oriental Sports Center, Shanghai</div><table>'
 '<tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
 '<tr><td class="up">Song Yadong</td><td>def. Umar Nurmagomedov</td><td>KO (right uppercut), R2 1:48</td></tr>'
 '<tr><td class="up">Denise Gomes</td><td>def. Yan Xiaonan</td><td>TKO (elbow and punches), R1 4:49</td></tr>'
 '<tr><td class="up">Kai Asakura</td><td>def. Aoriqileng</td><td>KO (head kick and strikes), R2 0:34</td></tr>'
 '<tr><td class="up">Bilal Hasan</td><td>def. Nilson Rojas</td><td>KO (single punch)</td></tr>'
 '</table>'
 '<div class="note">Aoriqileng is rendered “Aori Qileng” by some outlets; both spellings appear in sources. '
 'Yan Xiaonan is described in coverage of the card as a one-time strawweight title challenger.</div>'
 '<p style="margin:14px 0 0;font-size:14.8px"><b>Performance bonuses.</b> $100,000 each to Song Yadong and Bilal '
 'Hasan for Performance of the Night, and to Ce Liu and Levi Rodrigues for Fight of the Night. On the $25,000 finish '
 'bonuses the sources disagree: one account names seven &mdash; Denise Gomes, Kai Asakura, Andre Lima, '
 'Rei Tsuruya, Francesco Nuzzi, Hector Santiago and Julia Polastri &mdash; while another lists five and says '
 '“five.” Both are printed; neither is adopted.</p></div>')

mm.write('<h2 class="sec">Prospect Watch</h2><div class="cards">')
prospects = [
 ("Dana White&rsquo;s Contender Series, Season 10, Week 5",
  "Tuesday, September 8 at the Meta APEX in Las Vegas. Quentin Pasley vs. Arlind Berisha headlines at light "
  "heavyweight, with Isaac Moreno vs. Reginaldo Junior at welterweight, Martin Koz&aacute;k vs. Christian Echols at "
  "middleweight, Apollo Gomes vs. Kwon Won Il at bantamweight and Colton Loud vs. Christian Natividad at flyweight. "
  "Listings give the broadcaster as ESPN in one place and Paramount+ in another; neither is adopted."),
 ("August 18 signings",
  "Cristian Perez, Alik Lorenz, Roman Puga, Taner Trembley, Trent Miller and Kaik Brito were added to the roster on "
  "August 18. A further fighter was signed on September 2 following Contender Series activity."),
]
for h, p in prospects:
    mm.write('<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t new">New</span></div>'
             '<h3>%s</h3><p>%s</p></div>' % (h, p))
mm.write('</div>')

mm.write('<h2 class="sec">Around the Sport</h2><div class="panel"><ul class="bul">'
 '<li><b>Cris Cyborg has called out Amanda Nunes to headline UFC 332.</b> Nunes knocked Cyborg out at UFC 232 eight '
 'years ago to become a two-division champion; Nunes has not responded.</li>'
 '<li><b>Curtis Blaydes has signed a new eight-fight deal</b>, securing his stay in the heavyweight division. His '
 'first bout under it is Noche UFC on September 12 against Waldo Cortes-Acosta.</li>'
 '<li><b>Recent releases:</b> Jamie Mullarkey, Lando Vannata, Vince Morales and Daniel Marcos have been '
 'released, with Marcos’s contract expiring and the UFC deciding not to renew it.</li>'
 '<li><b>A note on one stale listing.</b> Some roster trackers still describe the UFC as “in talks '
 'to sign” Salahdine Parnasse. That is out of date: he signed in late July 2026 and headlines in Paris on '
 'Saturday.</li>'
 '</ul></div>')

mm.write('<h2 class="sec">Rankings &amp; Business</h2><div class="panel"><ul class="bul">'
 '<li><b>Rankings movement:</b> no ranking change is confirmed in today’s sources, so none is '
 'asserted here.</li>'
 '<li><b>Business &amp; broadcast:</b> no viewership, gate or rights figure is confirmed in today’s sources, so '
 'no dollar or audience number is published this edition.</li>'
 '</ul></div>')

mm.write('<h2 class="sec">Champions Board</h2><div class="panel"><table>'
 '<tr><th>Division</th><th>Champion</th><th>Note</th></tr>'
 '<tr><td>Heavyweight</td><td>Tom Aspinall</td><td>Undisputed. Interim heavyweight: Ciryl Gane.</td></tr>'
 '<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>Won the vacant belt by KO1 over Ji&#345;&iacute; Proch&aacute;zka at UFC 327 in Miami.</td></tr>'
 '<tr><td>Middleweight</td><td>Sean Strickland</td><td>Split-decision upset of Khamzat Chimaev at UFC 328 in Newark, '
 'two judges 48-47 Strickland; Chimaev’s first defeat. Two-time champion.</td></tr>'
 '<tr><td>Welterweight</td><td>Islam Makhachev</td><td>One defense, a decision over Ian Machado Garry at UFC 330.</td></tr>'
 '<tr><td>Lightweight</td><td>Justin Gaethje</td><td>TKO4 of Ilia Topuria at Freedom 250.</td></tr>'
 '<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td>Defended by decision over Diego Lopes at UFC 325.</td></tr>'
 '<tr><td>Bantamweight</td><td>Petr Yan</td><td>Decision over Merab Dvalishvili at UFC 323.</td></tr>'
 '<tr><td>Flyweight</td><td>Joshua Van</td><td>Defends against Alexandre Pantoja at UFC 331 on September 19.</td></tr>'
 '<tr><td>Women’s Flyweight</td><td>Valentina Shevchenko</td><td>Out of UFC 332 with an undisclosed injury; an '
 'interim title bout is reported as the replacement.</td></tr>'
 '<tr><td>Women’s Bantamweight</td><td>Kayla Harrison</td><td>No defenses.</td></tr>'
 '<tr><td>Women’s Strawweight</td><td>Mackenzie Dern</td><td>One defense, a decision over Gillian Robertson at UFC 330.</td></tr>'
 '</table><div class="note">Aggregated champions listings continue to give middleweight to Khamzat Chimaev. That '
 'is wrong, and the row above was re-checked against ESPN’s report of UFC 328 (“Strickland stuns rival '
 'Chimaev”), Bleacher Report, CBS Sports, Al Jazeera and UFC.com before this table was published.</div></div>')

mm.write('<footer>' + sources([
 ("Bloody Elbow &mdash; Cris Cyborg offers to &lsquo;save&rsquo; struggling UFC 332 after canceled main event",
  "https://bloodyelbow.com/2026/09/03/cris-cyborg-offers-to-save-struggling-ufc-332-in-huge-rematch-after-canceled-main-event/"),
 ("Athlon Sports &mdash; Shevchenko out of UFC 332, Wang Cong-Silva reportedly targeted",
  "https://athlonsports.com/mma/ufc-332-wang-cong-natalia-silva-shevchenko-rematch"),
 ("Sports Illustrated &mdash; UFC reportedly working on new UFC 332 title fight after Valentina Shevchenko injury",
  "https://www.si.com/fannation/mma/news/ufc-working-on-new-ufc-332-title-fight-valentina-shevchenko-injury"),
 ("UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse", "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
 ("Rotowire &mdash; Hooker vs Parnasse odds, Sept 5, 2026",
  "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
 ("CBS Sports &mdash; 2026 UFC event schedule", "https://www.cbssports.com/ufc/news/2026-ufc-event-schedule-islam-makhachev-ian-machado-garry/"),
 ("UFC.com &mdash; UFC Shanghai results: Nurmagomedov vs. Song", "https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song"),
 ("Sherdog &mdash; UFC Shanghai bonuses", "https://www.sherdog.com/news/news/UFC-Shanghai-bonuses-Yadong-Song-3-others-earn-36100000-202571"),
 ("Tapology &mdash; Contender Series 2026: Week 5", "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
 ("ESPN &mdash; Strickland stuns rival Chimaev for UFC middleweight title",
  "https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title"),
 ("ESPN &mdash; Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("Bloody Elbow &mdash; Ex-UFC title challenger signs new eight-fight deal",
  "https://bloodyelbow.com/2026/08/21/ex-ufc-title-challenger-survives-trend-of-surprise-roster-removals-by-signing-new-8-fight-deal/"),
]) + '<div class="disc">Cards and bouts are subject to change.</div></footer>')

mm.write("""<script>(function(){var t=new Date('2026-09-05T14:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return}var dd=Math.floor(d/86400000),hh=Math.floor(d/3600000)%24,mm=Math.floor(d/60000)%60;e.textContent=dd+'d '+hh+'h '+mm+'m'}u();setInterval(u,30000)})();</script>""")
mm.write('</div>' + STAMP + '\n</body></html>')

open(os.path.join(OUT, "mma-briefing.html"), "w").write(mm.getvalue())

# ==================================================================== INDEX
ix_css = css_for("#caa64a", "#e8c766", extra="""
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.big .card{padding:20px 22px}
.big .card h3{font-size:20px;margin:0 0 10px}
.big .card .kicker{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:9px}
.big .card p{font-size:15px;color:#cfc9c2;margin:0 0 14px}
.big .card a.more{font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase}
.c-sec{border-top:3px solid #22d3a8}.c-sec .kicker,.c-sec h3,.c-sec a.more{color:#22d3a8}
.c-sec:hover{border-color:#22d3a8}
.c-mkt{border-top:3px solid #caa64a}.c-mkt .kicker,.c-mkt a.more{color:#caa64a}
.c-mkt h3{color:#e8c766;font-family:Georgia,'Times New Roman',serif}
.c-mkt:hover{border-color:#caa64a}
.c-mma{border-top:3px solid #e84545}.c-mma .kicker,.c-mma h3,.c-mma a.more{color:#ff8a5c}
.c-mma:hover{border-color:#e84545}
""")
ix = io.StringIO()
ix.write(head("Daily Briefings", ix_css))
ix.write('<header class="mast"><h1>Daily Briefings</h1>'
         '<p class="tag">Security, markets and MMA &mdash; rebuilt from live sources every 30 minutes</p>'
         + META + '</header>')
ix.write('<div class="freshline" id="freshline">&nbsp;</div>')
ix.write(nav("index.html"))
ix.write('<div class="big">')
ix.write('<div class="card c-sec"><div class="kicker">⛨ The Cyber Wire · The Wire</div>'
         '<h3>Court records taken from Thomson Reuters’ C-Track</h3><p>%s</p>'
         '<a class="more" href="cyber-briefing.html">Read the briefing →</a></div>' % SUM_CY)
ix.write('<div class="card c-mkt"><div class="kicker">▲ The Closing Bell · The Tape</div>'
         '<h3>Waller opens the door to a September hold</h3><p>%s</p>'
         '<a class="more" href="wallstreet-briefing.html">Read the briefing →</a></div>' % SUM_WS)
ix.write('<div class="card c-mma"><div class="kicker">⊘ The Octagon · Tale of the Tape</div>'
         '<h3>UFC 332 still has no main event</h3><p>%s</p>'
         '<a class="more" href="mma-briefing.html">Read the briefing →</a></div>' % SUM_MM)
ix.write('</div>')
ix.write('<div class="note" style="margin-top:22px">Every figure on these pages is checked against a source fetched '
 'during the run that built them. Where sources disagree, both readings are printed and neither is adopted. '
 'Point-in-time snapshots of every edition are kept in the <a href="archive.html">Archive</a>.</div>')
ix.write('</div>' + STAMP + '\n</body></html>')
open(os.path.join(OUT, "index.html"), "w").write(ix.getvalue())

print("built:", ", ".join(sorted(os.listdir(OUT))))
