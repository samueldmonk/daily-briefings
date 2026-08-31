#!/usr/bin/env python3
# Each index card must faithfully summarize its own page's verified lead for THIS run.
import os, re
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D,'index.html'); h = open(p,encoding='utf-8').read()

CY = ('<p><b>PaperCut now has vendor severity scores &mdash; and a second emergency patch.</b> '
 'The chain runs <b>CVE-2026-81578 (CVSS 8.8</b>, improper access control in the web management interface, letting an unauthenticated attacker change system configuration<b>)</b> into '
 '<b>CVE-2026-82078 (CVSS 9.4</b>, unsafe dynamic class loading in the database connection utilities &rarr; arbitrary Java execution<b>)</b>, both added to CISA&rsquo;s KEV catalog on '
 '<b>August 31</b> with remediation due <b>September 14</b>. <b>PaperCut has issued a second emergency patch after researchers broke the first fix</b>, so patching once is not enough &mdash; '
 'which matters because <b>CISA reports Medusa affiliates have breached 500+ organisations by targeting exactly the not-yet-patched</b>. Also new: a <b>$55,236,150 ransom demand</b> against McKesson, '
 'and confirmed third-party intrusions at <b>Air France and KLM</b>.</p>')
WS = ('<p><b>A fifth read confirms the close, and the afternoon&rsquo;s open discrepancy closed with it.</b> '
 '<b>S&amp;P 500 7,686.14 (&minus;0.33%)</b>, <b>Nasdaq Composite 26,370.89 (&minus;0.12%)</b>, <b>Dow 53,185.90 (&minus;374.09, &minus;0.70%)</b> after U.S. and Iranian forces exchanged fire for the first time in a month &mdash; '
 'and all three still <b>capped August with a gain</b>. A quoted <b>10-year day range of 4.697%&ndash;4.767% against a 4.722% close</b> proves the &ldquo;topped 4.75%&rdquo; print and the daily mark were one path. '
 '<b>Edison International fell 23% to $54.22, its largest single-day drop in more than 25 years</b>, after California lawmakers blocked the Newsom wildfire-liability plan.</p>')
MM = ('<p><b>UFC.com settles the Paris card count, and it matches neither figure this page carried.</b> '
 'The promotion calls <b>UFC Fight Night: Hooker vs. Parnasse a 14-fight card</b> at the <b>Accor Arena on September 5</b> &mdash; against the 15 and 13 from secondary sources &mdash; '
 'with <b>prelims at noon ET and the main card at 3 PM ET on Paramount+</b>, and confirms <b>Saladhine Parnasse came through the Contender Series this year</b>. '
 'September fills in behind it: <b>Noche UFC: Silva vs. Delgado, September 12 in Glendale</b>, headed by <b>Grasso vs. Fiorot</b> and <b>Moreno vs. Morales</b>. '
 '<b>The champions board is unchanged for an eightieth straight edition.</b></p>')

def swap(h, cls, new):
    i = h.find('class="bigcard %s"' % cls)
    a = h.index('<p>', i); b = h.index('</p>', a)+4
    return h[:a] + new + h[b:]

h = swap(h,'c-cy',CY); h = swap(h,'c-ws',WS); h = swap(h,'c-mm',MM)
h = h.replace('<span id="updated">5:35 PM ET</span>','<span id="updated">6:05 PM ET</span>')
h = h.replace('Data as of 5:35 PM ET','Data as of 6:05 PM ET')
open(p,'w',encoding='utf-8').write(h)
print('index.html: three cards resynced to this run\'s verified leads')
