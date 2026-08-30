#!/usr/bin/env python3
"""One job: the refusal ledger on the cyber page (Nevada count + the new Iran-linked refusal)."""
import io, sys
REPO = sys.argv[1]
f = REPO + '/cyber-briefing.html'
h = io.open(f, encoding='utf-8').read()
n = 0

def sub(h, old, new, label):
    global n
    assert h.count(old) == 1, ('ANCHOR %s: %d hits' % (label, h.count(old)))
    n += 1
    return h.replace(old, new)

OLD = ('<b>Nevada&rsquo;s statewide ransomware incident was refused on sight for a ninth consecutive run</b> '
       '&mdash; it is an <b>August 2025</b> event, and the &ldquo;2026 breaches&rdquo; listings that keep '
       'surfacing it are mis-shelving last year&rsquo;s incident.')
NEW = ('<b>Nevada&rsquo;s statewide ransomware incident was refused on sight for an eleventh consecutive run</b> '
       '&mdash; it returned again this run in the same listing genre, with the same <b>August 24</b> date and the '
       'same <b>60-plus agencies</b>, and it is an <b>August 2025</b> event settled against the State of '
       'Nevada&rsquo;s own after-action report. <b>The refusal is now automatic and the reasoning is recorded '
       'below rather than re-argued here.</b>'
       '<br><br>&#10007; <b>New at 6:10 PM &mdash; a first refusal, and this one is refused for being too big to '
       'take on one source.</b> A daily-briefing aggregator fetched this run states that <b>Iran-linked actors '
       'disabled a UK power plant for four days and struck wastewater systems across twelve U.S. states within the '
       'same 24-to-48-hour window</b>. <b>Nothing else fetched this run returns it</b> &mdash; no national CERT '
       'notice, no utility statement, no second outlet. &#9888; <b>The size of the claim is the reason for the '
       'refusal, not an argument against it.</b> A four-day outage at a national power station and a '
       'twelve-state water-sector campaign would be among the most consequential operational-technology attacks '
       'ever reported, and an event of that scale leaves a paper trail in places this page can check. Until one '
       'of those returns it, <b>it is not published here in any form</b> &mdash; not as a report, not as an '
       'allegation, not hedged. <b>It is listed only so that the decision is visible</b>, on the same principle '
       'as every other line in this ledger: a refusal that is never shown is indistinguishable from a search that '
       'found nothing.')

h = sub(h, OLD, NEW, 'nevada-count')
io.open(f, 'w', encoding='utf-8').write(h)
print('refusal edits:', n)
