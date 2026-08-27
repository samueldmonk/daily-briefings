# -*- coding: utf-8 -*-
D='/tmp/db_1787854887/'
f='mma-briefing.html'; s=open(D+f,encoding='utf-8').read()
def rep(old,new):
    global s
    assert s.count(old)==1,"count %d :: %s"%(s.count(old),old[:90]); s=s.replace(old,new)

rep("<b>Re-verified at 12:38 &mdash; and this time ESPN agreed.</b>" if "<b>Re-verified at 12:38 &mdash; and this time ESPN agreed.</b>" in s else "<b>Re-verified at 12:38 — and this time ESPN agreed.</b>",
    "<b>Re-verified again at 2:21, and ESPN agreed for a second consecutive run — this time including the women's divisions.</b> "
    "The mandated query returned <b>Tom Aspinall</b> (heavyweight, June 21 2025), <b>Carlos Ulberg</b> (April 11 2026), <b>Sean Strickland</b> (May 9 2026), "
    "<b>Islam Makhachev</b> (November 15 2025), <b>Justin Gaethje</b> (June 14 2026) and <b>Alexander Volkanovski</b> (April 12 2025), and — new at 2:21 — "
    "<b>Kayla Harrison</b> at women's bantamweight, <b>Valentina Shevchenko</b> at women's flyweight and <b>Mackenzie Dern</b> at women's strawweight, "
    "the first time this page has had the three women's belts returned by ESPN in the same run. <b>Nine of the eleven divisions are now confirmed against the source rather than carried.</b> "
    "<span style=\"color:var(--mut)\">The two not returned this run — men's bantamweight (Petr Yan) and men's flyweight (Joshua Van) — are carried from the verified record. "
    "The 12:38 note read as follows and is kept for the record:</span> <b>Re-verified at 12:38 — and this time ESPN agreed.</b>")
rep("An hour earlier the same page returned a stale summary","Earlier in the day, at 12:05, the same page returned a stale summary")

open(D+f,'w',encoding='utf-8').write(s); print("ok")
