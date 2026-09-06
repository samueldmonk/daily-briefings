# -*- coding: utf-8 -*-
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shared
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date(2026, 9, 6)

def days_left(y, m, d):
    return (datetime.date(y, m, d) - TODAY).days

def cd(y, m, d):
    n = days_left(y, m, d)
    if n > 0:
        return '<span class="mut">(%d day%s left)</span>' % (n, "" if n == 1 else "s")
    if n == 0:
        return '<span class="down"><b>(due today)</b></span>'
    return '<span class="down"><b>(overdue by %d day%s)</b></span>' % (-n, "" if -n == 1 else "s")

def freshline():
    return '<div class="freshline" id="freshline">&nbsp;</div>'

def tldr(label, text):
    return '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (label, text)

def srcs(pairs):
    out = ['<h2 class="sec">Sources</h2><div class="panel srcs">']
    out.append(" &nbsp;&middot;&nbsp; ".join('<a href="%s">%s</a>' % (u, t) for t, u in pairs))
    out.append("</div>")
    return "".join(out)

def disc(t):
    return '<div class="disc">%s</div>' % t

# ---------------------------------------------------------------- CYBER
cy_extra = ""

cy_body = []
cy_body.append(masthead("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, vulnerabilities &amp; federal deadlines"))
cy_body.append(tldr("The Wire",
    "Attackers are actively exploiting a maximum-impact arbitrary-file-upload flaw in the Elementor Pro "
    "WordPress plugin that roughly two-thirds of Elementor&rsquo;s 10 million installs had still not patched as of "
    "Friday, while the seven vulnerabilities CISA added to its KEV catalog on 2 September blew past their "
    "federal remediation deadline yesterday."))
cy_body.append(freshline())
cy_body.append(nav("cyber"))

cy_body.append("""<div class="banner">
<span class="lvl">Threat level: High</span>
<span style="flex:1;min-width:220px;font-size:14px">Two separate unauthenticated remote-takeover chains &mdash; Elementor Pro on WordPress and the MikroTik RouterOS &ldquo;MikroTrick&rdquo; chain &mdash; are confirmed under active exploitation, and five KEV entries carrying a 5 September federal deadline are now past due.</span>
</div>""")

cy_body.append("""<div class="stats">
<div class="stat"><div class="n">9.8</div><div class="l">CVSS of CVE-2026-32475, the exploited Elementor Pro file-upload flaw</div></div>
<div class="stat"><div class="n">190,000+</div><div class="l">Exploit attempts against it blocked to date, per Defiant</div></div>
<div class="stat"><div class="n">8.8M</div><div class="l">Email addresses &amp; phone numbers in the leaked Manchester Airports Group dataset, per HaveIBeenPwned</div></div>
<div class="stat"><div class="n">7</div><div class="l">Vulnerabilities CISA added to the KEV catalog on 2 September</div></div>
</div>""")

cy_body.append('<h2 class="sec">Top Story</h2>')
cy_body.append("""<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">Elementor Pro flaw is being exploited against WordPress sites &mdash; and most installs are still vulnerable</h3>
<p style="margin:0 0 10px">WordPress security firm Defiant warns that threat actors are exploiting <b>CVE-2026-32475</b> (CVSS 9.8), an arbitrary file upload issue in the Elementor Pro form-submission handler. When the plugin&rsquo;s validation loop hits an upload slot marked empty it triggers an error and returns, so every remaining file in that field is written to disk unchecked. An attacker submits an upload field as an array &mdash; an empty slot to trigger the return, then a PHP payload &mdash; and can then request the uploaded file to execute it. &ldquo;As a result, an unauthenticated attacker can request the uploaded file to execute their PHP payload on the server,&rdquo; Defiant explains, noting this could lead to full site compromise.</p>
<p style="margin:0 0 10px">The bug affects <b>all Elementor Pro versions up to 4.2.1</b> and was patched in <b>4.2.2 on 19 August</b>. According to Defiant, attackers began exploiting it immediately after the fixes landed, and the firm has <b>blocked over 190,000 exploit attempts</b> to date. Elementor Pro has over 6 million active installations; per WordPress data cited by Defiant, roughly <b>two-thirds of Elementor&rsquo;s 10 million installations were running a vulnerable version as of 4 September</b>.</p>
<p style="margin:0"><b>Indicators of compromise.</b> Successful exploitation writes a PHP file into <span style="font-family:var(--mono);font-size:13px">/wp-content/uploads/elementor/forms/</span> &mdash; the presence of any PHP file in that directory is a strong IoC. Administrators are also advised to review logs for requests to <span style="font-family:var(--mono);font-size:13px">/wp-admin/admin-ajax.php</span> and to check for backdoors if any evidence of compromise turns up. <span class="mut">This flaw carries no CISA KEV entry this run could verify, so no federal deadline is asserted for it.</span></p>
</div>""")

cy_body.append("""<div class="callout crit">
<h3>Patch Priority &mdash; overdue</h3>
<p style="margin:0 0 8px">The five KEV entries added on <b>2 September</b> that were not granted an extension carried a federal remediation deadline of <b>Saturday 5 September 2026</b> under BOD 26-04. That date has passed. The most severe of the group is <b>CVE-2026-83548 &mdash; SonicWall SMA 1000 (CVSS 10.0)</b>, an unauthenticated server-side request forgery that SonicWall says it investigated &ldquo;a case indicating the active exploitation&rdquo; of; <b>CVE-2026-49869 &mdash; Kestra OSS (CVSS 10.0)</b> shares the same score. Agencies past due should treat these as an incident-response matter, not a patch-backlog item.</p>
<p style="margin:0"><span class="mut">The highest-volume exploitation right now is CVE-2026-32475 in Elementor Pro (fixed in 4.2.2), but it is not KEV-listed and carries no federal deadline &mdash; the red status here is earned by the elapsed 5 September date, and matches the KEV section below.</span></p>
</div>""")

