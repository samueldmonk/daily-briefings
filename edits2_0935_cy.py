#!/usr/bin/env python3
import io, sys
F = 'cyber-briefing.html'

def edit(tell, old, new, label):
    h = io.open(F, encoding='utf-8').read()
    if tell in h:
        print('skip (already applied):', label); return
    if old not in h:
        print('MISS ANCHOR:', label); sys.exit(1)
    h = h.replace(old, new, 1)
    io.open(F, 'w', encoding='utf-8').write(h)
    h2 = io.open(F, encoding='utf-8').read()
    assert tell in h2 and h2.count(tell) == 1, 'edit failed/duplicated: ' + label
    print('ok:', label)

# -------------------------------------------------- C2 New card, at the head of Breaches & Incidents
CARD = (
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t hot">Zero-day</span></div>\n'
'<h3>An MSP’s remote-control console is the fresh problem: N-able patches a pre-auth RCE in N-central, then '
'contradicts itself on whether it is being exploited</h3>\n'
'<p><b>Help Net Security reported this morning &mdash; the piece carries '
'<span style="font-family:var(--mono);font-size:12.5px">article:published_time 2026-09-07T11:55:57+00:00</span>, '
'07:55 ET, and was fetched directly this run &mdash; that N-able has shipped an emergency hotfix for '
'<b>CVE-2026-86218</b>, which its own release notes describe as a &ldquo;critical-CVSS-rated vulnerability that '
'could allow for pre-authenticated remote code execution on the N-central server.&rdquo;</b> N-central is N-able’s '
'remote monitoring and management platform, and its customers are largely <b>managed service providers</b> &mdash; '
'which is the whole weight of the story: the console that reaches every downstream client estate is the thing with '
'the pre-auth RCE in it. The fix landed on <b>5 September</b> as <b>Hotfix 4 for N-central 2026.3</b>, build '
'<b>2026.3.1.14</b>, with the instruction to &ldquo;upgrade &hellip; immediately.&rdquo;</p>\n'
'<p><b>The vendor tells two different stories, and this page prints both rather than picking one.</b> N-able’s '
'<b>public status-page advisory</b> says: &ldquo;At this time, we have no confirmations that this vulnerability has '
'been exploited in production environments, but unpatched systems remain at risk.&rdquo; A '
'<b>separate notice sent directly to customers</b>, marked urgent, says the flaw &ldquo;has been observed being '
'exploited in the wild&rdquo; and calls it a <b>zero-day</b>. Help Net Security states plainly that the customer '
'notice <b>contradicts the claims in the public advisory</b>. The customer notice lists both <b>hosted and '
'on-premises</b> deployments as impacted, across the <b>Americas, APAC and Europe</b>. Neither account is asserted '
'here as the truth; the more severe one is the safer planning assumption.</p>\n'
'<p><b>Huntress is the second party, and its account is carefully limited.</b> The firm flags CVE-2026-86218 as a '
'<b>potential</b> zero-day alongside two high-severity authentication-bypass flaws N-able patched over the same '
'weekend &mdash; <b>CVE-2026-86206</b> and <b>CVE-2026-86207</b> &mdash; which it says can give attackers '
'unrestricted access to the platform. Huntress had already seen one compromised N-central server in a customer’s '
'<i>patched</i> production environment, and says that because <b>the logs on it had already rotated</b> it cannot '
'determine which of the three CVEs was actually used. Huntress also says it learned of the flaw from a '
'<b>Discord post by an N-able employee</b> in the MSPGeek community, ahead of N-able’s own announcement. '
'N-able’s closing advice is to <b>audit N-central user accounts for unexpected users</b>. '
'<span class="mut">No numeric CVSS is published by the vendor for any of the three, so none is printed. None is '
'KEV-listed: a CISA-alert search this run again returned only the 2 and 4 September additions, and no 5, 6 or 7 '
'September addition exists.</span></p>\n'
'</div>\n'
)
edit('N-able patches a pre-auth RCE in N-central',
     '<div class="cards">\n<div class="card">\n<div class="tags"><span class="t hot">Exposure</span></div>\n',
     '<div class="cards">\n' + CARD + '<div class="card">\n<div class="tags"><span class="t hot">Exposure</span></div>\n',
     'C2 N-able card tagged New at the head of Breaches & Incidents')

# -------------------------------------------------- New-tag bookkeeping note (was stale and self-contradicting)
OLD_NOTE_START = '<b>One item is tagged New this edition, and the previous edition&rsquo;s tag has been stripped rather than left to decay.</b> The new card is the MikroTik exposure count below'
h = io.open(F, encoding='utf-8').read()
i = h.find(OLD_NOTE_START)
if i < 0 and 'the only card tagged New this edition is the N-able' not in h:
    print('MISS ANCHOR: New-tag note'); sys.exit(1)
