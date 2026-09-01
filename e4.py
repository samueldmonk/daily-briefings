# -*- coding: utf-8 -*-
import io
P='/tmp/db_1788305419/wallstreet-briefing.html'
s=io.open(P,encoding='utf-8').read(); n=0
def rep(old,new,label):
    global s,n
    c=s.count(old)
    if c!=1: print(('MISS: ' if c==0 else 'AMBIG(%d): '%c)+label); return False
    s=s.replace(old,new); n+=1; print('ok:',label); return True

# W6 -- append a post-close paragraph to The Lead
rep('nothing fetched this run confirms or refutes where the finished session ranks.</p></div>',
 'nothing fetched this run confirms or refutes where the finished session ranks.</p>'
 '<p style="margin-top:11px"><b>Since the close, the day has acquired a second half that has nothing to do with any of the above.</b> '
 'Three companies reported after the bell &mdash; <b>Dell, GitLab and MongoDB</b> &mdash; and produced the largest single-name moves attached to September 1, '
 'none of them during September 1&rsquo;s trading. Dell&rsquo;s print is the substantial one: <b>record revenue of $47 billion, up 58% year over year</b>, '
 '<b>a record $60.9 billion in AI server orders</b>, a <b>record $95 billion backlog</b> and full-year revenue guidance raised to <b>$192 billion</b>. '
 '&#9888; <b>These moves are deliberately kept out of the story above.</b> The session was a bond-and-oil story from the opening bell to the closing one, and it stays that way; '
 'the earnings are a separate event that happened afterwards and are covered in After-Hours Movers. '
 '&#9888; <b>The reason for the separation is not tidiness.</b> A macro session and an earnings evening have different causes, different participants and different durability &mdash; '
 'after-hours prices routinely do not survive the next open &mdash; and folding a $60.9 billion order book into an explanation of why the Nasdaq Composite fell 1.03% today '
 'would attribute a move to news that had not yet been published when the move happened.</p></div>',
 'W6 lead post-close para')

# W7 -- On the Radar additions
rep('<h2>On the Radar</h2><div class="panel"><ul class="bul"><li><b>The calendar itself is part of the story',
 '<h2>On the Radar</h2><div class="panel"><ul class="bul">'
 '<li><b>Tomorrow&rsquo;s open is the first test of tonight&rsquo;s three prints.</b> Dell, GitLab and MongoDB all moved sharply after the bell, and '
 '<b>after-hours quotes are thin and frequently do not hold</b>. The specific thing to watch is <b>MongoDB</b>: it beat on earnings and revenue, posted its '
 '<b>fastest revenue growth since fiscal 2024</b>, raised full-year guidance, and fell double digits anyway. '
 '&#9888; <b>No explanation for that has been sourced, and this page has not invented one</b> &mdash; if a reason emerges it will be a fact about expectations rather than about the quarter.</li>'
 '<li><b>The Federal Open Market Committee meets September 15&ndash;16</b>, and the pricing on this page has moved a long way in a week. '
 'The marks carried today span <b>CME FedWatch at 66%</b>, <b>Forbes at around 65%, up from 40% in late August</b>, <b>a read of odds near 70%</b> worth about '
 '<b>17 basis points of tightening</b>, and <b>Kalshi at 57% hike / 42% hold</b> &mdash; <b>all for a hike, in a year that began priced for a cut</b>. '
 '&#9888; <b>Five probabilities from five clocks, none adopted.</b> What matters is not which is right but that every one of them is on the same side of the argument.</li>'
 '<li><b>The Strait of Hormuz is the single variable behind both the oil line and the bond line.</b> Crude is bid because supply is threatened, long yields are up because crude is bid, '
 'and equities are down because long yields are up. &#9888; <b>That is one story wearing three hats, and it is worth naming as such:</b> the page&rsquo;s energy, rates and equity sections today are '
 'not three independent observations, and treating them as mutual confirmation would be double-counting a single cause.</li>'
 '<li><b>The calendar itself is part of the story',
 'W7 radar')

io.open(P,'w',encoding='utf-8').write(s); print('applied',n)
