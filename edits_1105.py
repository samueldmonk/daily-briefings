#!/usr/bin/env python3
"""Midday Edition edits, Wednesday August 26 2026, ~11:05 a.m. ET."""
import io, sys, os

D = os.path.dirname(os.path.abspath(__file__))
FAIL = []

def load(f):
    return io.open(os.path.join(D, f), encoding='utf-8').read()

def save(f, s):
    io.open(os.path.join(D, f), 'w', encoding='utf-8').write(s)

def rep(s, old, new, n=1, label=''):
    c = s.count(old)
    if c != n:
        FAIL.append('%s: expected %d occurrence(s), found %d :: %s' % (label, n, c, old[:90]))
        return s
    return s.replace(old, new)

# ---------------------------------------------------------------- demote tags
def demote(s):
    return s.replace('<span class="tag new">New &middot; 10:45</span>',
                     '<span class="tag">Carried &middot; 10:45 edition</span>')

NEW = '<span class="tag new">New &middot; 11:05</span>'

# ================================================================ WALL STREET
ws = load('wallstreet-briefing.html')
ws = demote(ws)

# --- tldr
old_tldr = ws[ws.find('<div class="tldr">'):ws.find('</span></div>', ws.find('<div class="tldr">')) + len('</span></div>')]
new_tldr = (u'<div class="tldr"><b>The Tape</b> <span>Two hours in, the tape has split and it is still barely moving &mdash; '
            u'the <b>S&amp;P&nbsp;500 is 7,681.36, up 4.08 points or 0.05%</b> in a read stamped <b>~11:06&nbsp;a.m. ET</b>, '
            u'reconciling three ways against Tuesday&rsquo;s close, while the <b>Dow is down about 0.2%</b> and the '
            u'<b>Nasdaq down about 0.3%</b> with no level stated for either &mdash; and Yahoo Finance&rsquo;s live blog has '
            u'reversed its own headline from <i>&ldquo;hold steady&rdquo;</i> to <b>&ldquo;slide as PCE inflation stays sticky&rdquo;</b>, '
            u'with <b>Abercrombie &amp; Fitch still the day&rsquo;s outlier at +30.85%</b> and everything waiting on '
            u'<b>Nvidia after the close</b>.</span></div>')
ws = rep(ws, old_tldr, new_tldr, 1, 'WS tldr')

# --- lead headline
ws = rep(ws,
    u'<h2>The tape finally prints &mdash; four indices, four reconciled reads, and almost no movement in any of them as of <i>~9:59&nbsp;a.m. ET</i></h2>',
    u'<h2>The tape splits &mdash; the S&amp;P&nbsp;500 clings to green while the Dow and Nasdaq slip, as of <i>~11:06&nbsp;a.m. ET</i></h2>',
    1, 'WS lead h2')

# --- new opening paragraph in The Lead
anchor = u'<p><b>This edition retires the refusal that ran on this page all morning.</b>'
newpara = (
 u'<p><b>&#9679; New at 11:05 &mdash; the freshest read on the tape, and it does not match the 9:59 board.</b> '
 u'A market summary returned this run states that <b>the S&amp;P&nbsp;500 stood at 7,681.36, up 4.08 points or 0.05%, at around 11:06&nbsp;a.m. EDT</b>. '
 u'That figure passes this page&rsquo;s three-way test on its own: <b>7,681.36 &minus; 4.08 = 7,677.28</b>, which is exactly Tuesday&rsquo;s '
 u'S&amp;P close as published in the Weekly Scorecard below, and <b>4.08 &divide; 7,677.28 = 0.053%</b>, which rounds to the stated 0.05%. '
 u'Level, points and percent agree with each other and with an independently published prior close, so it is published as the current read. '
 u'The same summary puts the <b>Dow down about 0.2%</b> and the <b>Nasdaq Composite down about 0.3%</b> &mdash; '
 u'<b>&#9888; those two are directions only. No level and no points figure is stated for either index at that clock time, so none is printed here.</b> '
 u'Against the 9:59 board reproduced below, that is a session that has <b>given back its opening gains on two of the three headline indices</b> '
 u'while the S&amp;P&nbsp;500 has roughly halved its own.</p>\n'
 u'<p><b>&#9679; The live blog has reversed its own headline.</b> Yahoo Finance&rsquo;s running Wednesday blog was titled '
 u'<b>&ldquo;Dow, S&amp;P 500, Nasdaq futures hold steady ahead of inflation data, Nvidia earnings&rdquo;</b> when this page read it earlier today. '
 u'This run it reads <b>&ldquo;Dow, S&amp;P 500, Nasdaq slide as PCE inflation stays sticky, Nvidia earnings loom.&rdquo;</b> '
 u'Same URL, same session, changed verb &mdash; which is the clearest single marker that the morning&rsquo;s flat print has turned. '
 u'The underlying story is unchanged: sticky PCE into a Jackson Hole week, and a market that will not commit before Nvidia opens its books after the bell.</p>\n'
 + anchor)
