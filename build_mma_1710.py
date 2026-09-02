# -*- coding: utf-8 -*-
import os,sys
exec(open('/tmp/build_1710.py').read().split('# ============================================================ WALL STREET')[0])

MM_EXTRA=""".cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:10px;padding:11px 15px;margin:0 0 18px;font-size:14.5px;display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}
.cdn b{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn #ufccdn{font-family:var(--mono);color:var(--accent2);font-size:15px}
.dv{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:5px}
.callout.lead{border-left-color:var(--accent)}
.callout.lead .k{color:var(--accent)}
"""
MMCSS=css_for("#100c0c","#1a1313","#322020","#e84545","#ff8a5c",MM_EXTRA)

MM_TLDR=("UFC Paris is three days out and the card just changed &mdash; Mairon Santos is off it with illness &mdash; while debutant "
 "Salahdine Parnasse has been bet from &minus;357 up to about &minus;667 over Dan Hooker in a main event that starts at the unusual hour "
 "of 3 PM ET.")

CDN=('<div class="cdn"><b>Next Card</b> <span>UFC Fight Night: Hooker vs. Parnasse &mdash; Accor Arena, Paris &middot; Saturday, Sept 5</span> '
 '<span id="ufccdn">&nbsp;</span></div>')

CDNJS=("<script>(function(){var tgt=new Date('2026-09-05T12:00:00-04:00');function u(){var el=document.getElementById('ufccdn');if(!el)return;"
 "var d=tgt-new Date();if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}"
 "var m=Math.floor(d/60000),h=Math.floor(m/60),dy=Math.floor(h/24);"
 "el.textContent=dy+'d '+(h%24)+'h '+(m%60)+'m';}u();setInterval(u,30000);})();</script>")

mm=[]
mm.append(CDN)
mm.append('<h2 class="sec">Top Story</h2><div class="callout lead"><div class="k">Fight Week &mdash; Paris</div>'
 '<h3>The card moved under Parnasse this week, and the money moved further</h3>'
 '<p><b>UFC Fight Night: Hooker vs. Parnasse</b> &mdash; UFC Fight Night 287 &mdash; runs Saturday, September 5 at the <b>Accor Arena in Paris</b>, '
 'with prelims at <b>12 PM ET</b> and the main card at <b>3 PM ET</b> on Paramount+. The early start is a concession to the French time zone, '
 'not a scheduling error.</p>'
 '<p><b>Salahdine Parnasse</b> headlines on debut. He is a <b>former two-time KSW featherweight champion and one-time KSW lightweight champion</b> '
 'who signed with the UFC in late July 2026 having previously turned the promotion down &mdash; he did <u>not</u> come through Dana White&rsquo;s '
 'Contender Series, a claim this desk published wrongly once and has refused every run since. He is 23-2 and a promotional newcomer, nothing more '
 'than that yet. <b>Dan Hooker is 24-14 as a professional and 14-10 inside the Octagon</b> &mdash; a record, not a fight count.</p>'
 '<p>The betting has moved hard in one direction. Parnasse <b>opened around &minus;357 with Hooker at +275</b>; he is now quoted '
 '<b>&minus;667 with Hooker at +417</b>, with the market spread across roughly &minus;500 to &minus;700 and +360 to +450. A debutant favoured '
 'that heavily over a fighter with 24 professional wins is the story of the week.</p>'
 '<p><b>New this run:</b> UFC.com has posted a card change. <b>Mairon Santos is out of his featherweight bout with Nathaniel Wood due to illness</b>, '
 'and <b>undefeated newcomer Pavel Andrusca</b> steps in, also making his UFC debut.</p></div>')

