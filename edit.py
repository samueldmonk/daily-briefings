import io,sys

def sub(path, old, new, count=1):
    s = io.open(path, encoding='utf-8').read()
    if s.count(old) < count:
        print("MISS in %s: %r" % (path, old[:70])); sys.exit(1)
    s = s.replace(old, new, count)
    io.open(path,'w',encoding='utf-8').write(s)

C='cyber-briefing.html'; W='wallstreet-briefing.html'; M='mma-briefing.html'; I='index.html'

# ---- CYBER ----
sub(C, "The Cl0p ransomware gang is raiding internet-exposed PTC Windchill and FlexPLM servers for engineering data through CVE-2026-12569 — a flaw patched since June whose federal fix deadline is nearly a month past — while Australia's Origin Energy confirms a breach at a retailer serving 4.8 million customers.",
 "Two federal patch deadlines land today — the actively exploited Microsoft SharePoint RCE CVE-2026-50522 and the Check Point SmartConsole zero-day CVE-2026-16232, both KEV-listed July 22 on three-day windows — while Cl0p keeps looting engineering data from exposed PTC Windchill and FlexPLM servers.")

sub(C, '<span class="lvl">Elevated</span>\n  <p>A named ransomware crew is actively mass-exploiting a KEV-listed PLM flaw whose federal deadline passed in June, several other KEV deadlines are already overdue, and a major energy retailer is working through a confirmed customer-data breach.</p>',
 '<span class="lvl" style="color:var(--crit);border-color:var(--crit)">High</span>\n  <p>Federal fix deadlines for two actively exploited flaws — the SharePoint RCE fueling a month-long attack wave and a Check Point SmartConsole zero-day — land today, while Cl0p\'s PLM data-theft campaign and several already-overdue KEV deadlines keep defenders behind the clock.</p>')

sub(C, '<div class="stat"><div class="n">146</div><div class="l">Active ransomware/extortion groups by June 2026 (Help Net Security)</div></div>\n  <div class="stat"><div class="n">61</div><div class="l">New ransomware groups that entered the market Apr 2025–Mar 2026 (Help Net Security)</div></div>',
 '<div class="stat"><div class="n">2</div><div class="l">Federal KEV fix deadlines that land today, Jul 25 — SharePoint CVE-2026-50522 and Check Point CVE-2026-16232 (CISA alerts/Help Net Security)</div></div>\n  <div class="stat"><div class="n">9.8</div><div class="l">CVSS of SharePoint CVE-2026-50522, exploited within hours of the Jul 20 public PoC (The Hacker News)</div></div>')

old_top = s = None
import re
txt = io.open(C,encoding='utf-8').read()
start = txt.index('<div class="panel top">'); end = txt.index('</div>', txt.index('<strong>Defender takeaway:</strong>'))+len('</div>')
new_top = '''<div class="panel top">
  <h3>Deadline day: fixes for the exploited SharePoint RCE and the Check Point SmartConsole zero-day come due today</h3>
  <p>CISA added two flaws to the Known Exploited Vulnerabilities catalog on July 22 and gave federal civilian agencies just three days — both fixes are due <strong>today, July 25</strong> (CISA/The Hacker News/Help Net Security). The first, CVE-2026-50522, is a CVSS 9.8 deserialization flaw in on-premises Microsoft SharePoint Server: a public proof-of-concept dropped July 20 and exploitation began within hours, with attackers executing code and stealing ASP.NET machine keys from on-prem servers. SecurityWeek counts it as the fourth SharePoint vulnerability exploited in the past month's wave of attacks against on-prem deployments (The Hacker News/CISO Platform/SecurityWeek/Resecurity).</p>
  <p>The second, CVE-2026-16232, was exploited as a zero-day against what Check Point calls "a small number of customers": an unauthenticated remote attacker who can reach a management server's IP — in environments that don't restrict Trusted Clients — can obtain an application login token and authenticate to the management server with full administrative privileges, enough to rewrite security policies and configurations. Check Point shipped fixes on July 22 as part of its Jumbo Hotfix release (BleepingComputer/Help Net Security/Rapid7).</p>
  <p><strong>Defender takeaway:</strong> patch on-prem SharePoint now and hunt for stolen machine keys — they survive patching and enable forged authentication later; apply Check Point's Jumbo Hotfix and restrict Trusted Clients on management servers. And if you run PTC Windchill/FlexPLM, Cl0p is still working through the internet-exposed stragglers (see spotlight below).</p>
</div>'''
txt = txt[:start] + new_top + txt[end:]
io.open(C,'w',encoding='utf-8').write(txt)

