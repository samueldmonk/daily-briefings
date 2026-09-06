# -*- coding: utf-8 -*-
"""Afternoon Edition edits, Sunday 6 September 2026, ~5:05pm ET run (archive stamp 1711)."""
import re, sys

def rep(t, old, new, label):
    if old not in t:
        sys.exit("MISS: " + label)
    if t.count(old) != 1:
        sys.exit("NOT UNIQUE (%d): %s" % (t.count(old), label))
    return t.replace(old, new)

# ───────────────────────── WALL STREET ─────────────────────────
w = open('wallstreet-briefing.html').read()

w = rep(w,
 'sending the 10-year yield to 4.79% and hardening the case for a Fed hike at the 15&ndash;16 September meeting.',
 'but the case for a Fed hike at the 15&ndash;16 September meeting has since softened, with governor Christopher Waller saying he would be inclined to hold if next Friday&rsquo;s CPI cools and CME FedWatch odds falling back to roughly even.',
 'WS tldr')

w = rep(w,
 '<tr><td>US 10-year Treasury yield</td><td><b>4.79%</b></td><td class="mut">Rose nearly 3 basis points Friday on the payrolls beat.</td></tr>',
 '<tr><td>US 10-year Treasury yield</td><td><b>Not asserted</b></td><td class="mut">Withdrawn this run. Previous editions carried <b>4.79%</b> for Friday; two independent returns fetched this run both put the note at <b>~4.76%</b> on Friday, and one adds that it <b>fell to 4.74% on Thursday</b> after touching <b>4.81%</b> earlier in the week. Thursday plus the roughly 3 basis points reported for Friday lands near 4.77%, not 4.79%, so the fresher pair is not a rounding of the figure this desk had published. A yield is a single number, so the conflict is printed and no level is carried. The direction &mdash; higher on the week, then lower after Waller &mdash; is not in dispute. On the superlative the sources also split: two returns put the 10-year at <b>three-year highs</b> / its <b>highest since November 2023</b> earlier in the week, while a third said &ldquo;highest since January 2025&rdquo;; the first two agree with each other and the third does not, so no record claim is asserted for the 10-year. The January 2025 comparison printed above under The Lead belongs to the <b>2-year</b>, a different instrument.</td></tr>',
 'WS 10Y row')

old_rate = re.search(r'<li><b>The rate call is genuinely contested.*?</li>', w, re.S).group(0)
new_rate = ('<li><span class="t new" style="margin-right:7px">New</span><b>The rate call is genuinely contested, and the most authoritative account of it landed on Thursday.</b> '
 'Associated Press, published by PBS NewsHour at <span style="font-family:var(--mono);font-size:12.5px">8:08 PM ET on 3 September</span> and fetched directly this run, reports that Fed governor '
 '<b>Christopher Waller</b> said the August inflation report due <b>Friday 11 September</b> will largely determine whether he supports a hike. If that report shows inflation continuing to cool, Waller '
 '&ldquo;would be inclined&rdquo; to keep the benchmark rate unchanged. &ldquo;But if inflation comes in hot, I would consider a rate hike,&rdquo; he said, adding that borrowing costs are only '
 '&ldquo;slightly restricting&rdquo; demand and that &ldquo;it may not take much acceleration in inflation to nudge me into supporting&rdquo; one. In a Reuters interview afterwards: &ldquo;I&rsquo;m '
 'willing to sit and wait and be patient &hellip; But if it reverses, then you know it&rsquo;s time to pull the trigger and hike rates.&rdquo; '
 '<b>Stocks rose and bond yields fell</b> on the remarks. '
 '<b>The odds moved with him.</b> Per AP citing CME FedWatch, investors had raised September hike odds to <b>nearly 65% by Wednesday</b>; after Waller spoke they fell to <b>roughly 50-50</b>. That is a '
 'dated, sourced sequence rather than a spot figure, and it supersedes the week-old 66.1% reading this desk printed in earlier editions. No single current probability is published here. '
 '<b>He is not alone.</b> New York Fed president <b>John Williams</b> said on Wednesday he too has been encouraged by recent inflation data but wants more evidence: &ldquo;I think that we have to wait '
 'and see. There&rsquo;s no clear signs right now whether monetary policy currently is sufficient.&rdquo; Against them, Chair <b>Kevin Warsh</b> told Jackson Hole that inflation had not improved enough '
 'and the Fed might have &ldquo;more work to do.&rdquo; <b>Joseph Purtell</b>, portfolio manager at Neuberger, told AP the meeting &ldquo;is going to be knife edge and it&rsquo;s going to come down to how '
 'the CPI data prints,&rdquo; and that Warsh could probably command a majority for either holding or raising. Separately, Vice President <b>JD Vance</b> said on Thursday the administration believes '
 '&ldquo;the Fed should be lowering interest rates&rdquo; &mdash; a third position, and not one held by anyone with a vote. '
 '<b>What the Fed&rsquo;s own gauge shows.</b> Per AP, prices <b>ticked down 0.1% from May to June</b> and <b>rose 0.2% from June to July</b>; annual inflation on that measure was last reported at '
 '<b>3.7%</b>, a figure a second independent return this run also gave for July. '
 '<span class="mut">Two readings are refused. A search summary attributed to Waller a three-month rate falling &ldquo;from 4.76% in February to 3.05%&rdquo;; no fetched page carries those numbers, and '
 '4.76% is also this run&rsquo;s contested 10-year level, so the pair is not printed. A second summary headlined Waller as calling for a 25 basis point <b>cut</b> &mdash; the opposite of what the AP '
 'account he is quoted in says, and refused outright. Earlier editions&rsquo; 58% / ~56% / 60% post-Jackson-Hole readings and Goldman Sachs&rsquo; &ldquo;very unlikely&rdquo; call are dropped rather than '
 'stacked: they all predate Thursday.</span></li>')
