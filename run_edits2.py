import io,sys
def sub(path, old, new, count=1):
    s = io.open(path, encoding='utf-8').read()
    if s.count(old) < count:
        print("MISS in %s: %r" % (path, old[:80])); sys.exit(1)
    s = s.replace(old, new, count)
    io.open(path,'w',encoding='utf-8').write(s)

C='cyber-briefing.html'; W='wallstreet-briefing.html'; I='index.html'

sub(C, "<div class=\"stat\"><div class=\"n\">1,684</div><div class=\"l\">Poisoned versions across 420 npm package names in the keyv-linked worm campaign, per SafeDep's registry-backed count (The Hacker News)</div></div>",
      "<div class=\"stat\"><div class=\"n\">2,234</div><div class=\"l\">Poisoned versions across 444 npm package names in the keyv-linked worm campaign, per SafeDep's updated registry-backed count (SafeDep, direct fetch)</div></div>")

sub(C, 'Shai-Hulud rides again: keyv-linked npm worm poisons 1,684 package versions in half an hour — and plants Claude Code and VS Code hooks',
      'Shai-Hulud rides again: keyv-linked npm worm poisons 2,234 package versions across twelve organizations — and plants Claude Code and VS Code hooks')

sub(C, "SafeDep's registry-backed count now stands at <b>1,684 poisoned versions across 420 package names tied to nine organizations</b> — the worm hopped between organizations every two to seven minutes and completed its cross-organization publishing burst in roughly half an hour (The Hacker News, direct fetch).",
      "SafeDep's updated registry-backed count now stands at <b>2,234 poisoned versions across 444 package names spanning twelve unrelated organizations</b> — among them @ornikar, @deliveroo, @servicetitan, @qlik and Picsart — all republished between 09:35 and 13:18 UTC on August 4 (SafeDep, direct fetch this edition). Four of the core libraries — keyv, flat-cache, file-entry-cache and cacheable-request — see a combined 1,877 million monthly downloads, and flat-cache and file-entry-cache ship inside ESLint, so the reach extends to projects that never installed keyv directly.")

sub(C, '(direct fetch this edition — SafeDep 1,684/420/nine orgs update, Shai-Hulud attribution, 546 staging repos, response guidance)',
      "(Shai-Hulud attribution, 546 staging repos, response guidance; its earlier 1,684/420/nine figures are superseded by SafeDep's updated direct count this edition)")

sub(C, '<li>SafeDep — npm Worm Poisons keyv, cacheable and 400+ Other Packages (payload analysis):',
      '<li>SafeDep — npm Worm Poisons keyv, cacheable and 400+ Other Packages Across Twelve Organisations (direct fetch this edition — updated count 2,234 versions / 444 packages / twelve orgs, 09:35–13:18 UTC timeline, ESLint reach, dead-man-switch response guidance):')

# ---- WALL STREET ----
sub(W, "CNBC's session banner credited <b>Nvidia with boosting the Dow</b> as the broader rally lost momentum.",
      "CNBC's session banner credited <b>Nvidia with boosting the Dow</b> as the broader rally lost momentum. Earlier in the session the S&amp;P 500 printed a fresh all-time intraday high of <b>7,793.68</b> and the Dow was up as much as 456 points before the afternoon fade (TheStreet live blog, direct fetch this edition).", 1)

sub(W, "<p>The June IPO <b>slumped 10%, erasing its surge from the prior session</b>, as forecasts of surging AI-infrastructure spending offset its Q2 revenue beat — and with a large portion of its IPO shares soon to be released for sale by primary buyers (Trading Economics summary). It fell 7% in Tuesday's extended session after reporting 38 launches vs. 43 anticipated.</p>",
      "<p>The June IPO <b>slumped double digits, erasing its surge from the prior session</b> — reads ran from −10% on Trading Economics' summary to \"tumbling nearly 12%\" on TheStreet's live blog — as heavy AI spending and capital expenditures overshadowed its Q2 earnings beat, with a large portion of IPO shares soon to be released for sale (Trading Economics; TheStreet). TheStreet notes the stock traded below its $135 June IPO price, far off the $225.64 record it touched June 16. It fell 7% in Tuesday's extended session after reporting 38 launches vs. 43 anticipated.</p>")

sub(W, "the day's standout commodity move as yields slipped.</td>",
      "the day's standout commodity move as yields slipped. Earlier, gold futures read +1.83% at $4,228.40 and silver futures +2.59% at $61.81/oz in morning trading (TheStreet) — all point-in-time reads.</td>")

sub(W, '— and remains headline-fragile in both directions.</li>',
      '— and remains headline-fragile: Trump said Wednesday the strait would reopen "very soon" or Iran would be "hit very hard," while Iranian state media said any Iran–Oman agreement has "no connection" to reopening it, and Houthi rebels claimed a missile attack on a Saudi tanker off Yanbu that lifted crude early in the day (TheStreet live blog; CNN/Reuters via TheStreet).</li>')

sub(W, '<li>TheStreet — Stock Market Today (Aug. 5, 2026): Stocks fall after Dow notches fresh record on strong corporate earnings (session headline):',
      "<li>TheStreet — Stock Market Today (Aug. 5, 2026) live blog (direct fetch this edition — S&amp;P intraday record 7,793.68, Dow +456 intraday, SpaceX below its $135 IPO price, gold/silver morning reads, Houthi tanker attack, Trump and Iranian-state-media statements):")

# ---- INDEX ----
sub(I, '<h2>An npm worm poisons 1,684 package versions in half an hour</h2>',
      '<h2>An npm worm poisons 2,234 package versions across twelve organizations</h2>')
sub(I, 'A self-propagating credential-stealing worm in the keyv/cacheable npm family poisoned 1,684 versions of 420 packages — planting Claude Code and VS Code execution hooks —',
      "A self-propagating credential-stealing worm in the keyv/cacheable npm family has poisoned 2,234 versions of 444 packages across twelve organizations (SafeDep's updated count) — planting Claude Code and VS Code execution hooks —")

print("ALL EDITS OK")
