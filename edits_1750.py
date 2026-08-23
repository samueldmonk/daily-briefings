#!/usr/bin/env python3
"""Edition edits for 2026-08-23 ~5:50 PM ET (Afternoon Edition).
Prior archived snapshot: 2026-08-23-1610. New tags scoped against that snapshot.
Run: python3 edits_1750.py <repo_dir>
"""
import sys, io, os

D = sys.argv[1] if len(sys.argv) > 1 else '.'
fails = []

def edit(fn, pairs):
    p = os.path.join(D, fn)
    s = io.open(p, encoding='utf-8').read()
    for i, (old, new) in enumerate(pairs):
        if old not in s:
            fails.append('%s pair#%d NOT FOUND: %s' % (fn, i, old[:80]))
            continue
        if s.count(old) != 1:
            fails.append('%s pair#%d NOT UNIQUE (%d): %s' % (fn, i, s.count(old), old[:80]))
            continue
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- CYBER
edit('cyber-briefing.html', [
# 1. stat strip: add the Dahua figure (5th stat)
('<div class="stat"><div class="n">245M</div><div class="l">Downloads of the hit Rust crates</div></div>',
 '<div class="stat"><div class="n">245M</div><div class="l">Downloads of the hit Rust crates</div></div>\n'
 '<div class="stat"><div class="n">14,530</div><div class="l">Dahua devices hijacked in 35 days</div></div>'),

# 2. new incident card: Operation CameraSwarm
('<div class="card">\n<div class="tags"><span class="tag hot">Supply chain</span><span class="tag">No CVE</span></div>',
 '<div class="card">\n'
 '<div class="tags"><span class="tag new">New</span><span class="tag hot">IoT</span><span class="tag">Operation CameraSwarm</span></div>\n'
 '<h3>One operator quietly took over 14,500 Dahua cameras</h3>\n'
 '<p>Hunt.io researchers reconstructed a 35-day campaign that compromised more than <strong>14,530 Dahua devices between June 17 and July 22, 2026</strong>, working from a 407 MB exposed working directory holding 2,616 files across 234 subdirectories &mdash; tooling, logs, shell history and campaign records. Three methods ran in parallel: credential attacks, two older authentication-bypass flaws (<strong>CVE-2021-33044</strong> and <strong>CVE-2021-33045</strong>), and a peer-to-peer relay that reached 283 cameras sitting behind NAT using nothing but a device serial number. A persistent account was configured on 1,923 cameras. Confirmed compromises cluster in Ukraine and Russia; language artifacts point to a Russian-speaking operator, but the activity has not been attributed to any named group or government.</p>\n'
 '</div>\n\n'
 '<div class="card">\n<div class="tags"><span class="tag hot">Supply chain</span><span class="tag">No CVE</span></div>'),

# 3. vulnerability table: add the Citrix row at the top
('<tbody>\n<tr><td>CVE-2026-19478</td>',
 '<tbody>\n'
 '<tr><td>CVE-2026-19490</td><td>9.3</td><td>NetScaler ADC &amp; NetScaler Gateway 14.1 before 14.1-73.32, 13.1 before 13.1-63.21 (plus FIPS/NDcPP builds)</td>'
 '<td><strong>New this edition.</strong> Authentication bypass using an alternate path (CWE-288) &mdash; remote, unauthenticated, no user interaction. Applies to appliances configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or an AAA virtual server; on newer vulnerable builds a configured SAML action is additionally required. Advisory published Aug 19. Rapid7 reported <strong>no evidence of in-the-wild exploitation</strong> as of that date, but urged emergency-basis patching; SecurityWeek headlined its coverage &ldquo;exploitation expected.&rdquo;</td></tr>\n'
 '<tr><td>CVE-2026-19478</td>'),

# 4. update the closing note (New-tag count + Citrix)
('The Hacker News front page was re-read again for this edition and its newest item is still dated August 22 (the TikTok settlement), so the top story is unchanged and nothing on this page is tagged New. The CISA KEV catalog mirror was also re-fetched this edition: the board below is unchanged at twelve tracked entries.',
 'The Hacker News front page still shows nothing newer than August 22 (the TikTok settlement), so the top story is unchanged. <strong>Two items are tagged New this edition</strong> &mdash; the Citrix NetScaler authentication bypass above and the Dahua camera campaign in Breaches &amp; Incidents &mdash; both absent from the previous archived snapshot. The Citrix 9.3 is the CVSS v4.0 base score carried in the vendor advisory and Rapid7&rsquo;s analysis; it is <em>not</em> a KEV entry and so does not appear in the federal-deadline board below, which is unchanged at twelve tracked entries after the catalog mirror was re-checked for this edition.'),

# 5. sources
('<li><a href="https://cvefeed.io/cisakev/cisa-known-exploited-vulnerability-catalog">',
 '<li><a href="https://www.rapid7.com/blog/post/etr-cve-2026-19490-critical-vulnerability-affecting-citrix-netscaler-adc-and-netscaler-gateway/">Rapid7 — ETR: CVE-2026-19490, critical vulnerability affecting Citrix NetScaler ADC and NetScaler Gateway (advisory published Aug 19, 2026)</a></li>\n'
 '<li><a href="https://www.helpnetsecurity.com/2026/08/21/citrix-netscaler-gateway-cve-2026-19490/">Help Net Security — Citrix urges customers to fix critical NetScaler authentication bypass (CVE-2026-19490)</a></li>\n'
 '<li><a href="https://www.securityweek.com/exploitation-expected-for-critical-authentication-bypass-patched-in-citrix-netscaler/">SecurityWeek — Exploitation expected for critical authentication bypass patched in Citrix NetScaler</a></li>\n'
 '<li><a href="https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised">Hunt.io — Operation CameraSwarm: over 14,000 Dahua cameras compromised across Ukraine and Russia</a></li>\n'
 '<li><a href="https://thehackernews.com/2026/08/hackers-compromised-14500-dahua-devices.html">The Hacker News — Hackers compromised 14,500+ Dahua devices using credential attacks, auth bypasses and P2P</a></li>\n'
 '<li><a href="https://www.bleepingcomputer.com/news/security/hackers-compromise-14-500-dahua-web-cameras-in-35-day-campaign/">BleepingComputer — Hackers compromise 14,500 Dahua web cameras in 35-day campaign</a></li>\n'
 '<li><a href="https://cvefeed.io/cisakev/cisa-known-exploited-vulnerability-catalog">'),
])