mm.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2><div class="cards two">'
 '<div class="card"><div class="dv">Sat Sept 5 &middot; Accor Arena, Paris</div><h4>UFC Fight Night: Hooker vs. Parnasse</h4>'
 '<span class="tag new">New</span><p>Dan Hooker vs. Salahdine Parnasse at lightweight; Parnasse headlines on his UFC debut. Co-main '
 '<b>Far&egrave;s Ziam vs. Axel Sola</b>, an all-French lightweight bout, plus <b>Daniil Donchenko vs. Punahele Soriano</b> and '
 '<b>Nathaniel Wood vs. Pavel Andrusca</b>, the replacement booking. Prelims 12 PM ET, main card 3 PM ET, Paramount+.<br>'
 '<b>Odds: Parnasse &minus;667 / Hooker +417</b> (Rotowire); DraftKings has had it &minus;600 / +440; opened &minus;357 / +275.</p></div>'
 '<div class="card"><div class="dv">Sat Sept 12 &middot; Glendale, Arizona</div><h4>Noche UFC: Silva vs. Delgado</h4>'
 '<p>The annual card celebrating Mexican and Mexican-American culture. Venue city sourced; no odds sourced for the headliner, so none printed.</p></div>'
 '<div class="card"><div class="dv">Sat Sept 19 &middot; Crypto.com Arena, Los Angeles</div><h4>UFC 331: Van vs. Pantoja 2</h4>'
 '<p>Flyweight champion Joshua Van meets Alexandre Pantoja in a rematch of the UFC 323 bout Van won by first-round TKO. Thirteen fights listed. '
 'No odds sourced this run.</p></div>'
 '<div class="card"><div class="dv">Sat Sept 26 &middot; Las Vegas</div><h4>UFC Fight Night: Rosas Jr. vs. Barcelos</h4>'
 '<p>Raul Rosas Jr. headlines against Raoni Barcelos. No odds sourced this run.</p></div>'
 '</div>'
 '<div class="note">Further out: <b>Oct 3 &mdash; UFC 332, Salt Lake City</b>; <b>Oct 10 &mdash; Allen vs. Duncan</b>; '
 '<b>Oct 17 &mdash; Buckley vs. Malott, Edmonton</b>; <b>Oct 24 &mdash; UFC 333: Volkanovski vs. Evloev, Abu Dhabi</b>; '
 '<b>Oct 31 &mdash; Las Vegas</b>. The UFC 333 listing fetched this run gives the matchup but <b>does not describe it as a title fight</b>; '
 'Volkanovski is the reigning featherweight champion and Evloev the number-one contender on this desk&rsquo;s standing record, and that framing '
 'is this desk&rsquo;s, not the listing&rsquo;s.</div>')

mm.append('<h2 class="sec">Last Event &mdash; UFC Shanghai, Saturday August 29</h2>'
 '<div class="note" style="margin-bottom:10px">UFC Fight Night: Nurmagomedov vs. Song &mdash; Oriental Sports Center, Shanghai. Thirteen fights.</div>'
 '<div class="tblwrap"><table>'
 '<tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
 '<tr><td class="win">Song Yadong</td><td>def. Umar Nurmagomedov (main event, bantamweight)</td><td>KO (uppercut), Round 2, 1:48</td></tr>'
 '<tr><td class="win">Bilal Hasan</td><td>def. Nilson Rojas</td><td>KO (single punch)</td></tr>'
 '<tr><td class="win">Liu Ce</td><td>def. Levi Rodrigues Jr.</td><td>Decision &mdash; Fight of the Night</td></tr>'
 '</table></div>'
 '<div class="note"><b>Performance bonuses, $100,000 each:</b> <b>Song Yadong</b> and <b>Bilal Hasan</b> took Performance of the Night; '
 '<b>Liu Ce vs. Levi Rodrigues Jr.</b> took Fight of the Night, with both fighters paid. Song&rsquo;s knockout of Nurmagomedov was an upset and '
 'a hometown one. Only the bouts whose winner, opponent and method were all confirmed in sources fetched this run are tabled &mdash; the full '
 'thirteen-fight card is not reproduced from memory.</div>')

