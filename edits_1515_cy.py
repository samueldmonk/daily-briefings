# -*- coding: utf-8 -*-
p='cyber-briefing.html'
s=open(p,encoding='utf-8').read()
def rep(old,new,label):
    global s
    assert old in s, "NOT FOUND: "+label
    assert s.count(old)==1, "NOT UNIQUE: "+label
    s=s.replace(old,new,1); print("ok:",label)

# C1 tldr
rep("Australian police have charged two men over TeamPCP, the supply-chain campaign that poisoned the open-source scanners Trivy and Checkmarx KICS and the AI gateway LiteLLM and, the AFP alleges, exposed more than 1,000 organisations and 500,000 credentials — and CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today, with about two hours of the East Coast business day left.",
"CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today with roughly an hour of the East Coast business day left, and a second report has now put Saturday's Citrix NetScaler deadline on that flaw alone — contradicting the reporting this page has been carrying, which had Microsoft SQL Server sharing it.",
'C1 tldr')

# C2 KEV conflict
rep('<li><b class="mono">CVE-2019-1068</b> — <b>new this run.</b> Microsoft SQL Server, added <b>Aug 26</b>, due <b>Aug 29</b> — <span class="mono" id="kev5">(2 days left)</span>. Shares its deadline with the Citrix flaw above.</li>',
'<li><b class="mono">CVE-2019-1068</b> — Microsoft SQL Server, added <b>Aug 26</b>. <b>Its deadline is now in dispute, and the dispute is printed rather than resolved.</b> The Hacker News, fetched at 12:38, reported CISA ordering this flaw fixed by <b>August 29</b> alongside the Citrix bug, with the remaining four due September 9. <b>Infosecurity Magazine, fetched at 3:15, says something different:</b> that CISA is urging agencies to fix <span class="mono">CVE-2026-8452</span> by <b>August 29</b> and <b>the rest of the six — all five, this one included — by September 9</b>. <span class="mono" id="kev5">(Aug 29 = 2 days left)</span> <span style="color:var(--mut)">Two competent outlets, read off the same CISA entry, disagree about which bucket this CVE is in. This page keeps it listed against <b>August 29</b>, the earlier of the two dates, for one reason: if the earlier date is the right one, treating it as September 9 means missing a federal deadline, while if the later date is right, patching by Saturday costs nothing. <b>Neither source is discarded and neither is asserted as correct</b> — the row says which one says what, and a defender who needs certainty should read the KEV catalog entry itself.</span></li>',
'C2 KEV conflict')

# C3 ATF card update
rep('Qilin, first detected in <b>2022</b>, runs a double-extortion model and has claimed roughly <b>1,900 victims</b> over the past 18 months. <i>(BleepingComputer, Cybernews, The Hill)</i>',
'Qilin, first detected in <b>2022</b>, runs a double-extortion model and has claimed roughly <b>1,900 victims</b> over the past 18 months. <b>Updated at 3:15 — a second, larger count and a first name for the group.</b> BleepingComputer describes Qilin as a ransomware-as-a-service operation <b>first spotted in August 2022 under the name &ldquo;Agenda&rdquo;</b> that has since claimed <b>more than 2,200 victims</b> on its leak site. <span style="color:var(--mut)">The two counts are not the same measurement — 1,900 was scoped to the past eighteen months, 2,200+ is the lifetime total on the leak site — so they are <b>not in conflict and are not merged</b>; both are printed with the window each was given. Leak-site counts are the group&rsquo;s own claims in either case, not verified victim tallies, and are read accordingly. <b>The same reporting confirms Qilin added the ATF to its dark-web leak portal on Wednesday without saying whether it had taken files or demanded a ransom</b> — the claim of a breach and the proof of one remain separate things here.</span> <i>(BleepingComputer, Cybernews, The Hill)</i>',
'C3 ATF card')

