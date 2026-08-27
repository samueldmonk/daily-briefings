# -*- coding: utf-8 -*-
import io
F='cyber-briefing.html'
s=io.open(F,encoding='utf-8').read()
def rep(old,new):
    global s
    n=s.count(old); assert n==1, "count=%d for %r"%(n,old[:90]); s=s.replace(old,new)

# 1 — TLDR
rep(u"<div class=\"tldr\"><b>The Wire</b> <span>CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today; the actively exploited Citrix NetScaler flaw behind it, CVE-2026-8452, is due Saturday and now carries a confirmed CVSS of 8.8 — and a second, separate NetScaler bug, a 9.3 authentication bypass, is patched but not yet reported exploited.</span></div>",
    u"<div class=\"tldr\"><b>The Wire</b> <span>CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today — a bug a China-linked actor has used against governments in more than 100 countries — while the ATF has confirmed a &ldquo;major incident&rdquo; on a standalone system after Qilin claimed the agency, and a second CVE now shares Saturday's Citrix deadline.</span></div>")

# 2 — stats strip: swap the 421 Patch Tuesday tile for the new CloudSEK figure, add ATF tile
rep(u'<div class="stat"><div class="n">421</div><div class="l">CVEs fixed in Microsoft\'s August 2026 Patch Tuesday, including one exploited zero-day (SecurityWeek)</div></div>',
    u'<div class="stat"><div class="n">140,000+</div><div class="l">Attack attempts against the Oracle proxy flaw logged by CloudSEK honeypots over 12 days, from 21 countries (TechTimes)</div></div>\n<div class="stat"><div class="n">100+</div><div class="l">Countries where a China-linked actor used CVE-2026-21962 among other bugs to deliver the SNOWLIGHT downloader (SOCRadar via TechTimes)</div></div>')

# 3 — Threat level banner: refresh for the ATF story
rep(u'and a single Aurora ransomware affiliate is now documented compromising more than 20 organisations across nine countries with an AI coding assistant in the loop.',
    u'a single Aurora ransomware affiliate is now documented compromising more than 20 organisations across nine countries with an AI coding assistant in the loop; and the <b>ATF</b> has confirmed a &ldquo;major incident&rdquo; on one of its systems after the Qilin ransomware group claimed the agency.')

# 4 — Top Story tag stamp + add the new attribution/scale paragraph
rep(u'<span class="tag new">Updated · 12:05</span><span class="tag crit">Deadline today</span><span class="tag acc">KEV</span>',
    u'<span class="tag new">Updated · 12:38</span><span class="tag crit">Deadline today</span><span class="tag acc">KEV</span>')

rep(u'A fix has existed since <b>January 20, 2026</b>',
    u'<b>New at 12:38 — who is using it, and how hard.</b> <span class="mono">CVE-2026-21962</span> is among several vulnerabilities a <b>China-linked threat actor</b> has exploited against government and commercial infrastructure across <b>more than 100 countries</b> to deliver the <b>SNOWLIGHT</b> downloader; SOCRadar reported in <b>July</b> that the flaw was already in that actor\'s toolkit against government targets. Separately, a <b>CloudSEK</b> honeypot study recorded <b>more than 140,000 attack attempts</b> from <b>21 countries</b> over a <b>12-day</b> window. <span style="color:var(--mut)">Both figures come from reporting fetched this run and are attributed rather than merged; no link is asserted between the honeypot traffic and the named actor, because no source seen makes one.</span></p>\n<p style="margin:0 0 10px">A fix has existed since <b>January 20, 2026</b>')

# 5 — KEV list: second CVE on the Aug 29 deadline + Sept 9 for the rest
rep(u'<b>A due date for <span class="mono">CVE-2026-8452</span> — August 29 — has now been verified and is carried above; no due date is asserted for the other five.</b></li>',
    u'<b>New at 12:38 — the rest of the batch now has dates too.</b> The Hacker News reports that CISA has told FCEB agencies to fix <b><span class="mono">CVE-2019-1068</span> (Microsoft SQL Server)</b> and <b><span class="mono">CVE-2026-8452</span></b> by <b>August 29</b>, and <b>the remaining four by September 9</b>. So two of the six share Saturday\'s deadline, not one. <span style="color:var(--mut)">The four dated to September 9 are <span class="mono">CVE-2015-3246</span>, <span class="mono">CVE-2015-5287</span>, <span class="mono">CVE-2021-23758</span> and <span class="mono">CVE-2022-0995</span> (Linux kernel). Both windows are longer than the three days assigned to the Oracle flaw and shorter than the retired flat three-week rule — which is what per-CVE risk-based dating under BOD 26-04 looks like in practice.</span></li>\n<li><b class="mono">CVE-2019-1068</b> — <b>new this run.</b> Microsoft SQL Server, added <b>Aug 26</b>, due <b>Aug 29</b> — <span class="mono" id="kev5">(2 days left)</span>. Shares its deadline with the Citrix flaw above.</li>')

