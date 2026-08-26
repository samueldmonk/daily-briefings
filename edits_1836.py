# -*- coding: utf-8 -*-
import re, io, sys

fails = []
def sub1(h, old, new, label):
    if h.count(old) != 1:
        fails.append("%s: anchor count=%d" % (label, h.count(old)))
        return h
    return h.replace(old, new, 1)

# ============================ CYBER ============================
c = open('cyber-briefing.html', encoding='utf-8').read()

# --- new tldr
old_tldr_start = c.find('<div class="tldr">')
old_tldr_end = c.find('</div>', c.find('</span>', old_tldr_start))
new_tldr = ('<div class="tldr"><b>The Wire</b> <span>The Justice Department and FBI have seized the domains behind '
 '<b>QScan</b> and <b>QTRouter</b>, two complementary hacking platforms built and run by a PRC state-sponsored group '
 'called <b>QTFY</b> and employed by the China-based <b>Nanjing Xinjiuwei Network Technology Company</b> &mdash; and the '
 'department&rsquo;s own list of victims of QTFY intrusion activity names <b>NASA, the Federal Reserve, the Departments of '
 'Energy, Justice and Health and Human Services, the National Institutes of Health and the U.S. Senate</b>; because the '
 'seized domains were hard-coded into both pieces of malware, the seizures made QScan and QTRouter inoperable.</span></div>')
c = c[:old_tldr_start] + new_tldr + c[old_tldr_end+6:]

# --- new top story, Boston Scientific demoted in place
anchor = '<div class="lab">Top story</div>\n<div class="lead">\n<h2>Boston Scientific'
new_top = '''<div class="lab">Top story</div>
<div class="lead">
<div class="tags"><span class="tag new">New &middot; 6:36</span><span class="tag crit">PRC state-sponsored</span><span class="tag warn">Botnet seizure</span><span class="tag">DOJ / FBI</span></div>
<h2>DOJ and FBI seize QScan and QTRouter &mdash; and name NASA, the Federal Reserve and the U.S. Senate among the victims</h2>
<p>The Justice Department press release was <b>fetched in full this run</b>, so this item rests on the primary source rather than on coverage of it. The department and the FBI announced <b>court-authorized domain seizures</b> today against <b>&ldquo;two complementary hacking platforms known as &lsquo;QScan&rsquo; and &lsquo;QTRouter,&rsquo; used to target U.S. critical infrastructure and other sensitive networks.&rdquo;</b> Court documents were unsealed in the <b>Southern District of California</b>. The operator is named: a PRC state-sponsored group known as <b>QTFY</b>, <b>employed by China-based Nanjing Xinjiuwei Network Technology Company</b>.</p>
<p><b>The victim list is the part that will travel.</b> DOJ states that among the victims of QTFY intrusion activity are the <b>National Aeronautics and Space Administration, the Federal Reserve, the Department of Energy, the Department of Justice, the Department of Health and Human Services, the National Institutes of Health, and the U.S. Senate</b>. &#9888; <b>DOJ does not state a breach date, a dwell time, a record count or an impact for any individual victim, and none is asserted here.</b></p>
<p><b>How the two platforms worked, in the department&rsquo;s own description.</b> QTFY <b>&ldquo;offers computer hacking services to its paying customers, including the PRC&rsquo;s Ministry of State Security and the People&rsquo;s Liberation Army.&rdquo;</b> <b>QScan</b> <b>&ldquo;scans and automatically infects thousands of &lsquo;internet-of-things&rsquo; (IoT) devices worldwide,&rdquo;</b> which are then added to <b>QTRouter</b> &mdash; a network of QTFY-controlled devices comprising those compromised IoT devices <b>plus commercial proxy service devices and leased virtual private servers</b>. QTRouter then serves as an <b>&ldquo;obfuscation network&rdquo;</b>, letting QTFY and other actors <b>conceal the PRC origin of their intrusions</b> because the traffic <b>&ldquo;appear[s] to originate from computers &hellip; that are outside of the PRC and may even be local to the targeted networks.&rdquo;</b></p>
<p><b>The seizure is a kill, not a takedown notice.</b> Because <b>the seized domains were hard-coded into both the QScan and QTRouter malware</b> and used for <b>essential tasks such as communication and authentication</b>, DOJ says <b>the court-authorized seizures made QScan and QTRouter inoperable</b>. Attorney General <b>Todd Blanche</b> called it <b>&ldquo;the latest in a series of technical operations to dismantle indiscriminate hacking activities sponsored by the People&rsquo;s Republic of China&rdquo;</b>; FBI Director <b>Kash Patel</b> described <b>&ldquo;the disruption of a global botnet and hacking platform.&rdquo;</b> Assistant Attorney General for National Security <b>John A. Eisenberg</b>, U.S. Attorney <b>Adam Gordon</b> for the Southern District of California and Special Agent in Charge <b>Mark Remily</b> of FBI San Diego are also quoted. Press release number <b>26-972</b>; published <b>8:20&nbsp;a.m. ET</b>, updated <b>10:22&nbsp;a.m. ET</b>.</p>
<p><b>Two artefacts for defenders, both named in the release.</b> The <b>FBI and NSA published a cybersecurity advisory providing indicators of compromise for QTFY</b>, based on analysis of activity <b>dating back to at least 2018</b>; and <b>Lumen Technologies&rsquo; Black Lotus Labs published a description of QTFY&rsquo;s tactics, techniques and procedures</b>. DOJ places the action in a line with three prior operations it names: the <b>2025</b> removal of <b>PlugX</b> malware from <b>over 4,000 U.S. computers</b> infected by <b>Mustang Panda</b>; the <b>2024</b> disabling of a botnet of <b>hundreds of thousands of IoT devices</b> supplied by <b>Flax Typhoon</b> to Chinese government customers; and the <b>2023</b> disruption of a botnet used by <b>Volt Typhoon</b>. &#9888; <b>No CVE, CVSS or patch is attached to this item &mdash; the seizure targets infrastructure, not a vulnerability, and nothing here is in KEV.</b> (U.S. Department of Justice, Office of Public Affairs.)</p>
</div>

<div class="lead" style="margin-top:22px">
<div class="tags"><span class="tag">Carried &middot; 6:06</span><span class="tag">SEC 8-K</span></div>
<h2>Boston Scientific'''
c = sub1(c, anchor, new_top, 'cyber-topstory')
# remove the now-duplicated <h2> opener remnant
c = c.replace('<h2>Boston Scientific&rsquo;s 8-K:', '<h2>Boston Scientific&rsquo;s 8-K:', 1)

