import io
P='/sessions/optimistic-youthful-curie/mnt/outputs/cyber-briefing.html'
s=io.open(P,encoding='utf-8').read()
n=0
def R(old,new):
    global s,n
    c=s.count(old); assert c==1,('COUNT %d for: %s'%(c,old[:110]))
    s=s.replace(old,new); n+=1

# 1 — TLDR
R('<div class="tldr"><b>The Wire</b> <span>CISA\'s federal deadline to patch the maximum-severity Oracle WebLogic Proxy flaw CVE-2026-21962 — CVSS 10.0 and confirmed under active exploitation — expires today, August 27.</span></div>',
  '<div class="tldr"><b>The Wire</b> <span>CISA\'s deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today, and a second federal deadline has now been verified right behind it — the actively exploited Citrix NetScaler flaw CVE-2026-8452 is due Saturday, August 29.</span></div>')

# 2 — stat strip: swap the 7-month stat for the Citrix deadline
R('<div class="stat"><div class="n">7 mo</div><div class="l">Between Oracle\'s January patch and CISA spotting exploitation (The Stack)</div></div>',
  '<div class="stat"><div class="n">Aug 29</div><div class="l">Newly verified federal deadline for the exploited Citrix NetScaler flaw CVE-2026-8452 (BleepingComputer)</div></div>')

# 3 — Top story tag + a new paragraph on the second deadline
R('<span class="tag new">Updated · 9:35</span><span class="tag crit">Deadline today</span><span class="tag acc">KEV</span>',
  '<span class="tag new">Updated · 11:35</span><span class="tag crit">Deadline today</span><span class="tag acc">KEV</span>')
R('<p style="margin:0">A fix has existed since <b>January 20, 2026</b>, when Oracle disclosed and patched the issue in its January Critical Patch Update — roughly seven months before CISA flagged exploitation.</p>',
  '<p style="margin:0 0 10px">A fix has existed since <b>January 20, 2026</b>, when Oracle disclosed and patched the issue in its January Critical Patch Update — roughly seven months before CISA flagged exploitation.</p>\n'
  '<p style="margin:0"><b>New this run — a second deadline is now confirmed behind it.</b> For four editions this page reported the <b>August 26</b> KEV batch with <i>no</i> due date, because none had been verified. One now has been: CISA has ordered federal agencies to remediate <span class="mono">CVE-2026-8452</span> in <b>Citrix NetScaler ADC and NetScaler Gateway</b> by <b>Saturday, August 29</b>. Citrix patched the flaw on <b>June 30, 2026</b>, and initially assessed it as denial-of-service only; researchers at <b>watchTowr</b> subsequently demonstrated that successful exploitation can yield <b>remote code execution as root</b> on unpatched appliances, and it is now being exploited in the wild to plant <b>web shells</b>. Fixed builds are <b>14.1-72.61 (FIPS)</b>, <b>13.1-63.18</b> and <b>13.1-37.272</b>. <span style="color:var(--mut)">The three-day window is consistent with the per-CVE, risk-based dates BOD 26-04 replaced the old fixed three-week rule with.</span></p>')

# 4 — Patch Priority: name the runner-up
R('Inventory every Apache HTTP Server and Microsoft IIS instance running the WebLogic proxy plug-in — including the copies bundled inside Oracle HTTP Server — and apply the January 2026 Critical Patch Update.</p>',
  'Inventory every Apache HTTP Server and Microsoft IIS instance running the WebLogic proxy plug-in — including the copies bundled inside Oracle HTTP Server — and apply the January 2026 Critical Patch Update.<br><br><b>Then do Citrix.</b> <span class="mono">CVE-2026-8452</span> on <b>NetScaler ADC and NetScaler Gateway</b> is also confirmed exploited — for remote code execution as root, not merely the denial of service Citrix first described — and its federal deadline is <b>Saturday, August 29</b>, two days out. Patch to <b>14.1-72.61 (FIPS)</b>, <b>13.1-63.18</b> or <b>13.1-37.272</b>. It ranks second today only because Oracle\'s clock runs out first.</p>')