ws = rep(ws, anchor, newpara, 1, 'WS lead new para')

# --- board paragraph gets a superseded marker
ws = rep(ws,
    u'That is the three-way test this page requires, and it passes on all four indices.</p>',
    u'That is the three-way test this page requires, and it passes on all four indices. '
    u'<b>&#9888; As of this edition that board is a 9:59 snapshot, not the current read</b> &mdash; the 11:06 figures above supersede it for the S&amp;P&nbsp;500 '
    u'and reverse its direction on the Dow and the Nasdaq. It is kept because it remains the only fully reconciled four-index board any source has produced today.</p>',
    1, 'WS board superseded')

# --- new mover card
movers_anchor = u'<div class="lab">Movers &amp; drivers</div>\n<div class="cards">\n'
newcard = movers_anchor + (
 u'<div class="card">\n'
 + u'<div class="tags">' + NEW + u'<span class="tag">Gainers</span><span class="tag">Losers</span></div>\n'
 u'<h3>Four more names get a number &mdash; and Intuit gets a second, larger one</h3>\n'
 u'<p><b>New reads surfaced this run, each stated as a percentage move with no level attached.</b> On the upside: '
 u'<b>SolarEdge (SEDG) &plus;8.3%</b> after <b>UBS upgraded the stock from Neutral to Buy and raised its price target to $42 from $36</b>; and '
 u'<b>The Williams Companies (WMB) &plus;5.6%</b>, attributed to surging natural-gas demand from AI data centres, solid results and new power-infrastructure projects. '
 u'On the downside: <b>Zoom Communications (ZM) &minus;6.2%</b>, where third-quarter guidance missed expectations and overshadowed a fiscal-second-quarter beat; and '
 u'<b>Moderna (MRNA) &minus;5%</b>, described as a pullback from a 150% surge that followed clinical-trial updates to its oncology pipeline.</p>\n'
 u'<p><b>&#9888; Intuit now has two competing regular-session numbers and neither is merged into the other.</b> '
 u'The same summary that carries the four names above puts <b>INTU &minus;9.2%</b>, attributing it to a quarterly beat paired with weak guidance for next year. '
 u'The Yahoo trending-tickers board read at ~9:59&nbsp;a.m. put it at <b>&minus;3.39%, at $345.35</b> &mdash; and that reading reconciles exactly against Tuesday&rsquo;s $357.46 close. '
 u'<b>Only the board figure carries a clock time and a prior close, so only it is used in the Chart of the Day note; the &minus;9.2% is printed as found.</b> '
 u'This page also carries a &minus;11.8% premarket read and a 7%&ndash;9% after-hours band from Tuesday night, all separately sourced and all left unmerged.</p></div>\n'
)
ws = rep(ws, movers_anchor, newcard, 1, 'WS new mover card')

# --- ticker tape: swap RZLV-style filler is not present; add SEDG while keeping mandatory five
ws = rep(ws, u'{"proName":"NASDAQ:MU","title":"Micron"}', u'{"proName":"NASDAQ:SEDG","title":"SolarEdge"}', 1, 'WS tape SEDG')

save('wallstreet-briefing.html', ws)

# ===================================================================== CYBER
cy = load('cyber-briefing.html')
cy = demote(cy)

