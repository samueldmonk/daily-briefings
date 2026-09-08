# -*- coding: utf-8 -*-
# Edition 2026-09-08 ~14:27 ET research / Midday. MMA page edits.
import io, os, sys
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, "b_mma.py")
s = io.open(p, encoding="utf-8").read()
n = 0

def rep(old, new):
    global s, n
    assert old in s, "MISSING: " + old[:90]
    s = s.replace(old, new, 1)
    n += 1

# ---------------- sources ----------------
rep(''' ("ESPN - UFC's first Paramount+ fight card averages nearly 5M views", "https://www.espn.com/espn/story/_/id/47738036/ufc-first-paramount+-fight-card-averages-nearly-5m-views"),''',
    ''' ("ESPN - UFC's first Paramount+ fight card averages nearly 5M views", "https://www.espn.com/espn/story/_/id/47738036/ufc-first-paramount+-fight-card-averages-nearly-5m-views"),
 ("Yardbarker - UFC Releases Michael Page After UFC Paris Win", "https://www.yardbarker.com/soccer/articles/ufc_releases_michael_page_after_ufc_paris_win/s1_17349_44273428"),
 ("boxingnews.com - UFC Releases Michael Page After UFC Paris Win", "https://boxingnews.com/news/ufc-releases-michael-page-paris"),
 ("Yahoo Sports - Michael 'Venom' Page's UFC Future Takes Major Hit After Rankings Snub", "https://sports.yahoo.com/articles/michael-venom-page-ufc-future-052647306.html"),
 ("Bloody Elbow - Michael 'Venom' Page doubts re-signing with UFC after UFC Paris win", "https://bloodyelbow.com/2026/09/05/michael-venom-page-doubts-re-signing-with-ufc-by-putting-himself-in-their-shoes-after-ufc-paris-win/"),
 ("Yahoo Sports - Noche UFC 4 odds: Betting line opens for Jean Silva vs. Jose Delgado main event", "https://sports.yahoo.com/articles/noche-ufc-4-odds-betting-171123912.html"),
 ("MMAOddsBreaker - Opening Betting Odds for Noche UFC: Silva vs. Delgado", "https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161244-opening-betting-odds-for-noche-ufc-silva-vs-delgado/"),
 ("LowKick MMA - UFC Noche: Jean Silva Heavy Favorite As Jose Delgado Takes Late Main Event Call", "https://www.lowkickmma.com/ufc-noche-jean-silva-heavy-favorite-as-jose-delgado-takes-late-main-event-call/"),
 ("Yahoo Sports - UFC Paris Bonuses! France's Parnasse, Sola, And Keita Clean Up With $100K Payouts", "https://sports.yahoo.com/articles/ufc-paris-bonuses-france-parnasse-230944058.html"),
 ("ESPN - Injured UFC champion Ulberg hopes to return 'early next year'", "https://www.espn.com/mma/story/_/id/49743588/injured-ufc-champion-ulberg-hopes-return-early-next-year"),
 ("Sports Illustrated / FanNation MMA - UFC Champion Carlos Ulberg Provides Updated Return Fight Timeline", "https://www.si.com/fannation/mma/news/ufc-champion-carlos-ulberg-provides-updated-return-fight-timeline"),
 ("Athlon Sports - When Is The Next UFC? Date, Start Times, Full Schedule", "https://athlonsports.com/mma/ufc-schedule-2026-dates-start-times-full-fight-cards"),''')

# ---------------- tldr ----------------
rep('''<div class="tldr"><b>Tale of the Tape</b> <span>Michael Page has been pulled from the UFC rankings less than two days after winning at UFC Paris with a release reportedly looming, while Valentina Shevchenko has been stripped of the women&#39;s flyweight title after telling the promotion she would be unable to compete for at least a year.</span></div>''',
    '''<div class="tldr"><b>Tale of the Tape</b> <span>Two outlets now report that Michael Page has actually been released by the UFC, three days after he won at UFC Paris and a day after being pulled from the rankings, though the promotion has announced nothing.</span></div>''')