cy_body.append('<h2 class="sec">Threat Actor Spotlight</h2>')
cy_body.append("""<div class="panel">
<div class="tags"><span class="t hot">Extortion</span><span class="t">Data theft</span><span class="t">Spotlight</span></div>
<h3 style="margin:0 0 8px;font-size:18px">FulcrumSec</h3>
<p class="note" style="margin:0 0 9px">Replaces Rhysida in this slot. <b>Not tagged New:</b> a grep of the previous archived edition found FulcrumSec already named there as the MAG claimant &mdash; it is newly the subject of the spotlight, which is not the same thing as a new development.</p>
<p style="margin:0 0 9px">The extortion group that claimed the Manchester Airports Group breach over the weekend and, after MAG refused to pay, published roughly <b>550 GB of uncompressed data</b>. The group has admitted MAG did not pay a ransom.</p>
<p style="margin:0 0 9px"><b>Tradecraft worth copying into your own threat model:</b> the group says it got in using admin keys for the customer-engagement platform Iterable that were sitting <i>&ldquo;in the frontend JavaScript of each of its three airports&rsquo; websites&rdquo;</i> &mdash; not on an obscure subdomain, but on each site&rsquo;s root domain. Client-side secrets remain a live initial-access path.</p>
<p style="margin:0">FulcrumSec claims the haul includes <b>2,482,763 purchases</b> (parking, lounge and fast-track bookings), <b>461,433 booking-related SMS messages</b>, and <b>108,077 unique UK vehicle registration plates</b>, plus the platform&rsquo;s configuration. <span class="mut">SecurityWeek states it has not independently verified the attackers&rsquo; claims, and neither has this desk.</span></p>
</div>""")

cy_body.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
cy_body.append("""<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">Aviation</span><span class="t new">New</span></div>
<h3>Manchester Airports Group &mdash; escalated to 8.8 million people</h3>
<p>MAG disclosed that attackers stole car park, lounge and Fast Track booking data plus in-airport Wi-Fi sign-ups across Manchester, London Stansted and East Midlands, and confirmed a ransom demand. After MAG declined, FulcrumSec published ~550 GB. HaveIBeenPwned parsed the dataset and logged roughly <b>8.8 million email addresses and phone numbers</b>, along with names, browser agent details, purchases and vehicle registration plates; the group itself claims ~8.7 million individuals. MAG says at no point was passenger safety or aviation security compromised.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">Manufacturing</span><span class="t new">New</span></div>
<h3>Tata Electronics &mdash; 630 GB posted by World Leaks</h3>
<p>The World Leaks group posted <b>204,341 files totalling over 630.4 GB</b> of Tata Electronics data to its dark-web leak site on 12 June 2026, after a ransom demand. The cache is reported to include purported component design papers from Apple and Tesla, both Tata clients, plus files attributed to TSMC and Qualcomm. Tata Electronics confirmed the incident on 22 June and said it caused no disruption to operations. World Leaks launched in early 2025 and is widely believed to be a rebrand of Hunters International.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Healthcare</span></div>
<h3>Aesto Health &mdash; 9.5 million individuals</h3>
<p>An intrusion dating to December 2025 that indirectly touched 29 provider organisations, including VillageMD, Everside Health (Marathon Health), Marana Health and Together Women&rsquo;s Health.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">Government</span></div>
<h3>Berlin / Rhysida &mdash; 5.79 TB, city refuses to pay</h3>
<p>Rhysida claims roughly 1.44 million files, including 148 IBANs, 3,200-plus documents marked as under NDA and water-supply infrastructure assessments, against a 30 BTC demand. Berlin has refused to pay. Reported exfiltration ran 7&ndash;12 August, with detection and isolation on 14 August.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Identity</span></div>
<h3>&ldquo;Nexus&rdquo; &mdash; 153 million driver&rsquo;s licence images offered</h3>
<p>A dark-web listing reported by Brian Krebs offers <b>153 million-plus</b> driver&rsquo;s licence images, tracing back to IDScan.net, with the FBI reported to be investigating. Published here as a reported claim.</p>
</div>
</div>""")

cy_body.append('<h2 class="sec">Vulnerability Watch</h2>')
cy_body.append("""<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td>CVE-2026-32475</td><td class="down"><b>9.8</b></td><td>Elementor Pro &le; 4.2.1 (WordPress)</td><td>Arbitrary file upload &rarr; unauthenticated RCE. <b>Actively exploited.</b> Fixed in 4.2.2 (19 Aug).</td></tr>
<tr><td>CVE-2026-83548</td><td class="down"><b>10.0</b></td><td>SonicWall SMA 1000</td><td>Unauthenticated SSRF. <b>KEV, exploited.</b> Deadline was 5 Sep.</td></tr>
<tr><td>CVE-2026-49869</td><td class="down"><b>10.0</b></td><td>Kestra OSS</td><td>OS command injection; unauthenticated workflow creation and execution. <b>KEV, exploited.</b></td></tr>
<tr><td>CVE-2026-75754</td><td class="down"><b>10.0</b></td><td>ASUS Control Center Enterprise</td><td>Missing auth + SSRF + key exposure &rarr; unauthenticated remote root. Fixed version reported inconsistently &mdash; see note.</td></tr>
<tr><td>CVE-2026-82329</td><td class="down"><b>9.8</b></td><td>JFrog Artifactory (default config)</td><td>Improper authentication &rarr; administrative privileges. <b>KEV, exploited</b> (watchTowr).</td></tr>
<tr><td>CVE-2026-9586</td><td class="down"><b>9.3</b></td><td>Sangoma Switchvox</td><td>Unauthenticated SQL injection via PhoneIP into PostgreSQL &rarr; RCE. <b>KEV, exploited</b> from 30 Aug (Horizon3).</td></tr>
<tr><td>CVE-2026-67276</td><td class="down"><b>9.2</b></td><td>MikroTik RouterOS (SSH)</td><td>SSH auth bypass &mdash; RouterOS did not compare the entire RSA public key. Half of the &ldquo;MikroTrick&rdquo; chain; <b>exploited in the wild</b> per CERT Polska.</td></tr>
<tr><td>CVE-2026-86060</td><td class="down"><b>9.2</b></td><td>MikroTik RouterOS (SSH)</td><td>Crafted-username privilege manipulation &rarr; full admin session. Chains with the above for full unauthenticated takeover.</td></tr>
<tr><td>CVE-2026-59822</td><td><b>8.8</b></td><td>Berri LiteLLM (MCP Streamable HTTP)</td><td>Improper authentication &mdash; authenticated MCP session from an arbitrary Bearer token. <b>KEV;</b> Wiz honeypots caught attempts.</td></tr>
<tr><td>CVE-2026-67277</td><td><b>8.8</b></td><td>MikroTik RouterOS (btest)</td><td>Uninitialised-memory disclosure / integer underflow &rarr; kernel memory leak or denial of service.</td></tr>
<tr><td>CVE-2026-48710</td><td><b>6.5</b></td><td>Kludex Starlette</td><td>HTTP request/response smuggling; path injection into the host part &rarr; auth bypass. <b>KEV;</b> exploited since May.</td></tr>
</table>
<p class="note"><b>Two things this desk will not assert.</b> (1) <b>ASUS ACC:</b> reporting says versions through 4.0.0.2 are affected and advises updating to &ldquo;3.1.0.9 or later&rdquo; &mdash; a <i>lower</i> build. Both figures are printed as reported; neither is asserted as the fixed version. Consistent mitigations across returns: isolate ACC interfaces, restrict TCP 2222, audit for unexpected SSH listeners. (2) <b>MikroTik:</b> MikroTik&rsquo;s own 3 September bulletin says it is not publishing detailed information yet, so only the three CVEs above are described; fixes are in 7.25 beta 3 / 7.24.2 / 7.23.4 / 6.49.21. CERT Polska IoCs: log lines <span style="font-family:var(--mono);font-size:12.5px">login failure for user -2 from &lt;ip&gt; via ssh</span> and <span style="font-family:var(--mono);font-size:12.5px">user &lt;name&gt; added by ssh:-2@&lt;ip&gt;</span>; a privileged user named <b>ops</b>; source IPs <b>82.192.72.4</b> (active since at least 2 September) and <b>103.102.31.18</b>.</p>""")

