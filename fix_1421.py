# -*- coding: utf-8 -*-
D='/tmp/db_1787854887/'
def go(f,pairs):
    s=open(D+f,encoding='utf-8').read()
    for old,new in pairs:
        c=s.count(old); assert c>=1,"MISSING in %s :: %s"%(f,old[:90]); s=s.replace(old,new)
    open(D+f,'w',encoding='utf-8').write(s)

# (i) WS: the tldr overclaimed — Benzinga stamped 8:15 a.m. on a FUTURES figure earlier today
go('wallstreet-briefing.html',[
 ("as of 1:25 PM ET — the first time-stamped figure any source has given this page today —",
  "as of 1:25 PM ET — the first cash-session figure any source has stamped with a time for this page today —"),
 ("<b>And for the first time this session a source has stamped a time on its number:</b>",
  "<b>And for the first time in the cash session a source has stamped a time on its number</b> — the only earlier timestamp this page holds is Benzinga's 8:15 a.m. read of S&amp;P <i>futures</i>:"),
 # (ii) retense the carried 12:38 paragraph so two paragraphs do not both claim 'the latest read'
 ("The latest read seen this run has the <b>Nasdaq Composite up 400.29 points, or 1.53%</b>",
  "The 12:38 read had the <b>Nasdaq Composite up 400.29 points, or 1.53%</b>"),
 ("<b>Both large-cap gauges are above the 12:05 tallies</b> this page carried",
  "<b>Both large-cap gauges were above the 12:05 tallies</b> this page carried"),
 ("<b>No fresh Russell 2000 read was seen this run</b>, so the small-cap line from 12:05 (+7.64, +0.25%) is not restated as current.",
  "<b>No fresh Russell 2000 read has been seen at 12:38 or at 2:21</b>, so the small-cap line from 12:05 (+7.64, +0.25%) is not restated as current."),
])

# (iii) cyber: Cursor and Kiro are TWO tools, not three
go('cyber-briefing.html',[
 ("the third AI developer tool to appear on this page today", "the second AI developer tool to appear on this page today"),
 ("This is the <b>third AI developer tool</b> to appear on this page today, alongside the Aurora affiliate's use of an AI coding assistant across 20+ intrusions and the earlier agent-tooling thread — but no source seen connects them, and no campaign is asserted.",
  "This is the <b>second AI developer tool</b> to appear on this page today, alongside the Aurora affiliate's use of the AI coding assistant Cursor across 20+ intrusions — but no source seen connects the two, and no campaign is asserted."),
])
print("fixes applied")