# ---------------- top story ----------------
rep('''<h3 style="margin:0 0 8px;font-size:20px">Michael Page wins on Saturday, is off the rankings by Monday, and a release is reportedly looming</h3>
<p style="margin:0 0 10px">UFC middleweight <b>Michael &ldquo;Venom&rdquo; Page</b> beat <b>Nursulton Ruziboev</b> by unanimous decision at <b>UFC Paris on 5 September</b>. He was initially eligible to be ranked following that win. Then, according to longtime MMA journalist <b>John Morgan</b>, the weekly UFC rankings email sent on <b>Monday 7 September</b> told voters that Page had been <b>removed from the rankings</b> and would not be eligible for this week&#39;s selection.</p>
<p style="margin:0">Page had been <b>No. 15 in the UFC&#39;s media rankings</b> and <b>No. 8 in the recently formed Meta rankings</b>, which the promotion adopted this summer. Reporting this run frames the removal as a strong signal that a <b>release from the promotion is imminent</b>. <span class="mut">The release itself is reported as looming rather than announced, and is described that way here; nothing read this run is a promotion statement, and the ranking removal is the only action actually confirmed to have happened.</span></p>''',
    '''<h3 style="margin:0 0 8px;font-size:20px">Michael Page wins on Saturday, is off the rankings by Monday, and is now reported to have been released outright</h3>
<p style="margin:0 0 10px"><b>Michael &ldquo;Venom&rdquo; Page</b>, a <b>39-year-old welterweight</b>, beat <b>Nursulton Ruziboev</b> by unanimous decision at <b>UFC Paris on 5 September</b>. He was initially eligible to be ranked after that win. Then, according to longtime MMA journalist <b>John Morgan</b>, the weekly UFC rankings email sent on <b>Monday 7 September</b> told voters that Page had been <b>removed from the rankings</b> and would not be eligible for this week&#39;s selection.</p>
<p style="margin:0 0 10px"><b>What has changed since this briefing&#39;s 1:50 p.m. edition:</b> two outlets now report the release as having <b>happened</b> rather than as looming, under the headline that the UFC has released him following the Paris win, and a third report says he has been <b>removed from the UFC roster</b>. <span class="mut">This is still reporting, not a promotion announcement &mdash; one of the same reads describes the release as &ldquo;reportedly&rdquo; done &mdash; and the rankings removal remains the only action independently documented in an artefact, namely the email to voters. The page states the reports and their status rather than treating a headline as a confirmation.</span></p>
<p style="margin:0">The context makes it plausible: Page had <b>not re-signed</b> with the promotion before the bout and was <b>fighting out his existing contract</b> at UFC Paris; days earlier he had said publicly he doubted he would re-sign. He had been <b>No. 15 in the UFC&#39;s media rankings</b> and <b>No. 8 in the recently formed Meta rankings</b>, which the promotion adopted this summer. He signed with the UFC in <b>December 2023</b> and went <b>5-1 across six appearances</b>, <b>without a single finish inside the Octagon</b>. <span class="mut">Correction to this briefing&#39;s earlier editions today: they called Page a middleweight. Sources read this run identify him as a welterweight, and the earlier description was wrong.</span></p>''')

# ---------------- Noche UFC card ----------------
rep('''<h3>Noche UFC: Jean Silva vs. Jose Delgado</h3>
<p>A featherweight (145 lb) main event. New this run: the card carries <b>13 bouts, the fullest lineup on the UFC calendar</b>, with <b>Paramount+ prelims at 2 p.m. ET and the main card at 5 p.m. ET</b>. Also on the card: <b>Brandon Moreno vs. Joseph Morales</b>, <b>Manon Fiorot vs. Alexa Grasso</b>, and &mdash; new this run &mdash; <b>Waldo Cortes-Acosta vs. Curtis Blaydes</b>. <br><span class="mut">Odds: <b>Silva &minus;428 / Delgado +324</b> (UFCalendar, across 20 sportsbooks, 81% implied) and <b>&minus;425 / +355</b> (FightOdds.io), both carried from a prior verified reading; no odds for this card returned in searches run this edition.</span></p>''',
    '''<h3>Noche UFC: Jean Silva vs. Jose Delgado</h3>
<p>A <b>five-round featherweight</b> main event, and this run finally explains why it is this pairing: <b>Yair Rodriguez withdrew from the card with an injury</b>, and <b>Jose Delgado took the main event on late notice</b> in his place. The card carries <b>13 bouts, the fullest lineup on the UFC calendar</b>. Also on it: <b>Brandon Moreno vs. Joseph Morales</b>, <b>Manon Fiorot vs. Alexa Grasso</b> and <b>Waldo Cortes-Acosta vs. Curtis Blaydes</b>.</p>
<p style="margin:9px 0 0"><b>Tale of the tape.</b> <b>Jean Silva is 17-3</b> and <b>6-1 in the UFC with five finishes</b>, having come through Dana White&#39;s Contender Series in <b>late 2023</b>. <b>Jose Delgado is 12-2</b> and <b>4-1 with a pair of knockouts</b>, from his own Contender Series win in <b>summer 2024</b>.</p>
<p style="margin:9px 0 0"><b>Odds, sourced directly this run rather than carried:</b> the line <b>opened at Silva &minus;450 / Delgado +350</b> and, within hours, <b>moved to Silva &minus;425 / Delgado +355</b>. <span class="mut">A start-time conflict is worth stating: a schedule page read this run lists the Noche main card at <b>2:00 p.m. ET</b>, where this briefing has carried <b>prelims at 2 p.m. ET and the main card at 5 p.m. ET</b>. Both readings are shown; neither is discarded, and no single time is asserted as correct.</span></p>''')

