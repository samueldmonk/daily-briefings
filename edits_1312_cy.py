#!/usr/bin/env python3
"""Cyber page — 1:12 PM ET edition, Aug 31 2026. Content edits only."""
import io

P = 'cyber-briefing.html'
h = io.open(P, encoding='utf-8').read()
orig = len(h)

# ---------------------------------------------------------------- 1. TLDR
s = h.find('<div class="tldr"><b>The Wire</b>')
assert s > 0
e = h.find('</div>', h.find('</span>', s)) + len('</div>')
NEW_TLDR = (
'<div class="tldr"><b>The Wire</b> <span>'
'<b>The Manchester Airports breach has an attacker, a method and a file size, and the method is the '
'part every other organisation should read.</b> The extortion group <b>FulcrumSec</b> claims it took '
'<b>86 GB</b> from <b>Manchester Airports Group</b> after finding <b>Iterable API credentials sitting '
'in client-side JavaScript</b> &mdash; code that runs in visitors&rsquo; browsers, where anyone with '
'developer tools could read them. Samples shared with reporters include a <b>21.5 GB export of '
'Manchester customer data</b> and <b>nearly 200,000 records tied to travel booked for the rest of '
'2026</b>, against the <b>8.7 million customers</b> MAG itself disclosed. '
'&#9888; <b>The 86 GB and the sample counts are the attacker&rsquo;s and its reporting&rsquo;s; the '
'8.7 million is the company&rsquo;s.</b> Separately, <b>Berlin&rsquo;s state government has confirmed '
'data theft</b> after <b>Rhysida</b> claimed <b>5.79 TB</b> three weeks before a state election, and '
'says it will not pay.'
'</span></div>')
h = h[:s] + NEW_TLDR + h[e:]

# ------------------------------------------------------- 2. Top Story prepend
anchor = '<h2 class="sec">Top Story</h2>'
assert anchor in h
TOP = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:12 PM</span> '
'<b>The Manchester Airports Group breach is no longer anonymous, and the entry point is the kind that '
'costs nothing to check for.</b> The data-extortion group <b>FulcrumSec</b> has claimed the intrusion '
'and says it exfiltrated <b>roughly 86 GB</b>. Its stated method: it found <b>airport-specific '
'Iterable API credentials inside client-side JavaScript</b> &mdash; the code delivered to and executed '
'in every visitor&rsquo;s browser, meaning <b>anyone inspecting the site with developer tools could '
'read them</b>. <b>Iterable is a customer-engagement and marketing-messaging platform</b>, used here to '
'drive <b>booking confirmations, promotional email and Wi-Fi sign-up flows</b> &mdash; which is exactly '
'why a key to it reaches the categories MAG disclosed.<br><br>'
'<b>The claimed volumes, with whose numbers they are stated on each.</b> FulcrumSec shared samples with '
'reporters that included a <b>21.5 GB export of Manchester customer data</b> carrying <b>personal '
'identifiers, historical booking detail and marketing information</b>, and it says the material contains '
'<b>nearly 200,000 records relating to upcoming travel across the remainder of 2026</b>. '
'&#9888; <b>Every one of those figures is the attacker&rsquo;s, relayed by reporting that saw a sample '
'&mdash; not a company statement and not an audited count.</b> The <b>8.7 million customers</b> figure '
'this page has carried since Saturday is the opposite: <b>MAG&rsquo;s own</b>. '
'<b>Both are printed; neither is used to check the other</b>, because a sample size and a '
'notification population are not the same measurement and an extortion group has every incentive to '
'blur them.<br><br>'
'<b>On the group itself, only what was returned.</b> FulcrumSec is described as a <b>financially '
'motivated data-extortion operation active since 2025</b> that <b>steals and threatens to publish '
'rather than encrypting</b> its victims&rsquo; systems. &#9888; <b>No ransom figure, no deadline and no '
'MAG response to the attribution was returned this run, so none is printed.</b> '
'&#9888; <b>The attribution is the group&rsquo;s claim plus reporters&rsquo; sample review; MAG has not '
'been fetched confirming it.</b> The company&rsquo;s own disclosure &mdash; detected <b>August 25</b>, '
'confirmed publicly <b>August 27</b>, <b>no bank or payment details held</b>, operations and aviation '
'security unaffected &mdash; is unchanged and sits below.<br><br>'
'&#9888; <b>The lesson here is not about airports.</b> A credential in client-side JavaScript is not a '
'breach of a perimeter; it is a key published on the front door. <b>It is discoverable by any visitor '
'and by every crawler</b>, it leaves no intrusion to detect, and <b>rotating the key is the whole '
'remediation</b> &mdash; which also means the exposure window runs from the day the code shipped, not '
'from the day anyone noticed.</div>')
h = h.replace(anchor, anchor + TOP, 1)

