#!/usr/bin/env python3
"""MMA edits, 2026-09-07 ~08:50 ET (Morning Edition, SECOND run of the day)."""
import sys, io

P = 'mma-briefing.html'
h = io.open(P, encoding='utf-8').read()
orig = h
n = 0

def sub(old, new, label):
    global h, n
    if h.count(old) != 1:
        sys.exit('MISS(%d): %s' % (h.count(old), label))
    h = h.replace(old, new, 1)
    n += 1
    print('  ok:', label)

# ---------------------------------------------- 1. NAME FIX (standing rule: exact spelling)
print('  skip: applied')

# ---------------------------------------------- 2. Delgado detail, newly sourced
old = ('Delgado is <b>12&ndash;2</b> and 4&ndash;1 with a pair of knockouts. '
       'Officially UFC Fight Night 288, billed as Noche UFC 4.')
new = ('Delgado is <b>12&ndash;2</b> and 4&ndash;1 with a pair of knockouts, and newly sourced '
       'this edition: he has <b>won nine of his last ten</b>, he earned his roster spot with a '
       'knee to the head of <b>Ernie Juarez</b> on season 8 of Dana White&rsquo;s Contender Series '
       'in <b>August 2024</b>, and his only UFC loss came to <b>Nathaniel Wood</b> in '
       '<b>October 2025</b> by unanimous decision, in a bout he <b>missed weight</b> for. Silva is '
       'described in the same reporting as the <b>No. 6-ranked</b> featherweight contender, and '
       'Delgado enters as a sizable underdog &mdash; which the odds line below already says '
       'numerically. Officially UFC Fight Night 288, billed as Noche UFC 4, and the card carries '
       '<b>13 bouts</b> in total.')
print('  skip: applied')

# ---------------------------------------------- 3. Blaydes / Cortes-Acosta descriptors
old = '<b>Waldo Cortes-Acosta vs. Curtis Blaydes</b> at heavyweight'
new = ('<b>Waldo Cortes-Acosta vs. Curtis Blaydes</b> at heavyweight &mdash; Wikipedia&rsquo;s '
       'event page describes Blaydes as a former interim heavyweight <i>title challenger</i> and '
       'Cortes-Acosta as a former <b>LFA</b> heavyweight champion; both descriptors are carried '
       'with that attribution and neither man is described as a former UFC champion, because '
       'neither is')
print('  skip: applied')

# ---------------------------------------------- 4. Rankings: name the trap
old = ('The most recent rankings return seen this run is still dated <b>2 September</b> &mdash; before '
       'the Paris card &mdash; so no official post-event movement is reflected anywhere yet, and '
       'none is asserted here.')
new = ('No post-Paris board has been sourced yet, and this run turned up a live trap on the way to '
       'establishing that. A search aimed squarely at &ldquo;Meta UFC Rankings, September 2026&rdquo; '
       'returned real, specific, confidently-dated movement &mdash; <b>Song Yadong</b> climbing in the '
       'bantamweight order and <b>Denise Gomes</b> jumping in women&rsquo;s strawweight. Both are '
       'genuine; <b>neither has anything to do with Paris</b>. They are the board&rsquo;s response to '
       '<b>UFC Shanghai on 29 August</b>, where Song knocked out Umar Nurmagomedov and Gomes finished '
       'Yan Xiaonan. Printing them here would have dressed a nine-day-old update as this morning&rsquo;s. '
       'They are additionally not printed as numbers at all, because two returns in the same search '
       'disagreed on where Song actually landed &mdash; one said third, one said fourth. So: no '
       'post-Paris movement is asserted here.')
sub(old, new, 'rankings: Shanghai-not-Paris trap named')

# ---------------------------------------------- 5. sources
old = 'Sources</h2><div class="panel srcs">'
new = ('Sources</h2><div class="panel srcs">'
       '<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado">Wikipedia &mdash; '
       'UFC Fight Night: Silva vs. Delgado (Noche UFC 4)</a> &nbsp;&middot;&nbsp; '
       '<a href="https://www.ufc.com/event/ufc-fight-night-september-12-2026">UFC.com &mdash; Noche UFC: '
       'Silva vs Delgado</a> &nbsp;&middot;&nbsp; ')
sub(old, new, 'sources footer')

io.open(P, 'w', encoding='utf-8').write(h)
print('mma: %d edits, %d -> %d bytes' % (n, len(orig), len(h)))