# --- threat actor spotlight: QTFY card
sp = '<div class="lab">Threat actor spotlight</div>\n<div class="cards">\n'
qtfy = sp + '''<div class="card"><div class="tags"><span class="tag new">New &middot; 6:36</span><span class="tag crit">PRC state-sponsored</span><span class="tag">Obfuscation-as-a-service</span></div>
<h3>QTFY &mdash; a contractor that sells concealment rather than intrusion</h3>
<p><b>Named for the first time on this page, from the DOJ release fetched this run.</b> QTFY is a <b>PRC state-sponsored group employed by Nanjing Xinjiuwei Network Technology Company</b> that <b>&ldquo;offers computer hacking services to its paying customers, including the PRC&rsquo;s Ministry of State Security and the People&rsquo;s Liberation Army.&rdquo;</b> What makes it worth a spotlight entry is the <b>product shape</b>: QScan mass-infects IoT devices, QTRouter aggregates them with <b>commercial proxy services and leased VPSs</b> into an <b>obfuscation network</b>, and the value sold to the customer is that intrusions <b>appear to come from outside the PRC &mdash; sometimes from devices local to the target</b>. That is a quartermaster model, not an operator model, and it is the same pattern the <b>Flax Typhoon</b> botnet followed in 2024 when it was supplied to Chinese government customers. <b>FBI/NSA have published IOCs</b> covering activity <b>back to at least 2018</b>; <b>Lumen&rsquo;s Black Lotus Labs</b> has published the TTPs. &#9888; <b>No malware hashes, IP ranges or device counts are reproduced here &mdash; the release states none, and the IOC advisory itself was not fetched this run.</b> (U.S. DOJ.)</p>
</div>
'''
c = sub1(c, sp, qtfy, 'cyber-spotlight')

