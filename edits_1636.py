#!/usr/bin/env python3
# Incremental edits: 4:36 PM ET Afternoon Edition, Aug 26 2026 (17th run of the day).
# The 4:14 pages said no verified after-hours move existed. Nvidia, CrowdStrike and
# Salesforce have all now reported. This run replaces the after-hours placeholder with
# the real, sourced prints and re-leads the Wall Street page on them.
import io, re, sys, os

D = os.path.dirname(os.path.abspath(__file__))
fails = []

def load(p):
    with io.open(os.path.join(D, p), encoding='utf-8') as f:
        return f.read()

def save(p, s):
    with io.open(os.path.join(D, p), 'w', encoding='utf-8') as f:
        f.write(s)

def sub_once(s, old, new, label):
    if s.count(old) != 1:
        fails.append('ANCHOR %s: found %d occurrences' % (label, s.count(old)))
        return s
    return s.replace(old, new, 1)

def demote_new(s):
    """Previous edition's 'New' tags stop being new this run."""
    return s.replace('<span class="tag new">New &middot; 4:15</span>',
                     '<span class="tag">4:15</span>')

# ---------------------------------------------------------------- WALL STREET
ws = load('wallstreet-briefing.html')
ws = demote_new(ws)

OLD_TLDR = ws[ws.index('<div class="tldr"><b>The Tape</b>'):]
OLD_TLDR = OLD_TLDR[:OLD_TLDR.index('</div>') + 6]
NEW_TLDR = (
 '<div class="tldr"><b>The Tape</b> <span>The regular session ended flat &mdash; '
 '<b>the S&amp;P&nbsp;500 closed at 7,675.70, down 1.58 points, &minus;0.02%</b> &mdash; and then the '
 'after-hours tape delivered the day: <b>Nvidia beat with revenue of $96.22&nbsp;billion against '
 '$92.17&nbsp;billion expected</b>, more than double a year ago, <b>guided the current quarter to '
 '$108&nbsp;billion</b> against $104.2&nbsp;billion expected &mdash; <b>and the stock slipped anyway</b>, '
 'while <b>Salesforce soared 14% in extended trading</b> and <b>CrowdStrike posted the best quarter in its '
 'history</b>.</span></div>')
ws = sub_once(ws, OLD_TLDR, NEW_TLDR, 'ws-tldr')

