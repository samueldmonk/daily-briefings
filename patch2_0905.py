# -*- coding: utf-8 -*-
"""Wall Street + MMA edits for the 9:05 AM ET edition."""
import io, sys

P = "/sessions/inspiring-practical-pasteur/build_0905.py"
s = io.open(P, encoding="utf-8").read()
n = 0

def rep(old, new, label):
    global s, n
    if old not in s:
        print("MISS:", label); sys.exit(1)
    if s.count(old) != 1:
        print("AMBIG(%d):" % s.count(old), label); sys.exit(1)
    s = s.replace(old, new)
    n += 1
    print("ok:", label)

Q = chr(39)

# ============================================================ WALL STREET: The Lead
rep("""    b.append('<div class="callout"><div class="k">Pre-open &middot; ~8:40 AM ET</div>'
             '<h3>Dow futures inch up, Nasdaq contracts slip, and oil keeps its war premium</h3>'
             '<p>U.S. stock futures are narrowly mixed early Thursday. Dow futures are up about 0.2%, at '
             '53,274.00 for a gain of 153.00 points or 0.29%; S&amp;P 500 futures are little changed at '
             '7,679.50, up 3.00 points or 0.04%; and Nasdaq 100 contracts sit just below the flat line at '
             '29,130.50, down 55.75 or 0.19%. A separate pre-market index reading has the S&amp;P 500 '
             '+0.12%, the Nasdaq 100 +0.04%, the Dow +0.25% and the Russell 2000 &minus;0.09%.</p>'""",
    """    b.append('<div class="callout"><div class="k">Pre-open &middot; ~9:05 AM ET</div>'
             '<h3>Futures firm up into the bell as claims land at 206,000</h3>'
             '<p>U.S. stock futures have turned higher across the board in the last half hour before the '
             'open. Dow futures are at <b>53,430.00</b>, up 309.00 points or <b>0.58%</b>; S&amp;P 500 '
             'futures at <b>7,699.50</b>, up 23.00 or <b>0.30%</b>; Nasdaq futures at <b>29,233.00</b>, '
             'up 46.75 or <b>0.16%</b>. Separately, Dow futures are described as up 0.2% with S&amp;P 500 '
             'contracts little changed and Nasdaq 100 contracts just below flat &mdash; a softer '
             'characterisation than the point-level quotes above, printed rather than reconciled.</p>'
             '<p>The Labor Department released its weekly claims report at 8:30 AM ET: initial jobless '
             'claims for the week ending <b>August 29</b> rose to <b>206,000</b>, above the 205,000 '
             'consensus, against <b>204,000</b> the week before &mdash; itself revised up from the '
             '203,000 first reported. The 8:16 and 8:49 AM editions of this page withheld the print '
             'because no source fetched for them stated it; it is published here on a fetch that '
             'does.</p>'""",
    "ws lead p1")

rep("""             'rates need to move higher." Brent is the contested figure this morning &mdash; see the '
             'rates and commodities table. The Labor Department released the week-ending-August-29 '
             'jobless claims report at 8:30 AM ET; no actual figure appeared in anything fetched for this '
             'edition, so none is printed. Friday\\'s August employment report is the last labour reading '
             'the FOMC sees before its September 16 decision.</p>'
             '<p class="note">These futures readings differ from the 8:16 AM edition\\'s (Dow +0.07%, '
             'S&amp;P 500 &minus;0.05%, Nasdaq 100 &minus;0.11%). That is drift across roughly twenty '
             'minutes of pre-market trade, not a disagreement between sources. Nothing on this page is a '
             'live Thursday session price &mdash; the opening bell is 9:30 AM ET.</p></div>')""",
    """             'rates need to move higher." Brent is the contested figure this morning &mdash; see the '
             'rates and commodities table. Gold futures are up 1.81% at $4,494.70 an ounce in early '
             'trading and silver futures up 1.42% at $66.39. Friday\\'s August employment report is the '
             'last labour reading the FOMC sees before its September 16 decision.</p>'
             '<p class="note">Futures have moved with each edition this morning: Dow contracts read '
             '+0.07% at 8:16 AM, +0.29% at 8:49 AM and +0.58% here. That is drift across pre-market '
             'trade, not a disagreement between sources. Nothing on this page is a live Thursday session '
             'price &mdash; the opening bell is 9:30 AM ET.</p></div>')""",
    "ws lead p2")