# --- KEV note
kev = '<div class="lab">CISA KEV &amp; federal deadlines</div>\n'
kev_new = kev + '''<p class="note"><b>&#9679; 6:36 &mdash; KEV static for a SEVENTEENTH consecutive edition, and today&rsquo;s federal cyber news does not touch the board.</b> A direct search this run again surfaced <b>no CISA alert page later than those already carried</b>; the visible alert pages remain <b>Aug&nbsp;18 (four)</b>, <b>Aug&nbsp;20 (two &mdash; TrueConf Server CVE-2026-72529 and CVE-2026-72530)</b> and <b>Aug&nbsp;21 (one &mdash; Zimbra CVE-2026-73570)</b>, with the <b>Gitea CVE-2026-60004 addition of August&nbsp;25</b> the latest entry on this board. The board holds at <b>14 rows</b>; nearest deadlines unchanged &mdash; <b>Oracle CVE-2026-21962 due August&nbsp;27</b> and <b>Gitea CVE-2026-60004 due August&nbsp;28</b>. <b>Patch Priority is unchanged.</b> &#9888; <b>The QScan/QTRouter seizure in the top story adds nothing to KEV</b> &mdash; it is an infrastructure disruption, not a vulnerability listing, and it carries no BOD 22-01 deadline. &#9888; <b>A search summary this run stated that CISA published a &ldquo;Vulnerability Review&rdquo; for fiscal years 2024 and 2025 on August&nbsp;26. The CISA resource page returned no body text when fetched, so nothing about that document &mdash; its existence, contents or date &mdash; is asserted on this page.</b></p>
'''
c = sub1(c, kev, kev_new, 'cyber-kev')

# --- breaches: rejection card for Tata + Taco Bell re-rejection
br = '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
br_new = br + '''<div class="card"><div class="tags"><span class="tag new">New &middot; 6:36</span><span class="tag warn">Rejected as current</span><span class="tag">Recycled June story</span></div>
<h3>An item that came back as today&rsquo;s news and is ten weeks old: the Tata Electronics leak</h3>
<p>A search for <b>&ldquo;cybersecurity news August 26 2026 data breach ransomware&rdquo;</b> returned, as a current item, that <b>Tata Electronics confirmed an incident after the World&nbsp;Leaks group published more than 200,000 alleged company files</b>. Follow-up searching dated it precisely and it is <b>not today&rsquo;s news</b>: World&nbsp;Leaks posted <b>204,341 files totalling 630.4&nbsp;GB</b> on <b>June&nbsp;12, 2026</b>, and <b>Tata Electronics confirmed the incident on June&nbsp;22</b>, saying it caused <b>no disruption to operations</b>. <b>Nothing about it is published as a current breach on this page.</b> It is recorded here only so a later edition does not pick the same summary up and run it as new. &#9888; <b>No claim about the contents of the leaked cache &mdash; the supplier documents, the customer names or the personal data reported in that coverage &mdash; is asserted, verified or endorsed here.</b></p>
<p><b>&#9679; And the Taco Bell / Pizza Hut headline returned too, for a third time.</b> The same summary again carried <b>&ldquo;a Taco Bell and Pizza Hut operator disclosed a breach after suspicious network activity on August&nbsp;26&rdquo;</b>. That headline was <b>examined and rejected at 4:15</b> when follow-up searches produced <b>only the 2023 Yum!&nbsp;Brands ransomware incident and no 2026 body text</b>. <b>It stays rejected. Nothing about it is asserted.</b> <b>RULE: a summary that dates a story to the query date is dating it to the query, not to the event.</b></p>
</div>
'''
c = sub1(c, br, br_new, 'cyber-breaches')

# --- sources footer
src_anchor = '<div class="lab">Sources</div>'
if c.count(src_anchor) == 1:
    ins = c.find('</p>', c.find(src_anchor))
    c = (c[:ins] + ' &middot; <a href="https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers">'
         'U.S. Department of Justice, &ldquo;Justice Department and FBI Seize Platforms Operated and Used by China State-Sponsored Hackers to Target U.S. Critical Infrastructure&rdquo; (press release 26-972, Aug&nbsp;26, 2026)</a>'
         ' &middot; <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA Known Exploited Vulnerabilities Catalog</a>' + c[ins:])
else:
    fails.append('cyber-sources')

# ============================ WALL STREET ============================
w = open('wallstreet-briefing.html', encoding='utf-8').read()

