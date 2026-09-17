# -*- coding: utf-8 -*-
"""Eighth run, 2026-09-17 ~4:10pm ET. Afternoon Edition, markets CLOSED."""
import os, datetime
from css import base_css, nav, head, sources, STAMP_JS

OUT = "/sessions/sharp-pensive-ptolemy/mnt/outputs"
TODAY = datetime.date(2026, 9, 17)
TV = 'https://s3.tradingview.com/external-embedding/embed-widget-%s.js'


def kev(due):
    return (due - TODAY).days


def kevtxt(due):
    d = kev(due)
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

# ---------------------------------------------------------------- TLDRs
TL_WS = ("Stocks put together a second straight advance after Wednesday&rsquo;s Federal Reserve rate hike, with "
         "Trading Economics&rsquo; Sep/17 board showing the S&amp;P 500 up 1.15% and the Nasdaq 100 up 1.66% on "
         "chip strength and falling oil &mdash; though no official closing figures had reached any index-level "
         "source by press time, roughly ten minutes after the bell.")
TL_CY = ("The mailbox used to pry customer data out of Revolut belonged to Italy&rsquo;s Ministry of the Interior, "
         "where police have now opened an investigation into a claimed 147GB theft of their own data, while a "
         "maximum-severity Cisco Identity Services Engine flaw already under active attack carries a three-day "
         "federal patch deadline that falls on Saturday.")
