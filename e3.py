# -*- coding: utf-8 -*-
import io
P='/tmp/db_1788305419/wallstreet-briefing.html'
s=io.open(P,encoding='utf-8').read(); n=0
def rep(old,new,label):
    global s,n
    c=s.count(old)
    if c!=1: print(('MISS: ' if c==0 else 'AMBIG(%d): '%c)+label); return False
    s=s.replace(old,new); n+=1; print('ok:',label); return True

# ---------- W4: Chart of the Day note -> add the LUMUS catalyst + why Dell does not take the slot
rep('Fervo and GoPro both remain in the movers list above.</div>',
 'Fervo and GoPro both remain in the movers list above. '
 '&#9888;&#9888; <b>The move now has a cause, which it did not have when the slot was assigned.</b> Alumis announced before the opening bell that its '
 '<b>Phase 2b LUMUS trial of envudeucitinib in moderate-to-severe systemic lupus erythematosus missed both its primary and its key secondary endpoints in the overall trial population</b>; '
 'the stock was <b>halted pending the news</b> and reopened sharply lower. A <b>prespecified subgroup with a high interferon gene signature (IFNGS-high) did respond</b> across the primary and key secondary endpoints, '
 'and the company says it <b>intends to discuss a Phase 3 programme in that biomarker-selected population with regulators</b>. '
 '&#9888; <b>A second clock on the same collapse:</b> one read has the stock <b>down 54.2% pre-open</b> against the <b>&minus;57.75%</b> session figure this slot was assigned on &mdash; '
 'pre-open and session are different windows, both are printed, neither is adopted as the other. '
 '&#9888; <b>And the slot does not move to Dell tonight.</b> Dell is by some distance the largest single-name move on this page, but it happened <i>after the close</i>; '
 'this slot is defined by the session, the session is over, and an after-hours gap does not retroactively become the session&rsquo;s biggest move. It is covered in After-Hours Movers instead.</div>',
 'W4 chart note')

# ---------- W5: rates rows ----------
rep('Schwab adds the 10-year is now &ldquo;a stone&rsquo;s throw from 5%.&rdquo;</td>',
 'Schwab adds the 10-year is now &ldquo;a stone&rsquo;s throw from 5%.&rdquo; '
 'A <b>fourth</b> Tuesday mark landed after the close: Trading Economics now quotes the 10-year at <b>4.81%</b> &mdash; the highest reading this page has carried today, '
 'and above every earlier print rather than in conflict with them. A separate read frames the same move as the benchmark yield rising <b>toward 4.78%</b>. '
 '&#9888; <b>Five clocks, one direction, no adoption</b> &mdash; the row header is a range for exactly this reason.</td>',
 'W5a 10y')

rep('The two are not the same record and are not merged here.</td>',
 'The two are not the same record and are not merged here. '
 'A post-close read adds a <b>third</b> September 1 mark, <b>5.28%</b> (Trading Economics), again the highest this page has carried today and still below the 5.34% level record; '
 'the same read describes <b>30-year bonds reaching levels not seen since 2006</b>, which corroborates the duration framing above from a second source. '
 '&#9888; <b>Note what that corroboration does and does not do:</b> it supports the &ldquo;worst stretch since 2006&rdquo; characterisation, it does not restate the 55-day count, and it is not merged into it.</td>',
 'W5b 30y')

rep('<td>Japan 10-year government bond</td><td>~3%</td><td class="up">Briefly touched <b>3% for the first time in 30 years</b> &mdash; the leg of the sell-off that makes it global rather than domestic</td></tr>',
 '<td>Japan 10-year government bond</td><td>~3%</td><td class="up">Briefly touched <b>3% for the first time in 30 years</b> &mdash; the leg of the sell-off that makes it global rather than domestic. '
 'A read fetched this run dates it precisely: the yield <b>jumped more than six basis points to 3% for the first time since 1996</b>, which is the same claim with a year attached rather than a rounded interval.</td></tr>'
 '<tr><td>Japan 2-year government bond</td><td>1.81%</td><td class="up">New this run: the Japanese <b>two-year</b> yield touched a <b>31-year high of 1.81%</b>. '
 '&#9888; It is listed because it answers an objection to the 10-year line &mdash; a single long-maturity print can be a technical event, whereas the short end moving to a multi-decade high alongside it is a policy-expectations move.</td></tr>',
 'W5c japan')

rep("<td>WTI crude</td><td>$86.57 &ndash; above $89</td>",
    "<td>WTI crude</td><td>$86.57 &ndash; above $95</td>", "W5d0 wti header")
rep('Trading Economics later at $86.57 (+0.94%)</td>',
 'Trading Economics later at $86.57 (+0.94%); a post-close read has WTI at <b>$90.82, up 5.90% on the session</b> and <b>up 13.05% over the past month</b> (Trading Economics), '
 'while a Yahoo Finance session headline has <b>oil topping $95</b>. '
 '&#9888;&#9888; <b>Those last two do not reconcile and are not made to.</b> A $90.82 quote and an &ldquo;above $95&rdquo; headline are more than four dollars apart on the same day &mdash; '
 'a gap that different contracts, different benchmarks or different clocks can each explain, and this desk cannot tell which without a source that says so. '
 '<b>Both are printed with their attributions; neither is adopted, and no midpoint is invented.</b> The direction &mdash; sharply higher on renewed U.S.&ndash;Iran fighting &mdash; is the part every read agrees on.</td>',
 'W5d wti')

io.open(P,'w',encoding='utf-8').write(s); print('applied',n)
