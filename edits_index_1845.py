#!/usr/bin/env python3
import re, sys, io
REPO = sys.argv[1]
p = REPO + '/index.html'
h = io.open(p, encoding='utf-8').read()

NOTE = ('Each card above carries that briefing\'s own summary line, unchanged. Briefings refresh every 30 minutes '
        'between 8 AM and 6 PM ET; point-in-time snapshots of every edition are kept in the '
        '<a href="archive.html">Archive</a>. Weekend note: U.S. equity markets are closed today, so the markets '
        'briefing carries Friday\'s official closes and says so &mdash; though this edition&rsquo;s lead is the first '
        'item all weekend that postdates them.')
h = re.sub(r'(<div class="note" style="margin-top:22px">).*?(</div>)',
           lambda m: m.group(1) + NOTE + m.group(2), h, count=1, flags=re.S)

CHANGED = (
 '<b>Three things changed at 6:45 PM, and the first two are corrections this project made against itself.</b> '
 'The security briefing found that its own lead extortion listing was wrong three ways at once: the company is '
 '<b>Questel SAS</b> and not &ldquo;Questal&rdquo;, the listing is <b>dated August 2</b> and not fresh, and the company '
 '<b>has now confirmed</b> a Microsoft 365 intrusion via voice phishing &mdash; while still <b>not</b> confirming the '
 'attacker&rsquo;s &ldquo;Salesforce records&rdquo; characterisation, which it describes as a <b>Sales SharePoint</b> '
 'environment. The MMA briefing ran its thirteenth champions cross-check and, for the first time, the cross-check source '
 'came back <b>current in six cells and stale in two</b> &mdash; refuted inside the same run by the promotion&rsquo;s own '
 'language, so the board did not move and the rule tightened to <b>per cell, not per return</b>. The markets briefing '
 'carries the weekend&rsquo;s first genuinely new event: a <b>U.S. strike on Iranian rocket launchers near the Strait of '
 'Hormuz</b> and <b>crude up 2% at the open</b>, with the oil <i>level</i> deliberately not recomputed and Dow '
 '<i>futures</i> deliberately kept out of the table of official closes.<br><br>'
)
h = re.sub(r'(<div class="srcs"><br><br>)', lambda m: m.group(1) + CHANGED, h, count=1)
io.open(p, 'w', encoding='utf-8').write(h)
print('index note + changed-block updated')
