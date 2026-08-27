# -*- coding: utf-8 -*-
P='/tmp/db_1787854887/mma-briefing.html'
s=open(P,encoding='utf-8').read()
def rep(old,new,n=1):
    global s
    c=s.count(old); assert c==n,"count %d want %d :: %s"%(c,n,old[:100]); s=s.replace(old,new)

s=s.replace('<span class="tag new">Updated · 12:38</span>','<span class="tag">Carried · 12:38</span>')
s=s.replace('<span class="tag new">New · 12:38</span>','<span class="tag">Carried · 12:38</span>')

# --- Noche UFC card: venue, billing, weight class and the withdrawal now sourced ---
rep('<div class="card"><span class="tag">Carried</span><span class="tag acc">Main event booked</span>\n<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT SEP 12 · NOCHE UFC</div>',
    '<div class="card"><span class="tag new">Updated · 2:21</span><span class="tag acc">Main event booked</span>\n<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT SEP 12 · DESERT DIAMOND ARENA, GLENDALE, AZ</div>')
rep('<p>A new main event has been announced for <b>Noche UFC</b> on <b>September 12</b>: <b>Jean Silva vs. Jos&eacute; Miguel Delgado</b>, streaming on <b>Paramount+</b>.<br><span style="color:var(--mut)">No venue, weight class or odds were stated in the announcement seen this run, so none are printed.</span></p>',
    '<p>A new main event headlines <b>Noche UFC</b> on <b>September 12</b>: <b>Jean Silva vs. Jos&eacute; Miguel Delgado</b>, streaming on <b>Paramount+</b>. '
    '<b>Updated at 2:21 — the blanks are now filled.</b> The card is scheduled for <b>Desert Diamond Arena in Glendale, Arizona</b>, is also billed as <b>UFC Fight Night 288</b> and <b>Noche UFC 4</b>, '
    'and the main event is a <b>featherweight</b> bout. <b>Why the change:</b> a featherweight bout between <b>Yair Rodr&iacute;guez</b> and Jean Silva was originally scheduled to headline; '
    'Rodr&iacute;guez <b>withdrew with an injury</b> and was replaced by Delgado, of Mexico. Silva stays in the headliner.<br>'
    '<span style="color:var(--mut)">The 12:38 edition printed &ldquo;no venue, weight class or odds were stated&rdquo; because none had been; venue and weight class have now been sourced and are added. '
    '<b>Odds still have not been</b>, and none are printed.</span></p>')

# --- Prospect Watch: Hasan debut tie-in + the Balletto spelling disagreement ---
rep('Hasan finished Mridul Saikia at bantamweight in <b>under a minute</b>.</p>',
    'Hasan finished Mridul Saikia at bantamweight in <b>under a minute</b>. '
    '<b>New at 2:21:</b> Hasan is now heading into his <b>UFC debut at UFC Shanghai this weekend</b> — sixteen days after winning his contract. '
    '<span style="color:var(--mut)">Wint played collegiately at FIU and spent time on the New York Jets practice squad.</span></p>')

rep('<b>Sean Clancy Jr. def. Gary Balleto</b> by TKO, <b>R2, 3:54</b>',
    '<b>Sean Clancy Jr. def. Gary Balleto</b> by TKO, <b>R2, 3:54</b> <span style="color:var(--mut)">(a source fetched at 2:21 spells the surname <b>Balletto</b>, with two t&rsquo;s, and confirms the second-round stoppage; both spellings are on the record and this page does not pick one)</span>')

open(P,'w',encoding='utf-8').write(s); print("MMA OK",len(s))