t0 = w.find('<div class="tldr">')
t1 = w.find('</div>', w.find('</span>', t0))
new_wtldr = ('<div class="tldr"><b>The Tape</b> <span>The night settles the way the call pointed: with the conference call over, '
 '<b>CNBC&rsquo;s live blog reports Nvidia shares up more than 4% in extended trading</b> and stock futures rising with them, '
 'after a quarter it describes as beating forecasts <b>by the largest margin in two years</b> &mdash; a third timestamped read that sits '
 'between the <b>&minus;1% / &minus;1.3%</b> observed before the call and the <b>~&plus;5%</b> peak seen at 5:10&nbsp;p.m., '
 'none of which this page merges or retracts.</span></div>')
w = w[:t0] + new_wtldr + w[t1+6:]

ah = '<div class="lab">After-hours movers</div>\n'
ah_new = ah + '''<p class="note"><b>&#9679; 6:36 &mdash; THE CALL IS OVER AND THE NIGHT HAS A THIRD READ: <span class="up">more than &plus;4%</span>.</b> CNBC&rsquo;s markets live blog is now headlined <b>&ldquo;Stock futures rise as Nvidia shares jump 4% after earnings&rdquo;</b>, and reports that <b>Nvidia added more than 4% after beating analyst expectations and forecasting strong revenue growth ahead</b>, with the fiscal second quarter <b>surpassing forecasts by its largest amount in two years</b>. <b>This is the first read taken after the conference call ended</b>, which makes it the most settled figure of the night &mdash; and it is <b>lower than the ~&plus;5% peak</b> Kiplinger recorded at <b>5:10&nbsp;p.m.</b>, exactly as that blog&rsquo;s own <b>5:24</b> entry (&ldquo;down some from its after-hours peak&rdquo;) predicted. &#9888; <b>ALL THREE READS STAND AS PUBLISHED: &minus;1.3% (Kiplinger, ~4:50, pre-call), &minus;1% (Investing.com, ~5:36), ~&plus;5% (Kiplinger, 5:10, on the call) and now &gt;&plus;4% (CNBC, post-call).</b> They are four observations of a live price at four different moments, not four competing answers to one question, and <b>nothing is averaged, reconciled or retracted.</b> <b>No after-hours dollar level is asserted.</b> (CNBC.)</p>
<p class="note"><b>&#9679; 6:36 &mdash; Okta gets a third read too: <span class="up">&plus;19%</span>.</b> A search summary this run puts the gain at <b>19%</b>, against <b>~15% (CNBC, ~5:06)</b> and <b>17% (Investing.com, ~5:36)</b>. <b>Same rule, same treatment: printed with its time, adopted over neither of the others.</b> The underlying figures are unchanged and were already verified &mdash; <b>adjusted EPS $1.05 vs 97 cents expected</b> on <b>revenue $805&nbsp;million vs $795&nbsp;million expected</b>, with <b>full-year guidance raised</b>.</p>
<p class="note"><b>&#9888; 6:36 &mdash; THE AUGUST&nbsp;25 CLOSING SET WAS OFFERED A THIRD TIME AND IS REJECTED A THIRD TIME.</b> A search for the August&nbsp;26 close again returned <b>S&amp;P 500 7,677.24 (&plus;24.38, &plus;0.3%) / Dow 53,577.40 (&plus;160.24) / Nasdaq 26,151.30 (&plus;171.11)</b>. <b>7,677.24 is a standing rejected figure in this desk&rsquo;s corrections file</b> and the set traces to <b>a CNBC article dated August&nbsp;25</b>, not August&nbsp;26. <b>The August&nbsp;26 close on this page stands: 7,675.70, &minus;1.58, &minus;0.02%</b>, which reconciles against the <b>7,677.28</b> Tuesday close. <b>Not merged, not published.</b></p>
'''
w = sub1(w, ah, ah_new, 'ws-afterhours')

s2 = '<div class="lab">Sources</div>'
if w.count(s2) == 1:
    ins = w.find('</p>', w.find(s2))
    w = (w[:ins] + ' &middot; <a href="https://www.cnbc.com/2026/08/26/stock-market-today-live-updates.html">CNBC, &ldquo;Stock futures rise as Nvidia shares jump 4% after earnings: Live updates&rdquo; (Aug&nbsp;26, 2026)</a>' + w[ins:])
else:
    fails.append('ws-sources')

# ============================ MMA ============================
m = open('mma-briefing.html', encoding='utf-8').read()

