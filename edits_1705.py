#!/usr/bin/env python3
"""Targeted edits onto the 4:55 PM pages -> 5:05 PM Afternoon Edition (post-close).
Every inserted fact was fetched THIS run (2026-08-31 ~17:05-17:12 ET)."""
import re, sys, io, os

REPO = sys.argv[1]
NOW = "5:05 PM"

def rd(f):
    return io.open(os.path.join(REPO, f), encoding="utf-8").read()

def wr(f, s):
    io.open(os.path.join(REPO, f), "w", encoding="utf-8").write(s)

def demote(s, stamp="4:55 PM"):
    """Sweep on the MARKER TEXT, never on the tag variant (defect class logged 4:55)."""
    pat = re.compile(r'<span class="tag[^"]*">New &middot; ' + re.escape(stamp) + r'</span>')
    return pat.sub('<span class="tag">Carried &middot; Aug 31, ' + stamp + '</span>', s)

def restamp(s):
    s = s.replace("Data as of 4:55 PM ET", "Data as of %s ET" % NOW)
    return s

NEW = lambda: '<span class="tag new">New &middot; %s</span>' % NOW

# ---------------------------------------------------------------- WALL STREET
ws = rd("wallstreet-briefing.html")
ws = demote(ws); ws = restamp(ws)

# 1) TLDR: add the month-end fact, verified this run (CNBC/Yahoo).
old_tl_tail = "&mdash; and the arithmetic of that close is what finally explains the wrap this page refused six times.</span></div>"
new_tl_tail = ("&mdash; and yet all three still <b>closed out August with a monthly gain</b>.</span></div>")
assert old_tl_tail in ws
ws = ws.replace(old_tl_tail, new_tl_tail, 1)

# 2) Movers: new block at the head of the section.
anchor = 'Movers &amp; Drivers</h2>'
assert anchor in ws
block = (anchor + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>Two winners finally have names and numbers, and the utilities rout tightens to a pair of '
  'closing percentages.</b> <b>Tesla rose about 3.7% after confirmation that its Optimus humanoid robot '
  'entered the production phase at the Fremont, California facility</b>, and <b>Ulta Beauty rose roughly '
  '4%</b> &mdash; the two clearest gainers named in reporting fetched this run, and the first time this '
  'page has carried either. &#9888; <b>A per-symbol read fetched alongside it prices Tesla at +3.41% '
  'rather than 3.7%</b>; both are printed because neither source is a screener and the gap is a '
  'rounding-window difference, not a contradiction.<br><br><b>On the losing side the close now reads '
  '<b>Edison International &minus;22.3%</b> and <b>PG&amp;E &minus;19.4%</b></b>, attributed to a '
  'sector wrap fetched this run, with a per-symbol read putting <b>PCG at &minus;19.13%</b>. '
  '&#9888; <b>This page has now carried five distinct figures for each name across the session '
  '(EIX &minus;21.0 / &minus;22.3 / &minus;23 / &minus;24; PCG &minus;16.7 / &minus;18 / &minus;19.13 / '
  '&minus;19.4 / &minus;20.0)</b> &mdash; they are the same rout read at different moments and by '
  'different vendors, and the closing pair above is the one this block leads with. <b>The cause is '
  'restated more plainly by this run’s sources than by earlier ones: California lawmakers '
  '<i>failed to pass</i> the reform that would have capped what individuals could recover from '
  'utilities whose equipment ignited wildfires, and several Wall Street analysts downgraded both '
  'names after the vote.</b></div>')
ws = ws.replace(anchor, block, 1)

# 3) After-hours: the screen refreshed; new names, same deliberate degradation.
ah = 'After-Hours Movers</h2>'
assert ah in ws
ah_block = (ah + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>The screen refreshed and returned a different set of microcaps, which is itself the finding.</b> '
  'An after-hours movers screen fetched this run names <b>Wetour Robotics (WETO)</b> and '
  '<b>Cango Inc. (CANG)</b> among gainers and <b>Zentek (ZTEK)</b> and '
  '<b>Jupiter Neurosciences (JUNS)</b> among decliners. &#9888; <b>Only ZTEK and JUNS survive from the '
  '4:55 PM screen; the gainers turned over completely inside ten minutes, and no percentage was stated '
  'for any of the four in what was fetched.</b> <b>No catalyst is attached to any of them and no '
  'percentages are printed for them here.</b> That churn is the reason this section stays degraded: it '
  'is a snapshot of a screen, not market news, and <b>no S&amp;P 500 company has a sourced post-close '
  'move this run either.</b></div>')
ws = ws.replace(ah, ah_block, 1)

