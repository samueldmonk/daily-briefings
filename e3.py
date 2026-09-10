D='/sessions/youthful-laughing-hamilton/mnt/outputs/'
p=D+'mma-briefing.html'; h=open(p).read()

def sub(old,new):
    global h
    assert h.count(old)==1,(old[:70],h.count(old))
    h=h.replace(old,new)

# odds refresh
sub('<b>Odds:</b> Silva &minus;450 / Delgado +350 at <b>Caesars</b>; &minus;428 / +324 as an average across 20 books tracked by UFCalendar. The line opened near &minus;425 and has traded in a &minus;400 to &minus;450 band. Silva&rsquo;s implied win probability sits around <b>80&ndash;82%</b>.',
 '<b>Odds, re-read for this edition:</b> Silva <b>&minus;440</b> / Delgado <b>+340</b> at <b>DraftKings</b>, and <b>&minus;430 / +335</b> at <b>Bovada</b>. Reads earlier today gave &minus;450 / +350 at Caesars and a &minus;428 / +324 average across 20 books tracked by UFCalendar, so the line has drifted a little toward the underdog without leaving the <b>&minus;400 to &minus;450</b> band it opened in near &minus;425. Silva&rsquo;s implied win probability sits around <b>80&ndash;82%</b>. This is the one card on the page with anything new attached to it tonight, which is why it alone is tagged Updated.')

# tag on that card -> Updated (highlighted)
sub('<div class="card"><span class="t carried">Updated</span><div class="kv">Sat 12 September &middot; Desert Diamond Arena',
    '<div class="card"><span class="t new">Updated</span><div class="kv">Sat 12 September &middot; Desert Diamond Arena')
h=h.replace('<span class="t carried">Updated</span>','<span class="t carried">Carried</span>')

# top story attribution
sub('<p>Asked on <b>9 September</b> for an update on the heavyweight champion&rsquo;s health, UFC chief executive Dana White said:',
 '<p>Speaking at a Contender Series press conference, in remarks reported on <b>9 September</b>, UFC chief executive Dana White gave this update on the heavyweight champion&rsquo;s health:')

# around the sport: callouts bullet
sub('<li><b>Roster churn cuts both ways.</b>',
 '<li><b>The heavyweight callouts have started.</b> With no Aspinall timeline to wait on, <b>Alex Pereira, Ciryl Gane and Josh Hokit have spent recent days calling each other out on social media</b> &mdash; which is what a division does when its champion has no return date and an interim belt is already in the room. Gane holds that interim title; Pereira lost to him for it at Freedom 250. Carried as reported: <b>no bout involving any of the three has been announced</b>.</li>\n<li><b>Roster churn cuts both ways.</b>')

# tags note
sub('<b>On the &ldquo;Carried&rdquo; tags.</b> Five editions of this page have published today, at 12:57, 1:15, 1:50, 6:15 p.m. and now, after 8 p.m. <b>No fight result, booking, signing or withdrawal landed in the latest interval</b> &mdash; a search for the day&rsquo;s UFC news returned only that no event is scheduled for Wednesday and that Noche UFC on Saturday is next &mdash; so <b>every card is tagged Carried and none is tagged New or Updated</b>. The two cards marked Updated last edition were demoted before tagging. Tagging an unchanged card &ldquo;New&rdquo; because the page was rebuilt would be a lie about the news, not about the build.',
 '<b>On the tags.</b> Six editions of this page have published today &mdash; at 12:57, 1:15, 1:50, 6:15, 8:29 p.m. and now. <b>No fight result, booking, signing or withdrawal has landed since the last one</b>: a fresh search for the day&rsquo;s UFC news again returned only that no event was scheduled for Wednesday and that Noche UFC on Saturday is next. So <b>no card is tagged New</b>, and every card carried from the previous edition was demoted before tagging. <b>One card is tagged Updated</b> &mdash; the Noche UFC main event, whose odds were re-read from two sportsbooks for this edition and have moved slightly. Tagging an unchanged card &ldquo;New&rdquo; because the page was rebuilt would be a lie about the news, not about the build.')

# champions note block
i=h.find('<div class="note"><b>How this board was checked this run.')
j=h.find('</div>',h.find('discrepancy stays flagged'))+6
assert i>0 and j>i
newnote=('<div class="note"><b>How this board was checked this run.</b> Every belt was re-checked against a fresh current-champions read for this edition, and this time <b>ten of the eleven rows matched exactly on champion and date</b> &mdash; Aspinall 21 Jun 2025, <b>Ulberg 11 Apr 2026</b>, Strickland 9 May 2026, Makhachev 15 Nov 2025, Gaethje 14 Jun 2026, Volkanovski 12 Apr 2025, Yan 6 Dec 2025, Van 6 Dec 2025, Harrison 7 Jun 2025 and Dern 25 Oct 2025. <b>The Pereira-at-205 regression that the previous edition had to refuse did not recur in this read:</b> light heavyweight came back as Carlos Ulberg, correctly. That is worth stating plainly, because it shows the failure is a property of individual reads rather than of the sport &mdash; two hours ago a read seated Pereira at light heavyweight and had to be refused; this one does not. Neither read seated Chimaev at middleweight, and neither called featherweight vacant.'
 '<br><br><b>One row was refused, and it is the same row as last time.</b> The read seats <b>Valentina Shevchenko at women&rsquo;s flyweight, dated 14 September 2024, with two defences</b>. She <b>vacated</b> that title while sidelined by injury, and <b>Nat&aacute;lia Silva vs. Wang Cong contest the vacant belt at UFC 332 on 3 October</b> &mdash; corroborated by the UFC 332 card itself, which bills the bout as being for the vacant title. The row was not carried; the belt stays <b>vacant</b> above. Ten correct rows do not license the eleventh, which is exactly why every belt is checked against the latest event results rather than copied from a list.'
 '<br><br><b>An open conflict this page keeps flagging rather than resolving.</b> This run&rsquo;s read again carried defence tallies, and again reproduced the disagreement: it lists <b>0 defences for both Joshua Van and Mackenzie Dern</b>, and 0 for Aspinall, Strickland, Gaethje, Yan and Harrison, with <b>1 each for Volkanovski and Makhachev</b>. The event record says otherwise for two of those &mdash; Van TKO5 Tatsuro Taira at UFC 328 and Dern UD Gillian Robertson at UFC 330 each look like a title defence, and the table above counts them as such. That is now the third consecutive read to reproduce the conflict, so it is a live disagreement between the reference list and the event record, not an artefact of one stale page, and it stays flagged rather than silently resolved in either direction.</div>')
h=h[:i]+newnote+h[j:]

# sources
marker='<footer><h5>Sources</h5>'
urls=['https://sports.yahoo.com/articles/dana-white-heavyweight-division-keep-110000289.html',
 'https://sports.yahoo.com/articles/noche-ufc-4-odds-betting-171123912.html',
 'https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161244-opening-betting-odds-for-noche-ufc-silva-vs-delgado/',
 'https://www.sherdog.com/news/news/Noche-UFC-4-odds-Alexa-Grasso-an-underdog-massive-850-favorite-emerges-202727',
 'https://www.rotowire.com/mma/article/ufc-best-bets-today-picks-odds-predictions-for-noche-ufc-133214']
add=''.join(f'<div><a href="{u}">{u}</a></div>' for u in urls if u not in h)
h=h.replace(marker,marker+add,1)
open(p,'w').write(h); print('mma ok')
