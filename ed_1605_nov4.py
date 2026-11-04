import re,sys
R='/tmp/db_1793826219/'
def rep(s,a,b,cnt=1):
    assert a in s,("MISSING",a[:80]); return s.replace(a,b,cnt)
TS='~4:05 PM ET'
JA='https://journalarta.com/en/2026/11/05/dow-jumps-2-91-as-brent-slides-7-77-and-gold-climbs-3-73/'
ST='https://www.stocktitan.net/articles/stock-market-today-live-november-4-2026'
CN='https://www.cnbc.com/2026/11/03/stock-market-today-live-updates.html'
# ---------- WALL STREET
w=open(R+'wallstreet-briefing.html').read()
w=re.sub(r'Updated <span id="updated">[^<]*','Updated <span id="updated">4:05 PM ET',w)
tape='The closing bell has rung on a post-midterm surge — official closing levels had not been published by a source this edition could verify at about 4:05 p.m. ET, but the last verified reads (~3:34 p.m.) had the Dow up roughly 3.2%, the S&amp;P 500 and Nasdaq Composite about 1.8%, with the Dow on pace for its best day since April 2025 as oil plunged and Apple and Microsoft hit records.'
w=re.sub(r'(<div class="tldr"><b>The Tape</b> <span>).*?(</span></div>)',lambda m:m.group(1)+tape+m.group(2),w,count=1,flags=re.S)
w=re.sub(r'id="freshline">[^<]*','id="freshline">Data as of ~4:05 PM ET (markets closed; official closes pending — latest verified index read ~3:34 PM ET) · briefings refresh every 30 minutes, 8 AM–6 PM ET',w)
w=rep(w,'<h3>Into the final half-hour (as of ~3:34 PM ET): Dow about +3.2%, S&amp;P 500 and Nasdaq about +1.8% — the Dow on pace for its best day since April 2025</h3><p><span class="tag new">New</span> With under half an hour left',
 '<h3>Closing bell: stocks finish a post-midterm surge — official closes pending; last verified read (~3:34 PM ET) Dow about +3.2%, S&amp;P 500 and Nasdaq about +1.8%</h3><p><span class="tag new">New</span> Regular trading ended at 4:00 p.m. ET. At this edition’s ~4:05 p.m. read, no fetched source had yet published official closing levels, so none are printed; they will go into the Weekly Scorecard once verified. CNBC’s 3 p.m. ET update had the Dow up 1,511 points, or 2.9% (<a href="'+CN+'" target="_blank" rel="noopener">CNBC, via search</a>).</p><p>With under half an hour left')
card=('<div class="card"><span class="tag new">New</span><span class="tag">Rotation</span><h3>Energy sinks, industrials and Oracle climb</h3><p>In a 1:38 p.m. ET market snapshot, ExxonMobil was −5.31% at $168.03 while Oracle gained 5.85% to $126.19, Eaton 7% to $391.70 and GE Vernova 6.49% to $918.20; AppLovin was +7.28% at $245.51 ahead of its after-the-close report. In the same snapshot Brent was −7.77% at $95.55 and WTI −7.62% at $88.77, gold +3.73% and the VIX −18.48% at 16.98. (<a href="'+JA+'" target="_blank" rel="noopener">JournalArta Markets, data via Yahoo Finance/Twelve Data, as of 18:38 GMT</a>)</p></div>')
w=rep(w,'<h2 class="sec">Movers &amp; Drivers</h2><div class="cards">','<h2 class="sec">Movers &amp; Drivers</h2><div class="cards">'+card)
ah=('<h2 class="sec">After-Hours Movers</h2><div class="cards"><div class="card"><span class="tag new">New</span><span class="tag">Earnings</span><h3>After the bell: Arm, Qualcomm, McKesson, AppLovin</h3><p>Arm, Qualcomm, McKesson and AppLovin report this evening (<a href="'+ST+'" target="_blank" rel="noopener">StockTitan</a>). No after-hours price moves had been confirmed by a source at this edition’s ~4:05 p.m. ET read; sourced moves will be added in the next edition.</p></div></div>')
w=rep(w,'<h2 class="sec">Weekly Scorecard</h2>',ah+'<h2 class="sec">Weekly Scorecard</h2>')
w=rep(w,'<li><b>Earnings still to come today:</b> Arm Holdings and Qualcomm are on Yahoo’s Nov. 4 earnings calendar (<a href="https://finance.yahoo.com/markets/live/stock-market-today-dow-sp-500-nasdaq-midterm-elections-earnings-140752043.html" target="_blank" rel="noopener">Yahoo Finance</a>).</li>',
 '<li><b>Tonight:</b> Arm, Qualcomm, McKesson and AppLovin report after the close (<a href="'+ST+'" target="_blank" rel="noopener">StockTitan</a>).</li><li><b>Thursday:</b> ConocoPhillips, Duke Energy, Southern Company and Verisk report before the open; Airbnb, Microchip Technology, Monster Beverage, Simon Property Group and Atlassian after the close; Charter Communications reports Friday morning (<a href="'+JA+'" target="_blank" rel="noopener">JournalArta</a>).</li>')