w = rep(w, old_rate, new_rate, 'WS rate call')

w = rep(w,
 '</a><a href="https://www.morningstar.com/economy/august-cpi-report-forecasts-point-sticky-inflation-tariff-pressures">Morningstar &mdash; August CPI forecasts point to sticky inflation</a>',
 '</a> &nbsp;&middot;&nbsp; <a href="https://www.morningstar.com/economy/august-cpi-report-forecasts-point-sticky-inflation-tariff-pressures">Morningstar &mdash; August CPI forecasts point to sticky inflation</a>'
 ' &nbsp;&middot;&nbsp; <a href="https://www.pbs.org/newshour/economy/fed-governor-waller-muddies-outlook-on-possible-rate-hike-later-this-month">PBS NewsHour / Associated Press &mdash; Waller muddies outlook on a possible rate hike this month</a>'
 ' &nbsp;&middot;&nbsp; <a href="https://www.semafor.com/article/09/03/2026/us-fed-governor-waller-floats-september-rate-hold">Semafor &mdash; US Fed governor Waller floats September rate hold</a>'
 ' &nbsp;&middot;&nbsp; <a href="https://tradingeconomics.com/united-states/government-bond-yield">Trading Economics &mdash; US 10-year Treasury note yield</a>',
 'WS sources')

open('wallstreet-briefing.html','w').write(w)

# ───────────────────────── CYBER ─────────────────────────
c = open('cyber-briefing.html').read()

c = rep(c,
 'while a second unpatched-at-exploitation chain, MikroTik&rsquo;s &ldquo;MikroTrick,&rdquo; drew an independent breakdown today that puts a public exploit one to two days away.',
 'and the only fixes that exist are unofficial ones two developers wrote independently of each other, while a second unpatched-at-exploitation chain, MikroTik&rsquo;s &ldquo;MikroTrick,&rdquo; drew a breakdown today that puts a public exploit one to two days away.',
 'CY tldr')

c = rep(c,
 '<div class="stat"><div class="n">4 of 4</div><div class="l">AI tools Raiu asked to reproduce the MikroTrick exploit that failed to produce a working one &mdash; one refused outright</div></div>',
 '<div class="stat"><div class="n">4 of 4</div><div class="l">AI tools Raiu asked to reproduce the MikroTrick exploit that failed to produce a working one &mdash; one refused outright</div></div>\n'
 '<div class="stat"><div class="n">3</div><div class="l">Unofficial StyleSmuggler mitigations in circulation &mdash; Disrex, ProxiBlue and Graycore &mdash; against zero from Adobe, per The Hacker News</div></div>',
 'CY stat strip')

