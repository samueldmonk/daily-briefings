#!/usr/bin/env python3
"""Edits for the Saturday Aug 22 2026 ~6:05pm ET Afternoon Edition (third run of Saturday)."""
import io, sys, os

D = sys.argv[1]

def nz(t):
    # pages store literal unicode punctuation, not HTML entities
    return (t.replace('&mdash;', '—').replace('&ndash;', '–')
             .replace('&middot;', '·').replace('&rarr;', '→'))

def rw(path, subs):
    p = os.path.join(D, path)
    s = io.open(p, encoding='utf-8').read()
    # index.html mixes entities and literals; try normalized, fall back to raw
    fixed = []
    for a, b in subs:
        if nz(a) in s:
            fixed.append((nz(a), nz(b)))
        else:
            fixed.append((a, b))
    subs = fixed
    for i, (old, new) in enumerate(subs):
        if old not in s:
            raise SystemExit("MISS in %s (#%d): %.140s" % (path, i, old))
        if s.count(old) != 1:
            raise SystemExit("AMBIG in %s (#%d) x%d: %.140s" % (path, i, s.count(old), old))
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)
    print("ok", path, len(subs), "edits")


# ---------------------------------------------------------------- CYBER
cy = []

# 1. TL;DR
cy.append((
'<div class="tldr"><b>The Wire</b> <span>A GitLab code-injection flaw rated CVSS 9.4 is being exploited in the wild within days of disclosure, Cisco has patched nine Crosswork and Secure Workload bugs including five scoring a maximum 10.0, and 7 entries in CISA\'s Known Exploited Vulnerabilities catalog are now past their federal remediation deadline.</span></div>',
'<div class="tldr"><b>The Wire</b> <span>A GitLab code-injection flaw rated CVSS 9.4 remains under active exploitation, the TrueConf Server flaw due for federal remediation tomorrow now carries a CVSS of 9.3 and a named attacker in the Head Mare group, and 7 entries in CISA\'s Known Exploited Vulnerabilities catalog are already past their deadline.</span></div>'))

# 2. Stat strip
cy.append((
'<div class="stat"><div class="n">5</div><div class="l">Cisco flaws at CVSS 10.0</div></div>\n<div class="stat"><div class="n">245M</div><div class="l">Downloads of the Rust crates hit</div></div>\n<div class="stat"><div class="n">6</div><div class="l">CVEs added to KEV since Aug 18</div></div>',
'<div class="stat"><div class="n">768</div><div class="l">Leaked AWS keys still live with full admin</div></div>\n<div class="stat"><div class="n">88%</div><div class="l">Of re-tested leaked AWS keys still authenticate</div></div>\n<div class="stat"><div class="n">5</div><div class="l">Cisco flaws at CVSS 10.0</div></div>'))

# 3. Patch Priority — TrueConf now has a CVSS and a named actor
cy.append((
'The nearest deadline still ahead is <b>CVE-2026-72529</b> in <b>TrueConf Server</b>, due <b>August 23 &mdash; tomorrow</b>.</p>\n<p class="note" style="margin-top:10px">No CVSS score is printed here for either TrueConf CVE because no source fetched this run stated one. TrueConf fixed both flaws back in June 2026 in Server versions 5.3.9, 5.4.9 and 5.5.5.</p>',
'The nearest deadline still ahead is <b>CVE-2026-72529</b> in <b>TrueConf Server</b> &mdash; <b>CVSS 9.3</b>, due <b>August 23, tomorrow</b>.</p>\n<p style="margin:10px 0 0;font-size:15px;color:#c6d2dd">The TrueConf figure is new to this edition: earlier runs could not source a score. CISA and SecurityWeek now describe CVE-2026-72529 as a missing-authentication flaw that lets an unprivileged remote attacker run arbitrary scripts by invoking an undocumented function over <b>port 4307/TCP</b>, and it is being chained with <b>CVE-2026-72530</b> (due September 3) to replace TrueConf client distribution files and push <b>PhantomCore</b> malware to meeting participants.</p>\n<p class="note" style="margin-top:10px">TrueConf fixed both flaws in June 2026 in Server versions 5.3.9, 5.4.9 and 5.5.5. The required action falls under CISA\'s risk-based BOD 26-04 guidance rather than a fixed three-week window.</p>'))

