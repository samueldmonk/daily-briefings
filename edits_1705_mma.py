# -*- coding: utf-8 -*-
import sys
def rep(t, old, new, label):
    if old not in t: sys.exit("MISS: " + label)
    if t.count(old) != 1: sys.exit("NOT UNIQUE (%d): %s" % (t.count(old), label))
    return t.replace(old, new)

m = open('mma-briefing.html').read()

m = rep(m, '<b>sixth consecutive edition</b> in which the two have failed to converge',
           '<b>eighth consecutive edition</b> in which the two have failed to converge', 'refusal count')

m = rep(m, 'byte-for-byte the timestamp recorded three runs ago, so the promotion has not revised it.',
           'byte-for-byte identical across five consecutive runs now, so the promotion has not revised it.', 'modified_time count')

m = rep(m,
 '<b>Charles Jourdain vs. Marlon Vera</b>, and Gable Steveson. Thirteen fights.',
 '<b>Charles Jourdain vs. Marlon Vera</b>, <b>Alonzo Menifield vs. Iwo Baraniewski</b> and Gable Steveson. Thirteen fights. The card is the promotion&rsquo;s <b>sixth visit to Los Angeles</b> and its <b>first since UFC 227 in August 2018</b>.',
 'UFC331 card')

m = rep(m,
 '<b>Gate and attendance, from UFC.com.</b>',
 '<b>Gate and attendance, from UFC.com &mdash; re-fetched directly this run.</b> The promotion&rsquo;s own bonus page was pulled again this edition and every figure below matched what this page already carried, as did all four Performance of the Night names and the absence of a Fight of the Night award.',
 'gate refetch')

open('mma-briefing.html','w').write(m)
print("MMA edits applied OK")