mm.append('<h2 class="sec">Prospect Watch</h2><div class="cards two">'
 '<div class="card"><div class="k">Lightweight &middot; France</div><h4>Salahdine Parnasse (23-2)</h4>'
 '<span class="tag new">New</span><span class="tag a">Debut main event</span>'
 '<p>Two-time KSW featherweight champion and one-time KSW lightweight champion, 14-2 inside KSW with four defences of the lightweight belt. '
 'Signed with the UFC in late July 2026 after previously declining the promotion. His U.S. debut came in May 2026 on the Rousey vs. Carano main '
 'card, a first-round stoppage of Kenneth Cross for a fifth straight win. He is a debutant, not a ranked contender &mdash; and he is not a '
 'Contender Series signee.</p></div>'
 '<div class="card"><div class="k">Featherweight &middot; Debut</div><h4>Pavel Andrusca</h4>'
 '<span class="tag new">New</span><span class="tag a">Prospect</span>'
 '<p>Undefeated UFC newcomer who takes the Paris bout with Nathaniel Wood on short notice after Mairon Santos withdrew with illness. '
 'His record was not stated in the source that announced the booking, so no number is printed here.</p></div>'
 '</div>'
 '<div class="note"><b>Contender Series, refused again.</b> Week 5 of the 2026 season is dated <b>September 8</b> by this run&rsquo;s sources and '
 'was dated <b>September 15</b> by last run&rsquo;s; both are printed, neither adopted. A contract-winners list surfaced this run naming five '
 'signings, but <b>the names in it do not correspond to any fighter on the Week 5 card in the same search</b>, which means it belongs to a '
 'different event. Nothing from it is published.</div>')

mm.append('<h2 class="sec">Around the Sport</h2><div class="panel"><ul class="b">'
 '<li><b>Paris start times are unusual and worth flagging:</b> prelims 12 PM ET / 9 AM PT, main card 3 PM ET / 12 PM PT, whole card on Paramount+.</li>'
 '<li><b>The Paris main event is officially billed &ldquo;Hooker vs. Parnasse&rdquo;</b> &mdash; the veteran&rsquo;s name first, despite the '
 'newcomer being a better than 6-to-1 favourite.</li>'
 '<li><b>Song Yadong&rsquo;s Shanghai knockout reshapes the bantamweight picture</b> at the top of a division whose champion, Petr Yan, is booked '
 'to defend at UFC 333 in October.</li>'
 '<li><b>A &ldquo;Dana White announces&rdquo; fight slate is refused for a second run.</b> It presented Harrison vs. Nunes, O&rsquo;Malley vs. '
 'Song Yadong and Grasso vs. Namajunas as current news, but it is undated and describes &ldquo;the first slate of fights for 2026.&rdquo; '
 'The Harrison&ndash;Nunes booking was cancelled after Harrison withdrew for neck surgery, and an O&rsquo;Malley&ndash;Song booking cannot be '
 'current news four days after Song fought Umar Nurmagomedov.</li>'
 '</ul></div>')

mm.append('<h2 class="sec">Rankings &amp; Business</h2><div class="panel">'
 '<p><b>Rankings movement.</b> Song Yadong&rsquo;s second-round knockout of Umar Nurmagomedov is the only ranked result inside the last week '
 'confirmed this run. No updated official ranking numbers were sourced, so none are printed.</p>'
 '<p><b>Business &amp; broadcast.</b> The entire 2026 UFC schedule streams on Paramount+, including numbered events &mdash; the Paris card '
 'carries no pay-per-view. <b>No viewership, gate or TKO Group financial figures were stated in any source fetched this run, so none appear '
 'on this page.</b></p></div>')

