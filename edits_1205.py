#!/usr/bin/env python3
"""Targeted edits onto the 11:44 pages -> 12:05 PM ET Midday Edition, Sat Aug 29 2026."""
import sys, io

MISSES = []

def ed(txt, old, new, label):
    if old not in txt:
        MISSES.append(label)
        return txt
    return txt.replace(old, new, 1)

def load(p):
    return io.open(p, encoding='utf-8').read()

def save(p, t):
    io.open(p, 'w', encoding='utf-8').write(t)

# ---------------------------------------------------------------- MMA
p = 'mma-briefing.html'
h = load(p)

h = ed(h,
  '<span class="pill">Updated <span id="updated">11:35 AM ET</span></span>',
  '<span class="pill">Updated <span id="updated">12:05 PM ET</span></span>',
  'mma-masthead-time')
h = ed(h,
  '<span class="pill" id="edition">Morning Edition</span>',
  '<span class="pill" id="edition">Midday Edition</span>',
  'mma-edition')
h = ed(h,
  '<div class="freshline" id="freshline">Data as of 11:35 AM ET</div>',
  '<div class="freshline" id="freshline">Data as of 12:05 PM ET</div>',
  'mma-freshline')

# --- TLDR
OLD_TLDR = ('Song Yadong knocked out Umar Nurmagomedov in the second round of the UFC Shanghai main event '
  'and asked for a title shot, but the bantamweight belt is already spoken for &mdash; Petr Yan defends it '
  'against Merab Dvalishvili in a trilogy at UFC 333 in Abu Dhabi on October 24, a card this page had not '
  'carried until now; a third source has meanwhile given the finishing punch a third different name, which '
  'retires this page&rsquo;s two-to-one tally rather than settling it; and Umar&rsquo;s brother Usman is '
  'reported to have come into the cage during Song&rsquo;s celebration, with both camps described as '
  'respectful afterwards.')
NEW_TLDR = ('Song Yadong knocked out Umar Nurmagomedov in the second round of the UFC Shanghai main event and '
  'asked for a title shot he cannot have next, because the bantamweight belt is booked &mdash; Petr Yan defends '
  'it against Merab Dvalishvili in a trilogy at UFC 333 in Abu Dhabi on October 24 &mdash; while the lightweight '
  'belt sits idle, with newly sourced reporting that champion Justin Gaethje has nothing scheduled and is not '
  'expected to fight again in 2026; and a fourth run of the same champions query produced a fourth different '
  'failure, a listing that agreed on six belts by name and date and then said in one sentence that Islam '
  'Makhachev had both vacated the lightweight title and still held it, which was rejected on its own wording '
  'before any source was consulted.')
h = ed(h, OLD_TLDR, NEW_TLDR, 'mma-tldr')

# --- Champions verification: append the fourth check
ANCHOR = 'for either belt.\n<b>UFC Shanghai carried no title bout'
NEWPARA = ('for either belt.</p>\n'
  '<p><b>Checked a fourth time at 12:05 PM, and the fourth run of that one query produced a fourth distinct '
  'failure.</b> This run&rsquo;s listing again <b>agreed with this board on six men&rsquo;s belts by name and '
  'by date</b> &mdash; Aspinall; <b>Ulberg, April&nbsp;11, 2026</b>; <b>Strickland, May&nbsp;9, 2026</b>; '
  '<b>Makhachev, November&nbsp;15, 2025</b>; <b>Gaethje, June&nbsp;14, 2026</b>; <b>Volkanovski, '
  'April&nbsp;12, 2025</b> &mdash; and named <b>Petr Yan</b> at bantamweight rather than repeating the '
  '11:35&nbsp;AM vacancy. It then closed with a sentence saying that Makhachev <b>&ldquo;vacated the '
  'lightweight title and now holds titles in both the welterweight and lightweight divisions.&rdquo;</b> '
  '&#9888; <b>That was rejected, and it did not need an external source to reject it:</b> a fighter cannot '
  'have vacated a belt and still hold it, so the sentence is disqualified by its own wording. The external '
  'check ran anyway and came back clean &mdash; a separate, fighter-specific search this run returns '
  '<b>Justin Gaethje as the undisputed lightweight champion</b>, and the same listing had already dated '
  'Gaethje&rsquo;s win to June&nbsp;14, 2026 four lines above the sentence that contradicted it. '
  '<b>The four runs of one query have now returned: stale names (10:50), full agreement (11:05), agreement '
  'plus a false vacancy (11:35), and agreement plus a self-contradicting two-division claim (12:05).</b> '
  '<b>RULE: a listing that is right about six things is not thereby right about the seventh</b> &mdash; '
  'accuracy elsewhere in a source is not evidence for the claim you are actually checking. The board is '
  'unchanged for a <b>fifty-third consecutive edition</b>, and the agreement count is again deliberately '
  '<b>not restated as a number</b>, because a tally computed across four mutually inconsistent snippets '
  'would describe a stability the evidence does not support.</p>\n'
  '<p><b>UFC Shanghai carried no title bout')
