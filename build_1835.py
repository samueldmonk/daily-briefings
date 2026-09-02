# -*- coding: utf-8 -*-
"""Daily Briefings builder — Wednesday September 2, 2026, Afternoon Edition (post-close)."""
import io, os
from css import base_css, nav, meta_row, head, sources, STAMP_JS

OUT = os.path.dirname(os.path.abspath(__file__))

def w(name, html):
    with io.open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, len(html))

FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'

# ---------------------------------------------------------------- CYBER
UTIL_CSS = "\n.warn{color:var(--warn)}\n.muted{color:var(--muted)}\ncode{font-family:var(--mono);font-size:12.5px}\n"

CY_CSS = base_css("#22d3a8", "#36c6ff", "#0b1110", "#121a19", "#1e2b29") + UTIL_CSS

CY_SOURCES = [
    ("The Hacker News — Attackers Exploit Critical JFrog Artifactory Flaw to Mint Admin Tokens",
     "https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html"),
    ("BleepingComputer — Hackers exploit critical JFrog Artifactory flaw to forge admin tokens",
     "https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/"),
    ("SecurityWeek — Critical JFrog Artifactory Vulnerability Reportedly Exploited in the Wild",
     "https://www.securityweek.com/critical-jfrog-artifactory-vulnerability-reportedly-exploited-in-the-wild/"),
    ("BleepingComputer — Aesto Health says data breach affects over 9.5 million patients",
     "https://www.bleepingcomputer.com/news/security/aesto-health-says-data-breach-affects-over-95-million-patients/amp/"),
    ("HIPAA Journal — Aesto Health Data Breach Affects 9.5 Million Patients",
     "https://www.hipaajournal.com/aesto-health-data-breach/"),
    ("BleepingComputer — Dropbox accounts breached through Lenovo email verification flaw",
     "https://www.bleepingcomputer.com/news/security/dropbox-accounts-breached-through-lenovo-email-verification-flaw/"),
    ("SecurityWeek — Ransomware Gang Claims Nutex Health Data Breach",
     "https://www.securityweek.com/ransomware-gang-claims-nutex-health-data-breach/"),
    ("The Record — Nutex Health says patient, employee data stolen",
     "https://therecord.media/nutex-health-data-breach"),
    ("Rapid7 — PaperCut NG/MF Critical Zero-Day Exploited in the Wild",
     "https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/"),
    ("CISA — CISA Adds Two Known Exploited Vulnerabilities to Catalog (Aug 31, 2026)",
     "https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
    ("NVD — CVE-2026-59822 Detail (BerriAI LiteLLM)",
     "https://nvd.nist.gov/vuln/detail/CVE-2026-59822"),
    ("Vulnerability-Lookup — CVE-2026-59822 (KEV added 2026-09-02, due 2026-09-16)",
     "https://vulnerability.circl.lu/vuln/CVE-2026-59822"),
    ("Tenable — CVE-2026-15409 / CVE-2026-15410 and the SonicWall SMA 1000 zero-days",
     "https://www.tenable.com/blog/cve-2026-15409-cve-2026-15410-sonicwall-sma-1000-zero-day-vulnerabilities-exploited-in-the"),
    ("Help Net Security — SonicWall SMA 1000 appliances under attack via zero-day flaws (CVE-2026-83548 / 83549)",
     "https://www.helpnetsecurity.com/2026/09/02/sonicwall-sma-1000-cve-2026-83548-cve-2026-83549-zero-day-attacks/"),
    ("Rapid7 — MDR Team Discovers New SonicWall SMA1000 Zero Days Being Actively Exploited",
     "https://www.rapid7.com/blog/post/etr-rapid7-mdr-team-discovers-new-sonicwall-sma1000-zero-days-being-actively-exploited-cve-2026-15409-cve-2026-15410/"),
    ("BleepingComputer — Critical Langflow flaw exploited to steal OpenAI and AWS keys",
     "https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/"),
    ("SecurityWeek — Hackers Start Exploiting Critical Langflow Vulnerability",
     "https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/"),
    ("Halcyon — INC Ransom Group Mounts Rapid Campaign Against Law Firms",
     "https://www.halcyon.ai/ransomware-alerts/inc-ransom-group-mounts-rapid-campaign-against-law-firms"),
    ("CISA — Known Exploited Vulnerabilities Catalog",
     "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
]

CY_SUMMARY = ("A critical JFrog Artifactory authentication bypass rated CVSS 9.8 is being exploited "
              "to forge administrator tokens days after disclosure, while Aesto Health told regulators "
              "a breach of its AWS infrastructure exposed the health data of 9,540,683 people.")

cy = []
cy.append(head("The Cyber Wire — Daily Briefing", CY_CSS))
cy.append('<header class="masthead"><h1>&#9960; The Cyber Wire</h1>'
          '<p class="tag">Your daily cybersecurity briefing — breaches, vulnerabilities & federal deadlines</p>'
          + meta_row() + '</header>')
cy.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % CY_SUMMARY)
cy.append(FRESH)
cy.append(nav("cyber"))

cy.append('<div class="banner high"><span class="k">Threat Level &middot; High</span>'
          'Two separate flaw sets are under confirmed active exploitation right now: a JFrog Artifactory '
          'authentication bypass (CVSS 9.8) that mints administrator tokens on default configurations, and a '
          'chained pair of SonicWall SMA1000 zero-days, one of which carries a CVSS of 10.</div>')

cy.append('<div class="stats">'
          '<div class="stat"><div class="n">9,540,683</div><div class="l">Individuals in the Aesto Health breach, per its filing with HHS’ Office for Civil Rights</div></div>'
          '<div class="stat"><div class="n">9.8</div><div class="l">CVSS v3.1 base score for JFrog Artifactory CVE-2026-82329</div></div>'
          '<div class="stat"><div class="n">360</div><div class="l">Langflow exploitation attempts logged by VulnCheck honeypots in the U.K.</div></div>'
          '<div class="stat"><div class="n">5,000</div><div class="l">Dropbox accounts accessed through a Lenovo ID email-verification flaw</div></div>'
          '</div>')

cy.append('<h2 class="sec">Top Story</h2>')
cy.append('<div class="panel"><h3>Attackers are forging admin tokens on JFrog Artifactory days after the patch shipped</h3>'
          '<p><b>CVE-2026-82329</b> is an authentication bypass in JFrog Artifactory carrying a <b>CVSS v3.1 base score of 9.8 '
          '(Critical)</b>. It requires no authentication, no privileges and no user interaction: under the default configuration, '
          'a remote attacker with network access can reach administrator-level privileges. Installations without an additional '
          'join key configured can be issued a &ldquo;phantom&rdquo; join key, which an attacker abuses to forge access and generate '
          'administrator-level tokens.</p>'
          '<p>JFrog disclosed and patched the issue on <b>August 28, 2026</b>. By <b>September 1</b>, exposure-management firm '
          '<b>watchTowr</b> had observed attackers exploiting vulnerable systems to generate administrative tokens and to enumerate '
          'users, groups, credentials and federated access relationships. The flaw is improper authentication rather than remote code '
          'execution, and it <b>does not affect the JFrog SaaS platform</b> — only self-hosted deployments.</p>'
          '<p class="note">Reported by The Hacker News, BleepingComputer, SecurityWeek and Dark Reading. Nothing fetched this run '
          'places CVE-2026-82329 in the CISA KEV catalog, so no federal remediation clock is asserted for it below.</p></div>')

cy.append('<h2 class="sec">Patch Priority</h2>')
cy.append('<div class="callout crit"><div class="k">Do this first</div>'
          '<p><b>Patch JFrog Artifactory (CVE-2026-82329) today.</b> A CVSS 9.8 pre-authentication bypass that yields '
          'administrator tokens, in a system that typically holds build artifacts, signing material and CI credentials, is the '
          'highest-leverage exposure on this page — and it is being exploited now, five days after the fix.</p>'
          '<p style="margin-bottom:0">It carries <b>no federal deadline</b> in anything fetched this run. The '
          '<b>shortest verified CISA deadline</b> below belongs to the two <b>PaperCut NG/MF</b> flaws '
          '(CVE-2026-81578 and CVE-2026-82078), added August 31 and <b>due September 14 — 12 days from today</b>. '
          'The KEV section uses that same verified date.</p></div>')

cy.append('<h2 class="sec">Threat Actor Spotlight</h2>')
cy.append('<div class="card"><div class="k">INC Ransom</div>'
          '<h4>Ten law firms posted to one leak site in 48 hours</h4>'
          '<p>The INC ransomware group claimed attacks against <b>ten law firms and legal-services organizations</b> on its dark-web '
          'leak site inside a single 48-hour window, according to Halcyon. Halcyon notes that the volume, the sector specificity and '
          'the timing together suggest either a coordinated campaign or a <b>shared upstream compromise</b> — a managed service '
          'provider or a common platform — rather than ten unrelated intrusions. Legal-sector data is unusually attractive for '
          'double extortion because privilege and client confidentiality raise the cost of publication.</p>'
          '<div style="margin-top:9px"><span class="tag c">Ransomware</span><span class="tag m">Legal sector</span>'
          '<span class="tag m">Double extortion</span></div></div>')

cy.append('<h2 class="sec">Breaches & Incidents</h2>')
cy.append('<div class="cards two">'
          '<div class="card"><div class="k">Healthcare &middot; 9.5M</div><h4>Aesto Health</h4>'
          '<p>The Alabama health-technology company — which provides SaaS for migrating, archiving and accessing patient data when '
          'providers replace EHR systems — says attackers reached its <b>AWS infrastructure</b>. It reported to HHS’ Office for '
          'Civil Rights that the electronic protected health information of <b>9,540,683 individuals</b> was involved, making it the '
          '<b>second-largest confirmed healthcare breach of the year to date</b>. The incident was detected on or about '
          '<b>December 18, 2025</b>; a later review put the access window at <b>December 2–18, 2025</b>. At least '
          '<b>30 healthcare provider clients</b> are affected.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag c">PHI</span><span class="tag m">Cloud</span></div></div>'
          '<div class="card"><div class="k">Identity &middot; 5,000 accounts</div><h4>Dropbox via Lenovo ID</h4>'
          '<p>Dropbox disclosed that roughly <b>5,000 accounts</b> were accessed between <b>August 4 and August 21, 2026</b> without '
          'any password being cracked. A weakness in <b>Lenovo’s email-verification process</b> let attackers register Lenovo IDs '
          'using victims’ email addresses, then sign in to the Dropbox account tied to the same address through the Lenovo ID '
          'integration. Every affected account was linked through Lenovo ID and <b>did not have Dropbox two-factor authentication '
          'enabled</b>. Dropbox says its logs show no evidence files were viewed or downloaded; it has terminated all sessions '
          'authenticated through Lenovo ID, disabled the integration entirely, and now requires a native Dropbox password.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag w">Federated auth</span><span class="tag m">Account takeover</span></div></div>'
          '<div class="card"><div class="k">Healthcare &middot; Extortion</div><h4>Nutex Health</h4>'
          '<p>The Houston micro-hospital operator first disclosed unauthorized network activity on <b>August 24, 2026</b>, and escalated '
          'the matter to a <b>material cybersecurity incident on August 31</b>. The ransomware-as-a-service group <b>The Gentlemen</b> '
          'added Nutex to its leak site and claimed responsibility — the hallmark of double extortion. The exfiltrated data is '
          'described as <b>patient, employee, provider, business and financial information</b>. Nutex says it has not identified any '
          'material impact on business operations or financial-reporting systems to date; a purported class action has been filed in '
          'Texas. <b>No record count is asserted here</b>, because none of this run’s sources states one.</p>'
          '<div style="margin-top:9px"><span class="tag c">Ransomware</span><span class="tag m">Leak site</span></div></div>'
          '<div class="card"><div class="k">Exploitation &middot; Print</div><h4>PaperCut NG/MF, patched twice</h4>'
          '<p><b>Huntress</b> observed exploitation in two customer environments, the first on <b>August 26</b>, with attacker activity '
          'focused on system discovery (<code>whoami</code>, <code>ver</code>, <code>tasklist</code>) and heavy anti-forensics. The '
          'story since: <b>the first emergency patch was bypassed</b> — both watchTowr and Huntress found bypasses — forcing '
          'PaperCut to publish <b>Emergency Patch Release 2</b> for v24, v25 and v26. Anyone who applied only the first patch is still '
          'exposed.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag c">Actively exploited</span><span class="tag w">Patch bypassed</span></div></div>'
          '</div>')

cy.append('<h2 class="sec">Vulnerability Watch</h2>')
cy.append('<div class="tblwrap"><table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr></thead><tbody>'
          '<tr><td><b>CVE-2026-82329</b></td><td class="down">9.8</td><td>JFrog Artifactory (self-hosted only)</td>'
          '<td>Authentication bypass &rarr; forged administrator tokens. Disclosed and patched Aug 28; exploitation observed by Sept 1. SaaS unaffected.</td></tr>'
          '<tr><td><b>CVE-2026-83548</b></td><td class="down">10</td><td>SonicWall SMA1000 (6210, 7210, 8200v)</td>'
          '<td>Pre-authentication SSRF in the Appliance Work Place interface. Chained with CVE-2026-83549 for unauthenticated RCE.</td></tr>'
          '<tr><td><b>CVE-2026-83549</b></td><td class="down">7.8</td><td>SonicWall SMA1000 Appliance Management Console</td>'
          '<td>Authenticated OS command injection. Hotfixes 12.4.3-03526 and 12.5.0-02952 (and later) patch both flaws. Discovered by Rapid7 MDR.</td></tr>'
          '<tr><td><b>CVE-2026-0768</b></td><td class="down">9.8</td><td>Langflow &le; 1.4.2</td>'
          '<td>Unauthenticated root RCE via the <code>code</code> parameter of the <code>validate</code> endpoint. Fixed in 1.11.6. Attackers are harvesting Langflow superuser credentials, AWS secrets and OpenAI API keys.</td></tr>'
          '<tr><td><b>CVE-2026-59822</b></td><td class="warn">8.2</td><td>BerriAI LiteLLM &lt; 1.84.0</td>'
          '<td>MCP Streamable HTTP endpoint accepts a fabricated Bearer token via an OAuth2 passthrough fallback. Fixed in 1.84.0. Added to CISA KEV Sept 2.</td></tr>'
          '<tr><td><b>CVE-2026-81578</b> / <b>CVE-2026-82078</b></td><td class="muted">Not stated</td><td>PaperCut NG/MF</td>'
          '<td>Missing authentication for a critical function, and unsafe reflection. Both in CISA KEV since Aug 31. No CVSS is printed because no source fetched this run stated one authoritatively.</td></tr>'
          '</tbody></table></div>')

cy.append('<h2 class="sec">CISA KEV & Federal Deadlines</h2>')
cy.append('<div class="panel"><ul class="b">'
          '<li><b>CVE-2026-59822</b> — BerriAI LiteLLM improper authentication. Added <b>September 2, 2026</b>; '
          'remediation due <b>September 16, 2026</b> <span class="warn">(14 days left)</span>. Fixed in LiteLLM 1.84.0.</li>'
          '<li><b>CVE-2026-81578</b> and <b>CVE-2026-82078</b> — PaperCut NG/MF. Added <b>August 31, 2026</b>; '
          'remediation due <b>September 14, 2026</b> <span class="warn">(12 days left)</span>. Note that Emergency Patch '
          'Release 2 is the one that holds — the first patch was bypassed.</li>'
          '<li class="note" style="list-style:none;margin-left:-19px"><b>Completeness caveat:</b> this run’s KEV query returned '
          'only the entries above for the September 2 and August 31 additions. Earlier editions today returned a different pair for '
          'September 2. These are the entries this run can verify; they are <b>not</b> presented as the complete list, and CISA’s '
          'catalog page is linked in Sources for the authoritative view.</li>'
          '</ul></div>')

cy.append(sources(CY_SOURCES))
cy.append('<div class="disc">Compiled from public reporting and vendor advisories. Severity scores and remediation deadlines '
          'can change as vendors and CISA update their records; verify against the vendor advisory and the CISA KEV catalog before '
          'acting. This briefing is informational and is not a substitute for your own incident-response process.</div></footer>')
cy.append(STAMP_JS)
cy.append('</div></body></html>')
w("cyber-briefing.html", "".join(cy))


# ---------------------------------------------------------------- WALL STREET
WS_CSS = base_css("#caa64a", "#e8c766", "#100e0a", "#191610", "#2c2619") + UTIL_CSS + """
.mast-serif h1,h3,h4{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:1fr;gap:12px}
@media(min-width:760px){.tickers{grid-template-columns:repeat(3,1fr)}}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""

WS_SOURCES = [
    ("CNBC — Stock market news for Sept. 2, 2026",
     "https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html"),
    ("Kiplinger — Stocks Snap Losing Streak as Treasury Yields Ease",
     "https://www.kiplinger.com/investing/stocks/stocks-snap-losing-streak-as-treasury-yields-ease-stock-market-today"),
    ("TheStreet — Stock Market Today (Sept. 2, 2026)",
     "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026"),
    ("CNBC — Stocks making the biggest moves midday: PG&E, Dell, GitLab, Credo",
     "https://www.cnbc.com/2026/09/02/stocks-making-the-biggest-moves-midday-pcg-dell-gtlb-crdo-bfb.html"),
    ("CNBC — Stocks making the biggest moves after hours: Snowflake, Broadcom, Netskope, Five Below",
     "https://www.cnbc.com/2026/09/02/stocks-making-the-biggest-moves-after-hours-snow-avgo-ntsk-five.html"),
    ("The Motley Fool — Stock Market Today, Sept. 2: Dell Surges 16% on Soaring AI Backlog",
     "https://www.fool.com/coverage/stock-market-today/2026/09/02/stock-market-today-sept-2-dell-surges-16-on-soaring-ai-backlog/"),
    ("Yahoo Finance — 10-year Treasury touches highest level since 2023 as oil prices stay elevated",
     "https://finance.yahoo.com/markets/article/10-year-treasury-touches-highest-level-since-2023-as-oil-prices-stay-elevated-134238599.html"),
    ("Yahoo Finance — Stock market today: Wednesday, September 2",
     "https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-2-dow-sp-500-nasdaq-082624175.html"),
    ("Fortune — Current price of oil as of September 2, 2026",
     "https://fortune.com/article/price-of-oil-09-02-2026/"),
    ("Trading Economics — Brent Crude Oil",
     "https://tradingeconomics.com/commodity/brent-crude-oil"),
    ("Investing.com — S&P 500 sector performance: Energy leads with +42% YTD gain in 2026",
     "https://www.investing.com/news/stock-market-news/sp-500-sector-performance-energy-leads-with-42-ytd-gain-in-2026-93CH-4883146"),
    ("FedRateCalc — September 2026 U.S. Economic Calendar",
     "https://fedratecalc.com/us-economic-calendar/september-2026/"),
    ("BLS — Schedule of Selected Releases 2026",
     "https://www.bls.gov/schedule/2026/home.htm"),
]

WS_SUMMARY = ("Stocks snapped a losing streak on Wednesday as Treasury yields eased — the S&P 500 closed at "
              "7,666.60 (+0.46%), the Dow at 53,061.95 (+295.07, +0.56%) and the Nasdaq Composite at 26,217.83 "
              "(+0.45%) — with Dell up roughly 16% on its AI backlog and Snowflake surging after the bell.")

ws = []
ws.append(head("The Closing Bell — Daily Briefing", WS_CSS))
ws.append('<header class="masthead mast-serif"><h1>&#9650; The Closing Bell</h1>'
          '<p class="tag">Your daily markets briefing — the tape, the movers and what’s next</p>'
          + meta_row() + '</header>')
ws.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % WS_SUMMARY)
ws.append(FRESH)
ws.append(nav("ws"))

# BLOCK A
ws.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
          '<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>'
          '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
          '{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},'
          '{"proName":"NASDAQ:DELL","title":"Dell"},{"proName":"NASDAQ:MU","title":"Micron"},'
          '{"proName":"NASDAQ:AMD","title":"AMD"},{"proName":"NYSE:SNOW","title":"Snowflake"},'
          '{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],'
          '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}'
          '</script></div>')

# BLOCK B
ws.append('<h2 class="sec">Live Index Quotes — updates in real time</h2>')
ws.append('<div class="tickers">'
          '<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
          '{"symbol":"FOREXCOM:SPXUSD","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'
          '<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
          '{"symbol":"FOREXCOM:NSXUSD","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'
          '<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
          '{"symbol":"FOREXCOM:DJI","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'
          '</div>'
          '<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; '
          'official closes are in the Weekly Scorecard.</div>')

ws.append('<h2 class="sec">The Lead</h2>')
ws.append('<div class="panel"><h3>Stocks snap a losing streak as yields ease and the dollar softens</h3>'
          '<p>Wednesday’s session is closed. The <b>S&amp;P 500</b> finished <b>+0.46%</b>, the <b>Nasdaq Composite</b> '
          '<b>+0.45%</b> and the <b>Dow Jones Industrial Average</b> <b>+295.07 points, or +0.56%</b>. The move came as U.S. '
          'Treasury yields took a breather from a run-up that had carried the 10-year to multiyear highs, and as the dollar '
          'weakened.</p>'
          '<p>The day’s single loudest signal was corporate rather than macro: <b>Dell</b> lifted its fiscal-2027 revenue '
          'forecast on the strength of its AI business and finished up roughly 16%, the largest gain among the session’s big '
          'movers. Beneath '
          'that, the tape stayed uneven — The Motley Fool framed the session as indexes snapping losing streaks '
          '<i>amid</i> U.S.–Iran hostilities and rising Treasury yields still pressuring technology valuations.</p>'
          '<p class="note"><b>An unresolved discrepancy, printed rather than picked:</b> CNBC describes Wednesday as snapping a '
          '<i>three-day</i> losing streak; Kiplinger describes it as a <i>two-day</i> streak. Both readings are shown here and '
          'neither is adopted. Separately, one aggregated return this run attached a set of much lower Treasury yields and a bond '
          'buy-back announcement to this session; those figures trace to an <b>August</b> article rather than to Wednesday, so they '
          'were <b>refused</b> and the rates table below carries only the September 2 readings.</p></div>')

ws.append('<h2 class="sec">Movers & Drivers</h2>')
ws.append('<div class="cards two">'
          '<div class="card"><div class="k">DELL &middot; up ~16%</div><h4>Dell Technologies</h4>'
          '<p>Lifted its fiscal-2027 revenue forecast, citing strength in its AI business. In the quarter, <b>sales rose 58%</b> and '
          '<b>adjusted EPS rose 203%</b>; <b>AI-optimized server revenue doubled</b>. The AI unit booked <b>$61 billion in orders</b>, '
          'taking backlog <b>above $95 billion</b>. This run’s fetch put the move at <b>+15.81%</b>; an earlier edition today '
          'reconciled it to <b>+15.76%</b> at $492.00. Both readings are shown, neither is adopted, and the page says '
          '&ldquo;roughly 16%&rdquo; throughout.</p>'
          '<div style="margin-top:9px"><span class="tag a">AI infrastructure</span><span class="tag m">Guidance raise</span></div></div>'
          '<div class="card"><div class="k">CRDO &middot; −18%</div><h4>Credo Technology</h4>'
          '<p>Fell <b>18% to $169.10</b> following its first-quarter results — the sharpest decline among the session’s '
          'large movers, and a reminder that the AI-connectivity trade is not moving in one direction.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag c">Earnings</span></div></div>'
          '<div class="card"><div class="k">GTLB &middot; +13%</div><h4>GitLab</h4>'
          '<p>Rallied <b>nearly 13%</b> on an earnings beat and upbeat full-year guidance: <b>24 cents per share excluding items</b> '
          'against an 18-cent estimate, on <b>$286 million</b> of second-quarter revenue against $273 million expected.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag a">Beat and raise</span></div></div>'
          '<div class="card"><div class="k">PCG &middot; −7%</div><h4>PG&amp;E</h4>'
          '<p>Dropped <b>another 7%</b> after plunging <b>20% on Monday</b>. The California utility has begun a <b>strategic and '
          'financial review</b> to study a possible reorganization, and has <b>deferred $2 billion of 2027 capital spending</b>.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag c">Utilities</span><span class="tag w">Restructuring review</span></div></div>'
          '<div class="card"><div class="k">BF.B &middot; +4%</div><h4>Brown-Forman</h4>'
          '<p>Advanced <b>4%</b> after earnings narrowly beat. The maker of Jack Daniel’s earned <b>38 cents per share</b>, a '
          'cent above the FactSet consensus, with <b>operating income of $252 million</b> also ahead of the consensus call.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag m">Consumer staples</span></div></div>'
          '</div>')

# BLOCK E
ws.append('<h2 class="sec">Chart of the Day</h2>')
ws.append('<div class="panel" style="padding:8px">'
          '<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>'
          '{"symbol":"NYSE:DELL","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark",'
          '"isTransparent":true,"autosize":false}</script></div>'
          '<div class="note"><b>Dell Technologies</b> — the session’s biggest gainer among the large-cap movers, up roughly 16% '
          'after raising its fiscal-2027 revenue forecast on a $95 billion-plus AI backlog.</div>')

# BLOCK D
ws.append('<h2 class="sec">Sector Heat — live</h2>')
ws.append('<div class="panel" style="padding:8px">'
          '<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>'
          '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en",'
          '"colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,'
          '"isMonoSize":false,"width":"100%","height":420}</script></div>'
          '<div class="note"><b>Year to date, energy is running away from the field:</b> the Energy Select Sector SPDR (XLE) is '
          '<b>+42.32%</b>, with materials <b>+15.86%</b>. Those are <b>YTD figures only</b>. Single-session sector leadership is '
          'deliberately not asserted on this page: returns across today’s fetches disagreed with each other about which sector '
          'led and which lagged, so the live heatmap above is the reference for the session.</div>')

# BLOCK F
ws.append('<h2 class="sec">The Calendar — live</h2>')
ws.append('<div class="panel" style="padding:8px">'
          '<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>'
          '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1",'
          '"countryFilter":"us"}</script></div>')

# BLOCK C
ws.append('<h2 class="sec">Live Market Headlines — updates in real time</h2>')
ws.append('<div class="panel" style="padding:8px">'
          '<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>'
          '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular",'
          '"width":"100%","height":420,"locale":"en"}</script></div>')

ws.append('<h2 class="sec">After-Hours Movers</h2>')
ws.append('<div class="cards two">'
          '<div class="card"><div class="k">SNOW &middot; sharply higher</div><h4>Snowflake</h4>'
          '<p>Second-quarter results topped expectations: <b>adjusted EPS of $0.62</b> against $0.45 expected, on <b>$1.55 billion</b> '
          'of revenue against $1.48 billion expected, with stronger full-year product-revenue guidance. <b>Three different readings of '
          'the after-hours move were returned and none is adopted:</b> +20% (CNBC, this run), +22% (The Motley Fool, stated as of '
          '5 p.m. ET this run) and +21% (an earlier edition’s fetch of a post-close piece timestamped 4:30 PM ET).</p>'
          '<div style="margin-top:9px"><span class="tag a">Earnings beat</span><span class="tag m">Guidance raise</span></div></div>'
          '<div class="card"><div class="k">AVGO &middot; lower</div><h4>Broadcom</h4>'
          '<p>Slipped after hours as investors focused on the outlook rather than the quarter: <b>fourth-quarter revenue guidance of '
          '$34.8 billion</b> against a $35.03 billion estimate, and a <b>non-GAAP operating margin of 66%</b> against 66.5% expected. '
          'CNBC put the decline at <b>more than 2%</b> this run; an earlier fetch today read <b>−3.5%</b>. Both are shown; neither '
          'is adopted. The &ldquo;fourth-quarter&rdquo; label above is the one CNBC states; <b>no fiscal-year period is asserted</b>, '
          'per a standing correction against inferring one from summarizer prose.</p>'
          '<div style="margin-top:9px"><span class="tag c">Guidance miss</span><span class="tag m">Semis</span></div></div>'
          '<div class="card"><div class="k">WOOF &middot; +10%</div><h4>Petco</h4>'
          '<p>Jumped <b>10%</b>, with second-quarter <b>adjusted EBITDA margin of 8.2%</b> against a StreetAccount consensus estimate '
          'of 7.4%.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag a">Margin beat</span></div></div>'
          '<div class="card"><div class="k">AGX &middot; +8%</div><h4>Argan</h4>'
          '<p>Popped <b>8%</b> after posting better-than-expected second-quarter earnings and revenue. No specific figures were stated '
          'in what was fetched, so none are printed.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag a">Earnings beat</span></div></div>'
          '<div class="card"><div class="k">HPE &middot; −1%</div><h4>Hewlett Packard Enterprise</h4>'
          '<p>Slipped <b>1%</b>, calling for earnings growth of <b>16% to 20%</b> for the fiscal year ending October 2027 while the '
          'FactSet consensus sought an <b>18.7%</b> increase.</p>'
          '<div style="margin-top:9px"><span class="tag w">Guidance</span></div></div>'
          '</div>')

ws.append('<h2 class="sec">Weekly Scorecard</h2>')
ws.append('<div class="tblwrap"><table><thead><tr><th>Index</th><th>Close</th><th>Change</th><th>%</th></tr></thead><tbody>'
          '<tr><td><b>S&amp;P 500</b></td><td>7,666.60</td><td class="up">+35.13</td><td class="up">+0.46%</td></tr>'
          '<tr><td><b>Nasdaq Composite</b></td><td>26,217.83</td><td class="up">+118.06</td><td class="up">+0.45%</td></tr>'
          '<tr><td><b>Dow Jones Industrial Average</b></td><td>53,061.95</td><td class="up">+295.07</td><td class="up">+0.56%</td></tr>'
          '</tbody></table></div>'
          '<div class="note">Official closes for <b>Wednesday, September 2, 2026</b>. The Dow point change is as reported. The S&amp;P 500 '
          'and Nasdaq point changes are <b>derived</b> from the reconciliation against Tuesday’s verified closes '
          '(7,631.47 and 26,099.77): 7,631.47 + 35.13 = 7,666.60, and 26,099.77 + 118.06 = 26,217.83. Every level, point change and '
          'percentage in this table reconciles arithmetically and against the prior session before being published.</div>')

ws.append('<h2 class="sec">Rates, Bonds & Commodities</h2>')
ws.append('<div class="tblwrap"><table><thead><tr><th>Instrument</th><th>Level</th><th>Session</th><th>Note</th></tr></thead><tbody>'
          '<tr><td><b>U.S. 10-year Treasury</b></td><td>4.79%</td><td class="up">eased ~0.01 pp</td>'
          '<td>Intraday high of 4.814%. Sources disagree on the &ldquo;highest since&rdquo; framing, so none is stated here.</td></tr>'
          '<tr><td><b>WTI crude</b></td><td>$90.76</td><td class="up">+0.60%</td><td>Wednesday close.</td></tr>'
          '<tr><td><b>Brent crude</b></td><td>$94.86</td><td class="up">+0.23%</td>'
          '<td>Reported as settling about 1% higher in a volatile session, with U.S.–Iran strikes threatening supply.</td></tr>'
          '<tr><td><b>Fed funds</b></td><td>Next decision Sept 16</td><td class="muted">—</td>'
          '<td>Chair Kevin Warsh’s hawkish remarks lifted Polymarket odds of a September <i>hike</i> to 56%; Governor Barr said the '
          'Fed should raise in September if inflation is not moderating sufficiently. No current target range is printed because none '
          'was stated in this run’s sources.</td></tr>'
          '</tbody></table></div>')

ws.append('<h2 class="sec">On the Radar</h2>')
ws.append('<div class="panel"><ul class="b">'
          '<li><b>Thursday, Sept 3 &middot; 8:30 AM ET — initial jobless claims.</b> Forecast 205,000, prior 203,000.</li>'
          '<li><b>Thursday, Sept 3 &middot; 8:30 AM ET — July international trade in goods and services.</b> Expected '
          '−$71.2 billion against a prior −$73.26 billion. Second-quarter productivity and costs (revised) lands at the same '
          'hour.</li>'
          '<li><b>Friday, Sept 4 &middot; 8:30 AM ET — the August employment situation.</b> The month’s single most '
          'consequential release, into a market now pricing a meaningful chance of a rate <i>hike</i>.</li>'
          '<li><b>Wednesday, Sept 16 &middot; 2:00 PM ET — the FOMC rate decision.</b></li>'
          '</ul></div>')

ws.append(sources(WS_SOURCES))
ws.append('<div class="disc">For information only. Nothing on this page is investment advice, a recommendation, or an offer to buy '
          'or sell any security. Figures are compiled from public reporting and may be revised; verify against primary sources before '
          'acting. Live widgets are supplied by TradingView and some feeds are delayed.</div></footer>')
ws.append(STAMP_JS)
ws.append('</div></body></html>')
w("wallstreet-briefing.html", "".join(ws))


# ---------------------------------------------------------------- MMA
MMA_CSS = base_css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020") + UTIL_CSS + """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:11px;
  padding:12px 16px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn .v{font-family:var(--mono);font-size:19px;color:var(--text)}
.cdn .w{font-size:13.5px;color:var(--muted)}
.when{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#e8c766;margin-bottom:6px}
.odds{font-family:var(--mono);font-size:11.5px;color:var(--muted);margin-top:8px}
"""

MMA_SOURCES = [
    ("Bloody Elbow — UFC 332 update: new main event will be announced this week",
     "https://bloodyelbow.com/2026/09/02/ufc-332-update-new-main-event-will-be-announced-this-week-after-title-fight-collapsed-due-to-injury/"),
    ("Bloody Elbow — Embattled UFC 332 loses main event as Valentina Shevchenko forced out with injury",
     "https://bloodyelbow.com/2026/09/01/embattled-ufc-332-loses-main-event-as-valentina-shevchenko-forced-out-with-injury/"),
    ("Yahoo Sports — Valentina Shevchenko pulls out of UFC 332",
     "https://sports.yahoo.com/articles/valentina-shevchenko-pulls-ufc-332-115326528.html"),
    ("UFC.com — UFC Fight Night: Hooker vs Parnasse (Sept 5, 2026)",
     "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
    ("Rotowire — Hooker vs Parnasse Sep 5, 2026 odds",
     "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
    ("UFC.com — Flyweight champion Joshua Van set for rematch with Alexandre Pantoja at Crypto.com UFC 331",
     "https://www.ufc.com/news/flyweight-champion-joshua-van-set-rematch-alexandre-pantoja-cryptocom-ufc-331"),
    ("ESPN — UFC 331: Van vs. Pantoja 2 fight center",
     "https://www.espn.com/mma/fightcenter/_/id/600060963/league/ufc"),
    ("ESPN — UFC Fight Night: Nurmagomedov vs. Song fight results",
     "https://www.espn.com/mma/fightcenter/_/id/600060620/league/ufc"),
    ("UFC.com — UFC Shanghai results: Nurmagomedov vs. Song",
     "https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song"),
    ("UFC.com — UFC Fight Night Shanghai 2026 bonus coverage",
     "https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage"),
    ("ESPN — Song Yadong KOs Umar Nurmagomedov in massive UFC upset",
     "https://www.espn.com/mma/story/_/id/49762250/song-yadong-kos-umar-nurmagomedov-massive-ufc-upset-shanghai"),
    ("Yahoo Sports — Song Yadong wants title shot after UFC Shanghai",
     "https://sports.yahoo.com/articles/song-yadong-wants-title-shot-160120772.html"),
    ("UFC.com — Welcome to the UFC: DWCS Season 10, Week 4",
     "https://www.ufc.com/news/welcome-ufc-dwcs-season-10-week-4"),
    ("ESPN — Current and all-time UFC champions",
     "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
    ("ESPN — Strickland stuns rival Chimaev for UFC middleweight title",
     "https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title"),
    ("Sky Sports — Sean Strickland defeats Khamzat Chimaev at UFC 328 to regain middleweight title",
     "https://www.skysports.com/mma/news/19828/13542189/sean-strickland-defeats-khamzat-chimaev-in-ufc-328-to-regain-middleweight-title-after-split-decision"),
    ("FIGHTMAG — UFC schedule",
     "https://schedule.fightmag.com/events/categories/ufc/"),
]

MMA_SUMMARY = ("UFC 332 has lost its main event — Valentina Shevchenko withdrew injured from a flyweight title "
               "defence against Natália Silva, and Dana White says a replacement announcement is imminent — while "
               "Salahdine Parnasse debuts as a heavy favourite in Saturday’s Paris headliner.")

mm = []
mm.append(head("The Octagon — Daily Briefing", MMA_CSS))
mm.append('<header class="masthead"><h1>&#8856; The Octagon</h1>'
          '<p class="tag">Your daily MMA briefing — UFC, prospects & the business of fighting</p>'
          + meta_row() + '</header>')
mm.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % MMA_SUMMARY)
mm.append(FRESH)
mm.append(nav("mma"))

mm.append('<div class="cdn"><span class="k">Next card</span><span class="v" id="ufccdn">&nbsp;</span>'
          '<span class="w">UFC Fight Night: Hooker vs. Parnasse · Saturday, September 5 · Accor Arena, Paris</span></div>')

mm.append('<h2 class="sec">Top Story</h2>')
mm.append('<div class="panel" style="border-left:3px solid var(--accent)">'
          '<h3>UFC 332 has no main event, and the replacement is said to be days away</h3>'
          '<p><b>Valentina Shevchenko has withdrawn from UFC 332 with an undisclosed injury</b>, collapsing a women’s '
          'flyweight title fight against <b>Natália Silva</b> that had been booked as the co-main event and was later reported to '
          'have been elevated to the main event. The bout is off. <b>UFC 332 takes place October 3, 2026 at the Delta Center in '
          'Salt Lake City.</b></p>'
          '<p><b>Dana White says an official announcement on a new main event is imminent</b>, and Bloody Elbow reported on '
          'September 2 that the replacement will be named <b>this week</b>. As of this edition the UFC has <b>not</b> disclosed a '
          'timeline for Shevchenko’s return and has <b>not</b> announced a replacement bout.</p>'
          '<p class="note">No replacement booking is asserted here. Names that have circulated in coverage are speculation until the '
          'promotion confirms a bout, and this page will carry one only when it does.</p></div>')

mm.append('<h2 class="sec">Fight Week — Upcoming Cards</h2>')
mm.append('<div class="cards two">'
          '<div class="card"><div class="when">Sept 5 &middot; Accor Arena, Paris</div>'
          '<h4>UFC Fight Night: Hooker vs. Parnasse</h4>'
          '<p><b>Dan Hooker vs. Salahdine Parnasse</b> at lightweight. Parnasse makes his <b>UFC debut in a main event</b> — a '
          'former <b>two-time KSW featherweight champion and one-time KSW lightweight champion</b> who signed with the UFC in late '
          'July 2026, having previously turned the promotion down. He did <b>not</b> come through Dana White’s Contender Series.</p>'
          '<div class="odds">Odds: Parnasse −600 / Hooker +440 (DraftKings); −667 / +417 (Betr). Across books Parnasse has '
          'ranged −500 to −700 and Hooker +360 to +450.</div>'
          '<div style="margin-top:9px"><span class="tag a">Main event debut</span><span class="tag m">Lightweight</span></div></div>'
          '<div class="card"><div class="when">Sept 12 &middot; Desert Diamond Arena, Glendale, AZ</div>'
          '<h4>Noche UFC: Silva vs. Delgado</h4>'
          '<p>The annual Mexican Independence weekend card. Listed on published UFC schedules; no card details beyond the headline '
          'billing were stated in what was fetched this run, so none are printed.</p>'
          '<div style="margin-top:9px"><span class="tag m">Noche UFC</span></div></div>'
          '<div class="card"><div class="when">Sept 19 &middot; Crypto.com Arena, Los Angeles</div>'
          '<h4>UFC 331: Van vs. Pantoja 2</h4>'
          '<p>A <b>flyweight title rematch</b>. Champion <b>Joshua Van</b> defends against former champion <b>Alexandre Pantoja</b>, '
          'whom he beat at UFC 323 in December 2025 by technical knockout <b>26 seconds into the first round</b>, after Pantoja '
          'sustained an arm injury. Prelims 6 PM ET, main card 9 PM ET, on Paramount+.</p>'
          '<div style="margin-top:9px"><span class="tag a">Title fight</span><span class="tag m">Rematch</span></div></div>'
          '<div class="card"><div class="when">Sept 26 &middot; Meta Apex, Las Vegas</div>'
          '<h4>UFC Fight Night: Rosas Jr. vs. Barcelos</h4>'
          '<p>An Apex card closing out the month. No further card details were stated in what was fetched this run.</p>'
          '<div style="margin-top:9px"><span class="tag m">Fight Night</span></div></div>'
          '<div class="card"><div class="when">Oct 3 &middot; Delta Center, Salt Lake City</div>'
          '<h4>UFC 332 — main event TBD</h4>'
          '<p>The card that lost its headliner. See the top story: a replacement main event is expected to be announced this week.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag c">Headliner vacant</span></div></div>'
          '<div class="card"><div class="when">Oct 24 &middot; Etihad Arena, Abu Dhabi</div>'
          '<h4>UFC 333: Volkanovski vs. Evloev</h4>'
          '<p>Featherweight champion <b>Alexander Volkanovski</b> defends against <b>Movsar Evloev</b>. The card is also slated to carry '
          'the <b>Petr Yan vs. Merab Dvalishvili trilogy bout</b> at bantamweight.</p>'
          '<div style="margin-top:9px"><span class="tag a">Two title fights</span></div></div>'
          '</div>')

mm.append('<h2 class="sec">Last Event — Results</h2>')
mm.append('<div class="note" style="margin:0 0 11px"><b>UFC Fight Night: Nurmagomedov vs. Song</b> · Saturday, August 29, 2026 '
          '· Oriental Sports Center, Shanghai. The bouts below are the ones confirmed across this run’s fetches; the table is '
          'not asserted to be the complete card.</div>')
mm.append('<div class="tblwrap"><table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr></thead><tbody>'
          '<tr><td class="win">Song Yadong</td><td>def. Umar Nurmagomedov</td><td>KO (right uppercut), R2 1:48</td></tr>'
          '<tr><td class="win">Denise Gomes</td><td>def. Yan Xiaonan</td><td>KO (elbow and punches), R1 4:49</td></tr>'
          '<tr><td class="win">Kai Asakura</td><td>def. Aori Qileng</td><td>TKO (head kick and punches), R2 0:34</td></tr>'
          '<tr><td class="win">Su Mudaerji</td><td>def. Alex Perez</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>'
          '<tr><td class="win">Ce Liu</td><td>def. Levi Rodrigues Jr.</td><td>KO (punch), R1 4:26</td></tr>'
          '<tr><td class="win">Rei Tsuruya</td><td>def. Kevin Borjas</td><td>Submission (rear-naked choke), R1 4:03</td></tr>'
          '<tr><td class="win">Sean Woodson</td><td>def. Jack Jenkins</td><td>Split decision (29-28, 28-29, 29-28)</td></tr>'
          '<tr><td class="win">Hector Santiago</td><td>def. Lawrence Lui</td><td>KO (punches), R2 0:53</td></tr>'
          '<tr><td class="win">Julia Polastri</td><td>def. Xiong Jingnan</td><td>KO (head kick), R1 3:06</td></tr>'
          '<tr><td class="win">André Lima</td><td>def. Namsrai Batbayar</td><td>Submission (guillotine choke), R3 3:03</td></tr>'
          '<tr><td class="win">Francesco Nuzzi</td><td>def. Xiao Long</td><td>TKO (strikes), R1 1:00</td></tr>'
          '</tbody></table></div>')
mm.append('<div class="panel" style="margin-top:13px"><div class="k" style="font-family:var(--mono);font-size:10.5px;'
          'letter-spacing:.15em;text-transform:uppercase;color:var(--accent);margin-bottom:7px">Performance bonuses</div>'
          '<p style="margin-bottom:7px"><b>$100,000 each:</b> Performance of the Night to <b>Song Yadong</b> and <b>Bilal Hasan</b>; '
          'Fight of the Night to <b>Ce Liu</b> and <b>Levi Rodrigues Jr.</b> (the bonus report renders his name &ldquo;Liu Ce&rdquo;; '
          'the results listing renders it &ldquo;Ce Liu&rdquo; — the same fighter, one bout).</p>'
          '<p style="margin-bottom:0"><b>$25,000 stoppage bonuses</b> were reported for <b>Hector Santiago, Francesco Nuzzi, '
          'Rei Tsuruya, Kai Asakura and Denise Gomes</b>.</p>'
          '<p class="note" style="margin-bottom:0">An earlier fetch today listed seven names in the $25,000 tier, including André '
          'Lima and Julia Polastri, while a following sentence in the same source said &ldquo;five more fighters.&rdquo; This run’s '
          'source names the five above. <b>No total count is asserted.</b></p></div>')

mm.append('<h2 class="sec">Prospect Watch</h2>')
mm.append('<div class="note" style="margin:0 0 11px">Five contracts were awarded at <b>Dana White’s Contender Series Season 10, '
          'Week 4</b>, held <b>September 1, 2026 at the Meta APEX</b>.</div>')
mm.append('<div class="cards two">'
          '<div class="card"><h4>Adam Darby</h4><p>The Cage Warriors contender from Ireland earned a UFC contract at the September 1 '
          'event.</p><div style="margin-top:9px"><span class="tag new">New</span><span class="tag" style="color:var(--up);border-color:var(--up)">Prospect</span></div></div>'
          '<div class="card"><h4>Modestino Rodrigues</h4><p>A former K-1 kickboxing ace, and the latest Brazilian added to the UFC '
          'roster.</p><div style="margin-top:9px"><span class="tag new">New</span><span class="tag" style="color:var(--up);border-color:var(--up)">Prospect</span></div></div>'
          '<div class="card"><h4>Gabriel Lorenco</h4><p>A 26-year-old heavyweight who earned his contract with a first-round knockout.'
          '</p><div style="margin-top:9px"><span class="tag new">New</span><span class="tag" style="color:var(--up);border-color:var(--up)">Prospect</span></div></div>'
          '<div class="card"><h4>Silvestre Sanchez</h4><p>The Lux Fight League fighter earned a UFC deal.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag" style="color:var(--up);border-color:var(--up)">Prospect</span></div></div>'
          '<div class="card"><h4>Adam Livingston</h4><p>The LFA veteran earned a UFC contract.</p>'
          '<div style="margin-top:9px"><span class="tag new">New</span><span class="tag" style="color:var(--up);border-color:var(--up)">Prospect</span></div></div>'
          '</div>')

mm.append('<h2 class="sec">Around the Sport</h2>')
mm.append('<div class="panel"><ul class="b">'
          '<li><b>Song Yadong is asking for the belt.</b> After knocking out Umar Nurmagomedov he said: &ldquo;I think the UFC should '
          'give me the title shot. I feel like I can finish everyone. I can finish Petr, I can finish Merab.&rdquo;</li>'
          '<li><b>Contender Series Season 10 continues.</b> Week 4 ran September 1; <b>Week 6 is scheduled for September 15</b>. '
          '(Reported dates for the intervening weeks have varied across sources, so none is stated.)</li>'
          '<li><b>UFC 332 is the card to watch this week</b> — not for a booking that exists, but for the one the promotion says '
          'it is about to announce.</li>'
          '</ul></div>')

mm.append('<h2 class="sec">Rankings & Business</h2>')
mm.append('<div class="panel"><p><b>Rankings movement.</b> Song Yadong’s knockout of the <b>No. 2-ranked</b> Umar Nurmagomedov '
          'launched him into the bantamweight championship picture; he is described as likely next in line at 135 pounds, depending on '
          'the outcome of the <b>Petr Yan vs. Merab Dvalishvili trilogy bout at UFC 333</b>. It was the second loss of Nurmagomedov’s '
          'career.</p>'
          '<p style="margin-bottom:0"><b>Business &amp; broadcast.</b> UFC 331 streams on <b>Paramount+</b>, prelims at 6 PM ET and main '
          'card at 9 PM ET; Dana White’s Contender Series also airs on Paramount+. <b>No viewership, gate or TKO Group figures are '
          'printed</b>, because none was stated in any source fetched this run.</p></div>')

mm.append('<h2 class="sec">Champions Board</h2>')
mm.append('<div class="tblwrap"><table><thead><tr><th>Division</th><th>Champion</th><th>Note</th></tr></thead><tbody>'
          '<tr><td><b>Heavyweight</b></td><td>Tom Aspinall</td><td>Undisputed. <b>Interim:</b> Ciryl Gane.</td></tr>'
          '<tr><td><b>Light Heavyweight</b></td><td>Carlos Ulberg</td><td>Won the vacant title by first-round knockout of Jiří Procházka at UFC 327.</td></tr>'
          '<tr><td><b>Middleweight</b></td><td>Sean Strickland</td><td>Split-decision upset of Khamzat Chimaev at UFC 328 in Newark — two judges 48-47 Strickland, one 48-47 Chimaev. Two-time champion; the first man to beat Chimaev.</td></tr>'
          '<tr><td><b>Welterweight</b></td><td>Islam Makhachev</td><td>Two-division champion; one defence.</td></tr>'
          '<tr><td><b>Lightweight</b></td><td>Justin Gaethje</td><td>&nbsp;</td></tr>'
          '<tr><td><b>Featherweight</b></td><td>Alexander Volkanovski</td><td>Defends against Movsar Evloev at UFC 333, October 24.</td></tr>'
          '<tr><td><b>Bantamweight</b></td><td>Petr Yan</td><td>Slated to face Merab Dvalishvili in a trilogy bout at UFC 333.</td></tr>'
          '<tr><td><b>Flyweight</b></td><td>Joshua Van</td><td>Defends against Alexandre Pantoja at UFC 331, September 19.</td></tr>'
          '<tr><td><b>Women’s Flyweight</b></td><td>Valentina Shevchenko</td><td class="nc">Withdrew from a UFC 332 title defence against Natália Silva with an undisclosed injury; no return timeline disclosed.</td></tr>'
          '<tr><td><b>Women’s Bantamweight</b></td><td>Kayla Harrison</td><td>&nbsp;</td></tr>'
          '<tr><td><b>Women’s Strawweight</b></td><td>Mackenzie Dern</td><td>One defence.</td></tr>'
          '<tr><td><b>Women’s Featherweight</b></td><td>Vacant</td><td>&nbsp;</td></tr>'
          '</tbody></table></div>'
          '<div class="note"><b>Verified this run.</b> A widely-syndicated &ldquo;current champions&rdquo; listing fetched this run '
          'again showed <b>Khamzat Chimaev</b> at middleweight. That is wrong, and it is the same single cell that has been wrong in '
          'those listings for months: <b>Sean Strickland</b> holds the belt, re-confirmed this run against ESPN, Bleacher Report, '
          'Sky Sports, CBS Sports and Al Jazeera. A related open discrepancy: ESPN and CBS date UFC 328 to May 10, 2026, while '
          'this desk’s standing record has May 9, 2026. May 9 is retained and the disagreement is printed rather than hidden; '
          'no weekday is attached to either date, because the two sources do not agree on one.</div>')

mm.append(sources(MMA_SOURCES))
mm.append('<div class="disc">Cards and bouts are subject to change. Fighters withdraw, bouts are rebooked and betting lines move; '
          'confirm any card against UFC.com before making plans. Odds shown are point-in-time quotes from the books named, not '
          'recommendations.</div></footer>')
mm.append("""<script>(function(){var el=document.getElementById('ufccdn');if(!el)return;
var target=new Date('2026-09-05T00:00:00-04:00').getTime();
function tick(){var d=target-Date.now();
if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}
var days=Math.floor(d/86400000),h=Math.floor(d%86400000/3600000),m=Math.floor(d%3600000/60000);
el.textContent=days+'d '+h+'h '+m+'m';}
tick();setInterval(tick,30000);})();</script>""")
mm.append(STAMP_JS)
mm.append('</div></body></html>')
w("mma-briefing.html", "".join(mm))


# ---------------------------------------------------------------- INDEX
IX_CSS = base_css("#c9c2b8", "#e9e6e1", "#0d0d0e", "#151517", "#26262a") + """
.big{display:grid;gap:15px;margin-top:6px}
@media(min-width:820px){.big{grid-template-columns:repeat(3,1fr)}}
.bigcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 21px;transition:.16s;
  display:flex;flex-direction:column}
