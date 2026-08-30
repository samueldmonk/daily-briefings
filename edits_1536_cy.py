#!/usr/bin/env python3
"""Cyber Wire edits — Sunday Aug 30 2026, ~3:36 PM ET research, seventh run of the day."""
import io, os, sys

D = sys.argv[1]
P = os.path.join(D, 'cyber-briefing.html')
h = io.open(P, encoding='utf-8').read()
n = 0

def sub(old, new, label):
    global h, n
    if old not in h:
        print('MISS:', label); return
    h = h.replace(old, new, 1); n += 1
    print('  ok:', label)

# ─────────────────────────────────────────────────────────────────────────────
# 1. TLDR
# ─────────────────────────────────────────────────────────────────────────────
old_tldr_start = '<div class="tldr"><b>The Wire</b> <span>Two federal remediation deadlines'
i = h.find(old_tldr_start)
j = h.find('</span></div>', i)
new_tldr = ('<div class="tldr"><b>The Wire</b> <span>A <b>$5.72 million theft across six blockchains</b> '
            'is new to this page and it is a governance failure as much as a code one &mdash; Cosmos Labs '
            'says the balance-handling flaw behind it was <b>reported through its own bug bounty on April 25 '
            'and assessed at the time as posing no risk to live funds</b>, four months before it was used; '
            'the <b>two federal deadlines due today</b> &mdash; CVE-2023-49105 in ownCloud and CVE-2026-53362 '
            'in the Linux kernel &mdash; were re-read against the clock and still fall <b>Sunday, August 30</b>, '
            'and a <b>fourteenth KEV check</b> returned nothing dated later than August 27 for an eighth '
            'consecutive time; and an internal contradiction inside the Patch Priority box, where the demoted '
            'Citrix item still said &ldquo;that is today&rdquo; under a heading reading EXPIRED YESTERDAY, '
            'was found and fixed.')
h = h[:i] + new_tldr + h[j:]
n += 1
print('  ok: tldr')

# ─────────────────────────────────────────────────────────────────────────────
# 2. Threat banner — keep High, refresh the "why"
# ─────────────────────────────────────────────────────────────────────────────
sub('biggest new item on this page &mdash; the McKesson data theft &mdash; was reportedly reached not through any\nsoftware flaw but through phone calls to employees.',
    'biggest new item on this page &mdash; the McKesson data theft &mdash; was reportedly reached not through any\n'
    'software flaw but through phone calls to employees. <b>Added this run:</b> a critical flaw in the shared '
    '<b>Cosmos EVM</b> module was used to drain <b>$5.72 million from six blockchains</b> between August 20 and '
    'August 25 &mdash; four months after it was reported and cleared as harmless.',
    'threat banner why')

# ─────────────────────────────────────────────────────────────────────────────
# 3. Stat strip — precise Shadowserver count, plus the Cosmos figure
# ─────────────────────────────────────────────────────────────────────────────
sub('<div class="stat"><div class="n">8,300+</div><div class="l">Internet-exposed <b>Gitea</b> servers still unpatched against an exploited 9.8 RCE, per Shadowserver</div></div>',
    '<div class="stat"><div class="n">8,393</div><div class="l">Internet-exposed <b>Gitea</b> IPs still vulnerable to an exploited 9.8 RCE &mdash; Shadowserver&rsquo;s count as of <b>Aug 27</b>, the precise form of the &ldquo;8,300+&rdquo; this page carried</div></div>\n'
    '<div class="stat"><div class="n">$5.72M</div><div class="l">Drained from <b>six Cosmos EVM chains</b> Aug 20&ndash;25 &mdash; and it reconciles: <b>$2.87M</b> through decentralised exchanges plus <b>$2.85M</b> through centralised ones</div></div>',
    'stat strip')

# ─────────────────────────────────────────────────────────────────────────────
# 4. Patch Priority — fix the internal contradiction on the demoted Citrix item
# ─────────────────────────────────────────────────────────────────────────────
sub('date of <b>Saturday, August 29</b>. That is today: the countdown below reads <b>0 days left</b>, and it does not\nget another edition.',
    'date of <b>Saturday, August 29</b>. <b>That date has passed:</b> the countdown below reads <b>OVERDUE</b>, '
    'not &ldquo;0 days left,&rdquo; and this paragraph said the opposite until it was re-read against the clock '
    'this run &mdash; the heading above it had already been demoted while the sentence under it still read '
    '&ldquo;that is today.&rdquo; <b>The same defect as last run, one paragraph deeper.</b>',
    'citrix contradiction fix')