old_tldr = cy[cy.find('<div class="tldr">'):cy.find('</span></div>', cy.find('<div class="tldr">')) + len('</span></div>')]
new_tldr = (u'<div class="tldr"><b>The Wire</b> <span>A pair of unauthenticated authentication bypasses in the '
            u'<b>Xecurify miniOrange SAML 2.0 Single Sign On</b> WordPress plugin &mdash; <b>CVE-2026-15981 (CVSS&nbsp;9.8)</b> and '
            u'<b>CVE-2026-61979 (CVSS&nbsp;8.1)</b> &mdash; are <b>under opportunistic mass scanning from six recorded IPs with public exploit code available</b>, '
            u'and they let an attacker log in as <b>any WordPress user, including administrators</b>; meanwhile <b>Boston Scientific&rsquo;s outage has moved the stock</b>, '
            u'with an 8-K describing an incident identified <b>August&nbsp;25</b> causing <b>&ldquo;a global disruption to the Company&rsquo;s operations&rdquo;</b> and Reuters '
            u'reporting shares <b>down 5.03% at $46.90</b>, while the federal board holds at <b>14 tracked KEV deadlines, 10 already past due</b>, '
            u'with the Oracle CVSS&nbsp;10.0 flaw due tomorrow.</span></div>')
cy = rep(cy, old_tldr, new_tldr, 1, 'CY tldr')

# --- Patch priority: new lead item
pp_anchor = u'<h3>Do this first &mdash; two federal deadlines inside 48 hours, both on flaws already under attack</h3>\n'
pp_new = (
 u'<h3>Do this first &mdash; a CVSS&nbsp;9.8 WordPress login bypass under live scanning, then two federal deadlines inside 48 hours</h3>\n'
 u'<p><b>&#9679; New at 11:05 &mdash; CVE-2026-15981 (CVSS&nbsp;9.8) and CVE-2026-61979 (CVSS&nbsp;8.1), Xecurify miniOrange SAML 2.0 Single Sign On for WordPress.</b> '
 u'The Hacker News, under <b>Ravie Lakshmanan</b>&rsquo;s byline dated <b>August&nbsp;25, 2026</b>, reports that bad actors are actively attempting to exploit both flaws. '
 u'They are <b>unauthenticated authentication bypasses that let an attacker sign in as any WordPress user, including administrators</b>. '
 u'CVE-2026-15981 exists because <code>mo_saml_validate_signature()</code> performs <b>&ldquo;a loose boolean check on the raw tri-state integer returned by PHP&rsquo;s openssl_verify()&rdquo;</b>, '
 u'so an <b>error return value of &minus;1 is evaluated as truthy and therefore treated as a successful signature verification</b> &mdash; a deliberately malformed signature '
 u'bypasses verification entirely and <code>wp_set_auth_cookie()</code> is called for the targeted account. CVE-2026-61979 is a privilege escalation stemming from '
 u'<b>signature algorithm confusion</b>. Disclosed by <b>Patchstack</b>, which credited the <b>DigitalOcean</b> security team after DigitalOcean spotted an anomalous '
 u'WordPress administrator session attempt from outside its trusted network. <b>Fixed in version 17.0.5 (61979) and 17.0.6 (15981) for the Standard edition.</b> '
 u'Patchstack recorded scanning from <b>207.211.214.41, 79.127.224.14, 102.91.71.83, 162.243.116.148, 84.201.6.54 and 64.225.25.188</b> and judged the spread to suggest '
 u'<b>&ldquo;opportunistic scanning rather than a targeted campaign&rdquo;</b> &mdash; whoever is running it is <b>&ldquo;throwing the exploit at every site with the plugin installed '
 u'without checking which edition or version is behind it.&rdquo;</b> <b>Proof-of-concept code is public</b> and chains the two flaws to admin. '
 u'<b>&#9888; Neither CVE is in KEV, so neither carries a federal deadline</b> &mdash; and <b>&#9888; a separate headline read this run described both as &ldquo;CVSS 9.8&rdquo;; '
 u'the CVE.org-sourced figures above give 9.8 only to 15981 and 8.1 to 61979, and those are what this page publishes.</b></p>\n'
)
cy = rep(cy, pp_anchor, pp_new, 1, 'CY patch priority')