m0 = m.find('<div class="tldr">')
m1 = m.find('</div>', m.find('</span>', m0))
new_mtldr = ('<div class="tldr"><b>Tale of the Tape</b> <span>Nothing in the sport moved in the last half hour: '
 '<b>UFC Shanghai &mdash; Umar Nurmagomedov vs. Song Yadong, Saturday August&nbsp;29 at the Oriental Sports Center</b> &mdash; '
 'remains the next card with the consensus line re-confirmed at <b>Nurmagomedov &minus;500 / Song &plus;380</b>, the most recent '
 'completed event remains <b>Hernandez vs. Rodrigues in Sacramento on August&nbsp;22</b>, and the champions board is unchanged for a '
 '<b>thirty-third consecutive edition</b>; the one thing this run turned up is that the two headliners&rsquo; exact rankings are '
 'reported two different ways, so this page asserts neither.</span></div>')
m = m[:m0] + new_mtldr + m[m1+6:]

fw = '<div class="lab">Fight week &mdash; upcoming cards</div>\n'
fw_new = fw + '''<p class="note"><b>&#9679; 6:36 &mdash; the card is unchanged and the line is unchanged; one new wrinkle, and it is a disagreement about numbers.</b> Fresh searching re-confirms the headliner, the venue and the date &mdash; <b>Umar Nurmagomedov vs. Song Yadong, Oriental Sports Center, Shanghai, August&nbsp;29</b> &mdash; and re-confirms the consensus odds at <b>Nurmagomedov &minus;500 / Song &plus;380</b>, roughly <b>80% / 20%</b> market-implied. &#9888; <b>THE FIGHTERS&rsquo; RANKINGS ARE REPORTED TWO WAYS AND NEITHER IS ADOPTED.</b> <b>UFC.com&rsquo;s own preview headline</b> bills the bout as <b>&ldquo;#3 Umar Nurmagomedov and #5 Song Yadong&rdquo;</b>; <b>a summary of that same coverage</b> instead says the two are <b>&ldquo;ranked No.&nbsp;2 and No.&nbsp;6 in the latest Meta UFC rankings at 135 pounds.&rdquo;</b> <b>Both readings are printed; this page asserts no numeric rank for either man</b> and says only that both are ranked bantamweight contenders. Records as stated in that coverage: <b>Nurmagomedov 20-1</b>, out of <b>Dagestan, Russia</b>, on a <b>two-fight win streak</b> since challenging for the bantamweight title; <b>Song Yadong &ldquo;The Kung Fu Kid&rdquo; 23-9-1</b>, out of <b>Heilongjiang, China</b>, making his <b>sixth main-event appearance</b> after a <b>submission win over former UFC flyweight champion Deiveson Figueiredo at UFC Fight Night Macau in May</b>. &#9888; <b>Fight week has begun &mdash; the two had their first face-off &mdash; but the card has not taken place and no result is asserted for any bout on it.</b></p>
'''
m = sub1(m, fw, fw_new, 'mma-fightweek')

cb = '<div class="lab">Champions board</div>\n'
cb_new = cb + '''<p class="note"><b>&#9679; 6:36 &mdash; unchanged for a THIRTY-THIRD consecutive edition, and re-checked rather than re-copied.</b> No event has taken place since <b>UFC Fight Night: Hernandez vs. Rodrigues, August&nbsp;22, Golden&nbsp;1 Center, Sacramento</b>, which was <b>not a title card</b>, so <b>no belt can have changed hands</b>; the next opportunity is <b>UFC Shanghai on August&nbsp;29</b>, which is <b>also not a title card</b>. The three regressions this desk has previously published and corrected are checked by name every run and remain correct here: <b>light heavyweight is Carlos Ulberg, not Alex Pereira</b>; <b>middleweight is Sean Strickland, not Khamzat Chimaev</b>; <b>featherweight is Alexander Volkanovski, not vacant</b>.</p>
'''
m = sub1(m, cb, cb_new, 'mma-champs')

if fails:
    print("FAILED:", fails); sys.exit(1)

open('cyber-briefing.html','w',encoding='utf-8').write(c)
open('wallstreet-briefing.html','w',encoding='utf-8').write(w)
open('mma-briefing.html','w',encoding='utf-8').write(m)
print("OK cyber=%d ws=%d mma=%d" % (len(c), len(w), len(m)))
