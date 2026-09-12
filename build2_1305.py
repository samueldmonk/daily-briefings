#!/usr/bin/env python3
import re, os
OUT = "/sessions/sleepy-hopeful-carson/mnt/outputs"
def load(f): return open(os.path.join(OUT, f), encoding="utf-8").read()
def save(f, s): open(os.path.join(OUT, f), "w", encoding="utf-8").write(s)
fails = []
def rep(s, old, new, label):
    if old not in s:
        fails.append("MISSING: " + label); return s
    return s.replace(old, new, 1)

# ---------- WALL STREET: Brent row ----------
ws = load("wallstreet-briefing.html")
m = re.search(r"<tr><td>Brent crude</td><td>\$104\.42</td><td>.*?</td></tr>", ws, re.S)
if not m:
    fails.append("MISSING: ws.brent")
else:
    ws = ws.replace(m.group(0),
      "<tr><td>Brent crude</td><td>$104.61 <span class=\"note\" style=\"display:inline;margin:0\">(settle)</span></td>"
      "<td><b>Settled down 2.8% on Friday 11 September</b> &mdash; a settlement figure, newly sourced this run, which supersedes both the "
      "&ldquo;~$99&rdquo; of earlier editions and the <b>$104.42 / &minus;2.98%</b> carried yesterday; that earlier read is named here rather "
      "than silently dropped, and the two describe the same move. Brent still gained <b>8.7% on the week</b> and held above $100. It had ended "
      "the previous session at <b>$107.63</b> after soaring <b>6.3% in a day</b> on 10 September.</td></tr>")
save("wallstreet-briefing.html", ws)

# ---------- MMA ----------
mma = load("mma-briefing.html")

# 1. Top story: resolve the start-time conflict + state the no-results position plainly.
mma = rep(mma,
 "<b>Prelims begin at 2 PM ET / 11 AM PT and the main card at 5 PM ET / 2 PM PT</b>, streaming exclusively on <b>Paramount+</b>. "
 "The 2 PM ET prelim time now has <b>three independent sources this run</b> (Yahoo Sports, Forbes and MMA Mania); UFC.com’s earlier "
 "1 PM ET listing is printed alongside rather than dropped.",
 "<b>Prelims begin at 2 PM ET / 11 AM PT and the main card at 5 PM ET / 2 PM PT</b>, streaming exclusively on <b>Paramount+</b>. "
 "<b>That start-time conflict is now resolved, and at its source.</b> Three earlier editions printed 2 PM ET alongside a 1 PM ET listing "
 "because UFC.com itself was the origin of the 1 PM figure. UFC.com's own event coverage, fetched this run, now states twice that "
 "&ldquo;<i>Noche UFC airs at a special time: prelims start at 2pm ET/11am PT, followed by the main card at 5pm ET/2pm PT</i>&rdquo;. The "
 "outlier has corrected itself; 1 PM ET is retired rather than carried.",
 "mma.times")

# 2. Insert a build-time / no-results panel right after the Top Story heading block.
i = mma.find("<h2>Fight Week — Upcoming Cards</h2>")
if i == -1:
    fails.append("MISSING: mma.fw")
else:
    note = ("<div class=\"panel\" style=\"border-left:3px solid var(--gold,#caa64a);margin-top:16px\">"
      "<span class=\"chip\">Build note</span>"
      "<h3 style=\"margin:8px 0 9px;font-size:17px\">No results are published on this page, and that is a finding rather than a gap</h3>"
      "<p style=\"margin:0;font-size:14.5px;color:#c6ced6\">This edition was built at about <b>1:25 PM ET</b>, roughly <b>35 minutes before "
      "the 2 PM ET prelims</b>. Rather than infer that from the clock, the check was made against the promotion's own live page: UFC.com's "
      "<b>&ldquo;Prelim Results | Noche UFC&rdquo;</b> article, fetched at <b>1:10 PM ET</b>, carries its seven prelim bouts as "
      "<b>matchup previews only</b> &mdash; fighters, records and hometowns, with no winner, method or round anywhere on the page, and an "
      "instruction to &ldquo;stay here for all the action as the prelims unfold&rdquo;. Its own metadata sets publication at "
      "<b>2:00 PM ET today</b>. So the absence of results here is confirmed against the authoritative source, not assumed. Any results "
      "circulating before 2 PM ET are not results.</p></div>")
    mma = mma[:i] + note + mma[i:]