c = rep(c,
 '<b>One item is tagged New this edition, and it is the first on this page in three runs.</b>',
 '<b>Two items are tagged New this edition.</b>',
 'CY newnote head')

c = rep(c,
 'so the tag is earned rather than assumed. Everything else on the page was re-checked and carried: StyleSmuggler&rsquo;s Disrex incident response, CrowdStrike SafeMind, the StyleSmuggler vulnerability row and Cisco Nexus 9000 all remain <b>Carried forward</b>. <b>Cyber carries 1 New tag, Wall Street 1, MMA 0.</b>',
 'so the tag is earned rather than assumed. The second is the StyleSmuggler mitigation card below: <span style="font-family:var(--mono);font-size:12.5px">thehackernews.com</span>&rsquo;s report was fetched directly this run and carries a post-publication update that was not in any earlier edition &mdash; the terms &ldquo;ProxiBlue,&rdquo; &ldquo;Graycore,&rdquo; &ldquo;Bouma&rdquo; and &ldquo;eComscan&rdquo; each return zero matches in <span style="font-family:var(--mono);font-size:12.5px">archive/cyber-2026-09-06-1641.html</span>. Everything else on the page was re-checked and carried: CrowdStrike SafeMind, the StyleSmuggler vulnerability row and Cisco Nexus 9000 all remain <b>Carried forward</b>. <b>Cyber carries 2 New tags, Wall Street 1, MMA 0.</b>',
 'CY newnote tail')

# New card, inserted directly after the existing StyleSmuggler victims card
anchor = ('Hosting providers <b>Nexcess and Liquid Web</b> posted identical precautionary notices on 5 September; '
          'neither claims a confirmed customer compromise.</p>\n</div>')
newcard = anchor + '\n' + (
 '<div class="card">\n<div class="tags"><span class="t hot">E-commerce</span><span class="t new">New</span></div>\n'
 '<h3>Two developers wrote the same StyleSmuggler fix without talking &mdash; and the scanner missed the implant</h3>\n'
 '<p>The Hacker News&rsquo; report was fetched directly this run and carries a post-publication update, sourced to Disrex co-founder <b>Rick Bouma</b>, that materially changes what a merchant can do today. '
 'With no vendor fix, three unofficial mitigations are now in circulation &mdash; from <b>Disrex</b>, <b>ProxiBlue</b> and <b>Graycore</b>.</p>\n'
 '<p><b>The convergence is the story.</b> Disrex&rsquo;s main mitigation adds a check to three methods in Magento&rsquo;s dependency-injection code scanners so they cannot run outside the command line. '
 'A GitHub user, <b>ProxiBlue</b> &mdash; whom Bouma identifies as Magento developer <b>Lucas van Staden</b> &mdash; published the same guard on <b>5 September</b> without coordination: the same three '
 'scanner methods, the same <span style="font-family:var(--mono);font-size:12.5px">PHP_SAPI !== &rsquo;cli&rsquo;</span> check, the same exception message. Disrex has reproduced ProxiBlue&rsquo;s patches in '
 'its own repository with credit, warns that the two are the same fix and <b>must not be applied on top of each other</b>, and regards the independent convergence as strong corroboration that it is the right '
 'one. <b>Graycore, LLC</b> published a separate Magento module hardening three points on the chain. '
 '<span class="mut">Neither Sansec nor Adobe has confirmed that these scanners are where the chain ends, and Graycore&rsquo;s own README says &ldquo;that is hardening, not a fix.&rdquo; One caution carried '
 'from the source: one of the three files, ClassesScanner.php, is called over HTTP by at least one third-party module, so guarding it breaks that module&rsquo;s admin screen.</span></p>\n'
 '<p><b>The scanner reported a compromised store clean.</b> eComscan ran on Store A at <b>10:00 UTC on 5 September</b>, roughly eleven hours after the implant first ran and while <b>1,728</b> cron lines were '
 'present, and returned clean. Disrex attributes this to scope rather than a scanner fault: the scheduled scan pointed at the store&rsquo;s document root, and the implant had installed one directory above it, '
 'under the account&rsquo;s home directory. The lesson is a scan path, not a product verdict.</p>\n'
 '<p><b>The implant, and the tell that found it.</b> Disrex describes the binary as a stripped, statically linked <b>Rust</b> program of roughly <b>1.9 MB</b> built for x86-64 and arm64, and notes the build '
 'running in memory on one store differed from the file on disk &mdash; so hash <span style="font-family:var(--mono);font-size:12.5px">/proc/&lt;pid&gt;/exe</span> as well as the file. What actually surfaced '
 'one of the two compromises was an email: the store sent its own owner a failed-transaction notice whose template variables were never resolved &mdash; a body of raw <span style="font-family:var(--mono);'
 'font-size:12.5px">{{var &hellip;}}</span> tags, a customer address on a <span style="font-family:var(--mono);font-size:12.5px">.invalid</span> domain and a total of zero. It reads like a broken order, Bouma '
 'said, but it is exhaust from the exploitation attempt passing through Magento&rsquo;s template filter. Disrex calls it the single most useful early-warning sign for merchants because noticing it needs no tooling.</p>\n'
 '<p class="mut">Two corrections travel with the update and are printed rather than smoothed over: Bouma revised the compromised stores&rsquo; versions and first-contact times &mdash; <b>Store A</b> ran '
 '<b>2.4.8</b> and was hit at 23:10 UTC on 4 September, <b>Store B</b> ran <b>2.4.7-p2</b> and was first hit at 00:55 UTC on 5 September &mdash; and an earlier count of 28 attacker source addresses was reduced '
 'to <b>26</b> after two of Disrex&rsquo;s own verification servers were removed. Both stores were contained the same day, and Disrex reports no exfiltration, no rogue admin accounts, no payment skimmer and no '
 'database backdoor.</p>\n</div>')