# ============================================================ WALL STREET: movers
rep("""    b.append('<div class="card"><span class="tag new">New</span><span class="tag c">&minus;2%+</span>'
             '<h4>Moderna</h4><p>Off more than 2% pre-market after Rothschild &amp; Co Redburn '
             'downgraded the stock to sell. No price target was stated in the material fetched this run, '
             'so none is printed.</p></div>')
    b.append('<div class="card"><span class="tag c">&minus;7%</span>'
             '<h4>The Campbell\\'s Company</h4><p>Down almost 7% pre-market after issuing fiscal 2027 '
             'earnings guidance below expectations. No guidance figures were stated in the material '
             'fetched this run, so none are printed.</p></div>')""",
    """    b.append('<div class="card"><span class="tag new">Now with figures</span><span class="tag c">&minus;7%</span>'
             '<h4>The Campbell\\'s Company</h4><p>Down almost 7% pre-market after guiding fiscal 2027 '
             'earnings to <b>$1.65 to $1.80 a share</b> against a FactSet consensus of <b>$1.83</b>. The '
             'two earlier editions today carried this move without figures because none had been '
             'sourced; the range is published here on a fetch that states it.</p></div>')""",
    "ws movers campbell")

rep("""    b.append('<div class="card"><span class="tag a">Software bid</span>'
             '<h4>Datadog and ServiceNow</h4><p>Snowflake\\'s rally lifted its software peers, with Datadog '
             'up more than 5% and ServiceNow up 3%. Hewlett Packard Enterprise, carried in the earlier '
             'edition at &minus;3%, was not restated in this run\\'s searches and is therefore not '
             'repeated with a number.</p></div>')""",
    """    b.append('<div class="card"><span class="tag a">Software bid</span>'
             '<h4>Datadog, ServiceNow and Salesforce</h4><p>Snowflake\\'s rally lifted its software peers: '
             'Datadog up more than 5%, ServiceNow up 3% and Salesforce up just over 1.5%. Salesforce is '
             'new to this list on the fetch made for this edition.</p></div>')
    b.append('<div class="card"><span class="tag c">&minus;3%</span>'
             '<h4>Hewlett Packard Enterprise</h4><p>The enterprise technology company slipped 3% '
             'pre-market. The figure was not restated in the 8:49 AM edition and is carried here only '
             'because this run\\'s fetch states it again.</p></div>')""",
    "ws movers software")

rep("""    b.append('<div class="note">Snowflake is the largest pre-market move among the large-cap names in the section above. It is <b>not</b> the largest move in the pre-market return overall: the same list carries Ultragenyx Pharmaceutical down 44.40% and Generation Income Properties up 44.46%, with Gelteq +35%, Tilly&#39;s +29.40% and Ethan Allen Interiors &minus;11.01%. Those are thinly traded small caps and are noted here only so the superlative above is not overstated.</div>')""",
    """    b.append('<div class="note">Snowflake is the largest pre-market move among the large-cap names in '
             'the section above, which are the names this run\\'s movers fetch identified. No claim is '
             'made about the pre-market list as a whole: an earlier edition today sourced several '
             'thinly traded small caps with larger percentage moves, and those figures were not '
             're-fetched for this edition, so they are not restated here.</div>')""",
    "ws chart note")

