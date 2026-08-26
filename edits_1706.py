import re,sys
p='wallstreet-briefing.html'
h=open(p).read()
def rep(old,new,label):
    global h
    assert h.count(old)==1, (label, h.count(old))
    h=h.replace(old,new)

# 1. TLDR
rep('<div class="tldr"><b>The Tape</b> <span>The regular session ended flat &mdash; <b>the S&amp;P&nbsp;500 closed at 7,675.70, down 1.58 points, &minus;0.02%</b> &mdash; and then the after-hours tape delivered the day: <b>Nvidia beat with revenue of $96.22&nbsp;billion against $92.17&nbsp;billion expected</b>, more than double a year ago, <b>guided the current quarter to $108&nbsp;billion</b> against $104.2&nbsp;billion expected &mdash; <b>and the stock slipped anyway</b>, while <b>Salesforce soared 14% in extended trading</b> and <b>CrowdStrike posted the best quarter in its history</b>.</span></div>',
 '<div class="tldr"><b>The Tape</b> <span>The regular session ended flat &mdash; <b>the S&amp;P&nbsp;500 closed at 7,675.70, down 1.58 points, &minus;0.02%</b> &mdash; and the after-hours tape has now sorted the night into one loser and three winners: <b>Nvidia beat with $96.22&nbsp;billion of revenue against $92.17&nbsp;billion expected</b> and guided the current quarter above the street, <b>and the stock slipped anyway</b>, while <b>Okta jumped about 15%</b>, <b>Salesforce soared 14%</b> and <b>CrowdStrike rose as much as 12%</b> in extended trading.</span></div>',
 'tldr')

# 2. Lead: new top paragraph
anchor='<div class="lead">\n<p><b>&#9679; Carried from the 4:15 edition &mdash; the close, and the prior-close arithmetic'
newp=('<div class="lead">\n<h2>Software takes the night that Nvidia was supposed to own</h2>\n'
 '<p><b>&#9679; New &middot; 5:06 &mdash; every name that mattered tonight now has a price, and the biggest one is the only red.</b> '
 '<b>Okta</b> is up <b>about 15% in extended trading</b> on <b>$1.05 adjusted EPS against 97 cents expected</b> and <b>revenue of $805&nbsp;million against $795&nbsp;million</b>; '
 '<b>Salesforce soared 14%</b>; <b>CrowdStrike jumped as much as 12%</b> after what its chief executive called the best quarter in the company&rsquo;s history. '
 '<b>Nvidia, which beat on both lines and guided the current quarter entirely above consensus, slipped.</b> '
 'The broader frame from <b>FactSet</b>, cited by <b>Bank of America</b> strategists: <b>second-quarter S&amp;P&nbsp;500 earnings are on pace to rise 50% year over year, the highest growth rate since 2021</b>, with AI the engine.</p>\n'
 '<p><b>&#9888; TWO NVIDIA AFTER-HOURS PERCENTAGES WERE OFFERED THIS RUN AND NEITHER IS PUBLISHED.</b> '
 'One summary returned <b>&ldquo;down 1.59% in extended trading&rdquo;</b> &mdash; but <b>&minus;1.59% is NVDA&rsquo;s regular-session close</b>, already printed below in this same Lead, so the figure is the day&rsquo;s close relabelled as the night&rsquo;s move. '
 'A second returned <b>&ldquo;$213.70, &plus;1.45% from a $210.65 close&rdquo;</b> and stamped it <b>&ldquo;as of 8:00&nbsp;PM ET&rdquo;</b> &mdash; a time that had not happened when this edition was built, and a <i>direction opposite</i> to what CNBC and Yahoo Finance both report. '
 '<b>Direction only for Nvidia; no magnitude.</b></p>\n'
 '<p><b>&#9679; Carried from the 4:15 edition &mdash; the close, and the prior-close arithmetic')
rep(anchor,newp,'lead')

# 3. After-hours intro note
rep('<p class="note"><b>&#9679; Updated 4:36 &mdash; the after-hours tape now exists, and it does not agree with the earnings.</b> At <b>4:15&nbsp;p.m. ET this page said, correctly, that no verified after-hours price move existed in any source.</b> Twenty minutes later three of the six names that reported have results, and <b>only one of them has a sourced price move.</b> Everything below is either a reported figure or an explicitly attributed direction; <b>no percentage is published for a stock unless a source stated it.</b></p>',
 '<p class="note"><b>&#9679; Updated 5:06 &mdash; the after-hours tape is now nearly complete, and it disagrees with the earnings in exactly one place.</b> At <b>4:15&nbsp;p.m. ET this page said, correctly, that no verified after-hours price move existed in any source</b>; at <b>4:36</b> exactly one did. <b>Fifty minutes later four of the six names have reported and three carry sourced price moves</b> &mdash; and the one that does not is the largest company on the list. Everything below is either a reported figure or an explicitly attributed direction; <b>no percentage is published for a stock unless a source stated it.</b></p>',
 'ah-intro')

