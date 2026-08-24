import re, sys, io

D = "/sessions/vibrant-festive-ramanujan/mnt/outputs/"
fails = []

def rd(f):
    return io.open(D + f, encoding="utf-8").read()

def wr(f, s):
    io.open(D + f, "w", encoding="utf-8").write(s)

def rep(s, old, new, label):
    if old not in s:
        fails.append("MISSING: " + label)
        return s
    if s.count(old) != 1:
        fails.append("NOT UNIQUE (%d): %s" % (s.count(old), label))
        return s
    return s.replace(old, new)

# ============================ WALL STREET ============================
ws = rd("wallstreet-briefing.html")

WS_TLDR = ("With about twenty minutes of regular trading left the shape of the session has not changed "
           "&mdash; the Dow higher, the S&amp;P 500 and the Nasdaq Composite lower on semiconductor weakness "
           "&mdash; and no source fetched this run carried a reading newer than roughly 3&nbsp;p.m. ET, with "
           "The Motley Fool frozen for a fifth consecutive run and Yahoo Finance cached for a seventh; the "
           "one thing that did move is the Iran story, where Treasury named the shadow-fleet network it is "
           "sanctioning and Tehran&rsquo;s new security chief answered with a threat to the tanker lanes.")

ws = rep(ws,
    '<div class="tldr"><b>The Tape</b> <span>With under an hour of trading left the shape of the session is unchanged',
    '<div class="tldr"><b>The Tape</b> <span>' + WS_TLDR + '</span></div>\n<!--OLDTLDR<span>With under an hour of trading left the shape of the session is unchanged',
    "WS tldr open")
ws = rep(ws,
    'so no reading here is asserted as the current tape.</span></div>\n<div class="freshline"',
    'so no reading here is asserted as the current tape.-->\n<div class="freshline"',
    "WS tldr close")

# --- lead headline ---
ws = rep(ws,
    '<h2>Under an hour from the close, the tape holds its shape &mdash; and a sixth cached page nearly got through</h2>',
    '<h2>Twenty minutes from the bell, the tape is unchanged &mdash; and the freshest reading available is forty minutes old</h2>',
    "WS lead h2")

OLD_P1_START = '<p><b>As of roughly 3:05 p.m. ET.</b> With under an hour of regular trading left,'
i = ws.find(OLD_P1_START)
j = ws.find('</p>', i)
if i == -1 or j == -1:
    fails.append("MISSING: WS lead paragraph 1")
