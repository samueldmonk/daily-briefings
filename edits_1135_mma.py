import re,sys
F='mma-briefing.html'
t=open(F).read()
E=[]
def rep(name,old,new):
    E.append((name,old,new))

# 1. TLDR
rep('tldr',
 'Song Yadong knocked out Umar Nurmagomedov in the second round of the UFC Shanghai main event and demanded a title shot in the cage, vowing to become China&rsquo;s first male UFC champion; the promotion has announced four $100,000 bonuses &mdash; a second outlet independently puts the card&rsquo;s total at $400,000, which is the same four awards counted a different way &mdash; and a third account now backs the version of the finish that calls the punch an uppercut, leaving that detail two-to-one but still unadopted.',
 'Song Yadong knocked out Umar Nurmagomedov in the second round of the UFC Shanghai main event and asked for a title shot, but the bantamweight belt is already spoken for &mdash; Petr Yan defends it against Merab Dvalishvili in a trilogy at UFC 333 in Abu Dhabi on October 24, a card this page had not carried until now; a third source has meanwhile given the finishing punch a third different name, which retires this page&rsquo;s two-to-one tally rather than settling it; and Umar&rsquo;s brother Usman is reported to have come into the cage during Song&rsquo;s celebration, with both camps described as respectful afterwards.')

# 2. freshline
rep('freshline','>Data as of 11:05 AM ET','>Data as of 11:35 AM ET')
# 3. masthead updated
rep('updated','Updated <span id="updated">10:50 AM ET</span>','Updated <span id="updated">11:35 AM ET</span>')

# 4. New UFC 333 card in Fight Week
rep('ufc333card',
 '<div class="cards">\n<div class="card"><div class="tags"><span class="tag">Carried</span></div>\n<div class="dateline">Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</div>',
 '''<div class="cards">
<div class="card"><div class="tags"><span class="tag new">New &middot; 11:35 AM</span></div>
<div class="dateline">Sat, Oct 24 &middot; Etihad Arena, Yas Island, Abu Dhabi</div>
<h4>UFC 333 &mdash; Volkanovski vs. Evloev, and Yan vs. Dvalishvili 3</h4>
<p><b>New to this page at 11:35 AM, and it is the card that answers the callout above.</b> Featherweight
champion <b>Alexander Volkanovski</b> headlines against undefeated No.&nbsp;1 contender <b>Movsar Evloev</b>;
in the co-main, bantamweight champion <b>Petr Yan</b> defends against No.&nbsp;1 contender
<b>Merab Dvalishvili</b> in a <b>trilogy bout</b> &mdash; Yan took the belt from Dvalishvili by unanimous
decision at UFC 323 in December 2025, avenging an earlier loss, and the series is level at
<b>one win apiece</b>. Also listed: <b>Lone&rsquo;er Kavanagh</b> (No.&nbsp;6 flyweight) vs.
<b>Ramazan Temirov</b> (No.&nbsp;7). Sourced this run from regional press, a national daily, a
national sports outlet and the venue&rsquo;s own event listing, all describing the same two title bouts.
<b>No betting line for this card was stated by any source seen this run, so none is printed</b>, and no
broadcast or start time was stated either.</p></div>
<div class="card"><div class="tags"><span class="tag">Carried</span></div>
<div class="dateline">Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</div>''')

# 5. Callout paragraph rewritten
rep('callout',
 'New at 10:50 AM &mdash; the callout, and what it is worth.</b> Song used his post-fight interview to <b>ask for the title shot outright</b> and to say he intends to become <b>the first male UFC champion from China</b>. That is stated here as he stated it &mdash; an ambition, not a record and not a booking. <b>Nothing has been announced.</b> The relevant fact from the board below is that the bantamweight title is held by <b>Petr Yan</b>, and no bantamweight title bout appears on any card in the Fight Week section above.</li>',
 '''The callout, and what it ran into at 11:35 AM.</b> Song used his post-fight interview to
<b>ask for the title shot outright</b> and to say he intends to become <b>the first male UFC champion from
China</b>. That is stated here as he stated it &mdash; an ambition, not a record and not a booking, and
<b>nothing has been announced for him</b>. What changed this edition is the other half of the sentence.
Until now this page said that no bantamweight title bout appeared on any card in the Fight Week section;
that was true of the September cards it was then listing, and it is <b>no longer the useful statement</b>.
Sources fetched at 11:35 AM place a bantamweight title fight on the calendar: <b>Petr Yan defends against
Merab Dvalishvili at UFC 333 in Abu Dhabi on October 24</b>, in the trilogy bout now carried in Fight Week
above. So the shot Song asked for is <b>already assigned to someone else</b> &mdash; which makes the callout
a bid to be next after that fight, not a bid for the next one. This page still does not treat a callout as a
booking; it now has the booking it should have been checked against.</li>''')

