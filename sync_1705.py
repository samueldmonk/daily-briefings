#!/usr/bin/env python3
"""Sync the three summary strips and the index cards to THIS run's verified leads."""
import re, sys, io, os
REPO = sys.argv[1]
rd = lambda f: io.open(os.path.join(REPO, f), encoding="utf-8").read()
wr = lambda f, s: io.open(os.path.join(REPO, f), "w", encoding="utf-8").write(s)

# ---- CYBER tldr ----
cy = rd("cyber-briefing.html")
new_cy = ('<div class="tldr"><b>The Wire</b> <span>The <b>PaperCut NG/MF</b> chain now has both a federal '
 'deadline and a post-exploitation profile: <b>CISA added CVE-2026-82078 (CVSS 9.4) and CVE-2026-81578 '
 'to the Known Exploited Vulnerabilities catalog on August 31 with a September 14 remediation date</b>, '
 'while attackers on compromised servers are installing <b>SimpleHelp and AnyDesk for redundant remote '
 'access</b> &mdash; and with <b>PaperCut’s first emergency patch already bypassed and 47% of tracked '
 'installations still vulnerable</b>, patching once is not enough.</span></div>')
cy = re.sub(r'<div class="tldr"><b>The Wire</b>.*?</div>', new_cy, cy, count=1, flags=re.S)
wr("cyber-briefing.html", cy)

# ---- MMA tldr ----
mm = rd("mma-briefing.html")
new_mm = ('<div class="tldr"><b>Tale of the Tape</b> <span>Paris has a current quote at last &mdash; '
 '<b>Parnasse &minus;600 / Hooker +430</b>, inside the &minus;500-to-&minus;700 range this page has been '
 'publishing and the widest consensus-side number yet on a one-way drift toward the debutant &mdash; '
 'and a report fetched this run states plainly that <b>Sean Strickland is once again the middleweight '
 'champion</b>, with a first defense targeted for December against either Chimaev or Imavov, which '
 'settles the belt an aggregator got wrong again today.</span></div>')
mm = re.sub(r'<div class="tldr"><b>Tale of the Tape</b>.*?</div>', new_mm, mm, count=1, flags=re.S)
wr("mma-briefing.html", mm)

# ---- INDEX: restamp + resync the three cards ----
ix = rd("index.html")
ix = ix.replace('<span id="updated">4:55 PM ET</span>', '<span id="updated">5:05 PM ET</span>')

cards = {
 "c-cy": ('<p><b>The PaperCut chain now has a deadline and a playbook.</b> <b>CISA added '
   '<b>CVE-2026-82078</b> (<b>CVSS 9.4</b>, unsafe reflection) and <b>CVE-2026-81578</b> '
   '(missing authentication) to the Known Exploited Vulnerabilities catalog on <b>August 31</b>, '
   'remediation due <b>September 14</b>.</b> On compromised servers attackers are installing '
   '<b>SimpleHelp</b> with auto-start and <b>AnyDesk</b> as a redundant channel; <b>PaperCut’s first '
   'emergency patch has already been bypassed and replaced</b>, and <b>47% of tracked installations '
   'remain vulnerable</b>. Elsewhere: <b>McKesson</b> confirms a breach after <b>ShinyHunters</b> claims '
   '284 million records and a <b>$55,236,150</b> demand, reached by <b>phone calls to employees</b>, '
   'not a flaw.</p>'),
 "c-ws": ('<p><b>The close is final and August still finished green.</b> The <b>S&amp;P 500 ended at '
   '7,686.14, &minus;0.33%</b>; the <b>Nasdaq Composite at 26,370.89, &minus;0.12%</b>; the <b>Dow at '
   '53,185.90, down 374.09 points or 0.7%</b> &mdash; <b>yet all three closed out the month higher</b>. '
   '<b>U.S. forces struck Iranian rocket launchers in the Strait of Hormuz</b>, <b>WTI settled +2.83% at '
   '$85.76</b> and <b>Brent +2.71% at $90.49</b>, and <b>energy was the only sector to finish up</b>. '
   '<b>Tesla rose about 3.7% on Optimus entering production at Fremont</b> and <b>Ulta about 4%</b>, '
   'while <b>Edison International (&minus;22.3%) and PG&amp;E (&minus;19.4%) cratered</b> after '
   'California lawmakers failed to pass a wildfire-liability cap.</p>'),
 "c-mm": ('<p><b>Paris finally has a current price.</b> <b>Parnasse &minus;600 / Hooker +430</b> on a '
   '15-fight card at the Accor Arena &mdash; inside the <b>&minus;500-to-&minus;700</b> range already '
   'published, and the widest consensus-side number yet on a market drifting one way toward the '
   'debutant. And the middleweight question closes: a report fetched this run says <b>Sean Strickland '
   'is once again the champion</b>, with a first defense targeted for <b>December</b> against either '
   '<b>Chimaev</b> or <b>Imavov</b> &mdash; a man cannot be booked to challenge for a belt he holds.</p>'),
}
for cls, html in cards.items():
    pat = re.compile(r'(<div class="bigcard ' + cls + r'">.*?)<p>.*?</p>', re.S)
    assert pat.search(ix), cls
    ix = pat.sub(lambda m: m.group(1) + html, ix, count=1)
wr("index.html", ix)
print("sync_1705 applied")
