#!/usr/bin/env python3
"""Cyber content edits, 1:41 PM ET edition, Aug 31 2026."""
import io, re
p = 'cyber-briefing.html'
h = io.open(p, encoding='utf-8').read()

h = h.replace('<span class="tag new">New &middot; 1:12 PM</span>',
              '<span class="tag">Carried &middot; Aug 31, 1:12 PM</span>')

# ------------------------------------------------ Threat Actor Spotlight: Fire Ant
FIREANT = (
'<div class="card"><div class="tags"><span class="tag crit">New &middot; 1:41 PM</span>'
'<span class="tag">China-nexus espionage</span><span class="tag warn">Network infrastructure</span></div>'
'<h4>Fire Ant &mdash; an espionage actor that has moved off the endpoint and onto the plumbing</h4>'
'<p>A <b>China-nexus cyber espionage actor tracked as Fire Ant</b> has <b>expanded a campaign to compromise '
'Cisco IOS XR routers, Terminal Access Controller Access-Control System (TACACS) servers and Linux management '
'hosts</b>, according to reporting fetched this run.</p>'
'<p>&#9888; <b>The target list is the whole finding, and it is worth reading as a set rather than three items.</b> '
'A <b>router</b>, the <b>TACACS server that authenticates administrators to it</b>, and the <b>Linux hosts those '
'administrators manage it from</b> are the three points at which network access is granted rather than used. '
'<b>An actor holding all three does not need to hold an endpoint</b>, and none of the three is where endpoint '
'detection normally lives.</p>'
'<p>&#9888; <b>What is not published here:</b> no victim, no country, no intrusion count, no CVE and no initial '
'access vector returned in the reporting fetched this run, so <b>none is printed</b>. '
'<b>&ldquo;Expanded&rdquo; is the source&rsquo;s word and this page does not translate it into a number.</b></p></div>'
)
a1 = '>Threat Actor Spotlight</h2><div class="cards">'
assert a1 in h
h = h.replace(a1, a1 + FIREANT, 1)

# ------------------------------------------------ Breaches note
BR = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>Two malware findings arrived this run and they are opposite ends of the same trick: borrow something the '
'target already trusts.</b><br><br>'
'<b>Silver Fox is shipping ValleyRAT inside a signed application that is a real product.</b> Kaspersky reports the '
'actor distributing the <b>ValleyRAT backdoor disguised as a signed Chinese adware application</b>, with the '
'disguise built around <b>QN Wallpaper, a genuine Chinese desktop-wallpaper tool</b>. '
'&#9888; <b>The word doing the work is &ldquo;genuine&rdquo;.</b> A fake installer fails a reputation check; a real '
'one that happens to be adware passes every check a signature or a publisher name can perform, and the user who '
'installed it did want a wallpaper program. <b>No victim count, no geography beyond the lure&rsquo;s language and '
'no campaign dates returned; none printed.</b><br><br>'
'<b>Aurora ransomware operators are reported using an AI coding assistant as an intrusion tool.</b> Findings from '
'<b>CloudSEK</b> and <b>Gambit Security</b> describe Aurora operators <b>using the AI-powered coding assistant '
'Cursor to break into target networks</b>. '
'&#9888; <b>One descriptor in that reporting is refused and it is recorded below</b> &mdash; see Refused This Run. '
'&#9888; <b>No victims, no volumes, no ransom figures and no technical detail of how the assistant was used '
'returned; none printed.</b> <b>The claim published here is the one the two firms are quoted making, at the level '
'of specificity they made it.</b><br><br>'
'<b>Also returned, all already on this page as of earlier editions:</b> the <b>FulcrumSec claim of 86 GB from '
'Manchester Airports Group</b>, <b>Hasbro and McKesson tied to ShinyHunters</b>, the <b>ATF attack linked to Qilin '
'ransomware</b>, and the <b>GiveWP flaw fixed in 4.16.7.2</b>. <b>Every one a re-confirmation.</b></div>'
)
a2 = '>Breaches &amp; Incidents</h2>'
assert a2 in h
h = h.replace(a2, a2 + BR, 1)

