import io
P = "/sessions/beautiful-zealous-mendel/mnt/outputs/cyber-briefing.html"
s = io.open(P, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    c = s.count(old)
    assert c == 1, "count=%d for: %s" % (c, old[:110])
    s = s.replace(old, new); n += 1

# 1 — TLDR
rep("CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today, and a second federal deadline has now been verified right behind it — the actively exploited Citrix NetScaler flaw CVE-2026-8452 is due Saturday, August 29.",
    "CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today; the actively exploited Citrix NetScaler flaw behind it, CVE-2026-8452, is due Saturday and now carries a confirmed CVSS of 8.8 — and a second, separate NetScaler bug, a 9.3 authentication bypass, is patched but not yet reported exploited.")

# 2 — Threat-level banner
rep("A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and its federal remediation deadline lands today; a <i>second</i> federal deadline, for the actively exploited Citrix NetScaler flaw CVE-2026-8452, falls on Saturday; a maximum-severity unauthenticated RCE in Veeam ONE has been disclosed and patched; and a live intrusion at Boston Scientific has cut off the medical-device maker's ability to process and ship customer orders.",
    "A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and its federal remediation deadline lands today; a <i>second</i> federal deadline, for the actively exploited Citrix NetScaler flaw CVE-2026-8452 — now scored <b>8.8</b> — falls on Saturday, and a separate NetScaler authentication bypass rated <b>9.3</b> sits patched alongside it; a maximum-severity unauthenticated RCE in Veeam ONE has been disclosed and patched; a live intrusion at Boston Scientific has cut off the medical-device maker's ability to process and ship customer orders; and a single Aurora ransomware affiliate is now documented compromising more than 20 organisations across nine countries with an AI coding assistant in the loop.")

# 3 — stat strip: swap CareCloud stat for the Aurora one
rep('<div class="stat"><div class="n">3.7M</div><div class="l">People affected by the CareCloud breach — now the fifth-largest health-data theft of 2026 (TechCrunch, SecurityWeek)</div></div>',
    '<div class="stat"><div class="n">20+</div><div class="l">Organisations compromised across nine countries by one Aurora ransomware affiliate, April–July 2026 (GBHackers)</div></div>')

# 4 — Top Story closing paragraph: add score + IoCs
rep("it is now being exploited in the wild to plant <b>web shells</b>. Fixed builds are <b>14.1-72.61 (FIPS)</b>, <b>13.1-63.18</b> and <b>13.1-37.272</b>.",
    "it is now being exploited in the wild to plant <b>web shells</b> — observed intrusions drop files named <b><span class=\"mono\">x.php</span></b> and <b><span class=\"mono\">z.php</span></b> and run discovery commands such as <span class=\"mono\">id</span> and <span class=\"mono\">echo</span>. Fixed builds are <b>14.1-72.61 (FIPS)</b>, <b>13.1-63.18</b> and <b>13.1-37.272</b>. <b>Updated at 12:05 — the score is no longer blank:</b> SecurityWeek reports that Citrix itself assigned the flaw a <b>CVSS of 8.8</b> when it reported the issue at the end of June, so the \"not confirmed\" cell this page carried for four editions is now filled with a vendor figure rather than a blog's.")

# 5 — Patch Priority: add score
rep("is also confirmed exploited — for remote code execution as root, not merely the denial of service Citrix first described — and its federal deadline is <b>Saturday, August 29</b>, two days out.",
    "is also confirmed exploited — for remote code execution as root, not merely the denial of service Citrix first described — carries a vendor-assigned <b>CVSS 8.8</b>, and its federal deadline is <b>Saturday, August 29</b>, two days out.")

# 6 — Vulnerability Watch: fill the 8452 score, add 19490 row
rep('<tr><td class="mono">CVE-2026-8452</td><td class="mono">Not confirmed (high severity per SecurityWeek)</td>',
    '<tr><td class="mono">CVE-2026-8452</td><td class="mono">8.8 (assigned by Citrix)</td>')
rep("In KEV since Aug 26; federal due date <b>Aug 29</b>. No numeric CVSS confirmed this run.</td></tr>",
    "In KEV since Aug 26; federal due date <b>Aug 29</b>. Intrusions drop <span class=\"mono\">x.php</span> / <span class=\"mono\">z.php</span> web shells. Score confirmed at 12:05 (SecurityWeek).</td></tr>\n<tr><td class=\"mono\">CVE-2026-19490</td><td class=\"mono\" style=\"color:var(--crit)\">9.3 (CVSS v4.0)</td><td>Citrix NetScaler ADC / NetScaler Gateway configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA virtual server</td><td><b>New this run — a second, separate NetScaler flaw.</b> Authentication bypass via an alternate path (CWE-288); unauthenticated, network-reachable, low complexity, no user interaction. On builds 14.1-43.56+ and 13.1-61.28+ it is exploitable only where a <b>SAML action</b> is configured; on earlier builds any Gateway or AAA vserver exposes it. Advisory published <b>Aug 19, 2026</b>. <b>Rapid7 reported no evidence of in-the-wild exploitation as of Aug 19</b>, and it is not in the KEV additions verified this run — do not confuse it with CVE-2026-8452, which is exploited.</td></tr>")

# 7 — Aurora card, rewritten with the detail sourced this run
rep('<div class="card"><span class="tag crit">Ransomware</span><span class="tag">AI-assisted</span><span class="tag">Carried</span>\n<h3>Aurora ransomware affiliate used an AI coding assistant</h3><p><b>Aurora</b> ransomware has been tied to a <b>Russian-speaking affiliate</b> that used an <b>AI coding assistant</b> while targeting <b>more than 20 organisations</b>. <span style="color:var(--mut)">No victim names, sectors or ransom figures were stated in the reporting seen this run, so none are printed. (Cybersecurity News)</span></p></div>',
    '<div class="card" style="grid-column:1/-1"><span class="tag new">Updated · 12:05</span><span class="tag crit">Ransomware</span><span class="tag">AI-assisted</span>\n<h3>The Aurora affiliate story is now quantified: 20+ victims, nine countries, and an exposed server showing the whole workflow</h3><p>The single-affiliate case first carried here in one line is now documented in detail. A <b>Russian-speaking affiliate</b> of the <b>Aurora</b> ransomware operation compromised <b>more than 20 organisations across nine countries between April and July 2026</b>, using the AI coding assistant <b>Cursor</b> to plan intrusion activity and Active Directory escalation. The operator reached <b>domain-level or interactive access in at least 17 environments</b>, and <b>four victims were subsequently named on Aurora\'s public leak site</b>.<br><br>What makes the case unusual is the evidence: an <b>exposed server</b> held victim-specific directories, shell history, <b>Kerberos tickets</b>, credential dumps, Group Policy exports, <b>BloodHound</b> collections, custom tooling, <b>Cursor chat logs</b> and Aurora ransomware binaries — an end-to-end view of one affiliate\'s workflow from AI-supported planning through domain compromise to ransomware deployment and payment collection. <span style="color:var(--mut)"><b>One naming caveat is worth stating.</b> The reporting fetched this run names <b>Cursor</b> as the assistant in the logs, and that is what is printed. A separate aggregator headline seen in the same search attributes the case to a different AI coding tool; no primary reporting seen here supports that, so no second product is named. <b>No victim names, sectors or ransom figures are stated in the reporting seen this run, so none are printed.</b> (GBHackers, Cybersecurity News)</span></p></div>')

# 8 — Server Killers: note the second appearance
rep("Attribution to a named group is exactly the kind of claim that must come from the reporting on the incident, not from a general news roundup.",
    "Attribution to a named group is exactly the kind of claim that must come from the reporting on the incident, not from a general news roundup. <b>The same claim was returned again in this run's roundup search and is rejected a second time on the same grounds</b> — a claim does not become sourced by reappearing.")

io.open(P, "w", encoding="utf-8").write(s)
print("cyber edits applied:", n)
