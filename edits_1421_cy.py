# -*- coding: utf-8 -*-
P='/tmp/db_1787854887/cyber-briefing.html'
s=open(P,encoding='utf-8').read()
def rep(old,new,n=1):
    global s
    c=s.count(old); assert c==n, "count %d want %d :: %s"%(c,n,old[:100]); s=s.replace(old,new)

# demote stale edition tags
s=s.replace('<span class="tag new">Updated · 12:38</span>','<span class="tag">Carried · 12:38</span>')
s=s.replace('<span class="tag new">New · 12:38</span>','<span class="tag">Carried · 12:38</span>')

# tldr
rep("CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today &mdash; a bug a China-linked actor has used against governments in more than 100 countries &mdash; while the ATF has confirmed a &ldquo;major incident&rdquo; on a standalone system after Qilin claimed the agency, and a second CVE now shares Saturday's Citrix deadline."
 if "CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today &mdash;" in s else
 "CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today — a bug a China-linked actor has used against governments in more than 100 countries — while the ATF has confirmed a &ldquo;major incident&rdquo; on a standalone system after Qilin claimed the agency, and a second CVE now shares Saturday's Citrix deadline.",
 "CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today with the working day more than half gone — a bug a China-linked actor has used against governments in more than 100 countries — while researchers have disclosed a prompt-injection data-exfiltration path in Amazon's agentic IDE Kiro, the third AI developer tool to appear on this page today.")

# stat strip: swap the 20+ Aurora tile for the ITRC figure, keep Aurora detail on its card
rep('<div class="stat"><div class="n">20+</div><div class="l">Organisations compromised across nine countries by one Aurora ransomware affiliate, April–July 2026 (GBHackers)</div></div>',
    '<div class="stat"><div class="n">471.2M</div><div class="l">Data-breach victim notices in the first six months of 2026 — already above the 297.5M logged in all of 2025, a 58% jump in half the time (Identity Theft Resource Center)</div></div>')

# threat banner: add Kiro
rep('and the <b>ATF</b> has confirmed a &ldquo;',
    'researchers have disclosed a prompt-injection path for exfiltrating data from <b>Amazon Kiro</b>, an agentic AI IDE; and the <b>ATF</b> has confirmed a &ldquo;')

# new breach/incident card — Amazon Kiro
anchor='<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n'
card=('<div class="card"><span class="tag new">New · 2:21</span><span class="tag acc">AI tooling</span>\n'
 '<h3>A prompt-injection flaw in Amazon Kiro can exfiltrate data out of an agentic IDE</h3>'
 '<p><b>New at 2:21:</b> researchers have disclosed details of a vulnerability in <b>Amazon Kiro</b>, an AI-powered <b>agentic integrated development environment</b>, '
 'that could facilitate <b>data exfiltration via prompt injection</b> and <b>Kiro Powers</b> (The Hacker News). '
 '<span style="color:var(--mut)">No CVE identifier, severity score, affected version or patch status was stated in the reporting fetched this run, and none is printed here. '
 'This is the <b>third AI developer tool</b> to appear on this page today, alongside the Aurora affiliate\'s use of an AI coding assistant across 20+ intrusions and the '
 'earlier agent-tooling thread — but no source seen connects them, and no campaign is asserted. What they have in common is the shape of the problem: '
 'an agent that treats attacker-controlled text as instructions.</span></p></div>\n\n')
rep(anchor, anchor+card)

# Vulnerability Watch: two additions, both carefully hedged
vrow_anchor='<tr><td class="mono">CVE-2026-21962</td>'
newrows=('<tr><td class="mono">CVE-2026-45659</td><td class="mono">Not confirmed this run</td><td>Microsoft SharePoint Server</td>'
 '<td><b>New at 2:21.</b> Deserialization flaw described as actively exploited by ransomware operators <b>since early July 2026</b>: a low-privileged authenticated attacker submits a crafted '
 'serialization payload, gains execution as the IIS service account and steals machine keys, yielding token-based access that survives password resets. '
 '<span style="color:var(--mut)">No CVSS was stated in the source fetched this run and none is borrowed; not among the KEV additions verified this run.</span></td></tr>\n'
 '<tr><td class="mono">CVE-2026-58231</td><td class="mono">Not confirmed this run</td><td>SAP Commerce Cloud</td>'
 '<td><b>New at 2:21.</b> Reported exploited <b>within 72 hours of public disclosure</b>. '
 '<span style="color:var(--mut)">No CVSS, affected build or patch level was stated in the source fetched this run, so none is printed; not among the KEV additions verified this run.</span></td></tr>\n')
rep(vrow_anchor, newrows+vrow_anchor)

open(P,'w',encoding='utf-8').write(s); print("CY OK",len(s))
