#!/usr/bin/env python3
# Daily Briefings — 6:06 PM ET edition (2026-08-26), incremental edits to the 5:36/5:50 pages.
# Writes are DEFERRED until after the failure check (lesson from the 1736 run).
import re, sys, os

D = os.path.dirname(os.path.abspath(__file__))
fails = []
docs = {}

def load(name):
    docs[name] = open(os.path.join(D, name)).read()

for n in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    load(n)

def sub(name, old, new, label, count=1):
    h = docs[name]
    if old not in h:
        fails.append('MISSING ANCHOR [%s / %s]: %r' % (name, label, old[:110]))
        return
    n_found = h.count(old)
    if count == 1 and n_found != 1:
        fails.append('AMBIGUOUS ANCHOR [%s / %s]: %d occurrences' % (name, label, n_found))
        return
    docs[name] = h.replace(old, new, count)

def insert_after(name, anchor, new, label):
    h = docs[name]
    if h.count(anchor) != 1:
        fails.append('ANCHOR NOT UNIQUE [%s / %s]: %d' % (name, label, h.count(anchor)))
        return
    docs[name] = h.replace(anchor, anchor + new, 1)

def replace_tldr(name, label, body):
    h = docs[name]
    m = re.search(r'<div class="tldr"><b>' + re.escape(label) + r'</b> <span>.*?</span></div>', h, re.S)
    if not m:
        fails.append('TLDR NOT FOUND [%s]' % name)
        return
    docs[name] = h[:m.start()] + '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (label, body) + h[m.end():]

# ============================================================ WALL STREET
W = 'wallstreet-briefing.html'

# -- (0) FIX A REAL PAGE DEFECT: the 5:36 run printed the same caveat sentence twice.
dupe = ('<b>&#9888; That last clause is no longer true as of 5:36 &mdash; Nvidia now has two sourced '
        'after-hours magnitudes; the sentence is kept only as the record of what this page said at 5:06.</b> ')
if docs[W].count(dupe) == 2:
    docs[W] = docs[W].replace(dupe + dupe, dupe, 1)
else:
    fails.append('DEDUPE [%s]: expected 2 copies of the doubled caveat, found %d' % (W, docs[W].count(dupe)))

replace_tldr(W, 'The Tape',
    '<b>Nvidia&rsquo;s after-hours loss reversed live on the earnings call:</b> the stock <b>turned sharply '
    'higher shortly after CFO Colette Kress began speaking and was up almost 5% in extended trading at '
    '~5:10&nbsp;p.m. ET</b>, after she put the <b>backlog above $2&nbsp;trillion</b> and forecast <b>70% revenue '
    'growth for fiscal 2028 on a &ldquo;supply-constrained&rdquo; basis</b> &mdash; the <b>&minus;1% and '
    '&minus;1.3% reads this page carried at 5:36 were true when they were taken</b>, and are kept as the record '
    'of an earlier tape rather than corrected away.')

# -- The lead: new headline + new lede block prepended, old lede preserved beneath.
old_h2 = ('<h2>Nvidia finally has an after-hours number &mdash; and it is HP, not Nvidia, taking the '
          'night&rsquo;s worst punishment</h2>')