ws = sub_once(ws,
 '<h2>A $17&nbsp;billion settlement, a later board that reconciles &mdash; and Nvidia after the bell</h2>',
 '<h2>Nvidia beats, guides above the street &mdash; and the stock goes down anyway</h2>\n'
 '<p><b>&#9679; New &middot; 4:36 &mdash; the print the whole tape was waiting on, and it is a result now, not an expectation.</b> '
 '<b>Nvidia</b> reported the second quarter of fiscal&nbsp;2027 after Wednesday&rsquo;s close and beat on both lines: '
 '<b>revenue of $96.22&nbsp;billion against $92.17&nbsp;billion expected</b>, and <b>adjusted earnings of $2.22 a share '
 'against $2.10 expected</b> (CNBC). Revenue <b>climbed 106% from a year earlier</b> &mdash; against the '
 '<b>$46.74&nbsp;billion</b> of the year-ago quarter that is <b>2.06&times;</b>, checked in Python, so the '
 '&ldquo;more than doubled&rdquo; framing is literally true. <b>Data Center revenue was $89&nbsp;billion against '
 '$86.33&nbsp;billion expected, up 117% year over year</b>, and now accounts for <b>92% of company sales</b> '
 '(89&nbsp;&divide;&nbsp;96.22 = <b>92.5%</b>, consistent). The guide is the bigger number: the company '
 '<b>sees $108&nbsp;billion in the current quarter, plus or minus 2%</b>, where <b>analysts wanted $104.2&nbsp;billion</b> '
 '&mdash; the <b>entire &plusmn;2% band, $105.84&nbsp;billion to $110.16&nbsp;billion, sits above the consensus</b>, '
 'and the midpoint is <b>12.2% sequential growth</b>. <b>&#9888; The outlook includes no data-center sales from China.</b> '
 '<b>&#9888; Note what the printed quarter did to this desk&rsquo;s own carried expectations:</b> $96.22&nbsp;billion is '
 '<b>above the top of the company&rsquo;s own $91.0&nbsp;billion &plusmn;2% guide ($89.18&ndash;$92.82&nbsp;billion)</b>, so '
 'every consensus figure this page carried all day &mdash; Visible Alpha&rsquo;s $92.16&nbsp;billion, the 41-analyst '
 '$92.07&nbsp;billion &mdash; was <b>too low by roughly $4&nbsp;billion</b>. <b>And the stock slipped in extended trading '
 'regardless</b> &mdash; a beat, a raise, and a lower price. <b>&#9888; No verified after-hours percentage for NVDA appeared '
 'in any source fetched this run; the direction is published, the magnitude is not.</b></p>\n'
 '<p><b>&#9679; New &middot; 4:36 &mdash; Salesforce is the actual after-hours move, and it has a number.</b> '
 '<b>Salesforce shares soared 14% in extended trading</b> after revenue of <b>$11.35&nbsp;billion against '
 '$11.32&nbsp;billion expected</b>, <b>up 11%</b> in the quarter ended July&nbsp;31 (CNBC). The company guided the full '
 'year to <b>$16.67&ndash;$16.71 in earnings per share on $46.1&ndash;$46.4&nbsp;billion of revenue</b>, which the source '
 'puts at <b>11% growth at the midpoint</b> ($46.25&nbsp;billion). Two items underneath the headline: a '
 '<b>$2.6&nbsp;billion gain on strategic investments from its stake in the AI startup Anthropic</b>, and '
 '<b>annualized revenue from Agentforce AI products above $1.5&nbsp;billion, up 240% year over year</b>. '
 '<b>&#9888; ONE FIGURE IS PRINTED AND FLAGGED, NOT SMOOTHED:</b> CNBC gives <b>net income of $3.53&nbsp;billion, or '
 '$4.29 a share, &ldquo;jumped 87%&rdquo; from $1.89&nbsp;billion, or $1.96 a share.</b> The net-income growth is '
 '<b>86.8%</b> and reconciles &mdash; but <b>per share the same pair is &plus;118.9%</b>, which would require the diluted '
 'share count to fall from <b>~964&nbsp;million to ~823&nbsp;million, down 14.7% in a year</b>. Both figures are quoted as '
 'the source states them; <b>no reconciled EPS growth rate is asserted.</b></p>\n'
 '<p><b>&#9679; New &middot; 4:36 &mdash; CrowdStrike, straight from the 8-K, and it is a records quarter.</b> '
 'The company&rsquo;s own earnings release filed with the SEC &mdash; fetched in full this run, not summarised &mdash; '
 'reports <b>total revenue of $1.47&nbsp;billion, up 26%</b> from $1.17&nbsp;billion (the statements give '
 '<b>$1,470,897&nbsp;thousand vs $1,168,952&nbsp;thousand</b>, which is <b>&plus;25.8%</b>), <b>non-GAAP earnings of '
 '$0.31 a share against $0.29 expected</b>, and <b>record net new ARR of $333&nbsp;million, accelerating to 51% '
 'year-over-year growth</b> &mdash; against guidance of <b>$284&ndash;$286&nbsp;million</b>, a beat of roughly '
 '<b>$47&nbsp;million</b>. Ending <b>ARR is $5.84&nbsp;billion, up 25%</b>; <b>Falcon Flex ending ARR passed '
 '$2.29&nbsp;billion, up 101%</b>; <b>Q2-record operating cash flow of $530&nbsp;million and free cash flow of '
 '$377&nbsp;million</b>. The company <b>raised its full-year fiscal&nbsp;2027 net new ARR growth outlook by 630 basis '
 'points to 34% at the midpoint</b>. Founder and CEO <b>George Kurtz</b>: <b>&ldquo;Q2 was the best quarter in '
 'CrowdStrike&rsquo;s history.&rdquo;</b> <b>&#9888; A SEARCH SUMMARY THIS RUN HANDED BACK THE WRONG QUARTER</b> &mdash; '
 '&ldquo;record $256&nbsp;million in net new ARR, up 32%&rdquo;, &ldquo;ending ARR $5.51&nbsp;billion&rdquo;, '
 '&ldquo;revenue $1.39&nbsp;billion&rdquo; &mdash; <b>those are the prior quarter&rsquo;s numbers, and they are rejected;</b> '
 'the 8-K governs. <b>&#9888; No verified after-hours percentage for CRWD exists in any source fetched this run.</b></p>',
 'ws-h2')

