# -*- coding: utf-8 -*-
import io
O="/sessions/tender-hopeful-newton/mnt/outputs/"
class Ed:
    def __init__(s_,fn):
        s_.fn=fn; s_.s=io.open(O+fn,encoding='utf-8').read(); s_.ok=[]; s_.miss=[]
    def rep(s_,n,o,w,c=1):
        if o in s_.s: s_.s=s_.s.replace(o,w,c); s_.ok.append(n)
        else: s_.miss.append(n)
    def hasnt(s_,n,p):
        if p in s_.s: s_.miss.append("STALE:"+n)
    def write(s_):
        io.open(O+s_.fn,'w',encoding='utf-8').write(s_.s)
        print("== %s : %d applied, %d issues"%(s_.fn,len(s_.ok),len(s_.miss)))
        for m in s_.miss: print("   !!",m)

c=Ed("cyber-briefing.html")
c.rep("cy.topstory.tag",
 '<div style="margin-bottom:9px"><span class="tag new">New &middot; 10:50 AM</span> <span class="tag crit">Healthca',
 '<div style="margin-bottom:9px"><span class="tag new">Carried &middot; updated 11:05 AM</span> <span class="tag crit">Healthca')
c.rep("cy.mckesson.two",
 '<b>voice phishing &mdash; vishing &mdash; multiple McKesson employees</b>, compromising their <b>Okta\nsingle sign-on accounts</b>',
 '<b>voice phishing &mdash; vishing &mdash; multiple McKesson employees</b> &mdash; and at <b>11:05 AM</b> that '
 'count stopped being vague: a report fetched this run puts it at <b>two</b> employees, which is the first '
 'specific number any edition has been able to attach to the intrusion &mdash; compromising their <b>Okta\n'
 'single sign-on accounts</b>')
c.rep("cy.ubnt2",'<td><b>New &middot; 10:50 AM.</b> <b>CRLF injection</b>','<td><b>Carried &middot; sourced 10:50 AM.</b> <b>CRLF injection</b>')
c.rep("cy.ubnt3",'<td><b>New &middot; 10:50 AM.</b> <b>Command injection</b>','<td><b>Carried &middot; sourced 10:50 AM.</b> <b>Command injection</b>')
c.hasnt("cy.newtag",'New &middot; 10:50 AM')
c.write()

m=Ed("mma-briefing.html")
m.rep("mma.champ.counter",
 '<b>This edition does not extend the agreement counter</b>, because the snippet returned this run\n<i>disagreed</i> on two belts and was rejected. The board itself is unchanged for a <b>fiftieth consecutive\nedition</b>',
 '<b>The 10:50 AM edition did not extend the agreement counter</b>, because the snippet it returned\n'
 '<i>disagreed</i> on two belts and was rejected; <b>the 11:05 AM re-check agrees on six of six men&rsquo;s belts '
 'and does extend it</b>. The counter is deliberately <b>not restated as a number</b> here: two consecutive runs of '
 'the same query, fifteen minutes apart, produced opposite snippets, and a tally across them would imply a stability '
 'the evidence does not show. The board itself is unchanged for a <b>fifty-first consecutive\nedition</b>')
m.hasnt("mma.fiftieth",'fiftieth consecutive')
m.write()