sub(C, '<h4>⚠ Patch now — actively exploited, deadline long past</h4>\n  <p>1) <strong>PTC Windchill/FlexPLM CVE-2026-12569</strong> — CVSS 9.3 pre-auth RCE now under mass exploitation by Cl0p; KEV-listed with a federal due date of <strong>Jun 28</strong>, now 27 days overdue. Patch per PTC advisory CS473270 and hunt for web shells. 2) <strong>Microsoft AD FS CVE-2026-56155</strong> (CVSS 7.8 EoP) — the one KEV deadline still ahead: FCEB due <strong>Jul 28</strong>, 3 days left.</p>',
 '<h4>⚠ Patch now — two federal deadlines land TODAY</h4>\n  <p>1) <strong>Microsoft SharePoint CVE-2026-50522</strong> — CVSS 9.8 deserialization RCE, exploited within hours of the Jul 20 public PoC with machine-key theft observed; KEV-listed Jul 22, FCEB fixes due <strong>TODAY, Jul 25</strong>. Patch and rotate/hunt stolen ASP.NET machine keys. 2) <strong>Check Point SmartConsole CVE-2026-16232</strong> — exploited zero-day auth bypass yielding full admin on management servers; Jumbo Hotfix shipped Jul 22; also due <strong>TODAY, Jul 25</strong>. Still ahead: Microsoft AD FS CVE-2026-56155 (CVSS 7.8 EoP), due <strong>Jul 28</strong> — 3 days left. Long past: PTC Windchill/FlexPLM CVE-2026-12569 (due Jun 28, 27 days overdue) remains under mass exploitation by Cl0p.</p>')

sub(C, '<tr><td>CVE-2026-58644</td><td class="cvss">9.8</td><td>Microsoft SharePoint (on-prem)</td><td>Unauthenticated deserialization RCE; KEV Jul 16, FCEB due Jul 19; part of the actively exploited SharePoint chain.</td></tr>',
 '''<tr><td>CVE-2026-50522</td><td class="cvss">9.8</td><td>Microsoft SharePoint (on-prem)</td><td>Deserialization RCE; public PoC Jul 20, exploited within hours incl. ASP.NET machine-key theft; KEV Jul 22, FCEB due Jul 25 — today.</td></tr>
  <tr><td>CVE-2026-16232</td><td class="cvss">9.1–9.3</td><td>Check Point SmartConsole</td><td>Auth bypass → full admin on the management server; exploited as a zero-day; fixed in the Jul 22 Jumbo Hotfix; KEV due Jul 25. Outlets report CVSS 9.1–9.3 — check the vendor advisory.</td></tr>
  <tr><td>CVE-2026-6875</td><td class="cvss">9.5</td><td>ServiceNow AI Platform</td><td>Unauthenticated sandbox escape → RCE via the pre-auth /assessment_thanks.do sink; in-the-wild exploitation since Jul 18 — five days after the patch — using escape routes beyond the public PoC (Help Net Security).</td></tr>
  <tr><td>CVE-2026-58644</td><td class="cvss">9.8</td><td>Microsoft SharePoint (on-prem)</td><td>Unauthenticated deserialization RCE; KEV Jul 16, FCEB due Jul 19; part of the actively exploited SharePoint chain.</td></tr>''')