# --- After-hours section: replace the 4:15 "nothing verified yet" placeholder body
AH_START = ws.index('<div class="lab">After-hours movers</div>')
AH_END = ws.index('</section>', AH_START)
NEW_AH = (
 '<div class="lab">After-hours movers</div>\n'
 '<p class="note"><b>&#9679; Updated 4:36 &mdash; the after-hours tape now exists, and it does not agree with the '
 'earnings.</b> At <b>4:15&nbsp;p.m. ET this page said, correctly, that no verified after-hours price move existed in any '
 'source.</b> Twenty minutes later three of the six names that reported have results, and <b>only one of them has a '
 'sourced price move.</b> Everything below is either a reported figure or an explicitly attributed direction; '
 '<b>no percentage is published for a stock unless a source stated it.</b></p>\n'
 '<div class="cards">\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:36</span><span class="tag up">+14%</span>'
 '<span class="tag">Sourced move</span></div>\n'
 '<h3>Salesforce (CRM) &mdash; the only after-hours number anyone has put a figure on</h3>\n'
 '<p><b>Shares soared 14% in extended trading</b> on revenue of <b>$11.35&nbsp;billion vs $11.32&nbsp;billion expected, '
 '&plus;11%</b>, and full-year guidance of <b>$16.67&ndash;$16.71 EPS on $46.1&ndash;$46.4&nbsp;billion</b>. '
 '<b>Agentforce annualized revenue tops $1.5&nbsp;billion, &plus;240% y/y</b>; a <b>$2.6&nbsp;billion gain on strategic '
 'investments</b> came from its <b>Anthropic</b> stake. <b>&#9888; The $4.29 per-share figure does not grow at the same '
 '87% the net-income line does &mdash; see The Lead; both printed, neither reconciled.</b></p>\n'
 '<h3>Nvidia (NVDA) &mdash; a beat, a raise above the street, and a lower price</h3>\n'
 '<p><b>$96.22&nbsp;billion revenue vs $92.17&nbsp;billion expected</b>; <b>$2.22 adjusted EPS vs $2.10</b>; '
 '<b>Data Center $89&nbsp;billion vs $86.33&nbsp;billion, &plus;117%</b>; <b>Q3 guide $108&nbsp;billion &plusmn;2% vs '
 '$104.2&nbsp;billion expected</b>, with <b>no China data-center revenue assumed</b>. <b>The stock slipped in extended '
 'trading.</b> <b>&#9888; DIRECTION ONLY &mdash; no source fetched this run states the size of the move, so none is '
 'printed.</b> For scale, the options market had priced <b>~$282&nbsp;billion</b> of value in play on a '
 '<b>13.26%</b> implied swing.</p>\n'
 '<h3>CrowdStrike (CRWD) &mdash; records on every line the company reports</h3>\n'
 '<p><b>Revenue $1.47&nbsp;billion &plus;26%</b>; <b>non-GAAP EPS $0.31 vs $0.29 expected</b>; <b>record net new ARR '
 '$333&nbsp;million, &plus;51% y/y</b> against a <b>$284&ndash;$286&nbsp;million</b> guide; <b>ARR $5.84&nbsp;billion '
 '&plus;25%</b>; <b>FY27 net new ARR growth outlook raised 630bp to 34%</b>. GAAP net income was <b>$5.3&nbsp;million, '
 '$0.01 a share</b> &mdash; positive, and far below the non-GAAP line, as the release&rsquo;s own reconciliation shows. '
 '<b>&#9888; No after-hours price move sourced.</b> The call is at <b>5:00&nbsp;p.m. ET</b>.</p>\n'
 '<h3>Still to be seen: Okta, Williams-Sonoma, Abercrombie &amp; Fitch</h3>\n'
 '<p><b>OKTA</b>, <b>WSM</b> and <b>ANF</b> were also on tonight&rsquo;s list per Yahoo Finance and TheStreet. '
 '<b>&#9888; No results and no after-hours prices for any of the three appeared in any source fetched this run &mdash; '
 'nothing is asserted about them.</b> Abercrombie was the <b>regular session&rsquo;s biggest mover</b> and remains the '
 'Chart of the Day on that basis.</p>\n'
 '</div>\n')
ws = ws[:AH_START] + NEW_AH + ws[AH_END:]

# Sources
ws = sub_once(ws, '<div class="lab">Sources</div>',
 '<div class="lab">Sources</div>\n'
 '<p class="note"><b>Added 4:36:</b> '
 '<a href="https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html">CNBC &mdash; Nvidia Q2 FY2027 results</a> &middot; '
 '<a href="https://www.cnbc.com/2026/08/26/salesforce-crm-q2-earnings-report-2027.html">CNBC &mdash; Salesforce Q2 FY2027 results</a> &middot; '
 '<a href="https://www.sec.gov/Archives/edgar/data/0001535527/000153552726000029/crwd-20260826xex991.htm">SEC &mdash; CrowdStrike Q2 FY2027 earnings release (Form 8-K Ex. 99.1)</a></p>',
 'ws-sources')
