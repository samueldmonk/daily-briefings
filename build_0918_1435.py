# -*- coding: utf-8 -*-
"""First run of 2026-09-18 (Friday), ~2:40pm ET. Afternoon Edition, markets OPEN."""
import os, datetime
from css import base_css, nav, head, sources, STAMP_JS

OUT = "/sessions/laughing-magical-cray/mnt/outputs"
TODAY = datetime.date(2026, 9, 18)
TV = 'https://s3.tradingview.com/external-embedding/embed-widget-%s.js'


def kevtxt(due):
    d = (due - TODAY).days
    if d > 1:
        return '%d days left' % d
    if d == 1:
        return '1 day left'
    if d == 0:
        return '0 days &mdash; due TODAY'
    return 'OVERDUE by %d days' % (-d)


def mast(title, sub):
    return ('<header class="masthead"><h1>%s</h1><p class="tag">%s</p>'
            '<div class="meta">'
            '<span class="pill live"><span class="dot"></span>Live</span>'
            '<span class="pill" id="edition">&nbsp;</span>'
            '<span class="pill" id="datestamp">&nbsp;</span>'
            '<span class="pill">Updated <span id="updated">&nbsp;</span></span>'
            '</div></header>' % (title, sub))


FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'
FOOT = '</div>' + STAMP_JS + '</body></html>'

DISC_WS = ('<div class="disc">Information only, not investment advice. Live widgets stream from TradingView and may be '
           'delayed; editorial figures carry the as-of time at which they were verified.</div>')
DISC_CY = ('<div class="disc">Compiled from public reporting and vendor advisories. Verify severity and patch status '
           'against your own vendor channels before acting.</div>')
DISC_MMA = '<div class="disc">Cards and bouts are subject to change. Odds move; figures are as published by the cited book.</div>'

# ---------------------------------------------------------------- TLDRs
TL_WS = ("Stocks slipped on Friday afternoon as the 10-year Treasury yield pushed back above 5%, with Trading "
         "Economics&rsquo; ~2:37 PM ET board showing its S&amp;P 500 proxy down 0.21% and its Dow proxy down 0.42% "
         "while chip producers rebounded and the Nasdaq 100 proxy held roughly flat.")
TL_CY = ("A maximum-severity Cisco Identity Services Engine authentication bypass already under active attack carries "
         "a federal remediation deadline of tomorrow, while researchers disclosed Plugin4Shell, a flaw that lets a "
         "plugin repository&rsquo;s owner swap the code four AI coding agents install even when it is pinned to a "
         "reviewed commit.")
TL_MMA = ("Joshua Van and Alexandre Pantoja both hit 125 pounds at Friday&rsquo;s official weigh-ins in Los Angeles "
          "and all 24 UFC 331 athletes made their limits, setting up Saturday night&rsquo;s flyweight title rematch "
          "at Crypto.com Arena.")