else:
    NEW_P1 = (
    '<p><b>As of roughly 3:38 p.m. ET.</b> With about twenty minutes of regular trading left, the session '
    'still looks as it has looked since the opening bell: blue chips up, semiconductors down, and nothing '
    'resolved until Nvidia reports on Wednesday. <b>Nothing newer than the previous edition surfaced this run.</b> '
    'The freshest index reading this desk could attribute remains an afternoon summary stamped around '
    '<b>3&nbsp;p.m. ET</b> at <b>S&amp;P 500 &minus;0.3%</b>, <b>Nasdaq Composite &minus;0.6%</b> and '
    '<b>Dow +0.2%</b>, re-confirmed in this run&rsquo;s searches and consistent with the read stamped roughly '
    '2:24&nbsp;p.m. ET carried at the previous edition (Dow +0.28%, S&amp;P 500 &minus;0.21%, Nasdaq Composite '
    '&minus;0.58%). The two agree on direction and disagree only on the width of the technology '
    'underperformance, so the range rather than a single figure is what is asserted here, and precise intraday '
    'index <em>levels</em> remain withheld from this editorial for a <b>twelfth consecutive run</b>. '
    'The official close was not available from any source fetched this run and is therefore not published '
    'here; it will be carried at the next edition. Every quote board checked was stale again. '
    '<b>The Motley Fool has now returned the identical print for a fifth consecutive run</b> &mdash; same '
    '11:37&nbsp;a.m. ET body stamp, same &ldquo;Stocks Mentioned&rdquo; module at S&amp;P 500 7,660.78 '
    '(&minus;0.18%), same footer strip, and an <code>article:modified_time</code> still frozen at '
    '12:15&nbsp;p.m. ET &mdash; which is the tell this desk wrote down earlier: once that timestamp stops '
    'advancing, the fresher-looking module freezes with the rest of the page. <b>Yahoo Finance served a '
    'cached page for the seventh time today</b>, and the countdown check caught it in its crudest form: the '
    'strip read &ldquo;U.S. markets open in 5h 6m&rdquo; and carried pre-open futures, dating it to roughly '
    '4:24&nbsp;a.m. ET against a live regular session. Nothing from it is published as current. '
    'The cause of the chip weakness is unchanged. 24/7&nbsp;Wall&nbsp;St. reported at 11:29&nbsp;a.m. ET that '
    'memory stocks slid on weekend reports Washington may permit Apple to source DRAM from China&rsquo;s '
    'ChangXin Memory Technologies (CXMT) and NAND flash from Yangtze Memory Technologies (YMTC), described as '
    'a possible diplomatic gesture ahead of President Xi Jinping&rsquo;s planned US visit, expected on or '
    'around September&nbsp;24. <b>No policy decision has been announced.</b> An afternoon summary fetched this '
    'run put <b>SanDisk down 10%</b> on those reports and <b>Monster Beverage up 2.3%</b> after record '
    'second-quarter 2026 results &mdash; the SanDisk figure is worse than the &minus;5.6% carried on the frozen '
    'Stock Market Watch board, and the gap between the two is itself a measure of how stale that board has '
    'become. Charles Schwab&rsquo;s early-session read had the technology sector off more than 2% and the '
    'semiconductor index down more than 3.75%, with <b>Nvidia &minus;2.3%</b>, <b>Taiwan Semiconductor '
    '&minus;3.7%</b>, <b>AMD &minus;3.33%</b> and <b>Broadcom &minus;1.3%</b>; those are early-session figures '
    'and are labelled as such. The session&rsquo;s biggest identified single-name decliner remains '
    '<b>Applied Optoelectronics</b>, down 11% in the morning on The Motley Fool&rsquo;s read and 13% on the '
    'Stock Market Watch board, after the company announced a $600&nbsp;million equity offering.</p>')
    ws = ws[:i] + NEW_P1 + ws[j + 4:]

# --- drop the New tag from the risk-gauges card ---
ws = rep(ws,
    '<div class="tags"><span class="tag up">VIX +3.64%</span><span class="tag down">RUT &lt;3,000</span><span class="tag new">New</span></div>',
    '<div class="tags"><span class="tag up">VIX +3.64%</span><span class="tag down">RUT &lt;3,000</span></div>',
    "WS drop new tag")
ws = rep(ws,
    '<p><b>New this edition.</b> The headline indexes have barely travelled all day,',
    '<p><b>Carried from the previous edition.</b> The headline indexes have barely travelled all day,',
    "WS risk-gauge card lede")