cy_body.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
cy_body.append("""<div class="panel">
<p style="margin:0 0 11px">CISA added <b>seven</b> vulnerabilities to the Known Exploited Vulnerabilities catalog on <b>Wednesday 2 September 2026</b>. Remediation windows are set under <b>BOD 26-04, &ldquo;Prioritizing Security Updates Based on Risk&rdquo;</b> &mdash; risk-based windows that supersede BOD 22-01&rsquo;s uniform three weeks.</p>
<ul class="bul">
<li><b>Due Saturday 5 September 2026</b> %s &mdash; <b>CVE-2026-83548</b> (SonicWall SMA 1000 SSRF, 10.0), <b>CVE-2026-83549</b> (SonicWall SMA 1000 post-auth OS command injection, 7.8), <b>CVE-2026-9586</b> (Sangoma Switchvox SQL injection, 9.3), <b>CVE-2026-82329</b> (JFrog Artifactory improper authentication, 9.8) and <b>CVE-2026-49869</b> (Kestra OSS command injection, 10.0).</li>
<li><b>Due Wednesday 16 September 2026</b> %s &mdash; <b>CVE-2026-48710</b> (Kludex Starlette request smuggling, 6.5) and <b>CVE-2026-59822</b> (Berri LiteLLM improper authentication, 8.8).</li>
<li><b>One reported discrepancy, stated rather than resolved.</b> The Hacker News, citing the CISA alert, places every CVE except 48710 and 59822 in the 5 September group &mdash; which puts Kestra there. SecurityWeek instead describes a three-day window &ldquo;except for the Kestra and Starlette flaws, which should be patched within two weeks.&rdquo; Two of three returns this run put Kestra on 5 September and that is what is printed above; the conflict is noted rather than hidden. <span class="mut">The CISA alert page itself returned empty on fetch again this run, so these dates are attributed to reporting.</span></li>
<li><b>No KEV entry and no deadline asserted</b> for Elementor Pro (CVE-2026-32475), the MikroTik RouterOS chain, or ASUS Control Center Enterprise &mdash; all three are exploited or maximum-severity, but none could be confirmed KEV-listed this run.</li>
</ul>
</div>""" % (cd(2026, 9, 5), cd(2026, 9, 16)))