# ================================================================ INDEX
def build_index():
    css = base_css("#8fb3c8", "#e8c766", "#0a0a0b", "#141414", "#262626") + """
.big{display:grid;gap:15px}
@media(min-width:760px){.big{grid-template-columns:repeat(3,1fr)}}
.bc{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:19px 20px;
  display:flex;flex-direction:column;transition:.17s}
.bc:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.36)}
.bc .glyph{font-size:22px;line-height:1;margin-bottom:9px}
.bc .name{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:3px}
.bc .lbl{font-family:var(--mono);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--muted);margin-bottom:11px}
.bc p{font-size:14px;color:#cfcbc6;flex:1;margin:0 0 15px}
.bc a.go{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase}
.sec-c{border-top:3px solid #22d3a8}.sec-c .glyph,.sec-c .name,.sec-c a.go{color:#22d3a8}
.mk-c{border-top:3px solid #caa64a}.mk-c .glyph,.mk-c .name,.mk-c a.go{color:#e8c766}
.mk-c .name{font-family:Georgia,'Times New Roman',serif;font-size:15px;letter-spacing:.02em;text-transform:none}
.mm-c{border-top:3px solid #e84545}.mm-c .glyph,.mm-c .name,.mm-c a.go{color:#ff8a5c}
"""
    o = [head("Daily Briefings", css)]
    o.append(mast("Daily Briefings",
                  "Security, markets and mixed martial arts &mdash; refreshed every 30 minutes, 8 AM&ndash;6 PM ET"))
    o.append(FRESH)
    o.append(nav("index"))
    o.append('<div class="big">')
    o.append('<div class="bc sec-c"><div class="glyph">&#9960;</div>'
             '<div class="name">The Cyber Wire</div><div class="lbl">The Wire</div>'
             '<p>%s</p><a class="go" href="cyber-briefing.html">Read the briefing &rarr;</a></div>' % TL_CY)
    o.append('<div class="bc mk-c"><div class="glyph">&#9650;</div>'
             '<div class="name">The Closing Bell</div><div class="lbl">The Tape</div>'
             '<p>%s</p><a class="go" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>' % TL_WS)
    o.append('<div class="bc mm-c"><div class="glyph">&#8856;</div>'
             '<div class="name">The Octagon</div><div class="lbl">Tale of the Tape</div>'
             '<p>%s</p><a class="go" href="mma-briefing.html">Read the briefing &rarr;</a></div>' % TL_MMA)
    o.append('</div>')
    o.append('<div class="disc">Every figure on these pages is checked against a source fetched during the run that '
             'produced this edition. Point-in-time snapshots of earlier editions live in the '
             '<a href="archive.html">Archive</a>.</div>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ CYBER
def build_cyber():
    css = base_css("#22d3a8", "#36c6ff", "#07100e", "#0e1a17", "#1d2f2a") + """
.topstory{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:18px 20px;margin-bottom:14px}
.topstory h3{margin:0 0 8px;font-size:19px;line-height:1.3}
.topstory p{margin:0 0 9px;font-size:14.5px;color:#cfe3de}
.topstory p:last-child{margin-bottom:0}
"""
    o = [head("The Cyber Wire &mdash; Daily Briefing", css)]
    o.append(mast("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, vulnerabilities &amp; federal deadlines"))
    o.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % TL_CY)
    o.append(FRESH)
    o.append(nav("cyber"))

    # Threat banner
    o.append('<div class="banner"><span class="lvl">Threat Level: High</span>'
             '<span style="font-size:14px">A CVSS 10.0 Cisco ISE authentication bypass is being exploited in the wild '
             'and federal agencies were told to remediate it by <b>Saturday, September 19</b> &mdash; %s.</span></div>'
             % kevtxt(datetime.date(2026, 9, 19)))

    # By the numbers
    o.append('<div class="stats">'
             '<div class="stat"><div class="n">10.0</div><div class="l">CVSS of CVE-2026-76460 (Cisco ISE), rated by Cisco and exploited in the wild</div></div>'
             '<div class="stat"><div class="n">28</div><div class="l">Critical CVEs disclosed Sept 18, up 47% from 19 the prior day (CVE Brief)</div></div>'
             '<div class="stat"><div class="n">23.62M</div><div class="l">Gyazo user records exposed, alongside 490M image records (TechRadar)</div></div>'
             '<div class="stat"><div class="n">7.49M</div><div class="l">Records an attacker claims to have taken from CenterPoint Energy (Security Affairs)</div></div>'
             '</div>')

    o.append('<h2 class="sec">Top Story</h2>')
    o.append('<div class="topstory"><h3>Plugin4Shell: a repository owner can swap the plugin code four AI coding agents install &mdash; even when it is pinned</h3>'
             '<p>Security firm Air Security said on Thursday that a flaw in four widely used AI coding agents lets '
             'whoever controls a plugin&rsquo;s code repository substitute a malicious version for the one the agent '
             'was told to install, defeating the version pinning the marketplaces rely on. Marketplaces lock each '
             'plugin to a single reviewed snapshot by its commit hash; Air found the agents fetch that snapshot but '
             'never verify that the code they end up with matches it. On a code host that permits a branch named to '
             'look like a commit hash, the repository owner can point the pin somewhere else.</p>'
             '<p>Air said Anthropic has patched the flaw in <b>Claude Code 2.1.179</b> and OpenAI in <b>Codex '
             '0.146.0</b>, that <b>GitHub Copilot has no fix</b>, and that <b>Google will not patch the Gemini CLI</b>, '
             'which it is retiring. The Hacker News carried the disclosure on September 18.</p></div>')

    o.append('<h2 class="sec">Patch Priority</h2>')
    o.append('<div class="callout crit"><h3>Patch first: CVE-2026-76460 &mdash; Cisco Identity Services Engine</h3>'
             '<p style="margin:0;font-size:14.5px">An unauthenticated remote attacker can bypass authentication '
             'through an ISE API and, per reporting on the emergency fix, ultimately reach command execution as root. '
             'Cisco rates it <b>CVSS 3.1 10.0</b> (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) and released emergency updates '
             'for ISE and ISE Passive Identity Connector after confirming exploitation in the wild. CISA added it to '
             'the KEV catalog on <b>September 16</b> and urged remediation before <b>September 19, 2026</b> &mdash; '
             '<b>%s</b>. This is the same deadline carried in the KEV section below.</p></div>'
             % kevtxt(datetime.date(2026, 9, 19)))

    o.append('<h2 class="sec">Threat Actor Spotlight</h2>')
    o.append('<div class="cards"><div class="card">'
             '<div class="tags"><span class="t new">New</span><span class="t">Espionage</span><span class="t">South Asia</span></div>'
             '<h3>Transparent Tribe (APT36) &mdash; &ldquo;Operation RapidRust&rdquo;</h3>'
             '<p>Zscaler ThreatLabz attributes a fresh set of attacks on government and defence entities in India and '
             'Afghanistan to the Pakistan-aligned group also tracked as Earth Karkaddan, using four previously '
             'undocumented tools &mdash; RUSTYSHADE, RUSTYMOVE, PSNATCH and BASHNATCH. Sudeep Singh, senior manager of '
             'APT research at ThreatLabz, said the group &ldquo;has maintained a high operational tempo&rdquo; and '
             'updated its tradecraft. The finding lands about a month after Acronis&rsquo; Threat Research Unit tied '
             'the group to a campaign against Afghan telecom providers and South Asian critical infrastructure.</p>'
             '</div></div>')

    o.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
    o.append('<div class="cards">')
    o.append('<div class="card"><div class="tags"><span class="t hot">Utility</span><span class="t">Confirmed</span></div>'
             '<h3>CenterPoint Energy confirms customer data theft</h3>'
             '<p>The Texas utility confirmed customer data was stolen after an attacker leaked material attributed to '
             'it. The attacker claims <b>7.49 million records</b>, including names, phone numbers, service and billing '
             'addresses, account numbers, billing amounts and partial Social Security numbers. The record count is the '
             'attacker&rsquo;s claim, not a company figure.</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t">Consumer</span><span class="t">PII</span></div>'
             '<h3>Gyazo image-sharing breach exposes 23.62M user records</h3>'
             '<p>A vulnerability in the screenshot-sharing service exposed <b>23.62 million user records</b> and '
             '<b>490 million image records</b>, with personally identifiable information and metadata among the data, '
             'per reporting published September 17.</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t new">New</span><span class="t">Supply chain</span><span class="t">npm</span></div>'
             '<h3>WeaselBiscuit stealer ships in 13 npm packages</h3>'
             '<p>Researchers at OpenSourceMalware found a cluster of 13 npm packages delivering a previously '
             'undocumented JavaScript stealer that harvests Chrome extension storage. Researcher Paul McCarty '
             'described it as &ldquo;smaller, lighter, and stripped down&rdquo; than the DPRK-linked BeaverTail and '
             'OtterCookie families it overlaps with.</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t">Government</span><span class="t">Credential abuse</span></div>'
             '<h3>Florida DMV and Japan&rsquo;s Digital Agency</h3>'
             '<p>The Florida Department of Highway Safety and Motor Vehicles confirmed its DAVID driver database was '
             'breached using stolen police credentials; ShinyHunters disclosed 52GB of compressed data. Separately, '
             'Japan&rsquo;s Digital Agency found a breach that may have exposed around <b>246,000 record rows</b> of '
             'government-employee personal information.</p></div>')
    o.append('</div>')
    o.append('<p class="note">One <b>New</b> tag in this section this edition. A check across all 759 prior archived '
             'snapshots found CenterPoint in 8, Gyazo in 2, the Florida DMV database in 27 and ShinyHunters in 123 &mdash; '
             'so only WeaselBiscuit, which appears in none, is tagged.</p>')

    o.append('<h2 class="sec">Vulnerability Watch</h2>')
    o.append('<div class="panel"><table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr></thead><tbody>')
    o.append('<tr><td>CVE-2026-76460</td><td class="down">10.0</td><td>Cisco Identity Services Engine / ISE-PIC</td>'
             '<td>Authentication bypass via an ISE API. Cisco-rated; emergency fixes released after confirmed '
             'exploitation. In CISA KEV since Sept 16.</td></tr>')
    o.append('<tr><td>CVE-2026-85889</td><td class="down">10.0</td><td>Azure AI Foundry (Microsoft Foundry)</td>'
             '<td>Missing authentication for a critical function allows an unauthorised attacker to elevate privileges '
             'over a network. Patched by Microsoft; <b>no customer action required</b> and no evidence of exploitation. '
             'Credited to R&eacute;my Marot.</td></tr>')
    o.append('<tr><td>CVE-2026-91843</td><td class="down">9.8</td><td>Check Point Security Management &amp; Log Servers</td>'
             '<td>Pre-authentication stack overflow in the login process; unauthenticated code execution as root. '
             'Check Point&rsquo;s own rating; fixed via LivePatch, with the vulnerable path reachable only through the '
             'Trusted Clients setting. No indication of exploitation.</td></tr>')
    o.append('<tr><td>CVE-2026-81642</td><td class="mut">Critical (see note)</td><td>Unbound DNS resolver, all releases before 1.26.1</td>'
             '<td>Heap overflow in the DNSSEC validator; an attacker controlling a malicious zone can reach remote '
             'code execution. NLnet Labs rates it Critical and its scoring lists CVSS 4.0 (9.1). Fixed in 1.26.1, '
             'alongside eight other flaws.</td></tr>')
    o.append('<tr><td>CVE-2026-77179</td><td class="mut">Critical (no score published)</td><td>Docker Sandboxes on macOS, 0.28.0 up to 0.42.0</td>'
             '<td>Guest code can escape the shared project directory and read or modify files anywhere the host account '
             'can reach. Fixed in 0.42.0 on September 7; CISA&rsquo;s assessment on the record lists exploitation as '
             'none.</td></tr>')
    o.append('</tbody></table></div>')
    o.append('<p class="note">CVSS figures are the vendor&rsquo;s or maintainer&rsquo;s own, not a blog&rsquo;s. Where '
             'no numeric score was published by the vendor, the severity word is given instead of a number.</p>')

    o.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
    o.append('<div class="panel"><ul class="bul">')
    o.append('<li><b>Sept 16 &mdash; two added:</b> CVE-2026-76460 (Cisco Identity Services Engine, incorrect use of '
             'privileged APIs) and CVE-2026-87886 (Acronis Backup, incorrect default permissions). CISA urged '
             'remediation of the Cisco flaw before <b>September 19, 2026</b> &mdash; <span class="down"><b>%s</b></span>. '
             'No separate due date for the Acronis entry was confirmed this run, so none is asserted.</li>'
             % kevtxt(datetime.date(2026, 9, 19)))
    o.append('<li><b>Sept 14 &mdash; one added.</b> <b>Sept 9 &mdash; four added.</b> <b>Sept 2 &mdash; seven added.</b> '
             'CISA&rsquo;s alert pages for these dates were confirmed to exist this run; individual CVE identifiers and '
             'due dates for them were not re-fetched, so none are listed here.</li>')
    o.append('<li><b>Which directive governs:</b> remediation dates for KEV entries now run under <b>BOD 26-04</b>, '
             '&ldquo;Prioritizing Security Updates Based on Risk,&rdquo; which sets the due dates for Federal Civilian '
             'Executive Branch agencies. It supersedes the flat three-week window of <b>BOD 22-01</b> &mdash; which is '
             'why a three-day deadline like the Cisco one is possible and is not a transcription error.</li>')
    o.append('</ul></div>')

    o.append(sources([
        ("The Hacker News &mdash; front page, Sept 18 2026 (Plugin4Shell, Transparent Tribe, WeaselBiscuit, Azure AI Foundry, Check Point, Unbound, Docker Sandboxes)", "https://thehackernews.com/"),
        ("The Hacker News &mdash; Plugin4Shell", "https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html"),
        ("The Hacker News &mdash; Microsoft patches CVSS 10.0 Azure AI Foundry flaw", "https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html"),
        ("The Hacker News &mdash; Check Point management flaw", "https://thehackernews.com/2026/09/critical-check-point-management-server.html"),
        ("The Hacker News &mdash; Unbound DNSSEC validator flaw", "https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html"),
        ("The Hacker News &mdash; Docker Sandboxes escape", "https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html"),
        ("CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (Sept 16 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
        ("CISA &mdash; Known Exploited Vulnerabilities Catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
        ("Qualys ThreatPROTECT &mdash; CISA warns of Cisco ISE authentication bypass (CVE-2026-76460)", "https://threatprotect.qualys.com/2026/09/17/cisa-warns-of-cisco-identity-services-engine-authentication-bypass-vulnerability-cve-2026-76460/"),
        ("BleepingComputer &mdash; Cisco warns of max severity ISE zero-day exploited in attacks", "https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/"),
        ("CVE Brief &mdash; September 18, 2026", "https://cvebrief.com/archive/2026/09/18/"),
        ("Security Affairs &mdash; CenterPoint Energy confirms data breach", "https://securityaffairs.com/199170/data-breach/texas-utility-centerpoint-energy-confirms-data-breach-after-hacker-claims-7-49m-records-stolen.html"),
        ("TechRadar &mdash; Gyazo breach exposes 23.62 million user records", "https://www.techradar.com/pro/security/gyazo-breach-exposes-23-62-million-user-records-and-490-million-image-records-pii-and-metadata-exposed-in-huge-attack"),
        ("Privacy Guides &mdash; Data Breach Roundup (Sep 11&ndash;17, 2026)", "https://www.privacyguides.org/news/2026/09/18/data-breach-roundup-sep-11-17-2026/"),
    ]))
    o.append(DISC_CY)
    o.append('</footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ WALL STREET
def build_ws():
    css = base_css("#caa64a", "#e8c766", "#0b0a07", "#16140f", "#2a261b") + """
.masthead h1,.topstory h3,.lead h3{font-family:Georgia,'Times New Roman',serif;letter-spacing:-.2px}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);
  display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:6px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 8px}
.lead{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:18px 20px;margin-bottom:14px}
.lead h3{margin:0 0 9px;font-size:21px;line-height:1.28}
.lead p{margin:0 0 9px;font-size:14.5px;color:#ded8c8}
.lead p:last-child{margin-bottom:0}
"""
    o = [head("The Closing Bell &mdash; Daily Briefing", css)]
    o.append(mast("The Closing Bell", "Your daily markets briefing &mdash; indices, movers, rates &amp; the week ahead"))
    o.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % TL_WS)
    o.append(FRESH)
    o.append(nav("ws"))

    # BLOCK A
    o.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
             '<script src="%s" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
             '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
             '{"proName":"NASDAQ:XENE","title":"Xenon"},{"proName":"NASDAQ:COIN","title":"Coinbase"},'
             '{"proName":"NASDAQ:HOOD","title":"Robinhood"},{"proName":"NYSE:ORCL","title":"Oracle"},'
             '{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"TVC:USOIL","title":"WTI Crude"},'
             '{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,'
             '"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>'
             % (TV % 'ticker-tape'))

    # BLOCK B
    o.append('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>')
    o.append('<div class="tickers">')
    for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"):
        o.append('<div class="ticker"><script src="%s" async>{"symbol":"%s","width":"100%%",'
                 '"colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'
                 % (TV % 'single-quote', sym))
    o.append('</div>')
    o.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest '
             'edition; official closes are in the Weekly Scorecard.</div>')

    o.append('<h2 class="sec">The Lead</h2>')
    o.append('<div class="lead"><h3>Yields back above 5% pull stocks off Thursday&rsquo;s bounce (as of ~2:37 PM ET)</h3>'
             '<p>Trading Economics&rsquo; live board at roughly 2:37 PM ET had its <b>S&amp;P 500 proxy at 7,621.99, '
             '&minus;15.77 (&minus;0.21%)</b>, its <b>Dow proxy at 51,560.61, &minus;217.43 (&minus;0.42%)</b>, its '
             '<b>Nasdaq 100 proxy at 29,460.55, +13.57 (+0.05%)</b> and its <b>Russell 2000 proxy at 2,850.70, '
             '&minus;23.93 (&minus;0.83%)</b>. These are contract-for-difference references, not official exchange '
             'values &mdash; Trading Economics says so itself &mdash; which is why the Weekly Scorecard below carries '
             'index-level closes instead.</p>'
             '<p>Trading Economics&rsquo; own Sept 18 wrap, headlined <i>US Stocks Pare Gains</i>, says stocks swung '
             'lower as Treasury yields rebounded, with the S&amp;P 500 and Dow dropping 0.3% and the Nasdaq 100 '
             'inching below the flatline &mdash; prose written at some earlier point in the session than the table '
             'read above, which is why the two do not match to the decimal. The 10-year note rebounded above the 5% threshold as uncertainty over Middle '
             'Eastern oil supply drove fuel and natural gas prices up. Credit-sensitive names fell, with banks and '
             'asset managers firmly in the red; AI hyperscalers were mostly lower amid what the wrap calls a debt-issuance '
             'spree for capital expenditure, with Oracle, Microsoft and Palantir dropping between 3% and 1%. Chip '
             'producers rebounded.</p>'
             '<p>Bloomberg&rsquo;s Sept 18 live coverage adds that traders also faced the expiry of a large pile of '
             'options, and that yields climbed on speculation elevated energy costs could fuel inflation and prompt '
             'further Fed hikes &mdash; keeping a lid on equities, with over 350 S&amp;P 500 members retreating.</p>'
             '<p class="note" style="margin-top:9px">Divergence printed rather than smoothed: Trading Economics&rsquo; '
             'own page description says the S&amp;P proxy &ldquo;fell to 7624 points&hellip; losing 0.18%&rdquo; while '
             'its live table read 7,621.99 / &minus;0.21% at fetch time. The table figure is used.</p></div>')

    o.append('<h2 class="sec">Movers &amp; Drivers</h2>')
    o.append('<div class="cards">')
    o.append('<div class="card"><div class="tags"><span class="t new">New</span><span class="t hot">Biotech</span></div>'
             '<h3 class="down">Xenon Pharmaceuticals &minus;22.24%</h3>'
             '<p>The session&rsquo;s largest sourced move. Xenon voluntarily paused new patient enrolment in ongoing '
             'Phase 3 trials of azetukalner as a treatment for focal seizures in epilepsy.</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t gold">Crypto brokers</span><span class="t">Regulation</span></div>'
             '<h3 class="up">Coinbase and Robinhood higher on the SEC&rsquo;s &ldquo;Innovation Exemption&rdquo;</h3>'
             '<p>The SEC issued a five-year conditional exemption on September 17 freeing eligible tokenised-securities '
             'venues from the legal definition of an exchange, and giving automated-market-maker liquidity providers '
             'relief from dealer registration. Two sourced reads, neither reconciled: a Sept 18 pre-market summary had '
             '<b>HOOD +3.71%</b> and <b>COIN +3.53%</b>; a separate Sept 18 market summary put <b>COIN +6.55%</b> and '
             '<b>HOOD +5.94%</b>. Robinhood CEO Vlad Tenev called it &ldquo;a good day for US innovation.&rdquo;</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t">Mega-cap</span><span class="t">AI capex</span></div>'
             '<h3 class="down">Oracle &minus;3.31%</h3>'
             '<p>The weakest of the large caps on Trading Economics&rsquo; live share table at fetch time, within the '
             '&ldquo;3% to 1%&rdquo; band its wrap describes for Oracle, Microsoft and Palantir. Alongside it: Meta '
             '&minus;1.64%, SpaceX &minus;1.94%, Tesla &minus;1.02%, Goldman Sachs &minus;0.90%, Microsoft &minus;0.82%. '
             'On the other side, Amazon +0.74%, Caterpillar +0.30% and Nvidia +0.17%.</p></div>')
    o.append('</div>')
    o.append('<p class="note">One <b>New</b> tag here this edition: Xenon appears in none of the 759 prior archived '
             'snapshots, while Coinbase (3), Robinhood (7) and Oracle (163) all do.</p>')

    # BLOCK E
    o.append('<h2 class="sec">Chart of the Day &mdash; Xenon Pharmaceuticals (NASDAQ:XENE)</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>{"symbol":"NASDAQ:XENE",'
             '"width":"100%%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark",'
             '"isTransparent":true,"autosize":false}</script></div>' % (TV % 'mini-symbol-overview'))

    # BLOCK D
    o.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>{"dataSource":"SPX500",'
             '"blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en",'
             '"colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
             '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%%","height":420}</script></div>'
             % (TV % 'stock-heatmap'))
    o.append('<p class="note">Sourced read on the day&rsquo;s split: technology did the heavy lifting while other '
             'sectors sagged and chipmakers gained, with the semiconductor group up close to 3% on one Sept 18 summary; '
             'credit-sensitive sectors &mdash; banks and asset managers &mdash; traded firmly in the red. Breadth was '
             'negative, with over 350 S&amp;P 500 firms retreating. No VIX figure is published: every reading reaching '
             'this desk remained internally inconsistent.</p>')

    # BLOCK F
    o.append('<h2 class="sec">The Calendar &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>{"colorTheme":"dark",'
             '"isTransparent":true,"width":"100%%","height":420,"locale":"en","importanceFilter":"0,1",'
             '"countryFilter":"us"}</script></div>' % (TV % 'events'))

    # BLOCK C
    o.append('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>{"feedMode":"market",'
             '"market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular",'
             '"width":"100%%","height":420,"locale":"en"}</script></div>' % (TV % 'timeline'))

    o.append('<h2 class="sec">Weekly Scorecard</h2>')
    o.append('<div class="panel"><table><thead><tr><th>Session</th><th>S&amp;P 500</th><th>Dow</th><th>Nasdaq</th><th>Note</th></tr></thead><tbody>')
    o.append('<tr><td>Mon Sept 14</td><td class="mut">Not verified</td><td class="mut">Not verified</td>'
             '<td class="mut">Not verified</td><td class="mut">No close for this session was re-fetched this run.</td></tr>')
    o.append('<tr><td>Tue Sept 15</td><td class="mut">Not verified</td><td class="mut">Not verified</td>'
             '<td class="mut">Not verified</td><td class="mut">No close for this session was re-fetched this run.</td></tr>')
    o.append('<tr><td>Wed Sept 16</td><td class="down">7,551.81 (&minus;0.45%)</td>'
             '<td class="down">51,461.90 (&minus;631.21, &minus;1.21%)</td>'
             '<td class="down">25,978.42 (&minus;0.01%, Composite)</td>'
             '<td>Fed day. Points, percent and level reconcile on the Dow (51,461.90 + 631.21 = 52,093.11; '
             '631.21/52,093.11 = 1.21%).</td></tr>')
    o.append('<tr><td>Thu Sept 17</td><td class="up">+1.12%</td><td class="up">51,779.85 (+0.62%)</td>'
             '<td class="up">29,446.98 (+1.73%, Nasdaq 100)</td>'
             '<td>The S&amp;P <b>level is withheld</b>: the source&rsquo;s own 7,637.72 against Wednesday&rsquo;s '
             '7,551.81 reconciles to +1.14%, not the +1.12% it states, so only the percentage is published. The Dow '
             'reconciles exactly (51,779.85 / 51,461.90 = +0.62%).</td></tr>')
    o.append('<tr><td>Fri Sept 18</td><td class="mut">Session in progress</td><td class="mut">Session in progress</td>'
             '<td class="mut">Session in progress</td>'
             '<td>No official close exists yet. Intraday proxies are in The Lead, with their as-of time.</td></tr>')
    o.append('</tbody></table></div>')

    o.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
    o.append('<div class="panel"><table><thead><tr><th>Instrument</th><th>Level</th><th>Change</th><th>Note</th></tr></thead><tbody>')
    o.append('<tr><td>US 10-year Treasury</td><td>5.0020%</td><td class="down">+0.065 pp (~6.5 bp)</td>'
             '<td>Back above the 5% threshold; reporting this week placed the 10-year at its highest since July 2007. '
             'The change is in yield points, not a percent change in the yield.</td></tr>')
    o.append('<tr><td>US 2-year Treasury</td><td class="mut">4.73%</td><td class="mut">&mdash;</td>'
             '<td class="mut">From a mid-September Trading Economics summary; <b>not re-fetched this run</b>, so no '
             'Friday change is asserted.</td></tr>')
    o.append('<tr><td>US 30-year Treasury</td><td class="mut">5.34%</td><td class="mut">&mdash;</td>'
             '<td class="mut">Same caveat as the 2-year.</td></tr>')
    o.append('<tr><td>Fed funds target</td><td>3.75%&ndash;4.00%</td><td class="down">+25 bp</td>'
             '<td>Raised unanimously on Wednesday &mdash; the first hike in three years. The dot plot showed the median '
             'official seeing at least one more hike in 2026.</td></tr>')
    o.append('<tr><td>WTI crude</td><td>$100.834</td><td class="down">&minus;1.06%</td><td>Swinging amid Saudi supply concerns, per Trading Economics&rsquo; commodity stream.</td></tr>')
    o.append('<tr><td>Brent crude</td><td>$103.564</td><td class="down">&minus;1.20%</td><td>Lower on Friday.</td></tr>')
    o.append('<tr><td>Natural gas</td><td>$2.9193</td><td class="up">+0.63%</td><td>US natural gas stocks rose less than expected.</td></tr>')
    o.append('<tr><td>Gold</td><td>$4,386.21</td><td class="up">+1.03%</td><td>&mdash;</td></tr>')
    o.append('<tr><td>Silver</td><td>$66.668</td><td class="up">+2.26%</td><td>&mdash;</td></tr>')
    o.append('<tr><td>Bitcoin</td><td>$80,732</td><td class="up">+5.65%</td><td>&mdash;</td></tr>')
    o.append('</tbody></table></div>')
    o.append('<p class="note">Colouring follows the sign of the percentage move, not the unsigned figure in Trading '
             'Economics&rsquo; raw change column &mdash; so WTI and Brent are red. Each percentage was reconciled '
             'against its own level and change before publishing (WTI 1.08/101.914 = 1.06%; Brent 1.26/104.824 = 1.20%; '
             'gold 44.82/4,341.39 = 1.03%; Bitcoin 4,320/76,412 = 5.65%).</p>')

    o.append('<h2 class="sec">On the Radar</h2>')
    o.append('<div class="panel"><ul class="bul">')
    o.append('<li><b>More hikes, on the committee&rsquo;s own arithmetic.</b> FOMC member projections point to one or '
             'two additional rate increases by next year, alongside upward revisions to inflation forecasts and '
             'downward revisions to unemployment. Fed Chair Kevin Warsh noted core US inflation rose more than '
             'anticipated in August, driven by surging energy prices.</li>')
    o.append('<li><b>Today&rsquo;s options expiry.</b> Bloomberg&rsquo;s Sept 18 coverage flags a large pile of expiring '
             'options as a source of sudden price swings into the close &mdash; a mechanical risk, not a directional call.</li>')
    o.append('<li><b>The data that landed today.</b> US manufacturing output unexpectedly fell and factory output '
             'stalled against forecasts; capacity utilisation held at a one-year high; pending home sales missed; the '
             '30-year mortgage rate rose further; and the dollar gained more than 1% on the week.</li>')
    o.append('<li><b>Next week.</b> Trading Economics&rsquo; calendar preview for the week beginning <b>Sept 21</b> is '
             'live in the Calendar panel above; specific releases are not listed here because none were individually '
             'verified this run.</li>')
    o.append('</ul></div>')

    o.append(sources([
        ("Trading Economics &mdash; United States Stock Market Index (live board, news stream, commodities, bonds and shares tables; fetched ~2:37 PM ET Sept 18 2026)", "https://tradingeconomics.com/united-states/stock-market"),
        ("Trading Economics &mdash; US Stocks Pare Gains (Sept 18 2026)", "https://tradingeconomics.com/united-states/stock-market/news/585064"),
        ("Bloomberg &mdash; Stock Market Today: Dow, S&P Live Updates for September 18", "https://www.bloomberg.com/news/articles/2026-09-17/stock-market-today-dow-s-p-live-updates"),
        ("TheStreet &mdash; Stock Market Today (Sept. 18, 2026)", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-18-2026"),
        ("Yahoo Finance &mdash; Dow, S&P 500, Nasdaq slip as bond yields rise (Sept 18 2026)", "https://finance.yahoo.com/markets/live/stock-market-today-friday-september-18-dow-sp-500-nasdaq-080504071.html"),
        ("CNBC &mdash; Dow drops 600 points as Fed rate hike and Warsh's inflation talk unnerve investors (Sept 16 2026)", "https://www.cnbc.com/2026/09/15/stock-market-today-live-updates.html"),
        ("TheStreet &mdash; Stock Market Today (Sept. 16, 2026): Dow, S&P 500 plummet after Fed hikes", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-16-2026"),
        ("TheStreet &mdash; Stock Market Today (Sept. 17, 2026): Nasdaq, S&P 500 surge on post-Fed rate hike buying", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-17-2026"),
        ("CNBC &mdash; SEC clears path for tokenized stocks (Sept 17 2026)", "https://www.cnbc.com/2026/09/17/sec-clears-path-for-tokenized-stocks-bringing-24/7-trading-closer.html"),
        ("Benzinga &mdash; SEC gives tokenized stocks a five-year onchain runway; Tenev comment", "https://www.benzinga.com/crypto/cryptocurrency/26/09/61860709/sec-gives-tokenized-stocks-a-five-year-onchain-runway-robinhood-ceo-vlad-tenev-says-its-a-good-day-for-us-innovation"),
        ("TradingKey &mdash; Crypto brokerage stocks gain pre-market on the Innovation Exemption (Sept 18 2026)", "https://www.tradingkey.com/analysis/stocks/us-stocks/262175029-sec-unveils-5-year-innovation-exemption-crypto-broker-stocks-rally-tradingkey"),
        ("Trading Economics &mdash; US 10-Year Treasury Note Yield", "https://tradingeconomics.com/united-states/government-bond-yield"),
    ]))
    o.append(DISC_WS)
    o.append('</footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ MMA
def build_mma():
    css = base_css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020") + """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:10px;padding:12px 16px;margin-bottom:16px;display:flex;flex-wrap:wrap;
  align-items:baseline;gap:10px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent2)}
.cdn .v{font-family:var(--mono);font-size:17px;color:var(--accent2)}
.cdn .w{font-size:14px;color:#e3d5d2}
.topstory{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:18px 20px;margin-bottom:14px}
.topstory h3{margin:0 0 8px;font-size:19px;line-height:1.3}
.topstory p{margin:0 0 9px;font-size:14.5px;color:#e3d5d2}
.topstory p:last-child{margin-bottom:0}
.when{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--warn);margin-bottom:7px}
.odds{font-family:var(--mono);font-size:11.5px;color:var(--muted);margin-top:8px;display:block}
"""
    o = [head("The Octagon &mdash; Daily Briefing", css)]
    o.append(mast("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    o.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % TL_MMA)
    o.append(FRESH)
    o.append(nav("mma"))

    o.append('<div class="cdn"><span class="k">Next Card</span><span class="v" id="ufccdn">&nbsp;</span>'
             '<span class="w">UFC 331: Van vs. Pantoja 2 &mdash; Sat Sept 19, Crypto.com Arena, Los Angeles. '
             'Early prelims 5:30 PM ET &middot; prelims 7 PM ET &middot; main card 9 PM ET, Paramount+.</span></div>')

    o.append('<h2 class="sec">Top Story</h2>')
    o.append('<div class="topstory"><h3>Everybody made weight: Van and Pantoja both hit 125 for Saturday&rsquo;s rematch</h3>'
             '<p>At Friday&rsquo;s official weigh-ins in Los Angeles, champion <b>Joshua Van</b> and challenger '
             '<b>Alexandre Pantoja</b> both recorded 125 pounds for the flyweight title rematch, and all <b>24 '
             'scheduled athletes</b> on the card came in within their divisional limits &mdash; no misses, no catchweights.</p>'
             '<p>Other headline weights: <b>Arman Tsarukyan 156</b> and <b>Mauricio Ruffy 155</b> for the lightweight '
             'co-main; <b>Patricio Pitbull 145.5</b> vs <b>Dooho Choi 146</b>; <b>Gable Steveson 240</b> vs <b>Sean '
             'Sharaf 241</b>; <b>Alonzo Menifield 205.5</b> vs <b>Iwo Baraniewski 206</b>; <b>Marlon Vera 136</b> vs '
             '<b>Charles Jourdain 135</b>; <b>Tai Tuivasa 264.5</b> vs <b>Robelis Despaigne 263</b>.</p>'
             '<p>Van won the belt from Pantoja roughly nine months ago on an injury stoppage, which is the premise the '
             'rematch is built on. A report circulating yesterday that Van had withdrawn from the card traces to a '
             'single automated aggregator and is contradicted by today&rsquo;s weigh-in coverage, in which he stood on '
             'the scale.</p></div>')

    o.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
    o.append('<div class="cards">')
    o.append('<div class="card"><div class="when">Sat Sept 19 &middot; Crypto.com Arena, Los Angeles</div>'
             '<h3>UFC 331: Van vs. Pantoja 2</h3>'
             '<p>Flyweight title rematch, with Arman Tsarukyan vs. Mauricio Ruffy in the lightweight co-main. '
             'Main card 9 PM ET on Paramount+.</p>'
             '<span class="odds">Odds: Van &minus;130 / Pantoja +110 (Covers, giving Van a 56% implied chance); '
             'CBS Sports&rsquo; DraftKings read had Van &minus;135. Co-main: Tsarukyan &minus;305 / Ruffy +240.</span></div>')
    o.append('<div class="card"><div class="when">Sat Oct 3 &middot; Delta Center, Salt Lake City</div>'
             '<h3>UFC 332: Silva vs. Wang</h3>'
             '<p>Nat&aacute;lia Silva and Wang Cong contest the <b>vacant</b> women&rsquo;s flyweight title, vacated by '
             'Valentina Shevchenko while she is sidelined by injury.</p>'
             '<span class="odds">No odds for this headliner were stated in any source fetched this run, so none are printed.</span></div>')
    o.append('<div class="card"><div class="when">Sat Oct 24 &middot; Etihad Arena, Abu Dhabi</div>'
             '<h3>UFC 333: Volkanovski vs. Evloev</h3>'
             '<p>Alexander Volkanovski defends the featherweight title against Movsar Evloev, with Petr Yan vs. Merab '
             'Dvalishvili 3 for the bantamweight belt in the co-main.</p>'
             '<span class="odds">No odds for this headliner were stated in any source fetched this run, so none are printed.</span></div>')
    o.append('</div>')
    o.append('<p class="note">No <b>New</b> tags anywhere on this page this edition &mdash; every fighter, event and '
             'venue named above already appears in the archived snapshots.</p>')

    o.append('<h2 class="sec">Last Event &mdash; Noche UFC: Silva vs. Delgado</h2>')
    o.append('<p class="note" style="margin:0 0 11px">Saturday, September 12, Desert Diamond Arena, Glendale, Arizona. '
             'Main-card results below are taken from UFC.com&rsquo;s own results page.</p>')
    o.append('<div class="panel"><table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr></thead><tbody>')
    rows = [
        ("Jean Silva", "def. Jose Miguel Delgado (main event, featherweight)",
         "Submission (rear-naked choke), R3 at 2:57"),
        ("Brandon Moreno", "def. Joseph Morales (co-main)", "Split decision"),
        ("Tommy McMillen", "def. Marwan Rahiki (featherweight)", "Unanimous decision (29-28, 29-28, 29-27)"),
        ("Alexa Grasso", "def. Manon Fiorot (flyweight)", "Unanimous decision (29-28, 29-28, 29-28)"),
        ("Curtis Blaydes", "def. Waldo Cortes Acosta (heavyweight)", "Unanimous decision (29-28, 29-28, 29-28)"),
        ("David Martinez", "def. Dan Ige", "Unanimous decision (30-27, 30-27, 29-28)"),
    ]
    for w, b, m in rows:
        o.append('<tr><td class="up"><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (w, b, m))
    o.append('</tbody></table></div>')
    o.append('<div class="callout"><h3>Performance Bonuses &mdash; UFC.com</h3>'
             '<p style="margin:0;font-size:14.5px"><b>Performance of the Night: Jean Silva</b>, who threw nothing in '
             'the first round before dropping Delgado and taking his back. <b>Performance of the Night: Sean King '
             'III</b> &mdash; UFC.com&rsquo;s own headline reads &ldquo;Sean King III Lands 0:36 KO In UFC Debut,&rdquo; '
             'and its copy says that 36 seconds in, King caught Jessie Rosas on a takedown attempt, lifted him and '
             'slammed him for an instant knockout, moving to 7-0. <b>Fight of the Night: Tommy McMillen vs. Marwan '
             'Rahiki</b>, a 15-minute back-and-forth McMillen took on the cards to go 12-0.</p></div>')
    o.append('<p class="note">Two corrections to this site&rsquo;s earlier editions, both resolved against UFC.com this '
             'run: Brandon Moreno&rsquo;s opponent and method are now confirmed as <b>Joseph Morales, split decision</b> '
             '(previously published as unverified), and <b>McMillen is confirmed the winner</b> over Rahiki (the result '
             'cell previously read &ldquo;no winner asserted&rdquo;). The King finish time is <b>0:36</b>, per UFC.com &mdash; '
             'a 33-second figure circulating in secondary summaries is not the official one.</p>')

    o.append('<h2 class="sec">Prospect Watch</h2>')
    o.append('<div class="cards">')
    o.append('<div class="card"><div class="tags"><span class="t pro">Prospect</span><span class="t">Featherweight</span></div>'
             '<h3>Tommy McMillen &mdash; 12-0</h3>'
             '<p>Took Fight of the Night in a survive-and-respond win over Marwan Rahiki, having been dropped and put '
             'on the brink in the second. UFC.com calls the DWCS Class of &rsquo;25 graduate one of the most '
             'entertaining all-action talents on the roster; he called for a fourth fight this year in Las Vegas.</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t pro">Prospect</span><span class="t">Debut</span></div>'
             '<h3>Sean King III &mdash; 7-0</h3>'
             '<p>Won Performance of the Night on debut with a 0:36 slam knockout of Jessie Rosas, catching him on a '
             'takedown attempt and putting him out on impact.</p></div>')
    o.append('<div class="card"><div class="tags"><span class="t pro">Prospect</span><span class="t">4-0 in the UFC</span></div>'
             '<h3>David Martinez &mdash; 11 straight</h3>'
             '<p>Swept the cards against Dan Ige to move to 4-0 inside the Octagon and extend his overall winning '
             'streak to 11, chopping the veteran&rsquo;s lead leg and out-landing him throughout.</p></div>')
    o.append('</div>')

    o.append('<h2 class="sec">Around the Sport</h2>')
    o.append('<div class="panel"><ul class="bul">')
    o.append('<li><b>Michael &ldquo;Venom&rdquo; Page has been released.</b> A leaked email reported by Bloody Elbow '
             'on September 7 indicated the UFC opted not to re-sign him after a decision win over Nursulton Ruziboev '
             'at UFC Paris &mdash; the last fight on his contract. He went 5-1 across six UFC appearances without a '
             'finish. He has since said he has offers from every other promotion, with Rizin among the options that '
             'interest him.</li>')
    o.append('<li><b>Curtis Blaydes signed a new eight-fight deal</b>, with the first bout on it coming at Noche UFC '
             'against Waldo Cortes Acosta &mdash; which he won on the cards.</li>')
    o.append('<li><b>Alexa Grasso is the clubhouse leader at 125.</b> Her unanimous-decision win over Manon Fiorot was '
             'a second straight victory and, in UFC.com&rsquo;s framing, sets her up in the chase for the next title '
             'shot &mdash; in a division whose belt is currently vacant.</li>')
    o.append('<li><b>Also on the schedule:</b> Dana White&rsquo;s Contender Series season 10 held official weigh-ins, '
             'and UFC.com published updates to the UFC Fight Night: Bonfim vs. Brown card.</li>')
    o.append('</ul></div>')

    o.append('<h2 class="sec">Rankings &amp; Business</h2>')
    o.append('<div class="panel">'
             '<p style="margin:0 0 10px"><b>Rankings movement.</b> Nothing this run traced to an official UFC rankings '
             'update, so no positions are asserted. What the results support: Blaydes is described by UFC.com as likely '
             'to re-claim a place in the heavyweight top five, and Grasso as the leading contender at flyweight. Jean '
             'Silva, now 7-1 in the Octagon with six finishes, made a case for a future title shot.</p>'
             '<p style="margin:0"><b>Business &amp; broadcast.</b> Paramount is in the first year of a <b>seven-year, '
             '$7.7 billion</b> media-rights deal with the UFC, owned by TKO Group. Since the start of the year, '
             '<b>16 million subscriber households</b> have watched more than <b>180 million hours</b> of UFC '
             'programming on Paramount+. Earlier benchmarks: UFC 324 averaged <b>4.96 million</b> for the main card '
             'with a <b>7.18 million</b> global household average; UFC Freedom 250 delivered <b>34 million total '
             'global viewers</b> per TKO&rsquo;s own release, with Variety reporting an <b>8.2 million</b> average. No '
             'gate figure and no viewership number for the September 12 card is published here &mdash; none was stated '
             'by an attributable source this run.</p></div>')

    o.append('<h2 class="sec">Champions Board</h2>')
    o.append('<div class="panel"><table><thead><tr><th>Division</th><th>Champion</th><th>Since / note</th></tr></thead><tbody>')
    champs = [
        ("Heavyweight", "VACANT", "Tom Aspinall vacated on Sept 14, 2026 over unresolved eye injuries; he is not retiring. <b>Interim: Ciryl Gane</b> (KO2 Pereira, Freedom 250, Jun 14 2026)."),
        ("Light Heavyweight", "Carlos Ulberg", "KO1 Ji&rcaron;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, Apr 11 2026."),
        ("Middleweight", "Sean Strickland", "Split decision over Khamzat Chimaev, UFC 328, May 9 2026. Two-time champion."),
        ("Welterweight", "Islam Makhachev", "UD Jack Della Maddalena, UFC 322, Nov 15 2025. One defence: UD Ian Machado Garry, UFC 330, Aug 15 2026."),
        ("Lightweight", "Justin Gaethje", "TKO4 Ilia Topuria, Freedom 250, Jun 14 2026."),
        ("Featherweight", "Alexander Volkanovski", "UD Diego Lopes, UFC 314, Apr 12 2025; defended UD Lopes, UFC 325, Jan 31 2026. Defends vs Movsar Evloev at UFC 333."),
        ("Bantamweight", "Petr Yan", "UD Merab Dvalishvili, UFC 323, Dec 6 2025. Faces Dvalishvili a third time at UFC 333."),
        ("Flyweight", "Joshua Van", "TKO1 Alexandre Pantoja, UFC 323, Dec 6 2025; defended TKO5 Tatsuro Taira, UFC 328, May 9 2026. Defends vs Pantoja tomorrow."),
        ("Women's Flyweight", "VACANT", "Valentina Shevchenko vacated while sidelined by injury. Nat&aacute;lia Silva vs Wang Cong contest it at UFC 332, Oct 3."),
        ("Women's Bantamweight", "Kayla Harrison", "Sub2 Julianna Pe&ntilde;a, UFC 316, Jun 7 2025. <b>Zero defences</b> &mdash; the Amanda Nunes bout has been postponed."),
        ("Women's Strawweight", "Mackenzie Dern", "UD Virna Jandiroba, UFC 321, Oct 25 2025. One defence: UD Gillian Robertson, UFC 330, Aug 15 2026."),
    ]
    for d, c, n in champs:
        cls = ' class="mut"' if c == "VACANT" else ""
        o.append('<tr><td>%s</td><td%s><b>%s</b></td><td>%s</td></tr>' % (d, cls, c, n))
    o.append('</tbody></table></div>')
    o.append('<div class="callout crit"><h3>Refused this run: ESPN&rsquo;s champions page</h3>'
             '<p style="margin:0;font-size:14.5px">ESPN&rsquo;s &ldquo;Current and all-time UFC champions&rdquo; page '
             'returned <b>no usable body text on direct fetch</b>, as it has on several recent runs. The search-level '
             'rendering available this run <b>seats Carlos Ulberg at heavyweight</b> &mdash; a division that has been '
             '<b>vacant</b> since Tom Aspinall stepped down on September 14, and not Ulberg&rsquo;s division, which is '
             'light heavyweight. That is the same division mis-assignment logged yesterday, and it is <b>refused</b>. '
             'Its other rows &mdash; Strickland at middleweight, Makhachev at welterweight with one defence, Gaethje at '
             'lightweight, Volkanovski at featherweight, Yan at bantamweight &mdash; agree with the board above. Every '
             'belt here is re-derived from the most recent title-changing card rather than copied from any single list.</p></div>')

    o.append(sources([
        ("UFC.com &mdash; Main Card Results, Noche UFC: Silva vs Delgado", "https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado"),
        ("UFC.com &mdash; Bonus Coverage, Noche UFC", "https://www.ufc.com/news/bonus-coverage-noche-ufc-glendale-2026"),
        ("UFC.com &mdash; Noche UFC official scorecards", "https://www.ufc.com/news/noche-ufc-official-scorecards-silva-vs-delgado"),
        ("Yahoo Sports &mdash; UFC 331 weigh-in results (Sept 18 2026)", "https://sports.yahoo.com/articles/ufc-331-weigh-results-joshua-173601093.html"),
        ("MiddleEasy &mdash; UFC 331 weigh-in results: Van and Pantoja make 125 pounds", "https://middleeasy.com/mma-news/ufc-331-weigh-in-results-joshua-van-alexandre-pantoja-125"),
        ("Covers &mdash; UFC 331 odds for Sept. 19: Van vs. Pantoja", "https://www.covers.com/ufc/331-odds-saturday-sept-19-2026"),
        ("CBS Sports &mdash; UFC 331 fight card predictions and odds", "https://www.cbssports.com/ufc/news/ufc-331-fight-card-predictions-joshua-van-alexandre-pantoja-expert-picks/"),
        ("Yahoo Sports &mdash; UFC 331 full fight card, start time, odds, how to watch", "https://sports.yahoo.com/mma/article/ufc-331-full-fight-card-start-time-odds-where-to-watch-and-everything-to-know-for-van-vs-pantoja-2-200052945.html"),
        ("ESPN &mdash; Current and all-time UFC champions (cross-check; regression refused this run)", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
        ("Bloody Elbow &mdash; Leaked email suggests Michael &lsquo;Venom&rsquo; Page has been released", "https://bloodyelbow.com/2026/09/07/leaked-email-suggests-michael-venom-page-has-been-released-following-his-win-at-ufc-paris/"),
        ("MMA Weekly &mdash; Michael &ldquo;Venom&rdquo; Page has offers from everyone following UFC release", "https://www.mmaweekly.com/news/michael-venom-page-has-offers-from-everyone-following-ufc-release"),
        ("Bloody Elbow &mdash; Ex-UFC title challenger signs new eight-fight deal (Blaydes)", "https://bloodyelbow.com/2026/08/21/ex-ufc-title-challenger-survives-trend-of-surprise-roster-removals-by-signing-new-8-fight-deal/"),
        ("TKO Group Holdings &mdash; UFC Freedom 250 delivers 34 million total global viewers", "https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx"),
        ("ESPN &mdash; UFC's first Paramount+ fight card averages nearly 5M views", "https://www.espn.com/espn/story/_/id/47738036/ufc-first-paramount+-fight-card-averages-nearly-5m-views"),
        ("Front Office Sports &mdash; UFC touts ratings success of CBS deal", "https://frontofficesports.com/ufc-touts-ratings-success-cbs-deal/"),
    ]))
    o.append(DISC_MMA)
    o.append('</footer>')
    o.append("""<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00').getTime();
var el=document.getElementById('ufccdn');if(!el)return;
function tick(){var d=t-Date.now();if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}
var m=Math.floor(d/60000),h=Math.floor(m/60),dy=Math.floor(h/24);
el.textContent=dy+'d '+(h%24)+'h '+(m%60)+'m';}
tick();setInterval(tick,30000);})();</script>""")
    o.append(FOOT)
    return "".join(o)


for name, fn in (("index.html", build_index), ("cyber-briefing.html", build_cyber),
                 ("wallstreet-briefing.html", build_ws), ("mma-briefing.html", build_mma)):
    html = fn()
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)
    print(name, len(html))