# ============================================================ WALL STREET: sector note
rep("""    b.append('<div class="note">Single-session sector leadership is <b>not</b> asserted for a twelfth '
             'consecutive edition. This run\\'s sector return offers single-day leader and laggard readings '
             'inside a piece that also states the S&amp;P 500 "declined 0.71% to 7,631.47" on the day '
             'in question. That '
             'contradicts Wednesday\\'s verified close of 7,666.60, up 0.46%, so the session cannot be '
             'pinned and the daily figures are not published. Only the year-to-date readings are firm, '
             'and even those return two ways for energy: <span class="up">+43% YTD</span> in this run\\'s '
             'return and <span class="up">+42.32% YTD</span> for XLE in the standing record &mdash; both '
             'printed, neither adopted. Consumer discretionary is <span class="down">&minus;2.3% '
             'YTD</span>; materials <span class="up">+15.86% YTD</span>.</div>')""",
    """    b.append('<div class="note">Single-session sector leadership is <b>not</b> asserted for a '
             'thirteenth consecutive edition. The only same-day reading this run\\'s sector fetch offers '
             'is energy up 1.3% on <b>August 31</b> &mdash; the last trading day before September 2, and '
             'so not Wednesday\\'s session at all. Year-to-date readings are the firm ones: energy leads, '
             'returning as <span class="up">+43% YTD</span> for the sector and <span class="up">+42.32% '
             'YTD</span> for the XLE ETF in the same return &mdash; both printed, neither adopted, and '
             'XLE is separately given as +40.82% over the past year. At the other end, communication '
             'services (XLC) is <span class="down">&minus;5.60% YTD</span> and consumer discretionary '
             '(XLY) <span class="down">&minus;3.02% YTD</span> &mdash; the latter against '
             '&minus;2.3% in the 8:49 AM edition, printed, not adopted. The materials figure carried '
             'earlier today was not re-sourced for this edition and is not repeated.</div>')""",
    "ws sector note")

# ============================================================ WALL STREET: scorecard note
rep("""    b.append('<div class="note">These three closes have now returned identical on seven consecutive '
             'fetches across editions, this run from The Globe and Mail, TheStreet and CNBC. Newly '
             'sourced framing: stocks rose Wednesday as Treasury yields "took a breather" from the '
             'run-up that had carried them to multiyear highs. The streak framing still does not agree '
             '&mdash; one reading has Wednesday snapping a <b>two-day</b> losing streak, CNBC coverage a '
             '<b>three-day</b> one; both are printed, neither adopted. Only Wednesday\\'s official closes '
             'are listed &mdash; earlier sessions in the week were not re-sourced in this run.</div>')""",
    """    b.append('<div class="note">These three closes have now returned identical on <b>eight</b> '
             'consecutive fetches across editions. On the streak framing, this run\\'s return says all '
             'three indices snapped a <b>three-day</b> losing streak, matching CNBC and against the '
             '<b>two-day</b> reading carried in both earlier editions today. Neither is adopted, but the '
             'three-day version has now returned on more fetches than the two-day one. Only Wednesday\\'s '
             'official closes are listed &mdash; earlier sessions in the week were not re-sourced in '
             'this run.</div>')""",
    "ws scorecard note")

# ============================================================ WALL STREET: WTI row
rep("""             '<tr><td>WTI crude</td><td class="mono">$90.76 (Sept 2 close, +0.60%)</td>'
             '<td>Historical data for Wednesday. A Thursday futures quote returned this run showed '
             '$91.01; the earlier edition carried $90.51 and $89.62 from other feeds. No single Thursday '
             'level is adopted.</td></tr>'""",
    """             '<tr><td>WTI crude</td><td class="mono">$90.87, +0.72%</td>'
             '<td>This run\\'s quote. Earlier editions today carried $90.76 as the September 2 close, a '
             'Thursday futures quote of $91.01, and $90.51 and $89.62 from other feeds. The readings sit '
             'within about $1.25 of each other; no single Thursday level is adopted.</td></tr>'""",
    "ws wti row")