# --------------------------------------------------- 3. Berlin breach card
banchor = '<h2 class="sec">Breaches &amp; Incidents</h2>'
assert banchor in h
BERLIN = (
'<div class="card"><div class="tags"><span class="tag new">New &middot; 1:12 PM</span>'
'<span class="tag crit">Government</span><span class="tag warn">Pre-election</span></div>'
'<h4>Berlin &mdash; the state confirms data theft as Rhysida claims 5.79 TB, three weeks before a vote</h4>'
'<p><b>Berlin&rsquo;s city-state government has confirmed that data was stolen</b> from its '
'administrative network after the <b>Rhysida</b> ransomware group claimed responsibility on its leak '
'site on <b>August 28</b>, posting an entry titled simply <b>&ldquo;Berlin, Germany&rdquo;</b>. '
'The group claims <b>5.79 terabytes across roughly 1.44 million files</b>, and says the trove includes '
'personal information on <b>12,076 individuals</b>.</p>'
'<p>The claimed contents, <b>as described by the attacker</b>: government, legal, financial, '
'contractual, HR, infrastructure, health and mapping records; names, email addresses and phone numbers; '
'<b>148 IBANs</b>; plaintext credentials, database accounts, password vaults and credentials belonging '
'to senior officials; personnel files, payroll data, administrative-offence records, email archives, '
'SQL dumps and identity documents. &#9888; <b>The confirmation and the inventory come from different '
'parties</b> &mdash; <b>Berlin confirms a theft; the 5.79 TB, the file count and the categories are '
'Rhysida&rsquo;s posting</b>, and a leak-site listing is not a source for its own volume.</p>'
'<p><b>The timing is the reason this is a top-tier item rather than another listing.</b> '
'<b>Berlin elects its House of Representatives on September 20</b>, under a month after the intrusion. '
'<b>Senator Iris Spranger states that officials found no evidence election data was compromised</b> and '
'that the technical environment supporting the vote is considered secure. '
'<b>Berlin says it will not pay</b>; the group is demanding <b>30 bitcoin</b>, put at close to '
'<b>$2.3 million</b> at the exchange rate cited, and has set a <b>one-week countdown</b> before it says '
'it will begin publishing. &#9888; <b>The dollar conversion is the reporting&rsquo;s, at its own '
'moment</b> &mdash; 30 BTC is the demand; the dollar figure is a derived number that moves.</p></div>')
h = h.replace(banchor, banchor + BERLIN, 1)

# ------------------------------------------------ 4. GiveWP vulnerability note
vanchor = '<h2 class="sec">Vulnerability Watch</h2>'
assert vanchor in h
GIVE = (
'<div class="note" style="margin-bottom:14px"><p><span class="tag new">New &middot; 1:12 PM</span> '
'<b>A CVSS 10.0 landed in a WordPress donation plugin, and the two accounts of how exploitable it is '
'only look contradictory until the third detail arrives.</b> <b>CVE-2026-82222</b>, rated '
'<b>CVSS 10.0</b>, affects <b>GiveWP through version 4.16.7.1</b>: an <b>unauthenticated PHP object '
'injection</b> that chains into <b>full remote code execution</b>. <b>Fixed in 4.16.7.2, released '
'August 27</b>, which blocks serialized data during donation processing and restricts object creation '
'at several deserialization points.</p>'
'<p>&#9888; <b>The reporting fetched this run says both that no account is needed and that successful '
'exploitation depends on the attacker having one.</b> <b>Neither is dropped, because the same reporting '
'reconciles them:</b> the plugin <b>exposes an unauthenticated registration action '
'(<code>give_action=user_register</code>) that never consults the WordPress '
'<code>users_can_register</code> option</b> &mdash; so an attacker who needs an account can create one '
'<b>even where registration is switched off</b>. <b>The account requirement is real and it is also not '
'a barrier</b>, which is how a flaw needing a login still scores 10.0.</p>'
'<p><b>What makes it a default-configuration problem rather than an edge case.</b> On '
'<b>4.16.5.1 and below</b>, a <b>default installation is enough</b>: the plugin ships with an active '
'<b>manual (Test Donation)</b> gateway and an active <b>offline</b> gateway, and the attack needs only '
'<b>one published donation form</b>. &#9888; <b>Nothing fetched this run reports in-the-wild '
'exploitation, and it is not in CISA KEV</b> &mdash; listed here as <b>disclosed and patched</b>, not '
'as exploited. &#9888; <b>The 10.0 is the score carried in this reporting; no vendor advisory or NVD '
'record was in hand this run</b>, and this page has been burned by a blog score before.</p></div>')
h = h.replace(vanchor, vanchor + GIVE, 1)