# ---------------- UFC 331 time conflict note ----------------
rep('''<span class="mut">An earlier edition carried Tsarukyan at &minus;380; this run&#39;s read gives &minus;400, and the newer read is used.</span></p>''',
    '''<span class="mut">An earlier edition carried Tsarukyan at &minus;380; a later read gives &minus;400, and the newer read is used. A schedule page read this run lists the UFC 331 main card at <b>5:00 p.m. ET</b>, against the <b>prelims 6 p.m. / main card 9 p.m. ET</b> this briefing has carried. Both are shown rather than reconciled.</span></p>''')

# ---------------- UFC 332 / Shevchenko rematch guarantee ----------------
rep('''<span class="mut">No betting line for this card returned in anything read this run, so none is printed.</span></p>''',
    '''New this run: the UFC has said <b>Shevchenko gets a title shot when she is cleared</b>, guaranteeing her a route back to the belt once she recovers. <span class="mut">No betting line for this card returned in anything read this run, so none is printed.</span></p>''')

# ---------------- results: $25k names ----------------
rep('''plus <b>four $25,000 cheques</b> for finishes that did not win a bonus. No Fight of the Night was awarded.''',
    '''plus <b>four $25,000 cheques</b> for finishes that did not win a Performance bonus, now named for the first time on this page: <b>Delphine Benouaich, Matthieu Duclos, Modestas Bukauskas</b> and <b>Kurtis Campbell</b>. No Fight of the Night was awarded.''')

rep('''Only bouts whose result and method were both stated in sources read this run are listed; the card ran to fourteen fights and the remainder are not reconstructed here.</p>''',
    '''Only bouts whose result and method were both stated in sources read this run are listed; the card ran to fourteen fights and the remainder are not reconstructed here. Two further main-card pairings surfaced this run &mdash; <b>Daniil Donchenko vs. Punahele Soriano</b> and <b>Kurtis Campbell vs. Trevor Peek</b> &mdash; but no winner or method was stated for either, so neither is tabulated above.</p>''')

# ---------------- Around the Sport: Ulberg ----------------
rep('''<li><b>Twelve events remain on the 2026 calendar</b>''',
    '''<li><b>Carlos Ulberg will not defend the light heavyweight title this year, and an interim belt is looking likelier.</b> He <b>tore the ACL in his right knee</b> during the opening of the UFC 327 fight in which he won the belt, rallied to finish Ji&#345;&iacute; Proch&aacute;zka anyway, and had reconstructive surgery a week later on what he has called a <b>full rupture</b> of the ligament. He now hopes to return <b>early next year</b>. This run&#39;s reads state that the UFC <b>has not yet indicated</b> an interim light heavyweight title will be created, while describing that outcome as increasingly likely given the timeline. His likeliest first challenger is named as <b>Magomed Ankalaev</b>, who finished <b>Bogdan Guskov</b> in July, or <b>Paulo Costa</b>, who has won back-to-back fights since his 2024 loss to Sean Strickland.</li>
<li><b>Twelve events remain on the 2026 calendar</b>''')

rep('''<li><b>Noche UFC&#39;s 13-bout card is the fullest on the calendar</b>, and it has grown again this run with Waldo Cortes-Acosta vs. Curtis Blaydes appearing among its main fights.</li>''',
    '''<li><b>Noche UFC&#39;s 13-bout card is the fullest on the calendar</b>, and the reason its main event changed is now on the record: <b>Yair Rodriguez withdrew injured</b> and <b>Jose Delgado stepped in on late notice</b> opposite Jean Silva. A schedule page read this run still bills the card as &ldquo;Rodriguez vs. Silva&rdquo;, which is a stale listing rather than a competing claim, and is not used.</li>''')

# ---------------- champions board: LHW regression ----------------
rep('''<span class="mut">This run&#39;s champions list seats Ulberg and dates it 11 April 2026 &mdash; agreeing with this board for a second consecutive edition.</span></td></tr>''',
    '''<b>He will not defend in 2026:</b> he tore the ACL in his right knee in that same fight and had reconstructive surgery a week later, and hopes to return early next year. <span class="mut">The champions list read this run has <b>regressed</b>: after two consecutive editions correctly seating Ulberg, it once again seats <b>Alex Pereira</b> at light heavyweight, dated 4 October 2025. That is refused. Pereira vacated to campaign at heavyweight and lost the interim heavyweight bid to Ciryl Gane at Freedom 250 on 14 June 2026; a list seating him at 205 lb cannot postdate UFC 327.</span></td></tr>''')

rep('''<p class="note">Ten of the eleven champions on the list read this run matched this board by name; the women&#39;s flyweight entry is refused above, with the reason given.''',
    '''<p class="note">Nine of the eleven champions on the list read this run matched this board by name &mdash; down from ten last edition, because the light heavyweight entry regressed to Pereira after two editions of agreeing with this board. Both that entry and the women&#39;s flyweight entry are refused above, with the reason given in each cell.''')

io.open(p, "w", encoding="utf-8").write(s)
print("mma edits:", n)