new_lead = (
 '<h2>Nvidia&rsquo;s after-hours loss reverses on the call &mdash; up almost 5% as the CFO speaks</h2>\n'
 '<p><b>&#9679; New &middot; 6:06 &mdash; the single biggest development since this page last published is that '
 'Nvidia&rsquo;s extended-hours decline did not hold.</b> Kiplinger&rsquo;s live blog, in an entry stamped '
 '<b>5:10&nbsp;p.m. ET</b>, reports that <b>&ldquo;Nvidia stock turned sharply higher shortly after CFO Colette '
 'Kress started talking&rdquo;</b> and that <b>&ldquo;NVDA stock is now up almost 5% in after-hours '
 'trading.&rdquo;</b> What she said on the way there: <b>&ldquo;another outstanding quarter,&rdquo;</b> with '
 '<b>record revenue, operating income and earnings per share</b>; <b>&ldquo;growth accelerated for the fourth '
 'consecutive quarter&rdquo;</b>; a <b>fiscal-2028 revenue growth forecast of 70%</b>, which she flagged '
 'explicitly as a <b>&ldquo;supply-constrained&rdquo; estimate</b>; a <b>backlog now above $2&nbsp;trillion</b>; '
 '<b>hyperscaler capital spending of more than $800&nbsp;billion this year and $1.3&nbsp;trillion in 2027</b>; and '
 'an <b>expansion of Nvidia&rsquo;s partnership with Amazon&rsquo;s AWS.</b> She also addressed head-on the '
 'criticism of the <b>$500&nbsp;billion third-party financing mechanism</b> Nvidia set up with six large financial '
 'institutions. '
 '<b>&#9888; THE EARLIER READS ARE NOT WRONG AND ARE NOT DELETED.</b> <b>&minus;1.3% about half an hour before the '
 'call</b> (Kiplinger) and <b>&minus;1% at 5:36</b> (Investing.com) were accurate observations of an earlier tape; '
 'by a <b>5:24&nbsp;p.m.</b> entry the same blog notes the share price is already <b>&ldquo;down some from its '
 'after-hours peak,&rdquo;</b> so <b>&ldquo;almost 5%&rdquo; is a peak-adjacent reading, not a settled figure, and '
 'no 6&nbsp;p.m. level is asserted here.</b> Jensen Huang opened the analyst Q&amp;A at <b>5:34</b> with '
 '<b>&ldquo;I don&rsquo;t know if you&rsquo;ve seen, AI has become useful&rdquo;</b>, added that <b>&ldquo;about '
 'half of our business is growing about 100% a year, and that&rsquo;s beyond the cloud,&rdquo;</b> and said '
 '<b>&ldquo;we&rsquo;ve got a huge year coming up next year. It&rsquo;s going to be extraordinary.&rdquo;</b> '
 '(Kiplinger, Nvidia earnings live blog, entries timestamped 20:32Z&ndash;21:34Z.)</p>\n'
 '<p class="note"><b>&#9888; REJECTED THIS RUN &mdash; FOUR CLAIMS ABOUT THE CALL THAT THE FETCHED BLOG DOES NOT '
 'CONTAIN.</b> A search summary attributed to Huang: a forecast of <b>$1&nbsp;trillion in combined Blackwell and '
 'Rubin sales from 2025 through the end of calendar 2027</b>; <b>350 plants building the 1.5&nbsp;million '
 'components in each Blackwell rack</b>; <b>Vera Rubin production shipments in Q3 unlocking a $200&nbsp;billion CPU '
 'market</b>; and the line <b>&ldquo;our demand is much higher than that&rdquo;</b> alongside the 70% fiscal-2028 '
 'figure. <b>None of the four appears anywhere in the live blog fetched this run</b>, and the fourth also '
 '<b>misattributes the 70% forecast, which the fetched blog gives to Kress, not Huang.</b> <b>The 70% number is '
 'published above as hers; the other four items are not published at all.</b> '
 '<b>RULE: a paraphrase of a call is not a transcript of it.</b></p>\n'
 '<p class="note"><b>&#9679; New &middot; 6:06 &mdash; the segment table reconciles exactly, so it publishes.</b> '
 'From the CFO commentary: <b>Data Center $89.02&nbsp;billion, &plus;116.6% y/y and &plus;18.3% q/q</b>, split into '
 '<b>Hyperscale $48.71&nbsp;billion (&plus;101.5% y/y, &plus;13.1% q/q)</b> and <b>ACIE &mdash; AI Clouds, '
 'Industrial and Enterprise &mdash; $40.31&nbsp;billion (&plus;138.1% y/y, &plus;25.2% q/q)</b>, plus <b>Edge '
 'Computing $7.20&nbsp;billion (&plus;27.5% y/y, &plus;13.0% q/q)</b> on strong Blackwell workstation sales '
 '<b>offset by slower consumer PC sales on higher memory and system prices</b> &mdash; the same memory-cost story '
 'that cost HP Inc 11% tonight. <b>Checked in Python: 48.71 &plus; 40.31 = 89.02 exactly, and 89.02 &plus; 7.20 = '
 '96.22, which rounds to the $96.2&nbsp;billion top line.</b> Gross margin <b>75.0% against 72.7%</b> a year ago; '
 'the Q3 guide is <b>74.0% against 73.6%</b>. The <b>$108&nbsp;billion &plusmn;2%</b> Q3 revenue guide is '
 '<b>&plus;89.4% on the $57.01&nbsp;billion</b> Nvidia reported for the year-ago quarter (checked). '
 '(Kiplinger, quoting the Q2&nbsp;FY27 CFO commentary.)</p>\n')