c = rep(c, anchor, newcard, 'CY new card')

c = rep(c,
 'Sansec&rsquo;s interim measure is to <b>disable GraphQL</b>,',
 'Sansec&rsquo;s interim measure is to <b>disable GraphQL</b>, three unofficial mitigations now exist (Disrex, ProxiBlue, Graycore &mdash; see below, and note the first two are the same fix and must not be stacked),',
 'CY patch priority')

open('cyber-briefing.html','w').write(c)

# ───────────────────────── MMA ─────────────────────────
m = open('mma-briefing.html').read()

m = rep(m,
 'and the sixth consecutive edition in which the two have failed to converge',
 'and the eighth consecutive edition in which the two have failed to converge',
 'MMA refusal count')

m = rep(m,
 'byte-for-byte the timestamp recorded three runs ago, so the promotion has not revised it.',
 'byte-for-byte identical across five consecutive runs now, so the promotion has not revised it.',
 'MMA modified_time count')

m = rep(m,
 'Also booked: <b>Renato Moicano vs. Brian Ortega 2</b>, <b>Patricio Pitbull vs. Doo Ho Choi</b>, <b>Charles Jourdain vs. Marlon Vera</b>, and Gable Steveson. Thirteen fights.',
 'Also booked: <b>Renato Moicano vs. Brian Ortega 2</b>, <b>Patricio Pitbull vs. Doo Ho Choi</b>, <b>Charles Jourdain vs. Marlon Vera</b>, <b>Alonzo Menifield vs. Iwo Baraniewski</b> and Gable Steveson. Thirteen fights. The card is the promotion&rsquo;s <b>sixth visit to Los Angeles and its first since UFC 227 in August 2018</b>.',
 'MMA UFC331 card')

m = rep(m,
 '<b>Gate and attendance, from UFC.com.</b>',
 '<b>Gate and attendance, from UFC.com &mdash; re-fetched directly this run.</b> UFC.com&rsquo;s own bonus page was pulled again this edition and every figure below matched what this page already carried, as did all four bonus names and the absence of a Fight of the Night award.',
 'MMA gate refetch')

open('mma-briefing.html','w').write(m)
print("edits applied OK")
