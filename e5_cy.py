# -*- coding: utf-8 -*-
import io
P='/tmp/db_1788305419/cyber-briefing.html'
s=io.open(P,encoding='utf-8').read(); n=0
def rep(old,new,label):
    global s,n
    c=s.count(old)
    if c!=1: print(('MISS: ' if c==0 else 'AMBIG(%d): '%c)+label); return False
    s=s.replace(old,new); n+=1; print('ok:',label); return True

# C1 -- TLDR: add the newly-sourced JFrog mechanism
rep('and the most urgent item on the page is still an elapsed one, the Citrix NetScaler flaw CVE-2026-8452, now three days past its August 29 deadline.</span></div>',
 'the JFrog Artifactory auth bypass now has a named mechanism &mdash; instances left without an additional join key are issued a &ldquo;phantom&rdquo; one that attackers forge to mint administrator credentials &mdash; '
 'and the most urgent item on the page is still an elapsed one, the Citrix NetScaler flaw CVE-2026-8452, now three days past its August 29 deadline.</span></div>',
 'C1 tldr')

# C2 -- JFrog CVE row: add the phantom join key mechanism
rep('<b>watchTowr reports exploitation observed as of September 1</b>, with attackers minting admin tokens. Not on the KEV catalog in anything fetched this run, so <b>no federal deadline applies</b>.</td>',
 '<b>watchTowr reports exploitation observed as of September 1</b>, with attackers minting admin tokens. '
 '&#9888;&#9888; <b>The mechanism is now sourced, and it changes who is exposed.</b> Instances that were never given an <b>additional join key</b> are issued a '
 '<b>&ldquo;phantom&rdquo; join key</b>, which an attacker can forge to mint <b>administrator-level credentials</b> outright. '
 '<b>That makes the risk a configuration property rather than a version property:</b> the exposed population is defined by what an operator did not set, not by which build they are running &mdash; '
 'which is why &ldquo;default configuration&rdquo; sits in the Affected column. '
 'Reporting this run notes exploitation <b>began days after public disclosure</b>, and one account raises the possibility that the scanning is being driven by '
 '<b>automated agents rather than people</b>. &#9888; <b>That last point is printed as the open question it is:</b> nothing fetched this run establishes it, '
 'and the defensive action &mdash; patch, and set a join key &mdash; is identical either way. '
 'Not on the KEV catalog in anything fetched this run, so <b>no federal deadline applies</b>.</td>',
 'C2 jfrog row')

# C3 -- Sources
rep('<h2>Sources</h2><div class="panel srcs">',
 '<h2>Sources</h2><div class="panel srcs">'
 '<a href="https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html" target="_blank" rel="noopener">The Hacker News &mdash; attackers exploit critical JFrog Artifactory flaw to mint admin tokens</a> &middot; '
 '<a href="https://www.theregister.com/security/2026/09/01/another-artifactory-cve-under-attack-by-ai-agents-or-humans/5293769" target="_blank" rel="noopener">The Register (Sept 1) &mdash; Artifactory CVE under attack</a> &middot; '
 '<a href="https://www.darkreading.com/application-security/attackers-pounce-critical-artifactory-flaw-disclosure" target="_blank" rel="noopener">Dark Reading &mdash; attackers jump on critical Artifactory flaw after disclosure</a> &middot; '
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog" target="_blank" rel="noopener">CISA &mdash; two KEV additions, Aug 31 (PaperCut pair, due Sept 14)</a> &middot; '
 '<a href="https://www.darkreading.com/vulnerabilities-threats/critical-langflow-flaw-exploited-attacks-rise" target="_blank" rel="noopener">Dark Reading &mdash; critical Langflow flaw exploited</a> &middot; ',
 'C3 sources')

io.open(P,'w',encoding='utf-8').write(s); print('applied',n)