# ---------------------------------------------------------------- MMA
edit('mma-briefing.html', [
# 1. tldr
('<div class="tldr"><b>Tale of the Tape</b> <span>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win, split Fight of the Night with him, and called out No. 2-ranked Dricus du Plessis — and attention now turns to Shanghai, where the full Nurmagomedov vs Song card is set behind a Yan Xiaonan co-main.</span></div>',
 '<div class="tldr"><b>Tale of the Tape</b> <span>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win and called out No. 2-ranked Dricus du Plessis; since then the UFC has locked in its final two numbered cards of the year &mdash; UFC 334 at Madison Square Garden on Nov 14 and UFC 335 in Las Vegas on Dec 12 &mdash; and lost Yair Rodriguez from the Noche UFC main event, with Jose Delgado stepping in against Jean Silva.</span></div>'),

# 2. drop the stale New tag on Shanghai
('<div class="tags"><span class="tag new">New</span><span class="tag">Full card announced</span></div>',
 '<div class="tags"><span class="tag">Full card announced</span></div>'),

# 3. rebuild the Noche card
('<div class="dv">Sat, Sep 12 · Desert Diamond Arena, Glendale, AZ</div>\n<h3>Noche UFC: Yair Rodriguez vs Jean Silva</h3>\n<p>The annual Mexican Independence weekend card, with Brandon Moreno, Manon Fiorot vs Alexa Grasso and Curtis Blaydes vs Waldo Cortes-Acosta also listed on the UFC.com fight card. Main card 9:00 PM ET.</p>\n<div class="odds">Odds: not stated in any source fetched this run.</div>',
 '<div class="dv">Sat, Sep 12 · Desert Diamond Arena, Glendale, AZ</div>\n'
 '<div class="tags"><span class="tag new">New</span><span class="tag hot">Main event changed</span></div>\n'
 '<h3>Noche UFC 4: Jean Silva vs Jose Delgado</h3>\n'
 '<p><strong>Yair Rodriguez is out.</strong> The former interim featherweight champion withdrew from the headliner with a groin injury suffered in training &mdash; &ldquo;I got injured. I tried to continue my preparation, but ultimately, it wasn&rsquo;t responsible to compete under these conditions,&rdquo; he wrote on Instagram &mdash; and Jose Delgado (12-2) steps in on short notice against Jean Silva (17-3). Delgado is 4-1 in the UFC since earning his contract on Dana White&rsquo;s Contender Series in 2024 and has beaten Andre Fili and Austin Bashi this year. The annual Mexican Independence weekend card also lists Brandon Moreno, Manon Fiorot vs Alexa Grasso and Curtis Blaydes vs Waldo Cortes-Acosta. Main card 9:00 PM ET on Paramount+.</p>\n'
 '<div class="odds">Odds: Silva &minus;425 / Delgado +355 (FightOdds.io, via MMA Mania/Yahoo Sports). Odds against Rodriguez in the original booking no longer apply.</div>'),

# 4. drop the stale New tag on Szabova
('<div class="tags"><span class="tag new">New</span><span class="tag prospect">Prospect</span></div>',
 '<div class="tags"><span class="tag prospect">Prospect</span></div>'),

# 5. Around the sport: UFC 334/335 + NSAC purses, before "Next up"
('<li><strong>Next up.</strong> The promotion heads to Shanghai on Saturday, August 29 for Umar Nurmagomedov vs Song Yadong, then Paris on September 5.</li>',
 '<li><strong>The year&rsquo;s last two numbered cards are official.</strong> <span style="font-family:var(--mono);font-size:10px;letter-spacing:.11em;text-transform:uppercase;color:var(--up);border:1px solid rgba(63,191,127,.4);border-radius:5px;padding:2px 6px;margin-right:6px">New</span> UFC 334 goes to <strong>Madison Square Garden in New York on Saturday, November 14</strong>, and UFC 335 closes the year at <strong>T-Mobile Arena in Las Vegas on Saturday, December 12</strong>. UFC 334 is being billed as <strong>Polymarket UFC 334</strong> after the prediction market became the promotion&rsquo;s exclusive prediction-market partner &mdash; the first time that sponsorship has been folded into an event name. No bouts have been announced for either card.</li>\n'
 '<li><strong>Nevada is holding three UFC 329 purses.</strong> <span style="font-family:var(--mono);font-size:10px;letter-spacing:.11em;text-transform:uppercase;color:var(--up);border:1px solid rgba(63,191,127,.4);border-radius:5px;padding:2px 6px;margin-right:6px">New</span> The Nevada State Athletic Commission has withheld the fight purses of <strong>Max Holloway, Paddy Pimblett and Gable Steveson</strong> pending disciplinary hearings, after all three climbed out over the cage following their wins &mdash; a violation Nevada has enforced more strictly since Khabib Nurmagomedov jumped the fence at UFC 229. Holloway and Pimblett were both shown on the broadcast leaving the cage after first-round stoppages; Steveson was not caught on camera doing so. The hearings will decide whether the withheld money is returned or converted into fines. Pimblett&rsquo;s manager, Cage Warriors CEO Graham Boyland, texted MMA Junkie: &ldquo;For the record, this rule needs to be changed.&rdquo; The precedent is small &mdash; Diego Lopes had $5,000 of his $100,000 show money frozen for scaling the cage at UFC 300 and was fined $2,500 &mdash; but the amounts withheld here have not been disclosed.</li>\n'
 '<li><strong>Next up.</strong> The promotion heads to Shanghai on Saturday, August 29 for Umar Nurmagomedov vs Song Yadong, then Paris on September 5.</li>'),

# 6. sources
('<li><a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">',
 '<li><a href="https://www.espn.com/mma/story/_/id/49667048/rodriguez-silva-bout-ufc-noche-replaced-delgado">ESPN — Rodriguez out of Silva bout at Noche UFC, replaced by Delgado</a></li>\n'
 '<li><a href="https://www.cbssports.com/ufc/news/noche-ufc-main-event-jose-delgado-yair-rodriguez-jean-silva/">CBS Sports — Noche UFC main event: Jose Delgado to step in as replacement for Yair Rodriguez against Jean Silva</a></li>\n'
 '<li><a href="https://www.mmamania.com/ufc-odds/466248/noche-ufc-4-odds-betting-line-opens-jean-silva-vs-jose-delgado-main-event-its-not-close">MMA Mania — Noche UFC 4 odds: betting line opens for Jean Silva vs. Jose Delgado (Silva &minus;425 / Delgado +355, FightOdds.io)</a></li>\n'
 '<li><a href="https://mmasucka.com/news/yair-rodriguez-releases-statement-after-pulling-out-noche-ufc-4-i-got-injured/">MMA Sucka — Yair Rodriguez breaks silence on his Noche UFC 4 pullout</a></li>\n'
 '<li><a href="https://www.mmamania.com/upcoming-ufc-events/467073/dates-and-locations-revealed-for-last-major-ufc-events-of-2026">MMA Mania — Dates and locations revealed for the last major UFC events of 2026</a></li>\n'
 '<li><a href="https://www.forbes.com/sites/brianmazique/2026/08/22/ufc-334-and-335-announced-dates-and-venues-confirmed/">Forbes — UFC 334 and 335 announced: dates and venues confirmed (Aug 22, 2026)</a></li>\n'
 '<li><a href="https://sports.yahoo.com/articles/ufc-makes-final-two-numbered-153827373.html">Yahoo Sports — UFC makes final two numbered events of &rsquo;26 official in New York, Las Vegas</a></li>\n'
 '<li><a href="https://bloodyelbow.com/2026/08/22/paddy-pimbletts-manager-demands-common-sense-after-commission-withholds-his-ufc-329-purse/">Bloody Elbow — Paddy Pimblett&rsquo;s manager demands &lsquo;common sense&rsquo; after commission withholds his UFC 329 purse (Aug 22, 2026)</a></li>\n'
 '<li><a href="https://sports.yahoo.com/articles/three-ufc-329-stars-facing-184111177.html">Yahoo Sports — Three UFC 329 stars face purse withholdings; manager calls for rule change</a></li>\n'
 '<li><a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">'),
])