mm.append('<h2 class="sec">Champions Board</h2><div class="tblwrap"><table>'
 '<tr><th>Division</th><th>Champion</th><th>Note</th></tr>'
 '<tr><td>Heavyweight</td><td class="win">Tom Aspinall</td><td>Undisputed. <b>Interim:</b> Ciryl Gane, KO2 of Alex Pereira at Freedom 250, June 14 2026.</td></tr>'
 '<tr><td>Light Heavyweight</td><td class="win">Carlos Ulberg</td><td>Won the vacant title, KO1 over Ji&#345;&iacute; Proch&aacute;zka, UFC 327, April 11 2026.</td></tr>'
 '<tr><td>Middleweight</td><td class="win">Sean Strickland</td><td>Split-decision upset of Khamzat Chimaev, UFC 328, May 9 2026. Two-time champion.</td></tr>'
 '<tr><td>Welterweight</td><td class="win">Islam Makhachev</td><td>Two-division champion. One defence &mdash; UD over Ian Machado Garry, UFC 330, Aug 15 2026, a 17th straight UFC win.</td></tr>'
 '<tr><td>Lightweight</td><td class="win">Justin Gaethje</td><td>TKO4 of Ilia Topuria, Freedom 250, June 14 2026.</td></tr>'
 '<tr><td>Featherweight</td><td class="win">Alexander Volkanovski</td><td><b>Not vacant.</b> Defended by UD over Diego Lopes, UFC 325, Jan 31 2026. Booked to defend vs. Movsar Evloev, UFC 333, Oct 24.</td></tr>'
 '<tr><td>Bantamweight</td><td class="win">Petr Yan</td><td>UD over Merab Dvalishvili, UFC 323, Dec 6 2025. Booked to defend at UFC 333.</td></tr>'
 '<tr><td>Flyweight</td><td class="win">Joshua Van</td><td>TKO1 of Alexandre Pantoja, UFC 323; defended TKO5 over Tatsuro Taira, UFC 328. Rematches Pantoja at UFC 331, Sept 19.</td></tr>'
 '<tr><td>Women&rsquo;s Bantamweight</td><td class="win">Kayla Harrison</td><td>Sub2 of Julianna Pe&ntilde;a, UFC 316. <b>Zero defences</b> &mdash; the UFC 324 defence vs. Amanda Nunes was cancelled after Harrison withdrew for neck surgery.</td></tr>'
 '<tr><td>Women&rsquo;s Flyweight</td><td class="win">Valentina Shevchenko</td><td>&mdash;</td></tr>'
 '<tr><td>Women&rsquo;s Strawweight</td><td class="win">Mackenzie Dern</td><td>UD over Virna Jandiroba, UFC 321. One defence &mdash; UD over Gillian Robertson, UFC 330, Aug 15 2026.</td></tr>'
 '<tr><td>Women&rsquo;s Featherweight</td><td class="nc">Vacant</td><td>Correctly returned as vacant again this run.</td></tr>'
 '</table></div>'
 '<div class="note"><b>The stale middleweight cell came back for a twenty-fourth time.</b> The champions list fetched this run offered twelve '
 'cells and got eleven of them right; the one it got wrong is the same one it has always got wrong &mdash; it lists <b>Khamzat Chimaev</b> at '
 'middleweight. Chimaev lost the belt by split decision to <b>Sean Strickland</b> at UFC 328 on May 9, 2026. The table above uses Strickland. '
 'Carlos Ulberg at light heavyweight, Alexander Volkanovski at featherweight and a vacant women&rsquo;s featherweight title were all returned '
 'correctly and independently re-confirmed this run.</div>')

mm.append(srcs([
 ("https://www.ufc.com/news/updates-ufc-fight-night-paris-2026","UFC.com &mdash; Updates to UFC Paris [Santos out, Andrusca in]"),
 ("https://www.ufc.com/event/ufc-fight-night-september-05-2026","UFC.com &mdash; UFC Fight Night: Hooker vs. Parnasse, Sept 5 2026"),
 ("https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse","Wikipedia &mdash; UFC Fight Night: Hooker vs. Parnasse (Fight Night 287, Accor Arena)"),
 ("https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365","Rotowire &mdash; Hooker vs. Parnasse odds, Sept 5 2026"),
 ("https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/","MMA Odds Breaker &mdash; Opening betting odds for UFC Paris"),
 ("https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage","UFC.com &mdash; UFC Shanghai bonus coverage"),
 ("https://sports.yahoo.com/articles/ufc-shanghai-bonuses-yadong-hasan-180000434.html","Yahoo Sports &mdash; UFC Shanghai bonuses: Yadong, Hasan lead $100K winners"),
 ("https://www.ufc.com/event/ufc-fight-night-august-29-2026","UFC.com &mdash; UFC Fight Night: Nurmagomedov vs. Song, Aug 29 2026"),
 ("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions","ESPN &mdash; Current and all-time UFC champions"),
 ("https://www.espn.com/mma/schedule","ESPN &mdash; MMA schedule, 2026 season"),
 ("https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/","Paramount+ &mdash; UFC 2026 schedule and start times"),
 ("https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5","Tapology &mdash; Contender Series 2026 Week 5 [date conflict, see note]"),
])+'<div class="disc">Cards and bouts are subject to change. Odds are a snapshot of the moneyline at the time of the fetch and move continuously; '
 'they are reported here as market information, not as betting advice.</div></footer>')