# ------------------------------------------------ 5. CVE table row (GiveWP)
row_anchor = '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>'
assert row_anchor in h
NEWROW = (
'<tr><td><code>CVE-2026-82222</code></td><td>10.0 <span class="tag warn">reporting&rsquo;s figure</span></td>'
'<td>WordPress plugin <b>GiveWP</b>, versions <b>through 4.16.7.1</b></td>'
'<td><span class="tag new">New &middot; 1:12 PM</span> <b>Unauthenticated PHP object injection chained '
'to remote code execution.</b> <b>Fixed in 4.16.7.2 (released August 27.)</b> A <b>default install on '
'4.16.5.1 and below</b> is exploitable with <b>one published donation form</b>, via the shipped manual '
'and offline gateways; an <b>unauthenticated registration action</b> supplies the account the chain '
'needs even where registration is disabled. &#9888; <b>No vendor advisory or NVD record fetched this '
'run</b> &mdash; the 10.0 is this reporting&rsquo;s. &#9888; <b>No in-the-wild exploitation reported '
'and not KEV-listed.</b></td></tr>')
h = h.replace(row_anchor, row_anchor + NEWROW, 1)

# ---------------------------------------------------------- 6. KEV 24th check
kanchor = 'CISA KEV &amp; Federal Deadlines</h2>'
assert kanchor in h
KEV = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:12 PM</span> '
'<b>A twenty-fourth check, and for the seventeenth consecutive run nothing on CISA&rsquo;s catalog is '
'dated later than August 27.</b> This run&rsquo;s sweep returned CISA&rsquo;s own dated alert pages for '
'<b>August 18</b> (four: <b>CVE-2026-33824</b> Microsoft IKE Service Extensions double free, '
'<b>CVE-2026-55040</b> SharePoint weak authentication, <b>CVE-2026-59310</b> Broadcom VMware vCenter '
'path traversal, <b>CVE-2026-65400</b> Apple macOS improper authentication), <b>August 20</b> (two: '
'<b>CVE-2026-72529</b> and <b>CVE-2026-72530</b>, TrueConf Server missing authentication and code '
'injection), <b>August 24</b> (one: <b>CVE-2026-21962</b>, Oracle HTTP Server and WebLogic Server proxy '
'plug-in improper access control), <b>August 26</b> (six: <b>CVE-2015-3246</b> Red Hat libuser, '
'<b>CVE-2015-5287</b> Red Hat ABRT, <b>CVE-2019-1068</b> Microsoft SQL Server RCE, '
'<b>CVE-2021-23758</b> Ajax.NET Professional deserialization, <b>CVE-2022-0995</b> Linux kernel '
'out-of-bounds write, <b>CVE-2026-8452</b> Citrix NetScaler ADC and Gateway) and <b>August 27</b> '
'(three: <b>CVE-2023-49105</b> ownCloud, <b>CVE-2026-53362</b> Linux kernel, <b>CVE-2026-66384</b> '
'JFrog Artifactory). <b>Every identifier returned is already a row on this page.</b><br><br>'
'&#9888; <b>Countdowns are unchanged and the baseline stays Monday, August 31, 2026.</b> '
'<b>Four deadlines are past</b> &mdash; the <b>ownCloud / Linux kernel</b> pair now overdue, the '
'<b>Citrix NetScaler / SQL Server</b> pair two days past &mdash; and <b>nothing is pending until '
'September 9</b>, with <b>JFrog Artifactory (CVE-2026-66384) due September 10</b>. '
'&#9888; <b>No remediation date was offered by any page fetched this run and none is derived</b>: '
'BOD 22-01&rsquo;s three-week heuristic remains superseded here, and <b>every countdown on this page '
'comes from a date CISA stated</b>. <b>No August KEV total is certified</b> &mdash; the alert pages give '
'per-day counts, and adding them is arithmetic this page has not been able to check against a catalog '
'view.</div>')
h = h.replace(kanchor, kanchor + KEV, 1)

assert len(h) > orig
io.open(P, 'w', encoding='utf-8').write(h)
print('cyber-briefing.html %d -> %d bytes' % (orig, len(h)))