# ---------------------------------------------------------------- WALL STREET
edit('wallstreet-briefing.html', [
# 1. weekly percentages, more precise
('all four indexes finished the week lower: the S&amp;P 500 &minus;1.4%, the Nasdaq Composite &minus;2%, the Dow &minus;0.9% on the week.',
 'all four indexes finished the week lower: the S&amp;P 500 &minus;1.4%, the Nasdaq Composite &minus;2%, the Dow &minus;0.9% on the week. CNBC&rsquo;s week-ahead piece, re-checked for this edition, puts the weekly declines slightly more precisely at &minus;1.43% for the S&amp;P 500 and &minus;2.05% for the Nasdaq Composite.'),

# 2. Warsh time
('<li><strong>Friday, August 28 — Warsh at Jackson Hole.</strong> Fed Chair Kevin Warsh delivers his first Jackson Hole keynote as chair.',
 '<li><strong>Friday, August 28 — Warsh at Jackson Hole.</strong> Fed Chair Kevin Warsh delivers his first Jackson Hole keynote as chair, scheduled for <strong>10 a.m.</strong> Investors want his read on inflation and the rate path after an unusually divided July meeting, though he is expected to stick to his practice of avoiding forward guidance.'),

# 3. calendar note refresh
('<li><strong>Wednesday, August 26 — PCE <em>and</em> Nvidia.</strong> The Fed&rsquo;s preferred inflation gauge lands in the morning: July PCE (&minus;0.1% m/m previously, +3.7% y/y) and core PCE (+0.1% m/m, +3.3% y/y),',
 '<li><strong>Wednesday, August 26 — PCE <em>and</em> Nvidia.</strong> The Fed&rsquo;s preferred inflation gauge lands in the morning: July PCE (&minus;0.1% m/m previously, +3.7% y/y) and core PCE (+0.1% m/m, +3.3% y/y) &mdash; CNBC&rsquo;s week-ahead independently puts the consensus for the core annual rate at <strong>3.3%</strong> &mdash;'),
])

