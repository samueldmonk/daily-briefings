# -*- coding: utf-8 -*-
import io
P='/tmp/db_1788305419/wallstreet-briefing.html'
s=io.open(P,encoding='utf-8').read(); n=0
def rep(old,new,label):
    global s,n
    c=s.count(old)
    if c!=1: print(('MISS: ' if c==0 else 'AMBIG(%d): '%c)+label); return False
    s=s.replace(old,new); n+=1; print('ok:',label); return True

# W2 ticker: feature the evening's three earnings names alongside DELL
rep('{"proName":"NYSE:DELL","title":"Dell"}',
    '{"proName":"NYSE:DELL","title":"Dell"},{"proName":"NASDAQ:GTLB","title":"GitLab"},{"proName":"NASDAQ:MDB","title":"MongoDB"}',
    'W2 ticker symbols')

# W3: After-Hours Movers -> full rewrite
i=s.find('<h2>After-Hours Movers</h2>')
j=s.find('<h2>Weekly Scorecard')
assert i>0 and j>i
ah = ('<h2>After-Hours Movers</h2><div class="panel">'
 '<p style="margin:0 0 10px;color:var(--muted2)">&#9888;&#9888; <b>This section said the opposite three hours ago, and the reversal is the story.</b> '
 'The 4:35 PM edition of this page recorded that the after-hours tape was quiet, that macro &ldquo;sells the whole index during the session and gives the after-hours tape nothing to trade,&rdquo; '
 'and that this was <i>the opposite of an earnings evening, when the index is quiet and individual names gap.</i> '
 '<b>The earnings evening then arrived.</b> Three large software and hardware reports landed after the close and the tape did exactly what that sentence described. '
 'The earlier observation is not deleted &mdash; it was true of the 4:35 PM tape and false of the 7:30 PM one, which is a fact about the clock rather than an error in the reading.</p>'

 '<div class="cards">'

 '<div class="card"><div class="tags"><span class="tag t-a">New</span><span class="tag t-c">Earnings</span></div>'
 '<h3>Dell Technologies <span class="up">+8% to +10% after hours</span></h3>'
 '<p>The largest single-name move of the evening, and the one with the most in it. Dell reported <b>revenue of $46.971&nbsp;billion against $44.915&nbsp;billion expected</b> and '
 '<b>adjusted earnings of $7.04 a share against $4.95 expected</b>. The company described <b>record revenue of $47&nbsp;billion, up 58% year over year</b>, with '
 '<b>adjusted earnings up 203%</b>, and booked <b>a record $60.9&nbsp;billion in AI server orders</b>, exiting the quarter with a <b>record $95&nbsp;billion backlog</b>. '
 'Full-year revenue guidance was raised to <b>$192&nbsp;billion</b>. '
 '&#9888; <b>Three reads, three clocks, and they are printed rather than reconciled:</b> one has the stock <b>up as much as 10%</b> after hours, '
 'one quotes <b>$462.34, +8.79%</b>, and a movers board quotes <b>$461.00, +8.47%</b>. The range is the honest answer; a single number would not be.</p>'
 '<p style="margin-top:9px">&#9888; <b>Read this against what the same page said during the session.</b> The Movers &amp; Drivers card above records that '
 '<b>&ldquo;Dell slipped ahead of its earnings&rdquo;</b> in the semiconductor-led sell-off. The stock fell into the print and gapped after it &mdash; '
 'the ordinary shape of an earnings day, and a reminder that the session move and the evening move are two different measurements of two different things.</p></div>'

 '<div class="card"><div class="tags"><span class="tag t-a">New</span><span class="tag t-c">Earnings</span></div>'
 '<h3>GitLab <span class="up">+~16% after hours</span></h3>'
 '<p><b>Revenue rose 21% year over year to $286.3&nbsp;million</b>, ahead of a <b>$273.12&nbsp;million</b> forecast, with <b>adjusted earnings of $0.25 a share against $0.18 expected</b> '
 'and non-GAAP operating income of <b>$42.6&nbsp;million, a 15% margin</b>. Full-year fiscal 2027 revenue guidance was raised to <b>$1.129&ndash;$1.133&nbsp;billion</b>, implying <b>18% to 19% growth</b>, '
 'with non-GAAP operating income of <b>$148&ndash;$152&nbsp;million</b> and adjusted earnings per share of <b>$0.85&ndash;$0.87</b>; the third quarter is guided to <b>$281&ndash;$283&nbsp;million</b>. '
 '&#9888; <b>Two reads again:</b> <b>+15.95% to $52.28</b> on one, <b>+17.61% to $53.03</b> on the other, after the stock had <b>fallen 3.12% to $45.09 in the regular session</b>. '
 'Both are printed; the gap between them is a timestamp, not a dispute.</p></div>'

 '<div class="card"><div class="tags"><span class="tag t-a">New</span><span class="tag t-c">Earnings</span></div>'
 '<h3>MongoDB <span class="down">&minus;12% to &minus;13% after hours</span></h3>'
 '<p>&#9888;&#9888; <b>The interesting one, because the numbers were good.</b> MongoDB reported <b>adjusted earnings of $1.90 a share</b> and <b>revenue of $771.8&nbsp;million</b>, '
 '<b>both above Wall Street forecasts</b>; revenue rose <b>30% year over year, the company&rsquo;s fastest quarterly growth since fiscal 2024</b>, and management '
 '<b>raised full-year guidance</b>. The stock fell anyway &mdash; <b>&minus;12.46% to $380.10</b> on one read and <b>&minus;13.18% to $377</b> on another, '
 'after closing the regular session <b>down 4.22% at $434.26</b>. '
 '&#9888; <b>No cause is supplied, because none was sourced.</b> A beat-and-raise that sells off is the kind of move that invites a guess about expectations, positioning or guidance quality; '
 'nothing fetched this run states one, so this card reports the beat, the raise and the decline, and stops.</p></div>'

 '<div class="card"><div class="tags"><span class="tag t-b">Carried</span><span class="tag t-c">Single name</span></div>'
 '<h3>Oracle traded lower after the bell</h3>'
 '<p>Carried from the 4:35 PM edition and unchanged: investors reacted to <b>significant job cuts effective September 1</b> and to a '
 '<b>planned $20 billion equity issuance to fund AI infrastructure</b>. &#9888; <b>No percentage for Oracle appeared in what was fetched then or now, and none is supplied.</b> '
 '&#9888; Both catalysts remain financing-side rather than demand-side: an equity raise to fund a build is a statement about how it is paid for, not about whether it pays off.</p></div>'

 '<div class="card"><div class="tags"><span class="tag t-b">Carried</span><span class="tag t-c">Mega-cap</span></div>'
 '<h3>The mega-caps stayed still while the reporters moved</h3>'
 '<p>The 4:35 PM reads had <b>Alphabet <span class="up">+0.03%</span></b>, <b>Microsoft <span class="down">&minus;0.12%</span></b>, <b>NVIDIA <span class="down">&minus;0.42%</span></b>, '
 '<b>Apple flat at 0.00%</b>, <b>Salesforce <span class="up">+0.21%</span></b>, <b>Tesla <span class="down">&minus;0.54%</span></b> and <b>Amazon <span class="up">+0.09%</span></b>. '
 '&#9888; <b>These are the earlier clock and are labelled as such;</b> they have not been refetched and are not presented as the 7:30 PM tape. '
 'They are kept because the contrast is the point &mdash; the names with news gapped, the names without news did not, which is the mechanism the opening paragraph describes.</p></div>'

 '</div>'
 '<div class="note">&#9888; <b>What this section does not claim.</b> Three companies reporting on the same evening is a calendar coincidence, not a sector verdict &mdash; '
 'Dell sells AI infrastructure, GitLab sells developer software and MongoDB sells a database, and the two that rose and the one that fell are not evidence about each other. '
 '&#9888; <b>After-hours prices are thin and frequently do not survive the next open;</b> every figure above is an after-hours quote, not a close, and none of them is in the Weekly Scorecard below.</div>'
 '</div>')
s=s[:i]+ah+s[j:]; n+=1; print('ok: W3 after-hours rewrite')

io.open(P,'w',encoding='utf-8').write(s)
print('applied',n)
