#!/usr/bin/env python3
"""Targeted edits onto the 1810 pages -> 1840 edition. Never sed; rep() asserts
presence and uniqueness."""
import sys, io

D = sys.argv[1] if len(sys.argv) > 1 else "."

def load(n):
    return io.open(D + "/" + n, encoding="utf-8").read()

def save(n, h):
    io.open(D + "/" + n, "w", encoding="utf-8").write(h)

def rep(h, old, new, label):
    c = h.count(old)
    assert c == 1, "rep(%s): expected 1 occurrence, found %d" % (label, c)
    return h.replace(old, new)

# ----------------------------------------------------------------- MMA
m = load("mma-briefing.html")
m = rep(m, "the <b>tenth consecutive edition</b>",
           "the <b>eleventh consecutive edition</b>", "mma streak")
m = rep(m, "the same trap logged at 4:41, 5:15 and 5:41 PM",
           "the same trap logged at 4:41, 5:15, 5:41 and 6:05 PM", "mma trap log")
m = rep(m, "byte-for-byte identical across <b>six</b> consecutive runs now",
           "byte-for-byte identical across <b>seven</b> consecutive runs now",
           "mma modified_time streak")
m = rep(m,
    "A stoppage time is a single number, so this desk still declines",
    "The whole main card was re-read off that same fetch this run and every row "
    "matched what is printed below &mdash; Sola KO R1 1:40 by overhand left, Page "
    "UD 29&ndash;28 across the board, Donchenko UD 30&ndash;27, 30&ndash;27, "
    "29&ndash;28, Campbell by rear-naked choke at R3 3:07, Keita KO R1 2:54 "
    "&mdash; so the disagreement is confined to this one stamp and nothing else. "
    "A stoppage time is a single number, so this desk still declines",
    "mma card reverify")
save("mma-briefing.html", m)

# ---------------------------------------------------------- WALL STREET
w = load("wallstreet-briefing.html")
w = rep(w, "the seventeenth consecutive run without one",
           "the eighteenth consecutive run without one", "vix streak")
w = rep(w,
    "<tr><td>Fed funds target range</td><td class=\"mut\">Not published</td>"
    "<td class=\"mut\">No current range was sourced this run.</td></tr>",
    "<tr><td>Fed funds target range</td><td><b>3.50% &ndash; 3.75%</b></td>"
    "<td class=\"mut\">Refusal partially lifted, with attribution. A September "
    "market-outlook piece from GO Markets fetched this run states the target "
    "range &ldquo;remains at 3.50% to 3.75%&rdquo; going into the 15&ndash;16 "
    "September meeting &mdash; the first return in eighteen runs to state the "
    "standing range at all. Printed with its name on it and not as an official "
    "Federal Reserve figure; one source is not corroboration.</td></tr>",
    "fed funds row")
w = rep(w,
    "decision Wednesday 2:00 PM ET, followed by the Chair’s press conference "
    "at 2:30 PM ET.",
    "decision Wednesday 2:00 PM ET, followed by the Chair’s press conference "
    "at 2:30 PM ET. Newly sourced this run: the decision arrives alongside "
    "<b>updated economic projections and the dot plot</b>, which is why a hot or "
    "cool CPI four days earlier matters beyond the single vote. ",
    "fomc dot plot")
save("wallstreet-briefing.html", w)

# --------------------------------------------------------------- CYBER
c = load("cyber-briefing.html")

OLD_ACCT_START = "<p class=\"note\" style=\"margin:-4px 0 12px\"><b>No item is tagged New this edition"
i = c.find(OLD_ACCT_START)
assert i != -1, "cyber accounting paragraph not found"
j = c.find("</p>", i) + 4
NEW_ACCT = (
    "<p class=\"note\" style=\"margin:-4px 0 12px\"><b>One item is tagged New this "
    "edition, and the streak of zero-tag runs ends on a direct fetch.</b> "
    "<span style=\"font-family:var(--mono);font-size:12.5px\">cybersecuritynews.com/"
    "nodestealer-record-everything/</span> was read first-hand this run "
    "(<span style=\"font-family:var(--mono);font-size:12.5px\">article:published_time "
    "2026-09-04T14:29:44+00:00</span>); the tokens <b>NodeStealer</b>, <b>Netskope</b> "
    "and <b>pynput</b> were each grepped against "
    "<span style=\"font-family:var(--mono);font-size:12.5px\">archive/cyber-2026-09-06-1810.html</span> "
    "and returned <b>zero matches</b> apiece before the tag went on. The MikroTik "
    "vendor-advisory tag stripped at 6:10 PM stays stripped. Everything else the "
    "searches returned this run &mdash; MikroTik RouterOS exploitation, the ASUS "
    "Control Center flaw, Toy Ghouls&rsquo; HiveMQ and Element backdoors, CrowdStrike "
    "SafeMind, the MAG leak, the IDScan.net licence scans &mdash; is already on this "
    "page and was left untagged. <b>Cyber carries 1 New tag, Wall Street 0, MMA 0.</b></p>"
)
c = c[:i] + NEW_ACCT + c[j:]