sub(W, old_h2, new_lead + '<p class="note"><b>Carried &middot; 5:36 &mdash; the roundup that preceded the '
    'reversal.</b></p>\n<h2 style="font-size:22px">Nvidia finally has an after-hours number &mdash; and it is HP, '
    'not Nvidia, taking the night&rsquo;s worst punishment</h2>', 'WS lead')

# -- After-hours movers: new card at the top of the deck.
ah_anchor = '<div class="lab">After-hours movers</div>'
ah_card = (
 '\n<div class="cards"><div class="card"><div class="tags"><span class="tag new">New &middot; 6:06</span>'
 '<span class="tag up">NVDA ~&plus;5% at 5:10</span><span class="tag">Reversed on the call</span>'
 '<span class="tag">Peak-adjacent, not settled</span></div>\n'
 '<h3>Nvidia (NVDA) &mdash; the tape changed its mind while the CFO was talking</h3>\n'
 '<p><b>The night&rsquo;s decline reversed during the conference call.</b> Kiplinger&rsquo;s live blog at '
 '<b>5:10&nbsp;p.m. ET</b>: the stock <b>&ldquo;turned sharply higher shortly after CFO Colette Kress started '
 'talking&rdquo;</b> and was <b>&ldquo;up almost 5% in after-hours trading.&rdquo;</b> The triggers, in her own '
 'framing: a <b>backlog above $2&nbsp;trillion</b>, a <b>70% fiscal-2028 revenue growth forecast</b> she called '
 '<b>supply-constrained</b>, <b>hyperscaler capex above $800&nbsp;billion this year and $1.3&nbsp;trillion in '
 '2027</b>, and an <b>expanded AWS partnership.</b> <b>&#9888; Fourteen minutes later the same blog says the price '
 'is &ldquo;down some from its after-hours peak&rdquo;</b> &mdash; so <b>~&plus;5% is a high-water reading, not the '
 'night&rsquo;s number, and this page asserts no level.</b> <b>The &minus;1.3% and &minus;1% reads below remain '
 'exactly as published:</b> they were correct before the call, and an after-hours percentage is a timestamped '
 'observation, not a fact awaiting reconciliation. (Kiplinger.)</p></div></div>\n')
insert_after(W, ah_anchor, ah_card, 'WS after-hours card')

# -- Sources
insert_after(W, '<div class="lab">Sources</div>\n',
 '<p class="note"><b>Added 6:06:</b> <a href="https://www.kiplinger.com/investing/live/nvidia-earnings-live-updates-and-'
 'commentary-august-2026">Kiplinger &mdash; Nvidia earnings live blog, conference-call entries (20:32Z&ndash;'
 '21:34Z, Aug&nbsp;26 2026)</a> &middot; <a href="https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/'
 'Q2FY27-CFO-Commentary.pdf">Nvidia &mdash; Q2 FY2027 CFO commentary (PDF, as quoted by Kiplinger)</a> &middot; '
 '<a href="https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027">'
 'Nvidia &mdash; Q2 FY2027 results release</a></p>\n', 'WS sources')

