# -*- coding: utf-8 -*-
"""11:05 AM edition edits. Partial-write semantics: apply what matches, REPORT misses, always write."""
import io, sys, re
O="/sessions/tender-hopeful-newton/mnt/outputs/"

class Ed:
    def __init__(self, fn):
        self.fn=fn; self.s=io.open(O+fn,encoding='utf-8').read(); self.ok=[]; self.miss=[]
    def rep(self, name, old, new, count=1):
        if old in self.s:
            self.s=self.s.replace(old,new,count); self.ok.append(name)
        else:
            self.miss.append(name)
    def hasnt(self, name, phrase):
        if phrase in self.s: self.miss.append("STALE:"+name+" -> "+phrase[:70])
    def has(self, name, phrase):
        if phrase not in self.s: self.miss.append("ABSENT:"+name+" -> "+phrase[:70])
    def write(self):
        io.open(O+self.fn,'w',encoding='utf-8').write(self.s)
        print("== %s : %d applied, %d issues"%(self.fn,len(self.ok),len(self.miss)))
        for m in self.miss: print("   !!",m)

# ---------------------------------------------------------------- CYBER
c=Ed("cyber-briefing.html")

c.rep("cy.freshline",
 '<div class="freshline" id="freshline">Data as of 10:50 AM ET</div>',
 '<div class="freshline" id="freshline">Data as of 11:05 AM ET</div>')

c.rep("cy.tldr",
 'and Ubiquiti has patched three separate maximum-severity UniFi flaws.</span>',
 'Ubiquiti has patched three separate maximum-severity UniFi flaws, and a 9.8-rated six-step '
 'chain in the Avada WordPress theme &mdash; found by an AI agent, not a person &mdash; puts every '
 'site running that theme in reach of unauthenticated code execution.</span>')

# Top story tag + the newly sourced "two employees" figure
c.rep("cy.topstory.tag",
 '<span class="tag new">New &middot; 10:50 AM</span><span class="tag crit">Healthcare</span>',
 '<span class="tag new">Carried &middot; updated 11:05 AM</span><span class="tag crit">Healthcare</span>')

c.rep("cy.mckesson.two",
 'ShinyHunters says it was behind the attack and that it got in by <b>voice phishing &mdash; vishing &mdash;\nmultiple McKesson employees</b>',
 'ShinyHunters says it was behind the attack and that it got in by <b>voice phishing &mdash; vishing &mdash;\nmultiple McKesson employees</b>')

# Ubiquiti rows: demote New -> Carried
c.rep("cy.ubnt1",'<td><b>New &middot; 10:50 AM.</b> Improper input validation','<td><b>Carried &middot; sourced 10:50 AM.</b> Improper input validation')
c.rep("cy.ubnt2",'<td><b>New &middot; 10:50 AM.</b> CRLF injection','<td><b>Carried &middot; sourced 10:50 AM.</b> CRLF injection')
c.rep("cy.ubnt3",'<td><b>New &middot; 10:50 AM.</b> Command injection','<td><b>Carried &middot; sourced 10:50 AM.</b> Command injection')

# ATF card: DOJ / containment detail
c.rep("cy.atf.tag",
 '<span class="tag">Carried &middot; sourced 10:20 AM</span><span class="tag crit">Federal</span>',
 '<span class="tag new">Updated &middot; 11:05 AM</span><span class="tag crit">Federal</span>')
c.rep("cy.atf.doj",
 '<b>The confirmation and the claim are both real; the link between them is not established by any source seen this run, and none is asserted here.</b></p></div>',
 '<b>The confirmation and the claim are both real; the link between them is not established by any source seen '
 'in any edition to date, and none is asserted here.</b> <b>Added at 11:05 AM &mdash; what the agency did, and who '
 'else is now in it.</b> Reporting fetched this run states that <b>immediately after discovering the incident the ATF '
 'cut off access to the affected system</b> and began <b>incident-response and forensic activities</b>, and that '
 '<b>senior Department of Justice officials designated the event a &ldquo;major incident&rdquo; under federal '
 'guidelines</b> &mdash; which is what brings the <b>DoJ into the investigation</b>. Note the direction of that: '
 '&ldquo;major incident&rdquo; is a <b>federal designation applied by DoJ</b>, not a severity adjective the agency '
 'chose for itself, and it is the reason this item sits in the federal column rather than the claims column. The same '
 'reporting repeats that <b>Qilin has made no specific claim about what it took</b>.</p></div>')