# ============================================================ WALL STREET: On the Radar
rep("""             '<li><b>Released this morning &mdash; initial jobless claims.</b> The Labor Department put '
             'out the weekly claims report for the week ending August 29 at 8:30 AM ET. Consensus was '
             '205,000 against 203,000 the week before. The actual print did not appear in any source '
             'fetched for this edition, so no figure is published here.</li>'""",
    """             '<li><b>Released this morning &mdash; initial jobless claims came in at 206,000.</b> The '
             'week-ending-August-29 print landed above the 205,000 consensus and above the prior week\\'s '
             '204,000, which was itself revised up from 203,000.</li>'""",
    "ws radar claims")

rep("""             '<li><b>Friday, September 4, 8:30 AM ET &mdash; the August employment report.</b> Kiplinger '
             'reports economists expect about 58,000 jobs added and unemployment holding at 4.1%. It is '
             'the last labour reading the FOMC sees before its decision.</li>'""",
    """             '<li><b>Friday, September 4, 8:30 AM ET &mdash; the August employment report.</b> The '
             'forecasts fetched for this edition spread widely: about <b>58,000</b> jobs added in one '
             'consensus reading and <b>53,000</b> in another, against <b>80,000</b> from Wells Fargo '
             'economists and a below-consensus <b>25,000 decline</b> from Fifth Third. Unemployment is '
             'expected to hold at <b>4.1%</b>. July payrolls fell 23,000, and Wednesday\\'s ADP report '
             'put private payrolls up just <b>38,000</b> in August, fewer than expected. It is the last '
             'labour reading the FOMC sees before its decision.</li>'""",
    "ws radar nfp")

print("ws edits done")

# ============================================================ MMA: top story
rep("""             '<p>Valentina Shevchenko is out of UFC 332 with an injury, and the promotion is still '
             'searching for a headliner for the card at the Delta Center in Salt Lake City on Saturday, '
             'October 3. Reporting this week says the UFC is working on an interim women\\'s flyweight '
             'title fight between <b>Natalia Silva</b> and <b>Wang Cong</b> as the replacement main '
             'event.</p>'""",
    """             '<p>Valentina Shevchenko is out of UFC 332 with an injury, and the promotion is still '
             'searching for a headliner for the card at the Delta Center in Salt Lake City on Saturday, '
             'October 3. Coverage fetched for this edition puts it plainly: the event is a month away and '
             'has <b>neither a main event nor a co-main event</b>. Reporting this week says the UFC is '
             'working on an interim women\\'s flyweight title fight between <b>Natalia Silva</b> and '
             '<b>Wang Cong</b> as the replacement main event.</p>'""",
    "mma top story")

# ============================================================ MMA: Paris odds
rep("""             'lightweight champion &mdash; not through the Contender Series. Far&egrave;s Ziam vs. Axel '
             'Sola sits on the main card.<br><b>Odds:</b> Parnasse &minus;600 / Hooker +440 '
             '(DraftKings); some books show &minus;500 / +400. Ziam is quoted &minus;145 against Sola at '
             '+125 this run, against &minus;155 in the earlier edition &mdash; both printed, neither '
             'adopted. The main-event total sits at 3.5 rounds, under at &minus;260.</p></div>')""",
    """             'lightweight champion &mdash; not through the Contender Series. Far&egrave;s Ziam vs. Axel '
             'Sola sits on the main card.<br><b>Odds:</b> Parnasse &minus;600 / Hooker +440 '
             '(DraftKings); another book is quoted at &minus;625 / +450, and a third reading has '
             '&minus;500 / +400. All three are printed; none is adopted. The line has moved a long way '
             'from the opening price of Parnasse &minus;357 / Hooker +275; one implied-probability '
             'reading puts Parnasse at 83%. The Ziam quote returned &minus;145 / +125 in the previous '
             'edition against &minus;155 earlier, and was not restated this run.</p></div>')""",
    "mma paris odds")