# 4. Threat Actor Spotlight -> Head Mare (rotated from UNC6293/7005/5976)
cy.append((
'''<div class="tags"><span class="tag new">New</span><span class="tag">Espionage</span><span class="tag">Russia-nexus (suspected)</span></div>
<h3>UNC6293, UNC7005 and UNC5976 &mdash; hijacking accounts through legitimate login flows</h3>
<p>Google Threat Intelligence Group researchers <b>Gabby Roncone</b> and <b>Wesley Shields</b> reported on August 20 that three distinct suspected Russian cyber-espionage clusters are abusing <b>legitimate authentication flows</b> &mdash; Google OAuth and WhatsApp device linking &mdash; rather than exploiting software flaws. Targets span academia, aerospace and defence, governments and think tanks across Europe, plus academia and think tanks in the United States. GTIG describes the clusters as running persistent, adaptive phishing campaigns that use sophisticated social engineering to compromise personal accounts across multiple platforms.</p>
<p style="margin-top:9px"><b>UNC6293</b>, first detailed by Google and the Citizen Lab in June 2025, is assessed to be a sub-cluster of <b>Ice Relic</b> &mdash; formerly APT29, also tracked as Cozy Bear and Midnight Blizzard &mdash; and was previously tied to a campaign abusing Google application-specific passwords.</p>
<p class="note">Attribution here is Google\'s own assessment of a suspected Russian nexus; the clusters are tracked under uncategorised (UNC) designations, which means Google has not publicly tied them to a named government entity.</p>''',
'''<div class="tags"><span class="tag new">New</span><span class="tag hot">Actively exploiting</span><span class="tag">Hacktivist</span></div>
<h3>Head Mare &mdash; turning a video-conferencing server into a malware delivery channel</h3>
<p>The group behind the two TrueConf Server flaws added to CISA\'s KEV catalog on August 20 is the hacktivist crew tracked as <b>Head Mare</b>. Rather than stopping at server compromise, the operators chained <b>CVE-2026-72529</b> (CVSS 9.3, missing authentication for a critical function) with <b>CVE-2026-72530</b> (code injection) against on-premises TrueConf instances, then <b>replaced the TrueConf client distribution files</b> hosted on those servers.</p>
<p style="margin-top:9px">That turns a trusted internal download into a delivery mechanism: anyone joining a meeting who pulled the client from the compromised server received <b>PhantomCore</b> malware instead. It is a supply-chain pattern executed inside the victim\'s own perimeter, which is why CISA set an unusually short remediation window &mdash; three days &mdash; on the first of the two CVEs.</p>
<p class="note">Reported by SecurityWeek, SC Media, BleepingComputer and Security Affairs following CISA\'s August 20 KEV addition. Head Mare is described in that reporting as a hacktivist group; no state sponsor is asserted here. Previous spotlight: the suspected-Russian UNC6293 / UNC7005 / UNC5976 clusters abusing Google OAuth and WhatsApp device linking.</p>'''))

# 5. New breach cards at the front of the deck
cy.append((
'<div class="lab">Breaches &amp; Incidents</div>\n<div class="cards">\n<div class="card">\n<div class="tags"><span class="tag new">New</span><span class="tag hot">Critical infrastructure</span></div>',
'''<div class="lab">Breaches &amp; Incidents</div>
<div class="cards">
<div class="card">
<div class="tags"><span class="tag new">New</span><span class="tag hot">Extortion</span><span class="tag">Financial services</span></div>
<h3>US Bank investigating LockBit claim, with a September 3 leak deadline</h3>
<p>US Bank says it is investigating claims by the <b>LockBit</b> ransomware group that the gang breached the bank and stole data, The Register reported on August 20. LockBit added the bank to its leak site and set a <b>14-day deadline, expiring September 3</b>, threatening to publish unless it is paid. The bank confirmed it is aware of the claims but declined to discuss any contact with the extortionists or the sum demanded, and said there is <b>no current indication of impact to its internal systems or of unauthorised network access</b>.</p>
<p class="note">No victim count, record total or data category is published here &mdash; none has been confirmed by the bank, and LockBit\'s own claims are unverified. The group re-emerged in 2025 with its LockBit 5.0 variant after earlier law-enforcement disruption.</p>
</div>
<div class="card">
<div class="tags"><span class="tag new">New</span><span class="tag warn">Cloud</span><span class="tag">Credentials</span></div>
<h3>768 leaked AWS keys are still live &mdash; and still hold full admin</h3>
<p>Truffle Security, analysing publicly exposed AWS credentials from <b>August 2022 to August 2026</b>, found <b>768 keys that remain active and carry full administrative privileges</b> over corporate cloud accounts: <b>526 root access keys</b> plus <b>242 IAM user keys</b> attached to the AdministratorAccess managed policy. Re-validating <b>10,616 key pairs</b> on <b>August 10</b>, the researchers found <b>88% still authenticated</b>.</p>
<p style="margin-top:9px">The exposure skews old rather than new. The oldest working credential was <b>17.4 years</b> old, and only <b>25</b> enumerable keys had been created in the preceding 30 days &mdash; so the dominant risk is forgotten credentials, not fresh developer mistakes. Of 2,903 keys examined, just <b>398</b> had a newer credential on the same IAM user, implying roughly <b>86% were never rotated or revoked</b>. Sources of leakage included public Git histories, Hugging Face datasets, Docker images, package registries and CI/CD logs.</p>
</div>
<div class="card">
<div class="tags"><span class="tag hot">Critical infrastructure</span></div>'''))

