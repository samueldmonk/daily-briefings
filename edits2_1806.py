#!/usr/bin/env python3
# Sync index.html card summaries to the 6:06 leads. Deferred write.
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
h = open(os.path.join(D, 'index.html')).read()
fails = []

def sub(old, new, label):
    global h
    if h.count(old) != 1:
        fails.append('%s: %d occurrences' % (label, h.count(old)))
        return
    h = h.replace(old, new, 1)

sub('<p><b>NVIDIA shipped four advisories &mdash; one covering 18 flaws in its AI-agent runtime products, two of '
    'them critical &mdash; and Adobe seven.</b> <b>Nutex Health has told the SEC that data was exfiltrated</b> and '
    '<b>ReliaQuest has confirmed a ShinyHunters intrusion.</b> KEV is unchanged; <b>Oracle CVE-2026-21962 is due '
    'tomorrow.</b></p>',
    '<p><b>Apollo Global Management says a social-engineering intrusion reached its cloud platforms between '
    'July&nbsp;6 and July&nbsp;10 and exposed names, dates of birth, addresses and Social Security numbers</b> '
    '&mdash; no count disclosed, no client funds taken. <b>A CVSS 9.1 Keycloak password-reset takeover</b> and an '
    '<b>NVIDIA NemoClaw model-poisoning flaw with no CVE and no Windows fix</b> join the board; KEV is static and '
    '<b>Oracle CVE-2026-21962 is due tomorrow.</b></p>', 'cyber card')

sub('<p>A full after-hours roundup prices the night at <b>Okta &plus;17%, Salesforce &plus;12%, CrowdStrike '
    '&plus;10%, Nutanix &plus;5%, Nvidia &minus;1%, Synopsys &minus;6% and HP Inc &minus;11%</b> &mdash; giving '
    'Nvidia its <b>first sourced magnitude</b> after a beat-and-raise the tape sold anyway, and making <b>HP, not '
    'Nvidia, the night&rsquo;s worst punishment</b>.</p>',
    '<p>Nvidia&rsquo;s extended-hours decline <b>reversed while CFO Colette Kress was speaking</b> &mdash; the stock '
    'was <b>up almost 5% at ~5:10&nbsp;p.m. ET</b> after she put the <b>backlog above $2&nbsp;trillion</b> and '
    'forecast <b>70% fiscal-2028 revenue growth on a supply-constrained basis</b>. The <b>&minus;1% and '
    '&minus;1.3% reads taken before the call are kept, not corrected away</b>, and <b>HP Inc &minus;11%</b> is '
    'still the night&rsquo;s worst move.</p>', 'markets card')

sub('<p>UFC Shanghai is set for <b>Saturday at the Oriental Sports Center</b> &mdash; <b>13 bouts</b> topped by '
    '<b>Umar Nurmagomedov vs. Song Yadong</b> at bantamweight, with the winner the clubhouse leader for the next '
    'title shot, and U.S. viewers watching from <b>3&nbsp;a.m. ET</b>.</p>',
    '<p><b>Gregory Rodrigues climbs three places to #7 at middleweight</b> and <b>Anthony Hernandez drops two to '
    '#9</b>; <b>Vitor Petrino rises to #8 at heavyweight</b> as <b>Serghei Spivac falls to #13</b>; and <b>Reinier '
    'de Ridder, Jamall Emmers (#14) and Carli Judice (#15)</b> all enter a top&nbsp;15 for the first time. '
    '<b>UFC Shanghai is Saturday</b>; the <b>champions board is unchanged.</b></p>', 'mma card')

if fails:
    print('FAILED — NOTHING WRITTEN')
    for f in fails:
        print('  ' + f)
    sys.exit(1)
open(os.path.join(D, 'index.html'), 'w').write(h)
print('OK — index.html synced')
