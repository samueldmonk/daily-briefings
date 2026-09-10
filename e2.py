D='/sessions/youthful-laughing-hamilton/mnt/outputs/'
def edit(fn,pairs):
    p=D+fn;h=open(p).read()
    for old,new in pairs:
        assert h.count(old)==1, (fn,old[:80],h.count(old))
        h=h.replace(old,new)
    open(p,'w').write(h)

def addsrc(fn,urls):
    p=D+fn;h=open(p).read()
    marker='<footer><h5>Sources</h5>'
    assert h.count(marker)==1
    add=''.join(f'<div><a href="{u}">{u}</a></div>' for u in urls if u not in h)
    h=h.replace(marker,marker+add); open(p,'w').write(h)

addsrc('wallstreet-briefing.html',[
 'https://investrade.com/market-review-september-09-2026/',
 'https://finance.yahoo.com/quote/%5ERUT/history/',
 'https://tradingstrategyguides.com/stock-market-preview-september-9-2026-oil-at-100-takes-center-stage/',
 'https://www.schwab.com/learn/story/stock-market-update-open',
])

# ===================== CYBER =====================
CY='cyber-briefing.html'
veradigm=('<div class="card"><span class="t new">New</span><span class="t tag">Healthcare</span>'
 '<h4>Veradigm confirms patient data exposed through a third-party vendor &mdash; and a ransomware gang claims 3.5 million records</h4>'
 '<p>Healthcare technology company <b>Veradigm</b> disclosed on <b>8 September</b> that a cybersecurity incident <b>at one of its third-party vendors</b> exposed sensitive patient data, including <b>Social Security numbers</b>, for a subset of its customers. The route in was <b>stolen login credentials inside the vendor&rsquo;s environment</b>, which gave unauthorised access to a <b>Veradigm API used for service delivery</b>; the attacker used that narrow access point to download patient records. Veradigm says <b>no clinical or medical data</b> was compromised, has started incident-response procedures, notified law enforcement and is notifying affected customers and individuals with credit monitoring where applicable. The extortion group <b>The Gentlemen</b> claims to hold more than <b>3.5 million</b> patient records &mdash; names, contact information and Social Security numbers. <b>That figure is the attacker&rsquo;s claim, not the company&rsquo;s</b>, and the scope of the incident is still under investigation. It is the second story on this page in two days in which the victim organisation was reached through somebody else&rsquo;s credentials.</p></div>\n')

papercut=('<div class="card"><span class="t new">New</span><span class="t tag">AI-run intrusion</span>'
 '<h4>Hundreds of autonomous AI agents compromise 440 PaperCut servers across 48 countries</h4>'
 '<p>GreyNoise reports a <b>Russian-speaking threat actor</b> running <b>hundreds of autonomous AI agents</b> against <b>PaperCut NG/MF</b> print-management servers, compromising at least <b>440 servers across 395 organisations in 48 countries</b>. The infrastructure pivoted to two PaperCut flaws on <b>31 August 2026</b> &mdash; <b>CVE-2026-81578</b>, an authentication/access-control bypass, and <b>CVE-2026-82078</b>, an unsafe-reflection remote code execution flaw &mdash; from a single address, <b>45.142.193.132</b>, that GreyNoise had been flagging since <b>early July</b> for probing internet-facing Palo Alto, Ubiquiti, Citrix, SonicWall and Proxmox VE systems. The agents were paired with conventional offensive-security tooling to move from initial access to credential theft and <b>domain-level compromise in minutes</b>. PaperCut shipped an <b>Emergency Patch (Release 3)</b> on <b>1 September</b> for customers with internet-facing application servers who cannot apply other mitigations. Whether the actor means to sell access to ransomware affiliates or extort directly is <b>not known</b>; previous PaperCut exploitation has historically ended in ransomware. <b>Why it belongs at the top of this section:</b> every other intrusion on this page was driven by people at human speed.</p></div>\n')

