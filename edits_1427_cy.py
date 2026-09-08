# -*- coding: utf-8 -*-
# Edition 2026-09-08 ~14:27 ET research / Midday. Cyber page edits.
import io, os, sys
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, "b_cyber.py")
s = io.open(p, encoding="utf-8").read()
n = 0

def rep(old, new):
    global s, n
    assert old in s, "MISSING: " + old[:90]
    s = s.replace(old, new, 1)
    n += 1

# ---------------- sources ----------------
rep(''' ("Help Net Security - Cybersecurity News and Expert Analysis", "https://www.helpnetsecurity.com/"),''',
    ''' ("Help Net Security - Cybersecurity News and Expert Analysis", "https://www.helpnetsecurity.com/"),
 ("Cyber Security News - Microsoft Patch Tuesday Update September 2026: 973 Vulnerabilities Fixed, Including 2 Zero-Days", "https://cybersecuritynews.com/microsoft-patch-tuesday-update-september-2026/"),
 ("SecurityOnline - September 2026 Patch Tuesday Fixes 2 Exploited Windows Zero-Days", "https://securityonline.info/patch-tuesday-zero-day-september-2026/"),
 ("ntcompatible - Microsoft September 2026 Patch Tuesday: 973 CVEs Fixed, 2 Actively Exploited Flaws Confirmed", "https://www.ntcompatible.com/story/microsoft-september-2026-patch-tuesday-973-cves-fixed-2-actively-exploited-flaws-confirmed"),
 ("Security Affairs - U.S. CISA adds PaperCut NG/MF flaws to its Known Exploited Vulnerabilities catalog", "https://securityaffairs.com/198200/security/u-s-cisa-adds-papercut-ng-mf-flaws-to-its-known-exploited-vulnerabilities-catalog.html"),
 ("gbhackers - CISA Flags Multiple PaperCut NG/MF Flaws Exploited in the Wild", "https://gbhackers.com/cisa-flags-multiple-papercut-ng-mf-flaws/"),
 ("Rapid7 - Critical SonicWall SMA1000 Vulnerabilities CVE-2026-83548, CVE-2026-83549 Exploited in the Wild", "https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild/"),
 ("Black Kite - 2026 Ransomware Report: 7,551 Victims, Up 24.9%", "https://blackkite.com/reports/2026-ransomware-report"),
 ("Tech.co - Data Breaches That Have Happened This Year (2026 Update)", "https://tech.co/news/data-breaches-updated-list"),''')

# ---------------- tldr ----------------
rep('''<div class="tldr"><b>The Wire</b> <span>An SSH authentication bypass in MikroTik RouterOS, chained for full administrative takeover and exploited in the wild since 2 September, is now the most urgent unpatched exposure on the internet-facing edge, with more than 122,000 devices showing exposed SSH interfaces.</span></div>''',
    '''<div class="tldr"><b>The Wire</b> <span>Microsoft&#39;s September Patch Tuesday shipped this afternoon and is the largest on record at 973 CVEs, two of which &mdash; both Windows privilege-escalation flaws &mdash; are already being exploited in the wild.</span></div>''')

# ---------------- banner + stats ----------------
rep('''<span class="lvl">Threat Level: High</span>
<span>Eight CVEs are under confirmed active exploitation as of today, an actively exploited router auth-bypass chain has more than 122,000 candidate targets, and three federal remediation deadlines fall inside the next ten days.</span>''',
    '''<span class="lvl">Threat Level: High</span>
<span>The largest Patch Tuesday Microsoft has ever shipped landed this afternoon carrying two already-exploited Windows zero-days; ten CVEs are under confirmed active exploitation; an actively exploited router auth-bypass chain still has more than 122,000 candidate targets; and three federal remediation deadlines fall inside the next ten days.</span>''')

rep('''<div class="stat"><div class="n">122,000+</div><div class="l">MikroTik devices with exposed SSH interfaces, the candidate target set for the MikroTrick chain</div></div>
<div class="stat"><div class="n">8</div><div class="l">CVEs showing confirmed active exploitation as of 8 September, including Kestra, Sangoma Switchvox, LiteLLM and Starlette</div></div>
<div class="stat"><div class="n">1,079,819</div><div class="l">People exposed in the Mathspace breach, all in Australia and New Zealand</div></div>
<div class="stat"><div class="n">410</div><div class="l">Ransomware incidents against U.S. healthcare organisations in H1 2026, up 14%</div></div>''',
    '''<div class="stat"><div class="n">973</div><div class="l">CVEs in Microsoft&#39;s September 2026 Patch Tuesday, described as its largest release to date</div></div>
<div class="stat"><div class="n">2</div><div class="l">Windows zero-days in that release confirmed exploited in the wild, both elevation-of-privilege flaws</div></div>
<div class="stat"><div class="n">10</div><div class="l">CVEs under active exploitation in a read taken this run, up from the eight this page carried earlier today</div></div>
<div class="stat"><div class="n">122,000+</div><div class="l">MikroTik devices with exposed SSH interfaces, the candidate target set for the MikroTrick chain</div></div>''')