# ============================================================ MMA: Noche card detail
rep("""    b.append('<div class="card"><div class="k">Sat, Sept 12 &middot; Desert Diamond Arena, Glendale</div>'
             '<h4>Noche UFC: Silva vs. Delgado</h4>'
             '<p>Jean Silva headlines against Jose Miguel Delgado, who stepped in after Yair Rodr&iacute;guez '
             'was forced out injured. The card also carries Waldo Cortes-Acosta vs. Curtis Blaydes, Manon '
             'Fiorot vs. Alexa Grasso and Brandon Moreno vs. Joseph Morales. No headline odds were stated '
             'in the material fetched this run, so none are printed.</p></div>')""",
    """    b.append('<div class="card"><div class="k">Sat, Sept 12 &middot; Desert Diamond Arena, Glendale</div>'
             '<h4>Noche UFC: Silva vs. Delgado</h4>'
             '<p>Brazil\\'s Jean Silva headlines at featherweight against Arizona\\'s Jose Miguel Delgado, '
             'who stepped in after Yair Rodr&iacute;guez was forced out injured. The card also carries '
             'Waldo Cortes-Acosta vs. Curtis Blaydes at heavyweight, Manon Fiorot vs. Alexa Grasso at '
             'women\\'s flyweight, Brandon Moreno vs. Joseph Morales at flyweight, David Mart&iacute;nez '
             'vs. Dan Ige at bantamweight and Tommy McMillen vs. Marwan Rahiki at featherweight. Doors '
             'open 10:00 AM PT, prelims 11:00 AM PT, main card live on Paramount+ at 2:00 PM PT. No '
             'headline odds were stated in the material fetched this run, so none are printed.</p></div>')""",
    "mma noche")

# ============================================================ MMA: add Sept 26 card
rep("""    b.append('<div class="card"><div class="k">Sat, Oct 3 &middot; Delta Center, Salt Lake City</div>'
             '<h4>UFC 332 &mdash; main event TBD</h4>'""",
    """    b.append('<div class="card"><div class="k">Sat, Sept 26 &middot; Meta APEX, Las Vegas</div>'
             '<h4>UFC Fight Night: Rosas Jr. vs. Barcelos</h4>'
             '<p>Also billed UFC Vegas 121 and UFC Fight Night 289. Twenty-one-year-old bantamweight '
             'prospect Raul Rosas Jr. headlines his first UFC card against Brazilian veteran Raoni '
             'Barcelos, an eighteen-year age gap. The bantamweight and women\\'s strawweight finals of '
             'The Ultimate Fighter: Team Cormier vs. Team Bisping are also scheduled for this event. '
             'Prelims 5 PM ET, main card 8 PM ET on Paramount+. No headline odds stated this run.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Oct 3 &middot; Delta Center, Salt Lake City</div>'
             '<h4>UFC 332 &mdash; main event TBD</h4>'""",
    "mma sept26 card")

# ============================================================ MMA: DWCS Week 5 full names
rep("""             '<p>Season 10, Week 5 runs Tuesday, September 8 at 7:00 PM ET from the Meta APEX in Las '
             'Vegas on Paramount+, headlined by Berisha against Pasley at 205 pounds &mdash; the listing '
             'gives surnames only, so no first names are supplied. That fills the gap '
             'this desk flagged earlier today, when no date had been sourced for the week between the '
             'September 1 card and Week 6 on September 15.</p></div>')""",
    """            '<p>Season 10, Week 5 runs Tuesday, September 8 from the Meta APEX in Las Vegas &mdash; '
             'five fights, headlined by undefeated light heavyweights <b>Quentin Pasley</b> and '
             '<b>Arlind Berisha</b>. The rest of the card: Isaac Moreno vs. Reginaldo Junior at '
             'welterweight, Martin Kozak vs. Christian Echols at middleweight, Apollo Gomes vs. Won Il '
             'Kwon at bantamweight and Colton Loud vs. Christian Natividad at flyweight. The earlier '
             'editions today had surnames only; full names come from this run\\'s fetch. Broadcast '
             'listings disagree &mdash; one carries the card on ESPN, another on Paramount+ at 7:00 PM '
             '&mdash; and neither is adopted.</p></div>')""",
    "mma dwcs wk5")