# strip stale "New" tags from items carried over from the 17:46 snapshot
for t in ['<div class="tags"><span class="tag new">New</span><span class="tag warn">Supply chain</span></div>',
          '<div class="tags"><span class="tag new">New</span><span class="tag">Endpoint</span></div>',
          '<div class="tags"><span class="tag new">New</span><span class="tag">Automotive</span></div>']:
    pass  # handled below (supply chain appears twice)

cy.append((
'''<div class="tags"><span class="tag new">New</span><span class="tag warn">Supply chain</span></div>
<h3>Malicious Rust crates published''',
'''<div class="tags"><span class="tag warn">Supply chain</span></div>
<h3>Malicious Rust crates published'''))
cy.append((
'''<div class="tags"><span class="tag new">New</span><span class="tag warn">Supply chain</span></div>
<h3>14 trojanized npm packages''',
'''<div class="tags"><span class="tag warn">Supply chain</span></div>
<h3>14 trojanized npm packages'''))
cy.append((
'<div class="tags"><span class="tag new">New</span><span class="tag">Endpoint</span></div>',
'<div class="tags"><span class="tag">Endpoint</span></div>'))
cy.append((
'<div class="tags"><span class="tag new">New</span><span class="tag">Automotive</span></div>',
'<div class="tags"><span class="tag">Automotive</span></div>'))

# 6. CVE table — add TrueConf rows
cy.append((
'<tr><td><b>CVE-2026-59310</b></td><td>9.8</td>',
'<tr><td><b>CVE-2026-72529</b></td><td>9.3</td><td>TrueConf Server (fixed in 5.3.9 / 5.4.9 / 5.5.5)</td><td><span class="down">Exploited in the wild</span> by Head Mare. Missing authentication for a critical function; arbitrary script execution via an undocumented function on port 4307/TCP. KEV deadline <b>Aug 23</b>.</td></tr>\n<tr><td><b>CVE-2026-72530</b></td><td>&mdash;</td><td>TrueConf Server (same fixed versions)</td><td>Code injection, chained with CVE-2026-72529 to swap client distribution files and spread PhantomCore. No CVSS stated in the sources fetched this run. KEV deadline Sep 3.</td></tr>\n<tr><td><b>CVE-2026-59310</b></td><td>9.8</td>'))

# 7. KEV bullets — add CVSS/actor to the TrueConf rows
cy.append((
'<li><b>CVE-2026-72529</b> &mdash; TrueConf Server &mdash; missing authentication for critical function. Added Aug 20, due <b>2026-08-23</b> <span class="kev-soon">(1 day left)</span></li>',
'<li><b>CVE-2026-72529</b> &mdash; TrueConf Server &mdash; missing authentication for critical function, <b>CVSS 9.3</b>, exploited by Head Mare. Added Aug 20, due <b>2026-08-23</b> <span class="kev-soon">(1 day left)</span></li>'))
cy.append((
'<li><b>CVE-2026-72530</b> &mdash; TrueConf Server &mdash; code injection. Added Aug 20, due <b>2026-09-03</b> <span class="kev-ok">(12 days left)</span></li>',
'<li><b>CVE-2026-72530</b> &mdash; TrueConf Server &mdash; code injection, chained with 72529. Added Aug 20, due <b>2026-09-03</b> <span class="kev-ok">(12 days left)</span></li>'))