h = ed(h, ANCHOR, NEWPARA, 'mma-champions-fourth-check')

# --- New item: the idle lightweight belt
AR_ANCHOR = '<h2 class="sec">Around the Sport</h2>'
if AR_ANCHOR in h:
    i = h.find(AR_ANCHOR) + len(AR_ANCHOR)
    j = h.find('<li>', i)
    if j > 0:
        NEWLI = ('<li><b>New at 12:05 PM &mdash; the belt Song is not being offered is booked; the one nobody '
          'mentions is idle.</b> Reporting fetched this run states that lightweight champion <b>Justin Gaethje '
          'has no title defence scheduled</b> and <b>is not expected to compete again in 2026</b> after stopping '
          'Ilia Topuria on June&nbsp;14; his camp does not expect him to defend the belt before <b>2027</b>. His '
          'manager <b>Ali Abdelaziz</b> has said only that the next fight will be against <i>&ldquo;someone he&rsquo;s '
          'never fought before&rdquo;</i>, and <b>Gaethje himself has said Arman Tsarukyan deserves the next '
          'crack</b> at the title. &#9888; <b>Nothing is booked</b> &mdash; no opponent and no date are confirmed, '
          'and the Tsarukyan line is printed as <b>the champion&rsquo;s opinion, not a matchmaking decision</b>. '
          'The contrast is the point: the division whose title Song asked for has a <b>dated trilogy on '
          'October&nbsp;24</b>, while the division above it has a champion with an <b>open calendar</b>.</li>')
        h = h[:j] + NEWLI + h[j:]
    else:
        MISSES.append('mma-around-li-anchor')
else:
    MISSES.append('mma-around-sec')

save(p, h)

# ---------------------------------------------------------------- CYBER
p = 'cyber-briefing.html'
h = load(p)

h = ed(h, '<span class="pill">Updated <span id="updated">11:35 AM ET</span></span>',
         '<span class="pill">Updated <span id="updated">12:05 PM ET</span></span>', 'cy-masthead-time')
h = ed(h, '<span class="pill" id="edition">Morning Edition</span>',
         '<span class="pill" id="edition">Midday Edition</span>', 'cy-edition')
h = ed(h, '<div class="freshline" id="freshline">Data as of 11:35 AM ET</div>',
         '<div class="freshline" id="freshline">Data as of 12:05 PM ET</div>', 'cy-freshline')

OLD_CT = ('McKesson has told the SEC it discovered a cybersecurity incident on August 25 involving third-party '
  'applications and data theft, and the ShinyHunters group claims it took roughly 284 million patient-related '
  'data records &mdash; records, not people &mdash; and demanded a $55,236,150 ransom the company did not '
  'answer; two federal remediation deadlines also expire today, Boston Scientific&rsquo;s outage is now in its '
  'fifth day with the company reporting that it has found no impact on implantable cardiac device function, '
  'and the affected-version range on the 9.8-rated Avada WordPress chain &mdash; found by an AI agent, not a '
  'person &mdash; has now been corroborated by two further vulnerability databases against the single '
  'aggregator that renders it differently.')
NEW_CT = ('McKesson has told the SEC it discovered a cybersecurity incident on August 25 involving third-party '
  'applications and data theft, and the ShinyHunters group claims it took roughly 284 million patient-related '
  'data records &mdash; records, not people &mdash; and demanded a $55,236,150 ransom the company did not '
  'answer, with the 8-K describing the investigation as still in its early stages and the company now pointing '
  'customers to a standing incident page for updates; two federal remediation deadlines also expire today, '
  'Boston Scientific&rsquo;s outage is in its fifth day with no impact found on implantable cardiac device '
  'function, and Manchester Airports Group &mdash; whose breach touched 8.7 million customers but no payment '
  'details &mdash; has now emailed those customers a phishing warning, which is the practical consequence of a '
  'breach that took contact details and nothing that can be cancelled.')
h = ed(h, OLD_CT, NEW_CT, 'cy-tldr')

# MAG card: add response + phishing warning
OLD_MAG = ('continue normally; the online <b>Manage My Booking</b> service is temporarily suspended and existing\n'
  'reservations remain valid.</p>')
