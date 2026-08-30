#!/usr/bin/env python3
"""Real defects caught by validate_1514.py. Four page defects + one tag class."""
D = "/sessions/serene-vigilant-hypatia/mnt/outputs/"
OBS = "3:10 PM"
fails = []

def edit(f, pairs):
    s = open(D + f, encoding="utf-8").read()
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new, 1)
        else:
            fails.append(f + " :: " + old[:70])
    open(D + f, "w", encoding="utf-8").write(s)

# DEFECT 1 (Wall Street): a declination that has since been answered still reads as open.
edit("wallstreet-briefing.html", [(
 "No reporting date for Palo Alto Networks was stated by anything fetched, so none is printed.",
 "<b>Superseded at " + OBS + ".</b> That sentence read, correctly at the time: <i>no reporting date for "
 "Palo Alto Networks was stated by anything fetched, so none is printed.</i> <b>A date has now been "
 "stated.</b> A week-ahead preview dated <b>August 30</b> puts <b>Palo Alto Networks and Dell "
 "Technologies after Tuesday&rsquo;s close</b>, and the date is printed in On the Radar below. "
 "<b>The declination is closed, not deleted</b> &mdash; a page that withholds a figure for want of a "
 "source should show what happened when the source arrived."
)])

# DEFECT 2 (Cyber): the countdown baseline was still Saturday after the board rolled to Sunday.
edit("cyber-briefing.html", [(
 "Countdowns above are measured from Saturday, August 29, 2026",
 "Countdowns above are measured from <b>Sunday, August 30, 2026</b> &mdash; corrected at " + OBS +
 ", because the board rolled at midnight and this baseline line had not rolled with it. It previously "
 "read &ldquo;Saturday, August 29,&rdquo; which was the baseline the day before. <b>The four countdowns "
 "themselves were already measured from today and did not change</b>: the August 29 pair is OVERDUE, the "
 "August 30 pair is 0 days, September 9 is 10 days and September 10 is 11 days"
)])

# DEFECT 3 (MMA): a paraphrase this page now refuses was still asserted elsewhere on the page.
edit("mma-briefing.html", [(
 "The rematch itself is described as coming out of a UFC 323 title fight that ended in injury.",
 "&#9888; <b>Corrected at " + OBS + " for internal consistency.</b> That report describes the rematch as "
 "coming out of a UFC 323 title fight &ldquo;that ended in injury,&rdquo; and this page had repeated the "
 "phrasing here while <b>declining it in the odds block above</b> &mdash; the two could not both stand. "
 "<b>The sourced finish governs:</b> Van took the belt by <b>technical knockout 26 seconds into round "
 "one</b>, after an arm injury to Pantoja. The characterisation is <b>recorded as the source&rsquo;s, not "
 "adopted as this page&rsquo;s</b>."
)])

# DEFECT 4 (MMA): undefined tag class introduced by this run's new card.
edit("mma-briefing.html", [('<span class="tag prospect">prospect</span>',
                            '<span class="tag pros">prospect</span>')])

print("FIX2 FAILURES:", fails if fails else "none")
