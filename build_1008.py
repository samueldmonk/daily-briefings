# -*- coding: utf-8 -*-
"""Daily Briefings build - 2026-09-03 ~10:08 AM ET, Morning Edition, FIRST POST-OPEN run."""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shared

OUT = "/sessions/magical-nifty-noether/mnt/outputs"

TEAL, TEAL2 = "#22d3a8", "#36c6ff"
GOLD, GOLD2 = "#caa64a", "#e8c766"
RED,  RED2  = "#e84545", "#ff8a5c"
BG, PANEL, LINE = "#0d0f11", "#14181b", "#232a2e"
MBG, MPANEL, MLINE = "#100c0c", "#1a1313", "#322020"

FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'

def mast(h1, tagline):
    return ('<header class="mast"><h1>%s</h1><p class="tag">%s</p>%s</header>'
            % (h1, tagline, shared.META))

def tldr(label, text):
    return '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (label, text)

def card(title, body, tags=""):
    t = '<div class="tags">%s</div>' % tags if tags else ""
    return '<div class="card">%s<h3>%s</h3><p>%s</p></div>' % (t, title, body)

def tbl(headers, rows):
    h = "".join("<th>%s</th>" % x for x in headers)
    body = ""
    for r in rows:
        body += "<tr>" + "".join('<td%s>%s</td>' % ((' class="%s"' % c) if c else "", v)
                                 for v, c in r) + "</tr>"
    return ('<div class="panel" style="padding:5px 7px"><table><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (h, body))

def write(name, html):
    with io.open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, len(html))