# 5 — new incident cards, inserted ahead of the Veeam card
R('<h3>Veeam patches a CVSS 10.0 unauthenticated RCE in Veeam ONE</h3>',
  'PLACEHOLDER_VEEAM')
R('PLACEHOLDER_VEEAM','<h3>Veeam patches a CVSS 10.0 unauthenticated RCE in Veeam ONE</h3>')

R('<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">',
  '''<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card"><span class="tag new">New · 11:35</span><span class="tag crit">Operational impact</span>
<h3>Boston Scientific cannot process or ship customer orders after an August 25 attack</h3><p>Medical-device maker <b>Boston Scientific</b> is investigating an <b>August 25</b> cyberattack that has disrupted operations across its global footprint. The company detected the intrusion on Monday; it triggered a network outage affecting <b>several IT operating systems and business applications</b>, and has cut off the company's ability to <b>process and ship customer orders</b>. Boston Scientific disclosed the incident in an <b>8-K filing with the SEC</b>, activated its incident response plan and is working with third-party cybersecurity experts. Thousands of staff at its <b>Irish plants</b> have been sent home to work remotely. The disruption is expected to continue, though the company has not said for how long. <b>Boston Scientific has named no attacker and no group has claimed the attack.</b> <span style="color:var(--mut)"><b>A claimed attribution was fetched this run and is not published:</b> one summary said the pro-Russian group "Server Killers" had claimed responsibility. A dedicated search of the primary coverage — Cybersecurity Dive, MedTech Dive, Healthcare Dive, Cybernews, HIPAA Journal — states explicitly that no group has claimed it. Attribution to a named group is exactly the kind of claim that must come from the reporting on the incident, not from a general news roundup. (Cybersecurity Dive, MedTech Dive, Cybernews)</span></p></div>

<div class="card"><span class="tag new">New · 11:35</span><span class="tag acc">Law enforcement</span>
<h3>Two charged in Australia over the TeamPCP supply-chain compromises</h3><p>The <b>Australian Federal Police</b> has charged two Western Australian men with <b>14 offences</b> over their alleged roles in <b>TeamPCP</b>, the group behind the <b>March 2026</b> compromise of the open-source security scanners <b>Trivy</b> and <b>Checkmarx KICS</b> and the AI gateway <b>LiteLLM</b>. <b>Louis Michael Gaebler, 23</b>, and <b>Ruben Ian Thomson, 21</b>, appeared in <b>Perth Magistrates Court on August 27, 2026</b> — today. <span style="color:var(--mut)">The charges are allegations; no plea or outcome is reported in the coverage seen this run, and none is implied here. (Cybersecurity News, Security Affairs)</span></p></div>
''')

# 6 — NemoClaw card gains real numbers
R('<h3>NVIDIA NemoClaw flaw can hijack an AI agent from a web page</h3><p>A critical vulnerability disclosed in <b>NVIDIA NemoClaw</b> could let an attacker hijack an AI agent after the victim simply visits a malicious website. <b>No CVE identifier or CVSS score was stated in the sources seen this run</b>, so none is printed. <span style="color:var(--mut)">(The Hacker News)</span></p></div>',
  '<h3>NVIDIA NemoClaw flaw can hijack an AI agent from a web page — and the advisory is now quantified</h3><p>A critical vulnerability disclosed in <b>NVIDIA NemoClaw</b> could let an attacker hijack an AI agent after the victim simply visits a malicious website. <b>New this run:</b> NVIDIA published <b>four advisories</b> this week, one of which covers <b>18 vulnerabilities in NemoClaw and OpenShell</b> — enterprise AI security and runtime products designed to wrap around autonomous AI agents. <b>Two of the 18 are rated critical</b> and can be exploited for code execution, privilege escalation, data tampering, information disclosure and denial of service. Adobe shipped patches in the same window, including <b>critical code-execution flaws</b> in Acrobat Reader, InDesign, InCopy, FrameMaker, Connect, Bridge, Photoshop and Illustrator. <span style="color:var(--mut)"><b>No CVE identifier or CVSS score is printed for the NemoClaw agent-hijack flaw</b> — none has been stated in any source seen across this run or the last. <b>No Adobe vulnerability count is printed either:</b> the sources this run give "51 across 5 products" and "55 across 11 products," and two counts that cannot both be right are not averaged into one. The publication day is also given as both Tuesday and August 26 in the same summary, so the page says "this week." (SecurityWeek, The Hacker News)</span></p></div>')