save('wallstreet-briefing.html', ws)

# --------------------------------------------------------------------- CYBER
cy = load('cyber-briefing.html')
cy = demote_new(cy)

# by-the-numbers: swap in the CrowdStrike record ARR figure is business, not threat --
# instead add the Gitea detail + the new RMM campaign as an incident card.
INC = cy.index('<div class="lab">Breaches &amp; incidents</div>')
CARDS = cy.index('<div class="cards">', INC) + len('<div class="cards">')
NEW_CARD = (
 '\n<div class="card"><div class="tags"><span class="tag new">New &middot; 4:36</span>'
 '<span class="tag warn">Phishing</span><span class="tag">RMM abuse</span></div>\n'
 '<h3>A phishing operation is installing legitimate remote-control software in 46 countries</h3>\n'
 '<p>Attackers are abusing <b>legitimate remote monitoring and management (RMM) tools</b> to take direct control of '
 'victim machines, in a campaign reported across <b>46 countries</b> and <b>active since January&nbsp;2026</b>. The '
 'lures are deliberately mundane &mdash; <b>Social Security Administration notices, Adobe PDF prompts, invoices, VAT '
 'alerts, shipping messages and shared-file themes</b>. A related strand aimed <b>primarily at financial institutions</b> '
 'uses <b>fake Adobe Document Cloud pages</b> to talk victims into installing <b>ScreenConnect</b>. '
 '<b>&#9888; Why it is hard to catch:</b> the tool being installed is signed, commercial and often already whitelisted, '
 'so the technique sits in the same family as the <b>ClickFix</b> and <b>Cruciferra</b> activity already in the Spotlight '
 'below &mdash; <b>the user performs the install, and no malicious binary is ever downloaded.</b> '
 '<b>&#9888; No CVE, not in KEV, no federal deadline.</b></p>\n'
 '</div>')
cy = cy[:CARDS] + NEW_CARD + cy[CARDS:]

# Enrich the Gitea KEV entry with the detail confirmed this run.
if 'CVE-2026-60004' in cy:
    KEV = cy.index('<div class="lab">CISA KEV')
    seg = cy[KEV:]
    li = seg.index('CVE-2026-60004')
    li_end = seg.index('</li>', li)
    add = ('  <b>&#9679; Updated 4:36:</b> confirmed this run &mdash; <b>CVSS 9.8</b>; an attacker with '
           '<b>ordinary repository write access</b> can plant an <b>executable Git hook</b> and run arbitrary shell '
           'commands as the <b>Gitea service account</b>. Affects <b>1.17 onward</b>, <b>fixed in 1.27.1</b>. The '
           'in-the-wild report traces to an incident write-up on the Russian blog <b>Habr</b> describing a self-hosted '
           'Gitea instance compromised to run <b>crypto-mining software</b>. CISA added it on <b>Aug&nbsp;25</b> and '
           'federal civilian agencies are instructed to remediate by <b>August&nbsp;28, 2026</b> &mdash; the same '
           'deadline the Patch Priority box carries.')
    cy = cy[:KEV] + seg[:li_end] + add + seg[li_end:]
else:
    fails.append('ANCHOR cy-gitea: CVE-2026-60004 not found')

cy = sub_once(cy, '<div class="lab">Sources</div>',
 '<div class="lab">Sources</div>\n'
 '<p class="note"><b>Added 4:36:</b> '
 '<a href="https://www.securityweek.com/cisa-warns-of-exploited-gitea-vulnerability/">SecurityWeek &mdash; CISA warns of exploited Gitea vulnerability</a> &middot; '
 '<a href="https://www.helpnetsecurity.com/2026/08/26/gitea-cve-2026-60004-exploited-in-the-wild/">Help Net Security &mdash; CVE-2026-60004 exploited in the wild</a> &middot; '
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/25/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; Adds one KEV, Aug 25 2026</a> &middot; '
 '<a href="https://cybersecuritynews.com/hackers-abuse-legitimate-rmm-tools-3/">Cybersecurity News &mdash; RMM abuse, 46-country phishing campaign</a> &middot; '
 '<a href="https://www.sec.gov/Archives/edgar/data/0001535527/000153552726000029/crwd-20260826xex991.htm">SEC &mdash; CrowdStrike Q2 FY2027 earnings release</a></p>',
 'cy-sources')