# ============================================================ CYBER
C = 'cyber-briefing.html'

replace_tldr(C, 'The Wire',
    'The run&rsquo;s new material is <b>a Wall Street breach with Social Security numbers in it</b>: '
    '<b>Apollo Global Management has confirmed that a social-engineering intrusion reached cloud platforms between '
    'July&nbsp;6 and July&nbsp;10 and exposed names, dates of birth, addresses, contact details and SSNs</b>, part '
    'of a wave of help-desk-impersonation attacks on financial firms; <b>SecurityWeek&rsquo;s Gitea write-up shows '
    'CVE-2026-60004 was fixed in 1.27.1 back in late July &mdash; roughly a month before CISA listed it as '
    'exploited</b>; and three fresh flaws land in Vulnerability Watch, including a <b>CVSS 9.1 Keycloak password-'
    'reset account takeover</b> and an <b>NVIDIA NemoClaw model-poisoning weakness with no CVE and no fix on '
    'Windows.</b> <b>Patch Priority is unchanged &mdash; Oracle CVE-2026-21962 is due tomorrow &mdash; and CISA&rsquo;s '
    'KEV catalogue is static for a sixteenth consecutive edition.</b>')

# -- Breaches & incidents: three new cards at the top of the deck.
br_anchor = '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">'
br_cards = (
 '\n<div class="card"><div class="tags"><span class="tag new">New &middot; 6:06</span>'
 '<span class="tag crit">SSNs exposed</span><span class="tag warn">Social engineering</span>'
 '<span class="tag">Private equity</span></div>\n'
 '<h3>Apollo Global Management confirms a social-engineering breach &mdash; and the exposed fields include Social '
 'Security numbers</h3>\n'
 '<p><b>Apollo has confirmed that attackers used social engineering &mdash; manipulating people rather than '
 'exploiting software &mdash; to reach data held in the firm&rsquo;s cloud platforms, with access occurring between '
 '<b>July&nbsp;6 and July&nbsp;10, 2026</b>.</b> An investigation determined on <b>August&nbsp;12</b> that the '
 'potentially affected information includes <b>names, dates of birth, contact information, home addresses and '
 'Social Security numbers.</b> Apollo says the incident was <b>limited to a subset of systems</b>, that <b>no '
 'client funds were compromised</b>, and that it has <b>no evidence the data has been publicly posted or used for '
 'identity theft or fraud</b>; it is offering <b>credit monitoring and identity protection.</b> '
 '<b>&#9888; Apollo has NOT disclosed how many people are affected, and no count is published here.</b> Reporting '
 'places it inside <b>a broader August wave against major U.S. private equity and financial services firms</b>, in '
 'which callers reach employees on <b>personal mobile phones while posing as internal IT help-desk staff</b> &mdash; '
 'the same human-in-the-loop pattern as the ClickFix, RMM-abuse and ReliaQuest items on this page. '
 '<b>No CVE, not in KEV, no federal deadline.</b> (SecurityWeek; Bloomberg; Cybernews.)</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 6:06</span>'
 '<span class="tag warn">Export control</span><span class="tag">Supply chain</span></div>\n'
 '<h3>Taiwan charges nine over illegal AI server exports to China &mdash; including Nvidia and Super Micro staff</h3>\n'
 '<p><b>Taiwanese prosecutors have charged nine people over the illegal export of AI servers to China, and the '
 'group includes employees of Nvidia and Super Micro.</b> The reporting frames AI infrastructure &mdash; and the '
 'advanced semiconductors mostly manufactured in Taiwan &mdash; as <b>a central point of competition between the '
 'United States and China.</b> <b>&#9888; No charge sheet, dollar value, server count or individual name is '
 'asserted here; the coverage fetched this run states none of them.</b> (SecurityWeek, Aug&nbsp;25.)</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 6:06</span>'
 '<span class="tag warn">Phishing-as-a-service</span><span class="tag">Microsoft 365</span>'
 '<span class="tag">2FA bypass</span></div>\n'
 '<h3>Mirage2FA: 4,500 companies, and the toolkit never has to break the login &mdash; it borrows it</h3>\n'
 '<p><b>A commercial phishing-as-a-service toolkit tracked as Mirage2FA has affected roughly 4,500 US and EU '
 'companies between 2024 and 2026</b>, targeting <b>Microsoft&nbsp;365 accounts by abusing legitimate login flows '
 'and bypassing two-factor authentication.</b> Per <b>ANY.RUN</b>, <b>48% of targeted email addresses were '
 'potentially compromised</b>, and <b>the United States accounts for 63.7%</b> of the targets. Stealing '
 '<b>passwords and session cookies</b> hands the attacker an <b>authenticated Microsoft&nbsp;365 session and the '
 'SSO-connected services behind it</b>, which is the whole point &mdash; corporate email and trusted business '
 'accounts become a launch pad for impersonation and fraud. <b>No CVE, not in KEV, no federal deadline.</b> '
 '(The Hacker News, citing ANY.RUN.)</p></div>\n')
