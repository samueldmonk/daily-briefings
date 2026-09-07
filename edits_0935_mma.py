#!/usr/bin/env python3
import io, sys
F = 'mma-briefing.html'

def edit(tell, old, new, label):
    h = io.open(F, encoding='utf-8').read()
    if tell in h:
        print('skip (already applied):', label); return
    if old not in h:
        print('MISS ANCHOR:', label); sys.exit(1)
    if h.count(old) != 1:
        print('AMBIGUOUS ANCHOR (%d matches):' % h.count(old), label); sys.exit(1)
    h = h.replace(old, new, 1)
    io.open(F, 'w', encoding='utf-8').write(h)
    h2 = io.open(F, encoding='utf-8').read()
    assert tell in h2 and h2.count(tell) == 1, 'edit failed/duplicated: ' + label
    print('ok:', label)

# ---- M1: describe THIS run's champions verification, not a previous run's
edit('This run&rsquo;s ESPN-sourced return got that label right too',
     'This run&rsquo;s return got that label right.',
     'This run&rsquo;s ESPN-sourced return got that label right too, and went further than most: it enumerated '
     '<b>all eleven undisputed belts</b> &mdash; every division except interim heavyweight &mdash; with a winning '
     'date, method, opponent, event and defence count against each, and <b>every one matched what this table already '
     'carried</b>. Aspinall 21 Jun 2025; Ulberg KO1 Proch&aacute;zka, UFC 327, 11 Apr 2026; Strickland SD Chimaev, '
     'UFC 328, 9 May 2026; Makhachev UD Della Maddalena, UFC 322, 15 Nov 2025, one defence; Gaethje TKO4 Topuria, '
     'UFC Freedom 250, 14 Jun 2026; Volkanovski UD Lopes, UFC 314, 12 Apr 2025, one defence; Yan UD Dvalishvili, '
     'UFC 323, 6 Dec 2025; Van TKO1 Pantoja, UFC 323, 6 Dec 2025; Harrison Sub2 Pe&ntilde;a, UFC 316, 7 Jun 2025, '
     'zero defences; Dern UD Jandiroba, UFC 321, 25 Oct 2025. <b>Pereira, Chimaev, Topuria, Pantoja and Dvalishvili '
     'appear in that return only as the men who lost the belts</b> &mdash; the four regressions this board exists to '
     'prevent are absent from a primary source, not merely absent from this page.',
     'M1 champions verification rewritten to describe this run\'s ESPN return')

# ---- M2: Shevchenko row upgraded from carried to verified
edit('UD Alexa Grasso, UFC 306, 14 Sep 2024; <b>2 defences</b>',
     '<tr><td>Women&rsquo;s Flyweight</td><td><b>Valentina Shevchenko</b></td><td class="mut">Carried, not re-confirmed this run.</td></tr>',
     '<tr><td>Women&rsquo;s Flyweight</td><td><b>Valentina Shevchenko</b></td><td class="mut">UD Alexa Grasso, '
     'UFC 306, 14 Sep 2024; <b>2 defences</b> &mdash; <b>no longer carried.</b> This row had read &ldquo;carried, not '
     're-confirmed&rdquo; for several editions because the champion&rsquo;s name kept appearing without the detail '
     'behind it; the ESPN-sourced return this run supplies the date, method, opponent, event and defence count, so '
     'the row is now verified on the same footing as the rest of the table.</td></tr>',
     'M2 Shevchenko row verified')

# ---- M3: how the Paris finish happened, plus the callout
edit('a clean kick to the liver and hard left hands',
     'stopped <b>Dan Hooker</b> inside a ',
     'stopped <b>Dan Hooker</b> &mdash; newly sourced this run, with <b>a clean kick to the liver and hard left hands</b>, '
     'after which Yahoo Sports reports he <b>called out Max Holloway</b> &mdash; inside a ',
     'M3 finish mechanics + Holloway callout')

# ---- M4: the ranking-number conflict, asserted as a conflict
edit('Two returns this run disagree on where Hooker was ranked',
     '<h2 class="sec">Prospect Watch</h2>',
     '<p class="note" style="margin:-2px 0 14px"><b>One number about that fight is not printed, and the reason is '
     'worth stating.</b> Two returns this run disagree on where Hooker was ranked going in &mdash; one describes him '
     'as the <b>No. 10-ranked</b> lightweight, another as <b>No. 12 at 155 pounds heading into the fight</b>. Both are '
     'reputable, neither cites a dated board, and a beaten opponent&rsquo;s ranking is exactly the kind of detail that '
     'inflates a debut when it is guessed upward. <b>No ranking is asserted for Hooker.</b> Nor is any post-Paris '
     'rankings movement: the algorithmic board is updated the Monday after each event, which makes today the scheduled '
     'update, but a return this run describes Parnasse only as &ldquo;an instant contender at 155 pounds&rdquo; and '
     'attaches no number to him. The mechanism is sourced; the outcome is not asserted ahead of it.</p>\n'
     '<h2 class="sec">Prospect Watch</h2>',
     'M4 Hooker ranking conflict printed, neither asserted')

print('--- mma edits done ---')