# --- Vulnerability watch rows
vw_anchor = u'<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n'
vw_new = vw_anchor + (
 u'<tr><td>CVE-2026-15981</td><td>9.8</td><td>Xecurify miniOrange SAML 2.0 Single Sign On for WordPress (fixed in 17.0.6, Standard edition)</td>'
 u'<td>Authentication bypass &mdash; malformed signatures accepted as valid because <code>openssl_verify()</code>&rsquo;s &minus;1 error is treated as truthy. '
 u'<b>Actively targeted; public PoC. Not in KEV, no deadline.</b> Patchstack / The Hacker News, Aug&nbsp;25.</td></tr>\n'
 u'<tr><td>CVE-2026-61979</td><td>8.1</td><td>Xecurify miniOrange SAML 2.0 Single Sign On for WordPress (fixed in 17.0.5, Standard edition)</td>'
 u'<td>Unauthenticated privilege escalation via signature algorithm confusion; chains with 15981 to obtain admin. '
 u'<b>Actively targeted. Not in KEV, no deadline.</b> Credited to the DigitalOcean security team.</td></tr>\n'
)
cy = rep(cy, vw_anchor, vw_new, 1, 'CY vuln rows')

# --- Breaches: CoreRAT card
br_anchor = u'<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
br_new = br_anchor + (
 u'<div class="card">\n'
 + u'<div class="tags">' + NEW + u'<span class="tag">Espionage</span><span class="tag">RAT</span></div>\n'
 u'<h3>Core Werewolf retires its borrowed tooling and ships a custom RAT</h3>\n'
 u'<p><b>BI.ZONE analysts have documented CoreRAT</b>, described as the group&rsquo;s <b>first fully functional remote access trojan</b>, replacing its earlier reliance on '
 u'the legitimate <b>UltraVNC</b> remote-access software. The campaigns were observed <b>from June through July 2026</b>, with evidence the tool has been active '
 u'<b>since at least March</b>. Delivery ran through <b>phishing messages on Telegram</b> carrying files dressed up as official military or government documents; '
 u'opening the attachment showed a <b>PDF decoy</b> while a hidden program installed the malware. The reported focus was <b>Russia&rsquo;s public sector and defence industry</b>.</p>\n'
 u'<p><b>Written in C++</b>, CoreRAT <b>encrypts its internal strings and command-and-control addresses</b>, and before running it checks for signs it is inside a '
 u'virtual analysis machine &mdash; system details, recent shortcut activity and network adapter identifiers &mdash; <b>shutting down rather than revealing its behaviour</b> '
 u'if it suspects it is being watched. <b>&#9888; No victim count, no named organisation and no CVE is stated in the reporting fetched this run, and none is asserted here.</b></p></div>\n'
)
cy = rep(cy, br_anchor, br_new, 1, 'CY corerat card')

# --- KEV consecutive count
cy = rep(cy,
    u'the third consecutive edition in which a catalogue search returned only the Aug&nbsp;18, Aug&nbsp;20 and Aug&nbsp;21 alerts and no alert page dated August&nbsp;25 or 26.</b>',
    u'the fourth consecutive edition in which a catalogue search returned no alert page dated August&nbsp;25 or 26. '
    u'This run the search surfaced CISA alert pages dated <b>August&nbsp;11 (three), August&nbsp;18 (four), August&nbsp;20 (two) and August&nbsp;24 (one)</b> and nothing later, '
    u'and it independently re-confirmed both adjudications: <b>CVE-2026-21962 is the Oracle HTTP Server and WebLogic Proxy Plug-in flaw added August&nbsp;24</b>, '
    u'and <b>CVE-2026-60004 is the Gitea remote code execution flaw</b>, patched by Gitea in late July in <b>version 1.27.1</b>.</b>',
    1, 'CY kev count')

save('cyber-briefing.html', cy)

# ======================================================================= MMA
mma = load('mma-briefing.html')
mma = demote(mma)

