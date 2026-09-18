# -*- coding: utf-8 -*-
"""Third run of 2026-09-18 (Friday), ~3:38pm ET. Afternoon Edition, markets OPEN (~22 min to the close)."""
import os, datetime
from css import base_css, nav, head, sources, STAMP_JS

OUT = "/sessions/eloquent-magical-fermat/mnt/outputs"
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
TL_WS = ("Stocks were close to flat into the final half hour of a triple-witching Friday &mdash; Trading "
         "Economics&rsquo; ~3:37 PM ET board had its S&amp;P 500 proxy up 0.05%, its Nasdaq 100 proxy up 0.24% and its "
         "Dow proxy down 0.24% &mdash; with the 10-year yield back near 5% and crude reversing the morning&rsquo;s "
         "decline to trade higher.")
TL_CY = ("Microsoft disclosed two maximum-severity cloud flaws on Friday &mdash; an authentication "
         "bypass in Microsoft Fabric and a data-authenticity failure in Azure Billing, both CVSS 10.0 and both fixed "
         "server-side &mdash; while the actively exploited Cisco Identity Services Engine bypass still carries a "
         "federal remediation deadline of tomorrow.")
TL_MMA = ("UFC 331 is set: all 24 athletes made weight in Los Angeles, Joshua Van opens a &minus;130 favourite over "
          "Alexandre Pantoja in Saturday&rsquo;s flyweight title rematch, and the promotion cleared nine fighters from "
          "the roster this week to make room for the Contender Series class.")


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
    DUE = datetime.date(2026, 9, 19)
    o = [head("The Cyber Wire &mdash; Daily Briefing", css)]
    o.append(mast("The Cyber Wire",
                  "Your daily cybersecurity briefing &mdash; breaches, vulnerabilities &amp; federal deadlines"))
    o.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % TL_CY)
    o.append(FRESH)
    o.append(nav("cyber"))

    o.append('<div class="banner high"><span class="k">Threat Level: High</span>'
             '<span>A CVSS 10.0 authentication bypass in Cisco Identity Services Engine is being exploited in the '
             'wild, and CISA told federal agencies to remediate it by <b>Saturday, 19 September 2026</b> &mdash; '
             '%s. Two more maximum-severity Microsoft cloud flaws were published this week.</span></div>' % kevtxt(DUE))

    o.append('<div class="stats">'
             '<div class="stat"><div class="n">10.0</div><div class="l">CVSS of CVE-2026-76460 (Cisco ISE), rated by Cisco and exploited in the wild</div></div>'
             '<div class="stat"><div class="n">28</div><div class="l">Critical CVEs disclosed 18 Sep, up 47% from 19 the prior day; six actively exploited (CVE Brief)</div></div>'
             '<div class="stat"><div class="n">566,000+</div><div class="l">Registered users of NightmareStresser, the DDoS-for-hire service seized by the FBI</div></div>'
             '<div class="stat"><div class="n">73.6%</div><div class="l">Of 61,500 abandoned Android IoT companion apps found to carry vulnerabilities</div></div>'
             '</div>')

    o.append('<h2 class="sec">Top Story</h2>')
    o.append('<div class="topstory">'
             '<h3>Two CVSS 10.0 holes in Microsoft&rsquo;s cloud, both fixed without anyone having to patch</h3>'
             '<p><b>CVE-2026-69843</b> is an authentication bypass by spoofing in <b>Microsoft Fabric</b>, scored '
             '<b>CVSS 10.0</b> and classified CWE-287. It needs no credentials and no user interaction: the attack '
             'vector is the network and the scope metric is changed, which is the part that matters &mdash; an '
             'attacker crosses out of the network boundary and lands directly in the analytics and data tier where '
             'OneLake keeps enterprise data.</p>'
             '<p><b>CVE-2026-62874</b> hits <b>Azure Billing</b> with an insufficient data-authenticity verification '
             'flaw (CWE-345), also <b>CVSS 10.0</b>. An unauthenticated attacker on the network can elevate privilege '
             'and, in the wording of the write-ups, compromise the financial integrity of a tenant.</p>'
             '<p>Both were published on 18 September and both were addressed by Microsoft server-side, so there is '
             '<b>no customer action</b> and no patch to deploy. That is the pattern worth noticing rather than the '
             'scores: the flaws with the highest numbers this week were in the parts of the stack customers cannot '
             'inspect, cannot patch and cannot verify were ever vulnerable. The ones that need your attention today '
             'are the smaller numbers with deadlines attached &mdash; see Patch Priority.</p>'
             '</div>')

    o.append('<h2 class="sec">Patch Priority</h2>')
    o.append('<div class="callout crit"><div class="k">Do this first</div>'
             '<p><b>CVE-2026-76460 &mdash; Cisco Identity Services Engine and ISE-PIC.</b> Authentication bypass, '
             'Cisco-rated <b>CVSS 3.1 10.0</b> (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H), exploited in the wild, emergency '
             'fixes issued. Added to the CISA KEV catalog on 16 September with a federal remediation date of '
             '<b>Saturday, 19 September 2026</b> &mdash; <b>%s</b>. ISE sits in front of network access for the whole '
             'estate; an authentication bypass there is a bypass of everything behind it.</p>'
             '<p class="note">This date appears in exactly three places on this page &mdash; the threat banner above, '
             'this box and the KEV section below &mdash; and the countdown is computed, not typed.</p>'
             '</div>' % kevtxt(DUE))

    o.append('<h2 class="sec">Threat Actor Spotlight</h2>')
    o.append('<div class="card"><div class="k">PeckBirdy &middot; China-aligned</div>'
             '<h4>A JavaScript C2 framework hiding behind casino and adult sites</h4>'
             '<p>Infoblox research, reported by The Register on 15 September, describes <b>PeckBirdy</b> as a '
             'JavaScript command-and-control framework in use by China-aligned APT groups since 2023, with its '
             'infrastructure concealed inside low-quality Chinese-language casino and adult websites. Targets are '
             'Asian government and corporate organisations; the loader abuses MSHTA and Windows Script Host. Infoblox '
             'says <b>just over 3%</b> of its enterprise customers resolved at least one PeckBirdy C2 domain, and that '
             'resolving <b>three to ten distinct domains</b> is a meaningful signal of compromise rather than noise. '
             'The casino-and-adult hosting choice is deliberate: those domains are noisy, disposable, and the sort of '
             'traffic a security team is inclined to write off as an employee&rsquo;s bad browsing habit.</p>'
             '<p class="note">Re-confirmed this run by a search-level summary describing the same casino and '
             'adult-site concealment; the underlying Infoblox reporting is carried from this site&rsquo;s standing '
             'corrections file.</p></div>')

    o.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
    o.append('<div class="cards two">')
    o.append('<div class="card"><span class="tag c">Takedown</span>'
             '<h4>FBI seizes NightmareStresser, one of the longest-running booters</h4>'
             '<p>The Justice Department announced a court-authorised seizure on <b>15 September</b> shutting down the '
             'websites behind <b>NightmareStresser</b>, active since at least 2022 and used for hundreds of thousands '
             'of actual or attempted DDoS attacks worldwide. The service rented botnets built from compromised routers '
             'and IoT devices, had <b>over 566,000 registered users</b> and could reach <b>200 Gbps</b>. Victims named '
             'include educational institutions, government agencies and gaming platforms, with the case run out of '
             'Alaska. It is the latest action under <b>Operation PowerOFF</b>, the multinational campaign against '
             'DDoS-for-hire infrastructure that began in December 2018 with fifteen site seizures.</p></div>')
    o.append('<div class="card"><span class="tag new">New</span><span class="tag w">Maritime</span>'
             '<h4>Coast Guard confirms malicious cyber activity aboard the VL Prosperity</h4>'
             '<p>The Coast Guard has confirmed evidence of malicious cyber activity on the vessel <b>VL Prosperity</b> '
             'but <b>has not attributed</b> it to Iran. The restraint is the story: shipping incidents in and around '
             'the Strait of Hormuz are being reported alongside kinetic attacks on tankers this week, and an '
             'unattributed finding is not the same as a state-sponsored one.</p></div>')
    o.append('<div class="card"><span class="tag new">New</span><span class="tag m">Research</span>'
             '<h4>61,500 abandoned Android IoT companion apps, 73.6% of them vulnerable</h4>'
             '<p>Researchers examined <b>61,500 abandoned Android Internet-of-Things companion applications</b> &mdash; '
             'the phone apps that pair with a bulb, a lock, a camera &mdash; and found <b>73.6%</b> presented '
             'vulnerabilities. Abandonment is the mechanism: the hardware keeps working, the app stays installed, and '
             'nobody is shipping fixes for either.</p></div>')
    o.append('<div class="card"><span class="tag a">Surveillance</span>'
             '<h4>A Flock camera pulled off its pole yields 50,200 vehicles in 21 days</h4>'
             '<p>A group calling itself <b>stegan0gram</b> physically removed a Flock automated licence-plate-reader '
             'camera and shared what it found with <b>Wired</b> and <b>404 Media</b>: <b>50,200 vehicles</b> and '
             '<b>1.6 million photographs</b> captured in <b>21 days</b>. Flock, in a statement to The National News '
             'Desk, characterised this as local storage on a single device rather than a compromise of its cloud.</p>'
             '</div>')
    o.append('</div>')
    o.append('<div class="note"><b>Two</b> items are tagged New this edition &mdash; the Coast Guard finding and the '
             'abandoned-app study &mdash; neither of which appears in any of the 765 archived snapshots. The '
             'NightmareStresser seizure and the Flock camera both appeared in earlier editions and are therefore not '
             'tagged. The Top Story is also new material by the same test &mdash; no prior snapshot mentions '
             'Microsoft Fabric, Azure Billing, CVE-2026-69843 or CVE-2026-62874 &mdash; but Top Story blocks do not '
             'carry tags on this site.</div>')

    o.append('<h2 class="sec">Vulnerability Watch</h2>')
    rows = [
        ("CVE-2026-69843", "10.0", "Microsoft Fabric",
         "Authentication bypass by spoofing (CWE-287). Network vector, no privileges, no user interaction, scope changed. Fixed server-side; no customer action."),
        ("CVE-2026-62874", "10.0", "Azure Billing",
         "Insufficient data authenticity verification (CWE-345). Unauthenticated network attacker can elevate privilege. Fixed server-side; no customer action."),
        ("CVE-2026-76460", "10.0 <span class='down'>(exploited)</span>", "Cisco ISE / ISE-PIC",
         "Authentication bypass, Cisco-rated. In CISA KEV since 16 Sep; federal deadline 19 Sep. Emergency fixes issued."),
        ("CVE-2026-53266", "8.8", "Linux kernel (netfilter bridge, ebtables SNAT)",
         "Out-of-bounds write; local privilege escalation. Added to KEV 18 Sep. Score is CVE Security&rsquo;s; no distinct vendor number was found this run."),
        ("CVE-2025-39964", "<span class=\"tag w\">disputed</span> 7.8 / 3.3", "Linux kernel (AF_ALG crypto user API)",
         "Race condition: two writers on one AF_ALG socket interleave request payloads, corrupting crypto results or causing denial of service. Added to KEV 18 Sep. CVE Security scores it 7.8, Strix 3.3 &mdash; both printed, neither asserted."),
        ("vm2 (four CVEs)", "9.9&ndash;10", "patriksimek vm2",
         "Sandbox-escape flaws, four of them scored 9.9 or higher in the 18 Sep disclosure batch. Individual identifiers were not stated in any source read this run, so none are printed."),
    ]
    o.append('<div class="tblwrap"><table><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>')
    for c, s, a, n in rows:
        o.append('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (c, s, a, n))
    o.append('</table></div>')

    o.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b>CVE-2026-76460 &mdash; Cisco Identity Services Engine.</b> Added <b>16 September</b>; remediate '
             'by <b>19 September 2026</b> (<span class="down">%s</span>).</li>' % kevtxt(DUE))
    o.append('<li><b>CVE-2026-87886 &mdash; Acronis Backup</b>, incorrect default permissions. Added the same day, '
             '16 September. <b>No due date for this entry was confirmed in any source read this run, and none is '
             'asserted anywhere on this page.</b></li>')
    o.append('<li><b>CVE-2026-53266</b> (Linux kernel out-of-bounds write) and <b>CVE-2025-39964</b> (Linux kernel '
             'race condition) were both added on <b>18 September</b>. A search-level rendering logged in this '
             'site&rsquo;s corrections file gives both a due date of <b>21 September 2026</b>; that date could not be '
             're-confirmed this run, so it is reported as attributed rather than as a verified deadline.</li>')
    o.append('<li>Earlier September additions, for context: seven on 2 September (Sangoma Switchvox, Starlette, '
             'Kestra, LiteLLM, JFrog Artifactory and two SonicWall SMA1000 flaws), four on 8 September (Adobe '
             'Commerce/Magento, two Microsoft Windows, N-able N-central) and one on 11 September (GitLab CE/EE path '
             'traversal).</li>')
    o.append('<li>The governing directive named on the 2026 additions is <b>BOD 26-04</b>, &ldquo;Prioritizing '
             'Security Updates Based on Risk&rdquo;, which is what makes a three-day remediation window coherent; the '
             'older <b>BOD 22-01</b> three-week schedule it supersedes is mentioned here only to explain that '
             'difference.</li>')
    o.append('</ul></div>')

    o.append('<h2 class="sec">Refused This Run</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li>A claim that attacks on manufacturers <b>rose 40% in early 2026</b> surfaced again in a search '
             'summary with <b>no identifiable publisher</b>. Refused for a second consecutive edition.</li>')
    o.append('<li><b>CVE-2026-58138</b>, described as unauthenticated remote code execution via inline workflow '
             'definitions, still has <b>no affected product named</b> by any source read this run. Refused.</li>')
    o.append('<li>Direct fetches of cisa.gov&rsquo;s 16 and 18 September alert pages and of cvebrief.com returned '
             '<b>empty bodies</b> again. Everything above that rests on those pages is sourced from search-level '
             'renderings and CVE databases, and this page says so rather than implying a direct read of CISA.</li>')
    o.append('</ul></div>')

    o.append(sources([
        ("CISA &mdash; Adds two known exploited vulnerabilities to catalog (18 Sep)",
         "https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
        ("CISA &mdash; Adds two known exploited vulnerabilities to catalog (16 Sep)",
         "https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
        ("CISA &mdash; Known Exploited Vulnerabilities Catalog",
         "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
        ("CVE Brief &mdash; 18 September 2026", "https://cvebrief.com/archive/2026/09/18/"),
        ("Strix &mdash; CVE-2026-69843 (Microsoft Fabric, CVSS 10)", "https://www.strix.ai/cve/CVE-2026-69843"),
        ("Strix &mdash; CVE-2026-62874 (Azure Billing, CVSS 10)", "https://www.strix.ai/cve/CVE-2026-62874"),
        ("VulDB &mdash; CVE-2026-69843 in Fabric", "https://vuldb.com/cve/CVE-2026-69843"),
        ("Microsoft Security Update Guide", "https://msrc.microsoft.com/update-guide/"),
        ("The Hacker News &mdash; US seizes NightmareStresser domains",
         "https://thehackernews.com/2026/09/us-seizes-nightmarestresser-domains.html"),
        ("Help Net Security &mdash; FBI takes down one of the longest-running DDoS-for-hire services",
         "https://www.helpnetsecurity.com/2026/09/17/fbi-nightmarestresser-ddos-for-hire-service-seized/"),
        ("SecurityOnline &mdash; Linux kernel vulnerabilities exploited in the wild",
         "https://securityonline.info/linux-kernel-vulnerabilities-exploited/"),
        ("SecurityWeek", "https://www.securityweek.com/"),
    ]))
    o.append(DISC_CY)
    o.append('</footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ WALL STREET
def build_ws():
    css = base_css("#caa64a", "#e8c766", "#0b0a08", "#171512", "#2b2621") + """
h1,h3,h4,.lead h3{font-family:Georgia,'Times New Roman',serif;font-weight:600}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);
  display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up)}
.tickers{display:grid;gap:12px;margin-bottom:8px}
@media(min-width:700px){.tickers{grid-template-columns:repeat(3,1fr)}}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
.lead{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:18px 20px}
.lead h3{margin:0 0 9px;font-size:21px;line-height:1.3}
.lead p{margin:0 0 10px;font-size:14.5px;color:#ded9d1}
.lead p:last-child{margin-bottom:0}
"""
    o = [head("The Closing Bell &mdash; Daily Briefing", css)]
    o.append(mast("The Closing Bell",
                  "Your daily markets briefing &mdash; the tape, the drivers &amp; what&rsquo;s next"))
    o.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % TL_WS)
    o.append(FRESH)
    o.append(nav("ws"))

    # BLOCK A
    o.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
             '<script src="%s" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
             '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
             '{"proName":"NASDAQ:XENE","title":"Xenon"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},'
             '{"proName":"NYSE:BRK.A","title":"Berkshire"},{"proName":"NASDAQ:SNDK","title":"Sandisk"},'
             '{"proName":"NYSE:ORCL","title":"Oracle"},{"proName":"TVC:USOIL","title":"WTI Crude"},'
             '{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,'
             '"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>' % (TV % 'ticker-tape'))

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

    # LEAD
    o.append('<h2 class="sec">The Lead</h2>')
    o.append('<div class="lead">'
             '<h3>Flat into the last half hour of a triple-witching Friday, with Buffett stepping back and yields '
             'climbing again &mdash; as of ~3:37 PM ET</h3>'
             '<p>Trading Economics&rsquo; live board, read at about <b>3:37 PM ET</b>, had its <b>S&amp;P 500 proxy at '
             '7,641.18, up 4 points or 0.05%</b>; its <b>Nasdaq 100 proxy at 29,517, up 70 or 0.24%</b>; and its '
             '<b>Dow proxy at 51,655, down 123 or 0.24%</b>. A slightly earlier read on the same site showed the '
             'small-cap <b>US2000 proxy down 0.59%</b>. All four are <b>contract-for-difference proxies</b>, per '
             'Trading Economics&rsquo; own disclaimer, not official exchange values. Trading Economics headlined the '
             'session <i>&ldquo;US Stocks Trade Muted at Week End&rdquo;</i> and noted the Dow opened 0.25% lower.</p>'
             '<p>The week&rsquo;s governing variable has not changed. The <b>10-year Treasury yield</b> was at '
             '<b>4.993%, up 0.056 percentage points</b> (about 5.6 basis points) on the Trading Economics bond table '
             '&mdash; consistent with a CNBC read describing the yield up more than five basis points at 4.998% after '
             'briefly crossing back above 5%. It reached its highest level since July 2007 earlier in the week. The '
             'Fed raised its benchmark to <b>3.75%&ndash;4.00%</b> on Wednesday, its first increase in three years, '
             'while signalling another later this year.</p>'
             '<p>Two things give the session its shape. First, <b>today is triple witching</b> &mdash; the quarterly '
             'simultaneous expiry of stock options, index futures and index options, which falls on the third Friday '
             'of March, June, September and December. TheStreet Pro&rsquo;s James DePorre warned in advance that it '
             '&ldquo;tends to produce heavy volume and sharp swings, particularly in the final hour&rdquo; and that '
             'the action is mechanical: <i>&ldquo;If the action is volatile into the close, don&rsquo;t read too much '
             'into it.&rdquo;</i> Second, <b>Warren Buffett, 96, is stepping down as chairman of Berkshire '
             'Hathaway</b>, announced in a letter to shareholders this morning. He becomes chairman emeritus '
             'effective immediately and stays on the board; his son <b>Howard Buffett</b> takes the chairmanship and '
             '<b>Susan Decker</b> remains lead independent director. It comes a little over nine months after Greg '
             'Abel, 64, became chief executive. &ldquo;Father Time always wins,&rdquo; Buffett wrote. &ldquo;He has, '
             'however, been generous with me.&rdquo;</p>'
             '<p>Underneath, the split is sharp: crypto-linked equities ripped, semiconductors held up, and rate-'
             'sensitive corners &mdash; utilities, real estate, small caps &mdash; took the damage.</p>'
             '</div>')

    # MOVERS
    o.append('<h2 class="sec">Movers &amp; Drivers</h2>')
    o.append('<div class="cards two">')
    o.append('<div class="card"><div class="k">Biotech &middot; the session&rsquo;s big decliner</div>'
             '<h4>Xenon Pharmaceuticals pauses Phase 3 enrolment</h4>'
             '<p><b>XENE</b> fell hard after voluntarily pausing new patient enrolment in ongoing Phase 3 trials of '
             '<b>azetukalner</b> for focal seizures in epilepsy. The size of the fall depends entirely on which clock '
             'you read: <b>&minus;22.24%</b> premarket (TheStreet, 8:38 AM), <b>&minus;29%</b> and <b>&minus;29.1%</b> '
             'at 10:29 and 11:44 AM, <b>&minus;23.0%</b> in Stock Market Watch&rsquo;s prose and <b>&minus;31% at '
             '$39.80</b> in that site&rsquo;s live losers table. All five are printed; none is asserted as the '
             'figure. Call it a quarter to a third of the company&rsquo;s value.</p></div>')
    o.append('<div class="card"><div class="k">Crypto complex</div>'
             '<h4>Digital-asset equities break out</h4>'
             '<p>The day&rsquo;s clearest risk-on trade. <b>Strategy (MSTR)</b> was up <b>13.14%</b> and '
             '<b>Coinbase (COIN) 11.58%</b> at midday on TheStreet&rsquo;s board, with <b>MARA Holdings +10.22%</b>, '
             '<b>BitMine +7.92%</b>, <b>Robinhood +7.87%</b> and <b>Galaxy Digital +7.59%</b>. The ETF proxies moved '
             'with them: <b>ETHA +5.87%</b>, <b>IBIT +5.81%</b> at 12:07 PM. Trading Economics had <b>Bitcoin at '
             '$79,038, +3.44%</b>, and <b>Ether at $2,531.28, +3.42%</b>, at ~3:37 PM. Two catalysts are cited and '
             'they do not agree: TheStreet attributes the early move to the SEC&rsquo;s five-year conditional '
             '&ldquo;Innovation Exemption&rdquo; for tokenised US-listed stocks, and separately to legislative '
             'progress in the House &mdash; days after the Senate failed to pass crypto market legislation.</p></div>')
    o.append('<div class="card"><div class="k">Semis &amp; memory</div>'
             '<h4>Broadcom, Micron and Sandisk carry the tape</h4>'
             '<p><b>Broadcom (AVGO) +3.74%</b> to $360.29 and <b>Micron (MU) +1.47%</b> to $991.84 on Trading '
             'Economics&rsquo; ~3:37 PM component table; the VanEck semiconductor ETF <b>SMH</b> was up 0.65% at '
             'midday. <b>Sandisk (SNDK)</b> is the memory standout &mdash; <b>+4.93%</b> per TheStreet at 10:29 AM '
             'but <b>+7.6% at $1,737.27</b> in Stock Market Watch&rsquo;s live table, whose own prose said +0.9%. '
             'Both are printed. Sandisk joins the S&amp;P 100 on 21 September.</p></div>')
    o.append('<div class="card"><div class="k">Downside &middot; old economy</div>'
             '<h4>GM, Nucor and Palo Alto Networks</h4>'
             '<p><b>General Motors &minus;5.16%</b>, pulling back with the auto complex after Volkswagen cut its '
             'outlook on an <b>$11.5 billion</b> hit. <b>Nucor &minus;5.33%</b> after third-quarter profit guidance '
             'came in below expectations. <b>Palo Alto Networks &minus;4.14%</b> after Bernstein cut it from '
             'Outperform to Market Perform on valuation following a sector-wide rally. <b>Oracle</b> was down '
             '<b>2.50%</b> to $146.82 at ~3:37 PM.</p></div>')
    o.append('</div>')
    o.append('<div class="note">This page carries <b>zero</b> New tags this edition, and that is the result of the '
             'check rather than an omission: every name in the four cards above &mdash; Xenon, Strategy, Coinbase, '
             'MARA, BitMine, Galaxy Digital, Broadcom, Micron, Sandisk, General Motors, Nucor, Palo Alto Networks, '
             'Oracle &mdash; already appears in at least one of the 765 archived snapshots, as do the SpaceX '
             'rebalance, the Silicon Valley Bank review and the F-35 sale below. Today&rsquo;s tape is a new day for '
             'names this site has already written about.</div>')

    # CHART OF THE DAY
    o.append('<h2 class="sec">Chart of the Day &mdash; Xenon Pharmaceuticals (XENE)</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"symbol":"NASDAQ:XENE","width":"100%%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>'
             % (TV % 'mini-symbol-overview'))
    o.append('<div class="note">Still the session&rsquo;s largest sourced single-name decline, on the voluntary pause '
             'of new Phase 3 enrolment described above.</div>')

    # SECTOR HEAT
    o.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
             '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
             '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%%","height":420}</script></div>'
             % (TV % 'stock-heatmap'))
    o.append('<div class="note">Editorial read, from Stock Market Watch&rsquo;s ETF-proxy sector strip at <b>12:07 PM '
             'ET</b>: leaders were crypto (ETHA +6.4%, IBIT +6.0%), AI (+0.8%) and semiconductors (+0.6%); laggards '
             'were nuclear (&minus;2.0%), materials (&minus;1.4%), utilities (&minus;1.3%) and biotech '
             '(&minus;1.3%). These are sector ETFs, not the GICS sector indices, and the timestamp is four hours '
             'before this edition &mdash; a separate same-day source put industrials best and energy worst, which is '
             'not reconcilable with the above, so no single leading/lagging pair is asserted.</div>')

    # CALENDAR
    o.append('<h2 class="sec">The Calendar &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"colorTheme":"dark","isTransparent":true,"width":"100%%","height":420,"locale":"en",'
             '"importanceFilter":"0,1","countryFilter":"us"}</script></div>' % (TV % 'events'))

    # HEADLINES
    o.append('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%%","height":420,"locale":"en"}</script></div>'
             % (TV % 'timeline'))
    # -- continues --

    # WEEKLY SCORECARD
    o.append('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2>')
    o.append('<div class="tblwrap"><table><tr><th>Session</th><th>S&amp;P 500</th><th>Nasdaq Composite</th>'
             '<th>Dow Jones Industrial Average</th></tr>')
    for day in ("Mon 14 Sep", "Tue 15 Sep", "Wed 16 Sep", "Thu 17 Sep"):
        o.append('<tr><td>%s</td><td>Not re-verified this run</td><td>Not re-verified this run</td>'
                 '<td>Not re-verified this run</td></tr>' % day)
    o.append('<tr><td><b>Fri 18 Sep</b></td><td>Session in progress</td><td>Session in progress</td>'
             '<td>Session in progress</td></tr>')
    o.append('</table></div>')
    o.append('<div class="note">No official exchange close for any session this week was re-fetched during this run, '
             'so nothing is carried forward into these cells. The one candidate figure that did appear &mdash; a '
             'Trading Economics summary describing the S&amp;P 500 proxy at 7,637.29, &ldquo;increasing 85.95 or 1.14 '
             'percent&rdquo; and labelled Friday &mdash; is the <i>previous</i> session&rsquo;s move on a page stamped '
             'today, and it is a CFD proxy in any case. An empty table with an explanation beats a table filled with '
             'figures that do not reconcile.</div>')

    # RATES & COMMODITIES
    o.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
    rows = [
        ("US 10-year Treasury yield", "4.993%", "+0.056 pp (~5.6 bp)", "up"),
        ("UK 10-year gilt yield", "5.297%", "+0.061 pp (~6.1 bp)", "up"),
        ("Fed funds target range", "3.75%&ndash;4.00%", "+25 bp on 16 Sep, first hike in three years", ""),
        ("WTI crude", "$103.204", "+1.27%", "up"),
        ("Brent crude", "$104.789", "&minus;0.03%", "down"),
        ("Natural gas", "$2.9094", "+0.29%", "up"),
        ("Gold", "$4,354.39", "+0.30%", "up"),
        ("Silver", "$66.394", "+1.84%", "up"),
        ("Bitcoin", "$79,038", "+3.44%", "up"),
        ("US dollar index (DXY)", "100.504", "+0.26%", "up"),
    ]
    o.append('<div class="tblwrap"><table><tr><th>Instrument</th><th>Level</th><th>Change</th></tr>')
    for n, lv, ch, cls in rows:
        o.append('<tr><td>%s</td><td>%s</td><td%s>%s</td></tr>'
                 % (n, lv, (' class="%s"' % cls) if cls else "", ch))
    o.append('</table></div>')
    o.append('<div class="note">Trading Economics live tables, read at about <b>3:37 PM ET</b>. Yield changes are in '
             '<b>percentage points</b>, not percent-of-yield &mdash; the 10-year moved roughly 5.6 basis points, not '
             '5.6 percent. Green means the instrument rose and red means it fell, including for Brent, whose '
             '&minus;0.03% is a fall on a level that barely moved. Each percentage above was recomputed from the '
             'printed level and points change and reconciles; natural gas is the one exception, where the change '
             'column is rounded to two decimals and so cannot reproduce 0.29% exactly.</div>')
    o.append('<div class="note"><b>Oil reversed during the session, and that is worth flagging rather than '
             'smoothing.</b> At 7:15 AM TheStreet reported WTI down 1.19% and Brent down 1.98% on easing Saudi supply '
             'concerns &mdash; a third straight daily decline, with PVM&rsquo;s Tamas Varga citing Saudi loading via '
             'Oman, product-inventory builds in the US, Singapore and Europe, and higher Chinese fuel exports. By '
             '12:07 PM the crude ETF was still down about 0.8%. The ~3:37 PM board has WTI <b>up</b> 1.27% above '
             '$103. Between those reads, a tanker was hit by an unknown projectile in the Strait of Hormuz, the '
             'second vessel attacked there in hours. <b>That same TheStreet item gave WTI and Brent the identical '
             'level of $100.70 while quoting different percentage moves, which is impossible; that pair is refused '
             'and only the direction is used from it.</b></div>')

    # ON THE RADAR
    o.append('<h2 class="sec">On the Radar</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b>Monday 21 September:</b> SpaceX&rsquo;s Nasdaq-100 weighting more than doubles, to roughly '
             '<b>2.82%</b> from about <b>1.28%</b>, as more shares become publicly tradable after lockup expiries. '
             'Investing.com estimates <b>$15.5&ndash;22 billion</b> of programmatic buying is triggered at today&rsquo;s '
             'close, with the new weighting effective Monday. Trading Economics had SpaceX at <b>$153.79, '
             '&minus;0.66%</b> at ~3:37 PM. <b>Sandisk</b> joins the S&amp;P 100 the same day.</li>')
    o.append('<li><b>Earnings next week</b> (Stock Market Watch): Korea Electric Power Monday; AutoZone Tuesday; '
             'General Mills and Cintas Wednesday; Costco, Nike and Jabil Thursday.</li>')
    o.append('<li><b>Iran.</b> President Trump told Axios he faces a &ldquo;big decision&rdquo; on whether to launch a '
             'major assault, ahead of a planned meeting next week with the leaders of Saudi Arabia, the UAE, Qatar, '
             'Bahrain, Kuwait and Oman. Separately the administration approved a potential <b>$24.3 billion</b> sale '
             'of <b>48 Lockheed Martin F-35s</b> and 49 Pratt &amp; Whitney engines to Saudi Arabia.</li>')
    o.append('<li><b>Supervision.</b> Fed Vice Chair for Supervision Michelle Bowman said Friday that an outside '
             'review by Starling Advisory Group found Fed staff &ldquo;knew, or should have known&rdquo; that Silicon '
             'Valley Bank was vulnerable before its 2023 failure; the review found deposits were &ldquo;94 percent '
             'uninsured and concentrated in venture capital-backed technology companies.&rdquo;</li>')
    o.append('</ul></div>')

    # REFUSALS
    o.append('<h2 class="sec">Refused or Left Unresolved</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b>The VIX is refused for a seventh consecutive edition.</b> Trading Economics printed it at 15 with '
             'a change of &minus;0.23 and a percentage change of &minus;0.23% &mdash; but &minus;0.23 on a level of 15 '
             'is about &minus;1.5%, not &minus;0.23%. Internally inconsistent, so no volatility level is published. '
             'The VIX short-term futures note, VXX, was up 1.16% at 12:07 PM.</li>')
    o.append('<li><b>Meta appears twice on the same source with two different moves</b> &mdash; &minus;1.55% at '
             '$671.71 in the component table and &minus;0.81% at $676.80 in the live share stream, both stamped '
             'today. Both are printed here; neither is used in the editorial.</li>')
    o.append('<li><b>Coinbase and Robinhood percentages do not reconcile across the day</b>: +6.55% / +5.94% at '
             '10:29 AM against +11.58% / +7.87% at 12:26 PM on the same publisher. Both pairs printed with their '
             'timestamps.</li>')
    o.append('<li><b>Sector leadership is unresolved.</b> One same-day source put industrials best (+0.87%) and energy '
             'worst (&minus;2.32%); Stock Market Watch&rsquo;s ETF strip put crypto and semis on top with energy '
             'roughly flat at &minus;0.1%. No leading and lagging pair is asserted.</li>')
    o.append('<li><b>Two tables on Trading Economics disagree with each other</b>, as noted in the Lead: 7,641.18 '
             '/ +0.05% against 7,638 / +0.01% for the S&amp;P proxy, and &minus;0.24% against &minus;0.26% for the '
             'Dow. Both sets reconcile internally against their own printed points changes; the later of the two is '
             'used in the summary line and both are shown. The gap is small, but smoothing it would have hidden the '
             'fact that this source refreshes its tables independently.</li>')
    o.append('<li><b>No after-hours section appears</b> in this edition: the regular session was still open when '
             'these figures were verified.</li>')
    o.append('</ul></div>')

    o.append(sources([
        ("TheStreet &mdash; Stock Market Today, 18 September 2026 (live blog)",
         "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-18-2026"),
        ("Stock Market Watch &mdash; live market updates",
         "https://stockmarketwatch.com/live/stock-market-today"),
        ("Trading Economics &mdash; US500 live quote", "https://tradingeconomics.com/spx:ind"),
        ("Trading Economics &mdash; US30 live quote", "https://tradingeconomics.com/indu:ind"),
        ("Trading Economics &mdash; United States stock market",
         "https://tradingeconomics.com/united-states/stock-market"),
        ("CNBC &mdash; Stock market live updates", "https://www.cnbc.com/2026/09/17/stock-market-today-live-updates.html"),
        ("CNBC &mdash; Buffett stepping down as Berkshire chairman",
         "https://www.cnbc.com/2026/09/18/buffett-stepping-down-as-berkshire-chairman.html"),
        ("CNBC &mdash; Fed review of Silicon Valley Bank supervision",
         "https://www.cnbc.com/2026/09/18/fed-silicon-valley-bank.html"),
        ("Reuters &mdash; Oil prices fall on hopes of limited supply disruptions",
         "https://www.reuters.com/business/energy/oil-prices-fall-1-hopes-limited-supply-disruptions-2026-09-18/"),
        ("Yahoo Finance &mdash; Stock market today, Friday 18 September",
         "https://finance.yahoo.com/markets/live/stock-market-today-friday-september-18-dow-sp-500-nasdaq-080504071.html"),
        ("CBS News &mdash; Iran war live updates, Strait of Hormuz",
         "https://www.cbsnews.com/live-updates/iran-war-trump-us-strait-of-hormuz-oil-houthis/"),
    ]))
    o.append(DISC_WS)
    o.append('</footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ MMA
CHAMPS = [
    ("Heavyweight", "VACANT",
     "Tom Aspinall vacated 14 Sep 2026 (eye injuries). <b>Interim: Ciryl Gane</b> &mdash; KO2 Alex Pereira, Freedom 250, 14 Jun 2026"),
    ("Light Heavyweight", "Carlos Ulberg",
     "KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, 11 Apr 2026"),
    ("Middleweight", "Sean Strickland",
     "Split decision over Khamzat Chimaev, UFC 328, 9 May 2026 &mdash; two-time champion"),
    ("Welterweight", "Islam Makhachev",
     "UD Jack Della Maddalena, UFC 322, 15 Nov 2025; 1 defence &mdash; UD Ian Machado Garry, UFC 330, 15 Aug 2026"),
    ("Lightweight", "Justin Gaethje", "TKO4 Ilia Topuria, Freedom 250, 14 Jun 2026"),
    ("Featherweight", "Alexander Volkanovski",
     "UD Diego Lopes, UFC 314, 12 Apr 2025; defended UD Lopes, UFC 325, 31 Jan 2026. Defends vs. Evloev at UFC 333"),
    ("Bantamweight", "Petr Yan",
     "UD Merab Dvalishvili, UFC 323, 6 Dec 2025. Trilogy bout vs. Dvalishvili at UFC 333"),
    ("Flyweight", "Joshua Van",
     "TKO1 Alexandre Pantoja, UFC 323, 6 Dec 2025; defended TKO5 Tatsuro Taira, UFC 328, 9 May 2026. <b>Rematches Pantoja tomorrow</b>"),
    ("Women&rsquo;s Bantamweight", "Kayla Harrison",
     "Sub2 Julianna Pe&ntilde;a, UFC 316, 7 Jun 2025 &mdash; 0 defences"),
    ("Women&rsquo;s Flyweight", "VACANT",
     "Valentina Shevchenko vacated while sidelined by injury. Natalia Silva vs. Wang Cong contest it at UFC 332, 3 Oct 2026"),
    ("Women&rsquo;s Strawweight", "Mackenzie Dern",
     "Won the vacant belt; defended UD over Gillian Robertson, UFC 330, 15 Aug 2026"),
]

CDN_JS = """<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00');function f(){var n=new Date(),d=t-n,e=document.getElementById('ufccdn');if(!e)return;if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}f();setInterval(f,3e4);})();</script>"""


def build_mma():
    css = base_css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020") + """
.topstory{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:18px 20px}
.topstory h3{margin:0 0 8px;font-size:19px;line-height:1.3}
.topstory p{margin:0 0 9px;font-size:14.5px;color:#e3d2cd}
.topstory p:last-child{margin-bottom:0}
.cdn{background:var(--panel);border:1px solid var(--line);border-radius:11px;padding:11px 16px;margin-bottom:16px;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:10px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent2)}
.cdn .v{font-family:var(--mono);font-size:19px;color:var(--accent2)}
.cdn .w{font-size:13.5px;color:var(--muted)}
.when{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#e8c766;margin-bottom:6px}
.odds{font-size:13px;color:var(--muted);margin-top:8px}
.odds b{color:var(--accent2)}
"""
    o = [head("The Octagon &mdash; Daily Briefing", css)]
    o.append(mast("The Octagon",
                  "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    o.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % TL_MMA)
    o.append(FRESH)
    o.append(nav("mma"))

    o.append('<div class="cdn"><span class="k">Next Card</span><span class="v" id="ufccdn">&nbsp;</span>'
             '<span class="w">UFC 331: Van vs. Pantoja 2 &middot; Sat 19 Sep, main card 9:00 PM ET &middot; '
             'Crypto.com Arena, Los Angeles</span></div>')

    o.append('<h2 class="sec">Top Story</h2>')
    o.append('<div class="topstory">'
             '<h3>UFC 331 is fully made: 24 fighters on weight, a flyweight rematch, and a card that reads deeper '
             'than its main event</h3>'
             '<p>All <b>24</b> scheduled athletes made their limits at Friday&rsquo;s official weigh-ins in Los '
             'Angeles &mdash; <b>Joshua Van 125 / Alexandre Pantoja 125</b>; Tsarukyan 156 / Ruffy 155; Patricio '
             'Pitbull 145.5 / Doo Ho Choi 146; Steveson 240 / Sharaf 241; Menifield 205.5 / Baraniewski 206; Vera 136 '
             '/ Jourdain 135; Tuivasa 264.5 / Despaigne 263. Ceremonial weigh-ins follow Friday evening at '
             'Crypto.com Arena, <b>5:00 PM PT / 8:00 PM ET</b>.</p>'
             '<p>The headline is a rematch nine months in the making. <b>Van</b> took the flyweight title from '
             '<b>Pantoja</b> inside the opening round at UFC 323 last December; Pantoja gets it back on Saturday or '
             'not at all. DraftKings has Van a <b>&minus;130</b> favourite against <b>+110</b> &mdash; about as close '
             'to a coin flip as a champion gets. The full main card, with lines: flyweight title Van (&minus;130) vs. '
             'Pantoja (+110); lightweight Arman Tsarukyan (&minus;305) vs. Mauricio Ruffy (+240); featherweight '
             'Patricio Pitbull (+220) vs. Doo Ho Choi (&minus;270); heavyweight Gable Steveson (&minus;1600) vs. Sean '
             'Sharaf (+900); light heavyweight Alonzo Menifield (+180) vs. Iwo Baraniewski (&minus;220); bantamweight '
             'Marlon Vera (+185) vs. Charles Jourdain (&minus;225); and heavyweight Tai Tuivasa (+500) vs. Robelis '
             'Despaigne (&minus;700).</p>'
             '<p>Early prelims start <b>5:30 PM ET</b>, prelims at <b>7:00</b>, main card at <b>9:00</b>, on '
             'Paramount+. Dana White has also attached a one-off <b>$50,000 &ldquo;Proper Chaos&rdquo; bonus</b> to '
             'the event, tied to the Paramount+ series <i>MobLand</i>, with White choosing the recipient and no '
             'formal scoring criteria announced.</p>'
             '</div>')

    o.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
    o.append('<div class="cards two">')
    o.append('<div class="card"><div class="when">Sat 19 Sep &middot; Crypto.com Arena, Los Angeles</div>'
             '<h4>UFC 331: Van vs. Pantoja 2</h4>'
             '<p>The flyweight title rematch. Champion <b>Joshua Van</b> defends against <b>Alexandre Pantoja</b>, '
             'the man he took the belt from at UFC 323 in December; their first meeting ended inside the opening '
             'round. Co-main is a lightweight fight between <b>Arman Tsarukyan</b> and <b>Mauricio Ruffy</b>. Also on '
             'the card: Olympic gold medallist <b>Gable Steveson</b>, and former two-division Bellator champion '
             '<b>Patricio Pitbull</b> against <b>Doo Ho Choi</b>. Early prelims 5:30 PM ET, prelims 7:00, main card '
             '9:00, Paramount+.</p>'
             '<div class="odds">Odds (DraftKings, via CBS Sports): Van <b>&minus;130</b> / Pantoja <b>+110</b>. '
             'Co-main: Tsarukyan <b>&minus;305</b> / Ruffy <b>+240</b>.</div></div>')
    o.append('<div class="card"><div class="when">Sat 26 Sep &middot; Meta APEX, Enterprise NV</div>'
             '<h4>UFC Fight Night: Rosas Jr. vs. Barcelos</h4>'
             '<p><b>Raul Rosas Jr.</b>, 21, takes his first UFC main event against <b>Raoni Barcelos</b> &mdash; an '
             '18-year age gap in the headliner. The card also carries the <i>TUF: Team Cormier vs. Team Bisping</i> '
             'bantamweight and women&rsquo;s strawweight finals, plus Nakamura vs. Hiestand, across 12 bouts. '
             '8:00 PM EDT, Paramount+.</p>'
             '<div class="odds">No betting line for the headliner appeared in any source read this run, so none is '
             'printed.</div></div>')
    o.append('<div class="card"><div class="when">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>'
             '<h4>UFC 332: Silva vs. Wang</h4>'
             '<p><b>Natalia Silva vs. Wang Cong for the vacant women&rsquo;s flyweight title</b>, the belt Valentina '
             'Shevchenko gave up while sidelined by injury. Thirteen fights, and the promotion&rsquo;s first numbered '
             'main card on <b>CBS</b>.</p>'
             '<div class="odds">No odds were sourced this run and none are printed.</div></div>')
    o.append('<div class="card"><div class="when">Sat 24 Oct &middot; Etihad Arena, Abu Dhabi</div>'
             '<h4>UFC 333: Volkanovski vs. Evloev</h4>'
             '<p>Featherweight champion <b>Alexander Volkanovski</b> defends against <b>Movsar Evloev</b>, with the '
             '<b>Petr Yan vs. Merab Dvalishvili</b> bantamweight trilogy bout in the co-main. Nine fights.</p>'
             '<div class="odds">No odds were sourced this run and none are printed.</div></div>')
    o.append('</div>')

    o.append('<h2 class="sec">Last Event &mdash; Noche UFC, 12 September, Glendale</h2>')
    res = [
        ("Jean Silva", "def. Jose Miguel Delgado", "Submission (rear-naked choke), R3 2:57"),
        ("Brandon Moreno", "def. Joseph Morales", "Split decision"),
        ("Tommy McMillen", "def. Marwan Rahiki", "Unanimous decision (29-28, 29-28, 29-27)"),
        ("Alexa Grasso", "def. Manon Fiorot", "Unanimous decision (29-28 &times;3)"),
        ("Curtis Blaydes", "def. Waldo Cortes Acosta", "Unanimous decision (29-28 &times;3)"),
        ("David Martinez", "def. Dan Ige", "Unanimous decision (30-27, 30-27, 29-28)"),
        ("Sean King III", "def. Jessie Rosas", "KO, R1 0:36 &mdash; UFC debut"),
    ]
    o.append('<div class="tblwrap"><table><tr><th>Result</th><th>Bout</th><th>Method</th></tr>')
    for w, b, m in res:
        o.append('<tr><td class="win">%s</td><td>%s</td><td>%s</td></tr>' % (w, b, m))
    o.append('</table></div>')
    o.append('<div class="note">Main-card results and methods are from UFC.com&rsquo;s own results page. Silva is now '
             '7-1 in the Octagon with six finishes; McMillen moves to 12-0; Martinez is 4-0 in the UFC on an 11-fight '
             'overall streak. <b>Bonuses:</b> Performance of the Night to <b>Jean Silva</b> and <b>Sean King III</b>, '
             'Fight of the Night to <b>McMillen vs. Rahiki</b> &mdash; exactly three awards are named on UFC.com&rsquo;s '
             'bonus page, and no dollar figures appear on it, so none are published. King&rsquo;s knockout time is '
             '<b>0:36</b> per UFC.com; the 33-second figure circulating in secondary summaries is not the official '
             'time.</div>')

    o.append('<h2 class="sec">Prospect Watch &mdash; Contender Series, Season 10 Week 6</h2>')
    o.append('<div class="cards two">')
    for name, wc, line in [
        ("Akbar Abdullaev", "Lightweight",
         "KO (punch), R1 <b>0:19</b>. Dana White called him &ldquo;the greatest talent that&rsquo;s ever been on this show.&rdquo;"),
        ("Mayton Perea", "Welterweight", "KO (punches), R1 <b>0:45</b>. Fighting out of Ecuador."),
        ("Igor Cavalcanti", "Middleweight",
         "TKO (punches), R1 <b>1:38</b>. White singled out the all-action approach; &ldquo;Jacar&eacute;&rdquo; earned the roster spot."),
        ("Luis Hernandez", "Middleweight", "Submission (rear-naked choke), R2 <b>1:01</b>."),
    ]:
        o.append('<div class="card"><span class="tag a">Prospect</span><div class="k">%s</div>'
                 '<h4>%s</h4><p>%s</p></div>' % (wc, name, line))
    o.append('</div>')
    o.append('<div class="note">Four contracts in one night, at Meta APEX &mdash; a record for contract offers in a '
             'Contender Series season, which concludes its tenth run in October. Three of the four finished inside '
             'the first round; the fourth needed a minute of the second.</div>')

    o.append('<h2 class="sec">Around the Sport</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><span class="tag new">New</span> <b>Nine fighters cleared from the roster.</b> The UFC released '
             '<b>Lyman Good, Saygid Izagakhmaev, Bruno Lopes, Bekzat Almakhan, Cody Gibson, Aoriqileng, Ravena '
             'Oliveira, Stewart Nicoll</b> and <b>Hailey Cowan</b>, with the Contender Series intake named as the '
             'reason room was needed. EssentiallySports notes that one of the nine is a teammate of Khabib '
             'Nurmagomedov but does not say which, so none is identified here.</li>')
    o.append('<li><b>Michael Page is not coming back.</b> Dana White has confirmed Page has been removed from the '
             'roster despite a winning record &mdash; &ldquo;What&rsquo;s the confusion?&rdquo; Page went 5-1 in six '
             'UFC fights with no finishes and says he has offers from every other promotion, Rizin among them.</li>')
    o.append('<li><b>Dana White&rsquo;s one-off $50,000 bonus</b> at UFC 331, branded &ldquo;Proper Chaos&rdquo; and '
             'tied to the Paramount+ series <i>MobLand</i>, whose second season premieres Friday. White picks the '
             'recipient; no formal scoring system was announced.</li>')
    o.append('</ul></div>')

    o.append('<h2 class="sec">Rankings &amp; Business</h2>')
    o.append('<div class="panel">'
             '<p><b>Rankings movement.</b> No official ranking update was published in any source read this run, so '
             'none is asserted. Saturday&rsquo;s card is the next real mover: a Pantoja win reclaims the flyweight '
             'belt, and the books make Arman Tsarukyan a heavy &minus;305 favourite in the lightweight '
             'co-main.</p>'
             '<p><b>Business &amp; broadcast.</b> Paramount is in year one of a <b>seven-year, $7.7 billion</b> UFC '
             'media-rights deal through TKO Group. <b>16 million</b> subscriber households have watched <b>180 '
             'million-plus hours</b> of UFC on Paramount+ since the start of the year. UFC 324 averaged <b>4.96 '
             'million</b> on the main card with a <b>7.18 million</b> global household average; Freedom 250 drew '
             '<b>34 million</b> total global viewers per TKO&rsquo;s investor release, with an <b>8.2 million</b> '
             'average per Variety.</p></div>')

    o.append('<h2 class="sec">Champions Board</h2>')
    o.append('<div class="tblwrap"><table><tr><th>Division</th><th>Champion</th><th>Won / last defended</th></tr>')
    for d, c, n in CHAMPS:
        cls = ' class="nc"' if c == "VACANT" else ' class="win"'
        o.append('<tr><td>%s</td><td%s>%s</td><td>%s</td></tr>' % (d, cls, c, n))
    o.append('</table></div>')
    o.append('<div class="note"><b>Verification note.</b> This board is carried from this site&rsquo;s sourced '
             'standing corrections file and was <b>not re-cross-checked against ESPN this run</b> &mdash; direct '
             'fetches of that page have returned no usable body text for several days, and its search-level rendering '
             'has now mis-seated a champion in the wrong division on three consecutive runs, most recently placing '
             'Carlos Ulberg at heavyweight, a belt vacant since Tom Aspinall stepped down on 14 September. What '
             'carries the board instead is chronology: <b>no title bout has taken place since UFC 330 on 15 '
             'August</b> &mdash; Shanghai (29 Aug), Paris and Noche UFC (12 Sep) were all non-title &mdash; so no '
             'belt can have changed hands since. <b>That ends tomorrow:</b> the flyweight row is live at UFC 331 and '
             'this table will need re-verifying against the result before the next edition treats it as current.</div>')
    o.append('<div class="note">MMA carries <b>one</b> New tag this edition &mdash; the nine roster releases. Every '
             'other name on this page has appeared in a prior archived snapshot.</div>')

    o.append(sources([
        ("Yahoo Sports &mdash; UFC 331 full fight card, start time, odds, how to watch",
         "https://sports.yahoo.com/mma/article/ufc-331-full-fight-card-start-time-odds-where-to-watch-and-everything-to-know-for-van-vs-pantoja-2-200052945.html"),
        ("CBS Sports &mdash; UFC 331 odds, fight card predictions",
         "https://www.cbssports.com/betting/news/ufc-331-odds-predictions-time-joshua-van-alexandre-pantoja-2-picks/"),
        ("ESPN &mdash; UFC 331: Van vs. Pantoja 2 fight centre",
         "https://www.espn.com/mma/fightcenter/_/id/600060963/league/ufc"),
        ("Tapology &mdash; UFC 331: Van vs. Pantoja 2", "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
        ("UFC.com &mdash; Welcome to the UFC: DWCS Season 10, Week 6",
         "https://www.ufc.com/news/welcome-ufc-dwcs-season-10-week-6"),
        ("Sherdog &mdash; Dana White hails &lsquo;greatest talent&rsquo; after 19-second KO",
         "https://www.sherdog.com/news/news/Dana-White-hails-greatest-talent-in-DWCS-history-after-19second-KO-202813"),
        ("Heavy &mdash; Dana White hands out 4 new UFC contracts after DWCS Week 6",
         "https://heavy.com/sports/ufc/dana-white-contracts-dwcs-week-6/"),
        ("MMA Mania &mdash; UFC cuts nine fighters in latest roster purge",
         "https://www.mmamania.com/ufc-roster-watch-cuts-tracker-free-agent-aquisitions-mma/472728/ufc-roster-cuts-nine-fighters-contender-series-2026"),
        ("MMA Mania &mdash; Dana White confirms Michael Page will not return",
         "https://www.mmamania.com/ufc-roster-watch-cuts-tracker-free-agent-aquisitions-mma/470585/dana-white-confirms-michael-page-will-not-return-to-the-ufc-whats-the-confusion"),
        ("EssentiallySports &mdash; Nine fighters cut in recent UFC roster purge",
         "https://www.essentiallysports.com/ufc-mma-news-khabib-nurmagomedov-s-teammate-among-nine-fighters-cut-in-recent-ufc-roster-purge/"),
        ("ESPN &mdash; Current and all-time UFC champions (direct fetch returns no body text; see verification note)",
         "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
        ("Wikipedia &mdash; 2026 in UFC", "https://en.wikipedia.org/wiki/2026_in_UFC"),
    ]))
    o.append(DISC_MMA)
    o.append('</footer>')
    o.append('</div>' + CDN_JS + STAMP_JS + '</body></html>')
    return "".join(o)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn, fx in (("index.html", build_index), ("cyber-briefing.html", build_cyber),
                   ("wallstreet-briefing.html", build_ws), ("mma-briefing.html", build_mma)):
        html = fx()
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print(fn, len(html))