if i >= 0:
    j = h.find('</p>', i) + 4
    NEW_NOTE = (
    '<b>One item is tagged New this edition: the N-able / N-central card below.</b> It qualifies on the plainest test '
    'this desk has &mdash; the tokens <b>N-able</b>, <b>N-central</b> and <b>86218</b> each grep to <b>zero</b> in '
    '<span style="font-family:var(--mono);font-size:12.5px">archive/cyber-2026-09-07-0917.html</span>, the previous '
    'edition, and its source was published at 07:55 ET this morning. The MikroTik exposure card carried the New tag in '
    'the 8:19 edition; that tag was correctly stripped at 9:17 and its content kept, and this note &mdash; which until '
    'now still described MikroTik as &ldquo;the new card&rdquo; while no New tag existed anywhere on the page &mdash; '
    'has been rewritten to match what is actually marked. <b>Cyber carries 1 New tag this edition; Wall Street 0; '
    'MMA 0.</b>'
    )
    h = h[:i] + NEW_NOTE + h[j-4:]
    io.open(F, 'w', encoding='utf-8').write(h)
    h2 = io.open(F, encoding='utf-8').read()
    assert 'the N-able / N-central card below' in h2
    assert h2.count('the N-able / N-central card below') == 1
    print('ok: New-tag bookkeeping note rewritten')

# -------------------------------------------------- tldr
h = io.open(F, encoding='utf-8').read()
if 'N-able shipped an emergency hotfix' in h:
    print('skip (already applied): tldr')
else:
    a = h.find('<div class="tldr">')
    b = h.find('</div>', a) + 6
    if a < 0: print('MISS ANCHOR: tldr'); sys.exit(1)
    NEW_TLDR = ('<div class="tldr"><b>The Wire</b> <span>N-able shipped an emergency hotfix on 5 September for a '
    'pre-authenticated remote code execution flaw in N-central, the remote-management console managed service '
    'providers use to reach every downstream customer, and then said two different things about it &mdash; its public '
    'advisory reports no confirmed exploitation while its urgent customer notice calls the bug a zero-day observed '
    'being exploited in the wild &mdash; while the Magento and Adobe Commerce zero-day StyleSmuggler is still '
    'backdooring stores with no CVE, no advisory and no vendor fix on its third day, Adobe&rsquo;s next scheduled '
    'security release is tomorrow, and five KEV entries are past their federal deadline.</span></div>')
    h = h[:a] + NEW_TLDR + h[b:]
    io.open(F, 'w', encoding='utf-8').write(h)
    assert 'N-able shipped an emergency hotfix' in io.open(F, encoding='utf-8').read()
    print('ok: tldr rewritten to lead on N-able')

# -------------------------------------------------- stats
edit('2026.3.1.14</div>',
     '<div class="stats">\n',
     '<div class="stats">\n'
     '<div class="stat"><div class="n">2026.3.1.14</div><div class="l">N-central build that carries Hotfix 4 for '
     'CVE-2026-86218 &mdash; released 5 September, per N-able via Help Net Security</div></div>\n'
     '<div class="stat"><div class="n">3</div><div class="l">N-central CVEs patched in one weekend &mdash; 86218 '
     '(pre-auth RCE) plus 86206 and 86207 (authentication bypass), per Huntress</div></div>\n',
     'stat strip: two N-able figures prepended')

# -------------------------------------------------- Sources
edit('helpnetsecurity.com/2026/09/07/n-able-n-central-hotfix-cve-2026-86218',
     '<h2 class="sec">Sources</h2>',
     '<h2 class="sec">Sources</h2>'
     '<a href="https://www.helpnetsecurity.com/2026/09/07/n-able-n-central-hotfix-cve-2026-86218/">Help Net Security '
     '&mdash; N-able patches critical N-central zero-day exploited in the wild, CVE-2026-86218 (7 Sep, 07:55 ET) '
     '&mdash; fetched directly this run</a> &nbsp;&middot;&nbsp; '
     '<a href="https://www.huntress.com/blog/n-able-vulnerability-exploitation">Huntress &mdash; N-able vulnerability '
     'exploitation (cited by Help Net Security; not fetched directly)</a> &nbsp;&middot;&nbsp; '
     '<a href="https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/">N-able status page '
     '&mdash; N-central 2026.3 Hotfix 4 advisory (cited by Help Net Security; not fetched directly)</a> '
     '&nbsp;&middot;&nbsp; ',
     'Sources: Help Net Security + Huntress + N-able status page')

print('--- cyber pass 2 done ---')
