#!/usr/bin/env python3
# Read-through fixes, 2026-09-02 09:35 ET.
# PRINCIPAL DEFECT: "the previous edition" is a RELATIVE pointer. Each new edition
# silently re-points it, so a sentence true when written becomes false with nothing
# on the page changing. Same family as an expired novelty marker. All such pointers
# are converted to ABSOLUTE, timestamped edition references.
import sys

def edit(path, pairs):
    h = open(path, encoding='utf-8').read()
    for old, new in pairs:
        if old not in h:
            print('FAIL[%s]: anchor not found: %s' % (path, old[:80])); sys.exit(1)
        h = h.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(h)
    print('  %-26s %d fixes' % (path, len(pairs)))

# ------------------------------------------------------------------ WALL STREET
edit('wallstreet-briefing.html', [
 # superlative removed from the TL;DR: Dell's cross-session swing is larger than oil's turn
 ('and the day&rsquo;s sharpest reversal is in oil, which hit a one-month high overnight '
  'on U.S.&ndash;Iran strikes and then turned <b>lower</b> by the opening bell',
  'while oil, which hit a one-month high overnight on U.S.&ndash;Iran strikes, has turned '
  '<b>lower</b> by the opening bell'),
 # [0] was written by the 8:48 edition's successor about the 8:48 edition
 ('the previous edition of this page researched from 8:35 to 8:47 AM and did not carry it',
  'the <b>8:48 AM</b> edition of this page researched from 8:35 to 8:47 AM and did not carry it'),
 # [1] the faulty preview bullet belonged to the 8:48 edition
 ('The previous edition&rsquo;s On the Radar item previewed ADP as',
  'The <b>8:48 AM</b> edition&rsquo;s On the Radar item previewed ADP as'),
 # [2] both futures reads were printed by the 9:18 edition
 ('The previous edition printed both and adopted neither.',
  'The <b>9:18 AM</b> edition printed both and adopted neither.'),
 # unsourced precision: the source says only "shortly after the opening bell"
 ('a futures quote at 8 AM and an index move at 9:31 are different measurements',
  'a futures quote at 8 AM and an index move just after 9:30 are different measurements'),
 # the refusal was made by the 9:18 edition, not this one
 ('A futures quote board consulted this run returned',
  'A futures quote board consulted for the <b>9:18 AM</b> edition returned'),
 ('Two fetches of TheStreet&rsquo;s Sept 2 page minutes apart returned',
  'Two fetches of TheStreet&rsquo;s Sept 2 page minutes apart, made for the <b>9:18 AM</b> edition, returned'),
 # [3] tidy the tag rubric
 ('<b>&ldquo;New&rdquo; tags mark items absent from the previous edition</b> (the 9:18 AM snapshot)',
  '<b>&ldquo;New&rdquo; tags mark items absent from the 9:18 AM edition</b>'),
 # [4] two different editions wrote the two superlatives; "previous" named neither correctly
 ('The previous edition called Dell &ldquo;the day&rsquo;s worst megacap&rdquo; and this one '
  'drafted &ldquo;the day&rsquo;s worst large-cap&rdquo;',
  'The <b>8:19 AM</b> edition called Dell &ldquo;the day&rsquo;s worst megacap&rdquo; and the '
  '<b>8:48 AM</b> edition drafted &ldquo;the day&rsquo;s worst large-cap&rdquo;'),
])

# ------------------------------------------------------------------ MMA
edit('mma-briefing.html', [
 ('That finding was recorded in the previous edition and is carried',
  'That finding was recorded in the <b>8:48 AM</b> edition and is carried'),
 # my own new text: the refusal was made at 8:19 THIS MORNING, not yesterday
 ('<b>A refusal this page made yesterday is now resolved, and the way it was resolved is the point.</b> '
  'The previous edition declined to print UFC.com odds',
  '<b>A refusal this page made earlier this morning is now resolved, and the way it was resolved is '
  'the point.</b> The <b>8:19 AM</b> edition declined to print UFC.com odds'),
 ('The previous edition placed <b>Charriere vs. Lima on the main card',
  'The <b>9:18 AM</b> edition placed <b>Charriere vs. Lima on the main card'),
 ('It was first read primary in the previous edition and is re-confirmed here',
  'It was first read primary in the <b>8:19 AM</b> edition and is re-confirmed here'),
 ('a refusal first made in the previous edition and re-confirmed here',
  'a refusal first made in the <b>8:19 AM</b> edition and re-confirmed here'),
 ('the previous edition had prelims at 6 PM ET',
  'the <b>9:18 AM</b> edition had prelims at 6 PM ET'),
 ('<b>The venue gap this page flagged yesterday is closed:</b> the previous edition refused',
  '<b>The venue gap this page flagged earlier this morning is closed:</b> the <b>8:19 AM</b> edition refused'),
 ('A schedule listing fetched in the previous edition states the venue directly',
  'A schedule listing fetched for the <b>8:48 AM</b> edition states the venue directly'),
])

# ------------------------------------------------------------------ standing provenance note on all three
NOTE = ('<div class="note" style="border-left:3px solid var(--muted);padding-left:11px;margin-top:18px">'
        '<b>On dates and pointers.</b> This page is rebuilt every half hour and carries items forward. '
        'Where a carried sentence says &ldquo;this run,&rdquo; it means the edition that wrote it, not '
        'necessarily this one. <b>References to other editions are given by clock time rather than as '
        '&ldquo;the previous edition,&rdquo;</b> because a relative pointer re-points itself every time '
        'a new edition is published and turns a true sentence false without anything on the page changing.'
        '</div>\n')
for p in ('wallstreet-briefing.html', 'cyber-briefing.html', 'mma-briefing.html'):
    h = open(p, encoding='utf-8').read()
    if 'On dates and pointers' in h:
        continue
    i = h.find('<h2>Sources</h2>')
    if i < 0:
        print('FAIL: no Sources header in ' + p); sys.exit(1)
    h = h[:i] + NOTE + h[i:]
    open(p, 'w', encoding='utf-8').write(h)
    print('  %-26s provenance note added' % p)

print('OK read-through fixes applied')
