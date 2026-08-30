#!/usr/bin/env python3
"""The Octagon edits — Sunday Aug 30 2026, ~3:36 PM ET research, seventh run of the day."""
import io, os, sys

D = sys.argv[1]
P = os.path.join(D, 'mma-briefing.html')
h = io.open(P, encoding='utf-8').read()
n = 0

def sub(old, new, label):
    global h, n
    if old not in h:
        print('MISS:', label); return
    h = h.replace(old, new, 1); n += 1
    print('  ok:', label)

# ── 1. TLDR ─────────────────────────────────────────────────────────────────
i = h.find('<div class="tldr"><b>Tale of the Tape</b> <span>')
j = h.find('</span></div>', i)
new_tldr = ('<div class="tldr"><b>Tale of the Tape</b> <span>The <b>UFC 333 card has filled out from two title '
            'fights into a full main card</b> &mdash; Volkov&ndash;Kuniev, Arnold Allen&ndash;Aaron Pico, '
            'Reyes&ndash;Murzakanov, Magomedov&ndash;Rowston, Krylov&ndash;Yakhyaev and Dawson&ndash;Aliev now '
            'sit under the two belts, with the main card at <b>2 PM ET</b> on Paramount+ at no extra cost; '
            'Song Yadong&rsquo;s post-fight record is sourced for the first time at <b>24-9-1, 1 NC</b>, and '
            'Umar Nurmagomedov has spoken &mdash; <b>&ldquo;I will work on the mistakes. And I will be '
            'back&rdquo;</b> &mdash; with reporting adding that it was the <b>first finish of his career</b>; '
            'and a <b>ranking conflict is recorded rather than resolved</b>, because one outlet calls '
            'Nurmagomedov the <b>No. 2</b> bantamweight where this page has carried <b>No. 3</b>.')
h = h[:i] + new_tldr + h[j:]
n += 1
print('  ok: tldr')

# ── 2. Top Story — post-fight record, the finish first, the statement ───────
sub('<h2 class="sec">Top Story</h2>\n<div class="panel lead" style="border-left:3px solid var(--acc)">\n',
    '<h2 class="sec">Top Story</h2>\n<div class="panel lead" style="border-left:3px solid var(--acc)">\n'
    '<p><span class="tag new">New &middot; 3:36 PM</span> <b>Three things arrived about a fight this page has '
    'carried since the 9:15 edition, and one of them is a number it had been careful not to compute.</b> '
    '<b>First, Song&rsquo;s record after the win is now stated rather than derived:</b> a post-event report '
    'fetched this run puts him at <b>24-9-1 with one no contest</b>. This page has printed his pre-fight '
    '<b>23-9-1, 1 NC</b> throughout and declined to add the win to it, on the same reasoning that kept '
    'Nurmagomedov&rsquo;s second loss unstated until a source said it. <b>Both halves of that pair are now '
    'sourced, and neither was ever guessed.</b> <b>Second, the finish has a first attached to it:</b> reporting '
    'this run states that Nurmagomedov was <b>finished for the first time in his career</b> &mdash; his '
    'previous defeat, at UFC 311, went to the judges. <b>Third, he has spoken.</b> On social media he wrote: '
    '<b>&ldquo;Everything is fine with me. Thank you so much to everyone who writes. I will work on the '
    'mistakes. And I will be back.&rdquo;</b> His team posted separately: <b>&ldquo;The result cannot be '
    'changed today; the opponent won. Everything happened according to the will of the Almighty, and there is '
    'wisdom in that.&rdquo;</b> <b>No injury, medical suspension or timeline was stated by anything fetched, '
    'and none is printed.</b></p>\n'
    '<p>&#9888; <b>A ranking disagreement is recorded and not resolved, because it changes the size of the '
    'upset.</b> This page has carried Nurmagomedov as the <b>No. 3</b> bantamweight, from the sourcing it had '
    'at the time. A rankings write-up fetched this run calls him <b>previously ranked No. 2</b>. <b>Neither is '
    'adopted over the other</b> &mdash; official rankings update on their own schedule and a post-event article '
    'may be describing the board either before or after that update. The two figures this page is confident of '
    'are unaffected: <b>Song entered at No. 6</b> and <b>beat a former title challenger</b> either way. '
    '<b>A number that moves the story is worth flagging even when the story survives it.</b></p>\n',
    'top story new paras')

