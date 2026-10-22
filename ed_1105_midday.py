import re,sys
D='/tmp/db_1792681308/'
def rd(f): return open(D+f,encoding='utf-8').read()
def wr(f,s): open(D+f,'w',encoding='utf-8').write(s)
def rep(s,a,b,f):
    assert a in s, (f,a[:80]); return s.replace(a,b,1)
NOW='11:15 AM ET'
SG='https://sundayguardianlive.com/business/us-stock-market-today-live-dow-jones-slips-300-points-sp-500-slips-127-and-nasdaq-down-207-as-price-tops-111-spacex-tech-stocks-slide-check-latest-wall-street-updates-310277/'
# ---------- WS
f='wallstreet-briefing.html'; s=rd(f)
s=s.replace('<span class="tag new">New</span>','')
s=re.sub(r'Data as of [0-9:]+ [AP]M ET ·','Data as of '+NOW+' ·',s)
old_h3=re.search(r'<div class="panel lead"><h3>.*?</h3>',s).group(0)
s=s.replace(old_h3,'<div class="panel lead"><h3>Late morning (~10:45 AM ET): Nasdaq −2.07%, S&amp;P 500 −1.27%, Dow −0.53% — the tech sell-off widens as Brent holds above $111</h3>\n<p><span class="tag new">New</span><b>Late morning (~10:45 AM ET).</b> The slide extended: a Sunday Guardian Live market snapshot updated at about 10:45 AM ET had the Nasdaq Composite down 2.07%, the S&amp;P 500 down 1.27% and the Dow down 0.53%, with semiconductor and major technology stocks leading the decline; Brent crude was $111.61 (+2.56%), U.S. crude $98.66 (+1.56%), gold $4,050.35 (−2.19%) and the 10-year yield 5.03%. The same snapshot put the VIX at 18.25. Its single-stock figures could not be corroborated this edition and are not repeated here (<a href="'+SG+'">Sunday Guardian Live</a>). Yahoo’s live pages served only cached ~10:15 AM data this edition.</p>',1)
tl=re.search(r'(class="tldr"><b>The Tape</b> <span>)(.*?)(</span>)',s)
NEWT='The tech-led sell-off widened through late morning — the Nasdaq Composite down 2.07%, the S&amp;P 500 1.27% and the Dow 0.53% as of ~10:45 AM ET — with chip-equipment makers such as Lam Research among the biggest decliners after premarket drops in Tesla and IBM, while Brent holds above $111 and the 10-year yield sits at 5.03%; jobless claims fell to 194,000, the lowest since July.'
s=s.replace(tl.group(0),tl.group(1)+NEWT+tl.group(3),1)
s=rep(s,'<footer><b>Sources (read this edition)</b><ol>','<footer><b>Sources (read this edition)</b><ol><li><a href="'+SG+'">Sunday Guardian Live — US Stock Market Today LIVE (updated ~10:45 AM ET, Oct. 22)</a></li>',f)
wr(f,s)
# ---------- index
f='index.html'; s=rd(f)
s=re.sub(r'Data as of [0-9:]+ [AP]M ET ·','Data as of '+NOW+' ·',s)
s=rep(s,'By mid-morning the selling has deepened — the Nasdaq Composite down 1.82%, the S&amp;P 500 1.03% and the Dow 0.22% as of ~10:15 AM ET — with chip-equipment makers such as Entegris (−10.8%) and Lam Research (−8.7%) among the biggest decliners after premarket drops in Tesla and IBM, while WTI trades near $99 and the 10-year yield sits at 5.03%; jobless claims fell to 194,000, the lowest since July.',NEWT,f)
CY_OLD='PHP has shipped emergency fixes (8.5.12, 8.4.27, 8.3.36, 8.2.35) for the two “PHP2Shell” remote-code-execution flaws, rated CVSS v4.0 9.2, with exploitation attempts now seen by several security firms — while federal agencies face a Friday, Oct. 23 deadline for three of the Plex and SiteGuard flaws CISA added to KEV.'
CY_NEW='PHP has shipped emergency fixes (8.5.12, 8.4.27, 8.3.36, 8.2.35) for the two “PHP2Shell” remote-code-execution flaws, rated CVSS 9.2, and the NSA has told PHP users to update immediately or take systems offline — while federal agencies face a Friday, Oct. 23 deadline for three of the Plex and SiteGuard flaws CISA added to KEV.'
s=rep(s,CY_OLD,CY_NEW,f)
wr(f,s)
# ---------- cyber
f='cyber-briefing.html'; s=rd(f)
s=s.replace('<span class="tag new">New</span>','')
s=re.sub(r'Data as of [0-9:]+ [AP]M ET ·','Data as of '+NOW+' ·',s)
tl=re.search(r'(class="tldr"><b>The Wire</b> <span>)(.*?)(</span>)',s)
s=s.replace(tl.group(0),tl.group(1)+CY_NEW.replace('three of the Plex and SiteGuard','three of the Plex2Shell and SiteGuard')+tl.group(3),1)
TC='https://techcrunch.com/2026/10/21/the-internet-is-having-a-very-bad-cybersecurity-day/'
CSN='https://cybersecuritynews.com/october-21-cybersecurity-nightmare/'
cards=('<div class="card"><span class="tag new">New</span> <span class="tag crit">PKI</span> <h3>eMudhra CA: eight intermediate signing keys compromised</h3><p>Eight intermediate signing keys at Indian certificate authority eMudhra were compromised; its updated disclosure says incorrect key generation made them recoverable from public certificates, creating a risk of forged certificates. Mozilla found all eight affected P-384 private keys were integers below 256, allowing almost instant recovery. Browser vendors have issued blocks, but applications with separate certificate bundles or no revocation checks may remain exposed — update browsers, operating systems, runtimes and trust stores. Public evidence has not established attacks on users through these keys (<a href="'+CSN+'">Cyber Security News, Oct. 22</a>; <a href="'+TC+'">TechCrunch</a>).</p></div>'
 '<div class="card"><span class="tag new">New</span> <span class="tag">Patch</span> <h3>NSA on PHP2Shell: update now or go offline; Node.js and Tomcat also patch</h3><p>The NSA advised organisations running PHP to update immediately or take systems offline until they can, and government websites worldwide went offline, per TechCrunch citing Reuters. The same day Node.js fixed ten vulnerabilities, four rated high, including CVE-2026-111497 in Brotli decompression that can allow code execution (patched in 26.12.1, 24.22.1 and 22.23.4), and Apache Tomcat disclosed eight fixes on Oct. 20, among them CVE-2026-101296, an authentication bypass when JNDIRealm uses non-GSSAPI SASL mechanisms (fixed in 11.0.27, 10.1.61, 9.0.123) (<a href="'+TC+'">TechCrunch, Oct. 21</a>; <a href="'+CSN+'">Cyber Security News</a>).</p></div>')