NEW_MAG = ('continue normally; the online <b>Manage My Booking</b> service is temporarily suspended and existing\n'
  'reservations remain valid. <b>Newly sourced at 12:05 PM:</b> MAG says <b>passenger safety and aviation '
  'security were not affected</b>; it <b>restricted access to the affected systems</b>, brought in <b>specialist '
  'cybersecurity advisers</b> and <b>notified the relevant authorities</b>; and it has <b>emailed affected '
  'customers warning them to be alert for phishing</b>. &#9888; That last item is the one with a defender '
  'action attached: because the stolen fields are <b>contact details, vehicle registrations and postcodes</b> '
  'rather than payment data, <b>there is nothing here a customer can cancel or reissue</b> &mdash; the residual '
  'risk is <b>targeted phishing built from real booking details</b>, and it does not expire.</p>')
h = ed(h, OLD_MAG, NEW_MAG, 'cy-mag-response')

save(p, h)

# ---------------------------------------------------------------- MARKETS
p = 'wallstreet-briefing.html'
h = load(p)

h = ed(h, '<span class="pill">Updated <span id="updated">11:35 AM ET</span></span>',
         '<span class="pill">Updated <span id="updated">12:05 PM ET</span></span>', 'ws-masthead-time')
h = ed(h, '<span class="pill" id="edition">Morning Edition</span>',
         '<span class="pill" id="edition">Midday Edition</span>', 'ws-edition')
h = ed(h, '<div class="freshline" id="freshline">Data as of 11:35 AM ET</div>',
         '<div class="freshline" id="freshline">Data as of 12:05 PM ET</div>', 'ws-freshline')

OLD_WT = ('Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 '
  'slipped 0.25% to 7,711.76 and still finished the week higher &mdash; and the &ldquo;one in three&rdquo; '
  'pre-speech figure on the September rate call now has a date and an origin: reporting from mid-August puts '
  'the same reading at roughly 30% odds of a hike against a near-70% chance of a pause, after Goldman Sachs '
  'called a September move &ldquo;extremely unlikely&rdquo; &mdash; which also puts this page&rsquo;s carried, '
  'undated &ldquo;above 70% by December&rdquo; line in conflict with a dated report that December pricing had '
  'already slipped into 2027, so that line is now marked contested rather than repeated.')
NEW_WT = ('Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 '
  'slipped 0.25% to 7,711.76 and still finished the week higher, re-verified a tenth time this run &mdash; and '
  'the pre-speech September rate reading, which had rested on a single mid-August report, is now corroborated '
  'by a second and differently sourced one: a week-ahead preview fetched this run states that before Warsh '
  'spoke the odds of the Fed holding in September were nearly 70%, matching the near-70% pause already carried, '
  'while the same preview re-states the Kalshi 48% hike price for after the speech; the undated '
  '&ldquo;above 70% by December&rdquo; line stays marked contested, since corroborating the pre-speech figure '
  'does nothing to resolve the December conflict.')
h = ed(h, OLD_WT, NEW_WT, 'ws-tldr')

OLD_LEAD = ('its official closes stand unchanged, <b>re-verified a ninth time at 11:35 AM</b> against a fresh\n'
  'search returning the same three figures')
NEW_LEAD = ('its official closes stand unchanged, <b>re-verified a tenth time at 12:05 PM</b> against a fresh\n'
  'search returning the same three figures')
h = ed(h, OLD_LEAD, NEW_LEAD, 'ws-lead-tenth')

OLD_ROW = ('<b>Three reads, all pointing the same way; none adopted.</b> Before the Jackson Hole speech the odds '
  'of a September <b>hike</b> were put at <b>about one in three</b>; after it, <b>above 50/50</b>. A prediction '
  'market (Kalshi) separately prices <b>48%</b> odds of a 25bp hike in September, revised from ~70% odds of '
  '<i>no change</i>.')
NEW_ROW = ('<b>Three reads, all pointing the same way; none adopted.</b> Before the Jackson Hole speech the odds '
  'of a September <b>hike</b> were put at <b>about one in three</b>; after it, <b>above 50/50</b>. A prediction '
  'market (Kalshi) separately prices <b>48%</b> odds of a 25bp hike in September, revised from ~70% odds of '
  '<i>no change</i>. <b>Corroborated at 12:05 PM:</b> a second, differently sourced week-ahead preview states '
  'independently that before the speech the odds of the Fed <b>holding</b> in September were <b>nearly 70%</b>, '
  'and re-states the <b>Kalshi 48%</b> read &mdash; the pre-speech pair no longer rests on one report.')
h = ed(h, OLD_ROW, NEW_ROW, 'ws-rates-corroboration')

OLD_ASOF = 'Pre/post-speech pair sourced 10:50 AM; Kalshi read 9:40 AM; December read contested 11:35 AM'
NEW_ASOF = ('Pre/post-speech pair sourced 10:50 AM, <b>corroborated by a second source 12:05 PM</b>; '
  'Kalshi read 9:40 AM, re-stated 12:05 PM; December read contested 11:35 AM')
h = ed(h, OLD_ASOF, NEW_ASOF, 'ws-rates-asof')

save(p, h)

print('MISSES:', MISSES if MISSES else 'none')