open(os.path.join(OUT,'mma-briefing.html'),'w').write(page(
 "The Octagon — Daily Briefings",MMCSS,
 mast("The Octagon","Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting","Tale of the Tape",MM_TLDR),
 ''.join(mm)+CDNJS,"mma-briefing.html"))
print("mma ok")

# ============================================================ INDEX
IX_EXTRA=""".big{display:grid;gap:15px}
.big .card{padding:20px 22px;border-radius:14px}
.big .card h3{font-size:22px;margin-bottom:9px}
.big .card .k{font-size:11.5px;letter-spacing:.16em;margin-bottom:9px}
.big .card p{font-size:15px;color:#cfcdc9;margin-bottom:12px}
.rd{font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase}
.c-sec{border-left:3px solid #22d3a8}.c-sec .k,.c-sec .rd{color:#22d3a8}
.c-sec:hover{border-color:#22d3a8;border-left-color:#22d3a8}
.c-mkt{border-left:3px solid #caa64a}.c-mkt .k,.c-mkt .rd{color:#caa64a}
.c-mkt h3{font-family:Georgia,'Times New Roman',serif}
.c-mkt:hover{border-color:#caa64a;border-left-color:#caa64a}
.c-mma{border-left:3px solid #e84545}.c-mma .k,.c-mma .rd{color:#ff8a5c}
.c-mma:hover{border-color:#e84545;border-left-color:#e84545}
"""
IXCSS=css_for("#0b0b0c","#151517","#26262a","#9aa7b8","#c9d3e0",IX_EXTRA)

ix=('<div class="big">'
 '<div class="card c-sec"><div class="k">&#9960; The Cyber Wire &middot; The Wire</div>'
 '<h3>Switchvox flaw scored 9.3 as reverse shells spread; MLflow deadline is today</h3>'
 '<p>CISA has given federal agencies until Friday to fix an actively exploited Sangoma Switchvox flaw now scored 9.3 and being used to drop '
 'reverse shells, while an MLflow credential-theft bug hits its federal deadline today and McKesson confirms a breach ShinyHunters says runs '
 'to 284 million patient records.</p><a class="rd" href="cyber-briefing.html">Read the briefing &rarr;</a></div>'
 '<div class="card c-mkt"><div class="k">&#9650; The Closing Bell &middot; The Tape</div>'
 '<h3>A three-day skid ends, and Dell&rsquo;s AI backlog is why</h3>'
 '<p>Wall Street snapped a three-day losing streak at Wednesday&rsquo;s close &mdash; S&amp;P 500 +0.46%, Dow +295.07 points, Nasdaq Composite '
 '+0.45% &mdash; led by Dell, the index&rsquo;s best performer on record AI-server orders, while Palo Alto Networks fell roughly 11% and '
 'Broadcom slipped after the bell.</p><a class="rd" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>'
 '<div class="card c-mma"><div class="k">&#8856; The Octagon &middot; Tale of the Tape</div>'
 '<h3>Paris is three days out and the card just changed</h3>'
 '<p>UFC Paris is three days out and the card just changed &mdash; Mairon Santos is off it with illness &mdash; while debutant Salahdine '
 'Parnasse has been bet from &minus;357 up to about &minus;667 over Dan Hooker in a main event that starts at the unusual hour of 3 PM ET.</p>'
 '<a class="rd" href="mma-briefing.html">Read the briefing &rarr;</a></div>'
 '</div>'
 '<div class="note" style="margin-top:22px">Three briefings, rebuilt from live sources every 30 minutes between 8 AM and 6 PM ET. '
 'Every figure on every page traces to a source fetched during the run that published it; where sources disagree, the disagreement is printed '
 'rather than resolved silently. Past editions are kept in the <a href="archive.html">Archive</a>.</div>')

open(os.path.join(OUT,'index.html'),'w').write(page(
 "Daily Briefings",IXCSS,
 mast("Daily Briefings","Security, markets and MMA &mdash; rebuilt from live sources through the day"),
 ix,"index.html"))
print("index ok")