# ---------------- top story ----------------
rep('''<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:20px">&ldquo;MikroTrick&rdquo;: attackers are taking full administrative control of MikroTik routers over SSH, and they started before the patch shipped</h3>''',
    '''<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:20px">Microsoft&#39;s September release shipped during this edition &mdash; 973 CVEs, the largest on record, and two of them are already being exploited</h3>
<p style="margin:0 0 10px">The release this briefing said at 11:44 a.m. and again at 1:50 p.m. had not yet been documented is now documented. Microsoft published its <b>September 2026 Patch Tuesday on 8 September</b>, addressing <b>973 vulnerabilities</b> across Windows, Office and server products &mdash; described in this run&#39;s reads as <b>its largest Patch Tuesday to date</b> &mdash; with <b>113 rated Critical</b>.</p>
<p style="margin:0 0 10px"><b>Two are confirmed exploited in the wild, and both are elevation-of-privilege flaws rather than remote code execution.</b> <b>CVE-2026-85880</b> affects the <b>Windows Advanced Local Procedure Call (ALPC)</b> component; Microsoft rates it Important and flags customer action as required. <b>CVE-2026-81963</b> is an Important-rated elevation-of-privilege flaw in the <b>Windows Update Stack</b>, caused by <b>improper link resolution before file access</b> &mdash; link following &mdash; which lets an already-authorised attacker escalate locally. One write-up read this run recommends patching <b>within 24 hours</b>. The updates to deploy are named as <b>KB5122871</b> and <b>KB5122876</b>.</p>
<p style="margin:0 0 10px"><b>What else is in it.</b> Microsoft&#39;s release notes are reported to attribute <b>723</b> of the fixes to Windows, <b>111</b> to Office, <b>62</b> to SQL, <b>22</b> to developer tools, <b>16</b> to SharePoint Server and <b>9</b> to Exchange Server. <span class="mut">Those figures sum to 943 of the stated 973, so the attribution read this run is partial rather than a complete breakdown; the gap is stated here rather than closed by assumption.</span> Critical remote-code-execution flaws in <b>DNS</b> and <b>Remote Desktop Services</b> also land this month, and <b>Windows Server 2012</b> and <b>Exchange 2016</b> are noted as approaching end of support.</p>
<p style="margin:0"><span class="mut">One vendor tracker page read this run gives the September release as &ldquo;9 CVEs, 9 Critical&rdquo;. That is irreconcilable with four independent reads giving 973, and reads as an unpopulated template, so it is refused rather than presented as a conflict of equals. No total other than 973 is printed.</span></p>
</div>

<h2 class="sec">Still Running: MikroTrick</h2>
<div class="panel" style="border-left:4px solid var(--accent2)">
<h3 style="margin:0 0 8px;font-size:20px">&ldquo;MikroTrick&rdquo;: attackers are taking full administrative control of MikroTik routers over SSH, and they started before the patch shipped</h3>''')

# ---------------- patch priority ----------------
rep('''<p style="margin:0 0 9px"><b>The most urgent item without a deadline: MikroTik RouterOS.</b>''',
    '''<p style="margin:0 0 9px"><b>Newly shipped and already exploited: Microsoft&#39;s two September zero-days.</b> <b>CVE-2026-85880</b> (Windows ALPC) and <b>CVE-2026-81963</b> (Windows Update Stack) are both elevation-of-privilege flaws confirmed under active exploitation, and both were fixed only this afternoon &mdash; which means every unpatched Windows estate has a live exploited weakness with a same-day fix available. Deploy <b>KB5122871</b> and <b>KB5122876</b>. <span class="mut">Neither is in the KEV catalog as of the last addition read this run, so no federal due date applies to them yet.</span></p>
<p style="margin:0 0 9px"><b>The most urgent item without a deadline: MikroTik RouterOS.</b>''')

# ---------------- new breach cards ----------------
rep('''<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Router</span></div>
<h3>MikroTik: exploitation confirmed in the wild</h3>''',
    '''<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">Financial</span></div>
<h3>AssetMark: around 570,000 individuals</h3>
<p><b>AssetMark, Inc.</b> has disclosed a data breach dating to <b>May 2026</b>, in which an unauthorised actor gained access to confidential information belonging to <b>around 570,000 individuals</b>. <span class="mut">The running 2026 breach index this appears in gives the scale, the month of the intrusion and the fact of disclosure. It does not name an attacker, a vector or the categories of data taken, so none of those is asserted here.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">Database</span></div>
<h3>&ldquo;PostGREShell&rdquo;: replication access becomes a permanent backdoor</h3>
<p><b>CVE-2026-6471</b>, dubbed <b>PostGREShell</b>, turns <b>low-level replication access</b> into <b>code execution</b>, <b>permanent superuser privileges</b> and a <b>persistent database backdoor</b>. The significance is the privilege jump: replication is routinely handed out as a restricted, low-trust role precisely because it is not supposed to be a path to the database&#39;s administrative account. <span class="mut">No CVSS score was stated in anything read this run, so none is printed, and the flaw is not in the KEV catalog. No in-the-wild exploitation was reported in this run&#39;s reads.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Trend</span></div>
<h3>7,551 publicly disclosed ransomware victims in 2026</h3>
<p>A 2026 ransomware report read this run counts <b>7,551 publicly disclosed victims</b> across the year, <b>up 24.9%</b> on the prior reporting period. <span class="mut">That is a count of victims named publicly on leak sites and in disclosures, not a count of attacks; the two differ, because unreported and unclaimed incidents never enter it. It sits alongside, and does not replace, the 410 U.S. healthcare incidents in the first half carried below.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Router</span></div>
<h3>MikroTik: exploitation confirmed in the wild</h3>''')