# 6. punch — third name
rep('punch',
 'That is <b>two sources for the uppercut against one for the hook</b>. This page still prints',
 'That was <b>two sources for the uppercut against one for the hook</b> &mdash; a count this edition retires; see the third name sourced at 11:35 AM below. This page still prints')

rep('punch3',
 '&mdash; does not distinguish between them. The same report adds a first-round detail',
 '''&mdash; does not distinguish between them. <b>New at 11:35 AM &mdash; a third name for the same punch, and the tally is abandoned rather than extended.</b> A major national sports outlet, reporting the result independently, calls the finishing blow neither a hook nor an uppercut but a <b>short right hand</b>, and supplies a mechanism the other accounts did not: Nurmagomedov <b>ducked away from a left hand and into the path of it</b>, it <b>connected near his right ear</b>, and Song landed <b>three finishing shots on the mat</b> before the referee intervened. Note what agrees and what does not. The <b>location</b> now corroborates across accounts that disagree on the punch &mdash; this report has it landing <b>near the right ear</b> and the bonus report has the uppercut landing <b>behind the ear</b>. The <b>name</b> does not: there are now <b>three different names for one punch</b> across at least four reports. This page therefore <b>stops counting</b>. A tally of secondary descriptions was never a verification method, and a third entrant makes that plain rather than breaking a tie; the official method, <b>knockout (punch)</b>, remains the only description with a primary source behind it. The same report adds a first-round detail''')

# 7. odds — 5-1 characterisation
rep('odds',
 'Open-to-current is the only move this page calls a\nmove; simultaneous books that disagree are a spread, not a drift.</p>',
 '''Open-to-current is the only move this page calls a
move; simultaneous books that disagree are a spread, not a drift.
<b>New at 11:35 AM &mdash; a characterisation that sits outside that range, printed as a characterisation.</b>
A national sports outlet describes Song as a <b>&ldquo;nearly 5-1 underdog&rdquo; at DraftKings</b>. The widest
price this page has recorded on any book is <b>+400</b>, and <b>no source seen this run states a DraftKings
number at all</b>. A rounded description of a price and a recorded price are different objects; both are
printed, <b>neither is adopted</b>, and this page does not convert one into the other to make them agree.</p>''')

# 8. champions check at 11:35
rep('champs',
 'unchanged for a <b>fifty-first consecutive\nedition</b> &mdash; unchanged and re-confirmed are different claims and only the first is being made here.',
 '''unchanged for a <b>fifty-first consecutive
edition</b> &mdash; unchanged and re-confirmed are different claims and only the first is being made here.</p>
<p><b>Checked a third time at 11:35 AM, and the same query has now produced three different outcomes in
three consecutive runs.</b> This run&rsquo;s listing <b>agreed with this board on six men&rsquo;s belts by
name and by date</b> &mdash; Aspinall; <b>Ulberg, April&nbsp;11, 2026</b>; <b>Strickland, May&nbsp;9,
2026</b>; <b>Makhachev, November&nbsp;15, 2025</b>; <b>Gaethje, June&nbsp;14, 2026</b>; <b>Volkanovski,
April&nbsp;12, 2025</b> &mdash; and then rendered <b>men&rsquo;s bantamweight as &ldquo;vacant&rdquo;</b>.
&#9888; <b>That was rejected.</b> The bantamweight belt is not vacant: <b>Petr Yan</b> holds it, and a
targeted check this run states he <b>reclaimed it by unanimous decision over Merab Dvalishvili at UFC 323
on December&nbsp;6, 2025</b> and <b>defends it against Dvalishvili at UFC 333 on October&nbsp;24</b> &mdash;
a champion with a booked defence is not a vacancy. <b>An absence in a listing is not a vacancy</b>, and a
&ldquo;vacant&rdquo; rendering is exactly the shape of one of the regressions this project&rsquo;s standing
corrections file already records, when featherweight was published vacant while Volkanovski held it. Across
three runs of one query the answers have been: a <b>stale</b> listing at 10:50, <b>full agreement</b> at
11:05, and <b>agreement plus one unsupported vacancy</b> at 11:35. That is the argument for the method
rather than for the source. Newly sourced on this board at 11:35 AM: <b>Volkanovski defends against
Movsar Evloev</b> on the same October&nbsp;24 card, which is the first dated booking this page has carried
for either belt.''')