# ============================================================ MMA: business figures
rep("""             '<li>Paramount is in the first year of a <b>seven-year, $7.7 billion</b> media-rights deal '
             'with the UFC, which is owned by TKO Group. UFC 331 and the Paris card are Paramount+ '
             'events.</li>'
             '<li>TKO\\'s own investor release puts UFC Freedom 250 &mdash; the White House card on June 14 '
             '&mdash; at <b>34 million total global viewers</b>, including 17 million across the U.S. and '
             'Latin America on Paramount+. The U.S. average is disputed: one return gives 7.0 million, '
             'described as the most-watched UFC event domestically, while The Hollywood Reporter\\'s '
             'headline says the card averaged 8 million viewers on Paramount+. Both are printed; neither '
             'is adopted.</li>'
             '<li>No gate figure was stated in anything fetched this run, so none is printed.</li>'""",
    """             '<li>Paramount is in the first year of a <b>seven-year, $7.7 billion</b> U.S. media-rights '
             'deal with TKO Group\\'s UFC, announced in August 2025 and beginning this year &mdash; an '
             'average of <b>$1.1 billion a year</b>, against the roughly $550 million a year ESPN was '
             'reported to pay under the previous arrangement.</li>'
             '<li>The deal covers all <b>43 annual UFC live events</b>, streamed exclusively in the U.S. '
             'on Paramount+: <b>30 Fight Nights and 13 marquee events</b> a year across CBS and '
             'Paramount+. It ends the pay-per-view model ESPN used, with events carried at no extra '
             'charge.</li>'
             '<li>The UFC Freedom 250 viewership figures carried in the 8:49 AM edition were not '
             'restated in this run\\'s fetch and are not repeated here. No gate figure was stated in '
             'anything fetched this run, so none is printed.</li>'""",
    "mma business")

# ============================================================ MMA: champions note (2 wrong cells)
rep("""    b.append('<div class="note"><b>Corrected again this run:</b> the aggregated champions list fetched for '
             'this edition returned Khamzat Chimaev at middleweight for the twenty-ninth time, dating his '
             'reign to August 16, 2025. It is wrong. Strickland\\'s title win was re-verified on a fresh '
             'fetch this run against ESPN ("Strickland stuns rival Chimaev"), CBS Sports, Sky Sports and '
             'Al Jazeera &mdash; a split decision, two judges 48-47 Strickland and one 48-47 Chimaev, at '
             'the Prudential Center in Newark. The list got eleven of its twelve cells right. Sources '
             'also disagree on the date of UFC 328 &mdash; Al Jazeera files it under May 10, 2026, while '
             'this desk\\'s standing record is May 9, 2026; the discrepancy is printed rather than '
             'silently resolved, and no weekday is attached to either.</div>')""",
    """    b.append('<div class="note"><b>Corrected again this run &mdash; and this time two cells were '
             'wrong, not one.</b> The aggregated champions list fetched for this edition returned '
             '<b>Khamzat Chimaev</b> at middleweight for the thirtieth time, and also returned '
             '<b>Alex Pereira</b> at light heavyweight, dating that reign to a win over Magomed Ankalaev '
             'in October 2025. Both are wrong, and both were re-verified against fresh fetches this run. '
             'Middleweight: Sean Strickland took the belt from Chimaev by split decision at UFC 328 at '
             'the Prudential Center in Newark &mdash; two judges 48-47 Strickland, one 48-47 Chimaev '
             '&mdash; per ESPN ("Strickland stuns rival Chimaev"), Bleacher Report, CBS Sports, Sky '
             'Sports and Al Jazeera; Strickland moved to 31-7 and handed Chimaev, 17-1, his first defeat. '
             'Light heavyweight: <b>Carlos Ulberg</b> knocked out Ji&#345;&iacute; Proch&aacute;zka at '
             '3:45 of round one at UFC 327 at the Kaseya Center in Miami to win the <b>vacant</b> belt '
             '&mdash; he blew out his right knee in the opening minute and won with a left hook while '
             'cornered &mdash; per ESPN, UFC.com and Al Jazeera. He is the third City Kickboxing fighter '
             'to win a UFC title, after Alexander Volkanovski and Israel Adesanya. Ten of the list\\'s '
             'twelve cells were right. Sources also disagree on the date of UFC 328 &mdash; Al Jazeera '
             'files it under May 10, 2026, while this desk\\'s standing record is May 9, 2026; the '
             'discrepancy is printed rather than silently resolved, and no weekday is attached to '
             'either.</div>')""",
    "mma champions note")