w=rep(w,'(fetched or searched this run, Nov. 4 ~3:40 PM ET,','(fetched or searched this run, Nov. 4 ~4:05 PM ET,')
w=rep(w,'<footer><b>Sources</b>','<footer><b>Sources</b>',1)
w=rep(w,'</ol><div class="disc">Information only','<li><a href="'+JA+'" target="_blank" rel="noopener">JournalArta — Dow Jumps 2.91% as Brent Slides 7.77% (fetched this run; snapshot as of 1:38 PM ET)</a></li><li><a href="'+CN+'" target="_blank" rel="noopener">CNBC — live updates (3 PM ET update, via search this run)</a></li></ol><div class="disc">Information only')
open(R+'wallstreet-briefing.html','w').write(w)
# ---------- CYBER
c=open(R+'cyber-briefing.html').read()
c=re.sub(r'Updated <span id="updated">[^<]*','Updated <span id="updated">4:05 PM ET',c)
c=re.sub(r'id="freshline">[^<]*','id="freshline">Data as of ~4:05 PM ET · briefings refresh every 30 minutes, 8 AM–6 PM ET',c)
T='https://thehackernews.com/2026/11/'
def cd(tag,h,p,u): return '<div class="card"><span class="tag new">New</span><span class="tag ">'+tag+'</span><h3>'+h+'</h3><p>'+p+' (<a href="'+T+u+'" target="_blank" rel="noopener">The Hacker News</a>)</p></div>'
cards=(cd('Espionage','APT29-linked “Poisoned Source” watering hole hits iOS and Android','Sekoia ties a large watering-hole campaign to Russia-linked APT29: compromised sites, fake domains and a supply-chain compromise of Ukrainian analytics service Plerdy SEO Tracker served injected JavaScript that fingerprinted devices, then delivered platform-specific N-day exploit chains to steal browser cookies and, in some cases, Wi-Fi passwords or full device data. Discovered mid-October 2026.','apt29-linked-hackers-hijack-web.html')
 +cd('Supply chain','cPGuard update channel hijacked to backdoor Linux servers','An attacker used compromised credentials to break into cPGuard’s update system on Nov. 2 and pushed a script that installed a backdoor and collected password hashes; it shipped in versions 5.88.12–5.88.19, and 5.88.25+ removes it. OPSSHIELD says copied credentials may still work — rotate passwords and keys.','cpguard-update-channel-hijacked-to.html')
 +cd('Data breach','Chainstack breach exposes customer data and password hashes','The blockchain infrastructure provider says an attacker entered a development environment via a third-party component on Oct. 26, escalated into parts of production, and was cut off Oct. 31; it is assessed as part of a large AI-powered campaign that surfaced last week.','chainstack-reports-production-systems.html')
 +cd('Incident','mSecure tells users to change passwords and reset 2FA','A Nov. 3 email from developer mSeven Software cites suspicious activity linked to the password manager and urges customers to change passwords, reset 2FA and remove passkeys; it does not say whether stored data was exposed.','msecure-warns-users-to-change-passwords.html')
 +cd('Espionage','SlippyNunchucks hijacks Sogou Input Method DNS to drop DarkVigil','ESET attributes a DNS-hijacking surveillance campaign, observed since July 1, 2026, abusing insecure HTTP traffic in Windows versions of Sogou Input Method to deploy the DarkVigil (FDMTP) implant against targets in Hong Kong, Thailand, Japan, Vietnam, Oman and Sri Lanka.','china-aligned-hackers-hijack-sogou.html'))