# ── 3. UFC 333 — the rest of the card ───────────────────────────────────────
sub('Also listed: <b>Lone&rsquo;er Kavanagh</b> (No.&nbsp;6 flyweight) vs.\n<b>Ramazan Temirov</b> (No.&nbsp;7).',
    'Also listed: <b>Lone&rsquo;er Kavanagh</b> (No.&nbsp;6 flyweight) vs.\n<b>Ramazan Temirov</b> (No.&nbsp;7). '
    '<b>Filled out at 3:36 PM &mdash; the card is no longer two title fights and a flyweight bout.</b> The main '
    'card as listed this run adds <b>Alexander Volkov vs. Rizvan Kuniev</b> at heavyweight, <b>Arnold Allen vs. '
    'Aaron Pico</b> at featherweight, <b>Dominick Reyes vs. Azamat Murzakanov</b> and <b>Nikita Krylov vs. '
    'Abdul Rakhman Yakhyaev</b> at light heavyweight, <b>Abus Magomedov vs. Cam Rowston</b> at middleweight and '
    '<b>Grant Dawson vs. Nurullo Aliev</b> at lightweight. <b>The main card starts at 2 PM ET / 11 AM PT</b> '
    '&mdash; an afternoon start in the United States, set by Abu Dhabi&rsquo;s clock &mdash; and the event is '
    'on <b>Paramount+ with no pay-per-view charge</b>, included with a subscription. &#9888; <b>The Yakhyaev '
    'spelling is deliberate:</b> it is <b>Abdul Rakhman Yakhyaev</b>, no hyphen, the form this project&rsquo;s '
    'own standing corrections file records after the name was published wrong once &mdash; and he is the same '
    'fighter as the light-heavyweight record 33-second debut submission and the 8-second knockout at UFC Baku, '
    'not a second man with a similar name.',
    'ufc 333 card fill')

# ── 4. Rankings & Business — where Song lands ───────────────────────────────
sub('</ul></div><h2 class="sec">Rankings &amp; Business</h2><div class="cards">\n',
    '</ul></div><h2 class="sec">Rankings &amp; Business</h2><div class="cards">\n'
    '<div class="card"><div class="tags"><span class="tag new">New &middot; 3:36 PM</span>'
    '<span class="tag warn">Reporting, not a booking</span></div>'
    '<h4>Where the win puts Song, in the words of the people who cover the division rather than of the promotion</h4>'
    '<p><b>What the reporting says.</b> Write-ups fetched this run put Song on a <b>two-fight winning streak</b> '
    'and <b>3-1 in his last four</b>, say the win <b>lands him in the top five</b>, and frame his realistic next '
    'assignment as a <b>title eliminator</b> against whoever wins <b>Yan vs. Dvalishvili 3</b> at UFC 333 in '
    'October. One goes further and says the performance <b>could catapult him into the No. 1 contender '
    'position</b>. Another states plainly that Nurmagomedov <b>was the one working toward another championship '
    'opportunity and that Song has taken his place in the contender line</b>.</p>'
    '<p>&#9888; <b>None of that is an announcement, and this page keeps the distinction it has kept all '
    'weekend.</b> Every sentence above is an outlet&rsquo;s read of the matchmaking. <b>The promotion has '
    'booked nothing after UFC 333</b> &mdash; no source fetched this run says otherwise &mdash; and the '
    'competing claim on that shot, former champion <b>Sean O&rsquo;Malley</b>, is recorded elsewhere on this '
    'page on exactly the same footing. <b>A consensus among writers is still not a contract</b>, and the '
    'bantamweight belt on the Champions Board below is Petr Yan&rsquo;s with a defence already scheduled.</p>'
    '</div>\n',
    'rankings song card')

# ── 5. Sources ──────────────────────────────────────────────────────────────
sub('<b>Sources checked this run:</b><br>',
    '<b>Sources checked this run:</b><br>'
    '<a href="https://sportsnaut.com/ufc/ufc-bantamweight-rankings-after-ufc-shanghai-2026">Sportsnaut &mdash; New UFC bantamweight rankings after UFC Shanghai (Song 24-9-1; &ldquo;previously ranked No. 2&rdquo;)</a><br>'
    '<a href="https://sports.yahoo.com/articles/umar-nurmagomedov-releases-statement-following-161222125.html">Yahoo Sports &mdash; Umar Nurmagomedov releases statement following UFC Shanghai knockout loss</a><br>'
    '<a href="https://bloodyelbow.com/2026/08/29/team-nurmagomedov-releases-first-statement-after-umars-devastating-ufc-shanghai-knockout-loss/">Bloody Elbow &mdash; Team Nurmagomedov&rsquo;s first statement after the Shanghai loss</a><br>'
    '<a href="https://sports.yahoo.com/articles/latest-ufc-333-fight-card-150135884.html">Yahoo Sports &mdash; Latest UFC 333 fight card and Paramount+ lineup (main card 2 PM ET)</a><br>'
    '<a href="https://www.ufc.com/event/ufc-333">UFC.com &mdash; UFC 333: Volkanovski vs. Evloev (event page)</a><br>'
    '<a href="https://bleacherreport.com/articles/25472734-ufc-333-fight-card-revealed-merab-dvalishvili-vs-petr-yan-3-volkanovski-vs-evloev">Bleacher Report &mdash; UFC 333 fight card revealed: Dvalishvili vs. Yan 3, Volkanovski vs. Evloev</a><br>'
    '<a href="https://sports.yahoo.com/articles/bantamweight-breakdown-song-yadong-status-221537850.html">Yahoo Sports &mdash; Bantamweight breakdown: Song Yadong&rsquo;s status after UFC Shanghai</a><br>',
    'mma sources')

io.open(P, 'w', encoding='utf-8').write(h)
print(f'mma edits applied: {n}')