# 7 — Vulnerability Watch: Citrix row
R('<tr><td class="mono">CVE-2026-12569</td>',
  '<tr><td class="mono">CVE-2026-8452</td><td class="mono">Not confirmed (high severity per SecurityWeek)</td><td>Citrix NetScaler ADC / NetScaler Gateway with Gateway VPN or AAA virtual servers</td><td>Memory-overflow flaw. Citrix first assessed it as denial-of-service only; watchTowr demonstrated <b>RCE as root</b>, and it is exploited in the wild to deliver web shells. Patched by Citrix <b>Jun 30, 2026</b>; fixed in <b>14.1-72.61 (FIPS)</b>, <b>13.1-63.18</b>, <b>13.1-37.272</b>. In KEV since Aug 26; federal due date <b>Aug 29</b>. No numeric CVSS confirmed this run.</td></tr>\n<tr><td class="mono">CVE-2026-12569</td>')

# 8 — KEV board: Citrix bullet with countdown, and the Aug 26 batch line updated
R('<li><b class="mono">CVE-2026-60004</b> — Gitea remote code execution, fixed in 1.27.1. Due <b>Aug 28</b> — <span class="mono" id="kev2">(1 day left)</span>.</li>',
  '<li><b class="mono">CVE-2026-60004</b> — Gitea remote code execution, fixed in 1.27.1. Due <b>Aug 28</b> — <span class="mono" id="kev2">(1 day left)</span>.</li>\n'
  '<li><b class="mono">CVE-2026-8452</b> — <b>new deadline verified this run.</b> Citrix NetScaler ADC / NetScaler Gateway, added <b>Aug 26</b>, due <b>Aug 29</b> — <span class="mono" id="kev4">(2 days left)</span>. Exploited in the wild for RCE as root; patch to 14.1-72.61 (FIPS), 13.1-63.18 or 13.1-37.272.</li>')
R('Five of the six are legacy CVEs from 2015&ndash;2022, a reminder that KEV additions are driven by observed exploitation, not by disclosure date. No due dates verified this run.</li>',
  'Five of the six are legacy CVEs from 2015&ndash;2022, a reminder that KEV additions are driven by observed exploitation, not by disclosure date. <b>A due date for <span class="mono">CVE-2026-8452</span> — August 29 — has now been verified and is carried above; no due date is asserted for the other five.</b></li>')
R("set('kev1',d(2026,8,27));set('kev2',d(2026,8,28));set('kev3',d(2026,8,25));",
  "set('kev1',d(2026,8,27));set('kev2',d(2026,8,28));set('kev3',d(2026,8,25));set('kev4',d(2026,8,29));")
R('and no due date is inferred for the Aug 26, Aug 21, Aug 20, Aug 11 or Aug 7 additions.</li>',
  'and no due date is inferred for the remaining Aug 26, Aug 21, Aug 20, Aug 11 or Aug 7 additions. <b>The Aug 29 date now carried for <span class="mono">CVE-2026-8452</span> is different in kind:</b> it comes from reporting that states the CISA order directly, and its three-day shape matches the Aug 18 batch\'s.</li>')

io.open(P,'w',encoding='utf-8').write(s)
print('cyber edits applied:',n)