# NEW panel: Avada, inserted before "Breaches & Incidents"
AVADA = ('<div class="panel"><div class="tags"><span class="tag new">New &middot; 11:05 AM</span>'
 '<span class="tag crit">CVSS 9.8</span><span class="tag warn">No exploitation stated</span></div>\n'
 '<h3>An AI agent chained six flaws in a WordPress theme on a million sites, and wrote the exploit itself</h3>\n'
 '<p><b>What it is.</b> A critical vulnerability chain in the <b>Avada</b> theme for WordPress lets an '
 '<b>unauthenticated</b> attacker execute <b>arbitrary PHP code</b> on the server. The six issues are tracked '
 'collectively as <b>CVE-2026-18431</b> and carry a <b>9.8</b> critical severity score. Chained in a specific order '
 'they form a <b>zero-click</b> attack; the components are authorization, input-validation, trust-boundary and '
 'file-handling weaknesses. A successful attacker can plant malware, reach databases, redirect visitors or add rogue '
 'administrator accounts.</p>\n'
 '<p><b>Why the prerequisites do not narrow it.</b> Exploitation requires vulnerable versions of both the theme '
 '(<b>Avada up to 7.16</b>) and the <b>Fusion Builder</b> plugin (<b>up to 3.16</b>) to be active. That sounds like '
 'a filter and is not one: Wordfence researchers clarified that <b>Fusion Builder is a required plugin for the Avada '
 'theme</b>, so <b>all sites running the theme are also running the plugin</b>. Avada has <b>more than 1 million '
 'sales</b>. In the researchers&rsquo; own words, &ldquo;any site that has the Avada theme installed is going to be '
 'exploitable.&rdquo;</p>\n'
 '<p><b>The part that is arguably the story.</b> The chain was found by <b>Argus</b>, an internal agentic framework '
 'at Wordfence, which also <b>developed proof-of-concept exploit code</b> &mdash; the whole thing in <b>about two '
 'hours</b>. Argus reproduced the flaw on <b>July 30</b>; the vendor got full details on <b>August 5</b>, '
 'acknowledged on <b>August 10</b>, and ThemeFusion shipped <b>Avada 7.16.1 and Fusion Builder 3.16.1</b>. '
 'Wordfence is <b>withholding complete technical details</b> to give administrators time to update, and published '
 'only a six-step outline of the chain.</p>\n'
 '<p class="note">&#9888; <b>What is not established.</b> No source seen this run states <b>in-the-wild '
 'exploitation</b>, a victim, or a public proof of concept outside Wordfence&rsquo;s own; the flaw is '
 '<b>not KEV-listed</b> and carries <b>no federal deadline</b>. It is on this page for its severity and its reach, '
 'not for evidence of attacks. One aggregator seen this run renders the affected range as &ldquo;&le; 7.1&rdquo; '
 'rather than 7.16; the vendor-sourced reporting says <b>7.16</b>, and that is the figure printed here.</p></div>\n')
c.rep("cy.avada.panel",'</div><h2 class="sec">Breaches &amp; Incidents</h2>', '</div>'+AVADA+'<h2 class="sec">Breaches &amp; Incidents</h2>')

# Avada row in Vulnerability Watch (top of table)
c.rep("cy.avada.row",
 '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n<tr><td><b>CVE-2026-77537</b></td>',
 '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n'
 '<tr><td><b>CVE-2026-18431</b></td><td class="critc">9.8</td>'
 '<td>Avada WordPress theme &le; 7.16 with Fusion Builder plugin &le; 3.16</td>'
 '<td><b>New &middot; 11:05 AM.</b> Six flaws chained into <b>zero-click, unauthenticated remote code execution</b>. '
 'Fixed in <b>Avada 7.16.1 / Fusion Builder 3.16.1</b>. Found by Wordfence&rsquo;s <b>Argus</b> agentic framework in '
 'about two hours. <b>Not KEV-listed; no in-the-wild exploitation stated by any source seen this run.</b></td></tr>\n'
 '<tr><td><b>CVE-2026-77537</b></td>')