# --- insert the New card at the top of Movers ---
NEWCARD = '''<div class="card">
<div class="tags"><span class="tag">Iran</span><span class="tag down">Hormuz risk</span><span class="tag new">New</span></div>
<h3>The sanctions package now has names attached &mdash; and Tehran has answered with a threat to the tanker lanes</h3>
<p><b>New this edition.</b> NPR updated its account of the Treasury announcement at <b>1:24&nbsp;p.m. ET</b>, and it fills in the two things the 1&nbsp;p.m. press conference left abstract: who is being sanctioned, and what Iran intends to do about it. A Treasury Department statement says the targets include &ldquo;a network of brokers, companies, and shadow fleet vessels operating across the United Arab Emirates (UAE), Hong Kong, China, Singapore, Switzerland, Europe, and other regions&rdquo; used to move Iranian oil and channel the revenue to the Islamic Revolutionary Guard Corps-Qods Force and other parts of the regime. Treasury Secretary Scott Bessent framed the objective as severing &ldquo;every economic lifeline that sustains this tyrannical regime until Tehran stands alone,&rdquo; and warned that &ldquo;those who tether themselves to Tehran should expect to share in the isolation of a withering regime.&rdquo; The market-relevant half is the response. Iran&rsquo;s new security chief <b>Mohsen Rezaei</b> &mdash; a former commander of the Revolutionary Guard, now a military adviser to Supreme Leader Mojtaba Khamenei &mdash; said on state television over the weekend that Iran would retaliate in a &ldquo;seismic manner,&rdquo; told Gulf states that any country joining the restrictions would be treated as an enemy and a target, and said Iran would go after oil tankers transiting the Omani side of the Strait of Hormuz so that &ldquo;not even a single drop of oil will leave the region.&rdquo; NPR notes Iran is <em>not</em> currently interfering with those routes, which is precisely why the threat is a new variable rather than a description of the status quo &mdash; and it is the reconciliation for a crude tape that sold off into an announcement designed to tighten supply. Two further figures from the same report: Iran&rsquo;s rial fell past <b>2 million to the dollar</b> on online exchange trackers in anticipation of the package, and inflation, per the Iranian government&rsquo;s own Statistical Center, is running at almost <b>90%</b>. Separately, UN Secretary-General Ant&oacute;nio Guterres offered on Monday to have the United Nations monitor civilian shipping through the strait &mdash; &ldquo;maritime chokepoints must never become instruments of coercion&rdquo; &mdash; but said the parties to the conflict would have to agree. One dissenting note worth carrying: Alan Eyre, a former US diplomat on the nuclear negotiating team until 2015, told NPR the United States has already taken &ldquo;the low-hanging fruit, the mid-hanging fruit, the high-hanging fruit, the tree,&rdquo; and that &ldquo;there are no new sanctions that are effective.&rdquo;</p>
</div>

'''
ws = rep(ws,
    '<div class="lab">Movers &amp; drivers — the overnight tape and the late morning</div>\n<div class="cards">\n\n<div class="card">\n<div class="tags"><span class="tag up">VIX +3.64%</span>',
    '<div class="lab">Movers &amp; drivers — the overnight tape and the late morning</div>\n<div class="cards">\n\n' + NEWCARD + '<div class="card">\n<div class="tags"><span class="tag up">VIX +3.64%</span>',
    "WS insert new card")

# --- movers footnote must name the actual tagged card ---
ws = rep(ws,
    'Exactly one card is tagged New this edition &mdash; the risk gauges waking up, at the top of this section &mdash; because it is the only development here that was not already in the previous archived snapshot. The New tag carried at the previous edition, on Alibaba&rsquo;s post-earnings slide and its read-through into PDD, has been dropped for that reason; that story still stands and remains on the page below.',
    'Exactly one card is tagged New this edition &mdash; the named shadow-fleet targets of the Iran sanctions package and Tehran&rsquo;s threatened response, at the top of this section &mdash; because it is the only development here that was not already in the previous archived snapshot. The New tag carried at the previous edition, on the risk gauges waking up, has been dropped for that reason; that card still stands and remains directly below.',
    "WS movers footnote")

# --- sources ---
ws = rep(ws,
    '<li>Charles Schwab — Schwab Market Update: Tech Stocks Drag Markets Lower Early',
    '<li>NPR — Treasury Secretary Scott Bessent unveils new U.S. economic sanctions on Iran (Fatima Al-Kassab, Hadeel Al-Shalchi, Emily Feng and Michele Kelemen; published 8:26 a.m. ET, <b>updated 1:24 p.m. ET Aug 24, 2026</b> — fetched this run; source for the Treasury statement naming brokers, companies and shadow-fleet vessels across the UAE, Hong Kong, China, Singapore, Switzerland and Europe; Bessent&rsquo;s &ldquo;sever every economic lifeline&rdquo; quote; Mohsen Rezaei&rsquo;s &ldquo;seismic manner&rdquo; and Strait of Hormuz tanker threat; the rial past 2 million to the dollar; ~90% Iranian inflation per the Statistical Center of Iran; Guterres on UN monitoring; and Alan Eyre&rsquo;s dissent) — https://www.npr.org/2026/08/24/g-s1-139743/treasury-secretary-scott-bessent-to-unveil-new-economic-sanctions-on-iran</li>\n<li>Charles Schwab — Schwab Market Update: Tech Stocks Drag Markets Lower Early',
    "WS sources NPR")

wr("wallstreet-briefing.html", ws)

# ============================ CYBER ============================
cy = rd("cyber-briefing.html")