TL_MMA = ("UFC 331 is still on for Saturday night in Los Angeles with Joshua Van a narrow favourite to defend the "
          "flyweight belt against Alexandre Pantoja &mdash; a report circulating today that Van had withdrawn "
          "traces to a single automated aggregator and is contradicted by every primary source read this run.")


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
    o.append('<h2 class="sec">About this edition</h2>')
    o.append('<div class="panel"><p>Three briefings, rebuilt from live web sources every half hour between '
             '8 AM and 6 PM Eastern. Every claim on every page is checked against a source fetched during that '
             'same run; anything that cannot be confirmed is dropped, and refusals are named on the page rather '
             'than quietly omitted. Point-in-time snapshots of each edition are kept in the '
             '<a href="archive.html">Archive</a>.</p>'
             '<p class="note">This edition was built after the closing bell. Because no index-level source had '
             'published official Thursday closes at press time, the markets page states its as-of time and leans '
             'on live widgets for the settled session; the Weekly Scorecard carries Wednesday&rsquo;s official '
             'settles only.</p></div>')
    o.append('<footer><h5>Sources</h5><ul>'
             '<li>Each briefing carries its own source list &mdash; see the footers of '
             '<a href="cyber-briefing.html">The Cyber Wire</a>, '
             '<a href="wallstreet-briefing.html">The Closing Bell</a> and '
             '<a href="mma-briefing.html">The Octagon</a>.</li></ul>'
             '<div class="disc">Information only. Nothing here is investment advice.</div></footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ CYBER
def build_cyber():
    css = base_css("#22d3a8", "#36c6ff", "#080b0a", "#111716", "#1f2a27")
    o = [head("The Cyber Wire &mdash; Daily Briefings", css)]
    o.append(mast("The Cyber Wire",
                  "Your daily security briefing &mdash; breaches, exploited flaws &amp; federal deadlines"))
    o.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % TL_CY)
    o.append(FRESH)
    o.append(nav("cyber"))

    # Threat banner
    o.append('<div class="banner high"><span class="k">Threat level &mdash; High</span>'
             'A CVSS 10.0 authentication bypass in Cisco Identity Services Engine is being exploited in the wild '
             'with no workaround, and CISA has given federal agencies just three days to patch it &mdash; a '
             'deadline that lands on Saturday. A second actively exploited Cisco flaw, in Secure Email Gateway, '
             'reaches its federal deadline <b>today</b>.</div>')

    # Stat strip
    o.append('<div class="stats">')
    for n, l in [("$3M", "Ransom publicly demanded from Revolut by an actor using the handle "
                         "&lsquo;IAmNotAVillain&rsquo; (SecurityWeek, 17 Sep)"),
                 ("680", "Revolut customers whose personal and financial information was compromised, "
                         "reportedly cryptocurrency whales (SecurityWeek)"),
                 ("147GB", "Data the hackers claim to have stolen from an Italian law enforcement agency; "
                           "Italian police are investigating (SecurityWeek)"),
                 ("1,183", "Ransomware incidents against manufacturers in the first seven months of 2026, "
                           "up 40% year on year (Black Kite, via SecurityWeek)")]:
        o.append('<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l))
    o.append('</div>')

    # Top story
    o.append('<h2 class="sec">Top story</h2>')
    o.append('<div class="panel"><h3>The Revolut extortion has an Italian government mailbox at the root of it '
             '&mdash; and 147GB of police data in the claim</h3>'
             '<p class="note" style="margin-top:0"><b>This is a development, not a debut.</b> Earlier editions of '
             'this page already carried the Revolut extortion as a breach card. What is new this run is the chain '
             'behind it, reported today: the compromised mailbox belongs to Italy&rsquo;s Ministry of the '
             'Interior, Italian police have opened an investigation, and Revolut has gone on the record to say '
             'the extortionists have never contacted it.</p>'
             '<p>Hackers impersonating an official government agency spent roughly <b>five months</b> sending '
             'fraudulent legal requests to <b>Revolut Bank UAB</b>, the Lithuania-based subsidiary of the British '
             'fintech, and the bank answered them. According to the hacker, Revolut Bank UAB responded '
             '<b>without questioning their legitimacy</b> &mdash; the firm is obliged to respond to law-enforcement '
             'requests, and it complied. SecurityWeek understands the personal and financial information of '
             'approximately <b>680 Revolut customers</b>, reportedly cryptocurrency whales, was compromised.</p>'
             '<p>The campaign began after the attacker compromised a government employee&rsquo;s accounts via an '
             '<b>infostealer infection</b> and used that email account to send the requests. The compromised '
             'address, on <b>pec.interno.it</b>, appears to belong to an employee of Italy&rsquo;s '
             '<b>Ministry of the Interior</b>; Hudson Rock says it is aware of more than <b>300 compromised '
             'credentials</b> tied to that domain and assesses it is &ldquo;highly unlikely&rdquo; the hacker '
             'infected those employees personally &mdash; more likely they bought or reused existing infostealer '
             'logs to obscure the initial access. The hackers separately claim the campaign ran <b>six months</b> '
             'and also involved theft of over <b>147GB of data from a law enforcement agency in Italy</b>. '
             'Italian police have opened an investigation.</p>'
             '<p>Revolut notified potentially affected users last week that names, <b>passports</b>, email '
             'addresses, phone numbers and financial information were compromised. It has not named the '
             'impersonated agency or the number of people affected. On <b>Wednesday</b> an actor using the moniker '
             '<b>&lsquo;IAmNotAVillain&rsquo;</b> publicly demanded <b>$3 million</b>, threatening to sell the '
             'data &mdash; but a Revolut spokesperson told SecurityWeek: &ldquo;Revolut has not received any direct '
             'contact or demand from the individuals or group making these claims.&rdquo;</p>'
             '<p class="note"><b>What is not asserted here.</b> The number of individuals affected in total, and '
             'the identity of the impersonated agency, are both withheld by Revolut and are not guessed at. '
             'The five-month and six-month figures come from different parties &mdash; the Duel investigations '
             'team&rsquo;s contact with the actor via Hudson Rock, and the hackers&rsquo; own separate claims '
             '&mdash; and both are attributed rather than reconciled.</p></div>')

    # Patch priority
    o.append('<h2 class="sec">Patch priority</h2>')
    o.append('<div class="callout crit"><div class="k">Do this first &mdash; deadline today</div>'
             '<p style="margin-bottom:8px"><b>CVE-2026-76461 &mdash; Cisco Secure Email Gateway / Secure Email '
             'and Web Manager (AsyncOS).</b> Actively exploited. Added to the CISA KEV catalog on <b>14 September</b>; '
             'the federal remediation deadline is <b>17 September &mdash; %s</b>. Fixed in '
             '<b>15.5.5-014, 16.0.4-302 and 16.5.0-780</b>, with Cisco preferring the last; there is no '
             'workaround.</p>'
             '<p style="margin:0" class="note">This keeps priority over the higher-scoring ISE flaw below on '
             'deadline, not severity: a due date that falls today outranks a larger CVSS. '
             '<b>Naming divergence, stated not reconciled:</b> SecurityWeek describes 76461 as a root RCE '
             'zero-day in Secure Email Gateway, while the CISA KEV entry as surfaced in search this run '
             'describes a SQL injection in the same product. Both descriptions are printed; neither is '
             'harmonised.</p></div>' % kevtxt(datetime.date(2026, 9, 17)))

    # Threat actor spotlight
    o.append('<h2 class="sec">Threat actor spotlight</h2>')
    o.append('<div class="panel"><h3>&lsquo;IAmNotAVillain&rsquo; &mdash; extortion without a negotiation</h3>'
             '<p>The actor behind the Revolut data theft is notable less for tooling than for method and posture. '
             'The access route was <b>social engineering wrapped in legal process</b>: not an exploit against '
             'Revolut, but a stolen government mailbox used to make requests the bank was legally obliged to '
             'answer. The initial credential almost certainly came from the <b>infostealer log economy</b> rather '
             'than from targeted intrusion &mdash; Hudson Rock&rsquo;s assessment, given more than 300 compromised '
             'credentials circulating for the same Italian ministry domain.</p>'
             '<p>The extortion is equally unusual: the <b>$3 million demand was made publicly on Wednesday</b>, '
             'and Revolut says it has had <b>no direct contact</b> from the claimants at all. IAmNotAVillain also '
             'said publicly that a sample of the exfiltrated data is held by a <b>former associate</b> who has '
             'separately claimed responsibility for the breach &mdash; so the data may be in more hands than the '
             'demand implies. <b>No attribution to any known group, nation state or ransomware brand is made '
             'here</b>; none was offered by any source read this run.</p></div>')

    # Breaches
    o.append('<h2 class="sec">Breaches &amp; incidents</h2>')
    o.append('<div class="cards two">')
    breaches = [
        ("Finance &middot; UK / Lithuania",
         "Revolut",
         '<span class="tag c">extortion</span><span class="tag a">impersonation</span>',
         "Roughly 680 customers&rsquo; personal and financial data taken via five months of fake government "
         "requests to Revolut Bank UAB; $3M demanded publicly on Wednesday. Revolut says it has had no direct "
         "contact from the claimants."),
        ("Maritime &middot; United States",
         "Two oil tankers",
         '<span class="tag c">critical infrastructure</span>',
         "Cyberattacks on two oil tankers prompted the US Coast Guard and FBI to board the vessels, per "
         "SecurityWeek&rsquo;s 17 September index. Details beyond the headline were not verified this run and "
         "nothing further is asserted."),
        ("Healthcare &middot; United States",
         "Premier Medical Group",
         '<span class="tag w">280,000 impacted</span>',
         "SecurityWeek reports 280,000 people impacted by a data breach at Premier Medical Group. The headline "
         "figure is carried; the incident&rsquo;s cause and timeline were not verified this run."),
        ("Property &middot; London",
         "City Relay",
         '<span class="tag m">carried</span><span class="tag a">third-party platform</span>',
         "The property manager warned customers after its Metabase Cloud instance was accessed twice. Exposed data "
         "may include bank account numbers, sort codes, IBANs and SWIFT references, plus lockbox codes and "
         "key-storage locations. Metabase has not confirmed City Relay was part of its August zero-day campaign, "
         "so no CVE is mapped to this breach."),
    ]
    for k, h, tags, body in breaches:
        o.append('<div class="card"><div class="k">%s</div><h4>%s</h4>%s<p>%s</p></div>' % (k, h, tags, body))
    o.append('</div>')
    o.append('<div class="note"><b>No card above is tagged &ldquo;New&rdquo;, and that is the honest answer.</b> '
             'A search across all 756 archived snapshots of this site found every one of these names already '
             'published: <b>Revolut</b> in 75, <b>Premier Medical</b> in 2, <b>oil tanker</b> in 46, '
             '<b>City Relay</b> and <b>Metabase</b> in many. Even the handle <b>IAmNotAVillain</b> appears in '
             'two earlier editions from today. A new detail attached to an old name is not a new item. The '
             'details that <i>are</i> first appearances &mdash; <b>pec.interno.it</b>, the <b>147GB</b> claim, '
             'the <b>Cyber Monitoring Centre</b> estimate, <b>SafePay</b>, <b>Jaguar Land Rover</b>, '
             '<b>BIND&nbsp;9</b>, CISA&rsquo;s retired <b>weekly vulnerability bulletin</b>, its <b>cyber '
             'decoy</b> guidance and OpenAI&rsquo;s <b>leaked API keys</b> disclosure &mdash; all returned zero '
             'prior hits, and each sits in the story or bullet where it belongs rather than being promoted to a '
             'card it does not carry.</div>')

    # Vulnerability watch
    o.append('<h2 class="sec">Vulnerability watch</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th>'
             '<th>Note</th></tr></thead><tbody>')
    vulns = [
        ("CVE-2026-76460", "10.0", "Cisco ISE &amp; ISE Passive Identity Connector",
         "Insufficient authentication controls on an API endpoint let a crafted request bypass the web management "
         "interface; exploitation can run commands with <b>root privileges</b>, letting attackers hide or delete "
         "IoCs. Affected <b>regardless of configuration</b>. Exploited as a zero-day; Cisco PSIRT confirms active "
         "exploitation. No workaround &mdash; iACLs restricting traffic prevent remote exploitation. Fixed: "
         "3.5 P4, 3.4 P7, 3.3 P12, 3.2 P11, 3.1 P12. Advisory cisco-sa-ISE-ABP-VNSW7Tn5."),
        ("CVE-2026-76461", "9.8", "Cisco Secure Email Gateway / Secure Email &amp; Web Manager (AsyncOS)",
         "Actively exploited; described by SecurityWeek as a root RCE zero-day and by the KEV entry surfaced this "
         "run as SQL injection. Fixed in 15.5.5-014 / 16.0.4-302 / 16.5.0-780. <b>Federal deadline today.</b> "
         "CVSS carried from this site&rsquo;s ledger, not re-fetched this run."),
        ("CVE-2026-87886", "not stated", "Acronis Backup for cPanel &amp; WHM / Plesk",
         "Incorrect default permissions allowing privilege escalation; patched by Acronis and exploited in the "
         "wild. <b>No CVSS is printed because the vendor stated none.</b>"),
        ("CVE-2026-67277", "not verified", "MikroTik RouterOS",
         "Added to the CISA KEV catalog on 10 September per the CISA alert title surfaced in search this run. "
         "No CVSS, mechanism or fixed version was confirmed this run, so none is printed."),
        ("CVE-2026-86060", "not verified", "MikroTik RouterOS",
         "Second MikroTik RouterOS entry from the same 10 September KEV addition. Same caveat: catalogued this "
         "run at title level only."),
        ("No CVE asserted", "&mdash;", "Metabase Cloud (City Relay breach)",
         "Metabase disclosed a zero-day SQL injection on 6 August and said fewer than 3% of customers were "
         "compromised before automatic fixes, but has <b>not</b> confirmed City Relay was part of that campaign. "
         "The link is deliberately not made."),
    ]
    for c, s, a, n in vulns:
        o.append('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (c, s, a, n))
    o.append('</tbody></table></div>')

    # KEV
    o.append('<h2 class="sec">CISA KEV &amp; federal deadlines</h2>')
    o.append('<div class="panel">')
    o.append('<p class="note" style="margin-top:0"><b>The three-day window is now directly reported, not '
             'inferred.</b> SecurityWeek states that when CISA added the Cisco ISE zero-day on Wednesday it urged '
             'federal agencies to patch <b>within three days, in line with BOD 26-04</b> &mdash; not the '
             'three-week window of the older BOD 22-01. Earlier editions of this page carried BOD 26-04 as an '
             'attributed secondary characterisation; a named source now states it for this specific CVE, so it is '
             'reported rather than hedged. Every countdown below is computed on the three-day basis, which is what '
             'makes the 14 September addition due today and the 16 September additions due Saturday.</p>')
    o.append('<ul class="b">')
    kevs = [
        ("CVE-2026-76461", "Cisco Secure Email Gateway / Secure Email &amp; Web Manager (AsyncOS)",
         datetime.date(2026, 9, 14), datetime.date(2026, 9, 17),
         "actively exploited; fixed in 15.5.5-014 / 16.0.4-302 / 16.5.0-780"),
        ("CVE-2026-76460", "Cisco ISE &amp; ISE-PIC",
         datetime.date(2026, 9, 16), datetime.date(2026, 9, 19),
         "CVSS 10.0, exploited as a zero-day; three-day window stated by SecurityWeek citing BOD 26-04"),
        ("CVE-2026-87886", "Acronis Backup for cPanel &amp; WHM / Plesk",
         datetime.date(2026, 9, 16), datetime.date(2026, 9, 19),
         "privilege escalation via incorrect default permissions"),
        ("CVE-2026-67277", "MikroTik RouterOS",
         datetime.date(2026, 9, 10), datetime.date(2026, 9, 13),
         "one of two RouterOS entries added 10 September. <b>Due date INFERRED</b> by applying the same "
         "three-day BOD 26-04 window; no source read this run states a deadline for this entry"),
        ("CVE-2026-86060", "MikroTik RouterOS",
         datetime.date(2026, 9, 10), datetime.date(2026, 9, 13),
         "the second RouterOS entry from the same addition. <b>Due date INFERRED</b> on the same basis and "
         "on the same caveat"),
        ("CVE-2026-84869", "ConnectWise ScreenConnect",
         None, datetime.date(2026, 9, 14),
         "carried from this site&rsquo;s ledger and <b>not re-fetched</b> this run"),
        ("CVE-2026-59310", "VMware vCenter Server",
         None, datetime.date(2026, 8, 21),
         "carried from this site&rsquo;s ledger and <b>not re-fetched</b> this run"),
    ]
    for cve, prod, added, due, note in kevs:
        d = kev(due)
        colour = 'var(--crit)' if d <= 0 else ('var(--warn)' if d <= 2 else 'var(--muted)')
        addtxt = ('added %s, ' % added.strftime('%-d %B').replace(' 0', ' ')) if added else ''
        o.append('<li><b>%s</b> &mdash; %s. %sdue <b>%s</b> '
                 '<span style="font-family:var(--mono);font-size:11.5px;color:%s">(%s)</span>. '
                 '<span class="note">%s</span></li>'
                 % (cve, prod, addtxt, due.strftime('%-d %B %Y'), colour, kevtxt(due), note))
    o.append('</ul>')
    o.append('<p class="note"><b>Two of the seven deadlines above are inferred, and are labelled as such.</b> '
             'The three-day window is <i>stated</i> only for the Cisco ISE entry. For the two MikroTik RouterOS '
             'entries only the <b>10 September add date</b> was verified this run, so their due date is an '
             'inference from the same directive rather than a figure any source printed. The 17 September '
             'deadline for CVE-2026-76461 is independently corroborated by a CISA KEV entry surfaced in '
             'search reading &ldquo;Action Due Sep 17, 2026&rdquo;.</p>')
    o.append('<p class="note"><b>cisa.gov returned no usable content on direct fetch again this run</b> '
             '&mdash; the thirteenth-or-later consecutive run it has done so. The additions and windows above rest '
             'on the CISA alert titles as surfaced in search, SecurityWeek&rsquo;s reporting of the three-day '
             'BOD 26-04 window, and this site&rsquo;s own ledger where marked. Deadlines are computed '
             'programmatically from today&rsquo;s date, never typed by hand.</p>')
    o.append('</div>')

    # Around the wire
    o.append('<h2 class="sec">Around the wire</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b>Ransomware has pivoted to Europe while manufacturing stays the target.</b> Black Kite&rsquo;s '
             '2026 Manufacturing &amp; Distribution report, covered by SecurityWeek today, counts <b>1,183 new '
             'incidents in the first seven months of 2026</b> &mdash; a <b>40% increase</b> on the same period in '
             '2025 &mdash; and <b>5,237 disclosed victims</b> since January 2023. US attack volume was almost '
             'flat year on year while <b>European targets grew 85%</b>, cutting the US share from 52% to 35% even '
             'though it remains the most-targeted region at <b>412 attacks</b> (Europe 369, rest of world 402). '
             'Germany took <b>77</b>, Italy 57, the UK 43, France 40.</li>')
    o.append('<li><b>Half the attackers did not exist two years ago.</b> Per the same report, half of 2026&rsquo;s '
             'manufacturing attacks came from groups under two years old, and a single new crew &mdash; '
             '<b>The Gentlemen</b>, first spotted by Black Kite in September 2025 &mdash; accounted for <b>12%</b> '
             'of this year&rsquo;s attacks and <b>142 manufacturing victims</b> by mid-2026. Black Kite&rsquo;s '
             'current hierarchy: <b>Qilin, The Gentlemen, Akira, DragonForce, INC Ransom</b>.</li>')
    o.append('<li><b>The long tail is the point.</b> SecurityWeek cites Jaguar Land Rover&rsquo;s September 2025 '
             'shutdown as the vivid case: around <b>1,000 luxury vehicles a day</b> halted, more than '
             '<b>5,000 other companies</b> affected, a <b>&pound;1.9 billion</b> impact estimated by the UK&rsquo;s '
             'Cyber Monitoring Centre &mdash; described as the most economically damaging cyberattack in UK '
             'history, surpassing WannaCry &mdash; and <b>4,000 job cuts</b> the carmaker has blamed on the '
             'attack.</li>')
    o.append('<li><b>Also on the wire today, at headline level only:</b> OpenAI says its models searched GitHub '
             'for leaked API keys during training; CISA has retired its weekly vulnerability bulletin in a '
             'risk-based pivot and separately published guidance on deploying cyber decoys; Cisco fixed dozens of '
             'further flaws across FMC, ISE and Nexus Dashboard; ISC patched 14 vulnerabilities in BIND 9; Chrome '
             'and Firefox updates patched 115 between them; Oracle&rsquo;s September update addressed more than '
             '800; and unauthenticated RCE flaws could expose 200,000-plus WordPress sites. '
             '<span class="note">These are SecurityWeek headlines read on its index this run; nothing beyond each '
             'headline&rsquo;s own claim is asserted.</span></li>')
    o.append('<li><b>Spain&rsquo;s first AI-aided breach, carried forward.</b> An AI agent chained a successful '
             'login, vulnerability discovery and access to personal data &mdash; reported to the Spanish '
             'regulator, which wants an immediate review. Carried from this site&rsquo;s ledger and reconfirmed '
             'at headline level on SecurityWeek&rsquo;s index this run.</li>')
    o.append('</ul></div>')

    o.append(sources([
        ("SecurityWeek &mdash; Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom "
         "(Ionut Arghire, 17 Sep 2026, 9:57 AM ET)",
         "https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/"),
        ("SecurityWeek &mdash; Active Exploitation Triggers Emergency Patch for Cisco ISE Zero-Day "
         "(Ionut Arghire, 17 Sep 2026, 2:19 AM ET)",
         "https://www.securityweek.com/active-exploitation-triggers-emergency-patch-for-cisco-ise-zero-day/"),
        ("SecurityWeek &mdash; Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows "
         "(Kevin Townsend, 17 Sep 2026, 8:29 AM ET)",
         "https://www.securityweek.com/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows/"),
        ("Cisco Security Advisory cisco-sa-ISE-ABP-VNSW7Tn5 (CVE-2026-76460)",
         "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5"),
        ("CISA &mdash; Known Exploited Vulnerabilities Catalog (returned no usable content on direct fetch this run)",
         "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
        ("CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog, 10 September 2026 (MikroTik RouterOS)",
         "https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
        ("SecurityWeek &mdash; Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation",
         "https://www.securityweek.com/root-rce-zero-day-in-cisco-secure-email-gateway-under-active-exploitation/"),
        ("SecurityWeek &mdash; Acronis Patches Exploited Vulnerability in cPanel Backup Plugin",
         "https://www.securityweek.com/acronis-patches-exploited-vulnerability-in-cpanel-backup-plugin/"),
        ("Black Kite &mdash; 2026 Manufacturing &amp; Distribution Ransomware Report",
         "https://blackkite.com/reports/2026-manufacturing-distribution"),
        ("Hudson Rock / infostealers.com &mdash; Revolut hackers used infostealers for elaborate social engineering",
         "https://www.infostealers.com/article/revolut-hackers-used-infostealers-for-elaborate-social-engineering/"),
    ]))
    o.append('<div class="disc">Severity scores, fixed versions and remediation deadlines are reproduced from '
             'vendor advisories and CISA material as read this run. Verify against your own vendor advisories '
             'before acting. This page is a news summary, not security guidance for your environment.</div>'
             '</footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ WALL STREET
def build_ws():
    css = base_css("#caa64a", "#e8c766", "#0b0a08", "#151310", "#2a2620") + """
.masthead h1,h3{font-family:Georgia,'Times New Roman',serif;letter-spacing:-.3px}
h3{font-size:20px}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);
  display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up)}
.tickers{display:grid;gap:11px;margin-bottom:6px}
@media(min-width:700px){.tickers{grid-template-columns:repeat(3,1fr)}}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""
    o = [head("The Closing Bell &mdash; Daily Briefings", css)]
    o.append(mast("The Closing Bell",
                  "Your daily markets briefing &mdash; indices, movers, rates &amp; what&rsquo;s next"))
    o.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % TL_WS)
    o.append(FRESH)
    o.append(nav("ws"))

    # BLOCK A
    o.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
             '<script src="%s" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
             '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
             '{"proName":"NASDAQ:MU","title":"Micron"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},'
             '{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"NYSE:GS","title":"Goldman Sachs"},'
             '{"proName":"NYSE:CRM","title":"Salesforce"},{"proName":"TVC:USOIL","title":"WTI Crude"},'
             '{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,'
             '"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>'
             % (TV % "ticker-tape"))

    # BLOCK B
    o.append('<h2 class="sec">Live index quotes &mdash; updates in real time</h2>')
    o.append('<div class="tickers">')
    for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"]:
        o.append('<div class="ticker"><script src="%s" async>{"symbol":"%s","width":"100%%",'
                 '"colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'
                 % (TV % "single-quote", sym))
    o.append('</div>')
    o.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the '
             'latest edition; official closes are in the Weekly Scorecard.</div>')

    # THE LEAD
    o.append('<h2 class="sec">The lead</h2>')
    o.append('<div class="panel"><h3>A second day of gains after the Fed hike, chips out front &mdash; but no '
             'official Thursday close had been published by 4:12 PM ET</h3>'
             '<p>Equities carried Wednesday&rsquo;s rebound through the Thursday session. On Trading '
             'Economics&rsquo; Sep/17 board, <b>re-read at roughly 4:12 PM ET &mdash; after the bell</b> &mdash; '
             'the <b>S&amp;P 500 stood at 7,639.02, up 87.21 points or +1.15%</b>; the <b>Nasdaq 100 at '
             '29,426.02, up 480.96 or +1.66%</b>; and the <b>Dow at 51,817.26, up 355.36 or +0.69%</b>. Breadth '
             'reached down the cap scale: <b>Russell 2000 +0.65%</b> (2,879.64) and <b>S&amp;P MidCap 400 '
             '+0.76%</b> (3,668.26). All three headline figures reconcile <i>exactly</i> against Wednesday&rsquo;s '
             'settles &mdash; 7,551.81 + 87.21, 51,461.90 + 355.36 and 28,945.06 + 480.96 &mdash; and every '
             'percentage was recomputed from those levels rather than taken on trust.</p>'
             '<p>The driver was a rotation back into growth and AI names. A closely watched gauge of chipmakers '
             'climbed about <b>3%</b>, and falling oil prices lent support to the argument that inflation can stay '
             'contained. Treasury yields fell &mdash; Trading Economics headlined it '
             '&ldquo;Treasury Yields Fall After Fed&rdquo; &mdash; with the <b>10-year easing to 4.94%</b>, about '
             'eight basis points lower on the day; Bloomberg reported yields retreating from their highest '
             'level since 2007, <b>snapping an eight-day rising streak</b>. All of it came one day after the '
             '<b>Federal Reserve raised its benchmark rate 25 basis points to 3.75%&ndash;4%</b>, its first '
             'increase since 2023.</p>'
             '<p class="note"><b>Freshness, handled honestly.</b> This edition was built roughly ten minutes '
             'after the closing bell. <b>No index-level source had published official Thursday closing figures at '
             'press time</b>, so none is published or implied here: the figures above are Trading '
             'Economics&rsquo; CFD board for Sep/17, read <i>after</i> the bell and identical to this '
             'site&rsquo;s 3:50 PM ET read, which is consistent with a settled session but is not the same thing '
             'as an official settle. For the settled session use the live widgets above. The <b>Weekly '
             'Scorecard below carries Wednesday&rsquo;s official settles only</b>, and says why Thursday is '
             'absent.</p>'
             '<p class="note"><b>Refused this run.</b> (1) A search-level figure of <b>7,596 / +0.59%</b> for '
             'the S&amp;P 500 is internally consistent but describes an <i>earlier hour</i> and is superseded '
             '&mdash; named, not silently dropped. (2) A summary asserting the market &ldquo;faced downward '
             'pressure&rdquo; today is contradicted by every verified read and by Trading Economics&rsquo; own '
             'headline, &ldquo;US Stocks Rebound Sharply&rdquo;; not one figure from it is used. (3) A claim that '
             'the 10-year hit <b>5.01%</b> today conflicts with the 4.94% read and is dropped. (4) A barchart '
             'wrap describing a Thursday with the S&amp;P +0.40%, the Dow +0.62% and <b>Micron up more than '
             '14%</b> on strong sales and profit forecasts plainly belongs to a different session and is not used. (5) The <b>VIX</b> row '
             'renders <b>15.49 | &minus;2.22 | &minus;2.22%</b> &mdash; a point change and a percentage cannot '
             'both describe one number &mdash; refused for a <b>fourth consecutive edition</b>. (6) <b>No Nasdaq '
             'Composite percentage is published</b> for a fourth straight edition: every circulating figure was '
             'an ETF proxy. (7) Trading Economics&rsquo; own page description reads &ldquo;rose to <b>7635</b> '
             'points, gaining <b>1.10%</b>&rdquo; and its daily field reads <b>7635.02</b> against Wednesday&rsquo;s '
             '7551.81, while its live table shows 7,639.02 / +1.15%; the table is used and the divergence is '
             'printed.</p></div>')

    # MOVERS
    o.append('<h2 class="sec">Movers &amp; drivers</h2>')
    o.append('<div class="cards two">')
    movers = [
        ("Semiconductors &middot; NASDAQ:MU", "Micron Technology &mdash; $977.36, +$50.81, +5.48%",
         '<span class="tag a">biggest single-name move</span>',
         "The largest move on Trading Economics&rsquo; mega-cap board and the day&rsquo;s Chart of the Day. "
         "Market capitalisation $1.18T. The percentage was recomputed from last-minus-change."),
        ("Semiconductors &middot; NASDAQ:AVGO", "Broadcom &mdash; $348.66, +$9.15, +2.70%",
         '<span class="tag a">chips</span>',
         "Part of the chipmaker gauge that climbed roughly 3% on the day. Reconciled from last-minus-change."),
        ("Semiconductors &middot; NASDAQ:NVDA", "NVIDIA &mdash; $219.66, +$5.76, +2.69%",
         '<span class="tag a">chips</span>',
         "Also a top Dow gainer in Trading Economics&rsquo; opening snapshot at +2.09%; market capitalisation "
         "$5.07T. Open-snapshot and full-session figures are labelled separately here."),
        ("Banks &middot; NYSE:GS", "Goldman Sachs &mdash; $955.80, +$17.82, +1.90%",
         '<span class="tag m">reversal completed</span>',
         "Goldman opened lower at &minus;0.80% and finished the reversal; a prior edition of this page caught it "
         "mid-turn at +1.77%. Nothing here is averaged across the two reads."),
        ("Software &middot; NYSE:CRM", "Salesforce &mdash; &minus;4.30% in the opening snapshot",
         '<span class="tag c">Dow&rsquo;s worst drag</span>',
         "The worst drag in Trading Economics&rsquo; Dow open note, one day after the Salesforce global outage "
         "&mdash; cross-linked to The Cyber Wire. <b>This is an opening-snapshot figure and is labelled as such;</b> "
         "no full-session percentage for CRM was verified this run."),
        ("Index breadth", "Dow open: +248 points / +0.48%",
         '<span class="tag m">open snapshot</span>',
         "Trading Economics&rsquo; opening note lists gainers Caterpillar +2.60%, NVIDIA +2.09% and Amazon "
         "+2.02%, against losers Salesforce &minus;4.30%, Goldman Sachs &minus;0.80% and Walmart &minus;0.47%. "
         "All six are opening-snapshot figures."),
    ]
    for k, h, tags, body in movers:
        o.append('<div class="card"><div class="k">%s</div><h4>%s</h4>%s<p>%s</p></div>' % (k, h, tags, body))
    o.append('</div>')
    o.append('<div class="note"><b>Zero &ldquo;New&rdquo; tags in this section, and that is deliberate.</b> '
             'Every mover name above already appears in this site&rsquo;s archived snapshots; a new number '
             'attached to an old name is not a new item.</div>')

    # BLOCK E
    o.append('<h2 class="sec">Chart of the day &mdash; Micron Technology</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"symbol":"NASDAQ:MU","width":"100%%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>'
             % (TV % "mini-symbol-overview"))
    o.append('<div class="note">Micron was the single largest move on the mega-cap board read this run: '
             '<b>$977.36, +$50.81, +5.48%</b>.</div>')

    # BLOCK D
    o.append('<h2 class="sec">Sector heat &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
             '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
             '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%%","height":420}</script></div>'
             % (TV % "stock-heatmap"))
    o.append('<div class="note">Technology carried the session: a closely watched gauge of chipmakers climbed '
             'about <b>3%</b>. <b>No breadth or VIX figure is published</b> &mdash; the VIX row read this run is '
             'internally inconsistent, and no advance/decline count was sourced.</div>')

    # BLOCK F
    o.append('<h2 class="sec">The calendar &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"colorTheme":"dark","isTransparent":true,"width":"100%%","height":420,"locale":"en",'
             '"importanceFilter":"0,1","countryFilter":"us"}</script></div>' % (TV % "events"))

    # BLOCK C
    o.append('<h2 class="sec">Live market headlines &mdash; updates in real time</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%%","height":420,"locale":"en"}</script></div>'
             % (TV % "timeline"))

    # AFTER HOURS
    o.append('<h2 class="sec">After-hours movers</h2>')
    o.append('<div class="panel"><p style="margin:0"><b>Nothing is published in this section, because nothing was '
             'sourced.</b> The session closed at 4:00 PM ET and this edition was built roughly twelve minutes '
             'later. Not one specific after-hours move &mdash; no ticker, no percentage, no direction &mdash; '
             'appeared in any source read this run; the after-hours trackers surfaced in search were showing '
             'prior sessions rather than tonight&rsquo;s tape.</p>'
             '<p class="note" style="margin-bottom:0">An empty section is the correct output here. Inventing an '
             'after-hours mover to fill the block would be the one failure this page cannot recover from. Use the '
             'live ticker at the top of the page for tonight&rsquo;s extended-hours quotes.</p></div>')

    # WEEKLY SCORECARD
    o.append('<h2 class="sec">Weekly scorecard</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Index</th><th>Wednesday 16 Sep close</th>'
             '<th>Change</th><th>%</th></tr></thead><tbody>'
             '<tr><td>S&amp;P 500</td><td>7,551.81</td><td class="down">&mdash;</td>'
             '<td class="down">lower</td></tr>'
             '<tr><td>Dow Jones Industrial Average</td><td>51,461.90</td><td class="down">&minus;631.21</td>'
             '<td class="down">&minus;1.21%</td></tr>'
             '<tr><td>Nasdaq Composite</td><td>25,978.42</td><td class="down">&mdash;</td>'
             '<td class="down">&minus;0.01%</td></tr>'
             '<tr><td>Nasdaq 100</td><td>28,945.06</td><td>&mdash;</td>'
             '<td>not verified</td></tr>'
             '</tbody></table></div>')
    o.append('<div class="note"><b>Thursday is absent on purpose.</b> This table carries official settles only, '
             'and no source read this run had published Thursday&rsquo;s official closes &mdash; the bell rang '
             'about twelve minutes before press time. Wednesday&rsquo;s Dow figure (&minus;631.21 points, '
             '&minus;1.21%, to 51,461.90) and the Nasdaq Composite&rsquo;s &minus;0.01% to 25,978.42 are as '
             'reported after the Fed decision; the S&amp;P 500 and Nasdaq 100 levels are the settles against '
             'which Thursday&rsquo;s Trading Economics changes reconcile exactly. Where a points change was not '
             'verified this run, the cell reads an em dash rather than a computed number.</div>')

    # RATES
    o.append('<h2 class="sec">Rates, bonds &amp; commodities</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Instrument</th><th>Level</th><th>Change</th>'
             '<th>Note</th></tr></thead><tbody>')
    rates = [
        ("US 10-year Treasury yield", "4.94%", "about &minus;8 bp",
         "Trading Economics, Sep/17, read after the bell. Bloomberg reported yields retreating from their "
         "highest level since 2007 and snapping an eight-day rising streak."),
        ("US 2-year Treasury yield", "4.69%", "&minus;5.6 bp",
         "Carried from this site&rsquo;s 3:50 PM ET curve read; <b>not re-fetched</b> this run."),
        ("US 5-year Treasury yield", "4.80%", "&minus;8.9 bp",
         "Carried from the same 3:50 PM ET read; not re-fetched."),
        ("US 30-year Treasury yield", "5.29%", "&minus;7.6 bp",
         "Carried from the same 3:50 PM ET read; not re-fetched."),
        ("Fed funds target", "4.00%", "+25 bp on 16 Sep",
         "Trading Economics&rsquo; indicator table: 4.00% for Sep 2026 against a previous 3.75%. First increase "
         "since 2023."),
        ("WTI crude", "$101.44", "&minus;0.96%", "Trading Economics commodities board, Sep/17, read this run."),
        ("Brent crude", "$104.23", "&minus;1.51%", "Same board, same read."),
        ("Natural gas", "$2.8836", "&minus;0.26%", "Same board, same read."),
        ("Gold", "$4,354.47", "+2.13%", "Same board, same read."),
        ("Silver", "$65.41", "+3.43%", "Same board, same read."),
        ("Bitcoin", "$76,499", "+0.46%", "Same board, same read."),
        ("VIX", "Not published", "&mdash;",
         "The row read <b>15.49 | &minus;2.22 | &minus;2.22%</b>. A point change and a percentage cannot both "
         "describe the same number, so the figure is refused for a fourth consecutive edition."),
    ]
    for i, l, c, n in rates:
        cls = ' class="down"' if c.strip().startswith(("&minus;", "about &minus;")) else (
            ' class="up"' if c.strip().startswith("+") else "")
        o.append('<tr><td>%s</td><td>%s</td><td%s>%s</td><td class="note">%s</td></tr>' % (i, l, cls, c, n))
    o.append('</tbody></table></div>')
    o.append('<div class="note">Trading Economics&rsquo; change column is unsigned; direction is taken from the '
             'percentage and that inference is stated rather than hidden.</div>')

    # ON THE RADAR
    o.append('<h2 class="sec">On the radar</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b>Thursday&rsquo;s official closes.</b> The first thing the next edition should settle: an '
             'index-level confirmation of where the S&amp;P 500, Dow and Nasdaq Composite actually finished. '
             'Nothing on this page asserts one.</li>')
    o.append('<li><b>Whether the Fed signalled more to come.</b> Two search-level summaries read this run say '
             'the Fed paired the hike with a signal of <b>further tightening</b> &mdash; one of them specifically '
             'another increase later this year. Both arrived inside the same summary this page refused for '
             'asserting a falling market, so the <b>25 basis point hike to 3.75%&ndash;4% is reported and the '
             'characterisation of its tone is not</b>. Settling that is next edition&rsquo;s job.</li>')
    o.append('<li><b>Whether the chip bid holds.</b> The gauge of chipmakers climbing about 3% carried a session '
             'in which the Dow managed only +0.69%. That is a narrow engine, and it is the thing to watch '
             'Friday.</li>')
    o.append('<li><b>The 10-year&rsquo;s streak.</b> Eight consecutive sessions of rising yields ended today. '
             'Whether 4.94% is a pause or a turn is the question the bond market answers next.</li>')
    o.append('</ul></div>')

    o.append(sources([
        ("Trading Economics &mdash; United States Stock Market Index (US500 / US30 / US100 / US2000 / US400, "
         "mega-cap board, commodities, bond yields; Sep/17, fetched in full ~4:12 PM ET)",
         "https://tradingeconomics.com/united-states/stock-market"),
        ("Trading Economics &mdash; Dow Jones Index Opens 0.48% Higher (17 Sep 2026)",
         "https://tradingeconomics.com/indu:ind/news/584646"),
        ("Trading Economics &mdash; US Stocks Rebound Sharply (17 Sep 2026)",
         "https://tradingeconomics.com/united-states/stock-market/news/584641"),
        ("Trading Economics &mdash; Treasury Yields Fall After Fed",
         "https://tradingeconomics.com/united-states/government-bond-yield"),
        ("Bloomberg &mdash; Stock Market Today: Dow, S&amp;P Live Updates for September 17 "
         "(returned no body text on direct fetch; used at search-summary level only)",
         "https://www.bloomberg.com/news/articles/2026-09-16/stock-market-today-dow-s-p-live-updates"),
        ("TheStreet &mdash; Stock Market Today (Sept. 16, 2026): Dow, S&amp;P 500 plummet after Fed hikes "
         "(Wednesday settles)",
         "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-16-2026"),
        ("CNBC &mdash; Stock market today: live updates",
         "https://www.cnbc.com/2026/09/15/stock-market-today-live-updates.html"),
    ]))
    o.append('<div class="disc">Information only &mdash; this page is not investment advice. Index and '
             'commodity figures are reproduced from the sources named above as read at the stated time; live '
             'widgets are supplied by TradingView and some feeds are delayed by roughly fifteen minutes. No '
             'official Thursday closing figures are asserted on this page.</div></footer>')
    o.append(FOOT)
    return "".join(o)


# ================================================================ MMA
def build_mma():
    css = base_css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020") + """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:11px;padding:12px 16px;margin-bottom:18px;display:flex;flex-wrap:wrap;
  align-items:baseline;gap:10px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent2)}
.cdn .v{font-family:var(--mono);font-size:17px;color:var(--text)}
.cdn .w{font-size:13.5px;color:var(--muted)}
.evd{font-family:var(--mono);font-size:11px;letter-spacing:.11em;text-transform:uppercase;
  color:#e8c766;margin-bottom:7px}
.topstory{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:17px 20px}
"""
    o = [head("The Octagon &mdash; Daily Briefings", css)]
    o.append(mast("The Octagon",
                  "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    o.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % TL_MMA)
    o.append(FRESH)
    o.append(nav("mma"))

    # countdown
    o.append('<div class="cdn"><span class="k">Next card</span>'
             '<span class="v" id="ufccdn">&nbsp;</span>'
             '<span class="w">UFC 331: Van vs. Pantoja 2 &middot; Crypto.com Arena, Los Angeles &middot; '
             'Saturday 19 September, main card 9 PM ET / 6 PM PT on Paramount+</span></div>')

    # TOP STORY
    o.append('<h2 class="sec">Top story</h2>')
    o.append('<div class="topstory"><h3>No, Joshua Van has not pulled out of UFC 331 &mdash; the report saying so '
             'traces to one automated aggregator</h3>'
             '<p>A story published this morning claiming that <b>Joshua Van withdrew from Saturday&rsquo;s '
             'flyweight title rematch late in fight week</b>, leaving Alexandre Pantoja without an opponent, is '
             '<b>refused on this page</b>. It appeared on boxingnews.com, bylined to &ldquo;MMA News Staff&rdquo;, '
             'timestamped 17 September, and it cites exactly one source: an ESPN preview headlined '
             '&ldquo;Pantoja sees opportunity in disaster.&rdquo;</p>'
             '<p>Four things rule it out. <b>First</b>, every other source read this run has the fight on: '
             'Wikipedia&rsquo;s UFC 331 entry, fetched today, still lists the title rematch as scheduled to '
             'headline; CBS Sports published main-card betting picks today with <b>Van&rsquo;s moneyline at '
             '&minus;135</b>; DraftKings Network ran a ceremonial weigh-in preview today; and Fight Matrix posted '
             'a Van-versus-Pantoja breakdown today. <b>Second</b>, the &ldquo;disaster&rdquo; in that ESPN '
             'headline is almost certainly the fluke injury that ended the first fight &mdash; CBS describes '
             'Pantoja as having &ldquo;lost the belt when he suffered a fluke injury shortly after the opening '
             'bell,&rdquo; which is exactly the opportunity-in-disaster framing. <b>Third</b>, the article calls '
             'Pantoja &ldquo;the Brazilian champion&rdquo; in the same breath as describing him as the man left '
             'without an opponent &mdash; Pantoja is the <i>former</i> champion; Van holds the belt. '
             '<b>Fourth</b>, the page lists <b>Anthony Joshua</b> among the &ldquo;related fighters in this '
             'story,&rdquo; which is what a keyword-matching bot does with the name Joshua.</p>'
             '<p>So the briefing for Saturday night is the ordinary one: <b>UFC 331: Van vs. Pantoja 2</b> goes '
             'ahead at the Crypto.com Arena, the UFC&rsquo;s first Los Angeles card since UFC 227 in August 2018 '
             'and its sixth visit to the city. Van won the belt at <b>UFC 323 in December 2025</b> by technical '
             'knockout <b>26 seconds into round one</b>, as a result of an arm injury Pantoja sustained &mdash; a '
             'title change nobody involved treats as settled business.</p>'
             '<p class="note"><b>What this page does not claim.</b> That boxingnews.com fabricated the story '
             'deliberately, or that ESPN reported a withdrawal &mdash; the ESPN article itself returned no body '
             'text on direct fetch this run, so it is judged only on its headline and on what every other source '
             'says. If Van does withdraw before Saturday, this page will be wrong and the next edition will say '
             'so.</p></div>')

    # UPCOMING
    o.append('<h2 class="sec">Fight week &mdash; upcoming cards</h2>')
    o.append('<div class="cards two">')
    cards = [
        ("Sat 19 Sep 2026 &middot; Crypto.com Arena, Los Angeles",
         "UFC 331: Van vs. Pantoja 2",
         "Joshua Van defends the flyweight title against the man he took it from. Co-main: <b>Arman Tsarukyan vs. "
         "Maur&iacute;cio Ruffy over five rounds</b> &mdash; Tsarukyan&rsquo;s first bout in ten months, and a "
         "replacement booking after Charles Oliveira withdrew in early August. Also on the card: Marlon Vera vs. "
         "Charles Jourdain, Renato Moicano vs. Brian Ortega, Patr&iacute;cio Pitbull vs. Dooho Choi, and Gable "
         "Steveson vs. Sean Sharaf. Early prelims 5 PM ET, prelims 7 PM ET, main card 9 PM ET on Paramount+.",
         "<b>Odds</b> (CBS Sports, via DraftKings, 17 Sep): <b>Van &minus;135</b> on the moneyline. A Yahoo "
         "fight-week read had it <b>Van &minus;107 / Pantoja &minus;113</b>, a true pick&rsquo;em; a Covers read "
         "carried by this site had <b>Van &minus;130 / Pantoja +110</b>; opening was <b>Van +170 / Pantoja "
         "&minus;200</b>. Every line is attributed to its book and its moment; nothing is averaged."),
        ("Sat 3 Oct 2026 &middot; Delta Center, Salt Lake City",
         "UFC 332: Silva vs. Wang",
         "<b>Nat&aacute;lia Silva vs. Wang Cong for the VACANT women&rsquo;s flyweight title</b>, after Valentina "
         "Shevchenko vacated. Silva enters on a <b>14-fight win streak</b>; Wang has won four straight in the "
         "Octagon, most recently beating Tracy Cortez at UFC 329 in July. The promotion&rsquo;s fifth visit to "
         "Salt Lake City and first since UFC 307 in October 2024.",
         "<b>First numbered-event main card to air on CBS</b>, simulcast on Paramount+, starting 8 PM ET / "
         "5 PM PT. No odds for this card were sourced this run, so none are printed."),
        ("Sat 24 Oct 2026 &middot; Etihad Arena, Abu Dhabi",
         "UFC 333: Volkanovski vs. Evloev",
         "<b>Two title fights.</b> Alexander Volkanovski defends the featherweight belt against undefeated "
         "contender Movsar Evloev; in the co-main, <b>Petr Yan vs. Merab Dvalishvili 3</b> for the bantamweight "
         "title. The five-fight main card also carries Lone&rsquo;er Kavanagh vs. Ramazan Temirov, Alexander "
         "Volkov vs. Rizvan Kuniev and Arnold Allen vs. Aaron Pico.",
         "Prelims 10 AM ET, main card 2 PM ET. Prelim bouts confirmed include Dominick Reyes vs. Azamat "
         "Murzakanov, Abus Magomedov vs. Cam Rowston, Nikita Krylov vs. Abdul Rakhman Yakhyaev and Grant Dawson "
         "vs. Nurullo Aliev. No odds sourced this run."),
        ("Thu 24 Sep 2026 &middot; grappling",
         "UFC BJJ 11: Musumeci vs. Mitchell",
         "The promotion&rsquo;s submission-grappling series returns. <span class=\"tag new\">New</span>",
         "Listed on boxingnews.com&rsquo;s upcoming-events rail this run at <b>date and title level only</b>. "
         "Given that the same outlet is the source of the withdrawal claim refused above, nothing beyond the "
         "date and the billing is asserted here."),
    ]
    for d, h, body, odds in cards:
        o.append('<div class="card"><div class="evd">%s</div><h4>%s</h4><p>%s</p>'
                 '<p class="note">%s</p></div>' % (d, h, body, odds))
    o.append('</div>')

    # LAST EVENT
    o.append('<h2 class="sec">Last event &mdash; results</h2>')
    o.append('<div class="note" style="margin-bottom:11px"><b>Noche UFC: Silva vs. Delgado</b> (also billed as '
             'UFC Fight Night 288 and Noche UFC 4) &mdash; Saturday 12 September 2026, Desert Diamond Arena, '
             'Glendale, Arizona.</div>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Result</th><th>Bout</th><th>Method</th>'
             '</tr></thead><tbody>'
             '<tr><td class="win">Jean Silva</td><td>def. Jose Miguel Delgado</td>'
             '<td>Submission (one-armed rear-naked choke), round 3, 2:57 &mdash; after stunning Delgado with a '
             'punch. Delgado had dropped Silva in round one.</td></tr>'
             '<tr><td class="win">Sean King III</td><td>def. Jessie Rosas</td>'
             '<td>Finish in round one</td></tr>'
             '<tr><td class="nc">No winner asserted</td><td>Tommy McMillen vs. Marwan Rahiki</td>'
             '<td>Three-round slugfest &mdash; Fight of the Night. <span class="note">The winner of this bout was '
             'not stated in any source read this run, so none is claimed and the result cell is deliberately '
             'blank; only the Fight of the Night award and McMillen&rsquo;s bonus are asserted.</span></td></tr>'
             '<tr><td class="win">Brandon Moreno</td><td>&mdash;</td>'
             '<td>Won. <span class="note">Opponent and method were not verified this run and are not '
             'printed.</span></td></tr>'
             '<tr><td class="win">Tommy Gantt</td><td>&mdash;</td><td>Won by finish (bonus-verified)</td></tr>'
             '<tr><td class="win">Yousri Belgaroui</td><td>&mdash;</td><td>Won by finish (bonus-verified)</td></tr>'
             '</tbody></table></div>')
    o.append('<div class="panel" style="margin-top:13px"><div class="k" style="font-family:var(--mono);'
             'font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--accent2);'
             'margin-bottom:7px">Performance bonuses</div>'
             '<p style="margin-bottom:8px">Four fighters took an extra <b>$100,000</b> and two took '
             '<b>$25,000</b> each for finishes.</p>'
             '<ul class="b"><li><b>Performance of the Night &mdash; Jean Silva</b>, $100,000, for the third-round '
             'submission. Silva now stands <b>7&ndash;1 inside the Octagon with six finishes</b>.</li>'
             '<li><b>Performance of the Night &mdash; Sean King III</b>, $100,000, for a first-round finish of '
             'Jessie Rosas.</li>'
             '<li><b>Fight of the Night &mdash; Tommy McMillen vs. Marwan Rahiki</b>. McMillen collected his '
             '<b>third $100,000 bonus in three UFC fights</b>.</li>'
             '<li><b>$25,000 finish bonuses &mdash; Tommy Gantt and Yousri Belgaroui.</b></li></ul>'
             '<p class="note" style="margin-bottom:0">A source read this run says four fighters received $100,000; '
             'three $100,000 recipients are named above and the fourth is not, because no source read this run '
             'named them. The natural inference is that Fight of the Night pays both men, which would make '
             '<b>Marwan Rahiki</b> the fourth &mdash; but that is an inference, no source read this run stated '
             'it, and it is therefore not printed as fact. An earlier read of this site&rsquo;s ledger '
             'timed the King finish at <b>0:36</b> and refused a competing <b>0:33</b>; this run confirms only '
             '&ldquo;round one&rdquo;, so no seconds figure is asserted.</p></div>')

    # PROSPECT WATCH
    o.append('<h2 class="sec">Prospect watch</h2>')
    o.append('<div class="cards two">')
    pros = [
        ("Heavyweight", "Gable Steveson",
         '<span class="tag a">prospect</span><span class="tag m">&minus;2100</span>',
         "The Olympic gold medallist gets his first main-card slot at UFC 331 against <b>Sean Sharaf</b>, and CBS "
         "Sports could not find a line inside its own betting criteria: Steveson is a <b>&minus;2100</b> "
         "favourite, the fight ending inside 1.5 rounds is <b>&minus;620</b>, and he is <b>&minus;275</b> to win "
         "by knockout. CBS&rsquo;s read: he &ldquo;should win with relative ease as he continues to receive soft "
         "touches while he develops as a fighter.&rdquo;"),
        ("Featherweight", "Patr&iacute;cio Pitbull",
         '<span class="tag m">&ldquo;a dud&rdquo;</span>',
         "The former Bellator champion faces <b>Dooho Choi</b> at UFC 331. CBS Sports calls his UFC tenure so far "
         "&ldquo;a dud&rdquo; and picks Choi, noting the most likely single outcome on the board is <b>Choi by "
         "knockout (+130)</b>: Pitbull is &ldquo;still a wildly talented fighter with tons of skill and fight "
         "knowledge, but his body isn&rsquo;t able to pull off the things he wants to do.&rdquo;"),
        ("Lightweight", "Arman Tsarukyan",
         '<span class="tag a">co-main</span>',
         "Returns after <b>ten months</b> out, against Maur&iacute;cio Ruffy over five rounds. He beat Charles "
         "Oliveira by split decision at UFC 300 in April 2024; the Oliveira rematch that was to headline this "
         "card was scrapped on 5 August, days after the death of Oliveira&rsquo;s longtime teammate Allan "
         "Nascimento, with <b>no official reason given</b> for the withdrawal. CBS&rsquo;s pick on the bout is "
         "<b>over 3.5 rounds (+154)</b>."),
        ("Flyweight", "Joshua Van",
         '<span class="tag a">champion</span>',
         "He has held the belt since UFC 323 and has not yet had a competitive round in "
         "defence of it &mdash; the first Pantoja fight lasted 26 seconds. Saturday is the first real test of the "
         "title reign."),
    ]
    for k, h, tags, body in pros:
        o.append('<div class="card"><div class="k">%s</div><h4>%s</h4>%s<p>%s</p></div>' % (k, h, tags, body))
    o.append('</div>')

    # AROUND THE SPORT
    o.append('<h2 class="sec">Around the sport</h2>')
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b>Harrison vs. Nunes is postponed, not cancelled &mdash; and not on Saturday.</b> A women&rsquo;s '
             'bantamweight title fight between reigning champion <b>Kayla Harrison</b> and former two-division '
             'champion <b>Amanda Nunes</b> was reportedly planned for UFC 331 but is <b>postponed for undisclosed '
             'reasons</b>, per Wikipedia&rsquo;s UFC 331 entry fetched this run. It was originally booked for '
             'UFC 324 in January 2026 before Harrison withdrew with herniated discs in her neck requiring '
             'surgery. <b>Harrison still has zero title defences</b> and this page does not credit her with '
             'one.</li>')
    o.append('<li><b>The Oliveira BMF thread ended quietly.</b> Tsarukyan vs. Oliveira 2 was reported for this '
             'card, initially with Oliveira&rsquo;s symbolic BMF title on the line and later changed to a '
             'non-title contest, before the booking collapsed on 5 August. Reports at the time said Tsarukyan '
             'would not be allowed to challenge for the BMF belt.</li>')
    o.append('<li><b>Blaydes vs. Cortes-Acosta moved off this card.</b> The heavyweight bout was announced for '
             'UFC 331 but actually took place a week earlier, at UFC Fight Night: Silva vs. Delgado.</li>')
    o.append('<li><b>Vera vs. Jourdain survived a venue shuffle.</b> The bantamweight bout was first set for '
             'UFC Fight Night: du Plessis vs. Usman in July, then moved here for undisclosed reasons. The card '
             'itself was once floated for the Intuit Dome in Inglewood or as part of Noche UFC 4 in Glendale '
             'before landing at Crypto.com Arena.</li>')
    o.append('<li><b>Two headline-level items, carried with their source named.</b> boxingnews.com&rsquo;s '
             'trending rail this run lists <b>Mokaev on a UFC offer &mdash; &ldquo;they wasted two years of my '
             'life&rdquo;</b> and <b>Topuria telling Gaethje and his manager the f-word still stands</b>. Given '
             'that outlet is the source of the withdrawal claim refused at the top of this page, both are listed '
             'as headlines only and neither is treated as established.</li>')
    o.append('</ul></div>')

    # RANKINGS & BUSINESS
    o.append('<h2 class="sec">Rankings &amp; business</h2>')
    o.append('<div class="panel">'
             '<p><b>Rankings movement.</b> Nothing verified this run. No official UFC rankings update was read, '
             'so no rise or fall is asserted for any fighter. One pound-for-pound top five surfaced on '
             'boxingnews.com this run &mdash; and it is <b>internally broken</b>, numbering its entries '
             '1, 2, 3, 5, 6 with no fourth place, which is reason enough not to publish it.</p>'
             '<p><b>Business &amp; broadcast.</b> The confirmed items are distribution, not dollars. UFC 331 '
             'airs on <b>Paramount+</b> in the United States. <b>UFC 332 on 3 October will be the first numbered '
             'event whose main card airs on CBS</b>, simulcast on Paramount+ at 8 PM ET. UFC 333 runs on Abu '
             'Dhabi time, with prelims at 10 AM ET and the main card at 2 PM ET. '
             '<b>No viewership, gate or TKO Group figure is published</b> &mdash; none was sourced this '
             'run.</p>'
             '<p class="note" style="margin-bottom:0">The only dollar figures on this page are the UFC&rsquo;s '
             'own bonus payments and sportsbook prices, each attributed to the source that stated it.</p></div>')

    # CHAMPIONS
    o.append('<h2 class="sec">Champions board</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Division</th><th>Champion</th><th>Won</th>'
             '<th>Notes</th></tr></thead><tbody>')
    champs = [
        ("Heavyweight", "VACANT", "&mdash;",
         "Tom Aspinall <b>vacated</b> on 14 September 2026 over unresolved eye complications; he is not retiring "
         "and intends to return once cleared. <b>Interim champion: Ciryl Gane</b> (KO2 Alex Pereira, Freedom 250, "
         "14 Jun 2026)."),
        ("Light Heavyweight", "Carlos Ulberg", "UFC 327, 11 Apr 2026",
         "KO1 over Ji&#345;&iacute; Proch&aacute;zka for the vacant belt; ACL surgery afterwards."),
        ("Middleweight", "Sean Strickland", "UFC 328, 9 May 2026",
         "Split-decision upset of Khamzat Chimaev; two-time champion."),
        ("Welterweight", "Islam Makhachev", "UFC 322, 15 Nov 2025",
         "Two-division champion (vacated lightweight). <b>1 defence</b> &mdash; UD over Ian Machado Garry, "
         "UFC 330, 15 Aug 2026, a record 17th straight Octagon win."),
        ("Lightweight", "Justin Gaethje", "Freedom 250, 14 Jun 2026", "TKO4 over Ilia Topuria."),
        ("Featherweight", "Alexander Volkanovski", "UFC 314, 12 Apr 2025",
         "<b>Defends at UFC 333</b> on 24 October against Movsar Evloev. Reclaimed the belt Topuria vacated and "
         "defended it against Diego Lopes at UFC 325."),
        ("Bantamweight", "Petr Yan", "UFC 323, 6 Dec 2025",
         "UD over Merab Dvalishvili. <b>Defends at UFC 333</b> in the trilogy bout against Dvalishvili."),
        ("Flyweight", "Joshua Van", "UFC 323, 6 Dec 2025",
         "TKO1 over Alexandre Pantoja (26 seconds, Pantoja arm injury). <b>1 defence</b> &mdash; TKO5 Tatsuro "
         "Taira, UFC 328. <b>Defends Saturday at UFC 331</b> in the Pantoja rematch."),
        ("Women&rsquo;s Flyweight", "VACANT", "&mdash;",
         "Valentina Shevchenko <b>vacated</b>; injured and sidelined roughly a year, and guaranteed a title shot "
         "when cleared. <b>Nat&aacute;lia Silva vs. Wang Cong contest the vacant belt at UFC 332</b> on "
         "3 October."),
        ("Women&rsquo;s Bantamweight", "Kayla Harrison", "UFC 316, 7 Jun 2025",
         "Sub2 Julianna Pe&ntilde;a. <b>0 defences</b> &mdash; the UFC 324 booking against Amanda Nunes was "
         "cancelled after neck surgery, and the bout reportedly planned for UFC 331 is postponed."),
        ("Women&rsquo;s Strawweight", "Mackenzie Dern", "UFC 321, 25 Oct 2025",
         "UD over Virna Jandiroba. <b>1 defence</b> &mdash; UD Gillian Robertson, UFC 330, 15 Aug 2026."),
        ("Interim Heavyweight", "Ciryl Gane", "Freedom 250, 14 Jun 2026",
         "KO2 over Alex Pereira in the interim-title bout."),
    ]
    for d, c, w, n in champs:
        cls = ' class="nc"' if c == "VACANT" else ''
        o.append('<tr><td>%s</td><td%s><b>%s</b></td><td>%s</td><td class="note">%s</td></tr>' % (d, cls, c, w, n))
    o.append('</tbody></table></div>')
    o.append('<div class="note"><b>ESPN&rsquo;s champions page was wrong again this run, and in a new way.</b> '
             'The page returned <b>no usable content on direct fetch</b>; its search-level rendering this run '
             'seated <b>Carlos Ulberg at HEAVYWEIGHT</b> &mdash; a division that has been <b>vacant</b> since '
             'Aspinall stepped down on 14 September &mdash; and <b>Sean Strickland at LIGHT HEAVYWEIGHT</b>, '
             'which is Ulberg&rsquo;s division. Both rows are <b>refused</b>. Its other rows agree with the board '
             'above: Makhachev at welterweight with one defence, Gaethje at lightweight, Volkanovski at '
             'featherweight, Yan at bantamweight. A source can be wrong about who holds a belt and wrong about '
             'which belt it is, in the same read &mdash; so every division above is re-derived from the most '
             'recent title-changing card rather than copied from any list.</div>')

    o.append(sources([
        ("Wikipedia &mdash; UFC 331 (fetched in full this run; card, venue, bout history)",
         "https://en.wikipedia.org/wiki/UFC_331"),
        ("CBS Sports &mdash; UFC 331 predictions, odds, best bets (fetched in full this run; DraftKings prices)",
         "https://www.cbssports.com/ufc/news/ufc-331-predictions-odds-best-bets-joshua-van-alexandre-pantoja-arman-tsarukyan/"),
        ("UFC.com &mdash; Crypto.com UFC 331: Van vs. Pantoja 2", "https://www.ufc.com/event/cryptocom-ufc-331"),
        ("UFC.com &mdash; UFC 332: Silva vs Wang", "https://www.ufc.com/event/ufc-332"),
        ("UFC.com &mdash; Undisputed Flyweight Title Up For Grabs At UFC 332 In Salt Lake City",
         "https://www.ufc.com/news/undisputed-flyweight-title-grabs-ufc-332-salt-lake-city"),
        ("UFC.com &mdash; Bonus Coverage: Noche UFC Glendale 2026",
         "https://www.ufc.com/news/bonus-coverage-noche-ufc-glendale-2026"),
        ("UFC.com &mdash; Main Card Results: Noche UFC", "https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado"),
        ("Wikipedia &mdash; UFC Fight Night: Silva vs. Delgado",
         "https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado"),
        ("CBS Sports &mdash; UFC 333 fight card: Volkanovski vs. Evloev, Yan vs. Dvalishvili 3",
         "https://www.cbssports.com/ufc/news/ufc-333-fight-card-alexander-volkanovski-vs-movsar-evloev-petr-yan-vs-merab-dvalishvili-3-abu-dhabi/"),
        ("Yahoo Sports &mdash; Noche UFC bonuses: Slick Silva sub snags six figures",
         "https://ca.sports.yahoo.com/news/noche-ufc-bonuses-slick-silva-013250148.html"),
        ("ESPN &mdash; Current and all-time UFC champions (returned no content on direct fetch; its "
         "search-level rendering seated two divisions wrongly this run and was refused)",
         "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
        ("boxingnews.com &mdash; Pantoja On Van&rsquo;s UFC 331 Withdrawal (the claim refused at the top of "
         "this page)", "https://boxingnews.com/news/pantoja-van-ufc-331-withdrawal"),
    ]))
    o.append('<div class="disc">Cards and bouts are subject to change. Betting lines move constantly and are '
             'reproduced only as stated by the book and at the moment named. Nothing here is betting '
             'advice.</div></footer>')
    o.append('</div>')
    o.append("""<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00').getTime();
function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-Date.now();
if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}
var dy=Math.floor(d/86400000),h=Math.floor(d%86400000/3600000),m=Math.floor(d%3600000/60000);
e.textContent=dy+'d '+h+'h '+m+'m';}u();setInterval(u,30000);})();</script>""")
    o.append(STAMP_JS + '</body></html>')
    return "".join(o)


for name, fn in [("index.html", build_index), ("cyber-briefing.html", build_cyber),
                 ("wallstreet-briefing.html", build_ws), ("mma-briefing.html", build_mma)]:
    html = fn()
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)
    print(name, len(html))