insert_after(C, br_anchor, br_cards, 'cyber breach cards')

# -- Vulnerability watch: prepend a 6:06 note above the 5:36 note.
vw_anchor = '<div class="lab">Vulnerability watch</div>\n'
vw_note = (
 '<p class="note"><b>&#9679; New &middot; 6:06 &mdash; three flaws that are not in KEV, do not have federal '
 'deadlines, and are worth patching anyway.</b> <b>CVE-2026-18963, CVSS 9.1</b> (rated by Red Hat as CNA) is a '
 '<b>critical Keycloak password-reset weakness</b> &mdash; classified as <b>weak password recovery for a forgotten '
 'password (CWE-640)</b>, root-caused to <b>improper state validation in the reset-credentials flow</b> &mdash; that '
 'lets an <b>unauthenticated remote attacker take over any account by forcing a password reset.</b> Upstream users '
 'should move to <b>26.7.2, released August&nbsp;19</b>; Red Hat build of Keycloak customers to <b>26.4.15 and '
 '26.6.6.</b> <b>&#9888; No evidence of exploitation and no verified public exploit as of August&nbsp;24.</b> '
 '<b>CVE-2026-75149</b> in the <b>Marimo</b> notebook carries <b>CVSS v4 8.7 and CVSS v3.1 8.8</b> from '
 '<b>VulnCheck</b> as CNA: a crafted notebook can supply an <b>attacker-controlled Model Context Protocol server '
 'command</b> that <b>runs as a local subprocess the moment the notebook is opened in edit mode</b> &mdash; user '
 'interaction required, attacker authentication not. Affects versions <b>before 0.23.15</b>, fixed in '
 '<b>0.23.15</b>, CVE published <b>August&nbsp;19</b>. Third, and with <b>no CVE at all</b>: <b>Oasis Security</b> '
 'has disclosed a weakness in <b>NVIDIA NemoClaw</b> by which an <b>attacker-controlled webpage takes '
 'unauthenticated control of the local Ollama instance serving an AI agent and plants hidden instructions inside '
 'the model itself.</b> <b>&#9888; This is a SEPARATE finding from the four NVIDIA advisories described below</b> '
 '&mdash; it carries <b>no CVE identifier</b>, and Oasis&rsquo;s head of research says <b>NemoClaw v0.0.35 fixed it '
 'on macOS and Linux while there is NO fix on the Windows and WSL path</b>, where v0.0.34 <b>added a Windows '
 'installation carrying a warning instead.</b> No exploitation reported as of August&nbsp;25. '
 '<b>&#9888; Note who is reporting whom: Oasis Security is the firm Cyera is acquiring in a $1&nbsp;billion deal, '
 'and Cyera is the vendor credited below with detailing the agent-hijack flaw in NVIDIA&rsquo;s own advisories.</b> '
 'Separately, <b>Chrome&nbsp;152 patches more than 300 vulnerabilities</b>, <b>most of them found by Google using '
 'AI</b> &mdash; <b>&#9888; no CVE, CVSS or individual flaw from that release is asserted here.</b> '
 '(The Hacker News; SecurityWeek.)</p>\n')