# 4) Rates/commodities reconciliation note appended after the section heading.
rates = 'Rates, Bonds &amp; Commodities</h2>'
if rates in ws:
    rblock = (rates + '<div class="note" style="margin-bottom:14px">' + NEW() +
      ' <b>Two independent marks land on the same day and neither overturns the settles below.</b> '
      'A rates read fetched this run has the <b>10-year Treasury yield holding at 4.72% on August 31</b>, '
      'against the <b>intraday print above 4.75% &mdash; the highest since January 2025</b> already '
      'carried; <b>a yield that tops 4.75% intraday and is marked at 4.72% on the day is one path, not '
      'two claims.</b> On crude, a commodities read marks <b>WTI at $85.54, +2.57%</b> and '
      '<b>Brent at $90.69, +2.93%</b> for August 31, against the <b>settles of $85.76 (+2.83%) and '
      '$90.49 (+2.71%)</b> this page leads with. &#9888; <b>Settlement prices win over live marks here '
      'and the marks are printed only to show the spread is sub-1%.</b> The same read puts crude '
      '<b>+6.48% over the past month</b> and Brent <b>+8.26%</b>, which is the fuller version of the '
      'energy-led August this page has been describing.</div>')
    ws = ws.replace(rates, rblock, 1)

wr("wallstreet-briefing.html", ws)

# ---------------------------------------------------------------------- CYBER
cy = rd("cyber-briefing.html")
cy = demote(cy); cy = restamp(cy)

top = re.search(r'(Top Story</h2>)', cy)
assert top, "cyber top story anchor missing"
cblock = (top.group(1) + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>The post-exploitation picture filled in, and it is remote-access tooling rather than ransomware.</b> '
  '<b>On compromised PaperCut servers attackers downloaded a malicious payload, silently installed and '
  'ran SimpleHelp remote access software with auto-start enabled, then pulled down AnyDesk as a second, '
  'redundant channel</b> (Help Net Security, August 31). <b>Huntress observed the activity in two customer '
  'environments, with Base64-encoded commands run first to enumerate the user account and operating '
  'system</b> &mdash; limited, hands-on, and aimed at persistence. &#9888; <b>Two facts make the '
  'September 14 federal deadline the floor rather than the ceiling of the problem:</b> <b>PaperCut has '
  'now shipped a SECOND emergency patch after researchers found multiple ways around the first fix</b>, '
  'and <b>47% of tracked PaperCut installations were still running versions vulnerable to remote code '
  'execution</b>. <b>Patching once is not sufficient here; the first patch is known-bypassable.</b> '
  'The vendor’s own guidance from August 27 &mdash; <b>restrict web access to trusted IP addresses '
  'immediately</b> &mdash; still stands as the compensating control.</div>')
cy = cy.replace(top.group(1), cblock, 1)

# KEV countdown sanity: Aug 31 -> Sep 14 = 14 days.
cy = cy.replace("(15 days left)", "(14 days left)")
wr("cyber-briefing.html", cy)

# ------------------------------------------------------------------------ MMA
mm = rd("mma-briefing.html")
mm = demote(mm); mm = restamp(mm)

ts = re.search(r'(Top Story</h2>)', mm)
assert ts, "mma top story anchor missing"
mblock = (ts.group(1) + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>The Paris line has a current quote again, and it sits inside the range this page published rather '
  'than replacing it.</b> A card listing fetched this run prices the September 5 main event at '
  '<b>Salahdine Parnasse &minus;600 / Dan Hooker +430</b> and describes the pair as <b>current</b>, '
  'while noting books elsewhere sit near <b>&minus;599 / +400</b>. &#9888; <b>Both fall within the '
  '&minus;500-to-&minus;700 and +360-to-+450 spread already established, so this is a point on the '
  'same one-way drift toward the debutant, not a competing claim &mdash; but it is the widest '
  'consensus-side number yet.</b> The card is confirmed at <b>15 fights at Accor Arena</b>, with '
  '<b>Hooker 24-14 and Parnasse 23-2</b>.<br><br>&#9888; <b>The middleweight regression presented '
  'itself again and was again beaten by a story rather than a list.</b> An aggregated champions page '
  'fetched this run returned <b>Khamzat Chimaev at 185</b>. <b>A separate report fetched this run states '
  'plainly that Sean Strickland <i>is once again the middleweight champion</i>, having recaptured the '
  'title from Chimaev at UFC 328, and that his first defense &mdash; targeted for December after a '
  'shoulder injury &mdash; would be a rematch with either Chimaev or Nassourdine Imavov.</b> '
  '<b>A champion cannot be scheduled to defend against the man who holds his belt. The board stands: '
  'Strickland at middleweight.</b></div>')
mm = mm.replace(ts.group(1), mblock, 1)
wr("mma-briefing.html", mm)

# ---------------------------------------------------------------------- INDEX
ix = rd("index.html")
ix = ix.replace("Data as of 4:55 PM ET", "Data as of %s ET" % NOW)
wr("index.html", ix)
print("edits_1705 applied")