sub(C, '<li>PTC Windchill/FlexPLM CVE-2026-12569 — FCEB due',
 '<li>SharePoint CVE-2026-50522 and Check Point SmartConsole CVE-2026-16232 — added Jul 22, FCEB due <strong>Jul 25</strong> <span class="due-crit">(due TODAY — 0 days left)</span>, a three-day window under BOD 26-04\'s risk-based deadlines (The Hacker News/Help Net Security). <span class="tag new">New</span></li>\n  <li>PTC Windchill/FlexPLM CVE-2026-12569 — FCEB due')

sub(C, '<li>WordPress CVE-2026-63030 (Jul 21) and SharePoint CVE-2026-50522 (Jul 22, "Adds Two" alert) — KEV-listed; no FCEB due date printed on the alerts. Under BOD 26-04, KEV deadlines are risk-based per CVE — always use the CISA-stated date.</li>',
 '<li>WordPress CVE-2026-63030 (added Jul 21) — KEV-listed; no FCEB due date printed on the alert. Under BOD 26-04, KEV deadlines are risk-based per CVE — always use the CISA-stated date.</li>')

sub(C, '<div class="card"><h4>Coca-Cola\'s Fairlife — Anubis leak-site listing <span class="tag ransom">Ransomware</span></h4><p>Coca-Cola disclosed in a July 16 SEC Form 8-K that attackers reached parts of dairy subsidiary Fairlife\'s environment tied to production; the Anubis ransomware group then listed Fairlife on its leak site on July 20 (SWK Technologies July 2026 recap).</p></div>',
 '<div class="card"><h4>Coca-Cola\'s Fairlife — Anubis deadline Monday <span class="tag ransom">Ransomware</span></h4><p>Coca-Cola disclosed in a July 16 SEC Form 8-K that attackers reached parts of dairy subsidiary Fairlife\'s environment tied to production, temporarily halting U.S. production while Canadian operations continued; the company says product quality and safety were not affected. The Anubis ransomware group listed Fairlife on its leak site July 20 and claims it encrypted Nutanix systems and exfiltrated 1TB of data, setting a leak deadline of Monday morning, July 27 — the group\'s claims are not independently confirmed (BleepingComputer/SecurityWeek/GovInfoSecurity).</p></div>')

sub(C, '  <a href="https://www.swktech.com/swk-cybersecurity-news-recap-july-2026/">SWK Technologies — Cybersecurity news recap July 2026 (Coca-Cola/Fairlife 8-K Jul 16; Anubis listing Jul 20)</a><br>',
 '''  <a href="https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html">The Hacker News — Critical SharePoint RCE CVE-2026-50522 under active exploitation after public PoC (FCEB due Jul 25)</a><br>
  <a href="https://www.cisa.gov/news-events/alerts/2026/07/22/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA — Adds two Known Exploited Vulnerabilities to catalog (Jul 22: CVE-2026-16232, CVE-2026-50522)</a><br>
  <a href="https://www.securityweek.com/fourth-sharepoint-vulnerability-exploited-in-past-months-wave-of-attacks/">SecurityWeek — Fourth SharePoint vulnerability exploited in past month's wave of attacks</a><br>
  <a href="https://www.resecurity.com/blog/article/from-web-request-to-domain-compromise-understanding-the-july-2026-sharepoint-attacks">Resecurity — From web request to domain compromise: the July 2026 SharePoint attacks</a><br>
  <a href="https://www.helpnetsecurity.com/2026/07/23/check-point-vulnerability-cve-2026-16232/">Help Net Security — Attackers exploit critical Check Point flaw to take over firewall management (due Jul 25)</a><br>
  <a href="https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/">BleepingComputer — Check Point warns of SmartConsole zero-day exploited in attacks</a><br>
  <a href="https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild/">Rapid7 — CVE-2026-16232: Check Point SmartConsole authentication bypass exploited in the wild</a><br>
  <a href="https://www.helpnetsecurity.com/2026/07/20/servicenow-cve-2026-6875-exploited/">Help Net Security — ServiceNow pre-auth RCE exploited in the wild (CVE-2026-6875)</a><br>
  <a href="https://www.bleepingcomputer.com/news/security/anubis-ransomware-claims-coca-cola-fairlife-attack-threatens-data-leak/">BleepingComputer — Anubis ransomware claims Coca-Cola Fairlife attack, threatens data leak (Jul 27 deadline)</a><br>
  <a href="https://www.securityweek.com/ransomware-group-threatening-to-leak-data-stolen-from-coca-colas-fairlife/">SecurityWeek — Ransomware group threatening to leak data stolen from Coca-Cola's Fairlife</a><br>
  <a href="https://www.swktech.com/swk-cybersecurity-news-recap-july-2026/">SWK Technologies — Cybersecurity news recap July 2026 (Coca-Cola/Fairlife 8-K Jul 16; Anubis listing Jul 20)</a><br>''')

