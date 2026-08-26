#!/usr/bin/env python3
# Cyber incremental edits — 10:55 a.m. ET edition, Wed Aug 26 2026
import sys, io
P = sys.argv[1] if len(sys.argv) > 1 else '.'
f = P + '/cyber-briefing.html'
h = io.open(f, encoding='utf-8').read()
n = 0
def rep(old, new, cnt=1):
    global h, n
    assert h.count(old) >= 1, 'MISSING: ' + old[:110]
    h = h.replace(old, new, cnt); n += 1

# 1 — demote old New tags
rep('<span class="tag new">New &middot; 10:20</span>',
    '<span class="tag">Carried &middot; 10:20 edition</span>', 99)

# 2 — TLDR
rep('&mdash; while the federal board holds at <b>14 tracked KEV deadlines, 10 already past due</b> and the Oracle CVSS&nbsp;10.0 flaw due tomorrow.',
    '&mdash; while the federal board holds at <b>14 tracked KEV deadlines, 10 already past due</b>, the Oracle CVSS&nbsp;10.0 flaw falls due tomorrow, and a critical <b>Adobe Commerce</b> account-takeover bug joins the watchlist as already-blocked exploitation attempts.')

# 3 — new Breaches card: Adobe Commerce
rep('<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n<div class="card">',
    '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
    '<div class="card">\n<div class="tags"><span class="tag new">New &middot; 10:55</span><span class="tag">Exploited</span><span class="tag">E-commerce</span></div>\n'
    '<h3>Attackers are switching Magento shoppers into other people&rsquo;s accounts &mdash; and Adobe says it has not seen it</h3>\n'
    '<p><b>CVE-2026-71362</b> is an <b>incorrect-authorization</b> flaw in <b>Adobe Commerce and Magento</b> that can be leveraged to <b>&ldquo;gain elevated access to sensitive resources&rdquo; without authentication</b>. It is one of seven issues Adobe fixed in a security update, and <b>the vendor advisory (APSB26-92) states Adobe is not aware of exploits in the wild for any of the fixed flaws</b>. E-commerce security firm <b>Sansec</b> says otherwise: its <b>Shield web application firewall is already blocking CVE-2026-71362 exploitation attempts</b>. Both statements are published as made; this page does not adjudicate between the vendor and the WAF vendor.</p>\n'
    '<p><b>The mechanic, from Sansec&rsquo;s patch analysis.</b> Exploiting it requires <b>&ldquo;no existing account, administrator privileges or user interaction.&rdquo;</b> The root cause is Magento improperly handling customer identity in an account session: <b>&ldquo;Sansec reviewed the patch and confirmed that the vulnerability lets attackers switch a customer session to another customer account. This gives them access to the victim&rsquo;s account and private customer data.&rdquo;</b> The other six flaws in the same update are <b>CVE-2026-48413 (8.7)</b> and <b>CVE-2026-48414 (7.7)</b>, stored XSS leading to arbitrary code execution; <b>CVE-2026-48415 (7.6)</b> and <b>CVE-2026-48416 (7.5)</b>, incorrect authorization enabling a security-feature bypass; <b>CVE-2026-48411 (6.5)</b>; and <b>CVE-2026-48412 (2.7)</b>.</p>\n'
    '<p><b>&#9888; This is not a today story and is not presented as one.</b> BleepingComputer&rsquo;s report is bylined <b>Bill Toulas</b> and dated <b>August&nbsp;12, 2026, 4:54&nbsp;p.m.</b>; it surfaced on this desk for the first time this run and is carried at its real date. <b>No CVSS score is published for CVE-2026-71362</b>, because the report gives scores for the other six flaws and not for that one. The operational note that matters: Sansec says these monthly fixes ship as <b>isolated patch files</b> rather than a new security release or updated Composer packages, so admins must first be on the latest <b>-p</b> release for their supported branch before the patch will apply. <b>It is not in KEV</b>, so no federal deadline attaches.</p></div>\n'
    '<div class="card">')