save('cyber-briefing.html', cy)

# ----------------------------------------------------------------------- MMA
mm = load('mma-briefing.html')
mm = demote_new(mm)
FW = mm.index('<div class="lab">Fight week')
CARDS = mm.index('<div class="cards">', FW) + len('<div class="cards">')
NEW_MMA = (
 '\n<div class="card"><div class="tags"><span class="tag new">New &middot; 4:36</span>'
 '<span class="tag">UFC Shanghai</span><span class="tag">Aug 29</span></div>\n'
 '<div class="dateline">Sat, Aug 29 &middot; Oriental Sports Center, Shanghai</div>\n'
 '<h3>The Shanghai card has its full shape: 13 bouts, and a start time that is not prime time</h3>\n'
 '<p>UFC.com and the event listing confirm <b>UFC Fight Night: Nurmagomedov vs. Song</b>, live from the '
 '<b>Oriental Sports Center in Shanghai on August&nbsp;29, 2026</b>. <b>Umar Nurmagomedov</b> and <b>Song Yadong</b> '
 '&ldquo;close out the festivities in a matchup that carries massive divisional significance in the 135-pound weight '
 'class,&rdquo; each looking to end up <b>the clubhouse leader in the chase for the next title opportunity</b>. The main '
 'event is <b>backed by a 12-fight undercard, for 13 bouts in total</b>. In the co-main, UFC.com describes '
 '<b>&ldquo;former title challenger and home country fighter Yan Xiaonan&rdquo;</b> looking to return to the win column '
 '&mdash; <b>the descriptor is the promotion&rsquo;s own</b>. <b>&#9888; Because the card is in China, the U.S. times are '
 'early morning, not evening: prelims 3&nbsp;a.m. ET, main card 6&nbsp;a.m. ET, on Paramount+.</b> Odds unchanged from the '
 'consensus already carried: <b>Nurmagomedov &minus;500 / Song &plus;380</b>. '
 '<b>&#9888; The card has not taken place; no result is asserted for any bout.</b></p>\n'
 '</div>')
mm = mm[:CARDS] + NEW_MMA + mm[CARDS:]
mm = sub_once(mm, '<div class="lab">Sources</div>',
 '<div class="lab">Sources</div>\n'
 '<p class="note"><b>Added 4:36:</b> '
 '<a href="https://www.ufc.com/event/ufc-fight-night-august-29-2026">UFC.com &mdash; UFC Fight Night: Nurmagomedov vs Song (Shanghai)</a> &middot; '
 '<a href="https://www.ufc.com/news/fight-fight-preview-ufc-shanghai-umar-nurmagomedov-vs-song-yadong">UFC.com &mdash; Fight-by-fight preview, UFC Shanghai</a></p>',
 'mma-sources')
save('mma-briefing.html', mm)

# --------------------------------------------------------------------- INDEX
ix = load('index.html')

def swap_card(s, cls, new_text):
    global fails
    i = s.find('class="bcard %s"' % cls)
    if i < 0:
        fails.append('ANCHOR index %s' % cls)
        return s
    p0 = s.index('<p', i)
    p1 = s.index('</p>', p0)
    return s[:p0] + '<p>' + new_text + s[p1:]

ix = swap_card(ix, 'c-mkt',
 'Nvidia beat with <b>$96.22&nbsp;billion of revenue against $92.17&nbsp;billion expected</b> and guided the current '
 'quarter <b>above the street to $108&nbsp;billion</b> &mdash; and the stock slipped anyway, while '
 '<b>Salesforce soared 14%</b> after the bell.')
ix = swap_card(ix, 'c-sec',
 'CISA&rsquo;s newest KEV entry, the <b>Gitea flaw CVE-2026-60004 (CVSS 9.8)</b>, is being used to plant Git hooks and '
 'mine crypto, with a <b>federal deadline of August&nbsp;28</b>; a separate phishing operation is installing '
 '<b>legitimate remote-control software across 46 countries</b>.')
ix = swap_card(ix, 'c-mma',
 'UFC Shanghai is set for <b>Saturday at the Oriental Sports Center</b> &mdash; <b>13 bouts</b> topped by '
 '<b>Umar Nurmagomedov vs. Song Yadong</b> at bantamweight, with the winner the clubhouse leader for the next title '
 'shot, and U.S. viewers watching from <b>3&nbsp;a.m. ET</b>.')
save('index.html', ix)

print('EDIT FAILURES:', fails if fails else 'none')
sys.exit(1 if fails else 0)