insert_after(C, vw_anchor, vw_note, 'cyber vuln note')

# -- KEV section: static note + the Gitea patch-gap detail.
kev_anchor = '<div class="lab">CISA KEV &amp; federal deadlines</div>\n'
kev_note = (
 '<p class="note"><b>&#9679; 6:06 &mdash; KEV static for a SIXTEENTH consecutive edition.</b> No CISA alert page '
 'later than those already on this board was published this run; the catalogue still ends with the <b>Gitea '
 'CVE-2026-60004 addition of August&nbsp;25</b>. Nearest deadlines are unchanged: <b>Oracle CVE-2026-21962 due '
 'August&nbsp;27 (tomorrow)</b> and <b>Gitea CVE-2026-60004 due August&nbsp;28.</b> <b>&#9679; New detail on the '
 'Gitea row:</b> SecurityWeek reports the flaw was <b>patched by Gitea&rsquo;s developers in late July with the '
 'release of version 1.27.1</b> &mdash; the same fixed version already on this board &mdash; which means <b>a fix '
 'existed for roughly a month before CISA listed the bug as exploited.</b> <b>&#9888; The federal deadline is '
 'unaffected by that; the patch gap is a defender&rsquo;s framing, not a change to the due date.</b> '
 '(SecurityWeek, Aug&nbsp;26.)</p>\n')
insert_after(C, kev_anchor, kev_note, 'cyber kev note')

# -- Stat strip: swap the least-fresh tile for tonight's figure.
sub(C,
 '<div class="stat"><div class="n">145</div><div class="l">Antivirus and EDR processes the <b>Cruciferra</b> '
 'loader can terminate through the vulnerable <b>MocoMsys</b> driver it drops</div></div>',
 '<div class="stat"><div class="n">300&plus;</div><div class="l">Vulnerabilities patched in <b>Chrome&nbsp;152</b>, '
 '<b>most of them discovered by Google using AI</b></div></div>', 'cyber stat swap')

# -- Sources
insert_after(C, '<div class="lab">Sources</div>\n',
 '<p class="note"><b>Added 6:06:</b> <a href="https://www.securityweek.com/personal-information-exposed-in-apollo-'
 'global-data-breach/">SecurityWeek &mdash; Personal information exposed in Apollo Global data breach</a> &middot; '
 '<a href="https://www.securityweek.com/cisa-warns-of-exploited-gitea-vulnerability/">SecurityWeek &mdash; CISA '
 'warns of exploited Gitea vulnerability</a> &middot; <a href="https://www.securityweek.com/chrome-152-patches-'
 'over-300-vulnerabilities/">SecurityWeek &mdash; Chrome 152 patches over 300 vulnerabilities</a> &middot; '
 '<a href="https://www.securityweek.com/taiwan-charges-9-over-illegal-ai-server-exports-to-china-including-nvidia-'
 'and-super-micro-staff/">SecurityWeek &mdash; Taiwan charges 9 over illegal AI server exports to China</a> '
 '&middot; <a href="https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html">The Hacker News '
 '&mdash; Critical Keycloak password reset flaw (CVE-2026-18963)</a> &middot; '
 '<a href="https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html">The Hacker News &mdash; '
 'Marimo notebook MCP flaw (CVE-2026-75149)</a> &middot; <a href="https://thehackernews.com/2026/08/a-malicious-'
 'webpage-could-poison-your.html">The Hacker News &mdash; Malicious webpage could poison your local AI model '
 'behind NVIDIA NemoClaw</a> &middot; <a href="https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-'
 'eu.html">The Hacker News &mdash; Mirage2FA surge hits 4,500 US and EU companies</a></p>\n',
 'cyber sources')

