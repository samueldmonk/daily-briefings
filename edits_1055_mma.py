#!/usr/bin/env python3
# MMA incremental edits — 10:55 a.m. ET edition, Wed Aug 26 2026
import sys, io
P = sys.argv[1] if len(sys.argv) > 1 else '.'
f = P + '/mma-briefing.html'
h = io.open(f, encoding='utf-8').read()
n = 0
def rep(old, new, cnt=1):
    global h, n
    assert h.count(old) >= 1, 'MISSING: ' + old[:110]
    h = h.replace(old, new, cnt); n += 1

# 1 — demote old New tags
rep('<span class="tag new">New &middot; 10:20</span>',
    '<span class="tag">Carried &middot; 10:20 edition</span>', 99)

# 2 — retire the unsourced event number from the card tag
rep('<span class="tag hot">This Saturday</span><span class="tag">Fight Night 286</span>',
    '<span class="tag hot">This Saturday</span><span class="tag">UFC Shanghai</span>')

# 3 — TLDR: add the business number now that one exists
rep('with Nurmagomedov a <b>&minus;470 favourite</b> at DraftKings.</span></div>',
    'with Nurmagomedov a <b>&minus;470 favourite</b> at DraftKings &mdash; while the business page finally gets a number, TKO&rsquo;s CFO having told investors the White House card lost about <b>$30&nbsp;million</b> on roughly <b>$60&nbsp;million</b> of production.</span></div>')

# 4 — Business & broadcast: replace the "none is published" note
rep('<p class="note"><b>Business &amp; broadcast.</b> No viewership figure, gate, TKO Group financial or broadcast-revenue number was stated in any source fetched this run, so <b>none is published</b>. The only dollar figures on this page are the bonus amounts stated in the UFC Sacramento reporting and the sportsbook lines for Saturday&rsquo;s main event. UFC&nbsp;331&rsquo;s broadcast timings &mdash; early prelims ~5&nbsp;p.m. ET, prelims 7&nbsp;p.m. ET, main card 9&nbsp;p.m. ET &mdash; are the only schedule detail confirmed.</p>',
    '<p class="note"><b>Business &amp; broadcast &mdash; the standing blank on this page is filled. <span class="tag new">New &middot; 10:55</span></b> Every recent edition has said that no viewership figure, gate or TKO Group financial was stated in any source fetched. One now is. <b>TKO Group Holdings chief financial officer Andrew Schleimer</b> told investors on the company&rsquo;s <b>second-quarter earnings call</b> that <b>UFC Freedom 250</b> &mdash; the seven-fight card staged on the White House South Lawn on <b>June&nbsp;14</b> &mdash; produced a <b>loss of roughly $30&nbsp;million</b>, a figure the company had anticipated. <b>Production ran about $60&nbsp;million</b>, and the promotion <b>sold no tickets</b>, seating around <b>4,000 invited guests</b> instead. Schleimer tied the card directly to <b>TKO&rsquo;s adjusted EBITDA margin falling from 59 percent to 52 percent year over year</b>, and told analysts the promotion used the event to sign partners on deals running <b>into 2027 and beyond</b>. Set against that, <b>TKO president and chief operating officer Mark Shapiro</b> said Freedom 250 generated <b>more than $1&nbsp;billion in earned media value</b> &mdash; which is, in the reporting&rsquo;s framing, the argument for doing it again.</p>\n'
    '<p class="note"><b>&#9888; Source and date, stated plainly.</b> Those figures come from MMA News (Mike Reichlin), <b>published August&nbsp;15, 2026</b> and fetched in full this run. They are <b>quarterly-earnings-call figures reported by that outlet</b>, not numbers read off a TKO filing by this desk, and they are eleven days old &mdash; they are published as the first sourced business numbers this page has been able to carry, not as today&rsquo;s news. <b>No gate, no viewership figure and no broadcast-revenue number is published</b>, because none was stated. UFC&nbsp;331&rsquo;s broadcast timings &mdash; early prelims ~5&nbsp;p.m. ET, prelims 7&nbsp;p.m. ET, main card 9&nbsp;p.m. ET &mdash; remain the only schedule detail confirmed.</p>')

# 5 — Around the sport: the "impossible event"
rep('<li><b>The bantamweight logjam is being watched closely.</b>',
    '<li><b>Dana White is teasing an &ldquo;impossible event&rdquo; &mdash; and the window he gave has already passed. <span class="tag new">New &middot; 10:55</span></b> Speaking on <b>The Pat McAfee Show</b>, White said the UFC&rsquo;s next spectacle event was close enough that an announcement <b>could land within a week</b>, and that the concept came from <b>Craig Borsari</b>, the promotion&rsquo;s head of production, who pitched it after running the White House card in June. White said he had calls scheduled once <b>UFC&nbsp;330</b> was finished, after which Borsari would fly out and walk the site: <b>&ldquo;If I end up doing this, I&rsquo;ll announce it here first.&rdquo;</b> He gave <b>no location, no date and no explanation of what makes the event difficult</b>, and has repeatedly said it will not top what the promotion pulled off in Washington. <b>&#9888; That report is dated August&nbsp;15</b>, before UFC&nbsp;330; the &ldquo;within a week&rdquo; window has therefore elapsed, and <b>no announcement has surfaced in any source fetched this run</b>. It is carried as a tease that has not yet resolved, not as a pending event. White has previously floated the <b>Roman Colosseum</b>, a site he has since called impossible on logistics.</li>\n'
    '<li><b>The bantamweight logjam is being watched closely.</b>')

# 6 — Sources
rep('<div class="lab">Sources</div>\n<ul>\n',
    '<div class="lab">Sources</div>\n<ul>\n'
    '<li><b>MMA News &mdash; <a href="https://www.mmanews.com/article/dana-white-ufc-next-impossible-event-announcement">&ldquo;Dana White Says UFC Could Announce Its Next Impossible Event&rdquo;</a></b> (Mike Reichlin, published August&nbsp;15, 2026), <b>fetched in full this run</b> &mdash; the source for every figure in Business &amp; broadcast: the <b>~$30&nbsp;million</b> loss on UFC Freedom 250 as stated to investors by TKO CFO <b>Andrew Schleimer</b> on the second-quarter earnings call, the <b>~$60&nbsp;million</b> production cost, the <b>no ticket sales / ~4,000 invited guests</b> detail, the <b>59% &rarr; 52%</b> adjusted-EBITDA-margin move, the partner deals running into 2027, and <b>Mark Shapiro</b>&rsquo;s <b>&gt;$1&nbsp;billion earned-media-value</b> figure &mdash; and for the &ldquo;impossible event&rdquo; tease, Craig Borsari&rsquo;s role, the Pat McAfee Show setting and the quoted line. <b>&#9888; Dated August&nbsp;15 and carried at that date; nothing here is presented as August&nbsp;26 news.</b></li>\n')

io.open(f, 'w', encoding='utf-8').write(h)
print('mma OK — %d edits' % n)