# demote previously-New cards
rep('''<div class="tags"><span class="t new">New</span><span class="t">Pattern</span></div>
<h3>Self-hosted Metabase is the common thread</h3>''',
    '''<div class="tags"><span class="t">Carried</span><span class="t">Pattern</span></div>
<h3>Self-hosted Metabase is the common thread</h3>''')
rep('''<div class="tags"><span class="t new">New</span><span class="t hot">Healthcare</span></div>
<h3>Healthcare ransomware up 14% in the first half</h3>''',
    '''<div class="tags"><span class="t">Carried</span><span class="t hot">Healthcare</span></div>
<h3>Healthcare ransomware up 14% in the first half</h3>''')

# ---------------- vuln table ----------------
rep('''<tr><td>CVE-2026-67276</td><td>9.2</td>''',
    '''<tr><td>CVE-2026-85880</td><td class="mut">not stated</td><td>Windows ALPC</td><td>Elevation of privilege. <b>Exploited in the wild</b>; fixed in the September 2026 Patch Tuesday. Microsoft rates it Important and flags customer action as required.</td></tr>
<tr><td>CVE-2026-81963</td><td class="mut">not stated</td><td>Windows Update Stack</td><td>Elevation of privilege via improper link resolution before file access (link following). <b>Exploited in the wild</b>; fixed in the September 2026 Patch Tuesday. Important-rated.</td></tr>
<tr><td>CVE-2026-6471</td><td class="mut">not stated</td><td>PostgreSQL (&ldquo;PostGREShell&rdquo;)</td><td>Escalates low-level replication access to code execution, permanent superuser privileges and a persistent backdoor. Not in KEV; no in-the-wild exploitation reported in this run&#39;s reads.</td></tr>
<tr><td>CVE-2026-67276</td><td>9.2</td>''')

# ---------------- KEV section ----------------
rep('''<li><b>PaperCut &mdash; CVE-2026-81578 and CVE-2026-82078.</b> Added to KEV <b>31 August</b>; remediation due <b>14 September</b>. <b class="down">(6 days left)</b></li>''',
    '''<li><b>PaperCut &mdash; CVE-2026-81578 and CVE-2026-82078.</b> Added to KEV <b>31 August</b>; remediation due <b>14 September</b>. <b class="down">(6 days left)</b> <span class="mut">Re-confirmed directly this run, with the flaw types now attached: CVE-2026-81578 is <b>missing authentication for a critical function</b> and CVE-2026-82078 is <b>unsafe reflection</b>, both in PaperCut NG/MF.</span></li>''')

rep('''<li><b>No KEV addition after 4 September surfaced in anything read this run</b>, so no fourth countdown has been invented.''',
    '''<li><b>No KEV addition after 4 September surfaced in anything read this run</b> &mdash; the CISA alert index was checked again this edition and the 4 September Chromium entry is still the most recent &mdash; so no fourth countdown has been invented.''')

# ---------------- Patch Tuesday section rewrite ----------------
rep('''<p style="margin:0 0 10px"><b>Microsoft&#39;s September 2026 release ships today, 8 September, at 1:00 PM ET</b> &mdash; effectively at the moment of this edition. <b>No September CVE count or zero-day detail had appeared in anything read this run, so none is printed here.</b> A count will appear in a later edition once the release is actually documented.</p>''',
    '''<p style="margin:0 0 10px"><b>The September count is in, and it is 973.</b> Microsoft&#39;s <b>8 September</b> release fixes <b>973 CVEs</b> with <b>113 rated Critical</b> and <b>two exploited zero-days</b>, <b>CVE-2026-85880</b> (Windows ALPC) and <b>CVE-2026-81963</b> (Windows Update Stack) &mdash; both elevation of privilege. Four independent reads this run give 973 and it is described as Microsoft&#39;s largest release to date. Full detail is in the Top Story above. <span class="mut">This briefing declined to print a September figure in its 11:21 a.m., 11:44 a.m. and 1:50 p.m. editions because the release had not been documented in anything read at those times; it is documented now, which is why a number appears here for the first time.</span></p>''')

rep('''<b>The August baseline is itself disputed, and the spread has widened this run.</b>''',
    '''<b>The August baseline remains disputed, and this month&#39;s number does not settle it.</b>''')

io.open(p, "w", encoding="utf-8").write(s)
print("cyber edits:", n)