CY_TLDR = ("Iran-linked hackers took a British power plant offline for four days in the first cyberattack "
           "known to have halted a UK generating station &mdash; the Treasury Secretary answered at 1 p.m. ET "
           "with &ldquo;Operation Economic Outcast,&rdquo; naming more than 60 Iran-linked entities, "
           "individuals and vessels, some of them accused of running cyber operations for Tehran &mdash; "
           "while CISA&rsquo;s remediation deadline for an actively exploited Zimbra command-injection flaw "
           "falls today with Shadowserver already counting more than 270 compromised servers, eight other "
           "Known Exploited Vulnerabilities entries tracked here are already past due, and researchers have "
           "named two fresh loaders, WordlistLoader and SynkLoader, that look built to sell access on to "
           "ransomware crews.")

old_tldr = cy[cy.find('<div class="tldr"><b>The Wire</b>'):cy.find('</span></div>', cy.find('<div class="tldr"><b>The Wire</b>')) + len('</span></div>')]
if '<div class="tldr">' not in old_tldr:
    fails.append("MISSING: CY tldr")
else:
    cy = cy.replace(old_tldr, '<div class="tldr"><b>The Wire</b> <span>' + CY_TLDR + '</span></div>')

CYCARD = '''<div class="card">
<div class="tags"><span class="tag">Loaders</span><span class="tag">ClickFix</span><span class="tag">Teams phishing</span><span class="tag new">New</span></div>
<h3>Two newly named loaders &mdash; one hides its shellcode in English words, the other ships seven modules</h3>
<p><b>New this edition.</b> The Hacker News reported on <b>August&nbsp;24</b> that researchers have flagged two previously unnamed malware families, <b>WordlistLoader</b> and <b>SynkLoader</b>, both of which deliver next-stage payloads and are assessed as likely routes for selling access on to ransomware groups.</p>
<p><b>WordlistLoader</b>, documented by Gen Digital researcher Vojt&#283;ch Krejsa, is an intermediate stage in a chain that ends in <b>Amatera Stealer</b> (also tracked as ACR Stealer or AcridRain). Delivery is a ClearFake campaign using the ClickFix pattern: a compromised website shows a fake CAPTCHA, the victim clicks &ldquo;I&rsquo;m not a robot,&rdquo; a malicious command is placed in the clipboard and the victim is talked into pasting it into the Windows Run dialog. The injected JavaScript is a Base64 blob that pulls further JavaScript from a blockchain smart contract &mdash; the <b>EtherHiding</b> technique &mdash; so burned URLs can be swapped for fresh ones without touching the compromised site; recent campaigns have staged the payload on the legitimate <code>cdn.jsdelivr[.]net</code> CDN. The loader takes its name from its evasion: the shellcode is stored as a sequence of ordinary English words, one word per byte, and reassembled at runtime, with a variant that uses 16-byte UUID-encoded chunks instead. It also uses a hardware-breakpoint technique to bypass Event Tracing for Windows. The execution chain runs <code>conhost</code> to launch a hidden <code>cmd.exe</code>, mounts a remote WebDAV share with <code>pushd</code> and loads the DLL via <code>rundll32.exe</code> &mdash; an approach Microsoft documented in July and which, per Gen Digital, has now replaced the Python-based loaders Microsoft observed in that chain between late April and mid-June 2026.</p>
<p><b>SynkLoader</b>, documented by Expel researcher Marcus Hutchins, is the one defenders should read closely, because the delivery is internal and the toolkit is broad. It arrives as a Microsoft Teams message from an account on the target&rsquo;s own <code>onmicrosoft.com</code> default domain, using the display name &ldquo;IT Service Desk,&rdquo; which talks the user into installing an MSI hosted on Azure Blob Storage and presented as a &ldquo;PowerShell Cleaner&rdquo; &mdash; so both the sender and the download location look like Microsoft. The MSI drops a ZIP and a PowerShell script that runs in memory and launches a Python loader; the loader picks one of three hard-coded command-and-control domains, checks in at random and sleeps 90 to 120 seconds between requests. At least <b>seven modules</b> have been identified: a System Profiler C# DLL that collects host, user and Active Directory detail; a persistence module that creates a randomly named scheduled task firing at every logon and daily at 10&nbsp;a.m.; <b>PhishLocker</b>, which serves a fake Windows lock screen to harvest the login password; <b>TrafficRedirector</b>, a reverse proxy into the local network; an interactive PowerShell RAT shell; <b>StreamMaster</b>, a VNC module for full desktop control; and a status checker reporting which modules are live. Expel does not state the operator&rsquo;s end goal, but the Active Directory profiling is the tell &mdash; that metric matters most to crews pricing a ransom against network size &mdash; and the assessment is that the toolkit belongs to a ransomware group or an initial access broker.</p>
<p class="note">Two practical notes for defenders, stated because they are the cheap controls. Both chains begin with a human being persuaded to run something: the ClickFix half dies if users are trained never to paste a clipboard command into the Run dialog, and the SynkLoader half dies if external Teams messaging is restricted and MSI installs from consumer cloud storage are blocked. No CVE is involved in either chain, so neither carries a patch or a federal deadline.</p>
</div>

'''
cy = rep(cy,
    '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n\n<div class="card">\n<div class="tags"><span class="tag">Ransomware</span><span class="tag">ClickFix</span></div>',
    '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n\n' + CYCARD + '<div class="card">\n<div class="tags"><span class="tag">Ransomware</span><span class="tag">ClickFix</span></div>',
    "CY insert new card")

