#!/usr/bin/env python3
"""One job: record THIS run's champions cross-check in the body of the Champions Board.

The summary strip says twelfth cross-check / sixty-ninth edition. The body's most recent
champions note still read "sixty-third consecutive edition" from an earlier run, so the strip
and the section it summarises disagreed on the count. The older paragraphs are a running log and
are left standing as the dated entries they are; this run's result is added above them and says
plainly that it supersedes the counts recorded beneath.
"""
import io, sys
REPO = sys.argv[1]
p = REPO + '/mma-briefing.html'
h = io.open(p, encoding='utf-8').read()

OLD = 'Champions Board</h2><div class="note" style="margin-bottom:12px">'
NEW = ('Champions Board</h2><div class="note" style="margin-bottom:12px">'
       '<span class="tag new">New &middot; 6:10 PM</span> <b>Twelfth consecutive cross-check '
       'against ESPN, and the widest return yet.</b> ESPN&rsquo;s &ldquo;Current and all-time UFC '
       'champions&rdquo; came back this run with <b>eight</b> of this board&rsquo;s eleven cells '
       '&mdash; <b>Aspinall</b> (heavyweight, inherited June 21 2025), <b>Ulberg</b> (light '
       'heavyweight, KO1 Proch&aacute;zka, UFC 327, April 11 2026), <b>Strickland</b> '
       '(middleweight, split decision over Chimaev, UFC 328, May 9 2026), <b>Makhachev</b> '
       '(welterweight, UD over Della Maddalena, UFC 322, November 15 2025), <b>Gaethje</b> '
       '(lightweight, TKO4 Topuria, Freedom 250, June 14 2026), <b>Volkanovski</b> (featherweight, '
       'UD over Lopes, UFC 314, April 12 2025), <b>Petr Yan</b> (bantamweight, UD over '
       'Dvalishvili, UFC 323, December 6 2025) and <b>Joshua Van</b> (flyweight, TKO1 Pantoja, '
       'UFC 323, December 6 2025). <b>Title dates and defence counts both matched</b> what this '
       'board carries, including the two counts this page has had to defend before &mdash; '
       'Makhachev at <b>one</b> defence and Van at <b>one</b>. <b>The board is unchanged for a '
       'sixty-ninth consecutive edition.</b> &#9888; <b>The previous check reached six cells; this '
       'one reached eight</b>, so the two men&rsquo;s divisions that had been resting on this '
       'page&rsquo;s own records &mdash; bantamweight and flyweight &mdash; now have the same '
       'external confirmation as the other six. <b>The remaining three are the women&rsquo;s '
       'belts</b>, which this return did not cover and which continue to rest on the checks '
       'recorded below. &#9888; <b>The edition and cross-check counts in the older paragraphs in '
       'this section are the counts as they stood when those paragraphs were written; this note '
       'carries the current ones.</b></div>'
       '<div class="note" style="margin-bottom:12px">')

assert h.count(OLD) == 1
io.open(p, 'w', encoding='utf-8').write(h.replace(OLD, NEW))
print('champions note added')