c.hasnt("cy.stale.newtag",'<span class="tag new">New &middot; 10:50 AM</span>')
c.has("cy.avada.present",'CVE-2026-18431')
c.write()

# ---------------------------------------------------------------- MARKETS
w=Ed("wallstreet-briefing.html")
w.rep("ws.freshline",
 '<div class="freshline" id="freshline">Data as of 10:50 AM ET</div>',
 '<div class="freshline" id="freshline">Data as of 11:05 AM ET</div>')

w.rep("ws.tldr",
 'with Friday&rsquo;s payrolls report the next test.</span>',
 'with next Friday&rsquo;s payrolls report the next test &mdash; and that report now carries two '
 'differently-sourced forecasts, +58,000 and +90,000, against a July print that went backwards.</span>')

w.rep("ws.movers.note",
 '<b>No figure on this movers board changed at 10:50 AM either</b>, and none can while the tape is shut. '
 'One number elsewhere on the page did move: the September rate pricing in <a href="#radar">On the Radar</a> '
 'gained a <b>third, independent read</b> at 10:50 AM. It is not a stock move and it is not tagged as one.',
 '<b>No figure on this movers board changed at 11:05 AM either</b>, and none can while the tape is shut. '
 'Two things elsewhere on the page did move, and neither is a stock move: the September rate pricing in '
 '<a href="#radar">On the Radar</a> gained a <b>third, independent read</b> in the <b>10:50 AM</b> edition, and '
 'the payrolls forecast in the same section gained a <b>second, differently-sourced number</b> at <b>11:05 AM</b>. '
 'Neither is tagged as a mover.')

w.rep("ws.radar.jobs",
 '<b>+3.1% year over year</b>. It is the first major read on the labour market since Warsh\'s Jackson Hole\n'
 'warning, and the week\'s largest scheduled risk.</li>',
 '<b>+3.1% year over year</b>. It is the first major read on the labour market since Warsh\'s Jackson Hole\n'
 'warning, and the week\'s largest scheduled risk.</li>\n'
 '<li><b>New at 11:05 AM &mdash; a second forecast for that report, and the two do not agree.</b> The +58,000 '
 'figure above is attributed to a <b>Reuters poll</b> cited in a week-ahead preview. A separate research house, '
 '<b>Capital Economics</b>, publishes an employment-report preview expecting nonfarm payrolls to have risen by '
 '<b>a modest 90,000</b> in August. <b>Neither is adopted and nothing is averaged</b> &mdash; they are two '
 'independent forecasts of the same release, roughly <b>32,000 apart</b>, and the gap between them is itself the '
 'useful information about how uncertain this print is. <b>The unemployment-rate expectation of 4.1% comes only '
 'from the first source</b>; no second read on it was returned this run, and none is invented.</li>\n'
 '<li><b>New at 11:05 AM &mdash; what the last jobs report actually did, which is why this one matters.</b> '
 '<b>July payrolls fell by 23,000</b> &mdash; a decline, not a slower gain &mdash; against a forecast of '
 '<b>+80,000</b>, and <b>June was revised down to a +20,000 gain</b>. A week-ahead preview describes the July '
 'report as a <b>surprise labour-market weakening</b>. Set that beside Warsh warning about inflation and the '
 'tension in next Friday&rsquo;s number is plain: a second weak print argues one way on rates and the inflation '
 'language argues the other. <b>This page forecasts neither the number nor the Fed&rsquo;s response to it.</b></li>')

w.rep("ws.radar.week",
 '<b>Monday, August 31 is quiet</b> &mdash; no major U.S. economic report is\nscheduled &mdash; but the tape reopens that morning.</li>',
 '<b>Monday, August 31 is quiet</b> &mdash; no major U.S. economic report is\nscheduled &mdash; but the tape reopens that morning. '
 '<b>Dated at 11:05 AM from a week-ahead preview:</b> ISM Manufacturing, construction spending and JOLTS on '
 '<b>Tuesday, September 1</b>; ADP and factory orders plus the Federal Reserve&rsquo;s <b>Beige Book</b> on '
 '<b>Wednesday, September 2</b>; the July trade balance, weekly jobless claims and ISM Services on '
 '<b>Thursday, September 3</b>. <b>Only the days are asserted, not the consensus figures</b>, none of which was '
 'stated for these releases by any source seen this run.</li>')

