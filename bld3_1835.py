import sys
fails=[]
m=open('mma-briefing.html').read()
old_start='<div class="note"><b>Cross-check, this run.</b> ESPN'
i=m.find(old_start); j=m.find('</div>',i)
if i<0 or j<0: print("MISS note"); sys.exit(1)
new=('<div class="note"><b>Cross-check, this run.</b> ESPN&rsquo;s &ldquo;Current and all-time UFC champions&rdquo; '
 'page again returned nothing usable on direct fetch, so the search-level rendering was read. It is <b>partly repaired '
 'and still wrong in one place</b>. The division-shift logged in the previous edition has healed at both ends that '
 'caused it: <b>Alex Pereira</b> is no longer filed at light heavyweight, and <b>bantamweight is populated with Petr Yan</b> '
 'rather than the &ldquo;TBD&rdquo; cell that rendering produced. What survives is the top row: the page seats '
 '<b>Carlos Ulberg at heavyweight</b> on his 11 April 2026 win, which is the <i>light heavyweight</i> belt he took '
 'vacant at UFC 327 &mdash; so Ulberg appears twice and the heavyweight row hides the fact that the undisputed belt is '
 '<b>vacant</b> after Tom Aspinall relinquished it this morning. That row is refused. The seven men&rsquo;s rows the '
 'rendering does get right &mdash; light heavyweight (Ulberg, UFC 327), middleweight (Strickland, UFC 328), welterweight '
 '(Makhachev, UFC 322), lightweight (Gaethje, Freedom 250), featherweight (Volkanovski, UFC 314), bantamweight (Yan, UFC 323) '
 'and flyweight (Van, UFC 323) &mdash; match this board exactly. The women&rsquo;s divisions did not render in what was '
 'returned this run, so nothing was taken from the source for them and all three are carried from the most recent '
 'title-changing card. Every belt on this board is re-derived that way rather than copied from a list; a source that is '
 'wrong on one row can be right on ten others, and the reverse.</div>')
m=m[:i]+new+m[j+6:]
m=m.replace('ESPN &mdash; Current and all-time UFC champions (cross-checked 18:05 ET; four rows refused)',
            'ESPN &mdash; Current and all-time UFC champions (cross-checked 18:36 ET; heavyweight row refused)')
m=m.replace('ESPN &mdash; Current and all-time UFC champions (cross-check; three rows refused)',
            'ESPN &mdash; Current and all-time UFC champions (cross-check; one row refused)')
open('mma-briefing.html','w').write(m)
print("NOTE-1835 OK")