# MMA sources additions
rep("""        ("Sky Sports &mdash; Strickland defeats Chimaev at UFC 328 to regain the middleweight title",""",
    """        ("ESPN &mdash; UFC 327 results: Carlos Ulberg stuns Ji&#345;&iacute; Proch&aacute;zka to win the light heavyweight title",
         "https://www.espn.com/mma/story/_/id/48432076/ufc-327-live-results-analysis-ji%C5%99i-prochazka-vs-carlos-ulberg-light-heavyweight-championship"),
        ("UFC.com &mdash; UFC 327: Proch&aacute;zka vs Ulberg results",
         "https://www.ufc.com/news/ufc-327-results-prochazka-vs-ulberg-main-card-highlights-winners-interviews"),
        ("Al Jazeera &mdash; UFC 327: Ulberg wins the light-heavyweight belt with a knockout",
         "https://www.aljazeera.com/sports/2026/4/12/ufc-327-ulberg-wins-light-heavyweight-belt-with-knockout-in-front-of-trump"),
        ("ESPN &mdash; Dana White&#39;s Contender Series Season 10 Week 5 fight centre",
         "https://www.espn.com/mma/fightcenter/_/id/600060736/league/ufc"),
        ("Tapology &mdash; Contender Series 2026: Week 5",
         "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
        ("Wikipedia &mdash; UFC Fight Night: Silva vs. Delgado (card and start times)",
         "https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado"),
        ("Yahoo Sports &mdash; Raul Rosas Jr. vs. Raoni Barcelos headlines UFC Vegas 121 on Sept. 26",
         "https://sports.yahoo.com/articles/raul-rosas-jr-vs-raoni-220000231.html"),
        ("UFC.com &mdash; UFC Fight Night, September 26, 2026",
         "https://www.ufc.com/event/ufc-fight-night-september-26-2026"),
        ("Rotowire &mdash; Hooker vs. Parnasse odds, September 5, 2026",
         "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
        ("MMA Odds Breaker &mdash; Opening betting odds for UFC Paris: Hooker vs. Parnasse",
         "https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/"),
        ("CBS News &mdash; Paramount acquires UFC rights in a seven-year, $7.7 billion deal with TKO",
         "https://www.cbsnews.com/news/ufc-paramount-plus-deal-2026-streaming-cbs/"),
        ("CNBC &mdash; Paramount buys UFC rights in $7.7 billion, seven-year deal",
         "https://www.cnbc.com/2025/08/11/paramount-buys-ufc-rights-skydance-merger.html"),
        ("Sportico &mdash; UFC media deal: $7.7 billion Paramount rights fee ends pay-per-views",
         "https://www.sportico.com/leagues/other-sports/2025/ufc-paramount-cbs-media-deal-streaming-contract-2026-1234866546/"),
        ("Sky Sports &mdash; Strickland defeats Chimaev at UFC 328 to regain the middleweight title",""",
    "mma sources")

io.open(P, "w", encoding="utf-8").write(s)
print("PATCH 2 COMPLETE:", n, "edits")