c=rep(c,'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">','<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">'+cards)
def row(cve,cv,aff,note,u,new=True): return '<tr><td>'+cve+'</td><td>'+cv+'</td><td>'+aff+'</td><td>'+('<span class="tag new">New</span> ' if new else '')+note+' (<a href="'+T+u+'" target="_blank" rel="noopener">THN</a>)</td></tr>'
rows=(row('GHSA-f3w6-w445-fwh9 (no CVE yet)','9.8','Ruby on Rails Active Storage (ImageMagick uploads)','Unauthenticated arbitrary file write; Disk-service apps may also leak secret_key_base; fixed 8.1.4.1 / 8.0.5.2','critical-rails-flaw-lets-attackers.html')
 +row('CVE-2026-58868','Critical (Google rating)','Android 14–17','Zero-click RCE (heap overflow, FrameDecoder.cpp); fixed in patch level 2026-11-01; no exploitation reported, not in KEV as of Nov. 3','google-patches-critical-android-flaw.html')
 +row('CVE-2026-116606 / -111560','9.3 / 8.6','Barracuda Email Security Gateway (+ WAF, Load Balancer ADC, Message Archiver, others for -111560)','Pre-auth authorization bypass + command injection chain to root; needs admin-interface access','barracuda-flaws-could-be-chained-to.html')
 +row('CVE-2026-98432','9.8','Linux kernel IPv4 TCP (since 4.4)','Remote unauthenticated use-after-free → RCE; Red Hat RHEL 8/9/10 fixed, Ubuntu fixes still in testing','red-hat-patches-98-rated-linux-tcp-rce.html')
 +row('CVE-2026-102703 / -102704','—','Xen hypervisor 4.6+ (XSA-523)','Malicious guest VM can read/write other VMs’ memory incl. dom0; patches out, no mitigation','xen-hypervisor-flaws-let-one-malicious.html'))
c=rep(c,'<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>','<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>'+rows)
c=rep(c,'<footer><b>Sources</b> (','<footer><b>Sources</b> (Nov. 4 ~4:05 PM run: The Hacker News front page fetched — APT29, cPGuard, Chainstack, mSecure, SlippyNunchucks, Rails, Android, Barracuda, Linux TCP and Xen items new this run; ')
src=''.join('<li><a href="'+T+u+'" target="_blank" rel="noopener">The Hacker News — '+t+' (fetched this run via THN front page)</a></li>' for t,u in [('APT29 Poisoned Source','apt29-linked-hackers-hijack-web.html'),('cPGuard update channel hijacked','cpguard-update-channel-hijacked-to.html'),('Chainstack breach','chainstack-reports-production-systems.html'),('mSecure warning','msecure-warns-users-to-change-passwords.html'),('SlippyNunchucks / Sogou','china-aligned-hackers-hijack-sogou.html'),('Critical Rails flaw','critical-rails-flaw-lets-attackers.html'),('Android CVE-2026-58868','google-patches-critical-android-flaw.html'),('Barracuda chained flaws','barracuda-flaws-could-be-chained-to.html'),('Linux TCP CVE-2026-98432','red-hat-patches-98-rated-linux-tcp-rce.html'),('Xen XSA-523','xen-hypervisor-flaws-let-one-malicious.html')])
c=rep(c,'<footer><b>Sources</b>','<footer><b>Sources</b>')
i=c.find('<ol>',c.find('<footer>')); c=c[:i+4]+src+c[i+4:]
open(R+'cyber-briefing.html','w').write(c)
# ---------- MMA
m=open(R+'mma-briefing.html').read()
m=re.sub(r'Updated <span id="updated">[^<]*','Updated <span id="updated">4:05 PM ET',m)
m=re.sub(r'id="freshline">[^<]*','id="freshline">Data as of ~4:05 PM ET · briefings refresh every 30 minutes, 8 AM–6 PM ET',m)
open(R+'mma-briefing.html','w').write(m)
# ---------- INDEX
x=open(R+'index.html').read()
x=re.sub(r'Updated <span id="updated">[^<]*','Updated <span id="updated">4:05 PM ET',x)
x=re.sub(r'id="freshline">[^<]*','id="freshline">Data as of ~4:05 PM ET · briefings refresh every 30 minutes, 8 AM–6 PM ET',x)
x=rep(x,'Final half-hour: Dow about +3.2%, on pace for its best day since April 2025','Closing bell: post-midterm surge; Dow on pace for best day since April 2025')
x=re.sub(r'(Markets · ▲ The Closing Bell · The Tape</div><h3[^>]*>[^<]*</h3><p>).*?(</p>)',lambda mm:mm.group(1)+tape+mm.group(2),x,count=1,flags=re.S)
open(R+'index.html','w').write(x)
print('ok')