# ============================== CYBER =========================================
CY_SOURCES = [
 ("BleepingComputer - Critical Langflow flaw exploited to steal OpenAI and AWS keys",
  "https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/"),
 ("Dark Reading - Critical Langflow Flaw Exploited as Attacks on AI Platform Rise",
  "https://www.darkreading.com/vulnerabilities-threats/critical-langflow-flaw-exploited-attacks-rise"),
 ("SecurityWeek - Hackers Start Exploiting Critical Langflow Vulnerability",
  "https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/"),
 ("Qualys ThreatPROTECT - Langflow RCE Exploited in Attacks (CVE-2026-0768)",
  "https://threatprotect.qualys.com/2026/09/02/langflow-remote-code-execution-vulnerability-exploited-in-attacks-cve-2026-0768/"),
 ("NVD - CVE-2026-0768 Detail", "https://nvd.nist.gov/vuln/detail/CVE-2026-0768"),
 ("CISA - Adds Seven Known Exploited Vulnerabilities to Catalog (Sept 2)",
  "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("CISA - Adds Two Known Exploited Vulnerabilities to Catalog (Aug 31)",
  "https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
 ("CISA - Known Exploited Vulnerabilities Catalog",
  "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("Rapid7 - Critical SonicWall SMA1000 Vulnerabilities Exploited in the Wild",
  "https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild/"),
 ("SOC Prime - CVE-2026-81578: Exploited PaperCut Auth Bypass",
  "https://socprime.com/blog/cve-2026-81578-analysis/"),
 ("SecurityAffairs - CISA adds PaperCut NG/MF flaws to KEV",
  "https://securityaffairs.com/198200/security/u-s-cisa-adds-papercut-ng-mf-flaws-to-its-known-exploited-vulnerabilities-catalog/"),
 ("GovInfoSecurity - Berlin Rejects Rhysida Ransomware Blackmail",
  "https://www.govinfosecurity.com/berlin-rejects-rhysida-ransomware-blackmail-a-32731"),
 ("SecurityAffairs - Rhysida Ransomware Group Targets Berlin Government Ahead of Vote",
  "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"),
 ("The Register - Legacy Lenovo login opens 5,000 Dropbox accounts to attackers",
  "https://www.theregister.com/security/2026/09/02/legacy-lenovo-login-opens-5000-dropbox-accounts-to-attackers/5293924"),
 ("Cybernews - Dropbox Lenovo Breach Let Hackers Access 5,000 Accounts",
  "https://cybernews.com/news/dropbox-accounts-breached-email-lenovo-id/"),
 ("Help Net Security - Global sinkhole operation ends Sality botnet's 23-year run",
  "https://www.helpnetsecurity.com/2026/09/02/sality-botnet-disruption-crowdstrike-law-enforcement/"),
 ("CrowdStrike - Inside the Sality Botnet Disruption Operation",
  "https://www.crowdstrike.com/en-us/blog/inside-sality-botnet-disruption-operation/"),
 ("The Record - Sality, one of the longest-running botnets, finally gets disrupted",
  "https://therecord.media/sality-botnet-cyber-doj"),
 ("SecurityWeek - Malicious Virtualizor Update Served via BGP Hijacking",
  "https://www.securityweek.com/malicious-virtualizor-update-served-via-bgp-hijacking/"),
 ("Virtualizor - Security Incident: BGP Hijacking",
  "https://www.virtualizor.com/blog/security-incident-bgp-hijacking/"),
 ("The Register - 33-hour BGP hijack of Softaculous traffic prompts security scramble",
  "https://www.theregister.com/security/2026/09/01/33-hour-bgp-hijack-of-softaculous-traffic-prompts-security-scramble/5293608"),
]

def cyber():
    b = []
    b.append(mast("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, exploits &amp; federal deadlines"))
    b.append(tldr("The Wire",
      "A critical Langflow flaw is being used to strip OpenAI, Anthropic and cloud API keys out of AI "
      "development servers, and five other actively exploited bugs must be remediated across federal "
      "networks by Saturday."))
    b.append(FRESH)
    b.append(shared.nav("cyber", TEAL))

    b.append('<div class="banner"><span class="lvl">Threat Level &middot; High</span>'
             '<span class="why">An unauthenticated root RCE in Langflow (CVE-2026-0768, CVSS 9.8) is under '
             'continuous exploitation for credential theft, and five separately exploited flaws &mdash; two of '
             'them scored 10.0 &mdash; carry a federal remediation deadline two days out.</span></div>')

    b.append('<div class="strip">'
      '<div class="stat"><div class="n">360+</div><div class="l">Langflow exploitation attempts against '
      "VulnCheck's UK canaries by Monday</div></div>"
      '<div class="stat"><div class="n">5.79 TB</div><div class="l">Data Rhysida claims it took from '
      "Berlin's state government</div></div>"
      '<div class="stat"><div class="n">15,000+</div><div class="l">Machines isolated in the Sality '
      'botnet sinkhole operation</div></div>'
      '<div class="stat"><div class="n">5,000</div><div class="l">Dropbox accounts reached through a '
      'legacy Lenovo ID sign-in</div></div>'
      '</div>')

    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="lead"><h3>Attackers are emptying AI development servers of their API keys '
      'through a critical Langflow flaw</h3>'
      '<p><b>CVE-2026-0768</b> carries a <b>CVSS 9.8</b> and allows unauthenticated arbitrary code execution '
      '<b>as root</b>: Langflow, an open-source low-code platform for building AI applications, fails to '
      'validate the <span class="mono">code</span> parameter of its validate endpoint before executing it as '
      'Python. The endpoint sits in the code validator behind the custom component editor.</p>'
      '<p>VulnCheck reports <b>continuous exploitation beginning August 29</b> &mdash; at least <b>50 attempts '
      'over the weekend</b> against honeypots in the U.K., and <b>more than 360 by Monday</b>, with attack '
      'traffic originating primarily from <b>Russia</b>. The behaviour is reconnaissance and credential '
      "harvesting rather than ransomware: reading Langflow's <span class=\"mono\">secret_key</span>, grepping "
      'environment variables for API keys and cloud credentials, hunting SSH keys and '
      '<span class="mono">.env</span> files, then moving laterally and exfiltrating source code.</p>'
      '<p>The stated objective is <b>OpenAI and Anthropic API keys, AWS, GCP and Azure credentials, and '
      'database connection strings</b>. Guidance from the reporting is blunt: any organisation running '
      'Langflow should <b>assume existing credentials are compromised and rotate every configured secret</b>. '
      'One outlet counts this as Langflow&rsquo;s twelfth exploited CVE.</p>'
      '<p class="note">CVE-2026-0768 does <b>not</b> appear among the vulnerabilities CISA added on August 31 '
      'or September 2, so no federal remediation deadline attaches to it. One aggregated return put roughly '
      '7,000 servers in scope; no source consulted for this edition states it directly, so it is not asserted here.</p></div>')

    b.append('<h2 class="sec">Patch Priority</h2>')
    b.append('<div class="callout crit"><div style="font-family:var(--mono);font-size:10.5px;'
      'letter-spacing:.15em;text-transform:uppercase;color:var(--crit);margin-bottom:6px">'
      'Do this first &middot; 2 days left</div>'
      '<h3>SonicWall SMA1000 &mdash; CVE-2026-83548 (CVSS 10.0), chained with CVE-2026-83549</h3>'
      '<p>SonicWall disclosed both flaws on September 1 as actively exploited. <b>CVE-2026-83548</b> is a '
      'critical <b>pre-authentication SSRF</b>; leveraging it, an attacker can reach <b>CVE-2026-83549</b>, an '
      'OS command injection in the Appliance Management Console, and <b>execute arbitrary OS commands without '
      'prior authentication</b>. <b>Kestra OSS CVE-2026-49869</b> is the other 10.0 in the same batch. Both '
      'were added to CISA KEV on <b>September 2</b> with a remediation date of '
      '<b>Saturday, September 5, 2026</b> &mdash; the same date carried in the federal-deadline list below.</p>'
      '</div>')

    b.append('<h2 class="sec">Threat Actor Spotlight</h2>')
    b.append('<div class="cards">' + card("MRXISBACK &mdash; routing as an attack surface",
      "Between <b>August 28 and 30</b> a threat actor Softaculous links to the handle <b>MRXISBACK</b> hijacked "
      "a block of the company's IP addresses. AS62390 (NexonHost) began announcing a more specific slice of "
      "Hetzner address space at roughly <b>20:57 UTC on August 28</b>, overriding normal routing. The attacker "
      "then routed domain validation through the hijacked network to obtain a <b>technically valid Let's "
      "Encrypt certificate</b> covering virtualizor.com, api.virtualizor.com and files.virtualizor.com &mdash; "
      "so diverted clients saw no TLS warning. A <b>malicious Virtualizor update package</b> was delivered to "
      "a small number of installations that checked for updates during the window. The incident ran roughly "
      "<b>33 hours</b> and touched update services, client billing areas and other Softaculous systems.",
      '<span class="t crit">BGP hijack</span><span class="t warn">Supply chain</span>'
      '<span class="t new">New</span>') + '</div>')

    b.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
    b.append('<div class="cards">')
    b.append(card("Berlin refuses to pay after Rhysida hits the city-state",
      "Rhysida attacked Berlin's state government weeks before an election. The group says it took "
      "<b>5.79 terabytes</b> &mdash; <b>46,500 contracts</b> plus emails, phone numbers, passwords and "
      "classified information &mdash; and is auctioning it from a starting price of <b>30 bitcoin "
      "($77,622)</b>. The leak occurred <b>August 7&ndash;12</b> and was discovered internally in mid-August. "
      "Officials <b>cut home-office access on Monday</b>: staff can send and receive email but cannot open VPN "
      "connections to internal networks, so they must work from office machines. Mayor <b>Kai Wegner</b> and "
      "interior senator <b>Iris Spranger</b> said jointly that &ldquo;the state of Berlin will not submit to "
      "extortion.&rdquo; Election infrastructure was not affected and no election data was compromised.",
      '<span class="t crit">Ransomware</span><span class="t">Government</span><span class="t new">New</span>'))
    b.append(card("A legacy Lenovo sign-in opened 5,000 Dropbox accounts",
      "From <b>August 4 to 21</b>, attackers reached at least <b>5,000 Dropbox accounts</b> holding nothing but "
      "the victims' <b>email addresses</b>. Lenovo's authentication let anyone register a Lenovo ID against any "
      "email address without verifying control of the inbox; because Dropbox accepted Lenovo ID as a sign-in "
      "path, that new identity bypassed the password entirely, and victims did not need a pre-existing Lenovo "
      "ID. About <b>a third of affected users had files viewed or downloaded</b>. Only accounts <b>without "
      "Dropbox's own 2FA</b> were exposed. Dropbox has terminated every Lenovo-ID session, disabled the "
      "integration outright, and now requires a native Dropbox password.",
      '<span class="t warn">Account takeover</span><span class="t">Identity</span><span class="t new">New</span>'))
    b.append(card("A 23-year-old botnet is sinkholed out of existence",
      "On <b>August 31</b> the U.S. Department of Justice, FBI, Defense Criminal Investigative Service, "
      "CrowdStrike, the Shadowserver Foundation and Europol disrupted <b>Sality</b>, a peer-to-peer botnet "
      "running since <b>2003</b> and used to deliver malware to more than <b>15,000 machines</b> worldwide "
      "&mdash; credential theft, spam, proxy services, network exploitation and DDoS. CrowdStrike's Counter "
      "Adversary Operations team turned the botnet's own peer-list mechanism against it, <b>stripping "
      "legitimate peers and substituting controlled sinkholes</b> so bots can no longer receive payload "
      "instructions. Shadowserver is working with ISPs and national CERTs to notify owners of infected devices.",
      '<span class="t ok">Takedown</span><span class="t">Botnet</span><span class="t new">New</span>'))
    b.append(card("PaperCut is on its third emergency patch",
      "PaperCut published an urgent advisory on <b>August 27</b> confirming it was investigating active "
      "exploitation of PaperCut NG and MF, and had shipped a <b>third emergency patch by September 1</b> after "
      "earlier fixes were bypassed. The two flaws chain: <b>CVE-2026-81578</b> (missing authentication for a "
      "critical function, CVSS v4.0 <b>8.8</b>) gives an unauthenticated attacker the ability to alter system "
      "configuration, and <b>CVE-2026-82078</b> (unsafe reflection, CVSS v4.0 <b>9.4</b>) uses that access to "
      "execute arbitrary Java bytecode on the application classpath under the PaperCut server process. Patches "
      "cover v24, v25 and v26. Both entered CISA KEV on <b>August 31</b>, due <b>September 14</b>.",
      '<span class="t crit">Exploited</span><span class="t warn">KEV</span>'))
    b.append('</div>')
    b.append('<p class="note"><b>Refused this run.</b> A search for current breaches returned the '
      '<b>IDMerit</b> identity-verification leak &mdash; roughly a billion KYC records &mdash; as though it '
      'were today&rsquo;s news. It is not: researchers found the unprotected MongoDB instance on '
      '<b>November 11, 2025</b>, it was secured the next day, and public disclosure came on '
      '<b>February 18, 2026</b>. It is not published here as current. The standing exclusion on the '
      'Pennsylvania Attorney General / INC Ransom incident (September <b>2025</b> coverage) also held for a '
      'third consecutive edition.</p>')

    b.append('<h2 class="sec">Vulnerability Watch</h2>')
    b.append(tbl(["CVE", "CVSS", "Affected", "Note"], [
      [("CVE-2026-0768", "mono"), ("9.8", "down"), ("Langflow &mdash; validate endpoint", ""),
       ("Unauthenticated RCE as root; exploited since Aug 29 for credential theft. Not among CISA's Aug 31 or Sept 2 additions.", "")],
      [("CVE-2026-83548", "mono"), ("10.0", "down"), ("SonicWall SMA1000", ""),
       ("Pre-auth SSRF; chains with 83549 for unauthenticated RCE. KEV Sept 2, due Sept 5.", "")],
      [("CVE-2026-83549", "mono"), ("7.8", ""), ("SonicWall SMA1000 &mdash; Appliance Management Console", ""),
       ("OS command injection reached via the SSRF above. KEV Sept 2, due Sept 5.", "")],
      [("CVE-2026-49869", "mono"), ("10.0", "down"), ("Kestra OSS", ""),
       ("OS command injection. KEV Sept 2, due Sept 5.", "")],
      [("CVE-2026-82329", "mono"), ("9.8", "down"), ("JFrog Artifactory (self-hosted)", ""),
       ("Improper authentication exploitable in the default configuration; SaaS unaffected. KEV Sept 2, due Sept 5.", "")],
      [("CVE-2026-9586", "mono"), ("9.3 (v4.0)", "down"), ("Sangoma Switchvox", ""),
       ("SQL injection. KEV Sept 2, due Sept 5.", "")],
      [("CVE-2026-82078", "mono"), ("9.4 (v4.0)", "down"), ("PaperCut NG/MF", ""),
       ("Unsafe reflection &rarr; arbitrary Java bytecode as the PaperCut server process. KEV Aug 31, due Sept 14.", "")],
      [("CVE-2026-81578", "mono"), ("8.8 (v4.0)", ""), ("PaperCut NG/MF", ""),
       ("Missing authentication for a critical function; unauthenticated config change. KEV Aug 31, due Sept 14.", "")],
      [("CVE-2026-48710", "mono"), ("Not stated in sources fetched", ""), ("Kludex Starlette", ""),
       ("HTTP request/response smuggling. KEV Sept 2, due Sept 16.", "")],
    ]))

    b.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
    b.append('<div class="panel"><ul class="bul">'
      '<li><b>Saturday, September 5</b> &mdash; <span class="down">2 days left</span>. Added <b>September 2</b>: '
      'Kestra OSS <span class="mono">CVE-2026-49869</span>, JFrog Artifactory '
      '<span class="mono">CVE-2026-82329</span>, Sangoma Switchvox <span class="mono">CVE-2026-9586</span>, and '
      'both SonicWall SMA1000 entries <span class="mono">CVE-2026-83548</span> and '
      '<span class="mono">CVE-2026-83549</span>.</li>'
      '<li><b>Monday, September 14</b> &mdash; 11 days left. Added <b>August 31</b>: PaperCut NG/MF '
      '<span class="mono">CVE-2026-81578</span> and <span class="mono">CVE-2026-82078</span>.</li>'
      '<li><b>Wednesday, September 16</b> &mdash; 13 days left. Added <b>September 2</b>: Kludex Starlette '
      '<span class="mono">CVE-2026-48710</span> and BerriAI LiteLLM '
      '<span class="mono">CVE-2026-59822</span>.</li>'
      '</ul><p class="note">Seven CVEs entered the catalogue in a single September 2 action, split across two '
      'due dates; the PaperCut pair came in separately on August 31. Countdowns are measured from today, '
      'September 3.</p></div>')

    b.append(shared.sources(CY_SOURCES))
    b.append('<p class="disc">Compiled from public reporting and vendor and government advisories fetched at '
      'build time. Severity scores follow the vendor or CISA figure where the two differ from third-party '
      'reporting. Nothing here is a substitute for your own vulnerability management process.</p></footer>')
    return shared.page("The Cyber Wire &mdash; Daily Briefing", TEAL, TEAL2, BG, PANEL, LINE, "\n".join(b))