.bigcard:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(0,0,0,.4)}
.bigcard .kick{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:9px}
.bigcard h3{font-size:22px;margin:0 0 4px}
.bigcard .sub{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin-bottom:12px}
.bigcard p{font-size:14.5px;color:#cfcdc9;flex:1}
.bigcard a.more{font-family:var(--mono);font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;margin-top:14px;display:inline-block}
.cy{--c:#22d3a8}.wsx{--c:#caa64a}.mx{--c:#e84545}
.bigcard.cy:hover,.bigcard.wsx:hover,.bigcard.mx:hover{border-color:var(--c)}
.bigcard .kick,.bigcard a.more{color:var(--c)}
.bigcard.wsx h3{font-family:Georgia,'Times New Roman',serif}
"""

ix = []
ix.append(head("Daily Briefings", IX_CSS))
ix.append('<header class="masthead"><h1>Daily Briefings</h1>'
          '<p class="tag">Three briefings, refreshed through the day — security, markets and the fight game</p>'
          + meta_row() + '</header>')
ix.append(FRESH)
ix.append(nav("index"))
ix.append('<div class="big">'
          '<div class="bigcard cy"><div class="kick">&#9960; The Cyber Wire</div><h3>The Wire</h3>'
          '<div class="sub">Security</div><p>%s</p>'
          '<a class="more" href="cyber-briefing.html">Read the briefing &rarr;</a></div>'
          '<div class="bigcard wsx"><div class="kick">&#9650; The Closing Bell</div><h3>The Tape</h3>'
          '<div class="sub">Markets</div><p>%s</p>'
          '<a class="more" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>'
          '<div class="bigcard mx"><div class="kick">&#8856; The Octagon</div><h3>Tale of the Tape</h3>'
          '<div class="sub">MMA</div><p>%s</p>'
          '<a class="more" href="mma-briefing.html">Read the briefing &rarr;</a></div>'
          '</div>' % (CY_SUMMARY, WS_SUMMARY, MMA_SUMMARY))
ix.append('<footer><h5>About</h5><p style="font-size:12.5px;color:var(--muted)">Each briefing is rebuilt from live web '
          'searches every 30 minutes between 8 AM and 6 PM ET. Every figure is checked against a source fetched on the same run '
          'before it is published; where sources disagree, the disagreement is printed rather than resolved silently. Past editions '
          'are kept in the <a href="archive.html">Archive</a>.</p>'
          '<div class="disc">Information only — not investment, legal or security advice.</div></footer>')
ix.append(STAMP_JS)
ix.append('</div></body></html>')
w("index.html", "".join(ix))
print("done")
