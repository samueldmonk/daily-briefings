#!/usr/bin/env python3
"""Fixes for the two guards that fired on validate_0940 (first pass)."""
import io, sys

D = sys.argv[1] if len(sys.argv) > 1 else "."
p = f"{D}/mma-briefing.html"
h = io.open(p, encoding="utf-8").read()

OLD = ("<b>Verification this run.</b> All six men's belts from heavyweight through featherweight were\n"
       "re-confirmed against ESPN's current-champions listing in this run &mdash; a <b>sixth consecutive edition</b> of\n"
       "agreement.")
NEW = ("<b>Verification this run.</b> All six men's belts from heavyweight through featherweight were\n"
       "re-confirmed against ESPN's current-champions listing in this run &mdash; a <b>seventh consecutive edition</b> of\n"
       "agreement, and the board is unchanged for a <b>forty-eighth consecutive edition</b>. "
       "&#9888; <b>The provenance of that check is weaker this run than last and the page says so.</b> A "
       "<b>direct fetch of ESPN's champions page returned an empty body</b>; the confirmation therefore comes from "
       "<b>search results whose leading source is that same ESPN listing</b>, which returned all six belts with "
       "<b>the winning method, event and date for each</b> &mdash; Aspinall (inherited, June 21 2025), Ulberg "
       "(KO1 Proch&aacute;zka, UFC 327, April 11 2026), Strickland (split decision over Chimaev, UFC 328, May 9 "
       "2026), Makhachev (UD over Della Maddalena, UFC 322, November 15 2025, 1 defence), Gaethje (TKO4 Topuria, "
       "Freedom 250, June 14 2026) and Volkanovski (UD over Lopes, UFC 314, April 12 2025, 1 defence) &mdash; "
       "every one matching the standing record exactly. <b>A snippet-mediated read of the primary source is not "
       "the same as reading it, and is recorded as the weaker check it is.</b> "
       "<b>UFC Shanghai carried no title bout, so no belt could move on it.</b>")
if OLD not in h:
    raise SystemExit("fix_0940: ESPN verification anchor missing")
h = h.replace(OLD, NEW, 1)
io.open(p, "w", encoding="utf-8").write(h)
print("fix_0940: OK")