cy = rep(cy,
    'No item anywhere on this page carries a New tag in this edition: every story here, including Akamai&rsquo;s August 24 finding on enterprise AI super-adopters, was already in the previous archived snapshot. That makes two consecutive cyber editions with zero New tags. The one story added at this edition &mdash; the StopAndProtect WordPress network, below &mdash; is Check Point research from earlier in August and is deliberately untagged for the same reason.',
    'Exactly one item on this page carries a New tag in this edition, and it is in Breaches &amp; incidents rather than here: the WordlistLoader and SynkLoader research published on August 24, which was not in the previous archived snapshot. That ends a run of four consecutive cyber editions with zero New tags. Everything else here, including Akamai&rsquo;s August 24 finding on enterprise AI super-adopters and the StopAndProtect WordPress network, was already in the previous archived snapshot and is deliberately untagged.',
    "CY vuln footnote")

cy = rep(cy,
    'No fresh CISA KEV addition surfaced in searches this run &mdash; the August 21 Zimbra entry remains the most recent, re-confirmed against the CISA alert page this run,',
    'No fresh CISA KEV addition surfaced in searches this run &mdash; a dedicated search for additions dated August 22&ndash;24 returned none, so the August 21 Zimbra entry remains the most recent, with the August 20 TrueConf alert page the latest CISA alert re-confirmed this run,',
    "CY KEV footnote")

# sources
cy = rep(cy,
    '<div class="lab">Sources</div>\n<ul>',
    '<div class="lab">Sources</div>\n<ul>\n<li>The Hacker News — WordlistLoader Delivers Amatera via ClickFix, SynkLoader Phishes Windows Passwords (Ravie Lakshmanan, <b>Aug 24, 2026</b>; fetched this run — source for the Gen Digital WordlistLoader research credited to Vojt&#283;ch Krejsa, the ClearFake/ClickFix and EtherHiding delivery chain, the English-wordlist shellcode encoding and ETW bypass, and for the Expel SynkLoader research credited to Marcus Hutchins, the Teams &ldquo;IT Service Desk&rdquo; lure, the Azure Blob &ldquo;PowerShell Cleaner&rdquo; MSI and the seven modules) — https://thehackernews.com/2026/08/wordlistloader-delivers-amatera-via.html</li>',
    "CY sources THN")

wr("cyber-briefing.html", cy)

# ============================ INDEX ============================
ix = rd("index.html")
ix = rep(ix,
    '<p>Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station',
    '<p>' + CY_TLDR + '</p>\n<!--OLD<p>Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station',
    "IX cyber card open")
ix = rep(ix,
    'exploitation attempts against honeypots.</p>\n',
    'exploitation attempts against honeypots.</p>-->\n',
    "IX cyber card close")
ix = rep(ix,
    '<p>With under an hour of trading left the shape of the session is unchanged',
    '<p>' + WS_TLDR + '</p>\n<!--OLD<p>With under an hour of trading left the shape of the session is unchanged',
    "IX markets card open")
ix = rep(ix,
    'so no reading here is asserted as the current tape.</p>\n',
    'so no reading here is asserted as the current tape.</p>-->\n',
    "IX markets card close")
wr("index.html", ix)

if fails:
    print("FAILURES:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("ALL EDITS APPLIED OK")