# 8. Breach-tracker note
cy.append((
'<p class="note">Breach-tracker aggregators circulated additional victim claims this weekend. None were corroborated by a primary source or victim statement fetched this run, so no victim counts or data categories are published here.</p>',
'<p class="note">Breach-tracker aggregators circulated further victim claims this weekend beyond the two added above. None were corroborated by a primary source or victim statement fetched this run, so no victim counts or data categories are published for them.</p>'))

# 9. Sources
cy.append((
'<li><a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds two known exploited vulnerabilities to catalog (Aug 20, 2026)</a></li>',
'''<li><a href="https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-trueconf-vulnerabilities/">SecurityWeek &mdash; CISA urges immediate patching of exploited TrueConf vulnerabilities</a></li>
<li><a href="https://www.scworld.com/news/trueconf-flaws-enabling-attacks-on-meeting-participants-added-to-kev-catalog">SC Media &mdash; TrueConf flaws enabling attacks on meeting participants added to KEV catalog</a></li>
<li><a href="https://securityaffairs.com/197602/security/u-s-cisa-adds-trueconf-server-flaws-to-its-known-exploited-vulnerabilities-catalog.html">Security Affairs &mdash; CISA adds TrueConf Server flaws to its KEV catalog</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-trueconf-server-flaws/">BleepingComputer &mdash; CISA orders feds to patch actively exploited TrueConf Server flaws</a></li>
<li><a href="https://www.theregister.com/security/2026/08/20/us-bank-investigates-lockbits-claims-as-ransomware-crims-set-pay-or-leak-deadline/">The Register &mdash; US Bank investigates LockBit\'s claims as ransomware crims set pay-or-leak deadline</a></li>
<li><a href="https://www.scworld.com/brief/us-bank-investigates-lockbit-ransomware-claims-of-data-breach">SC Media &mdash; US Bank investigates LockBit ransomware claims of data breach</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/hundreds-of-leaked-aws-keys-give-full-control-over-corporate-accounts/">BleepingComputer &mdash; Hundreds of leaked AWS keys give full control over corporate accounts</a></li>
<li><a href="https://gbhackers.com/768-leaked-aws-keys-still-active-with-full-admin/">GBHackers &mdash; 768 leaked AWS keys still active with full admin access</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds two known exploited vulnerabilities to catalog (Aug 20, 2026)</a></li>'''))

rw('cyber-briefing.html', cy)


# ---------------------------------------------------------------- WALL STREET
ws = []
ws.append((
'<li><b>Monday &mdash; Bessent press conference on Iran.</b> Treasury Secretary Scott Bessent is due to unveil details of the US plan to economically isolate Iran, the latest phase of the Middle East conflict. Earlier in the week President Trump threatened "TREMENDOUS Economic Consequences" for any country trading with Iran, putting the focus on China, which sources oil from the Gulf.</li>',
'<li><b>Monday, August 24 &mdash; Bessent press conference on Iran.</b> Treasury Secretary Scott Bessent is due to detail the US plan to economically isolate Iran and its trading partners. He has described it as "the greatest co-ordinated economic isolation in the history of the world," combining the naval blockade with what he called the toughest sanctions in history, and framed the choice for other countries as "whether you are either with us or against us." Al Jazeera reports he said the measures would "collapse" Iran\'s economy; CNBC reports he also said the US likely would not restart large-scale combat. Earlier in the week President Trump threatened "TREMENDOUS Economic Consequences" for any country trading with Iran, putting the focus on China, which sources oil from the Gulf.</li>'))
ws.append((
'<li><a href="https://www.cnbc.com/2026/08/20/stock-market-today-live-updates.html">CNBC &mdash; Dow surges 500 points Friday, but index posts back-to-back weekly losses</a></li>',
'''<li><a href="https://www.cnbc.com/2026/08/20/stock-market-today-live-updates.html">CNBC &mdash; Dow surges 500 points Friday, but index posts back-to-back weekly losses</a></li>
<li><a href="https://www.cnbc.com/2026/08/20/bessent-economy-iran-war-trump.html">CNBC &mdash; Bessent says US likely won\'t restart large-scale Iran combat as it steps up economic pressure</a></li>
<li><a href="https://www.aljazeera.com/news/2026/8/20/us-treasury-secretary-says-new-economic-measures-will-collapse-iran">Al Jazeera &mdash; US Treasury secretary says new economic measures will "collapse" Iran</a></li>
<li><a href="https://www.thenationalnews.com/news/us/2026/08/20/bessent-iran-sanctions/">The National &mdash; Bessent vows to isolate Iran\'s economy as US increases pressure on allies</a></li>
<li><a href="https://www.caixinglobal.com/2026-08-22/the-week-ahead-aug-24-30-us-to-unveil-plan-isolating-irans-economy-102476708.html">Caixin Global &mdash; The Week Ahead (Aug. 24&ndash;30): US to unveil plan isolating Iran\'s economy</a></li>'''))
rw('wallstreet-briefing.html', ws)