edit(CY,[
 # stat strip swap
 ('<div class="stat"><div class="n">200,000+</div><div class="l">Florida driver records ShinyHunters claims to have taken from the DAVID system</div></div>',
  '<div class="stat"><div class="n">440</div><div class="l">PaperCut NG/MF servers compromised across 395 organisations in 48 countries by a campaign run by autonomous AI agents, per GreyNoise</div></div>'),
 # new cards
 ('<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n',
  '<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">\n'+papercut+veradigm),
 # tags note
 ('<div class="note" style="margin:18px 0 0"><b>On the tags.</b> The previous edition published at about 6:15 p.m. ET; research for this one ran from roughly 6:25 p.m. to 8:30 p.m. and it publishes after 8 p.m. <b>No new breach, advisory or KEV entry landed in that interval</b>, so <b>every card on this page is tagged Carried and not one is tagged New</b> &mdash; including the StyleSmuggler implants card, which was the single New card last edition. What did change is inside the top story: three further reads widened the affected-version range for CVE-2026-86218 and surfaced a date conflict, both of which are stated there. A card is not made New by the page being rebuilt around it.</div>',
  '<div class="note" style="margin:18px 0 0"><b>On the tags.</b> This is the sixth edition of this page today. <b>Two cards are genuinely new</b> &mdash; the AI-agent campaign against PaperCut and the Veradigm third-party breach, neither of which appeared in any earlier edition today &mdash; and <b>every other card is tagged Carried</b>, including the StyleSmuggler implants card that was New two editions ago. Nothing changed in the N-able top story in this interval: no new advisory, KEV entry or vendor statement landed, and the affected-version range and add-date conflict stand as written above. A card is not made New by the page being rebuilt around it.</div>'),
 # vuln rows
 ('<tr><td>CVE-2026-85046</td><td>not stated</td><td>Google Chromium V8</td><td>Type confusion. KEV-listed 4 September.</td></tr></table>',
  '<tr><td>CVE-2026-85046</td><td>not stated</td><td>Google Chromium V8</td><td>Type confusion. KEV-listed 4 September.</td></tr>\n'
  '<tr><td>CVE-2026-82078</td><td class="down"><b>9.4</b></td><td>PaperCut NG/MF</td><td><b>New to this table.</b> Unsafe dynamic class loading in the database connection utilities: the application instantiates database driver classes from configurable driver names <b>without validating them against an allowlist</b>, so attacker-controlled Java code can be loaded. Rated Critical. Actively exploited; KEV-listed <b>31 August 2026</b>. Chained behind CVE-2026-81578 in the campaign described above.</td></tr>\n'
  '<tr><td>CVE-2026-81578</td><td>8.8</td><td>PaperCut NG/MF</td><td><b>New to this table.</b> Improper access control in the web management interface &mdash; requests aimed at administrative functions trigger backend actions <b>before access validation completes</b>, giving unauthenticated attackers the ability to alter the configuration that CVE-2026-82078 then abuses. Rated High. Actively exploited; KEV-listed <b>31 August 2026</b>. PaperCut shipped Emergency Patch (Release 3) on 1 September.</td></tr></table>'),
 # KEV bullet
 ('<li><b>4 September &mdash; one added.</b> CVE-2026-85046, Google Chromium V8 type confusion. <span class="down"><b>No due date verified this run.</b></span></li>',
  '<li><b>4 September &mdash; one added.</b> CVE-2026-85046, Google Chromium V8 type confusion. <span class="down"><b>No due date verified this run.</b></span></li>\n'
  '<li><b>31 August &mdash; the two PaperCut flaws, added to this page tonight.</b> CVE-2026-81578 (CVSS 8.8) and CVE-2026-82078 (CVSS 9.4) were added to the KEV catalogue on <b>31 August 2026</b> and are described as actively exploited in the reporting read this run. <span class="down"><b>No federal due date was verified this run, so none is printed.</b></span> They fall outside the seven-day window counted below, which is why the volume figure there is unchanged.</li>'),
])
addsrc(CY,[
 'https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf',
 'https://cybersecuritynews.com/papercut-flaws-compromised-using-ai/',
 'https://horizon3.ai/attack-research/vulnerabilities/cve-2026-81578-cve-2026-82078/',
 'https://www.securityweek.com/papercut-exploitation-escalates-to-active-intrusions/',
 'https://cybersecuritynews.com/veradigm-patient-data-breach/',
 'https://www.securitymagazine.com/articles/102564-healthcare-tech-company-veradigm-exposed-in-third-party-breach',
 'https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/',
])
print('cyber ok')