cy_body.append(srcs([
    ("SecurityWeek &mdash; Elementor Pro exploited", "https://www.securityweek.com/elementor-pro-wordpress-plugin-vulnerability-exploited-to-hack-sites/"),
    ("SecurityWeek &mdash; Sangoma Switchvox exploited / KEV batch", "https://www.securityweek.com/sangoma-switchvox-vulnerabilities-exploited-in-the-wild/"),
    ("SecurityWeek &mdash; MAG data on 8.8 million leaked", "https://www.securityweek.com/manchester-airports-group-data-on-8-8-million-people-leaked-after-ransom-refusal/"),
    ("The Hacker News &mdash; CISA adds seven exploited flaws", "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
    ("CISA &mdash; KEV catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
    ("CISA alert &mdash; 2 Sep additions", "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
    ("CERT Polska &mdash; MikroTik RouterOS actively exploited", "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"),
    ("MikroTik &mdash; September 2026 vulnerability", "https://mikrotik.com/supportsec/september-2026-vulnerability/"),
    ("HaveIBeenPwned &mdash; MAG breach", "https://haveibeenpwned.com/Breach/ManchesterAirportsGroup"),
    ("Cybernews &mdash; Tata Electronics breach", "https://cybernews.com/security/tata-electronics-breach-apple-tesla-secret-files/"),
    ("NVD &mdash; CVE-2026-9586", "https://nvd.nist.gov/vuln/detail/cve-2026-9586"),
    ("Wordfence / Defiant &mdash; Elementor Pro exploitation", "https://www.wordfence.com/blog/2026/09/attackers-actively-exploiting-critical-vulnerability-in-elementor-pro-plugin/"),
]))
cy_body.append(disc("Compiled from public reporting fetched during this run. Vulnerability details, CVSS scores and remediation deadlines are reproduced as published by the cited sources and may be revised; verify against your vendor&rsquo;s advisory before acting. Not security advice for any specific environment."))

cyber = page("The Cyber Wire &mdash; Daily Briefings",
             css("#22d3a8", "#36c6ff", "#0b0f0e", "#121918", "#1e2b28", cy_extra),
             "\n".join(cy_body))

# ---------------------------------------------------------------- WALL STREET
ws_extra = """
.masthead h1,.card h3,.panel h3{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:8px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""

TV_TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:TSLA","title":"Tesla"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"NASDAQ:AMD","title":"AMD"},{"proName":"NYSE:XOM","title":"Exxon"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:UKOIL","title":"Brent"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""

def sq(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)

ws_body = []
ws_body.append(masthead("The Closing Bell", "Your daily markets briefing &mdash; the tape, the drivers &amp; what&rsquo;s next"))
ws_body.append(tldr("The Tape",
    "U.S. markets are closed for the weekend and shut again Monday for Labor Day, leaving Friday&rsquo;s lower close "
    "as the last word: August payrolls came in at 162,000 against a 53,000 consensus, sending the 10-year yield to "
    "4.79% and hardening the case for a Fed hike at the 15&ndash;16 September meeting."))
ws_body.append(freshline())
ws_body.append(nav("ws"))
ws_body.append(TV_TICKER)

ws_body.append('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>')
ws_body.append('<div class="tickers">%s%s%s</div>' % (sq("FOREXCOM:SPXUSD"), sq("FOREXCOM:NSXUSD"), sq("FOREXCOM:DJI")))
ws_body.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>')

ws_body.append('<h2 class="sec">The Lead</h2>')
ws_body.append("""<div class="panel">
<h3 style="margin:0 0 9px;font-size:21px">A hot jobs number closed the week &mdash; and the next real test doesn&rsquo;t come until Thursday</h3>
<p style="margin:0 0 10px"><b>Markets are closed.</b> It is Sunday, and U.S. equity and bond markets are shut again on <b>Monday 7 September for Labor Day</b>, with the next session on <b>Tuesday 8 September</b>. Everything below reflects Friday 4 September, the most recent completed session.</p>
<p style="margin:0 0 10px">Stocks fell and Treasury yields rose after August nonfarm payrolls grew <b>162,000</b> &mdash; far above the <b>53,000</b> economists polled by Dow Jones had expected. The unemployment rate was <b>4.1%</b>, and average hourly earnings rose <b>0.3% month-over-month to $37.75</b>, up <b>3.1% year-over-year</b>. The read pushed traders toward pricing a Fed <i>hike</i> rather than a cut this month.</p>
<p style="margin:0">Under the surface the week was close to flat: the <b>S&amp;P 500 rose 0.1%</b>, the <b>Nasdaq rose 0.4%</b> and the <b>Dow fell 0.3%</b> across the five sessions. The bigger move was in energy, where Brent settled at <b>$96.28</b> after renewed U.S.&ndash;Iran hostilities &mdash; Kuwait&rsquo;s army reported missile and drone attacks from Iran on 3 September, and Strait of Hormuz traffic thinned to four vessels transiting Thursday against a 10-day average of 15.</p>
</div>""")

ws_body.append('<h2 class="sec">Movers &amp; Drivers</h2>')
ws_body.append("""<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">Down</span><span class="t new">New</span></div>
<h3>Tesla &minus;5.92%</h3>
<p>Shares fell after the Cybercab launch event underwhelmed Wall Street. Elon Musk was not at the private Austin event, attendance was limited to a small group of shareholders and content creators under NDA, and Tesla &mdash; which usually livestreams &mdash; did not stream it. The stock was further pressured after NHTSA opened an <b>&ldquo;audit query&rdquo;</b> into whether Tesla correctly self-certified that the Cybercab is safe for public road use and meets federal safety standards. Volume hit <b>64.4 million shares</b>, about <b>53% above</b> its three-month average of 42.1 million.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Up</span></div>
<h3>CDTG +43.27%</h3>
<p>The top gainer on ChartMill&rsquo;s 4 September U.S. market-movers screen for the regular session. Published as screen output; no narrative is attached because none was sourced.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Sectors</span></div>
<h3>Technology led, healthcare lagged</h3>
<p>S&amp;P sector winners on Friday were <b>Technology (XLK)</b>, <b>Industrials (XLI)</b> and <b>Utilities (XLU)</b>. The day&rsquo;s biggest losers were <b>Healthcare (XLV)</b>, <b>Consumer Discretionary (XLY)</b>, <b>Communications (XLC)</b> and <b>Energy (XLE)</b> &mdash; energy lagging even as crude rallied.</p>
</div>
</div>""")

ws_body.append('<h2 class="sec">Chart of the Day &mdash; Tesla (TSLA)</h2>')
ws_body.append("""<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NASDAQ:TSLA","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>
<p class="note">The session&rsquo;s signature single-stock move: Tesla closed down 5.92% on 4 September on the Cybercab reception and the NHTSA audit query.</p>""")

ws_body.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
ws_body.append("""<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>
</div>
<p class="note">Friday&rsquo;s sector split: Technology, Industrials and Utilities higher; Healthcare, Consumer Discretionary, Communications and Energy lower. <span class="mut">No VIX level is published &mdash; none was sourced this run.</span></p>""")

ws_body.append('<h2 class="sec">The Calendar &mdash; live</h2>')
ws_body.append("""<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script>
</div>""")

ws_body.append('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
ws_body.append("""<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script>
</div>""")

ws_body.append('<h2 class="sec">Weekly Scorecard</h2>')
ws_body.append("""<table>
<tr><th>Index</th><th>Friday 4 Sep close</th><th>Friday change</th><th>Week</th></tr>
<tr><td><b>S&amp;P 500</b></td><td>7,718.60</td><td class="down">&minus;0.38%</td><td class="up">+0.1%</td></tr>
<tr><td><b>Nasdaq Composite</b></td><td>26,506.99</td><td class="down">&minus;0.29%</td><td class="up">+0.4%</td></tr>
<tr><td><b>Dow Jones Industrial Average</b></td><td>53,414.25</td><td class="down">&minus;271.86 / &minus;0.51%</td><td class="down">&minus;0.3%</td></tr>
</table>
<p class="note">Official closes for the most recent completed session. The Dow arithmetic checks: 53,686.11 &minus; 271.86 = 53,414.25. Weekly figures are the change across the week ended 4 September.</p>""")

ws_body.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
ws_body.append("""<table>
<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>
<tr><td>US 10-year Treasury yield</td><td><b>4.79%</b></td><td class="mut">Rose nearly 3 basis points Friday on the payrolls beat.</td></tr>
<tr><td>Brent crude</td><td><b>$96.28</b></td><td class="mut">Friday close; higher on renewed U.S.&ndash;Iran hostilities.</td></tr>
<tr><td>WTI crude</td><td><b>~$91</b></td><td class="mut">Traded near $91 on Friday. No settle figure is asserted &mdash; none was sourced.</td></tr>
<tr><td>2-year / 30-year yields</td><td class="mut">Not published</td><td class="mut">The only figures returned this run were undated and conflicted with the last verified readings; withheld.</td></tr>
<tr><td>Fed funds target range</td><td class="mut">Not published</td><td class="mut">No current range was sourced this run.</td></tr>
</table>
<p class="note"><b>On the weekly crude move, this desk declines to pick a number.</b> Three returns this run gave the Brent weekly gain as roughly 5%, 7.6% and &ldquo;nearly 9%&rdquo;. The $96.28 settle is corroborated; the weekly percentage is not, so it is described only as sharply higher.</p>""")

ws_body.append('<h2 class="sec">On the Radar</h2>')
ws_body.append("""<ul class="bul">
<li><b>Monday 7 September &mdash; Labor Day.</b> U.S. stock and bond markets closed. Next session Tuesday 8 September.</li>
<li><b>Thursday 10 September &mdash; PPI</b>, 8:30 AM ET. Deutsche Bank expects headline producer prices <b>+0.2%</b> and core PPI <b>+0.3%</b>.</li>
<li><b>Friday 11 September &mdash; CPI</b>, 8:30 AM ET. The week&rsquo;s main event for the rate path; officials may weight the CPI and PPI reports more heavily than the jobs report in shaping the mid-month decision.</li>
<li><b>Tuesday 15 &ndash; Wednesday 16 September &mdash; FOMC</b>, decision Wednesday 2:00 PM ET. The pre-meeting quiet period began Saturday 5 September and runs through Thursday 17 September.</li>
<li><b>Earnings:</b> GameStop Tuesday 8 September; Chewy Wednesday 9 September; Oracle, Macy&rsquo;s and Adobe Thursday 10 September.</li>
<li><b>The rate call is genuinely contested and this desk is not drawing an arrow.</b> Returns this run put September hike odds at <b>58%</b>, <b>~56%</b> and <b>60%</b> after Jackson Hole, with several outlets calling it &ldquo;a coin flip.&rdquo; Fed Chair <b>Kevin Warsh&rsquo;s</b> 28 August Jackson Hole remarks &mdash; that underlying inflation is not slowing &mdash; were read as hawkish and roughly doubled hike odds from a prior reading near 30%. Other desks disagree outright: Goldman Sachs has called a September hike &ldquo;very unlikely.&rdquo; No single probability is published here.</li>
</ul>""")

ws_body.append(srcs([
    ("CNBC &mdash; Stock market news for Sept. 4, 2026", "https://www.cnbc.com/2026/09/03/stock-market-today-live-updates.html"),
    ("TheStreet &mdash; Stock Market Today, Sept. 4", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-04-2026"),
    ("Washington Post &mdash; How major US stock indexes fared Friday 9/4/2026", "https://www.washingtonpost.com/business/2026/09/04/stock-market-dow-nasdaq-jobs/b9e994e6-a89f-11f1-9e38-f705d048bd5a_story.html"),
    ("CNBC &mdash; Tesla stock drops as Cybercab update underwhelms", "https://www.cnbc.com/2026/09/04/teslas-stock-drops-as-cybercab-update-underwhelms-nhtsa-probe.html"),
    ("Motley Fool &mdash; Why Did Tesla Stock Fall Today?", "https://www.fool.com/investing/2026/09/04/why-did-tesla-stock-fall-today/"),
    ("CNBC &mdash; Oil prices post weekly gain on US-Iran fighting", "https://www.cnbc.com/2026/09/04/oil-set-for-steepest-weekly-gain-over-renewed-us-iran-tensions.html"),
    ("Trading Economics &mdash; US 10-year Treasury yield", "https://tradingeconomics.com/united-states/government-bond-yield"),
    ("Trading Economics &mdash; Brent crude", "https://tradingeconomics.com/commodity/brent-crude-oil"),
    ("Kiplinger &mdash; Economic calendar, September 7&ndash;11", "https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar"),
    ("CNBC &mdash; September Fed decision now a coin flip", "https://www.cnbc.com/2026/08/28/-september-fed-decision-now-a-coin-flip-as-rate-hike-odds-increase.html"),
    ("ChartMill &mdash; U.S. market movers, September 4, 2026", "https://www.chartmill.com/news/CDTG/Chartmill-54419-US-Market-Movers-Top-Gainers-and-Losers-for-September-4-2026"),
]))
ws_body.append(disc("For information only. Nothing here is investment advice, a recommendation, or an offer to buy or sell any security. Figures are reproduced from the cited sources and may be revised; live widgets are supplied by TradingView and some feeds are delayed. Verify prices with your broker before trading."))

ws = page("The Closing Bell &mdash; Daily Briefings",
          css("#caa64a", "#e8c766", "#0d0c0a", "#171511", "#2b2720", ws_extra),
          "\n".join(ws_body))

# ---------------------------------------------------------------- MMA
mm_extra = """
.cdbar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 17px;margin-bottom:16px;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdbar .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.cdbar .val{font-family:var(--mono);font-size:19px;color:var(--txt)}
.cdbar .ev{font-size:14px;color:var(--muted)}
.dv{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--warn);margin-bottom:6px}
"""

mm_body = []
mm_body.append(masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
mm_body.append(tldr("Tale of the Tape",
    "Salahdine Parnasse stopped Dan Hooker in the first round on his UFC debut in Paris on Saturday, taking one of "
    "four Performance of the Night bonuses on a sold-out card that UFC.com says became the highest-grossing event "
    "in Accor Arena history."))
mm_body.append(freshline())
mm_body.append(nav("mma"))

mm_body.append("""<div class="cdbar">
<span class="lab">Next card</span>
<span class="val" id="ufccdn">&nbsp;</span>
<span class="ev">Noche UFC: Silva vs. Delgado &middot; Sat 12 Sep &middot; Desert Diamond Arena, Glendale, AZ &middot; main card 5:00 PM ET</span>
</div>""")

mm_body.append('<h2 class="sec">Top Story</h2>')
mm_body.append("""<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">Parnasse arrives: a first-round finish of Dan Hooker, on debut, in a main event, at home</h3>
<p style="margin:0 0 10px">Salahdine Parnasse made his UFC debut in the <b>UFC Paris</b> main event on <b>Saturday 5 September</b> at Accor Arena and stopped <b>Dan Hooker</b> inside a round. About halfway through the opening round Parnasse landed a body kick that, in UFC.com&rsquo;s account, &ldquo;got Hooker&rsquo;s attention,&rdquo; then followed with a flurry against the fence to send Hooker crashing to the canvas. The 28-year-old has now <b>won six straight, all by stoppage</b>, and UFC.com says he &ldquo;instantly enters the highly touted lightweight Top 15.&rdquo;</p>
<p style="margin:0 0 10px">Parnasse is a <b>former two-time KSW featherweight champion and one-time KSW lightweight champion</b> &mdash; UFC.com calls him &ldquo;a two-division champion outside of the UFC&rdquo; &mdash; who signed with the promotion in late July 2026 having previously turned it down, and was handed a five-round main event on debut. He is <b>not</b> a Dana White&rsquo;s Contender Series signee.</p>
<p style="margin:0"><b>One number this desk will not assert: the stoppage time.</b> UFC.com&rsquo;s own main-card results page heads the bout <i>&ldquo;TKO, Round 1, 2:25&rdquo;</i>, while Yahoo Sports, Sherdog and other reporting give <b>2:35</b>. Both are noted here; the table below records the result as TKO, Round 1, with no stamp.</p>
</div>""")

mm_body.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
mm_body.append("""<div class="cards">
<div class="card">
<div class="dv">Sat 12 Sep &middot; Desert Diamond Arena, Glendale, AZ</div>
<h3>Noche UFC: Silva vs. Delgado</h3>
<p>The fourth annual Noche UFC, on Mexican Independence Day weekend. Featherweight <b>Jean Silva</b> meets Arizona&rsquo;s <b>Jose Miguel Delgado</b> in the main event &mdash; former interim featherweight champion <b>Yair Rodr&iacute;guez</b> was originally booked opposite Silva but withdrew injured and was replaced by Delgado, which is why some listings still carry the old billing. Also on the card: <b>Brandon Moreno vs. Joseph Morales</b>, the TUF season 33 winner, and <b>Manon Fiorot vs. Alexa Grasso</b> &mdash; a card bout, not the headliner. Prelims 2:00 PM ET, main card 5:00 PM ET on Paramount+.</p>
</div>
<div class="card">
<div class="dv">Sat 19 Sep &middot; Crypto.com Arena, Los Angeles</div>
<h3>UFC 331: Van vs. Pantoja 2</h3>
<p>Flyweight champion <b>Joshua Van</b> defends against <b>Alexandre Pantoja</b> in a rematch of their UFC 323 meeting in December 2025, which Van won by technical knockout 26 seconds into the first round after Pantoja suffered an arm injury. Co-main: <b>Arman Tsarukyan vs. Mauricio Ruffy</b> over five rounds. Also booked: <b>Renato Moicano vs. Brian Ortega 2</b>, <b>Patricio Pitbull vs. Doo Ho Choi</b>, <b>Charles Jourdain vs. Marlon Vera</b>, and Gable Steveson. Thirteen fights. Early prelims about 5:00 PM ET, prelims 7:00 PM ET, main card 9:00 PM ET.</p>
</div>
<div class="card">
<div class="dv">Tue 15 Sep &middot; Meta Apex, Las Vegas</div>
<h3>Dana White&rsquo;s Contender Series &mdash; Week 6</h3>
<p>Season 10 continues on Tuesday nights on Paramount+ at 7:00 PM ET, with Week 7 following on Tuesday 22 September. The season runs across ten weekly episodes from August into October 2026.</p>
</div>
</div>
<p class="note"><b>No betting odds are published this edition</b> &mdash; no source fetched this run stated a line for any of the headliners above.</p>""")

mm_body.append('<h2 class="sec">Last Event &mdash; UFC Paris, Saturday 5 September</h2>')
mm_body.append("""<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up"><b>Parnasse</b></td><td>Salahdine Parnasse def. Dan Hooker <span class="mut">(main event, lightweight)</span></td><td>TKO, R1 <span class="mut">&mdash; time reported as 2:25 (UFC.com) or 2:35 (other outlets); not asserted</span></td></tr>
<tr><td class="up"><b>Sola</b></td><td>Axel Sola def. Far&egrave;s Ziam <span class="mut">(co-main, lightweight)</span></td><td>KO, R1 1:40 <span class="mut">&mdash; overhand left</span></td></tr>
<tr><td class="up"><b>Page</b></td><td>Michael &ldquo;Venom&rdquo; Page def. Nursulton Ruziboev <span class="mut">(middleweight)</span></td><td>Unanimous decision (29&ndash;28, 29&ndash;28, 29&ndash;28)</td></tr>
<tr><td class="up"><b>Donchenko</b></td><td>Daniil Donchenko def. Punahele Soriano</td><td>Unanimous decision (30&ndash;27, 30&ndash;27, 29&ndash;28)</td></tr>
<tr><td class="up"><b>Campbell</b></td><td>Kurtis Campbell def. Trevor Peek</td><td>Submission, rear-naked choke, R3 3:07</td></tr>
<tr><td class="up"><b>Keita</b></td><td>Losene Keita def. Muhammad Naimov <span class="mut">(featherweight)</span></td><td>KO, R1 2:54 &mdash; right hand</td></tr>
<tr><td class="up"><b>Pinto</b></td><td>Mario Pinto def. Ryan Spann <span class="mut">(heavyweight)</span></td><td>Stoppage, R2 0:55 &mdash; ground-and-pound</td></tr>
<tr><td class="up"><b>Lima</b></td><td>Felipe Lima def. Morgan Charri&egrave;re <span class="mut">(prelims)</span></td><td>Unanimous decision (30&ndash;27, 29&ndash;28, 30&ndash;27)</td></tr>
</table>
<div class="panel" style="margin-top:14px">
<p style="margin:0 0 8px"><b>Bonuses &mdash; four Performance of the Night, no Fight of the Night.</b> UFC.com awarded Performance of the Night to <b>Salahdine Parnasse</b>, <b>Axel Sola</b>, <b>Losene Keita</b> and <b>Mario Pinto</b>. <span class="mut">UFC.com&rsquo;s own bonus page states no dollar amount; the $100,000 figure that circulates is attributed to MMA Mania, Sherdog, LowKick and Heavy rather than to the promotion.</span></p>
<p style="margin:0"><b>Gate and attendance, from UFC.com.</b> Gross total revenue <b>$4,365,335</b>; attendance <b>15,687 (sold out)</b>; the promotion records it as the <b>highest-grossing event in Accor Arena history</b>.</p>
</div>""")

mm_body.append('<h2 class="sec">Prospect Watch</h2>')
mm_body.append("""<div class="cards">
<div class="card">
<div class="tags"><span class="t pro">Prospect</span></div>
<h3>Axel Sola &mdash; lightweight</h3>
<p>The Nice native delivered what UFC.com called &ldquo;the knockout of his career,&rdquo; dropping Far&egrave;s Ziam with a left hand after about 90 seconds of feeling out. It was his <b>third Octagon appearance of 2026</b>, a <b>second straight first-round finish</b>, and a second win in Paris in as many starts there; he opened the year with a Fight of the Night performance opposite Mason Jones.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Prospect</span></div>
<h3>Losene Keita &mdash; featherweight</h3>
<p>The former Oktagon MMA double champion took his first UFC win, dropping Muhammad Naimov with a jab midway through the round and finishing with a clean right hook before scaling the Octagon wall and taking a front-row seat in the stands. He called out <b>Lerone Murphy</b> in a bilingual post-fight interview, after a close debut against Nathaniel Wood earlier this year.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Prospect</span></div>
<h3>Daniil Donchenko &mdash; 25, on an eight-fight run</h3>
<p>The Ultimate Fighter winner swept the cards against Punahele Soriano for a <b>third consecutive UFC win</b> and an <b>eight-fight winning streak</b>, hurting Soriano early and managing the rest. He called for a matchup with Daniel Rodriguez toward the end of the year.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Roster move</span></div>
<h3>Five DWCS contracts awarded, 1 September</h3>
<p>Week 4 of Contender Series season 10 ran at the Meta Apex in Las Vegas with a five-bout card and ten athletes. UFC CEO Dana White announced contract offers for all five winners: <b>Adam Darby</b>, <b>Modestino Rodrigues</b>, <b>Silvestre Sanchez</b>, <b>Gabriel Loren&ccedil;o</b> and <b>Adam Livingston</b>.</p>
</div>
</div>""")

mm_body.append('<h2 class="sec">Around the Sport</h2>')
mm_body.append("""<ul class="bul">
<li><b>Kurtis Campbell became the first fighter to finish Trevor Peek.</b> &ldquo;The Pink Panther&rdquo; took his first UFC win in his sophomore appearance, battering Peek with elbows from mount before working to the rear-naked choke in the third &mdash; a recovery after faltering on debut earlier this year.</li>
<li><b>Michael &ldquo;Venom&rdquo; Page has now won four straight</b> and all three of his middleweight appearances, though UFC.com&rsquo;s own account described the Ruziboev fight as &ldquo;a low-output jousting match&rdquo; that left viewers &ldquo;wanting more.&rdquo;</li>
<li><b>Mario Pinto remains undefeated</b> after overwhelming Ryan Spann with ground-and-pound 55 seconds into the second round, following a first round UFC.com described as back-and-forth with both men landing near fight-ending blows.</li>
<li><b>UFC 332 is being advertised for Salt Lake City</b> on UFC.com. <span class="mut">No date is asserted here &mdash; none appeared on any page fetched this run.</span></li>
</ul>""")

mm_body.append('<h2 class="sec">Rankings &amp; Business</h2>')
mm_body.append("""<div class="panel">
<p style="margin:0 0 9px"><b>Rankings movement.</b> UFC.com states Parnasse &ldquo;instantly enters the highly touted lightweight Top 15&rdquo; on the strength of the Hooker win. Hooker was listed at <b>#10</b> at lightweight going into the bout. <span class="mut">No other ranking changes were sourced this run, and no official post-event rankings update had been published at the time of writing.</span></p>
<p style="margin:0"><b>Business &amp; broadcast.</b> UFC Paris produced <b>$4,365,335</b> in gross total revenue against a sold-out <b>15,687</b>, a house record for Accor Arena. UFC events continue to stream on <b>Paramount+</b>, including Noche UFC on 12 September and Contender Series on Tuesday nights. <span class="mut">No viewership figures and no TKO Group financials were sourced this run, so none are published.</span></p>
</div>""")

mm_body.append('<h2 class="sec">Champions Board</h2>')
mm_body.append("""<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td><b>Tom Aspinall</b></td><td class="mut">Undisputed since 21 Jun 2025; 0 defences.</td></tr>
<tr><td>Interim Heavyweight</td><td><b>Ciryl Gane</b></td><td class="mut">KO2 Alex Pereira, UFC Freedom 250, 14 Jun 2026 &mdash; carried.</td></tr>
<tr><td>Light Heavyweight</td><td><b>Carlos Ulberg</b></td><td class="mut">KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, 11 Apr 2026; 0 defences.</td></tr>
<tr><td>Middleweight</td><td><b>Sean Strickland</b></td><td class="mut">Split decision over Khamzat Chimaev, UFC 328, 9 May 2026; two-time champion; 0 defences.</td></tr>
<tr><td>Welterweight</td><td><b>Islam Makhachev</b></td><td class="mut">UD over Jack Della Maddalena, UFC 322, 15 Nov 2025; 1 defence (UD Ian Machado Garry, UFC 330, 15 Aug 2026).</td></tr>
<tr><td>Lightweight</td><td><b>Justin Gaethje</b></td><td class="mut">TKO4 Ilia Topuria, UFC Freedom 250, 14 Jun 2026; 0 defences.</td></tr>
<tr><td>Featherweight</td><td><b>Alexander Volkanovski</b></td><td class="mut">UD over Diego Lopes, UFC 314, 12 Apr 2025; 1 defence. <b>Not vacant.</b></td></tr>
<tr><td>Bantamweight</td><td><b>Petr Yan</b></td><td class="mut">UD over Merab Dvalishvili, UFC 323, 6 Dec 2025 &mdash; carried, not re-confirmed this run.</td></tr>
<tr><td>Flyweight</td><td><b>Joshua Van</b></td><td class="mut">TKO1 Alexandre Pantoja, UFC 323, 6 Dec 2025; 1 defence. Defends against Pantoja again at UFC 331 &mdash; carried.</td></tr>
<tr><td>Women&rsquo;s Flyweight</td><td><b>Valentina Shevchenko</b></td><td class="mut">Carried, not re-confirmed this run.</td></tr>
<tr><td>Women&rsquo;s Bantamweight</td><td><b>Kayla Harrison</b></td><td class="mut">Sub2 Julianna Pe&ntilde;a, UFC 316, 7 Jun 2025; <b>0 defences</b> &mdash; the UFC 324 booking against Amanda Nunes was cancelled.</td></tr>
<tr><td>Women&rsquo;s Strawweight</td><td><b>Mackenzie Dern</b></td><td class="mut">UD over Virna Jandiroba, UFC 321, 25 Oct 2025; 1 defence (UD Gillian Robertson, UFC 330, 15 Aug 2026) &mdash; carried.</td></tr>
</table>
<p class="note"><b>Verification status.</b> An ESPN-sourced return this run re-confirmed <b>Aspinall, Ulberg, Strickland, Makhachev, Gaethje and Volkanovski</b> directly. <b>Gane, Yan, Van, Shevchenko, Harrison and Dern</b> were not in the return and are carried from this desk&rsquo;s standing record, labelled as carried above. UFC Paris was a non-title card, so no belt changed hands on Saturday; the most recent title bouts were at UFC 330 on 15 August.</p>""")

mm_body.append(srcs([
    ("UFC.com &mdash; Main Card Results, UFC Paris", "https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse"),
    ("UFC.com &mdash; Bonus Coverage, UFC Paris", "https://www.ufc.com/news/bonus-coverage-ufc-fight-night-paris-2026"),
    ("UFC.com &mdash; Prelim Results, UFC Paris", "https://www.ufc.com/news/ufc-paris-prelim-results-hooker-vs-parnasse"),
    ("ESPN &mdash; Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
    ("UFC.com &mdash; Noche UFC 2026", "https://www.ufc.com/noche-ufc-2026"),
    ("UFC.com &mdash; Van vs Pantoja 2 set for UFC 331", "https://www.ufc.com/news/flyweight-champion-joshua-van-set-rematch-alexandre-pantoja-cryptocom-ufc-331"),
    ("Al Jazeera &mdash; UFC 331 full fight card", "https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card"),
    ("Yahoo Sports &mdash; UFC Paris live results", "https://sports.yahoo.com/mma/live/ufc-paris-live-results-dan-hooker-vs-salahdine-parnasse-updates-round-by-round-scoring-for-todays-fight-063000135.html"),
    ("Sherdog &mdash; UFC Paris play-by-play", "https://www.sherdog.com/news/news/UFC-Paris-Hooker-vs-Parnasse-playbyplay-results-round-scoring-202671"),
    ("MMA Weekly &mdash; DWCS Week 4: five contracts awarded", "https://www.mmaweekly.com/news/dana-whites-contender-series-week-4-five-ufc-contracts-awarded"),
    ("Yahoo Sports &mdash; Noche UFC 4 card and start time", "https://sports.yahoo.com/articles/latest-noche-ufc-4-fight-131500339.html"),
]))
mm_body.append(disc("Cards and bouts are subject to change. Results, methods, times, bonuses and gate figures are reproduced from the cited sources; where sources disagree, the disagreement is stated rather than resolved. Not betting advice."))

MM_CD = """<script>(function(){var t=new Date('2026-09-12T17:00:00-04:00');function f(){var d=t-new Date();var e=document.getElementById('ufccdn');if(!e)return;if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/86400000),hh=Math.floor(d%86400000/3600000),mm=Math.floor(d%3600000/60000);e.textContent=dd+'d '+hh+'h '+mm+'m';}f();setInterval(f,30000);})();</script>"""

mma = page("The Octagon &mdash; Daily Briefings",
           css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020", mm_extra),
           "\n".join(mm_body) + "\n" + MM_CD)

# ---------------------------------------------------------------- INDEX
ix_extra = """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:15px}
.big .card{padding:19px 20px}
.big .card h3{font-size:19px;margin:0 0 4px}
.big .card .kick{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:9px}
.big .card p{font-size:14.5px;margin:0 0 13px}
.big .card a.read{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.c-sec{border-top:3px solid #22d3a8} .c-sec .kick,.c-sec a.read{color:#22d3a8}
.c-sec:hover{border-color:#22d3a8}
.c-mkt{border-top:3px solid #caa64a} .c-mkt .kick,.c-mkt a.read{color:#caa64a}
.c-mkt h3{font-family:Georgia,'Times New Roman',serif}
.c-mkt:hover{border-color:#caa64a}
.c-mma{border-top:3px solid #e84545} .c-mma .kick,.c-mma a.read{color:#e84545}
.c-mma:hover{border-color:#e84545}
"""

ix_body = []
ix_body.append(masthead("Daily Briefings", "Three desks, refreshed every 30 minutes &mdash; security, markets and the fight game"))
ix_body.append(freshline())
ix_body.append(nav("index"))
ix_body.append("""<div class="big">
<div class="card c-sec">
<div class="kick">&#9960; The Cyber Wire &middot; The Wire</div>
<h3>Elementor Pro exploited; KEV batch past its deadline</h3>
<p>Attackers are actively exploiting a maximum-impact arbitrary-file-upload flaw in the Elementor Pro WordPress plugin that roughly two-thirds of Elementor&rsquo;s 10 million installs had still not patched as of Friday, while the seven vulnerabilities CISA added to its KEV catalog on 2 September blew past their federal remediation deadline yesterday.</p>
<a class="read" href="cyber-briefing.html">Read the briefing &rarr;</a>
</div>
<div class="card c-mkt">
<div class="kick">&#9650; The Closing Bell &middot; The Tape</div>
<h3>A hot payrolls print, then a long weekend</h3>
<p>U.S. markets are closed for the weekend and shut again Monday for Labor Day, leaving Friday&rsquo;s lower close as the last word: August payrolls came in at 162,000 against a 53,000 consensus, sending the 10-year yield to 4.79% and hardening the case for a Fed hike at the 15&ndash;16 September meeting.</p>
<a class="read" href="wallstreet-briefing.html">Read the briefing &rarr;</a>
</div>
<div class="card c-mma">
<div class="kick">&#8856; The Octagon &middot; Tale of the Tape</div>
<h3>Parnasse stops Hooker on debut in Paris</h3>
<p>Salahdine Parnasse stopped Dan Hooker in the first round on his UFC debut in Paris on Saturday, taking one of four Performance of the Night bonuses on a sold-out card that UFC.com says became the highest-grossing event in Accor Arena history.</p>
<a class="read" href="mma-briefing.html">Read the briefing &rarr;</a>
</div>
</div>""")
ix_body.append(disc("Each briefing is compiled from public reporting fetched at the time of the run and links its own sources. Markets content is information only and not investment advice; security content is not advice for any specific environment; fight cards are subject to change."))

index = page("Daily Briefings", css("#8ab4f8", "#a6c8ff", "#0a0c10", "#12161d", "#222a35", ix_extra),
             "\n".join(ix_body))

for name, html in [("index.html", index), ("cyber-briefing.html", cyber),
                   ("wallstreet-briefing.html", ws), ("mma-briefing.html", mma)]:
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(name, len(html))