# 4 — Vulnerability Watch row
rep('<tr><td>CVE-2026-69836</td>',
    '<tr><td>CVE-2026-71362</td><td>not stated</td><td>Adobe Commerce &amp; Magento (fixed in the August 2026 update, APSB26-92)</td><td>Incorrect authorization &rarr; unauthenticated elevated access; lets an attacker switch a customer session to another customer account. <b>Adobe says it is unaware of in-the-wild exploits; Sansec says its WAF is already blocking exploitation attempts.</b> Not in KEV. BleepingComputer, Aug&nbsp;12.</td></tr>\n'
    '<tr><td>CVE-2026-69836</td>')

# 5 — sector-sequence line: add iRhythm and Amgen
rep('naming device makers <b>Abbott Laboratories, Stryker and Medtronic</b>, health insurer <b>Clover Health</b>, drugmaker <b>Novo Nordisk</b> and drug-delivery supplier <b>West Pharmaceutical Services</b> as having been hit recently.',
    'naming device makers <b>Abbott Laboratories, Stryker and Medtronic</b>, health insurer <b>Clover Health</b>, drugmaker <b>Novo Nordisk</b> and drug-delivery supplier <b>West Pharmaceutical Services</b> as having been hit recently. <b>Fierce Biotech, surfaced this run, gives an overlapping but not identical list</b> &mdash; <b>Abbott, iRhythm, Medtronic and Stryker</b> among medtechs, plus <b>Amgen</b> and <b>Novo Nordisk</b> among large pharma &mdash; adding <b>iRhythm</b> and <b>Amgen</b> to the names this page has seen. The two lists are printed as each outlet gives them and are not merged into one roster.')

# 6 — KEV board status: third consecutive edition with nothing seen
rep('Nothing has been added on August&nbsp;26.',
    '<b>Nothing was seen this run for August&nbsp;26 &mdash; the third consecutive edition in which a catalogue search returned only the Aug&nbsp;18, Aug&nbsp;20 and Aug&nbsp;21 alerts and no alert page dated August&nbsp;25 or 26.</b> That is stated as <i>nothing seen</i>, not as <i>nothing added</i>. <b>&#9888; A search summary this run described &ldquo;an Oracle HTTP Server and Oracle WebLogic Server Proxy Plug-in flaw, tracked as CVE-2026-60004&rdquo;</b> &mdash; that conflates two separate entries. <b>CVE-2026-21962 is the Oracle flaw (due Aug&nbsp;27); CVE-2026-60004 is the Gitea code-injection flaw (due Aug&nbsp;28)</b>, and the same summary goes on to describe 60004 correctly as an RCE exploitable by an attacker with write access to a repository, which is Gitea, not Oracle. The board below keeps them apart.')

# 7 — Sources
rep('<div class="lab">Sources</div>\n<ul>\n',
    '<div class="lab">Sources</div>\n<ul>\n'
    '<li><b>BleepingComputer &mdash; <a href="https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/">&ldquo;Hackers exploit critical Adobe Commerce flaw to hijack customer accounts&rdquo;</a></b> (Bill Toulas, August&nbsp;12, 2026, 4:54&nbsp;p.m.), <b>fetched in full this run</b> &mdash; the source for CVE-2026-71362, the Adobe advisory <b>APSB26-92</b>, Adobe&rsquo;s statement that it is unaware of exploits in the wild, Sansec&rsquo;s contrary WAF observation, the quoted Sansec patch analysis, the six accompanying CVEs with their scores, and the isolated-patch-file deployment note. Carried at its real date; it is not presented as August&nbsp;26 news.</li>\n'
    '<li><b>Fierce Biotech &mdash; &ldquo;Boston Scientific hit by cyberattack causing &lsquo;disruptions&rsquo; to parts of its business&rdquo;</b>, with <b>Insurance Journal</b>, <b>The Star</b> and the <b>Union Leader</b> &mdash; re-confirming the August&nbsp;25 detection, the incident-response activation, the third-party specialists, the unknown restoration timeline and the Reuters figure of <b>&minus;5.03% at $46.90, a fresh 20-day low</b>; Fierce Biotech is the source for the <b>iRhythm</b> and <b>Amgen</b> names added to the sector sequence above. <b>Search summaries and headlines, not fetched in full.</b></li>\n')

io.open(f, 'w', encoding='utf-8').write(h)
print('cyber OK — %d edits' % n)