rep(u"set('kev4',d(2026,8,29));",
    u"set('kev4',d(2026,8,29));set('kev5',d(2026,8,29));set('kev6',d(2026,9,9));")

# 6 — Patch Priority: name the second Aug 29 CVE
rep(u'It ranks second today only because Oracle\'s clock runs out first.',
    u'It ranks second today only because Oracle\'s clock runs out first. <b>New at 12:38:</b> Citrix no longer has Saturday to itself — <span class="mono">CVE-2019-1068</span> in <b>Microsoft SQL Server</b> carries the <b>same August 29 date</b>, and the four other CVEs from that batch are due <b>September 9</b> — <span class="mono" id="kev6">(13 days left)</span>.')

# 7 — Breaches: insert ATF and Nutex cards at the top of the section
rep(u'<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n<div class="card"><span class="tag">Carried</span><span class="tag crit">Operational impact</span>',
    u'<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n'
    u'<div class="card"><span class="tag new">New · 12:38</span><span class="tag crit">Federal</span>\n'
    u'<h3>The ATF confirms a &ldquo;major incident&rdquo; after Qilin claimed the agency</h3>'
    u'<p>The <b>Bureau of Alcohol, Tobacco, Firearms and Explosives</b> has confirmed that one of its systems was compromised, days after the <b>Qilin</b> ransomware group publicly claimed an attack on the agency on <b>August 26</b>. In a press release, the ATF described a breach of a <b>standalone system</b> as a <b>&ldquo;major incident&rdquo;</b> and said it is investigating in collaboration with the <b>Department of Justice</b>. The agency states the affected system operates separately from the ATF enterprise network and that there is <b>no indication</b> the enterprise network, the <b>ATF eForms</b> system or any other ATF system was affected. '
    u'<span style="color:var(--mut)">Sources inside the agency told reporters the attackers obtained <b>investigative tools and other operational files</b> and that <b>gun-owner information was not compromised</b> — that account is attributed, not asserted. Federal authorities have <b>not</b> disclosed when the breach occurred, how the network was penetrated, or whether data was successfully exfiltrated, and none of those is inferred here.</span> '
    u'Qilin, first detected in <b>2022</b>, runs a double-extortion model and has claimed roughly <b>1,900 victims</b> over the past 18 months. <i>(BleepingComputer, Cybernews, The Hill)</i></p></div>\n'
    u'<div class="card"><span class="tag new">New · 12:38</span><span class="tag warn">Healthcare</span>\n'
    u'<h3>Nutex Health says data was accessed and exfiltrated from its servers</h3>'
    u'<p><b>Nutex Health</b>, a publicly traded operator of <b>28 facilities across 12 US states</b>, disclosed a cybersecurity incident in an <b>8-K</b> filed <b>August 24, 2026</b>. The company says an unauthorised third party <b>accessed and exfiltrated</b> information held on its servers, including material that may be private or confidential. It has engaged an independent response team and forensic experts, activated its response plan, implemented containment measures and notified law enforcement. '
    u'<span style="color:var(--mut)"><b>No group has claimed the attack</b>, though the disclosure raises the possibility the attacker may leak what was taken. The company reports <b>no material impact</b> on business operations or financial reporting systems to date. The scope and the number of affected individuals are not yet known, and no count is printed here.</span> <i>(BleepingComputer, SecurityWeek, SEC 8-K)</i></p></div>\n'
    u'<div class="card"><span class="tag">Carried</span><span class="tag crit">Operational impact</span>')

io.open(F,'w',encoding='utf-8').write(s)
print("CY OK")