w.hasnt("ws.stale.friday", "with Friday&rsquo;s payrolls report the next test")
w.has("ws.cap", "Capital Economics")
w.write()

# ---------------------------------------------------------------- MMA
m=Ed("mma-briefing.html")
m.rep("mma.freshline",
 '<div class="freshline" id="freshline">Data as of 10:50 AM ET</div>',
 '<div class="freshline" id="freshline">Data as of 11:05 AM ET</div>')

m.rep("mma.tldr",
 'the promotion has announced four $100,000 bonuses, and a second independent account now backs the version of the finish that calls the punch an uppercut, leaving that detail two-to-one but still unadopted.</span>',
 'the promotion has announced four $100,000 bonuses &mdash; a second outlet independently puts the card&rsquo;s total '
 'at $400,000, which is the same four awards counted a different way &mdash; and a third account now backs the version '
 'of the finish that calls the punch an uppercut, leaving that detail two-to-one but still unadopted.</span>')

m.rep("mma.bonus.corrob",
 'The same report independently puts the card at <b>ten finishes</b>, which is the count this page has carried.',
 'The same report independently puts the card at <b>ten finishes</b>, which is the count this page has carried. '
 '<b>Corroborated at 11:05 AM, and the arithmetic is the check.</b> A second outlet reports the card produced '
 '<b>$400,000 in bonuses</b> &mdash; which is four awards of $100,000, exactly the four named above, arrived at '
 'independently and expressed as a total rather than a list. <b>That is corroboration of the same four, not a fifth '
 'award</b>, and this page does not read a round number as evidence of an extra recipient. The same report also '
 'attributes the <b>Performance of the Night</b> to <b>Song Yadong</b> by name. It adds one thing the bonus list only '
 'implies: <b>Denise Gomes did not receive a bonus</b> despite the co-main knockout, which the writer calls the most '
 'deserving performance that went unrewarded &mdash; that last part is the writer&rsquo;s judgement and is printed as '
 'his, not as a finding of this page.')

m.rep("mma.champ.check",
 '&#9888; <b>What that means for the confidence claim on this board.</b>',
 '<b>Re-checked at 11:05 AM, and this run the check went the other way.</b> A fresh general search for the current '
 'UFC champions was run again this edition and returned a listing that <b>agrees with this board on every men&rsquo;s '
 'belt it covered</b> &mdash; Aspinall at heavyweight, <b>Carlos Ulberg</b> at light heavyweight with the April 11, '
 '2026 date, <b>Sean Strickland</b> at middleweight with the May 9, 2026 date, Makhachev at welterweight, '
 '<b>Justin Gaethje</b> at lightweight and <b>Alexander Volkanovski</b> at featherweight. That is the exact reverse '
 'of the 10:50 AM result, on the same question, fifteen minutes apart. <b>The lesson is not that the board is now '
 'safer; it is that a single search is not a verification method.</b> The board did not change on either result, '
 'because on both runs the dates were compared before the names were copied.\n'
 '<p>&#9888; <b>What that means for the confidence claim on this board.</b>')

m.rep("mma.champ.counter",
 'This edition does not extend the agreement counter</b>, because the snippet returned this run disagreed on two belts and was rejected.',
 'The 10:50 AM edition did not extend the agreement counter</b>, because the snippet it returned disagreed on two '
 'belts and was rejected; <b>the 11:05 AM re-check agrees on six of six men&rsquo;s belts and does extend it</b>, '
 'and the counter is deliberately not restated as a number here because two consecutive runs of the same query '
 'produced opposite snippets and a tally across them would suggest a stability the evidence does not show.')

m.rep("mma.champ.unchanged",
 'The board itself is unchanged for a <b>fiftieth consecutive edition</b>',
 'The board itself is unchanged for a <b>fifty-first consecutive edition</b>')

m.hasnt("mma.stale.tldrbonus", 'and a second independent account now backs the version of the finish that calls the punch an uppercut')
m.has("mma.400k", '$400,000 in bonuses')
m.write()

# ---------------------------------------------------------------- INDEX
x=Ed("index.html")
x.rep("ix.fresh",'Data as of 10:50 AM ET','Data as of 11:05 AM ET')
x.write()