# ============================================================ MMA
M = 'mma-briefing.html'

replace_tldr(M, 'Tale of the Tape',
    'The Sacramento fallout finally lands with <b>exact numbers</b>: <b>Gregory Rodrigues climbs three places to '
    '#7 at middleweight</b> after upsetting <b>Anthony Hernandez</b>, who drops two to <b>#9</b> and is now on a '
    'two-fight skid; <b>Vitor Petrino rises three to #8 at heavyweight</b> as <b>Serghei Spivac</b> falls four to '
    '<b>#13</b>; and three fighters enter a top&nbsp;15 for the first time &mdash; <b>Reinier de Ridder at light '
    'heavyweight in his first fight in the division</b>, <b>Jamall Emmers at #14 featherweight</b> and <b>Carli '
    'Judice at #15 women&rsquo;s flyweight</b>. Three days out from <b>UFC Shanghai</b>, the <b>champions board is '
    'unchanged for a thirty-second consecutive edition.</b>')

# -- Rankings & business: prepend the sourced numbers the page previously withheld.
rk_anchor = '<div class="lab">Rankings &amp; business</div>\n<div class="panel">\n'
rk_new = (
 '<p><span class="tag new">New &middot; 6:06</span> <b>THE THREE RANKINGS THIS PAGE DELIBERATELY LEFT BLANK NOW '
 'HAVE NUMBERS.</b> Every edition since 12:50 has carried the de&nbsp;Ridder, Petrino and Judice entries '
 '<b>without a rank</b>, on the grounds that no fetched source stated one. <b>Sports Illustrated&rsquo;s '
 'rankings-update piece, published 10:05&nbsp;a.m. ET today and fetched in full this run, states all of them.</b> '
 '<b>Vitor Petrino moved up three spots to #8 at heavyweight</b> after a unanimous decision over <b>Serghei '
 'Spivac, who dropped four places to #13.</b> <b>Reinier de Ridder &mdash; previously ranked at middleweight, and '
 'fighting at light heavyweight for the first time &mdash; broke into the light heavyweight rankings after a '
 'first-round TKO of Roman Dolidze</b>, who was also moving up and <b>looked to be at a clear size '
 'disadvantage.</b> <b>Carli Judice rounds out the women&rsquo;s flyweight rankings at #15</b> after stopping the '
 '<b>formerly undefeated Jeisla Chaves</b>, her <b>fourth win in a row.</b> And a fourth name this page had never '
 'listed: <b>Jamall Emmers debuts at #14 at featherweight</b> after knocking out <b>Lerryan Douglas &mdash; who '
 'entered on a six-fight knockout streak &mdash; in the opening round</b>, giving Emmers <b>three straight wins for '
 'the first time since joining the UFC.</b> '
 '<b>&#9888; ONE FIGURE IS IN DISPUTE AND IS THEREFORE NOT ASSERTED: de&nbsp;Ridder&rsquo;s exact rank.</b> The SI '
 'article body says he <b>&ldquo;broke into the UFC light heavyweight rankings at #9&rdquo;</b>; a Sherdog headline '
 'and an MMA&nbsp;Mania headline both frame the same debut as <b>#10 / &ldquo;Top 10&rdquo;</b>. <b>Both readings '
 'are printed; neither is adopted, and this page says only that he entered the light heavyweight top ten.</b> '
 '<b>&#9888; These are the Meta UFC rankings, as the outlet labels them.</b> (Sports Illustrated / MMA Knockout, '
 'Aug&nbsp;26.)</p>\n'
 '<p class="note"><span class="tag new">New &middot; 6:06</span> <b>Two more details from the same piece.</b> '
 '<b>Rodrigues and Hernandez both took Fight of the Night bonuses</b>, and <b>10 of the 13 scheduled fights in '
 'Sacramento ended inside the distance.</b> <b>&#9888; No bonus dollar figure is stated in the article and none is '
 'published here.</b> The piece also independently describes <b>Sean Strickland as the reigning UFC middleweight '
 'champion</b> &mdash; a fresh, same-day cross-check of the belt this desk has had to correct before.</p>\n')