# --- odds: add UFC.com official rendering
mma = rep(mma,
 u'<p><b>Odds:</b> <b>Nurmagomedov &minus;470 / Song +360 (DraftKings)</b>, per MMA Junkie&rsquo;s odds piece re-fetched this run. '
 u'Two opening lines from other books also stand: <b>&minus;700 / +500 (BetOnline.ag)</b> and <b>&minus;500 / +385</b>. '
 u'The three are printed unmerged &mdash; they are different books at different moments &mdash; but they agree on the direction: '
 u'Nurmagomedov is a heavy favourite everywhere.</p>',
 u'<p><b>Odds:</b> <b>Nurmagomedov &minus;470 / Song +360 (DraftKings)</b>, per MMA Junkie&rsquo;s odds piece. '
 u'Three further lines stand: <b>&minus;700 / +500 (BetOnline.ag)</b>, <b>&minus;500 / +385</b>, and &mdash; <b>new this run</b> &mdash; '
 u'<b>&minus;500 / +375, the line the official UFC site is listing</b>. '
 u'The four are printed unmerged &mdash; they are different books at different moments &mdash; but they agree on the direction: '
 u'Nurmagomedov is a heavy favourite everywhere, and no source read this run has him anything but.</p>\n'
 u'<p class="note"><b>&#9679; Venue, re-confirmed this run.</b> A fresh search states the card is held at the '
 u'<b>Shanghai Oriental Sports Center, Shanghai, China</b>, which matches UFC.com and this page. '
 u'<b>&#9888; A separate result this run again renders the venue as &ldquo;Shanghai Indoor Stadium&rdquo; and again gives the card 13 fights; '
 u'the Oriental Sports Center name is the one published here.</b> Start times re-confirmed: '
 u'<b>Paramount+ prelims 3&nbsp;a.m. ET, main card 6&nbsp;a.m. ET</b>.</p>',
 1, 'MMA odds')

mma = rep(mma,
 u'<div class="tags"><span class="tag hot">This Saturday</span><span class="tag">UFC Shanghai</span></div>',
 u'<div class="tags"><span class="tag hot">This Saturday</span>' + NEW + u'<span class="tag">UFC Shanghai</span></div>',
 1, 'MMA card tag')

old_tldr = mma[mma.find('<div class="tldr">'):mma.find('</span></div>', mma.find('<div class="tldr">')) + len('</span></div>')]
new_tldr = (u'<div class="tldr"><b>Tale of the Tape</b> <span>Three days out from <b>UFC Shanghai</b>, the line on '
            u'<b>Umar Nurmagomedov (20-1) vs. Song Yadong (23-9-1)</b> has now been read four different ways &mdash; '
            u'<b>&minus;470/+360 at DraftKings</b>, <b>&minus;700/+500 at BetOnline.ag</b>, <b>&minus;500/+385</b>, and '
            u'<b>&minus;500/+375 on the official UFC site</b>, all published unmerged and all pointing the same way &mdash; '
            u'for a <b>6:00&nbsp;a.m. EDT Saturday</b> main event at the <b>Shanghai Oriental Sports Center</b> whose winner UFC.com says is '
            u'<b>&ldquo;first in line to face the winner of Yan-Dvalishvili 3,&rdquo;</b> while the business page still rests on TKO&rsquo;s CFO telling '
            u'investors the White House card lost about <b>$30&nbsp;million</b> on roughly <b>$60&nbsp;million</b> of production.</span></div>')
mma = rep(mma, old_tldr, new_tldr, 1, 'MMA tldr')

save('mma-briefing.html', mma)

# ===================================================================== INDEX
ix = load('index.html')

def card(ix, cls, h2, p, label):
    import re as _re
    m = _re.search(r'(<a class="bcard %s"[^>]*>.*?<h2>)(.*?)(</h2>\s*<p>)(.*?)(</p>)' % cls, ix, _re.S)
    if not m:
        FAIL.append('index card %s not matched' % label)
        return ix
    return ix[:m.start(2)] + h2 + ix[m.end(2):m.start(4)] + p + ix[m.end(4):]

def tldr_body(f):
    s = load(f)
    i = s.find('<div class="tldr">')
    a = s.find('<span>', i) + len('<span>')
    b = s.find('</span></div>', a)
    return s[a:b]

ix = card(ix, 'c-sec',
  u'A CVSS&nbsp;9.8 WordPress login bypass is under mass scanning &mdash; with public exploit code',
  tldr_body('cyber-briefing.html'), 'sec')
ix = card(ix, 'c-mkt',
  u'The tape splits at midday: the S&amp;P clings to green, the Dow and Nasdaq slide',
  tldr_body('wallstreet-briefing.html'), 'mkt')
ix = card(ix, 'c-mma',
  u'Four books, four different lines on Umar &mdash; and they all say the same thing',
  tldr_body('mma-briefing.html'), 'mma')

save('index.html', ix)

if FAIL:
    print('FAILURES:')
    for f in FAIL:
        print(' -', f)
    sys.exit(1)
print('edits OK')