# ---------------------------------------------------------------- INDEX
edit('index.html', [
('<h2>Rodrigues survives 25 minutes with Fluffy — and wants du Plessis</h2>\n<p>Gregory Rodrigues took a unanimous decision over Anthony Hernandez in Sacramento to win his fourth straight, split Fight of the Night with him, and call out No. 2-ranked Dricus du Plessis. Attention now shifts to Shanghai on Saturday, where the full Nurmagomedov vs Song card is set behind a Yan Xiaonan co-main.</p>',
 '<h2>Rodrigues survives 25 minutes with Fluffy — and wants du Plessis</h2>\n'
 '<p>Gregory Rodrigues took a unanimous decision over Anthony Hernandez in Sacramento to win his fourth straight, split Fight of the Night with him, and call out No. 2-ranked Dricus du Plessis. Since then the UFC has made its last two numbered cards of the year official &mdash; UFC 334 at Madison Square Garden on November 14, UFC 335 in Las Vegas on December 12 &mdash; and lost Yair Rodriguez from the Noche UFC main event to a groin injury, with Jose Delgado stepping in against Jean Silva.</p>'),

('<h2>A 9.8-rated flaw already under attack comes due today</h2>\n<p>The federal patch deadline for TrueConf Server&rsquo;s CVE-2026-72529 &mdash; an unauthenticated script-execution bug CISA says is being exploited &mdash; lands today, while seven other entries in the Known Exploited Vulnerabilities catalog are already past due, the oldest by nine days. The catalog was re-checked for this edition and the board is unchanged.</p>',
 '<h2>A 9.8-rated flaw already under attack comes due today</h2>\n'
 '<p>The federal patch deadline for TrueConf Server&rsquo;s CVE-2026-72529 &mdash; an unauthenticated script-execution bug CISA says is being exploited &mdash; lands today, while seven other entries in the Known Exploited Vulnerabilities catalog are already past due, the oldest by nine days. New this edition: a critical Citrix NetScaler authentication bypass (CVE-2026-19490, CVSS 9.3) that researchers expect to be exploited, and a campaign that quietly hijacked more than 14,500 Dahua cameras in 35 days.</p>'),
])

print('FAILURES: %d' % len(fails))
for f in fails:
    print(' - ' + f)