# C4 new cards at top of Breaches
rep('<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n',
'<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n'
'<div class="card" style="grid-column:1/-1"><span class="tag new">New &middot; 3:15</span><span class="tag warn">Patch pace</span>\n'
'<h3>Microsoft warns that attackers are now moving faster than defenders can patch</h3>'
'<p><b>New at 3:15:</b> in coverage dated <b>August 27</b>, <b>Microsoft</b> warns that attackers are moving faster than security teams can apply fixes. '
'<span style="color:var(--mut)">It is a framing claim rather than a measured one, and no figure, study or timeframe accompanied it in the reporting fetched this run, so <b>none is printed</b>. '
'It is included because it is the through-line of this page today rather than a separate story: the Oracle proxy flaw had a patch available from <b>January 20</b> and CISA still had to set a '
'three-day federal deadline seven months later; four of the six CVEs in this week&rsquo;s KEV batch date from <b>2015 to 2022</b>. The gap Microsoft is describing is visible in the sections below.</span> '
'<i>(Cybernews)</i></p></div>\n',
'C4 microsoft card')

# C5 stat tile
rep('<div class="stat"><div class="n">471.2M</div>',
'<div class="stat"><div class="n">2,200+</div><div class="l">Victims Qilin has claimed on its leak site since 2022, the group now claiming the ATF (BleepingComputer)</div></div>\n<div class="stat"><div class="n">471.2M</div>',
'C5 stat tile')

# C6 banner retime
rep('A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and its federal remediation deadline lands today;',
'A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and its federal remediation deadline lands today, with roughly an hour of the business day left;',
'C6 banner')

# C7 sources
rep('<footer><b style="color:var(--ink)">Sources</b><ul class="bul"><li><b>Fetched 2:41 PM ET</b>',
'<footer><b style="color:var(--ink)">Sources</b><ul class="bul">'
'<li><b>Fetched 3:15 PM ET</b> — Infosecurity Magazine, <a href="https://www.infosecurity-magazine.com/news/cisa-kev-microsoft-citrix/">CISA Warns of Six Exploited Flaws in Microsoft, Linux and Citrix</a> — CVE-2026-8452 due Aug 29; the remaining five of the six due Sept 9, which conflicts with the Aug 29 date this page carries for CVE-2019-1068.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Help Net Security, <a href="https://www.helpnetsecurity.com/2026/08/27/netscaler-adc-gateway-cve-2026-8452/">Previously patched Citrix NetScaler flaw exploited in the wild (CVE-2026-8452)</a> — memory overflow reported by Citrix at the end of June at CVSS 8.8; unpredictable behaviour or denial of service where the appliance is configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA virtual server.</li>'
'<li><b>Fetched 3:15 PM ET</b> — BleepingComputer, <a href="https://www.bleepingcomputer.com/news/security/atf-confirms-major-incident-after-recent-qilin-breach-claims/">ATF confirms &ldquo;major incident&rdquo; after recent Qilin breach claims</a> — Qilin first spotted August 2022 as &ldquo;Agenda&rdquo;; 2,200+ victims claimed on its leak site; ATF added to the leak portal Wednesday with no file or ransom claim stated.</li>'
'<li><b>Fetched 3:15 PM ET</b> — SecurityWeek, <a href="https://www.securityweek.com/cisa-warns-of-exploited-oracle-weblogic-vulnerability/">CISA Warns of Exploited Oracle WebLogic Vulnerability</a> — CVE-2026-21962 added Aug 24, remediation ordered by Aug 27; CVSS 10; Oracle HTTP Server and the WebLogic Server Proxy plug-in.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Cybernews, <a href="https://cybernews.com/">Cyber Security News Today</a> — Microsoft warns attackers are moving faster than security teams can patch (Aug 27).</li>'
'<li><b>Fetched 2:41 PM ET</b>',
'C7 sources')

open(p,'w',encoding='utf-8').write(s)
print("WROTE",p,len(s))