# ---------------------------------------------------------------- MMA
mm = []
mm.append((
'<div class="tldr"><b>Tale of the Tape</b> <span>UFC Sacramento is live tonight from the Golden 1 Center, with No. 6 middleweight Anthony Hernandez meeting No. 11 Gregory Rodrigues in a five-round main event &mdash; no results had been posted by any primary source at press time.</span></div>',
'<div class="tldr"><b>Tale of the Tape</b> <span>UFC Sacramento\'s prelims are roughly an hour deep at the Golden 1 Center and the main card is still to come at 8 PM ET, but every primary source checked for this edition was still showing blank result fields, so no winners are published here.</span></div>'))
mm.append((
'<p class="note">No results are published on this page. As of press time, UFC.com\'s live card, Sherdog\'s play-by-play and FightBook MMA\'s results page all still showed blank result fields for every bout, including the prelims. Aggregated search summaries circulating tonight assert several prelim winners, but none of the three primary sources checked this run confirms them, so nothing is asserted here. Results will appear in the next edition once a primary source posts them.</p>',
'<p class="note"><b>No results are published on this page.</b> Re-checked for this edition with the prelims about an hour old: UFC.com has now posted its dedicated <i>UFC Sacramento Prelim Results</i> page, but the page still carries only fight previews with no winners, methods or times; Sherdog\'s play-by-play shows an empty "The Official Result" heading under all thirteen bouts; and FightBook MMA reads "Result: TBD" on every line. Aggregated search summaries continue to assert prelim winners, and one of them mis-dated the event by a day, so none is treated as reliable. Winners will be published in the next edition once a primary source posts them.</p>'))
rw('mma-briefing.html', mm)


# ---------------------------------------------------------------- INDEX
ix = []
ix.append((
'<h2>Seven federal patch deadlines have already passed</h2>\n<p>A GitLab code-injection flaw rated CVSS 9.4 is being exploited in the wild within days of disclosure, Cisco has patched nine Crosswork and Secure Workload bugs including five scoring a maximum 10.0, and seven entries in CISA\'s Known Exploited Vulnerabilities catalog are now past their federal remediation deadline.</p>',
'<h2>A named group is behind tomorrow\'s federal patch deadline</h2>\n<p>The TrueConf Server flaw federal agencies must fix by tomorrow now carries a CVSS of 9.3 and an attacker &mdash; the Head Mare group, which used it to swap client downloads for malware. A GitLab flaw rated 9.4 remains under active exploitation, and seven KEV entries are already past due.</p>'))
ix.append((
'<h2>A Friday bounce that didn\'t save the week</h2>\n<p>US markets are closed for the weekend: stocks rose on Friday &mdash; the Dow up about 1% &mdash; but all three major indexes still finished the week lower after a bond sell-off, while bitcoin logged its best week in two years.</p>',
'<h2>A Friday bounce that didn\'t save the week</h2>\n<p>US markets are closed for the weekend: stocks rose on Friday &mdash; the Dow up about 1% &mdash; but all three major indexes still finished the week lower after a bond sell-off. Attention now turns to Monday, when Bessent details the plan to economically isolate Iran.</p>'))
ix.append((
'<h2>Sacramento is live, and the scorecards are blank</h2>\n<p>UFC Sacramento is live tonight from the Golden 1 Center, with No. 6 middleweight Anthony Hernandez meeting No. 11 Gregory Rodrigues in a five-round main event &mdash; no results had been posted by any primary source at press time.</p>',
'<h2>Sacramento is live, and the scorecards are blank</h2>\n<p>UFC Sacramento\'s prelims are roughly an hour deep at the Golden 1 Center and the main card is still to come at 8 PM ET, but every primary source checked for this edition was still showing blank result fields, so no winners are published.</p>'))
rw('index.html', ix)

print("ALL EDITS APPLIED")