insert_after(M, rk_anchor, rk_new, 'mma rankings')

# -- Around the sport: the rival card on the same night.
ats_anchor = '<div class="lab">Around the sport</div>\n'
ats_new = (
 '<p class="note"><span class="tag new">New &middot; 6:06</span> <b>Saturday is not a UFC monopoly.</b> '
 '<b>Duel Arena 1: Perry vs. Danis</b> runs the same night as UFC Shanghai &mdash; <b>Saturday, August&nbsp;29, at '
 'the Kia Center in Orlando, Florida, 8&nbsp;p.m. ET</b>, with <b>Mike Perry meeting Dillon Danis in an MMA bout at '
 '170&nbsp;pounds.</b> <b>&#9888; This is not a UFC event</b>, and the <b>8&nbsp;p.m. ET</b> start puts it '
 'fourteen hours after Shanghai&rsquo;s <b>6&nbsp;a.m. ET</b> main card rather than against it. <b>No odds, purse '
 'or broadcast figure is stated in the coverage fetched this run, so none is published.</b> '
 '(MMA&nbsp;Mania; Tapology.)</p>\n')
insert_after(M, ats_anchor, ats_new, 'mma around the sport')

# -- Sources
insert_after(M, '<div class="lab">Sources</div>\n',
 '<p class="note"><b>Added 6:06:</b> <a href="https://www.si.com/fannation/mma/news/ufc-rankings-update-several-'
 'new-fighters-debut-ufc-sacramento-wins">Sports Illustrated / MMA Knockout &mdash; UFC rankings update after UFC '
 'Sacramento (Aug&nbsp;26)</a> &middot; <a href="https://www.sherdog.com/news/rankings/4/UFC-Sacramento-shakes-up-'
 'rankings-as-Rodrigues-De-Ridder-surge-202500">Sherdog &mdash; UFC Sacramento shakes up rankings</a> &middot; '
 '<a href="https://www.mmamania.com/ufc-mma-rankings/467315/top-10-reinier-de-ridder-crashes-light-heavyweight-'
 'rankings-ufc-sacramento">MMA Mania &mdash; de Ridder crashes the light heavyweight rankings</a> &middot; '
 '<a href="https://www.mmamania.com/latest-news/467243/duel-arena-1-perry-vs-danis-fight-card-start-time-date-and-'
 'location">MMA Mania &mdash; Duel Arena 1: Perry vs. Danis card, start time, date and location</a></p>\n',
 'mma sources')

# ============================================================ INDEX
I = 'index.html'
sub(I, '<h2>Nvidia gets a number, HP takes the beating</h2>',
       '<h2>Nvidia&rsquo;s after-hours loss reverses on the call</h2>', 'index markets h2')
sub(I, '<h2>Two vendors empty their advisory queues, and WordPress takes the live hit</h2>',
       '<h2>Apollo Global confirms a breach with Social Security numbers in it</h2>', 'index cyber h2')
sub(I, '<h2>UFC.com fills in the rest of the Shanghai card</h2>',
       '<h2>The Sacramento rankings fallout gets its numbers</h2>', 'index mma h2')

open(os.path.join(D, '_index_probe.txt'), 'w').write('')

if fails:
    print('FAILED — NOTHING WRITTEN')
    for f in fails:
        print('  ' + f)
    sys.exit(1)

for n, h in docs.items():
    open(os.path.join(D, n), 'w').write(h)
print('OK — wrote %d files' % len(docs))