# ---- WALL STREET ----
sub(W, 'but fixed-income markets now price roughly a one-in-three chance of a <em>hike</em> as energy prices and hawkish Fed commentary keep inflation risk front and center (CBS News/Forbes, Jul 23). It\'s a non-SEP meeting, so no new dot plot (CME Group/KuCoin).',
 'and rate-hike odds have collapsed — from over 40% earlier in the week to below 17% — after June CPI printed below expectations (3.5% headline) and June payrolls came in at a soft 57,000 (CNBC next-week outlook). Forbes had pegged hike odds near one-in-three on Jul 23, before Friday\'s oil slide unwound the inflation-scare trade. It\'s a non-SEP meeting, so no new dot plot (CME Group/KuCoin).')

sub(W, 'The question: whether the market keeps punishing big AI spenders after Alphabet\'s capex guide of up to $205B sent its shares down 7.1% Thursday (CNBC).',
 'The question: whether the market keeps punishing big AI spenders after Alphabet\'s capex guide of up to $205B sent its shares down 7.1% Thursday (CNBC). Also on deck: PayPal, Coca-Cola, Boeing, Visa and Ford on Tuesday; ARM and Qualcomm Wednesday; Chevron and ExxonMobil close the week Friday (IG).')

sub(W, '  <a href="https://www.cnbc.com/2026/07/24/stock-market-next-week-outlook-for-july-27-31-2026.html">CNBC — Stock market next week: outlook for July 27–31, 2026 (Fed + megacap earnings)</a><br>',
 '  <a href="https://www.cnbc.com/2026/07/24/stock-market-next-week-outlook-for-july-27-31-2026.html">CNBC — Stock market next week: outlook for July 27–31, 2026 (Fed + megacap earnings; hike odds below 17%)</a><br>\n  <a href="https://www.ig.com/en-ch/news-and-trade-ideas/week-ahead--27-july-2026-260724">IG — Week ahead: 27 July 2026 (earnings calendar)</a><br>')

# ---- MMA ----
sub(M, 'Ulberg has been sidelined since ACL surgery following UFC 327. <span class="tag new">New</span>',
 'Ulberg has been sidelined since ACL surgery following UFC 327.')

# ---- INDEX ----
sub(I, '<h2>Cl0p is looting engineering data from exposed Windchill and FlexPLM servers</h2>\n    <p>The ransomware crew is mass-exploiting CVE-2026-12569 — patched since June, federal deadline a month past — while Origin Energy confirms a breach at a 4.8-million-customer retailer and the AD FS KEV deadline lands Tuesday.</p>',
 '<h2>Deadline day: SharePoint and Check Point fixes come due as exploitation spreads</h2>\n    <p>CISA gave federal agencies three days on the actively exploited SharePoint RCE (CVE-2026-50522) and the Check Point SmartConsole zero-day — both due today — while Cl0p keeps raiding exposed Windchill/FlexPLM servers and Origin Energy works through a 4.8M-customer breach.</p>')

print("ALL EDITS OK")