# sansec refusal -> second consecutive failure, keywords meta explicitly not taken
OLD_SANSEC = "<p class=\"note\" style=\"margin:0 0 12px\"><b>A direct fetch that only half-worked, reported as such.</b>"
i = c.find(OLD_SANSEC)
assert i != -1, "sansec refusal paragraph not found"
j = c.find("</p>", i) + 4
NEW_SANSEC = (
    "<p class=\"note\" style=\"margin:0 0 12px\"><b>The retry was run, and it failed "
    "the same way &mdash; twice now.</b> The previous edition set the test: re-request "
    "<span style=\"font-family:var(--mono);font-size:12.5px\">sansec.io/research/stylesmuggler</span>, "
    "the primary StyleSmuggler advisory this page has only ever read through other "
    "outlets. It was requested again this run and again returned the page&rsquo;s "
    "<b>metadata</b> (author <b>Sansec Forensics Team</b>, "
    "<span style=\"font-family:var(--mono);font-size:12.5px\">article:modified_time "
    "2026-09-05T20:18:09Z</span>, published 5 September) plus its section headings and "
    "site navigation &mdash; <b>the article body did not render</b>. The response also "
    "exposes a <span style=\"font-family:var(--mono);font-size:12.5px\">keywords</span> "
    "meta tag containing what look like indicators of compromise. <b>Nothing was taken "
    "from it</b>, IOC-shaped strings least of all: a keywords tag is search-engine "
    "metadata, not an advisory&rsquo;s findings, and this desk will not publish "
    "indicators it has not seen stated in the body of the advisory that produced them. "
    "Nothing on this page is upgraded to first-hand Sansec sourcing. &#9733; Next run: "
    "retry once more; if the body fails a third time, stop retrying and say so.</p>"
)
c = c[:i] + NEW_SANSEC + c[j:]

# NodeStealer card, inserted at the head of the Breaches & Incidents card deck
anchor = ("<div class=\"cards\">\n<div class=\"card\">\n"
          "<div class=\"tags\"><span class=\"t hot\">Network edge</span>"
          "<span class=\"t\">Carried forward</span></div>\n"
          "<h3>MikroTik&rsquo;s own advisory, read first-hand")
assert c.count(anchor) == 1, "breaches deck anchor not unique"
NODECARD = (
    "<div class=\"cards\">\n"
    "<div class=\"card\">\n"
    "<div class=\"tags\"><span class=\"t new\">New</span>"
    "<span class=\"t\">Infostealer</span></div>\n"
    "<h3>NodeStealer stops stealing and starts watching &mdash; keylogger, clipboard "
    "and screen capture bolted onto a credential thief</h3>\n"
    "<p><b>Netskope researchers identified an upgraded Python NodeStealer variant in "
    "August 2026 that turns an account-stealing infection into continuous "
    "surveillance.</b> The addition that matters is a keylogger built on Python&rsquo;s "
    "<span style=\"font-family:var(--mono);font-size:12.5px\">pynput</span> library: it "
    "writes captured text to a temporary file, ships it to the primary Telegram "
    "command-and-control channel <b>every 120 seconds</b>, clears the file and keeps "
    "going indefinitely. Clipboard monitoring picks up plain text that is pasted rather "
    "than typed, and the malware takes a <b>screenshot when it runs and a second one "
    "before its screenshot routine ends</b>, sending both over Telegram &mdash; which "
    "reaches dashboards, recovery codes and open documents that never touch the keyboard "
    "or the clipboard at all.</p>\n"
    "<p><b>Two Telegram bots, not one</b>, split the take: one receives an archive of "
    "browser credentials, passwords and cookie databases, the other Facebook-specific "
    "data. The newest samples query <b>more than 20 Facebook Graph API endpoints, up "
    "from two</b> in earlier versions, pulling identity details, contacts, posts, pages, "
    "advertising assets, business records and login data &mdash; enough for an attacker "
    "to run unauthorised ads or burn a company&rsquo;s ad budget rather than merely "
    "hijack one profile. Samples ship as compiled Python bytecode with altered header "
    "fields, apparently to obscure the compilation timeline and frustrate automated "
    "analysis. Netskope reports the recent activity landing mainly in <b>Asia and North "
    "America</b>, financial services worst hit but spread across sectors. The published "
    "indicator is a filename pattern: "
    "<span style=\"font-family:var(--mono);font-size:12.5px\">keylog({ip}).txt</span> in "
    "the temp folder.</p>\n"
    "<p><span class=\"mut\">Two things this desk is not asserting. Netskope&rsquo;s "
    "report <b>does not identify a confirmed initial delivery method</b>, so no infection "
    "route is printed here and defenders should not plan around a single one. And the "
    "AI angle is stated exactly as the researchers stated it &mdash; repeated, "
    "similarly-structured calls carrying decorative emoji labels, a pattern absent from "
    "earlier NodeStealer code, which they read as a sign some new code <i>may</i> have "
    "been produced with AI assistance. That is an inference about style, not proof of a "
    "tool or an author, and it is not evidence for the separate AI-assisted-intrusion "
    "story elsewhere on this page.</span></p>\n"
    "</div>\n"
    "<div class=\"card\">\n"
    "<div class=\"tags\"><span class=\"t hot\">Network edge</span>"
    "<span class=\"t\">Carried forward</span></div>\n"
    "<h3>MikroTik&rsquo;s own advisory, read first-hand")
c = c.replace(anchor, NODECARD)
save("cyber-briefing.html", c)

print("edits_1840 OK")