# 4. demote CRM new tag
rep('<div class="tags"><span class="tag new">New &middot; 4:36</span><span class="tag up">+14%</span><span class="tag">Sourced move</span></div>',
 '<div class="tags"><span class="tag">4:36</span><span class="tag up">+14%</span><span class="tag">Sourced move</span></div>',
 'crm-tag')
rep('<h3>Salesforce (CRM) &mdash; the only after-hours number anyone has put a figure on</h3>',
 '<h3>Okta (OKTA) &mdash; the night&rsquo;s biggest gainer <span class="tag new">New &middot; 5:06</span></h3>\n'
 '<p><b>Shares gained about 15% in extended trading.</b> <b>Adjusted EPS $1.05 vs 97 cents expected</b>; <b>revenue $805&nbsp;million vs $795&nbsp;million expected</b>, <b>&plus;11% from $728&nbsp;million</b> a year ago; <b>net income $116&nbsp;million, or 65 cents a share, against $67&nbsp;million, or 37 cents</b>. Chief executive <b>Todd McKinnon</b> says the agentic-AI security opportunity is still <b>&ldquo;very early.&rdquo;</b> (CNBC.)</p>\n'
 '<h3>Salesforce (CRM) &mdash; the first after-hours number anyone put a figure on</h3>',
 'okta-card')

# 5. NVDA paragraph
rep('<p><b>$96.22&nbsp;billion revenue vs $92.17&nbsp;billion expected</b>; <b>$2.22 adjusted EPS vs $2.10</b>; <b>Data Center $89&nbsp;billion vs $86.33&nbsp;billion, &plus;117%</b>; <b>Q3 guide $108&nbsp;billion &plusmn;2% vs $104.2&nbsp;billion expected</b>, with <b>no China data-center revenue assumed</b>. <b>The stock slipped in extended trading.</b> <b>&#9888; DIRECTION ONLY &mdash; no source fetched this run states the size of the move, so none is printed.</b> For scale, the options market had priced <b>~$282&nbsp;billion</b> of value in play on a <b>13.26%</b> implied swing.</p>',
 '<p><b>$96.22&nbsp;billion revenue vs $92.17&nbsp;billion expected</b>; <b>$2.22 adjusted EPS vs $2.10</b>; <b>Q3 guide $108&nbsp;billion &plusmn;2% vs $104.2&nbsp;billion expected</b>, with <b>no China data-center revenue assumed</b>. '
 '<b>&#9679; New &middot; 5:06 &mdash; the Data Center line now has its exact print:</b> a company-record <b>$89.02&nbsp;billion, &plus;116.6% year over year and &plus;18.3% sequentially</b>, which Nvidia attributes to <b>&ldquo;the ramp of our Blackwell Ultra infrastructure.&rdquo;</b> '
 '<b>The stock slipped in extended trading.</b> <b>&#9888; DIRECTION ONLY &mdash; the two percentages offered this run are both rejected in The Lead, so no magnitude is printed.</b> For scale, the options market had priced <b>~$282&nbsp;billion</b> of value in play on a <b>13.26%</b> implied swing.</p>',
 'nvda-p')

# 6. CRWD paragraph
rep('GAAP net income was <b>$5.3&nbsp;million, $0.01 a share</b> &mdash; positive, and far below the non-GAAP line, as the release&rsquo;s own reconciliation shows. <b>&#9888; No after-hours price move sourced.</b> The call is at <b>5:00&nbsp;p.m. ET</b>.</p>',
 'GAAP net income was <b>$5.3&nbsp;million, $0.01 a share</b> &mdash; positive, and far below the non-GAAP line, as the release&rsquo;s own reconciliation shows. '
 '<b>&#9679; New &middot; 5:06 &mdash; the stock now has a print: shares jumped as much as 12% in extended trading</b>, and the guidance behind it is out: '
 '<b>full-year FY27 revenue of $5.99&ndash;$6.01&nbsp;billion against a $5.94&nbsp;billion estimate</b> and <b>third-quarter revenue guidance of up to $1.53&nbsp;billion against $1.52&nbsp;billion</b>. The $0.31 beat is a <b>ninth consecutive quarterly EPS beat</b>. The call began at <b>5:00&nbsp;p.m. ET</b>.</p>',
 'crwd-p')

# 7. Remaining names
rep('<h3>Still to be seen: Okta, Williams-Sonoma, Abercrombie &amp; Fitch</h3>',
 '<h3>Still to be seen: Williams-Sonoma and Abercrombie &amp; Fitch</h3>','stb')
rep('<p><b>OKTA</b>, <b>WSM</b> and <b>ANF</b> were also on tonight&rsquo;s list per Yahoo Finance and TheStreet. <b>&#9888; No results and no after-hours prices for any of the three appeared in any source fetched this run &mdash; nothing is asserted about them.</b>',
 '<p><b>WSM</b> and <b>ANF</b> were also on tonight&rsquo;s list per Yahoo Finance and TheStreet. <b>&#9888; No results and no after-hours prices for either appeared in any source fetched this run &mdash; nothing is asserted about them.</b>',
 'wsm')
open(p,'w').write(h)
print("WS OK")