# 5. Patch Priority — ownCloud gains vendor-grade detail
sub('is an improper-authentication flaw in <b>ownCloud Server 10.6.0 through 10.13.0</b> that lets an unauthenticated attacker access or modify another user&rsquo;s files; reporting fetched this run ties its exploitation to the theft of nuclear research records from a Philippine research body.',
    'is an improper-authentication flaw in <b>ownCloud Server 10.6.0 through 10.13.0</b> that lets an '
    'unauthenticated attacker access or modify another user&rsquo;s files; reporting fetched this run ties its '
    'exploitation to the theft of nuclear research records from a Philippine research body. <b>New at 3:36 PM, '
    'and it is the detail that tells you whether you are exposed:</b> the flaw is a <b>WebDAV API authentication '
    'bypass</b> carrying <b>CVSS 9.8</b>, exploitable when the attacker knows a username and that user has '
    '<b>no signing key configured &mdash; which is the default</b>. It was <b>disclosed by ownCloud in November '
    '2023</b> and <b>fixed in core version 10.13.1</b>. A flaw whose precondition is the default configuration '
    'and whose fix shipped nearly three years ago is not a patching problem, it is an inventory problem. The '
    'actor is described as <b>Chinese-speaking</b>; no further attribution was stated by anything fetched, and '
    'none is printed.',
    'ownCloud detail')

# ─────────────────────────────────────────────────────────────────────────────
# 6. Breaches & Incidents — new Cosmos card at the head of the deck
# ─────────────────────────────────────────────────────────────────────────────
cosmos = (
'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n'
'<div class="card"><div class="tags"><span class="tag new">New &middot; 3:36 PM</span>'
'<span class="tag warn">No CVE assigned</span><span class="tag">Blockchain</span></div>'
'<h3>A bug reported in April and cleared as harmless was used in August to take $5.72 million off six chains</h3>'
'<p><b>What happened.</b> Cosmos Labs has warned that a <b>critical balance-handling flaw in the shared Cosmos EVM '
'module</b> was exploited to drain funds from <b>six blockchains between August 20 and August 25, 2026</b>. '
'<b>About $5.72 million</b> was taken, <b>three chains halted operations</b>, and Cosmos Labs says it contacted '
'<b>40 networks</b>. The mechanism is an <b>integer underflow</b>: driving an account balance below zero made the '
'system read the negative value as the <b>largest possible positive number</b>, from which the attacker could move '
'other accounts&rsquo; tokens to an address of their own.</p>'
'<p><b>The figure reconciles against itself, which is why it is printed as a figure and not as a range.</b> The '
'post-mortem accounts for the movement as <b>$2.87 million through decentralised exchanges</b> and <b>$2.85 million '
'through centralised ones</b>. Those two sum to <b>$5.72 million</b> exactly &mdash; the same arithmetic check the '
'markets page ran on Thursday and Friday&rsquo;s index closes, applied here. A separate report rounds the total to '
'<b>$5.7 million</b>; that is the same number with one fewer digit, not a second claim.</p>'
'<p><b>The part that makes this a governance story.</b> In a post-mortem published <b>August 28</b>, Cosmos Labs '
'says the flaw was <b>reported through its bug bounty programme on April 25</b> and <b>assessed at the time as '
'posing no risk to funds on live networks</b> &mdash; an assessment the organisation now says was wrong. The team '
'confirmed by <b>August 13</b> that <b>all Cosmos EVM chains were affected regardless of decimal configuration</b>. '
'Affected versions are <b>&lt; 0.6.2</b> and <b>&gt;= 0.7.0 &lt; 0.7.2</b>; the fix shipped in <b>v0.6.2 and v0.7.2 '
'on August 19</b> &mdash; the day before the first drain.</p>'
'<p>&#9888; <b>It has no CVE, and that is worth stating rather than working around.</b> The advisory is '
'<b>GHSA-7g4w-cg88-2cq2</b>, rated <b>Critical by Cosmos Labs</b> and published <b>without a CVE identifier, '
'without a weakness classification and without a CVSS score</b>. It gets no row in the Vulnerability Watch table '
'below for exactly that reason: <b>that table indexes CVEs, and this is not one</b>. A vulnerability that never '
'enters the CVE system is invisible to every scanner keyed to it, which is a defensive gap independent of the '
'money.</p></div>\n')
sub('<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n', cosmos, 'cosmos card')

# ─────────────────────────────────────────────────────────────────────────────
# 7. Anthropic card — name the families, and the reason 2FA does not help
# ─────────────────────────────────────────────────────────────────────────────
sub('<b>No number of affected accounts was stated by any source fetched this run, and none is printed here.</b></p></div>',
    '<b>No number of affected accounts was stated by any source fetched this run, and none is printed here.</b></p>'
    '<p><b>Added at 3:36 PM &mdash; the families are named, and so is the reason a second factor does not save you.</b> '
    'Reporting fetched this run lists the malware in question as <b>Vidar</b>, <b>LummaC2</b>, <b>StealC</b> and '
    '<b>RedLine</b> among others, each of which searches browsers for <b>passwords, cookies and authentication '
    'data</b>. The consequence is stated plainly by the same source and is the operative point for anyone writing '
    'a control around this: because the attacker <b>reuses a valid session</b>, the login flow is never entered, '
    'so <b>the password prompt and the 2FA prompt are both bypassed</b>. Multi-factor authentication defends '
    'the door; this walks in through a window that was already open. <b>Signing out kills the stolen session and '
    'does nothing to the malware</b> &mdash; if it is still resident, the next session is taken the same way.</p></div>',
    'anthropic families')

