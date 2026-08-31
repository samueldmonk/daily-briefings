#!/usr/bin/env python3
"""MMA page — 1:12 PM ET edition, Aug 31 2026. Content edits only."""
import io

P = 'mma-briefing.html'
h = io.open(P, encoding='utf-8').read()
orig = len(h)

# ---------------------------------------------------------------- 1. TLDR
s = h.find('<div class="tldr"><b>Tale of the Tape</b>')
assert s > 0
e = h.find('</div>', h.find('</span>', s)) + len('</div>')
NEW_TLDR = (
'<div class="tldr"><b>Tale of the Tape</b> <span>'
'<b>The champions board has been fully cross-checked for the first time in eighteen attempts &mdash; '
'all eleven divisions returned, all eleven matched.</b> An ESPN-sourced sweep this run reached the '
'<b>women&rsquo;s divisions and both smaller men&rsquo;s classes</b>, which the last four checks never '
'did, and confirmed <b>Yan</b>, <b>Van</b>, <b>Harrison</b>, <b>Shevchenko</b> and <b>Dern</b> alongside '
'the six it usually reaches. <b>Board unchanged &mdash; seventy-fifth consecutive edition</b>, and for '
'the first time in weeks <b>no row is carried unverified</b>. On the calendar, <b>UFC Edmonton is now '
'fully booked</b> for <b>October 17 at Rogers Place</b>, headlined by <b>Joaquin Buckley vs Mike '
'Malott</b> at welterweight with <b>Erin Blanchfield vs Jasmine Jasudavicius</b> as the co-main. '
'<b>UFC Paris is Saturday</b>, with <b>Salahdine Parnasse &minus;550 over Dan Hooker +400</b>.'
'</span></div>')
h = h[:s] + NEW_TLDR + h[e:]

# --------------------------------------------- 2. Champions board: 18th check
canchor = '<h2 class="sec">Champions Board</h2>'
assert canchor in h
h = h.replace(
    canchor + '<p class="note"><span class="tag new">New &middot; 12:51 PM</span>',
    canchor + '@@CHAMPSLOT@@<p class="note"><span class="tag">Carried &middot; Aug 31, 12:51 PM</span>', 1)
assert '@@CHAMPSLOT@@' in h

CHAMP = (
'<p class="note"><span class="tag new">New &middot; 1:12 PM</span> '
'<b>Eighteenth cross-check, and the first complete one this page has ever recorded: every division was '
'returned and every division matched.</b> An ESPN-sourced sweep this run gave all eleven belts &mdash; '
'<b>Aspinall</b> (heavyweight, won June 21, 2025), <b>Ulberg</b> (light heavyweight, April 11, 2026), '
'<b>Strickland</b> (middleweight, May 9, 2026), <b>Makhachev</b> (welterweight, November 15, 2025), '
'<b>Gaethje</b> (lightweight, June 14, 2026), <b>Volkanovski</b> (featherweight, April 12, 2025), '
'<b>Yan</b> (bantamweight), <b>Van</b> (flyweight), <b>Harrison</b> (women&rsquo;s bantamweight), '
'<b>Shevchenko</b> (women&rsquo;s flyweight) and <b>Dern</b> (women&rsquo;s strawweight) &mdash; '
'<b>each matching this board</b>. The return also restates <b>Makhachev as a two-division champion who '
'vacated lightweight before taking welterweight</b>, which is the framing this page carries. '
'<b>Board unchanged &mdash; seventy-fifth consecutive edition.</b><br><br>'
'&#9888; <b>Why a complete return matters more than a clean one.</b> The last four checks each matched '
'six or seven cells and <b>never reached the women&rsquo;s divisions</b>, so <b>Harrison, Shevchenko '
'and Dern have been carried rather than re-verified for a week</b> &mdash; carried correctly, as it '
'turns out, but carried. <b>This is the first run in which no row on the board rests on a previous '
'edition.</b> The flyweight row in particular no longer depends on <b>UFC 331&rsquo;s billing of Van as '
'current champion and Pantoja as former</b>; that billing and this return now agree.<br><br>'
'&#9888; <b>One wording variant recorded, not adopted.</b> The return describes <b>Dern</b> as having '
'<b>won the vacant title in October 2025</b>, where this board carries the fuller '
'<b>unanimous decision over Virna Jandiroba at UFC 321 on October 25, 2025</b>. '
'<b>Those are compatible, not conflicting</b> &mdash; a shorter rendering of the same result &mdash; and '
'the board keeps the specific one. &#9888; <b>The return did not restate the interim heavyweight '
'situation</b>: <b>Gane holds the interim belt and Aspinall is undisputed</b>, which is the row this '
'page refused to let an ESPN-sourced return overwrite at 11:50, and <b>a return that simply omits it is '
'not evidence against it</b>.</p>')
h = h.replace('@@CHAMPSLOT@@', CHAMP, 1)

# --------------------------------------------------- 3. UFC Edmonton card
fanchor = '<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>'
assert fanchor in h
EDM = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:12 PM</span> '
'<b>UFC Edmonton is now a full card rather than a date, and it is the first October event on this '
'page.</b> <b>Saturday, October 17, 2026, Rogers Place, Edmonton, Alberta</b>. '
'<b>Main event: Joaquin Buckley vs Mike Malott at welterweight.</b> '
'<b>Co-main: Erin Blanchfield vs Jasmine Jasudavicius at women&rsquo;s flyweight.</b> '
'The remainder of the announced lineup, copied as listed: '
'<b>Louis Jourdain vs Timmy Cuamba</b> (135), <b>Mandel Nallo vs Nate Landwehr</b> (155), '
'<b>Jamey-Lyn Horth vs Katlyn Cerminara</b> (145), <b>Tanner Boser vs Jhonata Diniz</b> (265), '
'<b>Melissa Croden vs Chelsea Chandler</b> (135), <b>Marc-Andr&eacute; Barriault vs Kyle Daukaus</b> '
'(185), <b>Gilbert Urbina vs Julien Leblanc</b> (185) and <b>Chad Anheliger vs Steven Koslow</b> (135). '
'<b>Prelims 5 PM ET, main card 8 PM ET, Paramount+.</b><br><br>'
'&#9888; <b>This card is printed in full where UFC 331&rsquo;s was not, and the difference is name '
'rendering.</b> The UFC 331 listing refused at 12:24 mangled three names in its last four lines &mdash; '
'a wrong first name, a surname run together and an &ldquo;additional fighter&rdquo; where an opponent '
'should be. <b>This listing names two identifiable fighters on every line at a stated weight</b>, and '
'the <b>Anheliger&ndash;Koslow booking is independently corroborated</b> by a newly-booked-fights '
'tracker for the week ending August 30. &#9888; <b>No odds were returned for any Edmonton bout and none '
'is printed.</b></div>')
h = h.replace(fanchor, fanchor + EDM, 1)

assert len(h) > orig
io.open(P, 'w', encoding='utf-8').write(h)
print('mma-briefing.html %d -> %d bytes' % (orig, len(h)))
