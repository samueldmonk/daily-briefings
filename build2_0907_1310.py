# -*- coding: utf-8 -*-
import re, os
R="/tmp/db_1788800764"; PAGES=["index","cyber-briefing","wallstreet-briefing","mma-briefing"]
S={p:open(os.path.join(R,p+".html"),encoding="utf-8").read() for p in PAGES}
log=[]
def sub1(page,old,new,why):
    n=S[page].count(old); assert n==1,"GOT %d :: %s :: %s"%(n,page,why)
    S[page]=S[page].replace(old,new); log.append("%-20s %s"%(page,why))

# ---- 1. CYBER tldr: point the "new" clause at Tengu ----
sub1("cyber-briefing",
 "but new the 12:16 edition is a flaw with no deadline at all, because it has nothing to attach one to:",
 "and the one genuinely new item this edition is not a vulnerability at all but a piece of malware, the <b>Tengu</b> Linux bot, freshly analysed today and built to reboot the machine when defenders kill it. The flaw with no deadline still stands behind it, because it has nothing to attach one to:",
 "tldr rewritten to lead the new item with Tengu")

# ---- 2. WALL STREET tldr: fix the single-level contradiction ----
sub1("wallstreet-briefing",
 "while Brent trades at <b>$97.39, up 1.15%</b>, as the U.S. and Iran exchange strikes around Hormuz.",
 "while Brent is higher again on the day, <b>quoted between roughly $97.27 and $97.50 across six separate readings of one thin holiday session</b>, "
 "as the U.S. and Iran exchange strikes around Hormuz. <span class=\"mut\">No single Brent level is asserted here, matching the body of the page &mdash; six minutes of a moving quote is a range, not a price.</span>",
 "tldr Brent claim reconciled with the body's explicit no-single-level refusal")

# ---- 3. WALL STREET: sixth Brent reading + independent corroboration of the Hormuz traffic low ----
anchor = ("<b>No single Brent level is asserted for today</b>")
newpara = ('<b>A sixth reading arrived this edition, and it is the widest of the six.</b> A search return dated today puts '
 '<b>Brent at about $97.50 a barrel at roughly 2:34&nbsp;a.m. ET, up about 1.7% on the session</b>, and states an '
 '<b>intraday high near $97.93</b> &mdash; the same $97.93 this page already carries from Reuters via EnergyNow as the level Brent touched. '
 'The same return puts <b>WTI above $92</b>, consistent with the ~$92.34 already in the commodities table. '
 '<span class="mut">A sixth minute of the same session; it moves nothing, and it is the second independent route to the $97.93 touch rather than a new high.</span> '
 '<b>It also corroborates the traffic figure in this page&rsquo;s lead from a second direction:</b> where Kpler counts about ten commodity ships a day, this return says '
 '<b>tanker traffic through the Strait of Hormuz has fallen to its lowest level since May</b> &mdash; an independent statement of the same four-month low, from a different measure. ')
sub1("wallstreet-briefing", anchor, newpara + anchor,
 "added sixth Brent reading (~$97.50 / +1.7% at ~2:34 a.m. ET) + second route to the Hormuz traffic low")

# ---- 4. MMA tldr: the Edmonton card is no longer new ----
sub1("mma-briefing",
 "while new the 12:16 edition the October schedule gains a second Canadian date,",
 "while the October schedule carries a second Canadian date, first added the 12:16 edition,",
 "tldr: Edmonton card demoted from New to carried")

# ---- 5. INDEX cards synced to their pages ----
sub1("index",
 "New the 12:45 edition: CVE-2026-84147, a CVSS 10.0 unauthenticated file-upload flaw in Manacle Technologies&rsquo; Multi-tenant ERP &mdash; disclosed, not exploited, and not in KEV.",
 "New this edition: <b>Tengu</b>, a Mirai-derived Linux bot given a fresh static analysis dated 7 September &mdash; it masquerades as a kernel worker, restarts itself from a hidden guardian process, and abuses the hardware watchdog to reboot the machine when defenders kill it. Malware, not a vulnerability: no CVE, no CVSS, and no KEV deadline.",
 "index security card: new item swapped to Tengu")
sub1("index",
 "while Brent traded at $97.39, up 1.15%, on renewed U.S.&ndash;Iran strikes around Hormuz.",
 "while Brent traded higher again, quoted between roughly $97.27 and $97.50 across six readings of one thin holiday session, on renewed U.S.&ndash;Iran strikes around Hormuz. No single level is asserted.",
 "index markets card: Brent claim reconciled to a range")
sub1("index",
 "UFC Fight Night: Buckley vs. Malott lands at Rogers Place in Edmonton on Saturday 17 October,",
 "Nothing new on the MMA beat this edition. UFC Fight Night: Buckley vs. Malott still lands at Rogers Place in Edmonton on Saturday 17 October,",
 "index MMA card: states plainly that nothing is new this edition")

for p in PAGES: open(os.path.join(R,p+".html"),"w",encoding="utf-8").write(S[p])
print("\n".join(log))