# 9. Usman incident
rep('usman',
 '<li><b>Sean Woodson\'s return.</b>',
 '''<li><b>New at 11:35 AM &mdash; what happened in the cage after the finish, with the intent left open.</b>
Two accounts of the same moments are on the record and this page prints both. In one, Song ran a victory lap
inside the cage and <b>nearly ran into Umar&rsquo;s younger brother and cornerman, Usman Nurmagomedov</b>
&mdash; the PFL lightweight champion &mdash; <b>who had rushed in to check on his fallen brother</b>. In the
other, <b>Usman charged the Octagon and came close to throwing a spinning elbow aimed at Song&rsquo;s head</b>
as Song celebrated. Both descriptions come from post-event reporting fetched this run; they differ on
<b>intent</b>, which is not something this page can establish, and they agree on the facts that matter:
<b>nothing landed</b>, and the footage circulated widely afterwards. What followed is reported without
disagreement &mdash; <b>both sides were respectful</b>, and <b>Khabib Nurmagomedov helped treat a cut on
Song&rsquo;s face</b>. No disciplinary action, commission statement or promotion comment was stated by any
source seen this run, and none is printed.</li>
<li><b>Sean Woodson\'s return.</b>''')

# 10. sources
rep('sources',
 'Sherdog &mdash; Yadong Song crushes Umar Nurmagomedov in big upset</a>',
 '''Sherdog &mdash; Yadong Song crushes Umar Nurmagomedov in big upset</a><br><a href="https://www.espn.com/mma/story/_/id/49762250/song-yadong-kos-umar-nurmagomedov-massive-ufc-upset-shanghai">ESPN &mdash; Song Yadong KOs Umar Nurmagomedov in massive UFC upset (short right hand; &ldquo;nearly 5-1 underdog&rdquo;)</a><br><a href="https://sports.yahoo.com/articles/song-yadong-lands-unbelievable-knockout-130811359.html">Yahoo Sports &mdash; Song Yadong lands knockout uppercut to upset Umar Nurmagomedov</a><br><a href="https://www.thenationalnews.com/sport/combat-sports/2026/08/16/volkanovski-vs-evloev-and-yan-vs-dvalishvili-trilogy-bout-set-for-ufc-333-in-abu-dhabi/">The National &mdash; Volkanovski vs Evloev and Yan vs Dvalishvili trilogy set for UFC 333 in Abu Dhabi</a><br><a href="https://gulfnews.com/sport/abu-dhabi-ufc-333-championship-fights-tickets-more-1.500643436">Gulf News &mdash; UFC 333 Abu Dhabi: title fights, Etihad Arena, October 24</a><br><a href="https://www.si.com/fannation/mma/news/ufc-reveals-alexander-volkanovski-s-title-defense-dvalishvili-yan-3-in-abu-dhabi">Sports Illustrated / FanNation &mdash; UFC reveals Volkanovski&rsquo;s title defence and Dvalishvili&ndash;Yan 3</a><br><a href="https://www.etihadarena.ae/en/event-booking/ufc-333">Etihad Arena &mdash; UFC 333 official event listing</a><br><a href="https://en.wikipedia.org/wiki/UFC_333">Wikipedia &mdash; UFC 333 (card, date, venue)</a>''')

miss=[]
for name,old,new in E:
    if old in t:
        t=t.replace(old,new,1)
    else:
        miss.append(name)
open(F,'w').write(t)   # partial-write discipline: write what matched
print('WROTE',F,'applied',len(E)-len(miss),'of',len(E))
print('MISSED:',miss if miss else 'none')
