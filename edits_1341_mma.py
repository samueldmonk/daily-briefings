#!/usr/bin/env python3
"""MMA content edits, 1:41 PM ET edition, Aug 31 2026."""
import io, re
p = 'mma-briefing.html'
h = io.open(p, encoding='utf-8').read()

h = h.replace('<span class="tag new">New &middot; 1:12 PM</span>',
              '<span class="tag">Carried &middot; Aug 31, 1:12 PM</span>')

# ------------------------------------------------ Fight Week
FW = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>The September 26 card gets a name, a venue and three bouts, which closes the gap this page has flagged since '
'Sunday.</b> A newly-booked-fights tracker for the <b>week ending August 30</b> lists the event as the '
'<b>TUF 34 Bantamweight Finale</b> on <b>September 26 at the Meta APEX</b>, and names '
'<b>Mehemmedeli Osmanli vs Ilimbek Akylbek Uulu</b> (bantamweight), <b>Rodolfo Vieira vs Robert Bryczek</b> '
'(middleweight) and <b>Brady Hiestand vs Rinya Nakamura</b> (bantamweight). '
'&#9888; <b>This is a corroborating source, not a reconciliation.</b> The three competing event names this page has '
'kept apart for September 26 are still not equated by anything fetched; what has changed is that <b>one rendering '
'now has a stated venue and three verifiable bouts attached to it</b>. <b>The names stay separate until a source '
'equates them.</b><br><br>'
'<b>Also newly booked, and the first November date on this page:</b> <b>Jonny Parsons opposite Jos&eacute; Souza</b> '
'on the <b>November 7 Meta APEX card</b>. &#9888; <b>Reported as a booking; no weight class returned and none is '
'assigned.</b> The same tracker states <b>six new bouts across three cards</b> this week and confirms '
'<b>Chad Anheliger vs Steven Koslow on October 17 at UFC Edmonton</b>, which is the corroboration this page cited '
'when it printed the Edmonton card in full.<br><br>'
'&#9888; <b>Paris odds refreshed, and for the first time this session nothing lands outside the band already '
'carried.</b> Two more renderings for <b>September 5, Accor Arena</b>: <b>BetWay at Parnasse &minus;400 / Hooker '
'+300</b>, and a <b>consensus line at Parnasse &minus;428 / Hooker +292</b>. '
'<b>Both sit inside the carried range of Parnasse &minus;400 to &minus;550 and Hooker +292 to +400</b>; '
'<b>the range is unchanged and no figure is adopted as the line.</b> The same return again describes Parnasse as a '
'<b>two-time KSW featherweight and one-time KSW lightweight champion</b>, and Hooker as a <b>perennial lightweight '
'contender</b> &mdash; <b>contender, not challenger</b>, and this page prints it as given.</div>'
)
a1 = 'Fight Week &mdash; Upcoming Cards</h2>'
assert a1 in h
h = h.replace(a1, a1 + FW, 1)

# ------------------------------------------------ Champions Board
CH = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>Nineteenth cross-check: six men&rsquo;s divisions returned from ESPN, six matched, and the detail lines matched '
'too.</b> An ESPN-sourced sweep this run restates <b>Tom Aspinall</b> at heavyweight (won June 21, 2025, inherited '
'on Jon Jones&rsquo;s retirement, <b>0 defenses</b>), <b>Carlos Ulberg</b> at light heavyweight (<b>KO1 over Ji&rcaron;&iacute; '
'Proch&aacute;zka at UFC 327, April 11, 2026</b>, 0 defenses), <b>Sean Strickland</b> at middleweight '
'(<b>split decision over Khamzat Chimaev at UFC 328, May 9, 2026</b>, 0 defenses), <b>Islam Makhachev</b> at '
'welterweight (<b>UD over Jack Della Maddalena at UFC 322, November 15, 2025</b>, <b>1 defense</b>), '
'<b>Justin Gaethje</b> at lightweight (<b>TKO4 over Ilia Topuria at UFC Freedom 250, June 14, 2026</b>, 0 defenses) '
'and <b>Alexander Volkanovski</b> at featherweight (<b>UD over Diego Lopes at UFC 314, April 12, 2025</b>, '
'<b>1 defense</b>). <b>Every cell on the board below is unchanged &mdash; the seventy-sixth consecutive edition.</b>'
'<br><br>'
'&#9888; <b>The four women&rsquo;s divisions, bantamweight and flyweight did not return in this sweep, and that is '
'recorded rather than treated as doubt.</b> The return states only that the ESPN page carries four women&rsquo;s '
'weight classes without naming their holders. <b>The 1:12 PM sweep reached all eleven divisions and matched all '
'eleven</b>; <b>an omission from a later search is not evidence against a row</b>, which is the distinction this '
'page drew when a genuine conflation was caught at 11:50. <b>Harrison, Shevchenko, Dern, Yan and Van stand on the '
'earlier verification.</b></div>'
)
a2 = 'Champions Board</h2>'
assert a2 in h
h = h.replace(a2, a2 + CH, 1)

# ------------------------------------------------ TLDR
new_tldr = (
'<div class="tldr"><b>Tale of the Tape</b> <span>The September 26 card finally has a venue and three bouts attached '
'to it &mdash; the <b>TUF 34 Bantamweight Finale</b> at the <b>Meta APEX</b>, headed by '
'<b>Osmanli&ndash;Akylbek Uulu</b>, <b>Vieira&ndash;Bryczek</b> and <b>Hiestand&ndash;Nakamura</b> &mdash; while a '
'nineteenth champions cross-check returned six men&rsquo;s divisions from ESPN and matched all six, leaving the '
'board unchanged for a seventy-sixth consecutive edition.</span></div>'
)
h = re.sub(r'<div class="tldr">.*?</div>\s*(?=<div class="freshline")', new_tldr, h, count=1, flags=re.S)
assert 'TUF 34 Bantamweight Finale</b> at the' in h, 'tldr not replaced'

io.open(p, 'w', encoding='utf-8').write(h)
print('mma edits applied,', len(h), 'bytes')