# ─────────────────────────────────────────────────────────────────────────────
# 8. Gitea row — precise exposure count, reporter, and the directive behind Aug 28
# ─────────────────────────────────────────────────────────────────────────────
sub('One report headlined a &ldquo;patch before August 28&rdquo; date; <b>no CISA page stating a due date was returned, so no deadline is printed for it above.</b>',
    'One report headlined a &ldquo;patch before August 28&rdquo; date; <b>no CISA page stating a due date was '
    'returned, so no deadline is printed for it above.</b> <b>Sharpened at 3:36 PM on three points.</b> First, '
    'the exposure figure has a precise form and a date: Shadowserver found <b>8,393 IPs vulnerable on August 27</b>, '
    'which is what this page&rsquo;s &ldquo;8,300+&rdquo; was rounding. Second, the flaw was <b>reported by '
    'Salesforce security researcher Shai Rod</b>. Third, the August 28 date now has a directive attached: reporting '
    'this run states CISA gave federal agencies <b>three days</b> to patch, under <b>BOD 26-04</b>, the same '
    'risk-based regime that produced the short windows elsewhere on this page. &#9888; <b>That is still not a '
    'CISA page, so it still gets no countdown row</b> &mdash; but it does mean the date, whoever states it, is now '
    '<b>two days past</b> either way.',
    'gitea sharpen')

# ─────────────────────────────────────────────────────────────────────────────
# 9. KEV — fourteenth check
# ─────────────────────────────────────────────────────────────────────────────
sub('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>\n<div class="panel"><ul class="bul">\n',
    '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>\n<div class="panel"><ul class="bul">\n'
    '<li><span class="tag new">New &middot; 3:36 PM</span> <b>A fourteenth check, and the interesting result is '
    'that the rows did not move on a day when they easily could have.</b> The sweep returned CISA&rsquo;s own '
    'alert pages for <b>August 11</b> (three), <b>August 18</b> (four), <b>August 20</b> (two: CVE-2026-72529 and '
    'CVE-2026-72530, TrueConf Server), <b>August 21</b> (one: CVE-2026-73570, Zimbra) and <b>August 26</b> (six, '
    'all six identifiers matching the rows below), with <b>nothing dated later than August 27</b> for an '
    '<b>eighth consecutive check</b>. <b>The two rows due today were re-read against the clock rather than '
    'against their source</b>, which is the check that failed yesterday: it is <b>Sunday, August 30</b>, the '
    'ownCloud and Linux kernel deadlines fall today, and the Citrix and SQL Server pair is a day overdue. '
    '&#9888; <b>One aggregate figure returned and is attributed rather than adopted:</b> a KEV-tracking site '
    'states CISA confirmed <b>24 new KEV entries in the 30 days of August</b>. That is a tracker&rsquo;s count of '
    'a catalogue this board has already shown itself to see only partly &mdash; <b>three known gaps in fourteen '
    'checks</b> &mdash; so it is printed as that site&rsquo;s number and is not used to conclude anything about '
    'completeness here.</li>\n',
    'fourteenth kev check')

# ─────────────────────────────────────────────────────────────────────────────
# 10. Sources
# ─────────────────────────────────────────────────────────────────────────────
sub('</ul></div><footer><div class="srcs"><b>Sources checked this run:</b><br>',
    '</ul></div><footer><div class="srcs"><b>Sources checked this run:</b><br>'
    '<a href="https://thehackernews.com/2026/08/cosmos-evm-flaw-exploited-after-cosmos.html">The Hacker News &mdash; Cosmos EVM flaw exploited after Cosmos Labs knew every chain running it was vulnerable</a><br>'
    '<a href="https://www.theblock.co/news/defi/2026-08-29-cosmos-labs-says-it-wrongly-cleared-the-bug-behind-a-5-7-million-six-chain-hack-413061">The Block &mdash; Cosmos Labs says it wrongly cleared the bug behind a $5.7 million six-chain hack</a><br>'
    '<a href="https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds three known exploited vulnerabilities to catalog (Aug 27, 2026)</a><br>'
    '<a href="https://www.scworld.com/brief/cisa-adds-owncloud-linux-kernel-and-jfrog-artifactory-flaws-to-exploited-vulnerabilities-list">SC Media &mdash; CISA adds ownCloud, Linux kernel and JFrog Artifactory flaws to the exploited list</a><br>'
    '<a href="https://www.bleepingcomputer.com/news/security/over-8-300-gitea-servers-vulnerable-to-code-execution-attacks/">BleepingComputer &mdash; Over 8,300 Gitea servers vulnerable to code execution attacks (Shadowserver: 8,393 IPs on Aug 27)</a><br>'
    '<a href="https://senserva.com/exploited-this-week.html">Senserva &mdash; CISA KEV additions this week (24 entries in August; tracker&rsquo;s own count)</a><br>',
    'cyber sources')

io.open(P, 'w', encoding='utf-8').write(h)
print(f'cyber edits applied: {n}')