# ------------------------------------------------ Refused This Run
REF = (
'<div class="card"><p><span class="tag new">New &middot; 1:41 PM</span> &#9888; '
'<b>&ldquo;SpaceX&rsquo;s AI-powered coding assistant Cursor&rdquo; &mdash; the ownership descriptor is refused, '
'the finding is not.</b> The same reporting that carries the CloudSEK and Gambit Security finding on '
'<b>Aurora ransomware operators using Cursor</b> attributes the product to <b>SpaceX</b>. '
'<b>Nothing fetched this run establishes who publishes Cursor</b>, and this page does not carry a corporate '
'attribution it has not sourced. <b>The tool name and the two research firms are printed; the vendor is not.</b>'
'<br><br>'
'&#9888; <b>Why the whole item was not dropped with the descriptor.</b> This page&rsquo;s standing practice is that '
'a wrong descriptor discredits the sentence it sits in, not every sentence around it &mdash; the same call made for '
'<b>&ldquo;ex-UFC title challenger&rdquo;</b> on the MMA page and for <b>&ldquo;former champion&rdquo;</b> before '
'that. <b>A misattributed publisher is a fact about a company; the intrusion finding is a fact about an actor, and '
'it is sourced to two named firms.</b> <b>The descriptor is struck and the finding stands, degraded to what its '
'sources actually said.</b></p></div>'
)
a3 = '>Refused This Run</h2>'
assert a3 in h
h = h.replace(a3, a3 + REF, 1)

# ------------------------------------------------ KEV
KEV = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>A twenty-fifth check, and for the eighteenth consecutive run nothing on CISA&rsquo;s catalog is dated later '
'than August 27.</b> This run&rsquo;s sweep returned CISA&rsquo;s own dated alert pages for <b>August 7</b> (one), '
'<b>August 11</b> (three), <b>August 18</b> (four), <b>August 20</b> (two) and <b>August 26</b> (six: '
'<b>CVE-2015-3246</b> Red Hat libuser race condition, <b>CVE-2015-5287</b> Red Hat ABRT privilege escalation, '
'<b>CVE-2019-1068</b> Microsoft SQL Server remote code execution, <b>CVE-2021-23758</b> Ajax.NET Professional '
'deserialization of untrusted data, <b>CVE-2022-0995</b> Linux kernel out-of-bounds write, <b>CVE-2026-8452</b> '
'Citrix NetScaler ADC and NetScaler Gateway improper restriction of operations within the bounds of a memory '
'buffer). <b>Every identifier returned is already a row on this page.</b><br><br>'
'&#9888; <b>The August 27 alert did not return this run and that is not evidence it went away.</b> The sweep '
'surfaced August 26 as the latest it reached; <b>seventeen prior runs reached August 27 directly</b>, and '
'<b>an omission from one search is not a retraction</b>. <b>The three August 27 identifiers stay as rows and the '
'&ldquo;nothing later than August 27&rdquo; framing is unchanged.</b><br><br>'
'&#9888; <b>Countdowns unchanged, baseline Monday, August 31:</b> four entries overdue, <b>nothing pending until '
'September 9</b>, and <b>JFrog Artifactory (CVE-2026-66384) due September 10</b>. '
'<b>No remediation date was offered by CISA in any page fetched this run and none is derived; the BOD 22-01 '
'three-week heuristic remains superseded on this page by stated dates only.</b> '
'<b>No August KEV total is certified</b> &mdash; per-day counts are given above and summing them would be '
'unchecked arithmetic.</div>'
)
a4 = 'CISA KEV &amp; Federal Deadlines</h2>'
assert a4 in h
h = h.replace(a4, a4 + KEV, 1)

# ------------------------------------------------ TLDR
new_tldr = (
'<div class="tldr"><b>The Wire</b> <span>Three new actors landed this run and none of them needed a new '
'vulnerability: <b>Fire Ant</b>, a China-nexus espionage group, has expanded onto <b>Cisco IOS XR routers, TACACS '
'servers and Linux management hosts</b> &mdash; the three places network access is granted rather than used; '
'<b>Silver Fox</b> is hiding the <b>ValleyRAT</b> backdoor inside a <i>genuine</i> signed Chinese wallpaper '
'application; and <b>Aurora</b> ransomware operators are reported using an AI coding assistant to break in, a claim '
'published here with its vendor attribution struck for want of a source.</span></div>'
)
h = re.sub(r'<div class="tldr">.*?</div>\s*(?=<div class="freshline")', new_tldr, h, count=1, flags=re.S)
assert 'Fire Ant</b>, a China-nexus' in h, 'tldr not replaced'

io.open(p, 'w', encoding='utf-8').write(h)
print('cyber edits applied,', len(h), 'bytes')