# 3. Enrich the Noche card with the full prelim lineup and records from UFC.com.
mma = rep(mma,
 "<b>Weigh-ins:</b> all 26 fighters on weight.</p></div>",
 "<b>Weigh-ins:</b> all 26 fighters on weight.<br><br><b>Full prelim card</b> (UFC.com, this run): Tim Elliott (22-14-1), the "
 "<i>Ultimate Fighter</i> season 24 winner, vs. Edgar Chairez (14-6, 1 NC) at <b>catchweight</b>; Ignacio Bahamondes (17-7) vs. Muslim "
 "Salikhov (22-6) at welterweight; Yousri Belgaroui (10-3), on a five-fight win streak, vs. Djorden Santos (11-3) at middleweight; "
 "Drakkar Klose (16-3-1), fighting out of Glendale, vs. unbeaten Contender Series product Tommy Gantt (12-0, 1 NC); Rafa Garcia (19-4) vs. "
 "Rongzhu (28-6); Sean King III (6-0) vs. Jessie Rosas (8-1); and No. 15-ranked JJ Aldrich (15-7) vs. 21-year-old Regina Tarin (8-0), who "
 "won her debut in February.</p></div>",
 "mma.prelims")

# 4. Main-event context from UFC.com / Yahoo this run.
mma = rep(mma,
 "<b>Jean Silva</b> headlines against <b>Jose Delgado</b>, a <b>short-notice replacement</b> after Yair Rodriguez withdrew injured.",
 "<b>Jean Silva</b> (17-3), the promotion's <b>No. 6-ranked featherweight</b>, headlines against <b>Jose Miguel Delgado</b> (12-2), a "
 "<b>short-notice replacement</b> after former interim champion <b>Yair Rodriguez</b> withdrew injured. Silva is coming off a decision win "
 "over <b>Arnold Allen</b> in January, his rebound from the first knockout loss of his career; Delgado, an <b>Arizona native</b> fighting in "
 "home territory, takes his first UFC main event having won <b>four of his first five</b> UFC fights, including wins over <b>Andre Fili</b> "
 "and <b>Austin Bashi</b> in 2026. In the co-main, two-time flyweight champion <b>Brandon Moreno</b> tries to arrest a <b>two-fight skid</b> "
 "against <b>Joseph Morales</b>.",
 "mma.mainevent")

# 5. Champions board: ESPN cross-check unavailable this run — say so.
m2 = re.search(r"(<h2>Champions Board</h2><div class=\"panel\"[^>]*>)", mma)
if not m2:
    fails.append("MISSING: mma.champ")
else:
    cn = ("<p class=\"note\" style=\"margin:0 0 12px\"><b>Cross-check status this run: unavailable, and the board is published from the "
      "standing record rather than from a fresh read.</b> The ESPN &ldquo;Current and all-time UFC champions&rdquo; article returned <b>no "
      "content</b> when fetched this run, so no verification against it was possible &mdash; which is reported here instead of being "
      "described as a clean check. The four preceding runs each found that page seating at least one stale champion (Alex Pereira at light "
      "heavyweight, twice; Valentina Shevchenko at women's flyweight, three times), so the list below is derived, as it has been throughout, "
      "from the most recent title-changing card in each division. <b>Light heavyweight is Carlos Ulberg</b> (KO1 over Ji&#345;&iacute; "
      "Proch&aacute;zka, UFC 327, 11 April 2026), not Pereira. <b>Women's flyweight is vacant</b> &mdash; Shevchenko <b>vacated</b> while "
      "injured, and Natalia Silva meets Wang Cong for the empty belt at UFC 332 on 3 October.</p>")
    mma = mma.replace(m2.group(0), m2.group(0) + cn)

save("mma-briefing.html", mma)

print("FAILURES:", len(fails))
for f in fails: print("  " + f)