# ============================== WALL STREET ===================================
TT = "https://s3.tradingview.com/external-embedding/embed-widget-"

TICKER = ('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
 '<script src="' + TT + 'ticker-tape.js" async>{"symbols":['
 '{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
 '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
 '{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
 '{"proName":"NASDAQ:NVDA","title":"NVIDIA"},'
 '{"proName":"NYSE:SNOW","title":"Snowflake"},'
 '{"proName":"NASDAQ:AVGO","title":"Broadcom"},'
 '{"proName":"NASDAQ:DDOG","title":"Datadog"},'
 '{"proName":"NYSE:CPB","title":"Campbell\'s"},'
 '{"proName":"TVC:USOIL","title":"WTI Crude"},'
 '{"proName":"TVC:US10Y","title":"US 10Y"}],'
 '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}'
 '</script></div>')

def quote(sym):
    return ('<div class="ticker"><script src="' + TT + 'single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}'
            '</script></div>' % sym)

WS_SOURCES = [
 ("Yahoo Finance - Stock market today: Dow, S&P 500, Nasdaq rise, yields fall (Thu Sept 3)",
  "https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-3-dow-sp-500-nasdaq-futures-081525933.html"),
 ("TheStreet - Stock Market Today (Sept. 3, 2026)",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-03-2026"),
 ("CNBC - Fed Governor Waller indicates he will support holding rates steady at September meeting",
  "https://www.cnbc.com/2026/09/03/fed-governor-waller-indicates-he-will-support-holding-rates-steady-at-september-meeting.html"),
 ("Washington Post - Fed's Waller says next rate move depends on upcoming inflation report",
  "https://www.washingtonpost.com/business/2026/09/03/inflation-federal-reserve-waller/e0f4cca2-a798-11f1-9e38-f705d048bd5a_story.html"),
 ("Investing.com - Fed's Waller open to leaving rates unchanged at September meeting",
  "https://www.investing.com/news/economy-news/feds-waller-open-to-leaving-rates-unchanged-at-september-meeting-4887866"),
 ("CNBC - Nvidia agrees to buy Hugging Face for almost $13 billion",
  "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html"),
 ("Fox Business - Nvidia to acquire Hugging Face for $12.9B",
  "https://www.foxbusiness.com/technology/nvidia-buy-ai-platform-hugging-face-nearly-13b"),
 ("Investing.com - Why is NVIDIA stock climbing today?",
  "https://www.investing.com/news/stock-market-news/why-is-nvidia-stock-climbing-today-93CH-4887980"),
 ("CNBC - Stocks making the biggest moves premarket: Snowflake, Moderna, Broadcom",
  "https://www.cnbc.com/2026/09/03/stocks-making-the-biggest-moves-premarket-snow-mrna-avgo.html"),
 ("Yahoo Finance - Snowflake stock skyrockets on AI-driven Q2 revenue jump",
  "https://finance.yahoo.com/markets/article/snowflake-stock-skyrockets-on-ai-driven-q2-revenue-jump-130537300.html"),
 ("Investing.com - Snowflake shares surge as AI demand powers growth, lifts outlook",
  "https://www.investing.com/news/stock-market-news/snowflake-shares-surge-as-ai-demand-powers-growth-lifts-outlook-4887223"),
 ("Broadcom - Announces Third Quarter Fiscal Year 2026 Financial Results",
  "https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial"),
 ("CNBC - Broadcom (AVGO) Q3 earnings report 2026",
  "https://www.cnbc.com/2026/09/02/broadcom-avgo-q3-earnings-report-2026.html"),
 ("Investing.com - Why is Datadog stock surging today?",
  "https://www.investing.com/news/stock-market-news/why-is-datadog-stock-surging-today-93CH-4887298"),
 ("The Globe and Mail - Stock Market News for Sep 2, 2026",
  "https://www.theglobeandmail.com/investing/markets/stocks/CVX/pressreleases/4395975/stock-market-news-for-sep-2-2026/"),
 ("Trading Economics - Brent oil price",
  "https://tradingeconomics.com/commodity/brent-crude-oil"),
 ("Trading Economics - US 10 Year Treasury Note Yield",
  "https://tradingeconomics.com/united-states/government-bond-yield"),
 ("Investing.com - US 10 Year Treasury Yield",
  "https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield"),
]

def wallstreet():
    b = []
    b.append(mast("The Closing Bell", "Your daily markets briefing &mdash; indices, movers, rates &amp; the calendar"))
    b.append(tldr("The Tape",
      "Stocks opened higher across the board after Fed Governor Christopher Waller said he could support "
      "holding rates steady this month, while Nvidia confirmed a deal for Hugging Face that sources value "
      "between $12.9 billion and roughly $14 billion depending on what is counted."))
    b.append(FRESH)
    b.append(shared.nav("ws", GOLD))
    b.append(TICKER)

    b.append('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>')
    b.append('<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD")
             + quote("FOREXCOM:DJI") + '</div>')
    b.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the '
             'latest edition; official closes are in the Weekly Scorecard.</div>')

    b.append('<h2 class="sec">The Lead</h2>')
    b.append('<div class="lead"><h3>Stocks open higher as Waller opens the door to a September hold '
      '&mdash; readings as of ~10:05&ndash;10:30 AM ET</h3>'
      '<p>Fed Governor <b>Christopher Waller</b> said Thursday that next week&rsquo;s inflation report will '
      'largely determine whether he supports a rate increase later this month. &ldquo;If this continues in the '
      'data due over the next two weeks, I would be inclined to support holding the target for the federal '
      'funds rate at its current setting,&rdquo; he said &mdash; while adding that if the August figures show '
      'recent progress has reversed, a hike at the <b>September 15&ndash;16 FOMC meeting</b> could be '
      'appropriate. August inflation data lands <b>September 11</b>.</p>'
      '<p>Markets moved on it: <b>Treasury yields dropped to session lows</b> and equity futures rose after the '
      'remarks, with traders dialling back September hike expectations to <b>roughly a coin flip</b> in fed '
      'funds futures and swaps. The tone reads as more dovish than Chair <b>Kevin Warsh</b>&rsquo;s Jackson '
      'Hole speech, which had pushed hike odds higher.</p>'
      '<p><b>Index readings differ by source and none is adopted here.</b> The Yahoo Finance live blog has the '
      '<b>S&amp;P 500 +0.57%, the Dow +0.80%, the Nasdaq +0.64% and the Russell 2000 +1.13%</b>; a second '
      'return gives <b>the Dow +0.8% with the S&amp;P 500 and Nasdaq Composite +0.5%</b>; a third has '
      '<b>the S&amp;P 500 +0.3% and the Dow +0.6%</b>; a fourth puts the <b>Nasdaq Composite +1%</b>. Every '
      'reading agrees on direction &mdash; higher. They are not all the same moment: some are pre-open '
      'readings and some are taken after the bell, and the sources do not all quote the same index, which '
      'is enough to account for the spread.</p>'
      '<p class="note">Nothing in this section is a closing price, and nothing in it is the current print. '
      'The percentages above were read between roughly <b>10:05 and 10:30 AM ET</b> and the market has '
      'traded since; the regular session runs to 4:00 PM ET. For the live number, use the streaming '
      'quotes at the top of this page; for the settled number, use the Weekly Scorecard below.</p></div>')

    b.append('<h2 class="sec">Movers &amp; Drivers</h2>')
    b.append('<div class="cards">')
    b.append(card("Nvidia buys Hugging Face",
      "Nvidia confirmed a definitive agreement for the open-source AI platform <b>Hugging Face</b>. The "
      "headline number is reported several ways and none is adopted here: Bloomberg and CNBC say <b>about "
      "$13 billion</b> / <b>almost $13 billion</b>; Fox Business and Variety say <b>$12.9 billion</b>; "
      "Investing.com gives <b>$12.93 billion plus roughly $1 billion in employee retention, about $14 billion "
      "all in</b>; CNBC breaks it out as <b>roughly $11.9 billion to shareholders plus up to $1 billion in "
      "equity-based retention awards</b>. Jensen Huang says Hugging Face will &ldquo;remain an open platform "
      "for the entire AI ecosystem.&rdquo; The platform counts <b>more than 18 million</b> developers, "
      "researchers and creators sharing <b>3 million+ models, 500,000 data sets and 1 million applications</b>. "
      "It is Nvidia's second-biggest purchase, after <b>$20 billion</b> for Groq assets at the end of last "
      "year. The stock was <b>+0.6% pre-open</b> on one reading and <b>+1% premarket</b> on another; JPMorgan "
      "reaffirmed Overweight and a <b>$320</b> price target.",
      '<span class="t new">New</span><span class="t ok">M&amp;A</span><span class="t">AI</span>'))
    b.append(card("Snowflake &mdash; a 24% move before the bell",
      "Shares were up <b>more than 24% pre-market</b> Thursday. That is a different window from Wednesday's "
      "after-hours move, reported at <b>22%</b> by CNBC and <b>23%</b> by Yahoo &mdash; two windows, not a "
      "range. Q2: adjusted <b>EPS $0.62 against a $0.45 consensus</b> on revenue of <b>$1.55 billion versus "
      "$1.48 billion expected</b>, up 35%; <b>product revenue +37% to $1.49 billion</b>. The FY2027 "
      "product-revenue guide went to <b>$6.07 billion from $5.84 billion</b>. AI products accounted for "
      "&ldquo;approximately half of the acceleration&rdquo;: coding assistant <b>Cortex Code passed 9,100 "
      "accounts</b> after adding more than 2,000 in the quarter, and enterprise chatbot <b>CoWork reached "
      "5,800 accounts</b>. At least <b>22 brokerages</b> raised targets, Wells Fargo to a Street-high "
      "<b>$525</b>.",
      '<span class="t ok">Earnings beat</span><span class="t">Software</span>'))
    b.append(card("Broadcom &mdash; a record quarter, a guide the market didn't like",
      "Fiscal Q3 revenue of <b>$29.6 billion, up 86%</b> year over year, with <b>AI semiconductor revenue of "
      "$16.7 billion, up 221% y/y and 54% q/q</b>, and record free cash flow of <b>$13.7 billion</b>. The "
      "fiscal Q4 guide is <b>$34.8 billion</b> &mdash; a 93% annual increase, but below a <b>$35.03 billion</b> "
      "consensus &mdash; with semiconductor revenue of $26.1 billion and AI semiconductors of $21.7 billion "
      "(+236%). Longer term the company points to <b>$58 billion</b> of AI revenue in fiscal 2026 and roughly "
      "<b>$115 billion</b> and <b>$230 billion</b> in fiscal 2027 and 2028. The stock read <b>-2.5% "
      "premarket</b> on CNBC's list and <b>-0.66%</b> in a later quote; two windows, neither adopted.",
      '<span class="t warn">Guidance</span><span class="t">Semis</span>'))
    b.append(card("Datadog rides the Snowflake read-across",
      "Up <b>5.7% pre-open</b> on nothing of its own &mdash; a sympathy move after Snowflake's report landed. "
      "The lift matters more than usual for Datadog: the shares had fallen roughly <b>22% over the prior "
      "month</b>.",
      '<span class="t new">New</span><span class="t">Sympathy move</span>'))
    b.append(card("Campbell's guides below the street",
      "Down <b>almost 7%</b> premarket after guiding fiscal 2027 EPS to <b>$1.65&ndash;$1.80</b> against a "
      "<b>$1.83</b> FactSet consensus.",
      '<span class="t down">Guidance cut</span><span class="t">Staples</span>'))
    b.append(card("Also on the premarket list",
      "<b>ServiceNow +3%</b> and <b>Hewlett Packard Enterprise -3%</b>, both from CNBC's premarket movers "
      "piece. Moderna appeared on an earlier edition's list on a Rothschild &amp; Co Redburn downgrade to "
      "sell, but no move for it is confirmed this morning, so it is not carried.",
      '<span class="t">Premarket</span>'))
    b.append('</div>')

    b.append('<h2 class="sec">Chart of the Day &mdash; Snowflake (NYSE:SNOW)</h2>')
    b.append('<div class="panel" style="padding:8px"><script src="' + TT + 'mini-symbol-overview.js" async>'
      '{"symbol":"NYSE:SNOW","width":"100%","height":240,"locale":"en","dateRange":"1D",'
      '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>')

    b.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
    b.append('<div class="panel" style="padding:8px"><script src="' + TT + 'stock-heatmap.js" async>'
      '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
      '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
      '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>')
    b.append('<p class="note"><b>Single-day sector breadth is refused for a fourteenth consecutive run.</b> The '
      'only same-session set returned describes sectors that <i>closed</i> higher and lower &mdash; a framing '
      'that cannot apply to a session still trading at 10 AM ET &mdash; so the figures cannot be attributed to '
      'any completed day and are not reprinted here. Year-to-date readings carried from earlier verified '
      'fetches: energy <b>+43%</b> and <b>XLE +42.32%</b> (both returned, neither adopted), '
      '<b>XLC -5.60%</b>, <b>XLY -3.02%</b>. The live heatmap above is the honest answer for today.</p>')

    b.append('<h2 class="sec">The Calendar &mdash; live</h2>')
    b.append('<div class="panel" style="padding:8px"><script src="' + TT + 'events.js" async>'
      '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
      '"importanceFilter":"0,1","countryFilter":"us"}</script></div>')

    b.append('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
    b.append('<div class="panel" style="padding:8px"><script src="' + TT + 'timeline.js" async>'
      '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
      '"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>')

    b.append('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2>')
    b.append(tbl(["Index", "Close (Wed, Sept 2)", "Change"], [
      [("S&amp;P 500", ""), ("7,666.60", "mono"), ("+0.46%", "up")],
      [("Nasdaq Composite", ""), ("26,217.83", "mono"), ("+0.45%", "up")],
      [("Dow Jones Industrial Average", ""), ("53,061.95", "mono"), ("+295.07 &nbsp;/&nbsp; +0.56%", "up")],
    ]))
    b.append('<p class="note">These three closes have now returned <b>identical on a ninth consecutive '
      'fetch</b>. One framing disagreement remains unresolved and unadopted: some accounts describe Wednesday '
      'as snapping a <b>two-day</b> losing streak and others a <b>three-day</b> one.</p>')

    b.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
    b.append(tbl(["Instrument", "Level", "Note"], [
      [("US 10-year Treasury", ""), ("4.820", "mono"),
       ("Prior close 4.796; day's range 4.765&ndash;4.820. Yields were reported <i>dropping to session lows</i> after Waller spoke, so this quote is not presented as the current print.", "")],
      [("10-year context", ""), ("&mdash;", "mono"),
       ("Described as the highest since <b>October 2023</b> in one account and since <b>November 2023</b> in another. Both printed, neither adopted.", "")],
      [("Brent crude", ""), ("$95.25", "mono"),
       ("-0.40%. A separate daily oil page had Brent at <b>$99.38</b> by 8 AM ET this morning. The roughly $4 gap is unresolved for a fifth consecutive edition; neither reading is adopted.", "")],
      [("WTI crude", ""), ("$90.76", "mono"),
       ("+0.60%, the September 2 close. A 9:05 AM quote showed $90.87 (+0.72%); earlier readings of $91.01, $90.51 and $89.62 are disclosed and none adopted.", "")],
      [("Fed funds", ""), ("Not confirmed", ""),
       ("No current target level is confirmed in today's reporting, so none is published. September hike odds are described as near a coin flip after Waller's remarks.", "")],
    ]))

    b.append('<h2 class="sec">On the Radar</h2>')
    b.append('<div class="panel"><ul class="bul">'
      '<li><b>Today, 8:30 AM ET &mdash; released.</b> Initial jobless claims came in at <b>206,000</b> for the '
      'week ending August 29, above the <b>205,000</b> consensus, against <b>204,000</b> the prior week, itself '
      'revised up from 203,000.</li>'
      '<li><b>Friday, September 4, 8:30 AM ET &mdash; August employment report.</b> Forecasts spread widely: '
      'consensus readings of <b>58,000</b> and <b>53,000</b>, Wells Fargo at <b>80,000</b>, Fifth Third at '
      '<b>-25,000</b>, unemployment held at <b>4.1%</b>. July payrolls were <b>-23,000</b> and Wednesday\'s ADP '
      'private payrolls came in at <b>+38,000</b>, fewer than expected.</li>'
      '<li><b>Friday, September 11 &mdash; August CPI.</b> Waller has made this report the explicit swing '
      'factor for his own vote.</li>'
      '<li><b>September 15&ndash;16 &mdash; FOMC</b>, with the decision on the 16th. Elevated energy prices '
      'have supported bets on a 25bp <b>hike</b> through the summer; softening labour data and today\'s Waller '
      'remarks have pulled the odds back toward even.</li>'
      '<li><b>Brent.</b> Two readings roughly $4 apart have now persisted across five editions without '
      'reconciling &mdash; worth watching for whichever one the market confirms.</li>'
      '</ul></div>')

    b.append(shared.sources(WS_SOURCES))
    b.append('<p class="disc">For information only. Nothing here is investment advice, a recommendation, or an '
      'offer to buy or sell any security. Intraday figures are snapshots taken at the time stated and will have '
      'moved; official closes are labelled as such.</p></footer>')
    return shared.page("The Closing Bell &mdash; Daily Briefing", GOLD, GOLD2, BG, PANEL, LINE,
                       "\n".join(b),
                       extra_css='.mast h1,.lead h3,h3{font-family:Georgia,"Times New Roman",serif}')

# ============================== MMA ===========================================
MMA_SOURCES = [
 ("Athlon Sports - Shevchenko Out of UFC 332, Wang Cong-Silva Reportedly Targeted",
  "https://athlonsports.com/mma/ufc-332-wang-cong-natalia-silva-shevchenko-rematch"),
 ("Sports Illustrated - UFC Reportedly Working on New UFC 332 Title Fight After Shevchenko Injury",
  "https://www.si.com/fannation/mma/news/ufc-working-on-new-ufc-332-title-fight-valentina-shevchenko-injury"),
 ("Bloody Elbow - Fans react to rumored replacement UFC 332 main event ahead of announcement",
  "https://bloodyelbow.com/2026/09/02/fans-react-to-rumored-replacement-ufc-332-main-event-ahead-of-announcement-nightmare-come-true/"),
 ("Yahoo Sports - UFC Champion Pulls Out Of UFC 332, Promotion Scrambles To Replace",
  "https://sports.yahoo.com/articles/ufc-champion-pulls-ufc-332-064218574.html"),
 ("UFC.com - UFC Fight Night: Hooker vs Parnasse (September 5, 2026)",
  "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
 ("UFCalendar - Next UFC Event and schedule", "https://www.ufcalendar.com/ufc/schedule"),
 ("Paramount+ - UFC Schedule 2026: Dates and Start Times",
  "https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/"),
 ("Rotowire - Hooker vs Parnasse Sep 5, 2026 Odds",
  "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
 ("MMA Odds Breaker - Opening Betting Odds for UFC Paris: Hooker vs. Parnasse",
  "https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/"),
 ("UFC.com - UFC Fight Night: Nurmagomedov vs Song (August 29, 2026)",
  "https://www.ufc.com/event/ufc-fight-night-august-29-2026"),
 ("UFC.com - Song Yadong KOs Umar Nurmagomedov In Round 2", "https://www.ufc.com/video/159691"),
 ("Bloody Elbow - Umar Nurmagomedov vs Song Yadong UFC Shanghai result",
  "https://bloodyelbow.com/2026/08/29/umar-nurmagomedov-vs-song-yadong-ufc-shanghai-result-khabibs-cousin-knocked-out-cold/"),
 ("ESPN - UFC Fight Night: Nurmagomedov vs. Song Fight Results",
  "https://www.espn.com/mma/fightcenter/_/id/600060620/league/ufc"),
 ("ESPN - Current and all-time UFC champions",
  "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("ESPN - Dana White's Contender Series: Season 10, Week 5",
  "https://www.espn.com/mma/fightcenter/_/id/600060736/league/ufc"),
 ("Tapology - Contender Series 2026: Week 5",
  "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
 ("Yahoo Sports - Dana White Says He Wants UFC Event in Hawaii",
  "https://sports.yahoo.com/articles/dana-white-says-wants-ufc-055314662.html"),
]

CDN_JS = """<script>(function(){var t=new Date('2026-09-05T19:00:00Z');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),h=Math.floor(d%864e5/36e5),m=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+h+'h '+m+'m';}u();setInterval(u,3e4);})();</script>"""

def mma():
    b = []
    b.append(mast("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    b.append(tldr("Tale of the Tape",
      "Valentina Shevchenko's injury has cost UFC 332 its main event, and the promotion is reportedly "
      "building an interim women's flyweight title fight between Natalia Silva and Wang Cong in its place."))
    b.append(FRESH)
    b.append(shared.nav("mma", RED))

    b.append('<div class="cdn"><span class="lbl">Next Card</span><span class="clk" id="ufccdn">&nbsp;</span>'
      '<span class="ev">UFC Fight Night: Hooker vs. Parnasse &middot; Sat, September 5 &middot; Accor Arena, '
      'Paris &middot; main card 3 PM ET, Paramount+</span></div>')

    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="lead"><h3>Shevchenko is out of UFC 332, and an interim women&rsquo;s flyweight '
      'title fight is reportedly being built to replace her</h3>'
      '<p>Women&rsquo;s flyweight champion <b>Valentina Shevchenko</b> has withdrawn from the <b>October 3</b> '
      'card at the <b>Delta Center in Salt Lake City</b> with an undisclosed injury. She had been set to defend '
      'the 125-pound title against top contender <b>Natalia Silva</b> &mdash; the bout reported as the '
      'promotion&rsquo;s leading option to headline UFC 332.</p>'
      '<p>In its place, the UFC is reportedly working on <b>Silva vs. Wang Cong for an interim women&rsquo;s '
      'flyweight championship</b>. As reported, the matchup &ldquo;could hand her a shot at avenging a 2015 '
      'kickboxing loss to Wang Cong.&rdquo;</p>'
      '<p><b>Nothing is official.</b> UFC CEO <b>Dana White</b> has said the main event will be announced this '
      'week; as of this edition the pairing has not been confirmed by the promotion.</p></div>')

    b.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
    b.append('<div class="cards">')
    b.append(card("Hooker vs. Parnasse",
      "<span class='mono' style='color:var(--accent2)'>Sat, Sept 5 &middot; Accor Arena, Paris</span><br>"
      "<b>Dan Hooker vs. Salahdine Parnasse</b>, lightweight, with the main card at <b>3 PM ET</b> on "
      "Paramount+. Parnasse is a <b>UFC debutant</b> given a main event on arrival: a former <b>two-time KSW "
      "featherweight and one-time KSW lightweight champion</b> who signed with the promotion in late July 2026 "
      "after previously turning it down. <b>Odds: Parnasse -600 / Hooker +440 (DraftKings)</b>; the same fight "
      "also returns -667/+417 and -625/+450 elsewhere, against an opener of -357/+275 &mdash; an <b>81.8% "
      "implied probability</b> for Parnasse with the vig removed. All printed, none adopted.",
      '<span class="t crit">Main event</span><span class="t">Lightweight</span>'))
    b.append(card("Noche UFC: Silva vs. Delgado",
      "<span class='mono' style='color:var(--accent2)'>Sat, Sept 12 &middot; Desert Diamond Arena, Glendale</span><br>"
      "Delgado stepped in for an injured <b>Yair Rodr&iacute;guez</b>, announced August 22. Also on the card: "
      "<b>Cortes-Acosta vs. Blaydes</b>, <b>Fiorot vs. Grasso</b> and <b>Moreno vs. Morales</b>.",
      '<span class="t">Fight Night</span>'))
    b.append(card("UFC 331: Van vs. Pantoja 2",
      "<span class='mono' style='color:var(--accent2)'>Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</span><br>"
      "Flyweight champion <b>Joshua Van</b> rematches <b>Alexandre Pantoja</b>, the man he took the belt from. "
      "Main card <b>9 PM ET / 6 PM PT</b> on Paramount+; the co-main is <b>Tsarukyan vs. Ruffy</b> over five "
      "rounds at lightweight. Thirteen fights.",
      '<span class="t crit">Title fight</span><span class="t">Numbered card</span>'))
    b.append(card("Rosas Jr. vs. Barcelos",
      "<span class='mono' style='color:var(--accent2)'>Sat, Sept 26 &middot; Meta APEX, Las Vegas</span><br>"
      "<b>Raul Rosas Jr.</b>, 21, gets his first UFC main event against <b>Raoni Barcelos</b> across an "
      "18-year age gap. The <i>TUF: Team Cormier vs. Team Bisping</i> bantamweight and women's strawweight "
      "finals are also on the card. <b>Start time is unresolved</b>: current listings give a <b>6 PM ET / "
      "3 PM PT</b> main card, against an <b>8 PM ET</b> listing carried earlier today. Both printed, neither adopted.",
      '<span class="t">Fight Night</span><span class="t new">New</span>'))
    b.append(card("UFC 332",
      "<span class='mono' style='color:var(--accent2)'>Sat, Oct 3 &middot; Delta Center, Salt Lake City</span><br>"
      "Main event <b>to be announced</b> following Shevchenko's withdrawal &mdash; see the top story. Dana "
      "White says the announcement lands this week.",
      '<span class="t warn">Main event TBA</span>'))
    b.append('</div>')

    b.append('<h2 class="sec">Last Event &mdash; Results</h2>')
    b.append('<p style="font-size:14.5px;color:#cfc9c2;margin:0 0 11px"><b>UFC Fight Night: Nurmagomedov vs. '
      'Song</b> &middot; Sat, August 29, 2026 &middot; Oriental Sports Center, Shanghai.</p>')
    b.append(tbl(["Result", "Bout", "Method"], [
      [("Song Yadong", "up"), ("def. Umar Nurmagomedov", ""), ("KO (right uppercut), R2 1:48", "")],
      [("Denise Gomes", "up"), ("def. Yan Xiaonan", ""), ("TKO (elbow and punches), R1 4:49", "")],
      [("Kai Asakura", "up"), ("def. Aoriqileng", ""), ("KO (head kick and strikes), R2 0:34", "")],
    ]))
    b.append('<p class="note">Only bouts confirmed against the event&rsquo;s own results pages are listed; no claim is made here about how '
      'deep the card ran. Nurmagomedov entered a <b>-600</b> favourite. Song called for the belt afterwards '
      '&mdash; &ldquo;Who&rsquo;s next, Uncle Dana? Give me the title shot!&rdquo; Gomes&rsquo; win was her '
      'fifth straight, the longest active streak at 115 lb, and <b>ties Jessica Andrade for the most KO wins in '
      'UFC strawweight history at four</b>. &ldquo;Aoriqileng&rdquo; is rendered &ldquo;Aori Qileng&rdquo; in '
      'some listings.</p>')
    b.append('<div class="panel"><b style="font-family:var(--mono);font-size:11px;letter-spacing:.15em;'
      'text-transform:uppercase;color:var(--accent)">Performance bonuses</b>'
      '<p style="margin:8px 0 0;font-size:14.5px"><b>$400,000</b> across the awards. <b>$100,000</b> each to '
      '<b>Song Yadong</b> and <b>Bilal Hasan</b> for Performance of the Night and to <b>Ce Liu</b> and '
      '<b>Levi Rodrigues Jr.</b> for Fight of the Night; <b>$25,000</b> finish bonuses to <b>Hector Santiago, '
      'Francesco Nuzzi, Rei Tsuruya, Kai Asakura</b> and <b>Denise Gomes</b> &mdash; five names against a '
      'source that says five.</p></div>')

    b.append('<h2 class="sec">Prospect Watch</h2>')
    b.append('<p style="font-size:14.5px;color:#cfc9c2;margin:0 0 11px"><b>Dana White&rsquo;s Contender '
      'Series, Season 10, Week 5</b> &middot; Tuesday, September 8 &middot; Meta APEX, Las Vegas.</p>')
    b.append('<div class="cards">')
    b.append(card("Quentin Pasley (3-0) vs. Arlind Berisha (5-0)",
      "Light heavyweight, and the headliner &mdash; both undefeated. Pasley arrives off a highlight-reel "
      "<b>flying-knee finish of Reylan Gracie</b>; Berisha is from Albania.",
      '<span class="t ok">Prospect</span><span class="t">205 lb</span>'))
    b.append(card("Isaac Moreno (8-0) vs. Reginaldo Geraldo Jr. (11-1)",
      "Welterweight. Moreno fights as &ldquo;Primetime&rdquo;.",
      '<span class="t ok">Prospect</span><span class="t">170 lb</span>'))
    b.append(card("Martin Kozak (6-0) vs. Christian Echols (8-4)",
      "Middleweight. Kozak is billed &ldquo;CEO&rdquo;, Echols &ldquo;The Vanilla Gorilla&rdquo;.",
      '<span class="t ok">Prospect</span><span class="t">185 lb</span>'))
    b.append(card("Apollo Gomes (12-2) vs. Won Il Kwon (14-6)",
      "Bantamweight. Gomes fights as &ldquo;Deus da Guerra&rdquo;, Kwon as &ldquo;Pretty Boy&rdquo;.",
      '<span class="t ok">Prospect</span><span class="t">135 lb</span>'))
    b.append(card("Colton Loud (7-1) vs. Christian Natividad (9-0)",
      "Flyweight. <b>Natividad stepped in on short notice</b> after Loud's original opponent withdrew over a "
      "visa issue.",
      '<span class="t ok">Prospect</span><span class="t warn">Short notice</span>'))
    b.append('</div>')
    b.append('<p class="note">Broadcast listings disagree on the outlet &mdash; ESPN in one, Paramount+ in '
      'another, both at 7:00 PM. Printed, neither adopted. Remaining Season 10 dates: <b>September 15, 22 and '
      '29</b>. Week 4 (September 1) handed out contracts to <b>Adam Darby, Modestino Rodrigues, Silvestre '
      'Sanchez, Gabriel Louren&ccedil;o</b> (rendered &ldquo;Lorenco&rdquo; elsewhere) and <b>Adam '
      'Livingston</b>, by split decision on a second appearance.</p>')

    b.append('<h2 class="sec">Around the Sport</h2>')
    b.append('<div class="panel"><ul class="bul">'
      '<li><b>Dana White wants Hawaii.</b> Speaking on <i>The Rich Eisen Show</i>, White called the island '
      'state his most desired destination for a UFC card, while acknowledging the practical obstacles that '
      'have kept the promotion from making the trip.</li>'
      '<li><b>Song Yadong is campaigning in public.</b> His post-fight callout in Shanghai &mdash; '
      '&ldquo;Who&rsquo;s next, Uncle Dana? Give me the title shot!&rdquo; &mdash; stakes a claim to the next '
      'bantamweight title shot against champion Petr Yan.</li>'
      '<li><b>UFC 332 needs a main event this week.</b> Whatever is announced sets the tone for the October '
      'pay-per-view calendar, and an interim belt at 125 lb would be the first women&rsquo;s interim title '
      'in the division.</li>'
      '</ul></div>')

    b.append('<h2 class="sec">Rankings &amp; Business</h2>')
    b.append('<div class="panel"><ul class="bul">'
      '<li><b>Rankings movement.</b> <b>Song Yadong moved from 7 to 4 at bantamweight</b> on ESPN\'s list after '
      'Shanghai, taking Umar Nurmagomedov\'s place. That move was confirmed earlier today and stands; '
      'no other ranking is asserted here.</li>'
      '<li><b>Broadcast.</b> Paramount is in year one of a <b>seven-year, $7.7 billion</b> rights deal with '
      'TKO &mdash; an average of about <b>$1.1 billion a year</b>, against roughly <b>$550 million a year</b> '
      'under the previous ESPN arrangement.</li>'
      '<li><b>Structure.</b> All <b>43 annual UFC live events</b> stream exclusively on Paramount+, with '
      '<b>30 Fight Nights and 13 marquee events</b> a year across CBS and Paramount+. The pay-per-view model '
      'ends.</li>'
      '<li>No gate or viewership figure is confirmed for the current cards, so none is printed.</li>'
      '</ul></div>')

    b.append('<h2 class="sec">Champions Board</h2>')
    b.append(tbl(["Division", "Champion", "Note"], [
      [("Heavyweight", ""), ("Tom Aspinall", ""), ("Undisputed. <b>Interim:</b> Ciryl Gane, KO2 over Alex Pereira at Freedom 250, June 14, 2026.", "")],
      [("Light Heavyweight", ""), ("Carlos Ulberg", ""), ("KO1 at 3:45 over Ji&#345;&iacute; Proch&aacute;zka for the <b>vacant</b> belt at UFC 327, Kaseya Center, Miami. Date recorded as April 11 in the standing record and April 12 in one report; unresolved.", "")],
      [("Middleweight", ""), ("Sean Strickland", ""), ("Split decision over Khamzat Chimaev at UFC 328, Prudential Center, Newark, May 9, 2026. Two-time champion.", "")],
      [("Welterweight", ""), ("Islam Makhachev", ""), ("1 defence &mdash; UD over Ian Machado Garry, UFC 330, Aug 15, 2026; a 17th straight UFC win.", "")],
      [("Lightweight", ""), ("Justin Gaethje", ""), ("TKO4 over Ilia Topuria at Freedom 250, June 14, 2026.", "")],
      [("Featherweight", ""), ("Alexander Volkanovski", ""), ("Defended by UD over Diego Lopes at UFC 325; ties Jos&eacute; Aldo at eight featherweight title defences.", "")],
      [("Bantamweight", ""), ("Petr Yan", ""), ("UD over Merab Dvalishvili, UFC 323, Dec 6, 2025.", "")],
      [("Flyweight", ""), ("Joshua Van", ""), ("1 defence. Rematches Alexandre Pantoja at UFC 331 on September 19.", "")],
      [("Women's Flyweight", ""), ("Valentina Shevchenko", ""), ("<b>Out of UFC 332 with an undisclosed injury</b>; an interim title bout is reportedly being built &mdash; see the top story.", "")],
      [("Women's Bantamweight", ""), ("Kayla Harrison", ""), ("0 defences. The UFC 324 defence vs Amanda Nunes was cancelled after Harrison withdrew for neck surgery.", "")],
      [("Women's Strawweight", ""), ("Mackenzie Dern", ""), ("1 defence &mdash; UD over Gillian Robertson, UFC 330, Aug 15, 2026.", "")],
    ]))
    b.append('<p class="note">Every cell was cross-checked against ESPN&rsquo;s current-champions page for this '
      'edition, and all eleven names on that page matched &mdash; notable, because aggregated summaries have '
      'repeatedly returned a stale middleweight or light heavyweight. The interim heavyweight row is not on '
      'ESPN&rsquo;s list and comes from the separately verified record of Freedom 250.</p>')

    b.append(shared.sources(MMA_SOURCES))
    b.append('<p class="disc">Cards and bouts are subject to change. Odds move constantly and are shown with '
      'the book that quoted them; where books disagree, every reading is printed and none is adopted.</p></footer>')
    return shared.page("The Octagon &mdash; Daily Briefing", RED, RED2, MBG, MPANEL, MLINE,
                       "\n".join(b), extra_js=CDN_JS)

# ============================== INDEX =========================================
IX_CSS = """
.big{display:grid;grid-template-columns:1fr;gap:15px;margin-top:6px}
@media(min-width:820px){.big{grid-template-columns:repeat(3,1fr)}}
.bcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 21px;
  display:flex;flex-direction:column;transition:transform .16s,border-color .16s,box-shadow .16s}
.bcard:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.35)}
.bcard .kick{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;
  margin-bottom:9px}
.bcard h3{margin:0 0 10px;font-size:20px;line-height:1.25}
.bcard p{margin:0 0 16px;font-size:14.5px;color:#cfc9c2;flex:1}
.bcard a.go{font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase}
.c-cy{border-top:3px solid #22d3a8} .c-cy .kick,.c-cy a.go{color:#22d3a8}
.c-cy:hover{border-color:#22d3a8}
.c-ws{border-top:3px solid #caa64a} .c-ws .kick,.c-ws a.go{color:#caa64a}
.c-ws:hover{border-color:#caa64a} .c-ws h3{font-family:Georgia,"Times New Roman",serif}
.c-mm{border-top:3px solid #e84545} .c-mm .kick,.c-mm a.go{color:#e84545}
.c-mm:hover{border-color:#e84545}
"""

def index():
    b = []
    b.append(mast("Daily Briefings",
                  "Three desks, refreshed every 30 minutes &mdash; security, markets and the fight game"))
    b.append(FRESH)
    b.append(shared.nav("index", GOLD))
    b.append('<div class="big">')
    b.append('<div class="bcard c-cy"><div class="kick">&#9960; The Cyber Wire &middot; The Wire</div>'
      '<h3>AI dev servers are being emptied of their API keys</h3>'
      '<p>A critical Langflow flaw is being used to strip OpenAI, Anthropic and cloud API keys out of AI '
      'development servers, and five other actively exploited bugs must be remediated across federal networks '
      'by Saturday.</p><a class="go" href="cyber-briefing.html">Read the briefing &rarr;</a></div>')
    b.append('<div class="bcard c-ws"><div class="kick">&#9650; The Closing Bell &middot; The Tape</div>'
      '<h3>Waller opens the door to a September hold</h3>'
      '<p>Stocks opened higher across the board after Fed Governor Christopher Waller said he could support '
      'holding rates steady this month, while Nvidia confirmed a deal for Hugging Face that sources value '
      'between $12.9 billion and roughly $14 billion depending on what is counted.</p>'
      '<a class="go" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>')
    b.append('<div class="bcard c-mm"><div class="kick">&#8856; The Octagon &middot; Tale of the Tape</div>'
      '<h3>UFC 332 loses its main event</h3>'
      "<p>Valentina Shevchenko's injury has cost UFC 332 its main event, and the promotion is reportedly "
      "building an interim women's flyweight title fight between Natalia Silva and Wang Cong in its place.</p>"
      '<a class="go" href="mma-briefing.html">Read the briefing &rarr;</a></div>')
    b.append('</div>')
    b.append('<footer><div style="font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;'
      'text-transform:uppercase;color:var(--muted);margin-bottom:6px">About</div>'
      '<p style="font-size:13px;color:var(--muted);margin:0">Each briefing is rebuilt from live web searches '
      'every 30 minutes between 8 AM and 6 PM ET, and every claim is checked against a source fetched in that '
      'run. Point-in-time snapshots of past editions are kept in the '
      '<a href="archive.html">Archive</a>.</p>'
      '<p class="disc">Information only. The markets briefing is not investment advice; the security briefing '
      'is not a substitute for your own vulnerability management; fight cards are subject to change.</p>'
      '</footer>')
    return shared.page("Daily Briefings", GOLD, GOLD2, BG, PANEL, LINE, "\n".join(b), extra_css=IX_CSS)


if __name__ == "__main__":
    write("index.html", index())
    write("cyber-briefing.html", cyber())
    write("wallstreet-briefing.html", wallstreet())
    write("mma-briefing.html", mma())