s=rep(s,'Breaches &amp; Incidents</h2><div class="cards">','Breaches &amp; Incidents</h2><div class="cards">'+cards,f)
s=rep(s,'<footer><b>Sources','<footer><b>Sources',f)
s=re.sub(r'(<footer><b>Sources[^<]*</b>(?:\s*)<ol>)',lambda m:m.group(1)+'<li><a href="'+CSN+'">Cyber Security News — October 21 Cybersecurity Nightmare (Oct. 22)</a></li><li><a href="'+TC+'">TechCrunch — The internet is having a very bad cybersecurity day (Oct. 21)</a></li>',s,1)
assert CSN in s.split('<footer')[1]
wr(f,s)
# ---------- mma
f='mma-briefing.html'; s=rd(f)
s=s.replace('<span class="tag new">New</span>','')
s=re.sub(r'Data as of [0-9:]+ [AP]M ET ·','Data as of '+NOW+' ·',s)
NAT='https://www.thenationalnews.com/sport/combat-sports/2026/10/22/ufc-333-predictions-volkanovski-and-dvalishvili-to-leave-abu-dhabi-as-champions/'
li='<li><span class="tag new">New</span> The National’s picks (Steve Luckings, Oct. 22): Volkanovski to retain on the judges’ scorecards and Dvalishvili to reclaim the bantamweight title; Temirov by KO over Lone’er Kavanagh, Volkov by decision over Kuniev, and Keita by KO over Aaron Pico. The paper notes Losene Keita was drafted in on short notice after an injury to Arnold Allen, that there are nine fights on the card, and that neither Yan nor Dvalishvili has fought since their December meeting (<a href="'+NAT+'">The National</a>).</li>'
s=rep(s,'Around the Sport</h2><div class="panel"><ul class="bul">','Around the Sport</h2><div class="panel"><ul class="bul">'+li,f)
s=re.sub(r'(<footer><b>Sources[^<]*</b>(?:\s*)<ol>)',lambda m:m.group(1)+'<li><a href="'+NAT+'">The National — UFC 333 predictions (Oct. 22)</a></li>',s,1)
assert NAT in s.split('<footer')[1]
wr(f,s)
print('ok')
