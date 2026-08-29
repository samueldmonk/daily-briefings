import re, io, sys

def rd(p): return io.open(p, encoding='utf-8').read()
def wr(p, s): io.open(p, 'w', encoding='utf-8').write(s)

def sub1(s, old, new, label):
    assert s.count(old) == 1, "ANCHOR %s count=%d" % (label, s.count(old))
    return s.replace(old, new)

# ---------------- CYBER ----------------
cy = rd('cyber-briefing.html')

SN_ROWS = u'''<tr><td><b>CVE-2026-18885</b></td><td class="critc">10.0</td><td>ServiceNow &mdash; GraphQL Composite Data API (Xanadu, Yokohama, Zurich)</td>
<td><b>New &middot; 1:05 PM.</b> Code injection permitting an <b>unauthenticated</b> user to <b>execute arbitrary code</b>
and access or modify instance data. Disclosed in ServiceNow&rsquo;s <b>August 27, 2026</b> advisory batch.
<b>ServiceNow states it is &ldquo;not currently aware of exploitation&rdquo; of any flaw in this batch</b>, and none of them is
KEV-listed &mdash; the CVSS 10.0 and the <b>no-authentication, no-user-interaction, low-complexity</b> profile are the
reason this row exists, not exploitation. Customers on ServiceNow&rsquo;s Patching Program received the fix automatically
on hosted instances; <b>self-hosted customers must apply it themselves</b>, which is where the exposure will sit.</td></tr>
<tr><td><b>CVE-2026-18886</b></td><td class="critc">10.0</td><td>ServiceNow &mdash; system configuration image upload processor</td>
<td><b>New &middot; 1:05 PM.</b> Improper access control enabling <b>privilege escalation</b>. Same August 27 batch,
same patch route, same <b>not-exploited / not-KEV</b> status as the two rows either side of it.</td></tr>
<tr><td><b>CVE-2026-74820</b></td><td class="critc">10.0</td><td>ServiceNow &mdash; dynamic schema ORDER BY clause</td>
<td><b>New &middot; 1:05 PM.</b> <b>SQL injection</b> allowing <b>unauthenticated</b> users to execute arbitrary SQL
against the instance&rsquo;s underlying database. Same August 27 batch; <b>not exploited, not KEV-listed</b>.</td></tr>
<tr><td><b>CVE-2026-6876</b></td><td class="warnc">8.7</td><td>ServiceNow Now Platform &mdash; sandbox escape</td>
<td><b>New &middot; 1:05 PM. The fourth flaw in the batch, and the one that carries a trap.</b>
Reported as a <b>sandbox escape</b> allowing an unauthenticated user to execute arbitrary code, <b>CVSS 8.7</b>, patched
alongside the three above. &#9888; <b>It is one digit away from a different vulnerability with the opposite status.</b>
<b>CVE-2026-6875</b> &mdash; also a ServiceNow sandbox escape, in the <b>AI Platform</b>, <b>CVSS 9.8</b>, reported to the
vendor on <b>April 1</b> by Searchlight Cyber &mdash; <b>is</b> confirmed exploited in the wild, in reporting from
<b>July 2026</b>. <b>6875 is exploited and old; 6876 is new and not exploited.</b> This page prints both so the pair
cannot be collapsed into one item, and <b>does not carry 6875 as a row</b>, because it is a July story and no source seen
this run states current activity against it. A vendor knowledge-base page fetched this run is titled for <b>6875</b>
while trade reporting on the August batch names <b>6876</b>; the discrepancy is <b>recorded, not resolved</b>.</td></tr>
'''

cy = sub1(cy,
  u'<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n',
  u'<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n' + SN_ROWS,
  'cve-table-header')

# cyber tldr
OLD_CY_T = u'McKesson has told the SEC it discovered a cybersecurity incident on August 25'
NEW_CY_T = (u'ServiceNow has patched <b>three separate CVSS 10.0 flaws</b> disclosed on August 27 &mdash; unauthenticated '
 u'code execution, privilege escalation and SQL injection, all exploitable without credentials or user interaction &mdash; '
 u'and says it is not aware of any of them being exploited, which matters because a fourth flaw in the same batch sits '
 u'one digit away from a ServiceNow vulnerability that <i>is</i> exploited: <b>CVE-2026-6876</b> is new and not exploited, '
 u'<b>CVE-2026-6875</b> is a July story and confirmed exploited, and this page prints both rather than let the pair be '
 u'read as one; separately, McKesson has told the SEC it discovered a cybersecurity incident on August 25')
cy = sub1(cy, OLD_CY_T, NEW_CY_T, 'cyber-tldr')

# freshline
cy = cy.replace(u'Data as of 12:35 PM ET', u'Data as of 1:05 PM ET')

SN_SRC = (u'<a href="https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html">The Hacker News &mdash; Three CVSS 10.0 ServiceNow flaws</a><br>'
 u'<a href="https://www.bleepingcomputer.com/news/security/servicenow-warns-of-three-max-severity-security-vulnerabilities/">BleepingComputer &mdash; ServiceNow warns of three max severity vulnerabilities</a><br>'
 u'<a href="https://www.csoonline.com/article/4215430/servicenow-patches-three-maximum-severity-flaws-that-could-put-enterprise-data-at-risk.html">CSO Online &mdash; ServiceNow patches three maximum-severity flaws</a><br>'
 u'<a href="https://support.servicenow.com/kb?id=kb_article_view&amp;sysparm_article=KB3152242">ServiceNow &mdash; August 2026 CVE Advisory Notification</a><br>'
 u'<a href="https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/">BleepingComputer &mdash; Critical ServiceNow code execution flaw now exploited (CVE-2026-6875, July)</a><br>'
 u'<a href="https://arcticwolf.com/resources/blog/cve-2026-6875/">Arctic Wolf &mdash; CVE-2026-6875 ServiceNow AI Platform RCE</a><br>'
 u'<a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA &mdash; Six KEV additions, August 26 2026</a><br>')
cy = sub1(cy, u'Sources checked this run:</b><br>', u'Sources checked this run:</b><br>' + SN_SRC, 'cyber-sources')
wr('cyber-briefing.html', cy)

# ---------------- MARKETS ----------------
ws = rd('wallstreet-briefing.html')
OLD_W = u're-verified an eleventh time this run'
NEW_W = u're-verified a twelfth time this run, the second consecutive check to return all three levels and all three percentage moves together,'
ws = ws.replace(OLD_W, NEW_W, 1)
assert NEW_W in ws, 'markets-tldr'
ws = ws.replace(u'Data as of 12:35 PM ET', u'Data as of 1:05 PM ET')
wr('wallstreet-briefing.html', ws)

# ---------------- MMA ----------------
mma = rd('mma-briefing.html')
mma = mma.replace(u'Data as of 12:35 PM ET', u'Data as of 1:05 PM ET')
wr('mma-briefing.html', mma)

# ---------------- INDEX ----------------
ix = rd('index.html')
ix = ix.replace(u'Data as of 12:35 PM ET', u'Data as of 1:05 PM ET')
ix = sub1(ix, OLD_CY_T, NEW_CY_T, 'index-cyber-card')
ix = ix.replace(OLD_W, NEW_W, 1)
assert NEW_W in ix, 'index-markets-card'
wr('index.html', ix)
print("EDITS OK")
